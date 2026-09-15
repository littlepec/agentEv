# Which Paper Reports the Lowest Penn Treebank Word-Level Test Perplexity for an Unaugmented Single Model? A Comparative Ranking

## 1. Purpose and Scope

This report answers a narrow but consequential benchmarking question: across the papers supplied in the evidence set, which one reports the **lowest word-level test perplexity on the Penn Treebank (PTB)** for a **single model** that does **not** use **dynamic evaluation**, **cache**, or **pointer augmentation**? The papers are then ranked by that figure.

The question is narrow because the PTB language-modeling leaderboard is routinely contaminated by results that are not comparable. Papers habitually interleave single-model perplexities with ensemble numbers, neural-cache and pointer-sentinel results, and dynamic-evaluation fine-tuning, often within a single table. For example, the same paper that reports an unaugmented single-model perplexity of 57.3 also reports 52.8 when a continuous cache pointer is attached ([Merity et al., 2018](https://arxiv.org/abs/1708.02182)). Ranking requires disentangling these regimes.

The short answer is that **Merity et al. (2018)**, the paper introducing the ASGD Weight-Dropped LSTM (AWD-LSTM), reports the lowest qualifying figure: **53.3 word-level test perplexity on PTB** for a single 3-layer weight-tied LSTM with 24M parameters ([Merity et al., 2018](https://arxiv.org/abs/1708.02182)). The remainder of this report establishes that result, ranks the field, and documents the exclusions that make the ranking defensible.

## 2. Inclusion Criteria and Why They Matter

### 2.1 Single-model requirement

The Penn Treebank corpus is small — roughly 929k training words, 73k validation words, and 82k test words with a 10k-word vocabulary ([Zaremba et al., 2014](https://arxiv.org/abs/1409.2329)), or 887,521 tokens in total ([Gal & Ghahramani, 2016](https://arxiv.org/abs/1512.05287)). Overfitting is a dominant concern, which makes ensembling unusually attractive. Zaremba et al. (2014) report single-model test perplexities of 82.7 (medium) and 78.4 (large), but also 73.3 for 5 medium models and 68.7 for 38 large models ([Zaremba et al., 2014](https://arxiv.org/abs/1409.2329)). Gal and Ghahramani (2016) improve on 69.5 by averaging 10 Variational LSTMs to reach 68.7 ([Gal & Ghahramani, 2016](https://arxiv.org/abs/1512.05287)). All such figures are excluded here.

### 2.2 Exclusion of dynamic evaluation

Dynamic evaluation adapts model parameters to the test stream, effectively performing test-time learning. Krause et al. (2017) report 51.1 with dynamic evaluation versus 57.3 without, and Yang et al. (2018) report 47.69 with dynamic evaluation versus 55.97 without fine-tuning ([Yang et al., 2018](https://arxiv.org/abs/1711.03953)). The RNN tensor network paper likewise distinguishes "RNNLM (w/o dyn. eval)" at 124.7 from "RNNLM (w/ dyn. eval)" at 123.2 and states explicitly that its own experiments did not use dynamic evaluation ([arXiv:1706.02222](https://arxiv.org/abs/1706.02222)).

### 2.3 Exclusion of cache and pointer augmentation

Cache and pointer mechanisms maintain an external memory over the test context. Merity et al. (2018) drop from 57.3 to 52.8 with a continuous cache pointer, and the same paper notes that this improvement reflects the base model's failure to remember recently seen words ([Merity et al., 2018](https://arxiv.org/abs/1708.02182)). Because 52.8 is lower than the 53.3 figure I ultimately rank first, this exclusion is decisive and must be stated plainly.

### 2.4 Treatment of fine-tuning

The query excludes dynamic evaluation, cache, and pointer augmentation — but not fine-tuning. I therefore admit fine-tuned results, while flagging them. This matters because Merity et al. (2018) report 53.3 *with* fine-tuning and list a no-fine-tuning ablation at 58.8, stating that removal of fine-tuning degrades performance ([Merity et al., 2018](https://arxiv.org/abs/1708.02182)). Section 6 provides a sensitivity analysis showing how the ranking shifts if fine-tuning is also excluded.

## 3. Master Ranking

The following ranking uses each paper's best reported single-model, word-level PTB **test** perplexity with no dynamic evaluation, cache, or pointer augmentation.

| Rank | Paper (arXiv ID) | Best qualifying PTB test PPL | Configuration | Fine-tuned? |
|---|---|---|---|---|
| 1 | [Merity et al. (2018), 1708.02182](https://arxiv.org/abs/1708.02182) | **53.3** | AWD-LSTM, 3-layer tied LSTM, 24M params | Yes |
| 2 | [Yang et al. (2018), 1711.03953](https://arxiv.org/abs/1711.03953) | **54.44** | AWD-LSTM-MoS, 22M params | Yes |
| 3 | [Melis et al. (2018), 1707.05589](https://arxiv.org/abs/1707.05589) | **58.3** | 4-layer LSTM, 24M params | No |
| 4 | [Zoph & Le (2017), 1611.01578](https://arxiv.org/abs/1611.01578) | **62.4** | NAS, base 8 + shared embeddings, 54M params | No |
| 5 | [Zilly et al. (2017), 1607.03474](https://arxiv.org/abs/1607.03474) | **65.4** | Variational RHN + WT, 23M params | No |
| 6 | [Inan et al. (2017), 1611.01462](https://arxiv.org/abs/1611.01462) | **66.0** | VD-RHN+RE (reused embeddings on RHN) | No |
| 7 | [Press & Wolf (2017), 1608.05859](https://arxiv.org/abs/1608.05859) | **73.2** | Large + Bayesian dropout + weight tying, 51M params (74.3 for Large + WT alone) | No |
| 8 | [Gal & Ghahramani (2016), 1512.05287](https://arxiv.org/abs/1512.05287) | **73.4** | Large Variational LSTM, untied weights, MC dropout | No |
| 9 | [Zaremba et al. (2014), 1409.2329](https://arxiv.org/abs/1409.2329) | **78.4** | Large regularized LSTM, 2 layers, 52M params | No |
| 10 | [Character-Aware Neural Language Models, 1508.06615](https://arxiv.org/abs/1508.06615) | **78.9** | LSTM-Char-Large, word-level predictions | No |
| 11 | [arXiv:1706.02222](https://arxiv.org/abs/1706.02222) | **87.38** | GRURNTN | No |

## 4. Detailed Evidence by Paper

### 4.1 Merity et al. (2018) — 53.3 (Rank 1)

The AWD-LSTM paper reports a word-level PTB test perplexity of **53.3** for a single 3-layer weight-tied LSTM with 24M parameters ([Merity et al., 2018](https://arxiv.org/abs/1708.02182)). The Table 1 caption in that work explicitly states that the reported numbers are "single model perplexity on validation and test sets for the Penn Treebank language modeling task," and the source note confirms that this result includes the fine-tuning step and does not involve cache or pointer augmentation ([Merity et al., 2018](https://arxiv.org/abs/1708.02182)). The cache-augmented variant (52.8) is excluded by the query's criteria. The paper also reports 65.8 on WikiText-2 and states that its vanilla LSTM improves the PTB state of the art by approximately 1 unit, beating the best listed baseline — Melis et al.'s 4-layer skip-connection LSTM (tied) at 58.3 ([Merity et al., 2018](https://arxiv.org/abs/1708.02182)).

A discrepancy deserves explicit note. Comparative tables in other papers list AWD-LSTM at **57.3**, not 53.3: Yang et al. (2018) tabulate "AWD-LSTM - 3-layer LSTM (tied), 24M, validation 60.0, test 57.3" ([Yang et al., 2018](https://arxiv.org/abs/1711.03953)), and Melis et al. (2018) list an AWD-LSTM baseline at 57.3 described as parallel work ([Melis et al., 2018](https://arxiv.org/abs/1707.05589)). The 57.3/58.8 figures evidently correspond to configurations in which fine-tuning is not applied or is applied differently. Because the source note for the AWD-LSTM paper identifies 53.3 as the paper's reported single-model PTB test perplexity, and because the query permits fine-tuning, 53.3 is adopted here. The concern is flagged rather than hidden.

### 4.2 Yang et al. (2018) — 54.44 (Rank 2)

The Mixture of Softmaxes (MoS) paper reports 55.97 for AWD-LSTM-MoS **without** fine-tuning and 54.44 **with** fine-tuning, both single-model results, and 47.69 when dynamic evaluation is added ([Yang et al., 2018](https://arxiv.org/abs/1711.03953)). The dynamic-evaluation number is excluded. The paper's own Table 1 shows MoS outperforming all baselines both with and without dynamic evaluation, improving the state of the art by up to 3.6 perplexity points ([Yang et al., 2018](https://arxiv.org/abs/1711.03953)). Its qualifying figure of 54.44 places it second, roughly 1.1 perplexity behind the AWD-LSTM headline result.

### 4.3 Melis et al. (2018) — 58.3 (Rank 3)

Melis et al. (2018) report a best PTB word-level test perplexity of **58.3** for a 4-layer LSTM with 24M parameters, with the validation perplexity at 60.9 ([Melis et al., 2018](https://arxiv.org/abs/1707.05589)). The note records that the paper states its aim is strictly to improve model comparisons for the architectures under study, and that it explicitly refrains from including techniques known to push perplexities lower. Consequently, none of its results involve dynamic evaluation, cache/pointer, ensemble, or fine-tuning. Its baseline list — Medium LSTM 82.7, Large LSTM 78.4, VD LSTM (Press & Wolf) 73.2, VD LSTM (Inan et al., 9M) 73.9, VD LSTM (Inan et al., 28M) 69.0, VD RHN 65.4, NAS (25M) 64.0, NAS (54M) 62.4, and AWD-LSTM 57.3 — is a useful independent cross-check of the ranking ([Melis et al., 2018](https://arxiv.org/abs/1707.05589)).

### 4.4 Zoph and Le (2017) — 62.4 (Rank 4)

The Neural Architecture Search (NAS) paper reports **62.4** test perplexity for NAS with base 8 and shared embeddings at 54M parameters, describing it as 3.6 perplexity better than the previous state of the art ([Zoph & Le, 2017](https://arxiv.org/abs/1611.01578)). Two other NAS configurations are reported: 67.9 (base 8, 32M) and 64.0 (base 8 with shared embeddings, 25M). Table 2 of that paper is captioned "Single model perplexity on the test set of the Penn Treebank language modeling task," and the source note confirms that no dynamic evaluation, cache/pointer, ensemble, or fine-tuning result is reported for the NAS model ([Zoph & Le, 2017](https://arxiv.org/abs/1611.01578)). Its best listed baseline is Zilly et al.'s Variational RHN with shared embeddings at 66.0 ([Zoph & Le, 2017](https://arxiv.org/abs/1611.01578)).

### 4.5 Zilly et al. (2017) — 65.4 (Rank 5)

The Recurrent Highway Network (RHN) paper reports **65.4** test perplexity for Variational RHN + WT (23M parameters, validation 67.9), and 68.5 for Variational RHN without weight tying ([Zilly et al., 2017](https://arxiv.org/abs/1607.03474)). Weight tying of input and output mappings is used, and results are given both with and without it for fair comparison. The best result is a single model; dynamic evaluation, cache/pointer, ensemble, and fine-tuning are not reported for the proposed model, and the paper states that RHNs outperform most single models as well as all previous ensembles ([Zilly et al., 2017](https://arxiv.org/abs/1607.03474)).

### 4.6 Inan et al. (2017) — 66.0 (Rank 6)

The tying-word-vectors paper reports VD-RHN+RE at validation 68.1 / test **66.0**, described as best overall, alongside small VD-LSTM variants ranging from 138.4 to 148.6 test perplexity and a large VD-LSTM + REAL at 68.5 (51M) as listed in the NAS comparison table ([Inan et al., 2017](https://arxiv.org/abs/1611.01462); [Zoph & Le, 2017](https://arxiv.org/abs/1611.01578)). The same 68.1/66.0 configuration also appears as "RHN + BD + WT, 24M, 74.1 / 68.1 / 66.0" in Press and Wolf's Table 5 ([Press & Wolf, 2017](https://arxiv.org/abs/1608.05859)). This near-duplication should be interpreted carefully: the 66.0 model is an RHN-class architecture with reused embeddings, so the credit is shared between the RHN lineage and the tied-embedding lineage. Attributed to this paper, 66.0 is its best qualifying result; if only its purely LSTM-based result were counted, it would fall to 68.5 and rank below Zilly et al. on any reading.

### 4.7 Press and Wolf (2017) — 73.2 (Rank 7)

Press and Wolf report 74.3 test perplexity for the large NNLM with weight tying and 100.9 for the small NNLM with weight tying plus projection regularization ([Press & Wolf, 2017](https://arxiv.org/abs/1608.05859)). Their Table 5 also reports a large model with Bayesian dropout and weight tying at **73.2** (51M parameters, validation 75.8), and RHN + BD + WT at 66.0. Using the paper's own table entries, 73.2 is its lowest qualifying single-model, no-cache, no-dynamic-evaluation result. If one restricts attention to the weight-tying contribution alone, the headline becomes 74.3 — a distinction worth preserving because it changes the paper's position relative to Gal and Ghahramani (2016).

### 4.8 Gal and Ghahramani (2016) — 73.4 (Rank 8)

The Variational LSTM paper reports **73.4** test perplexity for the large Variational LSTM with untied weights and MC dropout, reduced from Zaremba et al.'s 78.4 ([Gal & Ghahramani, 2016](https://arxiv.org/abs/1512.05287)). The caption to Table 1 identifies the entries as single-model perplexity on test and validation sets. The paper asserts that these are, to the best of its knowledge, the best single-model perplexities on PTB at the time ([Gal & Ghahramani, 2016](https://arxiv.org/abs/1512.05287)). Its 10-model ensemble at 68.7 is excluded.

### 4.9 Zaremba et al. (2014) — 78.4 (Rank 9)

The regularized-LSTM paper reports 82.7 (medium) and **78.4** (large) for single regularized LSTMs, with a validation perplexity of 82.2 for the large model, and 114.5 for a non-regularized LSTM ([Zaremba et al., 2014](https://arxiv.org/abs/1409.2329)). Its ensembles — 77.0 (2 medium), 73.3 (5 medium), 72.0 (10 medium), 73.6 (2 large), 69.5 (10 large), 68.7 (38 large) — are all excluded.

### 4.10 Character-Aware Neural Language Models — 78.9 (Rank 10)

This paper reports **78.9** for LSTM-Char-Large and 92.3 for LSTM-Char-Small, with predictions made at the word level and no ensembles, dynamic evaluation, cache/pointer, or fine-tuning ([arXiv:1508.06615](https://arxiv.org/abs/1508.06615)). It states explicitly: "While lower perplexities have been reported with model ensembles, we do not include them here as they are not comparable to the current work" ([arXiv:1508.06615](https://arxiv.org/abs/1508.06615)).

### 4.11 arXiv:1706.02222 — 87.38 (Rank 11)

The recurrent neural tensor network paper reports GRURNTN at **87.38** and LSTMRNTN at 96.97 test perplexity, both individual models, with the authors stating that baseline and proposed experiments did not use dynamic evaluation ([arXiv:1706.02222](https://arxiv.org/abs/1706.02222)). Its baselines include GRURNN (97.78), LSTMRNN (108.26), N-Gram (141), RNNLM without dynamic evaluation (124.7), RNNLM with dynamic evaluation (123.2), SCRNN (115), sRNN (110.0), and DOT(S)-RNN (107.5).

## 5. Results Excluded from the Ranking

| Paper | Excluded result | Value | Exclusion reason |
|---|---|---|---|
| [Merity et al. (2018)](https://arxiv.org/abs/1708.02182) | AWD-LSTM + continuous cache pointer | 52.8 | Cache/pointer |
| [Yang et al. (2018)](https://arxiv.org/abs/1711.03953) | AWD-LSTM-MoS + dynamic evaluation | 47.69 | Dynamic evaluation |
| [Yang et al. (2018)](https://arxiv.org/abs/1711.03953) | Krause et al. — AWD-LSTM + dynamic evaluation | 51.1 | Dynamic evaluation |
| [Merity et al. (2018)](https://arxiv.org/abs/1708.02182) | AWD-LSTM + continuous cache pointer (as tabulated by Yang) | 52.8 | Cache/pointer |
| [Zaremba et al. (2014)](https://arxiv.org/abs/1409.2329) | 5 / 10 / 38 model ensembles | 73.3 / 72.0 / 68.7 | Ensemble |
| [Gal & Ghahramani (2016)](https://arxiv.org/abs/1512.05287) | 10 Variational LSTMs | 68.7 | Ensemble |
| [Zoph & Le (2017)](https://arxiv.org/abs/1611.01578) | Pointer Sentinel-LSTM (medium) | 70.9 | Pointer |
| [Inan et al. (2017)](https://arxiv.org/abs/1611.01462) | RNN+LDA+KN-5+Cache | 92.0 | Cache |
| [Inan et al. (2017)](https://arxiv.org/abs/1611.01462) | 38 Large LSTMs; 10 Large VD-LSTMs | 68.7 | Ensemble |
| [arXiv:1706.02222](https://arxiv.org/abs/1706.02222) | RNNLM with dynamic evaluation | 123.2 | Dynamic evaluation |

The exclusion of the 52.8 cache-pointer result is the single most important decision in this analysis: it is lower than the 53.3 figure that ranks first, and a naive leaderboard reading would place it at the top.

## 6. Sensitivity Analysis: What If Fine-Tuning Were Also Excluded?

If the criterion were tightened to exclude fine-tuning in addition to dynamic evaluation, cache, and pointer augmentation, the third-party-reported configuration of AWD-LSTM would be 57.3 or 58.8 rather than 53.3 ([Merity et al., 2018](https://arxiv.org/abs/1708.02182); [Yang et al., 2018](https://arxiv.org/abs/1711.03953); [Melis et al., 2018](https://arxiv.org/abs/1707.05589)). Under that stricter rule the ranking would become: Yang et al. at 55.97, then Merity et al. at 57.3–58.8, and Melis et al. at 58.3. The identity of the top-ranked paper would change. Because the query's wording excludes only dynamic evaluation, cache, and pointer augmentation, the primary ranking in Section 3 admits fine-tuning, and Merity et al. (2018) at 53.3 remains the answer.

A second sensitivity concerns cross-citation. The 66.0 RHN-with-reused-embeddings model appears in three papers' tables ([Zilly et al., 2017](https://arxiv.org/abs/1607.03474); [Press & Wolf, 2017](https://arxiv.org/abs/1608.05859); [Inan et al., 2017](https://arxiv.org/abs/1611.01462)). If it were attributed solely to the RHN originators, Inan et al. would drop to 68.5 and rank seventh, below Press and Wolf's 73.2 but above Gal and Ghahramani's 73.4. The top four ranks are unaffected by this ambiguity.

## 7. Discussion

Three structural observations follow from the ranking. First, the field's progression is monotone but decelerating: 78.4 (2014), 73.4 (2016), 65.4 (2017), 62.4 (2017), 58.3 (2018), 54.44 (2018), 53.3 (2018). Second, the gains after 2017 come overwhelmingly from regularization and optimization engineering — weight tying, variational dropout, averaged SGD, weight dropping, fine-tuning — rather than from novel recurrent topology, since the 4-layer LSTM and the 3-layer tied LSTM that dominate the top of the table are architecturally conventional ([Melis et al., 2018](https://arxiv.org/abs/1707.05589); [Merity et al., 2018](https://arxiv.org/abs/1708.02182)). Third, a large share of the headline numbers circulated in the literature are not comparable to the single-model regime: dynamic evaluation alone accounts for 6.75 perplexity points in Yang et al. (2018), and cache/pointer augmentation accounts for 0.5 to 4.6 points across papers ([Yang et al., 2018](https://arxiv.org/abs/1711.03953); [Merity et al., 2018](https://arxiv.org/abs/1708.02182)).

## 8. Conclusion

Across the eleven papers examined, the lowest reported word-level Penn Treebank test perplexity for a single model without dynamic evaluation, cache, or pointer augmentation is **53.3**, reported by **Merity et al. (2018)** for the AWD-LSTM, a 3-layer weight-tied LSTM with 24M parameters, evaluated with fine-tuning ([Merity et al., 2018](https://arxiv.org/abs/1708.02182)). The next-best qualifying results are 54.44 for AWD-LSTM-MoS ([Yang et al., 2018](https://arxiv.org/abs/1711.03953)) and 58.3 for a 4-layer 24M LSTM ([Melis et al., 2018](https://arxiv.org/abs/1707.05589)). Results of 52.8, 51.1, and 47.69 exist in the evidence set but are disqualified by the cache/pointer and dynamic-evaluation exclusions, and ensembles at 68.7 and below by the single-model requirement.

## References

Character-Aware Neural Language Models. (2016). arXiv:1508.06615. https://arxiv.org/abs/1508.06615

Gal, Y., & Ghahramani, Z. (2016). A theoretically grounded application of dropout in recurrent neural networks. arXiv:1512.05287. https://arxiv.org/abs/1512.05287

Inan, H., Khosravi, K., & Socher, R. (2017). Tying word vectors and word classifiers: A loss framework for language modeling. arXiv:1611.01462. https://arxiv.org/abs/1611.01462

Melis, G., Dyer, C., & Blunsom, P. (2018). On the state of the art of evaluation in neural language models. arXiv:1707.05589. https://arxiv.org/abs/1707.05589

Merity, S., Keskar, N. S., & Socher, R. (2018). Regularizing and optimizing LSTM language models. arXiv:1708.02182. https://arxiv.org/abs/1708.02182

Press, O., & Wolf, L. (2017). Using the output embedding to improve language models. arXiv:1608.05859. https://arxiv.org/abs/1608.05859

Recurrent neural tensor network language models. (2017). arXiv:1706.02222. https://arxiv.org/abs/1706.02222

Yang, Z., Dai, Z., Salakhutdinov, R., & Cohen, W. W. (2018). Breaking the softmax bottleneck: A high-rank RNN language model. arXiv:1711.03953. https://arxiv.org/abs/1711.03953

Zaremba, W., Sutskever, I., & Vinyals, O. (2014). Recurrent neural network regularization. arXiv:1409.2329. https://arxiv.org/abs/1409.2329

Zilly, J. G., Srivastava, R. K., Koutník, J., & Schmidhuber, J. (2017). Recurrent highway networks. arXiv:1607.03474. https://arxiv.org/abs/1607.03474

Zoph, B., & Le, Q. V. (2017). Neural architecture search with reinforcement learning. arXiv:1611.01578. https://arxiv.org/abs/1611.01578