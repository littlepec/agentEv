# How Big Is the ANTISCAM Dataset? Scale, Composition, and Annotation of a Non-Collaborative Dialog Corpus

## Introduction

The ANTISCAM dataset is a corpus of human-human anti-scam dialogs introduced by Yu Li, Kun Qian, Weiyan Shi, and Zhou Yu (2020) in the paper "End-to-End Trainable Non-Collaborative Dialog System" ([Li et al., 2020](https://arxiv.org/abs/1911.10742)). The corpus was created to enrich the supply of publicly available non-collaborative task datasets and to serve as a benchmark for a class of dialog systems that must handle both on-task and off-task content, such as persuasion, negotiation, and scam deterrence ([Li et al., 2020](https://arxiv.org/abs/1911.10742)). Because non-collaborative dialog research is "still relatively new," the authors explicitly note that there are "insufficiently many meaningful datasets for evaluation" and present ANTISCAM as a valuable example ([Li et al., 2020](https://arxiv.org/abs/1911.10742)).

Answering the question "how big is the ANTISCAM dataset?" requires more than a single number. Size can be measured along several dimensions: the number of dialogs, the number of annotated dialogs and sentences, the average conversation and utterance length, the number of intent categories and semantic slots, and the volume of natural language produced. This report examines each of these dimensions, notes an important discrepancy between the primary source and a secondary note, and offers aggregate estimates derived from the reported figures.

## The Core Answer: 220 Human-Human Dialogs

According to the primary source — the paper itself — ANTISCAM consists of **220 human-human dialogs** ([Li et al., 2020](https://arxiv.org/abs/1911.10742)). This figure is stated twice in the paper: once in the dataset description section and once again in the appendix describing the anti-scam collection setting ([Li et al., 2020](https://arxiv.org/abs/1911.10742)). The authors describe the corpus as one "of human-human anti-scam dialogs in order to learn human elicitation strategies," collected by pairing users with attackers in a simulated Amazon customer service scam scenario ([Li et al., 2020](https://arxiv.org/abs/1911.10742)).

Beyond the dialog count, the paper reports the following size-related statistics:

- Average conversation length: **12.45 turns** ([Li et al., 2020](https://arxiv.org/abs/1911.10742))
- Average utterance length: **11.13 words** ([Li et al., 2020](https://arxiv.org/abs/1911.10742))
- Users who successfully identified their partner as an attacker: **172 out of 220** ([Li et al., 2020](https://arxiv.org/abs/1911.10742))
- Manually annotated subset: **100 dialogs and 3,044 sentences** ([Li et al., 2020](https://arxiv.org/abs/1911.10742))
- Inter-annotator agreement: **0.874 averaged weighted kappa** ([Li et al., 2020](https://arxiv.org/abs/1911.10742))

| Size Dimension | Reported Value | Source |
|---|---|---|
| Human-human dialogs collected | 220 | Primary paper ([Li et al., 2020](https://arxiv.org/abs/1911.10742)) |
| Manually annotated dialogs | 100 | Primary paper ([Li et al., 2020](https://arxiv.org/abs/1911.10742)) |
| Annotated sentences | 3,044 | Primary paper ([Li et al., 2020](https://arxiv.org/abs/1911.10742)) |
| Average conversation length | 12.45 turns | Primary paper ([Li et al., 2020](https://arxiv.org/abs/1911.10742)) |
| Average utterance length | 11.13 words | Primary paper ([Li et al., 2020](https://arxiv.org/abs/1911.10742)) |
| Users identifying the attacker | 172 / 220 (~78.2%) | Primary paper ([Li et al., 2020](https://arxiv.org/abs/1911.10742)) |
| On-task intents (ANTISCAM) | 3 | Primary paper ([Li et al., 2020](https://arxiv.org/abs/1911.10742)) |
| Off-task intents (shared across tasks) | 12 (6 general + 6 social) | Primary paper ([Li et al., 2020](https://arxiv.org/abs/1911.10742)) |
| Semantic slots (ANTISCAM) | 13 | Primary paper ([Li et al., 2020](https://arxiv.org/abs/1911.10742)) |
| Annotation quality (weighted kappa) | 0.874 | Primary paper ([Li et al., 2020](https://arxiv.org/abs/1911.10742)) |

## An Important Discrepancy: 220 Versus 320 Dialogs

A third-party research note describing the same paper reports that "the dataset contains 320 human-human dialogs" and repeats this total three additional times, including in a summary paragraph ([Third-party research note](document_2.txt)). That same note also states that "172 out of 320 users successfully identified their partner as an attacker" ([Third-party research note](document_2.txt)).

This conflicts directly with the primary source. The paper states, in two separate locations, that 220 dialogs were collected and that "172 out of 220 users successfully identified their partner as an attacker" ([Li et al., 2020](https://arxiv.org/abs/1911.10742)). My assessment, based on the relative reliability of the sources, is that **220 is the accurate figure and the 320 figure in the secondary note is erroneous**. Three reasons support this conclusion:

1. **Primary versus secondary sourcing.** The paper is the originating document for the dataset; the research note is a third-party summary ([Li et al., 2020](https://arxiv.org/abs/1911.10742); [Third-party research note](document_2.txt)).
2. **Internal consistency of the paper.** The 220 figure appears both in the main dataset description and in the appendix collection setting, alongside the 12.45-turn and 11.13-word averages ([Li et al., 2020](https://arxiv.org/abs/1911.10742)).
3. **Internal consistency of the note's other claims.** The note's annotation statistics (100 dialogs, 3,044 sentences, 12.45 turns, 11.13 words) exactly match the paper, suggesting the note's error is localized to the total dialog count ([Third-party research note](document_2.txt); [Li et al., 2020](https://arxiv.org/abs/1911.10742)).

Notably, the note never explains where 320 would come from — the paper contains no such figure anywhere ([Third-party research note](document_2.txt)). For the remainder of this report, the primary source's figure of **220 dialogs** is treated as authoritative, with the discrepancy flagged wherever the note is cited.

## Derived Aggregate Estimates of Corpus Size

Neither source reports total turn counts or total word counts for the corpus. However, using the reported averages, approximate aggregates can be derived. These are estimates, not reported figures, and should be treated as such.

- **Estimated total turns:** 220 dialogs × 12.45 turns ≈ **2,739 turns** (derived from [Li et al., 2020](https://arxiv.org/abs/1911.10742)).
- **Estimated total words:** 2,739 turns × 11.13 words ≈ **30,485 words** (derived from [Li et al., 2020](https://arxiv.org/abs/1911.10742)).
- **Sentences per annotated dialog:** 3,044 sentences ÷ 100 dialogs ≈ **30.44 sentences per dialog** (derived from [Li et al., 2020](https://arxiv.org/abs/1911.10742)).
- **Sentences per turn in the annotated subset:** ≈30.44 sentences ÷ 12.45 turns ≈ **2.4 sentences per turn** (derived from [Li et al., 2020](https://arxiv.org/abs/1911.10742)).

These derived figures indicate that the annotated 100-dialog subset alone contains on the order of 3,000 sentences, while the full 220-dialog corpus likely contains roughly 6,700 sentences if the annotated subset's sentence density holds — though the paper does not report sentence counts for the unannotated 120 dialogs, so this extrapolation is speculative ([Li et al., 2020](https://arxiv.org/abs/1911.10742)).

The data splits further define the working size of the dataset: when fine-tuning on ANTISCAM and PERSUASIONFORGOOD, the authors use 80% of data for training, 10% for validation, and 10% for testing ([Li et al., 2020](https://arxiv.org/abs/1911.10742)). Applied to 220 dialogs, this implies approximately **176 training dialogs, 22 validation dialogs, and 22 test dialogs** (derived from [Li et al., 2020](https://arxiv.org/abs/1911.10742)).

| Derived Aggregate | Estimate | Basis |
|---|---|---|
| Total turns (full corpus) | ≈2,739 | 220 × 12.45 ([Li et al., 2020](https://arxiv.org/abs/1911.10742)) |
| Total words (full corpus) | ≈30,485 | 2,739 × 11.13 ([Li et al., 2020](https://arxiv.org/abs/1911.10742)) |
| Sentences per annotated dialog | ≈30.4 | 3,044 ÷ 100 ([Li et al., 2020](https://arxiv.org/abs/1911.10742)) |
| Training split dialogs | ≈176 | 80% of 220 ([Li et al., 2020](https://arxiv.org/abs/1911.10742)) |
| Validation split dialogs | ≈22 | 10% of 220 ([Li et al., 2020](https://arxiv.org/abs/1911.10742)) |
| Test split dialogs | ≈22 | 10% of 220 ([Li et al., 2020](https://arxiv.org/abs/1911.10742)) |

## Size in Terms of Annotation Granularity

A distinguishing feature of ANTISCAM is the depth of its annotation relative to its raw dialog count. The authors designed a hierarchical intent annotation scheme that separates on-task and off-task information ([Li et al., 2020](https://arxiv.org/abs/1911.10742)). For ANTISCAM specifically, three on-task intents were defined — *elicitation*, *providing-information*, and *refusal* — because the task focuses on "understanding and reacting towards elicitations" ([Li et al., 2020](https://arxiv.org/abs/1911.10742)). The off-task categories are shared across non-collaborative tasks and comprise six general intents (open-question, yes_no-question, positive_answer, negative_answer, responsive_statement, and nonresponsive_statement) plus six social intents (greeting, closing, apology, thanking, respond_to_thank, and hold) ([Li et al., 2020](https://arxiv.org/abs/1911.10742)).

In addition, the paper identifies **13 main semantic slots** in the anti-scam task, including order_detail, order-update, payment, name, identity, address, phone_num, card_info, card_num, card_cvs, account_detail, card_date, and others ([Li et al., 2020](https://arxiv.org/abs/1911.10742)). Each sentence — not merely each turn — was segmented and annotated, meaning the annotation volume is considerably larger than the dialog count alone would suggest ([Li et al., 2020](https://arxiv.org/abs/1911.10742)).

The paper also reports distributional facts that quantify the off-task content: users produced more refusals than attackers (74 vs. 19), more open questions (173 vs. 54), and more yes/no questions (165 vs. 117), while both roles contributed substantial social content (292 attacker sentences and 252 user sentences) ([Li et al., 2020](https://arxiv.org/abs/1911.10742)). These counts confirm that ANTISCAM contains a "vast amount of off-task content," which the authors argue justifies the hierarchical annotation design ([Li et al., 2020](https://arxiv.org/abs/1911.10742)).

## Comparative Scale: ANTISCAM Versus PERSUASIONFORGOOD

Size is best interpreted in context. The paper evaluates the same model on two non-collaborative datasets: ANTISCAM and PERSUASIONFORGOOD ([Li et al., 2020](https://arxiv.org/abs/1911.10742)). PERSUASIONFORGOOD, collected by Wang et al. (2019), consists of **1,017 dialogs**, of which **300 are annotated with dialog acts**, with an average conversation length of 10.43 and a vocabulary size of 8,141 ([Li et al., 2020](https://arxiv.org/abs/1911.10742)).

| Dataset | Dialogs | Annotated Dialogs | Avg. Conversation Length | Vocabulary |
|---|---|---|---|---|
| ANTISCAM | 220 | 100 | 12.45 turns | Not reported |
| PERSUASIONFORGOOD | 1,017 | 300 | 10.43 turns | 8,141 |

Sources: ([Li et al., 2020](https://arxiv.org/abs/1911.10742)).

This comparison shows that ANTISCAM is substantially smaller than PERSUASIONFORGOOD in dialog count — roughly **22% of its size** (derived from [Li et al., 2020](https://arxiv.org/abs/1911.10742)) — but has slightly longer average conversations (12.45 versus 10.43 turns) and a proportionally deeper annotation scheme tailored to the anti-scam domain ([Li et al., 2020](https://arxiv.org/abs/1911.10742)). The authors acknowledge the scarcity of non-collaborative datasets explicitly, framing ANTISCAM as a contribution intended to address that gap ([Li et al., 2020](https://arxiv.org/abs/1911.10742)).

## How the Data Was Collected and Why the Corpus Is Modest in Size

The collection protocol helps explain the dataset's scale. The authors posted a role-playing task on Amazon Mechanical Turk, randomly pairing two workers: one assigned the role of attacker (trying to elicit user information) and one assigned the role of an everyday user protecting their information ([Li et al., 2020](https://arxiv.org/abs/1911.10742)). Both received specific personal data and detailed instructions; attackers were additionally "trained" to pretend to be Amazon customer service agents, and workers could not see their partners' instructions ([Li et al., 2020](https://arxiv.org/abs/1911.10742)).

A key constraint: "Each worker can only participate once to prevent workers from knowing their partner's information and goals in advance" ([Li et al., 2020](https://arxiv.org/abs/1911.10742)). This design choice — combined with bonuses paid to users for detecting attackers and to attackers for eliciting correct information — plausibly limited the achievable sample size, resulting in the 220-dialog corpus ([Li et al., 2020](https://arxiv.org/abs/1911.10742)).

## A Related but Distinct Figure: The Human Evaluation Set

It is important not to confuse the ANTISCAM corpus with the human evaluation data reported in the same paper. For evaluation, the authors recruited **15 college-student volunteers** who role-played attackers; each interacted with all five models (TransferTransfo, Hybrid, MISSA, MISSA-sel, and MISSA-con) at least three times, yielding **225 dialogs** in total, with each model receiving 45 human ratings ([Li et al., 2020](https://arxiv.org/abs/1911.10742)). These 225 dialogs are evaluation artifacts, not part of the 220-dialog training corpus, and should not be counted toward the dataset's size ([Li et al., 2020](https://arxiv.org/abs/1911.10742)).

## Conclusion and Assessment

Based on the primary source, the ANTISCAM dataset is **220 human-human dialogs in size**, with an average of **12.45 turns per conversation** and **11.13 words per utterance**, of which a subset of **100 dialogs containing 3,044 sentences** was manually annotated by two expert linguistically trained annotators at a weighted kappa of 0.874 ([Li et al., 2020](https://arxiv.org/abs/1911.10742)). Derived aggregates place the full corpus at approximately **2,739 turns and 30,485 words**, though these are calculations rather than reported figures ([Li et al., 2020](https://arxiv.org/abs/1911.10742)).

My concrete position on the discrepancy is unambiguous: the correct total is **220**, not the 320 reported in the third-party note ([Third-party research note](document_2.txt)). The paper states 220 twice, in the dataset description and in the appendix, and the "172 out of 220" success figure is internally consistent with it ([Li et al., 2020](https://arxiv.org/abs/1911.10742)). The secondary note's "320" figure appears in four places but is never corroborated by the paper, and the note is otherwise accurate on annotation statistics — suggesting a localized transcription or arithmetic error rather than a deliberate alternative count ([Third-party research note](document_2.txt)).

In comparative terms, ANTISCAM is a small-to-moderate corpus: about one-fifth the dialog count of PERSUASIONFORGOOD (1,017 dialogs, 300 annotated), but with longer average conversations and a finer-grained hierarchical annotation scheme spanning 3 on-task intents, 12 shared off-task intents, and 13 semantic slots ([Li et al., 2020](https://arxiv.org/abs/1911.10742)). Its size reflects its purpose: a carefully controlled, single-participation role-play study designed to produce high-quality, deeply annotated non-collaborative dialogs rather than a large-scale corpus ([Li et al., 2020](https://arxiv.org/abs/1911.10742)).

## References

Li, Y., Qian, K., Shi, W., & Yu, Z. (2020). *End-to-end trainable non-collaborative dialog system* (arXiv:1911.10742). https://arxiv.org/abs/1911.10742

Third-party research note: *End-to-end trainable non-collaborative dialog system* (document_2.txt).

Source documents used: document_1.txt; document_2.txt.