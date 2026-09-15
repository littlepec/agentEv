# Word-Level Penn Treebank Test Perplexity of Proposed Single Models: A Structured Review

## Introduction

The Penn Treebank (PTB) word-level language modeling benchmark is widely used to evaluate neural language models. Perplexity is the standard metric, with lower values indicating better performance. This report extracts, for each provided paper, the best word-level PTB test perplexity that the paper reports for its own proposed model under single-model conditions. The query specifically excludes dynamic evaluation, cache/pointer mechanisms, ensembles, and fine-tuning. Because the papers use different model sizes, regularization strategies, and experimental protocols, the extracted numbers are not directly comparable as a unified leaderboard. They are, however, the reported figures under the stated constraints.

The provided source notes cover nine unique papers: 1409.2329, 1508.06615, 1512.05287, 1607.03474, 1608.05859, 1611.01462, 1611.01578, 1706.02222, and 1707.05589. For each, I identified the proposed model and selected the best single-model PTB test perplexity without dynamic evaluation or cache. Where a paper reports multiple configurations, I chose the lowest perplexity among its proposed single models. Ensemble and model-averaging results are excluded.

## Methodology

The analysis uses the provided source documents as the sole basis for the reported numbers. For each paper, I examined the relevant note or excerpt, identified the proposed model, and recorded the best single-model word-level PTB test perplexity. When a paper reports both tied and untied weights, or small and large models, I selected the better single-model result. When a paper reports ensemble or model-averaging results, those were excluded. When a paper reports dynamic evaluation or cache/pointer methods, those were also excluded. If the source note does not provide a full title, I use the source identifier and indicate that the title is not provided.

## Results

### Summary Table

| Paper Title (Source Identifier) | Best Single-Model Word-Level PTB Test Perplexity | Reported Setting |
|---|---:|---|
| On the State of the Art of Evaluation in Neural Language Models (1707.05589_note.txt) | 58.3 | 4-layer LSTM, 24M parameters ([1707.05589_note.txt](https://arxiv.org/abs/1707.05589)) |
| Neural Architecture Search with Reinforcement Learning (1611.01578_note.txt) | 62.4 | NAS with base 8 and shared embeddings, 54M parameters ([1611.01578_note.txt](https://arxiv.org/abs/1611.01578)) |
| Recurrent Highway Networks (1607.03474_note.txt) | 65.4 | Variational RHN + WT, 23M parameters, 10 layers, reduced weight decay ([1607.03474_note.txt](https://arxiv.org/abs/1607.03474)) |
| A Theoretically Grounded Application of Dropout in Recurrent Neural Networks (1512.05287_note.txt) | 73.4 | Large Variational LSTM, untied weights, MC dropout ([1512.05287_note.txt](https://arxiv.org/abs/1512.05287)) |
| Using the Output Embedding to Improve Language Models (1608.05859_note.txt) | 74.3 | Large NNLM with weight tying ([1608.05859_note.txt](https://arxiv.org/abs/1608.05859)) |
| Recurrent Neural Network Regularization (1409.2329_note.txt) | 78.4 | Large regularized LSTM, single model ([1409.2329_note.txt](https://arxiv.org/abs/1409.2329)) |
| Character-Aware Neural Language Models (1508.06615_note.txt) | 78.9 | LSTM-Char-Large, single model ([1508.06615_note.txt](https://arxiv.org/abs/1508.06615)) |
| Paper 1706.02222 (title not provided in source) | 87.38 | GRURNTN, best proposed word-level PTB test perplexity ([1706.02222_note.txt](https://arxiv.org/abs/1706.02222)) |
| Regularizing Neural Networks by Penalizing Confident Output Distributions (1611.01462_note.txt) | 140.6 | VD-LSTM+REAL, 200-unit model, PTB validation/test ([1611.01462_note.txt](https://arxiv.org/abs/1611.01462)) |

The 1611.01462 result is for a small 200-unit model and is therefore not directly comparable to the large models in the other rows. The source note lists four numbers per row; the first pair (validation/test) corresponds to the Penn Treebank, yielding 140.6 test perplexity for VD-LSTM+REAL ([1611.01462_note.txt](https://arxiv.org/abs/1611.01462)).

### Detailed Findings by Paper

#### On the State of the Art of Evaluation in Neural Language Models (1707.05589)

The paper reports a best word-level test perplexity of 58.3 on Penn Treebank for its own proposed model, a 4-layer LSTM with 24M parameters ([1707.05589_note.txt](https://arxiv.org/abs/1707.05589)). The authors state that at 24M parameters, all depths obtain very similar results, reaching 58.3 at depth 4. This result is reported for a single model, without dynamic evaluation, cache/pointer, ensemble, or fine-tuning. The paper explicitly refrains from including techniques that are known to push perplexities even lower, because its aim is strictly to do better model comparisons for the architectures under study ([1707.05589_note.txt](https://arxiv.org/abs/1707.05589)). This is the lowest single-model PTB test perplexity among the provided papers.

#### Neural Architecture Search with Reinforcement Learning (1611.01578)

The best listed baseline in the paper's Penn Treebank comparison table is Zilly et al. 2016 - Variational RHN, shared embeddings, with 66.0 test perplexity and 24M parameters ([1611.01578_note.txt](https://arxiv.org/abs/1611.01578)). The best Neural Architecture Search (NAS) result is 62.4 test perplexity, which is 3.6 perplexity better than that baseline ([1611.01578_note.txt](https://arxiv.org/abs/1611.01578)). The 62.4 result is NAS with base 8 and shared embeddings, 54M parameters ([1611.01578_note.txt](https://arxiv.org/abs/1611.01578)). The paper also reports 64.0 and 67.9 for other NAS configurations ([1611.01578_note.txt](https://arxiv.org/abs/1611.01578)). These are single-model results; no dynamic evaluation, cache/pointer, ensemble, or fine-tuning is reported for the NAS model on PTB ([1611.01578_note.txt](https://arxiv.org/abs/1611.01578)).

#### Recurrent Highway Networks (1607.03474)

The paper reports its best Penn Treebank word-level test perplexity for the proposed model as 65.4 for Variational RHN + WT ([1607.03474_note.txt](https://arxiv.org/abs/1607.03474)). It also reports 68.5 test perplexity for Variational RHN without WT ([1607.03474_note.txt](https://arxiv.org/abs/1607.03474)). The best 10-layer model with reduced weight decay improves to 67.9/65.4 validation/test perplexity ([1607.03474_note.txt](https://arxiv.org/abs/1607.03474)). Table 1 lists Variational RHN + WT as 23M parameters with validation/test perplexity 67.9/65.4 ([1607.03474_note.txt](https://arxiv.org/abs/1607.03474)). This setting uses variational dropout and weight tying of input and output mappings ([1607.03474_note.txt](https://arxiv.org/abs/1607.03474)). The best Penn Treebank result is a single model; dynamic evaluation, cache/pointer, ensemble, and fine-tuning are not reported for the proposed model ([1607.03474_note.txt](https://arxiv.org/abs/1607.03474)). The paper states that RHNs outperform most single models as well as all previous ensembles ([1607.03474_note.txt](https://arxiv.org/abs/1607.03474)).

#### A Theoretically Grounded Application of Dropout in Recurrent Neural Networks (1512.05287)

The paper reports 73.4 test perplexity for the proposed Variational LSTM on Penn Treebank ([1512.05287_note.txt](https://arxiv.org/abs/1512.05287)). The paper states test perplexity is reduced from 78.4 down to 73.4 with MC dropout and untied weights ([1512.05287_note.txt](https://arxiv.org/abs/1512.05287)). This 73.4 result is a single-model result for the large Variational LSTM with untied weights and MC dropout at test time ([1512.05287_note.txt](https://arxiv.org/abs/1512.05287)). The paper states that to the best of its knowledge these are currently the best single model perplexities on the Penn Treebank ([1512.05287_note.txt](https://arxiv.org/abs/1512.05287)). The paper text does not report dynamic evaluation, cache/pointer, or fine-tuning for the Penn Treebank result ([1512.05287_note.txt](https://arxiv.org/abs/1512.05287)). The paper also reports an ensemble result: using 10 Variational LSTMs with MC dropout improves Zaremba et al.'s test set perplexity from 69.5 to 68.7 ([1512.05287_note.txt](https://arxiv.org/abs/1512.05287)). That ensemble result is excluded from the table above because the query asks for single-model results.

#### Using the Output Embedding to Improve Language Models (1608.05859)

The paper reports word-level Penn Treebank test perplexity for its proposed weight-tied neural network language models in single-model settings ([1608.05859_note.txt](https://arxiv.org/abs/1608.05859)). The large NNLM with weight tying (Large + Weight Tying) reaches 74.3 test perplexity ([1608.05859_note.txt](https://arxiv.org/abs/1608.05859)). The small NNLM with weight tying and projection regularization (Small + WT + PR) reaches 100.9 test perplexity ([1608.05859_note.txt](https://arxiv.org/abs/1608.05859)). Both numbers come from the paper's neural network language model experiments and are reported without dynamic evaluation, cache/pointer, ensemble, or fine-tuning ([1608.05859_note.txt](https://arxiv.org/abs/1608.05859)). The best single-model result is therefore 74.3.

#### Recurrent Neural Network Regularization (1409.2329)

The paper reports model averaging of regularized LSTMs ([1409.2329_note.txt](https://arxiv.org/abs/1409.2329)). It lists 2 medium regularized LSTMs at 77.0, 5 medium regularized LSTMs at 73.3, 10 medium regularized LSTMs at 72.0, 2 large regularized LSTMs at 73.6, 10 large regularized LSTMs at 69.5, and 38 large regularized LSTMs at 68.7 ([1409.2329_note.txt](https://arxiv.org/abs/1409.2329)). These are ensemble/model-averaging results and are excluded. The paper lists single-model baseline Penn Treebank word-level test perplexities: Pascanu et al. 2013 at 107.5, Cheng et al. at 100.0, and a non-regularized LSTM at 114.5 ([1409.2329_note.txt](https://arxiv.org/abs/1409.2329)). The proposed medium regularized LSTM at 82.7 and large regularized LSTM at 78.4 are lower, meaning better, than all listed single-model baselines ([1409.2329_note.txt](https://arxiv.org/abs/1409.2329)). The best single-model result for the proposed model is therefore 78.4.

#### Character-Aware Neural Language Models (1508.06615)

The paper reports word-level Penn Treebank test perplexity for the proposed character-aware LSTM language model ([1508.06615_note.txt](https://arxiv.org/abs/1508.06615)). LSTM-Char-Large attains 78.9; LSTM-Char-Small attains 92.3 ([1508.06615_note.txt](https://arxiv.org/abs/1508.06615)). Predictions are made at the word level ([1508.06615_note.txt](https://arxiv.org/abs/1508.06615)). These are single-model results ([1508.06615_note.txt](https://arxiv.org/abs/1508.06615)). The paper excludes ensembles: "While lower perplexities have been reported with model ensembles [2012], we do not include them here as they are not comparable to the current work." ([1508.06615_note.txt](https://arxiv.org/abs/1508.06615)). No dynamic evaluation, cache/pointer, or fine-tuning Penn Treebank results appear ([1508.06615_note.txt](https://arxiv.org/abs/1508.06615)). The best single-model result is therefore 78.9.

#### Paper 1706.02222 (Title Not Provided)

Both proposed models outperform their baselines ([1706.02222_note.txt](https://arxiv.org/abs/1706.02222)). GRURNTN reduces perplexity from 97.78 to 87.38 over GRURNN, a 10.4 absolute and 10.63% relative reduction ([1706.02222_note.txt](https://arxiv.org/abs/1706.02222)). LSTMRNTN reduces perplexity from 108.26 to 96.97 over LSTMRNN, an 11.29 absolute and 10.42% relative reduction ([1706.02222_note.txt](https://arxiv.org/abs/1706.02222)). The paper states that GRURNTN outperforms all baseline models and the other listed models by a large margin ([1706.02222_note.txt](https://arxiv.org/abs/1706.02222)). LSTMRNTN improves the LSTMRNN model and its performance closely resembles the baseline GRURNN ([1706.02222_note.txt](https://arxiv.org/abs/1706.02222)). The GRURNTN result is the strongest proposed word-level Penn Treebank perplexity in the table ([1706.02222_note.txt](https://arxiv.org/abs/1706.02222)). The best single-model result is therefore 87.38.

#### Regularizing Neural Networks by Penalizing Confident Output Distributions (1611.01462)

The source note provides a table with VD-LSTM, VD-LSTM+AL, VD-LSTM+RE, and VD-LSTM+REAL ([1611.01462_note.txt](https://arxiv.org/abs/1611.01462)). For the 200-unit models, the numbers are: VD-LSTM 159.1/148.0, VD-LSTM+AL 153.0/142.5, VD-LSTM+RE 152.4/141.9, VD-LSTM+REAL 149.3/140.6 ([1611.01462_note.txt](https://arxiv.org/abs/1611.01462)). The caption identifies this as "Table 3: Comparison of our work to previous state of the art on word-level validation and test perplexities on the Penn Treebank corpus" ([1611.01462_note.txt](https://arxiv.org/abs/1611.01462)). The best proposed model is VD-LSTM+REAL with 140.6 test perplexity ([1611.01462_note.txt](https://arxiv.org/abs/1611.01462)). The note also contains a second set of numbers (150.5/138.4 for VD-LSTM+REAL) that likely corresponds to a different dataset, but the Penn Treebank pair is the first validation/test pair ([1611.01462_note.txt](https://arxiv.org/abs/1611.01462)). This is a single-model result without dynamic evaluation or cache, though it is for a small 200-unit model and is not directly comparable to the large models above.

## Discussion

The extracted results span a wide range of perplexities, from 58.3 to 140.6. This range reflects differences in model size, regularization, and evaluation scope. The lowest single-model PTB test perplexity among the provided papers is 58.3 from the 4-layer LSTM in 1707.05589, which was specifically designed for fair architecture comparison and excludes techniques that artificially lower perplexity ([1707.05589_note.txt](https://arxiv.org/abs/1707.05589)). The NAS model in 1611.01578 achieves 62.4, showing that architecture search can find competitive single models ([1611.01578_note.txt](https://arxiv.org/abs/1611.01578)). The Recurrent Highway Network in 1607.03474 achieves 65.4, which is notable for a single model and is reported to outperform many previous ensembles ([1607.03474_note.txt](https://arxiv.org/abs/1607.03474)). The Variational LSTM in 1512.05287 achieves 73.4, which was state-of-the-art for single models at its time ([1512.05287_note.txt](https://arxiv.org/abs/1512.05287)). The weight-tied NNLM in 1608.05859 achieves 74.3 ([1608.05859_note.txt](https://arxiv.org/abs/1608.05859)), while the regularized LSTM in 1409.2329 achieves 78.4 ([1409.2329_note.txt](https://arxiv.org/abs/1409.2329)), and the character-aware LSTM in 1508.06615 achieves 78.9 ([1508.06615_note.txt](https://arxiv.org/abs/1508.06615)). The GRURNTN paper in 1706.02222 reports 87.38, which is higher but still the best among its proposed models ([1706.02222_note.txt](https://arxiv.org/abs/1706.02222)). The 1611.01462 paper reports 140.6 for a small 200-unit model, which is expected given the small model size ([1611.01462_note.txt](https://arxiv.org/abs/1611.01462)).

It is important to note that some papers report ensemble or model-averaging results that are lower than their single-model results. For example, 1512.05287 reports an ensemble of 10 Variational LSTMs at 68.7 ([1512.05287_note.txt](https://arxiv.org/abs/1512.05287)), and 1409.2329 reports 38 large regularized LSTMs at 68.7 ([1409.2329_note.txt](https://arxiv.org/abs/1409.2329)). These are excluded per the query's single-model constraint. Similarly, dynamic evaluation and cache/pointer methods are not included for the proposed models in the provided notes.

## Conclusion

Based on the provided source notes, the best single-model word-level Penn Treebank test perplexity reported by each paper for its own proposed model, without dynamic evaluation or cache, is as follows: 58.3 for 1707.05589, 62.4 for 1611.01578, 65.4 for 1607.03474, 73.4 for 1512.05287, 74.3 for 1608.05859, 78.4 for 1409.2329, 78.9 for 1508.06615, 87.38 for 1706.02222, and 140.6 for 1611.01462. These figures are reported under varying model sizes and experimental conditions, so they should be interpreted as individual paper claims rather than a unified benchmark ranking.

## References

- 1409.2329_note.txt. (n.d.). Retrieved from https://arxiv.org/abs/1409.2329
- 1508.06615_note.txt. (n.d.). Retrieved from https://arxiv.org/abs/1508.06615
- 1512.05287_note.txt. (n.d.). Retrieved from https://arxiv.org/abs/1512.05287
- 1607.03474_note.txt. (n.d.). Retrieved from https://arxiv.org/abs/1607.03474
- 1608.05859_note.txt. (n.d.). Retrieved from https://arxiv.org/abs/1608.05859
- 1611.01462_note.txt. (n.d.). Retrieved from https://arxiv.org/abs/1611.01462
- 1611.01578_note.txt. (n.d.). Retrieved from https://arxiv.org/abs/1611.01578
- 1706.02222_note.txt. (n.d.). Retrieved from https://arxiv.org/abs/1706.02222
- 1707.05589_note.txt. (n.d.). Retrieved from https://arxiv.org/abs/1707.05589