# Quantifying the BLEU Score Difference Between the Proposed Insertion-Deletion Transformer and the Insertion-Only Baseline

## Executive Summary

The Insertion-Deletion Transformer outperforms the insertion-only Insertion Model (KERMIT) baseline on every task for which BLEU scores are reported in the available material. However, the difference is **not a single aggregate figure**. The source paper reports **separate, per-task BLEU comparisons** on two synthetic character-level translation tasks ([document_2.txt](#ref2)). The two headline deltas are:

- **+21.34 BLEU points** on the alphabetic sequence shifting task (91.49 vs. 70.15) ([document_1.txt](#ref1); [document_2.txt](#ref2))
- **+2.02 BLEU points** on Caesar's cipher (37.57 vs. 35.55), described in the paper itself as "around 2 BLEU points" ([document_1.txt](#ref1); [document_2.txt](#ref2))

The arithmetic mean of the two reported deltas is **11.68 BLEU points**, but this figure is a derived statistic and is not reported by the authors. It should be treated as descriptive only, because the two tasks differ substantially in difficulty, data regime, and absolute score range.

---

## 1. Framing the Query

The question posed — "How much is the BLEU score difference between the proposed approach and the insertion-only method?" — presupposes a singular answer. The retrieved evidence does not support a singular answer. The third-party research note explicitly states that "the paper reports separate BLEU results for two synthetic translation tasks rather than one overall BLEU difference," and that "the comparisons are per task" ([document_2.txt](#ref2)). Any accurate response must therefore be decomposed by task, which is the approach taken throughout this report.

## 2. The Two Systems Being Compared

### 2.1 Proposed approach: Insertion-Deletion Transformer

The proposed method is the **Insertion-Deletion Transformer**, described as "a novel transformer-based neural architecture and training method for sequence generation" ([document_1.txt](#ref1)). The model "consists of two phases that are executed iteratively, 1) an insertion phase and 2) a deletion phase" ([document_1.txt](#ref1)). The insertion phase parameterizes a distribution over insertions on the current output hypothesis, while the deletion phase parameterizes a distribution over deletions over that same hypothesis ([document_1.txt](#ref1)).

Architecturally, the model "can be implemented with a simple stack of two Transformer decoders, where the top deletion transformer layer gets its signal from the bottom insertion transformer" ([document_1.txt](#ref1)). A crucial training design choice is that "the deletion model obtains its signal directly on-policy from the insertion model output" ([document_1.txt](#ref1)).

### 2.2 Baseline: Insertion Model (KERMIT)

The insertion-only baseline is the **Insertion Model (KERMIT)** ([document_2.txt](#ref2)). The research note characterizes it as extending "the Insertion Transformer insertion-only framework to handle insertions," and states that "the paper extends that insertion-only framework to handle both insertions and deletions, producing the Insertion-Deletion Model for direct comparison" ([document_2.txt](#ref2)). This makes the comparison a controlled, like-for-like evaluation in which the deletion phase is the primary manipulated variable.

The method section confirms this lineage directly: "We extend the Insertion Transformer (Stern et al., 2019), an insertion-only framework to handle both insertions and deletions" ([document_1.txt](#ref1)).

## 3. The Headline Answer: Per-Task BLEU Differences

### 3.1 Alphabetic Sequence Shifting: +21.34 BLEU Points

On the alphabetic sequence shifting task, "the reported BLEU scores are 91.49 for the Insertion-Deletion Model and 70.15 for the Insertion Model (KERMIT). The difference is 21.34 BLEU points in favor of the Insertion-Deletion Model" ([document_2.txt](#ref2)). These results are presented in Table 2 of the source paper ([document_1.txt](#ref1)).

The paper's own language is notably strong for this task: "We see our Insertion-Deletion Transformer model outperforms the Insertion Transformer significantly on this task" ([document_1.txt](#ref1)).

### 3.2 Caesar's Cipher: +2.02 BLEU Points

On Caesar's cipher, "the reported BLEU scores are 37.57 for the Insertion-Deletion Model and 35.55 for the Insertion Model (KERMIT). The difference is 2.02 BLEU points" ([document_2.txt](#ref2)). The paper describes this as "around 2 BLEU points," and the results are presented in Table 3 ([document_1.txt](#ref1)). The source text states plainly: "The table below shows that the deletion model again increases the BLEU score over just the insertion model, by around 2 BLEU points" ([document_1.txt](#ref1)).

### 3.3 Consolidated Comparison

**Table 1. Reported BLEU scores by task, model, and delta**

| Task | Insertion Model (KERMIT) | Insertion-Deletion Model | Delta (BLEU points) | Source table |
|---|---|---|---|---|
| Alphabetic sequence shifting | 70.15 | 91.49 | **+21.34** | Table 2 ([document_1.txt](#ref1)) |
| Caesar's cipher | 35.55 | 37.57 | **+2.02** | Table 3 ([document_1.txt](#ref1)) |
| Mean of the two deltas (derived, not reported) | — | — | 11.68 | Author's calculation |

## 4. Relative Magnitude of the Differences

Absolute BLEU-point deltas can obscure how large a gain actually is at different points on the scale. Expressing the same data as relative improvement sharpens the picture.

**Table 2. Absolute versus relative improvement**

| Task | Baseline BLEU | Proposed BLEU | Absolute delta | Relative improvement | Residual-error reduction* |
|---|---|---|---|---|---|
| Alphabetic sequence shifting | 70.15 | 91.49 | +21.34 | +30.42% | ≈71.5% |
| Caesar's cipher | 35.55 | 37.57 | +2.02 | +5.68% | ≈3.1% |

*Residual-error reduction is computed by the author as the reduction in the gap to a nominal ceiling of 100 BLEU points: (100 − proposed) vs. (100 − baseline). This is a derived interpretive metric, not one reported in the sources ([document_1.txt](#ref1); [document_2.txt](#ref2)).

Two observations follow. First, the alphabetic sequence shifting gain is large in both absolute and relative terms, and the resulting 91.49 score places the model in a very strong position on that task. Second, the Caesar's cipher gain — although statistically meaningful relative to its own baseline — leaves considerable headroom, with the proposed model still scoring 37.57 and both systems far from saturation. This divergence in magnitude is precisely why a single aggregate delta would be misleading.

## 5. Why There Is No Single Aggregate BLEU Difference

Three considerations argue against collapsing the results into one number:

1. **The sources explicitly reject aggregation.** The research note states that "the paper reports separate BLEU results for two synthetic translation tasks rather than one overall BLEU difference" ([document_2.txt](#ref2)).
2. **The evidence base is small.** The evaluation rests on two tasks only. The paper presents the framework "as a proof of concept by applying it to two synthetic character-based translation tasks" ([document_1.txt](#ref1)). Averaging two data points yields an unstable estimate with no dispersion information.
3. **BLEU is not additive across heterogeneous tasks.** A 21.34-point delta on a near-saturated task and a 2.02-point delta on a low-scoring task are not commensurate, because BLEU operates on an n-gram overlap scale whose sensitivity varies with absolute performance.

## 6. Experimental Conditions Behind the Numbers

The reported deltas are attached to specific, transparently documented training configurations.

**Table 3. Experimental setup by task**

| Element | Alphabetic sequence shifting | Caesar's cipher |
|---|---|---|
| Training examples | 1,000 | 100,000 |
| Held-out evaluation examples | 100 | 1,000 |
| Training steps | 200,000 | 200,000 |
| Batch size | 32 | 32 |
| Model selection | None | None |
| Source | [document_1.txt](#ref1) | [document_1.txt](#ref1) |

The absence of model selection in both settings is noteworthy: reported scores are therefore not inflated by post-hoc checkpoint selection against a validation set ([document_1.txt](#ref1)). This strengthens the reliability of the comparison, but it also means the single-run figures carry unquantified run-to-run variance.

Additionally, the paper reports a negative finding of relevance to the comparison: "We found that adversarial deletion training did not improve BLEU scores on these synthetic tasks" ([document_1.txt](#ref1)). However, "the adversarial training scheme can still be helpful when the deletion model does not receive a signal during training by sampling from the insertion model alone (i.e., when the insertion-model does not make any errors)" ([document_1.txt](#ref1)). This nuance indicates that the observed deltas reflect the on-policy deletion mechanism rather than adversarial variants.

## 7. Mechanistic Explanation for the Gains

The reported BLEU improvements have a coherent mechanistic rationale. The paper argues that "in a conventional insertion-based model, if the model makes a mistake during generation, this cannot be undone" ([document_1.txt](#ref1)). By contrast, "introducing the deletion phase makes it possible to undo the mistakes made by the insertion model, since it is trained on the on-policy errors of the insertion phase" ([document_1.txt](#ref1)).

The practical consequence is described in the conclusion: "the deletion model can significantly increase the BLEU score on simple tasks by iteratively refining the output sequence via sequences of insertion-deletions" ([document_1.txt](#ref1)). This suggests the gain is not a marginal tuning artifact but a structural capability — error correction — that the insertion-only baseline lacks by construction.

The framework also carries efficiency claims relevant to the comparison: it executes "one insertion phase and one deletion phase, without the need to predict the number of tokens needed to be inserted," which "greatly simplifies the model architecture, training procedure and inference runtime" ([document_1.txt](#ref1)). Implementation is described as a "simple stack of two Transformer decoders" ([document_1.txt](#ref1)).

Broader applicability is also claimed: the deletion extension "enables the framework to efficiently handle tasks like text simplification and style transfer by starting the decoding process from the original source sequence" ([document_1.txt](#ref1)). The paper connects this to antecedent work on post-editing, including Deliberation Networks (Xia et al., 2017), "which also acknowledges the potential benefits from post-editing output sequences and proposes a two-phase decoding framework" ([document_1.txt](#ref1)).

## 8. Scope, Limitations, and Threats to Validity

An objective reading requires flagging several caveats:

- **Synthetic tasks only.** Both evaluations are on synthetic character-based translation: alphabetic sequence shifting and Caesar's cipher ([document_1.txt](#ref1)). The source text uses the phrase "on simple tasks" ([document_1.txt](#ref1)), and the third-party note confirms the scope is "synthetic translation datasets" ([document_2.txt](#ref2)). Generalization to natural-language benchmarks is untested in the available material.
- **Two tasks provide no basis for an average.** Any mean delta is arithmetically computable but statistically hollow.
- **Rounding and reporting.** Caesar's cipher is described as "around 2 BLEU points" ([document_2.txt](#ref2)), whereas the table values support a precise 2.02 ([document_1.txt](#ref1)). The precise figure should be preferred for reporting.
- **No significance testing reported.** Word-level significance testing or confidence intervals for the BLEU deltas are absent from the provided material, so the 2.02-point gain in particular should be described as a reported improvement rather than an established significant effect.
- **Source duplication.** The retrieved corpus contains overlapping excerpts from the same two documents; the concordance of the numbers across both ([document_1.txt](#ref1); [document_2.txt](#ref2)) increases confidence that the figures are transcribed consistently.

## 9. Conclusion

The BLEU score difference between the proposed Insertion-Deletion Transformer and the insertion-only Insertion Model (KERMIT) is **task-specific**. It is **21.34 BLEU points** on alphabetic sequence shifting (91.49 vs. 70.15) and **2.02 BLEU points** on Caesar's cipher (37.57 vs. 35.55) ([document_1.txt](#ref1); [document_2.txt](#ref2)).

My concrete assessment, based on the evidence provided, is as follows: the correct headline figure for this comparison is the **pair of deltas**, not a mean. The alphabetic sequence shifting result is the stronger and more persuasive evidence, because a +21.34-point gain (a roughly 30% relative improvement) is difficult to attribute to noise and pushes performance to 91.49, a level at which meaningful headroom is limited. The Caesar's cipher gain of +2.02 points is real in direction and consistent across both sources ([document_1.txt](#ref1); [document_2.txt](#ref2)), but at approximately 5.7% relative improvement on a low-scoring task, it is modest and would benefit from significance testing before being characterized as substantial. Reporting an 11.68-point average across the two would therefore overstate the Caesar's cipher effect and understate the sequence shifting effect. The defensible one-sentence answer is this: **the addition of deletion improved BLEU by 21.34 points on alphabetic sequence shifting and by 2.02 points on Caesar's cipher, with no single aggregate figure reported or warranted.**

---

## References

<a id="ref1"></a>Document 1. (n.d.). *Insertion-Deletion Transformer* [Manuscript excerpt, document_1.txt]. Google Brain.

<a id="ref2"></a>Document 2. (n.d.). *Third-party research note: Insertion-Deletion Transformer* [Analytical note, document_2.txt].