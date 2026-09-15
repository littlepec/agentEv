# How Many Hand-Crafted Templates Were Required? A Detailed Assessment of Template Construction in Song and Zhao's Knowledge-Base Question Generation System

## Executive Summary

The question of how many hand-crafted question templates were required by Song and Zhao's knowledge-base (KB) question generation system has two defensible answers, depending on which figure is treated as authoritative for the in-house power tool domain. According to the primary paper itself, the authors hand-crafted **106 templates for the 500 Freebase triples** and **163 templates for the 67 predicates in the power tool domain**, implying a combined manual effort of **269 templates** ([Song & Zhao, 2017](document_1.txt)). A third-party research note summarizing the same work states that the Freebase figure is 106 but that the power tool figure is **103 templates**, yielding a combined total of **209 templates** ([Research Note, n.d.](document_2.txt)). The two sources agree exactly on the Freebase count and disagree on the power tool count by 60 templates. This report examines both figures, evaluates the internal evidence, and explains why the primary paper's numbers should generally be preferred while the discrepancy is acknowledged.

## Background: The Functional Role of Hand-Crafted Templates

Understanding the template counts requires first understanding what the templates do. Song and Zhao describe a system whose only reported human labor is question template construction ([Song & Zhao, 2017](document_1.txt)). Each template is associated with a predicate in the knowledge base, and each template contains a transcription of that predicate (for example, `performsActivity = how to`) plus placeholders for the subject (`#X#`) and the object (`#Y#`) ([Song & Zhao, 2017](document_1.txt)). Applying these templates to KB triples produces seed questions, which are then expanded through search engines and filtered for fluency and domain relevance ([Song & Zhao, 2017](document_1.txt)).

This architecture is what makes the template count a meaningful metric rather than a trivial bookkeeping detail. Because template creation is tied to predicates rather than to individual triples or entities, the manual effort scales with predicate coverage rather than with the full size of the knowledge base. The third-party note makes this design logic explicit, observing that "this design ties template creation to predicates, keeping the template set compact relative to the triple set" ([Research Note, n.d.](document_2.txt)). The authors themselves argue that their system does not require a large number of templates because iterative question expansion can produce many questions from a small seed set, and because multiple entities in a KB share the same predicates ([Song & Zhao, 2017](document_1.txt)).

## Template Counts for the Freebase Evaluation

The Freebase experiment is the more thoroughly documented of the two evaluations. The authors randomly selected 500 triples from Freebase, a domain-general knowledge base ([Song & Zhao, 2017](document_1.txt)). For these 500 triples, they hand-crafted **106 templates**, because the triples shared only **53 distinct predicates**, meaning the authors created approximately **two templates per predicate on average** ([Song & Zhao, 2017](document_1.txt)). Applying these templates to the triples generated **991 seed questions**, and a further **1,529 questions** were retrieved from Google ([Song & Zhao, 2017](document_1.txt)).

The third-party note independently reproduces these same Freebase figures — 500 triples, 106 templates, 53 distinct predicates, two templates per predicate on average, 991 seed questions, and 1,529 questions retrieved from Google ([Research Note, n.d.](document_2.txt)). This perfect agreement on the Freebase numbers is important because it establishes that both sources are working from the same underlying paper and that the disagreement is localized to the power tool figures rather than reflecting different versions of the work.

For fluency evaluation, the authors trained a 4-gram language model on Gigaword with Kneser-Ney smoothing and used the averaged language model score to select the top 500 questions for comparison against Serban et al. (2016) ([Song & Zhao, 2017](document_1.txt)). Three native English speakers rated both systems on a four-point scale, and the authors' system scored **3.53 on grammaticality** and **3.31 on naturalness**, compared with **3.36** and **3.14** respectively for the prior state-of-the-art neural machine translation approach ([Song & Zhao, 2017](document_1.txt)).

## Template Counts for the In-House Power Tool Domain

The power tool evaluation differs from the Freebase experiment in both scale and reported template count. The in-house KB contains **67 distinct predicates, 293 distinct subjects, and 279 distinct objects** ([Song & Zhao, 2017](document_1.txt)). Here the two sources diverge:

- The primary paper states that "for the 67 predicates, we hand-crafted **163 templates**" ([Song & Zhao, 2017](document_1.txt)).
- The third-party note states that "For the 67 predicates, the authors hand-crafted **103 templates**" and that, together with the 106 Freebase templates, "the authors wrote **209 templates in total**" ([Research Note, n.d.](document_2.txt)).

This domain produced **12,228 seed questions**, from which **20,000 more questions** were expanded with Google ([Song & Zhao, 2017](document_1.txt)). The expanded questions included examples such as "how to change circular saw blade," "how to sharpen drill bits on bench grinder," and "how to cut a groove in wood without a router" ([Song & Zhao, 2017](document_1.txt)).

## Reconstructing the Total Template Effort

The table below consolidates the reported figures from both sources.

| Evaluation Setting | Distinct Predicates | Templates Reported (Primary Paper) | Templates Reported (Third-Party Note) | Templates per Predicate (Paper) |
|---|---|---|---|---|
| Freebase (500 triples) | 53 | 106 | 106 | 2.00 |
| Power tool domain (in-house KB) | 67 | 163 | 103 | 2.43 |
| **Combined total** | **120** | **269** | **209** | — |

Sources: ([Song & Zhao, 2017](document_1.txt); [Research Note, n.d.](document_2.txt)).

The internal arithmetic is revealing. The Freebase ratio is exactly 2.00 templates per predicate, and the paper states this explicitly as "2 templates for each predicate on average" ([Song & Zhao, 2017](document_1.txt)). If the same two-per-predicate ratio were applied to the 67 power tool predicates, the expected count would be 134 templates — a figure that lies between the paper's 163 and the note's 103. This suggests either that the power tool templates were not constructed at the same average ratio as the Freebase templates, or that one of the two reported values contains a transcription or reporting error.

The third-party note offers a further clue. It asserts that "the paper reports this total" of 209 templates "in the template-construction experiment" ([Research Note, n.d.](document_2.txt)), yet the primary paper as provided states 163 for the power tool domain and never states a combined total of 209 ([Song & Zhao, 2017](document_1.txt)). The note's total of 209 is therefore a derived figure obtained by adding 106 and 103, not a figure quoted verbatim from the paper. This weakens the reliability of the 103 figure relative to the 163 figure, since the latter appears directly in the primary source while the former appears only in a secondary summary that does not reproduce the underlying table.

## Interpretation and Assessment

On the balance of evidence, the most defensible answer to the question posed is that the authors hand-crafted **106 templates for the Freebase evaluation** and **163 templates for the in-house power tool domain**, for a **combined manual effort of 269 templates** ([Song & Zhao, 2017](document_1.txt)). This conclusion rests on the following reasoning:

1. **Primacy of the source.** The paper itself is the primary record of the experimental design, whereas the third-party note is a secondary summary ([Song & Zhao, 2017](document_1.txt); [Research Note, n.d.](document_2.txt)). Where they conflict, the primary record carries greater evidentiary weight.

2. **Internal consistency of the Freebase figures.** Both sources agree on 106 Freebase templates and on the explicit two-per-predicate ratio, which suggests the note's Freebase transcription is accurate and that the discrepancy is isolated to a single number ([Song & Zhao, 2017](document_1.txt); [Research Note, n.d.](document_2.txt)).

3. **Absence of the 209 total in the primary source.** The combined total of 209 appears only in the secondary note and is an arithmetic derivation rather than a reported experimental figure ([Research Note, n.d.](document_2.txt)).

It should be stated plainly, however, that the discrepancy is unresolved by the available documents. A reader who relied solely on the third-party note would reasonably report 209 templates in total, while a reader relying on the primary paper would report 269. The honest position is that the Freebase count of 106 is firm, while the power tool count is contested between 103 and 163.

## Why the Template Count Matters

The template count is not merely descriptive; it is central to the paper's claimed contribution. The authors frame their system as one that "significantly reduces the human effort by leveraging massive web resources" and identify template construction as "the only human labor in this work" ([Song & Zhao, 2017](document_1.txt)). The comparison point is Serban et al. (2016), whose neural machine translation system was trained on **10,000 ⟨triple, question⟩ pairs** in which the question portion was human-generated, requiring a large amount of human effort and offering no guarantee of grammaticality or naturalness ([Song & Zhao, 2017](document_1.txt)).

Against that baseline, a manual investment of 106 or 269 templates to produce 991 seed questions on Freebase — and 12,228 seed questions plus 20,000 expansions in the power tool domain — represents a substantial reduction in annotation burden ([Song & Zhao, 2017](document_1.txt)). The efficiency claim also extends to quality: the authors' questions were rated 3.53 versus 3.36 on grammaticality and 3.31 versus 3.14 on naturalness ([Song & Zhao, 2017](document_1.txt)). Notably, the naturalness scores are lower than the grammaticality scores for both systems, which the authors attribute to naturalness being "a more strict metric since a natural question should also be grammatical" ([Song & Zhao, 2017](document_1.txt)).

The domain-relevance component of the system was validated separately on the web snippet dataset, which contains **10,060 training and 2,280 test snippets across 8 classes**, averaging 18 words per snippet ([Song & Zhao, 2017](document_1.txt)). The authors' domain-relevance method achieved **85.65% precision**, outperforming Phan et al. (2008) at 82.18%, Chen et al. (2011) at 85.31%, and Ma et al. (2015) at 85.48% ([Song & Zhao, 2017](document_1.txt)). Domain relevance is directly connected to template design, because the seed question set serves as the in-domain data against which expanded questions are scored ([Song & Zhao, 2017](document_1.txt)).

## Limitations and Directions

Two caveats should accompany any answer to the template-count question. First, the discrepancy between 103 and 163 for the power tool domain cannot be resolved from the supplied material alone and would require consultation of the published template-construction section of the paper. Second, the templates are described as "hand-crafted" but the reported counts do not specify whether they were built once and reused across predicates or whether each predicate required bespoke phrasing. The Freebase ratio of exactly 2.0 templates per predicate suggests a consistent design convention, whereas the power tool ratios implied by the two competing figures — 1.54 and 2.43 — do not ([Song & Zhao, 2017](document_1.txt); [Research Note, n.d.](document_2.txt)).

The authors also identify a clear limitation of scope: "Our current system only generates questions without answers, leaving automatic answer mining as our future work" ([Song & Zhao, 2017](document_1.txt)).

## Conclusion

The answer to the question of how many hand-crafted templates were required depends on which source is credited. The primary paper reports **106 templates for Freebase** and **163 templates for the power tool domain**, for a total of **269** ([Song & Zhao, 2017](document_1.txt)). The third-party note agrees on 106 for Freebase but reports **103 for the power tool domain**, for a total of **209** ([Research Note, n.d.](document_2.txt)). Given the primacy of the paper over the secondary summary and the observation that the 209 figure appears to be a derivation rather than a directly reported experimental value, the weight of evidence favors **269 templates in total**, with the Freebase component of **106** being unambiguously confirmed. Regardless of which figure is adopted, the central design claim holds: by binding templates to predicates rather than to individual triples, the authors kept manual annotation costs low relative to the 10,000 human-generated question-answer pairs used by the prior state-of-the-art system they benchmarked against ([Song & Zhao, 2017](document_1.txt)).

## References

Research note: Question generation from a knowledge base with web exploration [Third-party research note]. ([document_2.txt](document_2.txt))

Song, L., & Zhao, L. (2017). *Question generation from a knowledge base with web exploration* (arXiv:1610.03807v2). Computer Science Department, University of Rochester; Bosch Research and Technology Center. ([document_1.txt](document_1.txt))