# Quantifying the Improvement of Gated Recurrent Neural Tensor Networks over Standard Gated Recurrent Baselines

## 1. Purpose and Evidence Base

This report answers a single question: **how much improvement do the introduced models achieve compared to the previous models?** The introduced models are the **Gated Recurrent Unit Recurrent Neural Tensor Network (GRURNTN)** and the **Long Short-Term Memory Recurrent Neural Tensor Network (LSTMRNTN)**, both proposed by Tjandra, Sakti, Manurung, Adriani and Nakamura (2017). Their reference points are two matched baselines — the standard **Gated Recurrent Unit RNN (GRURNN)** and the standard **Long Short-Term Memory RNN (LSTMRNN)** — plus a set of published prior results on the same benchmark ([Tjandra et al., 2017](https://arxiv.org/abs/1706.02222)).

Two sources are available. The primary source is the arXiv preprint of the paper itself (arXiv:1706.02222), which contains the full experimental protocol, tables and derivations ([Tjandra et al., 2017](https://arxiv.org/abs/1706.02222)). The secondary source is a short third-party research note that restates the headline figures and frames them as improvements ([Third-party research note, n.d.](document_2.txt)). Because the primary source is the peer-visible manuscript and contains the underlying tables, it is treated here as authoritative; the secondary note is used only where it agrees with the primary source, and one of its claims is flagged as inconsistent in Section 8.

All experiments were run on the **PennTreeBank (PTB)** corpus, a standard statistical language-modelling benchmark with a 10,000-word vocabulary, split into 930,000 training words, 74,000 validation words and 82,000 test words ([Tjandra et al., 2017](https://arxiv.org/abs/1706.02222)). Two tasks were evaluated: **character-level language modelling**, measured in bits-per-character (BPC, lower is better), and **word-level language modelling**, measured in perplexity (PPL, lower is better) ([Tjandra et al., 2017](https://arxiv.org/abs/1706.02222)).

## 2. Fairness of the Comparison: Experimental Protocol

Before quantifying the gains, it is necessary to establish that the comparison is like-for-like. The authors explicitly state that the baselines were constrained to have a similar number of free parameters to the proposed tensor models in order to make the comparison fair ([Tjandra et al., 2017](https://arxiv.org/abs/1706.02222)). In the word-level task, GRURNN and GRURNTN had approximately 12 million parameters, while LSTMRNN and LSTMRNTN had approximately 13 million; in the character-level task the figures were approximately 2.2 million and 2.6 million respectively ([Tjandra et al., 2017](https://arxiv.org/abs/1706.02222)). The paper's conclusion reinforces this, stating that the proposed models "outperformed the baseline models with a similar number of parameters" in both tasks ([Tjandra et al., 2017](https://arxiv.org/abs/1706.02222)).

Architecturally, the baselines were given **larger hidden layers** than the proposed models to compensate for the tensor parameters: 860 hidden units for GRURNN and 740 for LSTMRNN versus 256 for both proposed models in the word-level task, and 820 and 600 versus 256 in the character-level task ([Tjandra et al., 2017](https://arxiv.org/abs/1706.02222)). Both families used 128-dimensional word embeddings (word-level) or 32-dimensional character embeddings (character-level), AdaGrad optimisation with mini-batches of 15 sentences, gradient rescaling when the norm exceeded 5, and orthogonal weight initialisation ([Tjandra et al., 2017](https://arxiv.org/abs/1706.02222)). Dropout probability differed slightly: p = 0.5 for the proposed models versus p = 0.6 for the baselines in the word-level task, and p = 0.25 across the board in the character-level task ([Tjandra et al., 2017](https://arxiv.org/abs/1706.02222)). The dropout asymmetry is a minor caveat, but the parameter-count control is the more important safeguard.

## 3. Character-Level Language Modelling: Modest but Consistent Gains

Table 1 reports the PTB test-set BPC for the four models.

| Model | Test BPC | Absolute Δ vs. matched baseline | Relative Δ vs. matched baseline |
|---|---|---|---|
| GRURNN (baseline) | 1.39 | — | — |
| **GRURNTN (proposed)** | **1.33** | **−0.06** | **−4.32%** |
| LSTMRNN (baseline) | 1.37 | — | — |
| **LSTMRNTN (proposed)** | **1.34** | **−0.03** | **−2.22%** |

Both proposed models improved on their matched baselines ([Tjandra et al., 2017](https://arxiv.org/abs/1706.02222)). GRURNTN reduced BPC from 1.39 to 1.33, an absolute reduction of 0.06 BPC or a 4.32% relative reduction over GRURNN; LSTMRNTN reduced BPC from 1.37 to 1.34, an absolute reduction of 0.03 BPC or a 2.22% relative reduction over LSTMRNN ([Tjandra et al., 2017](https://arxiv.org/abs/1706.02222)).

Three observations follow. First, the gains are real but small in **absolute** terms: 0.06 and 0.03 bits per character. Second, the **relative** gain from the tensor product is roughly twice as large in the GRU variant (4.32%) as in the LSTM variant (2.22%). Third, the proposed models did not merely beat their own baselines — they beat both baselines across the board: GRURNTN's 1.33 is also lower than the LSTMRNN baseline's 1.37 (a 2.92% relative reduction), and LSTMRNTN's 1.34 is also lower than the GRURNN baseline's 1.39 (a 3.60% relative reduction) ([Tjandra et al., 2017](https://arxiv.org/abs/1706.02222)). The paper reports that GRURNTN made faster training progress than LSTMRNTN and converged to a similar BPC in the final epoch, and that both proposed models produced lower BPC than the baselines from the first epoch to the last ([Tjandra et al., 2017](https://arxiv.org/abs/1706.02222)).

## 4. Word-Level Language Modelling: Substantially Larger Gains

Table 2 reports the PTB test-set perplexity.

| Model | Test PPL | Absolute Δ vs. matched baseline | Relative Δ vs. matched baseline |
|---|---|---|---|
| GRURNN (baseline) | 97.78 | — | — |
| **GRURNTN (proposed)** | **87.38** | **−10.40** | **−10.63%** |
| LSTMRNN (baseline) | 108.26 | — | — |
| **LSTMRNTN (proposed)** | **96.97** | **−11.29** | **−10.42%** |

Here the effect is materially larger. GRURNTN reduced perplexity from 97.78 to 87.38, an absolute reduction of 10.4 PPL or 10.63% relative; LSTMRNTN reduced perplexity from 108.26 to 96.97, an absolute reduction of 11.29 PPL or 10.42% relative ([Tjandra et al., 2017](https://arxiv.org/abs/1706.02222)). The third-party note reports identical figures ([Third-party research note, n.d.](document_2.txt)).

Comparatively, the relative reduction on the word-level task (10.42–10.63%) is approximately **2.5 to 4.7 times larger** than on the character-level task (2.22–4.32%). This is the single most defensible claim of improvement in the paper: on a perplexity basis, swapping the additive input-to-hidden interaction for a tensor (bilinear) interaction inside the gating equations buys roughly a tenth of the baseline error.

Two nuances are important for an impartial reading. First, the LSTMRNN baseline was unusually weak on this task (108.26 PPL), weaker than the GRURNN baseline (97.78). Consequently, LSTMRNTN's 96.97 PPL largely **recovers to**, rather than decisively surpasses, the GRURNN baseline's 97.78 — the residual advantage is only 0.81 PPL, or 0.83% relative ([Tjandra et al., 2017](https://arxiv.org/abs/1706.02222)). Second, the authors themselves note this: "LSTMRNTN improved the LSTMRNN model and its performance closely resembles the baseline GRURNN. However, GRURNTN outperformed all the baseline models as well as the other models by a large margin" ([Tjandra et al., 2017](https://arxiv.org/abs/1706.02222)). Measured against the stronger baseline, GRURNTN's advantage is 10.4 PPL (10.63% relative); measured against the weaker LSTMRNN baseline, it is 20.88 PPL (19.29% relative).

## 5. Improvement Relative to Previously Published Systems

The paper also positions the proposed models against published PTB results. Table 3 consolidates both tables.

| Model | Task | Score |
|---|---|---|
| NNLM | Char BPC | 1.57 |
| BPTT-RNN | Char BPC | 1.42 |
| HF-MRNN | Char BPC | 1.41 |
| sRNN | Char BPC | 1.41 |
| DOT(S)-RNN | Char BPC | 1.39 |
| LSTMRNN (adaptive noise, no dynamic eval.) | Char BPC | 1.26 |
| LSTMRNN (adaptive noise, with dynamic eval.) | Char BPC | 1.24 |
| N-Gram | Word PPL | 141 |
| RNNLM (no dynamic eval.) | Word PPL | 124.7 |
| RNNLM (with dynamic eval.) | Word PPL | 123.2 |
| SCRNN | Word PPL | 115 |
| sRNN | Word PPL | 110.0 |
| DOT(S)-RNN | Word PPL | 107.5 |
| GRURNTN (proposed) | Word PPL | 87.38 |
| LSTMRNTN (proposed) | Word PPL | 96.97 |

Data from ([Tjandra et al., 2017](https://arxiv.org/abs/1706.02222)).

On the character-level task, GRURNTN's 1.33 is 4.32% lower than the strongest comparable published non-dynamic-evaluation result listed, DOT(S)-RNN at 1.39, and LSTMRNTN's 1.34 is 3.60% lower ([Tjandra et al., 2017](https://arxiv.org/abs/1706.02222)). However, the proposed models do **not** surpass the adaptive-noise LSTM results of 1.26 and 1.24: GRURNTN's 1.33 remains 5.56% worse than 1.26 and 7.26% worse than 1.24 ([Tjandra et al., 2017](https://arxiv.org/abs/1706.02222)). The authors explicitly note that their experiments did not use adaptive noise regularisation or dynamic evaluation, so this is not a like-for-like comparison, but it does bound the claim: the improvement is an improvement over matched gated-RNN baselines, not a new state of the art on PTB character modelling.

On the word-level task, the picture is stronger. GRURNTN's 87.38 PPL is 18.72% lower than the best comparable listed published result (DOT(S)-RNN, 107.5), 20.6% lower than sRNN (110.0) and 29.1% lower than RNNLM with dynamic evaluation (123.2); LSTMRNTN's 96.97 is 9.80% lower than DOT(S)-RNN ([Tjandra et al., 2017](https://arxiv.org/abs/1706.02222)).

## 6. Why the Improvement Occurs: Mechanism

The gains are attributed to a specific architectural change rather than to extra tuning. The paper argues that standard RNNs model the input-to-hidden relationship through linear projection, addition and a nonlinearity, which corresponds to **first-degree polynomial interactions**, whereas the tensor product introduces **second-degree polynomial interactions** in a bilinear form ([Tjandra et al., 2017](https://arxiv.org/abs/1706.02222)). In GRURNTN the tensor product is applied between the current input and the reset-gated previous hidden layer when computing the candidate hidden layer; in LSTMRNTN it is applied between the current input and the previous hidden layer when computing the candidate memory cell ([Tjandra et al., 2017](https://arxiv.org/abs/1706.02222)). An asymmetric bilinear form is used to limit parameter growth ([Tjandra et al., 2017](https://arxiv.org/abs/1706.02222)).

The authors derive the backpropagation-through-time gradients with respect to the tensor weight (their Equations 24 and 25) and observe that each tensor slice is learned "more directly from their input and hidden layer values compared by using standard addition operations" ([Tjandra et al., 2017](https://arxiv.org/abs/1706.02222)). The gating units supply the long-range memory; the tensor product supplies the expressiveness. The paper states that, to the authors' knowledge, no prior work had combined the two ([Tjandra et al., 2017](https://arxiv.org/abs/1706.02222)).

## 7. Training Dynamics

Beyond final scores, the paper reports that GRURNN made faster early progress than LSTMRNN in both tasks, that GRURNTN progressed faster than LSTMRNTN, and that both proposed models maintained lower BPC (character-level) and lower PPL (word-level) than their baselines across every epoch of validation ([Tjandra et al., 2017](https://arxiv.org/abs/1706.02222)). The best model overall on the word-level task was GRURNTN, "which had a consistently lower PPL than the other models" ([Tjandra et al., 2017](https://arxiv.org/abs/1706.02222)). This consistency is meaningful: it argues against the possibility that a single fortunate epoch produced the final test figure.

## 8. Caveats and an Inconsistency Between Sources

Three caveats should be weighed.

**No statistical testing.** The abstract describes the results as "significantly improved," but the paper reports no multiple-seed runs, confidence intervals or significance tests ([Tjandra et al., 2017](https://arxiv.org/abs/1706.02222)). For the character-level gains of 0.03 BPC, this matters: a 2.22% relative difference is small enough that run-to-run variance could plausibly account for part of it. The word-level gains are large enough (≈10% relative) that this concern is much weaker.

**Single corpus, single domain.** All results come from PTB. The authors propose speech recognition and video recognition as future work ([Tjandra et al., 2017](https://arxiv.org/abs/1706.02222)). The stated improvement is therefore established for PTB language modelling only.

**Source inconsistency on parameter counts.** The third-party note asserts that the proposed models "outperformed the baseline models with roughly twice the number of parameters" ([Third-party research note, n.d.](document_2.txt)). This conflicts with the primary source, which reports approximately 12 million parameters for GRURNN/GRURNTN and approximately 13 million for LSTMRNN/LSTMRNTN, and which states that baselines were constrained "to have a similar number of parameters" for a fair comparison ([Tjandra et al., 2017](https://arxiv.org/abs/1706.02222)). Given this direct conflict, the primary source should be preferred, and the "twice the parameters" framing should not be relied upon. This is precisely the kind of claim for which a third-party summary is a less reliable witness than the manuscript.

A fourth, minor point: the paper's character-level model description contains an apparent typographical slip, listing "600 for LSTMRNTN" among the baseline hidden-unit counts ([Tjandra et al., 2017](https://arxiv.org/abs/1706.02222)). This does not affect the headline figures but is worth noting for anyone attempting exact replication.

## 9. Assessment and Verdict

The improvement achieved by the introduced models, judged strictly on the reported evidence, can be summarised as follows. Against **matched gated-RNN baselines with comparable parameter budgets**, GRURNTN and LSTMRNTN deliver a **character-level BPC reduction of 0.06 (4.32% relative) and 0.03 (2.22% relative)** respectively, and a **word-level perplexity reduction of 10.4 (10.63% relative) and 11.29 (10.42% relative)** respectively ([Tjandra et al., 2017](https://arxiv.org/abs/1706.02222)).

The evidence supports a clear, qualified conclusion. The **word-level perplexity improvement of roughly 10% relative is the substantive result** — it is large in absolute PPL terms, consistent across epochs, holds against both matched baselines and against the strongest comparable published systems listed, and is obtained without increasing the parameter count beyond the baseline budget ([Tjandra et al., 2017](https://arxiv.org/abs/1706.02222)). The **character-level gain is real but marginal**: 0.03–0.06 BPC absolute, with the LSTMRNTN reduction at only 2.22% relative, an effect size small enough that the absence of any variance reporting or significance testing prevents a strong claim on its own ([Tjandra et al., 2017](https://arxiv.org/abs/1706.02222)).

Finally, the improvement is **asymmetric across the two variants**. GRURNTN outperformed LSTMRNTN on both tasks and, on the word-level task, outperformed "all the baseline models as well as the other models by a large margin" ([Tjandra et al., 2017](https://arxiv.org/abs/1706.02222)). LSTMRNTN, by contrast, improved substantially on its own weak LSTMRNN baseline but finished only marginally better than the GRURNN baseline it was not directly compared against in the paper's own framing. The reasonable reading, therefore, is that combining gating with a tensor product produces a genuine and, in the word-level case, material improvement — and that the GRU-based instantiation of the idea is the more successful of the two.

## References

Tjandra, A., Sakti, S., Manurung, R., Adriani, M., & Nakamura, S. (2017). *Gated Recurrent Neural Tensor Network* (arXiv:1706.02222). arXiv. https://arxiv.org/abs/1706.02222

Third-party research note: Gated Recurrent Neural Tensor Network [Unpublished research note]. (n.d.). document_2.txt