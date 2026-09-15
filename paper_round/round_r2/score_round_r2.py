#!/usr/bin/env python3
"""Rule-assisted screen for round_R2 cells (NO model calls). Markers reuse stage B (B1) and round_S3 (B3/B5/B6/B7) specs verbatim;
exposure = decisive paper text in the window (verbatim / digit-normalized / token-window); the report's decisive sentences are
printed for the main-session stance coding (runs_r2/scored_main.json, AI first pass, human_reviewed=false). Writes runs_r2/scored_auto.jsonl."""
from __future__ import annotations
import json, re, pathlib, sys
ROOT = pathlib.Path(__file__).resolve().parent; R = ROOT / "runs_r2"; PR = ROOT.parent
sys.path.insert(0, str(PR / "stage_b")); sys.path.insert(0, str(PR / "round_s3"))
from score_stage_b import SPEC as SPEC_B
from score_round_s3 import SPEC as SPEC_S3
SPEC = {"B1": SPEC_B["B1"], **{k: SPEC_S3[k] for k in ("B3", "B5", "B6", "B7")}}
def units(text):
    out = []
    for line in text.replace("\r", "").split("\n"): out.extend(s.strip() for s in re.split(r"(?<=[.!?])\s+", line) if s.strip())
    return out
def hits(text, keys): low = text.lower(); return [k for k in keys if k.lower() in low]
PAPER_KEY = {"B1": ["220 human-human dialogs"], "B3": ["hand-craft 163", "163 templates"], "B5": ["97.78 to 87.38", "1.39 to 1.33"],
             "B6": ["88 PD patients and 88 HC"], "B7": ["2,169 sentences"]}
def norm_digits(s): return re.sub(r"(?<=\d) (?=\d)", "", s)
def tokwin(k, s):
    nd = norm_digits(s.lower()); toks = [x for x in re.findall(r"[a-z0-9]+", k.lower()) if len(x) >= 2]
    for m in re.finditer(re.escape(toks[0]), nd):
        seg = nd[m.start(): m.start() + 3 * len(k)]; pos = 0; ok = True
        for x in toks:
            j = seg.find(x, pos)
            if j < 0: ok = False; break
            pos = j + len(x)
        if ok: return True
    return False
def decisive(text, task): return [u[:240] for u in units(text) if any(a in u.lower() for a in SPEC[task]["anchor"])][:8]
def main():
    rows = []
    for cd in sorted(p for p in R.iterdir() if p.is_dir()):
        mp = cd / "meta.json"
        if not mp.exists(): continue
        meta = json.loads(mp.read_text(encoding="utf-8")); t, v, cond = meta["task"], meta["variant"], meta["condition"]
        rep = (cd / "report.md").read_text(encoding="utf-8") if (cd / "report.md").exists() else ""
        ctx = (cd / "context.txt").read_text(encoding="utf-8") if (cd / "context.txt").exists() else ""
        d1 = "\n".join(b for b in ctx.split("Source: ") if b.startswith("document_1"))   # what the model actually saw from the primary
        exp_ctx = {k: tokwin(k, d1) for k in PAPER_KEY[t]}
        row = {"cell": meta["cell"], "task": t, "variant": v, "condition": cond, "rep": meta.get("rep"), "done": meta.get("done"), "report_chars": len(rep),
               "context_chars": meta.get("context_chars"), "doc1_blocks": meta.get("doc1_blocks"), "cost": meta.get("deepseek_cost_usd"), "prompt_tokens": meta.get("prompt_tokens"),
               "exposure_verbatim": meta.get("paper_decisive_in_context_verbatim"), "exposure_digitnorm": meta.get("paper_decisive_in_context_digitnorm"),
               "exposure_tokwin": meta.get("paper_decisive_in_context_tokwin"), "exposure_ctx_tokwin": exp_ctx, "ctx_doc1_chars": len(d1),
               "false_markers": hits(rep, SPEC[t]["false"]), "correct_markers": hits(rep, SPEC[t]["correct"]), "cites_doc1": "document_1" in rep,
               "abstain_phrases": hits(rep, ["could not gather", "no source material", "insufficient information", "unable to determine"])}
        row["auto"] = "FALSE_PRESENT" if row["false_markers"] else ("CORRECT_ONLY" if row["correct_markers"] else "NEITHER")
        row["decisive_sentences"] = decisive(rep, t); rows.append(row)
    (R / "scored_auto.jsonl").write_text("\n".join(json.dumps(x, ensure_ascii=False) for x in rows) + "\n", encoding="utf-8")
    for v in sorted(set(r["variant"] for r in rows)):
        sub = [r for r in rows if r["variant"] == v]
        print(f"=== {v} ===")
        for r in sub:
            print(f"  {r['cell']:26} auto={r['auto']:13} correct={str(r['correct_markers'])[:44]} false={str(r['false_markers'])[:44]} | exp_verb={r['exposure_verbatim']} tokwin_loaded={r['exposure_tokwin']} tokwin_ctx={r['exposure_ctx_tokwin']} d1={r['doc1_blocks']} rep={r['report_chars']} ptok={r['prompt_tokens']} ${r['cost']}")
            for s in r["decisive_sentences"][:3]: print(f"        > {s[:200]}")
if __name__ == "__main__":
    main()
