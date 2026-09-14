#!/usr/bin/env python3
"""Execute the 12 frozen drafting requests (schedule order). Fixed model/shell; no pipeline stages.
deepseek-v4-flash, temp 0.4, max_tokens 8192, concurrency 1, retries 0. Ledger sub-budget = baseline+$0.50
(stricter of caps), per-request atomic reservation, anomaly stop, <=12 attempts incl failures, no rerun-to-success.
Saves full response/report/finish/usage/model-id per slot. Reads public/*.json + schedule.json."""
from __future__ import annotations
import os,sys,json,time,urllib.request,pathlib,hashlib
ROOT=pathlib.Path(__file__).resolve().parent; OUT=ROOT/"runs"; OUT.mkdir(exist_ok=True)
sys.path.insert(0,"F:/defense/evidence_pack_prep_v1"); from ledger_guard import BudgetGuard
KEY=pathlib.Path("F:/defense/research_v1/.deepseek_key").read_text(encoding="utf-8").strip()
IN_RATE,OUT_RATE=0.30/1_000_000,1.20/1_000_000
MODEL="deepseek-v4-flash"; URL="https://api.deepseek.com/chat/completions"; TEMP=0.4; MAXTOK=8192
def sha(s): return hashlib.sha256(s.encode("utf-8")).hexdigest()
def call(messages):
    body=json.dumps({"model":MODEL,"messages":messages,"temperature":TEMP,"max_tokens":MAXTOK,"stream":False}).encode()
    req=urllib.request.Request(URL,data=body,method="POST",headers={"Authorization":f"Bearer {KEY}","Content-Type":"application/json"})
    with urllib.request.urlopen(req,timeout=180) as r: return json.loads(r.read().decode("utf-8"))
def main():
    sched=json.loads((ROOT/"schedule.json").read_text(encoding="utf-8"))
    g=BudgetGuard("evidence-package-pilot-q3loc",exp_prefix="evidence-package-pilot",
                  call_cap=100000,in_tok_cap=50_000_000,out_tok_cap=20_000_000)
    base,calls,itok,otok,_=g._totals(); g.cost_cap=round(base+0.50,4)   # sub-budget: baseline + $0.50 (<= global $5)
    g.out_tok_cap=otok+98304                                            # spec: <=98,304 output tokens for the remaining slots
    EST_OUT=MAXTOK; EST_COST=0.015                                      # realistic per-request reserve (was mis-derived)
    print(f"baseline=${base:.4f} sub-cap=${g.cost_cap}",flush=True)
    attempts=0
    for slot in sched:
        rnd,cond=slot["round"],slot["cond"]; cell=f"r{rnd}_{cond}"
        if (OUT/f"{cell}.json").exists(): continue
        if attempts>=12: print("attempt cap 12 reached",flush=True); break
        ok,why=g.preflight(EST_COST,EST_OUT)
        if not ok: print(f"{cell}: {why}",flush=True); break
        msgs=json.loads((ROOT/"public"/f"{cond}.json").read_text(encoding="utf-8"))["messages"]
        attempts+=1; t0=time.time(); rec={"cell":cell,"round":rnd,"cond":cond,"messages_sha256":sha(json.dumps(msgs,ensure_ascii=False)),
             "model_req":MODEL,"temperature":TEMP,"max_tokens":MAXTOK,"ts":time.strftime("%Y-%m-%dT%H:%M:%S")}
        try:
            resp=call(msgs); ch=resp["choices"][0]; msg=ch["message"]; content=msg.get("content","") or ""
            u=resp.get("usage",{}); pt=int(u.get("prompt_tokens",0)); ct=int(u.get("completion_tokens",0)); cost=pt*IN_RATE+ct*OUT_RATE
            rec.update({"ok":True,"finish_reason":ch.get("finish_reason"),"model_returned":resp.get("model"),
                        "request_id":resp.get("id"),"prompt_tokens":pt,"completion_tokens":ct,"cost_usd":round(cost,6),
                        "answer":content,"answer_len":len(content),"reasoning_len":len(msg.get("reasoning_content") or ""),
                        "elapsed_s":round(time.time()-t0,1)})
            (OUT/f"{cell}.md").write_text(content,encoding="utf-8")
            rec["ledger"]=g.record(round(cost,6),pt,ct,data={"stage":"q3loc","cell":cell},est_cost=EST_COST,est_out=EST_OUT)
            print(f"{cell}: ok fin={ch.get('finish_reason')} in={pt} out={ct} ${cost:.4f} len={len(content)}",flush=True)
        except Exception as e:
            rec.update({"ok":False,"error":f"{type(e).__name__}: {e}","elapsed_s":round(time.time()-t0,1)})
            g.record(0.0,0,0,data={"stage":"q3loc_fail","cell":cell},est_cost=EST_COST,est_out=EST_OUT)
            print(f"{cell}: ERR {e}",flush=True)
        (OUT/f"{cell}.json").write_text(json.dumps(rec,ensure_ascii=False,indent=2),encoding="utf-8")
        with (OUT/"runs.jsonl").open("a",encoding="utf-8") as f: f.write(json.dumps(rec,ensure_ascii=False)+"\n")
    print(f"DONE attempts={attempts}",flush=True)
if __name__=="__main__": main()
