# Lowest Single-Model Penn Treebank Word-Level Test Perplexity Without Dynamic Evaluation, Cache, or Pointer Augmentation: A Cross-Paper Ranking

## 1. Scope, Definitions, and Inclusion Criteria

The Penn Treebank (PTB) word-level language modeling task is the most frequently reported small-scale benchmark in the neural language modeling literature covered by the provided sources. It is based on the Mikolov et al. preprocessing with a vocabulary capped at 10,000 words and standard splits of roughly 929k training, 73k validation, and 82k test words ([Zaremba et al., 2014](https://arxiv.org/abs/1409.2329); [Melis et al., 2017](https://arxiv.org/abs/1707.05589)). Because reported PTB perplexities are highly sensitive to evaluation protocol, this report applies an explicit, narrow inclusion rule.

**Eligibility criteria applied to every candidate number:**

1. **Single model.** Only one trained network is evaluated. Averages over independently trained models (for example, Zaremba et al.'s averages of 2, 5, 10, and 38 LSTMs) are excluded as ensembles ([Zaremba et al., 2014](https://arxiv.org/abs/1409.2329)).
2. **No dynamic evaluation.** Methods that adapt the model or its predictions on the test set at inference time are excluded, such as the dynamic-evaluation results reported in the MoS paper ([Yang et al., 2017](https://arxiv.org/abs/1711.03953)).
3. **No cache or pointer augmentation.** The continuous cache pointer, neural cache, and pointer-sentinel mechanisms are excluded, even when they are applied to an otherwise eligible single model ([Merity et al., 2017](https://arxiv.org/abs/1708.02182)).
4. **Fine-tuning is admitted, but reported separately.** Fine-tuning is a training-time procedure rather than an inference-time augmentation, so the query's stated exclusions do not cover it. To make the ranking robust, both fine-tuned and non-fine-tuned single-model values are reported wherever the sources distinguish them.

Eleven of the provided papers report their own PTB word-level models and therefore qualify for ranking. All numerical values below are drawn from those papers' own tables and from the accompanying research notes.

## 2. Direct Answer

**The lowest eligible value is 54.44 word-level test perplexity on Penn Treebank, reported by Yang et al. (2017) in "Breaking the Softmax Bottleneck: A High-Rank RNN Language Model" for the AWD-LSTM-MoS model with fine-tuning** ([Yang et al., 2017](https://arxiv.org/abs/1711.03953)). The same model reaches 55.97 test perplexity without fine-tuning, and the paper's Table 1 caption identifies both numbers as "single model perplexity on validation and test sets on Penn Treebank" ([Yang et al., 2017](https://arxiv.org/abs/1711.03953)). Both figures are obtained without dynamic evaluation, without cache/pointer, and without ensembles.

This answer is robust to a stricter reading of the query: even if fine-tuning were disallowed, MoS at 55.97 would still be the lowest number among all eligible results, ahead of the 57.3 and 58.8 AWD-LSTM variants of Merity et al. (2017) and the 58.3 LSTM of Melis et al. (2017) ([Merity et al., 2017](https://arxiv.org/abs/1708.02182); [Melis et al., 2017](https://arxiv.org/abs/1707.05589)).

## 3. Ranked Results Table

The table ranks the eleven qualifying papers by their best eligible single-model word-level PTB test perplexity (lower is better).

| Rank | Paper | Best eligible test PPL | Model / setting | Parameters | Other eligible values reported |
|---|---|---|---|---|---|
| 1 | Yang et al. (2017), arXiv:1711.03953 | **54.44** (55.97 w/o fine-tuning) | AWD-LSTM-MoS | ≈22M | 55.97, 56.17, 56.33, 57.36, 58.62 across mixture counts |
| 2 | Merity et al. (2017), arXiv:1708.02182 | **57.3** (58.8 w/o fine-tuning) | AWD-LSTM, 3-layer, tied weights | 24M | 58.8 (no fine-tuning ablation) |
| 3 | Melis et al. (2017), arXiv:1707.05589 | **58.3** | 4-layer LSTM, shared embeddings | 24M | 62.2 (RHN), 59.7 (NAS) at 24M |
| 4 | Zoph & Le (2016), arXiv:1611.01578 | **62.4** | NAS recurrent cell, shared embeddings | 54M | 64.0 (25M), 67.9 (32M) |
| 5 | Zilly et al. (2016), arXiv:1607.03474 | **65.4** | Variational RHN + weight tying | 23–24M | 68.5 (no weight tying) |
| 6 | Inan et al. (2016), arXiv:1611.01462 | **66.0** | VD-RHN + reused embeddings (RE) | not stated | 68.5 (VD-LSTM + REAL, large, 51M) |
| 7 | Press & Wolf (2016), arXiv:1608.05859 | **73.2** (headline result 74.3) | Large + Bayesian dropout + weight tying | 51M | 74.3, 75.2 |
| 8 | Gal & Ghahramani (2015), arXiv:1512.05287 | **73.4** | Variational LSTM, untied weights, MC dropout | 66M | 74.1, 75.0, 75.2, 78.6, 79.0, 79.7 |
| 9 | Zaremba et al. (2014), arXiv:1409.2329 | **78.4** | Large regularized LSTM | 66M | 82.7 (medium) |
| 10 | Kim et al. (2015), arXiv:1508.06615 | **78.9** | LSTM-Char-Large, two highway layers | ≈19M | 92.3 (small), 79.7, 84.6, 90.1, 92.6, 100.3, 111.2 |
| 11 | GRURNTN (2017), arXiv:1706.02222 | **87.38** | GRURNTN | not stated | 96.97 (LSTMRNTN), 97.78 (GRURNN), 108.26 (LSTMRNN) |

For Zaremba et al., Kim et al. estimate the large LSTM at approximately 52M parameters, while later comparison tables list 66M ([Kim et al., 2015](https://arxiv.org/abs/1508.06615); [Zilly et al., 2016](https://arxiv.org/abs/1607.03474)).

## 4. Detailed Paper-by-Paper Analysis

### 4.1 Rank 1 — Yang et al. (2017): 54.44 (and 55.97 without fine-tuning)

The MoS paper formulates language modeling as matrix factorization and argues that standard softmax-based models suffer from a softmax bottleneck ([Yang et al., 2017](https://arxiv.org/abs/1711.03953)). Its Mixture of Softmaxes (MoS) model is evaluated on PTB and WikiText-2 using the regularization and optimization recipe of Merity et al. (2017). Table 1 lists 55.97 for AWD-LSTM-MoS without fine-tuning and 54.44 with fine-tuning; the same table also lists AWD-LSTM-MoS plus dynamic evaluation at 47.69, which is excluded here ([Yang et al., 2017](https://arxiv.org/abs/1711.03953)). A hyperparameter sweep over the number of mixture components shows a monotone improvement up to 15 mixtures: 3 mixtures give 58.62, 5 give 57.36, 10 give 56.33, 15 give 55.97 (the best), and 20 give 56.17 due to overfitting ([Yang et al., 2017](https://arxiv.org/abs/1711.03953)). The authors characterize 54.44/55.97 as substantially improving over the then-current state of the art by up to 3.6 perplexity points ([Yang et al., 2017](https://arxiv.org/abs/1711.03953)).

### 4.2 Rank 2 — Merity et al. (2017): 57.3

The AWD-LSTM paper reports a 3-layer, weight-tied LSTM with 24M parameters at 60.0 validation and 57.3 test perplexity, explicitly captioned as a single model ([Merity et al., 2017](https://arxiv.org/abs/1708.02182)). This result includes the fine-tuning step; the paper's Table 4 lists a no-fine-tuning ablation at 58.8 and states that removing fine-tuning degrades performance ([Merity et al., 2017](https://arxiv.org/abs/1708.02182)). The paper states that its vanilla LSTM beats the prior state of the art by approximately one perplexity unit on PTB, and in Table 1 the 57.3 figure sits below Melis et al.'s 4-layer skip-connection LSTM at 58.3 ([Merity et al., 2017](https://arxiv.org/abs/1708.02182)). Adding a continuous cache pointer lowers test perplexity further to 52.8, but that variant is excluded under criterion 3 ([Merity et al., 2017](https://arxiv.org/abs/1708.02182)).

### 4.3 Rank 3 — Melis et al. (2017): 58.3

Melis et al. re-evaluate several popular architectures with large-scale automatic black-box hyperparameter tuning and conclude that well-regularized standard LSTMs outperform more recent architectures ([Melis et al., 2017](https://arxiv.org/abs/1707.05589)). Their best PTB result is 58.3 test perplexity (60.9 validation) for a single 4-layer LSTM with 24M parameters and shared input/output embeddings ([Melis et al., 2017](https://arxiv.org/abs/1707.05589)). Their tuned RHN reaches 62.2 and their tuned NAS model 59.7 at the same budget ([Melis et al., 2017](https://arxiv.org/abs/1707.05589)). Crucially for this report, the authors explicitly state that all their results are for models "without dynamic evaluation or caching," and that they deliberately refrain from techniques that push perplexities lower in order to keep architecture comparisons fair ([Melis et al., 2017](https://arxiv.org/abs/1707.05589)). Their comparison table places the 58.3 result above all listed baselines except the parallel AWD-LSTM work at 57.3 ([Melis et al., 2017](https://arxiv.org/abs/1707.05589)).

### 4.4 Rank 4 — Zoph and Le (2016): 62.4

The Neural Architecture Search (NAS) paper uses reinforcement learning to design a recurrent cell for PTB ([Zoph & Le, 2016](https://arxiv.org/abs/1611.01578)). Table 2, captioned as "single model perplexity on the test set," reports 67.9 for NAS with base 8 (32M parameters), 64.0 for NAS with base 8 and shared embeddings (25M), and 62.4 for NAS with base 8 and shared embeddings (54M) ([Zoph & Le, 2016](https://arxiv.org/abs/1611.01578)). The paper states that 62.4 is 3.6 perplexity better than the previous state of the art and that the cell also transfers to character-level PTB language modeling with 1.214 perplexity ([Zoph & Le, 2016](https://arxiv.org/abs/1611.01578)). No dynamic evaluation, cache/pointer, ensemble, or fine-tuning result is reported for the NAS model on PTB; cache/pointer appears only among baseline labels such as Pointer Sentinel-LSTM ([Zoph & Le, 2016](https://arxiv.org/abs/1611.01578)).

### 4.5 Rank 5 — Zilly et al. (2016): 65.4

Recurrent Highway Networks extend the LSTM to allow transition depths greater than one ([Zilly et al., 2016](https://arxiv.org/abs/1607.03474)). The paper's best PTB result is 65.4 test perplexity (67.9 validation) for Variational RHN with weight tying, listed at 23M parameters in Table 1 and 24M in some comparisons, with variational dropout and tied input/output mappings ([Zilly et al., 2016](https://arxiv.org/abs/1607.03474)). Without weight tying, the Variational RHN reaches 68.5 ([Zilly et al., 2016](https://arxiv.org/abs/1607.03474)). Increasing recurrence depth from 1 to 10 at a fixed 32M parameter budget improves PTB perplexity from 90.6 to 65.4, and reducing weight decay further yields the 67.9/65.4 validation/test pair ([Zilly et al., 2016](https://arxiv.org/abs/1607.03474)). The best result is a single model; dynamic evaluation, cache/pointer, ensemble, and fine-tuning are not reported for the proposed model, and the paper states that RHNs outperform most single models as well as all previous ensembles ([Zilly et al., 2016](https://arxiv.org/abs/1607.03474)).

### 4.6 Rank 6 — Inan et al. (2016): 66.0

The "Tying Word Vectors and Word Classifiers" paper introduces a loss framework that ties the input embedding and output projection ([Inan et al., 2016](https://arxiv.org/abs/1611.01462)). Its best overall PTB result is reported as 66.0 test perplexity (68.1 validation) for a VD-RHN model trained with reused embeddings ([Inan et al., 2016](https://arxiv.org/abs/1611.01462)). The paper also reports VD-LSTM + REAL (large) at 51M parameters and 68.5 test perplexity, and small 200-unit VD-LSTM variants in the 138–149 test perplexity range ([Inan et al., 2016](https://arxiv.org/abs/1611.01462); [Zoph & Le, 2016](https://arxiv.org/abs/1611.01578)). Cache, pointer, and ensemble baselines appear in the paper only as comparison entries — RNN+LDA+KN-5+Cache at 92.0, Pointer Sentinel-LSTM (medium) at 70.9, 38 large LSTMs at 68.7, and 10 large VD-LSTMs at 68.7 — and are not the paper's own single-model results ([Inan et al., 2016](https://arxiv.org/abs/1611.01462)).

### 4.7 Ranks 7–8 — Press and Wolf (2016) at 73.2/74.3 and Gal and Ghahramani (2015) at 73.4

Press and Wolf show that tying the output embedding to the input embedding improves language models ([Press & Wolf, 2016](https://arxiv.org/abs/1608.05859)). Their headline large model, "Large + Weight Tying" (51M parameters), reaches 74.3 test perplexity, and their Table 5 also lists "Large + BD + WT" at 75.8 validation and 73.2 test ([Press & Wolf, 2016](https://arxiv.org/abs/1608.05859)). The 73.2 figure is corroborated externally: Zilly et al. cite "Variational LSTM + WT (Press & Wolf 2016)" at 51M with 75.8/73.2, which indicates that 73.2 is Press and Wolf's own best eligible result rather than a third-party number ([Zilly et al., 2016](https://arxiv.org/abs/1607.03474)). The paper's small model with weight tying and projection regularization reaches 100.9 test perplexity ([Press & Wolf, 2016](https://arxiv.org/abs/1608.05859)). No dynamic evaluation, cache/pointer, ensemble, or fine-tuning is reported.

Gal and Ghahramani's variational dropout work replicates Zaremba et al.'s setup and reports that test perplexity is reduced from 78.4 to 73.4 for the large model with Monte Carlo dropout and untied weights, which the authors describe as the best single-model perplexities on PTB at that time ([Gal & Ghahramani, 2015](https://arxiv.org/abs/1512.05287)). Their table lists a full ladder of single-model results: variational tied weights at 79.7 (medium) and 75.0 (large); variational tied weights with MC dropout at 79.0 and 74.1; variational untied weights at 79.7 and 75.2; and variational untied weights with MC dropout at 78.6 and 73.4 ([Gal & Ghahramani, 2015](https://arxiv.org/abs/1512.05287)). The paper's 10-model ensemble at 68.7 is excluded under criterion 1 ([Gal & Ghahramani, 2015](https://arxiv.org/abs/1512.05287)).

### 4.8 Ranks 9–11 — Zaremba et al. (2014) at 78.4, Kim et al. (2015) at 78.9, and GRURNTN (2017) at 87.38

Zaremba et al.'s regularized LSTMs reach 82.7 (medium) and 78.4 (large) word-level PTB test perplexity as single models, compared with 107.5 for Pascanu et al. (2013), 100.0 for Cheng et al., and 114.5 for a non-regularized LSTM ([Zaremba et al., 2014](https://arxiv.org/abs/1409.2329)). This paper is historically important because it established the medium/large LSTM protocol reused by Gal and Ghahramani, Zilly et al., and Kim et al. ([Gal & Ghahramani, 2015](https://arxiv.org/abs/1512.05287); [Kim et al., 2015](https://arxiv.org/abs/1508.06615)). The character-aware model of Kim et al. reaches 78.9 test perplexity with its large configuration using two highway layers and 92.3 with the small configuration, on par with the state of the art at roughly 60% fewer parameters ([Kim et al., 2015](https://arxiv.org/abs/1508.06615)). The paper explicitly excludes ensembles from its comparison, noting that lower perplexities have been reported with model ensembles but are not comparable ([Kim et al., 2015](https://arxiv.org/abs/1508.06615)). Finally, the gated recurrent neural tensor network paper reports GRURNTN at 87.38 and LSTMRNTN at 96.97 PTB test perplexity, with its own GRURNN (97.78) and LSTMRNN (108.26) baselines, and states that the experiments did not use dynamic evaluation ([GRURNTN, 2017](https://arxiv.org/abs/1706.02222)).

## 5. Lower Numbers That Do Not Qualify

Several numbers in the corpus are lower than 54.44 but fail at least one eligibility criterion, and stating them clarifies the boundary of the answer.

**Dynamic evaluation.** AWD-LSTM-MoS with dynamic evaluation reaches 47.69 ([Yang et al., 2017](https://arxiv.org/abs/1711.03953)), and the same table lists Krause et al.'s AWD-LSTM with dynamic evaluation at 51.1 ([Yang et al., 2017](https://arxiv.org/abs/1711.03953)). The GRURNTN paper lists RNNLM with dynamic evaluation at 123.2 versus 124.7 without ([GRURNTN, 2017](https://arxiv.org/abs/1706.02222)).

**Cache or pointer.** AWD-LSTM with a continuous cache pointer reaches 52.8 on PTB and 52.0 on WikiText-2 ([Merity et al., 2017](https://arxiv.org/abs/1708.02182)). The Neural Cache of Grave et al. is referenced by Melis et al. as a technique whose gains are orthogonal to the base model ([Melis et al., 2017](https://arxiv.org/abs/1707.05589)).

**Ensembles.** Zaremba et al.'s model averaging yields 77.0 (2 medium), 73.3 (5 medium), 72.0 (10 medium), 73.6 (2 large), 69.5 (10 large), and 68.7 (38 large) ([Zaremba et al., 2014](https://arxiv.org/abs/1409.2329)). Gal and Ghahramani's 10-model variational ensemble improves 69.5 to 68.7, matching the 38-model result ([Gal & Ghahramani, 2015](https://arxiv.org/abs/1512.05287)). Notably, these ensemble values for older architectures are worse than the best modern single models, which is a substantive finding rather than a technicality: ensembling pre-2016 architectures does not compensate for architectural and regularization improvements.

## 6. Interpretation and Caveats

Three interpretative points deserve emphasis. First, the ranking has a clear temporal gradient that reflects genuine methodological progress rather than noise: the eligible frontier moves from 82.7/78.4 (2014) to 73.4 (2015), 65.4 (2016), 62.4 (2016), 58.3 (2017), 57.3 (2017), and 54.44 (2017). Second, the winning entry, MoS, is not an architecture-replacement story alone; it applies the AWD-LSTM regularization and optimization recipe and adds a mixture-of-softmaxes output layer, so its gain is attributable to the output representation rather than to a new recurrent cell ([Yang et al., 2017](https://arxiv.org/abs/1711.03953); [Merity et al., 2017](https://arxiv.org/abs/1708.02182)).

Third, cross-paper comparison on PTB is confounded by differing codebases, hyperparameter budgets, and regularization combinations. Melis et al. make exactly this argument, noting that ongoing architectural innovations have been evaluated with differing codebases and limited computational resources, which are uncontrolled sources of experimental variation ([Melis et al., 2017](https://arxiv.org/abs/1707.05589)). This is visible in the data: Zilly et al. report 65.4 for Variational RHN with weight tying, while NAS and Inan et al. list 66.0 for the shared-embedding RHN as a baseline ([Zilly et al., 2016](https://arxiv.org/abs/1607.03474); [Zoph & Le, 2016](https://arxiv.org/abs/1611.01578); [Inan et al., 2016](https://arxiv.org/abs/1611.01462)). Likewise, parameter counts for the same nominal model differ across papers (52M versus 66M for Zaremba's large LSTM), and fine-tuning is inconsistently separated from the headline number — MoS reports both 54.44 and 55.97, while Merity et al. report both 57.3 and 58.8 ([Kim et al., 2015](https://arxiv.org/abs/1508.06615); [Yang et al., 2017](https://arxiv.org/abs/1711.03953); [Merity et al., 2017](https://arxiv.org/abs/1708.02182)). A disciplined reading therefore treats the ranks as a confidence-ordered frontier rather than as a precise, single-protocol leaderboard.

## 7. Conclusion

Within the provided corpus, and under the constraints of single model, no dynamic evaluation, and no cache or pointer augmentation, the lowest word-level Penn Treebank test perplexity is **54.44, reported by Yang et al. (2017) for AWD-LSTM-MoS with fine-tuning**, with **55.97 for the same model without fine-tuning** ([Yang et al., 2017](https://arxiv.org/abs/1711.03953)). The complete eligible ranking is Yang et al. (2017) at 54.44/55.97, Merity et al. (2017) at 57.3/58.8, Melis et al. (2017) at 58.3, Zoph and Le (2016) at 62.4, Zilly et al. (2016) at 65.4, Inan et al. (2016) at 66.0, Press and Wolf (2016) at 73.2/74.3, Gal and Ghahramani (2015) at 73.4, Zaremba et al. (2014) at 78.4, Kim et al. (2015) at 78.9, and GRURNTN (2017) at 87.38. The answer is invariant to whether fine-tuning is permitted, and the excluded techniques — dynamic evaluation (47.69), continuous cache pointers (52.8), and ensembles (68.7 and above) — are the only mechanisms in the corpus that produce lower numbers than the winning single model.

## References

Gal, Y., & Ghahramani, Z. (2015). *A theoretically grounded application of dropout in recurrent neural networks* [arXiv:1512.05287]. arXiv. https://arxiv.org/abs/1512.05287

*Gated recurrent neural tensor network* [arXiv:1706.02222]. (2017). arXiv. https://arxiv.org/abs/1706.02222

Inan, H., Khosravi, K., & Socher, R. (2016). *Tying word vectors and word classifiers: A loss framework for language modeling* [arXiv:1611.01462]. arXiv. https://arxiv.org/abs/1611.01462

Kim, Y., Jernite, Y., Sontag, D., & Rush, A. M. (2015). *Character-aware neural language models* [arXiv:1508.06615]. arXiv. https://arxiv.org/abs/1508.06615

Melis, G., Dyer, C., & Blunsom, P. (2017). *On the state of the art of evaluation in neural language models* [arXiv:1707.05589]. arXiv. https://arxiv.org/abs/1707.05589

Merity, S., Keskar, N. S., & Socher, R. (2017). *Regularizing and optimizing LSTM language models* [arXiv:1708.02182]. arXiv. https://arxiv.org/abs/1708.02182

Press, O., & Wolf, L. (2016). *Using the output embedding to improve language models* [arXiv:1608.05859]. arXiv. https://arxiv.org/abs/1608.05859

Yang, Z., Dai, Z., Salakhutdinov, R., & Cohen, W. W. (2017). *Breaking the softmax bottleneck: A high-rank RNN language model* [arXiv:1711.03953]. arXiv. https://arxiv.org/abs/1711.03953

Zaremba, W., Sutskever, I., & Vinyals, O. (2014). *Recurrent neural network regularization* [arXiv:1409.2329]. arXiv. https://arxiv.org/abs/1409.2329

Zilly, J. G., Srivastava, R. K., Koutník, J., & Schmidhuber, J. (2016). *Recurrent highway networks* [arXiv:1607.03474]. arXiv. https://arxiv.org/abs/1607.03474

Zoph, B., & Le, Q. V. (2016). *Neural architecture search with reinforcement learning* [arXiv:1611.01578]. arXiv. https://arxiv.org/abs/1611.01578