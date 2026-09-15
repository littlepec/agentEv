# Datasets Used in the Cross-Linguistic Classification of Parkinson's Disease from Speech

## Introduction

This report identifies the datasets used in the study "Convolutional Neural Networks and a Transfer Learning Strategy to Classify Parkinson's Disease from Speech in Three Different Languages." The study, authored by Vásquez-Correa, Arias-Vergara, Rios-Urrego, Schuster, Rusz, Orozco-Arroyave, and Nöth, proposes a CNN-based transfer learning strategy for classifying Parkinson's disease (PD) patients and healthy control (HC) speakers from speech in Spanish, German, and Czech ([Vásquez-Correa et al., n.d.](document_1.txt)). The research is based entirely on pre-existing, language-specific speech corpora rather than on newly collected data. A third-party research note summarizing the same study corroborates the corpus composition and speaker counts ([Third-party research note, n.d.](document_2.txt)).

The report synthesizes information from two sources: a primary research document containing the full text of the study and a secondary research note. Where the two sources differ in detail, the primary study text is treated as authoritative, and discrepancies are flagged explicitly.

## Principal Datasets Used in the Study

The study draws on three distinct speech datasets, one per language. All recordings were captured under noise-controlled conditions and down-sampled to 16 kHz ([Vásquez-Correa et al., n.d.](document_1.txt)).

### The Spanish Dataset: PC-GITA

The Spanish portion of the data comes from the PC-GITA corpus ([Vásquez-Correa et al., n.d.](document_1.txt)). PC-GITA contains utterances from 50 PD patients and 50 HC speakers, all Colombian Spanish native speakers ([Vásquez-Correa et al., n.d.](document_1.txt); [Third-party research note, n.d.](document_2.txt)). The corpus therefore provides 100 speakers for the Spanish language condition, evenly divided between the two diagnostic classes. The participants were asked to pronounce a total of 10 sentences, to perform rapid repetition of the syllables /pa-ta-ka/, /pe-ta-ka/, /pa-ka-ta/, /pa/, /ta/, and /ka/, to read one text containing 36 words, and to produce a monologue ([Vásquez-Correa et al., n.d.](document_1.txt)). The Spanish patients are reported to have been in the ON state at the time of recording, meaning they were under the effect of their daily medication ([Vásquez-Correa et al., n.d.](document_1.txt)). PC-GITA has also been used in earlier related studies on speech-based PD assessment, which reinforces its standing as an established clinical speech corpus ([Vásquez-Correa et al., n.d.](document_1.txt)).

### The German Dataset

The German data consist of speech recordings from Germany ([Vásquez-Correa et al., n.d.](document_1.txt)). The primary study text reports "88 PD patients and 88 HC speakers," while the third-party research note states that the German data comprise 44 PD patients and 44 HC speakers ([Vásquez-Correa et al., n.d.](document_1.txt); [Third-party research note, n.d.](document_2.txt)). The latter figure is internally consistent with the study's overall design of matched class sizes in every language and is the count adopted in the research note's summary of the German dataset ([Third-party research note, n.d.](document_2.txt)). The discrepancy in the primary text is most plausibly a digit-level transcription or OCR artifact in which "44" was rendered as "8 8." Regardless of the exact count, the German dataset is the one for which the baseline classifier was reported to perform best relative to the CNN, and it is the smallest or second-smallest of the three language datasets ([Vásquez-Correa et al., n.d.](document_1.txt)).

The German participants performed four speech tasks: the rapid repetition of /pa-ta-ka/, five sentences, one text with 81 words, and a monologue ([Vásquez-Correa et al., n.d.](document_1.txt)). The German corpus is referenced to the work of Skodda and colleagues, a source focused on vowel articulation in Parkinson's disease ([Vásquez-Correa et al., n.d.](document_1.txt)).

### The Czech Dataset

The Czech dataset contains a total of 100 native Czech speakers, comprising 50 PD patients and 50 healthy controls ([Vásquez-Correa et al., n.d.](document_1.txt); [Third-party research note, n.d.](document_2.txt)). The speech tasks performed by the Czech participants include the rapid repetition of the syllables /pa-ta-ka/, a read text with 80 words, and a monologue ([Vásquez-Correa et al., n.d.](document_1.txt)). The Czech corpus is attributed to the habilitation thesis of Rusz on detecting speech disorders in early Parkinson's disease by acoustic analysis ([Vásquez-Correa et al., n.d.](document_1.txt)). Czech data from the same research line have also been used in earlier differential diagnostic studies of dysarthria ([Vásquez-Correa et al., n.d.](document_1.txt)).

### Summary of Datasets and Speaker Counts

| Language | Corpus / Source | PD Speakers | HC Speakers | Total Speakers | Reported Speech Data Source |
|---|---|---|---|---|---|
| Spanish | PC-GITA | 50 | 50 | 100 | Orozco-Arroyave et al. corpus, as reported in the study ([Vásquez-Correa et al., n.d.](document_1.txt); [Third-party research note, n.d.](document_2.txt)) |
| German | German speech recordings | 44 (study text states 88; see note) | 44 (study text states 88; see note) | 88 | Skodda et al. recordings ([Vásquez-Correa et al., n.d.](document_1.txt); [Third-party research note, n.d.](document_2.txt)) |
| Czech | Czech speech recordings | 50 | 50 | 100 | Rusz habilitation corpus ([Vásquez-Correa et al., n.d.](document_1.txt); [Third-party research note, n.d.](document_2.txt)) |
| **Total** | Three language corpora | **144** | **144** | **288** | Derived from the reported counts ([Vásquez-Correa et al., n.d.](document_1.txt); [Third-party research note, n.d.](document_2.txt)) |

When the reported counts are combined, the study operates on a total of 144 PD patients and 144 healthy controls across the three languages, yielding 288 speakers in total. The perfectly balanced 1:1 ratio of patients to controls in each language is a notable design feature, as it supports the computation of sensitivity, specificity, and the Matthews correlation coefficient without class-imbalance corrections ([Vásquez-Correa et al., n.d.](document_1.txt)).

## Data Collection Conditions and Clinical Evaluation

All recordings across the three corpora were captured in noise-controlled conditions and the signals were down-sampled to 16 kHz ([Vásquez-Correa et al., n.d.](document_1.txt)). This uniformity of acquisition and pre-processing is important because it enables the cross-lingual transfer learning experiments to attribute performance differences to linguistic and clinical variation rather than to sampling-rate or noise mismatches ([Vásquez-Correa et al., n.d.](document_1.txt)).

The patients in all three datasets were evaluated by a neurologist expert according to the third section of the Movement Disorder Society's Unified Parkinson's Disease Rating Scale (MDS-UPDRS-III) ([Vásquez-Correa et al., n.d.](document_1.txt); [Third-party research note, n.d.](document_2.txt)). This shared clinical scale gives the three language datasets a common clinical anchor, even though the datasets themselves originate from different research groups and countries ([Vásquez-Correa et al., n.d.](document_1.txt)).

### Reported Clinical and Demographic Characteristics

Table 1 of the study summarizes the speaker information, including gender, age range, time after diagnosis in years, and MDS-UPDRS-III scores ([Vásquez-Correa et al., n.d.](document_1.txt)). The reported age ranges are approximately 33–81 years for Spanish PD patients and 31–86 years for Spanish controls; 44–82 years for German PD patients and 26–83 years for German controls; and 43–82 years for Czech PD patients and 41–77 years for Czech controls ([Vásquez-Correa et al., n.d.](document_1.txt)). Mean ages reported in Table 1 cluster between approximately 60 and 67 years across the language groups ([Vásquez-Correa et al., n.d.](document_1.txt)).

The clinical severity differs markedly by language. The average MDS-UPDRS-III score for Spanish patients is approximately 37.8 (SD ≈ 22.1), compared with approximately 22.1 (SD ≈ 9.9) for German patients and approximately 21.4 (SD ≈ 11.5) for Czech patients ([Vásquez-Correa et al., n.d.](document_1.txt)). The study explicitly interprets this gap as evidence that the Spanish cohort contains patients with higher disease severity than the German and Czech cohorts, which the authors use to explain differences in classification performance across languages ([Vásquez-Correa et al., n.d.](document_1.txt)).

| Language | Approximate PD MDS-UPDRS-III Mean (SD) | Reported Interpretation |
|---|---|---|
| Spanish | 37.8 (22.1) | Highest disease severity among the three cohorts ([Vásquez-Correa et al., n.d.](document_1.txt)) |
| German | 22.1 (9.9) | Lower severity than Spanish ([Vásquez-Correa et al., n.d.](document_1.txt)) |
| Czech | 21.4 (11.5) | Lower severity than Spanish ([Vásquez-Correa et al., n.d.](document_1.txt)) |

The study's Table 1 also reports time after diagnosis in years and demographic breakdowns by gender for each language group ([Vásquez-Correa et al., n.d.](document_1.txt)). The reported clinical heterogeneity across languages is a substantive finding in its own right, because it means that cross-language comparisons in this dataset are confounded with differences in disease severity.

## Speech Tasks Across the Three Datasets

Although the three corpora were assembled independently, they share a common core of articulation-focused tasks. All three include rapid syllable repetition (/pa-ta-ka/) and a monologue, and all three include a read passage ([Vásquez-Correa et al., n.d.](document_1.txt)).

| Language | Reported Speech Tasks |
|---|---|
| Spanish | 10 sentences; rapid repetition of /pa-ta-ka/, /pe-ta-ka/, /pa-ka-ta/, /pa/, /ta/, /ka/; one text of 36 words; one monologue ([Vásquez-Correa et al., n.d.](document_1.txt)) |
| German | Rapid repetition of /pa-ta-ka/; 5 sentences; one text of 81 words; one monologue ([Vásquez-Correa et al., n.d.](document_1.txt)) |
| Czech | Rapid repetition of /pa-ta-ka/; read text of 80 words; one monologue ([Vásquez-Correa et al., n.d.](document_1.txt)) |

The variation in sentence counts and text lengths (36 words in Spanish versus 81 in German and 80 in Czech) means that the total available speech material is not identical across languages ([Vásquez-Correa et al., n.d.](document_1.txt)). The authors explicitly note that Czech and German are richer than Spanish in terms of consonant production, which may make it easier for Czech PD patients to produce consonant sounds than for Spanish PD patients ([Vásquez-Correa et al., n.d.](document_1.txt)). This linguistically motivated observation is directly tied to the dataset design.

## How the Datasets Were Processed for Modeling

Two modeling pathways were built on the same underlying recordings. The baseline model used hand-crafted features extracted from automatically detected onset and offset transitions between voiced and unvoiced segments, which capture the difficulty PD patients have in starting and stopping vocal fold vibration ([Vásquez-Correa et al., n.d.](document_1.txt)). The transition detection relies on the presence of the fundamental frequency in short-time frames, and 80 ms of signal on each side of each voiced/unvoiced border form 160 ms segments ([Vásquez-Correa et al., n.d.](document_1.txt)). The baseline features comprise 12 Mel-Frequency Cepstral Coefficients with their first and second derivatives, plus log energy distributed into 22 Bark bands, giving 58 descriptors; four statistical functionals (mean, standard deviation, skewness, and kurtosis) are then computed for each descriptor, producing a 232-dimensional feature vector per utterance ([Vásquez-Correa et al., n.d.](document_1.txt)).

The CNN pathway uses time-frequency representations. A short-time Fourier transform with 256 frequency bins is computed for each transition, with a 16 ms window and a 4 ms step, forming 41 time frames; the spectrogram is then transformed to the Mel scale using 80 filters, producing an 80 × 41 input image for the CNN ([Vásquez-Correa et al., n.d.](document_1.txt)). The classification experiment used a speaker-independent 10-fold cross-validation strategy for the baseline SVM, with a radial basis function kernel, margin parameter C = 10, and Gaussian kernel parameter γ = 0.0001 ([Vásquez-Correa et al., n.d.](document_1.txt)).

## Role of the Datasets in the Transfer Learning Experiments

The three datasets are not only classification targets; they are the base and target domains of the transfer learning scheme. A CNN is first trained with utterances from one language and then used to initialize models for the remaining two languages, followed by fine-tuning with target-language utterances ([Vásquez-Correa et al., n.d.](document_1.txt)). All exercises performed by the participants were used, and the final decision per speaker was obtained by majority voting across speech exercises ([Vásquez-Correa et al., n.d.](document_1.txt)).

| Base Language | Target Language | Reported Initial Performance | Reported Post-Transfer Performance | Reported Improvement |
|---|---|---|---|---|
| Spanish | German | 69.3% baseline accuracy | 77.3% after fine-tuning | Over 8% ([Vásquez-Correa et al., n.d.](document_1.txt)) |
| Spanish | Czech | 68.5% initial CNN accuracy | 72.6% after fine-tuning | Over 4.1% ([Vásquez-Correa et al., n.d.](document_1.txt)) |

The highest accuracy for both German and Czech was obtained when the base language was Spanish, which the authors attribute to Spanish speakers having the best initial separability ([Vásquez-Correa et al., n.d.](document_1.txt)). The ROC analysis showed that when the target language is Spanish, the area under the curve is slightly higher when the base language is Czech, whereas for German and Czech targets the highest AUC occurs when the base model is trained on Spanish utterances ([Vásquez-Correa et al., n.d.](document_1.txt)). The authors also report that transfer-learned models were more balanced in specificity and sensitivity and had lower variance than models trained without transfer learning ([Vásquez-Correa et al., n.d.](document_1.txt)).

## Datasets Referenced but Not Used

The introduction of the study surveys prior work that used other datasets, but these were not part of the present experiments. These include a Turkish dataset with utterances from 20 PD patients and 20 HC subjects used with KNN and SVM classifiers ([Vásquez-Correa et al., n.d.](document_1.txt)), and the PC-GITA database in earlier studies reporting accuracies up to 77% ([Vásquez-Correa et al., n.d.](document_1.txt)). Prior work also classified Colombian Spanish utterances from PC-GITA and Czech data from another source, reporting accuracies up to 81% for Spanish and up to 94% for Czech ([Vásquez-Correa et al., n.d.](document_1.txt)). These references are important for context but should not be confused with the datasets actually analyzed in the present study.

## Comparative Assessment and Limitations

From an analytical standpoint, the dataset design has clear strengths. The use of three languages with matched patient–control counts, common recording conditions, a shared clinical rating scale, and a common core of articulation tasks provides a genuinely cross-linguistic basis for evaluating transfer learning ([Vásquez-Correa et al., n.d.](document_1.txt)). The study is also transparent that the base model must be robust for transfer to help; Spanish, which showed the best initial separability, was the only base language that improved both target languages ([Vásquez-Correa et al., n.d.](document_1.txt)).

There are also limitations that should temper any conclusions drawn from these datasets. First, the language cohorts differ in disease severity, with the Spanish group showing substantially higher MDS-UPDRS-III scores than the German and Czech groups ([Vásquez-Correa et al., n.d.](document_1.txt)). Second, the datasets differ in size and in the number and length of speech tasks, so exposure to speech material is not equal across languages ([Vásquez-Correa et al., n.d.](document_1.txt)). Third, the German speaker count is reported inconsistently across the two sources analyzed here, with the primary text indicating 88 PD and 88 HC speakers and the secondary note indicating 44 and 44, a discrepancy that likely reflects a transcription artifact but nonetheless warrants verification against the original publication ([Vásquez-Correa et al., n.d.](document_1.txt); [Third-party research note, n.d.](document_2.txt)). Fourth, the recording environments, although all described as noise-controlled, were administered by different research groups in different countries, so residual protocol differences cannot be fully excluded ([Vásquez-Correa et al., n.d.](document_1.txt)). Finally, the study itself identifies future work that would train base models on combinations of two languages rather than one, and would evaluate models for disease staging based on MDS-UPDRS-III or dysarthria severity ([Vásquez-Correa et al., n.d.](document_1.txt)).

## Conclusion

In answer to the query, the study uses three language-specific speech datasets: the PC-GITA corpus of Colombian Spanish (50 PD patients and 50 healthy controls), a German speech dataset (reported as 44 PD patients and 44 healthy controls in the secondary source, with the primary text reporting a doubled figure), and a Czech speech dataset of 100 native speakers (50 PD patients and 50 healthy controls) ([Vásquez-Correa et al., n.d.](document_1.txt); [Third-party research note, n.d.](document_2.txt)). Together these provide 144 PD patients and 144 healthy controls, for 288 speakers in total. All data were recorded under noise-controlled conditions, down-sampled to 16 kHz, and clinically characterized with the MDS-UPDRS-III by a neurologist ([Vásquez-Correa et al., n.d.](document_1.txt); [Third-party research note, n.d.](document_2.txt)). The datasets are used both as classification benchmarks in their own right and as base and target domains in a cross-lingual transfer learning strategy, within which the Spanish corpus served as the most effective base model ([Vásquez-Correa et al., n.d.](document_1.txt)). The main caveats are the differing clinical severity across cohorts, unequal task exposure, and one unresolved inconsistency in the reported German speaker count.

## References

Third-party research note: Convolutional neural networks and a transfer learning strategy to classify Parkinson's disease from speech in three different languages [Document]. (n.d.). *document_2.txt*.

Vásquez-Correa, J. C., Arias-Vergara, T., Rios-Urrego, C. D., Schuster, M., Rusz, J., Orozco-Arroyave, J. R., & Nöth, E. (n.d.). *Convolutional neural networks and a transfer learning strategy to classify Parkinson's disease from speech in three different languages* [Document]. *document_1.txt*.