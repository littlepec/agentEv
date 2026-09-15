# How Big Is the AntiScam Dataset? A Detailed Assessment of Corpus Size, Annotation Coverage, and Source Reliability

## Introduction

The AntiScam dataset is a human-human, non-collaborative dialog corpus assembled to study how people defend themselves against social-engineering attacks and, conversely, how attackers elicit private information. It was introduced alongside the Multiple Intents and Semantic Slots Annotation Neural Network (MISSA) model as a benchmark resource for non-collaborative dialog research ([Li et al., 2019](https://arxiv.org/abs/1911.10742)). The question of how large AntiScam actually is matters for several reasons: corpus size determines the statistical power of any downstream model trained on it, governs the reliability of reported evaluation metrics, and shapes how confidently researchers can generalize findings to real-world anti-fraud dialog settings.

Answering the size question is less straightforward than it first appears, because the available information contains two conflicting figures. The primary source — the paper itself — reports a corpus of 220 human-human dialogs, whereas a third-party research note summarizing the same paper reports 320 human-human dialogs ([Third-Party Research Note](document_2.txt)). This report examines both claims, places them alongside the associated annotation and length statistics, and offers a reasoned conclusion about which figure should be treated as authoritative.

## Defining "Size" for a Dialog Corpus

Before quantifying AntiScam, it is useful to separate the several dimensions along which a dialog corpus can be measured, because the sources conflate them:

- **Total number of conversations (dialogs)** — the headline figure most people mean by "dataset size."
- **Number of annotated dialogs** — the subset that received manual linguistic annotation.
- **Number of annotated sentences** — the unit of annotation actually used in the paper.
- **Average conversation length in turns** — a measure of conversational depth.
- **Average utterance length in words** — a measure of per-turn lexical density.
- **Volume of social or off-task content** — a measure of how much of the corpus is not task-focused.

The primary source is explicit that annotation proceeded at the sentence level rather than the turn level: each conversation turn was segmented into single sentences, and each sentence was annotated rather than each turn ([Li et al., 2019](https://arxiv.org/abs/1911.10742)). This is an important methodological detail, because it means the "size" of the annotated resource is best expressed in sentences, not merely in dialogs.

## Primary-Source Report of AntiScam's Size

### Total number of dialogs

According to the paper's own description of the AntiScam dataset, the authors "collected 2 2 0 human-human dialogs" ([Li et al., 2019](https://arxiv.org/abs/1911.10742)). This figure appears in the dataset description section and is repeated in the appendix discussion of the anti-scam collection setting, where the authors again state that they "collected 2 2 0 human-human dialogs" ([Li et al., 2019](https://arxiv.org/abs/1911.10742)). The consistency of the 220 figure across two separate passages within the primary source strengthens its reliability.

The corpus was collected through a role-playing Amazon customer service scam scenario posted on the Amazon Mechanical Turk platform, in which one worker played an attacker posing as an Amazon customer service agent and the other played an everyday user ([Li et al., 2019](https://arxiv.org/abs/1911.10742)).

### Conversation and utterance length

The paper reports an average conversation length of 12.45 turns and an average utterance length of 11.13 words ([Li et al., 2019](https://arxiv.org/abs/1911.10742)). These averages are described as characterizing the full AntiScam corpus rather than only the annotated subset ([Third-Party Research Note](document_2.txt)). The paper also notes that the off-task dialog is interleaved within the task-oriented dialog, meaning that these 12.45 turns are not purely task-focused ([Li et al., 2019](https://arxiv.org/abs/1911.10742)).

### The manually annotated subset

Of the full corpus, a subset of 100 dialogs containing 3,044 sentences was manually annotated ([Li et al., 2019](https://arxiv.org/abs/1911.10742)). Two expert annotators with linguistic training performed this work, achieving a 0.874 averaged weighted kappa value — a strong inter-annotator agreement score ([Li et al., 2019](https://arxiv.org/abs/1911.10742)). The third-party note corroborates this subset exactly, reporting "100 dialogs containing 3,044 sentences" annotated by "two expert annotators who have linguistic training" ([Third-Party Research Note](document_2.txt)).

### Attacker-identification outcome

The paper reports that only 172 out of 220 users successfully identified their partner as an attacker, which the authors interpret as evidence that the attackers were well trained and not too easily identifiable ([Li et al., 2019](https://arxiv.org/abs/1911.10742)). This is a substantive size-related statistic: it establishes the denominator against which the 172 successful identifications should be read.

### Off-task and social content volume

The paper emphasizes that there is a "massive amount of social content (2 9 2 in total and 2 5 2 in tota1)" in the corpus, suggesting that social-intent sentences are important for maintaining the conversation ([Li et al., 2019](https://arxiv.org/abs/1911.10742)). This confirms that a substantial fraction of the corpus is off-task. The paper further observes that sentences from attackers and users have different intent distributions: users produce more refusals (74 versus 19), more open questions (173 versus 54), and more yes/no questions (165 versus 117) for off-task content than attackers do ([Li et al., 2019](https://arxiv.org/abs/1911.10742)).

## The Third-Party Note and Its Size Claim

The third-party research note states that AntiScam "contains 320 human-human dialogs" and asserts that "[t]he paper reports this total in its AntiScam dataset description" ([Third-Party Research Note](document_2.txt)). It then reports that "172 out of 320 users successfully identified their partner as an attacker" ([Third-Party Research Note](document_2.txt)).

The note's annotation statistics otherwise match the primary source precisely: 100 annotated dialogs, 3,044 annotated sentences, two expert annotators with linguistic training, 12.45 average conversation turns, and 11.13 average utterance words ([Third-Party Research Note](document_2.txt)). The disagreement is therefore localized and specific: it concerns the total dialog count (320 versus 220) and, consequently, the denominator in the attacker-identification statistic.

## Reconciling the Discrepancy

The two figures cannot both be correct as stated. Several observations point strongly toward 220 being the accurate total:

1. **Internal consistency of the primary source.** The paper states 220 in two distinct passages, in both the dataset description and the appendix collection-setting description ([Li et al., 2019](https://arxiv.org/abs/1911.10742)).
2. **Arithmetic coherence of the identification statistic.** Reading "172 out of 220" yields a 78.2% identification rate, which is consistent with the authors' framing that attackers were "not too easily identifiable" but were nonetheless detected by a clear majority ([Li et al., 2019](https://arxiv.org/abs/1911.10742)). Reading "172 out of 320" yields only 53.8%, which would substantially weaken the authors' characterization and would be an odd figure to describe in the same breath as a well-trained attacker pool.
3. **Selective divergence in the secondary source.** The third-party note agrees with the primary source on every other quantitative detail — 100 dialogs, 3,044 sentences, 12.45 turns, 11.13 words — suggesting that the 320 figure is an isolated transcription or summarization error rather than evidence of a different underlying dataset ([Third-Party Research Note](document_2.txt)).

My assessment is therefore that **the AntiScam dataset comprises 220 human-human dialogs**, and that the 320 figure circulated in the third-party note is unsupported by the primary source and should not be used in citation. Any downstream publication citing AntiScam's size should cite 220.

## Derived Size Metrics

Combining the figures above produces a fuller picture of the corpus's scale. The following derived values are my own arithmetic and are estimates rather than figures stated directly in the sources; they should be treated as such.

### Table 1. Reported and derived dimensions of AntiScam

| Dimension | Value | Status | Source |
|---|---|---|---|
| Total human-human dialogs | 220 | Reported | ([Li et al., 2019](https://arxiv.org/abs/1911.10742)) |
| Total dialogs (alternative claim) | 320 | Reported, disputed | ([Third-Party Research Note](document_2.txt)) |
| Annotated dialogs | 100 | Reported | ([Li et al., 2019](https://arxiv.org/abs/1911.10742)) |
| Annotated sentences | 3,044 | Reported | ([Li et al., 2019](https://arxiv.org/abs/1911.10742)) |
| Average conversation length | 12.45 turns | Reported | ([Li et al., 2019](https://arxiv.org/abs/1911.10742)) |
| Average utterance length | 11.13 words | Reported | ([Li et al., 2019](https://arxiv.org/abs/1911.10742)) |
| Inter-annotator agreement | 0.874 weighted kappa | Reported | ([Li et al., 2019](https://arxiv.org/abs/1911.10742)) |
| Users identifying attacker | 172 of 220 | Reported | ([Li et al., 2019](https://arxiv.org/abs/1911.10742)) |
| Identification rate | ~78.2% | Derived | Calculated from ([Li et al., 2019](https://arxiv.org/abs/1911.10742)) |
| Annotated coverage of corpus | ~45.5% of dialogs | Derived | Calculated from ([Li et al., 2019](https://arxiv.org/abs/1911.10742)) |
| Sentences per annotated dialog | ~30.4 | Derived | Calculated from ([Li et al., 2019](https://arxiv.org/abs/1911.10742)) |
| Approximate total corpus turns | ~2,739 | Derived | Calculated from 220 × 12.45 |
| Semantic slots defined | 13 | Reported | ([Li et al., 2019](https://arxiv.org/abs/1911.10742)) |

The derived coverage figure is particularly revealing: only about 45.5% of the 220 dialogs received manual sentence-level annotation, yet those 100 dialogs yielded 3,044 annotated sentences — roughly 30 sentences per dialog across an average of 12.45 turns ([Li et al., 2019](https://arxiv.org/abs/1911.10742)). This implies that a typical annotated dialog contains multiple sentences per turn, which is consistent with the paper's methodological choice to segment turns into sentences before annotation ([Li et al., 2019](https://arxiv.org/abs/1911.10742)).

### Table 2. AntiScam compared with the PersuasionForGood corpus

| Metric | AntiScam | PersuasionForGood |
|---|---|---|
| Total dialogs | 220 | 1,017 |
| Annotated dialogs | 100 | 300 |
| Average conversation length | 12.45 turns | 10.43 turns |
| Vocabulary size | Not reported | 8,141 |
| On-task intents | 3 (elicitation, providing_information, refusal) | 9 (donation-related) |
| Off-task intents | 12 (6 general + 6 social) | 12 (shared scheme) |

Sources: AntiScam figures from ([Li et al., 2019](https://arxiv.org/abs/1911.10742)); PersuasionForGood figures as reported in the same paper ([Li et al., 2019](https://arxiv.org/abs/1911.10742)).

## Significance of the Corpus Size

AntiScam's size is modest by contemporary dialog-corpus standards, sitting well below the 1,017 dialogs of the PersuasionForGood dataset described in the same paper ([Li et al., 2019](https://arxiv.org/abs/1911.10742)). The authors acknowledge this context directly, noting that "as non-collaborative tasks are still relatively new to the study of dialog systems, there are insufficiently many meaningful datasets for evaluation," and expressing the hope that AntiScam provides "a valuable example" ([Li et al., 2019](https://arxiv.org/abs/1911.10742)).

The corpus was nevertheless designed to serve as a benchmark: the authors describe it as "designed to interleave the on-task and off-task contents in the conversation" and as able to "serve as a benchmark dataset for similar non-collaborative tasks" ([Li et al., 2019](https://arxiv.org/abs/1911.10742)). It also underpins the paper's human evaluation, for which 15 college-student volunteers simulated attackers and produced 225 dialogs against five models, with each model receiving 45 human ratings ([Li et al., 2019](https://arxiv.org/abs/1911.10742)). Importantly, this 225-dialog human evaluation set is a separate artifact from the 220-dialog training corpus and should not be conflated with it.

The paper reports that MISSA maintained longer conversations (14.9 turns) than the TransferTransfo baseline (8.5 turns) and achieved a higher task success score (1.294 versus 1.025) on AntiScam ([Li et al., 2019](https://arxiv.org/abs/1911.10742)). The dataset's modest size does not appear to have prevented the authors from detecting meaningful differences between models, though it does limit how far the results can be generalized.

## Confidence Assessment and Limitations

The principal limitation of this analysis is that the available information contains an unresolved internal contradiction. I have argued that the primary source's 220-dialog figure should prevail, based on its internal repetition, its arithmetic coherence with the 172-user identification statistic, and the pattern of divergence in the secondary source ([Li et al., 2019](https://arxiv.org/abs/1911.10742); [Third-Party Research Note](document_2.txt)). However, without access to the released data — the paper states that code and data are available at the AntiScam repository ([Li et al., 2019](https://arxiv.org/abs/1911.10742)) — the discrepancy cannot be definitively closed by direct inspection.

A second limitation is that the reported averages (12.45 turns, 11.13 words) are described as characterizing the full corpus, and it is not stated whether the 100-dialog annotated subset is representative of the whole ([Third-Party Research Note](document_2.txt)). Derived figures such as sentences-per-dialog and estimated total turn counts therefore carry an associated uncertainty that is not quantified in the sources.

## Conclusion

The most defensible answer to the question "How big is the AntiScam dataset?" is that it consists of **220 human-human anti-scam dialogs**, of which **100 dialogs containing 3,044 sentences were manually annotated** by two linguistic-trained expert annotators, achieving a **0.874 weighted kappa** agreement, with an **average conversation length of 12.45 turns** and an **average utterance length of 11.13 words** ([Li et al., 2019](https://arxiv.org/abs/1911.10742)). Of the 220 users in the corpus, **172 successfully identified their partner as an attacker** ([Li et al., 2019](https://arxiv.org/abs/1911.10742)). A competing claim of 320 dialogs appears in a third-party research note but is not corroborated by the primary source and is inconsistent with the paper's own identification statistics ([Third-Party Research Note](document_2.txt)). Researchers citing AntiScam should therefore use 220 as the total corpus size, treat 100 dialogs / 3,044 sentences as the annotated scale, and flag the 320 figure as erroneous.

## References

Li, Y., Qian, K., Shi, W., & Yu, Z. (2019). *End-to-End Trainable Non-Collaborative Dialog System* (arXiv:1911.10742). University of California, Davis. https://arxiv.org/abs/1911.10742

Third-party research note: End-to-End Trainable Non-Collaborative Dialog System (document_2.txt).