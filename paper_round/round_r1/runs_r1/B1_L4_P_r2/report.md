# How Big Is the AntiScam Dataset? Corpus Size, Annotation Scale, and a Source Discrepancy

## Key Finding

The AntiScam dataset is a corpus of **220 human–human anti-scam dialogs**, collected through a role-playing Amazon customer service scam scenario hosted on Amazon Mechanical Turk ([Li et al., 2019](https://gitlab.com/ucdavisnlp/antiscam)). Within that corpus, a manually annotated subset covers **100 dialogs and 3,044 sentences**, labeled by two expert annotators with linguistic training who achieved a weighted kappa of 0.874 ([Li et al., 2019](https://gitlab.com/ucdavisnlp/antiscam)). The average conversation length is **12.45 turns**, and the average utterance length is **11.13 words** ([Li et al., 2019](https://gitlab.com/ucdavisnlp/antiscam)). One complication must be stated up front: a third-party research note that accompanies the paper asserts a larger total of **320 human–human dialogs** ([Third-Party Research Note, n.d.](#)). That claim conflicts with two explicit statements in the primary source and is therefore assessed below as the weaker of the two figures. The balance of this report examines the corpus size dimension by dimension, explains the discrepancy, and explains why the size of this particular dataset matters for the research program it supports.

## The Primary Size Figure: 220 Human–Human Dialogs

### Collection Design and Context

AntiScam was created to enrich the small pool of publicly available non-collaborative task datasets ([Li et al., 2019](https://gitlab.com/ucdavisnlp/antiscam)). The authors chose a popular Amazon customer service scam scenario and posted a role-playing task on Amazon Mechanical Turk in which two workers were randomly paired: one played an "attacker" posing as Amazon customer service and attempting to elicit personal information, while the other played an everyday user attempting to protect their information and, if the attacker was detected, to prolong the conversation and elicit the attacker's information in return ([Li et al., 2019](https://gitlab.com/ucdavisnlp/antiscam)). The resulting typed conversations form the corpus.

The primary source states plainly: "We collected 2 2 0 human-human dialogs" ([Li et al., 2019](https://gitlab.com/ucdavisnlp/antiscam)). The same source reports that the average conversation length is 12.45 turns and the average utterance length is 11.13 words, and that each worker could participate only once ([Li et al., 2019](https://gitlab.com/ucdavisnlp/antiscam)).

### Internal Consistency of the 220 Figure

The 220 figure appears more than once in the primary text. In the dataset description, the authors write that "Only 1 7 2 out of 2 2 0 users successfully identified their partner as an attacker, suggesting that the attackers are well trained and not too easily identifiable" ([Li et al., 2019](https://gitlab.com/ucdavisnlp/antiscam)). Two independent statements in the same source—the collection total and the detection denominator—agree on 220. This internal corroboration is the single strongest piece of evidence about the dataset's size, because both figures are drawn from the same documented collection process and are mutually reinforcing rather than independent estimates.

Using the reported numbers, 172 of 220 users detected their partner as an attacker, a detection rate of approximately **78.2%**. The authors interpret this as evidence that the attackers were well trained and not easily identifiable ([Li et al., 2019](https://gitlab.com/ucdavisnlp/antiscam)).

## The Conflicting Third-Party Figure: 320 Dialogs

### What the Note Claims

The third-party research note states that "The dataset contains 320 human-human dialogs" and repeats that "the total dataset comprises 320 human-human dialogs," while also reporting "172 out of 320 users successfully identified their partner as an attacker" ([Third-Party Research Note, n.d.](#)). The note otherwise reproduces the same annotation statistics as the primary source: a subset of 100 dialogs containing 3,044 sentences, two expert annotators, an average conversation length of 12.45 turns, and an average utterance length of 11.13 words ([Third-Party Research Note, n.d.](#)).

### Reliability Assessment and Judgment

Judged against the criteria of relevance, reliability, and proximity to the underlying evidence, the primary source is the more trustworthy record. It is the paper itself, authored by the team that collected the data, and it states 220 twice in mutually reinforcing ways ([Li et al., 2019](https://gitlab.com/ucdavisnlp/antiscam)). The third-party note is a secondary summary that carries no stated publication venue, no author attribution, and no locator of its own; it also mixes the study's own annotation figures with a headline total that the primary text never states ([Third-Party Research Note, n.d.](#)).

Two further observations reinforce the conclusion that 220 is the defensible figure. First, the note's own detection statistic (172) is inherited verbatim from the primary source, so the note is not an independent measurement—it is a restatement with one altered denominator ([Third-Party Research Note, n.d.](#)). Second, changing the denominator quietly changes the substantive finding about detection difficulty: 172/220 implies that roughly four in five users detected the attacker, whereas 172/320 implies that only a little over half did ([Li et al., 2019](https://gitlab.com/ucdavisnlp/antiscam)). No methodological explanation is offered for that shift in the note, which is characteristic of a transcription or inference error rather than a corrected dataset total ([Third-Party Research Note, n.d.](#)).

**My assessment:** the AntiScam corpus should be reported as **220 human–human dialogs**, with a note that a secondary research note circulating alongside the paper erroneously gives 320. Any downstream work that cites 320 should be corrected, because it also misstates the attacker-detection rate.

## Size Beyond Dialog Count: Turns, Sentences, and Words

Dialog count is only one measure of scale. The table below consolidates every size-related figure the sources provide, with derived quantities clearly identified as estimates rather than reported values.

| Dimension | Value | Status | Source |
|---|---|---|---|---|
| Human–human dialogs collected | 220 | Reported | ([Li et al., 2019](https://gitlab.com/ucdavisnlp/antiscam)) |
| Dialogs manually annotated | 100 | Reported | ([Li et al., 2019](https://gitlab.com/ucdavisnlp/antiscam)) |
| Sentences manually annotated | 3,044 | Reported | ([Li et al., 2019](https://gitlab.com/ucdavisnlp/antiscam)) |
| Average conversation length | 12.45 turns | Reported | ([Li et al., 2019](https://gitlab.com/ucdavisnlp/antiscam)) |
| Average utterance length | 11.13 words | Reported | ([Li et al., 2019](https://gitlab.com/ucdavisnlp/antiscam)) |
| Expert annotators | 2 | Reported | ([Li et al., 2019](https://gitlab.com/ucdavisnlp/antiscam)) |
| Inter-annotator agreement | 0.874 weighted kappa | Reported | ([Li et al., 2019](https://gitlab.com/ucdavisnlp/antiscam)) |
| Users who identified the attacker | 172 of 220 | Reported | ([Li et al., 2019](https://gitlab.com/ucdavisnlp/antiscam)) |
| Approximate total turns | ≈ 2,739 (220 × 12.45) | Derived estimate | ([Li et al., 2019](https://gitlab.com/ucdavisnlp/antiscam)) |
| Sentences per annotated dialog | ≈ 30.4 (3,044 ÷ 100) | Derived estimate | ([Li et al., 2019](https://gitlab.com/ucdavisnlp/antiscam)) |
| Extrapolated sentence count, full corpus | ≈ 6,700 (30.4 × 220) | Derived estimate, assumes uniform annotation density | ([Li et al., 2019](https://gitlab.com/ucdavisnlp/antiscam)) |
| Annotated share of the corpus | 45.5% of dialogs (100 of 220) | Derived estimate | ([Li et al., 2019](https://gitlab.com/ucdavisnlp/antiscam)) |

The derived figures should be read with appropriate caution. The paper does not report a total sentence count for the full 220-dialog corpus, nor a vocabulary size for AntiScam (the vocabulary size of 8,141 words belongs to the separate PersuasionForGood dataset) ([Li et al., 2019](https://gitlab.com/ucdavisnlp/antiscam)). A rough word-level estimate for the annotated subset, multiplying 3,044 sentences by the 11.13-word average utterance length, yields approximately 33,900 words, but because an utterance can contain multiple sentences, that product is better treated as an upper-bound style approximation than as a token count ([Li et al., 2019](https://gitlab.com/ucdavisnlp/antiscam)).

## Annotation Scale: What Portion of the Corpus Is Labeled

Roughly 45.5% of AntiScam dialogs (100 of 220) carry manual annotation ([Li et al., 2019](https://gitlab.com/ucdavisnlp/antiscam)). Annotation was performed at the sentence level rather than the turn level: the authors segment each conversation turn into single sentences and annotate each sentence, which allows a single utterance to carry multiple intents and multiple semantic slots ([Li et al., 2019](https://gitlab.com/ucdavisnlp/antiscam)). Two expert annotators with linguistic training labeled the 3,044 sentences, reaching a 0.874 averaged weighted kappa value—a level of agreement that supports the reliability of the label set despite the modest size of the corpus ([Li et al., 2019](https://gitlab.com/ucdavisnlp/antiscam)).

This annotation strategy means the labeled portion of the dataset is described in sentence units (3,044), while the corpus as a whole is described in dialog and turn units (220 dialogs; 12.45 turns on average) ([Li et al., 2019](https://gitlab.com/ucdavisnlp/antiscam)). For modeling purposes, the annotated subset is what supplies supervision for the intent and semantic-slot classifiers, with the full corpus available for dialogue-level language modeling.

## Composition: Intents, Slots, and Off-Task Content

Size in dialog count understates the informational breadth of the corpus. AntiScam uses a hierarchical annotation scheme in which on-task and off-task content are separated ([Li et al., 2019](https://gitlab.com/ucdavisnlp/antiscam)). On the anti-scam side, three task-specific intents are defined: *elicitation*, *providing_information*, and *refusal* ([Li et al., 2019](https://gitlab.com/ucdavisnlp/antiscam)). Off-task content is labeled with twelve shared categories—six general dialog acts (*open_question*, *yes_no_question*, *positive_answer*, *negative_answer*, *responsive_statement*, *nonresponsive_statement*) and six social acts (*greeting*, *thanking*, *respond_to_thank*, *apology*, *closing*, *hold*) ([Li et al., 2019](https://gitlab.com/ucdavisnlp/antiscam)).

A separate semantic slot scheme identifies 13 main slots in the anti-scam task, including *order_detail*, *order_update*, *payment*, *name*, *identity*, *address*, *phone_num*, *card_info*, *card_num*, *card_cvs*, *card_date*, *account_detail*, and *others* ([Li et al., 2019](https://gitlab.com/ucdavisnlp/antiscam)). The label inventory therefore comprises roughly 15 intent classes applicable to this task (3 on-task plus 12 off-task) and 13 semantic slot classes ([Li et al., 2019](https://gitlab.com/ucdavisnlp/antiscam)).

The distribution of labels also reveals how much social, off-task material the corpus contains: 292 social intent sentences from attackers and 252 from users, a total of 544 social sentences, which the authors cite as evidence that social intents are important for maintaining these conversations ([Li et al., 2019](https://gitlab.com/ucdavisnlp/antiscam)). Users produced more refusals than attackers (74 versus 19), more open questions (173 versus 54), and more yes/no questions (165 versus 117) ([Li et al., 2019](https://gitlab.com/ucdavisnlp/antiscam)). These asymmetries show that the corpus is not merely small in dialog count; it is also behaviorally rich per dialog.

## Comparative Scale: AntiScam Versus PersuasionForGood

Placing AntiScam in context clarifies what "220 dialogs" means in the non-collaborative literature. The paper evaluates on two datasets and reports their sizes side by side.

| Dataset | Dialogs | Annotated dialogs | Avg. conversation length | Vocabulary | Source |
|---|---|---|---|---|---|
| AntiScam | 220 | 100 | 12.45 turns | Not reported | ([Li et al., 2019](https://gitlab.com/ucdavisnlp/antiscam)) |
| PersuasionForGood | 1,017 | 300 | 10.43 turns | 8,141 | ([Li et al., 2019](https://gitlab.com/ucdavisnlp/antiscam)) |

AntiScam is thus roughly one-fifth the size of PersuasionForGood by raw dialog count (220 versus 1,017) and one-third its size by annotated dialog count (100 versus 300), while having slightly longer conversations on average (12.45 versus 10.43 turns) ([Li et al., 2019](https://gitlab.com/ucdavisnlp/antiscam)). For AntiScam, the paper does not report a vocabulary size, so a direct lexical-scale comparison is not possible from the available materials ([Li et al., 2019](https://gitlab.com/ucdavisnlp/antiscam)).

## Evaluation-Scale Data That Is Not the Corpus

One number that could be mistaken for corpus size is the human evaluation scale. The authors tested models with 15 college-student volunteers who each pretended to be an attacker and interacted with all models at least three times, yielding 225 collected human–system dialogs and 45 human ratings per model ([Li et al., 2019](https://gitlab.com/ucdavisnlp/antiscam)). That 225-dialog evaluation set is generated for system testing; it is distinct from the 220-dialog AntiScam corpus and should not be conflated with it ([Li et al., 2019](https://gitlab.com/ucdavisnlp/antiscam)).

The corpus itself is partitioned 80% for training, 10% for validation, and 10% for testing, both for AntiScam and for the fine-tuning stages described in the paper ([Li et al., 2019](https://gitlab.com/ucdavisnlp/antiscam)). On the 220-dialog corpus, those proportions imply roughly 176 training dialogs, 22 validation dialogs, and 22 test dialogs, before accounting for the fact that only 100 dialogs are annotated ([Li et al., 2019](https://gitlab.com/ucdavisnlp/antiscam)).

## Why the Size of AntiScam Matters

The authors' stated motivation for building the corpus was that non-collaborative tasks are relatively new to dialog systems research and that there were insufficient meaningful datasets for evaluation ([Li et al., 2019](https://gitlab.com/ucdavisnlp/antiscam)). The 220-dialog scale reflects a deliberate trade-off: a compact but fully task-specific corpus with a benchmark design that interleaves on-task and off-task content, which the authors position as a benchmark for similar non-collaborative tasks ([Li et al., 2019](https://gitlab.com/ucdavisnlp/antiscam)). The data and code are released publicly, which partially offsets the limited volume by making the corpus reusable and verifiable ([Li et al., 2019](https://gitlab.com/ucdavisnlp/antiscam)).

A corpus of this size also carries known limitations. The authors note that MISSA still produces responses inconsistent with distant conversation history because the underlying model can only track a limited history span, an issue they attribute to the model rather than a lack of data but one that larger corpora might help mitigate ([Li et al., 2019](https://gitlab.com/ucdavisnlp/antiscam)). Future work is planned to address longer-context tracking ([Li et al., 2019](https://gitlab.com/ucdavisnlp/antiscam)).

## Conclusion

**The AntiScam dataset is 220 human–human dialogs** ([Li et al., 2019](https://gitlab.com/ucdavisnlp/antiscam)). Of these, 100 dialogs comprising 3,044 sentences are manually annotated by two expert annotators at a weighted kappa of 0.874, with conversations averaging 12.45 turns and utterances averaging 11.13 words ([Li et al., 2019](https://gitlab.com/ucdavisnlp/antiscam)). The annotation covers 13 semantic slots and a hierarchical intent set of 3 on-task and 12 off-task classes ([Li et al., 2019](https://gitlab.com/ucdavisnlp/antiscam)). A third-party note's alternative figure of 320 dialogs is inconsistent with the primary source on two mutually corroborating statements and alters the reported attacker-detection rate from approximately 78.2% (172/220) to 53.8% (172/320) without methodological justification; on reliability grounds, 220 should be treated as the correct corpus size ([Li et al., 2019](https://gitlab.com/ucdavisnlp/antiscam); [Third-Party Research Note, n.d.](#)). Researchers citing this dataset should therefore report 220 dialogs, 100 annotated dialogs, and 3,044 annotated sentences, and should avoid propagating the 320-dialog figure.

## References

Li, Y., Qian, K., Shi, W., & Yu, Z. (2019). *End-to-End Trainable Non-Collaborative Dialog System*. University of California, Davis. https://gitlab.com/ucdavisnlp/antiscam

Third-Party Research Note. (n.d.). *Third-party research note: End-to-End Trainable Non-Collaborative Dialog System*. [Unpublished secondary note; no author, venue, or independent URL provided.]