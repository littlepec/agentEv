# Improvements Achieved by Gated Recurrent Neural Tensor Networks over Prior Gated RNN Baselines

## Introduction

The Gated Recurrent Neural Tensor Network paper by Tjandra et al. (2017) introduces two new recurrent architectures that attempt to unify two previously separate ideas in sequence modeling: the gating mechanism used in Long Short-Term Memory (LSTM) and Gated Recurrent Unit (GRU) networks, and the tensor product used in Recursive Neural Tensor Networks ([Tjandra et al., 2017](document_1.txt)). The central empirical question posed by the work is straightforward: does embedding a tensor product inside the gated recurrence of an already-strong gated RNN produce measurable gains on standard language-modeling benchmarks? The answer reported by the authors is affirmative on both tasks examined — word-level language modeling measured by perplexity (PPL) and character-level language modeling measured by bits-per-character (BPC) — although the magnitude of the gains differs substantially by task and by which of the two proposed models is considered ([Tjandra et al., 2017](document_1.txt)).

This report quantifies those improvements, places them in the context of the wider set of published baselines reported in the same paper, and evaluates the credibility and internal consistency of the reported figures using both the primary paper and an accompanying third-party research note ([Document 2: Third-party research note](document_2.txt)).

## The Models Under Comparison

### Baseline Models: GRURNN and LSTMRNN

The comparison targets two established gated recurrent architectures. The LSTM RNN, originally proposed by Hochreiter and Schmidhuber, employs three gates (input, forget, and output) together with a memory cell, allowing the network to retain useful information and discard irrelevant information across time steps ([Tjandra et al., 2017](document_1.txt)). The GRU RNN simplifies this design by removing the separate memory cell and reducing the number of gates to two — a reset gate and an update gate — while reportedly matching LSTM performance and sometimes converging faster ([Tjandra et al., 2017](document_1.txt)). These two models, labeled GRURNN and LSTMRNN, serve as the direct baselines.

### Proposed Models: GRURNTN and LSTMRNTN

The proposed architectures add a tensor product — a bilinear, second-degree polynomial interaction — inside the gated recurrence. In GRURNTN, the tensor product is applied between the current input and the reset-gated previous hidden layer when computing the candidate hidden state; in LSTMRNTN, it is applied between the current input and the previous hidden layer when computing the candidate memory cell ([Tjandra et al., 2017](document_1.txt)). An asymmetric bilinear formulation is used to limit the parameter growth relative to the full neural tensor network formulation ([Tjandra et al., 2017](document_1.txt)). The stated rationale is that standard RNNs model input–hidden interactions only through linear projection plus addition followed by a nonlinearity, whereas the tensor product yields a more expressive and direct interaction ([Tjandra et al., 2017](document_1.txt)).

## Experimental Design and Fairness Controls

All experiments used the PennTreeBank (PTB) corpus with standard preprocessing: sections 0–20 for training (930,000 words), sections 21–22 for validation (74,000 words), and sections 23–24 for testing (82,000 words), with a vocabulary limited to the 10,000 most frequent words and all others mapped to a `<unk>` token ([Tjandra et al., 2017](document_1.txt)). Optimization used AdaGrad with mini-batches of 15 sentences, a learning-rate decay factor of 0.5 triggered by development-set cost increases, gradient rescaling when the norm exceeded 5, and orthogonal weight initialization ([Tjandra et al., 2017](document_1.txt)).

Critically for the validity of the comparison, the baselines were constrained to have a similar number of free parameters to the proposed models ([Tjandra et al., 2017](document_1.txt)). For word-level modeling, the proposed models used 256 hidden units with 128-dimensional word embeddings, while GRURNN used 860 hidden units and LSTMRNN used 740; total parameters were approximately 12 million for GRURNN and GRURNTN and approximately 13 million for LSTMRNN and LSTMRNTN ([Tjandra et al., 2017](document_1.txt)). For character-level modeling, the proposed models again used 256 hidden units with 32-dimensional character embeddings, against 820 hidden units for GRURNN and 600 for the LSTM variant, with roughly 2.2 million parameters for GRURNN and GRURNTN and 2.6 million for the LSTM pair ([Tjandra et al., 2017](document_1.txt)). This parameter-matching design is important: it means the reported gains reflect architectural expressiveness rather than a simple increase in model capacity.

## Character-Level Language Modeling Results

On the PTB character-level task, the proposed models produced lower BPC than their corresponding baselines in every epoch examined, from the first epoch to the last ([Tjandra et al., 2017](document_1.txt)). The test-set outcomes were as follows:

| Model | Test BPC | Absolute Change vs. Baseline | Relative Change vs. Baseline |
|---|---|---|---|
| GRURNN (baseline) | 1.39 | — | — |
| GRURNTN (proposed) | 1.33 | −0.06 | −4.32% |
| LSTMRNN (baseline) | 1.37 | — | — |
| LSTMRNTN (proposed) | 1.34 | −0.03 | −2.22% |

Derived from Tjandra et al. (2017) ([Tjandra et al., 2017](document_1.txt)).

The GRU-based variant therefore gained roughly twice the relative improvement of the LSTM-based variant on this task. The authors further note that GRURNTN progressed faster during training than LSTMRNTN and converged to a comparable BPC by the final epoch, and that GRURNTN slightly outperformed LSTMRNTN overall on character-level modeling ([Tjandra et al., 2017](document_1.txt)).

## Word-Level Language Modeling Results

The word-level task produced considerably larger improvements, which is notable because perplexity is the more widely reported language-modeling metric for PTB.

| Model | Test PPL | Absolute Change vs. Baseline | Relative Change vs. Baseline |
|---|---|---|---|
| GRURNN (baseline) | 97.78 | — | — |
| GRURNTN (proposed) | 87.38 | −10.40 | −10.63% |
| LSTMRNN (baseline) | 108.26 | — | — |
| LSTMRNTN (proposed) | 96.97 | −11.29 | −10.42% |

Derived from Tjandra et al. (2017) ([Tjandra et al., 2017](document_1.txt)).

Two details deserve emphasis. First, although LSTMRNTN achieved the larger *absolute* reduction (11.29 PPL versus 10.40 PPL), GRURNTN achieved the marginally larger *relative* reduction (10.63% versus 10.42%) because it started from a much better baseline ([Tjandra et al., 2017](document_1.txt)). Second, and more consequentially, the modified LSTM (96.97) still did not surpass the unmodified GRU baseline (97.78) on an absolute basis, meaning the tensor enhancement narrowed but did not close the gap between the LSTM and GRU families on this task ([Tjandra et al., 2017](document_1.txt)). The authors acknowledge this directly, observing that LSTMRNTN's performance "closely resembles the baseline GRURNN," while GRURNTN "outperformed all the baseline models as well as the other models by a large margin" ([Tjandra et al., 2017](document_1.txt)).

## Position Relative to Published Benchmarks

The value of these gains depends on where the enhanced models land relative to the broader literature. The paper's comparison tables provide that context.

On word-level PPL, the published baselines listed include N-Gram at 141, RNNLM without dynamic evaluation at 124.7 and with it at 123.2, SCRNN at 115, sRNN at 110.0, and DOT(S)-RNN at 107.5 ([Tjandra et al., 2017](document_1.txt)). GRURNTN's 87.38 is therefore the lowest perplexity among every model tabulated, improving on the previously best listed system (DOT(S)-RNN, 107.5) by approximately 20.1 PPL, or roughly 18.7% in relative terms. This is the strongest single result in the paper.

On character-level BPC, however, the picture is more mixed. Published results include NNLM at 1.57, BPTT-RNN at 1.42, HF-MRNN at 1.41, sRNN at 1.41, DOT(S)-RNN at 1.39, and an LSTM RNN with adaptive noise regularization at 1.26 without dynamic evaluation and 1.24 with it ([Tjandra et al., 2017](document_1.txt)). The proposed GRURNTN (1.33) and LSTMRNTN (1.34) beat the simple and Hessian-free baselines but remain behind the adaptively regularized LSTM variants. An impartial reading is that the tensor product delivers a genuine and consistent improvement over its own gated baselines, but does not by itself establish a new state of the art on character-level PTB.

## Discrepancy Between the Primary Paper and the Third-Party Note

The third-party research note summarizing the paper reports the character-level improvements identically to the primary source (0.06 absolute / 4.32% relative for GRURNTN; 0.03 absolute / 2.22% relative for LSTMRNTN) but reports a different word-level result for GRURNTN: it states that GRURNTN reduced PPL from 97.78 to 92.98, an improvement of 4.8 absolute / 4.91% relative ([Document 2: Third-party research note](document_2.txt)). The primary paper's own results table and its conclusion both state 87.38 PPL, corresponding to 10.4 absolute / 10.63% relative ([Tjandra et al., 2017](document_1.txt)).

Because the primary paper is the authoritative account and the figure of 87.38 appears consistently in its results table, its analysis section, and its conclusion, the present report treats 87.38 (−10.4 absolute / −10.63% relative) as the correct word-level GRURNTN value, and treats the 92.98 figure in the third-party note as an error or a transcription of a different intermediate checkpoint. Notably, the third-party note's word-level figure is internally inconsistent with its own summary sentence, which repeats the 4.8 / 4.91% figures rather than the paper's 10.4 / 10.63% ([Document 2: Third-party research note](document_2.txt)). This discrepancy underscores the importance of verifying secondary summaries against primary results tables.

## Interpretation and Limitations

Several observations follow from the data. First, the direction of the effect is consistent: on every metric, in every reported epoch, and for both model families, the tensor-enhanced version outperformed its matched baseline ([Tjandra et al., 2017](document_1.txt)). Second, the magnitude of the effect is task-dependent, with relative PPL gains roughly two-and-a-half to five times larger than relative BPC gains. Third, the GRU-based tensor model was the more successful of the two proposed architectures on both tasks, both in absolute score and in relative improvement over its own baseline.

The study's main limitation is that the evaluation covers a single corpus (PTB) and a single task family (language modeling) ([Tjandra et al., 2017](document_1.txt)). The authors explicitly propose extending the work to speech recognition and video recognition in future research ([Tjandra et al., 2017](document_1.txt)). In addition, the parameter-matching strategy required allocating hidden units asymmetrically — 256 units for the proposed models against 860 for the GRURNN baseline — so the gains reflect the expressiveness of the tensor interaction rather than uniform architectural scaling ([Tjandra et al., 2017](document_1.txt)).

## Conclusion

The introduced models achieve consistent, measurable improvements over their gated recurrent baselines. On character-level PTB language modeling, GRURNTN reduces test BPC by 0.06 absolute (4.32% relative) and LSTMRNTN by 0.03 absolute (2.22% relative) ([Tjandra et al., 2017](document_1.txt)). On word-level PTB language modeling, GRURNTN reduces test perplexity by 10.4 absolute (10.63% relative) and LSTMRNTN by 11.29 absolute (10.42% relative) ([Tjandra et al., 2017](document_1.txt)). Taken as a whole, the GRU-based tensor network is the stronger of the two proposals, delivering the best word-level perplexity among all systems tabulated in the paper (87.38) while also leading the character-level comparison among its own baselines (1.33). The gains are achieved at comparable parameter counts, which strengthens the claim that the improvement derives from the tensor-product interaction itself. The most defensible summary is that combining gating with a tensor product yields reliable but task-dependent gains: substantial and benchmark-leading on word-level perplexity, and modest but consistent on character-level bits-per-character, where more heavily regularized LSTM variants remain superior ([Tjandra et al., 2017](document_1.txt)).

## References

Document 2: Third-party research note: Gated recurrent neural tensor network. (n.d.). [document_2.txt](document_2.txt)

Tjandra, A., Sakti, S., Manurung, R., Adriani, M., & Nakamura, S. (2017). *Gated recurrent neural tensor network*. arXiv:1706.02222. [document_1.txt](document_1.txt)