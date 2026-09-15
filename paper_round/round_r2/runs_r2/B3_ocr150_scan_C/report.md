# Hand-Crafted Question Templates in Knowledge Base Question Generation: How Many Were Needed?

## Overview: The Direct Answer

The question of how many hand-crafted templates the authors had to create does not have a single, system-wide answer. The work reports two separate template counts, one for each of the two knowledge bases (KBs) used in evaluation. For the Freebase evaluation on 500 randomly selected triples, the authors hand-crafted **106 templates**, because those triples shared only 53 distinct predicates, amounting to an average of two templates per predicate ([Song & Zhao, 2017](https://arxiv.org/abs/1610.03807)). For the in-house power tool domain KB, which contained 67 distinct predicates, the authors hand-crafted **163 templates** ([Song & Zhao, 2017](https://arxiv.org/abs/1610.03807)). The two figures are the only template-construction counts reported in the study, and both are tied to the specific predicate sets of each evaluation rather than representing a universal template inventory ([Third-Party Research Note, n.d.](document_2.txt)).

The remainder of this report examines what these numbers mean, how they were derived, why the count is structured this way, and what the associated evaluation outcomes indicate about the approach.

## The Two Reported Template Counts at a Glance

Table 1 consolidates the reported figures for the two evaluation settings.

| Evaluation setting | Knowledge base | Distinct predicates | Hand-crafted templates | Templates per predicate (derived) | Seed questions generated |
|---|---|---|---|---|---|
| Domain-general | Freebase (500 random triples) | 53 | 106 | ≈2.0 | 991 |
| Domain-specific | In-house power tool KB | 67 | 163 | ≈2.4 | 12,228 |

Sources: ([Song & Zhao, 2017](https://arxiv.org/abs/1610.03807); [Third-Party Research Note, n.d.](document_2.txt)).

The per-predicate ratios in the right-hand columns are arithmetic derivations from the reported numbers, not figures stated in the paper itself. They are included to show how tightly template authoring was coupled to predicate coverage in each setting.

## Freebase Evaluation: 106 Templates for 500 Triples

In the first experiment, the authors compared their end-to-end system with the previous state-of-the-art method of Serban et al. (2016) on 500 randomly selected triples from Freebase, a domain-general KB ([Song & Zhao, 2017](https://arxiv.org/abs/1610.03807)). For those 500 triples, they hand-crafted 106 templates. The reason the template count is so much smaller than the triple count is that the 500 triples share only 53 distinct predicates, so the authors produced approximately two templates for each predicate on average ([Song & Zhao, 2017](https://arxiv.org/abs/1610.03807)).

Applying those 106 templates to the triples generated **991 seed questions**, and the experiment then retrieved **1,529 additional questions from Google** ([Song & Zhao, 2017](https://arxiv.org/abs/1610.03807)). To evaluate fluency, the authors trained a 4-gram language model on Gigaword (LDC2011T07) with Kneser-Ney smoothing, and used the averaged language model score as an index to select the top 500 questions for comparison with the results of Serban et al. (2016) ([Song & Zhao, 2017](https://arxiv.org/abs/1610.03807)).

This design is explicitly predicate-oriented: template creation follows the predicates present in the KB, which keeps the template set compact relative to the triple set ([Third-Party Research Note, n.d.](document_2.txt)). In other words, 106 templates covered 500 triples because a single predicate such as `performsActivity` can appear across many subject–object pairs.

## Power Tool Domain Evaluation: 163 Templates for a Specialized KB

The third and final experiment ran the end-to-end system on a highly specialized in-house KB in the power tool domain ([Song & Zhao, 2017](https://arxiv.org/abs/1610.03807)). That KB contained **67 distinct predicates, 293 distinct subjects, and 279 distinct objects**. For the 67 predicates, the authors hand-crafted **163 templates** ([Song & Zhao, 2017](https://arxiv.org/abs/1610.03807)). This count is higher in absolute terms than the Freebase count, and it implies roughly 2.4 templates per predicate — a slightly denser template coverage than in the Freebase setting.

The domain-specific experiment reused the same language model as the first experiment and additionally learned a skip-gram model on Wikipedia for evaluating domain relevance ([Song & Zhao, 2017](https://arxiv.org/abs/1610.03807)). From the 163 templates, the system generated **12,228 seed questions**, from which **20,000 more questions** were expanded with Google ([Song & Zhao, 2017](https://arxiv.org/abs/1610.03807)). This illustrates the central efficiency argument of the paper: a modest number of manually authored templates can seed a very large question set.

The count differs from the Freebase total because the domain-specific KB has its own predicate set and therefore required its own template set; the two counts together show that manual template-building effort scales with predicate coverage rather than with the raw number of triples ([Third-Party Research Note, n.d.](document_2.txt)).

## Why So Few Templates? The Predicate-Centric Template Design

To understand why 106 and 163 templates were sufficient, it is necessary to understand what a template is in this framework. Given a KB, a small set of question templates is first hand-crafted based on the predicates in the KB. These templates consist of a transcription of the predicate (for example, `performsActivity = how to`) and placeholders for the subject (`#X#`) and the object (`#Y#`) ([Song & Zhao, 2017](https://arxiv.org/abs/1610.03807)). Each template is thus associated with a predicate, meaning that template creation follows the predicates present in the KB ([Third-Party Research Note, n.d.](document_2.txt)).

A concrete illustration is given in the paper: in the in-house power tool KB, the template "how to use #X#" was constructed for the predicate `performsActivity`, and applying that single template to the triple `(jigsaw, performsActivity, CurveCut)` produced the seed question "how to use jigsaw" ([Song & Zhao, 2017](https://arxiv.org/abs/1610.03807)). One template therefore instantiates many questions across many entities that share the same predicate.

The authors state that their system does not require a large number of templates for two reasons: first, the iterative question expansion can produce a large number of questions even from a relatively small number of seed questions, as the experiments demonstrate; and second, multiple entities in the KB share the same predicates ([Song & Zhao, 2017](https://arxiv.org/abs/1610.03807)). An additional advantage the authors claim is that the system can easily generate updated questions because the web is self-updating consistently ([Song & Zhao, 2017](https://arxiv.org/abs/1610.03807)).

## Template Construction as the Only Manual Component

The significance of the 106 and 163 figures lies in the fact that template construction is the *only* human labor in the system. The paper states plainly that "the only human labor in this work is the question template construction" ([Song & Zhao, 2017](https://arxiv.org/abs/1610.03807)). The third-party note reiterates this point, describing template construction as the manual component reported ([Third-Party Research Note, n.d.](document_2.txt)).

This stands in explicit contrast to prior work that relies on massive human-labeled data. Serban et al. (2016), treating question generation as a machine translation problem, trained a neural machine translation system with 10,000 (triple, question) pairs, where the question portion of those pairs was human-generated, requiring a large amount of human effort ([Song & Zhao, 2017](https://arxiv.org/abs/1610.03807)). The authors also note that the grammaticality and naturalness of questions generated by that approach cannot be guaranteed ([Song & Zhao, 2017](https://arxiv.org/abs/1610.03807)). The 106-template and 163-template figures are therefore best understood as the measured manual cost of the proposed alternative pipeline.

## From Templates to Questions: The Expansion and Selection Pipeline

The system contains four sub-modules: question template construction, seed question generation, question expansion, and selection ([Song & Zhao, 2017](https://arxiv.org/abs/1610.03807)). After templates are applied to the KB to produce a seed question set, the seed set is expanded through a search engine such as Google or Bing by iteratively forming each generated question as a search query to retrieve more related question candidates ([Song & Zhao, 2017](https://arxiv.org/abs/1610.03807)).

Algorithm 1 formalizes this: the expanded question set *E* is initialized as the seed question set *S*, and a queue *Q* is also initialized as *S*; in each iteration a previously obtained question is expanded from the web and newly retrieved questions are added to *E* if not already present, with a maximum number of iterations set by *I_max* ([Song & Zhao, 2017](https://arxiv.org/abs/1610.03807)). Because questions collected from web search may not be fluent or domain-relevant — and because domain relevance drops significantly as iteration proceeds — the system applies filtering ([Song & Zhao, 2017](https://arxiv.org/abs/1610.03807)).

Domain relevance is defined as the cosine similarity between the document embedding of the question and the averaged embedding of the in-domain data derived from the seed question set, while fluency is defined as the averaged language model score normalized by word count ([Song & Zhao, 2017](https://arxiv.org/abs/1610.03807)). Thresholds for domain relevance and fluency are applied, and questions scoring below them are filtered out ([Song & Zhao, 2017](https://arxiv.org/abs/1610.03807)). This pipeline is what allows a small template inventory to yield large, filtered question sets.

## Evaluation Outcomes Associated with the Template Sets

The reported evaluations indicate that the compact template sets produced competitive or superior output. Table 2 reproduces the human ratings.

| System | Grammaticality | Naturalness |
|---|---|---|
| Serban et al. (2016) | 3.36 | 3.14 |
| Ours | 3.53 | 3.31 |

Source: ([Song & Zhao, 2017](https://arxiv.org/abs/1610.03807)).

Three native English speakers evaluated fluency and naturalness on a 4-point scheme where 4 is best, and the authors' questions were rated more grammatical and more natural than those of Serban et al. (2016) ([Song & Zhao, 2017](https://arxiv.org/abs/1610.03807)). The paper notes that the naturalness score is lower than the grammaticality score for both methods because naturalness is a stricter metric — a natural question should also be grammatical, and additionally reflects whether people would ask it in reality ([Song & Zhao, 2017](https://arxiv.org/abs/1610.03807)).

Table 3 reports the domain-relevance evaluation on the web snippet dataset.

| Method | Precision |
|---|---|
| Phan et al. (2008) | 82.18 |
| Ma et al. (2015) | 85.31 |
| Chen et al. (2011) | 85.48 |
| Ours | 85.65 |

Source: ([Song & Zhao, 2017](https://arxiv.org/abs/1610.03807)).

The authors attribute this performance to word embeddings capturing similarity between distinct words, whereas traditional methods such as LDA only learn probabilities of words belonging to topics ([Song & Zhao, 2017](https://arxiv.org/abs/1610.03807)).

## Interpretation and Limitations

Several caveats are warranted when interpreting the 106 and 163 counts. First, both figures are evaluation-specific: the 106 templates correspond to the 53 distinct predicates found among 500 randomly selected Freebase triples, and the 163 templates correspond to the 67 predicates of the in-house power tool KB ([Song & Zhao, 2017](https://arxiv.org/abs/1610.03807)). Deploying the system on a different KB with a larger predicate inventory would require additional templates, because template creation follows predicate coverage ([Third-Party Research Note, n.d.](document_2.txt)).

Second, the paper does not report template counts for any other KB, so no general claim can be made about the total manual effort required for arbitrary domains. Third, the study does not present a formal cost-benefit analysis quantifying authoring time per template; the argument for reduced human effort rests on the qualitative contrast with the 10,000 human-generated question pairs used by Serban et al. (2016) ([Song & Zhao, 2017](https://arxiv.org/abs/1610.03807)). Fourth, the system generates questions without answers, leaving automatic answer mining as future work ([Song & Zhao, 2017](https://arxiv.org/abs/1610.03807)). Finally, the domain-specific experiment notes that at least one expanded question — "do I need a hammer drill" — lacked context information, indicating that filtering does not eliminate all under-specified outputs ([Song & Zhao, 2017](https://arxiv.org/abs/1610.03807)).

## Conclusion

In direct response to the question posed, the authors hand-crafted **106 templates** for the Freebase evaluation covering 500 triples and 53 distinct predicates, and **163 templates** for the in-house power tool domain KB covering 67 distinct predicates ([Song & Zhao, 2017](https://arxiv.org/abs/1610.03807)). These are the only template counts reported. The evidence indicates that template effort in this framework scales with the number of distinct predicates rather than the number of triples, which is precisely why a six-figure template count was unnecessary even for hundreds of triples ([Third-Party Research Note, n.d.](document_2.txt)). Whether this economy generalizes to other, more relationally diverse KBs remains untested in the reported experiments; the prudent interpretation is that 106 and 163 are bounded, setting-specific measurements of a predicate-driven manual step, not universal constants of the method.

## References

Song, L., & Zhao, L. (2017). *Question generation from a knowledge base with web exploration* (arXiv:1610.03807v2). arXiv. https://arxiv.org/abs/1610.03807

Third-party research note: Question generation from a knowledge base with web exploration. (n.d.). [document_2.txt]