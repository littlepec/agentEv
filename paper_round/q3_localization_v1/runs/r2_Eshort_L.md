# Quantifying the Advantage of an Embedding-Based Semantic Similarity Measure over BM25 in PubMed Query–Document Mapping

## Abstract

This report answers a single, precisely bounded question: by how much does the embedding-based semantic similarity measure proposed by the authors of *Bridging the Gap: Incorporating a Semantic Similarity Measure for Effectively Mapping PubMed Queries to Documents* (arXiv:1608.01972) outperform BM25? According to the reported TREC experiments, the embedding approach raises the average precision of BM25 by **19% on TREC 2006** and by **6% on TREC 2007** ([document_1.txt](https://arxiv.org/abs/1608.01972)). A third-party research note summarizing the same study corroborates both figures exactly, stating that the semantic-similarity approach "improves retrieval over BM25: it raises average precision by 19% on TREC 2006 and by 6% on TREC 2007" ([document_2.txt](document_2.txt)). The same evidence base also establishes the broader ranking of methods in the study: BM25 outperforms both TFIDF and CENTROID, and CENTROID scores below both BM25 and the embedding approach ([document_1.txt](https://arxiv.org/abs/1608.01972); [document_2.txt](document_2.txt)). The two headline deltas — 19% and 6% — are therefore the direct, defensible answer to the query, though their interpretation requires care regarding what "percent improvement" means, how the gains vary by collection, and how much independent corroboration exists.

## Introduction and Scope

The task under examination is the mapping of biomedical queries to documents, specifically PubMed queries to candidate documents ([document_1.txt](https://arxiv.org/abs/1608.01972)). This is a classic ad hoc retrieval problem in which a system must rank a corpus of documents in order of relevance to a user's information need. The paper's central claim is that adding a semantic similarity component to an otherwise lexical retrieval pipeline yields measurable gains across standard test collections ([document_1.txt](https://arxiv.org/abs/1608.01972)). Because the question posed here is narrowly quantitative — *how much* does the embedding approach outperform BM25? — this report concentrates on the reported deltas, the collections on which they were measured, and the conditions and caveats attached to them.

## The Comparator: BM25 as the Strongest Lexical Baseline

Any claim of improvement is only as meaningful as the baseline it is measured against. In this study, BM25 serves as the primary lexical comparator, and the evidence indicates that it is the strongest of the non-semantic methods tested ([document_1.txt](https://arxiv.org/abs/1608.01972)). As stated in the TREC Experiments section of the source paper, "BM25 performs better than TFIDF and CENTROID" ([document_1.txt](https://arxiv.org/abs/1608.01972)). The third-party note independently repeats this ordering, observing that "BM25 itself outperforms TFIDF and CENTROID" ([document_2.txt](document_2.txt)).

This matters for interpreting the answer to the query. A 19% or 6% gain over BM25 is a substantially more demanding benchmark than the same gain over TFIDF or CENTROID, because BM25 is the hardest baseline to beat in this particular comparison set ([document_1.txt](https://arxiv.org/abs/1608.01972)). The reported advantage of the embedding approach is therefore an advantage over the *best* competing lexical method available in the study, not over a weak straw-man baseline.

## The Proposed Approach: Embedding-Based Semantic Similarity

The method at issue is described as an embedding approach that incorporates a semantic similarity measure, and it is abbreviated in the source material as "SEM" ([document_1.txt](https://arxiv.org/abs/1608.01972)). Its distinguishing property is that it captures semantic relatedness beyond exact or near-exact term overlap, which is the essential limitation of lexical models such as BM25, TFIDF, and CENTROID ([document_2.txt](document_2.txt)). Whereas lexical methods score documents primarily by term-matching statistics, the embedding approach is designed to bridge the vocabulary gap between how a query is phrased and how relevant documents express the same concept ([document_1.txt](https://arxiv.org/abs/1608.01972)). The paper's own framing — "Bridging the Gap" — reflects this intent ([document_1.txt](https://arxiv.org/abs/1608.01972)).

## The Central Finding: Magnitude of Improvement over BM25

The direct answer to the query is contained in the results of Table 4 of the source paper, as reported in the TREC Experiments section ([document_1.txt](https://arxiv.org/abs/1608.01972)). The embedding approach "boosts the average precision of BM25 by 19% and 6% on TREC 2006 and 2007, respectively" ([document_1.txt](https://arxiv.org/abs/1608.01972)). The third-party note reproduces these same two numbers without variation ([document_2.txt](document_2.txt)).

### TREC 2006: A 19% Gain in Average Precision

On the TREC 2006 collection, the semantic similarity measure increased average precision over BM25 by 19% ([document_1.txt](https://arxiv.org/abs/1608.01972)). This is the largest of the two reported deltas and represents the strongest evidence in the provided material for the value of semantic similarity in query–document mapping ([document_2.txt](document_2.txt)).

### TREC 2007: A 6% Gain in Average Precision

On the TREC 2007 collection, the same approach increased average precision over BM25 by 6% ([document_1.txt](https://arxiv.org/abs/1608.01972)). While smaller in magnitude, this remains a positive gain over the strongest lexical baseline in the study ([document_2.txt](document_2.txt)).

### Consolidated View of the Reported Deltas

| Test collection | Baseline compared | Change in average precision attributable to the embedding/SEM approach | Source |
|---|---|---|---|
| TREC 2006 | BM25 | **+19%** | ([document_1.txt](https://arxiv.org/abs/1608.01972); [document_2.txt](document_2.txt)) |
| TREC 2007 | BM25 | **+6%** | ([document_1.txt](https://arxiv.org/abs/1608.01972); [document_2.txt](document_2.txt)) |

| Method | Relative standing reported in the study |
|---|---|
| Embedding / semantic similarity (SEM) | Above BM25 on both TREC 2006 and TREC 2007 ([document_1.txt](https://arxiv.org/abs/1608.01972); [document_2.txt](document_2.txt)) |
| BM25 | Above TFIDF and CENTROID ([document_1.txt](https://arxiv.org/abs/1608.01972); [document_2.txt](document_2.txt)) |
| TFIDF | Below BM25 ([document_1.txt](https://arxiv.org/abs/1608.01972); [document_2.txt](document_2.txt)) |
| CENTROID | Below both BM25 and SEM ([document_1.txt](https://arxiv.org/abs/1608.01972); [document_2.txt](document_2.txt)) |

The tables make the answer compact and explicit: the embedding approach's measured advantage over BM25 is **19% on TREC 2006 and 6% on TREC 2007**, as measured by average precision ([document_1.txt](https://arxiv.org/abs/1608.01972)).

## Interpretation: What These Percentages Do and Do Not Establish

Several interpretive points follow directly from the provided evidence. First, the reported gains are expressed in **average precision**, not in precision at a single cutoff or in recall ([document_1.txt](https://arxiv.org/abs/1608.01972)). Average precision is a ranking-sensitive measure that rewards placing relevant documents near the top of the retrieved list, so a 19% average-precision gain implies a meaningful reordering of results in favor of relevant items on TREC 2006 ([document_2.txt](document_2.txt)).

Second, the two deltas differ substantially — 19% versus 6% — which indicates that the benefit of semantic similarity is **collection-dependent** rather than a fixed constant ([document_1.txt](https://arxiv.org/abs/1608.01972)). The sources do not attribute a cause to this difference, and no explanation should be inferred beyond what is stated. What the evidence does support is the claim that the direction of the effect is consistent across both collections, while its magnitude is not ([document_2.txt](document_2.txt)).

Third, the provided material does not specify whether the percentages are relative improvements over the BM25 baseline score or absolute percentage-point differences ([document_1.txt](https://arxiv.org/abs/1608.01972); [document_2.txt](document_2.txt)). Both sources phrase the result identically — "boosts the average precision of BM25 by 19% and 6%" ([document_1.txt](https://arxiv.org/abs/1608.01972)) — and neither supplies the underlying baseline values. This is a genuine reporting ambiguity: a 19% relative gain on a baseline average precision of, hypothetically, 0.20 would correspond to roughly 0.038 in absolute terms, whereas a 19-percentage-point absolute gain would imply a far larger effect. Consumers of this result should therefore treat 19% and 6% as the study's reported deltas while recognizing that the absolute scale cannot be reconstructed from the supplied information ([document_2.txt](document_2.txt)).

Fourth, the sources provide no variance estimates, confidence intervals, or significance tests ([document_1.txt](https://arxiv.org/abs/1608.01972)). Consequently, the reliability of the 6% figure in particular — the smaller of the two — cannot be assessed from the provided material alone ([document_2.txt](document_2.txt)).

## Position Relative to the Other Methods Tested

The query asks specifically about the embedding approach versus BM25, but the comparison is sharpened by the presence of two additional baselines. CENTROID "provides scores lower than BM25 and SEM approaches" ([document_1.txt](https://arxiv.org/abs/1608.01972)), and the third-party note confirms that "CENTROID scores below both BM25 and the embedding approach" ([document_2.txt](document_2.txt)). TFIDF likewise ranks below BM25 ([document_1.txt](https://arxiv.org/abs/1608.01972)). The resulting hierarchy is unambiguous in the provided evidence: embedding/SEM > BM25 > TFIDF and CENTROID, with CENTROID explicitly at the bottom of the comparison set ([document_2.txt](document_2.txt)). This ordering strengthens the significance of the reported 19% and 6% gains, because they are improvements over the strongest of three non-semantic alternatives ([document_1.txt](https://arxiv.org/abs/1608.01972)).

## Evidence Quality and Source Independence

Two unique documents appear in the supplied information: the primary source, identified as the paper *Bridging the Gap: Incorporating a Semantic Similarity Measure for Effectively Mapping PubMed Queries to Documents* (arXiv:1608.01972), specifically its TREC Experiments section ([document_1.txt](https://arxiv.org/abs/1608.01972)); and a "third-party research note" on PubMed query–document mapping ([document_2.txt](document_2.txt)). The primary source is the more authoritative of the two for the purpose of answering this query, because it is the original report of the experiments and references its own Table 4 ([document_1.txt](https://arxiv.org/abs/1608.01972)). The third-party note is useful as corroboration, but it repeats the same figures verbatim in substance and cites the primary source ([document_2.txt](document_2.txt)).

A critical observation is warranted here: although the supplied information repeats these two documents multiple times, the repetitions contain no new numbers, no alternative framing, and no additional collections ([document_1.txt](https://arxiv.org/abs/1608.01972); [document_2.txt](document_2.txt)). The apparent redundancy therefore does not constitute independent replication. The third-party note paraphrases the primary paper rather than testing it afresh ([document_2.txt](document_2.txt)). The effective evidence base for the 19% and 6% figures is thus a single experimental source with a single secondary summary, and the reliability assessment should reflect that constraint ([document_1.txt](https://arxiv.org/abs/1608.01972)).

A further contextual point follows from the arXiv identifier given in the source: "1608.01972" indicates an August 2016 submission, meaning the reported experiments predate the current date of 2026-09-14 by roughly a decade ([document_1.txt](https://arxiv.org/abs/1608.01972)). The retrieved evidence speaks only to the state of retrieval methods as of that work; no newer comparison is available within the provided material to indicate whether the magnitude of the advantage over BM25 has since grown, shrunk, or been overtaken by hybrid approaches.

## Limitations of the Present Evidence

Several limitations should be stated plainly. (1) Only two benchmark collections are represented — TREC 2006 and TREC 2007 — so the generalization of the 19% and 6% deltas to other corpora, domains, or query types is unsupported by the provided material ([document_1.txt](https://arxiv.org/abs/1608.01972)). (2) The metric is average precision only; no other retrieval metrics are reported in the supplied excerpts ([document_1.txt](https://arxiv.org/abs/1608.01972); [document_2.txt](document_2.txt)). (3) Baseline scores, absolute values, and statistical significance are absent, preventing verification of the relative-versus-absolute nature of the percentages ([document_2.txt](document_2.txt)). (4) The document set provided is dominated by repetitive copies of the same two texts, which creates an illusion of multiple corroborating sources where only two exist ([document_1.txt](https://arxiv.org/abs/1608.01972); [document_2.txt](document_2.txt)). (5) The study concerns PubMed query–document mapping specifically, so the findings should not be extended to general web retrieval without further evidence ([document_1.txt](https://arxiv.org/abs/1608.01972)).

## Conclusion

Based strictly on the provided information, the embedding-based semantic similarity measure outperforms BM25 by **19% on TREC 2006** and **6% on TREC 2007**, as measured by average precision ([document_1.txt](https://arxiv.org/abs/1608.01972); [document_2.txt](document_2.txt)). These gains are achieved against the strongest lexical baseline in the study, since BM25 itself outperforms TFIDF and CENTROID, and CENTROID ranks below both BM25 and the embedding approach ([document_1.txt](https://arxiv.org/abs/1608.01972); [document_2.txt](document_2.txt)). The effect direction is consistent across both collections; the effect size is not. The principal qualifications are that the gains are reported without baseline values or significance testing, that they derive from a single experimental source with one paraphrasing secondary note, and that they pertain to a 2016-era study of two TREC collections ([document_1.txt](https://arxiv.org/abs/1608.01972); [document_2.txt](document_2.txt)). Within those bounds, the answer to the query is unambiguous: **19% on TREC 2006 and 6% on TREC 2007** ([document_1.txt](https://arxiv.org/abs/1608.01972)).

## References

Document_1.txt. (n.d.). *Source (paper): Bridging the Gap: Incorporating a Semantic Similarity Measure for Effectively Mapping PubMed Queries to Documents (arXiv:1608.01972), Section: TREC Experiments.* [https://arxiv.org/abs/1608.01972](https://arxiv.org/abs/1608.01972)

Document_2.txt. (n.d.). *Third-party research note: PubMed query-document mapping.* [document_2.txt](document_2.txt)