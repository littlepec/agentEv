# Determining the Final Merged, De-duplicated Tweet Dataset Size in Work-Life Event Classification Research

## Introduction

The query asks: “How large is their final (merged, de-duplicated) tweets dataset?” This report answers that question using two provided sources: the primary research paper *Integrating Crowdsourcing and Active Learning for Classification of Work-Life Events from Tweets* (arXiv:2003.12139) and a third-party summary of a work-life events tweet corpus. The primary source provides a detailed, step-by-step account of data collection and integration, reporting a final merged, de-duplicated dataset of 3,685,984 unique tweets ([Integrating Crowdsourcing and Active Learning, 2020](https://arxiv.org/abs/2003.12139)). The third-party summary reports a different final figure of 2,368,590 unique tweets ([Third-party summary, n.d.](document_2.txt)). This report evaluates both figures, prioritizes the primary source for its reliability and specificity, and concludes that the final dataset size is 3,685,984 unique tweets. The analysis below details the collection pipeline, compares the reported numbers, assesses source reliability, and discusses the implications of the discrepancy.

## Data Collection Methodology and Reported Figures

The primary source describes a two-source data collection strategy. The first source was the Twitter search API, and the second was a database of historical random public tweets. The authors applied filtering steps to ensure data quality before merging. The third-party summary provides only a high-level description without intermediate figures.

### Twitter Search API Collection

According to the primary source, the authors first collected 2,803,164 tweets using the Twitter search API ([Integrating Crowdsourcing and Active Learning, 2020](https://arxiv.org/abs/2003.12139)). This initial collection likely used keywords related to work-life events. After that, they filtered out duplicates and non-English tweets. The result was 1,952,079 tweets remaining ([Integrating Crowdsourcing and Active Learning, 2020](https://arxiv.org/abs/2003.12139)). This filtering step removed 851,085 tweets, representing approximately 30.36% of the initial API collection. The primary source does not specify the exact breakdown between duplicate removal and non-English filtering, but the combined effect is clear.

### Historical Random Public Tweets Database

Second, using the same keywords, the authors identified 1,733,905 relevant tweets from a database of historical random public tweets ([Integrating Crowdsourcing and Active Learning, 2020](https://arxiv.org/abs/2003.12139)). This database presumably provided a broader or longitudinal sample of public tweets that were not obtained through the search API. The primary source does not report a separate pre-filtering count for this database, so 1,733,905 appears to be the number of relevant tweets after any necessary filtering or selection based on the keywords.

### Integration and De-duplication

After integrating the tweets from the two data sources, the authors report that there were 3,685,984 unique tweets ([Integrating Crowdsourcing and Active Learning, 2020](https://arxiv.org/abs/2003.12139)). This is the final merged, de-duplicated dataset. Notably, the sum of the two post-filter sets is exactly 1,952,079 + 1,733,905 = 3,685,984. This exact match implies that the de-duplication process between the two sources did not reduce the total number, or that any cross-source duplicates were already eliminated before the final count. In other words, the final unique count equals the sum of the two cleaned source counts. This is an important observation because it suggests either that the two sources had no overlapping tweets or that the authors’ de-duplication step was applied within each source but not across sources in a way that reduced the total. Regardless, the primary source explicitly states that the integrated dataset contained 3,685,984 unique tweets.

## Final Dataset Size: The Primary Source Finding

The direct answer to the query, based on the primary source, is 3,685,984 unique tweets. The primary source states: “After integrating the tweets from the two data sources, there were 3,685,984 unique tweets” ([Integrating Crowdsourcing and Active Learning, 2020](https://arxiv.org/abs/2003.12139)). This figure represents the final merged, de-duplicated dataset used for subsequent crowdsourcing and active-learning classification. The number is derived from a transparent, reproducible pipeline: initial API collection (2,803,164), filtering (1,952,079), historical database extraction (1,733,905), and integration (3,685,984). Because the primary source provides these intermediate numbers, it allows for verification and contextualization of the final figure.

## Discrepancy with Third-Party Summary

The third-party summary reports a different final corpus size. It states: “After merging both sources and removing duplicates, the final corpus contains 2,368,590 unique tweets” ([Third-party summary, n.d.](document_2.txt)). This figure is 1,317,394 fewer than the primary source’s 3,685,984. The difference is substantial, representing approximately 35.75% of the primary source’s final count. To understand which figure is more reliable, it is necessary to compare the sources’ nature, specificity, and consistency.

### Quantitative Comparison

A side-by-side comparison of the available figures is presented in Table 1.

| Data collection stage | Primary source (document_1) | Third-party summary (document_2) |
|----------------------|----------------------------|----------------------------------|
| Initial tweets from Twitter search API | 2,803,164 | Not reported |
| After filtering duplicates and non-English tweets | 1,952,079 | Not reported |
| Relevant tweets from historical random public tweets database | 1,733,905 | Not reported |
| Final merged, de-duplicated dataset | 3,685,984 | 2,368,590 |
| Difference (primary minus third-party) | — | 1,317,394 |

Table 1. Comparison of reported dataset sizes across sources. The primary source provides intermediate counts, while the third-party summary provides only a final figure ([Integrating Crowdsourcing and Active Learning, 2020](https://arxiv.org/abs/2003.12139); [Third-party summary, n.d.](document_2.txt)).

The primary source provides four distinct figures that trace the data pipeline, whereas the third-party summary provides only the final figure. The primary source’s final figure is internally consistent with its intermediate figures: 1,952,079 + 1,733,905 = 3,685,984 ([Integrating Crowdsourcing and Active Learning, 2020](https://arxiv.org/abs/2003.12139)). The third-party summary’s figure cannot be verified against any intermediate steps because none are provided ([Third-party summary, n.d.](document_2.txt)).

### Source Reliability Assessment

The primary source is the original research paper, and it contains methodological details that allow for verification of the reported numbers ([Integrating Crowdsourcing and Active Learning, 2020](https://arxiv.org/abs/2003.12139)). The third-party summary is a secondary document that condenses the work without providing intermediate numbers or methodology ([Third-party summary, n.d.](document_2.txt)). Because the primary source is the authors’ own account and includes a step-by-step data collection narrative, it offers greater reliability for answering the query. The third-party summary’s provenance is unclear, and its final figure cannot be cross-checked against any reported intermediate counts.

### Possible Reasons for the Discrepancy

Several explanations could account for the difference between 3,685,984 and 2,368,590. First, the third-party summary may contain a transcription or calculation error. Second, the third-party summary may be based on a different version of the study or a different dataset altogether. Third, the third-party summary might have applied additional filtering criteria, such as stricter language detection, spam removal, or relevance thresholds, that reduced the final count. Fourth, the third-party summary might have de-duplicated across sources more aggressively, eliminating cross-source duplicates that the primary source did not remove. However, without explicit methodological details in the third-party summary, these remain speculative. The primary source’s step-by-step numbers make its final figure more trustworthy for this query ([Integrating Crowdsourcing and Active Learning, 2020](https://arxiv.org/abs/2003.12139); [Third-party summary, n.d.](document_2.txt)).

## Implications for the Research

The size of the final dataset has implications for the study’s methodology and findings. The paper’s title indicates the use of crowdsourcing and active learning for classification of work-life events ([Integrating Crowdsourcing and Active Learning, 2020](https://arxiv.org/abs/2003.12139)). A dataset of 3,685,984 unique tweets provides a large pool for these techniques, whereas a dataset of 2,368,590 would still be substantial but smaller by 1,317,394 tweets ([Third-party summary, n.d.](document_2.txt)). The discrepancy also highlights the importance of source verification in data-driven research. When secondary summaries disagree with primary sources, researchers should consult the original publication. In this case, the original publication provides a clear, auditable trail from collection to final dataset ([Integrating Crowdsourcing and Active Learning, 2020](https://arxiv.org/abs/2003.12139)).

## Conclusion

Based on the provided information, the final merged, de-duplicated tweets dataset is 3,685,984 unique tweets. This figure comes from the primary research paper, which reports a transparent data collection pipeline: 2,803,164 initial tweets from the Twitter search API, 1,952,079 after filtering duplicates and non-English tweets, and 1,733,905 relevant tweets from a historical random public tweets database. The sum of the two post-filter sets equals the final unique count of 3,685,984 ([Integrating Crowdsourcing and Active Learning, 2020](https://arxiv.org/abs/2003.12139)). The third-party summary’s figure of 2,368,590 unique tweets is secondary, unverifiable, and likely erroneous or based on different criteria ([Third-party summary, n.d.](document_2.txt)). Therefore, the answer to the query is 3,685,984 unique tweets. This report recommends relying on the primary source for the final dataset size.

## References

Integrating Crowdsourcing and Active Learning for Classification of Work-Life Events from Tweets. (2020). arXiv:2003.12139. https://arxiv.org/abs/2003.12139 (document_1.txt)

Third-party summary: work-life events tweet corpus. (n.d.). document_2.txt.