# Datasets Used in the Cross-Lingual Parkinson's Disease Speech Classification Study

## 1. Purpose and Scope of This Report

This report identifies, describes, and critically evaluates the datasets employed by Vasquez-Correa et al. (2020) in their investigation of convolutional neural networks (CNNs) and transfer learning for the classification of Parkinson's disease (PD) from speech in three languages ([Vasquez-Correa et al., 2020](document_1.txt)). The study's data foundation consists of three independent, language-specific clinical speech corpora — Colombian Spanish, German, and Czech — together with a set of derived, machine-readable representations generated through segmentation, feature extraction, and time–frequency transformation. Because a third-party research note summarising the same study is also available, that note is treated here as a secondary source and its statements are systematically compared against the primary paper ([Research note](document_2.txt)). Where the two sources disagree, the discrepancy is reported explicitly rather than resolved silently, since dataset composition figures are material to reproducibility.

## 2. Overview: The Three Primary Speech Corpora

The study is explicitly multi-corpus. The authors state that "speech recordings of patients in three different languages are considered: Spanish, German, and Czech," and that all recordings were captured in noise-controlled conditions and down-sampled to 16 kHz ([Vasquez-Correa et al., 2020](document_1.txt)). Table 1 below consolidates the headline composition of each corpus as reported in the primary source.

| Language | Corpus / Source | PD speakers | Healthy controls | Total speakers | Native-speaker population |
|---|---|---|---|---|---|
| Spanish | PC-GITA | 50 | 50 | 100 | Colombian Spanish |
| German | German speech recordings | 88 | 88 | 176 | German |
| Czech | Czech speech recordings | 50 | 50 | 100 | Czech |

Source: ([Vasquez-Correa et al., 2020](document_1.txt)).

The Spanish portion is drawn from the PC-GITA corpus, described in the paper as containing utterances from 50 PD patients and 50 healthy control (HC) speakers who are Colombian Spanish native speakers ([Vasquez-Correa et al., 2020](document_1.txt)). PC-GITA is not a corpus created for this study; it is an established resource introduced by Orozco-Arroyave et al. (2014) and cited as reference [6] in the paper's reference list ([Vasquez-Correa et al., 2020](document_1.txt)). The same corpus is also referenced as the data source for earlier reported results of approximately 77% accuracy in phono-articulatory analyses and up to 81% accuracy in forced-alignment-based phonetic modelling ([Vasquez-Correa et al., 2020](document_1.txt)).

The German data are described in the primary source as "speech recordings of 88 PD patients and 88 HC speakers from Germany," attributed in the reference list to the work of Skodda, Visser, and Schlegel on vowel articulation in Parkinson's disease ([Vasquez-Correa et al., 2020](document_1.txt)). The Czech data consist of a total of 100 native Czech speakers, comprising 50 PD patients and 50 healthy controls, attributed to the habilitation thesis of Rusz (2018) and, in earlier passages, to Czech data from Rusz et al. (2013) ([Vasquez-Correa et al., 2020](document_1.txt)).

## 3. Spanish Dataset: PC-GITA

### 3.1 Speaker Composition

The Spanish dataset contains utterances from 50 PD patients and 50 HC speakers, all Colombian Spanish native speakers ([Vasquez-Correa et al., 2020](document_1.txt)). Gender composition is balanced: 25 male and 25 female PD patients, and 25 male and 25 female controls ([Vasquez-Correa et al., 2020](document_1.txt)).

### 3.2 Speech Tasks

Participants were asked to pronounce a total of 10 sentences, to perform rapid repetition of the syllables /pa-ta-ka/, /pe-ta-ka/, /pa-ka-ta/, /pa/, /ta/ and /ka/, to read one text containing 36 words, and to produce a monologue ([Vasquez-Correa et al., 2020](document_1.txt)). This is the richest task set of the three corpora, which is relevant because the study's final speaker-level decision is obtained by majority voting across speech exercises ([Vasquez-Correa et al., 2020](document_1.txt)).

### 3.3 Clinical Context

All Spanish patients were recorded in the ON state, that is, under the effect of their daily medication ([Vasquez-Correa et al., 2020](document_1.txt)). This is an important design characteristic: the corpus captures medicated speech performance rather than the untreated baseline condition, which constrains the interpretation of any diagnostic claims derived from it.

## 4. German Dataset

### 4.1 Speaker Composition and a Noted Discrepancy

The primary source reports 88 PD patients and 88 HC speakers from Germany ([Vasquez-Correa et al., 2020](document_1.txt)). The gender breakdown given in the paper's speaker-information table is 41 male and 47 female PD patients, and 44 male and 44 female control speakers — totalling 88 PD and 88 HC respectively ([Vasquez-Correa et al., 2020](document_1.txt)).

The third-party research note, by contrast, asserts that "the German data consist of speech recordings of 44 PD patients and 44 HC speakers" and restates that "the speaker counts for the German and Czech data are 44 PD patients with 44 HC speakers and 50 PD patients with 50 HC, respectively" ([Research note](document_2.txt)). This directly contradicts the primary paper and its demographic table. Given that document_1 is the primary research article and document_2 is an unauthored third-party note, the 88 PD / 88 HC figure should be treated as authoritative, and the 44/44 figure in the note should be regarded as an error or an incomplete restatement (possibly a partial count). Any downstream analysis that relies on the secondary note's German sample size would understate the cohort by roughly half.

### 4.2 Speech Tasks

German participants performed four speech tasks: rapid repetition of /pa-ta-ka/, five sentences, one text with 81 words, and a monologue ([Vasquez-Correa et al., 2020](document_1.txt)). The task set therefore differs from the Spanish protocol (fewer sentences, longer read text) and from the Czech protocol, which is a relevant source of cross-linguistic and cross-protocol variability.

## 5. Czech Dataset

### 5.1 Speaker Composition

A total of 100 native Czech speakers were considered, comprising 50 PD patients and 50 healthy controls ([Vasquez-Correa et al., 2020](document_1.txt)). The gender split is 20 male and 30 female PD patients, and 30 male and 20 female controls ([Vasquez-Correa et al., 2020](document_1.txt)). The third-party note reports the same aggregate composition of 50 PD and 50 HC speakers, which is consistent with the primary source on this point ([Research note](document_2.txt)).

### 5.2 Speech Tasks

Czech participants performed the rapid repetition of the syllables /pa-ta-ka/, a read text with 80 words, and a monologue ([Vasquez-Correa et al., 2020](document_1.txt)). This is the smallest task battery of the three corpora.

## 6. Demographic and Clinical Characterisation of the Corpora

All patients across the three datasets were evaluated by an expert neurologist according to the third section of the Movement Disorder Society's Unified Parkinson's Disease Rating Scale (MDS-UPDRS-III) ([Vasquez-Correa et al., 2020](document_1.txt)). Table 2 summarises the recoverable demographic and clinical figures.

| Variable | Spanish PD (M / F) | Spanish HC (M / F) | German PD (M / F) | German HC (M / F) | Czech PD (M / F) | Czech HC (M / F) |
|---|---|---|---|---|---|---|
| Subjects | 25 / 25 | 25 / 25 | 41 / 47 | 44 / 44 | 20 / 30 | 30 / 20 |
| Age range (years) | 33–81 / 49–75 | 31–86 / 49–76 | 42–84 / 44–82 | 26–83 / 28–85 | 43–82 / 41–72 | 41–77 / 40–79 |
| Time since diagnosis, T (years) | 8.7 (5.9) / 12.6 (11.6) | — | 7.1 (6.2) / 7.0 (5.5) | — | 6.8 (5.2) / 6.7 (4.5) | — |
| MDS-UPDRS-III | 37.8 (22.1) / 37.6 (14.1) | — | 22.1 (9.9) / 23.3 (12.0) | — | 21.4 (11.5) / 18.1 (9.7) | — |

Source: ([Vasquez-Correa et al., 2020](document_1.txt)). Values are means with standard deviations in parentheses.

The extracted table also contains a row of mean ages (SD). Six values are legible — 60.7 (7.3), 61.4 (7.0), 66.2 (9.7), 62.6 (15.2), 60.1 (8.7) and 63.5 (11.1) — but the correspondence between individual values and specific PD/HC and gender subgroups is not fully recoverable from the extracted text, so these figures should be treated as indicative only ([Vasquez-Correa et al., 2020](document_1.txt)).

The clinical asymmetry is substantial and is explicitly acknowledged in the paper: the average MDS-UPDRS-III score of the Spanish patients is higher than that of the German and Czech patients, meaning the Spanish data contain patients with greater disease severity ([Vasquez-Correa et al., 2020](document_1.txt)). This severity gradient is used by the authors to explain performance differences across languages, and it also constitutes a confound that any cross-lingual comparison of these datasets must acknowledge.

## 7. Recording Conditions and Signal Pre-processing

Across all three corpora, recordings were captured in noise-controlled conditions and the speech signals were down-sampled to 16 kHz ([Vasquez-Correa et al., 2020](document_1.txt)). This uniformity of sampling rate is a genuine harmonising factor that makes the three corpora technically comparable at the signal level, notwithstanding their differing task protocols and clinical profiles.

## 8. Derived Data Representations

Beyond the raw corpora, the study constructs several derived datasets that function as the actual inputs to the classifiers.

### 8.1 Transition Segments

Speech signals were analysed through automatic detection of onset and offset transitions, which model patients' difficulties in starting and stopping vocal-fold vibration. The border between voiced and unvoiced frames was detected, and 80 ms of signal was taken to the left and right, forming segments of 160 ms in length ([Vasquez-Correa et al., 2020](document_1.txt)). These transition segments are the unit of analysis for both modelling approaches.

### 8.2 Hand-Crafted Feature Set (Baseline Model)

The baseline representation comprised 12 Mel-Frequency Cepstral Coefficients with their first and second derivatives, plus the log energy distributed into 22 Bark bands, giving 58 descriptors. Four statistical functionals — mean, standard deviation, skewness, and kurtosis — were computed for each descriptor, yielding a 232-dimensional feature vector per utterance ([Vasquez-Correa et al., 2020](document_1.txt)). Classification used a radial-basis SVM with margin parameter C = 10 and a Gaussian kernel parameter of 0.0001, evaluated under a speaker-independent 10-fold cross-validation strategy ([Vasquez-Correa et al., 2020](document_1.txt)).

### 8.3 Time–Frequency Representation (CNN Input)

The CNN inputs were short-time Fourier transform (STFT) spectrograms computed with 256 frequency bins, a window length of 16 ms and a step size of 4 ms, forming 41 time frames per transition. The spectrogram was then transformed to the Mel scale using 80 filters, producing inputs of size 80 × 41 ([Vasquez-Correa et al., 2020](document_1.txt)). The network consisted of four convolutional and max-pooling layers with dropout, followed by two fully connected layers and a softmax output, trained with cross-entropy loss using the Adam optimiser ([Vasquez-Correa et al., 2020](document_1.txt)).

## 9. How the Datasets Are Configured for the Transfer-Learning Experiment

The experimental design treats each corpus as both a base domain and a target domain. First, baseline and CNN models are trained on each language individually. Then, CNNs trained on one language are used to initialise models for the other two, with fine-tuning on the target language ([Vasquez-Correa et al., 2020](document_1.txt)). All speech exercises performed by participants were considered, and the final decision for each speaker was obtained by majority voting across exercises ([Vasquez-Correa et al., 2020](document_1.txt)). This means the effective evaluation unit is the speaker, not the individual utterance.

## 10. Reported Performance as Evidence About Dataset Utility

For within-language models, the paper reports that Spanish delivers the highest accuracy of the three languages, with similar accuracy between the baseline and the CNN; the highest German accuracy came from the baseline model (69.3%, SD 9.9; sensitivity 71.8%, SD 12.4; specificity 68.7%, SD 10.0; MCC 0.39), whereas for Czech the CNN was superior (68.5%, SD 14.1; sensitivity 94.0%, SD 13.5; specificity 42.0%, SD 33.2; MCC 0.43) against a Czech baseline of 61.0% (SD 12.5; sensitivity 64.5%, SD 19.5; specificity 60.2%, SD 11.9; MCC 0.27) ([Vasquez-Correa et al., 2020](document_1.txt)). The German CNN achieved 63.1% (SD 11.7) with markedly asymmetric sensitivity (43.1%) and specificity (83.1%) ([Vasquez-Correa et al., 2020](document_1.txt)). Exact Spanish figures are not recoverable from the extracted text, though the paper states the Spanish results are similar between baseline and CNN and are the highest of the three languages ([Vasquez-Correa et al., 2020](document_1.txt)).

Under transfer learning, accuracy improved by more than 8 percentage points for German (from 69.3% at baseline to 77.3% when fine-tuned from Spanish) and by more than 4.1 points for Czech (from 68.5% with the initial CNN to 72.6% when fine-tuned from Spanish); the highest German and Czech accuracies were both obtained with Spanish as the base language ([Vasquez-Correa et al., 2020](document_1.txt)). The authors attribute this to Spanish speakers having the best initial separability, so the other two languages benefit from the strongest starting model, and they note that transferred models were more balanced in specificity–sensitivity and had lower standard deviation, improving generalisation ([Vasquez-Correa et al., 2020](document_1.txt)).

ROC analysis reported the following areas under the curve: for target Spanish, a Spanish-only baseline AUC of 0.824 and a German-to-Spanish AUC of 0.779; for target German, a German-only AUC of 0.584, Czech-to-German 0.792, and Spanish-to-German 0.823; and for target Czech, a Czech-only AUC of 0.764, German-to-Czech 0.762, and Spanish-to-Czech 0.831 ([Vasquez-Correa et al., 2020](document_1.txt)). The paper states that the AUC for target Spanish is slightly higher when the base language is Czech, although the corresponding numeric value is corrupted in the extracted text ([Vasquez-Correa et al., 2020](document_1.txt)).

## 11. Critical Evaluation of the Datasets and Sources

Several considerations bear on the reliability and reuse potential of these datasets.

First, a documented inconsistency exists between the primary source and the secondary note regarding the German cohort. The primary paper reports 88 PD and 88 HC speakers, corroborated by its gender table, while the third-party note reports 44 PD and 44 HC ([Vasquez-Correa et al., 2020](document_1.txt); [Research note](document_2.txt)). The primary source should be preferred; the note's figure is not reproducible from the paper and appears erroneous. This is a concrete illustration of why secondary summaries of dataset composition should not be relied upon without verification.

Second, the third-party note omits several dataset-relevant details that the primary source provides, including the specific speech tasks in each language, recording conditions, sampling rate, and the clinical scores ([Research note](document_2.txt)). It is accurate on the Spanish corpus (PC-GITA, 50 PD and 50 HC, Colombian Spanish native speakers) and on the Czech cohort (50 PD and 50 HC), but incomplete overall ([Research note](document_2.txt)).

Third, comparability across the three corpora is limited by design differences. The three protocols use different task sets; the Spanish protocol has the largest battery (10 sentences, six rapid-repetition conditions, a 36-word text, and a monologue), while the Czech protocol has the smallest (rapid syllable repetition, an 80-word read text, and a monologue) ([Vasquez-Correa et al., 2020](document_1.txt)). The severity of disease also differs, with mean MDS-UPDRS-III around 37.6–37.8 for Spanish patients versus approximately 21.4–23.3 for German and 18.1–21.4 for Czech patients ([Vasquez-Correa et al., 2020](document_1.txt)). Consequently, higher Spanish classification accuracy may reflect greater disease severity rather than an inherently more informative corpus, and the cross-lingual transfer gains may be partly attributable to this asymmetry.

Fourth, the Spanish patients were recorded in the ON state, and therefore the corpus documents medicated speech rather than untreated symptomatology ([Vasquez-Correa et al., 2020](document_1.txt)). Whether the German and Czech cohorts were similarly medicated is not stated in the provided information.

Fifth, the authors themselves identify linguistic bias as a risk, noting that Czech and German are richer than Spanish in consonant production, which could make consonant sounds easier for Czech PD patients to produce than for Spanish PD patients ([Vasquez-Correa et al., 2020](document_1.txt)). This has direct implications for the validity of pooling or transferring across these corpora.

Sixth, the provided information contains no statement about public availability, licensing, or access conditions for any of the three corpora, which limits assessment of reproducibility. The statistical power of the individual corpora is also modest (100 speakers for Spanish and Czech, 176 for German), and speaker-independent 10-fold cross-validation is used for the SVM baseline ([Vasquez-Correa et al., 2020](document_1.txt)).

## 12. Conclusion

The study is built on three language-specific speech corpora: the Colombian Spanish PC-GITA corpus (50 PD patients, 50 healthy controls), a German corpus (88 PD patients, 88 healthy controls according to the primary source), and a Czech corpus (50 PD patients, 50 healthy controls), all recorded under noise-controlled conditions at 16 kHz and clinically annotated using MDS-UPDRS-III ([Vasquez-Correa et al., 2020](document_1.txt)). From these corpora, the authors derive 160 ms voiced–unvoiced transition segments, a 232-dimensional hand-crafted feature representation for the SVM baseline, and 80 × 41 Mel-scale spectrograms for CNN training ([Vasquez-Correa et al., 2020](document_1.txt)). The three corpora are deployed both as within-language training sets and as source and target domains in a cross-lingual transfer-learning scheme, with speaker-level majority voting across speech tasks ([Vasquez-Correa et al., 2020](document_1.txt)). Analysts seeking to reuse these data should observe three cautions: the German cohort size is misreported in the secondary note; the corpora differ in task protocol, disease severity, and medication state; and no access or licensing information is available in the provided materials.

## References

Third-party research note: Convolutional neural networks and a transfer learning strategy to classify Parkinson's disease from speech in three different languages [Unpublished research note]. (document_2.txt).

Vasquez-Correa, J. C., Arias-Vergara, T., Rios-Urrego, C. D., Schuster, M., Rusz, J., Orozco-Arroyave, J. R., & Nöth, E. (2020). *Convolutional neural networks and a transfer learning strategy to classify Parkinson's disease from speech in three different languages* [Preprint]. arXiv:2002.04374v1. (document_1.txt).