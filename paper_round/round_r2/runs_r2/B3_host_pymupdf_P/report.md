# Hand-Crafted Template Counts in “Question Generation from a Knowledge Base with Web Exploration”

## 1. Introduction

The query asks how many hand-crafted templates the authors of “Question Generation from a Knowledge Base with Web Exploration” had to make. The short answer is that the count depends on which evaluation is being discussed and which source is treated as authoritative. According to the primary paper by Song and Zhao (2017), the authors hand-crafted **106 templates** for the Freebase evaluation involving 500 triples, and **163 templates** for the in-house power tool domain knowledge base (KB) containing 67 distinct predicates ([Song & Zhao, 2017](https://arxiv.org/abs/1610.03807)). Summing those primary-source figures yields **269 templates** across the two reported evaluations. A third-party research note, however, states that the power tool KB used **103 templates** and that the aggregate total was **209 templates**, which is inconsistent with the 163-template figure reported in the primary paper (Third-party research note, n.d.). This report documents both figures, explains the structure of the template-construction task, and assesses which numbers should be treated as most reliable.

The question is significant because template construction is explicitly identified as the only manual component of the system. Song and Zhao (2017) state that “the only human labor in this work is the question template construction,” meaning the template count is the clearest available proxy for the amount of human annotation effort the system requires ([Song & Zhao, 2017](https://arxiv.org/abs/1610.03807)). Understanding that count is therefore central to evaluating the paper’s central claim: that large-scale web resources can replace massive human-labeled datasets in KB-based question generation.

## 2. What Counts as a Template in This System

Before comparing numbers, it is necessary to define what a template is in this framework. A knowledge base is modeled as a directed graph whose nodes are entities and whose edges are relations, or equivalently as a list of triples in the form ⟨subject, predicate, object⟩, where subjects and objects are entities and predicates are relations ([Song & Zhao, 2017](https://arxiv.org/abs/1610.03807)). A question template is constructed per predicate. It consists of a transcription of the predicate into natural-language phrasing—for example, the predicate “performsActivity” is transcribed as “how to”—plus placeholders for the subject (#X#) and the object (#Y#) ([Song & Zhao, 2017](https://arxiv.org/abs/1610.03807)).

This design means template effort scales with the number of distinct predicates in a KB, not with the number of triples. One template can be applied repeatedly across many entities that share the same predicate. For instance, the template “how to use #X#” is constructed for the predicate “performsActivity,” and applying it to the triple ⟨jigsaw, performsActivity, CurveCut⟩ produces the seed question “how to use jigsaw” ([Song & Zhao, 2017](https://arxiv.org/abs/1610.03807)). The same template can then generate questions for other tools that perform other activities, which is why the authors can describe the template set as “small” relative to the KB ([Song & Zhao, 2017](https://arxiv.org/abs/1610.03807)).

## 3. Template Counts for the Freebase Evaluation

### 3.1 Sample and predicate coverage

The Freebase evaluation used 500 randomly selected triples from Freebase, a domain-general KB ([Song & Zhao, 2017](https://arxiv.org/abs/1610.03807)). Those 500 triples shared only **53 distinct predicates**, which determines the minimum number of predicate-level template families required ([Song & Zhao, 2017](https://arxiv.org/abs/1610.03807)). To cover these 53 predicates, the authors hand-crafted **106 templates**, or roughly two templates per predicate on average ([Song & Zhao, 2017](https://arxiv.org/abs/1610.03807)).

### 3.2 The 106 hand-crafted templates

The 106-template figure is stated directly in the experimental section: “For the 500 triples, we hand-crafted 106 templates, as these triples share only 53 distinct predicates (we made 2 templates for each predicate on average)” ([Song & Zhao, 2017](https://arxiv.org/abs/1610.03807)). This is the most precise and best-supported template count in the entire source set, because it is stated in the primary paper and is internally consistent with the reported predicate count.

### 3.3 Downstream yield from the 106 templates

The template count matters because of the seed-question volume it produces. Applying the 106 hand-crafted templates to the 500 Freebase triples generated **991 seed questions** ([Song & Zhao, 2017](https://arxiv.org/abs/1610.03807)). The system then retrieved **1,529 additional questions from Google**, and the top 500 questions were selected using an averaged language-model score derived from a 4-gram language model trained on Gigaword (LDC2011T07) with Kneser-Ney smoothing ([Song & Zhao, 2017](https://arxiv.org/abs/1610.03807)). In other words, 106 human-authored templates ultimately supported a candidate pool of 2,520 questions before selection, illustrating the leverage the authors claim for their approach.

The evaluation itself involved three native English speakers rating fluency and naturalness on a 4-point scale. The system scored 3.53 on grammaticality and 3.31 on naturalness, compared with 3.36 and 3.14 for Serban et al. (2016) ([Song & Zhao, 2017](https://arxiv.org/abs/1610.03807)). These ratings are the empirical justification for the claim that the reduced template effort does not come at the cost of question quality.

## 4. Template Counts for the In-House Power Tool KB

### 4.1 KB composition

The second evaluation used an in-house KB in the power tool domain, containing **67 distinct predicates**, **293 distinct subjects**, and **279 distinct objects** ([Song & Zhao, 2017](https://arxiv.org/abs/1610.03807)). Because templates are built per predicate, the key figure for effort estimation is again the predicate count, 67.

### 4.2 The 163-template figure in the primary source

The primary paper states: “For the 67 predicates, we hand-craft **163 templates**” ([Song & Zhao, 2017](https://arxiv.org/abs/1610.03807)). This yields an average of roughly 2.43 templates per predicate, somewhat higher than the Freebase ratio of approximately 2.0 templates per predicate. That difference is plausible: a specialized domain may require more varied phrasings per predicate than a general-purpose KB, particularly for procedural “how-to” questions in a tool domain.

The paper reports that 12,228 seed questions were generated from these templates, and 20,000 more questions were expanded using Google ([Song & Zhao, 2017](https://arxiv.org/abs/1610.03807)). Example expanded questions include “how to change circular saw blade,” “how to measure lawn mower cutting height,” “how to sharpen drill bits on bench grinder,” and “how to cut a groove in wood without a router” ([Song & Zhao, 2017](https://arxiv.org/abs/1610.03807)).

### 4.3 The 103-template figure in the third-party note

The third-party research note states that “For the 67 predicates, the authors hand-crafted **103 templates**” and that “together with the 106 Freebase templates, the authors wrote **209 templates in total**” (Third-party research note, n.d.). This directly conflicts with the primary source’s 163-template figure and with the arithmetic total of 269 that follows from the primary source.

The discrepancy is material and cannot be resolved from the provided materials alone. What can be said is that the primary paper supplies an explicit in-text number, while the third-party note supplies a different number and a derived aggregate. When a primary source and a secondary note conflict on a specific reported figure, the primary source normally takes precedence, especially when the secondary note presents no independent verification procedure.

## 5. Aggregate Template Effort: 269 Versus 209

The following table summarizes the competing counts.

| Domain / KB | Distinct predicates | Templates per Song and Zhao (2017) | Templates per third-party note |
|---|---|---|---|
| Freebase (500 random triples) | 53 | 106 | 106 |
| In-house power tool KB | 67 | 163 | 103 |
| **Aggregate** | **120** | **269** | **209** |

Under the primary-source figures, the authors wrote **269 hand-crafted templates** across the two reported evaluations. Under the third-party note, the total would be **209**. The Freebase figure of 106 is identical in both sources, so the entire discrepancy is confined to the power tool domain.

There is a further interpretive question about whether “how many templates did they have to make” should be answered as 106 (the Freebase experiment only), 163 (the power tool experiment only), or 269 (the aggregate across both reported evaluations). The most defensible answer depends on scope: 106 is the figure for the primary comparative benchmark against Serban et al. (2016), while 269 is the aggregate human template effort reported across the paper’s two end-to-end evaluations.

## 6. Why So Few Templates? Design Rationale

The authors explicitly justify why the template set can remain small. First, iterative question expansion can produce a large number of questions even from a relatively small number of seed questions, as the experiments demonstrate ([Song & Zhao, 2017](https://arxiv.org/abs/1610.03807)). Second, multiple entities in the KB share the same predicates, so one predicate-level template serves many triples ([Song & Zhao, 2017](https://arxiv.org/abs/1610.03807)). A third stated advantage is that the web is self-updating, so the system can generate updated questions without new templates ([Song & Zhao, 2017](https://arxiv.org/abs/1610.03807)).

This rationale is consistent with the observed ratios. In the Freebase experiment, 106 templates covered 500 triples and produced 991 seed questions before expansion; in the power tool experiment, 163 templates (per the primary source) covered 67 predicates and produced 12,228 seed questions ([Song & Zhao, 2017](https://arxiv.org/abs/1610.03807)). The human-authored template set is therefore a small, predicate-indexed seed that the search-and-selection pipeline amplifies.

## 7. Comparative Human Effort

The template counts are best understood against the baseline the paper critiques. Serban et al. (2016) treated question generation as machine translation and trained a neural machine translation system on **10,000 ⟨triple, question⟩ pairs**, where the question portion was human-generated ([Song & Zhao, 2017](https://arxiv.org/abs/1610.03807)). Song and Zhao (2017) frame their contribution as reducing that human effort by leveraging web resources. Even at the aggregate primary-source figure of 269 templates, the manual component is orders of magnitude smaller than 10,000 human-written questions, though the two quantities are not directly equivalent: templates are reusable schemas, whereas the Serban et al. pairs are fully realized question strings.

The domain-relevance evaluation provides additional context for the system’s efficiency claim. On the web snippet dataset—10,060 training and 2,280 test snippets across 8 classes, averaging 18 words per snippet—the authors’ method achieved **85.65** precision, compared with 82.18 for Phan et al. (2008), 85.31 for Chen et al. (2011), and 85.48 for Ma et al. (2015) ([Song & Zhao, 2017](https://arxiv.org/abs/1610.03807)). This shows that the lightweight, embedding-based relevance filter used to rank expanded questions is competitive with more elaborate topic-modeling approaches, reinforcing the feasibility of the low-template design.

## 8. Reliability and Prioritization of Sources

Two sources are relevant here. The first is the primary research paper by Song and Zhao (2017), an arXiv preprint (arXiv:1610.03807v2, dated 1 February 2017) describing the system, its three experiments, and its numerical results ([Song & Zhao, 2017](https://arxiv.org/abs/1610.03807)). The second is a third-party research note that summarizes the paper and highlights template-construction figures (Third-party research note, n.d.). The third-party note is useful for emphasis and cross-checking, but it contains an internal inconsistency relative to the primary text on the power tool template count, and it asserts that the paper reports a 209-template total even though the primary paper’s stated figures do not sum to 209.

Given this, the appropriate evidentiary weighting is to treat **106** as certain for Freebase, **163** as the primary-source figure for the power tool KB, and **269** as the primary-source aggregate—while noting that the third-party note claims **103** and **209** respectively. Any downstream analysis that depends on the exact power tool template count should flag this discrepancy rather than silently adopting either number.

## 9. Conclusion

The answer to the query is multi-part. For the Freebase evaluation on 500 randomly selected triples sharing 53 distinct predicates, the authors hand-crafted **106 templates**, averaging about two per predicate, which produced 991 seed questions and supported a comparison against Serban et al. (2016) ([Song & Zhao, 2017](https://arxiv.org/abs/1610.03807)). For the in-house power tool domain KB with 67 distinct predicates, the primary paper reports **163 hand-crafted templates** ([Song & Zhao, 2017](https://arxiv.org/abs/1610.03807)), while a third-party note reports **103** (Third-party research note, n.d.). Combining the primary-source figures gives an aggregate of **269 templates** across the two reported evaluations; combining the third-party figures gives **209**. Because template construction is the only human labor the system requires, these counts define the system’s true manual footprint, and the most defensible headline figures are 106 for Freebase and 163 for the power tool KB, with 269 as the primary-source aggregate and the 103/209 figures treated as an unresolved secondary-source discrepancy.

## References

Song, L., & Zhao, L. (2017). *Question generation from a knowledge base with web exploration* (arXiv:1610.03807v2). arXiv. https://arxiv.org/abs/1610.03807

Third-party research note. (n.d.). *Question generation from a knowledge base with web exploration* [Unpublished research note; no persistent locator supplied].