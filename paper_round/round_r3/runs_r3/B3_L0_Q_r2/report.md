# How Many Hand-Crafted Templates? A Detailed Analysis of Template Construction in Song and Zhao’s Question Generation System

## Introduction

Question generation from a knowledge base (KB) is the task of producing natural language questions related to the domain of an input KB. Song and Zhao (2016) proposed a system that leverages massive web resources to generate fluent and natural questions from a KB, significantly reducing human effort. A central component of this system is the use of question templates. The query addressed in this report is: **How many hand-crafted templates did the researchers have to make?** This report provides a detailed answer by examining the primary source (Song & Zhao, 2016) and a third-party research note (Third-party research note, n.d.) that summarizes the paper. The report covers the role of templates, the specific counts for each evaluation, a discrepancy between sources, and the implications for human effort.

## The Function of Question Templates in the System

In the proposed system, a knowledge base is viewed as a directed graph where nodes are entities and edges are relations. It can also be represented as a list of triples in the format ⟨subject, predicate, object⟩. For example, ⟨jigsaw, performsActivity, CurveCut⟩ ([Song & Zhao, 2016](https://arxiv.org/abs/1610.03807)). Question generation from a KB is challenging because function words and morphological forms for entities are abstracted away when a KB is created. To address this, Song and Zhao (2016) construct a small set of question templates. Each template is associated with a predicate in the KB. These templates consist of a transcription of the predicate in the KB (e.g., performsActivity ⇒ how to) and placeholders for the subject (#X#) and the object (#Y#). For instance, the template “how to use #X#” is constructed for the predicate “performsActivity”. Applying this template to the triple ⟨jigsaw, performsActivity, CurveCut⟩ generates the seed question “how to use jigsaw” ([Song & Zhao, 2016](https://arxiv.org/abs/1610.03807)). The seed question set is then expanded through a search engine by iteratively forming already obtained questions as search queries to retrieve more related question candidates. Finally, a selection step estimates fluency and domain relevance to filter candidates.

The only human labor in this work is the question template construction ([Song & Zhao, 2016](https://arxiv.org/abs/1610.03807)). The system does not require a large number of templates because the iterative question expansion can produce many questions even from a relatively small number of seed questions, and multiple entities in the KB share the same predicates. This design ties template creation to predicates, keeping the template set compact relative to the triple set (Third-party research note, n.d.).

## Hand-Crafted Template Count in the Freebase Evaluation

The first experiment compares the system with a previous state-of-the-art method on 500 randomly selected triples from Freebase, a domain-general KB. For these 500 triples, the researchers hand-crafted **106 templates**. The triples share only 53 distinct predicates, so they made 2 templates for each predicate on average. Applying the templates to the triples generated 991 seed questions. The experiment also retrieved 1529 more questions from Google. This design ties template creation to predicates, keeping the template set compact relative to the triple set (Third-party research note, n.d.; [Song & Zhao, 2016](https://arxiv.org/abs/1610.03807)). Table 1 summarizes these figures.

| Freebase Evaluation Metric | Value |
|----------------------------|-------|
| Randomly selected triples | 500 |
| Distinct predicates | 53 |
| Hand-crafted templates | 106 |
| Average templates per predicate | 2 |
| Seed questions generated | 991 |
| Additional questions retrieved from Google | 1529 |

**Table 1.** Template construction statistics for the Freebase evaluation ([Song & Zhao, 2016](https://arxiv.org/abs/1610.03807); Third-party research note, n.d.).

This 106 figure is the most direct answer to the query for the primary Freebase evaluation. The human effort required to create 106 templates is substantially less than the 10,000 human-generated question-triple pairs used by the neural machine translation baseline (Serban et al., 2016, as cited in [Song & Zhao, 2016](https://arxiv.org/abs/1610.03807)). The paper states that treating question generation as a machine translation problem, the baseline trains an NMT system with 10,000 ⟨triple, question⟩ pairs, where the question part is human generated, requiring a large amount of human effort. In contrast, Song and Zhao’s system uses only 106 hand-crafted templates to handle 500 triples, a reduction of several orders of magnitude in manual annotation effort.

## Hand-Crafted Template Count in the Power Tool Domain Evaluation

The third experiment runs the end-to-end system on a highly specialized in-house KB in the power tool domain. This KB contains 67 distinct predicates, 293 distinct subjects, and 279 distinct objects. The original paper states: “For the 67 predicates, we hand-craft 163 templates” ([Song & Zhao, 2016](https://arxiv.org/abs/1610.03807)). However, a third-party research note (n.d.) claims that for the 67 predicates, the 163 templates were generated automatically from the predicate names rather than hand-crafted. This is a direct contradiction. The third-party note states: “For the in-house power tool domain knowledge base, the paper reports 67 predicates. For the 67 predicates, the 163 templates were generated automatically from the predicate names rather than hand-crafted” (Third-party research note, n.d.). The note further explains that the count differs from the Freebase template count because the domain-specific KB has its own predicate set and required its own template set.

Given the instructions to prioritize reliable sources, the primary source (Song & Zhao, 2016) is more authoritative than the third-party note. The primary paper explicitly uses the phrase “we hand-craft 163 templates” ([Song & Zhao, 2016](https://arxiv.org/abs/1610.03807)). Therefore, based on the primary source, the researchers hand-crafted 163 templates for the power tool domain. If the third-party note were correct, then the number of hand-crafted templates for that domain would be zero, which would contradict the paper’s statement that “the only human labor in this work is the question template construction” ([Song & Zhao, 2016](https://arxiv.org/abs/1610.03807)). It is possible that the third-party note contains an error or misinterpretation. For the purposes of this report, the primary source is treated as reliable, and the third-party note is noted as a conflicting secondary source.

Table 2 presents the power tool domain statistics.

| Power Tool Domain Metric | Value |
|--------------------------|-------|
| Distinct predicates | 67 |
| Distinct subjects | 293 |
| Distinct objects | 279 |
| Hand-crafted templates (per primary source) | 163 |
| Templates generated automatically (per third-party note) | 163 (disputed) |
| Seed questions generated | 12,228 |
| Additional questions expanded with Google | 20,000 |

**Table 2.** Template construction statistics for the in-house power tool domain evaluation ([Song & Zhao, 2016](https://arxiv.org/abs/1610.03807); Third-party research note, n.d.).

### Discrepancy Analysis: Primary vs. Secondary Source

The third-party note (n.d.) states that for the power tool domain, the 163 templates were generated automatically from predicate names rather than hand-crafted. This claim directly contradicts the primary source, which says “we hand-craft 163 templates” ([Song & Zhao, 2016](https://arxiv.org/abs/1610.03807)). The primary source is an arXiv preprint authored by the researchers who built the system. The third-party note is an unaffiliated summary. According to standard source evaluation, the primary source should be given precedence. Moreover, the primary source’s statement that “the only human labor in this work is the question template construction” ([Song & Zhao, 2016](https://arxiv.org/abs/1610.03807)) implies that all templates across all experiments were hand-crafted. If the power tool templates were automatic, then the human labor would be only the Freebase templates, but the paper does not mention any automatic generation method. The third-party note may have misinterpreted a different part of the paper, or it may have confused the power tool templates with something else. Therefore, this report concludes that the hand-crafted template count for the power tool domain is 163, as stated in the primary source.

## Aggregate Human Template Construction Effort

If we consider both evaluations reported in the primary source, the total number of hand-crafted templates is the sum of 106 (Freebase) and 163 (power tool), which equals **269**. However, it is important to note that these two experiments are separate. The Freebase evaluation is a domain-general benchmark, while the power tool domain is a specialized in-house KB. The researchers likely did not use the same templates across both, because the predicates and domains differ. The paper states that the only human labor in this work is the question template construction ([Song & Zhao, 2016](https://arxiv.org/abs/1610.03807)). This implies that all templates used in both experiments were hand-crafted. If the third-party note’s claim about automatic generation were true, then the total hand-crafted templates would be only 106, but that would conflict with the primary source’s wording.

Table 3 summarizes the template counts across both evaluations.

| Evaluation | Distinct Predicates | Hand-Crafted Templates | Source |
|------------|---------------------|------------------------|--------|
| Freebase | 53 | 106 | Primary source |
| Power tool domain | 67 | 163 | Primary source |
| Power tool domain (disputed) | 67 | 0 (claimed automatic) | Third-party note |
| Total (per primary source) | 120 (sum, not unique) | 269 | Calculated |

**Table 3.** Summary of hand-crafted template counts across evaluations. The total is calculated by summing the two experiments, though the predicate sets are disjoint.

The query “How many hand-crafted templates did they have to make?” can be answered in several ways depending on scope. For the main Freebase evaluation, the answer is 106. For the power tool domain evaluation, the primary source reports 163. Across both experiments, the total is 269. The most prominent single number in the paper’s abstract and introduction is not a template count, but in the experimental section, the Freebase count of 106 is highlighted as the human effort for the main comparison. The power tool count of 163 is reported later as part of a domain-specific demonstration.

## Why the Number Matters: Efficiency and Scalability

The small number of hand-crafted templates is significant because it demonstrates a drastic reduction in human effort compared to prior work. The neural machine translation baseline required 10,000 human-generated question-triple pairs ([Song & Zhao, 2016](https://arxiv.org/abs/1610.03807)). In contrast, 106 templates for 500 triples and 163 templates for 67 predicates represent a much smaller annotation burden. The system’s ability to generate 991 seed questions from 106 templates in the Freebase experiment, and 12,228 seed questions from 163 templates in the power tool experiment, shows that templates are highly reusable. This reusability stems from the fact that multiple entities in a KB share the same predicates. For example, many tools may share the “performsActivity” predicate, so one template “how to use #X#” can generate questions for many different tools.

Furthermore, the iterative web expansion step amplifies the seed set. In the Freebase experiment, 1529 additional questions were retrieved from Google, and in the power tool experiment, 20,000 more questions were expanded with Google ([Song & Zhao, 2016](https://arxiv.org/abs/1610.03807)). The selection step, which uses a skip-gram model for domain relevance and a language model for fluency, filters out low-quality candidates. The domain relevance metric is defined as the cosine similarity between the document embedding of the question and the document embedding of the seed question set. The fluency metric is the averaged language model score. Thresholds for both are applied to filter questions.

### Implications for Human Effort

The total hand-crafted templates of 269 (across both experiments) is still vastly smaller than the 10,000 human-generated question-triple pairs required by the NMT baseline ([Song & Zhao, 2016](https://arxiv.org/abs/1610.03807)). This reduction is a key contribution of the work. The templates are not just a small set; they are also reusable because multiple entities share predicates. For example, the predicate “performsActivity” can apply to many tools, so one template “how to use #X#” can generate questions for a jigsaw, a drill, a sander, etc. The iterative web expansion further reduces the need for manual template creation, as one seed question can lead to many related questions. The selection step ensures that only fluent and domain-relevant questions are kept. Thus, the number of hand-crafted templates is not just a count; it is a measure of the system’s efficiency.

## Evaluation Results and Template Count Context

The effectiveness of the system is evaluated through human ratings and precision metrics. For the Freebase evaluation, three native English speakers rated the questions on a 4-point scheme. The system’s questions scored 3.53 on grammaticality and 3.31 on naturalness, compared to 3.36 and 3.14 for the baseline ([Song & Zhao, 2016](https://arxiv.org/abs/1610.03807)). Table 4 presents these results.

| System | Grammaticality | Naturalness |
|--------|----------------|-------------|
| Baseline (Serban et al., 2016) | 3.36 | 3.14 |
| Song & Zhao (2016) | 3.53 | 3.31 |

**Table 4.** Human ratings of generated questions on a 4-point scale ([Song & Zhao, 2016](https://arxiv.org/abs/1610.03807)).

For the domain relevance evaluation on the web snippet dataset, the method achieved a precision of 85.65, outperforming previous methods: 82.18, 85.31, and 85.48 ([Song & Zhao, 2016](https://arxiv.org/abs/1610.03807)). These results indicate that the small template set, combined with web expansion and selection, produces high-quality questions. The power tool domain evaluation generated questions such as “how to change circular saw blade” and “how to cut a groove in wood without a router,” which are grammatical, domain-relevant, and informative ([Song & Zhao, 2016](https://arxiv.org/abs/1610.03807)). The one exception noted was “do I need a hammer drill,” which lacks context information. Overall, the system demonstrates that a relatively small number of hand-crafted templates can serve as an effective seed for generating a large, diverse set of natural questions.

## Conclusion

The question of how many hand-crafted templates Song and Zhao had to make has a multi-part answer. For the main Freebase evaluation on 500 randomly selected triples, they hand-crafted **106 templates**, averaging 2 templates per distinct predicate ([Song & Zhao, 2016](https://arxiv.org/abs/1610.03807)). For the in-house power tool domain KB with 67 distinct predicates, the primary source states that they hand-crafted **163 templates** ([Song & Zhao, 2016](https://arxiv.org/abs/1610.03807)). A third-party research note contradicts this by claiming the 163 templates were generated automatically from predicate names (Third-party research note, n.d.), but the primary source is more reliable and explicitly uses the phrase “hand-craft.” Therefore, based on the primary source, the total number of hand-crafted templates across both experiments is **269**. If one focuses only on the primary benchmark comparison, the answer is **106**. The small number of templates relative to the 10,000 human-generated pairs required by the baseline highlights the system’s efficiency in reducing human labor. The templates are reusable across shared predicates, and the iterative web expansion further amplifies the seed set, enabling the generation of thousands of questions from a modest manual investment. Future work could address the automatic mining of answers, as the current system only generates questions.

## References

Song, L., & Zhao, L. (2016). *Question generation from a knowledge base with web exploration*. arXiv. https://arxiv.org/abs/1610.03807

Third-party research note: Question generation from a knowledge base with web exploration. (n.d.). Unpublished manuscript.