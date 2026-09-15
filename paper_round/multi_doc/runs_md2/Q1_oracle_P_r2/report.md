# Lowest Word-Level Penn Treebank Test Perplexity for Single Models Without Dynamic Evaluation, Cache, or Pointer Augmentation: A Ranked Analysis

## Introduction

The Penn Treebank (PTB) word-level language modeling benchmark is a long-standing evaluation for neural language models. Performance is typically measured by perplexity (PPL), where lower values indicate better predictive performance. The provided corpus contains experimental setups and third-party notes on several neural language models that report PTB test perplexity. This report addresses a specific query: across the provided papers, which paper reports the lowest word-level test perplexity on PTB for a single model without dynamic evaluation, cache, or pointer augmentation, and what is that value? We also rank the papers by this metric.

The query’s constraints are precise. We must consider only single-model results, which excludes ensembles. We must exclude any result that uses dynamic evaluation, cache augmentation, or pointer augmentation. The query does not explicitly exclude fine-tuning, so we include fine-tuned single-model results unless a paper itself separates them. When both a primary paper text and a third-party note are available, we prioritize the primary paper text because it is the more reliable source ([1708.02182.txt](1708.02182.txt); [1708.02182_note.txt](1708.02182_note.txt)). This priority matters for one key discrepancy discussed below.

## Scope, Inclusion, and Exclusion Criteria

We examined all provided sources that report word-level PTB test perplexity. For each paper, we extracted the best single-model result that does not rely on dynamic evaluation, cache/pointer augmentation, or ensembling. We did not exclude fine-tuning unless the paper’s own reporting made clear that the result was obtained without it. We also treated model averaging as an ensemble technique and therefore excluded ensemble numbers such as the 38 large LSTMs at 68.7 or the 10 Variational LSTMs at 68.7 ([1512.05287_note.txt](1512.05287_note.txt); [1409.2329_note.txt](1409.2329_note.txt); [1611.01462_note.txt](1611.01462_note.txt)).

Several papers report lower perplexities with prohibited techniques. For example, the AWD-LSTM model with a continuous cache pointer reaches 52.8 test perplexity on PTB, but this is excluded because it uses cache/pointer augmentation ([1708.02182.txt](1708.02182.txt)). Similarly, AWD-LSTM-MoS with dynamic evaluation reaches 47.69, which is excluded because of dynamic evaluation ([1711.03953_note.txt](1711.03953_note.txt)). The Pointer Sentinel-LSTM at 70.9 is also excluded because it employs a pointer mechanism ([1611.01462_note.txt](1611.01462_note.txt)). These exclusions are important because they show that the lowest overall numbers in the corpus are not eligible for the query.

## Ranked Results

Table 1 presents the ranking of papers by their best single-model PTB word-level test perplexity without dynamic evaluation, cache/pointer augmentation, or ensembling. The rank is ascending, so Rank 1 is the lowest (best) perplexity.

| Rank | Paper (Source) | Model / Configuration | PTB Test PPL | Fine-Tuning? | Notes |
|---|---|---|---|---|---|
| 1 | Breaking the Softmax Bottleneck ([1711.03953_note.txt](1711.03953_note.txt)) | AWD-LSTM-MoS + finetune | **54.44** | Yes | Single model, no dynamic evaluation, cache, pointer, or ensemble. Without finetune, the same model reaches 55.97. |
| 2 | Regularizing and Optimizing LSTM Language Models ([1708.02182.txt](1708.02182.txt)) | AWD-LSTM (3-layer LSTM, tied) | **57.3** | Yes (per primary paper) | Primary paper abstract and Table 1 report 57.3. Table 4 reports 58.8 without fine-tuning. A third-party note claims 53.3, but this conflicts with the primary paper and is discussed below. |
| 3 | On the State of Art of Evaluation in Neural Language Models ([1707.05589_note.txt](1707.05589_note.txt)) | 4-layer LSTM, 24M parameters | **58.3** | No | Single model, no dynamic evaluation, cache/pointer, ensemble, or fine-tuning. |
| 4 | Neural Architecture Search with Reinforcement Learning ([1611.01578_note.txt](1611.01578_note.txt)) | NAS with base 8 and shared embeddings | **62.4** | No | Single model. Other NAS configurations report 64.0 and 67.9. |
| 5 | Recurrent Highway Networks ([1607.03474_note.txt](1607.03474_note.txt); [1607.03474.txt](1607.03474.txt)) | Variational RHN + WT | **65.4** | No | Single model. Without weight tying, 68.5. |
| 6 | Tying Word Vectors and Word Classifiers ([1611.01462_note.txt](1611.01462_note.txt)) | VD-RHN+RE | **66.0** | No | Single model. This is Zilly et al. 2016’s Variational RHN retrained with reused embeddings. |
| 7 | Variational LSTM ([1512.05287_note.txt](1512.05287_note.txt); [1512.05287.txt](1512.05287.txt)) | Large Variational LSTM, untied weights, MC dropout | **73.4** | No | Single model. The paper’s 10-model ensemble reaches 68.7 but is excluded. |
| 8 | Using the Output Embedding to Improve Language Models ([1608.05859_note.txt](1608.05859_note.txt)) | Large + Weight Tying | **74.3** | No | Single model. Small + WT + PR reaches 100.9. |
| 9 | Zaremba et al. 2014 (Recurrent Neural Network Regularization) ([1409.2329_note.txt](1409.2329_note.txt)) | Large regularized LSTM | **78.4** | No | Single model. The medium regularized LSTM reaches 82.7. Ensemble results are excluded. |
| 10 | Character-Aware Neural Language Models ([1508.06615_note.txt](1508.06615_note.txt); [1508.06615.txt](1508.06615.txt)) | LSTM-Char-Large | **78.9** | No | Single model. LSTM-Char-Small reaches 92.3. |
| 11 | GRURNTN and LSTMRNTN ([1706.02222_note.txt](1706.02222_note.txt)) | GRURNTN | **87.38** | No | Single model. LSTMRNTN reaches 96.97. The paper states no dynamic evaluation was used. |

## The Top Result: 54.44 from Breaking the Softmax Bottleneck

The lowest eligible value in the provided corpus is **54.44** test perplexity, reported by the paper *Breaking the Softmax Bottleneck: A High-Rank RNN Language Model* for its proposed AWD-LSTM-MoS model with fine-tuning ([1711.03953_note.txt](1711.03953_note.txt)). The same paper reports 55.97 for AWD-LSTM-MoS without fine-tuning, which is still lower than any other eligible result in the corpus. The paper also reports 47.69 with dynamic evaluation, but that result is excluded by the query’s constraints ([1711.03953_note.txt](1711.03953_note.txt)). No cache/pointer or ensemble result for AWD-LSTM-MoS is reported in the provided note ([1711.03953_note.txt](1711.03953_note.txt)).

This result is notable because it improves on the AWD-LSTM model from *Regularizing and Optimizing LSTM Language Models*, which reports 57.3 test perplexity for its 3-layer tied AWD-LSTM ([1708.02182.txt](1708.02182.txt)). The AWD-LSTM-MoS architecture builds on the same regularization and optimization strategies but introduces a mixture-of-softmaxes output layer to address the softmax bottleneck, yielding a lower perplexity ([1711.03953_note.txt](1711.03953_note.txt)). The improvement from 57.3 to 54.44 is approximately 2.86 perplexity points, which is meaningful on a benchmark where gains of a few tenths are often considered significant.

It is important to note that the 54.44 figure includes fine-tuning. If one were to exclude fine-tuning entirely, the lowest eligible value would become **55.97** from the same paper ([1711.03953_note.txt](1711.03953_note.txt)). This is still lower than the next best no-fine-tuning result, which is 58.3 from *On the State of Art of Evaluation in Neural Language Models* ([1707.05589_note.txt](1707.05589_note.txt)). Therefore, even under a stricter interpretation that disallows fine-tuning, the top-ranked paper would remain the same, though the exact value would shift from 54.44 to 55.97.

## The Second-Best Result and the AWD-LSTM Discrepancy

The second-ranked paper is *Regularizing and Optimizing LSTM Language Models*, which reports 57.3 test perplexity for AWD-LSTM, a 3-layer LSTM with tied weights, as a single model without cache/pointer ([1708.02182.txt](1708.02182.txt)). The paper’s abstract states that the model achieves “state-of-the-art word level perplexities on two data sets: 57.3 on Penn Treebank and 65.8 on WikiText-2” ([1708.02182.txt](1708.02182.txt)). Table 1 lists AWD-LSTM - 3-layer LSTM (tied) at 60.0 validation and 57.3 test perplexity ([1708.02182.txt](1708.02182.txt)). Table 4 lists an ablation without fine-tuning at 58.8 test perplexity, indicating that the full model includes fine-tuning and that removing it degrades performance ([1708.02182.txt](1708.02182.txt)).

However, a third-party research note on the same paper claims that the paper reports **53.3** test perplexity for AWD-LSTM and that “this result includes the fine-tuning step” ([1708.02182_note.txt](1708.02182_note.txt)). This claim directly contradicts the primary paper’s abstract, Table 1, and Table 4. The note also states that the no-fine-tuning ablation is 58.8, which matches Table 4, but the 53.3 figure does not appear in the primary paper text. Given the instruction to prioritize reliable sources, we treat the primary paper text as authoritative and therefore use 57.3 for AWD-LSTM. If one were to accept the third-party note’s 53.3, AWD-LSTM would become the lowest eligible result, ahead of 54.44. But because the primary source contradicts the note, and because the note provides no supporting table or context for 53.3, we judge 57.3 to be the more defensible value.

This discrepancy is significant for the ranking. Under our reliability prioritization, the top rank goes to *Breaking the Softmax Bottleneck* at 54.44. Under a less reliable reading that trusts the third-party note, the top rank would go to *Regularizing and Optimizing LSTM Language Models* at 53.3. We therefore report the ranking based on the primary paper text while noting the alternative value.

## Other Notably Excluded Results

Several results that would otherwise rank at or near the top are excluded by the query’s constraints. The AWD-LSTM model with a continuous cache pointer reaches **52.8** test perplexity on PTB, but this uses cache/pointer augmentation and is therefore ineligible ([1708.02182.txt](1708.02182.txt); [1708.02182_note.txt](1708.02182_note.txt)). This result is lower than 54.44, but it cannot be considered under the current query.

The AWD-LSTM-MoS model with dynamic evaluation reaches **47.69**, which is the lowest reported PTB test perplexity in the entire provided corpus, but it is excluded because of dynamic evaluation ([1711.03953_note.txt](1711.03953_note.txt)). Similarly, the Pointer Sentinel-LSTM reaches 70.9, but it uses a pointer mechanism and is excluded ([1611.01462_note.txt](1611.01462_note.txt)). Ensemble results such as 68.7 for 38 large LSTMs or 10 large VD-LSTMs are also excluded because the query specifies a single model ([1409.2329_note.txt](1409.2329_note.txt); [1611.01462_note.txt](1611.01462_note.txt); [1512.05287_note.txt](1512.05287_note.txt)).

These exclusions are crucial for interpreting the ranking. They show that the provided corpus contains several techniques that push PTB perplexity well below 54.44, but the query deliberately restricts the comparison to a specific evaluation setting.

## Discussion of the Broader Ranking

The ranked table reveals a clear progression in PTB performance among eligible single models. The top three results—54.44, 57.3, and 58.3—are all below 60, while the next group (62.4, 65.4, 66.0) is in the low-to-mid 60s. The remaining models range from 73.4 to 87.38. This spread reflects differences in architecture, regularization, and training procedures.

The best-performing models in the eligible set tend to use weight tying, advanced regularization, and careful optimization. The AWD-LSTM-MoS model combines the AWD-LSTM regularization strategies with a mixture-of-softmaxes output layer ([1711.03953_note.txt](1711.03953_note.txt)). The AWD-LSTM model itself uses DropConnect on hidden-to-hidden weights and NT-ASGD, which are described as key innovations ([1708.02182.txt](1708.02182.txt)). The 4-layer LSTM from *On the State of Art of Evaluation* achieves 58.3 through systematic evaluation and a relatively large parameter count of 24M ([1707.05589_note.txt](1707.05589_note.txt)). The NAS model reaches 62.4 by using reinforcement learning to discover a recurrent cell architecture ([1611.01578_note.txt](1611.01578_note.txt)). The Variational RHN with weight tying reaches 65.4 by increasing recurrence depth and using variational dropout ([1607.03474_note.txt](1607.03474_note.txt)). These results collectively show that architectural search, recurrent depth, and regularization all contribute to lower perplexity.

By contrast, the models at the bottom of the eligible ranking—GRURNTN at 87.38 and LSTMRNTN at 96.97—are still improvements over their respective baselines, but they do not match the regularization and optimization advances of the top models ([1706.02222_note.txt](1706.02222_note.txt)). The Character-Aware Neural Language Models, with 78.9, and the large weight-tied NNLM, with 74.3, are competitive but not state-of-the-art under the strict conditions of the query ([1508.06615_note.txt](1508.06615_note.txt); [1608.05859_note.txt](1608.05859_note.txt)).

## Conclusion

Based on the provided sources, and prioritizing primary paper texts over third-party notes, the paper that reports the lowest word-level PTB test perplexity for a single model without dynamic evaluation, cache or pointer augmentation is **Breaking the Softmax Bottleneck: A High-Rank RNN Language Model**, with a value of **54.44** for AWD-LSTM-MoS with fine-tuning ([1711.03953_note.txt](1711.03953_note.txt)). If fine-tuning is disallowed, the same paper’s AWD-LSTM-MoS without fine-tuning still leads at **55.97** ([1711.03953_note.txt](1711.03953_note.txt)). The second-ranked paper is *Regularizing and Optimizing LSTM Language Models*, whose AWD-LSTM reports **57.3** test perplexity per the primary paper, though a third-party note claims 53.3 ([1708.02182.txt](1708.02182.txt); [1708.02182_note.txt](1708.02182_note.txt)). The third-ranked paper is *On the State of Art of Evaluation in Neural Language Models*, with **58.3** ([1707.05589_note.txt](1707.05589_note.txt)). The remaining ranking follows as presented in Table 1.

The key caveat is the AWD-LSTM discrepancy. If one were to trust the third-party note’s 53.3 over the primary paper’s 57.3, the top rank would change. However, the primary paper’s abstract and tables consistently report 57.3, and the note provides no corroborating evidence. Therefore, the most reliable conclusion is that *Breaking the Softmax Bottleneck* holds the lowest eligible value at 54.44, with the no-fine-tuning variant at 55.97 still leading under a stricter interpretation.

## References

- 1508.06615. (2015). *Character-Aware Neural Language Models*. Retrieved from [1508.06615.txt](1508.06615.txt)
- 1508.06615_note. (n.d.). *Third-party research note: Character-Aware Neural Language Models*. Retrieved from [1508.06615_note.txt](1508.06615_note.txt)
- 1512.05287. (2015). *Variational LSTM*. Retrieved from [1512.05287.txt](1512.05287.txt)
- 1512.05287_note. (n.d.). *Third-party research note: Variational LSTM*. Retrieved from [1512.05287_note.txt](1512.05287_note.txt)
- 1607.03474. (2016). *Recurrent Highway Networks*. Retrieved from [1607.03474.txt](1607.03474.txt)
- 1607.03474_note. (n.d.). *Third-party research note: Recurrent Highway Networks*. Retrieved from [1607.03474_note.txt](1607.03474_note.txt)
- 1608.05859_note. (n.d.). *Third-party research note: Using the Output Embedding to Improve Language Models*. Retrieved from [1608.05859_note.txt](1608.05859_note.txt)
- 1611.01462_note. (n.d.). *Third-party research note: Tying Word Vectors and Word Classifiers: A Loss Framework for Language Modeling*. Retrieved from [1611.01462_note.txt](1611.01462_note.txt)
- 1611.01578_note. (n.d.). *Third-party research note: Neural Architecture Search with Reinforcement Learning*. Retrieved from [1611.01578_note.txt](1611.01578_note.txt)
- 1706.02222_note. (n.d.). *Third-party research note: GRURNTN and LSTMRNTN*. Retrieved from [1706.02222_note.txt](1706.02222_note.txt)
- 1707.05589_note. (n.d.). *Third-party research note: On the State of Art of Evaluation in Neural Language Models*. Retrieved from [1707.05589_note.txt](1707.05589_note.txt)
- 1708.02182. (2017). *Regularizing and Optimizing LSTM Language Models*. Retrieved from [1708.02182.txt](1708.02182.txt)
- 1708.02182_note. (n.d.). *Third-party research note: Regularizing and Optimizing LSTM Language Models*. Retrieved from [1708.02182_note.txt](1708.02182_note.txt)
- 1711.03953_note. (n.d.). *Third-party research note: Breaking the Softmax Bottleneck: A High-Rank RNN Language Model*. Retrieved from [1711.03953_note.txt](1711.03953_note.txt)
- 1409.2329_note. (n.d.). *Third-party research note: Recurrent Neural Network Regularization*. Retrieved from [1409.2329_note.txt](1409.2329_note.txt)