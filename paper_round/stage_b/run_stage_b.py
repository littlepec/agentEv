#!/usr/bin/env python3
"""Stage B first batch: 4 tasks x {C: E+L, P: E+L'} x {F0: default, F1: original SourceCurator} = 16 flows.
Frozen host/config as stage A (GPT-Researcher v3.6.1 6f998577, deepseek-v4-flash, temp 0.4, local HF embedding,
offline_null retriever, long report) + fixed contract (stable neutral doc ids, curated-key fix, full provider log).
document_1.txt = FULL paper (E, never modified); document_2.txt = third-party note (L or L').
Ledger: exp_key evidence-package-pilot-stageB; stage-B sub-budget cap = prep baseline + $0.50 (min $10 line cap);
one task block (4 flows) is not started unless the reserve fits. Eval labels stay private; scoring is separate.
Usage: python run_stage_b.py --dry   (build docpaths + load documents, no LLM)   |   python run_stage_b.py"""
from __future__ import annotations
import os, sys, json, time, asyncio, pathlib, hashlib
ROOT = pathlib.Path(__file__).resolve().parent; PR = ROOT.parent
RUNS = ROOT / "runs_b"; DOCP = ROOT / "docpaths_b"; RUNS.mkdir(exist_ok=True); DOCP.mkdir(exist_ok=True)
KEY = pathlib.Path("F:/defense/research_v1/.deepseek_key").read_text(encoding="utf-8").strip()
sys.path.insert(0, "F:/defense/evidence_pack_prep_v1"); sys.path.insert(0, str(PR))
from ledger_guard import BudgetGuard
import contract as C, offline_retriever
os.environ["OPENAI_API_KEY"] = KEY; os.environ["OPENAI_BASE_URL"] = "https://api.deepseek.com"
os.environ["FAST_LLM"] = os.environ["SMART_LLM"] = os.environ["STRATEGIC_LLM"] = "openai:deepseek-v4-flash"
os.environ["EMBEDDING"] = "huggingface:sentence-transformers/all-MiniLM-L6-v2"
os.environ["REPORT_SOURCE"] = "local"; os.environ["RETRIEVER"] = "offline_null"; os.environ["TEMPERATURE"] = "0.4"
os.environ.setdefault("TOKENIZERS_PARALLELISM", "false")
IN_RATE, OUT_RATE = 0.30 / 1_000_000, 1.20 / 1_000_000
TASKS = ["B3", "B4", "B2", "B1"]                      # short papers first; every task is a complete block of 4
COND_ROLES = {"C": {"evidence": "E_fulltext.txt", "interp": "L.txt"}, "P": {"evidence": "E_fulltext.txt", "interp": "Lprime.txt"}}
ARMS = {"F0": "false", "F1": "true"}
RES = {"F0": 0.03, "F1": 0.05}                         # per-flow reservation (stage A measured ~$0.012 for F0)
EXP_KEY, PREFIX, STAGE_SUBCAP, LINE_CAP = "evidence-package-pilot-stageB", "evidence-package-pilot", 0.50, 10.0
CELLS = [(t, c, a) for t in TASKS for c in COND_ROLES for a in ARMS]
CELL_ID = {cell: f"cell_{i+1:02d}" for i, cell in enumerate(CELLS)}   # neutral docpath dir names (private map)

def qtext(t): return json.loads((ROOT / "tasks" / t / "private_eval.json").read_text(encoding="utf-8"))["question"]
def sha(s): return hashlib.sha256(s.encode("utf-8")).hexdigest()
def get_cb():
    from langchain_community.callbacks.manager import get_openai_callback; return get_openai_callback

def build_docpath(t, cond, arm):
    role_files = {role: ROOT / "tasks" / t / fn for role, fn in COND_ROLES[cond].items()}
    dp, mapping = C.stable_docpath(role_files, DOCP / CELL_ID[(t, cond, arm)])
    return dp, mapping

def stage_cap(guard):
    bpath = ROOT / "gen_runs" / "ledger_baseline.json"
    baseline = json.loads(bpath.read_text(encoding="utf-8"))["line_cost_at_prep_start"]
    return round(min(LINE_CAP, baseline + STAGE_SUBCAP), 4)

async def dry():
    (RUNS / "cell_map.json").write_text(json.dumps({v: {"task": k[0], "cond": k[1], "arm": k[2]} for k, v in CELL_ID.items()}, indent=2), encoding="utf-8")
    from gpt_researcher.document.document import DocumentLoader
    for (t, cond, arm) in CELLS:
        dp, mapping = build_docpath(t, cond, arm)
        docs = await DocumentLoader(str(dp)).load()
        urls = sorted({d.get("url") for d in docs}); chars = {d.get("url"): len(d.get("raw_content", "")) for d in docs}
        leak = [u for u in urls if any(x in str(u) for x in ("L.txt", "Lprime", "E_fulltext", "_C_", "_P_", "F0", "F1", "cell_"))]
        print(f"{t} {cond} {arm} -> {CELL_ID[(t,cond,arm)]} docs={len(docs)} urls={urls} chars={chars} leak={leak}", flush=True)
    print("DRY DONE (no LLM calls)", flush=True)

async def run_cell(t, cond, arm, guard, gcb, PL, pvar):
    cell = f"{t}_{cond}_{arm}"; cdir = RUNS / cell; cdir.mkdir(exist_ok=True)
    if (cdir / "meta.json").exists() and json.loads((cdir / "meta.json").read_text(encoding="utf-8")).get("done"): return "skip"
    ok, why = guard.preflight(RES[arm], int(RES[arm] / OUT_RATE))
    if not ok: print(f"{cell}: {why}", flush=True); return "stop"
    dp, mapping = build_docpath(t, cond, arm)
    os.environ["DOC_PATH"] = str(dp); os.environ["CURATE_SOURCES"] = ARMS[arm]
    C._CUR_SINK["path"] = str(cdir / "curation.json") if arm == "F1" else None
    C._CUR_SINK["state"] = {} if arm == "F1" else None
    offline_retriever.install_offline_retriever()
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
    cost = pt * IN_RATE + ct * OUT_RATE
    guard.record(cost, pt, ct, data={"stage": "stageB-run", "cell": cell}, est_cost=RES[arm], est_out=int(RES[arm] / OUT_RATE))
    st = dict(C._CUR_SINK["state"]) if (arm == "F1" and C._CUR_SINK["state"] is not None) else None
    ctxs = (ctx if isinstance(ctx, str) else json.dumps(ctx, ensure_ascii=False, default=str)) or ""
    interp_text = (ROOT / "tasks" / t / COND_ROLES[cond]["interp"]).read_text(encoding="utf-8")
    kq = [l for l in interp_text.splitlines() if l.startswith("Key questions addressed:")]
    meta = {"cell": cell, "docpath_dir": CELL_ID[(t, cond, arm)], "task": t, "condition": cond, "arm": arm, "curate_sources": ARMS[arm],
            "docpath_mapping": mapping, "question": qtext(t), "prompt_tokens": pt, "completion_tokens": ct,
            "deepseek_cost_usd": round(cost, 6), "report_chars": len(report or ""), "context_chars": len(ctxs),
            "n_llm_calls": sum(1 for c2 in (plog.calls if plog else []) if c2.get("phase") == "start"),
            "interp_header_in_context": (kq[0].lower() in ctxs.lower()) if kq else None,
            "interp_sha256": sha(interp_text), "curation_state": st, "no_evidence_after_curation": (st or {}).get("no_evidence"),
            "elapsed_s": round(time.time() - t0, 1), "error": err, "done": err is None,
            "host": "gpt-researcher v3.6.1 (6f998577) fixed-contract, stage A config", "model": "deepseek-v4-flash"}
    (cdir / "meta.json").write_text(json.dumps(meta, ensure_ascii=False, indent=2), encoding="utf-8")
    with (RUNS / "stageB_results.jsonl").open("a", encoding="utf-8") as f: f.write(json.dumps(meta, ensure_ascii=False) + "\n")
    print(f"{cell}: {'ok' if not err else 'error'} calls={meta['n_llm_calls']} in={pt} out={ct} ${cost:.4f} rep={len(report or '')} "
          f"ctx={len(ctxs)} interp_in_ctx={meta['interp_header_in_context']} no_ev={meta['no_evidence_after_curation']}", flush=True)
    return "ok" if not err else "error"

async def main():
    C.install_curation_field_fix(); PL, pvar = C.make_provider_logger(); gcb = get_cb()
    guard = BudgetGuard(EXP_KEY, exp_prefix=PREFIX, call_cap=520, in_tok_cap=50_000_000, out_tok_cap=20_000_000)
    guard.cost_cap = stage_cap(guard)
    cur, calls, *_ = guard._totals()
    block = sum(RES[a] for a in ARMS) * len(COND_ROLES)
    print(f"COST ACCOUNTING: pilot* cum=${cur:.4f} ({calls} calls); stage-B cap=${guard.cost_cap}; per-block reserve=${block:.3f}; headroom=${guard.cost_cap-cur:.4f}", flush=True)
    for t in TASKS:
        cur, *_ = guard._totals()
        if cur + block > guard.cost_cap:
            print(f"BLOCK {t}: cannot cover full block (proj ${cur+block:.4f} > cap ${guard.cost_cap}) -> NOT starting", flush=True); break
        for cond in COND_ROLES:
            for arm in ARMS:
                st = await run_cell(t, cond, arm, guard, gcb, PL, pvar)
                if st == "stop": print("BUDGET STOP mid-block", flush=True); return
    cur, calls, *_ = guard._totals()
    print(f"STAGE B RUN DONE: pilot* cum=${cur:.4f} ({calls} calls)", flush=True)

if __name__ == "__main__":
    asyncio.run(dry() if "--dry" in sys.argv else main())
