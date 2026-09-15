# Improvement of Gated Recurrent Neural Tensor Networks over Previous Gated RNN Models

## Introduction

The paper *Gated Recurrent Neural Tensor Network* introduces two new recurrent neural network architectures: the Long-Short Term Memory Recurrent Neural Tensor Network (LSTMRNTN) and the Gated Recurrent Unit Recurrent Neural Tensor Network (GRURNTN). These models combine the gating mechanisms of Long Short-Term Memory (LSTM) and Gated Recurrent Unit (GRU) networks with tensor-product operations that create more expressive interactions between current inputs and previous hidden states ([Tjandra et al., n.d.](document_1.txt)). The paper evaluates these proposed models against two previous baseline models, GRURNN and LSTMRNN, on word-level and character-level language modeling using the PennTreeBank corpus ([Tjandra et al., n.d.](document_1.txt)). A third-party research note summarizes the same results and highlights the key improvement figures ([Third-party research note, n.d.](document_2.txt)).

The central question is: how much improvement do the introduced models achieve compared with the previous models? Based on the primary paper, the improvements are consistent and positive in both tasks, but they vary by architecture and task. GRURNTN achieves the strongest overall result, especially in word-level perplexity, while LSTMRNTN provides a solid but smaller improvement over LSTMRNN. This report quantifies those improvements, compares the models, discusses the evaluation setup, and notes an important discrepancy between the primary paper and the third-party summary.

## Evaluation Setup and Baselines

### Baseline Models

The baselines are standard gated recurrent networks. GRURNN uses reset and update gates to control information flow, while LSTMRNN uses input, forget, and output gates together with memory cells ([Tjandra et al., n.d.](document_1.txt)). In both baselines, interactions between the current input and previous hidden state are represented mainly by linear projection, addition, and a nonlinear activation function. This produces first-degree polynomial interactions, which limit the expressiveness of the hidden-layer transition ([Tjandra et al., n.d.](document_1.txt)).

### Proposed Models

The proposed GRURNTN and LSTMRNTN insert a tensor product into the recurrent formulation. In GRURNTN, the tensor product is applied between the current input and the previous hidden layer multiplied by the reset gate, and it is used to compute the candidate hidden layer ([Tjandra et al., n.d.](document_1.txt)). In LSTMRNTN, the tensor product is applied between the current input and the previous hidden layer to compute the candidate memory cell ([Tjandra et al., n.d.](document_1.txt)). The tensor weight is a three-dimensional parameter array, and each slice can capture a specific pattern between the input and hidden representation ([Tjandra et al., n.d.](document_1.txt)). The paper argues that this creates second-degree polynomial interactions, which are more expressive than the first-degree interactions in standard RNNs ([Tjandra et al., n.d.](document_1.txt)).

### Tasks and Metrics

The evaluation uses the PennTreeBank (PTB) corpus, a standard benchmark for statistical language modeling ([Tjandra et al., n.d.](document_1.txt)). Word-level language modeling is measured by perplexity (PPL), where lower is better. Character-level language modeling is measured by bits-per-character (BPC), where lower is also better ([Tjandra et al., n.d.](document_1.txt)). The word-level experiments used 256 hidden units for GRURNTN and LSTMRNTN, 860 for GRURNN, and 740 for LSTMRNN, with 128-dimensional word embeddings ([Tjandra et al., n.d.](document_1.txt)). The character-level experiments used 256 hidden units for the proposed models, 820 for GRURNN, and 600 for LSTMRNN, with 32-dimensional character embeddings ([Tjandra et al., n.d.](document_1.txt)). Importantly, the baselines were constrained to have a similar number of parameters to the proposed models for fair comparison ([Tjandra et al., n.d.](document_1.txt)).

## Character-Level Language Modeling Improvements

On character-level language modeling, both proposed models reduced test BPC relative to their corresponding baselines. GRURNTN reduced BPC from 1.39 to 1.33, an absolute reduction of 0.06 and a relative reduction of 4.32% over GRURNN ([Tjandra et al., n.d.](document_1.txt)). LSTMRNTN reduced BPC from 1.37 to 1.34, an absolute reduction of 0.03 and a relative reduction of 2.22% over LSTMRNN ([Tjandra et al., n.d.](document_1.txt)). The third-party note reports identical character-level numbers: GRURNTN improved by 0.06 absolute / 4.32% relative BPC, and LSTMRNTN improved by 0.03 absolute / 2.22% relative BPC ([Third-party research note, n.d.](document_2.txt)).

| Model | Baseline BPC | Proposed BPC | Absolute Improvement | Relative Improvement |
|---|---:|---:|---:|---:|
| GRURNTN vs. GRURNN | 1.39 | 1.33 | 0.06 | 4.32% |
| LSTMRNTN vs. LSTMRNN | 1.37 | 1.34 | 0.03 | 2.22% |

The table shows that GRURNTN gives the larger character-level improvement. Its 4.32% relative BPC reduction is nearly double the 2.22% relative reduction of LSTMRNTN. The paper also states that GRURNTN slightly outperformed LSTMRNTN, and both proposed models outperformed all baseline models on the character-level task ([Tjandra et al., n.d.](document_1.txt)). The improvement is modest in absolute terms because BPC values are already low, but a 0.06 BPC reduction is meaningful in language modeling benchmarks where small differences can reflect substantial changes in predictive quality.

## Word-Level Language Modeling Improvements

The word-level results show larger relative improvements and a more pronounced advantage for GRURNTN. According to the primary paper, GRURNN had a test PPL of 97.78, and GRURNTN reduced it to 87.38, an absolute reduction of 10.4 and a relative reduction of 10.63% ([Tjandra et al., n.d.](document_1.txt)). LSTMRNN had a test PPL of 108.26, and LSTMRNTN reduced it to 96.97, an absolute reduction of 11.29 and a relative reduction of 10.42% ([Tjandra et al., n.d.](document_1.txt)). The third-party note agrees with the LSTMRNTN word-level result: 108.26 to 96.97, or 11.29 absolute / 10.42% relative PPL ([Third-party research note, n.d.](document_2.txt)).

However, the third-party note reports a different GRURNTN word-level result. It states that GRURNTN reduced PPL from 97.78 to 92.98, which is 4.8 absolute / 4.91% relative PPL over GRURNN ([Third-party research note, n.d.](document_2.txt)). This conflicts with the primary paper’s table and conclusion, which both report 87.38 and a 10.4 absolute / 10.63% relative reduction ([Tjandra et al., n.d.](document_1.txt)). Because the primary paper’s own table and conclusion are internally consistent, the primary figure of 87.38 should be treated as the more reliable value for GRURNTN’s word-level performance. The third-party note may contain a transcription or extraction error for that single number.

| Model | Baseline PPL | Proposed PPL | Absolute Improvement | Relative Improvement | Source |
|---|---:|---:|---:|---:|---|
| GRURNTN vs. GRURNN | 97.78 | 87.38 | 10.4 | 10.63% | Primary paper ([Tjandra et al., n.d.](document_1.txt)) |
| GRURNTN vs. GRURNN | 97.78 | 92.98 | 4.8 | 4.91% | Third-party note ([Third-party research note, n.d.](document_2.txt)) |
| LSTMRNTN vs. LSTMRNN | 108.26 | 96.97 | 11.29 | 10.42% | Both sources agree ([Tjandra et al., n.d.](document_1.txt); [Third-party research note, n.d.](document_2.txt)) |

The primary paper’s word-level table also places the proposed models against several published results. GRURNN is listed at 97.78, LSTMRNN at 108.26, GRURNTN at 87.38, and LSTMRNTN at 96.97 ([Tjandra et al., n.d.](document_1.txt)). Other published results in the table include sRNN at 110.0, DOT(S)-RNN at 107.5, SCRNN at 115, RNNLM without dynamic evaluation at 124.7, RNNLM with dynamic evaluation at 123.2, and N-Gram at 141 ([Tjandra et al., n.d.](document_1.txt)). On this table, GRURNTN is the strongest model, and LSTMRNTN is also competitive with the best previously published results.

## Comparative Interpretation

### GRURNTN versus GRURNN

GRURNTN improves over GRURNN in both tasks. On character-level modeling, it reduces BPC by 0.06 absolute, or 4.32% relative ([Tjandra et al., n.d.](document_1.txt)). On word-level modeling, using the primary paper’s numbers, it reduces PPL by 10.4 absolute, or 10.63% relative ([Tjandra et al., n.d.](document_1.txt)). The word-level gain is the largest improvement reported in the study. The paper describes GRURNTN as outperforming all baseline models and the other proposed model by a large margin on the word-level task ([Tjandra et al., n.d.](document_1.txt)).

### LSTMRNTN versus LSTMRNN

LSTMRNTN also improves over its baseline. On character-level modeling, the reduction is 0.03 absolute BPC, or 2.22% relative ([Tjandra et al., n.d.](document_1.txt)). On word-level modeling, the reduction is 11.29 absolute PPL, or 10.42% relative ([Tjandra et al., n.d.](document_1.txt)). The absolute PPL reduction is actually slightly larger than GRURNTN’s primary-paper reduction of 10.4, but LSTMRNTN starts from a much worse baseline PPL of 108.26, so its final score of 96.97 remains worse than GRURNTN’s 87.38 ([Tjandra et al., n.d.](document_1.txt)). The paper notes that LSTMRNTN’s performance closely resembles the baseline GRURNN, while GRURNTN outperforms all other models ([Tjandra et al., n.d.](document_1.txt)).

### GRURNTN versus LSTMRNTN

Across tasks, GRURNTN is the stronger proposed model. On character-level BPC, GRURNTN achieves 1.33 versus LSTMRNTN’s 1.34, a small but consistent advantage ([Tjandra et al., n.d.](document_1.txt)). On word-level PPL, GRURNTN achieves 87.38 versus LSTMRNTN’s 96.97 under the primary paper’s numbers, a difference of 9.59 PPL points ([Tjandra et al., n.d.](document_1.txt)). This suggests that combining tensor products with GRU-style gating is more effective in this experimental setting than combining tensor products with LSTM-style gating. The paper’s conclusion similarly states that GRURNTN slightly outperformed LSTMRNTN and that both proposed models outperformed the baselines ([Tjandra et al., n.d.](document_1.txt)).

## Why the Improvements Occur

The paper attributes the improvements to two combined advantages. First, gating units help RNNs learn long-term dependencies by remembering and forgetting information across time steps ([Tjandra et al., n.d.](document_1.txt)). Second, tensor products create more direct and expressive interactions between the current input and previous hidden state ([Tjandra et al., n.d.](document_1.txt)). The paper argues that standard RNN transitions are shallow because they use only linear projection, addition, and nonlinearity, while the tensor product introduces second-degree polynomial interactions that can capture more complex relationships ([Tjandra et al., n.d.](document_1.txt)). The backpropagation derivation also shows that each slice of the tensor weight is learned directly from input and hidden-layer values, which allows more specific patterns to be captured than in standard addition-based transitions ([Tjandra et al., n.d.](document_1.txt)).

The parameter-efficient design also matters. The paper uses an asymmetric bilinear form that reduces the number of parameters compared with the original neural tensor network formulation while maintaining input-hidden interaction ([Tjandra et al., n.d.](document_1.txt)). Because the baselines were constrained to similar parameter counts, the improvements are less likely to be explained solely by adding more parameters ([Tjandra et al., n.d.](document_1.txt)). This strengthens the claim that the tensor-product operation itself contributes to the performance gains.

## Reliability, Limitations, and Discrepancies

The primary paper is the most reliable source for the numerical improvements because it contains the model equations, experimental settings, tables, and conclusion ([Tjandra et al., n.d.](document_1.txt)). The third-party note is useful for summarizing the key findings, and it agrees with the character-level results and the LSTMRNTN word-level results ([Third-party research note, n.d.](document_2.txt)). However, its GRURNTN word-level PPL figure of 92.98 conflicts with the primary paper’s 87.38 ([Third-party research note, n.d.](document_2.txt); [Tjandra et al., n.d.](document_1.txt)). For that reason, this report treats the primary paper’s GRURNTN word-level improvement as 10.4 absolute / 10.63% relative PPL, while noting the alternative third-party figure of 4.8 absolute / 4.91% relative PPL.

Several limitations should also be considered. The experiments are limited to the PennTreeBank corpus and two language-modeling tasks, so the results may not generalize to other domains such as speech recognition or machine translation ([Tjandra et al., n.d.](document_1.txt)). The paper proposes future work on stacked RNNs, other tensor operations, speech recognition, and video recognition, which implies that the current evaluation is not exhaustive ([Tjandra et al., n.d.](document_1.txt)). Published comparisons involve different regularization and evaluation settings, so direct comparisons with methods using adaptive noise or dynamic evaluation should be treated cautiously ([Tjandra et al., n.d.](document_1.txt)). Finally, some of the source text is affected by OCR errors, but the key experimental numbers are repeated consistently in the paper’s tables and conclusion ([Tjandra et al., n.d.](document_1.txt)).

## Conclusion

The introduced models achieve clear improvements over the previous GRURNN and LSTMRNN baselines. On character-level language modeling, GRURNTN reduces BPC by 0.06 absolute / 4.32% relative over GRURNN, and LSTMRNTN reduces BPC by 0.03 absolute / 2.22% relative over LSTMRNN ([Tjandra et al., n.d.](document_1.txt)). On word-level language modeling, the primary paper reports that GRURNTN reduces PPL by 10.4 absolute / 10.63% relative over GRURNN, while LSTMRNTN reduces PPL by 11.29 absolute / 10.42% relative over LSTMRNN ([Tjandra et al., n.d.](document_1.txt)). The third-party note agrees with the character-level results and the LSTMRNTN word-level result, but it reports a smaller GRURNTN word-level improvement of 4.8 absolute / 4.91% relative ([Third-party research note, n.d.](document_2.txt)). On the primary evidence, GRURNTN is the best-performing model in the study, and both proposed architectures confirm that combining gating mechanisms with tensor products improves recurrent language modeling over standard gated RNN baselines.

## References

Tjandra, A., Sakti, S., Manurung, R., Adriani, M., & Nakamura, S. (n.d.). *Gated recurrent neural tensor network*. document_1.txt. [Source](document_1.txt)

Third-party research note: Gated recurrent neural tensor network. (n.d.). document_2.txt. [Source](document_2.txt)