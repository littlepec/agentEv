# How Many Hand-Crafted Templates Did They Have to Make? A Detailed Analysis of Manual Effort in "Question Generation from a Knowledge Base with Web Exploration"

## Overview and Direct Answer

The central question of how much manual annotation effort the system of Song and Zhao (2017) actually required has a precise and surprisingly small answer. Because the authors designed template construction to be anchored to *predicates* rather than to individual triples or entities, the reported number of hand-crafted templates is measured in the low hundreds, not in the tens of thousands. The figures reported across the two evaluations are as follows:

| Evaluation Setting | Knowledge Base | Distinct Predicates | Hand-Crafted Templates | Templates per Predicate (avg.) |
|---|---|---|---|---|
| Experiment 1 | Freebase (500 random triples) | 53 | **106** | ~2.0 |
| Experiment 3 | In-house power tool domain KB | 67 | **103** (per third-party note) or **163** (per raw paper text) | ~1.5 or ~2.4 |
| **Combined** | Both KBs | 120 | **209** (as reported in the consolidated figure) | — |

Sources: ([Song & Zhao, 2017](document_1.txt)); ([Third-Party Research Note, n.d.](document_2.txt)).

In short, the answer to the query is **106 hand-crafted templates for the Freebase evaluation**, **103 templates for the power tool domain knowledge base according to the third-party research note**, and a **total of 209 hand-crafted templates across the entire work** ([Third-Party Research Note, n.d.](document_2.txt)). A notable textual inconsistency exists in the primary source, which I discuss in detail below.

## Why the Template Count Is the Single Most Important Number in This Work

The significance of the template count derives from the authors' explicit claim that "the only human labor in this work is the question template construction" ([Song & Zhao, 2017](document_1.txt)). Every other component of the pipeline — seed question generation, iterative web expansion, fluency scoring, and domain-relevance filtering — is automated. This means the total human annotation cost of the entire system is, in effect, equal to the number of hand-crafted templates. The template count is therefore not simply a descriptive statistic; it is the system's central efficiency claim.

That claim is made in direct contrast to prior work. Song and Zhao (2017) note that Serban et al. (2016) trained a neural machine translation (NMT) system on 10,000 (triple, question) pairs, where the question portion of those pairs was human-generated and therefore "requires a large amount of human effort" ([Song & Zhao, 2017](document_1.txt)). The comparison is stark: 106 templates versus 10,000 human-written question–answer pairs. Even if one counts the 209 templates across both evaluations, the manual burden remains roughly two orders of magnitude smaller than the NMT baseline it is compared against.

## The Freebase Evaluation: 106 Templates for 500 Triples

### The Basic Figures

For the primary quantitative comparison, the authors drew 500 randomly selected triples from Freebase ([Song & Zhao, 2017](document_1.txt)). Freebase is described as a collaboratively created, domain-general graph database for structuring human knowledge ([Bollacker et al., 2008](document_1.txt)). For these 500 triples, the authors hand-crafted **106 templates** ([Song & Zhao, 2017](document_1.txt)).

### Why 106 Templates Were Sufficient

The key structural insight is that the 500 sampled triples shared only **53 distinct predicates** ([Song & Zhao, 2017](document_1.txt)). Since templates are associated with predicates rather than with triples, the required template set scales with predicate diversity, not with triple volume. Dividing 106 templates by 53 predicates yields an average of **2 templates per predicate** ([Song & Zhao, 2017](document_1.txt)). The third-party note makes this point explicitly, observing that "this design ties template creation to predicates, keeping the template set compact relative to the triple set" ([Third-Party Research Note, n.d.](document_2.txt)).

A concrete illustration of the template mechanism is given for the power tool domain. The template "how to use #X#" is associated with the predicate "performsActivity," with placeholders for the subject (#X#) and the object (#Y#) ([Song & Zhao, 2017](document_1.txt)). Applying that single template to the triple *(jigsaw, performsActivity, CurveCut)* yields the seed question "how to use jigsaw" ([Song & Zhao, 2017](document_1.txt)). Thus one template can generate many questions across many triples, because multiple entities in a knowledge base share the same predicates ([Song & Zhao, 2017](document_1.txt)).

### Output Volume from 106 Templates

The output from those 106 templates is considerably larger than the input. Applying the templates to the triples generated **991 seed questions**, and the web expansion step retrieved **1,529 additional questions from Google** ([Song & Zhao, 2017](document_1.txt)). This means that 106 manual artifacts — combined with automated web retrieval — produced a candidate pool of 2,520 questions, from which the top 500 were selected by language-model score for human evaluation ([Song & Zhao, 2017](document_1.txt)).

## The Domain-Specific Power Tool Knowledge Base

### Reported Counts

The third experiment applies the same end-to-end system to a "highly specialized in-house KB" in the power tool domain ([Song & Zhao, 2017](document_1.txt)). This KB contains **67 distinct predicates, 293 distinct subjects, and 279 distinct objects** ([Song & Zhao, 2017](document_1.txt)).

Here the sources diverge. The raw text of the paper reads: "For the 67 predicates, we hand-craft 163 templates" ([Song & Zhao, 2017](document_1.txt)). The third-party research note, however, states: "For the 67 predicates, the authors hand-crafted 103 templates" and further reports a combined total of 209 templates ([Third-Party Research Note, n.d.](document_2.txt)).

### Resolving the Discrepancy

The arithmetic of the reported total favors the figure of 103. If the Freebase count is 106 and the power tool count is 103, the sum is exactly 209 — the total reported in the consolidated template-construction figure ([Third-Party Research Note, n.d.](document_2.txt)). If the power tool count were 163, the combined total would be 269, which is not reported. My assessment is that **103 is the more internally consistent reading**, and that the "163" appearing in the raw OCR-derived text is most likely a transcription artifact. I present both figures because the primary source, as provided, contains the value 163, and a careful reader should be aware of the inconsistency rather than silently resolving it.

### Scale of the Domain-Specific Generation

Despite the modest template count, the domain-specific run produced **12,228 seed questions**, from which **20,000 more questions were expanded with Google** ([Song & Zhao, 2017](document_1.txt)). The authors report that most expanded questions were grammatical and relevant to the power tool domain, and that many were complex rather than simple factoid questions — the illustrative example being "how to cut a groove in wood without a router" ([Song & Zhao, 2017](document_1.txt)). They also note a failure case: the question "do I need a hammer drill" lacks context information ([Song & Zhao, 2017](document_1.txt)).

## Aggregate Manual Effort Across Both Evaluations

Taken together, the reported template-construction figures show that the manual template-building effort scales with **predicate coverage** in each evaluation, not with the number of triples, entities, or target questions ([Third-Party Research Note, n.d.](document_2.txt)). The table below summarizes the scaling relationship:

| Metric | Freebase Evaluation | Power Tool Evaluation |
|---|---|---|
| Triples / KB scope | 500 random triples | 67 predicates, 293 subjects, 279 objects |
| Distinct predicates | 53 | 67 |
| Templates hand-crafted | 106 | 103 (or 163) |
| Templates per predicate | 2.0 | 1.54 (or 2.43) |
| Seed questions generated | 991 | 12,228 |
| Web-retrieved questions | 1,529 | 20,000 |
| Domain-adapted LM/KB embedding | 4-gram LM on Gigaword; skip-gram | Same LM; skip-gram on Wikipedia |
| Human evaluation regime | 3 native English speakers; 4-point scale; top 500 by LM score | Qualitative sample inspection |

Sources: ([Song & Zhao, 2017](document_1.txt)); ([Third-Party Research Note, n.d.](document_2.txt)).

## Design Rationale: Why So Few Templates?

The authors offer two explicit reasons for why the system does not require a large number of templates ([Song & Zhao, 2017](document_1.txt)):

1. **Iterative question expansion amplifies output.** A relatively small number of seed questions can, through iterative retrieval, produce a very large number of question candidates. This is empirically borne out: 991 seed questions from Freebase expanded into 1,529 additional retrieved questions, and 12,228 power-tool seed questions expanded into 20,000 more ([Song & Zhao, 2017](document_1.txt)).
2. **Entities share predicates.** Because multiple entities in a KB map to the same predicate, one predicate-associated template covers many triples simultaneously ([Song & Zhao, 2017](document_1.txt)).

A further, forward-looking advantage is that the system "can easily generate updated questions as web is self-updating consistently" ([Song & Zhao, 2017](document_1.txt)). This means the low template count is not merely a one-time cost saving; it is a maintenance advantage, since the automated web-exploration component refreshes itself without additional human authoring.

## Does the Small Template Count Compromise Quality?

A natural objection is that reducing human effort to 106–209 templates must degrade output quality. The experimental evidence in the paper suggests otherwise, at least on the metrics tested.

### Fluency and Naturalness

Three native English speakers evaluated the fluency and naturalness of the generated questions on a 4-point scale, where 4 is best ([Song & Zhao, 2017](document_1.txt)). The averaged results are shown below.

| System | Grammaticality | Naturalness |
|---|---|---|
| Serban et al. (2016) | 3.36 | 3.14 |
| **Ours (Song & Zhao)** | **3.53** | **3.31** |

Source: ([Song & Zhao, 2017](document_1.txt)).

The authors observe that their questions were "significantly better" than those of Serban et al. (2016) on both grammaticality and naturalness, and they note that the naturalness score is lower than the grammaticality score for both systems because "naturalness is a more strict metric since a natural question should also be grammatical" ([Song & Zhao, 2017](document_1.txt)). Sample outputs support this: the system generated questions such as "what is the cultural heritage of churchill national park," "how does leukemia affect the body in children," and "why is new york called the city that never sleeps," whereas the comparison system produced items the authors characterize as unnatural or confusing, such as "what's one of the mountain where can you found in argentina in netflix?" ([Song & Zhao, 2017](document_1.txt)).

### Domain Relevance

The domain-relevance evaluation used a standard short-document classification dataset of **10,060 training and 2,280 test snippets across 8 classes**, with roughly 18 words per snippet ([Song & Zhao, 2017](document_1.txt)). The comparison against prior state-of-the-art methods is presented below.

| Method | Precision |
|---|---|
| Phan et al. (2008) | 82.18 |
| Ma et al. (2015) | 85.31 |
| Chen et al. (2011) | 85.48 |
| **Ours (Song & Zhao)** | **85.65** |

Source: ([Song & Zhao, 2017](document_1.txt)).

The authors attribute the advantage to the fact that word embeddings capture similarity between distinct words (such as "finance" and "economy"), whereas LDA-based methods only learn probabilities of words belonging to topics ([Song & Zhao, 2017](document_1.txt)).

## My Assessment

On the basis of the provided evidence, I take the position that the headline answer of **106 hand-crafted templates for Freebase** is the most defensible single figure, and that the **209-template total** across both knowledge bases is the most meaningful measure of the system's overall manual cost ([Song & Zhao, 2017](document_1.txt)); ([Third-Party Research Note, n.d.](document_2.txt)). This is a genuinely low annotation burden relative to the 10,000 human-generated question–answer pairs used by the NMT baseline it outperforms ([Song & Zhao, 2017](document_1.txt)).

That said, two caveats temper the conclusion. First, the 103-versus-163 discrepancy in the power tool evaluation is unresolved in the supplied material and should be treated as an open question rather than assumed away ([Song & Zhao, 2017](document_1.txt)); ([Third-Party Research Note, n.d.](document_2.txt)). Second, the reported template counts cover only two knowledge bases, one general-domain and one narrow in-house domain; the authors' claim that template needs remain small "in wide scope" rests on a limited evidence base ([Song & Zhao, 2017](document_1.txt)). A third limitation, acknowledged by the authors themselves, is that the system generates questions without answers, leaving automatic answer mining as future work ([Song & Zhao, 2017](document_1.txt)).

## Conclusion

The direct answer to the question posed is this: the authors hand-crafted **106 templates for the 500-triple Freebase evaluation** and **103 templates for the 67-predicate power tool knowledge base**, yielding a reported **total of 209 hand-crafted templates** for the entire system ([Song & Zhao, 2017](document_1.txt)); ([Third-Party Research Note, n.d.](document_2.txt)). A competing figure of 163 templates for the power tool domain appears in the primary text and is arithmetically inconsistent with the reported 209 total ([Song & Zhao, 2017](document_1.txt)). Because template construction is explicitly the only manual component of the pipeline, these low counts constitute the system's core contribution: high-quality, fluent, domain-relevant question generation achieved at a small fraction of the human annotation cost of the neural machine translation approach it outperforms.

## References

Bollacker, K., Evans, C., Paritosh, P., Sturge, T., & Taylor, J. (2008). Freebase: A collaboratively created graph database for structuring human knowledge. In *Proceedings of the 2008 ACM SIGMOD*, 1247–1250. Retrieved from [document_1.txt](document_1.txt)

Chen, M., Jin, X., & Shen, D. (2011). Short text classification improved by learning multi-granularity topics. In *IJCAI*, 1776–1781. Retrieved from [document_1.txt](document_1.txt)

Ma, C., Xu, W., Li, P., & Yan, Y. (2015). Distributional representations of words for short text classification. In *Proceedings of the 1st Workshop on Vector Space Modeling for Natural Language Processing*, 33–38. Retrieved from [document_1.txt](document_1.txt)

Phan, X.-H., Nguyen, L.-M., & Horiguchi, S. (2008). Learning to classify short and sparse text & web with hidden topics from large-scale data collections. In *Proceedings of the 17th International Conference on World Wide Web*, 91–100. Retrieved from [document_1.txt](document_1.txt)

Serban, I. V., García-Durán, A., Gulcehre, C., Ahn, S., Chandar, S., Courville, A., & Bengio, Y. (2016). Generating factoid questions with recurrent neural networks: The 30M factoid question-answer corpus. In *Proceedings of the 54th Annual Meeting of the Association for Computational Linguistics (ACL-16)*, 588–598, Berlin, Germany. Retrieved from [document_1.txt](document_1.txt)

Song, L., & Zhao, L. (2017). *Question generation from a knowledge base with web exploration* (arXiv:1610.03807v2). Retrieved from [document_1.txt](document_1.txt)

Third-party research note: Question generation from a knowledge base with web exploration. (n.d.). Retrieved from [document_2.txt](document_2.txt)