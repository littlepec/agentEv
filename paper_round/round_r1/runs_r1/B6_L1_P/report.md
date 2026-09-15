# Datasets Used in Cross-Lingual Parkinson's Disease Speech Classification: A Detailed Report

## Introduction and Scope

The query concerns the datasets employed in the study "Convolutional Neural Networks and a Transfer Learning Strategy to Classify Parkinson's Disease from Speech in Three Different Languages" (Vásquez-Correa et al., 2020). This investigation addresses a specific and practically important problem: whether a convolutional neural network (CNN) trained to separate Parkinson's disease (PD) patients from healthy control (HC) speakers in one language can be repurposed, through transfer learning, to classify speakers in a different language (Vásquez-Correa et al., 2020). Because the central scientific claim depends on cross-linguistic generalization, the composition, provenance, and clinical characterization of the underlying speech datasets are not incidental background but the linchpin of the study's validity. This report catalogues the three primary datasets used in the study, describes their demographic and clinical profiles, details the speech tasks and signal-processing pipeline applied to them, compares them systematically, and evaluates the reliability of the reported figures—including one notable discrepancy between the primary source and a third-party research note.

## The Three Primary Datasets

The study draws on speech recordings from patients and healthy speakers in three languages: **Spanish, German, and Czech** (Vásquez-Correa et al., 2020). All recordings were captured under noise-controlled conditions, and all speech signals were down-sampled to 16 kHz (Vásquez-Correa et al., 2020). The patients across the three datasets were evaluated by an expert neurologist using the third section of the Movement Disorder Society–sponsored revision of the Unified Parkinson's Disease Rating Scale (MDS-UPDRS-III), which provides a standardized index of motor symptom severity (Vásquez-Correa et al., 2020).

### The Spanish Dataset: PC-GITA Corpus

The Spanish portion of the data derives from the **PC-GITA corpus**, which contains utterances from 50 PD patients and 50 healthy controls, all native speakers of Colombian Spanish (Vásquez-Correa et al., 2020). This yields a perfectly balanced Spanish dataset of 100 speakers in total (Vásquez-Correa et al., 2020). The corpus was originally introduced by Orozco-Arroyave and colleagues at the Ninth International Conference on Language Resources and Evaluation (Vásquez-Correa et al., 2020).

Two features of the Spanish dataset are especially consequential for the study's findings. First, **all Spanish patients were recorded in the ON state**—that is, under the effect of their daily dopaminergic medication (Vásquez-Correa et al., 2020). Second, the Spanish cohort exhibits the **highest average disease severity** among the three datasets, with mean MDS-UPDRS-III scores of 37.8 (SD = 22.1) for men and 37.6 (SD = 14.1) for women (Vásquez-Correa et al., 2020). The authors explicitly attribute the superior classification accuracy observed for Spanish to this higher disease severity, which increases the acoustic separability between patients and controls (Vásquez-Correa et al., 2020). Time since diagnosis averaged 8.7 years (SD = 5.9) for men and 12.6 years (SD = 11.6) for women (Vásquez-Correa et al., 2020).

The gender composition of the Spanish subset is exactly balanced: 25 male PD patients, 25 female PD patients, 25 male controls, and 25 female controls (Vásquez-Correa et al., 2020). Ages ranged from 33–81 years for male patients, 31–86 years for male controls, 49–75 years for female patients, and 49–76 years for female controls, with mean ages of 61.3 (SD = 11.4) and 60.5 (SD = 11.6) for male patients and controls respectively, and 60.7 (SD = 7.3) and 61.4 (SD = 7.0) for female patients and controls (Vásquez-Correa et al., 2020).

### The German Dataset

The German data consist of recordings from Germany described in the source paper as comprising **88 PD patients and 88 HC speakers**, giving a total of 176 participants—the largest of the three datasets (Vásquez-Correa et al., 2020). The German recordings were originally reported by Skodda, Visser, and Schlegel in the *Journal of Voice* (Vásquez-Correa et al., 2020).

The German cohort is somewhat older than the Spanish cohort. Mean ages were 66.7 years (SD = 8.7) for male patients versus 63.8 years (SD = 12.7) for male controls, and 66.2 years (SD = 9.7) for female patients versus 62.6 years (SD = 15.2) for female controls (Vásquez-Correa et al., 2020). Age ranges spanned 44–82 years for male patients, 26–83 for male controls, 42–84 for female patients, and 28–85 for female controls (Vásquez-Correa et al., 2020).

Crucially, the German patients exhibit **markedly milder disease severity** than the Spanish patients. Mean MDS-UPDRS-III scores were 22.1 (SD = 9.9) for men and 23.3 (SD = 12.0) for women (Vásquez-Correa et al., 2020). Time since diagnosis averaged 7.0 years (SD = 5.5) for men and 7.1 years (SD = 6.2) for women (Vásquez-Correa et al., 2020). Gender distribution was 47 male and 41 female PD patients, and 44 male and 44 female controls (Vásquez-Correa et al., 2020).

### The Czech Dataset

The Czech data comprise a total of **100 native Czech speakers, equally divided into 50 PD patients and 50 healthy controls** (Vásquez-Correa et al., 2020). These recordings were sourced from the habilitation thesis of Rusz at the Czech Technical University in Prague (Vásquez-Correa et al., 2020).

The Czech cohort shows the **lowest average disease severity** of the three groups, with mean MDS-UPDRS-III scores of 21.4 (SD = 11.5) for men and 18.1 (SD = 9.7) for women (Vásquez-Correa et al., 2020), and the shortest mean time since diagnosis: 6.7 years (SD = 4.5) for men and 6.8 years (SD = 5.2) for women (Vásquez-Correa et al., 2020). Gender composition was 30 male and 20 female PD patients, with an identical 30 male and 20 female control group (Vásquez-Correa et al., 2020). Mean ages were 65.3 years (SD = 9.6) for male patients, 60.3 years (SD = 11.5) for male controls, 60.1 years (SD = 8.7) for female patients, and 63.5 years (SD = 11.1) for female controls (Vásquez-Correa et al., 2020).

## Comparative Summary of the Datasets

**Table 1. Overview of the three primary speech datasets.**

| Language | Corpus / Source | PD patients | Healthy controls | Total speakers | Speaker origin |
|---|---|---|---|---|---|
| Spanish | PC-GITA (Orozco-Arroyave et al., 2014) | 50 | 50 | 100 | Colombian Spanish natives |
| German | Skodda et al. (2011) | 88 | 88 | 176 | German speakers |
| Czech | Rusz (2018) | 50 | 50 | 100 | Czech natives |

*Source: Vásquez-Correa et al. (2020).*

**Table 2. Gender composition and clinical profile by dataset and group.**

| Dataset | Group | Male (n) | Female (n) | MDS-UPDRS-III, M (SD) | MDS-UPDRS-III, F (SD) | Time since diagnosis, M (SD) | Time since diagnosis, F (SD) |
|---|---|---|---|---|---|---|---|
| Spanish | PD | 25 | 25 | 37.8 (22.1) | 37.6 (14.1) | 8.7 (5.9) yrs | 12.6 (11.6) yrs |
| Spanish | HC | 25 | 25 | — | — | — | — |
| German | PD | 47 | 41 | 22.1 (9.9) | 23.3 (12.0) | 7.0 (5.5) yrs | 7.1 (6.2) yrs |
| German | HC | 44 | 44 | — | — | — | — |
| Czech | PD | 30 | 20 | 21.4 (11.5) | 18.1 (9.7) | 6.7 (4.5) yrs | 6.8 (5.2) yrs |
| Czech | HC | 30 | 20 | — | — | — | — |

*Source: Vásquez-Correa et al. (2020).*

**Table 3. Speech tasks performed by participants in each dataset.**

| Dataset | Speech tasks |
|---|---|
| Spanish | 10 sentences; rapid repetition of /pa-ta-ka/, /pe-ta-ka/, /pa-ka-ta/, /pa/, /ta/, /ka/; one text of 36 words; a monologue |
| German | Rapid repetition of /pa-ta-ka/; 5 sentences; one text of 81 words; a monologue |
| Czech | Rapid repetition of /pa-ta-ka/; a read text of 80 words; a monologue |

*Source: Vásquez-Correa et al. (2020).*

The three datasets therefore share a **common core task battery**—rapid syllable repetition, read material, and spontaneous or semi-spontaneous monologue—which is essential for the cross-linguistic transfer design, since it permits a consistent alignment of acoustic analyses across languages (Vásquez-Correa et al., 2020). The Spanish protocol is the most extensive, incorporating six distinct rapid-repetition variants in addition to sentences and read text (Vásquez-Correa et al., 2020).

## How the Datasets Were Processed for Modelling

The datasets were not used in raw form. The researchers applied a segmentation procedure that isolates **transitions between voiced and unvoiced segments**, on the rationale that such transitions model the patients' difficulty in starting and stopping vocal fold vibration (Vásquez-Correa et al., 2020). Detection of these transitions relied on the presence of the fundamental frequency in short-time frames; 80 ms of signal were extracted on each side of the voiced/unvoiced boundary to produce 160 ms segments (Vásquez-Correa et al., 2020).

Two modelling streams were then applied. For the baseline, 12 Mel-Frequency Cepstral Coefficients with their first and second derivatives, plus log energy distributed across 22 Bark bands, yielded 58 descriptors; four statistical functionals (mean, standard deviation, skewness, kurtosis) expanded each utterance to a 232-dimensional feature vector, classified with a radial-basis SVM (C = 10, γ = 0.0001) under speaker-independent 10-fold cross-validation (Vásquez-Correa et al., 2020). For the deep learning stream, short-time Fourier transforms with 256 frequency bins, a 16 ms window, and a 4 ms step generated 41 time frames per transition, converted into Mel-scale spectrograms of size 80 × 41 using 80 filters (Vásquez-Correa et al., 2020).

## Performance Achieved on Each Dataset

The datasets yielded different levels of baseline separability. In individual-language experiments, the baseline SVM achieved 73.7% accuracy on Spanish, 69.3% on German, and 61.0% on Czech, while the CNN achieved 71.0%, 63.1%, and 68.5% respectively (Vásquez-Correa et al., 2020). Spanish thus produced the highest accuracy overall, which the authors attribute to its higher disease severity (Vásquez-Correa et al., 2020).

**Table 4. Accuracy (%) for baseline and CNN models trained per language.**

| Language | Baseline accuracy | CNN accuracy |
|---|---|---|
| Spanish | 73.7 (13.0) | 71.0 (15.9) |
| German | 69.3 (9.9) | 63.1 (11.7) |
| Czech | 61.0 (12.5) | 68.5 (14.1) |

*Source: Vásquez-Correa et al. (2020).*

In the transfer learning experiments, using Spanish as the base language improved accuracy on German to 77.3% (an improvement exceeding 8% over baseline) and on Czech to 76.7% (Vásquez-Correa et al., 2020). Using Czech as the base for German produced 70.7%, and using German as the base for Czech produced 72.0% (Vásquez-Correa et al., 2020). The authors conclude that transfer learning helped only when the base model was sufficiently robust—observed specifically when the Spanish-trained model initialized models for German and Czech (Vásquez-Correa et al., 2020).

**Table 5. Transfer learning results by base and target language.**

| Base language | Target language | Accuracy (%) | MCC |
|---|---|---|---|
| German | Spanish | 70.0 (12.5) | 0.41 |
| German | Czech | 72.0 (13.1) | 0.46 |
| Spanish | German | 77.3 (11.3) | 0.57 |
| Spanish | Czech | 76.7 (7.9) | 0.55 |
| Czech | Spanish | 72.6 (13.9) | 0.46 |
| Czech | German | 70.7 (14.5) | 0.38 |

*Source: Vásquez-Correa et al. (2020).*

## Additional Speech Datasets Referenced in the Study

Although the empirical work rests on the three corpora above, the paper's literature review cites several other speech datasets that contextualize the approach. These include a **Turkish Parkinson speech dataset** with multiple types of sound recordings from 20 PD patients and 20 HC subjects, used to report accuracies up to 75% (Vásquez-Correa et al., 2020). The PC-GITA corpus recurs in prior work, including a phonation analysis of energy and entropy features that reached up to 77% accuracy (Vásquez-Correa et al., 2020). A Czech dataset involving rapid repetition of /pa-ta-ka/ by 24 Czech native speakers supported an articulation study reporting 88% accuracy (Vásquez-Correa et al., 2020). The Czech data described by Rusz and colleagues (2013) also supported a forced-Gaussian methodology reaching up to 94% accuracy on Czech data and 81% on Spanish data (Vásquez-Correa et al., 2020).

## Reliability Assessment and a Critical Discrepancy

An impartial evaluation requires attention to one material inconsistency in the provided sources. The third-party research note states that "the German data consist of speech recordings of 44 PD patients and 44 HC speakers" (Third-party research note, n.d.). This conflicts with the primary source, which reports **88 PD patients and 88 HC speakers from Germany**, a figure corroborated by Table 1 of the primary paper, where male (47) and female (41) German PD counts sum to 88, and male (44) and female (44) German control counts sum to 88 (Vásquez-Correa et al., 2020). The note's figure of 44 + 44 appears to conflate the **control-group gender split** (44 male HC, 44 female HC) with the total speaker count. Given the principle of prioritizing the original, primary report, the correct German composition should be treated as 88 PD and 88 HC. The note is accurate, however, regarding the Spanish and Czech compositions (Third-party research note, n.d.).

A second consideration is that, while the three datasets are balanced in overall PD/HC ratios, the German cohort is nearly twice the size of the Spanish and Czech cohorts (Vásquez-Correa et al., 2020), which may influence the stability of transfer learning results. Furthermore, all Spanish patients were medicated (ON state) at the time of recording (Vásquez-Correa et al., 2020), a factor that limits comparability across datasets if medication status differed elsewhere.

## Conclusion

The study employs three primary speech datasets spanning three languages: the **PC-GITA corpus** for Colombian Spanish (50 PD, 50 HC), a **German dataset** (88 PD, 88 HC), and a **Czech dataset** (50 PD, 50 HC), all recorded under noise-controlled conditions and down-sampled to 16 kHz (Vásquez-Correa et al., 2020). Their value for the research question lies in their shared task battery and their common clinical annotation via MDS-UPDRS-III, while their differing disease-severity profiles—highest in Spanish, lower in German and Czech—explain much of the observed cross-linguistic performance variation (Vásquez-Correa et al., 2020). In my assessment, the dataset portfolio is well suited to the cross-lingual transfer question because it combines balanced case-control designs with genuinely distinct languages; however, readers should rely on the primary source for the German speaker counts, as the third-party note understates them (Third-party research note, n.d.; Vásquez-Correa et al., 2020). Future work outlined by the authors includes developing more robust base models via Bayesian hyper-parameter optimization, training base models on two languages rather than one, staging patients by MDS-UPDRS-III or dysarthria severity, and extending transfer learning to other neurological conditions such as Huntington's disease (Vásquez-Correa et al., 2020).

## References

Third-party research note on convolutional neural networks and a transfer learning strategy to classify Parkinson's disease from speech in three different languages [Research note]. (n.d.). [document_2.txt](document_2.txt).

Vásquez-Correa, J. C., Arias-Vergara, T., Rios-Urrego, C. D., Schuster, M., Rusz, J., Orozco-Arroyave, J. R., & Nöth, E. (2020). *Convolutional neural networks and a transfer learning strategy to classify Parkinson's disease from speech in three different languages* [Preprint]. arXiv. [document_1.txt](https://arxiv.org/abs/2002.04374)