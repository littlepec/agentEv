# The Size of the Final Merged, De-duplicated Tweet Dataset in the Work-Life Events Corpus

## Introduction

Determining the exact size of a research dataset is fundamental to assessing the scope, reproducibility, and validity of any empirical study. In the context of the work-life events tweet corpus, two documents provide information about the final merged, de-duplicated dataset: a primary source, which is an excerpt from the paper "Integrating Crowdsourcing and Active Learning for Classification of Work-Life Events from Tweets" (arXiv:2003.12139), and a third-party summary titled "work-life events tweet corpus" ([Integrating Crowdsourcing and Active Learning, 2020](https://arxiv.org/abs/2003.12139); [Third-party summary, n.d.](document_2.txt)). The primary source explicitly reports that after integrating tweets from two data sources, there were 3,685,984 unique tweets ([Integrating Crowdsourcing and Active Learning, 2020](https://arxiv.org/abs/2003.12139)). In contrast, the third-party summary states that the final corpus contains 2,368,590 unique tweets ([Third-party summary, n.d.](document_2.txt)). This report examines both figures, evaluates their reliability, and provides a definitive answer based on the primary source. The objective is to determine the size of the final dataset as reported by the original authors, while acknowledging the discrepancy with the third-party summary.

## Primary Source Evidence

### Data Collection Pipeline

The primary source describes a two-stage data collection process that culminates in the final merged, de-duplicated dataset. First, the authors collected 2,803,164 tweets using the Twitter search API ([Integrating Crowdsourcing and Active Learning, 2020](https://arxiv.org/abs/2003.12139)). After filtering out duplicates and non-English tweets, 1,952,079 tweets remained ([Integrating Crowdsourcing and Active Learning, 2020](https://arxiv.org/abs/2003.12139)). Second, using the same keywords, the authors identified 1,733,905 relevant tweets from a database of historical random public tweets ([Integrating Crowdsourcing and Active Learning, 2020](https://arxiv.org/abs/2003.12139)). After integrating the tweets from the two data sources, the paper states that there were 3,685,984 unique tweets ([Integrating Crowdsourcing and Active Learning, 2020](https://arxiv.org/abs/2003.12139)). This number is the final merged, de-duplicated dataset according to the primary source.

### Arithmetic Consistency

A notable feature of the primary source's figures is that the sum of the two filtered components exactly equals the reported final total: 1,952,079 + 1,733,905 = 3,685,984 ([Integrating Crowdsourcing and Active Learning, 2020](https://arxiv.org/abs/2003.12139)). This arithmetic identity suggests that after filtering duplicates within each source, there were no overlapping tweets between the two sources, or that any cross-source duplicates were already removed in the per-source filtering steps. The paper does not mention any additional de-duplication step between the two sources, nor does it report a reduction in the total after integration ([Integrating Crowdsourcing and Active Learning, 2020](https://arxiv.org/abs/2003.12139)). Therefore, the final dataset size is the sum of the two cleaned subsets. This internal consistency strengthens the credibility of the reported figure.

### Section Context

The information appears under "Results :: Data Collection" in the primary source ([Integrating Crowdsourcing and Active Learning, 2020](https://arxiv.org/abs/2003.12139)). This section is part of the paper's results, indicating that the data collection process is a reported outcome of the study. The explicit statement "After integrating the tweets from the two data sources, there were 3,685,984 unique tweets" is the most direct answer to the query ([Integrating Crowdsourcing and Active Learning, 2020](https://arxiv.org/abs/2003.12139)). The placement of this information in the results section, rather than in a preliminary methods section, further underscores its importance as a key finding of the data collection effort.

### Detailed Breakdown of the Data Collection Steps

Table 1 presents a step-by-step breakdown of the data collection numbers as reported in the primary source.

| Step | Source | Number of tweets |
|------|--------|------------------|
| Initial collection | Twitter search API | 2,803,164 |
| After filtering duplicates and non-English | Twitter search API | 1,952,079 |
| Identification from historical database | Historical random public tweets | 1,733,905 |
| Final integrated dataset | Both sources | 3,685,984 |

Table 1: Data collection steps and tweet counts from the primary source ([Integrating Crowdsourcing and Active Learning, 2020](https://arxiv.org/abs/2003.12139)).

## Third-Party Summary Evidence

### Reported Figure

The third-party summary states that the work builds a work-life-events tweet corpus by combining two sources: the Twitter search API and a historical random-tweet database ([Third-party summary, n.d.](document_2.txt)). After merging both sources and removing duplicates, the final corpus contains 2,368,590 unique tweets, which is then used for crowdsourcing and active-learning classification ([Third-party summary, n.d.](document_2.txt)). This figure is substantially lower than the 3,685,984 reported by the primary source.

### Discrepancy Analysis

The difference between the two reported figures is 3,685,984 − 2,368,590 = 1,317,394 tweets ([Integrating Crowdsourcing and Active Learning, 2020](https://arxiv.org/abs/2003.12139); [Third-party summary, n.d.](document_2.txt)). There are several possible explanations for this discrepancy, though none are specified in the provided information. The third-party summary may have applied additional de-duplication criteria, such as removing near-duplicates or retweets, or it may have used a different subset of the data for the final corpus. Alternatively, the summary could contain an error, or it might refer to a different stage of the pipeline, such as after further filtering for annotation. However, the third-party summary does not provide details about its data collection steps beyond the final count ([Third-party summary, n.d.](document_2.txt)). Without such details, it is impossible to verify the basis for the 2,368,590 figure.

### Lack of Methodological Transparency

The third-party summary lacks the methodological transparency of the primary source. It does not report intermediate counts, filtering criteria, or the specific keywords used ([Third-party summary, n.d.](document_2.txt)). In contrast, the primary source provides a clear sequence of steps, including the initial collection size, the number of tweets removed due to duplicates and language filtering, and the number of relevant tweets from the historical database ([Integrating Crowdsourcing and Active Learning, 2020](https://arxiv.org/abs/2003.12139)). This transparency allows for verification and replication, whereas the third-party summary's brevity precludes such scrutiny.

## Comparative Analysis

To evaluate the two sources, a comparison of their reported dataset sizes and data collection details is presented in Table 2.

### Table 2: Comparison of Reported Final Dataset Sizes

| Source | Reported final dataset size | Data collection details | Source type | Reliability assessment |
|--------|----------------------------|------------------------|-------------|------------------------|
| document_1.txt (primary paper) | 3,685,984 unique tweets | 2,803,164 collected via Twitter search API; 1,952,079 after filtering duplicates and non-English; 1,733,905 from historical random public tweets; integrated total | Primary source: original research paper | High reliability; provides step-by-step figures and arithmetic consistency |
| document_2.txt (third-party summary) | 2,368,590 unique tweets | Merged two sources and removed duplicates; final corpus used for crowdsourcing and active learning | Third-party summary | Lower reliability; lacks detailed steps and does not explain discrepancy |

Table 2: Comparison of the primary source and third-party summary ([Integrating Crowdsourcing and Active Learning, 2020](https://arxiv.org/abs/2003.12139); [Third-party summary, n.d.](document_2.txt)).

The primary source is a research paper, which is a more authoritative and reliable source than a third-party summary ([Integrating Crowdsourcing and Active Learning, 2020](https://arxiv.org/abs/2003.12139); [Third-party summary, n.d.](document_2.txt)). The primary source provides specific numbers at each stage of the data collection process, and its final total is arithmetically consistent with its components ([Integrating Crowdsourcing and Active Learning, 2020](https://arxiv.org/abs/2003.12139)). The third-party summary, by contrast, offers only a final count without intermediate steps or an explanation for the lower number ([Third-party summary, n.d.](document_2.txt)). Therefore, the primary source's figure should be preferred when answering the query.

## Why the Primary Source is Preferred

The preference for the primary source is based on several factors. First, it is the original research paper, which means it is the authoritative account of the data collection process ([Integrating Crowdsourcing and Active Learning, 2020](https://arxiv.org/abs/2003.12139)). Second, it provides a complete audit trail from initial collection to final dataset, allowing for verification of the arithmetic ([Integrating Crowdsourcing and Active Learning, 2020](https://arxiv.org/abs/2003.12139)). Third, the reported figures are internally consistent, with the sum of the two filtered components equaling the final total ([Integrating Crowdsourcing and Active Learning, 2020](https://arxiv.org/abs/2003.12139)). Fourth, the paper is a preprint on arXiv, which, while not peer-reviewed in the traditional sense, is a widely used and citable source in computer science and related fields. In contrast, the third-party summary is derivative, lacks methodological detail, and provides no basis for its lower figure ([Third-party summary, n.d.](document_2.txt)). When sources conflict, the one with greater transparency and internal consistency should be trusted.

## Implications of Dataset Size

The size of the final dataset has implications for the research methodology described in the paper. The paper focuses on integrating crowdsourcing and active learning for classification of work-life events from tweets ([Integrating Crowdsourcing and Active Learning, 2020](https://arxiv.org/abs/2003.12139)). A larger dataset of 3,685,984 unique tweets provides a substantial pool from which to sample for crowdsourced annotation and active learning ([Integrating Crowdsourcing and Active Learning, 2020](https://arxiv.org/abs/2003.12139)). Active learning typically requires an initial labeled set and then iteratively selects the most informative instances for annotation. A larger unlabeled pool can improve the diversity of instances selected, potentially leading to better classification performance. However, a larger dataset also increases the computational and annotation burden. The third-party summary's smaller figure of 2,368,590 would imply a more manageable but less comprehensive corpus ([Third-party summary, n.d.](document_2.txt)). The discrepancy between the two figures could affect the reproducibility of the study, as researchers attempting to replicate the work would need to know the exact final dataset size. If the third-party summary's figure were correct, the dataset would be approximately 35.7% smaller than the primary source's figure, which could materially affect the results of active learning experiments.

## Conclusion

Based on the provided information, the final merged, de-duplicated tweet dataset is 3,685,984 unique tweets, as reported in the primary source ([Integrating Crowdsourcing and Active Learning, 2020](https://arxiv.org/abs/2003.12139)). This figure is derived from the integration of 1,952,079 tweets from the Twitter search API (after filtering duplicates and non-English tweets) and 1,733,905 tweets from a historical random public tweets database ([Integrating Crowdsourcing and Active Learning, 2020](https://arxiv.org/abs/2003.12139)). The arithmetic sum of these two components exactly equals the reported total, indicating that no further cross-source de-duplication reduced the count ([Integrating Crowdsourcing and Active Learning, 2020](https://arxiv.org/abs/2003.12139)). A third-party summary reports a different figure of 2,368,590 unique tweets, but this source is less reliable and does not provide sufficient detail to substantiate its number ([Third-party summary, n.d.](document_2.txt)). Consequently, the answer to the query is 3,685,984 unique tweets. This report recommends that any subsequent analysis or replication of the work-life events corpus use the primary source's figure as the authoritative dataset size.

## References

Integrating Crowdsourcing and Active Learning for Classification of Work-Life Events from Tweets. (2020). arXiv. https://arxiv.org/abs/2003.12139

Third-party summary: work-life events tweet corpus. (n.d.). document_2.txt.