# Quantifying the Improvement of Gated Recurrent Neural Tensor Networks over Previous Gated RNN Models

## Introduction

The paper *Gated Recurrent Neural Tensor Network* by Tjandra, Sakti, Manurung, Adriani, and Nakamura introduces two new recurrent architectures—the Long Short-Term Memory Recurrent Neural Tensor Network (LSTMRNTN) and the Gated Recurrent Unit Recurrent Neural Tensor Network (GRURNTN)—and benchmarks them against two previously established gated recurrent baselines, the standard Long Short-Term Memory RNN (LSTMRNN) and the Gated Recurrent Unit RNN (GRURNN) ([Tjandra et al., 2017](https://arxiv.org/abs/1706.02222)). The central empirical question is straightforward: how much better do the proposed tensor-augmented, gated models perform than the gated models they are built upon? The answer, drawn from the PennTreeBank (PTB) character-level and word-level language modeling experiments, is that both proposed models beat their matched baselines on both tasks, with relative improvements ranging from 2.22% to 10.63%, and with GRURNTN emerging as the strongest model in the study ([Tjandra et al., 2017](https://arxiv.org/abs/1706.02222); [Third-party research note, n.d.](#references)).

## What Was Compared, and How

### The Baseline and Proposed Architectures

The two baselines are well-established gated RNN variants. GRURNN uses two gating layers (reset and update gates) and no separate memory cells, while LSTMRNN uses three gating layers (input, forget, and output gates) plus memory cells ([Tjandra et al., 2017](https://arxiv.org/abs/1706.02222)). The two proposed models retain those gating mechanisms but insert a tensor product into the core recurrence: GRURNTN adds a tensor-product operation between the current input and the reset-gated previous hidden layer when computing the candidate hidden layer, while LSTMRNTN adds a tensor product between the current input and the previous hidden layer when computing the candidate memory cell ([Tjandra et al., 2017](https://arxiv.org/abs/1706.02222)). The authors describe this as moving from first-degree polynomial interactions (dot product plus addition) to second-degree polynomial interactions, which they argue increases model expressiveness and yields a more direct input-to-hidden interaction ([Tjandra et al., 2017](https://arxiv.org/abs/1706.02222)). The tensor weights are trained with backpropagation through time (including truncated BPTT), optimized with AdaGrad, and stabilized with gradient rescaling when the gradient norm exceeded 5 and orthogonal weight initialization ([Tjandra et al., 2017](https://arxiv.org/abs/1706.02222)).

### Task Design and Fairness Controls

Both tasks use the PennTreeBank corpus, split into training sections 0–20 (930,000 words), validation sections 21–22 (74,000 words), and test sections 23–24 (82,000 words), with a 10,000-word vocabulary and out-of-vocabulary words mapped to an `<unk>` token ([Tjandra et al., 2017](https://arxiv.org/abs/1706.02222)). Word-level modeling is scored with perplexity (PPL) and character-level modeling with bits-per-character (BPC); in both metrics, lower is better ([Tjandra et al., 2017](https://arxiv.org/abs/1706.02222)). Critically for interpreting the improvements, the authors explicitly constrained each baseline to have a similar number of free parameters as its tensor counterpart "for a fair comparison" ([Tjandra et al., 2017](https://arxiv.org/abs/1706.02222)).

| Task | Model | Hidden units | Embedding dim. | Dropout p | Free parameters |
|---|---|---|---|---|---|
| Word-level | GRURNN (baseline) | 860 | 128 | 0.6 | ~12 million |
| Word-level | GRURNTN (proposed) | 256 | 128 | 0.5 | ~12 million |
| Word-level | LSTMRNN (baseline) | 740 | 128 | 0.6 | ~13 million |
| Word-level | LSTMRNTN (proposed) | 256 | 128 | 0.5 | ~13 million |
| Character-level | GRURNN (baseline) | 820 | 32 | 0.25 | ~2.2 million |
| Character-level | GRURNTN (proposed) | 256 | 32 | 0.25 | ~2.2 million |
| Character-level | LSTMRNN (baseline) | 600 | 32 | 0.25 | ~2.6 million |
| Character-level | LSTMRNTN (proposed) | 256 | 32 | 0.25 | ~2.6 million |

*Table 1. Experimental configuration and parameter budgets for all four models ([Tjandra et al., 2017](https://arxiv.org/abs/1706.02222)).*

## Results: Character-Level Language Modeling (BPC)

On the PTB character-level test set, GRURNTN reduced BPC from 1.39 to 1.33, an absolute reduction of 0.06 and a relative reduction of 4.32% over GRURNN; LSTMRNTN reduced BPC from 1.37 to 1.34, an absolute reduction of 0.03 and a relative reduction of 2.22% over LSTMRNN ([Tjandra et al., 2017](https://arxiv.org/abs/1706.02222); [Third-party research note, n.d.](#references)).

| Model | Test BPC | Change vs. matched baseline (absolute) | Relative change |
|---|---|---|---|
| GRURNN (baseline) | 1.39 | — | — |
| **GRURNTN (proposed)** | **1.33** | **−0.06** | **−4.32%** |
| LSTMRNN (baseline) | 1.37 | — | — |
| **LSTMRNTN (proposed)** | **1.34** | **−0.03** | **−2.22%** |

*Table 2. Character-level PTB test BPC ([Tjandra et al., 2017](https://arxiv.org/abs/1706.02222)).*

Two details in the paper's own analysis matter. First, GRURNTN "slightly outperformed" LSTMRNTN on this task, and both proposed models outperformed all of the models in the baseline set ([Tjandra et al., 2017](https://arxiv.org/abs/1706.02222)). Second, the gains were present from the very beginning of training: "Both proposed models produced lower BPC than our baseline models from the first epoch to the last epoch" on the validation set ([Tjandra et al., 2017](https://arxiv.org/abs/1706.02222)).

## Results: Word-Level Language Modeling (PPL)

The word-level results are substantially larger in relative terms. GRURNTN reduced perplexity from 97.78 to 87.38, an absolute reduction of 10.40 PPL and a relative reduction of 10.63% over GRURNN. LSTMRNTN reduced perplexity from 108.26 to 96.97, an absolute reduction of 11.29 PPL and a relative reduction of 10.42% over LSTMRNN ([Tjandra et al., 2017](https://arxiv.org/abs/1706.02222); [Third-party research note, n.d.](#references)).

| Model | Test PPL | Change vs. matched baseline (absolute) | Relative change |
|---|---|---|---|
| GRURNN (baseline) | 97.78 | — | — |
| **GRURNTN (proposed)** | **87.38** | **−10.40** | **−10.63%** |
| LSTMRNN (baseline) | 108.26 | — | — |
| **LSTMRNTN (proposed)** | **96.97** | **−11.29** | **−10.42%** |

*Table 3. Word-level PTB test PPL ([Tjandra et al., 2017](https://arxiv.org/abs/1706.02222)).*

The paper's qualitative summary reinforces the numbers: LSTMRNTN improved on LSTMRNN and ended up performing roughly like the *baseline* GRURNN, whereas GRURNTN "outperformed all the baseline models as well as the other models by a large margin" ([Tjandra et al., 2017](https://arxiv.org/abs/1706.02222)). This is confirmed by the epoch-wise validation curves, where "the best model in this task was GRURNTN, which had a consistently lower PPL than the other models" ([Tjandra et al., 2017](https://arxiv.org/abs/1706.02222)).

## How Large Are These Improvements, Really?

### Absolute versus relative magnitude

The pattern is clear when the two tasks are placed side by side. On character-level modeling, the relative gains are modest—4.32% for the GRU line and 2.22% for the LSTM line—and the absolute BPC differences (0.06 and 0.03) are small fractions of a bit. On word-level modeling, the relative gains are roughly two and a half to five times larger by percentage (10.63% and 10.42%), and the absolute reductions exceed ten perplexity points in both cases ([Tjandra et al., 2017](https://arxiv.org/abs/1706.02222)). In my assessment, the word-level result is the more persuasive evidence for the architecture, because a 10% relative perplexity reduction on a standard benchmark is difficult to attribute to noise, whereas a 0.03 BPC change is close to the granularity of typical run-to-run variation in character-level RNN experiments.

### Which proposed model benefited most

The GRU line gained more on character-level modeling (4.32% versus 2.22%), while the two proposed models were nearly tied on word-level modeling (10.63% versus 10.42%) ([Third-party research note, n.d.](#references)). However, the absolute end-state matters more than the delta: GRURNTN's 87.38 PPL is the best score reported anywhere in the paper's word-level table, whereas LSTMRNTN's 96.97 PPL only narrowly improves on the *baseline* GRURNN's 97.78 PPL (a 0.83% relative improvement, computed from the reported values) ([Tjandra et al., 2017](https://arxiv.org/abs/1706.02222)). A reader interested in deployment should therefore read the headline as "GRURNTN wins," not as "both new models win equally."

### Comparison with published third-party results

The paper also tabulates prior published systems. On word-level PTB, the published reference points listed are N-Gram at 141, RNNLM without dynamic evaluation at 124.7, RNNLM with dynamic evaluation at 123.2, SCRNN at 115, sRNN at 110.0, and DOT(S)-RNN at 107.5 ([Tjandra et al., 2017](https://arxiv.org/abs/1706.02222)). Against the strongest of these (DOT(S)-RNN, 107.5), GRURNTN's 87.38 represents a further 18.7% relative reduction, which I computed from the reported values. On character-level PTB, the tabulated third-party results include NNLM at 1.57, BPTT-RNN at 1.42, HF-MRNN at 1.24/1.41, sRNN at 1.39/1.41, and DOT(S)-RNN at 1.37 BPC ([Tjandra et al., 2017](https://arxiv.org/abs/1706.02222)). The character-level picture is notably less dominant: the paper's own footnote records that a published LSTMRNN configuration with adaptive noise regularization and dynamic evaluation reached 1.26 BPC, and the authors explicitly state that "Our baseline and proposed model experiment did not use dynamic evaluation" ([Tjandra et al., 2017](https://arxiv.org/abs/1706.02222)). Consequently, GRURNTN's 1.33 BPC is the best score among the models trained under the paper's own protocol, but it does not beat every previously published character-level result once adaptive noise and dynamic evaluation are allowed.

## Caveats and Reliability Assessment

Three issues temper the headline numbers, and I consider them material.

First, **the secondary research note overstates the parameter story**. That note claims the proposed models "outperformed the baseline models with roughly twice the number of parameters" ([Third-party research note, n.d.](#references)). The primary paper states the opposite: the baselines were deliberately constrained to a comparable parameter budget "for a fair comparison," and the conclusion reports that the proposed models "outperformed the baseline models with a similar number of parameters" ([Tjandra et al., 2017](https://arxiv.org/abs/1706.02222)). The reported budgets are approximately 12 million versus 12 million (word-level, GRU line) and 2.2 million versus 2.2 million (character-level, GRU line) ([Tjandra et al., 2017](https://arxiv.org/abs/1706.02222)). Where the secondary source conflicts with the primary source, the primary source should be preferred, so the "twice the parameters" framing should be treated as an error.

Second, **the comparison is not purely architectural**. To hold parameters constant, the baselines were given far more hidden units than the proposed models (860 versus 256 at word-level for the GRU line; 820 versus 256 at character-level) ([Tjandra et al., 2017](https://arxiv.org/abs/1706.02222)). This is a legitimate experimental control, but it means the improvement reflects the tensor formulation's greater capacity per parameter rather than a like-for-like comparison of identical hidden widths.

Third, **no variance estimates are reported**. The paper presents single test-set figures and epoch-level validation curves rather than multi-seed means with confidence intervals ([Tjandra et al., 2017](https://arxiv.org/abs/1706.02222)). The word-level gains are large enough that this is unlikely to change the conclusion, but the 0.03 BPC character-level gain for LSTMRNTN should be read with caution. It is also worth noting that the source text available for this analysis is an OCR-derived rendering with some garbled table entries, so table values should be cross-checked against the original publication before being reused.

## Conclusion

Based on the reported experiments, the introduced models do improve on the previous gated RNN baselines, but the size of the improvement depends heavily on the task and on which architectural line is considered. GRURNTN delivered the clearest and largest gains: 0.06 absolute / 4.32% relative BPC improvement over GRURNN on character-level language modeling and 10.40 absolute / 10.63% relative PPL improvement over GRURNN on word-level language modeling ([Tjandra et al., 2017](https://arxiv.org/abs/1706.02222); [Third-party research note, n.d.](#references)). LSTMRNTN delivered 0.03 absolute / 2.22% relative BPC improvement and 11.29 absolute / 10.42% relative PPL improvement over LSTMRNN ([Tjandra et al., 2017](https://arxiv.org/abs/1706.02222); [Third-party research note, n.d.](#references)). The gains were consistent across training epochs rather than appearing only at convergence, and they were achieved at matched parameter budgets ([Tjandra et al., 2017](https://arxiv.org/abs/1706.02222)). My overall judgement is that the evidence supports a meaningful improvement for the tensor-augmented gated architectures—especially GRURNTN—on word-level language modeling, while the character-level improvement, although real within the paper's protocol, is small in absolute terms and does not exceed the best previously published character-level results obtained with adaptive noise and dynamic evaluation.

## References

Tjandra, A., Sakti, S., Manurung, R., Adriani, M., & Nakamura, S. (2017). *Gated recurrent neural tensor network* (arXiv:1706.02222). arXiv. https://arxiv.org/abs/1706.02222

Third-party research note: Gated recurrent neural tensor network [Unpublished research note summarizing Tjandra et al. (2017)]. (n.d.).