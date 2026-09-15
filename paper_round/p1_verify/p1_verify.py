#!/usr/bin/env python3
"""P1: reference implementation of claim-level verification on FROZEN S4 snapshots (same saved retrieval context + same saved
draft), compared with full-text verification under the SAME patch protocol. Component reuse, not a new method:
  claim extraction with conditions kept (RefChecker-style), judgment against the known primary document (RefChecker
  Accurate-Context style, table composition / transparent arithmetic count as support), selective targeted retrieval only for
  claims the primary passages in the window do not address (skip signal = document support, not model confidence),
  minimal patches with a RARR-style edit-ratio rejection gate.
Arms:
  V-ref     : extract -> judge against document_1 blocks of the saved window -> for Neutral claims: one targeted struct retrieval
              over document_1 (query = subject/attribute/condition words, NO value) -> judge again (window + retrieved) -> patches
  V-full    : one call: draft + full document_1 -> same patch JSON
  V-rewrite : (optional ablation) S4 VERIFY_PROMPT full rewrite under the same reasoning configuration
Engineering contract: every call records finish_reason / tokens / parse status; statuses VALID_NO_GAP / VALID_GAP /
INVALID_OR_INCOMPLETE; empty text or bad JSON or truncation => INVALID; any INVALID stage => final output UNVERIFIED_OUTPUT.
Runtime never reads private_eval, evidence positions or gold values (assertion before each call). Ledger exp_key
evidence-package-pilot-p1verify, cap $0.50 on top of the line at stage start, call_cap +120 over the line count at stage start.
Calibration history: runs_p1/CALIBRATION_LOG.md (dev1 -> dev2 changes). Usage:
  python p1_verify.py --probe | --round dev2 --arms V-ref,V-full --snaps all [--config cfg.json] [--force]"""
from __future__ import annotations
import os, sys, re, json, time, math, pathlib, argparse, sqlite3, urllib.request, urllib.error
ROOT = pathlib.Path(__file__).resolve().parent; PR = ROOT.parent; SB = PR / "stage_b"; S4 = PR / "round_s4"
RUNS = ROOT / "runs_p1"; DOCP = ROOT / "docpaths_p1"
sys.path.insert(0, "F:/defense/evidence_pack_prep_v1"); sys.path.insert(0, str(PR)); sys.path.insert(0, str(S4))
IN_RATE, OUT_RATE = 0.30 / 1_000_000, 1.20 / 1_000_000
EXP_KEY, PREFIX, STAGE_CAP, LINE_CAP, CALL_CAP = "evidence-package-pilot-p1verify", "evidence-package-pilot", 0.50, 10.0, 120
MODEL = "deepseek-v4-flash"
SNAPS = {  # snapshot -> (S4 cell, draft file); context.txt of the cell is the frozen drafting window
    "S-miss-wrong": ("B6_P_T0", "report.md"), "S-miss-right": ("B6_C_T1", "report.md"),
    "S-table": ("B6_P_T2", "report_draft.md"), "S-present": ("B3_P_T2", "report_draft.md")}
DEFAULT_CFG = {"thinking": "disabled", "reasoning_effort": None, "temperature": 0.0, "max_tokens": 16384, "json_mode": True,
               "retrieval_k": 10, "max_neutral_retrieval": 12, "max_claims": 50, "max_spans": 5, "edit_ratio_gate": 0.5}
_KEY = {"v": None}
def key():
    if _KEY["v"] is None: _KEY["v"] = pathlib.Path("F:/defense/research_v1/.deepseek_key").read_text(encoding="utf-8").strip()
    return _KEY["v"]
from run_round_s4 import section_chunks, BM25, ROLE_TEXT, VERIFY_PROMPT   # verbatim components from round_S4

# ---------------- prompts (frozen at PREREG_p1 freeze; sha of this file recorded) ----------------
META_RULE = ("Statements about what the draft's own material or sources contain or omit (for example 'not reported in the extract', 'the provided "
             "information does not list', 'Document 2 confirms') are not claims about the paper's content: do not extract or patch them.")
EXTRACT_PROMPT = ("You extract the factual claims that a draft report actually asserts about a paper, so they can be verified.\n" + ROLE_TEXT + "\n"
 "Question the report answers: {q}\n\nDraft report:\n<<<\n{draft}\n>>>\n\n"
 "Extract claims that state a number, count, size, score, or a relation between named entities concerning the paper's content (its data, method, "
 "experiments, results). List each DISTINCT claim once (same subject, attribute, value and condition), starting with claims in the direct answer and the "
 "conclusion, at most {max_claims} claims. Keep each claim self-contained: record subject, attribute, value, unit_or_denominator and condition (dataset, "
 "language, setting or version; \"\" if none) exactly as the draft states them. If a sentence attributes the value to a source (e.g. 'the note reports 103'), "
 "put that attribution in the attribute (e.g. 'template count as reported by document_2'). Skip opinions, suggestions and hedges. " + META_RULE + " "
 "For each claim list sentence_spans: every place the draft states it (up to {max_spans}), each copied verbatim from the draft (an exact substring, at most "
 "250 characters, including table rows), and record cited_source for the first span as \"document_1.txt\", \"document_2.txt\", \"both\" or \"none\".\n"
 "Return only JSON: {{\"claims\":[{{\"id\":\"c1\",\"subject\":\"\",\"attribute\":\"\",\"value\":\"\",\"unit_or_denominator\":\"\",\"condition\":\"\",\"cited_source\":\"\",\"sentence_spans\":[\"\"]}}]}}")
JUDGE_PROMPT = ("You judge whether claims are supported by passages from the primary source.\n" + ROLE_TEXT + "\n"
 "Claims (JSON): {claims}\n\nPassages from document_1.txt:\n<<<\n{passages}\n>>>\n\n"
 "For each claim give label \"Entailment\" if the passages state the claim's value for the same subject, attribute and condition, either directly or "
 "by a transparent combination of figures the passages state (for example a table's male and female counts summing to the total, or counts stated for "
 "each part adding up to the claimed total); \"Contradiction\" if the passages state a different value for the same subject, attribute and condition; "
 "\"Neutral\" if the passages do not address that value. A claim whose attribute is 'as reported by document_2' is judged on whether document_1 states "
 "the same value: Contradiction if document_1 states or implies a different value. For Contradiction fill primary_value with what the passages state, "
 "written as the stated figures and, if a sum is involved, the arithmetic (e.g. \"106 + 163 = 269\"). Judge only against these passages; do not use "
 "outside knowledge. Quote the supporting or contradicting text verbatim in evidence_quote (at most 25 words) or \"\" for Neutral.\n"
 "Return only JSON: {{\"judgments\":[{{\"id\":\"c1\",\"label\":\"Entailment|Contradiction|Neutral\",\"primary_value\":\"\",\"evidence_quote\":\"\",\"reason\":\"\"}}]}}")
PATCH_PROMPT = ("You produce minimal patches to a draft report after its claims were verified against the primary source.\n" + ROLE_TEXT + "\n"
 "Draft report:\n<<<\n{draft}\n>>>\n\nVerification findings (JSON; only claims that need action; each has sentence_spans): {findings}\n\n"
 "Produce one patch per sentence_span (never two patches for the same span). old_str is always the span copied verbatim. "
 "For label \"Contradiction\": if the span asserts the value as the paper's fact, action \"replace\": new_str = the same sentence (or table row) restated "
 "with primary_value and the citation document_1.txt, optionally keeping one short clause that document_2.txt reports a different value; if the span only "
 "reports what document_2.txt says, action \"annotate\": new_str = old_str + \" [document_1.txt states: <primary_value>]\". "
 "For label \"Neutral\": action \"mark_unverified\": new_str = old_str with \" [not verified against the primary source]\" inserted before its final "
 "punctuation. For label \"Entailment_reattribute\": action \"reattribute\": new_str = old_str with its document_2.txt citation changed to document_1.txt "
 "(same citation style), value and wording unchanged. Change nothing else; do not add information.\n"
 "Return only JSON: {{\"patches\":[{{\"claim_id\":\"c1\",\"action\":\"replace|annotate|mark_unverified|reattribute\",\"old_str\":\"\",\"new_str\":\"\"}}]}}")
FULL_PROMPT = ("You verify a draft report against the full text of the primary source and return minimal patches.\n" + ROLE_TEXT + "\n"
 "Question the report answers: {q}\n\nFull text of document_1.txt:\n<<<\n{paper}\n>>>\n\nDraft report:\n<<<\n{draft}\n>>>\n\n"
 "Check every numeric or relational claim the draft makes about the paper's content, in every sentence and table row where it appears. old_str is always "
 "the sentence or table row copied verbatim (it must occur exactly once in the draft); produce at most one patch per sentence. "
 "Where the draft asserts a value that document_1.txt contradicts (directly, or by a transparent combination of its stated figures), action \"replace\": "
 "new_str = the sentence restated with document_1.txt's value and citation, optionally keeping one short clause that document_2.txt reports a different "
 "value. If the sentence only reports what document_2.txt says, action \"annotate\": new_str = old_str + \" [document_1.txt states: <value>]\". "
 "Where the draft asserts a value that document_1.txt neither states nor allows by transparent combination of its figures, action \"mark_unverified\": "
 "new_str = old_str with \" [not verified against the primary source]\" inserted before the final punctuation. Where a value is supported by document_1.txt "
 "but the sentence cites only document_2.txt, action \"reattribute\": new_str = old_str with the citation changed to document_1.txt, nothing else. "
 + META_RULE + " Leave every other sentence unchanged; do not add information; do not use outside knowledge; do not emit patches whose new_str equals old_str.\n"
 "Return only JSON: {{\"patches\":[{{\"action\":\"replace|annotate|mark_unverified|reattribute\",\"old_str\":\"\",\"new_str\":\"\",\"reason\":\"\"}}]}}")

# ---------------- provider call with contract ----------------
def api_call(prompt, cfg, guard, tag, log_path, json_mode):
    est_in = len(prompt) // 3; mt = cfg["max_tokens"]; est_cost = max(0.005, est_in * IN_RATE + mt * OUT_RATE)   # floor: the guard's spike rule compares the line's max call to the reservation
    ok, why = guard.preflight(est_cost, mt, est_in)
    if not ok: raise RuntimeError("BUDGET STOP " + why)
    body = {"model": MODEL, "messages": [{"role": "user", "content": prompt}], "max_tokens": mt}
    if cfg.get("thinking") == "disabled": body["thinking"] = {"type": "disabled"}; body["temperature"] = cfg.get("temperature", 0.0)
    elif cfg.get("reasoning_effort"): body["thinking"] = {"type": "enabled", "reasoning_effort": cfg["reasoning_effort"]}
    if json_mode and cfg.get("json_mode", True): body["response_format"] = {"type": "json_object"}
    req = urllib.request.Request("https://api.deepseek.com/chat/completions", data=json.dumps(body).encode("utf-8"),
                                 headers={"Content-Type": "application/json", "Authorization": "Bearer " + key()})
    t0 = time.time()
    try: resp = json.loads(urllib.request.urlopen(req, timeout=900).read().decode("utf-8")); http = 200
    except urllib.error.HTTPError as e:
        resp = {"error": e.read().decode("utf-8", "replace")[:500]}; http = e.code
    u = resp.get("usage") or {}; pt, ct = int(u.get("prompt_tokens", 0)), int(u.get("completion_tokens", 0)); cost = pt * IN_RATE + ct * OUT_RATE
    guard.record(cost, pt, ct, data={"stage": "p1verify", "tag": tag, "cfg": {k: cfg.get(k) for k in ("thinking", "reasoning_effort", "max_tokens")}}, est_cost=est_cost, est_out=mt, status="ok" if http == 200 else "error")
    ch0 = (resp.get("choices") or [{}])[0]; msg = ch0.get("message") or {}; content = msg.get("content") or ""; fin = ch0.get("finish_reason")
    parsed, perr = None, None
    if json_mode:
        try: parsed = json.loads(content) if content.strip() else None
        except Exception as e: perr = f"{type(e).__name__}: {e}"
    status = "VALID" if (http == 200 and fin == "stop" and content.strip() and (parsed is not None or not json_mode)) else "INVALID_OR_INCOMPLETE"
    rec = {"tag": tag, "http": http, "finish_reason": fin, "prompt_tokens": pt, "completion_tokens": ct, "reasoning_tokens": (u.get("completion_tokens_details") or {}).get("reasoning_tokens"),
           "cost_usd": round(cost, 6), "elapsed_s": round(time.time() - t0, 1), "content_chars": len(content), "parse_error": perr, "status": status, "cfg": body.get("thinking"), "max_tokens": mt}
    pathlib.Path(log_path).write_text(json.dumps({"prompt": prompt, "response": resp, "record": rec}, ensure_ascii=False, indent=1), encoding="utf-8")
    return content, parsed, rec

# ---------------- helpers ----------------
def doc1_blocks(ctx):
    out = []
    for seg in re.split(r"(?=Source: document_[12]\.txt)", ctx):
        m = re.match(r"Source: (document_[12]\.txt)\nTitle: \nContent: (.*)", seg, re.S)
        if m and m.group(1) == "document_1.txt": out.append(m.group(2).strip())
    return out
def lev(a, b):
    prev = list(range(len(b) + 1))
    for i, ca in enumerate(a, 1):
        cur = [i]
        for j, cb in enumerate(b, 1): cur.append(min(prev[j] + 1, cur[j - 1] + 1, prev[j - 1] + (ca != cb)))
        prev = cur
    return prev[-1]
def locate(text, old):
    """exact unique match, else whitespace-collapsed unique match; returns (start, end) or (None, reason)"""
    c = text.count(old)
    if c == 1: i = text.index(old); return (i, i + len(old))
    if c > 1: return (None, "not_unique")
    pat = r"\s+".join(re.escape(w) for w in old.split()); ms = list(re.finditer(pat, text)) if old.split() else []
    if len(ms) == 1: return (ms[0].start(), ms[0].end())
    return (None, "not_found" if not ms else "not_unique")
def apply_patches(draft, patches, gate):
    text, applied, rejected, seen = draft, [], [], set()
    for p in patches:
        o, n, act = (p.get("old_str") or "").strip(), (p.get("new_str") or "").strip(), p.get("action")
        if not o or not n: rejected.append({**p, "why": "empty"}); continue
        if o in seen: rejected.append({**p, "why": "duplicate_span"}); continue
        if o == n: rejected.append({**p, "why": "no_change"}); continue
        pos = locate(text, o)
        if pos[0] is None: rejected.append({**p, "why": pos[1]}); continue
        a, b = pos; actual_old = text[a:b]
        if act == "replace" and lev(actual_old, n) / max(1, len(actual_old), len(n)) > gate: rejected.append({**p, "why": f"edit_ratio>{gate}"}); continue   # normalized by the longer string
        if act in ("annotate", "mark_unverified", "reattribute") and lev(actual_old, n) > max(80, 0.5 * len(actual_old)): rejected.append({**p, "why": "annotation_too_large"}); continue
        text = text[:a] + n + text[b:]; seen.add(o); applied.append({**p, "matched": "exact" if actual_old == o else "ws_normalized"})
    return text, applied, rejected
def gold_guard(prompt, task):
    pe = json.loads((SB / "tasks" / task / "private_eval.json").read_text(encoding="utf-8"))
    if pe.get("correct_answer") and pe["correct_answer"] in prompt: raise RuntimeError("GOLD LEAK GUARD: private_eval text found in prompt")
    if "private_eval" in prompt: raise RuntimeError("GOLD LEAK GUARD: private_eval reference in prompt")
def snapshot(name):
    cell, dfile = SNAPS[name]; task, cond = cell.split("_")[0], cell.split("_")[1]
    cdir = S4 / "runs_s4" / cell; ctx = (cdir / "context.txt").read_text(encoding="utf-8"); draft = (cdir / dfile).read_text(encoding="utf-8")
    q = json.loads((SB / "tasks" / task / "private_eval.json").read_text(encoding="utf-8"))["question"]
    paper = (SB / "tasks" / task / "E_fulltext.txt").read_text(encoding="utf-8")
    return {"name": name, "cell": cell, "task": task, "cond": cond, "question": q, "draft": draft, "ctx": ctx, "doc1_blocks": doc1_blocks(ctx), "paper": paper}
class Doc1Index:
    """struct-style index over document_1 only (section-aware chunks; cosine top-k UNION BM25 top-k); dedup against seen blocks."""
    def __init__(self, paper, k):
        import numpy as np
        from langchain_huggingface import HuggingFaceEmbeddings
        self.k = k; self.ch = section_chunks(paper); self.emb = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
        E = np.array(self.emb.embed_documents(self.ch)); self.E = E / np.linalg.norm(E, axis=1, keepdims=True); self.bm = BM25(self.ch); self.np = np
    def query(self, q, seen):
        qv = self.np.array(self.emb.embed_query(q)); qv /= self.np.linalg.norm(qv); cos = self.E @ qv; bms = self.bm.score(q)
        tc = sorted(range(len(self.ch)), key=lambda i: -cos[i])[: self.k]; tb = sorted(range(len(self.ch)), key=lambda i: -bms[i])[: self.k]
        sel = sorted(set(tc) | set(tb)); out = []
        for i in sel:
            if self.ch[i].strip() in seen: continue
            seen.add(self.ch[i].strip()); out.append(self.ch[i])
        return out, {"cos_top": tc[:5], "bm25_top": tb[:5]}
def units_of(text):
    """sentences and table rows of the draft (patch units)"""
    out = []
    for line in text.replace("\r", "").split("\n"):
        if line.strip().startswith("|"): out.append(line.strip()); continue
        out.extend(u.strip() for u in re.split(r"(?<=[.!?])\s+", line) if u.strip())
    return out
def expand_spans(draft, claim, spans, cap=6):
    """Deterministic: add every sentence/table row of the draft that states the contradicted value together with a subject keyword.
    No gold involved: value and subject come from the extracted claim itself."""
    vals = re.findall(r"\d[\d,\.]*", str(claim.get("value") or "")); vals = [v for v in vals if len(v) >= 2]
    keys = [w.lower() for w in re.findall(r"[A-Za-z][A-Za-z\-]{3,}", str(claim.get("subject") or "")) if w.lower() not in ("data", "dataset", "datasets", "number", "speech", "recordings", "total", "study", "paper")]
    if not vals or not keys: return spans
    have = set(x.strip() for x in spans); out = list(spans)
    for u in units_of(draft):
        if len(out) >= cap: break
        if u in have or len(u) > 700: continue
        if any(re.search(r"\b" + re.escape(v) + r"\b", u) for v in vals) and any(k in u.lower() for k in keys): out.append(u); have.add(u)
    return out
def claim_query(c): return re.sub(r"\s+", " ", " ".join(str(c.get(k) or "") for k in ("subject", "attribute", "condition"))).strip()
def spans_of(c):
    s = c.get("sentence_spans"); s = s if isinstance(s, list) else ([c.get("sentence_span")] if c.get("sentence_span") else [])
    return [x for x in s if isinstance(x, str) and x.strip()]

# ---------------- arms ----------------
def run_vref(s, cfg, guard, odir, index):
    rec = {"arm": "V-ref", "calls": [], "stages": {}}
    p = EXTRACT_PROMPT.format(q=s["question"], draft=s["draft"], max_claims=cfg["max_claims"], max_spans=cfg["max_spans"]); gold_guard(p, s["task"])
    _, js, r = api_call(p, cfg, guard, f"{s['name']}:extract", odir / "extract.json", True); rec["calls"].append(r)
    claims = (js or {}).get("claims") if isinstance(js, dict) else None
    if r["status"] != "VALID" or not isinstance(claims, list) or not claims: rec["stages"]["extract"] = "INVALID_OR_INCOMPLETE"; rec["final_status"] = "UNVERIFIED_OUTPUT"; rec["final_text"] = s["draft"]; return rec
    claims = [c for c in claims if isinstance(c, dict) and c.get("id")][: cfg["max_claims"]]; rec["stages"]["extract"] = f"VALID({len(claims)} claims, {sum(len(spans_of(c)) for c in claims)} spans)"; rec["claims"] = claims
    slim = [{k: c.get(k) for k in ("id", "subject", "attribute", "value", "unit_or_denominator", "condition", "cited_source")} for c in claims]
    p = JUDGE_PROMPT.format(claims=json.dumps(slim, ensure_ascii=False), passages="\n\n".join(s["doc1_blocks"]) or "(none)"); gold_guard(p, s["task"])
    _, js, r = api_call(p, cfg, guard, f"{s['name']}:judge_window", odir / "judge_window.json", True); rec["calls"].append(r)
    jw = {j.get("id"): j for j in ((js or {}).get("judgments") or []) if isinstance(j, dict)} if isinstance(js, dict) else {}
    if r["status"] != "VALID" or not jw: rec["stages"]["judge_window"] = "INVALID_OR_INCOMPLETE"; rec["final_status"] = "UNVERIFIED_OUTPUT"; rec["final_text"] = s["draft"]; return rec
    rec["stages"]["judge_window"] = "VALID"; rec["judge_window"] = jw
    neutral = [c for c in claims if (jw.get(c["id"]) or {}).get("label") == "Neutral"][: cfg["max_neutral_retrieval"]]
    rec["retrieval"] = []; jr = {}
    if neutral:
        seen = set(b.strip() for b in s["doc1_blocks"]); added = []
        for c in neutral:
            q = claim_query(c); chunks, ranks = index.query(q, seen); added.extend(chunks)
            rec["retrieval"].append({"id": c["id"], "query": q, "n_new_chunks": len(chunks), "ranks": ranks})
        rec["retrieval_added_chars"] = sum(len(a) for a in added)
        if added:
            slim_n = [x for x in slim if x["id"] in set(c["id"] for c in neutral)]
            p = JUDGE_PROMPT.format(claims=json.dumps(slim_n, ensure_ascii=False), passages="\n\n".join(s["doc1_blocks"] + added)); gold_guard(p, s["task"])   # window + retrieved
            _, js, r = api_call(p, cfg, guard, f"{s['name']}:judge_retrieved", odir / "judge_retrieved.json", True); rec["calls"].append(r)
            jr = {j.get("id"): j for j in ((js or {}).get("judgments") or []) if isinstance(j, dict)} if isinstance(js, dict) else {}
            if r["status"] != "VALID" or not jr: rec["stages"]["judge_retrieved"] = "INVALID_OR_INCOMPLETE"; rec["final_status"] = "UNVERIFIED_OUTPUT"; rec["final_text"] = s["draft"]; return rec
            rec["stages"]["judge_retrieved"] = "VALID"; rec["judge_retrieved"] = jr
        else: rec["stages"]["judge_retrieved"] = "SKIPPED(no new chunks)"
    else: rec["stages"]["judge_retrieved"] = "SKIPPED(no neutral)"
    final = {}; checked = set(c["id"] for c in neutral)
    for c in claims:
        j = jr.get(c["id"]) or jw.get(c["id"]) or {}; lab = j.get("label"); src = "retrieved" if c["id"] in jr else "window"
        if lab == "Neutral" and c["id"] not in checked: lab = "UNCHECKED_CAP"
        if lab == "Entailment" and src == "retrieved" and (c.get("cited_source") == "document_2.txt"): lab = "Entailment_reattribute"
        final[c["id"]] = {**j, "label": lab, "source": src}
    rec["final_labels"] = final; rec["n_unchecked_cap"] = sum(1 for v in final.values() if v["label"] == "UNCHECKED_CAP")
    findings = [{**c, "sentence_spans": (expand_spans(s["draft"], c, spans_of(c)) if final[c["id"]]["label"] == "Contradiction" else spans_of(c)),
                 "label": final[c["id"]]["label"], "primary_value": final[c["id"]].get("primary_value"), "evidence_quote": final[c["id"]].get("evidence_quote")}
                for c in claims if final[c["id"]]["label"] in ("Contradiction", "Neutral", "Entailment_reattribute")]
    rec["spans_expanded"] = sum(len(f["sentence_spans"]) - len(spans_of(c)) for f, c in zip(findings, [c for c in claims if final[c["id"]]["label"] in ("Contradiction", "Neutral", "Entailment_reattribute")]))
    for f in findings: f.pop("sentence_span", None)
    if not findings: rec["stages"]["patch"] = "VALID_NO_GAP"; rec["patches_applied"] = []; rec["patches_rejected"] = []; rec["final_status"] = "VALID_NO_GAP"; rec["final_text"] = s["draft"]; return rec
    p = PATCH_PROMPT.format(draft=s["draft"], findings=json.dumps(findings, ensure_ascii=False)); gold_guard(p, s["task"])
    _, js, r = api_call(p, cfg, guard, f"{s['name']}:patch", odir / "patch.json", True); rec["calls"].append(r)
    patches = (js or {}).get("patches") if isinstance(js, dict) else None
    if r["status"] != "VALID" or not isinstance(patches, list): rec["stages"]["patch"] = "INVALID_OR_INCOMPLETE"; rec["final_status"] = "UNVERIFIED_OUTPUT"; rec["final_text"] = s["draft"]; return rec
    text, ap, rj = apply_patches(s["draft"], [x for x in patches if isinstance(x, dict)], cfg["edit_ratio_gate"]); rec["stages"]["patch"] = f"VALID({len(ap)} applied, {len(rj)} rejected)"
    rec["patches_applied"], rec["patches_rejected"], rec["final_status"], rec["final_text"] = ap, rj, ("VALID_GAP" if ap else "VALID_GAP_NO_PATCH_APPLIED"), text
    return rec
def run_vfull(s, cfg, guard, odir):
    rec = {"arm": "V-full", "calls": [], "stages": {}}
    p = FULL_PROMPT.format(q=s["question"], paper=s["paper"], draft=s["draft"]); gold_guard(p, s["task"])
    _, js, r = api_call(p, cfg, guard, f"{s['name']}:full", odir / "full.json", True); rec["calls"].append(r)
    patches = (js or {}).get("patches") if isinstance(js, dict) else None
    if r["status"] != "VALID" or not isinstance(patches, list): rec["stages"]["full"] = "INVALID_OR_INCOMPLETE"; rec["final_status"] = "UNVERIFIED_OUTPUT"; rec["final_text"] = s["draft"]; return rec
    text, ap, rj = apply_patches(s["draft"], [x for x in patches if isinstance(x, dict)], cfg["edit_ratio_gate"]); rec["stages"]["full"] = f"VALID({len(ap)} applied, {len(rj)} rejected)"
    rec["patches_applied"], rec["patches_rejected"], rec["final_text"] = ap, rj, text
    rec["final_status"] = "VALID_NO_GAP" if not patches else ("VALID_GAP" if ap else "VALID_GAP_NO_PATCH_APPLIED"); return rec
def run_vrewrite(s, cfg, guard, odir):
    rec = {"arm": "V-rewrite", "calls": [], "stages": {}}
    p = VERIFY_PROMPT.format(q=s["question"], paper=s["paper"], draft=s["draft"]); gold_guard(p, s["task"])
    content, _, r = api_call(p, cfg, guard, f"{s['name']}:rewrite", odir / "rewrite.json", False); rec["calls"].append(r)
    if r["status"] != "VALID": rec["stages"]["rewrite"] = "INVALID_OR_INCOMPLETE"; rec["final_status"] = "UNVERIFIED_OUTPUT"; rec["final_text"] = s["draft"]; return rec
    rec["stages"]["rewrite"] = "VALID"; rec["final_status"] = "VALID_REWRITE"; rec["final_text"] = content; return rec

# ---------------- ledger / main ----------------
def stage_cap():
    from ledger_guard import LEDGER
    bpath = RUNS / "ledger_baseline.json"
    if bpath.exists(): base = json.loads(bpath.read_text(encoding="utf-8"))["line_cost_at_stage_start"]
    else:
        c = sqlite3.connect(str(LEDGER), timeout=30)
        base = c.execute("select coalesce(sum(cost),0) from calls where exp_key like 'evidence-package-pilot%' and exp_key != ?", (EXP_KEY,)).fetchone()[0]; c.close()
        bpath.write_text(json.dumps({"line_cost_at_stage_start": base, "created": time.strftime("%Y-%m-%dT%H:%M:%S"), "stage_cap_usd": STAGE_CAP}, indent=2), encoding="utf-8")
    return round(min(LINE_CAP, base + STAGE_CAP), 4)
def probe(guard):
    out = {}
    for name, cfg in (("disabled+json", {"thinking": "disabled", "temperature": 0.0, "max_tokens": 64, "json_mode": True}),
                      ("effort_low", {"thinking": None, "reasoning_effort": "low", "temperature": 0.0, "max_tokens": 2048, "json_mode": False})):
        c, js, r = api_call('Reply with JSON {"ok": true}.', cfg, guard, f"probe:{name}", RUNS / f"probe_{name}.json", cfg["json_mode"])
        out[name] = {"http": r["http"], "finish": r["finish_reason"], "content": c[:60], "reasoning_tokens": r["reasoning_tokens"], "completion_tokens": r["completion_tokens"], "status": r["status"]}
        print(f"PROBE {name}: {out[name]}", flush=True)
    (RUNS / "probe_summary.json").write_text(json.dumps(out, indent=2), encoding="utf-8")
def main(a):
    from ledger_guard import BudgetGuard
    RUNS.mkdir(exist_ok=True); DOCP.mkdir(exist_ok=True)
    guard = BudgetGuard(EXP_KEY, exp_prefix=PREFIX, call_cap=CALL_CAP, in_tok_cap=20_000_000, out_tok_cap=5_000_000); guard.cost_cap = stage_cap()
    cur, calls, *_ = guard._totals()
    bl = json.loads((RUNS / "ledger_baseline.json").read_text(encoding="utf-8"))
    if "line_calls_at_stage_start" not in bl: bl["line_calls_at_stage_start"] = calls; (RUNS / "ledger_baseline.json").write_text(json.dumps(bl, indent=2), encoding="utf-8")
    guard.call_cap = bl["line_calls_at_stage_start"] + CALL_CAP   # guard counts calls line-wide; stage cap = +120 over the count at stage start
    print(f"COST ACCOUNTING: pilot* cum=${cur:.4f} ({calls} calls); stage cap=${guard.cost_cap}; call_cap={guard.call_cap} (stage +{CALL_CAP})", flush=True)
    if a.probe: probe(guard); return
    cfg = dict(DEFAULT_CFG)
    if a.config: cfg.update(json.loads(pathlib.Path(a.config).read_text(encoding="utf-8")))
    rdir = RUNS / a.round; rdir.mkdir(exist_ok=True); (rdir / "config.json").write_text(json.dumps(cfg, indent=2), encoding="utf-8")
    arms = a.arms.split(","); snaps = list(SNAPS) if a.snaps == "all" else a.snaps.split(",")
    index_cache = {}
    for sn in snaps:
        s = snapshot(sn)
        if s["task"] not in index_cache and "V-ref" in arms: index_cache[s["task"]] = Doc1Index(s["paper"], cfg["retrieval_k"])
        for arm in arms:
            odir = rdir / sn / arm; odir.mkdir(parents=True, exist_ok=True)
            if (odir / "result.json").exists() and not a.force: print(f"{sn}/{arm}: skip (exists)", flush=True); continue
            try:
                rec = run_vref(s, cfg, guard, odir, index_cache[s["task"]]) if arm == "V-ref" else (run_vfull(s, cfg, guard, odir) if arm == "V-full" else run_vrewrite(s, cfg, guard, odir))
            except RuntimeError as e:
                print(f"{sn}/{arm}: STOP {e}", flush=True); return
            rec.update({"snapshot": sn, "cell": s["cell"], "task": s["task"], "cond": s["cond"], "round": a.round, "config": cfg,
                        "cost_usd": round(sum(c["cost_usd"] for c in rec["calls"]), 6), "prompt_tokens": sum(c["prompt_tokens"] for c in rec["calls"]),
                        "completion_tokens": sum(c["completion_tokens"] for c in rec["calls"]), "n_calls": len(rec["calls"]), "draft_chars": len(s["draft"]), "final_chars": len(rec.get("final_text") or "")})
            (odir / "final.md").write_text(rec.get("final_text") or "", encoding="utf-8"); rec.pop("final_text", None)
            (odir / "result.json").write_text(json.dumps(rec, ensure_ascii=False, indent=1), encoding="utf-8")
            print(f"{sn}/{arm}: {rec['final_status']} stages={rec['stages']} calls={rec['n_calls']} ptok={rec['prompt_tokens']} ${rec['cost_usd']:.4f} "
                  f"applied={len(rec.get('patches_applied') or [])} rejected={[x.get('why') for x in (rec.get('patches_rejected') or [])]}", flush=True)
    cur, calls, *_ = guard._totals(); print(f"P1 ROUND {a.round} DONE: pilot* cum=${cur:.4f} ({calls} calls)", flush=True)

if __name__ == "__main__":
    ap = argparse.ArgumentParser(); ap.add_argument("--probe", action="store_true"); ap.add_argument("--round", default="dev1"); ap.add_argument("--arms", default="V-ref,V-full")
    ap.add_argument("--snaps", default="all"); ap.add_argument("--config", default=""); ap.add_argument("--force", action="store_true")
    os.environ.setdefault("TOKENIZERS_PARALLELISM", "false"); main(ap.parse_args())
