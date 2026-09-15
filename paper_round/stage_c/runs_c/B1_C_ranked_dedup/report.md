# The Size of the AntiScam Dataset: Dimensions, Composition, and Scale

## Introduction

The AntiScam dataset is a human-human anti-scam dialog corpus created to support research on non-collaborative dialog systems, in which the conversational agents involved do not share the same goal ([document_2.txt](document_2.txt)). Because the question "how big is the AntiScam dataset?" can be answered along several different axes — number of dialogs, number of conversational turns, number of annotated sentences, and estimated word volume — this report presents the reported figures for each dimension, derives secondary estimates where the source data permit, and offers an explicit assessment of what these numbers mean for the dataset's scientific utility. The short answer is that AntiScam comprises **220 human-human dialogs**, of which **100 dialogs containing 3,044 sentences** were manually annotated by two expert linguistically trained annotators ([document_1.txt](document_1.txt); [document_2.txt](document_2.txt)). Each of these figures, and the relationships among them, is examined in detail below.

## Provenance and Intended Use

Understanding the size figures requires first understanding how the corpus was produced. AntiScam was assembled to "enrich publicly available non-collaborative task datasets," with the explicit expectation that it would "provide a valuable example" for a research area that still lacks sufficiently many meaningful evaluation resources ([document_1.txt](document_1.txt)). The data were collected through a role-playing task posted on the Amazon Mechanical Turk platform, in which participants enacted a popular Amazon customer service scam scenario ([document_1.txt](document_1.txt); [document_2.txt](document_2.txt)). The resulting corpus captures human elicitation strategies — that is, how a user under attack attempts to occupy the attacker's attention and extract information from the attacker ([document_1.txt](document_1.txt)).

A third-party research note confirms these provenance details independently, describing AntiScam as "a corpus of human-human anti-scam dialogs created to learn human elicitation strategies" that "was collected through a role-playing Amazon customer service scam scenario on Amazon Mechanical Turk" ([document_2.txt](document_2.txt)). The convergence of the primary paper text and the secondary research note on the same collection protocol and the same headline count of 220 dialogs strengthens confidence in the reported size.

## Primary Size Indicator: Number of Dialogs

The single most frequently cited measure of the AntiScam corpus is its **220 human-human dialogs** ([document_1.txt](document_1.txt); [document_2.txt](document_2.txt)). Both sources state this figure directly. The paper describes the collection outcome as follows: "We collected 220 human-human dialogs" ([document_1.txt](document_1.txt)), and the research note states that "the dataset contains 220 human-human dialogs" and that "the total dataset comprises 220 human-human dialogs" ([document_2.txt](document_2.txt)).

This number constitutes the population of the corpus. It is the denominator against which all other statistics — including annotation coverage, train/validation/test partitioning, and attacker-identification rates — should be interpreted.

## Conversational Depth: Turns, Sentences, and Utterances

Size in dialogs alone understates the volume of interactional data. The sources therefore also report conversational depth. The **average conversation length is 12.45 turns**, and the **average utterance length is 11.13 words** ([document_1.txt](document_1.txt); [document_2.txt](document_2.txt)). The secondary note is explicit that "these averages describe the full AntiScam corpus" ([document_2.txt](document_2.txt)), meaning they are not restricted to the annotated subset.

Separately, the annotation effort covered **3,044 sentences in 100 dialogs** ([document_1.txt](document_1.txt); [document_2.txt](document_2.txt)). The paper states that the team "recruited two expert annotators who have linguistic training to annotate 3,044 sentences in 100 dialogs, achieving a 0.874 averaged weighted kappa value" ([document_1.txt](document_1.txt)). The research note corroborates this: "a subset of 100 dialogs containing 3,044 sentences was manually annotated," and "two expert annotators who have linguistic training performed this annotation" ([document_2.txt](document_2.txt)).

### Summary of Reported Size Descriptors

| Measure | Reported Value | Scope | Source |
|---|---|---|---|
| Number of dialogs | 220 | Full corpus | ([document_1.txt](document_1.txt); [document_2.txt](document_2.txt)) |
| Average conversation length | 12.45 turns | Full corpus | ([document_1.txt](document_1.txt); [document_2.txt](document_2.txt)) |
| Average utterance length | 11.13 words | Full corpus | ([document_1.txt](document_1.txt); [document_2.txt](document_2.txt)) |
| Dialogs manually annotated | 100 | Annotated subset | ([document_1.txt](document_1.txt); [document_2.txt](document_2.txt)) |
| Sentences manually annotated | 3,044 | Annotated subset | ([document_1.txt](document_1.txt); [document_2.txt](document_2.txt)) |
| Users who identified the attacker | 172 of 220 (78.2%) | Full corpus | ([document_1.txt](document_1.txt); [document_2.txt](document_2.txt)) |
| Inter-annotator agreement (weighted kappa) | 0.874 | Annotated subset | ([document_1.txt](document_1.txt)) |

### Derived Volume Estimates

Although the sources do not report a total word count, the furnished averages permit an approximate estimate. Multiplying 220 dialogs by 12.45 turns yields approximately **2,739 conversational turns** in the full corpus. Multiplying that figure by the average utterance length of 11.13 words yields approximately **30,485 words** of transcribed dialogue. These estimates should be treated as order-of-magnitude approximations, since they assume every turn is a single utterance of average length.

| Derived Quantity | Estimate | Basis |
|---|---|---|
| Total turns in full corpus | ≈ 2,739 | 220 dialogs × 12.45 turns |
| Approximate total words | ≈ 30,485 | 2,739 turns × 11.13 words |
| Sentences per annotated dialog | ≈ 30.44 | 3,044 sentences ÷ 100 dialogs |
| Implied sentences per turn | ≈ 2.44 | 30.44 sentences ÷ 12.45 turns |

### Reconciling the Reported Figures

It is worth flagging an arithmetic tension in the source material that an attentive reader should not overlook. If each turn corresponded to exactly one sentence, 100 annotated dialogs at 12.45 turns each would contain roughly 1,245 sentences — far fewer than the 3,044 actually annotated. The gap implies that the annotation unit ("sentence") is finer-grained than the conversational unit ("turn") used in the length statistic, with roughly 2.4 sentences per turn implied by the reported figures. The sources do not explain this relationship directly, so the derived word-count estimate above (~30,485) should be understood as a turn-based approximation rather than a precise token count of the transcript files. What is unambiguous, however, is that the annotated layer covers **100 dialogs and 3,044 sentences** ([document_2.txt](document_2.txt)) while the collected corpus covers **220 dialogs** ([document_1.txt](document_1.txt)).

## Annotation Coverage and Label Schema

Roughly **45.5% of the corpus (100 of 220 dialogs)** received expert manual annotation ([document_1.txt](document_1.txt); [document_2.txt](document_2.txt)). The annotation followed a **hierarchical intent scheme** applied to both AntiScam and the PersuasionForGood dataset, in which "the On-task intents are task-specific while the Off-task intents are general for different non-collaborative tasks" ([document_1.txt](document_1.txt)). On-task categories include task-specific acts such as elicitation, providing information, and refusal, while off-task categories include general dialog acts such as open questions, yes/no questions, positive and negative answers, responsive and nonresponsive statements, greetings, thanking, apology, closing, and hold ([document_1.txt](document_1.txt)).

The reported averaged weighted kappa of **0.874** ([document_1.txt](document_1.txt)) indicates substantial agreement between the annotators. In practical terms, this level of reliability is achievable within a 3,044-sentence budget and contributes to the corpus's value as a benchmark despite its modest scale.

## Dataset Partitioning and Experimental Scale

The paper reports that the data were divided into **80% training, 10% validation, and 10% testing** subsets ([document_1.txt](document_1.txt)). Applied to the full 220-dialog corpus, that partition implies approximately **176 training dialogs, 22 validation dialogs, and 22 test dialogs**. The sources do not specify whether the split was applied to the full corpus or only to the annotated subset, which matters for interpreting reported model metrics.

| Partition | Share | Implied Dialog Count (of 220) | Source |
|---|---|---|---|
| Training | 80% | ≈ 176 | ([document_1.txt](document_1.txt)) |
| Validation | 10% | ≈ 22 | ([document_1.txt](document_1.txt)) |
| Testing | 10% | ≈ 22 | ([document_1.txt](document_1.txt)) |

Model evaluation on AntiScam compared MISSA and its variants against TransferTransfo and a hybrid baseline across automatic metrics (perplexity, RIP, RSP, ERIP, ERSP) and human metrics (fluency, coherence, engagement, length, task success) ([document_1.txt](document_1.txt)). MISSA achieved the best reported figures among the compared systems on nearly all measures, including a perplexity of 21.07 versus 32.96 for TransferTransfo ([document_1.txt](document_1.txt)).

## Human Evaluation Scale

Beyond offline metrics, the authors conducted a human evaluation on AntiScam using **15 college-student volunteers**, each of whom was asked to pretend to be an attacker and interact with all models at least three times "to avoid randomness" ([document_1.txt](document_1.txt)). In total, **225 dialogs** were collected, and each model received **45 human ratings**, which were averaged into the final human-evaluation score ([document_1.txt](document_1.txt)). With five models evaluated — TransferTransfo, Hybrid, MISSA, MISSA-sel, and MISSA-con — the arithmetic is internally consistent: 15 evaluators × 3 rounds = 45 ratings per model, and 45 × 5 = 225 dialogs ([document_1.txt](document_1.txt)).

| Human Evaluation Parameter | Value | Source |
|---|---|---|
| Volunteers | 15 | ([document_1.txt](document_1.txt)) |
| Minimum interactions per volunteer per model | 3 | ([document_1.txt](document_1.txt)) |
| Total dialogs collected | 225 | ([document_1.txt](document_1.txt)) |
| Systems compared | 5 | ([document_1.txt](document_1.txt)) |
| Ratings per system | 45 | ([document_1.txt](document_1.txt)) |

## Interpreting the Size: An Assessment

Based on the furnished evidence, my own assessment is that AntiScam should be characterized as a **small, purpose-built, high-reliability corpus** rather than a large-scale resource. Three observations support this position.

First, 220 dialogs is modest in absolute terms. The total interaction volume implied by the reported averages is on the order of 2,700 turns or roughly 30,000 words ([document_1.txt](document_1.txt)), which is a narrow basis for training or fine-tuning dialog systems from scratch. The 22-dialog test split implied by the 80/10/10 partition ([document_1.txt](document_1.txt)) is small enough that evaluation differences between models could be sensitive to individual conversations, and the 10-point validation subset leaves limited room for hyperparameter tuning without overfitting.

Second, the corpus's reliability is disproportionately strong relative to its size. A weighted kappa of 0.874 across 3,044 expert-annotated sentences ([document_1.txt](document_1.txt)) is a genuine strength, and it is plausibly enabled precisely by the compact scale: exhaustive expert annotation of a few thousand sentences is feasible in a way that equivalent annotation of a corpus an order of magnitude larger would not be. Small size and high label quality are therefore linked here, not independent properties.

Third, the corpus has limited domain breadth. It derives from a single role-playing scenario — an Amazon customer service scam — executed on a single crowdsourcing platform ([document_1.txt](document_1.txt); [document_2.txt](document_2.txt)). The reported finding that only **172 of 220 users (approximately 78.2%)** successfully identified their partner as an attacker indicates the scenarios were challenging and the attackers were "well trained and not too easily identifiable" ([document_1.txt](document_1.txt)), which speaks well to task difficulty but says nothing about cross-domain coverage.

Importantly, the authors themselves appear to recognize that dataset character affects model design. When MISSA was applied to PersuasionForGood, MISSA-con performed best on RIP and ERIP, and the authors attribute this to there being "more possible responses with the same intent in PersuasionForGood than in AntiScam," concluding that "we should adjust the model structure according to the nature of the dataset" ([document_1.txt](document_1.txt)). This is a direct acknowledgment that the size and diversity of response space within a corpus shape which architectures succeed — reinforcing the view that AntiScam's 220 dialogs define a focused, task-specific evaluation regime rather than a general-purpose one.

The corpus nonetheless fulfills its stated purpose. It was created because "non-collaborative tasks are still relatively new" and "there are insufficiently many meaningful datasets for evaluation," and the authors "hope this provides a valuable example" ([document_1.txt](document_1.txt)). Evaluations on both AntiScam and PersuasionForGood showed MISSA outperforming competitive baselines ([document_1.txt](document_1.txt); [document_2.txt](document_2.txt)), demonstrating that 220 dialogs can support meaningful comparative research when paired with a second dataset and a thorough human-evaluation protocol of 225 collected dialogs ([document_1.txt](document_1.txt)).

## Conclusion

The AntiScam dataset is **220 human-human anti-scam dialogs** collected via a role-playing Amazon customer service scam scenario on Amazon Mechanical Turk ([document_1.txt](document_1.txt); [document_2.txt](document_2.txt)). Its average conversation length is **12.45 turns**, its average utterance length is **11.13 words** ([document_1.txt](document_1.txt); [document_2.txt](document_2.txt)), and a subset of **100 dialogs comprising 3,044 sentences** was annotated by two expert linguistically trained annotators at a weighted kappa of **0.874** ([document_1.txt](document_1.txt); [document_2.txt](document_2.txt)). From these figures one can derive approximately **2,739 turns** and roughly **30,485 words** of dialogue across the full corpus, with approximately **2.44 sentences per turn** implied by the annotation density — estimates that should be treated as approximate given the unit mismatch between the reported turn count and annotated sentence count. Functionally, AntiScam is a compact but carefully labeled benchmark whose scale constrains statistical precision yet enables the annotation quality and controlled human evaluation that make it a usable example for a still-emerging research area.

## References

document_1.txt. (n.d.). *MISSA: End-to-End Trainable Non-Collaborative Dialog System — manuscript excerpts, tables, and dataset description* [Unpublished manuscript]. 

document_2.txt. (n.d.). *Third-party research note: End-to-End Trainable Non-Collaborative Dialog System* [Research note].