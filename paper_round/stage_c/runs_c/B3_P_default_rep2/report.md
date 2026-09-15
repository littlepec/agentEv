# Hand-Crafted Template Construction in the Evaluated Question-Generation System: A Quantitative Report

## Introduction and Scope

This report addresses a single, precisely bounded question: **how many hand-crafted templates did the authors of the evaluated system have to create?** The answer is not a single number, because the reported work spans two distinct evaluation settings — a general-purpose Freebase evaluation and an in-house, domain-specific power tool knowledge base. The source material reports a separate template count for each setting, plus an aggregate total. Accordingly, this report isolates each figure, verifies the internal arithmetic, and situates the counts within the design logic that produced them.

All figures presented below derive exclusively from the supplied source document, *document_2.txt* ([document_2.txt](document_2.txt)). No external estimates, extrapolations, or third-party benchmarks are introduced, and no claim is made that extends beyond what that source states. Where the source is silent — for example, on the time cost of template authoring or on inter-annotator agreement — that silence is noted rather than filled.

## The Direct Answer: Headline Figures

The reported hand-crafted template counts are as follows.

| Evaluation setting | Predicates in the knowledge base | Hand-crafted templates | Templates per predicate |
|---|---|---|---|
| Freebase (general-purpose) | 53 distinct predicates across 500 triples | **106** | 2.0 (reported as "2 on average") |
| In-house power tool domain | 67 predicates | **103** | ≈ 1.54 (derived) |
| **Aggregate reported total** | — | **209** | — |

The aggregate figure of 209 templates is explicitly reported by the authors as the total number of templates they wrote across both settings ([document_2.txt](document_2.txt)). It is the sum of the two component figures: 106 (Freebase) plus 103 (power tool domain) equals 209 ([document_2.txt](document_2.txt)).

Two interpretive points follow immediately from this table. First, the largest single figure reported for any one setting is 106 templates — the Freebase count. Second, the aggregate manual authoring effort across both evaluations is 209 templates, which is the number most defensibly cited when the question is phrased in the broadest terms ("how many did they have to make, in total?").

## The Freebase Evaluation: 106 Templates for 53 Predicates

### The triple set and its predicate distribution

For the Freebase evaluation, the work drew on **500 randomly selected triples** ([document_2.txt](document_2.txt)). Critically, those 500 triples did not span 500 distinct relations. They shared only **53 distinct predicates** ([document_2.txt](document_2.txt)). This compression — 500 triples collapsing onto 53 predicates — is the structural fact that governs the template count.

### The template-to-predicate ratio

Because the design ties each template to a predicate rather than to an individual triple, the authors produced **106 hand-crafted templates** for the 500 Freebase triples ([document_2.txt](document_2.txt)). The source describes this as an average of **2 templates for each predicate** ([document_2.txt](document_2.txt)). The arithmetic is exact: 106 ÷ 53 = 2.0.

This ratio is the central design decision in the reported system. Had template creation been bound to triples rather than predicates, the manual effort would have scaled with the 500 triples. Instead, it scaled with the 53 predicates, and the per-predicate multiplier was held to two. The source explicitly frames this as a compactness property: the design "ties template creation to predicates, keeping the template set compact relative to the triple set" ([document_2.txt](document_2.txt)).

### Downstream question generation from the Freebase templates

The 106 templates were not an end in themselves; the source reports their downstream yield. Applying the templates to the triples generated **991 seed questions** ([document_2.txt](document_2.txt)). The experiment additionally **retrieved 1529 more questions from Google** ([document_2.txt](document_2.txt)).

Taken together, these two figures indicate a working question pool of 991 + 1529 = 2,520 items associated with the Freebase evaluation. The 1529 Google-retrieved questions are, importantly, *not* template-derived; the source distinguishes them from the template-generated seed questions ([document_2.txt](document_2.txt)). Any accounting of "templates made" must therefore exclude them — they represent retrieval, not manual construction.

The ratio of generated output to manual input is also notable: 991 seed questions from 106 templates is approximately 9.35 questions per template, though the source does not itself frame the figure in these terms ([document_2.txt](document_2.txt)).

### Why the Freebase template set is described as "small"

The source characterizes the system as first constructing "a small set of question templates," with each template associated with a knowledge base predicate ([document_2.txt](document_2.txt)). Within the Freebase evaluation, "small" is operationally defined: 106 templates covering 53 predicates, against a triple set of 500. The template set is roughly one-fifth the size of the triple set.

## The In-House Power Tool Domain: 103 Templates for 67 Predicates

The second evaluation setting is an in-house knowledge base specific to the power tool domain. The source reports **67 predicates** for this knowledge base ([document_2.txt](document_2.txt)). For those 67 predicates, the authors **hand-crafted 103 templates** ([document_2.txt](document_2.txt)).

This yields a derived ratio of approximately 1.54 templates per predicate, materially lower than the 2.0 templates per predicate observed in the Freebase setting. The source does not explain the difference, and this report does not speculate about its cause beyond noting that the two knowledge bases have distinct predicate sets and, in the source's framing, the domain-specific KB "required its own template set" ([document_2.txt](document_2.txt)).

The structural conclusion the source draws from this setting is a scaling one: the Freebase and power tool counts together "show the manual template-building effort scales with predicate coverage in each evaluation" ([document_2.txt](document_2.txt)). In other words, the binding constraint on manual authoring is the predicate inventory, not the triple inventory and not the volume of retrieved questions.

## Aggregate Accounting: 209 Templates in Total

The source reports the combined figure directly: "Together with the 106 Freebase templates, the authors wrote **209 templates in total**" ([document_2.txt](document_2.txt)). It further states that this total is the figure reported in the template-construction experiment ([document_2.txt](document_2.txt)).

The decomposition is shown below.

| Component | Count |
|---|---|
| Freebase templates (53 predicates, 500 triples) | 106 |
| Power tool domain templates (67 predicates) | 103 |
| **Reported total** | **209** |

An important caveat applies to this total, drawn from the source's own framing: the two template sets are not presented as a single unified artefact. The Freebase set and the power tool set serve two different knowledge bases with two different predicate inventories, and the source treats the domain-specific knowledge base as having "its own predicate set" and requiring "its own template set" ([document_2.txt](document_2.txt)). The 209 figure is therefore a sum of reported component counts — an accurate aggregate of manual authoring work performed — rather than a description of one reusable template library of 209 items. My assessment is that the 209 total is the correct headline number for "how many hand-crafted templates did they have to make," provided that the two-setting structure is stated alongside it. Reporting 209 without that qualifier would be technically correct but materially incomplete.

## Template Construction as the Sole Reported Human Labor

A distinct and consequential fact in the source is the scope of manual effort. The paper states that "the only human labor in this work is question template construction" ([document_2.txt](document_2.txt)). The source reiterates this directly: "The template construction therefore is the manual component reported" ([document_2.txt](document_2.txt)).

This matters for interpreting the 106 / 103 / 209 figures. Those numbers are not merely one input among many; under the reported design, they are the *entire* manual annotation budget. Everything else in the pipeline — the generation of 991 seed questions, the retrieval of 1529 additional questions from Google — is characterized as automated or retrieval-based rather than hand-authored ([document_2.txt](document_2.txt)).

The design logic that makes this concentration possible is the predicate–template association. Because "template creation follows the predicates present in the KB" ([document_2.txt](document_2.txt)), the manual cost is bounded by predicate count rather than by triple count. The source states this association as a defining property of the proposed system: "Each template is associated with a predicate in the knowledge base" ([document_2.txt](document_2.txt)).

## Comparative Analysis of the Two Settings

The table below consolidates the reported and derived quantities.

| Metric | Freebase evaluation | Power tool domain | Combined |
|---|---|---|---|
| Triples used | 500 | Not reported | — |
| Distinct predicates | 53 | 67 | — |
| Hand-crafted templates | 106 | 103 | 209 |
| Templates per predicate | 2.0 (as reported) | ≈ 1.54 (derived) | — |
| Template-application output | 991 seed questions | Not reported | — |
| Additional retrieved questions | 1,529 (Google) | Not reported | — |
| Manual labour scope | Template construction only | Template construction only | Template construction only |

Two observations follow. First, the two settings are roughly comparable in scale: 53 versus 67 predicates, and 106 versus 103 templates. Neither setting dominates the aggregate total; the split is close to even. Second, despite the comparable template counts, the Freebase setting covers a substantially larger triple set (500 triples), which is a direct consequence of the 53-predicate compression across those triples ([document_2.txt](document_2.txt)).

## Interpretation and Assessment

Based on the reported figures, my assessment is as follows.

**The answer to the query depends on scope, and the source supports three defensible answers.** If the question concerns the primary, most fully documented evaluation, the answer is **106 templates**. If it concerns the domain-specific deployment, the answer is **103 templates**. If it concerns total manual authoring across both reported evaluations, the answer is **209 templates**. The source reports all three, and the 209 figure is explicitly labelled as the total in the template-construction experiment ([document_2.txt](document_2.txt)).

**The template counts are modest and are structurally constrained by predicates, not data volume.** The system covered 500 Freebase triples with 106 templates because it deliberately indexed template creation to the 53 distinct predicates rather than to the 500 individual triples ([document_2.txt](document_2.txt)). This is a materially different cost model from approaches that would require per-instance authored data, and the source presents it as an intentional compactness property ([document_2.txt](document_2.txt)).

**The absence of reported automation for template creation is a stated limitation, not an omission in the reporting.** The source is explicit that template construction is the only human labour and is therefore the manual component ([document_2.txt](document_2.txt)). Under that design, every new predicate added to a knowledge base implies additional manual template authoring — approximately two templates per predicate in the Freebase setting and roughly 1.5 per predicate in the power tool setting.

**Limitations of the reported evidence should be acknowledged.** The source does not report the time or cost of authoring each template, does not report inter-annotator reliability for template construction, and does not report the template counts for any evaluation beyond the two described. It also does not explain why the per-predicate template ratio differs between the Freebase (2.0) and power tool (≈1.54) settings. These gaps limit any claim about how the 209-template figure would scale to substantially larger predicate inventories.

## Conclusion

The reported hand-crafted template counts are **106 templates for the Freebase evaluation** (covering 53 distinct predicates drawn from 500 randomly selected triples, at an average of 2 templates per predicate) and **103 templates for the in-house power tool domain** (covering 67 predicates), for a reported **total of 209 templates** ([document_2.txt](document_2.txt)). These templates constitute the entirety of the reported human labour in the system; all other components — including the 991 seed questions generated by applying the Freebase templates and the 1,529 additional questions retrieved from Google — are downstream of that manual step ([document_2.txt](document_2.txt)). The design's efficiency claim rests on binding template creation to knowledge base predicates rather than to individual triples, which keeps the manual template set compact relative to the data it covers and makes predicate coverage, rather than triple volume, the governing constraint on authoring effort ([document_2.txt](document_2.txt)).

## References

document_2.txt. (n.d.). *Reported template-construction figures for the Freebase evaluation (500 triples, 53 predicates, 106 templates, 991 seed questions, 1,529 Google-retrieved questions) and the in-house power tool domain knowledge base (67 predicates, 103 templates), with a combined total of 209 templates* [Source document]. ([document_2.txt](document_2.txt))