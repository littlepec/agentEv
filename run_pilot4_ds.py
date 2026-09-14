#!/usr/bin/env python3
"""v4 DeepSeek: ADVERSARIAL reliability signal (frozen4: N_CP_advrel, S_CP_advrel).
4 tasks x 2 combos x 2 reps = 16 calls. Logs runs/pilot4_ds_results.jsonl, ledger
exp_key=evidence-package-pilot-v4-deepseek. Shared $5 cap. Standard library."""
from __future__ import annotations
import json, pathlib, time, urllib.request, urllib.error, sqlite3, datetime
ROOT = pathlib.Path(__file__).resolve().parent
FROZEN = ROOT/"runs"/"frozen4"; RESULTS = ROOT/"runs"/"pilot4_ds_results.jsonl"
LEDGER = pathlib.Path("F:/defense/defense_injection/defense-audit-work/runs/budget.sqlite")
KEY_FILE = pathlib.Path("F:/defense/research_v1/.deepseek_key")
MODEL="deepseek-v4-flash"; URL="https://api.deepseek.com/chat/completions"; TEMP=0; MAX_TOKENS=6000
EXP_KEY="evidence-package-pilot-v4-deepseek"; QIDS=[88,89,94,73]; COMBOS=["N_CP_advrel","S_CP_advrel"]; REPS=[0,1]
COST_CAP=5.0; ATTEMPT_CAP=40; IN_RATE=0.30/1e6; OUT_RATE=1.20/1e6
def load_key():
    k=KEY_FILE.read_text(encoding="utf-8").strip()
    if not k: raise SystemExit("KEY EMPTY")
    return k
def done_set():
    s=set()
    if RESULTS.exists():
        for l in RESULTS.read_text(encoding="utf-8").splitlines():
            if l.strip():
                r=json.loads(l)
                if r.get("ok") and r.get("finish_reason")=="stop" and (r.get("answer") or "").strip(): s.add((r["task"],r["combo"],r["rep"]))
    return s
def call(key,msgs):
    body=json.dumps({"model":MODEL,"messages":msgs,"temperature":TEMP,"max_tokens":MAX_TOKENS,"stream":False}).encode()
    req=urllib.request.Request(URL,data=body,method="POST",headers={"Authorization":f"Bearer {key}","Content-Type":"application/json"})
    with urllib.request.urlopen(req,timeout=150) as resp: return json.loads(resp.read().decode("utf-8"))
def ledger(status,cost,it,ot,data):
    try:
        c=sqlite3.connect(str(LEDGER),timeout=30)
        c.execute("insert into calls(exp_key,status,reserved_cost,reserved_output,cost,input_tokens,output_tokens,data,created) values(?,?,?,?,?,?,?,?,?)",
            (EXP_KEY,status,cost,ot,cost,it,ot,json.dumps(data,ensure_ascii=False),datetime.datetime.now().isoformat(timespec="seconds")))
        c.commit(); c.close(); return True
    except Exception as e: return f"ledger_error: {e}"
def main():
    key=load_key(); done=done_set(); cum=0.0; att=0; RESULTS.parent.mkdir(parents=True,exist_ok=True)
    order=[(rep,q,c) for rep in REPS for q in QIDS for c in COMBOS]
    print(f"v4-ds: {len(order)} planned, {len(done)} done", flush=True)
    for rep,q,c in order:
        if (q,c,rep) in done: continue
        if att>=ATTEMPT_CAP or cum>=COST_CAP: print("CAP",flush=True); break
        msgs=json.loads((FROZEN/f"task_{q}_{c}.json").read_text(encoding="utf-8"))["messages"]
        t0=time.time(); att+=1
        row={"task":q,"combo":c,"rep":rep,"model":MODEL,"ts":datetime.datetime.now().isoformat(timespec="seconds")}
        try:
            resp=call(key,msgs); m=resp["choices"][0]["message"]; content=m.get("content",""); rsn=m.get("reasoning_content")
            u=resp.get("usage",{}); it=int(u.get("prompt_tokens",0)); ot=int(u.get("completion_tokens",0)); cost=it*IN_RATE+ot*OUT_RATE; cum+=cost
            row.update({"ok":True,"error":None,"finish_reason":resp["choices"][0].get("finish_reason"),"prompt_tokens":it,"completion_tokens":ot,
                        "cost_est_usd":round(cost,6),"answer":content,"reasoning_len":len(rsn) if rsn else 0,"answer_len":len(content or ""),"elapsed_s":round(time.time()-t0,1)})
            row["ledger"]=ledger("ok",round(cost,6),it,ot,{"task":q,"combo":c,"rep":rep})
            print(f"{q} {c} r{rep}: ok fin={row['finish_reason']} out={ot} cum=${cum:.4f}",flush=True)
        except urllib.error.HTTPError as e:
            row.update({"ok":False,"error":f"HTTP {e.code}: {e.read().decode('utf-8','replace')[:200]}"})
            with RESULTS.open("a",encoding="utf-8") as f: f.write(json.dumps(row,ensure_ascii=False)+"\n")
            if e.code in (401,403,404): print("AUTH/MODEL abort",flush=True); break
            continue
        except Exception as e:
            row.update({"ok":False,"error":f"{type(e).__name__}: {e}"})
            with RESULTS.open("a",encoding="utf-8") as f: f.write(json.dumps(row,ensure_ascii=False)+"\n");
            print(f"{q} {c} r{rep}: ERR {e}",flush=True); continue
        with RESULTS.open("a",encoding="utf-8") as f: f.write(json.dumps(row,ensure_ascii=False)+"\n")
    print(f"V4-DS DONE. attempts={att} cum=${cum:.4f}",flush=True)
if __name__=="__main__": main()
