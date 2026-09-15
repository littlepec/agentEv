# How Big Is the AntiScam Dataset? A Sizing and Composition Report

## Executive Summary

The AntiScam dataset is a human–human, non-collaborative dialogue corpus built around a role-played Amazon customer-service scam scenario and collected on Amazon Mechanical Turk ([Li et al., 2019](https://arxiv.org/abs/1911.10742)). Based on the primary evidence available, the dataset comprises **220 human–human dialogs**, with an **average conversation length of 12.45 turns** and an **average utterance length of 11.13 words** ([Li et al., 2019](https://arxiv.org/abs/1911.10742)). A subset of **100 dialogs containing 3,044 sentences** was manually annotated by two expert linguistic annotators, achieving a **0.874 averaged weighted kappa** ([Li et al., 2019](https://arxiv.org/abs/1911.10742)).

A secondary, third-party research note circulating with the paper reports the corpus size as **320 human–human dialogs** and correspondingly states that "172 out of 320 users" identified their partner as an attacker ([Third-party research note, n.d.](https://arxiv.org/abs/1911.10742)). This report evaluates both figures, weighs their reliability, and concludes — on the balance of evidence — that **220 is the correct dataset size**, and that the 320 figure in the secondary note is an error introduced in restatement rather than a revised or corrected statistic. This determination is explained in detail in the section "Reconciling the 220 and 320 Figures" below.

## Background and Provenance of the Corpus

The AntiScam corpus was created to address a documented shortage of datasets suitable for non-collaborative dialogue research. The authors observe that non-collaborative tasks — negotiation, persuasion, and deception-oriented interaction — were still new to dialogue-systems research, and that "there are insufficiently many meaningful datasets for evaluation" ([Li et al., 2019](https://arxiv.org/abs/1911.10742)). AntiScam was therefore proposed explicitly as a benchmark resource for such tasks, designed so that on-task and off-task content would be deliberately interleaved within conversations ([Li et al., 2019](https://arxiv.org/abs/1911.10742)).

The collection procedure is consequential for interpreting the corpus size. Two workers were randomly paired on Amazon Mechanical Turk: one assigned the role of "attacker" (pretending to be Amazon customer service and eliciting personal information) and the other assigned the role of an everyday user who protects their own information and, upon detecting the attacker, attempts to extract the attacker's information and prolong the exchange ([Li et al., 2019](https://arxiv.org/abs/1911.10742)). Both workers received specific synthetic personal data; the attacker additionally received training on elicitation tactics; workers could not see each other's instructions; and each worker could participate only once, so that no participant could learn their partner's goals in advance ([Li et al., 2019](https://arxiv.org/abs/1911.10742)). This one-shot, randomized pairing design is what makes the reported total dialog count the meaningful unit of dataset size.

## The Headline Number: Total Dialog Count

### The primary figure: 220 dialogs

The primary source states the corpus size twice, in two structurally separate passages. In the dataset description, it reports: "We collected 220 human-human dialogs" ([Li et al., 2019](https://arxiv.org/abs/1911.10742)). In the appendix section on collection setting, it repeats: "We collected 220 human-human dialogs. The average conversation length is 12.45 turns and the average utterance length is 11.13 words" ([Li et al., 2019](https://arxiv.org/abs/1911.10742)). The same passage then reports that "Only 172 out of 220 users successfully identified their partner as an attacker" ([Li et al., 2019](https://arxiv.org/abs/1911.10742)).

The internal arithmetic of the primary source is fully self-consistent: 172 successes out of 220 total participants yields a detection rate of approximately 78.2%, and leaves 48 participants who failed to identify their partner ([Li et al., 2019](https://arxiv.org/abs/1911.10742)).

### The secondary figure: 320 dialogs

The third-party research note reports, repeatedly and in multiple formulations, that "the dataset contains 320 human-human dialogs," that "the total dataset comprises 320 human-human dialogs," and that "172 out of 320 users successfully identified their partner as an attacker" ([Third-party research note, n.d.](https://arxiv.org/abs/1911.10742)). The note is otherwise aligned with the primary source on annotation statistics — 100 dialogs, 3,044 sentences, two expert annotators, 12.45 turns, 11.13 words ([Third-party research note, n.d.](https://arxiv.org/abs/1911.10742)).

### Reconciling the 220 and 320 Figures

The two sources conflict on a single scalar, and the conflict is systematically traceable. Three lines of reasoning support 220 as authoritative and 320 as erroneous.

First, **source hierarchy**. The primary document is the paper's own text, in which the authors describe a corpus they themselves collected, and it states the figure in two separate places with matching conversational statistics and a matching success count ([Li et al., 2019](https://arxiv.org/abs/1911.10742)). The secondary document is a restatement — a "third-party research note" whose own framing is that it is summarizing and reporting what "the paper reports" ([Third-party research note, n.d.](https://arxiv.org/abs/1911.10742)). In any evidentiary contest between an original record and a derivative summary, the original record governs.

Second, **the denominator coupling**. In the primary source, the success count (172) is bound to the corpus size (220) within a single sentence ([Li et al., 2019](https://arxiv.org/abs/1911.10742)). In the secondary note, the identical count (172) is bound to 320 ([Third-party research note, n.d.](https://arxiv.org/abs/1911.10742)). Because the numerator is unchanged, the substitution of a larger denominator materially changes the substantive finding: a detection rate of roughly 78% becomes roughly 54%. The primary source's interpretive gloss — that attackers "are well trained and not too easily identifiable" — sits more naturally with a high detection rate among users who were actively instructed to make that judgment, and the note's own gloss relies on the same sentence ([Li et al., 2019](https://arxiv.org/abs/1911.10742); [Third-party research note, n.d.](https://arxiv.org/abs/1911.10742)). The change in implication is itself a reason to be skeptical of the derivative number.

Third, **zero corroboration in the primary text**. No passage in the primary document anywhere reports 320 dialogs, 320 users, or any count of 320 in connection with AntiScam ([Li et al., 2019](https://arxiv.org/abs/1911.10742)). The secondary note supplies no independent collection record, no separate appendix reference, and no rationale for a discrepancy ([Third-party research note, n.d.](https://arxiv.org/abs/1911.10742)).

**Determination:** based on the evidence provided, AntiScam's size is **220 human–human dialogs**, and any size-related downstream statistic — most notably the attacker-detection rate — should be computed against 220, not 320.

**Table 1. Conflicting size claims and their support**

| Attribute | Primary paper ([Li et al., 2019](https://arxiv.org/abs/1911.10742)) | Third-party note ([Third-party research note, n.d.](https://arxiv.org/abs/1911.10742)) | Assessment |
|---|---|---|---|
| Total human–human dialogs | 220 | 320 | Primary figure adopted |
| Statements of the count | Two separate passages | Multiple, mutually redundant | Primary is internally varied in location, not in value |
| Success count (users identifying attacker) | 172 of 220 | 172 of 320 | Numerator agrees; denominator is the point of divergence |
| Implied detection rate | ~78.2% | ~54% (as stated, ~53.75%) | Discrepancy is material, not cosmetic |
| Supporting turn/length averages | 12.45 turns; 11.13 words | 12.45 turns; 11.13 words | Agree; averages describe the full corpus |
| Independent corroboration of the larger figure | None | None | No basis to prefer 320 |

## Turn-Level and Utterance-Level Size

Raw dialog count understates or overstates corpus scale depending on conversational depth, so the reported averages matter for sizing. AntiScam's average conversation length of 12.45 turns and average utterance length of 11.13 words ([Li et al., 2019](https://arxiv.org/abs/1911.10742)) provide the parameters for estimating the corpus's overall volume.

Applying these averages to the adopted 220-dialog count yields an approximate corpus of **2,739 conversational turns** and roughly **30,500 words** of dialogue. These derived figures are estimates computed from the paper's reported averages and are not reported totals in the source; they are presented here to convey order of magnitude rather than as citable dataset statistics ([Li et al., 2019](https://arxiv.org/abs/1911.10742)).

**Table 2. Sizing dimensions of AntiScam**

| Dimension | Reported / derived value | Status |
|---|---|---|
| Total human–human dialogs | 220 | Reported ([Li et al., 2019](https://arxiv.org/abs/1911.10742)) |
| Average conversation length | 12.45 turns | Reported ([Li et al., 2019](https://arxiv.org/abs/1911.10742)) |
| Average utterance length | 11.13 words | Reported ([Li et al., 2019](https://arxiv.org/abs/1911.10742)) |
| Approximate total turns | ~2,739 | Derived estimate |
| Approximate total words | ~30,500 | Derived estimate |
| Annotated subset (dialogs) | 100 | Reported ([Li et al., 2019](https://arxiv.org/abs/1911.10742)) |
| Annotated subset (sentences) | 3,044 | Reported ([Li et al., 2019](https://arxiv.org/abs/1911.10742)) |
| Sentences per annotated dialog | ~30.4 | Derived estimate |
| Annotators | 2 expert, linguistically trained | Reported ([Li et al., 2019](https://arxiv.org/abs/1911.10742)) |
| Inter-annotator agreement | 0.874 averaged weighted kappa | Reported ([Li et al., 2019](https://arxiv.org/abs/1911.10742)) |

## Annotation Coverage: Differences Between Corpus Size and Annotated Size

A critical distinction for anyone citing "the size of AntiScam" is that the annotated portion is substantially smaller than the collected corpus. The corpus is 220 dialogs, but only 100 dialogs — 3,044 sentences — received manual annotation ([Li et al., 2019](https://arxiv.org/abs/1911.10742)). That is roughly 45% of the corpus by dialog count.

This two-tier structure follows directly from the annotation design. The authors segment each conversation turn into individual sentences and annotate at the sentence level rather than the turn level, precisely so that on-task and off-task intents can be decoupled ([Li et al., 2019](https://arxiv.org/abs/1911.10742)). Sentence-level annotation under a hierarchical scheme — on-task intents, off-task general intents, off-task social intents, and 13 semantic slots — is labor-intensive, which plausibly explains why annotation was scoped to a 100-dialog subset rather than the full 220 ([Li et al., 2019](https://arxiv.org/abs/1911.10742)).

The annotation layer also quantifies what kind of content populates the corpus. The authors report that users produced more refusals than attackers (74 vs. 19); that users asked more open questions (173 vs. 54) and more yes/no questions (165 vs. 117); and that both roles produced substantial social content (292 and 252 instances respectively) ([Li et al., 2019](https://arxiv.org/abs/1911.10742)). These counts, drawn from the annotated subset, confirm that a large share of the corpus is off-task — which the authors present as the justification for the hierarchical on-task/off-task scheme ([Li et al., 2019](https://arxiv.org/abs/1911.10742)).

## Comparative Sizing: AntiScam Versus PersuasionForGood

Sizing AntiScam in isolation is less informative than placing it against the other non-collaborative dataset used in the same study. PersuasionForGood is markedly larger in raw dialog count — 1,017 dialogs, of which 300 were annotated with dialog acts, with an average conversation length of 10.43 and a vocabulary of 8,141 words ([Li et al., 2019](https://arxiv.org/abs/1911.10742)).

**Table 3. AntiScam and PersuasionForGood compared on size-related dimensions**

| Dimension | AntiScam | PersuasionForGood |
|---|---|---|
| Total dialogs | 220 ([Li et al., 2019](https://arxiv.org/abs/1911.10742)) | 1,017 ([Li et al., 2019](https://arxiv.org/abs/1911.10742)) |
| Annotated dialogs | 100 ([Li et al., 2019](https://arxiv.org/abs/1911.10742)) | 300 ([Li et al., 2019](https://arxiv.org/abs/1911.10742)) |
| Annotated sentences | 3,044 ([Li et al., 2019](https://arxiv.org/abs/1911.10742)) | Not specified in provided source |
| Average conversation length | 12.45 turns ([Li et al., 2019](https://arxiv.org/abs/1911.10742)) | 10.43 turns ([Li et al., 2019](https://arxiv.org/abs/1911.10742)) |
| Vocabulary size | Not specified in provided source | 8,141 ([Li et al., 2019](https://arxiv.org/abs/1911.10742)) |
| Collection platform | Amazon Mechanical Turk ([Li et al., 2019](https://arxiv.org/abs/1911.10742)) | Amazon Mechanical Turk ([Li et al., 2019](https://arxiv.org/abs/1911.10742)) |

The comparison yields a nuanced picture of "size." AntiScam is smaller by dialog count — roughly one-fifth the scale of PersuasionForGood — but longer per conversation (12.45 turns versus 10.43) and more heavily annotated in absolute sentence terms, at 3,044 annotated sentences ([Li et al., 2019](https://arxiv.org/abs/1911.10742)). The authors frame AntiScam not as a large corpus but as a purpose-designed one: unlike prior non-collaborative datasets, it is explicitly constructed so that on-task and off-task content are entangled in ways that can be disentangled and measured, positioning it as a benchmark rather than a bulk data resource ([Li et al., 2019](https://arxiv.org/abs/1911.10742)).

## Experimental Footprint as a Size Signal

The scale of evaluation reported alongside the dataset provides indirect corroboration of dataset size. The authors partition data using 80% for training, 10% for validation, and 10% for testing ([Li et al., 2019](https://arxiv.org/abs/1911.10742)). Applied to 220 dialogs, this implies roughly 176 training dialogs, 22 validation dialogs, and 22 test dialogs; applied to the annotated 100-dialog subset, it implies roughly 80/10/10. Either way, the evaluation operates on a corpus in the low hundreds of dialogs, not the many hundreds ([Li et al., 2019](https://arxiv.org/abs/1911.10742)).

The human evaluation adds a separate, adjacent dataset of its own: 15 college-student volunteers role-playing as attackers, each interacting with all models at least three times, producing 225 collected dialogs, with each model receiving 45 ratings across five models ([Li et al., 2019](https://arxiv.org/abs/1911.10742)). This evaluation corpus is comparable in magnitude to the underlying AntiScam collection itself, which is consistent with a dataset in the low hundreds.

## Why the Size Determination Matters

The 220-versus-320 question is not a pedantic one, because at least one substantive claim depends on the denominator. The paper's assessment of attacker quality rests on the proportion of users who failed to detect them ([Li et al., 2019](https://arxiv.org/abs/1911.10742)). At 220, the failure rate is roughly 22%; at 320, it would be roughly 46%. Those two characterizations support very different conclusions about how easily the attackers were identified, and by extension about how difficult the deception task in the corpus actually was. Adopting the primary figure preserves the paper's stated interpretation and keeps reported statistics internally consistent ([Li et al., 2019](https://arxiv.org/abs/1911.10742)).

Size also bears on generalization claims. The authors position AntiScam as a benchmark and report that their model outperforms baselines on both AntiScam and PersuasionForGood, which they present as evidence that the approach transfers across non-collaborative tasks ([Li et al., 2019](https://arxiv.org/abs/1911.10742)). The authors also acknowledge a substantive limitation in their model — that it "still produces responses that are not consistent with their distant conversation history as GPT can only track a limited history span" ([Li et al., 2019](https://arxiv.org/abs/1911.10742)). With a corpus of 220 dialogs and a 100-dialog annotated subset, the statistical reach of the reported comparisons is inherently bounded, and readers should treat cross-task generalization claims as indicative rather than conclusive at this corpus scale.

## Limitations of the Sizing Evidence

Several caveats should attend any citation of AntiScam's size. The corpus is not accompanied, in the provided material, by a breakdown of dialog counts by split beyond the 80/10/10 ratio, nor by a total sentence or token count for the full 220 dialogs; the 3,044-sentence figure applies only to the annotated 100-dialog subset ([Li et al., 2019](https://arxiv.org/abs/1911.10742)). The derived estimates in Table 2 rest on multiplication of reported averages and should be treated as approximations. Finally, the corpus is human–human rather than human–system in its collection phase, with system behavior introduced only during the modeling and evaluation stages ([Li et al., 2019](https://arxiv.org/abs/1911.10742)).

## Conclusion

AntiScam is a compact, purpose-built, human–human non-collaborative dialogue corpus whose size is best stated as **220 dialogs**, averaging **12.45 turns** and **11.13 words per utterance**, with a **100-dialog, 3,044-sentence** annotated subset produced by two expert annotators at **0.874 weighted kappa** and a reported **172 of 220** users successfully identifying their attacker partner ([Li et al., 2019](https://arxiv.org/abs/1911.10742)). The competing 320-dialog figure in the third-party note is unsupported by the primary text, uncorroborated by any second passage, and inconsistently paired with an unchanged numerator of 172 ([Third-party research note, n.d.](https://arxiv.org/abs/1911.10742); [Li et al., 2019](https://arxiv.org/abs/1911.10742)). Researchers citing AntiScam should therefore use 220 as the corpus size, 100 dialogs and 3,044 sentences as the annotated footprint, and should note that the corpus is roughly one-fifth the dialog count of PersuasionForGood while being slightly longer per conversation ([Li et al., 2019](https://arxiv.org/abs/1911.10742)).

## References

Li, Y., Qian, K., Shi, W., & Yu, Z. (2019). *End-to-end trainable non-collaborative dialog system* (arXiv:1911.10742). arXiv. https://arxiv.org/abs/1911.10742

Third-party research note: End-to-end trainable non-collaborative dialog system (document_2.txt) [Unpublished research note]. (n.d.). Accompanying commentary on arXiv:1911.10742. https://arxiv.org/abs/1911.10742