# How Big Is the AntiScam Dataset? A Detailed Assessment

## Executive Summary

The AntiScam dataset is a corpus of human–human anti-scam dialogs created to study human elicitation strategies in non-collaborative dialog settings ([Li et al., 2019](https://arxiv.org/abs/1911.10742)). The primary source document reports that the corpus consists of **220 human–human dialogs**, collected through a role-playing Amazon customer-service scam scenario posted on Amazon Mechanical Turk ([Li et al., 2019](https://arxiv.org/abs/1911.10742)). A secondary third-party research note instead reports **320 human–human dialogs** for the same corpus ([Research Note, 2026](https://gitlab.com/ucdavisnlp/antiscam)).

After weighing both sources, the most defensible answer to the question "How big is the AntiScam dataset?" is **220 human–human dialogs in total, of which 100 dialogs (3,044 sentences) were manually annotated**. The 320-dialog figure appears to be an error introduced in the secondary note, because it contradicts the primary source on two separate, mutually dependent statistics, as detailed below.

## Background on the AntiScam Corpus

### Purpose and Design

AntiScam was built to enrich the relatively sparse supply of publicly available non-collaborative task datasets ([Li et al., 2019](https://arxiv.org/abs/1911.10742)). Unlike collaborative task-oriented dialog (for example, restaurant reservations or bus timetable retrieval), non-collaborative tasks such as negotiation, persuasion, and scam deterrence involve users and systems that do not share a common goal ([Li et al., 2019](https://arxiv.org/abs/1911.10742)). The dataset was therefore designed to interleave on-task and off-task content within conversations, precisely because earlier work struggled to disentangle and measure those two content types ([Li et al., 2019](https://arxiv.org/abs/1911.10742)).

### Collection Procedure

To build the corpus, the authors "created a corpus of human-human anti-scam dialogs in order to learn human elicitation strategies" and chose "a popular Amazon customer service scam scenario to collect dialogs between users and attackers who aim to collect users information" ([Li et al., 2019](https://arxiv.org/abs/1911.10742)). The task was posted on Amazon Mechanical Turk and produced a typed conversation dataset named AntiScam ([Li et al., 2019](https://arxiv.org/abs/1911.10742)).

## Headline Size: The Number of Dialogs

### What the Primary Source Reports

The paper containing the dataset description states plainly: "We collected 2 2 0 human-human dialogs" ([Li et al., 2019](https://arxiv.org/abs/1911.10742)). It further reports that "the average conversation length is 1 2.4 5 turns and the average utterance length is 1 1.1 3 words," and that "only 1 7 2 out of 2 2 0 users successfully identified their partner as an attacker" ([Li et al., 2019](https://arxiv.org/abs/1911.10742)). The figure of 220 therefore appears twice in the same passage — once as the raw count and once as the denominator of the attacker-detection rate — which strengthens its reliability.

### What the Secondary Source Reports

A third-party research note addressing the same key questions ("AntiScam dataset non-collaborative dialog size," "AntiScam corpus number of dialogs," and "AntiScam dataset annotation statistics") states that "the dataset contains 320 human-human dialogs" and repeats that "the total dataset comprises 320 human-human dialogs" ([Research Note, 2026](https://gitlab.com/ucdavisnlp/antiscam)). It also reports "172 out of 320 users successfully identified their partner as an attacker" ([Research Note, 2026](https://gitlab.com/ucdavisnlp/antiscam)).

### Comparing the Two Accounts

| Quantity | Primary Source (Li et al., 2019) | Secondary Research Note (2026) | Assessment |
|---|---|---|---|
| Total human–human dialogs | 220 ([Li et al., 2019](https://arxiv.org/abs/1911.10742)) | 320 ([Research Note, 2026](https://gitlab.com/ucdavisnlp/antiscam)) | Primary source more credible |
| Annotated dialogs | 100 ([Li et al., 2019](https://arxiv.org/abs/1911.10742)) | 100 ([Research Note, 2026](https://gitlab.com/ucdavisnlp/antiscam)) | Both agree |
| Annotated sentences | 3,044 ([Li et al., 2019](https://arxiv.org/abs/1911.10742)) | 3,044 ([Research Note, 2026](https://gitlab.com/ucdavisnlp/antiscam)) | Both agree |
| Users who detected the attacker | 172 of 220 ([Li et al., 2019](https://arxiv.org/abs/1911.10742)) | 172 of 320 ([Research Note, 2026](https://gitlab.com/ucdavisnlp/antiscam)) | Numerator identical; denominator disputed |
| Average conversation length | 12.45 turns ([Li et al., 2019](https://arxiv.org/abs/1911.10742)) | 12.45 turns ([Research Note, 2026](https://gitlab.com/ucdavisnlp/antiscam)) | Both agree |
| Average utterance length | 11.13 words ([Li et al., 2019](https://arxiv.org/abs/1911.10742)) | 11.13 words ([Research Note, 2026](https://gitlab.com/ucdavisnlp/antiscam)) | Both agree |

The two accounts agree on everything except the total dialog count and the denominator of the detection statistic. That pattern is diagnostic: the secondary note preserved the numerator (172) but altered the denominator (from 220 to 320), which produces a materially different detection rate. Under the primary source, the detection rate is 172 ÷ 220 ≈ **78.2%**; under the secondary note, it is 172 ÷ 320 ≈ **53.8%**. The primary source's framing — that "attackers are well trained and not too easily identifiable" — is consistent with a high detection rate of roughly 78%, because a majority of users still succeeded even though the attackers were convincing ([Li et al., 2019](https://arxiv.org/abs/1911.10742)). A 53.8% rate would be closer to chance and would undercut the stated interpretation. On the balance of evidence, **220 dialogs is the figure that should be reported**, with the 320 figure flagged as an unresolved discrepancy in the secondary literature ([Research Note, 2026](https://gitlab.com/ucdavisnlp/antiscam)).

## Size Beyond the Dialog Count

Dialog count alone understates the dataset's scale, because AntiScam is annotated at the sentence level rather than the turn level ([Li et al., 2019](https://arxiv.org/abs/1911.10742)).

### Annotated Subset

Two expert annotators with linguistic training annotated **3,044 sentences across 100 dialogs**, achieving an averaged weighted kappa value of **0.874** ([Li et al., 2019](https://arxiv.org/abs/1911.10742)). This yields an average of approximately 30.4 annotated sentences per annotated dialog (3,044 ÷ 100), which is a useful derived indicator of annotation density.

### Derived Corpus-Level Estimates

Based on the reported averages for the full corpus, the following scale estimates can be derived arithmetically. These are calculated values, not figures stated directly in the source:

| Derived Quantity | Calculation | Estimated Value |
|---|---|---|
| Total conversation turns | 220 dialogs × 12.45 turns | ≈ 2,739 turns |
| Total words | ≈ 2,739 turns × 11.13 words | ≈ 30,485 words |
| Total unique participants | 220 dialogs × 2 paired workers | ≈ 440 workers |

The participant estimate follows from the collection design: the authors "randomly pair two workers," assigning one the attacker role and the other the everyday-user role, and "each worker can only participate once" ([Li et al., 2019](https://arxiv.org/abs/1911.10742)). With 220 dialogs and strict one-time participation, the corpus would represent approximately 440 distinct crowd workers.

### Social versus Task Content

Within the annotated data, the authors report "a massive amount of social content (2 9 2 in total and 2 5 2 in total)" contributed by attackers and users respectively, which they cite as evidence of the importance of social-intent sentences for maintaining conversation ([Li et al., 2019](https://arxiv.org/abs/1911.10742)). They also report an asymmetric distribution of intents between roles: users produced more refusals (74 versus 19), more open questions (173 versus 54), and more yes/no questions (165 versus 117) than attackers, reflecting the defensive posture of users who had detected the scam ([Li et al., 2019](https://arxiv.org/abs/1911.10742)).

## Annotation Structure and Label Space

The size of the dataset is best understood alongside the richness of its annotation scheme, which directly shaped the corpus's dimensions.

### Hierarchical Intent Annotation

The authors designed a hierarchical intent annotation scheme that separates on-task from off-task intents, on the rationale that on-task intents are task-specific while off-task content is "too general to design task-specific intents" ([Li et al., 2019](https://arxiv.org/abs/1911.10742)). For AntiScam, three on-task intents were defined — elicitation, providing_information, and refusal — while the off-task layer comprises six general intents (open_question, yes_no_question, positive_answer, negative_answer, responsive_statement, nonresponsive_statement) and six social intents (greeting, closing, apology, thanking, respond_to_thank, hold) ([Li et al., 2019](https://arxiv.org/abs/1911.10742)).

### Semantic Slot Annotation

In addition, the authors "identify l 3 main semantic slots in the anti-scam task," including order_detail, order_update, payment, name, identity, address, phone_num, card_info, card_num, card_cvs, card_date, account_detail, and others ([Li et al., 2019](https://arxiv.org/abs/1911.10742)). This slot scheme required segmenting each conversation turn into single sentences and annotating each sentence rather than each turn — a design choice that multiplies the unit of annotation and explains why 100 dialogs yield 3,044 annotated units ([Li et al., 2019](https://arxiv.org/abs/1911.10742)).

## Comparative Scale

Placing AntiScam's 220 dialogs in context helps clarify whether it should be considered large:

| Dataset | Total Dialogs | Annotated Dialogs | Average Dialog Length |
|---|---|---|---|
| AntiScam | 220 ([Li et al., 2019](https://arxiv.org/abs/1911.10742)) | 100 ([Li et al., 2019](https://arxiv.org/abs/1911.10742)) | 12.45 turns ([Li et al., 2019](https://arxiv.org/abs/1911.10742)) |
| PersuasionForGood | 1,017 ([Li et al., 2019](https://arxiv.org/abs/1911.10742)) | 300 ([Li et al., 2019](https://arxiv.org/abs/1911.10742)) | 10.43 turns ([Li et al., 2019](https://arxiv.org/abs/1911.10742)) |

AntiScam is substantially smaller than PersuasionForGood in raw dialog count and lacks that dataset's 8,141-token vocabulary scale ([Li et al., 2019](https://arxiv.org/abs/1911.10742)). The authors acknowledge this limitation explicitly, noting that non-collaborative tasks "are still relatively new to the study of dialog systems" and that "there are insufficiently many meaningful datasets for evaluation," framing AntiScam as "a valuable example" rather than a large-scale resource ([Li et al., 2019](https://arxiv.org/abs/1911.10742)). Importantly, the 220-dialog corpus was divided into 80% training, 10% validation, and 10% testing splits for model training ([Li et al., 2019](https://arxiv.org/abs/1911.10742)). The dataset and code were publicly released ([Li et al., 2019](https://arxiv.org/abs/1911.10742)).

## Evaluation-Scale Resource (Distinct from Dataset Size)

For completeness, the study also generated a separate evaluation resource that should not be confused with the AntiScam dataset itself. Human evaluation involved 15 college-student volunteers who each acted as an attacker and interacted with all five model variants at least three times, producing a total of 225 collected dialogs, with each model receiving 45 human ratings ([Li et al., 2019](https://arxiv.org/abs/1911.10742)). This 225-dialog evaluation set is a by-product of model testing, not part of the 220-dialog AntiScam corpus.

## Limitations of the Available Evidence

Three caveats should accompany any size claim:

1. **Source-text distortion.** The primary source is a machine-extracted document in which numerals are fragmented (for example, "2 2 0," "3,0 4 4," "1 2.4 5"), which introduces some risk of transcription error, though the digit sequence remains unambiguous in context ([Li et al., 2019](https://arxiv.org/abs/1911.10742)).
2. **Unresolved secondary discrepancy.** Only one of the two available sources reports 320 dialogs, and that source is a third-party note rather than the originating publication ([Research Note, 2026](https://gitlab.com/ucdavisnlp/antiscam)).
3. **No independent verification.** Neither provided document supplies a repository manifest, per-split file count, or download log that would allow the 220-versus-320 question to be settled definitively; verification would require inspecting the publicly released data directly ([Li et al., 2019](https://arxiv.org/abs/1911.10742)).

## Conclusion

On the evidence provided, the AntiScam dataset is **small but densely annotated**. Its total size is **220 human–human dialogs**, averaging 12.45 turns and 11.13 words per utterance, of which a **100-dialog subset containing 3,044 sentences** was manually annotated by two linguistic-trained experts at a weighted kappa of 0.874 ([Li et al., 2019](https://arxiv.org/abs/1911.10742)). Derived arithmetic places the full corpus at roughly 2,739 conversation turns, around 30,000 words, and approximately 440 unique crowd workers. The competing figure of 320 dialogs reported in a third-party note is best treated as an error: it preserves the annotated-subset figures exactly while altering only the total count and the denominator of the 172-user detection statistic, producing an internally weaker account ([Research Note, 2026](https://gitlab.com/ucdavisnlp/antiscam)). The honest summary is therefore: **220 dialogs total, 100 annotated, 3,044 annotated sentences — with a documented secondary-source discrepancy of 320 dialogs that should be resolved against the released data before citation.**

## References

Li, Y., Qian, K., Shi, W., & Yu, Z. (2019). *End-to-end trainable non-collaborative dialog system* (arXiv:1911.10742). https://arxiv.org/abs/1911.10742

Research Note. (2026). *Third-party research note: End-to-end trainable non-collaborative dialog system* [Research note on the AntiScam dataset]. https://gitlab.com/ucdavisnlp/antiscam