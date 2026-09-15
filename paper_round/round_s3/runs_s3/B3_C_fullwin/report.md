# Hand-Crafted Template Construction in Question Generation from a Knowledge Base with Web Exploration

## Executive Summary

The question of how many hand-crafted templates the authors had to make has two reported answers because the system was evaluated on two different knowledge bases. In the Freebase evaluation, the authors hand-crafted 106 templates for 500 randomly selected triples ([Song & Zhao, 2016](document_1.txt)). In the in-house power tool domain knowledge base evaluation, they hand-crafted 163 templates for 67 distinct predicates ([Song & Zhao, 2016](document_1.txt)). If the two reported evaluations are combined, the total number of hand-crafted templates is 269. However, these are separate, knowledge-base-specific template sets rather than a single universal template library. The paper states that the only human labor in this work is question template construction ([Song & Zhao, 2016](document_1.txt)). A third-party research note corroborates both counts: 106 templates for Freebase and 163 templates for the power tool domain ([Third-party research note, n.d.](document_2.txt)).

## The Core Answer: Two Reported Template Counts

### Freebase Evaluation: 106 Templates

In the Freebase experiment, the authors used 500 randomly selected triples. For these 500 triples, they hand-crafted 106 templates ([Song & Zhao, 2016](document_1.txt)). The triples shared only 53 distinct predicates, so the authors made an average of two templates for each predicate ([Song & Zhao, 2016](document_1.txt)). This design ties template creation to predicates rather than to individual triples, keeping the template set compact relative to the triple set ([Third-party research note, n.d.](document_2.txt)). Applying these templates to the triples generated 991 seed questions, and 1,529 more questions were retrieved from Google ([Song & Zhao, 2016](document_1.txt)).

### Power Tool Domain Evaluation: 163 Templates

In the in-house power tool domain knowledge base, the KB contained 67 distinct predicates, 293 distinct subjects, and 279 distinct objects ([Song & Zhao, 2016](document_1.txt)). For the 67 predicates, the authors hand-crafted 163 templates ([Song & Zhao, 2016](document_1.txt)). This count differs from the Freebase count because the domain-specific KB has its own predicate set and required its own template set ([Third-party research note, n.d.](document_2.txt)). The power tool evaluation generated 12,228 seed questions, from which 20,000 more questions were expanded with Google ([Song & Zhao, 2016](document_1.txt)).

### Aggregate Human Effort: 269 Templates Across Two Evaluations

When the two reported evaluations are considered together, the authors hand-crafted 106 + 163 = 269 templates. This aggregate figure represents the total template-construction work reported across the Freebase and power tool domain experiments. It does not imply that a single deployment would require 269 templates, because the two template sets were built for different predicate inventories and different KBs. The third-party research note explicitly states that the Freebase and power tool counts provide the reported template-construction figures for the system and that the manual template-building effort scales with predicate coverage in each evaluation ([Third-party research note, n.d.](document_2.txt)).

## Why the Counts Differ: Predicate-Driven Template Design

### Freebase: 53 Distinct Predicates, 500 Triples

The Freebase evaluation used 500 random-selected triples, but these triples shared only 53 distinct predicates ([Song & Zhao, 2016](document_1.txt)). The authors therefore needed 106 templates, which is exactly two templates per predicate on average ([Song & Zhao, 2016](document_1.txt)). This ratio shows that the template count is driven by predicate diversity, not by the number of triples. Because multiple entities in a KB share the same predicates, a relatively small template set can cover a much larger triple set ([Song & Zhao, 2016](document_1.txt)).

### Power Tool Domain: 67 Predicates, 293 Subjects, 279 Objects

The power tool domain KB had 67 distinct predicates, 293 distinct subjects, and 279 distinct objects ([Song & Zhao, 2016](document_1.txt)). For these 67 predicates, the authors hand-crafted 163 templates, which is approximately 2.43 templates per predicate. This is slightly higher than the Freebase ratio of 2.0 templates per predicate. The difference likely reflects the specialized nature of the power tool domain, where predicates may require more varied phrasings to produce fluent and natural questions. The third-party research note notes that the template count differs because the domain-specific KB has its own predicate set and required its own template set ([Third-party research note, n.d.](document_2.txt)).

The following table summarizes the reported template-construction figures.

| Evaluation Setting | Triples or Predicates | Distinct Predicates | Hand-Crafted Templates | Templates per Predicate (approx.) |
|---|---|---:|---:|---:|
| Freebase | 500 randomly selected triples | 53 | 106 | 2.00 |
| Power tool domain | 67 predicates; 293 subjects; 279 objects | 67 | 163 | 2.43 |
| **Combined total** | — | — | **269** | — |

*Note.* Data from Song and Zhao (2016) and the third-party research note (n.d.).

## Template Construction as the Only Human Labor

The paper states that the only human labor in this work is question template construction ([Song & Zhao, 2016](document_1.txt)). Each template is associated with a predicate in the KB, and template creation follows the predicates present in the KB ([Third-party research note, n.d.](document_2.txt)). The templates consist of a transcription of the predicate in the KB—for example, `performsActivity` becomes `how to`—and placeholders for the subject (`#X#`) and the object (`#Y#`) ([Song & Zhao, 2016](document_1.txt)). For instance, the template `how to use #X#` is constructed for the predicate `performsActivity`, and applying it to the triple `<jigsaw, performsActivity, CurveCut>` generates the seed question `how to use jigsaw` ([Song & Zhao, 2016](document_1.txt)).

The system does not require a large number of templates for two reasons. First, iterative question expansion can produce a large number of questions even with a relatively small number of seed questions ([Song & Zhao, 2016](document_1.txt)). Second, multiple entities in the KB share the same predicates ([Song & Zhao, 2016](document_1.txt)). Another advantage is that the system can easily generate updated questions because the web is self-updating consistently ([Song & Zhao, 2016](document_1.txt)). This design significantly reduces human effort compared with previous work that relies on massive human-labeled data. For example, a prior neural machine translation system was trained with 10,000 triple-question pairs, and the question part of those pairs was human generated ([Song & Zhao, 2016](document_1.txt)). In contrast, the proposed system requires only the template construction step.

## From Templates to Questions: Seed Generation and Web Expansion

### Freebase: 991 Seed Questions, 1,529 Retrieved Questions

Applying the 106 templates to the 500 Freebase triples generated 991 seed questions ([Song & Zhao, 2016](document_1.txt)). The system then retrieved 1,529 more questions from Google ([Song & Zhao, 2016](document_1.txt)). To evaluate fluency, the authors trained a 4-gram language model on Gigaword (LDC2011T07) with Kneser-Ney smoothing ([Song & Zhao, 2016](document_1.txt)). Using the averaged language model score as an index, the top 500 questions were selected for comparison with the baseline ([Song & Zhao, 2016](document_1.txt)).

### Power Tool Domain: 12,228 Seed Questions, 20,000 Retrieved Questions

In the power tool domain evaluation, the 163 templates generated 12,228 seed questions, from which 20,000 more questions were expanded with Google ([Song & Zhao, 2016](document_1.txt)). The same language model was used as in the first experiment, and a skip-gram model was learned on Wikipedia for evaluating domain relevance ([Song & Zhao, 2016](document_1.txt)). The following table summarizes the question-generation pipeline.

| Stage | Freebase Evaluation | Power Tool Domain Evaluation |
|---|---:|---:|
| Hand-crafted templates | 106 | 163 |
| Seed questions generated | 991 | 12,228 |
| Additional questions retrieved from Google | 1,529 | 20,000 |
| Language model for fluency | 4-gram LM on Gigaword | Same 4-gram LM |
| Domain relevance model | Skip-gram model | Skip-gram model on Wikipedia |

*Note.* Data from Song and Zhao (2016).

## Quality and Selection: Fluency, Naturalness, and Domain Relevance

### Human Ratings on Freebase

Three native English speakers evaluated the fluency and naturalness of both the proposed system’s questions and the baseline’s questions on a 4-point scheme where 4 is the best ([Song & Zhao, 2016](document_1.txt)). The averaged human ratings showed that the proposed system’s questions were more grammatical and natural than the baseline’s questions ([Song & Zhao, 2016](document_1.txt)). The proposed system scored 3.53 on grammaticality and 3.31 on naturalness, while the baseline scored 3.36 and 3.14, respectively ([Song & Zhao, 2016](document_1.txt)). The naturalness score was lower than the grammaticality score for both methods because naturalness is a stricter metric: a natural question should also be grammatical ([Song & Zhao, 2016](document_1.txt)).

The paper provides examples comparing the two systems. For instance, the proposed system generated “what is the cultural heritage of churchill national park,” while the baseline generated “where in australia is churchill national park” ([Song & Zhao, 2016](document_1.txt)). Other baseline questions were described as ungrammatical, unnatural, or confusing, such as “who was someone who was involved in the leukemia?” and “whats the title of a book of the subject of the bible?” ([Song & Zhao, 2016](document_1.txt)). The proposed system’s questions were judged to be grammatical and natural because they resemble questions people usually ask on the web ([Song & Zhao, 2016](document_1.txt)).

### Domain Relevance Evaluation

The authors also tested their domain-relevance evaluation method on the web snippet dataset, which contains 10,060 training and 2,280 test snippets in 8 classes, with each snippet averaging 18 words ([Song & Zhao, 2016](document_1.txt)). The proposed method achieved 85.65 precision, outperforming previous methods that scored 82.18, 85.31, and 85.48 ([Song & Zhao, 2016](document_1.txt)). The method first concatenates training documents of the same domain into one “domain document,” then calculates each document embedding by averaging word embeddings within it, and finally assigns the label of the nearest domain document to each test document ([Song & Zhao, 2016](document_1.txt)). The authors suggest that word embeddings capture similarity between distinct words such as “finance” and “economy,” whereas traditional methods like LDA only learn probabilities of words belonging to topics ([Song & Zhao, 2016](document_1.txt)).

## Limitations and Implications

The current system only generates questions without answers, and the authors leave automatic answer mining as future work ([Song & Zhao, 2016](document_1.txt)). This limitation means that the generated questions cannot yet be directly used for question-answering corpora without an additional answer-generation or answer-retrieval step. Nevertheless, the reported template counts—106 for Freebase and 163 for the power tool domain—demonstrate that the manual effort is concentrated in a small, predicate-driven template set. The system then leverages web resources to expand the question set to thousands of items. For the Freebase evaluation, 106 templates led to 991 seed questions and 1,529 retrieved questions; for the power tool domain, 163 templates led to 12,228 seed questions and 20,000 retrieved questions ([Song & Zhao, 2016](document_1.txt)). This ratio of templates to generated questions illustrates the leverage provided by web exploration.

## Conclusion

The answer to the query “How many hand-crafted templates did they have to make?” depends on which evaluation is considered. The authors hand-crafted 106 templates for the Freebase experiment and 163 templates for the in-house power tool domain experiment. Across both reported evaluations, the total is 269 hand-crafted templates. These templates are the only human labor in the system, and their construction is tied to the predicates in each knowledge base. The Freebase set covered 53 distinct predicates, while the power tool set covered 67 predicates. The system then used web search to expand a relatively small seed question set into a large candidate pool, followed by fluency and domain-relevance filtering. This design significantly reduces human effort compared with prior approaches that rely on thousands of human-generated question-answer pairs. The reported human ratings and domain-relevance precision further indicate that the approach produces fluent, natural, and domain-relevant questions.

## References

Song, L., & Zhao, L. (2016). *Question generation from a knowledge base with web exploration* [Document]. document_1.txt.

Third-party research note: Question generation from a knowledge base with web exploration. (n.d.). document_2.txt.