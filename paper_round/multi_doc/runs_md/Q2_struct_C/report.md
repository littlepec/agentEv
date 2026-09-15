# Word-Level Penn Treebank Test Perplexity of Each Paper's Own Proposed Single Model

## 1. Scope, Definitions, and Method

This report compiles, for every paper represented in the supplied research-note corpus, the **word-level Penn Treebank (PTB) test perplexity that the paper reports for its own proposed model**, under a strict comparability rule. Only results satisfying all of the following conditions are counted:

1. The result belongs to the paper's **own proposed architecture or method** (not a baseline it merely cites);
2. The result is a **single-model** result (no ensembles or model averaging);
3. The result does **not** use **dynamic evaluation**;
4. The result does **not** use a **cache or pointer** mechanism at test time;
5. The metric is **word-level PTB test perplexity**.

Fine-tuning is *not* excluded by the query's criteria (which exclude only dynamic evaluation and cache/pointer), so reported results that include a fine-tuning step are retained and flagged. All figures below are drawn exclusively from the third-party research notes and paper excerpts supplied in the corpus; no external numbers have been introduced.

A practical caveat applies throughout: the corpus consists of **third-party research notes and excerpts**, not the full papers. Some notes report only validation/test pairs, some report only the best configuration, and one paper (arXiv:1611.01462) is represented only by a partial table fragment. These limitations are stated explicitly wherever they affect a reported number.

## 2. Consolidated Results Table

Table 1 lists, for each of the eleven papers, the best PTB word-level test perplexity reported for the paper's own proposed model under the stated criteria.

**Table 1. Best single-model word-level PTB test perplexity per paper (no dynamic evaluation, no cache/pointer, no ensembles)**

| # | Paper (arXiv ID) | Paper's own proposed model (best configuration) | PTB test PPL |
|---|---|---|---|
| 1 | Recurrent Neural Network Regularization (arXiv:1409.2329) | Large regularized LSTM | **78.4** |
| 2 | Character-Aware Neural Language Models (arXiv:1508.06615) | LSTM-Char-Large | **78.9** |
| 3 | Variational LSTM with MC dropout (arXiv:1512.05287) | Large Variational LSTM, untied weights, MC dropout | **73.4** |
| 4 | Recurrent Highway Networks (arXiv:1607.03474) | Variational RHN + weight tying (23M params) | **65.4** |
| 5 | Using the Output Embedding to Improve Language Models (arXiv:1608.05859) | Large NNLM + weight tying | **74.3** |
| 6 | Tying Word Vectors and Word Classifiers (arXiv:1611.01462) | VD-LSTM+REAL (small, 200 units)* | **138.4*** |
| 7 | Neural Architecture Search with Reinforcement Learning (arXiv:1611.01578) | NAS, base 8 + shared embeddings (54M params) | **62.4** |
| 8 | Gated Recurrent Neural Tensor Network (arXiv:1706.02222) | GRURNTN | **87.38** |
| 9 | On the State of the Art of Evaluation in Neural Language Models (arXiv:1707.05589) | 4-layer LSTM, 24M params | **58.3** |
| 10 | Regularizing and Optimizing LSTM Language Models (arXiv:1708.02182) | AWD-LSTM, 3-layer LSTM with tied weights | **57.3** |
| 11 | Breaking the Softmax Bottleneck (arXiv:1711.03953) | AWD-LSTM-MoS with finetuning | **54.44** |

*The figure for arXiv:1611.01462 is the lowest test-style value appearing in the supplied table fragment, which covers a small (200-unit) model configuration; the corpus does not supply the paper's full PTB comparison table, so this entry should be treated as provisional (see Section 3.6).

Table 2 re-ranks the same figures from lowest (best) to highest perplexity, which makes the state-of-the-art trajectory visible.

**Table 2. Ranked view of the reported results**

| Rank | Paper (arXiv ID) | PTB test PPL |
|---|---|---|
| 1 | Breaking the Softmax Bottleneck (arXiv:1711.03953) | 54.44 |
| 2 | Regularizing and Optimizing LSTM Language Models (arXiv:1708.02182) | 57.3 |
| 3 | On the State of the Art of Evaluation in Neural Language Models (arXiv:1707.05589) | 58.3 |
| 4 | Neural Architecture Search with Reinforcement Learning (arXiv:1611.01578) | 62.4 |
| 5 | Recurrent Highway Networks (arXiv:1607.03474) | 65.4 |
| 6 | Variational LSTM with MC dropout (arXiv:1512.05287) | 73.4 |
| 7 | Using the Output Embedding to Improve Language Models (arXiv:1608.05859) | 74.3 |
| 8 | Recurrent Neural Network Regularization (arXiv:1409.2329) | 78.4 |
| 9 | Character-Aware Neural Language Models (arXiv:1508.06615) | 78.9 |
| 10 | Gated Recurrent Neural Tensor Network (arXiv:1706.02222) | 87.38 |
| 11 | Tying Word Vectors and Word Classifiers (arXiv:1611.01462) | 138.4* |

## 3. Paper-by-Paper Analysis

### 3.1 Recurrent Neural Network Regularization (arXiv:1409.2329) — 78.4

This paper reports word-level PTB test perplexity for its proposed regularized LSTM models as single models: the medium regularized LSTM reaches **82.7**, and the large regularized LSTM reaches **78.4** ([Zaremba et al., 2014](https://arxiv.org/abs/1409.2329)). The best single-model value is therefore **78.4**. The same paper lists single-model baselines of Pascanu et al. 2013 at 107.5, Cheng et al. at 100.0, and a non-regularized LSTM at 114.5, all of which the proposed regularized models beat ([Zaremba et al., 2014](https://arxiv.org/abs/1409.2329)). Its widely cited 69.5 and 68.7 figures are **model-averaging (ensemble) results** — 10 large regularized LSTMs at 69.5 and 38 large regularized LSTMs at 68.7 — and are excluded here because the query restricts the compilation to single models ([Zaremba et al., 2014](https://arxiv.org/abs/1409.2329)). No dynamic evaluation, cache/pointer, or fine-tuning PTB results are reported by this paper.

### 3.2 Character-Aware Neural Language Models (arXiv:1508.06615) — 78.9

The proposed character-aware LSTM language model is evaluated at the word level on PTB. **LSTM-Char-Large attains 78.9** and LSTM-Char-Small attains 92.3, both as single-model results ([Character-Aware Neural Language Models, 2016](https://arxiv.org/abs/1508.06615)). The best single-model value is **78.9**. The paper explicitly excludes ensembles on comparability grounds: "While lower perplexities have been reported with model ensembles [2012], we do not include them here as they are not comparable to the current work" ([Character-Aware Neural Language Models, 2016](https://arxiv.org/abs/1508.06615)). The note records no dynamic evaluation, cache/pointer, or fine-tuning PTB results for this work. Notably, this paper's headline single-model number (78.9) is marginally higher than the large regularized LSTM of arXiv:1409.2329 (78.4), which it effectively treats as the reference point to match.

### 3.3 Variational LSTM with MC Dropout (arXiv:1512.05287) — 73.4

The paper reports **73.4 test perplexity** for the large Variational LSTM with untied weights and MC dropout at test time, a single-model result; the paper states that test perplexity is reduced from 78.4 down to 73.4 with MC dropout and untied weights ([Variational LSTM, 2016](https://arxiv.org/abs/1512.05287)). Table 1 in that paper is captioned "Single model perplexity (on test and validation sets) for the Penn Treebank language modelling task," and the proposed variants are listed as Variational tied weights (medium 79.7, large 75.0), Variational tied weights MC (medium 79.0, large 74.1), Variational untied weights (medium 79.7, large 75.2), and Variational untied weights MC (medium 78.6, large **73.4**) ([Variational LSTM, 2016](https://arxiv.org/abs/1512.05287)). The best value consistent with the inclusion criteria is therefore **73.4**. The same paper reports an **ensemble** result — 10 Variational LSTMs with MC dropout improving Zaremba et al.'s test set perplexity from 69.5 to 68.7 — which is excluded here ([Variational LSTM, 2016](https://arxiv.org/abs/1512.05287)).

### 3.4 Recurrent Highway Networks (arXiv:1607.03474) — 65.4

The paper reports its best PTB word-level test perplexity for the proposed model as **65.4 for Variational RHN + WT** (variational dropout plus weight tying), with 67.9 validation perplexity; the same table lists this configuration at 23M parameters ([Zilly et al., 2016](https://arxiv.org/abs/1607.03474)). The paper also reports **68.5 test perplexity for Variational RHN without weight tying** ([Zilly et al., 2016](https://arxiv.org/abs/1607.03474)). RHNs were trained with a fixed 32M total parameter budget across recurrence depths from 1 to 10, and the best 10-layer model with further reduced weight decay improved to 67.9/65.4 validation/test perplexity ([Zilly et al., 2016](https://arxiv.org/abs/1607.03474)). The best single-model figure is **65.4**. The note states that the best PTB result is a single model, that dynamic evaluation, cache/pointer, ensemble, and fine-tuning are not reported for the proposed model, and that cache/pointer methods appear only as baselines while ensembles are mentioned only in comparison ([Zilly et al., 2016](https://arxiv.org/abs/1607.03474)). An interesting cross-paper discrepancy is worth recording: the NAS paper later cites "Zilly et al. 2016 - Variational RHN, shared embeddings" at **66.0** test perplexity, whereas the RHN paper's own best table entry is 65.4 ([Neural Architecture Search with Reinforcement Learning, 2017](https://arxiv.org/abs/1611.01578); [Zilly et al., 2016](https://arxiv.org/abs/1607.03474)).

### 3.5 Using the Output Embedding to Improve Language Models (arXiv:1608.05859) — 74.3

This paper reports word-level PTB test perplexity for its proposed weight-tied neural network language models in single-model settings. **Large NNLM with weight tying reaches 74.3**, while Small NNLM with weight tying plus projection regularization reaches 100.9 ([Using the Output Embedding to Improve Language Models, 2017](https://arxiv.org/abs/1608.05859)). The best figure is **74.3**. Its comparison baselines include a large NNLM at 78.4 and a small NNLM at 114.5, and it also lists non-dropout baselines such as KN 5-gram 141, RNN 123, LSTM 117, Stack RNN 110, FOFE-FNN 108, Noisy LSTM 108.0, and Deep RNN 107.5 ([Using the Output Embedding to Improve Language Models, 2017](https://arxiv.org/abs/1608.05859)). The note explicitly records that no dynamic evaluation, cache/pointer, ensemble, or fine-tuning settings are reported for its PTB results ([Using the Output Embedding to Improve Language Models, 2017](https://arxiv.org/abs/1608.05859)).

### 3.6 Tying Word Vectors and Word Classifiers (arXiv:1611.01462) — 138.4 (provisional)

The material supplied for this paper is a partial table fragment captioned "Comparison of our work to previous state of the art on word-level validation and test perplexities on the Penn Treebank corpus" ([Tying Word Vectors and Word Classifiers, 2017](https://arxiv.org/abs/1611.01462)). Within the "Small (200 units)" block, the note lists VD-LSTM at 159.1 / 148.0 / 163.19 / 148.6; VD-LSTM+AL at 153.0 / 142.5 / 156.4 / 143.7; VD-LSTM+RE at 152.4 / 141.9 / 152.5 / 140.9; and VD-LSTM+REAL at 149.3 / 140.6 / 150.5 / **138.4** ([Tying Word Vectors and Word Classifiers, 2017](https://arxiv.org/abs/1611.01462)). The lowest value appearing anywhere in the fragment is **138.4**, so that is the number entered in Table 1. The excerpt does not include the paper's larger-model rows or the full baseline table, and the mapping of the four numeric columns is not fully specified in the supplied note. Consequently, this paper's figure is **not directly comparable** to the other ten entries and should be read as the best value present in the supplied fragment rather than as a confirmed best configurational result. The paper's abstract does claim that the framework "leads to state of the art performance on the Penn Treebank with a variety of network models," which cannot be reconciled with 138.4 as a headline PTB test score and strongly implies that the larger-model results lie outside the supplied excerpt ([Tying Word Vectors and Word Classifiers, 2017](https://arxiv.org/abs/1611.01462)).

### 3.7 Neural Architecture Search with Reinforcement Learning (arXiv:1611.01578) — 62.4

The best NAS model reaches **62.4 test perplexity** (NAS with base 8 and shared embeddings, 54M parameters); other NAS configurations score 64.0 (base 8 + shared embeddings, 25M parameters) and 67.9 (base 8, 32M parameters) ([Neural Architecture Search with Reinforcement Learning, 2017](https://arxiv.org/abs/1611.01578)). The best figure is **62.4**, which is 3.6 perplexity better than the best listed baseline, Zilly et al. 2016 Variational RHN with shared embeddings at 66.0 ([Neural Architecture Search with Reinforcement Learning, 2017](https://arxiv.org/abs/1611.01578)). The note confirms a single-model evaluation protocol for PTB, with no dynamic evaluation, cache/pointer, ensemble, or fine-tuning result reported for the NAS model; cache/pointer appears only among baseline labels such as Pointer Sentinel-LSTM ([Neural Architecture Search with Reinforcement Learning, 2017](https://arxiv.org/abs/1611.01578)).

### 3.8 Gated Recurrent Neural Tensor Network (arXiv:1706.02222) — 87.38

For word-level PTB language modeling, the paper's Table II reports test perplexity **87.38 for GRURNTN** and 96.97 for LSTMRNTN, both as individual models ([Gated Recurrent Neural Tensor Network, 2017](https://arxiv.org/abs/1706.02222)). The best value is **87.38**. GRURNTN reduces perplexity from 97.78 to 87.38 relative to GRURNN (a 10.4 absolute, 10.63% relative reduction), and LSTMRNTN reduces 108.26 to 96.97 relative to LSTMRNN (an 11.29 absolute, 10.42% relative reduction) ([Gated Recurrent Neural Tensor Network, 2017](https://arxiv.org/abs/1706.02222)). The paper states that baseline and proposed model experiments did not use dynamic evaluation, and no cache/pointer, ensemble, or fine-tuning setting is reported for the proposed word-level results ([Gated Recurrent Neural Tensor Network, 2017](https://arxiv.org/abs/1706.02222)). Listed comparison values include N-Gram (141), RNNLM without dynamic evaluation (124.7), RNNLM with dynamic evaluation (123.2), SCRNN (115), sRNN (110.0), and DOT(S)-RNN (107.5) ([Gated Recurrent Neural Tensor Network, 2017](https://arxiv.org/abs/1706.02222)). This paper's result is substantially higher than the LSTM-based lines of work, which is consistent with its use of small, tensor-flavored recurrent models rather than large regularized LSTMs.

### 3.9 On the State of the Art of Evaluation in Neural Language Models (arXiv:1707.05589) — 58.3

This paper reports a best word-level PTB test perplexity of **58.3** for its own proposed model, a 4-layer LSTM with 24M parameters, with the authors stating that at 24M, all depths obtain very similar results, reaching 58.3 at depth 4 ([Melis et al., 2017](https://arxiv.org/abs/1707.05589)). The result is a single-model result without dynamic evaluation, cache/pointer, ensemble, or fine-tuning; the paper explicitly refrains from including techniques known to push perplexities lower because its aim is strictly better model comparisons for the architectures under study ([Melis et al., 2017](https://arxiv.org/abs/1707.05589)). Its best figure under the inclusion criteria is **58.3**.

### 3.10 Regularizing and Optimizing LSTM Language Models (arXiv:1708.02182) — 57.3

The paper proposes AWD-LSTM (ASGD Weight-Dropped LSTM) and reports a word-level PTB test perplexity of **57.3** for a 3-layer LSTM with tied weights as a single model without cache/pointer; the result includes the fine-tuning step ([Regularizing and Optimizing LSTM Language Models, 2017](https://arxiv.org/abs/1708.02182)). Table 1 is captioned "Single model perplexity on validation and test sets for the Penn Treebank language modeling task," and Table 4 lists a no-fine-tuning ablation at 58.8 test perplexity, with the paper stating that removal of the fine-tuning step degrades performance ([Regularizing and Optimizing LSTM Language Models, 2017](https://arxiv.org/abs/1708.02182)). The best value is therefore **57.3**; the 52.8 figure is obtained with a **continuous cache pointer** and is excluded under the query's criteria ([Regularizing and Optimizing LSTM Language Models, 2017](https://arxiv.org/abs/1708.02182)). The paper states that its vanilla LSTM improves the state of the art by approximately 1 unit on PTB, and in Table 1 AWD-LSTM's 57.3 beats the best listed baseline, Melis et al. 2017's 4-layer skip-connection LSTM (tied) at 58.3 ([Regularizing and Optimizing LSTM Language Models, 2017](https://arxiv.org/abs/1708.02182)).

### 3.11 Breaking the Softmax Bottleneck (arXiv:1711.03953) — 54.44

For the proposed AWD-LSTM-MoS, Table 1 lists **55.97 without finetuning** and **54.44 with finetuning**, in single-model settings without dynamic evaluation ([Breaking the Softmax Bottleneck, 2017](https://arxiv.org/abs/1711.03953)). With dynamic evaluation the paper reports 47.69, which is excluded ([Breaking the Softmax Bottleneck, 2017](https://arxiv.org/abs/1711.03953)). Because fine-tuning is not among the excluded techniques, the best qualifying value is **54.44**. The note records that the paper does not report cache/pointer or ensemble results for its proposed model on PTB, reporting only results with and without dynamic evaluation and finetuning ([Breaking the Softmax Bottleneck, 2017](https://arxiv.org/abs/1711.03953)).

## 4. Excluded Results and the Reason for Exclusion

Table 3 documents the important results that were deliberately **not** entered into Table 1, so the boundaries of this compilation are transparent.

**Table 3. Notable excluded results**

| Paper | Excluded result | Reason |
|---|---|---|
| arXiv:1409.2329 | 2 medium LSTMs 77.0; 5 medium 73.3; 10 medium 72.0; 2 large 73.6; 10 large 69.5; 38 large 68.7 | Model averaging / ensembles ([Zaremba et al., 2014](https://arxiv.org/abs/1409.2329)) |
| arXiv:1512.05287 | 10 Variational LSTMs with MC dropout, 68.7 | Ensemble of 10 models ([Variational LSTM, 2016](https://arxiv.org/abs/1512.05287)) |
| arXiv:1708.02182 | 52.8 on PTB; 52.0 on WikiText-2 | Continuous cache pointer ([Regularizing and Optimizing LSTM Language Models, 2017](https://arxiv.org/abs/1708.02182)) |
| arXiv:1711.03953 | 47.69 | Dynamic evaluation ([Breaking the Softmax Bottleneck, 2017](https://arxiv.org/abs/1711.03953)) |
| arXiv:1706.02222 | RNNLM with dynamic evaluation, 123.2 | Baseline, not proposed model, and uses dynamic evaluation ([Gated Recurrent Neural Tensor Network, 2017](https://arxiv.org/abs/1706.02222)) |

## 5. Cross-Paper Trends and Interpretation

**The qualifying figures span a factor of roughly 2.5, from 138.4 down to 54.44.** Ordered by reported value, the progression is 138.4 (arXiv:1611.01462, provisional) → 87.38 (arXiv:1706.02222) → 78.9 (arXiv:1508.06615) → 78.4 (arXiv:1409.2329) → 74.3 (arXiv:1608.05859) → 73.4 (arXiv:1512.05287) → 65.4 (arXiv:1607.03474) → 62.4 (arXiv:1611.01578) → 58.3 (arXiv:1707.05589) → 57.3 (arXiv:1708.02182) → 54.44 (arXiv:1711.03953). The lowest single-model, non-dynamic-evaluation, non-cache PTB word-level test perplexity in this corpus is therefore **54.44**, reported by the AWD-LSTM-MoS model ([Breaking the Softmax Bottleneck, 2017](https://arxiv.org/abs/1711.03953)). This is my own assessment based strictly on the supplied figures.

Several structural patterns emerge from the data:

- **Regularization and dropout define the first plateau.** The regularized LSTM (78.4) and the character-aware LSTM (78.9) cluster tightly around 78–79, and variational dropout with MC dropout pushes the large LSTM to 73.4 ([Zaremba et al., 2014](https://arxiv.org/abs/1409.2329); [Character-Aware Neural Language Models, 2016](https://arxiv.org/abs/1508.06615); [Variational LSTM, 2016](https://arxiv.org/abs/1512.05287)).
- **Weight tying and depth carry the next jump.** Weight tying alone yields 74.3 in a large NNLM, and combining variational dropout with weight tying in a recurrent highway network reaches 65.4 ([Using the Output Embedding to Improve Language Models, 2017](https://arxiv.org/abs/1608.05859); [Zilly et al., 2016](https://arxiv.org/abs/1607.03474)).
- **The most recent entries reflect attention to evaluation protocol and optimization.** The evaluation-focused study reaches 58.3 with a deliberately modest, well-tuned 4-layer LSTM, explicitly declining to use lowering tricks for the sake of fair architecture comparison ([Melis et al., 2017](https://arxiv.org/abs/1707.05589)), while AWD-LSTM reaches 57.3 and AWD-LSTM-MoS reaches 54.44 ([Regularizing and Optimizing LSTM Language Models, 2017](https://arxiv.org/abs/1708.02182); [Breaking the Softmax Bottleneck, 2017](https://arxiv.org/abs/1711.03953)).
- **The excluded techniques are far more powerful than any architectural change in this set.** Dynamic evaluation pulls the MoS model from 54.44 to 47.69, and a continuous cache pointer pulls AWD-LSTM from 57.3 to 52.8 ([Breaking the Softmax Bottleneck, 2017](https://arxiv.org/abs/1711.03953); [Regularizing and Optimizing LSTM Language Models, 2017](https://arxiv.org/abs/1708.02182)). This is precisely why the query's restriction matters: without it, nearly every ranking in Table 1 would shift.

## 6. Limitations of This Compilation

First, the underlying evidence consists of third-party research notes and partial excerpts; for several papers only a subset of configurations is described. Second, parameter budgets are heterogeneous — 23M for Variational RHN + WT, 24M for the 4-layer LSTM, 25M/32M/54M for NAS configurations, and a fixed 32M training budget for the RHN depth study — so the numbers in Table 1 are not parameter-matched ([Zilly et al., 2016](https://arxiv.org/abs/1607.03474); [Melis et al., 2017](https://arxiv.org/abs/1707.05589); [Neural Architecture Search with Reinforcement Learning, 2017](https://arxiv.org/abs/1611.01578)). Third, some entries include fine-tuning (57.3, 54.44) while others do not report it at all, which slightly favors the fine-tuned models. Fourth, the single most fragile entry is arXiv:1611.01462, where the supplied fragment covers only small (200-unit) configurations and yields 138.4 as the minimum value present; that figure should not be read as the paper's true best PTB single-model result. Fifth, validation/test pairs sometimes appear side by side in the source tables, and I have selected the test-side value in each case (e.g., 67.9/65.4 → 65.4), consistent with the query's focus on test perplexity ([Zilly et al., 2016](https://arxiv.org/abs/1607.03474)).

## 7. Conclusion

Across the eleven papers in the corpus, the qualifying best single-model word-level PTB test perplexities are: 78.4 (arXiv:1409.2329), 78.9 (arXiv:1508.06615), 73.4 (arXiv:1512.05287), 65.4 (arXiv:1607.03474), 74.3 (arXiv:1608.05859), 138.4 provisional (arXiv:1611.01462), 62.4 (arXiv:1611.01578), 87.38 (arXiv:1706.02222), 58.3 (arXiv:1707.05589), 57.3 (arXiv:1708.02182), and 54.44 (arXiv:1711.03953). My assessment, grounded only in the supplied material, is that the strongest defensible claim to the best single-model PTB word-level result under the exclusion of dynamic evaluation and cache/pointer belongs to AWD-LSTM-MoS at 54.44 with finetuning, closely followed by AWD-LSTM at 57.3 and the 4-layer LSTM at 58.3; the apparent 138.4 entry is best treated as an artifact of a truncated source table rather than as a competitive result.

## References

Character-aware neural language models. (2016). *arXiv*. https://arxiv.org/abs/1508.06615

Gated recurrent neural tensor network. (2017). *arXiv*. https://arxiv.org/abs/1706.02222

Inan, H., Khosravi, K., & Socher, R. (2017). *Tying word vectors and word classifiers: A loss framework for language modeling*. arXiv. https://arxiv.org/abs/1611.01462

*Breaking the softmax bottleneck: A high-rank RNN language model*. (2017). arXiv. https://arxiv.org/abs/1711.03953

Melis, G., et al. (2017). *On the state of the art of evaluation in neural language models*. arXiv. https://arxiv.org/abs/1707.05589

*Neural architecture search with reinforcement learning*. (2017). arXiv. https://arxiv.org/abs/1611.01578

*Regularizing and optimizing LSTM language models*. (2017). arXiv. https://arxiv.org/abs/1708.02182

*Using the output embedding to improve language models*. (2017). arXiv. https://arxiv.org/abs/1608.05859

*Variational LSTM with MC dropout (a theoretically grounded application of dropout in recurrent neural networks)*. (2016). arXiv. https://arxiv.org/abs/1512.05287

Zaremba, W., et al. (2014). *Recurrent neural network regularization*. arXiv. https://arxiv.org/abs/1409.2329

Zilly, J. G., et al. (2016). *Recurrent highway networks*. arXiv. https://arxiv.org/abs/1607.03474