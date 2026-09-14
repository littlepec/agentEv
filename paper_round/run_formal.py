#!/usr/bin/env python3
"""Formal flow: 4 tasks x 3 conditions (E / E+L / E+L') x {R0, R1fix} x 1 rep = 24 GPT-Researcher flows.
Frozen host/model/config; fixed engineering contract (stable ids, field-fix+empty->no-evidence, full
provider log). Interleaved by TASK BLOCK (one block = a task's 6 flows); a block is NOT started unless
the budget can cover all 6 (no half-done task). Ledger exp_key=...-paper-formal; absolute cap on the
whole evidence-package-pilot* line = min(global $5, chosen sub-budget) -> $3.3 (stricter). Eval labels
stay private (private_eval.json); scoring is separate."""
from __future__ import annotations
import os,sys,json,time,asyncio,pathlib
ROOT=pathlib.Path(__file__).resolve().parent; RUNS=ROOT/"runs_formal"; DOCP=ROOT/"docpaths_formal"
RUNS.mkdir(exist_ok=True); DOCP.mkdir(exist_ok=True)
KEY=pathlib.Path("F:/defense/research_v1/.deepseek_key").read_text(encoding="utf-8").strip()
sys.path.insert(0,"F:/defense/evidence_pack_prep_v1"); sys.path.insert(0,str(ROOT))
from ledger_guard import BudgetGuard
import contract as C, offline_retriever
os.environ["OPENAI_API_KEY"]=KEY; os.environ["OPENAI_BASE_URL"]="https://api.deepseek.com"
os.environ["FAST_LLM"]=os.environ["SMART_LLM"]=os.environ["STRATEGIC_LLM"]="openai:deepseek-v4-flash"
os.environ["EMBEDDING"]="huggingface:sentence-transformers/all-MiniLM-L6-v2"
os.environ["REPORT_SOURCE"]="local"; os.environ["RETRIEVER"]="offline_null"; os.environ["TEMPERATURE"]="0.4"
os.environ.setdefault("TOKENIZERS_PARALLELISM","false")
TASKS=["Q3","Q2","Q4","Q7"]
COND_ROLES={"E":{"evidence":"E.txt"},"E+L":{"evidence":"E.txt","interp":"L.txt"},"E+Lp":{"evidence":"E.txt","interp":"Lprime.txt"}}
ARMS={"R0":"false","R1fix":"true"}
IN_RATE,OUT_RATE=0.30/1_000_000,1.20/1_000_000
RES={"R0":0.03,"R1fix":0.05}; CAP=3.3
def qtext(t): return json.loads((ROOT/"tasks"/t/"private_eval.json").read_text(encoding="utf-8"))["question"]
def get_cb():
    from langchain_community.callbacks.manager import get_openai_callback; return get_openai_callback
async def run_cell(t,cond,arm,guard,gcb,PL,pvar):
    cell=f"{t}_{cond}_{arm}"; cdir=RUNS/cell; cdir.mkdir(exist_ok=True)
    if (cdir/"meta.json").exists() and json.loads((cdir/"meta.json").read_text(encoding="utf-8")).get("done"): return "skip"
    ok,why=guard.preflight(RES[arm],int(RES[arm]/OUT_RATE))
    if not ok: print(f"{cell}: {why}",flush=True); return "stop"
    role_files={role:ROOT/"tasks"/t/fn for role,fn in COND_ROLES[cond].items()}
    dp,mapping=C.stable_docpath(role_files,DOCP/cell)
    os.environ["DOC_PATH"]=str(dp); os.environ["CURATE_SOURCES"]=ARMS[arm]
    C._CUR_SINK["path"]=str(cdir/"curation.json") if arm=="R1fix" else None
    C._CUR_SINK["state"]={} if arm=="R1fix" else None
    offline_retriever.install_offline_retriever()
    from gpt_researcher import GPTResearcher
    plog=PL() if PL else None
    if plog is not None and pvar is not None: pvar.set(plog)
    t0=time.time(); pt=ct=0; report=""; err=None
    try:
        r=GPTResearcher(query=qtext(t),report_type="research_report",report_source="local")
        with gcb() as cb:
            await r.conduct_research(); report=await r.write_report()
        pt,ct=cb.prompt_tokens,cb.completion_tokens
        (cdir/"report.md").write_text(report or "",encoding="utf-8")
        try:(cdir/"context.json").write_text(json.dumps(r.context,ensure_ascii=False,indent=2,default=str),encoding="utf-8")
        except Exception: pass
        if plog is not None: C.save_provider_logs(plog.calls,cdir/"provider_log.json",cdir/"provider_log_preview.json")
    except Exception as e: err=f"{type(e).__name__}: {e}"; print(f"{cell}: ERR {err}",flush=True)
    cost=pt*IN_RATE+ct*OUT_RATE
    guard.record(cost,pt,ct,data={"stage":"paper_formal","cell":cell},est_cost=RES[arm],est_out=int(RES[arm]/OUT_RATE))
    st=dict(C._CUR_SINK["state"]) if (arm=="R1fix" and C._CUR_SINK["state"] is not None) else None
    meta={"cell":cell,"task":t,"condition":cond,"arm":arm,"curate_sources":ARMS[arm],"docpath_mapping":mapping,
          "prompt_tokens":pt,"completion_tokens":ct,"deepseek_cost_usd":round(cost,6),"report_chars":len(report or ""),
          "curation_state":st,"no_evidence_after_curation":(st or {}).get("no_evidence"),
          "elapsed_s":round(time.time()-t0,1),"error":err,"done":err is None,
          "host":"gpt-researcher v3.6.1 (6f998577) fixed-contract","model":"deepseek-v4-flash"}
    (cdir/"meta.json").write_text(json.dumps(meta,ensure_ascii=False,indent=2),encoding="utf-8")
    with (RUNS/"formal_results.jsonl").open("a",encoding="utf-8") as f: f.write(json.dumps(meta,ensure_ascii=False)+"\n")
    print(f"{cell}: {'ok' if not err else 'error'} in={pt} out={ct} ${cost:.4f} chars={len(report or '')} no_ev={meta['no_evidence_after_curation']}",flush=True)
    return "ok" if not err else "error"
async def main():
    C.install_curation_field_fix(); PL,pvar=C.make_provider_logger(); gcb=get_cb()
    guard=BudgetGuard("evidence-package-pilot-paper-formal",exp_prefix="evidence-package-pilot",
                      cost_cap=CAP,call_cap=100000,in_tok_cap=40_000_000,out_tok_cap=15_000_000)
    cur,calls,itok,otok,mx=guard._totals()
    block_cost=sum(RES[a] for a in ARMS)*len(COND_ROLES)   # reserve for one task block (6 flows)
    print(f"COST ACCOUNTING: pilot* cum=${cur:.4f}; cap=${CAP}; per-block reserve=${block_cost:.3f}; remaining headroom=${CAP-cur:.3f}",flush=True)
    for t in TASKS:
        cur,*_=guard._totals()
        if cur+block_cost>CAP:
            print(f"BLOCK {t}: cannot cover full block (proj ${cur+block_cost:.3f} > cap ${CAP}) -> NOT starting block",flush=True); break
        for cond in COND_ROLES:
            for arm in ARMS:
                st=await run_cell(t,cond,arm,guard,gcb,PL,pvar)
                if st=="stop": print("BUDGET STOP mid-block",flush=True); return
    print("FORMAL DONE",flush=True)
if __name__=="__main__": asyncio.run(main())
