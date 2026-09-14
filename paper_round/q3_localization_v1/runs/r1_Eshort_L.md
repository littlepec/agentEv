# Quantifying the Embedding-Based Semantic Similarity Advantage over BM25 in PubMed Query–Document Mapping

## Introduction and Scope

The query under examination asks a precise, quantitative question: by how much does the semantic similarity measure — the embedding approach described in the paper *Bridging the Gap: Incorporating a Semantic Similarity Measure for Effectively Mapping PubMed Queries to Documents* (arXiv:1608.01972) — outperform BM25? The evidence available for answering this question comes from two documents: the primary research paper itself, specifically its "TREC Experiments" section and Table 4, and a third-party research note that summarizes the same study ([Bridging the Gap, arXiv:1608.01972](https://arxiv.org/abs/1608.01972); [Third-party research note, document_2.txt](document_2.txt)).

Both sources converge on a single, unambiguous quantitative finding: the embedding-based semantic similarity approach improves the average precision of BM25 by **19% on TREC 2006** and **6% on TREC 2007** ([Bridging the Gap, arXiv:1608.01972](https://arxiv.org/abs/1608.01972); [Third-party research note, document_2.txt](document_2.txt)). This report unpacks that headline figure, situates it within the broader baseline landscape reported in the same study, and evaluates what the number does and does not tell us.

## The Direct Answer: Magnitude of the Improvement

The core answer to the query is a pair of relative improvements in average precision, one per evaluation year. Table 4 of the source paper reports that the embedding approach boosts BM25's average precision by 19% on TREC 2006 and by 6% on TREC 2007 ([Bridging the Gap, arXiv:1608.01972](https://arxiv.org/abs/1608.01972)). The third-party research note independently restates the identical figures, describing the semantic-similarity (embedding) approach as improving retrieval over BM25 by raising average precision 19% on TREC 2006 and 6% on TREC 2007 ([Third-party research note, document_2.txt](document_2.txt)).

These results can be summarized in structured form as follows:

| Evaluation Year | Metric | Improvement over BM25 | Direction |
|---|---|---|---|
| TREC 2006 | Average precision | +19% | Embedding approach superior |
| TREC 2007 | Average precision | +6% | Embedding approach superior |

Table 1. Reported gains of the embedding-based semantic similarity approach over BM25, as stated in the primary paper and repeated by the third-party note ([Bridging the Gap, arXiv:1608.01972](https://arxiv.org/abs/1608.01972); [Third-party research note, document_2.txt](document_2.txt)).

The most defensible single-sentence answer is therefore: **the embedding approach outperforms BM25 by 19% on TREC 2006 and by 6% on TREC 2007, measured in average precision** ([Bridging the Gap, arXiv:1608.01972](https://arxiv.org/abs/1608.01972)).

## What the Percentage Figures Actually Represent

An important interpretive point concerns the nature of these percentages. Both sources phrase the result as an improvement *of* BM25's average precision — that is, a relative or proportional gain measured against the BM25 baseline, not an absolute gain expressed in percentage points of average precision ([Bridging the Gap, arXiv:1608.01972](https://arxiv.org/abs/1608.01972); [Third-party research note, document_2.txt](document_2.txt)). Formally, if BM25 achieves an average precision of *P* on a given TREC collection, the embedding-augmented approach is reported to achieve approximately 1.19 × *P* on TREC 2006 and 1.06 × *P* on TREC 2007.

This distinction matters considerably for anyone attempting to translate the finding into expected performance. A 19% relative improvement is meaningful but is not equivalent to a 19-point increase in average precision; the absolute increment depends entirely on the underlying BM25 baseline, which the provided sources do not disclose ([Bridging the Gap, arXiv:1608.01972](https://arxiv.org/abs/1608.01972)). Neither document provides the absolute average precision values for BM25, TF-IDF, CENTROID, or the embedding approach, nor does either report raw score tables beyond the percentage deltas ([Bridging the Gap, arXiv:1608.01972](https://arxiv.org/abs/1608.01972); [Third-party research note, document_2.txt](document_2.txt)). Consequently, the precise magnitude of the advantage in absolute terms cannot be derived from the information at hand; only the proportional relationship is documented.

## Comparative Context: Where the Embedding Approach Sits Relative to Other Retrieval Methods

The improvement figures become more informative when placed alongside the full set of baselines evaluated in the study. According to the paper's Table 4 discussion, BM25 performs better than both TF-IDF and CENTROID ([Bridging the Gap, arXiv:1608.01972](https://arxiv.org/abs/1608.01972)). In turn, the embedding approach — sometimes referred to in the source as the SEM approach — outperforms BM25 ([Bridging the Gap, arXiv:1608.01972](https://arxiv.org/abs/1608.01972)). CENTROID, meanwhile, provides scores lower than both BM25 and the SEM approach ([Bridging the Gap, arXiv:1608.01972](https://arxiv.org/abs/1608.01972)). The third-party note reaches the same ordering, stating that BM25 outperforms TF-IDF and CENTROID and that CENTROID scores below both BM25 and the embedding approach ([Third-party research note, document_2.txt](document_2.txt)).

This yields a consistent ranking of the four methods reported:

| Rank | Method | Comparative Position |
|---|---|---|
| 1 | Embedding / semantic similarity (SEM) | Best; boosts BM25 average precision by 19% (TREC 2006) and 6% (TREC 2007) |
| 2 | BM25 | Strong lexical baseline; outperforms TF-IDF and CENTROID |
| 3 | TF-IDF | Outperformed by BM25 |
| 4 | CENTROID | Lowest; scores below both BM25 and the embedding approach |

Table 2. Relative ordering of retrieval approaches as reported in the source materials ([Bridging the Gap, arXiv:1608.01972](https://arxiv.org/abs/1608.01972); [Third-party research note, document_2.txt](document_2.txt)).

The practical implication of this ranking is notable: the embedding approach does not merely beat a weak baseline. It improves upon BM25, which is itself the strongest of the lexical baselines tested in the study ([Bridging the Gap, arXiv:1608.01972](https://arxiv.org/abs/1608.01972)). The gain is therefore measured against a competitive sparse-retrieval reference point rather than against a trivially weak system.

## Year-over-Year Variability and Its Interpretation

The reported gains are not uniform across the two evaluation years. The 19% improvement on TREC 2006 is more than three times the 6% improvement on TREC 2007, a spread of 13 percentage points between the two relative-improvement figures ([Bridging the Gap, arXiv:1608.01972](https://arxiv.org/abs/1608.01972); [Third-party research note, document_2.txt](document_2.txt)).

Two conclusions follow from this spread. First, the direction of the effect is stable: in both years, the embedding approach is reported to improve over BM25 ([Bridging the Gap, arXiv:1608.01972](https://arxiv.org/abs/1608.01972)). This consistency across two separate TREC collections strengthens confidence that the semantic similarity component contributes genuine retrieval value rather than reflecting an artifact of a single test set ([Third-party research note, document_2.txt](document_2.txt)). Second, the magnitude of the effect is clearly collection-dependent. A 19% gain and a 6% gain are substantively different outcomes, and the source materials do not offer an explanation for the divergence between the two years, nor do they present an analysis attributing the difference to query characteristics, collection composition, or topic difficulty ([Bridging the Gap, arXiv:1608.01972](https://arxiv.org/abs/1608.01972)).

For practitioners, this variability argues against assuming a fixed, transferable uplift from semantic similarity. A reasonable reading of the evidence is that the embedding approach delivers an improvement somewhere in the low-to-moderate double-digit relative range on the collections studied, with 19% representing the upper end observed and 6% the lower end ([Bridging the Gap, arXiv:1608.01972](https://arxiv.org/abs/1608.01972); [Third-party research note, document_2.txt](document_2.txt)).

## Source Reliability and Evidential Basis

Assessing the reliability of the 19% and 6% figures requires attention to the provenance of the two documents. The first source is the primary research paper itself, identified by its arXiv identifier (arXiv:1608.01972), and specifically its "TREC Experiments" section and Table 4 ([Bridging the Gap, arXiv:1608.01972](https://arxiv.org/abs/1608.01972)). This is the authoritative origin of the numbers: the paper is the venue in which the experiment was conducted and the results tabulated. Its status as an arXiv preprint means the material should be treated as a research manuscript rather than as a formally peer-reviewed journal publication, which is a relevant caveat when weighing the strength of the evidence.

The second source is a third-party research note on PubMed query–document mapping ([Third-party research note, document_2.txt](document_2.txt)). This note restates the same figures — 19% on TREC 2006 and 6% on TREC 2007 — along with the same comparative claims about BM25, TF-IDF, and CENTROID ([Third-party research note, document_2.txt](document_2.txt)). Critically, the note explicitly attributes its content back to document_1, meaning it is a derivative summary rather than an independent replication ([Third-party research note, document_2.txt](document_2.txt)).

This has a direct bearing on how much confidence the figures deserve. The apparent agreement between the two sources is not independent corroboration; it is the same underlying result reported twice. The provided information contains multiple repetitions of both documents, but these repetitions do not add evidential weight — they are duplicates of the same two artifacts. Accordingly, the 19% and 6% values should be treated as a single experimental finding from one study, summarized consistently by a secondary note, rather than as a finding validated across multiple independent investigations ([Bridging the Gap, arXiv:1608.01972](https://arxiv.org/abs/1608.01972); [Third-party research note, document_2.txt](document_2.txt)).

On the positive side, the consistency of the secondary note with the primary paper indicates that the headline result has been transmitted accurately and that there is no evident distortion or inflation of the reported improvement ([Third-party research note, document_2.txt](document_2.txt)).

## Limitations and Unresolved Questions

Several limitations constrain the strength of any conclusion drawn from this evidence base:

1. **Absence of absolute scores.** Neither source reports the absolute average precision values underlying the percentage improvements, so the deltas cannot be converted into absolute retrieval gains ([Bridging the Gap, arXiv:1608.01972](https://arxiv.org/abs/1608.01972); [Third-party research note, document_2.txt](document_2.txt)).
2. **No statistical significance information.** The materials do not report significance tests, confidence intervals, or per-query variance for the 19% and 6% improvements, leaving the statistical robustness of the deltas unestablished ([Bridging the Gap, arXiv:1608.01972](https://arxiv.org/abs/1608.01972)).
3. **Limited generalizability.** The results pertain to TREC 2006 and TREC 2007 in the specific PubMed query–document mapping setting; no evidence is provided that the same improvement magnitudes hold on other collections or domains ([Bridging the Gap, arXiv:1608.01972](https://arxiv.org/abs/1608.01972); [Third-party research note, document_2.txt](document_2.txt)).
4. **Unexplained year-to-year divergence.** The threefold difference between the 19% and 6% gains is reported without analysis, so the conditions under which the embedding approach is most advantageous remain unclear ([Bridging the Gap, arXiv:1608.01972](https://arxiv.org/abs/1608.01972)).
5. **Single-study basis.** As noted, the two sources are not independent, so the finding rests on one experimental program ([Third-party research note, document_2.txt](document_2.txt)).

## Conclusion

The answer to the query is straightforward and consistently reported across the available evidence: the embedding-based semantic similarity measure outperforms BM25 by **19% on TREC 2006** and **6% on TREC 2007** in average precision ([Bridging the Gap, arXiv:1608.01972](https://arxiv.org/abs/1608.01972); [Third-party research note, document_2.txt](document_2.txt)). These are relative improvements over a BM25 baseline that is itself the strongest lexical method tested, exceeding both TF-IDF and CENTROID, with CENTROID ranking lowest of all approaches evaluated ([Bridging the Gap, arXiv:1608.01972](https://arxiv.org/abs/1608.01972)). The improvement is directionally consistent across both evaluation years but varies substantially in magnitude, with the 2006 gain more than three times the 2007 gain — a discrepancy the sources report without explanation ([Third-party research note, document_2.txt](document_2.txt)). The finding carries weight because it is anchored in a primary research paper and has been summarized accurately by a secondary note; it is weakened by the derivative nature of the secondary source, the absence of absolute baseline values and significance testing, and the restriction of the evidence to two TREC collections within a single study ([Bridging the Gap, arXiv:1608.01972](https://arxiv.org/abs/1608.01972); [Third-party research note, document_2.txt](document_2.txt)). Within those boundaries, the reported advantage of semantic similarity over BM25 is real, positive, and quantitatively specified as 19% and 6% for the two evaluation years respectively.

## References

Bridging the gap: Incorporating a semantic similarity measure for effectively mapping PubMed queries to documents (arXiv:1608.01972) [Document 1]. (n.d.). arXiv. https://arxiv.org/abs/1608.01972

Third-party research note: PubMed query–document mapping [Document 2]. (n.d.).