# The Size of the AntiScam Dataset: Dialogs, Sentences, Annotation Coverage, and Derived Scale Estimates

## 1. Introduction and Scope of the Question

The query concerns the overall size of the AntiScam dataset, a human–human anti-scam dialog corpus introduced to support research on non-collaborative dialog systems. Size, in the context of a conversational corpus, is not a single number but a small family of related measurements: the count of complete conversations, the count of annotated conversations, the count of individual sentences or utterances, the average length of a conversation in turns, and the average length of an utterance in words. The available documentation reports all of these dimensions explicitly, which allows the size of AntiScam to be characterized with considerable precision ([Document 2](document_2.txt)).

The most direct answer to the query is that AntiScam comprises **320 human–human dialogs** in total, of which a **subset of 100 dialogs containing 3,044 sentences** was manually annotated ([Document 2](document_2.txt)). The corpus records an average conversation length of **12.45 turns** and an average utterance length of **11.13 words**, and it further reports that **172 out of 320 users** successfully identified their conversational partner as an attacker ([Document 2](document_2.txt)). Each of these figures is examined in turn below, together with the collection methodology that produced them and a set of clearly labelled derived estimates that describe the corpus at a scale not directly reported in the source material.

## 2. The Headline Figure: 320 Human–Human Dialogs

### 2.1 What the 320 Dialogs Represent

AntiScam is described as a corpus of human–human anti-scam dialogs created to learn human elicitation strategies, and it contains 320 human–human dialogs ([Document 2](document_2.txt)). This total is reported by the paper itself within its AntiScam dataset description, meaning the figure is a primary, first-party statistic rather than an external estimate ([Document 2](document_2.txt)). The designation "human–human" is significant for interpreting the size figure: every one of the 320 conversations involves two human participants interacting with one another, rather than a human interacting with a simulated or scripted agent ([Document 2](document_2.txt)).

The corpus was collected through a role-playing Amazon customer service scam scenario on Amazon Mechanical Turk ([Document 2](document_2.txt)). Within this scenario, users defend themselves against attackers who are attempting to collect personal information ([Document 1](document_1.txt)). This framing explains why the dataset is classified as non-collaborative: the two participants in each conversation do not share a cooperative goal, and the size of the dataset should therefore be understood as 320 instances of adversarial, goal-conflicting interaction rather than 320 cooperative task-completion dialogues ([Document 1](document_1.txt)).

### 2.2 Why the Total Matters

The size of AntiScam is directly tied to the motivation for its creation. The stated purpose was to enrich publicly available non-collaborative task datasets because, as the paper observes, non-collaborative tasks are still relatively new to the study of dialog systems and there are insufficiently many meaningful datasets available for evaluation ([Document 1](document_1.txt)). In that context, 320 dialogs functions as the primary claim of scale: it is the quantity offered as a remedy to the scarcity of evaluation resources in this subfield ([Document 1](document_1.txt)).

## 3. The Annotated Subset: 100 Dialogs and 3,044 Sentences

### 3.1 Reported Annotation Statistics

Beyond the raw corpus count, the documentation distinguishes carefully between the full corpus and the portion that received manual annotation. For annotation statistics, the paper reports that a subset of 100 dialogs containing 3,044 sentences was manually annotated ([Document 2](document_2.txt)). This means that annotation coverage extends to approximately 31.25% of the corpus by dialog count, a proportion derived by dividing 100 by 320 ([Document 2](document_2.txt)).

The annotation was performed by two expert annotators who have linguistic training ([Document 2](document_2.txt)). The documentation explicitly states that the manually annotated subset comprises 100 dialogs and 3,044 sentences, while the total dataset comprises 320 human–human dialogs ([Document 2](document_2.txt)). This distinction is repeated consistently across the available sources, which increases confidence that 320 and 100 are intended as two different quantities serving two different purposes—corpus size and annotation coverage, respectively ([Document 2](document_2.txt)).

### 3.2 Interpretive Implications

The existence of a 100-dialog annotated subset alongside a 320-dialog full corpus has practical consequences for how the dataset's size should be quoted in research contexts. A study reporting results on AntiScam's human-annotated labels is, in effect, working with 3,044 sentences drawn from 100 conversations, whereas a study training or evaluating on unannotated dialog structure has access to the full 320 dialogs ([Document 2](document_2.txt)). The documentation notes that the average conversation length of 12.45 turns and the average utterance length of 11.13 words describe the full AntiScam corpus, not merely the annotated subset ([Document 2](document_2.txt)). This is an important qualification, because it means the per-conversation length statistics can legitimately be applied to all 320 dialogs.

## 4. Internal Size Metrics: Turn and Word Lengths

### 4.1 Average Conversation Length

The average conversation length in AntiScam is 12.45 turns ([Document 2](document_2.txt)). This figure functions as the unit-level measure of size: it describes how deep an individual conversation runs, complementing the corpus-level measure of how many conversations exist. Because the documentation states that these averages describe the full corpus, the 12.45-turn figure is applicable to the 320-dialog total rather than being restricted to the annotated subset ([Document 2](document_2.txt)).

### 4.2 Average Utterance Length

The average utterance length is 11.13 words ([Document 2](document_2.txt)). Utterance-level length is the smallest reported unit of size in the documentation and provides the basis for estimating the corpus's lexical scale. As with the turn statistic, the documentation attributes this average to the full AntiScam corpus ([Document 2](document_2.txt)).

### 4.3 Derived Corpus-Level Estimates

The source material reports per-unit averages rather than aggregate totals for turns and words. It is therefore possible, and analytically useful, to derive aggregate estimates by combining the reported figures. The following calculations are the present author's arithmetic extensions of the reported statistics and should be treated as illustrative derived quantities rather than values stated in the source documents ([Document 2](document_2.txt)).

| Derived Quantity | Calculation | Result |
|---|---|---|
| Total turns, full corpus | 320 dialogs × 12.45 turns | ≈ 3,984 turns |
| Total words, full corpus (utterance = 11.13 words) | 3,984 turns × 11.13 words | ≈ 44,342 words |
| Annotation coverage by dialog | 100 ÷ 320 | 31.25% |
| Sentences per annotated dialog | 3,044 ÷ 100 | ≈ 30.44 sentences |
| Sentences per turn, annotated subset | 30.44 ÷ 12.45 | ≈ 2.44 sentences |
| Words in annotated subset (utterance = 11.13 words) | 3,044 × 11.13 | ≈ 33,880 words |

Two observations follow from this table. First, applying the reported averages to the full 320-dialog corpus yields an estimated scale on the order of 3,984 turns and roughly 44,000 words ([Document 2](document_2.txt)). Second, the annotated subset alone contains roughly 30 sentences per conversation, which implies that each conversational turn may encompass more than one sentence-level utterance ([Document 2](document_2.txt)). This ratio is consistent with the scenario being studied: a role-playing scam interaction in which attackers attempt to elicit personal information and users defend themselves would plausibly generate multi-sentence turns rather than single-clause exchanges ([Document 1](document_1.txt)).

## 5. Outcome Scale: 172 of 320 Users Identified the Attacker

A distinct dimension of the dataset's size concerns the recorded outcome of the interactions. The paper reports that 172 out of 320 users successfully identified their partner as an attacker ([Document 2](document_2.txt)). Expressed as a proportion, this represents a 53.75% identification rate, with the remaining 148 users, or 46.25%, not reported as having identified their partner as an attacker. These percentages are derived directly from the reported numerator and denominator ([Document 2](document_2.txt)).

This outcome statistic is tightly bound to the corpus size, because its denominator is the same 320 that defines the dataset. The figure therefore reinforces the 320-dialog total as the authoritative corpus count and demonstrates that the outcome variable is recorded at the level of every conversation in the dataset, not merely for the annotated subset ([Document 2](document_2.txt)).

## 6. Size in Comparative Context

The documentation indicates that AntiScam was used alongside an existing PersuasionForGood dataset in the evaluation of the MISSA model ([Document 1](document_1.txt)). The reported comparison states that MISSA outperforms two baseline models, TransferTransfo and a hybrid model, on almost all metrics across both datasets, with main results on AntiScam presented in Table 3 and results on PersuasionForGood presented in Table 5 ([Document 1](document_1.txt)). Both automatic and human evaluation metrics were employed, and examples of real dialogs from the human evaluation appear in Table 4 ([Document 1](document_1.txt)).

It is worth stating plainly that the supplied documentation does **not** report the size of the PersuasionForGood dataset, nor does it provide absolute scores or metric values from Tables 3, 4, or 5 ([Document 1](document_1.txt)). Consequently, no quantitative size comparison between AntiScam and PersuasionForGood can be made from the available material. Any such comparison would require information not present in these sources.

## 7. Source Reliability and Evidence Weighting

The available information derives from two documents of differing character. Document 1 contains text drawn from the research paper itself, describing dataset construction, model evaluation, and results presentation, and therefore carries the highest evidentiary weight for claims about AntiScam's purpose and experimental use ([Document 1](document_1.txt)). Document 2 contains concentrated dataset statistics—dialog counts, annotation counts, turn and utterance averages, and the attacker-identification outcome—presented both as direct statements and as third-party research notes that compile key questions and answers about the AntiScam dataset ([Document 2](document_2.txt)).

Both documents are internally consistent on the central size figures. Across all statements, the total corpus is 320 dialogs, the annotated subset is 100 dialogs and 3,044 sentences, the average conversation length is 12.45 turns, the average utterance length is 11.13 words, and 172 of 320 users identified their partner as an attacker ([Document 2](document_2.txt); [Document 1](document_1.txt)). No conflicting figures appear anywhere in the supplied material. Because Document 1 supplies the methodological context and Document 2 supplies the numeric detail, the two are mutually reinforcing rather than redundant, and the reported size statistics can be treated with high confidence.

## 8. Consolidated Summary of Size Dimensions

| Size Dimension | Reported Value | Scope | Source |
|---|---|---|---|
| Total dialogs | 320 | Full corpus | ([Document 2](document_2.txt)) |
| Annotated dialogs | 100 | Annotated subset | ([Document 2](document_2.txt)) |
| Annotated sentences | 3,044 | Annotated subset | ([Document 2](document_2.txt)) |
| Expert annotators | 2 (linguistically trained) | Annotated subset | ([Document 2](document_2.txt)) |
| Average conversation length | 12.45 turns | Full corpus | ([Document 2](document_2.txt)) |
| Average utterance length | 11.13 words | Full corpus | ([Document 2](document_2.txt)) |
| Users identifying attacker | 172 of 320 | Full corpus | ([Document 2](document_2.txt)) |
| Dialog type | Human–human, non-collaborative | Full corpus | ([Document 1](document_1.txt); [Document 2](document_2.txt)) |
| Collection platform | Amazon Mechanical Turk | Full corpus | ([Document 2](document_2.txt)) |

## 9. Conclusion

The AntiScam dataset is a 320-dialog human–human corpus of anti-scam conversations collected through a role-playing Amazon customer service scam scenario on Amazon Mechanical Turk, with 100 of those dialogs and 3,044 sentences manually annotated by two linguistically trained expert annotators ([Document 2](document_2.txt)). Its internal size metrics are an average conversation length of 12.45 turns and an average utterance length of 11.13 words, both reported as describing the full corpus ([Document 2](document_2.txt)). Its recorded outcome statistic is that 172 of 320 users successfully identified their partner as an attacker, a 53.75% rate ([Document 2](document_2.txt)). Derived arithmetic on these reported averages suggests an order of magnitude of approximately 3,984 total turns and roughly 44,000 words across the full corpus, and approximately 30 sentences per conversation within the annotated subset, though these aggregates are calculations rather than reported figures. The dataset was created specifically to address the shortage of meaningful non-collaborative dialog datasets for evaluation, and it was used alongside a PersuasionForGood dataset to evaluate the MISSA model, which outperformed TransferTransfo and a hybrid baseline on almost all metrics ([Document 1](document_1.txt)).

## References

Document 1. (n.d.). *End-to-end trainable non-collaborative dialog system* [Research paper text]. `document_1.txt`.

Document 2. (n.d.). *AntiScam dataset statistics and research notes* [Dataset description and compiled notes]. `document_2.txt`.