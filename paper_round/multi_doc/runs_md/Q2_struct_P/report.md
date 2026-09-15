# Word-Level Penn Treebank Test Perplexities for Proposed Single Models: A Structured Extraction

## Introduction

The Penn Treebank (PTB) word-level language modeling benchmark remains a central evaluation for neural language models. In this task, models are trained to predict the next word, and performance is reported as test perplexity, where lower values indicate better predictive performance. The query asks for the best single-model PTB test perplexity reported by each provided paper for its own proposed model, specifically excluding dynamic evaluation and cache/pointer mechanisms. This report synthesizes the provided source notes and paper excerpts to produce a comparative table and a detailed discussion. The analysis covers eleven papers spanning regularized LSTMs, variational dropout, recurrent highway networks, weight tying, neural architecture search, and high-rank softmax models.

## Methodology

The extraction followed a set of inclusion rules. First, only results for the paper's own proposed model were considered; baseline results from other papers were excluded unless they helped identify the proposed model's number, as in the case of the Inan et al. (2016) model. Second, only single-model results were recorded; ensemble or model-averaging results were excluded. Third, dynamic evaluation and continuous cache pointer results were excluded. Fourth, fine-tuning was not excluded, because the query only specifies exclusion of dynamic evaluation and cache. When a paper reported multiple configurations, the lowest (best) PTB test perplexity satisfying these constraints was selected. When the provided source did not directly state the best number, it was inferred from a third-party comparison table included in the provided information. All numbers are word-level PTB test perplexities unless otherwise noted.

## Results

The following table lists each paper, its proposed model, and the best single-model PTB test perplexity without dynamic evaluation or cache.

| Paper Title | Proposed Model | Best Single-Model PTB Test Perplexity | Notes |
|-------------|----------------|----------------------------------------|-------|
| Regularizing and Optimizing LSTM Language Models | AWD-LSTM | 53.3 | With fine-tuning; no cache/pointer/dynamic evaluation ([1708.02182_note.txt](1708.02182_note.txt)) |
| Breaking the Softmax Bottleneck: A High-Rank RNN Language Model | AWD-LSTM-MoS | 54.44 | With fine-tuning; without dynamic evaluation ([1711.03953_note.txt](1711.03953_note.txt)) |
| On the State of the Art of Evaluation in Neural Language Models | 4-layer LSTM (24M) | 58.3 | Single model, no dynamic/cache ([1707.05589_note.txt](1707.05589_note.txt)) |
| Neural Architecture Search with Reinforcement Learning | NAS (base 8, shared embeddings, 54M) | 62.4 | Single model, no dynamic/cache ([1611.01578_note.txt](1611.01578_note.txt)) |
| Recurrent Highway Networks | Variational RHN + WT | 65.4 | Single model, no dynamic/cache ([1607.03474_note.txt](1607.03474_note.txt)) |
| Tying Word Vectors and Word Classifiers: A Loss Framework for Language Modeling | VD-LSTM+REAL (28M) | 69.0 | Reported as VD LSTM (Inan et al., 28M) in comparison table ([1707.05589_note.txt](1707.05589_note.txt)) |
| A Theoretically Grounded Application of Dropout in Recurrent Neural Networks | Variational LSTM (large, untied, MC dropout) | 73.4 | Single model, no dynamic/cache ([1512.05287_note.txt](1512.05287_note.txt)) |
| Using the Output Embedding to Improve Language Models | Large + Weight Tying | 74.3 | Single model, no dynamic/cache ([1608.05859_note.txt](1608.05859_note.txt)) |
| Recurrent Neural Network Regularization | Large regularized LSTM | 78.4 | Single model, no dynamic/cache ([1409.2329_note.txt](1409.2329_note.txt)) |
| Character-Aware Neural Language Models | LSTM-Char-Large | 78.9 | Single model, no dynamic/cache ([1508.06615_note.txt](1508.06615_note.txt)) |
| Gated Recurrent Neural Tensor Network | GRURNTN | 87.38 | Single model, no dynamic/cache ([1706.02222_note.txt](1706.02222_note.txt)) |

## Detailed Findings by Paper

### Regularizing and Optimizing LSTM Language Models (Merity et al., 2017)

The paper proposes AWD-LSTM and reports a single-model PTB test perplexity of 53.3 with fine-tuning and tied weights ([1708.02182_note.txt](1708.02182_note.txt)). The Table 1 caption explicitly identifies the results as single-model perplexity on validation and test sets ([1708.02182_note.txt](1708.02182_note.txt)). A no-fine-tuning ablation is reported at 58.8 test perplexity, and the paper states that removal of fine-tuning degrades performance ([1708.02182_note.txt](1708.02182_note.txt)). A continuous cache pointer variant achieves 52.8, but that result is excluded here because it uses a cache mechanism ([1708.02182_note.txt](1708.02182_note.txt)). Therefore, the best eligible single-model result is 53.3.

### Breaking the Softmax Bottleneck (Yang et al., 2018)

This paper introduces AWD-LSTM-MoS. Table 1 lists 55.97 for AWD-LSTM-MoS without fine-tuning and 54.44 with fine-tuning, both single-model results without dynamic evaluation ([1711.03953_note.txt](1711.03953_note.txt)). With dynamic evaluation, the model reaches 47.69, but that is excluded by the query ([1711.03953_note.txt](1711.03953_note.txt)). Consequently, the best eligible single-model result is 54.44 with fine-tuning.

### On the State of the Art of Evaluation in Neural Language Models (Melis et al., 2018)

The paper reports a best PTB test perplexity of 58.3 for a 4-layer LSTM with 24M parameters ([1707.05589_note.txt](1707.05589_note.txt)). The authors explicitly avoid techniques that push perplexities lower, such as dynamic evaluation or caching, because their aim is model comparison ([1707.05589_note.txt](1707.05589_note.txt)). Thus, 58.3 is the best eligible single-model result.

### Neural Architecture Search with Reinforcement Learning (Zoph & Le, 2017)

The best NAS configuration achieves 62.4 test perplexity on PTB with base 8 and shared embeddings and 54M parameters ([1611.01578_note.txt](1611.01578_note.txt)). Other configurations report 64.0 and 67.9 ([1611.01578_note.txt](1611.01578_note.txt)). The paper does not report dynamic evaluation, cache/pointer, ensemble, or fine-tuning for the NAS model on PTB ([1611.01578_note.txt](1611.01578_note.txt)). Therefore, 62.4 is the best eligible single-model result.

### Recurrent Highway Networks (Zilly et al., 2017)

The proposed Variational RHN + WT achieves 65.4 test perplexity ([1607.03474_note.txt](1607.03474_note.txt)). The paper also reports 68.5 for Variational RHN without WT ([1607.03474_note.txt](1607.03474_note.txt)). The best 10-layer model with reduced weight decay improves to 67.9/65.4 validation/test ([1607.03474.txt](1607.03474.txt)). No dynamic evaluation, cache/pointer, ensemble, or fine-tuning is reported for the proposed model ([1607.03474_note.txt](1607.03474_note.txt)). Thus, 65.4 is the best eligible single-model result.

### Tying Word Vectors and Word Classifiers (Inan et al., 2016)

The paper proposes weight-tied neural network language models. The provided source notes do not explicitly state the best PTB test perplexity in the paper's own note, but a third-party comparison table in the provided information lists "VD LSTM (Inan et al., 9M)" at 73.9 and "VD LSTM (Inan et al., 28M)" at 69.0 ([1707.05589_note.txt](1707.05589_note.txt)). The 28M model is the best proposed configuration, so 69.0 is recorded. The provided 1611.01462.txt excerpt shows small 200-unit models with PTB test perplexities around 140–148, but those are not the best proposed models ([1611.01462.txt](1611.01462.txt)). The paper's own note focuses on key questions regarding PTB perplexity ([1611.01462_note.txt](1611.01462_note.txt)). The 69.0 result is listed as a baseline comparison in the provided third-party note ([1707.05589_note.txt](1707.05589_note.txt)).

### A Theoretically Grounded Application of Dropout in Recurrent Neural Networks (Gal & Ghahramani, 2016)

The paper reports 73.4 test perplexity for the proposed Variational LSTM on PTB ([1512.05287_note.txt](1512.05287_note.txt)). It states that test perplexity is reduced from 78.4 to 73.4 with MC dropout and untied weights ([1512.05287_note.txt](1512.05287_note.txt)). The result is a single-model result for the large Variational LSTM with untied weights and MC dropout at test time ([1512.05287_note.txt](1512.05287_note.txt)). The paper does not report dynamic evaluation, cache/pointer, or fine-tuning for this result ([1512.05287_note.txt](1512.05287_note.txt)). An ensemble result of 68.7 with 10 Variational LSTMs is excluded because the query asks for single-model results ([1512.05287_note.txt](1512.05287_note.txt)). Therefore, 73.4 is the best eligible single-model result.

### Using the Output Embedding to Improve Language Models (Press & Wolf, 2017)

The paper reports 74.3 test perplexity for the large NNLM with weight tying ([1608.05859_note.txt](1608.05859_note.txt)). The small NNLM with weight tying and projection regularization reaches 100.9 ([1608.05859_note.txt](1608.05859_note.txt)). Both are single-model results without dynamic evaluation, cache/pointer, ensemble, or fine-tuning ([1608.05859_note.txt](1608.05859_note.txt)). The best eligible result is 74.3.

### Recurrent Neural Network Regularization (Zaremba et al., 2014)

The paper reports single-model PTB test perplexities of 82.7 for the medium regularized LSTM and 78.4 for the large regularized LSTM ([1409.2329_note.txt](1409.2329_note.txt)). The paper does not report dynamic evaluation, cache/pointer, or fine-tuning settings for PTB perplexity ([1409.2329_note.txt](1409.2329_note.txt)). The best eligible single-model result is 78.4. Model averaging results (e.g., 73.3 for 5 medium models, 69.5 for 10 large models) are excluded as ensembles ([1409.2329_note.txt](1409.2329_note.txt)).

### Character-Aware Neural Language Models (Kim et al., 2016)

The paper reports 78.9 test perplexity for LSTM-Char-Large and 92.3 for LSTM-Char-Small ([1508.06615_note.txt](1508.06615_note.txt)). These are single-model results, and the paper explicitly excludes ensembles because they are not comparable ([1508.06615_note.txt](1508.06615_note.txt)). No dynamic evaluation, cache/pointer, or fine-tuning PTB results appear ([1508.06615_note.txt](1508.06615_note.txt)). The best eligible result is 78.9.

### Gated Recurrent Neural Tensor Network (Zuo et al., 2017)

The paper reports 87.38 test perplexity for GRURNTN and 96.97 for LSTMRNTN ([1706.02222_note.txt](1706.02222_note.txt)). These are individual models, and the paper states that baseline and proposed model experiments did not use dynamic evaluation ([1706.02222_note.txt](1706.02222_note.txt)). No cache/pointer, ensemble, or fine-tuning setting is reported for the proposed word-level results ([1706.02222_note.txt](1706.02222_note.txt)). The best eligible result is 87.38.

## Comparative Observations

Among the eleven papers, the best single-model PTB test perplexity without dynamic evaluation or cache is 53.3, achieved by AWD-LSTM with fine-tuning ([1708.02182_note.txt](1708.02182_note.txt)). The second best is 54.44, achieved by AWD-LSTM-MoS with fine-tuning ([1711.03953_note.txt](1711.03953_note.txt)). If fine-tuning were excluded, the best eligible numbers would shift: AWD-LSTM without fine-tuning is 58.8 ([1708.02182_note.txt](1708.02182_note.txt)), and AWD-LSTM-MoS without fine-tuning is 55.97 ([1711.03953_note.txt](1711.03953_note.txt)). Under that stricter condition, AWD-LSTM-MoS without fine-tuning would still be 55.97, making it the best, followed by 58.3 from the 4-layer LSTM ([1707.05589_note.txt](1707.05589_note.txt)).

The results also show a clear trend: later papers tend to report lower perplexities, reflecting advances in regularization, weight tying, and architecture search. The 2014 regularized LSTM at 78.4 ([1409.2329_note.txt](1409.2329_note.txt)) is substantially improved upon by the 2016 Variational LSTM at 73.4 ([1512.05287_note.txt](1512.05287_note.txt)), the 2016 weight-tied NNLM at 74.3 ([1608.05859_note.txt](1608.05859_note.txt)), the 2017 Variational RHN at 65.4 ([1607.03474_note.txt](1607.03474_note.txt)), the 2017 NAS at 62.4 ([1611.01578_note.txt](1611.01578_note.txt)), and the 2018 4-layer LSTM at 58.3 ([1707.05589_note.txt](1707.05589_note.txt)). The 2017 AWD-LSTM and 2018 AWD-LSTM-MoS push the single-model boundary further to 53.3 and 54.44 respectively ([1708.02182_note.txt](1708.02182_note.txt); [1711.03953_note.txt](1711.03953_note.txt)).

It is important to note that dynamic evaluation and cache pointer methods, while excluded by the query, can produce even lower numbers. For example, AWD-LSTM with dynamic evaluation reaches 51.6/51.1 validation/test ([1711.03953.txt](1711.03953.txt)), and AWD-LSTM-MoS with dynamic evaluation reaches 47.69 test ([1711.03953_note.txt](1711.03953_note.txt)). AWD-LSTM with continuous cache pointer reaches 52.8 test ([1708.02182_note.txt](1708.02182_note.txt)). These are not included in the main table because they violate the query's exclusion criteria.

## Limitations

The extracted numbers rely on third-party research notes and paper excerpts provided in the source information. In some cases, the primary paper text was not fully available, and the best number had to be inferred from a comparison table in another paper, as with the Inan et al. (2016) result of 69.0 ([1707.05589_note.txt](1707.05589_note.txt)). Additionally, the treatment of fine-tuning varies across papers. The query does not exclude fine-tuning, so results with fine-tuning were eligible; however, readers interested in strictly no-fine-tuning comparisons should use the alternative numbers noted above. Finally, the provided information does not include every possible configuration for each paper, so the selected numbers represent the best eligible results as reported in the available sources.

## Conclusion

This report compiled the best single-model word-level Penn Treebank test perplexities for eleven provided papers, excluding dynamic evaluation and cache/pointer methods. The best eligible result is 53.3 from AWD-LSTM with fine-tuning, followed by 54.44 from AWD-LSTM-MoS with fine-tuning. Without fine-tuning, the best eligible result would be 55.97 from AWD-LSTM-MoS. The table and discussion above provide a comprehensive comparison of proposed models across a range of neural language modeling architectures.

## References

- 1409.2329_note.txt. (n.d.). Third-party research note: Recurrent Neural Network Regularization.
- 1508.06615_note.txt. (n.d.). Third-party research note: Character-Aware Neural Language Models.
- 1512.05287_note.txt. (n.d.). Third-party research note: A Theoretically Grounded Application of Dropout in Recurrent Neural Networks.
- 1607.03474.txt. (n.d.). 5.2.1 Penn Treebank.
- 1607.03474_note.txt. (n.d.). Third-party research note: Recurrent Highway Networks.
- 1608.05859_note.txt. (n.d.). Third-party research note: Using the Output Embedding to Improve Language Models.
- 1611.01462.txt. (n.d.). Tying Word Vectors and Word Classifiers: A Loss Framework for Language Modeling.
- 1611.01462_note.txt. (n.d.). Third-party research note: Tying Word Vectors and Word Classifiers: A Loss Framework for Language Modeling.
- 1611.01578_note.txt. (n.d.). Third-party research note: Neural Architecture Search with Reinforcement Learning.
- 1706.02222_note.txt. (n.d.). Third-party research note: Gated Recurrent Neural Tensor Network.
- 1707.05589_note.txt. (n.d.). Third-party research note: On the State of the Art of Evaluation in Neural Language Models.
- 1708.02182_note.txt. (n.d.). Third-party research note: Regularizing and Optimizing LSTM Language Models.
- 1711.03953.txt. (n.d.). Breaking the Softmax Bottleneck: A High-Rank RNN Language Model.
- 1711.03953_note.txt. (n.d.). Third-party research note: Breaking the Softmax Bottleneck: A High-Rank RNN Language Model.