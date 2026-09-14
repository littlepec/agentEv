#!/usr/bin/env python3
"""v4 multi-model: does the HONEST reliability signal (frozen3 N_CP_rel: A-high/B-low)
help the other two model families? gpt-4o-mini was 12/12 credulous; claude 7/12.
4 tasks x 1 rep x 2 models = 8 calls via OpenRouter. Logs runs/pilot4_mm_results.jsonl,
ledger exp_key=evidence-package-pilot-v4-multimodel. Shared $5 cap."""
from __future__ import annotations
import json, os, pathlib, time, urllib.request, urllib.error, sqlite3, datetime
ROOT = pathlib.Path(__file__).resolve().parent
FROZEN = ROOT/"runs"/"frozen3"; RESULTS = ROOT/"runs"/"pilot4_mm_results.jsonl"
LEDGER = pathlib.Path("F:/defense/defense_injection/defense-audit-work/runs/budget.sqlite")
URL="https://openrouter.ai/api/v1/chat/completions"; EXP_KEY="evidence-package-pilot-v4-multimodel"
QIDS=[88,89,94,73]; COND="N_CP_rel"; TEMP=0; MAX_TOKENS=1500
MODELS=[("openai/gpt-4o-mini",0.15/1e6,0.60/1e6),("anthropic/claude-sonnet-4",3.0/1e6,15.0/1e6)]
COST_CAP=5.0; ATTEMPT_CAP=20
def key():
    k=os.environ.get("OPENROUTER_API_KEY","").strip()
    if not k: raise SystemExit("OPENROUTER_API_KEY missing")
    return k
def done_set():
    s=set()
    if RESULTS.exists():
        for l in RESULTS.read_text(encoding="utf-8").splitlines():
            if l.strip():
                r=json.loads(l)
                if r.get("ok") and (r.get("answer") or "").strip(): s.add((r["model"],r["task"]))
    return s
def call(k,model,msgs):
    body=json.dumps({"model":model,"messages":msgs,"temperature":TEMP,"max_tokens":MAX_TOKENS}).encode()
    req=urllib.request.Request(URL,data=body,method="POST",headers={"Authorization":f"Bearer {k}","Content-Type":"application/json","HTTP-Referer":"https://localhost/defense-research","X-Title":"evidence-pilot-v4"})
    with urllib.request.urlopen(req,timeout=120) as resp: return json.loads(resp.read().decode("utf-8"))
def ledger(status,cost,it,ot,data):
    try:
        c=sqlite3.connect(str(LEDGER),timeout=30)
        c.execute("insert into calls(exp_key,status,reserved_cost,reserved_output,cost,input_tokens,output_tokens,data,created) values(?,?,?,?,?,?,?,?,?)",
            (EXP_KEY,status,cost,ot,cost,it,ot,json.dumps(data,ensure_ascii=False),datetime.datetime.now().isoformat(timespec="seconds")))
        c.commit(); c.close(); return True
    except Exception as e: return f"ledger_error: {e}"
def main():
    k=key(); done=done_set(); cum=0.0; att=0; RESULTS.parent.mkdir(parents=True,exist_ok=True)
    rate={m:(a,b) for m,a,b in MODELS}
    order=[(m,q) for (m,_,_) in MODELS for q in QIDS]
    print(f"v4-mm: {len(order)} planned", flush=True)
    for m,q in order:
        if (m,q) in done: continue
        if att>=ATTEMPT_CAP or cum>=COST_CAP: print("CAP",flush=True); break
        msgs=json.loads((FROZEN/f"task_{q}_{COND}.json").read_text(encoding="utf-8"))["messages"]
        t0=time.time(); att+=1
        row={"model":m,"task":q,"cond":COND,"rep":0,"ts":datetime.datetime.now().isoformat(timespec="seconds")}
        try:
            resp=call(k,m,msgs); ch=resp["choices"][0]; content=ch["message"].get("content","")
            u=resp.get("usage",{}); it=int(u.get("prompt_tokens",0)); ot=int(u.get("completion_tokens",0))
            ir,orr=rate[m]; cost=it*ir+ot*orr; cum+=cost
            row.update({"ok":True,"error":None,"finish_reason":ch.get("finish_reason"),"prompt_tokens":it,"completion_tokens":ot,
                        "cost_est_usd":round(cost,6),"answer":content,"answer_len":len(content or ""),"elapsed_s":round(time.time()-t0,1)})
            row["ledger"]=ledger("ok",round(cost,6),it,ot,{"model":m,"task":q,"cond":COND})
            print(f"{m} {q}: ok out={ot} cum=${cum:.4f}",flush=True)
        except urllib.error.HTTPError as e:
            row.update({"ok":False,"error":f"HTTP {e.code}: {e.read().decode('utf-8','replace')[:200]}"})
            with RESULTS.open("a",encoding="utf-8") as f: f.write(json.dumps(row,ensure_ascii=False)+"\n")
            if e.code in (401,403): print("AUTH abort",flush=True); break
            continue
        except Exception as e:
            row.update({"ok":False,"error":f"{type(e).__name__}: {e}"})
            with RESULTS.open("a",encoding="utf-8") as f: f.write(json.dumps(row,ensure_ascii=False)+"\n");
            print(f"{m} {q}: ERR {e}",flush=True); continue
        with RESULTS.open("a",encoding="utf-8") as f: f.write(json.dumps(row,ensure_ascii=False)+"\n")
    print(f"V4-MM DONE. attempts={att} cum=${cum:.4f}",flush=True)
if __name__=="__main__": main()
