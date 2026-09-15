# How Big Is the AntiScam Dataset? A Detailed Size Assessment

## Introduction and Scope of the Query

The AntiScam dataset is a human–human dialog corpus introduced by Li, Qian, Shi, and Yu (2019) to support research on non-collaborative dialog systems, in which the interacting parties do not share a common goal ([Li et al., 2019](https://arxiv.org/abs/1911.10742)). The question “how big is the AntiScam dataset?” appears simple, but it cannot be answered adequately with a single number. A dialog corpus has several distinct size dimensions: the number of conversations, the number of annotated conversations, the number of annotated sentences, the average conversation length in turns, the average utterance length in words, the number of label categories, and the scale of the auxiliary evaluation data generated from it. This report examines each of these dimensions, adjudicates a discrepancy between the primary paper and a secondary research note, and states a concrete assessment of the corpus size.

## Source Provenance and Reliability Assessment

Two sources are available for this assessment. The first is the original paper, “End-to-End Trainable Non-Collaborative Dialog System,” by Yu Li, Kun Qian, Weiyan Shi, and Zhou Yu of the University of California, Davis, identified as arXiv:1911.10742 and reproduced here as document_1.txt ([Li et al., 2019](https://arxiv.org/abs/1911.10742)). This is the primary source: it is the paper that proposes the dataset, describes its collection procedure, and reports its statistics. The second is a third-party research note, reproduced here as document_2.txt, that summarizes the AntiScam dataset’s size and annotation statistics ([Third-party research note, n.d.](document_2.txt)).

For any factual claim about a dataset, the paper that created the dataset must take precedence over a derivative summary, because the creators directly controlled the collection process and reported the resulting counts. The third-party note is useful as corroboration for figures on which it agrees with the primary source, but it loses evidentiary weight where it conflicts with the primary source. As documented below, such a conflict exists, and it concerns the headline number.

## Headline Size: The Conversation Count

### The 220-Dialog Figure in the Primary Source

The primary source states the AntiScam corpus size consistently and repeatedly. In its dataset description, the paper reports: “We collected 220 human-human dialogs” ([Li et al., 2019](https://arxiv.org/abs/1911.10742)). The same figure is restated in the appendix section describing the anti-scam collection setting: “We collected 220 human-human dialogs. The average conversation length is 12.45 turns and the average utterance length is 11.13 words” ([Li et al., 2019](https://arxiv.org/abs/1911.10742)). The attacker-identification result is also anchored to this number: “Only 172 out of 220 users successfully identified their partner as an attacker, suggesting that the attackers are well trained and not too easily identifiable” ([Li et al., 2019](https://arxiv.org/abs/1911.10742)). The number 220 therefore appears in at least three separate locations in the primary document, each tied to a different descriptive claim, which makes it the internally consistent value.

### The 320-Dialog Claim in the Secondary Note

The third-party research note asserts a different total: “The dataset contains 320 human-human dialogs” ([Third-party research note, n.d.](document_2.txt)). It repeats this figure several times, including in the statement that “172 out of 320 users successfully identified their partner as an attacker,” and in its summary paragraph ([Third-party research note, n.d.](document_2.txt)). Notably, the note never explains where the additional 100 dialogs would have come from, nor does it reconcile the total with the paper’s own narrative.

### Adjudication Between the Two Figures

In my assessment, the defensible size of the AntiScam corpus is **220 human–human dialogs**, not 320. Three considerations support this conclusion. First, the primary source is the dataset creator’s own report and states 220 in multiple, mutually reinforcing passages ([Li et al., 2019](https://arxiv.org/abs/1911.10742)). Second, the secondary note’s figure of 320 is internally inconsistent with the very statistic it reports alongside it: the paper’s identification rate is 172 out of 220, whereas the note converts it into 172 out of 320 without any supporting evidence from the paper ([Third-party research note, n.d.](document_2.txt)). Third, the third-party note itself concedes that its numbers are drawn from “the paper” ([Third-party research note, n.d.](document_2.txt)); since the paper does not contain the number 320, the note’s total is unsupported by its own cited origin. A reader should therefore treat 320 as an unverified secondary transcription error and adopt 220 as the reliable corpus size.

## Annotation Footprint

The full collection and the annotated subset must be distinguished, because the AntiScam corpus was not annotated in its entirety. The primary source states that “two expert annotators who have linguistic training” annotated “3,044 sentences in 100 dialogs,” achieving a “0.874 averaged weighted kappa value” ([Li et al., 2019](https://arxiv.org/abs/1911.10742)). The third-party note agrees on exactly these figures: a subset of 100 dialogs and 3,044 sentences was manually annotated, by two expert annotators with linguistic training ([Third-party research note, n.d.](document_2.txt)). This is the strongest point of agreement between the two sources and the most reliable statement about the annotation scale.

A straightforward derived estimate indicates that the annotated subset averages approximately 30.4 sentences per dialog (3,044 ÷ 100), based on the reported counts ([Li et al., 2019](https://arxiv.org/abs/1911.10742)). The annotation level of granularity is the sentence rather than the turn: the paper explicitly notes that, following prior work, “we segment each conversation turn into single sentences and then annotate each sentence rather than turns” ([Li et al., 2019](https://arxiv.org/abs/1911.10742)). The measured inter-annotator agreement of 0.874 weighted kappa suggests that the annotation scheme was applied with substantial consistency.

## Conversational Scale: Turns, Utterances, and Words

Beyond raw dialog counts, the primary source reports two averages that describe the conversational scale of the corpus: an average conversation length of 12.45 turns and an average utterance length of 11.13 words ([Li et al., 2019](https://arxiv.org/abs/1911.10742)). The third-party note reproduces both averages and adds the clarification that “these averages describe the full AntiScam corpus” ([Third-party research note, n.d.](document_2.txt)).

Applying these reported averages arithmetically yields approximate upper-bound estimates of the corpus’s textual footprint: roughly 2,739 conversational turns (220 × 12.45) and roughly 30,500 words (220 × 12.45 × 11.13), assuming the turn and word averages are computed over the same 220 dialogs ([Li et al., 2019](https://arxiv.org/abs/1911.10742)). These derived figures should be treated as approximations rather than reported statistics, but they help place the corpus in context: AntiScam is a modestly sized, specialized corpus rather than a large-scale dataset.

The corpus is also balanced with respect to role: each dialog pairs a “attacker” role, instructed to elicit personal information while impersonating an Amazon customer service agent, with a “user” role instructed to protect personal information and, once the attacker is detected, to prolong the conversation and elicit the attacker’s information in return ([Li et al., 2019](https://arxiv.org/abs/1911.10742)). Each worker could participate only once, preventing prior knowledge of the partner’s instructions or goals ([Li et al., 2019](https://arxiv.org/abs/1911.10742)).

## Label Space as a Dimension of Size

The size of AntiScam is also reflected in its annotation label inventory rather than in raw dialog counts. The paper defines a hierarchical intent scheme in which on-task intents are task-specific and off-task intents are universal across non-collaborative tasks ([Li et al., 2019](https://arxiv.org/abs/1911.10742)). For AntiScam, three on-task intents are defined—*elicitation*, *providing_information*, and *refusal*—because the task “focuses on understanding and reacting towards elicitations” ([Li et al., 2019](https://arxiv.org/abs/1911.10742)). The off-task layer comprises twelve categories: six general intents (*open_question*, *yes_no_question*, *positive_answer*, *negative_answer*, *responsive_statement*, and *nonresponsive_statement*) and six social intents (*greeting*, *closing*, *apology*, *thanking*, *respond_to_thank*, and *hold*) ([Li et al., 2019](https://arxiv.org/abs/1911.10742)). In addition, the paper identifies “13 main semantic slots in the anti-scam task, for example, credit card numbers,” including labels such as *order_detail*, *order_update*, *payment*, *name*, *identity*, *address*, *phone_num*, *card_info*, *card_num*, *card_cvs*, *card_date*, *account_detail*, and *others* ([Li et al., 2019](https://arxiv.org/abs/1911.10742)).

The resulting label space—three on-task intents, twelve off-task intents, and thirteen semantic slots—constitutes a substantial annotation burden relative to the corpus’s 100 annotated dialogs, and it explains why only a subset of the collection was annotated ([Li et al., 2019](https://arxiv.org/abs/1911.10742)).

## Intent Distributions Within the Corpus

The published intent counts give additional texture to the corpus size. Users produced far more *refusal* labels than attackers (74 versus 19), reflecting the instruction to withhold information after detecting the attacker ([Li et al., 2019](https://arxiv.org/abs/1911.10742)). Users also asked more *open_questions* (173 versus 54) and *yes_no_questions* (165 versus 117), consistent with the instruction to prolong the conversation ([Li et al., 2019](https://arxiv.org/abs/1911.10742)). Social content was abundant for both roles, with 292 social-intent sentences from attackers and 252 from users, which the authors use to argue that social intent sentences are important for maintaining conversation ([Li et al., 2019](https://arxiv.org/abs/1911.10742)).

## Comparative Size Context

Comparing AntiScam with the PersuasionForGood dataset, also used in the paper, places its size in perspective. PersuasionForGood consists of 1,017 dialogs, of which 300 are annotated with dialog acts, with an average conversation length of 10.43 and a vocabulary size of 8,141 ([Li et al., 2019](https://arxiv.org/abs/1911.10742)). AntiScam is therefore roughly one-fifth the total dialog count of PersuasionForGood and roughly one-third its annotated dialog count, but its average conversation length is slightly longer (12.45 versus 10.43 turns) ([Li et al., 2019](https://arxiv.org/abs/1911.10742)).

## Consolidated Size Summary

The table below consolidates the primary source’s reported size dimensions, with the conflicting secondary claim shown separately.

| Size dimension | Reported value (primary source) | Secondary-note claim |
|---|---|---|
| Total human–human dialogs | 220 ([Li et al., 2019](https://arxiv.org/abs/1911.10742)) | 320 ([Third-party research note, n.d.](document_2.txt)) |
| Manually annotated dialogs | 100 ([Li et al., 2019](https://arxiv.org/abs/1911.10742)) | 100 ([Third-party research note, n.d.](document_2.txt)) |
| Manually annotated sentences | 3,044 ([Li et al., 2019](https://arxiv.org/abs/1911.10742)) | 3,044 ([Third-party research note, n.d.](document_2.txt)) |
| Average conversation length | 12.45 turns ([Li et al., 2019](https://arxiv.org/abs/1911.10742)) | 12.45 turns ([Third-party research note, n.d.](document_2.txt)) |
| Average utterance length | 11.13 words ([Li et al., 2019](https://arxiv.org/abs/1911.10742)) | 11.13 words ([Third-party research note, n.d.](document_2.txt)) |
| Users identifying the attacker | 172 of 220 ([Li et al., 2019](https://arxiv.org/abs/1911.10742)) | 172 of 320 ([Third-party research note, n.d.](document_2.txt)) |
| Annotators | 2 expert linguistic annotators ([Li et al., 2019](https://arxiv.org/abs/1911.10742)) | 2 expert linguistic annotators ([Third-party research note, n.d.](document_2.txt)) |
| Inter-annotator agreement | 0.874 weighted kappa ([Li et al., 2019](https://arxiv.org/abs/1911.10742)) | Not stated ([Third-party research note, n.d.](document_2.txt)) |
| On-task intent labels | 3 ([Li et al., 2019](https://arxiv.org/abs/1911.10742)) | Not stated ([Third-party research note, n.d.](document_2.txt)) |
| Off-task intent labels | 12 (6 general + 6 social) ([Li et al., 2019](https://arxiv.org/abs/1911.10742)) | Not stated ([Third-party research note, n.d.](document_2.txt)) |
| Semantic slot labels | 13 ([Li et al., 2019](https://arxiv.org/abs/1911.10742)) | Not stated ([Third-party research note, n.d.](document_2.txt)) |

## Auxiliary and Downstream Data Scale

Two further quantities are sometimes conflated with the corpus size and should be separated from it. First, the model experiments used an 80%/10%/10% training, validation, and test split for both AntiScam and PersuasionForGood ([Li et al., 2019](https://arxiv.org/abs/1911.10742)). Applied to 220 dialogs, that split implies approximately 176 training dialogs, 22 validation dialogs, and 22 test dialogs ([Li et al., 2019](https://arxiv.org/abs/1911.10742)). Second, the human evaluation was conducted with 15 college-student volunteers, each of whom interacted with all five models at least three times, producing a total of 225 human–system dialogs and 45 human ratings per model ([Li et al., 2019](https://arxiv.org/abs/1911.10742)). These 225 evaluation dialogs are a research artifact generated during testing, not part of the AntiScam corpus itself.

The dialog-length results from that evaluation provide a useful sense of scale in deployment: MISSA maintained conversations of 14.9 turns on average, compared with 8.5 turns for TransferTransfo and 8.2 turns for the hybrid baseline, while MISSA-sel averaged 9.9 turns and MISSA-con averaged 14.8 turns ([Li et al., 2019](https://arxiv.org/abs/1911.10742)). The corresponding task-success scores were 1.294 for MISSA, 1.341 for MISSA-con, 1.025 for TransferTransfo, 1.000 for MISSA-sel, and 0.975 for the hybrid system ([Li et al., 2019](https://arxiv.org/abs/1911.10742)).

## Interpretation and Limitations

In my assessment, the most accurate single-sentence answer is that the AntiScam dataset contains 220 human–human anti-scam dialogs collected on Amazon Mechanical Turk, of which 100 dialogs and 3,044 sentences were manually annotated by two expert annotators, with an average conversation length of 12.45 turns and an average utterance length of 11.13 words ([Li et al., 2019](https://arxiv.org/abs/1911.10742)). The secondary claim of 320 dialogs is not supported by the primary paper and is contradicted by the paper’s own identification statistic of 172 out of 220 ([Third-party research note, n.d.](document_2.txt)).

Several limitations should be acknowledged. The published averages do not include the total word count or total turn count of the corpus, so the derived figures of roughly 2,739 turns and roughly 30,500 words are approximations rather than reported values ([Li et al., 2019](https://arxiv.org/abs/1911.10742)). The paper also does not report a vocabulary size for AntiScam, although it does so for PersuasionForGood, which prevents a direct lexical-size comparison ([Li et al., 2019](https://arxiv.org/abs/1911.10742)). Finally, only 100 of the 220 dialogs carry full intent and slot annotation, so the label-rich portion of the corpus is smaller than the raw collection size ([Li et al., 2019](https://arxiv.org/abs/1911.10742)).

## Conclusion

The AntiScam dataset is a small-to-medium, richly annotated corpus rather than a large-scale resource. Its headline size is 220 human–human anti-scam dialogs, gathered through a role-playing Amazon customer service scam scenario on Amazon Mechanical Turk ([Li et al., 2019](https://arxiv.org/abs/1911.10742)). Its annotated core is 100 dialogs and 3,044 sentences, labeled by two linguistic experts at 0.874 weighted kappa agreement, using 3 on-task intents, 12 off-task intents, and 13 semantic slots ([Li et al., 2019](https://arxiv.org/abs/1911.10742)). Conversations average 12.45 turns and utterances 11.13 words ([Li et al., 2019](https://arxiv.org/abs/1911.10742)). The code and data were released publicly at the project’s GitLab repository ([Li et al., 2019](https://arxiv.org/abs/1911.10742)). Where the secondary note claims 320 dialogs, the weight of the primary evidence points to 220, and the 320 figure should be regarded as an unverified transcription error ([Third-party research note, n.d.](document_2.txt)).

## References

Li, Y., Qian, K., Shi, W., & Yu, Z. (2019). *End-to-end trainable non-collaborative dialog system* [document_1.txt] (arXiv:1911.10742). University of California, Davis. https://arxiv.org/abs/1911.10742

Third-party research note: End-to-end trainable non-collaborative dialog system [document_2.txt]. (n.d.).