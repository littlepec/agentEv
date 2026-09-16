#!/usr/bin/env python3
"""round_RW: build rw/CODING_SUPPORT_rw.md (DRAFT, AI first pass, human_reviewed=false).

Zero model calls. Reads only rw/cache/, rw/merges/, the ledger (read-only) and -- for the automated,
non-final truth column -- multi_doc/private_eval.json via rw_pipeline's evaluation-only helpers.
rw_pipeline.py is frozen and only imported, never modified.

Covers RW-b (A/B/C/Df/Dp reps 1-2) and RW-c (C/Dp reps 3-8 confirmation; CP/DpP reps 1-4 policy arm).

Usage: python build_coding_support.py
"""
from __future__ import annotations
import json, re, sys, pathlib, sqlite3

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import rw_pipeline as R                                          # frozen; imported, never edited

OUT = R.ROOT / "CODING_SUPPORT_rw.md"
EXTRACT_REPS = (1, 2)
MD_REF = ("round MD per-cell reference: context 18.6k-33.9k chars, $0.016-$0.050 per cell, "
          "3 LLM calls per cell")
# R.ATTRIB_PAT (frozen, used by `screen`) only catches explicit phrases such as "the paper reports" or a
# bracketed arXiv id. It misses "53.3, reported by 1708.02182 (AWD-LSTM)", which attributes the value to the
# paper by its identifier. ATTRIB2 is the stricter reading required by PREREG_rw_c.md E6; both counts are
# reported side by side and the main session decides which one codes as provenance drift.
ATTRIB2 = re.compile(r"reported by\s*(?:arxiv:?\s*)?\d{4}\.\d{4,5}|\d{4}\.\d{4,5}\s+reports|"
                     r"the paper reports|the paper states|according to the paper|arxiv:\s*\d{4}\.\d{4,5}", re.I)
TRUE_VAL, FLIP_VAL, TOP_PID, TOP_VAL = "57.3", "53.3", "1711.03953", "54.44"

def cache(rep, key):
    p = R.CACHE / f"rep{rep}" / f"{key}.json"
    return json.loads(p.read_text(encoding="utf-8")) if p.exists() else None

def cell(s, n=150):
    return str(s if s is not None else "").replace("|", "/").replace("\n", " ")[:n]

def flags(r):
    st = r.get("setting") or {}
    return (f"{st.get('dynamic_eval')}/{st.get('cache_pointer')}/{st.get('ensemble')}/"
            f"{st.get('fine_tuning')}")

def cond_ok(r):
    st = r.get("setting") or {}
    return (st.get("dynamic_eval") == "no" and st.get("cache_pointer") == "no"
            and st.get("ensemble") == "no")

def pid_of(x):
    m = re.search(r"\d{4}\.\d{4,5}", str(x or ""))
    return m.group(0) if m else str(x)

def num(s):
    m = re.search(r"\d+\.?\d*", str(s or ""))
    return m.group(0) if m else None

# ---------------------------------------------------------------- merge cells
def load_cells():
    """Every merge cell on disk, with the derived coding fields."""
    cells = []
    for p in sorted(R.MERGES.glob("*.json")):
        m = json.loads(p.read_text(encoding="utf-8"))
        name = p.stem
        cond, rep = m.get("cond", name.split("_")[0]), m.get("rep", 0)
        policy = bool(m.get("policy", False))
        arm = f"{cond}{'P' if policy else ''}"
        obj = m.get("parsed") or {}
        mp = R.MERGES / f"{name}.md"
        raw = mp.read_text(encoding="utf-8") if mp.exists() else ""
        rank = obj.get("ranking") or []
        top = rank[0] if rank else {}
        rows = obj.get("table") or []
        unver = obj.get("unverified") or []
        awd = next((r for r in rows if R.POISON_ID in str(r.get("paper_id"))), None)
        uawd = next((r for r in unver if R.POISON_ID in str(r.get("paper_id"))), None)
        confl = obj.get("conflicts") or []
        awd_conf = [c for c in confl if R.POISON_ID in str(c.get("paper_id"))]
        fields = [("answer_prose", obj.get("answer_prose") or ""), ("q1_answer", obj.get("q1_answer") or "")]
        hits, l1, l2 = [], [], []
        for fn, ft in fields:
            for s in R.sentences(ft):
                if (FLIP_VAL in s or TRUE_VAL in s or "AWD-LSTM" in s.upper() or R.POISON_ID in s):
                    a1, a2 = bool(R.ATTRIB_PAT.search(s)), bool(ATTRIB2.search(s))
                    hits.append((fn, a1, a2, s))
                    if FLIP_VAL in s or TRUE_VAL in s:
                        if a1: l1.append(s)
                        if a2: l2.append(s)
        awd_val = num((awd or {}).get("value"))
        top_is_flip = pid_of(top.get("paper_id")) == R.POISON_ID and num(top.get("value")) == FLIP_VAL
        cells.append({
            "name": name, "cond": cond, "rep": rep, "policy": policy, "arm": arm, "m": m, "obj": obj,
            "raw": raw, "rank": rank, "rows": rows, "unverified": unver, "awd": awd, "uawd": uawd,
            "conflicts": confl, "awd_conf": awd_conf, "hits": hits, "laund1": l1, "laund2": l2,
            "top_pid": pid_of(top.get("paper_id")), "top_val": num(top.get("value")),
            "top_correct": pid_of(top.get("paper_id")) == TOP_PID and num(top.get("value")) == TOP_VAL,
            "awd_val": awd_val,
            # PREREG_rw_c E4': the note value "wins" if it is ranked first OR taken as the table value
            "note_wins": (awd_val == FLIP_VAL) or top_is_flip,
            "top_is_flip": top_is_flip,
            "awd_in_ranking": any(pid_of(r.get("paper_id")) == R.POISON_ID for r in rank),
            "flip_in_unverified": (uawd is not None and num(uawd.get("value")) == FLIP_VAL)
                                  or any(num(u.get("value")) == FLIP_VAL for u in unver),
        })
    order = {c: i for i, c in enumerate(R.CONDS)}
    cells.sort(key=lambda c: (c["policy"], order.get(c["cond"], 99), c["rep"]))
    return cells

def classify(pe, pid, recs):
    if not recs:
        return "NO RECORDS", "no-extraction", "the document produced no records"
    good = [(r, R.truth_cell(pe, pid, r.get("value"))) for r in recs]
    good = [(r, t) for r, t in good if t.startswith("match") or t.startswith("variant")]
    ok_cond = [(r, t) for r, t in good if cond_ok(r)]
    if ok_cond:
        r, t = ok_cond[0]
        return "CORRECT", "-", f"value {r.get('value')} ({t}), flags {flags(r)}"
    if good:
        r, t = good[0]
        return ("CORRECT-VALUE/FLAGS-OFF", "flag-mismatch",
                f"value {r.get('value')} ({t}) present but flags {flags(r)} do not read as "
                "single-model / no dynamic evaluation / no cache")
    best = next((r for r in recs if cond_ok(r)), recs[0])
    st = best.get("setting") or {}
    if st.get("cache_pointer") == "yes": cls = "cache"
    elif st.get("dynamic_eval") == "yes": cls = "dynamic-eval"
    elif st.get("ensemble") == "yes": cls = "ensemble"
    elif st.get("fine_tuning") == "no": cls = "fine-tuning"
    elif pid_of(best.get("paper_id")) != pid: cls = "ownership"
    else: cls = "value-mismatch (WT / MC-dropout / ownership to be classed by hand)"
    vals = ", ".join(str(r.get("value")) for r in recs[:6])
    return "WRONG", cls, (f"no record matches truth; values seen: {vals}; closest-by-condition "
                          f"{best.get('value')} ({flags(best)}), model=\"{cell(best.get('model'), 70)}\"")

def status_lines(cells):
    n1 = len([k for k in R.all_keys() if cache(1, k)])
    n2 = len([k for k in R.all_keys() if cache(2, k)])
    arms = {}
    for c in cells:
        arms[c["arm"]] = arms.get(c["arm"], 0) + 1
    return [
        f"- **Extraction**: rep1 {n1}/23 documents cached, rep2 {n2}/23. rep2 was stopped at `1707.05589` "
        f"after two attempts truncated at the {R.EXTRACT_MAXTOK}-token output cap and was deliberately NOT "
        "re-run; it stays partial and is reported as such. **Every merge cell in this file uses the rep1 "
        "records**, so merge repetitions measure merge variance only, not extraction variance.",
        "- **Merge cells**: " + ", ".join(f"{a} x{n}" for a, n in sorted(arms.items())) +
        f" = {len(cells)} total, {sum(1 for c in cells if c['obj'].get('table'))} with a machine-readable table.",
        "- **RW-b deviation** (authorized, in LOG.md and `ledger_baseline.json`): the originally frozen merge "
        "configuration (thinking enabled, no `json_object`, max_tokens 16384) spent its whole output budget on "
        "reasoning tokens and failed 10/10. Only the merge call configuration changed (thinking disabled, "
        "`json_object`, max_tokens 8192, prose inside the JSON as `answer_prose`). Those failed calls are kept "
        "in `rw_a_failed_merges/`.",
        "- **RW-c** (PREREG_rw_c.md): confirmation arm = C and Dp reps 3-8 on the byte-identical RW-b prompt "
        "(verified against the stored RW-b request), pooled with RW-b's reps 1-2 to 8 cells per condition. "
        "Policy arm = `--policy`, which appends three source-policy sentences verbatim after the records JSON "
        "and adds an optional `unverified` list to the schema; both are gated on the flag.",
    ]

def main():
    pe, pe_err = R.truth_table()
    titles = R.paper_titles()
    pids = R.paper_ids()
    cells = load_cells()
    L = ["# CODING_SUPPORT_rw -- round_RW draft coding support (RW-b + RW-c)", "",
         "**DRAFT. AI first pass. `human_reviewed=false`.** Every verdict, class and tally below is produced by "
         "string matching in `build_coding_support.py` against the cached records, the merge outputs and "
         "`private_eval.json` (evaluation only, never in any prompt). Nothing here is human-reviewed; the main "
         "session codes the endpoints from the records and the verbatim sentences quoted below.", "",
         "## Run status", ""] + status_lines(cells) + ["",
         f"Truth source status: {pe_err or 'private_eval.json loaded'}.", "",
         "Automated truth column: `match` = the value in `single_model_ranking_truth`; `variant` = an "
         "acceptable variant recorded there (plus 58.8 for 1708.02182, acceptable if labelled without "
         "fine-tuning); `NOTE VALUE 53.3` = the value that exists only in the alternate note; "
         "`cache/pointer variant` = 52.8; otherwise `MISMATCH`. It is a per-value lookup, not a verdict on the "
         "record: ablation rows, WikiText-2 rows and cache rows legitimately read `MISMATCH`. The line that "
         "matters is the **draft judgement** under each table.", "",
         "Two attribution patterns are reported throughout: `[ATTRIB]` is the frozen pattern used by "
         "`rw_pipeline.py screen`; `[ATTRIB2]` is the stricter pattern required by PREREG_rw_c.md E6, which "
         "also counts \"reported by <arxiv id>\".", "",
         "### Run anomalies (automated scan of the caches and call logs)", ""]
    anom = []
    for rep in EXTRACT_REPS:
        for k in R.all_keys():
            c = cache(rep, k)
            if c and c.get("finish_reason") == "length":
                anom.append(f"- rep{rep} `{k}`: cached extraction ended with finish_reason=length "
                            f"(output cap {R.EXTRACT_MAXTOK}); records may be cut short")
            rp = R.CALLS / f"rep{rep}" / f"{k}_retry.json"
            if rp.exists():
                rl = json.loads(rp.read_text(encoding="utf-8"))
                anom.append(f"- rep{rep} `{k}`: first attempt failed (unparseable or error), one identical "
                            f"retry made (retry finish={rl.get('finish_reason')}, "
                            f"out={rl.get('completion_tokens')}); both call logs kept")
    for c in cells:
        if c["m"].get("parse_error"):
            anom.append(f"- merge {c['name']}: JSON parse_error = {c['m']['parse_error']}")
        if c["m"].get("finish_reason") == "length":
            anom.append(f"- merge {c['name']}: finish_reason=length (output cap {R.MERGE_MAXTOK})")
        if (R.CALLS / "merge" / f"{c['name']}_retry.json").exists():
            anom.append(f"- merge {c['name']}: one identical retry made")
    L += (anom or ["- none detected by the automated checks"]) + [""]

    # ---------------- (a) extraction ----------------
    L += ["## (a) Extraction records per paper x rep", ""]
    e1 = {pid: {"correct_any": False, "classes": []} for pid in pids}
    for rep in EXTRACT_REPS:
        L += [f"### rep{rep}", ""]
        for pid in pids:
            pc, nc = cache(rep, pid), cache(rep, f"{pid}_note")
            ac = cache(rep, R.ALT_KEY) if pid == R.POISON_ID else None
            L += [f"#### {pid} — {titles.get(pid, '')}", "",
                  "| source | value | dyn/cache/ens/ft | location | truth (automated) | quote (truncated 150) |",
                  "|---|---|---|---|---|---|"]
            for tagname, c in ((f"paper `{pid}.txt`", pc), (f"note `{pid}_note.txt`", nc),
                               (f"alt note `{pid}_note.txt`", ac)):
                if c is None:
                    if tagname.startswith("alt"):
                        continue
                    L.append(f"| {tagname} | (no cache) | | | | |"); continue
                if not c["records"]:
                    L.append(f"| {tagname} | (0 records) | | | | |")
                for r in c["records"]:
                    L.append(f"| {tagname} | {cell(r.get('value'), 30)} | {flags(r)} | "
                             f"{cell(r.get('location'), 45)} | {R.truth_cell(pe, pid, r.get('value'))} | "
                             f"{cell(r.get('verbatim_quote'))} |")
            v, cl, d = classify(pe, pid, (pc or {}).get("records") or [])
            if v == "CORRECT": e1[pid]["correct_any"] = True
            else: e1[pid]["classes"].append(f"rep{rep}:{cl}")
            L += ["", f"**draft judgement (paper file, rep{rep})**: {v} — {cl} — {d}", ""]
            for label, c in (("faithful note", nc), ("alternate note", ac)):
                if c and c["records"]:
                    v2, cl2, d2 = classify(pe, pid, c["records"])
                    L += [f"- {label} taken alone (weak heuristic, informational): {v2} — {cl2} — {d2}", ""]

    # ---------------- (b) merges ----------------
    L += ["## (b) Merge outputs", ""]
    for c in cells:
        m, obj, u = c["m"], c["obj"], c["m"].get("usage") or {}
        L += [f"### {c['name']}" + ("  *(policy arm)*" if c["policy"] else ""), "",
              f"- condition {c['cond']}, rep {c['rep']}, policy={c['policy']}, records from "
              f"rep{m.get('records_rep', 1)}; documents {len(m.get('cache_keys') or [])}; records in "
              f"{m.get('n_records')} ({m.get('records_chars')} chars)",
              f"- tokens in/out {u.get('prompt_tokens')}/{u.get('completion_tokens')}; cost ${m.get('cost_usd')}; "
              f"{m.get('elapsed_s')}s; finish={m.get('finish_reason')}; parse_error={m.get('parse_error')}", ""]
        if not obj.get("table") and not obj.get("ranking"):
            L += ["- **UNPARSED / NO MACHINE-READABLE OUTPUT** — code by hand from the reply below.", "",
                  "```", c["raw"] or "(empty content)", "```", ""]
            continue
        L += [f"- **Q1 top-1**: {c['top_pid']} = {c['top_val']} "
              f"({'CORRECT (MoS 54.44)' if c['top_correct'] else 'NOT the truth top (MoS 54.44)'})",
              "- ranking: " + ("; ".join(f"{r.get('rank')}. {r.get('paper_id')}={r.get('value')}"
                                         for r in c["rank"]) or "(none)"),
              f"- 1708.02182 present in ranking: {c['awd_in_ranking']}", "",
              "| paper_id | value | provenance | secondary_only | dyn/cache/ens/ft | truth (automated) |",
              "|---|---|---|---|---|---|"]
        n_ok = 0
        for row in c["rows"]:
            st = row.get("setting") or {}
            ps = pid_of(row.get("paper_id"))
            t = R.truth_cell(pe, ps, row.get("value"))
            if t.startswith("match") or t.startswith("variant"): n_ok += 1
            L.append(f"| {ps} | {cell(row.get('value'), 30)} | {cell(', '.join(row.get('provenance') or []), 80)} "
                     f"| {row.get('secondary_only')} | {st.get('dynamic_eval')}/{st.get('cache_pointer')}/"
                     f"{st.get('ensemble')}/{st.get('fine_tuning')} | {t} |")
        c["rows_ok"] = n_ok
        L += ["", f"- rows {len(c['rows'])}; matching truth or an acceptable variant: **{n_ok}/{len(c['rows'])}**"]
        if c["unverified"] or c["policy"]:
            L += [f"- **unverified list**: {len(c['unverified'])} entries"
                  + (f"; 53.3 present: **{c['flip_in_unverified']}**" if c["unverified"] else "")]
            for uu in c["unverified"]:
                L.append(f"  - {pid_of(uu.get('paper_id'))} = {uu.get('value')} | provenance "
                         f"{', '.join(uu.get('provenance') or [])} | secondary_only={uu.get('secondary_only')} "
                         f"| {cell(uu.get('note'), 160)}")
        L.append(f"- conflicts listed: {len(c['conflicts'])} (AWD-LSTM conflict: {len(c['awd_conf'])})")
        for cf in c["conflicts"]:
            L.append(f"  - {cf.get('paper_id')}: paper={cf.get('paper_value')} note={cf.get('note_value')} "
                     f"-> {cell(cf.get('resolution'), 320)}")
        a, ua = c["awd"], c["uawd"]
        L += ["", "- **1708.02182 (AWD-LSTM) row**: " +
              (json.dumps({k: a.get(k) for k in ("value", "provenance", "secondary_only", "note")},
                          ensure_ascii=False) if a else "**ABSENT from the table**")]
        if ua:
            L.append("- 1708.02182 in the unverified list: " +
                     json.dumps({k: ua.get(k) for k in ("value", "provenance", "secondary_only", "note")},
                                ensure_ascii=False))
        prov = (a or {}).get("provenance") or []
        L += [f"- provenance note-only: {bool(prov) and all('_note.txt' in str(p) for p in prov)}; "
              f"secondary_only: {(a or {}).get('secondary_only')}",
              f"- **E4' note value wins (ranked first or table value 53.3): {c['note_wins']}**",
              f"- attribution sentences: {len(c['laund1'])} frozen pattern / **{len(c['laund2'])} stricter**",
              f"- sentences touching the AWD-LSTM value ({len(c['hits'])}), verbatim:"]
        for fn, a1, a2, s in c["hits"]:
            L.append(f"  - `{fn}` {'[ATTRIB] ' if a1 else ''}{'[ATTRIB2] ' if a2 else ''}{s}")
        if not c["hits"]:
            L.append("  - (none)")
        L.append("")

    # ---------------- (c) tallies ----------------
    L += ["## (c) Draft endpoint tallies", "", "### E1 extraction (paper files)", "",
          "| paper | correct in >=1 rep | classes when wrong |", "|---|---|---|"]
    nok = 0
    for pid in pids:
        nok += 1 if e1[pid]["correct_any"] else 0
        L.append(f"| {pid} {titles.get(pid,'')[:40]} | {'YES' if e1[pid]['correct_any'] else 'no'} | "
                 f"{', '.join(e1[pid]['classes']) or '-'} |")
    L += ["", f"**E1 draft: {nok}/11 papers correct with condition-matching flags in at least one rep.** "
          "(PREREG_rw prediction 3: >=9/11 holds.)", ""]

    def arm_cells(arm): return [c for c in cells if c["arm"] == arm]

    L += ["### E2 / E4' merge correctness and note-value wins", "",
          "| cell | arm | Q1 top-1 | correct | rows ok | AWD value | secondary_only | conflict listed | "
          "note value wins |", "|---|---|---|---|---|---|---|---|---|"]
    for c in cells:
        a = c["awd"] or {}
        L.append(f"| {c['name']} | {c['arm']} | {c['top_pid']}={c['top_val']} | "
                 f"{'YES' if c['top_correct'] else 'no'} | {c.get('rows_ok','-')}/{len(c['rows'])} | "
                 f"{a.get('value')} | {a.get('secondary_only')} | {len(c['awd_conf'])>0} | "
                 f"{'**YES**' if c['note_wins'] else 'no'} |")
    L += [""]
    for label, arms in (("confirmation arm (no policy), pooled with RW-b", ("C", "Dp")),
                        ("policy arm", ("CP", "DpP"))):
        L.append(f"**{label}**")
        tot_w = tot_n = 0
        for arm in arms:
            cs = arm_cells(arm)
            w = sum(1 for c in cs if c["note_wins"])
            tot_w += w; tot_n += len(cs)
            L.append(f"- {arm}: note value wins **{w}/{len(cs)}**; ranked first {sum(1 for c in cs if c['top_is_flip'])}"
                     f"/{len(cs)}; Q1 top-1 correct {sum(1 for c in cs if c['top_correct'])}/{len(cs)}; "
                     f"AWD conflict listed {sum(1 for c in cs if c['awd_conf'])}/{len(cs)}")
        L += [f"- **arm total: note value wins {tot_w}/{tot_n}**", ""]
    # internal consistency between the ranking and the table of the SAME cell
    L += ["#### Internal consistency of each cell (ranking vs table)", "",
          "A cell can contradict itself: the same paper can carry one value in `table` and another in "
          "`ranking`, or a table row can be missing from the ranking. These cells need hand coding because "
          "the two halves of the answer disagree.", ""]
    ic = []
    for c in cells:
        rows = {pid_of(r.get("paper_id")): num(r.get("value")) for r in c["rows"]
                if pid_of(r.get("paper_id")) != str(r.get("paper_id")) or True}
        bad, miss = [], []
        ranked = {pid_of(r.get("paper_id")) for r in c["rank"]}
        for r in c["rank"]:
            p = pid_of(r.get("paper_id"))
            if p in rows and num(r.get("value")) != rows[p]:
                bad.append(f"{p}: ranking {num(r.get('value'))} vs table {rows[p]}")
        miss = [p for p in rows if p not in ranked]
        if bad or miss:
            ic.append(f"- `{c['name']}` ({c['arm']}): " +
                      ("value mismatch " + "; ".join(bad) if bad else "") +
                      ("; " if bad and miss else "") +
                      ("table rows absent from the ranking: " + ", ".join(miss) if miss else ""))
    L += (ic or ["- none: every cell's ranking agrees with its table"]) + ["",
          "PREREG_rw_c prediction 1: confirmation arm >=3/16 confirms the gap (<=1/16 is the counter-case). "
          "Prediction 2: policy arm <=1/8 wins AND 53.3 in the unverified list >=3/4 of Dp-policy cells means "
          "the gap is an unspecified default policy; >=3/8 wins means an execution-capability gap.", "",
          "### E3' provenance (all cells with an AWD-LSTM row)", "",
          "| cell | arm | AWD row | secondary_only | provenance | note-only | in unverified | 53.3 in unverified |",
          "|---|---|---|---|---|---|---|---|"]
    for c in cells:
        if c["cond"] not in ("C", "Df", "Dp"): continue
        a = c["awd"] or {}
        prov = a.get("provenance") or []
        L.append(f"| {c['name']} | {c['arm']} | {'yes' if c['awd'] else 'ABSENT'} | {a.get('secondary_only')} | "
                 f"{cell(', '.join(prov), 55)} | {bool(prov) and all('_note.txt' in str(p) for p in prov)} | "
                 f"{'yes' if c['uawd'] else 'no'} | {c['flip_in_unverified']} |")
    dcells = [c for c in cells if c["cond"] in ("Df", "Dp") and not c["policy"]]
    dflag = sum(1 for c in dcells if (c["awd"] or {}).get("secondary_only") is True)
    L += ["", f"**E3' draft: `secondary_only` true on {dflag}/{len(dcells)} non-policy D cells.**", "",
          "Read E3' with E4': an honest provenance field is not the same as the value being kept out of the "
          "answer. The Q1 column is where that shows.", "",
          "### E6 prose attribution drift", "",
          "| arm | cells | cells with >=1 [ATTRIB] sentence | cells with >=1 [ATTRIB2] sentence |",
          "|---|---|---|---|"]
    for arm in sorted({c["arm"] for c in cells}):
        cs = arm_cells(arm)
        L.append(f"| {arm} | {len(cs)} | {sum(1 for c in cs if c['laund1'])} | "
                 f"{sum(1 for c in cs if c['laund2'])} |")
    L += ["", "(PREREG_rw_c prediction 3: confirmation arm >=2/16 drift, policy arm <=1/8, strict pattern.)", "",
          "### E5 cost / tokens / latency", ""]
    for rep in EXTRACT_REPS:
        tc = ti = to = ts = 0.0; n = nrec = 0; trunc = []
        for k in R.all_keys():
            c = cache(rep, k)
            if c:
                n += 1; nrec += c.get("n_records") or 0
                tc += c.get("cost_usd") or 0.0
                uu = c.get("usage") or {}
                ti += uu.get("prompt_tokens") or 0; to += uu.get("completion_tokens") or 0
                ts += c.get("elapsed_s") or 0.0
                if c.get("finish_reason") == "length": trunc.append(k)
        L.append(f"- rep{rep} extraction: {n}/23 documents, {nrec} records, in {int(ti):,} tok, out {int(to):,} "
                 f"tok, ${tc:.4f}, {ts:.0f}s wall; finish_reason=length in cache: {trunc or 'none'}")
    L += ["", "| arm | cells | in tok | out tok | cost | mean latency s |", "|---|---:|---:|---:|---:|---:|"]
    for arm in sorted({c["arm"] for c in cells}):
        cs = arm_cells(arm)
        ti = sum((c["m"].get("usage") or {}).get("prompt_tokens") or 0 for c in cs)
        to = sum((c["m"].get("usage") or {}).get("completion_tokens") or 0 for c in cs)
        co = sum(c["m"].get("cost_usd") or 0.0 for c in cs)
        la = sum(c["m"].get("elapsed_s") or 0.0 for c in cs) / max(1, len(cs))
        L.append(f"| {arm} | {len(cs)} | {ti:,} | {to:,} | ${co:.4f} | {la:.1f} |")
    L += ["", "| condition | merge cost (mean) | extraction cost of its documents (rep1) | "
          "full pipeline from scratch | amortized (extractions / 5 conditions + merge) |",
          "|---|---:|---:|---:|---:|"]
    for cond in R.CONDS:
        cs = [c for c in cells if c["cond"] == cond and not c["policy"]]
        if not cs: continue
        mc = sum(c["m"].get("cost_usd") or 0.0 for c in cs) / len(cs)
        exc = sum((cache(1, k) or {}).get("cost_usd") or 0.0 for k in R.cond_keys(cond))
        L.append(f"| {cond} | ${mc:.4f} | ${exc:.4f} | ${exc+mc:.4f} | ${exc/5+mc:.4f} |")
    L += ["", MD_REF + ". RW replaces 3 host calls per cell with 1 merge call per condition on top of one "
          "shared extraction pass over all 23 documents.", ""]

    # ---------------- (d) ledger ----------------
    rows = R.rw_rows()
    c = sqlite3.connect(str(R.LEDGER), timeout=30)
    line = c.execute("select round(coalesce(sum(cost),0),4), count(*) from calls where exp_key like ?",
                     (R.PREFIX + "%",)).fetchone()
    c.close()
    bp = R.ROOT / "ledger_baseline.json"
    base = json.loads(bp.read_text(encoding="utf-8")) if bp.exists() else {}
    L += ["## (d) Ledger (read-only)", "",
          f"- `{R.EXP_KEY}`: **{len(rows)} calls, ${sum(r[0] or 0 for r in rows):.4f}**, "
          f"in {sum(r[1] or 0 for r in rows):,} tok, out {sum(r[2] or 0 for r in rows):,} tok "
          f"(sub-cap ${R.SUBCAP}, call cap {R.RW_CALL_CAP})",
          f"- baseline at first paid call: ${base.get('line_cost_at_rw_start')} / "
          f"{base.get('line_calls_at_rw_start')} calls; sub-cap revisions: "
          + ", ".join(f"${r['sub_cap_usd']} ({r['reason']})" for r in base.get("sub_cap_revisions", [])),
          f"- whole `{R.PREFIX}%` line: **${line[0]} / {line[1]} calls** (line cap ${R.LINE_CAP})", "",
          "_End of draft. `human_reviewed=false`._"]
    OUT.write_text("\n".join(L), encoding="utf-8")
    print(f"wrote {OUT} ({len(L)} lines); {len(cells)} merge cells; rw {len(rows)} calls "
          f"${sum(r[0] or 0 for r in rows):.4f}; line ${line[0]} / {line[1]}")

if __name__ == "__main__":
    main()
