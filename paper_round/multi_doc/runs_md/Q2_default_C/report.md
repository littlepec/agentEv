# Word-Level Penn Treebank Test Perplexity of Proposed Single Models: A Comparative Extraction

## Introduction

The Penn Treebank (PTB) word-level language modeling benchmark is a standard evaluation for neural language models. Reported test perplexity is only directly comparable when the evaluation setting is held constant: single model, no dynamic evaluation, no cache/pointer mechanisms, no ensembles, and no fine-tuning. This report extracts the best single-model PTB test perplexity reported by each provided paper for its own proposed model. The sources are the supplied notes and text excerpts for nine arXiv papers. Where a paper reports ensembles, model averaging, or other non-single-model enhancements, those results are excluded. Where the source does not supply a title, the arXiv identifier is used.

## Methodology

For each paper, I identified the proposed model and selected the lowest reported word-level PTB test perplexity that satisfies the single-model restriction. I excluded: (a) ensembles and model averaging, (b) dynamic evaluation, (c) cache/pointer methods, (d) fine-tuning, and (e) any result that the paper itself identifies as a baseline or third-party model. The selection is based solely on the provided information. Some notes contain multiple configurations; the best single-model result is taken. For arXiv:1611.01462, the table extraction is partial and the best proposed test number is inferred from the available rows; this caveat is noted.

## Summary Table

| Rank | Paper Title / arXiv ID | Proposed Model | Best Single-Model Word-Level PTB Test Perplexity | Source |
|------|------------------------|----------------|--------------------------------------------------|--------|
| 1 | arXiv:1707.05589 (title not provided) | 4-layer 24M LSTM | 58.3 | ([1707.05589_note.txt](https://arxiv.org/abs/1707.05589)) |
| 2 | Neural Architecture Search with Reinforcement Learning (arXiv:1611.01578) | NAS with base 8 and shared embeddings | 62.4 | ([1611.01578_note.txt](https://arxiv.org/abs/1611.01578)) |
| 3 | Recurrent Highway Networks (arXiv:1607.03474) | Variational RHN + WT | 65.4 | ([1607.03474_note.txt](https://arxiv.org/abs/1607.03474)) |
| 4 | A Theoretically Grounded Application of Dropout in Recurrent Neural Networks (arXiv:1512.05287) | Variational LSTM (large, untied, MC) | 73.4 | ([1512.05287_note.txt](https://arxiv.org/abs/1512.05287)) |
| 5 | Using the Output Embedding to Improve Language Models (arXiv:1608.05859) | Large NNLM + Weight Tying | 74.3 | ([1608.05859_note.txt](https://arxiv.org/abs/1608.05859)) |
| 6 | Recurrent Neural Network Regularization (arXiv:1409.2329) | Large regularized LSTM | 78.4 | ([1409.2329_note.txt](https://arxiv.org/abs/1409.2329)) |
| 7 | Character-Aware Neural Language Models (arXiv:1508.06615) | LSTM-Char-Large | 78.9 | ([1508.06615_note.txt](https://arxiv.org/abs/1508.06615)) |
| 8 | arXiv:1706.02222 (title not provided) | GRURNTN | 87.38 | ([1706.02222_note.txt](https://arxiv.org/abs/1706.02222)) |
| 9 | arXiv:1611.01462 (title not provided) | VD-LSTM+REAL | 138.4 (see caveat) | ([1611.01462.txt](https://arxiv.org/abs/1611.01462)) |

## Detailed Paper-by-Paper Analysis

### arXiv:1707.05589: 4-Layer 24M LSTM (58.3)

The paper reports its own best model at 58.3 test perplexity on PTB. The note states that this 4-layer 24M LSTM outperforms all listed baselines except AWD-LSTM at 57.3, which is described as a parallel work and slightly better ([1707.05589_note.txt](https://arxiv.org/abs/1707.05589)). The listed baselines include Medium LSTM 82.7, Large LSTM 78.4, VD LSTM (Press & Wolf) 73.2, VD LSTM (Inan et al., 9M) 73.9, VD LSTM (Inan et al., 28M) 69.0, VD RHN 65.4, NAS (25M) 64.0, NAS (54M) 62.4, and AWD-LSTM 57.3. The paper does not report dynamic evaluation, cache/pointer, ensemble, or fine-tuning for its own model; all reported results are single-model. Therefore, the best single-model result for the paper's own proposed model is 58.3. AWD-LSTM's 57.3 is excluded because it is a baseline/parallel work, not the paper's own model.

### arXiv:1611.01578: Neural Architecture Search (62.4)

The paper reports 62.4 test perplexity on PTB for the best Neural Architecture Search (NAS) model ([1611.01578_note.txt](https://arxiv.org/abs/1611.01578)). This result is NAS with base 8 and shared embeddings, using 54M parameters. The paper also reports 64.0 and 67.9 for other NAS configurations: NAS with base 8 and shared embeddings at 64.0 with 25M parameters, and NAS with base 8 at 67.9 with 32M parameters. These are single-model test perplexities. The best listed baseline is Zilly et al. 2016 Variational RHN with shared embeddings at 66.0 test perplexity and 24M parameters. The NAS result of 62.4 is 3.6 perplexity better than that baseline. The note explicitly states that no dynamic evaluation, cache/pointer, ensemble, or fine-tuning result is reported for the NAS model on PTB. Thus, the best single-model result is 62.4.

### arXiv:1607.03474: Recurrent Highway Networks (65.4)

The paper reports its best PTB word-level test perplexity for the proposed model as 65.4 for Variational RHN + WT ([1607.03474_note.txt](https://arxiv.org/abs/1607.03474)). It also reports 68.5 test perplexity for Variational RHN without WT. The best 10-layer model with reduced weight decay improves to 67.9/65.4 validation/test perplexity. Table 1 lists Variational RHN + WT as 23M parameters with validation/test perplexity 67.9/65.4. This setting uses variational dropout and weight tying of input and output mappings. The paper reports both with and without weight tying for fair comparisons. The best PTB result is a single model. Dynamic evaluation, cache/pointer, ensemble, and fine-tuning are not reported for the proposed model. Cache and pointer methods appear only as baselines, and ensembles are mentioned only in comparison. The paper states that RHNs outperform most single models as well as all previous ensembles. The best single-model result is therefore 65.4. Note that a later paper (arXiv:1611.01578) cites a Zilly et al. 2016 Variational RHN with shared embeddings at 66.0; this is a different citation context and does not change the paper's own reported best of 65.4.

### arXiv:1512.05287: Variational LSTM (73.4)

The paper reports 73.4 test perplexity for the proposed Variational LSTM on PTB ([1512.05287_note.txt](https://arxiv.org/abs/1512.05287)). The paper states that test perplexity is reduced from 78.4 down to 73.4 with MC dropout and untied weights. This 73.4 result is a single-model result for the large Variational LSTM with untied weights and MC dropout at test time. The paper claims that to the best of its knowledge these are the best single-model perplexities on PTB. The paper text does not report dynamic evaluation, cache/pointer, or fine-tuning for the PTB result. The table caption identifies the results as single-model perplexity on test and validation sets. The paper also reports an ensemble result: using 10 Variational LSTMs with MC dropout improves Zaremba et al.'s test set perplexity from 69.5 to 68.7, obtaining identical perplexity to Zaremba et al.'s experiment with 38 models. This ensemble result is excluded from the single-model extraction. Thus, the best single-model result is 73.4.

### arXiv:1608.05859: Using the Output Embedding to Improve Language Models (74.3)

The paper reports word-level PTB test perplexity for its proposed weight-tied neural network language models in single-model settings ([1608.05859_note.txt](https://arxiv.org/abs/1608.05859)). The large NNLM with weight tying (Large + Weight Tying) reaches 74.3 test perplexity. The small NNLM with weight tying and projection regularization (Small + WT + PR) reaches 100.9 test perplexity. Both numbers come from the paper's neural network language model experiments and are reported without dynamic evaluation, cache/pointer, ensemble, or fine-tuning. The paper's comparison baselines include the large NNLM of Zaremba et al. (2014) at 78.4 and the small NNLM at 114.5. The proposed large weight-tied model improves on the large baseline, and the proposed small weight-tied plus projection-regularized model improves on the small baseline. The paper also lists non-dropout baselines: KN 5-gram 141, RNN 123, LSTM 117, Stack RNN 110, FOFE-FNN 108, Noisy LSTM 108.0, and Deep RNN 107.5. The best proposed single-model result is 74.3.

### arXiv:1409.2329: Recurrent Neural Network Regularization (78.4)

The paper reports model averaging of regularized LSTMs ([1409.2329_note.txt](https://arxiv.org/abs/1409.2329)). It lists 2 medium regularized LSTMs at 77.0, 5 medium at 73.3, 10 medium at 72.0, 2 large at 73.6, 10 large at 69.5, and 38 large at 68.7. These are ensemble/model-averaging results and are excluded. The paper lists single-model baseline PTB word-level test perplexities: Pascanu et al. 2013 at 107.5, Cheng et al. at 100.0, and a non-regularized LSTM at 114.5. The proposed medium regularized LSTM at 82.7 and large regularized LSTM at 78.4 are lower, meaning better, than all listed single-model baselines. The paper does not report dynamic evaluation, cache/pointer, or fine-tuning settings for PTB perplexity. Therefore, the best single-model result for the paper's own proposed model is the large regularized LSTM at 78.4.

### arXiv:1508.06615: Character-Aware Neural Language Models (78.9)

The paper reports word-level PTB test perplexity for the proposed character-aware LSTM language model ([1508.06615_note.txt](https://arxiv.org/abs/1508.06615)). LSTM-Char-Large attains 78.9; LSTM-Char-Small attains 92.3. Predictions are made at the word level. These are single-model results. The paper excludes ensembles: "While lower perplexities have been reported with model ensembles [2012], we do not include them here as they are not comparable to the current work." No dynamic evaluation, cache/pointer, or fine-tuning PTB results appear. The best single-model result is 78.9.

### arXiv:1706.02222: GRURNTN (87.38)

The paper reports that both proposed models outperform their baselines ([1706.02222_note.txt](https://arxiv.org/abs/1706.02222)). GRURNTN reduces perplexity from 97.78 to 87.38 over GRURNN, a 10.4 absolute and 10.63% relative reduction. LSTMRNTN reduces perplexity from 108.26 to 96.97 over LSTMRNN, an 11.29 absolute and 10.42% relative reduction. The paper states that GRURNTN outperforms all baseline models and the other listed models by a large margin. LSTMRNTN improves the LSTMRNN model and its performance closely resembles the baseline GRURNN. The GRURNTN result is the strongest proposed word-level PTB perplexity in the table. The note does not report dynamic evaluation, cache/pointer, ensemble, or fine-tuning for these results. Therefore, the best single-model result for the paper's own proposed model is 87.38.

### arXiv:1611.01462: VD-LSTM+REAL (138.4, with caveat)

The provided note for this paper is partial and does not supply a title ([1611.01462.txt](https://arxiv.org/abs/1611.01462)). It lists several proposed VD-LSTM variants with four numbers each: (200 units) VD-LSTM 159.1, 148.0, 163.19, 148.6; VD-LSTM+AL 153.0, 142.5, 156.4, 143.7; VD-LSTM+RE 152.4, 141.9, 152.5, 140.9; and VD-LSTM+REAL 149.3, 140.6, 150.5, 138.4. The caption for Table 3 describes a comparison of the work to previous state of the art on word-level validation and test perplexities on the PTB corpus. The table then lists baselines including RNN (Mikolov & Zweig) 124.7, Deep RNN (Pascanu et al. 2013a) 107.5, LSTM medium (Zaremba et al. 2014) 82.7, CharCNN (Kim et al. 2015) 78.9, LSTM large (Zaremba et al. 2014) 78.4, and VD-LSTM (large, untied, MC) (Gal 2015) 73.4. Because the note does not give column headers for the first block, the exact mapping of the four numbers per row is ambiguous. However, the lowest test perplexity among the proposed VD-LSTM variants is 138.4 (VD-LSTM+REAL). If the first two numbers per row are the primary validation/test pair, the best test value would be 140.6; if the last two are the primary validation/test pair, or if the best among all provided test values is taken, the value is 138.4. Given the instruction to extract the best single-model result from the provided information, 138.4 is the strongest candidate. This value is much higher than the baselines in the same note, which suggests the table may correspond to a smaller-scale setup or that the note is incomplete. No dynamic evaluation, cache/pointer, ensemble, or fine-tuning is reported for this model in the provided note. The caveat is important for interpretation.

## Discussion and Comparability

The extracted results span a wide range. The lowest (best) perplexity is 58.3 from arXiv:1707.05589, followed by 62.4 from NAS (arXiv:1611.01578) and 65.4 from Variational RHN (arXiv:1607.03474). The middle group includes 73.4 from Variational LSTM (arXiv:1512.05287), 74.3 from weight-tied NNLM (arXiv:1608.05859), 78.4 from large regularized LSTM (arXiv:1409.2329), and 78.9 from character-aware LSTM (arXiv:1508.06615). The higher values are 87.38 from GRURNTN (arXiv:1706.02222) and 138.4 from the partially extracted VD-LSTM+REAL (arXiv:1611.01462). These differences reflect not only model quality but also differences in model size, regularization, training data preprocessing, and whether the paper is reporting a small-scale experiment or a state-of-the-art result.

The exclusion criteria matter. For arXiv:1512.05287, the ensemble result of 68.7 is excluded; for arXiv:1409.2329, the model-averaging results as low as 68.7 are excluded. For arXiv:1508.06615, the paper explicitly excludes ensembles. For arXiv:1607.03474, the paper reports no ensemble for its proposed model but mentions ensembles only in comparison. For arXiv:1611.01578, no dynamic evaluation or ensembling is reported. For arXiv:1707.05589, the paper's own model is single-model, and the AWD-LSTM result is a parallel work. For arXiv:1706.02222, the note does not mention any excluded technique. For arXiv:1611.01462, no excluded technique is mentioned in the provided note.

## Conclusion

Based on the provided information, the best single-model word-level PTB test perplexities reported by the papers for their own proposed models are: 58.3 (arXiv:1707.05589), 62.4 (arXiv:1611.01578), 65.4 (arXiv:1607.03474), 73.4 (arXiv:1512.05287), 74.3 (arXiv:1608.05859), 78.4 (arXiv:1409.2329), 78.9 (arXiv:1508.06615), 87.38 (arXiv:1706.02222), and 138.4 (arXiv:1611.01462, with caveat). These figures are extracted under the strict condition of single-model evaluation without dynamic evaluation or cache. The table above provides the direct comparison requested.

## References

- 1409.2329_note.txt. (n.d.). Recurrent Neural Network Regularization. https://arxiv.org/abs/1409.2329
- 1508.06615_note.txt. (n.d.). Character-Aware Neural Language Models. https://arxiv.org/abs/1508.06615
- 1512.05287_note.txt. (n.d.). A Theoretically Grounded Application of Dropout in Recurrent Neural Networks. https://arxiv.org/abs/1512.05287
- 1607.03474_note.txt. (n.d.). Recurrent Highway Networks. https://arxiv.org/abs/1607.03474
- 1608.05859_note.txt. (n.d.). Using the Output Embedding to Improve Language Models. https://arxiv.org/abs/1608.05859
- 1611.01462.txt. (n.d.). [Title not provided in source]. https://arxiv.org/abs/1611.01462
- 1611.01578_note.txt. (n.d.). Neural Architecture Search with Reinforcement Learning. https://arxiv.org/abs/1611.01578
- 1706.02222_note.txt. (n.d.). [Title not provided in source]. https://arxiv.org/abs/1706.02222
- 1707.05589_note.txt. (n.d.). [Title not provided in source]. https://arxiv.org/abs/1707.05589