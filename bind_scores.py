#!/usr/bin/env python3
"""Fix (2): bind each score label to the ACTUAL model output hash and the evidence location.

The hardcoded label tables inside score*.py / score_reaudit_v7.py / score_taskB.py and the
human_review_v8.jsonl are ANNOTATION EXPORTS (AI-initial, or human where marked) — NOT an
independent automated verifier. This script makes those annotations auditable by joining each
labeled cell to: the sha256 of the exact answer bytes it refers to, and the frozen input file
(which holds the exact sources shown) + the underlying evidence file paths.

Output: runs/scored_bound.jsonl (one row per labeled cell). No model calls.
"""
from __future__ import annotations
import json, hashlib, pathlib

ROOT = pathlib.Path(__file__).resolve().parent
R = ROOT / "runs"
OUT = R / "scored_bound.jsonl"

def sha(b): return hashlib.sha256(b).hexdigest()
def fhash(p):
    p = pathlib.Path(p)
    return sha(p.read_bytes()) if p.exists() else None

# cond -> (results_file, match{field:value}, frozen_file_tmpl, evidence_files_tmpl)
COND = {
 "S_CP":   ("pilot_results.jsonl",  {"cond":"CP"},      "frozen/task_{q}_CP.json",
            ["packs/task_{q}/public/evidence/evidence_1.txt","packs/task_{q}/public/poison_source.txt"]),
 "N_CP":   ("pilot2_results.jsonl", {"combo":"N_CP"},   "frozen2/task_{q}_N_CP.json",
            ["packs/task_{q}/public/evidence/evidence_1.txt","packs/task_{q}/public/poison_source.txt"]),
 "S2_CP":  ("pilot6_results.jsonl", {"combo":"S2_CP"},  "frozen6/task_{q}_S2_CP.json",
            ["packs/task_{q}/public/evidence/evidence_1.txt","packs/task_{q}/public/poison_source.txt"]),
 "S_C0S":  ("pilot5_results.jsonl", {"combo":"S_C0S"},  "frozen5/task_{q}_S_C0S.json",
            ["packs/task_{q}/public/evidence_sufficient.txt"]),
 "N_C0S":  ("pilot5_results.jsonl", {"combo":"N_C0S"},  "frozen5/task_{q}_N_C0S.json",
            ["packs/task_{q}/public/evidence_sufficient.txt"]),
 "S2_C0S": ("pilot6_results.jsonl", {"combo":"S2_C0S"}, "frozen6/task_{q}_S2_C0S.json",
            ["packs/task_{q}/public/evidence_sufficient.txt"]),
 # task beta curated draft: input assembled at runtime (recorded in sent_messages), no frozen file
 "S2_CP_curated": (None, None, None, None),
}

def best_answer(results_file, match, task, rep):
    p = R / results_file
    if not p.exists(): return None
    best = None
    for l in p.read_text(encoding="utf-8").splitlines():
        if not l.strip(): continue
        r = json.loads(l)
        if not r.get("ok"): continue
        if r.get("task") != task or r.get("rep") != rep: continue
        if any(r.get(k) != v for k, v in (match or {}).items()): continue
        a = (r.get("answer") or "")
        if not a.strip(): continue
        sc = (2 if r.get("finish_reason") == "stop" else 1, len(a))
        if best is None or sc > best[0]: best = (sc, r)
    return best[1] if best else None

def bind_cell(source, task, cond, rep, labels):
    spec = COND.get(cond)
    rows = []
    if spec and spec[0]:
        results_file, match, frozen_tmpl, ev_tmpl = spec
        r = best_answer(results_file, match, task, rep)
        ans = (r or {}).get("answer")
        frozen = frozen_tmpl.format(q=task)
        ev = [e.format(q=task) for e in ev_tmpl]
        return {
            "source_annotation": source, "task": task, "cond": cond, "rep": rep,
            "labels": labels,
            "output_sha256": sha(ans.encode("utf-8")) if ans else None,
            "output_present": bool(ans),
            "results_file": results_file, "finish_reason": (r or {}).get("finish_reason"),
            "evidence_locator": {"frozen_input": frozen, "frozen_input_sha256": fhash(R/frozen),
                                 "evidence_files": ev,
                                 "evidence_sha256": {e: fhash(ROOT/e) for e in ev}},
            "binding_status": "BOUND" if ans else "OUTPUT_MISSING",
            "provenance": "ANNOTATION_EXPORT (hardcoded label table; AI-initial or human-marked; NOT independent auto-verification)",
        }
    # curated_draft (taskB): input in sent_messages, evidence = evidence_1 + poison + runtime curation verdict
    r = None
    p = R / "taskB_results.jsonl"
    if p.exists():
        for l in p.read_text(encoding="utf-8").splitlines():
            if not l.strip(): continue
            rr = json.loads(l)
            if rr.get("ok") and rr.get("stage")=="curated_draft" and rr.get("task")==task and rr.get("rep")==rep:
                r = rr; break
    ans = (r or {}).get("answer")
    sent = (r or {}).get("sent_messages")
    return {
        "source_annotation": source, "task": task, "cond": cond, "rep": rep, "labels": labels,
        "output_sha256": sha(ans.encode("utf-8")) if ans else None, "output_present": bool(ans),
        "results_file": "taskB_results.jsonl", "finish_reason": (r or {}).get("finish_reason"),
        "evidence_locator": {"runtime_input_sha256": sha(json.dumps(sent,ensure_ascii=False).encode()) if sent else None,
                             "evidence_files": [f"packs/task_{task}/public/evidence/evidence_1.txt",
                                                f"packs/task_{task}/public/poison_source.txt"],
                             "note":"curated_draft input assembled at runtime (evidence_1+poison+curation verdict); full sent_messages in taskB_results.jsonl"},
        "binding_status": "BOUND" if ans else "OUTPUT_MISSING",
        "provenance": "ANNOTATION_EXPORT (curation-stage pilot; AI-initial; NOT independent auto-verification)",
    }

def main():
    out = []
    # v7 reaudit (48 cells): fields axisA_stance5 / axisB_coverage / review_status
    p = R / "scored_reaudit_v7.jsonl"
    for l in p.read_text(encoding="utf-8").splitlines():
        if not l.strip(): continue
        s = json.loads(l)
        labels = {k: s.get(k) for k in ("axisA_stance5","axisB_coverage","truth_basis","review_status","border_item")}
        out.append(bind_cell("scored_reaudit_v7.jsonl", s["task"], s["cond"], s["rep"], labels))
    # taskB curated_draft (8 cells)
    p = R / "scored_taskB.jsonl"
    if p.exists():
        for l in p.read_text(encoding="utf-8").splitlines():
            if not l.strip(): continue
            s = json.loads(l)
            labels = {k: s.get(k) for k in ("axisA_stance5","axisB_coverage","curation_flagged_B_low","review_status")}
            out.append(bind_cell("scored_taskB.jsonl", s["task"], "S2_CP_curated", s["rep"], labels))
    # human review (9 cells): overlay human labels onto the same bound cells (by task/cond/rep)
    p = R / "human_review_v8.jsonl"
    if p.exists():
        for l in p.read_text(encoding="utf-8").splitlines():
            if not l.strip(): continue
            s = json.loads(l)
            labels = {"human_axisA": s.get("human_axisA"), "human_axisB": s.get("human_axisB"),
                      "review_status": s.get("review_status"), "item": s.get("item")}
            out.append(bind_cell("human_review_v8.jsonl", s["task"], s["cond"], s["rep"], labels))

    OUT.write_text("\n".join(json.dumps(x, ensure_ascii=False) for x in out) + "\n", encoding="utf-8")
    bound = sum(1 for x in out if x["binding_status"]=="BOUND")
    miss  = sum(1 for x in out if x["binding_status"]!="BOUND")
    print(f"wrote {OUT.name}: {len(out)} annotated cells bound; BOUND={bound} MISSING={miss}")
    if miss:
        for x in out:
            if x["binding_status"]!="BOUND":
                print("  MISSING:", x["source_annotation"], x["task"], x["cond"], x["rep"])

if __name__ == "__main__":
    main()
