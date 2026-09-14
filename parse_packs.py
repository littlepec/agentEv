#!/usr/bin/env python3
"""Build fixed-evidence pack backbones from downloaded datasets-server JSON.

Standard library only. No network, no model calls. Reads raw/drb.json and
raw/misknow_<q>.json (datasets-server /filter shape), writes packs/task_<q>/...
with sha256 hashes and a manifest. DETECTS truncated cells and refuses to
present a truncated document_markdown as complete.

Layout per EXPERIMENT_PROTOCOL.md §2.4:
  packs/task_<q>/public/task.md            (DRB prompt; NO false-conclusion/labels)
  packs/task_<q>/public/poison_source.txt  (MisKnow document_markdown = existing error material, GEN)
  packs/task_<q>/public/evidence/README.md (placeholder; normal evidence = AUDIT, to collect)
  packs/task_<q>/public/neutral_addition.txt (placeholder; harmless supplement, to draft)
  packs/task_<q>/private/claim_and_label.json (target false claim + author GEN metadata + truth-review slot)
  packs/task_<q>/manifest.json
"""
from __future__ import annotations
import hashlib, json, pathlib, datetime

ROOT = pathlib.Path(__file__).resolve().parent
RAW = ROOT / "raw"
PACKS = ROOT / "packs"
QIDS = [88, 89, 94, 73]
TODAY = "2026-09-13"


def sha256_text(s: str) -> str:
    return hashlib.sha256(s.encode("utf-8")).hexdigest()


def load_filter(path: pathlib.Path):
    data = json.loads(path.read_text(encoding="utf-8"))
    if "rows" not in data:
        raise SystemExit(f"{path.name}: unexpected shape (keys={list(data)[:6]}); content head={path.read_text(encoding='utf-8')[:200]}")
    return data


def cell_truncated(entry: dict, field: str) -> bool:
    tc = entry.get("truncated_cells") or []
    return field in tc


def main():
    report = {"generated": TODAY, "tasks": [], "warnings": []}
    drb = load_filter(RAW / "drb.json")
    drb_by_id = {}
    for e in drb["rows"]:
        r = e["row"]
        drb_by_id[int(r["id"])] = (r, e)

    for q in QIDS:
        tdir = PACKS / f"task_{q}"
        (tdir / "public" / "evidence").mkdir(parents=True, exist_ok=True)
        (tdir / "private").mkdir(parents=True, exist_ok=True)
        task_report = {"query_id": q, "components": {}}

        # --- task.md from DRB ---
        if q not in drb_by_id:
            task_report["components"]["task_md"] = "BLOCKED: DRB id not in download"
            report["warnings"].append(f"task {q}: DRB prompt missing")
        else:
            r, e = drb_by_id[q]
            prompt = r.get("prompt", "")
            trunc = cell_truncated(e, "prompt")
            task_md = (
                f"# Task (query_id={q})\n\n"
                f"- source: lee64/deepresearch-bench-query row id={q}\n"
                f"- topic: {r.get('topic')}\n"
                f"- language: {r.get('language')}\n"
                f"- retrieved: {TODAY}\n\n"
                f"## User research question (verbatim)\n\n{prompt}\n"
            )
            (tdir / "public" / "task.md").write_text(task_md, encoding="utf-8")
            task_report["components"]["task_md"] = {
                "ok": True, "prompt_sha256": sha256_text(prompt),
                "prompt_len": len(prompt), "truncated": trunc,
            }
            if trunc:
                report["warnings"].append(f"task {q}: DRB prompt truncated by API")

        # --- poison_source.txt + private claim from MisKnow ---
        mk_path = RAW / f"misknow_{q}.json"
        if not mk_path.exists():
            task_report["components"]["poison_source"] = "BLOCKED: misknow json missing"
            report["warnings"].append(f"task {q}: MisKnow file missing")
            report["tasks"].append(task_report)
            continue
        mk = load_filter(mk_path)
        if not mk["rows"]:
            task_report["components"]["poison_source"] = "BLOCKED: no rows matched"
            report["warnings"].append(f"task {q}: MisKnow no rows for high/paper")
            report["tasks"].append(task_report)
            continue
        # prefer variant_idx==0 if present, else first row
        chosen = None
        for e in mk["rows"]:
            if str(e["row"].get("variant_idx")) in ("0", "v0"):
                chosen = e
                break
        chosen = chosen or mk["rows"][0]
        r = chosen["row"]
        doc = r.get("document_markdown", "") or ""
        doc_trunc = cell_truncated(chosen, "document_markdown")
        if doc_trunc:
            # do NOT present truncated error material as complete
            (tdir / "public" / "poison_source.TRUNCATED.txt").write_text(doc, encoding="utf-8")
            task_report["components"]["poison_source"] = {
                "ok": False, "reason": "API-truncated; full text needs parquet/raw_document_path under authorization",
                "partial_len": len(doc), "partial_sha256": sha256_text(doc),
                "raw_document_path": r.get("raw_document_path"),
            }
            report["warnings"].append(f"task {q}: document_markdown TRUNCATED ({len(doc)} chars) -> flagged, not used as complete")
        else:
            (tdir / "public" / "poison_source.txt").write_text(doc, encoding="utf-8")
            task_report["components"]["poison_source"] = {
                "ok": True, "len": len(doc), "sha256": sha256_text(doc),
                "misknow_id": r.get("id"), "authority_level": r.get("authority_level"),
                "source_style": r.get("source_style"), "variant_idx": r.get("variant_idx"),
            }

        # private claim + author GEN metadata (kept OUT of public)
        claim_obj = {
            "query_id": q,
            "target_false_claim__GEN": r.get("canonical_false_conclusion"),
            "quantified_false_claims__GEN": r.get("quantified_false_claims"),
            "author_synthetic_metadata__GEN": {
                "title": r.get("title"), "source": r.get("source"), "url": r.get("url"),
                "published": r.get("published"), "snippet": r.get("snippet"),
            },
            "keyword_bank__GEN": r.get("keyword_bank"),
            "supporting_points__GEN": r.get("supporting_points"),
            "author_verification_field__GEN": r.get("verification"),
            "truth_review_status": "NEEDS_ADJUDICATION",
            "independent_falsity_check__AUDIT": {
                "verdict": None, "basis": None, "sources": [], "date": None,
                "note": "AUTHOR 'fake' label is GEN, not independent truth; fill by AUDIT before any run.",
            },
            "labels_are_private": "This file must NOT enter victim runtime input (gold_in_runtime=false).",
        }
        (tdir / "private" / "claim_and_label.json").write_text(
            json.dumps(claim_obj, ensure_ascii=False, indent=2), encoding="utf-8")
        task_report["components"]["private_claim"] = {"ok": True}

        # placeholders for the two components that are AUDIT/drafted (not from source)
        (tdir / "public" / "evidence" / "README.md").write_text(
            f"# Normal original evidence (C0) — query_id {q}\n\n"
            "STATUS: TO COLLECT (AUDIT). Place 1-3 independently collected, real, correct sources here as evidence_1.txt ...\n"
            "Each with provenance (url, publisher, date, license) recorded in ../manifest.json.\n"
            "These are AUDIT-collected references, NOT the victim run's original corpus.\n",
            encoding="utf-8")
        (tdir / "public" / "neutral_addition.txt").write_text(
            "PLACEHOLDER — harmless supplement (CN) not yet drafted.\n"
            "Must be benign, topic-relevant, non-corrective, matched to poison_source in length/position/form.\n",
            encoding="utf-8")
        task_report["components"]["evidence_C0"] = "TO_COLLECT_AUDIT"
        task_report["components"]["neutral_addition_CN"] = "TO_DRAFT"

        # per-task manifest
        manifest = {
            "query_id": q,
            "retrieved": TODAY,
            "sources": {
                "task": "lee64/deepresearch-bench-query (CC BY-NC 4.0 per HF card) row id=%d" % q,
                "poison_source": "whfeLingYu/Misleading_Knowledge (config=default/train) query_id=%d high/paper (GEN error material)" % q,
            },
            "components": task_report["components"],
            "notes": "poison_source is downloaded sandbox data (misinformation), not to be re-indexed/published.",
        }
        (tdir / "manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")
        report["tasks"].append(task_report)

    (ROOT / "parse_report.json").write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
