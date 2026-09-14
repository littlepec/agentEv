"""Paper-round engineering contract (extends the calibration's fixed_contract with the 3 offline
closeouts the user required). Separate module so gptr_round calibration stays reproducible.

Closeout 1 — provider logging is COMPLETE (no 4000/6000 char truncation); a truncated PREVIEW is
             saved to a SEPARATE file by the runner.
Closeout 2 — empty Content does NOT merely get flagged: empty-Content items are routed into a
             predefined no-evidence path (dropped from curated list; if nothing remains, a
             NO_EVIDENCE state is raised to the runner, which records it as a defined outcome and
             does NOT count the cell as a grounded completion).
Closeout 3 — source ids/order come from a PRE-STORED STABLE MAPPING keyed by (task, role) only,
             identical across R0/R1 and across paired conditions (E / E+L / E+L'). No hash(cell)
             or arm in the layout.
Only retriever selection + curated-key normalization + logging are patched; pinned package untouched.
"""
from __future__ import annotations
import json, pathlib, shutil

# ---- Closeout 3: stable (task,role)->neutral id mapping; fixed order, no arm/cell/rep, no shuffle ----
# Every condition places the paper evidence first and the third-party interpretation second, so E,
# E+L and E+L' differ ONLY in document_2's bytes; R0 and R1 see identical layouts.
ROLE_ORDER = ["evidence", "interp"]        # evidence=E (paper), interp=L or L'
ROLE_TO_DOCID = {"evidence": "document_1.txt", "interp": "document_2.txt"}

def stable_docpath(role_files: dict, out_dir: pathlib.Path):
    """role_files: {role: src_path} for the roles present in this condition (E has only 'evidence';
    E+L / E+L' also have 'interp'). Returns (out_dir, mapping role->docid). Deterministic: identical
    inputs -> identical layout, independent of arm/rep/condition-name."""
    if out_dir.exists(): shutil.rmtree(out_dir)
    out_dir.mkdir(parents=True)
    mapping = {}
    for role in ROLE_ORDER:
        if role in role_files:
            docid = ROLE_TO_DOCID[role]
            shutil.copy(role_files[role], out_dir / docid)
            mapping[role] = docid
    return out_dir, mapping

# ---- Closeout 2: curated-key normalization + empty-Content -> predefined no-evidence path ----
class CurationContractError(Exception): ...
_CUR_SINK = {"path": None, "state": None}   # state dict filled per cell: {total, dropped_empty, no_evidence}

def _normalize_item(d):
    if not isinstance(d, dict):
        return {"Source": "", "Title": "", "Content": str(d)}
    out = {}
    for cap, low in [("Source", "source"), ("Title", "title"), ("Content", "content")]:
        hv, lv = d.get(cap), d.get(low)
        if hv is not None and lv is not None and str(hv) != str(lv):
            raise CurationContractError(f"key case conflict on {cap}/{low}: {hv!r} != {lv!r}")
        out[cap] = hv if hv is not None else (lv if lv is not None else "")
    return out

def normalize_curated(curated):
    """Return (kept_items, state). Empty-Content items are DROPPED (not passed as shells).
    state.no_evidence=True if nothing usable remains -> predefined no-evidence handling."""
    if not isinstance(curated, list):
        return curated, {"total": None, "dropped_empty": 0, "no_evidence": not bool(str(curated).strip())}
    kept, dropped = [], 0
    for d in curated:
        nd = _normalize_item(d)
        if str(nd["Content"]).strip():
            kept.append(nd)
        else:
            dropped += 1
    return kept, {"total": len(curated), "dropped_empty": dropped, "no_evidence": len(kept) == 0}

def install_curation_field_fix():
    import gpt_researcher.skills.curator as cur
    orig = cur.SourceCurator.curate_sources
    async def wrap(self, source_data, *a, **k):
        out = await orig(self, source_data, *a, **k)
        kept, state = normalize_curated(out)
        try:
            if _CUR_SINK["path"]:
                pathlib.Path(_CUR_SINK["path"]).write_text(json.dumps(
                    {"raw": source_data if isinstance(source_data, list) else str(source_data),
                     "curated_raw": out, "curated_kept": kept, "state": state},
                    ensure_ascii=False, indent=2, default=str), encoding="utf-8")
        except Exception: pass
        if _CUR_SINK["state"] is not None:
            _CUR_SINK["state"].clear(); _CUR_SINK["state"].update(state)
        return kept
    cur.SourceCurator.curate_sources = wrap

# ---- Closeout 1: provider logger with FULL content (no truncation); preview saved separately ----
def make_provider_logger():
    try:
        from langchain_core.callbacks import BaseCallbackHandler
    except Exception:
        return None, None
    class ProviderLogger(BaseCallbackHandler):
        def __init__(self): self.calls = []
        def _msgs(self, messages):
            out = []
            for group in (messages or []):
                for m in (group or []):
                    out.append({"type": getattr(m, "type", m.__class__.__name__),
                                "content": (getattr(m, "content", "") or "")})   # FULL, no truncation
            return out
        def on_chat_model_start(self, serialized, messages, **kw):
            self.calls.append({"phase": "start", "messages": self._msgs(messages)})
        def on_llm_end(self, response, **kw):
            gens = []
            try:
                for gg in response.generations:
                    for g in gg:
                        info = getattr(g, "generation_info", None) or {}
                        msg = getattr(g, "message", None)
                        text = getattr(g, "text", "") or (getattr(msg, "content", "") if msg else "")
                        gens.append({"text": (text or ""), "finish": info.get("finish_reason")})  # FULL
            except Exception as e:
                gens = [{"err": str(e)}]
            usage = None
            try: usage = response.llm_output.get("token_usage") if response.llm_output else None
            except Exception: pass
            self.calls.append({"phase": "end", "generations": gens, "token_usage": usage})
    try:
        from langchain_core.tracers.context import register_configure_hook
        import contextvars
        var = contextvars.ContextVar("paper_provider_logger", default=None)
        register_configure_hook(var, True)
        return ProviderLogger, var
    except Exception:
        return ProviderLogger, None

def save_provider_logs(calls, full_path, preview_path, preview_chars=800):
    """Closeout 1: full log to full_path; a separate truncated preview to preview_path."""
    pathlib.Path(full_path).write_text(json.dumps(calls, ensure_ascii=False, indent=2, default=str), encoding="utf-8")
    def trunc(x):
        if isinstance(x, dict): return {k: trunc(v) for k, v in x.items()}
        if isinstance(x, list): return [trunc(v) for v in x]
        if isinstance(x, str) and len(x) > preview_chars: return x[:preview_chars] + f"...[+{len(x)-preview_chars} chars]"
        return x
    pathlib.Path(preview_path).write_text(json.dumps(trunc(calls), ensure_ascii=False, indent=2, default=str), encoding="utf-8")
