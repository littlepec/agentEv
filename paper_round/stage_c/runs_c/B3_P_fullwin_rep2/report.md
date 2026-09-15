# How Many Hand-Crafted Templates Did They Have to Make?

## Direct Answer to the Query

The number of hand-crafted templates required by the question generation system proposed by Song and Zhao depends on which evaluation setting is being considered, and the two source documents available provide partially conflicting figures. According to the primary research paper, the authors hand-crafted **106 templates** for the Freebase evaluation and **163 templates** for the in-house power tool domain knowledge base ([Song & Zhao, 2016](https://arxiv.org/abs/1610.03807)). Taken together, that represents **269 hand-crafted templates** across the two reported evaluations. A third-party research note summarizing the same work, however, states that only **103 templates** were hand-crafted for the power tool domain and that the combined total across both evaluations was **209 templates** ([Third-party research note, n.d.](document_2.txt)). Because the primary paper is the more authoritative source, the best-supported answer to the query is that the authors made **106 Freebase templates plus 163 domain-specific templates, for a reported total of 269**, while acknowledging that the secondary note reports a lower domain-specific count of 103 and a total of 209.

## Background: Why Templates Matter in This System

To understand the significance of these numbers, it is necessary to understand the architecture of the system. The task addressed is question generation from a knowledge base (KB), defined as generating questions related to the domain of the input KB ([Song & Zhao, 2016](https://arxiv.org/abs/1610.03807)). A KB is treated as a directed graph in which nodes are entities and edges are relations, or equivalently as a list of triples in the format ⟨subject, predicate, object⟩, such as ⟨jigsaw, performsActivity, CurveCut⟩ ([Song & Zhao, 2016](https://arxiv.org/abs/1610.03807)).

The system pipeline contains four sub-modules: question template construction, seed question generation, question expansion, and selection ([Song & Zhao, 2016](https://arxiv.org/abs/1610.03807)). Each template is associated with a predicate in the KB and consists of a transcription of that predicate (for example, "performsActivity" mapping to "how to") plus placeholders for the subject (#X#) and the object (#Y#) ([Song & Zhao, 2016](https://arxiv.org/abs/1610.03807)). A concrete example given in the paper is the template "how to use #X#", constructed for the predicate "performsActivity", which is then applied to the triple ⟨jigsaw, performsActivity, CurveCut⟩ to yield the seed question "how to use jigsaw" ([Song & Zhao, 2016](https://arxiv.org/abs/1610.03807)).

Crucially, the paper states explicitly that "the only human labor in this work is the question template construction" ([Song & Zhao, 2016](https://arxiv.org/abs/1610.03807)). The template count is therefore the single most important measure of the manual effort the system requires, which is precisely why the query is significant.

## Template Counts by Evaluation Setting

### The Freebase Evaluation: 106 Templates

For the Freebase evaluation, the authors used 500 randomly selected triples. These triples shared only 53 distinct predicates, so the authors hand-crafted 106 templates, which amounts to roughly 2 templates per predicate on average ([Song & Zhao, 2016](https://arxiv.org/abs/1610.03807)). Applying those templates to the triples generated 991 seed questions, and a further 1,529 questions were retrieved from Google ([Song & Zhao, 2016](https://arxiv.org/abs/1610.03807)). The third-party research note confirms these same figures and emphasizes that this design ties template creation to predicates, keeping the template set compact relative to the triple set ([Third-party research note, n.d.](document_2.txt)).

The table below summarizes the reported Freebase template construction data.

| Evaluation Setting | Triples | Distinct Predicates | Hand-Crafted Templates | Templates per Predicate | Seed Questions | Web-Retrieved Questions |
|---|---|---|---|---|---|---|
| Freebase | 500 | 53 | 106 | ~2.0 | 991 | 1,529 |
| Power tool KB (primary paper) | Not reported for triples | 67 | 163 | ~2.43 | 12,228 | 20,000 |
| Power tool KB (third-party note) | Not reported | 67 | 103 | ~1.54 | 12,228 | 20,000 |

*Sources: ([Song & Zhao, 2016](https://arxiv.org/abs/1610.03807); [Third-party research note, n.d.](document_2.txt))*

### The In-House Power Tool Domain Knowledge Base

The second and final experiment was conducted on an in-house KB in the power tool domain. This KB contains 67 distinct predicates, 293 distinct subjects, and 279 distinct objects ([Song & Zhao, 2016](https://arxiv.org/abs/1610.03807)). For those 67 predicates, the paper reports that the authors hand-crafted 163 templates ([Song & Zhao, 2016](https://arxiv.org/abs/1610.03807)). From these templates they generated 12,228 seed questions, from which 20,000 additional questions were expanded with Google ([Song & Zhao, 2016](https://arxiv.org/abs/1610.03807)).

The third-party research note diverges from the primary paper here. It reports that for the 67 predicates, the authors hand-crafted 103 templates, and that together with the 106 Freebase templates, the authors wrote 209 templates in total ([Third-party research note, n.d.](document_2.txt)). The note's arithmetic is internally consistent—106 plus 103 equals 209—but it conflicts with the primary paper's figure of 163 for the same set of 67 predicates.

## Resolving the Discrepancy: 209 or 269?

Presented with two conflicting accounts, a careful analyst must weigh source reliability. The primary paper is the original peer-reviewed-style research report authored by the system's creators, whereas the third-party research note is a derivative summary ([Song & Zhao, 2016](https://arxiv.org/abs/1610.03807); [Third-party research note, n.d.](document_2.txt)). On that basis, the figure of 163 domain-specific templates should be treated as the more reliable datum, making the aggregate 269. Nevertheless, the discrepancy is material enough that it should be disclosed rather than suppressed, since a difference of 60 templates changes the estimated manual burden substantially.

| Scenario | Freebase Templates | Power Tool Templates | Aggregate Total |
|---|---|---|---|
| Primary paper figure only | 106 | 163 | 269 |
| Third-party note figure only | 106 | 103 | 209 |

*Sources: ([Song & Zhao, 2016](https://arxiv.org/abs/1610.03807); [Third-party research note, n.d.](document_2.txt))*

It is worth noting that the third-party note also asserts that the paper itself reports the total of 209 templates in the template-construction experiment ([Third-party research note, n.d.](document_2.txt)). If that assertion is accurate, then the note and the paper are in direct conflict over both the domain-specific count and the aggregate. In either case, the reported range for total manual template construction effort is **209 to 269 templates** across the two evaluations, with 106 templates consistently attributed to the Freebase setting.

## Why So Few Templates? The Design Rationale

The relatively modest template counts are not accidental; they reflect a deliberate design choice. The paper argues that the system does not require a large number of templates for two stated reasons: first, the iterative question expansion can produce a large number of questions even from a relatively small number of seed questions, and second, multiple entities in the KB share the same predicates ([Song & Zhao, 2016](https://arxiv.org/abs/1610.03807)). The Freebase data illustrate this logic well: 500 triples collapsed to only 53 distinct predicates, so template construction scaled with predicates rather than with triples ([Song & Zhao, 2016](https://arxiv.org/abs/1610.03807)).

An additional advantage claimed by the authors is that the system can easily generate updated questions because the web is self-updating consistently ([Song & Zhao, 2016](https://arxiv.org/abs/1610.03807)). This contrasts with prior work that relies on massive human-labeled data—for instance, training a neural machine translation system on 10,000 ⟨triple, question⟩ pairs, where the question portion is human generated ([Song & Zhao, 2016](https://arxiv.org/abs/1610.03807)). The template-based approach replaces that large-scale annotation effort with a predicate-level investment.

## What the Templates Produced: Expansion and Selection

The templates are only the starting point. The expanded question set is initialized as the seed question set, and in each iteration an already-obtained question is expanded from the web, with retrieved questions added to the set if not already present, subject to a maximum iteration limit ([Song & Zhao, 2016](https://arxiv.org/abs/1610.03807)). Because questions collected from a search engine may lack fluency or domain relevance—especially as iteration proceeds—the system applies a skip-gram model for domain relevance and a language model for fluency ([Song & Zhao, 2016](https://arxiv.org/abs/1610.03807)). Domain relevance is defined as the cosine similarity between the document embedding of a question and that of the seed question set, while fluency is the averaged language model score, and questions below the relevance and fluency thresholds are filtered out ([Song & Zhao, 2016](https://arxiv.org/abs/1610.03807)).

The payoff from the modest template investment is visible in the evaluation results. On the Freebase comparison, human graders rated the system's questions higher than the prior state-of-the-art method on both grammaticality and naturalness, as shown below.

| System | Grammaticality | Naturalness |
|---|---|---|
| Prior method (Serban et al., 2016) | 3.36 | 3.14 |
| Ours (Song & Zhao) | 3.53 | 3.31 |

*Source: ([Song & Zhao, 2016](https://arxiv.org/abs/1610.03807))*

The domain relevance component was separately validated on the web snippet dataset, which contains 10,060 training and 2,280 test snippets across 8 domains, with an average of 18 words per snippet. The embedding-based method achieved 85.65 precision, outperforming prior methods scoring 82.18, 85.31, and 85.48 ([Song & Zhao, 2016](https://arxiv.org/abs/1610.03807)).

## Limitations and Caveats

Two caveats should accompany any answer to the query. First, the source conflict over the domain-specific count means the aggregate total should be reported as a range rather than a single number, unless the primary paper is privileged. Second, the templates themselves are the only manual component reported; the paper is explicit that all remaining effort is automated ([Song & Zhao, 2016](https://arxiv.org/abs/1610.03807)). Furthermore, the system only generates questions without answers, leaving automatic answer mining as future work ([Song & Zhao, 2016](https://arxiv.org/abs/1610.03807)). Finally, the paper's own comparison figures appear with anonymized citation placeholders in the source text, but the reference list identifies the baseline as Serban et al. (2016) ([Song & Zhao, 2016](https://arxiv.org/abs/1610.03807)).

## Conclusion

The most defensible answer to the question "How many hand-crafted templates did they have to make?" is **106 templates for Freebase and 163 templates for the in-house power tool domain, totaling 269** according to the primary paper ([Song & Zhao, 2016](https://arxiv.org/abs/1610.03807)). A third-party research note instead reports **103 domain-specific templates and a total of 209** ([Third-party research note, n.d.](document_2.txt)). Given the authors' explicit statement that template construction is the only human labor in the work, and given that the Freebase templates covered 53 distinct predicates while the power tool templates covered 67, the reported counts are consistent with a design philosophy that scales manual effort to predicate coverage rather than to the volume of triples or generated questions ([Song & Zhao, 2016](https://arxiv.org/abs/1610.03807)). Whether the true aggregate is 209 or 269, the system's core claim—that a small, hand-crafted template set can be expanded through web exploration into tens of thousands of fluent, domain-relevant questions—remains supported by the reported seed counts of 991 (Freebase) and 12,228 (power tool) and expanded counts of 1,529 and 20,000 respectively ([Song & Zhao, 2016](https://arxiv.org/abs/1610.03807)).

## References

Song, L., & Zhao, L. (2016). *Question generation from a knowledge base with web exploration* (arXiv:1610.03807). arXiv. https://arxiv.org/abs/1610.03807

Third-party research note: Question generation from a knowledge base with web exploration. (n.d.). [Research note]. [document_2.txt](document_2.txt)