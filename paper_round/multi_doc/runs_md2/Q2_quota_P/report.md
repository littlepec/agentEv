# Word-Level Penn Treebank Test Perplexity of Proposed Single Models: A Compilation of Eleven Papers

## 1. Scope, Inclusion Criteria, and Method

This report answers a narrowly defined question: for each of the eleven papers represented in the supplied corpus, what word-level Penn Treebank (PTB) test perplexity does the paper report for **its own proposed model**, using the **best single-model configuration that does not rely on dynamic evaluation or a cache/pointer mechanism**?

The evidence base consists of two document types: excerpts from the papers themselves (the `.txt` files) and third-party research notes (the `_note.txt` files). All PTB evaluations discussed here are word-level and, unless stated otherwise, follow the standard preprocessing of Mikolov et al. (2010), with training on sections 0–20, validation on sections 21–22, and test on sections 23–24, a vocabulary capped at the 10,000 most frequent words, and out-of-vocabulary items mapped to `<unk>` ([1508.06615.txt](1508.06615.txt); [1706.02222.txt](1706.02222.txt); [1611.01462.txt](1611.01462.txt)). Perplexity (PPL) is computed on the test set and lower values are better ([1508.06615.txt](1508.06615.txt)).

Five inclusion rules were applied consistently:

1. **Own proposed model only.** Baselines reported in the same papers (for example, the non-regularized LSTM at 114.5 in [1409.2329_note.txt](1409.2329_note.txt), or the N-gram model at 141 in [1706.02222_note.txt](1706.02222_note.txt)) are excluded from the headline figures.
2. **Word-level PTB test perplexity.** Character-level bits-per-character results (for example, 1.33 BPC for GRURNTN in [1706.02222_note.txt](1706.02222_note.txt)) are outside the query's scope.
3. **Single-model results.** Model-averaging and ensembling are excluded. This removes the regularized-LSTM averages of 2/5/10/38 models at 77.0/73.3/72.0/73.6/69.5/68.7 ([1409.2329_note.txt](1409.2329_note.txt)) and the 10-model Variational LSTM result of 68.7, which the paper itself notes "obtain[s] identical perplexity to Zaremba et al.'s experiment with 38 models" ([1512.05287_note.txt](1512.05287_note.txt)).
4. **No dynamic evaluation and no cache/pointer.** This excludes, for example, the 47.69 of AWD-LSTM-MoS with dynamic evaluation ([1711.03953_note.txt](1711.03953_note.txt)), the 52.8 of AWD-LSTM with a continuous cache pointer ([1708.02182_note.txt](1708.02182_note.txt)), and the RNNLM-with-dynamic-evaluation baseline of 123.2 ([1706.02222_note.txt](1706.02222_note.txt)).
5. **Fine-tuning is retained.** The query excludes only dynamic evaluation and cache mechanisms, so configurations that include a fine-tuning step—AWD-LSTM and AWD-LSTM-MoS—remain eligible.

## 2. Summary Table

| # | Paper | Own proposed model | Best single-model PTB word-level test PPL (no dynamic eval, no cache) | Other single-model figures reported by the paper |
|---|---|---|---|---|
| 1 | Recurrent Neural Network Regularization ([1409.2329_note.txt](1409.2329_note.txt)) | Large regularized LSTM | **78.4** | Medium regularized LSTM 82.7; non-regularized LSTM 114.5 |
| 2 | Character-Aware Neural Language Models ([1508.06615_note.txt](1508.06615_note.txt)) | LSTM-Char-Large | **78.9** | LSTM-Char-Small 92.3 |
| 3 | A Theoretically Grounded Application of Dropout in RNNs (Variational LSTM) ([1512.05287_note.txt](1512.05287_note.txt)) | Large Variational LSTM, MC dropout, untied weights | **73.4** | Validation 77.3 with weight tying / 77.9 untied |
| 4 | Recurrent Highway Networks ([1607.03474_note.txt](1607.03474_note.txt)) | Variational RHN + WT | **65.4** | Variational RHN without WT 68.5 |
| 5 | Using the Output Embedding to Improve Language Models ([1608.05859_note.txt](1608.05859_note.txt)) | Large NNLM + weight tying | **74.3** | Small + WT + PR 100.9; Large + BD + WT 73.2 |
| 6 | Tying Word Vectors and Word Classifiers ([1611.01462.txt](1611.01462.txt); [1611.01578.txt](1611.01578.txt)) | VD-LSTM + REAL (large, 51M) | **68.5** | Small (200-unit) variants in the 138–163 range |
| 7 | Neural Architecture Search with Reinforcement Learning ([1611.01578_note.txt](1611.01578_note.txt)) | NAS with base 8 + shared embeddings (54M) | **62.4** | 64.0 (25M); 67.9 (32M) |
| 8 | Gated Recurrent Neural Tensor Network ([1706.02222_note.txt](1706.02222_note.txt)) | GRURNTN | **87.38** | LSTMRNTN 96.97 |
| 9 | On the State of the Art of Evaluation in Neural Language Models ([1707.05589_note.txt](1707.05589_note.txt)) | 4-layer LSTM, 24M parameters | **58.3** | RHN 62.2; NAS 59.7 (in its table) |
| 10 | Regularizing and Optimizing LSTM Language Models ([1708.02182.txt](1708.02182.txt); [1708.02182_note.txt](1708.02182_note.txt)) | AWD-LSTM, 3-layer LSTM (tied) | **57.3** (paper Table 1); 53.3 claimed with fine-tuning | No-fine-tuning ablation 58.8; with cache 52.8 (excluded) |
| 11 | Breaking the Softmax Bottleneck ([1711.03953_note.txt](1711.03953_note.txt)) | AWD-LSTM-MoS (with finetune) | **54.44** | 55.97 without finetune; 47.69 with dynamic evaluation (excluded) |

## 3. Findings by Paper

### 3.1 Recurrent Neural Network Regularization — 78.4

The paper trains two-layer regularized LSTMs of medium and large size on PTB. The medium regularized LSTM reaches 82.7 and the large regularized LSTM reaches 78.4 test perplexity; both are lower (better) than every listed single-model baseline, including Pascanu et al. (2013) at 107.5, Cheng et al. at 100.0, and the non-regularized LSTM at 114.5 ([1409.2329_note.txt](1409.2329_note.txt)). The paper reports no dynamic evaluation, cache/pointer, or fine-tuning for PTB, and the model-averaged results (down to 68.7 with 38 models) are excluded by the stated criteria ([1409.2329_note.txt](1409.2329_note.txt)).

### 3.2 Character-Aware Neural Language Models — 78.9

The proposed character-aware LSTM makes predictions at the word level. LSTM-Char-Large attains 78.9 and LSTM-Char-Small 92.3 as single models; the authors explicitly state that ensembles are excluded because they are "not comparable to the current work" ([1508.06615_note.txt](1508.06615_note.txt)). The highway-layer ablations confirm the large two-highway configuration at 78.9 versus 84.6 without highway layers, and the small model at 90.1 with two highway layers ([1508.06615.txt](1508.06615.txt)). The paper frames this as achieving results "on par with the existing state-of-the-art on the Penn Treebank" with roughly 60% fewer parameters ([1508.06615.txt](1508.06615.txt)).

### 3.3 Variational LSTM (Theoretically Grounded Dropout) — 73.4

Test perplexity is reduced from 78.4 to 73.4 using MC dropout with untied weights, a single-model result for the large Variational LSTM; the validation perplexity improves from 82.2 to 77.3 with weight tying or 77.9 without ([1512.05287_note.txt](1512.05287_note.txt)). The paper asserts that these are, to the best of its knowledge, "the best single model perplexities on the Penn Treebank" ([1512.05287_note.txt](1512.05287_note.txt)). Table 1 identifies the results as single-model perplexity on validation and test sets ([1512.05287.txt](1512.05287.txt)). The 10-model ensemble (68.7) is excluded here ([1512.05287_note.txt](1512.05287_note.txt)).

### 3.4 Recurrent Highway Networks — 65.4

The best PTB word-level test perplexity reported for the proposed model is 65.4 for Variational RHN + WT, with 67.9 validation; the same architecture without weight tying reaches 68.5 ([1607.03474_note.txt](1607.03474_note.txt)). The setting uses variational dropout and weight tying of input and output mappings, with 23M parameters in the table ([1607.03474_note.txt](1607.03474_note.txt)). The best result is a single model; dynamic evaluation, cache/pointer, ensembles, and fine-tuning are not reported for the proposed model, and the paper states that RHNs outperform most single models as well as all previous ensembles ([1607.03474_note.txt](1607.03474_note.txt)).

### 3.5 Using the Output Embedding to Improve Language Models — 74.3

For its proposed weight-tied neural network language models, the paper reports 74.3 test perplexity for the Large NNLM with weight tying (51M parameters, 77.7 validation) and 100.9 for Small + WT + PR, both as single models without dynamic evaluation, cache/pointer, ensembles, or fine-tuning ([1608.05859_note.txt](1608.05859_note.txt)). The comparison context includes Zaremba et al.'s large model at 78.4 and small model at 114.5, plus non-dropout baselines: KN 5-gram 141, RNN 123, LSTM 117, Stack RNN 110, FOFE-FNN 108, Noisy LSTM 108.0, and Deep RNN 107.5 ([1608.05859_note.txt](1608.05859_note.txt)). The paper's own table also lists a "Large + BD + WT" configuration at 73.2, discussed in Section 5 ([1608.05859.txt](1608.05859.txt)).

### 3.6 Tying Word Vectors and Word Classifiers — 68.5

The large VD-LSTM + REAL model (51M parameters) is listed at 68.5 test perplexity in a comparison table explicitly captioned "Single model perplexity on the test set of the Penn Treebank language modeling task" ([1611.01578.txt](1611.01578.txt)). The paper's own excerpt reports small (200-unit) configurations whose numbers fall in the 138–163 range for VD-LSTM and its augmented-loss variants, with VD-LSTM+REAL lowest ([1611.01462.txt](1611.01462.txt)); the column structure of that small-model table is not fully recoverable from the excerpt, so the 68.5 large-model figure is the defensible headline value. The paper claims state-of-the-art PTB performance from tying the input embedding and output projection ([1611.01462.txt](1611.01462.txt)).

### 3.7 Neural Architecture Search with Reinforcement Learning — 62.4

The best result is 62.4 test perplexity for NAS with base 8 and shared embeddings (54M parameters), 3.6 perplexity better than the previous state of the art; other NAS configurations reach 64.0 (25M) and 67.9 (32M) ([1611.01578_note.txt](1611.01578_note.txt)). The comparison table's best baseline is Zilly et al. (2016) Variational RHN with shared embeddings at 66.0 and 24M parameters, alongside Zoneout + Variational LSTM (medium) at 80.6, Pointer Sentinel-LSTM (medium) at 70.9, and Inan et al.'s VD-LSTM + REAL (large) at 68.5 ([1611.01578.txt](1611.01578.txt)). No dynamic evaluation, cache/pointer, ensemble, or fine-tuning result is reported for the NAS model ([1611.01578_note.txt](1611.01578_note.txt)).

### 3.8 Gated Recurrent Neural Tensor Network — 87.38

For word-level PTB modeling, Table II reports 87.38 test perplexity for GRURNTN and 96.97 for LSTMRNTN as individual models; experiments did not use dynamic evaluation, and no cache/pointer, ensemble, or fine-tuning setting is reported ([1706.02222_note.txt](1706.02222_note.txt)). GRURNTN reduces perplexity by 10.4 absolute (10.63% relative) over its GRURNN baseline (97.78), and LSTMRNTN by 11.29 absolute (10.42% relative) over LSTMRNN (108.26) ([1706.02222_note.txt](1706.02222_note.txt)). Published baselines in the same table include N-Gram 141, RNNLM without/with dynamic evaluation at 124.7/123.2, SCRNN 115, sRNN 110.0, and DOT(S)-RNN 107.5 ([1706.02222.txt](1706.02222.txt)).

### 3.9 On the State of the Art of Evaluation in Neural Language Models — 58.3

The paper's best word-level PTB test perplexity is 58.3 for a 4-layer LSTM with 24M parameters (60.9 validation), reported as a single model without dynamic evaluation, cache/pointer, ensemble, or fine-tuning ([1707.05589_note.txt](1707.05589_note.txt)). Its table also reports RHN at 62.2 and NAS at 59.7 for the same evaluation protocol, with all results other than Zaremba's using shared input and output embeddings ([1707.05589.txt](1707.05589.txt)). The authors state they deliberately refrain from including techniques that push perplexities even lower, "because its aim is strictly to do better model comparisons for the architectures under study" ([1707.05589_note.txt](1707.05589_note.txt)).

### 3.10 Regularizing and Optimizing LSTM Language Models — 57.3 (with a 53.3 claim)

The paper proposes AWD-LSTM (ASGD Weight-Dropped LSTM). Its Table 1 is captioned as "Single model perplexity on validation and test sets for the Penn Treebank language modeling task" and lists AWD-LSTM as a 3-layer, tied LSTM with 24M parameters at 60.0 validation / 57.3 test, and the continuous-cache variant at 53.9/52.8 ([1708.02182.txt](1708.02182.txt)). A research note in the corpus instead attributes 53.3 PTB test perplexity to AWD-LSTM including the fine-tuning step, and reports a no-fine-tuning ablation at 58.8 ([1708.02182_note.txt](1708.02182_note.txt)). Because the cache variant (52.8) is excluded by the query's criteria, this paper's eligible figure is the non-cache AWD-LSTM value; the discrepancy between 57.3 and 53.3 is examined in Section 5. The note also records that AWD-LSTM's result beats the best listed baseline, Melis et al.'s 4-layer skip-connection LSTM (tied) at 58.3 ([1708.02182_note.txt](1708.02182_note.txt)).

### 3.11 Breaking the Softmax Bottleneck — 54.44

The proposed AWD-LSTM-MoS (Mixture of Softmaxes, 22M parameters) reaches 55.97 PTB test perplexity without finetuning and 54.44 with finetuning, both as single models without dynamic evaluation; with dynamic evaluation the same model reaches 47.69 ([1711.03953_note.txt](1711.03953_note.txt)). Table 1 lists the excluded dynamic-evaluation baselines AWD-LSTM + continuous cache pointer at 52.8 and AWD-LSTM + dynamic evaluation at 51.1 ([1711.03953.txt](1711.03953.txt)). The paper reports that MoS outperforms all baselines with or without dynamic evaluation, improving on the state of the art by up to 3.6 points ([1711.03953.txt](1711.03953.txt)).

## 4. Cross-Cutting Observations

Across the eleven papers, the eligible single-model frontier moves from 78.4 (2014) to 78.9 (2015), 73.4 (2015), 65.4 (2016), 62.4 (2016), 58.3 (2017), 57.3 (2017), and 54.44 (2017), with two clear outliers: the 74.3 weight-tied NNLM ([1608.05859_note.txt](1608.05859_note.txt)) and the 87.38 tensor-network model ([1706.02222_note.txt](1706.02222_note.txt)), which is a 2017 paper whose PTB numbers are well above the contemporaneous frontier because it compares against an older baseline suite.

Weight tying is the most consistent architectural theme in this corpus: it appears in the 65.4 RHN + WT versus 68.5 without WT ([1607.03474_note.txt](1607.03474_note.txt)), the 74.3 large weight-tied NNLM ([1608.05859_note.txt](1608.05859_note.txt)), the 68.5 VD-LSTM + REAL ([1611.01578.txt](1611.01578.txt)), the 62.4 NAS with shared embeddings ([1611.01578_note.txt](1611.01578_note.txt)), and the shared embeddings used throughout the 58.3 evaluation study ([1707.05589.txt](1707.05589.txt)). A second theme is that ensembles and dynamic evaluation, although excluded from the table above, are systematically stronger than any listed single model in the same papers, which is why the query's exclusion criteria materially change the ranking that would otherwise be obtained ([1409.2329_note.txt](1409.2329_note.txt); [1512.05287_note.txt](1512.05287_note.txt); [1711.03953_note.txt](1711.03953_note.txt)).

## 5. Discrepancies, Caveats, and Evidentiary Limits

Several figures in the corpus are contested or reported indirectly, and these should be weighed when using the table.

- **RHN: 65.4 versus 66.0.** The paper's note reports 65.4 as its best, obtained by reducing weight decay further, while independent comparison tables in other papers list "Variational RHN, shared embeddings" at 66.0 with 24M parameters ([1607.03474_note.txt](1607.03474_note.txt); [1608.05859.txt](1608.05859.txt); [1611.01578.txt](1611.01578.txt)). The table above uses the paper's own 65.4 and flags the alternative.
- **Variational LSTM: 73.4 versus 75.0.** The 73.4 figure corresponds to MC dropout at test time; a later table lists "Variational LSTM (Gal 2015)" at 75.0, which reflects the dropout-approximation rather than MC dropout ([1512.05287_note.txt](1512.05287_note.txt); [1607.03474.txt](1607.03474.txt)).
- **Press & Wolf: 74.3 versus 73.2.** The paper's own table includes "Large + BD + WT" at 73.2, which Zilly et al. attribute to "Variational LSTM + WT (Press & Wolf 2016)" ([1608.05859.txt](1608.05859.txt); [1607.03474.txt](1607.03474.txt)). Because that row combines weight tying with Bayesian dropout, it is reported here as a secondary configuration rather than the paper's clean proposed model.
- **AWD-LSTM: 57.3 versus 53.3.** The paper text's Table 1 gives 57.3 for AWD-LSTM and 52.8 only when the continuous cache pointer is added, which is excluded ([1708.02182.txt](1708.02182.txt)); the corpus note claims 53.3 including fine-tuning ([1708.02182_note.txt](1708.02182_note.txt)). No table in the supplied paper text corroborates 53.3, so 57.3 is treated as the primary value while 53.3 is disclosed. If 53.3 were accepted, AWD-LSTM would become the strongest eligible result in the set.
- **Inan et al.: indirect sourcing.** The 68.5 figure is taken from a comparison table in another paper rather than from the paper's own note, and the paper's small-model table has an ambiguous column structure ([1611.01462.txt](1611.01462.txt); [1611.01578.txt](1611.01578.txt)).

## 6. Conclusion

Based strictly on the supplied information and the stated inclusion criteria, the compiled answer is: Zaremba et al. 78.4; Kim et al. 78.9; Gal & Ghahramani 73.4; Zilly et al. 65.4; Press & Wolf 74.3; Inan et al. 68.5; NAS 62.4; GRURNTN 87.38; Melis et al. 58.3; AWD-LSTM 57.3 (53.3 claimed); and AWD-LSTM-MoS 54.44. On my reading of the evidence, the single best word-level PTB test perplexity reported for an author's own proposed model without dynamic evaluation or cache is 54.44 for AWD-LSTM-MoS with finetuning ([1711.03953_note.txt](1711.03953_note.txt)); this conclusion is conditional on treating the paper's own Table 1 value of 57.3 as the AWD-LSTM figure rather than the uncorroborated 53.3, and would reverse if the latter were verified. The ranking is also sensitive to whether combined configurations (for example, weight tying plus Bayesian dropout at 73.2) are counted as the paper's proposed model; under the more conservative reading applied here, they are not.

## References

- 1409.2329.txt [Recurrent Neural Network Regularization — paper excerpt]. Provided corpus.
- 1409.2329_note.txt [Third-party research note: Recurrent Neural Network Regularization]. Provided corpus.
- 1508.06615.txt [Character-Aware Neural Language Models — paper excerpt]. Provided corpus.
- 1508.06615_note.txt [Third-party research note: Character-Aware Neural Language Models]. Provided corpus.
- 1512.05287.txt [A Theoretically Grounded Application of Dropout in Recurrent Neural Networks — paper excerpt]. Provided corpus.
- 1512.05287_note.txt [Third-party research note: Variational LSTM / A Theoretically Grounded Application of Dropout]. Provided corpus.
- 1607.03474.txt [Recurrent Highway Networks — paper excerpt]. Provided corpus.
- 1607.03474_note.txt [Third-party research note: Recurrent Highway Networks]. Provided corpus.
- 1608.05859.txt [Using the Output Embedding to Improve Language Models — paper excerpt]. Provided corpus.
- 1608.05859_note.txt [Third-party research note: Using the Output Embedding to Improve Language Models]. Provided corpus.
- 1611.01462.txt [Tying Word Vectors and Word Classifiers: A Loss Framework for Language Modeling — paper excerpt]. Provided corpus.
- 1611.01462_note.txt [Third-party research note: Tying Word Vectors and Word Classifiers]. Provided corpus.
- 1611.01578.txt [Neural Architecture Search with Reinforcement Learning — paper excerpt]. Provided corpus.
- 1611.01578_note.txt [Third-party research note: Neural Architecture Search with Reinforcement Learning]. Provided corpus.
- 1706.02222.txt [Gated Recurrent Neural Tensor Network — paper excerpt]. Provided corpus.
- 1706.02222_note.txt [Third-party research note: Gated Recurrent Neural Tensor Network]. Provided corpus.
- 1707.05589.txt [On the State of the Art of Evaluation in Neural Language Models — paper excerpt]. Provided corpus.
- 1707.05589_note.txt [Third-party research note: On the State of the Art of Evaluation in Neural Language Models]. Provided corpus.
- 1708.02182.txt [Regularizing and Optimizing LSTM Language Models — paper excerpt]. Provided corpus.
- 1708.02182_note.txt [Third-party research note: Regularizing and Optimizing LSTM Language Models]. Provided corpus.
- 1711.03953.txt [Breaking the Softmax Bottleneck: A High-Rank RNN Language Model — paper excerpt]. Provided corpus.
- 1711.03953_note.txt [Third-party research note: Breaking the Softmax Bottleneck]. Provided corpus.