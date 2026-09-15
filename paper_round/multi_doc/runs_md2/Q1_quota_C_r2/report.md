# Lowest Penn Treebank Word-Level Test Perplexity for a Single Model Without Dynamic Evaluation, Cache, or Pointer Augmentation: A Comparative Ranking of Provided Papers

## Objective and Scope

This report answers a narrow, well-defined question: **across the papers supplied in the source material, which paper reports the lowest word-level test perplexity on the Penn Treebank (PTB) for a single model that does not use dynamic evaluation and does not use cache or pointer augmentation?** It then ranks all supplied papers according to that comparable number.

The query imposes three exclusion criteria: (1) no dynamic evaluation, (2) no cache/pointer augmentation, and (3) single model only (i.e., no ensembles). It does **not** exclude fine-tuning, although fine-tuning status is flagged explicitly wherever it is reported, because it materially affects comparability. Only numbers that the provided sources explicitly attach to the Penn Treebank word-level language modeling test set are used ([Marcus et al., 1993](https://arxiv.org/abs/1409.2329); [Mikolov et al., 2010](https://arxiv.org/abs/1508.06615)).

## Inclusion and Exclusion Criteria

All included results share the standard evaluation protocol: Peppertreebank-style preprocessing following Mikolov et al. (2010), a 10k-word vocabulary, and the standard train/validation/test split used in the language modeling community ([Mikolov et al., 2010](https://arxiv.org/abs/1508.06615); [Marcus et al., 1993](https://arxiv.org/abs/1611.01462)). Papers were excluded from the ranking column **only for specific configurations**, not entirely, when they reported qualifying single-model results alongside non-qualifying ones.

### Excluded configurations

The following reported results are disqualified by the query's criteria and are therefore not counted as each paper's ranking entry:

- **Ensembles:** Zaremba et al.'s 2-medium (77.0), 5-medium (73.3), 10-medium (72.0), 2-large (73.6), 10-large (69.5), and 38-large (68.7) averaged LSTMs ([Zaremba et al., 2014](https://arxiv.org/abs/1409.2329)); Gal and Ghahramani's 10-model Variational LSTM ensemble at 68.7 ([Gal & Ghahramani, 2016](https://arxiv.org/abs/1512.05287)).
- **Cache/pointer augmentation:** AWD-LSTM + continuous cache pointer at 52.8 ([Merity et al., 2018](https://arxiv.org/abs/1708.02182)); Pointer Sentinel-LSTM (medium) at 70.9 ([Inan et al., 2017](https://arxiv.org/abs/1611.01462)); RNN+LDA+KN-5+Cache at 92.0 ([Inan et al., 2017](https://arxiv.org/abs/1611.01462)).
- **Dynamic evaluation:** AWD-LSTM-MoS + dynamic evaluation at 47.69 ([Yang et al., 2018](https://arxiv.org/abs/1711.03953)); AWD-LSTM + dynamic evaluation at 51.1 ([Yang et al., 2018](https://arxiv.org/abs/1711.03953)).

## Principal Finding

The lowest qualifying value in the supplied material is **54.44 word-level PTB test perplexity**, reported by Yang, Dai, Salakhutdinov, and Cohen for **AWD-LSTM-MoS with fine-tuning but without dynamic evaluation**, together with 55.97 for the same model without fine-tuning ([Yang et al., 2018](https://arxiv.org/abs/1711.03953)). Critically, the answer is robust to the treatment of fine-tuning: even the *no-fine-tuning* variant (55.97) remains lower than every other qualifying single-model number in the corpus. The paper also reports 47.69 with dynamic evaluation, but that figure is excluded under the stated criteria ([Yang et al., 2018](https://arxiv.org/abs/1711.03953)).

## Ranking of Papers by Lowest Qualifying PTB Word-Level Test Perplexity

| Rank | Paper (Source ID) | Lowest qualifying single-model test PPL | Configuration | Dynamic eval / cache / ensemble? | Fine-tuning? |
|------|-------------------|------------------------------------------|---------------|----------------------------------|--------------|
| 1 | Yang et al., 2018 ([1711.03953](https://arxiv.org/abs/1711.03953)) | **54.44** (55.97 without finetune) | AWD-LSTM-MoS, 22M params | No | Yes (54.44); No (55.97) |
| 2 | Merity et al., 2018 ([1708.02182](https://arxiv.org/abs/1708.02182)) | 57.3 (58.8 without finetune) | AWD-LSTM, 3-layer tied LSTM, 24M | No | Yes (57.3); No (58.8) |
| 3 | Melis et al., 2018 ([1707.05589](https://arxiv.org/abs/1707.05589)) | 58.3 | 4-layer LSTM with down-projection, 24M | No | Not reported |
| 4 | Zoph & Le, 2017 ([1611.01578](https://arxiv.org/abs/1611.01578)) | 62.4 | NAS cell, base 8 + shared embeddings, 54M | No | Not reported |
| 5 | Zilly et al., 2017 ([1607.03474](https://arxiv.org/abs/1607.03474)) | 65.4 | Variational RHN + WT, 23M | No | Not reported |
| 6 | Inan et al., 2017 ([1611.01462](https://arxiv.org/abs/1611.01462)) | 66.0 (VD-RHN+RE); own large model listed at 68.5 | Reused-embedding RHN / VD-LSTM+REAL (large), 51M | No | Not reported |
| 7 | Gal & Ghahramani, 2016 ([1512.05287](https://arxiv.org/abs/1512.05287)) | 73.4 | Large Variational LSTM, untied weights, MC dropout | No | Not reported |
| 8 | Press & Wolf, 2017 ([1608.05859](https://arxiv.org/abs/1608.05859)) | 74.3 | Large NNLM + weight tying, 51M | No | Not reported |
| 9 | Zaremba et al., 2014 ([1409.2329](https://arxiv.org/abs/1409.2329)) | 78.4 | Large regularized LSTM, 2 layers | No | Not reported (dropout-based regularization) |
| 10 | Kim et al., 2016 ([1508.06615](https://arxiv.org/abs/1508.06615)) | 78.9 | LSTM-Char-Large (character CNN + highway LSTM) | No | Not reported |
| 11 | GRURNTN/LSTMRNTN paper ([1706.02222](https://arxiv.org/abs/1706.02222)) | 87.38 | GRURNTN (proposed) | No | Not reported |

## Detailed Discussion by Rank

### Rank 1 — Yang et al. (2018): 54.44 / 55.97

Yang et al. frame language modeling as matrix factorization and argue that softmax-based models suffer from a "Softmax bottleneck," motivating the Mixture of Softmaxes (MoS) architecture ([Yang et al., 2018](https://arxiv.org/abs/1711.03953)). In Table 1, they report 55.97 test perplexity for AWD-LSTM-MoS without fine-tuning and 54.44 with fine-tuning, both explicitly labeled as single-model results; the 47.69 figure incorporates dynamic evaluation and is therefore excluded here ([Yang et al., 2018](https://arxiv.org/abs/1711.03953)). The model has roughly 22M parameters, comparable to the 24M baselines it outperforms, and the paper states that with comparable parameter counts MoS outperforms all baselines "with or without dynamic evaluation" ([Yang et al., 2018](https://arxiv.org/abs/1711.03953)). Notably, the paper's own comparison table lists Merity et al.'s AWD-LSTM at 57.3 and the no-fine-tune ablation at 58.8, confirming that the 54.44/55.97 results sit strictly below the previous best single-model entries ([Yang et al., 2018](https://arxiv.org/abs/1711.03953)).

### Rank 2 — Merity et al. (2018): 57.3 (58.8 without fine-tuning)

The AWD-LSTM ("ASGD Weight-Dropped LSTM") paper reports 57.3 test perplexity for a 3-layer tied LSTM with 24M parameters under a Table 1 caption that explicitly states "Single model perplexity on validation and test sets for the Penn Treebank language modeling task" ([Merity et al., 2018](https://arxiv.org/abs/1708.02182)). The paper attributes an improvement of approximately 1 perplexity unit over the previous state of the art on PTB and reports that fine-tuning removal degrades performance to 58.8 ([Merity et al., 2018](https://arxiv.org/abs/1708.02182)). Adding the continuous cache pointer reduces test perplexity further to 52.8, but that variant is excluded by the query's cache/pointer criterion; the paper does not report dynamic evaluation or ensemble results ([Merity et al., 2018](https://arxiv.org/abs/1708.02182)).

### Rank 3 — Melis et al. (2018): 58.3

Melis et al. conduct a rigorous re-evaluation of evaluation practice and report 58.3 test perplexity for a 4-layer LSTM with 24M parameters on PTB ([Melis et al., 2018](https://arxiv.org/abs/1707.05589)). The authors explicitly state that the result is for a single model "without dynamic evaluation, cache/pointer, ensemble, or fine-tuning" and that they deliberately refrain from including techniques known to push perplexities lower, because their aim is fair architecture comparison ([Melis et al., 2018](https://arxiv.org/abs/1707.05589)). This makes 58.3 arguably the cleanest "no-extra-techniques" reference point in the corpus, even though it is not the lowest number overall. The paper also notes down-projection improved PTB results by roughly 2–5 perplexity points at some depths ([Melis et al., 2018](https://arxiv.org/abs/1707.05589)).

### Rank 4 — Zoph and Le (2017): 62.4

The Neural Architecture Search (NAS) paper reports 62.4 test perplexity for a recurrent cell discovered by reinforcement learning, using base 8 with shared embeddings and 54M parameters; alternative configurations yield 64.0 (25M) and 67.9 (32M) ([Zoph & Le, 2017](https://arxiv.org/abs/1611.01578)). These are single-model test perplexities without dynamic evaluation, cache/pointer, ensemble, or fine-tuning, and the paper states the cell is 3.6 perplexity better than the previous state of the art, identified as Zilly et al.'s Variational RHN with shared embeddings at 66.0 ([Zoph & Le, 2017](https://arxiv.org/abs/1611.01578)). Cache/pointer appears in that table only as a baseline label ([Zoph & Le, 2017](https://arxiv.org/abs/1611.01578)).

### Rank 5 — Zilly et al. (2017): 65.4

Recurrent Highway Networks with variational dropout and weight tying (Variational RHN + WT) achieve 67.9/65.4 validation/test perplexity with 23M parameters; the same architecture without weight tying reports 68.5 test perplexity ([Zilly et al., 2017](https://arxiv.org/abs/1607.03474)). The best PTB result is a single model, and the paper reports no dynamic evaluation, cache/pointer, ensemble, or fine-tuning for its proposed model—cache and pointer methods appear only as baselines and ensembles only in comparison ([Zilly et al., 2017](https://arxiv.org/abs/1607.03474)). The authors claim RHNs outperform most single models as well as all previous ensembles ([Zilly et al., 2017](https://arxiv.org/abs/1607.03474)).

### Rank 6 — Inan et al. (2017): 66.0 reported; own large model listed at 68.5

Inan et al. propose a loss framework that ties input embeddings and output projections, reporting that VD-RHN+RE (a Variational RHN trained with reused embeddings, following Zilly et al.'s architecture) reaches 68.1 validation / 66.0 test perplexity, which the paper describes as "best overall" ([Inan et al., 2017](https://arxiv.org/abs/1611.01462)). Attribution here requires care: the same 66.0 figure appears in Press and Wolf's Table 5 as "RHN + BD + WT" attributed to Zilly et al. (2016), with 24M parameters ([Press & Wolf, 2017](https://arxiv.org/abs/1608.05859)), indicating that 66.0 corresponds to the RHN family with tied/shared embeddings rather than a uniquely new Inan et al. architecture. For Inan et al.'s own proposed model, the third-party NAS comparison table lists "Inan et al. 2016 – VD-LSTM + REAL (large)," 51M parameters, at 68.5 test perplexity ([Zoph & Le, 2017](https://arxiv.org/abs/1611.01578)). The paper's own PTB table entries supplied in the source material include small-model rows in the 138–159 range whose exact column semantics are not fully specified, so 68.5 is the most defensible single-model figure for the paper's own large configuration ([Inan et al., 2017](https://arxiv.org/abs/1611.01462); [Zoph & Le, 2017](https://arxiv.org/abs/1611.01578)). The paper's baseline list explicitly includes cache/pointer and ensemble entries (RNN+LDA+KN-5+Cache 92.0; Pointer Sentinel-LSTM medium 70.9; 38 Large LSTMs 68.7; 10 Large VD-LSTMs 68.7), all excluded here ([Inan et al., 2017](https://arxiv.org/abs/1611.01462)).

### Rank 7 — Gal and Ghahramani (2016): 73.4

The Variational LSTM paper reports 73.4 test perplexity for the large model with untied weights and MC dropout, reduced from Zaremba et al.'s 78.4; with weight tying the test result is 75.0 (or 74.1 with MC dropout) ([Gal & Ghahramani, 2016](https://arxiv.org/abs/1512.05287)). The paper's Table 1 caption identifies these as single-model perplexities on test and validation sets, and the text states these are the best single-model perplexities on PTB at the time ([Gal & Ghahramani, 2016](https://arxiv.org/abs/1512.05287)). No dynamic evaluation, cache, or pointer results are reported for PTB; the only ensemble reported is the 10-model combination that improves Zaremba's 69.5 to 68.7 ([Gal & Ghahramani, 2016](https://arxiv.org/abs/1512.05287)).

### Rank 8 — Press and Wolf (2017): 74.3

Press and Wolf report 74.3 test perplexity for a large NNLM with weight tying (51M parameters) and 100.9 for a small NNLM with weight tying plus projection regularization, both single-model and without dynamic evaluation, cache/pointer, ensemble, or fine-tuning ([Press & Wolf, 2017](https://arxiv.org/abs/1608.05859)). The large weight-tied model improves on the 78.4 baseline of Zaremba et al., and the small model improves on the 114.5 small-model baseline ([Press & Wolf, 2017](https://arxiv.org/abs/1608.05859)).

### Rank 9 — Zaremba et al. (2014): 78.4

The regularized LSTM paper reports single-model test perplexities of 82.7 (medium) and 78.4 (large), both lower than the single-model baselines it lists: Pascanu et al. (107.5), Cheng et al. (100.0), and a non-regularized LSTM (114.5) ([Zaremba et al., 2014](https://arxiv.org/abs/1409.2329)). The paper reports no dynamic evaluation, cache/pointer, or fine-tuning settings; its best results are ensemble averages, which are excluded here ([Zaremba et al., 2014](https://arxiv.org/abs/1409.2329)).

### Rank 10 — Kim et al. (2016): 78.9

The character-aware language model reports LSTM-Char-Large at 78.9 and LSTM-Char-Small at 92.3, both single-model word-level predictions ([Kim et al., 2016](https://arxiv.org/abs/1508.06615)). The paper explicitly excludes ensembles as not comparable, and reports no dynamic evaluation, cache/pointer, or fine-tuning on PTB ([Kim et al., 2016](https://arxiv.org/abs/1508.06615)). It achieves results on par with the then state of the art with roughly 60% fewer parameters ([Kim et al., 2016](https://arxiv.org/abs/1508.06615)).

### Rank 11 — GRURNTN/LSTMRNTN paper: 87.38

The recurrent neural tensor network paper reports 87.38 for GRURNTN and 96.97 for LSTMRNTN as individual models, against its own baselines GRURNN (97.78) and LSTMRNN (108.26); it explicitly states the experiments did not use dynamic evaluation ([1706.02222](https://arxiv.org/abs/1706.02222)). The listed comparison entries include an RNNLM with dynamic evaluation (123.2 vs. 124.7 without), confirming that dynamic evaluation is a distinct reported setting not applied to the proposed word-level results ([1706.02222](https://arxiv.org/abs/1706.02222)).

## Caveats and Limitations

Several qualifications temper the ranking. First, **fine-tuning status differs across entries**: the top two ranks include fine-tuned numbers (54.44 and 57.3), while their no-fine-tune variants (55.97 and 58.8) still preserve the same rank order ([Yang et al., 2018](https://arxiv.org/abs/1711.03953); [Merity et al., 2018](https://arxiv.org/abs/1708.02182)). Second, **parameter budgets are not equalized**: 22M (Yang), 24M (Merity; Melis), 54M (NAS), 23M (RHN), and 51M (Inan) differ substantially ([Zoph & Le, 2017](https://arxiv.org/abs/1611.01578); [Inan et al., 2017](https://arxiv.org/abs/1611.01462)). Third, **attribution ambiguity affects rank 6**, where 66.0 is credited to an RHN-family model with reused/tied embeddings rather than a novel cell ([Inan et al., 2017](https://arxiv.org/abs/1611.01462); [Press & Wolf, 2017](https://arxiv.org/abs/1608.05859)). Fourth, **training regimes and reported variances differ**, with only Gal and Ghahramani reporting standard deviations (e.g., 73.4 ± 0.0), while most others report single point estimates ([Gal & Ghahramani, 2016](https://arxiv.org/abs/1512.05287)). Finally, the corpus is not a complete census of the literature: several numbers appear only as third-party baselines within the supplied texts ([Yang et al., 2018](https://arxiv.org/abs/1711.03953); [Zoph & Le, 2017](https://arxiv.org/abs/1611.01578)).

## Conclusion

Within the provided source material, **Yang et al. (2018) report the lowest word-level Penn Treebank test perplexity for a single model without dynamic evaluation, cache, or pointer augmentation: 54.44 (with fine-tuning) and 55.97 (without fine-tuning), using AWD-LSTM-MoS** ([Yang et al., 2018](https://arxiv.org/abs/1711.03953)). The complete ordering is: Yang et al. (54.44) < Merity et al. (57.3) < Melis et al. (58.3) < Zoph and Le (62.4) < Zilly et al. (65.4) < Inan et al. (66.0/68.5) < Gal and Ghahramani (73.4) < Press and Wolf (74.3) < Zaremba et al. (78.4) < Kim et al. (78.9) < GRURNTN (87.38). The conclusion is robust because the winning paper's *less* favorable configuration (55.97, no fine-tuning) still beats the next-best qualifying result.

## References

Gal, Y., & Ghahramani, Z. (2016). *A theoretically grounded application of dropout in recurrent neural networks* [Variational LSTM]. arXiv. https://arxiv.org/abs/1512.05287

Inan, H., Khosravi, K., & Socher, R. (2017). *Tying word vectors and word classifiers: A loss framework for language modeling*. arXiv. https://arxiv.org/abs/1611.01462

Kim, Y., Jernite, Y., Sontag, D., & Rush, A. M. (2016). *Character-aware neural language models*. arXiv. https://arxiv.org/abs/1508.06615

Melis, G., Dyer, C., & Blunsom, P. (2018). *On the state of the art of evaluation in neural language models*. arXiv. https://arxiv.org/abs/1707.05589

Merity, S., Keskar, N. S., & Socher, R. (2018). *Regularizing and optimizing LSTM language models* [AWD-LSTM]. arXiv. https://arxiv.org/abs/1708.02182

Press, O., & Wolf, L. (2017). *Using the output embedding to improve language models*. arXiv. https://arxiv.org/abs/1608.05859

*Recurrent neural tensor networks for word-level and character-level language modeling* [GRURNTN and LSTMRNTN]. (2017). arXiv. https://arxiv.org/abs/1706.02222

Yang, Z., Dai, Z., Salakhutdinov, R., & Cohen, W. W. (2018). *Breaking the softmax bottleneck: A high-rank RNN language model*. arXiv. https://arxiv.org/abs/1711.03953

Zaremba, W., Sutskever, I., & Vinyals, O. (2014). *Recurrent neural network regularization*. arXiv. https://arxiv.org/abs/1409.2329

Zilly, J. G., Srivastava, R. K., Koutník, J., & Schmidhuber, J. (2017). *Recurrent highway networks*. arXiv. https://arxiv.org/abs/1607.03474

Zoph, B., & Le, Q. V. (2017). *Neural architecture search with reinforcement learning*. arXiv. https://arxiv.org/abs/1611.01578