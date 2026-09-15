#!/usr/bin/env python3
"""round_S3 runtime comparison on frozen materials (stage_b/tasks/B3,B5,B6,B7; sha in stage_b/tasks_manifest_b.json).
Variants (F0, no curation, host/model/config as stage A):
  default  : host default local retrieval (chunk 1000/100, cosine > cfg 0.42, file order, <=10)   -> current retrieval
  struct   : cheapest structural fix chosen from the offline path analysis: section-aware chunking (split at headings,
             then 1000/100) + per-sub-query UNION of cosine top-10 and BM25 top-10, deduplicated across sub-queries;
             no extra LLM call. Implemented as a runtime patch of ContextCompressor.async_get_context (pinned package untouched).
  followup : default retrieval + ONE gap check (LLM lists <=2 missing-information search queries or NONE, Sufficient-Context
             style trigger) + re-retrieval with the SAME default retriever (IRCoT-style truncated to one step). Adapted stand-in,
             not a re-implementation of any published method.
  fullwin  : documents directly in the window (COMPRESSION_THRESHOLD raised)                           -> reference
Evidence positions are NEVER given to any variant. Ledger exp_key evidence-package-pilot-roundS3; round cap $1.00 incl. materials.
Usage: python run_round_s3.py --variant struct --tasks B3,B5,B6,B7 --conds C,P --phase confirmatory   |   --dry"""
from __future__ import annotations
import os, sys, re, json, time, math, asyncio, pathlib, argparse, sqlite3, collections, urllib.request
ROOT = pathlib.Path(__file__).resolve().parent; PR = ROOT.parent; SB = PR / "stage_b"
RUNS = ROOT / "runs_s3"; DOCP = ROOT / "docpaths_s3"; RUNS.mkdir(exist_ok=True); DOCP.mkdir(exist_ok=True)
KEY = pathlib.Path("F:/defense/research_v1/.deepseek_key").read_text(encoding="utf-8").strip()
sys.path.insert(0, "F:/defense/evidence_pack_prep_v1"); sys.path.insert(0, str(PR))
from ledger_guard import BudgetGuard, LEDGER
import contract as C, offline_retriever
os.environ["OPENAI_API_KEY"] = KEY; os.environ["OPENAI_BASE_URL"] = "https://api.deepseek.com"
os.environ["FAST_LLM"] = os.environ["SMART_LLM"] = os.environ["STRATEGIC_LLM"] = "openai:deepseek-v4-flash"
os.environ["EMBEDDING"] = "huggingface:sentence-transformers/all-MiniLM-L6-v2"
os.environ["REPORT_SOURCE"] = "local"; os.environ["RETRIEVER"] = "offline_null"; os.environ["TEMPERATURE"] = "0.4"
os.environ.setdefault("TOKENIZERS_PARALLELISM", "false")
IN_RATE, OUT_RATE = 0.30 / 1_000_000, 1.20 / 1_000_000
EXP_KEY, PREFIX, ROUND_CAP, LINE_CAP = "evidence-package-pilot-roundS3", "evidence-package-pilot", 1.00, 10.0
VARIANT_CAP = {"default": 0.12, "struct": 0.15, "followup": 0.20, "fullwin": 0.30}
RES = {"default": 0.015, "struct": 0.015, "followup": 0.02, "fullwin": 0.03}
COND_ROLES = {"C": {"evidence": "E_fulltext.txt", "interp": "L.txt"}, "P": {"evidence": "E_fulltext.txt", "interp": "Lprime.txt"}}
PAPER_KEY = {"B3": ["hand-craft 163", "163 templates"], "B5": ["97.78 to 87.38", "1.39 to 1.33"], "B6": ["88 PD patients and 88 HC"], "B7": ["2,169 sentences"]}
HEAD_RE = re.compile(r"^(?:\d+(?:\.\d+)*\s+)?[A-Z][A-Za-z\-]+(?:\s+[A-Za-z\-]+){0,7}$")
MODEL, MAXTOK = "deepseek-v4-flash", 4096

def qtext(t): return json.loads((SB / "tasks" / t / "private_eval.json").read_text(encoding="utf-8"))["question"]
def get_cb():
    from langchain_community.callbacks.manager import get_openai_callback; return get_openai_callback
def cell_id(cell):
    mp = RUNS / "cell_map.json"; m = json.loads(mp.read_text(encoding="utf-8")) if mp.exists() else {}
    if cell not in m: m[cell] = f"cell_{len(m)+1:02d}"; mp.write_text(json.dumps(m, indent=2), encoding="utf-8")
    return m[cell]
def build_docpath(t, cond, cell):
    return C.stable_docpath({role: SB / "tasks" / t / fn for role, fn in COND_ROLES[cond].items()}, DOCP / cell_id(cell))

# ---------------- struct variant: section-aware chunking + cosine/BM25 union, dedup across sub-queries ----------------
def tokenize(s): return re.findall(r"[a-z0-9]+", s.lower())
class BM25:
    def __init__(self, docs, k1=1.5, b=0.75):
        self.docs = [tokenize(d) for d in docs]; self.N = max(1, len(docs)); self.avgdl = sum(map(len, self.docs)) / self.N
        self.df = collections.Counter(w for d in self.docs for w in set(d)); self.k1, self.b = k1, b
    def score(self, q):
        qt = tokenize(q); out = []
        for d in self.docs:
            tf = collections.Counter(d); s = 0.0
            for w in qt:
                if w not in tf: continue
                idf = math.log(1 + (self.N - self.df[w] + 0.5) / (self.df[w] + 0.5))
                s += idf * tf[w] * (self.k1 + 1) / (tf[w] + self.k1 * (1 - self.b + self.b * len(d) / self.avgdl))
            out.append(s)
        return out
def section_chunks(text, size=1000, overlap=100):
    from langchain_text_splitters import RecursiveCharacterTextSplitter
    from langchain_core.documents import Document
    lines = text.split("\n"); heads = []
    for i, l in enumerate(lines):
        s = l.strip()
        if 3 <= len(s) <= 70 and HEAD_RE.match(s) and i + 1 < len(lines) and lines[i + 1].strip() == "":
            heads.append(sum(len(x) + 1 for x in lines[:i]))
    bounds = ([0] if not heads or heads[0] > 0 else []) + heads + [len(text)]
    sp = RecursiveCharacterTextSplitter(chunk_size=size, chunk_overlap=overlap); out = []
    for a, b in zip(bounds, bounds[1:]):
        seg = text[a:b].strip()
        if seg: out.extend(c.page_content for c in sp.split_documents([Document(page_content=seg)]))
    return out
_SEEN: set = set(); _STRUCT_STATE = {"chunks": None}
async def struct_get_context(self, query, max_results=5, cost_callback=None):
    import numpy as np
    if _STRUCT_STATE["chunks"] is None:
        ch = []
        for d in self.documents:
            for c in section_chunks(d.get("raw_content", "") or ""): ch.append((d.get("url") or d.get("source") or "", c))
        E = np.array(self.embeddings.embed_documents([c for _, c in ch])); E = E / np.linalg.norm(E, axis=1, keepdims=True)
        _STRUCT_STATE["chunks"] = (ch, E, BM25([c for _, c in ch]))
    ch, E, bm = _STRUCT_STATE["chunks"]
    qv = np.array(self.embeddings.embed_query(query)); qv /= np.linalg.norm(qv)
    cos = E @ qv; bms = bm.score(query)
    top_cos = sorted(range(len(ch)), key=lambda i: -cos[i])[:10]; top_bm = sorted(range(len(ch)), key=lambda i: -bms[i])[:10]
    sel = sorted(set(top_cos) | set(top_bm))          # union, original order
    out = []
    for i in sel:
        key = (ch[i][0], ch[i][1].strip())
        if key in _SEEN: continue
        _SEEN.add(key); out.append(f"Source: {ch[i][0]}\nTitle: \nContent: {ch[i][1]}\n")
    return "\n".join(out)

_ORIG = {}
def apply_variant(variant):
    import gpt_researcher.context.compression as CM
    if "agc" not in _ORIG: _ORIG["agc"] = CM.ContextCompressor.async_get_context
    os.environ["COMPRESSION_THRESHOLD"] = "400000" if variant == "fullwin" else "8000"
    _SEEN.clear(); _STRUCT_STATE["chunks"] = None
    CM.ContextCompressor.async_get_context = struct_get_context if variant == "struct" else _ORIG["agc"]

# ---------------- followup variant: one gap check + <=2 re-retrievals with the same default retriever ----------------
GAP_PROMPT = ("You are checking whether retrieved context is sufficient to answer a question completely.\n"
              "Question: {q}\n\nRetrieved context:\n{ctx}\n\n"
              "Sufficient context means the context alone supports a complete answer to every part of the question. "
              "If it is sufficient, reply exactly: NONE. Otherwise list at most 2 short, specific search queries (one per line, no numbering) "
              "that would retrieve the missing information from the same documents. Reply with only NONE or the queries.")
def deepseek_call(prompt, guard, tag, log_path):
    est_in = len(prompt) // 3; est_cost = est_in * IN_RATE + MAXTOK * OUT_RATE
    ok, why = guard.preflight(est_cost, MAXTOK, est_in)
    if not ok: raise RuntimeError("BUDGET STOP " + why)
    body = json.dumps({"model": MODEL, "messages": [{"role": "user", "content": prompt}], "temperature": 0.4, "max_tokens": MAXTOK}).encode("utf-8")
    req = urllib.request.Request("https://api.deepseek.com/chat/completions", data=body, headers={"Content-Type": "application/json", "Authorization": "Bearer " + KEY})
    resp = json.loads(urllib.request.urlopen(req, timeout=600).read().decode("utf-8"))
    u = resp.get("usage") or {}; pt, ct = int(u.get("prompt_tokens", 0)), int(u.get("completion_tokens", 0)); cost = pt * IN_RATE + ct * OUT_RATE
    guard.record(cost, pt, ct, data={"stage": "roundS3", "variant": "followup", "tag": tag}, est_cost=est_cost, est_out=MAXTOK)
    content = ((resp.get("choices") or [{}])[0].get("message") or {}).get("content", "") or ""
    pathlib.Path(log_path).write_text(json.dumps({"prompt": prompt, "response": resp, "cost_usd": round(cost, 6)}, ensure_ascii=False, indent=2), encoding="utf-8")
    return content, cost, pt, ct

def variant_spent(variant):
    c = sqlite3.connect(str(LEDGER), timeout=30)
    v = c.execute("select coalesce(sum(cost),0) from calls where exp_key=? and data like ?", (EXP_KEY, f'%"variant": "{variant}"%')).fetchone()[0]; c.close(); return float(v)
def round_cap():
    bpath = RUNS / "ledger_baseline.json"
    if bpath.exists(): base = json.loads(bpath.read_text(encoding="utf-8"))["line_cost_at_round_start"]
    else:
        c = sqlite3.connect(str(LEDGER), timeout=30)
        base = c.execute("select coalesce(sum(cost),0) from calls where exp_key like 'evidence-package-pilot%' and exp_key != ?", (EXP_KEY,)).fetchone()[0]; c.close()
        bpath.write_text(json.dumps({"line_cost_at_round_start": base, "note": "round cap counts every roundS3 call incl. material generation", "created": time.strftime("%Y-%m-%dT%H:%M:%S")}, indent=2), encoding="utf-8")
    return round(min(LINE_CAP, base + ROUND_CAP), 4)

async def dry(cells):
    from gpt_researcher.document.document import DocumentLoader
    for (t, cond, v) in cells:
        cell = f"{t}_{cond}_{v}"; dp, mapping = build_docpath(t, cond, cell); docs = await DocumentLoader(str(dp)).load()
        line = f"{cell} -> {cell_id(cell)} docs={[d.get('url') for d in docs]} chars={[len(d.get('raw_content','')) for d in docs]}"
        if v == "struct": line += f" section_chunks={[len(section_chunks(d.get('raw_content',''))) for d in docs]}"
        print(line, flush=True)
    print("DRY DONE", flush=True)

async def run_cell(t, cond, variant, phase, guard, gcb, PL, pvar):
    cell = f"{t}_{cond}_{variant}"; cdir = RUNS / cell; cdir.mkdir(exist_ok=True)
    if (cdir / "meta.json").exists() and json.loads((cdir / "meta.json").read_text(encoding="utf-8")).get("done"): return "skip"
    if variant_spent(variant) + RES[variant] > VARIANT_CAP[variant]:
        print(f"{cell}: STOP variant cap {VARIANT_CAP[variant]} (spent ${variant_spent(variant):.4f})", flush=True); return "stop"
    ok, why = guard.preflight(RES[variant], int(RES[variant] / OUT_RATE))
    if not ok: print(f"{cell}: {why}", flush=True); return "stop"
    dp, mapping = build_docpath(t, cond, cell)
    os.environ["DOC_PATH"] = str(dp); os.environ["CURATE_SOURCES"] = "false"; C._CUR_SINK["path"] = None; C._CUR_SINK["state"] = None
    apply_variant(variant); offline_retriever.install_offline_retriever()
    from gpt_researcher import GPTResearcher
    plog = PL() if PL else None
    if plog is not None and pvar is not None: pvar.set(plog)
    t0 = time.time(); pt = ct = 0; report = ""; ctx = None; err = None; fu = None; extra_cost = 0.0
    try:
        r = GPTResearcher(query=qtext(t), report_type="research_report", report_source="local")
        with gcb() as cb:
            await r.conduct_research()
            if variant == "followup":
                ctx0 = r.context if isinstance(r.context, str) else "\n\n".join(map(str, r.context or []))
                ans, c1, p1, o1 = deepseek_call(GAP_PROMPT.format(q=qtext(t), ctx=ctx0[:60000]), guard, f"{cell}:gap", cdir / "gap_check.json")
                extra_cost += c1
                qs = [l.strip("-• ").strip() for l in ans.strip().splitlines() if l.strip() and l.strip().upper() != "NONE"][:2]
                fu = {"gap_answer": ans.strip()[:500], "queries": qs, "added_chars": 0}
                if qs:
                    from gpt_researcher.document.document import DocumentLoader
                    pages = await DocumentLoader(str(dp)).load(); added = []
                    for q in qs:
                        added.append(await r.context_manager.get_similar_content_by_query(q, pages))
                    addtxt = "\n\n".join(a for a in added if a)
                    fu["added_chars"] = len(addtxt); fu["added_doc1"] = addtxt.count("Source: document_1.txt"); fu["added_doc2"] = addtxt.count("Source: document_2.txt")
                    r.context = (ctx0 + "\n\n" + addtxt) if addtxt else ctx0
            report = await r.write_report()
        pt, ct = cb.prompt_tokens, cb.completion_tokens; ctx = r.context
        (cdir / "report.md").write_text(report or "", encoding="utf-8")
        (cdir / "context.txt").write_text(ctx if isinstance(ctx, str) else json.dumps(ctx, ensure_ascii=False, default=str), encoding="utf-8")
        if plog is not None: C.save_provider_logs(plog.calls, cdir / "provider_log.json", cdir / "provider_log_preview.json")
    except Exception as e:
        err = f"{type(e).__name__}: {e}"; print(f"{cell}: ERR {err}", flush=True)
    finally:
        apply_variant("default")
    cost = pt * IN_RATE + ct * OUT_RATE
    guard.record(cost, pt, ct, data={"stage": "roundS3", "variant": variant, "phase": phase, "cell": cell}, est_cost=RES[variant], est_out=int(RES[variant] / OUT_RATE))
    ctxs = (ctx if isinstance(ctx, str) else json.dumps(ctx, ensure_ascii=False, default=str)) or ""
    meta = {"cell": cell, "docpath_dir": cell_id(cell), "task": t, "condition": cond, "variant": variant, "arm": "F0", "phase": phase, "docpath_mapping": mapping,
            "question": qtext(t), "prompt_tokens": pt, "completion_tokens": ct, "deepseek_cost_usd": round(cost + extra_cost, 6), "host_cost_usd": round(cost, 6),
            "followup": fu, "report_chars": len(report or ""), "context_chars": len(ctxs), "doc1_blocks": ctxs.count("Source: document_1.txt"), "doc2_blocks": ctxs.count("Source: document_2.txt"),
            "paper_decisive_in_context": {k: (k.lower() in ctxs.lower()) for k in PAPER_KEY[t]},
            "n_llm_calls": sum(1 for c2 in (plog.calls if plog else []) if c2.get("phase") == "start") + (1 if variant == "followup" else 0),
            "elapsed_s": round(time.time() - t0, 1), "error": err, "done": err is None,
            "host": "gpt-researcher v3.6.1 (6f998577) fixed-contract, stage A config + variant", "model": "deepseek-v4-flash", "materials_manifest": "paper_round/stage_b/tasks_manifest_b.json"}
    (cdir / "meta.json").write_text(json.dumps(meta, ensure_ascii=False, indent=2), encoding="utf-8")
    with (RUNS / "roundS3_results.jsonl").open("a", encoding="utf-8") as f: f.write(json.dumps(meta, ensure_ascii=False) + "\n")
    print(f"{cell}: {'ok' if not err else 'error'} calls={meta['n_llm_calls']} ${cost+extra_cost:.4f} rep={len(report or '')} ctx={len(ctxs)} doc1={meta['doc1_blocks']} doc2={meta['doc2_blocks']} "
          f"decisive={meta['paper_decisive_in_context']} fu={None if not fu else (fu['queries'], fu.get('added_doc1'), fu.get('added_doc2'))}", flush=True)
    return "ok" if not err else "error"

async def main(args):
    variants = args.variant.split(","); tasks = args.tasks.split(","); conds = args.conds.split(",")
    cells = [(t, c, v) for v in variants for t in tasks for c in conds]
    if args.dry: await dry(cells); return
    C.install_curation_field_fix(); PL, pvar = C.make_provider_logger(); gcb = get_cb()
    guard = BudgetGuard(EXP_KEY, exp_prefix=PREFIX, call_cap=10**6, in_tok_cap=80_000_000, out_tok_cap=30_000_000); guard.cost_cap = round_cap()
    cur, calls, *_ = guard._totals(); print(f"COST ACCOUNTING: pilot* cum=${cur:.4f} ({calls} calls); round cap=${guard.cost_cap}; variant caps={VARIANT_CAP}; phase={args.phase}", flush=True)
    for (t, c, v) in cells:
        st = await run_cell(t, c, v, args.phase, guard, gcb, PL, pvar)
        if st == "stop": print("STOP (budget)", flush=True); break
    cur, calls, *_ = guard._totals(); print(f"ROUND S3 BATCH DONE: pilot* cum=${cur:.4f} ({calls} calls)", flush=True)

if __name__ == "__main__":
    ap = argparse.ArgumentParser(); ap.add_argument("--variant", default="default"); ap.add_argument("--tasks", default="B3,B5,B6,B7")
    ap.add_argument("--conds", default="C,P"); ap.add_argument("--phase", default="confirmatory"); ap.add_argument("--dry", action="store_true")
    asyncio.run(main(ap.parse_args()))
