# Quantifying the Semantic Similarity (Embedding) Advantage over BM25: A Detailed Report on Reported Gains in PubMed Query–Document Mapping

## Summary of the Core Finding

The central question addressed in this report is straightforward: by how much does the embedding-based semantic similarity measure outperform BM25 in the PubMed query–document mapping experiments reported in the source material? According to the primary source, an arXiv paper titled *Bridging the Gap: Incorporating a Semantic Similarity Measure for Effectively Mapping PubMed Queries to Documents* (arXiv:1608.01972), the answer is that the embedding approach boosts the average precision of BM25 by **19% on TREC 2006** and by **6% on TREC 2007** ([document_1.txt](#reference-1)). This result is reported in the TREC Experiments section of the paper, with reference to the results presented in its Table 4 ([document_1.txt](#reference-1)).

A third-party research note on PubMed query–document mapping restates the same figures, indicating that the proposed semantic-similarity (embedding) approach improves retrieval over BM25 by raising average precision by 19% on TREC 2006 and by 6% on TREC 2007 ([document_2.txt](#reference-2)). Because the third-party note explicitly attributes these figures to the same primary study, the two documents should not be treated as independent confirmations; they constitute one data point reported twice.

## Direct Answer to the Query

The embedding approach outperforms BM25 by **two distinct margins**, depending on the test collection:

- **+19%** in average precision on TREC 2006
- **+6%** in average precision on TREC 2007

These are reported as relative improvements in the average precision metric, not as absolute percentage-point gains, and not as a single pooled figure across collections ([document_1.txt](#reference-1); [document_2.txt](#reference-2)). Consequently, the honest answer to "by how much" is not a single number but a range: the advantage varies by roughly a factor of three between the two evaluation sets, from a modest 6% gain to a substantial 19% gain.

## Where the Numbers Come From

### The Primary Source

The primary evidence is the TREC Experiments section of arXiv:1608.01972, which reports a comparison of four retrieval approaches on two TREC collections: BM25, TFIDF, CENTROID, and the proposed embedding/semantic similarity approach (referred to as "SEM" in the text) ([document_1.txt](#reference-1)). The paper's Table 4 is the specific locus of the reported figures, and the text states that "the embedding approach boosts the average precision of BM25 by 19% and 6% on TREC 2006 and 2007, respectively" ([document_1.txt](#reference-1)).

### The Secondary Source

The third-party research note titled "PubMed query-document mapping" independently paraphrases the same finding: "the proposed semantic-similarity (embedding) approach improves retrieval over BM25: it raises average precision by 19% on TREC 2006 and by 6% on TREC 2007" ([document_2.txt](#reference-2)). The note also states that "BM25 itself outperforms TFIDF and CENTROID, and CENTROID scores below both BM25 and the embedding approach" ([document_2.txt](#reference-2)). Notably, the note carries an attribution line pointing back to document_1.txt, confirming that it is a derivative summary rather than an independent replication ([document_2.txt](#reference-2)).

## The Full Comparison Landscape

The query concerns only the embedding-versus-BM25 gap, but that gap is best understood within the complete ranking of systems reported in Table 4. The source material supports the following ordinal relationships.

| Rank | Approach | Reported Relationship |
|------|----------|----------------------|
| 1 | Embedding / SEM approach | Outperforms BM25 by 19% (TREC 2006) and 6% (TREC 2007) in average precision ([document_1.txt](#reference-1)) |
| 2 | BM25 | Performs better than TFIDF and CENTROID ([document_1.txt](#reference-1)) |
| 3 | TFIDF | Below BM25 ([document_1.txt](#reference-1)) |
| 4 | CENTROID | Provides scores lower than both BM25 and the SEM approach ([document_1.txt](#reference-1)) |

This ranking is important for interpretation. It establishes that the embedding approach is not merely better than a weak baseline; it surpasses BM25, which is itself the strongest of the three lexical/statistical baselines tested ([document_1.txt](#reference-1)). In other words, the reported 19% and 6% gains are measured against the strongest competing method in the study, which strengthens the significance of the finding.

## The Magnitude of the Gains in Context

| Test Collection | Relative Improvement of Embedding Approach over BM25 |
|-----------------|------------------------------------------------------|
| TREC 2006 | +19% ([document_1.txt](#reference-1)) |
| TREC 2007 | +6% ([document_1.txt](#reference-1)) |
| Simple arithmetic mean of the two reported values | 12.5% |

The arithmetic mean of 12.5% is presented here purely as a descriptive summary of the two reported figures; it should not be interpreted as the study's headline result, because the source reports the two collections separately and the underlying collections differ in composition, query sets, and relevance judgments ([document_1.txt](#reference-1)). Nevertheless, a mean relative gain of roughly 12.5% in average precision over BM25 across two TREC collections is a materially large effect in retrieval evaluation terms, particularly because BM25 is a well-established and competitive lexical baseline.

The disparity between the two collections — 19% versus 6%, a difference of 13 percentage points, or roughly a threefold ratio — is itself informative. It suggests that the benefit of incorporating a semantic similarity measure is collection-dependent. On the collection where lexical matching is less adequate (TREC 2006), the semantic component adds considerable value; on the collection where lexical matching is already relatively effective (TREC 2007), the incremental benefit is smaller but still positive ([document_1.txt](#reference-1)).

## Interpretation and Assessment

Based on the provided information, my assessment is as follows. The evidence supports a clear and consistent directional conclusion: the embedding-based semantic similarity approach outperforms BM25 on both evaluated TREC collections, with gains of 19% and 6% in average precision ([document_1.txt](#reference-1); [document_2.txt](#reference-2)). The direction of the effect is unambiguous and is corroborated by both documents, while the magnitude is variable.

Three points deserve emphasis:

**First, the gains are relative, not absolute.** The source reports percentage improvements over BM25's average precision rather than the absolute average precision values themselves ([document_1.txt](#reference-1)). A 6% relative gain and a 19% relative gain therefore do not map directly onto percentage-point differences unless the BM25 baseline values are known, and those baseline values are not provided in the available material.

**Second, the evaluation rests on two collections.** Both reported figures derive from TREC 2006 and TREC 2007 ([document_1.txt](#reference-1)). No additional collections, domains, or query sets are reported in the provided material. Generalization beyond these two evaluation settings is therefore not established by the evidence at hand.

**Third, the corroborating source is derivative.** Because document_2.txt explicitly cites document_1.txt as its source ([document_2.txt](#reference-2)), the apparent convergence of two documents reflects a single underlying experiment rather than independent verification. For evidentiary purposes, this report treats arXiv:1608.01972 as the authoritative source and the third-party note as a consistency check.

## Limitations and Caveats

Several limitations constrain the precision of any answer to the query:

- **No absolute scores are provided.** The material reports relative improvements only, without stating the absolute average precision values for BM25 or for the embedding approach on either TREC collection ([document_1.txt](#reference-1)).
- **No statistical significance testing is reported** in the available material, so it is not possible to determine whether the 6% gain on TREC 2007, in particular, is statistically reliable or within the range of noise ([document_1.txt](#reference-1)).
- **No confidence intervals or variance estimates** accompany the reported figures ([document_1.txt](#reference-1)).
- **No detail is provided on the embedding method itself** — the source material refers to "the embedding approach" and "SEM" without describing the underlying model architecture, training data, or dimensionality in the excerpts available ([document_1.txt](#reference-1)).
- **The metric is specified as average precision**, but the material does not indicate whether this refers to mean average precision aggregated over queries or another variant ([document_1.txt](#reference-1)).

These limitations do not undermine the directional finding, but they do mean the answer "19% on TREC 2006 and 6% on TREC 2007" should be quoted with the qualifier that these are relative improvements in the reported average precision metric on two specific collections.

## Why the Comparison Matters

The comparison is significant for at least two reasons. First, it benchmarks a semantic approach against BM25, which the source explicitly identifies as outperforming both TFIDF and CENTROID ([document_1.txt](#reference-1)). This means the reported 19% and 6% gains are measured against the strongest baseline in the study, making them a meaningful test of whether semantic similarity adds value beyond well-tuned lexical retrieval. Second, the finding that CENTROID "provides scores lower than BM25 and SEM approaches" ([document_1.txt](#reference-1)) reinforces the interpretation that the improvement is attributable to the semantic similarity mechanism rather than to the general use of embedding representations, since at least one alternative embedding-based aggregation strategy (CENTROID) underperforms the baseline.

## Conclusion

The embedding-based semantic similarity measure outperforms BM25 by **19% in average precision on TREC 2006 and by 6% on TREC 2007**, as reported in the TREC Experiments section of arXiv:1608.01972 and confirmed as a restatement in the third-party research note ([document_1.txt](#reference-1); [document_2.txt](#reference-2)). There is no single figure that captures the advantage; the gain is collection-dependent and ranges from 6% to 19% across the two evaluated sets, with a descriptive mean of 12.5%. The direction of the effect is consistent across sources, the baseline is the strongest of the compared lexical methods, and the gains are reported in a standard retrieval metric. The principal caveats are that the figures are relative rather than absolute, that no significance testing or absolute baseline scores are provided in the available material, and that the corroborating document is a derivative summary of the same primary study rather than an independent verification ([document_1.txt](#reference-1); [document_2.txt](#reference-2)).

## References

document_1.txt. (n.d.). *Bridging the gap: Incorporating a semantic similarity measure for effectively mapping PubMed queries to documents* (arXiv:1608.01972), Section: TREC Experiments. https://arxiv.org/abs/1608.01972

document_2.txt. (n.d.). *Third-party research note: PubMed query-document mapping.*