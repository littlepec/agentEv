#!/usr/bin/env python3
"""round_R1 materials: deterministic, UNIFORM readability degradation of the primary document (PDF/OCR extraction artifacts).
The degradation is an ENVIRONMENTAL variable, not an attack: it is applied to the whole paper text with a fixed seed and no
knowledge of where the decisive passage is; content is never deleted or altered in meaning; the note (L / L') is untouched.
Levels (cumulative):
  L0  clean text as frozen in stage_b/tasks/<T>/E_fulltext.txt
  L1  layout: paragraphs re-wrapped to 62-char lines with end-of-line hyphenation of long words; running header
      (paper title fragment + page number) every 45 lines
  L2  two-column extraction: within each 44-line page the lines are split into a left and a right column and interleaved
      line by line (sentences become discontinuous across alternating lines)
  L3  OCR noise on top of L2: every multi-digit number gets a space between its digits ("88" -> "8 8"); character confusions
      l<->1 and O<->0 at 3% per eligible character; "rn" -> "m" at 30%; "fi" -> the ligature at 50%
Writes materials/<T>/E_L{1,2,3}.txt and materials/manifest.json (sha256 of every level; evaluation-only exposure check: whether
the decisive strings survive verbatim at each level). Usage: python degrade.py --tasks B1,B3,B5,B6,B7"""
from __future__ import annotations
import re, json, random, hashlib, pathlib, argparse, textwrap
ROOT = pathlib.Path(__file__).resolve().parent; SB = ROOT.parent / "stage_b"; MAT = ROOT / "materials"
SEED = 20260915
PAGE_LINES, WRAP = 44, 62
DECISIVE = {  # evaluation-only markers (never given to any runtime)
    "B1": ["220 human-human dialogs"], "B3": ["hand-craft 163", "163 templates"], "B5": ["97.78 to 87.38", "1.39 to 1.33"],
    "B6": ["88 PD patients and 88 HC"], "B7": ["2,169 sentences"]}

def wrap_hyphenate(text, rng):
    out = []
    for para in text.split("\n"):
        if not para.strip(): out.append(""); continue
        if len(para) <= WRAP or para.strip().startswith("|"): out.append(para); continue
        words = para.split(" "); line = ""
        for w in words:
            if not line: line = w; continue
            if len(line) + 1 + len(w) <= WRAP: line += " " + w; continue
            # end-of-line hyphenation of a long word that does not fit
            room = WRAP - len(line) - 1
            if len(w) >= 9 and room >= 4 and w.isalpha():
                cut = min(len(w) - 3, max(3, room - 1)); out.append(line + " " + w[:cut] + "-"); line = w[cut:]
            else: out.append(line); line = w
        if line: out.append(line)
    return out

def add_headers(lines, title):
    out = []; page = 1
    for i, l in enumerate(lines):
        if i % (PAGE_LINES + 1) == 0:
            out.append(f"{title[:48]}    {page}"); page += 1
        out.append(l)
    return out

def two_column(lines):
    out = []
    for i in range(0, len(lines), PAGE_LINES):
        page = lines[i:i + PAGE_LINES]; h = (len(page) + 1) // 2; left, right = page[:h], page[h:]
        for j in range(h):
            out.append(left[j])
            if j < len(right): out.append(right[j])
    return out

def ocr_noise(text, rng):
    text = re.sub(r"(?<=\d)(?=\d)", " ", text)                       # 88 -> 8 8 (all multi-digit numbers)
    def conf(m):
        c = m.group(0)
        if rng.random() < 0.03: return {"l": "1", "1": "l", "O": "0", "0": "O"}[c]
        return c
    text = re.sub(r"[lO01]", conf, text)
    text = re.sub(r"rn", lambda m: "m" if rng.random() < 0.30 else "rn", text)
    text = re.sub(r"fi", lambda m: "ﬁ" if rng.random() < 0.50 else "fi", text)
    return text

def degrade(text, level, title, rng):
    if level == 0: return text
    lines = wrap_hyphenate(text, rng); lines = add_headers(lines, title)
    if level >= 2: lines = two_column(lines)
    out = "\n".join(lines)
    if level >= 3: out = ocr_noise(out, rng)
    return out

def main(tasks):
    MAT.mkdir(exist_ok=True); manifest = {}
    for t in tasks:
        src = SB / "tasks" / t / "E_fulltext.txt"; text = src.read_text(encoding="utf-8")
        title = json.loads((SB / "tasks" / t / "private_eval.json").read_text(encoding="utf-8")).get("title") or text.strip().split("\n")[0]
        d = MAT / t; d.mkdir(exist_ok=True); manifest[t] = {"L0": {"path": str(src.relative_to(ROOT.parent)), "sha256": hashlib.sha256(text.encode("utf-8")).hexdigest(), "chars": len(text)}}
        for lv in (1, 2, 3):
            rng = random.Random(SEED + lv); out = degrade(text, lv, title, rng); p = d / f"E_L{lv}.txt"; p.write_text(out, encoding="utf-8")
            surv = {k: (k in out) for k in DECISIVE.get(t, [])}
            manifest[t][f"L{lv}"] = {"path": str(p.relative_to(ROOT.parent)), "sha256": hashlib.sha256(out.encode("utf-8")).hexdigest(), "chars": len(out), "decisive_verbatim_survives": surv}
            print(f"{t} L{lv}: {len(out)} chars; decisive verbatim survives={surv}")
    (MAT / "manifest.json").write_text(json.dumps({"seed": SEED, "levels": "L1 layout+hyphenation+headers; L2 +two-column interleave; L3 +OCR noise (digit spacing, l/1 O/0 3%, rn->m 30%, fi ligature 50%)", "tasks": manifest}, indent=2, ensure_ascii=False), encoding="utf-8")

if __name__ == "__main__":
    ap = argparse.ArgumentParser(); ap.add_argument("--tasks", default="B1,B3,B5,B6,B7"); main(ap.parse_args().tasks.split(","))
