#!/usr/bin/env python3
"""round_S4 pre-freeze feasibility probe ($0, local embeddings only). Evidence positions are used for EVALUATION only.
Question: under the struct retriever (section-aware chunking + cosine top-10 UNION BM25 top-10, same code as round_S3 /
run_round_s4.py), can a *targeted* follow-up query of the kind a source-constraint checker would plausibly write (no gold
numbers, no gold passage text) retrieve the decisive paper passage that the initial sub-queries missed?
Tasks B3 (decisive: 4.3 '163 templates' passage; solved by struct in S3) and B6 (decisive: German '88 PD / 88 HC' sentence;
NOT retrieved by struct in S3). Documents = E_fulltext + L' (P condition) and E_fulltext + L (C condition).
Writes offline_probe_s4.json. Probe queries were written by the main session before freezing; they are NOT runtime inputs."""
from __future__ import annotations
import json, pathlib, sys
import numpy as np
ROOT = pathlib.Path(__file__).resolve().parent; SB = ROOT.parent / "stage_b"
sys.path.insert(0, str(ROOT))
from run_round_s4 import section_chunks, BM25   # same chunking / lexical scorer as the runtime
from langchain_huggingface import HuggingFaceEmbeddings

DECISIVE = {"B3": "hand-craft 163", "B6": "88 PD patients and 88 HC"}
PROBES = {
    "B3": ["number of hand-crafted templates for the domain-specific knowledge base",
           "templates hand-crafted for the in-house KB predicates",
           "how many templates were written for the domain-specific KB evaluation",
           "hand-crafted templates power tool knowledge base"],
    "B6": ["German speech recordings PD patients HC speakers",
           "German data participants Parkinson patients healthy controls",
           "number of German speakers in the dataset",
           "German corpus size PD and HC",
           "speech recordings from Germany",
           "datasets used"],
}
def main():
    emb = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2"); out = {}
    for t in ("B3", "B6"):
        out[t] = {}
        for cond, note in (("P", "Lprime.txt"), ("C", "L.txt")):
            docs = [("document_1.txt", (SB / "tasks" / t / "E_fulltext.txt").read_text(encoding="utf-8")),
                    ("document_2.txt", (SB / "tasks" / t / note).read_text(encoding="utf-8"))]
            ch = [(src, c) for src, txt in docs for c in section_chunks(txt)]
            E = np.array(emb.embed_documents([c for _, c in ch])); E = E / np.linalg.norm(E, axis=1, keepdims=True); bm = BM25([c for _, c in ch])
            dec = [i for i, (s, c) in enumerate(ch) if s == "document_1.txt" and DECISIVE[t].lower() in c.lower()]
            rows = []
            for q in PROBES[t]:
                qv = np.array(emb.embed_query(q)); qv /= np.linalg.norm(qv); cos = E @ qv; bms = bm.score(q)
                rc = sorted(range(len(ch)), key=lambda i: -cos[i]); rb = sorted(range(len(ch)), key=lambda i: -bms[i])
                r_cos = min(rc.index(i) + 1 for i in dec) if dec else None; r_bm = min(rb.index(i) + 1 for i in dec) if dec else None
                union = set(rc[:10]) | set(rb[:10])
                rows.append({"query": q, "cos_rank": r_cos, "bm25_rank": r_bm, "in_union10": any(i in union for i in dec),
                             "union_size": len(union), "union_doc2": sum(1 for i in union if ch[i][0] == "document_2.txt")})
            out[t][cond] = {"n_chunks": len(ch), "decisive_chunk_idx": dec, "decisive_chunk_len": [len(ch[i][1]) for i in dec], "probes": rows}
            print(f"{t}/{cond}: chunks={len(ch)} decisive_idx={dec}")
            for r in rows: print(f"   union10={str(r['in_union10']):5} cos#{r['cos_rank']:<3} bm25#{r['bm25_rank']:<3} | {r['query']}")
    (ROOT / "offline_probe_s4.json").write_text(json.dumps(out, indent=2, ensure_ascii=False), encoding="utf-8")
if __name__ == "__main__":
    main()
