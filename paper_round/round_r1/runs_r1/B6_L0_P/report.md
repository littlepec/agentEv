# Datasets Used in the Cross-Lingual Classification of Parkinson's Disease from Speech

## Introduction

The question of which datasets are used in speech-based Parkinson's disease (PD) classification is answered most directly by the study of Vásquez-Correa et al. (2020), which assembled speech recordings of PD patients and healthy control (HC) speakers in three languages: Spanish, German, and Czech ([Vásquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)). The datasets are not a single monolithic resource but a deliberate compilation of three independently collected corpora, each tied to a specific language community, clinical setting, and recording protocol. According to the authors, the data consist of "speech recordings of patients in three different languages," all captured "in noise controlled conditions" and down-sampled to 16 kHz ([Vásquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)). This report describes each dataset in detail, summarises its composition, speech tasks, and clinical annotations, explains how the corpora were used in the baseline and transfer-learning experiments, and evaluates the reliability of the available source material — including a notable numerical discrepancy in the secondary research note ([Research Note](document_2.txt)).

## Overview of the Data Sources

The study draws on three named or described corpora. The Spanish portion comes from the PC-GITA corpus ([Vásquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)). The German portion consists of speech recordings from Germany attributed to Skodda, Visser, and Schlegel (2011), as cited within the paper ([Vásquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)). The Czech portion was originally collected and described by Rusz (2018) in a habilitation thesis ([Vásquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)). Together these three sources form the dataset base for the convolutional neural network (CNN) and cross-lingual transfer-learning strategy evaluated in the paper ([Research Note](document_2.txt)).

The consolidated composition of the three datasets is summarised in Table 1.

**Table 1. Consolidated speaker composition across the three language datasets**

| Language | Corpus / Source | PD patients | Healthy controls | Total speakers |
|---|---|---|---|---|
| Spanish | PC-GITA | 50 | 50 | 100 |
| German | Skodda et al. recordings | 88 | 88 | 176 |
| Czech | Rusz recordings | 50 | 50 | 100 |
| **Total** | — | **188** | **188** | **376** |

The figures in Table 1 are taken from the paper's description and Table 1 ([Vásquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)). The German total of 88 PD patients and 88 HC speakers is confirmed by the text ("Speech recordings of 88 PD patients and 88 HC speakers from Germany are considered") and by the gender breakdown in the paper's Table 1, where 47 male and 41 female PD patients sum to 88, and 44 male and 44 female controls sum to 88 ([Vásquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)).

## The Spanish Dataset: PC-GITA Corpus

### Composition and demographics

The Spanish data comprise the PC-GITA corpus, which "contains utterances from 50 PD patients and 50 HC, Colombian Spanish native speakers" ([Vásquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)). The speaker composition is therefore 50 PD patients and 50 healthy controls, all Colombian Spanish native speakers, a point also confirmed by the secondary research note ([Research Note](document_2.txt)). The gender distribution is balanced: 25 male and 25 female PD patients, and 25 male and 25 female controls ([Vásquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)).

Mean ages were 61.3 years (SD = 11.4) for male PD patients and 60.7 years (SD = 7.3) for female PD patients, compared with 60.5 years (SD = 11.6) and 61.4 years (SD = 7.0) for male and female controls, respectively ([Vásquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)). The age ranges spanned 33–81 years for male patients and 49–75 for female patients, versus 31–86 and 49–76 for controls ([Vásquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)). Time since diagnosis averaged 8.7 years (SD = 5.9) for male patients and 12.6 years (SD = 11.6) for female patients ([Vásquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)).

### Speech tasks and clinical state

Participants were asked to pronounce a total of 10 sentences, the rapid repetition of /pa-ta-ka/, /pe-ta-ka/, /pa-ka-ta/, /pa/, /ta/, and /ka/, one text with 36 words, and a monologue ([Vásquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)). Importantly, all Spanish patients "were in ON state at the time of the recording, i.e., under the effect of their daily medication" ([Vásquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)). The Spanish patients also exhibited the highest disease severity of the three cohorts, with a mean MDS-UPDRS-III score of 37.8 (SD = 22.1) for men and 37.6 (SD = 14.1) for women ([Vásquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)).

## The German Dataset

The German dataset comprises speech recordings of 88 PD patients and 88 HC speakers from Germany ([Vásquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)). The participants performed four speech tasks: the rapid repetition of /pa-ta-ka/, five sentences, one text with 81 words, and a monologue ([Vásquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)). Gender composition was 47 male and 41 female PD patients, and 44 male and 44 female controls ([Vásquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)).

Mean ages were 66.7 years (SD = 8.7) for male patients and 66.2 years (SD = 9.7) for female patients, while controls averaged 63.8 years (SD = 12.7) and 62.6 years (SD = 15.2) for men and women, respectively ([Vásquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)). Age ranges were 44–82 (male patients), 42–84 (female patients), 26–83 (male controls), and 28–85 (female controls) ([Vásquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)). Mean time since diagnosis was 7.0 years (SD = 5.5) for men and 7.1 years (SD = 6.2) for women, and mean MDS-UPDRS-III scores were 22.1 (SD = 9.9) and 23.3 (SD = 12.0), respectively ([Vásquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)).

## The Czech Dataset

The Czech dataset contains a total of 100 native Czech speakers, comprising 50 PD patients and 50 healthy controls ([Vásquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)). The gender distribution is 30 male and 20 female PD patients, and 30 male and 20 female controls ([Vásquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)). Speech tasks included the rapid repetition of /pa-ta-ka/, a read text with 80 words, and a monologue ([Vásquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)).

Mean ages were 65.3 years (SD = 9.6) for male patients and 60.1 years (SD = 8.7) for female patients, versus 60.3 years (SD = 11.5) and 63.5 years (SD = 11.1) for male and female controls ([Vásquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)). Age ranges were 43–82 (male patients), 41–72 (female patients), 41–77 (male controls), and 40–79 (female controls) ([Vásquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)). Time since diagnosis averaged 6.7 years (SD = 4.5) for men and 6.8 years (SD = 5.2) for women, with MDS-UPDRS-III means of 21.4 (SD = 11.5) and 18.1 (SD = 9.7), respectively ([Vásquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)).

## Speech Tasks Across the Three Datasets

Table 2 compares the speech tasks performed by participants in each language, as reported by Vásquez-Correa et al. (2020).

**Table 2. Speech tasks by language**

| Language | Rapid syllable repetition | Sentences | Read text | Monologue |
|---|---|---|---|---|
| Spanish | /pa-ta-ka/, /pe-ta-ka/, /pa-ka-ta/, /pa/, /ta/, /ka/ | 10 sentences | 36-word text | Yes |
| German | /pa-ta-ka/ | 5 sentences | 81-word text | Yes |
| Czech | /pa-ta-ka/ | — | 80-word text | Yes |

The table is constructed from the descriptions provided in the paper ([Vásquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)). The Spanish protocol is the richest in terms of syllable repetition, whereas the German corpus contains the longest read text and the Czech corpus the fewest task types ([Vásquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)).

## How the Datasets Were Processed and Used

All recordings were captured under noise-controlled conditions and down-sampled to 16 kHz ([Vásquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)). The speech signals were then analysed by automatically detecting onset and offset transitions between voiced and unvoiced frames — a process intended to model patients' difficulties in starting and stopping vocal fold vibration ([Vásquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)). Around each detected border, 80 ms of signal were taken to the left and right, forming segments of 160 ms ([Vásquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)).

Two modelling paths were applied to these segments. The baseline model extracted 12 Mel-Frequency Cepstral Coefficients with first and second derivatives plus log energy distributed into 22 Bark bands, yielding 58 descriptors; four statistical functionals (mean, standard deviation, skewness, kurtosis) produced a 232-dimensional feature vector per utterance, classified by a radial-basis SVM ([Vásquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)). The CNN path computed short-time Fourier transform spectrograms with 256 frequency bins, 16 ms windows, and 4 ms steps, producing 41 time frames per transition; these were converted to 80-filter Mel spectrograms of size 80 × 41 as CNN input ([Vásquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)).

The datasets were used in two experimental phases. First, baseline and CNN models were trained per language individually, with a speaker-independent 10-fold cross-validation for the SVM ([Vásquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)). Second, the CNNs trained on one language were used as base models to initialise and fine-tune classifiers for the remaining two languages ([Vásquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)). Final per-speaker decisions were made by majority voting across the different speech exercises ([Vásquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)).

## Comparative Performance Suggesting Dataset Effects

The choice of dataset materially influenced classification performance. For Spanish, the baseline reached 73.7% accuracy (MCC = 0.50) and the CNN 71.0% (MCC = 0.42); German baseline accuracy was 69.3% (MCC = 0.39) versus 63.1% for the CNN; and Czech baseline accuracy was 61.0% (MCC = 0.27) versus 68.5% for the CNN (MCC = 0.43) ([Vásquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)). The authors attribute the Spanish advantage partly to the higher MDS-UPDRS-III scores in that cohort, i.e., greater disease severity in the Spanish data ([Vásquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)).

Under transfer learning, accuracy improved by more than 8% for German (from 69.3% baseline to 77.3% when fine-tuned from Spanish) and by more than 4.1% for Czech (from 68.5% to 72.6% when fine-tuned from Spanish) ([Vásquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)). The best German and Czech results were obtained when Spanish was the base language — an outcome the authors explain by Spanish speakers having the best initial separability ([Vásquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)).

## Reliability of the Sources and a Numerical Discrepancy

The datasets are documented in a peer-review-style preprint from arXiv, which provides detailed tables of demographics, speech tasks, and classification results ([Vásquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)). The secondary research note corroborates the Spanish and Czech compositions — "50 PD patients and 50 HC" for both — and confirms the use of the MDS-UPDRS-III for all three datasets ([Research Note](document_2.txt)).

However, the note contains an internal inconsistency regarding the German data. It states that "the German data consist of speech recordings of 44 PD patients and 44 HC speakers," and repeats that "the speaker counts for the German and Czech data are 44 PD patients with 44 HC speakers and 50 PD patients with 50 HC" ([Research Note](document_2.txt)). This conflicts with the primary paper, which explicitly reports 88 PD patients and 88 HC speakers from Germany, with a gender breakdown (47 male + 41 female patients; 44 male + 44 female controls) that sums to 88 in each group ([Vásquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)). The figure of 44 in the note appears to be the count of male controls rather than the total number of speakers. Given that the primary source provides a fully internally consistent table and narrative, the present report treats 88 PD and 88 HC as the accurate German dataset size ([Vásquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)).

## Significance, Limitations, and Future Directions

The three datasets are significant because they enable a cross-lingual, multi-corpus evaluation with a combined total of 376 speakers (188 PD, 188 HC) ([Vásquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)). They support a clinically grounded target — discriminating PD patients from healthy controls using speech — and include MDS-UPDRS-III annotations for all patient groups ([Research Note](document_2.txt)).

Nevertheless, several limitations follow from the dataset design. First, the datasets are unbalanced across languages in size (German has 176 speakers, Spanish and Czech 100 each) and differ in speech-task protocols, which complicates direct cross-lingual comparison ([Vásquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)). Second, the Spanish cohort was recorded in the ON-medication state, which may influence speech characteristics ([Vásquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)). Third, disease severity varies by cohort, with Spanish patients showing markedly higher MDS-UPDRS-III scores than German or Czech patients ([Vásquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)). The authors propose future work using more robust base models, hyper-parameter optimisation such as Bayesian optimisation, base models trained on two languages rather than one, staging of disease severity, and transfer learning across diseases such as Huntington's disease ([Vásquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)).

## Conclusion

The datasets used by Vásquez-Correa et al. (2020) are the PC-GITA corpus for Spanish (50 PD, 50 HC, Colombian Spanish speakers), German speech recordings (88 PD, 88 HC), and Czech speech recordings (50 PD, 50 HC) ([Vásquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)). All were collected under noise-controlled conditions, down-sampled to 16 kHz, and clinically annotated with the MDS-UPDRS-III ([Vásquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)). They supplied the transition segments, Mel spectrograms, and cross-lingual transfer experiments at the heart of the study, and they remain a valuable multi-language resource for speech-based PD research — notwithstanding the minor numerical error in the secondary note concerning the German sample ([Research Note](document_2.txt)).

## References

Vásquez-Correa, J. C., Arias-Vergara, T., Rios-Urrego, C. D., Schuster, M., Rusz, J., Orozco-Arroyave, J. R., & Nöth, E. (2020). *Convolutional neural networks and a transfer learning strategy to classify Parkinson's disease from speech in three different languages*. arXiv. https://arxiv.org/abs/2002.04374

Research note: *Convolutional neural networks and a transfer learning strategy to classify Parkinson's disease from speech in three different languages* [Third-party research note]. ([document_2.txt](document_2.txt))