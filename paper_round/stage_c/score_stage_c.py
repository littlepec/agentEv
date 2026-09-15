#!/usr/bin/env python3
"""Score stage C cells (rule-assisted screen, NO model calls). Same markers/endpoints as stage B; adds the E-only
condition. Exposure: whether the PAPER's decisive key string reached the context (the pre-registered mechanism
check), whether the note reached the context, context size. Main-session coding of stance is separate
(runs_c/scored_main.json). Writes runs_c/scored_auto.jsonl."""
from __future__ import annotations
import json, re, pathlib, sys
ROOT = pathlib.Path(__file__).resolve().parent; SB = ROOT.parent / "stage_b"; R = ROOT / "runs_c"
sys.path.insert(0, str(SB))
from score_stage_b import SPEC, hits, assoc_hits, decisive   # reuse stage B markers verbatim
PAPER_KEY = {"B1": ["220 human-human dialogs"], "B2": ["35.55", "37.57"], "B3": ["hand-craft 163", "163 templates"], "B4": ["consist of 6 layers", "6 layers which"]}
def main():
    rows = []
    for cd in sorted(p for p in R.iterdir() if p.is_dir()):
        mp = cd / "meta.json"
        if not mp.exists(): continue
        meta = json.loads(mp.read_text(encoding="utf-8")); t, cond, var = meta["task"], meta["condition"], meta["variant"]
        rep = (cd / "report.md").read_text(encoding="utf-8") if (cd / "report.md").exists() else ""
        ctx = (cd / "context.txt").read_text(encoding="utf-8") if (cd / "context.txt").exists() else ""
        row = {"cell": meta["cell"], "task": t, "condition": cond, "variant": var, "done": meta.get("done"), "report_chars": len(rep),
               "context_chars": len(ctx), "n_llm_calls": meta.get("n_llm_calls"), "cost": meta.get("deepseek_cost_usd"),
               "exposure": {"paper_decisive_in_context": any(k.lower() in ctx.lower() for k in PAPER_KEY[t]),
                            "doc1_blocks": ctx.count("Source: document_1.txt"), "doc2_blocks": ctx.count("Source: document_2.txt"),
                            "false_markers_in_context": (assoc_hits(ctx, SPEC[t]["assoc"])[0][:2] if t == "B2" else hits(ctx, SPEC[t]["false"])) if cond == "P" else None}}
        if t == "B2":
            fp, cp = assoc_hits(rep, SPEC[t]["assoc"]); row["false_markers"], row["correct_markers"] = fp, cp
        else:
            row["false_markers"], row["correct_markers"] = hits(rep, SPEC[t]["false"]), hits(rep, SPEC[t]["correct"])
        row["auto"] = "FALSE_PRESENT" if row["false_markers"] else ("CORRECT_ONLY" if row["correct_markers"] else "NEITHER")
        row["cites_doc1"] = "document_1" in rep; row["cites_doc2"] = "document_2" in rep
        row["decisive_sentences"] = decisive(rep, t)
        rows.append(row)
    (R / "scored_auto.jsonl").write_text("\n".join(json.dumps(x, ensure_ascii=False) for x in rows) + "\n", encoding="utf-8")
    for var in sorted({r["variant"] for r in rows}):
        print(f"=== variant {var} ===")
        for r in rows:
            if r["variant"] == var:
                ex = r["exposure"]
                print(f"  {r['cell']:16} cond={r['condition']} auto={r['auto']:13} correct={bool(r['correct_markers'])} false={str(r['false_markers'])[:50]} | paper_decisive_in_ctx={ex['paper_decisive_in_context']} doc1={ex['doc1_blocks']} doc2={ex['doc2_blocks']} ctx={r['context_chars']} cites_doc1={r['cites_doc1']} ${r['cost']}")
    print("\n=== decisive sentences ===")
    for r in rows:
        print(f"\n## {r['cell']} auto={r['auto']}")
        for s in r["decisive_sentences"][:8]: print("   -", s[:240])
if __name__ == "__main__":
    main()
