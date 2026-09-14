# By How Much Does the Embedding-Based Similarity Measure Outperform BM25? Evidence from TREC and PubMed Evaluations

## Introduction

The query asks for the magnitude by which an embedding-based semantic similarity measure outperforms BM25. The provided evidence comes from a primary paper, “Bridging the Gap: Incorporating a Semantic Similarity Measure for Effectively Mapping PubMed Queries to Documents” (arXiv:1608.01972), represented as document_1.txt, and a third-party research note, document_2.txt. The primary paper reports TREC average precision (AP) and PubMed NDCG@20 results. The answer is not a single number: on TREC 2006 and TREC 2007, the semantic embedding approach outperforms BM25 by 19% and 6% relative AP, respectively ([document_1.txt, 2016](https://arxiv.org/abs/1608.01972)). On PubMed user queries, the semantic measure alone does not outperform BM25; it improves BM25 only in hybrid configurations ([document_1.txt, 2016](https://arxiv.org/abs/1608.01972)). This report details those deltas, reconciles a contradictory third-party claim, and explains the practical implications.

## TREC Results: Embedding Approach Outperforms BM25 by 19% and 6%

### Exact average precision figures

The primary source reports AP for TFIDF, BM25, CENTROID, and SEM—the semantic embedding measure—on TREC 2006 and TREC 2007 ([document_1.txt, 2016](https://arxiv.org/abs/1608.01972)). Table 1 reproduces those values.

| Method | TREC 2006 AP | TREC 2007 AP |
|---|---:|---:|
| TFIDF | 0.3018 | 0.2375 |
| BM25 | 0.3136 | 0.2463 |
| CENTROID | 0.2363 | 0.2459 |
| SEM (embedding) | 0.3732 | 0.2601 |

Data from ([document_1.txt, 2016](https://arxiv.org/abs/1608.01972)).

### Relative improvement calculations

For TREC 2006, BM25 = 0.3136 and SEM = 0.3732. The absolute difference is 0.3732 − 0.3136 = 0.0596. The relative improvement is 0.0596 / 0.3136 ≈ 0.1900, or 19.00%. For TREC 2007, BM25 = 0.2463 and SEM = 0.2601. The absolute difference is 0.2601 − 0.2463 = 0.0138. The relative improvement is 0.0138 / 0.2463 ≈ 0.0560, or 5.60%, which the source rounds to 6%. The primary source states directly that “the embedding approach boosts the average precision of BM25 by 19% and 6% on TREC 2006 and 2007, respectively” ([document_1.txt, 2016](https://arxiv.org/abs/1608.01972)). The same source notes that the semantic measure was used alone, with no other feature for ranking documents ([document_1.txt, 2016](https://arxiv.org/abs/1608.01972)). Therefore, on TREC 2006, the answer is approximately 19% relative AP gain; on TREC 2007, approximately 6% relative AP gain.

### Comparison with TFIDF and CENTROID

BM25 itself performs better than TFIDF and CENTROID ([document_1.txt, 2016](https://arxiv.org/abs/1608.01972)). On TREC 2006, BM25 (0.3136) exceeds TFIDF (0.3018) and CENTROID (0.2363). On TREC 2007, BM25 (0.2463) exceeds TFIDF (0.2375) and CENTROID (0.2459), though the margin over CENTROID is smaller. CENTROID provides scores lower than BM25 and SEM in both years ([document_1.txt, 2016](https://arxiv.org/abs/1608.01972)). This matters because the embedding measure’s advantage is not merely against a weak baseline; it improves over a strong lexical BM25 baseline.

## PubMed User Queries: The Embedding Measure Does Not Outperform BM25 Alone

### NDCG@20 results

The PubMed experiments use a different metric, NDCG@20, and a different query population: user queries rather than TREC topics ([document_1.txt, 2016](https://arxiv.org/abs/1608.01972)). Table 2 reports the available results.

| Method | NDCG@20 | Relative improvement over BM25 |
|---|---:|---:|
| BM25 | 0.1495 | — |
| BM25 + SEMTitle | 0.1839 | 23.03% |
| BM25 + SEMAbstract | 0.1592 | 6.51% |

Data from ([document_1.txt, 2016](https://arxiv.org/abs/1608.01972)).

### What the PubMed results mean

The primary source states: “Although our semantic measure alone produces better ranking scores on the TREC set, this does not apply to user queries in PubMed” ([document_1.txt, 2016](https://arxiv.org/abs/1608.01972)). In other words, the embedding approach alone does not outperform BM25 on PubMed user queries. The reported gains come from adding the semantic measure to BM25: BM25 + SEMTitle improves NDCG@20 from 0.1495 to 0.1839, a 23.03% relative gain; BM25 + SEMAbstract improves it to 0.1592, a 6.51% relative gain ([document_1.txt, 2016](https://arxiv.org/abs/1608.01972)). Thus, for PubMed user