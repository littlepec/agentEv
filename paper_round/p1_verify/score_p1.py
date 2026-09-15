#!/usr/bin/env python3
"""Rule-assisted screen for P1 rounds (NO model calls). Per snapshot x arm: pipeline status, target-fact markers in the final text
(evaluation-only SPEC, same anchors as round_S3/S4), patches split into target vs non-target, unverified marks, support source,
tokens/cost per stage. Main-session judgment is separate (runs_p1/<round>/scored_main.json). Usage: python score_p1.py --round dev1"""
from __future__ import annotations
import json, re, pathlib, argparse
ROOT = pathlib.Path(__file__).resolve().parent; RUNS = ROOT / "runs_p1"
SPEC = {
 "B3": {"anchor": ["template", "269", "209", "163", "103", "106"], "false": ["103 templates", "209 templates", "total of 209", "209 in total", "209 hand-crafted", "106 + 103", "106 and 103"],
        "correct": ["163 templates", "269 templates", "total of 269", "269 in total", "269 hand-crafted", "106 + 163", "106 and 163"], "target_words": ["103", "163", "209", "269"]},
 "B6": {"anchor": ["german", "88", "44", "pd patients", "czech", "pc-gita"], "false": ["44 pd patients", "44 pd", "44 hc", "44 healthy"],
        "correct": ["88 pd patients", "88 pd", "88 hc", "88 healthy"], "target_words": ["german", "germany"]},
}
def hits(text, keys): low = text.lower(); return [k for k in keys if k.lower() in low]
def target_sentences(text, task):
    """sentences that state the target relation (B6: German count; B3: domain-KB / total template count)"""
    out = []
    for u in re.split(r"(?<=[.!?])\s+", text.replace("\n", " ")):
        low = u.lower()
        if task == "B6" and re.search(r"german|germany", low) and re.search(r"\b(44|88)\b", low): out.append(u.strip()[:260])
        if task == "B3" and re.search(r"\b(103|163|209|269)\b", low): out.append(u.strip()[:260])
    return out
def main(rnd):
    rdir = RUNS / rnd; rows = []
    for sdir in sorted(p for p in rdir.iterdir() if p.is_dir()):
        for adir in sorted(p for p in sdir.iterdir() if p.is_dir()):
            rp = adir / "result.json"
            if not rp.exists(): continue
            r = json.loads(rp.read_text(encoding="utf-8")); t = r["task"]; final = (adir / "final.md").read_text(encoding="utf-8")
            ap = r.get("patches_applied") or []; rj = r.get("patches_rejected") or []
            tgt = [p for p in ap if any(w in (p.get("old_str") or "").lower() for w in SPEC[t]["target_words"]) and (t != "B6" or re.search(r"\b(44|88)\b", p.get("old_str") or ""))]
            row = {"snapshot": r["snapshot"], "arm": r["arm"], "task": t, "cond": r["cond"], "final_status": r["final_status"], "stages": r["stages"],
                   "false_markers_final": hits(final, SPEC[t]["false"]), "correct_markers_final": hits(final, SPEC[t]["correct"]),
                   "unverified_marks": final.count("[not verified against the primary source]"), "annotations": final.count("[document_1.txt states"),
                   "patches_applied": len(ap), "patches_target": len(tgt), "patches_non_target": len(ap) - len(tgt), "patches_rejected": [x.get("why") for x in rj],
                   "n_claims": len(r.get("claims") or []), "labels": (lambda f: {k: sum(1 for v in f.values() if v.get("label") == k) for k in ("Entailment", "Contradiction", "Neutral", "UNCHECKED_CAP")})(r.get("final_labels") or {}),
                   "retrieval": r.get("retrieval"), "n_calls": r["n_calls"], "prompt_tokens": r["prompt_tokens"], "completion_tokens": r["completion_tokens"], "cost": r["cost_usd"],
                   "calls": [(c["tag"].split(":")[-1], c["status"], c["finish_reason"], c["prompt_tokens"], c["completion_tokens"]) for c in r["calls"]],
                   "target_sentences_final": target_sentences(final, t)[:6], "target_patches": [{"action": p["action"], "old": (p.get("old_str") or "")[:160], "new": (p.get("new_str") or "")[:200]} for p in tgt]}
            rows.append(row)
    (rdir / "scored_auto.jsonl").write_text("\n".join(json.dumps(x, ensure_ascii=False) for x in rows) + "\n", encoding="utf-8")
    for r in rows:
        print(f"=== {r['snapshot']:13} {r['arm']:9} {r['final_status']:24} false={r['false_markers_final']} correct={str(r['correct_markers_final'])[:40]} unverified={r['unverified_marks']} annot={r['annotations']} "
              f"patches={r['patches_applied']} (target {r['patches_target']}, other {r['patches_non_target']}, rejected {r['patches_rejected']}) claims={r['n_claims']} labels={r['labels']} calls={r['n_calls']} ptok={r['prompt_tokens']} ${r['cost']:.4f}")
        for c in r["calls"]: print(f"      call {c}")
        for p in r["target_patches"]: print(f"      TARGET PATCH [{p['action']}] {p['old'][:120]}  ==>  {p['new'][:160]}")
        for s in r["target_sentences_final"][:3]: print(f"      final: {s[:200]}")
if __name__ == "__main__":
    ap = argparse.ArgumentParser(); ap.add_argument("--round", default="dev1"); main(ap.parse_args().round)
