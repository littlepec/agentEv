#!/usr/bin/env python3
"""Evidence-dependence diagnostic (NOT host performance): short-answer, no-source vs with-source(E).
4 tasks x {nosource, withE} x 2 reps = 16 direct DeepSeek calls. Purpose: confirm each task truly
DEPENDS on the external evidence (nosource should NOT yield the correct specific; withE should).
One no-source failure alone is not proof of dependence -> we look at the pattern across reps + the
withE contrast. Ledger exp_key=...-paper-diag. No GPT-Researcher host here."""
from __future__ import annotations
import os,sys,json,time,urllib.request,pathlib
ROOT=pathlib.Path(__file__).resolve().parent; OUT=ROOT/"diag"; OUT.mkdir(exist_ok=True)
sys.path.insert(0,"F:/defense/evidence_pack_prep_v1"); from ledger_guard import BudgetGuard
KEY=pathlib.Path("F:/defense/research_v1/.deepseek_key").read_text(encoding="utf-8").strip()
IN_RATE,OUT_RATE=0.30/1_000_000,1.20/1_000_000
TASKS=["Q3","Q2","Q4","Q7"]; REPS=[0,1]
SYS=("Answer the question in one or two sentences with the specific detail asked. "
     "If you do not have enough information to answer with confidence, reply exactly 'INSUFFICIENT'.")
def q(tid): return json.loads((ROOT/"tasks"/tid/"private_eval.json").read_text(encoding="utf-8"))["question"]
def E(tid): return (ROOT/"tasks"/tid/"E.txt").read_text(encoding="utf-8")
def call(user):
    body=json.dumps({"model":"deepseek-v4-flash","messages":[{"role":"system","content":SYS},
        {"role":"user","content":user}],"temperature":0.4,"max_tokens":600,"stream":False}).encode()
    req=urllib.request.Request("https://api.deepseek.com/chat/completions",data=body,method="POST",
        headers={"Authorization":f"Bearer {KEY}","Content-Type":"application/json"})
    with urllib.request.urlopen(req,timeout=120) as r: return json.loads(r.read().decode())
def main():
    g=BudgetGuard("evidence-package-pilot-paper-diag",exp_prefix="evidence-package-pilot",cost_cap=2.5,
                  call_cap=100000,in_tok_cap=20_000_000,out_tok_cap=8_000_000)
    order=[(t,cond,rep) for rep in REPS for t in TASKS for cond in ["nosource","withE"]]
    for (t,cond,rep) in order:
        cell=f"{t}_{cond}_r{rep}"
        if (OUT/f"{cell}.json").exists(): continue
        ok,why=g.preflight(0.01,2000)
        if not ok: print(f"{cell}: {why}",flush=True); break
        user=(f"Question: {q(t)}" if cond=="nosource"
              else f"Provided source material:\n{E(t)}\n\nQuestion: {q(t)}")
        t0=time.time(); pt=ct=0; ans=""; err=None
        try:
            resp=call(user); m=resp["choices"][0]["message"]["content"]; u=resp.get("usage",{})
            pt=int(u.get("prompt_tokens",0)); ct=int(u.get("completion_tokens",0)); ans=m
        except Exception as e: err=str(e); print(f"{cell}: ERR {e}",flush=True)
        cost=pt*IN_RATE+ct*OUT_RATE
        g.record(cost,pt,ct,data={"stage":"paper_diag","cell":cell},est_cost=0.01,est_out=2000)
        rec={"cell":cell,"task":t,"condition":cond,"rep":rep,"question":q(t),"answer":ans,
             "prompt_tokens":pt,"completion_tokens":ct,"cost":round(cost,6),"elapsed_s":round(time.time()-t0,1),"error":err}
        (OUT/f"{cell}.json").write_text(json.dumps(rec,ensure_ascii=False,indent=2),encoding="utf-8")
        with (OUT/"diag_results.jsonl").open("a",encoding="utf-8") as f: f.write(json.dumps(rec,ensure_ascii=False)+"\n")
        print(f"{cell}: {'ok' if not err else 'ERR'} in={pt} out={ct} ${cost:.4f} | {ans[:90].replace(chr(10),' ')}",flush=True)
    print("DIAGNOSTIC DONE",flush=True)
if __name__=="__main__": main()
