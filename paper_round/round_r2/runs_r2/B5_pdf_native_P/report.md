# Quantifying the Improvement of Gated Recurrent Neural Tensor Networks over Gated RNN Baselines

## Introduction and Scope of the Query

This report examines how much improvement the Gated Recurrent Neural Tensor Network (RNTN) architectures introduced by Tjandra, Sakti, Manurung, Adriani, and Nakamura (2017) achieve relative to the previous models against which they were compared. The paper proposes two hybrid architectures — the Long Short-Term Memory Recurrent Neural Tensor Network (LSTMRNTN) and the Gated Recurrent Unit Recurrent Neural Tensor Network (GRURNTN) — and evaluates them on two language modeling tasks using the PennTreeBank (PTB) corpus: character-level language modeling measured by bits-per-character (BPC) and word-level language modeling measured by perplexity (PPL) ([Tjandra et al., 2017](https://arxiv.org/abs/1706.02222)).

The central claim of the paper is that both proposed models outperform their corresponding parameter-matched baselines, with GRURNTN producing the strongest overall results. The improvements are reported in absolute terms and as relative percentages, and they differ substantially between the two tasks: character-level gains are modest, while word-level gains are considerably larger. This report presents those figures in full, situates them against both the authors' own baselines and a broader set of published results, and flags a numerical discrepancy in the accompanying third-party research note.

## The Proposed Architectures and Their Baselines

### What the new models change

The proposed models combine two ideas that the authors argue had not previously been merged in a single recurrent architecture. The first is the gating mechanism found in LSTM and GRU units, which regulates the flow of information across time steps and mitigates vanishing and exploding gradients. The second is the tensor product, which replaces the conventional linear projection-plus-addition interaction between the current input and the previous hidden state with a bilinear, second-degree polynomial interaction ([Tjandra et al., 2017](https://arxiv.org/abs/1706.02222)).

In GRURNTN, the tensor product is applied between the current input and the reset-gated previous hidden state when computing the candidate hidden layer. In LSTMRNTN, the tensor product is applied between the current input and the previous hidden layer when computing the candidate memory cell. Both models use an asymmetric bilinear form with a tensor weight W ∈ R^(i×d×d), where i is the input size and d the hidden size; the authors state that this asymmetric variant reduces the parameter count relative to the original, fully symmetric neural tensor network formulation while retaining input–hidden interaction ([Tjandra et al., 2017](https://arxiv.org/abs/1706.02222)).

### Fairness of the comparison

A notable methodological point is that the baselines were given **larger hidden layers** than the proposed models so that total parameter counts would be comparable. For word-level modeling, GRURNTN and LSTMRNTN used 256 hidden units, while GRURNN used 860 and LSTMRNN used 740; all used 128-dimensional word embeddings, with dropout of p = 0.5 for the proposed models and p = 0.6 for the baselines. For character-level modeling, the proposed models again used 256 hidden units, GRURNN used 820, and LSTMRNN used 600, with 32-dimensional character embeddings and dropout of p = 0.25 ([Tjandra et al., 2017](https://arxiv.org/abs/1706.02222)). Total parameters were approximately 12 million for GRURNN/GRURNTN and 13 million for LSTMRNN/LSTMRNTN in the word-level setting, and approximately 2.2 million and 2.6 million respectively in the character-level setting. The authors explicitly state that they "constrained our baseline GRURNN to have a similar number of parameters as the GRURNTN model for a fair comparison" ([Tjandra et al., 2017](https://arxiv.org/abs/1706.02222)).

This design means the reported gains are attributable to architectural expressiveness rather than to greater capacity. Training used AdaGrad with mini-batches of 15 sentences, a learning-rate decay factor of 0.5 triggered by development-set cost increases, gradient rescaling when the norm exceeded 5, and orthogonal weight initialization ([Tjandra et al., 2017](https://arxiv.org/abs/1706.02222)).

## Character-Level Language Modeling Results

On the PTB character-level task, both proposed models reduced test BPC relative to their direct baselines.

| Model | Test BPC | Change vs. counterpart | Relative change |
|---|---|---|---|
| GRURNN (baseline) | 1.39 | — | — |
| LSTMRNN (baseline) | 1.37 | — | — |
| GRURNTN (proposed) | 1.33 | −0.06 | −4.32% |
| LSTMRNTN (proposed) | 1.34 | −0.03 | −2.22% |

GRURNTN reduced BPC from 1.39 to 1.33, an absolute reduction of 0.06 and a relative reduction of 4.32% over GRURNN. LSTMRNTN reduced BPC from 1.37 to 1.34, an absolute reduction of 0.03 and a relative reduction of 2.22% over LSTMRNN ([Tjandra et al., 2017](https://arxiv.org/abs/1706.02222)). The authors also report that both proposed models produced lower BPC than the baselines from the first epoch through the last, and that GRURNTN converged faster than LSTMRNTN but landed at a similar final BPC ([Tjandra et al., 2017](https://arxiv.org/abs/1706.02222)).

My assessment of these figures is that the character-level improvement is real but small. A 0.06 BPC reduction is meaningful in the context of a metric where published systems cluster tightly between roughly 1.24 and 1.57, but a 2.22% relative gain for the LSTM variant is close to the noise floor that one would expect without repeated runs or significance testing, which the paper does not report.

## Word-Level Language Modeling Results

On the PTB word-level task, the improvements are substantially larger in both absolute and relative terms.

| Model | Test PPL | Change vs. counterpart | Relative change |
|---|---|---|---|
| GRURNN (baseline) | 97.78 | — | — |
| LSTMRNN (baseline) | 108.26 | — | — |
| GRURNTN (proposed) | 87.38 | −10.40 | −10.63% |
| LSTMRNTN (proposed) | 96.97 | −11.29 | −10.42% |

GRURNTN reduced perplexity from 97.78 to 87.38, an absolute reduction of 10.4 PPL and a relative reduction of 10.63% over GRURNN. LSTMRNTN reduced perplexity from 108.26 to 96.97, an absolute reduction of 11.29 PPL and a relative reduction of 10.42% over LSTMRNN ([Tjandra et al., 2017](https://arxiv.org/abs/1706.02222)). The authors further note that LSTMRNTN's final performance "closely resembles the baseline GRURNN," while GRURNTN "outperformed all the baseline models as well as the other models by a large margin" ([Tjandra et al., 2017](https://arxiv.org/abs/1706.02222)). Numerically, LSTMRNTN at 96.97 is 0.81 PPL better than the GRURNN baseline at 97.78, a relative advantage of roughly 0.83%, and GRURNTN is 9.59 PPL better than LSTMRNTN, a relative advantage of roughly 9.9%.

The asymmetry between the two tasks is the most interesting finding in the paper. The GRU variant achieved a 4.32% relative BPC reduction at the character level but a 10.63% relative PPL reduction at the word level, while the LSTM variant achieved 2.22% and 10.42% respectively. In my reading, this suggests that the bilinear input–hidden interaction contributes most when the model must model longer-range dependencies at the word level, and contributes less when the character-level task can already be handled well by gated recurrence alone.

## Comparison Against the Broader Published Literature

### Character-level (test BPC)

| Model | Test BPC |
|---|---|
| NNLM | 1.57 |
| BPTT-RNN | 1.42 |
| HF-MRNN | 1.41 |
| sRNN | 1.41 |
| DOT(S)-RNN | 1.39 |
| GRURNN (baseline) | 1.39 |
| LSTMRNN (baseline) | 1.37 |
| LSTMRNTN (proposed) | 1.34 |
| GRURNTN (proposed) | 1.33 |
| LSTMRNN (adaptive noise, no dynamic eval) | 1.26 |
| LSTMRNN (adaptive noise, dynamic eval) | 1.24 |

GRURNTN at 1.33 BPC improves on NNLM (1.57), BPTT-RNN (1.42), HF-MRNN (1.41), sRNN (1.41), and DOT(S)-RNN (1.39). It does **not** beat the LSTM results using adaptive noise regularization with or without dynamic evaluation (1.26 and 1.24 respectively). The authors explicitly note that their experiments did not use dynamic evaluation and that the adaptive-noise baselines employ a different regularization regime ([Tjandra et al., 2017](https://arxiv.org/abs/1706.02222)). This is an important qualifier: the strongest published character-level numbers in the table come from a different training and regularization setup, so GRURNTN's 1.33 is best understood as the best result among comparably configured models rather than the best overall.

### Word-level (test PPL)

| Model | Test PPL |
|---|---|
| N-Gram | 141 |
| RNNLM (no dynamic eval) | 124.7 |
| RNNLM (dynamic eval) | 123.2 |
| SCRNN | 115 |
| sRNN | 110.0 |
| DOT(S)-RNN | 107.5 |
| GRURNN (baseline) | 97.78 |
| LSTMRNN (baseline) | 108.26 |
| LSTMRNTN (proposed) | 96.97 |
| GRURNTN (proposed) | 87.38 |

Here GRURNTN's 87.38 PPL is the best figure in the table, ahead of DOT(S)-RNN by 20.12 PPL (roughly 18.7% relative) and ahead of the non-dynamic RNNLM by 37.32 PPL (roughly 29.9% relative). LSTMRNTN at 96.97 also outperforms every published baseline listed, including DOT(S)-RNN and sRNN ([Tjandra et al., 2017](https://arxiv.org/abs/1706.02222)).

## A Numerical Discrepancy Worth Flagging

The third-party research note accompanying the paper states that, on word-level modeling, "GRURNTN reduced test PPL from 97.78 to 92.98, which is 4.8 absolute / 4.91% relative PPL, over GRURNN" (Third-party research note, n.d.). This conflicts with the primary source, whose results section and conclusion both report 87.38 PPL, a 10.4 absolute and 10.63% relative reduction, and whose Table II lists GRURNTN at 87.38 ([Tjandra et al., 2017](https://arxiv.org/abs/1706.02222)).

The primary source is internally consistent: the same 87.38 value appears in the results table, in the analysis text, and again in the conclusion. The third-party note's figure of 92.98 is not corroborated anywhere in the paper. Given the guidance to prioritize reliable and primary sources, I treat the paper's 87.38 and 10.63% relative reduction as authoritative and the note's 92.98 / 4.91% figure as erroneous. Notably, the note's character-level figures (1.39 → 1.33 and 1.37 → 1.34) and its LSTMRNTN word-level figures (108.26 → 96.97) agree exactly with the paper, so the discrepancy is isolated to the GRURNTN word-level perplexity value. Readers relying on the note alone for the headline word-level number would substantially understate the reported improvement.

## Interpretation, Limitations, and Overall Verdict

Taken together, the evidence supports the following conclusions about the magnitude of improvement:

1. **Direction is consistent.** All four head-to-head comparisons (two models × two tasks) favor the tensor-augmented variants, and the character-level advantage held across every epoch for both models ([Tjandra et al., 2017](https://arxiv.org/abs/1706.02222)).
2. **Magnitude depends heavily on the task.** Character-level gains are 0.03–0.06 BPC (2.22%–4.32% relative), whereas word-level gains are 10.40–11.29 PPL (10.42%–10.63% relative). The word-level effect is roughly two to five times larger in relative terms.
3. **The gain is architectural, not capacity-driven.** Because baselines were allotted substantially more hidden units (860 vs. 256 for the GRU pair; 740 vs. 256 for the LSTM pair) to match parameter counts, the improvement cannot be attributed to a larger model ([Tjandra et al., 2017](https://arxiv.org/abs/1706.02222)).
4. **GRU is the stronger host for the tensor modification in this study.** GRURNTN produced the best absolute result on both tasks (1.33 BPC, 87.38 PPL) and beat its baseline by the largest relative margin on word-level modeling.

Several limitations qualify these conclusions. The evaluation is restricted to a single corpus (PennTreeBank), with no confidence intervals, significance tests, or multiple random seeds reported, so small deltas — particularly the 0.03 BPC and 2.22% relative gain for LSTMRNTN — should be treated cautiously. The proposed models' advantage in parameter-matched comparisons comes partly from using far fewer hidden units than the baselines, which raises the question of whether the comparison isolates the tensor interaction or simply trades width for a richer interaction function at fixed parameter budget; the paper does not ablate this. Finally, the proposed character-level results do not surpass the adaptive-noise LSTM entries (1.26 and 1.24) because those use a different regularization and dynamic evaluation regime that the authors deliberately excluded ([Tjandra et al., 2017](https://arxiv.org/abs/1706.02222)).

My overall assessment is that the reported improvements are credible and consistently favorable, but their practical significance is task-dependent: a 10.6% relative perplexity reduction at the word level at matched parameter count is a substantial and practically meaningful gain, whereas a 2–4% relative BPC reduction at the character level is a modest gain that would benefit from statistical corroboration before being treated as robust. The single most defensible headline claim is that GRURNTN reduced word-level test perplexity by 10.40 absolute (10.63% relative) over a parameter-matched GRURNN baseline, and by 11.29 absolute (10.42% relative) for LSTMRNTN over LSTMRNN, per the primary source ([Tjandra et al., 2017](https://arxiv.org/abs/1706.02222)).

## References

Tjandra, A., Sakti, S., Manurung, R., Adriani, M., & Nakamura, S. (2017). *Gated Recurrent Neural Tensor Network*. arXiv:1706.02222 [cs.LG]. ([Tjandra et al., 2017](https://arxiv.org/abs/1706.02222))

Third-party research note: Gated Recurrent Neural Tensor Network. (n.d.). [Unpublished research note summarizing Tjandra et al. (2017); no URL provided.]