# How Much Does the Embedding-Based Semantic Similarity Measure Outperform BM25? A Focused Analysis of the TREC Evidence

## Executive Summary

The single most direct answer available in the supplied evidence is quantitative and collection-specific. According to the TREC experiments reported in *Bridging the Gap: Incorporating a Semantic Similarity Measure for Effectively Mapping PubMed Queries to Documents*, the embedding-based semantic similarity approach (labelled **SEM** in the authors' Table 4) raises the **average precision of BM25 by 19% on TREC 2006 and by 6% on TREC 2007** ([arXiv:1608.01972](https://arxiv.org/abs/1608.01972)). In other words, the advantage of the semantic measure over BM25 is **not a single fixed number**; it is a range of roughly **6% to 19% relative improvement in average precision**, depending on the evaluation collection. The same passage establishes the surrounding ranking context: BM25 outperforms both TFIDF and CENTROID, while CENTROID produces scores below both BM25 and the SEM approach ([arXiv:1608.01972](https://arxiv.org/abs/1608.01972)). This report unpacks those figures, examines what they do and do not license us to conclude, and situates the deltas within the broader logic of hybrid lexical–semantic retrieval.

## The Retrieval Setting and the Baseline Being Improved

The comparison in question arises from the biomedical literature retrieval task commonly associated with the Text REtrieval Conference (TREC) genomics and PubMed-style collections, in which natural-language clinical or scientific queries must be mapped onto a large corpus of indexed documents. Within that setting, the paper reports results in a "TREC Experiments" section that tabulates four families of retrieval scoring: TFIDF, CENTROID, BM25, and the authors' semantic/embedding-based measure, referred to as SEM ([arXiv:1608.01972](https://arxiv.org/abs/1608.01972)).

BM25 is the pivot of the comparison because it functions here as the strongest lexical baseline. The evidence excerpt is explicit on this point: "BM25 performs better than TFIDF and CENTROID" ([arXiv:1608.01972](https://arxiv.org/abs/1608.01972)). That ordering matters methodologically. When a new semantic method is benchmarked against a weak baseline, improvements are easy to obtain and correspondingly uninformative. Here, the embedding approach is measured against the best-performing of the three lexical or centroid-style alternatives, which means the reported 19% and 6% gains are **incremental over an already competitive sparse-retrieval system** rather than over an artificially weak straw man ([arXiv:1608.01972](https://arxiv.org/abs/1608.01972)).

The CENTROID result reinforces the same point from the opposite direction. CENTROID — a pseudo-relevance-feedback-style document-centroid method — falls below both BM25 and SEM ([arXiv:1608.01972](https://arxiv.org/abs/1608.01972)). The overall pattern in Table 4 is therefore a three-tier ordering: TFIDF and CENTROID at the lower end, BM25 as the strong lexical reference point, and the semantic similarity measure at the top of the reported comparison ([arXiv:1608.01972](https://arxiv.org/abs/1608.01972)).

## Reported Performance Deltas by Collection

### TREC 2006: A 19% Gain in Average Precision

On the TREC 2006 evaluation, the embedding approach produced the larger of the two reported effects. The semantic measure boosted the average precision of BM25 **by 19%** ([arXiv:1608.01972](https://arxiv.org/abs/1608.01972)). To state this precisely and without overreach: the improvement is expressed as a **relative percentage increase in average precision** over the BM25 baseline, not as a reported absolute mean average precision (MAP) score. The excerpt as supplied does not reproduce the raw MAP values from Table 4, so the arithmetic increment in absolute MAP terms cannot be reconstructed from the available text alone ([arXiv:1608.01972](https://arxiv.org/abs/1608.01972)).

### TREC 2007: A 6% Gain in Average Precision

On the TREC 2007 evaluation, the same semantic approach boosted BM25's average precision **by 6%** ([arXiv:1608.01972](https://arxiv.org/abs/1608.01972)). This is the more conservative of the two effect sizes, and it is the figure that should anchor any general claim about the method's advantage, because it represents the smaller — and therefore safer — boundary of the reported range.

### The Asymmetry Between the Two Collections

The two numbers differ by a factor of slightly more than three: the 19% gain on TREC 2006 is roughly 3.2 times the 6% gain on TREC 2007 (derived from the figures reported in [arXiv:1608.01972](https://arxiv.org/abs/1608.01972)). This asymmetry is analytically informative rather than incidental. It indicates that the benefit of adding a semantic similarity signal to a lexical BM25 ranking is **collection-dependent** — sensitive, plausibly, to query formulation, topic difficulty, average document length, term-overlap characteristics, and the degree of vocabulary mismatch between queries and relevant documents in each track. A report that cited only the 19% figure would overstate the case; one that cited only the 6% figure would understate it. The honest summary statistic is the interval.

## Consolidated View of the Reported Results

The table below organises every quantitative claim about relative performance that the supplied excerpt supports. Cells marked "not reported" indicate that the source excerpt does not contain the underlying absolute score, and no value is inferred in its place.

| Retrieval system | TREC 2006 average precision | TREC 2007 average precision | Source |
|---|---|---|---|
| TFIDF | Below BM25 (magnitude not reported) | Below BM25 (magnitude not reported) | ([arXiv:1608.01972](https://arxiv.org/abs/1608.01972)) |
| CENTROID | Lower than both BM25 and SEM | Lower than both BM25 and SEM | ([arXiv:1608.01972](https://arxiv.org/abs/1608.01972)) |
| BM25 (baseline) | Reference point for all deltas | Reference point for all deltas | ([arXiv:1608.01972](https://arxiv.org/abs/1608.01972)) |
| SEM (embedding approach) | **+19% over BM25** | **+6% over BM25** | ([arXiv:1608.01972](https://arxiv.org/abs/1608.01972)) |
| Absolute MAP values | Not reported in excerpt | Not reported in excerpt | ([arXiv:1608.01972](https://arxiv.org/abs/1608.01972)) |

## Interpreting the Magnitude of the Gains

### Relative Versus Absolute Improvement

The most important interpretive caution concerns the unit of measurement. The source states that the embedding approach "boosts the average precision of BM25 by 19% and 6%" ([arXiv:1608.01972](https://arxiv.org/abs/1608.01972)). The phrase "boosts … by X%" is normally read as a **relative** gain — that is, the new score equals the BM25 score multiplied by 1.19 (TREC 2006) or 1.06 (TREC 2007). It is not equivalent to an absolute addition of 19 or 6 MAP points, and treating it as such would be a material misreading. Because the underlying BM25 MAP values are absent from the excerpt, the absolute effect cannot be computed here; nonetheless, the relative framing is the one the source supports ([arXiv:1608.01972](https://arxiv.org/abs/1608.01972)).

### Why a 6–19% Relative Gain Is Substantively Meaningful

Relative improvements of this size in an established retrieval benchmark are non-trivial. In the biomedical domain, where the same concept is routinely expressed through different surface forms — gene symbols versus gene names, abbreviations versus expanded terminology, lay phrasing versus controlled vocabulary — lexical matching through BM25 is structurally vulnerable to vocabulary mismatch. A semantic similarity component is designed precisely to bridge that gap, which is why the paper's framing speaks of "bridging the gap" between queries and documents ([arXiv:1608.01972](https://arxiv.org/abs/1608.01972)). The reported deltas are consistent with that motivation: the semantic measure adds value on top of a strong term-matching baseline rather than replacing it, since BM25 itself still outperformed TFIDF and CENTROID ([arXiv:1608.01972](https://arxiv.org/abs/1608.01972)).

### The Direction of the Evidence on Hybridisation

Read as a whole, the passage supports a **hybrid lexical-plus-semantic** conclusion rather than a "dense replaces sparse" conclusion. BM25 is described as the best of the three non-semantic methods, and the semantic approach is measured as an *uplift on BM25* rather than as a standalone replacement ([arXiv:1608.01972](https://arxiv.org/abs/1608.01972)). The CENTROID result — worse than BM25 as well as worse than SEM — suggests that not every attempt to move beyond pure term matching yields gains; the specific embedding-based formulation does, whereas the centroid formulation does not ([arXiv:1608.01972](https://arxiv.org/abs/1608.01972)).

## Limitations of the Evidence Presented Here

Several constraints qualify the confidence with which the 19% and 6% figures should be generalised:

1. **No absolute scores.** Neither MAP values nor the number of topics per track is reproduced in the supplied excerpt, so effect sizes cannot be converted into absolute retrieval gains ([arXiv:1608.01972](https://arxiv.org/abs/1608.01972)).
2. **No variance or significance statistics.** The excerpt reports point estimates only. It does not report confidence intervals, per-topic variance, or significance tests, so it cannot be determined from this evidence alone whether the smaller 6% TREC 2007 gain is statistically distinguishable from zero ([arXiv:1608.01972](https://arxiv.org/abs/1608.01972)).
3. **Two collections only.** The reported range rests on two evaluation years of one biomedical track; no cross-domain or cross-language evidence is presented in the excerpt ([arXiv:1608.01972](https://arxiv.org/abs/1608.01972)).
4. **Single metric.** The deltas are stated for average precision. Recall at fixed cut-offs, nDCG, or precision at k are not reported in the excerpt, so it is unknown whether the embedding approach produces a uniform or a metric-specific advantage ([arXiv:1608.01972](https://arxiv.org/abs/1608.01972)).
5. **Metric-level detail.** Improvements are described at the level of average precision; the excerpt does not indicate whether the reported figures are mean average precision across all topics or an alternative aggregation ([arXiv:1608.01972](https://arxiv.org/abs/1608.01972)).

## Conclusion

To the question of how much the embedding-based similarity measure outperforms BM25, the supplied evidence supports a precise and bounded answer: **the semantic similarity measure increased BM25's average precision by 19% on TREC 2006 and by 6% on TREC 2007** ([arXiv:1608.01972](https://arxiv.org/abs/1608.01972)). The reliable summary is therefore a **relative average-precision uplift of between 6% and 19% across the two evaluated TREC collections**, achieved against BM25, which was itself the strongest of the three non-semantic baselines and superior to both TFIDF and CENTROID ([arXiv:1608.01972](https://arxiv.org/abs/1608.01972)). The roughly threefold difference between the two collections should be treated as a genuine feature of the finding — evidence that the magnitude of the semantic advantage is conditional on the collection — rather than as noise to be averaged away. Because the excerpt omits absolute scores, significance testing, and metrics beyond average precision, the appropriate conclusion is directional and relative, not absolute: the embedding approach improves meaningfully on a strong lexical baseline in biomedical query-to-document retrieval, with the size of that improvement varying substantially by collection ([arXiv:1608.01972](https://arxiv.org/abs/1608.01972)).

## References

document_1.txt (2016). *Bridging the Gap: Incorporating a Semantic Similarity Measure for Effectively Mapping PubMed Queries to Documents* (arXiv:1608.01972), Section: TREC Experiments. [https://arxiv.org/abs/1608.01972](https://arxiv.org/abs/1608.01972)