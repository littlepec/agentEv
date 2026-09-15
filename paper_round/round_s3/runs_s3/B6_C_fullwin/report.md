# Datasets Used in Convolutional Neural Networks and Transfer Learning for Parkinson's Disease Speech Classification

## Introduction
The study under review, "Convolutional Neural Networks and a Transfer Learning Strategy to Classify Parkinson’s Disease from Speech in Three Different Languages," employs three distinct speech datasets representing Spanish, German, and Czech languages to develop and evaluate models that distinguish Parkinson's disease (PD) patients from healthy control (HC) speakers ([Vásquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)). The selection of these datasets is central to the study's cross-lingual transfer learning approach. This report provides a detailed examination of each dataset, including their sources, participant composition, speech tasks, clinical variables, collection and preprocessing methods, and limitations. The information is drawn primarily from the study itself and a third-party research note summarizing its data ([Third-party research note, n.d.](document_2.txt)).

## Overview of the Three Datasets
The study utilizes three language-specific datasets: the Spanish PC-GITA corpus, a German dataset from prior research, and a Czech dataset from a habilitation thesis ([Vásquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)). Table 1 summarizes their key characteristics.

| Language | Source/Corpus | PD Participants | HC Participants | Total Participants | Primary Speech Tasks | Clinical Evaluation |
|----------|---------------|-----------------|-----------------|--------------------|----------------------|---------------------|
| Spanish  | PC-GITA corpus [6] | 50 | 50 | 100 | 10 sentences; rapid repetition of /pa-ta-ka/, /pe-ta-ka/, /pa-ka-ta/, /pa/, /ta/, /ka/; 36-word text; monologue | MDS-UPDRS-III |
| German   | Speech recordings from Germany [18] | 88 | 88 | 176 | Rapid repetition of /pa-ta-ka/; 5 sentences; 81-word text; monologue | MDS-UPDRS-III |
| Czech    | Czech dataset [19] | 50 | 50 | 100 | Rapid repetition of /pa-ta-ka/; 80-word read text; monologue | MDS-UPDRS-III |

*Note.* PD = Parkinson's disease; HC = healthy control; MDS-UPDRS-III = Movement Disorder Society Unified Parkinson's Disease Rating Scale, Part III. Data compiled from Vásquez-Correa et al. (2020) and the third-party research note (n.d.).

The datasets collectively provide speech recordings from 188 PD patients and 188 HC speakers across three languages ([Vásquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)). All recordings were captured under noise-controlled conditions and down-sampled to 16 kHz ([Vásquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)). Patients in all three datasets were evaluated by a neurologist expert using the MDS-UPDRS-III ([Vásquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374); [Third-party research note, n.d.](document_2.txt)).

## Spanish Dataset: PC-GITA Corpus
### Source and Composition
The Spanish data are drawn from the PC-GITA corpus, a Colombian Spanish speech database designed for the analysis of people suffering from Parkinson's disease ([Vásquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)). The corpus contains utterances from 50 PD patients and 50 HC speakers, all native Colombian Spanish speakers ([Vásquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374); [Third-party research note, n.d.](document_2.txt)). The speaker composition is balanced by gender: 25 male and 25 female PD patients, and 25 male and 25 female HC speakers ([Vásquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)).

### Speech Tasks
Participants were asked to perform a comprehensive set of speech tasks: 10 sentences, the rapid repetition of syllables /pa-ta-ka/, /pe-ta-ka/, /pa-ka-ta/, /pa/, /ta/, and /ka/, one text containing 36 words, and a monologue ([Vásquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)). This variety of tasks is the richest among the three datasets, potentially providing a broader representation of speech impairments.

### Clinical and Demographic Variables
Table 2 presents the demographic and clinical details for the Spanish cohort. All Spanish patients were in the ON state at the time of recording, meaning they were under the effect of their daily medication ([Vásquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)). The mean age for male PD patients was 61.3 years (SD = 11.4), and for female PD patients, 60.7 years (SD = 7.3). Healthy controls had similar mean ages: 60.5 years (SD = 11.6) for males and 61.4 years (SD = 7.0) for females ([Vásquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)). The time after diagnosis averaged 8.7 years (SD = 5.9) for males and 12.6 years (SD = 11.6) for females, indicating a relatively long disease duration, particularly among women ([Vásquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)). The mean MDS-UPDRS-III score was 37.8 (SD = 22.1) for males and 37.6 (SD = 14.1) for females, reflecting moderate to high disease severity ([Vásquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)).

## German Dataset
### Source and Composition
The German dataset consists of speech recordings from 88 PD patients and 88 HC speakers from Germany ([Vásquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)). The source is cited as Skodda, Visser, and Schlegel (2011) [18] ([Vásquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)). This dataset is the largest in terms of total participants (176 speakers) ([Third-party research note, n.d.](document_2.txt)). The gender distribution is 47 male and 41 female PD patients, and 44 male and 44 female HC speakers ([Vásquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)).

### Speech Tasks
German participants performed four speech tasks: rapid repetition of /pa-ta-ka/, five sentences, one text with 81 words, and a monologue ([Vásquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)). Notably, the German dataset lacks the expanded syllable repetitions and single-syllable tasks present in the Spanish dataset, which may influence comparability.

### Clinical and Demographic Variables
The German PD patients had a mean age of 66.7 years (SD = 8.7) for males and 66.2 years (SD = 9.7) for females, slightly older than the Spanish cohort ([Vásquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)). HC speakers had mean ages of 63.8 years (SD = 12.7) for males and 62.6 years (SD = 15.2) for females ([Vásquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)). Time since diagnosis was approximately 7 years for both genders (males: 7.0, SD = 5.5; females: 7.1, SD = 6.2) ([Vásquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)). The mean MDS-UPDRS-III score was 22.1 (SD = 9.9) for males and 23.3 (SD = 12.0) for females, indicating lower disease severity compared to the Spanish cohort ([Vásquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)). This lower severity likely contributed to the lower classification accuracy observed for German in the baseline model ([Vásquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)).

## Czech Dataset
### Source and Composition
The Czech dataset comprises 100 native Czech speakers, with 50 PD patients and 50 HC subjects ([Vásquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)). The data source is cited as Rusz (2018) [19], a habilitation thesis ([Vásquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)). The gender breakdown is 30 male and 20 female PD patients, and 30 male and 20 female HC speakers ([Vásquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)).

### Speech Tasks
Czech participants performed three speech tasks: rapid repetition of the syllables /pa-ta-ka/, a read text with 80 words, and a monologue ([Vásquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)). This dataset has the fewest task types, missing the sentence repetition and single-syllable tasks found in the Spanish and German datasets.

### Clinical and Demographic Variables
The Czech PD patients had a mean age of 65.3 years (SD = 9.6) for males and 60.1 years (SD = 8.7) for females ([Vásquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)). HC speakers had mean ages of 60.3 years (SD = 11.5) for males and 63.5 years (SD = 11.1) for females ([Vásquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)). Time since diagnosis averaged 6.7 years (SD = 4.5) for males and 6.8 years (SD = 5.2) for females ([Vásquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)). The mean MDS-UPDRS-III score was 21.4 (SD = 11.5) for males and 18.1 (SD = 9.7) for females, the lowest disease severity among the three groups ([Vásquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)).

## Data Collection and Preprocessing
### Recording Conditions
All speech recordings across the three datasets were captured in noise-controlled conditions and down-sampled to 16 kHz ([Vásquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)). This standardization ensures consistent signal quality for computational analysis.

### Clinical Evaluation
Patients in all datasets were assessed by a neurologist expert using the MDS-UPDRS-III ([Vásquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374); [Third-party research note, n.d.](document_2.txt)). This scale provides a standardized measure of motor impairment severity, allowing for comparison across languages.

### Segmentation and Feature Extraction
For the study's models, speech signals were analyzed by automatically detecting onset and offset transitions between voiced and unvoiced segments, which reflect patients' difficulties in starting and stopping vocal fold vibration ([Vásquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)). The border between voiced and unvoiced frames was identified, and 80 ms of signal were taken to the left and right, forming 160 ms segments ([Vásquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)). 

For the baseline model, 12 Mel-Frequency Cepstral Coefficients (MFCCs) with first and second derivatives, plus log energy distributed into 22 Bark bands, yielded 58 descriptors ([Vásquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)). Four statistical functionals (mean, standard deviation, skewness, kurtosis) were computed for each descriptor, resulting in a 232-dimensional feature vector per utterance ([Vásquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)). Classification used a radial basis SVM with C = 10 and γ = 0.0001, evaluated via 10-fold cross-validation, speaker-independent ([Vásquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)).

For the CNN model, time-frequency representations based on the short-time Fourier transform (STFT) were computed with 256 frequency bins, a 16 ms window, and a 4 ms step, yielding 41 time frames per transition ([Vásquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)). The spectrogram was transformed to the Mel scale using 80 filters, producing an 80 × 41 input for the CNN ([Vásquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)).

### Speaker-Level Decisions
The final decision for each speaker was obtained by a majority voting strategy among the different speech exercises ([Vásquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)). This approach aggregates per-utterance classifications to produce a single diagnostic prediction per participant.

## Comparative Analysis of the Datasets
Table 2 provides a side-by-side comparison of key demographic and clinical variables for the PD groups across the three languages.

| Variable | Spanish PD | German PD | Czech PD |
|----------|------------|-----------|----------|
| N | 50 | 88 | 50 |
| Gender (M/F) | 25/25 | 47/41 | 30/20 |
| Mean age M (SD) | 61.3 (11.4) | 66.7 (8.7) | 65.3 (9.6) |
| Mean age F (SD) | 60.7 (7.3) | 66.2 (9.7) | 60.1 (8.7) |
| Time since diagnosis M (SD) | 8.7 (5.9) | 7.0 (5.5) | 6.7 (4.5) |
| Time since diagnosis F (SD) | 12.6 (11.6) | 7.1 (6.2) | 6.8 (5.2) |
| MDS-UPDRS-III M (SD) | 37.8 (22.1) | 22.1 (9.9) | 21.4 (11.5) |
| MDS-UPDRS-III F (SD) | 37.6 (14.1) | 23.3 (12.0) | 18.1 (9.7) |

*Note.* M = male; F = female; SD = standard deviation. Data from Vásquez-Correa et al. (2020).

Several observations emerge from this comparison. First, the Spanish cohort exhibits substantially higher disease severity, with mean MDS-UPDRS-III scores near 37.7, compared to approximately 22.7 for German and 19.8 for Czech patients ([Vásquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)). This difference explains why the Spanish dataset achieved the highest initial classification accuracy and served as the most robust base model for transfer learning ([Vásquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)). Second, the German dataset is the largest, with 176 total speakers, which may provide more training data but does not necessarily translate to higher accuracy due to lower disease severity ([Third-party research note, n.d.](document_2.txt)). Third, the Spanish female PD patients had a notably longer time since diagnosis (12.6 years) compared to other groups, which could affect speech characteristics ([Vásquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)). Fourth, the speech tasks are not identical across languages, introducing potential confounds when comparing model performance across datasets ([Vásquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)).

## Limitations of the Datasets
The datasets, while valuable, have several limitations that warrant consideration. The differences in speech tasks across languages mean that models may learn task-specific rather than language-general features ([Vásquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)). The variation in sample sizes and gender distributions could introduce sampling bias ([Vásquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)). The significant disparity in disease severity, with Spanish patients being more severely affected, may confound cross-lingual comparisons ([Vásquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)). Medication state is only reported for the Spanish dataset (all ON state), while it is unspecified for German and Czech participants, potentially affecting speech performance ([Vásquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)). Additionally, the German and Czech datasets are not as well-known as the PC-GITA corpus, and their accessibility may be limited ([Vásquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374); [Third-party research note, n.d.](document_2.txt)). Language-specific phonetic properties, such as the richer consonant production in Czech and German compared to Spanish, may bias models trained on one language when applied to another ([Vásquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)).

## Role of the Datasets in the Study
The three datasets were used in two primary experimental setups. First, baseline and CNN models were trained and tested individually for each language ([Vásquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)). The baseline model achieved accuracies of 73.7% for Spanish, 69.3% for German, and 61.0% for Czech, while the CNN achieved 71.0%, 63.1%, and 68.5%, respectively ([Vásquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)). Second, transfer learning was applied, where a CNN pre-trained on one language was fine-tuned on another ([Vásquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)). The transfer learning strategy improved accuracy for German and Czech when the base language was Spanish: German reached 77.3% and Czech reached 76.7% (or 72.6% depending on the table interpretation) ([Vásquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)). These results underscore the importance of dataset characteristics, particularly disease severity and initial separability, in determining the success of cross-lingual transfer ([Vásquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)).

## Conclusion
The study by Vásquez-Correa et al. (2020) utilizes three speech datasets in Spanish, German, and Czech to investigate cross-lingual Parkinson's disease classification. The Spanish dataset (PC-GITA) comprises 50 PD and 50 HC speakers with the highest disease severity; the German dataset includes 88 PD and 88 HC speakers with moderate severity; and the Czech dataset consists of 50 PD and 50 HC speakers with the lowest severity ([Vásquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)). All datasets provide noise-controlled, 16 kHz recordings with MDS-UPDRS-III evaluations. While they enable valuable cross-lingual research, limitations such as task heterogeneity, sample size differences, and severity disparities must be considered when interpreting results ([Vásquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)). The datasets collectively form a rich resource for developing and testing speech-based diagnostic tools for Parkinson's disease across languages.

## References
Third-party research note. (n.d.). *Convolutional Neural Networks and a Transfer Learning Strategy to Classify Parkinson's Disease from Speech in Three Different Languages*. document_2.txt.

Vásquez-Correa, J. C., Arias-Vergara, T., Rios-Urrego, C. D., Schuster, M., Rusz, J., Orozco-Arroyave, J. R., & Nöth, E. (2020). *Convolutional Neural Networks and a Transfer Learning Strategy to Classify Parkinson's Disease from Speech in Three Different Languages*. arXiv preprint arXiv:2002.04374. https://arxiv.org/abs/2002.04374