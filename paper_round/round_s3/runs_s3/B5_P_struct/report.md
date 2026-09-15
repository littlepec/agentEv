# How Much Improvement Do the Introduced Gated Recurrent Neural Tensor Network Models Achieve?

## Introduction and Scope

The introduced models in the provided material are the Gated Recurrent Unit Recurrent Neural Tensor Network (GRURNTN) and the Long Short-Term Memory Recurrent Neural Tensor Network (LSTMRNTN). These models are compared against two previous baseline architectures: the Gated Recurrent Unit Recurrent Neural Network (GRURNN) and the Long Short-Term Memory Recurrent Neural Network (LSTMRNN) ([Document 1](document_1.txt)). The evaluation covers two language-modeling tasks: character-level language modeling on the Penn Treebank (PTB) dataset, measured by bits-per-character (BPC), and word-level language modeling on PTB, measured by perplexity (PPL) ([Document 1](document_1.txt); [Document 2](document_2.txt)). Lower BPC and lower PPL both indicate better performance.

The core architectural claim is that adding a tensor product operation to gated recurrent models improves their ability to model interactions between the current input and previous hidden-layer representations ([Document 1](document_1.txt)). The paper argues that gating alone helps with long-term dependencies and gradient flow, but it does not by itself provide a more powerful way to model the relation between the current input and previous hidden states ([Document 1](document_1.txt)). By using a tensor product, the proposed models introduce second-degree polynomial interactions, whereas standard recurrent models rely on first-degree polynomial interactions through dot products followed by addition ([Document 1](document_1.txt)). The key question is therefore how much empirical improvement this combination of gating and tensor products delivers over the previous GRURNN and LSTMRNN baselines.

## Character-Level Language Modeling Improvements

On PTB character-level language modeling, both proposed models reduced test BPC relative to their corresponding baselines. GRURNTN reduced BPC from 1.39 to 1.33, which is an absolute improvement of 0.06 and a relative improvement of 4.32% over GRURNN ([Document 1](document_1.txt); [Document 2](document_2.txt)). LSTMRNTN reduced BPC from 1.37 to 1.34, which is an absolute improvement of 0.03 and a relative improvement of 2.22% over LSTMRNN ([Document 1](document_1.txt); [Document 2](document_2.txt)). These figures are consistent across the primary paper content and the third-party research note ([Document 2](document_2.txt)).

### Character-Level Test BPC Comparison

| Model | Test BPC | Improvement over baseline |
|---|---:|---:|
| NNLM | 1.57 | — |
| BPTT-RNN | 1.42 | — |
| HF-MRNN | 1.41 | — |
| sRNN | 1.41 | — |
| DOT(S)-RNN | 1.39 | — |
| LSTMRNN with adaptive noise, without dynamic evaluation | 1.26 | — |
| LSTMRNN with adaptive noise, with dynamic evaluation | 1.24 | — |
| GRURNN (baseline) | 1.39 | — |
| LSTMRNN (baseline) | 1.37 | — |
| GRURNTN (proposed) | 1.33 | 0.06 absolute / 4.32% relative over GRURNN |
| LSTMRNTN (proposed) | 1.34 | 0.03 absolute / 2.22% relative over LSTMRNN |

The table shows that GRURNTN and LSTMRNTN improved over their directly corresponding baselines ([Document 1](document_1.txt)). The paper also reports that both proposed models produced lower BPC than the baseline models from the first epoch to the last epoch on the validation set ([Document 1](document_1.txt)). In addition, GRURNTN made faster and quicker progress than LSTMRNTN and converged into a similar BPC in the last epoch, while both proposed models remained better than their baselines throughout training ([Document 1](document_1.txt)).

However, the broader benchmark context is more nuanced. Although the paper states that both proposed models outperformed all baseline models on character-level language modeling, the same table lists two published LSTMRNN variants with adaptive noise and dynamic evaluation at 1.26 and 1.24 BPC, which are lower than the proposed models’ 1.33 and 1.34 ([Document 1](document_1.txt)). A careful reading therefore suggests that the strongest defensible claim is that GRURNTN and LSTMRNTN outperformed the directly implemented GRURNN and LSTMRNN baselines, not that they achieved state-of-the-art results against every published system in the table ([Document 1](document_1.txt)). The character-level gains are real but relatively modest in absolute terms, ranging from 0.03 to 0.06 BPC.

## Word-Level Language Modeling Improvements

The word-level language modeling task provides the largest and most consequential reported improvements. In the primary source, GRURNTN reduced test PPL from 97.78 to 87.38, an absolute reduction of 10.4 PPL and a relative reduction of 10.63% over GRURNN ([Document 1](document_1.txt)). LSTMRNTN reduced test PPL from 108.26 to 96.97, an absolute reduction of 11.29 PPL and a relative reduction of 10.42% over LSTMRNN ([Document 1](document_1.txt); [Document 2](document_2.txt)). The primary paper further reports that GRURNTN consistently had lower PPL than the other models and was the best model in that task ([Document 1](document_1.txt)). LSTMRNTN improved over LSTMRNN, and its performance closely resembled the baseline GRURNN, although 96.97 is still slightly lower than GRURNN’s 97.78 ([Document 1](document_1.txt)).

### Word-Level Test PPL Comparison

| Model | Test PPL | Improvement over baseline |
|---|---:|---:|
| N-Gram | 141 | — |
| RNNLM without dynamic evaluation | 124.7 | — |
| RNNLM with dynamic evaluation | 123.2 | — |
| SCRNN | 115 | — |
| sRNN | 110.0 | — |
| DOT(S)-RNN | 107.5 | — |
| GRURNN (baseline) | 97.78 | — |
| LSTMRNN (baseline) | 108.26 | — |
| GRURNTN (proposed) | 87.38 | 10.4 absolute / 10.63% relative over GRURNN |
| LSTMRNTN (proposed) | 96.97 | 11.29 absolute / 10.42% relative over LSTMRNN |

These results indicate that the proposed tensor-based gated models delivered substantial word-level improvements over the previous GRURNN and LSTMRNN architectures ([Document 1](document_1.txt)). GRURNTN was especially strong: its 87.38 PPL is lower than all other listed models in the table, including the published N-Gram, RNNLM, SCRNN, sRNN, and DOT(S)-RNN results ([Document 1](document_1.txt)). LSTMRNTN’s 96.97 PPL also outperformed its LSTMRNN baseline and slightly outperformed the GRURNN baseline ([Document 1](document_1.txt)). Thus, on word-level language modeling, the introduced models achieved both statistically meaningful relative reductions and, for GRURNTN, a leading position among the provided comparisons.

### Discrepancy in the Third-Party Research Note

A notable discrepancy exists between the primary source and the third-party research note. The third-party note states that GRURNTN reduced test PPL from 97.78 to 92.98, which is 4.8 absolute and 4.91% relative PPL improvement over GRURNN ([Document 2](document_2.txt)). The primary source, however, reports GRURNTN at 87.38 PPL and a 10.4 absolute / 10.63% relative improvement ([Document 1](document_1.txt)). Because the primary source contains the underlying results table and a matching narrative statement, its figure of 87.38 PPL is the better-supported value for the report’s main numerical assessment ([Document 1](document_1.txt)). The third-party note’s 92.98 PPL should be treated as a secondary or possibly erroneous transcription ([Document 2](document_2.txt)). If the third-party figure were used, GRURNTN’s word-level improvement would still be positive but only about half as large in absolute PPL terms.

## Comparative Interpretation and Fairness of Comparison

A central reason these improvements are credible is that the paper attempted to keep the comparisons fair in terms of parameter counts. For word-level language modeling, GRURNN and GRURNTN had about 12 million free parameters, while LSTMRNN and LSTMRNTN had about 13 million free parameters ([Document 1](document_1.txt)). For character-level language modeling, GRURNN and GRURNTN had about 2.2 million free parameters, while LSTMRNN and LSTMRNTN had about 2.6 million free parameters ([Document 1](document_1.txt)). The paper explicitly states that the baseline GRURNN was constrained to have a similar number of parameters as GRURNTN, and the baseline LSTMRNN was constrained similarly to LSTMRNTN ([Document 1](document_1.txt)). Therefore, the reported improvements are unlikely to be explained solely by the proposed models being much larger than their baselines.

The architecture also explains why improvements should be expected. The tensor product operation is applied between the current input and previous hidden layer, multiplied by the reset gates for calculating the current candidate hidden-layer values, and parameterized by tensor weights ([Document 1](document_1.txt)). This increases model expressiveness through second-degree polynomial interactions rather than the first-degree interactions of standard dot-product-plus-addition recurrent architectures ([Document 1](document_1.txt)). The paper’s derivations also suggest that each slice of the tensor weight is learned more directly from input and hidden-layer values than in standard addition operations ([Document 1](document_1.txt)). The gating mechanism contributes the ability to learn long-term dependencies and to backpropagate error recursively without suffering from vanishing or exploding gradient problems ([Document 1](document_1.txt)). Combining these two mechanisms is the core reason for the observed gains.

### Consolidated Improvement Summary

| Proposed model | Baseline | Task | Metric | Baseline score | Proposed score | Absolute improvement | Relative improvement |
|---|---|---|---:|---:|---:|---:|---:|
| GRURNTN | GRURNN | Character-level | BPC | 1.39 | 1.33 | 0.06 | 4.32% |
| LSTMRNTN | LSTMRNN | Character-level | BPC | 1.37 | 1.34 | 0.03 | 2.22% |
| GRURNTN | GRURNN | Word-level | PPL | 97.78 | 87.38 (primary) | 10.40 | 10.63% |
| GRURNTN | GRURNN | Word-level | PPL | 97.78 | 92.98 (third-party) | 4.80 | 4.91% |
| LSTMRNTN | LSTMRNN | Word-level | PPL | 108.26 | 96.97 | 11.29 | 10.42% |

The consolidated table shows a clear pattern: the introduced models achieved their largest relative improvements on word-level PPL, where both GRURNTN and LSTMRNTN produced roughly 10% relative reductions under the primary source’s numbers ([Document 1](document_1.txt)). Character-level improvements were smaller in relative terms, at 4.32% for GRURNTN and 2.22% for LSTMRNTN ([Document 1](document_1.txt)). Across tasks, GRURNTN was the stronger proposed model: it achieved 1.33 BPC versus LSTMRNTN’s 1.34, and 87.38 PPL versus LSTMRNTN’s 96.97 ([Document 1](document_1.txt)). LSTMRNTN nevertheless improved substantially over its own baseline on the word-level task, reducing PPL by 11.29 absolute points ([Document 1](document_1.txt)).

## Benchmark Context and Limitations

The improvements should be interpreted within the specific benchmark tables provided. On word-level PTB, GRURNTN’s 87.38 PPL is clearly better than N-Gram at 141, RNNLM without dynamic evaluation at 124.7, RNNLM with dynamic evaluation at 123.2, SCRNN at 115, sRNN at 110.0, and DOT(S)-RNN at 107.5 ([Document 1](document_1.txt)). LSTMRNTN’s 96.97 PPL also beats those published results and beats the GRURNN baseline, though it is not as strong as GRURNTN ([Document 1](document_1.txt)). On character-level PTB, the situation is less dominant: GRURNTN’s 1.33 BPC and LSTMRNTN’s 1.34 BPC beat NNLM, BPTT-RNN, HF-MRNN, sRNN, DOT(S)-RNN, GRURNN, and LSTMRNN, but they do not beat the two adaptive-noise LSTMRNN variants at 1.26 and 1.24 BPC ([Document 1](document_1.txt)). This means the answer to “how much improvement” depends on the comparison set: the introduced models improve clearly over the previous GRURNN and LSTMRNN baselines, but they do not universally dominate every previously published result on character-level language modeling.

Another limitation is that the third-party research note introduces a conflicting GRURNTN word-level PPL value of 92.98 instead of 87.38 ([Document 2](document_2.txt)). This discrepancy means that any summary should explicitly state which source is being used. The primary source’s table and narrative both support 87.38 PPL and a 10.4 absolute / 10.63% relative improvement, so that is the most reliable figure for the primary paper’s reported result ([Document 1](document_1.txt)). The third-party note remains useful as corroboration for the direction and for the LSTMRNTN numbers, but it should not override the primary source on the specific GRURNTN word-level PPL ([Document 2](document_2.txt)).

## Conclusion

The introduced GRURNTN and LSTMRNTN models achieved consistent improvements over the previous GRURNN and LSTMRNN models on both character-level and word-level PTB language modeling. On character-level BPC, GRURNTN improved by 0.06 absolute and 4.32% relative over GRURNN, while LSTMRNTN improved by 0.03 absolute and 2.22% relative over LSTMRNN ([Document 1](document_1.txt); [Document 2](document_2.txt)). On word-level PPL, the primary source reports that GRURNTN improved by 10.4 absolute and 10.63% relative over GRURNN, and LSTMRNTN improved by 11.29 absolute and 10.42% relative over LSTMRNN ([Document 1](document_1.txt)). A third-party note reports a smaller GRURNTN word-level improvement of 4.8 absolute and 4.91% relative, but the primary source’s 87.38 PPL is better supported and should be preferred ([Document 1](document_1.txt); [Document 2](document_2.txt)).

Overall, the strongest evidence indicates that the tensor-product-plus-gating design delivers meaningful gains, especially on word-level perplexity, where both proposed models reduce error by roughly 10% relative under the primary results. GRURNTN is the stronger of the two introduced models in the provided comparisons, while LSTMRNTN provides a large improvement over its own LSTM baseline and nearly matches the GRURNN baseline on word-level PPL. The gains are not uniform across all benchmarks, since character-level performance remains behind adaptive-noise LSTM variants in the same table, but relative to the specific previous models being challenged, both GRURNTN and LSTMRNTN achieve clear and measurable improvements ([Document 1](document_1.txt)).

## References

Document 1. (n.d.). *Source: document_1.txt*. document_1.txt

Document 2. (n.d.). *Third-party research note: Gated Recurrent Neural Tensor Network*. document_2.txt