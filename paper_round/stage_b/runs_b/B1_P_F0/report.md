# The Size of the AntiScam Dataset: A Comprehensive Report on Corpus Scale, Annotation Coverage, and Derived Metrics

## 1. Introduction

The question "How big is the AntiScam dataset?" appears simple, but the available documentation shows that the answer depends on which dimension of size is being measured. AntiScam is reported to be a human–human anti-scam dialog corpus collected through a role-playing Amazon customer service scam scenario on Amazon Mechanical Turk ([document_2.txt](document_2.txt)). Its size is stated in absolute terms as 320 human–human dialogs, while its annotation statistics are reported separately as covering 100 dialogs and 3,044 sentences ([document_2.txt](document_2.txt)). In addition, the corpus has measurable interactional dimensions—an average conversation length of 12.45 turns and an average utterance length of 11.13 words—which are explicitly said to describe the full AntiScam corpus ([document_2.txt](document_2.txt)).

This report answers the size question along four distinct axes: (a) the total number of dialogs, (b) the annotated subset, (c) the interactional volume expressed in turns and words, and (d) the outcome-level scale expressed as the number of users who successfully identified their partner as an attacker. It also presents derived volume estimates, clearly labeled as calculations by this report rather than as figures reported by the source, and it assesses the reliability and limitations of the available documentation.

## 2. Dialog-Level Size: The Primary Answer

The most direct answer to the question is that the AntiScam dataset contains **320 human–human dialogs**. This figure is reported consistently and repeatedly across the available documentation. The paper states that AntiScam is a human–human anti-scam dialog corpus with a size of 320 human–human dialogs ([document_2.txt](document_2.txt)). The same total appears in the structured annotation statistics, where the total dataset is described as comprising 320 human–human dialogs ([document_2.txt](document_2.txt)). A third-party research note on the *End-to-End Trainable Non-Collaborative Dialog System* likewise reports that the dataset contains 320 human–human dialogs and that the paper reports this total in its AntiScam dataset description ([document_2.txt](document_2.txt)).

The consistency of this figure across the narrative summary, the annotation statistics, and the third-party research note is notable. Where a corpus size is repeated in three separate framings without contradiction, the 320-dialog total can be treated as the well-established headline size of AntiScam ([document_2.txt](document_2.txt)).

It is worth emphasizing what "320 dialogs" means in this context. Each dialog is a two-party human–human exchange, not a human–machine exchange, and each was produced under an anti-scam role-play in which one participant played an attacker and the other a potential victim. The corpus was created specifically to learn human elicitation strategies, and it serves as the dataset for non-collaborative dialog research in the paper ([document_2.txt](document_2.txt)). The unit of measurement is therefore a complete dyadic conversation, not an individual message, participant, or session.

## 3. Annotation-Level Size: 100 Dialogs and 3,044 Sentences

A second, smaller figure describes the manually annotated portion of the corpus. The paper reports that a subset of 100 dialogs containing 3,044 sentences was manually annotated ([document_2.txt](document_2.txt)). This annotation was performed by two expert annotators who have linguistic training ([document_2.txt](document_2.txt)). The same statistics are restated in the summary description, which notes that AntiScam's annotation statistics cover 100 dialogs and 3,044 sentences, annotated by two expert annotators with linguistic training ([document_2.txt](document_2.txt)).

This creates an important distinction for anyone asking about dataset size. AntiScam is large at the dialog level (320 dialogs) but is annotated at roughly one-third of that scale (100 dialogs). The annotated subset is therefore a 100-dialog sample drawn from the full 320-dialog corpus, and the 3,044-sentence figure applies specifically to that annotated sample rather than to the entire corpus ([document_2.txt](document_2.txt)). The documentation is explicit on this point: the manually annotated subset comprises 100 dialogs and 3,044 sentences ([document_2.txt](document_2.txt)).

A simple calculation by this report—3,044 sentences divided by 100 dialogs—yields approximately 30.4 sentences per annotated dialog. This derived figure is not stated in the sources but follows arithmetically from the reported numbers ([document_2.txt](document_2.txt)).

## 4. Interactional Size: Turns and Words

The third dimension of size is interactional. The paper reports an average conversation length of 12.45 turns and an average utterance length of 11.13 words, and the documentation states explicitly that these averages describe the full AntiScam corpus ([document_2.txt](document_2.txt)). This clarification matters: the turn and utterance averages are not restricted to the 100-dialog annotated subset; they characterize the complete 320-dialog collection ([document_2.txt](document_2.txt)).

The reporting of averages rather than totals means that the exact word count and turn count of the corpus are not directly stated in the available documentation. However, because the averages are explicitly attached to the full corpus, reasonable derived estimates can be produced. If the 320 dialogs average 12.45 turns each, the full corpus contains approximately 3,984 turns. If each turn averages 11.13 words, the full corpus contains on the order of 44,300 words. Applying the same average utterance length to the 3,044 annotated sentences yields roughly 33,900 words within the annotated subset. These derived figures are computed by this report from the reported averages and should be treated as estimates, not as figures asserted by the source ([document_2.txt](document_2.txt)).

The distinction between "turns" and "utterances" is not fully resolved in the provided documentation. The sources report turn length and utterance length as separate averages without clarifying whether a turn and an utterance are operationally identical in this corpus. Consequently, the derived word estimates carry a degree of uncertainty and should be read as order-of-magnitude indications of corpus volume rather than precise counts ([document_2.txt](document_2.txt)).

## 5. Outcome-Level Size: Successful Attacker Identification

A fourth measurable quantity concerns the outcomes recorded within the corpus rather than its structural dimensions. The paper reports that 172 out of 320 users successfully identified their partner as an attacker ([document_2.txt](document_2.txt)). This outcome is described as part of the AntiScam dataset description ([document_2.txt](document_2.txt)).

Calculated as a proportion, 172 of 320 corresponds to 53.75 percent—a majority, but a slim one. This figure indicates that in roughly half of the recorded interactions, the participant in the victim role detected the scam attempt. From a dataset-size perspective, this means the corpus contains 172 dialogs with a successful identification outcome and, by subtraction, 148 dialogs without one. That derived split is a straightforward consequence of the reported numbers ([document_2.txt](document_2.txt)) and is relevant because it shows the corpus is not skewed overwhelmingly toward one outcome class.

## 6. Consolidated Size Metrics

The table below consolidates every size-related figure explicitly reported in the available documentation.

| Dimension | Reported Figure | Scope | Source |
|---|---|---|---|
| Total dialogs | 320 | Full corpus | ([document_2.txt](document_2.txt)) |
| Annotated dialogs | 100 | Manually annotated subset | ([document_2.txt](document_2.txt)) |
| Annotated sentences | 3,044 | Manually annotated subset | ([document_2.txt](document_2.txt)) |
| Annotators | 2 expert annotators with linguistic training | Annotated subset | ([document_2.txt](document_2.txt)) |
| Average conversation length | 12.45 turns | Full corpus | ([document_2.txt](document_2.txt)) |
| Average utterance length | 11.13 words | Full corpus | ([document_2.txt](document_2.txt)) |
| Successful attacker identification | 172 of 320 users | Full corpus | ([document_2.txt](document_2.txt)) |
| Dialog type | Human–human anti-scam dialogs | Full corpus | ([document_2.txt](document_2.txt)) |
| Collection setting | Role-playing Amazon customer service scam on Amazon Mechanical Turk | Full corpus | ([document_2.txt](document_2.txt)) |

## 7. Derived Volume Estimates

The table below presents figures calculated by this report from the reported averages and ratios. None of these values are stated in the source documents, and they are included only to give a sense of the order of magnitude of the corpus.

| Derived Metric | Calculation | Estimated Value |
|---|---|---|
| Total turns in full corpus | 320 dialogs × 12.45 turns | ≈ 3,984 turns |
| Total words in full corpus | ≈ 3,984 turns × 11.13 words | ≈ 44,300 words |
| Sentences per annotated dialog | 3,044 sentences ÷ 100 dialogs | ≈ 30.4 sentences |
| Words in annotated subset | 3,044 sentences × 11.13 words | ≈ 33,900 words |
| Share of users identifying attacker | 172 ÷ 320 | 53.75% |
| Dialogs without successful identification | 320 − 172 | 148 dialogs |

All underlying figures are drawn from ([document_2.txt](document_2.txt)).

## 8. Research Context and the Position of AntiScam

The size of AntiScam is best understood alongside its role in the research literature. The available documentation includes results and analysis from an experimental study in which AntiScam serves as a primary evaluation dataset. Table 3 of that study presents the main experiment results on the AntiScam dataset for both automatic evaluation metrics and human evaluation metrics, and the experiment results on PersuasionForGood are shown in Table 5 ([document_1.txt](document_1.txt)). The authors report that MISSA outperforms two baseline models—TransferTransfo and a hybrid model—on almost all metrics on both datasets, and examples of real dialogs from the human evaluation are presented in Table 4 ([document_1.txt](document_1.txt)).

This context indicates that AntiScam is used both as a training/evaluation resource and as a source of human-evaluated dialog examples. The availability of human evaluation metrics alongside automatic metrics suggests the corpus is large enough to support dual-mode assessment, though the documentation does not state how many dialogs were sampled for the human evaluation ([document_1.txt](document_1.txt)). Notably, the sources do not report the size of PersuasionForGood, so no size comparison between the two corpora can be made from the available information ([document_1.txt](document_1.txt)).

## 9. Limitations and Gaps in the Documentation

Several size-related questions cannot be answered from the provided material. First, the exact total number of turns and words in the corpus is not reported; only averages are given ([document_2.txt](document_2.txt)). Second, the number of participants involved in collecting 320 dialogs is not stated, so the count of unique individuals cannot be determined. Third, the documentation does not specify the sentence count of the full 320-dialog corpus—only the 100-dialog annotated subset has a reported sentence total of 3,044 ([document_2.txt](document_2.txt)). Fourth, it is unclear whether the 3,044 annotated sentences correspond one-to-one with turns or utterances, which affects the precision of any word-volume estimate ([document_2.txt](document_2.txt)). Fifth, the split of the 172 successful identifications between attacker-role and victim-role participants is not described ([document_2.txt](document_2.txt)).

These gaps mean that the most defensible answer to the size question is the reported dialog count, supplemented by the annotation and interactional statistics, with derived volume figures treated as estimates.

## 10. Source Reliability Assessment

The documentation draws on two source files. *document_2.txt* is the more relevant and reliable source for the size question, because it contains the AntiScam dataset description, the annotation statistics, the collection methodology, and the third-party research note that directly addresses the corpus size ([document_2.txt](document_2.txt)). *document_1.txt* is relevant for research context and evaluation results but does not itself state the corpus size; it references AntiScam as an evaluation dataset and describes comparative model performance ([document_1.txt](document_1.txt)). Neither source is dated, so recency comparisons cannot be made, but *document_2.txt* should be prioritized for any factual claim about dataset size because its statements are internally consistent and repeated across multiple framings ([document_2.txt](document_2.txt)).

## 11. Conclusion

The AntiScam dataset is, by its headline measure, a corpus of **320 human–human anti-scam dialogs** collected through a role-playing Amazon customer service scam scenario on Amazon Mechanical Turk ([document_2.txt](document_2.txt)). Its manually annotated portion covers **100 dialogs and 3,044 sentences**, annotated by two expert annotators with linguistic training ([document_2.txt](document_2.txt)). At the interactional level, the full corpus averages **12.45 turns per conversation and 11.13 words per utterance** ([document_2.txt](document_2.txt)). At the outcome level, **172 of 320 users** successfully identified their partner as an attacker, equivalent to 53.75 percent ([document_2.txt](document_2.txt)).

Taken together, these figures describe a medium-scale, richly structured corpus that is fully populated at the dialog level but annotated at approximately one-third of that scale. Anyone citing the size of AntiScam should therefore specify which figure they mean—320 dialogs, 100 annotated dialogs, 3,044 annotated sentences, or the average interactional dimensions—because each represents a genuinely different aspect of the dataset's size.

## References

document_1.txt. (n.d.). *Results and analysis*.

document_2.txt. (n.d.). *AntiScam dataset description and third-party research note on the End-to-End Trainable Non-Collaborative Dialog System*.