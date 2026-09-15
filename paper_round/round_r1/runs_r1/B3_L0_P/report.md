# Hand-Crafted Question Templates in Knowledge-Base Question Generation: A Detailed Count and Analysis

## Introduction

The paper "Question Generation from a Knowledge Base with Web Exploration" by Linfeng Song and Lin Zhao presents a system that generates fluent, natural-language questions from an input knowledge base (KB) by combining a small set of hand-crafted templates with iterative web exploration ([Song & Zhao, 2016](https://arxiv.org/abs/1610.03807)). The central design claim of the work is that human effort is dramatically reduced because the only manual labor required is the construction of question templates, and because templates are tied to KB predicates rather than to individual triples ([Song & Zhao, 2016](https://arxiv.org/abs/1610.03807)). The present report answers the specific query — "How many hand-crafted templates did they have to make?" — by extracting every reported template count from the two available sources, reconciling the figures where they conflict, and placing those counts in the context of the system's overall methodology and evaluation.

A precise answer requires distinguishing between the two experimental settings reported in the paper: a domain-general evaluation on Freebase and a domain-specific evaluation on an in-house power-tool KB. Each setting required its own template set because each KB exposes a different predicate inventory ([Song & Zhao, 2016](https://arxiv.org/abs/1610.03807)).

## The Central Answer: Template Counts by Knowledge Base

### Freebase Evaluation

For the Freebase experiment, the authors randomly selected 500 triples from Freebase and reported that they hand-crafted **106 templates** for those triples ([Song & Zhao, 2016](https://arxiv.org/abs/1610.03807)). The reason the template count is so much smaller than the triple count is that the 500 triples shared only **53 distinct predicates**; on average, the authors made **2 templates for each predicate** ([Song & Zhao, 2016](https://arxiv.org/abs/1610.03807)). Applying this compact template set to the triples produced **991 seed questions**, and the system subsequently retrieved **1,529 additional questions from Google** ([Song & Zhao, 2016](https://arxiv.org/abs/1610.03807)).

This design deliberately decouples manual effort from the number of triples. Because template creation follows predicates, not entities, a KB with many triples but few predicates can be covered with relatively little human work ([Song & Zhao, 2016](https://arxiv.org/abs/1610.03807)). The third-party research note on this work makes the same observation, stating that the design "ties template creation to predicates, keeping the template set compact relative to the triple set" ([Third-party research note, n.d.]).

### Power-Tool Domain Knowledge Base

For the in-house KB in the power-tool domain, the paper reports a KB containing **67 distinct predicates, 293 distinct subjects, and 279 distinct objects** ([Song & Zhao, 2016](https://arxiv.org/abs/1610.03807)). For those 67 predicates, the authors state that they **hand-crafted 163 templates** ([Song & Zhao, 2016](https://arxiv.org/abs/1610.03807)). This template set generated **12,228 seed questions**, from which **20,000 more questions were expanded with Google** ([Song & Zhao, 2016](https://arxiv.org/abs/1610.03807)).

Using the primary paper's own figures, the total number of hand-crafted templates across both evaluations is therefore **106 + 163 = 269 templates** ([Song & Zhao, 2016](https://arxiv.org/abs/1610.03807)).

## Reconciling a Discrepancy Between the Two Sources

The two provided documents do not agree on the power-tool template count, and this discrepancy must be flagged because it changes the answer to the query.

| Metric | Primary paper ([Song & Zhao, 2016](https://arxiv.org/abs/1610.03807)) | Third-party note ([Third-party research note, n.d.]) |
|---|---|---|
| Freebase templates | 106 | 106 |
| Freebase distinct predicates | 53 | 53 |
| Freebase templates per predicate (avg.) | 2 | 2 |
| Freebase seed questions | 991 | 991 |
| Freebase web-retrieved questions | 1,529 | 1,529 |
| Power-tool distinct predicates | 67 | 67 |
| Power-tool templates | **163** | **103** |
| Reported combined total | 269 (computed) | **209** |

The third-party note asserts that "for the 67 predicates, the authors hand-crafted 103 templates" and that "together with the 106 Freebase templates, the authors wrote 209 templates in total" ([Third-party research note, n.d.]). The primary paper, however, states unambiguously that "for the 67 predicates, we hand-craft 163 templates" ([Song & Zhao, 2016](https://arxiv.org/abs/1610.03807)).

In keeping with the instruction to prioritize reliable sources, the primary paper must be treated as authoritative here, because it is the original research artifact, whereas the note is a secondary summary. On that basis, the defensible answer is **106 templates for Freebase and 163 for the power-tool domain, for a combined 269 templates**. The note's 103 and 209 figures are inconsistent with the primary source and should not be relied upon. Even so, an honest report must acknowledge that the note's numbers exist, because a reader encountering both documents could otherwise be confused.

## Why the Template Count Is the Key Measure of Human Effort

The paper is explicit that "the only human labor in this work is the question template construction" ([Song & Zhao, 2016](https://arxiv.org/abs/1610.03807)). Every other stage — seed question generation, iterative web expansion, and filtering — is automated. This makes the template count the single most important quantity for assessing how much human effort the system actually demands.

Structurally, a template consists of a transcription of a KB predicate (for example, `performsActivity ⇒ how to`) plus placeholders for the subject (`#X#`) and the object (`#Y#`) ([Song & Zhao, 2016](https://arxiv.org/abs/1610.03807)). The paper illustrates this with a concrete example: the template "how to use #X#" is constructed for the predicate "performsActivity," and applying it to the triple `⟨jigsaw, performsActivity, CurveCut⟩` yields the seed question "how to use jigsaw" ([Song & Zhao, 2016](https://arxiv.org/abs/1610.03807)).

The authors give two reasons the system does not require a large number of templates: (1) iterative question expansion can produce many questions even from a relatively small seed set, and (2) multiple entities in the KB share the same predicates ([Song & Zhao, 2016](https://arxiv.org/abs/1610.03807)). A third structural advantage is that the system can generate updated questions over time because the web is self-updating ([Song & Zhao, 2016](https://arxiv.org/abs/1610.03807)).

Contrast this with the prior state of the art. Serban et al. (2016), as described in the paper, trained a neural machine translation system on **10,000 human-generated ⟨triple, question⟩ pairs**, requiring a large amount of human effort and still failing to guarantee grammaticality and naturalness ([Song & Zhao, 2016](https://arxiv.org/abs/1610.03807)). The template-based approach thus replaces ten thousand human-written question examples with a few hundred predicate-linked templates — a difference of more than an order of magnitude in manual annotation.

## From Templates to Questions: The Expansion and Selection Pipeline

Understanding the template count also requires understanding what happens after templates are built, because the templates alone do not produce the final question set.

The algorithm initializes an expanded question set *E* with the seed question set *S*, then repeatedly pops a question from a queue, retrieves related questions from the web via a `WebExp` function, and adds any new questions to *E* and the queue ([Song & Zhao, 2016](https://arxiv.org/abs/1610.03807)). A maximum iteration count, *I*max, caps the loop because the process can otherwise generate an unbounded number of questions ([Song & Zhao, 2016](https://arxiv.org/abs/1610.03807)).

Two filters then screen the expanded candidates ([Song & Zhao, 2016](https://arxiv.org/abs/1610.03807)). Domain relevance is computed as the cosine similarity between the embedding of the candidate question *q* and the embedding of the in-domain seed set *D*in, where each document embedding is the average of its word embeddings, derived from a skip-gram model ([Song & Zhao, 2016](https://arxiv.org/abs/1610.03807)). Fluency is computed as the average language-model score, i.e., the general-domain log probability divided by word count ([Song & Zhao, 2016](https://arxiv.org/abs/1610.03807)). Questions scoring below thresholds *t*rel and *t*flu are filtered out ([Song & Zhao, 2016](https://arxiv.org/abs/1610.03807)). The paper notes that domain relevance drops significantly as iteration proceeds, which is precisely why these thresholds matter ([Song & Zhao, 2016](https://arxiv.org/abs/1610.03807)).

For the Freebase evaluation specifically, a 4-gram language model trained on Gigaword (LDC2011T07) with Kneser-Ney smoothing was used, and the **top 500 questions** by averaged language-model score were selected for comparison against the baseline ([Song & Zhao, 2016](https://arxiv.org/abs/1610.03807)).

## Evaluation Outcomes

The payoff from a small template set is measured by human judgment. Three native English speakers rated fluency and naturalness on a 4-point scale, evaluating whether people would ask the questions in reality ([Song & Zhao, 2016](https://arxiv.org/abs/1610.03807)). The results are shown below.

| System | Grammaticality | Naturalness |
|---|---|---|
| Baseline (Serban et al., 2016) | 3.36 | 3.14 |
| Ours (Song & Zhao, 2016) | 3.53 | 3.31 |

The template-and-web system was judged more grammatical and more natural than the neural machine translation baseline ([Song & Zhao, 2016](https://arxiv.org/abs/1610.03807)). The paper explains that naturalness scores are lower than grammaticality scores for both methods because naturalness is the stricter metric — a natural question must also be grammatical ([Song & Zhao, 2016](https://arxiv.org/abs/1610.03807)). The qualitative comparison in the paper shows baseline outputs that are ungrammatical (e.g., "who was someone who was involved in the leukemia?"), unnatural ("what's one of the mountain where can you found in argentina in netflix?"), or confusing, whereas the proposed system's questions read like genuine web queries ([Song & Zhao, 2016](https://arxiv.org/abs/1610.03807)).

Separately, the domain-relevance evaluation method was validated on the web snippet dataset, which contains 10,060 training and 2,280 test snippets across 8 classes, averaging 18 words per snippet ([Song & Zhao, 2016](https://arxiv.org/abs/1610.03807)). The proposed method achieved **85.65 precision**, outperforming the three prior methods at 82.18, 85.31, and 85.48 ([Song & Zhao, 2016](https://arxiv.org/abs/1610.03807)). The paper attributes this to word embeddings capturing similarity between distinct words (such as "finance" and "economy"), which traditional topic-based methods struggle to do ([Song & Zhao, 2016](https://arxiv.org/abs/1610.03807)).

On the power-tool KB, the expanded questions in the paper's Table 4 are grammatical and domain-relevant, including "how to change circular saw blade," "how to sharpen drill bits on bench grinder," and even complex questions such as "how to cut a groove in wood without a router" ([Song & Zhao, 2016](https://arxiv.org/abs/1610.03807)). The authors note that most questions are informative and correspond to a specific answer, with the exception of one example — "do I need a hammer drill" — that lacks context information ([Song & Zhao, 2016](https://arxiv.org/abs/1610.03807)).

## Interpretation and Opinion

Based on the primary source, the most defensible answer to the query is that the authors hand-crafted **106 templates for the Freebase evaluation and 163 templates for the in-house power-tool domain, for a total of 269 hand-crafted templates** ([Song & Zhao, 2016](https://arxiv.org/abs/1610.03807)). The third-party note's alternative figures of 103 and 209 are internally consistent with each other but conflict with the paper's explicit statement of 163, so the note's numbers should be regarded as an error or a transcription discrepancy until the original publication is consulted directly ([Third-party research note, n.d.]; [Song & Zhao, 2016](https://arxiv.org/abs/1610.03807)).

Two conclusions follow. First, the template count scales with the number of distinct predicates, not with the number of triples or entities. Freebase required 106 templates for 53 predicates; the power-tool KB required 163 templates for 67 predicates. In both cases, the ratio of templates to predicates is modest (roughly 2.0 and roughly 2.4 per predicate respectively), which supports the paper's claim that a "small number of hand-crafted templates" can seed a large question corpus ([Song & Zhao, 2016](https://arxiv.org/abs/1610.03807)).

Second, the human effort is genuinely small relative to the output. From 269 total templates, the two evaluations produced 991 seed questions on Freebase plus 12,228 seed questions on the power-tool KB, and a combined 21,529 additional questions expanded from the web ([Song & Zhao, 2016](https://arxiv.org/abs/1610.03807)). That leverage — hundreds of templates yielding tens of thousands of questions — is the core economic argument for the approach, and it stands even if one adopts the note's lower power-tool figure.

The main limitation, as the authors themselves acknowledge, is that the system "only generates questions without answers," leaving automatic answer mining as future work ([Song & Zhao, 2016](https://arxiv.org/abs/1610.03807)). For applications such as student assessment, intelligent tutoring, or building question-answer corpora for NLP training, that gap must eventually be closed. Nevertheless, on the specific question of manual template construction, the evidence is clear: the hand-crafted template burden was 106 templates for Freebase and 163 for the power-tool domain, totaling 269 — a figure consistent with the authors' explicit framing of template construction as the only human labor in the pipeline ([Song & Zhao, 2016](https://arxiv.org/abs/1610.03807)).

## Conclusion

The number of hand-crafted templates required by the system described in "Question Generation from a Knowledge Base with Web Exploration" depends on which evaluation is considered. For the Freebase experiment, the authors hand-crafted 106 templates to cover 500 triples sharing 53 distinct predicates ([Song & Zhao, 2016](https://arxiv.org/abs/1610.03807)). For the in-house power-tool KB, they hand-crafted 163 templates to cover 67 predicates ([Song & Zhao, 2016](https://arxiv.org/abs/1610.03807)). The combined total from the primary source is therefore 269 templates. A third-party research note instead records 103 power-tool templates and a total of 209, but this conflicts with the primary paper and should be treated as less reliable ([Third-party research note, n.d.]; [Song & Zhao, 2016](https://arxiv.org/abs/1610.03807)). Whichever set of figures is adopted, the broader finding holds: tying templates to predicates rather than to triples keeps human effort small while web-based expansion and embedding-based filtering scale the resulting question corpus into the tens of thousands.

## References

Song, L., & Zhao, L. (2016). *Question generation from a knowledge base with web exploration* (arXiv:1610.03807). arXiv. https://arxiv.org/abs/1610.03807

Third-party research note: Question generation from a knowledge base with web exploration. (n.d.). [Research note].