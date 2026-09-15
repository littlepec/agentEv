# Datasets Used to Classify Parkinson’s Disease from Speech in Three Languages

## Introduction

The study under examination introduces a methodology for classifying Parkinson’s disease (PD) from speech using convolutional neural networks (CNNs) trained on time–frequency representations, combined with a cross-lingual transfer learning strategy ([Vásquez-Correa et al., 2019](document_1.txt)). The empirical foundation of that methodology is a portfolio of three language-specific speech datasets — Spanish, German, and Czech — each containing recordings of PD patients and healthy control (HC) speakers, all captured in noise-controlled conditions and down-sampled to 16 kHz ([Vásquez-Correa et al., 2019](document_1.txt)). This report catalogues those datasets in detail: their provenance and sources, speaker composition, speech tasks, clinical annotations, the derived representations used as model input, their limitations, and their principal use cases.

## 1. Overview of the Dataset Portfolio

The three datasets constitute a balanced, binary-classified (PD vs. HC) speech corpus family spanning three languages ([Vásquez-Correa et al., 2019](document_1.txt); [Third-party research note, n.d.](document_2.txt)).

| Dataset (language) | Named corpus | PD speakers | HC speakers | Total | Source reference cited in the study |
|---|---|---|---|---|---|
| Spanish | PC-GITA | 50 | 50 | 100 | Orozco-Arroyave et al. (2014), LREC, pp. 342–347 |
| German | Not named in the study | 88 | 88 | 176 | Skodda, Visser, & Schlegel (2011), *Journal of Voice*, 25(4), 467–472 |
| Czech | Not named in the study | 50 | 50 | 100 | Rusz (2018), habilitation thesis, Czech Technical University in Prague |

**Important discrepancy.** The primary study text states that “speech recordings of 88 PD patients and 88 HC speakers from Germany are considered” ([Vásquez-Correa et al., 2019](document_1.txt)), whereas the accompanying third-party research note reports the German composition as “44 PD patients and 44 HC speakers” ([Third-party research note, n.d.](document_2.txt)). These two figures cannot both be correct, and the transcription of the study’s Table 1 is partially garbled. My assessment is that the primary source figure (88 PD / 88 HC) should be treated as provisional rather than definitive, and that the German sample size is the single least reliable figure in the whole dataset description. This is a genuine reproducibility weakness, not a trivial matter of transcription.

## 2. The Spanish Dataset: PC-GITA

### 2.1 Provenance and speaker composition

The Spanish portion of the data is drawn from the PC-GITA corpus ([Vásquez-Correa et al., 2019](document_1.txt)). PC-GITA “contains utterances from 50 PD patients and 50 HC, Colombian Spanish native speakers,” giving a Spanish dataset of 100 speakers in total, with an exactly balanced class distribution ([Third-party research note, n.d.](document_2.txt)). The same composition is reported in the primary source ([Vásquez-Correa et al., 2019](document_1.txt)).

### 2.2 Speech tasks

Spanish participants were asked to pronounce ten sentences; to rapidly repeat the syllables /pa-ta-ka/, /pe-ta-ka/, /pa-ka-ta/, /pa/, /ta/, and /ka/; to read one text containing 36 words; and to produce a monologue ([Vásquez-Correa et al., 2019](document_1.txt)). This makes the Spanish protocol the most extensive of the three in terms of the number of elicitation tasks.

### 2.3 Clinical annotation

All Spanish patients were recorded in the ON state, that is, under the effect of their daily medication ([Vásquez-Correa et al., 2019](document_1.txt)). This is a meaningful design variable: medication state is known to influence hypokinetic dysarthria, and the study does not report an equivalent statement for the German and Czech groups.

## 3. The German Dataset

The German data consist of speech recordings of PD patients and HC speakers from Germany, with the participants performing four speech tasks: the rapid repetition of /pa-ta-ka/, five sentences, one text with 81 words, and a monologue ([Vásquez-Correa et al., 2019](document_1.txt)). The underlying source is identified in the reference list as Skodda, Visser, and Schlegel’s 2011 *Journal of Voice* article on vowel articulation in Parkinson’s disease ([Vásquez-Correa et al., 2019](document_1.txt)).

The German dataset is the largest of the three if the primary source count is accepted (176 speakers), but its reported composition is internally inconsistent, as noted above ([Vásquez-Correa et al., 2019](document_1.txt); [Third-party research note, n.d.](document_2.txt)). Notably, the German protocol includes five sentences and an 81-word text — item counts that differ from both the Spanish (ten sentences; 36-word text) and Czech (no sentence list reported; 80-word text) protocols.

## 4. The Czech Dataset

A total of 100 native Czech speakers, comprising 50 PD patients and 50 healthy controls, were considered ([Vásquez-Correa et al., 2019](document_1.txt); [Third-party research note, n.d.](document_2.txt)). The speech tasks performed by the Czech participants include the rapid repetition of the syllables /pa-ta-ka/, a read text with 80 words, and a monologue ([Vásquez-Correa et al., 2019](document_1.txt)). The Czech data derive from Rusz’s 2018 habilitation thesis on detecting speech disorders in early Parkinson’s disease by acoustic analysis ([Vásquez-Correa et al., 2019](document_1.txt)). Compared with the Spanish and German protocols, the Czech protocol is the most compact, containing no listed sentence-repetition task.

## 5. Comparative View of the Three Datasets

| Property | Spanish (PC-GITA) | German | Czech |
|---|---|---|---|
| Native language | Colombian Spanish | German | Czech |
| PD / HC speakers | 50 / 50 | 88 / 88 (or 44 / 44) | 50 / 50 |
| Rapid syllable task | /pa-ta-ka/, /pe-ta-ka/, /pa-ka-ta/, /pa/, /ta/, /ka/ | /pa-ta-ka/ | /pa-ta-ka/ |
| Sentence list | 10 sentences | 5 sentences | Not reported |
| Read text length | 36 words | 81 words | 80 words |
| Monologue | Yes | Yes | Yes |
| Medication state reported | ON state | Not reported | Not reported |
| Clinical scale | MDS-UPDRS-III | MDS-UPDRS-III | MDS-UPDRS-III |

The three datasets were all captured under noise-controlled conditions and down-sampled to 16 kHz, and all patients were evaluated by a neurologist expert according to the third section of the Movement Disorder Society–sponsored revision of the Unified Parkinson’s Disease Rating Scale (MDS-UPDRS-III) ([Vásquez-Correa et al., 2019](document_1.txt); [Third-party research note, n.d.](document_2.txt)). Table 1 of the study records, for each dataset, the number of subjects, gender distribution (M/F), age, MDS-UPDRS-III score, and time since diagnosis in years ([Vásquez-Correa et al., 2019](document_1.txt)).

## 6. Variables Derived from the Datasets

### 6.1 Transition segmentation

Speech signals were analysed using automatic detection of onset and offset transitions between voiced and unvoiced segments, which models the patients’ difficulty in starting and stopping vocal fold vibration ([Vásquez-Correa et al., 2019](document_1.txt)). The border between voiced and unvoiced frames was detected, and 80 ms of signal on either side were taken, forming segments of 160 ms in length ([Vásquez-Correa et al., 2019](document_1.txt)). The datasets are therefore used at the *segment* level rather than only at the utterance level, and the final decision for each speaker was obtained by a majority voting strategy across the different speech exercises ([Vásquez-Correa et al., 2019](document_1.txt)).

### 6.2 Hand-crafted baseline descriptors

The baseline feature set comprises 12 Mel-Frequency Cepstral Coefficients (MFCCs) with their first and second derivatives, plus the log energy of the signal distributed into 22 Bark bands — 58 descriptors in total ([Vásquez-Correa et al., 2019](document_1.txt)). Four statistical functionals (mean, standard deviation, skewness, and kurtosis) were computed for each descriptor, producing a 232-dimensional feature vector per utterance ([Vásquez-Correa et al., 2019](document_1.txt)). Classification used a radial basis function SVM with margin parameter C = 10 and Gaussian kernel parameter γ = 0.0001, evaluated with speaker-independent 10-fold cross-validation ([Vásquez-Correa et al., 2019](document_1.txt)).

### 6.3 CNN input representations

Short-time Fourier transform (STFT) representations with 256 frequency bins were computed for each segmented transition, with a window length of 16 ms and a step size of 4 ms, forming 41 time frames per transition; the spectrogram was then converted to the Mel scale using 80 filters, yielding an 80 × 41 input spectrogram ([Vásquez-Correa et al., 2019](document_1.txt)). The CNN comprises four convolutional and max-pooling layers, dropout regularisation, and two fully connected layers followed by a softmax output layer, trained with cross-entropy loss and an Adam optimiser ([Vásquez-Correa et al., 2019](document_1.txt)).

## 7. Principal Findings Obtained from These Datasets

Using these datasets, the study compared hand-crafted-feature SVMs with CNNs within each language, and then applied cross-lingual transfer learning ([Vásquez-Correa et al., 2019](document_1.txt)).

| Base language | Target language | Accuracy % (SD) | Sensitivity % (SD) | Specificity % (SD) | MCC |
|---|---|---|---|---|---|
| Spanish | German | 77.3 (11.3) | 86.2 (13.8) | 68.3 (14.3) | 0.57 |
| Spanish | Czech | 72.6 (13.9) | 82.0 (14.8) | 62.0 (28.9) | 0.46 |
| German | Spanish | 70.0 (12.5) | 62.0 (19.9) | 78.0 (23.9) | 0.41 |
| German | Czech | 72.0 (13.1) | 67.0 (11.6) | 78.0 (23.9) | 0.46 |
| Czech | German | 70.7 (14.5) | 80.0 (16.3) | 62.5 (26.3) | 0.38 |
| Czech | Spanish | 76.7 (7.9) | 87.5 (11.0) | 66.0 (15.6) | 0.55 |

*Reconstructed from a partially garbled transcription of Table 4 ([Vásquez-Correa et al., 2019](document_1.txt)); row labels should be verified against the original.*

The prose of the study confirms the key comparisons: accuracy improved over 8% for German (from 69.3% in the baseline to 77.3% when fine-tuned from Spanish) and over 4.1% for Czech (from 68.5% with the initial CNN to 72.6% when fine-tuned from Spanish) ([Vásquez-Correa et al., 2019](document_1.txt)). The highest accuracy for German and Czech was obtained when Spanish was the base language, which the authors explain by the better initial separability of the Spanish data ([Vásquez-Correa et al., 2019](document_1.txt)). That better separability is itself attributed to the higher average MDS-UPDRS-III scores of the Spanish patients relative to the German and Czech patients — that is, greater disease severity in the Spanish group ([Vásquez-Correa et al., 2019](document_1.txt)).

## 8. Limitations, Reliability, and Bias Considerations

Several limitations follow directly from the dataset design. First, the three corpora are **not task-matched**: the sentence lists differ (ten Spanish vs. five German vs. none reported for Czech), and read-text lengths differ (36, 81, and 80 words respectively) ([Vásquez-Correa et al., 2019](document_1.txt)). Only the rapid /pa-ta-ka/ repetition, a read text, and a monologue are shared across all three languages. Cross-lingual transfer results are therefore confounded with task differences, not just linguistic ones.

Second, **phonetic and phonological bias** is explicitly acknowledged: Czech and German are richer than Spanish in consonant production, which may make consonant sounds easier for Czech PD patients to produce than for Spanish PD patients ([Vásquez-Correa et al., 2019](document_1.txt)). The authors note that classification in different languages must be carefully conducted to avoid bias toward the linguistic content present in each language ([Vásquez-Correa et al., 2019](document_1.txt)).

Third, **clinical heterogeneity** exists across the datasets: the Spanish patients were recorded in the ON medication state ([Vásquez-Correa et al., 2019](document_1.txt)), and Spanish patients had higher average disease severity than German and Czech patients ([Vásquez-Correa et al., 2019](document_1.txt)).

Fourth, **class balance versus prediction balance**: although all three datasets are perfectly balanced by design (50/50, 44/44 or 88/88, 50/50), the per-language baseline and CNN models produced results that were unbalanced toward one class in terms of specificity and sensitivity ([Vásquez-Correa et al., 2019](document_1.txt)). Transfer learning was found to yield more balanced specificity–sensitivity and lower variance ([Vásquez-Correa et al., 2019](document_1.txt)).

Fifth, the study cautions that earlier reported accuracies of 80%–94% on comparable multilingual data were **optimistic**, because classifier hyper-parameters had been optimised on the test set ([Vásquez-Correa et al., 2019](document_1.txt)). This is a useful warning about the reliability of headline accuracy figures in this literature more broadly.

## 9. Common and Intended Use Cases

The datasets support at least five use cases. (1) **Diagnostic classification** of HC subjects versus PD patients from speech ([Vásquez-Correa et al., 2019](document_1.txt)). (2) **Severity assessment**, namely predicting the degradation of speech according to a specific clinical scale such as MDS-UPDRS-III ([Vásquez-Correa et al., 2019](document_1.txt)). (3) **Benchmarking** hand-crafted acoustic descriptors (MFCCs, Bark-band log energy, statistical functionals) against CNN-learned representations ([Vásquez-Correa et al., 2019](document_1.txt)). (4) **Cross-lingual transfer learning research**, in which a model trained on one language initialises a model for another ([Vásquez-Correa et al., 2019](document_1.txt)). (5) **Future multi-lingual and cross-disease transfer**, including training base models on two languages instead of one and transferring from PD to other neurological diseases such as Huntington’s disease ([Vásquez-Correa et al., 2019](document_1.txt)).

## 10. Conclusion

In answer to the query, three datasets are used: the Spanish **PC-GITA** corpus (50 PD, 50 HC), German speech recordings (88 PD, 88 HC per the primary source; 44 PD, 44 HC per the third-party note), and Czech speech recordings (50 PD, 50 HC), all annotated with MDS-UPDRS-III scores, recorded under noise-controlled conditions at 16 kHz, and segmented into 160 ms voiced–unvoiced transitions for modelling ([Vásquez-Correa et al., 2019](document_1.txt); [Third-party research note, n.d.](document_2.txt)). In my assessment, the three-language design is a genuine strength for cross-lingual research, but the corpora are heterogeneous in task structure, clinically heterogeneous in medication state and severity, and inconsistently documented in the case of the German speaker counts. Any downstream reuse of these datasets should therefore begin by verifying the German composition and by treating cross-lingual comparisons as confounded with task design.

## References

Third-party research note: Convolutional neural networks and a transfer learning strategy to classify Parkinson’s disease from speech in three different languages [document_2.txt]. (n.d.).

Vásquez-Correa, J. C., Arias-Vergara, T., Rios-Urrego, C. D., Schuster, M., Rusz, J., Orozco-Arroyave, J. R., & Nöth, E. (2019). *Convolutional neural networks and a transfer learning strategy to classify Parkinson’s disease from speech in three different languages* [document_1.txt].