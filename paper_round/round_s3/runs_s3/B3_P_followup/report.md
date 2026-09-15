# How Many Hand-Crafted Question Templates Were Required? A Detailed Analysis of Reported Template-Construction Effort

## Executive Summary

Based on the technical data contained in the source document, the reported hand-crafted template count for the system under review is **209 templates in total** ([document_2.txt](document_2.txt)). This total is the sum of two distinct, domain-specific template-construction efforts: **106 templates** built for the Freebase evaluation and **103 templates** built for an in-house power tool domain knowledge base ([document_2.txt](document_2.txt)). Because the source explicitly states that question template construction constitutes the *only* human labor reported in the work, these 209 hand-crafted templates represent the complete measured manual annotation effort of the system ([document_2.txt](document_2.txt)).

This report decomposes that headline figure, examines the predicate-driven logic behind it, derives secondary efficiency metrics from the reported numbers, and identifies the boundaries and limitations of what the source material does and does not establish.

## Framing the Query

The question of how many hand-crafted templates were required is not merely a counting exercise. In template-based question generation systems, the number of templates is a direct proxy for human labor cost. If a system requires thousands of templates to cover a knowledge base, the manual burden is considerable. If a system requires only a few hundred templates to cover hundreds of triples and more than a hundred distinct predicates, the manual burden is comparatively modest. The source document frames this explicitly: the design "ties template creation to predicates, keeping the template set compact relative to the triple set" ([document_2.txt](document_2.txt)). Understanding the template count therefore requires understanding the unit to which templates are attached — the predicate, not the triple.

## The Direct Answer: 209 Templates

The single most useful figure for answering the query is stated directly and unambiguously in the source: "Together with the 106 Freebase templates, the authors wrote **209 templates in total**" ([document_2.txt](document_2.txt)). This total was reported specifically within the template-construction experiment described in the paper ([document_2.txt](document_2.txt)).

The arithmetic is transparent and internally consistent:

| Component | Templates | Predicates Covered |
|---|---|---|
| Freebase evaluation | 106 | 53 |
| In-house power tool domain | 103 | 67 |
| **Total reported** | **209** | **120** (53 + 67) |

The 106 + 103 = 209 sum is exact, with no rounding or estimation involved ([document_2.txt](document_2.txt)). The 120-predicate aggregate is a derived figure computed by this analysis and is subject to the caveat discussed later in this report regarding possible predicate-name overlap between the two knowledge bases.

## Breakdown by Evaluation Domain

### The Freebase Evaluation

For the Freebase evaluation, the work used **500 randomly selected triples** ([document_2.txt](document_2.txt)). Against those 500 triples, the paper reports **106 hand-crafted templates** ([document_2.txt](document_2.txt)). The critical structural detail is that the 500 triples shared only **53 distinct predicates**, meaning the authors made approximately **two templates for each predicate on average** ([document_2.txt](document_2.txt)).

This yields a precise ratio: 106 templates ÷ 53 predicates = 2.00 templates per predicate. The source's characterisation of "2 templates for each predicate on average" is therefore not an approximation but an exact arithmetic outcome of the reported figures ([document_2.txt](document_2.txt)).

### The In-House Power Tool Domain

The second evaluation domain is an in-house power tool knowledge base. For this domain, the paper reports **67 predicates**, and for those 67 predicates the authors hand-crafted **103 templates** ([document_2.txt](document_2.txt)). The source notes that "the domain-specific KB has its own predicate set and required its own template set" ([document_2.txt](document_2.txt)).

Here the ratio differs from the Freebase case: 103 templates ÷ 67 predicates ≈ **1.54 templates per predicate**. This is a materially lower intensity of template coverage than the Freebase domain, where the ratio was exactly 2.00. The source does not explain the reason for the difference, but the discrepancy is worth flagging because it indicates that template-to-predicate density is not a fixed constant across domains but a design choice that varies with the characteristics of each predicate set ([document_2.txt](document_2.txt)).

## Template-to-Triple and Template-to-Question Efficiency

Beyond the raw template count, the source provides enough data to derive several efficiency indicators that contextualise the 209-template figure.

For the Freebase evaluation, applying the 106 templates to the 500 selected triples generated **991 seed questions** ([document_2.txt](document_2.txt)). The experiment additionally retrieved **1,529 more questions from Google** ([document_2.txt](document_2.txt)).

| Derived Metric | Value | Calculation Basis |
|---|---|---|
| Triples per template (Freebase) | ≈ 4.72 | 500 ÷ 106 |
| Seed questions per template (Freebase) | ≈ 9.35 | 991 ÷ 106 |
| Seed questions per triple (Freebase) | ≈ 1.98 | 991 ÷ 500 |
| Templates per predicate (Freebase) | 2.00 | 106 ÷ 53 |
| Templates per predicate (power tool) | ≈ 1.54 | 103 ÷ 67 |
| Templates per predicate (combined) | ≈ 1.74 | 209 ÷ 120 |
| Freebase share of all templates | ≈ 50.7% | 106 ÷ 209 |
| Power tool share of all templates | ≈ 49.3% | 103 ÷ 209 |

These derived ratios are computed by this analysis from the raw figures reported in the source ([document_2.txt](document_2.txt)). They are not stated in the document itself and should be treated as interpretive rather than as reported results.

The most significant ratio is the one the source emphasises directly: the template set is "compact relative to the triple set" ([document_2.txt](document_2.txt)). A single template reused across multiple triples produces multiple seed questions, which is precisely how 106 templates can service 500 triples and yield 991 seed questions.

## The Question-Generation Pipeline and Where Templates Fit

The source describes a clear architectural sequence. The proposed system "first constructs a small set of question templates," and "each template is associated with a predicate in the knowledge base" ([document_2.txt](document_2.txt)). This association is the defining constraint: template creation follows the predicates present in the knowledge base rather than the triples or entities ([document_2.txt](document_2.txt)).

The pipeline can be summarised in three stages as reported:

1. **Predicate enumeration.** Identify the distinct predicates in the target knowledge base — 53 for Freebase, 67 for the power tool domain ([document_2.txt](document_2.txt)).
2. **Manual template construction.** Hand-craft templates mapped to those predicates — 106 and 103 respectively, for a total of 209 ([document_2.txt](document_2.txt)).
3. **Question generation and augmentation.** Apply templates to triples to produce seed questions (991 in the Freebase case), then supplement with externally retrieved questions (1,529 from Google) ([document_2.txt](document_2.txt)).

Under this architecture, the manual bottleneck is bounded by predicate count rather than by triple count. That is why 500 randomly selected Freebase triples required only 106 templates rather than 500 or more ([document_2.txt](document_2.txt)).

## Significance: Template Construction as the Only Reported Human Labor

The source makes an important claim about the scope of manual effort: "The paper states that the only human labor in this work is question template construction" ([document_2.txt](document_2.txt)). This elevates the 209 figure from a descriptive statistic to the single quantitative measure of human annotation cost for the entire system as reported.

This has two implications. First, the reported manual burden of the system is 209 discrete template authoring tasks — a strikingly small number relative to the volume of data handled (500 triples in Freebase alone, plus an entire in-house domain, plus a combined question pool of 2,520 questions when the 991 seeds and 1,529 retrieved items are aggregated). Second, the source frames this explicitly as a design virtue: "This design ties template creation to predicates, keeping the template set compact relative to the triple set" ([document_2.txt](document_2.txt)).

The source further generalises: "These figures show the manual template-building effort scales with predicate coverage in each evaluation" ([document_2.txt](document_2.txt)). This is a scaling claim. It asserts that if a knowledge base has more predicates, more templates are needed — but crucially, not more templates in proportion to triples. The 209 total across 120 predicates and at least 500 triples supports this reading, though only two data points are available.

## Limitations and Caveats

An objective reading requires acknowledging what the source does not establish.

**The 120-predicate figure is derived, not reported.** The source reports 53 Freebase predicates and 67 power tool predicates, but never states a combined predicate count ([document_2.txt](document_2.txt)). The 120 figure assumes no predicate names are shared between the two knowledge bases. It is plausible that Freebase predicates and in-house power tool predicates are disjoint, but the source does not confirm this. If the sets overlap, the combined distinct-predicate count would be lower than 120 and the combined templates-per-predicate ratio correspondingly higher.

**Per-domain template-to-predicate ratios are uneven.** The Freebase domain received exactly 2.00 templates per predicate while the power tool domain received approximately 1.54 ([document_2.txt](document_2.txt)). The discrepancy is unexplained in the source and suggests that the 209 total masks non-uniform allocation of manual effort.

**Question-level usage is only reported for Freebase.** The 991 seed questions and 1,529 Google-retrieved questions are reported only in connection with the Freebase evaluation ([document_2.txt](document_2.txt)). No equivalent question-generation figures are provided for the power tool domain, so template productivity cannot be compared across domains on a per-question basis.

**The source is a secondary summary.** The document consistently refers to what "the paper reports" or "the paper states" ([document_2.txt](document_2.txt)), indicating it is an account of a primary research paper rather than the primary report itself. The figures therefore carry the reliability of the summarising document, which appears internally consistent given that its repeated numeric claims (500 triples, 106 templates, 53 predicates, 991 seed questions, 1,529 Google questions, 67 predicates, 103 templates, 209 total) do not conflict across passages ([document_2.txt](document_2.txt)).

**Notable internal redundancy.** The source document contains repeated near-identical blocks of text covering the same Freebase and power tool figures ([document_2.txt](document_2.txt)). This redundancy does not introduce contradictions, but it means the corpus provides no additional independent corroboration for the numbers — the same claims recur rather than being independently evidenced.

## Conclusion

The answer to the query is **209 hand-crafted templates** ([document_2.txt](document_2.txt)). This total is composed of 106 templates for the Freebase evaluation, covering 53 distinct predicates across 500 randomly selected triples, and 103 templates for the in-house power tool domain, covering 67 predicates ([document_2.txt](document_2.txt)). Because the source identifies template construction as the only human labor reported in the work, these 209 templates constitute the entire measured manual effort of the system ([document_2.txt](document_2.txt)).

The deeper significance lies not in the number itself but in its ratio to the underlying data. At roughly 1.74 templates per predicate across the two evaluations, and with 106 Freebase templates servicing 500 triples to produce 991 seed questions, the reported design achieves substantial data coverage from a comparatively small hand-authored template set ([document_2.txt](document_2.txt)). The authors' predicate-anchored approach — binding each template to a knowledge base predicate rather than to individual triples — is the mechanism that keeps the manual figure at 209 rather than at a multiple of the triple count. That said, the 209 total is an aggregate across two heterogeneous domains with unequal template densities, and the combined predicate count of 120 is a derived figure rather than a reported one. The reported evidence supports the conclusion that manual effort scales with predicate coverage, but with only two evaluation domains available, the generalisability of that scaling claim remains to be tested.

## References

Document_2.txt. (n.d.). *[Source document on hand-crafted question template construction for Freebase and in-house power tool domain knowledge bases]* [Unpublished source document]. ([document_2.txt](document_2.txt))