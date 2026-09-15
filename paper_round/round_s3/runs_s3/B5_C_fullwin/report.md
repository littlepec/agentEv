# Quantifying the Improvement of Gated Recurrent Neural Tensor Networks over Standard Gated RNN Baselines

## Introduction

The Gated Recurrent Neural Tensor Network (RNTN) paper introduces two hybrid recurrent architectures that fuse the gating mechanism of modern recurrent networks with the bilinear tensor-product interaction previously used in recursive neural tensor networks ([Tjandra et al., 2017](https://arxiv.org/abs/1706.02222)). The central empirical question the paper sets out to answer is a simple one: when a tensor product is inserted into the candidate-state equations of a Gated Recurrent Unit (GRU) or a Long Short-Term Memory (LSTM) unit, how much does language-modeling performance actually improve relative to otherwise comparable gated baselines? The paper reports gains on two tasks — character-level language modeling measured in bits-per-character (BPC) and word-level language modeling measured in perplexity (PPL) — using the Penn Treebank (PTB) corpus. This report quantifies those gains, places them in context against both the paper's own baselines and previously published results, and evaluates how much of the reported improvement should be treated as robust evidence of a genuine architectural advantage.

## The Two Proposed Architectures and Their Baselines

The paper proposes two models. The first is the **Gated Recurrent Unit Recurrent Neural Tensor Network (GRURNTN)**, in which a tensor product is applied between the current input and the reset-gated previous hidden state when computing the candidate hidden layer ([Tjandra et al., 2017](https://arxiv.org/abs/1706.02222)). The second is the **Long Short-Term Memory Recurrent Neural Tensor Network (LSTMRNTN)**, in which the tensor product is applied between the current input and the previous hidden layer when computing the candidate memory cell ([Tjandra et al., 2017](https://arxiv.org/abs/1706.02222)). Both are compared against parameter-matched gated baselines: a plain GRU RNN (**GRURNN**) and a plain LSTM RNN (**LSTMRNN**) ([Tjandra et al., 2017](https://arxiv.org/abs/1706.02222)).

The motivation for the tensor product is explicitly stated: standard RNNs represent input–hidden interactions through linear projection plus addition followed by a nonlinearity, which the authors characterize as a first-degree polynomial interaction, whereas the tensor product introduces second-degree polynomial interactions and therefore greater expressiveness ([Tjandra et al., 2017](https://arxiv.org/abs/1706.02222)). The paper also introduces an asymmetric bilinear variant of the tensor formulation specifically to reduce the parameter count relative to the original neural tensor network formulation ([Tjandra et al., 2017](https://arxiv.org/abs/1706.02222)). The paper argues that combining tensors with gating is the key novelty, because prior tensor-based recurrent models lacked gating and therefore could not fully exploit tensor parameters due to vanishing or exploding gradients ([Tjandra et al., 2017](https://arxiv.org/abs/1706.02222)).

## Experimental Setup and Comparability of Baselines

Experiments use the preprocessed Penn Treebank corpus: sections 0–20 for training (930,000 words), sections 21–22 for validation (74,000 words), and sections 23–24 for testing (82,000 words), with vocabulary limited to the 10,000 most frequent words and all others mapped to an `<unk>` token ([Tjandra et al., 2017](https://arxiv.org/abs/1706.02222)). For word-level modeling, the proposed models use 256 hidden units, GRURNN uses 860, and LSTMRNN uses 740, all with 128-dimensional word embeddings; dropout is 0.5 for the proposed models and 0.6 for the baselines ([Tjandra et al., 2017](https://arxiv.org/abs/1706.02222)). For character-level modeling, the proposed models again use 256 hidden units, GRURNN uses 820, and the LSTM baseline uses 600, with 32-dimensional character embeddings and dropout of 0.25 ([Tjandra et al., 2017](https://arxiv.org/abs/1706.02222)).

Crucially, the authors state that they constrained the baseline GRURNN and LSTMRNN to have a similar number of free parameters as their tensor counterparts "for a fair comparison" ([Tjandra et al., 2017](https://arxiv.org/abs/1706.02222)). Total parameter counts were approximately 12 million for GRURNN/GRURNTN and 13 million for LSTMRNN/LSTMRNTN on the word-level task, and approximately 2.2 million for GRURNN/GRURNTN and 2.6 million for LSTMRNN/LSTMRNTN on the character-level task ([Tjandra et al., 2017](https://arxiv.org/abs/1706.02222)). All models were trained with AdaGrad using mini-batches of 15 sentences, a 0.5 learning-rate decay on development-set cost regression, gradient rescaling when the gradient norm exceeded 5, and orthogonal weight initialization ([Tjandra et al., 2017](https://arxiv.org/abs/1706.02222)).

## Character-Level Language Modeling: Bits-Per-Character

On character-level language modeling, both proposed models improve on their matching baselines ([Tjandra et al., 2017](https://arxiv.org/abs/1706.02222)). The headline numbers are summarized below.

| Model | Test BPC | Absolute change vs. own baseline | Relative change vs. own baseline |
|---|---|---|---|
| NNLM | 1.57 | — | — |
| BPTT-RNN | 1.42 | — | — |
| HF-MRNN | 1.41 | — | — |
| sRNN | 1.41 | — | — |
| DOT(S)-RNN | 1.39 | — | — |
| GRURNN (baseline) | 1.39 | — | — |
| LSTMRNN (baseline) | 1.37 | — | — |
| LSTMRNN w/ adaptive noise, w/o dynamic eval | 1.26 | — | — |
| LSTMRNN w/ adaptive noise, w/ dynamic eval | 1.24 | — | — |
| **GRURNTN (proposed)** | **1.33** | **−0.06** | **−4.32%** |
| **LSTMRNTN (proposed)** | **1.34** | **−0.03** | **−2.22%** |

The GRURNTN model reduced test BPC from 1.39 to 1.33, an absolute reduction of 0.06 and a relative reduction of 4.32% over GRURNN ([Third-party research note, n.d.](document_2.txt)). The LSTMRNTN model reduced BPC from 1.37 to 1.34, an absolute reduction of 0.03 and a relative reduction of 2.22% over LSTMRNN ([Third-party research note, n.d.](document_2.txt)). In this task GRURNTN slightly outperformed LSTMRNTN (1.33 vs. 1.34), and the paper reports that both proposed models produced lower BPC than the baselines from the first epoch through the last ([Tjandra et al., 2017](https://arxiv.org/abs/1706.02222)). GRURNTN also reportedly converged faster and more smoothly than LSTMRNTN ([Tjandra et al., 2017](https://arxiv.org/abs/1706.02222)).

Two qualifications matter for an impartial reading. First, the 2.22% relative figure for LSTMRNTN does not reconcile exactly with the rounded values: 0.03/1.37 equals approximately 2.19%, so the stated 2.22% implies an unrounded absolute difference closer to 0.0304 BPC. This is a rounding artifact rather than a substantive error, but it illustrates that the character-level gains are small enough that rounding precision materially affects how they are stated. Second, the paper's claim that both proposed models "outperformed all of the baseline models" on character-level modeling holds for the models listed as baselines and for the older published results (DOT(S)-RNN at 1.39, sRNN and HF-MRNN at 1.41, BPTT-RNN at 1.42, NNLM at 1.57), but it does **not** hold against Graves' adaptively-noised LSTM results of 1.26 and 1.24, which were obtained with adaptive noise regularization and, in the stronger configuration, dynamic evaluation ([Tjandra et al., 2017](https://arxiv.org/abs/1706.02222)). Those 1.24–1.26 results are better than both proposed models, although the paper notes that its own experiments used neither adaptive noise nor dynamic evaluation ([Tjandra et al., 2017](https://arxiv.org/abs/1706.02222)).

There is also an apparent typographical inconsistency in the character-level configuration description, which lists "600" hidden units for "LSTMRNTN" rather than for LSTMRNN ([Tjandra et al., 2017](https://arxiv.org/abs/1706.02222)). Given that the paper elsewhere uses 256 hidden units for both proposed models in both tasks, this is almost certainly a transcription error in the baseline column, and it does not change the reported test scores.

## Word-Level Language Modeling: Perplexity

On word-level language modeling, the reported improvements are substantially larger in relative terms than on the character-level task.

| Model | Test PPL | Absolute change vs. own baseline | Relative change vs. own baseline |
|---|---|---|---|
| N-Gram | 141 | — | — |
| RNNLM (w/o dynamic eval) | 124.7 | — | — |
| RNNLM (w/ dynamic eval) | 123.2 | — | — |
| SCRNN | 115 | — | — |
| sRNN | 110.0 | — | — |
| DOT(S)-RNN | 107.5 | — | — |
| GRURNN (baseline) | 97.78 | — | — |
| LSTMRNN (baseline) | 108.26 | — | — |
| **GRURNTN (proposed)** | **87.38** | **−10.40** | **−10.63%** |
| **LSTMRNTN (proposed)** | **96.97** | **−11.29** | **−10.42%** |

GRURNTN reduced test perplexity from 97.78 to 87.38, an absolute reduction of 10.4 and a relative reduction of 10.63% over GRURNN ([Third-party research note, n.d.](document_2.txt)). LSTMRNTN reduced perplexity from 108.26 to 96.97, an absolute reduction of 11.29 and a relative reduction of 10.42% over LSTMRNN ([Third-party research note, n.d.](document_2.txt)). Notably, LSTMRNTN's final perplexity of 96.97 actually edges just past the GRURNN baseline of 97.78, meaning that adding the tensor product to the weaker LSTM baseline brought it up to roughly the level of the plain GRU baseline ([Tjandra et al., 2017](https://arxiv.org/abs/1706.02222)). The authors acknowledge this explicitly, stating that LSTMRNTN's performance "closely resembles the baseline GRURNN," while GRURNTN was the best model in the task with a consistently lower PPL than all others ([Tjandra et al., 2017](https://arxiv.org/abs/1706.02222)).

Against the broader published set, GRURNTN's 87.38 is far ahead of the next-best tabulated result, DOT(S)-RNN at 107.5, and even further ahead of sRNN (110.0), SCRNN (115), and the dynamic-evaluation RNNLM (123.2) ([Tjandra et al., 2017](https://arxiv.org/abs/1706.02222)). That said, those published numbers come from earlier work with different training regimes and model sizes, so the cross-paper gap should be read as indicative rather than as a controlled comparison. The internally controlled comparison — the parameter-matched GRU and LSTM baselines — remains the strongest evidence, and there the gain is roughly a one-tenth relative reduction in perplexity for both proposed models.

## Synthesis: How Large Is the Improvement?

The paper's own conclusion states the headline numbers compactly: on character-level modeling, GRURNTN achieved a 0.06 absolute (4.32% relative) BPC reduction over GRURNN and LSTMRNTN achieved a 0.03 absolute (2.22% relative) BPC reduction over LSTMRNN; on word-level modeling, GRURNTN achieved a 10.4 absolute (10.63% relative) PPL reduction over GRURNN and LSTMRNTN achieved an 11.29 absolute (10.42% relative) PPL reduction over LSTMRNN ([Tjandra et al., 2017](https://arxiv.org/abs/1706.02222)). These figures are corroborated independently by the third-party research note, which reports the same absolute and relative deltas ([Third-party research note, n.d.](document_2.txt)).

Three patterns emerge from these numbers. First, the **word-level gains are consistently about an order of magnitude larger in relative terms** than the character-level gains: roughly 10.4–10.6% relative on PPL versus 2.2–4.3% relative on BPC. Second, **GRURNTN is the stronger of the two proposed models on both tasks** (1.33 vs. 1.34 BPC; 87.38 vs. 96.97 PPL), which is consistent with the paper's observation that GRURNN also made faster progress than LSTMRNN in both experiments ([Tjandra et al., 2017](https://arxiv.org/abs/1706.02222)). Third, the **LSTM-based variant benefits more in absolute terms on the word-level task** (11.29 PPL reduction) than the GRU-based variant (10.4 PPL reduction), even though the GRU-based variant ends at a better absolute score; this is because LSTMRNN started from a much weaker baseline of 108.26 ([Tjandra et al., 2017](https://arxiv.org/abs/1706.02222)).

My assessment is that the reported improvements constitute a genuine but moderate architectural effect. The tensors add only a modest number of parameters at the same nominal parameter budget (approximately 12 million vs. 13 million for the LSTM pair, and 2.2 million vs. 2.6 million for the character-level pair), and the baselines were deliberately widened — 860 and 740 hidden units versus 256 for the proposed models — so the gains cannot be attributed simply to greater capacity ([Tjandra et al., 2017](https://arxiv.org/abs/1706.02222)). At the same time, the evidence base is narrow: a single corpus, a single reported test run per model, no variance estimates or significance testing, and no ablation isolating the tensor product from the asymmetric bilinear reformulation or the dropout difference (0.5 for proposed models vs. 0.6 for baselines on the word-level task) ([Tjandra et al., 2017](https://arxiv.org/abs/1706.02222)). The character-level result for LSTMRNTN — a 0.03 BPC improvement, or roughly 0.03 bits per character — is small enough that it should be regarded as suggestive rather than decisive.

## Comparison with the Broader Literature

The paper positions its contribution against earlier attempts to enrich RNN hidden-state interactions. Pascanu et al. added nonlinear transition layers and shortcut connections, but still used linear projection plus addition; Gated Feedback RNNs added connections from all stacked hidden layers of previous time steps, again without tensor interactions; Irsoy and Cardie proposed a tensor product between input and hidden layers without gating; and Sutskever et al.'s multiplicative RNN used tensor weights but selected a slice and then fell back to linear projection plus addition ([Tjandra et al., 2017](https://arxiv.org/abs/1706.02222)). The paper's stated claim to novelty is that no prior work combined gating with tensor products in a single recurrent architecture ([Tjandra et al., 2017](https://arxiv.org/abs/1706.02222)). On the evidence presented, that claim is credible, and the reported gains relative to gated baselines are consistent with the argument that gating is what allows tensor parameters to be trained effectively.

## Limitations and Future Directions

The authors themselves scope the work as an initial investigation and outline three extensions: combining the tensor RNTN models with stacked RNN architectures such as Gated Feedback RNNs, exploring alternative tensor operations, and applying the models to other temporal and sequential tasks including speech recognition and video recognition ([Tjandra et al., 2017](https://arxiv.org/abs/1706.02222)). Until those extensions are validated, the practical takeaway is that the tensor-product modification delivered roughly a 10% relative perplexity reduction on word-level PTB modeling and a smaller 2–4% relative bits-per-character reduction on character-level PTB modeling, at approximately comparable parameter counts, with GRURNTN being the more effective of the two proposed variants.

## Conclusion

The answer to the question of how much improvement the introduced models achieve is precise and can be stated in the paper's own terms. **GRURNTN improves over GRURNN by 0.06 absolute BPC (4.32% relative) on character-level modeling and by 10.4 absolute PPL (10.63% relative) on word-level modeling. LSTMRNTN improves over LSTMRNN by 0.03 absolute BPC (2.22% relative) on character-level modeling and by 11.29 absolute PPL (10.42% relative) on word-level modeling** ([Tjandra et al., 2017](https://arxiv.org/abs/1706.02222); [Third-party research note, n.d.](document_2.txt)). Both proposed models beat their parameter-matched baselines on both tasks, and GRURNTN was the single best model in both experiments. The word-level gains, at roughly one-tenth relative perplexity reduction, are the more convincing result; the character-level gains, particularly the 2.22% relative reduction for LSTMRNTN, are marginal and sit behind stronger published LSTM results that used adaptive noise and dynamic evaluation. The contribution is therefore best characterized as a real, reproducible-looking improvement of moderate magnitude on one benchmark corpus, with the strongest case being the consistent direction of the effect across two tasks and two gated base architectures rather than the size of any individual number.

## References

Tjandra, A., Sakti, S., Manurung, R., Adriani, M., & Nakamura, S. (2017). *Gated Recurrent Neural Tensor Network* [document_1.txt]. arXiv:1706.02222. https://arxiv.org/abs/1706.02222

Third-party research note: Gated Recurrent Neural Tensor Network [document_2.txt]. (n.d.).