# Datasets Used in the Cross-Lingual Classification of Parkinson's Disease from Speech

## 1. Purpose and Scope of the Report

This report identifies and characterises the datasets employed in the study "Convolutional Neural Networks and a Transfer Learning Strategy to Classify Parkinson's Disease from Speech in Three Different Languages," which develops a methodology for classifying Parkinson's disease (PD) from speech in Spanish, German, and Czech using convolutional neural networks (CNNs) trained on time-frequency representations combined with a transfer learning strategy among the three languages ([document_2.txt](document_2.txt)).

The direct answer to the query is that the study uses **three language-specific clinical speech corpora covering three languages — Spanish, German, and Czech** — totalling roughly 288 speakers, comprising approximately 144 PD patients and 144 healthy control (HC) subjects ([document_2.txt](document_2.txt)). All three corpora were recorded under noise-controlled conditions, down-sampled to 16 kHz, and clinically annotated by a neurologist expert according to the third section of the Movement Disorder Society–sponsored revision of the Unified Parkinson's Disease Rating Scale (MDS-UPDRS-III) ([document_1.txt](document_1.txt)). The report below details each corpus, its speaker composition, the speech tasks it contains, the common acquisition protocol, the data preparation pipeline, and the role each dataset plays in the modelling and transfer learning experiments.

## 2. The Three Language-Specific Speech Corpora

### 2.1 Spanish: The PC-GITA Corpus

The Spanish portion of the data is drawn from the **PC-GITA corpus** ([document_1.txt](document_1.txt)). PC-GITA contains utterances from 50 PD patients and 50 healthy control subjects, all Colombian Spanish native speakers ([document_2.txt](document_2.txt)). This corpus provides the Spanish half of the cross-lingual speech data and is the single largest of the three language partitions together with the Czech data ([document_2.txt](document_2.txt)).

The recorded tasks in PC-GITA are comparatively rich. Participants were asked to pronounce a total of 10 sentences, to perform rapid repetition of the syllable sequences /pa-ta-ka/, /pe-ta-ka/, /pa-ka-ta/, and the sustained vowels /pa/, /ta/, and /ka/, to read one text containing 36 words, and to produce a monologue ([document_1.txt](document_1.txt)). An important clinical detail is that all PD patients in the Spanish cohort were recorded in the **ON state**, that is, under the effect of their daily medication ([document_1.txt](document_1.txt)). This is methodologically consequential: medication status is known to influence speech motor performance, and the ON-state recording condition constrains how the results generalise to unmedicated patients.

### 2.2 German Speech Recordings

The German data consist of speech recordings from **44 PD patients and 44 HC speakers** ([document_2.txt](document_2.txt)). The German dataset is therefore the smallest of the three language partitions in terms of speaker count, and its composition is described as 44 PD patients paired with 44 healthy controls ([document_2.txt](document_2.txt)). The German recordings, together with the Spanish and Czech recordings, form the dataset base for the CNN and transfer learning strategy investigated in the study ([document_2.txt](document_2.txt)). Notably, the German cohort is the language group where the hand-crafted baseline outperformed the CNN in within-language training, a fact that becomes relevant when assessing the value of the transfer learning approach ([document_1.txt](document_1.txt)).

### 2.3 Czech Speech Recordings

The Czech dataset contains a total of **100 native Czech speakers, comprising 50 PD patients and 50 healthy controls** ([document_2.txt](document_2.txt)). The speech tasks performed by the Czech participants include the rapid repetition of the syllables /pa-ta-ka/, a read text containing 80 words, and a monologue ([document_1.txt](document_1.txt)). The Czech corpus is thus structurally different from PC-GITA: it contains fewer and partly different elicitation tasks (notably a longer 80-word reading passage rather than the 36-word text used in Spanish), and it does not include the sustained vowel or the full set of rapid syllable sequences found in the Spanish protocol ([document_1.txt](document_1.txt)).

## 3. Comparative Overview of the Datasets

The following table consolidates the available facts about speaker composition, corpus identity, and clinical evaluation for the three datasets.

| Language | Corpus / Source | PD Patients | Healthy Controls | Total Speakers | Clinical Scale | Key Speech Tasks |
|---|---|---|---|---|---|---|
| Spanish | PC-GITA ([document_1.txt](document_1.txt)) | 50 | 50 | 100 | MDS-UPDRS-III ([document_2.txt](document_2.txt)) | 10 sentences; /pa-ta-ka/, /pe-ta-ka/, /pa-ka-ta/; /pa/, /ta/, /ka/; 36-word text; monologue ([document_1.txt](document_1.txt)) |
| German | German speech recordings ([document_2.txt](document_2.txt)) | 44 | 44 | 88 | MDS-UPDRS-III ([document_2.txt](document_2.txt)) | Not specified in the available material |
| Czech | Czech speech recordings, Rusz corpus ([document_1.txt](document_1.txt)) | 50 | 50 | 100 | MDS-UPDRS-III ([document_2.txt](document_2.txt)) | /pa-ta-ka/; 80-word read text; monologue ([document_1.txt](document_1.txt)) |
| **Total** | **Three corpora** | **144** | **144** | **288** | **MDS-UPDRS-III across all** | Heterogeneous across languages |

Beyond the language-specific summaries, the study reports a Table 1 that summarises speaker information across the three datasets using fields for number of subjects, gender (male or female), and time after diagnosis in years ([document_1.txt](document_1.txt)). Only the header information for that table is available in the source material, so the per-group gender distributions and mean disease durations cannot be reported here ([document_1.txt](document_1.txt)).

## 4. Common Acquisition and Clinical Protocol

A defining feature of the dataset design is that the three corpora share a common acquisition and clinical annotation framework, which is a prerequisite for any cross-lingual transfer experiment. Specifically:

- **Noise-controlled recording conditions.** All recordings across the three languages were captured in noise-controlled conditions ([document_1.txt](document_1.txt)).
- **Uniform sampling rate.** The speech signals were down-sampled to 16 kHz in all three datasets ([document_1.txt](document_1.txt)).
- **Common clinical reference standard.** The patients in the three datasets were evaluated by a neurologist expert according to the third section of the MDS-UPDRS-III ([document_1.txt](document_1.txt); [document_2.txt](document_2.txt)).
- **Disease-level labelling.** The classification task is binary — PD versus healthy control — rather than severity regression, although the authors state that further experiments will evaluate the models to classify PD patients at several stages of the disease based on the MDS-UPDRS-III score or on dysarthria severity ([document_1.txt](document_1.txt)).

The German and Czech speaker counts of 44 PD with 44 HC and 50 PD with 50 HC respectively, together with the Spanish 50 PD and 50 HC composition, confirm that the datasets supply balanced PD/HC groups within each language ([document_2.txt](document_2.txt)). This within-language balance matters for the evaluation metrics used later, because sensitivity and specificity are computed separately and can be interpreted against a 50/50 prior within each language ([document_1.txt](document_1.txt)).

## 5. From Raw Recordings to Model Inputs: The Data Preparation Pipeline

The datasets are not consumed directly as raw audio. The study applies a segmentation procedure grounded in the clinical phenomenology of PD speech, namely the difficulty patients exhibit in starting and stopping vocal fold movement. Speech signals are analysed based on automatic detection of onset and offset transitions, and the detection of these transitions is based on the presence of the fundamental frequency in short-time frames ([document_1.txt](document_1.txt)). The border between voiced and unvoiced frames is detected, and 80 ms of signal are taken to the left and to the right, forming segments of 160 ms length ([document_1.txt](document_1.txt)).

These transition segments are then modelled in two ways: (1) a baseline model based on hand-crafted features classified with a support vector machine (SVM), and (2) a CNN model using time-frequency representations as input, which is subsequently used for the transfer learning strategy ([document_1.txt](document_1.txt)). For the CNN branch, time-frequency representations based on the short-time Fourier transform (STFT) are computed with 256 frequency bins, a window length of 16 ms and a step-size of 4 ms, forming 41 time frames per transition; the spectrogram is then transformed into the Mel scale using 80 filters, producing an 80 × 41 spectrogram used to train the CNNs ([document_1.txt](document_1.txt)). This representation is generated identically across the three language datasets, which is what makes the cross-lingual weight initialisation technically feasible ([document_1.txt](document_1.txt)).

Finally, the study considers all speech exercises performed by participants for classification, and the final decision for each speaker is obtained by a majority voting strategy among the different speech exercises ([document_1.txt](document_1.txt)). The datasets are therefore used at two levels of granularity: the segment/utterance level for model training, and the speaker level for the final diagnostic decision.

## 6. How the Datasets Are Used in the Experiments

The experimental design is explicitly structured around the three datasets. The experiments are divided into two stages: first, the baseline and the CNN models are trained considering each language individually; then, the trained CNNs for each language are used as base models in the transfer learning strategy in order to improve accuracy in the other two languages ([document_1.txt](document_1.txt)).

### 6.1 Within-Language Results on Each Dataset

The results obtained for the baseline and the CNNs trained for each language individually reveal that dataset-specific behaviour differs markedly by language.

| Language | Model | Accuracy (%) | Sensitivity (%) | Specificity (%) | MCC |
|---|---|---|---|---|---|
| Spanish | Baseline | 73.7 (13.0) | 74.5 (16.7) | 77.1 (16.2) | 0.50 |
| Spanish | CNN | 71.0 (15.9) | 74.0 (25.0) | 68.0 (28.6) | 0.42 |
| German | Baseline | 69.3 (9.9) | 71.8 (12.4) | 68.7 (10.0) | 0.39 |
| German | CNN | 63.1 (11.7) | 43.1 (38.0) | 83.1 (17.7) | 0.30 |
| Czech | Baseline | 61.0 (12.5) | 64.5 (19.5) | 60.2 (11.9) | 0.27 |
| Czech | CNN | 68.5 (14.1) | 94.0 (13.5) | 42.0 (33.2) | 0.43 |

Adapted from ([document_1.txt](document_1.txt)).

Similar accuracies are obtained between the baseline and the CNN for Spanish, which also exhibits the highest accuracy among the three languages; the highest accuracy for German was obtained with the baseline model; conversely, for Czech the CNN produced the highest accuracy ([document_1.txt](document_1.txt)). The authors also note that for all three languages, the results are unbalanced towards one of the two classes according to the specificity and sensitivity values ([document_1.txt](document_1.txt)) — a pattern especially visible in the Czech CNN, with 94.0% sensitivity against 42.0% specificity ([document_1.txt](document_1.txt)).

### 6.2 Cross-Lingual Transfer Results Across the Datasets

The transfer learning stage uses a CNN trained with utterances from one dataset/language to fine-tune a model for a second language dataset.

| Base Language | Target Language | Accuracy (%) | Sensitivity (%) | Specificity (%) | MCC |
|---|---|---|---|---|---|
| German | Spanish | 70.0 (12.5) | 62.0 (19.9) | 78.0 (23.9) | 0.41 |
| Czech | Spanish | 72.0 (13.1) | 67.0 (11.6) | 78.0 (23.9) | 0.46 |
| Spanish | German | 77.3 (11.3) | 86.2 (13.8) | 68.3 (14.3) | 0.57 |
| Czech | German | 76.7 (7.9) | 87.5 (11.0) | 66.0 (15.6) | 0.55 |
| Spanish | Czech | 72.6 (13.9) | 82.0 (14.8) | 62.0 (28.9) | 0.46 |
| German | Czech | 70.7 (14.5) | 80.0 (16.3) | 62.5 (26.3) | 0.38 |

Adapted from ([document_1.txt](document_1.txt)).

The accuracy improved over 8% for German (from 69.3% in the baseline to 77.3% when fine-tuned from Spanish) and over 4.1% for Czech (from 68.5% with the initial CNN to 72.6% when fine-tuned from Spanish) ([document_1.txt](document_1.txt)). The highest accuracy for both German and Czech was obtained when the base language was Spanish, which the authors explain by noting that Spanish speakers have the best initial separability, so the other two languages benefit from the best initial model ([document_1.txt](document_1.txt)). The receiver operating characteristic analysis reinforces this: when the target is Spanish, the area under the curve is slightly higher when the base language is Czech, whereas for German and Czech targets the highest AUC is obtained when the base model is trained on Spanish utterances ([document_1.txt](document_1.txt)).

## 7. Strengths, Constraints, and Interpretive Caveats

The dataset design underlying this study has several notable strengths. It is genuinely multilingual and multi-corpus, spanning three distinct language families and three geographically and culturally distinct patient populations, while retaining a single clinical reference instrument (MDS-UPDRS-III) and a single recording standard (noise-controlled, 16 kHz) ([document_1.txt](document_1.txt)). Within each language, the PD and HC groups are matched in size — 50/50 for Spanish, 44/44 for German, and 50/50 for Czech — which supports interpretable sensitivity and specificity reporting ([document_2.txt](document_2.txt)).

The constraints are equally important to register. First, the speech elicitation protocols are not identical across languages: the Spanish protocol includes sustained vowels and multiple rapid syllable sequences that the Czech protocol does not, and the reading texts differ in length (36 words versus 80 words) ([document_1.txt](document_1.txt)). Cross-lingual transfer therefore confounds language differences with task differences to an unknown degree. Second, only the Spanish cohort's medication state is documented in the available material, where all patients were recorded in the ON state ([document_1.txt](document_1.txt)). Third, the German and Czech datasets' detailed composition (gender and time since diagnosis) is only referenced indirectly through Table 1, the contents of which are not available in the source material ([document_1.txt](document_1.txt)). Finally, the transfer strategy was only beneficial when the base model was sufficiently robust — observed specifically when the Spanish-trained model was used to initialise German and Czech models — meaning that dataset quality, not merely dataset availability, governs whether cross-lingual transfer helps ([document_1.txt](document_1.txt)).

A further consideration is that the authors themselves identify dataset expansion as future work: they plan to develop more robust base models using hyper-parameter optimisation such as Bayesian optimisation, to train base models on two languages instead of one, to evaluate classification of PD stages from the MDS-UPDRS-III score or dysarthria severity, and to extend transfer learning across diseases, for instance training a base model on PD utterances to initialize a model for Huntington's disease ([document_1.txt](document_1.txt)). This indicates that the current three-corpus configuration is regarded as a starting point rather than an endpoint.

## 8. Conclusion

The study uses three clinical speech datasets, one per language: the **Spanish PC-GITA corpus** (50 PD patients and 50 healthy controls, Colombian Spanish native speakers), **German speech recordings** (44 PD patients and 44 healthy controls), and **Czech speech recordings** (50 PD patients and 50 healthy controls) ([document_2.txt](document_2.txt)). Together these amount to approximately 144 PD patients and 144 healthy controls across 288 speakers ([document_2.txt](document_2.txt)). All three datasets were recorded under noise-controlled conditions, down-sampled to 16 kHz, and clinically assessed with the MDS-UPDRS-III in their respective patient groups ([document_1.txt](document_1.txt)). From these corpora, 160 ms voiced/unvoiced transition segments are extracted and converted into 80 × 41 Mel-scale spectrograms, which train per-language CNNs and serve as the basis for the cross-lingual transfer learning strategy that improved accuracy by up to approximately 8% when the robust Spanish-trained base model was transferred to German and Czech ([document_1.txt](document_1.txt)).

## References

document_1.txt. (n.d.). *Convolutional neural networks and a transfer learning strategy to classify Parkinson's disease from speech in three different languages* [Unpublished manuscript / source document]. Retrieved September 15, 2026, from [document_1.txt](document_1.txt)

document_2.txt. (n.d.). *Third-party research note: Convolutional neural networks and a transfer learning strategy to classify Parkinson's disease from speech in three different languages* [Research note]. Retrieved September 15, 2026, from [document_2.txt](document_2.txt)

Orozco-Arroyave, J. R., et al. (2014). New Spanish speech corpus database for the analysis of people suffering from Parkinson's disease. In *Proceedings of the Ninth International Conference on Language Resources and Evaluation* (pp. 342–347). [As cited in document_1.txt](document_1.txt)

Goetz, C. G., et al. (2008). Movement Disorder Society-sponsored revision of the Unified Parkinson's Disease Rating Scale (MDS-UPDRS): Scale presentation and clinimetric testing results. *Movement Disorders, 23*(15), 2129–2170. [As cited in document_1.txt](document_1.txt)

Rusz, J. (n.d.). [Czech Parkinsonian speech corpus]. [As cited in document_1.txt](document_1.txt)

Sakar, B. E., et al. (2013). Collection and analysis of a Parkinson speech dataset with multiple types of sound recordings. *IEEE Journal of Biomedical and Health Informatics, 17*(4), 828–834. [As cited in document_1.txt](document_1.txt)