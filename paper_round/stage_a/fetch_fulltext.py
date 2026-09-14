#!/usr/bin/env python3
"""Stage A: fetch FULL paper text (not the pre-selected answer paragraph) for calibration.
Uses ar5iv HTML via stdlib urllib + a minimal HTML->text strip. Saves snapshot + sha + a coarse
paragraph-chunk map (eval-side answer location only). No model calls, no answer pre-selection in DOC_PATH."""
from __future__ import annotations
import urllib.request, pathlib, hashlib, re, json, html
from html.parser import HTMLParser
ROOT=pathlib.Path(__file__).resolve().parent
PAPERS={"Q4":"1908.09590","Q7":"2003.07459"}   # up to 2 old tasks (CHIM, OGTD)
class Strip(HTMLParser):
    def __init__(self): super().__init__(); self.buf=[]; self.skip=0
    def handle_starttag(self,t,a):
        if t in ("script","style"): self.skip+=1
        if t in ("p","div","li","tr","h1","h2","h3","h4","td","br","section"): self.buf.append("\n")
    def handle_endtag(self,t):
        if t in ("script","style") and self.skip: self.skip-=1
    def handle_data(self,d):
        if not self.skip and d.strip(): self.buf.append(d)
def fetch(arxiv):
    url=f"https://ar5iv.labs.arxiv.org/html/{arxiv}"
    req=urllib.request.Request(url,headers={"User-Agent":"Mozilla/5.0 research"})
    raw=urllib.request.urlopen(req,timeout=120).read().decode("utf-8","replace")
    p=Strip(); p.feed(raw); txt=html.unescape(" ".join(p.buf))
    txt=re.sub(r"[ \t]+"," ",txt); txt=re.sub(r"\n\s*\n+","\n\n",txt).strip()
    return url,txt
def sha(s): return hashlib.sha256(s.encode("utf-8")).hexdigest()
def main():
    (ROOT/"papers").mkdir(parents=True,exist_ok=True); man={}
    for tid,ax in PAPERS.items():
        url,txt=fetch(ax)
        (ROOT/"papers"/f"{tid}_fulltext.txt").write_text(txt,encoding="utf-8")
        man[tid]={"arxiv":ax,"url":url,"chars":len(txt),"sha256":sha(txt)}
        print(f"{tid} {ax}: {len(txt)} chars sha={sha(txt)[:12]}")
    (ROOT/"papers/fulltext_manifest.json").write_text(json.dumps(man,ensure_ascii=False,indent=2),encoding="utf-8")
if __name__=="__main__": main()
