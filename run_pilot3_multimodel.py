#!/usr/bin/env python3
"""v3 track C: cross-family generalization. Re-run the 3 DISCRIMINATING conditions
(N_CP, S_CPO, N_CPO) from frozen2 on 2 additional model families via OpenRouter.
4 tasks x 3 conds x 1 rep x 2 models = 24 calls. Standard library (urllib).
Sends ONLY frozen2 public inputs. Logs runs/pilot3_results.jsonl, ledger exp_key
=evidence-package-pilot-v3-multimodel. Shared $5 cap (env already ~$0.22 used).
Key from env OPENROUTER_API_KEY (never printed).
"""
from __future__ import annotations
import json, os, pathlib, time, urllib.request, urllib.error, sqlite3, datetime

ROOT = pathlib.Path(__file__).resolve().parent
FROZEN = ROOT / "runs" / "frozen2"
RESULTS = ROOT / "runs" / "pilot3_results.jsonl"
LEDGER = pathlib.Path("F:/defense/defense_injection/defense-audit-work/runs/budget.sqlite")
URL = "https://openrouter.ai/api/v1/chat/completions"
EXP_KEY = "evidence-package-pilot-v3-multimodel"
QIDS = [88, 89, 94, 73]
CONDS = ["N_CP", "S_CPO", "N_CPO"]
REPS = [0]
TEMP = 0
MAX_TOKENS = 1500
# (model_id, in_rate, out_rate) USD/token estimates (labelled estimates)
MODELS = [
    ("openai/gpt-4o-mini", 0.15/1e6, 0.60/1e6),
    ("anthropic/claude-sonnet-4", 3.0/1e6, 15.0/1e6),
]
COST_CAP = 5.0; ATTEMPT_CAP = 60

def key():
    k = os.environ.get("OPENROUTER_API_KEY", "").strip()
    if not k: raise SystemExit("OPENROUTER_API_KEY missing")
    return k

def done_set():
    s = set()
    if RESULTS.exists():
        for l in RESULTS.read_text(encoding="utf-8").splitlines():
            if l.strip():
                r = json.loads(l)
                if r.get("ok") and (r.get("answer") or "").strip():
                    s.add((r["model"], r["task"], r["cond"], r["rep"]))
    return s

def call(k, model, messages):
    body = json.dumps({"model": model, "messages": messages, "temperature": TEMP,
                       "max_tokens": MAX_TOKENS}).encode("utf-8")
    req = urllib.request.Request(URL, data=body, method="POST", headers={
        "Authorization": f"Bearer {k}", "Content-Type": "application/json",
        "HTTP-Referer": "https://localhost/defense-research", "X-Title": "evidence-pilot-v3"})
    with urllib.request.urlopen(req, timeout=120) as resp:
        return json.loads(resp.read().decode("utf-8"))

def ledger_append(status, cost, in_tok, out_tok, data):
    try:
        c = sqlite3.connect(str(LEDGER), timeout=30)
        c.execute("insert into calls(exp_key,status,reserved_cost,reserved_output,cost,input_tokens,output_tokens,data,created)"
                  " values(?,?,?,?,?,?,?,?,?)",
                  (EXP_KEY, status, cost, out_tok, cost, in_tok, out_tok, json.dumps(data, ensure_ascii=False),
                   datetime.datetime.now().isoformat(timespec="seconds")))
        c.commit(); c.close(); return True
    except Exception as e:
        return f"ledger_error: {e}"

def main():
    k = key(); done = done_set()
    cum = 0.0; attempts = 0
    RESULTS.parent.mkdir(parents=True, exist_ok=True)
    order = [(m, q, c, rp) for (m, ir, orr) in MODELS for rp in REPS for q in QIDS for c in CONDS]
    rate = {m: (ir, orr) for (m, ir, orr) in MODELS}
    print(f"v3-multimodel: {len(order)} planned", flush=True)
    for m, q, c, rp in order:
        if (m, q, c, rp) in done: continue
        if attempts >= ATTEMPT_CAP or cum >= COST_CAP:
            print("CAP reached", flush=True); break
        msgs = json.loads((FROZEN / f"task_{q}_{c}.json").read_text(encoding="utf-8"))["messages"]
        t0 = time.time(); attempts += 1
        row = {"model": m, "task": q, "cond": c, "rep": rp, "temperature": TEMP,
               "ts": datetime.datetime.now().isoformat(timespec="seconds")}
        try:
            resp = call(k, m, msgs)
            ch = resp["choices"][0]; content = ch["message"].get("content", "")
            usage = resp.get("usage", {}); it = int(usage.get("prompt_tokens", 0)); ot = int(usage.get("completion_tokens", 0))
            ir, orr = rate[m]; cost = it*ir + ot*orr; cum += cost
            row.update({"ok": True, "error": None, "finish_reason": ch.get("finish_reason"),
                        "prompt_tokens": it, "completion_tokens": ot, "cost_est_usd": round(cost, 6),
                        "cum_cost_est_usd": round(cum, 6), "answer": content, "answer_len": len(content or ""),
                        "elapsed_s": round(time.time()-t0, 1)})
            row["ledger"] = ledger_append("ok", round(cost, 6), it, ot, {"model": m, "task": q, "cond": c, "rep": rp})
            print(f"{m} {q} {c}: ok fin={row['finish_reason']} in={it} out={ot} cum=${cum:.4f}", flush=True)
        except urllib.error.HTTPError as e:
            detail = e.read().decode("utf-8", "replace")[:300]
            row.update({"ok": False, "error": f"HTTP {e.code}: {detail}"})
            with RESULTS.open("a", encoding="utf-8") as f: f.write(json.dumps(row, ensure_ascii=False)+"\n")
            print(f"{m} {q} {c}: HTTP {e.code} {detail[:100]}", flush=True)
            if e.code in (401, 403):
                print("AUTH error -> abort", flush=True); break
            if e.code == 404:
                print(f"model {m} not found -> skip to next model", flush=True)
                done |= {(m, qq, cc, rr) for qq in QIDS for cc in CONDS for rr in REPS}
            continue
        except Exception as e:
            row.update({"ok": False, "error": f"{type(e).__name__}: {e}"})
            with RESULTS.open("a", encoding="utf-8") as f: f.write(json.dumps(row, ensure_ascii=False)+"\n")
            print(f"{m} {q} {c}: ERR {e}", flush=True); continue
        with RESULTS.open("a", encoding="utf-8") as f: f.write(json.dumps(row, ensure_ascii=False)+"\n")
    print(f"V3-MULTIMODEL DONE. attempts={attempts} cum=${cum:.4f}", flush=True)

if __name__ == "__main__":
    main()
