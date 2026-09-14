#!/usr/bin/env python3
"""v3 DeepSeek runner: track A (reliability signal: N_CP_rel, S_CP_rel) + track B
(de-telled poison-only: S_CPO3, N_CPO3). 4 combos x 4 tasks x 2 reps = 32 calls.
Reads frozen3. Standard library. Logs runs/pilot3_ds_results.jsonl, ledger exp_key
=evidence-package-pilot-v3-deepseek. max_tokens 8000 (reasoning model). Shared $5 cap.
"""
from __future__ import annotations
import json, pathlib, time, urllib.request, urllib.error, sqlite3, datetime

ROOT = pathlib.Path(__file__).resolve().parent
FROZEN = ROOT / "runs" / "frozen3"
RESULTS = ROOT / "runs" / "pilot3_ds_results.jsonl"
LEDGER = pathlib.Path("F:/defense/defense_injection/defense-audit-work/runs/budget.sqlite")
KEY_FILE = pathlib.Path("F:/defense/research_v1/.deepseek_key")
MODEL = "deepseek-v4-flash"; URL = "https://api.deepseek.com/chat/completions"
TEMP = 0; MAX_TOKENS = 8000; EXP_KEY = "evidence-package-pilot-v3-deepseek"
QIDS = [88, 89, 94, 73]; COMBOS = ["N_CP_rel", "S_CP_rel", "S_CPO3", "N_CPO3"]; REPS = [0, 1]
COST_CAP = 5.0; ATTEMPT_CAP = 50; IN_RATE = 0.30/1e6; OUT_RATE = 1.20/1e6

def load_key():
    k = KEY_FILE.read_text(encoding="utf-8").strip()
    if not k: raise SystemExit("KEY EMPTY")
    return k
def done_set():
    s = set()
    if RESULTS.exists():
        for l in RESULTS.read_text(encoding="utf-8").splitlines():
            if l.strip():
                r = json.loads(l)
                if r.get("ok") and r.get("finish_reason") == "stop" and (r.get("answer") or "").strip():
                    s.add((r["task"], r["combo"], r["rep"]))
    return s
def call(key, messages):
    body = json.dumps({"model": MODEL, "messages": messages, "temperature": TEMP, "max_tokens": MAX_TOKENS, "stream": False}).encode()
    req = urllib.request.Request(URL, data=body, method="POST", headers={"Authorization": f"Bearer {key}", "Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=150) as resp:
        return json.loads(resp.read().decode("utf-8"))
def ledger_append(status, cost, it, ot, data):
    try:
        c = sqlite3.connect(str(LEDGER), timeout=30)
        c.execute("insert into calls(exp_key,status,reserved_cost,reserved_output,cost,input_tokens,output_tokens,data,created) values(?,?,?,?,?,?,?,?,?)",
                  (EXP_KEY, status, cost, ot, cost, it, ot, json.dumps(data, ensure_ascii=False), datetime.datetime.now().isoformat(timespec="seconds")))
        c.commit(); c.close(); return True
    except Exception as e: return f"ledger_error: {e}"

def main():
    key = load_key(); done = done_set()
    order = [(rep, q, combo) for rep in REPS for q in QIDS for combo in COMBOS]
    cum = 0.0; attempts = 0; RESULTS.parent.mkdir(parents=True, exist_ok=True)
    print(f"v3-deepseek: {len(order)} planned, {len(done)} done", flush=True)
    for rep, q, combo in order:
        if (q, combo, rep) in done: continue
        if attempts >= ATTEMPT_CAP or cum >= COST_CAP: print("CAP", flush=True); break
        msgs = json.loads((FROZEN / f"task_{q}_{combo}.json").read_text(encoding="utf-8"))["messages"]
        t0 = time.time(); attempts += 1
        row = {"task": q, "combo": combo, "rep": rep, "model": MODEL, "ts": datetime.datetime.now().isoformat(timespec="seconds")}
        try:
            resp = call(key, msgs); msg = resp["choices"][0]["message"]
            content = msg.get("content", ""); reasoning = msg.get("reasoning_content")
            u = resp.get("usage", {}); it = int(u.get("prompt_tokens", 0)); ot = int(u.get("completion_tokens", 0))
            cost = it*IN_RATE + ot*OUT_RATE; cum += cost
            row.update({"ok": True, "error": None, "finish_reason": resp["choices"][0].get("finish_reason"),
                        "prompt_tokens": it, "completion_tokens": ot, "cost_est_usd": round(cost, 6),
                        "answer": content, "reasoning_len": len(reasoning) if reasoning else 0,
                        "answer_len": len(content or ""), "elapsed_s": round(time.time()-t0, 1)})
            row["ledger"] = ledger_append("ok", round(cost, 6), it, ot, {"task": q, "combo": combo, "rep": rep})
            print(f"{q} {combo} r{rep}: ok fin={row['finish_reason']} out={ot} cum=${cum:.4f}", flush=True)
        except urllib.error.HTTPError as e:
            row.update({"ok": False, "error": f"HTTP {e.code}: {e.read().decode('utf-8','replace')[:200]}"})
            with RESULTS.open("a", encoding="utf-8") as f: f.write(json.dumps(row, ensure_ascii=False)+"\n")
            if e.code in (401, 403, 404): print("AUTH/MODEL abort", flush=True); break
            continue
        except Exception as e:
            row.update({"ok": False, "error": f"{type(e).__name__}: {e}"})
            with RESULTS.open("a", encoding="utf-8") as f: f.write(json.dumps(row, ensure_ascii=False)+"\n");
            print(f"{q} {combo} r{rep}: ERR {e}", flush=True); continue
        with RESULTS.open("a", encoding="utf-8") as f: f.write(json.dumps(row, ensure_ascii=False)+"\n")
    print(f"V3-DEEPSEEK DONE. attempts={attempts} cum=${cum:.4f}", flush=True)

if __name__ == "__main__":
    main()
