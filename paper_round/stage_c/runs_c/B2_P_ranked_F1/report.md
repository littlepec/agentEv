# BLEU Score Differences Between the Proposed Insertion-Deletion Transformer and the Insertion-Only (KERMIT) Baseline

## 1. Direct Answer to the Query

The question asks how large the BLEU score difference is between the proposed approach and the insertion-only method. Based strictly on the supplied evidence, the answer is that the paper does **not** report a single aggregate BLEU difference. It evaluates the proposed model on two synthetic character-based translation tasks and reports a separate BLEU comparison for each, so the difference is task-specific rather than global ([document_2.txt](document_2.txt)). The two reported differences are:

- **21.34 BLEU points** in the first comparison (91.49 for the Insertion-Deletion model versus 70.15 for the Insertion Model / KERMIT), and
- **2.02 BLEU points** in the second comparison (37.57 versus 35.55), which the paper itself describes as "around 2 BLEU points" ([document_1.txt](document_1.txt); [document_2.txt](document_2.txt)).

Both sources agree on these four underlying BLEU values and on the two arithmetic differences; they disagree only about which named task is attached to which pair of numbers ([document_1.txt](document_1.txt); [document_2.txt](document_2.txt)). The direction of the effect is nevertheless consistent across both tasks: "the experiments on synthetic translation datasets show that the addition of deletion improves BLEU score" ([document_2.txt](document_2.txt)).

Table 1. *Reported BLEU scores and differences for the proposed model versus the insertion-only baseline*

| Comparison (as reported in the paper) | Insertion Model (KERMIT) — baseline | Insertion-Deletion Model — proposed | Absolute difference | Relative gain (computed from reported values) |
|---|---|---|---|---|
| Comparison reported alongside Table 2 | 70.15 | 91.49 | **+21.34** | +30.4% |
| Comparison reported alongside Table 3 | 35.55 | 37.57 | **+2.02** | +5.7% |

*Note.* BLEU values as reported ([document_1.txt](document_1.txt); [document_2.txt](document_2.txt)). The relative gains are arithmetic derivations from the reported values; the paper reports absolute BLEU point differences, not percentages.

If one were to average the two per-task differences, the arithmetic mean would be 11.68 BLEU points; however, the sources are explicit that "the paper reports separate BLEU results for two synthetic translation tasks rather than one overall BLEU difference" ([document_2.txt](document_2.txt)). That mean is therefore a derived illustration only and should not be treated as a result reported by the authors.

## 2. The Two Systems Being Compared

### 2.1 Proposed approach: the Insertion-Deletion Transformer

The proposed approach is the Insertion-Deletion Transformer, described as "a transformer-based neural architecture and training method for sequence generation" that is implemented as "a simple stack of two Transformer decoders, where the top deletion transformer layer gets its signal from the bottom insertion transformer" ([document_1.txt](document_1.txt); [document_2.txt](document_2.txt)). The design "extend[s] the Insertion Transformer Stern et al. 2019, an insertion-only framework to handle both insertions and deletions" ([document_1.txt](document_1.txt)).

The stated motivation for adding a deletion phase is error correction. In a conventional insertion-based model, "if the model makes a mistake during generation, this cannot be undone," whereas the deletion phase "makes it possible to undo the mistakes made by the insertion model, since it is trained on the on-policy errors of the insertion phase" ([document_1.txt](document_1.txt)). The framework is also claimed to support flexible sequence generation, parallel token generation, and text editing, and to enable tasks such as text simplification and style transfer by starting decoding from the original source sequence ([document_1.txt](document_1.txt)).

### 2.2 Baseline: the Insertion Model (KERMIT)

The insertion-only baseline is the Insertion Model (KERMIT), which the paper extends to handle both insertions and deletions in order to produce the Insertion-Deletion Model for direct comparison ([document_2.txt](document_2.txt)). KERMIT derives from the insertions-only framework of Chan et al. 2019, and the Insertion Transformer lineage traces to Stern et al. 2019 ([document_1.txt](document_1.txt)). The paper also positions its contribution against another post-editing-style approach, Deliberation Networks (Xia et al. 2017), "a two-phase decoding framework" that likewise "acknowledges the potential benefits from post-editing output sequences" ([document_1.txt](document_1.txt)).

## 3. The Reported Per-Task BLEU Results

### 3.1 The 21.34-point comparison

In the experiment that reports the larger effect, the Insertion Model (KERMIT) scores 70.15 BLEU and the Insertion-Deletion Model scores 91.49 BLEU, a difference of 21.34 BLEU points in favor of the proposed model ([document_1.txt](document_1.txt); [document_2.txt](document_2.txt)). In the section containing this comparison, the paper states that "our Insertion-Deletion Transformer model outperforms the Insertion Transformer significantly on this task," and notes that the models were trained for 200k steps with a batch size of 32 and no model selection ([document_1.txt](document_1.txt)).

### 3.2 The 2.02-point comparison

In the experiment that reports the smaller effect, the Insertion Model (KERMIT) scores 35.55 BLEU and the Insertion-Deletion Model scores 37.57 BLEU, a difference of 2.02 BLEU points ([document_1.txt](document_1.txt); [document_2.txt](document_2.txt)). Here the paper states that "the deletion model again increases the BLEU score over just the insertion model, by around 2 BLEU points," and the same training configuration is used (200k steps, batch size 32, no model selection) ([document_1.txt](document_1.txt)).

## 4. Resolving the Discrepancy in Task Labels Between the Two Sources

The two supplied sources attach different task names to the same numbers, as summarized below.

Table 2. *Competing task attributions for the same BLEU values*

| Source | Table 2 attribution | Table 3 attribution |
|---|---|---|
| [document_1.txt](document_1.txt) (primary paper excerpts) | "Alphabetic Sequence Shifting BLEU" — 70.15 → 91.49 (Δ = 21.34); captioned "Table 2: BLEU scores for the sequence shifting task" | "Caesar's Cipher BLEU" — 35.55 → 37.57 (Δ = 2.02); captioned "Table 3: BLEU scores for the Caesar's cipher task" |
| [document_2.txt](document_2.txt) (third-party note) | Caesar's cipher task — 70.15 → 91.49 (Δ = 21.34) | Shifted alphabetic sequence task — 35.55 → 37.57 (Δ = 2.02) |

On balance, I regard the attribution in [document_1.txt](document_1.txt) as the more probable one, for three reasons grounded in that source itself. First, the table captions are explicit and internally consistent: "Table 2: BLEU scores for the sequence shifting task" and "Table 3: BLEU scores for the Caesar's cipher task" ([document_1.txt](document_1.txt)). Second, the section ordering corroborates the captions: the heading "3.2 Learning Caesar's Cipher" immediately follows the Table 2 material, and the Table 3 Caesar's cipher material appears immediately before "4 Conclusion," which is the expected position for the paper's second experiment ([document_1.txt](document_1.txt)). Third, the worked examples align with the captions: the decoding-iteration example shown in Table 1 consists of ordered alphabetical tokens, consistent with a sequence-shifting task, while the section reporting the smaller 2.02-point gain is accompanied by the "h k b e t" → "g j a d s" example, which is a shift-by-one transformation of an arbitrary letter string, i.e., a Caesar-type cipher ([document_1.txt](document_1.txt)).

That said, the discrepancy cannot be dismissed entirely: [document_2.txt](document_2.txt) is a purpose-written research note that explicitly poses the comparison question and asserts the opposite assignment ([document_2.txt](document_2.txt)). Because the two documents are the only evidence available, a reader should treat the pairing of task names to scores as unsettled and rely on the more robust claim that the paper reports two per-task improvements of 21.34 and 2.02 BLEU points, both favoring the Insertion-Deletion model ([document_1.txt](document_1.txt); [document_2.txt](document_2.txt)).

## 5. Interpretation of a 21.34-Point Versus a 2.02-Point Gain

The two effects differ by an order of magnitude, and the paper's own language reflects this: the larger result is characterized as the proposed model "outperform[ing] the Insertion Transformer significantly," while the smaller result is described as an increase "by around 2 BLEU points" ([document_1.txt](document_1.txt)). Two observations follow.

First, BLEU gains are not directly comparable across tasks with different difficulty and different data regimes. The two experiments in the supplied excerpts use different amounts of supervision: one section reports 1,000 training examples with 100 held-out examples, while the other reports 100,000 training examples with 1,000 held-out examples ([document_1.txt](document_1.txt)). Because the task labels themselves are disputed across sources, the mapping between data scale and task name cannot be stated with certainty from the supplied material; what is clear is that the two headline numbers come from non-identical experimental setups, which limits how meaningfully they can be averaged or ranked.

Second, the mechanism offered for the improvement is correction of insertion errors through deletion, since the deletion model "is trained on the on-policy errors of the insertion phase" ([document_1.txt](document_1.txt)). The paper's conclusion states that "the deletion model can significantly increase the BLEU score on simple tasks by iteratively refining the output sequence via sequences of insertion-deletions" ([document_1.txt](document_1.txt)). This mechanism implies that the size of the gain should depend on how much residual error the insertion stage leaves behind, which is a plausible qualitative explanation for why one task benefits by roughly 21 BLEU points and the other by roughly 2 ([document_1.txt](document_1.txt)).

## 6. Reliability, Caveats, and Limitations

Several caveats temper the headline numbers. The evaluation is explicitly a "proof of concept" on "two synthetic character-based translation tasks" rather than on natural language benchmarks ([document_1.txt](document_1.txt)). No confidence intervals, variance estimates, or significance tests are reported in the supplied material, so although the paper uses the adverb "significantly" in prose, the supplied evidence does not document statistical significance testing ([document_1.txt](document_1.txt)). The training regime also includes a negative finding: "adversarial deletion training did not improve BLEU scores on these synthetic tasks," although that scheme "can still be helpful when the deletion model does not receive a signal during training by sampling from the insertion model alone (i.e., when the insertion-model does not make any errors)" ([document_1.txt](document_1.txt)).

With respect to source quality, [document_1.txt](document_1.txt) is the higher-value source because it reproduces the paper's own sections, table captions, and worked examples, whereas [document_2.txt](document_2.txt) is a third-party summary note ([document_1.txt](document_1.txt); [document_2.txt](document_2.txt)). Where the two conflict on task labeling, the primary-source captions and section structure deserve greater weight, while the numerical values themselves are corroborated by both sources and can therefore be reported with high confidence ([document_1.txt](document_1.txt); [document_2.txt](document_2.txt)).

## 7. Conclusion

The reported BLEU advantage of the proposed Insertion-Deletion Transformer over the insertion-only Insertion Model (KERMIT) is **21.34 BLEU points on one synthetic task (91.49 versus 70.15)** and **2.02 BLEU points on the other (37.57 versus 35.55, described as "around 2 BLEU points")** ([document_1.txt](document_1.txt); [document_2.txt](document_2.txt)). There is no single pooled BLEU difference in the supplied material, and any average of the two would be a derived figure rather than a reported result ([document_2.txt](document_2.txt)). The substantive conclusion — that adding a deletion phase improves BLEU over an insertion-only baseline on both tasks — is supported by both sources, and the evidence from the primary excerpts indicates that the larger gain belongs to the sequence-shifting task (Table 2) and the smaller gain to the Caesar's cipher task (Table 3), although the third-party note assigns the task names in the opposite order ([document_1.txt](document_1.txt); [document_2.txt](document_2.txt)). Readers should therefore cite the differences as per-task figures of 21.34 and 2.02 BLEU points rather than as a single aggregate improvement.

## References

document_1.txt. (n.d.). *Insertion-Deletion Transformer: Paper excerpts, tables, and experimental sections* [Unpublished manuscript excerpts].

document_2.txt. (n.d.). *Third-party research note: Insertion-Deletion Transformer* [Analytical summary].