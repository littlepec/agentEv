# Quantifying the Improvement of GRURNTN and LSTMRNTN over Previous Language Models

## Introduction

This report answers the query: **How much improvement do the introduced models achieve compared to the previous models?** The introduced models are GRURNTN and LSTMRNTN, and the previous models primarily refer to their corresponding baselines, GRURNN and LSTMRNN, as well as several published language models. The evidence supplied comes from two documents: one reporting Penn Treebank (PTB) test-set perplexity (PPL) and validation progress, and another reporting broader character-level and word-level language modeling results, including bits-per-character (BPC) and PPL improvements ([Document 1](document_1.txt); [Document 2](document_2.txt)). The findings consistently indicate that both proposed models outperform their respective baselines, although the magnitude of improvement varies by metric, task, and source ([Document 1](document_1.txt); [Document 2](document_2.txt)).

The most conservative summary is that the introduced models deliver double-digit relative reductions in PTB word-level PPL over their matching baselines: GRURNTN reduces PPL by 10.4 absolute points (10.63% relative) over GRURNN, and LSTMRNTN reduces PPL by 11.29 absolute points (10.42% relative) over LSTMRNN ([Document 1](document_1.txt)). In character-level or additional word-level evaluations, the proposed models also improve BPC: GRURNTN achieves a 0.06 absolute / 4.32% relative BPC gain over GRURNN, and LSTMRNTN achieves a 0.03 absolute / 2.22% relative BPC gain over LSTMRNN ([Document 2](document_2.txt)). However, one source reports a smaller GRURNTN PPL improvement of 4.8 absolute / 4.91% relative over GRURNN, which introduces an important inconsistency that must be acknowledged ([Document 2](document_2.txt)). Overall, the evidence supports a clear conclusion: GRURNTN is the strongest introduced model, and both introduced models improve over the previous baselines, but the exact headline improvement for GRURNTN depends on the evaluation context ([Document 1](document_1.txt); [Document 2](document_2.txt)).

## Evaluated Models and Benchmarks

### Baseline and Proposed Models

The previous models in this comparison are GRURNN and LSTMRNN, described as baseline models, and several published models including N-Gram, RNNLM, SCRNN, sRNN, and DOT(S)-RNN ([Document 1](document_1.txt)). The introduced models are GRURNTN and LSTMRNTN, which are proposed variants of the GRU-based and LSTM-based recurrent neural networks, respectively ([Document 1](document_1.txt)). The naming suggests that the proposed models add a tensor network or similar component to the baseline architectures, although the supplied documents do not provide full architectural details ([Document 1](document_1.txt); [Document 2](document_2.txt)). What is clear is that the proposed models are evaluated directly against their matching baselines and against previously published results ([Document 1](document_1.txt)).

Document 2 adds that both proposed models produced lower test scores than their corresponding baselines and outperformed the baselines in character-level and word-level language modeling tasks with a similar number of parameters ([Document 2](document_2.txt)). This is a significant point because it reduces the likelihood that the improvements are simply due to a larger parameter budget. The source explicitly states that the comparison was made with a similar number of parameters, which strengthens the claim that the architectural changes are responsible for the gains ([Document 2](document_2.txt)).

### Evaluation Metrics and Datasets

The primary benchmark discussed in Document 1 is the PTB word-level language modeling task, measured by test-set perplexity ([Document 1](document_1.txt)). The document also reports validation-set PPL per epoch to compare training progress across models ([Document 1](document_1.txt)). Document 2 extends the evaluation to character-level and word-level tasks, using both BPC and PPL as metrics ([Document 2](document_2.txt)). The combined evidence therefore covers multiple metrics and task types, which is useful for assessing whether the improvements are robust or metric-specific ([Document 1](document_1.txt); [Document 2](document_2.txt)).

The PTB test-set PPL values for the published models and the internal baselines are as follows: N-Gram 141, RNNLM without dynamic evaluation 124.7, RNNLM with dynamic evaluation 123.2, SCRNN 115, sRNN 110.0, and DOT(S)-RNN 107.5 ([Document 1](document_1.txt)). The baseline models are GRURNN at 97.78 and LSTMRNN at 108.26, while the proposed models are GRURNTN at 87.38 and LSTMRNTN at 96.97 ([Document 1](document_1.txt)). These values form the basis for the quantitative comparisons below.

## Word-Level PTB Perplexity Improvements

### GRURNTN versus GRURNN

The clearest and most direct improvement reported in Document 1 is that GRURNTN reduced perplexity from 97.78 to 87.38 relative to the baseline GRURNN ([Document 1](document_1.txt)). This represents a reduction of 10.4 absolute PPL points and a 10.63% relative improvement ([Document 1](document_1.txt)). The source further states that GRURNTN outperformed all baseline models as well as the other models by a large margin ([Document 1](document_1.txt)). This is a strong claim because it places GRURNTN not only ahead of its matched baseline but also ahead of every published model listed in the comparison table ([Document 1](document_1.txt)).

The practical significance of a 10.63% relative PPL reduction is substantial in language modeling. Perplexity is an exponential measure of uncertainty, so a lower PPL indicates that the model assigns higher probability to the correct next word on average. A drop from 97.78 to 87.38 means the model is meaningfully more confident and accurate on the PTB test set ([Document 1](document_1.txt)). When compared with the best published model in the table, DOT(S)-RNN at 107.5, GRURNTN’s 87.38 represents an additional reduction of 20.12 absolute points, or approximately 18.72% relative to DOT(S)-RNN ([Document 1](document_1.txt)). This calculation is derived from the reported values and reinforces the conclusion that GRURNTN is the top-performing model in the PTB comparison ([Document 1](document_1.txt)).

### LSTMRNTN versus LSTMRNN

LSTMRNTN also improves over its baseline, reducing PPL from 108.26 to 96.97, which is a reduction of 11.29 absolute points and 10.42% relative ([Document 1](document_1.txt)). In absolute terms, this is an even larger point reduction than GRURNTN’s improvement over GRURNN, although the relative percentage is slightly smaller (10.42% vs. 10.63%) ([Document 1](document_1.txt)). The source notes that LSTMRNTN improved the LSTMRNN model and that its performance closely resembles the baseline GRURNN ([Document 1](document_1.txt)). Numerically, however, LSTMRNTN’s 96.97 is slightly better than GRURNN’s 97.78, giving LSTMRNTN a small additional advantage of 0.81 absolute points, or about 0.83% relative to GRURNN ([Document 1](document_1.txt)).

This nuance matters for interpretation. LSTMRNTN is clearly better than the model it was designed to improve, LSTMRNN, but it does not dominate the GRU-based baseline GRURNN by a wide margin ([Document 1](document_1.txt)). It does, however, outperform the best published model in the table: against DOT(S)-RNN at 107.5, LSTMRNTN’s 96.97 is a reduction of 10.53 absolute points, or approximately 9.79% relative ([Document 1](document_1.txt)). Thus, LSTMRNTN is a meaningful improvement over both its own baseline and the previously published results, even if it remains behind GRURNTN ([Document 1](document_1.txt)).

### Comparison with Published Models

The published models listed in Document 1 range from 141 PPL for N-Gram to 107.5 PPL for DOT(S)-RNN ([Document 1](document_1.txt)). Both proposed models beat all of them. GRURNTN at 87.38 is 53.62 points better than N-Gram, 37.32 points better than RNNLM without dynamic evaluation, 35.82 points better than RNNLM with dynamic evaluation, 27.62 points better than SCRNN, 22.62 points better than sRNN, and 20.12 points better than DOT(S)-RNN ([Document 1](document_1.txt)). LSTMRNTN at 96.97 is also better than every published model, with reductions of 44.03, 27.73, 26.23, 18.03, 13.03, and 10.53 points against the same respective models ([Document 1](document_1.txt)). These derived comparisons are summarized in Table 1 and Table 2 below.

**Table 1. PTB test-set PPL for published models, baselines, and proposed models**

| Model | PTB Test PPL |
|---|---:|
| N-Gram | 141 |
| RNNLM (w/o dyn. eval) | 124.7 |
| RNNLM (w/ dyn. eval) | 123.2 |
| SCRNN | 115 |
| sRNN | 110.0 |
| DOT(S)-RNN | 107.5 |
| GRURNN (baseline) | 97.78 |
| LSTMRNN (baseline) | 108.26 |
| GRURNTN (proposed) | 87.38 |
| LSTMRNTN (proposed) | 96.97 |

*Note.* Values are from Document 1 ([Document 1](document_1.txt)).

**Table 2. Derived PPL reductions of proposed models against selected previous models**

| Comparison | Absolute PPL Reduction | Relative PPL Reduction |
|---|---:|---:|
| GRURNTN vs. GRURNN | 10.40 | 10.63% |
| LSTMRNTN vs. LSTMRNN | 11.29 | 10.42% |
| GRURNTN vs. DOT(S)-RNN | 20.12 | 18.72% |
| LSTMRNTN vs. DOT(S)-RNN | 10.53 | 9.79% |
| GRURNTN vs. N-Gram | 53.62 | 38.03% |
| LSTMRNTN vs. N-Gram | 44.03 | 31.23% |

*Note.* Absolute and relative reductions are calculated from the PPL values reported in Document 1 ([Document 1](document_1.txt)). Relative reductions are computed as the absolute reduction divided by the previous model’s PPL.

## Character-Level and Additional PPL Improvements

### BPC Improvements

Document 2 reports additional gains on character-level and word-level language modeling tasks using BPC and PPL ([Document 2](document_2.txt)). For BPC, GRURNTN delivered a 0.06 absolute improvement and a 4.32% relative improvement over GRURNN ([Document 2](document_2.txt)). LSTMRNTN delivered a 0.03 absolute improvement and a 2.22% relative improvement over LSTMRNN ([Document 2](document_2.txt)). These BPC gains are smaller in absolute terms than the PPL gains, but they are still positive and meaningful in relative terms, especially for GRURNTN at 4.32% ([Document 2](document_2.txt)). The fact that both BPC and PPL improve suggests that the proposed models are not merely benefiting from a metric-specific artifact ([Document 2](document_2.txt)).

**Table 3. Reported BPC and PPL improvements over baselines**

| Proposed Model | Baseline | Metric | Absolute Improvement | Relative Improvement |
|---|---|---|---:|---:|
| GRURNTN | GRURNN | BPC | 0.06 | 4.32% |
| LSTMRNTN | LSTMRNN | BPC | 0.03 | 2.22% |
| GRURNTN | GRURNN | PPL | 4.8 | 4.91% |
| LSTMRNTN | LSTMRNN | PPL | 11.29 | 10.42% |

*Note.* Values are from Document 2 ([Document 2](document_2.txt)). The GRURNTN PPL row differs from the PTB-specific value in Document 1, as discussed below.

### Discrepancy in Reported GRURNTN PPL Improvement

A careful reading reveals an inconsistency between the two documents regarding GRURNTN’s PPL improvement over GRURNN. Document 1 reports a PTB test-set PPL reduction from 97.78 to 87.38, which equals 10.4 absolute points and 10.63% relative improvement ([Document 1](document_1.txt)). Document 2, however, reports a GRURNTN PPL improvement of 4.8 absolute points and 4.91% relative improvement over GRURNN ([Document 2](document_2.txt)). For LSTMRNTN, both documents agree on the 11.29 absolute and 10.42% relative PPL improvement over LSTMRNN ([Document 1](document_1.txt); [Document 2](document_2.txt)). The GRURNTN discrepancy is therefore specific to that model-metric pair and likely reflects a different evaluation setting, dataset, or averaging procedure in Document 2 ([Document 2](document_2.txt)). Because Document 1 explicitly ties its numbers to the PTB test set, the 10.4-point figure is the more precise PTB-specific claim, while the 4.8-point figure may refer to a broader or different task average ([Document 1](document_1.txt); [Document 2](document_2.txt)). This inconsistency means that any single headline number for GRURNTN’s PPL gain should be qualified by the evaluation context.

## Synthesis of Absolute and Relative Gains

Combining the evidence, the introduced models achieve the following improvements over the previous models:

- **GRURNTN over GRURNN:** 10.4 absolute / 10.63% relative PPL improvement on PTB, and 0.06 absolute / 4.32% relative BPC improvement in additional tasks ([Document 1](document_1.txt); [Document 2](document_2.txt)). Document 2 also reports a 4.8 absolute / 4.91% relative PPL improvement, which is smaller and context-dependent ([Document 2](document_2.txt)).
- **LSTMRNTN over LSTMRNN:** 11.29 absolute / 10.42% relative PPL improvement, and 0.03 absolute / 2.22% relative BPC improvement ([Document 1](document_1.txt); [Document 2](document_2.txt)).
- **Against published models:** Both proposed models outperform every published model in the PTB table, with GRURNTN achieving the largest margin over the best published model, DOT(S)-RNN (20.12 absolute / 18.72% relative reduction), followed by LSTMRNTN (10.53 absolute / 9.79% relative reduction) ([Document 1](document_1.txt)).

The training-progress evidence reinforces these results. Document 1 reports that GRURNN made faster progress than LSTMRNN, and that GRURNTN’s progress was better than LSTMRNTN’s ([Document 1](document_1.txt)). The best model in the task was GRURNTN, which had a consistently lower PPL than the other models across epochs ([Document 1](document_1.txt)). This suggests that GRURNTN’s advantage is not a single-epoch fluctuation but a stable pattern during training ([Document 1](document_1.txt)).

## Interpretation and Opinion

Based on the provided information, my concrete opinion is that the introduced models deliver reliable and meaningful improvements over the previous models, but the strength of the evidence is uneven across the two proposed architectures. GRURNTN is the most compelling result: it achieves a double-digit relative PPL reduction over its baseline on the PTB test set, it surpasses all published models by a wide margin, and it shows the best training progress and lowest PPL among the compared models ([Document 1](document_1.txt)). LSTMRNTN is also a successful improvement over its baseline, with an even larger absolute PPL reduction (11.29 points) and a comparable relative reduction (10.42%), but its advantage over the GRU-based baseline GRURNN is marginal (0.81 points, 0.83% relative), and it remains behind GRURNTN ([Document 1](document_1.txt)). Therefore, if the question is “which introduced model achieves the greatest improvement over previous models,” the answer is GRURNTN. If the question is “does the LSTM-based introduction improve its own previous model,” the answer is yes, and substantially so ([Document 1](document_1.txt)).

The BPC results add a second dimension of support: both proposed models improve over their baselines in character-level or additional word-level tasks with a similar number of parameters ([Document 2](document_2.txt)). The relative BPC gains of 4.32% for GRURNTN and 2.22% for LSTMRNTN are not enormous, but they are consistent with the PPL findings and suggest that the architectural changes generalize beyond a single metric ([Document 2](document_2.txt)). The main caveat is the GRURNTN PPL discrepancy between the two documents; this does not undermine the overall conclusion that GRURNTN improves over GRURNN, but it does mean that the exact magnitude should be reported with its source and evaluation context ([Document 1](document_1.txt); [Document 2](document_2.txt)).

## Limitations and Reliability of Evidence

The analysis relies on two supplied documents that appear to be primary experimental reports ([Document 1](document_1.txt); [Document 2](document_2.txt)). They are relevant because they directly report the baseline and proposed model results, and they are the only sources permitted for this review. However, several limitations should be noted. First, neither document provides publication dates, so recency cannot be evaluated; they are treated as current evidence for this report. Second, exact parameter counts are not given, although Document 2 states that the models were compared with a similar number of parameters ([Document 2](document_2.txt)). Third, no statistical significance tests, confidence intervals, or variance estimates are reported, so the improvements are point estimates rather than statistically validated effects ([Document 1](document_1.txt); [Document 2](document_2.txt)). Fourth, the GRURNTN PPL discrepancy between Document 1 and Document 2 means that the precise size of the improvement depends on which evaluation context is used ([Document 1](document_1.txt); [Document 2](document_2.txt)). These limitations do not overturn the conclusion that the introduced models improve over the previous models, but they do call for cautious interpretation of any single headline number.

## Conclusion

The introduced models achieve substantial improvements compared to the previous models. GRURNTN improves over GRURNN by 10.4 absolute PPL points, or 10.63% relative, on the PTB test set, and by 0.06 absolute BPC, or 4.32% relative, in additional evaluations ([Document 1](document_1.txt); [Document 2](document_2.txt)). LSTMRNTN improves over LSTMRNN by 11.29 absolute PPL points, or 10.42% relative, and by 0.03 absolute BPC, or 2.22% relative ([Document 1](document_1.txt); [Document 2](document_2.txt)). Both proposed models outperform all published models listed in the PTB comparison, with GRURNTN delivering the largest margin over the best published model, DOT(S)-RNN, at 20.12 absolute points, or 18.72% relative ([Document 1](document_1.txt)). The only notable inconsistency is the smaller GRURNTN PPL improvement reported in Document 2 (4.8 absolute / 4.91% relative), which likely reflects a different evaluation context ([Document 2](document_2.txt)). On balance, the answer to the query is that the introduced models achieve meaningful, multi-metric improvements over the previous models, and GRURNTN is the strongest of the introduced models ([Document 1](document_1.txt); [Document 2](document_2.txt)).

## References

Document 1. (n.d.). *[PTB test set PPL and related work]*. document_1.txt.

Document 2. (n.d.). *[Overall results on character-level and word-level language modeling]*. document_2.txt.