# Datasets Used in “Convolutional Neural Networks and a Transfer Learning Strategy to Classify Parkinson’s Disease from Speech in Three Different Languages”

## Introduction

The study under review investigates the automatic classification of Parkinson’s disease (PD) from speech using convolutional neural networks (CNNs) and a cross-lingual transfer learning strategy ([Vásquez-Correa et al., 2020](document_1.txt)). The primary research question concerns whether CNNs trained on time-frequency representations of speech transitions can be fine-tuned across languages to improve diagnostic accuracy ([Vásquez-Correa et al., 2020](document_1.txt)). To answer this question, the authors assembled and analyzed speech recordings from patients and healthy controls (HC) in three languages: Spanish, German, and Czech ([Vásquez-Correa et al., 2020](document_1.txt)). A secondary third-party research note also describes the datasets but contains a factual error regarding the languages used ([Third-party research note, n.d.](document_2.txt)). This report provides a detailed, source-critical account of the datasets, their composition, speech tasks, clinical evaluations, and preprocessing steps.

## Primary Source and Reliability

The primary source for this report is the original paper by Vásquez-Correa et al. (2020), which explicitly states that the three languages are Spanish, German, and Czech ([Vásquez-Correa et al., 2020](document_1.txt)). The secondary source, a third-party research note, incorrectly claims that the study uses “Spanish, Italian, and Czech” ([Third-party research note, n.d.](document_2.txt)). Because the primary paper is the original scientific report and repeatedly names German rather than Italian, the present report treats the German dataset as the correct one and identifies the secondary note’s “Italian” reference as an error ([Vásquez-Correa et al., 2020](document_1.txt); [Third-party research note, n.d.](document_2.txt)). This discrepancy is important for any downstream use of the data, as it could lead to misidentification of the corpus.

## Overview of the Three Datasets

The study considers three language-specific datasets: PC-GITA for Spanish, a German dataset from Skodda et al. (2011), and a Czech dataset from Rusz (2018) ([Vásquez-Correa et al., 2020](document_1.txt)). All recordings were captured under noise-controlled conditions, and all speech signals were down-sampled to 16 kHz ([Vásquez-Correa et al., 2020](document_1.txt)). Patients in all three datasets were evaluated by a neurologist expert using the third section of the Movement Disorder Society–sponsored revision of the Unified Parkinson’s Disease Rating Scale (MDS-UPDRS-III) ([Vásquez-Correa et al., 2020](document_1.txt)). The datasets therefore combine acoustic speech data with clinical severity scores, enabling both classification and severity-related analyses.

### Spanish Dataset: PC-GITA Corpus

The Spanish data come from the PC-GITA corpus, which contains utterances from 50 PD patients and 50 healthy control speakers, all Colombian Spanish native speakers ([Vásquez-Correa et al., 2020](document_1.txt)). The speaker composition is balanced by gender: 25 male PD patients, 25 female PD patients, 25 male HC, and 25 female HC ([Vásquez-Correa et al., 2020](document_1.txt)). All patients were in the ON state at the time of recording, meaning they were under the effect of their daily medication ([Vásquez-Correa et al., 2020](document_1.txt)). The speech tasks for the Spanish participants included ten sentences, the rapid repetition of /pa-ta-ka/, /pe-ta-ka/, /pa-ka-ta/, /pa/, /ta/, and /ka/, one text with 36 words, and a monologue ([Vásquez-Correa et al., 2020](document_1.txt)). This set of tasks is broader than those of the German and Czech datasets, providing multiple contexts for assessing articulatory and phonatory impairments ([Vásquez-Correa et al., 2020](document_1.txt)).

### German Dataset

The German dataset consists of speech recordings from 88 PD patients and 88 HC speakers from Germany ([Vásquez-Correa et al., 2020](document_1.txt)). The gender distribution is 47 male PD patients, 41 female PD patients, 44 male HC, and 44 female HC ([Vásquez-Correa et al., 2020](document_1.txt)). Participants performed four speech tasks: the rapid repetition of /pa-ta-ka/, five sentences, one text with 81 words, and a monologue ([Vásquez-Correa et al., 2020](document_1.txt)). The German data are sourced from Skodda et al. (2011), a study on vowel articulation in Parkinson’s disease ([Vásquez-Correa et al., 2020](document_1.txt)). This dataset is the largest in terms of total speakers among the three languages, with 176 participants overall ([Vásquez-Correa et al., 2020](document_1.txt)). It is important to reiterate that the secondary note mislabels this dataset as Italian, although the speaker counts (88 PD and 88 HC) match the German data exactly ([Third-party research note, n.d.](document_2.txt); [Vásquez-Correa et al., 2020](document_1.txt)).

### Czech Dataset

The Czech dataset comprises a total of 100 native Czech speakers, with 50 PD patients and 50 healthy controls ([Vásquez-Correa et al., 2020](document_1.txt)). The gender split is 30 male PD patients, 20 female PD patients, 30 male HC, and 20 female HC ([Vásquez-Correa et al., 2020](document_1.txt)). The speech tasks include the rapid repetition of the syllables /pa-ta-ka/, a read text with 80 words, and a monologue ([Vásquez-Correa et al., 2020](document_1.txt)). The Czech data are attributed to Rusz (2018), a habilitation thesis on detecting speech disorders in early Parkinson’s disease by acoustic analysis ([Vásquez-Correa et al., 2020](document_1.txt)). This dataset provides a balanced number of PD and HC speakers, similar to the Spanish dataset, but with a different distribution of speech tasks and a different gender composition ([Vásquez-Correa et al., 2020](document_1.txt)).

## Speaker Demographics and Clinical Characteristics

Table 1 summarizes the speaker counts and gender distribution for all three datasets. These numbers are taken directly from Table 1 of the primary paper ([Vásquez-Correa et al., 2020](document_1.txt)). The Spanish and Czech datasets each contain 50 PD patients and 50 HC, whereas the German dataset contains 88 PD patients and 88 HC ([Vásquez-Correa et al., 2020](document_1.txt)). This imbalance in sample size across languages is relevant for the transfer learning experiments, because the German dataset offers more training examples than the Spanish and Czech datasets ([Vásquez-Correa et al., 2020](document_1.txt)).

| Language | Group | Total N | Male | Female |
|----------|-------|---------|------|--------|
| Spanish  | PD    | 50      | 25   | 25     |
| Spanish  | HC    | 50      | 25   | 25     |
| German   | PD    | 88      | 47   | 41     |
| German   | HC    | 88      | 44   | 44     |
| Czech    | PD    | 50      | 30   | 20     |
| Czech    | HC    | 50      | 30   | 20     |

*Note.* Data from Table 1 in Vásquez-Correa et al. (2020) ([Vásquez-Correa et al., 2020](document_1.txt)).

Table 2 presents age, time since diagnosis, and MDS-UPDRS-III scores. The Spanish PD group has the highest mean MDS-UPDRS-III scores (37.8 for males and 37.6 for females), indicating greater disease severity compared with the German and Czech PD groups ([Vásquez-Correa et al., 2020](document_1.txt)). The German PD group has mean scores of 22.1 (male) and 23.3 (female), while the Czech PD group has mean scores of 21.4 (male) and 18.1 (female) ([Vásquez-Correa et al., 2020](document_1.txt)). These clinical differences are important because the authors suggest they may explain why the Spanish model exhibits the best initial separability and serves as the strongest base model for transfer learning ([Vásquez-Correa et al., 2020](document_1.txt)).

| Language | Group | Mean age male (SD) | Mean age female (SD) | Time after diagnosis male (SD) | Time after diagnosis female (SD) | MDS-UPDRS-III male (SD) | MDS-UPDRS-III female (SD) |
|----------|-------|-------------------|---------------------|-------------------------------|--------------------------------|------------------------|--------------------------|
| Spanish  | PD    | 61.3 (11.4)       | 60.7 (7.3)          | 8.7 (5.9)                     | 12.6 (11.6)                    | 37.8 (22.1)            | 37.6 (14.1)              |
| Spanish  | HC    | 60.5 (11.6)       | 61.4 (7.0)          | –                             | –                              | –                      | –                        |
| German   | PD    | 66.7 (8.7)        | 66.2 (9.7)          | 7.0 (5.5)                     | 7.1 (6.2)                      | 22.1 (9.9)             | 23.3 (12.0)              |
| German   | HC    | 63.8 (12.7)       | 62.6 (15.2)         | –                             | –                              | –                      | –                        |
| Czech    | PD    | 65.3 (9.6)        | 60.1 (8.7)          | 6.7 (4.5)                     | 6.8 (5.2)                      | 21.4 (11.5)            | 18.1 (9.7)               |
| Czech    | HC    | 60.3 (11.5)       | 63.5 (11.1)         | –                             | –                              | –                      | –                        |

*Note.* Dashes indicate not applicable because healthy controls do not have diagnosis time or MDS-UPDRS-III scores. Data from Table 1 in Vásquez-Correa et al. (2020) ([Vásquez-Correa et al., 2020](document_1.txt)).

## Speech Tasks Across Datasets

The speech tasks differ across the three datasets, which is a notable feature of the study design. Table 3 outlines the tasks per language. The Spanish dataset includes the most extensive set of tasks, with ten sentences and multiple rapid syllable repetitions in addition to a read text and a monologue ([Vásquez-Correa et al., 2020](document_1.txt)). The German dataset includes five sentences, one text with 81 words, and a monologue, while the Czech dataset includes a read text with 80 words and a monologue, but fewer sentence-level tasks ([Vásquez-Correa et al., 2020](document_1.txt)). These differences mean that the datasets are not fully parallel in their speech material, which could influence cross-linguistic transfer learning results ([Vásquez-Correa et al., 2020](document_1.txt)).

| Language | Speech tasks |
|----------|--------------|
| Spanish  | 10 sentences; rapid repetition of /pa-ta-ka/, /pe-ta-ka/, /pa-ka-ta/, /pa/, /ta/, /ka/; one text with 36 words; monologue |
| German   | Rapid repetition of /pa-ta-ka/; 5 sentences; one text with 81 words; monologue |
| Czech    | Rapid repetition of /pa-ta-ka/; read text with 80 words; monologue |

*Note.* Data from Section 2.1 in Vásquez-Correa et al. (2020) ([Vásquez-Correa et al., 2020](document_1.txt)).

## Data Preprocessing and Feature Extraction

The datasets were preprocessed in several steps before being used for classification. First, all recordings were captured in noise-controlled conditions and down-sampled to 16 kHz ([Vásquez-Correa et al., 2020](document_1.txt)). Second, speech signals were analyzed based on the automatic detection of onset and offset transitions, which model the difficulties of patients to start and stop vocal fold vibration ([Vásquez-Correa et al., 2020](document_1.txt)). The transition detection is based on the presence of the fundamental frequency in short-time frames; the border between voiced and unvoiced frames is detected, and 80 ms of signal are taken to the left and right, forming segments of 160 ms length ([Vásquez-Correa et al., 2020](document_1.txt)). These segments serve as the basic unit for both the baseline model and the CNN model ([Vásquez-Correa et al., 2020](document_1.txt)).

For the baseline model, hand-crafted features were extracted from the transitions. These include 12 Mel-Frequency Cepstral Coefficients (MFCCs) with their first and second derivatives, plus the log energy of the signal distributed into 22 Bark bands, yielding 58 descriptors ([Vásquez-Correa et al., 2020](document_1.txt)). Four statistical functionals—mean, standard deviation, skewness, and kurtosis—were computed for each descriptor, resulting in a 232-dimensional feature vector per utterance ([Vásquez-Correa et al., 2020](document_1.txt)). Classification was performed with a radial basis support vector machine (SVM) using a margin parameter C = 10 and a Gaussian kernel with γ = 0.0001, evaluated with 10-fold cross-validation in a speaker-independent manner ([Vásquez-Correa et al., 2020](document_1.txt)).

For the CNN model, time-frequency representations based on the short-time Fourier transform (STFT) were used. The STFT was computed with 256 frequency bins, a window length of 16 ms, and a step size of 4 ms, forming 41 time frames per transition ([Vásquez-Correa et al., 2020](document_1.txt)). The spectrogram was then transformed into the Mel scale using 80 filters, producing an 80 × 41 spectrogram that served as input to the CNN ([Vásquez-Correa et al., 2020](document_1.txt)). The CNN architecture consists of four convolutional and max-pooling layers, dropout regularization, and two fully connected layers followed by an output layer with softmax activation ([Vásquez-Correa et al., 2020](document_1.txt)). The model was trained with cross-entropy loss and the Adam optimizer ([Vásquez-Correa et al., 2020](document_1.txt)).

## Transfer Learning and the Role of the Datasets

The transfer learning strategy treats each language dataset as both a potential base and a target domain ([Vásquez-Correa et al., 2020](document_1.txt)). A CNN is first trained on utterances from one language, and the pretrained model is then used to initialize models for the remaining two languages through fine-tuning ([Vásquez-Correa et al., 2020](document_1.txt)). The authors report that the accuracy improved by over 8% for German when the base model was trained on Spanish (from 69.3% in the baseline to 77.3% after transfer), and by over 4.1% for Czech when fine-tuned from Spanish (from 68.5% with the initial CNN to 72.6% after transfer) ([Vásquez-Correa et al., 2020](document_1.txt)). The highest accuracy for German and Czech was obtained when the base language was Spanish, which the authors attribute to Spanish speakers having the best initial separability ([Vásquez-Correa et al., 2020](document_1.txt)). The transfer learning results were also more balanced in terms of specificity and sensitivity, with lower standard deviations, indicating improved generalization ([Vásquez-Correa et al., 2020](document_1.txt)).

## Discrepancy Between Primary and Secondary Sources

A critical reading of the provided materials reveals a significant discrepancy. The third-party research note states that the study uses “Spanish, Italian, and Czech” and that “the Italian dataset contains speech recordings of 88 PD patients and 88 HC speakers from Italy” ([Third-party research note, n.d.](document_2.txt)). However, the primary paper consistently identifies the second language as German and cites Skodda et al. (2011) for the German data ([Vásquez-Correa et al., 2020](document_1.txt)). The speaker counts for the “Italian” dataset in the secondary note (88 PD and 88 HC) exactly match the German dataset in the primary paper ([Third-party research note, n.d.](document_2.txt); [Vásquez-Correa et al., 2020](document_1.txt)). There is no mention of an Italian dataset anywhere in the primary source ([Vásquez-Correa et al., 2020](document_1.txt)). Therefore, the secondary note likely contains a substitution error, replacing “German” with “Italian” ([Third-party research note, n.d.](document_2.txt)). For any research or replication purpose, the correct datasets are PC-GITA (Spanish), the German dataset from Skodda et al. (2011), and the Czech dataset from Rusz (2018) ([Vásquez-Correa et al., 2020](document_1.txt)).

## Ethical and Access Considerations

The provided sources do not specify ethical approval procedures, informed consent details, or data access mechanisms for the three datasets ([Vásquez-Correa et al., 2020](document_1.txt); [Third-party research note, n.d.](document_2.txt)). However, the datasets are derived from previously published corpora and studies: PC-GITA is a known Spanish speech corpus for Parkinson’s disease analysis, the German data come from Skodda et al. (2011), and the Czech data come from Rusz (2018) ([Vásquez-Correa et al., 2020](document_1.txt)). Researchers interested in using these datasets would need to consult the original corpus publications and their respective access policies ([Vásquez-Correa et al., 2020](document_1.txt)). The clinical evaluations with MDS-UPDRS-III indicate that the datasets include sensitive health information, so ethical handling and privacy protections are implied even if not explicitly described in the provided text ([Vásquez-Correa et al., 2020](document_1.txt)).

## Conclusion

In summary, the study uses three speech datasets: the PC-GITA corpus for Colombian Spanish (50 PD, 50 HC), a German dataset (88 PD, 88 HC), and a Czech dataset (50 PD, 50 HC) ([Vásquez-Correa et al., 2020](document_1.txt)). All datasets include speech recordings from PD patients and healthy controls, clinical evaluations via MDS-UPDRS-III, and a variety of speech tasks such as sustained vowels, rapid syllable repetitions, read texts, and monologues ([Vásquez-Correa et al., 2020](document_1.txt)). The recordings were preprocessed with down-sampling to 16 kHz and segmented into 160 ms transitions between voiced and unvoiced frames ([Vásquez-Correa et al., 2020](document_1.txt)). The primary paper’s dataset description is reliable and internally consistent, whereas the secondary note incorrectly substitutes Italian for German ([Vásquez-Correa et al., 2020](document_1.txt); [Third-party research note, n.d.](document_2.txt)). Researchers should therefore rely on the primary source for accurate dataset identification and characteristics.

## References

Vásquez-Correa, J. C., Arias-Vergara, T., Rios-Urrego, C. D., Schuster, M., Rusz, J., Orozco-Arroyave, J. R., & Nöth, E. (2020). *Convolutional Neural Networks and a Transfer Learning Strategy to Classify Parkinson’s Disease from Speech in Three Different Languages*. arXiv:2002.04374. [document_1.txt](document_1.txt)

Third-party research note: *Convolutional Neural Networks and a Transfer Learning Strategy to Classify Parkinson's Disease from Speech in Three Different Languages*. [document_2.txt](document_2.txt)