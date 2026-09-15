# Quantifying the Performance Improvements of Gated Recurrent Neural Tensor Networks over Gated RNN Baselines

## Introduction

Recurrent Neural Networks (RNNs) are a foundational architecture for modeling temporal and sequential data, and they have been applied successfully in speech recognition, machine translation, and language modeling ([Tjandra et al., n.d.](document_1.txt)). However, standard gated RNNs such as the Long Short Term Memory (LSTM) RNN and the Gated Recurrent Unit (GRU) RNN rely on linear projection, addition, and a nonlinear activation to relate the current input to the previous hidden state, a transition that the authors characterize as "shallow" because no intermediate hidden layers exist for projecting the hidden states ([Tjandra et al., n.d.](document_1.txt)).

The paper under analysis, "Gated Recurrent Neural Tensor Network," introduces two new architectures that combine gating mechanisms with tensor products into a single model: the Gated Recurrent Unit Recurrent Neural Tensor Network (GRURNTN) and the Long-Short Term Memory Recurrent Neural Tensor Network (LSTMRNTN) ([Tjandra et al., n.d.](document_1.txt)). The central question addressed in this report is how much improvement these introduced models achieve relative to their corresponding previous baseline models, GRURNN and LSTMRNN, on word-level and character-level language modeling tasks. The evidence indicates that both proposed models outperform their baselines consistently, with relative improvements ranging from roughly 2.2% to 4.3% on character-level bits-per-character (BPC) and from roughly 4.9% to 10.6% on word-level perplexity (PPL), depending on which source figure is accepted for the GRURNTN word-level result ([Tjandra et al., n.d.](document_1.txt); [Third-party research note, n.d.](document_2.txt)).

## Experimental Setup and Fairness Controls

Understanding the magnitude of the reported improvements requires examining how the comparisons were constructed, because the authors explicitly constrained the baselines to have a similar number of parameters as the proposed models for a fair comparison ([Tjandra et al., n.d.](document_1.txt)). This is a critical methodological detail: it means the observed gains are attributable to the architectural innovation—the tensor product plus gating combination—rather than to a larger parameter budget.

Experiments were conducted on the PennTreeBank (PTB) corpus, a standard benchmark for statistical language modeling that is a subset of the WSJ corpus. The dataset was divided into a training set of 930,000 words (sections 0–20), a validation set of 74,000 words (sections 21–22), and a test set of 82,000 words (sections 23–24), with vocabulary limited to the 10,000 most common words ([Tjandra et al., n.d.](document_1.txt)). All models used AdaGrad optimization, mini-batches of 15 sentences, dropout regularization, gradient rescaling when the norm exceeded 5, and orthogonal weight initialization ([Tjandra et al., n.d.](document_1.txt)).

### Model Configuration and Parameter Budgets

| Task | Proposed Models (GRURNTN / LSTMRNTN) | Baseline GRURNN | Baseline LSTMRNN | Embedding Dim. | Dropout |
|---|---|---|---|---|---|
| Word-level | 256 hidden units | 860 hidden units | 740 hidden units | 128 | p = 0.5 (proposed); p = 0.6 (baseline) |
| Character-level | 256 hidden units | 820 hidden units | 600 hidden units | 32 | p = 0.25 |

*Source: ([Tjandra et al., n.d.](document_1.txt)).*

| Task | GRURNN / GRURNTN Parameters | LSTMRNN / LSTMRNTN Parameters |
|---|---|---|
| Word-level | ~12 million | ~13 million |
| Character-level | ~2.2 million | ~2.6 million |

*Source: ([Tjandra et al., n.d.](document_1.txt)).*

The baselines were deliberately given more hidden units (860 and 740 at the word level; 820 and 600 at the character level) so that their total free parameters would approximate those of the proposed 256-unit tensor models ([Tjandra et al., n.d.](document_1.txt)). This design strengthens the interpretation that the improvement stems from the tensor product interaction, which the authors describe as increasing model expressiveness through "second-degree polynomial interactions" compared to the "first-degree polynomial interactions" of standard dot products followed by addition ([Tjandra et al., n.d.](document_1.txt)).

## Character-Level Language Modeling Results

On the character-level task, both proposed models reduced test BPC relative to their respective baselines. The paper reports that GRURNTN reduced BPC from 1.39 to 1.33, an absolute reduction of 0.06 and a relative reduction of 4.32%, while LSTMRNTN reduced BPC from 1.37 to 1.34, an absolute reduction of 0.03 and a relative reduction of 2.22% ([Tjandra et al., n.d.](document_1.txt)). The independent third-party research note reproduces these same figures exactly ([Third-party research note, n.d.](document_2.txt)), which increases confidence in their reliability since two sources agree.

| Proposed Model | Baseline BPC | Proposed BPC | Absolute Reduction | Relative Reduction |
|---|---|---|---|---|
| GRURNTN (vs. GRURNN) | 1.39 | 1.33 | 0.06 | 4.32% |
| LSTMRNTN (vs. LSTMRNN) | 1.37 | 1.34 | 0.03 | 2.22% |

*Sources: ([Tjandra et al., n.d.](document_1.txt); [Third-party research note, n.d.](document_2.txt)).*

Beyond the headline comparison, the paper emphasizes that both proposed models produced lower BPC than the baseline models "from the first epoch to the last epoch," indicating that the advantage is not merely a final-epoch artifact but a persistent property of the training trajectory ([Tjandra et al., n.d.](document_1.txt)). The paper also notes that GRURNTN slightly outperformed LSTMRNTN on this task, and that both proposed models outperformed all baseline models ([Tjandra et al., n.d.](document_1.txt)).

Placing these results in a broader context, Table I of the paper reports several published character-level results: NNLM at 1.57 BPC, BPTT-RNN at 1.42, HF-MRNN at 1.24/1.41, sRNN at 1.39, DOT(S)-RNN at 1.37, and an LSTM variant with adaptive noise at 1.33 ([Tjandra et al., n.d.](document_1.txt)). The proposed GRURNTN's 1.33 BPC therefore matches the best published result in that table among models without dynamic evaluation, while LSTMRNTN's 1.34 sits just above it. This contextual placement suggests the tensor-gating combination delivers competitive rather than merely internally-consistent gains.

## Word-Level Language Modeling Results

On the word-level task, the improvement is larger, though the two sources diverge on one figure. The primary paper reports that GRURNTN reduced perplexity from 97.78 to 87.38, an absolute reduction of 10.4 and a relative reduction of 10.63%, over the baseline GRURNN, and that LSTMRNTN reduced perplexity from 108.26 to 96.97, an absolute reduction of 11.29 and a relative reduction of 10.42%, over the baseline LSTMRNN ([Tjandra et al., n.d.](document_1.txt)). The third-party research note, by contrast, states that GRURNTN reduced PPL from 97.78 to 92.98, which it computes as 4.8 absolute and 4.91% relative ([Third-party research note, n.d.](document_2.txt)). The two sources agree on the LSTMRNTN figures.

| Proposed Model | Baseline PPL | Proposed PPL | Absolute Reduction | Relative Reduction | Source |
|---|---|---|---|---|---|
| GRURNTN (vs. GRURNN) | 97.78 | 87.38 | 10.40 | 10.63% | Primary paper |
| GRURNTN (vs. GRURNN) | 97.78 | 92.98 | 4.80 | 4.91% | Third-party note |
| LSTMRNTN (vs. LSTMRNN) | 108.26 | 96.97 | 11.29 | 10.42% | Both sources |

*Sources: ([Tjandra et al., n.d.](document_1.txt); [Third-party research note, n.d.](document_2.txt)).*

Given the instruction to prioritize reliability and to favor primary over secondary sources, the figure of 87.38 and the 10.63% relative reduction should be treated as the authoritative GRURNTN word-level result, since it appears in the original paper's results and conclusion sections. It is worth stating explicitly that the numerical disagreement is confined to this single cell of the results; all other reported comparisons align across both sources. The discrepancy does not undermine the overall conclusion that both proposed models outperform their baselines, because even the more conservative third-party figure (4.91% relative) still represents a meaningful improvement.

The paper also provides an important qualitative finding about the relative standing of the models: although LSTMRNTN improved upon LSTMRNN, its performance "closely resembles the baseline GRURNN" (96.97 versus 97.78 PPL), whereas GRURNTN "outperformed all the baseline models as well as the other models by a large margin" ([Tjandra et al., n.d.](document_1.txt)). In other words, the GRU-based tensor network was the strongest model in the word-level task, producing a consistently lower PPL than the other three models ([Tjandra et al., n.d.](document_1.txt)). For external context, Table II reports N-Gram at 141 PPL, RNNLM without dynamic evaluation at 124.7, RNNLM with dynamic evaluation at 123.2, SCRNN at 115, sRNN at 110.0, and DOT(S)-RNN at 107.5 ([Tjandra et al., n.d.](document_1.txt)). The proposed GRURNTN at 87.38 and LSTMRNTN at 96.97 both sit well below these published baselines, reinforcing the significance of the gains.

## Convergence Behavior and Training Dynamics

The improvements are not limited to final test scores. In the word-level experiment, GRURNN made faster initial progress than LSTMRNN, and GRURNTN's progress was also better than LSTMRNTN's; the best model overall was GRURNTN, which maintained a consistently lower PPL across validation epochs ([Tjandra et al., n.d.](document_1.txt)). At the character level, GRURNN progressed faster than LSTMRNN but eventually converged to a better BPC, while GRURNTN made "faster and quicker progress than LSTMRNTN" and converged to a similar final BPC ([Tjandra et al., n.d.](document_1.txt)). This pattern is consistent with the authors' hypothesis that the tensor product provides a more direct and expressive interaction between input and hidden layers, which the gradient derivations suggest allows each tensor weight slice to be learned "more directly from their input and hidden layer values" than standard addition operations permit ([Tjandra et al., n.d.](document_1.txt)).

## Interpretation and Magnitude of the Improvements

Taken together, the evidence supports a graded conclusion about the size of the improvement. On character-level modeling, the gains are modest in absolute terms (0.03–0.06 BPC) but consistent in direction, and the relative reductions of 2.22% and 4.32% are non-trivial for a task where published results cluster tightly between roughly 1.24 and 1.57 BPC ([Tjandra et al., n.d.](document_1.txt)). On word-level modeling, the relative reductions are considerably larger—10.42% for LSTMRNTN and 10.63% for GRURNTN per the primary source—which suggests that the tensor product's richer second-degree interactions pay off more substantially when the prediction task requires modeling longer-range dependencies across words ([Tjandra et al., n.d.](document_1.txt)).

A further observation is the asymmetry between the two proposed models. GRURNTN delivered the largest and most consistent gains, outperforming all baselines and the other proposed model on both tasks, while LSTMRNTN delivered a smaller character-level gain (2.22%) and, despite a large relative word-level gain (10.42%), only reached parity with the GRURNN baseline ([Tjandra et al., n.d.](document_1.txt)). This nuance matters for interpretation: the LSTMRNTN improvement over its own baseline is real and sizeable, but it does not make LSTMRNTN the strongest model overall.

## Limitations and Caveats

Several caveats should temper strong claims. First, the discrepancy between the primary paper and the third-party note on the GRURNTN word-level result means that the exact magnitude of that particular gain is uncertain, even though its direction is not ([Tjandra et al., n.d.](document_1.txt); [Third-party research note, n.d.](document_2.txt)). Second, the evidence comes from a single corpus (PTB) and two task variants, with no reported statistical significance testing, confidence intervals, or multiple-seed runs, so the robustness of the improvements across corpora is untested. Third, the parameter-matching is approximate: the baselines were allocated roughly 12–13 million parameters at the word level versus the proposed models' corresponding budgets, so "similar" rather than "identical" is the accurate characterization ([Tjandra et al., n.d.](document_1.txt)). Fourth, the paper itself frames the contribution as a combination of two previously separate ideas—gating and tensor products—and notes that to the authors' knowledge, none of the prior work combined them into a single architecture, meaning the improvements cannot easily be decomposed into the separate contributions of gating and tensoring ([Tjandra et al., n.d.](document_1.txt)).

## Conclusion

The answer to the question of how much improvement the introduced models achieve relative to previous models is as follows. On character-level language modeling, GRURNTN improved BPC by 0.06 absolute and 4.32% relative over GRURNN (1.39 to 1.33), and LSTMRNTN improved BPC by 0.03 absolute and 2.22% relative over LSTMRNN (1.37 to 1.34), with both figures corroborated by two independent sources ([Tjandra et al., n.d.](document_1.txt); [Third-party research note, n.d.](document_2.txt)). On word-level language modeling, LSTMRNTN improved PPL by 11.29 absolute and 10.42% relative over LSTMRNN (108.26 to 96.97), while GRURNTN improved PPL over GRURNN by either 10.40 absolute and 10.63% relative (97.78 to 87.38, per the primary paper) or 4.80 absolute and 4.91% relative (97.78 to 92.98, per the third-party note) ([Tjandra et al., n.d.](document_1.txt); [Third-party research note, n.d.](document_2.txt)). Across both tasks, the gains were achieved with a similar number of free parameters and were observable from the earliest epochs, and GRURNTN consistently emerged as the strongest of the four models evaluated. The most defensible summary is that the tensor-gating combination yields consistent, practically meaningful improvements—roughly 2–5% relative on character-level BPC and roughly 5–11% relative on word-level PPL—rather than dramatic gains, with the primary-source figures representing the more reliable estimate.

## References

Tjandra, A., Sakti, S., Manurung, R., Adriani, M., & Nakamura, S. (n.d.). *Gated Recurrent Neural Tensor Network* [document_1.txt]. ([link](document_1.txt))

Third-party research note: Gated Recurrent Neural Tensor Network (n.d.) [document_2.txt]. ([link](document_2.txt))