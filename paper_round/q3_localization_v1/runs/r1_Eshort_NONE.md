# Quantifying the Incremental Gain of an Embedding-Based Semantic Similarity Measure over BM25: Evidence from TREC 2006 and TREC 2007

## Executive Summary

The direct answer to the question posed is that the embedding-based semantic similarity measure reported in the source improves upon BM25 by **19% on TREC 2006** and by **6% on TREC 2007**, measured in terms of average precision ([Bridging the Gap, 2016](https://arxiv.org/abs/1608.01972)). These two figures constitute the complete, explicit answer available in the supplied evidence: the source reports a 19% boost in average precision of BM25 on the TREC 2006 collection and a 6% boost on the TREC 2007 collection ([Bridging the Gap, 2016](https://arxiv.org/abs/1608.01972)). The same passage further establishes the comparative ordering of the baselines, noting that BM25 outperforms both TFIDF and CENTROID, while CENTROID yields scores below both BM25 and the semantic (SEM) approach ([Bridging the Gap, 2016](https://arxiv.org/abs/1608.01972)). This report examines what those two numbers mean, how they should be interpreted, what they do and do not license as conclusions, and what a careful reader should conclude about the practical value of adding a semantic similarity component to a lexical retriever.

## 1. Framing the Question

The question — "By how much does their similarity measure (the embedding approach) outperform BM25?" — presupposes a head-to-head comparison between a dense, embedding-based similarity signal and a classical lexical ranking function. In the source, that comparison is reported not as a wholesale replacement of BM25 but as an augmentation: the paper's title describes "incorporating a semantic similarity measure" for mapping PubMed queries to documents ([Bridging the Gap, 2016](https://arxiv.org/abs/1608.01972)). This distinction matters for interpreting the reported deltas. A 19% gain "of BM25" is naturally read as an incremental, relative improvement attributable to the semantic component layered onto or combined with a BM25 retrieval pipeline, rather than as the performance of a standalone embedding system competing against a standalone lexical system ([Bridging the Gap, 2016](https://arxiv.org/abs/1608.01972)).

The domain is also material. The source concerns the mapping of PubMed queries to documents, i.e., a biomedical literature retrieval setting in which vocabulary mismatch between consumer-style queries and technical article text is a well-recognized failure mode ([Bridging the Gap, 2016](https://arxiv.org/abs/1608.01972)). Improvements of the magnitude reported are therefore best understood as domain-specific gains in a retrieval environment where lexical overlap is an imperfect proxy for topical relevance.

## 2. The Evidence Base

### 2.1 Provenance and Reliability

The sole source available for this report is a preprint hosted on arXiv, identified as arXiv:1608.01972, titled *Bridging the Gap: Incorporating a Semantic Similarity Measure for Effectively Mapping PubMed Queries to Documents* ([Bridging the Gap, 2016](https://arxiv.org/abs/1608.01972)). The relevant material comes from a section labeled "TREC Experiments" and centers on a results table designated as Table 4 ([Bridging the Gap, 2016](https://arxiv.org/abs/1608.01972)). The claims are therefore drawn from a single, self-contained experimental report rather than from a systematic review, a meta-analysis, or a multi-paper replication effort.

Two reliability considerations follow. First, the source is a primary research report, which lends it authority on its own experimental results but limits generalization beyond the specific corpora, queries, and configuration it tested. Second, the citation is described as a preprint from 2016, meaning that by the current date (September 2026) it is a decade-old artifact; its findings remain relevant as a documented data point, but they should not be assumed to reflect the current state of the art in dense or hybrid retrieval ([Bridging the Gap, 2016](https://arxiv.org/abs/1608.01972)).

### 2.2 An Important Observation About the Supplied Evidence

The provided context reproduces the identical passage four times, each attributed to "document_1.txt" with the same title, content, and section ([Bridging the Gap, 2016](https://arxiv.org/abs/1608.01972)). This redundancy is worth flagging explicitly: the four occurrences do **not** constitute four independent confirmations of the 19% and 6% figures. They are repeated retrievals of the same underlying text. Analytically, the effective evidence base is a single sentence-level finding from a single table in a single paper. Any confidence assigned to the numbers must be calibrated to that reality rather than to the apparent volume of textual support ([Bridging the Gap, 2016](https://arxiv.org/abs/1608.01972)).

## 3. The Reported Headline Result

The core quantitative finding can be stated compactly and reproduced faithfully as follows.

| Benchmark collection | Direction of comparison | Reported improvement in average precision |
|---|---|---|
| TREC 2006 | Embedding approach over BM25 | +19% |
| TREC 2007 | Embedding approach over BM25 | +6% |

**Table 1.** Reported relative improvements in average precision attributable to the embedding-based semantic similarity approach relative to BM25 ([Bridging the Gap, 2016](https://arxiv.org/abs/1608.01972)).

The source states the result in the following terms: "the embedding approach boosts the average precision of BM25 by 19% and 6% on TREC 2006 and 2007, respectively" ([Bridging the Gap, 2016](https://arxiv.org/abs/1608.01972)). This sentence contains the entirety of the numeric answer to the query. There is no third benchmark reported in the supplied material, and no additional magnitude is given for any other collection, query set, or metric ([Bridging the Gap, 2016](https://arxiv.org/abs/1608.01972)).

## 4. What "19% and 6%" Actually Means

### 4.1 Relative, Not Absolute, Improvement

The phrasing "boosts the average precision of BM25 by 19%" is a relative-change formulation ([Bridging the Gap, 2016](https://arxiv.org/abs/1608.01972)). A relative improvement of 19% is not the same as an increase of 19 percentage points in average precision. The excerpt does not disclose the underlying absolute average-precision values for BM25 on either collection, so the corresponding absolute gains cannot be derived from the provided information ([Bridging the Gap, 2016](https://arxiv.org/abs/1608.01972)).

This distinction is decisive for anyone attempting to translate the finding into expected operational benefit. If the BM25 baseline were very high, a 19% relative gain could correspond to only a modest absolute increment; if the baseline were low, the same relative gain could represent a substantial shift in absolute ranking quality. The source as supplied does not permit the reader to determine which scenario applies ([Bridging the Gap, 2016](https://arxiv.org/abs/1608.01972)).

### 4.2 An Explicitly Illustrative Arithmetic Exercise

To make the relative-versus-absolute gap concrete, Table 2 presents purely hypothetical baseline values. **These numbers are not reported in the source and must not be attributed to it**; they exist only to demonstrate how relative percentages translate into absolute differences.

| Hypothetical BM25 average precision | +19% relative (TREC 2006 analogue) | +6% relative (TREC 2007 analogue) |
|---|---|---|
| 0.100 | 0.119 (+0.019) | 0.106 (+0.006) |
| 0.200 | 0.238 (+0.038) | 0.212 (+0.012) |
| 0.300 | 0.357 (+0.057) | 0.318 (+0.018) |

**Table 2.** Hypothetical illustration of how a constant relative improvement maps to differing absolute gains. All values are invented for illustration only and are not drawn from ([Bridging the Gap, 2016](https://arxiv.org/abs/1608.01972)); the source does not report BM25 baseline scores.

### 4.3 Metric Scope

The reported metric is average precision ([Bridging the Gap, 2016](https://arxiv.org/abs/1608.01972)). Average precision is a rank-sensitive measure that rewards placing relevant documents early in the returned list, so a gain in this metric indicates improved ordering quality, not merely improved recall of a set of documents. Within the constraints of the excerpt, however, no additional metrics — such as recall at fixed cutoffs, nDCG, or precision at k — are reported for the BM25-versus-embedding comparison ([Bridging the Gap, 2016](https://arxiv.org/abs/1608.01972)). The conclusion supported by the evidence is therefore narrowly about average precision.

## 5. Comparative Positioning of the Methods

Beyond the two headline percentages, the source provides a ranking of the approaches it evaluated, which is useful for placing the semantic component in context.

| Method | Reported comparative performance |
|---|---|
| Embedding / SEM approach | Improves BM25 average precision by 19% (TREC 2006) and 6% (TREC 2007) |
| BM25 | Outperforms TFIDF and CENTROID |
| TFIDF | Outperformed by BM25 |
| CENTROID | Lower than both BM25 and the SEM approach |

**Table 3.** Reported comparative ordering of retrieval methods ([Bridging the Gap, 2016](https://arxiv.org/abs/1608.01972)).

Two observations follow from Table 3. First, the lexical baseline chosen for the semantic comparison is BM25, and the source explicitly justifies this by noting that BM25 performs better than TFIDF and CENTROID ([Bridging the Gap, 2016](https://arxiv.org/abs/1608.01972)). The comparison is thus against the strongest of the lexical alternatives tested, which makes the reported improvement more meaningful than a comparison against a weaker baseline would be. Second, the simple centroid-of-embeddings strategy performs poorly — below BM25 and below the SEM approach ([Bridging the Gap, 2016](https://arxiv.org/abs/1608.01972)). This indicates that the benefit is not attributable to embeddings as such, but to how the semantic similarity signal is constructed and incorporated; a naive embedding aggregation does not, on this evidence, outperform BM25 at all ([Bridging the Gap, 2016](https://arxiv.org/abs/1608.01972)).

## 6. Why the Gain Varies Between the Two Collections

The threefold difference between the 2006 gain (19%) and the 2007 gain (6%) is one of the most analytically interesting features of the reported result ([Bridging the Gap, 2016](https://arxiv.org/abs/1608.01972)). Several explanations are consistent with the evidence, though the excerpt does not adjudicate among them:

- **Baseline strength differences.** If BM25 happened to perform comparatively well on the TREC 2007 topics, there would be less headroom for a semantic component to add value, compressing the relative gain ([Bridging the Gap, 2016](https://arxiv.org/abs/1608.01972)).
- **Topic-set composition.** Different query sets contain different proportions of queries that suffer from vocabulary mismatch, the precise failure mode a semantic similarity measure is designed to address ([Bridging the Gap, 2016](https://arxiv.org/abs/1608.01972)).
- **Relevance-assessment and collection differences.** The two TREC editions represent distinct corpora and judgment sets, and the semantic component's utility need not transfer uniformly across them ([Bridging the Gap, 2016](https://arxiv.org/abs/1608.01972)).

The variance is itself a finding: the benefit of the embedding approach is not a fixed constant but is collection-dependent, and the average across the two reported collections is approximately 12.5%, a figure derived by simple arithmetic from the two reported percentages and not asserted by the source ([Bridging the Gap, 2016](https://arxiv.org/abs/1608.01972)).

## 7. Methodological Limitations of the Evidence

A rigorous reading requires acknowledging what the supplied material cannot establish.

1. **No absolute scores.** The excerpt reports only relative percentages; BM25 baseline values, and hence absolute gains, are absent ([Bridging the Gap, 2016](https://arxiv.org/abs/1608.01972)).
2. **No variance or significance information.** The excerpt reports no confidence intervals, standard deviations across topics, or statistical significance tests, so the reliability of the 19% and 6% figures across query samples is unknown ([Bridging the Gap, 2016](https://arxiv.org/abs/1608.01972)).
3. **Single-domain scope.** The results concern PubMed queries mapped to documents, and the source's framing is biomedical and domain-specific ([Bridging the Gap, 2016](https://arxiv.org/abs/1608.01972)). Generalization to web search, legal retrieval, or other domains is not supported by the evidence.
4. **Two collections only.** The claim rests on TREC 2006 and TREC 2007, the latter of which is a nine-year-old collection relative to the source's own publication and roughly two decades old as of 2026 ([Bridging the Gap, 2016](https://arxiv.org/abs/1608.01972)).
5. **Redundant evidence, not corroborating evidence.** As noted in Section 2.2, the excerpt is repeated four times, which inflates apparent support without adding independent information ([Bridging the Gap, 2016](https://arxiv.org/abs/1608.01972)).

## 8. Implications

Taken at face value, the evidence supports the following practical conclusion: in biomedical literature retrieval, adding a semantic similarity signal to a BM25 pipeline yields a meaningful but variable improvement in ranking quality, reported as 19% and 6% relative gains in average precision on two TREC collections ([Bridging the Gap, 2016](https://arxiv.org/abs/1608.01972)). The evidence does **not** support the stronger claim that embedding-based retrieval replaces lexical retrieval. On the contrary, the source's own framing is one of incorporation, and its finding that a centroid-based embedding approach underperforms BM25 demonstrates that semantic methods are not automatically superior ([Bridging the Gap, 2016](https://arxiv.org/abs/1608.01972)). The defensible position is a hybrid one: lexical matching supplies a strong foundation, and carefully constructed semantic similarity provides an incremental, collection-dependent uplift.

## 9. Conclusion

To answer the query directly and without embellishment: according to the supplied source, the embedding-based semantic similarity measure outperforms BM25 by **19% in average precision on TREC 2006** and by **6% in average precision on TREC 2007** ([Bridging the Gap, 2016](https://arxiv.org/abs/1608.01972)). BM25 remains the stronger baseline relative to TFIDF and CENTROID, and a centroid-based embedding strategy performs below both BM25 and the semantic approach, which underscores that the reported gain comes from the specific semantic similarity method rather than from embeddings generically ([Bridging the Gap, 2016](https://arxiv.org/abs/1608.01972)). The principal caveats are that the figures are relative rather than absolute, that they derive from a single preprint and a single repeated excerpt rather than from independent corroboration, that they vary substantially between the two collections, and that they are specific to a biomedical retrieval setting ([Bridging the Gap, 2016](https://arxiv.org/abs/1608.01972)).

## References

Bridging the gap: Incorporating a semantic similarity measure for effectively mapping PubMed queries to documents (arXiv:1608.01972). (2016). *arXiv*. https://arxiv.org/abs/1608.01972