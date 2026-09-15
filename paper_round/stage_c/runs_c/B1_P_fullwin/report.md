# How Big Is the AntiScam Dataset? A Sizing, Composition, and Reliability Analysis

## Executive Summary

The AntiScam dataset — a corpus of human-human anti-scam dialogs introduced to support research on non-collaborative dialog systems — is reported by its originating authors as comprising **220 human-human dialogs** ([Li, Qian, Shi, & Yu, 2019](https://arxiv.org/abs/1911.10742)). This figure is stated twice within the primary paper, once in the dataset description section and again in the anti-scam collection setting section, which gives it strong internal consistency ([Li et al., 2019](https://arxiv.org/abs/1911.10742)). Within that total corpus, a manually annotated subset of **100 dialogs containing 3,044 sentences** was labeled by two expert annotators with linguistic training ([Li et al., 2019](https://arxiv.org/abs/1911.10742)).

However, a secondary source supplied in the research materials — a third-party research note summarizing the same paper — reports the dataset size as **320 human-human dialogs**, and further states that "172 out of 320 users" identified their partner as an attacker ([Third-party research note, n.d.](document_2.txt)). This conflicts directly with the primary paper's repeated statement that "172 out of 220 users" successfully identified their partner as an attacker ([Li et al., 2019](https://arxiv.org/abs/1911.10742)). The report below resolves this conflict in favor of the primary peer-reviewed-style source, explains the evidentiary basis for that judgment, and situates the dataset size within the broader scale of the study.

## Primary Source Evidence: The Reported Dataset Size

### The 220-Dialog Figure

The AntiScam corpus was created to learn human elicitation strategies in a scam-defense setting. The authors describe choosing "a popular Amazon customer service scam scenario to collect dialogs between users and attackers who aim to collect users information," and posting a role-playing task on the Amazon Mechanical Turk platform ([Li et al., 2019](https://arxiv.org/abs/1911.10742)). The reported collection total is unambiguous in the primary text:

> "We posted a role-playing task on the Amazon Mechanical Turk platform and collected a typing conversation dataset named AntiScam. We collected 220 human-human dialogs." ([Li et al., 2019](https://arxiv.org/abs/1911.10742))

The same figure is reiterated in the appendix describing the collection setting: "We collected 220 human-human dialogs" ([Li et al., 2019](https://arxiv.org/abs/1911.10742)). The repetition of the identical number in two structurally distinct sections of the paper — the dataset section and the collection-setting appendix — substantially reduces the likelihood of a typographical error, since independent editorial drafting would be required for the same error to appear twice.

### Conversation and Utterance Lengths

Beyond raw dialog count, the paper specifies descriptive statistics that characterize dataset size in conversational terms. The average conversation length is **12.45 turns**, and the average utterance length is **11.13 words** ([Li et al., 2019](https://arxiv.org/abs/1911.10742)). These averages are characterized in the third-party note as describing "the full AntiScam corpus" ([Third-party research note, n.d.](document_2.txt)), which is consistent with the primary paper's presentation of the statistics alongside the 220-dialog total.

From these reported statistics, approximately 138.6 words per dialog and roughly 30,500 total words across the corpus can be derived by multiplication (220 × 12.45 × 11.13). These derived values are arithmetic extensions of the reported figures, not figures stated directly in the source, and should be treated as estimates rather than reported statistics.

### Attacker Identification Rate

A notable outcome statistic tied to the corpus size concerns detection: "Only 172 out of 220 users successfully identified their partner as an attacker, suggesting that the attackers are well trained and not too easily identifiable" ([Li et al., 2019](https://arxiv.org/abs/1911.10742)). This corresponds to a detection rate of approximately 78.2% of users, a figure that supports the authors' interpretation that the simulated attackers were credible. The paper's use of the qualifier "only" is linguistically consistent with a high proportion being described as surprisingly incomplete — further evidence that 220, not 320, is the intended denominator, since 172/320 (53.75%) would describe roughly half the participants and would more naturally be framed as a moderate rather than "only" a near-total detection outcome.

## Discrepancy in Secondary Reporting: The 320-Dialog Claim

### Details of the Conflict

The third-party research note states that "The dataset contains 320 human-human dialogs" and repeats, "The total dataset comprises 320 human-human dialogs" ([Third-party research note, n.d.](document_2.txt)). It then states: "The paper reports that 172 out of 320 users successfully identified their partner as an attacker" ([Third-party research note, n.d.](document_2.txt)).

This creates a three-way inconsistency:

| Statistic | Primary paper ([Li et al., 2019](https://arxiv.org/abs/1911.10742)) | Third-party note ([Third-party research note, n.d.](document_2.txt)) |
|---|---|---|
| Total human-human dialogs | 220 | 320 |
| Users identifying attacker | 172 out of 220 | 172 out of 320 |
| Implied detection rate | ~78.2% | ~53.8% |
| Annotated dialogs | 100 | 100 |
| Annotated sentences | 3,044 | 3,044 |
| Average conversation length | 12.45 turns | 12.45 turns |
| Average utterance length | 11.13 words | 11.13 words |

### Assessment of Source Reliability

Applying standard source-hierarchy principles, the primary document should be weighted above the secondary summary for three reasons.

First, **the paper is the originating source**. Its statements about its own dataset constitute primary evidence; the third-party note is an interpretive summary referencing "document_1.txt" as its basis ([Third-party research note, n.d.](document_2.txt)).

Second, **the primary source is internally consistent across sections**. The number 220 appears in both the dataset section and the collection-setting appendix, and the 172/220 pairing is coherent with the qualitative framing ("only") ([Li et al., 2019](https://arxiv.org/abs/1911.10742)).

Third, **all other reported statistics align between the two sources**, including the 100-dialog annotation subset, the 3,044 annotated sentences, the 12.45-turn average, and the 11.13-word average ([Li et al., 2019](https://arxiv.org/abs/1911.10742); [Third-party research note, n.d.](document_2.txt)). The single divergence is the total dialog count and its associated denominator. Because the annotation and length statistics match exactly while only the total count differs, the most parsimonious explanation is a localized error in the secondary note rather than two independent errors in the primary paper — particularly since the secondary note itself asserts that "the paper reports this total in its AntiScam dataset description," an attribution that the primary text does not support ([Third-party research note, n.d.](document_2.txt)).

Accordingly, the evidence-based position of this report is that **220 human-human dialogs is the defensible figure**, with the 320 figure treated as an unverified and likely erroneous secondary transcription.

## Annotation Scale and Composition

### The Annotated Subset

Annotation coverage is a second dimension of dataset size. The paper reports recruiting "two expert annotators who have linguistic training to annotate 3,044 sentences in 100 dialogs, achieving a 0.874 averaged weighted kappa value" ([Li et al., 2019](https://arxiv.org/abs/1911.10742)). This establishes that roughly 45.5% of the 220-dialog corpus received expert manual annotation — a derived ratio based on the primary sources' own figures. Dividing 3,044 sentences across 100 dialogs yields approximately 30.4 sentences per annotated dialog, and dividing that by the reported 12.45-turn average produces roughly 2.44 sentences per turn (derived estimates).

The 0.874 weighted kappa value indicates substantial inter-annotator agreement, which matters for dataset size interpretation: a larger but weakly annotated corpus would be less analytically usable than a smaller, high-agreement annotated subset ([Li et al., 2019](https://arxiv.org/abs/1911.10742)).

### Intent and Slot Schema Size

The dataset's labeling framework adds further dimensionality. The AntiScam task defines three task-specific on-task intents — *elicitation*, *providing_information*, and *refusal* — alongside a shared off-task scheme of six general intents (*open_question*, *yes_no_question*, *positive_answer*, *negative_answer*, *responsive_statement*, *nonresponsive_statement*) and six social intents (*greeting*, *closing*, *apology*, *thanking*, *respond_to_thank*, *hold*) ([Li et al., 2019](https://arxiv.org/abs/1911.10742)). Separately, 13 main semantic slots are identified for the anti-scam task, including order detail, payment, name, identity, address, phone number, card information, card number, card CVS, card date, account detail, order update, and an "others" category ([Li et al., 2019](https://arxiv.org/abs/1911.10742)).

### Distributional Evidence of Scale

The paper reports intent distribution counts that shed light on corpus composition across the annotated portion: users produced 74 refusals versus attackers' 19; users asked 173 open questions versus attackers' 54; users asked 165 yes/no questions versus attackers' 117; and social content totaled 292 sentences for attackers and 252 for users ([Li et al., 2019](https://arxiv.org/abs/1911.10742)). Summing the four social categories alone (292 + 252 = 544) against the 3,044-sentence annotation set indicates that social content accounts for a meaningful share of the annotated material.

## Comparative Context: PersuasionForGood and Data Splits

Scale is best understood comparatively. The paper also evaluates on the PersuasionForGood dataset, which "consists of 1,017 dialogs, where 300 dialogs are annotated with dialog acts," with an average conversation length of 10.43 and a vocabulary size of 8,141 ([Li et al., 2019](https://arxiv.org/abs/1911.10742)). Thus, AntiScam at 220 dialogs is roughly one-fifth the size of PersuasionForGood in raw dialog count, while the PersuasionForGood annotation coverage (300 of 1,017 dialogs, ~29.5%) exceeds AntiScam's (100 of 220, ~45.5%) only when measured as a proportion; in annotated-dialog counts, AntiScam's 100 exceeds the annotation focus of the comparison set's 300 only in relative terms (derived comparisons).

Both datasets were split identically: 80% for training, 10% for validation, and 10% for testing ([Li et al., 2019](https://arxiv.org/abs/1911.10742)). Applied to AntiScam's 220 dialogs, this implies approximately 176 training dialogs, 22 validation dialogs, and 22 test dialogs (derived estimates). Applied to PersuasionForGood's 1,017 dialogs, it implies roughly 814, 102, and 102 dialogs respectively (derived estimates).

| Dimension | AntiScam | PersuasionForGood |
|---|---|---|
| Raw dialogs | 220 ([Li et al., 2019](https://arxiv.org/abs/1911.10742)) | 1,017 ([Li et al., 2019](https://arxiv.org/abs/1911.10742)) |
| Annotated dialogs | 100 ([Li et al., 2019](https://arxiv.org/abs/1911.10742)) | 300 ([Li et al., 2019](https://arxiv.org/abs/1911.10742)) |
| Annotated sentences | 3,044 ([Li et al., 2019](https://arxiv.org/abs/1911.10742)) | Not reported in source |
| Avg. turns per dialog | 12.45 ([Li et al., 2019](https://arxiv.org/abs/1911.10742)) | 10.43 ([Li et al., 2019](https://arxiv.org/abs/1911.10742)) |
| Avg. utterance length | 11.13 words ([Li et al., 2019](https://arxiv.org/abs/1911.10742)) | Not reported in source |
| Vocabulary size | Not reported in source | 8,141 ([Li et al., 2019](https://arxiv.org/abs/1911.10742)) |

## Study Design Scale: Human Evaluation

The scale of human evaluation surrounding the dataset provides additional context on its operational size. The authors "test our models and baselines with 15 college-student volunteers," each asked to role-play an attacker and "interact with all the models for at least three times," yielding "in total collect 225 number of dialogs," with each of the five models receiving 45 human ratings ([Li et al., 2019](https://arxiv.org/abs/1911.10742)). The five evaluated systems were TransferTransfo, Hybrid, MISSA, MISSA-sel, and MISSA-con ([Li et al., 2019](https://arxiv.org/abs/1911.10742)). This evaluation scale — 225 interaction dialogs collected specifically for testing, separate from the 220-dialog training corpus — illustrates that the total conversation volume associated with the AntiScam research effort exceeds the headline dataset count.

## Implications and Interpretation

The size of AntiScam carries direct methodological consequences. At 220 dialogs with 100 annotated, it is a small-to-medium corpus by contemporary dialog-system standards, and the authors themselves acknowledge the scarcity of comparable resources: "As non-collaborative tasks are still relatively new to the study of dialog systems, there are insufficiently many meaningful datasets for evaluation and we hope this provides a valuable example" ([Li et al., 2019](https://arxiv.org/abs/1911.10742)).

The dataset's stated purpose also shapes how its size should be judged. It is positioned as a benchmark designed to "interleave the on-task and off-task contents in the conversation," addressing the difficulty that earlier non-collaborative datasets were "not specifically collected and designed for non-collaborative tasks," making it "difficult to disentangle the on-task and off-task contents and measure the performance" ([Li et al., 2019](https://arxiv.org/abs/1911.10742)). Under this framing, annotation depth and label reliability (0.874 weighted kappa) may matter more than raw dialog count.

A final consideration is the risk of propagating secondary-source errors. The third-party note's 320 figure, if adopted uncritically, would inflate the corpus by approximately 45.5% and would simultaneously misstate the attacker-detection rate from roughly 78.2% to roughly 53.8% ([Third-party research note, n.d.](document_2.txt); [Li et al., 2019](https://arxiv.org/abs/1911.10742)). Because the note explicitly attributes the 320 figure to the paper, downstream users relying on it would attribute an unsupported claim to the original authors. This underscores the importance of verifying size statistics against the primary text.

## Conclusion

The AntiScam dataset, as reported by its originating authors, is **220 human-human dialogs** collected through a role-playing Amazon customer-service scam scenario on Amazon Mechanical Turk, with an average conversation length of 12.45 turns and an average utterance length of 11.13 words ([Li et al., 2019](https://arxiv.org/abs/1911.10742)). A subset of 100 dialogs and 3,044 sentences was manually annotated by two linguistically trained expert annotators, achieving a 0.874 averaged weighted kappa value ([Li et al., 2019](https://arxiv.org/abs/1911.10742)). Of the 220 users, 172 successfully identified their partner as an attacker ([Li et al., 2019](https://arxiv.org/abs/1911.10742)). A conflicting secondary report of 320 dialogs is not supported by the primary text and is best treated as an unverified discrepancy, given that the same secondary source reproduces all other statistics accurately and that the primary paper states 220 consistently in two separate sections ([Third-party research note, n.d.](document_2.txt); [Li et al., 2019](https://arxiv.org/abs/1911.10742)).

## References

Li, Y., Qian, K., Shi, W., & Yu, Z. (2019). *End-to-end trainable non-collaborative dialog system* (arXiv:1911.10742). arXiv. https://arxiv.org/abs/1911.10742

Third-party research note: End-to-End Trainable Non-Collaborative Dialog System. (n.d.). [Unpublished research note, document_2.txt].