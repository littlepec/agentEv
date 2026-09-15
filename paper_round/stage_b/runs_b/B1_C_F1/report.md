# Size and Composition of the AntiScam Dataset

## Introduction
The AntiScam dataset is a human-human anti-scam dialog corpus collected via a role-playing Amazon customer service scam scenario on Amazon Mechanical Turk ([document_2.txt](document_2.txt)). When asking how big the dataset is, the answer depends on the unit of measurement. The reported figures describe the dataset in terms of total dialogs, annotated dialogs, annotated sentences, average conversation length, average utterance length, and user identification outcomes. This report provides a detailed, source-based assessment of the dataset's size using all relevant information from document_2.txt. All reported figures are drawn directly from that source, and any calculated values are explicitly identified as derived.

## Primary Size: Total Number of Dialogs
The most direct answer to the size question is that AntiScam comprises 220 human-human dialogs ([document_2.txt](document_2.txt)). This figure represents the full corpus and is the largest unit count reported for the dataset. The corpus was collected through a role-playing Amazon customer service scam scenario on Amazon Mechanical Turk ([document_2.txt](document_2.txt)). The 220 dialogs therefore form the primary measure of the dataset's scale. In dialog research, the number of dialogs is often the headline size metric because it indicates the number of independent conversational episodes available for training, evaluation, or analysis.

The total dataset comprises 220 human-human dialogs ([document_2.txt](document_2.txt)). This number is consistent across the source's descriptions. It is the foundational quantity from which other size-related figures are derived. The source also reports that the average conversation length is 12.45 turns, and this average describes the full AntiScam corpus ([document_2.txt](document_2.txt)). Consequently, the 220 dialogs collectively contain an estimated 2,739 turns (derived from 220 × 12.45). This derived total provides a sense of the conversational volume beyond the raw dialog count.

## Annotated Subset Size
Of the 220 total dialogs, a subset of 100 dialogs was manually annotated ([document_2.txt](document_2.txt)). This annotated subset represents 45.45% of the full corpus (derived from 100 / 220). The annotation was performed by two expert annotators who have linguistic training ([document_2.txt](document_2.txt)). The manually annotated subset comprises 100 dialogs and 3,044 sentences ([document_2.txt](document_2.txt)). The existence of this subset means that AntiScam has two relevant sizes: the full corpus of 220 dialogs and the annotated core of 100 dialogs.

The 100 annotated dialogs are a substantial portion of the full dataset but do not cover the entire corpus. The remaining 120 dialogs, representing 54.55% of the total, are not part of the manually annotated subset ([document_2.txt](document_2.txt)). This distinction is important because annotation statistics apply only to the 100-dialog subset, while the average conversation and utterance lengths apply to the full 220-dialog corpus ([document_2.txt](document_2.txt)). The annotated subset therefore provides detailed sentence-level information for less than half of the total dialogs.

### Sentence-Level Size
The 3,044 sentences are contained within the 100 annotated dialogs ([document_2.txt](document_2.txt)). On average, this amounts to approximately 30.44 sentences per annotated dialog (derived from 3,044 / 100). The source does not report the total number of sentences in the full 220-dialog corpus. If the annotated subset is representative, one could estimate that the full corpus might contain approximately 6,697 sentences (derived from 220 × 30.44). However, this is an extrapolation and not a reported figure ([document_2.txt](document_2.txt)). The reported sentence count of 3,044 is therefore the only definitive sentence-level size measurement available.

## Conversational and Utterance Length
The paper reports that the average conversation length is 12.45 turns ([document_2.txt](document_2.txt)). This average describes the full AntiScam corpus ([document_2.txt](document_2.txt)). Similarly, the average utterance length is 11.13 words, also describing the full corpus ([document_2.txt](document_2.txt)). These two averages provide a sense of the granularity of the dialogs. A conversation of 12.45 turns suggests a relatively short exchange, and an utterance length of 11.13 words suggests concise individual contributions.

Using the average conversation length, the total number of turns in the full corpus can be estimated at 2,739 turns (derived from 220 × 12.45). For the 100 annotated dialogs, the estimated number of turns is 1,245 (derived from 100 × 12.45). These estimates assume that the average applies uniformly across all dialogs. The source does not provide a distribution or variance for conversation length, so the actual number of turns per dialog may vary.

The total word count of the corpus cannot be precisely determined from the provided information. The average utterance length is 11.13 words, but the number of utterances per turn is not specified ([document_2.txt](document_2.txt)). If one assumes that each turn contains exactly one utterance, then the full corpus would contain approximately 30,485 words (derived from 2,739 × 11.13), and the annotated subset would contain approximately 13,857 words (derived from 1,245 × 11.13). Because the relationship between turns and utterances is not defined in the source, these word-count estimates should be treated as conditional rather than definitive ([document_2.txt](document_2.txt)).

## User Identification Outcome
The paper reports that 172 out of 220 users successfully identified their partner as an attacker ([document_2.txt](document_2.txt)). This outcome is part of the AntiScam dataset description ([document_2.txt](document_2.txt)). The success rate is therefore 78.18% (derived from 172 / 220). Conversely, 48 users did not successfully identify their partner as an attacker, representing 21.82% of the user population (derived from 48 / 220). This metric does not directly measure dataset size, but it describes the composition and performance context of the 220 dialogs. It indicates that the majority of participants detected the scam, while a substantial minority did not.

## Summary of Reported and Derived Metrics
The following table consolidates the reported and derived figures for AntiScam.

| Metric | Value | Type | Scope |
|---|---|---|---|
| Total dialogs | 220 | Reported | Full corpus |
| Annotated dialogs | 100 | Reported | Subset |
| Annotated sentences | 3,044 | Reported | Subset |
| Average conversation length | 12.45 turns | Reported | Full corpus |
| Average utterance length | 11.13 words | Reported | Full corpus |
| Users | 220 | Reported | Full corpus |
| Users identifying attacker | 172 | Reported | Full corpus |
| Users not identifying attacker | 48 | Derived | Full corpus |
| User success rate | 78.18% | Derived | Full corpus |
| Annotated dialogs as percentage of total | 45.45% | Derived | Subset vs full |
| Average sentences per annotated dialog | 30.44 | Derived | Subset |
| Estimated total turns (full corpus) | 2,739 | Derived | Full corpus |
| Estimated total turns (annotated subset) | 1,245 | Derived | Subset |
| Estimated total sentences (full corpus, if representative) | ~6,697 | Derived | Full corpus |
| Estimated total words (if one utterance per turn) | ~30,485 | Derived | Full corpus |

Note: Derived values are calculated from the reported figures in document_2.txt and are not independently reported in the source ([document_2.txt](document_2.txt)).

## Full Corpus Versus Annotated Subset
The full corpus has 220 dialogs, while the annotated subset has 100 dialogs ([document_2.txt](document_2.txt)). This means 120 dialogs, or 54.55% of the total, are not part of the manually annotated subset. The annotated subset contains 3,044 sentences ([document_2.txt](document_2.txt)). If annotation was performed at the sentence level, then these 3,044 sentences represent the sentence-level units within the 100 annotated dialogs. The full corpus may contain additional sentences that are unannotated. The average conversation length and average utterance length are reported for the full corpus, so they apply to all 220 dialogs, not only the annotated 100 ([document_2.txt](document_2.txt)).

This distinction matters for interpreting the dataset's size. A researcher interested in sentence-level linguistic annotation would work with 3,044 sentences across 100 dialogs. A researcher interested in the overall conversational corpus would work with 220 dialogs and an estimated 2,739 turns. The two scopes are related but not identical.

## Interpreting the Size of AntiScam
In absolute terms, 220 human-human dialogs is a moderate-sized dialog corpus. The manually annotated subset of 100 dialogs and 3,044 sentences is smaller but still substantial for detailed linguistic annotation. The average conversation length of 12.45 turns suggests that each dialog is relatively short, containing approximately 12 to 13 speaker turns. At an average utterance length of 11.13 words, individual utterances are also relatively concise ([document_2.txt](document_2.txt)). This combination indicates that AntiScam is composed of short, focused exchanges rather than long, multi-turn conversations.

The fact that 172 out of 220 users (78.18%) successfully identified their partner as an attacker suggests that the scam scenario was detectable by a majority of participants ([document_2.txt](document_2.txt)). This outcome provides context for the dataset's composition: the dialogs include both successful and unsuccessful identification cases, which may be useful for analyzing deception detection and scam recognition. However, the source does not provide a breakdown of how the 172 successful and 48 unsuccessful cases are distributed across the 100 annotated dialogs.

The dataset's size can also be considered in terms of its human-human nature. The corpus consists of 220 human-human dialogs ([document_2.txt](document_2.txt)). This means the interactions are between two human participants rather than between a human and a system. The role-playing Amazon customer service scam scenario on Amazon Mechanical Turk provides the collection context ([document_2.txt](document_2.txt)). The size of 220 dialogs is therefore tied to the number of successfully completed human-human interactions in that scenario.

## Reliability and Source Assessment
The information used in this report comes from a single source, document_2.txt ([document_2.txt](document_2.txt)). This source provides specific numerical figures for the AntiScam dataset, including 220 dialogs, 100 annotated dialogs, 3,044 sentences, an average conversation length of 12.45 turns, an average utterance length of 11.13 words, and 172 out of 220 users identifying their partner as an attacker. The source is internally consistent and directly addresses the size and annotation statistics of the dataset.

However, the source does not provide standard deviations, ranges, or confidence intervals for the averages. It also does not specify the total number of utterances, the total number of words, or the total number of sentences in the full corpus. Consequently, any full-corpus sentence or word estimates are extrapolations. The absence of these details limits the precision with which the absolute size of the dataset can be described beyond the reported dialog and annotated sentence counts. The source also does not indicate whether the 100 annotated dialogs were selected randomly or according to specific criteria, which affects how confidently one can generalize from the annotated subset to the full corpus.

## Conclusion
The AntiScam dataset is fundamentally a corpus of 220 human-human dialogs collected via a role-playing Amazon customer service scam scenario on Amazon Mechanical Turk ([document_2.txt](document_2.txt)). Its manually annotated subset comprises 100 dialogs and 3,044 sentences, annotated by two expert annotators with linguistic training ([document_2.txt](document_2.txt)). The average conversation length is 12.45 turns, and the average utterance length is 11.13 words ([document_2.txt](document_2.txt)). In terms of user outcomes, 172 out of 220 users successfully identified their partner as an attacker ([document_2.txt](document_2.txt)). Therefore, the size of AntiScam is best described as 220 dialogs in total, with a 100-dialog annotated core containing 3,044 sentences. Any broader word- or sentence-level totals for the full corpus remain estimates rather than reported facts. The dataset is moderate in scale, with a focused annotated subset that supports detailed linguistic analysis.

## References

document_2.txt. (n.d.). AntiScam dataset description. Retrieved from document_2.txt.