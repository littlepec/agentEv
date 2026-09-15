# Datasets Used in “Convolutional Neural Networks and a Transfer Learning Strategy to Classify Parkinson’s Disease from Speech in Three Different Languages”

## 1. Introduction: Locating the Data Behind the Study

The study under review is a machine-learning paper, first posted as an arXiv preprint on 11 February 2020, that proposes a convolutional neural network (CNN) pipeline plus a cross-lingual transfer-learning scheme for separating Parkinson’s disease (PD) patients from healthy control (HC) speakers on the basis of speech ([Vasquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)). Because the central contribution of the work is a *cross-lingual* strategy, the datasets are not incidental to the study; they are the object of comparison. The authors deliberately assembled three separately collected speech corpora, one per language — Spanish, German, and Czech — each recorded under noise-controlled conditions, each containing both PD patients and healthy speakers, and each accompanied by expert neurological assessment ([Vasquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)). A third-party research note summarising the same study confirms the same three-corpus structure and the same speaker counts for each language ([Third-Party Research Note, n.d.](#references)).

The purpose of this report is to identify precisely which datasets were used, to describe their sources, structure, features, and clinical annotations, and to evaluate their limitations and suitability for the classification task they were asked to support. All claims below are drawn exclusively from the two supplied documents: the preprint text (`document_1.txt`) and the accompanying research note (`document_2.txt`).

## 2. Inventory of Datasets Used

Three language-specific datasets constitute the entire data foundation of the study. Table 1 summarises their identities and sizes.

**Table 1. Datasets used in the study**

| Language | Dataset / corpus | PD patients | Healthy controls | Total speakers | Reference cited in the study |
|---|---|---|---|---|---|
| Spanish | PC-GITA corpus | 50 | 50 | 100 | Orozco-Arroyave et al. (2014), as cited in ([Vasquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)) |
| German | German speech recordings (Germany) | 88 | 88 | 176 | Skodda, Visser, & Schlegel (2011), as cited in ([Vasquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)) |
| Czech | Czech speech recordings | 50 | 50 | 100 | Rusz (2018), as cited in ([Vasquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)) |
| **Total** | — | **188** | **188** | **376** | — |

The totals in the final row are arithmetic derivations from the per-language counts reported in the paper and corroborated by the research note; the documents themselves report 50/50 for Spanish, 88/88 for German, and 50/50 for Czech ([Third-Party Research Note, n.d.](#references)). The corpus is therefore perfectly class-balanced within each language (equal numbers of PD and HC speakers in every subset), although it is not balanced across languages, since the German material is 76% larger than either the Spanish or the Czech material.

## 3. The Spanish Dataset: PC-GITA

### 3.1 Provenance and composition

The Spanish data come from the PC-GITA corpus, which contains utterances from 50 PD patients and 50 HC speakers, all Colombian Spanish native speakers ([Vasquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)). The corpus is the most frequently reused of the three within the study’s own literature review, having previously supported phonation analyses, forced-alignment phonetic models, and deep-learning articulation models with reported accuracies of approximately 77–81% ([Vasquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)).

### 3.2 Speech tasks

Participants in PC-GITA were asked to complete a comparatively rich protocol: they pronounced a total of ten sentences; performed rapid repetition of the syllables /pa-ta-ka/, /pe-ta-ka/, /pa-ka-ta/, /pa/, /ta/, and /ka/; read one text containing 36 words; and produced a monologue ([Vasquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)). A notable clinical detail is that all PD patients were recorded in the ON state, that is, while under the effect of their daily medication ([Vasquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)). This matters for interpretation, because ON-state recordings tend to attenuate motor speech symptoms relative to OFF-state recordings, which can make classification harder but also more clinically realistic for treated populations.

### 3.3 Clinical profile

The Spanish cohort shows the highest disease severity of the three datasets. Mean MDS-UPDRS-III scores were 37.8 (SD 22.1) for men and 37.6 (SD 14.1) for women, against time since diagnosis of 8.7 (SD 5.9) years for men and 12.6 (SD 11.6) years for women ([Vasquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)). Age ranges were 33–81 years (PD men), 49–75 years (PD women), 31–86 years (HC men), and 49–76 years (HC women) ([Vasquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)).

## 4. The German Dataset

### 4.1 Provenance and composition

The German data comprise speech recordings of 88 PD patients and 88 HC speakers from Germany ([Vasquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)). This is the largest of the three datasets, both in total speakers (176) and in the number of PD participants. The recordings are associated with the vowel-articulation work of Skodda, Visser, and Schlegel (2011), as cited in the study ([Vasquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)).

### 4.2 Speech tasks

German participants performed four speech tasks: rapid repetition of /pa-ta-ka/, five sentences, one text with 81 words, and a monologue ([Vasquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)). The German protocol therefore shares the diadochokinetic syllable task, a read text, and a monologue with the Spanish protocol, but uses a longer reading passage (81 words versus 36) and fewer sentence repetitions (five versus ten).

### 4.3 Clinical profile

Mean time since diagnosis was 7.1 (SD 6.2) years for men and 7.0 (SD 5.5) years for women, and mean MDS-UPDRS-III scores were 22.1 (SD 9.9) and 23.3 (SD 12.0) respectively ([Vasquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)). Age ranges were 42–84 years (PD men), 44–82 years (PD women), 26–83 years (HC men), and 28–85 years (HC women) ([Vasquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)). Severity is thus markedly lower than in the Spanish cohort.

## 5. The Czech Dataset

### 5.1 Provenance and composition

The Czech material contains a total of 100 native Czech speakers, comprising 50 PD patients and 50 healthy controls ([Vasquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)). The recordings are associated with Rusz’s habilitation thesis on detecting speech disorders in early Parkinson’s disease ([Vasquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)).

### 5.2 Speech tasks

Czech participants completed the smallest task battery of the three: rapid repetition of the syllables /pa-ta-ka/, a read text with 80 words, and a monologue ([Vasquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)). The absence of the sentence-repetition block present in the Spanish and German protocols makes the Czech corpus the least redundant in task variety of the three.

### 5.3 Clinical profile

Mean time since diagnosis was 6.8 (SD 5.2) years for men and 6.7 (SD 4.5) years for women; mean MDS-UPDRS-III scores were 21.4 (SD 11.5) and 18.1 (SD 9.7) respectively ([Vasquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)). Age ranges were 43–82 years (PD men), 41–72 years (PD women), 41–77 years (HC men), and 40–79 years (HC women) ([Vasquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)). The Czech PD group therefore has the lowest average symptom severity of the three.

## 6. Comparative Structure of the Three Datasets

**Table 2. Demographic and clinical characteristics reported for the three datasets**

| Characteristic | Spanish (PC-GITA) | German | Czech |
|---|---|---|---|
| PD / HC speakers | 50 / 50 | 88 / 88 | 50 / 50 |
| PD sex split (M / F) | 25 / 25 | 41 / 47 | 20 / 30 |
| HC sex split (M / F) | 25 / 25 | 44 / 44 | 30 / 20 |
| Age range, PD men | 33–81 | 42–84 | 43–82 |
| Age range, PD women | 49–75 | 44–82 | 41–72 |
| Age range, HC men | 31–86 | 26–83 | 41–77 |
| Age range, HC women | 49–76 | 28–85 | 40–79 |
| Time since diagnosis, M, years | 8.7 (5.9) | 7.1 (6.2) | 6.8 (5.2) |
| Time since diagnosis, F, years | 12.6 (11.6) | 7.0 (5.5) | 6.7 (4.5) |
| MDS-UPDRS-III, M | 37.8 (22.1) | 22.1 (9.9) | 21.4 (11.5) |
| MDS-UPDRS-III, F | 37.6 (14.1) | 23.3 (12.0) | 18.1 (9.7) |

All values in Table 2 are taken from Table 1 of the source paper ([Vasquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)). Two features of this table deserve emphasis. First, the Spanish dataset is both the smallest balanced PD/HC set and the most severely affected: its mean MDS-UPDRS-III is roughly 15 points above the German and Czech means. The authors explicitly attribute the higher classification accuracy obtained in Spanish to this severity difference ([Vasquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)). Second, the German and Czech datasets differ in sex composition, with the Czech PD group skewed toward women (20 men, 30 women) while the Czech HC group is skewed toward men (30 men, 20 women); this is a potential confounding factor not addressed in the study itself.

The mean ages of the subgroups are also reported in the source table, with values such as 60.7 (7.3), 61.4 (7.0), 66.2 (9.7), 62.6 (15.2), 60.1 (8.7) and 63.5 (11.1) appearing alongside the range data ([Vasquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)). The plain-text rendering of that table does not align these six mean values unambiguously with individual subgroups, so they are reported here without firm group attribution; the age ranges in Table 2 are unambiguous.

## 7. Acquisition and Derived Representations

All recordings across the three datasets were captured under noise-controlled conditions and down-sampled to 16 kHz, and all patients were evaluated by an expert neurologist according to the third section of the Movement Disorder Society–sponsored revision of the Unified Parkinson’s Disease Rating Scale (MDS-UPDRS-III) ([Vasquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)). The importance of this harmonisation is that a single clinical instrument was applied across three languages, making the severity columns in Table 2 directly comparable.

Two kinds of derived data were extracted from the raw corpora. The first is the segmentation layer: the analysis focuses on onset and offset transitions between voiced and unvoiced frames, detected from the presence of the fundamental frequency in short-time frames, with 80 ms of signal taken to each side to form 160 ms segments ([Vasquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)). The second is the feature or representation layer. For the baseline model, 12 Mel-Frequency Cepstral Coefficients with first and second derivatives plus log energy distributed into 22 Bark bands yield 58 descriptors, which are expanded by mean, standard deviation, skewness, and kurtosis into a 232-dimensional vector per utterance ([Vasquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)). For the CNN, a short-time Fourier transform with 256 frequency bins (16 ms window, 4 ms step, 41 time frames) is converted to the Mel scale with 80 filters, producing an 80 × 41 spectrogram as network input ([Vasquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)).

## 8. How the Datasets Were Partitioned and Used

Within each language, the baseline support vector machine (radial basis kernel, C = 10, γ = 0.0001) was evaluated with speaker-independent 10-fold cross-validation ([Vasquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)). In the CNN experiments, all speech exercises performed by a participant were classified, and the final decision for each speaker was obtained by majority voting across exercises, meaning that the effective unit of analysis is the speaker rather than the utterance ([Vasquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)). In the transfer-learning experiments, a CNN trained on one language (the base) was used to initialise models for each of the other two languages (the targets) and then fine-tuned with utterances from the target language ([Vasquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)).

## 9. Classification Results Obtained with These Datasets

**Table 3. Individually trained models (% accuracy, with standard deviation)**

| Language | Baseline (SVM) accuracy | CNN accuracy |
|---|---|---|
| German | 69.3 (9.9) | 63.1 (11.7) |
| Czech | 61.0 (12.5) | 68.5 (14.1) |
| Spanish | Highest of the three; baseline and CNN described as similar | Highest of the three; baseline and CNN described as similar |

The figures for German and Czech are read directly from Table 3 of the source ([Vasquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)). The source text states that the highest accuracy for German was obtained with the baseline model, that the CNN produced the highest accuracy for Czech, and that Spanish showed the highest accuracy overall with similar baseline and CNN performance ([Vasquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)). The class balance behind these accuracies was poor: the German CNN reached sensitivity 43.1% against specificity 83.1%, and the Czech CNN reached sensitivity 94.0% against specificity 42.0% ([Vasquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)).

Transfer learning improved results chiefly when Spanish was the base language: accuracy for German rose from 69.3% at baseline to 77.3% when fine-tuned from Spanish (an improvement of more than 8 percentage points), and accuracy for Czech rose from 68.5% with the initial CNN to 72.6% when fine-tuned from Spanish (more than 4.1 percentage points) ([Vasquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)). Area-under-the-ROC-curve values reported for German as target were 0.584 (German alone), 0.792 (Czech base) and 0.823 (Spanish base); for Czech as target they were 0.764 (Czech alone), 0.762 (German base) and 0.831 (Spanish base) ([Vasquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)). When Spanish was the target language, the highest AUC was obtained with a Czech base model, while the AUC of the Spanish model alone was 0.824 and that of the German-based transfer model was 0.779 ([Vasquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)). The transferred models also showed lower variance and better sensitivity–specificity balance ([Vasquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)).

## 10. Assessment: Strengths, Limitations, and Suitability

The strongest feature of this dataset collection is its design. Three languages, three independent clinical cohorts, identical down-sampling, noise-controlled recording conditions, and one uniform clinical severity instrument make the collection genuinely suitable for the cross-lingual question the authors pose, and the perfect within-language PD/HC balance (50/50, 88/88, 50/50) removes class-prior distortion as an explanation for accuracy differences ([Vasquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)). The inclusion of an expert MDS-UPDRS-III rating for every patient also gives the data a ready-made severity covariate, which the authors exploit to explain why Spanish is the easiest language to classify ([Vasquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)).

The limitations are equally clear. First, the three subsets are not exchangeable samples: they differ in speaker count (176 German versus 100 Spanish and 100 Czech), in severity (MDS-UPDRS-III means of roughly 22–38 across groups), in sex composition, particularly in the Czech cohort, and in task battery (four tasks in German, several in Spanish, three in Czech) ([Vasquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)). Because of this, an unknown portion of any “language effect” may actually be a severity, task, or demographic effect. The authors themselves concede that language-specific phonetic differences — Czech and German being phonetically richer than Spanish in consonant production — can bias cross-lingual comparisons ([Vasquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)). Second, all Spanish patients were recorded in the ON state, which is not stated for the German and Czech cohorts, so pharmacological state is an uncontrolled variable ([Vasquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)). Third, the paper’s transfer-learning conclusion is explicitly conditional: the strategy improved target-language accuracy only when the base model was “robust enough,” which in practice meant the Spanish base ([Vasquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)). Fourth, from the documents supplied, no licence, access route, or data-availability statement for the three corpora is reported, so reproducibility depends on obtaining PC-GITA and the German and Czech recordings from their original publishers. Finally, the plain-text rendering of Tables 3 and 4 in the supplied documents is partially corrupted, which prevents an exact cell-by-cell reproduction of every result; the figures reported above are those that are legible or corroborated by the narrative text ([Vasquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)).

In the reviewer’s assessment, the collection is well suited for within-language PD-versus-HC classification and for demonstrating that transfer learning can help when a strong base language exists, but it is only moderately suited for strong causal claims about language itself, because severity, cohort size, sex ratio, and task design co-vary with language.

## 11. Conclusion

The study uses exactly three datasets: the PC-GITA corpus of Colombian Spanish (50 PD, 50 HC), a German corpus (88 PD, 88 HC), and a Czech corpus (50 PD, 50 HC), together covering 376 speakers, 188 of them with Parkinson’s disease, all annotated with MDS-UPDRS-III severity by expert neurologists and all recorded under noise-controlled conditions at 16 kHz ([Vasquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374); [Third-Party Research Note, n.d.](#references)). From these recordings the authors derive 160 ms voiced–unvoiced transition segments, 232-dimensional hand-crafted feature vectors for an SVM baseline, and 80 × 41 Mel spectrograms for a CNN whose weights are then transferred across languages. The datasets are balanced within language, clinically annotated, and multilingual — the properties that make the study’s transfer-learning experiment possible — but they are unbalanced across languages in size, severity, sex composition, and task design, and the resulting cross-lingual comparisons should be read with those confounds in mind ([Vasquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)).

## References

Vasquez-Correa, J. C., Arias-Vergara, T., Rios-Urrego, C. D., Schuster, M., Rusz, J., Orozco-Arroyave, J. R., & Noth, E. (2020). *Convolutional neural networks and a transfer learning strategy to classify Parkinson’s disease from speech in three different languages* (arXiv:2002.04374v1) [Preprint]. arXiv. https://arxiv.org/abs/2002.04374 (Source: document_1.txt)

Third-party research note: Convolutional neural networks and a transfer learning strategy to classify Parkinson’s disease from speech in three different languages [Research note]. (n.d.). (Source: document_2.txt)