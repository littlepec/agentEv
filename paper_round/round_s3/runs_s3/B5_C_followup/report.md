# Quantifying the Improvement of GRURNTN and LSTMRNTN Over Prior Language Models: An Analysis of Penn Treebank Perplexity Results

## Introduction

The document under review reports the results of a word-level language modeling experiment on the Penn Treebank (PTB) dataset, in which two proposed recurrent architectures — GRURNTN and LSTMRNTN — are evaluated against two architecturally matched internal baselines (GRURNN and LSTMRNN) and against six previously published models ([Anonymous, n.d.](document_1.txt)). The source presents test-set perplexity (PPL) figures for every model, alongside a qualitative account of validation-set learning dynamics. This report answers the central question: **how much improvement do the introduced models achieve compared to previous models?** The analysis distinguishes between two comparison classes — (a) the paper's own baselines, and (b) previously published third-party models — and quantifies each margin in both absolute and relative terms, using only the figures supplied by the source ([Anonymous, n.d.](document_1.txt)).

## Scope and Method of This Review

All quantitative statements in this report are derived exclusively from the figures reported in the single source document. Where the source supplies a percentage, that figure is reproduced directly; where it does not, the absolute difference and the relative (percentage) reduction are computed from the reported perplexity values so that the reader can see the full size of every margin rather than only the headline comparisons. No external benchmark data, no parameter counts, and no statistical significance tests are available in the source, so the analysis is strictly descriptive of the reported point estimates ([Anonymous, n.d.](document_1.txt)).

## Performance Metric and Experimental Setup

### The Penn Treebank word-level task

The reported experiment concerns word-level language modeling on PTB, a standard benchmark in which a model assigns probabilities to sequences of words ([Anonymous, n.d.](document_1.txt)). The source frames the task around test-set perplexity, which is the quantity tabulated for every model compared.

### Perplexity as the evaluation metric

Perplexity is reported for all models, and the source treats lower values as better throughout: improvements are described as "reductions," and the best model is identified as the one "which had a consistently lower PPL than the other models" ([Anonymous, n.d.](document_1.txt)). Accordingly, a reduction in PPL from one model to another constitutes an improvement, and the magnitude of that reduction — in absolute points and in percentage terms — is the natural measure of the gain.

### Models under comparison

The comparison set consists of four groups ([Anonymous, n.d.](document_1.txt)):

1. **Classical and early neural baselines**: N-Gram (141), RNNLM without dynamic evaluation (124.7), and RNNLM with dynamic evaluation (123.2).
2. **Intermediate recurrent baselines**: SCRNN (115), sRNN (110.0), and DOT(S)-RNN (107.5).
3. **The paper's own baselines**: GRURNN (97.78) and LSTMRNN (108.26).
4. **The proposed models**: GRURNTN (87.38) and LSTMRNTN (96.97).

## Improvements of the Proposed Models Over Their Own Baselines

### GRURNTN versus GRURNN

The source reports that GRURNTN reduced perplexity from 97.78 to 87.38, a reduction of **10.40 PPL in absolute terms** and **10.63% in relative terms** ([Anonymous, n.d.](document_1.txt)). This direction of change is unambiguous: the proposed gated recurrent unit with a tensor-network component improves on its architecturally matched baseline on the same test set under the same experimental conditions described by the source.

### LSTMRNTN versus LSTMRNN

The second proposed model reduced perplexity from 108.26 to 96.97, a reduction of **11.29 PPL absolute** and **10.42% relative** ([Anonymous, n.d.](document_1.txt)). Notably, this is the **larger absolute gain of the two**, driven by the weaker starting point of the LSTM baseline (108.26 versus 97.78 for GRURNN). The two models therefore produce near-identical *relative* gains (10.63% and 10.42%) despite different absolute starting points ([Anonymous, n.d.](document_1.txt)).

### Aggregate view of the two within-paper gains

| Comparison | Baseline PPL | Proposed PPL | Absolute reduction | Relative reduction |
|---|---|---|---|---|
| GRURNTN vs. GRURNN | 97.78 | 87.38 | 10.40 | 10.63% |
| LSTMRNTN vs. LSTMRNN | 108.26 | 96.97 | 11.29 | 10.42% |
| Mean of the two comparisons | — | — | 10.85 | 10.53% |

Source: ([Anonymous, n.d.](document_1.txt)).

Averaged across the two architecture families, the proposed modifications deliver a reduction of roughly **10.85 PPL, or about 10.53% relative**, over matched baselines — a consistent, in-family improvement rather than an isolated win in a single configuration ([Anonymous, n.d.](document_1.txt)).

### Head-to-head comparison of the two proposed models

The two proposed models are not equivalent in strength. GRURNTN (87.38) is **9.59 PPL lower** than LSTMRNTN (96.97), a **9.89% relative advantage** ([Anonymous, n.d.](document_1.txt)). The source states directly that "GRURNTN outperformed all the baseline models as well as the other models by a large margin" ([Anonymous, n.d.](document_1.txt)). Consequently, within the paper's own contribution set, the GRU-based variant of the proposed method is the superior configuration, and the LSTM-based variant is the more modest improvement.

### Relationship between the improved LSTM model and the GRU baseline

The source also makes an important cross-family observation: LSTMRNTN "improved the LSTMRNN model and its performance closely resembles the baseline GRURNN" ([Anonymous, n.d.](document_1.txt)). Quantitatively, LSTMRNTN (96.97) actually edges past GRURNN (97.78) by **0.81 PPL**, a **0.83% relative** margin. Framed as gap closure, the 11.29-point improvement of LSTMRNTN against its own 108.26 baseline eliminates 107.7% of the 10.48-point gap that separated LSTMRNN from GRURNN — that is, the proposed LSTM variant not only closes the architectural deficit but slightly exceeds the competing baseline ([Anonymous, n.d.](document_1.txt)).

## Improvements of the Proposed Models Over Previously Published Models

### Full comparison against prior published results

| Model | Test PPL | GRURNTN advantage (absolute) | GRURNTN advantage (relative) | LSTMRNTN advantage (absolute) | LSTMRNTN advantage (relative) |
|---|---|---|---|---|---|
| N-Gram | 141 | 53.62 | 38.03% | 44.03 | 31.23% |
| RNNLM (w/o dyn. eval) | 124.7 | 37.32 | 29.93% | 27.73 | 22.24% |
| RNNLM (w/ dyn. eval) | 123.2 | 35.82 | 29.07% | 26.23 | 21.29% |
| SCRNN | 115 | 27.62 | 24.02% | 18.03 | 15.68% |
| sRNN | 110.0 | 22.62 | 20.56% | 13.03 | 11.85% |
| DOT(S)-RNN | 107.5 | 20.12 | 18.72% | 10.53 | 9.79% |
| LSTMRNN (own baseline) | 108.26 | 20.88 | 19.29% | 11.29 | 10.42% |
| GRURNN (own baseline) | 97.78 | 10.40 | 10.63% | 0.81 | 0.83% |
| GRURNTN (proposed) | 87.38 | — | — | −9.59 (GRURNTN is better) | 9.89% |
| LSTMRNTN (proposed) | 96.97 | 9.59 | 9.89% | — | — |

Perplexity values are from the source; absolute and relative margins are computed from those values ([Anonymous, n.d.](document_1.txt)).

### Absolute margins

Against the weakest published comparator, the N-Gram model at 141 PPL, GRURNTN achieves a **53.62-point reduction** and LSTMRNTN a **44.03-point reduction** ([Anonymous, n.d.](document_1.txt)). Against the strongest published neural comparator, DOT(S)-RNN at 107.5 PPL, the margins narrow but remain substantial: **20.12 points** for GRURNTN and **10.53 points** for LSTMRNTN ([Anonymous, n.d.](document_1.txt)).

### Relative margins

In relative terms, GRURNTN's advantage ranges from **38.03%** over N-Gram down to **18.72%** over DOT(S)-RNN, while LSTMRNTN's advantage ranges from **31.23%** down to **9.79%** over the same endpoints ([Anonymous, n.d.](document_1.txt)). This produces a clear, monotone pattern: the stronger the prior model, the smaller the margin — a standard signature of diminishing returns as the baseline quality improves, and an indication that the reported comparisons behave sensibly rather than exhibiting implausible discontinuities.

### Diminishing returns as baselines strengthen

The steepest single drop in margin occurs between the N-Gram model and the RNNLM variants: GRURNTN's relative advantage falls from 38.03% to 29.07% across that step, and LSTMRNTN's falls from 31.23% to 21.29% ([Anonymous, n.d.](document_1.txt)). The margin then declines more gradually across SCRNN, sRNN, and DOT(S)-RNN. Importantly, GRURNTN's advantage over the strongest previously published model (18.72%) remains larger than its advantage over its own GRURNN baseline (10.63%), and roughly double that baseline margin in absolute terms (20.12 versus 10.40 PPL) ([Anonymous, n.d.](document_1.txt)).

## Learning Dynamics on the Validation Set

The source supplements the test-set table with a per-epoch validation-set comparison ([Anonymous, n.d.](document_1.txt)). Three observations are reported:

- GRURNN "made faster progress than LSTMRNN," indicating a convergence-speed advantage for the GRU baseline within the paper's own experimental setup.
- GRURNTN's progress was "also better than LSTMRNTN," meaning the proposed GRU variant improved faster during training than the proposed LSTM variant.
- GRURNTN was "the best model in this task," with "a consistently lower PPL than the other models" across the validation-set epochs ([Anonymous, n.d.](document_1.txt)).

These findings reinforce the test-set result: GRURNTN's advantage is not attributable to a single favourable evaluation point but appears consistently throughout training, at least at the granularity reported ([Anonymous, n.d.](document_1.txt)).

## Interpretation: How Large Is the Improvement?

Three conclusions follow from the reported figures, each grounded in the source data.

First, within the paper's own experimental framework, **both proposed models produce consistent, two-digit-percentage relative improvements over their matched baselines** — 10.63% for GRURNTN over GRURNN and 10.42% for LSTMRNTN over LSTMRNN ([Anonymous, n.d.](document_1.txt)). Because each proposed model differs from its baseline by a single architectural modification, this consistency across two different recurrent families (GRU-based and LSTM-based) strengthens the inference that the modification — rather than a confound specific to one architecture — drives the gain.

Second, **GRURNTN is the single best-performing model reported in the document**, outperforming both the published models and the paper's own baselines by what the source itself characterizes as a large margin ([Anonymous, n.d.](document_1.txt)). Its 87.38 PPL is 18.72% better than the best previously published model and 10.63% better than the best internal baseline.

Third, the improvement against prior published work is **substantial in relative terms but uneven in magnitude**: 18.72%–38.03% for GRURNTN and 9.79%–31.23% for LSTMRNTN depending on the comparator ([Anonymous, n.d.](document_1.txt)). The correct takeaway is therefore that the improvement is large relative to the field's earlier entries, but that its size is highly sensitive to which prior model is used as the reference point — a nuance that any headline summary should preserve.

## Limitations and Caveats

Several limitations constrain how far these numbers can be generalized.

- **No statistical testing**: The source reports point estimates without variance, confidence intervals, repeated runs, or significance tests, so no claim about the statistical reliability of the reported margins can be verified ([Anonymous, n.d.](document_1.txt)).
- **A single benchmark**: All evidence comes from the PTB word-level language modeling task; no second dataset is reported, so cross-domain generalization cannot be assessed from the source ([Anonymous, n.d.](document_1.txt)).
- **Unknown provenance of comparators**: The published models appear as bracketed citation numbers (e.g., [24], [33], [12]) without titles, venues, or years in the supplied text, so the recency and reliability of those comparators cannot be independently evaluated ([Anonymous, n.d.](document_1.txt)).
- **Table formatting artifacts**: The source table contains stray characters (for example, "0 0 footnotemark: 0" adjacent to the RNNLM rows) and the result table is labelled "TABLE II" although the text refers to "Table I"; these inconsistencies do not alter the numeric values used here but do indicate imperfect transcription ([Anonymous, n.d.](document_1.txt)).
- **Attribution of gains**: The source attributes the improvements to the proposed tensor-network component by construction, but it does not isolate the effect of individual architectural changes, so the improvement cannot be decomposed into contributions from specific design choices on the basis of this document alone ([Anonymous, n.d.](document_1.txt)).

## Conclusion

Based on the data provided, the introduced models achieve clear and quantifiable improvements over previous models on PTB word-level language modeling. Against their own matched baselines, GRURNTN reduces perplexity by **10.40 points (10.63%)** relative to GRURNN, and LSTMRNTN reduces perplexity by **11.29 points (10.42%)** relative to LSTMRNN, for an average relative gain of approximately **10.53%** ([Anonymous, n.d.](document_1.txt)). Against previously published work, the strongest proposed model, GRURNTN, lowers perplexity by **18.72% to 38.03%** depending on the comparator, including a 20.12-point (18.72%) reduction relative to the best prior published model, DOT(S)-RNN, and reductions of 24.02% or more relative to N-Gram, RNNLM, and SCRNN ([Anonymous, n.d.](document_1.txt)). LSTMRNTN likewise improves on all published models, with margins from 9.79% to 31.23%, and slightly surpasses the paper's own GRURNN baseline by 0.81 PPL ([Anonymous, n.d.](document_1.txt)). The source further reports that GRURNTN maintained a consistently lower validation perplexity throughout training and made faster progress than the other models ([Anonymous, n.d.](document_1.txt)). The improvement is therefore best characterized as **consistent in direction, moderate-to-large in magnitude, and most pronounced for the GRU-based proposed model**, though its generalizability beyond PTB cannot be established from the information supplied.

## References

Anonymous. (n.d.). *document_1.txt* [Unpublished research document]. ([document_1.txt](document_1.txt))