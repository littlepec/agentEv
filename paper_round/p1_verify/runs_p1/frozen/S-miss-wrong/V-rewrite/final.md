# Datasets Used in the Cross-Lingual Transfer Learning Study of Parkinson's Disease Speech Classification

## Introduction

The evidence supplied describes a study applying convolutional neural networks (CNNs) and a cross-lingual transfer learning strategy to classify Parkinson's disease (PD) from speech. Because the central experimental variable is *language*, the datasets are three language-specific speech collections: Spanish, German, and Czech ([document_1.txt](#ref-doc1)). This report identifies those datasets, describes their composition, recording conditions, annotation, and preprocessing, documents their use in the experiments, and notes limitations.

The evidence base consists of two documents: an extended technical extract of the study itself ([document_1.txt](#ref-doc1)) and a third-party research note ([document_2.txt](#ref-doc2)). Where the two overlap, they are consistent.

## The Three Core Speech Datasets

The study states that "speech recordings of patients in three different languages are considered: Spanish, German, and Czech," captured under noise-controlled conditions and down-sampled to 16 kHz ([document_1.txt](#ref-doc1)). Patients in all three datasets were evaluated by a neurologist expert using the MDS-UPDRS-III ([document_1.txt](#ref-doc1)).

### Spanish: The PC-GITA Corpus

The Spanish data come from the PC-GITA corpus ([document_1.txt](#ref-doc1)). PC-GITA contains utterances from 50 PD patients and 50 HC speakers, Colombian Spanish native speakers — 100 speakers in a balanced 1:1 design ([document_1.txt](#ref-doc1)). The corpus is attributed to the Spanish speech database of Orozco-Arroyave and colleagues ([document_1.txt](#ref-doc1)).

PC-GITA had previously been used in phonation/tremor analysis with time–frequency representations, energy and entropy features classified with GMMs and SVMs, reporting accuracies up to 77% ([document_1.txt](#ref-doc1)).

### German Speech Recordings

The German data consist of speech recordings from 88 PD patients and 88 HC speakers from Germany ([document_1.txt](#ref-doc1)). The German data are associated with the vowel-articulation work of Skodda, Visser and Schlegel in the *Journal of Voice* ([document_1.txt](#ref-doc1)). The German participants performed four speech tasks: rapid repetition of /pa-ta-ka/, 5 sentences, one text with 81 words, and a monologue ([document_1.txt](#ref-doc1)).

### Czech Speech Recordings

The Czech dataset comprises 100 native Czech speakers (50 PD, 50 HC) ([document_1.txt](#ref-doc1)). Speech tasks included rapid repetition of /pa-ta-ka/, a read text with 80 words, and a monologue ([document_1.txt](#ref-doc1)). The Czech data derive from the work of Rusz ([document_1.txt](#ref-doc1)).

### Comparative Summary of Dataset Composition

| Dataset / language | Corpus or source | PD patients | Healthy controls | Total speakers | Native-speaker background | Documented speech tasks |
|---|---|---|---|---|---|---|
| Spanish | PC-GITA | 50 | 50 | 100 | Colombian Spanish | 10 sentences; /pa-ta-ka/, /pe-ta-ka/, /pa-ka-ta/, /pa/, /ta/, /ka/; 36-word text; monologue |
| German | German speech recordings ([18]) | 88 | 88 | 176 | German | /pa-ta-ka/; 5 sentences; 81-word text; monologue |
| Czech | Czech speech recordings ([19]) | 50 | 50 | 100 | Czech | /pa-ta-ka/; 80-word read text; monologue |

*Sources: ([document_1.txt](#ref-doc1))*

The three corpora range from 100 to 176 speakers, and all three are balanced between classes.

## Clinical Annotation and Severity Distribution

All three datasets share a common clinical anchor: each participant was rated by a neurologist according to the MDS-UPDRS-III ([document_1.txt](#ref-doc1)). The authors attribute differing results across languages to their Table 1: the average MDS-UPDRS-III score of Spanish patients is higher than that of German and Czech patients, meaning the Spanish data contain patients with greater disease severity ([document_1.txt](#ref-doc1)).

The study documents that dysarthria effects in PD speech include increased acoustic noise, reduced intensity, harsh and breathy voice quality, increased voice nasality, monopitch, monoloudness, speech rate disturbances, imprecise articulation of consonants, and involuntary pauses ([document_1.txt](#ref-doc1)).

## Recording Conditions and Preprocessing Pipeline

All recordings were captured under noise-controlled conditions and down-sampled to 16 kHz ([document_1.txt](#ref-doc1)). Segmentation was based on automatic detection of onset and offset transitions, relying on the presence of the fundamental frequency in short-time frames ([document_1.txt](#ref-doc1)). The border between voiced and unvoiced frames is identified, and 80 ms of signal is taken to the left and right, producing 160 ms segments ([document_1.txt](#ref-doc1)).

For the CNN branch, STFT representations are computed with 256 frequency bins, window length 16 ms, step size 4 ms, forming 41 time frames per transition ([document_1.txt](#ref-doc1)). Each spectrogram is transformed to the Mel scale using 80 filters, giving a final input of 80 × 41 ([document_1.txt](#ref-doc1)).

| Parameter | Value |
|---|---|
| Sampling rate | 16 kHz |
| Segment definition | 80 ms either side of the voiced/unvoiced border |
| Segment length | 160 ms |
| STFT frequency bins | 256 |
| STFT window length | 16 ms |
| STFT step size | 4 ms |
| Time frames per transition | 41 |
| Mel filters | 80 |
| Final spectrogram size | 80 × 41 |

*Source: ([document_1.txt](#ref-doc1))*

## How the Datasets Were Used in the Experiments

Baseline and CNN models are first trained per language individually. Then trained CNNs are used as base models in a transfer learning strategy for the other two languages; all speech exercises were considered, and the final decision per speaker used majority voting across exercises ([document_1.txt](#ref-doc1)).

| Language | Model | Acc (%) | Sen (%) | Spe (%) | MCC |
|---|---|---|---|---|---|
| Spanish | Baseline (SVM) | 73.7 (13.0) | 74.5 (16.7) | 77.1 (16.2) | 0.50 |
| Spanish | CNN | 71.0 (15.9) | 74.0 (25.0) | 68.0 (28.6) | 0.42 |
| German | Baseline (SVM) | 69.3 (9.9) | 71.8 (12.4) | 68.7 (10.0) | 0.39 |
| German | CNN | 63.1 (11.7) | 43.1 (38.0) | 83.1 (17.7) | 0.30 |
| Czech | Baseline (SVM) | 61.0 (12.5) | 64.5 (19.5) | 60.2 (11.9) | 0.27 |
| Czech | CNN | 68.5 (14.1) | 94.0 (13.5) | 42.0 (33.2) | 0.43 |

*Source: ([document_1.txt](#ref-doc1))*

| Base language (pre-training) | Target language (fine-tuning) | Acc (%) | Sen (%) | Spe (%) | MCC |
|---|---|---|---|---|---|
| German | Spanish | 70.0 (12.5) | 62.0 (19.9) | 78.0 (23.9) | 0.41 |
| German | Czech | 72.0 (13.1) | 67.0 (11.6) | 78.0 (23.9) | 0.46 |
| Spanish | German | 77.3 (11.3) | 86.2 (13.8) | 68.3 (14.3) | 0.57 |
| Spanish | Czech | 76.7 (7.9) | 87.5 (11.0) | 66.0 (15.6) | 0.55 |
| Czech | Spanish | 72.6 (13.9) | 82.0 (14.8) | 62.0 (28.9) | 0.46 |
| Czech | German | 70.7 (14.5) | 80.0 (16.3) | 62.5 (26.3) | 0.38 |

*Source: ([document_1.txt](#ref-doc1))*

The best German model improves from 69.3% (baseline) to 77.3% when initialised with Spanish utterances — an improvement of roughly 8 percentage points over the strongest German-only result ([document_1.txt](#ref-doc1)). The Czech target improves from 68.5% (CNN) to 72.6% under the Spanish base, an increase of just over 4 percentage points ([document_1.txt](#ref-doc1)). The study claims transfer learning improved accuracy "in up to 8%" and, separately, "over 8%" ([document_1.txt](#ref-doc1)). The study reports transfer results are more balanced in specificity/sensitivity with lower variance, and that transfer helped only when the base model was robust enough ([document_1.txt](#ref-doc1)).

## Datasets Referenced in the Related Work but Not Used

The reference list includes the Parkinson speech dataset with multiple types of sound recordings by Sakar and colleagues ([document_1.txt](#ref-doc1)). This corpus is cited in related work; the extracts do not indicate it contributes speakers to the present experiments. The study also references prior work modelling the same three-language data with a deep-learning articulation approach, reporting accuracies between 70% and 89% depending on language, but below 60% in a language-independent scenario ([document_1.txt](#ref-doc1)).

## Limitations and Analytical Commentary

First, the datasets are not matched on clinical severity: Spanish patients have higher average MDS-UPDRS-III scores than German and Czech patients, confounding language with disease severity ([document_1.txt](#ref-doc1)). Second, sample sizes are modest (100–176 speakers per language), with substantial standard deviations in several conditions (e.g., specificity 42.0 with SD 33.2 for the Czech CNN) ([document_1.txt](#ref-doc1)). Third, the German task inventory is documented in the primary source (four tasks), though task-level comparability across corpora remains imperfect.

The study proposes future work: more robust base models via hyper-parameter optimisation such as Bayesian optimisation, base models trained on two languages, evaluation of PD staging based on MDS-UPDRS-III or dysarthria severity, and transfer learning across diseases ([document_1.txt](#ref-doc1)).

## Conclusion

The study draws on three language-specific speech datasets of PD patients and healthy controls: the Spanish PC-GITA corpus (50 PD, 50 HC, Colombian Spanish speakers), German speech recordings (88 PD, 88 HC), and Czech speech recordings (50 PD, 50 HC native Czech speakers performing /pa-ta-ka/ repetition, an 80-word reading task and a monologue) ([document_1.txt](#ref-doc1)). All three were recorded under noise-controlled conditions, down-sampled to 16 kHz, clinically annotated with the MDS-UPDRS-III, and processed identically into 160 ms voiced/unvoiced transition segments and 80 × 41 Mel spectrograms. The datasets are balanced in class composition but not in disease severity, which plausibly explains both the higher baseline accuracy for Spanish and the disproportionate success of the Spanish-initialised transfer models, which raised target-language accuracy by up to roughly 8 percentage points over the strongest monolingual German result ([document_1.txt](#ref-doc1)).

## References

<a id="ref-doc1"></a>document_1.txt. (n.d.). *Source document 1: Convolutional neural networks and a transfer learning strategy to classify Parkinson's disease from speech in three different languages* [Unpublished manuscript extract].

<a id="ref-doc2"></a>document_2.txt. (n.d.). *Source document 2: Third-party research note on convolutional neural networks and a transfer learning strategy to classify Parkinson's disease from speech in three different languages* [Research note].