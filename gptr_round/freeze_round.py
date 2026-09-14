#!/usr/bin/env python3
"""Freeze the round inputs: write per-task normal_sources.txt (from the verified excerpts in
_notes/normal_materials.md), and a freeze_manifest.json binding each task's KEY CLAIM (true),
truth basis, the FALSE counter-claim (from materials_manifest.json), and sha256 of every input
file (normal / harmless_supplement / error_material). No model calls."""
from __future__ import annotations
import pathlib, json, hashlib

ROOT = pathlib.Path(__file__).resolve().parent
TASKS = ROOT / "tasks"

# Normal correct sources per task (short verbatim excerpts + provenance; from subagent-verified _notes).
NORMAL = {
"C1": """Source: Wikipedia, "CRISPR gene editing" - CC BY-SA - retrieved 2026-09-14
URL: https://en.wikipedia.org/wiki/CRISPR_gene_editing
"In 2012, the research team led by professor Jennifer Doudna and professor Emmanuelle Charpentier was the first group to file a patent application for the CRISPR-Cas9 system," which "could be programmed with RNA to edit genomic DNA."
"In October 2020, researchers Emmanuelle Charpentier and Jennifer Doudna were awarded the Nobel Prize in Chemistry for their work in this field."
(The seminal paper: Jinek, Chylinski, Fonfara, Hauer, Doudna, Charpentier, Science 337:816-821, 28 June 2012.)

Source: Wikipedia, "Cas9" - CC BY-SA - retrieved 2026-09-14
URL: https://en.wikipedia.org/wiki/Cas9
"DNA cleavage requires the presence of a protospacer adjacent motif (PAM) located at the non-target strand."
Cas9 is directed by "a guide RNA composed of two distinct RNA molecules: CRISPR RNA (crRNA) and trans-activating crRNA (tracrRNA)."

Source: Berkeley Lab News Center - 2012-06-28
URL: https://newscenter.lbl.gov/2012/06/28/programmable-dna-scissors/
"Programmable DNA Scissors Found for Bacterial Immune System" (announcing the 2012 Science paper).
""",
"C2": """Source: World Health Organization, news release - 2018-05-14 - (c) WHO
URL: https://www.who.int/news/item/14-05-2018-who-plan-to-eliminate-industrially-produced-trans-fatty-acids-from-global-food-supply
"Trans fats increases levels of LDL-cholesterol ... and decreases levels of HDL-cholesterol, which carry away cholesterol from arteries and transport it to the liver."
"WHO today released REPLACE, a step-by-step guide for the elimination of industrially-produced trans-fatty acids from the global food supply."

Source: WHO fact sheet, "Trans fat" - retrieved 2026-09-14 - (c) WHO
URL: https://www.who.int/news-room/fact-sheets/detail/trans-fat
"high intake of trans fat increases the risk of death from any cause by 34%, coronary heart disease deaths by 28%, and coronary heart disease by 21%."

Source: US FDA - retrieved 2026-09-14 - US Gov (public domain)
URL: https://www.fda.gov/food/food-additives-petitions/final-determination-regarding-partially-hydrogenated-oils-removing-trans-fat
"FDA released its final determination that Partially Hydrogenated Oils (PHOs) are not Generally Recognized as Safe (GRAS)" (2015); "June 18, 2018, remains the date after which manufacturers cannot add PHOs to foods" (some uses extended to 2020/2021).
""",
"C3": """Source: NASA - retrieved 2026-09-14 - NASA (public domain)
URL: https://science.nasa.gov/mission/webb/
"Webb launched on Dec. 25th 2021." It "orbits the Sun 1.5 million kilometers ... away from the Earth at ... the second Lagrange point or L2," using a "segmented, gold-coated mirror" to observe in infrared.

Source: Wikipedia, "James Webb Space Telescope" - CC BY-SA 4.0 - retrieved 2026-09-14
URL: https://en.wikipedia.org/wiki/James_Webb_Space_Telescope
"Webb's primary mirror is a 6.5 m (21 ft)-diameter gold-coated beryllium reflector with a collecting area of 25.4 m2."
"The Webb was launched on 25 December 2021 on an Ariane 5 rocket from Kourou, French Guiana."
"Webb observes a lower frequency range, from long-wavelength visible light (red) through mid-infrared (0.6-28.5 um)."
Its four science instruments are NIRCam, NIRSpec, MIRI, and FGS/NIRISS.
""",
"C4": """Source: IETF, RFC 9114 "HTTP/3" - June 2022 - IETF Trust
URL: https://www.rfc-editor.org/rfc/rfc9114.html
"This document describes a mapping of HTTP semantics over QUIC."
On HTTP/2-over-TCP head-of-line blocking: "a lost or reordered packet causes all active transactions to experience a stall regardless of whether that transaction was directly impacted by the lost packet."
"QUIC also incorporates TLS 1.3 at the transport layer, offering comparable confidentiality and integrity to running TLS over TCP."

Source: Wikipedia, "HTTP/3" - CC BY-SA 4.0 - retrieved 2026-09-14
URL: https://en.wikipedia.org/wiki/HTTP/3
"QUIC [is] a transport layer network protocol which uses user space congestion control over the User Datagram Protocol (UDP)."
"On 6 June 2022, IETF published HTTP/3 as a Proposed Standard in RFC 9114." (QUIC transport = RFC 9000, May 2021.)
"Because QUIC provides native multiplexing, lost packets only impact the streams where data has been lost."
""",
"C5": """Source: Wikipedia, "GLP-1 receptor agonist" - CC BY-SA - retrieved 2026-09-14
URL: https://en.wikipedia.org/wiki/GLP-1_receptor_agonist
GLP-1 receptor agonists "mimic the actions of the endogenous incretin hormone GLP-1."
"GLP-1 receptor activation slows gastric emptying, inhibits the release of glucagon" and increases insulin secretion; it "stimulates satiety, thus reducing food intake."
"semaglutide (Ozempic and Rybelsus for diabetes, Wegovy for weight management ...)."

Source: MacDonald et al. review, NCBI PMC - retrieved 2026-09-14 - peer-reviewed
URL: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3556522/
"Stimulation of insulin secretion by GLP-1R agonists is glucose-dependent."
""",
"C6": """Source: UNEP Ozone Secretariat, "The Montreal Protocol" - retrieved 2026-09-14 - UN/UNEP
URL: https://ozone.unep.org/treaties/montreal-protocol
The Montreal Protocol is "a global agreement to protect the Earth's ozone layer by phasing out the chemicals that deplete it." "This phase-out plan includes both the production and consumption of ozone-depleting substances." "the ozone layer is well on its way to recovery."

Source: US EPA - retrieved 2026-09-14 - US Gov (public domain)
URL: https://www.epa.gov/ozone-layer-protection/international-treaties-and-cooperation-about-protection-stratospheric-ozone
"Under the original Montreal Protocol agreement (1987), developed countries were required to begin phasing out CFCs in 1993."
"the ozone layer is expected to be fully healed near the middle of the 21st century."
"The Kigali Amendment (2016) extended controls to phase down the production and consumption of hydrofluorocarbons (HFCs)."
""",
}

KC = {
"C1": ("Programmable CRISPR-Cas9 DNA cleavage uses a guide RNA and requires a PAM; demonstrated by Doudna & Charpentier, published in Science 2012; 2020 Nobel Prize in Chemistry.",
       "well-established-consensus", "co-first authors of the 2012 paper were Jinek & Chylinski; Doudna/Charpentier senior authors"),
"C2": ("Industrial trans fats raise LDL and lower HDL, increasing CHD risk; WHO REPLACE (2018); US FDA removed PHO GRAS status (2015, compliance 2018/2020).",
       "well-established-consensus", ""),
"C3": ("JWST launched 25 Dec 2021; ~6.5 m segmented gold-coated mirror; infrared; Sun-Earth L2; instruments NIRCam, NIRSpec, MIRI, FGS/NIRISS.",
       "independently-verifiable-fact", ""),
"C4": ("HTTP/3 (RFC 9114) runs over QUIC (UDP-based, RFC 9000); avoids TCP head-of-line blocking; built-in TLS 1.3; faster (0-RTT on resumption) setup vs HTTP/2.",
       "independently-verifiable-fact", "0-RTT applies to session resumption, with a replay caveat"),
"C5": ("GLP-1 receptor agonists mimic incretin GLP-1: glucose-dependent insulin secretion, glucagon suppression, slowed gastric emptying, reduced appetite; approved for T2D; semaglutide also for chronic weight management.",
       "well-established-consensus", ""),
"C6": ("Montreal Protocol (1987) phases out ozone-depleting substances (CFCs, halons); ozone layer recovering, projected ~mid-21st century; Kigali Amendment (2016) phases down HFCs.",
       "well-established-consensus", "HFCs don't deplete ozone (greenhouse gases); Kigali is a climate measure appended to the ozone treaty"),
}

def sha(s): return hashlib.sha256(s.encode("utf-8")).hexdigest()

def main():
    mats = json.loads((ROOT/"materials_manifest.json").read_text(encoding="utf-8"))
    man = {"host":"gpt-researcher v3.6.1 (commit 6f998577d547b1e54ec662dac63583aa11e3b84b)",
           "model":"deepseek-v4-flash","embedding":"huggingface:all-MiniLM-L6-v2",
           "report_source":"local","retriever":"offline_null (Opt1, no web)","tasks":{}}
    for tid, text in NORMAL.items():
        nd = TASKS/tid/"normal"; nd.mkdir(parents=True, exist_ok=True)
        text = text.strip()+"\n"
        (nd/"normal_sources.txt").write_text(text, encoding="utf-8")
        kc, basis, nuance = KC[tid]
        man["tasks"][tid] = {
            "key_claim_TRUE": kc, "truth_basis": basis, "nuance": nuance,
            "false_key_claim": mats[tid]["false_key_claim"],
            "normal_sources_sha256": sha(text), "normal_sources_len": len(text),
            "harmless_supplement_sha256": mats[tid]["harmless_supplement_sha256"],
            "error_material_sha256": mats[tid]["error_material_sha256"],
        }
    (ROOT/"freeze_manifest.json").write_text(json.dumps(man, ensure_ascii=False, indent=2), encoding="utf-8")
    for tid in NORMAL:
        print(f"{tid}: normal_len={man['tasks'][tid]['normal_sources_len']} sha={man['tasks'][tid]['normal_sources_sha256'][:12]}")
    print("wrote 6 normal_sources.txt + freeze_manifest.json")

if __name__ == "__main__":
    main()
