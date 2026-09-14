#!/usr/bin/env python3
"""Run the authorized fixed-evidence pilot: 4 tasks x 3 conditions x 2 repeats
= 24 answer calls to DeepSeek (deepseek-v4-flash, api.deepseek.com, temp 0).

Standard library only (urllib). Sends ONLY the frozen public inputs; never the
private claim/label. Logs every call to runs/pilot_results.jsonl and appends a
row per call to the global ledger with exp_key=evidence-package-pilot-v1.
Enforces cost/token/attempt caps from plan_execute.json. Key is read from file
and never printed. No judge model is used (scoring is done later by the analyst).
"""
from __future__ import annotations
import json, pathlib, time, urllib.request, urllib.error, sqlite3, datetime

ROOT = pathlib.Path(__file__).resolve().parent
FROZEN = ROOT / "runs" / "frozen"
RESULTS = ROOT / "runs" / "pilot_results.jsonl"
LEDGER = pathlib.Path("F:/defense/defense_injection/defense-audit-work/runs/budget.sqlite")
KEY_FILE = pathlib.Path("F:/defense/research_v1/.deepseek_key")

MODEL = "deepseek-v4-flash"
URL = "https://api.deepseek.com/chat/completions"
TEMP = 0
MAX_TOKENS = 3000
EXP_KEY = "evidence-package-pilot-v1"
QIDS = [88, 89, 94, 73]
CONDS = ["C0", "CN", "CP"]
REPS = [0, 1]

# caps (mirror plan_execute.json)
COST_CAP = 5.0
INPUT_TOK_CAP = 200000
OUTPUT_TOK_CAP = 40000
ATTEMPT_CAP = 40
# cost estimate rates (USD per token) — ESTIMATE only; actual billing is DeepSeek's
IN_RATE = 0.30 / 1_000_000
OUT_RATE = 1.20 / 1_000_000

def load_key() -> str:
    k = KEY_FILE.read_text(encoding="utf-8").strip()
    if not k:
        raise SystemExit("KEY EMPTY")
    return k

def done_set():
    s = set()
    if RESULTS.exists():
        for line in RESULTS.read_text(encoding="utf-8").splitlines():
            if line.strip():
                r = json.loads(line)
                # only count as done if VALID: ok, finished normally, non-empty content
                if r.get("ok") and r.get("finish_reason") == "stop" and (r.get("answer") or "").strip():
                    s.add((r["task"], r["cond"], r["rep"]))
    return s

def call(key: str, messages: list[dict]) -> dict:
    body = json.dumps({"model": MODEL, "messages": messages, "temperature": TEMP,
                       "max_tokens": MAX_TOKENS, "stream": False}).encode("utf-8")
    req = urllib.request.Request(URL, data=body, method="POST", headers={
        "Authorization": f"Bearer {key}", "Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=90) as resp:
        return json.loads(resp.read().decode("utf-8"))

def ledger_append(status, cost, in_tok, out_tok, data):
    try:
        c = sqlite3.connect(str(LEDGER), timeout=30)
        c.execute(
            "insert into calls(exp_key,status,reserved_cost,reserved_output,cost,input_tokens,output_tokens,data,created)"
            " values(?,?,?,?,?,?,?,?,?)",
            (EXP_KEY, status, cost, out_tok, cost, in_tok, out_tok, json.dumps(data, ensure_ascii=False),
             datetime.datetime.now().isoformat(timespec="seconds")))
        c.commit(); c.close()
        return True
    except Exception as e:
        return f"ledger_error: {type(e).__name__}: {e}"

def main():
    key = load_key()
    done = done_set()
    order = [(rep, q, cond) for rep in REPS for q in QIDS for cond in CONDS]
    cum_cost = cum_in = cum_out = attempts = 0
    RESULTS.parent.mkdir(parents=True, exist_ok=True)
    print(f"pilot start: {len(order)} planned, {len(done)} already done", flush=True)
    for rep, q, cond in order:
        if (q, cond, rep) in done:
            continue
        if attempts >= ATTEMPT_CAP or cum_cost >= COST_CAP or cum_in >= INPUT_TOK_CAP or cum_out >= OUTPUT_TOK_CAP:
            print(f"CAP REACHED before task {q} {cond} r{rep}: attempts={attempts} cost={cum_cost:.4f}", flush=True)
            break
        frozen = json.loads((FROZEN / f"task_{q}_{cond}.json").read_text(encoding="utf-8"))
        messages = frozen["messages"]
        t0 = time.time(); attempts += 1
        row = {"task": q, "cond": cond, "rep": rep, "model": MODEL, "temperature": TEMP,
               "frozen_file": f"task_{q}_{cond}.json",
               "ts": datetime.datetime.now().isoformat(timespec="seconds")}
        try:
            resp = call(key, messages)
            msg = resp["choices"][0]["message"]
            content = msg.get("content", "")
            reasoning = msg.get("reasoning_content")
            usage = resp.get("usage", {})
            in_tok = int(usage.get("prompt_tokens", 0)); out_tok = int(usage.get("completion_tokens", 0))
            cost = in_tok * IN_RATE + out_tok * OUT_RATE
            cum_in += in_tok; cum_out += out_tok; cum_cost += cost
            row.update({"ok": True, "error": None,
                        "finish_reason": resp["choices"][0].get("finish_reason"),
                        "prompt_tokens": in_tok, "completion_tokens": out_tok,
                        "cost_est_usd": round(cost, 6), "cum_cost_est_usd": round(cum_cost, 6),
                        "answer": content, "has_reasoning": bool(reasoning),
                        "reasoning_len": len(reasoning) if reasoning else 0,
                        "answer_len": len(content or ""), "redo": (q, cond, rep) in [],
                        "elapsed_s": round(time.time() - t0, 1)})
            led = ledger_append("ok", round(cost, 6), in_tok, out_tok,
                                {"task": q, "cond": cond, "rep": rep, "model": MODEL})
            row["ledger"] = led
            print(f"task {q} {cond} r{rep}: ok in={in_tok} out={out_tok} cost={cost:.5f} cum={cum_cost:.4f}", flush=True)
        except urllib.error.HTTPError as e:
            detail = e.read().decode("utf-8", "replace")[:300]
            row.update({"ok": False, "error": f"HTTP {e.code}: {detail}", "elapsed_s": round(time.time()-t0,1)})
            print(f"task {q} {cond} r{rep}: HTTP {e.code} {detail[:120]}", flush=True)
            with RESULTS.open("a", encoding="utf-8") as f:
                f.write(json.dumps(row, ensure_ascii=False) + "\n")
            if e.code in (401, 403, 404):
                print("AUTH/MODEL error on this call -> aborting run to preserve config integrity.", flush=True)
                break
            continue
        except Exception as e:
            row.update({"ok": False, "error": f"{type(e).__name__}: {e}", "elapsed_s": round(time.time()-t0,1)})
            print(f"task {q} {cond} r{rep}: ERR {type(e).__name__}: {e}", flush=True)
            with RESULTS.open("a", encoding="utf-8") as f:
                f.write(json.dumps(row, ensure_ascii=False) + "\n")
            continue
        with RESULTS.open("a", encoding="utf-8") as f:
            f.write(json.dumps(row, ensure_ascii=False) + "\n")
    print(f"PILOT DONE. attempts={attempts} cum_cost_est=${cum_cost:.4f} in_tok={cum_in} out_tok={cum_out}", flush=True)

if __name__ == "__main__":
    main()
