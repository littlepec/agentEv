# Datasets Used in the Cross-Lingual Parkinson's Disease Speech Classification Study

## Introduction

The study investigates automatic classification of Parkinson's disease (PD) from speech using convolutional neural networks (CNNs) trained on time–frequency representations, combined with transfer learning across languages ([document_1.txt](document_1.txt)). The central experimental design compares models trained and tested across Spanish, German, and Czech linguistic groups. This report identifies the datasets used, their collection and preprocessing, their role in the experiments, and strengths and limitations. The primary source is document_1.txt; document_2.txt is a secondary reading note.

## Primary Datasets Used in the Study

Three speech datasets, corresponding to three languages — Spanish, German, and Czech — constitute the primary data resource ([document_1.txt](document_1.txt)). All recordings were captured under noise-controlled conditions and down-sampled to 16 kHz ([document_1.txt](document_1.txt)). Patients in all three datasets were evaluated by an expert neurologist according to the third section of the Movement Disorder Society–Unified Parkinson's Disease Rating Scale (MDS-UPDRS-III) ([document_1.txt](document_1.txt)).

### The Spanish Dataset: PC-GITA Corpus

The Spanish data are drawn from the PC-GITA corpus ([document_1.txt](document_1.txt)). PC-GITA contains utterances from 50 PD patients and 50 healthy control (HC) subjects, all native Colombian Spanish speakers ([document_1.txt](document_1.txt)). The Spanish participants were asked to pronounce 10 sentences; the rapid repetition of /pa-ta-ka/, /pe-ta-ka/, /pa-ka-ta/, /pa/, /ta/, and /ka/; one text with 36 words; and a monologue ([document_1.txt](document_1.txt)). All patients were in ON state at the time of recording ([document_1.txt](document_1.txt)). Earlier work cited in the paper reported accuracies of up to 77% on PC-GITA utterances using energy- and entropy-based features from time–frequency representations ([document_1.txt](document_1.txt)).

### The German Dataset

The German dataset contains speech recordings of 88 PD patients and 88 HC speakers from Germany ([document_1.txt](document_1.txt)). The German participants performed four speech tasks: rapid repetition of /pa-ta-ka/, 5 sentences, one text with 81 words, and a monologue ([document_1.txt](document_1.txt)). No corpus-level designation comparable to “PC-GITA” is given for the German recordings in the primary source; they are associated with reference [18] ([document_1.txt](document_1.txt)).

### The Czech Dataset

The Czech dataset comprises 100 native Czech speakers: 50 PD patients and 50 healthy controls ([document_1.txt](document_1.txt)). The Czech speech tasks include rapid repetition of the syllables /pa-ta-ka/, a read text with 80 words, and a monologue ([document_1.txt](document_1.txt)). The Czech recordings are associated with reference [19], identified as J. Rusz's habilitation thesis on detecting speech disorders in early Parkinson's disease by acoustic analysis ([document_1.txt](document_1.txt)).

### Comparative Summary of Primary Datasets

**Table 1.** Speaker composition of the three primary datasets.

| Language | Corpus / Source | PD Patients | Healthy Controls | Total Speakers | Native Speaker Group |
|---|---|---|---|---|---|
| Spanish | PC-GITA | 50 | 50 | 100 | Colombian Spanish |
| German | German speech recordings | 88 | 88 | 176 | German |
| Czech | Czech speech recordings (Rusz) | 50 | 50 | 100 | Czech |
| **Total** | — | **188** | **188** | **376** | — |

The combined resource thus comprises 376 speakers across three languages, of whom 188 are PD patients and 188 are healthy controls ([document_1.txt](document_1.txt)).

## Data Collection and Preprocessing Methodology

### Recording Conditions

All recordings across the three datasets were captured in noise-controlled conditions and down-sampled to 16 kHz ([document_1.txt](document_1.txt)). The primary source does not specify recording hardware, room acoustics, or signal-to-noise ratios ([document_1.txt](document_1.txt)).

### Clinical Evaluation

Patients in all three datasets were assessed by an expert neurologist using MDS-UPDRS-III ([document_1.txt](document_1.txt)). The primary source's Table 1 provides demographic and clinical details, including gender counts, age ranges and means, time after diagnosis, and MDS-UPDRS-III scores for the PD and HC groups across languages ([document_1.txt](document_1.txt)). The draft's statement that these tabulated values were truncated is not supported by document_1.txt.

### Segmentation

Speech signals were analyzed based on automatic detection of onset and offset transitions, which model difficulties patients experience in starting and stopping vocal-fold movement ([document_1.txt](document_1.txt)). Transition detection relied on the presence of the fundamental frequency in short-time frames ([document_1.txt](document_1.txt)). The border between voiced and unvoiced frames was detected, and 80 ms of signal were taken to the left and right, forming segments of 160 ms ([document_1.txt](document_1.txt)).

### Time–Frequency Representation

Short-time Fourier transform (STFT) representations served as CNN input ([document_1.txt](document_1.txt)). The STFT with 256 frequency bins was computed for each segmented transition, using a window length of 16 ms and a step size of 4 ms, producing 41 time frames per transition ([document_1.txt](document_1.txt)). The spectrogram was transformed to the Mel scale with 80 filters, forming an 80 × 41 spectrogram used to train the CNNs ([document_1.txt](document_1.txt)).

## Speech Tasks and Linguistic Considerations

All speech exercises performed by participants were considered for the classification strategy, and the final decision for each speaker was obtained by majority voting across the different speech exercises ([document_1.txt](document_1.txt)). The primary source itemizes task inventories for all three datasets: Spanish (10 sentences; /pa-ta-ka/, /pe-ta-ka/, /pa-ka-ta/, /pa/, /ta/, /ka/; 36-word text; monologue), German (/pa-ta-ka/; 5 sentences; 81-word text; monologue), and Czech (/pa-ta-ka/; 80-word text; monologue) ([document_1.txt](document_1.txt)). The draft's claim that Spanish and German task inventories were not itemized is contradicted by document_1.txt.

The study acknowledges that classification across languages must be conducted carefully to avoid bias toward linguistic content ([document_1.txt](document_1.txt)). Czech and German are described as richer than Spanish in consonant production, which may make consonant sounds easier for Czech PD patients to produce than for Spanish PD patients ([document_1.txt](document_1.txt)).

## Datasets Referenced in Related Work (Not Used in Present Experiments)

The literature review cites additional datasets that informed the study but were not part of its experiments:

1. **Turkish PD/HC speech data (Sakar et al.).** Reference [4] concerns a Parkinson speech dataset with multiple sound recordings. Prior work using this data classified utterances from 20 PD patients and 20 HC subjects, Turkish speakers, reporting accuracies up to 75% with KNN and SVM classifiers ([document_1.txt](document_1.txt)).
2. **PC-GITA in earlier work.** Reference [5] used phonation analysis based on time–frequency representations to assess tremor in PD speech, reporting accuracies up to 77% on PC-GITA utterances ([document_1.txt](document_1.txt)). This is the same corpus that supplies the Spanish data in the present study ([document_1.txt](document_1.txt)).
3. **Deep learning articulation model [12].** This prior model used speech recordings of PD patients and HC speakers in Spanish, German, and Czech, reporting accuracies from 70% to 89% depending on language; in a language-independent setting, accuracy was below 60% ([document_1.txt](document_1.txt)).

**Table 2.** Datasets identified in the source material and their role.

| Dataset | Language(s) | PD / HC Counts | Role in the Study |
|---|---|---|---|
| PC-GITA | Colombian Spanish | 50 / 50 | Primary (Spanish) |
| German speech recordings | German | 88 / 88 | Primary (German) |
| Czech speech recordings | Czech | 50 / 50 | Primary (Czech) |
| Sakar et al. Parkinson speech dataset | Turkish | 20 / 20 | Referenced only (prior work) |

## Use of the Datasets in Experiments and Results

The experiments were divided into two stages: first, baseline and CNN models were trained for each language individually; then, the trained CNNs for each language were used as base models in a transfer learning strategy to improve accuracy in the other two languages ([document_1.txt](document_1.txt)).

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

The highest monolingual accuracy was obtained for Spanish; German's best result came from the baseline rather than the CNN, and Czech's best result came from the CNN ([document_1.txt](document_1.txt)). For all three languages, results were unbalanced toward one class according to specificity and sensitivity ([document_1.txt](document_1.txt)).

### Cross-Lingual Transfer Learning Results

**Table 4.** Transfer learning results using CNNs across languages ([document_1.txt](document_1.txt)). The draft's Table 4 misassigned several base/target pairs; corrected to the primary source's rows.

| Base Language | Target Language | Acc (%) | Sen (%) | Spe (%) | MCC |
|---|---|---|---|---|---|
| German | Spanish | 70.0 (12.5) | 62.0 (19.9) | 78.0 (23.9) | 0.41 |
| German | Czech | 72.0 (13.1) | 67.0 (11.6) | 78.0 (23.9) | 0.46 |
| Spanish | German | 77.3 (11.3) | 86.2 (13.8) | 68.3 (14.3) | 0.57 |
| Spanish | Czech | 76.7 (7.9) | 87.5 (11.0) | 66.0 (15.6) | 0.55 |
| Czech | Spanish | 72.6 (13.9) | 82.0 (14.8) | 62.0 (28.9) | 0.46 |
| Czech | German | 70.7 (14.5) | 80.0 (16.3) | 62.5 (26.3) | 0.38 |

The transfer learning scheme improved accuracy by up to 8% when the base model used to initialize the classifier weights was sufficiently robust ([document_1.txt](document_1.txt)). Reported gains were observed when the model trained on Spanish utterances was used to initialize models for German and Czech, and transfer-learned models were generally more balanced in specificity–sensitivity and exhibited lower variance than models trained without transfer learning ([document_1.txt](document_1.txt)).

## Assessment of the Datasets: Strengths and Limitations

Strengths: the three corpora are balanced within each language, with equal numbers of PD patients and healthy controls ([document_1.txt](document_1.txt)). Clinical ground truth is anchored in MDS-UPDRS-III administered by an expert neurologist ([document_1.txt](document_1.txt)), and recordings are noise-controlled and normalized to 16 kHz ([document_1.txt](document_1.txt)).

Limitations: sample sizes are modest for deep learning — 100, 176, and 100 speakers respectively ([document_1.txt](document_1.txt)) — and reported standard deviations are large, in some cases exceeding 20 percentage points for specificity or sensitivity (e.g., Spanish CNN specificity 68.0 ± 28.6; Czech CNN specificity 42.0 ± 33.2) ([document_1.txt](document_1.txt)). Speaker decisions rely on majority voting over heterogeneous speech tasks ([document_1.txt](document_1.txt)); task inventories are documented for all three languages, but cross-language task differences remain a plausible confound. The authors acknowledge richer consonant inventories in Czech and German versus Spanish ([document_1.txt](document_1.txt)). No acquisition hardware or signal-to-noise specifications are disclosed ([document_1.txt](document_1.txt)). The transfer-learning conclusion is constrained by the three-language design and the reported gains mainly from Spanish-base models ([document_1.txt](document_1.txt)).

## Conclusion

The study uses three primary speech datasets: PC-GITA (50 PD patients and 50 healthy controls, Colombian Spanish speakers), German speech recordings (88 PD patients and 88 healthy controls), and Czech speech recordings (50 PD patients and 50 healthy controls) — a combined 376 speakers, evenly divided between 188 PD patients and 188 healthy controls ([document_1.txt](document_1.txt)). All recordings were collected under noise-controlled conditions, down-sampled to 16 kHz, and clinically annotated with MDS-UPDRS-III ([document_1.txt](document_1.txt)). Additional datasets referenced in the literature review include the Turkish Parkinson speech dataset of Sakar et al. (20 PD, 20 HC); PC-GITA also appears in earlier phonation work, but it is the Spanish primary dataset in this study ([document_1.txt](document_1.txt)). Future work is planned to train base models using two languages rather than one, apply hyper-parameter optimization, and extend transfer learning across diseases such as Huntington's disease ([document_1.txt](document_1.txt)).

## References

document_1.txt. (n.d.). *Convolutional neural networks and a transfer learning strategy to classify Parkinson's disease from speech in three different languages* [Manuscript source document]. Retrieved September 15, 2026, from document_1.txt

document_2.txt. (n.d.). *Third-party research note: Convolutional neural networks and a transfer learning strategy to classify Parkinson's disease from speech in three different languages* [Research note source document]. Retrieved September 15, 2026, from document_2.txt