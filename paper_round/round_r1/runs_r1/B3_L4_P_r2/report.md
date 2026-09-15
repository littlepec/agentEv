# Hand-Crafted Template Requirements in “Question Generation from a Knowledge Base with Web Exploration”

## Introduction

The research paper “Question Generation from a Knowledge Base with Web Exploration” by Linfeng Song and Lin Zhao presents a system that generates natural language questions from structured knowledge bases (KBs). A central design choice of the system is the use of hand-crafted question templates, which the authors identify as the only human labor required by their approach ([Song & Zhao, n.d.](document_1.txt)). This report addresses the specific query: **How many hand-crafted templates did they have to make?** The answer depends on which evaluation setting is considered—the domain-general Freebase evaluation or the domain-specific in-house power tool knowledge base. Additionally, a third-party research note provides conflicting figures for the power tool domain, which necessitates a careful comparison of sources ([Third-party research note, n.d.](document_2.txt)). The following sections detail the template counts, the methodology behind them, and the implications for the system’s human effort.

## The Role of Hand-Crafted Templates in the System

The proposed system operates on a knowledge base represented as a directed graph or a list of triples in the format of ⟨subject, predicate, object⟩ ([Song & Zhao, n.d.](document_1.txt)). The authors’ method begins with a small set of question templates that are hand-crafted based on the predicates present in the KB. Each template is associated with a specific predicate and consists of a transcription of that predicate into natural language (for example, `performsActivity` becomes “how to”) along with placeholders for the subject (`#X#`) and the object (`#Y#`) ([Song & Zhao, n.d.](document_1.txt)). For instance, the template “how to use #X#” is constructed for the predicate `performsActivity`, and applying it to the triple ⟨jigsaw, performsActivity, CurveCut⟩ yields the seed question “how to use jigsaw” ([Song & Zhao, n.d.](document_1.txt)).

The authors emphasize that “the only human labor in this work is the question template construction” ([Song & Zhao, n.d.](document_1.txt)). This makes the number of templates a critical measure of the manual effort required. The system does not require a large number of templates because iterative question expansion through a search engine can produce many questions even from a small seed set, and because multiple entities in the KB share the same predicates ([Song & Zhao, n.d.](document_1.txt)). Nevertheless, the exact count of templates varies by evaluation domain.

## Template Count for the Freebase Evaluation

In the first experiment, the authors compare their system with a previous state-of-the-art method on 500 randomly selected triples from Freebase, a domain-general knowledge base ([Song & Zhao, n.d.](document_1.txt)). For these 500 triples, the authors hand-crafted **106 templates** ([Song & Zhao, n.d.](document_1.txt)). This number is directly tied to the predicates present in the sample: the 500 triples share only 53 distinct predicates, so the authors made an average of 2 templates for each predicate ([Song & Zhao, n.d.](document_1.txt)). Applying these 106 templates to the triples generated 991 seed questions, and an additional 1,529 questions were retrieved from Google ([Song & Zhao, n.d.](document_1.txt)). This demonstrates that a relatively compact template set can seed a much larger question set.

The third-party research note corroborates this figure: “The paper reports 106 hand-crafted templates for those 500 Freebase triples” ([Third-party research note, n.d.](document_2.txt)). Thus, there is consensus across both sources regarding the Freebase template count.

## Template Count for the In-House Power Tool Domain

The second evaluation uses an in-house knowledge base in the power tool domain. This KB contains 67 distinct predicates, 293 distinct subjects, and 279 distinct objects ([Song & Zhao, n.d.](document_1.txt)). For these 67 predicates, the original paper states: “we hand-craft **163 templates**” ([Song & Zhao, n.d.](document_1.txt)). From these templates, the system generated 12,228 seed questions, and 20,000 more questions were expanded with Google ([Song & Zhao, n.d.](document_1.txt)).

However, the third-party research note reports a different figure: “For the 67 predicates, the authors hand-crafted **103 templates**” ([Third-party research note, n.d.](document_2.txt)). The note further states that together with the 106 Freebase templates, the authors wrote **209 templates in total** ([Third-party research note, n.d.](document_2.txt)). This conflicts with the original paper’s statement of 163 templates for the power tool domain alone.

### Discrepancy Analysis

The discrepancy is significant. If the original paper’s figure of 163 is correct, the total across both evaluations would be 106 + 163 = **269 templates**. If the third-party note’s figure of 103 is correct, the total would be 106 + 103 = **209 templates**. The third-party note explicitly claims that “the paper reports this total in the template-construction experiment” ([Third-party research note, n.d.](document_2.txt)), but the original paper does not provide such a total; it only provides the separate counts of 106 and 163 ([Song & Zhao, n.d.](document_1.txt)).

Given that the original paper is the primary source and the third-party note is a secondary summary, the original paper’s figure of 163 for the power tool domain should be given greater weight. The discrepancy may stem from a typographical error, an OCR misreading, or a transcription mistake in the third-party note. For instance, “163” could have been misread as “103” if the “6” was confused with a “0” or if the text was garbled. The original paper’s content is internally consistent: it reports 67 predicates and 163 templates, which yields approximately 2.43 templates per predicate. The third-party note’s 103 templates would yield only about 1.54 templates per predicate, which is lower than the average of 2 templates per predicate used in the Freebase evaluation ([Song & Zhao, n.d.](document_1.txt)). While not impossible, the original paper’s higher ratio aligns better with the stated practice of creating multiple templates per predicate when needed.

## Summary of Template Counts

The following table consolidates the reported figures from both sources.

| Evaluation Setting | Distinct Predicates | Hand-Crafted Templates (Original Paper) | Hand-Crafted Templates (Third-Party Note) | Source |
|---------------------|---------------------|------------------------------------------|--------------------------------------------|--------|
| Freebase (500 triples) | 53 | 106 | 106 | ([Song & Zhao, n.d.](document_1.txt); [Third-party research note, n.d.](document_2.txt)) |
| In-house power tool KB | 67 | 163 | 103 | ([Song & Zhao, n.d.](document_1.txt); [Third-party research note, n.d.](document_2.txt)) |
| **Total across both** | — | **269** | **209** | Calculated from above |

## Implications of the Template Counts

The number of hand-crafted templates directly reflects the manual effort required by the system. For the Freebase evaluation, 106 templates were sufficient to cover 53 predicates and generate nearly 1,000 seed questions, which were then expanded to over 2,500 candidates ([Song & Zhao, n.d.](document_1.txt)). For the power tool domain, 163 templates covered 67 predicates and produced over 12,000 seed questions, expanding to more than 32,000 candidates ([Song & Zhao, n.d.](document_1.txt)). This demonstrates that the template construction effort scales with the number of distinct predicates rather than the number of triples or entities. The authors explicitly note that “multiple entities in the KB share the same predicates,” which reduces the template burden ([Song & Zhao, n.d.](document_1.txt)).

The system’s reliance on web exploration also means that the templates do not need to encode every possible question phrasing. Instead, the seed questions are used as search queries to retrieve related questions from a search engine, and a selection step filters candidates by fluency and domain relevance ([Song & Zhao, n.d.](document_1.txt)). This architecture allows the authors to keep the template set relatively small while still achieving high-quality question generation. Human graders rated the generated questions as more grammatical (3.53 vs. 3.36) and more natural (3.31 vs. 3.14) than those from a prior neural machine translation approach ([Song & Zhao, n.d.](document_1.txt)). The domain relevance evaluation method also outperformed previous methods with a precision of 85.65% on a web snippet dataset ([Song & Zhao, n.d.](document_1.txt)).

## Conclusion

The query “How many hand-crafted templates did they have to make?” can be answered as follows. According to the original paper, the authors hand-crafted **106 templates** for the Freebase evaluation and **163 templates** for the in-house power tool domain, for a total of **269 templates** across both evaluations ([Song & Zhao, n.d.](document_1.txt)). A third-party research note reports 103 templates for the power tool domain and a total of 209 templates, but this conflicts with the primary source and likely contains an error ([Third-party research note, n.d.](document_2.txt)). Given the reliability of the original paper, the most defensible answer is that the authors made **106 templates for Freebase and 163 for the power tool KB, totaling 269 hand-crafted templates**. This modest manual effort enabled the generation of thousands of fluent and domain-relevant questions, underscoring the efficiency of the proposed web-exploration approach.

## References

Song, L., & Zhao, L. (n.d.). *Question generation from a knowledge base with web exploration*. [document_1.txt](document_1.txt).

Third-party research note. (n.d.). *Question generation from a knowledge base with web exploration*. [document_2.txt](document_2.txt).