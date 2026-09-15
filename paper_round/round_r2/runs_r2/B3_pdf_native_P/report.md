# How Many Hand-Crafted Templates Were Required? A Detailed Analysis of Template Construction in “Question Generation from a Knowledge Base with Web Exploration”

## Executive Summary

The question of how many hand-crafted templates the authors had to create has a multi-part answer, because template construction in Song and Zhao’s system was performed separately for each knowledge base (KB) evaluated. According to the primary source, the authors hand-crafted **106 templates** for the Freebase evaluation ([Song & Zhao, 2017](https://arxiv.org/abs/1610.03807)) and **163 templates** for the in-house power tool domain evaluation ([Song & Zhao, 2017](https://arxiv.org/abs/1610.03807)). Taken together, this amounts to **269 hand-crafted templates** across the two reported evaluations. A third-party research note in the provided materials states that the power tool effort involved “103 templates” and that “the authors wrote 209 templates in total,” but this conflicts with the primary paper’s explicit figure of 163 ([Third-party Research Note, n.d.](document_2.txt)). Because the original paper is the authoritative source for its own experimental setup, this report treats 106 (Freebase) and 163 (power tool) as the reliable figures, while documenting the discrepancy transparently.

## Introduction and Context

Question generation from a knowledge base is the task of producing natural-language questions related to the domain of an input KB ([Song & Zhao, 2017](https://arxiv.org/abs/1610.03807)). The authors motivate this task by noting that questions support student assessment, coaching, question answering, dialogue interaction, and intelligent tutoring systems ([Song & Zhao, 2017](https://arxiv.org/abs/1610.03807)). Prior work such as Serban et al. (2016) treated question generation as a machine translation problem and trained a neural machine translation system on 10,000 ⟨triple, question⟩ pairs, all of which were human-generated and therefore required a large amount of human effort ([Song & Zhao, 2017](https://arxiv.org/abs/1610.03807)).

Song and Zhao’s central design goal was to reduce that human effort by leveraging massive web resources ([Song & Zhao, 2017](https://arxiv.org/abs/1610.03807)). Their pipeline contains four submodules: question template construction, seed question generation, question expansion, and selection ([Song & Zhao, 2017](https://arxiv.org/abs/1610.03807)). Within this pipeline, the authors state plainly that “the only human labor in this work is the question template construction” ([Song & Zhao, 2017](https://arxiv.org/abs/1610.03807)). The template count is therefore the single most important measure of the manual annotation burden in the entire system.

## The Function and Design of Templates

A template consists of a transcription of a predicate from the KB plus placeholders for the subject (#X#) and the object (#Y#) ([Song & Zhao, 2017](https://arxiv.org/abs/1610.03807)). For example, the predicate `performsActivity` maps to the transcription “how to,” producing the template “how to use #X#” ([Song & Zhao, 2017](https://arxiv.org/abs/1610.03807)). Applying this template to the triple ⟨jigsaw, performsActivity, CurveCut⟩ yields the seed question “how to use jigsaw” ([Song & Zhao, 2017](https://arxiv.org/abs/1610.03807)).

Crucially, each template is associated with a predicate, not with an individual triple ([Song & Zhao, 2017](https://arxiv.org/abs/1610.03807)). This association is what keeps the human effort compact: because many entities share the same predicates, a single template can generate many seed questions. The authors explain that the system does not require a large number of templates for two reasons: (1) iterative question expansion can produce a large number of questions even from a relatively small seed set, and (2) multiple entities in the KB share the same predicates ([Song & Zhao, 2017](https://arxiv.org/abs/1610.03807)).

## Template Counts by Evaluation

### Freebase Evaluation: 106 Templates

For the comparison against Serban et al. (2016), the authors randomly selected 500 triples from Freebase ([Song & Zhao, 2017](https://arxiv.org/abs/1610.03807)). Those triples shared only 53 distinct predicates, so the authors hand-crafted 106 templates — approximately two templates per predicate on average ([Song & Zhao, 2017](https://arxiv.org/abs/1610.03807)). The third-party note corroborates this figure and describes the design as tying “template creation to predicates, keeping the template set compact relative to the triple set” ([Third-party Research Note, n.d.](document_2.txt)).

Applying these 106 templates to the 500 triples produced 991 seed questions, and a further 1,529 questions were retrieved from Google ([Song & Zhao, 2017](https://arxiv.org/abs/1610.03807)). A 4-gram language model trained on Gigaword (LDC2011T07) with Kneser-Ney smoothing was used to select the top 500 questions for human evaluation ([Song & Zhao, 2017](https://arxiv.org/abs/1610.03807)).

### Power Tool Domain Evaluation: 163 Templates

The final experiment ran the end-to-end system on an in-house KB in the power tool domain, which contains 67 distinct predicates, 293 distinct subjects, and 279 distinct objects ([Song & Zhao, 2017](https://arxiv.org/abs/1610.03807)). For those 67 predicates, the paper explicitly states that the authors “hand-craft 163 templates” ([Song & Zhao, 2017](https://arxiv.org/abs/1610.03807)). This produced 12,228 seed questions, from which 20,000 more questions were expanded using Google ([Song & Zhao, 2017](https://arxiv.org/abs/1610.03807)).

The ratio here differs meaningfully from the Freebase case. In Freebase, 53 predicates received 106 templates (2.0 per predicate). In the power tool domain, 67 predicates received 163 templates (approximately 2.43 per predicate). This suggests that domain-specific predicates required denser template coverage to capture specialized phrasings.

## Resolving the Discrepancy in Reported Template Counts

The provided materials contain a direct numerical conflict that must be addressed rather than ignored.

| Evaluation | Predicates | Templates (Primary Source) | Templates (Third-party Note) | Seed Questions |
|---|---|---|---|---|
| Freebase | 53 distinct | 106 | 106 | 991 |
| Power tool domain | 67 distinct | 163 | 103 | 12,228 |
| **Total across evaluations** | — | **269** | **209** | — |

Table: Comparison of template counts reported by the primary paper versus the third-party research note ([Song & Zhao, 2017](https://arxiv.org/abs/1610.03807); [Third-party Research Note, n.d.](document_2.txt)).

The third-party note asserts that “for the 67 predicates, the authors hand-crafted 103 templates” and that “together with the 106 Freebase templates, the authors wrote 209 templates in total” ([Third-party Research Note, n.d.](document_2.txt)). It further claims that “the paper reports this total in the template-construction experiment” ([Third-party Research Note, n.d.](document_2.txt)). However, the primary paper does not contain any statement of a 209-template total; it reports 163 for the power tool domain and does not aggregate across experiments ([Song & Zhao, 2017](https://arxiv.org/abs/1610.03807)).

Three considerations support prioritizing the primary source. First, the original paper is the authoritative record of its own methodology and experimental parameters ([Song & Zhao, 2017](https://arxiv.org/abs/1610.03807)). Second, the paper’s internal consistency — 106 templates for 53 predicates, and 163 templates for 67 predicates — implies a plausible per-predicate density in both cases, whereas 103 templates for 67 predicates would be closer to 1.5 per predicate and less consistent with the paper’s stated practice of making roughly two templates per predicate ([Song & Zhao, 2017](https://arxiv.org/abs/1610.03807)). Third, the third-party note is a secondary summary rather than a primary experimental report, and its claim about what “the paper reports” is demonstrably not present in the paper text provided.

Accordingly, the most defensible answer to the query is: **106 templates for the Freebase evaluation, 163 templates for the power tool domain evaluation, and 269 templates in total across the two reported evaluations.**

## Aggregate Human Effort Across Evaluations

If one aggregates the manual effort reported across both evaluations, the authors constructed 269 templates in total (106 + 163). This is the figure most relevant to a question about total hand-crafted template burden. The number is notable for its smallness relative to the scale of output: 269 templates ultimately contributed to the generation of 991 seed questions plus 1,529 web-retrieved questions in the Freebase experiment, and 12,228 seed questions plus 20,000 expanded questions in the power tool experiment ([Song & Zhao, 2017](https://arxiv.org/abs/1610.03807)).

The efficiency ratio is striking. In the power tool domain, 163 templates yielded 12,228 seed questions, meaning each template generated approximately 75 seed questions on average. In the Freebase experiment, 106 templates yielded 991 seed questions, roughly 9.3 seed questions per template. The much higher yield in the power tool domain reflects the larger number of triples instantiated from the in-house KB’s 293 subjects and 279 objects ([Song & Zhao, 2017](https://arxiv.org/abs/1610.03807)).

## Why the Template Count Remains Manageable

The authors explicitly argue that their system does not require a large number of templates because iterative question expansion can produce many questions from a modest seed set, and because multiple entities share predicates ([Song & Zhao, 2017](https://arxiv.org/abs/1610.03807)). They also claim that their system can easily generate updated questions because “web is self-updating consistently” ([Song & Zhao, 2017](https://arxiv.org/abs/1610.03807)).

This design choice stands in contrast to the approach of Serban et al. (2016), which relied on 10,000 human-generated ⟨triple, question⟩ pairs ([Song & Zhao, 2017](https://arxiv.org/abs/1610.03807)). By shifting the manual burden from question authoring to compact predicate-level template authoring, Song and Zhao reduced the human component to a fraction of the prior state of the art’s annotation requirement ([Song & Zhao, 2017](https://arxiv.org/abs/1610.03807)).

The quality of the resulting questions was validated by three native English speakers on a four-point scale ([Song & Zhao, 2017](https://arxiv.org/abs/1610.03807)). The system’s questions scored 3.53 on grammaticality and 3.31 on naturalness, compared with 3.36 and 3.14 for Serban et al. (2016) ([Song & Zhao, 2017](https://arxiv.org/abs/1610.03807)). The naturalness scores were lower than the grammaticality scores for both systems because naturalness is a stricter metric — a natural question should also be grammatical ([Song & Zhao, 2017](https://arxiv.org/abs/1610.03807)). These results suggest that the relatively small template investment did not come at the cost of output quality; on the contrary, the hand-crafted templates appear to have grounded the generated questions in fluent, web-like phrasing ([Song & Zhao, 2017](https://arxiv.org/abs/1610.03807)).

## Methodological and Practical Implications

Three implications follow from the template counts.

First, **template effort scales with predicate coverage, not with KB size**. The Freebase experiment used 500 triples but only 106 templates because those triples shared 53 predicates ([Song & Zhao, 2017](https://arxiv.org/abs/1610.03807)). The power tool KB had 67 predicates and required 163 templates ([Song & Zhao, 2017](https://arxiv.org/abs/1610.03807)). In both cases, the manual unit of work was the predicate.

Second, **domain specificity raises template density**. The power tool domain required roughly 2.43 templates per predicate, compared with 2.0 per predicate for the domain-general Freebase sample ([Song & Zhao, 2017](https://arxiv.org/abs/1610.03807)). Specialized predicates such as `performsActivity` benefit from multiple surface realizations, and the authors’ practice of making about two templates per predicate on average reflects this ([Song & Zhao, 2017](https://arxiv.org/abs/1610.03807)).

Third, **the web-expansion stage amplifies a small template set**. The power tool system generated 12,228 seed questions from 163 templates and then added 20,000 more questions through Google-based expansion ([Song & Zhao, 2017](https://arxiv.org/abs/1610.03807)). The domain relevance and fluency filters — using a skip-gram model for relevance and a language model for fluency, with thresholds $t_{rel}$ and $t_{flu}$ — control the quality of that amplified set ([Song & Zhao, 2017](https://arxiv.org/abs/1610.03807)). The domain-relevance method itself was validated on a web snippet dataset containing 10,060 training and 2,280 test snippets across 8 classes, achieving 85.65 precision and outperforming Phan et al. (2008) at 82.18, Chen et al. (2011) at 85.31, and Ma et al. (2015) at 85.48 ([Song & Zhao, 2017](https://arxiv.org/abs/1610.03807)).

## Conclusion

The direct answer to the query is that the authors hand-crafted **106 templates** for the Freebase evaluation and **163 templates** for the in-house power tool domain evaluation, for a combined total of **269 hand-crafted templates** across the two reported experiments ([Song & Zhao, 2017](https://arxiv.org/abs/1610.03807)). A third-party note in the provided materials reports 103 power-tool templates and a 209-template total, but this is inconsistent with the primary paper’s explicit statement and with the paper’s stated practice of making roughly two templates per predicate ([Third-party Research Note, n.d.](document_2.txt); [Song & Zhao, 2017](https://arxiv.org/abs/1610.03807)). Given the primacy of the original publication, 106, 163, and 269 are the figures that should be relied upon.

The broader significance is that 269 templates — the only human labor in the system — were sufficient to support the generation of thousands of questions and to outperform a neural machine translation baseline trained on 10,000 human-generated pairs on both grammaticality and naturalness ([Song & Zhao, 2017](https://arxiv.org/abs/1610.03807)). The authors identify automatic answer mining as future work, noting that the current system generates questions without answers ([Song & Zhao, 2017](https://arxiv.org/abs/1610.03807)).

## References

Song, L., & Zhao, L. (2017). *Question generation from a knowledge base with web exploration* (arXiv:1610.03807v2). arXiv. https://arxiv.org/abs/1610.03807

Third-party research note: Question generation from a knowledge base with web exploration. (n.d.). [document_2.txt](document_2.txt).