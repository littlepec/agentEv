# Quantifying the Improvement of the Gated Recurrent Neural Tensor Network Models Over Previous Recurrent Language Models

## Introduction

The paper *Gated Recurrent Neural Tensor Network* (arXiv:1706.02222) by Tjandra, Sakti, Manurung, Adriani and Nakamura proposes a new family of recurrent architectures that fuses two previously separate design ideas: gating mechanisms, which allow a recurrent neural network (RNN) to retain or discard information across long time spans, and tensor products, which allow a network to compute richer, higher-order interactions between the current input and the previous hidden state ([Tjandra et al., 2017](https://arxiv.org/abs/1706.02222)). Two concrete models are derived from this fusion: the Long-Short Term Memory Recurrent Neural Tensor Network (LSTMRNTN) and the Gated Recurrent Unit Recurrent Neural Tensor Network (GRURNTN) ([Tjandra et al., 2017](https://arxiv.org/abs/1706.02222)).

The central empirical claim of the work is that both proposed models significantly improve on their matched gated baselines — LSTMRNN and GRURNN — when evaluated on PennTreeBank (PTB) word-level and character-level language modelling tasks ([Tjandra et al., 2017](https://arxiv.org/abs/1706.02222)). The purpose of this report is to answer a single question in quantitative detail: **how much improvement do the introduced models achieve compared to the previous models?** The answer is presented along two axes: improvement relative to the authors' own parameter-matched baselines, and improvement relative to previously published systems listed in the paper's benchmark tables.

## Background: Where the Improvement Is Expected to Originate

### Baseline architectures

The two baselines are the standard Long Short-Term Memory (LSTM) RNN and the Gated Recurrent Unit (GRU) RNN. LSTM employs three gating layers (input, forget, output) together with a separate memory cell that stores information across time, whereas GRU uses only two gates (reset and update) and dispenses with a separate memory cell ([Tjandra et al., 2017](https://arxiv.org/abs/1706.02222)). The paper notes that despite having one fewer gating layer, GRU can match LSTM's performance and sometimes converges faster ([Tjandra et al., 2017](https://arxiv.org/abs/1706.02222)).

Gating solves the problem of vanishing or exploding gradients, but the authors argue it does not change the *expressiveness* of the input-to-hidden relationship: in both baselines, the interaction between current input and previous hidden state remains a linear projection plus addition, subsequently transformed by a nonlinear activation ([Tjandra et al., 2017](https://arxiv.org/abs/1706.02222)). This is the gap the proposed models target.

### The tensor-product addition

The proposed models insert a tensor weight parameter *W*<sub>tsr</sub> ∈ ℝ<sup>i×d×d</sup> that maps a bilinear product of the current input and the (gated) previous hidden state into the recurrent computation ([Tjandra et al., 2017](https://arxiv.org/abs/1706.02222)). GRURNTN applies this operation inside the candidate hidden-state equation using the reset-gate-modulated previous hidden state, while LSTMRNTN applies it inside the candidate cell equation using the raw previous hidden state ([Tjandra et al., 2017](https://arxiv.org/abs/1706.02222)). The authors deliberately adopt an asymmetric bilinear form rather than the fully symmetric Recursive Neural Tensor Network formulation in order to reduce the number of tensor parameters while preserving input–hidden interaction ([Tjandra et al., 2017](https://arxiv.org/abs/1706.02222)). The stated theoretical benefit is a shift from first-degree polynomial interactions (dot product plus addition) to second-degree polynomial interactions ([Tjandra et al., 2017](https://arxiv.org/abs/1706.02222)).

## Experimental Setup and Controlled Comparison

The evaluation uses the PennTreeBank corpus, a standard benchmark for statistical language modelling, split into 930,000 training words (sections 0–20), 74,000 validation words (sections 21–22) and 82,000 test words (sections 23–24), with vocabulary limited to the 10,000 most common words ([Tjandra et al., 2017](https://arxiv.org/abs/1706.02222)). Two tasks are run: word-level prediction measured by perplexity (PPL) and character-level prediction measured by bits-per-character (BPC); lower values are better on both metrics ([Tjandra et al., 2017](https://arxiv.org/abs/1706.02222)).

Crucially, the authors constrained each baseline to have approximately the same number of free parameters as its corresponding tensor model, stating explicitly that "we constrained our baseline GRURNN to have a similar number of parameters as the GRURNTN model for a fair comparison" and applied the same constraint between LSTMRNN and LSTMRNTN ([Tjandra et al., 2017](https://arxiv.org/abs/1706.02222)). This design decision matters for interpreting the magnitude of the gains.

| Configuration item | Word-level task | Character-level task |
|---|---|---|
| Hidden units, GRURNTN / LSTMRNTN | 256 / 256 | 256 / 256 |
| Hidden units, GRURNN / LSTMRNN | 860 / 740 | 820 / 600 |
| Embedding dimensions | 128 (word) | 32 (character) |
| Dropout probability, proposed / baseline | 0.5 / 0.6 | 0.25 / 0.25 |
| Parameters, GRURNN & GRURNTN | ≈12 million | ≈2.2 million |
| Parameters, LSTMRNN & LSTMRNTN | ≈13 million | ≈2.6 million |

*Note.* All values as reported in the experiment settings section ([Tjandra et al., 2017](https://arxiv.org/abs/1706.02222)).

All models were optimised with AdaGrad, mini-batches of 15 sentences, learning-rate halving on development-set cost increases, gradient rescaling when the norm exceeded 5, and orthogonal weight initialisation ([Tjandra et al., 2017](https://arxiv.org/abs/1706.02222)).

## Quantitative Improvement: Character-Level Language Modelling

On the PTB character-level task, both proposed models reduced test BPC relative to their matched baselines ([Tjandra et al., 2017](https://arxiv.org/abs/1706.02222)).

| Model | Test BPC | Absolute change vs. baseline | Relative change vs. baseline |
|---|---|---|---|
| GRURNN (baseline) | 1.39 | — | — |
| **GRURNTN (proposed)** | **1.33** | **−0.06** | **−4.32%** |
| LSTMRNN (baseline) | 1.37 | — | — |
| **LSTMRNTN (proposed)** | **1.34** | **−0.03** | **−2.22%** |

*Note.* Lower BPC is better. Deltas computed from reported test-set values ([Tjandra et al., 2017](https://arxiv.org/abs/1706.02222)).

The GRURNTN improvement of 0.06 BPC (4.32% relative) is approximately twice the magnitude of the LSTMRNTN improvement of 0.03 BPC (2.22% relative) ([Tjandra et al., 2017](https://arxiv.org/abs/1706.02222)). The paper further reports that both proposed models produced lower BPC than the baselines from the first epoch to the last epoch on the validation set, and that GRURNTN converged to a similar BPC as LSTMRNTN in the final epoch; overall GRURNTN slightly outperformed LSTMRNTN on this task ([Tjandra et al., 2017](https://arxiv.org/abs/1706.02222)). An independent research note summarising the same results repeats these figures verbatim ([Third-party research note](#references)).

## Quantitative Improvement: Word-Level Language Modelling

The word-level task shows substantially larger relative gains, which is the most significant finding of the paper ([Tjandra et al., 2017](https://arxiv.org/abs/1706.02222)).

| Model | Test PPL | Absolute change vs. baseline | Relative change vs. baseline |
|---|---|---|---|
| GRURNN (baseline) | 97.78 | — | — |
| **GRURNTN (proposed)** | **87.38** | **−10.40** | **−10.63%** |
| LSTMRNN (baseline) | 108.26 | — | — |
| **LSTMRNTN (proposed)** | **96.97** | **−11.29** | **−10.42%** |

*Note.* Lower PPL is better. Deltas computed from reported test-set values ([Tjandra et al., 2017](https://arxiv.org/abs/1706.02222)).

Both tensor models delivered roughly a 10% relative reduction in perplexity over their respective baselines — a consistent effect size across the two architectures ([Tjandra et al., 2017](https://arxiv.org/abs/1706.02222)). The paper reports that GRURNTN was the best model on this task, maintaining a consistently lower PPL than all other models throughout training, and that LSTMRNTN's final performance closely resembles the baseline GRURNN (96.97 vs. 97.78) ([Tjandra et al., 2017](https://arxiv.org/abs/1706.02222)). In other words, adding a tensor product to the GRU yielded a model that clearly dominated both baselines, whereas adding it to the LSTM lifted that architecture only back to the level of the plain GRU baseline ([Tjandra et al., 2017](https://arxiv.org/abs/1706.02222)).

## Improvement Relative to Previously Published Systems

The paper also positions its models against external published results ([Tjandra et al., 2017](https://arxiv.org/abs/1706.02222)).

| System | Character BPC | Word PPL |
|---|---|---|
| N-Gram | — | 141 |
| NNLM | 1.57 | — |
| BPTT-RNN | 1.42 | — |
| HF-MRNN | 1.41 | — |
| sRNN | 1.41 | 110.0 |
| DOT(S)-RNN | 1.39 | 107.5 |
| SCRNN | — | 115 |
| RNNLM (w/o dynamic evaluation) | — | 124.7 |
| RNNLM (w/ dynamic evaluation) | — | 123.2 |
| LSTMRNN w/ adaptive noise, w/o dynamic evaluation | 1.26 | — |
| LSTMRNN w/ adaptive noise, w/ dynamic evaluation | 1.24 | — |
| **GRURNTN (proposed)** | **1.33** | **87.38** |
| **LSTMRNTN (proposed)** | **1.34** | **96.97** |

*Note.* Compiled from Tables I and II of the source paper ([Tjandra et al., 2017](https://arxiv.org/abs/1706.02222)). The adaptive-noise LSTM rows employ additional regularisation and dynamic evaluation techniques that the authors' own models and baselines did not use ([Tjandra et al., 2017](https://arxiv.org/abs/1706.02222)).

On the word-level task, GRURNTN's 87.38 PPL is a 20.1-point improvement over the strongest external baseline listed (DOT(S)-RNN at 107.5), an 18.7% relative reduction, and is 53.6 points (38.0%) better than the N-Gram baseline ([Tjandra et al., 2017](https://arxiv.org/abs/1706.02222)). Even the weaker proposed model, LSTMRNTN at 96.97, beats every external system in the table by at least 10.5 PPL points ([Tjandra et al., 2017](https://arxiv.org/abs/1706.02222)). On the character-level task the picture is more nuanced: GRURNTN (1.33) and LSTMRNTN (1.34) beat DOT(S)-RNN (1.39), sRNN (1.41), HF-MRNN (1.41), BPTT-RNN (1.42) and NNLM (1.57), but remain behind the LSTM variants using adaptive noise regularisation (1.26) and dynamic evaluation (1.24) ([Tjandra et al., 2017](https://arxiv.org/abs/1706.02222)).

## Interpretation, Caveats and an Assessment of the Evidence

Several points qualify how the reported improvements should be read.

First, the internal comparison is deliberately fair: baselines were given parameter budgets comparable to the tensor models (≈12M vs. ≈12M, and ≈13M vs. ≈13M on word-level; ≈2.2M vs. ≈2.2M and ≈2.6M vs. ≈2.6M on character-level), and hidden-layer sizes were reduced in the proposed models (256 units) while baselines used larger layers (740–860 units) to reach the same parameter count ([Tjandra et al., 2017](https://arxiv.org/abs/1706.02222)). This means the reported gains reflect architectural expressiveness rather than simple parameter scaling.

Second, there is a direct factual conflict between the two supplied sources on this exact point. The third-party research note asserts that the proposed models "outperformed the baseline models with roughly twice the number of parameters in character-level language modeling and word-level language modeling tasks" ([Third-party research note](#references)). The primary paper states the opposite: that baselines were constrained to have a similar number of parameters for a fair comparison ([Tjandra et al., 2017](https://arxiv.org/abs/1706.02222)). Given that the primary source contains the full experiment-settings section and explicit parameter counts, the primary paper should be treated as authoritative, and the secondary note's parameter claim should be regarded as an error introduced during summarisation.

Third, the paper's own experimental section contains at least one apparent typographical inconsistency: the character-level configuration lists "600 for LSTMRNTN" among the hidden-unit counts, where the context (a list distinguishing baselines from proposed models, all of which use 256 units) indicates this should read LSTMRNN ([Tjandra et al., 2017](https://arxiv.org/abs/1706.02222)). Similarly, the GRU update-gate bias in Equation 9 is written as *b*<sub>r</sub> rather than *b*<sub>z</sub>, which appears to be a transcription slip ([Tjandra et al., 2017](https://arxiv.org/abs/1706.02222)).

Fourth, the results derive from a single corpus (PennTreeBank) and, as reported, single training runs without variance estimates or significance testing, despite the abstract's claim of "significantly improved" performance ([Tjandra et al., 2017](https://arxiv.org/abs/1706.02222)). The 0.03 BPC gain for LSTMRNTN over LSTMRNN — a 2.22% relative reduction — is small enough that run-to-run variance could plausibly account for part of it, and the paper provides no confidence intervals to rule this out ([Tjandra et al., 2017](https://arxiv.org/abs/1706.02222)).

Fifth, the improvement pattern is asymmetric by architecture: GRU benefits more from the tensor product than LSTM does, especially at the word level where GRURNTN (87.38) is roughly 9.6 PPL better than LSTMRNTN (96.97) despite both being compared against baselines of differing quality ([Tjandra et al., 2017](https://arxiv.org/abs/1706.02222)). Conversely, the authors' own LSTMRNN baseline (108.26 PPL) was considerably weaker than the GRURNN baseline (97.78 PPL), so the LSTMRNTN gain of 10.42% is measured from a lower starting point ([Tjandra et al., 2017](https://arxiv.org/abs/1706.02222)).

My own assessment, based strictly on the supplied material, is that the evidence supports a genuine and consistent improvement, but of two different magnitudes. At the word level, the roughly 10% relative perplexity reduction delivered by both tensor models, combined with GRURNTN's decisive margin over all published comparators, constitutes a substantive advance. At the character level, the gains are real but modest — 4.32% relative for GRURNTN and 2.22% for LSTMRNTN — and do not surpass the best externally reported LSTM configurations, which used additional regularisation and evaluation-time adaptation that the proposed models did not employ ([Tjandra et al., 2017](https://arxiv.org/abs/1706.02222)). The headline characterisation that both models "significantly improved their performance" is therefore best read as directionally correct for character-level modelling and strongly supported for word-level modelling.

## Conclusion

Relative to their parameter-matched baselines, the proposed Gated Recurrent Neural Tensor Network models achieve the following improvements. GRURNTN reduces character-level test BPC from 1.39 to 1.33, a 0.06 absolute and 4.32% relative gain, and reduces word-level test PPL from 97.78 to 87.38, a 10.4 absolute and 10.63% relative gain ([Tjandra et al., 2017](https://arxiv.org/abs/1706.02222)). LSTMRNTN reduces character-level test BPC from 1.37 to 1.34, a 0.03 absolute and 2.22% relative gain, and reduces word-level test PPL from 108.26 to 96.97, an 11.29 absolute and 10.42% relative gain ([Tjandra et al., 2017](https://arxiv.org/abs/1706.02222)). Both models therefore produce lower test scores than their corresponding baselines across both tasks, with GRURNTN emerging as the strongest overall model, particularly on the word-level task where it also outperforms every previously published system reported in the comparison ([Tjandra et al., 2017](https://arxiv.org/abs/1706.02222)). The improvement is thus consistent and architecturally reproducible, but it is roughly four to five times larger in relative terms at the word level than at the character level, and the strongest claims rest on a single benchmark corpus without repeated-run variance reporting.

## References

Tjandra, A., Sakti, S., Manurung, R., Adriani, M., & Nakamura, S. (2017). *Gated recurrent neural tensor network* (arXiv:1706.02222). arXiv. https://arxiv.org/abs/1706.02222

Third-party research note: Gated recurrent neural tensor network [Unpublished research note]. (n.d.).