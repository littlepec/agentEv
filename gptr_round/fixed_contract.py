"""ENGINEERING-CONTRACT FIX (fixed version; NOT a new method) for the audit's two confounds.
Kept separate from the original run_round.py. Provides:
 1) neutral_docpath(): DOC_PATH files with NEUTRAL ids that do NOT encode true/false or role
    (document_1.txt, document_2.txt, shuffled), removing the filename-leak confound.
 2) install_curation_field_fix(): normalize curate_sources() output keys to the documented
    {Source,Title,Content} schema, ERROR on case-conflict, and FLAG empty Content (an empty body
    must not be masked by a Title placeholder). Fixes the field-name-mismatch -> empty-shell bug.
 3) ProviderLogger: log every LLM call's request (messages) + response + finish status per cell.
Reuses offline_retriever (no web). All are runtime patches; pinned package on disk untouched.
"""
from __future__ import annotations
import json, pathlib, shutil, random

# ---- (1) neutral source ids ----
def neutral_docpath(task_dir: pathlib.Path, cond: str, out_dir: pathlib.Path, seed: int):
    """Build DOC_PATH with neutral filenames; return (dir, mapping) where mapping (role->neutral name)
    is returned for PRIVATE logging only (never enters the model input)."""
    if out_dir.exists(): shutil.rmtree(out_dir)
    out_dir.mkdir(parents=True)
    items = [("normal", task_dir/"normal"/"normal_sources.txt")]
    if cond == "harmless": items.append(("harmless", task_dir/"harmless_supplement.txt"))
    elif cond == "error":  items.append(("error", task_dir/"error_material.txt"))
    rng = random.Random(seed)
    order = items[:]; rng.shuffle(order)
    mapping = {}
    for i, (role, src) in enumerate(order, 1):
        neutral = f"document_{i}.txt"
        shutil.copy(src, out_dir/neutral)
        mapping[role] = neutral
    return out_dir, mapping

# ---- (2) curated-list field normalization + empty-body guard ----
class CurationContractError(Exception): ...

_CUR_SINK = {"path": None, "flags": None}

def _normalize_item(d):
    if not isinstance(d, dict): return {"Source":"","Title":"","Content":str(d)}, {"nondict":True}
    out = {}; flags = {}
    for cap, low in [("Source","source"),("Title","title"),("Content","content")]:
        hv = d.get(cap); lv = d.get(low)
        if hv is not None and lv is not None and str(hv) != str(lv):
            raise CurationContractError(f"key case conflict on {cap}/{low}: {hv!r} != {lv!r}")
        out[cap] = (hv if hv is not None else (lv if lv is not None else ""))
    if not str(out["Content"]).strip():
        flags["empty_content"] = True   # must NOT be silently masked by a Title placeholder
    return out, flags

def install_curation_field_fix():
    import gpt_researcher.skills.curator as cur
    orig = cur.SourceCurator.curate_sources
    async def wrap(self, source_data, *a, **k):
        out = await orig(self, source_data, *a, **k)
        if isinstance(out, list):
            norm = []; allflags = []
            for d in out:
                nd, fl = _normalize_item(d); norm.append(nd)
                if fl: allflags.append(fl)
            try:
                if _CUR_SINK["path"]:
                    pathlib.Path(_CUR_SINK["path"]).write_text(
                        json.dumps({"raw": source_data if isinstance(source_data,list) else str(source_data),
                                    "curated_raw": out, "curated_normalized": norm,
                                    "empty_content_items": sum(1 for f in allflags if f.get("empty_content")),
                                    "total_items": len(norm)}, ensure_ascii=False, indent=2, default=str),
                        encoding="utf-8")
            except Exception: pass
            if _CUR_SINK["flags"] is not None:
                _CUR_SINK["flags"].clear()
                _CUR_SINK["flags"].update({"empty_content_items": sum(1 for f in allflags if f.get("empty_content")),
                                           "total_items": len(norm)})
            return norm   # capitalized keys -> researcher.py s.get("Title"/...) now maps
        return out
    cur.SourceCurator.curate_sources = wrap

# ---- (3) provider request/response/finish logging ----
def make_provider_logger():
    try:
        from langchain_core.callbacks import BaseCallbackHandler
    except Exception:
        return None, None
    class ProviderLogger(BaseCallbackHandler):
        def __init__(self): self.calls = []
        def _msgs(self, messages):
            out=[]
            for group in (messages or []):
                for m in (group or []):
                    out.append({"type": getattr(m,"type",m.__class__.__name__),
                                "content": (getattr(m,"content","") or "")[:4000]})
            return out
        def on_chat_model_start(self, serialized, messages, **kw):
            self.calls.append({"phase":"start","messages":self._msgs(messages)})
        def on_llm_end(self, response, **kw):
            gens=[]
            try:
                for gg in response.generations:
                    for g in gg:
                        info = getattr(g,"generation_info",None) or {}
                        text = getattr(g,"text","") or (getattr(getattr(g,"message",None),"content","") if getattr(g,"message",None) else "")
                        gens.append({"text":(text or "")[:6000],"finish":info.get("finish_reason")})
            except Exception as e:
                gens=[{"err":str(e)}]
            usage=None
            try: usage=response.llm_output.get("token_usage") if response.llm_output else None
            except Exception: pass
            self.calls.append({"phase":"end","generations":gens,"token_usage":usage})
    try:
        from langchain_core.tracers.context import register_configure_hook
        import contextvars
        var = contextvars.ContextVar("provider_logger", default=None)
        register_configure_hook(var, True)
        return ProviderLogger, var
    except Exception:
        return ProviderLogger, None
