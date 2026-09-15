# Quantifying the BLEU Score Difference Between the Insertion-Deletion Transformer and the Insertion-Only Baseline

## Introduction

The query asks how large the BLEU score difference is between the proposed approach and the insertion-only method. Based on the available source material, the answer is not a single number. The paper reports two separate synthetic translation experiments, and the reported advantage of the Insertion-Deletion Transformer over the Insertion Model (KERMIT) differs substantially by task. The two headline gaps are **21.34 BLEU points** on one task and **2.02 BLEU points** — described by the authors as "around 2 BLEU points" — on the other ([document_2.txt](document_2.txt); [document_1.txt](document_1.txt)). Both gaps favor the insertion-deletion approach. This report documents the exact figures, the experimental conditions under which they were obtained, and a reconciliation of an inconsistency between the two source documents regarding which task produced which score set.

## Background: The Two Architectures Being Compared

### The proposed approach: Insertion-Deletion Transformer

The proposed approach is the Insertion-Deletion Transformer, described as a transformer-based neural architecture and training method for sequence generation ([document_2.txt](document_2.txt)). Architecturally, it can be implemented as a simple stack of two Transformer decoders, where the top deletion transformer layer receives its signal from the bottom insertion transformer ([document_1.txt](document_1.txt)). The method extends the Insertion Transformer of Stern et al. (2019), an insertion-only framework, so that it handles both insertions and deletions ([document_1.txt](document_1.txt)).

The training and inference procedure comprises one insertion phase and one deletion phase, without the need to predict the number of tokens that must be inserted. According to the paper, this greatly simplifies the model architecture, the training procedure, and the inference runtime ([document_1.txt](document_1.txt)).

### The baseline: Insertion Model (KERMIT)

The insertion-only baseline is the Insertion Model (KERMIT), which extends the Insertion Transformer insertion-only framework to handle insertions ([document_2.txt](document_2.txt)). The paper then extends that insertion-only framework to handle both insertions and deletions, producing the Insertion-Deletion Model for direct comparison ([document_2.txt](document_2.txt)). Because both systems share the same insertion backbone, the reported comparisons isolate the contribution of adding the deletion phase.

### Why deletion is expected to help

In a conventional insertion-based model, if the model makes a mistake during generation, that mistake cannot be undone. Introducing the deletion phase makes it possible to undo mistakes made by the insertion model, since the deletion model is trained on the on-policy errors of the insertion phase ([document_1.txt](document_1.txt)). The deletion extension also enables the framework to handle tasks such as text simplification and style transfer by starting the decoding process from the original source sequence ([document_1.txt](document_1.txt)). More broadly, the paper situates itself within a recent spike of research on insertion-based non- or partially-autoregressive models (Stern et al., 2019; Welleck et al., 2019; Gu et al., 2019a; Chan et al., 2019), which are more flexible than autoregressive counterparts, can generate sequences in any order, and can benefit from parallel token generation ([document_1.txt](document_1.txt)).

## The Reported BLEU Figures

The paper reports separate BLEU results for two synthetic translation tasks rather than one overall BLEU difference. The comparisons are per task: 21.34 BLEU points on one task and 2.02 BLEU points on the other, the latter described as around 2 BLEU points ([document_2.txt](document_2.txt)). The experiments on synthetic translation datasets show that the addition of deletion improves the BLEU score ([document_2.txt](document_2.txt)).

### Score table

| Metric | Insertion Model (KERMIT) | Insertion-Deletion Model | Difference |
|---|---|---|---|
| Task A BLEU | 70.15 | 91.49 | **+21.34** |
| Task B BLEU | 35.55 | 37.57 | **+2.02** |

Both rows are reported in the source material ([document_2.txt](document_2.txt); [document_1.txt](document_1.txt)). The remaining question is which task corresponds to which row, because the two source documents label the tasks differently.

### Task naming and table numbering per document_1.txt

The underlying manuscript excerpt — document_1.txt — presents the results in two numbered tables. The table labeled "Alphabetic Sequence Shifting BLEU" lists the Insertion Model (KERMIT) at 70.15 and the Insertion-Deletion Model at 91.49, and is presented as Table 2 ([document_1.txt](document_1.txt)). The table labeled "Caesar's Cipher BLEU" lists the Insertion Model (KERMIT) at 35.55 and the Insertion-Deletion Model at 37.57, and is presented as Table 3 ([document_1.txt](document_1.txt)).

### Task naming per document_2.txt

The third-party research note — document_2.txt — states that on the Caesar's cipher task the reported BLEU scores are 91.49 for the Insertion-Deletion Model and 70.15 for the Insertion Model (KERMIT), a difference of 21.34 BLEU points in favor of the Insertion-Deletion Model, presented in Table 2 ([document_2.txt](document_2.txt)). It further states that on the shifted alphabetic sequence task the reported BLEU scores are 37.57 for the Insertion-Deletion Model and 35.55 for the Insertion Model (KERMIT), a difference of 2.02 BLEU points, presented in Table 3 ([document_2.txt](document_2.txt)).

### The discrepancy, stated plainly

The two documents agree on the four numeric values and on both differences, but they swap the task labels:

| Source | 91.49 vs 70.15 (+21.34) | 37.57 vs 35.55 (+2.02) |
|---|---|---|
| document_1.txt (table labels) | Alphabetic Sequence Shifting (Table 2) | Caesar's Cipher (Table 3) |
| document_2.txt (research note) | Caesar's Cipher (Table 2) | Shifted Alphabetic Sequence (Table 3) |

This is a labeling conflict, not a numerical conflict. The magnitude of the insertion-deletion advantage on each dataset is unaffected: one dataset shows a large gain of 21.34 BLEU points, and the other shows a modest gain of 2.02 BLEU points ([document_1.txt](document_1.txt); [document_2.txt](document_2.txt)).

## Which Mapping Is Better Supported?

On the evidence available, the mapping implied by document_1.txt is the better supported, for three reasons.

First, document_1.txt is the primary source; document_2.txt is explicitly a third-party research note synthesizing the paper ([document_2.txt](document_2.txt)). Where a synthesis conflicts with the primary text, the primary text should generally be weighted more heavily.

Second, the surrounding manuscript prose in document_1.txt is internally consistent with its own table labels. The section "3.1 Learning shifted alphabetic sequences" precedes Table 2, and the text immediately before that table states: "We generate 1000 of examples for training, and evaluate on 100 held-out examples. Table 2 reports our BLEU... We see our Insertion-Deletion Transformer model outperforms the Insertion Transformer significantly on this task." This precedes the "Alphabetic Sequence Shifting BLEU" table showing 70.15 and 91.49, and the word "significantly" matches a 21.34-point gap ([document_1.txt](document_1.txt)).

Third, the section "3.2 Learning Caesar's Cipher" follows, and the text preceding Table 3 states: "We generate 100k examples to train on, and evaluate on 1000 held-out examples... The table below shows that the deletion model again increases the BLEU score over just the insertion model, by around 2 BLEU points." This precedes the "Caesar's Cipher BLEU" table showing 35.55 and 37.57 ([document_1.txt](document_1.txt)). The phrase "again increases" and the explicit "around 2 BLEU points" match the 2.02-point gap exactly.

Under this reading, the mapping is: the small-data alphabetic sequence shifting task (1,000 training examples, 100 held-out) produced 70.15 → 91.49, a gain of 21.34 BLEU points; the larger-data Caesar's cipher task (100,000 training examples, 1,000 held-out) produced 35.55 → 37.57, a gain of 2.02 BLEU points ([document_1.txt](document_1.txt)).

Both tasks were trained for 200,000 steps with batch size 32 and no model selection ([document_1.txt](document_1.txt)).

## Derived Quantities and Interpretation

Two derived values help frame the practical significance of the gap, both computed from the reported figures.

**Average absolute gain across the two tasks.** The mean of the two reported differences is (21.34 + 2.02) / 2 = **11.68 BLEU points** in favor of the Insertion-Deletion Model, computed from the reported per-task differences ([document_1.txt](document_1.txt); [document_2.txt](document_2.txt)).

**Relative improvement.** On the dataset with the larger absolute gain, 70.15 → 91.49 corresponds to an increase of roughly 30.4 percent over the baseline; on the dataset with the smaller gain, 35.55 → 37.57 corresponds to roughly 5.7 percent, computed from the reported figures ([document_1.txt](document_1.txt)).

The asymmetry is notable. A single deletion phase added to an insertion-only backbone yields a very large improvement on one synthetic character-level task and a modest improvement on the other. The paper frames the overall result at the level of direction rather than a single pooled number: the experiments on synthetic translation datasets show that the addition of deletion improves the BLEU score ([document_2.txt](document_2.txt)), and the insertion-deletion framework is presented as a proof of concept applied to two synthetic character-based translation tasks ([document_1.txt](document_1.txt)).

One negative finding is also reported: adversarial deletion training did not improve BLEU scores on these synthetic tasks. However, the adversarial training scheme can still be helpful when the deletion model does not receive a signal during training by sampling from the insertion model alone — that is, when the insertion model does not make any errors ([document_1.txt](document_1.txt)).

The paper also documents how the insertion and deletion models interact at the level of individual decoding steps, with one randomly chosen example of this interaction during a decoding step shown in Table 1 of the manuscript, where insertions are inserted to the left of each token in the target sequence occurring after the [SEP] token ([document_1.txt](document_1.txt)).

## Context: Related Work on Post-Editing and Deletion

The paper positions the deletion phase relative to prior work on text editing and post-editing. Xia et al. (2017) proposed Deliberation Networks, a two-phase decoding framework that likewise acknowledges potential benefits from post-editing output sequences ([document_1.txt](document_1.txt)). The broader citation base includes the Levenshtein Transformer (Gu et al., 2019b), Optimal Completion Distillation (Sabour et al., 2019), the original sequence-to-sequence learning work (Sutskever et al., 2014), and the Transformer architecture itself (Vaswani et al., 2017) ([document_1.txt](document_1.txt)). These references establish that insertion-based and deletion-based generation were active research directions at the time, but they are not the source of the BLEU numbers in question.

## Limitations and Caveats

Four caveats should accompany any use of these figures.

1. **Two tasks, not one aggregate.** The paper reports separate BLEU results for two synthetic translation tasks rather than one overall BLEU difference ([document_2.txt](document_2.txt)). Quoting a single "BLEU improvement" for the model would obscure this.
2. **Labeling discrepancy.** The task-to-score mapping differs between the two available sources, as detailed above ([document_1.txt](document_1.txt); [document_2.txt](document_2.txt)). The per-dataset magnitudes remain stable regardless of which mapping is adopted.
3. **Synthetic, character-based data.** The evaluation is restricted to synthetic character-based translation tasks used as a proof of concept ([document_1.txt](document_1.txt)). Nothing in the source material establishes that the same gains transfer to natural-language benchmarks.
4. **Dataset size imbalance across tasks.** The two tasks differ by two orders of magnitude in training data (1,000 versus 100,000 examples) and by an order of magnitude in held-out evaluation size (100 versus 1,000 examples) ([document_1.txt](document_1.txt)), so the two BLEU gaps are not directly comparable as estimates of the same underlying effect.

## Conclusion

The BLEU score difference between the proposed Insertion-Deletion Transformer and the insertion-only Insertion Model (KERMIT) is task-dependent. The reported gaps are **21.34 BLEU points** on one synthetic translation task and **2.02 BLEU points** on the other, with the latter described by the authors as around 2 BLEU points ([document_2.txt](document_2.txt); [document_1.txt](document_1.txt)). Both differences favor the insertion-deletion model, and the direction of the effect is consistent across the two experiments ([document_2.txt](document_2.txt)). The maximum observed advantage is therefore 21.34 BLEU points, the minimum is 2.02 BLEU points, and the unweighted average across the two reported tasks is 11.68 BLEU points, computed from the reported per-task figures ([document_1.txt](document_1.txt)). The strongest and most defensible summary statement is that adding a deletion phase produced a statistically and practically visible BLEU gain in both reported settings, but of dramatically different magnitude depending on the dataset, and that the primary source supports an average gain in the low double digits rather than a single uniform improvement figure.

## References

- Document_1.txt [Unpublished manuscript excerpt on the Insertion-Deletion Transformer]. (n.d.). ([document_1.txt](document_1.txt))
- Document_2.txt [Third-party research note on the Insertion-Deletion Transformer]. (n.d.). ([document_2.txt](document_2.txt))