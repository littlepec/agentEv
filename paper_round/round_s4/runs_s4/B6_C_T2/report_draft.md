# Datasets Used in the Cross-Lingual Parkinson's Disease Speech Classification Study

## Introduction

The study under review investigates the automatic classification of Parkinson's disease (PD) from speech using convolutional neural networks (CNNs) trained on time–frequency representations, combined with a transfer learning strategy across languages ([document_1.txt](document_1.txt)). Because the central experimental design depends on comparing models trained and tested across different linguistic groups, the composition, provenance, and clinical annotation of the underlying speech corpora are decisive for interpreting the reported results. This report identifies and describes every dataset employed, the collection and preprocessing procedures applied to them, the manner in which they were used in the experiments, and an assessment of the strengths and limitations of the data resources. Where the provided source material is incomplete or truncated, this is stated explicitly rather than inferred ([document_1.txt](document_1.txt); [document_2.txt](document_2.txt)).

## Primary Datasets Used in the Study

Three speech datasets, corresponding to three languages — Spanish, German, and Czech — constitute the primary data resource for the study ([document_1.txt](document_1.txt)). All recordings were captured under noise-controlled conditions and down-sampled to 16 kHz ([document_1.txt](document_1.txt)). The patients in all three datasets were evaluated by an expert neurologist according to the third section of the Movement Disorder Society–Unified Parkinson's Disease Rating Scale (MDS-UPDRS-III) ([document_1.txt](document_1.txt)). A summary of the speaker composition is provided in Table 1.

### The Spanish Dataset: PC-GITA Corpus

The Spanish portion of the data is drawn from the PC-GITA corpus, a Spanish speech corpus created for the analysis of people suffering from Parkinson's disease ([document_1.txt](document_1.txt); [document_2.txt](document_2.txt)). PC-GITA contains utterances from 50 PD patients and 50 healthy control (HC) subjects, all native Colombian Spanish speakers ([document_2.txt](document_2.txt); [document_1.txt](document_1.txt)). The speaker composition of the Spanish dataset is therefore exactly 50 PD patients and 50 healthy controls, yielding a perfectly balanced 1:1 clinical ratio across 100 speakers ([document_2.txt](document_2.txt)). This corpus supplies the Spanish portion of the cross-lingual speech data and has been widely used in prior PD speech research; for example, earlier work reported accuracies of up to 77% on PC-GITA utterances using energy- and entropy-based features computed from time–frequency representations ([document_1.txt](document_1.txt)).

### The German Dataset

The German dataset contains speech recordings of 88 PD patients and 88 HC speakers from Germany ([document_2.txt](document_2.txt)). With 176 speakers in total, it is the largest of the three language-specific datasets in terms of participant count, and it is likewise clinically balanced at a 1:1 ratio ([document_2.txt](document_2.txt)). The German data supply speech recordings of Parkinson's disease patients and healthy controls for the second language evaluated ([document_2.txt](document_2.txt)). No further corpus-level designation (comparable to "PC-GITA" for Spanish) is given for the German recordings in the provided material ([document_1.txt](document_1.txt); [document_2.txt](document_2.txt)).

### The Czech Dataset

The Czech dataset comprises a total of 100 native Czech speakers, consisting of 50 PD patients and 50 healthy controls ([document_1.txt](document_1.txt); [document_2.txt](document_2.txt)). The speech tasks performed by the Czech participants include the rapid repetition of the syllables /pa-ta-ka/, a read text of 80 words, and a monologue ([document_1.txt](document_1.txt)). The Czech recordings are associated with reference [19], identified as J. Rusz's habilitation thesis on detecting speech disorders in early Parkinson's disease by acoustic analysis ([document_1.txt](document_1.txt)).

### Comparative Summary of Primary Datasets

**Table 1.** Speaker composition of the three primary datasets used in the study.

| Language | Corpus / Source | PD Patients | Healthy Controls | Total Speakers | Native Speaker Group |
|---|---|---|---|---|---|
| Spanish | PC-GITA | 50 | 50 | 100 | Colombian Spanish |
| German | German speech recordings | 88 | 88 | 176 | German |
| Czech | Czech speech recordings (Rusz) | 50 | 50 | 100 | Czech |
| **Total** | — | **188** | **188** | **376** | — |

The combined resource thus comprises 376 speakers across three languages, of whom 188 are PD patients and 188 are healthy controls ([document_2.txt](document_2.txt); [document_1.txt](document_1.txt)). The balanced design at the aggregate level is notable because it minimizes systematic bias in the accuracy, sensitivity, and specificity metrics reported for each language ([document_1.txt](document_1.txt)).

## Data Collection and Preprocessing Methodology

### Recording Conditions

All recordings across the three datasets were captured in noise-controlled conditions and subsequently down-sampled to 16 kHz ([document_1.txt](document_1.txt)). The source material does not specify recording hardware, room acoustics, or signal-to-noise ratios, which limits full reproducibility of the acquisition protocol ([document_1.txt](document_1.txt)).

### Clinical Evaluation

Patients in all three datasets were assessed by an expert neurologist using MDS-UPDRS-III ([document_1.txt](document_1.txt); [document_2.txt](document_2.txt)). Table 1 of the study is described as summarizing information about the patients and healthy speakers, including subjects, gender (male or female), and time after diagnosis in years ([document_1.txt](document_1.txt)). However, the specific tabulated values were truncated in the available source excerpt, so the individual demographic and clinical figures cannot be reproduced here ([document_1.txt](document_1.txt)).

### Segmentation

Speech signals were analyzed on the basis of automatic detection of onset and offset transitions, which model the difficulties patients experience in starting and stopping the movement of the vocal folds ([document_1.txt](document_1.txt)). Transition detection relied on the presence of the fundamental frequency of speech in short-time frames ([document_1.txt](document_1.txt)). The border between voiced and unvoiced frames was identified, and 80 ms of signal were taken to the left and right, forming segments of 160 ms in length ([document_1.txt](document_1.txt)).

### Time–Frequency Representation

Time–frequency representations based on the short-time Fourier transform (STFT) served as CNN input ([document_1.txt](document_1.txt)). The STFT with 256 frequency bins was computed for each segmented transition, using a window length of 16 ms and a step size of 4 ms, producing 41 time frames per transition ([document_1.txt](document_1.txt)). The resulting spectrogram was transformed to the Mel scale with 80 filters, forming an 80 × 41 spectrogram used to train the CNNs ([document_1.txt](document_1.txt)).

## Speech Tasks and Linguistic Considerations

All speech exercises performed by participants were considered for the classification strategy, and the final decision for each speaker was obtained by a majority voting strategy across the different speech exercises ([document_1.txt](document_1.txt)). The Czech dataset's tasks — /pa-ta-ka/ repetitions, an 80-word read text, and a monologue — are explicitly enumerated, whereas the corresponding task inventories for the Spanish and German datasets are not itemized in the provided material ([document_1.txt](document_1.txt)).

The study explicitly acknowledges that classification across languages must be conducted carefully to avoid bias toward linguistic content ([document_1.txt](document_1.txt)). Czech and German are described as richer than Spanish in consonant production, which may make consonant sounds easier for Czech PD patients to produce than for Spanish PD patients ([document_1.txt](document_1.txt)). This linguistic asymmetry is precisely the phenomenon that motivates the cross-lingual transfer learning design ([document_1.txt](document_1.txt)).

## Datasets Referenced in Related Work (Not Used in the Present Experiments)

The literature review cites additional datasets that informed the study but were not part of its experiments:

1. **Turkish PD/HC speech data (Sakar et al.).** Reference [4] concerns the collection and analysis of a Parkinson speech dataset with multiple types of sound recordings ([document_1.txt](document_1.txt)). Prior work using this data computed features related to perturbations of the fundamental frequency and amplitude to classify utterances from 20 PD patients and 20 HC subjects, Turkish speakers, reporting accuracies of up to 75% with KNN and SVM classifiers ([document_1.txt](document_1.txt)).
2. **PC-GITA in earlier work.** Reference [5] employed a phonation analysis based on several time–frequency representations to assess tremor in PD speech, reporting accuracies of up to 77% on utterances of the PC-GITA database ([document_1.txt](document_1.txt)). This is the same corpus that supplies the Spanish data in the present study ([document_1.txt](document_1.txt)).

A deep learning articulation model [12] also used speech recordings of PD patients and HC speakers in Spanish, German, and Czech, reporting accuracies ranging from 70% to 89% depending on the language; however, in a language-independent setting the results were unsatisfactory, with accuracy below 60% ([document_1.txt](document_1.txt)).

**Table 2.** Datasets identified in the source material and their role.

| Dataset | Language(s) | PD / HC Counts | Role in the Study |
|---|---|---|---|
| PC-GITA | Colombian Spanish | 50 / 50 | Primary (Spanish) |
| German speech recordings | German | 88 / 88 | Primary (German) |
| Czech speech recordings | Czech | 50 / 50 | Primary (Czech) |
| Sakar et al. Parkinson speech dataset | Turkish | 20 / 20 | Referenced only (prior work) |

## Use of the Datasets in Experiments and Results

The experiments were divided into two stages: first, baseline and CNN models were trained considering each language individually; then, the trained CNNs for each language were used as base models in a transfer learning strategy to improve accuracy in the other two languages ([document_1.txt](document_1.txt)).

### Monolingual Baseline and CNN Results

**Table 3.** Baseline and CNN results per language (standard deviations in parentheses) ([document_1.txt](document_1.txt)).

| Language | Model | Acc (%) | Sen (%) | Spe (%) | MCC |
|---|---|---|---|---|---|
| Spanish | Baseline | 73.7 (13.0) | 74.5 (16.7) | 77.1 (16.2) | 0.50 |
| Spanish | CNN | 71.0 (15.9) | 74.0 (25.0) | 68.0 (28.6) | 0.42 |
| German | Baseline | 69.3 (9.9) | 71.8 (12.4) | 68.7 (10.0) | 0.39 |
| German | CNN | 63.1 (11.7) | 43.1 (38.0) | 83.1 (17.7) | 0.30 |
| Czech | Baseline | 61.0 (12.5) | 64.5 (19.5) | 60.2 (11.9) | 0.27 |
| Czech | CNN | 68.5 (14.1) | 94.0 (13.5) | 42.0 (33.2) | 0.43 |

The highest monolingual accuracy was obtained for Spanish, while German's best result came from the baseline rather than the CNN, and Czech's best result came from the CNN ([document_1.txt](document_1.txt)). For all three languages, the results were unbalanced toward one of the two classes according to specificity and sensitivity ([document_1.txt](document_1.txt)).

### Cross-Lingual Transfer Learning Results

**Table 4.** Transfer learning results using CNNs across languages ([document_1.txt](document_1.txt)).

| Base Language | Target Language | Acc (%) | Sen (%) | Spe (%) | MCC |
|---|---|---|---|---|---|
| German | Spanish | 70.0 (12.5) | 62.0 (19.9) | 78.0 (23.9) | 0.41 |
| Czech | Spanish | 72.0 (13.1) | 67.0 (11.6) | 78.0 (23.9) | 0.46 |
| Spanish | German | 77.3 (11.3) | 86.2 (13.8) | 68.3 (14.3) | 0.57 |
| Czech | German | 76.7 (7.9) | 87.5 (11.0) | 66.0 (15.6) | 0.55 |
| Spanish | Czech | 72.6 (13.9) | 82.0 (14.8) | 62.0 (28.9) | 0.46 |
| German | Czech | 70.7 (14.5) | 80.0 (16.3) | 62.5 (26.3) | 0.38 |

The transfer learning scheme improved model accuracy by up to 8% when the base model used to initialize the classifier weights was sufficiently robust ([document_1.txt](document_1.txt)). The gains were observed when the model trained on Spanish utterances was used to initialize models for German and Czech, and transfer-learned models were generally more balanced in specificity–sensitivity and exhibited lower variance than models trained without transfer learning ([document_1.txt](document_1.txt)).

## Assessment of the Datasets: Strengths and Limitations

Based on the provided information, the dataset design has clear strengths. The three corpora are balanced within each language, with equal numbers of PD patients and healthy controls in every case ([document_2.txt](document_2.txt)). Clinical ground truth is anchored in a standardized instrument (MDS-UPDRS-III) administered by an expert neurologist ([document_1.txt](document_1.txt)), and the acoustic recordings are controlled for noise and normalized to a common 16 kHz sampling rate ([document_1.txt](document_1.txt)), supporting comparability across languages.

At the same time, several limitations are evident. First, the sample sizes are modest for deep learning — 100, 176, and 100 speakers respectively ([document_2.txt](document_2.txt)) — and the reported standard deviations are large, in several cases exceeding 20 percentage points for specificity or sensitivity (e.g., Spanish CNN specificity 68.0 ± 28.6; Czech CNN specificity 42.0 ± 33.2) ([document_1.txt](document_1.txt)). Second, the class decisions for each speaker rely on majority voting over heterogeneous speech tasks ([document_1.txt](document_1.txt)); because the task inventory is documented only for Czech ([document_1.txt](document_1.txt)), cross-language task differences are a plausible confound that cannot be fully disentangled from language effects. Third, the linguistic asymmetry acknowledged by the authors — richer consonant inventories in Czech and German versus Spanish ([document_1.txt](document_1.txt)) — suggests that apparent "language" effects may partly reflect phonological rather than pathological variation. Fourth, no acquisition hardware or signal-to-noise specifications are disclosed ([document_1.txt](document_1.txt)), which restricts reproducibility. In my assessment, the study's transfer learning conclusion — that cross-lingual initialization improves performance only when the base model is robust enough ([document_1.txt](document_1.txt)) — is plausible given the data, but its generalizability is constrained by the small number of languages (three) and the single base-model source (Spanish) that produced the gains ([document_1.txt](document_1.txt)).

## Conclusion

The study draws on three primary speech datasets spanning Spanish, German, and Czech: the PC-GITA corpus (50 PD patients and 50 healthy controls, Colombian Spanish speakers), German speech recordings (88 PD patients and 88 healthy controls), and Czech speech recordings (50 PD patients and 50 healthy controls) — a combined 376 speakers, evenly divided between 188 PD patients and 188 healthy controls ([document_2.txt](document_2.txt); [document_1.txt](document_1.txt)). All recordings were collected under noise-controlled conditions, down-sampled to 16 kHz, and clinically annotated with MDS-UPDRS-III ([document_1.txt](document_1.txt)). Additional datasets — the Turkish Parkinson speech dataset of Sakar et al. (20 PD, 20 HC) and PC-GITA as used in earlier phonation research — appear only in the literature review and were not part of the present experiments ([document_1.txt](document_1.txt)). Future work is planned to train base models using two languages rather than one, to apply hyper-parameter optimization, and to extend transfer learning across diseases such as Huntington's disease ([document_1.txt](document_1.txt)).

## References

document_1.txt. (n.d.). *Convolutional neural networks and a transfer learning strategy to classify Parkinson's disease from speech in three different languages* [Manuscript source document]. Retrieved September 15, 2026, from document_1.txt

document_2.txt. (n.d.). *Third-party research note: Convolutional neural networks and a transfer learning strategy to classify Parkinson's disease from speech in three different languages* [Research note source document]. Retrieved September 15, 2026, from document_2.txt