# Word-Level Penn Treebank Test Perplexity of Proposed Single Models: A Tabulated Synthesis of Eleven Language-Modeling Papers

## Scope, Inclusion Criteria, and Method

This report answers a narrowly defined question: for each paper represented in the supplied corpus, what is the word-level Penn Treebank (PTB) test perplexity that the paper reports for **its own proposed model**, understood as the **best single-model result obtained without dynamic evaluation and without a cache/pointer mechanism**? Four inclusion rules follow directly from that wording and were applied uniformly.

First, the figure must belong to the paper's **own proposed architecture** rather than to a cited baseline, even when the baseline is numerically stronger or weaker. Second, the figure must be a **word-level PTB test perplexity**; character-level figures such as bits-per-character are excluded, as are results on WikiText-2, enwik8, text8, or the 1B Word dataset. Third, the figure must be a **single-model** number: ensembles and model averaging are disallowed, which is consequential for Zaremba et al. (2014), whose averaged large-LSTM configurations reach 69.5 and 68.7, and for Gal (2015), whose ten-model ensemble reaches 68.7. Fourth, **dynamic evaluation and cache/pointer mechanisms are excluded**, which is consequential for Merity et al. (2017) and Yang et al. (2017). Fine-tuning is *not* excluded by the query, so single-model results that use it are retained and flagged.

A final methodological caution governs the whole table. Several of these papers advertise their abstract-level headline numbers using dynamic evaluation or caching, and those numbers are systematically lower than the single-model, no-cache figures requested here. Yang et al. (2018), for example, headline 47.69 on PTB, but that figure uses dynamic evaluation; the corresponding single-model, no-cache best is 54.44 ([Yang et al., 2017](https://arxiv.org/abs/1711.03953)). Likewise, Merity et al. (2017) headline 52.8 only when the continuous cache pointer is enabled; the plain single model is 57.3 ([Merity et al., 2017](https://arxiv.org/abs/1708.02182)). The table below therefore corrects for a very common source of misreading in the PTB literature.

## Consolidated Results

| Paper (arXiv ID) | Proposed model / configuration | Best single-model word-level PTB test PPL (no dynamic eval, no cache) | Source of figure |
|---|---|---|---|
| Zaremba et al., 2014 ([1409.2329](https://arxiv.org/abs/1409.2329)) | Large regularized LSTM (single model) | **78.4** | Paper's own proposed model |
| Kim et al., 2015 ([1508.06615](https://arxiv.org/abs/1508.06615)) | LSTM-Char-Large (two highway layers) | **78.9** | Paper's own proposed model |
| Gal & Ghahramani, 2015 ([1512.05287](https://arxiv.org/abs/1512.05287)) | Large Variational LSTM, MC dropout, untied weights | **73.4** | Paper's own proposed model |
| Zilly et al., 2016 ([1607.03474](https://arxiv.org/abs/1607.03474)) | Variational RHN + weight tying (WT) | **65.4** | Paper's own proposed model |
| Press & Wolf, 2016 ([1608.05859](https://arxiv.org/abs/1608.05859)) | Large NNLM + Weight Tying | **74.3** (see note) | Paper's own proposed model |
| Inan et al., 2016 ([1611.01462](https://arxiv.org/abs/1611.01462)) | VD-LSTM + REAL (large) | **68.5** | Large-model figure reported in the NAS comparison table ([Zoph & Le, 2016](https://arxiv.org/abs/1611.01578)) |
| Zoph & Le, 2016 ([1611.01578](https://arxiv.org/abs/1611.01578)) | NAS, base 8 + shared embeddings (54M) | **62.4** | Paper's own proposed model |
| Gated Recurrent Neural Tensor Network, 2017 ([1706.02222](https://arxiv.org/abs/1706.02222)) | GRURNTN | **87.38** | Paper's own proposed model |
| Melis et al., 2017 ([1707.05589](https://arxiv.org/abs/1707.05589)) | 4-layer LSTM, 24M parameters | **58.3** | Paper's own proposed model |
| Merity et al., 2017 ([1708.02182](https://arxiv.org/abs/1708.02182)) | AWD-LSTM, 3-layer, tied weights | **57.3** | Paper's own proposed model |
| Yang et al., 2017 ([1711.03953](https://arxiv.org/abs/1711.03953)) | AWD-LSTM-MoS, with fine-tuning | **54.44** | Paper's own proposed model |

The span from 78.4 to 54.44 over roughly three calendar years is itself a finding: the PTB word-level benchmark, despite being small (approximately 929k training words, 73k validation words, and 82k test words, with a 10k vocabulary), was still being driven downward by architectural and regularization innovation rather than by test-time augmentation alone ([Zaremba et al., 2014](https://arxiv.org/abs/1409.2329)).

## Detailed Findings by Paper

### Zaremba et al. (2014): Recurrent Neural Network Regularization

The paper trains two regularized LSTM sizes, a medium model reaching 82.7 and a large model reaching 78.4 single-model test perplexity ([Zaremba et al., 2014](https://arxiv.org/abs/1409.2329)). The 78.4 figure is the relevant single-model result; the paper's considerably lower averaged numbers — 77.0 for two medium LSTMs, 73.3 for five, 72.0 for ten, 73.6 for two large LSTMs, 69.5 for ten large LSTMs, and 68.7 for thirty-eight large LSTMs — are model-averaging results and are excluded by the query ([Zaremba et al., 2014](https://arxiv.org/abs/1409.2329)). The paper's listed single-model baselines are Pascanu et al. (2013) at 107.5, Cheng et al. at 100.0, and a non-regularized LSTM at 114.5, all of which the proposed regularized models beat; the paper reports no dynamic evaluation, cache/pointer, or fine-tuning configuration for PTB.

### Kim et al. (2015): Character-Aware Neural Language Models

The proposed character-aware LSTM language model attains 78.9 test perplexity in its LSTM-Char-Large configuration and 92.3 in the LSTM-Char-Small configuration, with predictions made at the word level ([Kim et al., 2015](https://arxiv.org/abs/1508.06615)). The paper's ablation table clarifies the architecture: with no highway layers the small/large models score 100.3/84.6; with one highway layer 92.3/79.7; with two highway layers 90.1/78.9; and with one MLP layer instead 111.2/92.6. The best proposed single-model result is therefore **78.9**. The paper explicitly refuses to include ensembles, stating that "while lower perplexities have been reported with model ensembles, we do not include them here as they are not comparable to the current work" ([Kim et al., 2015](https://arxiv.org/abs/1508.06615)). Its comparison table lists Zaremba et al.'s LSTM-1 at 82.7 and LSTM-2 at 78.4 as baselines, meaning the character-aware large model is competitive with the large word-level LSTM while using approximately 60% fewer parameters.

### Gal and Ghahramani (2015): Variational Dropout for Recurrent Networks

The proposed large Variational LSTM with untied weights and Monte Carlo (MC) dropout at test time achieves **73.4** test perplexity, improved from Zaremba et al.'s 78.4 ([Gal, 2015](https://arxiv.org/abs/1512.05287)). Validation perplexity improves from 82.2 to 77.3 with weight tying, or 77.9 without; the reported paired values of 78.6 ± 0.1 and 73.4 ± 0.0 in the extracted table correspond to the dropout-approximation and MC-dropout variants. The author states that, to the best of his knowledge, 73.4 is the best single-model perplexity on PTB at that time. The paper's ten-model ensemble improving 69.5 to 68.7 is excluded as an ensemble result ([Gal, 2015](https://arxiv.org/abs/1512.05287)). A cross-paper discrepancy is worth recording: the RHN comparison table reproduces Gal's Variational LSTM at 75.0 rather than 73.4, which reflects the distinction between the approximate-dropout evaluation and the MC-dropout evaluation ([Zilly et al., 2016](https://arxiv.org/abs/1607.03474)).

### Zilly et al. (2016): Recurrent Highway Networks

The best proposed single model is Variational RHN + WT at **65.4** test perplexity with 23M parameters and 67.9 validation perplexity; without weight tying the same model scores 68.5 ([Zilly et al., 2016](https://arxiv.org/abs/1607.03474)). The model uses variational dropout plus tying of the input and output mappings, and the paper reports that reducing weight decay for the best ten-layer model yields the 67.9/65.4 validation/test pair. The paper's comparison table places this against RNN-LDA + KN-5 + cache at 92.0, Conv.+Highway+LSTM+dropout at 78.9, LSTM+dropout at 78.4, Variational LSTM at 75.0, and Variational LSTM + WT at 73.2. The authors state that RHNs outperform most single models as well as all previous ensembles; dynamic evaluation, cache/pointer, ensemble, and fine-tuning are not reported for the proposed model, with cache and pointer methods appearing only as baselines. Note that the Press and Wolf table lists the related RHN+BD+WT configuration at 66.0 rather than 65.4, a reproduction discrepancy in the literature ([Press & Wolf, 2016](https://arxiv.org/abs/1608.05859)).

### Press and Wolf (2016): Using the Output Embedding to Improve Language Models

The proposed large neural network language model with weight tying reaches **74.3** test perplexity, well below the 78.4 of the untied large baseline ([Press & Wolf, 2016](https://arxiv.org/abs/1608.05859)). The proposed small model with weight tying and projection regularization reaches 100.9, below the small baseline's 114.5. The paper's comparison table additionally contains a *Large + BD + WT* row at 73.2 and a *Large + BD + WD* row at 75.2; if the Bayesian-dropout-plus-weight-tying configuration is attributed to the paper's own weight-tied model family, then 73.2, not 74.3, would be the best figure. Because the supplied research note identifies the paper's proposed results as 74.3 and 100.9, this report adopts 74.3 as the headline value while flagging the 73.2 alternative explicitly. No dynamic evaluation, cache/pointer, ensemble, or fine-tuning settings are reported for these PTB numbers; all are single-model results.

### Inan et al. (2016): Tying Word Vectors and Word Classifiers

The supplied excerpt from this paper reports only the smallest configuration, a 200-unit model, with VD-LSTM at 148.6, VD-LSTM+AL at 143.7, VD-LSTM+RE at 140.9, and VD-LSTM+REAL at 138.4 test perplexity ([Inan et al., 2016](https://arxiv.org/abs/1611.01462)). The paper's large configuration, VD-LSTM + REAL with 51M parameters, is listed at **68.5** test perplexity in the Neural Architecture Search comparison table ([Zoph & Le, 2016](https://arxiv.org/abs/1611.01578)). The 68.5 figure is the paper's best single-model PTB word-level result and is the value tabulated here; the 138.4 figure is applicable only to the small 200-unit ablation family. The paper's contribution is a loss framework that ties input embeddings and output projections, and the reported results are single models without dynamic evaluation, cache, ensemble, or fine-tuning.

### Zoph and Le (2016): Neural Architecture Search with Reinforcement Learning

The best proposed model is the NAS cell with base 8 and shared embeddings, 54M parameters, at **62.4** test perplexity ([Zoph & Le, 2016](https://arxiv.org/abs/1611.01578)). Two smaller NAS configurations reach 64.0 (25M, base 8 and shared embeddings) and 67.9 (32M, base 8, 32M). The paper states that 62.4 is 3.6 perplexity better than the previous state of the art. The comparison table lists Merity et al. (2016) Zoneout + Variational LSTM (medium) at 80.6, Pointer Sentinel-LSTM (medium) at 70.9, Inan et al. (2016) VD-LSTM + REAL (large) at 68.5, and Zilly et al. (2016) Variational RHN with shared embeddings at 66.0. These are single-model test perplexities; dynamic evaluation, cache/pointer, ensemble, and fine-tuning are not reported for the NAS model on PTB, and cache/pointer appears only in baseline labels.

### Gated Recurrent Neural Tensor Network (2017)

This paper proposes GRURNTN and LSTMRNTN, described as a Gated Recurrent Unit Recurrent Neural Tensor Network and a Long Short-Term Memory Recurrent Neural Tensor Network. On word-level PTB, the test perplexities are **87.38** for GRURNTN and 96.97 for LSTMRNTN ([Gated Recurrent Neural Tensor Network, 2017](https://arxiv.org/abs/1706.02222)). GRURNTN reduces perplexity by 10.4 absolute (10.63% relative) from its GRURNN baseline at 97.78, and LSTMRNTN reduces perplexity by 11.29 absolute (10.42% relative) from its LSTMRNN baseline at 108.26. The remaining listed baselines are N-Gram at 141, RNNLM without dynamic evaluation at 124.7, RNNLM with dynamic evaluation at 123.2, SCRNN at 115, sRNN at 110.0, and DOT(S)-RNN at 107.5. The paper states that its baseline and proposed experiments did not use dynamic evaluation, and no cache/pointer, ensemble, or fine-tuning setting is reported. It is important to observe that the 87.38 best figure sits far above contemporaneous results from 2017 (58.3, 57.3, 54.44), which strongly indicates non-comparable experimental conditions — likely smaller models or lighter regularization — rather than a genuine step backward in the state of the art.

### Melis et al. (2017): On the State of the Art of Evaluation in Neural Language Models

After large-scale black-box hyperparameter tuning, the paper's best proposed model — a 4-layer LSTM with 24M parameters using shared input and output embeddings — reaches **58.3** test perplexity and 60.9 validation perplexity ([Melis et al., 2017](https://arxiv.org/abs/1707.05589)). The same table reports RHN at 64.8/62.2 (depth 5) and NAS at 62.1/59.7 (depth 1). The authors conclude that properly regularized standard LSTMs outperform more recent architectures, and they establish a new state of the art on PTB and WikiText-2. The paper explicitly refrains from including techniques that push perplexities lower because its aim is model comparison. Importantly, later references to Melis et al.'s 65.9 pertain to WikiText-2, not PTB, and must not be confused with the PTB 58.3 ([Melis et al., 2017](https://arxiv.org/abs/1707.05589)).

### Merity et al. (2017): Regularizing and Optimizing LSTM Language Models

The proposed AWD-LSTM (ASGD Weight-Dropped LSTM), a 3-layer tied-weight LSTM with 24M parameters, reaches **57.3** test perplexity and 60.0 validation perplexity as a single model without the cache pointer ([Merity et al., 2017](https://arxiv.org/abs/1708.02182)). Adding the continuous cache pointer lowers the test perplexity to 52.8 (53.9 validation), but the cache mechanism is excluded by the query. The table is explicitly captioned as single-model perplexity on validation and test sets. Fine-tuning is part of the reported training procedure; the paper's ablation table lists the no-fine-tuning variant at 58.8 test perplexity and states that removal of fine-tuning degrades performance. The paper reports that its vanilla LSTM improves the state of the art by approximately one unit on PTB (57.3 versus Melis et al.'s 58.3) and by 0.1 units on WikiText-2.

### Yang et al. (2017): Breaking the Softmax Bottleneck

The proposed AWD-LSTM-MoS reaches **54.44** test perplexity with fine-tuning and 55.97 without fine-tuning, both in single-model settings without dynamic evaluation ([Yang et al., 2017](https://arxiv.org/abs/1711.03953)). With dynamic evaluation the model reaches 47.69, but that result is excluded by the query's no-dynamic-evaluation rule. The paper's table also lists Merity et al.'s AWD-LSTM + continuous cache pointer at 53.9/52.8 and Krause et al.'s AWD-LSTM + dynamic evaluation at 51.6/51.1, both excluded for the same reasons. On the 1B Word dataset, the paper reports a MoS test perplexity of 37.10 against a Softmax baseline of 42.77, demonstrating that the mixture-of-softmaxes gain is not PTB-specific.

## Cross-Paper Observations

Three patterns emerge from the tabulation. First, the progression is near-monotonic over time: 78.4 (2014), 78.9 and 73.4 (2015), 65.4/74.3/68.5/62.4 (2016), and 58.3/57.3/54.44 (2017), with the Gated Recurrent Neural Tensor Network's 87.38 as a clear outlier produced under non-comparable conditions. Second, the largest single jumps come from regularization and parameter sharing rather than from exotic architectures: variational dropout (78.4 → 73.4), weight tying combined with recurrent highway depth (73.4 → 65.4), and the combination of weight tying, careful regularization, and softmax capacity (65.4 → 54.44). Third, headline numbers in this literature are routinely inflated by test-time methods that the query excludes; any reader comparing papers must therefore verify whether a quoted perplexity uses dynamic evaluation, a cache, fine-tuning, or model averaging.

## Caveats and Exclusions

The following results were deliberately excluded: Zaremba et al.'s averaged LSTMs (77.0, 73.3, 72.0, 73.6, 69.5, 68.7) and Gal's ten-model ensemble (68.7); Merity et al.'s continuous-cache-pointer result (52.8) and its no-fine-tuning ablation (58.8); Yang et al.'s dynamic-evaluation result (47.69); and all character-level, WikiText-2, enwik8, text8, IMDB, BBC, and 1B Word results. Two attribution ambiguities were flagged rather than silently resolved: the Press and Wolf 73.2 alternative, and the Inan et al. large-model figure of 68.5, which is sourced from a third-party comparison table rather than from the excerpted portion of the Inan paper itself. Finally, small reproduction discrepancies across papers (for example, 65.4 versus 66.0 for Variational RHN + WT, and 73.4 versus 75.0 for Variational LSTM) suggest that reported PTB perplexities carry an implicit variance of roughly one to two points across codebases and hyperparameter budgets.

## References

Gal, Y. (2015). *A theoretically grounded application of dropout in recurrent neural networks*. arXiv:1512.05287. https://arxiv.org/abs/1512.05287

*Gated recurrent neural tensor network*. (2017). arXiv:1706.02222. https://arxiv.org/abs/1706.02222

Inan, H., Khosravi, K., & Socher, R. (2016). *Tying word vectors and word classifiers: A loss framework for language modeling*. arXiv:1611.01462. https://arxiv.org/abs/1611.01462

Kim, Y., Jernite, Y., Sontag, D., & Rush, A. M. (2015). *Character-aware neural language models*. arXiv:1508.06615. https://arxiv.org/abs/1508.06615

Melis, G., Dyer, C., & Blunsom, P. (2017). *On the state of the art of evaluation in neural language models*. arXiv:1707.05589. https://arxiv.org/abs/1707.05589

Merity, S., Keskar, N. S., & Socher, R. (2017). *Regularizing and optimizing LSTM language models*. arXiv:1708.02182. https://arxiv.org/abs/1708.02182

Press, O., & Wolf, L. (2016). *Using the output embedding to improve language models*. arXiv:1608.05859. https://arxiv.org/abs/1608.05859

Yang, Z., Dai, Z., Salakhutdinov, R., & Cohen, W. W. (2017). *Breaking the softmax bottleneck: A high-rank RNN language model*. arXiv:1711.03953. https://arxiv.org/abs/1711.03953

Zaremba, W., Sutskever, I., & Vinyals, O. (2014). *Recurrent neural network regularization*. arXiv:1409.2329. https://arxiv.org/abs/1409.2329

Zilly, J. G., Srivastava, R. K., Koutník, J., & Schmidhuber, J. (2016). *Recurrent highway networks*. arXiv:1607.03474. https://arxiv.org/abs/1607.03474

Zoph, B., & Le, Q. V. (2016). *Neural architecture search with reinforcement learning*. arXiv:1611.01578. https://arxiv.org/abs/1611.01578