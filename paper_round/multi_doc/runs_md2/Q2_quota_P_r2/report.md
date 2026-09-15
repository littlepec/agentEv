# Word-Level Penn Treebank Test Perplexity of Proposed Single Models: A Comparative Report

## Scope, Inclusion Criteria, and Evaluation Protocol

This report compiles, for each of the eleven papers represented in the supplied source documents, the word-level Penn Treebank (PTB) test perplexity that the paper reports for **its own proposed model** under a **best single-model, no-dynamic-evaluation, no-cache/pointer** protocol. Penn Treebank word-level language modeling follows a standard protocol in this literature: the corpus is preprocessed by Mikolov et al. (2010), contains approximately one million tokens with a 10,000-word vocabulary, and uses the standard splits of sections 0–20 for training, 21–22 for validation, and 23–24 for test ([1508.06615.txt](https://arxiv.org/abs/1508.06615)); other descriptions match these statistics, for example 929k/73k/82k words ([1409.2329.txt](https://arxiv.org/abs/1409.2329)), 930k/74k/82k words ([1706.02222.txt](https://arxiv.org/abs/1706.02222)), and 923k/73k/82k words ([1611.01462.txt](https://arxiv.org/abs/1611.01462)).

Excluded from the main table, in accordance with the query, are: (a) **ensembles**, such as the 10- and 38-model averages reported by Zaremba et al. (2014) ([1409.2329_note.txt](https://arxiv.org/abs/1409.2329)) and the 10-model Variational LSTM ensemble ([1512.05287_note.txt](https://arxiv.org/abs/1512.05287)); (b) **dynamic evaluation**, such as RNNLM with dynamic evaluation at 123.2 ([1706.02222.txt](https://arxiv.org/abs/1706.02222)) and AWD-LSTM-MoS with dynamic evaluation at 47.69 ([1711.03953_note.txt](https://arxiv.org/abs/1711.03953)); and (c) **cache/pointer augmentation**, such as AWD-LSTM + continuous cache pointer at 52.8 ([1708.02182_note.txt](https://arxiv.org/abs/1708.02182)) and Pointer Sentinel-LSTM at 70.9 among baselines ([1611.01578.txt](https://arxiv.org/abs/1611.01578)). Fine-tuning is **not** excluded by the query, and it is retained where the source reports it as part of the single-model training procedure.

## Summary Table of Proposed-Model Results

| Paper (source document) | Proposed model | PTB word-level test PPL | Notes |
|---|---|---|---|
| Recurrent Neural Network Regularization (1409.2329) | Large regularized LSTM | **78.4** | Medium regularized LSTM: 82.7 ([1409.2329_note.txt](https://arxiv.org/abs/1409.2329)) |
| Character-Aware Neural Language Models (1508.06615) | LSTM-Char-Large | **78.9** | Small: 92.3 ([1508.06615_note.txt](https://arxiv.org/abs/1508.06615)) |
| Variational LSTM / MC dropout paper (1512.05287) | Large Variational LSTM, untied, MC dropout | **73.4** | Tied MC: 74.1; untied non-MC: 75.2 ([1512.05287_note.txt](https://arxiv.org/abs/1512.05287)) |
| Recurrent Highway Networks (1607.03474) | Variational RHN + weight tying | **65.4** | Without WT: 68.5 ([1607.03474_note.txt](https://arxiv.org/abs/1607.03474)) |
| Using the Output Embedding to Improve Language Models (1608.05859) | Large + weight tying | **74.3** | Large + Bayesian dropout + WT: 73.2 ([1608.05859.txt](https://arxiv.org/abs/1608.05859)) |
| Tying Word Vectors and Word Classifiers (1611.01462) | VD-RHN + reused embeddings (RE) | **66.0** | Paper calls this best overall; large VD-LSTM+REAL listed at 68.5 elsewhere ([1611.01462_note.txt](https://arxiv.org/abs/1611.01462); [1611.01578.txt](https://arxiv.org/abs/1611.01578)) |
| Neural Architecture Search with Reinforcement Learning (1611.01578) | NAS cell, base 8 + shared embeddings (54M) | **62.4** | Other NAS configs: 64.0 (25M), 67.9 (32M) ([1611.01578_note.txt](https://arxiv.org/abs/1611.01578)) |
| Gated Recurrent Neural Tensor Network (1706.02222) | GRURNTN | **87.38** | LSTMRNTN: 96.97 ([1706.02222_note.txt](https://arxiv.org/abs/1706.02222)) |
| On the State of the Art of Evaluation in Neural Language Models (1707.05589) | 4-layer LSTM (24M) | **58.3** | RHN: 62.2; NAS: 59.7 in same table ([1707.05589.txt](https://arxiv.org/abs/1707.05589)) |
| Regularizing and Optimizing LSTM Language Models (1708.02182) | AWD-LSTM, 3-layer, tied | **53.3** | Table 1 lists 57.3; no-fine-tuning ablation: 58.8 ([1708.02182_note.txt](https://arxiv.org/abs/1708.02182)) |
| Breaking the Softmax Bottleneck (1711.03953) | AWD-LSTM-MoS + finetune | **54.44** | Without finetune: 55.97 ([1711.03953_note.txt](https://arxiv.org/abs/1711.03953)) |

## Detailed Findings by Paper

### Recurrent Neural Network Regularization (1409.2329)

The paper trained two-layer regularized LSTMs unrolled for 35 steps with minibatches of 20, reporting a medium model at 82.7 and a large model at 78.4 as single models ([1409.2329_note.txt](https://arxiv.org/abs/1409.2329)); both figures appear as test perplexity in the paper's own comparison of single-model baselines including Pascanu et al. (107.5), Cheng et al. (100.0), and a non-regularized LSTM (114.5) ([1409.2329_note.txt](https://arxiv.org/abs/1409.2329)). The 78.4 large-model result became the reference baseline reused by many later papers. Ensemble averaging, excluded here, reaches 77.0 (2 medium), 73.3 (5 medium), 72.0 (10 medium), 73.6 (2 large), 69.5 (10 large), and 68.7 (38 large) ([1409.2329_note.txt](https://arxiv.org/abs/1409.2329)).

### Character-Aware Neural Language Models (1508.06615)

This model consumes characters through a CNN and highway network but predicts at the word level, so its PTB numbers are directly comparable as word-level perplexities ([1508.06615_note.txt](https://arxiv.org/abs/1508.06615)). The large character-aware LSTM reaches 78.9 and the small one 92.3 ([1508.06615_note.txt](https://arxiv.org/abs/1508.06615)); the underlying ablation table reports small/large perplexities of 100.3/84.6 with no highway layers, 92.3/79.7 with one, 90.1/78.9 with two, and 111.2/92.6 with an MLP layer instead ([1508.06615.txt](https://arxiv.org/abs/1508.06615)). The paper explicitly excludes ensembles from its comparison, stating that lower perplexities have been reported with model ensembles but are not comparable to the current work ([1508.06615_note.txt](https://arxiv.org/abs/1508.06615)).

### Variational LSTM with MC Dropout (1512.05287)

The large Variational LSTM with untied weights and Monte Carlo dropout at test time attains 73.4 test perplexity, reducing the Zaremba et al. large-model result from 78.4; the paper asserts this is the best single-model perplexity on PTB ([1512.05287_note.txt](https://arxiv.org/abs/1512.05287)). Validation perplexity for the large model improves from 82.2 to 77.3 with tying or 77.9 without ([1512.05287.txt](https://arxiv.org/abs/1512.05287)). The comparison table lists 79.7/75.0 (tied), 79.0/74.1 (tied + MC), and 79.7/75.2 (untied) for medium/large configurations ([1512.05287_note.txt](https://arxiv.org/abs/1512.05287)). Its ensemble result is excluded.

### Recurrent Highway Networks (1607.03474)

Variational RHN with weight tying (WT) reaches 67.9/65.4 validation/test with 23M parameters, and the best 10-layer model with reduced weight decay also yields 67.9/65.4 ([1607.03474_note.txt](https://arxiv.org/abs/1607.03474)). Without WT the model reports 68.5 test ([1607.03474_note.txt](https://arxiv.org/abs/1607.03474)). The experimental setup used a fixed 32M-parameter budget, batch size 20, sequence length 35, learning rate 0.2 with decay 1.02 starting at 20 epochs, weight decay 1e-7, and maximum gradient norm 10 ([1607.03474.txt](https://arxiv.org/abs/1607.03474)). The paper claims RHNs outperform most single models as well as all previous ensembles, while dynamic evaluation, cache/pointer, ensembles, and fine-tuning are not reported for the proposed model ([1607.03474_note.txt](https://arxiv.org/abs/1607.03474)).

### Using the Output Embedding to Improve Language Models (1608.05859)

Tying the input embedding to the output projection yields 74.3 test perplexity for the large NNLM (51M parameters) versus 78.4 for the untied 66M baseline; the small weight-tied plus projection-regularized model reaches 100.9 versus 114.5 for the small baseline ([1608.05859_note.txt](https://arxiv.org/abs/1608.05859)). The paper's table also includes Large + Bayesian dropout + weight decay at 75.2 and Large + BD + WT at 73.2, which is the lowest PTB figure for a model using the paper's tying proposal ([1608.05859.txt](https://arxiv.org/abs/1608.05859)). Non-dropout baselines listed are KN 5-gram 141, RNN 123, LSTM 117, Stack RNN 110, FOFE-FNN 108, Noisy LSTM 108.0, and Deep RNN 107.5 ([1608.05859_note.txt](https://arxiv.org/abs/1608.05859)). No dynamic evaluation, cache/pointer, ensemble, or fine-tuning is reported for these results.

### Tying Word Vectors and Word Classifiers (1611.01462)

Under the paper's augmented-loss framework, VD-RHN+RE attains 66.0 test (68.1 validation), which the paper describes as best overall ([1611.01462_note.txt](https://arxiv.org/abs/1611.01462)). The paper's own small 200-unit VD-LSTM variants are much weaker — 138.4 test for VD-LSTM+REAL, 140.9 for VD-LSTM+RE, 143.7 for VD-LSTM+AL, and 148.6 for the VD-LSTM baseline ([1611.01462.txt](https://arxiv.org/abs/1611.01462)) — while the large VD-LSTM+REAL is listed at 68.5 in a comparison table ([1611.01578.txt](https://arxiv.org/abs/1611.01578)). Cache, pointer, and ensemble baselines in the paper include RNN+LDA+KN-5+Cache (92.0), Pointer Sentinel-LSTM (70.9), 38 large LSTMs (68.7), and 10 large VD-LSTMs (68.7) ([1611.01462_note.txt](https://arxiv.org/abs/1611.01462)).

### Neural Architecture Search with Reinforcement Learning (1611.01578)

The best searched recurrent cell, NAS with base 8 and shared embeddings at 54M parameters, achieves 62.4 test perplexity; 64.0 (25M) and 67.9 (32M) are reported for other configurations ([1611.01578_note.txt](https://arxiv.org/abs/1611.01578)). The table labels all figures as single-model test perplexity on PTB, and the previous state of the art listed there is Zilly et al.'s Variational RHN with shared embeddings at 66.0 (24M), so the 62.4 result is a 3.6-point improvement ([1611.01578_note.txt](https://arxiv.org/abs/1611.01578)). Other listed baselines include Zoneout + Variational LSTM (medium) at 80.6 and Pointer Sentinel-LSTM (medium) at 70.9 ([1611.01578.txt](https://arxiv.org/abs/1611.01578)). No dynamic evaluation, cache/pointer, ensemble, or fine-tuning is reported for the NAS model.

### Gated Recurrent Neural Tensor Network (1706.02222)

GRURNTN achieves 87.38 test perplexity and LSTMRNTN 96.97, against their own GRURNN (97.78) and LSTMRNN (108.26) baselines ([1706.02222_note.txt](https://arxiv.org/abs/1706.02222)). The paper reports absolute reductions of 10.4 (10.63% relative) and 11.29 (10.42% relative), respectively, and states that experiments did not use dynamic evaluation ([1706.02222_note.txt](https://arxiv.org/abs/1706.02222)). Its table also lists N-Gram 141, RNNLM without dynamic evaluation 124.7, RNNLM with dynamic evaluation 123.2, SCRNN 115, sRNN 110.0, and DOT(S)-RNN 107.5 ([1706.02222.txt](https://arxiv.org/abs/1706.02222)).

### On the State of the Art of Evaluation in Neural Language Models (1707.05589)

With large-scale automatic hyperparameter tuning, the paper's best single model is a 4-layer LSTM with 24M parameters at 58.3 test (60.9 validation); RHN reaches 62.2 and NAS 59.7 in the same table ([1707.05589.txt](https://arxiv.org/abs/1707.05589)). The authors explicitly note their PTB and WikiText-2 results are for models without dynamic evaluation or caching, and that all results except Zaremba's use shared input and output embeddings ([1707.05589.txt](https://arxiv.org/abs/1707.05589)).

### Regularizing and Optimizing LSTM Language Models (1708.02182)

The paper's AWD-LSTM (ASGD Weight-Dropped LSTM), a 3-layer tied-weight LSTM with 24M parameters, is reported at 53.3 PTB test perplexity including the fine-tuning step, and 65.8 on WikiText-2; the source note states that Table 1 is captioned as single-model perplexity on validation and test sets, that the no-fine-tuning ablation is 58.8, and that removing fine-tuning degrades performance ([1708.02182_note.txt](https://arxiv.org/abs/1708.02182)). The paper text itself shows 60.0 validation / 57.3 test for the tied 3-layer model without the cache pointer, and 53.9/52.8 with the continuous cache pointer, which is excluded here ([1708.02182.txt](https://arxiv.org/abs/1708.02182); [1708.02182_note.txt](https://arxiv.org/abs/1708.02182)). The source materials are internally in tension about whether the headline is 53.3 or 57.3; both are reported above.

### Breaking the Softmax Bottleneck (1711.03953)

AWD-LSTM-MoS records 55.97 test without finetune and 54.44 with finetune as single models without dynamic evaluation; with dynamic evaluation it reaches 47.69, which is excluded ([1711.03953_note.txt](https://arxiv.org/abs/1711.03953)). The paper's Table 1 is captioned as single-model validation/test perplexity and lists AWD-LSTM + continuous cache pointer at 52.8 and Krause et al.'s AWD-LSTM + dynamic evaluation at 51.1 as comparison rows ([1711.03953.txt](https://arxiv.org/abs/1711.03953)).

## Comparative Observations and Assessment

Three patterns are evident in the compiled figures. First, **the frontier on PTB has moved steadily downward in the included, non-augmented single-model regime**, from 78.4 in 2014 ([1409.2329_note.txt](https://arxiv.org/abs/1409.2329)) to 73.4 ([1512.05287_note.txt](https://arxiv.org/abs/1512.05287)), 65.4 ([1607.03474_note.txt](https://arxiv.org/abs/1607.03474)), 62.4 ([1611.01578_note.txt](https://arxiv.org/abs/1611.01578)), and 58.3 ([1707.05589.txt](https://arxiv.org/abs/1707.05589)), culminating at 53.3–54.4 ([1708.02182_note.txt](https://arxiv.org/abs/1708.02182); [1711.03953_note.txt](https://arxiv.org/abs/1711.03953)). Second, **weight tying and shared input/output embeddings recur in nearly every strong result** (74.3, 65.4, 66.0, 62.4, 58.3, 53.3, 54.44), which is consistent with the tying analyses of Press and Wolf ([1608.05859_note.txt](https://arxiv.org/abs/1608.05859)) and Inan et al. ([1611.01462_note.txt](https://arxiv.org/abs/1611.01462)). Third, **parameter counts are not a reliable predictor** of quality: 24M-parameter models reach 53.3–58.3 while a 32M-parameter RHN reaches 65.4 and 51M–66M models reach 68.5–74.3 ([1708.02182_note.txt](https://arxiv.org/abs/1708.02182); [1707.05589.txt](https://arxiv.org/abs/1707.05589); [1607.03474_note.txt](https://arxiv.org/abs/1607.03474); [1608.05859_note.txt](https://arxiv.org/abs/1608.05859)).

My assessment is that these numbers should be read as **protocol-consistent but implementation-inconsistent**. The excluded techniques (dynamic evaluation, cache/pointer, ensembles) would substantially reorder the table — for example, 52.8 with a cache pointer and 47.69 with dynamic evaluation ([1708.02182_note.txt](https://arxiv.org/abs/1708.02182); [1711.03953_note.txt](https://arxiv.org/abs/1711.03953)) — and ensemble averaging alone worsens comparability, as Zaremba et al.'s 38-model average (68.7) is better than many single models ([1409.2329_note.txt](https://arxiv.org/abs/1409.2329)). The conclusions of Melis et al. support this caution: with extensive tuning, standard LSTMs outperform more recent architectures, implying that architecture-vs-architecture comparisons in this literature confound architecture with regularization and tuning quality ([1707.05589.txt](https://arxiv.org/abs/1707.05589)).

## Limitations of This Compilation

The figures above depend on the supplied source documents, some of which are third-party notes rather than the papers themselves; the notes occasionally conflict with paper tables (most notably the 53.3 versus 57.3 AWD-LSTM discrepancy) ([1708.02182_note.txt](https://arxiv.org/abs/1708.02182)). Attribution is also imperfect in one case: the 66.0 result from Inan et al. is the framework applied to the externally proposed VD-RHN architecture, while the same paper's own LSTM variants are much weaker at small scale ([1611.01462_note.txt](https://arxiv.org/abs/1611.01462); [1611.01462.txt](https://arxiv.org/abs/1611.01462)). Finally, training-set-size details vary slightly across sources (887,521 tokens; 929k/73k/82k; 930k/74k/82k) ([1512.05287.txt](https://arxiv.org/abs/1512.05287); [1409.2329.txt](https://arxiv.org/abs/1409.2329); [1706.02222.txt](https://arxiv.org/abs/1706.02222)).

## References

1. Recurrent neural network regularization (1409.2329.txt; 1409.2329_note.txt) [Source documents]. (2014). arXiv. https://arxiv.org/abs/1409.2329
2. Character-aware neural language models (1508.06615.txt; 1508.06615_note.txt) [Source documents]. (2015). arXiv. https://arxiv.org/abs/1508.06615
3. Variational LSTM with Monte Carlo dropout (1512.05287.txt; 1512.05287_note.txt) [Source documents]. (2015). arXiv. https://arxiv.org/abs/1512.05287
4. Recurrent highway networks (1607.03474.txt; 1607.03474_note.txt) [Source documents]. (2016). arXiv. https://arxiv.org/abs/1607.03474
5. Using the output embedding to improve language models (1608.05859.txt; 1608.05859_note.txt) [Source documents]. (2016). arXiv. https://arxiv.org/abs/1608.05859
6. Tying word vectors and word classifiers: A loss framework for language modeling (1611.01462.txt; 1611.01462_note.txt) [Source documents]. (2016). arXiv. https://arxiv.org/abs/1611.01462
7. Neural architecture search with reinforcement learning (1611.01578.txt; 1611.01578_note.txt) [Source documents]. (2016). arXiv. https://arxiv.org/abs/1611.01578
8. Gated recurrent neural tensor network (1706.02222.txt; 1706.02222_note.txt) [Source documents]. (2017). arXiv. https://arxiv.org/abs/1706.02222
9. On the state of the art of evaluation in neural language models (1707.05589.txt; 1707.05589_note.txt) [Source documents]. (2017). arXiv. https://arxiv.org/abs/1707.05589
10. Regularizing and optimizing LSTM language models (1708.02182.txt; 1708.02182_note.txt) [Source documents]. (2017). arXiv. https://arxiv.org/abs/1708.02182
11. Breaking the softmax bottleneck: A high-rank RNN language model (1711.03953.txt; 1711.03953_note.txt) [Source documents]. (2017). arXiv. https://arxiv.org/abs/1711.03953