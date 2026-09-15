# Quantifying the BLEU Score Advantage of the Insertion-Deletion Model over the Insertion-Only KERMIT Baseline

## Executive Summary

The question posed concerns the magnitude of the BLEU score difference between a proposed approach and an insertion-only baseline. Based on the available evidence, the answer is not a single number: the advantage of the proposed Insertion-Deletion Model over the Insertion Model (KERMIT) is **task-dependent**, and the source documents report two distinct effect sizes. On the **alphabetic sequence shifting task**, the Insertion-Deletion Model achieves a BLEU score of 91.49 against 70.15 for the insertion-only baseline, a difference of **21.34 BLEU points** ([Document 2, n.d.](document_2.txt)). On **Caesar's cipher**, the same model achieves 37.57 against 35.55, a difference of **2.02 BLEU points**, which the authors themselves characterize as "around 2 BLEU points" ([Document 1, n.d.](document_1.txt); [Document 2, n.d.](document_2.txt)). In both cases the difference favors the proposed insertion-deletion architecture, but the magnitude of that advantage varies by more than an order of magnitude across the two reported evaluations ([Document 2, n.d.](document_2.txt)).

This report examines those figures in detail, situates them within the experimental protocol described in the sources, computes both absolute and relative effect sizes, and discusses the interpretive caveats that should accompany any comparison of the two tasks.

## 1. Preliminary Note on Terminology: "BELU" versus "BLEU"

The query refers to a "BELU score." No source document in the provided information uses the term "BELU"; all reported metrics are explicitly labeled **BLEU** — the bilingual evaluation understudy metric — and appear in tables titled with that metric ([Document 1, n.d.](document_1.txt); [Document 2, n.d.](document_2.txt)). It is therefore reasonable to treat "BELU" as a typographical variant of "BLEU" and to answer the query accordingly. This report proceeds on that assumption and uses "BLEU" throughout, consistent with the source terminology ([Document 1, n.d.](document_1.txt)). If the intent was some other metric, the provided evidence does not support an answer, because no alternative metric is reported anywhere in the supplied material ([Document 2, n.d.](document_2.txt)).

## 2. The Two Systems Under Comparison

### 2.1 The Proposed Approach: The Insertion-Deletion Model

The "proposed approach" in the query corresponds to the **Insertion-Deletion Model**, which extends an insertion-based generation mechanism with an explicit deletion operation ([Document 2, n.d.](document_2.txt)). The evidence for its benefit rests on comparisons against a strictly insertion-only alternative across two controlled sequence-transformation benchmarks ([Document 2, n.d.](document_2.txt)).

### 2.2 The Baseline: The Insertion Model (KERMIT)

The "insertion-only method" in the query corresponds to the **Insertion Model (KERMIT)** ([Document 1, n.d.](document_1.txt); [Document 2, n.d.](document_2.txt)). KERMIT is the comparator in both reported experiments, meaning that the same baseline is held constant across both tasks, which strengthens the internal comparability of the two reported deltas ([Document 2, n.d.](document_2.txt)).

The critical architectural distinction, as implied by the naming and by the reported pattern of results, is that the baseline can only insert tokens into a sequence, whereas the proposed model can both insert and delete ([Document 2, n.d.](document_2.txt)). This distinction matters because certain transformation tasks require the output length to differ from the input length, and a strictly insertion-only model must emulate deletions indirectly ([Document 2, n.d.](document_2.txt)).

## 3. Task 1: Alphabetic Sequence Shifting — A 21.34-Point Gain

### 3.1 Reported Figures

On the alphabetic sequence shifting task, the reported BLEU scores are **91.49** for the Insertion-Deletion Model and **70.15** for the Insertion Model (KERMIT) ([Document 2, n.d.](document_2.txt)). The difference is **21.34 BLEU points** in favor of the Insertion-Deletion Model ([Document 2, n.d.](document_2.txt)). The source explicitly states that "the Insertion-Deletion Model improves BLEU score on this task," and notes that these results are presented in Table 2 of the underlying work ([Document 2, n.d.](document_2.txt)).

### 3.2 Structured Presentation

| System | BLEU Score (Alphabetic Sequence Shifting) | Difference vs. Baseline | Relative Improvement |
|---|---|---|---|
| Insertion Model (KERMIT) — baseline | 70.15 | — | — |
| Insertion-Deletion Model — proposed | 91.49 | +21.34 | +30.42% |

*Note.* Values as reported ([Document 2, n.d.](document_2.txt)); relative improvement is computed as the absolute difference divided by the baseline score.

### 3.3 Interpretation

The 21.34-point gain is substantial in both absolute and relative terms. Relative to the baseline, it represents an improvement of approximately **30.4%** ([Document 2, n.d.](document_2.txt)). Because the baseline already sits at 70.15 BLEU, the proposed model's movement to 91.49 places it in a qualitatively different performance regime — closing most of the remaining gap to a perfect score on this task ([Document 2, n.d.](document_2.txt)). This is the headline result of the comparison and the largest reported advantage of the deletion-augmented architecture ([Document 2, n.d.](document_2.txt)).

## 4. Task 2: Caesar's Cipher — A 2.02-Point Gain

### 4.1 Reported Figures

On Caesar's cipher, the reported BLEU scores are **37.57** for the Insertion-Deletion Model and **35.55** for the Insertion Model (KERMIT) ([Document 1, n.d.](document_1.txt); [Document 2, n.d.](document_2.txt)). The difference is **2.02 BLEU points**, and the paper describes this as "around 2 BLEU points" ([Document 2, n.d.](document_2.txt)). These results are presented in Table 3 ([Document 2, n.d.](document_2.txt)). As with the previous task, the insertion-deletion model improves the BLEU score ([Document 2, n.d.](document_2.txt)).

Document 1 provides the same result in the paper's own tabular format, listing "Insertion Model (KERMIT) 35.55" and "Insertion Deletion Model 37.57" under the heading "Caesar's Cipher BLEU" ([Document 1, n.d.](document_1.txt)). Document 1 also states the finding in prose: "The table below shows that the deletion model again increases the BLEU score over just the insertion model, by around 2 BLEU points" ([Document 1, n.d.](document_1.txt)). The word "again" is significant, indicating that the Caesar's cipher result is a replication of a directional effect already observed on the other task ([Document 1, n.d.](document_1.txt)).

### 4.2 Structured Presentation

| System | BLEU Score (Caesar's Cipher) | Difference vs. Baseline | Relative Improvement |
|---|---|---|---|
| Insertion Model (KERMIT) — baseline | 35.55 | — | — |
| Insertion-Deletion Model — proposed | 37.57 | +2.02 | +5.68% |

*Note.* Values as reported ([Document 1, n.d.](document_1.txt); [Document 2, n.d.](document_2.txt)); relative improvement is computed as the absolute difference divided by the baseline score.

### 4.3 Interpretation

A 2.02-point gain is modest in absolute terms, and it corresponds to a relative improvement of approximately **5.68%** over the baseline ([Document 1, n.d.](document_1.txt)). Unlike the alphabetic sequence shifting task, the Caesar's cipher setting leaves both systems far from ceiling: both scores sit in the mid-30s on the BLEU scale ([Document 2, n.d.](document_2.txt)). This suggests that the cipher task is intrinsically harder, or that both architectures share a common bottleneck that the deletion mechanism only partially alleviates ([Document 2, n.d.](document_2.txt)).

## 5. Comparative Synthesis: One Mechanism, Two Effect Sizes

The two experiments share a baseline, a metric, and a direction of effect, but they differ sharply in the magnitude of the advantage conferred by the deletion mechanism ([Document 2, n.d.](document_2.txt)). Table 3 consolidates the comparison.

| Task | Baseline (KERMIT) | Proposed (Insertion-Deletion) | Absolute Gain | Relative Gain | Source Table |
|---|---|---|---|---|---|
| Alphabetic sequence shifting | 70.15 | 91.49 | +21.34 | +30.42% | Table 2 ([Document 2, n.d.](document_2.txt)) |
| Caesar's cipher | 35.55 | 37.57 | +2.02 | +5.68% | Table 3 ([Document 1, n.d.](document_1.txt); [Document 2, n.d.](document_2.txt)) |

The ratio between the two absolute gains is approximately **10.6 to 1** (21.34 ÷ 2.02), meaning the deletion mechanism's measured benefit on the alphabetic sequence shifting task is more than ten times larger than its measured benefit on Caesar's cipher ([Document 2, n.d.](document_2.txt)). Even in relative terms, the disparity is pronounced: 30.42% versus 5.68%, a factor of roughly 5.4 ([Document 1, n.d.](document_1.txt); [Document 2, n.d.](document_2.txt)).

The most defensible reading of this pattern is that the deletion operation provides the greatest marginal value when the underlying transformation requires the model to change sequence length or shift alignment in ways that pure insertion cannot express efficiently ([Document 2, n.d.](document_2.txt)). Conversely, where the transformation is closer to a position-preserving or length-preserving mapping, the incremental benefit of deletion shrinks considerably ([Document 1, n.d.](document_1.txt)). The evidence supports the general claim that deletion helps, and the alphabetic sequence shifting result supports the claim that it can help a great deal ([Document 2, n.d.](document_2.txt)).

## 6. Experimental Protocol Behind the Numbers

Document 1 supplies the training and evaluation configuration underlying at least one of the reported results, and this context is important for judging the reliability of the deltas ([Document 1, n.d.](document_1.txt)):

- **Training data:** 100,000 generated examples ([Document 1, n.d.](document_1.txt)).
- **Evaluation data:** 1,000 held-out examples ([Document 1, n.d.](document_1.txt)).
- **Optimization:** 200,000 training steps with a batch size of 32 ([Document 1, n.d.](document_1.txt)).
- **Model selection:** none — "we perform no model selection" ([Document 1, n.d.](document_1.txt)).
- **Illustrative transformation pair:** Source "h k b e t" mapped to Target "g j a d s" ([Document 1, n.d.](document_1.txt)).

The absence of model selection is methodologically notable: it means the reported scores are not the product of cherry-picking the best checkpoint against the evaluation set, which strengthens confidence that the 2.02-point Caesar's cipher gain is a genuine architectural effect rather than an artifact of selection ([Document 1, n.d.](document_1.txt)). At the same time, the sources do not report confidence intervals, standard deviations, or significance tests for either comparison, so the precision of the 21.34-point and 2.02-point figures cannot be independently assessed from the provided material ([Document 1, n.d.](document_1.txt); [Document 2, n.d.](document_2.txt)).

## 7. Limitations and Caveats

Several limitations should temper any strong conclusion drawn from these figures.

First, the evidence covers only **two tasks**, both of which are synthetic, cipher-like sequence transformations rather than natural-language problems ([Document 1, n.d.](document_1.txt); [Document 2, n.d.](document_2.txt)). Generalization to broader translation or generation settings is not established by the provided material.

Second, the two tasks are not directly comparable in difficulty: baseline BLEU is 70.15 on one and 35.55 on the other, so the headroom available for improvement differs substantially ([Document 2, n.d.](document_2.txt)). A 21.34-point gain on a task starting near 70 BLEU and a 2.02-point gain on a task starting near 35 BLEU reflect different ceilings and should not be treated as interchangeable measures of the mechanism's value ([Document 2, n.d.](document_2.txt)).

Third, BLEU is itself a surface-overlap metric, and the sources do not provide complementary metrics or human evaluations ([Document 1, n.d.](document_1.txt); [Document 2, n.d.](document_2.txt)). The direction of the effect is consistent across both tasks, which is reassuring, but the magnitude on the cipher task in particular is small enough that evaluation noise could, in principle, account for part of it — a possibility that cannot be ruled out from the information given ([Document 1, n.d.](document_1.txt)).

## 8. Conclusion

The BLEU score difference between the proposed Insertion-Deletion Model and the insertion-only KERMIT baseline is **+21.34 points on the alphabetic sequence shifting task** (91.49 vs. 70.15) and **+2.02 points on Caesar's cipher** (37.57 vs. 35.55) ([Document 1, n.d.](document_1.txt); [Document 2, n.d.](document_2.txt)). The paper itself summarizes the latter as "around 2 BLEU points" ([Document 2, n.d.](document_2.txt)). The proposed approach therefore outperforms the insertion-only method on both reported benchmarks, but the practical significance of that improvement is highly task-contingent: it is transformative on alphabetic sequence shifting and marginal on Caesar's cipher ([Document 1, n.d.](document_1.txt); [Document 2, n.d.](document_2.txt)). Any single-number answer to the query would misrepresent the evidence; the defensible answer is a two-part one, with the 21.34-point gap representing the strongest reported case for the deletion mechanism and the 2.02-point gap representing its weakest ([Document 2, n.d.](document_2.txt)).

## References

Document 1. (n.d.). *Source and target examples, training configuration, and Caesar's cipher BLEU results* [Unpublished manuscript]. document_1.txt

Document 2. (n.d.). *Reported BLEU scores for the alphabetic sequence shifting task and Caesar's cipher* [Unpublished manuscript]. document_2.txt