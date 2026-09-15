# How Big Is the AntiScam Dataset? A Detailed Assessment

## Introduction

The AntiScam dataset is a corpus of human-human anti-scam dialogs created to support research on non-collaborative dialog systems and, specifically, to learn human elicitation strategies in a role-played Amazon customer service scam scenario ([Li et al., 2019](https://gitlab.com/ucdavisnlp/antiscam)). Answering the question of how big this dataset is requires attention to several distinct dimensions of scale: the number of dialogs, the number of conversational turns, the volume of words and sentences, the size of the manually annotated subset, and the size of the label space used for annotation. The primary paper and an accompanying third-party research note converge on a consistent set of figures, which are consolidated and interpreted below. Where a total is not stated directly in the sources, this report labels it clearly as a derived estimate computed from reported averages.

## Headline Size: 220 Human-Human Dialogs

The most direct answer to the query is that the AntiScam dataset contains **220 human-human dialogs**. The paper states plainly that the authors "collected 2 2 0 human-human dialogs" for the corpus, which was gathered through a role-playing task posted on the Amazon Mechanical Turk platform ([Li et al., 2019](https://gitlab.com/ucdavisnlp/antiscam)). The third-party research note repeats this figure and identifies it as the size of the full corpus, noting that AntiScam "contains 220 human-human dialogs" and that "the total dataset comprises 220 human-human dialogs" ([Research Note, n.d.](https://gitlab.com/ucdavisnlp/antiscam)). There is no disagreement between the sources on this headline number, and no larger or smaller full-corpus count is reported anywhere in the provided materials.

## Conversational Length Dimensions

Beyond the raw dialog count, the sources report two average length measures for the full corpus. The average conversation length is **12.45 turns**, and the average utterance length is **11.13 words** ([Li et al., 2019](https://gitlab.com/ucdavisnlp/antiscam); [Research Note, n.d.](https://gitlab.com/ucdavisnlp/antiscam)). The research note explicitly clarifies that "these averages describe the full AntiScam corpus" rather than only the annotated subset ([Research Note, n.d.](https://gitlab.com/ucdavisnlp/antiscam)).

These averages permit approximate corpus-level estimates, although such estimates must be treated with caution because they are derived rather than directly reported. Multiplying 220 dialogs by 12.45 turns suggests roughly **2,739 conversational turns** in the corpus. Multiplying that turn estimate by the average utterance length of 11.13 words suggests approximately **30,500 words** of dialog text. Because the sources present only averages and not a directly reported word or turn total, these derived values are best understood as order-of-magnitude approximations that illustrate the corpus scale rather than as verified corpus statistics.

### Table 1. Directly Reported Size Figures for AntiScam

| Dimension | Reported Value | Source |
|---|---|---|
| Full corpus size | 220 human-human dialogs | ([Li et al., 2019](https://gitlab.com/ucdavisnlp/antiscam); [Research Note, n.d.](https://gitlab.com/ucdavisnlp/antiscam)) |
| Average conversation length | 12.45 turns | ([Li et al., 2019](https://gitlab.com/ucdavisnlp/antiscam); [Research Note, n.d.](https://gitlab.com/ucdavisnlp/antiscam)) |
| Average utterance length | 11.13 words | ([Li et al., 2019](https://gitlab.com/ucdavisnlp/antiscam); [Research Note, n.d.](https://gitlab.com/ucdavisnlp/antiscam)) |
| Manually annotated subset | 100 dialogs | ([Li et al., 2019](https://gitlab.com/ucdavisnlp/antiscam); [Research Note, n.d.](https://gitlab.com/ucdavisnlp/antiscam)) |
| Annotated sentences | 3,044 sentences | ([Li et al., 2019](https://gitlab.com/ucdavisnlp/antiscam); [Research Note, n.d.](https://gitlab.com/ucdavisnlp/antiscam)) |
| Annotators | 2 expert annotators with linguistic training | ([Li et al., 2019](https://gitlab.com/ucdavisnlp/antiscam); [Research Note, n.d.](https://gitlab.com/ucdavisnlp/antiscam)) |
| Inter-annotator agreement | 0.874 averaged weighted kappa | ([Li et al., 2019](https://gitlab.com/ucdavisnlp/antiscam)) |
| Semantic slots (anti-scam task) | 13 main semantic slots | ([Li et al., 2019](https://gitlab.com/ucdavisnlp/antiscam)) |
| On-task intents | 3 (elicitation, providing_information, refusal) | ([Li et al., 2019](https://gitlab.com/ucdavisnlp/antiscam)) |
| Off-task intents | 12 (6 general + 6 social) | ([Li et al., 2019](https://gitlab.com/ucdavisnlp/antiscam)) |

## Annotation Scale

The annotation scale of AntiScam is considerably smaller than the raw corpus and is one of the clearest size qualifications in the sources. Two expert annotators with linguistic training manually annotated **3,044 sentences spanning 100 dialogs**, achieving a 0.874 averaged weighted kappa value ([Li et al., 2019](https://gitlab.com/ucdavisnlp/antiscam); [Research Note, n.d.](https://gitlab.com/ucdavisnlp/antiscam)). This means that approximately 45% of the 220-dialog corpus (100 of 220 dialogs) received manual sentence-level annotation, while the remaining dialogs were not annotated by the expert team. The research note emphasizes this distinction, stating that "the manually annotated subset comprises 100 dialogs and 3,044 sentences" ([Research Note, n.d.](https://gitlab.com/ucdavisnlp/antiscam)).

A derived sentence-density estimate can be computed from the annotated subset: 3,044 sentences divided by 100 dialogs yields approximately **30.4 sentences per annotated dialog**. If that density were extended across the full corpus of 220 dialogs, the corpus would contain an estimated 6,700 sentences; however, this is a derived extrapolation, not a reported figure, and should be treated accordingly. The paper's note that an utterance "can consist of multiple sentences" helps explain why the sentence count exceeds the turn count ([Li et al., 2019](https://gitlab.com/ucdavisnlp/antiscam)).

## Label Space Size

The "size" of AntiScam also includes the size of its annotation vocabulary. The paper reports that the authors designed a hierarchical intent annotation scheme and a semantic slot annotation scheme for the dataset. For AntiScam, three on-task intents were defined—**elicitation**, **providing_information**, and **refusal**—because the task focuses on understanding and reacting to elicitations ([Li et al., 2019](https://gitlab.com/ucdavisnlp/antiscam)). The off-task intents are shared across tasks and comprise six general intents (**open_question**, **yes_no_question**, **positive_answer**, **negative_answer**, **responsive_statement**, and **nonresponsive_statement**) plus six social intents (**greeting**, **closing**, **apology**, **thanking**, **respond_to_thank**, and **hold**) ([Li et al., 2019](https://gitlab.com/ucdavisnlp/antiscam)). In total, the anti-scam intent scheme thus contains 15 distinct intents (3 on-task plus 12 off-task). In addition, the authors identified **13 main semantic slots** for the anti-scam task, covering entities such as credit card numbers and related personal details ([Li et al., 2019](https://gitlab.com/ucdavisnlp/antiscam)).

## Collection Design and Quality Indicators

The size of AntiScam is inseparable from its collection protocol. The corpus was collected through a role-playing Amazon customer service scam scenario on Amazon Mechanical Turk, in which two workers were randomly paired: one assigned the role of an attacker attempting to elicit personal information, and the other assigned the role of an everyday user aiming to protect their information and potentially elicit the attacker's information ([Li et al., 2019](https://gitlab.com/ucdavisnlp/antiscam)). Each worker could participate only once, which the authors state prevented workers from knowing their partner's information and goals in advance ([Li et al., 2019](https://gitlab.com/ucdavisnlp/antiscam)).

A notable quality indicator reported in both sources is that **172 out of 220 users successfully identified their partner as an attacker**, a figure that the paper uses to argue that the attackers "are well trained and not too easily identifiable" ([Li et al., 2019](https://gitlab.com/ucdavisnlp/antiscam); [Research Note, n.d.](https://gitlab.com/ucdavisnlp/antiscam)). Expressed as a proportion, this is approximately 78.2% of users. The sources also report differential intent distributions between attackers and users: compared with attackers, users produced more refusals (74 vs. 19), more open questions (173 vs. 54), and more yes/no questions (165 vs. 117) ([Li et al., 2019](https://gitlab.com/ucdavisnlp/antiscam)). The paper further reports a large amount of social content in the corpus—292 sentences in total for one party and 252 in total for the other—which the authors cite as evidence that social intent sentences are important for maintaining conversation ([Li et al., 2019](https://gitlab.com/ucdavisnlp/antiscam)).

## Comparative Scale Relative to PersuasionForGood

Placing AntiScam in comparative context helps clarify its size. The paper evaluates its MISSA model on both AntiScam and the existing PersuasionForGood dataset. PersuasionForGood consists of **1,017 dialogs**, of which **300 dialogs are annotated** with dialog acts; its average conversation length is **10.43 turns**, and its vocabulary size is reported as **8,141** ([Li et al., 2019](https://gitlab.com/ucdavisnlp/antiscam)). Relative to that dataset, AntiScam is substantially smaller in dialog count (220 vs. 1,017) but is purpose-built for non-collaborative dialog research and interleaves on-task and off-task content by design ([Li et al., 2019](https://gitlab.com/ucdavisnlp/antiscam)). The paper justifies creating AntiScam precisely because "there are insufficiently many meaningful datasets for evaluation" in non-collaborative tasks ([Li et al., 2019](https://gitlab.com/ucdavisnlp/antiscam)).

### Table 2. AntiScam Compared with PersuasionForGood

| Attribute | AntiScam | PersuasionForGood |
|---|---|---|
| Full corpus dialogs | 220 | 1,017 |
| Annotated dialogs | 100 | 300 |
| Annotated sentences | 3,044 | Not reported in provided sources |
| Average conversation length | 12.45 turns | 10.43 turns |
| Average utterance length | 11.13 words | Not reported in provided sources |
| Vocabulary size | Not reported | 8,141 |
| On-task intents | 3 | 9 |

The comparison figures for PersuasionForGood are drawn from the same paper ([Li et al., 2019](https://gitlab.com/ucdavisnlp/antiscam)).

## Evaluation Resources Associated with the Dataset

It is important not to conflate the size of the AntiScam corpus with the size of the human evaluation conducted using it. For human evaluation, the authors tested models with **15 college-student volunteers**, each of whom was asked to pretend to be an attacker and interact with all models at least three times; in total, **225 dialogs** were collected, and each model received a total of **45 human ratings** ([Li et al., 2019](https://gitlab.com/ucdavisnlp/antiscam)). These 225 evaluation dialogs are separate from the 220-dialog training corpus and should be counted separately when assessing dataset scale.

The paper also reports that the model was trained using an 80%/10%/10% split of the data for training, validation, and testing, respectively ([Li et al., 2019](https://gitlab.com/ucdavisnlp/antiscam)). For the AntiScam corpus of 220 dialogs, this implies roughly 176 training dialogs, 22 validation dialogs, and 22 test dialogs, though the sources do not state these split counts explicitly. The intent predictor reportedly achieved 84% accuracy and the semantic slot predictor 77% accuracy on the AntiScam dataset ([Li et al., 2019](https://gitlab.com/ucdavisnlp/antiscam)).

## Interpretation: What "Big" Means for AntiScam

Taken together, the evidence supports a multi-dimensional answer. AntiScam is a **small-to-medium-sized, purpose-built corpus**: 220 human-human dialogs, averaging 12.45 turns and 11.13 words per utterance, with a 100-dialog, 3,044-sentence manually annotated subset and a compact label space of 15 intents and 13 semantic slots ([Li et al., 2019](https://gitlab.com/ucdavisnlp/antiscam); [Research Note, n.d.](https://gitlab.com/ucdavisnlp/antiscam)). Its closest benchmark in the paper, PersuasionForGood, is roughly 4.6 times larger in dialog count but has a shorter average conversation length (10.43 turns) and a different annotation scope ([Li et al., 2019](https://gitlab.com/ucdavisnlp/antiscam)). The value of AntiScam therefore lies less in raw volume than in its deliberate design: it interleaves on-task and off-task content, was explicitly constructed for non-collaborative dialog research, and is publicly released with code and data ([Li et al., 2019](https://gitlab.com/ucdavisnlp/antiscam)). For researchers asking whether the dataset is large enough for their purposes, the honest answer is that it is a modestly sized corpus whose annotation coverage (100 of 220 dialogs) and average dialog length (12.45 turns) are the two figures most likely to constrain modeling choices.

## Conclusion

The AntiScam dataset is **220 human-human dialogs** in size, with an average conversation length of **12.45 turns** and an average utterance length of **11.13 words** ([Li et al., 2019](https://gitlab.com/ucdavisnlp/antiscam); [Research Note, n.d.](https://gitlab.com/ucdavisnlp/antiscam)). Manual sentence-level annotation covers a subset of **100 dialogs and 3,044 sentences**, produced by two expert annotators with linguistic training and achieving a 0.874 averaged weighted kappa ([Li et al., 2019](https://gitlab.com/ucdavisnlp/antiscam); [Research Note, n.d.](https://gitlab.com/ucdavisnlp/antiscam)). Its label space includes 3 on-task intents, 12 shared off-task intents, and 13 semantic slots ([Li et al., 2019](https://gitlab.com/ucdavisnlp/antiscam)). In comparative terms, it is smaller than the 1,017-dialog PersuasionForGood dataset but was specifically designed to fill a gap in non-collaborative dialog resources ([Li et al., 2019](https://gitlab.com/ucdavisnlp/antiscam)). Anyone citing the "size" of AntiScam should therefore specify which dimension they mean—dialogs, turns, sentences, annotated subset, or label inventory—because the reported figures differ meaningfully across these axes.

## References

Li, Y., Qian, K., Shi, W., & Yu, Z. (2019). *End-to-End Trainable Non-Collaborative Dialog System* [document_1.txt]. Retrieved September 15, 2026, from https://gitlab.com/ucdavisnlp/antiscam

Research Note. (n.d.). *Third-party research note: End-to-End Trainable Non-Collaborative Dialog System* [document_2.txt]. Retrieved September 15, 2026, from https://gitlab.com/ucdavisnlp/antiscam