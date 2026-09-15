#!/usr/bin/env python3
"""round_S4 EXPLORATORY diagnostic (runs only after the frozen 12 cells; not a flow, no drafting).
Observed: the T1 source-constraint check (max_tokens 4096) exhausted its completion budget on reasoning in some cells and returned
empty content, which the runner parses as 'no queries'. This script re-issues the SAME check prompt on the SAME saved context
with a larger completion cap, then runs the SAME struct re-retrieval locally (no LLM) to see whether the returned queries would
have added the decisive paper passage. Also optionally probes the provider's max_tokens ceiling with a trivial prompt.
Costs are recorded in the ledger under exp_key evidence-package-pilot-roundS4 with tag 'diag:*'. Results: runs_s4/diag/.
Usage: python diag_check_cap_s4.py --cells B6_C_T1,B3_P_T1 --max-tokens 8192 [--variant T1] [--cap-probe 16384]"""
from __future__ import annotations
import os, sys, re, json, time, pathlib, argparse, asyncio, urllib.request, urllib.error
ROOT = pathlib.Path(__file__).resolve().parent; sys.path.insert(0, str(ROOT))
import run_round_s4 as R
DIAG = R.RUNS / "diag"

def cap_probe(guard, n):
    """Ask for max_tokens=n on a trivial prompt; report whether the API accepts it (HTTP 400 => ceiling below n)."""
    body = json.dumps({"model": R.MODEL, "messages": [{"role": "user", "content": "Reply with the single word OK."}], "temperature": 0.0, "max_tokens": n}).encode("utf-8")
    req = urllib.request.Request("https://api.deepseek.com/chat/completions", data=body, headers={"Content-Type": "application/json", "Authorization": "Bearer " + R.key()})
    try:
        resp = json.loads(urllib.request.urlopen(req, timeout=120).read().decode("utf-8"))
        u = resp.get("usage") or {}; pt, ct = int(u.get("prompt_tokens", 0)), int(u.get("completion_tokens", 0)); cost = pt * R.IN_RATE + ct * R.OUT_RATE
        guard.record(cost, pt, ct, data={"stage": "roundS4", "variant": "diag", "tag": f"diag:cap-probe-{n}"}, est_cost=cost, est_out=ct)
        out = {"max_tokens_requested": n, "accepted": True, "finish_reason": resp["choices"][0].get("finish_reason"), "content": (resp["choices"][0].get("message") or {}).get("content", "")[:50], "usage": u}
    except urllib.error.HTTPError as e:
        out = {"max_tokens_requested": n, "accepted": False, "http_status": e.code, "body": e.read().decode("utf-8", "replace")[:400]}
    (DIAG / f"cap_probe_{n}.json").write_text(json.dumps(out, indent=2, ensure_ascii=False), encoding="utf-8"); print("CAP PROBE:", out, flush=True); return out

async def recheck(cell, max_tokens, variant, guard):
    from gpt_researcher.document.document import DocumentLoader
    from gpt_researcher import GPTResearcher
    import contract as C, offline_retriever
    cdir = R.RUNS / cell; meta = json.loads((cdir / "meta.json").read_text(encoding="utf-8")); t = meta["task"]
    ctx0 = (cdir / "context.txt").read_text(encoding="utf-8")
    if meta.get("check", {}).get("added_chars"): ctx0 = ctx0[: len(ctx0) - meta["check"]["added_chars"] - 2]   # strip the appended follow-up text
    prompt = R.CHECK_PROMPT[variant].format(q=meta["question"], ctx=ctx0[:60000])
    ans, cost, pt, ct, fin = R.deepseek_call(prompt, guard, f"{cell}:diag-check{max_tokens}", DIAG / f"{cell}_check{max_tokens}.json", max_tokens, "diag")
    qs = R.parse_queries(ans)
    out = {"cell": cell, "variant_prompt": variant, "max_tokens": max_tokens, "finish_reason": fin, "completion_tokens": ct, "answer": ans.strip()[:500], "queries": qs, "cost_usd": round(cost, 6)}
    if qs:
        # same struct re-retrieval as the runtime, with _SEEN pre-filled from the cell's context so only NEW chunks count
        dp = R.DOCP / meta["docpath_dir"]
        if not dp.exists(): dp, _ = R.build_docpath(t, meta["condition"], cell)
        C.install_curation_field_fix(); offline_retriever.install_offline_retriever(); R.apply_struct(True)
        for seg in re.split(r"(?=Source: document_[12]\.txt)", ctx0):
            m = re.match(r"Source: (document_[12]\.txt)\nTitle: \nContent: (.*)", seg, re.S)
            if m: R._SEEN.add((m.group(1), m.group(2).strip()))
        os.environ["DOC_PATH"] = str(dp)
        r = GPTResearcher(query=meta["question"], report_type="research_report", report_source="local")
        pages = await DocumentLoader(str(dp)).load(); added = []
        for q in qs: added.append(await r.context_manager.get_similar_content_by_query(q, pages))
        addtxt = "\n\n".join(a for a in added if a); R.apply_struct(False)
        d1 = " ".join(s for s in re.split(r"(?=Source: document_[12]\.txt)", addtxt) if s.startswith("Source: document_1.txt"))
        out.update({"added_chars": len(addtxt), "added_doc1": addtxt.count("Source: document_1.txt"), "added_doc2": addtxt.count("Source: document_2.txt"),
                    "paper_decisive_in_added_doc1": {k: (k.lower() in d1.lower()) for k in R.PAPER_KEY[t]}})
        (DIAG / f"{cell}_added{max_tokens}.txt").write_text(addtxt, encoding="utf-8")
    (DIAG / f"{cell}_recheck{max_tokens}.json").write_text(json.dumps(out, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"RECHECK {cell} cap={max_tokens}: fin={fin} ctok={ct} queries={qs} " + (f"added_doc1={out.get('added_doc1')} decisive={out.get('paper_decisive_in_added_doc1')}" if qs else "(no queries)"), flush=True)


async def reverify(cell, max_tokens, guard):
    """Re-issue the SAME T2 verification prompt on the SAME saved draft with a larger completion cap (no drafting, not a flow)."""
    cdir = R.RUNS / cell; meta = json.loads((cdir / "meta.json").read_text(encoding="utf-8")); t = meta["task"]
    draft = (cdir / "report_draft.md").read_text(encoding="utf-8")
    dp = R.DOCP / meta["docpath_dir"]
    if not dp.exists(): dp, _ = R.build_docpath(t, meta["condition"], cell)
    name, paper = R.primary_text(dp, t)
    prompt = R.VERIFY_PROMPT.format(q=meta["question"], paper=paper, draft=draft)
    ans, cost, pt, ct, fin = R.deepseek_call(prompt, guard, f"{cell}:diag-verify{max_tokens}", DIAG / f"{cell}_verify{max_tokens}.json", max_tokens, "diag")
    (DIAG / f"{cell}_revised{max_tokens}.md").write_text(ans, encoding="utf-8")
    out = {"cell": cell, "max_tokens": max_tokens, "finish_reason": fin, "completion_tokens": ct, "prompt_tokens": pt, "output_chars": len(ans), "cost_usd": round(cost, 6)}
    (DIAG / f"{cell}_reverify{max_tokens}.json").write_text(json.dumps(out, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"REVERIFY {cell} cap={max_tokens}: fin={fin} ctok={ct} out_chars={len(ans)} ${cost:.4f}", flush=True)

async def main(a):
    from ledger_guard import BudgetGuard
    DIAG.mkdir(exist_ok=True)
    guard = BudgetGuard(R.EXP_KEY, exp_prefix=R.PREFIX, call_cap=10**6, in_tok_cap=80_000_000, out_tok_cap=30_000_000); guard.cost_cap = R.round_cap()
    cur, calls, *_ = guard._totals(); print(f"COST ACCOUNTING: pilot* cum=${cur:.4f} ({calls} calls); round cap=${guard.cost_cap}", flush=True)
    if a.cap_probe: cap_probe(guard, a.cap_probe)
    for cell in [c for c in a.cells.split(",") if c]: await recheck(cell, a.max_tokens, a.variant, guard)
    for cell in [c for c in a.reverify.split(",") if c]: await reverify(cell, a.max_tokens, guard)
    cur, calls, *_ = guard._totals(); print(f"DIAG DONE: pilot* cum=${cur:.4f} ({calls} calls)", flush=True)

if __name__ == "__main__":
    ap = argparse.ArgumentParser(); ap.add_argument("--cells", default=""); ap.add_argument("--max-tokens", type=int, default=8192)
    ap.add_argument("--variant", default="T1"); ap.add_argument("--cap-probe", type=int, default=0); ap.add_argument("--reverify", default="")
    a = ap.parse_args(); R.setup_env(); asyncio.run(main(a))
