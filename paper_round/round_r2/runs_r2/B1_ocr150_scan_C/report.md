# How Big Is the ANTISCAM Dataset? A Detailed Assessment of the Size, Composition, and Annotation Scope of a Non-Collaborative Anti-Scam Dialogue Corpus

## Introduction

The ANTISCAM dataset is a human–human dialogue corpus created to study non-collaborative conversation, specifically the scenario in which an ordinary user must recognize, resist, and counter an attacker impersonating Amazon customer service in order to extract personal information such as credit card numbers, CVVs, expiration dates, names, and billing addresses ([Li et al., 2020](document_1.txt)). Answering the question "how big is the ANTISCAM dataset?" requires more than a single number, because the corpus has a two-tier structure: a full collection of dialogues and a smaller manually annotated subset that supports supervised learning. This report examines the dataset's size along several dimensions — number of dialogues, number of annotated sentences, average turns and utterance length, annotation scheme breadth, and comparative scale against a related non-collaborative corpus — and evaluates what those dimensions mean for the dataset's utility, reliability, and limitations.

## The Two-Tier Structure of the Corpus

The most important fact about the size of ANTISCAM is that the paper reports two distinct figures: the total number of collected dialogues and the number of dialogues that were manually annotated. The authors state plainly that they "collected 220 human-human dialogs" and that the average conversation length is 12.45 turns, with an average utterance length of 11.13 words ([Li et al., 2020](document_1.txt)). Separately, the annotation effort covered only a portion of this material: "We recruited two expert annotators who have linguistic training to annotate 3,044 sentences in 100 dialogs, achieving a 0.874 averaged weighted kappa value" ([Li et al., 2020](document_1.txt)). A third-party research note summarizing the same paper confirms this partitioning, describing the total dataset as "220 human-human dialogs" and the "manually annotated subset" as "100 dialogs and 3,044 sentences" ([Third-Party Research Note](document_2.txt)).

### Table 1. Core Size Dimensions of ANTISCAM

| Dimension | Reported Value | Source |
|---|---|---|
| Total human–human dialogues collected | 220 | ([Li et al., 2020](document_1.txt)) |
| Manually annotated dialogues | 100 | ([Li et al., 2020](document_1.txt)) |
| Manually annotated sentences | 3,044 | ([Li et al., 2020](document_1.txt)) |
| Average conversation length (full corpus) | 12.45 turns | ([Li et al., 2020](document_1.txt)) |
| Average utterance length (full corpus) | 11.13 words | ([Li et al., 2020](document_1.txt)) |
| Annotators | 2 expert annotators with linguistic training | ([Li et al., 2020](document_1.txt)) |
| Inter-annotator agreement | 0.874 averaged weighted kappa | ([Li et al., 2020](document_1.txt)) |
| Users who identified their partner as an attacker | 172 out of 220 | ([Li et al., 2020](document_1.txt)) |

The distinction between the 220-dialogue corpus and the 100-dialogue annotated subset is not a trivial bookkeeping detail. It determines what kinds of research the dataset can support: the full 220 dialogues provide distributional and behavioral evidence about how real people behave under attempted social-engineering attacks, while the 100 annotated dialogues supply the supervised labels required to train intent and semantic-slot classifiers ([Li et al., 2020](document_1.txt)).

## Conversational Scale in Turns and Words

Beyond dialogue counts, the paper quantifies the linguistic volume of the corpus through turn-level and utterance-level averages. It reports that collection produced 220 dialogues whose average conversation length is 12.45 turns and whose average utterance length is 11.13 words ([Li et al., 2020](document_1.txt)). The third-party note explicitly clarifies that these averages "describe the full AntiScam corpus," not merely the annotated subset ([Third-Party Research Note](document_2.txt)).

### Table 2. Derived Approximations of Corpus Volume

| Derived Quantity | Calculation | Approximate Value |
|---|---|---|
| Total dialogue turns (full corpus) | 220 dialogues × 12.45 turns | ≈ 2,739 turns |
| Total words at turn level (full corpus) | ≈ 2,739 turns × 11.13 words | ≈ 30,485 words |
| Annotated sentences per annotated dialogue | 3,044 sentences ÷ 100 dialogues | ≈ 30.4 sentences per dialogue |
| Training dialogues under an 80/10/10 split | 80% of 220 | ≈ 176 dialogues |
| Validation / test dialogues | 10% each of 220 | ≈ 22 dialogues each |

It is important to state clearly that the values in Table 2 beyond the first three reported statistics are derived estimates computed by this report from the paper's own averages and not figures published in the paper ([Li et al., 2020](document_1.txt)). They are presented to convey order of magnitude. The only sentence-level count that the paper states directly is 3,044 annotated sentences ([Li et al., 2020](document_1.txt)). The sentence count for the remaining 120 unannotated dialogues is not reported anywhere in the supplied material.

## Annotation Breadth as a Measure of Size

Size in a dialogue dataset is not only a matter of raw volume; it also concerns the number of label categories that were applied. ANTISCAM uses a hierarchical annotation scheme that separates on-task content from off-task content ([Li et al., 2020](document_1.txt)). For the anti-scam task, the authors define three on-task intents — elicitation, providing-information, and refusal — reflecting the central actions of the scam scenario ([Li et al., 2020](document_1.txt)). The off-task layer is shared across non-collaborative tasks and comprises six general intents that encode syntactic function (open_question, yes_no_question, positive_answer, negative_answer, responsive_statement, and nonresponsive_statement) plus six social intents (greeting, closing, apology, thanking, respond_to_thank, and hold) ([Li et al., 2020](document_1.txt)).

### Table 3. Hierarchical Intent Categories Applied to ANTISCAM

| Layer | Categories | Count |
|---|---|---|
| On-task (anti-scam specific) | Elicitation; providing-information; refusal | 3 |
| Off-task general | open_question; yes_no_question; positive_answer; negative_answer; responsive_statement; nonresponsive_statement | 6 |
| Off-task social | greeting; closing; apology; thanking; respond_to_thank; hold | 6 |

On the semantic side, the authors "identify 13 main semantic slots in the anti-scam task, for example, credit card numbers," and present the scheme in their Table 2 ([Li et al., 2020](document_1.txt)). The enumerated slots in that table include order.update, payment, phone.num, name, card.num, account.detail, identity, address, card.info, card.cvs, card.date, and others ([Li et al., 2020](document_1.txt)). This means each annotated sentence carries both an intent label and one or more semantic-slot labels, and the authors note that MISSA "is able to classify multiple intents and multiple semantic slots in a single utterance with these classifiers" ([Li et al., 2020](document_1.txt)). Consequently, the label volume of the dataset is substantially larger than the 3,044 sentence count alone might suggest, because sentences can be multiply labeled.

## Distributional Characteristics of the Collected Content

The paper provides several content-distribution statistics that further characterize the dataset's composition. Users produced more refusals than attackers (74 versus 19), "because users are more likely to refuse to provide requested information if they have detected the attacker" ([Li et al., 2020](document_1.txt)). Users also asked more open questions (173 versus 54) and more yes/no questions (165 versus 117) for off-task content, a pattern the authors attribute to the instruction to prolong the conversation after detecting an attacker ([Li et al., 2020](document_1.txt)). Both roles generated substantial social content, with 292 social-content sentences attributed to attackers and 252 to users, which the authors interpret as evidence "that it is important to have social intent sentences to maintain the conversation" ([Li et al., 2020](document_1.txt)).

A behavioral outcome statistic is also reported: only 172 out of 220 users successfully identified their partner as an attacker, which the authors interpret as indicating "that the attackers are well trained and not too easily identifiable" ([Li et al., 2020](document_1.txt)). This equates to approximately 78.2% detection, a derived percentage, meaning that roughly 48 of the 220 users failed to identify the attacker within the dialogue. This feature is relevant to dataset size because it confirms that the collection contains genuine adversarial difficulty rather than trivially detectable attacks ([Third-Party Research Note](document_2.txt)).

## Comparative Scale: ANTISCAM Versus PERSUASIONFORGOOD

Placing ANTISCAM in context helps clarify whether 220 dialogues should be considered large or small for this research area. The companion dataset used in the same paper, PERSUASIONFORGOOD, contains 1,017 dialogues, of which 300 are annotated, with an average conversation length of 10.43 and a vocabulary size of 8,141 ([Li et al., 2020](document_1.txt)). By raw dialogue count, PERSUASIONFORGOOD is roughly 4.6 times larger than ANTISCAM, although only 300 of its dialogues are annotated — still three times the 100 annotated dialogues in ANTISCAM.

### Table 4. Scale Comparison of the Two Non-Collaborative Corpora

| Property | ANTISCAM | PERSUASIONFORGOOD |
|---|---|---|
| Total dialogues | 220 | 1,017 |
| Annotated dialogues | 100 | 300 |
| Average conversation length | 12.45 turns | 10.43 turns |
| Average utterance length | 11.13 words | Not reported in supplied material |
| Vocabulary size | Not reported in supplied material | 8,141 |
| Annotated sentences | 3,044 | Not reported in supplied material |

Both corpora were collected on Amazon Mechanical Turk as typed conversations with off-task dialogue interleaved with on-task content ([Li et al., 2020](document_1.txt)). The authors explicitly justify creating ANTISCAM on the grounds that "there are insufficiently many meaningful datasets for evaluation" for non-collaborative tasks and that existing corpora "are not specifically collected and designed for non-collaborative tasks," making it "difficult to disentangle the on-task and off-task contents and measure the performance" ([Li et al., 2020](document_1.txt)).

## What the Size Enables and What It Constrains

An assessment of dataset size should be honest about both capabilities and limitations. On the capability side, ANTISCAM is large enough to support multi-task end-to-end training. The authors fine-tuned their MISSA model on ANTISCAM and PERSUASIONFORGOOD using 80% of the data for training, 10% for validation, and 10% for testing ([Li et al., 2020](document_1.txt)). They report that their trained system maintained longer conversations (14.9 turns) than the TransferTransfo baseline (8.5 turns) and achieved a higher task-success score (1.294 versus 1.025), indicating that the dataset provides sufficient signal for models to learn strategic information elicitation ([Li et al., 2020](document_1.txt)). The paper's own intent predictor achieves 84% accuracy and its semantic slot predictor 77% on ANTISCAM, and these trained predictors were then reused to evaluate baseline outputs ([Li et al., 2020](document_1.txt)). Such results would be difficult to obtain from a corpus an order of magnitude smaller.

On the constraint side, three limitations follow from the reported sizes. First, the annotated subset is only 100 dialogues; with an 80/10/10 split of the 220-dialogue corpus, the test portion is small, and the authors themselves observe that "there are more possible responses with the same intent in PERSUASIONFORGOOD than in ANTISCAM," suggesting that model structure should be adjusted "according to the nature of the dataset" ([Li et al., 2020](document_1.txt)). Second, the average dialogue is short — 12.45 turns — and the paper acknowledges a broader weakness of the underlying GPT-based approach: "MISSA still produces responses that are not consistent with their distant conversation history as GPT can only track a limited history span," with plans to develop methods that "can effectively track longer dialog context" ([Li et al., 2020](document_1.txt)). Third, the human evaluation, while rigorous, was necessarily modest in scale: 15 college-student volunteers each interacted with five models at least three times, yielding 225 collected dialogues and 45 human ratings per model ([Li et al., 2020](document_1.txt)).

## Reliability and Provenance of the Size Figures

The size figures cited here derive from two sources. The primary source is the paper "End-to-End Trainable Non-Collaborative Dialog System" by Yu Li, Kun Qian, Weiyan Shi, and Zhou Yu of the University of California, Davis, dated November 2019 and published in the 2020 proceedings of the Association for the Advancement of Artificial Intelligence ([Li et al., 2020](document_1.txt)). The secondary source is a third-party research note whose stated purpose is to consolidate exactly the statistics at issue here — the AntiScam corpus's number of dialogues and annotation statistics ([Third-Party Research Note](document_2.txt)). Crucially, the two sources agree on every overlapping figure: 220 total dialogues, 100 annotated dialogues, 3,044 annotated sentences, 12.45 average turns, 11.13 average words, and 172 of 220 users identifying the attacker ([Third-Party Research Note](document_2.txt)). This convergence increases confidence in the numbers. The paper also states that code and data were released publicly at `https://gitlab.com/ucdavisnlp/antiscam`, which provides a route to independent verification ([Li et al., 2020](document_1.txt)).

## Conclusion and Assessment

The most defensible direct answer to the question is that ANTISCAM comprises 220 human–human anti-scam dialogues, of which 100 dialogues containing 3,044 sentences were manually annotated by two linguistically trained expert annotators at a 0.874 weighted kappa, with average conversation length of 12.45 turns and average utterance length of 11.13 words ([Li et al., 2020](document_1.txt); [Third-Party Research Note](document_2.txt)). Any claim that the dataset simply "is 220 dialogues" or simply "is 100 dialogues" is incomplete: the first figure describes the collected corpus, the second the supervised training and evaluation material. In my assessment, ANTISCAM should be regarded as a small-to-medium specialist corpus rather than a large-scale benchmark. It is considerably smaller than PERSUASIONFORGOOD (1,017 dialogues) and far smaller than general-purpose dialogue corpora such as PERSONA-CHAT, which served as the pre-training source for the models in this work ([Li et al., 2020](document_1.txt)). Its value lies less in scale than in annotation depth: a fine-grained hierarchical intent scheme with three on-task intents, six general off-task intents, six social intents, and 13 semantic slots, all applied at sentence level across 3,044 sentences, combined with a rare behavioral finding that only about 78% of users detected their attacker ([Li et al., 2020](document_1.txt)). For researchers seeking to reproduce or extend non-collaborative dialogue research, the practical implication is that ANTISCAM offers rich labels but limited volume, and results trained on it — including MISSA's reported advantages over TransferTransfo and hybrid baselines on fluency, coherence, engagement, and task success — should be interpreted with that sample size in mind ([Li et al., 2020](document_1.txt)).

## References

Li, Y., Qian, K., Shi, W., & Yu, Z. (2020). *End-to-end trainable non-collaborative dialog system* [document_1.txt]. University of California, Davis.

Third-party research note: *End-to-end trainable non-collaborative dialog system* [document_2.txt].