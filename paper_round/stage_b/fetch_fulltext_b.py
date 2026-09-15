#!/usr/bin/env python3
"""Stage B-prep: fetch FULL paper text snapshots (ar5iv HTML -> text) for the selected tasks, reusing the
stage A fetcher unchanged. Saves snapshot + sha256 + manifest; checks that the private key strings occur
in the snapshot (eval-side only; never written into DOC_PATH). No model calls."""
from __future__ import annotations
import sys, json, pathlib, argparse
ROOT = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT.parent / "stage_a"))
from fetch_fulltext import fetch, sha   # stage A implementation, byte-identical behaviour

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("spec", help="json: {arxiv_id: [key strings to check]}")
    a = ap.parse_args()
    spec = json.loads(pathlib.Path(a.spec).read_text(encoding="utf-8"))
    out = ROOT / "papers"; out.mkdir(exist_ok=True)
    mpath = out / "fulltext_manifest.json"
    man = json.loads(mpath.read_text(encoding="utf-8")) if mpath.exists() else {}
    for ax, keys in spec.items():
        p = out / f"{ax}_fulltext.txt"
        if p.exists():
            txt = p.read_text(encoding="utf-8"); url = man.get(ax, {}).get("url", "cached")
        else:
            url, txt = fetch(ax); p.write_text(txt, encoding="utf-8")
        checks = {k: (k.lower() in txt.lower()) for k in keys}
        man[ax] = {"url": url, "chars": len(txt), "sha256": sha(txt), "key_strings_present": checks}
        print(f"{ax}: {len(txt)} chars sha={sha(txt)[:12]} checks={checks}")
    mpath.write_text(json.dumps(man, ensure_ascii=False, indent=2), encoding="utf-8")

if __name__ == "__main__":
    main()
