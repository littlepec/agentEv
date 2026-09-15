# Incremental Gains from Gating–Tensor Hybridization: Quantifying the Reported Improvements of LSTMRNTN and GRURNTN over Gated RNN Baselines

## Introduction

The paper "Gated Recurrent Neural Tensor Network" introduces two recurrent architectures that fuse the gating mechanism of Long Short-Term Memory (LSTM) and Gated Recurrent Unit (GRU) networks with a tensor-product (bilinear) interaction between the current input and the previous hidden state ([Tjandra et al., 2017](https://arxiv.org/abs/1706.02222)). The two proposed models — Long Short-Term Memory Recurrent Neural Tensor Network (LSTMRNTN) and Gated Recurrent Unit Recurrent Neural Tensor Network (GRURNTN) — are evaluated on word-level and character-level language modeling using the PennTreeBank (PTB) corpus, and are compared against matched-parameter baseline gated RNNs (LSTMRNN and GRURNN) as well as against several previously published results ([Tjandra et al., 2017](https://arxiv.org/abs/1706.02222)). This report quantifies the reported improvements, separates the baseline-relative gains from the broader literature comparison, and evaluates how large and how reliable those gains are.

## What the Proposed Models Change

The paper's motivating claim is that gating alone lets an RNN remember and forget information across time, but does not give the network a more expressive way to model the relationship between the current input and the previous hidden representation; conversely, tensor products give more expressive interactions but, without gating, suffer from vanishing or exploding gradients ([Tjandra et al., 2017](https://arxiv.org/abs/1706.02222)). By using a tensor product, the authors argue, the model increases expressiveness through second-degree polynomial interactions, compared with the first-degree polynomial interactions produced by the standard dot-product-plus-addition formulation ([Tjandra et al., 2017](https://arxiv.org/abs/1706.02222)). In GRURNTN the tensor product is applied between the current input and the reset-gated previous hidden state inside the candidate hidden-layer equation, while in LSTMRNTN it is applied between the current input and the previous hidden state inside the candidate cell equation ([Tjandra et al., 2017](https://arxiv.org/abs/1706.02222)). The paper also adopts an asymmetric bilinear form to keep the parameter count down relative to the original neural tensor network formulation ([Tjandra et al., 2017](https://arxiv.org/abs/1706.02222)).

## Experimental Setup and Fair-Comparison Controls

For the word-level task, the proposed models used 256 hidden units, whereas baselines used 860 (GRURNN) and 740 (LSTMRNN); all models used 128-dimensional word embeddings, and dropout probabilities of 0.5 for the proposed models versus 0.6 for the baselines ([Tjandra et al., 2017](https://arxiv.org/abs/1706.02222)). For the character-level task, the proposed models used 256 hidden units, the GRURNN baseline used 820, and the LSTM baseline used 600, with 32-dimensional character embeddings and dropout of 0.25 ([Tjandra et al., 2017](https://arxiv.org/abs/1706.02222)). Parameter counts were about 12 million for GRURNN/GRURNTN and about 13 million for LSTMRNN/LSTMRNTN on the word-level task, and about 2.2 million and 2.6 million respectively on the character-level task ([Tjandra et al., 2017](https://arxiv.org/abs/1706.02222)). The paper explicitly states that baselines were constrained to have a similar number of parameters to the corresponding tensor models "for a fair comparison" ([Tjandra et al., 2017](https://arxiv.org/abs/1706.02222)). This control matters for interpretation: because the baselines were parameter-matched, the reported gains are more plausibly attributable to the tensor-product inductive bias than to a simple increase in model capacity.

All models used AdaGrad with a mini-batch size of 15 sentences, a learning-rate decay factor of 0.5 when development cost increased, gradient rescaling when the norm exceeded 5, and orthogonal weight initialization ([Tjandra et al., 2017](https://arxiv.org/abs/1706.02222)). The PTB corpus contained 930,000 training words, 74,000 validation words, and 82,000 test words, with a 10,000-word vocabulary ([Tjandra et al., 2017](https://arxiv.org/abs/1706.02222)).

## Reported Improvements on Character-Level Language Modeling

### Baseline-relative gains

On the character-level task, performance is reported as bits-per-character (BPC), where lower is better ([Tjandra et al., 2017](https://arxiv.org/abs/1706.02222)). The reported test-set improvements are as follows.

| Model | Test BPC | Absolute Δ vs. its baseline | Relative Δ vs. its baseline |
|---|---|---|---|
| GRURNN (baseline) | 1.39 | — | — |
| GRURNTN (proposed) | 1.33 | 0.06 lower | 4.32% lower |
| LSTMRNN (baseline) | 1.37 | — | — |
| LSTMRNTN (proposed) | 1.34 | 0.03 lower | 2.22% lower |

GRURNTN reduced BPC from 1.39 to 1.33 (0.06 absolute / 4.32% relative) over GRURNN, and LSTMRNTN reduced BPC from 1.37 to 1.34 (0.03 absolute / 2.22% relative) over LSTMRNN ([Tjandra et al., 2017](https://arxiv.org/abs/1706.02222)). The paper also reports that both proposed models produced lower BPC than their baselines from the first epoch to the last, and that GRURNTN progressed faster and converged to a slightly better BPC than LSTMRNTN ([Tjandra et al., 2017](https://arxiv.org/abs/1706.02222)). This epoch-level observation strengthens the result: the advantage is not a single lucky test-set outcome but a consistent separation across training.

### Comparison with previously published character-level results

The gains become larger when the proposed models are placed against older published systems.

| Model | Test BPC | GRURNTN (1.33) advantage | Relative reduction |
|---|---|---|---|
| NNLM | 1.57 | 0.24 | 15.29% |
| BPTT-RNN | 1.42 | 0.09 | 6.34% |
| HF-MRNN | 1.41 | 0.08 | 5.67% |
| sRNN | 1.41 | 0.08 | 5.67% |
| DOT(S)-RNN | 1.39 | 0.06 | 4.32% |
| LSTMRNN w/ adaptive noise, w/o dynamic eval | 1.26 | −0.07 (worse) | −5.56% |
| LSTMRNN w/ adaptive noise, w/ dynamic eval | 1.24 | −0.09 (worse) | −7.26% |

Published comparison values are drawn from the paper's Table I ([Tjandra et al., 2017](https://arxiv.org/abs/1706.02222)). Two important caveats follow. First, the strongest published entries (1.26 and 1.24) use adaptive noise regularization and, in the 1.24 case, dynamic evaluation, which updates model parameters during test-time processing; the authors explicitly note that their baseline and proposed models did not use dynamic evaluation ([Tjandra et al., 2017](https://arxiv.org/abs/1706.02222)). These are therefore not apples-to-apples comparisons. Second, the paper claims that "both proposed models outperformed all of the baseline models on the character-level language modeling task" ([Tjandra et al., 2017](https://arxiv.org/abs/1706.02222)) — a claim that holds with respect to the four models it trained (GRURNN and LSTMRNN) and the older non-adaptive published systems, but not with respect to the adaptive-noise LSTM variants.

## Reported Improvements on Word-Level Language Modeling

### Baseline-relative gains

On the word-level task, performance is reported as perplexity (PPL), again with lower being better ([Tjandra et al., 2017](https://arxiv.org/abs/1706.02222)).

| Model | Test PPL | Absolute Δ vs. its baseline | Relative Δ vs. its baseline |
|---|---|---|---|
| GRURNN (baseline) | 97.78 | — | — |
| GRURNTN (proposed) | 87.38 | 10.4 lower | 10.63% lower |
| LSTMRNN (baseline) | 108.26 | — | — |
| LSTMRNTN (proposed) | 96.97 | 11.29 lower | 10.42% lower |

GRURNTN reduced perplexity from 97.78 to 87.38 (10.4 absolute / 10.63% relative), and LSTMRNTN reduced perplexity from 108.26 to 96.97 (11.29 absolute / 10.42% relative) ([Tjandra et al., 2017](https://arxiv.org/abs/1706.02222)). These are substantially larger relative gains than those observed at the character level (roughly 10% versus 2–4%), which the authors attribute in part to GRURNTN being the best model on this task, consistently achieving lower perplexity than the alternatives ([Tjandra et al., 2017](https://arxiv.org/abs/1706.02222)). The paper also notes that LSTMRNTN's word-level performance "closely resembles the baseline GRURNN," since 96.97 versus 97.78 is a difference of only 0.81 PPL, or about 0.83% relative ([Tjandra et al., 2017](https://arxiv.org/abs/1706.02222)). In other words, the LSTM-based tensor variant essentially catches up to the GRU baseline rather than surpassing the best baseline outright.

### Comparison with previously published word-level results

| Model | Test PPL | GRURNTN (87.38) advantage | Relative reduction |
|---|---|---|---|
| N-Gram | 141 | 53.62 | 38.03% |
| RNNLM (w/o dynamic eval) | 124.7 | 37.32 | 29.93% |
| RNNLM (w/ dynamic eval) | 123.2 | 35.82 | 29.07% |
| SCRNN | 115 | 27.62 | 24.02% |
| sRNN | 110.0 | 22.62 | 20.56% |
| DOT(S)-RNN | 107.5 | 20.12 | 18.72% |

Published comparison values are drawn from the paper's Table II ([Tjandra et al., 2017](https://arxiv.org/abs/1706.02222)). On this task the proposed GRURNTN model is presented as the strongest system in the comparison, outperforming "all the baseline models as well as the other models by a large margin" ([Tjandra et al., 2017](https://arxiv.org/abs/1706.02222)). Notably, GRURNTN's 87.38 PPL is 20.88 points lower than the LSTMRNN baseline (108.26), a 19.29% relative reduction.

## Discrepancy in the Secondary Source

A third-party research note supplied alongside the paper reports a different word-level result for GRURNTN: it states that GRURNTN reduced test PPL "from 97.78 to 92.98, which is 4.8 absolute / 4.91% relative PPL, over GRURNN" (Third-party research note, n.d.). This figure conflicts with the primary source on two independent grounds. First, the paper's Table II lists GRURNTN (proposed) at 87.38, not 92.98 ([Tjandra et al., 2017](https://arxiv.org/abs/1706.02222)). Second, the paper's conclusion states that "GRURNTN obtained 10.4 absolute (10.63% relative) PPL reduction over GRURNN" ([Tjandra et al., 2017](https://arxiv.org/abs/1706.02222)), which is arithmetically consistent with 97.78 → 87.38 but not with 97.78 → 92.98. The secondary note's character-level figures (1.39 → 1.33 and 1.37 → 1.34) do agree exactly with the primary source (Third-party research note, n.d.; [Tjandra et al., 2017](https://arxiv.org/abs/1706.02222)). Because the primary arXiv paper is the more authoritative record and is internally consistent in both its results table and its conclusion, this report treats the 87.38 / 10.4 absolute / 10.63% relative figures as the correct word-level result and flags the 92.98 figure as an apparent error in the secondary note. An analyst relying only on the secondary note would understate GRURNTN's word-level improvement by more than half.

## Synthesis: How Much Improvement, and How Meaningful Is It?

Across both tasks, the consistent finding is that adding a tensor-product interaction to a gated RNN produces a measurable but not uniform improvement. The largest relative gain attributable to the architectural change is GRURNTN on word-level perplexity (10.63%), followed closely by LSTMRNTN on the same task (10.42%). On character-level BPC the gains are smaller: 4.32% for GRURNTN and 2.22% for LSTMRNTN ([Tjandra et al., 2017](https://arxiv.org/abs/1706.02222)). Three interpretive points follow.

First, the GRU-based tensor variant systematically outperformed the LSTM-based tensor variant, both on character-level BPC (1.33 vs. 1.34) and on word-level PPL (87.38 vs. 96.97) ([Tjandra et al., 2017](https://arxiv.org/abs/1706.02222)). This suggests the benefit of tensor products is not equally distributed across gating designs, and that the simpler two-gate GRU formulation interacts more favorably with the bilinear term.

Second, the fairness control matters. Because the paper constrained baseline parameter counts to be similar to the proposed models' ([Tjandra et al., 2017](https://arxiv.org/abs/1706.02222)), the gains cannot be dismissed as the result of adding free parameters. This is the strongest argument in the paper's favor and the reason the reported percentages are more informative than a raw leaderboard comparison.

Third, the absolute magnitudes should temper strong claims. On character-level BPC, a 0.03 improvement (LSTMRNTN) is small, and both proposed models remain behind the adaptive-noise LSTM results of 1.26 and 1.24 reported by Graves, though those employ different regularization and, for 1.24, dynamic evaluation ([Tjandra et al., 2017](https://arxiv.org/abs/1706.02222)). Similarly, LSTMRNTN's 0.83% relative edge over the GRURNN baseline at word level is marginal ([Tjandra et al., 2017](https://arxiv.org/abs/1706.02222)). The strongest, most defensible claim is therefore narrower than the abstract's "significantly improved their performance": both proposed models outperform their matched-parameter baselines on both tasks, with GRURNTN delivering the largest and most consistent gains.

## Limitations of the Evidence

The evaluation is confined to a single dataset (PennTreeBank) and two language-modeling tasks, and the paper does not report statistical significance testing, multiple random seeds, or confidence intervals ([Tjandra et al., 2017](https://arxiv.org/abs/1706.02222)). Comparisons against published systems involve heterogeneous training regimes, regularization schemes, and evaluation protocols, which limits their evidentiary weight; the paper itself notes the dynamic-evaluation caveat for the strongest LSTM comparators ([Tjandra et al., 2017](https://arxiv.org/abs/1706.02222)). The paper also contains minor internal inconsistencies, such as describing the word-level table as "Table I" when the perplexity results appear in Table II, and listing 600 hidden units for "LSTMRNTN" in the character-level configuration where the baseline LSTMRNN was presumably intended ([Tjandra et al., 2017](https://arxiv.org/abs/1706.02222)). Finally, the secondary source's conflicting word-level number demonstrates the value of verifying summary notes against primary tables (Third-party research note, n.d.).

## Conclusion

The introduced models achieve, relative to their matched-parameter baselines, reductions of 0.06 absolute / 4.32% relative BPC (GRURNTN over GRURNN) and 0.03 absolute / 2.22% relative BPC (LSTMRNTN over LSTMRNN) on character-level language modeling, and reductions of 10.4 absolute / 10.63% relative PPL (GRURNTN over GRURNN) and 11.29 absolute / 10.42% relative PPL (LSTMRNTN over LSTMRNN) on word-level language modeling ([Tjandra et al., 2017](https://arxiv.org/abs/1706.02222)). GRURNTN is the stronger of the two proposals on both tasks, and on the word-level task it also exceeds all listed previously published systems by a wide margin (e.g., 20.12 PPL, or 18.72% relative, below DOT(S)-RNN) ([Tjandra et al., 2017](https://arxiv.org/abs/1706.02222)). The improvement is therefore real and consistent within the paper's controlled comparison, but it is task-dependent in size, modest on character-level BPC, and not sufficient to overtake the strongest adaptive-noise LSTM results reported in the same tables ([Tjandra et al., 2017](https://arxiv.org/abs/1706.02222)). The headline word-level improvement is 10.63% relative PPL, not the 4.91% relative figure reported in the secondary note (Third-party research note, n.d.).

## References

Tjandra, A., Sakti, S., Manurung, R., Adriani, M., & Nakamura, S. (2017). *Gated Recurrent Neural Tensor Network* (arXiv:1706.02222). arXiv. https://arxiv.org/abs/1706.02222

Third-party research note: Gated Recurrent Neural Tensor Network. (n.d.). [Unpublished research note, document_2].