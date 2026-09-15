#!/usr/bin/env python3
"""round_R3: CONDITION-flip notes (L'', materials/<T>/Lcond.txt, one flipped qualifier, numbers unchanged) x primary readability.
Host, model, config, tasks and attack permission unchanged from round_R1/R2 (full documents in the window, COMPRESSION_THRESHOLD=400000,
F0, thinking mode, one run per cell). Primary variants: synthetic levels of round_R1 (L0 clean, L3 OCR-style noise, ...) or a real
extraction variant of round_R2 (materials/<T>/E_<variant>.txt). Note conditions: C = faithful L, P = numeric flip L' (round_R1),
Q = condition flip L'' (this round). Ledger exp_key evidence-package-pilot-roundR3; per-cell reservation $0.035.
Usage: python run_round_r3.py --tasks B1,B3,B5,B6,B7 --levels 0,3 --conds Q --rep 1 --cap 0.80 | --dry"""
from __future__ import annotations
import os, sys, re, json, time, shutil, asyncio, pathlib, argparse, sqlite3
ROOT = pathlib.Path(__file__).resolve().parent; PR = ROOT.parent; SB = PR / "stage_b"; R1MAT = PR / "round_r1" / "materials"; R2MAT = PR / "round_r2" / "materials"
MAT = ROOT / "materials"; RUNS = ROOT / "runs_r3"; DOCP = ROOT / "docpaths_r3"
sys.path.insert(0, "F:/defense/evidence_pack_prep_v1"); sys.path.insert(0, str(PR)); sys.path.insert(0, str(ROOT))
from gen_cond_r3 import COND
IN_RATE, OUT_RATE = 0.30 / 1_000_000, 1.20 / 1_000_000
EXP_KEY, PREFIX, ROUND_CAP, LINE_CAP, RES = "evidence-package-pilot-roundR3", "evidence-package-pilot", 0.80, 10.0, 0.035
NUM_KEY = {"B1": ["220 human-human dialogs"], "B3": ["hand-craft 163", "163 templates"], "B5": ["97.78 to 87.38", "1.39 to 1.33"],
           "B6": ["88 PD patients and 88 HC"], "B7": ["2,169 sentences"]}   # evaluation-only exposure markers (numeric flip)
def paper_key(t, cond): return COND[t]["paper_decisive"] if cond == "Q" else NUM_KEY[t]
_KEY = {"v": None}
def key():
    if _KEY["v"] is None: _KEY["v"] = pathlib.Path("F:/defense/research_v1/.deepseek_key").read_text(encoding="utf-8").strip()
    return _KEY["v"]
def setup_env():
    os.environ["OPENAI_API_KEY"] = key(); os.environ["OPENAI_BASE_URL"] = "https://api.deepseek.com"
    os.environ["FAST_LLM"] = os.environ["SMART_LLM"] = os.environ["STRATEGIC_LLM"] = "openai:deepseek-v4-flash"
    os.environ["EMBEDDING"] = "huggingface:sentence-transformers/all-MiniLM-L6-v2"
    os.environ["REPORT_SOURCE"] = "local"; os.environ["RETRIEVER"] = "offline_null"; os.environ["TEMPERATURE"] = "0.4"
    os.environ["COMPRESSION_THRESHOLD"] = "400000"
    os.environ.setdefault("TOKENIZERS_PARALLELISM", "false"); RUNS.mkdir(exist_ok=True); DOCP.mkdir(exist_ok=True)

def qtext(t): return json.loads((SB / "tasks" / t / "private_eval.json").read_text(encoding="utf-8"))["question"]
def note_file(t, cond): return {"C": SB / "tasks" / t / "L.txt", "P": SB / "tasks" / t / "Lprime.txt", "Q": MAT / t / "Lcond.txt"}[cond]
def evidence_file(t, level):
    if level == "0": return SB / "tasks" / t / "E_fulltext.txt"
    if level.isdigit(): return R1MAT / t / f"E_L{level}.txt"
    return R2MAT / t / f"E_{level}.txt"
def lvname(level): return f"L{level}" if level.isdigit() else level
def get_cb():
    from langchain_community.callbacks.manager import get_openai_callback; return get_openai_callback
def cell_id(cell):
    mp = RUNS / "cell_map.json"; m = json.loads(mp.read_text(encoding="utf-8")) if mp.exists() else {}
    if cell not in m: m[cell] = f"cell_{len(m)+1:02d}"; mp.write_text(json.dumps(m, indent=2), encoding="utf-8")
    return m[cell]
def build_docpath(t, level, cond, cell):
    out = DOCP / cell_id(cell)
    if out.exists(): shutil.rmtree(out)
    out.mkdir(parents=True)
    shutil.copy(evidence_file(t, level), out / "document_1.txt"); shutil.copy(note_file(t, cond), out / "document_2.txt")
    return out, {"evidence": "document_1.txt", "interp": "document_2.txt"}
def norm_digits(s): return re.sub(r"(?<=\d) (?=\d)", "", s)
def tokwin(k, s):
    """decisive tokens present IN ORDER inside a window of 3x the string length (digit-space-normalized, lower-cased)"""
    nd = norm_digits(s.lower()); toks = [x for x in re.findall(r"[a-z0-9]+", k.lower()) if len(x) >= 2]
    for m in re.finditer(re.escape(toks[0]), nd):
        seg = nd[m.start(): m.start() + 3 * len(k)]; pos = 0; ok = True
        for x in toks:
            j = seg.find(x, pos)
            if j < 0: ok = False; break
            pos = j + len(x)
        if ok: return True
    return False
async def primary_text(dp):
    """text of document_1.* exactly as the host's DocumentLoader loads it (page blocks joined); the note is excluded so the
    exposure check measures the primary source only (the faithful note L contains the decisive strings verbatim)"""
    from gpt_researcher.document.document import DocumentLoader
    docs = await DocumentLoader(str(dp)).load()
    return "\n".join(d.get("raw_content", "") for d in docs if str(d.get("url", "")).startswith("document_1")), len(docs)
def round_cap():
    from ledger_guard import LEDGER
    bpath = RUNS / f"ledger_baseline_{EXP_KEY.rsplit('-', 1)[-1]}.json"
    if bpath.exists(): base = json.loads(bpath.read_text(encoding="utf-8"))["line_cost_at_round_start"]
    else:
        c = sqlite3.connect(str(LEDGER), timeout=30)
        base = c.execute("select coalesce(sum(cost),0) from calls where exp_key like 'evidence-package-pilot%' and exp_key != ?", (EXP_KEY,)).fetchone()[0]; c.close()
        bpath.write_text(json.dumps({"line_cost_at_round_start": base, "created": time.strftime("%Y-%m-%dT%H:%M:%S"), "round_cap_usd": ROUND_CAP}, indent=2), encoding="utf-8")
    return round(min(LINE_CAP, base + ROUND_CAP), 4)

async def dry(cells):
    from gpt_researcher.document.document import DocumentLoader
    for (t, lv, cond) in cells:
        cell = f"{t}_{lvname(lv)}_{cond}"; dp, mapping = build_docpath(t, lv, cond, cell); docs = await DocumentLoader(str(dp)).load()
        joined = "\n".join(d.get("raw_content", "") for d in docs if str(d.get("url", "")).startswith("document_1")); total = sum(len(d.get("raw_content", "")) for d in docs)
        print(f"{cell} -> {cell_id(cell)} blocks={len(docs)} chars={total} (<400000 -> direct window) decisive_tokwin={ {k: tokwin(k, joined) for k in paper_key(t, cond)} }", flush=True)
    print("DRY DONE", flush=True)

async def run_cell(t, lv, cond, phase, guard, gcb, PL, pvar, rep=1):
    import contract as C, offline_retriever
    cell = f"{t}_{lvname(lv)}_{cond}" + (f"_r{rep}" if rep > 1 else ""); cdir = RUNS / cell; cdir.mkdir(exist_ok=True)
    if (cdir / "meta.json").exists() and json.loads((cdir / "meta.json").read_text(encoding="utf-8")).get("done"): return "skip"
    ok, why = guard.preflight(RES, int(RES / OUT_RATE))
    if not ok: print(f"{cell}: {why}", flush=True); return "stop"
    dp, mapping = build_docpath(t, lv, cond, cell)
    os.environ["DOC_PATH"] = str(dp); os.environ["CURATE_SOURCES"] = "false"; C._CUR_SINK["path"] = None; C._CUR_SINK["state"] = None
    offline_retriever.install_offline_retriever()
    from gpt_researcher import GPTResearcher
    plog = PL() if PL else None
    if plog is not None and pvar is not None: pvar.set(plog)
    t0 = time.time(); pt = ct = 0; report = ""; ctx = None; err = None
    try:
        r = GPTResearcher(query=qtext(t), report_type="research_report", report_source="local")
        with gcb() as cb:
            await r.conduct_research(); report = await r.write_report()
        pt, ct = cb.prompt_tokens, cb.completion_tokens; ctx = r.context
        (cdir / "report.md").write_text(report or "", encoding="utf-8")
        (cdir / "context.txt").write_text(ctx if isinstance(ctx, str) else json.dumps(ctx, ensure_ascii=False, default=str), encoding="utf-8")
        if plog is not None: C.save_provider_logs(plog.calls, cdir / "provider_log.json", cdir / "provider_log_preview.json")
    except Exception as e:
        err = f"{type(e).__name__}: {e}"; print(f"{cell}: ERR {err}", flush=True)
    cost = pt * IN_RATE + ct * OUT_RATE
    guard.record(cost, pt, ct, data={"stage": "roundR3", "level": lv, "cond": cond, "phase": phase, "cell": cell}, est_cost=RES, est_out=int(RES / OUT_RATE))
    ctxs = (ctx if isinstance(ctx, str) else json.dumps(ctx, ensure_ascii=False, default=str)) or ""
    prim, _nblk = await primary_text(dp)   # exposure on the primary only
    meta = {"cell": cell, "docpath_dir": cell_id(cell), "task": t, "level": lvname(lv), "condition": cond, "rep": rep, "arm": "F0-fullwin", "phase": phase, "docpath_mapping": mapping,
            "evidence_file": str(evidence_file(t, lv)), "note_file": str(note_file(t, cond)), "question": qtext(t), "prompt_tokens": pt, "completion_tokens": ct, "deepseek_cost_usd": round(cost, 6),
            "report_chars": len(report or ""), "context_chars": len(ctxs), "primary_chars": len(prim), "exposure_scope": "document_1 only", "doc1_blocks": ctxs.count("Source: document_1."), "doc2_blocks": ctxs.count("Source: document_2.txt"),
            "paper_decisive_in_context_verbatim": {k: (k.lower() in prim.lower()) for k in paper_key(t, cond)},
            "paper_decisive_in_context_digitnorm": {k: (k.lower() in norm_digits(prim).lower()) for k in paper_key(t, cond)},
            "paper_decisive_in_context_tokwin": {k: tokwin(k, prim) for k in paper_key(t, cond)},
            "n_llm_calls": sum(1 for c2 in (plog.calls if plog else []) if c2.get("phase") == "start"),
            "elapsed_s": round(time.time() - t0, 1), "error": err, "done": err is None,
            "host": "gpt-researcher v3.6.1 (6f998577) fixed-contract, stage A config, full documents in window (COMPRESSION_THRESHOLD=400000)", "model": "deepseek-v4-flash",
            "materials_manifest": "round_r3/materials/manifest.json (L'') + round_r1/materials/manifest.json (levels) + round_r2/materials/manifest.json (real variants)"}
    (cdir / "meta.json").write_text(json.dumps(meta, ensure_ascii=False, indent=2), encoding="utf-8")
    with (RUNS / "roundR3_results.jsonl").open("a", encoding="utf-8") as f: f.write(json.dumps(meta, ensure_ascii=False) + "\n")
    print(f"{cell}: {'ok' if not err else 'error'} calls={meta['n_llm_calls']} ${cost:.4f} ptok={pt} rep={len(report or '')} ctx={len(ctxs)} tokwin={meta['paper_decisive_in_context_tokwin']}", flush=True)
    return "ok" if not err else "error"

async def main(args):
    from ledger_guard import BudgetGuard
    import contract as C
    tasks = args.tasks.split(","); levels = args.levels.split(","); conds = args.conds.split(",")
    cells = [(t, lv, c) for lv in levels for t in tasks for c in conds]
    if args.dry: await dry(cells); return
    C.install_curation_field_fix(); PL, pvar = C.make_provider_logger(); gcb = get_cb()
    guard = BudgetGuard(EXP_KEY, exp_prefix=PREFIX, call_cap=10**6, in_tok_cap=80_000_000, out_tok_cap=30_000_000); guard.cost_cap = round_cap()
    cur, calls, *_ = guard._totals(); print(f"COST ACCOUNTING: pilot* cum=${cur:.4f} ({calls} calls); round cap=${guard.cost_cap}; cells={len(cells)}; phase={args.phase}", flush=True)
    for (t, lv, c) in cells:
        st = await run_cell(t, lv, c, args.phase, guard, gcb, PL, pvar, rep=args.rep)
        if st == "stop": print("STOP (budget)", flush=True); break
    cur, calls, *_ = guard._totals(); print(f"ROUND R3 BATCH DONE: pilot* cum=${cur:.4f} ({calls} calls)", flush=True)

if __name__ == "__main__":
    ap = argparse.ArgumentParser(); ap.add_argument("--tasks", default="B1,B3,B5,B6,B7"); ap.add_argument("--levels", default="0,3")
    ap.add_argument("--conds", default="Q"); ap.add_argument("--phase", default="confirmatory"); ap.add_argument("--dry", action="store_true"); ap.add_argument("--rep", type=int, default=1)
    ap.add_argument("--exp-key", default=""); ap.add_argument("--cap", type=float, default=0.0)
    a = ap.parse_args()
    if a.exp_key: EXP_KEY = a.exp_key
    if a.cap: ROUND_CAP = a.cap
    setup_env(); asyncio.run(main(a))
