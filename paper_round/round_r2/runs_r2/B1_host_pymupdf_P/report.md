# Sizing the ANTISCAM Dataset: A Detailed Report on the Scale, Composition, and Reporting Discrepancies of the Human-Human Anti-Scam Dialog Corpus

## Introduction

The ANTISCAM dataset is a specialized human-human dialogue corpus introduced by Li, Qian, Shi, and Yu (2019) to support research on non-collaborative dialog systems, specifically in the domain of anti-scam interactions ([Li et al., 2019](https://arxiv.org/abs/1911.10742)). The corpus was collected through a role-playing Amazon customer service scam scenario on Amazon Mechanical Turk, in which one participant acted as a scammer attempting to elicit personal information, while the other participant acted as a user who could detect the scammer and then attempt to prolong the conversation and elicit the scammer’s own information ([Li et al., 2019](https://arxiv.org/abs/1911.10742)). Because the dataset is relatively new and designed specifically for non-collaborative dialog research, its size and annotation depth are central to evaluating its utility as a benchmark. This report examines the size of the ANTISCAM dataset using the primary source paper and a third-party research note, resolves a discrepancy in the reported dialog count, and situates the dataset’s scale within the broader context of non-collaborative dialogue corpora.

## Core Size Metrics from the Primary Source

### Total Number of Human-Human Dialogs

The primary source paper reports that the ANTISCAM corpus contains **220 human-human dialogs** ([Li et al., 2019](https://arxiv.org/abs/1911.10742)). This figure appears twice in the paper: once in the “ANTISCAM Dataset” section and again in the Appendix under “Anti-Scam Collection Setting” ([Li et al., 2019](https://arxiv.org/abs/1911.10742)). Specifically, the paper states: “We collected 220 human-human dialogs” ([Li et al., 2019](https://arxiv.org/abs/1911.10742)). The repetition of this number in two separate sections strengthens its reliability as the authoritative total.

### Annotated Subset

Although the full corpus comprises 220 dialogs, only a subset was manually annotated for intent and semantic slot labels. The paper reports that **100 dialogs containing 3,044 sentences** were annotated by two expert annotators with linguistic training ([Li et al., 2019](https://arxiv.org/abs/1911.10742)). The annotation achieved an **averaged weighted kappa value of 0.874**, indicating strong inter-annotator agreement ([Li et al., 2019](https://arxiv.org/abs/1911.10742)). This means that the annotated portion of ANTISCAM represents approximately 45.5% of the total dialogs (100 out of 220), while the remaining 120 dialogs are unannotated but still available as raw conversational data.

### Conversation-Level Averages

The paper provides two key averages that characterize the size of individual dialogs within the corpus:
- **Average conversation length:** 12.45 turns ([Li et al., 2019](https://arxiv.org/abs/1911.10742)).
- **Average utterance length:** 11.13 words ([Li et al., 2019](https://arxiv.org/abs/1911.10742)).

These averages describe the full ANTISCAM corpus, not merely the annotated subset ([Li et al., 2019](https://arxiv.org/abs/1911.10742)). Based on these figures, the total corpus of 220 dialogs would contain approximately 2,739 conversational turns (220 × 12.45) and roughly 30,485 words (2,739 turns × 11.13 words per utterance, assuming one utterance per turn). This provides a rough estimate of the corpus’s overall token volume, although the paper does not report the exact total number of words or turns.

### Attacker Identification Rate

Another size-related outcome is the proportion of users who successfully identified their partner as an attacker. The paper reports that **172 out of 220 users** successfully identified their partner as an attacker ([Li et al., 2019](https://arxiv.org/abs/1911.10742)). This corresponds to a detection rate of approximately 78.2%. The paper interprets this as evidence that the attackers were well trained and not too easily identifiable ([Li et al., 2019](https://arxiv.org/abs/1911.10742)).

## Tabular Summary of ANTISCAM Size Indicators

| Metric | Value | Source |
|---|---|---|
| Total human-human dialogs | 220 | ([Li et al., 2019](https://arxiv.org/abs/1911.10742)) |
| Manually annotated dialogs | 100 | ([Li et al., 2019](https://arxiv.org/abs/1911.10742)) |
| Annotated sentences | 3,044 | ([Li et al., 2019](https://arxiv.org/abs/1911.10742)) |
| Inter-annotator agreement (weighted kappa) | 0.874 | ([Li et al., 2019](https://arxiv.org/abs/1911.10742)) |
| Average conversation length | 12.45 turns | ([Li et al., 2019](https://arxiv.org/abs/1911.10742)) |
| Average utterance length | 11.13 words | ([Li et al., 2019](https://arxiv.org/abs/1911.10742)) |
| Users who identified attacker | 172 out of 220 (≈78.2%) | ([Li et al., 2019](https://arxiv.org/abs/1911.10742)) |
| Estimated total turns (220 × 12.45) | ≈2,739 | Calculated from ([Li et al., 2019](https://arxiv.org/abs/1911.10742)) |

## The Conflicting Figure in the Third-Party Research Note

A third-party research note on the same paper presents a different total for the ANTISCAM dataset. The note states that “the dataset contains **320 human-human dialogs**” and that “172 out of **320** users successfully identified their partner as an attacker” ([Third-party research note, n.d.](document_2.txt)). This directly contradicts the primary source, which reports 220 dialogs and 172 out of 220 users ([Li et al., 2019](https://arxiv.org/abs/1911.10742)).

### Resolving the Discrepancy

Several factors indicate that the **220-dialog figure is correct** and that the 320 figure in the note is erroneous:

1. **Primary source authority:** The paper by Li et al. is the original source that describes the collection and composition of the ANTISCAM dataset ([Li et al., 2019](https://arxiv.org/abs/1911.10742)). The third-party note is a secondary summary ([Third-party research note, n.d.](document_2.txt)).
2. **Internal consistency:** The paper reports 220 dialogs in two separate sections (the dataset description and the appendix), and it also reports the attacker detection rate as “172 out of 220” ([Li et al., 2019](https://arxiv.org/abs/1911.10742)). The note’s claim that the paper reports 320 is not supported by any passage in the primary source.
3. **Numerator agreement, denominator disagreement:** Both sources agree on the numerator (172 users identified the attacker), but they disagree on the denominator (220 vs. 320). This pattern suggests that the note may have accidentally altered the total while preserving the detection count, or that it conflated the ANTISCAM total with another number from the paper (e.g., the number of dialogs in the PERSUASIONFORGOOD dataset is 1,017, not 320; the human evaluation used 225 dialogs, not 320) ([Li et al., 2019](https://arxiv.org/abs/1911.10742)).
4. **No supporting evidence for 320:** A thorough review of the primary source reveals no mention of 320 dialogs anywhere ([Li et al., 2019](https://arxiv.org/abs/1911.10742)).

Therefore, the most reliable conclusion is that the ANTISCAM dataset comprises **220 human-human dialogs**, and the third-party note’s figure of 320 is likely a transcription or summarization error ([Third-party research note, n.d.](document_2.txt); [Li et al., 2019](https://arxiv.org/abs/1911.10742)).

## Additional Dimensions of Dataset Scale and Annotation Depth

Beyond the raw dialog count, the size of ANTISCAM can be characterized by its annotation schema and the distribution of intents and semantic slots.

### Hierarchical Intent Annotation

The dataset uses a hierarchical intent annotation scheme that separates on-task and off-task intents ([Li et al., 2019](https://arxiv.org/abs/1911.10742)). For ANTISCAM, three on-task intents are defined: **elicitation**, **providing information**, and **refusal** ([Li et al., 2019](https://arxiv.org/abs/1911.10742)). The off-task intents are universal across non-collaborative tasks and include six general intents (open question, yes/no question, negative answer, positive answer, responsive statement, nonresponsive statement) and six social intents (greeting, thanking, respond to thank, apology, closing, hold) ([Li et al., 2019](https://arxiv.org/abs/1911.10742)). This results in a total of 15 intent categories available for annotation.

### Semantic Slot Annotation

The paper also defines **13 main semantic slots** for the anti-scam task, such as order detail, order update, payment, name, identity, address, phone number, card information, card number, card CVS, card date, account detail, and others ([Li et al., 2019](https://arxiv.org/abs/1911.10742)). Each sentence in the annotated subset (3,044 sentences) was labeled with one or more intents and semantic slots ([Li et al., 2019](https://arxiv.org/abs/1911.10742)).

### Intent Distribution Counts

The paper provides specific counts that further illustrate the scale and composition of the annotated data:
- Users produced **74 refusals** compared to attackers’ **19 refusals** ([Li et al., 2019](https://arxiv.org/abs/1911.10742)).
- Users asked **173 open questions** compared to attackers’ **54** ([Li et al., 2019](https://arxiv.org/abs/1911.10742)).
- Users asked **165 yes/no questions** compared to attackers’ **117** ([Li et al., 2019](https://arxiv.org/abs/1911.10742)).
- Social content sentences totaled **292 for attackers** and **252 for users** ([Li et al., 2019](https://arxiv.org/abs/1911.10742)).

These counts confirm that the annotated subset is rich in off-task and social content, which is central to the dataset’s purpose ([Li et al., 2019](https://arxiv.org/abs/1911.10742)).

## Comparative Scale: ANTISCAM Versus PERSUASIONFORGOOD

The paper evaluates its proposed model on two non-collaborative datasets: ANTISCAM and PERSUASIONFORGOOD ([Li et al., 2019](https://arxiv.org/abs/1911.10742)). Comparing their sizes provides useful context.

| Dataset | Total Dialogs | Annotated Dialogs | Average Conversation Length | Vocabulary Size |
|---|---|---|---|---|
| ANTISCAM | 220 | 100 | 12.45 turns | Not reported |
| PERSUASIONFORGOOD | 1,017 | 300 | 10.43 turns | 8,141 |

Note: PERSUASIONFORGOOD data from ([Li et al., 2019](https://arxiv.org/abs/1911.10742)).

ANTISCAM is approximately one-fifth the size of PERSUASIONFORGOOD in terms of total dialogs, and one-third the size in terms of annotated dialogs ([Li et al., 2019](https://arxiv.org/abs/1911.10742)). However, ANTISCAM’s average conversation length is slightly longer (12.45 vs. 10.43 turns), suggesting that individual ANTISCAM dialogs are more extended ([Li et al., 2019](https://arxiv.org/abs/1911.10742)). The vocabulary size for ANTISCAM is not reported in the paper, which limits direct lexical comparisons ([Li et al., 2019](https://arxiv.org/abs/1911.10742)).

## Human Evaluation Scale as a Separate Metric

The paper also reports a human evaluation conducted with 15 college-student volunteers who role-played as attackers ([Li et al., 2019](https://arxiv.org/abs/1911.10742)). This evaluation collected **225 dialogs** in total, with each of five models receiving 45 human ratings ([Li et al., 2019](https://arxiv.org/abs/1911.10742)). While this evaluation scale is distinct from the dataset size, it is worth noting because it demonstrates the research effort surrounding the corpus. The 225 evaluation dialogs do not form part of the ANTISCAM dataset itself; they were generated during testing ([Li et al., 2019](https://arxiv.org/abs/1911.10742)).

## Limitations and Implications of Dataset Size

With 220 total dialogs and only 100 annotated dialogs, ANTISCAM is a relatively small corpus by contemporary dialogue dataset standards ([Li et al., 2019](https://arxiv.org/abs/1911.10742)). This small size presents both advantages and limitations:

- **Advantages:** The dense, multi-sentence annotation (3,044 sentences in 100 dialogs) and the hierarchical intent scheme provide rich supervision for training end-to-end models ([Li et al., 2019](https://arxiv.org/abs/1911.10742)). The paper demonstrates that the model (MISSA) trained on this small dataset can outperform baselines in terms of fluency, coherence, engagement, and task success ([Li et al., 2019](https://arxiv.org/abs/1911.10742)).
- **Limitations:** The small number of dialogs may limit generalization to broader scam scenarios. The paper itself notes that the model still produces responses inconsistent with distant conversation history because GPT can only track a limited span ([Li et al., 2019](https://arxiv.org/abs/1911.10742)). The authors call for future work to address longer context tracking ([Li et al., 2019](https://arxiv.org/abs/1911.10742)).

From an impartial standpoint, the ANTISCAM dataset should be understood as a **pilot-scale, deeply annotated corpus** rather than a large-scale resource. Its value lies in its novel task design and annotation scheme rather than in its raw volume ([Li et al., 2019](https://arxiv.org/abs/1911.10742)).

## Conclusion

The ANTISCAM dataset contains **220 human-human anti-scam dialogs** collected via a role-playing Amazon customer service scam scenario on Amazon Mechanical Turk ([Li et al., 2019](https://arxiv.org/abs/1911.10742)). Of these, **100 dialogs (3,044 sentences)** were manually annotated by two expert annotators with linguistic training, achieving a weighted kappa of 0.874 ([Li et al., 2019](https://arxiv.org/abs/1911.10742)). The average conversation length is **12.45 turns**, and the average utterance length is **11.13 words** ([Li et al., 2019](https://arxiv.org/abs/1911.10742)). In total, **172 out of 220 users** successfully identified their partner as an attacker ([Li et al., 2019](https://arxiv.org/abs/1911.10742)).

A third-party research note incorrectly reports the dataset size as 320 dialogs ([Third-party research note, n.d.](document_2.txt)). Based on the primary source’s consistent and repeated reporting of 220 dialogs in two separate sections, the correct size is **220 dialogs**. The 320 figure in the note appears to be an error, possibly a transcription mistake or a conflation with another number from the paper. Researchers relying on ANTISCAM should therefore use the 220-dialog figure as the authoritative total and treat the 100-dialog annotated subset as the labeled portion available for supervised learning.

## References

Li, Y., Qian, K., Shi, W., & Yu, Z. (2019). *End-to-End Trainable Non-Collaborative Dialog System* (document_1.txt). arXiv preprint arXiv:1911.10742. https://arxiv.org/abs/1911.10742

Third-party research note: End-to-End Trainable Non-Collaborative Dialog System (document_2.txt). (n.d.).