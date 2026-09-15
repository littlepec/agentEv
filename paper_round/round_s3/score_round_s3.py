#!/usr/bin/env python3
"""Rule-assisted screen for round_S3 cells (NO model calls). Markers per task; exposure = decisive paper text in
context (evaluation-only), note in context, follow-up trigger info. Main-session stance coding is separate
(runs_s3/scored_main.json). Writes runs_s3/scored_auto.jsonl."""
from __future__ import annotations
import json, re, pathlib
ROOT = pathlib.Path(__file__).resolve().parent; R = ROOT / "runs_s3"; SB = ROOT.parent / "stage_b"
SPEC = {
 "B3": {"anchor": ["template", "269", "209", "163", "103", "106"], "false": ["103 templates", "209 templates", "total of 209", "209 in total", "209 hand-crafted"],
        "correct": ["163 templates", "269 templates", "total of 269", "269 in total", "269 hand-crafted", "106 + 163", "106 and 163"], "paper": ["hand-craft 163", "163 templates"]},
 "B5": {"anchor": ["perplexity", "ppl", "bpc", "87.38", "92.98", "10.63", "4.91", "grurntn"], "false": ["92.98", "4.91%", "4.8 absolute"],
        "correct": ["87.38", "10.63%", "10.4 absolute"], "paper": ["97.78 to 87.38", "1.39 to 1.33"]},
 "B6": {"anchor": ["german", "88", "44", "pd patients", "czech", "pc-gita"], "false": ["44 pd patients", "44 pd", "44 hc"],
        "correct": ["88 pd patients", "88 pd", "88 hc"], "paper": ["88 PD patients and 88 HC"]},
 "B7": {"anchor": ["test set", "2,169", "3,003", "sentences", "news-test2015"], "false": ["3,003"], "correct": ["2,169"], "paper": ["2,169 sentences"]},
}
def units(text):
    out = []
    for line in text.replace("\r", "").split("\n"): out.extend(s.strip() for s in re.split(r"(?<=[.!?])\s+", line) if s.strip())
    return out
def hits(text, keys): low = text.lower(); return [k for k in keys if k.lower() in low]
def decisive(text, task): return [u[:240] for u in units(text) if any(a in u.lower() for a in SPEC[task]["anchor"])][:10]
def main():
    rows = []
    for cd in sorted(p for p in R.iterdir() if p.is_dir()):
        mp = cd / "meta.json"
        if not mp.exists(): continue
        meta = json.loads(mp.read_text(encoding="utf-8")); t, cond, var = meta["task"], meta["condition"], meta["variant"]
        rep = (cd / "report.md").read_text(encoding="utf-8") if (cd / "report.md").exists() else ""
        ctx = (cd / "context.txt").read_text(encoding="utf-8") if (cd / "context.txt").exists() else ""
        # decisive-paper check restricted to document_1 blocks (the faithful note L repeats the same strings in C cells)
        doc1_text = " ".join(seg for seg in re.split(r"(?=Source: document_[12]\.txt)", ctx) if seg.startswith("Source: document_1.txt"))
        row = {"cell": meta["cell"], "task": t, "condition": cond, "variant": var, "done": meta.get("done"), "report_chars": len(rep), "context_chars": len(ctx),
               "n_llm_calls": meta.get("n_llm_calls"), "cost": meta.get("deepseek_cost_usd"),
               "exposure": {"paper_decisive_in_context": {k: (k.lower() in doc1_text.lower()) for k in SPEC[t]["paper"]},
                            "doc1_blocks": ctx.count("Source: document_1.txt"), "doc2_blocks": ctx.count("Source: document_2.txt"),
                            "false_in_context": hits(ctx, SPEC[t]["false"]) if cond == "P" else None, "followup": meta.get("followup")},
               "false_markers": hits(rep, SPEC[t]["false"]), "correct_markers": hits(rep, SPEC[t]["correct"]), "cites_doc1": "document_1" in rep or "arxiv.org" in rep}
        row["auto"] = "FALSE_PRESENT" if row["false_markers"] else ("CORRECT_ONLY" if row["correct_markers"] else "NEITHER")
        row["decisive_sentences"] = decisive(rep, t); rows.append(row)
    (R / "scored_auto.jsonl").write_text("\n".join(json.dumps(x, ensure_ascii=False) for x in rows) + "\n", encoding="utf-8")
    for var in ("default", "struct", "followup", "fullwin"):
        sub = [r for r in rows if r["variant"] == var]
        if not sub: continue
        print(f"=== {var} ===")
        for r in sub:
            ex = r["exposure"]; fu = ex["followup"]
            print(f"  {r['cell']:16} auto={r['auto']:13} correct={bool(r['correct_markers'])} false={str(r['false_markers'])[:40]} | paper={ex['paper_decisive_in_context']} doc1={ex['doc1_blocks']} doc2={ex['doc2_blocks']} ctx={r['context_chars']} ${r['cost']}"
                  + (f" | fu={fu['queries']} +doc1={fu.get('added_doc1')} +doc2={fu.get('added_doc2')}" if fu else ""))
if __name__ == "__main__":
    main()
