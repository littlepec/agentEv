#!/usr/bin/env python3
"""ZERO-MODEL-CALL validity audit of the 72-cell round (commit 39b1b9b outputs kept intact).
Classifies each cell for TWO confounds + separates 4 metrics. Writes runs/audit_round.jsonl.
Confound 1: filename/label leakage (model sees 'error_material.txt' etc. as a Source id).
Confound 2: curated-list field-name mismatch -> empty-shell context (report from parametric knowledge).
4 metrics kept separate: report_returned / evidence_delivered / false_claim_adopted(needs read) /
grounded_task_completed. No re-run; no model calls."""
from __future__ import annotations
import json, pathlib, re

ROOT = pathlib.Path(__file__).resolve().parent; RUNS = ROOT / "runs"
FNAMES = ["error_material.txt","normal_sources.txt","harmless_supplement.txt"]
NO_SRC = re.compile(r"no source(s| packet| package)?|supplied no source|without (any )?(the )?provided source|no source materials|no provided source", re.I)

def load_json(p):
    try: return json.loads(pathlib.Path(p).read_text(encoding="utf-8"))
    except Exception: return None

def real_content_len(ctx_str):
    """chars remaining after stripping the Title/Content/Source scaffold, filenames, whitespace."""
    s = ctx_str
    for tok in ["Title:","Content:","Source:"] + FNAMES:
        s = s.replace(tok, "")
    return len(re.sub(r"\s+", "", s))

def main():
    rows=[]
    for cd in sorted([p for p in RUNS.iterdir() if p.is_dir()]):
        meta = load_json(cd/"meta.json")
        if not meta: continue
        cell=meta["cell"]; arm=meta["arm"]; cond=meta["condition"]; task=meta["task"]
        report=(cd/"report.md").read_text(encoding="utf-8") if (cd/"report.md").exists() else ""
        ctx = load_json(cd/"context.json")
        ctx_str = ctx if isinstance(ctx,str) else json.dumps(ctx,ensure_ascii=False) if ctx is not None else ""
        rc = real_content_len(ctx_str)
        leak_ctx=[f for f in FNAMES if f in ctx_str]
        leak_rep=[f for f in FNAMES if f in report]
        no_src = bool(NO_SRC.search(report[:800]))
        rec={"cell":cell,"task":task,"condition":cond,"arm":arm,"rep":meta["rep"],
             "filename_leak_in_context":leak_ctx,"filename_leak_in_report":leak_rep,
             "context_real_content_chars":rc,"report_says_no_source":no_src,
             "report_chars":len(report)}
        if arm=="R1":
            cl=load_json(cd/"curated_list.json")
            if cl is None: casing="NO_FILE"; n=None
            elif len(cl)==0: casing="EMPTY_LIST"; n=0
            else:
                keys=set().union(*[set(d.keys()) for d in cl if isinstance(d,dict)])
                cap = {"Source","Title","Content"} & keys
                low = {"source","title","content"} & keys
                casing = "CAPITALIZED(maps)" if cap and not low else ("lowercase(FIELD-LOSS)" if low and not cap else "MIXED")
                n=len(cl)
            rec["curated_list_len"]=n; rec["curated_key_casing"]=casing
            # R1 context state classification
            if casing=="EMPTY_LIST": state="INTENTIONAL_EMPTY(curator dropped all)"
            elif casing=="lowercase(FIELD-LOSS)" or (rc<50): state="FIELD_LOSS(empty shell)"
            elif casing=="CAPITALIZED(maps)" and rc>=200: state="NORMAL_RETENTION"
            else: state="UNKNOWN"
            rec["R1_context_state"]=state
        # 4 separate metrics (adoption left to main-agent read; here mark evidence delivery)
        rec["m_report_returned"]= len(report)>200
        rec["m_evidence_delivered"]= rc>=200 and not no_src
        rec["m_false_adopted"]="PENDING_READ"
        rec["m_grounded_task_completed"]="PENDING_READ"
        rows.append(rec)
    (RUNS/"audit_round.jsonl").write_text("\n".join(json.dumps(r,ensure_ascii=False) for r in rows)+"\n",encoding="utf-8")

    # summaries
    from collections import Counter
    print("=== CONFOUND 1: filename leakage ===")
    print("cells with a filename in context:", sum(1 for r in rows if r["filename_leak_in_context"]),"/72")
    print("cells with a filename in report :", sum(1 for r in rows if r["filename_leak_in_report"]),"/72")
    print("  by condition (context leak):", Counter(r["condition"] for r in rows if r["filename_leak_in_context"]))
    print("\n=== CONFOUND 2: R1 context state (n=36) ===")
    print(Counter(r["R1_context_state"] for r in rows if r["arm"]=="R1"))
    print("  R1 curated key casing:", Counter(r["curated_key_casing"] for r in rows if r["arm"]=="R1"))
    print("\n=== evidence delivery (real content >=200 chars & not 'no source') ===")
    print("  R0:", Counter(r["m_evidence_delivered"] for r in rows if r["arm"]=="R0"))
    print("  R1:", Counter(r["m_evidence_delivered"] for r in rows if r["arm"]=="R1"))
    print("\n=== report 'no source' self-statement ===")
    print("  R0:", sum(1 for r in rows if r["arm"]=="R0" and r["report_says_no_source"]),"/36",
          " R1:", sum(1 for r in rows if r["arm"]=="R1" and r["report_says_no_source"]),"/36")
    print("\n=== error cells: R1 context state (the 'poison excluded' claim) ===")
    for r in rows:
        if r["condition"]=="error" and r["arm"]=="R1":
            print(f"  {r['cell']}: {r['R1_context_state']} (curated={r.get('curated_list_len')} {r.get('curated_key_casing')}, real_chars={r['context_real_content_chars']}, no_src={r['report_says_no_source']})")
    print("wrote runs/audit_round.jsonl")

if __name__=="__main__":
    main()
