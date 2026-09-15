# Size and Scope of the AntiScam Dataset: A Detailed Assessment

## Answer at a Glance

The AntiScam dataset, as reported in the End-to-End Trainable Non-Collaborative Dialog System paper, consists of **220 human–human dialogs** collected through a role-playing Amazon customer-service scam scenario on Amazon Mechanical Turk ([Li et al., n.d.](https://gitlab.com/ucdavisnlp/antiscam)). A **manually annotated subset of 100 dialogs containing 3,044 sentences** was labelled by two expert annotators with linguistic training, achieving a 0.874 averaged weighted kappa value ([Li et al., n.d.](https://gitlab.com/ucdavisnlp/antiscam)). The corpus has an average conversation length of **12.45 turns** and an average utterance length of **11.13 words** ([Third-party research note](https://gitlab.com/ucdavisnlp/antiscam)). In short, AntiScam is a **small, densely annotated benchmark corpus** rather than a large-scale training resource — a characterisation that is consistent with every figure the source documents provide.

## Primary Sources and Their Reliability

Two documents inform this report. The first (document_1.txt) is the full text of the paper itself, including its methods, tables, appendices, collection instructions, and reference list; it is the primary and most reliable source for dataset facts ([Li et al., n.d.](https://gitlab.com/ucdavisnlp/antiscam)). The second (document_2.txt) is a third-party research note that summarises the paper's dataset description and explicitly frames its key questions around "AntiScam dataset non-collaborative dialog size" ([Third-party research note](https://gitlab.com/ucdavisnlp/antiscam)). The note is useful as corroboration, but it is derivative: where it and the primary text diverge, the primary text should be preferred. The paper also states that code and data are released at a public repository ([Li et al., n.d.](https://gitlab.com/ucdavisnlp/antiscam)), which strengthens the verifiability of the reported size, although the repository itself was not inspected for this report.

## Headline Size Metrics

### Total dialog count

The paper states plainly: "We collected 2 2 0 human-human dialogs" ([Li et al., n.d.](https://gitlab.com/ucdavisnlp/antiscam)). The third-party note concurs, reporting that "the dataset contains 220 human-machine dialogs" ([Third-party research note](https://gitlab.com/ucdavisnlp/antiscam)). This is the single most direct answer to the query: **220 dialogs**.

### Annotation subset

Not all 220 dialogs are annotated. The paper reports that two expert annotators with linguistic training "annotate[d] 3,0 4 4 sentences in 1 0 0 dialogs, achieving a 0.8 7 4 averaged weighted kappa value" ([Li et al., n.d.](https://gitlab.com/ucdavisnlp/antiscam)). The third-party note independently reports the same subset: "a subset of 100 dialogs containing 3,044 sentences was manually annotated" ([Third-party research note](https://gitlab.com/ucdavisnlp/antiscam)). Thus the **annotated core is roughly 45% of the dialogs by count**.

### Average lengths

Two averages are reported and they apply to the full 220-dialog collection rather than the annotated subset: the average conversation length is **12.45 turns** and the average utterance length is **11.13 words** ([Third-party research note](https://gitlab.com/ucdavisnlp/antiscam); [Li et al., n.d.](https://gitlab.com/ucdavisnlp/antiscam)). The third-party note explicitly clarifies that "these averages describe the full AntiScam corpus" ([Third-party research note](https://gitlab.com/ucdavisnlp/antiscam)).

### Detection outcome within the corpus

Of the 220 role-playing users, "Only 1 7 2 out of 2 2 0 users successfully identified their partner as an attacker, suggesting that the attackers are well trained and not too easily identifiable" ([Li et al., n.d.](https://gitlab.com/ucdavisnlp/antiscam)). This corresponds to a detection rate of approximately 78.2%, a figure that characterises the content of the corpus rather than its volume, but which is frequently reported alongside its size.

| Reported size metric | Value |
|---|---|
| Total dialogs | 220 |
| Manually annotated dialogs | 100 |
| Manually annotated sentences | 3,044 |
| Average conversation length | 12.45 turns |
| Average utterance length | 11.13 words |
| Expert annotators | 2 |
| Inter-annotator agreement | 0.874 weighted kappa |
| Users who identified the attacker | 172 of 220 |

All values are drawn from Li et al. (n.d.) and the third-party research note ([Li et al., n.d.](https://gitlab.com/ucdavisnlp/antiscam); [Third-party research note](https://gitlab.com/ucdavisnlp/antiscam)).

## Derived Scale Estimates

The source documents do not report a total word count, sentence count for the full corpus, or file size. However, the reported averages permit transparent arithmetic estimates. These are **derived figures**, not reported ones, and should be treated as approximate.

| Derived quantity | Calculation | Estimate |
|---|---|---|
| Total turns in the 220-dialog corpus | 220 × 12.45 | ≈ 2,739 turns |
| Total words in the 220-dialog corpus | 2,739 × 11.13 | ≈ 30,485 words |
| Words per dialog | 12.45 × 11.13 | ≈ 139 words |
| Sentences per annotated dialog | 3,044 ÷ 100 | ≈ 30.4 sentences |
| Sentences per turn | 30.4 ÷ 12.45 | ≈ 2.44 sentences |
| Sentences if extrapolated to all 220 dialogs | 220 × 30.4 | ≈ 6,700 sentences |

The extrapolation to roughly 6,700 sentences assumes the annotated 100 dialogs are representative of the remaining 120, an assumption the sources do not verify. Even so, the exercise is useful: it confirms that AntiScam is a corpus on the order of **tens of thousands of words**, not hundreds of thousands or millions.

## Composition of the Dataset Alongside Its Size

Size figures are most meaningful when paired with the annotation inventory that must be applied across the data.

### Intent scheme

The paper defines a hierarchical intent scheme. For AntiScam, three on-task intents are defined — *elicitation*, *providing_information*, and *refusal* — while the off-task layer is universal across tasks and comprises six general intents (*open_question*, *yes_no_question*, *positive_answer*, *negative_answer*, *responsive_statement*, *nonresponsive_statement*) and six social intents (*greeting*, *closing*, *apology*, *thanking*, *respond_to_thank*, *hold*) ([Li et al., n.d.](https://gitlab.com/ucdavisnlp/antiscam)). This yields fifteen intent categories in total for the AntiScam configuration.

| Intent category | Items | Count |
|---|---|---|
| On-task (AntiScam-specific) | elicitation, providing_information, refusal | 3 |
| Off-task general | open_question, yes_no_question, positive_answer, negative_answer, responsive_statement, nonresponsive_statement | 6 |
| Off-task social | greeting, closing, apology, thanking, respond_to_thank, hold | 6 |
| **Total** | | **15** |

### Semantic slots

The paper identifies "l 3 main semantic slots in the anti-scam task, for example, credit card numbers," and presents slot examples including *order_detail*, *order_update*, *payment*, *name*, *identity*, *address*, *phone_num*, *card_info*, *card_num*, *card_cvs*, *card_date*, *account_detail*, and *others* ([Li et al., n.d.](https://gitlab.com/ucdavisnlp/antiscam)). The annotation unit is the sentence rather than the turn: each conversation turn is segmented into single sentences and each sentence is labelled ([Li et al., n.d.](https://gitlab.com/ucdavisnlp/antiscam)).

### Social content volume

The appendix reports that attackers and users together "have a massive amount of social content (2 9 2 in total and 2 5 2 in tota1)" ([Li et al., n.d.](https://gitlab.com/ucdavisnlp/antiscam)). These counts indicate that off-task, socially oriented utterances constitute a substantial portion of the annotated sentences in the 100-dialog subset. The paper also reports asymmetries in behaviour: users produced more *refusal* (74 vs. 19), more *open_question* (173 vs. 54), and more *yes_no_question* (165 vs. 117) than attackers ([Li et al., n.d.](https://gitlab.com/ucdavisnlp/antiscam)).

## Scale in Comparative Context

The paper evaluates on a second non-collaborative dataset, PersuasionForGood, which provides a useful yardstick because both corpora share the same off-task intent layer ([Li et al., n.d.](https://gitlab.com/ucdavisnlp/antiscam)).

| Property | AntiScam | PersuasionForGood |
|---|---|---|
| Total dialogs | 220 | 1,017 |
| Dialogs annotated with dialog acts | 100 | 300 |
| Average conversation length | 12.45 turns | 10.43 turns |
| Vocabulary size | Not reported | 8,141 |
| On-task intents | 3 | 9 |
| Off-task intents | 12 (shared scheme) | 12 (shared scheme) |

PersuasionForGood figures are from the paper's dataset section ([Li et al., n.d.](https://gitlab.com/ucdavisnlp/antiscam)). On this comparison, AntiScam is roughly **one-fifth the size** of PersuasionForGood in total dialogs and **one-third the size** in annotated dialogs. Both corpora are small by the standards of contemporary pre-training corpora, but AntiScam's annotation depth per dialog is comparable to or greater than PersuasionForGood's annotated subset: 3,044 sentences across 100 dialogs versus a 300-dialog annotated subset with no reported sentence count.

## Methodological Implications of the Dataset Size

The modest scale of AntiScam explains several design decisions in the paper.

First, the model is pre-trained on the Persona-Chat dataset before fine-tuning on AntiScam, and MISSA is built on the TransferTransfo framework and the generative pre-trained transformer ([Li et al., n.d.](https://gitlab.com/ucdavisnlp/antiscam)). Transfer learning of this kind is a standard response to limited in-domain data.

Second, the paper reports that "we use 8 0 % 8 0\% data for training, 1 0 % 1 0\% data for validation, and 1 0 % 1 0\% data for testing" ([Li et al., n.d.](https://gitlab.com/ucdavisnlp/antiscam)). Applying these proportions to the 220-dialog corpus yields approximately 176 training, 22 validation, and 22 test dialogs; applying them to the 100 annotated dialogs yields approximately 80/10/10. The sources do not resolve which base the proportions were applied to, so both interpretations are presented here.

Third, the paper's data augmentation via nucleus sampling and a rule-based response filter can be read as compensating for the limited number of gold responses available ([Li et al., n.d.](https://gitlab.com/ucdavisnlp/antiscam)).

## Data Collection Procedure Underpinning the Size

The 220 dialogs were produced under a structured role-play. Two workers were randomly paired; one was assigned the role of attacker and the other the role of an everyday user ([Li et al., n.d.](https://gitlab.com/ucdavisnlp/antiscam)). Each worker could participate only once "to prevent workers from knowing their partner's information and goals in advance" ([Li et al., n.d.](https://gitlab.com/ucdavisnlp/antiscam)). Bonuses were offered to attackers for eliciting correct information and to users for detecting attackers and eliciting real information from them ([Li et al., n.d.](https://gitlab.com/ucdavisnlp/antiscam)). The "attacker" additionally received training on how to elicit information, and workers could not see their partners' instructions ([Li et al., n.d.](https://gitlab.com/ucdavisnlp/antiscam)). These constraints help explain why the corpus is small: the design deliberately trades volume for ecological validity and controlled adversarial behaviour.

## Caveats, Ambiguities and Source Discrepancies

Three caveats should accompany any citation of the dataset size.

The first is a terminology discrepancy. The primary paper describes the corpus as containing "human-human dialogs" produced by paired Mechanical Turk workers, one playing an attacker and one a user ([Li et al., n.d.](https://gitlab.com/ucdavisnlp/antiscam)). The third-party note repeatedly describes the same resource as "human-machine anti-scam dialogs" ([Third-party research note](https://gitlab.com/ucdavisnlp/antiscam)). Based on the collection protocol described in the paper, "human–human" is the accurate description and "human–machine" appears to be an error in the secondary note. The systems in the paper that interact with humans are trained models evaluated separately, not the source of the 220-dialog corpus.

The second is scope ambiguity around the averages. The 12.45-turn and 11.13-word averages describe the full 220-dialog corpus, while the 3,044-sentence figure describes only the 100-dialog annotated subset ([Third-party research note](https://gitlab.com/ucdavisnlp/antiscam)).

The third is a potential confusion with evaluation data. The human evaluation collected "2 2 5 number of dialogs" from 15 college-student volunteers, with each model receiving 45 human ratings ([Li et al., n.d.](https://gitlab.com/ucdavisnlp/antiscam)). Those 225 dialogs are evaluation artefacts and are **not** part of the 220-dialog AntiScam corpus; the numerical proximity of 220 and 225 invites error.

## Conclusion

The AntiScam dataset is **220 human–human anti-scam dialogs**, of which **100 dialogs containing 3,044 sentences** carry expert linguistic annotation, with average lengths of **12.45 turns per conversation** and **11.13 words per utterance**, an inter-annotator agreement of **0.874 weighted kappa**, and an attacker-detection rate of **172 of 220 users** ([Li et al., n.d.](https://gitlab.com/ucdavisnlp/antiscam); [Third-party research note](https://gitlab.com/ucdavisnlp/antiscam)). Derived estimates place the full corpus at roughly **2,739 turns**, **30,500 words**, and, if the annotation density of the 100-dialog subset generalises, on the order of **6,700 sentences**.

My assessment, based strictly on these sources, is that AntiScam should be understood as a **small, high-precision benchmark corpus** rather than a large-scale dataset. It is roughly one-fifth the size of PersuasionForGood in dialog count, and its two expert annotators achieved strong agreement across only about 45% of the collected dialogs. Its contribution is therefore best framed as annotation depth and adversarial realism — fifteen hierarchical intent categories, thirteen semantic slots, and a controlled scam role-play — supported by transfer learning from Persona-Chat and TransferTransfo rather than by raw volume ([Li et al., n.d.](https://gitlab.com/ucdavisnlp/antiscam)). Researchers citing the dataset should state the 220-dialog figure and the 100-dialog/3,044-sentence annotated subset separately, and should avoid conflating either with the 225 dialogs gathered for human evaluation.

## References

Li, Y., Qian, K., Shi, W., & Yu, Z. (n.d.). *End-to-End Trainable Non-Collaborative Dialog System* [document_1.txt]. Retrieved from https://gitlab.com/ucdavisnlp/antiscam

Third-party research note: *End-to-End Trainable Non-Collaborative Dialog System* [document_2.txt]. (n.d.). Retrieved from https://gitlab.com/ucdavisnlp/antiscam