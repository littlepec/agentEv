# Quantifying the Performance Improvements of GRURNTN and LSTMRNTN over Baseline and Previously Published Language Models on the Penn Treebank Benchmark

## Introduction

Word-level language modeling on the Penn Treebank (PTB) benchmark is a long-standing testbed for evaluating recurrent neural network architectures, and perplexity (PPL) is the standard evaluation metric because it summarizes how well a model predicts the next token in a sequence. In this metric, lower values are better, and reductions correspond to more accurate probability assignments over test sequences. The source document analyzed here reports a controlled comparison in which two internally constructed baselines — a gated recurrent unit recurrent neural network (GRURNN) and a long short-term memory recurrent neural network (LSTMRNN) — are evaluated against two proposed variants, GRURNTN and LSTMRNTN, as well as against several previously published systems, including N-Gram, RNNLM with and without dynamic evaluation, SCRNN, sRNN, and DOT(S)-RNN ([Document 1](document_1.txt)).

The query guiding this report concerns the magnitude of improvement achieved by the introduced models relative to previous models. Answering this question carefully requires separating two distinct comparison classes that the source reports: first, the paired improvements of each proposed model over its own in-house baseline, and second, the improvements of the proposed models over previously published results. The document provides explicit numerical evidence for the first class and a full results table that permits computation of the second class. This report quantifies both, examines the training-dynamics evidence, and assesses the reliability and limitations of the conclusions that can be drawn.

## Data and Evaluation Framework

### Benchmark and Metric

All figures reported in the source derive from the PTB word-level language modeling task, with test set perplexity as the primary outcome and validation set perplexity per epoch used to characterize learning progress ([Document 1](document_1.txt)). Because perplexity is an exponential function of average negative log-likelihood, even modest absolute reductions are meaningful; double-digit absolute reductions on a benchmark where published systems cluster between roughly 107 and 141 PPL are substantial.

### Models Compared

The comparison set comprises three tiers. The first tier consists of the authors' own baselines: GRURNN at 97.78 test PPL and LSTMRNN at 108.26 test PPL. The second tier contains the proposed models: GRURNTN at 87.38 PPL and LSTMRNTN at 96.97 PPL. The third tier contains previously published results: N-Gram (141), RNNLM without dynamic evaluation (124.7), RNNLM with dynamic evaluation (123.2), SCRNN (115), sRNN (110.0), and DOT(S)-RNN (107.5) ([Document 1](document_1.txt)). The naming convention implies that the "TN" suffix denotes an architectural modification applied to the corresponding baseline unit, which enables clean paired comparisons between GRURNTN and GRURNN, and between LSTMRNTN and LSTMRNN.

## Quantitative Results

### Improvements Over the In-House Baselines

The source states directly that both proposed models outperformed their respective baselines. GRURNTN reduced perplexity from 97.78 to 87.38, an absolute reduction of 10.40 PPL and a relative reduction of 10.63%. LSTMRNTN reduced perplexity from 108.26 to 96.97, an absolute reduction of 11.29 PPL and a relative reduction of 10.42% ([Document 1](document_1.txt)).

| Comparison | Baseline PPL | Proposed PPL | Absolute Reduction | Relative Reduction |
|---|---|---|---|---|
| GRURNTN vs. GRURNN | 97.78 | 87.38 | 10.40 | 10.63% |
| LSTMRNTN vs. LSTMRNN | 108.26 | 96.97 | 11.29 | 10.42% |

Source: test set perplexity values as reported in [Document 1](document_1.txt); absolute and relative reductions as stated in the same source.

Two observations follow from these paired results. First, the relative gains are nearly identical across the two architecture families — 10.63% for the GRU variant and 10.42% for the LSTM variant — which is consistent with the proposed modification conferring a roughly proportional benefit irrespective of the underlying recurrent unit. Second, in absolute terms LSTMRNTN achieves the larger reduction (11.29 PPL), but this partly reflects its higher starting point; in relative terms GRURNTN's gain is marginally larger. Neither difference in relative gain is large, and the source does not report variance or significance testing, so the two relative gains should be treated as effectively comparable rather than ranked.

The source also notes that LSTMRNTN "improved the LSTMRNN model and its performance closely resembles the baseline GRURNN" ([Document 1](document_1.txt)). Numerically, LSTMRNTN (96.97) is 0.81 PPL better than GRURNN (97.78), a relative edge of approximately 0.83%. In other words, the LSTM-based proposed model essentially closes the gap that separated the LSTM baseline from the GRU baseline, but does not open a new margin beyond it. By contrast, the source states that GRURNTN "outperformed all the baseline models as well as the other models by a large margin" ([Document 1](document_1.txt)), and this claim is supported by the cross-model ranking presented below.

### Improvements Over Previously Published Models

The published reference models span a range of 33.5 PPL, from N-Gram at 141 to DOT(S)-RNN at 107.5 ([Document 1](document_1.txt)). Against this set, GRURNTN records large reductions across the board, while LSTMRNTN records moderate but consistent reductions. The table below reports absolute differences and relative reductions computed from the perplexity values given in the source.

| Prior Model | Prior PPL | GRURNTN PPL | Abs. Gain (GRURNTN) | Rel. Gain (GRURNTN) | LSTMRNTN PPL | Abs. Gain (LSTMRNTN) | Rel. Gain (LSTMRNTN) |
|---|---|---|---|---|---|---|---|
| N-Gram | 141 | 87.38 | 53.62 | 38.03% | 96.97 | 44.03 | 31.23% |
| RNNLM (w/o dyn. eval.) | 124.7 | 87.38 | 37.32 | 29.93% | 96.97 | 27.73 | 22.24% |
| RNNLM (w/ dyn. eval.) | 123.2 | 87.38 | 35.82 | 29.07% | 96.97 | 26.23 | 21.29% |
| SCRNN | 115 | 87.38 | 27.62 | 24.02% | 96.97 | 18.03 | 15.68% |
| sRNN | 110.0 | 87.38 | 22.62 | 20.56% | 96.97 | 13.03 | 11.85% |
| DOT(S)-RNN | 107.5 | 87.38 | 20.12 | 18.72% | 96.97 | 10.53 | 9.80% |
| GRURNN (baseline) | 97.78 | 87.38 | 10.40 | 10.63% | 96.97 | 0.81 | 0.83% |
| LSTMRNN (baseline) | 108.26 | 87.38 | 20.88 | 19.29% | 96.97 | 11.29 | 10.42% |

Source: perplexity values from [Document 1](document_1.txt); absolute and relative gains computed by the author of this report from those values, using (prior PPL − proposed PPL) / prior PPL × 100.

Several patterns emerge. GRURNTN's advantage over the strongest published prior model, DOT(S)-RNN, is 20.12 PPL, or 18.72% relative; over the weakest, N-Gram, it is 53.62 PPL, or 38.03% relative. LSTMRNTN's corresponding gains are 10.53 PPL (9.80%) over DOT(S)-RNN and 44.03 PPL (31.23%) over N-Gram. Notably, the GRURNTN improvement over the LSTM baseline (19.29% relative) is nearly as large as its improvement over the strongest published model (18.72% relative), because the LSTMRNN baseline itself was weaker than DOT(S)-RNN at 108.26 versus 107.5 PPL ([Document 1](document_1.txt)).

### Cross-Model Ranking

Ordering all ten reported systems from lowest to highest test perplexity clarifies the overall landscape: GRURNTN (87.38) ranks first, followed by LSTMRNTN (96.97), GRURNN (97.78), DOT(S)-RNN (107.5), LSTMRNN (108.26), sRNN (110.0), SCRNN (115), RNNLM with dynamic evaluation (123.2), RNNLM without dynamic evaluation (124.7), and N-Gram (141) ([Document 1](document_1.txt)). Two implications are worth stating explicitly. First, the GRURNN baseline already surpassed every published model in the comparison set, which means the proposed GRURNTN improves upon a baseline that was already best in class. Second, the LSTMRNN baseline did not surpass the strongest published model, so the proposed LSTMRNTN's advance past DOT(S)-RNN is a genuine, if modest, contribution of that model variant.

### Training Dynamics

Beyond terminal test perplexity, the source reports that Fig. 9 compares validation-set perplexity per epoch across models. GRURNN made faster progress than LSTMRNN, and GRURNTN's progress was also better than LSTMRNTN's; the best model in the task was GRURNTN, which had a consistently lower perplexity than the other models throughout training ([Document 1](document_1.txt)). This convergence evidence suggests that GRURNTN's final advantage is not solely a test-set artifact but is observable on held-out validation data across epochs.

## Discussion and Interpretation

The headline answer to the query is that the introduced models achieve approximately a 10.4% to 10.6% relative perplexity reduction over their own direct baselines, and substantially larger reductions — ranging from roughly 9.8% to 38.0% — over previously published models, depending on which prior system is used as the comparator ([Document 1](document_1.txt)). The single most defensible framing of the result is that GRURNTN is the strongest model reported in the study, at 87.38 PPL, beating every baseline and every published comparator by a margin the source describes as large; LSTMRNTN is a moderate improvement that lifts the LSTM family to approximately parity with the GRU baseline but does not exceed GRURNTN.

The consistency of the paired relative gains (10.63% and 10.42%) is arguably the most robust finding, because it holds under a controlled comparison in which baselines and proposed models were trained within the same experimental pipeline. The comparisons against published results are directionally clear but weaker evidentially, because they compare numbers produced under potentially different training regimes, regularization schemes, and tuning budgets. The source does not state that published models were re-implemented under identical conditions, so those gaps should be interpreted as indicative rather than strictly controlled.

## Limitations and Caveats

Several limitations constrain the strength of the conclusions. The evidence rests on a single dataset and task (PTB word-level language modeling), so generalization to other corpora or tasks is untested in the provided material ([Document 1](document_1.txt)). No variance estimates, confidence intervals, or significance tests are reported, so the reliability of small differences — most notably the 0.81 PPL edge of LSTMRNTN over GRURNN — cannot be assessed. The excerpt also omits parameter counts, computational cost, and architectural detail, which are necessary for judging whether the gains are attributable to the proposed mechanism rather than to increased capacity. Finally, the published-model comparisons are cross-study and therefore potentially confounded, and the two RNNLM variants differ by only 1.5 PPL, indicating that the dynamic-evaluation distinction is a comparatively small factor in this comparison set ([Document 1](document_1.txt)).

## Conclusion

Based on the reported evidence, the proposed models deliver consistent and meaningful improvements. GRURNTN reduces perplexity by 10.40 absolute points (10.63% relative) over the GRURNN baseline, and LSTMRNTN reduces perplexity by 11.29 absolute points (10.42% relative) over the LSTMRNN baseline ([Document 1](document_1.txt)). Against previously published models, GRURNTN achieves relative reductions of 18.72% against DOT(S)-RNN and 38.03% against N-Gram, while LSTMRNTN achieves 9.80% and 31.23% against the same comparators, respectively. GRURNTN is unambiguously the best-performing system in the study, both in final test perplexity and in per-epoch validation progress, whereas LSTMRNTN provides a moderate gain that essentially brings the LSTM family to parity with the GRU baseline. The improvements are therefore best characterized as robust and practically meaningful within this benchmark, but supported by a narrow evidence base that would benefit from multi-seed replication, significance testing, and efficiency reporting before broader claims can be made.

## References

document_1.txt. (n.d.). *Penn Treebank word-level language modeling results: Baseline models, proposed models, and published comparisons* [Unpublished manuscript]. Retrieved September 15, 2026, from document_1.txt