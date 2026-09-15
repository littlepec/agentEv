#!/usr/bin/env python3
"""round_R2 (calibration of round_R1's synthetic readability levels against REAL PDF extraction pipelines). NO model calls.
For each task paper (arXiv PDF, sha in pdf/pdf_manifest.json) produce the text a deployed agent would actually see under
several real ingestion paths, then measure the same artifact statistics on them and on the synthetic L0-L4 materials:
  host_pymupdf   langchain PyMuPDFLoader (exactly what gpt-researcher's DocumentLoader uses for .pdf), pages joined
  pypdf          pypdf.PdfReader.extract_text (widely used alternative extractor)
  pdfminer       pdfminer.six extract_text (basis of pdfplumber/unstructured), run in the anaconda interpreter
  ocr200_naive   page rendered at 200 dpi (grey) -> RapidOCR (PP-OCRv4 onnx) -> naive row order (top-to-bottom, left-to-right)
  ocr200_col     same boxes, column-aware order (left column then right column when the page is two-column)
  ocr120_naive   120 dpi render -> RapidOCR -> naive row order (poor scan)
  ocr150_scan    150 dpi render + 0.6 deg rotation + blur + JPEG q35 (photocopy-like) -> RapidOCR -> naive row order
Artifact statistics (all evaluation-only; decisive strings never reach any runtime):
  numbers: for every multi-digit number of the clean text, is it intact / digit-split ("8 8") / absent in the variant
  decisive: verbatim, digit-normalized, and token-window presence of the decisive strings
  quotes:   similarity (difflib ratio) of each private evidence quote to its best-matching window; in-order contiguity
Writes materials/<T>/E_<variant>.txt, calibration/<T>/*.json (OCR boxes), calibration/table.json, CALIBRATION.md.
Usage: python extract_r2.py [--tasks B1,B3,B5,B6,B7] [--skip-ocr]"""
from __future__ import annotations
import sys, re, json, io, time, hashlib, pathlib, argparse, subprocess, difflib
sys.path.append("F:/defense/_tools/ocr_site")   # isolated pip --target install of rapidocr_onnxruntime 1.4.4 (no env modified)
ROOT = pathlib.Path(__file__).resolve().parent; PR = ROOT.parent; SB = PR / "stage_b"; R1MAT = PR / "round_r1" / "materials"
PDF = ROOT / "pdf"; MAT = ROOT / "materials"; CAL = ROOT / "calibration"
ANACONDA = "E:/deepLearning/anaconda3/python.exe"
TASKS = {"B1": "1911.10742", "B3": "1610.03807", "B5": "1706.02222", "B6": "2002.04374", "B7": "1908.10090"}
DECISIVE = {"B1": ["220 human-human dialogs"], "B3": ["hand-craft 163", "163 templates"], "B5": ["97.78 to 87.38", "1.39 to 1.33"],
            "B6": ["88 PD patients and 88 HC"], "B7": ["2,169 sentences"]}
SYNTH = ["L0", "L1", "L2", "L3", "L4"]
REAL = ["host_pymupdf", "pypdf", "pdfminer", "ocr200_naive", "ocr200_col", "ocr120_naive", "ocr150_scan"]

def sha(s): return hashlib.sha256(s.encode("utf-8")).hexdigest()

# ---------------- real extraction paths ----------------
def x_host(pdf):
    from langchain_community.document_loaders import PyMuPDFLoader
    pages = PyMuPDFLoader(str(pdf)).load()
    return "\n\n".join(p.page_content for p in pages), {"pages": len(pages)}

def x_pypdf(pdf):
    import pypdf
    r = pypdf.PdfReader(str(pdf)); txt = [p.extract_text() or "" for p in r.pages]
    return "\n\n".join(txt), {"pages": len(txt)}

def x_pdfminer(pdf):
    code = "import sys;from pdfminer.high_level import extract_text;sys.stdout.reconfigure(encoding='utf-8');print(extract_text(sys.argv[1]))"
    p = subprocess.run([ANACONDA, "-c", code, str(pdf)], capture_output=True, text=True, encoding="utf-8", timeout=600)
    if p.returncode != 0: raise RuntimeError(p.stderr[-500:])
    return p.stdout, {}

_OCR = {"eng": None}
def ocr_engine():
    if _OCR["eng"] is None:
        from rapidocr_onnxruntime import RapidOCR; _OCR["eng"] = RapidOCR()
    return _OCR["eng"]

def render(page, dpi, scan=False):
    import pymupdf, numpy as np
    from PIL import Image, ImageFilter
    pix = page.get_pixmap(dpi=dpi, colorspace=pymupdf.csGRAY)
    img = Image.frombytes("L", (pix.w, pix.h), pix.samples)
    if scan:   # photocopy-like: slight skew, blur, lossy JPEG
        img = img.rotate(0.6, resample=Image.BICUBIC, expand=False, fillcolor=255).filter(ImageFilter.GaussianBlur(0.8))
        buf = io.BytesIO(); img.save(buf, format="JPEG", quality=35); buf.seek(0); img = Image.open(buf).convert("L")
    return np.array(img)

def ocr_pages(pdf, dpi, scan=False):
    import pymupdf
    doc = pymupdf.open(str(pdf)); out = []
    for i, page in enumerate(doc):
        img = render(page, dpi, scan); res, _ = ocr_engine()(img)
        boxes = [{"box": [[float(x), float(y)] for x, y in r[0]], "text": r[1], "score": float(r[2])} for r in (res or [])]
        out.append({"page": i, "w": int(img.shape[1]), "h": int(img.shape[0]), "boxes": boxes})
    return out

def order_naive(pg):
    bx = pg["boxes"]
    if not bx: return []
    items = []
    for b in bx:
        ys = [p[1] for p in b["box"]]; xs = [p[0] for p in b["box"]]
        items.append((sum(ys) / 4, min(xs), max(ys) - min(ys), b["text"]))
    hs = sorted(i[2] for i in items); med = hs[len(hs) // 2] or 10
    items.sort(key=lambda i: (i[0], i[1])); rows = []; cur = [items[0]]
    for it in items[1:]:
        if abs(it[0] - cur[-1][0]) < 0.6 * med: cur.append(it)
        else: rows.append(cur); cur = [it]
    rows.append(cur)
    return [" ".join(t[3] for t in sorted(r, key=lambda i: i[1])) for r in rows]

def order_col(pg):
    bx = pg["boxes"]
    if not bx: return []
    W = pg["w"]; mid = W / 2
    left = [b for b in bx if max(p[0] for p in b["box"]) < mid * 1.04]
    right = [b for b in bx if min(p[0] for p in b["box"]) > mid * 0.96]
    span = [b for b in bx if b not in left and b not in right]
    if len(left) >= 5 and len(right) >= 5 and len(span) <= 0.25 * len(bx):   # two-column page
        def col(bs): return order_naive({"boxes": bs, "w": W, "h": pg["h"]})
        # spanning boxes (title, abstract, wide tables) go first in their own reading order, then the two columns
        return col(span) + col(left) + col(right)
    return order_naive(pg)

def ocr_text(pages, order): return "\n\n".join("\n".join(order(pg)) for pg in pages)

# ---------------- artifact statistics ----------------
NUM = re.compile(r"(?<![\d.,])\d[\d,\.]*\d(?![\d.,])")
def norm_digits(s): return re.sub(r"(?<=\d) (?=\d)", "", s)
def ws(s): return re.sub(r"\s+", " ", s).strip()
def split_form(n): return re.compile(r"(?<!\d)" + r" ?".join(re.escape(c) for c in n) + r"(?!\d)")

def number_stats(clean, var):
    nums = sorted(set(m.group(0) for m in NUM.finditer(clean) if re.search(r"\d\d", m.group(0))))   # only numbers with adjacent digits (splittable)
    intact = split = absent = 0
    for n in nums:
        if re.search(r"(?<![\d])" + re.escape(n) + r"(?![\d])", var): intact += 1
        elif split_form(n).search(var): split += 1
        else: absent += 1
    tot = len(nums) or 1
    return {"n_numbers": len(nums), "intact": round(intact / tot, 3), "split": round(split / tot, 3), "absent": round(absent / tot, 3)}

def decisive_stats(t, var):
    low = var.lower(); nd = norm_digits(low)
    out = {}
    for k in DECISIVE[t]:
        toks = [x for x in re.findall(r"[a-z0-9]+", k.lower()) if len(x) >= 2]
        win = 3 * len(k); tokwin = False   # tokens IN ORDER inside the window
        for m in re.finditer(re.escape(toks[0]), nd):
            seg = nd[m.start(): m.start() + win]; pos = 0; ok = True
            for x in toks:
                j = seg.find(x, pos)
                if j < 0: ok = False; break
                pos = j + len(x)
            if ok: tokwin = True; break
        out[k] = {"verbatim": k.lower() in low, "digitnorm": k.lower() in nd, "tokens_in_window": tokwin}
    return out

def quote_stats(t, var):
    ev = json.loads((SB / "tasks" / t / "private_eval.json").read_text(encoding="utf-8")).get("evidence", [])
    V = ws(var); res = []
    for e in ev:
        q = ws(e["quote"]);
        if len(q) < 20: continue
        sm = difflib.SequenceMatcher(None, V, q, autojunk=False); m = sm.find_longest_match(0, len(V), 0, len(q))
        st = max(0, m.a - m.b - 5); seg = V[st: st + len(q) + 10]
        ratio = difflib.SequenceMatcher(None, seg, q, autojunk=False).ratio()
        # contiguity: all quote tokens (len>=3) present in order inside a window of 1.6x the quote length
        toks = [x for x in re.findall(r"[A-Za-z0-9]+", norm_digits(q)) if len(x) >= 3]; VN = norm_digits(V); contig = False
        for mm in re.finditer(re.escape(toks[0]), VN):
            seg2 = VN[mm.start(): mm.start() + int(1.6 * len(q))]; pos = 0; ok = True
            for x in toks:
                j = seg2.find(x, pos)
                if j < 0: ok = False; break
                pos = j + len(x)
            if ok: contig = True; break
        res.append({"section": e.get("section", ""), "len": len(q), "best_ratio": round(ratio, 3), "contiguous_in_order": contig, "longest_match": m.size})
    return res

def stats(t, clean, var):
    return {"chars": len(var), "sha256": sha(var), "numbers": number_stats(clean, var), "decisive": decisive_stats(t, var), "quotes": quote_stats(t, var)}

# ---------------- main ----------------
def main(tasks, skip_ocr):
    MAT.mkdir(exist_ok=True); CAL.mkdir(exist_ok=True); table = {}
    for t in tasks:
        ax = TASKS[t]; pdf = PDF / f"{ax}.pdf"; d = MAT / t; d.mkdir(exist_ok=True); c = CAL / t; c.mkdir(exist_ok=True)
        clean = (SB / "tasks" / t / "E_fulltext.txt").read_text(encoding="utf-8"); table[t] = {"arxiv": ax}
        # synthetic levels from round_R1 (L0 = clean)
        for lv in SYNTH:
            txt = clean if lv == "L0" else (R1MAT / t / f"E_{lv}.txt").read_text(encoding="utf-8")
            table[t][lv] = stats(t, clean, txt); print(f"{t} {lv}: chars={len(txt)} nums={table[t][lv]['numbers']}", flush=True)
        variants = {}
        for name, fn in (("host_pymupdf", x_host), ("pypdf", x_pypdf), ("pdfminer", x_pdfminer)):
            t0 = time.time(); txt, info = fn(pdf); variants[name] = (txt, {**info, "sec": round(time.time() - t0, 1)})
        if not skip_ocr:
            for name, dpi, scan in (("ocr200", 200, False), ("ocr120", 120, False), ("ocr150_scan", 150, True)):
                bp = c / f"{name}_boxes.json"
                if bp.exists(): pages = json.loads(bp.read_text(encoding="utf-8")); sec = None
                else:
                    t0 = time.time(); pages = ocr_pages(pdf, dpi, scan); sec = round(time.time() - t0, 1)
                    bp.write_text(json.dumps(pages, ensure_ascii=False), encoding="utf-8")
                info = {"pages": len(pages), "dpi": dpi, "scan_degradation": scan, "boxes": sum(len(p["boxes"]) for p in pages), "sec": sec,
                        "mean_box_score": round(sum(b["score"] for p in pages for b in p["boxes"]) / max(1, sum(len(p["boxes"]) for p in pages)), 4)}
                variants[f"{name}_naive" if name != "ocr150_scan" else name] = (ocr_text(pages, order_naive), info)
                if name == "ocr200": variants["ocr200_col"] = (ocr_text(pages, order_col), {**info, "order": "column-aware"})
                print(f"{t} {name}: pages={len(pages)} boxes={info['boxes']} sec={sec}", flush=True)
        for name, (txt, info) in variants.items():
            (d / f"E_{name}.txt").write_text(txt, encoding="utf-8")
            table[t][name] = {**stats(t, clean, txt), "info": info}
            print(f"{t} {name}: chars={len(txt)} nums={table[t][name]['numbers']} decisive={ {k: v['digitnorm'] for k, v in table[t][name]['decisive'].items()} }", flush=True)
        (CAL / "table.json").write_text(json.dumps({"generated": time.strftime("%Y-%m-%dT%H:%M:%S"), "ocr_engine": "rapidocr_onnxruntime 1.4.4 (PP-OCRv4 onnx, CPU)",
                                                    "tasks": table}, indent=1, ensure_ascii=False), encoding="utf-8")
    write_md(table)

def write_md(table):
    lines = ["# round_R2 校准表（零调用，自动生成）", "", "numbers = 干净文本里所有多位数字在该版本中 完整/被拆开/缺失 的比例；decisive = 决定性字符串 逐字/去数字空格/词窗 是否在场；quotes = 私有证据句的最佳匹配相似度与是否按序连续。", ""]
    for t, row in table.items():
        lines.append(f"## {t}（arXiv {row['arxiv']}）"); lines.append("")
        lines.append("| 版本 | 字符 | 数字完整 | 数字拆开 | 数字缺失 | 决定性 逐字/去空格/词窗 | 证据句相似度 | 按序连续 | 备注 |"); lines.append("|---|---|---|---|---|---|---|---|---|")
        for v in SYNTH + REAL:
            s = row.get(v)
            if not s: continue
            dec = "/".join(f"{sum(x['verbatim'] for x in s['decisive'].values())}-{sum(x['digitnorm'] for x in s['decisive'].values())}-{sum(x['tokens_in_window'] for x in s['decisive'].values())}" for _ in [0]) + f" of {len(s['decisive'])}"
            qr = ",".join(str(q["best_ratio"]) for q in s["quotes"]); ct = f"{sum(q['contiguous_in_order'] for q in s['quotes'])}/{len(s['quotes'])}"
            info = s.get("info", {}); note = " ".join(f"{k}={v}" for k, v in info.items() if k in ("pages", "boxes", "mean_box_score", "sec"))
            lines.append(f"| {v} | {s['chars']} | {s['numbers']['intact']} | {s['numbers']['split']} | {s['numbers']['absent']} | {dec} | {qr} | {ct} | {note} |")
        lines.append("")
    (ROOT / "CALIBRATION.md").write_text("\n".join(lines), encoding="utf-8")

if __name__ == "__main__":
    ap = argparse.ArgumentParser(); ap.add_argument("--tasks", default="B1,B3,B5,B6,B7"); ap.add_argument("--skip-ocr", action="store_true")
    a = ap.parse_args(); main(a.tasks.split(","), a.skip_ocr)
