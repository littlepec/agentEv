#!/usr/bin/env python3
"""round_MD2: separate "retrieval never surfaces the primary" from "drafting ignores the primary" (PREREG_multidoc2.md).

Materials/host/model/questions identical to round_MD (run_multidoc.py): 11 PTB LM papers + 11 third-party notes =
22 local documents; C = all notes faithful, P = 1708.02182 note rewritten 57.3 -> 53.3.

Arms (all built ON TOP of the round_S3 struct retrieval, imported verbatim from paper_round/round_s3/run_round_s3.py):
  struct : reference only (identical to round_MD's struct arm) -- allowed on the CLI, not part of this round's cells
  quota  : struct's per-sub-query union, then for EACH of the 11 paper documents its own top-2 chunks by cosine to the
           sub-query (k=2 fixed in advance); chunks already selected in this sub-query or emitted in an earlier one are
           skipped (same cross-sub-query dedup set _SEEN struct uses), so a paper may contribute fewer than 2 new chunks.
  oracle : DIAGNOSTIC, not a defense. struct's union, then every section_chunks chunk of 1708.02182.txt that contains
           "57.3" is appended (deduplicated; the _SEEN mechanism makes them appear in the first sub-query's context
           only). No role text, no prompt change, no note change; the appendix is the paper's own text under its own
           source name.
COMPRESSION_THRESHOLD stays 8000; with 22 documents (> 10) and > 400k chars the host fast path can never apply.

Ledger: exp_key evidence-package-pilot-multidoc2 (prefix evidence-package-pilot), per-cell reservation $0.05,
round cap = line total at round start + --cap, line cap $10.

Usage:
  python run_multidoc2.py --dry                                            # zero model calls, builds docpaths + index
  python run_multidoc2.py --questions Q1,Q2 --conds P --arms oracle --rep 2 --cap 0.50 --phase confirmatory
--rep N means N repetitions per cell (cell suffix _r2, _r3, ... for repetitions after the first).
"""
from __future__ import annotations
import os, sys, re, json, time, shutil, asyncio, pathlib, argparse, sqlite3, hashlib

ROOT = pathlib.Path(__file__).resolve().parent            # .../paper_round/multi_doc
PR = ROOT.parent                                          # .../paper_round
POOL = ROOT / "pool"
MAT = ROOT / "materials"
RUNS = ROOT / "runs_md2"
DOCP = ROOT / "docpaths_md2"
S3DIR = PR / "round_s3"
sys.path.insert(0, "F:/defense/evidence_pack_prep_v1")    # ledger_guard
sys.path.insert(0, str(PR))                               # contract, offline_retriever
sys.path.insert(0, str(S3DIR))                            # run_round_s3 (struct retrieval, verbatim)
sys.path.insert(0, str(ROOT))                             # run_multidoc (pure helpers only)
import run_round_s3 as S3M                                # section_chunks, struct_get_context, BM25, _SEEN, _STRUCT_STATE
import run_multidoc as MD                                 # pure helpers: paper_ids, note_path, questions, exposure, tokwin

IN_RATE, OUT_RATE = 0.30 / 1_000_000, 1.20 / 1_000_000
EXP_KEY, PREFIX, ROUND_CAP, LINE_CAP, RES = "evidence-package-pilot-multidoc2", "evidence-package-pilot", 0.50, 10.0, 0.05
HOST = ("gpt-researcher v3.6.1 (6f998577) fixed-contract, stage A config, retrieval path "
        "(COMPRESSION_THRESHOLD=8000, 22 documents) + MD2 retrieval variant")
MODEL = "deepseek-v4-flash"
ARMS = ("quota", "oracle", "struct")
K_QUOTA = 4   # set by the main session before freezing: dry-run ranks of the 57.3 chunks are 3-4 among the paper own chunks (see PREREG_multidoc2.md)

POISON_ID, TRUE_VAL, FLIP_VAL = MD.POISON_ID, MD.TRUE_VAL, MD.FLIP_VAL
DECISIVE, PTB_NUM = MD.DECISIVE, MD.PTB_NUM
PRIMARY_FILE = f"{POISON_ID}.txt"

# ---- environment (identical to run_multidoc.setup_env, own runs/docpaths dirs) ----------------------------
def setup_env():
    os.environ["OPENAI_API_KEY"] = MD.key(); os.environ["OPENAI_BASE_URL"] = "https://api.deepseek.com"
    os.environ["FAST_LLM"] = os.environ["SMART_LLM"] = os.environ["STRATEGIC_LLM"] = "openai:deepseek-v4-flash"
    os.environ["EMBEDDING"] = "huggingface:sentence-transformers/all-MiniLM-L6-v2"
    os.environ["REPORT_SOURCE"] = "local"; os.environ["RETRIEVER"] = "offline_null"; os.environ["TEMPERATURE"] = "0.4"
    os.environ["COMPRESSION_THRESHOLD"] = "8000"
    os.environ.setdefault("TOKENIZERS_PARALLELISM", "false")
    RUNS.mkdir(exist_ok=True); DOCP.mkdir(exist_ok=True)

# ---- docpaths / cell ids (own dirs; never touches runs_md/ or docpaths_md/) -------------------------------
def cell_name(qid, arm, cond, rep): return f"{qid}_{arm}_{cond}" + (f"_r{rep}" if rep > 1 else "")

def cell_id(cell):
    mp = RUNS / "cell_map.json"
    m = json.loads(mp.read_text(encoding="utf-8")) if mp.exists() else {}
    if cell not in m:
        m[cell] = f"cell_{len(m)+1:02d}"; mp.write_text(json.dumps(m, indent=2), encoding="utf-8")
    return m[cell]

def build_docpath(cell, cond, ids, allow_placeholder):
    """22 files: <arxiv_id>.txt (paper) and <arxiv_id>_note.txt (third-party note). Neutral names, no labels."""
    out = DOCP / cell_id(cell)
    if out.exists(): shutil.rmtree(out)
    out.mkdir(parents=True)
    notes, ph = {}, []
    for pid in ids:
        shutil.copy(POOL / f"{pid}.txt", out / f"{pid}.txt")
        np_ = MD.note_path(pid, cond)
        if np_.exists():
            shutil.copy(np_, out / f"{pid}_note.txt"); notes[pid] = str(np_)
        elif allow_placeholder:
            (out / f"{pid}_note.txt").write_text(MD.PLACEHOLDER_NOTE.format(pid=pid), encoding="utf-8")
            notes[pid] = "PLACEHOLDER"; ph.append(pid)
        else:
            raise SystemExit(f"STOP (materials): note missing: {np_}")
    return out, notes, ph

# ---- retrieval variants: struct + per-document quota / oracle appendix -------------------------------------
_PAPERS = {"v": None}
def paper_files(ids):
    if _PAPERS["v"] is None: _PAPERS["v"] = [f"{p}.txt" for p in ids]
    return _PAPERS["v"]

_QUOTA_STATE = {"sub_queries": []}
_ORACLE_STATE = {"chunks": None, "appended": [], "source": None, "sub_queries": 0}

def _blocks(src, chunk): return f"Source: {src}\nTitle: \nContent: {chunk}\n"

def _join(base, extra):
    parts = ([base] if base else []) + extra
    return "\n".join(parts)

async def quota_get_context(self, query, max_results=5, cost_callback=None):
    """struct's union, then each paper document's own cosine top-2 chunks (dedup against _SEEN)."""
    import numpy as np
    base = await S3M.struct_get_context(self, query, max_results=max_results, cost_callback=cost_callback)
    ch, E, _bm = S3M._STRUCT_STATE["chunks"]
    qv = np.array(self.embeddings.embed_query(query)); qv /= np.linalg.norm(qv)
    cos = E @ qv
    papers = set(paper_files(MD.paper_ids()))
    by_src = {}
    for i, (src, _c) in enumerate(ch):
        if src in papers: by_src.setdefault(src, []).append(i)
    extra, rec = [], {"query_chars": len(query), "k": K_QUOTA, "per_source": {}, "n_added": 0,
                      "n_added_primary": 0, "n_added_primary_with_true_value": 0}
    for src in sorted(by_src):
        idxs = sorted(by_src[src], key=lambda i: -cos[i])[:K_QUOTA]      # top-2 first, then dedup (PREREG wording)
        added = 0
        for i in idxs:
            k = (ch[i][0], ch[i][1].strip())
            if k in S3M._SEEN: continue
            S3M._SEEN.add(k); extra.append(_blocks(ch[i][0], ch[i][1])); added += 1
            if src == PRIMARY_FILE and TRUE_VAL in ch[i][1]: rec["n_added_primary_with_true_value"] += 1
        rec["per_source"][src] = {"topk_cos": [round(float(cos[i]), 4) for i in idxs], "added": added}
        rec["n_added"] += added
        if src == PRIMARY_FILE: rec["n_added_primary"] = added
    rec["n_sources_with_chunks"] = len(by_src)
    _QUOTA_STATE["sub_queries"].append(rec)
    return _join(base, extra)

async def oracle_get_context(self, query, max_results=5, cost_callback=None):
    """struct's union, then every 1708.02182.txt section chunk containing "57.3" (once per cell, via _SEEN)."""
    base = await S3M.struct_get_context(self, query, max_results=max_results, cost_callback=cost_callback)
    _ORACLE_STATE["sub_queries"] += 1
    if _ORACLE_STATE["chunks"] is None:
        src, text = None, None
        for d in self.documents:
            u = str(d.get("url") or d.get("source") or "")
            if os.path.basename(u) == PRIMARY_FILE: src, text = u, (d.get("raw_content", "") or "")
        if text is None:
            raise RuntimeError(f"STOP (materials): {PRIMARY_FILE} not among the loaded documents")
        seen, chunks = set(), []
        for c in S3M.section_chunks(text):
            if TRUE_VAL in c and c.strip() not in seen: seen.add(c.strip()); chunks.append(c)
        if not chunks:
            raise RuntimeError(f"STOP (materials): no section_chunks chunk of {PRIMARY_FILE} contains {TRUE_VAL}")
        _ORACLE_STATE["chunks"], _ORACLE_STATE["source"] = chunks, src
    src = _ORACLE_STATE["source"]
    extra = []
    for c in _ORACLE_STATE["chunks"]:
        k = (src, c.strip())
        if k in S3M._SEEN: continue
        S3M._SEEN.add(k); extra.append(_blocks(src, c))
        _ORACLE_STATE["appended"].append({"sha256_12": hashlib.sha256(c.encode("utf-8")).hexdigest()[:12],
                                          "chars": len(c), "has_true_value": TRUE_VAL in c,
                                          "sub_query_index": _ORACLE_STATE["sub_queries"]})
    return _join(base, extra)

_ORIG2 = {}
def apply_variant2(variant):
    """Patch ContextCompressor.async_get_context; reset struct + variant state. Mirrors S3M.apply_variant."""
    import gpt_researcher.context.compression as CM
    if "agc" not in _ORIG2: _ORIG2["agc"] = CM.ContextCompressor.async_get_context
    os.environ["COMPRESSION_THRESHOLD"] = "8000"
    S3M._SEEN.clear(); S3M._STRUCT_STATE["chunks"] = None
    _QUOTA_STATE["sub_queries"] = []
    _ORACLE_STATE.update({"chunks": None, "appended": [], "source": None, "sub_queries": 0})
    fn = {"quota": quota_get_context, "oracle": oracle_get_context, "struct": S3M.struct_get_context}.get(variant)
    CM.ContextCompressor.async_get_context = fn if fn is not None else _ORIG2["agc"]

def variant_extras(arm):
    if arm == "quota":
        subs = _QUOTA_STATE["sub_queries"]
        return {"k": K_QUOTA, "n_sub_queries": len(subs),
                "added_per_sub_query": [s["n_added"] for s in subs],
                "added_primary_per_sub_query": [s["n_added_primary"] for s in subs],
                "added_primary_with_true_value": sum(s["n_added_primary_with_true_value"] for s in subs),
                "total_added": sum(s["n_added"] for s in subs), "per_sub_query": subs}
    if arm == "oracle":
        return {"n_oracle_chunks_available": len(_ORACLE_STATE["chunks"] or []),
                "n_appended": len(_ORACLE_STATE["appended"]), "n_sub_queries": _ORACLE_STATE["sub_queries"],
                "source_name": _ORACLE_STATE["source"], "appended": _ORACLE_STATE["appended"]}
    return {}

# ---- budget --------------------------------------------------------------------------------------------------
def round_cap():
    from ledger_guard import LEDGER
    bpath = RUNS / "ledger_baseline_multidoc2.json"
    if bpath.exists():
        base = json.loads(bpath.read_text(encoding="utf-8"))["line_cost_at_round_start"]
    else:
        c = sqlite3.connect(str(LEDGER), timeout=30)
        base = c.execute("select coalesce(sum(cost),0) from calls where exp_key like 'evidence-package-pilot%' "
                         "and exp_key != ?", (EXP_KEY,)).fetchone()[0]; c.close()
        bpath.write_text(json.dumps({"line_cost_at_round_start": base, "round_cap_usd": ROUND_CAP,
                                     "created": time.strftime("%Y-%m-%dT%H:%M:%S")}, indent=2), encoding="utf-8")
    return round(min(LINE_CAP, base + ROUND_CAP), 4)

def get_cb():
    from langchain_community.callbacks.manager import get_openai_callback; return get_openai_callback

# ---- dry run (no model calls; local embeddings only) -----------------------------------------------------------
def _embeddings():
    from gpt_researcher.config import Config
    from gpt_researcher.memory import Memory
    cfg = Config()
    return Memory(cfg.embedding_provider, cfg.embedding_model,
                  **(getattr(cfg, "embedding_kwargs", {}) or {})).get_embeddings()

class _FakeCompressor:
    """Minimal stand-in exposing exactly what struct_get_context reads (documents, embeddings)."""
    def __init__(self, documents, embeddings): self.documents, self.embeddings = documents, embeddings

async def dry(cells, ids):
    import numpy as np
    from gpt_researcher.document.document import DocumentLoader
    thr = int(os.environ.get("COMPRESSION_THRESHOLD", "8000"))
    L = []
    def out(s):
        print(s, flush=True); L.append(s)
    out(f"# round_MD2 dry run (0 model calls) — {time.strftime('%Y-%m-%dT%H:%M:%S')}")
    out("")
    out(f"COMPRESSION_THRESHOLD={thr}; host fast path needs total_chars < {thr} AND n_docs <= 10; "
        f"arms={ARMS}; k_quota={K_QUOTA}")
    out("")
    out("## 1. docpaths / documents")
    out("")
    out("| cell | dir | docs | chars | fast_path | 57.3 in 1708.02182.txt | notes |")
    out("|---|---|---|---|---|---|---|")
    docs_by_cond = {}
    for (qid, arm, cond, rep) in cells:
        cell = cell_name(qid, arm, cond, rep)
        dp, notes, ph = build_docpath(cell, cond, ids, allow_placeholder=True)
        docs = await DocumentLoader(str(dp)).load()
        total = sum(len(d.get("raw_content", "") or "") for d in docs)
        by_url = {str(d.get("url")): (d.get("raw_content", "") or "") for d in docs}
        fast = (total < thr) and (len(docs) <= 10)
        docs_by_cond.setdefault(cond, docs)
        out(f"| {cell} | {cell_id(cell)} | {len(docs)} | {total} | {'YES' if fast else 'no'} | "
            f"{TRUE_VAL in by_url.get(PRIMARY_FILE, '')} | {('PLACEHOLDER x%d' % len(ph)) if ph else 'materials'} |")
    out("")
    out(f"Fast path NOT applicable in any cell: {len(docs_by_cond.get('P', []))} documents (> 10) and "
        f"{sum(len(d.get('raw_content','') or '') for d in docs_by_cond.get('P', []))} chars (> 400000). "
        f"Retrieval is unavoidable by construction.")
    out("")

    # ---- section_chunks per document (both conditions; papers are identical, only the poisoned note differs) ----
    out("## 2. section_chunks per document")
    out("")
    counts = {}
    for cond, docs in sorted(docs_by_cond.items()):
        counts[cond] = {str(d.get("url")): len(S3M.section_chunks(d.get("raw_content", "") or "")) for d in docs}
    ref = "P" if "P" in counts else sorted(counts)[0]
    out(f"| document | chunks ({ref}) | " + " | ".join(f"chunks ({c})" for c in sorted(counts) if c != ref) + " |")
    out("|---|---|" + "---|" * (len(counts) - 1))
    for u in sorted(counts[ref]):
        row = [str(counts[ref][u])] + [str(counts[c].get(u)) for c in sorted(counts) if c != ref]
        out(f"| {u} | " + " | ".join(row) + " |")
    tot = {c: sum(v.values()) for c, v in counts.items()}
    papers_tot = {c: sum(n for u, n in v.items() if not u.endswith("_note.txt")) for c, v in counts.items()}
    out(f"| **total** | " + " | ".join(str(tot[c]) for c in [ref] + [x for x in sorted(counts) if x != ref]) + " |")
    out("")
    out(f"totals: {tot}; paper chunks only: {papers_tot}; "
        f"notes: { {c: tot[c] - papers_tot[c] for c in tot} }")
    out("")

    # ---- struct chunk index (local embeddings), built once on the P docpath ----
    docs = docs_by_cond.get(ref)
    fake = _FakeCompressor(docs, _embeddings())
    qs = MD.questions()
    qids = [q for q in ("Q1", "Q2") if q in qs] or sorted(qs)
    t0 = time.time()
    first = await S3M.struct_get_context(fake, MD.qtext(qids[0]))   # builds _STRUCT_STATE exactly as at runtime
    S3M._SEEN.clear()
    ch, E, bm = S3M._STRUCT_STATE["chunks"]
    out(f"struct chunk index built on condition {ref}: {len(ch)} chunks, embedding dim {E.shape[1]}, "
        f"{round(time.time()-t0,1)}s (local HF all-MiniLM-L6-v2, $0).")
    out("")

    pidx = [i for i, (s, _c) in enumerate(ch) if s == PRIMARY_FILE]
    hit = [i for i in pidx if TRUE_VAL in ch[i][1]]
    if not hit:
        out(f"STOP CONDITION: no section_chunks chunk of {PRIMARY_FILE} contains {TRUE_VAL}.")
        (RUNS / "dry_run_md2.md").write_text("\n".join(L) + "\n", encoding="utf-8")
        raise SystemExit("STOP: 57.3 chunks not found by section_chunks")

    # ---- (b) quota-exposure ESTIMATE: rank of the 57.3 chunks among the paper's own chunks, raw question query ----
    out("## 3. quota exposure ESTIMATE for 1708.02182.txt (query = raw question text)")
    out("")
    out("ESTIMATE ONLY: at run time the host queries with sub-queries the model generates from the question, not with "
        "the raw question text; these ranks are a proxy for whether quota k=2 would surface a 57.3 chunk.")
    out("")
    out(f"| question | 57.3 chunk (idx) | cos | rank among the {len(pidx)} chunks of {PRIMARY_FILE} | in top-{K_QUOTA}? | "
        f"global cos rank / {len(ch)} | in struct global top-10? |")
    out("|---|---|---|---|---|---|---|")
    est = {}
    for qid in qids:
        qv = np.array(fake.embeddings.embed_query(MD.qtext(qid))); qv /= np.linalg.norm(qv)
        cos = E @ qv
        order = sorted(pidx, key=lambda i: -cos[i])
        gorder = sorted(range(len(ch)), key=lambda i: -cos[i])
        grank = {i: r + 1 for r, i in enumerate(gorder)}
        top2 = order[:K_QUOTA]
        est[qid] = {"in_top2": False, "rows": []}
        for i in hit:
            r = order.index(i) + 1
            intop = i in top2
            est[qid]["in_top2"] = est[qid]["in_top2"] or intop
            est[qid]["rows"].append((i, float(cos[i]), r, intop, grank[i]))
            out(f"| {qid} | {i} | {cos[i]:.4f} | {r} | {'YES' if intop else 'no'} | {grank[i]} | "
                f"{'YES' if grank[i] <= 10 else 'no'} |")
        t2 = ", ".join(f"idx {i} (cos {cos[i]:.4f}, 57.3={'yes' if TRUE_VAL in ch[i][1] else 'no'})" for i in top2)
        out(f"| {qid} | *quota top-{K_QUOTA} of this paper* | | | | | {t2} |")
    out("")

    # ---- (c) oracle appendix content ----
    out("## 4. oracle appendix (chunks of 1708.02182.txt containing 57.3)")
    out("")
    out(f"{len(hit)} chunk(s) would be appended per cell (once, in the first sub-query's context).")
    out("")
    for i in hit:
        c = ch[i][1]
        out(f"- idx {i}, {len(c)} chars, sha256 {hashlib.sha256(c.encode('utf-8')).hexdigest()[:12]}: "
            f"`{c[:120].replace(chr(10), ' ')}`")
    out("")
    out(f"(struct's own union for the raw question of {qids[0]} returned "
        f"{first.count('Source: ')} blocks, {len(first)} chars — reference only.)")
    out("")
    out("DRY DONE (0 model calls)")
    (RUNS / "dry_run_md2.md").write_text("\n".join(L) + "\n", encoding="utf-8")
    print(f"\nwritten: {RUNS / 'dry_run_md2.md'}", flush=True)

# ---- one cell ---------------------------------------------------------------------------------------------------
async def run_cell(qid, arm, cond, rep, ids, phase, guard, gcb, PL, pvar):
    import contract as C, offline_retriever
    cell = cell_name(qid, arm, cond, rep); cdir = RUNS / cell; cdir.mkdir(exist_ok=True)
    if (cdir / "meta.json").exists() and json.loads((cdir / "meta.json").read_text(encoding="utf-8")).get("done"):
        print(f"{cell}: skip (done)", flush=True); return "skip"
    ok, why = guard.preflight(RES, int(RES / OUT_RATE))
    if not ok: print(f"{cell}: {why}", flush=True); return "stop"
    dp, notes, ph = build_docpath(cell, cond, ids, allow_placeholder=False)
    os.environ["DOC_PATH"] = str(dp); os.environ["CURATE_SOURCES"] = "false"
    C._CUR_SINK["path"] = None; C._CUR_SINK["state"] = None
    apply_variant2(arm)                          # quota | oracle | struct ; COMPRESSION_THRESHOLD -> 8000
    offline_retriever.install_offline_retriever()
    from gpt_researcher import GPTResearcher
    plog = PL() if PL else None
    if plog is not None and pvar is not None: pvar.set(plog)
    t0 = time.time(); pt = ct = 0; report = ""; ctx = None; err = None
    try:
        r = GPTResearcher(query=MD.qtext(qid), report_type="research_report", report_source="local")
        with gcb() as cb:
            await r.conduct_research(); report = await r.write_report()
        pt, ct = cb.prompt_tokens, cb.completion_tokens; ctx = r.context
        ctxs, is_list = MD.ctx_to_str(ctx)
        (cdir / "report.md").write_text(report or "", encoding="utf-8")
        (cdir / "context.txt").write_text(ctxs, encoding="utf-8")
        if plog is not None: C.save_provider_logs(plog.calls, cdir / "provider_log.json", cdir / "provider_log_preview.json")
    except Exception as e:
        err = f"{type(e).__name__}: {e}"; print(f"{cell}: ERR {err}", flush=True)
    extras = variant_extras(arm)
    apply_variant2("default")
    cost = pt * IN_RATE + ct * OUT_RATE
    guard.record(cost, pt, ct, data={"stage": "multidoc2", "question": qid, "arm": arm, "cond": cond, "rep": rep,
                                     "phase": phase, "cell": cell}, est_cost=RES, est_out=int(RES / OUT_RATE))
    ctxs, is_list = MD.ctx_to_str(ctx)
    exp = MD.exposure(ctxs, ids)
    meta = {"cell": cell, "docpath_dir": cell_id(cell), "question_id": qid, "question": MD.qtext(qid),
            "question_placeholder": MD.q_is_placeholder(qid), "condition": cond, "arm": arm, "rep": rep, "phase": phase,
            "prompt_tokens": pt, "completion_tokens": ct, "deepseek_cost_usd": round(cost, 6),
            "report_chars": len(report or ""), "context_chars": len(ctxs), "context_was_list": is_list,
            "n_documents": 2 * len(ids), "poisoned_paper": POISON_ID, "true_value": TRUE_VAL, "flipped_value": FLIP_VAL,
            "decisive_strings": DECISIVE, "note_files": notes, "placeholder_notes": ph,
            "n_llm_calls": sum(1 for c2 in (plog.calls if plog else []) if c2.get("phase") == "start"),
            "elapsed_s": round(time.time() - t0, 1), "error": err, "done": err is None,
            "host": HOST, "model": MODEL, "variant_extras": extras,
            "materials_manifest": [str(POOL / "pool_manifest.json"), str(MAT / "manifest.json"), str(ROOT / "questions.json")]}
    meta.update(exp)
    (cdir / "meta.json").write_text(json.dumps(meta, ensure_ascii=False, indent=2), encoding="utf-8")
    with (RUNS / "multidoc2_results.jsonl").open("a", encoding="utf-8") as f:
        f.write(json.dumps(meta, ensure_ascii=False) + "\n")
    xs = (f"quota_added={extras.get('total_added')}/prim={extras.get('added_primary_per_sub_query')}" if arm == "quota"
          else (f"oracle_appended={extras.get('n_appended')}" if arm == "oracle" else ""))
    print(f"{cell}: {'ok' if not err else 'error'} calls={meta['n_llm_calls']} ${cost:.4f} rep_chars={len(report or '')} "
          f"ctx={len(ctxs)} blocks={exp['n_blocks']} primary_blocks={exp['source_block_counts'].get(PRIMARY_FILE)} "
          f"note_blocks={exp['source_block_counts'].get(POISON_ID + '_note.txt')} "
          f"primary={exp['primary_exposure']['true_value_verbatim']} note_flip={exp['note_exposure']['flipped_value_present']} "
          f"{xs}", flush=True)
    return "ok" if not err else "error"

async def main(args):
    from ledger_guard import BudgetGuard
    import contract as C
    ids = MD.paper_ids()
    qs = [x for x in args.questions.split(",") if x]; arms = [x for x in args.arms.split(",") if x]
    conds = [x for x in args.conds.split(",") if x]
    bad = [a for a in arms if a not in ARMS]
    if bad: raise SystemExit(f"STOP: unknown arm(s) {bad}")
    cells = [(q, a, c, rep) for rep in range(1, max(1, args.rep) + 1) for q in qs for a in arms for c in conds]
    if args.dry: await dry(cells, ids); return
    C.install_curation_field_fix(); PL, pvar = C.make_provider_logger(); gcb = get_cb()
    guard = BudgetGuard(EXP_KEY, exp_prefix=PREFIX, call_cap=10**6, in_tok_cap=80_000_000, out_tok_cap=30_000_000)
    guard.cost_cap = round_cap()
    cur, calls, *_ = guard._totals()
    print(f"COST ACCOUNTING: pilot* cum=${cur:.4f} ({calls} calls); round cap=${guard.cost_cap}; "
          f"cells={len(cells)}; reservation=${RES}/cell; phase={args.phase}", flush=True)
    for (q, a, c, rep) in cells:
        st = await run_cell(q, a, c, rep, ids, args.phase, guard, gcb, PL, pvar)
        if st == "stop": print("STOP (budget)", flush=True); break
    cur, calls, *_ = guard._totals()
    print(f"MULTIDOC2 BATCH DONE: pilot* cum=${cur:.4f} ({calls} calls)", flush=True)

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--questions", default="Q1,Q2"); ap.add_argument("--conds", default="C,P")
    ap.add_argument("--arms", default="quota,oracle"); ap.add_argument("--rep", type=int, default=1)
    ap.add_argument("--cap", type=float, default=0.0); ap.add_argument("--phase", default="confirmatory")
    ap.add_argument("--exp-key", default=""); ap.add_argument("--dry", action="store_true")
    a = ap.parse_args()
    if a.exp_key: EXP_KEY = a.exp_key
    if a.cap: ROUND_CAP = a.cap
    setup_env(); asyncio.run(main(a))
