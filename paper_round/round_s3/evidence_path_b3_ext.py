#!/usr/bin/env python3
"""round_S3 step 1b ($0): structural variants for the same B3 evidence path. Reuses evidence_path_b3 helpers.
Variants (each with/without the note; ranks of E1 and E2 under the 30 host sub-queries):
  chunk1000 (host)   : RecursiveCharacterTextSplitter(1000,100) over the whole text
  chunk500           : (500,50)
  section1000        : split at detected headings first, then (1000,100) inside each section (section-aware chunking)
  section500         : headings first, then (500,50)
Selections: cosine top-10, cosine top-20, BM25 top-10, hybrid RRF top-10, UNION(cos top-10, bm25 top-10).
Evidence positions are for evaluation only."""
from __future__ import annotations
import os, re, json, pathlib, numpy as np
os.environ.setdefault("TOKENIZERS_PARALLELISM", "false")
ROOT = pathlib.Path(__file__).resolve().parent
import sys; sys.path.insert(0, str(ROOT))
from evidence_path_b3 import sections, heading_at, BM25, rrf, ranks_from_scores, DECISIVE, SB, TASK
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document

def chunk_text(text, size, overlap, by_section, heads):
    sp = RecursiveCharacterTextSplitter(chunk_size=size, chunk_overlap=overlap)
    if not by_section:
        return [(c.page_content, heading_at(heads, text.find(c.page_content[:60]))) for c in sp.split_documents([Document(page_content=text)])]
    out = []; bounds = [off for off, _ in heads] + [len(text)]
    if not heads or heads[0][0] > 0: bounds = [0] + bounds
    for a, b in zip(bounds, bounds[1:]):
        seg = text[a:b]; h = heading_at(heads, a)
        for c in sp.split_documents([Document(page_content=seg)]): out.append((c.page_content, h))
    return out

def main():
    paper = (SB / "papers" / "1610.03807_fulltext.txt").read_text(encoding="utf-8")
    note = (SB / "tasks" / TASK / "Lprime.txt").read_text(encoding="utf-8")
    heads = sections(paper)
    subq = json.loads((ROOT / "evidence_path_b3.json").read_text(encoding="utf-8"))["sub_queries"]
    emb = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    def embed(ts):
        E = np.array(emb.embed_documents(ts)); return E / np.linalg.norm(E, axis=1, keepdims=True)
    Q = np.array([emb.embed_query(q) for q in subq]); Q = Q / np.linalg.norm(Q, axis=1, keepdims=True)
    variants = {"chunk1000": (1000, 100, False), "chunk500": (500, 50, False), "section1000": (1000, 100, True), "section500": (500, 50, True)}
    results = {}
    for vname, (size, ov, by_sec) in variants.items():
        pch = chunk_text(paper, size, ov, by_sec, heads)
        nch = [(c.page_content, "(note)") for c in RecursiveCharacterTextSplitter(chunk_size=size, chunk_overlap=ov).split_documents([Document(page_content=note)])]
        for with_note in (True, False):
            ch = pch + (nch if with_note else []); texts = [t for t, _ in ch]; srcs = ["doc1"] * len(pch) + (["note"] * len(nch) if with_note else [])
            dec = {k: [i for i, t in enumerate(texts) if v in t] for k, v in DECISIVE.items()}
            E = embed(texts); bm = BM25(texts); cnt = {k: {m: 0 for m in ("cos10", "cos20", "bm10", "hyb10", "union10", "gate042")} for k in DECISIVE}
            cos_ranks = {k: [] for k in DECISIVE}
            for qi, q in enumerate(subq):
                cos = E @ Q[qi]; bms = bm.score(q); r_cos = ranks_from_scores(cos); r_bm = ranks_from_scores(bms)
                hyb = rrf([r_cos, r_bm]); r_hyb = {i: r + 1 for r, (i, _) in enumerate(sorted(hyb.items(), key=lambda x: -x[1]))}
                gate = [i for i in range(len(texts)) if cos[i] > 0.42][:10]
                for k, idxs in dec.items():
                    hit = lambda cond: any(cond(i) for i in idxs)
                    cnt[k]["cos10"] += hit(lambda i: r_cos[i] <= 10); cnt[k]["cos20"] += hit(lambda i: r_cos[i] <= 20)
                    cnt[k]["bm10"] += hit(lambda i: r_bm[i] <= 10); cnt[k]["hyb10"] += hit(lambda i: r_hyb[i] <= 10)
                    cnt[k]["union10"] += hit(lambda i: r_cos[i] <= 10 or r_bm[i] <= 10); cnt[k]["gate042"] += hit(lambda i: i in gate)
                    cos_ranks[k].append(min(r_cos[i] for i in idxs) if idxs else None)
            key = f"{vname}|{'note' if with_note else 'nonote'}"
            results[key] = {"n_chunks": len(texts), "decisive_idx": dec, "decisive_headings": {k: [ch[i][1] for i in v] for k, v in dec.items()},
                            "decisive_len": {k: [len(texts[i]) for i in v] for k, v in dec.items()}, "hits_of_%d" % len(subq): cnt,
                            "E2_cos_rank_min_max": (min(cos_ranks["E2_domain_163"]), max(cos_ranks["E2_domain_163"]))}
            print(f"{key:22s} chunks={len(texts):3d} E2@{results[key]['decisive_headings']['E2_domain_163']} len={results[key]['decisive_len']['E2_domain_163']} "
                  f"E2 cos-rank {results[key]['E2_cos_rank_min_max']} | E2 hits/30: {cnt['E2_domain_163']} | E1 hits/30: {cnt['E1_freebase_106']}")
    (ROOT / "evidence_path_b3_ext.json").write_text(json.dumps(results, ensure_ascii=False, indent=1), encoding="utf-8")

if __name__ == "__main__":
    main()
