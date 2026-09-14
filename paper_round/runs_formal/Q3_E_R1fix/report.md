# Quantifying the Improvement of an Embedding-Based Semantic Similarity Measure over BM25 in PubMed Query Mapping

## Introduction

The query asks by how much the embedding-based similarity measure described in the source outperforms BM25. The provided information comes from the TREC Experiments section of *Bridging the Gap: Incorporating a Semantic Similarity Measure for Effectively Mapping PubMed Queries to Documents* (arXiv:1608.01972). According to that source, the embedding approach boosts the average precision of BM25 by 19% on TREC 2006 and by 6% on TREC 2007 ([document_1.txt, 2016](https://arxiv.org/abs/1608.01972)). These two figures constitute the direct answer to the query. The same source also reports that BM25 performs better than TFIDF and CENTROID, and that CENTROID produces scores lower than BM25 and SEM approaches ([document_1.txt, 2016](https://arxiv.org/abs/1608.01972)). Therefore, the embedding approach’s advantage over BM25 is positive in both reported TREC evaluations, but it is not uniform across datasets.

The purpose of this report is to present that answer in a structured, detailed, and unbiased manner. It examines the exact reported percentages, places them in the context of the other retrieval methods compared in the source, discusses the implications and limitations of the evidence, and concludes with a clear statement of what can and cannot be inferred from the provided information. Because the source excerpt is brief, the report relies strictly on the numbers and comparative statements contained in it.

## Direct Answer to the Query

### Reported Improvement over BM25

The most direct answer is that the embedding approach outperforms BM25 by 19% in average precision on TREC 2006 and by 6% in average precision on TREC 2007 ([document_1.txt, 2016](https://arxiv.org/abs/1608.01972)). The source phrases these as boosts to BM25’s average precision, which means the embedding approach improves upon the BM25 baseline rather than merely matching it. The two percentages are relative improvements over BM25, not absolute average precision scores. The source does not provide the underlying absolute average precision values for BM25 or for the embedding approach in the excerpt provided. Consequently, the answer should be reported as a relative gain: +19% on TREC 2006 and +6% on TREC 2007.

### Why the Two Numbers Matter

The difference between 19% and 6% is substantial. On TREC 2006, the embedding approach yields a nearly one-fifth relative increase in average precision over BM25, whereas on TREC 2007 the gain is a more modest but still positive 6% ([document_1.txt, 2016](https://arxiv.org/abs/1608.01972)). This dataset-dependent pattern suggests that the benefit of the semantic similarity measure varies with the query set or collection used in each TREC cycle. That interpretation is consistent with the source’s decision to report results separately for TREC 2006 and TREC 2007 rather than as a single aggregated number ([document_1.txt, 2016](https://arxiv.org/abs/1608.01972)). The positive direction of both results, however, indicates that the embedding approach does not lose to BM25 on either evaluation.

## Structured Presentation of the Results

The following table summarizes the quantitative comparison provided in the source.

| Dataset | Baseline | Embedding Approach Improvement | Additional Comparative Note |
|---|---|---|---|
| TREC 2006 | BM25 | +19% average precision | BM25 performs better than TFIDF and CENTROID; CENTROID is lower than BM25 and SEM |
| TREC 2007 | BM25 | +6% average precision | Same baseline and comparison pattern as reported for the TREC experiments |

*Note.* All figures and comparative statements are drawn from the TREC Experiments section of the source ([document_1.txt, 2016](https://arxiv.org/abs/1608.01972)). The table does not include absolute average precision values because the provided information does not report them.

## Detailed Breakdown by Dataset

### TREC 2006 Result

On TREC 2006, the embedding approach boosts BM25’s average precision by 19% ([document_1.txt, 2016](https://arxiv.org/abs/1608.01972)). This is the largest reported gain in the provided information. The source does not break this 19% down into per-query or per-topic results, nor does it report the absolute average precision values that would allow a reader to compute the raw difference ([document_1.txt, 2016](https://arxiv.org/abs/1608.01972)). Nevertheless, the 19% figure clearly indicates a substantial relative improvement over BM25 on that dataset. It suggests that, for the TREC 2006 queries and collection, the semantic similarity measure added considerable value beyond the lexical matching provided by BM25.

### TREC 2007 Result

On TREC 2007, the embedding approach boosts BM25’s average precision by 6% ([document_1.txt, 2016](https://arxiv.org/abs/1608.01972)). Although smaller than the TREC 2006 gain, this is still a positive improvement. The source does not explain why the gain is lower on TREC 2007, and the provided information does not include an analysis of query characteristics or collection differences ([document_1.txt, 2016](https://arxiv.org/abs/1608.01972)). The safe conclusion is that the embedding approach remains better than BM25 on both datasets, but the size of the advantage varies. A 6% relative gain is not negligible, but it is far less dramatic than the 19% gain observed on TREC 2006.

## Comparative Context among Retrieval Methods

The source positions the embedding approach against several baselines. First, BM25 performs better than TFIDF and CENTROID ([document_1.txt, 2016](https://arxiv.org/abs/1608.01972)). Second, the embedding approach boosts BM25’s average precision by 19% on TREC 2006 and 6% on TREC 2007 ([document_1.txt, 2016](https://arxiv.org/abs/1608.01972)). Third, CENTROID provides scores lower than BM25 and SEM approaches ([document_1.txt, 2016](https://arxiv.org/abs/1608.01972)). Taken together, these statements imply a performance ordering in which the embedding approach (SEM) is above BM25, BM25 is above TFIDF, and BM25 is also above CENTROID, while CENTROID is below SEM ([document_1.txt, 2016](https://arxiv.org/abs/1608.01972)). The source does not explicitly state that the embedding approach outperforms TFIDF, but because the embedding approach outperforms BM25 and BM25 outperforms TFIDF, the transitive conclusion is that the embedding approach also outperforms TFIDF in these experiments ([document_1.txt, 2016](https://arxiv.org/abs/1608.01972)). This makes the embedding approach the strongest method among those compared in the provided excerpt.

### BM25 as a Strong Baseline

The fact that the embedding approach improves over BM25 is meaningful because BM25 is itself reported as stronger than TFIDF and CENTROID ([document_1.txt, 2016](https://arxiv.org/abs/1608.01972)). In other words, the embedding approach is not merely beating a weak baseline. It is improving upon the best-performing baseline mentioned in the source. The reported 19% and 6% gains therefore represent improvements over a competitive lexical retrieval method rather than over a trivial alternative ([document_1.txt, 2016](https://arxiv.org/abs/1608.01972)). This strengthens the practical significance of the embedding approach for PubMed query-to-document mapping, although the source does not provide statistical significance tests or confidence intervals.

### The Meaning of “SEM”

The source uses the abbreviation “SEM” in the statement that CENTROID provides scores lower than BM25 and SEM approaches ([document_1.txt, 2016](https://arxiv.org/abs/1608.01972)). The query refers to “their similarity measure (the embedding approach),” and the same source states that the embedding approach boosts BM25’s average precision ([document_1.txt, 2016](https://arxiv.org/abs/1608.01972)). The provided excerpt does not explicitly define SEM, but the context strongly associates it with the embedding-based semantic similarity measure under evaluation. For the purpose of answering the query, the key quantitative result is the embedding approach’s improvement over BM25, which is 19% on TREC 2006 and 6% on TREC 2007 ([document_1.txt, 2016](https://arxiv.org/abs/1608.01972)).

## Interpretation and Implications

### Dataset-Dependent Gains

The central interpretive point is that the embedding approach’s advantage over BM25 is not constant. The 19% gain on TREC 2006 is more than three times the 6% gain on TREC 2007 ([document_1.txt, 2016](https://arxiv.org/abs/1608.01972)). This variation indicates that the semantic similarity measure may be more beneficial for certain query distributions or document collections than for others. Any claim that the embedding approach always improves BM25 by a single fixed percentage would be inconsistent with the reported evidence ([document_1.txt, 2016](https://arxiv.org/abs/1608.01972)). Instead, the correct summary is that the improvement ranges from 6% to 19% across the two TREC datasets examined.

### Relevance to PubMed Query Mapping

The source’s title identifies the task as effectively mapping PubMed queries to documents ([document_1.txt, 2016](https://arxiv.org/abs/1608.01972)). The TREC experiments are therefore relevant to biomedical literature retrieval, where queries may be short, technical, and semantically complex. The embedding approach’s improvement over BM25 suggests that incorporating a semantic similarity measure can help bridge vocabulary gaps that a purely lexical method such as BM25 might miss ([document_1.txt, 2016](https://arxiv.org/abs/1608.01972)). However, the provided excerpt does not include qualitative examples or error analyses, so the specific reasons for the gains cannot be verified from the available information.

### Practical Significance

For researchers or practitioners comparing retrieval methods, the reported numbers provide a clear benchmark: if BM25 is used as the baseline, an embedding-based semantic similarity measure can be expected to improve average precision by 19% on TREC 2006 and 6% on TREC 2007 in the reported setup ([document_1.txt, 2016](https://arxiv.org/abs/1608.01972)). This does not mean that the embedding approach will always produce such gains in every retrieval environment. It does mean that, within the source’s TREC experiments, the embedding approach consistently outperformed BM25 on the metric of average precision ([document_1.txt, 2016](https://arxiv.org/abs/1608.01972)). The consistency of the positive direction across two separate evaluation cycles is notable, even though the magnitude differs.

## Limitations and Caveats

Several limitations should be considered when interpreting the answer. First, the source reports only two TREC datasets: TREC 2006 and TREC 2007 ([document_1.txt, 2016](https://arxiv.org/abs/1608.01972)). Generalization to other TREC years, other biomedical collections, or non-PubMed domains is not established by the provided information. Second, the source reports relative percentage improvements but does not provide absolute average precision scores, statistical significance tests, or confidence intervals in the excerpt ([document_1.txt, 2016](https://arxiv.org/abs/1608.01972)). Without those details, the practical magnitude of the 19% and 6% gains cannot be fully assessed. Third, the source refers to Table 4 but the table itself is not included in the provided information, so the analysis relies on the textual summary rather than the full numerical table ([document_1.txt, 2016](https://arxiv.org/abs/1608.01972)). Fourth, the term SEM is used in the source’s comparative note, and while the query identifies the embedding approach as “their similarity measure,” the excerpt does not provide a full definition of SEM ([document_1.txt, 2016](https://arxiv.org/abs/1608.01972)). Finally, the source is an arXiv paper with a 2016 identifier, and the TREC data are from 2006 and 2007, so the results predate many recent developments in neural retrieval ([document_1.txt, 2016](https://arxiv.org/abs/1608.01972)). The findings should therefore be understood as historical benchmarks from that experimental setting rather than as a claim about current state-of-the-art performance.

### Relative versus Absolute Gains

The source reports relative improvements: 19% and 6% boosts to BM25’s average precision ([document_1.txt, 2016](https://arxiv.org/abs/1608.01972)). Without absolute scores, one cannot determine whether a 6% relative gain corresponds to a small or large absolute increase in average precision. This is a limitation of the provided excerpt. A complete assessment would require the baseline and experimental average precision values, as well as variance estimates. The source does not provide those values in the excerpt, so the answer must remain at the level of relative percentages ([document_1.txt, 2016](https://arxiv.org/abs/1608.01972)).

### Generalization

The two TREC datasets provide a limited basis for generalization. TREC 2006 and TREC 2007 are separate evaluation cycles, and the source reports different gains for each ([document_1.txt, 2016](https://arxiv.org/abs/1608.01972)). This suggests that the embedding approach’s advantage over BM25 is not a fixed constant. Researchers should therefore avoid citing a single number, such as 19%, as if it applied universally. The more accurate statement is that the embedding approach improved average precision over BM25 by 19% on TREC 2006 and 6% on TREC 2007 in the reported experiments ([document_1.txt, 2016](https://arxiv.org/abs/1608.01972)).

## Conclusion and Opinion

Based on the provided information, the embedding approach outperforms BM25 by 19% in average precision on TREC 2006 and by 6% in average precision on TREC 2007 ([document_1.txt, 2016](https://arxiv.org/abs/1608.01972)). This is the concrete answer to the query. The improvement is positive on both datasets, but it is not uniform, and the larger gain occurs on TREC 2006. The source further indicates that BM25 performs better than TFIDF and CENTROID, while CENTROID scores lower than both BM25 and SEM ([document_1.txt, 2016](https://arxiv.org/abs/1608.01972)). Consequently, the embedding approach appears to be the strongest method among those compared, and its advantage over BM25 is both real and dataset-dependent within the reported experiments. The most defensible conclusion is that the embedding approach provides a relative average precision gain of 6% to 19% over BM25 across the two TREC collections, with the exact gain depending on the dataset ([document_1.txt, 2016](https://arxiv.org/abs/1608.01972)). This finding supports the view that incorporating a semantic similarity measure can improve over a strong lexical baseline for PubMed query-to-document mapping, while also highlighting the need for broader evaluation before making universal claims.

## References

document_1.txt. (2016). *Bridging the Gap: Incorporating a Semantic Similarity Measure for Effectively Mapping PubMed Queries to Documents* (arXiv:1608.01972). Retrieved from https://arxiv.org/abs/1608.01972