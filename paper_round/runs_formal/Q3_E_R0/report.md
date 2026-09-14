# Quantifying the Embedding Approach's Improvement over BM25: Evidence from TREC 2006 and TREC 2007

## Executive Summary and Direct Answer

The query asks: "By how much does their similarity measure (the embedding approach) outperform BM25?" Based on the supplied evidence, the embedding approach boosts the average precision of BM25 by 19% on TREC 2006 and by 6% on TREC 2007 ([document_1.txt](https://arxiv.org/abs/1608.01972)). These are the only quantitative improvement figures provided. The source does not supply absolute average precision scores, confidence intervals, or significance tests, so the improvement should be understood as a relative percentage gain in average precision as reported in Table 4 of the source ([document_1.txt](https://arxiv.org/abs/1608.01972)). The most defensible opinion from the given information is that the embedding approach materially outperforms BM25 on both collections, with a much larger advantage on TREC 2006 than on TREC 2007, but the evidence is limited to a single repeated passage and therefore should not be overgeneralized ([document_1.txt](https://arxiv.org/abs/1608.01972)).

## Source and Evidence Base

### Source Identity

The evidence comes from document_1.txt, which identifies the source paper as "Bridging the Gap: Incorporating a Semantic Similarity Measure for Effectively Mapping PubMed Queries to Documents" (arXiv:1608.01972) ([document_1.txt](https://arxiv.org/abs/1608.01972)). The relevant section is "TREC Experiments" ([document_1.txt](https://arxiv.org/abs/1608.01972)). The paper's title indicates a biomedical retrieval context focused on mapping PubMed queries to documents ([document_1.txt](https://arxiv.org/abs/1608.01972)).

### Repetition and Independence

The provided information contains the same passage four times ([document_1.txt](https://arxiv.org/abs/1608.01972)). This repetition does not constitute four independent sources; it is one source reproduced multiple times ([document_1.txt](https://arxiv.org/abs/1608.01972)). Consequently, the evidence base is a single document with a single reported set of findings ([document_1.txt](https://arxiv.org/abs/1608.01972)).

### Reliability Considerations

The source is identified as an arXiv paper ([document_1.txt](https://arxiv.org/abs/1608.01972)). The excerpt does not state whether the work was peer-reviewed, nor does it provide the full experimental setup ([document_1.txt](https://arxiv.org/abs/1608.01972)). The reported figures are therefore taken as claims from that paper, not as independently replicated results ([document_1.txt](https://arxiv.org/abs/1608.01972)).

## Core Quantitative Findings

### TREC 2006

The source states that the embedding approach boosts the average precision of BM25 by 19% on TREC 2006 ([document_1.txt](https://arxiv.org/abs/1608.01972)).

### TREC 2007

The source states that the embedding approach boosts the average precision of BM25 by 6% on TREC 2007 ([document_1.txt](https://arxiv.org/abs/1608.01972)).

### Summary Table

| TREC collection | Reported improvement in average precision over BM25 |
| --- | --- |
| TREC 2006 | 19% |
| TREC 2007 | 6% |

Source: ([document_1.txt](https://arxiv.org/abs/1608.01972)).

### Comparative Magnitude

The 2006 gain is larger than the 2007 gain by 13 percentage points on the relative scale reported (19% − 6% = 13%) ([document_1.txt](https://arxiv.org/abs/1608.01972)). In ratio terms, the 2006 improvement is approximately 3.17 times the 2007 improvement (19 ÷ 6 ≈ 3.17) ([document_1.txt](https://arxiv.org/abs/1608.01972)). This indicates substantial year-to-year variability in the reported benefit of the embedding approach ([document_1.txt](https://arxiv.org/abs/1608.01972)).

## Comparative Context: BM25, TFIDF, CENTROID, and SEM

The same passage reports that BM25 performs better than TFIDF and CENTROID ([document_1.txt](https://arxiv.org/abs/1608.01972)). It also reports that CENTROID provides scores lower than BM25 and SEM approaches ([document_1.txt](https://arxiv.org/abs/1608.01972)). The embedding approach is discussed as improving BM25's average precision ([document_1.txt](https://arxiv.org/abs/1608.01972)). Because the embedding approach boosts BM25, and BM25 is reported as better than TFIDF and CENTROID, the reported ordering would imply that the embedding/SEM approach is above BM25, which in turn is above TFIDF and CENTROID if that ordering is transitive ([document_1.txt](https://arxiv.org/abs/1608.01972)). However, the excerpt does not quantify the TFIDF or CENTROID results; it only indicates direction ([document_1.txt](https://arxiv.org/abs/1608.01972)). The only numerical comparison supplied for the embedding approach versus BM25 is the 19% and 6% improvement on TREC 2006 and 2007 ([document_1.txt](https://arxiv.org/abs/1608.01972)).

## Interpretation of the Reported Gains

### Relative versus Absolute Improvement

The source says the embedding approach "boosts the average precision of BM25 by 19% and 6%" ([document_1.txt](https://arxiv.org/abs/1608.01972)). This is a relative improvement, meaning the embedding approach's average precision is 19% higher than BM25's on TREC 2006 and 6% higher on TREC 2007 ([document_1.txt](https://arxiv.org/abs/1608.01972)). It is not 19 or 6 absolute percentage points unless the baseline average precision is known ([document_1.txt](https://arxiv.org/abs/1608.01972)). The provided excerpt does not include the underlying average precision values, so absolute point gains cannot be computed from the given information ([document_1.txt](https://arxiv.org/abs/1608.01972)).

### Practical Significance

In my assessment, the 19% gain is more consequential than the 6% gain, but this assessment is based solely on the relative magnitudes reported in the source ([document_1.txt](https://arxiv.org/abs/1608.01972)). A 19% relative improvement in average precision is larger than a 6% relative improvement on the same metric ([document_1.txt](https://arxiv.org/abs/1608.01972)). However, without baseline scores, confidence intervals, or significance tests, the practical significance of these gains cannot be fully assessed from the excerpt alone ([document_1.txt](https://arxiv.org/abs/1608.01972)). The source presents the gains as table-based results but does not, in the provided text, report statistical validation ([document_1.txt](https://arxiv.org/abs/1608.01972)).

### Variability across Collections

The difference between 19% and 6% suggests that the embedding approach's advantage over BM25 is collection-dependent ([document_1.txt](https://arxiv.org/abs/1608.01972)). The provided information does not explain why TREC 2006 yielded a larger gain than TREC 2007 ([document_1.txt](https://arxiv.org/abs/1608.01972)). Possible explanations—such as differences in query difficulty, document collection, relevance judgments, or baseline strength—are not discussed in the excerpt ([document_1.txt](https://arxiv.org/abs/1608.01972)). Therefore, any explanation would be speculative beyond the source material ([document_1.txt](https://arxiv.org/abs/1608.01972)).

## Limitations and Methodological Cautions

### Single-Source Evidence

All findings come from one document, repeated four times ([document_1.txt](https://arxiv.org/abs/1608.01972)). There is no independent corroboration in the provided information ([document_1.txt](https://arxiv.org/abs/1608.01972)).

### Missing Experimental Details

The excerpt does not describe the embedding model, training data, similarity function, hyperparameters, or implementation details ([document_1.txt](https://arxiv.org/abs/1608.01972)). It also does not describe the TREC 2006 and 2007 collections, query sets, or relevance judgments ([document_1.txt](https://arxiv.org/abs/1608.01972)). The source uses the term "SEM" alongside "embedding approach" in the same passage, suggesting that SEM refers to the semantic similarity measure, but the excerpt does not explicitly define the acronym ([document_1.txt](https://arxiv.org/abs/1608.01972)). Similarly, the source's phrasing that the embedding approach "boosts the average precision of BM25" could imply either a standalone embedding approach or an embedding-augmented BM25 system; the excerpt does not clarify this distinction ([document_1.txt](https://arxiv.org/abs/1608.01972)).

### Missing Statistical Details

No confidence intervals, standard deviations, effect sizes, or significance tests are reported in the excerpt ([document_1.txt](https://arxiv.org/abs/1608.01972)). The 19% and 6% figures are presented as point estimates ([document_1.txt](https://arxiv.org/abs/1608.01972)).

### Table 4 Not Reproduced

The source references Table 4 as the basis for the findings ([document_1.txt](https://arxiv.org/abs/1608.01972)). The table itself is not included in the provided information, so the underlying numbers cannot be verified ([document_1.txt](https://arxiv.org/abs/1608.01972)).

### Generalization Risk

Because the evidence is limited to TREC 2006 and 2007 in a PubMed-oriented retrieval setting, the results should not be assumed to generalize to other collections, domains, or query types ([document_1.txt](https://arxiv.org/abs/1608.01972)).

## Implications for Retrieval Model Evaluation

The reported results support a specific conclusion: on TREC 2006 and TREC 2007, the embedding-based semantic similarity approach improved average precision over BM25 by 19% and 6%, respectively ([document_1.txt](https://arxiv.org/abs/1608.01972)). This positions the embedding approach as a potentially effective enhancement to a strong lexical baseline in biomedical query-document mapping ([document_1.txt](https://arxiv.org/abs/1608.01972)). At the same time, the variation between the two collections indicates that the benefit is not uniform ([document_1.txt](https://arxiv.org/abs/1608.01972)). For retrieval researchers and practitioners, the findings suggest that semantic similarity measures can add value beyond BM25, but the magnitude of that value may depend heavily on the evaluation collection ([document_1.txt](https://arxiv.org/abs/1608.01972)). The source also indicates that BM25 remains a stronger baseline than TFIDF and CENTROID, and that CENTROID underperforms both BM25 and SEM ([document_1.txt](https://arxiv.org/abs/1608.01972)). Thus, if the reported ordering is transitive, the embedding approach would be the strongest among the mentioned approaches, though the evidence for that ordering is directional except for the 19% and 6% BM25 comparisons ([document_1.txt](https://arxiv.org/abs/1608.01972)).

## Conclusion

The direct answer to the query is that the embedding approach outperforms BM25 by 19% on TREC 2006 and by 6% on TREC 2007 in terms of average precision, according to the supplied source ([document_1.txt](https://arxiv.org/abs/1608.01972)). The 2006 gain is approximately 3.17 times the 2007 gain ([document_1.txt](https://arxiv.org/abs/1608.01972)). These figures should be interpreted as relative improvements reported in the paper's TREC experiments, not as absolute point increases, and they are drawn from a single repeated passage rather than independent studies ([document_1.txt](https://arxiv.org/abs/1608.01972)). The most balanced conclusion is therefore that the embedding approach shows a clear but collection-dependent advantage over BM25, with a strong reported benefit in TREC 2006 and a more modest reported benefit in TREC 2007 ([document_1.txt](https://arxiv.org/abs/1608.01972)).

## References

document_1.txt. (n.d.). *Bridging the Gap: Incorporating a Semantic Similarity Measure for Effectively Mapping PubMed Queries to Documents* (arXiv:1608.01972). https://arxiv.org/abs/1608.01972