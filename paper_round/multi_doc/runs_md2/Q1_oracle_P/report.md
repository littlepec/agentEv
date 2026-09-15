# Lowest Word-Level Penn Treebank Test Perplexity for Single Models Without Dynamic Evaluation, Cache, or Pointer Augmentation

## Introduction

The Penn Treebank (PTB) word-level language modeling benchmark remains a central point of comparison for neural language models. Reported perplexities vary widely depending on model size, regularization, training procedures, and whether test-time techniques such as dynamic evaluation or cache/pointer augmentation are used. This report addresses a specific question: across the provided papers, which paper reports the lowest word-level PTB test perplexity for a single model without dynamic evaluation, cache, or pointer augmentation, and what is that value? It then ranks the papers by this number.

To answer this question, I synthesized results from the provided source documents, which include primary paper excerpts and third-party research notes. The inclusion criteria are strict: the result must be a word-level PTB test perplexity, must come from a single model (not an ensemble or model averaging), and must not use dynamic evaluation, continuous cache, pointer sentinel, or similar test-time augmentation. Fine-tuning is not excluded by the query, so fine-tuned single-model results are eligible unless they also use dynamic evaluation or cache/pointer mechanisms. Where a paper reports multiple configurations, I use the best eligible configuration for ranking.

## Source Reliability and Data Conflicts

Before ranking, it is necessary to address a reliability issue. The AWD-LSTM paper text ([1708.02182.txt](1708.02182.txt)) reports a PTB test perplexity of 57.3 in its abstract and in Table 1. The same source’s Table 4 reports 57.3 for the full model and 58.8 when fine-tuning is removed ([1708.02182.txt](1708.02182.txt)). However, one provided research note states that the paper reports 53.3 for AWD-LSTM without cache/pointer ([1708.02182_note.txt](1708.02182_note.txt)). This is inconsistent with the primary paper text: the abstract, Table 1, and Table 4 all indicate 57.3, and the note itself says the no-fine-tuning ablation is 58.8. The 53.3 figure appears to be a transcription error. In this report, I prioritize the primary paper text and treat 57.3 as the reliable AWD-LSTM result. If one were to accept the note’s 53.3, then AWD-LSTM would be the lowest at 53.3; however, based on the primary source, the lowest eligible result is different.

A second reliability consideration concerns the AWD-LSTM-MoS result. The primary source excerpt for [1711.03953.txt](1711.03953.txt) shows only the dynamic-evaluation row, 47.69, and baseline rows with cache/pointer and dynamic evaluation. The associated note ([1711.03953_note.txt](1711.03953_note.txt)) explicitly states that Table 1 lists 55.97 for AWD-LSTM-MoS without fine-tuning and 54.44 with fine-tuning, both without dynamic evaluation. Since no primary text contradicts these numbers, I use the note’s 54.44 as the best eligible AWD-LSTM-MoS result.

## Ranked Eligible Single-Model Results

Table 1 lists the best eligible PTB word-level test perplexity from each provided paper. The ranking uses the lowest eligible value per paper. All entries are single-model results without dynamic evaluation, cache, or pointer augmentation. Fine-tuning status is noted where relevant.

### Table 1. Best Eligible Single-Model PTB Word-Level Test Perplexities (No Dynamic Evaluation, Cache, or Pointer)

| Rank | Paper / Source | Model | Test PPL | Fine-tuning | Notes |
|------|----------------|-------|----------|-------------|-------|
| 1 | 1711.03953 | AWD-LSTM-MoS | 54.44 | Yes | Single model; no dynamic/cache/pointer; without fine-tuning 55.97 |
| 2 | 1708.02182 | AWD-LSTM (3-layer tied) | 57.3 | Yes | Primary paper text; note reports 53.3 (inconsistent) |
| 3 | 1707.05589 | 4-layer LSTM (24M) | 58.3 | No | Single model; no dynamic/cache/pointer |
| 4 | 1611.01578 | NAS (base 8, shared embeddings, 54M) | 62.4 | Not reported | Single model; no dynamic/cache/pointer |
| 5 | 1607.03474 | Variational RHN + WT (23M) | 65.4 | Not reported | Single model; variational dropout + weight tying |
| 6 | 1611.01462 | VD-RHN + RE | 66.0 | Not reported | Single model; reused embeddings |
| 7 | 1512.05287 | Variational LSTM (large, untied, MC dropout) | 73.4 | Not reported | Single model; no dynamic/cache/pointer |
| 8 | 1608.05859 | Large NNLM + weight tying | 74.3 | Not reported | Single model; no dynamic/cache/pointer |
| 9 | 1409.2329 | Large regularized LSTM | 78.4 | Not reported | Single model; model averaging excluded |
| 10 | 1508.06615 | LSTM-Char-Large | 78.9 | Not reported | Single model; ensembles excluded |
| 11 | 1706.02222 | GRURNTN | 87.38 | Not reported | Single model; no dynamic evaluation |

## Detailed Findings by Paper

### 1. AWD-LSTM-MoS (1711.03953) — 54.44

The lowest eligible single-model PTB test perplexity in the provided set is 54.44, reported for AWD-LSTM-MoS with fine-tuning in “Breaking the Softmax Bottleneck: A High-Rank RNN Language Model” ([1711.03953_note.txt](1711.03953_note.txt)). The same note states that AWD-LSTM-MoS without fine-tuning reaches 55.97. Both values are single-model results without dynamic evaluation, cache, or pointer augmentation. The paper does report a lower value, 47.69, for AWD-LSTM-MoS with dynamic evaluation, but that is explicitly excluded by the query’s criteria ([1711.03953_note.txt](1711.03953_note.txt); [1711.03953.txt](1711.03953.txt)). The paper also lists Merity et al. 2017 – AWD-LSTM + continuous cache pointer at 52.8 and Krause et al. 2017 – AWD-LSTM + dynamic evaluation at 51.1, both of which are excluded because they use cache/pointer or dynamic evaluation ([1711.03953.txt](1711.03953.txt)). Thus, under the stated criteria, 54.44 is the best eligible result.

### 2. AWD-LSTM (1708.02182) — 57.3

The primary AWD-LSTM paper reports 57.3 test perplexity for a 3-layer tied LSTM with 24M parameters ([1708.02182.txt](1708.02182.txt)). This result includes fine-tuning, as shown by Table 4, where removing fine-tuning degrades perplexity to 58.8 ([1708.02182.txt](1708.02182.txt)). The paper also reports 52.8 with a continuous cache pointer, but that is excluded because it uses cache/pointer augmentation ([1708.02182.txt](1708.02182.txt)). The abstract explicitly states state-of-the-art word-level perplexities of 57.3 on Penn Treebank and 65.8 on WikiText-2 ([1708.02182.txt](1708.02182.txt)). As noted above, one research note claims 53.3 for AWD-LSTM without cache/pointer ([1708.02182_note.txt](1708.02182_note.txt)), but this conflicts with the primary paper text and is not used for ranking. If it were accepted, AWD-LSTM would rank first at 53.3.

### 3. 4-Layer LSTM (1707.05589) — 58.3

“On the State of the Art of Evaluation in Neural Language Models” reports a best word-level PTB test perplexity of 58.3 for a 4-layer LSTM with 24M parameters ([1707.05589_note.txt](1707.05589_note.txt)). This is a single-model result without dynamic evaluation, cache/pointer, ensemble, or fine-tuning. The paper explicitly avoids techniques that are known to push perplexities lower, because its goal is a controlled architecture comparison ([1707.05589_note.txt](1707.05589_note.txt)). Its listed baselines include Medium LSTM 82.7, Large LSTM 78.4, VD LSTM variants 73.2–69.0, VD RHN 65.4, NAS 64.0 and 62.4, and AWD-LSTM 57.3; the paper’s 58.3 outperforms all except AWD-LSTM at 57.3 ([1707.05589_note.txt](1707.05589_note.txt)).

### 4. Neural Architecture Search (1611.01578) — 62.4

The Neural Architecture Search paper reports 62.4 test perplexity for the best NAS model, described as NAS with base 8 and shared embeddings, 54M parameters ([1611.01578_note.txt](1611.01578_note.txt)). Other NAS configurations reach 64.0 and 67.9 ([1611.01578_note.txt](1611.01578_note.txt)). These are single-model PTB test perplexities without dynamic evaluation, cache/pointer, ensemble, or fine-tuning. The paper’s best listed baseline is Zilly et al. 2016 Variational RHN with shared embeddings at 66.0, so the 62.4 result is 3.6 perplexity better than that baseline ([1611.01578_note.txt](1611.01578_note.txt)).

### 5. Variational RHN + WT (1607.03474) — 65.4

“Recurrent Highway Networks” reports a best PTB word-level test perplexity of 65.4 for Variational RHN + WT ([1607.03474_note.txt](1607.03474_note.txt)). The model uses variational dropout and weight tying, and the table entry lists 23M parameters with validation/test perplexity 67.9/65.4 ([1607.03474_note.txt](1607.03474_note.txt)). The paper also reports 68.5 for Variational RHN without weight tying ([1607.03474_note.txt](1607.03474_note.txt)). Dynamic evaluation, cache/pointer, ensemble, and fine-tuning are not reported for the proposed model; cache and pointer methods appear only as baselines ([1607.03474_note.txt](1607.03474_note.txt)). The paper states that RHNs outperform most single models as well as all previous ensembles ([1607.03474_note.txt](1607.03474_note.txt)).

### 6. VD-RHN + RE (1611.01462) — 66.0

“Tying Word Vectors and Word Classifiers: A Loss Framework for Language Modeling” reports that VD-RHN+RE, trained with reused embeddings, achieves validation perplexity 68.1 and test perplexity 66.0 on PTB ([1611.01462_note.txt](1611.01462_note.txt)). The note describes this as the best overall result in that paper. The same paper lists cache/pointer or ensemble baselines such as RNN+LDA+KN-5+Cache at 92.0, Pointer Sentinel-LSTM (medium) at 70.9, 38 Large LSTMs at 68.7, and 10 Large VD-LSTMs at 68.7 ([1611.01462_note.txt](1611.01462_note.txt)). Because 66.0 does not use dynamic evaluation, cache/pointer, or ensemble, it is eligible for the ranking.

### 7. Variational LSTM (1512.05287) — 73.4

The Variational LSTM paper reports 73.4 test perplexity for the large Variational LSTM with untied weights and MC dropout at test time ([1512.05287_note.txt](1512.05287_note.txt)). The paper states that test perplexity is reduced from 78.4 to 73.4 with MC dropout and untied weights, and claims this is the best single-model perplexity on PTB at the time ([1512.05287_note.txt](1512.05287_note.txt)). The paper’s table also lists Variational tied weights MC at 74.1, Variational untied weights without MC at 75.2, and several higher baselines ([1512.05287_note.txt](1512.05287_note.txt)). No dynamic evaluation, cache/pointer, or fine-tuning is reported for the 73.4 result ([1512.05287_note.txt](1512.05287_note.txt)). The paper does report an ensemble result of 68.7 using 10 Variational LSTMs with MC dropout, but ensembles are excluded from this ranking ([1512.05287_note.txt](1512.05287_note.txt)).

### 8. Large NNLM + Weight Tying (1608.05859) — 74.3

“Using the Output Embedding to Improve Language Models” reports a large NNLM with weight tying reaching 74.3 test perplexity ([1608.05859_note.txt](1608.05859_note.txt)). The small NNLM with weight tying and projection regularization reaches 100.9 ([1608.05859_note.txt](1608.05859_note.txt)). Both are single-model results without dynamic evaluation, cache/pointer, ensemble, or fine-tuning ([1608.05859_note.txt](1608.05859_note.txt)). The paper’s baselines include the large NNLM of Zaremba et al. (2014) at 78.4 and the small NNLM at 114.5, so the weight-tied large model improves on the large baseline ([1608.05859_note.txt](1608.05859_note.txt)).

### 9. Large Regularized LSTM (1409.2329) — 78.4

The regularized LSTM paper reports a large regularized LSTM at 78.4 test perplexity and a medium regularized LSTM at 82.7 ([1409.2329_note.txt](1409.2329_note.txt)). These are single-model results without dynamic evaluation, cache/pointer, or fine-tuning ([1409.2329_note.txt](1409.2329_note.txt)). The paper also reports model-averaging results: 2 medium regularized LSTMs at 77.0, 5 medium at 73.3, 10 medium at 72.0, 2 large at 73.6, 10 large at 69.5, and 38 large at 68.7 ([1409.2329_note.txt](1409.2329_note.txt)). All model-averaging results are excluded because they are ensembles. The single large regularized LSTM at 78.4 is lower than the listed single-model baselines Pascanu et al. 2013 at 107.5, Cheng et al. at 100.0, and a non-regularized LSTM at 114.5 ([1409.2329_note.txt](1409.2329_note.txt)).

### 10. LSTM-Char-Large (1508.06615) — 78.9

“Character-Aware Neural Language Models” reports LSTM-Char-Large at 78.9 and LSTM-Char-Small at 92.3 for word-level PTB test perplexity ([1508.06615_note.txt](1508.06615_note.txt)). These are single-model results. The paper explicitly excludes ensembles, stating that lower perplexities have been reported with model ensembles but that they are not comparable to the current work ([1508.06615_note.txt](1508.06615_note.txt)). No dynamic evaluation, cache/pointer, or fine-tuning PTB results appear ([1508.06615_note.txt](1508.06615_note.txt)).

### 11. GRURNTN (1706.02222) — 87.38

The GRURNTN and LSTMRNTN paper reports word-level PTB test perplexity 87.38 for GRURNTN and 96.97 for LSTMRNTN ([1706.02222_note.txt](1706.02222_note.txt)). These are individual models. The paper states that baseline and proposed model experiments did not use dynamic evaluation ([1706.02222_note.txt](1706.02222_note.txt)). No cache/pointer, ensemble, or fine-tuning setting is reported for the proposed word-level results ([1706.02222_note.txt](1706.02222_note.txt)). GRURNTN improves over its GRURNN baseline of 97.78, a 10.4 absolute and 10.63% relative reduction ([1706.02222_note.txt](1706.02222_note.txt)).

## Discussion

The ranking in Table 1 shows a clear winner under the stated criteria. According to the primary paper text, AWD-LSTM reaches 57.3 without cache/pointer, and AWD-LSTM-MoS reaches 54.44 with fine-tuning and 55.97 without fine-tuning, both without dynamic evaluation or cache/pointer ([1711.03953_note.txt](1711.03953_note.txt); [1708.02182.txt](1708.02182.txt)). Therefore, the lowest eligible word-level PTB test perplexity is 54.44, reported by “Breaking the Softmax Bottleneck: A High-Rank RNN Language Model” for AWD-LSTM-MoS with fine-tuning ([1711.03953_note.txt](1711.03953_note.txt)).

Two caveats deserve emphasis. First, if one accepts the 53.3 figure from the AWD-LSTM note ([1708.02182_note.txt](1708.02182_note.txt)), then AWD-LSTM would take the top spot at 53.3. However, the primary paper text reports 57.3 in the abstract and Table 1, and 58.8 without fine-tuning in Table 4 ([1708.02182.txt](1708.02182.txt)). The weight of evidence favors 57.3. Second, if fine-tuning were excluded from consideration, AWD-LSTM-MoS without fine-tuning still achieves 55.97, which remains lower than the next eligible results at 57.3 and 58.3 ([1711.03953_note.txt](1711.03953_note.txt); [1708.02182.txt](1708.02182.txt); [1707.05589_note.txt](1707.05589_note.txt)). Thus, the identity of the winning paper is robust to the fine-tuning question, though the exact value changes from 54.44 to 55.97.

The gap between the top result and the rest is notable. The next best single models without dynamic/cache/pointer are AWD-LSTM at 57.3, Melis et al.’s 4-layer LSTM at 58.3, NAS at 62.4, Variational RHN + WT at 65.4, and VD-RHN+RE at 66.0 ([1708.02182.txt](1708.02182.txt); [1707.05589_note.txt](1707.05589_note.txt); [1611.01578_note.txt](1611.01578_note.txt); [1607.03474_note.txt](1607.03474_note.txt); [1611.01462_note.txt](1611.01462_note.txt)). Lower numbers exist in the provided sources but only with excluded techniques: AWD-LSTM + continuous cache pointer at 52.8 ([1708.02182.txt](1708.02182.txt)), AWD-LSTM + dynamic evaluation at 51.1 ([1711.03953.txt](1711.03953.txt)), and AWD-LSTM-MoS + dynamic evaluation at 47.69 ([1711.03953_note.txt](1711.03953_note.txt)). This confirms that the query’s exclusions significantly affect the outcome.

## Conclusion

Across the provided papers, the lowest word-level Penn Treebank test perplexity for a single model without dynamic evaluation, cache, or pointer augmentation is **54.44**, reported by **AWD-LSTM-MoS** in “Breaking the Softmax Bottleneck: A High-Rank RNN Language Model” ([1711.03953_note.txt](1711.03953_note.txt)). The ranking by this criterion is: 1711.03953 (54.44), 1708.02182 (57.3, with a note reporting 53.3), 1707.05589 (58.3), 1611.01578 (62.4), 1607.03474 (65.4), 1611.01462 (66.0), 1512.05287 (73.4), 1608.05859 (74.3), 1409.2329 (78.4), 1508.06615 (78.9), and 1706.02222 (87.38). If the AWD-LSTM note’s 53.3 were accepted over the primary paper text, AWD-LSTM would rank first; under the primary-source evidence, AWD-LSTM-MoS at 54.44 is the lowest eligible result.

## References

- 1409.2329_note.txt. (2014). Recurrent Neural Network Regularization. [Note]
- 1508.06615.txt. (2016). Character-Aware Neural Language Models.
- 1508.06615_note.txt. (2016). Character-Aware Neural Language Models. [Note]
- 1512.05287.txt. (2016). A Theoretically Grounded Application of Dropout in Recurrent Neural Networks.
- 1512.05287_note.txt. (2016). A Theoretically Grounded Application of Dropout in Recurrent Neural Networks. [Note]
- 1607.03474.txt. (2016). Recurrent Highway Networks.
- 1607.03474_note.txt. (2016). Recurrent Highway Networks. [Note]
- 1608.05859_note.txt. (2016). Using the Output Embedding to Improve Language Models. [Note]
- 1611.01462_note.txt. (2016). Tying Word Vectors and Word Classifiers: A Loss Framework for Language Modeling. [Note]
- 1611.01578_note.txt. (2016). Neural Architecture Search with Reinforcement Learning. [Note]
- 1706.02222_note.txt. (2017). Gated Recurrent Neural Tensor Network. [Note]
- 1707.05589_note.txt. (2017). On the State of the Art of Evaluation in Neural Language Models. [Note]
- 1708.02182.txt. (2017). Regularizing and Optimizing LSTM Language Models.
- 1708.02182_note.txt. (2017). Regularizing and Optimizing LSTM Language Models. [Note]
- 1711.03953.txt. (2017). Breaking the Softmax Bottleneck: A High-Rank RNN Language Model.
- 1711.03953_note.txt. (2017). Breaking the Softmax Bottleneck: A High-Rank RNN Language Model. [Note]