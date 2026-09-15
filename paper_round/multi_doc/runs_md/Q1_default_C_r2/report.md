# Lowest Eligible Single-Model Penn Treebank Word-Level Test Perplexity: Ranking Across the Provided Papers

## Introduction and Scope

This report addresses the query: across the provided papers, which reports the lowest word-level test perplexity on the Penn Treebank (PTB) for a single model without dynamic evaluation, cache or pointer augmentation, and what is that value? It also ranks the papers by that number. The Penn Treebank word-level language modeling task is a standard benchmark in neural language modeling, and the provided sources report multiple single-model, ensemble, cache/pointer, and baseline results. To answer the query rigorously, I apply the following inclusion criteria: the result must be a word-level PTB test perplexity; it must come from a single model rather than an ensemble or model-averaging setup; it must not rely on dynamic evaluation, cache augmentation, or pointer augmentation; and it must not be a baseline reported only for context. Where a paper reports several eligible single-model results, I use the paper’s best eligible number for ranking. All figures and claims are drawn only from the provided source notes and paper excerpts.

## Direct Answer

The paper that reports the lowest eligible single-model PTB word-level test perplexity is the one represented by source 1707.05589, with a value of **58.3 test perplexity** ([1707.05589_note.txt](https://arxiv.org/abs/1707.05589)). That result is for a 4-layer LSTM with 24M parameters. The note states that at 24M parameters, all depths obtain very similar results, reaching 58.3 at depth 4. Importantly, the result is reported for a single model, without dynamic evaluation, cache/pointer, ensemble, or fine-tuning. The paper explicitly refrains from including techniques that are known to push perplexities even lower, because its aim is strictly to do better model comparisons for the architectures under study ([1707.05589_note.txt](https://arxiv.org/abs/1707.05589)). This makes 58.3 the lowest and cleanest eligible result in the provided set.

## Ranking of Papers by Eligible Single-Model PTB Test Perplexity

The table below ranks the papers by their best eligible single-model word-level PTB test perplexity. Lower perplexity is better. The ranking excludes ensembles, model averaging, cache/pointer methods, and baseline-only entries unless otherwise noted.

| Rank | Paper / Source | Model | PTB word-level test PPL | Parameters | Eligibility notes |
|---|---|---|---|---|---|
| 1 | [1707.05589_note.txt](https://arxiv.org/abs/1707.05589) | 4-layer LSTM | 58.3 | 24M | Single model; no dynamic evaluation, cache/pointer, ensemble, or fine-tuning ([1707.05589_note.txt](https://arxiv.org/abs/1707.05589)) |
| 2 | [1611.01578_note.txt](https://arxiv.org/abs/1611.01578) | Neural Architecture Search, base 8 + shared embeddings | 62.4 | 54M | Single model; no dynamic evaluation, cache/pointer, ensemble, or fine-tuning reported ([1611.01578_note.txt](https://arxiv.org/abs/1611.01578)) |
| 3 | [1607.03474_note.txt](https://arxiv.org/abs/1607.03474) | Variational RHN + WT | 65.4 | 23M | Single model; no dynamic evaluation, cache/pointer, ensemble, or fine-tuning reported for the proposed model ([1607.03474_note.txt](https://arxiv.org/abs/1607.03474)) |
| 4 | [1611.01462_note.txt](https://arxiv.org/abs/1611.01462) | VD-RHN+RE | 66.0 | — | Described as best overall; cache/pointer/ensemble entries appear as baselines, not as the reported result ([1611.01462_note.txt](https://arxiv.org/abs/1611.01462)) |
| 5 | [1512.05287_note.txt](https://arxiv.org/abs/1512.05287) | Large Variational LSTM, untied weights, MC dropout | 73.4 | 66M | Single-model result; ensemble result of 68.7 is excluded ([1512.05287_note.txt](https://arxiv.org/abs/1512.05287)) |
| 6 | [1608.05859_note.txt](https://arxiv.org/abs/1608.05859) | Large NNLM + Weight Tying | 74.3 | — | Single-model setting; no dynamic evaluation, cache/pointer, ensemble, or fine-tuning ([1608.05859_note.txt](https://arxiv.org/abs/1608.05859)) |
| 7 | [1409.2329_note.txt](https://arxiv.org/abs/1409.2329) | Large regularized LSTM | 78.4 | — | Single-model result; model averaging results excluded ([1409.2329_note.txt](https://arxiv.org/abs/1409.2329)) |
| 8 | [1508.06615_note.txt](https://arxiv.org/abs/1508.06615) | LSTM-Char-Large | 78.9 | — | Single-model result; ensembles explicitly excluded ([1508.06615_note.txt](https://arxiv.org/abs/1508.06615)) |
| 9 | [1706.02222_note.txt](https://arxiv.org/abs/1706.02222) | GRURNTN | 87.38 | — | Best proposed result; no dynamic/cache/pointer/ensemble/fine-tuning noted ([1706.02222_note.txt](https://arxiv.org/abs/1706.02222)) |

A separate source, 1711.03953, evaluates the proposed MoS model on Penn Treebank and WikiText-2 based on perplexity, but the provided note does not supply a PTB perplexity figure, so that paper cannot be ranked on this metric ([1711.03953.txt](https://arxiv.org/abs/1711.03953)).

## Detailed Analysis of Ranked Results

### Rank 1: 1707.05589 — 58.3

The top-ranked result is the 58.3 word-level test perplexity reported for a 4-layer LSTM with 24M parameters. The note states that at 24M, all depths obtain very similar results, reaching 58.3 at depth 4. This is a single-model result and is reported without dynamic evaluation, cache/pointer, ensemble, or fine-tuning. The paper’s stated aim is to do better model comparisons, and it explicitly refrains from including techniques known to push perplexities even lower ([1707.05589_note.txt](https://arxiv.org/abs/1707.05589)). This makes the 58.3 figure particularly valuable for the query: it is not only the lowest number in the provided set, but also one of the most methodologically controlled and directly comparable results. The margin over the next best eligible result is 3.4 perplexity points, which is substantial in the PTB word-level setting.

### Rank 2: 1611.01578 — 62.4

The second-ranked result is 62.4 test perplexity from Neural Architecture Search with base 8 and shared embeddings, using 54M parameters. The same source reports 64.0 and 67.9 for other Neural Architecture Search configurations. The note states that these are single-model perplexity numbers on the PTB test set, and that the paper does not report dynamic evaluation, cache/pointer, ensemble, or fine-tuning for the Neural Architecture Search model. Cache/pointer appears only among baseline labels such as Pointer Sentinel-LSTM ([1611.01578_note.txt](https://arxiv.org/abs/1611.01578)). This result is eligible because it is a single model without the excluded augmentation techniques, and it is the second-lowest value among the provided papers.

### Rank 3: 1607.03474 — 65.4

The third-ranked result is 65.4 test perplexity for Variational RHN + WT. The note reports that the paper’s best PTB word-level test perplexity for the proposed model is 65.4 for Variational RHN + WT, and that Variational RHN without WT achieves 68.5. The best 10-layer model with reduced weight decay improves to 67.9/65.4 validation/test perplexity. Table 1 lists Variational RHN + WT as 23M parameters with validation/test perplexity 67.9/65.4. This setting uses variational dropout and weight tying of input and output mappings. The note explicitly states that the best PTB result is a single model, and that dynamic evaluation, cache/pointer, ensemble, and fine-tuning are not reported for the proposed model. Cache and pointer methods appear only as baselines, and ensembles are mentioned only in comparison ([1607.03474_note.txt](https://arxiv.org/abs/1607.03474)). The paper also states that RHNs outperform most single models as well as all previous ensembles ([1607.03474_note.txt](https://arxiv.org/abs/1607.03474)). The original paper text confirms that for the best 10-layer model, reducing weight decay further improves the results to 67.9/65.4 validation/test perplexity ([1607.03474.txt](https://arxiv.org/abs/1607.03474)).

### Rank 4: 1611.01462 — 66.0

The fourth-ranked result is 66.0 test perplexity for VD-RHN+RE (Zilly et al. 2016), trained with reused embeddings following the paper’s work. The note states that this achieves validation perplexity 68.1 and test perplexity 66.0 on Penn Treebank, and the paper describes it as best overall. The same note lists cache, pointer, and ensemble baselines separately: RNN+LDA+KN-5+Cache with 92.0 test perplexity, Pointer Sentinel-LSTM(medium) with 70.9, 38 Large LSTMs with 68.7, and 10 Large VD-LSTMs with 68.7 ([1611.01462_note.txt](https://arxiv.org/abs/1611.01462)). The provided note does not explicitly state that the 66.0 result is free of dynamic evaluation, but it is presented as the best overall result and the cache/pointer/ensemble entries are baselines rather than the proposed result. Under the provided framing, 66.0 is eligible, with this caveat noted.

### Rank 5: 1512.05287 — 73.4

The fifth-ranked result is 73.4 test perplexity for the large Variational LSTM with untied weights and MC dropout at test time. The note states that test perplexity is reduced from 78.4 down to 73.4 with MC dropout and untied weights, and that this is a single-model result. The paper states that to the best of its knowledge these are currently the best single-model perplexities on the Penn Treebank. The note also states that the paper text does not report dynamic evaluation, cache/pointer, or fine-tuning for the PTB result, and the Table 1 caption identifies the results as single-model perplexity on test and validation sets ([1512.05287_note.txt](https://arxiv.org/abs/1512.05287)). The same paper reports an ensemble result: using 10 Variational LSTMs with MC dropout improves Zaremba et al.’s test set perplexity from 69.5 to 68.7, obtaining identical perplexity to Zaremba et al.’s experiment with 38 models ([1512.05287_note.txt](https://arxiv.org/abs/1512.05287)). Because the query requires a single model, the 68.7 ensemble result is excluded.

### Rank 6: 1608.05859 — 74.3

The sixth-ranked result is 74.3 test perplexity for the large NNLM with weight tying. The small NNLM with weight tying and projection regularization reaches 100.9 test perplexity. The note states that both numbers come from the paper’s neural network language model experiments and are reported without dynamic evaluation, cache/pointer, ensemble, or fine-tuning ([1608.05859_note.txt](https://arxiv.org/abs/1608.05859)). The paper’s comparison baselines include the large NNLM of Zaremba et al. (2014) at 78.4 test perplexity and the small NNLM at 114.5. The paper also lists non-dropout baselines: KN 5-gram 141, RNN 123, LSTM 117, Stack RNN 110, FOFE-FNN 108, Noisy LSTM 108.0, and Deep RNN 107.5 ([1608.05859_note.txt](https://arxiv.org/abs/1608.05859)). These baselines are higher than the proposed 74.3 and do not affect the ranking of the paper’s best eligible result.

### Rank 7: 1409.2329 — 78.4

The seventh-ranked result is 78.4 test perplexity for the large regularized LSTM. The note reports that the medium regularized LSTM reaches 82.7, and the large regularized LSTM reaches 78.4, both lower than all listed single-model baselines. Those baselines are Pascanu et al. 2013 at 107.5, Cheng et al. at 100.0, and a non-regularized LSTM at 114.5 ([1409.2329_note.txt](https://arxiv.org/abs/1409.2329)). The paper also reports model averaging results: 2 medium regularized LSTMs at 77.0, 5 medium at 73.3, 10 medium at 72.0, 2 large at 73.6, 10 large at 69.5, and 38 large at 68.7. These are ensembles or model-averaging results and are therefore excluded from the ranking. The note states that the paper does not report dynamic evaluation, cache/pointer, or fine-tuning settings for PTB perplexity ([1409.2329_note.txt](https://arxiv.org/abs/1409.2329)). Thus, 78.4 is the paper’s best eligible single-model result.

### Rank 8: 1508.06615 — 78.9

The eighth-ranked result is 78.9 test perplexity for LSTM-Char-Large, with LSTM-Char-Small at 92.3. Predictions are made at the word level, and the note states these are single-model results. The paper explicitly excludes ensembles: “While lower perplexities have been reported with model ensembles [2012], we do not include them here as they are not comparable to the current work.” No dynamic evaluation, cache/pointer, or fine-tuning PTB results appear ([1508.06615_note.txt](https://arxiv.org/abs/1508.06615)). Because the paper’s best eligible result is 78.9, it ranks just below the 78.4 large regularized LSTM from 1409.2329.

### Rank 9: 1706.02222 — 87.38

The ninth-ranked result is 87.38 test perplexity for GRURNTN. The note states that GRURNTN reduces perplexity from 97.78 to 87.38 over GRURNN, a 10.4 absolute and 10.63% relative reduction. LSTMRNTN reduces perplexity from 108.26 to 96.97 over LSTMRNN, an 11.29 absolute and 10.42% relative reduction. The paper states that GRURNTN outperforms all baseline models and the other listed models by a large margin, and that LSTMRNTN improves the LSTMRNN model while closely resembling the baseline GRURNN. The GRURNTN result is the strongest proposed word-level PTB perplexity in the table ([1706.02222_note.txt](https://arxiv.org/abs/1706.02222)). The note does not mention dynamic evaluation, cache/pointer, ensemble, or fine-tuning, so the result is treated as eligible, though with the caveat that the note does not explicitly state their absence.

### Unranked: 1711.03953

The source 1711.03953 describes experiments on Penn Treebank and WikiText-2 based on perplexity, following regularization and optimization techniques from Merity et al. 2017. However, the provided note does not include a PTB perplexity figure for the MoS model ([1711.03953.txt](https://arxiv.org/abs/1711.03953)). Because no numeric PTB test perplexity is available in the provided information, this paper cannot be placed in the ranking.

## Excluded Results and Why

Several lower numbers appear in the provided sources but are excluded because they do not meet the query’s eligibility criteria. The table below summarizes the most important exclusions.

| Excluded result | Value | Reason for exclusion | Source |
|---|---|---|---|
| 38 large regularized LSTMs | 68.7 | Ensemble/model averaging | [1409.2329_note.txt](https://arxiv.org/abs/1409.2329) |
| 10 large regularized LSTMs | 69.5 | Ensemble/model averaging | [1409.2329_note.txt](https://arxiv.org/abs/1409.2329) |
| 10 Variational LSTMs with MC dropout | 68.7 | Ensemble | [1512.05287_note.txt](https://arxiv.org/abs/1512.05287) |
| 38 Large LSTMs | 68.7 | Ensemble baseline | [1611.01462_note.txt](https://arxiv.org/abs/1611.01462) |
| 10 Large VD-LSTMs | 68.7 | Ensemble baseline | [1611.01462_note.txt](https://arxiv.org/abs/1611.01462) |
| Pointer Sentinel-LSTM(medium) | 70.9 | Pointer/cache baseline | [1611.01462_note.txt](https://arxiv.org/abs/1611.01462) |
| RNN+LDA+KN-5+Cache | 92.0 | Cache baseline | [1611.01462_note.txt](https://arxiv.org/abs/1611.01462) |
| Variational RHN without WT | 68.5 | Single model but higher than the paper’s 65.4 | [1607.03474_note.txt](https://arxiv.org/abs/1607.03474) |
| Small + WT + PR | 100.9 | Single model but higher than the paper’s 74.3 | [1608.05859_note.txt](https://arxiv.org/abs/1608.05859) |
| LSTM-Char-Small | 92.3 | Single model but higher than the paper’s 78.9 | [1508.06615_note.txt](https://arxiv.org/abs/1508.06615) |
| LSTMRNTN | 96.97 | Single model but higher than the paper’s 87.38 | [1706.02222_note.txt](https://arxiv.org/abs/1706.02222) |
| Non-dropout baselines | 107.5–141 | Baseline-only entries, not proposed models | [1608.05859_note.txt](https://arxiv.org/abs/1608.05859) |

The exclusion of ensembles is important because some ensemble results are lower than several single-model results. For example, the 38 large regularized LSTMs at 68.7 and the 10 Variational LSTMs at 68.7 are both lower than the eligible single-model 73.4 from 1512.05287, but they do not qualify as single models. Similarly, the 10 large regularized LSTMs at 69.5 and the 2 large regularized LSTMs at 73.6 are model-averaging results and are therefore excluded ([1409.2329_note.txt](https://arxiv.org/abs/1409.2329)). Cache and pointer methods are also excluded: the Pointer Sentinel-LSTM(medium) at 70.9 and RNN+LDA+KN-5+Cache at 92.0 are explicitly cache/pointer baselines ([1611.01462_note.txt](https://arxiv.org/abs/1611.01462)). Dynamic evaluation is not reported in any of the provided PTB results, so it did not directly remove any candidate numbers, but it remains part of the query’s exclusion criteria.

## Methodological Caveats and Reliability

Several caveats should be considered when interpreting this ranking. First, many of the provided documents are third-party research notes rather than full original papers. The notes are consistent and detailed, but they are secondary sources. Where original paper excerpts are available, such as 1607.03474.txt, 1512.05287.txt, and 1611.01462.txt, they corroborate the note figures ([1607.03474.txt](https://arxiv.org/abs/1607.03474); [1512.05287.txt](https://arxiv.org/abs/1512.05287); [1611.01462.txt](https://arxiv.org/abs/1611.01462)). Second, not all papers explicitly state that their PTB results avoid dynamic evaluation, cache/pointer, ensemble, and fine-tuning. The 1707.05589, 1611.01578, 1607.03474, 1512.05287, 1608.05859, 1409.2329, and 1508.06615 sources provide clear or near-clear eligibility statements ([1707.05589_note.txt](https://arxiv.org/abs/1707.05589); [1611.01578_note.txt](https://arxiv.org/abs/1611.01578); [1607.03474_note.txt](https://arxiv.org/abs/1607.03474); [1512.05287_note.txt](https://arxiv.org/abs/1512.05287); [1608.05859_note.txt](https://arxiv.org/abs/1608.05859); [1409.2329_note.txt](https://arxiv.org/abs/1409.2329); [1508.06615_note.txt](https://arxiv.org/abs/1508.06615)). The 1611.01462 and 1706.02222 sources are less explicit about dynamic evaluation, so their inclusion is based on the provided framing and the absence of indicated cache/pointer/ensemble augmentation in the reported result ([1611.01462_note.txt](https://arxiv.org/abs/1611.01462); [1706.02222_note.txt](https://arxiv.org/abs/1706.02222)). Third, parameter counts differ widely across models, from 23M to 66M and 54M, so the ranking should be read as a comparison of reported test perplexity under the stated constraints, not as a controlled parameter-matched comparison. Fourth, the 58.3 result comes from a newer and explicitly evaluation-focused paper, which strengthens its reliability for this query ([1707.05589_note.txt](https://arxiv.org/abs/1707.05589)).

## Conclusion

Across the provided papers, the lowest word-level Penn Treebank test perplexity for a single model without dynamic evaluation, cache or pointer augmentation is **58.3**, reported by the paper represented by source **1707.05589** ([1707.05589_note.txt](https://arxiv.org/abs/1707.05589)). The next best eligible results are 62.4 from 1611.01578, 65.4 from 1607.03474, 66.0 from 1611.01462, 73.4 from 1512.05287, 74.3 from 1608.05859, 78.4 from 1409.2329, 78.9 from 1508.06615, and 87.38 from 1706.02222 ([1611.01578_note.txt](https://arxiv.org/abs/1611.01578); [1607.03474_note.txt](https://arxiv.org/abs/1607.03474); [1611.01462_note.txt](https://arxiv.org/abs/1611.01462); [1512.05287_note.txt](https://arxiv.org/abs/1512.05287); [1608.05859_note.txt](https://arxiv.org/abs/1608.05859); [1409.2329_note.txt](https://arxiv.org/abs/1409.2329); [1508.06615_note.txt](https://arxiv.org/abs/1508.06615); [1706.02222_note.txt](https://arxiv.org/abs/1706.02222)). The 58.3 result is notably lower than the next best eligible number and is reported under a deliberately controlled single-model evaluation without the excluded techniques.

## References

- 1409.2329_note.txt [Research note]. (2014). arXiv. https://arxiv.org/abs/1409.2329
- 1508.06615_note.txt [Research note]. (2015). arXiv. https://arxiv.org/abs/1508.06615
- 1512.05287_note.txt [Research note]. (2015). arXiv. https://arxiv.org/abs/1512.05287
- 1512.05287.txt [Paper excerpt]. (2015). arXiv. https://arxiv.org/abs/1512.05287
- 1607.03474_note.txt [Research note]. (2016). arXiv. https://arxiv.org/abs/1607.03474
- 1607.03474.txt [Paper excerpt]. (2016). arXiv. https://arxiv.org/abs/1607.03474
- 1608.05859_note.txt [Research note]. (2016). arXiv. https://arxiv.org/abs/1608.05859
- 1611.01462_note.txt [Research note]. (2016). arXiv. https://arxiv.org/abs/1611.01462
- 1611.01462.txt [Paper excerpt]. (2016). arXiv. https://arxiv.org/abs/1611.01462
- 1611.01578_note.txt [Research note]. (2016). arXiv. https://arxiv.org/abs/1611.01578
- 1706.02222_note.txt [Research note]. (2017). arXiv. https://arxiv.org/abs/1706.02222
- 1707.05589_note.txt [Research note]. (2017). arXiv. https://arxiv.org/abs/1707.05589
- 1711.03953.txt [Paper excerpt]. (2017). arXiv. https://arxiv.org/abs/1711.03953