# How Many Hand-Crafted Templates Were Made? A Detailed Analysis of Song and Zhao's Question Generation System

## Summary of the Direct Answer

The number of hand-crafted templates in Song and Zhao's question generation system depends on which knowledge base (KB) is being evaluated. In the Freebase experiment, the authors made 106 hand-crafted templates for 500 randomly selected triples ([Song & Zhao, 2016](document_1.txt)). In the in-house power tool domain experiment, the primary paper reports 163 hand-crafted templates for 67 distinct predicates ([Song & Zhao, 2016](document_1.txt)). Therefore, across the two reported evaluations, the total is 269 templates: 106 + 163 = 269 ([Song & Zhao, 2016](document_1.txt)). A third-party research note instead claims 103 power-tool templates and a total of 209 templates, but that figure conflicts with the primary source and should be treated as less reliable ([Third-Party Research Note, n.d.](document_2.txt)). If the question is limited to the Freebase evaluation, the answer is 106; if it is limited to the power tool KB, the primary-source answer is 163.

My assessment is that the most defensible answer is 269 hand-crafted templates across the two evaluations reported in the primary paper, with 106 for Freebase and 163 for the power tool domain ([Song & Zhao, 2016](document_1.txt)). The 209 total in the third-party note appears to be based on a mistaken or inconsistent reading of the power-tool template count, and it should not override the primary paper's explicit statement ([Third-Party Research Note, n.d.](document_2.txt)).

## Why the Template Count Matters

Question generation from a knowledge base is the task of generating questions related to the domain of an input KB ([Song & Zhao, 2016](document_1.txt)). Song and Zhao propose a system that generates fluent and natural questions from a KB while significantly reducing human effort by leveraging massive web resources ([Song & Zhao, 2016](document_1.txt)). The system first generates a seed question set by applying a small number of hand-crafted templates to the input KB, then retrieves more questions by iteratively using already-obtained questions as search queries in a standard search engine, and finally selects questions by estimating fluency and domain relevance ([Song & Zhao, 2016](document_1.txt)).

The authors state that the only human labor in their work is question template construction ([Song & Zhao, 2016](document_1.txt)). This makes the number of hand-crafted templates the central measure of manual effort in the system. Unlike previous work that relies on massive human-labeled data, such as training a neural machine translation system with 10,000 ⟨triple, question⟩ pairs, Song and Zhao's approach requires only a compact template set ([Song & Zhao, 2016](document_1.txt)). Consequently, determining exactly how many templates were made is not a trivial detail; it is the key quantity that supports the paper's claim of reduced human effort.

## How Templates Are Defined and Applied

In Song and Zhao's framework, a KB can be viewed as a directed graph in which nodes are entities and edges are relations, or as a list of triples in the format ⟨subject, predicate, object⟩ ([Song & Zhao, 2016](document_1.txt)). The system contains sub-modules for question template construction, seed question generation, question expansion, and selection ([Song & Zhao, 2016](document_1.txt)). Given an input KB, a small set of question templates is first constructed such that each template is associated with a predicate ([Song & Zhao, 2016](document_1.txt)). These templates consist of a transcription of the predicate in the KB and placeholders for the subject (#X#) and the object (#Y#) ([Song & Zhao, 2016](document_1.txt)). For example, the predicate "performsActivity" can be transcribed as "how to," and the template "how to use #X#" can be applied to the triple ⟨jigsaw, performsActivity, CurveCut⟩ to generate the seed question "how to use jigsaw" ([Song & Zhao, 2016](document_1.txt)).

This design explains why the template count is tied to predicates rather than to individual triples or entities. Multiple entities in the KB can share the same predicate, so a single template can produce many seed questions ([Song & Zhao, 2016](document_1.txt)). The authors also note that the iterative question expansion can produce a large number of questions even with a relatively small number of seed questions, as seen in the experiments ([Song & Zhao, 2016](document_1.txt)).

## Freebase Evaluation: 106 Hand-Crafted Templates

The Freebase evaluation is the first experiment in which the authors quantitatively compare their end-to-end system with a previous state-of-the-art method ([Song & Zhao, 2016](document_1.txt)). The evaluation uses 500 randomly selected triples from Freebase ([Song & Zhao, 2016](document_1.txt)). For those 500 triples, the authors hand-crafted 106 templates ([Song & Zhao, 2016](document_1.txt)). The reason for this relatively compact set is that the 500 triples share only 53 distinct predicates, and the authors made 2 templates for each predicate on average ([Song & Zhao, 2016](document_1.txt)). Applying the templates to the triples generated 991 seed questions, and the experiment retrieved 1,529 more questions from Google ([Song & Zhao, 2016](document_1.txt)).

To evaluate fluency, the authors trained a 4-gram language model on Gigaword with Kneser-Ney smoothing ([Song & Zhao, 2016](document_1.txt)). Using the averaged language model score as an index, the top 500 questions were selected for comparison with the baseline ([Song & Zhao, 2016](document_1.txt)). Three native English speakers evaluated fluency and naturalness on a 4-point scheme where 4 is best ([Song & Zhao, 2016](document_1.txt)). The authors' system received an average grammaticality score of 3.53 and a naturalness score of 3.31, compared with 3.36 and 3.14 for the baseline ([Song & Zhao, 2016](document_1.txt)). These results support the claim that 106 templates were sufficient to produce high-quality questions for the Freebase evaluation.

### Freebase Template Count at a Glance

| Freebase evaluation component | Reported figure |
|---|---|
| Randomly selected triples | 500 |
| Distinct predicates | 53 |
| Hand-crafted templates | 106 |
| Average templates per predicate | 2 |
| Seed questions generated | 991 |
| Additional questions retrieved from Google | 1,529 |
| Questions selected for human evaluation | Top 500 |

## In-House Power Tool Domain: 163 Hand-Crafted Templates in the Primary Source

The third experiment is on the authors' in-house KB in the power tool domain ([Song & Zhao, 2016](document_1.txt)). This KB contains 67 distinct predicates, 293 distinct subjects, and 279 distinct objects ([Song & Zhao, 2016](document_1.txt)). For the 67 predicates, the authors hand-craft 163 templates ([Song & Zhao, 2016](document_1.txt)). They use the same language model as in the first experiment and learn a skip-gram model on Wikipedia for evaluating domain relevance ([Song & Zhao, 2016](document_1.txt)). The system generates 12,228 seed questions, from which 20,000 more questions are expanded with Google ([Song & Zhao, 2016](document_1.txt)).

This is the only place in the primary paper where a second concrete template count is given. The Freebase count is 106, and the power tool count is 163 ([Song & Zhao, 2016](document_1.txt)). The power tool KB has more distinct predicates than the Freebase subset (67 vs. 53), and the authors created more templates for it (163 vs. 106) ([Song & Zhao, 2016](document_1.txt)). This pattern is consistent with the paper's design principle that template creation follows the predicates present in the KB ([Song & Zhao, 2016](document_1.txt)).

### Power Tool Domain Template Count at a Glance

| Power tool KB component | Reported figure |
|---|---|
| Distinct predicates | 67 |
| Distinct subjects | 293 |
| Distinct objects | 279 |
| Hand-crafted templates (primary source) | 163 |
| Seed questions generated | 12,228 |
| Additional questions expanded with Google | 20,000 |
| Example expanded questions | "how to change circular saw blade," "how to cut a groove in wood without a router," "do i need a hammer drill" |

## The Discrepancy: Third-Party Note's 103 and 209 Figures

The third-party research note states that, for the in-house power tool domain KB, the paper reports 67 predicates and that the authors hand-crafted 103 templates ([Third-Party Research Note, n.d.](document_2.txt)). It further states that, together with the 106 Freebase templates, the authors wrote 209 templates in total ([Third-Party Research Note, n.d.](document_2.txt)). This directly conflicts with the primary paper's statement that the authors hand-craft 163 templates for the 67 predicates ([Song & Zhao, 2016](document_1.txt)).

There are several reasons to prefer the primary-source figure of 163 over the third-party note's 103. First, the primary paper is the original source and provides the number in the context of the experiment itself ([Song & Zhao, 2016](document_1.txt)). Second, the third-party note is explicitly described as a research note, not as the original paper, and it does not explain the discrepancy ([Third-Party Research Note, n.d.](document_2.txt)). Third, the arithmetic in the primary source is internally consistent: 106 templates for 53 predicates yields 2.0 templates per predicate, while 163 templates for 67 predicates yields approximately 2.43 templates per predicate ([Song & Zhao, 2016](document_1.txt)). A figure of 103 templates for 67 predicates would yield only about 1.54 templates per predicate, which is lower than the Freebase average despite the power tool KB having more predicates and being described as highly specialized ([Song & Zhao, 2016](document_1.txt); [Third-Party Research Note, n.d.](document_2.txt)). That makes the 103 figure less plausible on its face.

Therefore, my concrete opinion is that the 209 total in the third-party note is unreliable. It likely results from a transcription or extraction error in which "163" was misread as "103" ([Third-Party Research Note, n.d.](document_2.txt)). The primary paper's explicit count should govern: 106 Freebase templates and 163 power tool templates ([Song & Zhao, 2016](document_1.txt)).

## Total Hand-Crafted Templates Across Reported Evaluations

If one aggregates the two template counts explicitly reported in the primary paper, the total is:

106 Freebase templates + 163 power tool templates = 269 hand-crafted templates ([Song & Zhao, 2016](document_1.txt)).

This total does not include any templates that might have been created for other, unreported KBs. It also does not include templates that might be reused across KBs, because the paper treats the Freebase and power tool evaluations as separate settings with their own predicate sets ([Song & Zhao, 2016](document_1.txt)). The third-party note's alternative total of 209 is based on the disputed 103 figure and is not supported by the primary text ([Third-Party Research Note, n.d.](document_2.txt)).

### Comparison of Primary and Third-Party Template Counts

| Evaluation / KB | Distinct predicates | Templates (primary source) | Templates (third-party note) | Templates per predicate (primary) |
|---|---:|---:|---:|---:|
| Freebase (500 triples) | 53 | 106 | 106 | 2.00 |
| In-house power tool domain | 67 | 163 | 103 | 2.43 |
| Total across reported evaluations | 120 predicate slots | 269 | 209 | — |

The table shows that only the power tool count is disputed. Both sources agree that the Freebase evaluation used 106 templates ([Song & Zhao, 2016](document_1.txt); [Third-Party Research Note, n.d.](document_2.txt)). The disagreement is entirely about whether the power tool KB required 163 or 103 templates ([Song & Zhao, 2016](document_1.txt); [Third-Party Research Note, n.d.](document_2.txt)). Because the primary paper states 163, the total should be 269 unless new evidence emerges.

## Why the Number of Templates Is Relatively Small

The authors explicitly argue that their system does not require a large number of templates for two reasons: iterative question expansion can produce a large number of questions even with a relatively small number of seed questions, and multiple entities in the KB share the same predicates ([Song & Zhao, 2016](document_1.txt)). Another advantage is that the system can easily generate updated questions because the web is self-updating ([Song & Zhao, 2016](document_1.txt)). These design choices explain how 106 templates can support 500 Freebase triples and how 163 templates can support 67 power tool predicates ([Song & Zhao, 2016](document_1.txt)).

The paper also notes that the only human labor is question template construction, which means the template count is the primary measure of manual annotation cost ([Song & Zhao, 2016](document_1.txt)). Compared with prior work that trained a neural machine translation system on 10,000 human-generated ⟨triple, question⟩ pairs, the template-based approach reduces human effort substantially ([Song & Zhao, 2016](document_1.txt)). The Freebase evaluation generated 991 seed questions from 106 templates, and the power tool evaluation generated 12,228 seed questions from 163 templates ([Song & Zhao, 2016](document_1.txt)). These ratios demonstrate the leverage that predicate-level templates provide.

## Implications for Human Effort and System Design

The template counts have direct implications for the practicality of question generation from KBs. In the Freebase setting, 106 templates were sufficient to cover 53 distinct predicates and 500 triples ([Song & Zhao, 2016](document_1.txt)). In the power tool setting, 163 templates covered 67 predicates, 293 subjects, and 279 objects ([Song & Zhao, 2016](document_1.txt)). The authors also report that most expanded questions in the power tool domain were grammatical, relevant, and informative, with examples such as "how to change circular saw blade," "how to sharpen drill bits on bench grinder," and "how to cut a groove in wood without a router" ([Song & Zhao, 2016](document_1.txt)). The system also generated complex questions beyond simple factoid questions ([Song & Zhao, 2016](document_1.txt)).

On the domain-relevance evaluation, the authors' method achieved a precision of 85.65 on the web snippet dataset, outperforming prior methods with scores of 82.18, 85.31, and 85.48 ([Song & Zhao, 2016](document_1.txt)). This result supports the effectiveness of the selection component that filters expanded questions by fluency and domain relevance ([Song & Zhao, 2016](document_1.txt)). Together with the template counts, these results indicate that a relatively small hand-crafted template set can be paired with web exploration and automatic selection to produce high-quality questions at scale ([Song & Zhao, 2016](document_1.txt)).

## Conclusion

The most reliable answer to the question "How many hand-crafted templates did they have to make?" is not a single number without context. Based on the primary paper, the authors made 106 hand-crafted templates for the Freebase evaluation and 163 hand-crafted templates for the in-house power tool domain KB ([Song & Zhao, 2016](document_1.txt)). Across those two reported evaluations, the total is 269 templates ([Song & Zhao, 2016](document_1.txt)). The third-party note's alternative figures of 103 power-tool templates and 209 total templates conflict with the primary source and should not be treated as authoritative ([Third-Party Research Note, n.d.](document_2.txt)).

If the query is intended to ask only about Freebase, the answer is 106 ([Song & Zhao, 2016](document_1.txt)). If it is intended to ask only about the power tool KB, the primary-source answer is 163 ([Song & Zhao, 2016](document_1.txt)). If it is intended to ask about the full set of templates reported across the paper's experiments, the answer is 269 ([Song & Zhao, 2016](document_1.txt)). My assessment is that the 269 figure is the most comprehensive and defensible aggregation from the primary source, while the 209 figure is likely the result of a transcription error in the third-party note ([Third-Party Research Note, n.d.](document_2.txt)).

## References

Song, L., & Zhao, L. (2016). *Question generation from a knowledge base with web exploration* (arXiv:1610.03807). [document_1.txt](document_1.txt)

Third-Party Research Note. (n.d.). *Question generation from a knowledge base with web exploration*. [document_2.txt](document_2.txt)