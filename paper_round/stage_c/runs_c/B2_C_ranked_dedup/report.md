# BLEU Score Differences Between the Insertion-Deletion Transformer and the Insertion-Only Baseline (KERMIT)

## Introduction

This report addresses a narrowly specified question: how large is the BLEU score difference between the proposed approach and the insertion-only method in the work described in the provided source materials? The proposed approach is the **Insertion-Deletion Transformer**, a transformer-based neural architecture and training method for sequence generation, while the comparison baseline is the **Insertion Model (KERMIT)**, described in the source material as an insertion-only baseline that extends the Insertion Transformer insertion-only framework ([document_2.txt](document_2.txt)). The central finding, established directly from the reported experimental tables, is that the difference is **not a single figure**. The work reports separate BLEU comparisons on two distinct synthetic character-based translation tasks rather than one aggregate difference ([document_2.txt](document_2.txt)). The two reported differences are **21.34 BLEU points on the alphabetic sequence shifting task** and **2.02 BLEU points on Caesar's cipher**, the latter described in the paper as "around 2 BLEU points" ([document_2.txt](document_2.txt)). Both differences favor the Insertion-Deletion model, but their magnitudes differ by more than an order of magnitude, which means that any answer to the query must be stated on a per-task basis.

## Background: The Proposed Method and the Baseline

### The Insertion-Deletion Transformer

The authors present the insertion-deletion framework as a proof of concept, applying it to two synthetic character-based translation tasks and showing that it can significantly increase the BLEU score over the insertion-only framework ([document_1.txt](document_1.txt)). The model extends the Insertion Transformer of Stern et al. (2019), an insertion-only framework, in order to handle both insertions and deletions ([document_1.txt](document_1.txt)). Structurally, the Insertion-Deletion Transformer consists of an **insertion phase** and a **deletion phase** that are executed iteratively ([document_1.txt](document_1.txt)). The insertion phase follows the typical insertion-based framework; in the deletion phase, the model is taught to perform deletions with on-policy training, sampling an input sequence on-policy from the insertion model (including on-policy insertion errors) and teaching the deletion model its appropriate deletions ([document_1.txt](document_1.txt)).

The motivation for the deletion phase is explicitly corrective. In a conventional insertion-based model, if the model makes a mistake during generation, this cannot be undone; introducing the deletion phase makes it possible to undo the mistakes made by the insertion model, because the deletion model is trained on the on-policy errors of the insertion phase ([document_1.txt](document_1.txt)). The framework is further described as allowing flexible sequence generation, parallel token generation, and text editing, and as enabling efficient handling of tasks such as text simplification and style transfer by starting the decoding process from the original source sequence ([document_1.txt](document_1.txt)). A graphical depiction of the model appears in Figure 1, which is read from bottom to top, with source and target sequences in the bottom row passed through the models to create an output sequence ([document_1.txt](document_1.txt)).

### The Insertion-Only Baseline (KERMIT)

The baseline against which the proposed approach is measured is the Insertion Model (KERMIT), characterized in the source material as the insertion-only baseline ([document_2.txt](document_2.txt)). The paper extends that insertion-only framework to handle both insertions and deletions, producing the Insertion-Deletion Model for direct comparison ([document_2.txt](document_2.txt)). Because both systems are evaluated under the same experimental protocol, the reported BLEU deltas isolate the contribution of adding the deletion phase to an otherwise insertion-based pipeline.

## Reported BLEU Score Differences

The reported BLEU scores and their differences are summarized below. All figures are as reported in the source tables ([document_2.txt](document_2.txt)).

| Task | Insertion Model (KERMIT) | Insertion-Deletion Model | Difference (BLEU points) | Direction |
|---|---|---|---|---|
| Alphabetic sequence shifting | 70.15 | 91.49 | **+21.34** | Favors Insertion-Deletion |
| Caesar's cipher | 35.55 | 37.57 | **+2.02** | Favors Insertion-Deletion |

### Alphabetic Sequence Shifting

On the alphabetic sequence shifting task, the reported BLEU scores are 91.49 for the Insertion-Deletion Model and 70.15 for the Insertion Model (KERMIT), a difference of 21.34 BLEU points in favor of the Insertion-Deletion Model ([document_2.txt](document_2.txt)). The paper reports that the Insertion-Deletion Transformer model outperforms the Insertion Transformer significantly on this task ([document_1.txt](document_1.txt)). These results are presented in Table 2 of the source paper ([document_2.txt](document_2.txt)), and an example of the interaction between the insertion and deletion model during a decoding step is shown in Table 1 ([document_1.txt](document_1.txt)).

This 21.34-point gap is the largest reported difference between the two systems and is, by a wide margin, the most consequential comparison in the paper.

### Caesar's Cipher

On Caesar's cipher, the reported BLEU scores are 37.57 for the Insertion-Deletion Model and 35.55 for the Insertion Model (KERMIT), a difference of 2.02 BLEU points, which the paper describes as "around 2 BLEU points" ([document_2.txt](document_2.txt)). These results are presented in Table 3 of the source paper ([document_2.txt](document_2.txt)). The source text states plainly that the deletion model again increases the BLEU score over just the insertion model, by around 2 BLEU points ([document_1.txt](document_1.txt)), and that the insertion-deletion model improves BLEU score on this task ([document_2.txt](document_2.txt)).

### No Single Aggregate Difference Is Reported

A critical qualification for answering the query precisely is that the paper reports separate BLEU results for two synthetic translation tasks rather than one overall BLEU difference; the comparisons are per task ([document_2.txt](document_2.txt)). Consequently, the answer to "how much is the BLEU score difference" is twofold: **21.34 BLEU points** on alphabetic sequence shifting and **2.02 BLEU points** on Caesar's cipher. Any single-number summary would misrepresent the source. The paper's overall claim, supported by both comparisons, is that the experiments on synthetic translation datasets show that the addition of deletion improves BLEU score ([document_2.txt](document_2.txt)), and that the framework can significantly increase BLEU score over the insertion-only framework ([document_1.txt](document_1.txt)).

## Experimental Conditions Underlying the Comparison

The reliability of the reported deltas depends on the conditions under which they were obtained. The source materials specify the following setup for each task.

| Task | Training examples | Held-out evaluation examples | Training steps | Batch size | Model selection |
|---|---|---|---|---|---|
| Alphabetic sequence shifting | 1,000 | 100 | 200k | 32 | None |
| Caesar's cipher | 100,000 | 1,000 | 200k | 32 | None |

For the alphabetic sequence shifting task, the authors generate 1,000 examples for training and evaluate on 100 held-out examples, training models for 200k steps with a batch size of 32 and performing no model selection ([document_1.txt](document_1.txt)). For Caesar's cipher, they generate 100k examples to train on and evaluate on 1,000 held-out examples, again training for 200k steps with a batch size of 32 and performing no model selection ([document_1.txt](document_1.txt)).

Two observations follow. First, the training data regimes are not identical across tasks: the Caesar's cipher experiment uses one hundred times more training examples (100,000 versus 1,000) and ten times more held-out evaluation examples (1,000 versus 100) than the alphabetic sequence shifting experiment ([document_1.txt](document_1.txt)). Second, the deliberate absence of model selection means the reported scores reflect single training runs under a fixed step budget rather than best-checkpoint selection, which is relevant when interpreting relatively small deltas such as the 2.02-point gain on Caesar's cipher.

An additional methodological detail concerns adversarial deletion training, which the authors found did not improve BLEU scores on these synthetic tasks; however, they note that the adversarial training scheme can still be helpful when the deletion model does not receive a signal during training by sampling from the insertion model alone, that is, when the insertion model does not make any errors ([document_1.txt](document_1.txt)). This is a constraint on when the proposed extension is expected to add value.

## Contextualizing the Magnitude of the Differences

To interpret the two deltas on comparable scales, the following derived quantities are computed from the reported BLEU values. These are author calculations based on the figures reported in the source tables and are not themselves stated in the source material ([document_2.txt](document_2.txt)).

| Task | Absolute difference (BLEU points) | Relative improvement over baseline | Reduction in "non-BLEU" gap (i.e., 1 − (100 − proposed)/(100 − baseline)) |
|---|---|---|---|
| Alphabetic sequence shifting | +21.34 | ≈ +30.4% | ≈ 71.5% |
| Caesar's cipher | +2.02 | ≈ +5.7% | ≈ 3.1% |

The contrast is substantial. On alphabetic sequence shifting, the proposed model closes roughly seven-tenths of the distance between the baseline and a perfect BLEU score, whereas on Caesar's cipher the corresponding reduction is on the order of three percent. This asymmetry is consistent with the paper's own framing: the largest and most emphatic result is the sequence shifting task, where the authors state that the model "outperforms the Insertion Transformer significantly" ([document_1.txt](document_1.txt)), while the Caesar's cipher result is presented with the more measured language of an improvement "by around 2 BLEU points" ([document_1.txt](document_1.txt)). The source material itself acknowledges the discrepancy in magnitude by describing the Caesar's cipher gain as "around 2 BLEU points" rather than as a significant improvement ([document_2.txt](document_2.txt)).

It is also worth noting that the two tasks have very different baseline difficulty levels. The insertion-only baseline already achieves 70.15 BLEU on sequence shifting but only 35.55 BLEU on Caesar's cipher ([document_2.txt](document_2.txt)). The absolute improvement is far larger on the task where the baseline was already stronger, which indicates that the benefit of the deletion phase is not simply a function of low baseline performance.

## Interpretation and Limitations

Based on the information provided, the direct answer to the query is as follows. The BLEU score difference between the proposed Insertion-Deletion Transformer and the insertion-only Insertion Model (KERMIT) is **task-dependent**, with **+21.34 BLEU points** reported on the alphabetic sequence shifting task and **+2.02 BLEU points** reported on Caesar's cipher, both favoring the proposed approach ([document_2.txt](document_2.txt)). No overall or averaged BLEU difference is reported ([document_2.txt](document_2.txt)).

Several limitations should temper any generalization from these numbers. First, both evaluations are on **synthetic character-based translation tasks**; the authors present the insertion-deletion framework as a "proof of concept" applied to these synthetic tasks ([document_1.txt](document_1.txt)). The source material does not report results on natural-language benchmarks, so the reported deltas should not be extrapolated to realistic machine translation settings. Second, the absence of model selection means the reported scores arise from single training configurations under a fixed 200k-step budget with a batch size of 32 ([document_1.txt](document_1.txt)). Third, the two experiments differ in training-set size by two orders of magnitude, which limits direct comparison between the two deltas. Fourth, the adversarial deletion training variant did not improve BLEU on these synthetic tasks, suggesting that the benefit of deletion is conditional on the insertion model producing on-policy errors ([document_1.txt](document_1.txt)).

The paper situates its contribution among related efforts in insertion-based and editing-based generation. Related work on insertion-based non- or partially autoregressive models is cited as having spiked recently, including Stern et al. (2019), Welleck et al. (2019), Gu et al. (2019a), and Chan et al. (2019), with such models described as more flexible than autoregressive counterparts because they can generate sequences in any order, benefit from parallel token generation, learn complex orderings such as tree orderings, and may be more applicable to tasks such as cloze question answering and text simplification where generation order is not naturally left to right ([document_1.txt](document_1.txt)). The authors also discuss Deliberation Networks (Xia et al., 2017) as an alternative text-editing approach that acknowledges potential benefits from post-editing output sequences and proposes a two-phase decoding framework ([document_1.txt](document_1.txt)). The reference list in the source material further includes the Insertion Transformer (Stern et al., 2019), the Levenshtein Transformer (Gu et al., 2019b), Optimal Completion Distillation for Sequence Learning (Sabour et al., 2019), "Attention Is All You Need" (Vaswani et al., 2017), and Sequence to Sequence Learning with Neural Networks (Sutskever et al., 2014) ([document_1.txt](document_1.txt)).

## Conclusion

The evidence supports a clear but qualified conclusion. Adding a deletion phase to an insertion-only generation framework yields consistent BLEU gains across the two synthetic tasks evaluated, but the magnitude of those gains ranges from marginal to substantial. The proposed Insertion-Deletion model improves over the insertion-only Insertion Model (KERMIT) by **21.34 BLEU points** on alphabetic sequence shifting (91.49 versus 70.15) and by **2.02 BLEU points** on Caesar's cipher (37.57 versus 35.55), described in the paper as "around 2 BLEU points" ([document_2.txt](document_2.txt)). Since the paper reports per-task results rather than a single aggregate difference ([document_2.txt](document_2.txt)), the most defensible answer to the query is to report both figures and to state that the direction of the effect is consistently favorable to the proposed approach. The practical implication, drawn from the relative magnitudes, is that the insertion-deletion extension appears to deliver its largest benefit on the alphabetic sequence shifting task and a comparatively modest benefit on Caesar's cipher, with the general claim that the deletion model "again increases the BLEU score over just the insertion model" holding in both cases ([document_1.txt](document_1.txt)).

## References

document_1.txt. (n.d.). *Insertion-Deletion Transformer* [Unpublished manuscript/source document].

document_2.txt. (n.d.). *Third-party research note: Insertion-Deletion Transformer* [Research note].