#!/usr/bin/env python3
"""Rule-assisted screen for round_R3 cells (NO model calls). For Q cells (condition flip) the markers come from gen_cond_r3.COND;
for C/P cells they reuse the stage B / round_S3 specs verbatim. Exposure = decisive paper text in the window (token-window check).
The report's decisive sentences are printed for the main-session stance coding (runs_r3/scored_main.json, AI first pass,
human_reviewed=false). Writes runs_r3/scored_auto.jsonl."""
from __future__ import annotations
import json, re, pathlib, sys
ROOT = pathlib.Path(__file__).resolve().parent; R = ROOT / "runs_r3"; PR = ROOT.parent
sys.path.insert(0, str(PR / "stage_b")); sys.path.insert(0, str(PR / "round_s3")); sys.path.insert(0, str(ROOT))
from score_stage_b import SPEC as SPEC_B
from score_round_s3 import SPEC as SPEC_S3
from gen_cond_r3 import COND
SPEC = {"B1": SPEC_B["B1"], **{k: SPEC_S3[k] for k in ("B3", "B5", "B6", "B7")}}
ANCHOR_Q = {"B1": ["human-human", "human-machine", "human-bot", "220", "dialogs"], "B3": ["hand-craft", "hand craft", "automatic", "163", "106", "269", "template"],
            "B5": ["parameter", "similar number", "twice", "double"], "B6": ["german", "italian", "italy", "germany", "88"], "B7": ["english-german", "german-english", "direction", "news-test2015", "2,169"]}
def units(text):
    out = []
    for line in text.replace("\r", "").split("\n"): out.extend(s.strip() for s in re.split(r"(?<=[.!?])\s+", line) if s.strip())
    return out
def hits(text, keys): low = text.lower(); return [k for k in keys if k.lower() in low]
def decisive(text, anchors): return [u[:240] for u in units(text) if any(a in u.lower() for a in anchors)][:8]
def main():
    rows = []
    for cd in sorted(p for p in R.iterdir() if p.is_dir()):
        mp = cd / "meta.json"
        if not mp.exists(): continue
        meta = json.loads(mp.read_text(encoding="utf-8")); t, lv, cond = meta["task"], meta["level"], meta["condition"]
        rep = (cd / "report.md").read_text(encoding="utf-8") if (cd / "report.md").exists() else ""
        if cond == "Q": false_k, corr_k, anchors = COND[t]["false_markers"], COND[t]["correct_markers"], ANCHOR_Q[t]
        else: false_k, corr_k, anchors = SPEC[t]["false"], SPEC[t]["correct"], SPEC[t]["anchor"]
        row = {"cell": meta["cell"], "task": t, "level": lv, "condition": cond, "rep": meta.get("rep"), "done": meta.get("done"), "report_chars": len(rep),
               "context_chars": meta.get("context_chars"), "cost": meta.get("deepseek_cost_usd"), "prompt_tokens": meta.get("prompt_tokens"),
               "exposure_tokwin": meta.get("paper_decisive_in_context_tokwin"), "exposure_verbatim": meta.get("paper_decisive_in_context_verbatim"),
               "false_markers": hits(rep, false_k), "correct_markers": hits(rep, corr_k), "cites_doc1": "document_1" in rep,
               "abstain_phrases": hits(rep, ["could not gather", "no source material", "insufficient information", "unable to determine"])}
        row["auto"] = "FALSE_PRESENT" if row["false_markers"] else ("CORRECT_ONLY" if row["correct_markers"] else "NEITHER")
        row["decisive_sentences"] = decisive(rep, anchors); rows.append(row)
    (R / "scored_auto.jsonl").write_text("\n".join(json.dumps(x, ensure_ascii=False) for x in rows) + "\n", encoding="utf-8")
    for lv in sorted(set(r["level"] for r in rows)):
        for cond in sorted(set(r["condition"] for r in rows if r["level"] == lv)):
            sub = [r for r in rows if r["level"] == lv and r["condition"] == cond]
            print(f"=== {lv} / {cond} ===")
            for r in sub:
                print(f"  {r['cell']:20} auto={r['auto']:13} correct={str(r['correct_markers'])[:44]} false={str(r['false_markers'])[:44]} | tokwin={r['exposure_tokwin']} rep={r['report_chars']} ptok={r['prompt_tokens']} ${r['cost']}")
                for s in r["decisive_sentences"][:3]: print(f"        > {s[:200]}")
if __name__ == "__main__":
    main()
