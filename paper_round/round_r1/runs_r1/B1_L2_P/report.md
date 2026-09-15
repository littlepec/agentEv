# How Big Is the AntiScam Dataset? A Detailed Assessment of Corpus Scale, Annotation Depth, and Conversational Dimensions

## Introduction

The AntiScam dataset is a corpus of human–human anti-scam dialogs introduced to support research on non-collaborative dialog systems — conversational settings in which the user and the system do not share a common goal (Li et al., 2019). The dataset was created to learn human elicitation strategies by placing participants in a role-playing Amazon customer service scam scenario, where one participant acts as an attacker attempting to extract personal information and the other acts as an everyday user defending that information (Li et al., 2019). Because the size of a dialog corpus determines what modeling approaches are statistically feasible, how reliable evaluation results are, and how far findings can generalize, a precise accounting of AntiScam's scale — in dialogs, turns, utterances, sentences, and annotations — is essential. This report synthesizes every size-related figure reported in the primary source, the paper itself, and evaluates a conflicting figure reported in a secondary research note.

## Source Provenance and Reliability Assessment

Two sources are available. The first is the primary paper, "End-to-End Trainable Non-Collaborative Dialog System" by Yu Li, Kun Qian, Weiyan Shi, and Zhou Yu of the University of California, Davis, distributed as arXiv preprint 1911.10742 (Li et al., 2019). The second is a third-party research note summarizing the same paper's AntiScam dataset description (Third-party research note, n.d.). Because the primary source contains the authors' own methodological description, its figures must be prioritized over those of a derivative summary. This principle becomes decisive in the present case, since the two sources disagree on the headline dataset size, as discussed below.

## Headline Size: Number of Human–Human Dialogs

According to the primary source, AntiScam comprises **220 human–human dialogs** collected on the Amazon Mechanical Turk platform through a typing-conversation role-play task (Li et al., 2019). This is the single most important size figure for the dataset. The collection setting randomly paired two workers: one was assigned the role of an attacker who "receives training on how to elicit information from people," and the other was assigned the role of an everyday user who "aims to protect her/his information and potentially elicit the attacker's information" (Li et al., 2019). Workers could not see their partners' instructions, and each worker could participate only once, which prevented participants from knowing their partner's information and goals in advance (Li et al., 2019).

The secondary research note instead asserts that "the dataset contains 320 human-human dialogs" and repeats this total three times, including in its summary (Third-party research note, n.d.). This figure conflicts directly with the paper's repeated statement of 220 dialogs and, critically, with the paper's own derived statistic that "only 172 out of 220 users successfully identified their partner as an attacker" (Li et al., 2019). The denominator of 220 appears twice in the primary text — once in the dataset description and once in the training-details appendix — whereas no occurrence of "320" as a dialog count appears in the paper's own prose (Li et al., 2019). The best-supported reading is therefore that the AntiScam corpus contains **220 dialogs**, and that the 320 figure in the secondary note is an error, most plausibly a transposition of the digits in 220 and/or a conflation with the 3,044 annotated sentences discussed later. This report adopts 220 as the authoritative corpus size while flagging the discrepancy transparently.

| Size Metric | Primary Source Figure | Secondary Note Figure | Assessment |
|---|---|---|---|
| Total human–human dialogs | 220 | 320 | Primary source preferred; 220 stated twice |
| Users identifying attacker | 172 of 220 | 172 of 320 | Primary source internally consistent |
| Annotated dialogs (subset) | 100 | 100 | Both sources agree |
| Annotated sentences | 3,044 | 3,044 | Both sources agree |
| Avg. conversation length | 12.45 turns | 12.45 turns | Both sources agree |
| Avg. utterance length | 11.13 words | 11.13 words | Both sources agree |

## Conversational Depth: Turns, Utterances, and Sentences

Beyond the dialog count, the paper reports the internal dimensions of the corpus. The **average conversation length is 12.45 turns**, and the **average utterance length is 11.13 words** (Li et al., 2019). These two averages describe the full AntiScam corpus rather than only the annotated subset (Third-party research note, n.d.).

These averages allow an approximate reconstruction of the corpus's total conversational volume. Multiplying 220 dialogs by 12.45 turns yields roughly **2,739 conversational turns**; multiplying that by 11.13 words per utterance yields on the order of **30,000 words** of dialog text. These derived values should be treated as order-of-magnitude estimates rather than reported statistics, because they assume that every turn consists of exactly one utterance of average length and that the averages hold uniformly across all 220 dialogs. They are nonetheless useful for gauging the corpus's scale: AntiScam is a compact, human-authored dataset rather than a large-scale scraped corpus.

One structural feature noted in the paper is that utterances frequently contain multiple sentences. The authors state that they "segment each conversation turn into single sentences and then annotate each sentence rather than turns" (Li et al., 2019). Consequently, the number of annotation units is substantially larger than the number of turns: 3,044 sentences across 100 annotated dialogs implies roughly **30 sentences per dialog** and, given 12.45 turns per dialog, roughly **2.4 sentences per turn** in the annotated portion. Again, these are derived figures, not reported ones, but they clarify why sentence-level annotation was chosen as the granularity for the corpus.

## Annotation Scale and Density

A distinctive dimension of AntiScam's size is the density of its human annotation. The paper reports that "two expert annotators who have linguistic training" annotated **3,044 sentences in 100 dialogs**, achieving a **0.874 averaged weighted kappa value** (Li et al., 2019). The annotated subset therefore covers 100 of the 220 dialogs — approximately 45 percent of the corpus — and the reported kappa indicates substantial inter-annotator agreement.

The annotation infrastructure attached to the corpus is multi-layered. The paper introduces a **hierarchical intent annotation scheme** that separates on-task from off-task content (Li et al., 2019). For AntiScam specifically, three on-task intents are defined: *elicitation*, *providing_information*, and *refusal* (Li et al., 2019). The off-task layer is shared across non-collaborative tasks and consists of **six general intents** (*open_question*, *yes_no_question*, *positive_answer*, *negative_answer*, *responsive_statement*, *nonresponsive_statement*) plus **six social intents** (*greeting*, *closing*, *apology*, *thanking*, *respond_to_thank*, *hold*) — twelve off-task categories in total (Li et al., 2019). Separately, the authors "identify 13 main semantic slots in the anti-scam task" corresponding to domain entities such as order details, payment, name, identity, address, phone number, card information, card number, card CVS, and card date (Li et al., 2019).

| Annotation Layer | Inventory Size | Notes |
|---|---|---|
| On-task intents (AntiScam) | 3 | elicitation, providing_information, refusal |
| Off-task general intents | 6 | Shared across tasks |
| Off-task social intents | 6 | Shared across tasks |
| Semantic slots | 13 | Task-specific to the anti-scam scenario |
| Annotated dialogs | 100 | Subset of the 220-dialog corpus |
| Annotated sentences | 3,044 | Sentence-level, not turn-level |
| Annotation quality | 0.874 | Averaged weighted kappa |

## Structural and Distributional Size Characteristics

The corpus also has measurable internal asymmetries that bear on its effective research value. The paper reports that "sentences from the attacker and user have different intent distributions": compared with attackers, users produced more *refusal* utterances (74 versus 19), and users asked more *open_questions* (173 versus 54) and *yes_no_questions* (165 versus 117) for off-task content (Li et al., 2019). The paper further observes that attackers and users collectively contribute a substantial volume of social content — 292 and 252 instances respectively — which the authors cite as evidence "that it is important to have social intent sentences to maintain the conversation" (Li et al., 2019). These counts suggest that off-task, socially oriented material is not a marginal component of the corpus but a large share of its utterances, a fact that motivated the hierarchical annotation design.

Data splits further define how the corpus is consumed. In experiments on AntiScam and PersuasionForGood, the authors used **80 percent of data for training, 10 percent for validation, and 10 percent for testing** (Li et al., 2019). Applied to 220 dialogs, this corresponds to approximately 176 training dialogs, 22 validation dialogs, and 22 test dialogs. The paper additionally states that the code and data are released publicly at a GitLab repository associated with the authors' group, making the resource externally available (Li et al., 2019).

## Comparative Scale: AntiScam Versus PersuasionForGood

Placing AntiScam in context requires comparison with the second non-collaborative dataset used in the paper, PersuasionForGood. That corpus "consists of 1,017 dialogs, where 300 dialogs are annotated with dialog acts," with an average conversation length of 10.43 turns and a vocabulary size of 8,141 (Li et al., 2019). AntiScam is thus roughly one-fifth the dialog count of PersuasionForGood but presents a longer average conversation (12.45 versus 10.43 turns) and a deeper, purpose-built annotation layer covering intents and semantic slots in addition to dialog acts (Li et al., 2019).

| Dimension | AntiScam | PersuasionForGood |
|---|---|---|
| Total dialogs | 220 | 1,017 |
| Annotated dialogs | 100 | 300 |
| Annotated sentences | 3,044 | Not reported |
| Avg. conversation length | 12.45 turns | 10.43 turns |
| Avg. utterance length | 11.13 words | Not reported |
| Vocabulary size | Not reported | 8,141 |
| On-task intents | 3 | 9 |
| Semantic slots | 13 | Not reported |

## Derived Estimates of Corpus Volume

Combining reported averages permits a cautious estimate of the total corpus scale. At 220 dialogs and 12.45 turns each, AntiScam contains roughly 2,739 turns; at 11.13 words per utterance, this is on the order of 30,000 words of dialog text. If the annotated subset's density of about 30 sentences per dialog held across the whole corpus, the full dataset would contain approximately 6,700 sentences, of which 3,044 — about 45 percent — carry human labels (Li et al., 2019). These extrapolations are offered as bounding estimates only; the paper does not report corpus-wide sentence or token counts.

## Implications of Dataset Size for Research Use

The scale of AntiScam has several practical consequences. First, at 220 dialogs with 100 fully annotated, the dataset is large enough to support the paper's multi-task training regime — joint language modeling, next-utterance classification, and intent and semantic-slot classification — but small enough that the released code and data remain tractable for individual research groups (Li et al., 2019). Second, the reported intent predictor accuracy of 84 percent and semantic slot predictor accuracy of 77 percent were obtained on this corpus, figures whose reliability is bounded by the size of the annotated subset (Li et al., 2019). Third, the human evaluation component extended the corpus's footprint beyond the original dialogs: 15 college-student volunteers each interacted with all five models at least three times, yielding **225 additional human–system dialogs** and 45 ratings per model (Li et al., 2019). Fourth, the authors explicitly frame AntiScam as filling a gap — "as non-collaborative tasks are still relatively new to the study of dialog systems, there are insufficiently many meaningful datasets for evaluation" — positioning a 220-dialog corpus as a benchmark contribution rather than a large-scale resource (Li et al., 2019).

## Conclusion

The AntiScam dataset is a compact, richly annotated corpus whose size is best characterized along several axes rather than a single number. Its headline size is **220 human–human dialogs**, average **12.45 turns** and **11.13 words per utterance**, with a **100-dialog, 3,044-sentence subset** annotated by two linguistic experts at **0.874 averaged weighted kappa** (Li et al., 2019). It carries a hierarchical intent scheme of three task-specific on-task intents plus twelve universal off-task intents, alongside thirteen semantic slots (Li et al., 2019). A third-party research note reports the corpus as 320 dialogs, but this conflicts with the primary source's internally consistent statement that 172 out of **220** users identified their partner as an attacker, and the primary source should be preferred (Li et al., 2019; Third-party research note, n.d.). For researchers seeking a non-collaborative dialog benchmark, AntiScam's value lies not in raw volume but in the depth of its annotation relative to its size — roughly 45 percent of dialogs carry sentence-level intent and slot labels, and the dataset was purpose-built to interleave on-task and off-task content in a way that earlier corpora were not (Li et al., 2019).

## References

Li, Y., Qian, K., Shi, W., & Yu, Z. (2019). *End-to-end trainable non-collaborative dialog system* [Source: document_1.txt]. arXiv. https://arxiv.org/abs/1911.10742

Third-party research note: End-to-end trainable non-collaborative dialog system [Source: document_2.txt]. (n.d.). https://arxiv.org/abs/1911.10742