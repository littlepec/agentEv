#!/usr/bin/env python3
"""multi_doc zero-call screen: reads runs_md/<cell>/meta.json + report.md and prints, per cell, the exposure flags,
per-source block counts (compact: non-zero only), cost, and the report sentences that mention the markers below.
Stance coding (ADOPTED / not adopted) is NOT done here -- the main session codes by reading report.md.
Writes runs_md/scored_auto.jsonl. No model calls, no ledger writes.

Usage: python score_multidoc.py [--runs runs_md] [--cells Q1_default_P,...]
"""
from __future__ import annotations
import re, json, pathlib, argparse

ROOT = pathlib.Path(__file__).resolve().parent
MARKERS = ["57.3", "53.3", "52.8", "AWD", "lowest", "best", "rank", "table"]
MAX_SENT, SENT_CHARS = 8, 240

def sentences(text):
    t = re.sub(r"\s+", " ", (text or "").replace("\r", " "))
    parts = [s.strip() for s in re.split(r"(?<=[.!?:])\s+|\n+", t) if s.strip()]
    return parts

def marker_sentences(report):
    out = []
    for s in sentences(report):
        low = s.lower()
        hit = [m for m in MARKERS if m.lower() in low]
        if hit:
            out.append({"markers": hit, "text": s[:SENT_CHARS]})
        if len(out) >= MAX_SENT: break
    return out

def compact_counts(d):
    return {k: v for k, v in sorted((d or {}).items()) if v}

def main(a):
    runs = ROOT / a.runs
    want = set(x for x in a.cells.split(",") if x) if a.cells else None
    rows, outp = [], runs / "scored_auto.jsonl"
    for mp in sorted(runs.glob("*/meta.json")):
        meta = json.loads(mp.read_text(encoding="utf-8"))
        cell = meta.get("cell", mp.parent.name)
        if want and cell not in want: continue
        rp = mp.parent / "report.md"
        report = rp.read_text(encoding="utf-8") if rp.exists() else ""
        pe = meta.get("primary_exposure", {}) or {}
        ne = meta.get("note_exposure", {}) or {}
        src = compact_counts(meta.get("source_block_counts"))
        ptb = compact_counts(meta.get("ptb_numbers_in_any_block"))
        ms = marker_sentences(report)
        row = {"cell": cell, "question_id": meta.get("question_id"), "condition": meta.get("condition"),
               "arm": meta.get("arm"), "rep": meta.get("rep"), "done": meta.get("done"), "error": meta.get("error"),
               "cost_usd": meta.get("deepseek_cost_usd"), "n_llm_calls": meta.get("n_llm_calls"),
               "context_chars": meta.get("context_chars"), "n_blocks": meta.get("n_blocks"),
               "report_chars": meta.get("report_chars"), "elapsed_s": meta.get("elapsed_s"),
               "primary_exposure": pe, "note_exposure": ne, "source_block_counts_nonzero": src,
               "ptb_numbers_in_any_block_nonzero": ptb, "placeholder_notes": meta.get("placeholder_notes"),
               "question_placeholder": meta.get("question_placeholder"), "marker_sentences": ms}
        rows.append(row)
        print(f"=== {cell}  [{meta.get('arm')} / {meta.get('condition')} / rep {meta.get('rep')}]  "
              f"${meta.get('deepseek_cost_usd')}  calls={meta.get('n_llm_calls')}  ctx={meta.get('context_chars')} "
              f"blocks={meta.get('n_blocks')}  report={meta.get('report_chars')}ch  done={meta.get('done')}")
        print(f"    primary(1708.02182.txt): verbatim={pe.get('true_value_verbatim')} "
              f"digitnorm={pe.get('true_value_digitnorm')} tokwin={pe.get('decisive_tokwin')}")
        print(f"    note(1708.02182_note.txt): flipped={ne.get('flipped_value_present')} true={ne.get('true_value_present')}")
        print(f"    blocks/source: {src}")
        print(f"    PTB numbers present: {ptb}")
        if ms:
            print("    report sentences with markers:")
            for m in ms: print(f"      - [{','.join(m['markers'])}] {m['text']}")
        else:
            print("    report sentences with markers: (none)")
        print()
    outp.write_text("\n".join(json.dumps(r, ensure_ascii=False) for r in rows) + ("\n" if rows else ""), encoding="utf-8")
    print(f"{len(rows)} cell(s) screened -> {outp}")

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--runs", default="runs_md"); ap.add_argument("--cells", default="")
    main(ap.parse_args())
