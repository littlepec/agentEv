# How Big Is the AntiScam Dataset? A Detailed Assessment of Corpus Size, Composition, and Provenance

## Executive Summary

The AntiScam dataset is a purpose-built non-collaborative dialogue corpus introduced to support research on anti-scam and other adversarial conversational systems. Based on the primary source describing the corpus, its headline size is **220 human–human dialogs**, collected through a role-playing Amazon customer service scam scenario on Amazon Mechanical Turk (Li et al., 2019). Within that total, the paper reports an **average conversation length of 12.45 turns** and an **average utterance length of 11.13 words** (Li et al., 2019). A manually annotated subset of **100 dialogs containing 3,044 sentences** was labeled by two expert annotators with linguistic training, achieving an averaged weighted kappa of **0.874** (Li et al., 2019). In addition, **172 out of 220 users** (approximately 78.2%) correctly identified their partner as an attacker (Li et al., 2019).

This report examines each of these size-related figures, situates them against the dataset's collection methodology and annotation scheme, compares the corpus with the related PersuasionForGood dataset, and flags a notable discrepancy between the primary source and a third-party research note regarding whether the dialogs are human–human or human–machine.

## Introduction: What Is the AntiScam Dataset?

AntiScam was created by Li, Qian, Shi, and Yu at the University of California, Davis, to enrich the relatively thin supply of publicly available non-collaborative task datasets (Li et al., 2019). Non-collaborative tasks are those in which the user and the system do not share a common goal—examples include negotiation, persuasion, and defending against scammers (Li et al., 2019). The paper argues that because such settings require rapport-building, off-task and social content is interleaved with task-oriented content, motivating a hierarchical annotation scheme that separates on-task from off-task intents (Li et al., 2019).

The AntiScam corpus specifically models an Amazon customer service scam: one participant plays an "attacker" attempting to elicit personal information, while the other plays an everyday user who aims to protect their information and, after detecting the attack, to elicit the attacker's information and waste their time (Li et al., 2019). This design makes the corpus a benchmark for similar non-collaborative tasks, and the authors released the code and data at a public repository (Li et al., 2019).

## The Core Size Metrics

### Total Number of Dialogs

The single most direct answer to the question of dataset size is that **AntiScam contains 220 dialogs** (Li et al., 2019). The paper states plainly: "We collected 220 human-human dialogs" (Li et al., 2019). The third-party research note corroborates this figure, reporting that "the dataset contains 220 human-machine dialogs" and that "the total dataset comprises 220 human-machine dialogs" (Third-party research note, n.d.).

### Conversation and Utterance Length

Beyond the raw dialog count, the paper reports two descriptive length statistics for the full corpus:

- **Average conversation length: 12.45 turns** (Li et al., 2019)
- **Average utterance length: 11.13 words** (Li et al., 2019)

These averages are explicitly described as characteristics of the full AntiScam corpus rather than of the annotated subset alone (Third-party research note, n.d.). They indicate a corpus of short-to-medium-length task conversations, which is consistent with the human evaluation results reported later in the paper, where the best-performing model maintained conversations of approximately 14.9 turns—only marginally above the human–human average (Li et al., 2019).

### Annotated Subset Size

Not all 220 dialogs were annotated. The paper reports that two expert annotators with linguistic training manually annotated **3,044 sentences across 100 dialogs**, achieving a **0.874 averaged weighted kappa value** (Li et al., 2019). This means annotation coverage extends to roughly **45.5% of the dialogs** in the corpus (100 of 220), a derived proportion based on the reported figures (Li et al., 2019). The annotated subset therefore constitutes a substantial but partial slice of the total collection.

### Table 1: Summary of Reported AntiScam Size Metrics

| Metric | Reported Value | Coverage | Source |
|---|---|---|---|
| Total dialogs collected | 220 | Full corpus | (Li et al., 2019) |
| Average conversation length | 12.45 turns | Full corpus | (Li et al., 2019) |
| Average utterance length | 11.13 words | Full corpus | (Li et al., 2019) |
| Manually annotated dialogs | 100 | ~45.5% of corpus | (Li et al., 2019) |
| Manually annotated sentences | 3,044 | Annotated subset | (Li et al., 2019) |
| Inter-annotator agreement (weighted kappa) | 0.874 | Annotated subset | (Li et al., 2019) |
| Users correctly identifying attacker | 172 of 220 (~78.2%) | Full corpus | (Li et al., 2019) |
| Data splits (train/val/test) | 80% / 10% / 10% | Corpus-level protocol | (Li et al., 2019) |

## Composition: Sentences, Turns, and Derived Scale Estimates

The reported figures permit some cautious derived estimates of the corpus's internal scale, though these are not official statistics from the paper and should be treated as illustrative only.

Across the annotated subset, 3,044 sentences distributed over 100 dialogs implies an average of approximately **30.4 sentences per annotated dialog** (derived from Li et al., 2019). Given the reported average of 12.45 turns per conversation, this suggests that individual turns frequently comprise more than one sentence—consistent with the paper's methodological note that each conversation turn was segmented into single sentences, and that annotation was performed at the sentence rather than turn level (Li et al., 2019).

A further, more speculative, order-of-magnitude estimate can be obtained by multiplying the corpus-level averages: 220 dialogs × 12.45 turns × 11.13 words yields approximately **30,485 words** across the full corpus (derived from Li et al., 2019). This computation assumes that each reported "turn" corresponds to a single utterance of average length, which the paper does not explicitly confirm; the figure should therefore be regarded as a rough approximation rather than a reported dataset statistic (Li et al., 2019).

What is unambiguous is the annotation scheme's scope, which itself indicates the granularity of the dataset's labeling. The AntiScam corpus uses three task-specific on-task intents—**elicitation, providing_information, and refusal**—plus a shared set of off-task intents consisting of six general dialog acts (open_question, yes_no_question, positive_answer, negative_answer, responsive_statement, nonresponsive_statement) and six social acts (greeting, closing, apology, thanking, respond_to_thank, hold) (Li et al., 2019). The corpus also employs **13 main semantic slots**, including categories such as order_detail, payment, name, identity, address, phone_num, card_info, card_num, card_cvs, card_date, account_detail, and others (Li et al., 2019). Both the intent taxonomy and the slot inventory were applied across the annotated sentences, giving the dataset a rich multi-label structure that complements its relatively modest dialog count.

## Provenance and Collection Method

The size of AntiScam must be understood in light of how it was produced. The corpus was collected via a role-playing task on **Amazon Mechanical Turk**, with two randomly paired workers assigned asymmetric roles: an attacker trained to elicit information and a user instructed to protect their information and, upon detecting the attack, to prolong the conversation and elicit the attacker's information (Li et al., 2019). Workers were given specific fabricated personal data and could not see their partners' instructions (Li et al., 2019). Each worker could participate only once, which prevented participants from learning their partner's goals in advance and additionally constrained the feasible collection volume (Li et al., 2019).

The paper reports that of the 220 users, **172 correctly identified their partner as an attacker**, which the authors interpret as evidence that the simulated attackers were well trained and not trivially identifiable (Li et al., 2019). This detection rate is a quality signal for the corpus rather than a size measure, but it matters for interpreting scale: a dataset of 220 dialogs is arguably adequate for the benchmark purpose precisely because the interactions are adversarially realistic, which the detection statistic supports (Li et al., 2019).

Data were partitioned using an **80% training / 10% validation / 10% testing** protocol when fine-tuning models on AntiScam (Li et al., 2019). Applied to 220 dialogs, this corresponds to approximately 176 training dialogs, 22 validation dialogs, and 22 test dialogs, though the paper reports the proportions rather than the absolute split counts (Li et al., 2019).

## Comparative Scale: AntiScam Versus PersuasionForGood

To contextualize AntiScam's size, the paper evaluates MISSA on a second non-collaborative corpus, PersuasionForGood (Li et al., 2019). The comparative figures show that AntiScam is smaller in dialog count but slightly longer per conversation on average:

### Table 2: AntiScam Compared with PersuasionForGood

| Attribute | AntiScam | PersuasionForGood | Source |
|---|---|---|---|
| Total dialogs | 220 | 1,017 | (Li et al., 2019) |
| Dialogs annotated with dialog acts | 100 (in this work: 100 dialogs, 3,044 sentences) | 300 | (Li et al., 2019) |
| Average conversation length | 12.45 turns | 10.43 turns | (Li et al., 2019) |
| Vocabulary size | Not reported | 8,141 | (Li et al., 2019) |
| Average utterance length | 11.13 words | Not reported | (Li et al., 2019) |

The contrast is instructive. PersuasionForGood is roughly **4.6 times larger** in total dialog count than AntiScam (1,017 vs. 220), but only 300 of its dialogs are annotated with dialog acts—meaning that AntiScam's 100 annotated dialogs are proportionally comparable in annotation depth relative to the overall corpus (approximately 45.5% coverage versus approximately 29.5% for PersuasionForGood, derived from Li et al., 2019). The AntiScam corpus also has a slightly higher average conversation length (12.45 turns vs. 10.43 turns), suggesting that although it is smaller in breadth, it is not trivially shorter in interaction depth (Li et al., 2019).

## Evidence Reliability and a Notable Source Discrepancy

The available evidence comprises two items: the primary paper and a third-party research note summarizing the same paper. The primary source is the stronger evidentiary basis for size claims, and it consistently describes AntiScam as a corpus of **human–human dialogs**: "we created a corpus of human-human anti-scam dialogs" and "We collected 220 human-human dialogs" (Li et al., 2019). The third-party note, by contrast, repeatedly characterizes AntiScam as a corpus of **"human-machine anti-scam dialogs"** (Third-party research note, n.d.).

This is a material discrepancy in provenance, though not in size: both sources agree on the 220-dialog total, the 100-dialog/3,044-sentence annotation subset, the 12.45-turn and 11.13-word averages, and the 172-of-220 detection result (Li et al., 2019; Third-party research note, n.d.). Because the corpus was collected by pairing two Amazon Mechanical Turk workers who role-played attacker and user, the primary source's "human–human" description aligns directly with the described collection procedure (Li et al., 2019). The human–machine label in the third-party note appears to reflect the corpus's downstream use—training and evaluating an automated dialogue system—rather than its original collection design (Third-party research note, n.d.). For size questions, the distinction does not affect the reported magnitudes, but it does affect how the dataset's composition should be described.

Two further observations about reliability are warranted. First, the reported averages in the third-party note are explicitly attributed to the full AntiScam corpus rather than to the annotated subset, which is consistent with the primary source's framing (Third-party research note, n.d.; Li et al., 2019). Second, the human evaluation conducted to benchmark models against AntiScam involved **15 college-student volunteers**, **225 collected dialogs**, and **45 ratings per model** (Li et al., 2019). Those 225 dialogs are an evaluation artifact, not part of the AntiScam corpus itself, and should not be conflated with the dataset's 220-dialog size (Li et al., 2019).

## Implications of Dataset Size for Research

The AntiScam corpus's scale—220 dialogs, of which 100 are annotated—places it in the category of small, purpose-built benchmark datasets rather than large-scale training corpora. The authors themselves justify creating it on the grounds that existing non-collaborative datasets were not explicitly designed to interleave on-task and off-task content, making it difficult to disentangle these elements and measure performance (Li et al., 2019). In that sense, the corpus's value derives less from scale than from its annotation design: the hierarchical on-task/off-task intent scheme and the 13-slot semantic annotation scheme provide the kind of detailed supervision that larger but unannotated conversation corpora cannot offer (Li et al., 2019).

This interpretation is supported by the empirical results reported on the corpus. MISSA achieved a perplexity of 21.07 on AntiScam and outperformed both the TransferTransfo and hybrid baselines on most automatic and human metrics, with the authors attributing its gains in coherence and conversation length specifically to the structured intent and slot supervision (Li et al., 2019). Notably, MISSA maintained conversations of 14.9 turns compared with 8.5 turns for TransferTransfo, and achieved a task success score of 1.294 versus 1.025—indicating that even a 220-dialog corpus can support meaningful model differentiation when the annotation is information-dense (Li et al., 2019).

The corpus also exhibits measurable internal structure that speaks to its composition. The paper reports that users produced substantially more refusals than attackers (74 vs. 19), asked more open questions (173 vs. 54) and yes/no questions (165 vs. 117), and that the two roles together generated a large volume of social content (292 and 252 sentences, respectively) (Li et al., 2019). These sentence-level counts reinforce the picture of a compact but richly labeled dataset in which off-task and social content form a substantial share of the total.

## Conclusion

The AntiScam dataset is a corpus of **220 anti-scam dialogs**, averaging **12.45 turns** per conversation and **11.13 words** per utterance, with a manually annotated subset of **100 dialogs comprising 3,044 sentences** labeled by two expert annotators with linguistic training at a weighted kappa of **0.874** (Li et al., 2019). It was collected on Amazon Mechanical Turk through a role-playing Amazon customer service scam scenario, in which **172 of 220 users** successfully identified their partner as an attacker (Li et al., 2019). It is smaller in raw dialog count than the companion PersuasionForGood corpus (220 vs. 1,017 dialogs), but its annotation density and slightly longer average conversations make it a targeted benchmark rather than a large-scale resource (Li et al., 2019). Readers should note the discrepancy between the primary source's "human–human" characterization and the third-party note's "human–machine" phrasing; both nevertheless agree on all quantitative size figures (Li et al., 2019; Third-party research note, n.d.).

## References

Li, Y., Qian, K., Shi, W., & Yu, Z. (2019). *End-to-End Trainable Non-Collaborative Dialog System*. arXiv:1911.10742. https://arxiv.org/abs/1911.10742

Third-party research note: *End-to-End Trainable Non-Collaborative Dialog System* (document_2.txt, n.d.).