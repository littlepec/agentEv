#!/usr/bin/env python3
"""Stage C: strong simple baselines on the FROZEN stage B materials (paper_round/stage_b/tasks, sha in tasks_manifest_b.json).
Variants (all F0 = no curation; host/model/config otherwise as stage A/B):
  eonly   : document_1 (full paper) only, default retrieval  -> C-0 mechanism check (is the paper visible without the note?)
  fullwin : documents placed DIRECTLY in the model input via the host's own fast path (COMPRESSION_THRESHOLD raised so no
            embedding gate is applied)                        -> C-1 "full paper in the window" baseline (roadmap §5.1)
  ranked  : retrieval gate replaced by top-10 chunks ranked by cosine similarity (runtime patch of the compressor; pinned
            package untouched)                                -> C-2 cheaper engineering knob (secondary)
Ledger: exp_key evidence-package-pilot-stageC; stage cap = line cost at stage-C start + $0.60; per-variant caps enforced.
Usage: python run_stage_c.py --variant fullwin --tasks B3 --conds C --phase feasibility
       python run_stage_c.py --variant eonly --tasks B1,B2,B3,B4 --conds E --phase confirmatory
       python run_stage_c.py --dry"""
from __future__ import annotations
import os, sys, json, time, asyncio, pathlib, argparse, sqlite3
ROOT = pathlib.Path(__file__).resolve().parent; PR = ROOT.parent; SB = PR / "stage_b"
RUNS = ROOT / "runs_c"; DOCP = ROOT / "docpaths_c"; RUNS.mkdir(exist_ok=True); DOCP.mkdir(exist_ok=True)
KEY = pathlib.Path("F:/defense/research_v1/.deepseek_key").read_text(encoding="utf-8").strip()
sys.path.insert(0, "F:/defense/evidence_pack_prep_v1"); sys.path.insert(0, str(PR))
from ledger_guard import BudgetGuard, LEDGER
import contract as C, offline_retriever
os.environ["OPENAI_API_KEY"] = KEY; os.environ["OPENAI_BASE_URL"] = "https://api.deepseek.com"
os.environ["FAST_LLM"] = os.environ["SMART_LLM"] = os.environ["STRATEGIC_LLM"] = "openai:deepseek-v4-flash"
os.environ["EMBEDDING"] = "huggingface:sentence-transformers/all-MiniLM-L6-v2"
os.environ["REPORT_SOURCE"] = "local"; os.environ["RETRIEVER"] = "offline_null"; os.environ["TEMPERATURE"] = "0.4"
os.environ.setdefault("TOKENIZERS_PARALLELISM", "false")
IN_RATE, OUT_RATE = 0.30 / 1_000_000, 1.20 / 1_000_000
EXP_KEY, PREFIX, LINE_CAP = "evidence-package-pilot-stageC", "evidence-package-pilot", 10.0
STAGE_SUBCAP = 0.60 + 0.35   # step 1 (PREREG_stage_c.md, $0.60; actual $0.4167) + step 2 (PREREG_stage_c5.md, $0.35, pre-registered
                             # before any C-5 cell ran). Per-variant caps below enforce each step's own limits.
VARIANT_CAP = {"eonly": 0.06, "fullwin": 0.25, "ranked": 0.15, "default_rep2": 0.08, "fullwin_rep2": 0.12,
               "ranked_rep2": 0.12, "ranked_rep3": 0.12, "ranked_dedup": 0.14, "ranked_F1": 0.09}   # C-5 (PREREG_stage_c5.md)
# ranked_rep2 + ranked_rep3 share ONE pre-registered sub-budget ($0.12): spent is summed over the group (see variant_spent).
CAP_GROUP = {"ranked_rep2": "ranked_rep", "ranked_rep3": "ranked_rep"}
RES = {"eonly": 0.03, "fullwin": 0.06, "ranked": 0.03, "default_rep2": 0.03, "fullwin_rep2": 0.06,
       "ranked_rep2": 0.015, "ranked_rep3": 0.015, "ranked_dedup": 0.015, "ranked_F1": 0.02}   # measured means (deviation note 2)
RES["fullwin_rep2"] = 0.03   # deviation note 2026-09-15: reservation lowered to the measured cost (0.018-0.030/flow) after the
                             # $0.06 reservation blocked B4_P_fullwin_rep2 at $0.066 spent; the pre-registered sub-budget ($0.12) is unchanged.
VARIANT_ARM = {"ranked_F1": "true"}   # every other variant runs F0 (no curation)
_SEEN_CHUNKS: set = set()             # ranked_dedup: chunk texts already emitted in the current cell
# C-4 replication (PREREG_stage_c4.md): default_rep2 = stage-B default retrieval (gate 0.42) re-run once;
# fullwin_rep2 = C-1 configuration re-run once. Same frozen materials; separate cell names so nothing is overwritten.
COND_ROLES = {"E": {"evidence": "E_fulltext.txt"},
              "C": {"evidence": "E_fulltext.txt", "interp": "L.txt"},
              "P": {"evidence": "E_fulltext.txt", "interp": "Lprime.txt"}}
PAPER_KEY = {"B1": ["220 human-human dialogs"], "B2": ["35.55", "37.57"], "B3": ["hand-craft 163", "163 templates"], "B4": ["consist of 6 layers", "6 layers which"]}
ALL_TASKS = ["B1", "B2", "B3", "B4"]

def qtext(t): return json.loads((SB / "tasks" / t / "private_eval.json").read_text(encoding="utf-8"))["question"]
def get_cb():
    from langchain_community.callbacks.manager import get_openai_callback; return get_openai_callback
def cell_id(cell):
    mp = RUNS / "cell_map.json"; m = json.loads(mp.read_text(encoding="utf-8")) if mp.exists() else {}
    if cell not in m: m[cell] = f"cell_{len(m)+1:02d}"; mp.write_text(json.dumps(m, indent=2), encoding="utf-8")
    return m[cell]
def build_docpath(t, cond, cell):
    role_files = {role: SB / "tasks" / t / fn for role, fn in COND_ROLES[cond].items()}
    return C.stable_docpath(role_files, DOCP / cell_id(cell))

# ---- variant switches (applied per cell; reverted after) ----
_ORIG_RETRIEVER = None; _ORIG_PPD = None
def apply_variant(variant):
    global _ORIG_RETRIEVER, _ORIG_PPD
    import gpt_researcher.context.compression as CM
    import gpt_researcher.prompts as PM
    if _ORIG_RETRIEVER is None: _ORIG_RETRIEVER = CM.ContextCompressor._ContextCompressor__get_contextual_retriever
    if _ORIG_PPD is None: _ORIG_PPD = PM.PromptFamily.__dict__["pretty_print_docs"]   # staticmethod object
    os.environ["COMPRESSION_THRESHOLD"] = "400000" if variant in ("fullwin", "fullwin_rep2") else "8000"   # host default is 8000
    _SEEN_CHUNKS.clear()
    if variant == "ranked_dedup":
        orig_fn = _ORIG_PPD.__func__
        def _ppd_dedup(docs, top_n=None):
            kept = []
            for d in docs:
                key = (d.metadata.get("source"), d.page_content.strip())
                if key in _SEEN_CHUNKS: continue
                _SEEN_CHUNKS.add(key); kept.append(d)
            return orig_fn(kept, top_n)
        PM.PromptFamily.pretty_print_docs = staticmethod(_ppd_dedup)
    else:
        PM.PromptFamily.pretty_print_docs = _ORIG_PPD
    if variant.startswith("ranked"):
        from langchain_classic.retrievers import ContextualCompressionRetriever
        from langchain_classic.retrievers.document_compressors import DocumentCompressorPipeline, EmbeddingsFilter
        from langchain_text_splitters import RecursiveCharacterTextSplitter
        from gpt_researcher.context.retriever import SearchAPIRetriever
        def _ranked(self):
            splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
            relevance_filter = EmbeddingsFilter(embeddings=self.embeddings, k=10, similarity_threshold=None)  # top-10 by cosine, no gate
            pipeline = DocumentCompressorPipeline(transformers=[splitter, relevance_filter])
            return ContextualCompressionRetriever(base_compressor=pipeline, base_retriever=SearchAPIRetriever(pages=self.documents))
        CM.ContextCompressor._ContextCompressor__get_contextual_retriever = _ranked
    else:
        CM.ContextCompressor._ContextCompressor__get_contextual_retriever = _ORIG_RETRIEVER

def variant_spent(variant):
    c = sqlite3.connect(str(LEDGER), timeout=30)
    pat = f'%"variant": "{CAP_GROUP[variant]}%' if variant in CAP_GROUP else f'%"variant": "{variant}"%'
    v = c.execute("select coalesce(sum(cost),0) from calls where exp_key=? and data like ?", (EXP_KEY, pat)).fetchone()[0]
    c.close(); return float(v)

def stage_cap():
    bpath = RUNS / "ledger_baseline.json"
    if bpath.exists(): base = json.loads(bpath.read_text(encoding="utf-8"))["line_cost_at_stageC_start"]
    else:
        g = BudgetGuard(EXP_KEY, exp_prefix=PREFIX, call_cap=10**6); base = g._totals()[0]
        bpath.write_text(json.dumps({"line_cost_at_stageC_start": base, "created": time.strftime("%Y-%m-%dT%H:%M:%S")}, indent=2), encoding="utf-8")
    return round(min(LINE_CAP, base + STAGE_SUBCAP), 4)

async def dry(cells):
    from gpt_researcher.document.document import DocumentLoader
    for (t, cond, variant) in cells:
        cell = f"{t}_{cond}_{variant}"; dp, mapping = build_docpath(t, cond, cell)
        docs = await DocumentLoader(str(dp)).load()
        print(f"{cell} -> {cell_id(cell)} docs={[d.get('url') for d in docs]} chars={[len(d.get('raw_content','')) for d in docs]}", flush=True)
    print("DRY DONE", flush=True)

async def run_cell(t, cond, variant, phase, guard, gcb, PL, pvar):
    cell = f"{t}_{cond}_{variant}"; cdir = RUNS / cell; cdir.mkdir(exist_ok=True)
    if (cdir / "meta.json").exists() and json.loads((cdir / "meta.json").read_text(encoding="utf-8")).get("done"): return "skip"
    if variant_spent(variant) + RES[variant] > VARIANT_CAP[variant]:
        print(f"{cell}: STOP variant cap {VARIANT_CAP[variant]} (spent ${variant_spent(variant):.4f})", flush=True); return "stop"
    ok, why = guard.preflight(RES[variant], int(RES[variant] / OUT_RATE))
    if not ok: print(f"{cell}: {why}", flush=True); return "stop"
    dp, mapping = build_docpath(t, cond, cell)
    arm = VARIANT_ARM.get(variant, "false")
    os.environ["DOC_PATH"] = str(dp); os.environ["CURATE_SOURCES"] = arm
    C._CUR_SINK["path"] = str(cdir / "curation.json") if arm == "true" else None
    C._CUR_SINK["state"] = {} if arm == "true" else None
    apply_variant(variant); offline_retriever.install_offline_retriever()
    from gpt_researcher import GPTResearcher
    plog = PL() if PL else None
    if plog is not None and pvar is not None: pvar.set(plog)
    t0 = time.time(); pt = ct = 0; report = ""; ctx = None; err = None
    try:
        r = GPTResearcher(query=qtext(t), report_type="research_report", report_source="local")
        with gcb() as cb:
            await r.conduct_research(); report = await r.write_report()
        pt, ct = cb.prompt_tokens, cb.completion_tokens; ctx = r.context
        (cdir / "report.md").write_text(report or "", encoding="utf-8")
        (cdir / "context.txt").write_text(ctx if isinstance(ctx, str) else json.dumps(ctx, ensure_ascii=False, default=str), encoding="utf-8")
        if plog is not None: C.save_provider_logs(plog.calls, cdir / "provider_log.json", cdir / "provider_log_preview.json")
    except Exception as e:
        err = f"{type(e).__name__}: {e}"; print(f"{cell}: ERR {err}", flush=True)
    finally:
        apply_variant("eonly")   # revert patches / env
    cost = pt * IN_RATE + ct * OUT_RATE
    guard.record(cost, pt, ct, data={"stage": "stageC", "variant": variant, "phase": phase, "cell": cell}, est_cost=RES[variant], est_out=int(RES[variant] / OUT_RATE))
    ctxs = (ctx if isinstance(ctx, str) else json.dumps(ctx, ensure_ascii=False, default=str)) or ""
    st = dict(C._CUR_SINK["state"]) if (arm == "true" and C._CUR_SINK["state"] is not None) else None
    meta = {"cell": cell, "docpath_dir": cell_id(cell), "task": t, "condition": cond, "variant": variant, "arm": ("F1" if arm == "true" else "F0"), "phase": phase,
            "curation_state": st,
            "docpath_mapping": mapping, "question": qtext(t), "prompt_tokens": pt, "completion_tokens": ct, "deepseek_cost_usd": round(cost, 6),
            "report_chars": len(report or ""), "context_chars": len(ctxs), "doc1_blocks": ctxs.count("Source: document_1.txt"), "doc2_blocks": ctxs.count("Source: document_2.txt"),
            "paper_decisive_in_context": any(k.lower() in ctxs.lower() for k in PAPER_KEY[t]),
            "n_llm_calls": sum(1 for c2 in (plog.calls if plog else []) if c2.get("phase") == "start"),
            "elapsed_s": round(time.time() - t0, 1), "error": err, "done": err is None,
            "host": "gpt-researcher v3.6.1 (6f998577) fixed-contract, stage A config + variant", "model": "deepseek-v4-flash",
            "materials_manifest": "paper_round/stage_b/tasks_manifest_b.json"}
    (cdir / "meta.json").write_text(json.dumps(meta, ensure_ascii=False, indent=2), encoding="utf-8")
    with (RUNS / "stageC_results.jsonl").open("a", encoding="utf-8") as f: f.write(json.dumps(meta, ensure_ascii=False) + "\n")
    print(f"{cell}: {'ok' if not err else 'error'} calls={meta['n_llm_calls']} in={pt} out={ct} ${cost:.4f} rep={len(report or '')} ctx={len(ctxs)} "
          f"doc1={meta['doc1_blocks']} doc2={meta['doc2_blocks']} paper_decisive={meta['paper_decisive_in_context']}", flush=True)
    return "ok" if not err else "error"

async def main(args):
    variants = args.variant.split(","); tasks = args.tasks.split(","); conds = args.conds.split(",")
    cells = [(t, c, v) for v in variants for t in tasks for c in conds]
    if args.dry: await dry(cells); return
    C.install_curation_field_fix(); PL, pvar = C.make_provider_logger(); gcb = get_cb()
    guard = BudgetGuard(EXP_KEY, exp_prefix=PREFIX, call_cap=10**6, in_tok_cap=80_000_000, out_tok_cap=30_000_000)
    guard.cost_cap = stage_cap(); cur, calls, *_ = guard._totals()
    print(f"COST ACCOUNTING: pilot* cum=${cur:.4f} ({calls} calls); stage-C cap=${guard.cost_cap}; variant caps={VARIANT_CAP}; phase={args.phase}", flush=True)
    for (t, c, v) in cells:
        st = await run_cell(t, c, v, args.phase, guard, gcb, PL, pvar)
        if st == "stop": print("STOP (budget)", flush=True); break
    cur, calls, *_ = guard._totals(); print(f"STAGE C BATCH DONE: pilot* cum=${cur:.4f} ({calls} calls)", flush=True)

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--variant", default="eonly"); ap.add_argument("--tasks", default=",".join(ALL_TASKS)); ap.add_argument("--conds", default="E")
    ap.add_argument("--phase", default="confirmatory"); ap.add_argument("--dry", action="store_true")
    asyncio.run(main(ap.parse_args()))
