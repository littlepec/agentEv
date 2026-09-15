# How Big Is the ANTISCAM Dataset? Scale, Composition, and Source Reliability

## Introduction

The ANTISCAM dataset is a corpus of human–human anti-scam dialogs introduced to support research on non-collaborative dialog systems—conversational settings in which the user and the system do not share a common goal ([Li et al., 2020](document_1.txt)). Because non-collaborative tasks such as deception, persuasion, and negotiation require systems to handle both on-task and off-task (social) content, the authors designed ANTISCAM to serve as a benchmark in which a user defends personal information against an attacker impersonating an Amazon customer service agent ([Li et al., 2020](document_1.txt)). Determining "how big" the dataset is therefore requires attention to at least four distinct dimensions: the number of dialogs collected, the number of dialogs manually annotated, the sentence-level annotation volume, and the conversational characteristics (turns and utterances) of the corpus as a whole. Each of these is reported in the source material, and each carries a different implication for how the dataset can be used.

A complication arises immediately: the two provided sources disagree on the headline dialog count. The primary paper states the corpus contains 220 human–human dialogs, while a third-party research note states 320 ([Li et al., 2020](document_1.txt); [Third-party research note](document_2.txt)). This report resolves that discrepancy in favor of the primary source while transparently documenting the conflict.

## Direct Answer: 220 Human–Human Dialogs

The authoritative figure comes from the paper that created the dataset. In its dataset description, the paper states: "We collected 220 human-human dialogs" ([Li et al., 2020](document_1.txt)). The same figure is repeated verbatim in the paper's Appendix under the heading "Anti-Scam Collection Setting," which reports that the authors "collected 220 human-human dialogs" and immediately follows it with the average conversation length of 12.45 turns and average utterance length of 11.13 words ([Li et al., 2020](document_1.txt)). Because the number appears twice in the primary source—once in the main body and once in the appendix—and is internally consistent with the denominator used in the paper's task-outcome statistic, 220 is the most defensible count of the ANTISCAM corpus size.

Stated plainly: **the ANTISCAM dataset comprises 220 human–human dialogs**, collected as typed conversations on Amazon Mechanical Turk through a role-playing Amazon customer service scam scenario ([Li et al., 2020](document_1.txt)).

## Conversation-Level Dimensions

Raw dialog count alone understates the scale of the corpus, because each dialog contains multiple turns and each turn contains multiple sentences. The paper reports two complementary measures of conversational extent:

- **Average conversation length: 12.45 turns** ([Li et al., 2020](document_1.txt)).
- **Average utterance length: 11.13 words** ([Li et al., 2020](document_1.txt)).

Multiplying the average conversation length by the number of dialogs yields an approximate corpus size of 2,739 turns (220 × 12.45) and, applying the average utterance length of 11.13 words, roughly 30,485 words of dialog content before annotation overhead. It should be emphasized that these are derived estimates based on reported averages, not figures stated in the source; the paper reports only the averages themselves ([Li et al., 2020](document_1.txt)).

| Metric | Reported Value | Source |
|---|---|---|
| Human–human dialogs collected | 220 | ([Li et al., 2020](document_1.txt)) |
| Average conversation length | 12.45 turns | ([Li et al., 2020](document_1.txt)) |
| Average utterance length | 11.13 words | ([Li et al., 2020](document_1.txt)) |
| Approximate total turns (derived) | ≈ 2,739 | Derived from 220 × 12.45 |
| Approximate total words (derived) | ≈ 30,485 | Derived from turns × 11.13 |

*Table 1. Reported and derived size metrics for the ANTISCAM corpus. Derived values are estimates computed from reported averages and are not stated in the source.*

## Annotation Scale: The Manually Labeled Subset

The portion of ANTISCAM that carries gold-standard annotation is substantially smaller than the corpus as a whole. The paper states that two expert annotators with linguistic training annotated **3,044 sentences across 100 dialogs**, achieving an average weighted kappa value of 0.874 ([Li et al., 2020](document_1.txt)). This means that annotation coverage amounts to approximately 45.5% of the 220 collected dialogs (100 ÷ 220), and that the three thousand-plus annotated sentences constitute the supervised signal on which the paper's intent and semantic slot classifiers are trained and evaluated.

This distinction matters for anyone assessing dataset size for research purposes. A dataset of 220 dialogs is small by the standards of collaborative task-oriented corpora, but the fact that fewer than half of those dialogs were annotated means that the *annotated* ANTISCAM is smaller still—100 dialogs is a modest figure that makes transfer learning and pre-training on external data essentially necessary rather than optional ([Li et al., 2020](document_1.txt)).

| Annotation Metric | Reported Value |
|---|---|
| Dialogs manually annotated | 100 |
| Sentences annotated | 3,044 |
| Expert annotators | 2 (with linguistic training) |
| Inter-annotator agreement (average weighted kappa) | 0.874 |
| Annotated share of corpus (derived) | ≈ 45.5% |

*Table 2. Annotation statistics for the ANTISCAM dataset ([Li et al., 2020](document_1.txt)). The annotated share is derived from 100 annotated dialogs out of 220 collected.*

## Label Schema Size: Intents and Semantic Slots

The size of a dataset can also be expressed in terms of the label space it supports. ANTISCAM employs a hierarchical intent annotation scheme that separates on-task from off-task content. On-task intents for the anti-scam task are **elicitation, providing-information, and refusal** ([Li et al., 2020](document_1.txt)). Off-task intents are shared across non-collaborative tasks and comprise six general dialog acts (open question, yes–no question, positive answer, negative answer, responsive statement, non-responsive statement) plus six social intents (greeting, closing, apology, thanking, respond-to-thank, and hold) ([Li et al., 2020](document_1.txt)).

In addition, the authors "identify 13 main semantic slots in the anti-scam task, for example, credit card numbers" ([Li et al., 2020](document_1.txt)). The documented slot categories include order_update, payment, phone_num, name, card_num, account_detail, identity, address, card_info, card_cvs, card_date, and others ([Li et al., 2020](document_1.txt)). Annotators segmented each conversation turn into single sentences and annotated at the sentence rather than turn level, allowing multiple intents and multiple semantic slots to be assigned within a single utterance ([Li et al., 2020](document_1.txt)).

## Behavioral Outcome Measures as a Scale Indicator

The paper reports one further statistic that functions as an informal measure of dataset quality: **172 out of 220 users successfully identified their partner as an attacker** ([Li et al., 2020](document_1.txt)). This corresponds to approximately 78.2% of the user-side participants, a figure the authors interpret as evidence that "the attackers are well trained and not too easily identifiable" ([Li et al., 2020](document_1.txt)).

Notably, this single statistic is the point where the two sources diverge most visibly. The primary paper pairs "172" with a denominator of 220 ([Li et al., 2020](document_1.txt)), while the third-party note pairs the same numerator with a denominator of 320, which would imply a 53.75% identification rate ([Third-party research note](document_2.txt)). Internal consistency therefore favors the primary source: the numerator is identical across both documents, but only the primary source's denominator is repeated elsewhere in its own text.

## Evaluation and Training Scale

The dataset's downstream use also reveals its effective size. For experiments, the authors partitioned the data into 80% training, 10% validation, and 10% test splits ([Li et al., 2020](document_1.txt)). They first pre-trained the MISSA model on the PERSONA-CHAT dataset before fine-tuning on ANTISCAM, a strategy consistent with the small scale of the in-domain corpus ([Li et al., 2020](document_1.txt)).

Human evaluation was likewise of modest scale: 15 college-student volunteers were asked to pretend to be attackers and to interact with all models at least three times, yielding **225 dialogs in total**, with each model receiving a total of 45 human ratings ([Li et al., 2020](document_1.txt)). The paper also reports that the intent predictor achieved 84% accuracy and the semantic slot predictor 77% on ANTISCAM ([Li et al., 2020](document_1.txt)).

## Comparative Context: ANTISCAM Versus PERSUASIONFORGOOD

Placing ANTISCAM in context clarifies whether 220 dialogs is large or small for its research niche. The companion dataset used in the same paper, PERSUASIONFORGOOD, comprises **1,017 dialogs**, of which 300 are annotated with dialog acts; its average conversation length is 10.43 turns and its vocabulary size is 8,141 ([Li et al., 2020](document_1.txt)). By that comparison, ANTISCAM is roughly one-fifth the size of PERSUASIONFORGOOD in raw dialog count and one-third the size in annotated dialog count.

| Dataset | Total Dialogs | Annotated Dialogs | Avg. Conversation Length | Source |
|---|---|---|---|---|
| ANTISCAM | 220 | 100 | 12.45 turns | ([Li et al., 2020](document_1.txt)) |
| PERSUASIONFORGOOD | 1,017 | 300 | 10.43 turns | ([Li et al., 2020](document_1.txt)) |

*Table 3. Comparative scale of the two non-collaborative dialog corpora evaluated in the same study. Vocabulary size for PERSUASIONFORGOOD is reported as 8,141; no vocabulary size is reported for ANTISCAM ([Li et al., 2020](document_1.txt)).*

## Resolving the Source Discrepancy

The third-party note asserts that "the dataset contains 320 human-human dialogs," that annotation covers "100 dialogs and 3,044 sentences," and that "172 out of 320 users successfully identified their partner as an attacker" ([Third-party research note](document_2.txt)). Apart from the total dialog count and the associated denominator, every other figure in the note matches the primary paper exactly: 100 annotated dialogs, 3,044 sentences, two expert annotators with linguistic training, 12.45 turns, and 11.13 words ([Li et al., 2020](document_1.txt); [Third-party research note](document_2.txt)). This pattern—identical annotation statistics but a different corpus total—suggests that the discrepancy originates in the headline count rather than in the annotation or conversational metrics.

Applying the stated prioritization of trusted sources over less reliable ones, the primary paper authored by the dataset creators, reported as a peer-reviewed AAAI 2020 publication, must outweigh an unattributed third-party summary ([Li et al., 2020](document_1.txt)). The primary source is also internally corroborated, since "220" appears twice in its own text ([Li et al., 2020](document_1.txt)). The best-supported conclusion is therefore that ANTISCAM contains 220 human–human dialogs, with 320 representing an unverified secondary figure.

| Attribute | Primary Paper ([Li et al., 2020](document_1.txt)) | Third-Party Note ([Third-party research note](document_2.txt)) |
|---|---|---|
| Total dialogs | 220 | 320 |
| Users identifying attacker | 172 of 220 | 172 of 320 |
| Annotated dialogs | 100 | 100 |
| Annotated sentences | 3,044 | 3,044 |
| Avg. conversation length | 12.45 turns | 12.45 turns |
| Avg. utterance length | 11.13 words | 11.13 words |
| Annotator agreement | 0.874 | Not reported |

*Table 4. Side-by-side comparison of reported ANTISCAM statistics across the two sources. All figures other than the total dialog count agree.*

## Implications of the Dataset's Size

Three implications follow from the reported scale. First, ANTISCAM is a small dataset by any measure: 220 dialogs and 100 annotated dialogs place it well below the scale of multipurpose corpora such as MULTIWOZ or the Dialog State Tracking Challenge series discussed in the paper's related work ([Li et al., 2020](document_1.txt)). Second, its small annotated subset explains the paper's methodological choices—delexicalization of slot values during training, pre-training on PERSONA-CHAT, and reliance on a hierarchical annotation scheme whose off-task categories are task-independent and therefore reusable ([Li et al., 2020](document_1.txt)). Third, the authors explicitly frame ANTISCAM as a contribution to a sparse data landscape, stating that because non-collaborative tasks are "relatively new to the study of dialog systems, there are insufficiently many meaningful datasets for evaluation," and offering ANTISCAM as "a valuable example" ([Li et al., 2020](document_1.txt)).

## Conclusion

The most reliable answer to the question "how big is the ANTISCAM dataset?" is that it contains **220 human–human anti-scam dialogs**, of which **100 dialogs spanning 3,044 sentences** were manually annotated by two expert linguistically trained annotators with an average weighted kappa of 0.874 ([Li et al., 2020](document_1.txt)). Conversations average 12.45 turns and utterances average 11.13 words, and 172 of the 220 users successfully identified their partner as an attacker ([Li et al., 2020](document_1.txt)). A competing third-party note reports 320 dialogs and a denominator of 320 for the identification statistic, but given that every other figure it cites matches the primary paper exactly, and given the primary paper's internal repetition of the 220 figure, the 320 count should be treated as an unverified discrepancy rather than a correction ([Third-party research note](document_2.txt); [Li et al., 2020](document_1.txt)). For research purposes, ANTISCAM is best understood as a small, carefully annotated benchmark—modest in raw volume, but paired with a hierarchical intent and semantic slot schema (three on-task intents, twelve universal off-task intents, and thirteen semantic slots) designed to generalize across non-collaborative tasks ([Li et al., 2020](document_1.txt)).

## References

Li, Y., Qian, K., Shi, W., & Yu, Z. (2020). *End-to-end trainable non-collaborative dialog system* [document_1.txt]. University of California, Davis.

*Third-party research note: End-to-end trainable non-collaborative dialog system* [document_2.txt].