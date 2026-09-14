#!/usr/bin/env python3
"""Main comparison runner: GPT-Researcher v3.6.1, DeepSeek + local HF embed + offline retriever
(fixed local sources, no web). Grid = 6 tasks x 3 conditions x 2 arms (R0/R1) x 2 reps = 72 reports.
ONLY manipulated variable across arms = CURATE_SOURCES (R0 False / R1 True). Rep-1 full grid first.

Per cell: assemble DOC_PATH (normal sources [+ harmless_supplement | + error_material]); run pipeline;
capture tokens via get_openai_callback -> DeepSeek-priced cost; ledger_guard preflight (reserve) + record;
archive full IO (docpath files, pre-curation research_data, curated list if R1, final report, meta).

Budget: ledger_guard round scope exp_prefix=evidence-package-pilot, exp_key=...-gptr-round,
round cap $3.0; reserve R0 $0.02 / R1 $0.04 before each report; stop on projected-over or anomaly.
Resumable: skips cells whose meta.json already marks done.
"""
from __future__ import annotations
import os, sys, json, time, asyncio, pathlib, shutil

ROOT = pathlib.Path(__file__).resolve().parent
RUNS = ROOT / "runs"; DOCP = ROOT / "docpaths"
RUNS.mkdir(exist_ok=True); DOCP.mkdir(exist_ok=True)
DEEPSEEK_KEY = pathlib.Path("F:/defense/research_v1/.deepseek_key").read_text(encoding="utf-8").strip()
sys.path.insert(0, "F:/defense/evidence_pack_prep_v1")
from ledger_guard import BudgetGuard

# ---- pinned config ----
os.environ["OPENAI_API_KEY"] = DEEPSEEK_KEY
os.environ["OPENAI_BASE_URL"] = "https://api.deepseek.com"
os.environ["FAST_LLM"] = os.environ["SMART_LLM"] = os.environ["STRATEGIC_LLM"] = "openai:deepseek-v4-flash"
os.environ["EMBEDDING"] = "huggingface:sentence-transformers/all-MiniLM-L6-v2"
os.environ["REPORT_SOURCE"] = "local"
os.environ["RETRIEVER"] = "offline_null"
os.environ["TEMPERATURE"] = "0.4"
os.environ.setdefault("TOKENIZERS_PARALLELISM", "false")

TASKS = {
 "C1": "Provide an overview of CRISPR-Cas9 gene editing: how it works and how it was developed.",
 "C2": "Summarize the established health effects of industrial trans fats and the main regulatory responses.",
 "C3": "Describe the James Webb Space Telescope: its design, main instruments, and purpose.",
 "C4": "Explain HTTP/3 and QUIC and their key improvements over HTTP/2.",
 "C5": "Provide an overview of GLP-1 receptor agonists (e.g., semaglutide): mechanism and approved uses.",
 "C6": "Summarize the Montreal Protocol: what it regulates and its effect on the ozone layer.",
}
CONDITIONS = ["normal", "harmless", "error"]
ARMS = {"R0": "false", "R1": "true"}   # CURATE_SOURCES
REPS = [0, 1]
RESERVE = {"R0": 0.02, "R1": 0.04}
ROUND_CAP = 3.0
IN_RATE, OUT_RATE = 0.30/1_000_000, 1.20/1_000_000

def get_cb():
    for mod in ("langchain_community.callbacks.manager","langchain_community.callbacks",
                "langchain.callbacks","langchain_core.callbacks"):
        try:
            m = __import__(mod, fromlist=["get_openai_callback"]); return getattr(m,"get_openai_callback")
        except Exception: continue
    return None

def build_docpath(task, cond):
    d = DOCP / f"{task}_{cond}"
    if d.exists(): shutil.rmtree(d)
    d.mkdir(parents=True)
    normal = ROOT / "tasks" / task / "normal" / "normal_sources.txt"
    if not normal.exists(): raise SystemExit(f"missing normal sources: {normal} (run freeze_round.py first)")
    shutil.copy(normal, d / "normal_sources.txt")
    if cond == "harmless":
        shutil.copy(ROOT/"tasks"/task/"harmless_supplement.txt", d/"harmless_supplement.txt")
    elif cond == "error":
        shutil.copy(ROOT/"tasks"/task/"error_material.txt", d/"error_material.txt")
    return d, sorted(p.name for p in d.iterdir())

# ---- curated-list observation hook (pure logging; return unchanged) ----
_SINK = {"pre": None, "post": None}
def install_curation_observer():
    import gpt_researcher.skills.curator as cur
    orig = cur.SourceCurator.curate_sources
    async def wrap(self, source_data, *a, **k):
        try:
            if _SINK["pre"]: pathlib.Path(_SINK["pre"]).write_text(json.dumps(source_data, ensure_ascii=False, indent=2, default=str), encoding="utf-8")
        except Exception: pass
        out = await orig(self, source_data, *a, **k)
        try:
            if _SINK["post"]: pathlib.Path(_SINK["post"]).write_text(json.dumps(out, ensure_ascii=False, indent=2, default=str), encoding="utf-8")
        except Exception: pass
        return out
    cur.SourceCurator.curate_sources = wrap

async def run_cell(task, cond, arm, rep, guard, get_openai_callback):
    cell = f"{task}_{cond}_{arm}_r{rep}"
    cdir = RUNS / cell; cdir.mkdir(exist_ok=True)
    meta_p = cdir / "meta.json"
    if meta_p.exists():
        try:
            if json.loads(meta_p.read_text(encoding="utf-8")).get("done"): return "skip", 0.0
        except Exception: pass
    est = RESERVE[arm]
    ok, why = guard.preflight(est_cost=est, est_out_tokens=int(est/OUT_RATE))
    if not ok:
        print(f"{cell}: {why}", flush=True); return "stop", 0.0
    docpath, files = build_docpath(task, cond)
    os.environ["DOC_PATH"] = str(docpath)
    os.environ["CURATE_SOURCES"] = ARMS[arm]
    _SINK["pre"] = str(cdir/"research_data_precurate.json")
    _SINK["post"] = str(cdir/"curated_list.json") if arm == "R1" else None
    import offline_retriever; offline_retriever.install_offline_retriever()
    from gpt_researcher import GPTResearcher
    t0 = time.time(); pt = ct = 0; report = ""; err = None; fin = "ok"
    try:
        r = GPTResearcher(query=TASKS[task], report_type="research_report", report_source="local")
        if get_openai_callback:
            with get_openai_callback() as cb:
                await r.conduct_research(); report = await r.write_report()
            pt, ct = cb.prompt_tokens, cb.completion_tokens
        else:
            await r.conduct_research(); report = await r.write_report()
        try: ctx = r.context
        except Exception: ctx = None
        (cdir/"report.md").write_text(report or "", encoding="utf-8")
        try: (cdir/"context.json").write_text(json.dumps(ctx, ensure_ascii=False, indent=2, default=str), encoding="utf-8")
        except Exception: pass
    except Exception as e:
        err = f"{type(e).__name__}: {e}"; fin = "error"; print(f"{cell}: ERR {err}", flush=True)
    cost = pt*IN_RATE + ct*OUT_RATE
    guard.record(cost, pt, ct, data={"stage":"gptr_round","cell":cell,"arm":arm}, est_cost=est, est_out=int(est/OUT_RATE))
    meta = {"cell":cell,"task":task,"condition":cond,"arm":arm,"curate_sources":ARMS[arm],"rep":rep,
            "docpath_files":files,"query":TASKS[task],"prompt_tokens":pt,"completion_tokens":ct,
            "deepseek_cost_usd":round(cost,6),"report_chars":len(report or ""),"elapsed_s":round(time.time()-t0,1),
            "error":err,"done": err is None,"model":"deepseek-v4-flash","host":"gpt-researcher v3.6.1 (6f998577)"}
    meta_p.write_text(json.dumps(meta, ensure_ascii=False, indent=2), encoding="utf-8")
    with (RUNS/"round_results.jsonl").open("a", encoding="utf-8") as f: f.write(json.dumps(meta, ensure_ascii=False)+"\n")
    print(f"{cell}: {fin} in={pt} out={ct} ${cost:.4f} chars={len(report or '')}", flush=True)
    return fin, cost

async def main():
    install_curation_observer()
    get_openai_callback = get_cb()
    guard = BudgetGuard("evidence-package-pilot-gptr-round", exp_prefix="evidence-package-pilot",
                        cost_cap=ROUND_CAP, call_cap=100000, in_tok_cap=50_000_000, out_tok_cap=20_000_000)
    # rep-1 full grid first, then rep-2 (coverage-complete ordering)
    order = [(t,c,a,rep) for rep in REPS for t in TASKS for c in CONDITIONS for a in ARMS]
    done = stopped = 0
    for (t,c,a,rep) in order:
        st, _ = await run_cell(t,c,a,rep,guard,get_openai_callback)
        if st == "stop": stopped += 1; print("BUDGET STOP -> halting round", flush=True); break
        if st in ("ok","error"): done += 1
    print(f"ROUND DONE. cells_run={done} stopped={stopped}", flush=True)

if __name__ == "__main__":
    asyncio.run(main())
