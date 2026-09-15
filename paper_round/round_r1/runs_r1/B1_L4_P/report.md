# How Big Is the AntiScam Dataset? A Source-Weighted Assessment of Corpus Size, Annotation Coverage, and Reporting Discrepancies

## Scope and Method of This Assessment

This report answers a single, deceptively simple question: how big is the AntiScam dataset? The answer requires more than quoting a number, because the two documents supplied to this analysis disagree. One document is the primary research paper describing AntiScam, "End-to-End Trainable Non-Collaborative Dialog System" by Li, Qian, Shi, and Yu of the University of California, Davis ([Li et al., 2019](https://arxiv.org/abs/1911.10742)). The other is a short third-party research note that summarizes the same paper and explicitly frames itself around questions of dataset size, dialog count, and annotation statistics ([Third-party research note, n.d.](https://arxiv.org/abs/1911.10742)).

Where sources conflict, this report privileges the primary source, applies internal-consistency checks, and reports derived estimates only with clearly stated assumptions. The conclusion reached is that AntiScam comprises **220 human-human dialogs**, with a manually annotated subset of **100 dialogs and 3,044 sentences** — and that the alternative figure of 320 dialogs reported in the secondary note is not supported by the primary text.

## The Headline Answer: Total Corpus Size

The primary source states directly and unambiguously: "We collected 2 2 0 human-human dialogs" ([Li et al., 2019](https://arxiv.org/abs/1911.10742)). This figure appears twice within the paper — once in the "AntiScam Dataset" section describing the corpus, and again in the "Anti-Scam Collection Setting" section of the Appendix, which documents the data-collection protocol ([Li et al., 2019](https://arxiv.org/abs/1911.10742)). The repeated appearance of the same number in two structurally independent sections of the paper (the main body and the methodological appendix) is a meaningful signal of reliability: the figure is not an isolated transcription artifact but a consistently reported property of the collection effort.

The paper also links the corpus to a public code and data release hosted at the UC Davis NLP GitLab repository, indicating that the dataset is intended to function as a reusable benchmark for non-collaborative dialog research ([Li et al., 2019](https://arxiv.org/abs/1911.10742); [UC Davis NLP, n.d.](https://gitlab.com/ucdavisnlp/antiscam)).

### Table 1. Competing Size Claims Across Sources

| Claim | Primary Paper (Li et al., 2019) | Third-Party Note | Assessment |
|---|---|---|---|
| Total human-human dialogs | 220 | 320 | Primary source preferred; 220 is internally consistent |
| Users identifying attacker | 172 out of 220 | 172 out of 320 | Same numerator, conflicting denominator |
| Detection rate implied | 78.2% | 53.8% | Primary source supports the higher rate |
| Annotated dialogs | 100 | 100 | Agreement |
| Annotated sentences | 3,044 | 3,044 | Agreement |

## Resolving the 220 Versus 320 Discrepancy

The third-party research note asserts that "The dataset contains 320 human-human dialogs. The paper reports this total in its AntiScam dataset description," and repeats that "Its size is 320 human-human dialogs" ([Third-party research note, n.d.](https://arxiv.org/abs/1911.10742)). This directly contradicts the primary text, which records 220 dialogs in both of its relevant sections ([Li et al., 2019](https://arxiv.org/abs/1911.10742)).

Deciding between these figures does not require external evidence, because the primary document contains an internal consistency test. The paper reports that "Only 1 7 2 out of 2 2 0 users successfully identified their partner as an attacker," and interprets this as evidence that "the attackers are well trained and not too easily identifiable" ([Li et al., 2019](https://arxiv.org/abs/1911.10742)). A detection rate of 172/220 equals approximately 78.2%. By contrast, the secondary note preserves the numerator of 172 but changes the denominator to 320, yielding 53.8% ([Third-party research note, n.d.](https://arxiv.org/abs/1911.10742)). The paper's own interpretive gloss — that most users *did* successfully identify their partner, but that attackers nevertheless remained difficult to detect — fits the 78.2% figure rather than the 53.8% figure, under which nearly half of all users would have failed to detect a deliberately adversarial partner.

Two competing explanations exist for the discrepancy. The first is a simple transcription or summarization error in the secondary note, which would be consistent with the note's otherwise close reproduction of the paper's numbers, including the annotation statistics of 100 dialogs and 3,044 sentences that both sources share ([Third-party research note, n.d.](https://arxiv.org/abs/1911.10742)). The second, less likely explanation is that the primary paper has a typographical error in its dialog total and that the true count is 320. On the available evidence, the first explanation is more plausible, because the 220 figure is corroborated by repetition across sections and by consistency with the reported detection outcome, whereas the 320 figure appears only in the derivative summary.

**Analyst position:** practitioners should treat 220 as the operative corpus size unless and until the released data itself is audited. The 320 figure should be flagged as unreliable in any downstream citation.

## Size Across Multiple Dimensions of Granularity

Raw dialog count is only one measure of a corpus's scale. The documents permit a multi-dimensional profile covering dialogs, turns, utterances, words, annotated sentences, and label space.

### Table 2. Multi-Dimensional Size Profile of AntiScam

| Dimension | Reported Value | Source |
|---|---|---|
| Human-human dialogs | 220 | ([Li et al., 2019](https://arxiv.org/abs/1911.10742)) |
| Average conversation length | 12.45 turns | ([Li et al., 2019](https://arxiv.org/abs/1911.10742)) |
| Average utterance length | 11.13 words | ([Li et al., 2019](https://arxiv.org/abs/1911.10742)) |
| Expert-annotated dialogs | 100 | ([Li et al., 2019](https://arxiv.org/abs/1911.10742)) |
| Expert-annotated sentences | 3,044 | ([Li et al., 2019](https://arxiv.org/abs/1911.10742)) |
| Inter-annotator agreement | 0.874 averaged weighted kappa | ([Li et al., 2019](https://arxiv.org/abs/1911.10742)) |
| Number of annotators | 2 (linguistically trained) | ([Li et al., 2019](https://arxiv.org/abs/1911.10742)) |
| Anti-scam semantic slots | 13 | ([Li et al., 2019](https://arxiv.org/abs/1911.10742)) |
| On-task intents (AntiScam) | 3 (elicitation, providing_information, refusal) | ([Li et al., 2019](https://arxiv.org/abs/1911.10742)) |
| Off-task intents (shared) | 12 (6 general + 6 social) | ([Li et al., 2019](https://arxiv.org/abs/1911.10742)) |
| Collection platform | Amazon Mechanical Turk | ([Li et al., 2019](https://arxiv.org/abs/1911.10742)) |

### Turn-Level and Utterance-Level Scale

Multiplying the reported averages yields a useful, if approximate, impression of conversation volume. At 220 dialogs and an average of 12.45 turns per dialog, the corpus contains approximately 2,739 turns in total. Applying the average utterance length of 11.13 words produces an estimated word volume of roughly 30,500 words, on the assumption that one utterance corresponds to one turn ([Li et al., 2019](https://arxiv.org/abs/1911.10742)).

That assumption should be stated explicitly, because the paper does not define whether a "turn" is a single speaker's contribution or a full exchange. If a turn denotes a complete exchange of two utterances, the estimated word volume would approximately double to the range of 60,000–61,000 words. Both figures should be treated as order-of-magnitude estimates rather than audited counts, since they are derived from rounded averages rather than from the released transcripts ([Li et al., 2019](https://arxiv.org/abs/1911.10742)).

### Sentence-Level and Annotation Scale

The most concrete measure of the corpus's analytical depth is the annotation layer. The paper reports that two expert annotators with linguistic training annotated 3,044 sentences drawn from 100 dialogs, achieving an averaged weighted kappa of 0.874 ([Li et al., 2019](https://arxiv.org/abs/1911.10742)). This means the manually annotated portion covers 100 of 220 dialogs, or approximately 45.5% of the corpus.

Dividing 3,044 sentences by 100 dialogs yields an average of roughly 30.4 sentences per annotated dialog. If that density were assumed to hold across the full corpus, the total sentence count would be approximately 6,700 sentences. This extrapolation is presented here strictly as an illustrative estimate: the paper does not claim the annotated subset is representative of the remaining dialogs, and manual annotation is expensive enough that unannotated dialogs may differ systematically ([Li et al., 2019](https://arxiv.org/abs/1911.10742)).

The annotation scheme itself contributes to the dataset's effective "size" in research terms. AntiScam is annotated with a hierarchical intent scheme separating task-specific on-task intents — elicitation, providing_information, and refusal — from a universal off-task layer comprising six general dialog acts (open_question, yes_no_question, positive_answer, negative_answer, responsive_statement, nonresponsive_statement) and six social acts (greeting, closing, apology, thanking, respond_to_thank, hold) ([Li et al., 2019](https://arxiv.org/abs/1911.10742)). It additionally carries a semantic slot scheme with 13 main slots for the anti-scam domain, such as credit card numbers, order details, payment, name, identity, address, phone number, and card information ([Li et al., 2019](https://arxiv.org/abs/1911.10742)). A corpus of 220 dialogs paired with this dual-layer annotation is therefore substantially richer per dialog than an unannotated corpus of the same raw size.

## Comparative Context: AntiScam Against PersuasionForGood

The paper evaluates its model on two non-collaborative datasets, which permits a direct size comparison. AntiScam, the corpus introduced by the paper, is smaller in dialog count than the pre-existing PersuasionForGood dataset, which consists of 1,017 dialogs, of which 300 are annotated with dialog acts, with an average conversation length of 10.43 turns and a vocabulary size of 8,141 ([Li et al., 2019](https://arxiv.org/abs/1911.10742)).

### Table 3. Size Comparison of the Two Non-Collaborative Datasets

| Metric | AntiScam | PersuasionForGood |
|---|---|---|
| Total dialogs | 220 | 1,017 |
| Annotated dialogs | 100 | 300 |
| Share annotated | ~45.5% | ~29.5% |
| Average conversation length | 12.45 turns | 10.43 turns |
| Average utterance length | 11.13 words | Not reported |
| Vocabulary size | Not reported | 8,141 |
| On-task intents defined | 3 | 9 |
| Task domain | Anti-scam (Amazon customer service scam) | Charitable donation persuasion |

The comparison reveals a trade-off rather than a simple ranking. AntiScam is roughly one-fifth the size of PersuasionForGood in total dialogs, yet it is annotated more densely as a proportion of the whole: about 45.5% of AntiScam dialogs carry manual annotation versus about 29.5% of PersuasionForGood ([Li et al., 2019](https://arxiv.org/abs/1911.10742)). Average conversation length is also modestly higher in AntiScam, at 12.45 turns compared with 10.43 turns ([Li et al., 2019](https://arxiv.org/abs/1911.10742)). The paper does not report a vocabulary size for AntiScam, so no comparison on that dimension is possible from the supplied information.

This context matters because the paper explicitly frames dataset scarcity as the motivation for building AntiScam in the first place, noting that non-collaborative tasks remain relatively new to dialog-system research and that there are "insufficiently many meaningful datasets for evaluation" ([Li et al., 2019](https://arxiv.org/abs/1911.10742)). A 220-dialog corpus is thus best understood not as a large dataset in absolute terms but as a deliberately constructed benchmark that interleaves on-task and off-task content in a way prior corpora did not ([Li et al., 2019](https://arxiv.org/abs/1911.10742)).

## Related Scale Figures: The Human Evaluation Corpus

For completeness, it is worth distinguishing the AntiScam training and annotation corpus from the separate human-evaluation dataset generated during the study. To assess model performance, the researchers recruited 15 college-student volunteers, each of whom role-played an attacker and interacted with all models at least three times; this produced 225 dialogs, and each model received 45 human ratings ([Li et al., 2019](https://arxiv.org/abs/1911.10742)). These 225 evaluation dialogs are not part of the 220-dialog AntiScam corpus and should not be conflated with it in any size accounting.

## Implications of the Size Figure for Research Use

The practical consequence of AntiScam's scale is visible in how the corpus was used. The paper reports an 80/10/10 train-validation-test split for fine-tuning MISSA on both AntiScam and PersuasionForGood ([Li et al., 2019](https://arxiv.org/abs/1911.10742)). Applied to a 220-dialog corpus, that split corresponds to roughly 176 training dialogs, 22 validation dialogs, and 22 test dialogs — a small test set that would tend to produce high-variance evaluation estimates. Any reader evaluating the reported metrics — including the intent and slot classifier accuracies of 84% and 77% respectively on AntiScam — should weigh them against that limited evaluation base ([Li et al., 2019](https://arxiv.org/abs/1911.10742)).

The corpus does, however, carry structurally interesting content that compensates in part for its modest size. The paper reports that both attackers and users produced substantial social content, and that user and attacker utterances exhibit different intent distributions — users produced more refusals (74 versus 19), more open questions (173 versus 54), and more yes/no questions (165 versus 117) than attackers ([Li et al., 2019](https://arxiv.org/abs/1911.10742)). These asymmetries are only measurable because the corpus is annotated at sentence level, which reinforces that annotation depth, not raw dialog count, is where AntiScam's value concentrates.

## Conclusion and Assessment

Based on the evidence supplied, the AntiScam dataset is best characterized as follows:

- **Total size:** 220 human-human anti-scam dialogs, collected via a role-playing Amazon customer service scam scenario on Amazon Mechanical Turk ([Li et al., 2019](https://arxiv.org/abs/1911.10742)).
- **Annotated subset:** 100 dialogs and 3,044 sentences, annotated by two linguistically trained experts with an averaged weighted kappa of 0.874 ([Li et al., 2019](https://arxiv.org/abs/1911.10742)).
- **Conversational characteristics:** average conversation length of 12.45 turns and average utterance length of 11.13 words ([Li et al., 2019](https://arxiv.org/abs/1911.10742)).
- **Label space:** a hierarchical scheme with 3 anti-scam-specific on-task intents, 12 universal off-task intents, and 13 anti-scam semantic slots ([Li et al., 2019](https://arxiv.org/abs/1911.10742)).

The competing claim of 320 dialogs originates solely in the secondary research note and conflicts with the primary paper's repeated statement of 220 as well as with the internal consistency of the reported detection rate ([Third-party research note, n.d.](https://arxiv.org/abs/1911.10742); [Li et al., 2019](https://arxiv.org/abs/1911.10742)). The defensible position is therefore that AntiScam is a **220-dialog corpus** — small in absolute volume relative to collaborative datasets and to PersuasionForGood, but comparatively well annotated and purpose-built for a research area that the authors themselves describe as data-poor ([Li et al., 2019](https://arxiv.org/abs/1911.10742)).

## References

Li, Y., Qian, K., Shi, W., & Yu, Z. (2019). *End-to-end trainable non-collaborative dialog system*. arXiv. https://arxiv.org/abs/1911.10742

Third-party research note on the AntiScam dataset [Unpublished research note]. (n.d.). https://arxiv.org/abs/1911.10742

UC Davis NLP. (n.d.). *AntiScam* [Code and data repository]. GitLab. https://gitlab.com/ucdavisnlp/antiscam