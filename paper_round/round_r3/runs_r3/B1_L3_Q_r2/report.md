# How Big Is the AntiScam Dataset? A Multi-Dimensional Assessment of Corpus Size, Composition, and Annotation Depth

## Introduction

The AntiScam dataset is a purpose-built corpus of role-played anti-scam conversations created to support research on non-collaborative dialog systems, in which users and systems do not share a common goal ([Li et al., n.d.](document_1.txt)). Because the question "How big is the AntiScam dataset?" can be answered along several dimensions—absolute dialog count, conversational length, annotation volume, and taxonomic richness—this report provides a structured, multi-metric assessment. The analysis draws primarily on the original paper describing the dataset ([Li et al., n.d.](document_1.txt)), with reference to a third-party research note that summarizes its size and annotation statistics ([Third-Party Research Note, n.d.](document_2.txt)). The central finding is that AntiScam contains **220 dialogs**, of which **100 dialogs and 3,044 sentences** were manually annotated, with an average conversation length of **12.45 turns** and an average utterance length of **11.13 words** ([Li et al., n.d.](document_1.txt)).

## Primary Size Measure: Number of Dialogs

The most direct answer to the query is that the AntiScam dataset comprises **220 dialogs**. The original paper states, "We collected 2 2 0 human-human dialogs" ([Li et al., n.d.](document_1.txt)). The third-party research note corroborates this figure, reporting that "the dataset contains 220 human-machine dialogs" and that "its size is 220 human-machine dialogs" ([Third-Party Research Note, n.d.](document_2.txt)). The numerical agreement between the two sources is unambiguous: 220 dialogs constitute the full corpus.

However, the two sources characterize the participants differently. The primary source describes the data as "human-human dialogs" collected from typed conversations between two Amazon Mechanical Turk workers, one role-playing an attacker and the other an everyday user ([Li et al., n.d.](document_1.txt)). The third-party note instead labels them "human-machine anti-scam dialogs" ([Third-Party Research Note, n.d.](document_2.txt)). Given that the original paper describes a human-human chat and includes an example of a "human-human dialog in AntiScam dataset," the primary source's characterization is more authoritative ([Li et al., n.d.](document_1.txt)). This discrepancy does not alter the headline count of 220 dialogs but is important for consumers of the dataset to understand what "big" means in this context: 220 dyadic, human-to-human, text-based conversations.

The paper also reports that "only 1 7 2 out of 2 2 0 users successfully identified their partner as an attacker," which means approximately 78.2% of users detected the scam ([Li et al., n.d.](document_1.txt)). This outcome is part of the AntiScam dataset description and indicates that the corpus captures a realistic mix of successful and unsuccessful detection scenarios ([Third-Party Research Note, n.d.](document_2.txt)).

## Conversational Length and Utterance-Level Statistics

Beyond the dialog count, the dataset's size can be expressed in turns and words. The paper reports that the "average conversation length is 12.45 turns and the average utterance length is 11.13 words" ([Li et al., n.d.](document_1.txt)). These averages are described by the third-party note as applying to "the full AntiScam corpus" ([Third-Party Research Note, n.d.](document_2.txt)).

Using these reported averages, one can derive rough corpus-level estimates. If there are 220 dialogs and an average of 12.45 turns per dialog, the corpus contains approximately **2,739 turns**. Applying the average utterance length of 11.13 words yields an approximate total of **30,485 words**. These derived figures are estimates based on reported means rather than directly reported totals, and they should be treated as indicative rather than exact. Nevertheless, they help situate the corpus: AntiScam is a small-to-moderate-sized dialog dataset by contemporary standards, but it is densely annotated relative to its size.

| Metric | Reported Value | Source |
|---|---|---|
| Number of dialogs | 220 | Li et al.; Third-Party Research Note |
| Average conversation length | 12.45 turns | Li et al. |
| Average utterance length | 11.13 words | Li et al. |
| Annotated dialogs | 100 | Li et al. |
| Annotated sentences | 3,044 | Li et al. |
| Annotators | 2 expert annotators with linguistic training | Li et al. |
| Inter-annotator agreement | 0.874 averaged weighted kappa | Li et al. |
| Users identifying attacker | 172 of 220 | Li et al. |

## Annotation Coverage and Scale

A crucial dimension of dataset size is annotation volume. Although 220 dialogs were collected, only a subset was manually annotated. The paper reports that "two expert annotators who have linguistic training" annotated "3,0 4 4 sentences in 1 0 0 dialogs," achieving "a 0.8 7 4 averaged weighted kappa value" ([Li et al., n.d.](document_1.txt)). The third-party note confirms that "a subset of 100 dialogs containing 3,044 sentences was manually annotated" ([Third-Party Research Note, n.d.](document_2.txt)).

This means that 100 of the 220 dialogs—approximately **45.5% of the corpus**—received manual sentence-level annotation. Within those 100 dialogs, 3,044 sentences were annotated, yielding an average of roughly **30.4 sentences per annotated dialog**. Given the reported average of 12.45 turns per conversation, this implies roughly 2.44 sentences per turn in the annotated subset, reflecting the paper's design decision to "segment each conversation turn into single sentences and then annotate each sentence rather than turns" ([Li et al., n.d.](document_1.txt)).

The 0.874 weighted kappa value indicates a high level of agreement between the two annotators, which strengthens confidence in the annotation quality even though the annotated subset is relatively small ([Li et al., n.d.](document_1.txt)). For researchers considering reuse, the effective annotated size is therefore 100 dialogs and 3,044 sentences, while the full 220-dialog corpus provides additional unannotated material. The paper notes that it releases "the code and data" at a public repository, indicating that the dataset is accessible for replication and extension ([Li et al., n.d.](document_1.txt)).

## Compositional Size: On-Task versus Off-Task Content

The AntiScam dataset was explicitly designed to "interleave the on-task and off-task contents in the conversation" ([Li et al., n.d.](document_1.txt)). This compositional feature affects how its size should be interpreted. The paper reports that "attackers and users both have a massive amount of social content (2 9 2 in total and 2 5 2 in total), suggesting that it is important to have social intent sentences to maintain the conversation" ([Li et al., n.d.](document_1.txt)). Thus, in addition to task-oriented exchanges (elicitation, providing information, refusal), the corpus contains hundreds of socially oriented sentences that are essential to its non-collaborative framing.

The distribution of intents also differs by role. Compared with attackers, users produce more refusals (74 vs. 19), ask more open questions (173 vs. 54), and ask more yes/no questions (165 vs. 117) ([Li et al., n.d.](document_1.txt)). These asymmetries indicate that the dataset is not merely large in raw counts but is structured to capture the divergent conversational strategies of attackers and defenders—a qualitative dimension of "size" that matters for training and evaluating non-collaborative systems. The presence of substantial off-task content also confirms the necessity of the hierarchical annotation scheme that separates task-specific and general intents ([Li et al., n.d.](document_1.txt)).

## Intent and Semantic Slot Taxonomy as a Measure of Annotation Richness

The annotation schema further characterizes the dataset's size in terms of label space. The hierarchical intent scheme separates on-task intents, general off-task intents, and social intents ([Li et al., n.d.](document_1.txt)). For AntiScam, the on-task intents are "elicitation, providing_information and refusal" ([Li et al., n.d.](document_1.txt)). The general off-task intents are six in number: open_question, yes_no_question, positive_answer, negative_answer, responsive_statement, and nonresponsive_statement; the social intents are also six: greeting, closing, apology, thanking, respond_to_thank, and hold ([Li et al., n.d.](document_1.txt)). This yields a **15-category intent taxonomy** spanning task and social dimensions.

In addition, the dataset uses **13 semantic slots** for the anti-scam domain, such as order_detail, order_update, payment, name, identity, address, phone_num, card_info, card_num, card_cvs, card_date, account_detail, and others ([Li et al., n.d.](document_1.txt)). The combination of 15 intent categories and 13 slot categories applied at sentence level gives the annotated subset substantial label density: 3,044 sentences × multiple possible intents and slots per sentence. This label richness is a meaningful aspect of the dataset's "size" for machine learning purposes, even if the dialog count is modest. The paper emphasizes that the semantic slot information enables the model "to keep track of the current entities, and the intent information helps MISSA to maintain coherency and prolong conversations" ([Li et al., n.d.](document_1.txt)).

## Collection Methodology and Its Bearing on Dataset Size

The size of AntiScam is a direct consequence of its collection methodology. The corpus was gathered through "a role-playing task on the Amazon Mechanical Turk platform," in which two workers were randomly paired: one assigned the role of an attacker attempting to elicit personal information, and the other an everyday user aiming to protect their information and potentially elicit the attacker's information ([Li et al., n.d.](document_1.txt)). Workers could participate only once, "to prevent workers from knowing their partner's information and goals in advance" ([Li et al., n.d.](document_1.txt)). Bonuses incentivized attackers to elicit correct information and users to detect attackers and prolong conversations ([Li et al., n.d.](document_1.txt)).

This design supports data quality but constrains scale: each worker contributed only once, and the resulting 220 dialogs represent the realized sample. The attackers were "well-trained to pretend to be an Amazon customer service agent," and to simulate a real-world scam, they were given some details about the user, such as the user's name, to prevent them from being too easily identified ([Li et al., n.d.](document_1.txt)). The dataset thus reflects a carefully controlled elicitation setting rather than an opportunistic scrape of naturally occurring conversations.

## Comparative Context: AntiScam versus PersuasionForGood

To contextualize AntiScam's size, it is useful to compare it with the PersuasionForGood dataset, the other non-collaborative corpus used in the paper's experiments. PersuasionForGood "consists of 1,0 1 7 dialogs, where 3 0 0 dialogs are annotated with dialog acts," with an average conversation length of 10.43 and a vocabulary size of 8,141 ([Li et al., n.d.](document_1.txt)). By contrast, AntiScam has 220 dialogs, 100 annotated dialogs, and an average conversation length of 12.45 turns ([Li et al., n.d.](document_1.txt)).

| Metric | AntiScam | PersuasionForGood |
|---|---|---|
| Total dialogs | 220 | 1,017 |
| Annotated dialogs | 100 | 300 |
| Average conversation length | 12.45 turns | 10.43 turns |
| Vocabulary size | Not reported | 8,141 |
| Domain | Anti-scam / fraud deterrence | Charity donation persuasion |

The comparison shows that AntiScam is smaller in total dialog count (220 vs. 1,017) and in annotated dialog count (100 vs. 300), though its average conversation length is slightly longer (12.45 vs. 10.43 turns) ([Li et al., n.d.](document_1.txt)). Its annotated sentence count of 3,044 provides a concrete measure of annotation volume that complements the dialog-level comparison. The paper presents AntiScam as a benchmark for non-collaborative tasks and as a complement to existing datasets, noting that "as non-collaborative tasks are still relatively new to the study of dialog systems, there are insufficiently many meaningful datasets for evaluation" ([Li et al., n.d.](document_1.txt)).

## How the Dataset Was Used: Training and Evaluation Scale

The paper's experimental setup provides further evidence of AntiScam's scale. The authors used "8 0 % data for training, 1 0 % data for validation, and 1 0 % data for testing" ([Li et al., n.d.](document_1.txt)). For human evaluation, they recruited "1 5 college-student volunteers," each of whom interacted with all models at least three times, yielding "2 2 5 number of dialogs" and "a total of 4 5 human ratings" per model ([Li et al., n.d.](document_1.txt)). These figures describe the evaluation protocol rather than the dataset itself, but they illustrate the practical scale at which the dataset operates: small enough for detailed human evaluation, yet large enough to train and compare multiple models. The paper reports that the proposed MISSA model maintained longer conversations (14.9 turns) compared with the TransferTransfo baseline (8.5 turns), which is a direct consequence of training on the AntiScam corpus's interleaved on-task and off-task content ([Li et al., n.d.](document_1.txt)).

## Reliability of Sources and Data Discrepancies

The primary source is the original paper, which provides the definitive dataset description, annotation statistics, and collection methodology ([Li et al., n.d.](document_1.txt)). The third-party research note is a secondary summary that corroborates the core numbers—220 dialogs, 100 annotated dialogs, 3,044 sentences, 12.45-turn average, 11.13-word average, and 172 of 220 users identifying the attacker ([Third-Party Research Note, n.d.](document_2.txt)). The most notable discrepancy is the "human-human" versus "human-machine" labeling; the primary source's "human-human" description is more consistent with its detailed account of paired MTurk workers and its example dialog ([Li et al., n.d.](document_1.txt)). Researchers should therefore treat the 220-dialog count as reliable while being precise about the human-human nature of the interactions.

## Conclusion

In summary, the AntiScam dataset is a 220-dialog corpus of human-human, role-played anti-scam conversations, of which 100 dialogs containing 3,044 sentences have been manually annotated with a hierarchical intent scheme and 13 semantic slots ([Li et al., n.d.](document_1.txt)). The average conversation is 12.45 turns long, and the average utterance is 11.13 words ([Li et al., n.d.](document_1.txt)). Approximately 172 of 220 users successfully identified their partner as an attacker ([Li et al., n.d.](document_1.txt)). While modest in absolute dialog count compared with larger corpora such as PersuasionForGood's 1,017 dialogs, AntiScam is densely annotated, purpose-built for non-collaborative dialog research, and publicly released to serve as a benchmark ([Li et al., n.d.](document_1.txt)). Its size is therefore best understood not as a single number but as a combination of **220 dialogs, roughly 2,739 turns, an estimated 30,000+ words, 3,044 annotated sentences, 15 intent categories, and 13 semantic slots**. In my assessment, based on the given information, AntiScam should be characterized as a small but annotation-rich dataset whose value lies in its carefully controlled collection, its realistic interleaving of on-task and social content, and its role as a reproducible benchmark for non-collaborative dialog systems.

## References

Li, Y., Qian, K., Shi, W., & Yu, Z. (n.d.). *End-to-end trainable non-collaborative dialog system* [Document]. document_1.txt.

Third-Party Research Note. (n.d.). *Third-party research note: End-to-end trainable non-collaborative dialog system* [Document]. document_2.txt.