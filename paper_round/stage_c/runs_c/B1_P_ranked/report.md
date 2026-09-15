# How Big Is the AntiScam Dataset? Corpus Size, Annotation Scale, and Evaluation Scale in the *End-to-End Trainable Non-Collaborative Dialog System*

## Introduction

The direct answer to the query is that the AntiScam dataset is reported to contain **320 human-human dialogs**, collected through a role-playing Amazon customer service scam scenario on Amazon Mechanical Turk ([document_2.txt](document_2.txt)). That headline figure, however, is only one of several size measures attached to the corpus, and the supplied record also contains a competing count of 220 dialogs in the paper's own dataset description ([document_1.txt](document_1.txt)). Because the question "how big is the dataset?" can legitimately be answered in terms of dialogs, annotated sentences, conversational turns, utterances, annotation coverage, and human-evaluation volume, this report reconstructs every available size measure, examines the internal contradiction in the reported dialog counts, and offers an explicit assessment of which figure should be treated as authoritative. The position taken here is that **320 dialogs is the best-supported headline size**, with the 220 figure most plausibly reflecting an earlier corpus iteration or an internal reporting inconsistency, while the fully documented annotation scope remains 100 dialogs and 3,044 sentences.

## What AntiScam Is, and Why Its Size Matters

AntiScam was created to enrich the pool of publicly available non-collaborative task datasets; in it, users defend themselves against attackers attempting to collect personal information ([document_1.txt](document_1.txt)). The dataset was assembled specifically "to learn human elicitation strategies" by collecting dialogs "between users and attackers who aim to collect users information" ([document_1.txt](document_1.txt)). This purpose matters for interpreting corpus size: non-collaborative dialog tasks are described in the source material as "still relatively new to the study of dialog systems," with "insufficiently many meaningful datasets for evaluation," so AntiScam is presented as "a valuable example" rather than one contribution among many ([document_1.txt](document_1.txt)).

The corpus was used as one of two evaluation benchmarks for the MISSA model, alongside the existing PersuasionForGood dataset, which targets charitable-donation persuasion ([document_1.txt](document_1.txt)). AntiScam's objective within that study is to "build a dialog system that occupies the attacker's attention and elicits the attacker's information" ([document_1.txt](document_1.txt)). Consequently, the size of the corpus determines both what can be learned from it and how credible the reported model comparisons are.

## The Headline Size: Number of Dialogs

### The 320-dialog figure

The most frequently repeated size claim in the supplied record is that AntiScam "is a human-human anti-scam dialog corpus collected via a role-playing Amazon customer service scam scenario on Amazon Mechanical Turk" whose "size is 320 human-human dialogs" ([document_2.txt](document_2.txt)). The same figure appears again in the summary statement that "the total dataset comprises 320 human-human dialogs" ([document_2.txt](document_2.txt)). A third-party research note reproduced in the same source, framed explicitly around the key question "AntiScam corpus number of dialogs," likewise states that "the dataset contains 320 human-human dialogs" and that "the paper reports this total in its AntiScam dataset description" ([document_2.txt](document_2.txt)).

### The 220-dialog figure

In tension with these statements, the paperside dataset description reports that "we collected 220 human-human dialogs" ([document_1.txt](document_1.txt)). That passage also reports the corpus's average conversation length of 12.45 turns and average utterance length of 11.13 words, and states that "only 172 out of 220 users successfully identified their partner as an attacker" ([document_1.txt](document_1.txt)). The annotation figures attached to the same passage—two expert annotators with linguistic training annotating 3,044 sentences in 100 dialogs, with a 0.874 averaged weighted kappa—are consistent with the annotation figures reported elsewhere ([document_1.txt](document_1.txt)).

### Assessment of the discrepancy

Two mutually exclusive totals cannot both be correct for the same corpus version: 220 and 320 cannot simultaneously describe the full dialog count. Three considerations lead me to treat **320 dialogs as the more defensible working figure**:

1. **Frequency and explicitness.** The 320 figure appears repeatedly and is the answer given to a question explicitly framed as "AntiScam corpus number of dialogs" and "AntiScam dataset non-collaborative dialog size" ([document_2.txt](document_2.txt)), whereas 220 appears in a single passage ([document_1.txt](document_1.txt)).
2. **Internal consistency of the detection statistic.** The statement that "only 172 out of 220 users successfully identified their partner as an attacker, suggesting that the attackers are well trained and not too easily identifiable" is internally strained: 172 of 220 corresponds to roughly 78% identification, a success rate in tension with the inference that attackers were "not too easily identifiable" ([document_1.txt](document_1.txt)). By contrast, the parallel statement that "172 out of 320 users successfully identified their partner as an attacker" corresponds to approximately 54%, a rate far more compatible with the claim that attackers were difficult to detect ([document_2.txt](document_2.txt)). The 172 numerator is stable across both versions, which suggests it is the denominator that changed.
3. **Direction of revision.** The most economical explanation is that the corpus grew (or was re-counted) after the dataset description was drafted, leaving an earlier "220" in one paragraph while later summaries report 320. This is a hypothesis rather than a documented fact, since none of the supplied sources states that a revision occurred.

On that basis, the answer I would give to the query is: **antiScam comprises 320 human-human dialogs (or, on the conflicting report, 220)**, with 320 as the working headline size. A careful reader should treat the dialog count as requiring verification against the published paper, because the supplied record is not internally consistent.

## Annotation Scale: How Much of the Corpus Is Labeled

Corpus size and annotation scope are distinct in AntiScam. The manually annotated portion is a subset: "a subset of 100 dialogs containing 3,044 sentences was manually annotated" ([document_2.txt](document_2.txt)), and this annotation was performed by "two expert annotators who have linguistic training" ([document_2.txt](document_2.txt)). The paper-side description matches this, reporting that the researchers "recruited two expert annotators who have linguistic training to annotate 3,044 sentences in 100 dialogs, achieving a 0.874 averaged weighted kappa value" ([document_1.txt](document_1.txt)).

Two implications follow. First, the annotation coverage is roughly 31% of the 320-dialog corpus (100 of 320) — a derived proportion, since the source material states the two figures separately rather than as a percentage. Second, the reported inter-annotator agreement of 0.874 (averaged weighted kappa) is a size-relevant quality signal: it indicates that the 3,044 annotated sentences carry labels on which trained annotators converged to a high degree ([document_1.txt](document_1.txt)).

### The annotation scheme

The labeled data are organized under a hierarchical intent annotation scheme applied to both AntiScam and PersuasionForGood ([document_1.txt](document_1.txt)). For AntiScam, the on-task intents are **elicitation, providing_information, and refusal** — three task-specific categories ([document_1.txt](document_1.txt)). The off-task intents, described as "general for different non-collaborative tasks," comprise **open_question, yes_no_question, negative_answer, positive_answer, responsive_statement, nonresponsive_statement, greeting, thanking, respond_to_thank, apology, closing, and hold** — twelve shared categories ([document_1.txt](document_1.txt)). These label counts are derived by enumerating the categories listed in the reported scheme; the sources present them as a scheme rather than as totals.

## Conversational Granularity: Turns and Utterances

Beyond the dialog count, the corpus is sized by its conversational density. The average conversation length is **12.45 turns** and the average utterance length is **11.13 words** ([document_1.txt](document_1.txt)); the annotation summary states that "these averages describe the full AntiScam corpus" ([document_2.txt](document_2.txt)). Applying these reported averages arithmetically (a calculation performed here, not stated in the sources), a 320-dialog corpus corresponds to approximately 3,984 turns and, at 11.13 words per utterance, on the order of 44,300 words of dialog text. The same arithmetic applied to a 220-dialog corpus would yield roughly 2,739 turns.

A second derived observation concerns the units used. The annotated subset of 3,044 sentences across 100 dialogs implies about 30.4 sentences per dialog, which is substantially higher than the reported 12.45 turns per dialog ([document_1.txt](document_1.txt); [document_2.txt](document_2.txt)). Because the sources do not define the relationship between "sentence" and "turn," these two counts should not be treated as interchangeable, and any quantitative synthesis relying on both should flag the unit mismatch.

## Related Size Measures: Splits and Human Evaluation Volume

Two further quantities describe the scale at which the corpus was used rather than the scale at which it was collected. First, the experimental protocol divided the data into **80% training, 10% validation, and 10% testing** ([document_1.txt](document_1.txt)). Applied to a 320-dialog corpus, that implies approximately 256 training, 32 validation, and 32 test dialogs — again a derived figure.

Second, human evaluation was conducted at a scale independent of the corpus itself. The researchers "test our models and baselines with 15 college-student volunteers," each asked "to pretend to be an attacker and interact with all the models for at least three times to avoid randomness," yielding "225 number of dialogs" in total and "a total of 45 human ratings" per model ([document_1.txt](document_1.txt)). Because five models were compared (TransferTransfo, Hybrid, MISSA, MISSA-sel, and MISSA-con), the 225 collected dialogs and 45 ratings per model are arithmetically consistent (15 volunteers × 3 rounds × 5 models = 225; 15 × 3 = 45 per model), a derivation based on the reported figures ([document_1.txt](document_1.txt)).

The evaluation dimensions themselves were extensive: automatic metrics included perplexity and the RIP, RSP, ERIP, and ERSP rates, while human metrics included Fluency, Coherence, Engagement, Length, and TaskSuc ([document_1.txt](document_1.txt)). On the AntiScam data, MISSA recorded a perplexity of 21.07 against 32.96 for TransferTransfo, and the paper reports that "MISSA outperforms two baseline models (TransferTransfo and hybrid model) on almost all the metrics on both datasets" ([document_1.txt](document_1.txt)).

## Consolidated Size Metrics

| Size dimension | Reported value | Source |
|---|---|---|
| Total human-human dialogs | 320 (conflicting report: 220) | [document_2.txt](document_2.txt); [document_1.txt](document_1.txt) |
| Manually annotated subset | 100 dialogs | [document_1.txt](document_1.txt); [document_2.txt](document_2.txt) |
| Annotated sentences | 3,044 sentences | [document_1.txt](document_1.txt); [document_2.txt](document_2.txt) |
| Annotators | 2 expert annotators with linguistic training | [document_1.txt](document_1.txt); [document_2.txt](document_2.txt) |
| Inter-annotator agreement | 0.874 averaged weighted kappa | [document_1.txt](document_1.txt) |
| Average conversation length | 12.45 turns | [document_1.txt](document_1.txt); [document_2.txt](document_2.txt) |
| Average utterance length | 11.13 words | [document_1.txt](document_1.txt); [document_2.txt](document_2.txt) |
| Users identifying partner as attacker | 172 | [document_1.txt](document_1.txt); [document_2.txt](document_2.txt) |
| Train / validation / test split | 80% / 10% / 10% | [document_1.txt](document_1.txt) |
| Human-evaluation dialogs collected | 225 | [document_1.txt](document_1.txt) |
| Human ratings per model | 45 (15 volunteers × 3 rounds) | [document_1.txt](document_1.txt) |
| AntiScam-specific on-task intents | 3 (elicitation, providing_information, refusal) | [document_1.txt](document_1.txt) |
| Shared off-task intents | 12 | [document_1.txt](document_1.txt) |

| Conflicting dialog counts | Denominator used for the 172 figure | Implied identification rate |
|---|---|---|
| 320 dialogs | 320 | ≈53.8% |
| 220 dialogs | 220 | ≈78.2% |

The implied identification rates in the second table are my own calculations from the reported numbers ([document_1.txt](document_1.txt); [document_2.txt](document_2.txt)).

## Interpretation: How "Big" Is AntiScam, Really?

My assessment is that AntiScam is **small-to-moderate by modern dialog-corpus standards, and explicitly positioned as such by its authors**. A few hundred dialogs, a few thousand annotated sentences, and roughly a dozen turns per conversation describe a resource built to demonstrate feasibility in an under-resourced task family, not to support large-scale pretraining. The authors themselves frame the contribution this way, noting that non-collaborative tasks are "still relatively new" and that available datasets are "insufficiently many" ([document_1.txt](document_1.txt)). Two design choices reinforce the reading of AntiScam as a compact, carefully curated benchmark rather than a bulk corpus: only about a third of dialogs were manually annotated, and those annotations were produced by two linguistically trained experts with a high reported agreement ([document_1.txt](document_1.txt); [document_2.txt](document_2.txt)).

The 172-of-320 detection outcome is also substantive rather than incidental, because it characterizes corpus difficulty rather than corpus volume: it indicates that a slight majority of users failed to recognize their interlocutor as an attacker, which the summary interprets as evidence that "the attackers are well trained and not too easily identifiable" ([document_2.txt](document_2.txt)). A corpus of this size with a detection rate near chance is more informative for elicitation-strategy research than a larger corpus in which the adversarial role is trivially detectable.

## Limitations and Caveats

The principal limitation of this report is the unresolved numeric conflict between 220 and 320 dialogs ([document_1.txt](document_1.txt); [document_2.txt](document_2.txt)). No supplied passage explains the difference, so the reconciliation offered above is inference, not documentation. A second caveat is unit ambiguity: the sources report dialogs, sentences, turns, and utterances without defining their relationships, so derived totals (such as approximately 3,984 turns or 44,300 words for a 320-dialog corpus) should be treated as illustrative estimates. Third, the level of detail available differs by metric — annotation and human-evaluation figures are comparatively precise, whereas the corpus-level dialog count is the least stable number in the record. Finally, the sources carry no dates or bibliographic metadata, so recency cannot be used as a tiebreaker, and the reliability ranking used here rests instead on explicitness, repetition, and internal consistency.

## Conclusion

**The AntiScam dataset is reported as 320 human-human anti-scam dialogs**, collected through a role-playing Amazon customer service scam on Amazon Mechanical Turk ([document_2.txt](document_2.txt)). Within that corpus, 100 dialogs and 3,044 sentences were manually annotated by two linguistically trained experts with a 0.874 averaged weighted kappa, conversations average 12.45 turns and 11.13 words per utterance, 172 users identified their partner as an attacker, and experiments used an 80/10/10 split with 225 human-evaluation dialogs and 45 ratings per model ([document_1.txt](document_1.txt); [document_2.txt](document_2.txt)). The one competing figure — 220 dialogs, stated in the paper's dataset description ([document_1.txt](document_1.txt)) — cannot be reconciled with 320 on the evidence provided, but the 320 figure is the more repeatedly and explicitly asserted count and is the one that renders the 172-user detection rate coherent with the claim that attackers were difficult to identify. The prudent conclusion is therefore that AntiScam is a compact, densely annotated corpus of roughly 320 dialogs, with the dialog count itself flagged as the least reliable number in the published description.

## References

document_1.txt. (n.d.). *End-to-End trainable non-collaborative dialog system* [Excerpted source document]. ([document_1.txt](document_1.txt))

document_2.txt. (n.d.). *Third-party research note: End-to-End trainable non-collaborative dialog system* [Excerpted source document]. ([document_2.txt](document_2.txt))