# CHIM Variant Performance on Accuracy: A Detailed Analysis of Reported Improvements

## Introduction

This report addresses the query: Which of the authors' CHIM variants performs best on accuracy, and by how much does it improve on each dataset? The analysis is based exclusively on the provided source excerpt from the paper titled "Rethinking Attribute Representation and Injection for Sentiment Classification" (arXiv:1908.09590), specifically the section "Experiments :: Comparisons with models in the literature" ([document_1.txt, n.d.](https://arxiv.org/abs/1908.09590)). The source reports results on three datasets: IMDB, Yelp 2013, and Yelp 2014. It compares the authors' models against previous models in the literature using two metrics: accuracy and RMSE ([document_1.txt, n.d.](https://arxiv.org/abs/1908.09590)).

The central finding from the excerpt is unambiguous: among the authors' models, CHIM-embedding performs best in terms of accuracy. The reported performance increases are 2.4% on IMDB, 1.3% on Yelp 2013, and 1.6% on Yelp 2014 ([document_1.txt, n.d.](https://arxiv.org/abs/1908.09590)). In contrast, CHIM-classifier performs best in terms of RMSE, while CHIM-attention performs worst among the models ([document_1.txt, n.d.](https://arxiv.org/abs/1908.09590)). This report will elaborate on these findings, compare the variants, provide dataset-specific breakdowns, and discuss the implications and limitations of the available information.

## Background and Experimental Context

The paper investigates attribute representation and injection for sentiment classification ([document_1.txt, n.d.](https://arxiv.org/abs/1908.09590)). The authors propose multiple CHIM variants and evaluate them on three widely used datasets. The excerpt does not define the full form of CHIM or describe the internal architecture of each variant. However, it does name three CHIM variants: CHIM-embedding, CHIM-classifier, and CHIM-attention ([document_1.txt, n.d.](https://arxiv.org/abs/1908.09590)). It also refers to "our four models," which suggests that there may be a fourth model or variant not named in the provided excerpt ([document_1.txt, n.d.](https://arxiv.org/abs/1908.09590)). Because the query specifically concerns CHIM variants, this report focuses on the three variants that are explicitly identified.

The experimental comparison covers both accuracy and RMSE. The source states that on all three datasets, the authors' best results outperform all previous models based on accuracy and RMSE ([document_1.txt, n.d.](https://arxiv.org/abs/1908.09590)). This overall claim establishes the competitive strength of the proposed approach. Within that broader success, the authors separately identify which variant is best for accuracy and which is best for RMSE ([document_1.txt, n.d.](https://arxiv.org/abs/1908.09590)).

## Main Finding: CHIM-Embedding Leads on Accuracy

The direct answer to the query is that CHIM-embedding is the authors' best-performing CHIM variant on accuracy ([document_1.txt, n.d.](https://arxiv.org/abs/1908.09590)). The excerpt states: "Among our four models, CHIM-embedding performs the best in terms of accuracy, with performance increases of 2.4%, 1.3%, and 1.6% on IMDB, Yelp 2013, and Yelp 2014, respectively" ([document_1.txt, n.d.](https://arxiv.org/abs/1908.09590)). This statement directly identifies CHIM-embedding as the top accuracy variant and quantifies its improvements across the three datasets.

The increases are reported in the order IMDB, Yelp 2013, and Yelp 2014. Therefore, the improvement is 2.4% on IMDB, 1.3% on Yelp 2013, and 1.6% on Yelp 2014 ([document_1.txt, n.d.](https://arxiv.org/abs/1908.09590)). These figures represent the performance gains associated with the authors' best results relative to previous models in the literature ([document_1.txt, n.d.](https://arxiv.org/abs/1908.09590)). The excerpt does not clarify whether the percentages are absolute percentage-point gains or relative percentage improvements. It also does not provide the underlying absolute accuracy scores. Nevertheless, the reported values are the only quantitative accuracy improvements available in the source, and they consistently favor CHIM-embedding as the leading accuracy-oriented variant.

### Dataset-by-Dataset Breakdown

#### IMDB

On the IMDB dataset, CHIM-embedding achieves the largest reported accuracy improvement of the three datasets: 2.4% ([document_1.txt, n.d.](https://arxiv.org/abs/1908.09590)). This is the highest gain among the three, indicating that the advantage of CHIM-embedding over previous models is most pronounced on IMDB according to the excerpt. The source does not explain why IMDB shows the largest improvement, nor does it provide additional statistics such as variance or significance tests.

#### Yelp 2013

On Yelp 2013, CHIM-embedding achieves a reported accuracy improvement of 1.3% ([document_1.txt, n.d.](https://arxiv.org/abs/1908.09590)). This is the smallest of the three reported improvements. Even so, it remains a positive gain and contributes to the overall claim that the authors' best results outperform previous models on all three datasets ([document_1.txt, n.d.](https://arxiv.org/abs/1908.09590)). The smaller improvement on Yelp 2013 may suggest that previous models were already relatively stronger on this dataset, but the excerpt does not offer an explanation.

#### Yelp 2014

On Yelp 2014, CHIM-embedding achieves a reported accuracy improvement of 1.6% ([document_1.txt, n.d.](https://arxiv.org/abs/1908.09590)). This gain falls between the IMDB and Yelp 2013 improvements. It reinforces the pattern that CHIM-embedding provides consistent positive improvements across all three datasets, with the magnitude varying by dataset ([document_1.txt, n.d.](https://arxiv.org/abs/1908.09590)).

A summary of these results is presented in Table 1.

**Table 1. Reported accuracy improvements of CHIM-embedding across datasets**

| Dataset | Best CHIM variant for accuracy | Reported accuracy improvement |
|---|---|---|
| IMDB | CHIM-embedding | 2.4% |
| Yelp 2013 | CHIM-embedding | 1.3% |
| Yelp 2014 | CHIM-embedding | 1.6% |

Note: Data from ([document_1.txt, n.d.](https://arxiv.org/abs/1908.09590)).

## Comparative View of CHIM Variants

To fully answer the query, it is useful to place CHIM-embedding in the context of the other CHIM variants. The excerpt provides a clear qualitative ranking for two metrics. CHIM-embedding is best for accuracy, CHIM-classifier is best for RMSE, and CHIM-attention is worst among the authors' models ([document_1.txt, n.d.](https://arxiv.org/abs/1908.09590)). This indicates a metric-dependent trade-off: no single variant dominates on both accuracy and RMSE according to the provided information.

**Table 2. Qualitative performance ranking of CHIM variants**

| CHIM variant | Best metric | Relative standing |
|---|---|---|
| CHIM-embedding | Accuracy | Best among authors' models for accuracy |
| CHIM-classifier | RMSE | Best among authors' models for RMSE |
| CHIM-attention | Neither | Worst among authors' models |

Note: Data from ([document_1.txt, n.d.](https://arxiv.org/abs/1908.09590)).

The fact that CHIM-embedding is best on accuracy but not necessarily best on RMSE suggests that the variant may be particularly effective at classification decisions rather than rating error minimization. However, the excerpt does not provide architectural details or ablation results that would explain why this occurs ([document_1.txt, n.d.](https://arxiv.org/abs/1908.09590)). Similarly, CHIM-classifier's best RMSE performance does not imply that it is best for accuracy. The excerpt explicitly separates these two outcomes, and researchers should avoid conflating them.

The statement that CHIM-attention performs worst is also notable. It suggests that the attention-based variant, at least in the form evaluated here, did not yield the strongest results on these datasets according to the provided excerpt ([document_1.txt, n.d.](https://arxiv.org/abs/1908.09590)). This is a negative but useful finding: it helps narrow the design space for attribute representation and injection in sentiment classification. The excerpt does not specify whether "worst" refers to accuracy, RMSE, or both, but the sentence appears in a discussion of the authors' models generally ([document_1.txt, n.d.](https://arxiv.org/abs/1908.09590)). Therefore, the safest interpretation is that CHIM-attention is the weakest of the authors' models overall in the reported comparisons.

## Significance and Interpretation

The reported improvements are meaningful for several reasons. First, they are consistent across all three datasets: CHIM-embedding improves accuracy on IMDB, Yelp 2013, and Yelp 2014 ([document_1.txt, n.d.](https://arxiv.org/abs/1908.09590)). Consistency across multiple datasets strengthens the generalizability of the finding, at least within the scope of the experiments. Second, the authors' best results outperform all previous models on both accuracy and RMSE ([document_1.txt, n.d.](https://arxiv.org/abs/1908.09590)). This suggests that the CHIM framework as a whole is competitive with the state of the art, even though different variants excel on different metrics.

Third, the magnitude of the accuracy gains varies by dataset. IMDB shows the largest improvement at 2.4%, followed by Yelp 2014 at 1.6%, and Yelp 2013 at 1.3% ([document_1.txt, n.d.](https://arxiv.org/abs/1908.09590)). This variation may reflect differences in dataset characteristics, baseline strength, or the interaction between attribute representation and injection mechanisms. The provided excerpt does not offer a causal explanation, so any interpretation beyond the reported numbers would be speculative. What can be stated confidently is that CHIM-embedding is the best accuracy variant, and its improvements are positive on every dataset tested.

From a practical standpoint, the answer to the query has clear implications. If the goal is to maximize accuracy in sentiment classification on these datasets, CHIM-embedding is the recommended variant among those named in the excerpt ([document_1.txt, n.d.](https://arxiv.org/abs/1908.09590)). If the goal is to minimize RMSE, CHIM-classifier would be preferred based on the same source ([document_1.txt, n.d.](https://arxiv.org/abs/1908.09590)). CHIM-attention would not be the first choice for either metric based on the reported rankings. These recommendations are limited to the specific datasets and experimental setup described in the paper.

## Methodological Caveats and Limitations

The provided excerpt is informative but incomplete. It does not report absolute accuracy values, RMSE values, standard deviations, confidence intervals, or statistical significance tests ([document_1.txt, n.d.](https://arxiv.org/abs/1908.09590)). As a result, it is not possible to determine whether the reported improvements are statistically significant or whether they would generalize beyond the tested datasets. The excerpt also does not define the CHIM variants in detail, describe their architectures, or explain why CHIM-embedding performs best on accuracy ([document_1.txt, n.d.](https://arxiv.org/abs/1908.09590)). It refers to "our four models" but only names three CHIM variants, leaving ambiguity about the fourth model ([document_1.txt, n.d.](https://arxiv.org/abs/1908.09590)). Finally, the source does not specify whether the reported increases are absolute percentage points or relative percentages ([document_1.txt, n.d.](https://arxiv.org/abs/1908.09590)). These limitations should be kept in mind when interpreting the findings.

Despite these caveats, the excerpt provides a direct and unambiguous answer to the query. The best CHIM variant for accuracy is CHIM-embedding, and its reported improvements are 2.4% on IMDB, 1.3% on Yelp 2013, and 1.6% on Yelp 2014 ([document_1.txt, n.d.](https://arxiv.org/abs/1908.09590)). The ranking of variants for RMSE is also clear: CHIM-classifier is best, and CHIM-attention is worst ([document_1.txt, n.d.](https://arxiv.org/abs/1908.09590)). These findings are consistent with the overall claim that the authors' best results outperform previous models on both metrics.

## Conclusion

In summary, the authors' CHIM-embedding variant performs best on accuracy among the CHIM variants described in the provided excerpt ([document_1.txt, n.d.](https://arxiv.org/abs/1908.09590)). It improves performance by 2.4% on IMDB, 1.3% on Yelp 2013, and 1.6% on Yelp 2014 ([document_1.txt, n.d.](https://arxiv.org/abs/1908.09590)). CHIM-classifier performs best on RMSE, while CHIM-attention performs worst among the authors' models ([document_1.txt, n.d.](https://arxiv.org/abs/1908.09590)). On all three datasets, the authors' best results outperform all previous models on accuracy and RMSE ([document_1.txt, n.d.](https://arxiv.org/abs/1908.09590)). The answer to the query is therefore that CHIM-embedding is the accuracy leader, with dataset-specific gains of 2.4%, 1.3%, and 1.6% on IMDB, Yelp 2013, and Yelp 2014, respectively. These conclusions are based solely on the provided source excerpt and are subject to the limitations noted above.

## References

document_1.txt. (n.d.). *Rethinking Attribute Representation and Injection for Sentiment Classification* (arXiv:1908.09590). Retrieved from https://arxiv.org/abs/1908.09590