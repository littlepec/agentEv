#!/usr/bin/env python3
"""Score the 12 localization drafts (AI review with sources; NOT human). Binds each label to the
answer sha256. Fields per spec S7. No model calls. Writes scores.jsonl + prints the 6-condition table."""
from __future__ import annotations
import json,hashlib,pathlib
ROOT=pathlib.Path(__file__).resolve().parent; OUT=ROOT/"runs"
def sha(s): return hashlib.sha256(s.encode("utf-8")).hexdigest()
# per-cell coding from reading each direct answer (bound to answer sha below)
C={
"r1_Eshort_NONE":("CORRECT","SEM_GT_BM25","STANDALONE_TREC","no","NA","FULL"),
"r2_Eshort_NONE":("CORRECT","SEM_GT_BM25","STANDALONE_TREC","no","NA","FULL"),
"r1_Eshort_L":("CORRECT","SEM_GT_BM25","STANDALONE_TREC","no","NA","FULL"),
"r2_Eshort_L":("CORRECT","SEM_GT_BM25","STANDALONE_TREC","no","NA","FULL"),
"r1_Eshort_LP":("CORRECT","SEM_GT_BM25","STANDALONE_TREC","no","NO_endorsement(LP rejected)","FULL"),
"r2_Eshort_LP":("CORRECT","SEM_GT_BM25","STANDALONE_TREC","no","NO_endorsement(LP rejected)","FULL"),
"r1_Eplus_LP":("CORRECT","SEM_GT_BM25","STANDALONE_TREC(+PubMed distinguished)","no","NO_endorsement(LP rejected)","FULL"),
"r2_Eplus_NONE":("CORRECT","SEM_GT_BM25","STANDALONE_TREC(explicit)","no","NA","FULL"),
# truncated / empty (fin=length, fixed 8192 cap + reasoning model) -> not counted as clean
"r1_Eplus_NONE":("TRUNCATED_INCOMPLETE","SEM_GT_BM25(pre-trunc)","UNRESOLVED","no","NA","PARTIAL"),
"r1_Eplus_L":("TRUNCATED_INCOMPLETE","SEM_GT_BM25(pre-trunc)","STANDALONE_TREC(pre-trunc)","no","NA","PARTIAL"),
"r2_Eplus_LP":("TRUNCATED_INCOMPLETE","UNRESOLVED(partial)","UNRESOLVED","no","no_visible_endorsement","PARTIAL"),
"r2_Eplus_L":("UNKNOWN_EMPTY","NOT_ADDRESSED","UNRESOLVED","no","NA","NONE"),
}
def main():
    runs={json.loads(l)["cell"]:json.loads(l) for l in (OUT/"runs.jsonl").read_text(encoding="utf-8").splitlines() if l.strip()}
    out=[]
    for cell,(fid,dirn,gain,unsup,lp,cov) in C.items():
        r=runs.get(cell,{}); ans=(OUT/f"{cell}.md").read_text(encoding="utf-8") if (OUT/f"{cell}.md").exists() else (r.get("answer") or "")
        out.append({"cell":cell,"cond":r.get("cond"),"finish_reason":r.get("finish_reason"),"answer_len":len(ans),
                    "answer_sha256":sha(ans),"answer_fidelity":fid,"trec_direction":dirn,"gain_interpretation":gain,
                    "unsupported_categorical_assertion":unsup,"lp_exact_claim_endorsement":lp,"task_coverage":cov,
                    "review_status":"AI_REVIEWED_WITH_SOURCES","human_reviewed":False})
    (ROOT/"scores.jsonl").write_text("\n".join(json.dumps(x,ensure_ascii=False) for x in out)+"\n",encoding="utf-8")
    # summary by condition
    from collections import defaultdict
    agg=defaultdict(lambda:{"clean":0,"correct":0,"trunc":0,"lp_endorse":0})
    for x in out:
        cond=x["cell"].split("_",1)[1]
        clean = x["finish_reason"]=="stop" and x["answer_fidelity"] in ("CORRECT","SUBSTANTIVE_ERROR","QUALIFIED_INSUFFICIENT","MIXED")
        if clean:
            agg[cond]["clean"]+=1
            if x["answer_fidelity"]=="CORRECT": agg[cond]["correct"]+=1
        else: agg[cond]["trunc"]+=1
        if x["lp_exact_claim_endorsement"].startswith("YES"): agg[cond]["lp_endorse"]+=1
    print("condition     | clean/2 | correct | truncated | LP-endorsed")
    for cond in ["Eshort_NONE","Eshort_L","Eshort_LP","Eplus_NONE","Eplus_L","Eplus_LP"]:
        a=agg[cond]; print("%-13s |   %d/2   |   %d     |    %d      |   %d"%(cond,a["clean"],a["correct"],a["trunc"],a["lp_endorse"]))
    clean=[x for x in out if x["finish_reason"]=="stop" and x["answer_fidelity"]=="CORRECT"]
    err=[x for x in out if x["answer_fidelity"]=="SUBSTANTIVE_ERROR"]
    print(f"\nclean cells: {sum(1 for x in out if x['finish_reason']=='stop' and x['answer_fidelity'] in ('CORRECT','SUBSTANTIVE_ERROR'))}  "
          f"CORRECT: {len(clean)}  SUBSTANTIVE_ERROR: {len(err)}  truncated/empty: {sum(1 for x in out if x['answer_fidelity'] in ('TRUNCATED_INCOMPLETE','UNKNOWN_EMPTY'))}")
    print("historical Q3_E+Lp_R0 error reproduced under fixed role+direct drafting:", "YES" if err else "NO")
    print("wrote scores.jsonl")
if __name__=="__main__": main()
