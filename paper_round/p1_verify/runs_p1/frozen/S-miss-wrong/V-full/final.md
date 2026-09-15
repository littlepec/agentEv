# Datasets Used in the Cross-Lingual Transfer Learning Study of Parkinson's Disease Speech Classification

## Introduction

The body of evidence supplied for this report describes a study that applies convolutional neural networks (CNNs) and a cross-lingual transfer learning strategy to classify Parkinson's disease (PD) from speech. Because the central experimental variable in that work is *language*, the datasets it relies upon are not a single corpus but a set of three parallel, language-specific speech collections: Spanish, German, and Czech ([document_1.txt](#ref-doc1)). The purpose of this report is to identify those datasets precisely, to describe their composition, recording conditions, annotation protocols, and preprocessing pipeline, to document how each was used in the baseline and transfer learning experiments, and to note the limitations that follow from the way the data are assembled.

The evidence base consists of two documents: an extended technical extract of the study itself ([document_1.txt](#ref-doc1)) and a third-party research note summarising the study's dataset-related questions ([document_2.txt](#ref-doc2)). Where the two overlap, they are consistent with one another, which increases confidence in the figures reported below.

## The Three Core Speech Datasets

The study explicitly states that "speech recordings of patients in three different languages are considered: Spanish, German, and Czech," and that all recordings were captured under noise-controlled conditions and down-sampled to 16 kHz ([document_1.txt](#ref-doc1)). The patients in all three datasets were evaluated by a neurologist expert using the third section of the Movement Disorder Society–sponsored revision of the Unified Parkinson's Disease Rating Scale (MDS-UPDRS-III) ([document_1.txt](#ref-doc1)).

### Spanish: The PC-GITA Corpus

The Spanish portion of the data comes from the PC-GITA corpus ([document_1.txt](#ref-doc1)). PC-GITA contains utterances from 50 PD patients and 50 healthy control (HC) speakers, all Colombian Spanish native speakers, giving a total of 100 speakers and a perfectly balanced 1:1 case–control design ([document_1.txt](#ref-doc1)). The corpus is attributed to the Spanish speech database described by Orozco-Arroyave and colleagues for the analysis of people suffering from Parkinson's disease ([document_1.txt](#ref-doc1)).

PC-GITA is not exclusive to this study. It had previously been used in phonation and tremor analysis work based on several time–frequency representations, in which energy and entropy features were classified with Gaussian mixture models (GMMs) and support vector machines (SVMs), reporting accuracies of up to 77% ([document_1.txt](#ref-doc1)). This prior use matters for interpreting the present results, because the Spanish data are therefore the best-characterised and arguably the most methodologically mature of the three language subsets.

### German Speech Recordings

The German data consist of speech recordings from 88 PD patients and 88 HC speakers ([document_1.txt](#ref-doc1)). As with the Spanish set, the case–control distribution is balanced, yielding 176 speakers in total. The German data are associated with the vowel-articulation work of Skodda, Visser and Schlegel published in the *Journal of Voice* ([document_1.txt](#ref-doc1)). The supplied extracts do not itemise the specific speech tasks performed by the German participants in the way that they do for the Czech participants; the report therefore treats the German set as a balanced 44/44 PD–HC corpus without a documented task list in the available evidence.

### Czech Speech Recordings

The Czech dataset comprises a total of 100 native Czech speakers, of whom 50 are PD patients and 50 are healthy controls ([document_1.txt](#ref-doc1); [document_2.txt](#ref-doc2)). Unlike the other two sets, the specific elicitation tasks are documented: participants performed the rapid repetition of the syllables /pa-ta-ka/, read a text of 80 words, and produced a monologue ([document_1.txt](#ref-doc1)). The Czech data derive from the work of Rusz and colleagues on detecting speech disorders in early Parkinson's disease by acoustic analysis ([document_1.txt](#ref-doc1)).

It is notable that the Czech protocol combines a diadochokinetic task (rapid syllable repetition), a controlled reading task, and a spontaneous-speech task. This heterogeneity is methodologically valuable: it allows the classification pipeline to draw on complementary articulatory, prosodic and fluency information, and it explains why the study aggregates decisions across exercises.

### Comparative Summary of Dataset Composition

The table below consolidates the composition of the three datasets as reported in the supplied documents.

| Dataset / language | Corpus or source | PD patients | Healthy controls | Total speakers | Native-speaker background | Documented speech tasks |
|---|---|---|---|---|---|---|
| Spanish | PC-GITA | 50 | 50 | 100 | Colombian Spanish | Not itemised in the extract (all exercises used for classification) |
| German | German speech recordings ([18]) | 88 | 88 | 176 | German | Not itemised in the extract |
| Czech | Czech speech recordings ([19]) | 50 | 50 | 100 | Czech | /pa-ta-ka/ rapid repetition; 80-word read text; monologue |

*Sources: ([document_1.txt](#ref-doc1); [document_2.txt](#ref-doc2))*

Two observations follow directly from this table. First, the three corpora are of comparable size (100–176 speakers), which is important because transfer learning performance depends heavily on the representativeness of the base model. Second, all three are balanced between classes, so accuracy is an interpretable metric in the baseline condition and any drift toward sensitivity or specificity reflects genuine model behaviour rather than class priors.

## Clinical Annotation and Severity Distribution

All three datasets share a common clinical anchor: each participant was rated by a neurologist according to the MDS-UPDRS-III ([document_1.txt](#ref-doc1)). This shared scale is what makes cross-lingual pooling analytically defensible, since it provides a language-independent measure of disease severity that can be used to explain differences in classification performance between languages.

That explanatory role is explicit in the study's own interpretation. The authors attribute the differing results across the three languages to the information summarised in their Table 1: the average MDS-UPDRS-III score of the Spanish patients is higher than that of the German and Czech patients, meaning the Spanish data contain patients with greater disease severity ([document_1.txt](#ref-doc1)). Since more severe disease generally produces more marked dysarthric symptoms, the Spanish subset is the "easiest" of the three languages to classify — a pattern confirmed by the baseline results described later in this report.

The study also documents that the speech effects of dysarthria in PD include increased acoustic noise, reduced intensity, harsh and breathy voice quality, increased voice nasality, monopitch, monoloudness, speech rate disturbances, imprecise articulation of consonants, and the involuntary introduction of pauses ([document_1.txt](#ref-doc1)). These are the clinical phenomena that the automated pipeline is designed to capture, and the MDS-UPDRS-III scores provide the corresponding clinical ground truth.

## Recording Conditions and Preprocessing Pipeline

The three datasets were harmonised before modelling. All recordings were captured under noise-controlled conditions and down-sampled to 16 kHz ([document_1.txt](#ref-doc1)). Segmentation was based on the automatic detection of onset and offset transitions, which model the patients' difficulties in starting and stopping the movement of the vocal folds; the detection of these transitions relies on the presence of the fundamental frequency of speech in short-time frames ([document_1.txt](#ref-doc1)). The border between voiced and unvoiced frames is identified, and 80 ms of signal is taken to the left and to the right of that border, producing segments of 160 ms ([document_1.txt](#ref-doc1)).

For the CNN branch, short-time Fourier transform (STFT) representations are computed for each segmented transition with 256 frequency bins, using a window length of 16 ms and a step size of 4 ms, forming 41 time frames per transition ([document_1.txt](#ref-doc1)). Each spectrogram is then transformed to the Mel scale using 80 filters, giving a final input of 80 × 41 ([document_1.txt](#ref-doc1)). The summarised pipeline parameters are:

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

The experimental design is explicitly staged. First, baseline and CNN models are trained considering each language individually. Then, the trained CNNs for each language are used as base models in a transfer learning strategy intended to improve accuracy in the other two languages; all speech exercises performed by participants were considered, and the final decision for each speaker was obtained by majority voting across exercises ([document_1.txt](#ref-doc1)).

The monolingual results (Table 3 of the source) are reproduced below.

| Language | Model | Acc (%) | Sen (%) | Spe (%) | MCC |
|---|---|---|---|---|---|
| Spanish | Baseline (SVM) | 73.7 (13.0) | 74.5 (16.7) | 77.1 (16.2) | 0.50 |
| Spanish | CNN | 71.0 (15.9) | 74.0 (25.0) | 68.0 (28.6) | 0.42 |
| German | Baseline (SVM) | 69.3 (9.9) | 71.8 (12.4) | 68.7 (10.0) | 0.39 |
| German | CNN | 63.1 (11.7) | 43.1 (38.0) | 83.1 (17.7) | 0.30 |
| Czech | Baseline (SVM) | 61.0 (12.5) | 64.5 (19.5) | 60.2 (11.9) | 0.27 |
| Czech | CNN | 68.5 (14.1) | 94.0 (13.5) | 42.0 (33.2) | 0.43 |

*Source: ([document_1.txt](#ref-doc1))*

The cross-lingual transfer learning results (Table 4 of the source) are presented next; where the source text reports base and target language labels in a compressed format, the pairings below follow the row structure of the reported table ([document_1.txt](#ref-doc1)).

| Base language (pre-training) | Target language (fine-tuning) | Acc (%) | Sen (%) | Spe (%) | MCC |
|---|---|---|---|---|---|
| German | Spanish | 70.0 (12.5) | 62.0 (19.9) | 78.0 (23.9) | 0.41 |
| German | Czech | 72.0 (13.1) | 67.0 (11.6) | 78.0 (23.9) | 0.46 |
| Spanish | German | 77.3 (11.3) | 86.2 (13.8) | 68.3 (14.3) | 0.57 |
| Spanish | Czech | 76.7 (7.9) | 87.5 (11.0) | 66.0 (15.6) | 0.55 |
| Czech | Spanish | 72.6 (13.9) | 82.0 (14.8) | 62.0 (28.9) | 0.46 |
| Czech | German | 70.7 (14.5) | 80.0 (16.3) | 62.5 (26.3) | 0.38 |

*Source: ([document_1.txt](#ref-doc1))*

Read against the monolingual baselines, the transfer results show that the best German model improves from 69.3% (baseline) and 63.1% (monolingual CNN) to 77.3% when the CNN is initialised with Spanish utterances — an improvement of roughly 8 percentage points over the strongest German-only result, and more than 14 points over the German CNN ([document_1.txt](#ref-doc1)). The Czech target improves from 68.5% (CNN) to 76.7% under the same Spanish base, an increase of just over 8 percentage points ([document_1.txt](#ref-doc1)). These figures correspond exactly to the study's claim that transfer learning improved accuracy "in up to 8%" and, in a separate statement, "over 8%" ([document_1.txt](#ref-doc1)). The study further reports that transfer learning results are more balanced in terms of specificity and sensitivity and have lower variance, and that cross-lingual transfer helped only when the base model was robust enough — which was observed for the Spanish-trained base ([document_1.txt](#ref-doc1)).

## Datasets Referenced in the Related Work but Not Used

The reference list of the source document also includes the Parkinson speech dataset with multiple types of sound recordings collected by Sakar and colleagues and published in the *IEEE Journal of Biomedical and Health Informatics* ([document_1.txt](#ref-doc1)). This corpus is cited in the related-work context, but the extracts do not indicate that it contributes speakers to the present experiments; the analysed data are limited to the Spanish (PC-GITA), German and Czech sets. Separately, the study's own discussion references prior work in which the same three-language data were modelled with a deep-learning articulation approach, reporting accuracies between 70% and 89% depending on language, but below 60% in a language-independent scenario where the CNN was trained on one language and tested on the other two ([document_1.txt](#ref-doc1)). The present study is therefore best understood as an attempt to solve the generalisation failure observed on exactly these datasets.

## Limitations and Analytical Commentary

Three limitations concerning the datasets are worth stating plainly. First, the datasets are not perfectly matched on clinical severity: the Spanish patients have higher average MDS-UPDRS-III scores than the German and Czech patients, which confounds language with disease severity ([document_1.txt](#ref-doc1)). This is almost certainly why the Spanish models — and the Spanish-initialised transfer models — perform best. The reported 8% gain may therefore reflect, in part, the transfer of a model trained on a more severely affected population, rather than the transfer of purely linguistic or acoustic invariances. Second, sample sizes are modest (100–176 speakers per language), and the reported standard deviations are substantial in several conditions (for example, a specificity of 42.0 with a standard deviation of 33.2 for the Czech CNN) ([document_1.txt](#ref-doc1)). Third, the German task inventory is not documented in the available evidence, so the degree of task-level comparability across the three corpora cannot be verified from these sources alone.

These caveats are relevant to how the datasets should be reused. The study itself proposes future work that would address them: more robust base models via hyper-parameter optimisation such as Bayesian optimisation, base models trained on two languages rather than one, evaluation of PD staging based on MDS-UPDRS-III or dysarthria severity, and transfer learning across diseases — for instance training a base model on PD and using it to initialise a classifier for Huntington's disease ([document_1.txt](#ref-doc1)).

## Conclusion

The study draws on three language-specific speech datasets of Parkinson's disease patients and healthy controls: the Spanish PC-GITA corpus (50 PD, 50 HC, Colombian Spanish speakers), German speech recordings (88 PD, 88 HC), and Czech speech recordings (50 PD, 50 HC native Czech speakers performing /pa-ta-ka/ repetition, an 80-word reading task and a monologue) ([document_1.txt](#ref-doc1); [document_2.txt](#ref-doc2)). All three were recorded under noise-controlled conditions, down-sampled to 16 kHz, clinically annotated with the MDS-UPDRS-III, and processed identically into 160 ms voiced/unvoiced transition segments and 80 × 41 Mel spectrograms. The datasets are balanced in class composition but not in disease severity, and this imbalance is the most plausible explanation for both the higher baseline accuracy observed for Spanish and the disproportionate success of the Spanish-initialised transfer models, which raised target-language accuracy by up to roughly 8 percentage points over the strongest monolingual German result ([document_1.txt](#ref-doc1)).

## References

<a id="ref-doc1"></a>document_1.txt. (n.d.). *Source document 1: Convolutional neural networks and a transfer learning strategy to classify Parkinson's disease from speech in three different languages* [Unpublished manuscript extract].

<a id="ref-doc2"></a>document_2.txt. (n.d.). *Source document 2: Third-party research note on convolutional neural networks and a transfer learning strategy to classify Parkinson's disease from speech in three different languages* [Research note].