#!/usr/bin/env python3
"""Round v6 runner (skeptical-wording variant boundary test): 4 tasks x 2 combos x 2 reps = 16 calls to
DeepSeek deepseek-v4-flash. Sends ONLY frozen6 public inputs (sufficient correct
evidence, no poison). Logs to runs/pilot6_results.jsonl, appends ledger exp_key=...-v5.
Same caps/config as run_pilot2.py; max_tokens 8000. Resumable (done_set)."""
from __future__ import annotations
import json, pathlib, time, urllib.request, urllib.error, sqlite3, datetime

ROOT = pathlib.Path(__file__).resolve().parent
FROZEN = ROOT / "runs" / "frozen6"
RESULTS = ROOT / "runs" / "pilot6_results.jsonl"
LEDGER = pathlib.Path("F:/defense/defense_injection/defense-audit-work/runs/budget.sqlite")
KEY_FILE = pathlib.Path("F:/defense/research_v1/.deepseek_key")

MODEL = "deepseek-v4-flash"
URL = "https://api.deepseek.com/chat/completions"
TEMP = 0
MAX_TOKENS = 8000
EXP_KEY = "evidence-package-pilot-v6"
QIDS = [88, 89, 94, 73]
COMBOS = ["S2_CP", "S2_C0S"]
REPS = [0, 1]

COST_CAP = 5.0; INPUT_TOK_CAP = 300000; OUTPUT_TOK_CAP = 120000; ATTEMPT_CAP = 40
IN_RATE = 0.30 / 1_000_000; OUT_RATE = 1.20 / 1_000_000

def load_key():
    k = KEY_FILE.read_text(encoding="utf-8").strip()
    if not k: raise SystemExit("KEY EMPTY")
    return k

def done_set():
    s = set()
    if RESULTS.exists():
        for line in RESULTS.read_text(encoding="utf-8").splitlines():
            if line.strip():
                r = json.loads(line)
                if r.get("ok") and r.get("finish_reason") == "stop" and (r.get("answer") or "").strip():
                    s.add((r["task"], r["combo"], r["rep"]))
    return s

def call(key, messages):
    body = json.dumps({"model": MODEL, "messages": messages, "temperature": TEMP,
                       "max_tokens": MAX_TOKENS, "stream": False}).encode("utf-8")
    req = urllib.request.Request(URL, data=body, method="POST",
        headers={"Authorization": f"Bearer {key}", "Content-Type": "application/json"})
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
        return f"ledger_error: {type(e).__name__}: {e}"

def main():
    key = load_key(); done = done_set()
    order = [(rep, q, combo) for rep in REPS for q in QIDS for combo in COMBOS]
    cum_cost = cum_in = cum_out = attempts = 0
    RESULTS.parent.mkdir(parents=True, exist_ok=True)
    print(f"pilot5 start: {len(order)} planned, {len(done)} done", flush=True)
    for rep, q, combo in order:
        if (q, combo, rep) in done: continue
        if attempts >= ATTEMPT_CAP or cum_cost >= COST_CAP or cum_in >= INPUT_TOK_CAP or cum_out >= OUTPUT_TOK_CAP:
            print(f"CAP REACHED before {q} {combo} r{rep}", flush=True); break
        frozen = json.loads((FROZEN / f"task_{q}_{combo}.json").read_text(encoding="utf-8"))
        t0 = time.time(); attempts += 1
        row = {"task": q, "combo": combo, "rep": rep, "model": MODEL, "temperature": TEMP,
               "frozen_file": f"task_{q}_{combo}.json", "ts": datetime.datetime.now().isoformat(timespec="seconds")}
        try:
            resp = call(key, frozen["messages"]); msg = resp["choices"][0]["message"]
            content = msg.get("content", ""); reasoning = msg.get("reasoning_content")
            usage = resp.get("usage", {}); in_tok = int(usage.get("prompt_tokens", 0)); out_tok = int(usage.get("completion_tokens", 0))
            cost = in_tok * IN_RATE + out_tok * OUT_RATE
            cum_in += in_tok; cum_out += out_tok; cum_cost += cost
            row.update({"ok": True, "error": None, "finish_reason": resp["choices"][0].get("finish_reason"),
                        "prompt_tokens": in_tok, "completion_tokens": out_tok, "cost_est_usd": round(cost, 6),
                        "cum_cost_est_usd": round(cum_cost, 6), "answer": content,
                        "has_reasoning": bool(reasoning), "reasoning_len": len(reasoning) if reasoning else 0,
                        "answer_len": len(content or ""), "elapsed_s": round(time.time() - t0, 1)})
            row["ledger"] = ledger_append("ok", round(cost, 6), in_tok, out_tok, {"task": q, "combo": combo, "rep": rep, "model": MODEL})
            print(f"{q} {combo} r{rep}: ok fin={row['finish_reason']} in={in_tok} out={out_tok} cum=${cum_cost:.4f}", flush=True)
        except urllib.error.HTTPError as e:
            detail = e.read().decode("utf-8", "replace")[:300]
            row.update({"ok": False, "error": f"HTTP {e.code}: {detail}", "elapsed_s": round(time.time()-t0,1)})
            with RESULTS.open("a", encoding="utf-8") as f: f.write(json.dumps(row, ensure_ascii=False) + "\n")
            print(f"{q} {combo} r{rep}: HTTP {e.code}", flush=True)
            if e.code in (401, 403, 404): print("AUTH/MODEL error -> abort", flush=True); break
            continue
        except Exception as e:
            row.update({"ok": False, "error": f"{type(e).__name__}: {e}", "elapsed_s": round(time.time()-t0,1)})
            with RESULTS.open("a", encoding="utf-8") as f: f.write(json.dumps(row, ensure_ascii=False) + "\n")
            print(f"{q} {combo} r{rep}: ERR {e}", flush=True); continue
        with RESULTS.open("a", encoding="utf-8") as f: f.write(json.dumps(row, ensure_ascii=False) + "\n")
    print(f"PILOT5 DONE. attempts={attempts} cum_cost_est=${cum_cost:.4f} in={cum_in} out={cum_out}", flush=True)

if __name__ == "__main__":
    main()
