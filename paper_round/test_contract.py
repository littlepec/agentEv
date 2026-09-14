#!/usr/bin/env python3
"""Targeted unit tests for the 3 offline closeouts in contract.py. No model calls, no full audit."""
from __future__ import annotations
import asyncio, pathlib, tempfile, json, contract as C

def _mk(tmp, name, text):
    p = pathlib.Path(tmp)/name; p.write_text(text, encoding="utf-8"); return p

def test_stable_mapping():
    tmp = tempfile.mkdtemp()
    ev = _mk(tmp,"ev.txt","EVIDENCE PAPER TEXT")
    L  = _mk(tmp,"L.txt","faithful interpretation")
    Lp = _mk(tmp,"Lp.txt","one relation flipped")
    # E+L and E+L' must share identical document_1 (evidence) and differ only in document_2
    d1,m1 = C.stable_docpath({"evidence":ev,"interp":L}, pathlib.Path(tmp)/"EL")
    d2,m2 = C.stable_docpath({"evidence":ev,"interp":Lp}, pathlib.Path(tmp)/"ELp")
    assert m1==m2=={"evidence":"document_1.txt","interp":"document_2.txt"}, m1
    assert (d1/"document_1.txt").read_text()== (d2/"document_1.txt").read_text()=="EVIDENCE PAPER TEXT"
    assert (d1/"document_2.txt").read_text()!=(d2/"document_2.txt").read_text()
    # layout independent of any 'arm'/'cell' — repeated calls identical
    d3,m3 = C.stable_docpath({"evidence":ev,"interp":L}, pathlib.Path(tmp)/"EL_again")
    assert m3==m1 and (d3/"document_1.txt").read_text()==(d1/"document_1.txt").read_text()
    # E condition (evidence only) -> only document_1
    dE,mE = C.stable_docpath({"evidence":ev}, pathlib.Path(tmp)/"E")
    assert mE=={"evidence":"document_1.txt"} and not (dE/"document_2.txt").exists()
    print("PASS test_stable_mapping (id/order stable across conditions & arms; E+L vs E+L' differ only in document_2)")

def test_normalize_and_no_evidence():
    # lowercase keys normalized + content kept
    kept,st = C.normalize_curated([{"source":"document_1.txt","title":"T","content":"real body"}])
    assert kept==[{"Source":"document_1.txt","Title":"T","Content":"real body"}] and st["no_evidence"] is False
    # empty-content item DROPPED (not passed as shell); all-empty -> no_evidence path
    kept,st = C.normalize_curated([{"source":"d","title":"only title","content":"   "}])
    assert kept==[] and st["dropped_empty"]==1 and st["no_evidence"] is True, (kept,st)
    # mixed: one real, one empty -> keep real, drop empty, not no_evidence
    kept,st = C.normalize_curated([{"Source":"a","Title":"t","Content":"x"},{"source":"b","content":""}])
    assert len(kept)==1 and st["dropped_empty"]==1 and st["no_evidence"] is False
    # key-case conflict raises
    try:
        C.normalize_curated([{"Source":"A","source":"B","Content":"x"}]); assert False,"no raise"
    except C.CurationContractError: pass
    print("PASS test_normalize_and_no_evidence (empty->dropped->predefined no_evidence; conflict raises)")

def test_provider_log_full_and_preview():
    tmp = tempfile.mkdtemp()
    big = "X"*5000
    calls=[{"phase":"start","messages":[{"type":"human","content":big}]},
           {"phase":"end","generations":[{"text":"Y"*7000,"finish":"stop"}]}]
    full=pathlib.Path(tmp)/"provider_log.json"; prev=pathlib.Path(tmp)/"provider_log_preview.json"
    C.save_provider_logs(calls, full, prev, preview_chars=800)
    fj=json.loads(full.read_text(encoding="utf-8")); pj=json.loads(prev.read_text(encoding="utf-8"))
    assert len(fj[0]["messages"][0]["content"])==5000, "full log must NOT truncate"
    assert len(fj[1]["generations"][0]["text"])==7000, "full log must NOT truncate"
    assert pj[0]["messages"][0]["content"].endswith("chars]") and len(pj[0]["messages"][0]["content"])<900
    print("PASS test_provider_log_full_and_preview (full untruncated; preview separate & truncated)")

if __name__=="__main__":
    test_stable_mapping(); test_normalize_and_no_evidence(); test_provider_log_full_and_preview()
    print("ALL UNIT TESTS PASSED")
