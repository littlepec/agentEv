# Datasets Used in the Cross-Lingual Parkinson's Disease Speech Classification Study

## Introduction

The study under review proposes a methodology for classifying Parkinson's disease (PD) from speech in three different languages — Spanish, German, and Czech — by combining convolutional neural networks (CNNs) trained on time–frequency representations with a cross-lingual transfer learning strategy ([Vasquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)). Because the central contribution of the work is the extent to which knowledge learned from one language's speech data can be transferred to another, the datasets occupy a defining role in the research design. This report identifies and describes, in detail, the datasets used in the study, including their speaker composition, demographic and clinical characteristics, speech tasks, recording and preprocessing conditions, and the way each dataset was partitioned and employed in the baseline, individual-language CNN, and transfer learning experiments. Where the available sources conflict, the discrepancy is explicitly flagged and assessed.

The study relies on three language-specific speech corpora: the PC-GITA corpus for Colombian Spanish, a German speech corpus of PD patients and healthy controls, and a Czech speech corpus of native Czech speakers ([Vasquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374); [Third-party research note, n.d.](document_2.txt)). Together, these corpora supply the recordings of PD patients and healthy control (HC) speakers that form the dataset base for all experiments.

## Overview of the Three Speech Datasets

The three datasets are independent, language-specific collections rather than a single merged corpus. Each was collected in noise-controlled conditions, and each contains recordings from both PD patients and healthy controls who are native speakers of the respective language ([Vasquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)). Table 1 summarizes the inventory.

**Table 1. Inventory of datasets used in the study**

| Language | Corpus / Source | PD speakers | HC speakers | Total speakers | Native speakers of | Source reference in paper |
|---|---|---|---|---|---|---|
| Spanish | PC-GITA corpus | 50 | 50 | 100 | Colombian Spanish | Orozco-Arroyave et al. (2014) |
| German | German speech recordings | 88 | 88 | 176 | German | Skodda, Visser, & Schlegel (2011) |
| Czech | Czech speech recordings | 50 | 50 | 100 | Czech | Rusz (2018) |

*Note.* Compiled from the dataset description provided in the study ([Vasquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)). A third-party research note reports the German dataset as 44 PD and 44 HC speakers ([Third-party research note, n.d.](document_2.txt)); the primary study reports 88 PD and 88 HC, a discrepancy discussed later in this report.

### The Spanish Dataset: PC-GITA

The Spanish portion of the data is drawn from the PC-GITA corpus, which the study describes as containing utterances from 50 PD patients and 50 HC speakers who are Colombian Spanish native speakers ([Vasquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374); [Third-party research note, n.d.](document_2.txt)). The corpus was originally introduced by Orozco-Arroyave and colleagues as a Spanish speech corpus database for the analysis of people suffering from Parkinson's disease ([Vasquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)). The Spanish participants were asked to produce a relatively rich set of speech material: a total of 10 sentences, rapid repetition of the syllable sequences /pa-ta-ka/, /pe-ta-ka/, /pa-ka-ta/, as well as sustained /pa/, /ta/, and /ka/, one text containing 36 words, and a monologue ([Vasquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)). An important clinical detail is that all Spanish PD patients were recorded in the ON state, that is, under the effect of their daily medication ([Vasquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)).

The gender distribution of the Spanish group is balanced: 25 male and 25 female PD patients, and 25 male and 25 female healthy controls ([Vasquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)). Age ranges span 33–81 years for male PD patients, 49–75 years for female PD patients, 31–86 years for male controls, and 49–76 years for female controls, with mean ages around 60.7 years (SD = 7.3) for male PD patients and 61.4 years (SD = 7.0) for female PD patients ([Vasquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)). Clinically, the Spanish cohort exhibits the highest disease severity of the three groups, with mean MDS-UPDRS-III scores of 37.8 (SD = 22.1) for men and 37.6 (SD = 14.1) for women, and mean time since diagnosis of 8.7 years (SD = 5.9) for men and 12.6 years (SD = 11.6) for women ([Vasquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)).

### The German Dataset

The German data consist of speech recordings of PD patients and healthy control speakers from Germany ([Vasquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)). The primary study reports 88 PD patients and 88 HC speakers, citing Skodda, Visser, and Schlegel's work on vowel articulation in Parkinson's disease as the underlying source ([Vasquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)). The German participants performed four speech tasks: rapid repetition of /pa-ta-ka/, five sentences, one text with 81 words, and a monologue ([Vasquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)).

According to the demographic table in the study, the German PD group comprises 41 male and 47 female patients, while the German control group comprises 44 male and 44 female speakers; these figures sum to 88 PD patients and 88 controls, which is internally consistent with the stated totals ([Vasquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)). Age ranges are 42–84 years for male PD patients, 44–82 years for female PD patients, 26–83 years for male controls, and 28–85 years for female controls. Mean ages are reported as 66.2 years (SD = 9.7) for male PD patients and 62.6 years (SD = 15.2) for female PD patients. Mean time since diagnosis is 7.1 years (SD = 6.2) for men and 7.0 years (SD = 5.5) for women, and mean MDS-UPDRS-III scores are 22.1 (SD = 9.9) for men and 23.3 (SD = 12.0) for women ([Vasquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)).

### The Czech Dataset

The Czech dataset contains a total of 100 native Czech speakers, comprising 50 PD patients and 50 healthy controls ([Vasquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374); [Third-party research note, n.d.](document_2.txt)). The study attributes this corpus to Rusz's habilitation thesis on detecting speech disorders in early Parkinson's disease by acoustic analysis ([Vasquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)). The Czech speakers performed three speech tasks: rapid repetition of the syllables /pa-ta-ka/, a read text with 80 words, and a monologue ([Vasquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)).

The Czech PD group consists of 20 male and 30 female patients, while the control group consists of 30 male and 20 female speakers ([Vasquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)). Age ranges are 43–82 years for male PD patients, 41–72 years for female PD patients, 41–77 years for male controls, and 40–79 years for female controls. Mean ages are reported as 60.1 years (SD = 8.7) for male PD patients and 63.5 years (SD = 11.1) for female PD patients. Mean time since diagnosis is 6.8 years (SD = 5.2) for men and 6.7 years (SD = 4.5) for women, and mean MDS-UPDRS-III scores are 21.4 (SD = 11.5) for men and 18.1 (SD = 9.7) for women ([Vasquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)).

## Demographic and Clinical Characterization

Table 2 consolidates the available demographic and clinical information. The patients in all three datasets were evaluated by an expert neurologist according to the third section of the Movement Disorder Society–sponsored revision of the Unified Parkinson's Disease Rating Scale (MDS-UPDRS-III), which provides a common clinical anchor across languages ([Vasquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374); [Third-party research note, n.d.](document_2.txt)).

**Table 2. Demographic and clinical profile of the three datasets**

| Group | N (M/F) | Age range (M; F) | Mean age (M; F) | Time since diagnosis, years (M; F) | MDS-UPDRS-III (M; F) |
|---|---|---|---|---|---|
| Spanish PD | 50 (25/25) | 33–81; 49–75 | 60.7 (7.3); 61.4 (7.0) | 8.7 (5.9); 12.6 (11.6) | 37.8 (22.1); 37.6 (14.1) |
| Spanish HC | 50 (25/25) | 31–86; 49–76 | Not reported | — | — |
| German PD | 88 (41/47) | 42–84; 44–82 | 66.2 (9.7); 62.6 (15.2) | 7.1 (6.2); 7.0 (5.5) | 22.1 (9.9); 23.3 (12.0) |
| German HC | 88 (44/44) | 26–83; 28–85 | Not reported | — | — |
| Czech PD | 50 (20/30) | 43–82; 41–72 | 60.1 (8.7); 63.5 (11.1) | 6.8 (5.2); 6.7 (4.5) | 21.4 (11.5); 18.1 (9.7) |
| Czech HC | 50 (30/20) | 41–77; 40–79 | Not reported | — | — |

*Note.* Values in parentheses are standard deviations. M = male, F = female. Compiled from the speaker information table and accompanying text in the study ([Vasquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)).

A clinically salient pattern emerges from Table 2: the Spanish patients have substantially higher MDS-UPDRS-III scores than the German and Czech patients, indicating greater disease severity in the Spanish cohort ([Vasquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)). The study itself uses this observation to explain why the highest classification accuracy was obtained for Spanish and why the Spanish-trained model served as the most effective base model for transfer to the other two languages ([Vasquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)). In my assessment, this severity imbalance is a genuine confound for cross-lingual comparisons: differences in classification performance between languages cannot be attributed purely to linguistic factors, because the Spanish data also present an easier discrimination problem due to more advanced disease.

## Speech Tasks and Recording Protocols

The speech tasks differ across the three datasets, which is relevant because the classification pipeline ultimately aggregates decisions across exercises. Table 3 summarizes the tasks per language.

**Table 3. Speech tasks performed by participants in each dataset**

| Language | Speech tasks |
|---|---|
| Spanish (PC-GITA) | 10 sentences; rapid repetition of /pa-ta-ka/, /pe-ta-ka/, /pa-ka-ta/; sustained /pa/, /ta/, /ka/; one text with 36 words; one monologue |
| German | Rapid repetition of /pa-ta-ka/; 5 sentences; one text with 81 words; one monologue |
| Czech | Rapid repetition of syllables /pa-ta-ka/; a read text with 80 words; one monologue |

*Note.* Compiled from the data description in the study ([Vasquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)).

All recordings in all three datasets were captured under noise-controlled conditions, and the speech signals were down-sampled to 16 kHz ([Vasquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)). This uniform sampling rate is an important harmonization step: it ensures that the subsequent time–frequency representations, computed with identical parameters across languages, are comparable in terms of frequency resolution and frame timing.

## Preprocessing and Segmentation of the Datasets

The datasets were not fed to the classifiers as raw continuous speech. Instead, the speech signals were analyzed based on the automatic detection of onset and offset transitions, which model the difficulty PD patients experience in starting and stopping the movement of the vocal folds ([Vasquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)). The detection of these transitions relies on the presence of the fundamental frequency of speech in short-time frames. Once the border between voiced and unvoiced frames is detected, 80 ms of signal is taken to the left and to the right, forming segments of 160 ms in length ([Vasquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)). These transition segments constitute the actual modeling units for both the baseline and the CNN pipelines.

Two parallel modeling routes were applied to the same segmented data. The baseline model extracted hand-crafted features consisting of 12 Mel-Frequency Cepstral Coefficients (MFCCs) with their first and second derivatives, plus the log energy of the signal distributed into 22 Bark bands, yielding 58 descriptors; four statistical functionals (mean, standard deviation, skewness, and kurtosis) were computed for each descriptor, producing a 232-dimensional feature vector per utterance ([Vasquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)). Classification was performed with a radial basis function SVM (margin parameter C = 10, Gaussian kernel parameter 0.0001) evaluated under a speaker-independent 10-fold cross-validation strategy ([Vasquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)).

The CNN route used time–frequency representations based on the short-time Fourier transform (STFT) with 256 frequency bins, a window length of 16 ms, and a step size of 4 ms, forming 41 time frames per transition; the spectrogram was then transformed into the Mel scale using 80 filters, producing an 80 × 41 input representation ([Vasquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)). The CNN architecture consists of four convolutional and max-pooling layers, dropout regularization, two fully connected layers, and a softmax output layer, trained with cross-entropy loss and an Adam optimizer ([Vasquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)).

## How the Datasets Were Used in the Experiments

The experimental protocol treated each language dataset in two ways. First, the baseline SVM and the CNN were trained separately for each language, providing within-language benchmarks ([Vasquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)). Second, the trained CNN for each language was used as a base model to initialize and fine-tune models for the remaining two languages — the core cross-lingual transfer learning design ([Vasquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)). All speech exercises performed by the participants were considered for the classification strategy, and the final decision for each speaker was obtained by majority voting across the different speech exercises ([Vasquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)). This speaker-level aggregation is methodologically important because it aligns the unit of prediction with the unit of clinical interest (the speaker) rather than the individual utterance.

The transfer learning results indicated that accuracy improved considerably when German and Czech were the target languages. Accuracy improved by over 8% for German (from 69.3% in the baseline to 77.3% when fine-tuned from Spanish) and by over 4.1% for Czech (from 68.5% with the initial CNN to 72.6% when fine-tuned from Spanish) ([Vasquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)). The highest accuracy for German and Czech was obtained when Spanish was the base language, which the authors attribute to Spanish speakers having the best initial separability ([Vasquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)). The reported ROC analyses show area-under-the-curve values of 0.823 for the Spanish-to-German transfer, 0.831 for the Spanish-to-Czech transfer, and 0.792 for the Czech-to-German transfer, compared with 0.584 for the German-only CNN ([Vasquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)).

## Data Reliability, Discrepancies, and Limitations

Two issues deserve attention. First, there is an explicit inconsistency regarding the German dataset size: the primary study reports 88 PD patients and 88 HC speakers, consistent with the gender breakdown in its own speaker table (41 + 47 = 88 PD; 44 + 44 = 88 HC), whereas the third-party research note states that the German data consist of 44 PD patients and 44 HC speakers ([Vasquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374); [Third-party research note, n.d.](document_2.txt)). Given the internal consistency of the primary source's table and its explicit textual statement, the 88/88 figure should be treated as the more reliable one, and the 44/44 figure in the secondary note appears to be an error. Second, several numeric fields in the provided text — particularly the within-language classification table and parts of the ROC figure captions — are partially garbled by optical character recognition, so exact baseline values for Spanish and some AUC labels cannot be recovered with certainty from the available material ([Vasquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)). These are limitations of the source text rather than of the underlying study.

From a design standpoint, the most significant limitation is the lack of matching disease severity and demographic balance across the three datasets. The Spanish cohort is older in terms of time since diagnosis and markedly more severe on the MDS-UPDRS-III than the German and Czech cohorts, and the German dataset is nearly twice the size of the other two ([Vasquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)). Consequently, cross-lingual transfer gains may partly reflect the transfer of a decision boundary learned from a more separable clinical population, not purely the transferability of acoustic–phonetic markers of dysarthria. Future work proposed by the authors — training base models with two languages instead of one, applying Bayesian hyper-parameter optimization, and extending transfer learning across diseases such as Huntington's disease — would help disentangle these factors ([Vasquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)).

## Conclusion

The study is built on three language-specific speech datasets: the PC-GITA corpus of Colombian Spanish (50 PD, 50 HC), a German corpus here reported as comprising 88 PD and 88 HC speakers, and a Czech corpus of 50 PD and 50 HC native speakers ([Vasquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374); [Third-party research note, n.d.](document_2.txt)). Each dataset pairs PD patients with healthy controls, was recorded under noise-controlled conditions at 16 kHz, and includes read, repetition, and monologue tasks, with all patients clinically rated via MDS-UPDRS-III. The datasets were segmented into 160 ms voiced–unvoiced transition windows, modeled both with hand-crafted MFCC/Bark-energy features and with Mel-scale spectrograms feeding a CNN, and then combined through a cross-lingual transfer learning scheme in which one language's trained model initializes classifiers for the other two ([Vasquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)). My assessment is that the three-corpus design is a genuine methodological strength for studying language robustness in pathological speech analysis, but the severity and size imbalance across the corpora means the reported cross-lingual improvements should be interpreted as promising rather than conclusive until balanced, severity-matched replication is performed. Resolving the German speaker-count discrepancy between the primary and secondary sources is a necessary first step for any such replication.

## References

Third-party research note: Convolutional neural networks and a transfer learning strategy to classify Parkinson's disease from speech in three different languages. (n.d.). *document_2.txt*.

Vasquez-Correa, J. C., Arias-Vergara, T., Rios-Urrego, C. D., Schuster, M., Rusz, J., Orozco-Arroyave, J. R., & Nöth, E. (2020). *Convolutional neural networks and a transfer learning strategy to classify Parkinson's disease from speech in three different languages* (arXiv:2002.04374). https://arxiv.org/abs/2002.04374