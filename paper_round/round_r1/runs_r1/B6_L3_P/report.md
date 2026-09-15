# Datasets Used in the Cross-Lingual Parkinson's Disease Speech Classification Study

## 1. Introduction: Scope of the Query and the Evidence Base

The query asks which datasets are used in the study titled *"Convolutional Neural Networks and a Transfer Learning Strategy to Classify Parkinson's Disease from Speech in Three Different Languages."* The short answer is that the work draws on **three language-specific speech corpora** — one Spanish, one German, and one Czech — each containing speech recordings from Parkinson's disease (PD) patients and healthy control (HC) speakers who were clinically evaluated by a neurologist using the third section of the Movement Disorder Society–sponsored Unified Parkinson's Disease Rating Scale (MDS-UPDRS-III) ([document_1.txt](document_1.txt)). This report identifies each dataset, describes its speaker composition, recording conditions, speech tasks, and clinical annotations, explains how the data were processed and fed into the convolutional neural network (CNN) pipeline, summarizes the transfer-learning results the datasets produced, and evaluates the strengths and limitations of the data design ([document_1.txt](document_1.txt); [document_2.txt](document_2.txt)).

Two source documents inform this report. The first, `document_1.txt`, is the manuscript itself, authored by J. C. Vásquez-Correa, T. Arias-Vergara, C. D. Rios-Urrego, M. Schuster, J. Rusz, J. R. Orozco-Arroyave, and E. Nöth, with affiliations spanning the Universidad de Antioquia (Medellín, Colombia), Friedrich-Alexander Universität Erlangen-Nürnberg (Germany), Ludwig-Maximilians University, the Czech Technical University in Prague, and Universität Munich ([document_1.txt](document_1.txt)). The second, `document_2.txt`, is a third-party research note that digests the dataset information from the same manuscript ([document_2.txt](document_2.txt)). Because `document_1.txt` is an OCR-degraded rendering of the original paper, several numeric tables are partially corrupted; where this affects the level of detail that can be reliably reported, the limitation is flagged explicitly rather than silently smoothed over ([document_1.txt](document_1.txt)).

## 2. The Three Primary Datasets at a Glance

The study explicitly considers "speech recordings of patients in three different languages… Spanish, German, and Czech" ([document_1.txt](document_1.txt)). All recordings were captured under noise-controlled conditions, and all speech signals were down-sampled to 16 kHz ([document_1.txt](document_1.txt)). Table 1 summarizes the datasets.

### Table 1. Overview of the datasets used in the study

| Language | Corpus / source | PD speakers | HC speakers | Total speakers | Speech tasks | Source reference in study |
|---|---|---|---|---|---|---|
| Spanish | PC-GITA corpus | 50 | 50 | 100 (Colombian Spanish natives) | 10 sentences; rapid repetition of /pa-ta-ka/, /pe-ta-ka/, /pa-ka-ta/, /pa/, /ta/, /ka/; one 36-word text; monologue | [6] ([document_1.txt](document_1.txt)) |
| German | German speech recordings | 88 (stated) / 44 (per third-party note) | 88 (stated) / 44 (per third-party note) | 176 (stated) / 88 (per third-party note) | Rapid repetition of /pa-ta-ka/; 5 sentences; one 81-word text; monologue | [18] ([document_1.txt](document_1.txt); [document_2.txt](document_2.txt)) |
| Czech | Czech speech recordings | 50 | 50 | 100 native Czech speakers | Rapid repetition of /pa-ta-ka/; one 80-word read text; monologue | [19] ([document_1.txt](document_1.txt)) |

### 2.1 The Spanish Dataset: PC-GITA Corpus

The Spanish portion of the data is the **PC-GITA corpus**, which "contains utterances from 50 PD patients and 50 HC, Colombian Spanish native speakers" ([document_1.txt](document_1.txt)). The third-party note corroborates this composition and emphasizes that PC-GITA "provides the Spanish portion of the cross-lingual speech data" ([document_2.txt](document_2.txt)). PC-GITA is a well-known Spanish-language resource for Parkinsonian speech analysis; the study cites it as reference [6], the "New Spanish Speech Corpus Database for the Analysis of People Suffering from Parkinson's Disease," presented at the Ninth International Conference on Language Resources and Evaluation ([document_1.txt](document_1.txt)). The corpus is described as having been used previously for baseline evaluations reaching up to 77% accuracy with Gaussian mixture models and support vector machines, and up to 81% in a forced-alignment phoneme-based model ([document_1.txt](document_1.txt)).

The Spanish participants were asked to pronounce ten sentences, the rapid repetition of the syllables /pa-ta-ka/, /pe-ta-ka/, /pa-ka-ta/, /pa/, /ta/, and /ka/, one text with 36 words, and a monologue ([document_1.txt](document_1.txt)). This makes the Spanish protocol the most extensive of the three in terms of task variety, a point that matters for comparability across languages. The manuscript also states that all patients "were in ON state at the time of the recording, i.e., under the effect of their daily medication" ([document_1.txt](document_1.txt)).

### 2.2 The German Dataset

The German data are described in the manuscript as "speech recordings of 8 8 PD patients and 8 8 HC speakers from Germany," cited to reference [18], a study on vowel articulation in Parkinson's disease published in the *Journal of Voice* ([document_1.txt](document_1.txt)). The German participants performed four speech tasks: the rapid repetition of /pa-ta-ka/, five sentences, one text with 81 words, and a monologue ([document_1.txt](document_1.txt)).

There is an important discrepancy in the reported German speaker count. The third-party research note states that "the German data consist of speech recordings of 44 PD patients and 44 HC speakers" and that "the German dataset description reports this composition" ([document_2.txt](document_2.txt)). Read literally, the primary manuscript appears to claim 88 PD patients and 88 HC speakers, while the digest claims 44 and 44. The most economical reconciliation — consistent with the OCR artifact pattern in `document_1.txt`, where digits are frequently duplicated or split (for example, "1 0 0" for 100 and "5 0" for 50) — is that the German set comprises **88 speakers in total (44 PD and 44 HC)**, matching the third-party note ([document_1.txt](document_1.txt); [document_2.txt](document_2.txt)). Either way, the German dataset is the smallest of the three in the digest's rendering, and this ambiguity is a genuine documentation weakness rather than a mere typographical curiosity.

### 2.3 The Czech Dataset

The Czech data comprise "a total of 1 0 0 native Czech speakers (5 0 PD, 5 0 HC)," cited to reference [19], J. Rusz's habilitation thesis on detecting speech disorders in early Parkinson's disease by acoustic analysis ([document_1.txt](document_1.txt)). The third-party note confirms the same counts: 50 PD patients and 50 healthy controls, all native Czech speakers ([document_2.txt](document_2.txt)). The Czech participants performed the rapid repetition of the syllables /pa-ta-ka/, a read text with 80 words, and a monologue ([document_1.txt](document_1.txt)). Notably, the Czech protocol lacks a multi-sentence task comparable to the five sentences used in German or the ten sentences used in Spanish, and the sentence material differs in length (80-word Czech text versus 81-word German text versus 36-word Spanish text) ([document_1.txt](document_1.txt)). The manuscript also references earlier Czech data from the same group, which achieved accuracies of up to 94% in prior articulation studies ([document_1.txt](document_1.txt)).

## 3. Population and Clinical Characterization of the Datasets

Beyond speaker counts, Table 1 of the manuscript summarizes demographically and clinically relevant variables: number of speakers, gender (M/F), age range, MDS-UPDRS-III score, and time after diagnosis in years ([document_1.txt](document_1.txt)). Table 2 reproduces the recoverable elements.

### Table 2. Recoverable demographic and clinical descriptors from the study's Table 1

| Measure | Spanish | German | Czech |
|---|---|---|---|
| PD / HC count | 50 / 50 | 88 / 88 (stated) or 44 / 44 (note) | 50 / 50 |
| Age range, PD | 33–81 years | 44–82 years | 43–82 years |
| Age range, HC | 31–86 years | 26–83 years | 41–77 years |
| Clinical rating | MDS-UPDRS-III by expert neurologist | MDS-UPDRS-III by expert neurologist | MDS-UPDRS-III by expert neurologist |
| Disease severity | Higher average MDS-UPDRS-III than German and Czech cohorts | Lower than Spanish cohort | Lower than Spanish cohort |

Source: ([document_1.txt](document_1.txt); [document_2.txt](document_2.txt)).

The clinical scale used across all three datasets is the MDS-UPDRS-III, applied by expert neurologists ([document_1.txt](document_1.txt); [document_2.txt](document_2.txt)). The authors report a substantive clinical asymmetry: "for the patients in the Spanish language, the average MDS-UPDRS-III score is higher compared with the German and Czech patients, i.e., there are patients with higher disease severity in the Spanish data" ([document_1.txt](document_1.txt)). This single fact is pivotal for interpreting the entire cross-lingual experiment, because it offers a non-linguistic explanation for why the Spanish model separates PD from HC most effectively and, consequently, why a Spanish-pretrained model transfers best to the other languages ([document_1.txt](document_1.txt)).

The manuscript's Table 1 also contains gender distributions and mean (standard deviation) values for age, MDS-UPDRS-III, and time since diagnosis per language and per group ([document_1.txt](document_1.txt)). Because the OCR rendering interleaves columns and rows (for example, fragments such as "6 1.3 (1 1.4)" and "2 3.3 (1 2.0)"), only the age ranges and the qualitative severity ordering can be stated with confidence here; the remaining gender and time-since-diagnosis cells cannot be reliably reconstructed from the available text ([document_1.txt](document_1.txt)). This constraint should be borne in mind by any reader attempting to reuse the numbers.

## 4. How the Datasets Were Prepared and Represented

All three corpora were processed identically, which is what makes cross-language transfer learning feasible in this design ([document_1.txt](document_1.txt)). The pipeline has four steps.

### 4.1 Segmentation of onset/offset transitions

Speech signals were analyzed via "the automatic detection of onset and offset transitions, which model the difficulties of the patients to start/stop the movement of the vocal folds" ([document_1.txt](document_1.txt)). Detection relies on the presence of the fundamental frequency in short-time frames; the border between voiced and unvoiced frames is identified, and 80 ms of signal are taken to the left and right, forming segments of 160 ms ([document_1.txt](document_1.txt)). This articulation-centered segmentation is the conceptual bridge between the three language datasets, since it avoids dependence on linguistic content ([document_1.txt](document_1.txt)).

### 4.2 Baseline feature representation

The baseline model extracts 12 Mel-Frequency Cepstral Coefficients (MFCCs) with their first and second derivatives, plus the log energy of the signal distributed into 22 Bark bands, totaling 58 descriptors ([document_1.txt](document_1.txt)). Four statistical functionals — mean, standard deviation, skewness, and kurtosis — are computed for each descriptor, yielding a 232-dimensional feature vector per utterance ([document_1.txt](document_1.txt)). Classification uses a radial-basis SVM with margin parameter C = 10 and a Gaussian kernel with γ = 0.0001, tested with speaker-independent 10-fold cross-validation ([document_1.txt](document_1.txt)).

### 4.3 CNN input representation

For the deep model, a short-time Fourier transform with 256 frequency bins is computed for each segmented transition, using a 16 ms window and a 4 ms step size, producing 41 time frames per transition ([document_1.txt](document_1.txt)). The spectrogram is then mapped to the Mel scale with 80 filters, forming an 80 × 41 time-frequency image used to train the CNNs ([document_1.txt](document_1.txt)). The CNN architecture comprises four convolutional and max-pooling layers, dropout regularization, two fully connected layers, and a softmax output layer, with feature maps doubled at each convolutional layer and trained with cross-entropy loss using the Adam optimizer ([document_1.txt](document_1.txt)).

### 4.4 Speaker-level aggregation

All speech exercises performed by participants were used for classification, and the final decision for each speaker was obtained by majority voting across the different speech exercises ([document_1.txt](document_1.txt)). This detail is essential because it means the unit of analysis is the speaker, not the utterance, and the reported accuracies therefore reflect speaker-level diagnosis.

## 5. How the Datasets Were Used: Experiments and Results

The experimental design exploits the three datasets in two stages ([document_1.txt](document_1.txt)). First, baseline and CNN models are trained for each language individually, establishing monolingual reference performance. Second, a CNN trained on one language (the "base" language) is used to initialize a model that is then fine-tuned with utterances from a target language ([document_1.txt](document_1.txt)). The transfer-learning scheme aims to improve accuracy "when the weights of the neural network are initialized with utterances from a different language than the used for the test set" ([document_1.txt](document_1.txt)).

For the monolingual stage, the manuscript reports that similar accuracies were obtained between the baseline and CNN models for Spanish, which also exhibited the highest accuracy among the three languages; the highest accuracy for German was obtained with the baseline model (69.3%); and for Czech the CNN produced the highest accuracy (68.5%) ([document_1.txt](document_1.txt)). The authors also note that for all three languages the monolingual results "are unbalanced towards one of the two classes according to the specificity and sensitivity values" ([document_1.txt](document_1.txt)). The full per-language baseline/CNN accuracy matrix cannot be reconstructed from the degraded tables in `document_1.txt`, so only the prose-anchored figures are reported here ([document_1.txt](document_1.txt)).

For the transfer-learning stage, Table 3 reproduces the recoverable six-cell transfer matrix.

### Table 3. Transfer-learning results across languages (accuracy with standard deviation in parentheses)

| Base language (pre-training) | Target language (fine-tuning/testing) | Accuracy (%) | Sensitivity (%) | Specificity (%) | MCC |
|---|---|---|---|---|---|
| Spanish | German | 77.3 (11.3) | 86.2 (13.8) | 68.3 (14.3) | 0.57 |
| Czech | German | 76.7 (7.9) | 87.5 (11.0) | 66.0 (15.6) | 0.55 |
| Spanish | Czech | 72.6 (13.9) | 82.0 (14.8) | 62.0 (28.9) | 0.46 |
| German | Czech | 70.7 (14.5) | 80.0 (16.3) | 62.5 (26.3) | 0.38 |
| Czech | Spanish | 72.0 (13.1) | 67.0 (11.6) | 78.0 (23.9) | 0.46 |
| German | Spanish | 70.0 (12.5) | 62.0 (19.9) | 78.0 (23.9) | 0.41 |

Source: reconstructed from Table 4 and the accompanying prose in ([document_1.txt](document_1.txt)). The prose confirms the two headline figures: German improved "over 8%" from 69.3% baseline to 77.3% when fine-tuned from Spanish, and Czech improved over 4.1% from 68.5% with the initial CNN to 72.6% when fine-tuned from Spanish ([document_1.txt](document_1.txt)). The receiver operating characteristic analysis similarly shows the highest AUC for German and Czech targets when the base model is trained on Spanish, while for a Spanish target the highest AUC occurs with a Czech base model ([document_1.txt](document_1.txt)).

The authors explain the Spanish advantage by reference to the datasets themselves: "Spanish speakers have the best initial separability, thus, the other two languages benefit from the best initial model" ([document_1.txt](document_1.txt)). They also report that transfer-learned models are "more balanced in terms of the specificity-sensitivity" and show lower variance, improving generalization ([document_1.txt](document_1.txt)). Critically, they caution that transfer learning improved target-language accuracy "only when the base model was robust enough" ([document_1.txt](document_1.txt)).

## 6. Datasets and Corpora Referenced but Not Used

The manuscript reviews several other resources that are not part of the present experiments but shape its motivation. These include a Turkish dataset of 20 PD patients and 20 HC subjects used by Sakar et al. with KNN and SVM classifiers reaching up to 75% accuracy ([document_1.txt](document_1.txt)); Czech data from Rusz et al. on imprecise vowel articulation, used to test a forced-Gaussian methodology and yielding up to 94% accuracy on Czech data versus 81% on Spanish data ([document_1.txt](document_1.txt)); and handwriting data used in a separate transfer-learning study by Naseer et al. ([document_1.txt](document_1.txt)). The manuscript also flags a methodological caveat in prior work: one study reported accuracies of 80% to 94% across the three languages, but "the results were optimistic, since the hyper-parameters of the classifier were optimized based on the accuracy on the test set" ([document_1.txt](document_1.txt)). Distinguishing these background corpora from the three datasets actually used is important, because the third-party note's phrasing could otherwise be read as if all referenced data were part of the present study ([document_2.txt](document_2.txt)).

## 7. Assessment: Strengths, Limitations, and an Analytic Position

The dataset design has clear merits. It is genuinely multilingual, pairing matched PD and HC groups in Spanish, German, and Czech; it uses clinically grounded labels from expert neurologist ratings on the MDS-UPDRS-III rather than convenience labels; it standardizes recording conditions (noise-controlled, 16 kHz) and processing across languages; and it adopts a speaker-independent cross-validation protocol, which is essential to avoid speaker leakage ([document_1.txt](document_1.txt); [document_2.txt](document_2.txt)). The articulation-transition segmentation further reduces direct dependence on linguistic content, making the cross-language comparison more defensible ([document_1.txt](document_1.txt)).

The limitations, however, are substantial and should temper any strong conclusion. First, the sample size per language is modest — 100 speakers each for Spanish and Czech and, on the most plausible reading, 88 for German — and the number of independent speakers, rather than utterances, governs statistical power ([document_1.txt](document_1.txt); [document_2.txt](document_2.txt)). Second, the German speaker count is reported inconsistently between the manuscript and the digest, which weakens confidence in the underlying corpora documentation ([document_1.txt](document_1.txt); [document_2.txt](document_2.txt)). Third, the protocols are not fully parallel: Spanish includes ten sentences and a six-syllable repetition set, German includes five sentences and an 81-word text, and Czech includes only a syllable repetition and an 80-word text, so task coverage differs across languages ([document_1.txt](document_1.txt)). Fourth, and most importantly, the authors themselves identify a severity confound: the Spanish cohort had the highest average MDS-UPDRS-III, meaning that the "best initial separability" of the Spanish model may reflect greater disease severity rather than a language-independent representational advantage ([document_1.txt](document_1.txt)). Fifth, the manuscript does not state that the German and Czech corpora are publicly available or shared under an open license; they appear tethered to prior studies, which constrains reproducibility ([document_1.txt](document_1.txt)). Finally, the OCR-degraded tables in `document_1.txt` prevent independent verification of parts of the demographic and monolingual results ([document_1.txt](document_1.txt)).

My concrete position is this: the three corpora constitute an appropriate and unusually well-matched foundation for a cross-lingual pilot study of Parkinsonian speech, and the reported 8% gain for German and the improved specificity–sensitivity balance are plausible and clinically meaningful directions of effect, but the evidence is not yet strong enough to support broad claims about "language-independent" Parkinsonian speech markers. The design confounds language with disease severity, the German documentation is internally inconsistent, and the absence of a documented, versioned, openly available multilingual benchmark makes the results hard to validate. A convincing follow-up would require (a) resolving the German speaker count and publishing the exact corpus provenance, (b) matching MDS-UPDRS-III distributions across languages through stratified sampling or covariate adjustment, (c) harmonizing speech tasks and text lengths, and (d) reporting per-speaker predictions and confidence intervals rather than only aggregate accuracy, sensitivity, specificity, and MCC. The authors' own proposed extensions — Bayesian hyper-parameter optimization for more robust base models, training base models on two languages, and staging patients by MDS-UPDRS-III or dysarthria severity — point in precisely this direction ([document_1.txt](document_1.txt)).

## 8. Conclusion

To answer the query directly: the study uses **three datasets**, one per language. The Spanish dataset is the **PC-GITA corpus** (50 PD patients, 50 healthy controls, Colombian Spanish native speakers; tasks include ten sentences, six syllable-repetition patterns, a 36-word text, and a monologue). The German dataset consists of speech recordings from German speakers reported as 88 PD and 88 HC in the manuscript, but as 44 PD and 44 HC in the accompanying research note (tasks: /pa-ta-ka/, five sentences, an 81-word text, and a monologue). The Czech dataset contains 100 native Czech speakers (50 PD, 50 HC; tasks: /pa-ta-ka/, an 80-word read text, and a monologue) ([document_1.txt](document_1.txt); [document_2.txt](document_2.txt)). All three were recorded in noise-controlled conditions, down-sampled to 16 kHz, clinically rated with MDS-UPDRS-III, and converted into 160 ms voiced/unvoiced transition segments represented as 80 × 41 Mel-scale spectrograms for CNN training and transfer learning ([document_1.txt](document_1.txt)). These three corpora jointly support the study's central finding that a Spanish-pretrained CNN fine-tuned to German or Czech improves accuracy (up to 8% for German) and produces more balanced sensitivity–specificity trade-offs, with the caveat that this benefit depends on the robustness of the base model ([document_1.txt](document_1.txt)).

## References

Convolutional neural networks and a transfer learning strategy to classify Parkinson's disease from speech in three different languages [document_1.txt]. (n.d.).

Third-party research note: Convolutional neural networks and a transfer learning strategy to classify Parkinson's disease from speech in three different languages [document_2.txt]. (n.d.).