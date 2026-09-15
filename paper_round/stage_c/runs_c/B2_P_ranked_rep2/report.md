# BLEU Score Differences Between the Insertion-Deletion Transformer (Proposed Approach) and the Insertion-Only KERMIT Baseline

## 1. Purpose, Evidence Base, and Headline Finding

This report answers a single, narrowly scoped question: **how large is the BLEU score difference between the proposed approach and the insertion-only baseline?** The evidence base consists of two provided documents. Document 1 contains passages, tables, and captions extracted from the paper itself, including the method description, the experimental setup, and the numerical result tables. Document 2 is a "Third-party research note: Insertion-Deletion Transformer" that restates the same comparison figures from the outside and explicitly frames the key question as the "proposed insertion-deletion model versus insertion-only model BLEU difference" ([Document 2, n.d.](document_2.txt)).

The short answer is that **there is no single overall BLEU difference**. The paper "reports separate BLEU results for two synthetic translation tasks rather than one overall BLEU difference," and the per-task comparisons are **21.34 BLEU points** on one task and **2.02 BLEU points** on the other, in both cases in favour of the proposed insertion-deletion model ([Document 2, n.d.](document_2.txt)). The remainder of this report substantiates those figures, documents a labelling conflict between the two sources, and assesses what the numbers do and do not support.

## 2. The Two Systems Being Compared

### 2.1 Proposed approach: the Insertion-Deletion Transformer

The proposed approach is the Insertion-Deletion Transformer, described as "a transformer-based neural architecture and training method for sequence generation" ([Document 2, n.d.](document_2.txt)). Architecturally, it "can be implemented with a simple stack of two Transformer decoders, where the top deletion transformer layer gets its signal from the bottom insertion transformer" ([Document 1, n.d.](document_1.txt)). The pipeline consists of "one insertion phase and one deletion phase, without the need to predict the number of tokens needed to be inserted," which "greatly simplifies the model architecture, training procedure and inference runtime" ([Document 1, n.d.](document_1.txt)).

The stated motivation for adding a deletion phase is error correction: "In a conventional insertion-based model, if the model makes a mistake during generation, this cannot be undone. Introducing the deletion phase makes it possible to undo the mistakes made by the insertion model, since it is trained on the on-policy errors of the insertion phase" ([Document 1, n.d.](document_1.txt)). The framework is additionally claimed to support "tasks like text simplification and style transfer by starting the decoding process from the original source sequence" ([Document 1, n.d.](document_1.txt)).

### 2.2 Insertion-only baseline: the Insertion Model (KERMIT)

The baseline is the Insertion Model (KERMIT). According to the research note, this baseline "extends the Insertion Transformer insertion-only framework to handle insertions," and the paper "extends that insertion-only framework to handle both insertions and deletions, producing the Insertion-Deletion Model for direct comparison" ([Document 2, n.d.](document_2.txt)). In the paper's own words: "We extend the Insertion Transformer Stern et al. 2019, an insertion-only framework to handle both insertions and deletions" ([Document 1, n.d.](document_1.txt)).

The comparison is therefore clean and single-variable in design: both systems are insertion-based Transformer models trained under the same schedule, and the only architectural difference is the presence or absence of the deletion phase.

### 2.3 Evaluation protocol

The evaluation uses two synthetic character-based translation tasks ([Document 1, n.d.](document_1.txt)). The paper describes the framework as "a proof of concept by applying it to two synthetic character-based translation tasks and showing it can significantly increase the BLEU score over the insertion-only framework" ([Document 1, n.d.](document_1.txt)). Two protocol statements appear in the extracted passages:

- For the result pair reported in Table 2: "We generate 1000 of examples for training, and evaluate on 100 held-out examples... We train our models for 200k steps, batch size of 32 and perform no model selection" ([Document 1, n.d.](document_1.txt)).
- For the result pair reported in Table 3: "We generate 100k examples to train on, and evaluate on 1000 held-out examples. We train our models for 200k steps, batch size of 32 and perform no model selection" ([Document 1, n.d.](document_1.txt)).

Both configurations therefore share an identical training schedule (200,000 steps, batch size 32) and explicitly involve **no model selection** ([Document 1, n.d.](document_1.txt)).

## 3. Headline Results: The Two Per-Task BLEU Differences

Table 1 consolidates the reported numbers, the source tables, and the task labels as given by each document.

**Table 1. Reported BLEU scores and differences for the proposed model versus the insertion-only baseline**

| Score pair | KERMIT (insertion-only) | Insertion-Deletion Model | BLEU difference | Paper table | Task label (Document 1) | Task label (Document 2) |
|---|---|---|---|---|---|---|
| Pair A | 70.15 | 91.49 | **+21.34** | Table 2 | Alphabetic Sequence Shifting | Caesar's cipher |
| Pair B | 35.55 | 37.57 | **+2.02** | Table 3 | Caesar's Cipher | Shifted alphabetic sequence |

*Sources: ([Document 1, n.d.](document_1.txt); [Document 2, n.d.](document_2.txt))*

### 3.1 The larger gap: 21.34 BLEU points

For Pair A, the note states that "the reported BLEU scores are 91.49 for the Insertion-Deletion Model and 70.15 for the Insertion Model (KERMIT). The difference is 21.34 BLEU points in favor of the Insertion-Deletion Model," and that "the Insertion-Deletion Model improves BLEU score on this task" ([Document 2, n.d.](document_2.txt)). The paper reports the identical pair under the heading "Alphabetic Sequence Shifting BLEU" with the caption "Table 2: BLEU scores for the sequence shifting task" ([Document 1, n.d.](document_1.txt)), and states plainly: "We see our Insertion-Deletion Transformer model outperforms the Insertion Transformer significantly on this task" ([Document 1, n.d.](document_1.txt)).

### 3.2 The smaller gap: 2.02 BLEU points

For Pair B, the note states that the scores are "37.57 for the Insertion-Deletion Model and 35.55 for the Insertion Model (KERMIT)," that "the difference is 2.02 BLEU points," and that "the paper describes this as around 2 BLEU points" ([Document 2, n.d.](document_2.txt)). Consistent with this, the paper's own text says "the deletion model again increases the BLEU score over just the insertion model, by around 2 BLEU points," immediately above a table headed "Caesar's Cipher BLEU" with values 35.55 and 37.57 and the caption "Table 3: BLEU scores for the Caesar's cipher task" ([Document 1, n.d.](document_1.txt)).

### 3.3 No aggregate difference is reported

To be explicit: the sources do not report a single averaged or pooled BLEU difference. The research note states that "the paper reports separate BLEU results for two synthetic translation tasks rather than one overall BLEU difference," adding that "the experiments on synthetic translation datasets show that the addition of deletion improves BLEU score" ([Document 2, n.d.](document_2.txt)). This is echoed in the paper's conclusion, which reports that "the deletion model can significantly increase the BLEU score on simple tasks by iteratively refining the output sequence via sequences of insertion-deletions" ([Document 1, n.d.](document_1.txt)).

## 4. Conflict Between the Sources on Task Attribution

The two documents agree completely on the **numbers** and on the **table numbering**, but they disagree on which **task** produced which pair. Table 2, below, isolates the conflict.

**Table 2. Cross-source comparison of task labels for identically numbered results**

| Table | Scores reported | Label in Document 1 (paper text/captions) | Label in Document 2 (third-party note) |
|---|---|---|---|
| Table 2 | 70.15 → 91.49 | "Alphabetic Sequence Shifting BLEU" / "BLEU scores for the sequence shifting task" ([Document 1, n.d.](document_1.txt)) | "Caesar's cipher task" ([Document 2, n.d.](document_2.txt)) |
| Table 3 | 35.55 → 37.57 | "Caesar's Cipher BLEU" / "BLEU scores for the Caesar's cipher task" ([Document 1, n.d.](document_1.txt)) | "shifted alphabetic sequence task" ([Document 2, n.d.](document_2.txt)) |

Document 1 places the section heading "3.2 Learning Caesar's Cipher" immediately after the Table 2 block, and places "4 Conclusion" immediately after the Table 3 block, which indicates that Table 2 closes the section on shifted alphabetic sequences and Table 3 closes the Caesar's cipher section ([Document 1, n.d.](document_1.txt)). Document 1 also contains a decoding example for the sequence-shifting setting showing an output sequence of `[CLS] e f g h i j k l m [SEP] o p q r u v w [SEP]` with a predicted deletion, alongside the caption "Table 1: Example decoding iteration during inference" ([Document 1, n.d.](document_1.txt)).

**Assessment.** On balance, the task labels given in Document 1 are more credible for three reasons: (i) they are attached to the table captions and section headings of the primary text, (ii) the paper's own sentence describing the gain as "around 2 BLEU points" sits directly above the table it describes ([Document 1, n.d.](document_1.txt)), and (iii) Document 2 is explicitly a "third-party research note" rather than the source text ([Document 2, n.d.](document_2.txt)). My conclusion is therefore that **21.34 BLEU points belongs to the shifted alphabetic sequence task (Table 2)** and **2.02 BLEU points belongs to the Caesar's cipher task (Table 3)**. Critically, however, this disagreement does not change the answer to the numerical question: regardless of which task label is attached, the two reported differences are 21.34 and 2.02 BLEU points.

## 5. Analytical Context: What the Magnitudes Mean

### 5.1 Relative gain and error reduction

The following quantities are my own calculations from the cited figures and are offered as interpretive context rather than as reported results ([Document 1, n.d.](document_1.txt); [Document 2, n.d.](document_2.txt)):

**Table 3. Derived measures of the two reported differences**

| Measure | Pair A (70.15 → 91.49) | Pair B (35.55 → 37.57) |
|---|---|---|
| Absolute BLEU gain | +21.34 | +2.02 |
| Relative gain over baseline | +30.4% | +5.7% |
| BLEU "deficit" before (100 − baseline) | 29.85 | 64.45 |
| BLEU "deficit" after (100 − proposed) | 8.51 | 62.43 |
| Proportional deficit reduction | ≈71.5% | ≈3.1% |

Two observations follow. First, the two effects differ by more than an order of magnitude in absolute terms (21.34 ÷ 2.02 ≈ 10.6). Second, expressed as a reduction in the residual non-overlap implied by BLEU, Pair A is a very large effect while Pair B is a marginal one.

### 5.2 On averaging the two figures

A naive unweighted mean of the two differences is (21.34 + 2.02) ÷ 2 = **11.68 BLEU points**. This number is *not* reported by the paper and should not be presented as the study's result, because the two tasks are different, the evaluation sets differ, and the note explicitly states that separate per-task results are given rather than one overall difference ([Document 2, n.d.](document_2.txt)). It is included here only to show what a reader would obtain by aggregating the two figures without justification, and to warn against doing so.

### 5.3 Dataset-size asymmetry

The extracted passages associate the 21.34-point result with a relatively small setup of "1000 of examples for training" and "100 held-out examples," and the 2.02-point result with a much larger setup of "100k examples to train on" and "1000 held-out examples" ([Document 1, n.d.](document_1.txt)). Both used 200k training steps, batch size 32, and no model selection ([Document 1, n.d.](document_1.txt)). This asymmetry is worth noting because it means the effect sizes are not directly comparable across tasks in any simple "more data, more gain" sense; the modest gain occurs in the higher-resource configuration and the large gain in the lower-resource configuration.

## 6. Reliability, Limitations, and Cautions

Several features of the evidence constrain how strongly the differences should be stated.

**No reported variance or significance testing.** The protocol explicitly states that the models were trained for 200k steps and that "no model selection" was performed ([Document 1, n.d.](document_1.txt)). No confidence intervals, standard deviations, or significance tests are reported in the provided material. The 21.34-point gap is large enough that it is unlikely to be explained by ordinary run-to-run noise, but the 2.02-point gap is not strongly established by a single point estimate.

**Small evaluation samples.** One comparison is evaluated on "100 held-out examples," the other on "1000 held-out examples" ([Document 1, n.d.](document_1.txt)). Small held-out sets make BLEU estimates volatile, and this matters most for the smaller of the two differences.

**Approximate reporting.** The paper itself characterizes the smaller difference as "around 2 BLEU points" ([Document 1, n.d.](document_1.txt)), and the note confirms that this is the paper's own description ([Document 2, n.d.](document_2.txt)). The approximation signals that the authors did not treat the second decimal place as meaningful.

**Narrow task scope.** The findings come from "two synthetic character-based translation tasks," and the authors frame the work as "a proof of concept" ([Document 1, n.d.](document_1.txt)). The results therefore support claims about these synthetic tasks, not about general-purpose machine translation.

**A countervailing negative result.** The paper reports that "adversarial deletion training did not improve BLEU scores on these synthetic tasks," although it adds that the adversarial scheme "can still be helpful when the deletion model does not receive a signal during training by sampling from the insertion model alone" ([Document 1, n.d.](document_1.txt)). This indicates that the gains come from the deletion phase as trained, not from every training variant attempted.

**Source disagreement.** As documented in Section 4, the two sources disagree on task labels for the same table numbers ([Document 1, n.d.](document_1.txt); [Document 2, n.d.](document_2.txt)). The numeric pairs and the "favoring the insertion-deletion model" direction are consistent across both sources; the attribution of those pairs to named tasks is not.

## 7. Direct Answer to the Query

**The BLEU score difference between the proposed Insertion-Deletion Transformer and the insertion-only baseline (Insertion Model, KERMIT) is not a single figure. It is reported per task: a difference of 21.34 BLEU points on one synthetic task (91.49 versus 70.15) and a difference of 2.02 BLEU points on the other (37.57 versus 35.55), with both differences favoring the proposed insertion-deletion model** ([Document 1, n.d.](document_1.txt); [Document 2, n.d.](document_2.txt)). The 21.34-point difference is associated with Table 2, which Document 1 labels as the "Alphabetic Sequence Shifting" task, and the 2.02-point difference is associated with Table 3, which Document 1 labels as the "Caesar's Cipher" task, described by the authors as "around 2 BLEU points" ([Document 1, n.d.](document_1.txt)). Document 2 assigns the two task labels in the reverse order while reporting the same table numbers and the same score pairs ([Document 2, n.d.](document_2.txt)).

My assessment, based on the relative reliability of the sources, is that the defensible headline is **21.34 BLEU points on the sequence-shifting task and 2.02 BLEU points on the Caesar's cipher task**, and that the primary source's table captions and section headings should be preferred over the third-party note's labels. Substantively, the 21.34-point gap represents a large, order-of-magnitude-scale improvement that is unlikely to be an artifact of noise, whereas the 2.02-point gap should be treated as provisional, given the absence of reported variance and the explicit "around 2 BLEU points" phrasing ([Document 1, n.d.](document_1.txt); [Document 2, n.d.](document_2.txt)). Any statement that the proposed model improves BLEU by a single aggregate amount would misrepresent the paper, which reports separate results for separate tasks rather than one overall difference ([Document 2, n.d.](document_2.txt)).

## References

Document 1. (n.d.). *Paper text and tables for the Insertion-Deletion Transformer* [Unpublished manuscript]. document_1.txt.

Document 2. (n.d.). *Third-party research note: Insertion-Deletion Transformer* [Research note]. document_2.txt.