#!/usr/bin/env python3
"""round_S4: simple verification strategies on top of the strongest cheap structural retrieval (struct, verbatim from round_S3).
Question: can a reasonable, simple verification strategy close the gap between "the context can answer the question"
(answerability) and "primary-source support was actually obtained"? Frozen materials stage_b/tasks/{B3,B6} (sha in
stage_b/tasks_manifest_b.json); host/model/config as stage A; F0 (no curation); one run per cell; <=12 completed flows.
Variants (ALL use struct retrieval = section-aware chunking + per-sub-query UNION of cosine top-10 and BM25 top-10, dedup):
  T0 : struct + the EXISTING answerability check of round_S3 (GAP_PROMPT verbatim) -> <=2 follow-up queries -> struct re-retrieval
  T1 : struct + a SOURCE-CONSTRAINT check: is every part of the question supported by a document_1 passage in the context?
       -> <=2 targeted follow-up queries only when primary support is missing -> struct re-retrieval
  T2 : struct + ONE fixed post-hoc verification call: the draft report is revised against the full text of document_1
       (research-and-revise idea truncated to one pass with a fixed evidence source; adapted stand-in, not any published method)
Roles (fixed by the deployment, given ONLY to the T1 checker and the T2 verifier, never to host drafting):
  document_1.txt = primary source (the paper); document_2.txt = secondary source (third-party note).
Evidence positions / gold values are NEVER given to any variant; follow-up queries come from the model given question+context.
Ledger exp_key evidence-package-pilot-roundS4; round cap $0.45 on top of the line total at round start; per-variant caps below.
Usage: python run_round_s4.py --variant T1 --tasks B3,B6 --conds C,P --phase confirmatory   |  --dry  |  --selftest"""
from __future__ import annotations
import os, sys, re, json, time, math, asyncio, pathlib, argparse, sqlite3, collections, urllib.request
ROOT = pathlib.Path(__file__).resolve().parent; PR = ROOT.parent; SB = PR / "stage_b"
RUNS = ROOT / "runs_s4"; DOCP = ROOT / "docpaths_s4"
sys.path.insert(0, "F:/defense/evidence_pack_prep_v1"); sys.path.insert(0, str(PR))
IN_RATE, OUT_RATE = 0.30 / 1_000_000, 1.20 / 1_000_000
EXP_KEY, PREFIX, ROUND_CAP, LINE_CAP = "evidence-package-pilot-roundS4", "evidence-package-pilot", 0.45, 10.0
VARIANT_CAP = {"T0": 0.10, "T1": 0.10, "T2": 0.14}
RES = {"T0": 0.02, "T1": 0.02, "T2": 0.03}          # per-cell reservation (host + extra calls), from round_S3 struct means + extra-call estimates
COND_ROLES = {"C": {"evidence": "E_fulltext.txt", "interp": "L.txt"}, "P": {"evidence": "E_fulltext.txt", "interp": "Lprime.txt"}}
PAPER_KEY = {"B3": ["hand-craft 163", "163 templates"], "B6": ["88 PD patients and 88 HC"]}   # evaluation-only exposure markers
HEAD_RE = re.compile(r"^(?:\d+(?:\.\d+)*\s+)?[A-Z][A-Za-z\-]+(?:\s+[A-Za-z\-]+){0,7}$")
MODEL, MAXTOK_CHECK, MAXTOK_VERIFY = "deepseek-v4-flash", 4096, 8192
_KEY = {"v": None}
def key():
    if _KEY["v"] is None: _KEY["v"] = pathlib.Path("F:/defense/research_v1/.deepseek_key").read_text(encoding="utf-8").strip()
    return _KEY["v"]
def setup_env():
    os.environ["OPENAI_API_KEY"] = key(); os.environ["OPENAI_BASE_URL"] = "https://api.deepseek.com"
    os.environ["FAST_LLM"] = os.environ["SMART_LLM"] = os.environ["STRATEGIC_LLM"] = "openai:deepseek-v4-flash"
    os.environ["EMBEDDING"] = "huggingface:sentence-transformers/all-MiniLM-L6-v2"
    os.environ["REPORT_SOURCE"] = "local"; os.environ["RETRIEVER"] = "offline_null"; os.environ["TEMPERATURE"] = "0.4"
    os.environ.setdefault("TOKENIZERS_PARALLELISM", "false"); RUNS.mkdir(exist_ok=True); DOCP.mkdir(exist_ok=True)

def qtext(t): return json.loads((SB / "tasks" / t / "private_eval.json").read_text(encoding="utf-8"))["question"]
def get_cb():
    from langchain_community.callbacks.manager import get_openai_callback; return get_openai_callback
def cell_id(cell):
    mp = RUNS / "cell_map.json"; m = json.loads(mp.read_text(encoding="utf-8")) if mp.exists() else {}
    if cell not in m: m[cell] = f"cell_{len(m)+1:02d}"; mp.write_text(json.dumps(m, indent=2), encoding="utf-8")
    return m[cell]
def build_docpath(t, cond, cell):
    import contract as C
    return C.stable_docpath({role: SB / "tasks" / t / fn for role, fn in COND_ROLES[cond].items()}, DOCP / cell_id(cell))
def primary_text(dp, t):
    """The runtime reads the primary document from the host's own document folder (deployment knowledge: which file is the
    paper). Asserts the role mapping so that a mapping slip can never silently hand the note to the verifier."""
    paper = (SB / "tasks" / t / "E_fulltext.txt").read_text(encoding="utf-8")
    for name in ("document_1.txt", "document_2.txt"):
        p = pathlib.Path(dp) / name
        if p.exists() and p.read_text(encoding="utf-8") == paper: return name, paper
    raise RuntimeError("primary document not found in docpath")

# ---------------- struct retrieval: VERBATIM copy of round_S3 run_round_s3.py (section-aware chunking + cosine/BM25 union) ----------------
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
        key_ = (ch[i][0], ch[i][1].strip())
        if key_ in _SEEN: continue
        _SEEN.add(key_); out.append(f"Source: {ch[i][0]}\nTitle: \nContent: {ch[i][1]}\n")
    return "\n".join(out)
_ORIG = {}
def apply_struct(on: bool):
    import gpt_researcher.context.compression as CM
    if "agc" not in _ORIG: _ORIG["agc"] = CM.ContextCompressor.async_get_context
    os.environ["COMPRESSION_THRESHOLD"] = "8000"
    _SEEN.clear(); _STRUCT_STATE["chunks"] = None
    CM.ContextCompressor.async_get_context = struct_get_context if on else _ORIG["agc"]

# ---------------- prompts (frozen inputs; sha of this file is recorded at freeze) ----------------
ROLE_TEXT = ("Document roles, fixed by the deployment (not stated inside the documents): document_1.txt is the primary source, "
             "the paper itself. document_2.txt is a secondary source, a third-party reading note about the paper.")
GAP_PROMPT = ("You are checking whether retrieved context is sufficient to answer a question completely.\n"       # VERBATIM round_S3
              "Question: {q}\n\nRetrieved context:\n{ctx}\n\n"
              "Sufficient context means the context alone supports a complete answer to every part of the question. "
              "If it is sufficient, reply exactly: NONE. Otherwise list at most 2 short, specific search queries (one per line, no numbering) "
              "that would retrieve the missing information from the same documents. Reply with only NONE or the queries.")
SUPPORT_PROMPT = ("You are checking whether retrieved context contains primary-source support for a complete answer to a question.\n"
                  + ROLE_TEXT + "\n"
                  "Question: {q}\n\nRetrieved context:\n{ctx}\n\n"
                  "Primary-source support for a part of the question means a passage labelled 'Source: document_1.txt' in the context "
                  "that itself states the needed fact. Passages labelled 'Source: document_2.txt' do not count as support, even if they "
                  "answer that part of the question. If every part of the question has primary-source support, reply exactly: NONE. "
                  "Otherwise list at most 2 short, specific search queries (one per line, no numbering) that would retrieve the missing "
                  "primary-source passages from document_1.txt. Reply with only NONE or the queries.")
VERIFY_PROMPT = ("You are performing one verification pass of a draft report against the primary source.\n"
                 + ROLE_TEXT + "\n"
                 "Question the report answers: {q}\n\n"
                 "Full text of document_1.txt (primary source):\n<<<\n{paper}\n>>>\n\n"
                 "Draft report:\n<<<\n{draft}\n>>>\n\n"
                 "Instructions: check every factual claim in the draft that concerns the paper against the primary source text above. "
                 "Where the draft states a value or relation that contradicts the primary source, replace it with the primary source's value, "
                 "cite document_1.txt, and you may note the discrepancy in one sentence. Where a claim cannot be found in the primary source, "
                 "keep it only if it is clearly attributed to document_2.txt and mark it as not verified against the primary source. "
                 "Do not add claims that appear in neither document and do not use outside knowledge. "
                 "Output the complete revised report in Markdown with the same overall structure, under 1500 words, keeping the final answer "
                 "to the question explicit. Output only the revised report.")
CHECK_PROMPT = {"T0": GAP_PROMPT, "T1": SUPPORT_PROMPT}
def parse_queries(ans):
    return [l.strip("-• ").strip() for l in ans.strip().splitlines() if l.strip() and l.strip().upper() != "NONE"][:2]

def deepseek_call(prompt, guard, tag, log_path, max_tokens, variant):
    est_in = len(prompt) // 3; est_cost = est_in * IN_RATE + max_tokens * OUT_RATE
    ok, why = guard.preflight(est_cost, max_tokens, est_in)
    if not ok: raise RuntimeError("BUDGET STOP " + why)
    body = json.dumps({"model": MODEL, "messages": [{"role": "user", "content": prompt}], "temperature": 0.4, "max_tokens": max_tokens}).encode("utf-8")
    req = urllib.request.Request("https://api.deepseek.com/chat/completions", data=body, headers={"Content-Type": "application/json", "Authorization": "Bearer " + key()})
    resp = json.loads(urllib.request.urlopen(req, timeout=900).read().decode("utf-8"))
    u = resp.get("usage") or {}; pt, ct = int(u.get("prompt_tokens", 0)), int(u.get("completion_tokens", 0)); cost = pt * IN_RATE + ct * OUT_RATE
    guard.record(cost, pt, ct, data={"stage": "roundS4", "variant": variant, "tag": tag}, est_cost=est_cost, est_out=max_tokens)
    ch0 = (resp.get("choices") or [{}])[0]; content = (ch0.get("message") or {}).get("content", "") or ""; fin = ch0.get("finish_reason")
    pathlib.Path(log_path).write_text(json.dumps({"prompt": prompt, "response": resp, "cost_usd": round(cost, 6)}, ensure_ascii=False, indent=2), encoding="utf-8")
    return content, cost, pt, ct, fin

def variant_spent(variant):
    from ledger_guard import LEDGER
    c = sqlite3.connect(str(LEDGER), timeout=30)
    v = c.execute("select coalesce(sum(cost),0) from calls where exp_key=? and data like ?", (EXP_KEY, f'%"variant": "{variant}"%')).fetchone()[0]; c.close(); return float(v)
def round_cap():
    from ledger_guard import LEDGER
    bpath = RUNS / "ledger_baseline.json"
    if bpath.exists(): base = json.loads(bpath.read_text(encoding="utf-8"))["line_cost_at_round_start"]
    else:
        c = sqlite3.connect(str(LEDGER), timeout=30)
        base = c.execute("select coalesce(sum(cost),0) from calls where exp_key like 'evidence-package-pilot%' and exp_key != ?", (EXP_KEY,)).fetchone()[0]; c.close()
        bpath.write_text(json.dumps({"line_cost_at_round_start": base, "note": "round cap counts every roundS4 call (host + check + verify)", "created": time.strftime("%Y-%m-%dT%H:%M:%S")}, indent=2), encoding="utf-8")
    return round(min(LINE_CAP, base + ROUND_CAP), 4)

async def dry(cells):
    from gpt_researcher.document.document import DocumentLoader
    for (t, cond, v) in cells:
        cell = f"{t}_{cond}_{v}"; dp, mapping = build_docpath(t, cond, cell); docs = await DocumentLoader(str(dp)).load()
        name, paper = primary_text(dp, t)
        print(f"{cell} -> {cell_id(cell)} docs={[d.get('url') for d in docs]} chars={[len(d.get('raw_content','')) for d in docs]} "
              f"section_chunks={[len(section_chunks(d.get('raw_content',''))) for d in docs]} primary={name}", flush=True)
    print("DRY DONE", flush=True)

async def selftest():
    """Zero-cost plumbing test: struct re-retrieval through the host's context manager, check-prompt parsing, verify-prompt size."""
    from gpt_researcher.document.document import DocumentLoader
    from gpt_researcher import GPTResearcher
    import contract as C, offline_retriever
    C.install_curation_field_fix(); offline_retriever.install_offline_retriever()
    for t in ("B6", "B3"):
        dp, mapping = C.stable_docpath({role: SB / "tasks" / t / fn for role, fn in COND_ROLES["P"].items()}, DOCP / f"selftest_{t}"); apply_struct(True)
        r = GPTResearcher(query=qtext(t), report_type="research_report", report_source="local")
        pages = await DocumentLoader(str(dp)).load()
        q1 = "what is the paper about"                       # generic warm-up: fills _SEEN like real sub-queries would
        first = await r.context_manager.get_similar_content_by_query(q1, pages)
        q2 = {"B6": "German speech recordings PD patients HC speakers", "B3": "hand-crafted templates for the domain-specific knowledge base"}[t]
        added = await r.context_manager.get_similar_content_by_query(q2, pages)
        name, paper = primary_text(dp, t)
        vp = VERIFY_PROMPT.format(q=qtext(t), paper=paper, draft="(draft placeholder)" * 500)
        print(f"{t}: first={len(first)} chars doc1={first.count('Source: document_1.txt')} | re-retrieval added={len(added)} chars "
              f"doc1={added.count('Source: document_1.txt')} doc2={added.count('Source: document_2.txt')} decisive_in_added={[k.lower() in added.lower() for k in PAPER_KEY[t]]} "
              f"| primary={name} verify_prompt_chars={len(vp)} parse={parse_queries('foo\nNONE\nbar\nbaz')}", flush=True)
        apply_struct(False)
    print("SELFTEST DONE", flush=True)

async def run_cell(t, cond, variant, phase, guard, gcb, PL, pvar):
    from gpt_researcher.document.document import DocumentLoader
    import contract as C, offline_retriever
    cell = f"{t}_{cond}_{variant}"; cdir = RUNS / cell; cdir.mkdir(exist_ok=True)
    if (cdir / "meta.json").exists() and json.loads((cdir / "meta.json").read_text(encoding="utf-8")).get("done"): return "skip"
    if variant_spent(variant) + RES[variant] > VARIANT_CAP[variant]:
        print(f"{cell}: STOP variant cap {VARIANT_CAP[variant]} (spent ${variant_spent(variant):.4f})", flush=True); return "stop"
    ok, why = guard.preflight(RES[variant], int(RES[variant] / OUT_RATE))
    if not ok: print(f"{cell}: {why}", flush=True); return "stop"
    dp, mapping = build_docpath(t, cond, cell)
    os.environ["DOC_PATH"] = str(dp); os.environ["CURATE_SOURCES"] = "false"; C._CUR_SINK["path"] = None; C._CUR_SINK["state"] = None
    apply_struct(True); offline_retriever.install_offline_retriever()
    from gpt_researcher import GPTResearcher
    plog = PL() if PL else None
    if plog is not None and pvar is not None: pvar.set(plog)
    t0 = time.time(); pt = ct = 0; report = ""; draft = None; ctx = None; err = None; chk = None; ver = None; extra_cost = 0.0; extra_pt = 0; extra_ct = 0
    try:
        r = GPTResearcher(query=qtext(t), report_type="research_report", report_source="local")
        with gcb() as cb:
            await r.conduct_research()
            if variant in ("T0", "T1"):
                ctx0 = r.context if isinstance(r.context, str) else "\n\n".join(map(str, r.context or []))
                ans, c1, p1, o1, fin = deepseek_call(CHECK_PROMPT[variant].format(q=qtext(t), ctx=ctx0[:60000]), guard, f"{cell}:check", cdir / "check.json", MAXTOK_CHECK, variant)
                extra_cost += c1; extra_pt += p1; extra_ct += o1
                qs = parse_queries(ans)
                chk = {"kind": "answerability" if variant == "T0" else "primary_support", "answer": ans.strip()[:500], "queries": qs, "finish_reason": fin,
                       "ctx0_chars": len(ctx0), "ctx0_doc1": ctx0.count("Source: document_1.txt"), "ctx0_doc2": ctx0.count("Source: document_2.txt"),
                       "paper_decisive_in_ctx0": {k: (k.lower() in ctx0.lower()) for k in PAPER_KEY[t]}, "added_chars": 0, "added_doc1": 0, "added_doc2": 0, "cost_usd": round(c1, 6)}
                if qs:
                    pages = await DocumentLoader(str(dp)).load(); added = []
                    for q in qs: added.append(await r.context_manager.get_similar_content_by_query(q, pages))   # struct patch active, dedup vs _SEEN
                    addtxt = "\n\n".join(a for a in added if a)
                    chk["added_chars"] = len(addtxt); chk["added_doc1"] = addtxt.count("Source: document_1.txt"); chk["added_doc2"] = addtxt.count("Source: document_2.txt")
                    chk["paper_decisive_in_added"] = {k: (k.lower() in addtxt.lower()) for k in PAPER_KEY[t]}
                    (cdir / "added_context.txt").write_text(addtxt, encoding="utf-8")
                    r.context = (ctx0 + "\n\n" + addtxt) if addtxt else ctx0
            report = await r.write_report()
            if variant == "T2":
                draft = report; (cdir / "report_draft.md").write_text(draft or "", encoding="utf-8")
                name, paper = primary_text(dp, t)
                vp = VERIFY_PROMPT.format(q=qtext(t), paper=paper, draft=draft or "")
                ans, c2, p2, o2, fin = deepseek_call(vp, guard, f"{cell}:verify", cdir / "verify.json", MAXTOK_VERIFY, variant)
                extra_cost += c2; extra_pt += p2; extra_ct += o2
                ver = {"primary_file": name, "input_chars": len(vp), "paper_chars": len(paper), "draft_chars": len(draft or ""), "output_chars": len(ans),
                       "finish_reason": fin, "prompt_tokens": p2, "completion_tokens": o2, "cost_usd": round(c2, 6), "fallback_to_draft": not ans.strip()}
                report = ans if ans.strip() else draft
        pt, ct = cb.prompt_tokens, cb.completion_tokens; ctx = r.context
        (cdir / "report.md").write_text(report or "", encoding="utf-8")
        (cdir / "context.txt").write_text(ctx if isinstance(ctx, str) else json.dumps(ctx, ensure_ascii=False, default=str), encoding="utf-8")
        if plog is not None: C.save_provider_logs(plog.calls, cdir / "provider_log.json", cdir / "provider_log_preview.json")
    except Exception as e:
        err = f"{type(e).__name__}: {e}"; print(f"{cell}: ERR {err}", flush=True)
    finally:
        apply_struct(False)
    cost = pt * IN_RATE + ct * OUT_RATE
    guard.record(cost, pt, ct, data={"stage": "roundS4", "variant": variant, "phase": phase, "cell": cell, "tag": "host"}, est_cost=RES[variant], est_out=int(RES[variant] / OUT_RATE))
    ctxs = (ctx if isinstance(ctx, str) else json.dumps(ctx, ensure_ascii=False, default=str)) or ""
    meta = {"cell": cell, "docpath_dir": cell_id(cell), "task": t, "condition": cond, "variant": variant, "arm": "F0", "phase": phase, "docpath_mapping": mapping,
            "question": qtext(t), "host_prompt_tokens": pt, "host_completion_tokens": ct, "extra_prompt_tokens": extra_pt, "extra_completion_tokens": extra_ct,
            "total_prompt_tokens": pt + extra_pt, "deepseek_cost_usd": round(cost + extra_cost, 6), "host_cost_usd": round(cost, 6), "extra_cost_usd": round(extra_cost, 6),
            "check": chk, "verify": ver, "report_chars": len(report or ""), "draft_chars": (len(draft) if draft is not None else None),
            "context_chars": len(ctxs), "doc1_blocks": ctxs.count("Source: document_1.txt"), "doc2_blocks": ctxs.count("Source: document_2.txt"),
            "paper_decisive_in_context": {k: (k.lower() in ctxs.lower()) for k in PAPER_KEY[t]},
            "n_llm_calls": sum(1 for c2 in (plog.calls if plog else []) if c2.get("phase") == "start") + (1 if variant in ("T0", "T1", "T2") else 0),
            "elapsed_s": round(time.time() - t0, 1), "error": err, "done": err is None,
            "host": "gpt-researcher v3.6.1 (6f998577) fixed-contract, stage A config + struct retrieval + variant", "model": "deepseek-v4-flash",
            "materials_manifest": "paper_round/stage_b/tasks_manifest_b.json"}
    (cdir / "meta.json").write_text(json.dumps(meta, ensure_ascii=False, indent=2), encoding="utf-8")
    with (RUNS / "roundS4_results.jsonl").open("a", encoding="utf-8") as f: f.write(json.dumps(meta, ensure_ascii=False) + "\n")
    print(f"{cell}: {'ok' if not err else 'error'} calls={meta['n_llm_calls']} ${cost+extra_cost:.4f} (host ${cost:.4f}) ptok={pt + extra_pt} rep={len(report or '')} ctx={len(ctxs)} "
          f"doc1={meta['doc1_blocks']} doc2={meta['doc2_blocks']} decisive={meta['paper_decisive_in_context']} "
          f"check={None if not chk else (chk['queries'], chk['added_doc1'], chk['added_doc2'], chk.get('paper_decisive_in_added'))} "
          f"verify={None if not ver else (ver['finish_reason'], ver['output_chars'], ver['completion_tokens'])}", flush=True)
    return "ok" if not err else "error"

async def main(args):
    from ledger_guard import BudgetGuard
    import contract as C
    variants = args.variant.split(","); tasks = args.tasks.split(","); conds = args.conds.split(",")
    cells = [(t, c, v) for v in variants for t in tasks for c in conds]
    if args.dry: await dry(cells); return
    if args.selftest: await selftest(); return
    C.install_curation_field_fix(); PL, pvar = C.make_provider_logger(); gcb = get_cb()
    guard = BudgetGuard(EXP_KEY, exp_prefix=PREFIX, call_cap=10**6, in_tok_cap=80_000_000, out_tok_cap=30_000_000); guard.cost_cap = round_cap()
    cur, calls, *_ = guard._totals(); print(f"COST ACCOUNTING: pilot* cum=${cur:.4f} ({calls} calls); round cap=${guard.cost_cap}; variant caps={VARIANT_CAP}; phase={args.phase}", flush=True)
    for (t, c, v) in cells:
        st = await run_cell(t, c, v, args.phase, guard, gcb, PL, pvar)
        if st == "stop": print("STOP (budget)", flush=True); break
    cur, calls, *_ = guard._totals(); print(f"ROUND S4 BATCH DONE: pilot* cum=${cur:.4f} ({calls} calls)", flush=True)

if __name__ == "__main__":
    ap = argparse.ArgumentParser(); ap.add_argument("--variant", default="T0"); ap.add_argument("--tasks", default="B3,B6")
    ap.add_argument("--conds", default="C,P"); ap.add_argument("--phase", default="confirmatory"); ap.add_argument("--dry", action="store_true"); ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args(); setup_env(); asyncio.run(main(a))
