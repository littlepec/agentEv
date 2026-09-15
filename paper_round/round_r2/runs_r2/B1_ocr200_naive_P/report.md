# How Big Is the ANTISCAM Dataset? A Detailed Assessment of Corpus Size, Composition, and Annotation Scope

## Executive Summary

The ANTISCAM dataset is a human–human anti-scam dialogue corpus introduced by Yu Li, Kun Qian, Weiyan Shi, and Zhou Yu of the University of California, Davis, in the paper *End-to-End Trainable Non-Collaborative Dialog System* ([Yu et al., 2020](https://arxiv.org/abs/1911.10742)). The primary source — the paper itself — reports that the corpus consists of **220 human–human dialogs**, with an average conversation length of **12.45 turns** and an average utterance length of **11.13 words** ([Yu et al., 2020](https://arxiv.org/abs/1911.10742)). A manually annotated subset of **100 dialogs containing 3,044 sentences** was labeled by two expert annotators with linguistic training, achieving an averaged weighted kappa value of **0.874** ([Yu et al., 2020](https://arxiv.org/abs/1911.10742)).

A secondary source supplied for this analysis — a third-party research note ([Document 2, n.d.](https://arxiv.org/abs/1911.10742)) — asserts that the corpus contains **320 human–human dialogs**. This figure conflicts with the original paper and appears to be an error. The present report evaluates both figures against the available evidence, concludes that **220 dialogs is the accurate and defensible size of the ANTISCAM dataset**, and contextualizes that number within the corpus's turn counts, annotation scope, intent taxonomy, and evaluation scale.

## The Primary Figure: 220 Human–Human Dialogs

The ANTISCAM corpus was collected to enrich the scarce supply of publicly available non-collaborative task datasets. The authors note that "as non-collaborative tasks are still relatively new to the study of dialog systems, there are insufficiently many meaningful datasets for evaluation" ([Yu et al., 2020](https://arxiv.org/abs/1911.10742)). To address this gap, they created "a corpus of human-human anti-scam dialogs in order to learn human elicitation strategies," choosing "a popular Amazon customer service scam scenario to collect dialogs between users and attackers who aim to collect users' information" ([Yu et al., 2020](https://arxiv.org/abs/1911.10742)).

The corpus size is reported explicitly in the dataset description: "We posted a role-playing task on the Amazon Mechanical Turk platform and collected a typing conversation dataset named ANTISCAM. We collected 220 human-human dialogs" ([Yu et al., 2020](https://arxiv.org/abs/1911.10742)). The same figure is repeated in the paper's appendix under the "Anti-Scam Collection Setting" section: "We collected 220 human-human dialogs. The average conversation length is 12.45 turns and the average utterance length is 11.13 words. Only 172 out of 220 users successfully identified their partner as an attacker, suggesting that the attackers are well trained and not too easily identifiable" ([Yu et al., 2020](https://arxiv.org/abs/1911.10742)).

Two independent occurrences of the number "220" within the same paper — one in the main body and one in the appendix — strengthen confidence in this figure. Furthermore, the ratio of successful attacker identifications (172) to total dialogs (220) is internally consistent across both passages, since both report "172 out of 220."

| Size Dimension | Reported Value | Source |
|---|---|---|
| Total human–human dialogs | 220 | Yu et al. (2020) |
| Average conversation length | 12.45 turns | Yu et al. (2020) |
| Average utterance length | 11.13 words | Yu et al. (2020) |
| Manually annotated subset | 100 dialogs | Yu et al. (2020) |
| Manually annotated sentences | 3,044 sentences | Yu et al. (2020) |
| Annotators | 2 expert annotators with linguistic training | Yu et al. (2020) |
| Inter-annotator agreement | 0.874 averaged weighted kappa | Yu et al. (2020) |
| Users identifying partner as attacker | 172 of 220 | Yu et al. (2020) |

## The 320-Dialog Claim and Why It Is Unreliable

The third-party research note states that "the dataset contains 320 human-human dialogs" and repeats that "the total dataset comprises 320 human-human dialogs" ([Document 2, n.d.](https://arxiv.org/abs/1911.10742)). It further claims that "the paper reports that 172 out of 320 users successfully identified their partner as an attacker" ([Document 2, n.d.](https://arxiv.org/abs/1911.10742)).

This claim is not supported by the primary source. The note's own internal logic collapses on inspection: the numerator 172 is preserved from the original paper, where it was paired with a denominator of 220, not 320. If the corpus truly contained 320 dialogs while only 172 users detected the attacker, the detection rate would drop from approximately 78.2% to 53.8% — a materially different interpretation of how "well trained" the attackers were. The original paper explicitly interprets the 172-of-220 ratio as evidence that "the attackers are well trained and not too easily identifiable" ([Yu et al., 2020](https://arxiv.org/abs/1911.10742)), an inference that is far weaker under a 172-of-320 reading.

| Claim | Primary Source (Yu et al., 2020) | Secondary Note (Document 2) | Assessment |
|---|---|---|---|
| Total dialogs | 220 | 320 | Primary source is authoritative |
| Detection rate | 172 of 220 (≈78.2%) | 172 of 320 (≈53.8%) | Note contradicts itself and the paper |
| Annotated subset | 100 dialogs / 3,044 sentences | 100 dialogs / 3,044 sentences | Sources agree |
| Avg. conversation length | 12.45 turns | 12.45 turns | Sources agree |
| Avg. utterance length | 11.13 words | 11.13 words | Sources agree |

Notably, the secondary note agrees with the primary source on every other statistic — the 100-dialog annotation subset, the 3,044 annotated sentences, the two expert annotators, the 12.45-turn average, and the 11.13-word average ([Document 2, n.d.](https://arxiv.org/abs/1911.10742)). The 320 figure is therefore best understood as an isolated transcription or paraphrase error rather than a correction of the original publication. Given the instruction to prioritize reliability and significance, the primary, peer-reviewed published paper ([Yu et al., 2020](https://arxiv.org/abs/1911.10742)) must be preferred over an unattributed third-party summary. My concrete assessment is that **the ANTISCAM dataset contains 220 human–human dialogs**, and the 320 figure should not be propagated.

## Size Beyond the Raw Dialog Count

Raw dialog count is only one dimension of a dataset's magnitude. The ANTISCAM corpus can be sized along several additional axes.

### Conversational Volume

With 220 dialogs averaging 12.45 turns each, the corpus comprises approximately **2,739 conversational turns** in total. At an average of 11.13 words per utterance, the corpus contains roughly **30,000 words** of dialogue. These figures are approximate aggregates derived from the authors' reported averages ([Yu et al., 2020](https://arxiv.org/abs/1911.10742)); the paper does not publish exact totals for turns or token counts.

### Annotation Depth

The annotated portion is substantial relative to the corpus. Two expert annotators with linguistic training annotated **3,044 sentences across 100 dialogs**, achieving a **0.874 averaged weighted kappa value** ([Yu et al., 2020](https://arxiv.org/abs/1911.10742)). This means roughly 45% of the 220 dialogs received sentence-level manual annotation. The paper reports that independent annotators had to "segment each conversation turn into single sentences and then annotate each sentence rather than turns" ([Yu et al., 2020](https://arxiv.org/abs/1911.10742)), following the approach of Wang et al.

### Label Taxonomy

The annotation scheme itself adds structural size. The authors designed a hierarchical intent scheme that separates on-task from off-task intents. For the anti-scam task, three task-specific on-task intents were defined — `elicitation`, `providing-information`, and `refusal` — while the off-task layer is universal across non-collaborative tasks, comprising six general intents (open-question, yes/no-question, positive_answer, negative_answer, responsive_statement, and nonresponsive_statement) plus six social intents (greeting, closing, apology, thanking, respond_to_thank, and hold) ([Yu et al., 2020](https://arxiv.org/abs/1911.10742)).

Separately, the authors "identify 13 main semantic slots in the anti-scam task, for example, credit card numbers," spanning categories such as order_detail, order_update, payment, name, identity, address, phone_num, card_info, card_num, card_cvs, account_detail, card_date, and others ([Yu et al., 2020](https://arxiv.org/abs/1911.10742)).

### Size in Tokens of Supervision

Because each conversation turn was segmented into sentences and each sentence was labeled with both an intent and a semantic slot, the 3,044-sentence annotation set yields on the order of 6,000 or more individual label assignments ([Yu et al., 2020](https://arxiv.org/abs/1911.10742)). This figure is not reported directly but follows from the dual-labeling design described in the paper.

## Class Balance as an Indicator of Corpus Composition

The composition of the corpus reveals how its size is distributed across the two speaker roles. The authors report distinct intent distributions for attackers and users:

| Intent Category | Attackers | Users |
|---|---|---|
| Refusal | 19 | 74 |
| Open questions | 54 | 173 |
| Yes/no questions | 117 | 165 |
| Social content | 292 | 252 |

Source: [Yu et al., 2020](https://arxiv.org/abs/1911.10742).

The disparity is explained by the experimental design: users were instructed to prolong the conversation once they detected an attacker, which is why "users also ask more open_questions (173 vs 54) and yes_no-questions (165 vs 117) for off-task content" ([Yu et al., 2020](https://arxiv.org/abs/1911.10742)). The authors additionally observe that both roles produced substantial social content — "292 in total and 252 in total" — concluding that "it is important to have social intent sentences to maintain the conversation" ([Yu et al., 2020](https://arxiv.org/abs/1911.10742)).

## Comparative Context: ANTISCAM Versus PERSUASIONFORGOOD

The paper evaluated its model (MISSA) on two non-collaborative datasets, which allows a direct size comparison.

| Dataset | Total Dialogs | Annotated Dialogs | Avg. Conversation Length | Vocabulary |
|---|---|---|---|---|
| ANTISCAM | 220 | 100 | 12.45 turns | Not reported |
| PERSUASIONFORGOOD | 1,017 | 300 | 10.43 turns | 8,141 |

Sources: [Yu et al., 2020](https://arxiv.org/abs/1911.10742); [Wang et al., 2019](https://arxiv.org/abs/1906.06725).

ANTISCAM is substantially smaller than PERSUASIONFORGOOD in raw dialog count — roughly 22% the size — but its dialogs are somewhat longer on average (12.45 versus 10.43 turns) and its annotation density is higher, since 100 of 220 dialogs (≈45%) were sentence-level annotated compared with 300 of 1,017 (≈30%) for PERSUASIONFORGOOD ([Yu et al., 2020](https://arxiv.org/abs/1911.10742)). This trade-off suggests ANTISCAM prioritizes annotation depth over raw breadth, which is consistent with the authors' stated goal of providing "a valuable example" for a research area with "insufficiently many meaningful datasets" ([Yu et al., 2020](https://arxiv.org/abs/1911.10742)).

## The Size of the Evaluation Effort

The scale of evaluation conducted against the corpus further contextualizes its magnitude. The human evaluation enlisted **15 college-student volunteers**, each asked to "pretend to be an attacker and interact with all the models for at least three times to avoid randomness," producing a total of **225 collected dialogs** and **45 human ratings per model** across five models ([Yu et al., 2020](https://arxiv.org/abs/1911.10742)). Notably, this evaluation corpus (225 dialogs) is slightly larger than the original training corpus (220 dialogs), reflecting the relatively compact size of the underlying resource.

In terms of performance, the MISSA model maintained conversations of **14.9 turns** on ANTISCAM compared with **8.5 turns** for the TransferTransfo baseline, and achieved a task success score of **1.294** versus **1.025** ([Yu et al., 2020](https://arxiv.org/abs/1911.10742)). The paper's automatic metrics also show MISSA achieving the lowest perplexity among the compared systems on ANTISCAM at **21.07** ([Yu et al., 2020](https://arxiv.org/abs/1911.10742)).

| Model | Perplexity | Dialog Length (turns) | Task Success |
|---|---|---|---|
| TransferTransfo | 32.96 | 8.5 | 1.025 |
| Hybrid | Not reported | 8.2 | 0.975 |
| MISSA | 21.07 | 14.9 | 1.294 |
| MISSA-sel | 30.54 | 9.9 | 1.000 |
| MISSA-con | 24.46 | 14.8 | 1.341 |

Source: [Yu et al., 2020](https://arxiv.org/abs/1911.10742).

## Data Splits

The corpus was partitioned using an 80/10/10 scheme: "we use 80% data for training, 10% data for validation, and 10% data for testing" ([Yu et al., 2020](https://arxiv.org/abs/1911.10742)). Applied to 220 dialogs, this implies approximately 176 training dialogs, 22 validation dialogs, and 22 test dialogs. The models were first pre-trained on the PERSONA-CHAT dataset before fine-tuning on ANTISCAM and PERSUASIONFORGOOD ([Yu et al., 2020](https://arxiv.org/abs/1911.10742)).

## Interpretation and Opinion

Based on the evidence presented, my assessment is unambiguous: **the ANTISCAM dataset consists of 220 human–human dialogs**, not 320. The 220 figure appears twice in the primary source, is internally consistent with the reported 172-of-220 detection statistic, and is embedded in a peer-reviewed publication from the AAAI Conference on Artificial Intelligence ([Yu et al., 2020](https://arxiv.org/abs/1911.10742)). The 320 figure appears only once in a secondary, unattributed summary and is contradicted by that summary's own repetition of the 172 numerator ([Document 2, n.d.](https://arxiv.org/abs/1911.10742)).

Equally important is the qualitative point that "size" for a dataset of this kind is multidimensional. A corpus of 220 dialogs is modest by the standards of large-scale dialogue datasets such as PERSUASIONFORGOOD's 1,017 dialogs ([Wang et al., 2019](https://arxiv.org/abs/1906.06725)), but ANTISCAM compensates with dense, sentence-level annotation across a rich hierarchical label taxonomy: 3,044 sentences, dual intent-and-slot labeling, three task-specific on-task intents, twelve universal off-task intents, and thirteen semantic slot categories ([Yu et al., 2020](https://arxiv.org/abs/1911.10742)). The corpus's approximately 2,739 turns and roughly 30,000 words of dialogue, aggregated from the reported averages, further characterize its scope.

The authors themselves frame ANTISCAM as an example rather than an exhaustive benchmark, describing it as a resource that "can serve as a benchmark dataset for similar non-collaborative tasks" and noting they release the code and data publicly ([Yu et al., 2020](https://arxiv.org/abs/1911.10742)). Later work building on this corpus may expand it, and researchers relying on secondary summaries should verify the canonical figure of 220 against the original publication to avoid propagating the incorrect 320-dialog count.

## Conclusion

The ANTISCAM dataset is a compact but densely annotated human–human anti-scam dialogue corpus. Its size is **220 dialogs**, averaging **12.45 turns** and **11.13 words per utterance**, with **100 dialogs and 3,044 sentences** manually annotated by two expert linguistically trained annotators at a **0.874 weighted kappa** agreement level ([Yu et al., 2020](https://arxiv.org/abs/1911.10742)). Reports of a 320-dialog corpus are inconsistent with the primary source and should be treated as erroneous. When citing the dataset's size, researchers should reference the original paper and use 220 as the authoritative figure.

## References

Document 2: Third-party research note on the End-to-End Trainable Non-Collaborative Dialog System. (n.d.). [Secondary source note; unreliable on the corpus-size figure.]

Wang, X., Shi, W., Kim, R., Oh, Y., Yang, S., Zhang, J., & Yu, Z. (2019). Persuasion for good: Towards a personalized persuasive dialogue system for social good. *arXiv preprint arXiv:1906.06725*. [https://arxiv.org/abs/1906.06725](https://arxiv.org/abs/1906.06725)

Yu, L., Qian, K., Shi, W., & Yu, Z. (2020). End-to-end trainable non-collaborative dialog system. *Proceedings of the AAAI Conference on Artificial Intelligence*. [https://arxiv.org/abs/1911.10742](https://arxiv.org/abs/1911.10742)