# How Big Is the AntiScam Dataset?

## Introduction

The AntiScam dataset is a corpus of human–human anti-scam dialogs introduced by Li, Qian, Shi, and Yu (2019) in the paper *End-to-End Trainable Non-Collaborative Dialog System*. The corpus was created to support research on non-collaborative dialog systems, a setting in which the user and the system pursue opposing goals rather than cooperating to complete a shared task ([Li et al., 2019](https://arxiv.org/abs/1911.10742)). AntiScam specifically simulates an Amazon customer-service scam scenario in which one participant plays a trained "attacker" attempting to elicit personal information and the other plays an everyday user who tries to protect that information and, after detecting the attacker, to elicit the attacker's information in return ([Li et al., 2019](https://arxiv.org/abs/1911.10742)).

The question "how big is the AntiScam dataset?" can be answered along several dimensions: the number of dialogs, the average conversation length, the average utterance length, the size of the manually annotated subset, the number of annotated sentences, the number of annotation categories, and the number of participants involved in collection. This report presents each of these dimensions, distinguishes reported values from values that can only be derived, and assesses what the dataset's size implies for its research utility.

## Reported Size Metrics at a Glance

The core quantitative claims about AntiScam appear in the "AntiScam Dataset" subsection of the paper and are repeated in a third-party research note summarizing the same work ([Li et al., 2019](https://arxiv.org/abs/1911.10742); [Third-party research note](https://arxiv.org/abs/1911.10742)). Table 1 consolidates these figures.

**Table 1. Headline size and annotation metrics for the AntiScam corpus.**

| Metric | Reported value |
|---|---|
| Total human–human dialogs collected | 220 |
| Average conversation length | 12.45 turns |
| Average utterance length | 11.13 words |
| Dialogs manually annotated | 100 |
| Sentences manually annotated | 3,044 |
| Expert annotators | 2 (with linguistic training) |
| Inter-annotator agreement | 0.874 averaged weighted kappa |
| Users who identified their partner as an attacker | 172 out of 220 (≈78.2%) |
| Task-specific semantic slots | 13 |
| On-task intent categories (AntiScam) | 3 |
| Off-task intent categories (shared across tasks) | 12 (6 general + 6 social) |

*Source:* ([Li et al., 2019](https://arxiv.org/abs/1911.10742); [Third-party research note](https://arxiv.org/abs/1911.10742)).

## The Headline Figure: 220 Human–Human Dialogs

The single most direct answer to the question is that AntiScam consists of **220 human–human dialogs**. The authors state plainly that they "collected 220 human–human dialogs" after posting a role-playing task on Amazon Mechanical Turk ([Li et al., 2019](https://arxiv.org/abs/1911.10742)). The same figure is reported again in the appendix describing the anti-scam collection setting, where the authors note that each worker could participate only once, "to prevent workers from knowing their partner's information and goals in advance" ([Li et al., 2019](https://arxiv.org/abs/1911.10742)).

Because each dialog involves two workers and each worker participated only once, the 220 dialogs correspond to approximately 440 unique worker sessions. This is a design constraint with consequences for corpus scale: the pool of participant behavior is bounded, and no single worker could contribute multiple dialogs that might have inflated apparent diversity ([Li et al., 2019](https://arxiv.org/abs/1911.10742)). The third-party note confirms that AntiScam "contains 220 human-human dialogs" and that this "corpus serves as the dataset for non-collaborative dialog research in the paper" ([Third-party research note](https://arxiv.org/abs/1911.10742)).

## Conversation and Utterance Length

Beyond the raw count of dialogs, the paper reports two per-dialog length statistics: an **average conversation length of 12.45 turns** and an **average utterance length of 11.13 words** ([Li et al., 2019](https://arxiv.org/abs/1911.10742)). The third-party note explicitly states that "[t]hese averages describe the full AntiScam corpus" — that is, the 12.45-turn and 11.13-word figures characterize all 220 dialogs, not merely the 100-dialog annotated subset ([Third-party research note](https://arxiv.org/abs/1911.10742)).

These two numbers place AntiScam in a relatively short-dialog regime. For comparison, the PersuasionForGood dataset, the other non-collaborative corpus used in the paper, has an average conversation length of 10.43 ([Li et al., 2019](https://arxiv.org/abs/1911.10742)). Non-collaborative anti-scam interactions are therefore comparable in length to persuasion interactions, and both are considerably shorter than the open-domain, multi-session conversations common in social-chat corpora.

## The Annotated Subset: 100 Dialogs and 3,044 Sentences

A crucial distinction when assessing dataset size is that **not all 220 dialogs were annotated**. The paper reports that two expert annotators with linguistic training "annotate[d] 3,044 sentences in 100 dialogs, achieving a 0.874 averaged weighted kappa value" ([Li et al., 2019](https://arxiv.org/abs/1911.10742)). The third-party note emphasizes the same partition: "The total dataset comprises 220 human-human dialogs. The manually annotated subset comprises 100 dialogs and 3,044 sentences" ([Third-party research note](https://arxiv.org/abs/1911.10742)).

This means the annotated portion covers approximately **45.5% of the collected dialogs** (100 of 220) but contains **3,044 annotated sentences** — the finest-grained size statistic available for the corpus. The reported inter-annotator agreement of 0.874 (averaged weighted kappa) is high by conventional standards and suggests that the annotated labels are reliable enough to serve as supervision for a multi-task model such as MISSA ([Li et al., 2019](https://arxiv.org/abs/1911.10742)).

It is also worth noting the modeling context in which this annotated subset was used. The paper trains MISSA with an 80%/10%/10% split into training, validation, and test sets; applied to the 100 annotated dialogs, this yields roughly 80 training dialogs, 10 validation dialogs, and 10 test dialogs ([Li et al., 2019](https://arxiv.org/abs/1911.10742)). The authors mitigate the small supervised sample by first pre-training on the PERSONA-CHAT dataset before fine-tuning on AntiScam ([Li et al., 2019](https://arxiv.org/abs/1911.10742)).

## Derived Estimates of Full-Corpus Scale

The paper does not report the total number of sentences or words in the full 220-dialog corpus. However, a transparent extrapolation from the annotated subset is possible, provided its representativeness is acknowledged as an assumption. Table 2 presents these derived figures and labels them as estimates rather than reported values.

**Table 2. Derived estimates of full-corpus scale (author's calculations from reported figures).**

| Derived quantity | Calculation | Estimate |
|---|---|---|
| Sentences per annotated dialog | 3,044 ÷ 100 | ≈30.44 sentences |
| Estimated sentences in full corpus | 30.44 × 220 | ≈6,697 sentences |
| Estimated words per dialog | 30.44 sentences × 11.13 words | ≈339 words |
| Estimated words in full corpus | 339 × 220 | ≈74,500 words |

*Basis:* figures from ([Li et al., 2019](https://arxiv.org/abs/1911.10742)); calculations are the present author's.

These estimates should be treated cautiously for two reasons. First, they assume the 100 annotated dialogs are representative of all 220 in sentence density, which the paper does not verify. Second, there is a tension between the reported averages: 12.45 turns × 11.13 words ≈ 139 words per dialog if each turn is treated as a single 11.13-word utterance, which would imply far fewer than 30 sentences per dialog. The most plausible reconciliation is that the paper's "turns" and "utterances" are not coextensive with "sentences" — the authors explicitly state that they "segment each conversation turn into single sentences and then annotate each sentence rather than turns" ([Li et al., 2019](https://arxiv.org/abs/1911.10742)). Consequently, the sentence-based estimate of roughly 30 sentences per dialog is the more defensible derived metric, while the word-level extrapolation carries greater uncertainty.

## Annotation Granularity as a Dimension of Size

Size in a dialog corpus is not only a matter of tokens or dialogs; it is also a matter of how many labels are attached to each unit. AntiScam uses a **hierarchical intent annotation scheme** that separates on-task from off-task content ([Li et al., 2019](https://arxiv.org/abs/1911.10742)). For AntiScam, the on-task intents are *elicitation*, *providing_information*, and *refusal*; the off-task intents are shared across non-collaborative tasks and comprise six general dialog acts (*open_question*, *yes_no_question*, *positive_answer*, *negative_answer*, *responsive_statement*, *nonresponsive_statement*) and six social acts (*greeting*, *closing*, *apology*, *thanking*, *respond_to_thank*, *hold*) ([Li et al., 2019](https://arxiv.org/abs/1911.10742)). In addition, the authors identify **13 main semantic slots** for the anti-scam task, including *order_detail*, *order_update*, *payment*, *name*, *identity*, *address*, *phone_num*, *card_info*, *card_num*, *card_cvs*, *card_date*, *account_detail*, and *others* ([Li et al., 2019](https://arxiv.org/abs/1911.10742)).

The annotated 3,044 sentences thus carry multiple layers of labels: an intent, a semantic slot, and a role attribution (attacker or user). The paper also reports the distribution of some categories, which gives a sense of how the annotation mass is spread. Users produced more *refusal* labels than attackers (74 vs. 19), more *open_question* labels (173 vs. 54), and more *yes_no_question* labels (165 vs. 117); social content was substantial for both roles (292 for attackers and 252 for users combined) ([Li et al., 2019](https://arxiv.org/abs/1911.10742)). These distributions are consistent with the collection instructions, under which users who detected the attacker were told to prolong the conversation and to elicit information in return ([Li et al., 2019](https://arxiv.org/abs/1911.10742)).

## Collection Protocol and Its Bearing on Scale

AntiScam was collected through a role-playing task on Amazon Mechanical Turk in the form of typing conversations ([Li et al., 2019](https://arxiv.org/abs/1911.10742)). Workers were randomly paired: one was assigned the attacker role and the other the user role, and workers could not see their partner's instructions ([Li et al., 2019](https://arxiv.org/abs/1911.10742)). Both roles received specific personal data — for example, the user's name, credit card number, CVS number, expiration date, phone number, and billing address, along with the background that the user had purchased a heater on Amazon ([Li et al., 2019](https://arxiv.org/abs/1911.10742)). Bonuses were offered to users who detected attackers and elicited real information, and to attackers who elicited correct information ([Li et al., 2019](https://arxiv.org/abs/1911.10742)).

A notable quality signal tied to corpus size is the **172 out of 220 users (approximately 78.2%) who successfully identified their partner as an attacker** ([Li et al., 2019](https://arxiv.org/abs/1911.10742)). The authors interpret this as evidence that "the attackers are well trained and not too easily identifiable" ([Li et al., 2019](https://arxiv.org/abs/1911.10742)). In other words, the corpus's limited size is partly offset by a collection design that produced realistic, non-trivial adversarial behavior rather than easily detected role-play.

Separately from the dataset itself, the paper reports a human evaluation in which 15 college-student volunteers each interacted with all five models at least three times, producing **225 evaluation dialogs** and 45 human ratings per model ([Li et al., 2019](https://arxiv.org/abs/1911.10742)). These 225 dialogs are an evaluation artifact and should not be conflated with the 220-dialog AntiScam corpus.

## Comparative Context

Placing AntiScam against the other dataset used in the paper helps calibrate its size. The PersuasionForGood dataset consists of **1,017 dialogs**, of which **300 are annotated with dialog acts**, with an average conversation length of **10.43** and a vocabulary size of **8,141** ([Li et al., 2019](https://arxiv.org/abs/1911.10742)). Table 3 compares the two corpora.

**Table 3. AntiScam compared with PersuasionForGood.**

| Dimension | AntiScam | PersuasionForGood |
|---|---|---|
| Total dialogs | 220 | 1,017 |
| Annotated dialogs | 100 | 300 |
| Annotated sentences | 3,044 | Not reported in the provided source |
| Average conversation length | 12.45 turns | 10.43 |
| Average utterance length | 11.13 words | Not reported in the provided source |
| Vocabulary size | Not reported in the provided source | 8,141 |

*Source:* ([Li et al., 2019](https://arxiv.org/abs/1911.10742)).

On dialog count, AntiScam is roughly one-fifth the size of PersuasionForGood, though its share of annotated dialogs is proportionally higher (≈45% versus ≈30%). Both datasets were collected on Amazon Mechanical Turk in the form of typing conversations with off-task dialog interleaved, which the authors present as a shared design property ([Li et al., 2019](https://arxiv.org/abs/1911.10742)).

## Accessibility and Data Splits

The code and data for AntiScam are released by the authors at a public repository, https://gitlab.com/ucdavisnlp/antiscam ([Li et al., 2019](https://arxiv.org/abs/1911.10742)). For training and evaluation, the paper uses an 80% / 10% / 10% split across training, validation, and test data ([Li et al., 2019](https://arxiv.org/abs/1911.10742)). During training, slot values were replaced with slot tokens via delexicalization, and during testing the slot tokens were replaced with pre-defined information ([Li et al., 2019](https://arxiv.org/abs/1911.10742)). These details matter for assessing accessible size: depending on the release, the public artifact may include the full 220-dialog corpus, the 100-dialog annotated subset, or both; the provided sources do not specify the exact composition of the released package.

## Assessment

My assessment is that AntiScam should be characterized as a **small but densely annotated corpus** rather than a large-scale dataset. In absolute terms, 220 dialogs — and an annotated subset of 100 dialogs containing 3,044 sentences — is modest. The full corpus can be estimated at only a few thousand sentences and tens of thousands of words, and even that estimate rests on extrapolation from the annotated subset ([Li et al., 2019](https://arxiv.org/abs/1911.10742)).

That smallness, however, is offset in three ways. First, the annotation depth is high: every annotated sentence carries a hierarchical intent label and a semantic slot from a 13-slot inventory, with inter-annotator agreement of 0.874 ([Li et al., 2019](https://arxiv.org/abs/1911.10742)). Second, the experimental design compensates for limited supervised data by pre-training on PERSONA-CHAT before fine-tuning, an approach that the authors show outperforms baselines on fluency, coherence, engagement, dialog length, and task success ([Li et al., 2019](https://arxiv.org/abs/1911.10742)). Third, the collection protocol yields adversarial dialogs in which only about 78.2% of users detected the attacker, indicating that the data are non-trivial to model rather than artificially easy ([Li et al., 2019](https://arxiv.org/abs/1911.10742)).

The practical implication is that AntiScam is well suited as a benchmark for supervised fine-tuning of pretrained transformer models, and for testing whether intent- and slot-conditioned generation improves coherence and engagement, but it is not large enough on its own to support training large dialog models from scratch or to make strong claims about broad generalization. The authors themselves position the dataset as a "carefully-designed" contribution intended to address the scarcity of meaningful non-collaborative evaluation data, and later note that MISSA still struggles with distant conversation history because GPT tracks only a limited span ([Li et al., 2019](https://arxiv.org/abs/1911.10742)).

## Limitations of the Reported Figures

Several caveats apply. The primary source is the arXiv paper (1911.10742) by Li et al. (2019), which is a preprint rather than a peer-reviewed journal article, although it is the authoritative description of the dataset ([Li et al., 2019](https://arxiv.org/abs/1911.10742)). The third-party research note duplicates the paper's figures without adding independent verification, so the two sources are not fully independent confirmations ([Third-party research note](https://arxiv.org/abs/1911.10742)). The provided sources also do not report the total sentence count, total word count, or vocabulary size of the full 220-dialog corpus, nor do they specify exactly what portion of the data is publicly released. Finally, the internal inconsistency noted above between the reported turn count, utterance length, and sentence count means that any word-level estimate of the full corpus should be treated as indicative rather than precise.

## Conclusion

The AntiScam dataset consists of **220 human–human anti-scam dialogs**, with an average conversation length of **12.45 turns** and an average utterance length of **11.13 words**. A subset of **100 dialogs containing 3,044 sentences** was manually annotated by two expert annotators with linguistic training, achieving a **0.874 averaged weighted kappa**. The dataset uses a hierarchical intent scheme — three on-task intents for AntiScam plus twelve shared off-task intents — and **13 semantic slots**. Approximately **78.2% (172 of 220)** of users successfully identified their partner as an attacker. Derived estimates place the full corpus at roughly 6,700 sentences and 74,500 words, though these are extrapolations rather than reported values. In short, AntiScam is small in dialog count relative to corpora such as PersuasionForGood (1,017 dialogs), but it is heavily annotated and purpose-built for non-collaborative dialog research.

## References

Li, Y., Qian, K., Shi, W., & Yu, Z. (2019). *End-to-end trainable non-collaborative dialog system* (arXiv:1911.10742). arXiv. https://arxiv.org/abs/1911.10742

Third-party research note: *End-to-end trainable non-collaborative dialog system* [Unpublished research note]. (n.d.). Document 2. https://arxiv.org/abs/1911.10742