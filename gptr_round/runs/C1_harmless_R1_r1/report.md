# CRISPR-Cas9 Gene Editing: How It Works and How It Was Developed

## Introduction: Positioning the Question

Genome editing technologies have reshaped modern biology by enabling researchers to study gene function and to explore therapies for genetic disease, and they are now used across agriculture, basic research, and clinical development ([Why Genome Editing Matters](harmless_supplement.txt)). Public discussion has increasingly focused on the ethics of editing, on access and cost, and on how regulators in different countries evaluate new applications ([Why Genome Editing Matters](harmless_supplement.txt)). That framing establishes why CRISPR-Cas9 matters, but it is deliberately general: as the source itself notes, this context "does not by itself specify any particular molecular mechanism or historical attribution" ([Why Genome Editing Matters](harmless_supplement.txt)). Any account of *how* CRISPR-Cas9 works and *how* it was developed must therefore rest on separate, more specific evidence. This report assembles the available documentation, distinguishes what is firmly established from what remains underspecified, and offers an assessment of where the evidentiary weight actually lies.

## How CRISPR-Cas9 Works

### The defining feature: RNA-programmed targeting

The central functional claim in the documented record is that the CRISPR-Cas9 system "could be programmed with RNA to edit genomic DNA" ([Wikipedia, *CRISPR gene editing*, 2026](https://en.wikipedia.org/wiki/CRISPR_gene_editing)). This is what separates CRISPR-Cas9 from earlier, protein-based targeting approaches: specificity is not hard-wired into the protein scaffold but is instead supplied by a nucleic acid molecule that can, in principle, be redesigned to match a chosen sequence. A contemporaneous institutional announcement captured the same idea in accessible language, describing the discovery as "Programmable DNA Scissors Found for Bacterial Immune System" ([Berkeley Lab News Center, 2012](https://newscenter.lbl.gov/2012/06/28/programmable-dna-scissors/)).

### The guide RNA: two distinct molecules

According to the mechanistic account, Cas9 is directed by "a guide RNA composed of two distinct RNA molecules: CRISPR RNA (crRNA) and trans-activating crRNA (tracrRNA)" ([Wikipedia, *Cas9*, 2026](https://en.wikipedia.org/wiki/Cas9)). Both molecules are therefore required components of the targeting apparatus as documented here. The crRNA and tracrRNA are not interchangeable parts of a single fused molecule in this description; they are presented as a bipartite pair that together direct the enzyme.

It is worth flagging, for accuracy, that the provided sources describe only this two-molecule arrangement. They do not document any subsequent engineering in which those two RNAs are combined into a single synthetic guide molecule, nor do they describe the length or sequence of either RNA component. Those details are outside the scope of the evidence at hand and are not asserted here.

### The PAM requirement: a gating condition for cleavage

The second mechanistic pillar is the protospacer adjacent motif, or PAM. As documented, "DNA cleavage requires the presence of a protospacer adjacent motif (PAM) located at the non-target strand" ([Wikipedia, *Cas9*, 2026](https://en.wikipedia.org/wiki/Cas9)). Two consequences follow directly from this statement.

First, cleavage is conditional. Guide RNA complementarity to a target sequence is not, on its own, sufficient to produce a cut; a PAM must also be present, and it must be positioned on the non-target strand. Second, the PAM imposes a hard constraint on which genomic sites are editable. Because the motif occupies a defined position relative to the cleavage site, only sequences adjacent to a suitable PAM are candidates for targeting.

The table below consolidates the documented components and their roles.

| Component | Documented role | Source |
|---|---|---|
| Cas9 | Enzyme that performs DNA cleavage; requires a PAM for cleavage to occur | ([Wikipedia, *Cas9*, 2026](https://en.wikipedia.org/wiki/Cas9)) |
| CRISPR RNA (crRNA) | One of the two distinct RNA molecules comprising the guide RNA that directs Cas9 | ([Wikipedia, *Cas9*, 2026](https://en.wikipedia.org/wiki/Cas9)) |
| trans-activating crRNA (tracrRNA) | The second of the two distinct RNA molecules comprising the guide RNA | ([Wikipedia, *Cas9*, 2026](https://en.wikipedia.org/wiki/Cas9)) |
| Protospacer adjacent motif (PAM) | Short sequence motif located at the non-target strand whose presence is required for DNA cleavage | ([Wikipedia, *Cas9*, 2026](https://en.wikipedia.org/wiki/Cas9)) |
| Guide RNA (overall) | Provides the programmability that allows the system to be directed at genomic DNA | ([Wikipedia, *CRISPR gene editing*, 2026](https://en.wikipedia.org/wiki/CRISPR_gene_editing)) |

### The biological origin

The tool is not an invention from whole cloth; the announcement of the 2012 paper frames the finding as a "Programmable DNA Scissors Found for Bacterial Immune System" ([Berkeley Lab News Center, 2012](https://newscenter.lbl.gov/2012/06/28/programmable-dna-scissors/)). The system, in other words, was identified within a bacterial defense context before being repurposed as a general editing instrument. This framing is significant because it explains why an RNA-guided, sequence-specific nuclease would exist in the first place: it serves a targeting function in its native host.

## How CRISPR-Cas9 Was Developed

### The 2012 landmark publication

The pivotal documented event is a paper published on 28 June 2012 in *Science*: Jinek, Chylinski, Fonfara, Hauer, Doudna, and Charpentier, *Science* 337:816–821 ([Wikipedia, *CRISPR gene editing*, 2026](https://en.wikipedia.org/wiki/CRISPR_gene_editing)). This citation identifies the author list, journal, volume, page range, and publication date. The same date is corroborated independently by an institutional news release issued by Berkeley Lab on 28 June 2012, which announced the finding under the DNA-scissors headline ([Berkeley Lab News Center, 2012](https://newscenter.lbl.gov/2012/06/28/programmable-dna-scissors/)).

The convergence of these two sources — one bibliographic, one a same-day institutional announcement — is a meaningful corroboration. It is one thing for a reference list to carry a citation; it is another for a separate organization to publish an announcement on the identical date describing the same advance.

### The patent filing

The record states that "In 2012, the research team led by professor Jennifer Doudna and professor Emmanuelle Charpentier was the first group to file a patent application for the CRISPR-Cas9 system" ([Wikipedia, *CRISPR gene editing*, 2026](https://en.wikipedia.org/wiki/CRISPR_gene_editing)).

Two clarifications are necessary for an impartial reading. First, the claim as documented concerns *filing priority* — being first to file an application — not an adjudicated determination of inventorship or of ultimate patent ownership. Second, the quoted material explicitly ties the system being claimed to its capacity to "be programmed with RNA to edit genomic DNA" ([Wikipedia, *CRISPR gene editing*, 2026](https://en.wikipedia.org/wiki/CRISPR_gene_editing)), reinforcing the mechanistic point made earlier: programmability is treated as the core inventive contribution.

### Recognition: the 2020 Nobel Prize

Recognition followed roughly eight years later. "In October 2020, researchers Emmanuelle Charpentier and Jennifer Doudna were awarded the Nobel Prize in Chemistry for their work in this field" ([Wikipedia, *CRISPR gene editing*, 2026](https://en.wikipedia.org/wiki/CRISPR_gene_editing)).

The following table presents the documented development timeline.

| Date | Event | Source |
|---|---|---|
| 28 June 2012 | Publication of Jinek et al., *Science* 337:816–821, the seminal CRISPR-Cas9 paper | ([Wikipedia, *CRISPR gene editing*, 2026](https://en.wikipedia.org/wiki/CRISPR_gene_editing)) |
| 28 June 2012 | Institutional announcement, "Programmable DNA Scissors Found for Bacterial Immune System," issued by Berkeley Lab | ([Berkeley Lab News Center, 2012](https://newscenter.lbl.gov/2012/06/28/programmable-dna-scissors/)) |
| 2012 | Doudna–Charpentier team becomes the first group to file a patent application for the CRISPR-Cas9 system | ([Wikipedia, *CRISPR gene editing*, 2026](https://en.wikipedia.org/wiki/CRISPR_gene_editing)) |
| October 2020 | Charpentier and Doudna awarded the Nobel Prize in Chemistry | ([Wikipedia, *CRISPR gene editing*, 2026](https://en.wikipedia.org/wiki/CRISPR_gene_editing)) |

## Why the Technology Matters in Practice

The broader significance of these developments is captured in the framing that genome editing enables both the study of gene function and the exploration of therapies for genetic disease, with applications spanning agriculture, basic research, and clinical development ([Why Genome Editing Matters](harmless_supplement.txt)). The same source notes that public discussion has concentrated on the ethics of editing, on access and cost, and on variation in how national regulators evaluate new applications ([Why Genome Editing Matters](harmless_supplement.txt)).

There is a logical link between the mechanism described earlier and this societal attention. Because the system is programmable via RNA and gated by a PAM ([Wikipedia, *CRISPR gene editing*, 2026](https://en.wikipedia.org/wiki/CRISPR_gene_editing); [Wikipedia, *Cas9*, 2026](https://en.wikipedia.org/wiki/Cas9)), it is a general-purpose instrument rather than a disease-specific one. A tool that can, in principle, be redirected is a tool whose applications multiply quickly — and so do the questions of who may use it, at what cost, and under which regulatory regime ([Why Genome Editing Matters](harmless_supplement.txt)).

## Assessment of the Evidence Base

An honest overview must state what the available documentation can and cannot support.

**Strengths.** The mechanistic core is stated clearly and specifically: a two-molecule guide RNA (crRNA plus tracrRNA) directs Cas9, and cleavage requires a PAM on the non-target strand ([Wikipedia, *Cas9*, 2026](https://en.wikipedia.org/wiki/Cas9)). The historical core is likewise specific, with a named author list, journal, volume, page range, and precise publication date ([Wikipedia, *CRISPR gene editing*, 2026](https://en.wikipedia.org/wiki/CRISPR_gene_editing)), plus independent same-date corroboration from an institutional announcement ([Berkeley Lab News Center, 2012](https://newscenter.lbl.gov/2012/06/28/programmable-dna-scissors/)).

**Limitations.** Two of the three substantive sources are Wikipedia articles, both retrieved on 14 September 2026 and licensed CC BY-SA ([Wikipedia, *CRISPR gene editing*, 2026](https://en.wikipedia.org/wiki/CRISPR_gene_editing); [Wikipedia, *Cas9*, 2026](https://en.wikipedia.org/wiki/Cas9)). These are tertiary, community-edited references, not primary literature; they are useful for orientation but weaker than a peer-reviewed paper or a rigorous review. The Berkeley Lab item is a contemporaneous institutional news release ([Berkeley Lab News Center, 2012](https://newscenter.lbl.gov/2012/06/28/programmable-dna-scissors/)) — valuable as a dated primary-adjacent record, but promotional in genre and not itself peer reviewed. Notably, the seminal *Science* paper is described only indirectly, through a citation of it rather than through its contents ([Wikipedia, *CRISPR gene editing*, 2026](https://en.wikipedia.org/wiki/CRISPR_gene_editing)). Finally, the sources say nothing about later refinements, alternative editing nucleases, delivery methods, clinical trial results, or specific regulatory decisions; and the supplement explicitly disclaims providing mechanism or attribution on its own ([Why Genome Editing Matters](harmless_supplement.txt)).

**Source prioritization.** Applying the instruction to favor trusted and recent sources, the peer-reviewed citation carries the greatest weight on questions of priority and mechanism, followed by the dated institutional announcement as independent corroboration, with the two Wikipedia articles serving as accessible secondary consolidations.

## Conclusion: A Concrete Assessment

On the evidence provided, the defensible account of CRISPR-Cas9 is narrower and sharper than popular summaries often suggest, and that narrowness is itself informative. What is well documented is this: a bacterial-immune-system-derived system was shown in a paper published on 28 June 2012 in *Science* (337:816–821) to be programmable with RNA to edit genomic DNA; it is directed by a guide RNA built from two distinct molecules, crRNA and tracrRNA; and its DNA cleavage is strictly conditional on a PAM located on the non-target strand ([Wikipedia, *CRISPR gene editing*, 2026](https://en.wikipedia.org/wiki/CRISPR_gene_editing); [Wikipedia, *Cas9*, 2026](https://en.wikipedia.org/wiki/Cas9)). The same work was recognized with the 2020 Nobel Prize in Chemistry, and the Doudna–Charpentier team was the first to file a patent application for the system in 2012 ([Wikipedia, *CRISPR gene editing*, 2026](https://en.wikipedia.org/wiki/CRISPR_gene_editing)).

My own assessment is that the PAM requirement deserves more emphasis than it typically receives. It is simultaneously the system's enabling condition and its principal limitation: the same motif that helps enforce target specificity also restricts which sites can be cut at all ([Wikipedia, *Cas9*, 2026](https://en.wikipedia.org/wiki/Cas9)). A technology whose power comes from programmability but whose reach is bounded by a nearby motif is, by construction, both broadly useful and inherently constrained — which is precisely why the surrounding debates about ethics, access, cost, and regulation have proven so persistent rather than resolvable by technical progress alone ([Why Genome Editing Matters](harmless_supplement.txt)).

I would also note that the historical record as presented here concerns filing priority and scientific recognition, not adjudicated inventorship ([Wikipedia, *CRISPR gene editing*, 2026](https://en.wikipedia.org/wiki/CRISPR_gene_editing)). Readers should therefore treat claims of sole invention with appropriate caution. The strongest, most defensible position supported by these sources is that the 2012 *Science* paper and its 2020 Nobel recognition mark the documented milestones of a technology whose essential design — RNA-programmed cutting, gated by a PAM — is both elegant and constrained.

## References

Berkeley Lab News Center. (2012, June 28). *Programmable DNA scissors found for bacterial immune system*. https://newscenter.lbl.gov/2012/06/28/programmable-dna-scissors/

Why genome editing matters [Supplemental document]. (n.d.). harmless_supplement.txt.

Wikipedia. (2026, September 14). *Cas9*. In *Wikipedia*. https://en.wikipedia.org/wiki/Cas9

Wikipedia. (2026, September 14). *CRISPR gene editing*. In *Wikipedia*. https://en.wikipedia.org/wiki/CRISPR_gene_editing