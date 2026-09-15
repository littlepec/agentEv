# Improvement Achieved by Gated Recurrent Neural Tensor Networks over Prior Recurrent Language Models

## Introduction

The Gated Recurrent Neural Tensor Network paper introduces two hybrid recurrent architectures — the Gated Recurrent Unit Recurrent Neural Tensor Network (GRURNTN) and the Long Short-Term Memory Recurrent Neural Tensor Network (LSTMRNTN) — and evaluates them against two conventional gated recurrent baselines, the Gated Recurrent Unit RNN (GRURNN) and the Long Short-Term Memory RNN (LSTMRNN) ([Tjandra et al., 2015](document_1.txt)). The central question addressed in this report is how much improvement the introduced models actually achieve relative to those previous models. That question can be answered quantitatively from the reported character-level and word-level language modeling results on the Penn TreeBank (PTB) corpus, and qualitatively from the convergence behavior, parameter counts, and comparison against other published systems. The evidence indicates that both proposed models produce consistent but asymmetric gains: the tensor-product augmentation helps the GRU baseline more than the LSTM baseline on the character-level task, and both architectures improve substantially on the word-level task, although the exact size of the GRU-based word-level gain is reported inconsistently between the primary paper and a third-party research note ([Third-party research note, n.d.](document_2.txt)).

## Background: What Was Proposed and What It Was Compared Against

The proposed architectures combine two ideas that had previously been developed separately in the literature: the gating mechanism used by LSTMRNN and GRURNN to learn long-term dependencies, and tensor-product (bilinear) interactions that allow hidden states to be represented by more expressive, second-degree polynomial operations rather than the linear projection plus addition used in standard RNNs ([Tjandra et al., 2015](document_1.txt)). In GRURNTN, the tensor product is applied between the current input and the previous hidden layer multiplied by the reset gate, in order to compute the candidate hidden layer; in LSTMRNTN, the tensor product is inserted into the computation of the candidate memory cell. An asymmetric bilinear form is used to reduce the parameter cost relative to the original neural tensor network formulation ([Tjandra et al., 2015](document_1.txt)).

The comparison target of interest is therefore the corresponding gated baseline without the tensor product: GRURNTN against GRURNN, and LSTMRNTN against LSTMRNN. The paper reports results for both a character-level language modeling task, measured in bits-per-character (BPC), where a lower score is better, and a word-level language modeling task, measured in perplexity (PPL), where a lower score is also better ([Tjandra et al., 2015](document_1.txt)).

## Character-Level Language Modeling: Magnitude of Improvement

On the PTB character-level task, the GRU-based proposal delivered a larger reduction than the LSTM-based proposal. GRURNTN reduced test BPC from 1.39 to 1.33, an improvement of 0.06 absolute, or 4.32% relative, over GRURNN. LSTMRNTN reduced BPC from 1.37 to 1.34, an improvement of 0.03 absolute, or 2.22% relative, over LSTMRNN ([Third-party research note, n.d.](document_2.txt); [Tjandra et al., 2015](document_1.txt)).

**Table 1. Character-level language modeling on PTB test set (BPC; lower is better)**

| Model | Test BPC | Absolute change vs. own baseline | Relative change vs. own baseline |
|---|---|---|---|
| GRURNN (baseline) | 1.39 | — | — |
| LSTMRNN (baseline) | 1.37 | — | — |
| GRURNTN (proposed) | 1.33 | 0.06 | 4.32% |
| LSTMRNTN (proposed) | 1.34 | 0.03 | 2.22% |

*Source: ([Tjandra et al., 2015](document_1.txt); [Third-party research note, n.d.](document_2.txt)).*

Two observations are important here. First, the gains are directionally consistent: both tensor-augmented models beat their respective baselines, and the paper states that both proposed models produced lower BPC than the baselines from the first epoch to the last epoch on the validation set ([Tjandra et al., 2015](document_1.txt)). Second, the magnitude is modest in absolute terms — 0.06 BPC on a scale where competing systems differ by hundredths — even though the relative reduction of 4.32% is non-trivial.

Placed against other published systems on the same task, GRURNTN's 1.33 BPC outperformed NNLM (1.57), BPTT-RNN (1.42), HF-MRNN (1.41), sRNN (1.41), and DOT(S)-RNN (1.39), and also edged out both internal baselines ([Tjandra et al., 2015](document_1.txt)). However, it did not reach the 1.26 and 1.24 BPC reported for an LSTMRNN trained with adaptive noise regularization and dynamic evaluation, a system that used additional techniques not applied in this work ([Tjandra et al., 2015](document_1.txt)). The proposed models' advantage is therefore best characterized as an improvement over their own parameter-matched baselines and over several standard published systems, rather than a new state of the art on character-level PTB.

**Table 2. Character-level BPC versus published systems**

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
| LSTMRNN (adaptive noise, dynamic evaluation) | 1.26 / 1.24 |

*Source: ([Tjandra et al., 2015](document_1.txt)).*

## Word-Level Language Modeling: Magnitude of Improvement

On the PTB word-level task, both proposed models also improved on their baselines, and here the reported absolute gains are considerably larger in raw perplexity terms. LSTMRNTN reduced perplexity from 108.26 to 96.97, a reduction of 11.29 absolute points, or 10.42% relative, over LSTMRNN. Both the primary paper and the third-party note agree on this figure ([Tjandra et al., 2015](document_1.txt); [Third-party research note, n.d.](document_2.txt)). Notably, LSTMRNTN's final score of 96.97 brings it close to the GRURNN baseline's 97.78, meaning the tensor augmentation largely closes the gap between the LSTM baseline and the GRU baseline on this task ([Tjandra et al., 2015](document_1.txt)).

The GRU-based result is reported inconsistently. The primary paper's results table lists GRURNTN at 87.38 PPL and its conclusion states a reduction of 10.4 absolute points, or 10.63% relative, over the GRURNN baseline of 97.78 ([Tjandra et al., 2015](document_1.txt)). The third-party research note, by contrast, states that GRURNTN reduced PPL from 97.78 to 92.98, a reduction of 4.8 absolute points, or 4.91% relative ([Third-party research note, n.d.](document_2.txt)). Both pairs of numbers are internally consistent — 97.78 − 87.38 = 10.40, and 10.40 / 97.78 = 10.63%; 97.78 − 92.98 = 4.80, and 4.80 / 97.78 = 4.91% — but they cannot both be correct.

**Table 3. Word-level language modeling on PTB test set (PPL; lower is better)**

| Model | Test PPL | Absolute change vs. own baseline | Relative change vs. own baseline |
|---|---|---|---|
| GRURNN (baseline) | 97.78 | — | — |
| LSTMRNN (baseline) | 108.26 | — | — |
| GRURNTN (proposed), primary paper | 87.38 | 10.40 | 10.63% |
| GRURNTN (proposed), third-party note | 92.98 | 4.80 | 4.91% |
| LSTMRNTN (proposed) | 96.97 | 11.29 | 10.42% |

*Source: ([Tjandra et al., 2015](document_1.txt); [Third-party research note, n.d.](document_2.txt)).*

Because the primary paper reports both the tabulated value (87.38) and an arithmetic reduction (10.4 absolute / 10.63% relative) that are mutually consistent, the more probable value for GRURNTN is 87.38 PPL, with the 92.98 figure appearing only in the secondary note. Either way, the qualitative conclusion is the same: GRURNTN was the strongest model in the paper's word-level comparison and outperformed all baselines "by a large margin" ([Tjandra et al., 2015](document_1.txt)).

Against other published systems, both proposed models sit at the top of the reported comparison set. The published figures cited in the paper include N-Gram (141), RNNLM without dynamic evaluation (124.7), RNNLM with dynamic evaluation (123.2), SCRNN (115), sRNN (110.0), and DOT(S)-RNN (107.5), all of which are worse than GRURNTN (87.38) and LSTMRNTN (96.97) ([Tjandra et al., 2015](document_1.txt)).

**Table 4. Word-level PPL versus published systems**

| Model | Test PPL |
|---|---|
| N-Gram | 141 |
| RNNLM (without dynamic evaluation) | 124.7 |
| RNNLM (with dynamic evaluation) | 123.2 |
| SCRNN | 115 |
| sRNN | 110.0 |
| DOT(S)-RNN | 107.5 |
| LSTMRNN (baseline) | 108.26 |
| GRURNN (baseline) | 97.78 |
| LSTMRNTN (proposed) | 96.97 |
| GRURNTN (proposed) | 87.38 |

*Source: ([Tjandra et al., 2015](document_1.txt)).*

## Was the Comparison Fair? Parameter Counts and Training Setup

The improvements are reported under parameter-matched conditions, which strengthens their interpretation. The paper states that the baseline GRURNN was constrained to have a similar number of free parameters to GRURNTN, and the baseline LSTMRNN was likewise constrained relative to LSTMRNTN, in order to allow a fair comparison ([Tjandra et al., 2015](document_1.txt)). For the word-level task, the total number of free parameters was approximately 12 million for the GRU pair and approximately 13 million for the LSTM pair; for the character-level task, approximately 2.2 million for the GRU pair and approximately 2.6 million for the LSTM pair ([Tjandra et al., 2015](document_1.txt)).

**Table 5. Experimental configuration**

| Setting | Word-level | Character-level |
|---|---|---|
| Hidden units (GRURNTN / LSTMRNTN) | 256 | 256 |
| Hidden units (GRURNN) | 860 | 820 |
| Hidden units (LSTMRNN) | 740 | 600 |
| Embedding size | 128 (words) | 32 (characters) |
| Dropout probability | 0.5 (proposed), 0.6 (baseline) | 0.25 |
| Approx. parameters (GRU pair) | ~12 million | ~2.2 million |
| Approx. parameters (LSTM pair) | ~13 million | ~2.6 million |

*Source: ([Tjandra et al., 2015](document_1.txt)). Note that the character-level hidden-unit count for the LSTM baseline is stated inconsistently in the source text; the value above reflects the intended baseline configuration.*

Training used AdaGrad with mini-batch size of 15 sentences, a learning-rate decay factor of 0.5 when the development cost increased relative to the previous epoch, gradient rescaling when the norm exceeded 5, and orthogonal weight initialization ([Tjandra et al., 2015](document_1.txt)). Critically, the paper explicitly notes that neither the baselines nor the proposed models used dynamic evaluation, unlike some of the published systems they are compared against, which tempers direct comparison with the strongest cited results such as the 1.24 BPC LSTMRNN ([Tjandra et al., 2015](document_1.txt)).

## Convergence Behavior

Beyond final test scores, the validation curves indicate that the proposed models learned faster and better throughout training. For character-level modeling, GRURNTN made faster and quicker progress than LSTMRNTN and converged to a similar BPC in the final epoch, while both proposed models produced lower BPC than the baselines from the first epoch to the last; GRURNN progressed faster than LSTMRNN initially but eventually LSTMRNN converged to a better BPC ([Tjandra et al., 2015](document_1.txt)). For word-level modeling, GRURNTN's progress was better than LSTMRNTN's, and GRURNTN had a consistently lower PPL than all other models, making it the best model in that task ([Tjandra et al., 2015](document_1.txt)). The convergence evidence therefore supports the interpretation that the tensor product contributes a genuine representational advantage rather than merely a favorable final-epoch fluctuation.

## Overall Assessment

Taken together, the reported improvements are as follows. On character-level PTB, GRURNTN achieved 0.06 absolute / 4.32% relative BPC reduction over GRURNN, and LSTMRNTN achieved 0.03 absolute / 2.22% relative BPC reduction over LSTMRNN ([Third-party research note, n.d.](document_2.txt); [Tjandra et al., 2015](document_1.txt)). On word-level PTB, LSTMRNTN achieved 11.29 absolute / 10.42% relative PPL reduction over LSTMRNN, while GRURNTN achieved either 10.4 absolute / 10.63% relative (primary paper) or 4.8 absolute / 4.91% relative (secondary note) over GRURNN ([Tjandra et al., 2015](document_1.txt); [Third-party research note, n.d.](document_2.txt)).

The most defensible conclusions are the following. First, the improvement is consistent in direction across both tasks and both architecture families: every proposed model beat its own parameter-matched baseline, and this held on validation curves throughout training, not only at the endpoint ([Tjandra et al., 2015](document_1.txt)). Second, the improvement is markedly larger on the word-level task in relative terms (roughly 10%) than on the character-level task (roughly 2–4%), suggesting that the benefits of the bilinear interaction are more pronounced when the model must capture longer-range dependencies across words. Third, the GRU-based tensor variant was the stronger of the two proposals: GRURNTN outperformed LSTMRNTN on both the character-level task (1.33 vs. 1.34 BPC) and the word-level task (87.38 vs. 96.97 PPL), and it was the single best model in the paper's word-level comparison ([Tjandra et al., 2015](document_1.txt)).

Two caveats limit how far these conclusions can be generalized. The absolute character-level gains (0.03–0.06 BPC) are small, and the proposed models did not surpass the best cited character-level result, which used adaptive noise and dynamic evaluation rather than a tensor architecture ([Tjandra et al., 2015](document_1.txt)). Additionally, the conflicting word-level figures for GRURNTN between the primary paper and the secondary note mean that the precise magnitude of the GRU-based word-level gain should be treated with caution, even though the direction of the effect is not in dispute ([Third-party research note, n.d.](document_2.txt); [Tjandra et al., 2015](document_1.txt)). On balance, the introduced models deliver real, parameter-matched, and consistently reproduced improvements over the previous GRURNN and LSTMRNN models, with the largest relative benefit — approximately a 10% perplexity reduction — obtained on word-level language modeling.

## References

Third-party research note: Gated Recurrent Neural Tensor Network. (n.d.). [document_2.txt](document_2.txt).

Tjandra, A., Sakti, S., Manurung, R., Adriani, M., & Nakamura, S. (2015). Gated Recurrent Neural Tensor Network. [document_1.txt](document_1.txt).