# Quantifying the Improvement of Gated Recurrent Neural Tensor Networks over Gated Recurrent Neural Network Baselines

## Introduction and Scope of the Query

This report addresses a single, focused question: how much improvement do the two models introduced by Tjandra, Sakti, Manurung, Adriani, and Nakamura — the Long Short-Term Memory Recurrent Neural Tensor Network (LSTMRNTN) and the Gated Recurrent Unit Recurrent Neural Tensor Network (GRURNTN) — achieve relative to the gated recurrent baselines they were designed to replace? The answer is reported at two levels of granularity: the aggregate improvements reported by the authors themselves, and the position of those improvements relative to previously published language-modeling results on the same benchmark corpus ([Tjandra et al., 2017](https://arxiv.org/abs/1706.02222)).

The two baselines are the standard Gated Recurrent Unit RNN (GRURNN) and the standard Long Short-Term Memory RNN (LSTMRNN). The two proposed architectures embed a tensor-product operation inside the gating equations of those units: GRURNTN places the bilinear tensor interaction inside the candidate hidden-layer equation, whereas LSTMRNTN places it inside the candidate memory-cell equation ([Tjandra et al., 2017](https://arxiv.org/abs/1706.02222)). All four models were evaluated on the PennTreeBank (PTB) corpus in two settings — word-level language modeling measured by perplexity (PPL), and character-level language modeling measured by bits-per-character (BPC) — using the standard preprocessing of the corpus and the RNNLM-toolkit version of the data ([Tjandra et al., 2017](https://arxiv.org/abs/1706.02222)).

## Headline Improvements Reported by the Authors

The authors summarize the results in their conclusion with the following numbers, which constitute the most direct answer to the query:

- **Character-level modeling:** GRURNTN obtained a **0.06 absolute / 4.32% relative BPC reduction** over GRURNN, and LSTMRNTN obtained a **0.03 absolute / 2.22% relative BPC reduction** over LSTMRNN ([Tjandra et al., 2017](https://arxiv.org/abs/1706.02222)).
- **Word-level modeling:** GRURNTN obtained a **10.4 absolute / 10.63% relative PPL reduction** over GRURNN, and LSTMRNTN obtained an **11.29 absolute / 10.42% relative PPL reduction** over LSTMRNN ([Tjandra et al., 2017](https://arxiv.org/abs/1706.02222)).

The abstract and conclusion both describe these gains as "significant" improvements relative to the baselines, while explicitly conditioning the comparison on the two models having a similar number of free parameters ([Tjandra et al., 2017](https://arxiv.org/abs/1706.02222)).

### Character-Level Language Modeling (BPC)

For character-level language modeling, lower BPC is better. The baseline GRURNN reached 1.39 BPC and the baseline LSTMRNN reached 1.37 BPC; the proposed GRURNTN reached 1.33 BPC and the proposed LSTMRNTN reached 1.34 BPC ([Tjandra et al., 2017](https://arxiv.org/abs/1706.02222)). The table below reproduces the paired comparison.

| Task level | Baseline model | Baseline score | Proposed model | Proposed score | Absolute change | Relative change |
|---|---|---|---|---|---|---|
| Character (BPC) | GRURNN | 1.39 | GRURNTN | 1.33 | −0.06 | 4.32% |
| Character (BPC) | LSTMRNN | 1.37 | LSTMRNTN | 1.34 | −0.03 | 2.22% |

The authors further note that GRURNTN slightly outperformed LSTMRNTN on this task and that both proposed models outperformed all of the baseline models throughout training, producing lower BPC "from the first epoch to the last epoch" on the validation set ([Tjandra et al., 2017](https://arxiv.org/abs/1706.02222)). This epoch-by-epoch claim is methodologically important: it indicates that the tensor-product advantage is not merely a late-convergence artifact but is visible in early training as well.

### Word-Level Language Modeling (PPL)

For word-level language modeling, the pattern is more striking because the two baseline families diverge substantially. GRURNN scored 97.78 test PPL, whereas LSTMRNN scored 108.26 test PPL — meaning that the LSTM baseline was markedly worse than the GRU baseline before any tensor product was added ([Tjandra et al., 2017](https://arxiv.org/abs/1706.02222)). Against that backdrop, LSTMRNTN reduced perplexity to 96.97, a **11.29 absolute / 10.42% relative** improvement over LSTMRNN that essentially restored LSTM performance to the GRU baseline level. GRURNTN, by contrast, reduced perplexity to **87.38**, a **10.4 absolute / 10.63% relative** improvement over GRURNN and the best result among the four models ([Tjandra et al., 2017](https://arxiv.org/abs/1706.02222)).

| Task level | Baseline model | Baseline score | Proposed model | Proposed score | Absolute change | Relative change |
|---|---|---|---|---|---|---|
| Word (PPL) | GRURNN | 97.78 | GRURNTN | 87.38 | −10.40 | 10.63% |
| Word (PPL) | LSTMRNN | 108.26 | LSTMRNTN | 96.97 | −11.29 | 10.42% |

The authors state that "LSTMRNTN improved the LSTMRNN model and its performance closely resembles the baseline GRURNN," while "GRURNTN outperformed all the baseline models as well as the other models by a large margin" ([Tjandra et al., 2017](https://arxiv.org/abs/1706.02222)). In relative terms, the two proposed models deliver nearly identical percentage gains over their own baselines (10.63% versus 10.42%), but the GRU-based variant ends up at an objectively better absolute operating point.

## A Discrepancy in the Secondary Source

An independent third-party research note summarizing the paper reports the same character-level figures (1.39 → 1.33 for GRURNTN; 1.37 → 1.34 for LSTMRNTN) and the same LSTMRNTN word-level figure (108.26 → 96.97, i.e., 11.29 absolute / 10.42% relative) ([Research note](document_2.txt)). However, for the GRURNTN word-level result, the note states that perplexity fell from 97.78 to **92.98** — a 4.8 absolute / 4.91% relative improvement — rather than to 87.38 as reported in the primary paper's Table II and conclusion ([Research note](document_2.txt); [Tjandra et al., 2017](https://arxiv.org/abs/1706.02222)).

This is a substantive inconsistency, and it matters for answering the query precisely. The primary source is internally consistent on this point: its Table II lists "GRURNTN (proposed) 87.38," and its conclusion repeats the 10.4 absolute / 10.63% relative figure derived from that table ([Tjandra et al., 2017](https://arxiv.org/abs/1706.02222)). The secondary note's 92.98 figure does not appear in the primary paper and conflicts with both its tabulated value and its stated relative improvement. Given that the primary paper is the authoritative record of its own experiment, the defensible position is that **GRURNTN's word-level improvement is 10.4 absolute / 10.63% relative (97.78 → 87.38)**, and that the 4.8 absolute / 4.91% relative figure in the secondary note should be treated as an error rather than as an alternative finding. Readers comparing the two sources should prefer the primary paper for all quantitative claims and treat the note as corroborating the character-level and LSTMRNTN word-level numbers only.

## Position Relative to Previously Published Results

Beyond the head-to-head baseline comparison, the paper places its results among published results on the same corpus. On the character-level task, published systems include NNLM at 1.57 BPC, BPTT-RNN at 1.42, HF-MRNN at 1.24, sRNN at 1.41, and DOT(S)-RNN at 1.39, while an LSTMRNN variant with adaptive noise and without dynamic evaluation reached 1.33, and with dynamic evaluation reached 1.26 ([Tjandra et al., 2017](https://arxiv.org/abs/1706.02222)). The proposed GRURNTN at 1.33 is therefore competitive with the strongest non-dynamic-evaluation published result, but remains behind the 1.26 figure achieved with dynamic evaluation — a technique the authors explicitly did not use in their own experiments ([Tjandra et al., 2017](https://arxiv.org/abs/1706.02222)).

On the word-level task, published systems range from N-Gram at 141 PPL, RNNLM without and with dynamic evaluation at 124.7 and 123.2 respectively, SCRNN at 115, sRNN at 110.0, and DOT(S)-RNN at 107.5, down to the GRURNN baseline at 97.78 and LSTMRNN baseline at 108.26; the proposed models occupy 87.38 (GRURNTN) and 96.97 (LSTMRNTN) ([Tjandra et al., 2017](https://arxiv.org/abs/1706.02222)). GRURNTN therefore improves not only on its paired baseline but on every published system listed in the comparison table.

## Training Dynamics, Parameter Budget, and Fairness

Three methodological details shape how the improvements should be interpreted.

First, the comparisons were budget-matched. The authors state that they "constrained our baseline GRURNN to have a similar number of parameters as the GRURNTN model for a fair comparison" and applied the same constraint to LSTMRNN versus LSTMRNTN ([Tjandra et al., 2017](https://arxiv.org/abs/1706.02222)). For the word-level task, GRURNTN and LSTMRNTN used 256 hidden units, while GRURNN used 860 and LSTMRNN used 740; for the character-level task, the proposed models again used 256 hidden units, against 820 for GRURNN ([Tjandra et al., 2017](https://arxiv.org/abs/1706.02222)). The reported free-parameter totals are approximately 12 million for the GRU pair and 13 million for the LSTM pair at word level, and approximately 2.2 million and 2.6 million at character level ([Tjandra et al., 2017](https://arxiv.org/abs/1706.02222)). This is a meaningful control: the gains cannot be dismissed as simply buying more capacity, although the comparison does confound the tensor product with a much narrower hidden layer (256 versus 740–860 units). It is possible that the tensor product's advantage partly reflects the parameter-efficiency of width-256 tensor-augmented layers rather than tensor products being uniformly superior at equal width.

Second, training-regime details differed slightly between proposed and baseline models: dropout probability was 0.5 for the proposed models versus 0.6 for the baselines at word level, and 0.25 at character level, with orthogonal weight initialization, AdaGrad, mini-batches of 15 sentences, gradient rescaling above a norm of 5, and a dropout-rate decay of 0.5 when validation cost increased ([Tjandra et al., 2017](https://arxiv.org/abs/1706.02222)). These are conventional choices, but they mean the comparison is not a pure architecture ablation.

Third, convergence behavior differed. GRURNN progressed faster than LSTMRNN on both tasks, but LSTMRNN eventually converged to a better character-level BPC; GRURNTN made faster progress than LSTMRNTN and was the single best model on the word-level task, with "consistently lower PPL than the other models" ([Tjandra et al., 2017](https://arxiv.org/abs/1706.02222)). The improvement is therefore observable across the whole learning curve, not only at the terminal epoch.

## Analytical Opinion

Based on the evidence provided, my assessment is as follows. The improvements are real, reproducible within the paper's own experimental setup, and directionally consistent across two different tasks, two different base architectures, and both aggregate and epoch-level analyses. The strongest result is GRURNTN's word-level perplexity reduction of 10.4 absolute / 10.63% relative, which moves the model from 97.78 to 87.38 and makes it the best model in the paper's comparison table ([Tjandra et al., 2017](https://arxiv.org/abs/1706.02222)). The weakest result is LSTMRNTN's character-level reduction of 0.03 BPC (2.22% relative), which is small in absolute terms and is partly attributable to the LSTM baseline already sitting at a low BPC ([Tjandra et al., 2017](https://arxiv.org/abs/1706.02222)). The GRU-based tensor architecture is the more compelling contribution: it achieves the largest relative word-level gain, the largest absolute character-level gain, and the best absolute score on both tasks, all while using only two gates rather than three.

Two caveats temper this conclusion. The results rest on a single corpus (PennTreeBank) and, as reported, a single experimental configuration; the paper reports no statistical significance testing despite describing the gains as significant ([Tjandra et al., 2017](https://arxiv.org/abs/1706.02222)). Also, the numerical discrepancy between the primary paper and the secondary note on GRURNTN's word-level PPL (87.38 versus 92.98) should prompt independent verification before the 10.63% relative figure is treated as settled ([Research note](document_2.txt)). On balance, the evidence supports the claim that tensor-product interactions inside gating equations yield consistent, parameter-budget-neutral gains of roughly 2–4% relative on character-level modeling and roughly 10–11% relative on word-level perplexity, with the GRU variant delivering the better final operating point.

## Conclusion

In direct answer to the query: GRURNTN improved character-level BPC by 0.06 absolute (4.32% relative) over GRURNN and word-level PPL by 10.4 absolute (10.63% relative) over GRURNN; LSTMRNTN improved character-level BPC by 0.03 absolute (2.22% relative) over LSTMRNN and word-level PPL by 11.29 absolute (10.42% relative) over LSTMRNN ([Tjandra et al., 2017](https://arxiv.org/abs/1706.02222)). Both proposed models outperformed their parameters-matched baselines on both tasks and across training epochs, and GRURNTN also surpassed every previously published result listed in the paper's comparison tables ([Tjandra et al., 2017](https://arxiv.org/abs/1706.02222)). The magnitude of the benefit is task-dependent — modest on character-level prediction, substantial on word-level perplexity — and the GRU-based variant is the stronger of the two proposed architectures.

## References

Tjandra, A., Sakti, S., Manurung, R., Adriani, M., & Nakamura, S. (2017). *Gated recurrent neural tensor network*. arXiv. https://arxiv.org/abs/1706.02222

Third-party research note: Gated recurrent neural tensor network [Research note]. (n.d.). document_2.txt