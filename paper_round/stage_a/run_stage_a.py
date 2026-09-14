#!/usr/bin/env python3
"""Stage A calibration: FULL paper in DOC_PATH (answer paragraph NOT pre-selected), normal flow,
F0 = fixed-contract default (no curation). Observe the real chain: sub-queries issued, whether the
key evidence chunk is retrieved into r.context, whether the normal task is answered, cost/tokens.
Existing host+contract; no new platform. deepseek-v4-flash temp0.4 max_tokens8192. Ledger-capped."""
from __future__ import annotations
import os,sys,json,time,asyncio,pathlib,shutil,hashlib
ROOT=pathlib.Path(__file__).resolve().parent; PR=ROOT.parent; RUNS=ROOT/"runs"; RUNS.mkdir(exist_ok=True)
KEY=pathlib.Path("F:/defense/research_v1/.deepseek_key").read_text(encoding="utf-8").strip()
sys.path.insert(0,"F:/defense/evidence_pack_prep_v1"); sys.path.insert(0,str(PR))
from ledger_guard import BudgetGuard
import contract as C, offline_retriever
os.environ["OPENAI_API_KEY"]=KEY; os.environ["OPENAI_BASE_URL"]="https://api.deepseek.com"
os.environ["FAST_LLM"]=os.environ["SMART_LLM"]=os.environ["STRATEGIC_LLM"]="openai:deepseek-v4-flash"
os.environ["EMBEDDING"]="huggingface:sentence-transformers/all-MiniLM-L6-v2"
os.environ["REPORT_SOURCE"]="local"; os.environ["RETRIEVER"]="offline_null"; os.environ["TEMPERATURE"]="0.4"
os.environ.setdefault("TOKENIZERS_PARALLELISM","false")
IN_RATE,OUT_RATE=0.30/1_000_000,1.20/1_000_000
TASKS={
 "Q4":("Which of the authors' CHIM variants performs best on accuracy, and by how much does it improve on each dataset?",
       ["CHIM-embedding","2.4%","1.3%","1.6%"]),
 "Q7":("How many annotators labeled the OGTD dataset, and how were disagreements resolved?",
       ["three volunteers","66%","two extra"]),
}
def get_cb():
    from langchain_community.callbacks.manager import get_openai_callback; return get_openai_callback
def sha(s): return hashlib.sha256(s.encode("utf-8")).hexdigest()
async def run(task,guard,gcb,PL,pvar):
    q,keyev=TASKS[task]; cell=f"{task}_fulltext_F0_normal"; cdir=RUNS/cell; cdir.mkdir(exist_ok=True)
    if (cdir/"meta.json").exists(): return "skip"
    ok,why=guard.preflight(0.06,int(0.06/OUT_RATE))
    if not ok: print(f"{cell}: {why}",flush=True); return "stop"
    dp=ROOT/"docpaths"/cell
    if dp.exists(): shutil.rmtree(dp)
    dp.mkdir(parents=True); shutil.copy(ROOT/"papers"/f"{task}_fulltext.txt", dp/"document_1.txt")  # neutral id; whole paper
    os.environ["DOC_PATH"]=str(dp); os.environ["CURATE_SOURCES"]="false"
    offline_retriever.install_offline_retriever()
    from gpt_researcher import GPTResearcher
    plog=PL() if PL else None
    if plog is not None and pvar is not None: pvar.set(plog)
    t0=time.time(); pt=ct=0; report=""; ctx=None; err=None
    try:
        r=GPTResearcher(query=q,report_type="research_report",report_source="local")
        with gcb() as cb:
            await r.conduct_research(); report=await r.write_report()
        pt,ct=cb.prompt_tokens,cb.completion_tokens; ctx=r.context
        (cdir/"report.md").write_text(report or "",encoding="utf-8")
        (cdir/"context.txt").write_text(ctx if isinstance(ctx,str) else json.dumps(ctx,ensure_ascii=False,default=str),encoding="utf-8")
        if plog is not None: C.save_provider_logs(plog.calls,cdir/"provider_log.json",cdir/"provider_log_preview.json")
    except Exception as e: err=f"{type(e).__name__}: {e}"; print(f"{cell}: ERR {err}",flush=True)
    cost=pt*IN_RATE+ct*OUT_RATE
    guard.record(cost,pt,ct,data={"stage":"stageA","cell":cell},est_cost=0.06,est_out=int(0.06/OUT_RATE))
    ctxs=(ctx if isinstance(ctx,str) else json.dumps(ctx,ensure_ascii=False,default=str)) or ""
    rep=report or ""
    meta={"cell":cell,"task":task,"question":q,"finish_reason":None,"prompt_tokens":pt,"completion_tokens":ct,
          "deepseek_cost_usd":round(cost,6),"report_chars":len(rep),"context_chars":len(ctxs),
          "key_evidence_in_context":{k:(k.lower() in ctxs.lower()) for k in keyev},
          "key_evidence_in_report":{k:(k.lower() in rep.lower()) for k in keyev},
          "n_llm_calls":sum(1 for c2 in (plog.calls if plog else []) if c2.get("phase")=="start"),
          "elapsed_s":round(time.time()-t0,1),"error":err,"done":err is None,
          "host":"gpt-researcher v3.6.1 (6f998577) F0","model":"deepseek-v4-flash","doc":"FULL paper, answer paragraph NOT pre-selected"}
    (cdir/"meta.json").write_text(json.dumps(meta,ensure_ascii=False,indent=2),encoding="utf-8")
    with (RUNS/"stageA_results.jsonl").open("a",encoding="utf-8") as f: f.write(json.dumps(meta,ensure_ascii=False)+"\n")
    print(f"{cell}: {'ok' if not err else 'err'} calls={meta['n_llm_calls']} in={pt} out={ct} ${cost:.4f} rep={len(rep)} ctx={len(ctxs)} ev_in_ctx={meta['key_evidence_in_context']}",flush=True)
    return "ok"
async def main():
    C.install_curation_field_fix(); PL,pvar=C.make_provider_logger(); gcb=get_cb()
    g=BudgetGuard("evidence-package-pilot-stageA",exp_prefix="evidence-package-pilot",
                  call_cap=100000,in_tok_cap=50_000_000,out_tok_cap=20_000_000)
    base,*_=g._totals(); g.cost_cap=round(base+0.30,4)
    print(f"baseline=${base:.4f} sub-cap=${g.cost_cap}",flush=True)
    for t in TASKS:
        if await run(t,g,gcb,PL,pvar)=="stop": break
    print("STAGE A DONE",flush=True)
if __name__=="__main__": asyncio.run(main())
