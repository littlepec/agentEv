#!/usr/bin/env python3
"""Evaluation-only: print how the decisive paper sentence appears in each real extraction variant (neighbourhood of the
decisive number / phrase after whitespace normalisation), so the calibration can say whether the decisive number itself is intact,
corrupted, split, or fused with neighbouring words. NO model calls. Usage: python inspect_decisive.py [--tasks B1,B3,...]"""
from __future__ import annotations
import re, json, pathlib, argparse, difflib
ROOT = pathlib.Path(__file__).resolve().parent; MAT = ROOT / "materials"; SB = ROOT.parent / "stage_b"
DEC = {"B1": "We collected 220 human-human dialogs", "B3": "we hand-craft 163 templates", "B5": "from 97.78 to 87.38",
       "B6": "88 PD patients and 88 HC speakers from Germany", "B7": "news-test2015 test set (2,169 sentences)"}
VARS = ["host_pymupdf", "pypdf", "pdfminer", "ocr200_naive", "ocr200_col", "ocr120_naive", "ocr150_scan"]
def ws(s): return re.sub(r"\s+", " ", s).strip()
def main(tasks):
    for t in tasks:
        q = DEC[t]; print(f"##### {t}: '{q}'")
        for v in VARS:
            p = MAT / t / f"E_{v}.txt"
            if not p.exists(): print(f"  {v:14} (missing)"); continue
            V = ws(p.read_text(encoding="utf-8"))
            sm = difflib.SequenceMatcher(None, V, q, autojunk=False); m = sm.find_longest_match(0, len(V), 0, len(q))
            st = max(0, m.a - m.b - 25); seg = V[st: st + len(q) + 50]
            ratio = difflib.SequenceMatcher(None, V[max(0, m.a - m.b): max(0, m.a - m.b) + len(q)], q, autojunk=False).ratio()
            print(f"  {v:14} ratio={ratio:.2f} | {seg}")
if __name__ == "__main__":
    ap = argparse.ArgumentParser(); ap.add_argument("--tasks", default="B1,B3,B5,B6,B7"); main(ap.parse_args().tasks.split(","))
