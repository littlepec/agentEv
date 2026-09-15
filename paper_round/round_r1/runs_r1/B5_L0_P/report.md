# Quantifying the Improvement of Gated Recurrent Neural Tensor Networks over Gated RNN Baselines

## Introduction

The paper "Gated Recurrent Neural Tensor Network" introduces two hybrid recurrent architectures that fuse the gating mechanism of gated recurrent networks with the tensor-product hidden-state interaction previously exploited in recursive neural tensor networks (Tjandra et al., 2017). The two proposed models are the Long Short-Term Memory Recurrent Neural Tensor Network (LSTMRNTN) and the Gated Recurrent Unit Recurrent Neural Tensor Network (GRURNTN). Both are evaluated against matched-parameter baselines, namely a gated recurrent unit network (GRURNN) and a long short-term memory network (LSTMRNN), on the Penn Treebank (PTB) corpus under two language modeling regimes: word-level prediction measured by perplexity (PPL) and character-level prediction measured by bits-per-character (BPC) (Tjandra et al., 2017).

This report answers the question of how much improvement the introduced models achieve relative to previous models. It does so by (a) summarizing the reported absolute and relative gains, (b) situating those gains against published reference numbers on the same benchmark, (c) assessing the reliability of the available sources, including one internal discrepancy, and (d) identifying the methodological limits that constrain how strongly the results should be interpreted.

## Experimental Setup That Defines the Comparison

Before stating the magnitude of improvement, it matters how the comparison was constructed. The authors deliberately constrained the baseline models to have a similar number of free parameters to the tensor variants, so that gains could be attributed to architectural design rather than to raw capacity (Tjandra et al., 2017). For the word-level task, GRURNN and GRURNTN used approximately 12 million parameters, while LSTMRNN and LSTMRNTN used approximately 13 million; hidden-layer sizes were adjusted accordingly (256 units for the proposed models, 860 for GRURNN, and 740 for LSTMRNN) with 128-dimensional word embeddings (Tjandra et al., 2017). For the character-level task, GRURNN and GRURNTN used about 2.2 million parameters and LSTMRNN and LSTMRNTN about 2.6 million, with 256 hidden units for the proposed models, 820 for GRURNN, 600 for LSTMRNN, and 32-dimensional character embeddings (Tjandra et al., 2017).

All models were trained with AdaGrad using mini-batches of 15 sentences, a learning-rate decay of 0.5 triggered when development-set cost increased, gradient rescaling when the norm exceeded 5, and orthogonal weight initialization (Tjandra et al., 2017). Dropout probabilities differed slightly between proposed and baseline models: 0.5 versus 0.6 at the word level, and 0.25 uniformly at the character level (Tjandra et al., 2017). The matching of parameter counts is a genuine methodological strength because it isolates the effect of the tensor-product operation; the differing dropout rates are a minor confound worth noting.

## Character-Level Language Modeling: Improvements in Bits-Per-Character

On the PTB test set, the proposed models reduced BPC relative to their direct baselines, and the improvements are consistent across the two model families.

| Model | Test BPC | Source |
|---|---|---|
| GRURNN (baseline) | 1.39 | (Tjandra et al., 2017) |
| GRURNTN (proposed) | 1.33 | (Tjandra et al., 2017) |
| LSTMRNN (baseline) | 1.37 | (Tjandra et al., 2017) |
| LSTMRNTN (proposed) | 1.34 | (Tjandra et al., 2017) |

GRURNTN reduced BPC from 1.39 to 1.33, an absolute reduction of 0.06 and a relative reduction of 4.32% over GRURNN (Tjandra et al., 2017). LSTMRNTN reduced BPC from 1.37 to 1.34, an absolute reduction of 0.03 and a relative reduction of 2.22% over LSTMRNN (Tjandra et al., 2017). The paper reports that both proposed models produced lower BPC than the baselines from the first epoch through the last, indicating that the advantage was not merely a final-epoch artifact but a persistent gap during training (Tjandra et al., 2017).

Two cross-family observations are also informative. GRURNTN (1.33) outperformed the LSTMRNN baseline (1.37) by 0.04 BPC, or roughly 2.92% relative, and LSTMRNTN (1.34) outperformed the GRURNN baseline (1.39) by 0.05 BPC, or approximately 3.60% relative. In other words, the tensor-augmented variants were strong enough to overcome the architectural disadvantage of their weaker parent family. The paper itself notes that GRURNTN slightly outperformed LSTMRNTN on this task (Tjandra et al., 2017).

## Word-Level Language Modeling: Improvements in Perplexity

The word-level results show considerably larger gains than the character-level results, which is the more practically significant finding.

| Model | Test PPL | Source |
|---|---|---|
| GRURNN (baseline) | 97.78 | (Tjandra et al., 2017) |
| GRURNTN (proposed) | 87.38 | (Tjandra et al., 2017) |
| LSTMRNN (baseline) | 108.26 | (Tjandra et al., 2017) |
| LSTMRNTN (proposed) | 96.97 | (Tjandra et al., 2017) |

GRURNTN reduced perplexity from 97.78 to 87.38, an absolute reduction of 10.40 and a relative reduction of 10.63% over GRURNN (Tjandra et al., 2017). LSTMRNTN reduced perplexity from 108.26 to 96.97, an absolute reduction of 11.29 and a relative reduction of 10.42% over LSTMRNN (Tjandra et al., 2017). Both relative gains land near the 10.5% mark, suggesting that the tensor-product interaction contributes a broadly consistent benefit in this setting regardless of which gating family it augments.

Cross-family comparisons again favor the tensor variants. GRURNTN (87.38) beat the LSTMRNN baseline (108.26) by 20.88 PPL, or about 19.29% relative, and LSTMRNTN (96.97) narrowly beat the GRURNN baseline (97.78) by 0.81 PPL, roughly 0.83% relative (Tjandra et al., 2017). The authors characterize GRURNTN as the best model in this task, maintaining a consistently lower PPL than all others, and describe LSTMRNTN as performing closely to the GRURNN baseline (Tjandra et al., 2017).

## Comparison Against Published Reference Results

The paper positions its numbers against prior published results on the same benchmark, which provides useful context for judging whether the gains are large in absolute terms.

### Character-level published results

Prior systems listed for character-level PTB include NNLM at 1.57, BPTT-RNN at 1.42, HF-MRNN at 1.41, sRNN at 1.41, and DOT(S)-RNN at 1.39 (Tjandra et al., 2017). Against DOT(S)-RNN, GRURNTN's 1.33 represents a 0.06 BPC improvement, or 4.32% relative. However, the same table reports an LSTMRNN with adaptive noise regularization at 1.26 and the same model with dynamic evaluation at 1.24 (Tjandra et al., 2017). Both figures are better than either proposed model. This is an important caveat: on character-level PTB, the proposed architectures improve on their own baselines but do not surpass the strongest previously published result, which relied on additional regularization and test-time adaptation techniques the authors did not use (Tjandra et al., 2017).

### Word-level published results

The word-level picture is more favorable. Prior results include N-Gram at 141, RNNLM without dynamic evaluation at 124.7, RNNLM with dynamic evaluation at 123.2, SCRNN at 115, sRNN at 110.0, and DOT(S)-RNN at 107.5 (Tjandra et al., 2017). GRURNTN's 87.38 improves on DOT(S)-RNN by 20.12 PPL, approximately 18.72% relative, and on sRNN by 22.62 PPL, roughly 20.56% relative. Relative to RNNLM with dynamic evaluation, the gap is 35.82 PPL, or about 29.07% relative. The paper states that GRURNTN outperformed all baseline models and other published models by a large margin on this task (Tjandra et al., 2017).

## Source Reliability and an Internal Discrepancy

Two documents are available. The first is the primary paper, whose abstract, results tables, and conclusion are internally consistent with one another: the word-level GRURNTN result appears as 87.38 in both Table II and the surrounding text, and the corresponding gain is stated as 10.4 absolute and 10.63% relative PPL (Tjandra et al., 2017). The second is a third-party research note that restates the same study but reports the GRURNTN word-level result as 92.98, yielding a gain of 4.8 absolute and 4.91% relative over GRURNN (Third-party research note). This figure conflicts with the primary source and with the primary source's own arithmetic. Because the primary paper is the original, internally consistent record, its value of 87.38 (10.4 absolute, 10.63% relative) should be treated as authoritative, and the 92.98 figure in the secondary note should be regarded as an error rather than an alternative finding.

Notably, the two sources agree exactly on both character-level comparisons (0.06 absolute / 4.32% relative for GRURNTN; 0.03 absolute / 2.22% relative for LSTMRNTN) and on the LSTMRNTN word-level comparison (11.29 absolute / 10.42% relative), which isolates the discrepancy to a single data point (Tjandra et al., 2017; Third-party research note).

## Interpretation and Limitations

My assessment, based on the evidence available, is that the reported improvements are real and directionally consistent but uneven in magnitude and weaker in evidentiary strength than the paper's language implies. Three considerations support this view.

First, the authors describe the results as "significantly" improved (Tjandra et al., 2017), yet no statistical significance testing, confidence intervals, or variance across multiple random seeds is reported anywhere in the available material. All figures appear to be single point estimates, so "significantly" should be read as a descriptive rather than an inferential claim.

Second, the magnitude of improvement is task-dependent. At the word level, a roughly 10.5% relative perplexity reduction over matched-parameter baselines is a substantive and practically meaningful gain, and GRURNTN's 87.38 exceeds every prior result listed. At the character level, the gains are markedly smaller, at 4.32% and 2.22% relative, and both proposed models remain behind previously published LSTMRNN variants using adaptive noise and dynamic evaluation (Tjandra et al., 2017). The character-level improvement is therefore best described as modest.

Third, the evidence rests on a single benchmark corpus, PTB, and a single task family, language modeling (Tjandra et al., 2017). The authors themselves identify speech recognition and video recognition as future work, meaning generalization beyond language modeling is untested (Tjandra et al., 2017). The paper's theoretical justification—that the tensor product raises input-to-hidden interaction from first-degree to second-degree polynomial expressiveness, implemented in an asymmetric bilinear form that reduces parameter count relative to the full neural tensor formulation—is coherent and plausible, but it is an explanation for why gains occur rather than independent evidence that they do (Tjandra et al., 2017).

A further nuance is that GRURNTN is the more consistently effective variant: it produced the largest word-level gain, tied for the best character-level score, and trained faster than LSTMRNTN in both experiments (Tjandra et al., 2017). Where a practitioner must choose one architecture from this work, GRURNTN is the better-supported option.

## Conclusion

Relative to directly matched-parameter baselines, GRURNTN improved character-level BPC by 0.06 absolute and 4.32% relative over GRURNN, and word-level PPL by 10.4 absolute and 10.63% relative over the same baseline (Tjandra et al., 2017). LSTMRNTN improved character-level BPC by 0.03 absolute and 2.22% relative over LSTMRNN, and word-level PPL by 11.29 absolute and 10.42% relative (Tjandra et al., 2017). Both tensor-augmented models also outperformed the opposite family's baseline in both tasks, and GRURNTN exceeded all previously published word-level results listed in the paper (Tjandra et al., 2017). The gains are therefore best characterized as substantial at the word level, modest at the character level, and confined in scope to the Penn Treebank language modeling setting without reported significance testing or multi-seed validation. A secondary source that quotes a smaller 4.8 absolute PPL gain for GRURNTN is inconsistent with the primary paper and should not be relied upon (Third-party research note; Tjandra et al., 2017).

## References

Third-party research note: Gated Recurrent Neural Tensor Network [document_2.txt](document_2.txt).

Tjandra, A., Sakti, S., Manurung, R., Adriani, M., & Nakamura, S. (2017). *Gated Recurrent Neural Tensor Network* (arXiv:1706.02222) [document_1.txt](https://arxiv.org/abs/1706.02222).