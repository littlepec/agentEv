# Lowest Word-Level Penn Treebank Test Perplexity for Single Models Without Dynamic Evaluation or Cache/Pointer Augmentation: A Comparative Ranking

## Introduction

The Penn Treebank (PTB) word-level language modeling benchmark is a standard evaluation for neural language models. The query asks which provided paper reports the lowest PTB word-level test perplexity for a single model without dynamic evaluation, cache or pointer augmentation, and what that value is. It also asks to rank the papers by this number. This report addresses that query using only the provided research notes and paper excerpts. The scope is deliberately narrow: ensemble results are excluded because the query specifies a single model; dynamic evaluation is excluded by the query; cache and pointer augmentations are excluded by the query. Fine-tuning is not explicitly excluded by the query, so the primary ranking allows fine-tuning when a paper reports it. A sensitivity analysis then considers how the ranking changes if fine-tuning is also treated as an exclusion.

## Criteria and Method

A qualifying result must satisfy four conditions. First, it must be a word-level PTB test perplexity. Second, it must be for a single model, not an ensemble or model average. Third, it must not use dynamic evaluation. Fourth, it must not use cache or pointer augmentation. The query does not exclude fine-tuning, so the primary answer uses the best qualifying single-model result from each paper, including fine-tuned results when available. When a paper reports multiple qualifying configurations, the lowest qualifying number is selected for ranking. When a paper reports lower numbers that use excluded techniques, those numbers are identified but not used for the ranking.

Eleven unique papers are represented in the provided information. Each is identified by its arXiv identifier and, where available, its title from the provided notes. The papers are 1409.2329, 1508.06615, 1512.05287, 1607.03474, 1608.05859, 1611.01462, 1611.01578, 1706.02222, 1707.05589, 1708.02182, and 1711.03953. The following sections present the lowest qualifying result, the full ranking, the excluded lower results, and a sensitivity analysis for fine-tuning.

## The Lowest Qualifying Single-Model Result

The lowest qualifying PTB word-level test perplexity is **54.44**, reported by the paper **1711.03953**, titled *Breaking the Softmax Bottleneck: A High-Rank RNN Language Model* ([1711.03953_note.txt](https://arxiv.org/abs/1711.03953)). The proposed model, AWD-LSTM-MoS, reaches 54.44 test perplexity with fine-tuning. The same paper reports 55.97 test perplexity for AWD-LSTM-MoS without fine-tuning ([1711.03953_note.txt](https://arxiv.org/abs/1711.03953)). These are single-model results without dynamic evaluation. The paper also reports 47.69 test perplexity for AWD-LSTM-MoS with dynamic evaluation, but that result is excluded because of the dynamic evaluation constraint ([1711.03953_note.txt](https://arxiv.org/abs/1711.03953); [1711.03953.txt](https://arxiv.org/abs/1711.03953)). The table in the paper is explicitly captioned as single-model perplexity on validation and test sets on PTB, with a dagger indicating dynamic evaluation ([1711.03953.txt](https://arxiv.org/abs/1711.03953)). Therefore, under the query's constraints, the lowest value is 54.44. If one additionally excludes fine-tuning, the lowest qualifying value becomes 55.97, still from the same paper, because 55.97 is lower than the next-best no-fine-tuning single-model results of 58.3 from 1707.05589 and 58.8 from 1708.02182 ([1711.03953_note.txt](https://arxiv.org/abs/1711.03953); [1707.05589_note.txt](https://arxiv.org/abs/1707.05589); [1708.02182_note.txt](https://arxiv.org/abs/1708.02182)). This makes 1711.03953 the lowest-ranked paper whether or not fine-tuning is allowed.

The second-lowest qualifying result is **57.3** from **1708.02182**, *Regularizing and Optimizing LSTM Language Models*, for AWD-LSTM, a 3-layer LSTM with tied weights. This is a single-model result without cache or pointer augmentation, and it includes the fine-tuning step ([1708.02182_note.txt](https://arxiv.org/abs/1708.02182)). The same paper reports 58.8 test perplexity for the no-fine-tuning ablation, and it states that removal of the fine-tuning step degrades performance ([1708.02182_note.txt](https://arxiv.org/abs/1708.02182)). It also reports 52.8 test perplexity with a continuous cache pointer, but that result is excluded because of the cache/pointer constraint ([1708.02182_note.txt](https://arxiv.org/abs/1708.02182)).

The third-lowest qualifying result is **58.3** from **1707.05589**, *On the State of the Art of Evaluation in Neural Language Models*. The paper reports a best word-level test perplexity of 58.3 on PTB for its own proposed model, a 4-layer LSTM with 24M parameters. The authors state that at 24M, all depths obtain very similar results, reaching 58.3 at depth 4. This is a single model without dynamic evaluation, cache/pointer, ensemble, or fine-tuning ([1707.05589_note.txt](https://arxiv.org/abs/1707.05589)). The paper explicitly refrains from including techniques that are known to push perplexities even lower because its aim is strictly to do better model comparisons for the architectures under study ([1707.05589_note.txt](https://arxiv.org/abs/1707.05589)).

## Full Ranking of Qualifying Single-Model Results

### Primary Ranking Table

Table 1 ranks the eleven papers by their best qualifying PTB word-level test perplexity under the primary criteria: single model, no dynamic evaluation, no cache/pointer augmentation, and no ensemble. Fine-tuning is allowed in this primary ranking. Lower values are better.

| Rank | Source ID | Model / Configuration | PTB word-level test PPL | Fine-tuning | Dynamic eval | Cache/pointer | Ensemble | Notes |
|---:|---|---|---:|---|---|---|---|---|
| 1 | 1711.03953 | AWD-LSTM-MoS | 54.44 | Yes | No | No | No | Best qualifying; 55.97 without finetune; 47.69 with dynamic eval excluded ([1711.03953_note.txt](https://arxiv.org/abs/1711.03953)) |
| 2 | 1708.02182 | AWD-LSTM (3-layer LSTM, tied weights) | 57.3 | Yes | No | No | No | 58.8 without finetune; 52.8 with continuous cache pointer excluded ([1708.02182_note.txt](https://arxiv.org/abs/1708.02182)) |
| 3 | 1707.05589 | 4-layer LSTM, 24M params | 58.3 | No | No | No | No | No dynamic eval, cache/pointer, ensemble, or fine-tuning ([1707.05589_note.txt](https://arxiv.org/abs/1707.05589)) |
| 4 | 1611.01578 | Neural Architecture Search, base 8 + shared embeddings, 54M | 62.4 | No | No | No | No | Other NAS configurations: 64.0 and 67.9 ([1611.01578_note.txt](https://arxiv.org/abs/1611.01578)) |
| 5 | 1607.03474 | Variational RHN + WT, 23M | 65.4 | No | No | No | No | Validation/test 67.9/65.4; Variational RHN without WT 68.5 ([1607.03474_note.txt](https://arxiv.org/abs/1607.03474)) |
| 6 | 1611.01462 | VD-RHN+RE | 66.0 | Not reported | No | No | No | Validation/test 68.1/66.0; described as best overall ([1611.01462_note.txt](https://arxiv.org/abs/1611.01462)) |
| 7 | 1512.05287 | Variational LSTM, large untied, MC dropout | 73.4 | No | No | No | No | Ensemble of 10 Variational LSTMs at 68.7 excluded ([1512.05287_note.txt](https://arxiv.org/abs/1512.05287)) |
| 8 | 1608.05859 | Large NNLM + weight tying | 74.3 | No | No | No | No | Small NNLM + WT + PR at 100.9 ([1608.05859_note.txt](https://arxiv.org/abs/1608.05859)) |
| 9 | 1409.2329 | Large regularized LSTM | 78.4 | No | No | No | No | Medium regularized LSTM 82.7; model averaging results lower but excluded ([1409.2329_note.txt](https://arxiv.org/abs/1409.2329)) |
| 10 | 1508.06615 | LSTM-Char-Large | 78.9 | No | No | No | No | LSTM-Char-Small 92.3; ensembles excluded ([1508.06615_note.txt](https://arxiv.org/abs/1508.06615)) |
| 11 | 1706.02222 | GRURNTN | 87.38 | No | No | No | No | LSTMRNTN 96.97; GRURNTN is strongest proposed ([1706.02222_note.txt](https://arxiv.org/abs/1706.02222)) |

### Ranking Interpretation

The ranking shows a clear separation between the top three papers and the rest. The top three are all below 59 test perplexity, while the fourth-ranked NAS model is at 62.4, and the remaining papers range from 65.4 to 87.38. The top two use AWD-LSTM variants, with the AWD-LSTM-MoS model achieving the lowest qualifying number. The third-ranked model is a 4-layer LSTM from a study focused on fair evaluation without additional techniques. The fifth-ranked Variational RHN + WT at 65.4 is notable because it is lower than several later papers, and the sixth-ranked VD-RHN+RE at 66.0 is close behind. The older regularized LSTM results from 1409.2329 and the character-aware LSTM from 1508.06615 are in the 78–79 range, and the GRURNTN result from 1706.02222 is the highest in this ranking at 87.38.

## Excluded Lower Results

Several reported perplexities are lower than 54.44 but are excluded by the query's constraints. These exclusions are important for interpreting the ranking correctly.

### Dynamic Evaluation

Dynamic evaluation produces the lowest overall numbers. The 1711.03953 paper reports 47.69 test perplexity for AWD-LSTM-MoS with dynamic evaluation ([1711.03953_note.txt](https://arxiv.org/abs/1711.03953)). The same paper's table also lists Krause et al. 2017 AWD-LSTM + dynamic evaluation at 51.1 test perplexity ([1711.03953.txt](https://arxiv.org/abs/1711.03953)). These are lower than 54.44 but use dynamic evaluation, so they do not qualify.

### Cache or Pointer Augmentation

Cache or pointer augmentation produces lower numbers. The 1708.02182 paper reports 52.8 test perplexity for AWD-LSTM with a continuous cache pointer ([1708.02182_note.txt](https://arxiv.org/abs/1708.02182)). The 1711.03953 table also lists Merity et al. 2017 AWD-LSTM + continuous cache pointer at 52.8 test perplexity ([1711.03953.txt](https://arxiv.org/abs/1711.03953)). These are lower than 54.44 but use cache/pointer augmentation, so they do not qualify.

### Ensembles and Model Averaging

Ensemble or model-averaging results produce lower numbers. The 1409.2329 paper reports 2 medium regularized LSTMs at 77.0, 5 medium regularized LSTMs at 73.3, 10 medium regularized LSTMs at 72.0, 2 large regularized LSTMs at 73.6, 10 large regularized LSTMs at 69.5, and 38 large regularized LSTMs at 68.7 ([1409.2329_note.txt](https://arxiv.org/abs/1409.2329)). The 1512.05287 paper reports that 10 Variational LSTMs with MC dropout improve Zaremba et al.'s test perplexity from 69.5 to 68.7 ([1512.05287_note.txt](https://arxiv.org/abs/1512.05287)). The 1611.01462 paper lists 38 Large LSTMs at 68.7 and 10 Large VD-LSTMs at 68.7 among baselines ([1611.01462_note.txt](https://arxiv.org/abs/1611.01462)). All of these are ensembles and are therefore excluded.

### Baselines with Excluded Techniques

Some baselines with cache/pointer are lower than some qualifying results. The 1611.01462 paper lists RNN+LDA+KN-5+Cache at 92.0 and Pointer Sentinel-LSTM(medium) at 70.9 ([1611.01462_note.txt](https://arxiv.org/abs/1611.01462)). These are not lower than 54.44, but they illustrate the excluded cache/pointer category. The 1611.01578 paper lists a best baseline of Zilly et al. 2016 Variational RHN with shared embeddings at 66.0 test perplexity ([1611.01578_note.txt](https://arxiv.org/abs/1611.01578)). That baseline is a single model without dynamic evaluation or cache/pointer, but it is a baseline rather than the paper's proposed model. Even if baselines are considered, it does not beat 54.44.

## Sensitivity Analysis: What If Fine-Tuning Is Excluded?

### Fine-Tuning-Excluded Ranking

The query does not exclude fine-tuning, so the primary answer is 54.44 from 1711.03953. However, because some may treat fine-tuning as an additional augmentation, it is useful to consider the ranking if fine-tuning is also excluded. Under that stricter criterion, the lowest qualifying result becomes **55.97** from 1711.03953, the AWD-LSTM-MoS without fine-tuning ([1711.03953_note.txt](https://arxiv.org/abs/1711.03953)). The next-best no-fine-tuning results are 58.3 from 1707.05589 and 58.8 from 1708.02182 ([1707.05589_note.txt](https://arxiv.org/abs/1707.05589); [1708.02182_note.txt](https://arxiv.org/abs/1708.02182)). The rest of the ranking remains the same as in Table 1, except that 1708.02182 moves from 57.3 to its no-fine-tuning value of 58.8, which places it below 1707.05589's 58.3. Thus, even under the stricter interpretation, 1711.03953 remains the paper with the lowest qualifying PTB word-level test perplexity. This robustness strengthens the conclusion that 1711.03953 is the correct answer to the query.

## Discussion

The ranking reflects several patterns in the provided data. The lowest qualifying results come from models that combine strong regularization, weight tying, and, in the top case, a mixture-of-softmaxes approach. The AWD-LSTM-MoS model at 54.44 and the AWD-LSTM model at 57.3 outperform the 4-layer LSTM at 58.3, the NAS model at 62.4, and the Variational RHN + WT at 65.4. The older regularized LSTM and character-aware LSTM results are considerably higher, at 78.4 and 78.9, respectively. The GRURNTN result at 87.38 is the highest in the qualifying ranking, although it still improves substantially over its GRURNN baseline of 97.78 and its LSTMRNN baseline of 108.26 ([1706.02222_note.txt](https://arxiv.org/abs/1706.02222)).

It is also important to note that the lowest numbers in the broader literature represented here—47.69 with dynamic evaluation, 52.8 with continuous cache pointer—are excluded by the query. If the query had allowed cache/pointer augmentation, the answer would be 52.8 from 1708.02182 or 1711.03953's table. If it had allowed dynamic evaluation, the answer would be 47.69 from 1711.03953. But under the stated constraints, those techniques are disallowed, and the lowest qualifying single-model result is 54.44.

The ranking also shows that the difference between the top two papers is 2.86 perplexity (57.3 − 54.44), and the difference between the top result and the third-ranked result is 3.86 perplexity (58.3 − 54.44). The top result is 3.6 perplexity better than the best baseline in the 1611.01578 comparison, which was 66.0 for Zilly et al. 2016 Variational RHN with shared embeddings ([1611.01578_note.txt](https://arxiv.org/abs/1611.01578)). The top result is also 10.96 perplexity better than the fifth-ranked Variational RHN + WT at 65.4 ([1607.03474_note.txt](https://arxiv.org/abs/1607.03474)). These comparisons underscore the strength of the AWD-LSTM-MoS result under the query's constraints.

## Conclusion

The paper that reports the lowest word-level test perplexity on the Penn Treebank for a single model without dynamic evaluation, cache or pointer augmentation is **1711.03953**, *Breaking the Softmax Bottleneck: A High-Rank RNN Language Model*. Its best qualifying value is **54.44** test perplexity for AWD-LSTM-MoS with fine-tuning ([1711.03953_note.txt](https://arxiv.org/abs/1711.03953)). If fine-tuning is also excluded, the same paper's no-fine-tuning value of **55.97** remains the lowest qualifying result ([1711.03953_note.txt](https://arxiv.org/abs/1711.03953)). The full ranking places 1708.02182 second at 57.3, 1707.05589 third at 58.3, 1611.01578 fourth at 62.4, 1607.03474 fifth at 65.4, 1611.01462 sixth at 66.0, 1512.05287 seventh at 73.4, 1608.05859 eighth at 74.3, 1409.2329 ninth at 78.4, 1508.06615 tenth at 78.9, and 1706.02222 eleventh at 87.38. Lower numbers exist in the provided information—47.69 with dynamic evaluation and 52.8 with cache/pointer—but they are excluded by the query's explicit constraints. Therefore, 1711.03953 is the correct answer, and 54.44 is the value under the primary criteria.

## References

1409.2329_note.txt. (n.d.). *Recurrent Neural Network Regularization*. https://arxiv.org/abs/1409.2329

1508.06615_note.txt. (n.d.). *Character-Aware Neural Language Models*. https://arxiv.org/abs/1508.06615

1512.05287_note.txt. (n.d.). *Variational LSTM*. https://arxiv.org/abs/1512.05287

1607.03474_note.txt. (n.d.). *Recurrent Highway Networks*. https://arxiv.org/abs/1607.03474

1608.05859_note.txt. (n.d.). *Using the Output Embedding to Improve Language Models*. https://arxiv.org/abs/1608.05859

1611.01462_note.txt. (n.d.). *Tying Word Vectors and Word Classifiers: A Loss Framework for Language Modeling*. https://arxiv.org/abs/1611.01462

1611.01578_note.txt. (n.d.). *Neural Architecture Search with Reinforcement Learning*. https://arxiv.org/abs/1611.01578

1706.02222_note.txt. (n.d.). *GRURNTN and LSTMRNTN*. https://arxiv.org/abs/1706.02222

1707.05589_note.txt. (n.d.). *On the State of the Art of Evaluation in Neural Language Models*. https://arxiv.org/abs/1707.05589

1708.02182_note.txt. (n.d.). *Regularizing and Optimizing LSTM Language Models*. https://arxiv.org/abs/1708.02182

1711.03953_note.txt. (n.d.). *Breaking the Softmax Bottleneck: A High-Rank RNN Language Model*. https://arxiv.org/abs/1711.03953