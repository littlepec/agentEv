# Datasets Used in Parkinson's Disease Speech Classification Across Three Languages

## Introduction

The study by Vásquez-Correa et al. (n.d.) investigates the classification of Parkinson's disease (PD) from speech using convolutional neural networks (CNNs) and a transfer learning strategy across three languages: Spanish, German, and Czech. The core of this investigation rests on three distinct speech datasets, each corresponding to one of the target languages. These datasets provide the recordings of PD patients and healthy control (HC) speakers that are necessary to train, validate, and test the proposed models. The present report details the datasets used in the study, including their composition, the speech tasks performed by participants, the clinical evaluations conducted, and the preprocessing steps applied before analysis ([Vásquez-Correa et al., n.d.](document_1.txt)).

## Overview of the Three Datasets

The study considers speech recordings from three different languages: Spanish, German, and Czech. All recordings were captured under noise-controlled conditions, and the speech signals were down-sampled to 16 kHz ([Vásquez-Correa et al., n.d.](document_1.txt)). The patients in all three datasets were evaluated by a neurologist expert according to the third section of the Movement Disorder Society's Unified Parkinson's Disease Rating Scale (MDS-UPDRS-III) ([Vásquez-Correa et al., n.d.](document_1.txt)). Table 1 provides a comparative summary of the three datasets, including speaker counts, native languages, and the source references provided in the primary document. Note that a third-party research note reports different speaker counts for the German dataset; this discrepancy is discussed in the relevant section below ([Third-party research note, n.d.](document_2.txt)).

| Language | Dataset / Source | PD Speakers | HC Speakers | Native Speakers | Primary Reference |
|----------|------------------|-------------|-------------|-----------------|-------------------|
| Spanish  | PC-GITA corpus   | 50          | 50          | Colombian Spanish | [6] |
| German   | German speech recordings | 88 (primary) / 44 (third-party note) | 88 (primary) / 44 (third-party note) | German | [18] |
| Czech    | Czech speech recordings | 50          | 50          | Czech | [19] |

*Table 1. Summary of datasets used in the study. Speaker counts for German reflect a discrepancy between the primary source ([Vásquez-Correa et al., n.d.](document_1.txt)) and a third-party research note ([Third-party research note, n.d.](document_2.txt)).*

## Spanish Dataset: PC-GITA Corpus

### Composition and Speakers
The Spanish data come from the PC-GITA corpus, which contains utterances from 50 PD patients and 50 HC speakers who are Colombian Spanish native speakers ([Vásquez-Correa et al., n.d.](document_1.txt)). The third-party research note confirms this composition, stating that the Spanish dataset speaker composition is 50 PD patients and 50 healthy control speakers, Colombian Spanish native speakers, and that this corpus provides the Spanish portion of the cross-lingual speech data ([Third-party research note, n.d.](document_2.txt)). The balanced design—equal numbers of PD and HC speakers—supports comparative analyses of speech impairments associated with PD.

### Speech Tasks
Participants in the Spanish dataset were asked to produce a variety of speech tasks. These included pronouncing a total of 10 sentences, the rapid repetition of syllables /pa-ta-ka/, /pe-ta-ka/, /pa-ka-ta/, /pa/, /ta/, and /ka/, one text with 36 words, and a monologue ([Vásquez-Correa et al., n.d.](document_1.txt)). This range of tasks allows for the assessment of different aspects of speech production, including articulation, prosody, and connected speech.

### Clinical Evaluation
All Spanish-speaking patients were in the ON state at the time of the recording, meaning they were under the effect of their daily medication ([Vásquez-Correa et al., n.d.](document_1.txt)). They were evaluated by a neurologist expert according to the MDS-UPDRS-III ([Vásquez-Correa et al., n.d.](document_1.txt)). The average MDS-UPDRS-III score for the Spanish patients is reported to be higher compared with the German and Czech patients, indicating a higher disease severity in the Spanish data ([Vásquez-Correa et al., n.d.](document_1.txt)). This severity difference is relevant because it may influence the initial separability of the classes and, consequently, the performance of the transfer learning strategy.

## German Dataset

### Composition and Speakers
The German dataset consists of speech recordings from Germany. The primary source states that speech recordings of 88 PD patients and 88 HC speakers from Germany are considered ([Vásquez-Correa et al., n.d.](document_1.txt)). However, a third-party research note reports that the German data consist of speech recordings of 44 PD patients and 44 HC speakers, and that the German dataset description reports this composition ([Third-party research note, n.d.](document_2.txt)). This discrepancy is noteworthy. The primary source is the original research paper, whereas the third-party note is a secondary summary. In this report, both figures are presented to reflect the available information, but the primary source's figure of 88 PD and 88 HC speakers is treated as the more authoritative description of the dataset used in the study. The balanced design (equal PD and HC) is consistent across both accounts.

### Speech Tasks
German participants performed four speech tasks: the rapid repetition of /pa-ta-ka/, five sentences, one text with 81 words, and a monologue ([Vásquez-Correa et al., n.d.](document_1.txt)). These tasks are similar in nature to those in the Spanish and Czech datasets, although the specific sentence counts and text lengths vary, reflecting language-specific materials.

### Clinical Evaluation
As with the other datasets, the German patients were evaluated by a neurologist expert using the MDS-UPDRS-III ([Vásquez-Correa et al., n.d.](document_1.txt)). The primary source notes that the average MDS-UPDRS-III score for German patients is lower than that of the Spanish patients, indicating a lower average disease severity ([Vásquez-Correa et al., n.d.](document_1.txt)). This is an important factor in the cross-lingual transfer learning experiments, as the initial model's robustness can be affected by the severity distribution in the source dataset.

## Czech Dataset

### Composition and Speakers
The Czech dataset comprises a total of 100 native Czech speakers, with 50 PD patients and 50 HC speakers ([Vásquez-Correa et al., n.d.](document_1.txt)). The third-party research note also confirms this composition: the Czech dataset contains 50 PD patients and 50 healthy controls ([Third-party research note, n.d.](document_2.txt)). This dataset is referenced as [19] in the primary source, which corresponds to a habilitation thesis by J. Rusz (2018) on detecting speech disorders in early Parkinson's disease by acoustic analysis ([Vásquez-Correa et al., n.d.](document_1.txt)).

### Speech Tasks
The Czech participants performed the rapid repetition of the syllables /pa-ta-ka/, a read text with 80 words, and a monologue ([Vásquez-Correa et al., n.d.](document_1.txt)). The inclusion of a monologue and a read text allows for the analysis of continuous speech, while the rapid syllable repetition targets articulatory precision.

### Clinical Evaluation
The Czech patients were also evaluated with the MDS-UPDRS-III ([Vásquez-Correa et al., n.d.](document_1.txt)). The average MDS-UPDRS-III score for Czech patients is reported to be lower than that of the Spanish patients, similar to the German patients ([Vásquez-Correa et al., n.d.](document_1.txt)). This pattern of disease severity across languages is mentioned as an explanation for differences in classification results among the three languages.

## Data Acquisition and Preprocessing

All speech recordings in the three datasets were captured in noise-controlled conditions, and the signals were down-sampled to 16 kHz ([Vásquez-Correa et al., n.d.](document_1.txt)). The analysis focuses on the automatic detection of onset and offset transitions, which model the difficulties of PD patients in starting and stopping the movement of the vocal folds ([Vásquez-Correa et al., n.d.](document_1.txt)). The detection of transitions is based on the presence of the fundamental frequency of speech in short-time frames; the border between voiced and unvoiced frames is detected, and 80 ms of the signal are taken to the left and to the right, forming segments with 160 ms length ([Vásquez-Correa et al., n.d.](document_1.txt)). These transition segments are then modeled using two approaches: (1) a baseline model based on hand-crafted features classified with an SVM, and (2) a model based on time-frequency representations used to train a CNN for transfer learning ([Vásquez-Correa et al., n.d.](document_1.txt)).

For the baseline model, features extracted from the transitions include 12 Mel-Frequency Cepstral Coefficients (MFCCs) with their first and second derivatives, and the log energy of the signal distributed into 22 Bark bands, totaling 58 descriptors ([Vásquez-Correa et al., n.d.](document_1.txt)). Four statistical functionals (mean, standard deviation, skewness, and kurtosis) are computed for each descriptor, resulting in a 232-dimensional feature vector per utterance ([Vásquez-Correa et al., n.d.](document_1.txt)). The classification is performed with a radial basis SVM with a margin parameter C=10 and a Gaussian kernel with parameter γ=0.0001, tested with a 10-fold cross-validation strategy that is speaker independent ([Vásquez-Correa et al., n.d.](document_1.txt)).

For the CNN model, time-frequency representations based on the short-time Fourier transform (STFT) are used. The STFT with 256 frequency bins is computed for each segmented transition, using a window length of 16 ms and a step-size of 4 ms, forming 41 time frames per transition ([Vásquez-Correa et al., n.d.](document_1.txt)). The obtained spectrogram is transformed into the Mel scale using 80 filters, forming a spectrogram of size 80 × 41, which is used to train the CNNs ([Vásquez-Correa et al., n.d.](document_1.txt)). This preprocessing pipeline is applied consistently across the three language datasets, enabling cross-lingual experiments.

## Role of the Datasets in the Transfer Learning Strategy

The three datasets are not only used for within-language classification but also serve as the basis for a transfer learning strategy among languages. The CNN architecture is first trained with utterances from one language (the base language), and the pre-trained model is then used to initialize models for the remaining languages (the target languages) ([Vásquez-Correa et al., n.d.](document_1.txt)). This procedure aims to improve the accuracy of the models when the weights of the neural network are initialized with utterances from a different language than the one used for the test set ([Vásquez-Correa et al., n.d.](document_1.txt)).

The results indicate that the transfer learning strategy improved the accuracy of the models by up to 8% when the base model used to initialize the weights of the classifier is robust enough ([Vásquez-Correa et al., n.d.](document_1.txt)). Specifically, the accuracy improved over 8% for German (from 69.3% in the baseline to 77.3% when fine-tuned from Spanish) and over 4.1% for Czech (from 68.5% with the initial CNN to 72.6% when fine-tuned from Spanish) ([Vásquez-Correa et al., n.d.](document_1.txt)). The highest accuracy for German and Czech was obtained when the base language was Spanish, which is explained by the Spanish speakers having the best initial separability, thus providing the best initial model for the other languages ([Vásquez-Correa et al., n.d.](document_1.txt)). The results after transfer learning were also more balanced in terms of specificity and sensitivity, and had lower variance, leading to improved generalization ([Vásquez-Correa et al., n.d.](document_1.txt)).

## Summary Table of Dataset Characteristics

Table 2 provides a detailed comparison of the speech tasks and clinical evaluations across the three datasets.

| Characteristic | Spanish (PC-GITA) | German | Czech |
|----------------|-------------------|--------|-------|
| PD speakers | 50 | 88 (primary) / 44 (third-party note) | 50 |
| HC speakers | 50 | 88 (primary) / 44 (third-party note) | 50 |
| Native language | Colombian Spanish | German | Czech |
| Speech tasks | 10 sentences, rapid repetition of /pa-ta-ka/, /pe-ta-ka/, /pa-ka-ta/, /pa/, /ta/, /ka/, 36-word text, monologue | Rapid repetition of /pa-ta-ka/, 5 sentences, 81-word text, monologue | Rapid repetition of /pa-ta-ka/, 80-word read text, monologue |
| Clinical scale | MDS-UPDRS-III | MDS-UPDRS-III | MDS-UPDRS-III |
| Medication state | ON state | Not specified | Not specified |
| Source reference | [6] | [18] | [19] |

*Table 2. Detailed characteristics of the three datasets used in the study ([Vásquez-Correa et al., n.d.](document_1.txt); [Third-party research note, n.d.](document_2.txt)).*

## Discussion and Conclusion

The study by Vásquez-Correa et al. (n.d.) utilizes three language-specific speech datasets: the PC-GITA corpus for Spanish, a German speech dataset, and a Czech speech dataset. Each dataset comprises recordings from PD patients and healthy controls, with balanced designs (equal numbers of PD and HC speakers in all cases). The Spanish dataset is clearly defined as the PC-GITA corpus with 50 PD and 50 HC speakers, a composition corroborated by the third-party research note ([Third-party research note, n.d.](document_2.txt)). The Czech dataset is consistently reported as 100 native Czech speakers, split evenly between 50 PD patients and 50 HC speakers ([Vásquez-Correa et al., n.d.](document_1.txt); [Third-party research note, n.d.](document_2.txt)). The German dataset, however, presents a discrepancy: the primary source reports 88 PD and 88 HC speakers, while the third-party note reports 44 PD and 44 HC speakers ([Vásquez-Correa et al., n.d.](document_1.txt); [Third-party research note, n.d.](document_2.txt)). This report has highlighted both figures without resolving the discrepancy, as the available information does not permit a definitive conclusion. Researchers using this study should be aware of this inconsistency and consult the original German data source [18] for confirmation.

The datasets are central to the study's methodology. They provide the speech material for training and testing both the baseline SVM model and the CNN model. They also enable the cross-lingual transfer learning experiments, which demonstrate that a robust base model trained on Spanish data can improve classification accuracy in German and Czech. The use of multiple languages addresses the challenge of linguistic bias in speech-based PD classification and demonstrates the potential of transfer learning to leverage data from one language to improve performance in another.

In conclusion, the datasets used in this study are the PC-GITA corpus (Spanish), German speech recordings, and Czech speech recordings. They are characterized by balanced PD/HC speaker groups, clinically evaluated participants, and a common set of speech tasks that include sustained phonation, rapid syllable repetition, read text, and monologue. These datasets form a valuable resource for investigating cross-lingual and transfer learning approaches to Parkinson's disease classification from speech.

## References

Vásquez-Correa, J. C., Arias-Vergara, T., Rios-Urrego, C. D., Schuster, M., Rusz, J., & Orozco-Arroyave, J. R. (n.d.). *Convolutional neural networks and a transfer learning strategy to classify Parkinson’s disease from speech in three different languages*. document_1.txt.

Third-party research note. (n.d.). *Convolutional neural networks and a transfer learning strategy to classify Parkinson's disease from speech in three different languages*. document_2.txt.