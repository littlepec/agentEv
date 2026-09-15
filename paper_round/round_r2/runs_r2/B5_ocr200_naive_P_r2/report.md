# How Much Improvement Do the Introduced Models Achieve? A Comparative Assessment of GRURNTN and LSTMRNTN Against Gated RNN Baselines

## Scope and Source Basis

This report answers the question of how much performance improvement the two introduced architectures—the Gated Recurrent Unit Recurrent Neural Tensor Network (GRURNTN) and the Long Short-Term Memory Recurrent Neural Tensor Network (LSTMRNTN)—deliver relative to the previous models against which they were benchmarked, namely the standard GRU RNN (GRURNN) and LSTM RNN (LSTMRNN). The evidence base consists of two documents: the primary research paper describing the architectures and experiments, and a third-party research note summarising that paper ([Tjandra et al., 2015](document_1.txt); [Third-party research note, n.d.](document_2.txt)).

Because the two documents disagree on one headline number, this report prioritises the primary source (the paper itself, which contains the underlying experimental tables) over the secondary summary, and it flags the discrepancy explicitly rather than silently averaging or ignoring it ([Tjandra et al., 2015](document_1.txt)). All numerical claims below are attributed to the specific document that reports them.

## What the Proposed Models Actually Change

GRURNTN applies a tensor product operation between the current input and the previous hidden layer multiplied by the reset gate in order to compute the candidate hidden layer, thereby increasing model expressiveness through second-degree polynomial interactions compared with the first-degree interactions of standard dot-product-plus-addition RNNs ([Tjandra et al., 2015](document_1.txt)). LSTMRNTN applies the same tensor-product principle between the current input and the previous hidden layer, but inside the memory-cell computation of the LSTM unit ([Tjandra et al., 2015](document_1.txt)). The stated design motivation is that gating alone does not give an RNN a more powerful means of modelling direct input–hidden interaction, while tensor networks alone struggle to capture long-term dependencies because they lack gating ([Tjandra et al., 2015](document_1.txt)).

The baselines are therefore the natural controls: GRURNN against GRURNTN, and LSTMRNN against LSTMRNTN, with the baselines deliberately enlarged so that parameter counts are comparable ([Tjandra et al., 2015](document_1.txt)).

## Experimental Conditions That Make the Comparison Fair

Three design choices are relevant to judging the size of the reported gains. First, the baseline GRURNN was constrained to have a similar number of parameters to GRURNTN, and the baseline LSTMRNN was similarly constrained against LSTMRNTN ([Tjandra et al., 2015](document_1.txt)). Second, all experiments used the Penn TreeBank corpus with standard preprocessing, a 10,000-word vocabulary, and AdaGrad optimisation with an identical learning-rate decay schedule ([Tjandra et al., 2015](document_1.txt)). Third, the authors state that their baseline and proposed-model experiments did not use dynamic evaluation, which matters because one published LSTM result in their own comparison table does use it ([Tjandra et al., 2015](document_1.txt)).

The reported parameter budgets were approximately 12 million for the GRU-based pair and approximately 13 million for the LSTM-based pair at word level, and approximately 2.2 million versus approximately 2.6 million respectively at character level ([Tjandra et al., 2015](document_1.txt)). The paper achieves parameter matching by shrinking the proposed models' hidden layers (256 units for both proposed models) while widening the baselines (860 units for GRURNN at word level; 740 for LSTMRNN at word level; 820 for GRURNN and 600 for LSTMRNN at character level) ([Tjandra et al., 2015](document_1.txt)).

## Reported Improvements on Character-Level Language Modelling

On character-level language modelling, performance is reported in bits-per-character (BPC), where lower is better ([Tjandra et al., 2015](document_1.txt)). The results on the Penn TreeBank test set are as follows.

| Model | Test BPC | Absolute change vs paired baseline | Relative change vs paired baseline |
|---|---|---|---|
| GRURNN (baseline) | 1.39 | — | — |
| GRURNTN (proposed) | 1.33 | 0.06 lower | 4.32% |
| LSTMRNN (baseline) | 1.37 | — | — |
| LSTMRNTN (proposed) | 1.34 | 0.03 lower | 2.22% |

GRURNTN reduced BPC from 1.39 to 1.33, an absolute reduction of 0.06 and a relative reduction of 4.32% over the GRURNN baseline, while LSTMRNTN reduced BPC from 1.37 to 1.34, an absolute reduction of 0.03 and a relative reduction of 2.22% over the LSTMRNN baseline ([Tjandra et al., 2015](document_1.txt); [Third-party research note, n.d.](document_2.txt)). Both documents agree on these two figures, which strengthens confidence in them ([Tjandra et al., 2015](document_1.txt); [Third-party research note, n.d.](document_2.txt)).

Two further observations from the same experiment are worth recording. First, GRURNTN slightly outperformed LSTMRNTN on this task, 1.33 versus 1.34, so the tensor-augmented GRU was the best of the four models tested ([Tjandra et al., 2015](document_1.txt)). Second, the validation curves showed that both proposed models produced lower BPC than their baselines from the first epoch to the last, indicating the advantage was not merely a final-epoch artefact ([Tjandra et al., 2015](document_1.txt)).

## Reported Improvements on Word-Level Language Modelling

On word-level language modelling, performance is reported in perplexity (PPL), again with lower being better ([Tjandra et al., 2015](document_1.txt)).

| Model | Test PPL | Absolute change vs paired baseline | Relative change vs paired baseline |
|---|---|---|---|
| GRURNN (baseline) | 97.78 | — | — |
| GRURNTN (proposed) | 87.38 | 10.40 lower | 10.63% |
| LSTMRNN (baseline) | 108.26 | — | — |
| LSTMRNTN (proposed) | 96.97 | 11.29 lower | 10.42% |

The primary source reports that GRURNTN reduced perplexity from 97.78 to 87.38, an absolute reduction of 10.4 and a relative reduction of 10.63% over GRURNN, and that LSTMRNTN reduced perplexity from 108.26 to 96.97, an absolute reduction of 11.29 and a relative reduction of 10.42% over LSTMRNN ([Tjandra et al., 2015](document_1.txt)). The paper further states that GRURNTN outperformed all baseline models as well as the other proposed model by a large margin on this task ([Tjandra et al., 2015](document_1.txt)).

It is notable that on word-level modelling the two baselines invert their relative ordering compared with character-level modelling: the GRURNN baseline (97.78) was substantially better than the LSTMRNN baseline (108.26), whereas on character level the LSTMRNN baseline (1.37) was better than the GRURNN baseline (1.39) ([Tjandra et al., 2015](document_1.txt)). Nevertheless, the tensor-augmented GRU remained the strongest single model overall on word-level perplexity, beating even LSTMRNTN by roughly 9.9% in relative terms ([Tjandra et al., 2015](document_1.txt)).

## Improvements Relative to Published Prior Results

Both documents also situate the proposed models against published systems evaluated on the same corpus.

### Character-level comparisons

| Model | Test BPC |
|---|---|
| NNLM | 1.57 |
| BPTT-RNN | 1.42 |
| HF-MRNN | 1.41 |
| sRNN | 1.41 |
| DOT(S)-RNN | 1.39 |
| LSTMRNN (with adaptive noise, with dynamic evaluation) | 1.26 / 1.24 |
| GRURNN (baseline) | 1.39 |
| LSTMRNN (baseline) | 1.37 |
| GRURNTN (proposed) | 1.33 |
| LSTMRNTN (proposed) | 1.34 |

The character-level results were reported in the paper's first table ([Tjandra et al., 2015](document_1.txt)). GRURNTN at 1.33 improves on the DOT(S)-RNN result of 1.39 by 4.32% in relative terms, and on the NNLM result of 1.57 by 15.29% ([Tjandra et al., 2015](document_1.txt)). The single published LSTM variant reporting 1.26 and 1.24 achieves a lower BPC than the proposed models, but it uses adaptive noise regularisation and dynamic evaluation, which the authors explicitly state were not used in their own baseline or proposed-model experiments ([Tjandra et al., 2015](document_1.txt)). Directly comparing the proposed models with that entry would therefore be invalid, and the paper does not claim otherwise ([Tjandra et al., 2015](document_1.txt)).

### Word-level comparisons

| Model | Test PPL |
|---|---|
| N-Gram | 141 |
| RNNLM (without dynamic evaluation) | 124.7 |
| RNNLM (with dynamic evaluation) | 123.2 |
| SCRNN | 115 |
| sRNN | 110.0 |
| DOT(S)-RNN | 107.5 |
| GRURNN (baseline) | 97.78 |
| LSTMRNN (baseline) | 108.26 |
| GRURNTN (proposed) | 87.38 |
| LSTMRNTN (proposed) | 96.97 |

These figures were reported in the paper's second table ([Tjandra et al., 2015](document_1.txt)). Relative to the best previously published non-dynamic-evaluation tensor or deep-transition model listed, DOT(S)-RNN at 107.5, GRURNTN at 87.38 represents an 18.72% relative perplexity reduction, and relative to sRNN at 110.0 it represents a 20.56% reduction ([Tjandra et al., 2015](document_1.txt)). LSTMRNTN at 96.97 improves on DOT(S)-RNN by 9.80% in relative terms ([Tjandra et al., 2015](document_1.txt)). GRURNTN also outperformed the paper's own GRU baseline by 10.63% and LSTMRNTN by 9.89% ([Tjandra et al., 2015](document_1.txt)).

## A Material Discrepancy Between the Two Sources

The two documents disagree on the word-level GRURNTN result, and this must be stated plainly.

| Metric | Primary paper ([Tjandra et al., 2015](document_1.txt)) | Third-party note ([Third-party research note, n.d.](document_2.txt)) |
|---|---|---|
| GRURNTN word-level test PPL | 87.38 | 92.98 |
| Absolute PPL reduction vs GRURNN (97.78) | 10.40 | 4.8 |
| Relative PPL reduction vs GRURNN | 10.63% | 4.91% |

The primary source reports 87.38 for GRURNTN in its own results table and states the improvement as 10.4 absolute / 10.63% relative ([Tjandra et al., 2015](document_1.txt)). The third-party note instead reports 92.98 and a 4.8 absolute / 4.91% relative improvement, while simultaneously asserting that this figure "comes from the paper's word-level language modeling experiment" ([Third-party research note, n.d.](document_2.txt)). Since the paper's own table contains 87.38 and not 92.98, and since 97.78 minus 87.38 equals 10.40 (matching the paper's stated absolute figure), the internally consistent value is 87.38 ([Tjandra et al., 2015](document_1.txt)). I therefore treat the 92.98 figure in the secondary note as unsupported and use 87.38, 10.40 absolute and 10.63% relative as the correct word-level GRURNTN improvement ([Tjandra et al., 2015](document_1.txt)). The character-level figures and the LSTMRNTN word-level figures are identical in both documents and are not in dispute ([Tjandra et al., 2015](document_1.txt); [Third-party research note, n.d.](document_2.txt)).

## How Large Are These Gains, in Context?

Several features of the results bear on how the magnitude of the improvement should be interpreted.

On the smaller task, character-level modelling, the gains are modest in absolute terms but consistent: 0.06 BPC for the GRU variant and 0.03 BPC for the LSTM variant, corresponding to 4.32% and 2.22% relative reductions ([Tjandra et al., 2015](document_1.txt)). The GRU variant benefits roughly twice as much as the LSTM variant in relative terms on this task ([Tjandra et al., 2015](document_1.txt)).

On the larger task, word-level modelling, the gains are considerably larger: 10.63% relative for GRURNTN and 10.42% relative for LSTMRNTN ([Tjandra et al., 2015](document_1.txt)). The asymmetry between tasks suggests the tensor interaction contributes more when the model must capture longer-range lexical dependencies, which is consistent with the paper's framing that tensor products supply richer input–hidden interaction while gating supplies long-term memory ([Tjandra et al., 2015](document_1.txt)).

The claim that these gains came at a comparable parameter budget is explicitly supported by the paper's parameter-matching procedure and its stated totals ([Tjandra et al., 2015](document_1.txt)); the secondary note repeats this conclusion ([Third-party research note, n.d.](document_2.txt)). Because optimisation settings, corpus splits and vocabulary were held constant across the comparisons, the reported differences are not plausibly attributable to a more favourable training regime ([Tjandra et al., 2015](document_1.txt)).

Two caveats temper the magnitude claims. First, all results come from a single corpus, Penn TreeBank, so generalisation to other temporal or sequential tasks remains untested by these experiments; the authors themselves list speech recognition and video recognition as future work ([Tjandra et al., 2015](document_1.txt)). Second, the best character-level figure in the comparison table, 1.24, belongs to an LSTM configuration using adaptive noise and dynamic evaluation, which was outside the experimental protocol of this study, meaning the proposed models are not shown to be the best absolute performers on that benchmark ([Tjandra et al., 2015](document_1.txt)). Third, no significance testing, confidence intervals, or repeated-run variance is reported in either document, so the improvements are described as observed differences between runs rather than as statistically validated effects ([Tjandra et al., 2015](document_1.txt); [Third-party research note, n.d.](document_2.txt)).

## Conclusion

Based on the evidence available, the introduced models improve on their paired baselines on both evaluated tasks and under matched parameter budgets. GRURNTN reduced character-level test BPC from 1.39 to 1.33 (0.06 absolute, 4.32% relative) and word-level test PPL from 97.78 to 87.38 (10.40 absolute, 10.63% relative). LSTMRNTN reduced character-level test BPC from 1.37 to 1.34 (0.03 absolute, 2.22% relative) and word-level test PPL from 108.26 to 96.97 (11.29 absolute, 10.42% relative) ([Tjandra et al., 2015](document_1.txt)). GRURNTN was the strongest of the four models on both tasks, and both proposed models outperformed all published baselines listed in the paper that were evaluated without dynamic evaluation ([Tjandra et al., 2015](document_1.txt)). A secondary source's claim of a 92.98 word-level perplexity for GRURNTN is inconsistent with the primary paper's own results table and should not be relied upon ([Third-party research note, n.d.](document_2.txt); [Tjandra et al., 2015](document_1.txt)). The most defensible reading is that combining gating with tensor products delivered moderate relative gains on character-level modelling and larger relative gains on word-level modelling, within the limits of a single-corpus, single-run experimental design.

## References

Tjandra, A., Sakti, S., Manurung, R., Adriani, M., & Nakamura, S. (2015). *Gated recurrent neural tensor network* [Research paper]. document_1.txt

Third-party research note: Gated recurrent neural tensor network. (n.d.). document_2.txt