# How Much Improvement Do Gated Recurrent Neural Tensor Networks Achieve Over Prior Models?

## Scope and Evaluation Framework

This report quantifies the performance gain reported by Tjandra, Sakti, Manurung, Adriani, and Nakamura (2017) for two newly introduced recurrent architectures — the Long Short-Term Memory Recurrent Neural Tensor Network (LSTMRNTN) and the Gated Recurrent Unit Recurrent Neural Tensor Network (GRURNTN) — relative to the prior, non-tensor gated baselines LSTMRNN and GRURNN. Both proposed models fuse two established ideas: gating mechanisms that control information flow across time, and tensor-product operations that create richer, second-degree polynomial interactions between the current input and the previous hidden state, rather than the first-degree dot-product-plus-addition interactions used in standard gated RNNs ([Tjandra et al., 2017](https://arxiv.org/abs/1706.02222)).

The evaluation covers two tasks on the PennTreeBank (PTB) corpus: word-level language modeling measured by perplexity (PPL) and character-level language modeling measured by bits-per-character (BPC), where lower scores are better in both cases ([Tjandra et al., 2017](https://arxiv.org/abs/1706.02222)).

## Experimental Controls and Fairness of the Comparison

The strength of the reported gains depends heavily on whether the comparison is parameter-matched. The authors explicitly state that they constrained the baseline GRURNN to have a similar number of free parameters to GRURNTN, and applied the same constraint to LSTMRNN relative to LSTMRNTN, "for a fair comparison" ([Tjandra et al., 2017](https://arxiv.org/abs/1706.02222)). Reported parameter magnitudes were approximately 12–13 million at word level and 2.2–2.6 million at character level ([Tjandra et al., 2017](https://arxiv.org/abs/1706.02222)).

An important structural detail is that parity in total parameters was achieved with very different hidden-layer widths, as summarized below.

| Setting | Configurations |
|---|---|
| Word-level | 256 hidden units for GRURNTN/LSTMRNTN; 860 for GRURNN; 740 for LSTMRNN; 128-dim word embeddings ([Tjandra et al., 2017](https://arxiv.org/abs/1706.02222)) |
| Character-level | 256 hidden units for GRURNTN/LSTMRNTN; 820 for GRURNN; 600 for LSTMRNN; 32-dim character embeddings ([Tjandra et al., 2017](https://arxiv.org/abs/1706.02222)) |
| Regularization | Dropout p = 0.5 (word-level) and p = 0.25 (character-level); gradient rescaling when norm > 5 ([Tjandra et al., 2017](https://arxiv.org/abs/1706.02222)) |
| Optimization | AdaGrad, mini-batch of 15 sentences; orthogonal weight initialization; BPTT with optional truncation ([Tjandra et al., 2017](https://arxiv.org/abs/1706.02222)) |

This means the tensor models reached the same or better scores with roughly one-third of the hidden units used by their baselines, because the tensor weight itself consumes parameters. The authors further note that the asymmetric bilinear formulation was adopted specifically to reduce the parameter burden of the original neural tensor network formulation ([Tjandra et al., 2017](https://arxiv.org/abs/1706.02222)).

## Character-Level Language Modeling: Modest but Consistent Gains

On the PTB character-level task, both proposed models improved over their matched baselines.

| Model | Test BPC | Absolute change | Relative change |
|---|---|---|---|
| GRURNN (baseline) | 1.39 | — | — |
| GRURNTN (proposed) | 1.33 | −0.06 | −4.32% |
| LSTMRNN (baseline) | 1.37 | — | — |
| LSTMRNTN (proposed) | 1.34 | −0.03 | −2.22% |

GRURNTN reduced BPC from 1.39 to 1.33, an absolute reduction of 0.06 and a 4.32% relative reduction; LSTMRNTN reduced BPC from 1.37 to 1.34, an absolute reduction of 0.03 and a 2.22% relative reduction ([Tjandra et al., 2017](https://arxiv.org/abs/1706.02222)). The paper also reports that both proposed models produced lower BPC than the baselines from the first epoch to the last, and that GRURNTN progressed faster and converged to a similar final BPC as LSTMRNTN ([Tjandra et al., 2017](https://arxiv.org/abs/1706.02222)).

In absolute terms, these character-level gains are small. On the word-level task, the picture is quite different.

## Word-Level Language Modeling: Substantial Two-Digit Relative Gains

Word-level results show considerably larger improvements than the character-level results.

| Model | Test PPL | Absolute change | Relative change |
|---|---|---|---|
| GRURNN (baseline) | 97.78 | — | — |
| GRURNTN (proposed) | 87.38 | −10.40 | −10.63% |
| LSTMRNN (baseline) | 108.26 | — | — |
| LSTMRNTN (proposed) | 96.97 | −11.29 | −10.42% |

GRURNTN reduced perplexity from 97.78 to 87.38, an absolute reduction of 10.4 and a 10.63% relative reduction over GRURNN; LSTMRNTN reduced perplexity from 108.26 to 96.97, an absolute reduction of 11.29 and a 10.42% relative reduction over LSTMRNN ([Tjandra et al., 2017](https://arxiv.org/abs/1706.02222)). The authors describe GRURNTN as the best model in this task, with a consistently lower PPL than the other models ([Tjandra et al., 2017](https://arxiv.org/abs/1706.02222)).

A nuance worth highlighting for objectivity: although LSTMRNTN's absolute gain (11.29 PPL) is numerically larger than GRURNTN's (10.40 PPL), this is partly because it started from a much weaker baseline. After training, LSTMRNTN's 96.97 only "closely resembles the baseline GRURNN" at 97.78, whereas GRURNTN at 87.38 moved far ahead of every model considered ([Tjandra et al., 2017](https://arxiv.org/abs/1706.02222)). In other words, the tensor modification was more transformative for the GRU backbone on this task, bringing the already-strong GRU baseline to the best result in the study.

## Comparison Against Published Results

The paper situates its results among prior published figures, reproduced below.

| Model | Test PPL (word) | Test BPC (character) |
|---|---|---|
| N-Gram | 141 | — |
| RNNLM (w/o dynamic evaluation) | 124.7 | — |
| RNNLM (w/ dynamic evaluation) | 123.2 | — |
| SCRNN | 115 | — |
| sRNN | 110.0 | 1.41 |
| DOT(S)-RNN | 107.5 | 1.39 |
| NNLM | — | 1.57 |
| BPTT-RNN | — | 1.42 |
| HF-MRNN | — | 1.24 |
| GRURNN (baseline) | 97.78 | 1.39 |
| LSTMRNN (baseline) | 108.26 | 1.37 |
| GRURNTN (proposed) | 87.38 | 1.33 |
| LSTMRNTN (proposed) | 96.97 | 1.34 |

(Adapted from [Tjandra et al., 2017](https://arxiv.org/abs/1706.02222).)

On the word-level task, GRURNTN's 87.38 is lower than every listed system, including sRNN (110.0) and DOT(S)-RNN (107.5), and the paper states it outperformed "all the baseline models as well as the other models by a large margin" ([Tjandra et al., 2017](https://arxiv.org/abs/1706.02222)). The authors caution, however, that their own baseline and proposed experiments did not use dynamic evaluation, whereas some published entries did — so those comparisons are not perfectly controlled ([Tjandra et al., 2017](https://arxiv.org/abs/1706.02222)).

On the character-level task, the picture is more qualified. GRURNTN's 1.33 beats the comparable sRNN (1.41) and DOT(S)-RNN (1.39), but several published figures are lower, including HF-MRNN at 1.24, an LSTMRNN variant with adaptive noise and dynamic evaluation at 1.26, and an LSTMRNN variant with adaptive noise (without dynamic evaluation) that also reaches 1.33, tying GRURNTN ([Tjandra et al., 2017](https://arxiv.org/abs/1706.02222)). This is a material caveat: at character level, the proposed architecture does not establish a new state of the art once externally regularized variants are included.

## Source Reliability and an Internal Discrepancy

Two source documents were provided. The primary source is the paper itself, which reports both a results table and an independently stated conclusion; these agree: Table II lists GRURNTN at 87.38 and the Conclusion states a 10.4 absolute / 10.63% relative PPL reduction over GRURNN ([Tjandra et al., 2017](https://arxiv.org/abs/1706.02222)). The character-level figures (0.06 / 4.32% and 0.03 / 2.22%) likewise appear in both the Results and Conclusion sections ([Tjandra et al., 2017](https://arxiv.org/abs/1706.02222)).

The second document, a third-party research note, agrees with the character-level figures and with the LSTMRNTN word-level figures (108.26 → 96.97; 11.29 absolute / 10.42% relative), but reports GRURNTN's word-level test PPL as 92.98, yielding 4.8 absolute / 4.91% relative improvement over GRURNN ([Third-party research note](https://arxiv.org/abs/1706.02222)). That figure contradicts the primary source's table and conclusion and is not corroborated anywhere in the paper.

| Claim | Primary source (paper) | Third-party note |
|---|---|---|
| GRURNTN word-level PPL | 87.38 (10.4 / 10.63%) | 92.98 (4.8 / 4.91%) |
| LSTMRNTN word-level PPL | 96.97 (11.29 / 10.42%) | 96.97 (11.29 / 10.42%) |
| GRURNTN character BPC | 1.33 (0.06 / 4.32%) | 1.33 (0.06 / 4.32%) |
| LSTMRNTN character BPC | 1.34 (0.03 / 2.22%) | 1.34 (0.03 / 2.22%) |

Given the internal consistency of the primary source and the fact that the note is secondary and provides no methodology for the 92.98 value, this report privileges the paper's figures. Readers relying on the note alone would underestimate the word-level gain by more than half.

## Interpretation of the Magnitude of Improvement

Three observations summarize the evidence. First, the direction of the effect is unanimous: all four baseline-to-proposed comparisons improved, across two tasks and two backbone architectures ([Tjandra et al., 2017](https://arxiv.org/abs/1706.02222)). Second, the magnitude is task-dependent: character-level relative gains of 2.22% and 4.32% contrast with word-level relative gains of 10.42% and 10.63% ([Tjandra et al., 2017](https://arxiv.org/abs/1706.02222)). Third, the gains are achieved under parameter matching, so they are not attributable to simply adding capacity — a point the authors emphasize by constraining baselines to comparable parameter counts ([Tjandra et al., 2017](https://arxiv.org/abs/1706.02222)).

The authors attribute the improvement to expressiveness rather than capacity: replacing first-degree dot-product interactions with second-degree polynomial (bilinear tensor) interactions allows the hidden layer to model more complex input–hidden relationships, and the tensor sliced weights are learned more directly from input and hidden-layer values ([Tjandra et al., 2017](https://arxiv.org/abs/1706.02222)). They also note that prior tensor-based models lacked gating, so their tensor parameters could not be fully exploited due to vanishing or exploding gradients — the combination of gating and tensor products is presented as the novel contribution ([Tjandra et al., 2017](https://arxiv.org/abs/1706.02222)).

## Limitations and Open Questions

Several limitations temper the conclusions. The evaluation is confined to a single corpus (PTB), so generalization to other domains is untested; the authors list speech recognition and video recognition as future work ([Tjandra et al., 2017](https://arxiv.org/abs/1706.02222)). Character-level results do not surpass all published systems, as noted above. The number of epochs, detailed learning-rate schedule, and convergence plots are described only qualitatively, with no variance or repeated-run statistics given, so the stability of small differences — for example, GRURNTN's 1.33 versus LSTMRNTN's 1.34 — cannot be assessed ([Tjandra et al., 2017](https://arxiv.org/abs/1706.02222)). Finally, the conflicting word-level GRURNTN number in the secondary note indicates some risk in how the results have been disseminated, even though the primary source is self-consistent.

## Conclusion

Expressed as direct answers to the query: relative to the previous models, GRURNTN achieved a 4.32% relative reduction in character-level BPC (1.39 → 1.33; 0.06 absolute) and a 10.63% relative reduction in word-level perplexity (97.78 → 87.38; 10.4 absolute) over GRURNN. LSTMRNTN achieved a 2.22% relative reduction in character-level BPC (1.37 → 1.34; 0.03 absolute) and a 10.42% relative reduction in word-level perplexity (108.26 → 96.97; 11.29 absolute) over LSTMRNN ([Tjandra et al., 2017](https://arxiv.org/abs/1706.02222)). The improvement is therefore best characterized as marginal-to-moderate on character-level modeling and clearly substantial, exceeding ten percent relative on both backbones, on word-level modeling — with all gains obtained under a parameter-matched comparison and with roughly one-third of the hidden units used by the baselines. GRURNTN is the stronger of the two proposals overall; LSTMRNTN's word-level gain, while large in absolute terms, primarily restores LSTM performance to the level of the unaugmented GRU baseline rather than surpassing it ([Tjandra et al., 2017](https://arxiv.org/abs/1706.02222)).

## References

Tjandra, A., Sakti, S., Manurung, R., Adriani, M., & Nakamura, S. (2017). *Gated recurrent neural tensor network* (arXiv:1706.02222). arXiv. https://arxiv.org/abs/1706.02222

Third-party research note: Gated recurrent neural tensor network (document_2.txt). (n.d.). [Unpublished research note]. https://arxiv.org/abs/1706.02222