# Reported Word-Level Penn Treebank Test Perplexity for Proposed Single Models: A Comparative Extraction Across Eleven Papers

## Scope, Inclusion Criteria, and Evaluation Protocol

This report answers a narrow question: for each paper supplied in the source corpus, what word-level Penn Treebank (PTB) test perplexity does the paper report for **its own proposed model**, using the best **single-model** configuration that does **not** rely on dynamic evaluation or a cache/pointer mechanism? Three boundary rules follow directly from that framing.

First, **ensemble results are excluded**, because the query asks for single-model figures. This exclusion is substantively important: the regularized-LSTM paper reports averaged models at 77.0 (2 medium), 73.3 (5 medium), 72.0 (10 medium), 73.6 (2 large), 69.5 (10 large), and 68.7 (38 large), all well below its single-model headline of 78.4 ([Recurrent neural network regularization, arXiv:1409.2329](https://arxiv.org/abs/1409.2329)). Similarly, an ensemble of 10 Variational LSTMs improves Zaremba et al.'s 69.5 to 68.7 ([Variational LSTM, arXiv:1512.05287](https://arxiv.org/abs/1512.05287)).

Second, **dynamic evaluation and cache/pointer variants are excluded**. This removes the 47.69 dynamic-evaluation figure reported for AWD-LSTM-MoS ([Breaking the softmax bottleneck, arXiv:1711.03953](https://arxiv.org/abs/1711.03953)) and the 52.8 continuous-cache-pointer variant of AWD-LSTM ([Regularizing and optimizing LSTM language models, arXiv:1708.02182](https://arxiv.org/abs/1708.02182)).

Third, **fine-tuning is retained**, because the query excludes only dynamic evaluation and caching. This is decisive for the two lowest numbers in the corpus: AWD-LSTM's 53.3 includes a fine-tuning step ([Regularizing and optimizing LSTM language models, arXiv:1708.02182](https://arxiv.org/abs/1708.02182)), and AWD-LSTM-MoS's 54.44 is likewise reported with fine-tuning ([Breaking the softmax bottleneck, arXiv:1711.03953](https://arxiv.org/abs/1711.03953)).

The evaluation protocol is consistent across the corpus. Papers use the standard training (0–20), validation (21–22), and test (23–24) splits with the standard preprocessing and word-level prediction over roughly 10k vocabulary ([Character-aware neural language models, arXiv:1508.06615](https://arxiv.org/abs/1508.06615)); perplexity is defined as $\exp(NLL/T)$ computed over the test set ([Character-aware neural language models, arXiv:1508.06615](https://arxiv.org/abs/1508.06615)); the Recurrent Highway Network experiments use the same dataset preprocessed by Mikolov et al. ([Recurrent highway networks, arXiv:1607.03474](https://arxiv.org/abs/1607.03474)); and the AWD-LSTM tables are explicitly captioned as "single model perplexity on validation and test sets for the Penn Treebank language modeling task" ([Regularizing and optimizing LSTM language models, arXiv:1708.02182](https://arxiv.org/abs/1708.02182)).

## Summary Table: Best Qualifying Single-Model Result per Paper

### Table 1. Best proposed single-model word-level PTB test perplexity, by paper

| Paper (arXiv ID) | Proposed model, best qualifying configuration | PTB test PPL |
|---|---|---|
| Recurrent Neural Network Regularization (1409.2329) | Large regularized LSTM (single model) | **78.4** |
| Character-Aware Neural Language Models (1508.06615) | LSTM-Char-Large (word-level predictions) | **78.9** |
| Variational LSTM (1512.05287) | Large Variational LSTM, untied weights, MC dropout | **73.4** |
| Recurrent Highway Networks (1607.03474) | Variational RHN + WT (10 layers, 23M params) | **65.4** |
| Using the Output Embedding to Improve Language Models (1608.05859) | Large NNLM + weight tying | **74.3** |
| Tying Word Vectors and Word Classifiers (1611.01462) | VD-LSTM+REAL (small, 200 units) | **≈140.6** (see caveat) |
| Neural Architecture Search with Reinforcement Learning (1611.01578) | NAS, base 8 + shared embeddings, 54M params | **62.4** |
| Gated Recurrent Neural Tensor Network (1706.02222) | GRURNTN | **87.38** |
| On the State of the Art of Evaluation in Neural Language Models (1707.05589) | 4-layer LSTM, 24M params | **58.3** |
| Regularizing and Optimizing LSTM Language Models (1708.02182) | AWD-LSTM, 3-layer, tied weights (with fine-tuning) | **53.3** |
| Breaking the Softmax Bottleneck (1711.03953) | AWD-LSTM-MoS (with fine-tuning) | **54.44** |

### Table 2. Ranked comparison (lower perplexity is better)

| Rank | Paper (arXiv ID) | Test PPL |
|---|---|---|
| 1 | Regularizing and Optimizing LSTM Language Models (1708.02182) | 53.3 |
| 2 | Breaking the Softmax Bottleneck (1711.03953) | 54.44 |
| 3 | On the State of the Art of Evaluation in Neural Language Models (1707.05589) | 58.3 |
| 4 | Neural Architecture Search with Reinforcement Learning (1611.01578) | 62.4 |
| 5 | Recurrent Highway Networks (1607.03474) | 65.4 |
| 6 | Variational LSTM (1512.05287) | 73.4 |
| 7 | Using the Output Embedding to Improve Language Models (1608.05859) | 74.3 |
| 8 | Recurrent Neural Network Regularization (1409.2329) | 78.4 |
| 9 | Character-Aware Neural Language Models (1508.06615) | 78.9 |
| 10 | Gated Recurrent Neural Tensor Network (1706.02222) | 87.38 |
| 11 | Tying Word Vectors and Word Classifiers (1611.01462) | ≈140.6 (small-scale model; not comparable) |

## Paper-by-Paper Detail

### Regularized LSTMs and dropout-based models

The earliest paper in the corpus reports a medium regularized LSTM at 82.7 and a large regularized LSTM at 78.4, both as single models ([Recurrent neural network regularization, arXiv:1409.2329](https://arxiv.org/abs/1409.2329)). Its listed single-model baselines are Pascanu et al. 2013 at 107.5, Cheng et al. at 100.0, and a non-regularized LSTM at 114.5, so the proposed models improve on all three ([Recurrent neural network regularization, arXiv:1409.2329](https://arxiv.org/abs/1409.2329)). The paper reports no dynamic evaluation, cache/pointer, or fine-tuning settings for PTB perplexity ([Recurrent neural network regularization, arXiv:1409.2329](https://arxiv.org/abs/1409.2329)).

The Variational LSTM paper reports 73.4 for the large model with untied weights and MC dropout at test time, describing a reduction from 78.4 to 73.4 and claiming this to be the best single-model perplexity on PTB at the time ([Variational LSTM, arXiv:1512.05287](https://arxiv.org/abs/1512.05287)). Its comparison table situates 73.4 against non-regularized early stopping (medium 121.7, large 127.4), Moon et al. December 2015 (97.0/118.7), Moon et al. plus embedding dropout (86.5/86.0), Zaremba et al. 2014 (82.7/78.4), and its own tied and untied variants (75.0, 74.1, 75.2, 73.4) ([Variational LSTM, arXiv:1512.05287](https://arxiv.org/abs/1512.05287)). No dynamic evaluation, cache/pointer, or fine-tuning is reported for PTB ([Variational LSTM, arXiv:1512.05287](https://arxiv.org/abs/1512.05287)).

### Character-level input, word-level prediction

The character-aware language model predicts at the word level and reports 78.9 for LSTM-Char-Large and 92.3 for LSTM-Char-Small, both single-model results ([Character-aware neural language models, arXiv:1508.06615](https://arxiv.org/abs/1508.06615)). The paper explicitly excludes ensembles, stating that "lower perplexities have been reported with model ensembles… we do not include them here as they are not comparable to the current work," and reports no dynamic evaluation, cache/pointer, or fine-tuning PTB results ([Character-aware neural language models, arXiv:1508.06615](https://arxiv.org/abs/1508.06615)). Its best qualifying figure is therefore 78.9 — essentially tied with the large regularized LSTM baseline it compares against.

### Embedding-related model classes

The weight-tying paper reports 74.3 for a large NNLM with weight tying and 100.9 for a small NNLM with weight tying plus projection regularization, both single-model and without dynamic evaluation, cache/pointer, ensemble, or fine-tuning ([Using the output embedding to improve language models, arXiv:1608.05859](https://arxiv.org/abs/1608.05859)). Its baselines are the large NNLM of Zaremba et al. at 78.4 and the small NNLM at 114.5, plus non-dropout comparators: KN 5-gram 141, RNN 123, LSTM 117, Stack RNN 110, FOFE-FNN 108, Noisy LSTM 108.0, and Deep RNN 107.5 ([Using the output embedding to improve language models, arXiv:1608.05859](https://arxiv.org/abs/1608.05859)).

The tied-loss-framework paper is the one case in this corpus where the extraction is not clean. The supplied excerpt contains only a small (200-unit) comparison table: VD-LSTM reaches 159.1/148.0 and 163.19/148.6; VD-LSTM+AL reaches 153.0/142.5 and 156.4/143.7; VD-LSTM+RE reaches 152.4/141.9 and 152.5/140.9; and VD-LSTM+REAL reaches 149.3/140.6 and 150.5/138.4, under a caption describing comparison to previous state of the art on word-level validation and test perplexities on PTB ([Tying word vectors and word classifiers, arXiv:1611.01462](https://arxiv.org/abs/1611.01462)). The strongest proposed figure in the excerpt is therefore approximately 140.6 (with a second test-column value of 138.4), but the excerpt does not make it unambiguous which of the two column pairs corresponds to PTB, and the paper's large-model PTB number is not present in the supplied text ([Tying word vectors and word classifiers, arXiv:1611.01462](https://arxiv.org/abs/1611.01462)). This value reflects a 200-unit model and should not be read as the paper's headline scale ([Tying word vectors and word classifiers, arXiv:1611.01462](https://arxiv.org/abs/1611.01462)).

### Highway recurrency and architecture search

The Recurrent Highway Network paper reports 65.4 for Variational RHN + WT (23M parameters, validation 67.9) and 68.5 for Variational RHN without weight tying ([Recurrent highway networks, arXiv:1607.03474](https://arxiv.org/abs/1607.03474)). Test scores improve as recurrence depth increases from 1 to 10 at a fixed 32M parameter budget, and further weight-decay reduction yields 67.9/65.4 validation/test ([Recurrent highway networks, arXiv:1607.03474](https://arxiv.org/abs/1607.03474)). The best PTB result is a single model; dynamic evaluation, cache/pointer, ensemble, and fine-tuning are not reported for the proposed model, with cache/pointer and ensembles appearing only as baselines or comparisons ([Recurrent highway networks, arXiv:1607.03474](https://arxiv.org/abs/1607.03474)).

The Neural Architecture Search paper reports 62.4 test perplexity for its best searched architecture (base 8 with shared embeddings, 54M parameters), together with 64.0 (base 8 + shared embeddings, 25M) and 67.9 (base 8, 32M) for other configurations ([Neural architecture search with reinforcement learning, arXiv:1611.01578](https://arxiv.org/abs/1611.01578)). The best listed baseline is 66.0 for Zilly et al. 2016 Variational RHN with shared embeddings, so the 62.4 result represents a 3.6 perplexity improvement over that baseline ([Neural architecture search with reinforcement learning, arXiv:1611.01578](https://arxiv.org/abs/1611.01578)). No dynamic evaluation, cache/pointer, ensemble, or fine-tuning is reported for the searched model on PTB ([Neural architecture search with reinforcement learning, arXiv:1611.01578](https://arxiv.org/abs/1611.01578)).

### Evaluation-focused and tensor/mixture models

The evaluation-methodology paper reports 58.3 on PTB for its own proposed 4-layer LSTM with 24M parameters, noting that at that scale all depths obtain similar results, reaching 58.3 at depth 4 ([On the state of the art of evaluation in neural language models, arXiv:1707.05589](https://arxiv.org/abs/1707.05589)). The result is a single model without dynamic evaluation, cache/pointer, ensemble, or fine-tuning; the authors deliberately refrain from including techniques that push perplexities lower in order to make fair architectural comparisons ([On the state of the art of evaluation in neural language models, arXiv:1707.05589](https://arxiv.org/abs/1707.05589)).

The Gated Recurrent Neural Tensor Network paper reports 87.38 for GRURNTN and 96.97 for LSTMRNTN, both individual models, reducing their own baselines from 97.78 (GRURNN) and 108.26 (LSTMRNN) — absolute reductions of 10.4 and 11.29 and relative reductions of 10.63% and 10.42% ([Gated recurrent neural tensor network, arXiv:1706.02222](https://arxiv.org/abs/1706.02222)). The paper states that baseline and proposed experiments did not use dynamic evaluation, and reports no cache/pointer, ensemble, or fine-tuning setting ([Gated recurrent neural tensor network, arXiv:1706.02222](https://arxiv.org/abs/1706.02222)). Its listed baselines include GRURNN (97.78), LSTMRNN (108.26), N-Gram (141), RNNLM without dynamic evaluation (124.7), RNNLM with dynamic evaluation (123.2), SCRNN (115), sRNN (110.0), and DOT(S)-RNN (107.5) ([Gated recurrent neural tensor network, arXiv:1706.02222](https://arxiv.org/abs/1706.02222)).

The AWD-LSTM paper reports 53.3 for a 3-layer tied-weight AWD-LSTM on PTB as a single model without cache/pointer, including the fine-tuning step ([Regularizing and optimizing LSTM language models, arXiv:1708.02182](https://arxiv.org/abs/1708.02182)). Its no-fine-tuning ablation is 58.8 ([Regularizing and optimizing LSTM language models, arXiv:1708.02182](https://arxiv.org/abs/1708.02182)). Table 1 shows 53.3 beating the best listed baseline, Melis et al. 2017 4-layer skip-connection LSTM (tied) at 58.3, and the continuous-cache-pointer variant reaches 52.8, which is excluded here by the cache criterion ([Regularizing and optimizing LSTM language models, arXiv:1708.02182](https://arxiv.org/abs/1708.02182)).

Finally, the mixture-of-softmaxes paper reports 55.97 for AWD-LSTM-MoS without fine-tuning and 54.44 with fine-tuning, both single-model and without dynamic evaluation, plus 47.69 with dynamic evaluation (excluded) ([Breaking the softmax bottleneck, arXiv:1711.03953](https://arxiv.org/abs/1711.03953)). No cache/pointer or ensemble results are reported for the proposed model ([Breaking the softmax bottleneck, arXiv:1711.03953](https://arxiv.org/abs/1711.03953)).

## Cross-Cutting Observations and Assessment

Three analytic points are worth stating explicitly. First, **the trajectory is monotone downward over time**: 78.4 → 78.9 → 74.3 → 73.4 → 65.4 → 62.4 → 58.3 → 54.44 → 53.3 across the corpus ([Recurrent neural network regularization, arXiv:1409.2329](https://arxiv.org/abs/1409.2329); [Character-aware neural language models, arXiv:1508.06615](https://arxiv.org/abs/1508.06615); [Using the output embedding to improve language models, arXiv:1608.05859](https://arxiv.org/abs/1608.05859); [Variational LSTM, arXiv:1512.05287](https://arxiv.org/abs/1512.05287); [Recurrent highway networks, arXiv:1607.03474](https://arxiv.org/abs/1607.03474); [Neural architecture search with reinforcement learning, arXiv:1611.01578](https://arxiv.org/abs/1611.01578); [On the state of the art of evaluation in neural language models, arXiv:1707.05589](https://arxiv.org/abs/1707.05589); [Breaking the softmax bottleneck, arXiv:1711.03953](https://arxiv.org/abs/1711.03953); [Regularizing and optimizing LSTM language models, arXiv:1708.02182](https://arxiv.org/abs/1708.02182)). The two exceptions are the character-aware model at 78.9, which is competitive rather than state of the art ([Character-aware neural language models, arXiv:1508.06615](https://arxiv.org/abs/1508.06615)), and the tensor-network paper at 87.38, which compares against much weaker baselines ([Gated recurrent neural tensor network, arXiv:1706.02222](https://arxiv.org/abs/1706.02222)).

Second, **the fine-tuning boundary determines the top of the table**. Under the query's rule, AWD-LSTM leads at 53.3 and AWD-LSTM-MoS follows at 54.44 ([Regularizing and optimizing LSTM language models, arXiv:1708.02182](https://arxiv.org/abs/1708.02182); [Breaking the softmax bottleneck, arXiv:1711.03953](https://arxiv.org/abs/1711.03953)). Had fine-tuning been excluded, the leading positions would be 55.97 for AWD-LSTM-MoS and 58.8 for AWD-LSTM ([Breaking the softmax bottleneck, arXiv:1711.03953](https://arxiv.org/abs/1711.03953); [Regularizing and optimizing LSTM language models, arXiv:1708.02182](https://arxiv.org/abs/1708.02182)), with the 58.3 skip-connection LSTM of the evaluation paper essentially tied ([On the state of the art of evaluation in neural language models, arXiv:1707.05589](https://arxiv.org/abs/1707.05589)). The reader should therefore treat the 53.3 and 54.44 figures as configuration-dependent, not as bare architecture scores.

Third, **one cross-source discrepancy exists for the same architecture family**. The RHN paper reports 65.4 for Variational RHN + WT ([Recurrent highway networks, arXiv:1607.03474](https://arxiv.org/abs/1607.03474)), whereas the NAS paper's baseline table lists "Zilly et al. 2016 – Variational RHN, shared embeddings" at 66.0 ([Neural architecture search with reinforcement learning, arXiv:1611.01578](https://arxiv.org/abs/1611.01578)). Weight tying and shared embeddings are the same mechanism, so the 0.6 difference most plausibly reflects different reported configurations or tuning steps rather than a substantive disagreement; the NAS paper's own claim of a 3.6-perplexity gain is stated against the 66.0 anchor ([Neural architecture search with reinforcement learning, arXiv:1611.01578](https://arxiv.org/abs/1611.01578)).

The principal limitation of this extraction concerns the tied-loss-framework paper, where the supplied excerpt supports only a small-model figure near 140.6 (or 138.4) and does not unambiguously map test columns to PTB ([Tying word vectors and word classifiers, arXiv:1611.01462](https://arxiv.org/abs/1611.01462)). It is also worth noting that the corpus's PTB results are overwhelmingly single-model and non-augmented: dynamic evaluation, cache/pointer, ensembles, and fine-tuning are absent from most papers, and where they appear they are explicitly flagged or excluded from comparability ([Character-aware neural language models, arXiv:1508.06615](https://arxiv.org/abs/1508.06615); [Recurrent highway networks, arXiv:1607.03474](https://arxiv.org/abs/1607.03474); [On the state of the art of evaluation in neural language models, arXiv:1707.05589](https://arxiv.org/abs/1707.05589)).

## References

- *Breaking the Softmax Bottleneck: A High-Rank RNN Language Model* [arXiv:1711.03953]. (n.d.). https://arxiv.org/abs/1711.03953
- *Character-Aware Neural Language Models* [arXiv:1508.06615]. (n.d.). https://arxiv.org/abs/1508.06615
- *Gated Recurrent Neural Tensor Network* [arXiv:1706.02222]. (n.d.). https://arxiv.org/abs/1706.02222
- *Neural Architecture Search with Reinforcement Learning* [arXiv:1611.01578]. (n.d.). https://arxiv.org/abs/1611.01578
- *On the State of the Art of Evaluation in Neural Language Models* [arXiv:1707.05589]. (n.d.). https://arxiv.org/abs/1707.05589
- *Recurrent Highway Networks* [arXiv:1607.03474]. (n.d.). https://arxiv.org/abs/1607.03474
- *Recurrent Neural Network Regularization* [arXiv:1409.2329]. (n.d.). https://arxiv.org/abs/1409.2329
- *Regularizing and Optimizing LSTM Language Models* [arXiv:1708.02182]. (n.d.). https://arxiv.org/abs/1708.02182
- *Tying Word Vectors and Word Classifiers: A Loss Framework for Language Modeling* [arXiv:1611.01462]. (n.d.). https://arxiv.org/abs/1611.01462
- *Using the Output Embedding to Improve Language Models* [arXiv:1608.05859]. (n.d.). https://arxiv.org/abs/1608.05859
- *Variational LSTM / Monte-Carlo Dropout for Recurrent Networks* [arXiv:1512.05287]. (n.d.). https://arxiv.org/abs/1512.05287

*Note on citations: the supplied corpus provides arXiv identifiers, note titles, and quoted results but does not supply author metadata or publication years, so references are given by work title and identifier rather than by author–date entries.*