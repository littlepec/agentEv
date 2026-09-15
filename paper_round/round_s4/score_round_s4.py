#!/usr/bin/env python3
"""Rule-assisted screen for round_S4 cells (NO model calls). Markers per task (same SPEC as round_S3 for B3/B6); exposure =
decisive paper text in the drafting context (document_1 blocks only), in the follow-up additions, and in the T2 verification
input; check / verify metadata. For T2 the draft report is screened as well as the final. Main-session stance coding is separate
(runs_s4/scored_main.json, AI first pass, human_reviewed=false). Writes runs_s4/scored_auto.jsonl."""
from __future__ import annotations
import json, re, pathlib
ROOT = pathlib.Path(__file__).resolve().parent; R = ROOT / "runs_s4"
SPEC = {
 "B3": {"anchor": ["template", "269", "209", "163", "103", "106"], "false": ["103 templates", "209 templates", "total of 209", "209 in total", "209 hand-crafted", "106 + 103", "106 and 103"],
        "correct": ["163 templates", "269 templates", "total of 269", "269 in total", "269 hand-crafted", "106 + 163", "106 and 163"], "paper": ["hand-craft 163", "163 templates"]},
 "B6": {"anchor": ["german", "88", "44", "pd patients", "czech", "pc-gita"], "false": ["44 pd patients", "44 pd", "44 hc", "44 healthy"],
        "correct": ["88 pd patients", "88 pd", "88 hc", "88 healthy"], "paper": ["88 PD patients and 88 HC"]},
}
def units(text):
    out = []
    for line in text.replace("\r", "").split("\n"): out.extend(s.strip() for s in re.split(r"(?<=[.!?])\s+", line) if s.strip())
    return out
def hits(text, keys): low = text.lower(); return [k for k in keys if k.lower() in low]
def decisive(text, task): return [u[:240] for u in units(text) if any(a in u.lower() for a in SPEC[task]["anchor"])][:10]
def doc1_only(ctx): return " ".join(seg for seg in re.split(r"(?=Source: document_[12]\.txt)", ctx) if seg.startswith("Source: document_1.txt"))
def main():
    rows = []
    for cd in sorted(p for p in R.iterdir() if p.is_dir()):
        mp = cd / "meta.json"
        if not mp.exists(): continue
        meta = json.loads(mp.read_text(encoding="utf-8")); t, cond, var = meta["task"], meta["condition"], meta["variant"]
        rep = (cd / "report.md").read_text(encoding="utf-8") if (cd / "report.md").exists() else ""
        drf = (cd / "report_draft.md").read_text(encoding="utf-8") if (cd / "report_draft.md").exists() else None
        ctx = (cd / "context.txt").read_text(encoding="utf-8") if (cd / "context.txt").exists() else ""
        d1 = doc1_only(ctx); chk = meta.get("check") or {}; ver = meta.get("verify") or {}
        row = {"cell": meta["cell"], "task": t, "condition": cond, "variant": var, "done": meta.get("done"), "report_chars": len(rep), "context_chars": len(ctx),
               "n_llm_calls": meta.get("n_llm_calls"), "cost": meta.get("deepseek_cost_usd"), "total_prompt_tokens": meta.get("total_prompt_tokens"),
               "exposure": {"paper_decisive_in_drafting_ctx": {k: (k.lower() in d1.lower()) for k in SPEC[t]["paper"]},
                            "doc1_blocks": ctx.count("Source: document_1.txt"), "doc2_blocks": ctx.count("Source: document_2.txt"),
                            "false_in_context": hits(ctx, SPEC[t]["false"]) if cond == "P" else None,
                            "check": {k: chk.get(k) for k in ("kind", "answer", "queries", "added_doc1", "added_doc2", "paper_decisive_in_added", "finish_reason")} if chk else None,
                            "verify": {k: ver.get(k) for k in ("finish_reason", "input_chars", "output_chars", "completion_tokens", "fallback_to_draft")} if ver else None},
               "false_markers": hits(rep, SPEC[t]["false"]), "correct_markers": hits(rep, SPEC[t]["correct"]), "cites_doc1": "document_1" in rep,
               "draft_false_markers": (hits(drf, SPEC[t]["false"]) if drf is not None else None), "draft_correct_markers": (hits(drf, SPEC[t]["correct"]) if drf is not None else None)}
        row["auto"] = "FALSE_PRESENT" if row["false_markers"] else ("CORRECT_ONLY" if row["correct_markers"] else "NEITHER")
        row["decisive_sentences"] = decisive(rep, t); rows.append(row)
    (R / "scored_auto.jsonl").write_text("\n".join(json.dumps(x, ensure_ascii=False) for x in rows) + "\n", encoding="utf-8")
    for var in ("T0", "T1", "T2"):
        sub = [r for r in rows if r["variant"] == var]
        if not sub: continue
        print(f"=== {var} ===")
        for r in sub:
            ex = r["exposure"]; c = ex["check"]; v = ex["verify"]
            print(f"  {r['cell']:10} auto={r['auto']:13} correct={str(r['correct_markers'])[:40]} false={str(r['false_markers'])[:40]} | draft_false={r['draft_false_markers']} "
                  f"| paper_in_draft_ctx={ex['paper_decisive_in_drafting_ctx']} doc1={ex['doc1_blocks']} doc2={ex['doc2_blocks']} ptok={r['total_prompt_tokens']} ${r['cost']}"
                  + (f" | check={c['kind']} q={c['queries']} +doc1={c['added_doc1']} +doc2={c['added_doc2']} dec_added={c.get('paper_decisive_in_added')}" if c else "")
                  + (f" | verify fin={v['finish_reason']} out={v['output_chars']} ctok={v['completion_tokens']} fallback={v['fallback_to_draft']}" if v else ""))
if __name__ == "__main__":
    main()
