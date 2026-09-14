#!/usr/bin/env python3
"""Minimal calibration after the audit (fixed engineering contract). NOT a re-run of the 72 grid.
C3,C4 x {normal,error} x {R0, R1fix} x 2 reps = 16 reports, with:
  - neutral source ids (no true/false in filenames)  [confound 1 fix]
  - curated-key normalization + empty-body guard      [confound 2 fix]
  - full provider request/response/finish logging per cell
Plus a small NO-SOURCE parametric control (C3,C4 x 2 reps = 4 direct DeepSeek calls), clearly
labeled control_nosource (NOT host normal execution). Ledger exp_key=...-gptr-calib, cap $1.0.
Does NOT alter error materials. Original run kept intact."""
from __future__ import annotations
import os, sys, json, time, asyncio, pathlib, urllib.request, contextvars

ROOT = pathlib.Path(__file__).resolve().parent
RUNS = ROOT / "runs_calib"; DOCP = ROOT / "docpaths_calib"
RUNS.mkdir(exist_ok=True); DOCP.mkdir(exist_ok=True)
DEEPSEEK_KEY = pathlib.Path("F:/defense/research_v1/.deepseek_key").read_text(encoding="utf-8").strip()
sys.path.insert(0, "F:/defense/evidence_pack_prep_v1"); sys.path.insert(0, str(ROOT))
from ledger_guard import BudgetGuard
import fixed_contract as FC
import offline_retriever

os.environ["OPENAI_API_KEY"] = DEEPSEEK_KEY
os.environ["OPENAI_BASE_URL"] = "https://api.deepseek.com"
os.environ["FAST_LLM"] = os.environ["SMART_LLM"] = os.environ["STRATEGIC_LLM"] = "openai:deepseek-v4-flash"
os.environ["EMBEDDING"] = "huggingface:sentence-transformers/all-MiniLM-L6-v2"
os.environ["REPORT_SOURCE"] = "local"; os.environ["RETRIEVER"] = "offline_null"; os.environ["TEMPERATURE"] = "0.4"
os.environ.setdefault("TOKENIZERS_PARALLELISM", "false")

TASKS = {
 "C3": "Describe the James Webb Space Telescope: its design, main instruments, and purpose.",
 "C4": "Explain HTTP/3 and QUIC and their key improvements over HTTP/2.",
}
CONDS = ["normal","error"]; ARMS = {"R0":"false","R1fix":"true"}; REPS=[0,1]
IN_RATE, OUT_RATE = 0.30/1_000_000, 1.20/1_000_000
SYS_NEUTRAL = ("You are a helpful research assistant. Use the provided source materials to answer the "
    "user's research question. Give a clear, informative answer and cite the source(s) you draw on.")

def get_cb():
    from langchain_community.callbacks.manager import get_openai_callback
    return get_openai_callback

def deepseek_direct(question):
    body=json.dumps({"model":"deepseek-v4-flash","messages":[{"role":"system","content":SYS_NEUTRAL},
        {"role":"user","content":question}],"temperature":0.4,"max_tokens":6000,"stream":False}).encode()
    req=urllib.request.Request("https://api.deepseek.com/chat/completions",data=body,method="POST",
        headers={"Authorization":f"Bearer {DEEPSEEK_KEY}","Content-Type":"application/json"})
    with urllib.request.urlopen(req,timeout=120) as r: return json.loads(r.read().decode())

async def run_cell(task,cond,arm,rep,guard,get_openai_callback,ProviderLogger,plog_var):
    cell=f"{task}_{cond}_{arm}_r{rep}"; cdir=RUNS/cell; cdir.mkdir(exist_ok=True)
    if (cdir/"meta.json").exists() and json.loads((cdir/"meta.json").read_text(encoding="utf-8")).get("done"): return "skip"
    ok,why=guard.preflight(0.03,int(0.03/OUT_RATE))
    if not ok: print(f"{cell}: {why}",flush=True); return "stop"
    docpath,mapping=FC.neutral_docpath(ROOT/"tasks"/task,cond,DOCP/cell,seed=hash(cell)%99999)
    os.environ["DOC_PATH"]=str(docpath); os.environ["CURATE_SOURCES"]=ARMS[arm]
    FC._CUR_SINK["path"]=str(cdir/"curation_normalized.json"); FC._CUR_SINK["flags"]={}
    offline_retriever.install_offline_retriever()
    from gpt_researcher import GPTResearcher
    plog = ProviderLogger() if ProviderLogger else None
    if plog is not None and plog_var is not None: plog_var.set(plog)
    t0=time.time(); pt=ct=0; report=""; err=None
    try:
        r=GPTResearcher(query=TASKS[task],report_type="research_report",report_source="local")
        with get_openai_callback() as cb:
            await r.conduct_research(); report=await r.write_report()
        pt,ct=cb.prompt_tokens,cb.completion_tokens
        (cdir/"report.md").write_text(report or "",encoding="utf-8")
        try: (cdir/"context.json").write_text(json.dumps(r.context,ensure_ascii=False,indent=2,default=str),encoding="utf-8")
        except Exception: pass
        if plog is not None:
            (cdir/"provider_log.json").write_text(json.dumps(plog.calls,ensure_ascii=False,indent=2,default=str),encoding="utf-8")
    except Exception as e:
        err=f"{type(e).__name__}: {e}"; print(f"{cell}: ERR {err}",flush=True)
    cost=pt*IN_RATE+ct*OUT_RATE
    guard.record(cost,pt,ct,data={"stage":"gptr_calib","cell":cell},est_cost=0.03,est_out=int(0.03/OUT_RATE))
    meta={"cell":cell,"task":task,"condition":cond,"arm":arm,"rep":rep,"neutral_id_mapping_PRIVATE":mapping,
          "prompt_tokens":pt,"completion_tokens":ct,"deepseek_cost_usd":round(cost,6),"report_chars":len(report or ""),
          "curation_empty_flags":dict(FC._CUR_SINK["flags"]) if arm=="R1fix" else None,
          "elapsed_s":round(time.time()-t0,1),"error":err,"done":err is None,
          "host":"gpt-researcher v3.6.1 (6f998577) FIXED-CONTRACT","model":"deepseek-v4-flash"}
    (cdir/"meta.json").write_text(json.dumps(meta,ensure_ascii=False,indent=2),encoding="utf-8")
    with (RUNS/"calib_results.jsonl").open("a",encoding="utf-8") as f: f.write(json.dumps(meta,ensure_ascii=False)+"\n")
    print(f"{cell}: {'ok' if not err else 'error'} in={pt} out={ct} ${cost:.4f} chars={len(report or '')} emptyflags={meta['curation_empty_flags']}",flush=True)
    return "ok" if not err else "error"

async def main():
    FC.install_curation_field_fix()
    ProviderLogger, plog_var = FC.make_provider_logger()
    get_openai_callback=get_cb()
    # cost_cap is the ABSOLUTE ceiling on the whole evidence-package-pilot* line (already ~$1.955);
    # $2.6 leaves ~$0.6 for this calibration, still far under the $5 line cap.
    guard=BudgetGuard("evidence-package-pilot-gptr-calib",exp_prefix="evidence-package-pilot",
                      cost_cap=2.6,call_cap=100000,in_tok_cap=20_000_000,out_tok_cap=8_000_000)
    order=[(t,c,a,rep) for rep in REPS for t in TASKS for c in CONDS for a in ARMS]
    for (t,c,a,rep) in order:
        st=await run_cell(t,c,a,rep,guard,get_openai_callback,ProviderLogger,plog_var)
        if st=="stop": print("BUDGET STOP",flush=True); return
    # no-source parametric control (NOT host execution) — direct DeepSeek, labeled clearly
    for rep in REPS:
        for t in TASKS:
            cell=f"{t}_control_nosource_r{rep}"; cdir=RUNS/cell; cdir.mkdir(exist_ok=True)
            if (cdir/"meta.json").exists(): continue
            ok,why=guard.preflight(0.02,int(0.02/OUT_RATE))
            if not ok: print(f"{cell}: {why}",flush=True); break
            try:
                resp=deepseek_direct(TASKS[t]); msg=resp["choices"][0]["message"]["content"]; u=resp.get("usage",{})
                pt=int(u.get("prompt_tokens",0)); ct=int(u.get("completion_tokens",0)); cost=pt*IN_RATE+ct*OUT_RATE
                (cdir/"report.md").write_text(msg or "",encoding="utf-8")
                guard.record(cost,pt,ct,data={"stage":"gptr_calib_control","cell":cell},est_cost=0.02,est_out=int(0.02/OUT_RATE))
                meta={"cell":cell,"task":t,"condition":"control_nosource","arm":"CONTROL(direct DeepSeek, NOT host)",
                      "rep":rep,"prompt_tokens":pt,"completion_tokens":ct,"deepseek_cost_usd":round(cost,6),
                      "report_chars":len(msg or ""),"done":True,"note":"pure parametric baseline; no sources; not GPT-Researcher"}
                (cdir/"meta.json").write_text(json.dumps(meta,ensure_ascii=False,indent=2),encoding="utf-8")
                with (RUNS/"calib_results.jsonl").open("a",encoding="utf-8") as f: f.write(json.dumps(meta,ensure_ascii=False)+"\n")
                print(f"{cell}: control ok in={pt} out={ct} ${cost:.4f}",flush=True)
            except Exception as e: print(f"{cell}: control ERR {e}",flush=True)
    print("CALIBRATION DONE",flush=True)

if __name__=="__main__":
    asyncio.run(main())
