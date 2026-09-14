# Final Dataset Size Report: The Merged, De-Duplicated Work-Life Events Tweet Corpus

## Executive Summary

The final, merged, de-duplicated dataset reported in *Integrating Crowdsourcing and Active Learning for Classification of Work-Life Events from Tweets* (arXiv:2003.12139) contains **3,685,984 unique tweets** ([Document_1.txt, n.d.](https://arxiv.org/abs/2003.12139)). This figure represents the consolidated output of a two-stream data collection strategy: a keyword-driven harvest from the Twitter search API and a keyword-matched extraction from a database of historical random public tweets. A corroborating third-party summary independently reiterates the same total, stating that "after merging both sources and removing duplicates, the final corpus contains 3,685,984 unique tweets" ([Document_2.txt, n.d.]). Because two separate documents converge on an identical value, the estimate can be treated as reliable for the purposes of understanding the corpus scale, while the underlying de-duplication mechanics remain only partially transparent, a caveat examined later in this report.

## Background and Context of the Corpus

### Research Objective

The study under review addresses a practical problem in computational social science: automatically identifying *work-life events* — such as job changes, promotions, resignations, or work-related transitions — from the informal, noisy language of social media posts. To pursue this goal, the authors combine two annotation and modelling strategies: crowdsourcing, which distributes labelling work across many human annotators, and active learning, which selectively prioritises the most informative unlabelled examples for human review ([Document_1.txt, n.d.](https://arxiv.org/abs/2003.12139)). Both strategies are data-hungry: crowdsourcing requires a sufficient pool of items to distribute efficiently, and active learning requires a large unlabelled reservoir from which to sample strategically. The size of the underlying corpus is therefore not an incidental detail but a structural determinant of what the methodology can achieve ([Document_2.txt, n.d.]).

### Why Dataset Scale Matters Here

A corpus of several million tweets provides two distinct advantages. First, it increases the probability that rarer work-life event types — which are naturally low-frequency in a random sample of public discourse — are represented in sufficient numbers to support supervised classification. Second, it gives active learning a broad candidate space, allowing the sampling strategy to select genuinely uncertain or diverse instances rather than being forced to exhaust a small pool. The magnitude of 3,685,984 tweets situates this corpus firmly in the "large-scale" category for social media NLP research, and this scale is the direct product of the two-source collection design described below ([Document_1.txt, n.d.](https://arxiv.org/abs/2003.12139)).

## Data Collection Procedure

The collection pipeline proceeded in three clearly delineated stages, as reported in the Results section of the paper.

### Stage 1: Twitter Search API Harvest

The researchers first queried the Twitter search API using a defined set of keywords, retrieving **2,803,164 tweets** ([Document_1.txt, n.d.](https://arxiv.org/abs/2003.12139)). This raw pull was then subjected to two cleaning operations: removal of duplicate records and removal of non-English tweets. After these filters were applied, **1,952,079 tweets** remained eligible for inclusion ([Document_1.txt, n.d.](https://arxiv.org/abs/2003.12139)). In other words, 851,085 records — roughly 30.4% of the original API pull — were discarded during this screening step.

### Stage 2: Historical Random Public Tweet Database

Independently, the researchers applied the *same keywords* to a database of historical random public tweets ([Document_1.txt, n.d.](https://arxiv.org/abs/2003.12139)). This second stream yielded **1,733,905 relevant tweets**. The use of an identical keyword set across both streams is methodologically important: it ensures that the resulting records are conceptually comparable and can be pooled without semantic mismatch, even though the sampling frames differ (a live search API versus a retrospective random archive) ([Document_1.txt, n.d.](https://arxiv.org/abs/2003.12139)).

### Stage 3: Integration and De-Duplication

The two cleaned streams were then integrated and de-duplicated, producing a single consolidated corpus of **3,685,984 unique tweets** ([Document_1.txt, n.d.](https://arxiv.org/abs/2003.12139)). This merged corpus is the dataset subsequently used for crowdsourcing and active-learning classification ([Document_2.txt, n.d.]).

#### Table 1. Data Collection Stages and Record Counts

| Stage | Operation | Records | Source |
|---|---|---|---|
| 1a | Tweets collected via Twitter search API | 2,803,164 | ([Document_1.txt, n.d.](https://arxiv.org/abs/2003.12139)) |
| 1b | After removing duplicates and non-English tweets | 1,952,079 | ([Document_1.txt, n.d.](https://arxiv.org/abs/2003.12139)) |
| 2 | Keyword-matched tweets from historical random public tweet database | 1,733,905 | ([Document_1.txt, n.d.](https://arxiv.org/abs/2003.12139)) |
| 3 | **Final merged, de-duplicated corpus** | **3,685,984** | ([Document_1.txt, n.d.](https://arxiv.org/abs/2003.12139); [Document_2.txt, n.d.]) |

## The Definitive Answer: Final Dataset Size

### Direct Response to the Query

**The final merged, de-duplicated tweets dataset contains 3,685,984 unique tweets.** This is stated explicitly in the primary source: "After integrating the tweets from the two data sources, there were 3,685,984 unique tweets" ([Document_1.txt, n.d.](https://arxiv.org/abs/2003.12139)). The secondary source corroborates this without variation: the final corpus "contains 3,685,984 unique tweets, which is then used for crowdsourcing and active-learning classification" ([Document_2.txt, n.d.]).

### Arithmetic Verification and Internal Consistency

A useful test of any reported aggregate is whether it reconciles with its component parts. In this case:

1,952,079 (Stream 1, post-cleaning) + 1,733,905 (Stream 2) = **3,685,984**

The sum matches the reported final figure exactly. This is a striking and analytically meaningful result. It implies one of two possibilities:

- **Interpretation A (strict reading):** The two streams were entirely disjoint after their respective cleaning steps, such that no tweet appeared in both. Under this reading, the reported 3,685,984 is genuinely the count of unique tweets, and the "de-duplication" step removed only duplicates that had already been eliminated within each stream.
- **Interpretation B (looser reading):** The reported figure is the simple aggregate of the two cleaned sets, and cross-source de-duplication either found no overlap or was subsumed into the per-stream cleaning described in Stage 1.

Both readings converge on the same headline number, and the secondary source — which explicitly frames the total as the product of "merging both sources and removing duplicates" — supports the view that 3,685,984 is intended as a *unique-tweet* count rather than a raw sum ([Document_2.txt, n.d.]). My own assessment is that 3,685,984 should be accepted as the authoritative dataset size for descriptive purposes, while acknowledging that the absence of a documented cross-source overlap count means the figure's precision depends on an unstated assumption of near-zero inter-source duplication.

#### Table 2. Composition of the Final Corpus

| Contribution | Tweets | Share of Final Corpus |
|---|---|---|
| Twitter search API (post-cleaning) | 1,952,079 | ≈ 52.96% |
| Historical random public tweet database | 1,733,905 | ≈ 47.04% |
| **Total (merged, de-duplicated)** | **3,685,984** | **100.00%** |

## Interpretation: What the Numbers Reveal About the Pipeline

### Yield and Attrition Analysis

The search-API stream experienced substantial attrition: 2,803,164 raw tweets were reduced to 1,952,079, a loss of 851,085 records, or approximately 30.4% of the initial harvest ([Document_1.txt, n.d.](https://arxiv.org/abs/2003.12139)). This retention rate of roughly 69.6% is consistent with the combined effect of two distinct filters — duplicate removal and language restriction — each of which independently removes a non-trivial fraction of raw keyword-matched tweets. Duplicates are common in API-based harvesting when queries overlap or when the same content is retweeted, while non-English removal is a broad filter that can eliminate a substantial share of globally sourced keyword matches.

By contrast, the historical database stream is reported as producing 1,733,905 *relevant* tweets with no intermediate raw count disclosed ([Document_1.txt, n.d.](https://arxiv.org/abs/2003.12139)). This asymmetry in reporting means that the cleaning efficiency of the second stream cannot be evaluated, and it also means the *relative* quality of the two streams cannot be directly compared.

### The Cross-Source Duplication Question

The most analytically interesting feature of the reported figures is the exact additivity described above. When two independent keyword-driven streams are pooled, some overlap would ordinarily be expected, particularly if the same keywords were used and the historical archive covers a period partially overlapping the live API window. The fact that the merged total equals the arithmetic sum of the parts suggests that overlap was negligible, or that any overlap was resolved in a manner not separately documented ([Document_1.txt, n.d.](https://arxiv.org/abs/2003.12139)). This is not a contradiction, but it is a transparency gap worth noting for anyone seeking to replicate the corpus construction.

### Scale Relative to the Inputs

The final corpus is approximately 1.31 times the size of the raw search-API harvest and roughly 1.89 times the size of the cleaned search-API subset alone. It is approximately 2.13 times the size of the historical-database contribution. These ratios confirm that neither source alone would have delivered the full corpus: the two-stream design roughly doubled the available data relative to what the live API query alone produced after cleaning ([Document_1.txt, n.d.](https://arxiv.org/abs/2003.12139)).

## Significance of a 3.69-Million-Tweet Corpus

A dataset of 3,685,984 tweets has practical consequences for the research design. For crowdsourcing, a pool of this magnitude means that annotation resources can be concentrated on a stratified or sampled subset without risking coverage gaps, because the underlying population is large enough to support multiple sampling strategies. For active learning, the size of the unlabelled pool directly affects how much statistical leverage the selection strategy can extract per annotation dollar: with millions of candidates, the algorithm can prioritise boundary cases and diverse instances rather than settling for whatever happens to be available ([Document_2.txt, n.d.]).

It is also worth emphasising that the corpus is documented as *unique* tweets, not merely aggregated records. Uniqueness matters because duplicate text in a training or evaluation set can inflate apparent model performance and distort annotation workloads — a well-known hazard in social media datasets where retweets and near-duplicate phrasing are pervasive ([Document_1.txt, n.d.](https://arxiv.org/abs/2003.12139)). The reported de-duplication step therefore protects the validity of downstream classification results, not merely the tidiness of the dataset.

## Limitations, Assumptions, and Source Reliability

### Primary versus Secondary Evidence

The two documents differ considerably in authority. Document_1.txt is the primary account, drawn from the Results :: Data Collection section of the underlying paper, and it supplies the granular stage-by-stage counts (2,803,164; 1,952,079; 1,733,905; 3,685,984) ([Document_1.txt, n.d.](https://arxiv.org/abs/2003.12139)). Document_2.txt is a third-party summary that provides a high-level restatement and, importantly, confirms both the final total and the framing of the corpus as merged and de-duplicated ([Document_2.txt, n.d.]). Given the instruction to prioritise more reliable sources, the primary paper is treated here as the evidentiary basis for all numeric claims, with the summary serving only as independent corroboration of the headline figure.

### Unresolved Methodological Details

Three details are not specified in the available information and should temper any over-confident reading of the numbers:

1. **No cross-source overlap count is reported.** The number of tweets appearing in both streams is not disclosed, which is why the exact additivity of the two cleaned sets requires interpretation rather than confirmation ([Document_1.txt, n.d.](https://arxiv.org/abs/2003.12139)).
2. **No raw count is given for the historical database stream.** Only the post-matching figure of 1,733,905 is available, so its cleaning yield is unknown ([Document_1.txt, n.d.](https://arxiv.org/abs/2003.12139)).
3. **The keyword set itself is not enumerated** in the supplied material, limiting assessment of how the two streams were made comparable ([Document_1.txt, n.d.](https://arxiv.org/abs/2003.12139)).

None of these gaps undermines the headline answer. They do, however, define the boundary between what can be asserted with confidence (the final corpus size) and what cannot (the precise redundancy structure of the two inputs).

## Conclusion

The question of how large the final merged, de-duplicated tweets dataset is has a clear and well-evidenced answer: **3,685,984 unique tweets** ([Document_1.txt, n.d.](https://arxiv.org/abs/2003.12139)). This total was assembled from 2,803,164 raw search-API tweets reduced to 1,952,079 after duplicate and language filtering, plus 1,733,905 keyword-matched tweets drawn from a historical random public tweet database ([Document_1.txt, n.d.](https://arxiv.org/abs/2003.12139)). The figure is reported identically by an independent third-party summary, which strengthens confidence in its accuracy ([Document_2.txt, n.d.]). The corpus is fairly balanced between its two sources, with the search-API stream contributing approximately 53.0% and the historical stream approximately 47.0% of the final total. My assessment is that 3,685,984 is the appropriate figure to cite for the dataset's size, with the caveat that the exact equality between the sum of the two cleaned streams and the reported merged total should prompt future users of this corpus to seek clarification on cross-source de-duplication before treating the two streams as guaranteed disjoint.

## References

Document_1.txt. (n.d.). *Integrating crowdsourcing and active learning for classification of work-life events from tweets* (arXiv:2003.12139) — Results: Data collection [Source document]. Retrieved September 14, 2026, from https://arxiv.org/abs/2003.12139

Document_2.txt. (n.d.). *Third-party summary: Work-life events tweet corpus* [Source document].