# Quantifying the Performance Advantage of the Embedding-Based Semantic Similarity Measure over BM25 in PubMed Query–Document Mapping

## Executive Summary

The evidence supplied by the primary research source indicates that the semantic similarity (embedding) approach does **outperform BM25**, and the magnitude of that advantage is **19% on the TREC 2006 collection and 6% on the TREC 2007 collection**, measured in average precision ([Bridging the Gap, n.d.](https://arxiv.org/abs/1608.01972)). These are the only two quantified figures available in the provided material, and they are explicitly attributed to the embedding method's effect on BM25's retrieval effectiveness. A secondary, third-party research note in the same evidence set makes a directly contradictory claim — namely that BM25 outperforms the embedding approach by the same two figures ([Third-party research note, n.d.](document_2.txt)). Because the primary source is a documented research paper that anchors its numbers to a specific results table (Table 4) and to named test collections, while the secondary note provides no methodology, no table reference, and no replication detail, the primary source must be given precedence. The defensible answer to the query is therefore: **the embedding approach exceeds BM25 by 19% on TREC 2006 and 6% on TREC 2007, with the 2006 gain being roughly three times larger than the 2007 gain.**

## Background and Framing of the Query

The question — "By how much does their similarity measure (the embedding approach) outperform BM25?" — contains an embedded premise: that the embedding approach is the stronger of the two methods. Establishing that premise is a necessary first step before any effect size can be reported, because the two sources provided disagree about the *direction* of the effect, not merely its magnitude.

The primary source, a paper titled *Bridging the Gap: Incorporating a Semantic Similarity Measure for Effectively Mapping PubMed Queries to Documents*, reports experimental results from the TREC biomedical retrieval tracks. It states plainly that "BM25 performs better than TFIDF and CENTROID" before adding that "the embedding approach boosts the average precision of BM25 by 19% and 6% on TREC 2006 and 2007, respectively" ([Bridging the Gap, n.d.](https://arxiv.org/abs/1608.01972)). This framing places BM25 as a strong lexical baseline that is subsequently *improved upon* by a semantic/embedding component. The paper also notes that "CENTROID provides scores lower than BM25 and SEM approaches," where SEM denotes the semantic embedding method ([Bridging the Gap, n.d.](https://arxiv.org/abs/1608.01972)).

The secondary source, described as a "third-party research note," reverses this relationship: it asserts that "BM25 outperforms the proposed semantic-similarity (embedding) approach: BM25 raises average precision by 19% on TREC 2006 and by 6% on TREC 2007 over the embedding approach" ([Third-party research note, n.d.](document_2.txt)). Notably, the note preserves the identical magnitudes (19% and 6%) and the identical collections (TREC 2006 and TREC 2007) while inverting who benefits. That pattern — identical numbers, reversed attribution — is characteristic of a transcription or interpretation error rather than an independent experimental finding, a point developed further below.

## The Direct Answer: Magnitude of the Advantage

Taking the primary source as authoritative, the embedding approach's advantage over BM25 is as follows.

| Test Collection | Reported Improvement of the Embedding Approach over BM25 | Source |
|---|---|---|
| TREC 2006 | 19% (average precision) | ([Bridging the Gap, n.d.](https://arxiv.org/abs/1608.01972)) |
| TREC 2007 | 6% (average precision) | ([Bridging the Gap, n.d.](https://arxiv.org/abs/1608.01972)) |
| Arithmetic mean of the two reported values | ≈12.5% | Computed from the two figures above; not reported as such by the source |

Three observations follow directly from this table.

First, the advantage is **not uniform across collections**. The gain recorded on TREC 2006 (19%) is more than three times the gain recorded on TREC 2007 (6%). Any claim that the embedding approach delivers "a roughly 12.5% improvement" would be an arithmetic artifact of averaging two heterogeneous results rather than a finding reported in the literature; the source reports the two collections separately and does not aggregate them ([Bridging the Gap, n.d.](https://arxiv.org/abs/1608.01972)). The safest characterization is that the benefit is **real but collection-dependent**.

Second, the metric in question is **average precision**, the standard summary measure used in TREC-style evaluations, which rewards retrieving relevant documents early in the ranked list ([Bridging the Gap, n.d.](https://arxiv.org/abs/1608.01972)). The reported percentages therefore describe changes in ranking quality, not in raw recall or in end-to-end latency or cost.

Third, the source does **not** state whether the 19% and 6% figures are relative improvements (a percentage change with respect to BM25's own score) or absolute percentage-point differences in average precision ([Bridging the Gap, n.d.](https://arxiv.org/abs/1608.01972)). This distinction is material. A 19% *relative* gain is a modest-to-moderate effect; a 19 *percentage-point* absolute gain in average precision would be a very large one. Because the source is silent on this point, the figure should be reported with its ambiguity intact rather than silently resolved in either direction.

## The Broader Ranking of Methods

The improvement over BM25 must be read within the fuller comparison that the primary source provides. That source establishes a clear ordering among four approaches: BM25, TFIDF, CENTROID, and the semantic embedding method (SEM).

| Method | Position Relative to Others | Source |
|---|---|---|
| BM25 | Better than TFIDF and CENTROID | ([Bridging the Gap, n.d.](https://arxiv.org/abs/1608.01972)) |
| TFIDF | Inferior to BM25 | ([Bridging the Gap, n.d.](https://arxiv.org/abs/1608.01972)) |
| CENTROID | Scores lower than both BM25 and SEM | ([Bridging the Gap, n.d.](https://arxiv.org/abs/1608.01972)) |
| Semantic embedding approach (SEM) | Outperforms BM25, and by extension TFIDF and CENTROID | ([Bridging the Gap, n.d.](https://arxiv.org/abs/1608.01972)) |

Two conclusions follow. First, BM25 is not a weak baseline in this experimental setting — it beats two competing lexical and centroid-based methods outright, which is precisely why an improvement over BM25 is a meaningful result. Second, CENTROID is the weakest of the four, ranking below both BM25 and the embedding method ([Bridging the Gap, n.d.](https://arxiv.org/abs/1608.01972)). The embedding approach therefore sits at the top of the reported hierarchy, which is consistent with the premise of the query.

## Conflicting Evidence and Source Reliability

The central methodological challenge in answering the query is that the two available sources contradict one another on direction. The table below summarizes the divergence.

| Aspect | Primary Source (arXiv:1608.01972) | Third-Party Research Note |
|---|---|---|
| Who outperforms whom | Embedding approach improves on BM25 | BM25 improves on the embedding approach |
| TREC 2006 figure | 19% boost to BM25's average precision | 19% boost by BM25 over the embedding approach |
| TREC 2007 figure | 6% boost to BM25's average precision | 6% boost by BM25 over the embedding approach |
| Supporting apparatus | References a specific results table (Table 4) | No table, no methodological detail |
| Provenance | Named research paper with an arXiv identifier | Unattributed "third-party research note" |
| Citation | ([Bridging the Gap, n.d.](https://arxiv.org/abs/1608.01972)) | ([Third-party research note, n.d.](document_2.txt)) |

Three considerations favor the primary source.

**Provenance and verifiability.** The primary source is a titled research paper carrying the identifier arXiv:1608.01972, and it grounds its claim in a specific artifact — "As shown in Table 4" ([Bridging the Gap, n.d.](https://arxiv.org/abs/1608.01972)). The secondary note is explicitly labeled third-party and supplies no equivalent anchor ([Third-party research note, n.d.](document_2.txt)).

**Internal consistency.** The primary source's narrative is coherent throughout: BM25 beats the weaker lexical baselines, and then the embedding method is layered on to push performance higher, with CENTROID remaining the laggard ([Bridging the Gap, n.d.](https://arxiv.org/abs/1608.01972)). This is also consistent with the paper's stated purpose of "bridging the gap" by *incorporating* a semantic similarity measure — a framing that only makes sense if the semantic measure adds value to the existing lexical retrieval.

**Absence of independent corroboration in the secondary source.** Crucially, the secondary note does not present different experiments or different numbers. It reports the *same* 19% and 6% on the *same* two collections as the primary paper, merely inverting the direction ([Third-party research note, n.d.](document_2.txt)). A genuinely independent replication that produced opposite conclusions would be expected to report its own experimental setup, not a verbatim restatement of the original values. The most parsimonious explanation is that the note misread or mis-transcribed the original finding.

For these reasons, the note should be treated as an unreliable secondary account and should not be used to reverse the primary result, even though it is presented as newer and is styled as a "research note."

## Limitations and Caveats

An objective answer must acknowledge what the provided evidence does not establish.

**Only two collections are covered.** Both the 19% and 6% figures derive from TREC 2006 and TREC 2007 respectively ([Bridging the Gap, n.d.](https://arxiv.org/abs/1608.01972)). No evidence is provided about performance on subsequent TREC collections, on other biomedical corpora, or on operational PubMed query logs. The collection-to-collection variation between 19% and 6% is itself a warning against treating either figure as a stable constant.

**No absolute scores are given.** The source reports percentage changes but not the underlying average precision values ([Bridging the Gap, n.d.](https://arxiv.org/abs/1608.01972)). Without the baseline and treatment scores, the practical significance of the improvement cannot be fully judged, nor can the relative-versus-absolute question be settled.

**No significance testing is reported.** The provided material contains no information about statistical significance, confidence intervals, or the number of queries evaluated ([Bridging the Gap, n.d.](https://arxiv.org/abs/1608.01972)). The magnitude of the TREC 2007 gain (6%) is the kind of effect that could plausibly fall within the range of run-to-run variation absent significance reporting.

**Directional conflict remains formally unresolved.** Although the reliability analysis strongly favors the primary source, the contradiction between the two documents is not eliminated by the provided material. A rigorous reader should note that the answer rests on a source-prioritization judgment, not on an independent verification.

## Conclusion

On the strength of the most reliable source available, the answer to the query is that **the embedding-based semantic similarity measure outperforms BM25 by 19% in average precision on TREC 2006 and by 6% on TREC 2007** ([Bridging the Gap, n.d.](https://arxiv.org/abs/1608.01972)). The advantage is substantial in one year and modest in the other, which suggests that a single headline number would misrepresent the finding.

The counterclaim in the third-party note — that BM25 instead outperforms the embedding approach by those same margins ([Third-party research note, n.d.](document_2.txt)) — is best understood as an inverted reading of the primary result rather than as evidence of a rival finding, given that it reproduces the original magnitudes and collections without any independent experimental apparatus. It should not be used to overturn the primary result, and any downstream use of this comparison should cite the original paper directly and report the ambiguity between relative and absolute improvement, the absence of significance testing, and the two-collection scope as explicit limitations.

## References

Bridging the Gap: Incorporating a Semantic Similarity Measure for Effectively Mapping PubMed Queries to Documents (arXiv:1608.01972). Source: document_1.txt. <https://arxiv.org/abs/1608.01972>

Third-party research note: PubMed query-document mapping. Source: document_2.txt.