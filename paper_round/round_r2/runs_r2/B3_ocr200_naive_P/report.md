# Hand-Crafted Template Counts in *Question Generation from a Knowledge Base with Web Exploration*

## Introduction

The question of how many hand-crafted templates were required is central to understanding the human-effort profile of the system proposed by Song and Zhao (2017) in *Question Generation from a Knowledge Base with Web Exploration*. The authors explicitly frame template construction as the sole manual component of their pipeline, stating that "The only human labor in this work is the question template construction" ([Song & Zhao, 2017](document_1.txt)). Because that single manual step anchors the entire system, the reported template counts are not incidental statistics but the primary measure of the method's human cost. This report examines the reported figures across the two evaluations conducted by the authors — the domain-general Freebase experiment and the domain-specific in-house power tool experiment — and reconciles the differing counts found in the primary paper and in a third-party research note summarizing it.

## The Function of Hand-Crafted Templates in the System

### Template Structure and Predicate Association

In the proposed framework, a small set of question templates is first constructed for the input knowledge base, and each template is associated with a predicate (Song & Zhao, 2017). The templates are not arbitrary natural-language strings; they consist of a transcription of the predicate in the KB alongside placeholders for the subject and the object. The paper illustrates this with the predicate `performsActivity`, which is transcribed as `how to`, and with placeholders `#X#` for the subject and `#Y#` for the object ([Song & Zhao, 2017](document_1.txt)). Applied to the triple `<jigsaw, performsActivity, CurveCut>`, the template `how to use #X#` yields the seed question `how to use jigsaw` ([Song & Zhao, 2017](document_1.txt)). The design therefore binds template creation directly to the predicate inventory of the knowledge base rather than to its entities or triples (Third-party research note, n.d.).

### Human Labor and Design Rationale

The authors argue that their system does not require a large number of templates for two reasons: first, iterative question expansion can produce a large number of questions even from a relatively small seed set; second, multiple entities in a KB share the same predicates, so one template can service many triples ([Song & Zhao, 2017](document_1.txt)). A third stated advantage is that the web is self-updating, so the system can generate updated questions without re-authoring templates ([Song & Zhao, 2017](document_1.txt)). This predicate-centric economy is the core justification for the specific counts reported below.

## Reported Template Counts

### Freebase Evaluation

For the domain-general evaluation, the authors compared their system against Serban et al. (2016) on 500 randomly selected triples from Freebase. For those 500 triples they hand-crafted **106 templates**, because the triples shared only 53 distinct predicates, which works out to roughly two templates per predicate on average ([Song & Zhao, 2017](document_1.txt)). Applying those templates to the triples generated 991 seed questions, and a further 1,529 questions were retrieved from Google ([Song & Zhao, 2017](document_1.txt)). The third-party research note corroborates the Freebase figure of 106 templates and the figure of 53 distinct predicates, and likewise reports the 991 seed questions and the 1,529 additional retrieved questions (Third-party research note, n.d.).

### In-House Power Tool Domain

For the domain-specific evaluation, the authors used an in-house knowledge base in the power tool domain containing 67 distinct predicates, 293 distinct subjects, and 279 distinct objects ([Song & Zhao, 2017](document_1.txt)). For those 67 predicates, the primary paper states that the authors **hand-crafted 163 templates** ([Song & Zhao, 2017](document_1.txt)). From those templates, 12,228 seed questions were generated, from which 20,000 more questions were expanded using Google ([Song & Zhao, 2017](document_1.txt)).

### A Discrepancy Between the Primary Paper and the Research Note

The third-party research note reports a different count for the power tool domain: it states that the authors hand-crafted **103 templates** for the 67 power tool predicates and that, together with the 106 Freebase templates, **209 templates** were written in total (Third-party research note, n.d.). This conflicts with the primary paper's figure of 163 templates for the same 67 predicates, which would imply a total of **269 templates** across the two evaluations (Song & Zhao, 2017). The discrepancy is material and should be adjudicated in favor of the primary source: the paper itself, not a derived summary, is the authoritative record of how many templates its authors built. The near-transposition of digits (163 versus 103) suggests a transcription error in the secondary note rather than a genuine alternative figure. The tables below present both figures transparently, while the analysis that follows relies on the primary paper unless otherwise noted.

**Table 1. Reported hand-crafted template counts across the two evaluations**

| Evaluation setting | Knowledge base size | Distinct predicates | Templates reported (primary paper) | Templates reported (research note) |
|---|---|---|---|---|
| Freebase (domain-general) | 500 randomly selected triples | 53 | 106 | 106 |
| In-house power tool (domain-specific) | 67 predicates; 293 subjects; 279 objects | 67 | 163 | 103 |
| **Total** | — | 120 (53 + 67) | **269** | **209** |

Sources: ([Song & Zhao, 2017](document_1.txt)); (Third-party research note, n.d.).

**Table 2. Template intensity per predicate**

| Evaluation setting | Distinct predicates | Templates (primary paper) | Templates per predicate | Templates (research note) | Templates per predicate |
|---|---|---|---|---|---|
| Freebase | 53 | 106 | ~2.00 | 106 | ~2.00 |
| Power tool | 67 | 163 | ~2.43 | 103 | ~1.54 |

Sources: ([Song & Zhao, 2017](document_1.txt)); (Third-party research note, n.d.).

## Why the Template Burden Remains Proportionally Small

The reported figures demonstrate that manual effort scales with the number of distinct predicates rather than with the number of triples or entities in the knowledge base. In the Freebase evaluation, 500 triples collapsed to only 53 distinct predicates, so 106 templates covered the entire sample ([Song & Zhao, 2017](document_1.txt)). The research note makes this design economization explicit, observing that because template creation is tied to predicates, the template set is kept compact relative to the triple set (Third-party research note, n.d.). The power tool evaluation reinforces the same pattern: 67 predicates required 163 templates, an average of about 2.4 templates per predicate ([Song & Zhao, 2017](document_1.txt)). Across both evaluations, the authors wrote on the order of two to two-and-a-half templates per distinct predicate, which is why the paper can describe the template set as "small" and argue that the system "does not require a large number of templates" ([Song & Zhao, 2017](document_1.txt)).

It is also worth noting that the Freebase templates were built only for a random sample of 500 triples, not for the entirety of Freebase ([Song & Zhao, 2017](document_1.txt)). The 106-template figure therefore describes the scope of the comparative experiment rather than the full cost of covering the KB. Similarly, the power tool count reflects a single specialized in-house KB with its own predicate set, which the research note emphasizes required its own template set (Third-party research note, n.d.).

## Consequences of the Template Count: Seed Questions and Web Expansion

The template counts translate directly into seed-question volume, which in turn drives the web-expansion stage. In the Freebase experiment, 106 templates applied across 500 triples produced 991 seed questions, and the search engine retrieved 1,529 additional questions ([Song & Zhao, 2017](document_1.txt)). In the power tool experiment, 163 templates produced 12,228 seed questions, from which 20,000 more questions were expanded via Google ([Song & Zhao, 2017](document_1.txt)).

**Table 3. Seed question and expansion volumes by evaluation**

| Evaluation setting | Templates (primary paper) | Seed questions generated | Additional questions from web | Total candidate questions |
|---|---|---|---|---|
| Freebase | 106 | 991 | 1,529 | 2,520 |
| Power tool | 163 | 12,228 | 20,000 | 32,228 |

Sources: ([Song & Zhao, 2017](document_1.txt)). Totals are arithmetic sums of the reported generation and retrieval figures.

These numbers underline the leverage of the template approach: a few hundred manual templates ultimately yielded tens of thousands of candidate questions. The authors' first stated rationale — that iterative expansion produces many questions from few seed questions — is thus empirically borne out by their own results ([Song & Zhao, 2017](document_1.txt)).

## Evaluation Context Supporting the Template Figures

### Freebase Human Ratings

To evaluate fluency and naturalness, the authors trained a 4-gram language model on Gigaword (LDC2011T07) with Kneser-Ney smoothing and selected the top 500 questions by averaged language-model score for comparison with Serban et al. (2016) ([Song & Zhao, 2017](document_1.txt)). Three native English speakers rated both sets on a 4-point scheme ([Song & Zhao, 2017](document_1.txt)). The system's questions were rated 3.53 on grammaticality and 3.31 on naturalness, compared with 3.36 and 3.14 for Serban et al. (2016) ([Song & Zhao, 2017](document_1.txt)). The authors note that naturalness scores are lower than grammaticality scores for both systems because naturalness is the stricter metric ([Song & Zhao, 2017](document_1.txt)).

**Table 4. Human ratings of generated questions (4-point scale)**

| System | Grammaticality | Naturalness |
|---|---|---|
| Serban et al. (2016) | 3.36 | 3.14 |
| Ours (Song & Zhao) | 3.53 | 3.31 |

Source: ([Song & Zhao, 2017](document_1.txt)).

### Domain Relevance on the Web Snippet Dataset

The domain-relevance component (the `REL(q) = cos(v(q), v(D_in))` measure) was validated on a web snippet dataset with 10,060 training and 2,280 test snippets across 8 domains, averaging 18 words per snippet ([Song & Zhao, 2017](document_1.txt)). The method achieved 85.65 precision, surpassing Phan et al. (2008) at 82.18, Chen et al. (2011) at 85.31, and Ma et al. (2015) at 85.48 ([Song & Zhao, 2017](document_1.txt)).

**Table 5. Precision on the web snippet dataset**

| Method | Precision |
|---|---|
| Phan et al. (2008) | 82.18 |
| Chen et al. (2011) | 85.31 |
| Ma et al. (2015) | 85.48 |
| Ours (Song & Zhao) | 85.65 |

Source: ([Song & Zhao, 2017](document_1.txt)).

## Discussion

Taking the primary paper at face value, the answer to the query is that the authors hand-crafted **106 templates for the Freebase evaluation** and **163 templates for the in-house power tool evaluation**, for a combined total of **269 hand-crafted templates** ([Song & Zhao, 2017](document_1.txt)). If the third-party research note's power tool figure of 103 is preferred, the combined total would instead be 209 (Third-party research note, n.d.). The weight of evidence favors the primary source: it is the document in which the authors describe their own experimental procedure in the section on the domain-specific KB evaluation, and it reports the number in a direct statement about the 67 predicates ([Song & Zhao, 2017](document_1.txt)). The research note is explicitly a "third-party" summary (Third-party research note, n.d.), and a derived document is by definition less authoritative than the paper it summarizes.

There is also an internal-consistency argument favoring 163. The Freebase evaluation averaged about two templates per predicate; a figure of 163 for 67 predicates averages about 2.4, which is a plausible extension of the same authoring practice, whereas 103 averages about 1.5 and would represent a marked drop in per-predicate coverage for a domain the authors describe as "highly specialized" ([Song & Zhao, 2017](document_1.txt)). A specialized domain with idiosyncratic predicates would, if anything, be expected to demand at least as much per-predicate template investment as a general-purpose KB, not less.

Regardless of which figure one adopts, the substantive conclusion is unchanged: the manual template effort was on the order of a few hundred templates in total, each tied to a predicate, and this modest manual investment was leveraged into tens of thousands of candidate questions through web search expansion ([Song & Zhao, 2017](document_1.txt)).

## Conclusion

The system in *Question Generation from a Knowledge Base with Web Exploration* depends on hand-crafted, predicate-associated templates as its only human-labor component. The primary paper reports 106 templates for 500 randomly selected Freebase triples spanning 53 distinct predicates, and 163 templates for the 67 predicates of the in-house power tool knowledge base, implying a combined total of 269 hand-crafted templates ([Song & Zhao, 2017](document_1.txt)). A third-party research note instead reports 103 power tool templates and a combined total of 209 (Third-party research note, n.d.). Because the primary paper is the authoritative source and its figures are internally consistent with the observed per-predicate authoring rate, this report treats 106 and 163 — totaling 269 — as the best-supported answer, while documenting the alternative count for completeness. The broader finding is that the manual burden scales with predicate coverage, not with KB size, which is precisely what allows the approach to generate fluent, natural, and domain-relevant questions at low human cost ([Song & Zhao, 2017](document_1.txt)).

## References

Song, L., & Zhao, L. (2017). *Question generation from a knowledge base with web exploration* (arXiv:1610.03807v2). [document_1.txt](document_1.txt)

Third-party research note: *Question generation from a knowledge base with web exploration* [Research note]. (n.d.). [document_2.txt](document_2.txt)