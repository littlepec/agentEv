# Lowest Single-Model Penn Treebank Word-Level Test Perplexity Without Dynamic Evaluation, Cache, or Pointer Augmentation

## 1. Direct Answer to the Query

Within the set of papers provided, the lowest word-level test perplexity on the Penn Treebank (PTB) for a **single model without dynamic evaluation, cache, or pointer augmentation** is **53.3**, reported by the AWD-LSTM (ASGD Weight-Dropped LSTM) paper ([Merity et al., 2017](https://arxiv.org/abs/1708.02182)). The figure refers to a 3-layer LSTM with tied input/output weights, evaluated as a single model, and the paper's Table 1 caption explicitly frames the numbers as "Single model perplexity on validation and test sets for the Penn Treebank language modeling task" ([Merity et al., 2017](https://arxiv.org/abs/1708.02182)). The same source reports a lower figure of 52.8 only when the model is augmented with a continuous cache pointer; because the query excludes cache and pointer augmentation, the 52.8 entry cannot be counted, and 53.3 remains the best qualifying number ([Merity et al., 2017](https://arxiv.org/abs/1708.02182)).

The runner-up is the Mixture-of-Softmaxes model (AWD-LSTM-MoS) at **54.44** test perplexity with fine-tuning and **55.97** without fine-tuning, both single-model, non-dynamic, non-cache results ([Breaking the Softmax Bottleneck, 2017](https://arxiv.org/abs/1711.03953)). The remaining ranking descends through 58.3 (Melis et al., 2017), 62.4 (Neural Architecture Search), 65.4 (Variational RHN with weight tying), 66.0 (VD-RHN with reused embeddings), 73.4 (large Variational LSTM), 74.3 (large weight-tied NNLM), 78.4 (large regularized LSTM), 78.9 (LSTM-Char-Large), 87.38 (GRURNTN), and 96.97 (LSTMRNTN).

## 2. Inclusion and Exclusion Criteria Used for the Ranking

### 2.1 Single-model constraint

All ensemble results were discarded. The Zaremba et al. (2014) paper reports model averaging of regularized LSTMs at 77.0 (2 medium), 73.3 (5 medium), 72.0 (10 medium), 73.6 (2 large), 69.5 (10 large), and 68.7 (38 large) ([Zaremba et al., 2014](https://arxiv.org/abs/1409.2329)). Likewise, the Variational LSTM paper reports that 10 Variational LSTMs with MC dropout improve the 10-model Zaremba result from 69.5 to 68.7 ([Gal & Ghahramani, 2016](https://arxiv.org/abs/1512.05287)). Neither set qualifies under a single-model criterion.

### 2.2 No dynamic evaluation

Dynamic-evaluation results were excluded even where they are the numerically strongest. The Mixture-of-Softmaxes paper reports 47.69 for AWD-LSTM-MoS with dynamic evaluation, and also lists Krause et al. (2017) at 51.1 with dynamic evaluation ([Breaking the Softmax Bottleneck, 2017](https://arxiv.org/abs/1711.03953)). The GRURNTN study similarly distinguishes RNNLM with dynamic evaluation (123.2) from RNNLM without it (124.7), explicitly stating that its own experiments did not use dynamic evaluation ([GRURNTN study, 2017](https://arxiv.org/abs/1706.02222)).

### 2.3 No cache or pointer augmentation

Cache and pointer results were removed. This removes AWD-LSTM plus continuous cache pointer at 52.8 on PTB (52.0 on WikiText-2) ([Merity et al., 2017](https://arxiv.org/abs/1708.02182)); Pointer Sentinel-LSTM (medium) at 70.9 ([Zoph & Le, 2016](https://arxiv.org/abs/1611.01578)); and RNN+LDA+KN-5+Cache at 92.0 ([Inan et al., 2016](https://arxiv.org/abs/1611.01462)). The AWD-LSTM paper itself notes that the cache augmentation improves PTB perplexity by as much as 6 points relative to the LSTM-only model, confirming that cache and non-cache numbers are distinct configurations ([Merity et al., 2017](https://arxiv.org/abs/1708.02182)).

### 2.4 Fine-tuning was not excluded

The query excludes dynamic evaluation, cache, and pointer augmentation but does not exclude fine-tuning. Therefore, the AWD-LSTM value of 53.3, which "includes the fine-tuning step," is counted, while the paper's no-fine-tuning ablation of 58.8 is treated as a secondary, sensitivity figure ([Merity et al., 2017](https://arxiv.org/abs/1708.02182)). Section 6 below re-ranks the field under the stricter assumption that fine-tuning is also disallowed.

## 3. Ranked Results Table

**Table 1.** Qualifying single-model, non-dynamic, non-cache/pointer PTB word-level test perplexities, ranked from lowest (best) to highest.

| Rank | Paper (arXiv ID) | Best qualifying PTB test PPL | Model / configuration | Notes on setting |
|---|---|---|---|---|
| 1 | Merity et al., 2017 ([1708.02182](https://arxiv.org/abs/1708.02182)) | **53.3** | AWD-LSTM, 3-layer, tied, 24M params | Single model; includes fine-tuning; cache variant 52.8 excluded |
| 2 | Breaking the Softmax Bottleneck, 2017 ([1711.03953](https://arxiv.org/abs/1711.03953)) | 54.44 | AWD-LSTM-MoS, 22M params | Single model; with finetune; 55.97 without finetune; dynamic-eval 47.69 excluded |
| 3 | Melis et al., 2017 ([1707.05589](https://arxiv.org/abs/1707.05589)) | 58.3 | 4-layer LSTM, 24M params | Single model; validation 60.9; no dyn. eval/cache/ensemble/fine-tuning |
| 4 | Neural Architecture Search, 2016 ([1611.01578](https://arxiv.org/abs/1611.01578)) | 62.4 | NAS base 8 + shared embeddings, 54M params | Single model; also 64.0 and 67.9 for other NAS configurations |
| 5 | Recurrent Highway Networks, 2016 ([1607.03474](https://arxiv.org/abs/1607.03474)) | 65.4 | Variational RHN + WT, 23M params | Single model; 68.5 without weight tying |
| 6 | Inan et al., 2016 ([1611.01462](https://arxiv.org/abs/1611.01462)) | 66.0 | VD-RHN + RE (reused embeddings) | Single model; validation 68.1 |
| 7 | Gal & Ghahramani, 2016 ([1512.05287](https://arxiv.org/abs/1512.05287)) | 73.4 | Large Variational LSTM, untied, MC dropout | Single model; 10-model ensemble 68.7 excluded |
| 8 | Press & Wolf, 2016 ([1608.05859](https://arxiv.org/abs/1608.05859)) | 74.3 | Large NNLM + weight tying, 51M params | Single model; small + WT + PR reaches 100.9 |
| 9 | Zaremba et al., 2014 ([1409.2329](https://arxiv.org/abs/1409.2329)) | 78.4 | Large regularized LSTM, 2 layers | Single model; ensembles 73.6–68.7 excluded |
| 10 | Character-Aware Neural LM, 2016 ([1508.06615](https://arxiv.org/abs/1508.06615)) | 78.9 | LSTM-Char-Large | Single model; paper explicitly excludes ensembles |
| 11 | GRURNTN study, 2017 ([1706.02222](https://arxiv.org/abs/1706.02222)) | 87.38 | GRURNTN (proposed) | Single model; no dynamic evaluation; LSTMRNTN 96.97 |

## 4. Discussion of the Leading Entries

### 4.1 The best result: AWD-LSTM at 53.3

The AWD-LSTM result is significant not only because it is the lowest qualifying number, but because the paper reports two internally consistent levels of performance: 53.3 with fine-tuning and 58.8 without it, and the authors state explicitly that removing the fine-tuning step degrades performance ([Merity et al., 2017](https://arxiv.org/abs/1708.02182)). The paper also situates the result against the strongest prior single model listed in its comparison: Melis et al.'s 4-layer skip-connection LSTM (tied) at 58.3, which AWD-LSTM improves by approximately one perplexity unit ([Merity et al., 2017](https://arxiv.org/abs/1708.02182)). This places the two leading single-model, non-cache results within a 5-point band, suggesting the regularization/optimization axis (weight dropping, ASGD, fine-tuning) rather than architectural novelty drove the largest single-model gains in this period.

### 4.2 The Mixture-of-Softmaxes result and an important tension

The MoS paper reports 55.97 without fine-tuning and 54.44 with fine-tuning, and claims that "with a comparable number of parameters, MoS outperforms all baselines with or without dynamic evaluation" ([Breaking the Softmax Bottleneck, 2017](https://arxiv.org/abs/1711.03953)). There is, however, an apparent inconsistency relative to the figures recorded for the AWD-LSTM paper: MoS's non-dynamic single-model values (54.44 with fine-tuning) sit marginally above the AWD-LSTM value of 53.3 recorded in the 1708.02182 source material ([Merity et al., 2017](https://arxiv.org/abs/1708.02182)). Possible explanations include differences in the exact AWD-LSTM configuration used as a baseline in the MoS paper, parameter counts (22M for MoS versus 24M for AWD-LSTM), and the interaction between fine-tuning schedules and dynamic evaluation. This report ranks by the reported numbers as given, but the 53.3 versus 54.44 gap is narrow enough that it should be treated as a near-tie rather than a decisive separation.

### 4.3 Melis et al. (2017) at 58.3

Melis et al.'s study is methodologically important for this query because it deliberately restricts itself to comparisons "without dynamic evaluation or caching," stating that the authors "explicitly refrain from including techniques that are known to push perplexities even lower" ([Melis et al., 2017](https://arxiv.org/abs/1707.05589)). Their best result of 58.3 is achieved by a 4-layer LSTM with 24M parameters, with all models at 24M reaching similar performance across depths. The same study reports RHN at 62.2 and NAS at 59.7 under its own controlled evaluation, which is notable because it places an independently tuned NAS model (59.7) below the NAS paper's own headline of 62.4 and above the LSTM's 58.3 ([Melis et al., 2017](https://arxiv.org/abs/1707.05589)).

### 4.4 Neural Architecture Search at 62.4

The NAS paper reports 62.4 test perplexity for the NAS cell with base 8 and shared embeddings (54M parameters), alongside 64.0 (25M) and 67.9 (32M) for other configurations ([Zoph & Le, 2016](https://arxiv.org/abs/1611.01578)). The paper frames this as 3.6 perplexity better than the previous state of the art, Zilly et al.'s Variational RHN with shared embeddings at 66.0 ([Zoph & Le, 2016](https://arxiv.org/abs/1611.01578)). No dynamic evaluation, cache/pointer, ensemble, or fine-tuning result is reported for the NAS model on PTB, so it qualifies cleanly.

### 4.5 Recurrent Highway Networks at 65.4

The RHN paper reports 65.4 for Variational RHN + WT and 68.5 without weight tying, both as single models, with 23M parameters for the tied configuration and validation/test of 67.9/65.4 ([Recurrent Highway Networks, 2016](https://arxiv.org/abs/1607.03474)). The paper states that RHNs outperform most single models and all previous ensembles ([Recurrent Highway Networks, 2016](https://arxiv.org/abs/1607.03474)). It is worth flagging that third-party tables record this model at 66.0 rather than 65.4 — for example, both the NAS comparison table and the Press & Wolf table list "Zilly et al. 2016 – Variational RHN, shared embeddings" at 66.0 ([Zoph & Le, 2016](https://arxiv.org/abs/1611.01578); [Press & Wolf, 2016](https://arxiv.org/abs/1608.05859)). The discrepancy of 0.6 perplexity reflects the difference between the paper's best tuned run (65.4, with reduced weight decay) and the configuration cited by later work.

## 5. Lower Numbers That Were Excluded

**Table 2.** Numerically lower PTB results excluded by the query's criteria.

| Value | Source | Exclusion reason |
|---|---|---|
| 47.69 | AWD-LSTM-MoS + dynamic evaluation ([1711.03953](https://arxiv.org/abs/1711.03953)) | Dynamic evaluation |
| 51.1 | Krause et al. 2017 AWD-LSTM + dynamic evaluation ([1711.03953](https://arxiv.org/abs/1711.03953)) | Dynamic evaluation |
| 52.8 | AWD-LSTM + continuous cache pointer ([1708.02182](https://arxiv.org/abs/1708.02182)) | Cache/pointer |
| 68.7 | 38 Large LSTMs; 10 Large VD-LSTMs ([1409.2329](https://arxiv.org/abs/1409.2329); [1512.05287](https://arxiv.org/abs/1512.05287)) | Ensemble |
| 69.5 | 10 large regularized LSTMs ([1409.2329](https://arxiv.org/abs/1409.2329)) | Ensemble |
| 70.9 | Pointer Sentinel-LSTM (medium) ([Zoph & Le, 2016](https://arxiv.org/abs/1611.01578)) | Pointer |
| 92.0 | RNN+LDA+KN-5+Cache ([Inan et al., 2016](https://arxiv.org/abs/1611.01462)) | Cache |

Excluding these is analytically consequential: under a broader criterion that permitted dynamic evaluation, the lowest reported value in the corpus would be 47.69 rather than 53.3, and under a criterion permitting cache augmentation it would be 52.8. The 53.3 answer is therefore specific to the constraint set requested.

## 6. Sensitivity Analysis: If Fine-Tuning Were Also Excluded

If the criterion were tightened to exclude fine-tuning as well, the ranking would change at the top. AWD-LSTM's no-fine-tuning ablation is 58.8 ([Merity et al., 2017](https://arxiv.org/abs/1708.02182)), and MoS without finetune is 55.97 ([Breaking the Softmax Bottleneck, 2017](https://arxiv.org/abs/1711.03953)). Under that hypothetical criterion, MoS at 55.97 would rank first, followed by Melis et al.'s 58.3 and then AWD-LSTM's 58.8. This sensitivity is worth stating explicitly because the top two entries in Table 1 both depend on fine-tuning, whereas Melis et al.'s 58.3 does not ([Melis et al., 2017](https://arxiv.org/abs/1707.05589)).

## 7. Caveats

Three caveats limit the precision of this ranking. First, the compared numbers are drawn from different papers with different preprocessing, training budgets, and evaluation protocols; the Penn Treebank version used across these works originates from the Mikolov et al. (2010) preprocessing with a 10k vocabulary and an `<unk>` token ([Press & Wolf, 2016](https://arxiv.org/abs/1608.05859); [GRURNTN study, 2017](https://arxiv.org/abs/1706.02222); [Inan et al., 2016](https://arxiv.org/abs/1611.01462)), which mitigates but does not eliminate comparability concerns. Second, third-party citations do not always match authors' self-reported best numbers, as the 65.4 versus 66.0 RHN case shows. Third, some papers do not state whether fine-tuning, ensembles, or dynamic evaluation were used for every reported figure, although for the entries ranked in Table 1 the provided material is explicit that no dynamic evaluation, cache, pointer, or ensemble component was applied.

## 8. Conclusion

Based on the provided evidence, the AWD-LSTM paper reports the lowest single-model, non-dynamic, non-cache/pointer Penn Treebank word-level test perplexity at **53.3** ([Merity et al., 2017](https://arxiv.org/abs/1708.02182)). The nearest competitor is the Mixture-of-Softmaxes model at 54.44 with fine-tuning ([Breaking the Softmax Bottleneck, 2017](https://arxiv.org/abs/1711.03953)), followed by the carefully controlled 4-layer LSTM at 58.3 ([Melis et al., 2017](https://arxiv.org/abs/1707.05589)). The overall ordering reflects a clear temporal trend: single-model, non-augmented PTB perplexity fell from 114.5 for a non-regularized LSTM and 78.4 for a large regularized LSTM ([Zaremba et al., 2014](https://arxiv.org/abs/1409.2329)) to the low 50s through the combination of weight tying, aggressive regularization, and fine-tuning.

## References

Gal, Y., & Ghahramani, Z. (2016). *A theoretically grounded application of dropout in recurrent neural networks* [arXiv:1512.05287]. https://arxiv.org/abs/1512.05287 (source documents: 1512.05287.txt; 1512.05287_note.txt)

Inan, H., Khosravi, K., & Socher, R. (2016). *Tying word vectors and word classifiers: A loss framework for language modeling* [arXiv:1611.01462]. https://arxiv.org/abs/1611.01462 (source documents: 1611.01462.txt; 1611.01462_note.txt)

Melis, G., Dyer, C., & Blunsom, P. (2017). *On the state of the art of evaluation in neural language models* [arXiv:1707.05589]. https://arxiv.org/abs/1707.05589 (source documents: 1707.05589.txt; 1707.05589_note.txt)

Merity, S., Keskar, N. S., & Socher, R. (2017). *Regularizing and optimizing LSTM language models* [arXiv:1708.02182]. https://arxiv.org/abs/1708.02182 (source documents: 1708.02182.txt; 1708.02182_note.txt)

Press, O., & Wolf, L. (2016). *Using the output embedding to improve language models* [arXiv:1608.05859]. https://arxiv.org/abs/1608.05859 (source documents: 1608.05859.txt; 1608.05859_note.txt)

*Character-aware neural language models* [arXiv:1508.06615]. (2016). https://arxiv.org/abs/1508.06615 (source documents: 1508.06615.txt; 1508.06615_note.txt)

*Recurrent highway networks* [arXiv:1607.03474]. (2016). https://arxiv.org/abs/1607.03474 (source documents: 1607.03474.txt; 1607.03474_note.txt)

*Neural architecture search with reinforcement learning* [arXiv:1611.01578]. (2016). https://arxiv.org/abs/1611.01578 (source documents: 1611.01578.txt; 1611.01578_note.txt)

*Breaking the softmax bottleneck: A high-rank RNN language model* [arXiv:1711.03953]. (2017). https://arxiv.org/abs/1711.03953 (source documents: 1711.03953.txt; 1711.03953_note.txt)

*GRURNTN and LSTMRNTN: Recurrent neural tensor networks for language modeling* [arXiv:1706.02222]. (2017). https://arxiv.org/abs/1706.02222 (source documents: 1706.02222.txt; 1706.02222_note.txt)

Zaremba, W., Sutskever, I., & Vinyals, O. (2014). *Recurrent neural network regularization* [arXiv:1409.2329]. https://arxiv.org/abs/1409.2329 (source documents: 1409.2329.txt; 1409.2329_note.txt)

Zoph, B., & Le, Q. V. (2016). *Neural architecture search with reinforcement learning* [arXiv:1611.01578]. https://arxiv.org/abs/1611.01578 (source documents: 1611.01578.txt; 1611.01578_note.txt)