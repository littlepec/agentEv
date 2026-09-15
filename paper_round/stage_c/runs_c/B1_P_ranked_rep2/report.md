# How Big Is the AntiScam Dataset? A Detailed Report on Corpus Size, Annotation Scope, and Structural Dimensions

## 1. Introduction and Scope of the Query

The question "How big is the AntiScam dataset?" is deceptively simple. A dataset's "size" in dialog-system research can be measured along at least five distinct axes: the number of raw conversations collected, the number of conversations that were manually annotated, the number of sentences or utterances those annotations cover, the average conversational depth (turns) and utterance length (words), and the volume of dialog generated for downstream human evaluation. This report addresses all of these dimensions for AntiScam, the human–human anti-scam dialog corpus introduced alongside the End-to-End Trainable Non-Collaborative Dialog System and the MISSA model ([Document 1](document_1.txt)). It also confronts an important discrepancy in the available evidence, in which two competing totals — 220 dialogs and 320 dialogs — appear for the same corpus ([Document 1](document_1.txt); [Document 2](document_2.txt)).

## 2. What AntiScam Is

AntiScam is a corpus of human–human anti-scam dialogs created to learn human elicitation strategies in non-collaborative dialog settings ([Document 1](document_1.txt); [Document 2](document_2.txt)). It was collected through a role-playing Amazon customer service scam scenario posted on Amazon Mechanical Turk, in which one participant plays an attacker attempting to extract personal information and the other defends against that attempt ([Document 1](document_1.txt); [Document 2](document_2.txt)). The authors describe the motivation for building it as filling a gap: "As non-collaborative tasks are still relatively new to the study of dialog systems, there are insufficiently many meaningful datasets for evaluation and we hope this provides a valuable example" ([Document 1](document_1.txt)). AntiScam therefore serves as both a research artifact and a size benchmark for a task category that was, at the time of publication, data-poor.

## 3. The Headline Figure: Total Number of Dialogs

### 3.1 The 320-Dialog Figure

The research notes state plainly that "AntiScam is a human-human anti-scam dialog corpus" whose "size is 320 human-human dialogs," and that "The dataset contains 320 human-human dialogs" ([Document 2](document_2.txt)). The same source repeats this total in its summary of annotation statistics, noting that the manually annotated subset comprises 100 dialogs and 3,044 sentences while the total dataset comprises 320 human-human dialogs ([Document 2](document_2.txt)). Under this reading, the annotated subset covers 31.25% of the full corpus.

### 3.2 The 220-Dialog Figure

The primary paper text contained in the first source provides a different number inside its dedicated "AntiScam Dataset" section:

> "We posted a role-playing task on the Amazon Mechanical Turk platform and collected a typing conversation dataset named AntiScam. We collected 220 human-human dialogs." ([Document 1](document_1.txt))

The same paragraph continues with the annotation and outcome statistics, reporting that only 172 out of 220 users successfully identified their partner as an attacker ([Document 1](document_1.txt)).

### 3.3 Assessment and Reasoned Position

Two figures cannot both describe the same collection event. In forming a position, three considerations carry weight:

1. **Source proximity.** The 220 figure appears within the paper's own verbatim dataset-construction narrative, in the same paragraph as the annotation procedure, the inter-annotator agreement, and the identification outcome ([Document 1](document_1.txt)). The 320 figure appears in summary notes that consistently frame statements as "the paper reports" ([Document 2](document_2.txt)), which indicates secondary rather than primary reporting.
2. **Internal consistency of the ratio.** The 220 figure is paired with "172 out of 220" in one contiguous passage ([Document 1](document_1.txt)), yielding a 78.2% identification rate. The 320 figure is paired with "172 out of 320" in the notes ([Document 2](document_2.txt)), yielding 53.75%. Only one pairing can be original to the paper.
3. **Qualitative fit.** The paper's gloss — that the attackers were "well trained and not too easily identifiable" ([Document 1](document_1.txt)) — fits a ~54% identification rate more naturally than a ~78% rate, which is an argument in favor of the 320/172 pairing and against my first two considerations.

Weighing these, my position is that **the corpus described in the paper's dataset section comprises 220 human–human dialogs, with 172 of those 220 users (78.2%) identifying their partner as an attacker** ([Document 1](document_1.txt)). The 320 total most plausibly reflects either a revised or expanded release of the corpus, or a transcription or summarization error propagated through repeated secondary notes ([Document 2](document_2.txt)). Because the discrepancy is material and unresolvable from the supplied evidence alone, the most defensible way to answer the query is: **AntiScam contains between 220 and 320 human–human dialogs, with 220 as the primary-source figure and 320 as the figure reported in secondary summaries** ([Document 1](document_1.txt); [Document 2](document_2.txt)).

## 4. Annotation Coverage: The Annotated Subset

Regardless of which corpus total is correct, the annotation statistics are reported consistently across both sources: a subset of **100 dialogs containing 3,044 sentences** was manually annotated ([Document 1](document_1.txt); [Document 2](document_2.txt)). Two expert annotators with linguistic training performed this annotation ([Document 1](document_1.txt); [Document 2](document_2.txt)). The annotated portion therefore represents:

| Metric | Value | Coverage of 220 dialogs | Coverage of 320 dialogs |
|---|---|---|---|
| Annotated dialogs | 100 ([Document 1](document_1.txt)) | 45.45% | 31.25% |
| Annotated sentences | 3,044 ([Document 1](document_1.txt)) | — | — |
| Sentences per annotated dialog | ≈30.4 (derived) | — | — |
| Annotators | 2 linguistic experts ([Document 1](document_1.txt)) | — | — |
| Weighted kappa | 0.874 ([Document 1](document_1.txt)) | — | — |

The 0.874 averaged weighted kappa value indicates strong agreement between the two expert annotators on the 3,044-sentence subset ([Document 1](document_1.txt)).

## 5. Conversational Depth and Utterance Length

The corpus is characterized by two structural averages that both sources report identically: an **average conversation length of 12.45 turns** and an **average utterance length of 11.13 words** ([Document 1](document_1.txt); [Document 2](document_2.txt)). The notes describe these averages as characterizing "the full AntiScam corpus" rather than only the annotated subset ([Document 2](document_2.txt)).

These two averages allow approximate volume estimates, which are derived by this report and not stated in the sources:

| Derived quantity | If 220 dialogs | If 320 dialogs |
|---|---|---|
| Total turns (dialogs × 12.45) | ≈2,739 | ≈3,984 |
| Total words (turns × 11.13) | ≈30,488 | ≈44,342 |
| Estimated total sentences (scaling 3,044 / 100 dialogs) | ≈6,697 | ≈9,741 |
| Sentences per turn (3,044 ÷ 100 ÷ 12.45) | ≈2.44 | ≈2.44 |

A useful structural check: 3,044 sentences spread across 100 dialogs and 12.45 turns per dialog implies roughly 2.44 sentences per turn, which is plausible for a typed chat exchange in which each turn may itself be sentence-fragmented. These figures are extrapolations and should be treated as approximate order-of-magnitude estimates rather than reported statistics.

## 6. Corpus Partitioning for Modeling

For experimentation, the corpus is split into **80% training, 10% validation, and 10% testing** ([Document 1](document_1.txt)). Applied to the competing totals, this yields approximately 176/22/22 dialogs under the 220-dialog reading and 256/32/32 dialogs under the 320-dialog reading (derived). The same 80/10/10 scheme is applied to the second non-collaborative dataset used in the paper, PersuasionForGood, which targets charitable donation persuasion rather than scam defense ([Document 1](document_1.txt)).

## 7. A Separate Quantity: The Human Evaluation Corpus

A frequently conflated number is the volume of dialogs generated during human evaluation of the MISSA system on AntiScam. This is distinct from the AntiScam dataset itself. The evaluation recruited **15 college-student volunteers**, each asked to impersonate an attacker and interact with all models at least three times to avoid randomness, producing **225 dialogs in total** ([Document 1](document_1.txt)). Each model received 45 human ratings, and average scores were reported as the final human-evaluation figures ([Document 1](document_1.txt)).

| Human-evaluation parameter | Value |
|---|---|
| Volunteers (attacker role-players) | 15 ([Document 1](document_1.txt)) |
| Interactions per volunteer per model | ≥3 ([Document 1](document_1.txt)) |
| Total evaluation dialogs | 225 ([Document 1](document_1.txt)) |
| Ratings per model | 45 ([Document 1](document_1.txt)) |

## 8. Dimensional Size of the Annotation Scheme

Beyond raw counts, the corpus is labeled under a hierarchical intent scheme spanning both datasets. On-task intents for AntiScam include *elicitation*, *providing_information*, and *refusal*, while off-task general intents include *open_question*, *yes_no_question*, *negative_answer*, *positive_answer*, *responsive_statement*, *nonresponsive_statement*, *greeting*, *thanking*, *respond_to_thank*, *apology*, *closing*, and *hold* ([Document 1](document_1.txt)). This taxonomy constitutes an additional, categorical dimension of dataset size that is independent of dialog count.

## 9. Performance Context

Because dataset size is typically invoked to justify modeling claims, the reported results situate AntiScam's scale. MISSA achieved a perplexity of 21.07 and a TaskSuc score of 1.294 on AntiScam, versus 32.96 and 1.025 for TransferTransfo and no reported perplexity with 0.975 TaskSuc for the hybrid model ([Document 1](document_1.txt)). MISSA also led on human metrics such as fluency (4.18), coherence (3.75), and engagement (3.69) ([Document 1](document_1.txt)). The authors conclude that MISSA outperforms two baseline models on almost all metrics across both datasets ([Document 1](document_1.txt)).

## 10. Synthesis: Sizes at a Glance

| Dimension | Value | Confidence |
|---|---|---|
| Total human–human dialogs | 220 (primary text) or 320 (secondary notes) | Contested ([Document 1](document_1.txt); [Document 2](document_2.txt)) |
| Annotated dialogs | 100 | High ([Document 1](document_1.txt); [Document 2](document_2.txt)) |
| Annotated sentences | 3,044 | High ([Document 1](document_1.txt); [Document 2](document_2.txt)) |
| Avg. turns per conversation | 12.45 | High ([Document 1](document_1.txt); [Document 2](document_2.txt)) |
| Avg. words per utterance | 11.13 | High ([Document 1](document_1.txt); [Document 2](document_2.txt)) |
| Users identifying attacker | 172 | High ([Document 1](document_1.txt); [Document 2](document_2.txt)) |
| Inter-annotator weighted kappa | 0.874 | Moderate ([Document 1](document_1.txt)) |
| Human-evaluation dialogs | 225 | Moderate ([Document 1](document_1.txt)) |

## 11. Conclusion

AntiScam is a small-to-moderate corpus by contemporary dialog-system standards. Its most reliably attested figures are 100 annotated dialogs containing 3,044 sentences, 12.45 turns per conversation, 11.13 words per utterance, and 172 users successfully identifying their attacker partner ([Document 1](document_1.txt); [Document 2](document_2.txt)). The total collection size is reported as either 220 or 320 human–human dialogs depending on the source, and I judge the 220 figure — embedded as it is in the paper's own dataset-construction passage alongside the 172/220 outcome — to be the stronger candidate for the version described in the primary text, while acknowledging that the qualitative claim that attackers were "not too easily identifiable" fits a ~54% identification rate better ([Document 1](document_1.txt); [Document 2](document_2.txt)). Users of the dataset should therefore cite the total as approximately 220 dialogs unless they can verify the 320 figure against the released artifact, and should always report the annotated subset separately at 100 dialogs and 3,044 sentences, since that is where the corpus's labeled value resides.

## References

Document 1. (n.d.). *End-to-end trainable non-collaborative dialog system* [Excerpts and experiment tables; source document_1.txt].

Document 2. (n.d.). *Research notes on the AntiScam dataset: Size, annotation statistics, and collection methodology* [Summary notes; source document_2.txt].