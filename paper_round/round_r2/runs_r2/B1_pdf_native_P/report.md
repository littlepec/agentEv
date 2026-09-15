# How Big Is the AntiScam Dataset?

## Introduction

The question of how "big" a conversational dataset is can be answered along several distinct axes: the number of conversations it contains, the number of conversations that carry human annotation, the number of sentences annotated, the typical length of each conversation, and the typical length of each utterance within it. For the AntiScam corpus, all of these dimensions are reported, and they do not all point to the same single number. A responsible answer therefore requires disaggregating the headline figure from the annotation footprint and from the conversational scale metrics ([Document 2](document_2.txt)).

This report provides a consolidated answer to the query "How big is the ANTISCAM dataset?" It uses only the information supplied in the source document, prioritizes figures that the source attributes directly to the underlying paper ("End-to-End Trainable Non-Collaborative Dialog System"), and treats a third-party research note contained in the same source as corroborating rather than primary evidence ([Document 2](document_2.txt)). Where figures are derived rather than reported, this is explicitly flagged as the author's own calculation.

## Direct Answer: The Headline Size of AntiScam

The AntiScam dataset comprises **320 human-human dialogs** ([Document 2](document_2.txt)). This is the figure the source describes as the dataset's size: "In sum, AntiScam is a human-human anti-scam dialog corpus collected via a role-playing Amazon customer service scam scenario on Amazon Mechanical Turk. Its size is 320 human-human dialogs" ([Document 2](document_2.txt)). The same total is repeated consistently throughout the source, which states that "the total dataset comprises 320 human-human dialogs" and that "the dataset contains 320 human-human dialogs" ([Document 2](document_2.txt)).

It is worth emphasizing that the 320-dialog figure is the total corpus size, not the annotated size. The source draws this distinction explicitly: "The total dataset comprises 320 human-human dialogs. The manually annotated subset comprises 100 dialogs and 3,044 sentences" ([Document 2](document_2.txt)). Any downstream user of AntiScam who requires gold-standard linguistic annotation is therefore working with roughly one-third of the corpus, a point developed in the next section.

## Composition and Provenance of the Corpus

Understanding what the 320 dialogs consist of clarifies what "size" means in substantive terms. According to the source, AntiScam is a "human-human anti-scam dialog corpus" created "to learn human elicitation strategies" ([Document 2](document_2.txt)). The collection method was a role-playing setup: participants engaged in a "role-playing Amazon customer service scam scenario" hosted on Amazon Mechanical Turk ([Document 2](document_2.txt)). This provenance matters for interpreting size, because it means each of the 320 units is a two-party interaction between crowd workers rather than a scraped, in-the-wild log or a human-machine exchange ([Document 2](document_2.txt)).

The source also situates the corpus within a specific research program: AntiScam "serves as the dataset for non-collaborative dialog research in the paper" titled "End-to-End Trainable Non-Collaborative Dialog System" ([Document 2](document_2.txt)). In other words, the 320-dialog total is the resource that underwrites an entire study of non-collaborative dialogue, which is a useful indicator of scale relative to purpose, even if the source does not provide comparative benchmarks against other corpora.

## Annotation Footprint: The 100-Dialog, 3,044-Sentence Subset

The second major dimension of size concerns annotation. The source reports that "a subset of 100 dialogs containing 3,044 sentences was manually annotated," and that "two expert annotators who have linguistic training performed this annotation" ([Document 2](document_2.txt)). This is consistently restated: the annotation statistics "cover 100 dialogs and 3,044 sentences, annotated by two expert annotators with linguistic training" ([Document 2](document_2.txt)).

Three features of this annotation footprint deserve attention.

First, the annotation is partial. Only 100 of the 320 dialogs in the corpus carry manual annotation. Expressed as a proportion, this is 31.25% of the total corpus (author's calculation based on the reported figures of 100 and 320) ([Document 2](document_2.txt)).

Second, the annotation was performed by two experts with linguistic training rather than by crowdworkers, which the source presents as a quality characteristic of the annotation statistics ([Document 2](document_2.txt)).

Third, the sentence count of 3,044 provides the finest-grained measure of corpus size available. Dividing the reported sentence total by the reported annotated dialog count yields approximately 30.44 sentences per annotated dialog (author's calculation from 3,044 and 100) ([Document 2](document_2.txt)). This derived figure should be read as an average across the annotated subset only, not across the full 320-dialog corpus.

## Conversational Scale: Turns and Utterances

The source reports two average-length statistics. The "average conversation length is 12.45 turns," and the "average utterance length is 11.13 words" ([Document 2](document_2.txt)). Critically, the source specifies that "these averages describe the full AntiScam corpus," not merely the 100 annotated dialogs ([Document 2](document_2.txt)). This attribution is important for anyone attempting to reconcile the length statistics with the annotation statistics, because the two sets of numbers describe different populations.

An additional caution is warranted regarding units. The 12.45-turn average and the 11.13-word average are expressed in different units from the 3,044-sentence figure. The source does not define the relationship between "sentences," "turns," and "utterances," and it does not state how many utterances comprise a turn. Consequently, the derived value of roughly 30.44 sentences per annotated dialog and the reported value of 12.45 turns per conversation cannot be directly divided to yield a sentences-per-turn figure without additional assumptions the source does not supply ([Document 2](document_2.txt)). The prudent reading is that the corpus is dense at the sentence level relative to its turn count, but the exact ratio is not established by the available information.

## Participant-Level Size: The 172 Identifiers

A final size-adjacent statistic concerns outcomes rather than volume. The source reports that "172 out of 320 users successfully identified their partner as an attacker" and describes this as "part of the AntiScam dataset description" ([Document 2](document_2.txt)). This figure is anchored to the full 320-dialog corpus, since it is expressed as a fraction of 320 users.

As a derived proportion, 172 out of 320 corresponds to 53.75% of users (author's calculation from the reported figures of 172 and 320) ([Document 2](document_2.txt)). For present purposes, the significance of this statistic is that it confirms the denominator of the corpus: the participant count and the dialog count align at 320, which reinforces that the dataset contains 320 two-party interactions rather than 320 participants distributed across a different number of conversations ([Document 2](document_2.txt)).

## Consolidated Table of Reported and Derived Figures

The following table separates figures the source attributes to the paper from figures computed for this report.

| Metric | Value | Status | Population described |
|---|---|---|---|
| Total dialogs | 320 | Reported ([Document 2](document_2.txt)) | Full corpus |
| Manually annotated dialogs | 100 | Reported ([Document 2](document_2.txt)) | Annotated subset |
| Manually annotated sentences | 3,044 | Reported ([Document 2](document_2.txt)) | Annotated subset |
| Expert annotators | 2 | Reported ([Document 2](document_2.txt)) | Annotated subset |
| Average conversation length | 12.45 turns | Reported ([Document 2](document_2.txt)) | Full corpus |
| Average utterance length | 11.13 words | Reported ([Document 2](document_2.txt)) | Full corpus |
| Users identifying partner as attacker | 172 | Reported ([Document 2](document_2.txt)) | Full corpus |
| Annotated share of corpus | ~31.25% | Derived (100 ÷ 320) | Full corpus |
| Sentences per annotated dialog | ~30.44 | Derived (3,044 ÷ 100) | Annotated subset |
| Attack-identification rate | ~53.75% | Derived (172 ÷ 320) | Full corpus |

## Assessment of Source Reliability and Internal Consistency

The source document contains both paper-attributed statistics and a section explicitly labeled "Third-party research note" ([Document 2](document_2.txt)). In assessing reliability, the paper-attributed statements should be given priority, because they purport to report what "the paper reports" directly rather than summarizing it second-hand ([Document 2](document_2.txt)). Reassuringly, the third-party note does not conflict with the paper-attributed figures: it independently states that "the dataset contains 320 human-human dialogs" and that "the corpus serves as the dataset for non-collaborative dialog research in the paper" ([Document 2](document_2.txt)).

Internal consistency across the source is also strong. The figure of 320 dialogs appears in the summary statement, in the annotation discussion, and in the third-party note; the annotation figures of 100 dialogs and 3,044 sentences appear in multiple passages; and the length statistics of 12.45 turns and 11.13 words recur consistently ([Document 2](document_2.txt)). No contradictory numbers appear anywhere in the supplied material. On this basis, the 320-dialog total and the 100-dialog / 3,044-sentence annotation subset can be treated as the reliable answer to the size question.

## Conclusion

The AntiScam dataset is **320 human-human dialogs in total**, collected through a role-playing Amazon customer service scam scenario on Amazon Mechanical Turk ([Document 2](document_2.txt)). Within that corpus, a manually annotated subset of **100 dialogs containing 3,044 sentences** was labeled by two expert annotators with linguistic training, representing roughly 31.25% of the corpus ([Document 2](document_2.txt)). Conversations average **12.45 turns** and utterances average **11.13 words**, with both averages characterizing the full corpus rather than the annotated subset alone ([Document 2](document_2.txt)). Finally, **172 of the 320 users** successfully identified their partner as an attacker, a figure that confirms the 320-unit denominator of the dataset ([Document 2](document_2.txt)).

Taken together, these figures establish a corpus that is moderate in conversational count but explicitly structured in two tiers: a fully collected set of 320 dialogs and a linguistically annotated core of 100 dialogs and 3,044 sentences. Anyone reporting the size of AntiScam should state which tier they mean, because the difference between 320 dialogs and 100 annotated dialogs is material to how the dataset can be used ([Document 2](document_2.txt)).

## References

Document 2. (n.d.). *AntiScam dataset description and third-party research note* [Source document]. Retrieved from document_2.txt