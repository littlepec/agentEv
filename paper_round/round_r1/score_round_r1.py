#!/usr/bin/env python3
"""Rule-assisted screen for round_R1 cells (NO model calls). Markers reuse stage B (B1) and round_S3 (B3/B5/B6/B7) specs verbatim;
exposure = decisive paper text in the window (verbatim and digit-space-normalized); the report's decisive sentences are printed
for the main-session stance coding (runs_r1/scored_main.json, AI first pass, human_reviewed=false). Writes runs_r1/scored_auto.jsonl."""
from __future__ import annotations
import json, re, pathlib, sys
ROOT = pathlib.Path(__file__).resolve().parent; R = ROOT / "runs_r1"; PR = ROOT.parent
sys.path.insert(0, str(PR / "stage_b")); sys.path.insert(0, str(PR / "round_s3"))
from score_stage_b import SPEC as SPEC_B
from score_round_s3 import SPEC as SPEC_S3
SPEC = {"B1": SPEC_B["B1"], **{k: SPEC_S3[k] for k in ("B3", "B5", "B6", "B7")}}
def units(text):
    out = []
    for line in text.replace("\r", "").split("\n"): out.extend(s.strip() for s in re.split(r"(?<=[.!?])\s+", line) if s.strip())
    return out
def hits(text, keys): low = text.lower(); return [k for k in keys if k.lower() in low]
def decisive(text, task): return [u[:240] for u in units(text) if any(a in u.lower() for a in SPEC[task]["anchor"])][:8]
def main():
    rows = []
    for cd in sorted(p for p in R.iterdir() if p.is_dir()):
        mp = cd / "meta.json"
        if not mp.exists(): continue
        meta = json.loads(mp.read_text(encoding="utf-8")); t, lv, cond = meta["task"], meta["level"], meta["condition"]
        rep = (cd / "report.md").read_text(encoding="utf-8") if (cd / "report.md").exists() else ""
        row = {"cell": meta["cell"], "task": t, "level": lv, "condition": cond, "done": meta.get("done"), "report_chars": len(rep), "context_chars": meta.get("context_chars"),
               "cost": meta.get("deepseek_cost_usd"), "prompt_tokens": meta.get("prompt_tokens"),
               "exposure_verbatim": meta.get("paper_decisive_in_context_verbatim"), "exposure_digitnorm": meta.get("paper_decisive_in_context_digitnorm"),
               "false_markers": hits(rep, SPEC[t]["false"]), "correct_markers": hits(rep, SPEC[t]["correct"]), "cites_doc1": "document_1" in rep,
               "abstain_phrases": hits(rep, ["could not gather", "no source material", "insufficient information", "unable to determine"])}
        row["auto"] = "FALSE_PRESENT" if row["false_markers"] else ("CORRECT_ONLY" if row["correct_markers"] else "NEITHER")
        row["decisive_sentences"] = decisive(rep, t); rows.append(row)
    (R / "scored_auto.jsonl").write_text("\n".join(json.dumps(x, ensure_ascii=False) for x in rows) + "\n", encoding="utf-8")
    for lv in (0, 1, 2, 3):
        sub = [r for r in rows if r["level"] == lv]
        if not sub: continue
        print(f"=== L{lv} ===")
        for r in sub:
            print(f"  {r['cell']:10} auto={r['auto']:13} correct={str(r['correct_markers'])[:44]} false={str(r['false_markers'])[:44]} | exp_verb={r['exposure_verbatim']} exp_norm={r['exposure_digitnorm']} rep={r['report_chars']} ptok={r['prompt_tokens']} ${r['cost']}")
            for s in r["decisive_sentences"][:3]: print(f"        > {s[:200]}")
if __name__ == "__main__":
    main()
