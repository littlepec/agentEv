# How Many Hand-Crafted Templates Did They Have to Make? A Detailed Analysis of Template Construction in "Question Generation from a Knowledge Base with Web Exploration"

## Executive Summary

The system described in "Question Generation from a Knowledge Base with Web Exploration" requires **106 hand-crafted question templates** for its domain-general Freebase evaluation and **163 templates** for its specialized in-house power tool knowledge base (KB) ([Song & Zhao, n.d.-a](document_1.txt); [Third-party research note, n.d.](document_2.txt)). The 106 Freebase templates were derived from 500 randomly selected triples that share only 53 distinct predicates, meaning the authors built roughly **two templates per predicate on average** ([Song & Zhao, n.d.-a](document_1.txt)). The paper explicitly states that template construction constitutes **"the only human labor in this work"** ([Song & Zhao, n.d.-a](document_1.txt)). This report examines those figures in depth, places them in the context of the system's overall architecture, and evaluates why such a comparatively small manual investment was sufficient to generate tens of thousands of candidate questions.

## Introduction: Why Template Counts Matter

Question generation from a knowledge base (KB) is the task of producing natural-language questions that relate to the domain of an input KB ([Song & Zhao, n.d.-a](document_1.txt)). Such questions are valuable for student assessment and coaching in educational and professional contexts, and large-scale question–answer corpora are critical to downstream NLP tasks including question answering, dialogue interaction, and intelligent tutoring systems ([Song & Zhao, n.d.-a](document_1.txt)).

The central technical difficulty is that KBs abstract away precisely the information a fluent question requires. As the paper notes, "function words and morphological forms for entities are abstracted away when a KB is created" ([Song & Zhao, n.d.-a](document_1.txt)). A triple such as ⟨jigsaw, performsActivity, CurveCut⟩ contains no surface realization of "how to use jigsaw" — that mapping must be supplied externally ([Song & Zhao, n.d.-a](document_1.txt)).

Prior work attacked this problem with massive human-labeled data: Seyler et al. (2015) and Serban et al. (2016) treat question generation as a machine translation problem, training a neural machine translation (NMT) system on 10,000 ⟨triple, question⟩ pairs whose question components were human-generated ([Song & Zhao, n.d.-a](document_1.txt)). The authors of the present system position their contribution as a radical reduction of exactly this annotation burden: rather than labeling 10,000 question strings, they label a small set of templates tied to predicates, and let the web supply the rest ([Song & Zhao, n.d.-a](document_1.txt)).

Consequently, the number of hand-crafted templates is not a peripheral implementation detail. It is the paper's headline efficiency claim, and the figure most directly comparable against prior work's annotation cost.

## The Direct Answer

### Freebase Evaluation: 106 Hand-Crafted Templates

For the primary comparison against the prior state of the art, the authors sampled 500 triples at random from Freebase, a domain-general KB ([Song & Zhao, n.d.-a](document_1.txt)). For those 500 triples they hand-crafted **106 templates** ([Song & Zhao, n.d.-a](document_1.txt); [Third-party research note, n.d.](document_2.txt)). The reason the count is so much smaller than the triple count is that the 500 triples share only **53 distinct predicates**; the authors therefore produced about **two templates per predicate** on average ([Song & Zhao, n.d.-a](document_1.txt)).

Applying those 106 templates to the triples produced **991 seed questions** ([Song & Zhao, n.d.-a](document_1.txt)). A further **1,529 questions** were retrieved from Google through iterative web expansion ([Song & Zhao, n.d.-a](document_1.txt)). From the resulting candidate pool, the top 500 questions were selected using an averaged language-model score as the ranking index ([Song & Zhao, n.d.-a](document_1.txt)).

### In-House Power Tool Domain: 163 Templates

The third experiment applies the same end-to-end pipeline to a highly specialized in-house KB in the power tool domain, containing **67 distinct predicates, 293 distinct subjects, and 279 distinct objects** ([Song & Zhao, n.d.-a](document_1.txt)). Here the reported figure is **163 templates** ([Song & Zhao, n.d.-a](document_1.txt)), or roughly 2.4 templates per predicate. This template set yielded **12,228 seed questions**, from which **20,000 more questions** were expanded using Google ([Song & Zhao, n.d.-a](document_1.txt)).

### Summary Table

| Knowledge base | Distinct predicates | Hand-crafted templates | Templates per predicate | Seed questions generated | Additional questions from web expansion |
|---|---|---|---|---|---|
| Freebase (500 random triples) | 53 | 106 | ≈2.0 | 991 | 1,529 |
| In-house power tool KB | 67 | 163 | ≈2.4 | 12,228 | 20,000 |

*Sources: ([Song & Zhao, n.d.-a](document_1.txt); [Third-party research note, n.d.](document_2.txt)).*

## The Design Logic Behind the Template Set

Templates are "a transcription of the predicate in the KB (e.g. performsActivity ⇒ how to)" together with placeholders for the subject (#X#) and the object (#Y#) ([Song & Zhao, n.d.-a](document_1.txt)). Each template is associated with a single predicate, so template creation scales with predicate coverage rather than with the number of triples or entities ([Song & Zhao, n.d.-a](document_1.txt); [Third-party research note, n.d.](document_2.txt)).

The paper gives a concrete worked example. For the predicate "performsActivity," the template "how to use #X#" is constructed once; applying it to the triple ⟨jigsaw, performsActivity, CurveCut⟩ produces the seed question "how to use jigsaw," which is then submitted to Google to retrieve related questions ([Song & Zhao, n.d.-a](document_1.txt)).

The third-party note frames this as the key structural insight: "This design ties template creation to predicates, keeping the template set compact relative to the triple set" ([Third-party research note, n.d.](document_2.txt)). In other words, the 106 Freebase templates are not 106 independent writing tasks matched to 500 data points; they are roughly 53 predicate-level decisions, each instantiated one to three times.

## Why So Few Templates Are Sufficient

The authors offer two explicit reasons why their system "does not require a large number of templates" ([Song & Zhao, n.d.-a](document_1.txt)):

1. **Iterative expansion amplifies seeds.** Even a relatively small seed set can produce a large number of questions through web expansion. Empirically, 991 seeds produced at least 1,529 additional candidates in the Freebase setting, and 12,228 seeds produced 20,000 more in the power tool setting ([Song & Zhao, n.d.-a](document_1.txt)).
2. **Entity sharing of predicates.** Multiple entities in the KB share the same predicates, so a single predicate-level template covers many triples ([Song & Zhao, n.d.-a](document_1.txt)).

A third, practical advantage is also claimed: because the web is self-updating, the system "can easily generate updated questions" without revisiting the manual template set ([Song & Zhao, n.d.-a](document_1.txt)). This means the 106 (or 163) templates are a one-time capital cost, not a recurring maintenance burden.

## The Expansion Pipeline That Consumes the Templates

Understanding the template count requires understanding what happens to it. The seed question set S is generated by applying the template set to the KB ([Song & Zhao, n.d.-a](document_1.txt)). Algorithm 1 then operates as follows ([Song & Zhao, n.d.-a](document_1.txt)):

| Step | Operation |
|---|---|
| Initialization | Expanded set E ← S; queue Q ← S; iteration counter I ← 0 |
| Loop condition | While len(Q) > 0 and I < I_max |
| Iteration | I ← I + 1; q_cur ← Q.Pop() |
| Web expansion | For each q_next in WebExp(q_cur): if E does not contain q_next, append to E and push to Q |
| Termination | Loop ends when the queue is empty or I_max is reached |

Because loops can generate large volumes, the authors cap the maximum number of iterations with I_max ([Song & Zhao, n.d.-a](document_1.txt)). Retrieved candidates are then filtered by two thresholds — t_rel for domain relevance and t_flu for fluency ([Song & Zhao, n.d.-a](document_1.txt)). Domain relevance is computed as the cosine similarity between the question embedding and the embedding of the seed-question set treated as in-domain data D_in, where v(·) is the averaged word embedding within the document ([Song & Zhao, n.d.-a](document_1.txt)). Fluency uses an averaged language-model score, AvgLM(q) = Lm(q)/Len(q), where Lm(·) is a general-domain language-model log-probability and Len(·) is the word count ([Song & Zhao, n.d.-a](document_1.txt)).

The filtering step matters because "the domain relevance drops significantly as the iteration goes on" ([Song & Zhao, n.d.-a](document_1.txt)). Thus the small hand-crafted template set is protected by an automated quality gate rather than by exhaustive manual authoring.

## Reported Evaluation Outcomes

Human evaluation used three native English speakers rating fluency and naturalness on a 4-point scheme, where 4 is best, applied to both systems' outputs on the 500 Freebase triples ([Song & Zhao, n.d.-a](document_1.txt)).

| System | Grammaticality | Naturalness |
|---|---|---|
| Prior state of the art (Serban et al., 2016) | 3.36 | 3.14 |
| Proposed system | 3.53 | 3.31 |

*Source: ([Song & Zhao, n.d.-a](document_1.txt)).*

The authors observe that naturalness scores fall below grammaticality scores for both systems because "naturalness is a more strict metric since a natural question should also be grammatical" ([Song & Zhao, n.d.-a](document_1.txt)). Qualitative examples in Table 1 of the paper show baseline errors such as "whats the title of a book of the subject of the bible ?" (ungrammatical), "what 's one of the mountain where can you found in argentina in netflix ?" (unnatural), and "who was someone who was involved in the leukemia ?" (confusing), against more idiomatic outputs from the proposed system ([Song & Zhao, n.d.-a](document_1.txt)).

The domain-relevance component was separately validated on the web snippet dataset — 10,060 training and 2,280 test snippets in 8 classes, averaging 18 words each ([Song & Zhao, n.d.-a](document_1.txt)).

| Method | Precision |
|---|---|
| Baseline approach 1 | 82.18 |
| Baseline approach 2 | 85.31 |
| Baseline approach 3 | 85.48 |
| Proposed method | 85.65 |

*Source: ([Song & Zhao, n.d.-a](document_1.txt)).*

The authors attribute the advantage to word embeddings capturing similarity between distinct words (e.g., "finance" and "economy"), whereas LDA-based methods only learn probabilities of words belonging to topics ([Song & Zhao, n.d.-a](document_1.txt)).

## A Discrepancy Between the Sources Worth Flagging

The two provided sources disagree on one point regarding the power tool templates. The primary document states plainly: "For the 6 7 predicates, we hand-craft 1 6 3 templates" ([Song & Zhao, n.d.-a](document_1.txt)). The third-party research note, however, asserts that these particular templates "were generated automatically from the predicate names rather than hand-crafted" ([Third-party research note, n.d.](document_2.txt)).

Given the reporting guidelines favoring primary sources for factual claims, this report treats the **106 Freebase templates as unambiguously hand-crafted** — the paper twice states the templates are "hand-crafted" and designates template construction as the only human labor ([Song & Zhao, n.d.-a](document_1.txt)). The Freebase figure is therefore the most reliable answer to the query. For the power tool KB, the primary text's "hand-craft" wording and the secondary note's "automatic" wording cannot both be true; a reasonable reconciliation is that the predicate-name-to-template mapping was systematized for the specialized KB, but the supplied evidence does not permit a firm conclusion. The safe, defensible statement is that the paper reports **163 templates for the 67 power tool predicates**, with the primary source describing them as hand-crafted ([Song & Zhao, n.d.-a](document_1.txt); [Third-party research note, n.d.](document_2.txt)).

Notably, even the third-party note confirms the headline framing: "The Freebase and power tool counts provide the reported template-construction figures for the system. These figures show the template-building effort scales with predicate coverage in each evaluation" ([Third-party research note, n.d.](document_2.txt)).

## Interpretation and Implications

Read together, the figures support a specific and defensible claim: the manual bottleneck in KB question generation can be moved from the *question* level to the *predicate* level. Rather than labeling 10,000 complete questions, as the NMT approach does ([Song & Zhao, n.d.-a](document_1.txt)), the authors label 106 templates for 53 predicates and let a search engine plus two automated filters do the rest.

The economics are stark. In the Freebase setting, 106 templates produced 991 seed questions — roughly 9.3 questions per template before any web expansion — and 2,520 total candidates once the 1,529 Google-retrieved questions are included ([Song & Zhao, n.d.-a](document_1.txt)). In the power tool setting, 163 templates produced 12,228 seeds — about 75 seeds per template — and over 32,000 candidates in total ([Song & Zhao, n.d.-a](document_1.txt)). The amplification ratio grows with the number of entities per predicate, which is exactly what the design predicts.

Two caveats temper the claim. First, the top-500 selection for the Freebase comparison was made with an automatic language-model score, not with human judgment on the full pool ([Song & Zhao, n.d.-a](document_1.txt)); the human evaluation therefore assesses the best-selected outputs rather than the average of the generated set. Second, the system generates questions **without answers**, which the authors explicitly leave to future work ([Song & Zhao, n.d.-a](document_1.txt)). Both limitations are relevant to anyone extrapolating the low template count into a claim about full question–answer corpus construction.

## Conclusion

The direct answer to the query is that the authors hand-crafted **106 templates** for the 500-triple Freebase evaluation, covering 53 distinct predicates at roughly two templates per predicate, and **163 templates** for the 67-predicate in-house power tool knowledge base ([Song & Zhao, n.d.-a](document_1.txt); [Third-party research note, n.d.](document_2.txt)). The paper's central efficiency argument rests on this number: template construction is the *only* human labor in the pipeline, and it is organized around predicates rather than triples, so a compact manual artifact can seed thousands of fluent, domain-relevant questions through iterative web retrieval plus fluency and relevance filtering ([Song & Zhao, n.d.-a](document_1.txt)). Human graders rated the resulting questions higher in both grammaticality (3.53 vs. 3.36) and naturalness (3.31 vs. 3.14) than the prior NMT-based state of the art on the same 500 triples ([Song & Zhao, n.d.-a](document_1.txt)).

## References

Song, L., & Zhao, L. (n.d.-a). *Question generation from a knowledge base with web exploration* [document_1.txt]. Computer Science Department, University of Rochester; Bosch Research and Technology Center.

Third-party research note: *Question generation from a knowledge base with web exploration* [document_2.txt]. (n.d.).