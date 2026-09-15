# How Big Is the AntiScam Dataset?

## 1. Direct Answer to the Query

The AntiScam dataset is a corpus of **220 human–human anti-scam dialogs**, collected to support research on non-collaborative dialog systems and to learn human elicitation strategies ([Li et al., 2019](document_1.txt)). Each conversation averages **12.45 turns**, with an average utterance length of **11.13 words**, which places the corpus at roughly 2,700 conversational turns in total ([Li et al., 2019](document_1.txt)). A manually annotated subset covering **100 dialogs and 3,044 sentences** was produced by two expert annotators with linguistic training, achieving an averaged weighted kappa value of **0.874** ([Li et al., 2019](document_1.txt)). A third-party research note circulating alongside the paper reports a competing figure of **320 dialogs**; this report explains why the primary source's figure of 220 is the more defensible number while acknowledging the discrepancy ([Third-party research note, n.d.](document_2.txt)).

In short, AntiScam is a **small-to-medium, densely annotated, high-quality dialog corpus** rather than a large-scale dataset. Its size is deliberately modest because of the way it was collected—single-participation, incentivized role-play between paired crowdworkers—but its annotation depth compensates for the limited dialog count ([Li et al., 2019](document_1.txt)).

## 2. Size in the Primary Source

### 2.1 The headline number

The paper's "AntiScam Dataset" section states unambiguously: "We posted a role-playing task on the Amazon Mechanical Turk platform and collected a typing conversation dataset named AntiScam. We collected **220 human-human dialogs**" ([Li et al., 2019](document_1.txt)). The appendix section "Anti-Scam Collection Setting" repeats the figure: "We collected **220 human-human dialogs**. The average conversation length is 12.45 turns and the average utterance length is 11.13 words" ([Li et al., 2019](document_1.txt)). Because the number appears twice, in two structurally distinct parts of the paper, the 220-dialog count should be treated as the authors' intended, authoritative size claim.

### 2.2 Structural dimensions at a glance

The following table consolidates every size-related statistic reported in the primary source.

| Dimension | Reported value | Source |
|---|---|---|
| Total human–human dialogs | 220 | ([Li et al., 2019](document_1.txt)) |
| Manually annotated dialogs | 100 | ([Li et al., 2019](document_1.txt)) |
| Manually annotated sentences | 3,044 | ([Li et al., 2019](document_1.txt)) |
| Average conversation length | 12.45 turns | ([Li et al., 2019](document_1.txt)) |
| Average utterance length | 11.13 words | ([Li et al., 2019](document_1.txt)) |
| Users correctly identifying the attacker | 172 of 220 (78.2%) | ([Li et al., 2019](document_1.txt)) |
| Inter-annotator agreement | 0.874 averaged weighted kappa | ([Li et al., 2019](document_1.txt)) |
| Task-specific semantic slots | 13 | ([Li et al., 2019](document_1.txt)) |
| Train / validation / test split | 80% / 10% / 10% | ([Li et al., 2019](document_1.txt)) |

### 2.3 The annotated subset

Annotation was not applied to the whole corpus. The paper states that two expert annotators with linguistic training annotated **3,044 sentences across 100 dialogs** ([Li et al., 2019](document_1.txt)). This makes the annotated subset roughly **45% of the dialogs** (100 of 220) but the single most information-rich component of the dataset, since each sentence carries both an intent label and a semantic-slot label under the hierarchical scheme ([Li et al., 2019](document_1.txt)).

## 3. Reconciling the 220 vs. 320 Discrepancy

The third-party research note states that "the dataset contains **320 human-human dialogs**" and repeats "172 out of 320 users successfully identified their partner as an attacker" ([Third-party research note, n.d.](document_2.txt)). This conflicts directly with the primary paper, which reports 172 out of **220** ([Li et al., 2019](document_1.txt)).

Three considerations favor the primary source:

1. **Repetition and location.** The 220 figure appears twice in the original paper—once in the dataset description and once in the collection-setting appendix ([Li et al., 2019](document_1.txt)). The derivative note is a secondary summary whose stated purpose is to answer key questions, not to introduce new facts ([Third-party research note, n.d.](document_2.txt)).
2. **Internal arithmetic plausibility.** A 78.2% detection rate (172/220) is described by the authors as evidence that "the attackers are well trained and not too easily identifiable" ([Li et al., 2019](document_1.txt)). A rate of 53.75% (172/320) is possible in principle but is not the number the source text supports.
3. **A likely mechanism for the error.** The note's 320 plausibly arises from conflation: 220 collected dialogs plus the 100 annotated dialogs sum exactly to 320. Because the note treats "100 dialogs" as a subset of the total, it may have inadvertently added the subset to the whole ([Third-party research note, n.d.](document_2.txt); [Li et al., 2019](document_1.txt)).

**My assessment:** the best-supported size claim is **220 dialogs**, with **100 dialogs / 3,044 sentences** carrying manual annotation ([Li et al., 2019](document_1.txt)). Any downstream citation using 320 should be corrected or flagged.

## 4. Derived Size Estimates

Because the paper supplies averages rather than totals for turns and words, approximate totals can be computed:

- **Turns:** 220 dialogs × 12.45 turns ≈ **2,739 turns** ([Li et al., 2019](document_1.txt)).
- **Utterances and words:** if each turn contains one utterance from each of the two participants, the corpus contains roughly 5,478 utterances and, at 11.13 words each, approximately **61,000 words**. If "utterance" is used interchangeably with "turn," the lower-bound estimate is about **30,500 words** ([Li et al., 2019](document_1.txt)).
- **Annotation density:** within the annotated subset, 100 dialogs × 12.45 turns ≈ 1,245 turns carrying 3,044 sentences, i.e., roughly **2.4 sentences per turn** ([Li et al., 2019](document_1.txt)).
- **Extrapolated sentence count:** if annotation density held constant across the whole corpus, the full 220 dialogs would correspond to approximately **6,700 sentences** (220/100 × 3,044) ([Li et al., 2019](document_1.txt), derived).
- **Split sizes:** the 80/10/10 partition corresponds to roughly **176 training, 22 validation, and 22 test dialogs** ([Li et al., 2019](document_1.txt), derived).

## 5. Composition of the Corpus

Size is not only a matter of counts; the distribution of content types indicates how much of the corpus is on-task versus off-task. The paper reports the following counts across the annotated data ([Li et al., 2019](document_1.txt)):

| Intent category | Attacker | User |
|---|---|---|
| Refusal | 19 | 74 |
| Open question | 54 | 173 |
| Yes/no question | 117 | 165 |
| Social content (combined social intents) | 292 | 252 |

These figures reveal a corpus rich in the "off-task" material that gives non-collaborative dialog its distinctive character: users ask far more open questions (173 vs. 54) and yes/no questions (165 vs. 117) than attackers, because once users detect an attacker they are instructed to prolong the conversation ([Li et al., 2019](document_1.txt)). The 544 social-intent sentences (292 + 252) further indicate that a substantial share of the corpus is social rather than task content ([Li et al., 2019](document_1.txt)).

## 6. Comparative Scale: AntiScam Versus PersuasionForGood

The paper evaluates on two non-collaborative datasets, allowing a direct size comparison ([Li et al., 2019](document_1.txt)):

| Property | AntiScam | PersuasionForGood |
|---|---|---|
| Total dialogs | 220 | 1,017 |
| Annotated dialogs | 100 | 300 |
| Annotated sentences | 3,044 | Not reported |
| Average conversation length | 12.45 turns | 10.43 turns |
| Vocabulary size | Not reported | 8,141 |
| Collection platform | Amazon Mechanical Turk | Amazon Mechanical Turk |

AntiScam is therefore roughly **21.6% the size of PersuasionForGood** in dialog count (220/1,017), and about **one-third** its size in annotated dialogs (100 vs. 300) ([Li et al., 2019](document_1.txt)). Its dialogs are, on average, longer (12.45 vs. 10.43 turns), which partially offsets the smaller dialog count in terms of conversational content ([Li et al., 2019](document_1.txt)).

## 7. How the Collection Protocol Constrains Size

The modest scale is a direct consequence of design choices. Workers were randomly paired on Amazon Mechanical Turk, with one assigned the attacker role and the other the everyday-user role, each receiving private personal data and role instructions ([Li et al., 2019](document_1.txt)). Two constraints limited throughput:

1. **Single participation:** "Each worker can only participate once to prevent workers from knowing their partner's information and goals in advance" ([Li et al., 2019](document_1.txt)). This eliminated repeat contributors and capped the pool of dialogues.
2. **Incentives and role training:** attackers were trained to impersonate Amazon customer service and received bonuses for eliciting information; users received bonuses for detecting attackers and eliciting the attacker's name, address, and phone number ([Li et al., 2019](document_1.txt)).

These design decisions increase realism and annotation quality but limit the volume of data that can be gathered economically, which explains why the final corpus is 220 dialogs rather than several thousand ([Li et al., 2019](document_1.txt)).

## 8. A Separate Corpus: The Human-Evaluation Dialogs

It is important not to confuse the AntiScam dataset with the dialogs collected for human evaluation. For evaluation, 15 college-student volunteers each interacted with all five models at least three times, yielding **225 human–system dialogs** and 45 ratings per model ([Li et al., 2019](document_1.txt)). This evaluation corpus is distinct from the 220-dialog training/benchmark corpus and should not be added to it ([Li et al., 2019](document_1.txt)).

## 9. Conclusion

Taken together, the evidence supports a clear answer: **AntiScam contains 220 human–human dialogs**, averaging 12.45 turns and 11.13 words per utterance, with a manually annotated subset of **100 dialogs and 3,044 sentences** labeled by two linguistic experts at 0.874 weighted kappa agreement ([Li et al., 2019](document_1.txt)). The dataset is small relative to PersuasionForGood's 1,017 dialogs but is comparatively long-conversation and annotation-dense ([Li et al., 2019](document_1.txt)). The 320-dialog figure in the secondary research note appears to be an error, most plausibly arising from adding the 100 annotated dialogs to the 220 collected dialogs ([Third-party research note, n.d.](document_2.txt)). For any practical purpose—benchmark reporting, model training budgets, or dataset comparison—the figure to cite is **220 dialogs**, with the caveat that only the annotated 100-dialog subset supports the hierarchical intent and semantic-slot supervision the research relies on ([Li et al., 2019](document_1.txt)).

## References

Li, Y., Qian, K., Shi, W., & Yu, Z. (2019). *End-to-End Trainable Non-Collaborative Dialog System* (arXiv:1911.10742) [document_1.txt].

Third-party research note: End-to-End Trainable Non-Collaborative Dialog System [document_2.txt]. (n.d.).