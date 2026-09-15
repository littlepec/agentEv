# Lowest Penn Treebank Word-Level Single-Model Test Perplexity Without Dynamic Evaluation or Cache/Pointer Augmentation

## Key Finding and Direct Answer

Across the provided papers, the lowest word-level Penn Treebank (PTB) test perplexity for a single model that does **not** use dynamic evaluation and does **not** use cache or pointer augmentation is **53.3**, reported in the source note for **1708.02182_note.txt**, the paper “Regularizing and Optimizing LSTM Language Models,” which proposes **AWD-LSTM** ([1708.02182_note.txt](1708.02182_note.txt)). The note states that this 53.3 result is for a 3-layer LSTM with tied weights, reported as a single model without cache/pointer augmentation, and that the result includes the paper’s fine-tuning step ([1708.02182_note.txt](1708.02182_note.txt)). The same note also reports an even lower PTB test perplexity of **52.8** when the model is augmented with a **continuous cache pointer**, but that value is excluded from the present ranking because the query explicitly excludes cache or pointer augmentation ([1708.02182_note.txt](1708.02182_note.txt)).

This finding is not merely a matter of selecting the smallest number. It depends on applying the query’s constraints consistently: single-model results only, no dynamic evaluation, and no cache/pointer augmentation. Under those constraints, the 53.3 AWD-LSTM result is the best qualifying value among the provided papers. Fine-tuning is allowed because the query does not exclude it; however, because this is a potentially important interpretive point, I also provide a sensitivity analysis showing how the ranking would change if fine-tuning were additionally excluded.

## Scope and Inclusion Criteria

For this report, a result qualifies only if it satisfies all of the following criteria:

1. It is a **word-level Penn Treebank test perplexity**.
2. It is reported for a **single model**, not an ensemble, model average, or multi-model combination.
3. It does **not** use **dynamic evaluation**.
4. It does **not** use **cache or pointer augmentation**.
5. It is either the paper’s proposed model or the best qualifying single-model result reported by that paper.

Fine-tuning is not excluded by the query, so results that include fine-tuning are treated as eligible. Ensembles and model averaging are excluded because they are not single-model results. For example, the regularized-LSTM note lists model-averaging values such as 68.7 for 38 large regularized LSTMs, but those are averaged or ensembled results rather than single-model perplexities ([1409.2329_note.txt](1409.2329_note.txt)). Similarly, the variational-dropout note reports an ensemble result where 10 Variational LSTMs with MC dropout improve Zaremba et al.’s test perplexity from 69.5 to 68.7, but that is also not a single-model result ([1512.05287_note.txt](1512.05287_note.txt)).

The ranking below uses each paper’s best qualifying single-model PTB test perplexity. Lower perplexity is better.

## Ranking of Papers by Best Qualifying Single-Model PTB Test Perplexity

| Rank | Source note / paper | Best qualifying single-model PTB test perplexity | Model and qualifying notes |
|---:|---|---:|---|
| 1 | [1708.02182_note.txt](1708.02182_note.txt) | **53.3** | AWD-LSTM, 3-layer LSTM with tied weights; single model without cache/pointer; includes fine-tuning; cache-pointer variant of 52.8 excluded |
| 2 | [1711.03953_note.txt](1711.03953_note.txt) | **54.44** | AWD-LSTM-MoS with fine-tuning; 55.97 without fine-tuning; dynamic-evaluation result of 47.69 excluded |
| 3 | [1707.05589_note.txt](1707.05589_note.txt) | **58.3** | 4-layer LSTM with 24M parameters; single model; no dynamic evaluation, cache/pointer, ensemble, or fine-tuning |
| 4 | [1611.01578_note.txt](1611.01578_note.txt) | **62.4** | Neural Architecture Search with base 8 and shared embeddings, 54M parameters; single model; no dynamic evaluation, cache/pointer, ensemble, or fine-tuning |
| 5 | [1607.03474_note.txt](1607.03474_note.txt) | **65.4** | Variational RHN + WT, 23M parameters; single model; no dynamic evaluation, cache/pointer, ensemble, or fine-tuning |
| 6 | [1611.01462_note.txt](1611.01462_note.txt) | **66.0** | VD-RHN+RE; described as best overall; cache/pointer/ensemble entries appear only as baselines |
| 7 | [1512.05287_note.txt](1512.05287_note.txt) | **73.4** | Large Variational LSTM with untied weights and MC dropout; single model; no dynamic evaluation, cache/pointer, or fine-tuning |
| 8 | [1608.05859_note.txt](1608.05859_note.txt) | **74.3** | Large NNLM with weight tying; single model; no dynamic evaluation, cache/pointer, ensemble, or fine-tuning |
| 9 | [1409.2329_note.txt](1409.2329_note.txt) | **78.4** | Large regularized LSTM; single model; model-averaging values such as 68.7 are excluded |
| 10 | [1508.06615_note.txt](1508.06615_note.txt) | **78.9** | LSTM-Char-Large; single model; ensembles excluded; no dynamic evaluation, cache/pointer, or fine-tuning |
| 11 | [1706.02222_note.txt](1706.02222_note.txt) | **87.38** | GRURNTN; individual model; no dynamic evaluation, cache/pointer, ensemble, or fine-tuning |

## Detailed Discussion of the Lowest-Reporting Paper

The lowest qualifying result comes from the note on **1708.02182_note.txt**, which describes the paper “Regularizing and Optimizing LSTM Language Models” and its proposed **AWD-LSTM**, short for ASGD Weight-Dropped LSTM ([1708.02182_note.txt](1708.02182_note.txt)). The note reports a word-level PTB test perplexity of **53.3** for AWD-LSTM, described as a 3-layer LSTM with tied weights and as a single model without cache/pointer augmentation ([1708.02182_note.txt](1708.02182_note.txt)). The result includes the paper’s fine-tuning step, and the Table 1 caption explicitly identifies the results as single-model perplexity on validation and test sets for the PTB language modeling task ([1708.02182_note.txt](1708.02182_note.txt)).

The same note contains two important qualifications. First, a no-fine-tuning ablation is listed at **58.8** PTB test perplexity, and the paper states that removal of the fine-tuning step degrades performance ([1708.02182_note.txt](1708.02182_note.txt)). Second, the paper reports a **continuous cache pointer** variant with an even lower PTB test perplexity of **52.8**, and 52.0 on WikiText-2 ([1708.02182_note.txt](1708.02182_note.txt)). Because the query excludes cache or pointer augmentation, the 52.8 value is not eligible. The 53.3 value remains eligible because it is a single model without cache/pointer augmentation, and fine-tuning is not excluded by the query.

The note also states that the vanilla AWD-LSTM improves the state of the art by approximately 1 unit on PTB and 0.1 units on WikiText-2, and that AWD-LSTM’s 53.3 beats the best listed baseline, Melis et al. 2017 4-layer skip connection LSTM (tied) at 58.3 ([1708.02182_note.txt](1708.02182_note.txt)). This matters for ranking because it shows the 53.3 result is not merely the best among weaker baselines; it is reported as a genuine single-model advance under the paper’s own evaluation conditions.

The closest competitor is the note for **1711.03953_note.txt**, “Breaking the Softmax Bottleneck: A High-Rank RNN Language Model,” which reports AWD-LSTM-MoS at **55.97** without fine-tuning and **54.44** with fine-tuning ([1711.03953_note.txt](1711.03953_note.txt)). The same note reports a dynamic-evaluation result of **47.69**, but that is excluded under the query because it uses dynamic evaluation ([1711.03953_note.txt](1711.03953_note.txt)). Thus, even though 47.69 is numerically lower, it does not qualify. Under the query’s criteria, 1708.02182_note.txt’s 53.3 is lower than 1711.03953_note.txt’s 54.44 by 1.14 perplexity points.

## Detailed Discussion of the Remaining Ranked Papers

### 1711.03953: AWD-LSTM-MoS at 54.44

The AWD-LSTM-MoS paper reports its proposed model in single-model settings without dynamic evaluation ([1711.03953_note.txt](1711.03953_note.txt)). Table 1 lists 55.97 without fine-tuning and 54.44 with fine-tuning, while the dynamic-evaluation variant reaches 47.69 ([1711.03953_note.txt](1711.03953_note.txt)). The note further states that the paper does not report results for its proposed model on PTB using cache/pointer or ensemble methods; it reports results with and without dynamic evaluation and fine-tuning ([1711.03953_note.txt](1711.03953_note.txt)). Therefore, the best qualifying value for this paper is 54.44.

### 1707.05589: 4-Layer LSTM at 58.3

The note for **1707.05589_note.txt**, “On the State of the Art of Evaluation in Neural Language Models,” reports a best word-level PTB test perplexity of **58.3** for a 4-layer LSTM with 24M parameters ([1707.05589_note.txt](1707.05589_note.txt)). The authors state that at 24M, all depths obtain very similar results, reaching 58.3 at depth 4 ([1707.05589_note.txt](1707.05589_note.txt)). This result is reported for a single model, without dynamic evaluation, cache/pointer, ensemble, or fine-tuning ([1707.05589_note.txt](1707.05589_note.txt)). The note also says the paper explicitly refrains from including techniques known to push perplexities even lower because its aim is strictly better model comparisons for the architectures under study ([1707.05589_note.txt](1707.05589_note.txt)). That makes the 58.3 result a particularly clean qualifying value.

### 1611.01578: Neural Architecture Search at 62.4

The Neural Architecture Search note reports **62.4** PTB test perplexity for the best NAS model, described as NAS with base 8 and shared embeddings, 54M parameters ([1611.01578_note.txt](1611.01578_note.txt)). Other NAS configurations are listed at 64.0 and 67.9 ([1611.01578_note.txt](1611.01578_note.txt)). These are single-model test perplexities, and the note states that the paper does not report dynamic evaluation, cache/pointer, ensemble, or fine-tuning for the NAS model on PTB ([1611.01578_note.txt](1611.01578_note.txt)). The best listed baseline in that comparison is Zilly et al. 2016 Variational RHN with shared embeddings at 66.0, so the 62.4 NAS result is 3.6 perplexity better than that baseline ([1611.01578_note.txt](1611.01578_note.txt)).

### 1607.03474: Variational RHN + WT at 65.4

The Recurrent Highway Networks note reports **65.4** PTB word-level test perplexity for **Variational RHN + WT** ([1607.03474_note.txt](1607.03474_note.txt)). It also reports 68.5 for Variational RHN without WT, and the best 10-layer model with reduced weight decay improves to 67.9/65.4 validation/test perplexity ([1607.03474_note.txt](1607.03474_note.txt)). Table 1 lists this as 23M parameters with validation/test perplexity 67.9/65.4, using variational dropout and weight tying of input and output mappings ([1607.03474_note.txt](1607.03474_note.txt)). The best PTB result is a single model, and dynamic evaluation, cache/pointer, ensemble, and fine-tuning are not reported for the proposed model; cache and pointer methods appear only as baselines, and ensembles only in comparison ([1607.03474_note.txt](1607.03474_note.txt)).

### 1611.01462: VD-RHN+RE at 66.0

The note for **1611.01462_note.txt**, “Tying Word Vectors and Word Classifiers: A Loss Framework for Language Modeling,” reports that **VD-RHN+RE** trained with reused embeddings achieves validation perplexity 68.1 and test perplexity **66.0** on PTB, which the paper describes as best overall ([1611.01462_note.txt](1611.01462_note.txt)). The note’s PTB baselines involving cache, pointer, or ensemble methods include RNN+LDA+KN-5+Cache at 92.0, Pointer Sentinel-LSTM(medium) at 70.9, 38 Large LSTMs at 68.7, and 10 Large VD-LSTMs at 68.7 ([1611.01462_note.txt](1611.01462_note.txt)). Those lower-looking numbers are not eligible as the paper’s proposed single-model result because they involve cache, pointer, or ensemble settings. The 66.0 result is the paper’s qualifying single-model value.

### 1512.05287: Variational LSTM at 73.4

The note for **1512.05287_note.txt**, “A Theoretically Grounded Application of Dropout in Recurrent Neural Networks,” reports **73.4** test perplexity for the proposed Variational LSTM on PTB ([1512.05287_note.txt](1512.05287_note.txt)). The paper states that test perplexity is reduced from 78.4 down to 73.4 with MC dropout and untied weights, and the note identifies this as a single-model result for the large Variational LSTM with untied weights and MC dropout at test time ([1512.05287_note.txt](1512.05287_note.txt)). The paper does not report dynamic evaluation, cache/pointer, or fine-tuning for this PTB result, and the Table 1 caption identifies the results as single-model perplexity on test and validation sets ([1512.05287_note.txt](1512.05287_note.txt)). Its ensemble result of 68.7 with 10 Variational LSTMs is excluded because it is not a single model ([1512.05287_note.txt](1512.05287_note.txt)).

### 1608.05859: Large NNLM + Weight Tying at 74.3

The note for **1608.05859_note.txt**, “Using the Output Embedding to Improve Language Models,” reports word-level PTB test perplexity for its proposed weight-tied neural network language models in single-model settings ([1608.05859_note.txt](1608.05859_note.txt)). The large NNLM with weight tying reaches **74.3** test perplexity, while the small NNLM with weight tying and projection regularization reaches 100.9 ([1608.05859_note.txt](1608.05859_note.txt)). Both numbers are reported without dynamic evaluation, cache/pointer, ensemble, or fine-tuning ([1608.05859_note.txt](1608.05859_note.txt)). The paper’s comparison baselines include Zaremba et al. 2014’s large NNLM at 78.4 and small NNLM at 114.5, so the large weight-tied result improves on the large baseline ([1608.05859_note.txt](1608.05859_note.txt)).

### 1409.2329: Large Regularized LSTM at 78.4

The note for **1409.2329_note.txt** reports model averaging of regularized LSTMs and lists averaged values such as 77.0, 73.3, 72.0, 73.6, 69.5, and 68.7 ([1409.2329_note.txt](1409.2329_note.txt)). Those are not single-model results and are therefore excluded. The paper’s single-model baseline list includes Pascanu et al. 2013 at 107.5, Cheng et al. at 100.0, and a non-regularized LSTM at 114.5 ([1409.2329_note.txt](1409.2329_note.txt)). The proposed medium regularized LSTM is reported at 82.7 and the large regularized LSTM at **78.4**, both described as lower than all listed single-model baselines ([1409.2329_note.txt](1409.2329_note.txt)). The note also states that the paper does not report dynamic evaluation, cache/pointer, or fine-tuning settings for PTB perplexity ([1409.2329_note.txt](1409.2329_note.txt)). Thus 78.4 is the qualifying value.

### 1508.06615: Character-Aware LSTM at 78.9

The Character-Aware Neural Language Models note reports word-level PTB test perplexity for the proposed character-aware LSTM language model: LSTM-Char-Large attains **78.9** and LSTM-Char-Small attains 92.3 ([1508.06615_note.txt](1508.06615_note.txt)). Predictions are made at the word level, and these are single-model results ([1508.06615_note.txt](1508.06615_note.txt)). The paper explicitly excludes ensembles, stating that lower perplexities have been reported with model ensembles but are not comparable to the current work ([1508.06615_note.txt](1508.06615_note.txt)). No dynamic evaluation, cache/pointer, or fine-tuning PTB results appear ([1508.06615_note.txt](1508.06615_note.txt)). The best qualifying value is therefore 78.9.

### 1706.02222: GRURNTN at 87.38

The note for **1706.02222_note.txt** proposes GRURNTN and LSTMRNTN, described as a Gated Recurrent Unit Recurrent Neural Tensor Network and a Long-Short Term Memory Recurrent Neural Tensor Network ([1706.02222_note.txt](1706.02222_note.txt)). For word-level PTB language modeling, Table II reports test perplexity **87.38** for GRURNTN and 96.97 for LSTMRNTN ([1706.02222_note.txt](1706.02222_note.txt)). These proposed results are reported as individual models, and the paper states that baseline and proposed model experiments did not use dynamic evaluation ([1706.02222_note.txt](1706.02222_note.txt)). No cache/pointer, ensemble, or fine-tuning setting is reported for the proposed word-level results ([1706.02222_note.txt](1706.02222_note.txt)). The paper lists baseline and published word-level PTB test perplexities including GRURNN at 97.78, LSTMRNN at 108.26, N-Gram at 141, RNNLM without dynamic evaluation at 124.7, RNNLM with dynamic evaluation at 123.2, SCRNN at 115, sRNN at 110.0, and DOT(S)-RNN at 107.5 ([1706.02222_note.txt](1706.02222_note.txt)).

## Sensitivity Analysis: If Fine-Tuning Is Also Excluded

The query excludes dynamic evaluation and cache/pointer augmentation but does not exclude fine-tuning. That is why AWD-LSTM’s 53.3 result qualifies and ranks first. If a stricter interpretation were applied—excluding fine-tuning as well—the ranking would change.

Under that stricter interpretation, AWD-LSTM’s no-fine-tuning ablation is 58.8 PTB test perplexity ([1708.02182_note.txt](1708.02182_note.txt)). The AWD-LSTM-MoS paper reports 55.97 without fine-tuning ([1711.03953_note.txt](1711.03953_note.txt)). The 4-layer LSTM paper reports 58.3 without fine-tuning ([1707.05589_note.txt](1707.05589_note.txt)). Therefore, if fine-tuning were excluded as well, the lowest qualifying value would become **55.97**, from **1711.03953_note.txt**’s AWD-LSTM-MoS without fine-tuning ([1711.03953_note.txt](1711.03953_note.txt)). The top three under that alternative reading would be: 1711.03953 at 55.97, 1707.05589 at 58.3, and 1708.02182 at 58.8. This sensitivity analysis reinforces that the direct answer to the stated query is 53.3, but also shows that the ranking is sensitive to how fine-tuning is treated.

## Excluded Lower Numbers and Why They Do Not Qualify

Several reported values are numerically lower than the top qualifying result but fail one or more of the query’s constraints. The most important is AWD-LSTM’s **52.8** with a continuous cache pointer, which is excluded because it uses cache/pointer augmentation ([1708.02182_note.txt](1708.02182_note.txt)). The AWD-LSTM-MoS **47.69** result is excluded because it uses dynamic evaluation ([1711.03953_note.txt](1711.03953_note.txt)). The regularized-LSTM model-averaging values, including 68.7 for 38 large regularized LSTMs, are excluded because they are not single-model results ([1409.2329_note.txt](1409.2329_note.txt)). The 10-Variational-LSTM ensemble at 68.7 is excluded for the same reason ([1512.05287_note.txt](1512.05287_note.txt)). The Tying Word Vectors note lists cache/pointer/ensemble baselines such as RNN+LDA+KN-5+Cache at 92.0, Pointer Sentinel-LSTM(medium) at 70.9, 38 Large LSTMs at 68.7, and 10 Large VD-LSTMs at 68.7, but those are not the paper’s proposed single-model result ([1611.01462_note.txt](1611.01462_note.txt)). The GRURNTN paper reports an RNNLM with dynamic evaluation at 123.2, but that is a baseline and is also excluded by the no-dynamic-evaluation criterion ([1706.02222_note.txt](1706.02222_note.txt)).

## Conclusion

The direct answer to the query is that the lowest qualifying word-level Penn Treebank test perplexity for a single model without dynamic evaluation and without cache or pointer augmentation is **53.3**, reported in **1708.02182_note.txt** for **AWD-LSTM** ([1708.02182_note.txt](1708.02182_note.txt)). The next best qualifying result is **54.44** from **1711.03953_note.txt** for AWD-LSTM-MoS with fine-tuning ([1711.03953_note.txt](1711.03953_note.txt)), followed by **58.3** from **1707.05589_note.txt** ([1707.05589_note.txt](1707.05589_note.txt)). The ranking is robust under the stated criteria, but it depends on permitting fine-tuning: if fine-tuning were also excluded, the lowest value would shift to **55.97** from 1711.03953_note.txt ([1711.03953_note.txt](1711.03953_note.txt)). Under the query as written, however, the answer and top rank belong to AWD-LSTM at 53.3.

## References

- 1409.2329_note.txt. (n.d.). *Source note on regularized LSTMs*. Retrieved from [1409.2329_note.txt](1409.2329_note.txt)
- 1508.06615_note.txt. (n.d.). *Character-Aware Neural Language Models*. Retrieved from [1508.06615_note.txt](1508.06615_note.txt)
- 1512.05287_note.txt. (n.d.). *A Theoretically Grounded Application of Dropout in Recurrent Neural Networks*. Retrieved from [1512.05287_note.txt](1512.05287_note.txt)
- 1607.03474_note.txt. (n.d.). *Recurrent Highway Networks*. Retrieved from [1607.03474_note.txt](1607.03474_note.txt)
- 1608.05859_note.txt. (n.d.). *Using the Output Embedding to Improve Language Models*. Retrieved from [1608.05859_note.txt](1608.05859_note.txt)
- 1611.01462_note.txt. (n.d.). *Tying Word Vectors and Word Classifiers: A Loss Framework for Language Modeling*. Retrieved from [1611.01462_note.txt](1611.01462_note.txt)
- 1611.01578_note.txt. (n.d.). *Neural Architecture Search with Reinforcement Learning*. Retrieved from [1611.01578_note.txt](1611.01578_note.txt)
- 1706.02222_note.txt. (n.d.). *Source note on GRURNTN and LSTMRNTN*. Retrieved from [1706.02222_note.txt](1706.02222_note.txt)
- 1707.05589_note.txt. (n.d.). *On the State of the Art of Evaluation in Neural Language Models*. Retrieved from [1707.05589_note.txt](1707.05589_note.txt)
- 1708.02182_note.txt. (n.d.). *Regularizing and Optimizing LSTM Language Models*. Retrieved from [1708.02182_note.txt](1708.02182_note.txt)
- 1711.03953_note.txt. (n.d.). *Breaking the Softmax Bottleneck: A High-Rank RNN Language Model*. Retrieved from [1711.03953_note.txt](1711.03953_note.txt)