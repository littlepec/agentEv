#!/usr/bin/env python3
"""Stage B-prep, step 1: scan the QASPER *test* split for candidate tasks by STRUCTURE, recording
every filter stage's denominator (roadmap 4.1: report the whole pool + selection rule).
Read-only public data (HF datasets-server HTTP API). No model calls. No writes outside stage_b/.
Structures (STAGE_B_FIRST_BATCH_PLAN.md §1):
  S1  single fact (one evidence paragraph, specific number/name answer)
  S2  object/condition/version applicability (question/answer scoped to a setting/dataset/version)
  S3  cross-paragraph / cross-section (every annotator's evidence spans >=2 sections)
  NEG simple query negative control (single short scalar answer, one paragraph)
Excluded papers: the four already used in development/calibration (Q2/Q3/Q4/Q7)."""
from __future__ import annotations
import json, re, pathlib, urllib.request, collections, gzip, hashlib, time

ROOT = pathlib.Path(__file__).resolve().parent
RAW = ROOT / "raw"; RAW.mkdir(exist_ok=True)
OUT = ROOT / "candidate_scan"; OUT.mkdir(exist_ok=True)
CACHE = RAW / "qasper_test_rows.json.gz"
USED_PAPERS = {"1608.01972", "2003.12139", "1908.09590", "2003.07459"}   # Q3, Q2, Q4, Q7 (dev/calibration)
BASE = "https://datasets-server.huggingface.co/rows?dataset=allenai/qasper&config=qasper&split=test"

def fetch_rows():
    if CACHE.exists():
        with gzip.open(CACHE, "rt", encoding="utf-8") as f: return json.load(f)
    rows = []
    for off in range(0, 500, 100):
        url = f"{BASE}&offset={off}&length=100"
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 research"})
        for attempt in range(3):
            try:
                body = urllib.request.urlopen(req, timeout=180).read().decode("utf-8"); break
            except Exception as e:
                if attempt == 2: raise
                time.sleep(5)
        j = json.loads(body); got = [r["row"] for r in j.get("rows", [])]
        print(f"offset {off}: {len(got)} rows", flush=True)
        rows.extend(got)
        if len(got) < 100: break
    with gzip.open(CACHE, "wt", encoding="utf-8") as f: json.dump(rows, f, ensure_ascii=False)
    return rows

def para_index(ft):
    """map paragraph text -> section name (first occurrence)."""
    idx = {}
    secs, paras = ft.get("section_name", []), ft.get("paragraphs", [])
    for s, plist in zip(secs, paras):
        for p in plist:
            idx.setdefault(p, s)
    return idx

NUM = re.compile(r"\d")
COND_Q = re.compile(r"\b(which|what)\b.*\b(dataset|datasets|setting|settings|condition|conditions|language|languages|domain|domains|version|configuration|case|cases|task|tasks|scenario)\b|\bunder\b|\bonly\b|\bwhen\b", re.I)

def answers_of(qas, qi):
    """Return list of per-annotator dicts for question index qi (handles HF nesting)."""
    a = qas["answers"][qi]
    if isinstance(a, dict) and "answer" in a: a = a["answer"]
    return a if isinstance(a, list) else [a]

def main():
    rows = fetch_rows()
    n_papers = len(rows); n_q = 0; stage = collections.Counter()
    cands = []
    for r in rows:
        pid = r["id"]; idx = para_index(r["full_text"]); qas = r["qas"]
        for qi, q in enumerate(qas["question"]):
            n_q += 1
            anns = answers_of(qas, qi)
            if not anns: stage["no_annotation"] += 1; continue
            if any(a.get("unanswerable") for a in anns): stage["some_unanswerable"] += 1; continue
            if any(a.get("yes_no") is not None for a in anns): stage["yes_no"] += 1; continue
            stage["answerable_non_yesno"] += 1
            if pid in USED_PAPERS: stage["excluded_used_paper"] += 1; continue
            per = []
            for a in anns:
                ev = [e for e in (a.get("evidence") or []) if isinstance(e, str) and e.strip()]
                ev = [e for e in ev if not e.startswith("FLOAT SELECTED")]      # figure/table refs, not paragraphs
                secs = sorted({idx.get(e, "?") for e in ev})
                ans = "; ".join(a.get("extractive_spans") or []) or (a.get("free_form_answer") or "")
                per.append({"answer": ans.strip(), "n_ev": len(ev), "secs": secs, "ev": ev})
            if any(p["n_ev"] == 0 or not p["answer"] for p in per): stage["missing_evidence_or_answer"] += 1; continue
            if any("?" in p["secs"] for p in per): stage["evidence_not_mapped_to_section"] += 1; continue
            stage["mapped"] += 1
            answers = [p["answer"] for p in per]
            has_num = any(NUM.search(a) for a in answers)
            min_ev = min(p["n_ev"] for p in per); max_ev = max(p["n_ev"] for p in per)
            min_secs = min(len(p["secs"]) for p in per)
            alen = max(len(a.split()) for a in answers)
            tags = []
            if min_secs >= 2 and (has_num or alen >= 3): tags.append("S3")
            if max_ev == 1 and has_num: tags.append("S1")
            if max_ev == 1 and has_num and alen <= 4: tags.append("NEG")
            if COND_Q.search(q) and max_ev <= 2 and (has_num or alen >= 2): tags.append("S2")
            if not tags: stage["no_structure_tag"] += 1; continue
            stage["tagged"] += 1
            cands.append({"paper": pid, "title": r["title"], "q_idx": qi, "question": q, "answers": answers,
                          "n_annotators": len(per), "min_ev": min_ev, "max_ev": max_ev, "min_sections": min_secs,
                          "sections": sorted({s for p in per for s in p["secs"]}), "tags": tags,
                          "evidence": [p["ev"] for p in per]})
    summary = {"papers_in_test": n_papers, "questions_total": n_q, "filter_stages": dict(stage),
               "tag_counts": dict(collections.Counter(t for c in cands for t in c["tags"])),
               "cache_sha256": hashlib.sha256(CACHE.read_bytes()).hexdigest()}
    (OUT / "scan_summary.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")
    (OUT / "candidates_all.json").write_text(json.dumps(cands, ensure_ascii=False, indent=1), encoding="utf-8")
    for tag in ("S3", "S2", "S1", "NEG"):
        sub = [c for c in cands if tag in c["tags"]]
        lines = [f"# {tag} candidates ({len(sub)}) — auto-tagged, NOT yet selected", ""]
        for c in sub:
            lines.append(f"- {c['paper']} | {c['title'][:80]} | q{c['q_idx']}: {c['question']} | A: {' || '.join(a[:120] for a in c['answers'])} | ev {c['min_ev']}-{c['max_ev']} paras, secs={c['min_sections']}+ {c['sections'][:4]}")
        (OUT / f"{tag.lower()}_candidates.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(json.dumps(summary, ensure_ascii=False, indent=2))

if __name__ == "__main__":
    main()
