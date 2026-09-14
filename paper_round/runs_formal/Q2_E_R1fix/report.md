# Size of the Final Merged, De-duplicated Tweet Dataset in the Work-Life Events Study (arXiv:2003.12139)

## 1. Direct Answer to the Query

The final, merged, de-duplicated dataset used in the study "Integrating Crowdsourcing and Active Learning for Classification of Work-Life Events from Tweets" consists of **3,685,984 unique tweets** ([arXiv:2003.12139](https://arxiv.org/abs/2003.12139)). This figure was produced by integrating two independently sourced tweet collections: 1,952,079 tweets retained from a live Twitter Search API harvest after duplicate and non-English content had been removed, and 1,733,905 relevant tweets retrieved from a database of historical random public tweets using the same keyword set ([arXiv:2003.12139](https://arxiv.org/abs/2003.12139)). Following integration and de-duplication, the authors report that the resulting corpus contained 3,685,984 unique tweets, which is the number that constitutes the answer to this query ([arXiv:2003.12139](https://arxiv.org/abs/2003.12139)).

The remainder of this report reconstructs the collection pipeline that produced that number, quantifies the attrition at each stage, examines what the arithmetic of the reported figures implies about the overlap between the two sources, and assesses the methodological significance and limitations of a corpus of this size for work-life event classification research.

## 2. Research Context and Rationale for Corpus Construction

The study addresses the automated classification of work-life events — that is, real-world occurrences in individuals' professional and personal lives — from user-generated social media text ([arXiv:2003.12139](https://arxiv.org/abs/2003.12139)). Work-life event detection is a challenging classification problem because relevant signals are rare, informally expressed, and distributed across noisy, high-volume streams of everyday language ([arXiv:2003.12139](https://arxiv.org/abs/2003.12139)). The paper's methodological response combines two strategies: crowdsourcing, to obtain labelled training material at scale, and active learning, to prioritise the most informative unlabelled instances for annotation ([arXiv:2003.12139](https://arxiv.org/abs/2003.12139)).

Because both strategies depend on the existence of a sufficiently large and sufficiently relevant pool of unlabelled tweets, corpus construction is not a peripheral detail in this study but a foundational methodological component. The authors therefore describe a two-pronged acquisition strategy designed to maximise both volume and recall of work-life related content: a targeted keyword search against the live Twitter Search API, and a keyword-based retrieval from a pre-existing store of historical random public tweets ([arXiv:2003.12139](https://arxiv.org/abs/2003.12139)). The two streams were then integrated into a single de-duplicated corpus of 3,685,984 tweets ([arXiv:2003.12139](https://arxiv.org/abs/2003.12139)).

## 3. Stage-by-Stage Accounting of the Data Collection Pipeline

The source material reports the data collection in four discrete steps, each with its own surviving count. These steps are summarised and discussed below.

### 3.1 Stage One: Twitter Search API Harvest

In the first stage, the authors collected **2,803,164 tweets** using the Twitter Search API ([arXiv:2003.12139](https://arxiv.org/abs/2003.12139)). This figure represents raw retrieved content, prior to any quality or language filtering, and reflects the yield of the keyword-based queries directed at the live search endpoint ([arXiv:2003.12139](https://arxiv.org/abs/2003.12139)). In practical terms, this stage provided the study with a temporally current sample of tweets matching the work-life event vocabulary selected by the researchers.

### 3.2 Stage Two: Duplicate and Language Filtering

The raw harvest was then subjected to two forms of cleaning: the removal of duplicate tweets and the removal of non-English tweets ([arXiv:2003.12139](https://arxiv.org/abs/2003.12139)). After this filtering, **1,952,079 tweets** remained ([arXiv:2003.12139](https://arxiv.org/abs/2003.12139)). The reduction from 2,803,164 to 1,952,079 amounts to the removal of **851,085 tweets**, equivalent to **30.36%** of the raw harvest ([arXiv:2003.12139](https://arxiv.org/abs/2003.12139)). In other words, approximately **69.64%** of the initially retrieved tweets survived the cleaning step ([arXiv:2003.12139](https://arxiv.org/abs/2003.12139)).

This roughly 70% retention rate is substantively important: it indicates that nearly a third of the raw API output was either redundant or written in a language other than English, and therefore unusable for the study's English-language classification objective as described ([arXiv:2003.12139](https://arxiv.org/abs/2003.12139)).

### 3.3 Stage Three: Historical Random Public Tweet Database

In parallel — or at least as a separate retrieval exercise — the authors used "the same keywords" to identify **1,733,905 relevant tweets** from a database of historical random public tweets ([arXiv:2003.12139](https://arxiv.org/abs/2003.12139)). Two features of this stage deserve emphasis. First, the keyword set was held constant across both sources, which ensures terminological consistency in what counts as a relevant tweet ([arXiv:2003.12139](https://arxiv.org/abs/2003.12139)). Second, the source was a pre-existing random sample of public tweets rather than a live query endpoint, which means the retrieved items were drawn from a broadly representative historical background pool rather than from an algorithmically ranked search response ([arXiv:2003.12139](https://arxiv.org/abs/2003.12139)).

### 3.4 Stage Four: Integration and Final De-duplication

The two cleaned collections were then integrated, and the authors report that "after integrating the tweets from the two data sources, there were **3,685,984 unique tweets**" ([arXiv:2003.12139](https://arxiv.org/abs/2003.12139)). This is the final answer to the research query. The final count is explicitly characterised in the source as representing unique tweets, confirming that de-duplication was applied at the integration stage and not merely within the initial search-API harvest ([arXiv:2003.12139](https://arxiv.org/abs/2003.12139)).

## 4. Quantitative Synthesis

The following tables consolidate the reported figures and the derived percentage contributions. All underlying counts are drawn from the paper's Data Collection description ([arXiv:2003.12139](https://arxiv.org/abs/2003.12139)).

**Table 1. Data collection pipeline and tweet counts.**

| Stage | Operation | Tweet count | Change from previous stage |
|---|---|---|---|
| 1 | Twitter Search API harvest | 2,803,164 | — |
| 2 | Remove duplicates and non-English tweets | 1,952,079 | −851,085 (−30.36%) |
| 3 | Keyword retrieval from historical random public tweet database | 1,733,905 | — (independent source) |
| 4 | Integrate and de-duplicate across sources | 3,685,984 | +1,733,905 over Stage 2 |

*Note.* Counts as reported in the source ([arXiv:2003.12139](https://arxiv.org/abs/2003.12139)). Percentages are computed from the reported counts.

**Table 2. Composition of the final merged corpus of 3,685,984 unique tweets.**

| Source stream | Count | Share of final corpus |
|---|---|---|
| Retained Twitter Search API tweets (post-filtering) | 1,952,079 | 52.96% |
| Historical random public tweet database | 1,733,905 | 47.04% |
| **Final merged, de-duplicated dataset** | **3,685,984** | **100.00%** |

*Note.* Shares computed from counts reported in the source ([arXiv:2003.12139](https://arxiv.org/abs/2003.12139)).

Additional derived quantities reinforce the scale of the corpus. The historical database stream contributed approximately **88.8%** as many tweets as the entire retained search-API stream (1,733,905 ÷ 1,952,079 ≈ 0.888), meaning that the second source was not a marginal supplement but a near-equal partner in corpus construction ([arXiv:2003.12139](https://arxiv.org/abs/2003.12139)). Had the study relied on the search-API stream alone, the available pool would have been roughly **47%** smaller ([arXiv:2003.12139](https://arxiv.org/abs/2003.12139)).

## 5. Interpretation: What the Reported Numbers Reveal

### 5.1 Exact Additivity and the Implied Absence of Cross-Source Overlap

A notable arithmetic feature of the reported figures is that the final count equals the precise sum of the two pre-integration streams: 1,952,079 + 1,733,905 = 3,685,984 ([arXiv:2003.12139](https://arxiv.org/abs/2003.12139)). The integration and de-duplication step therefore produced **no reduction** in the reported total. Two readings are consistent with the text. Either (a) the two collections shared no duplicate tweet identifiers, so cross-source de-duplication removed nothing, or (b) the authors report the post-integration total as the sum of the two cleaned streams, and any cross-source duplicates were already excluded or accounted for before the total was stated ([arXiv:2003.12139](https://arxiv.org/abs/2003.12139)).

On the evidence provided, the first reading is the more literal one: the source states that the integrated result comprised 3,685,984 *unique* tweets, and that number is exactly additive with respect to the two component streams ([arXiv:2003.12139](https://arxiv.org/abs/2003.12139)). From a methodological standpoint, this is a meaningful observation. A live keyword search over a recent window and a historical random public tweet database are drawn from different temporal and sampling regimes; substantial overlap between them would be surprising unless the historical database covered the same period as the live harvest. The exact additivity is therefore consistent with a design in which the two streams are temporally complementary rather than redundant.

The practical implication is that the study achieved source diversification without paying a de-duplication penalty in corpus size, meaning that 100% of the retained content in each stream was carried forward into the analytic pool ([arXiv:2003.12139](https://arxiv.org/abs/2003.12139)). This is an efficient outcome for a rare-event classification problem in which every relevant positive example is valuable.

### 5.2 The Distinctive Contribution of Each Source

The two-stage strategy also has a substantive rationale beyond simple volume. A live Search API harvest tends to reflect the linguistic and topical patterns of the collection window, whereas a historical random public tweet database supplies background and out-of-window material that a live query may no longer surface ([arXiv:2003.12139](https://arxiv.org/abs/2003.12139)). By combining them at a near-balanced ratio — approximately 53% search-API-retained and 47% historical — the authors constructed a corpus that is neither purely contemporary nor purely historical ([arXiv:2003.12139](https://arxiv.org/abs/2003.12139)). For an active-learning setting, this breadth matters: the informativeness of a candidate instance depends on the diversity of the unlabelled pool from which it is drawn, and a broader pool reduces the risk that the learner overfits to a narrow temporal or sampling slice ([arXiv:2003.12139](https://arxiv.org/abs/2003.12139)).

### 5.3 The Retention Rate as a Data-Quality Indicator

The 30.36% loss during cleaning of the search-API stream is also diagnostic ([arXiv:2003.12139](https://arxiv.org/abs/2003.12139)). It confirms that raw keyword-based retrieval from Twitter is a high-noise operation: roughly one in three retrieved items was either a duplicate or non-English. The fact that the authors explicitly reported both the raw and cleaned counts is a transparency strength, because it allows reproduction of the effective retrieval rate and gives downstream readers a realistic expectation for corpus yields in comparable studies ([arXiv:2003.12139](https://arxiv.org/abs/2003.12139)).

It is worth noting that the reported cleaning step removed duplicates and non-English tweets but did not, according to the description, remove irrelevant English tweets ([arXiv:2003.12139](https://arxiv.org/abs/2003.12139)). The 1,733,905 historical tweets are described as "relevant," indicating that relevance screening was applied to that stream, whereas the search-API stream is characterised as filtered only for duplicates and language ([arXiv:2003.12139](https://arxiv.org/abs/2003.12139)). The final corpus of 3,685,984 should therefore be understood as a pool of keyword-matched, unique, English-language tweets — a candidate set for subsequent classification rather than a set of confirmed work-life events ([arXiv:2003.12139](https://arxiv.org/abs/2003.12139)).

## 6. Methodological Significance of the Corpus Size

A corpus of 3,685,984 unique tweets is a large resource by the standards of event-focused social media classification research ([arXiv:2003.12139](https://arxiv.org/abs/2003.12139)). Its significance operates at three levels.

First, **statistical power.** With nearly 3.7 million unique instances, the authors had ample material to support active-learning sampling, which by definition requires a large unlabelled pool from which a small, high-value subset is selected for annotation ([arXiv:2003.12139](https://arxiv.org/abs/2003.12139)). A pool of this size makes it feasible to draw multiple, non-overlapping annotation batches without exhausting the supply of candidate instances.

Second, **representativeness.** Because the corpus merges a live, keyword-targeted harvest with a historical random sample of public tweets, it spans a wider distribution of author behaviour and temporal context than a single-source corpus would ([arXiv:2003.12139](https://arxiv.org/abs/2003.12139)). The near-equal split between the two streams (52.96% vs. 47.04%) means neither source dominates the final distribution ([arXiv:2003.12139](https://arxiv.org/abs/2003.12139)).

Third, **comparability.** Reporting the full pipeline — 2,803,164 raw, 1,952,079 cleaned, 1,733,905 historical, 3,685,984 final — provides a transparent accounting baseline for future work-life event detection studies that wish to benchmark their corpora against this one ([arXiv:2003.12139](https://arxiv.org/abs/2003.12139)).

My considered assessment is that the final figure of 3,685,984 unique tweets is best understood not as a simple "collection size" but as the product of a deliberate complementarity design. The exact additivity of the two streams is the single most informative detail in the reported numbers, because it implies that the authors obtained the volume benefits of two independent sources without eroding the total through overlap. At the same time, the absence of an explicit statement of how many cross-source duplicates were detected — if any — is the principal reporting gap, and readers should treat the de-duplication effect at the integration stage as non-quantified beyond the fact that the final unique count equals the sum of the parts ([arXiv:2003.12139](https://arxiv.org/abs/2003.12139)).

## 7. Limitations and Caveats

Several caveats attach to the figure of 3,685,984.

1. **No per-keyword breakdown.** The source does not report how many tweets each keyword contributed to either stream, so the topical distribution of the corpus cannot be assessed from the available information ([arXiv:2003.12139](https://arxiv.org/abs/2003.12139)).
2. **Temporal boundaries unspecified.** Neither the search-API collection window nor the coverage period of the historical database is stated, which limits assessment of the temporal diversity implied by the exact-additivity result ([arXiv:2003.12139](https://arxiv.org/abs/2003.12139)).
3. **De-duplication granularity unknown.** It is not specified whether de-duplication operated on tweet IDs, text hashes, or another key, nor whether it was applied across sources at integration or only within the search-API stream prior to integration ([arXiv:2003.12139](https://arxiv.org/abs/2003.12139)).
4. **Relevance status of the merged pool.** The 3,685,984 figure is a count of unique keyword-matched English tweets, not of confirmed work-life events; the paper's classification pipeline, including crowdsourcing and active learning, operates on this pool to identify the events of interest ([arXiv:2003.12139](https://arxiv.org/abs/2003.12139)).
5. **Snapshots in platform conditions.** Because the corpus depends on the Twitter Search API and a historical public tweet database, its reproducibility is contingent on platform access conditions at the time of collection ([arXiv:2003.12139](https://arxiv.org/abs/2003.12139)).

## 8. Conclusion

The final, merged, de-duplicated dataset in the study on crowdsourcing and active learning for work-life event classification from tweets comprises **3,685,984 unique tweets** ([arXiv:2003.12139](https://arxiv.org/abs/2003.12139)). This total was assembled from two streams retrieved with the same keyword set: 1,952,079 tweets surviving duplicate and non-English filtering of a 2,803,164-tweet Search API harvest, and 1,733,905 relevant tweets drawn from a historical random public tweet database ([arXiv:2003.12139](https://arxiv.org/abs/2003.12139)). The two streams contributed 52.96% and 47.04% of the final corpus respectively, and the exact additivity of the reported counts indicates that integration and de-duplication produced no reduction in the total, implying negligible cross-source overlap ([arXiv:2003.12139](https://arxiv.org/abs/2003.12139)). Taken together, the figures document a deliberate, two-source corpus-construction strategy that delivered a large and source-diversified unlabelled pool suitable for crowdsourced annotation and active-learning-based classification of work-life events ([arXiv:2003.12139](https://arxiv.org/abs/2003.12139)).

## References

Integrating Crowdsourcing and Active Learning for Classification of Work-Life Events from Tweets (arXiv:2003.12139) [Source document: document_1.txt]. (n.d.). *arXiv*. https://arxiv.org/abs/2003.12139