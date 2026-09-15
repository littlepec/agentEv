# Datasets Used in “Convolutional Neural Networks and a Transfer Learning Strategy to Classify Parkinson’s Disease from Speech in Three Different Languages”

## Introduction

The study under examination proposes a cross-lingual methodology for classifying Parkinson’s disease (PD) from speech, combining convolutional neural networks (CNNs) trained on time–frequency representations with a transfer learning strategy across languages ([Vásquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)). Because the validity and the generalizability of any supervised classification study depend directly on the data on which it is built, this report identifies, describes, and evaluates the datasets employed. The analysis draws primarily on the peer-reviewed arXiv preprint that reports the study (document_1) and secondarily on a derivative third-party research note (document_2) that summarizes the same work. As demonstrated below, the primary source establishes that the three datasets correspond to **Spanish, German, and Czech** speech, whereas the third-party note incorrectly substitutes Italian for German ([Third-party research note, n.d.](document_2.txt)). The report therefore details the three corpora, their speaker composition, recording conditions, speech tasks, clinical evaluations, and the derived data structures used for modeling.

## Overview of the Three Datasets

The study evaluates speech recordings of PD patients and healthy control (HC) speakers in three languages: Spanish, German, and Czech ([Vásquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)). All recordings were captured under noise-controlled conditions, and all speech signals were down-sampled to 16 kHz ([Vásquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)). The three datasets are not a single unified corpus but rather three independent language-specific collections that were harmonized methodologically for the cross-lingual experiments. It is important to distinguish these three experimental datasets from other corpora mentioned only as related literature in the introduction — for example, a Turkish dataset of 20 PD patients and 20 HC subjects used in prior work, and Czech data used in the related work of Rusz et al. ([Vásquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)). Those corpora are cited as context but are not among the datasets analyzed in this study.

| Language | Corpus / Source | PD Speakers | HC Speakers | Total Speakers |
|---|---|---|---|---|
| Spanish | PC-GITA corpus | 50 | 50 | 100 |
| German | German speech recordings | 88 | 88 | 176 |
| Czech | Czech speech recordings | 50 | 50 | 100 |

*Table 1. Summary of the three datasets used in the study. Figures are taken from Section 2.1 of the primary source ([Vásquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)).*

## Spanish Dataset: PC-GITA Corpus

### Composition and Speaker Population

The Spanish portion of the data comes from the **PC-GITA corpus**, which contains utterances from 50 PD patients and 50 HC speakers who are Colombian Spanish native speakers ([Vásquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)). The corpus is described in the study’s reference list as a “New Spanish Speech Corpus Database for the Analysis of People Suffering from Parkinson’s Disease,” presented at the Ninth International Conference on Language Resources and Evaluation ([Orozco-Arroyave et al., 2014](https://arxiv.org/abs/2002.04374)). The PC-GITA corpus is thus the only explicitly named corpus among the three datasets, and it constitutes the Spanish half of the cross-lingual design.

### Speech Tasks

Participants in the Spanish dataset were asked to pronounce a total of 10 sentences, the rapid repetition of the syllables /pa-ta-ka/, /pe-ta-ka/, /pa-ka-ta/, /pa/, /ta/, and /ka/, one text with 36 words, and a monologue ([Vásquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)). A clinically relevant detail is that all Spanish patients were recorded in the **ON state**, that is, under the effect of their daily medication ([Vásquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)). This medication status is a meaningful methodological consideration, because dopaminergic medication can influence speech motor performance and therefore the acoustic markers available to the classifier.

## German Dataset

### Composition and Speaker Population

The German data consist of speech recordings of **88 PD patients and 88 HC speakers from Germany**, yielding the largest speaker population among the three datasets ([Vásquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)). The source of this dataset is cited as Skodda, Visser, and Schlegel’s study on vowel articulation in Parkinson’s disease, published in the *Journal of Voice* ([Skodda et al., 2011](https://arxiv.org/abs/2002.04374)).

### Speech Tasks

German participants performed four speech tasks: the rapid repetition of /pa-ta-ka/, five sentences, one text with 81 words, and a monologue ([Vásquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)). The task battery overlaps partially with the Spanish protocol (rapid syllable repetition, connected text, and monologue) but differs in the number of sentences and in the length of the read text, reflecting the practical reality of pooling independently designed corpora.

## Czech Dataset

### Composition and Speaker Population

The Czech data comprise a total of **100 native Czech speakers, consisting of 50 PD patients and 50 HC speakers** ([Vásquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)). The dataset is attributed to Rusz’s habilitation thesis, “Detecting Speech Disorders in Early Parkinson’s Disease by Acoustic Analysis,” completed at the Czech Technical University in Prague ([Rusz, 2018](https://arxiv.org/abs/2002.04374)).

### Speech Tasks

The Czech participants performed the rapid repetition of the syllables /pa-ta-ka/, a read text with 80 words, and a monologue ([Vásquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)). As with the other two datasets, the protocol includes a diadochokinetic task, connected speech, and spontaneous speech, which supports the extraction of the voiced–unvoiced transition segments central to the modeling approach.

## Consolidated Speaker Demographics and Clinical Profiles

The primary source provides detailed demographic and clinical information for all three datasets, reproduced in Table 2 below ([Vásquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)). These figures are essential for judging comparability across languages and for interpreting the classification results.

| Group | Gender | Spanish PD | Spanish HC | German PD | German HC | Czech PD | Czech HC |
|---|---|---|---|---|---|---|---|
| Speakers | M | 25 | 25 | 47 | 44 | 30 | 30 |
| Speakers | F | 25 | 25 | 41 | 44 | 20 | 20 |
| Age range | M | 33–81 | 31–86 | 44–82 | 26–83 | 43–82 | 41–77 |
| Age range | F | 49–75 | 49–76 | 42–84 | 28–85 | 41–72 | 40–79 |
| Mean age (SD) | M | 61.3 (11.4) | 60.5 (11.6) | 66.7 (8.7) | 63.8 (12.7) | 65.3 (9.6) | 60.3 (11.5) |
| Mean age (SD) | F | 60.7 (7.3) | 61.4 (7.0) | 66.2 (9.7) | 62.6 (15.2) | 60.1 (8.7) | 63.5 (11.1) |
| Time after diagnosis (years) | M | 8.7 (5.9) | – | 7.0 (5.5) | – | 6.7 (4.5) | – |
| Time after diagnosis (years) | F | 12.6 (11.6) | – | 7.1 (6.2) | – | 6.8 (5.2) | – |
| MDS-UPDRS-III | M | 37.8 (22.1) | – | 22.1 (9.9) | – | 21.4 (11.5) | – |
| MDS-UPDRS-III | F | 37.6 (14.1) | – | 23.3 (12.0) | – | 18.1 (9.7) | – |

*Table 2. Speaker demographics, disease duration, and clinical severity across the three datasets ([Vásquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)). G. = gender; M. = male; F. = female; T = time after diagnosis in years.*

A notable feature of these data is the difference in disease severity. The Spanish PD group exhibits substantially higher mean MDS-UPDRS-III scores (37.8 for males and 37.6 for females) than the German (22.1 and 23.3) and Czech (21.4 and 18.1) groups ([Vásquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)). The authors explicitly attribute the cross-lingual differences in classification performance to this disparity, noting that “there are patients with higher disease severity in the Spanish data compared to German and Czech patients” ([Vásquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)). This finding has direct implications for the interpretation of the transfer learning results: the Spanish dataset appears to offer the strongest initial separability, which explains why it serves as the most effective base language for German and Czech targets.

## Clinical Evaluation and Recording Conditions

Across all three datasets, patients were evaluated by a neurologist expert according to the third section of the Movement Disorder Society–sponsored revision of the Unified Parkinson’s Disease Rating Scale (MDS-UPDRS-III) ([Vásquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374); [Goetz et al., 2008](https://arxiv.org/abs/2002.04374)). This shared clinical instrument is a significant strength of the study, because it provides a common severity metric across the three language cohorts despite their independent provenance. Recordings were captured in noise-controlled conditions and down-sampled to 16 kHz, which standardizes the signal acquisition pipeline for downstream modeling ([Vásquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)).

## Derived Data Structures Used for Modeling

Beyond the raw corpora, the study constructs two derived representations from the speech signals. First, speech is segmented based on the automatic detection of onset and offset transitions between voiced and unvoiced frames, with 80 ms of signal taken to each side to form 160 ms segments ([Vásquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)). These transitions are intended to model the difficulty PD patients experience in starting and stopping vocal fold vibration.

For the baseline model, features extracted from these transitions include 12 Mel-Frequency Cepstral Coefficients (MFCCs) with their first and second derivatives, plus the log energy of the signal distributed into 22 Bark bands, giving 58 descriptors; four statistical functionals (mean, standard deviation, skewness, and kurtosis) are then computed per descriptor, producing a 232-dimensional feature vector per utterance, classified with a radial basis SVM (C = 10, γ = 0.0001) under speaker-independent 10-fold cross-validation ([Vásquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)).

For the CNN model, short-time Fourier transform representations with 256 frequency bins are computed with a 16 ms window and 4 ms step, yielding 41 time frames per transition; the spectrogram is then mapped to the Mel scale using 80 filters, producing an 80 × 41 input ([Vásquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)). The final decision for each speaker is obtained by a majority voting strategy across the different speech exercises ([Vásquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)). These derived structures are important to report because they define the effective dataset on which the CNN and transfer learning experiments operate.

## Verification of Language Composition: A Discrepancy in the Third-Party Note

A critical finding of this review is that the third-party research note (document_2) misreports the languages used in the study. The note states that “the study uses speech recordings of patients in three different languages: Spanish, Italian, and Czech,” and asserts that “the Italian dataset contains speech recordings of 88 PD patients and 88 HC speakers from Italy” ([Third-party research note, n.d.](document_2.txt)). This is inconsistent with the primary source in multiple independent locations:

1. **Abstract:** The study is explicitly described as classifying PD from speech “in three different languages: Spanish, German, and Czech” in both the abstract and the conclusion ([Vásquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)).
2. **Section 2.1 (Data):** The subsection heading is “German,” and the text states that “speech recordings of 88 PD patients and 88 HC speakers from Germany are considered” ([Vásquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)).
3. **Table 1:** The column header for the third-language dataset is “German,” with speaker counts matching those attributed to Italy by the note ([Vásquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)).
4. **Table 4 (Transfer learning results):** The base and target languages listed are Spanish, German, and Czech, with no Italian entry ([Vásquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)).

The speaker counts cited in the third-party note (88 PD and 88 HC) coincide exactly with the German dataset, which strongly suggests a substitution error in which “German” was mistakenly rendered as “Italian” ([Third-party research note, n.d.](document_2.txt); [Vásquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)). Consequently, the valid answer to the question of which datasets are used is **PC-GITA (Colombian Spanish), the German dataset, and the Czech dataset** — not Italian.

## Dataset Provenance and Reliability Assessment

From an evidential standpoint, the primary source (document_1) is the study itself, an arXiv preprint with a complete description of methods, results, and references, authored by the researchers who performed the work ([Vásquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)). It therefore constitutes the authoritative record of the datasets. The third-party research note (document_2) is a derivative summary that lacks independent verification and contains at least one demonstrable factual error ([Third-party research note, n.d.](document_2.txt)). Following the principle of prioritizing reliable and primary sources, this report treats document_1 as controlling and uses document_2 only where it corroborates the primary record (for example, in confirming the PC-GITA composition and the MDS-UPDRS-III evaluation procedure).

The underlying corpora themselves are documented in established venues: PC-GITA in the Proceedings of the Ninth International Conference on Language Resources and Evaluation ([Orozco-Arroyave et al., 2014](https://arxiv.org/abs/2002.04374)); the German data in the *Journal of Voice* ([Skodda et al., 2011](https://arxiv.org/abs/2002.04374)); and the Czech data in a habilitation thesis at the Czech Technical University in Prague ([Rusz, 2018](https://arxiv.org/abs/2002.04374)). This provenance supports the credibility of the datasets, although it also highlights that the three corpora were originally collected for separate purposes and later combined, which introduces heterogeneity in task protocols and speaker characteristics.

## Discussion and Synthesis

Several observations emerge from this dataset review. First, the study’s cross-lingual design rests on three datasets of unequal size and severity: Spanish (100 speakers), German (176 speakers), and Czech (100 speakers) ([Vásquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)). Second, the language cohorts differ systematically in clinical profile, with the Spanish patients being the most severely affected according to MDS-UPDRS-III ([Vásquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)). This difference plausibly explains why Spanish served as the most effective base language for transfer learning, improving German accuracy from 69.3% at baseline to 77.3% and Czech accuracy from 68.5% to 72.6% ([Vásquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)). Third, gender balance varies by dataset: the Spanish data are perfectly balanced (25/25 for both PD and HC), whereas the German data are less balanced (47 male and 41 female PD patients; 44/44 HC), and the Czech data show a 30/20 male-to-female split for both PD and HC groups ([Vásquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)). These compositional differences are relevant when interpreting specificity and sensitivity results, which the authors note were “unbalanced towards one of the two classes” in the per-language baseline and CNN models ([Vásquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)).

It is also worth emphasizing what the study is not: despite the third-party note’s claim of an Italian dataset, there is no Italian speech data anywhere in the primary source ([Vásquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374); [Third-party research note, n.d.](document_2.txt)). Any downstream analysis that relied on the note would therefore mischaracterize the study’s language coverage and its transfer learning topology.

## Conclusion

In answer to the question “What datasets are used?”, the primary source establishes that the study employs three language-specific speech datasets consisting of PD patients and healthy controls: (1) the **PC-GITA corpus** for Colombian Spanish, comprising 50 PD and 50 HC speakers; (2) a **German dataset** of 88 PD and 88 HC speakers from Germany; and (3) a **Czech dataset** of 50 PD and 50 HC native Czech speakers ([Vásquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)). All three datasets include diadochokinetic syllable repetition, read text, and monologue tasks, were recorded under noise-controlled conditions at 16 kHz, and were clinically rated with the MDS-UPDRS-III ([Vásquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)). The third-party research note’s assertion of an Italian dataset is a factual error contradicted throughout the primary source, and should not be relied upon ([Third-party research note, n.d.](document_2.txt)). The dominant strengths of this data foundation are the inclusion of three typologically distinct languages, a common clinical rating instrument, and a transfer learning design explicitly tailored to linguistic heterogeneity; its principal limitations are uneven dataset sizes, unbalanced gender distributions in the German and Czech cohorts, differing task protocols, and a systematic severity gap favoring the Spanish data.

## References

Goetz, C. G., et al. (2008). Movement Disorder Society-sponsored revision of the Unified Parkinson’s Disease Rating Scale (MDS-UPDRS): Scale presentation and clinimetric testing results. *Movement Disorders, 23*(15), 2129–2170. [https://arxiv.org/abs/2002.04374](https://arxiv.org/abs/2002.04374)

Orozco-Arroyave, J. R., et al. (2014). New Spanish speech corpus database for the analysis of people suffering from Parkinson’s disease. In *Proceedings of the Ninth International Conference on Language Resources and Evaluation* (pp. 342–347). [https://arxiv.org/abs/2002.04374](https://arxiv.org/abs/2002.04374)

Rusz, J. (2018). *Detecting speech disorders in early Parkinson’s disease by acoustic analysis* [Habilitation thesis]. Czech Technical University in Prague. [https://arxiv.org/abs/2002.04374](https://arxiv.org/abs/2002.04374)

Skodda, S., Visser, W., & Schlegel, U. (2011). Vowel articulation in Parkinson’s disease. *Journal of Voice, 25*(4), 467–472. [https://arxiv.org/abs/2002.04374](https://arxiv.org/abs/2002.04374)

Third-party research note: Convolutional neural networks and a transfer learning strategy to classify Parkinson’s disease from speech in three different languages. (n.d.). [document_2.txt]. [Third-party research note](document_2.txt)

Vásquez-Correa, J. C., Arias-Vergara, T., Rios-Urrego, C. D., Schuster, M., Rusz, J., Orozco-Arroyave, J. R., & Nöth, E. (2020). *Convolutional neural networks and a transfer learning strategy to classify Parkinson’s disease from speech in three different languages* (arXiv:2002.04374). [https://arxiv.org/abs/2002.04374](https://arxiv.org/abs/2002.04374)