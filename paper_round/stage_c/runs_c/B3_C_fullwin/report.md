# How Many Hand-Crafted Templates Were Required? An Analysis of Template Construction in Question Generation from a Knowledge Base

## Introduction

The task of generating natural language questions from a knowledge base (KB) presents a distinct challenge because KBs abstract away function words and morphological forms that are essential for fluent question phrasing ([Song & Zhao, 2016](https://arxiv.org/abs/1610.03807)). To address this challenge, Song and Zhao (2016) proposed a system that combines a small set of hand-crafted templates with iterative web exploration. A central design feature of this system is its reliance on a limited number of manually constructed templates, which are associated with predicates in the KB. The paper explicitly states that "the only human labor in this work is the question template construction" ([Song & Zhao, 2016](https://arxiv.org/abs/1610.03807)). Consequently, the number of hand-crafted templates is a critical metric for understanding the manual effort required by the proposed method.

This report answers the question: *How many hand-crafted templates did they have to make?* Based on the provided documents, the answer is twofold. In the Freebase evaluation, the authors hand-crafted **106 templates** for 500 randomly selected triples that shared 53 distinct predicates ([Song & Zhao, 2016](https://arxiv.org/abs/1610.03807); [Third-party research note](document_2.txt)). In the domain-specific power tool evaluation, the authors hand-crafted **163 templates** for an in-house KB containing 67 distinct predicates ([Song & Zhao, 2016](https://arxiv.org/abs/1610.03807)). Therefore, if considering both reported evaluations separately, the total number of hand-crafted templates constructed across the two experiments is **269**. However, because the experiments used different KBs and different predicate sets, each evaluation required its own independent template set. This report will detail the template counts, the context in which they were created, and the implications for the system's scalability and human effort.

## Template Construction as the Sole Human Labor

The proposed system consists of four main sub-modules: question template construction, seed question generation, question expansion, and selection ([Song & Zhao, 2016](https://arxiv.org/abs/1610.03807)). Among these, only template construction requires human intervention. The templates themselves consist of a transcription of a predicate in the KB (for example, `performsActivity` is transcribed as `how to`) and placeholders for the subject (`#X#`) and the object (`#Y#`) ([Song & Zhao, 2016](https://arxiv.org/abs/1610.03807)). For instance, the template `"how to use #X#"` is constructed for the predicate `"performsActivity"`, and applying it to the triple `⟨jigsaw, performsActivity, CurveCut⟩` yields the seed question `"how to use jigsaw"` ([Song & Zhao, 2016](https://arxiv.org/abs/1610.03807)).

Because each template is associated with a predicate, the number of templates scales with the number of distinct predicates in the target KB, not with the number of triples or entities. This design choice is intentional: multiple entities in a KB share the same predicates, so a single template can generate many seed questions ([Song & Zhao, 2016](https://arxiv.org/abs/1610.03807)). The third-party research note emphasizes this point, stating that "template creation follows the predicates present in the KB" and that "the manual template-building effort scales with predicate coverage in each evaluation" ([Third-party research note](document_2.txt)). This predicate-centric approach keeps the manual workload compact relative to the size of the KB.

## Freebase Evaluation: 106 Hand-Crafted Templates

In the first experiment, the authors evaluated their system on 500 randomly selected triples from Freebase, a domain-general KB ([Song & Zhao, 2016](https://arxiv.org/abs/1610.03807)). These 500 triples shared only 53 distinct predicates. To cover these predicates, the authors hand-crafted **106 templates**, which corresponds to an average of 2 templates per predicate ([Song & Zhao, 2016](https://arxiv.org/abs/1610.03807)). The third-party note confirms these figures, reporting: "For the Freebase evaluation, the work uses 500 randomly selected triples. The paper reports 106 hand-crafted templates for those 500 Freebase triples. The triples share only 53 distinct predicates, so the authors made 2 templates for each predicate on average" ([Third-party research note](document_2.txt)).

Applying these 106 templates to the 500 triples generated **991 seed questions** ([Song & Zhao, 2016](https://arxiv.org/abs/1610.03807)). The system then retrieved **1,529 additional questions** from Google, resulting in a total candidate pool that was later filtered for fluency and domain relevance ([Song & Zhao, 2016](https://arxiv.org/abs/1610.03807)). For evaluation, a 4-gram language model was trained on Gigaword (LDC2011T07) with Kneser-Ney smoothing, and the top 500 questions by averaged language model score were selected for comparison with the baseline method by Serban et al. (2016) ([Song & Zhao, 2016](https://arxiv.org/abs/1610.03807)).

Human evaluation was performed by three native English speakers using a 4-point scheme, where 4 was the best score. The system's questions achieved an average grammaticality score of **3.53** and a naturalness score of **3.31**, compared to the baseline's **3.36** and **3.14**, respectively ([Song & Zhao, 2016](https://arxiv.org/abs/1610.03807)). These results indicate that the 106 hand-crafted templates, combined with web expansion and selection, produced questions that were judged more fluent and natural than those generated by a neural machine translation approach trained on 10,000 human-generated question-triple pairs ([Song & Zhao, 2016](https://arxiv.org/abs/1610.03807)).

## Domain-Specific Power Tool Evaluation: 163 Hand-Crafted Templates

The third experiment focused on a highly specialized in-house KB in the power tool domain ([Song & Zhao, 2016](https://arxiv.org/abs/1610.03807)). This KB contained **67 distinct predicates**, **293 distinct subjects**, and **279 distinct objects** ([Song & Zhao, 2016](https://arxiv.org/abs/1610.03807)). For these 67 predicates, the authors hand-crafted **163 templates** ([Song & Zhao, 2016](https://arxiv.org/abs/1610.03807)). This count is higher than the Freebase template count because the domain-specific KB required its own predicate set and template set ([Third-party research note](document_2.txt)). On average, this equates to approximately **2.43 templates per predicate** (163 ÷ 67), which is slightly higher than the 2.0 average in the Freebase evaluation, reflecting the greater need for domain-specific phrasing in a specialized KB.

Using the same language model as in the first experiment and a skip-gram model trained on Wikipedia for domain relevance, the authors generated **12,228 seed questions** from the 163 templates ([Song & Zhao, 2016](https://arxiv.org/abs/1610.03807)). From these, **20,000 more questions** were expanded using Google ([Song & Zhao, 2016](https://arxiv.org/abs/1610.03807)). The expanded questions were generally grammatical and relevant to the power tool domain. Examples include:

- "how to change circular saw blade"
- "how to measure lawn mower cutting height"
- "how to sharpen drill bits on bench grinder"
- "how does an oscillating multi tool work"
- "how to cut a groove in wood without a router"
- "what type of sander to use on deck"
- "do i need a hammer drill"
- "can i use acrylic paint on wood"
- "how to use a sharpening stone with oil" ([Song & Zhao, 2016](https://arxiv.org/abs/1610.03807))

The authors noted that most questions were informative and corresponded to a specific answer, with the exception of "do I need a hammer drill," which lacks context information ([Song & Zhao, 2016](https://arxiv.org/abs/1610.03807)). The system also generated complex questions beyond simple factoids, such as "how to cut a groove in wood without a router" ([Song & Zhao, 2016](https://arxiv.org/abs/1610.03807)). This demonstrates that a moderate number of hand-crafted templates (163) can yield a large and diverse set of domain-relevant questions when combined with iterative web expansion.

## Comparative Table of Template Counts

The following table summarizes the key figures for hand-crafted templates across the two evaluations reported in the paper.

| Knowledge Base | Distinct Predicates | Hand-Crafted Templates | Average Templates per Predicate | Seed Questions | Expanded Questions (Google) |
|----------------|---------------------|------------------------|-------------------------------|----------------|----------------------------|
| Freebase (500 triples) | 53 | 106 | 2.00 | 991 | 1,529 |
| In-house power tool | 67 | 163 | ~2.43 | 12,228 | 20,000 |

*Sources: Song & Zhao (2016); Third-party research note (n.d.).*

## Why So Few Templates? Scalability and Design Implications

The relatively small number of templates—106 for Freebase and 163 for the power tool domain—is a deliberate design feature of the system. The paper explains that a large number of templates is unnecessary for two reasons: (1) the iterative question expansion can produce a large number of questions even with a relatively small number of seed questions, and (2) multiple entities in the KB share the same predicates ([Song & Zhao, 2016](https://arxiv.org/abs/1610.03807)). For example, in the Freebase evaluation, 991 seed questions were generated from just 106 templates, and 1,529 additional questions were retrieved from the web ([Song & Zhao, 2016](https://arxiv.org/abs/1610.03807)). In the power tool domain, 12,228 seed questions were generated from 163 templates, and 20,000 more were expanded ([Song & Zhao, 2016](https://arxiv.org/abs/1610.03807)). This amplification factor—where a single template can produce dozens or hundreds of questions—is central to reducing human effort.

Another advantage is that the system can easily generate updated questions because the web is self-updating ([Song & Zhao, 2016](https://arxiv.org/abs/1610.03807)). As new content appears online, the iterative expansion process can retrieve new question candidates without requiring new templates. This makes the approach adaptable to evolving domains and reduces the need for continuous manual template maintenance.

The third-party research note further emphasizes that the template set is kept compact relative to the triple set: "This design ties template creation to predicates, keeping the template set compact relative to the triple set" ([Third-party research note](document_2.txt)). The note also states that "the manual template-building effort scales with predicate coverage in each evaluation" ([Third-party research note](document_2.txt)). In other words, the number of templates grows with the number of distinct predicates, not with the number of triples or entities. For the Freebase evaluation, 500 triples shared only 53 predicates, so 106 templates (2 per predicate) were sufficient. For the power tool domain, 67 predicates required 163 templates (about 2.43 per predicate). If the KB had more predicates, more templates would be needed, but the growth is linear with respect to predicates, not triples.

## Implications for the Query: Total Template Count

The query asks: *How many hand-crafted templates did they have to make?* The answer depends on whether one considers each evaluation separately or the total across both reported experiments.

- **Freebase evaluation:** **106 hand-crafted templates** ([Song & Zhao, 2016](https://arxiv.org/abs/1610.03807); [Third-party research note](document_2.txt)).
- **Power tool domain evaluation:** **163 hand-crafted templates** ([Song & Zhao, 2016](https://arxiv.org/abs/1610.03807); [Third-party research note](document_2.txt)).
- **Total across both evaluations:** **269 hand-crafted templates** (106 + 163). However, these templates were not used simultaneously; they were constructed for two separate KBs with different predicate sets. Therefore, the total represents the sum of manual effort across the two reported experiments, not a single unified template set.

It is also worth noting that the paper does not report any additional hand-crafted templates beyond these two sets. The only human labor involved in the entire system is the construction of these templates ([Song & Zhao, 2016](https://arxiv.org/abs/1610.03807)). All other components—seed question generation, web expansion, and selection—are automated. This makes the template counts of 106 and 163 the definitive measures of manual effort required by the proposed method.

## Conclusion

In summary, the hand-crafted template counts reported in Song and Zhao (2016) are **106 templates for the Freebase evaluation** and **163 templates for the in-house power tool domain evaluation**. These figures correspond to 53 and 67 distinct predicates, respectively, yielding average template-to-predicate ratios of 2.0 and approximately 2.43. The total number of templates constructed across both experiments is **269**, but each set was designed for a separate KB. The system's reliance on a small, predicate-focused template set, combined with iterative web exploration, significantly reduces human effort while producing fluent and domain-relevant questions. This design demonstrates that a modest amount of manual template construction can be leveraged to generate thousands of questions, as evidenced by 991 seed questions and 1,529 expanded questions in the Freebase experiment, and 12,228 seed questions and 20,000 expanded questions in the power tool experiment ([Song & Zhao, 2016](https://arxiv.org/abs/1610.03807)). The answer to the query is therefore twofold: **106 templates for Freebase, and 163 templates for the power tool domain**, for a combined total of **269 hand-crafted templates** across the reported evaluations.

## References

Song, L., & Zhao, L. (2016). *Question generation from a knowledge base with web exploration*. arXiv preprint arXiv:1610.03807. https://arxiv.org/abs/1610.03807

Third-party research note: Question generation from a knowledge base with web exploration. (n.d.). *document_2.txt*.