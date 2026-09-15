# How Big Is the AntiScam Dataset? A Sizing Analysis of a Human–Human Anti-Scam Dialog Corpus

## Executive Summary

The AntiScam corpus is a human–human anti-scam dialog dataset developed to study non-collaborative dialog, and it was collected through a role-playing Amazon customer-service scam scenario hosted on Amazon Mechanical Turk ([Document 1](document_1.txt)). Its size is reported in the primary source as **220 human–human dialogs**, with an average conversation length of 12.45 turns and an average utterance length of 11.13 words ([Document 1](document_1.txt)). A manually annotated subset of **100 dialogs containing 3,044 sentences** was labeled by two expert annotators with linguistic training, reaching an averaged weighted kappa value of 0.874 ([Document 1](document_1.txt)). A third-party research note characterizing the same corpus states that it contains **320 human–human dialogs** ([Document 2](document_2.txt)). This report examines both figures, quantifies the consequences of each, and concludes that **220 dialogs is the better-supported total**, while the 100-dialog / 3,044-sentence annotation block is the only size statistic that is fully consistent across all available sources ([Document 1](document_1.txt); [Document 2](document_2.txt)).

## 1. Background: What the AntiScam Dataset Is

To enrich the pool of publicly available non-collaborative task datasets, the authors collected a new dataset named AntiScam, in which users defend themselves against attackers attempting to collect personal information ([Document 1](document_1.txt)). The stated purpose was to build a corpus of human–human anti-scam dialogs in order to learn human elicitation strategies ([Document 1](document_1.txt)). The authors selected "a popular Amazon customer service scam scenario" and posted a role-playing task on the Amazon Mechanical Turk platform, producing a typed conversation dataset ([Document 1](document_1.txt)). Because non-collaborative tasks are relatively new to dialog-system research, the authors explicitly note that there are insufficiently many meaningful datasets for evaluation and express the hope that AntiScam provides a valuable example ([Document 1](document_1.txt)).

This provenance matters for interpreting "size." AntiScam is a human–human corpus, not a human–machine or synthetic corpus, which means its size is bounded by the cost of recruiting and paying Turkers to role-play both a user and an attacker across a full scam conversation ([Document 1](document_1.txt); [Document 2](document_2.txt)). It is also a *typed* conversation dataset, so size can be counted in dialogs, turns, utterances, sentences, or words—each of which yields a different number ([Document 1](document_1.txt)).

## 2. The Core Size Figures

The following table consolidates every size-relevant statistic reported across the two available sources.

### Table 1. Reported size metrics for the AntiScam corpus

| Metric | Reported value | Source |
|---|---|---|
| Total human–human dialogs | 220 | [Document 1](document_1.txt) |
| Total human–human dialogs (alternative figure) | 320 | [Document 2](document_2.txt) |
| Manually annotated dialogs | 100 | [Document 1](document_1.txt); [Document 2](document_2.txt) |
| Manually annotated sentences | 3,044 | [Document 1](document_1.txt); [Document 2](document_2.txt) |
| Expert annotators | 2 (linguistically trained) | [Document 1](document_1.txt); [Document 2](document_2.txt) |
| Average conversation length | 12.45 turns | [Document 1](document_1.txt); [Document 2](document_2.txt) |
| Average utterance length | 11.13 words | [Document 1](document_1.txt); [Document 2](document_2.txt) |
| Users who identified their partner as an attacker | 172 | [Document 1](document_1.txt); [Document 2](document_2.txt) |
| Inter-annotator agreement (averaged weighted kappa) | 0.874 | [Document 1](document_1.txt) |
| Train / validation / test split | 80% / 10% / 10% | [Document 1](document_1.txt) |

### 2.1 Number of dialogs

The single most direct statement of corpus size appears in the dataset section of the primary source: "We collected 220 human-human dialogs" ([Document 1](document_1.txt)). The third-party note, by contrast, states that "[t]he dataset contains 320 human-human dialogs" and that "[t]he total dataset comprises 320 human-human dialogs" ([Document 2](document_2.txt)). Both cannot be simultaneously correct for the same corpus, and the discrepancy is analyzed in Section 3.

### 2.2 Conversational turns

Average conversation length is reported as 12.45 turns ([Document 1](document_1.txt); [Document 2](document_2.txt)). Multiplying this mean by the number of dialogs yields a derived corpus-level turn count of approximately **2,739 turns** under the 220-dialog total, or approximately **3,984 turns** under the 320-dialog total. Both values are derived estimates and should be treated as approximations, since the underlying average is rounded to two decimal places and the multiplier is itself disputed.

### 2.3 Utterance length

Average utterance length is 11.13 words ([Document 1](document_1.txt); [Document 2](document_2.txt)). The figures for turns and utterance length are explicitly described in the third-party note as describing the *full* AntiScam corpus rather than only the annotated subset, which means they can legitimately be used to extrapolate corpus-wide totals ([Document 2](document_2.txt)).

### 2.4 Annotated sentences and the annotation subset

For annotation statistics, a subset of 100 dialogs containing 3,044 sentences was manually annotated by two expert annotators with linguistic training ([Document 1](document_1.txt); [Document 2](document_2.txt)). This is the most precisely specified size figure in the entire documentation: 100 dialogs and 3,044 sentences, independent of the disputed corpus total ([Document 1](document_1.txt); [Document 2](document_2.txt)). It implies roughly 30.44 sentences per annotated dialog.

### Table 2. Derived corpus-level estimates under each reported dialog total

| Derived quantity | Based on 220 dialogs | Based on 320 dialogs |
|---|---|---|
| Total turns (12.45 × N) | ≈ 2,739 | ≈ 3,984 |
| Total words (turns × 11.13) | ≈ 30,485 | ≈ 44,342 |
| Extrapolated sentence count (30.44 × N) | ≈ 6,697 | ≈ 9,741 |
| Annotated sentences as share of extrapolated corpus | ≈ 45.5% | ≈ 31.3% |
| Derived words per sentence | ≈ 4.6 | ≈ 4.6 |
| Train split (80%) | 176 dialogs | 256 dialogs |
| Validation split (10%) | 22 dialogs | 32 dialogs |
| Test split (10%) | 22 dialogs | 32 dialogs |

*Note.* All values in this table are derived by applying reported averages to reported dialog counts; they are not directly reported in either source.

The derived words-per-sentence value of approximately 4.6 is internally consistent under both totals, because it is computed from the paired averages (12.45 turns and 11.13 words) against the fixed 3,044 sentences per 100 dialogs. This consistency does not resolve the dialog-count dispute but does confirm that the reported averages and the annotation count are mutually coherent.

## 3. Reconciling the 220 Versus 320 Discrepancy

The conflict between the two sources is material: it is a difference of 100 dialogs, or approximately 45% of the smaller total. Three lines of evidence bear on which figure should be preferred.

### 3.1 Evidence favoring 220

The 220 figure appears in what is functionally the primary source: the dataset section of the underlying paper, including its own subsection headings (AntiScam Dataset, PersuasionForGood Dataset), experimental results tables, and evaluation-metric definitions ([Document 1](document_1.txt)). The statement is a first-person, authorial declaration of collection outcome—"We collected 220 human-human dialogs"—rather than a paraphrase or summary ([Document 1](document_1.txt)). Primary-source collection statements are generally more reliable for dataset sizing than derivative summaries, because the authors are describing their own data-collection procedure rather than reconstructing it.

### 3.2 Evidence favoring 320

The 320 figure is stated consistently across three separate blocks of the third-party note, including one that explicitly labels itself a "Third-party research note" ([Document 2](document_2.txt)). Internal consistency across repeated statements is a mild indicator of reliability. Additionally, the paper's own interpretive gloss is that "attackers are well trained and not too easily identifiable," which sits more comfortably with a 53.8% identification rate (172 of 320) than with a 78.2% identification rate (172 of 220). A corpus in which nearly four in five users correctly identified the attacker is arguably not one in which attackers are "not too easily identifiable."

### Table 3. Attack-identification rates under each reported denominator

| Reported denominator | Users identifying attacker | Success rate |
|---|---|---|
| 220 dialogs | 172 | 78.2% |
| 320 dialogs | 172 | 53.8% |

### 3.3 Assessment

Weighing these considerations, this report adopts **220 dialogs as the primary, best-supported figure**, because the direct, first-person, primary-source collection statement carries greater evidentiary weight than the repeated but derivative third-party restatements. The interpretation-based argument favoring 320 (the "well trained" attackers gloss) is suggestive but not decisive, since 78.2% success can still be described as falling short of perfect detection. Users of the dataset should nonetheless treat the corpus size as **unsettled between 220 and 320 dialogs** and should verify against the released data before reporting either number. What can be stated with confidence is that AntiScam is a **mid-sized, human-collected dialog corpus on the order of a few hundred conversations**, containing roughly 2,700–4,000 conversational turns and roughly 30,000–44,000 words by extrapolation from its reported averages ([Document 1](document_1.txt); [Document 2](document_2.txt)).

## 4. Label Space: A Second Dimension of Size

Dataset "size" is not only a matter of raw volume; it also includes the size of the annotation label space. The primary source presents a hierarchical intent annotation scheme applied to both AntiScam and PersuasionForGood ([Document 1](document_1.txt)). The scheme separates on-task intents, which are task-specific, from off-task intents, which are general across non-collaborative tasks ([Document 1](document_1.txt)). For AntiScam, the on-task intents are *elicitation*, *providing_information*, and *refusal*; for PersuasionForGood, the on-task intents include *agree_donation*, *disagree_donation*, *disagree_donation_more*, *ask_donation_amount*, *ask_donate_more*, *proposition_of_donation*, *offer_confirm_donation*, *seek_confirm_donation*, and *provide_donation_amount* ([Document 1](document_1.txt)). The shared off-task inventory consists of *open_question*, *yes_no_question*, *negative_answer*, *positive_answer*, *responsive_statement*, *nonresponsive_statement*, *greeting*, *thanking*, *respond_to_thank*, *apology*, *closing*, and *hold* ([Document 1](document_1.txt)). The three AntiScam on-task intents were applied across the 3,044 annotated sentences in the 100-dialog subset ([Document 1](document_1.txt)).

## 5. How the Corpus Size Is Used: Data Partitioning and Evaluation

The corpus size directly determines the experimental partition. The authors used 80% of the data for training, 10% for validation, and 10% for testing, with further training details relegated to an appendix ([Document 1](document_1.txt)). Under the 220-dialog reading, this yields approximately 176 training dialogs, 22 validation dialogs, and 22 test dialogs; under the 320-dialog reading, it yields 256, 32, and 32 respectively. Because the same averages were used to derive both columns, neither can be treated as reported fact.

The corpus size also underpins the reported benchmark results. On AntiScam, MISSA achieved a perplexity of 21.07, while TransferTransfo reached 32.96, Hybrid 32.0% on response intent precision (with perplexity not reported), MISSA-sel 30.54, and MISSA-con 24.46 ([Document 1](document_1.txt)). Human evaluation scores showed MISSA leading on fluency (4.18), coherence (3.75), engagement (3.69), length (14.9), and TaskSuc (1.294) ([Document 1](document_1.txt)). These results are only as generalizable as the underlying corpus is large, which is precisely why the 220-versus-320 ambiguity matters for downstream readers.

## 6. Distinguishing the Corpus From Its Human-Evaluation Set

A common source of confusion when sizing AntiScam is the human-evaluation data, which is a separate artifact from the corpus itself. For human evaluation, the authors tested their models and baselines with 15 college-student volunteers, each of whom pretended to be an attacker and interacted with all models at least three times to avoid randomness, producing 225 collected dialogs in total ([Document 1](document_1.txt)). Each model received 45 human ratings, and the average score was reported as the final human-evaluation score ([Document 1](document_1.txt)).

### Table 4. Human-evaluation data collected (distinct from the AntiScam corpus)

| Item | Value | Source |
|---|---|---|
| Volunteers | 15 college students | [Document 1](document_1.txt) |
| Models compared | 5 | [Document 1](document_1.txt) |
| Minimum rounds per volunteer per model | 3 | [Document 1](document_1.txt) |
| Total evaluation dialogs collected | 225 | [Document 1](document_1.txt) |
| Ratings per model | 45 | [Document 1](document_1.txt) |

The 225-dialog evaluation set must not be conflated with the 220- or 320-dialog AntiScam corpus; the numerical proximity of 220 and 225 is coincidental and the two datasets serve entirely different purposes ([Document 1](document_1.txt)).

## 7. Comparative Context

AntiScam was evaluated alongside PersuasionForGood, an existing dataset that also targets a non-collaborative task, namely persuading people to donate to a charity ([Document 1](document_1.txt)). The two datasets share the off-task intent inventory but differ in their on-task intents, reflecting the differing objectives of defending against an attacker versus soliciting a donation ([Document 1](document_1.txt)). AntiScam's role in the literature is therefore that of a task-specific complement to an existing non-collaborative resource, and its size should be read in that comparative frame: it is a newly collected corpus rather than a large-scale aggregation ([Document 1](document_1.txt)).

## 8. Implications of the Reported Size

Several conclusions follow from the sizing evidence. First, AntiScam is a **specialist, mid-scale corpus**, not a large-scale one; its value lies in its novel non-collaborative task framing rather than in raw volume ([Document 1](document_1.txt)). Second, its annotation depth is unusually high relative to its raw size: 100 dialogs and 3,044 sentences were labeled by two linguistically trained experts who achieved a 0.874 averaged weighted kappa, indicating strong agreement ([Document 1](document_1.txt)). Under either dialog total, the annotated subset represents a substantial fraction of the corpus—approximately 45.5% of 220 dialogs or 31.3% of 320 dialogs. Third, the documentation contains an unresolved inconsistency in the reported total, and any rigorous downstream use of the dataset should therefore report the specific figures it relies on (e.g., 3,044 annotated sentences in 100 dialogs) rather than a single disputed dialog count.

## 9. Conclusion

The AntiScam dataset is a human–human anti-scam dialog corpus collected via a role-playing Amazon customer-service scam scenario on Amazon Mechanical Turk ([Document 1](document_1.txt); [Document 2](document_2.txt)). Its size is reported as **220 human–human dialogs** in the primary source ([Document 1](document_1.txt)) and as **320 human–human dialogs** in derivative third-party material ([Document 2](document_2.txt)). This report concludes that **220 is the better-supported figure**, given that it originates in a direct, first-person authorial statement about the collection process, while acknowledging that the corpus should be regarded as falling somewhere in the 220-to-320 range until verified against the released data. Both sources agree on the corpus's conversational profile—12.45 turns per conversation and 11.13 words per utterance—and both agree that a 100-dialog subset containing 3,044 sentences was annotated by two linguistically trained experts, with an averaged weighted kappa of 0.874 ([Document 1](document_1.txt); [Document 2](document_2.txt)). In practical terms, AntiScam is a corpus of a few hundred conversations, roughly 2,700–4,000 turns, roughly 30,000–44,000 words, and about 3,000 densely annotated sentences—designed not to be large, but to be a well-annotated, human-collected example of the under-resourced non-collaborative dialog task.

## References

Document 1. (n.d.). *AntiScam dataset, experiments, and annotation scheme* [Excerpt from the End-to-End Trainable Non-Collaborative Dialog System paper]. document_1.txt.

Document 2. (n.d.). *AntiScam corpus size and annotation statistics* [Third-party research note]. document_2.txt.