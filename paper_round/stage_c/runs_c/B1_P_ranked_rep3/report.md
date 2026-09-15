# How Big Is the AntiScam Dataset? A Detailed Assessment of Corpus Size, Annotation Scope, and Related Quantitative Dimensions

## Introduction

The AntiScam dataset is a human–human anti-scam dialog corpus introduced to support research on non-collaborative dialog systems—conversational settings in which the two parties pursue divergent goals rather than cooperating toward a shared objective ([Document 1](document_1.txt)). Because dataset size directly conditions what can be claimed about model generalization, annotation coverage, and statistical reliability, the question "How big is the AntiScam dataset?" is not a trivial one. The available documentary evidence answers it along several distinct axes: the total number of collected dialogs, the number of dialogs and sentences that were manually annotated, the average conversation and utterance lengths, and the number of users who successfully identified their conversational partner as an attacker. This report synthesizes those figures, flags an internal discrepancy between the two source documents regarding the headline dialog count, and offers a reasoned judgment about which figure should be treated as authoritative.

## Provenance and Purpose of the Corpus

AntiScam was created to enrich the pool of publicly available non-collaborative task datasets, which the authors characterize as still relatively new to the study of dialog systems and therefore insufficiently numerous for meaningful evaluation ([Document 1](document_1.txt)). The corpus consists of human–human anti-scam dialogs designed to learn human elicitation strategies, and it was collected through a role-playing Amazon customer service scam scenario hosted on Amazon Mechanical Turk ([Document 2](document_2.txt)). In the scenario, users defend themselves against attackers attempting to collect personal information; the corresponding system-level objective in the paper is to build a dialog system that occupies the attacker's attention and elicits the attacker's information ([Document 1](document_1.txt)). A third-party research note independently confirms that the corpus comprises human–human anti-scam dialogs, was collected via the Amazon Mechanical Turk role-playing scenario, and serves as the dataset for non-collaborative dialog research in the paper ([Document 2](document_2.txt)).

## The Headline Question: Total Size of the Corpus

### Reported Totals and the Discrepancy Between Sources

The two available source documents disagree on the total number of dialogs in AntiScam. The primary paper text, in its dedicated "AntiScam Dataset" section, states plainly that the authors "collected 220 human-human dialogs" ([Document 1](document_1.txt)). By contrast, the third-party research note states that "the dataset contains 320 human-human dialogs" and repeats that figure multiple times, including in a summary paragraph ([Document 2](document_2.txt)).

| Source | Reported total dialogs | Reported identification statistic | Reported annotated subset |
|---|---|---|---|
| Primary paper text (AntiScam Dataset section) | 220 ([Document 1](document_1.txt)) | 172 out of 220 ([Document 1](document_1.txt)) | 3,044 sentences in 100 dialogs ([Document 1](document_1.txt)) |
| Third-party research note / summary | 320 ([Document 2](document_2.txt)) | 172 out of 320 ([Document 2](document_2.txt)) | 100 dialogs and 3,044 sentences ([Document 2](document_2.txt)) |

Notably, the identification statistic is reported as "172 out of 220" in the primary paper text but as "172 out of 320" in the third-party note ([Document 1](document_1.txt); [Document 2](document_2.txt)). The numerator is identical in both accounts, which suggests that the denominator—and hence the headline corpus size—is where the inconsistency lies.

### Which Figure Should Be Trusted?

My assessment, based on the internal evidence of the supplied documents, is that **220 dialogs is the more defensible figure**. Three considerations support this conclusion. First, the 220 figure appears in the authors' own dataset description section, where the corpus is described in the first person ("We collected 220 human-human dialogs"), which is the most direct form of primary reporting available in these materials ([Document 1](document_1.txt)). Second, the 220 figure is internally consistent with the accompanying identification statistic: "Only 172 out of 220 users successfully identified their partner as an attacker, suggesting that the attackers are well trained and not too easily identifiable" ([Document 1](document_1.txt)). Replacing the denominator with 320 without changing the numerator of 172 would silently alter the reported identification rate from approximately 78.2% to approximately 53.8%, a materially different interpretation of the same underlying experiment. Third, the 320 figure appears only in derived or summary material—the third-party research note and repeated summarizing paragraphs—rather than in the primary dataset description ([Document 2](document_2.txt)). Derived notes are more susceptible to transcription or revision errors than the originating text. That said, it remains possible that 320 reflects an extended or later version of the corpus not described in the primary excerpt; the supplied documents do not allow that possibility to be excluded with certainty, and I therefore treat 220 as the best-supported estimate while recording 320 as the alternative reported figure.

## The Annotated Subset: A Distinct Measure of Size

Corpus size and annotation coverage are not the same quantity. Regardless of whether the full corpus contains 220 or 320 dialogs, the manually annotated subset is consistently reported as **100 dialogs containing 3,044 sentences** ([Document 1](document_1.txt); [Document 2](document_2.txt)). Two expert annotators with linguistic training performed this annotation ([Document 2](document_2.txt)), and they achieved an averaged weighted kappa value of 0.874 ([Document 1](document_1.txt)), which indicates a high level of inter-annotator agreement. A third-party research note confirms that the annotation statistics cover 100 dialogs and 3,044 sentences and that the annotation was performed by two expert annotators with linguistic training ([Document 2](document_2.txt)).

This means that, on the most conservative reading, only about 45.5% of a 220-dialog corpus (100/220) — or approximately 31.3% of a 320-dialog corpus (100/320) — received manual sentence-level annotation. The annotated subset is therefore a substantial but partial layer of the overall collection.

## Turn-Level and Utterance-Level Scale

Beyond raw dialog counts, AntiScam's size can be expressed in conversational units. The average conversation length is **12.45 turns**, and the average utterance length is **11.13 words** ([Document 1](document_1.txt); [Document 2](document_2.txt)). The third-party note specifies that these averages describe the full AntiScam corpus rather than only the annotated subset ([Document 2](document_2.txt)).

These averages permit rough order-of-magnitude estimates of the corpus's textual volume. Using the stated averages, a 220-dialog corpus would comprise approximately 2,739 conversational turns and roughly 30,500 words, whereas a 320-dialog corpus would comprise approximately 3,984 turns and roughly 44,300 words. Within the annotated subset specifically, the reported 3,044 sentences across 100 dialogs implies approximately 30.4 sentences per annotated dialog, suggesting that the annotated material captures multiple utterances per turn of conversation. These derived figures are computational illustrations based on the stated averages and should be treated as approximate.

| Corpus statistic | Reported value | Source |
|---|---|---|
| Total human–human dialogs | 220 (primary) / 320 (third-party note) | ([Document 1](document_1.txt); [Document 2](document_2.txt)) |
| Annotated dialogs | 100 | ([Document 1](document_1.txt); [Document 2](document_2.txt)) |
| Annotated sentences | 3,044 | ([Document 1](document_1.txt); [Document 2](document_2.txt)) |
| Average conversation length | 12.45 turns | ([Document 1](document_1.txt); [Document 2](document_2.txt)) |
| Average utterance length | 11.13 words | ([Document 1](document_1.txt); [Document 2](document_2.txt)) |
| Inter-annotator agreement (weighted kappa) | 0.874 | ([Document 1](document_1.txt)) |

## Participant-Level Size and the Identification Outcome

Another dimension of size concerns the human participants involved. The paper reports that **172 users successfully identified their partner as an attacker**, out of either 220 or 320 participants depending on the source ([Document 1](document_1.txt); [Document 2](document_2.txt)). Under the 220-dialog reading, the success rate is approximately 78.2%, which the authors describe as evidence that "the attackers are well trained and not too easily identifiable" ([Document 1](document_1.txt)). Under the 320-dialog reading, the success rate falls to approximately 53.8% ([Document 2](document_2.txt)). Either way, the figure indicates that a meaningful share of users failed to detect the scam, underscoring the practical relevance of the corpus for studying elicitation and defense strategies.

## Data Splits and Experimental Scale

For modeling purposes, the dataset is partitioned into **80% training, 10% validation, and 10% testing** splits ([Document 1](document_1.txt)). Applying these proportions to the two candidate totals yields the following:

| Corpus total | Training (80%) | Validation (10%) | Test (10%) |
|---|---|---|---|
| 220 dialogs | ~176 | ~22 | ~22 |
| 320 dialogs | ~256 | ~32 | ~32 |

These split sizes are derived from the stated percentages and are presented as estimates. They matter because they determine the scale of the evaluation reported on AntiScam, where the MISSA model was benchmarked against TransferTransfo and a hybrid baseline ([Document 1](document_1.txt)).

Separately from the corpus itself, the paper conducted a human evaluation in which 15 college-student volunteers each role-played an attacker and interacted with all five models at least three times to avoid randomness, yielding **225 collected dialogs** and **45 human ratings per model** ([Document 1](document_1.txt)). This evaluation set is distinct from the AntiScam corpus and should not be conflated with its size.

## Structural Composition: The Intent Annotation Scheme

Size also has a compositional dimension. The annotation scheme is hierarchical, splitting intents into task-specific "On-task" categories and general "Off-task" categories ([Document 1](document_1.txt)). For AntiScam, the On-task intents are *elicitation*, *providing_information*, and *refusal*; for PersuasionForGood, the On-task intents include *agree_donation*, *disagree_donation*, *ask_donation_amount*, and related categories. The Off-task intents—*open_question*, *yes_no_question*, *negative_answer*, *positive_answer*, *responsive_statement*, *nonresponsive_statement*, *greeting*, *thanking*, *respond_to_thank*, *apology*, *closing*, and *hold*—are shared across both datasets ([Document 1](document_1.txt)). This scheme defines the label space over which the 3,044 annotated sentences are distributed.

## Comparative Context and Significance

AntiScam was evaluated alongside the existing PersuasionForGood dataset, in which a dialog system aims to persuade people to donate to a charity ([Document 1](document_1.txt)). On PersuasionForGood, MISSA achieved the lowest perplexity at 19.91 and the highest ERIP at 51.6%, outperforming TransferTransfo and the hybrid baseline across all evaluation metrics ([Document 1](document_1.txt)). The paper attributes this to the greater variety of possible responses with the same intent in PersuasionForGood than in AntiScam, and concludes that model structure should be adjusted according to dataset characteristics ([Document 1](document_1.txt)). This comparison reinforces that AntiScam's relatively compact scale—whether 220 or 320 dialogs, with 100 annotated—is nonetheless sufficient to support meaningful non-collaborative dialog research when combined with a second corpus.

## Conclusion

The AntiScam dataset's size depends on which layer of the resource is being measured. The primary paper text reports **220 human–human dialogs**, while a third-party research note reports **320** ([Document 1](document_1.txt); [Document 2](document_2.txt)). On balance, the 220 figure is better supported because it originates in the authors' own dataset description and is internally consistent with the reported statistic that 172 users identified their partner as an attacker ([Document 1](document_1.txt)). Consistent across both sources is the manually annotated subset of **100 dialogs and 3,044 sentences**, annotated by two expert linguistically trained annotators with a weighted kappa of 0.874 ([Document 1](document_1.txt); [Document 2](document_2.txt)). Structurally, the corpus averages **12.45 turns per conversation** and **11.13 words per utterance**, and it is partitioned into 80% training, 10% validation, and 10% test sets ([Document 1](document_1.txt); [Document 2](document_2.txt)). Any downstream use of AntiScam should therefore cite the dialog count with explicit acknowledgement of the 220-versus-320 divergence, and should rely on the 100-dialog/3,044-sentence annotated subset as the agreed foundation for supervised modeling.

## References

Document 1. (n.d.). *End-to-End Trainable Non-Collaborative Dialog System* [Manuscript excerpts]. document_1.txt.

Document 2. (n.d.). *Third-party research note: End-to-End Trainable Non-Collaborative Dialog System* [Research note]. document_2.txt.