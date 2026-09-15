# BLEU Score Differences Between the Insertion-Deletion Transformer and the Insertion-Only (KERMIT) Baseline

## Abstract

This report examines the magnitude of the reported BLEU score gap (spelled "BELU" in the query) between the proposed **Insertion-Deletion Transformer** and the **Insertion Model (KERMIT)** insertion-only baseline. Based on the supplied source documents, the answer is that **there is no single, aggregate BLEU difference**; instead, the paper reports two task-specific comparisons. On the Caesar's cipher task, the Insertion-Deletion Model scores 91.49 BLEU versus 70.15 BLEU for the Insertion Model, a difference of **21.34 BLEU points in favor of the proposed approach** ([document_2.txt](document_2.txt)). On the shifted alphabetic sequence task, the Insertion-Deletion Model scores 37.57 BLEU versus 35.55 BLEU for the Insertion Model, a difference of **2.02 BLEU points (described in the paper as "around 2 BLEU points")** ([document_2.txt](document_2.txt); [document_1.txt](document_1.txt)). Both comparisons favor the insertion-deletion extension, but the effect size varies by roughly an order of magnitude across the two synthetic tasks.

## Introduction and Framing of the Query

The query asks how large the BLEU gap is between the proposed approach and the insertion-only method. Answering this precisely requires two clarifications derived from the source material. First, the metric is BLEU (bilingual evaluation understudy), a standard sequence-generation quality metric; the query's spelling "BELU" is a typographical variant that does not alter the interpretation. Second, and more importantly, the source documents explicitly caution that the paper reports **"separate BLEU results for two synthetic translation tasks rather than one overall BLEU difference"** ([document_2.txt](document_2.txt)). Therefore, any honest answer must present a per-task decomposition rather than a single number.

This framing matters because a naive reader might expect one headline improvement figure. The third-party research note states outright that "the comparisons are per task: 21.34 BLEU points on Caesar's cipher and 2.02 BLEU points on the shifted alphabetic sequence task, described as around 2 BLEU points" ([document_2.txt](document_2.txt)). The remainder of this report details the architecture, the experimental setup, the exact figures, and an interpretation of why the two differences diverge so strongly.

## The Proposed Approach and the Insertion-Only Baseline

The proposed approach is the **Insertion-Deletion Transformer**, described as "a transformer-based neural architecture and training method for sequence generation" ([document_2.txt](document_2.txt)). The insertion-only baseline is the **Insertion Model (KERMIT)**, which "extends the Insertion Transformer insertion-only framework to handle insertions" ([document_2.txt](document_2.txt)). The paper itself describes the relationship directly: "we describe our Insertion-Deletion model. We extend the Insertion Transformer Stern et al. 2019, an insertion-only framework to handle both insertions and deletions" ([document_1.txt](document_1.txt)).

Architecturally, the Insertion-Deletion Transformer "can be implemented with a simple stack of two Transformer decoders, where the top deletion transformer layer gets its signal from the bottom insertion transformer" ([document_1.txt](document_1.txt)). The framework comprises "one insertion phase and one deletion phase, without the need to predict the number of tokens needed to be inserted," which "greatly simplifies the model architecture, training procedure and inference runtime" ([document_1.txt](document_1.txt)).

The functional rationale for adding deletion is that it enables error correction: "In a conventional insertion-based model, if the model makes a mistake during generation, this cannot be undone. Introducing the deletion phase makes it possible to undo the mistakes made by the insertion model, since it is trained on the on-policy errors of the insertion phase" ([document_1.txt](document_1.txt)). The framework also "allows for flexible sequence generation, parallel token generation and text editing," and "enables the framework to efficiently handle tasks like text simplification and style transfer by starting the decoding process from the original source sequence" ([document_1.txt](document_1.txt)).

## Reported BLEU Results

The core data answering the query are the two per-task comparisons. The table below consolidates the figures reported across the two source documents.

| Task | Insertion Model (KERMIT) BLEU | Insertion-Deletion Model BLEU | Difference (BLEU points) | Reported Table |
|---|---|---|---|---|
| Caesar's cipher | 70.15 | 91.49 | +21.34 | Table 2 |
| Shifted alphabetic sequence | 35.55 | 37.57 | +2.02 | Table 3 |

Sources: ([document_2.txt](document_2.txt); [document_1.txt](document_1.txt)).

The source documents state these comparisons explicitly. On the first task, "the reported BLEU scores are 91.49 for the Insertion-Deletion Model and 70.15 for the Insertion Model (KERMIT). The difference is 21.34 BLEU points in favor of the Insertion-Deletion Model. Table 2 presents these results. The Insertion-Deletion Model improves BLEU score on this task" ([document_2.txt](document_2.txt)). On the second task, "the reported BLEU scores are 37.57 for the Insertion-Deletion Model and 35.55 for the Insertion Model (KERMIT). The difference is 2.02 BLEU points. The paper describes this as around 2 BLEU points. Table 3 presents these results. The insertion-deletion model improves BLEU score on this task" ([document_2.txt](document_2.txt)).

The primary paper corroborates the smaller gap in its narrative: "The table below shows that the deletion model again increases the BLEU score over just the insertion model, by around 2 BLEU points" ([document_1.txt](document_1.txt)). It also corroborates the larger gap with a qualitative claim: "We see our Insertion-Deletion Transformer model outperforms the Insertion Transformer significantly on this task" ([document_1.txt](document_1.txt)).

### Summary Answer to the Query

If the question is interpreted as "what is the BLEU difference between the proposed approach and the insertion-only method?", the defensible answer is: **the difference is task-dependent and is reported as 21.34 BLEU points on one synthetic task and 2.02 BLEU points on the other, with both differences favoring the Insertion-Deletion Transformer** ([document_2.txt](document_2.txt)). There is no overall pooled difference in the provided material.

## Experimental Setup Behind the Numbers

The magnitude of the two gaps is best understood alongside the experimental conditions. The source documents provide the following setup details.

For the sequence-shifting-style experiment, "We generate 1000 of examples for training, and evaluate on 100 held-out examples. Table 2 reports our BLEU. We train our models for 200k steps, batch size of 32 and perform no model selection" ([document_1.txt](document_1.txt)). For the other experiment, "We generate 100k examples to train on, and evaluate on 1000 held-out examples. We train our models for 200k steps, batch size of 32 and perform no model selection" ([document_1.txt](document_1.txt)).

| Experimental Parameter | Experiment A | Experiment B |
|---|---|---|
| Training examples | 1,000 | 100,000 |
| Held-out evaluation examples | 100 | 1,000 |
| Training steps | 200k | 200k |
| Batch size | 32 | 32 |
| Model selection | None | None |

Sources: ([document_1.txt](document_1.txt)).

Two observations follow. First, the experiment with the dramatically larger BLEU gap (21.34 points) is also the one with the far larger training set (100,000 examples versus 1,000), which is consistent with the deletion module having more on-policy insertion errors to learn from. Second, the shared hyperparameters (200k steps, batch size 32, no model selection) indicate that the reported deltas are not artifacts of differing training budgets between the two model variants ([document_1.txt](document_1.txt)).

The paper also notes a negative result relevant to interpreting the gap: "We found that adversarial deletion training did not improve BLEU scores on these synthetic tasks. However, the adversarial training scheme can still be helpful when the deletion model does not receive a signal during training by sampling from the insertion model alone (i.e., when the insertion-model does not make any errors)" ([document_1.txt](document_1.txt)). This suggests the observed gains stem from the deletion mechanism itself rather than from adversarial refinements.

## Interpretation: Why the Two Differences Diverge

The 21.34-point and 2.02-point gaps are not contradictory; they reflect different task difficulty and different headroom. On the task where the insertion-only baseline already performs strongly (70.15 BLEU), the deletion phase delivers a large absolute gain of 21.34 points ([document_2.txt](document_2.txt)). On the task where the insertion-only baseline is much weaker overall (35.55 BLEU), the incremental benefit is only about 2 BLEU points ([document_2.txt](document_2.txt); [document_1.txt](document_1.txt)).

One plausible, source-grounded reading is that the deletion phase adds the most value when insertion errors are structured and correctable — precisely the scenario the paper invokes when it argues that deletion "makes it possible to undo the mistakes made by the insertion model, since it is trained on the on-policy errors of the insertion phase" ([document_1.txt](document_1.txt)). Where errors are less systematic or the overall sequence modeling problem is harder, the ceiling for post-hoc correction is lower, producing the ~2-point improvement.

The paper's own summary is deliberately qualitative on this point: "We demonstrated the capabilities of the model on two synthetic data sets and showed that the deletion model can significantly increase the BLEU score on simple tasks by iteratively refining the output sequence via sequences of insertion-deletions" ([document_1.txt](document_1.txt)). The phrase "iteratively refining" aligns with the described decoding dynamic, in which insertions and deletions interact within a decoding step ([document_1.txt](document_1.txt)). A worked decoding example is illustrated in Table 1 of the paper, which shows "Predicted deletions," an output sequence containing `[CLS]`, `[SEP]` tokens, and a deleted token `u`, described as "an example decoding iteration during inference" ([document_1.txt](document_1.txt)).

## Methodological Caveats and Source Reliability

Two cautions should accompany the headline numbers.

### Task-to-Table Labeling Inconsistency

The two source documents do not fully agree on how the figures map onto named tasks and table numbers. The third-party research note assigns 91.49 vs 70.15 to Caesar's cipher (Table 2) and 37.57 vs 35.55 to the shifted alphabetic sequence (Table 3) ([document_2.txt](document_2.txt)). The primary-paper excerpts, however, show a table captioned "Alphabetic Sequence Shifting BLEU" containing the 70.15 and 91.49 values as Table 2, and a table captioned "Caesar's Cipher BLEU" containing the 35.55 and 37.57 values as Table 3 ([document_1.txt](document_1.txt)). This is an internal labeling conflict in the supplied material. Importantly, **the numerical deltas themselves are unaffected**: whichever label is correct, the two gaps are 21.34 BLEU points and 2.02 BLEU points, both favoring the insertion-deletion model ([document_2.txt](document_2.txt); [document_1.txt](document_1.txt)). Where this report names tasks above, it follows the third-party research note, which is the more internally consistent summary document.

### Scope of Evidence

Both documents are excerpt-based and concern only two synthetic character-based translation tasks. The paper itself positions the work as "a proof of concept by applying it to two synthetic character-based translation tasks and showing it can significantly increase the BLEU score over the insertion-only framework" ([document_1.txt](document_1.txt)). Consequently, the 21.34-point and 2.02-point figures should be read as evidence of directional improvement on controlled synthetic tasks, not as estimates of gains on natural-language benchmarks.

## Conclusions

The evidence in the provided sources supports the following concrete findings:

1. The proposed approach is the **Insertion-Deletion Transformer**, an extension of the Insertion Transformer framework that adds a deletion phase on top of insertion-only generation ([document_2.txt](document_2.txt); [document_1.txt](document_1.txt)).
2. The insertion-only baseline is the **Insertion Model (KERMIT)** ([document_2.txt](document_2.txt)).
3. On one synthetic task, the BLEU difference is **21.34 points** (91.49 vs 70.15) in favor of the Insertion-Deletion Model ([document_2.txt](document_2.txt)).
4. On the second synthetic task, the BLEU difference is **2.02 points** (37.57 vs 35.55), described by the paper as around 2 BLEU points ([document_2.txt](document_2.txt); [document_1.txt](document_1.txt)).
5. There is **no single overall BLEU difference** reported; the paper presents separate per-task results ([document_2.txt](document_2.txt)).

In short, the answer to "How much is the BLEU score difference between the proposed approach and the insertion-only method?" is **not one number but two: approximately 21.3 BLEU points on one task and approximately 2.0 BLEU points on the other, with the proposed insertion-deletion model ahead in both cases** ([document_2.txt](document_2.txt)). The consistency of direction — "The experiments on synthetic translation datasets show that the addition of deletion improves BLEU score" ([document_2.txt](document_2.txt)) — is the strongest generalizable claim the sources support, while the variable magnitude underscores the task-dependence of the improvement.

## References

Insertion-Deletion Transformer [Manuscript excerpts, document_1.txt]. (n.d.). ([document_1.txt](document_1.txt))

Third-party research note: Insertion-Deletion Transformer [Research note, document_2.txt]. (n.d.). ([document_2.txt](document_2.txt))