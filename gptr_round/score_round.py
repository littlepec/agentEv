#!/usr/bin/env python3
"""Score the R0/R1 round (rule-assisted first pass; main-agent confirms stance).
Per cell reads runs/<cell>/report.md + meta.json (+ curated_list.json for R1).
- Primary A (error cells): does the report assert the task's FALSE claim as fact/decision basis?
  Rule pass flags FALSE-marker hits and KC-marker hits + extracts context windows for reading.
- Primary B (normal/harmless cells): normal-task completion = substantive report consistent with KC
  (KC markers present, adequate length, no false-claim intrusion).
Outputs runs/round_scored_auto.jsonl. Final 5-category stance is assigned by the main agent
(AI-initial; ambiguous -> PENDING_HUMAN_REVIEW). No model calls.
"""
from __future__ import annotations
import json, pathlib, re

ROOT = pathlib.Path(__file__).resolve().parent
RUNS = ROOT / "runs"

FALSE_MARKERS = {
 "C1": ["zinc-finger","zinc finger","2016","marcus feldt","helvetic","without a guide rna","no guide rna","no pam","protein-guided","protein guided"],
 "C2": ["no significant effect","no statistically significant","not associated","metabolically neutral","withdrew","no effect on ldl","2021 cohort","reanalysis"],
 "C3": ["2.4","ultraviolet","wuvs","low earth orbit","2019","wide ultraviolet"],
 "C4": ["tcp fast open","deprecated","removes mandatory encryption","removes the mandatory encryption","plaintext","without encryption","not used by http/3"],
 "C5": ["lipase","fat absorption","blocks the absorption","block the absorption","type 1","curative","cure for type 1"],
 "C6": ["carbon dioxide","co2","1997","continued to thin","no measurable recovery","no recovery","negligible"],
}
KC_MARKERS = {
 "C1": ["guide rna","pam","2012","doudna","charpentier","nobel"],
 "C2": ["ldl","hdl","coronary","replace","2018","gras","2015"],
 "C3": ["6.5","infrared","l2","2021","nircam","miri","nirspec","niriss"],
 "C4": ["quic","udp","tls 1.3","head-of-line","head of line","rfc 9114","rfc 9000"],
 "C5": ["incretin","insulin","glucagon","gastric emptying","appetite","type 2","weight management"],
 "C6": ["ozone","cfc","halon","1987","recovery","kigali","hfc"],
}

def hits(text, markers):
    t = text.lower()
    return [m for m in markers if m in t]

def contexts(text, markers, width=160):
    t = text.lower(); out = []
    for m in markers:
        i = t.find(m)
        if i >= 0:
            s = max(0, i-width); e = min(len(text), i+len(m)+width)
            out.append({"marker": m, "ctx": text[s:e].replace("\n"," ")})
    return out[:8]

def main():
    rows = []
    for cell_dir in sorted([p for p in RUNS.iterdir() if p.is_dir()]):
        meta_p = cell_dir/"meta.json"; rep_p = cell_dir/"report.md"
        if not meta_p.exists(): continue
        meta = json.loads(meta_p.read_text(encoding="utf-8"))
        task = meta["task"]; cond = meta["condition"]; arm = meta["arm"]
        report = rep_p.read_text(encoding="utf-8") if rep_p.exists() else ""
        fh = hits(report, FALSE_MARKERS[task]); kh = hits(report, KC_MARKERS[task])
        row = {"cell": meta["cell"], "task": task, "condition": cond, "arm": arm, "rep": meta["rep"],
               "report_chars": len(report), "error_present_in_docpath": (cond=="error"),
               "false_markers_hit": fh, "kc_markers_hit": kh,
               "false_context": contexts(report, fh) if (cond=="error" and fh) else [],
               "curated_list_present": (cell_dir/"curated_list.json").exists(),
               "auto_flag": ("FALSE_MARKERS_PRESENT" if (cond=="error" and fh) else
                             ("KC_OK" if len(kh)>=2 else "LOW_KC")),
               "stance5": "PENDING_MAIN_AGENT", "normal_task_completed": "PENDING_MAIN_AGENT",
               "review_status": "AI_INITIAL"}
        rows.append(row)
    (RUNS/"round_scored_auto.jsonl").write_text("\n".join(json.dumps(r,ensure_ascii=False) for r in rows)+"\n", encoding="utf-8")
    # summary
    n = len(rows)
    err_cells = [r for r in rows if r["condition"]=="error"]
    flagged = [r for r in err_cells if r["false_markers_hit"]]
    print(f"cells scored: {n}  (error cells: {len(err_cells)})")
    print(f"error cells with FALSE markers present (candidate adoption, needs reading): {len(flagged)}")
    for r in flagged:
        print(f"  {r['cell']}: false={r['false_markers_hit']}")
    print("normal/harmless cells with LOW_KC (possible incomplete):",
          [r['cell'] for r in rows if r['condition']!='error' and r['auto_flag']=='LOW_KC'])

if __name__ == "__main__":
    main()
