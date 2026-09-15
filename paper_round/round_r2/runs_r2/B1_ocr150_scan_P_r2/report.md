# How Large Is the ANTISCAM Dataset? A Detailed Assessment of Reported Corpus Size and Annotation Scale

## Executive Summary

The ANTISCAM dataset is a human–human, non-collaborative dialogue corpus built from a role-playing Amazon customer service scam scenario collected on Amazon Mechanical Turk ([Li et al., 2020](https://gitlab.com/ucdavisnlp/antiscam)). The two documents supplied here disagree on one central figure: the primary paper states that the corpus comprises **220 human–human dialogs** ([Li et al., 2020](https://gitlab.com/ucdavisnlp/antiscam)), whereas the third-party research note states that it comprises **320 human–human dialogs** ([Third-Party Research Note, n.d.](document_2.txt)). Every other headline statistic — 100 annotated dialogs, 3,044 annotated sentences, 12.45 average turns per conversation, 11.13 average words per utterance, and 172 users who successfully identified their partner as an attacker — is identical across both documents ([Li et al., 2020](https://gitlab.com/ucdavisnlp/antiscam); [Third-Party Research Note, n.d.](document_2.txt)).

On the balance of the evidence, the defensible answer is that **ANTISCAM contains 220 human–human dialogs**, with a manually annotated subset of 100 dialogs containing 3,044 sentences. The 320 figure appears to be unsupported and internally inconsistent with the paper's own qualitative and quantitative claims, as argued in detail below.

## What the ANTISCAM Dataset Is

ANTISCAM was created to fill a gap in non-collaborative dialogue research. Prior end-to-end task-oriented dialogue systems had been optimized for collaborative tasks — restaurant reservations, bus timetable retrieval — where the user and system pursue an identical goal. Non-collaborative settings, such as negotiation, deception, and persuasion, invert that assumption: the two parties do not share a goal, and social or off-task content becomes strategically important ([Li et al., 2020](https://gitlab.com/ucdavisnlp/antiscam)).

To study this, the authors posted a role-playing task on Amazon Mechanical Turk in which one worker played an attacker impersonating Amazon customer service to extract personal information, and the other played an ordinary user tasked with protecting their own data and, once suspicious, wasting the attacker's time and eliciting the attacker's information ([Li et al., 2020](https://gitlab.com/ucdavisnlp/antiscam)). Workers could not see each other's instructions, and each worker could participate only once, which prevents prior knowledge of the partner's goals ([Li et al., 2020](https://gitlab.com/ucdavisnlp/antiscam)).

## Reported Corpus Size: The Two Competing Figures

### The Primary Source Position: 220 Dialogs

The paper's appendix, which describes the anti-scam collection setting, states directly: "We collected 220 human-human dialogs" ([Li et al., 2020](https://gitlab.com/ucdavisnlp/antiscam)). The main body repeats this figure when reporting identification rates: "Only 172 out of 220 users successfully identified their partner as an attacker, suggesting that the attackers are well trained and not too easily identifiable" ([Li et al., 2020](https://gitlab.com/ucdavisnlp/antiscam)).

This figure is stated twice, in two different sections, and is used as the denominator for a qualitative interpretation of attacker quality. It is therefore not a passing mention but a load-bearing statistic.

### The Third-Party Position: 320 Dialogs

The third-party research note asserts the corpus "contains 320 human-human dialogs" and repeats the claim in its summary section, stating that "the paper reports that 172 out of 320 users successfully identified their partner as an attacker" ([Third-Party Research Note, n.d.](document_2.txt)).

Notably, however, the note reproduces every other statistic verbatim from the paper — 100 annotated dialogs, 3,044 sentences, two expert annotators with linguistic training, 12.45 average turns, 11.13 average words ([Third-Party Research Note, n.d.](document_2.txt)). The only deviation is the total dialog count.

## Side-by-Side Comparison of Reported Figures

| Metric | Primary paper (`document_1.txt`) | Third-party note (`document_2.txt`) | Agreement |
|---|---|---|---|
| Total human–human dialogs | 220 | 320 | **Conflict** |
| Users identifying attacker | 172 of 220 (78.2%) | 172 of 320 (53.8%) | **Conflict (denominator)** |
| Manually annotated dialogs | 100 | 100 | Agree |
| Manually annotated sentences | 3,044 | 3,044 | Agree |
| Expert annotators | 2, with linguistic training | 2, with linguistic training | Agree |
| Annotator agreement (weighted kappa) | 0.874 | Not reported | — |
| Average conversation length | 12.45 turns | 12.45 turns | Agree |
| Average utterance length | 11.13 words | 11.13 words | Agree |
| Collection platform | Amazon Mechanical Turk | Amazon Mechanical Turk | Agree |
| Scenario | Amazon customer service scam role-play | Amazon customer service scam role-play | Agree |

*Sources: ([Li et al., 2020](https://gitlab.com/ucdavisnlp/antiscam); [Third-Party Research Note, n.d.](document_2.txt)).*

## Derived Estimates of Corpus Scale

Because the two documents agree on turn length, utterance length, and annotation counts, it is possible to derive approximate measures of total corpus scale. These are my own calculations based on the reported averages and should be treated as estimates rather than reported figures.

| Derived quantity | Value | Basis (own calculation) |
|---|---|---|
| Total turns across full corpus | ≈ 2,739 turns | 220 dialogs × 12.45 turns ([Li et al., 2020](https://gitlab.com/ucdavisnlp/antiscam)) |
| Sentences per annotated dialog | ≈ 30.4 | 3,044 sentences ÷ 100 dialogs ([Li et al., 2020](https://gitlab.com/ucdavisnlp/antiscam)) |
| Sentences per turn (annotated subset) | ≈ 2.4 | 30.4 ÷ 12.45 turns ([Li et al., 2020](https://gitlab.com/ucdavisnlp/antiscam)) |
| Projected sentences across full corpus | ≈ 6,700 sentences | 2,739 turns × 2.4 sentences/turn (own projection) |
| Unique worker participants | ≈ 440 | 220 dialogs × 2 roles, one participation per worker ([Li et al., 2020](https://gitlab.com/ucdavisnlp/antiscam)) |
| Annotated subset as share of corpus | ≈ 45.5% | 100 ÷ 220 dialogs (own calculation) |

Under the third-party note's 320-dialog figure, the same arithmetic yields ≈ 3,984 turns, ≈ 9,700 projected sentences, ≈ 640 unique participants, and an annotated share of only ≈ 31.3% ([Third-Party Research Note, n.d.](document_2.txt)). These derived values are presented only to show how consequential the disputed numerator is; they are not reported by either source.

## Scale of the Annotation Layer

The manually annotated subset of ANTISCAM is a meaningfully large annotation effort in its own right. Two expert annotators with linguistic training labeled **3,044 sentences across 100 dialogs**, achieving an average weighted kappa of **0.874**, which indicates strong inter-annotator agreement ([Li et al., 2020](https://gitlab.com/ucdavisnlp/antiscam)).

Annotation operated at the sentence level rather than the turn level, meaning each conversation turn was segmented into individual sentences that were then labeled ([Li et al., 2020](https://gitlab.com/ucdavisnlp/antiscam)). The scheme is hierarchical, separating on-task from off-task intents:

- **On-task intents (ANTISCAM):** elicitation, providing-information, refusal ([Li et al., 2020](https://gitlab.com/ucdavisnlp/antiscam)).
- **On-task intents (PERSUASIONFORGOOD):** nine donation-related intents, including proposition of donation, confirm donation, agree donation, ask donate more, provide donation amount, ask donation amount, disagree donation, and disagree donation more ([Li et al., 2020](https://gitlab.com/ucdavisnlp/antiscam)).
- **Off-task general intents:** open question, yes/no question, positive answer, negative answer, responsive statement, non-responsive statement ([Li et al., 2020](https://gitlab.com/ucdavisnlp/antiscam)).
- **Off-task social intents:** greeting, closing, apology, thanking, respond to thank, hold ([Li et al., 2020](https://gitlab.com/ucdavisnlp/antiscam)).
- **Semantic slots (ANTISCAM):** 13 main slots, including name, address, card number, card CVS, card date, phone number, account detail, identity, payment, card info, order detail, order update, and others ([Li et al., 2020](https://gitlab.com/ucdavisnlp/antiscam)).

## Why the Discrepancy Matters, and Which Figure to Trust

The disagreement between 220 and 320 is not cosmetic. It changes the denominator of the dataset's most quoted behavioral statistic: the proportion of users who detected the attacker. At 172 of 220, the detection rate is **78.2%**; at 172 of 320, it is **53.8%** ([Li et al., 2020](https://gitlab.com/ucdavisnlp/antiscam); [Third-Party Research Note, n.d.](document_2.txt)). The paper uses the higher detection rate to argue that "attackers are well trained and not too easily identifiable," a framing that is far more coherent when the denominator is 220 ([Li et al., 2020](https://gitlab.com/ucdavisnlp/antiscam)) — the authors treat 172 as a noteworthy shortfall ("only 172"), which only reads naturally if the base is 220, not 320.

My considered assessment is that **220 is the correct total**. Three reasons support this:

1. **Source hierarchy.** The primary paper is the origin of the dataset and states the figure twice, in both the main text and the appendix ([Li et al., 2020](https://gitlab.com/ucdavisnlp/antiscam)). The third-party note is a derived summary that reproduces all other statistics faithfully but alters exactly one number ([Third-Party Research Note, n.d.](document_2.txt)).
2. **Internal consistency.** The note itself claims "These averages describe the full AntiScam corpus" and "The total dataset comprises 320 human-human dialogs," yet it also borrows the 12.45-turn and 11.13-word averages directly from the paper's description of the 220-dialog corpus ([Third-Party Research Note, n.d.](document_2.txt)). Mixing an altered corpus size with unaltered corpus-level averages produces an internally inconsistent description.
3. **Narrative coherence.** As argued above, the "only 172 of 220" framing supports the paper's interpretation of attacker quality; the "172 of 320" framing does not ([Li et al., 2020](https://gitlab.com/ucdavisnlp/antiscam)).

The most plausible explanation for the third-party error is a transcription or summarization slip in which a different numeral was substituted for the correct total while the surrounding statistics were copied verbatim ([Third-Party Research Note, n.d.](document_2.txt)).

## Contextualizing the Scale Against a Comparable Corpus

To judge whether ANTISCAM is "large" or "small," it helps to compare it with the other non-collaborative dataset used in the same paper, PERSUASIONFORGOOD ([Wang et al., 2019](https://gitlab.com/ucdavisnlp/antiscam)).

| Dataset | Dialogs | Act-annotated dialogs | Avg. turns | Vocabulary |
|---|---|---|---|---|
| ANTISCAM | 220 (disputed: 320) | 100 dialogs / 3,044 sentences | 12.45 | Not reported |
| PERSUASIONFORGOOD | 1,017 | 300 | 10.43 | 8,141 |

*Sources: ([Li et al., 2020](https://gitlab.com/ucdavisnlp/antiscam); [Third-Party Research Note, n.d.](document_2.txt)).*

ANTISCAM is therefore roughly one-fifth the total dialog count of PERSUASIONFORGOOD (220 ÷ 1,017 ≈ 21.6%, my calculation), but its conversations run longer on average (12.45 versus 10.43 turns) and it carries a bespoke hierarchical annotation layer rather than being adapted from an existing dialog-act scheme ([Li et al., 2020](https://gitlab.com/ucdavisnlp/antiscam)). The paper explicitly positions ANTISCAM as filling a dataset gap, noting that non-collaborative tasks are "relatively new to the study of dialog systems" and that there are "insufficiently many meaningful datasets for evaluation" ([Li et al., 2020](https://gitlab.com/ucdavisnlp/antiscam)).

## How the Dataset Was Used at Scale in Evaluation

Beyond the corpus itself, the paper reports a substantial human evaluation built on top of the 220-dialog dataset. Fifteen college-student volunteers each interacted with five models (TransferTransfo, Hybrid, MISSA, MISSA-sel, MISSA-con) at least three times, producing 225 collected dialogs and 45 human ratings per model ([Li et al., 2020](https://gitlab.com/ucdavisnlp/antiscam)). MISSA maintained conversations averaging 14.9 turns versus 8.5 for the vanilla TransferTransfo baseline, and achieved a higher task success score (1.294 versus 1.025) ([Li et al., 2020](https://gitlab.com/ucdavisnlp/antiscam)). Training used an 80/10/10 split of the corpus ([Li et al., 2020](https://gitlab.com/ucdavisnlp/antiscam)).

The annotated subset also revealed meaningful intent asymmetries: users produced more refusals than attackers (74 versus 19), asked more open questions (173 versus 54) and more yes/no questions (165 versus 117), and both roles generated substantial social content (292 and 252 social sentences respectively) ([Li et al., 2020](https://gitlab.com/ucdavisnlp/antiscam)).

## Conclusion

ANTISCAM is a **220-dialog** human–human anti-scam corpus collected via a role-playing Amazon customer service scam on Amazon Mechanical Turk, containing approximately 2,739 conversation turns and roughly 6,700 sentences by projection, with a manually annotated subset of **100 dialogs and 3,044 sentences** labeled by two expert annotators at a weighted kappa of 0.874 ([Li et al., 2020](https://gitlab.com/ucdavisnlp/antiscam)). A third-party research note reports 320 dialogs, but this figure is uncorroborated, inconsistent with the paper's own qualitative framing of the 172-user detection statistic, and contradicted by the paper's repeated statement of the 220 total ([Third-Party Research Note, n.d.](document_2.txt); [Li et al., 2020](https://gitlab.com/ucdavisnlp/antiscam)). Anyone citing ANTISCAM should use **220 dialogs** as the corpus size, **100 dialogs / 3,044 sentences** as the annotated subset, and **172 of 220 (78.2%)** as the user detection rate — while flagging the 320 figure as a likely secondary-source error.

## References

Li, Y., Qian, K., Shi, W., & Yu, Z. (2020). *End-to-end trainable non-collaborative dialog system* [document_1.txt]. University of California, Davis. https://gitlab.com/ucdavisnlp/antiscam

Third-party research note: End-to-end trainable non-collaborative dialog system [document_2.txt]. (n.d.).