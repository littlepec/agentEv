# How Big Is the AntiScam Dataset? A Structured Assessment of Corpus Scale, Annotation Depth, and Interpretive Boundaries

## Introduction

The question "how big is the AntiScam dataset?" appears straightforward, but a rigorous answer requires distinguishing between several different measures of scale that the available documentation reports separately. AntiScam is not described by a single size figure; instead, the corpus is characterized by (a) a total dialog count, (b) an annotated subset count, (c) a sentence count confined to that subset, (d) turn-level and utterance-level averages that the source explicitly states describe the full corpus, and (e) a user-outcome statistic expressed as a fraction of the total corpus. This report reconstructs the size of AntiScam from the two source documents provided, presents the directly reported figures, derives several arithmetically implied estimates while clearly labeling them as derived rather than reported, and identifies the boundaries of what the evidence does and does not support. The central finding is that AntiScam consists of **220 human-human dialogs**, of which **100 dialogs comprising 3,044 sentences** were manually annotated by two expert annotators with linguistic training ([Document 2, n.d.](document_2.txt)).

## Source Basis and Reliability Assessment

Two source documents supply all information used in this report. Document 1 is a results-and-analysis excerpt reporting the main experimental evaluation of a model named MISSA on the AntiScam dataset, alongside a second dataset, PersuasionForGood ([Document 1, n.d.](document_1.txt)). Document 2 is a dataset-description excerpt that reports the corpus construction method, its total size, its annotation statistics, and a user-identification outcome ([Document 2, n.d.](document_2.txt)).

Both documents are treated here as primary sources because they report first-hand experimental and descriptive results rather than secondary commentary. Neither document carries a visible publication date or title in the provided material, so recency cannot be independently assessed, and no preference for a newer source over an older one can be justified on the evidence available. Document 2 is the more authoritative source for questions of corpus size, since size and annotation statistics fall squarely within its descriptive scope. Document 1 contributes corroborating context: it confirms that AntiScam is used as an evaluation benchmark with automatic and human evaluation metrics reported in tabulated form ([Document 1, n.d.](document_1.txt)). Notably, the excerpt from Document 2 repeats its descriptive content across multiple blocks in the supplied material; those repetitions were consolidated into a single reference, and no duplicate citation is used.

## Directly Reported Size Figures

The following figures are stated explicitly in the source material and require no computation.

### Total Dialog Volume

AntiScam is described as a human-human anti-scam dialog corpus collected via a role-playing Amazon customer service scam scenario on Amazon Mechanical Turk, and its size is reported as **220 human-human dialogs** ([Document 2, n.d.](document_2.txt)). This is the headline answer to the question of how big the dataset is: 220 conversations.

### Annotated Subset Size

Independent of the total dialog count, the paper reports that a **subset of 100 dialogs containing 3,044 sentences was manually annotated** ([Document 2, n.d.](document_2.txt)). This annotation was performed by **two expert annotators who have linguistic training** ([Document 2, n.d.](document_2.txt)). The annotated subset therefore represents less than half of the total corpus, a point developed further below.

### Turn-Level and Utterance-Level Dimensions

The corpus is further characterized by two averages: an **average conversation length of 12.45 turns** and an **average utterance length of 11.13 words** ([Document 2, n.d.](document_2.txt)). Critically, the source states explicitly that "these averages describe the full AntiScam corpus" ([Document 2, n.d.](document_2.txt)). This scoping statement matters, because it means the turn and word averages should not automatically be attributed to the 100-dialog annotated subset without an additional assumption.

### Outcome Statistic

The source also reports that **172 out of 220 users successfully identified their partner as an attacker**, describing this as part of the AntiScam dataset description ([Document 2, n.d.](document_2.txt)). Because this statistic is expressed against the full corpus denominator of 220, it confirms 220 as the operative total-unit count for the dataset as a whole.

### Summary Table of Reported Figures

| Dimension | Reported Value | Scope Specified by Source |
|---|---|---|
| Total dialogs | 220 human-human dialogs | Full AntiScam corpus |
| Annotated dialogs | 100 dialogs | Manually annotated subset |
| Annotated sentences | 3,044 sentences | Manually annotated subset |
| Annotators | 2 expert annotators with linguistic training | Manually annotated subset |
| Average conversation length | 12.45 turns | Full AntiScam corpus |
| Average utterance length | 11.13 words | Full AntiScam corpus |
| Successful attacker identification | 172 of 220 users | Full AntiScam corpus |

*Note.* All values in the table are directly reported ([Document 1, n.d.](document_1.txt); [Document 2, n.d.](document_2.txt)).

## Derived Estimates: What the Reported Numbers Imply

The reported figures support several arithmetic estimates that are not themselves stated in the sources. These are presented as derived values with explicit assumptions, because they are useful for interpreting scale but carry the risk of over-extension.

If the reported average of 12.45 turns per conversation applies uniformly across the corpus, the 220-dialog total implies approximately **2,739 dialogue turns** in aggregate. Multiplying that figure by the reported average utterance length of 11.13 words yields an approximate total of **30,485 words** across the corpus. Both values are arithmetic extrapolations from the reported averages and inherit any variance in the underlying distributions ([Document 2, n.d.](document_2.txt)).

For the annotated subset, dividing 3,044 sentences by 100 dialogs yields approximately **30.44 sentences per annotated dialog** ([Document 2, n.d.](document_2.txt)). Applying the corpus-level averages to the 100-dialog subset would imply roughly 1,245 turns and about 13,857 words within the annotated portion, though this projection assumes the annotated subset resembles the corpus average, an assumption the source does not confirm ([Document 2, n.d.](document_2.txt)).

The user-identification statistic converts to a success rate of approximately **78.2%** (172 divided by 220), meaning that roughly one in five users failed to identify their partner as an attacker ([Document 2, n.d.](document_2.txt)). The source reports the raw fraction rather than the percentage, and the percentage here is derived.

The annotated subset covers approximately **45.5%** of the dialogs in the full corpus (100 of 220) ([Document 2, n.d.](document_2.txt)). This is a derived ratio, not a reported one, but it is important for interpreting how much of AntiScam carries manual annotation.

| Derived Quantity | Value | Basis and Assumption |
|---|---|---|
| Estimated total turns | ~2,739 | 220 dialogs × 12.45 turns |
| Estimated total words | ~30,485 | 2,739 turns × 11.13 words |
| Sentences per annotated dialog | ~30.44 | 3,044 sentences ÷ 100 dialogs |
| Projected turns in annotated subset | ~1,245 | 100 dialogs × 12.45 turns (assumes subset matches corpus average) |
| Projected words in annotated subset | ~13,857 | 1,245 turns × 11.13 words (same assumption) |
| Attacker identification rate | ~78.2% | 172 ÷ 220 |
| Annotated share of dialogs | ~45.5% | 100 ÷ 220 |

*Note.* None of the values in this table appear as such in the sources; they are arithmetic derivations from the reported figures ([Document 2, n.d.](document_2.txt)).

## Unit Ambiguity: Turns, Utterances, and Sentences

One methodological caution deserves emphasis. The source reports the average conversation length in **turns** and the average utterance length in **words**, while the annotated subset is measured in **sentences** ([Document 2, n.d.](document_2.txt)). The provided material does not define whether a "turn," an "utterance," and a "sentence" are equivalent units. If one were to treat turns and sentences as interchangeable, the reported figures would conflict, since 12.45 turns per conversation is far below the derived 30.44 sentences per annotated dialog. The more plausible reading, consistent with the reported numbers, is that a single conversational turn may contain multiple sentences, with the derived ratio implying roughly 2.4 sentences per turn in the annotated portion of the corpus ([Document 2, n.d.](document_2.txt)). This reconciliation is an inference, not a statement made by the sources, and the absence of an explicit unit definition is a limitation the user of these figures should acknowledge.

A second caution concerns scope. The source states that the 12.45-turn and 11.13-word averages describe the **full** AntiScam corpus, whereas the 3,044-sentence count applies only to the **annotated subset** ([Document 2, n.d.](document_2.txt)). Any analysis that multiplies the corpus-level averages by the subset dialog count, or that treats 3,044 as the sentence total for all 220 dialogs, risks conflating two different levels of description. If the annotated subset's per-dialog sentence rate were applied across all 220 dialogs, the implied corpus-wide sentence total would be approximately 6,697 sentences, but this projection rests on an untested representativeness assumption ([Document 2, n.d.](document_2.txt)).

## What "Big" Means Here: An Interpretive Judgment

Scale in dialogue-corpus research is multidimensional, and the sources support a specific and defensible reading of AntiScam's size. In absolute terms, 220 dialogs is a compact corpus, and the material provided offers no comparative benchmarks for other anti-scam corpora against which to position it. Document 1 does state that MISSA was evaluated on both AntiScam and PersuasionForGood, with AntiScam results in Table 3 and PersuasionForGood results in Table 5, but the provided excerpt does not report the size of PersuasionForGood, so no size comparison between the two datasets can be made from this evidence ([Document 1, n.d.](document_1.txt)).

Where AntiScam's scale is more substantial is in annotation depth relative to raw volume. With 100 dialogs and 3,044 sentences manually annotated by two expert annotators with linguistic training, the dataset pairs a compact conversation count with dense, expert-produced annotation ([Document 2, n.d.](document_2.txt)). My assessment, based strictly on the supplied figures, is that AntiScam is best described as a **small-to-moderate corpus by dialog count but a comparatively annotation-rich one**, since nearly half of its 220 dialogs carry manual sentence-level annotation produced by trained linguists ([Document 2, n.d.](document_2.txt)). Its size claim should therefore be stated as a pair of numbers—220 dialogs overall, 100 dialogs and 3,044 sentences annotated—rather than as a single quantity.

## What the Evidence Does Not Establish

Several questions about dataset size cannot be answered from the provided material. The sources do not report the total number of participants, the distribution of dialog lengths beyond the mean, the total token or word count as a directly measured value, the number of unique annotators beyond "two expert annotators," or any inter-annotator agreement statistic ([Document 2, n.d.](document_2.txt)). The sources also do not report the size of the PersuasionForGood dataset referenced in Document 1, nor do they provide any tabulated breakdown of results by split ([Document 1, n.d.](document_1.txt)). Finally, because neither document carries a usable date in the provided material, no claim can be made about the dataset's recency or about subsequent expansions of the corpus. All derived estimates in this report should be treated as bounded by these gaps.

## Conclusion

The AntiScam dataset is **220 human-human dialogs**, collected through a role-playing Amazon customer service scam scenario on Amazon Mechanical Turk ([Document 2, n.d.](document_2.txt)). Within that total, **100 dialogs containing 3,044 sentences** were manually annotated by **two expert annotators with linguistic training** ([Document 2, n.d.](document_2.txt)). The corpus averages **12.45 turns per conversation** and **11.13 words per utterance**, averages the source explicitly attributes to the full corpus rather than to the annotated subset ([Document 2, n.d.](document_2.txt)). The dataset also records that **172 of 220 users** successfully identified their partner as an attacker, a roughly 78.2% success rate by derivation ([Document 2, n.d.](document_2.txt)). AntiScam additionally serves as an evaluation benchmark for the MISSA model and for baseline models including TransferTransfo and a hybrid model, with results reported across automatic and human evaluation metrics ([Document 1, n.d.](document_1.txt)). Taken together, the most accurate single-sentence answer is that AntiScam is a 220-dialog corpus with an expert-annotated core of 100 dialogs and 3,044 sentences—modest in dialog volume, but deliberately dense in linguistic annotation.

## References

Document 1. (n.d.). *Results and analysis* [Manuscript excerpt].

Document 2. (n.d.). *AntiScam dataset description* [Manuscript excerpt].