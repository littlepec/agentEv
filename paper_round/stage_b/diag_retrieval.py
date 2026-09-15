#!/usr/bin/env python3
"""$0 diagnostic (local embeddings only, no LLM): replicate the pinned host's context selection for a finished cell.
Host rule (gpt_researcher/context/compression.py + langchain_classic EmbeddingsFilter, k=None):
  chunks = RecursiveCharacterTextSplitter(1000, 100) over documents in loader order
  keep chunks with cosine(query, chunk) > SIMILARITY_THRESHOLD (default 0.35), ORIGINAL ORDER (not sorted)
  context = first max_results (5) kept chunks
Prints, per host sub-query (from provider_log call 2), similarity of every chunk by source and the host's selection,
so we can tell "paper chunks failed the relevance gate" from "paper chunks outranked" or "file order".
Usage: python diag_retrieval.py B3_P_F0 [B3_C_F0 ...]"""
from __future__ import annotations
import os, sys, json, pathlib, asyncio
os.environ.setdefault("TOKENIZERS_PARALLELISM", "false")
ROOT = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))
# Effective host values (verified 2026-09-14): cfg SIMILARITY_THRESHOLD default 0.42 (config/variables/default.py),
# context_manager passes max_results=10; the 0.35 / 5 values in compression.py are only fallbacks.
THRESH = float(os.environ.get("SIMILARITY_THRESHOLD", 0.42)); TOPN = int(os.environ.get("HOST_TOPN", 10))

async def load_docs(dp):
    from gpt_researcher.document.document import DocumentLoader
    return await DocumentLoader(str(dp)).load()

def main(cells):
    from langchain_huggingface import HuggingFaceEmbeddings
    from langchain_text_splitters import RecursiveCharacterTextSplitter
    from langchain_core.documents import Document
    import numpy as np
    emb = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    cell_map = json.loads((ROOT / "runs_b" / "cell_map.json").read_text(encoding="utf-8"))
    out = {}
    for cell in cells:
        meta = json.loads((ROOT / "runs_b" / cell / "meta.json").read_text(encoding="utf-8"))
        dp = ROOT / "docpaths_b" / meta["docpath_dir"]
        pages = asyncio.run(load_docs(dp))
        docs = [Document(page_content=p["raw_content"], metadata={"source": p.get("url", "")}) for p in pages]
        chunks = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100).split_documents(docs)
        srcs = [c.metadata["source"] for c in chunks]
        E = np.array(emb.embed_documents([c.page_content for c in chunks]))
        E = E / np.linalg.norm(E, axis=1, keepdims=True)
        calls = json.load(open(ROOT / "runs_b" / cell / "provider_log.json", encoding="utf-8"))
        ends = [c for c in calls if c.get("phase") == "end"]
        try: subq = json.loads(ends[1]["generations"][0]["text"])
        except Exception: subq = [meta["question"]]
        actual_ctx = (ROOT / "runs_b" / cell / "context.txt").read_text(encoding="utf-8")
        res = {"loader_order": [p.get("url") for p in pages], "n_chunks": {s: srcs.count(s) for s in set(srcs)}, "sub_queries": subq, "per_query": []}
        print(f"=== {cell} loader_order={res['loader_order']} chunks={res['n_chunks']} threshold={THRESH}")
        for q in subq:
            qv = np.array(emb.embed_query(q)); qv = qv / np.linalg.norm(qv)
            sim = E @ qv
            kept = [i for i in range(len(chunks)) if sim[i] > THRESH]
            sel = kept[:TOPN]
            by_src = {}
            for s in set(srcs):
                idx = [i for i in range(len(chunks)) if srcs[i] == s]
                by_src[s] = {"max_sim": round(float(sim[idx].max()), 3), "n_above": int(sum(sim[i] > THRESH for i in idx)),
                             "top3": [round(float(x), 3) for x in sorted(sim[idx], reverse=True)[:3]]}
            r = {"query": q, "by_source": by_src, "host_selection": [(srcs[i], round(float(sim[i]), 3)) for i in sel],
                 "would_select_if_sorted": [(srcs[i], round(float(sim[i]), 3)) for i in sorted(kept, key=lambda i: -sim[i])[:TOPN]]}
            res["per_query"].append(r)
            print(f"  Q: {q}")
            for s, v in by_src.items(): print(f"     {s}: max={v['max_sim']} n_above={v['n_above']} top3={v['top3']}")
            print(f"     host selection (first {TOPN} above threshold, file order): {r['host_selection']}")
            print(f"     if sorted by similarity instead: {r['would_select_if_sorted']}")
        res["actual_context_blocks"] = {s: actual_ctx.count(f"Source: {s}") for s in set(srcs)}
        print(f"  actual context blocks in run: {res['actual_context_blocks']}")
        out[cell] = res
    (ROOT / "runs_b" / "diag_retrieval.json").write_text(json.dumps({**(json.loads((ROOT / "runs_b" / "diag_retrieval.json").read_text(encoding="utf-8")) if (ROOT / "runs_b" / "diag_retrieval.json").exists() else {}), **out}, ensure_ascii=False, indent=2), encoding="utf-8")

if __name__ == "__main__":
    main(sys.argv[1:])
