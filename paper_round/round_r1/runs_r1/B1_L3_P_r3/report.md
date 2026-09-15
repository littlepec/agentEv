# How Big Is the AntiScam Dataset? A Detailed Assessment of Corpus Size, Composition, and Annotation Scale

## Introduction

AntiScam is a human–human anti-scam dialog corpus introduced by Li, Qian, Shi, and Yu (2019) in the paper *End-to-End Trainable Non-Collaborative Dialog System*. The corpus was created "in order to learn human elicitation strategies" and was collected through a popular Amazon customer service scam role-playing scenario, in which workers were paired as attackers attempting to extract personal information and ordinary users attempting to protect it ([Li et al., 2019](#ref1)). Because the corpus is a non-collaborative dialog dataset — one in which users and systems do not share a common goal — the question of "how big" it is cannot be answered with a single number. Size can be measured in dialogs, turns, utterances, words, sentences, annotated sentences, and labeled intent and slot categories. This report examines each of those dimensions, using the primary paper as the authoritative source and flagging a discrepancy introduced by a secondary research note.

## The Primary Reported Corpus Size: 220 Human–Human Dialogs

The most direct answer to the question is found in the AntiScam dataset description itself. The paper states: "We posted a role-playing task on the Amazon Mechanical Turk platform and collected a typing conversation dataset named AntiScam. We collected 2 2 0 human-human dialogs" ([Li et al., 2019](#ref1)). The headline size of the AntiScam corpus is therefore **220 human–human dialogs**, collected on Amazon Mechanical Turk as typed (text) conversations rather than spoken ones ([Li et al., 2019](#ref1)).

Several secondary size metrics accompany that headline figure. The average conversation length is reported as 12.45 turns, and the average utterance length is reported as 11.13 words ([Li et al., 2019](#ref1)). In addition, only 172 out of 220 users successfully identified their partner as an attacker, a result the authors interpret as evidence that "the attackers are well trained and not too easily identifiable" ([Li et al., 2019](#ref1)). That corresponds to a detection rate of roughly 78.2%, leaving a substantial minority of users unable to recognize the scam. Table 1 consolidates the core size figures.

### Table 1. Headline size metrics for the AntiScam corpus

| Metric | Reported value |
|---|---|
| Total human–human dialogs | 220 ([Li et al., 2019](#ref1)) |
| Average conversation length | 12.45 turns ([Li et al., 2019](#ref1)) |
| Average utterance length | 11.13 words ([Li et al., 2019](#ref1)) |
| Users who correctly identified their partner as an attacker | 172 of 220 ([Li et al., 2019](#ref1)) |
| Manually annotated dialogs | 100 ([Li et al., 2019](#ref1)) |
| Manually annotated sentences | 3,044 ([Li et al., 2019](#ref1)) |
| Inter-annotator agreement | 0.874 averaged weighted kappa ([Li et al., 2019](#ref1)) |

## Annotation Scale and Density

Beyond raw dialog counts, the "size" of AntiScam is also defined by how much of it was annotated and how richly. The paper reports that "two expert annotators who have linguistic training" annotated 3,044 sentences across 100 dialogs, achieving a 0.874 averaged weighted kappa value ([Li et al., 2019](#ref1)). This means that the manually annotated portion — the subset used for supervised intent and slot modeling — covers 100 of the 220 dialogs, or approximately 45.5% of the corpus. The annotation was performed at the sentence level rather than the turn level: "we segment each conversation turn into single sentences and then annotate each sentence rather than turns" ([Li et al., 2019](#ref1)).

The paper also notes that the model can predict multiple intents and multiple semantic slots for each human utterance and system response, so the annotation density per sentence can exceed one label ([Li et al., 2019](#ref1)). Using the reported figures, several descriptive quantities can be derived (these are estimates derived from the paper's reported numbers, not figures stated directly in the paper):

- Annotation density: 3,044 ÷ 100 = **≈30.44 sentences per dialog** among annotated dialogs.
- Sentences per turn: ≈30.44 ÷ 12.45 = **≈2.44 sentences per turn**.
- Words per dialog: 12.45 turns × 11.13 words = **≈138.6 words per dialog**.
- Extrapolated corpus words: ≈138.6 × 220 = **≈30,500 words** across the full corpus (assuming comparable density).

These derived figures should be treated cautiously, since the paper reports averages for the full corpus and annotation counts for the subset, and it does not explicitly state that the subset is representative.

### Table 2. Annotation scheme scale

| Annotation component | Scale |
|---|---|
| On-task intents for AntiScam | 3 (elicitation, providing_information, refusal) ([Li et al., 2019](#ref1)) |
| Off-task general intents | 6 (open_question, yes_no_question, positive_answer, negative_answer, responsive_statement, nonresponsive_statement) ([Li et al., 2019](#ref1)) |
| Off-task social intents | 6 (greeting, closing, apology, thanking, respond_to_thank, hold) ([Li et al., 2019](#ref1)) |
| Total AntiScam intent categories | 15 ([Li et al., 2019](#ref1)) |
| Semantic slots for AntiScam | 13 ([Li et al., 2019](#ref1)) |

The 13 semantic slots identified for the anti-scam task are order_detail, order_update, payment, name, identity, address, phone_num, card_info, card_num, card_cvs, card_date, account_detail, and others ([Li et al., 2019](#ref1)). The intent scheme is hierarchical: on-task intents are task-specific, whereas off-task intents are universal across non-collaborative tasks, which the authors argue is the scheme's main advantage when starting a new task ([Li et al., 2019](#ref1)). For comparison, the annotation scheme applied to the PersuasionForGood dataset in the same paper defines nine on-task donation-related intents based on the original PersuasionForGood dialog act scheme ([Li et al., 2019](#ref1)).

## Corpus Composition: On-Task, Off-Task, and Social Content

The size of AntiScam is tightly linked to its composition. The paper states that "there is a vast amount of off-task content in the dataset, which confirms the necessity of a hierarchical on-task/off-task annotation scheme" ([Li et al., 2019](#ref1)). Quantitatively, the authors observe that attackers and users "both have a massive amount of social content (2 9 2 in total and 2 5 2 in total)," suggesting that it is important to include social intent sentences to maintain conversation ([Li et al., 2019](#ref1)). The reported sentence-level intent frequencies also indicate a substantial annotation volume distributed across roles and intents:

### Table 3. Reported intent frequencies by role

| Intent | Users | Attackers |
|---|---|---|
| refusal | 74 | 19 |
| open_question | 173 | 54 |
| yes_no_question | 165 | 117 |

Source: ([Li et al., 2019](#ref1)). The paper attributes the higher refusal count among users to their greater likelihood of withholding information after detecting an attacker ([Li et al., 2019](#ref1)).

A further size-related dimension is the human evaluation set built on top of the corpus. The authors tested models with 15 college-student volunteers who role-played as attackers, collecting 225 human–system dialogs in total, with each model receiving 45 human ratings ([Li et al., 2019](#ref1)). This evaluation set is separate from the 220-dialog AntiScam corpus but is part of the paper's overall data footprint. During evaluation, the best model (MISSA) maintained conversations of 14.9 turns on average versus 8.5 turns for the TransferTransfo baseline and achieved a higher task success score (1.294 versus 1.025) ([Li et al., 2019](#ref1)) — figures that illustrate the practical scale at which the dataset supports model training and assessment.

## Discrepancy in the Reported Corpus Size: 220 Versus 320

A secondary source included among the provided materials — a third-party research note — states that "the dataset contains 320 human-human dialogs" and reports that "172 out of 320 users successfully identified their partner as an attacker" ([Third-party research note, n.d.](#ref2)). This conflicts directly with the primary paper, which reports 220 dialogs and a ratio of 172 out of 220 ([Li et al., 2019](#ref1)).

Evaluating the two on the available evidence, the primary paper's figure of 220 is the more defensible one for several reasons. First, the primary paper is the source of the dataset and states the 220 figure explicitly in its AntiScam dataset description ([Li et al., 2019](#ref1)). Second, the 320 figure conflicts with the paper's own interpretation of its data: a 172-out-of-320 detection rate would imply roughly 46.3% of users failed to identify attackers, which sits awkwardly with the authors' characterization that attackers "are well trained and not too easily identifiable" while also implying a lower detection rate than the paper's stated ratio ([Li et al., 2019](#ref1)). Third, no other figure of 320 appears anywhere in the primary paper's dataset description; the nearest large numbers are 220 (corpus dialogs) and 225 (human-evaluation dialogs) ([Li et al., 2019](#ref1)). On balance, the secondary note's 320 figure appears inconsistent with the primary source, and the most accurate answer to the question "how big is AntiScam?" is **220 human–human dialogs**, with 100 of those dialogs and 3,044 sentences manually annotated ([Li et al., 2019](#ref1)).

### Table 4. Comparison of reported size claims

| Source | Total dialogs | Users who identified attacker | Annotated dialogs | Annotated sentences |
|---|---|---|---|---|
| Primary paper ([Li et al., 2019](#ref1)) | 220 | 172 of 220 | 100 | 3,044 |
| Third-party note ([Third-party research note, n.d.](#ref2)) | 320 | 172 of 320 | 100 | 3,044 |

Note that both sources agree on the annotation subset — 100 dialogs and 3,044 sentences annotated by two expert annotators with linguistic training, with average conversation length 12.45 turns and average utterance length 11.13 words ([Li et al., 2019](#ref1); [Third-party research note, n.d.](#ref2)). The disagreement is confined to the total corpus count.

## How AntiScam Compares with PersuasionForGood

Placing AntiScam in context helps calibrate its size. The same paper evaluates on both AntiScam and the existing PersuasionForGood dataset. PersuasionForGood "consists of 1,0 1 7 dialogs, where 3 0 0 dialogs are annotated with dialog acts," with an average conversation length of 10.43 and a vocabulary size of 8,141 ([Li et al., 2019](#ref1)). AntiScam is therefore substantially smaller in raw dialog count — 220 versus 1,017 — and has a smaller annotated subset in absolute terms (100 versus 300 annotated dialogs) ([Li et al., 2019](#ref1)). However, AntiScam has a slightly longer average conversation (12.45 turns versus 10.43) and a higher annotation density per annotated dialog by sentence count, reflecting its sentence-level annotation design ([Li et al., 2019](#ref1)). The authors position AntiScam as a benchmark that "is designed to interleave the on-task and off-task contents in the conversation" and that fills a gap, since non-collaborative tasks "are still relatively new to the study of dialog systems" and there are "insufficiently many meaningful datasets for evaluation" ([Li et al., 2019](#ref1)).

## Significance and Interpretation

The most concrete, defensible answer to the query is that AntiScam comprises **220 human–human anti-scam dialogs**, averaging 12.45 turns and 11.13 words per utterance, of which **100 dialogs and 3,044 sentences** were manually annotated by two linguistic experts with a 0.874 weighted kappa agreement ([Li et al., 2019](#ref1)). The corpus supports 15 intent categories (3 task-specific on-task intents plus 12 universal off-task intents) and 13 semantic slots ([Li et al., 2019](#ref1)). The code and data are released publicly at the project repository, which the authors cite as https://gitlab.com/ucdavisnlp/antiscam ([Li et al., 2019](#ref1)).

It is important to recognize that 220 dialogs is small by contemporary dialog-dataset standards — PersuasionForGood alone provides 1,017 dialogs ([Li et al., 2019](#ref1)) — and the authors acknowledge this limitation, stating that meaningful datasets for non-collaborative evaluation are scarce and that AntiScam is offered as "a valuable example" ([Li et al., 2019](#ref1)). The corpus's value therefore lies less in scale than in structure: it deliberately interleaves on-task and off-task content and supplies hierarchical, sentence-level supervision, enabling models such as MISSA (Multiple Intents and Semantic Slots Annotation Neural Network) to achieve an intent-prediction accuracy of 84% and a semantic slot-prediction accuracy of 77% on the dataset ([Li et al., 2019](#ref1)). For researchers planning to use the corpus, the practical sizing figures are 220 dialogs for unsupervised or weakly supervised use, and 100 dialogs / 3,044 sentences for the fully annotated portion, split into 80% training, 10% validation, and 10% testing as in the original experiments ([Li et al., 2019](#ref1)).

## Conclusion

Based on the primary source, the AntiScam dataset is **220 human–human anti-scam dialogs** collected via a role-playing Amazon customer service scam scenario on Amazon Mechanical Turk ([Li et al., 2019](#ref1)). Its average conversation length is 12.45 turns and its average utterance length is 11.13 words ([Li et al., 2019](#ref1)). The manually annotated subset consists of **100 dialogs and 3,044 sentences**, labeled by two expert annotators with a 0.874 averaged weighted kappa, using 15 intent categories and 13 semantic slots ([Li et al., 2019](#ref1)). A secondary research note reports 320 dialogs, but that figure conflicts with the primary paper's explicit statement and internal evidence, and should not be preferred over the source-of-record value of 220 ([Li et al., 2019](#ref1); [Third-party research note, n.d.](#ref2)). For most research purposes, the operative size of AntiScam is therefore 220 dialogs in total, with a 100-dialog, 3,044-sentence fully annotated core.

## References

<a id="ref1"></a>Li, Y., Qian, K., Shi, W., & Yu, Z. (2019). *End-to-end trainable non-collaborative dialog system* [Paper]. University of California, Davis. Code and data: https://gitlab.com/ucdavisnlp/antiscam

<a id="ref2"></a>Third-party research note: *End-to-end trainable non-collaborative dialog system* [Research note]. (n.d.).