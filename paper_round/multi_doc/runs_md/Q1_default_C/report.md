# Lowest Single-Model Word-Level Penn Treebank Test Perplexity Without Dynamic Evaluation, Cache/Pointer Augmentation, or Ensembling: A Comparative Ranking of Nine Papers

## Summary of the Finding

Across the nine papers represented in the supplied source material, the lowest reported word-level test perplexity on the Penn Treebank (PTB) for a **single model evaluated without dynamic evaluation, cache or pointer augmentation, or ensembling** is **58.3**, reported by the paper *On the State of the Art of Evaluation in Neural Language Models*, identified here by its arXiv identifier 1707.05589 ([Melis et al., 2017](https://arxiv.org/abs/1707.05589)). That figure is attributed to a 4-layer LSTM with 24M parameters, and the authors explicitly state that they refrained from including techniques known to push perplexities lower because their goal was strictly to improve the fairness of architecture comparisons ([Melis et al., 2017](https://arxiv.org/abs/1707.05589)).

The runner-up is the Neural Architecture Search (NAS) model at **62.4** test perplexity with 54M parameters ([Zoph & Le, 2016](https://arxiv.org/abs/1611.01578)), followed by Variational RHN + WT at **65.4** with 23M parameters ([Zilly et al., 2016](https://arxiv.org/abs/1607.03474)). The remaining papers cluster between 66.0 and 87.38 test perplexity. A complete ranking is presented in the next section.

## Inclusion Criteria and Metric Definition

### The target metric

The query concerns **word-level test perplexity on the Penn Treebank** — that is, the standard word-level language modeling benchmark originally associated with Marcus et al. (1993) and preprocessed by Mikolov et al. (2010), as described in the PTB experiment section of the Recurrent Highway Networks paper ([Zilly et al., 2016](https://arxiv.org/abs/1607.03474)). Lower values are better. Only the **single-model** configuration is counted, following the explicit statement in the source notes that model averaging and ensembling are excluded from the comparison, since ensembles are "not comparable to the current work" ([Kim et al., 2015](https://arxiv.org/abs/1508.06615)).

### Exclusions applied

The following result classes were excluded from the ranking because they violate the query's constraints:

1. **Ensembles and model averaging.** These include 2, 5, 10, and 38 regularized LSTM averages at 77.0, 73.3, 72.0, 73.6, 69.5, and 68.7 respectively ([Zaremba et al., 2014](https://arxiv.org/abs/1409.2329)); the 10-large-VD-LSTM and 38-large-LSTM ensembles at 68.7 reported as baselines ([Inan et al., 2016](https://arxiv.org/abs/1611.01462)); and the 10-model Variational LSTM ensemble at 68.7 in the variational dropout paper ([Gal & Ghahramani, 2016](https://arxiv.org/abs/1512.05287)).
2. **Cache and pointer augmentation.** The RNN+LDA+KN-5+Cache system at 92.0 test perplexity ([Inan et al., 2016](https://arxiv.org/abs/1611.01462)) and Pointer Sentinel-LSTM (medium) at 70.9 are excluded ([Inan et al., 2016](https://arxiv.org/abs/1611.01462)). In the NAS paper, cache/pointer appears only as a baseline label such as Pointer Sentinel-LSTM ([Zoph & Le, 2016](https://arxiv.org/abs/1611.01578)).
3. **Dynamic evaluation and fine-tuning.** Notably, none of the supplied source notes report dynamic evaluation or fine-tuning results for the proposed models, so this exclusion does not remove any candidate entry.

## Ranking of Papers by Best Single-Model PTB Word-Level Test Perplexity

| Rank | Paper (arXiv ID) | Best single-model test PPL | Model / configuration | Parameters | Primary source type |
|:----:|:-----------------|:--------------------------:|:----------------------|:----------:|:--------------------|
| 1 | [1707.05589](https://arxiv.org/abs/1707.05589) | **58.3** | 4-layer LSTM (depth 4) | 24M | Third-party research note / paper |
| 2 | [1611.01578](https://arxiv.org/abs/1611.01578) | **62.4** | NAS, base 8 + shared embeddings | 54M | Paper-derived note |
| 3 | [1607.03474](https://arxiv.org/abs/1607.03474) | **65.4** | Variational RHN + WT (10 layers) | 23M | Paper-derived note + paper text |
| 4 | [1611.01462](https://arxiv.org/abs/1611.01462) | **66.0** | VD-RHN+RE (third-party model reported in-paper) | n/r | Paper-derived note |
| 5 | [1512.05287](https://arxiv.org/abs/1512.05287) | **73.4** | Large Variational LSTM, untied, MC dropout | 66M | Paper-derived note + paper text |
| 6 | [1608.05859](https://arxiv.org/abs/1608.05859) | **74.3** | Large NNLM + weight tying | n/r | Third-party research note |
| 7 | [1409.2329](https://arxiv.org/abs/1409.2329) | **78.4** | Large regularized LSTM (single) | 66M | Paper-derived note |
| 8 | [1508.06615](https://arxiv.org/abs/1508.06615) | **78.9** | LSTM-Char-Large | n/r | Paper-derived note |
| 9 | [1706.02222](https://arxiv.org/abs/1706.02222) | **87.38** | GRURNTN | n/r | Paper-derived note |

## Detailed Discussion of the Top-Ranked Results

### Rank 1 — 58.3 test perplexity (arXiv:1707.05589)

This paper reports a best word-level test perplexity of **58.3** on PTB for its own proposed model, a 4-layer LSTM with 24M parameters ([Melis et al., 2017](https://arxiv.org/abs/1707.05589)). The authors state that at 24M parameters all depths obtain very similar results, reaching 58.3 at depth 4 ([Melis et al., 2017](https://arxiv.org/abs/1707.05589)). Critically for the present query, the result is reported for a single model, without dynamic evaluation, cache/pointer augmentation, ensemble, or fine-tuning, and the paper explicitly refrains from including techniques that are known to push perplexities even lower because its aim is strictly to do better model comparisons for the architectures under study ([Melis et al., 2017](https://arxiv.org/abs/1707.05589)).

This is also the most recent source in the set (2017), and the source is an independent, methodologically oriented evaluation study rather than a claim of a new architecture, which strengthens its credibility for benchmarking purposes.

### Rank 2 — 62.4 test perplexity (arXiv:1611.01578)

The NAS paper reports **62.4** test perplexity on PTB for its best Neural Architecture Search model, described as NAS with base 8 and shared embeddings and 54M parameters ([Zoph & Le, 2016](https://arxiv.org/abs/1611.01578)). Two further NAS configurations are reported: 64.0 with 25M parameters (base 8 plus shared embeddings) and 67.9 with 32M parameters (base 8 only) ([Zoph & Le, 2016](https://arxiv.org/abs/1611.01578)). These are single-model test-set perplexities, and the paper does not report dynamic evaluation, cache/pointer, ensemble, or fine-tuning for the NAS model on PTB ([Zoph & Le, 2016](https://arxiv.org/abs/1611.01578)). The 62.4 result is therefore fully eligible, and the fact that it is achieved at 54M parameters — more than twice the 24M of the rank-1 model — is a relevant efficiency caveat.

### Rank 3 — 65.4 test perplexity (arXiv:1607.03474)

The Recurrent Highway Networks paper reports its best PTB word-level test perplexity for the proposed model as **65.4** for Variational RHN + WT, with validation/test perplexity of 67.9/65.4 at 23M parameters ([Zilly et al., 2016](https://arxiv.org/abs/1607.03474)). The paper also reports 68.5 test perplexity for Variational RHN without weight tying (WT), and notes that it presents PTB results both with and without WT for fair comparisons ([Zilly et al., 2016](https://arxiv.org/abs/1607.03474)). The best 10-layer model with reduced weight decay improves to 67.9/65.4 validation/test perplexity, and the paper's own experiment section confirms that test scores improve as recurrence depth increases from 1 to 10 at a fixed 32M total parameter budget ([Zilly et al., 2016](https://arxiv.org/abs/1607.03474)). The best PTB result is a single model; dynamic evaluation, cache/pointer, ensemble, and fine-tuning are not reported for the proposed model, and cache/pointer methods appear only as baselines ([Zilly et al., 2016](https://arxiv.org/abs/1607.03474)). The paper further states that RHNs outperform most single models as well as all previous ensembles ([Zilly et al., 2016](https://arxiv.org/abs/1607.03474)) — a strong claim that is nevertheless consistent with the numbers assembled here.

### Rank 4 — 66.0 test perplexity (arXiv:1611.01462), with an important caveat

The tying/reused-embedding paper reports that VD-RHN+RE (Zilly et al., 2016), trained with reused embeddings following the paper's framework, achieves validation perplexity 68.1 and test perplexity **66.0** on PTB, which the paper describes as best overall ([Inan et al., 2016](https://arxiv.org/abs/1611.01462)). This is a third-party re-application of another paper's architecture rather than the paper's own headline model, and it lands almost exactly on top of the 65.4 reported by the original RHN work, which is a useful cross-validation of that result.

However, a sensitivity check matters: the paper's **own** models in the same table — the 200-unit VD-LSTM family — occupy a far worse range, with perplexities spanning 138.4 to 163.19 (for example, VD-LSTM 148.6, VD-LSTM+RE 140.9, and VD-LSTM+REAL 138.4 in the relevant columns) ([Inan et al., 2016](https://arxiv.org/abs/1611.01462)). If the ranking were restricted strictly to each paper's *own* proposed architecture, this paper would fall to last place rather than fourth. The paper also lists cache-, pointer-, and ensemble-based baselines that are excluded here: RNN+LDA+KN-5+Cache at 92.0, Pointer Sentinel-LSTM (medium) at 70.9, 38 Large LSTMs at 68.7, and 10 Large VD-LSTMs at 68.7 ([Inan et al., 2016](https://arxiv.org/abs/1611.01462)).

## Mid-Tier and Lower-Tier Entries

### Rank 5 — 73.4 test perplexity (arXiv:1512.05287)

The variational dropout paper reports **73.4** test perplexity for the large Variational LSTM with untied weights and MC dropout at test time, reduced from 78.4 with MC dropout and untied weights; the paper claims this is the best single-model perplexity on PTB at the time ([Gal & Ghahramani, 2016](https://arxiv.org/abs/1512.05287)). Its own comparison table places it below all listed baselines: non-regularized early stopping (medium 121.7, large 127.4), Moon et al. December 2015 (medium 97.0, large 118.7), Moon et al. plus embedding dropout (medium 86.5, large 86.0), Zaremba et al. 2014 (medium 82.7, large 78.4), Variational tied weights (medium 79.7, large 75.0), Variational tied weights with MC (medium 79.0, large 74.1), and Variational untied weights (medium 79.7, large 75.2) ([Gal & Ghahramani, 2016](https://arxiv.org/abs/1512.05287)). Its ensemble result at 68.7 is excluded by the query's single-model restriction ([Gal & Ghahramani, 2016](https://arxiv.org/abs/1512.05287)).

### Rank 6 — 74.3 test perplexity (arXiv:1608.05859)

The output-embedding paper reports word-level PTB test perplexity for its weight-tied neural network language models in single-model settings: the large NNLM with weight tying reaches **74.3**, and the small NNLM with weight tying plus projection regularization reaches 100.9 ([Press & Wolf, 2016](https://arxiv.org/abs/1608.05859)). Neither uses dynamic evaluation, cache/pointer, ensemble, or fine-tuning ([Press & Wolf, 2016](https://arxiv.org/abs/1608.05859)). Its comparison context includes the large Zaremba NNLM at 78.4 and the small one at 114.5, along with non-dropout baselines such as KN 5-gram 141, RNN 123, LSTM 117, Stack RNN 110, FOFE-FNN 108, Noisy LSTM 108.0, and Deep RNN 107.5 ([Press & Wolf, 2016](https://arxiv.org/abs/1608.05859)).

### Rank 7 — 78.4 test perplexity (arXiv:1409.2329)

The regularized LSTM paper's single-model results are the medium regularized LSTM at 82.7 and the large regularized LSTM at **78.4**, both better than the listed single-model baselines (Pascanu et al. 2013 at 107.5, Cheng et al. at 100.0, and a non-regularized LSTM at 114.5) ([Zaremba et al., 2014](https://arxiv.org/abs/1409.2329)). Its averaged results — 77.0, 73.3, 72.0, 73.6, 69.5, and 68.7 for 2/5/10 medium and 2/10/38 large models — are excluded by the query's restriction to single models ([Zaremba et al., 2014](https://arxiv.org/abs/1409.2329)). It is worth noting that this paper's single-model 78.4 is the very baseline that the variational LSTM improved upon four years later ([Gal & Ghahramani, 2016](https://arxiv.org/abs/1512.05287)).

### Rank 8 — 78.9 test perplexity (arXiv:1508.06615)

The character-aware language model paper reports LSTM-Char-Large at **78.9** and LSTM-Char-Small at 92.3, with predictions made at the word level; both are single-model results and the paper explicitly excludes ensembles as not comparable ([Kim et al., 2015](https://arxiv.org/abs/1508.06615)). No dynamic evaluation, cache/pointer, or fine-tuning PTB results appear ([Kim et al., 2015](https://arxiv.org/abs/1508.06615)). Its 78.9 is also the value cited as the CharCNN baseline in later tables ([Inan et al., 2016](https://arxiv.org/abs/1611.01462)).

### Rank 9 — 87.38 test perplexity (arXiv:1706.02222)

The gated recurrent neural tensor network paper reports that GRURNTN reduces perplexity from 97.78 to **87.38** over GRURNN (a 10.4 absolute and 10.63% relative reduction), while LSTMRNTN reduces perplexity from 108.26 to 96.97 over LSTMRNN (11.29 absolute, 10.42% relative) ([arXiv:1706.02222](https://arxiv.org/abs/1706.02222)). GRURNTN is stated to outperform all baseline and other listed models by a large margin, and it is the strongest proposed word-level PTB perplexity in that paper's table ([arXiv:1706.02222](https://arxiv.org/abs/1706.02222)). Its relatively high absolute perplexity reflects a different, more compact experimental regime rather than a failure to meet the query's constraints.

## Cross-Cutting Observations

Three patterns are worth emphasizing. First, **parameter count does not track perplexity monotonically across papers**: the rank-1 model achieves 58.3 with 24M parameters, whereas the rank-2 NAS model needs 54M for 62.4 ([Melis et al., 2017](https://arxiv.org/abs/1707.05589); [Zoph & Le, 2016](https://arxiv.org/abs/1611.01578)). Second, **weight tying is a recurring, independently validated ingredient**: it underlies the 65.4 RHN result ([Zilly et al., 2016](https://arxiv.org/abs/1607.03474)), the 74.3 NNLM result ([Press & Wolf, 2016](https://arxiv.org/abs/1608.05859)), the 66.0 VD-RHN+RE reproduction ([Inan et al., 2016](https://arxiv.org/abs/1611.01462)), and the tied-weight variants in the variational LSTM table ([Gal & Ghahramani, 2016](https://arxiv.org/abs/1512.05287)). Third, **the absence of dynamic evaluation is universal in this source set** — no paper reports it, so the ranking is not distorted by selective inclusion of that technique, but it also means the ceiling of achievable perplexity under this constraint is not established by these sources alone.

A caution on source reliability applies. Several entries here derive from third-party research notes rather than from directly quoted paper text ([Press & Wolf, 2016](https://arxiv.org/abs/1608.05859); [Melis et al., 2017](https://arxiv.org/abs/1707.05589)), and one source is represented only as a note without full bibliographic metadata ([arXiv:1706.02222](https://arxiv.org/abs/1706.02222)). Where a figure appears in both a note and the paper's own extracted text — as with the 65.4 RHN result and the 73.4 variational LSTM result — confidence is higher ([Zilly et al., 2016](https://arxiv.org/abs/1607.03474); [Gal & Ghahramani, 2016](https://arxiv.org/abs/1512.05287)).

## Conclusion

The lowest word-level PTB test perplexity for a single model without dynamic evaluation, cache/pointer augmentation, or ensembling is **58.3**, reported by *On the State of the Art of Evaluation in Neural Language Models* (arXiv:1707.05589) for a 4-layer, 24M-parameter LSTM ([Melis et al., 2017](https://arxiv.org/abs/1707.05589)). The ranking continues with NAS at 62.4 ([Zoph & Le, 2016](https://arxiv.org/abs/1611.01578)), Variational RHN + WT at 65.4 ([Zilly et al., 2016](https://arxiv.org/abs/1607.03474)), VD-RHN+RE at 66.0 ([Inan et al., 2016](https://arxiv.org/abs/1611.01462)), Variational LSTM at 73.4 ([Gal & Ghahramani, 2016](https://arxiv.org/abs/1512.05287)), weight-tied NNLM at 74.3 ([Press & Wolf, 2016](https://arxiv.org/abs/1608.05859)), regularized LSTM at 78.4 ([Zaremba et al., 2014](https://arxiv.org/abs/1409.2329)), character-aware LSTM at 78.9 ([Kim et al., 2015](https://arxiv.org/abs/1508.06615)), and GRURNTN at 87.38 ([arXiv:1706.02222](https://arxiv.org/abs/1706.02222)).

## References

Gal, Y., & Ghahramani, Z. (2016). *A theoretically grounded application of dropout in recurrent neural networks* [arXiv:1512.05287]. arXiv. https://arxiv.org/abs/1512.05287

Inan, H., Khosravi, K., & Socher, R. (2016). *Tying word vectors and word classifiers: A loss framework for language modeling* [arXiv:1611.01462]. arXiv. https://arxiv.org/abs/1611.01462

Kim, Y., Jernite, Y., Sontag, D., & Rush, A. M. (2015). *Character-aware neural language models* [arXiv:1508.06615]. arXiv. https://arxiv.org/abs/1508.06615

Melis, G., Dyer, C., & Blunsom, P. (2017). *On the state of the art of evaluation in neural language models* [arXiv:1707.05589]. arXiv. https://arxiv.org/abs/1707.05589

Press, O., & Wolf, L. (2016). *Using the output embedding to improve language models* [arXiv:1608.05859]. arXiv. https://arxiv.org/abs/1608.05859

[arXiv:1706.02222]. (2017). *Research note on word-level Penn Treebank perplexities for GRURNTN and LSTMRNTN models* [Source note]. arXiv. https://arxiv.org/abs/1706.02222

Zaremba, W., Sutskever, I., & Vinyals, O. (2014). *Recurrent neural network regularization* [arXiv:1409.2329]. arXiv. https://arxiv.org/abs/1409.2329

Zilly, J. G., Srivastava, R. K., Koutník, J., & Schmidhuber, J. (2016). *Recurrent highway networks* [arXiv:1607.03474]. arXiv. https://arxiv.org/abs/1607.03474

Zoph, B., & Le, Q. V. (2016). *Neural architecture search with reinforcement learning* [arXiv:1611.01578]. arXiv. https://arxiv.org/abs/1611.01578