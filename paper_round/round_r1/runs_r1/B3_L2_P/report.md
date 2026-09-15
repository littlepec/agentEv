# How Many Hand-Crafted Templates Were Required? A Detailed Analysis of Template Construction in *Question Generation from a Knowledge Base with Web Exploration*

## Introduction

Question generation from a knowledge base (KB) is the task of producing natural-language questions that are related to the domain of an input KB, a capability the authors describe as useful for student assessment, coaching, question answering, dialogue interaction, and intelligent tutoring systems ([Song & Zhao, 2016](https://arxiv.org/abs/1610.03807)). The system proposed by Linfeng Song (Computer Science Department, University of Rochester) and Lin Zhao (Bosch Research and Technology Center, Palo Alto) deliberately minimizes human involvement, and the authors state plainly that "the only human labor in this work is the question template construction" ([Song & Zhao, 2016](https://arxiv.org/abs/1610.03807)). Because template authoring is the single manual component of the pipeline, the question of how many templates had to be made is central to evaluating the system's practical cost. This report answers that question directly, distinguishes the figures reported for each experimental setting, flags a numerical discrepancy between the primary paper and a third-party research note, and explains why the reported counts remain modest relative to the size of the KBs involved.

## The Direct Answer in Summary

The primary source reports two distinct, non-overlapping template-building efforts, one for each KB used in evaluation. For the domain-general Freebase evaluation, the authors hand-crafted **106 templates**. For the domain-specific in-house power tool KB, the authors hand-crafted **163 templates**. That yields a combined manual effort of **269 templates** across both settings ([Song & Zhao, 2016](https://arxiv.org/abs/1610.03807)).

A third-party research note summarizing the same work reports **106 templates** for Freebase and **103 templates** for the power tool KB, giving a stated total of **209 templates** ([Third-party research note](document_2.txt)). The two sources therefore agree on the Freebase figure but disagree on the power-tool figure (163 versus 103). The discrepancy and its possible interpretation are analyzed in a dedicated section below.

| Evaluation setting | Knowledge base | Distinct predicates | Templates reported (primary paper) | Templates reported (third-party note) |
|---|---|---|---|---|
| Domain-general | Freebase, 500 randomly selected triples | 53 | 106 | 106 |
| Domain-specific | In-house power tool KB | 67 | 163 | 103 |
| **Combined** | — | — | **269** | **209** |

## Template Construction Methodology

### What a Template Is

Templates in this system are not free-form question strings authored one by one for every triple. Instead, each template consists of a transcription of a KB predicate into natural language, together with placeholders for the subject (`#X#`) and the object (`#Y#`) ([Song & Zhao, 2016](https://arxiv.org/abs/1610.03807)). The canonical example given is the predicate `performsActivity`, which is transcribed as "how to," producing the template "how to use #X#" ([Song & Zhao, 2016](https://arxiv.org/abs/1610.03807)). Applying that template to the triple ⟨jigsaw, performsActivity, CurveCut⟩ yields the seed question "how to use jigsaw" ([Song & Zhao, 2016](https://arxiv.org/abs/1610.03807)).

### Templates Are Tied to Predicates, Not to Triples

Crucially, template creation follows the predicates present in the KB rather than the individual triples. The primary paper states that "a small set of question templates is first constructed such that each template is associated with a predicate," and that "multiple entities in the KB share the same predicates" ([Song & Zhao, 2016](https://arxiv.org/abs/1610.03807)). The third-party note interprets this design correctly when it observes that tying template creation to predicates "keeps the template set compact relative to the triple set" ([Third-party research note](document_2.txt)). This design decision is the primary reason the human template count stays in the low hundreds rather than scaling with the number of triples.

## Template Counts by Evaluation Setting

### The Freebase Evaluation

For the domain-general evaluation, the authors compared their system against a previous state-of-the-art neural machine translation approach on 500 randomly selected triples from Freebase, a domain-general KB ([Song & Zhao, 2016](https://arxiv.org/abs/1610.03807)). Because those 500 triples share only 53 distinct predicates, the authors hand-crafted 106 templates, which the paper describes as "2 templates for each predicate on average" ([Song & Zhao, 2016](https://arxiv.org/abs/1610.03807)). The third-party note reports the identical numbers and confirms the arithmetic: 106 templates covering 53 distinct predicates, at approximately two templates per predicate ([Third-party research note](document_2.txt)).

The scale of the resulting question set demonstrates the leverage gained from predicate-level templating. Applying the 106 templates to the 500 triples generated 991 seed questions, and the experiment retrieved 1,529 additional questions from Google ([Song & Zhao, 2016](https://arxiv.org/abs/1610.03807)). Using an averaged language-model score as the selection index, the top 500 questions were chosen for comparison against the baseline results ([Song & Zhao, 2016](https://arxiv.org/abs/1610.03807)). In other words, 106 manual templates ultimately yielded 991 seed questions and 1,529 web-retrieved candidates in this setting alone.

### The In-House Power Tool Domain Knowledge Base

The third experiment moved to a highly specialized in-house KB in the power tool domain, containing 67 distinct predicates, 293 distinct subjects, and 279 distinct objects ([Song & Zhao, 2016](https://arxiv.org/abs/1610.03807)). For these 67 predicates, the primary paper states that the authors "hand-craft 163 templates" ([Song & Zhao, 2016](https://arxiv.org/abs/1610.03807)). This corresponds to roughly 2.43 templates per predicate. The third-party note, by contrast, states that "for the 67 predicates, the authors hand-crafted 103 templates," which corresponds to roughly 1.54 templates per predicate ([Third-party research note](document_2.txt)).

The downstream yield in this setting was substantial. From the seed question set of 12,228 questions, an additional 20,000 questions were expanded via Google, and the sampled outputs — including "how to change circular saw blade," "how to measure lawn mower cutting height," "how to sharpen drill bits on bench grinder," and "how does an oscillating multi tool work" — were reported as grammatical and domain-relevant ([Song & Zhao, 2016](https://arxiv.org/abs/1610.03807)).

### Aggregate Totals

If the primary paper's figures are taken at face value, the total manual template effort across both evaluations is **269 templates** (106 + 163). If the third-party note's power-tool figure is taken instead, the total is **209 templates** (106 + 103), which is the sum that note explicitly reports ([Third-party research note](document_2.txt)). Both sources agree that the Freebase effort accounts for 106 of these templates, and that the only human labor in the entire system is template construction ([Song & Zhao, 2016](https://arxiv.org/abs/1610.03807); [Third-party research note](document_2.txt)).

## Resolving the Reported Discrepancy

The conflict between 163 and 103 templates for the power tool KB cannot be resolved from the information provided, but the relative reliability of the two sources can be assessed. The primary paper is the direct source of the design description, the examples, and the experimental protocol; it states unambiguously that 163 templates were hand-crafted for the 67 predicates ([Song & Zhao, 2016](https://arxiv.org/abs/1610.03807)). The third-party note is a secondary summary that also contains an internal inconsistency: it reports 103 templates for the power tool KB, but then asserts that "the paper reports this total in the template-construction experiment" while summing 106 + 103 = 209 ([Third-party research note](document_2.txt)). Since the note's own arithmetic depends on its 103 figure, and since the note is one step removed from the underlying research, the primary paper's figure of 163 should be treated as the more reliable data point, with the 103 figure treated as a possible transcription or summarization error in the secondary note. Regardless of which figure is adopted, the reported magnitude of the manual effort remains on the order of one to two hundred templates per evaluation setting — a low number given the thousands of questions produced.

## Why the Manual Burden Remains Small

The authors explicitly justify why their system "does not require a large number of templates," offering two reasons: first, iterative question expansion can produce a large number of questions even from a relatively small number of seed questions; second, multiple entities in the KB share the same predicates ([Song & Zhao, 2016](https://arxiv.org/abs/1610.03807)). Both claims are supported by the experiment: 106 templates applied to 500 Freebase triples produced 991 seed questions and 1,529 web-retrieved candidates, while 163 templates (per the primary paper) applied to a 67-predicate KB produced 12,228 seed questions and 20,000 expanded questions ([Song & Zhao, 2016](https://arxiv.org/abs/1610.03807)).

A further advantage the authors claim is that the system can generate updated questions because "web is self-updating consistently" ([Song & Zhao, 2016](https://arxiv.org/abs/1610.03807)). This means the manual template asset does not need to be re-authored as language usage drifts; it only needs to cover the KB's predicates, while the web-search expansion step supplies fresh formulations.

## Context and Comparative Significance

The template counts are best understood against the alternative paradigm the paper criticizes. Previous work such as Serban et al. (2016) treated question generation as a machine translation problem and trained a neural machine translation system on 10,000 ⟨triple, question⟩ pairs ([Song & Zhao, 2016](https://arxiv.org/abs/1610.03807)). Critically, "the question part of the 10,000 pairs are human generated, which requires a large amount of human effort" ([Song & Zhao, 2016](https://arxiv.org/abs/1610.03807)). Against that backdrop, a few hundred human-authored templates is a small manual footprint, and it constitutes the entirety of the system's human labor ([Song & Zhao, 2016](https://arxiv.org/abs/1610.03807)).

The empirical payoff is also documented. Evaluated by three native English speakers on a 4-point scale, the system's questions scored 3.53 on grammaticality and 3.31 on naturalness, compared with 3.36 and 3.14 for the baseline ([Song & Zhao, 2016](https://arxiv.org/abs/1610.03807)). On the web snippet dataset for short-document domain classification, the system's embedding-based domain-relevance method achieved 85.65 precision, outperforming prior methods at 85.48, 85.31, and 82.18 ([Song & Zhao, 2016](https://arxiv.org/abs/1610.03807)).

## Implications and Limitations

Three limitations of the template-based approach deserve note. First, the templates must be authored per KB, so the manual cost is repeated for each new domain: the Freebase evaluation's 106 templates and the power tool KB's 163 templates were separate, non-shared assets, since each KB has its own predicate inventory ([Song & Zhao, 2016](https://arxiv.org/abs/1610.03807)). Second, the current system "only generates questions without answers," leaving automatic answer mining as future work ([Song & Zhao, 2016](https://arxiv.org/abs/1610.03807)). Third, the web expansion step introduces noise — the paper notes that domain relevance "drops significantly as the iteration goes on," which is why relevance and fluency thresholds are applied ([Song & Zhao, 2016](https://arxiv.org/abs/1610.03807)). The template count is therefore the floor, not the ceiling, of the system's operating cost.

## Conclusion

The answer to the question depends on which evaluation setting is meant, and on which source is treated as authoritative. For the domain-general Freebase experiment, the answer is unambiguous: **106 hand-crafted templates** covering 53 distinct predicates ([Song & Zhao, 2016](https://arxiv.org/abs/1610.03807)). For the domain-specific power tool KB, the primary paper reports **163 templates** for 67 predicates, while a third-party research note reports **103** ([Song & Zhao, 2016](https://arxiv.org/abs/1610.03807); [Third-party research note](document_2.txt)). The aggregate total is therefore either **269** (106 + 163, per the primary paper) or **209** (106 + 103, per the secondary note). Given the primary paper's direct authorship of the experiments and the secondary note's internally inconsistent arithmetic, the 269 total is the better-supported figure. In either case, the essential finding stands: by tying each template to a KB predicate rather than to individual triples, the system reduces a task that previously required 10,000 human-generated question–answer pairs to a few hundred manually authored templates — the sole human labor in the pipeline — while still producing thousands of fluent, domain-relevant questions ([Song & Zhao, 2016](https://arxiv.org/abs/1610.03807)).

## References

Song, L., & Zhao, L. (2016). *Question generation from a knowledge base with web exploration* (arXiv:1610.03807). https://arxiv.org/abs/1610.03807

Third-party research note: Question Generation from a Knowledge Base with Web Exploration (document_2.txt).