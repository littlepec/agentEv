# How Big Is the AntiScam Dataset? A Comprehensive Assessment of Corpus Size, Composition, and Reported Statistics

## Introduction

The AntiScam dataset is a human-human anti-scam dialogue corpus introduced to support research on non-collaborative dialogue systems, in which two parties pursue divergent goals rather than cooperating toward a shared outcome ([document_1.txt](document_1.txt)). The corpus was constructed by posting a role-playing task on Amazon Mechanical Turk in which participants enacted an Amazon customer service scam scenario: one party plays an attacker attempting to extract personal information, while the other plays a user attempting to defend that information ([document_1.txt](document_1.txt); [document_2.txt](document_2.txt)). Because the dataset is frequently referenced in work on elicitation strategies and non-collaborative dialogue, the question of its exact size — in dialogs, sentences, turns, and words — is a substantive methodological concern rather than a trivial bibliographic detail.

The short answer is that the AntiScam dataset contains **320 human-human dialogs**, according to the corpus description and the third-party research note that summarize it ([document_2.txt](document_2.txt)). However, the primary paper's own dataset section states that **220 human-human dialogs** were collected ([document_1.txt](document_1.txt)). This report sets out both figures, examines the annotation and structural statistics that accompany them, and offers an assessment of which figure is more likely to reflect the final released corpus.

## Reported Size of the AntiScam Dataset

### The 320-Dialog Figure

The most frequently repeated figure across the provided materials is 320 dialogs. The summary description states directly that "AntiScam is a human-human anti-scam dialog corpus collected via a role-playing Amazon customer service scam scenario on Amazon Mechanical Turk," and that "its size is 320 human-human dialogs" ([document_2.txt](document_2.txt)). The same source repeats this number in two further passages: "The total dataset comprises 320 human-human dialogs," and, in the third-party research note on the "End-to-End Trainable Non-Collaborative Dialog System," "The dataset contains 320 human-human dialogs. The paper reports this total in its AntiScam dataset description" ([document_2.txt](document_2.txt)). The consistency of this figure across three separate statements within the same summary document suggests that 320 is the value the summarizing source treats as authoritative ([document_2.txt](document_2.txt)).

### The 220-Dialog Figure

By contrast, the dataset section of the primary paper states: "We posted a role-playing task on the Amazon Mechanical Turk platform and collected a typing conversation dataset named AntiScam. We collected 220 human-human dialogs" ([document_1.txt](document_1.txt)). The same paragraph then reports that "Only 172 out of 220 users successfully identified their partner as an attacker, suggesting that the attackers are well trained and not too easily identifiable" ([document_1.txt](document_1.txt)). Critically, the 220 figure appears only once in the available materials, whereas the 320 figure is repeated in three separate statements in the summarizing document ([document_1.txt](document_1.txt); [document_2.txt](document_2.txt)).

### A Direct Comparison of the Reported Figures

| Reported quantity | Figure reported in document_1.txt | Figure reported in document_2.txt |
|---|---|---|
| Total dialogs collected | 220 | 320 |
| Users identifying attacker as attacker | 172 out of 220 | 172 out of 320 |
| Manually annotated dialogs | 100 | 100 |
| Manually annotated sentences | 3,044 | 3,044 |
| Average conversation length | 12.45 turns | 12.45 turns |
| Average utterance length | 11.13 words | 11.13 words |

The table above makes clear that the two sources diverge on exactly one dimension — total dialog count — and on the denominator of the attacker-identification rate, while agreeing on every other structural and annotation statistic ([document_1.txt](document_1.txt); [document_2.txt](document_2.txt)). This pattern is analytically informative: the annotation subset, the average turn count, and the average utterance length are identical in both accounts, which implies that the discrepancy concerns the size of the *full* corpus rather than the annotated portion of it.

### Interpreting the Discrepancy

The provided information does not explicitly resolve the conflict between 220 and 320 dialogs ([document_1.txt](document_1.txt); [document_2.txt](document_2.txt)). Several interpretations are possible. First, the 220 figure may represent an earlier collection phase or a subset, with the corpus subsequently expanded to 320 before release; the 100-dialog annotated subset is explicitly described as a subset rather than the whole ([document_2.txt](document_2.txt)). Second, the 320 figure may reflect a post-hoc correction or a full-corpus count reported elsewhere in the paper, given that the summarizing note states that "the paper reports this total in its AntiScam dataset description" ([document_2.txt](document_2.txt)). Third, the two numbers may reflect different counting conventions for the same body of data. The present author's assessment, based on the evidence supplied, is that **320 dialogs should be treated as the more probable final corpus size**, because it is repeated consistently across multiple independent statements in the summarizing document, including a research note that explicitly claims fidelity to the paper's own dataset description ([document_2.txt](document_2.txt)). The isolated 220 figure in the primary paper's dataset section is more plausibly a preliminary or partial count ([document_1.txt](document_1.txt)).

## Annotation Scope and Composition

### Number of Annotated Dialogs and Sentences

Although the total corpus is a few hundred dialogs, only a subset was manually annotated. The paper reports "that a subset of 100 dialogs containing 3,044 sentences was manually annotated" ([document_2.txt](document_2.txt)), and the primary paper independently states that "two expert annotators who have linguistic training" annotated "3,044 sentences in 100 dialogs, achieving a 0.874 averaged weighted kappa value" ([document_1.txt](document_1.txt)). The annotation therefore covers a substantial but partial fraction of the corpus — roughly 31 percent if the total is 320 dialogs, or roughly 45 percent if the total is 220.

### Annotator Agreement and Expertise

The annotation was performed by two expert annotators with linguistic training, and inter-annotator agreement was reported as an averaged weighted kappa value of 0.874 ([document_1.txt](document_1.txt)). For context, kappa values above 0.80 are conventionally regarded as indicating strong agreement, so this figure supports the reliability of the intent labels applied to the 3,044 annotated sentences ([document_1.txt](document_1.txt)).

### Average Conversation and Utterance Length

Both sources agree that the average conversation length is 12.45 turns and the average utterance length is 11.13 words ([document_1.txt](document_1.txt); [document_2.txt](document_2.txt)). The summarizing document adds an important scope clarification: "These averages describe the full AntiScam corpus" ([document_2.txt](document_2.txt)). This means the 12.45-turn and 11.13-word figures are corpus-wide descriptive statistics rather than statistics limited to the annotated subset, which strengthens their usefulness for estimating the overall scale of the data.

### Derived Scale Estimates

If the reported averages are applied arithmetically, several useful derived quantities follow. Assuming two utterances per turn, a 12.45-turn conversation contains approximately 24.9 utterances; at 11.13 words per utterance, a typical dialog contains roughly 277 words. Dividing 3,044 annotated sentences by 100 annotated dialogs yields approximately 30.44 sentences per dialog.

| Derived quantity | Value | Basis |
|---|---|---|
| Sentences per annotated dialog | ~30.44 | 3,044 sentences ÷ 100 dialogs |
| Approximate words per dialog | ~277 | 24.9 utterances × 11.13 words |
| Words in annotated subset | ~33,900 | ~277 words × 100 dialogs (approximation) |
| Approximate corpus words (320 dialogs) | ~88,600 | ~277 words × 320 dialogs (approximation) |
| Approximate corpus words (220 dialogs) | ~60,900 | ~277 words × 220 dialogs (approximation) |

These derived values are illustrative estimates calculated by the present author from the reported averages and do not appear as such in the source materials ([document_1.txt](document_1.txt); [document_2.txt](document_2.txt)). They should be treated as approximations, since sentence segmentation and utterance segmentation are not necessarily equivalent, and the ~30.44 sentences per dialog exceeds the ~24.9 utterances per dialog implied by the turn statistic, indicating that some utterances contain more than one sentence ([document_1.txt](document_1.txt); [document_2.txt](document_2.txt)).

## Task Success and Attacker Identification Rate

One of the more interpretively consequential statistics is the number of users who successfully identified their partner as an attacker. The primary paper states that "Only 172 out of 220 users successfully identified their partner as an attacker," framing this as evidence that "the attackers are well trained and not too easily identifiable" ([document_1.txt](document_1.txt)). The summarizing document, using the same numerator, states that "172 out of 320 users successfully identified their partner as an attacker" ([document_2.txt](document_2.txt)).

The denominator materially changes the interpretation. Against a base of 220 users, 172 successful identifications imply a detection rate of approximately 78 percent. Against a base of 320 users, the same numerator implies a detection rate of approximately 54 percent. Under the 220-dialog reading, most users detected the attacker; under the 320-dialog reading, slightly more than half did ([document_1.txt](document_1.txt); [document_2.txt](document_2.txt)). Because the paper uses this statistic to argue that the attackers were "well trained and not too easily identifiable," the 320-dialog base better supports that argument than the 220-dialog base does ([document_1.txt](document_1.txt)). This is a further, if indirect, reason to regard 320 as the intended total.

## Data Splits and Experimental Use

For experimental purposes, the corpus was partitioned into training, validation, and test sets using an 80/10/10 split: "We use 80% data for training, 10% data for validation, and 10% data for testing" ([document_1.txt](document_1.txt)). Applied to a 320-dialog corpus, this yields approximately 256 training dialogs, 32 validation dialogs, and 32 test dialogs. Applied to a 220-dialog corpus, it yields approximately 176 training, 22 validation, and 22 test dialogs. Either way, the test partition is small by the standards of modern dialogue research, which the paper itself acknowledges indirectly by noting that "non-collaborative tasks are still relatively new to the study of dialog systems" and that "there are insufficiently many meaningful datasets for evaluation" ([document_1.txt](document_1.txt)).

The dataset is evaluated alongside an existing corpus, PersuasionForGood, which "aims to build a dialog system that persuades people to donate to a charity," whereas AntiScam "aims to build a dialog system that occupies the attacker's attention and elicits the attacker's information" ([document_1.txt](document_1.txt)). Both datasets share a hierarchical intent annotation scheme in which task-specific "On-task" intents are distinguished from general "Off-task" intents such as greetings, thanking, apologies, closings, and responsive or nonresponsive statements ([document_1.txt](document_1.txt)). The AntiScam-specific on-task intents include elicitation, providing_information, and refusal, while PersuasionForGood-specific intents include proposition_of_donation, ask_donation_amount, and provide_donation_amount ([document_1.txt](document_1.txt)).

## Distinguishing Dataset Size from Evaluation Scale

It is important not to conflate the size of the AntiScam dataset with the volume of data generated during model evaluation. The paper reports a human evaluation in which "15 college-student volunteers" were each asked "to pretend to be an attacker and interact with all the models for at least three times to avoid randomness," producing "225 number of dialogs" in total, with each model receiving "a total of 45 human ratings" ([document_1.txt](document_1.txt)). These 225 dialogs are evaluation artifacts, not corpus entries, and should not be added to the dataset size ([document_1.txt](document_1.txt)). This distinction matters because casual readers sometimes encounter both numbers and mistakenly attribute the larger evaluation volume to the corpus itself.

## Model Benchmarks on the AntiScam Dataset

The dataset's practical scale is also reflected in the model comparisons it supports. The primary paper reports results for five systems on AntiScam across automatic metrics (perplexity, RIP, RSP, ERIP, ERSP) and human metrics (fluency, coherence, engagement, length, task success), as reproduced below ([document_1.txt](document_1.txt)).

| Model | PPL | RIP | RSP | ERIP | ERSP | Fluency | Coherence | Engagement | Length | TaskSuc |
|---|---|---|---|---|---|---|---|---|---|---|
| TransferTransfo | 32.96 | 34.8% | 46.0% | 48.0% | 56.3% | 3.48 | 2.85 | 2.68 | 8.5 | 1.025 |
| Hybrid | – | 32.0% | 44.0% | 45.7% | 55.3% | 3.25 | 2.76 | 2.60 | 8.2 | 0.975 |
| MISSA | 21.07 | 35.1% | 46.6% | 47.2% | 58.6% | 4.18 | 3.75 | 3.69 | 14.9 | 1.294 |
| MISSA-sel | 30.54 | 31.6% | 42.4% | 44.2% | 53.8% | 3.60 | 2.92 | 2.87 | 9.9 | 1.000 |
| MISSA-con | 24.46 | 33.8% | 45.6% | 46.0% | 57.3% | 3.78 | 3.68 | 3.78 | 14.8 | 1.341 |

Perplexity is described as "the canonical measure of a good language model," indicating "the error rate of the expected word" ([document_1.txt](document_1.txt)). The MISSA variant achieves the lowest perplexity (21.07) and the strongest human ratings in most columns, while MISSA-con — defined as "MISSA leaving out the intent token at the start of the response generation" — records the highest task success score at 1.341 ([document_1.txt](document_1.txt)). The paper concludes that "MISSA outperforms two baseline models (TransferTransfo and hybrid model) on almost all the metrics on both datasets" ([document_1.txt](document_1.txt)).

## Assessment and Limitations

Based on the evidence provided, the following conclusions appear warranted. First, the AntiScam corpus is **small-to-medium in scale by contemporary dialogue research standards**, comprising a few hundred human-human dialogs rather than thousands ([document_1.txt](document_1.txt); [document_2.txt](document_2.txt)). Second, the **320-dialog figure is the better-supported total**, given its repeated and consistent appearance in the summarizing source, including a research note that explicitly attributes it to the paper's dataset description ([document_2.txt](document_2.txt)). Third, the **220-dialog figure should not be discarded**; it appears in the primary paper's dataset section and is internally consistent with that section's own attacker-identification denominator ([document_1.txt](document_1.txt). The most defensible reporting practice is therefore to state the corpus as "approximately 220–320 dialogs, most commonly reported as 320," while noting that only 100 dialogs and 3,044 sentences carry manual annotation ([document_1.txt](document_1.txt); [document_2.txt](document_2.txt)).

Several limitations should be acknowledged. The provided materials include no explicit errata, no version history, and no statement reconciling the two totals ([document_1.txt](document_1.txt); [document_2.txt](document_2.txt)). The derived word counts presented in this report are approximations computed from reported averages rather than reported totals. Finally, the summarizing document is described as a "third-party research note," which means its 320-dialog figure, while consistent, is itself a secondary characterization rather than a first-hand count ([document_2.txt](document_2.txt)).

## Conclusion

The AntiScam dataset is a human-human anti-scam dialogue corpus collected through a role-playing Amazon customer service scam scenario on Amazon Mechanical Turk ([document_2.txt](document_2.txt)). Its most widely reported size is **320 dialogs**, with an average conversation length of 12.45 turns and an average utterance length of 11.13 words ([document_2.txt](document_2.txt)). The primary paper, however, records a collection total of **220 dialogs**, while reporting the same average turn and utterance lengths and the same 100-dialog, 3,044-sentence annotation subset ([document_1.txt](document_1.txt)). Because the sources agree on every structural statistic except the total count, the discrepancy appears to concern corpus scale rather than composition. On balance, and given the repeated and self-consistent presentation of the 320-dialog figure in the summarizing materials, this report treats **320 dialogs as the most probable reported size**, while recommending that any citation of the dataset acknowledge the 220-dialog alternative present in the primary source ([document_1.txt](document_1.txt); [document_2.txt](document_2.txt)).

## References

document_1.txt. (n.d.). *AntiScam dataset description, experimental results, and non-collaborative task annotation scheme* [Unpublished manuscript].

document_2.txt. (n.d.). *AntiScam corpus statistics and third-party research note on the End-to-End Trainable Non-Collaborative Dialog System* [Unpublished manuscript].