# Lowest Penn Treebank Word-Level Test Perplexity for Single Models Without Dynamic Evaluation or Cache/Pointer Augmentation

## Executive Summary

Across the provided papers, the lowest reported word-level Penn Treebank test perplexity for a single model that does **not** use dynamic evaluation and does **not** use cache or pointer augmentation is **54.44**, reported for **AWD-LSTM-MoS with fine-tuning** in the source note `1711.03953_note.txt` ([1711.03953_note.txt](1711.03953_note.txt)). This value is lower than all other eligible single-model results in the provided information. If one applies a stricter criterion and also excludes fine-tuning, the lowest eligible value becomes **55.97**, reported for **AWD-LSTM-MoS without fine-tuning** in the same paper ([1711.03953_note.txt](1711.03953_note.txt)). Thus, under either interpretation, the same paper reports the lowest eligible Penn Treebank word-level test perplexity among the provided sources.

The main ranking below uses the query’s explicit exclusion criteria: single model, no dynamic evaluation, and no cache or pointer augmentation. Ensembles are excluded because the query asks for a single model. Fine-tuning is allowed in the primary ranking because the query does not exclude it. A sensitivity table excludes fine-tuning as well.

## Scope, Definitions, and Inclusion Criteria

This report evaluates only the information provided in the source notes and excerpts. The target metric is **word-level Penn Treebank test perplexity** for language modeling. Lower perplexity is better. The inclusion criteria are:

1. **Single model**: The result must not be an ensemble, model average, or multi-model combination.
2. **No dynamic evaluation**: Results obtained with dynamic evaluation are excluded.
3. **No cache or pointer augmentation**: Results using continuous cache, cache memory, pointer mechanisms, or similar augmentation are excluded.
4. **Word-level Penn Treebank test perplexity**: Character-level or word-level results are considered only when the reported number is a word-level Penn Treebank test perplexity.
5. **Fine-tuning**: The query does not explicitly exclude fine-tuning; therefore, the primary ranking allows it. A separate sensitivity analysis excludes it.

The Penn Treebank language modeling setup is standard: the English Penn Treebank with the Mikolov preprocessing, approximately 1 million tokens, and a vocabulary of about 10,000 words ([1508.06615.txt](1508.06615.txt)). The provided notes report single-model and ensemble results separately for several papers, and this distinction is critical for ranking ([1512.05287.txt](1512.05287.txt)).

## The Lowest Reported Result

The lowest eligible result is **54.44 test perplexity** for **AWD-LSTM-MoS with fine-tuning** on word-level Penn Treebank ([1711.03953_note.txt](1711.03953_note.txt)). The source note states that the paper reports “word-level Penn Treebank test perplexity for its proposed model, AWD-LSTM-MoS, in single-model settings without dynamic evaluation” and that “Table 1 lists 55.97 for AWD-LSTM-MoS without finetune and 54.44 for AWD-LSTM-MoS with finetune” ([1711.03953_note.txt](1711.03953_note.txt)). The same note clarifies that the paper also reports **47.69** for AWD-LSTM-MoS with dynamic evaluation, but that result is excluded here because of the dynamic evaluation criterion ([1711.03953_note.txt](1711.03953_note.txt)).

A related excluded result is the **52.8** Penn Treebank test perplexity reported for AWD-LSTM augmented with a continuous cache pointer ([1708.02182_note.txt](1708.02182_note.txt)). Although 52.8 is lower than 54.44, it uses a cache/pointer mechanism and therefore fails the inclusion criteria. This distinction is important: the lowest number overall in the provided sources may be lower, but the lowest number satisfying the stated constraints is 54.44.

If fine-tuning is also disallowed, the lowest eligible number becomes **55.97**, again from AWD-LSTM-MoS without fine-tuning in `1711.03953_note.txt` ([1711.03953_note.txt](1711.03953_note.txt)). This is still lower than all other non-fine-tuned single models in the provided corpus.

## Ranked Papers by Best Eligible Single-Model Penn Treebank Test Perplexity

The following table ranks each paper by its best eligible single-model, no-dynamic-evaluation, no-cache/pointer word-level Penn Treebank test perplexity. Fine-tuning is allowed in this primary ranking. Each source citation is embedded in the source column.

| Rank | Paper / Source | Best eligible model | PTB test perplexity | Fine-tuning? | Notes |
|---:|---|---|---:|---|---|
| 1 | [1711.03953_note.txt](1711.03953_note.txt) | AWD-LSTM-MoS + finetune | 54.44 | Yes | Single model, no dynamic evaluation, no cache/pointer; dynamic-evaluation result 47.69 excluded |
| 2 | [1708.02182_note.txt](1708.02182_note.txt) | AWD-LSTM (3-layer, tied weights) | 57.3 | Yes | Single model; includes fine-tuning; continuous cache-pointer result 52.8 excluded |
| 3 | [1707.05589_note.txt](1707.05589_note.txt) | 4-layer LSTM (24M parameters) | 58.3 | Not reported | Single model, no dynamic evaluation, no cache/pointer, no ensemble, no fine-tuning |
| 4 | [1611.01578_note.txt](1611.01578_note.txt) | NAS with base 8 and shared embeddings | 62.4 | Not reported | Single model; no dynamic evaluation, cache/pointer, ensemble, or fine-tuning |
| 5 | [1607.03474_note.txt](1607.03474_note.txt) | Variational RHN + WT | 65.4 | Not reported | Single model; variational dropout and weight tying; no dynamic evaluation, cache/pointer, or ensemble |
| 6 | [1611.01462_note.txt](1611.01462_note.txt) | VD-RHN+RE | 66.0 | Not reported | Single model; cache/pointer and ensemble baselines excluded |
| 7 | [1512.05287_note.txt](1512.05287_note.txt) | Variational LSTM, large, untied weights, MC dropout | 73.4 | Not reported | Single model; ensemble result 68.7 excluded |
| 8 | [1608.05859_note.txt](1608.05859_note.txt) | Large NNLM + Weight Tying | 74.3 | Not reported | Single model; no dynamic evaluation, cache/pointer, ensemble, or fine-tuning |
| 9 | [1409.2329_note.txt](1409.2329_note.txt) | Large regularized LSTM | 78.4 | Not reported | Single model; model-averaging results 68.7, 69.5, 73.6, etc. excluded |
| 10 | [1508.06615_note.txt](1508.06615_note.txt) | LSTM-Char-Large | 78.9 | Not reported | Single model; no dynamic evaluation, cache/pointer, or ensemble |
| 11 | [1706.02222_note.txt](1706.02222_note.txt) | GRURNTN | 87.38 | No | Single model; no dynamic evaluation; no cache/pointer or ensemble |

The ranking shows a clear separation between the lowest group—AWD-LSTM-MoS, AWD-LSTM, and the 4-layer LSTM of `1707.05589_note.txt`—and the rest. The top three eligible results are all below 60 test perplexity, while the next best eligible result is 62.4 from Neural Architecture Search ([1611.01578_note.txt](1611.01578_note.txt)). The GRURNTN result at 87.38 is the highest best-eligible value among the provided papers ([1706.02222_note.txt](1706.02222_note.txt)).

## Sensitivity Analysis: Excluding Fine-Tuning

Because the query does not explicitly mention fine-tuning, the primary ranking allows it. However, some readers may interpret “without dynamic evaluation, cache or pointer augmentation” as excluding other test-time or training enhancements as well. The table below re-ranks papers when fine-tuning is also excluded. This changes the order of the second and third positions but not the identity of the lowest result.

| Rank | Paper / Source | Best eligible model without fine-tuning | PTB test perplexity | Notes |
|---:|---|---|---:|---|
| 1 | [1711.03953_note.txt](1711.03953_note.txt) | AWD-LSTM-MoS without finetune | 55.97 | Single model, no dynamic evaluation, no cache/pointer |
| 2 | [1707.05589_note.txt](1707.05589_note.txt) | 4-layer LSTM (24M parameters) | 58.3 | Single model, no dynamic evaluation, no cache/pointer, no ensemble |
| 3 | [1708.02182_note.txt](1708.02182_note.txt) | AWD-LSTM no-fine-tuning ablation | 58.8 | Single model; no cache/pointer; no dynamic evaluation |
| 4 | [1611.01578_note.txt](1611.01578_note.txt) | NAS base 8, shared embeddings | 62.4 | Single model; no dynamic evaluation, cache/pointer, or ensemble |
| 5 | [1607.03474_note.txt](1607.03474_note.txt) | Variational RHN + WT | 65.4 | Single model; no dynamic evaluation, cache/pointer, or ensemble |
| 6 | [1611.01462_note.txt](1611.01462_note.txt) | VD-RHN+RE | 66.0 | Single model; cache/pointer and ensemble baselines excluded |
| 7 | [1512.05287_note.txt](1512.05287_note.txt) | Variational LSTM large MC | 73.4 | Single model; ensemble excluded |
| 8 | [1608.05859_note.txt](1608.05859_note.txt) | Large NNLM + Weight Tying | 74.3 | Single model; no dynamic evaluation, cache/pointer, or ensemble |
| 9 | [1409.2329_note.txt](1409.2329_note.txt) | Large regularized LSTM | 78.4 | Single model; model averages excluded |
| 10 | [1508.06615_note.txt](1508.06615_note.txt) | LSTM-Char-Large | 78.9 | Single model; no dynamic evaluation, cache/pointer, or ensemble |
| 11 | [1706.02222_note.txt](1706.02222_note.txt) | GRURNTN | 87.38 | Single model; no dynamic evaluation, cache/pointer, or ensemble |

Even with this stricter interpretation, the same paper—`1711.03953_note.txt`—owns the lowest eligible value, now 55.97 rather than 54.44 ([1711.03953_note.txt](1711.03953_note.txt)). This robustness strengthens the central finding.

## Detailed Notes on Each Ranked Paper

### 1711.03953: Breaking the Softmax Bottleneck

The paper proposes AWD-LSTM-MoS and reports 55.97 for the model without fine-tuning and 54.44 with fine-tuning ([1711.03953_note.txt](1711.03953_note.txt)). It also reports 47.69 with dynamic evaluation, which is excluded. The note explicitly states that the paper does not report cache/pointer or ensemble results for its proposed model on Penn Treebank ([1711.03953_note.txt](1711.03953_note.txt)). The 54.44 result is therefore the lowest eligible single-model value in the provided corpus.

### 1708.02182: Regularizing and Optimizing LSTM Language Models

The paper proposes AWD-LSTM and reports a Penn Treebank test perplexity of 57.3 for a 3-layer LSTM with tied weights as a single model without cache/pointer ([1708.02182_note.txt](1708.02182_note.txt)). This result includes the fine-tuning step. The paper also reports a no-fine-tuning ablation at 58.8, and a continuous cache pointer variant at 52.8 ([1708.02182_note.txt](1708.02182_note.txt)). The 52.8 result is excluded because of cache/pointer augmentation. The 57.3 result is the second-lowest eligible value when fine-tuning is allowed, and the 58.8 result is third-lowest when fine-tuning is excluded.

### 1707.05589: On the State of the Art of Evaluation in Neural Language Models

The paper reports a best word-level Penn Treebank test perplexity of 58.3 for a 4-layer LSTM with 24M parameters ([1707.05589_note.txt](1707.05589_note.txt)). The authors emphasize that this is a single model without dynamic evaluation, cache/pointer, ensemble, or fine-tuning ([1707.05589_note.txt](1707.05589_note.txt)). This makes the result particularly clean for the present ranking, although it is not the lowest overall.

### 1611.01578: Neural Architecture Search with Reinforcement Learning

The paper reports 62.4 for the best Neural Architecture Search model, with 64.0 and 67.9 for other configurations ([1611.01578_note.txt](1611.01578_note.txt)). These are single-model test perplexities without dynamic evaluation, cache/pointer, ensemble, or fine-tuning ([1611.01578_note.txt](1611.01578_note.txt)). The 62.4 result is the best eligible value from this paper, ranking fourth in the primary table.

### 1607.03474: Recurrent Highway Networks

The paper reports 65.4 for Variational RHN + WT and 68.5 for Variational RHN without WT ([1607.03474_note.txt](1607.03474_note.txt)). The best 10-layer model with reduced weight decay improves to 67.9 validation and 65.4 test perplexity ([1607.03474.txt](1607.03474.txt)). The note states that the best Penn Treebank result is a single model, and that dynamic evaluation, cache/pointer, ensemble, and fine-tuning are not reported for the proposed model ([1607.03474_note.txt](1607.03474_note.txt)). The 65.4 result ranks fifth.

### 1611.01462: Tying Word Vectors and Word Classifiers

The paper reports VD-RHN+RE with reused embeddings at 66.0 test perplexity and 68.1 validation perplexity on Penn Treebank ([1611.01462_note.txt](1611.01462_note.txt)). The note describes this as “best overall” in that paper. Cache/pointer baselines such as Pointer Sentinel-LSTM at 70.9 and RNN+LDA+KN-5+Cache at 92.0 are excluded, as are ensemble baselines at 68.7 ([1611.01462_note.txt](1611.01462_note.txt)). The 66.0 result ranks sixth.

### 1512.05287: A Theoretically Grounded Application of Dropout in Recurrent Neural Networks

The paper reports 73.4 test perplexity for the proposed Variational LSTM on Penn Treebank, a single-model result for the large Variational LSTM with untied weights and MC dropout at test time ([1512.05287_note.txt](1512.05287_note.txt)). The table caption identifies the results as single-model perplexity on test and validation sets ([1512.05287.txt](1512.05287.txt)). The paper also reports an ensemble result of 68.7 using 10 Variational LSTMs, which is excluded ([1512.05287_note.txt](1512.05287_note.txt)). The 73.4 result ranks seventh.

### 1608.05859: Using the Output Embedding to Improve Language Models

The paper reports 74.3 test perplexity for the large NNLM with weight tying and 100.9 for the small NNLM with weight tying and projection regularization ([1608.05859_note.txt](1608.05859_note.txt)). These are single-model results without dynamic evaluation, cache/pointer, ensemble, or fine-tuning ([1608.05859_note.txt](1608.05859_note.txt)). The 74.3 result ranks eighth.

### 1409.2329: Regularized LSTMs

The paper reports model-averaging results such as 77.0, 73.3, 72.0, 73.6, 69.5, and 68.7 for various ensemble sizes ([1409.2329_note.txt](1409.2329_note.txt)). These are excluded because they are model averages. The best eligible single-model results are the medium regularized LSTM at 82.7 and the large regularized LSTM at 78.4 ([1409.2329_note.txt](1409.2329_note.txt)). The 78.4 result ranks ninth in the primary table.

### 1508.06615: Character-Aware Neural Language Models

The paper reports word-level Penn Treebank test perplexity of 78.9 for LSTM-Char-Large and 92.3 for LSTM-Char-Small ([1508.06615_note.txt](1508.06615_note.txt)). These are single-model results, and the paper explicitly excludes ensembles from comparison ([1508.06615_note.txt](1508.06615_note.txt)). No dynamic evaluation, cache/pointer, or fine-tuning results appear. The 78.9 result ranks tenth.

### 1706.02222: GRURNTN and LSTMRNTN

The paper proposes GRURNTN and LSTMRNTN. For word-level Penn Treebank, it reports 87.38 test perplexity for GRURNTN and 96.97 for LSTMRNTN ([1706.02222_note.txt](1706.02222_note.txt)). These are individual models without dynamic evaluation, cache/pointer, ensemble, or fine-tuning ([1706.02222_note.txt](1706.02222_note.txt)). The best eligible value is 87.38, which ranks eleventh.

## Excluded Results and Why

Several lower perplexities appear in the provided sources but are excluded under the query’s criteria:

- **Dynamic evaluation**: AWD-LSTM-MoS + dynamic evaluation at 47.69 is excluded ([1711.03953_note.txt](1711.03953_note.txt)). RNNLM with dynamic evaluation at 123.2 is also excluded ([1706.02222_note.txt](1706.02222_note.txt)).
- **Cache/pointer augmentation**: AWD-LSTM + continuous cache pointer at 52.8 is excluded ([1708.02182_note.txt](1708.02182_note.txt)). Pointer Sentinel-LSTM at 70.9 and RNN+LDA+KN-5+Cache at 92.0 are excluded ([1611.01462_note.txt](1611.01462_note.txt)).
- **Ensembles and model averaging**: 10 Variational LSTMs at 68.7, 38 Large LSTMs at 68.7, 10 Large VD-LSTMs at 68.7, and 2/5/10 medium and large regularized LSTM averages at 77.0, 73.3, 72.0, 73.6, 69.5, and 68.7 are excluded ([1512.05287_note.txt](1512.05287_note.txt), [1611.01462_note.txt](1611.01462_note.txt), [1409.2329_note.txt](1409.2329_note.txt)).

These exclusions are consistent with the query’s requirement of a single model without dynamic evaluation or cache/pointer augmentation.

## Reliability and Limitations

The evidence comes from provided research notes and partial paper excerpts. Some sources are primary excerpts, such as `1607.03474.txt`, `1508.06615.txt`, and `1512.05287.txt`, while others are third-party research notes that summarize reported tables ([1607.03474.txt](1607.03474.txt), [1508.06615.txt](1508.06615.txt), [1512.05287.txt](1512.05287.txt)). The notes are generally explicit about whether a result is single-model, ensemble, dynamic-evaluation, or cache/pointer-based. However, not every paper reports standard deviations, hyperparameter details, or whether fine-tuning was used. The primary ranking therefore follows the most literal reading of the query: single model, no dynamic evaluation, no cache/pointer, with fine-tuning permitted. The sensitivity analysis addresses the main ambiguity. The ranking is limited to the provided information; no external leaderboard or newer results are considered.

## Conclusion

Under the stated criteria—single model, word-level Penn Treebank test perplexity, no dynamic evaluation, and no cache or pointer augmentation—the lowest reported value is **54.44**, from **AWD-LSTM-MoS with fine-tuning** in `1711.03953_note.txt` ([1711.03953_note.txt](1711.03953_note.txt)). If fine-tuning is also excluded, the lowest becomes **55.97** from AWD-LSTM-MoS without fine-tuning in the same paper ([1711.03953_note.txt](1711.03953_note.txt)). The next best eligible results are AWD-LSTM at 57.3, the 4-layer LSTM at 58.3, and Neural Architecture Search at 62.4 ([1708.02182_note.txt](1708.02182_note.txt), [1707.05589_note.txt](1707.05589_note.txt), [1611.01578_note.txt](1611.01578_note.txt)). The ranking is robust to the fine-tuning interpretation, and the same paper remains the source of the lowest eligible value in both cases.

## References

- 1409.2329_note.txt. (n.d.). *Regularized LSTM Penn Treebank notes* [Research note]. Available from 1409.2329_note.txt
- 1508.06615.txt. (n.d.). *Character-Aware Neural Language Models: Experimental setup* [Paper excerpt]. Available from 1508.06615.txt
- 1508.06615_note.txt. (n.d.). *Character-Aware Neural Language Models: Penn Treebank results* [Research note]. Available from 1508.06615_note.txt
- 1512.05287.txt. (n.d.). *A Theoretically Grounded Application of Dropout in Recurrent Neural Networks: Table excerpt* [Paper excerpt]. Available from 1512.05287.txt
- 1512.05287_note.txt. (n.d.). *A Theoretically Grounded Application of Dropout in Recurrent Neural Networks: Penn Treebank results* [Research note]. Available from 1512.05287_note.txt
- 1607.03474.txt. (n.d.). *Recurrent Highway Networks: Penn Treebank section* [Paper excerpt]. Available from 1607.03474.txt
- 1607.03474_note.txt. (n.d.). *Recurrent Highway Networks: Penn Treebank results* [Research note]. Available from 1607.03474_note.txt
- 1608.05859_note.txt. (n.d.). *Using the Output Embedding to Improve Language Models: Penn Treebank results* [Research note]. Available from 1608.05859_note.txt
- 1611.01462_note.txt. (n.d.). *Tying Word Vectors and Word Classifiers: Penn Treebank results* [Research note]. Available from 1611.01462_note.txt
- 1611.01578_note.txt. (n.d.). *Neural Architecture Search with Reinforcement Learning: Penn Treebank results* [Research note]. Available from 1611.01578_note.txt
- 1706.02222_note.txt. (n.d.). *GRURNTN and LSTMRNTN: Penn Treebank results* [Research note]. Available from 1706.02222_note.txt
- 1707.05589_note.txt. (n.d.). *On the State of the Art of Evaluation in Neural Language Models: Penn Treebank results* [Research note]. Available from 1707.05589_note.txt
- 1708.02182_note.txt. (n.d.). *Regularizing and Optimizing LSTM Language Models: Penn Treebank results* [Research note]. Available from 1708.02182_note.txt
- 1711.03953_note.txt. (n.d.). *Breaking the Softmax Bottleneck: Penn Treebank results* [Research note]. Available from 1711.03953_note.txt