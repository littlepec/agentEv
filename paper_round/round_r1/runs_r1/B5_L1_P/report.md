# Improvements Achieved by Gated Recurrent Neural Tensor Networks over Prior Gated RNN Baselines

## Introduction

The paper *Gated Recurrent Neural Tensor Network* introduces two novel recurrent neural network architectures: the Long Short-Term Memory Recurrent Neural Tensor Network (LSTMRNTN) and the Gated Recurrent Unit Recurrent Neural Tensor Network (GRURNTN) (Tjandra et al., 2017). These models combine the gating mechanisms of Long Short-Term Memory (LSTM) and Gated Recurrent Unit (GRU) networks with tensor product operations, aiming to capture long-term dependencies while also enabling more expressive interactions between current inputs and previous hidden states. The authors evaluate their proposed models against baseline gated RNNs—GRURNN and LSTMRNN—on two language modeling tasks using the PennTreeBank (PTB) corpus: character-level language modeling, measured by bits-per-character (BPC), and word-level language modeling, measured by perplexity (PPL). The central question addressed in this report is: how much improvement do the introduced models achieve compared to the previous models? Based on the original paper, the improvements are consistent and quantifiable, with GRURNTN generally delivering the strongest gains, particularly on the word-level task. This report provides a detailed, objective analysis of those improvements, including absolute and relative reductions, parameter-matched comparisons, and a cautious note on a conflicting figure found in a secondary source.

## Overview of Models and Evaluation Setup

The proposed architectures integrate tensor products into the gating equations of GRU and LSTM units. In GRURNTN, the tensor product is applied between the current input and the reset-gated previous hidden state to compute the candidate hidden layer (Tjandra et al., 2017). In LSTMRNTN, the tensor product is applied between the current input and the previous hidden state to compute the candidate cell state (Tjandra et al., 2017). The tensor weights are three-dimensional arrays, and the authors adopt an asymmetric bilinear form to reduce parameter count while preserving input–hidden interactions (Tjandra et al., 2017). Backpropagation through time (BPTT) is used to optimize the tensor weights, with truncated BPTT available for long sequences (Tjandra et al., 2017).

The baselines are standard GRURNN and LSTMRNN models. Crucially, the authors constrained the baselines to have a similar number of parameters as the proposed models for fair comparison (Tjandra et al., 2017). For word-level modeling, GRURNN and GRURNTN had approximately 12 million free parameters, while LSTMRNN and LSTMRNTN had approximately 13 million (Tjandra et al., 2017). For character-level modeling, GRURNN and GRURNTN had about 2.2 million parameters, while LSTMRNN and LSTMRNTN had about 2.6 million (Tjandra et al., 2017). This parameter matching is important because it ensures that observed improvements are not simply due to larger model capacity. The PTB dataset was preprocessed following standard practices, with a vocabulary limited to the 10,000 most common words (Tjandra et al., 2017).

## Character-Level Language Modeling Improvements

On the character-level language modeling task, the proposed models achieved modest but consistent reductions in BPC relative to their respective baselines. Table I in the paper reports test BPC values of 1.39 for GRURNN, 1.37 for LSTMRNN, 1.33 for GRURNTN, and 1.34 for LSTMRNTN (Tjandra et al., 2017). The improvements are as follows:

| Model | Baseline BPC | Proposed BPC | Absolute Reduction | Relative Reduction |
|-------|--------------|--------------|-------------------|-------------------|
| GRURNTN vs. GRURNN | 1.39 | 1.33 | 0.06 | 4.32% |
| LSTMRNTN vs. LSTMRNN | 1.37 | 1.34 | 0.03 | 2.22% |

These figures are directly reported in the paper’s results and conclusion (Tjandra et al., 2017). GRURNTN reduced BPC by 0.06 absolute, or 4.32% relative, over GRURNN. LSTMRNTN reduced BPC by 0.03 absolute, or 2.22% relative, over LSTMRNN. The paper notes that both proposed models produced lower BPC than the baselines from the first epoch to the last epoch, indicating that the advantage is not merely a final-epoch artifact but a consistent trend throughout training (Tjandra et al., 2017).

In terms of model ranking, GRURNTN slightly outperformed LSTMRNTN on this task, achieving 1.33 versus 1.34 (Tjandra et al., 2017). The paper states that both proposed models outperformed all baseline models on character-level language modeling, although this claim should be interpreted within the scope of their own baselines; published results such as LSTMRNN with adaptive noise and dynamic evaluation achieved 1.24–1.26 BPC, but those methods use additional regularization and test-time adaptation not employed in the proposed models (Tjandra et al., 2017). Therefore, the character-level improvements are real and meaningful under matched conditions, but they are relatively small in absolute terms because BPC is already low and the task is highly competitive. A 4.32% relative reduction for GRURNTN is nonetheless notable given the parameter-matched setup.

## Word-Level Language Modeling Improvements

The word-level language modeling task shows substantially larger improvements. The paper reports test PPL values of 97.78 for GRURNN, 108.26 for LSTMRNN, 87.38 for GRURNTN, and 96.97 for LSTMRNTN (Tjandra et al., 2017). The reductions are summarized below:

| Model | Baseline PPL | Proposed PPL | Absolute Reduction | Relative Reduction |
|-------|--------------|--------------|-------------------|-------------------|
| GRURNTN vs. GRURNN | 97.78 | 87.38 | 10.40 | 10.63% |
| LSTMRNTN vs. LSTMRNN | 108.26 | 96.97 | 11.29 | 10.42% |

These values come from Table II and the conclusion of the original paper (Tjandra et al., 2017). GRURNTN reduced perplexity by 10.40 absolute points, or 10.63% relative, over GRURNN. LSTMRNTN reduced perplexity by 11.29 absolute points, or 10.42% relative, over LSTMRNN. The paper describes GRURNTN as the best model in this task, with a consistently lower PPL than the other models (Tjandra et al., 2017). LSTMRNTN improved over its baseline and its performance closely resembles the baseline GRURNN (96.97 vs. 97.78), but GRURNTN outperformed all baselines by a large margin (Tjandra et al., 2017).

It is important to note a discrepancy in the provided secondary source. A third-party research note states that GRURNTN reduced test PPL from 97.78 to 92.98, which is 4.8 absolute / 4.91% relative PPL, over GRURNN ([Third-party research note](document_2.txt)). This conflicts with the original paper’s reported 87.38 and 10.63% relative reduction (Tjandra et al., 2017). In cases of conflict, the primary source—the original peer-reviewed paper—should be prioritized. The original paper’s Table II and conclusion both consistently report 87.38, and the paper’s own analysis emphasizes a “large margin” improvement. Therefore, this report adopts the original paper’s figures. The secondary note may contain a transcription error, refer to a different experimental configuration, or represent an unverified interpretation. Readers should be cautious about relying on the 92.98 figure without further corroboration.

## Comparative Summary Across Tasks

Table 3 consolidates the improvements across both tasks.

| Task | Baseline Model | Proposed Model | Metric | Baseline Score | Proposed Score | Absolute Improvement | Relative Improvement |
|------|----------------|----------------|--------|----------------|----------------|----------------------|----------------------|
| Character-level | GRURNN | GRURNTN | BPC | 1.39 | 1.33 | 0.06 | 4.32% |
| Character-level | LSTMRNN | LSTMRNTN | BPC | 1.37 | 1.34 | 0.03 | 2.22% |
| Word-level | GRURNN | GRURNTN | PPL | 97.78 | 87.38 | 10.40 | 10.63% |
| Word-level | LSTMRNN | LSTMRNTN | PPL | 108.26 | 96.97 | 11.29 | 10.42% |

These results show that the benefits of adding tensor products to gated RNNs are task-dependent. On character-level modeling, where local dependencies dominate and BPC is already low, the relative gains are smaller (2.22%–4.32%). On word-level modeling, where longer-range semantic dependencies are more critical, the relative gains are substantial (10.42%–10.63%). This pattern aligns with the paper’s motivation: tensor products increase the expressive power of input–hidden interactions, which is particularly advantageous when the model must capture complex relationships over longer sequences (Tjandra et al., 2017). GRURNTN was the stronger of the two proposed models overall, achieving the best PPL and the best BPC among the proposed variants. LSTMRNTN still delivered meaningful improvements, but its gains were more modest on the character-level task and its word-level performance only approached the baseline GRURNN.

## Why the Improvements Occur

The paper argues that the improvements stem from combining two complementary ideas. First, gating mechanisms help RNNs learn long-term dependencies by controlling information flow and mitigating vanishing or exploding gradients (Tjandra et al., 2017). Second, tensor products enable second-degree polynomial interactions between the input and hidden layers, whereas standard RNNs rely on first-degree dot products followed by addition (Tjandra et al., 2017). This richer interaction allows each slice of the tensor weight to capture specific patterns between the two vectors (Tjandra et al., 2017). The authors also derive the gradients for the tensor weights and show that each slice is learned more directly from input and hidden layer values than in standard addition-based operations (Tjandra et al., 2017). In other words, the tensor product does not merely add parameters; it changes the functional form of the interaction, enabling the model to represent more complex relationships without requiring a disproportionate increase in parameters. The parameter-matched baselines strengthen the causal interpretation: the improvements are attributable to the architectural change rather than to model size.

## Reliability and Context of the Findings

The primary source is an arXiv preprint (arXiv:1706.02222) authored by Tjandra, Sakti, Manurung, Adriani, and Nakamura (Tjandra et al., 2017). It provides detailed equations, experimental settings, and tables. The experiments use a standard benchmark (PTB) and report both validation trends and test scores. The paper’s conclusion states that both proposed models outperformed the baselines with a similar number of parameters in both tasks (Tjandra et al., 2017). This is a reasonable and well-supported claim. The secondary source, a third-party research note, largely summarizes the paper but introduces at least one numerical inconsistency in the word-level PPL for GRURNTN ([Third-party research note](document_2.txt)). Because the note does not provide additional experimental evidence and conflicts with the primary paper, its discrepant figure should not be treated as authoritative. The rest of the note’s summary—character-level improvements and LSTMRNTN word-level improvements—matches the original paper.

## Conclusion

The introduced models achieve measurable and consistent improvements over the previous gated RNN baselines. On character-level language modeling, GRURNTN reduces BPC by 0.06 absolute (4.32% relative) over GRURNN, while LSTMRNTN reduces BPC by 0.03 absolute (2.22% relative) over LSTMRNN (Tjandra et al., 2017). On word-level language modeling, GRURNTN reduces PPL by 10.40 absolute (10.63% relative) over GRURNN, and LSTMRNTN reduces PPL by 11.29 absolute (10.42% relative) over LSTMRNN (Tjandra et al., 2017). These gains are achieved with parameter-matched baselines, which strengthens the conclusion that the tensor-product gating architecture is the source of improvement. GRURNTN is the strongest overall model, particularly for word-level modeling. The improvements are modest in absolute terms on character-level BPC but substantial in relative terms on word-level PPL. Given the discrepancy in the secondary note, the original paper’s figures should be regarded as the authoritative source. In my assessment, the improvements are meaningful and well-supported for the word-level task, while the character-level gains are real but smaller and should be interpreted within the context of already low BPC and more advanced regularization methods used in other published results.

## References

Tjandra, A., Sakti, S., Manurung, R., Adriani, M., & Nakamura, S. (2017). *Gated Recurrent Neural Tensor Network*. arXiv:1706.02222. https://arxiv.org/abs/1706.02222

Third-party research note: Gated Recurrent Neural Tensor Network. (n.d.). *document_2.txt*. [Link](document_2.txt)