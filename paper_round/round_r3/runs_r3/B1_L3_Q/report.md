# Assessing the Size, Structure, and Annotation Scale of the AntiScam Dataset

## Introduction

The AntiScam dataset is a non-collaborative dialog corpus introduced to support research on anti-scam conversational systems, specifically systems designed to waste attackers' time and elicit their private information for social good ([Li et al., 2019](https://gitlab.com/ucdavisnlp/antiscam)). The question of how "big" the dataset is cannot be answered by a single number alone, because the corpus has multiple dimensions of scale: the total number of dialogs collected, the number of dialogs that were manually annotated, the number of sentences and turns these contain, the average length of each conversation, and the breadth of the annotation scheme applied to those dialogs ([Third-party research note](https://gitlab.com/ucdavisnlp/antiscam)). This report synthesizes the available evidence to provide a comprehensive answer, including primary size figures, derived estimates, annotation coverage, and a discussion of source reliability. The central finding is that AntiScam comprises **220 human-human dialogs**, of which **100 dialogs containing 3,044 sentences** were manually annotated, with an average conversation length of **12.45 turns** and an average utterance length of **11.13 words** ([Li et al., 2019](https://gitlab.com/ucdavisnlp/antiscam); [Third-party research note](https://gitlab.com/ucdavisnlp/antiscam)).

## Core Size Metrics

### Total Dialog Count

The most direct measure of the AntiScam dataset's size is the number of dialogs it contains. The paper states unambiguously that the authors "collected 2 2 0 human-human dialogs" through a role-playing task posted on Amazon Mechanical Turk ([Li et al., 2019](https://gitlab.com/ucdavisnlp/antiscam)). This figure of **220 dialogs** constitutes the full corpus size. The third-party research note corroborates this number, reporting that "the dataset contains 220 human-machine dialogs" and that "its size is 220 human-machine dialogs" ([Third-party research note](https://gitlab.com/ucdavisnlp/antiscam)). However, the note's characterization of these as "human-machine" dialogs appears to conflict with the primary source, which describes a setting in which "two workers" were randomly paired—one as an attacker and one as an everyday user—making the interactions human-human rather than human-machine ([Li et al., 2019](https://gitlab.com/ucdavisnlp/antiscam)). This discrepancy is addressed further in the source reliability section below.

### Turn and Utterance Dimensions

Beyond the raw dialog count, the dataset's size is characterized by conversation length and utterance length. The average conversation length is reported as **12.45 turns**, and the average utterance length is **11.13 words** ([Li et al., 2019](https://gitlab.com/ucdavisnlp/antiscam); [Third-party research note](https://gitlab.com/ucdavisnlp/antiscam)). These averages describe the full AntiScam corpus, not merely the annotated subset ([Third-party research note](https://gitlab.com/ucdavisnlp/antiscam)). These two figures allow for a derived estimate of the corpus's overall volume in turns and words, which is useful for understanding the dataset's practical scale for model training.

### Derived Corpus Volume

Using the reported averages, one can estimate the total volume of the full 220-dialog corpus. Multiplying 220 dialogs by 12.45 turns per dialog yields approximately **2,739 turns** across the corpus. Multiplying those turns by 11.13 words per utterance yields approximately **30,484 words** in total. These are approximations, because the averages may not be uniformly distributed across all dialogs, and because a "turn" may contain more than one utterance or sentence ([Li et al., 2019](https://gitlab.com/ucdavisnlp/antiscam)). Nevertheless, they provide a concrete sense of scale: AntiScam is a small-to-medium-sized dialog corpus by contemporary standards, comparable to or smaller than many task-oriented dialog datasets.

**Table 1. Core Size Metrics of the AntiScam Dataset**

| Metric | Value | Source |
|---|---|---|
| Total dialogs collected | 220 human-human dialogs | ([Li et al., 2019](https://gitlab.com/ucdavisnlp/antiscam)) |
| Average conversation length | 12.45 turns | ([Li et al., 2019](https://gitlab.com/ucdavisnlp/antiscam)) |
| Average utterance length | 11.13 words | ([Li et al., 2019](https://gitlab.com/ucdavisnlp/antiscam)) |
| Manually annotated dialogs | 100 dialogs | ([Li et al., 2019](https://gitlab.com/ucdavisnlp/antiscam)) |
| Manually annotated sentences | 3,044 sentences | ([Li et al., 2019](https://gitlab.com/ucdavisnlp/antiscam)) |
| Inter-annotator agreement (weighted kappa) | 0.874 | ([Li et al., 2019](https://gitlab.com/ucdavisnlp/antiscam)) |

**Table 2. Derived Volume Estimates for the Full Corpus**

| Derived Metric | Calculation | Approximate Value |
|---|---|---|
| Total turns | 220 dialogs × 12.45 turns | ~2,739 turns |
| Total words | ~2,739 turns × 11.13 words | ~30,484 words |
| Extrapolated sentences | 3,044 sentences × (220/100) | ~6,697 sentences |

The extrapolated sentence figure in Table 2 assumes that the 100 annotated dialogs are representative of the full 220 dialogs in terms of sentences per dialog. This assumption is plausible but unverified in the source material, and the figure should be treated as an indicative estimate only ([Li et al., 2019](https://gitlab.com/ucdavisnlp/antiscam)).

## Annotation Coverage and Scope

### Annotated Subset

The manually annotated portion of AntiScam is smaller than the full corpus. Two expert annotators with linguistic training annotated **3,044 sentences in 100 dialogs**, achieving a **0.874 averaged weighted kappa value** ([Li et al., 2019](https://gitlab.com/ucdavisnlp/antiscam)). This means that less than half of the collected dialogs (100 out of 220, or approximately 45.5%) received manual annotation. The third-party research note confirms these annotation statistics, stating that "a subset of 100 dialogs containing 3,044 sentences was manually annotated" and that "two expert annotators who have linguistic training performed this annotation" ([Third-party research note](https://gitlab.com/ucdavisnlp/antiscam)). The annotation subset therefore contains an average of approximately **30.44 sentences per dialog**, which is higher than the number of turns (12.45) because each turn may be segmented into multiple sentences ([Li et al., 2019](https://gitlab.com/ucdavisnlp/antiscam)).

### Intent Annotation Dimensions

The annotation scheme applied to AntiScam is hierarchical, separating on-task and off-task intents. For the AntiScam task specifically, three on-task intents were defined: **elicitation**, **providing_information**, and **refusal** ([Li et al., 2019](https://gitlab.com/ucdavisnlp/antiscam)). The off-task intents are shared across non-collaborative tasks and comprise six general intents—**open_question**, **yes_no_question**, **positive_answer**, **negative_answer**, **responsive_statement**, and **nonresponsive_statement**—plus six social intents: **greeting**, **closing**, **apology**, **thanking**, **respond_to_thank**, and **hold** ([Li et al., 2019](https://gitlab.com/ucdavisnlp/antiscam)). In total, therefore, the annotation scheme encompasses **three on-task intents and twelve off-task intents**, giving fifteen intent categories, though not all apply equally to both speakers.

### Semantic Slot Annotation

In addition to intents, the dataset includes a semantic slot annotation scheme. The authors "identify l 3 main semantic slots in the anti-scam task," including slots such as **order_detail**, **order_update**, **payment**, **name**, **identity**, **address**, **phone_num**, **card_info**, **card_num**, **card_cvs**, **card_date**, **account_detail**, and **others** ([Li et al., 2019](https://gitlab.com/ucdavisnlp/antiscam)). This means each annotated sentence can carry both an intent label and one or more semantic slot labels, multiplying the effective annotation density beyond the raw sentence count.

**Table 3. Annotation Dimensions of the AntiScam Dataset**

| Dimension | Count | Examples |
|---|---|---|
| On-task intents | 3 | elicitation, providing_information, refusal |
| Off-task general intents | 6 | open_question, yes_no_question, positive_answer, negative_answer, responsive_statement, nonresponsive_statement |
| Off-task social intents | 6 | greeting, closing, apology, thanking, respond_to_thank, hold |
| Semantic slots | 13 | name, address, phone_num, card_num, card_cvs, card_date, payment, order_detail, order_update, identity, card_info, account_detail, others |

### Inter-Annotator Reliability

The reported averaged weighted kappa of **0.874** indicates strong agreement between the two expert annotators ([Li et al., 2019](https://gitlab.com/ucdavisnlp/antiscam)). This is a meaningful quality indicator: it suggests that the annotation guidelines for intents and semantic slots were sufficiently well defined to be applied consistently across 3,044 sentences. For a dataset of this size, such reliability supports the corpus's utility as a benchmark for non-collaborative dialog research.

## Compositional Characteristics

### On-Task Versus Off-Task Content

The AntiScam dataset is deliberately designed to interleave on-task and off-task content, a design choice intended to reflect the realities of non-collaborative dialogs in which rapport-building and social exchange are necessary to advance task goals ([Li et al., 2019](https://gitlab.com/ucdavisnlp/antiscam)). The authors note that "there is a vast amount of off-task content in the dataset," which they argue confirms the necessity of a hierarchical on-task/off-task annotation scheme ([Li et al., 2019](https://gitlab.com/ucdavisnlp/antiscam)). Quantitatively, attackers and users both contributed substantial social content: **292 social-content sentences in total for one group and 252 in total for the other** ([Li et al., 2019](https://gitlab.com/ucdavisnlp/antiscam)). This indicates that roughly half of the annotated social behavior comes from each side of the conversation, underscoring the dataset's balanced representation of both participants.

### Attacker Versus User Contributions

The dataset reveals distinct intent distributions between attackers and users. Compared to attackers, users produced more **refusal** instances (**74 vs. 19**), because users are more likely to refuse to provide requested information once they have detected the attacker ([Li et al., 2019](https://gitlab.com/ucdavisnlp/antiscam)). Users also asked more **open_questions** (**173 vs. 54**) and more **yes_no_questions** (**165 vs. 117**) as part of off-task content ([Li et al., 2019](https://gitlab.com/ucdavisnlp/antiscam)). These asymmetries are important for understanding the dataset's internal balance: it is not a homogeneous corpus but one with systematically different speaker behaviors, which is precisely what makes it valuable for training non-collaborative dialog systems.

### Attacker Detection Outcomes

A notable dataset-level statistic is that "only 1 7 2 out of 2 2 0 users successfully identified their partner as an attacker," suggesting that the attackers were well trained and not easily identifiable ([Li et al., 2019](https://gitlab.com/ucdavisnlp/antiscam)). This means that **172 of 220 users (approximately 78.2%)** correctly detected the scam, while 48 users (approximately 21.8%) did not. This outcome is part of the AntiScam dataset description and provides context on the difficulty of the anti-scam task ([Third-party research note](https://gitlab.com/ucdavisnlp/antiscam)).

## Comparative Scale

### AntiScam Versus PersuasionForGood

To contextualize the size of AntiScam, it is useful to compare it with the PersuasionForGood dataset, the other non-collaborative corpus used in the study. PersuasionForGood consists of **1,017 dialogs**, of which **300 dialogs are annotated with dialog acts**, with an average conversation length of **10.43 turns** and a vocabulary size of **8,141** ([Li et al., 2019](https://gitlab.com/ucdavisnlp/antiscam)). AntiScam is therefore smaller in total dialog count (220 vs. 1,017) but has a higher average conversation length (12.45 vs. 10.43 turns) and a higher proportion of manually annotated dialogs relative to its size (100/220 ≈ 45.5% vs. 300/1,017 ≈ 29.5%).

**Table 4. Comparative Scale of AntiScam and PersuasionForGood**

| Metric | AntiScam | PersuasionForGood |
|---|---|---|
| Total dialogs | 220 | 1,017 |
| Annotated dialogs | 100 | 300 |
| Annotated sentences | 3,044 | Not reported |
| Average conversation length | 12.45 turns | 10.43 turns |
| Average utterance length | 11.13 words | Not reported |
| Vocabulary size | Not reported | 8,141 |

Sources: ([Li et al., 2019](https://gitlab.com/ucdavisnlp/antiscam)).

### Human Evaluation Data

In addition to the core corpus, the study generated a separate human evaluation dataset. The authors tested their models with **15 college-student volunteers**, each of whom was asked to pretend to be an attacker and interact with all models at least three times, yielding a total of **225 dialogs** ([Li et al., 2019](https://gitlab.com/ucdavisnlp/antiscam)). Each model received a total of **45 human ratings**, and the average score was reported as the final human-evaluation score ([Li et al., 2019](https://gitlab.com/ucdavisnlp/antiscam)). This evaluation corpus is distinct from the 220-dialog training corpus and represents an additional layer of data volume associated with the AntiScam research program.

**Table 5. Human Evaluation Data Volume**

| Metric | Value |
|---|---|
| Volunteers | 15 college students |
| Dialogs collected | 225 |
| Ratings per model | 45 |
| Models evaluated | 5 |

Source: ([Li et al., 2019](https://gitlab.com/ucdavisnlp/antiscam)).

## Source Reliability and Discrepancies

The two sources provided differ in one important respect. The primary source describes AntiScam as a corpus of "human-human dialogs" collected by pairing two workers on Amazon Mechanical Turk, one playing an attacker and the other an everyday user ([Li et al., 2019](https://gitlab.com/ucdavisnlp/antiscam)). The third-party research note, by contrast, repeatedly describes the corpus as consisting of "human-machine anti-scam dialogs" ([Third-party research note](https://gitlab.com/ucdavisnlp/antiscam)). Given that the primary source explicitly describes a human-human role-playing setup in which "workers cannot see their partners' instructions," the characterization as human-machine appears to be an error in the secondary note ([Li et al., 2019](https://gitlab.com/ucdavisnlp/antiscam)). In accordance with the principle of prioritizing reliable primary sources over less authoritative summaries, this report treats the 220 dialogs as human-human interactions, while noting that the raw count of 220 is consistent across both sources ([Li et al., 2019](https://gitlab.com/ucdavisnlp/antiscam); [Third-party research note](https://gitlab.com/ucdavisnlp/antiscam)).

## Interpretive Caveats

Several caveats should accompany any answer to the question of dataset size. First, the 3,044-sentence figure applies only to the 100 annotated dialogs, not to all 220 ([Li et al., 2019](https://gitlab.com/ucdavisnlp/antiscam)). Second, the average conversation length of 12.45 turns describes the full corpus, so it cannot be directly multiplied by 100 to describe the annotated subset without an unverified assumption of uniformity ([Third-party research note](https://gitlab.com/ucdavisnlp/antiscam)). Third, the dataset's 13 semantic slots and 15 intent categories mean that the effective annotation density is higher than the raw sentence count alone would suggest ([Li et al., 2019](https://gitlab.com/ucdavisnlp/antiscam)). Fourth, the vocabulary size of AntiScam is not reported in the available sources, unlike PersuasionForGood's 8,141-word vocabulary, so lexical diversity cannot be directly compared ([Li et al., 2019](https://gitlab.com/ucdavisnlp/antiscam)).

## Conclusion

In direct answer to the question, the AntiScam dataset is **220 human-human dialogs in total**, with **100 dialogs and 3,044 sentences manually annotated** by two expert annotators, an average conversation length of **12.45 turns**, and an average utterance length of **11.13 words** ([Li et al., 2019](https://gitlab.com/ucdavisnlp/antiscam); [Third-party research note](https://gitlab.com/ucdavisnlp/antiscam)). In terms of derived volume, the full corpus contains approximately **2,739 turns** and **30,484 words**. The dataset is accompanied by 15 intent categories, 13 semantic slots, and a human evaluation set of 225 dialogs. By the standards of task-oriented dialog research, AntiScam is a modestly sized but richly annotated corpus, smaller than PersuasionForGood in total dialog count but with a higher average turn length and a higher proportion of annotated dialogs relative to its total size ([Li et al., 2019](https://gitlab.com/ucdavisnlp/antiscam)). Its value lies less in raw volume and more in its deliberate design: it interleaves on-task and off-task content, supports multiple intents and semantic slots per sentence, and captures the adversarial dynamics of anti-scam conversations, making it a purposeful benchmark for non-collaborative dialog systems ([Li et al., 2019](https://gitlab.com/ucdavisnlp/antiscam)).

## References

Li, Y., Qian, K., Shi, W., & Yu, Z. (2019). *End-to-end trainable non-collaborative dialog system*. Retrieved from https://gitlab.com/ucdavisnlp/antiscam

Third-party research note. (n.d.). *End-to-end trainable non-collaborative dialog system: AntiScam dataset*. Retrieved from https://gitlab.com/ucdavisnlp/antiscam