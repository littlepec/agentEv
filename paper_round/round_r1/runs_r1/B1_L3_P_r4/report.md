# How Big Is the AntiScam Dataset? Scale, Annotation Depth, and Composition of a Human–Human Anti-Scam Dialog Corpus

## Purpose and Scope of This Report

The question "How big is the AntiScam dataset?" is deceptively simple, because the size of a conversational corpus can be measured along several independent axes: the raw number of conversations, the number of conversations that carry manual annotation, the number of annotated sentences, the per-conversation dimensions of turns and utterances, and the breadth of the annotation label space applied to the data. This report answers the question along all of these axes using two source documents: the primary research paper *End-to-End Trainable Non-Collaborative Dialog System* by Li, Qian, Shi, and Yu of the University of California, Davis ([Li et al., 2020](https://arxiv.org/abs/1911.10742)), and a third-party research note that summarizes the dataset description contained in that paper ([Third-party research note](https://gitlab.com/ucdavisnlp/antiscam)). The report also explicitly identifies a numerical discrepancy between the two sources regarding the headline dialog count, and states a reasoned position on which figure should be treated as authoritative.

## The Headline Number: Total Number of Dialogs

AntiScam is described as a corpus of human–human anti-scam dialogs created to learn human elicitation strategies, collected through a role-playing Amazon customer service scam scenario on Amazon Mechanical Turk, in which the corpus is designed to interleave on-task and off-task content so that it can serve as a benchmark for non-collaborative dialog research ([Li et al., 2020](https://arxiv.org/abs/1911.10742)).

The two sources disagree on the exact total, and that disagreement must be surfaced rather than smoothed over.

| Source | Dialogs reported | Users who identified the attacker | Implied detection rate |
|---|---|---|---|
| Primary paper description ([Li et al., 2020](https://arxiv.org/abs/1911.10742)) | 220 | 172 out of 220 | 78.2% (derived) |
| Third-party research note ([Third-party research note](https://gitlab.com/ucdavisnlp/antiscam)) | 320 | 172 out of 320 | 53.8% (derived) |

The primary paper states plainly: "We collected 2 2 0 human-human dialogs," and later, "Only 1 7 2 out of 2 2 0 users successfully identified their partner as an attacker, suggesting that the attackers are well trained and not too easily identifiable" ([Li et al., 2020](https://arxiv.org/abs/1911.10742)). The third-party note instead asserts that "the dataset contains 320 human-human dialogs" and that "172 out of 320 users successfully identified their partner as an attacker" ([Third-party research note](https://gitlab.com/ucdavisnlp/antiscam)).

**My assessment:** the figure of **220 human–human dialogs** should be treated as the authoritative size of the AntiScam corpus. Three considerations support this. First, the number 220 appears twice, independently, in the primary source — once in the dataset description and once in the analytical discussion of attacker identifiability — whereas 320 appears only in the secondary note ([Li et al., 2020](https://arxiv.org/abs/1911.10742); [Third-party research note](https://gitlab.com/ucdavisnlp/antiscam)). Second, the primary source is the originating document, and the secondary note is by definition a derivative summary; when a derivative summary conflicts with its origin, the origin takes precedence. Third, the machine-extracted text of the primary source renders numbers in a spaced-digit format in which "2 2 0" and "3 2 0" differ by a single character, making a transcription error in the derivative note a straightforward and plausible explanation. Researchers requiring a definitive count should verify against the released corpus at the project repository, which the paper cites as the location of the released code and data ([Li et al., 2020](https://arxiv.org/abs/1911.10742)). Both candidate totals should be reported in any downstream citation, however, because the discrepancy is unresolved by the evidence available in these two documents.

## The Annotated Subset: 100 Dialogs and 3,044 Sentences

Raw dialog count alone understates the effective size of AntiScam, because the corpus is only partly annotated. The paper reports that two expert annotators with linguistic training annotated **3,044 sentences across 100 dialogs**, achieving a 0.874 averaged weighted kappa value ([Li et al., 2020](https://arxiv.org/abs/1911.10742)). The same annotation statistics — 100 dialogs and 3,044 sentences, annotated by two expert annotators with linguistic training — are independently restated in the third-party note ([Third-party research note](https://gitlab.com/ucdavisnlp/antiscam)).

This yields several derived quantities that are useful for judging data volume:

- **Annotated coverage:** 100 of 220 dialogs, or approximately 45% of the corpus, carry manual intent and slot annotation (derived from [Li et al., 2020](https://arxiv.org/abs/1911.10742)).
- **Sentence density:** 3,044 sentences ÷ 100 annotated dialogs ≈ **30.44 annotated sentences per dialog** (derived).
- **Sentences per turn:** with an average conversation length of 12.45 turns, 30.44 ÷ 12.45 ≈ **2.44 sentences per turn**, which is consistent with the paper's statement that each conversation turn was segmented into single sentences and annotated at the sentence level rather than the turn level ([Li et al., 2020](https://arxiv.org/abs/1911.10742)).
- **Projected full-corpus sentence count:** if sentence density holds across the unannotated portion, 220 dialogs × 30.44 sentences ≈ **6,700 sentences** in the corpus as a whole (derived projection, not a reported figure).

The choice to annotate at sentence granularity rather than turn granularity is analytically important: it means the 3,044 figure represents a finer unit of analysis than the dialog count, and the annotation ceiling for training the intent and slot classifiers is bounded by this annotated subset, not by the full 220-dialog corpus ([Li et al., 2020](https://arxiv.org/abs/1911.10742)).

## Per-Conversation Dimensions: Turns and Utterance Length

Beyond raw counts, the size of the corpus is characterized by the length of its constituent conversations. The paper reports an average conversation length of **12.45 turns** and an average utterance length of **11.13 words**, and the secondary note confirms that these averages describe the full AntiScam corpus rather than only the annotated subset ([Li et al., 2020](https://arxiv.org/abs/1911.10742); [Third-party research note](https://gitlab.com/ucdavisnlp/antiscam)).

| Dimension | Reported value | Derived corpus-level estimate (220 dialogs) | Derived corpus-level estimate (320 dialogs) |
|---|---|---|---|
| Dialogs | 220 ([Li et al., 2020](https://arxiv.org/abs/1911.10742)) / 320 ([Third-party research note](https://gitlab.com/ucdavisnlp/antiscam)) | 220 | 320 |
| Average turns per dialog | 12.45 ([Li et al., 2020](https://arxiv.org/abs/1911.10742)) | ≈ 2,739 turns | ≈ 3,984 turns |
| Average utterance length | 11.13 words ([Li et al., 2020](https://arxiv.org/abs/1911.10742)) | — | — |
| Approximate total words | — | ≈ 30,500 words | ≈ 44,300 words |
| Manually annotated dialogs | 100 ([Li et al., 2020](https://arxiv.org/abs/1911.10742)) | 100 | 100 |
| Manually annotated sentences | 3,044 ([Li et al., 2020](https://arxiv.org/abs/1911.10742)) | 3,044 | 3,044 |

All corpus-level estimates in the right-hand columns are products of reported values and are labeled here as derived rather than reported. On this reckoning AntiScam is a **small-to-moderate corpus by dialog count but a comparatively dense one by annotation**, since roughly 3,044 of an estimated 6,700 sentences carry manual labels. For context, the paper does not report a vocabulary size for AntiScam, although it reports a vocabulary of **8,141** for the PersuasionForGood corpus used as a second evaluation set ([Li et al., 2020](https://arxiv.org/abs/1911.10742)).

## Participant and Collection Footprint

The corpus was collected through role-playing tasks on Amazon Mechanical Turk in the form of typing conversations, in which two workers were randomly paired: one assigned the role of an attacker eliciting user information, and the other assigned the role of an everyday user aiming to protect their information and potentially elicit the attacker's information ([Li et al., 2020](https://arxiv.org/abs/1911.10742)). Because "each worker can only participate once to prevent workers from knowing their partner's information and goals in advance," the corpus is built from one-shot dyads rather than repeated participants ([Li et al., 2020](https://arxiv.org/abs/1911.10742)). If every one of the 220 dialogs drew a fresh pair, the collection would represent approximately **440 unique worker-sessions** (derived inference). Workers could not see their partners' instructions, and financial bonuses were provided to attackers who successfully elicited correct information and to users who detected attackers and elicited real information, including the attacker's name, address, and phone number ([Li et al., 2020](https://arxiv.org/abs/1911.10742)).

A signal relevant to the dataset's difficulty and quality is that only **172 of 220 users** successfully identified their partner as an attacker within the 220-dialog reading of the corpus, which the authors interpret as evidence that the attackers were well trained and not too easily identifiable ([Li et al., 2020](https://arxiv.org/abs/1911.10742)). Under the alternative 320-dialog reading, the same 172 detections would represent a substantially lower success rate of roughly 54% ([Third-party research note](https://gitlab.com/ucdavisnlp/antiscam)).

## Annotation Label Space as a Dimension of Size

A further sense in which AntiScam is "big" concerns the richness of its label inventory rather than its raw volume. The corpus uses a hierarchical intent annotation scheme that separates on-task from off-task intents, in which on-task intents are task-specific key actions while off-task intents are general across non-collaborative tasks ([Li et al., 2020](https://arxiv.org/abs/1911.10742)). For AntiScam the three on-task intents are **elicitation**, **providing_information**, and **refusal** ([Li et al., 2020](https://arxiv.org/abs/1911.10742)). The off-task label inventory is shared with PersuasionForGood and comprises six general intents — **open_question**, **yes_no_question**, **positive_answer**, **negative_answer**, **responsive_statement**, and **nonresponsive_statement** — plus six social intents — **greeting**, **closing**, **apology**, **thanking**, **respond_to_thank**, and **hold** ([Li et al., 2020](https://arxiv.org/abs/1911.10742)).

In addition, the paper identifies **13 main semantic slots** for the anti-scam task, including credit card numbers, names, addresses, phone numbers, and related account and payment fields, illustrated by slot definitions such as *order_detail*, *order_update*, *payment*, *name*, *identity*, *address*, *phone_num*, *card_info*, *card_num*, *card_cvs*, *card_date*, *account_detail*, and *others* ([Li et al., 2020](https://arxiv.org/abs/1911.10742)).

| Label category | Count | Examples |
|---|---|---|
| AntiScam on-task intents | 3 | elicitation, providing_information, refusal ([Li et al., 2020](https://arxiv.org/abs/1911.10742)) |
| Off-task general intents | 6 | open_question, yes_no_question, positive_answer, negative_answer, responsive_statement, nonresponsive_statement ([Li et al., 2020](https://arxiv.org/abs/1911.10742)) |
| Off-task social intents | 6 | greeting, closing, apology, thanking, respond_to_thank, hold ([Li et al., 2020](https://arxiv.org/abs/1911.10742)) |
| AntiScam semantic slots | 13 | name, address, phone_num, card_num, card_cvs, card_date, account_detail, others ([Li et al., 2020](https://arxiv.org/abs/1911.10742)) |

## Distribution of Annotated Content

The paper also reports distributional counts that indicate how the annotation volume is spread across speaker roles. Sentences from attackers and users follow different intent distributions: compared with attackers, users produced more refusals (**74 versus 19**), more open questions (**173 versus 54**), and more yes/no questions (**165 versus 117**) ([Li et al., 2020](https://arxiv.org/abs/1911.10742)). The paper further notes that attackers and users both generated a large volume of social content, reported as **292 in total** and **252 in total** respectively, which the authors cite as evidence that social-intent annotation is necessary to maintain conversation ([Li et al., 2020](https://arxiv.org/abs/1911.10742)). These counts describe the annotated portion of the corpus and confirm that off-task content constitutes a numerically substantial share of the dataset rather than a marginal residue, which the paper links to the necessity of a hierarchical on-task/off-task annotation scheme ([Li et al., 2020](https://arxiv.org/abs/1911.10742)).

## Comparative Scale and Model-Training Implications

Positioning AntiScam against the companion dataset used in the same study clarifies its relative size. PersuasionForGood consists of **1,017 dialogs**, of which **300 are annotated with dialog acts**, with an average conversation length of **10.43** turns ([Li et al., 2020](https://arxiv.org/abs/1911.10742)). AntiScam is therefore smaller than PersuasionForGood in raw dialog count under either the 220 or 320 reading, but it is purpose-built for non-collaborative anti-scam research: the authors state that they created it specifically because insufficient meaningful datasets existed for evaluation of non-collaborative systems, and that it interleaves on-task and off-task content to serve as a benchmark ([Li et al., 2020](https://arxiv.org/abs/1911.10742)).

The corpus size also constrains how the data is used. Models were trained with an **80% / 10% / 10%** training, validation, and testing split ([Li et al., 2020](https://arxiv.org/abs/1911.10742)), which implies roughly **176 training dialogs, 22 validation dialogs, and 22 test dialogs** under the 220-dialog reading (derived). The MISSA model was pretrained on the PERSONA-CHAT dataset before fine-tuning on AntiScam and PersuasionForGood, using an Adam optimizer with a learning rate of 6.25e-5 and L2 weight decay of 0.01 ([Li et al., 2020](https://arxiv.org/abs/1911.10742)) — a design choice consistent with the modest size of the target corpora. The intent predictor reached **84%** accuracy and the semantic slot predictor **77%** on AntiScam ([Li et al., 2020](https://arxiv.org/abs/1911.10742)).

Finally, the scale of evaluation activity surrounding the corpus is distinct from, and should not be confused with, the corpus size itself. Human evaluation involved **15 college-student volunteers**, each interacting with all models at least three times, producing a total of **225 dialogs** and **45 human ratings per model** ([Li et al., 2020](https://arxiv.org/abs/1911.10742)). This is internally consistent: 15 volunteers × 3 interactions × 5 models = 225 evaluation dialogs (derived). MISSA maintained longer conversations (14.9 turns) than TransferTransfo (8.5 turns) and achieved a higher task success score (1.294 versus 1.025) ([Li et al., 2020](https://arxiv.org/abs/1911.10742)).

## Bottom Line

On the most reliable reading of the available evidence, the AntiScam dataset is a **human–human anti-scam dialog corpus of approximately 220 dialogs** collected via a role-playing Amazon customer service scam scenario on Amazon Mechanical Turk, with a **manually annotated subset of 100 dialogs comprising 3,044 sentences**, authored by two linguistically trained expert annotators at a 0.874 averaged weighted kappa ([Li et al., 2020](https://arxiv.org/abs/1911.10742)). Each conversation averages **12.45 turns** with utterances averaging **11.13 words** ([Li et al., 2020](https://arxiv.org/abs/1911.10742)). Under the alternative reading offered by the secondary source, the corpus would contain **320 dialogs** with the same 100-dialog, 3,044-sentence annotated subset ([Third-party research note](https://gitlab.com/ucdavisnlp/antiscam)). Either way, AntiScam should be characterized as a compact but annotation-dense corpus governed by a label inventory of **3 task-specific on-task intents, 12 off-task intents, and 13 semantic slots**, with a released code and data artifact available for verification ([Li et al., 2020](https://arxiv.org/abs/1911.10742)).

## References

Li, Y., Qian, K., Shi, W., & Yu, Z. (2020). *End-to-end trainable non-collaborative dialog system* [Document 1: document_1.txt]. University of California, Davis. https://arxiv.org/abs/1911.10742

Third-party research note: *End-to-end trainable non-collaborative dialog system* [Document 2: document_2.txt]. (n.d.). [Note: this secondary source is a summary note without an independent publisher URL; the project artifact cited within the source documents is used here.] https://gitlab.com/ucdavisnlp/antiscam