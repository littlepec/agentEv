# Datasets Used in the Parkinson’s Disease Speech Classification Study

## Overview

The study titled “Convolutional Neural Networks and a Transfer Learning Strategy to Classify Parkinson’s Disease from Speech in Three Different Languages” by Vásquez-Correa et al. (2020) uses three distinct speech datasets, each representing a different language: Spanish, German, and Czech. The central research question of the work is whether convolutional neural networks (CNNs) trained on time-frequency representations, combined with cross-lingual transfer learning, can improve the classification of Parkinson’s disease (PD) from speech across languages ([Vásquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374v1)). The primary source document, referred to here as document_1.txt, provides the full methodology, speaker tables, and results. A secondary third-party research note, document_2.txt, summarizes the datasets but contains at least one factual error regarding the German dataset. This report identifies and describes each dataset, its composition, speaker demographics, speech tasks, clinical evaluations, and its specific role in the experiments. The report prioritizes the primary source over the secondary note and explicitly addresses the discrepancy between them.

## Spanish Dataset: PC-GITA Corpus

### Source and Composition

The Spanish data are drawn from the PC-GITA corpus, which contains utterances from 50 PD patients and 50 healthy control (HC) subjects, all Colombian Spanish native speakers ([Vásquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374v1)). This yields a total of 100 speakers, perfectly balanced between the two diagnostic classes. The corpus is referenced as source [6] in the original paper and is described as a new Spanish speech corpus database for the analysis of people suffering from Parkinson’s disease (Orozco-Arroyave et al., 2014, as cited in Vásquez-Correa et al., 2020). The third-party note confirms this composition: “The Spanish data come from the PC-GITA corpus. PC-GITA contains utterances from 50 PD patients and 50 HC, Colombian Spanish native speakers” ([Document 2](document_2.txt)). The Spanish dataset is therefore the most prominently described corpus in the study and serves as the baseline for several transfer learning comparisons.

### Speaker Demographics

Table 1 of the primary source provides detailed demographic and clinical information for the Spanish cohort. The PD group consisted of 25 males and 25 females, while the HC group also consisted of 25 males and 25 females. Age ranges were as follows: PD males 33–81 years, PD females 49–75 years; HC males 31–86 years, HC females 49–76 years. Mean ages were 61.3 years (SD 11.4) for PD males and 60.7 years (SD 7.3) for PD females; HC males averaged 60.5 years (SD 11.6) and HC females averaged 61.4 years (SD 7.0). Time since diagnosis was 8.7 years (SD 5.9) for PD males and 12.6 years (SD 11.6) for PD females. The MDS-UPDRS-III scores, which quantify motor impairment, were 37.8 (SD 22.1) for PD males and 37.6 (SD 14.1) for PD females ([Vásquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374v1)). These scores are notably higher than those of the German and Czech PD groups, indicating greater average disease severity in the Spanish dataset.

### Speech Tasks

Participants in the Spanish dataset were asked to pronounce a total of 10 sentences, the rapid repetition of /pa-ta-ka/, /pe-ta-ka/, /pa-ka-ta/, /pa/, /ta/, and /ka/, one text with 36 words, and a monologue. All patients were in the ON state at the time of recording, meaning they were under the effect of their daily medication ([Vásquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374v1)). This ON-state condition is important because it may influence speech motor performance and therefore the acoustic characteristics captured by the models.

## German Dataset

### Source and Composition

The German data consist of speech recordings of 88 PD patients and 88 HC speakers from Germany ([Vásquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374v1)). This composition is explicitly stated in the primary source and is corroborated by Table 1, which lists 47 male and 41 female PD patients (47 + 41 = 88) and 44 male and 44 female HC speakers (44 + 44 = 88). The third-party research note incorrectly states that the German data consist of 44 PD patients and 44 HC speakers ([Document 2](document_2.txt)). That note further claims that “the speaker counts for the German and Czech data are 44 PD patients with 44 HC speakers and 50 PD patients with 50 HC, respectively” ([Document 2](document_2.txt)). The primary source, however, is unambiguous: the German dataset contains 88 PD patients and 88 HC speakers, for a total of 176 speakers. This report treats the primary source as authoritative and flags the secondary note’s German count as an error, likely arising from a misreading of gender-specific subgroup sizes or a transcription mistake.

### Speaker Demographics

For the German PD group, there were 47 males and 41 females. The HC group comprised 44 males and 44 females. Age ranges were: PD males 44–82 years, PD females 42–84 years; HC males 26–83 years, HC females 28–85 years. Mean ages were 66.7 years (SD 8.7) for PD males and 66.2 years (SD 9.7) for PD females; HC males averaged 63.8 years (SD 12.7) and HC females averaged 62.6 years (SD 15.2). Time since diagnosis was 7.0 years (SD 5.5) for PD males and 7.1 years (SD 6.2) for PD females. MDS-UPDRS-III scores were 22.1 (SD 9.9) for PD males and 23.3 (SD 12.0) for PD females ([Vásquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374v1)). The German cohort therefore has a larger number of speakers than the Spanish and Czech cohorts, but its average disease severity is lower than that of the Spanish cohort.

### Speech Tasks

The German participants performed four speech tasks: the rapid repetition of /pa-ta-ka/, 5 sentences, one text with 81 words, and a monologue ([Vásquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374v1)). The speech tasks are broadly comparable to those in the Spanish and Czech datasets, allowing for cross-linguistic modeling of articulation and phonation deficits.

## Czech Dataset

### Source and Composition

A total of 100 native Czech speakers were considered, comprising 50 PD patients and 50 HC subjects ([Vásquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374v1)). This is consistent with the third-party note, which states: “The Czech dataset contains a total of 100 native Czech speakers, comprising 50 PD patients and 50 healthy controls” ([Document 2](document_2.txt)). The primary source references the Czech data as source [19], a habilitation thesis by J. Rusz (2018) on detecting speech disorders in early Parkinson’s disease by acoustic analysis. The Czech dataset therefore has the same class balance as the Spanish dataset, with 100 speakers in total.

### Speaker Demographics

For the Czech PD group, there were 30 males and 20 females; the HC group also had 30 males and 20 females. Age ranges were: PD males 43–82 years, PD females 41–72 years; HC males 41–77 years, HC females 40–79 years. Mean ages were 65.3 years (SD 9.6) for PD males and 60.1 years (SD 8.7) for PD females; HC males averaged 60.3 years (SD 11.5) and HC females averaged 63.5 years (SD 11.1). Time since diagnosis was 6.7 years (SD 4.5) for PD males and 6.8 years (SD 5.2) for PD females. MDS-UPDRS-III scores were 21.4 (SD 11.5) for PD males and 18.1 (SD 9.7) for PD females ([Vásquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374v1)). As with the German cohort, the Czech PD group has lower average MDS-UPDRS-III scores than the Spanish PD group.

### Speech Tasks

The Czech speech tasks included the rapid repetition of the syllables /pa-ta-ka/, a read text with 80 words, and a monologue ([Vásquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374v1)). These tasks overlap substantially with the Spanish and German protocols, enabling the study’s cross-lingual transfer learning design.

## Recording Conditions and Clinical Evaluation

All recordings across the three datasets were captured in noise-controlled conditions. The speech signals were down-sampled to 16 kHz. The patients in all three datasets were evaluated by a neurologist expert according to the third section of the Movement Disorder Society, Unified Parkinson’s Disease Rating Scale (MDS-UPDRS-III) ([Vásquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374v1)). This clinical scale is used to quantify motor impairment and disease severity. A key cross-dataset difference is that the Spanish PD patients had higher average MDS-UPDRS-III scores (37.8 for males, 37.6 for females) compared with German patients (22.1 males, 23.3 females) and Czech patients (21.4 males, 18.1 females). The authors note that this difference in disease severity may help explain why the Spanish dataset exhibited the highest classification accuracy among the three languages ([Vásquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374v1)).

## Detailed Speaker Demographics Table

The following table summarizes the demographic and clinical information from Table 1 of the primary source.

| Dataset | Group | Gender | N | Age range | Mean age (SD) | Time since diagnosis (years) | MDS-UPDRS-III |
|---------|-------|--------|---|-----------|---------------|------------------------------|----------------|
| Spanish | PD | M | 25 | 33–81 | 61.3 (11.4) | 8.7 (5.9) | 37.8 (22.1) |
| Spanish | PD | F | 25 | 49–75 | 60.7 (7.3) | 12.6 (11.6) | 37.6 (14.1) |
| Spanish | HC | M | 25 | 31–86 | 60.5 (11.6) | – | – |
| Spanish | HC | F | 25 | 49–76 | 61.4 (7.0) | – | – |
| German | PD | M | 47 | 44–82 | 66.7 (8.7) | 7.0 (5.5) | 22.1 (9.9) |
| German | PD | F | 41 | 42–84 | 66.2 (9.7) | 7.1 (6.2) | 23.3 (12.0) |
| German | HC | M | 44 | 26–83 | 63.8 (12.7) | – | – |
| German | HC | F | 44 | 28–85 | 62.6 (15.2) | – | – |
| Czech | PD | M | 30 | 43–82 | 65.3 (9.6) | 6.7 (4.5) | 21.4 (11.5) |
| Czech | PD | F | 20 | 41–72 | 60.1 (8.7) | 6.8 (5.2) | 18.1 (9.7) |
| Czech | HC | M | 30 | 41–77 | 60.3 (11.5) | – | – |
| Czech | HC | F | 20 | 40–79 | 63.5 (11.1) | – | – |

Source: Table 1 in Vásquez-Correa et al. (2020) ([Vásquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374v1)).

## Speech Task Summary Table

| Language | Speech tasks |
|----------|--------------|
| Spanish | 10 sentences; rapid repetition of /pa-ta-ka/, /pe-ta-ka/, /pa-ka-ta/, /pa/, /ta/, /ka/; one text with 36 words; monologue; all patients in ON state |
| German | Rapid repetition of /pa-ta-ka/; 5 sentences; one text with 81 words; monologue |
| Czech | Rapid repetition of /pa-ta-ka/; read text with 80 words; monologue |

Source: Vásquez-Correa et al. (2020) ([Vásquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374v1)).

## Data Preparation for Modeling

### Segmentation

Speech signals were analyzed based on automatic detection of onset and offset transitions, which model the difficulties of patients to start and stop the movement of the vocal folds. Detection was based on the presence of the fundamental frequency of speech in short-time frames. The border between voiced and unvoiced frames was detected, and 80 ms of the signal were taken to the left and to the right, forming segments with 160 ms length ([Vásquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374v1)). This segmentation procedure was applied to all three datasets.

### Baseline Model Features

For the baseline model, features extracted from the transitions included 12 Mel-Frequency Cepstral Coefficients (MFCCs) with their first and second derivatives, and the log energy of the signal distributed into 22 Bark bands. The total number of descriptors was 58. Four statistical functionals (mean, standard deviation, skewness, and kurtosis) were computed for each descriptor, obtaining a 232-dimensional feature vector per utterance. Classification was performed with a radial basis SVM with margin parameter C = 10 and a Gaussian kernel with parameter γ = 0.0001. The SVM was tested following a 10-fold cross-validation strategy, speaker independent ([Vásquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374v1)).

### CNN Input Representations

For the CNN models, time-frequency representations based on the short-time Fourier transform (STFT) were used. The STFT with 256 frequency bins was computed for each segmented transition, for a window length of 16 ms and a step-size of 4 ms, forming 41 time frames per transition. The obtained spectrogram was transformed into the Mel-scale using 80 filters, forming a spectrogram with a size of 80×41, which was used to train the CNNs ([Vásquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374v1)).

### Transfer Learning Design

The CNN architecture consisted of four convolutional and max-pooling layers, dropout to regularize the weights, and two fully connected layers followed by the output layer with a softmax activation function. The CNN was trained using cross-entropy as the loss function with an Adam optimizer. Transfer learning was implemented by training a CNN with utterances from one language (the base language), then using the pre-trained model to initialize models for the remaining languages (the target languages). This procedure aimed to improve accuracy when the weights of the neural network are initialized with utterances from a different language than the one used for the test set ([Vásquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374v1)).

## Dataset Utilization and Results

### Individual Language Models

Table 3 in the study reports baseline and CNN results for each language individually. For Spanish, the baseline accuracy was 73.7% and the CNN accuracy was 71.0%. For German, the baseline accuracy was 69.3% and the CNN accuracy was 63.1%. For Czech, the baseline accuracy was 61.0% and the CNN accuracy was 68.5% ([Vásquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374v1)). The Spanish dataset showed the highest accuracy among the three languages, which the authors attribute to the higher disease severity of the Spanish patients.

### Transfer Learning Results

Table 4 presents the transfer learning results. When the base language was German and the target was Spanish, accuracy was 70.0%. Base Czech to Spanish yielded 72.0%. Base Spanish to German yielded 77.3%. Base Czech to German yielded 76.7%. Base Spanish to Czech yielded 72.6%. Base German to Czech yielded 70.7% ([Vásquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374v1)). The highest accuracy for German and Czech targets was obtained when the base language was Spanish. The accuracy improved by over 8% for German (from 69.3% baseline to 77.3% with Spanish fine-tuning) and by over 4.1% for Czech (from 68.5% with the initial CNN to 72.6% with Spanish fine-tuning) ([Vásquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374v1)). These results demonstrate that the Spanish dataset, despite having fewer speakers than the German dataset, provided the most robust base model for cross-lingual transfer.

### ROC AUCs

ROC curves show AUC values for each target language. For target Spanish, the AUC was 0.824 for Spanish alone, 0.779 for German-Spanish, and 0.838 for Czech-Spanish. For target German, the AUC was 0.684 for German alone, 0.792 for Czech-German, and 0.823 for Spanish-German. For target Czech, the AUC was 0.764 for Czech alone, 0.762 for German-Czech, and 0.831 for Spanish-Czech ([Vásquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374v1)). These metrics further illustrate how each dataset contributes to cross-lingual classification performance.

## Reliability and Discrepancy in Source Information

The third-party research note in document_2.txt provides a summary but contains a factual error regarding the German dataset. It states: “The German data consist of speech recordings of 44 PD patients and 44 HC speakers” and “The speaker counts for the German and Czech data are 44 PD patients with 44 HC speakers and 50 PD patients with 50 HC, respectively” ([Document 2](document_2.txt)). However, the primary source text states: “German Speech recordings of 88 PD patients and 88 HC speakers from Germany are considered” ([Vásquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374v1)). Table 1 of the primary source lists German PD: 47 males + 41 females = 88; German HC: 44 males + 44 females = 88. Therefore, the primary source is authoritative, and the third-party note’s German count should be disregarded. This report relies on the primary source for all dataset compositions and explicitly notes the discrepancy to avoid propagating incorrect information.

## Summary of Datasets

| Language | Corpus/Source | PD Speakers | HC Speakers | Total Speakers | Key Speech Tasks | Clinical Evaluation |
|----------|---------------|-------------|-------------|----------------|------------------|---------------------|
| Spanish | PC-GITA | 50 | 50 | 100 | 10 sentences, /pa-ta-ka/, /pe-ta-ka/, /pa-ka-ta/, /pa/, /ta/, /ka/, 36-word text, monologue | MDS-UPDRS-III; patients in ON state |
| German | Skodda et al. (2011) recordings | 88 | 88 | 176 | Rapid /pa-ta-ka/, 5 sentences, 81-word text, monologue | MDS-UPDRS-III |
| Czech | Rusz (2018) habilitation data | 50 | 50 | 100 | Rapid /pa-ta-ka/, 80-word read text, monologue | MDS-UPDRS-III |

Note: Table compiled from Vásquez-Correa et al. (2020) ([Vásquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374v1)).

## Conclusion

The study uses three language-specific speech datasets: the Spanish PC-GITA corpus (50 PD, 50 HC), German recordings (88 PD, 88 HC), and Czech recordings (50 PD, 50 HC). Across all three datasets, there are 188 PD patients and 188 healthy control speakers, totaling 376 speakers. These datasets are used to train and evaluate CNNs on Mel-spectrogram representations of voiced/unvoiced transitions, and to test cross-lingual transfer learning strategies. The primary source is the paper by Vásquez-Correa et al. (2020), while the third-party note contains a German speaker count error that should not be relied upon. The datasets are well-characterized in terms of demographics, speech tasks, and MDS-UPDRS-III scores, enabling a rigorous cross-lingual investigation of Parkinson’s disease speech classification. From the evidence provided, the Spanish PC-GITA dataset appears to be the most influential for transfer learning, as it produced the highest accuracy improvements when used as the base language for German and Czech target models.

## References

- Vásquez-Correa, J. C., Arias-Vergara, T., Rios-Urrego, C. D., Schuster, M., Rusz, J., Orozco-Arroyave, J. R., & Nöth, E. (2020). *Convolutional neural networks and a transfer learning strategy to classify Parkinson’s disease from speech in three different languages*. arXiv:2002.04374v1. https://arxiv.org/abs/2002.04374v1
- Document 2. (n.d.). *Third-party research note: Convolutional neural networks and a transfer learning strategy to classify Parkinson's disease from speech in three different languages*. [document_2.txt](document_2.txt)