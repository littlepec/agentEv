# How Much Improvement Do the Introduced Models Achieve? A Detailed Assessment of the Gated Recurrent Neural Tensor Network

## Introduction

The paper *Gated Recurrent Neural Tensor Network* by Tjandra, Sakti, Manurung, Adriani, and Nakamura proposes two new recurrent neural network (RNN) architectures that fuse the gating mechanism of modern recurrent units with a tensor-product interaction between the current input and the previous hidden state ([Tjandra et al., document_1.txt](document_1.txt)). The two models are the **Long Short-Term Memory Recurrent Neural Tensor Network (LSTMRNTN)**, which inserts a tensor product into the candidate memory-cell equation of an LSTM, and the **Gated Recurrent Unit Recurrent Neural Tensor Network (GRURNTN)**, which inserts a tensor product into the candidate hidden-layer equation of a GRU ([Tjandra et al., document_1.txt](document_1.txt)). Both are evaluated on PennTreeBank (PTB) word-level and character-level language modeling against matched GRU and LSTM baselines, and the authors conclude that both models "significantly improved their performance compared to our baseline models" ([Tjandra et al., document_1.txt](document_1.txt)).

The purpose of this report is to quantify precisely how large that improvement is, to decompose it into absolute and relative terms across the two tasks, and to evaluate how credible the gains are given the experimental design. A third-party research note summarizing the same paper is also considered, but — as shown below — it disagrees with the primary source on one headline number, and the discrepancy must be resolved before any conclusion is drawn ([Third-party research note, document_2.txt](document_2.txt)).

## The Proposed Models and the Comparison Design

### What the tensor product changes

The paper's motivating argument is representational. In standard gated RNNs, the interaction between the current input and the previous hidden state is a first-degree (linear) projection followed by addition and a non-linearity; the authors characterize this transition as "shallow because no intermediate hidden layers exist for projecting the hidden states" ([Tjandra et al., document_1.txt](document_1.txt)). By replacing that interaction with a bilinear tensor product, the models capture "second-degree polynomial interactions" and each slice of the tensor weight is intended to capture a specific pattern between the two vectors ([Tjandra et al., document_1.txt](document_1.txt)).

In **GRURNTN**, the tensor operation is applied between the current input and the reset-gated previous hidden state when computing the candidate hidden layer, and the authors use an asymmetric bilinear form, \(W_{tsr}^{[1:d]} \in \mathbb{R}^{i\times d \times d}\), explicitly to reduce the number of parameters relative to the original neural tensor network formulation ([Tjandra et al., document_1.txt](document_1.txt)). In **LSTMRNTN**, the tensor operation is applied between the current input and the previous hidden layer to compute the candidate cell \(\tilde{c_t}\) ([Tjandra et al., document_1.txt](document_1.txt)).

### Baselines and controlled comparison

Critically, the comparison is a *controlled* one. The paper states that baseline GRURNN was constrained "to have a similar number of parameters as the GRURNTN model for a fair comparison," and the same constraint was applied to LSTMRNN relative to LSTMRNTN ([Tjandra et al., document_1.txt](document_1.txt)). The third-party note confirms that the proposed models "outperformed the baseline models with a similar number of parameters" in both tasks ([Third-party research note, document_2.txt](document_2.txt)).

To achieve parameter parity, the baselines were given far larger hidden layers than the tensor models:

| Setting | Hidden units (GRURNTN / LSTMRNTN) | Hidden units (GRURNN / LSTMRNN) | Embedding dim. |
|---|---|---|---|
| Word-level | 256 / 256 | 860 / 740 | 128 (all models) |
| Character-level | 256 / 256 | 820 / 600 | 32 (all models) |

Source: ([Tjandra et al., document_1.txt](document_1.txt)).

The paper reports roughly 12 million free parameters for the GRU family and 13 million for the LSTM family in the word-level task, and roughly 2.2 million (GRU family) versus 2.6 million (LSTM family) in the character-level task ([Tjandra et al., document_1.txt](document_1.txt)). This is an important interpretive point: the tensor models win with roughly one-third of the hidden units of their baselines, which the authors present as evidence that the extra parameters are better spent on tensor interactions than on width.

Training was identical across conditions in most respects: AdaGrad with mini-batches of 15 sentences, gradient rescaling when the norm exceeded 5 to avoid exploding gradients, orthogonal weight initialization, and a learning-rate decay factor of 0.5 when development-set cost increased ([Tjandra et al., document_1.txt](document_1.txt)). One asymmetry does exist in the word-level experiment: dropout was set to \(p=0.5\) for the proposed models but \(p=0.6\) for the baselines ([Tjandra et al., document_1.txt](document_1.txt)). For the character-level experiment, dropout was reported as \(p=0.25\) ([Tjandra et al., document_1.txt](document_1.txt)).

## Results on Character-Level Language Modeling

Character-level performance was measured in bits-per-character (BPC), where lower is better. The paper reports the following PTB test-set results ([Tjandra et al., document_1.txt](document_1.txt)):

| Model | Test BPC | Absolute change | Relative change |
|---|---|---|---|
| GRURNN (baseline) | 1.39 | — | — |
| **GRURNTN (proposed)** | **1.33** | **−0.06** | **−4.32 %** |
| LSTMRNN (baseline) | 1.37 | — | — |
| **LSTMRNTN (proposed)** | **1.34** | **−0.03** | **−2.22 %** |

The same figures are repeated verbatim in the conclusion: "GRURNTN obtained 0.06 absolute (4.32 % relative) BPC reduction over GRURNN, and LSTMRNTN obtained 0.03 absolute (2.22 % relative) BPC reduction over LSTMRNN" ([Tjandra et al., document_1.txt](document_1.txt)). The third-party research note reproduces identical numbers ([Third-party research note, document_2.txt](document_2.txt)).

Two further observations from the paper's own analysis are relevant. First, the learning-curve comparison on the validation set showed that "both proposed models produced lower BPC than our baseline models from the first epoch to the last epoch," meaning the advantage is present throughout training rather than only at convergence ([Tjandra et al., document_1.txt](document_1.txt)). Second, GRURNTN trained "faster and quicker" than LSTMRNTN and converged to a similar BPC in the final epoch, and "GRURNTN slightly outperformed LSTMRNTN" overall on the character-level task ([Tjandra et al., document_1.txt](document_1.txt)).

### Context against published baselines

The paper's Table I also lists published character-level results: NNLM at 1.57 BPC, BPTT-RNN at 1.42, HF-MRNN at 1.24, sRNN at 1.41, and DOT(S)-RNN at 1.37, alongside an adaptive-noise LSTM baseline that reached 1.33 without dynamic evaluation and 1.26 with dynamic evaluation ([Tjandra et al., document_1.txt](document_1.txt)). The authors explicitly note that their own experiments "did not use dynamic evaluation," so the 1.26 figure is not a like-for-like comparison ([Tjandra et al., document_1.txt](document_1.txt)). Within the non-dynamic-evaluation regime, GRURNTN's 1.33 is competitive with the strongest regularized LSTM baseline reported in the same table, but it is not a new state of the art in absolute terms.

## Results on Word-Level Language Modeling

Word-level performance was measured by perplexity (PPL), again with lower being better:

| Model | Test PPL | Absolute change | Relative change |
|---|---|---|---|
| GRURNN (baseline) | 97.78 | — | — |
| **GRURNTN (proposed)** | **87.38** | **−10.40** | **−10.63 %** |
| LSTMRNN (baseline) | 108.26 | — | — |
| **LSTMRNTN (proposed)** | **96.97** | **−11.29** | **−10.42 %** |

Source: ([Tjandra et al., document_1.txt](document_1.txt)).

The paper states this result in three mutually consistent places — the Section V-B narrative, Table II, and the conclusion — reporting that "GRURNTN reduced the perplexity from 97.78 to 87.38 (10.4 absolute / 10.63 % relative PPL) over the baseline GRURNN" and that "LSTMRNTN reduced the perplexity from 108.26 to 96.97 (11.29 absolute / 10.42 % relative PPL) over the baseline LSTMRNN" ([Tjandra et al., document_1.txt](document_1.txt)).

Two qualitative findings deserve emphasis. First, LSTMRNTN's improvement over LSTMRNN is by far the largest *relative correction of a weak baseline*: it lifts an underperforming LSTM (108.26) to a level close to the untuned GRU baseline, which the authors acknowledge when they write that LSTMRNTN's "performance closely resembles the baseline GRURNN. However, GRURNTN outperformed all the baseline models as well as the other models by a large margin" ([Tjandra et al., document_1.txt](document_1.txt)). Second, GRURNTN's absolute score of 87.38 is the best in the paper: it beats SCRNN (115), sRNN (110.0), DOT(S)-RNN (107.5), GRURNN (97.78), and LSTMRNTN (96.97), while RNNLM baselines with and without dynamic evaluation sit at 124.7 and 123.2 and N-Gram at 141 ([Tjandra et al., document_1.txt](document_1.txt)). The validation-set curves likewise showed GRURNTN "had a consistently lower PPL than the other models" ([Tjandra et al., document_1.txt](document_1.txt)).

## Resolving the Discrepancy Between the Two Sources

The third-party research note reports the character-level results identically to the primary paper, but it reports a *different* word-level result for GRURNTN: a reduction "from 97.78 to 92.98, which is 4.8 absolute / 4.91 % relative PPL" ([Third-party research note, document_2.txt](document_2.txt)). This conflicts with the primary source on all three quantities — endpoint (92.98 vs. 87.38), absolute change (4.8 vs. 10.4), and relative change (4.91 % vs. 10.63 %).

The discrepancy should be resolved in favour of the primary paper for three reasons. First, internal concordance: document_1 reports 87.38 and 10.63 % in its Section V-B narrative, its Table II entry, and its conclusion, giving three independent statements of the same value, whereas the note's 92.98 appears only once and is never supported by any table entry in the primary source ([Tjandra et al., document_1.txt](document_1.txt)). Second, internal arithmetic: 4.8/97.78 = 4.91 % confirms the note is self-consistent but does not corroborate the paper. Third, the note is described as a "Third-party research note" rather than the authors' own text, whereas document_1 is the paper itself, including its equations, training derivations, and reference list ([Third-party research note, document_2.txt](document_2.txt); [Tjandra et al., document_1.txt](document_1.txt)). Consequently, the defensible reading is that GRURNTN reduced word-level test perplexity by **10.40 absolute / 10.63 % relative**, not by 4.8 / 4.91 %. The discrepancy is nevertheless worth flagging, because it changes the headline story: under the note's figures, LSTMRNTN would be the stronger contributor on the word-level task by a wide margin, whereas under the paper's figures the two tensor models deliver nearly identical relative gains (10.63 % vs. 10.42 %).

## Interpretation, Caveats, and Overall Verdict

**Magnitude.** The improvements are real but modest in absolute terms on the character-level task — 0.06 BPC and 0.03 BPC, corresponding to 4.32 % and 2.22 % relative reductions — and substantial on the word-level task, near 10.5 % relative perplexity reduction for both models ([Tjandra et al., document_1.txt](document_1.txt)). A 10 % relative perplexity reduction with matched parameter counts is a meaningful result by the standards of PTB-era language modeling; a 2–4 % relative BPC reduction is smaller and, at 1.34 vs. 1.37 BPC, sits close to the rounding resolution of reported scores.

**Attribution.** Because baselines were matched on parameter count and trained with the same optimizer, batch size, gradient clipping, initialization, and learning-rate schedule, the comparison isolates the architectural change reasonably well ([Tjandra et al., document_1.txt](document_1.txt)). The word-level dropout asymmetry (\(p=0.5\) for the proposed models vs. \(p=0.6\) for baselines) is a genuine, if probably second-order, confound that the paper does not address ([Tjandra et al., document_1.txt](document_1.txt)). The hidden-size asymmetry also means the comparison is not "same architecture, bigger model" but "different parameterization at equal budget," which is exactly the comparison the authors intend but which means the gains cannot be attributed purely to the tensor operator without further ablation.

**Which model is better?** On the evidence presented, GRURNTN is the stronger model: it achieves the best test BPC (1.33) and the best test PPL (87.38) of all models evaluated by the authors, and it outperforms "all the baseline models as well as the other models by a large margin" on the word-level task ([Tjandra et al., document_1.txt](document_1.txt)). LSTMRNTN delivers the largest *improvement over its own baseline* in absolute perplexity (11.29) but lands behind GRURNTN in absolute score. My assessment, based on the reported numbers, is that the gating-plus-tensor combination is validated most convincingly for the GRU variant, and that the LSTM variant's gain is better described as repairing a weak baseline than as establishing a new best result.

**External validity.** The paper's own comparison set is dated: the strongest published character-level number cited (HF-MRNN, 1.24 BPC) is better than either proposed model, and the adaptive-noise LSTM with dynamic evaluation reaches 1.26 ([Tjandra et al., document_1.txt](document_1.txt)). The authors are careful to note they did not use dynamic evaluation, so the correct claim is that the proposed models beat their own matched baselines and many published PTB baselines, not that they are globally state of the art.

**Final verdict.** Measured against the models they were designed to replace, GRURNTN and LSTMRNTN deliver consistent, reproducible improvements: −0.06 BPC (4.32 %) and −10.40 PPL (10.63 %) for GRURNTN, and −0.03 BPC (2.22 %) and −11.29 PPL (10.42 %) for LSTMRNTN, with validation curves showing the advantage from the first training epoch onward ([Tjandra et al., document_1.txt](document_1.txt); [Third-party research note, document_2.txt](document_2.txt)). Whether those percentages constitute a "large" improvement depends on the axis: on the character-level axis they are small, on the word-level axis they are substantial and, given parameter-matched baselines, architecturally meaningful.

## References

Tjandra, A., Sakti, S., Manurung, R., Adriani, M., & Nakamura, S. (n.d.). *Gated recurrent neural tensor network* [document_1.txt]. ([document_1.txt](document_1.txt))

Third-party research note: Gated recurrent neural tensor network [document_2.txt]. (n.d.). ([document_2.txt](document_2.txt))