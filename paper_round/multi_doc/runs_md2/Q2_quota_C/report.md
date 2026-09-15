# Word-Level Penn Treebank Test Perplexity for Proposed Single Models: A Source-by-Source Review

## Scope and Selection Criteria

This report extracts, for each provided paper, the best word-level Penn Treebank (PTB) test perplexity that the paper reports for its own proposed model under a single-model evaluation without dynamic evaluation or cache/pointer augmentation. The selection criteria are therefore:

- **Word-level PTB test perplexity**, not validation perplexity, not character-level bits-per-character, and not WikiText-2 or other corpora.
- **Own proposed model**, not a third-party baseline reproduced for comparison.
- **Single model only**, so ensemble or model-averaging results are excluded.
- **No dynamic evaluation**, and **no cache/pointer** mechanism.
- **Fine-tuning is not excluded by the query**, because the query excludes only dynamic evaluation and cache. Where a paper reports both fine-tuned and non-fine-tuned single-model numbers, the best single-model result without dynamic evaluation or cache is used, and the alternative is noted.

This distinction matters because several papers report lower numbers only when they use an ensemble, dynamic evaluation, or a continuous cache. For example, Zaremba et al. (2014) report averaged results down to 68.7, but their single-model large regularized LSTM is 78.4 ([Zaremba et al., 2014](https://arxiv.org/abs/1409.2329)). Similarly, Gal and Ghahramani (2016) report an ensemble result of 68.7 with 10 Variational LSTMs, but the single-model large Variational LSTM with MC dropout and untied weights is 73.4 ([Gal & Ghahramani, 2016](https://arxiv.org/abs/1512.05287)). Merity et al. (2017) report 52.8 with a continuous cache pointer, but their single-model AWD-LSTM without cache is 57.3 ([Merity et al., 2017](https://arxiv.org/abs/1708.02182)). These excluded settings are important because they can obscure the comparable single-model performance of the proposed architectures.

## Summary Table

| Paper Title | Proposed Model | PTB Word-Level Test PPL (Best Single Model, No Dynamic Evaluation/Cache) |
|---|---:|---:|
| Recurrent Neural Network Regularization (Zaremba et al., 2014) | Large regularized LSTM | 78.4 |
| Character-Aware Neural Language Models (Kim et al., 2016) | LSTM-Char-Large | 78.9 |
| Dropout as a Bayesian Approximation / Variational LSTM (Gal & Ghahramani, 2016) | Large Variational LSTM, untied weights, MC dropout | 73.4 |
| Recurrent Highway Networks (Zilly et al., 2017) | Variational RHN + WT | 65.4 |
| Using the Output Embedding to Improve Language Models (Press & Wolf, 2016) | Large + Weight Tying | 74.3 |
| Tying Word Vectors and Word Classifiers (Inan et al., 2016) | VD-LSTM + REAL (large) | 68.5 |
| Neural Architecture Search with Reinforcement Learning (Zoph & Le, 2016) | NAS with base 8 and shared embeddings, 54M | 62.4 |
| Gated Recurrent Neural Tensor Network (2017) | GRURNTN | 87.38 |
| On the State of the Art of Evaluation in Neural Language Models (Melis et al., 2017) | 4-layer LSTM, 24M | 58.3 |
| Regularizing and Optimizing LSTM Language Models (Merity et al., 2017) | AWD-LSTM (3-layer LSTM tied) | 57.3 |
| Breaking the Softmax Bottleneck (Yang et al., 2017) | AWD-LSTM-MoS with finetune | 54.44 |

## Detailed Findings by Paper

### Recurrent Neural Network Regularization (Zaremba et al., 2014)

Zaremba et al. (2014) propose regularized LSTMs for word-level language modeling on PTB. The paper reports a medium regularized LSTM at 82.7 test perplexity and a large regularized LSTM at 78.4 test perplexity ([Zaremba et al., 2014](https://arxiv.org/abs/1409.2329)). These are single-model results. The paper also reports model-averaging results, including 2 medium regularized LSTMs at 77.0, 5 medium regularized LSTMs at 73.3, 10 medium regularized LSTMs at 72.0, 2 large regularized LSTMs at 73.6, 10 large regularized LSTMs at 69.5, and 38 large regularized LSTMs at 68.7 ([Zaremba et al., 2014](https://arxiv.org/abs/1409.2329)). Those averaged results are excluded by the single-model criterion. The best proposed single-model result is therefore **78.4**.

### Character-Aware Neural Language Models (Kim et al., 2016)

Kim et al. (2016) propose a character-aware neural language model that builds word representations from characters and then predicts words at the word level. The paper reports LSTM-Char-Large at 78.9 test perplexity and LSTM-Char-Small at 92.3 test perplexity ([Kim et al., 2016](https://arxiv.org/abs/1508.06615)). The authors explicitly exclude ensembles, stating that lower perplexities have been reported with model ensembles but are not comparable to the current work ([Kim et al., 2016](https://arxiv.org/abs/1508.06615)). No dynamic evaluation, cache/pointer, or fine-tuning PTB result appears in the provided material. The best proposed single-model result is **78.9**.

### Dropout as a Bayesian Approximation / Variational LSTM (Gal & Ghahramani, 2016)

Gal and Ghahramani (2016) propose Variational LSTMs, applying a Bayesian interpretation of dropout. The paper reports 73.4 test perplexity for the large Variational LSTM with untied weights and MC dropout at test time ([Gal & Ghahramani, 2016](https://arxiv.org/abs/1512.05287)). The paper states that test perplexity is reduced from 78.4 down to 73.4 with MC dropout and untied weights, and that these are currently the best single-model perplexities on PTB ([Gal & Ghahramani, 2016](https://arxiv.org/abs/1512.05287)). The paper also reports an ensemble result: 10 Variational LSTMs with MC dropout improve Zaremba et al.’s test perplexity from 69.5 to 68.7 ([Gal & Ghahramani, 2016](https://arxiv.org/abs/1512.05287)). That ensemble is excluded. The best proposed single-model result is **73.4**.

### Recurrent Highway Networks (Zilly et al., 2017)

Zilly et al. (2017) propose Recurrent Highway Networks (RHNs) and evaluate them on PTB word-level language modeling. The best proposed Penn Treebank word-level test perplexity is 65.4 for Variational RHN + WT ([Zilly et al., 2017](https://arxiv.org/abs/1607.03474)). The paper also reports 68.5 test perplexity for Variational RHN without weight tying ([Zilly et al., 2017](https://arxiv.org/abs/1607.03474)). The best 10-layer model with reduced weight decay improves to 67.9/65.4 validation/test perplexity ([Zilly et al., 2017](https://arxiv.org/abs/1607.03474)). This setting uses variational dropout and weight tying of input and output mappings. The result is a single model; dynamic evaluation, cache/pointer, ensemble, and fine-tuning are not reported for the proposed model ([Zilly et al., 2017](https://arxiv.org/abs/1607.03474)). The best proposed single-model result is **65.4**.

### Using the Output Embedding to Improve Language Models (Press & Wolf, 2016)

Press and Wolf (2016) propose weight tying of input embeddings and output embeddings for neural language models. The paper reports a large NNLM with weight tying at 74.3 test perplexity ([Press & Wolf, 2016](https://arxiv.org/abs/1608.05859)). It also reports a small NNLM with weight tying and projection regularization at 100.9 test perplexity ([Press & Wolf, 2016](https://arxiv.org/abs/1608.05859)). Both numbers are single-model results without dynamic evaluation, cache/pointer, ensemble, or fine-tuning ([Press & Wolf, 2016](https://arxiv.org/abs/1608.05859)). The paper’s broader comparison table also includes a combined Large + BD + WT row at 73.2 test perplexity, but the provided research note identifies the proposed large weight-tied model as Large + Weight Tying at 74.3 ([Press & Wolf, 2016](https://arxiv.org/abs/1608.05859)). Using the paper’s core weight-tied large model, the best proposed single-model result is **74.3**.

### Tying Word Vectors and Word Classifiers (Inan et al., 2016)

Inan et al. (2016) propose a loss framework that ties word vectors and word classifiers. The provided direct excerpt from this paper shows small-model variants such as VD-LSTM, VD-LSTM+AL, VD-LSTM+RE, and VD-LSTM+REAL, with the small VD-LSTM+REAL reaching 138.4 test perplexity ([Inan et al., 2016](https://arxiv.org/abs/1611.01462)). However, the best proposed large result is listed in the Neural Architecture Search comparison as “Inan et al. 2016 - VD-LSTM + REAL (large) 51M 68.5 68.5” ([Zoph & Le, 2016](https://arxiv.org/abs/1611.01578)). That large VD-LSTM + REAL result is a single-model PTB test perplexity without dynamic evaluation or cache. The best proposed single-model result is therefore **68.5**, with the caveat that the direct provided excerpt from Inan et al. shows only the small-model rows.

### Neural Architecture Search with Reinforcement Learning (Zoph & Le, 2016)

Zoph and Le (2016) apply Neural Architecture Search (NAS) to PTB recurrent cell design. The best NAS model, NAS with base 8 and shared embeddings at 54M parameters, achieves 62.4 test perplexity ([Zoph & Le, 2016](https://arxiv.org/abs/1611.01578)). The paper also reports 64.0 and 67.9 for other NAS configurations ([Zoph & Le, 2016](https://arxiv.org/abs/1611.01578)). These numbers are described as single-model perplexity on the test set of the PTB language modeling task ([Zoph & Le, 2016](https://arxiv.org/abs/1611.01578)). The paper does not report dynamic evaluation, cache/pointer, ensemble, or fine-tuning for the NAS model on PTB ([Zoph & Le, 2016](https://arxiv.org/abs/1611.01578)). The best proposed single-model result is **62.4**.

### Gated Recurrent Neural Tensor Network (2017)

The Gated Recurrent Neural Tensor Network paper proposes GRURNTN and LSTMRNTN. For word-level PTB language modeling, it reports test perplexity 87.38 for GRURNTN and 96.97 for LSTMRNTN ([Gated Recurrent Neural Tensor Network, 2017](https://arxiv.org/abs/1706.02222)). These are individual models. The paper states that baseline and proposed model experiments did not use dynamic evaluation ([Gated Recurrent Neural Tensor Network, 2017](https://arxiv.org/abs/1706.02222)). No cache/pointer, ensemble, or fine-tuning setting is reported for the proposed word-level results. The best proposed single-model result is **87.38**.

### On the State of the Art of Evaluation in Neural Language Models (Melis et al., 2017)

Melis et al. (2017) report a best word-level test perplexity of 58.3 on PTB for their own proposed model, a 4-layer LSTM with 24M parameters ([Melis et al., 2017](https://arxiv.org/abs/1707.05589)). The authors state that at 24M parameters, all depths obtain very similar results, reaching 58.3 at depth 4 ([Melis et al., 2017](https://arxiv.org/abs/1707.05589)). This result is a single model without dynamic evaluation, cache/pointer, ensemble, or fine-tuning. The paper explicitly refrains from including techniques that push perplexities lower, because its aim is to improve model comparisons for the architectures under study ([Melis et al., 2017](https://arxiv.org/abs/1707.05589)). The best proposed single-model result is **58.3**.

### Regularizing and Optimizing LSTM Language Models (Merity et al., 2017)

Merity et al. (2017) propose AWD-LSTM, an ASGD Weight-Dropped LSTM. The paper reports a word-level PTB test perplexity of 57.3 for AWD-LSTM, a 3-layer LSTM with tied weights, as a single model without cache/pointer ([Merity et al., 2017](https://arxiv.org/abs/1708.02182)). Table 1 is captioned as single-model perplexity on validation and test sets for the PTB language modeling task ([Merity et al., 2017](https://arxiv.org/abs/1708.02182)). This result includes the fine-tuning step. The paper also reports a continuous cache pointer variant at 52.8 test perplexity, which is excluded by the no-cache criterion ([Merity et al., 2017](https://arxiv.org/abs/1708.02182)). The no-fine-tuning ablation is listed at 58.8 test perplexity, and removal of fine-tuning degrades performance ([Merity et al., 2017](https://arxiv.org/abs/1708.02182)). Because the query excludes only dynamic evaluation and cache, the best single-model result without cache is **57.3**.

### Breaking the Softmax Bottleneck (Yang et al., 2017)

Yang et al. (2017) propose AWD-LSTM-MoS, a Mixture of Softmaxes language model. The paper reports 55.97 for AWD-LSTM-MoS without finetune and 54.44 for AWD-LSTM-MoS with finetune as single-model results without dynamic evaluation ([Yang et al., 2017](https://arxiv.org/abs/1711.03953)). With dynamic evaluation, the paper reports 47.69 for AWD-LSTM-MoS + dynamic evaluation ([Yang et al., 2017](https://arxiv.org/abs/1711.03953)). The paper does not report cache/pointer or ensemble methods for its proposed model on PTB; it reports results with and without dynamic evaluation and finetuning ([Yang et al., 2017](https://arxiv.org/abs/1711.03953)). Because the query excludes dynamic evaluation and cache but does not exclude fine-tuning, the best proposed single-model result is **54.44**. If fine-tuning were also excluded, the corresponding number would be 55.97.

## Synthesis and Comparative Observations

The extracted results show a clear downward trajectory in single-model PTB word-level test perplexity across the provided papers. Early regularized LSTM work sits in the high-70s: Zaremba et al. (2014) report 78.4, and Kim et al. (2016) report 78.9 for a character-aware LSTM ([Zaremba et al., 2014](https://arxiv.org/abs/1409.2329); [Kim et al., 2016](https://arxiv.org/abs/1508.06615)). Variational dropout improves this to 73.4 ([Gal & Ghahramani, 2016](https://arxiv.org/abs/1512.05287)). Weight tying and recurrent highway networks push the number into the mid-60s to low-70s, with Inan et al. (2016) at 68.5, Press and Wolf (2016) at 74.3, and Zilly et al. (2017) at 65.4 ([Inan et al., 2016](https://arxiv.org/abs/1611.01462); [Press & Wolf, 2016](https://arxiv.org/abs/1608.05859); [Zilly et al., 2017](https://arxiv.org/abs/1607.03474)). NAS reports 62.4, Melis et al. (2017) report 58.3, Merity et al. (2017) report 57.3, and Yang et al. (2017) report 54.44 with fine-tuning ([Zoph & Le, 2016](https://arxiv.org/abs/1611.01578); [Melis et al., 2017](https://arxiv.org/abs/1707.05589); [Merity et al., 2017](https://arxiv.org/abs/1708.02182); [Yang et al., 2017](https://arxiv.org/abs/1711.03953)).

The most important comparative caution is that these numbers are not perfectly interchangeable. They differ in parameter budgets, preprocessing, weight tying, dropout variant, fine-tuning, and whether the reported figure is a single model or an ensemble. For example, Zaremba et al.’s 78.4 is a large regularized LSTM with 52M parameters, while Yang et al.’s 54.44 is a 22M AWD-LSTM-MoS with fine-tuning ([Zaremba et al., 2014](https://arxiv.org/abs/1409.2329); [Yang et al., 2017](https://arxiv.org/abs/1711.03953)). The Gated Recurrent Neural Tensor Network result at 87.38 is much higher than the state-of-the-art numbers in the other papers, but it is still the best proposed single-model result in its own paper ([Gated Recurrent Neural Tensor Network, 2017](https://arxiv.org/abs/1706.02222)).

Another caveat concerns fine-tuning. Merity et al. (2017) include fine-tuning in the 57.3 result, and Yang et al. (2017) include fine-tuning in the 54.44 result ([Merity et al., 2017](https://arxiv.org/abs/1708.02182); [Yang et al., 2017](https://arxiv.org/abs/1711.03953)). If one imposes a stricter “no fine-tuning” rule, the comparable numbers would be 58.8 for AWD-LSTM and 55.97 for AWD-LSTM-MoS ([Merity et al., 2017](https://arxiv.org/abs/1708.02182); [Yang et al., 2017](https://arxiv.org/abs/1711.03953)). The query, however, excludes only dynamic evaluation and cache, so the better fine-tuned single-model numbers are retained here.

Overall, the best directly reported single-model PTB word-level test perplexity in this set, without dynamic evaluation or cache, is **54.44** from Yang et al. (2017), followed by **57.3** from Merity et al. (2017) and **58.3** from Melis et al. (2017). The older regularized LSTM and character-aware models remain substantially higher, which is consistent with the later introduction of weight tying, variational dropout, recurrent highway connections, NAS, and advanced softmax mixtures.

## References

- Gal, Y., & Ghahramani, Z. (2016). *Dropout as a Bayesian approximation: Representing model uncertainty in deep learning*. arXiv. https://arxiv.org/abs/1512.05287
- Gated Recurrent Neural Tensor Network. (2017). *Gated recurrent neural tensor network*. arXiv. https://arxiv.org/abs/1706.02222
- Inan, H., Khosravi, K., & Socher, R. (2016). *Tying word vectors and word classifiers: A loss framework for language modeling*. arXiv. https://arxiv.org/abs/1611.01462
- Kim, Y., Jernite, Y., Sontag, D., & Rush, A. M. (2016). *Character-aware neural language models*. arXiv. https://arxiv.org/abs/1508.06615
- Melis, G., Dyer, C., & Blunsom, P. (2017). *On the state of the art of evaluation in neural language models*. arXiv. https://arxiv.org/abs/1707.05589
- Merity, S., Keskar, N. S., & Socher, R. (2017). *Regularizing and optimizing LSTM language models*. arXiv. https://arxiv.org/abs/1708.02182
- Press, O., & Wolf, L. (2016). *Using the output embedding to improve language models*. arXiv. https://arxiv.org/abs/1608.05859
- Yang, Z., Dai, Z., Salakhutdinov, R., & Cohen, W. W. (2017). *Breaking the softmax bottleneck: A high-rank RNN language model*. arXiv. https://arxiv.org/abs/1711.03953
- Zaremba, V., Vinyals, O., & Sutskever, I. (2014). *Recurrent neural network regularization*. arXiv. https://arxiv.org/abs/1409.2329
- Zilly, J. G., Srivastava, R. K., Koutník, J., & Schmidhuber, J. (2017). *Recurrent highway networks*. arXiv. https://arxiv.org/abs/1607.03474
- Zoph, B., & Le, Q. V. (2016). *Neural architecture search with reinforcement learning*. arXiv. https://arxiv.org/abs/1611.01578