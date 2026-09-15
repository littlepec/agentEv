# Performance Improvements of Gated Recurrent Neural Tensor Networks over Gated RNN Baselines in Language Modeling

## Introduction

The Gated Recurrent Neural Tensor Network paper introduces two new recurrent architectures—the Gated Recurrent Unit Recurrent Neural Tensor Network (GRURNTN) and the Long-Short Term Memory Recurrent Neural Tensor Network (LSTMRNTN)—that combine gating mechanisms with tensor-product operations inside their recurrent formulations ([Tjandra et al., n.d.](document_1.txt)). The central question addressed in this report is how much improvement these introduced models achieve relative to the previous gated recurrent baselines, namely the standard Gated Recurrent Unit RNN (GRURNN) and the Long Short Term Memory RNN (LSTMRNN). The paper evaluates the models on two language-modeling tasks using the PennTreeBank (PTB) corpus: character-level language modeling measured by bits-per-character (BPC) and word-level language modeling measured by perplexity (PPL) ([Tjandra et al., n.d.](document_1.txt)).

The motivation for the proposed architectures is that gating units allow RNNs to learn long-term dependencies and mitigate vanishing or exploding gradients, but they do not by themselves provide a more powerful way to model the relation between the current input and previous hidden layers ([Tjandra et al., n.d.](document_1.txt)). Tensor products, by contrast, introduce second-degree polynomial interactions between the input and hidden layers, compared with the first-degree polynomial interactions produced by standard dot-product-plus-addition formulations ([Tjandra et al., n.d.](document_1.txt)). The paper therefore argues that combining the two concepts should yield both better temporal memory and richer input–hidden interaction, and the experimental results are designed to test that claim ([Tjandra et al., n.d.](document_1.txt)).

## Evaluation Protocol and Comparability

The PTB corpus used in the experiments is a standard benchmark for statistical language modeling and a subset of the WSJ corpus; it was divided into a training set of 930,000 words (sections 0–20), a validation set of 74,000 words (sections 21–22), and a test set of 82,000 words (sections 23–24), with vocabulary limited to the 10,000 most common words and out-of-vocabulary tokens mapped to a special unknown token ([Tjandra et al., n.d.](document_1.txt)). BPC was used for character-level evaluation and PPL for word-level evaluation, with lower values indicating better performance in both cases ([Tjandra et al., n.d.](document_1.txt)).

For the word-level task, the proposed GRURNTN and LSTMRNTN used 256 hidden units, whereas the baselines used 860 (GRURNN) and 740 (LSTMRNN) hidden units, with 128-dimensional word embeddings ([Tjandra et al., n.d.](document_1.txt)). For the character-level task, the proposed models again used 256 hidden units, while the baselines used 820 (GRURNN) and 600 (LSTMRNN, reported in the source as an apparent typographical repetition of the proposed model name), with 32-dimensional character embeddings ([Tjandra et al., n.d.](document_1.txt)). Dropout probabilities were set to 0.5 for the proposed word-level models and 0.6 for the word-level baselines, and to 0.25 for the character-level experiments ([Tjandra et al., n.d.](document_1.txt)). All models were trained with AdaGrad, mini-batches of 15 sentences, a learning rate decay factor of 0.5 when development cost increased, gradient rescaling when the norm exceeded 5, and orthogonal weight initialization ([Tjandra et al., n.d.](document_1.txt)).

Crucially for the interpretation of the results, the authors constrained the baseline GRURNN to have a similar number of parameters to the GRURNTN model and applied the same constraint to the LSTMRNN baseline relative to LSTMRNTN ([Tjandra et al., n.d.](document_1.txt)). This parameter-matching design is important because it implies that the observed gains stem from the architectural addition of the tensor product rather than from simply allocating more learnable capacity to the proposed models. It should be noted, however, that the third-party research note characterizing this work states that the proposed models outperformed the baselines "with roughly twice the number of parameters" ([Third-party research note, n.d.](document_2.txt)), which conflicts with the primary source's explicit statement that parameter counts were matched and that the proposed models outperformed baselines "with a similar number of parameters" ([Tjandra et al., n.d.](document_1.txt)). Given this contradiction, the primary paper is the more reliable source, and the evidence indicates that the comparison was parameter-controlled.

## Character-Level Language Modeling Improvements

On the PTB test set for character-level language modeling, the proposed tensor-based models reduced BPC relative to their respective gated baselines. GRURNTN reduced BPC from 1.39 to 1.33, an absolute reduction of 0.06, corresponding to a 4.32% relative improvement over GRURNN ([Tjandra et al., n.d.](document_1.txt)). LSTMRNTN reduced BPC from 1.37 to 1.34, an absolute reduction of 0.03, corresponding to a 2.22% relative improvement over LSTMRNN ([Tjandra et al., n.d.](document_1.txt)). The results are summarized in Table 1.

**Table 1. Character-level language modeling results on the PennTreeBank test set (BPC; lower is better)**

| Model | Type | Test BPC | Absolute change vs. baseline | Relative change vs. baseline |
|---|---|---|---|---|
| GRURNN | Baseline | 1.39 | — | — |
| GRURNTN | Proposed | 1.33 | −0.06 | −4.32% |
| LSTMRNN | Baseline | 1.37 | — | — |
| LSTMRNTN | Proposed | 1.34 | −0.03 | −2.22% |

Source: ([Tjandra et al., n.d.](document_1.txt)).

Beyond the final test-set scores, the paper reports that both proposed models produced lower BPC than the baselines from the first epoch to the last, and that GRURNTN improved faster than LSTMRNTN, with the two converging to similar BPC values in the final epoch ([Tjandra et al., n.d.](document_1.txt)). This convergence-speed observation matters because it suggests the tensor product not only improves the final solution quality but also accelerates optimization relative to the gated baselines. The paper further states that GRURNTN slightly outperformed LSTMRNTN and that both proposed models outperformed all baseline models on the character-level task ([Tjandra et al., n.d.](document_1.txt)).

## Word-Level Language Modeling Improvements

The word-level results are considerably larger in both absolute and relative terms. GRURNTN reduced perplexity from 97.78 to 87.38, an absolute reduction of 10.4, equivalent to a 10.63% relative improvement over GRURNN ([Tjandra et al., n.d.](document_1.txt)). LSTMRNTN reduced perplexity from 108.26 to 96.97, an absolute reduction of 11.29, equivalent to a 10.42% relative improvement over LSTMRNN ([Tjandra et al., n.d.](document_1.txt)). These results are summarized in Table 2.

**Table 2. Word-level language modeling results on the PennTreeBank test set (PPL; lower is better)**

| Model | Type | Test PPL | Absolute change vs. baseline | Relative change vs. baseline |
|---|---|---|---|---|
| GRURNN | Baseline | 97.78 | — | — |
| GRURNTN | Proposed | 87.38 | −10.40 | −10.63% |
| LSTMRNN | Baseline | 108.26 | — | — |
| LSTMRNTN | Proposed | 96.97 | −11.29 | −10.42% |

Source: ([Tjandra et al., n.d.](document_1.txt)).

Two observations are especially important here. First, although LSTMRNTN achieved a larger absolute PPL reduction than GRURNTN (11.29 versus 10.40), the relative reductions are nearly identical (10.42% versus 10.63%) because the LSTMRNN baseline started from a substantially worse perplexity of 108.26 ([Tjandra et al., n.d.](document_1.txt)). Second, the paper notes that LSTMRNTN's final performance "closely resembles" the baseline GRURNN, while GRURNTN outperformed all baseline models as well as the other proposed model "by a large margin" ([Tjandra et al., n.d.](document_1.txt)). In practical terms, the LSTM-plus-tensor model essentially caught up to the untensored GRU baseline, whereas the GRU-plus-tensor model moved clearly beyond every other model evaluated.

## Head-to-Head Comparison of the Proposed Models

Comparing the two proposed architectures directly sharpens the picture of where the tensor product pays off most. On the character-level task the two models are nearly indistinguishable, with GRURNTN at 1.33 BPC and LSTMRNTN at 1.34 BPC, a difference of 0.01 BPC (approximately 0.75% relative) ([Tjandra et al., n.d.](document_1.txt)). On the word-level task, however, the gap is much wider: GRURNTN at 87.38 PPL versus LSTMRNTN at 96.97 PPL, a difference of 9.59 PPL, or roughly 9.89% relative ([Tjandra et al., n.d.](document_1.txt)). Table 3 consolidates this comparison.

**Table 3. Head-to-head comparison of the two proposed models**

| Metric | GRURNTN | LSTMRNTN | GRURNTN advantage |
|---|---|---|---|
| Test BPC (character-level) | 1.33 | 1.34 | 0.01 BPC (≈0.75% relative) |
| Test PPL (word-level) | 87.38 | 96.97 | 9.59 PPL (≈9.89% relative) |

Source: ([Tjandra et al., n.d.](document_1.txt)).

The asymmetry between the two tasks suggests that the GRU-based tensor architecture was the stronger and more consistent beneficiary of the tensor product in this study, particularly for word-level modeling ([Tjandra et al., n.d.](document_1.txt)).

## Comparison with Published External Results

The paper also positions its results against previously published models. On word-level PPL, the proposed GRURNTN achieved 87.38, which is lower than the next-best listed external system, DOT(S)-RNN at 107.5, and lower than sRNN at 110.0, SCRNN at 115, RNNLM with and without dynamic evaluation at 123.2 and 124.7 respectively, and the N-Gram baseline at 141 ([Tjandra et al., n.d.](document_1.txt)). Relative to DOT(S)-RNN, GRURNTN represents a reduction of 20.12 PPL, or about 18.72% relative; relative to sRNN, the reduction is 22.62 PPL, or about 20.56% relative. LSTMRNTN's 96.97 PPL likewise exceeds sRNN (110.0) and DOT(S)-RNN (107.5) by 13.03 and 10.53 PPL respectively, corresponding to roughly 11.85% and 9.80% relative reductions ([Tjandra et al., n.d.](document_1.txt)).

On character-level BPC, the picture is more nuanced. GRURNTN at 1.33 and LSTMRNTN at 1.34 beat NNLM (1.57), BPTT-RNN (1.42), sRNN (1.39), and DOT(S)-RNN (1.37), but they do not beat HF-MRNN at 1.24 or LSTMRNN with adaptive noise and dynamic evaluation at 1.26 ([Tjandra et al., n.d.](document_1.txt)). Importantly, the authors state that their baseline and proposed model experiments did not use dynamic evaluation, so comparisons against dynamically evaluated systems are not strictly like-for-like ([Tjandra et al., n.d.](document_1.txt)). This qualification is essential for an objective reading: the tensor-based models deliver clear, consistent gains over their own hyperparameter-matched baselines, but they do not establish a new state of the art on character-level BPC across all published approaches.

**Table 4. Selected published word-level PPL results compared with proposed models**

| Model | Test PPL |
|---|---|
| N-Gram | 141 |
| RNNLM (w/o dynamic evaluation) | 124.7 |
| RNNLM (w/ dynamic evaluation) | 123.2 |
| SCRNN | 115 |
| sRNN | 110.0 |
| DOT(S)-RNN | 107.5 |
| LSTMRNN (baseline) | 108.26 |
| LSTMRNTN (proposed) | 96.97 |
| GRURNN (baseline) | 97.78 |
| GRURNTN (proposed) | 87.38 |

Source: ([Tjandra et al., n.d.](document_1.txt)).

## Why the Improvements Occur

The paper attributes the gains to two complementary mechanisms. First, gating units allow the network to remember and forget information across time steps, which helps it learn long-term dependencies and recursively backpropagate error without suffering from vanishing or exploding gradients ([Tjandra et al., n.d.](document_1.txt)). Second, replacing the standard linear projection and addition between input and hidden layers with a tensor product introduces second-degree polynomial interactions, increasing the expressiveness of the hidden-layer representation and allowing each tensor slice to capture a specific pattern of interaction between the input and hidden states ([Tjandra et al., n.d.](document_1.txt)). The paper also reduces the parameter cost of the tensor formulation by adopting an asymmetric bilinear form, which preserves input–hidden interaction while reducing the number of parameters relative to the original neural tensor network formulation ([Tjandra et al., n.d.](document_1.txt)).

From a methodological standpoint, the parameter-matching constraint on baselines is the strongest argument that the gains are architectural rather than capacity-driven ([Tjandra et al., n.d.](document_1.txt)). However, several limitations temper the strength of the conclusions. The evaluation covers a single dataset and a single task family (language modeling); the proposed and baseline models used different hidden-unit counts and different dropout probabilities; and no statistical significance testing is reported ([Tjandra et al., n.d.](document_1.txt)). The reported improvements should therefore be read as consistent and meaningful within this experimental setting, but not as universally established effect sizes.

## Summary of Improvement Magnitudes

**Table 5. Consolidated improvement summary**

| Task | Metric | Baseline | Proposed | Absolute improvement | Relative improvement |
|---|---|---|---|---|---|
| Character-level | BPC | GRURNN 1.39 | GRURNTN 1.33 | 0.06 | 4.32% |
| Character-level | BPC | LSTMRNN 1.37 | LSTMRNTN 1.34 | 0.03 | 2.22% |
| Word-level | PPL | GRURNN 97.78 | GRURNTN 87.38 | 10.40 | 10.63% |
| Word-level | PPL | LSTMRNN 108.26 | LSTMRNTN 96.97 | 11.29 | 10.42% |

Source: ([Tjandra et al., n.d.](document_1.txt)).

Averaging across the four baseline-versus-proposed comparisons yields a mean relative improvement of approximately 6.90%, but this average masks substantial variation: the tensor product delivers roughly a 10.5% relative perplexity reduction at the word level but only a 2.22%–4.32% relative BPC reduction at the character level ([Tjandra et al., n.d.](document_1.txt)). The pattern suggests that the benefits of tensor-product interactions are most pronounced when the model must capture longer-range dependencies among relatively sparse, higher-level units (words) rather than short-range character sequences.

## Conclusion

Based on the evidence in the primary source, the introduced models achieve consistent and quantifiable improvements over the previous gated RNN baselines. GRURNTN reduces character-level BPC by 0.06 absolute (4.32% relative) and word-level PPL by 10.40 absolute (10.63% relative) relative to GRURNN, while LSTMRNTN reduces character-level BPC by 0.03 absolute (2.22% relative) and word-level PPL by 11.29 absolute (10.42% relative) relative to LSTMRNN ([Tjandra et al., n.d.](document_1.txt)). The improvements are observed not only in final test scores but also in per-epoch validation performance, with both proposed models outperforming their baselines from the first epoch onward ([Tjandra et al., n.d.](document_1.txt)).

My assessment is that the word-level gains are the most convincing result in the paper: they are large in relative terms, consistent across both gated architectures, and obtained under a parameter-matched comparison, which strengthens the causal interpretation that the tensor product—not extra capacity—is responsible ([Tjandra et al., n.d.](document_1.txt)). The character-level gains are real but modest, and the proposed models do not surpass the best published character-level results such as HF-MRNN (1.24 BPC) or dynamically evaluated LSTMRNN (1.26 BPC) ([Tjandra et al., n.d.](document_1.txt)). Among the two proposed architectures, GRURNTN is the stronger model overall, matching LSTMRNTN closely on character-level BPC (1.33 versus 1.34) while substantially outperforming it on word-level PPL (87.38 versus 96.97) ([Tjandra et al., n.d.](document_1.txt)). The most defensible conclusion, therefore, is that combining gating with tensor products yields reliable but task-dependent gains, with the largest benefit appearing in word-level language modeling and the GRU-based variant emerging as the best-performing configuration in this study.

## References

Third-party research note: Gated recurrent neural tensor network. (n.d.). *document_2.txt*.

Tjandra, A., Sakti, S., Manurung, R., Adriani, M., & Nakamura, S. (n.d.). *Gated recurrent neural tensor network*. document_1.txt.