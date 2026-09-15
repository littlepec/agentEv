# Datasets Used in the Cross-Lingual Classification of Parkinson's Disease from Speech

## 1. Scope and Framing of the Query

This report addresses the question "What datasets are used?" with respect to the study *Convolutional Neural Networks and a Transfer Learning Strategy to Classify Parkinson's Disease from Speech in Three Different Languages* by Vasquez-Correa and colleagues ([Vasquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)). The answer is not a single dataset but a composite, multi-language data foundation assembled from three independently collected clinical speech corpora: a Colombian Spanish corpus (PC-GITA), a German speech database, and a Czech speech database ([Vasquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)). A supplementary third-party research note summarises the same data foundation and provides its own account of the speaker composition, which is used here to corroborate — and in one instance to question — the primary article ([Third-party research note, n.d.](document_2.txt)).

The report distinguishes three layers of "dataset" that must be understood separately: (a) the three *source corpora* of recorded speech; (b) the *clinical and demographic metadata* attached to those corpora (age, gender, time since diagnosis, MDS-UPDRS-III severity); and (c) the *derived representations* generated from the corpora for machine learning, namely transition segments, hand-crafted feature vectors, and Mel-scale spectrograms ([Vasquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)).

## 2. Overview of the Datasets

Three corpora, each representing a different native language, constitute the complete data basis of the study. All recordings were captured under noise-controlled conditions and the speech signals were down-sampled to 16 kHz ([Vasquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)). All participants across the three datasets were evaluated by an expert neurologist using the third section of the Movement Disorder Society Unified Parkinson's Disease Rating Scale (MDS-UPDRS-III) ([Third-party research note, n.d.](document_2.txt)).

**Table 1. Overview of the three source corpora used in the study.**

| Language | Corpus / provenance | PD speakers | Healthy control speakers | Speech tasks |
|---|---|---|---|---|
| Spanish | PC-GITA corpus | 50 | 50 | 10 sentences; rapid repetition of /pa-ta-ka/, /pe-ta-ka/, /pa-ka-ta/, /pa/, /ta/, /ka/; one text of 36 words; a monologue |
| German | German speech recordings (source cited as Skodda et al.) | 44 (per third-party note) / gender table implies 88 | 44 (per third-party note) / gender table implies 88 | Rapid repetition of /pa-ta-ka/; 5 sentences; one text of 81 words; a monologue |
| Czech | Czech speech recordings (source cited as Rusz, habilitation thesis) | 50 | 50 | Rapid repetition of /pa-ta-ka/; read text of 80 words; a monologue |

Sources: ([Vasquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374); [Third-party research note, n.d.](document_2.txt)).

## 3. The Spanish Dataset: The PC-GITA Corpus

The Spanish portion of the data comes from the PC-GITA corpus, which contains utterances from 50 Parkinson's disease (PD) patients and 50 healthy control (HC) speakers, all Colombian Spanish native speakers ([Vasquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)). The third-party note confirms this composition and explicitly identifies PC-GITA as the corpus that "provides the Spanish portion of the cross-lingual speech data" ([Third-party research note, n.d.](document_2.txt)).

The elicitation protocol for PC-GITA is comparatively rich. Participants were asked to pronounce a total of 10 sentences, to perform rapid repetition of the syllables /pa-ta-ka/, /pe-ta-ka/, /pa-ka-ta/, and the single syllables /pa/, /ta/ and /ka/, to read one text containing 36 words, and to produce a monologue ([Vasquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)). An important clinical detail is that all Spanish patients were recorded in the ON state, meaning under the effect of their daily medication ([Vasquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)). This is a methodological fact with direct consequences: the speech data reflect medicated rather than untreated Parkinsonian speech, which may attenuate some dysarthric markers.

The Spanish dataset also exhibits the highest reported disease severity of the three language groups. Mean MDS-UPDRS-III scores were 37.8 (SD = 22.1) for male patients and 37.6 (SD = 14.1) for female patients, compared with roughly 21–23 for the German and Czech patients ([Vasquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)). Time since diagnosis was also longest in the Spanish group: 12.6 years (SD = 11.6) for males and 8.7 years (SD = 5.9) for females ([Vasquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)). Age ranges spanned 33–81 years for male PD patients and 49–75 years for female PD patients, with mean ages of 61.3 (SD = 11.4) and 60.5 (SD = 11.6) respectively ([Vasquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)).

## 4. The German Dataset

The German data consist of speech recordings whose source is cited in the primary article under reference number [18], a study on vowel articulation in Parkinson's disease published in the *Journal of Voice* ([Vasquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)). The German narrative paragraph in the primary document is partially corrupted in the available text, but the speech tasks are recoverable: participants performed four tasks, namely rapid repetition of /pa-ta-ka/, five sentences, one text with 81 words, and a monologue ([Vasquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)).

**Table 2. German dataset characteristics, including the discrepancy between sources.**

| Attribute | Primary article (Table 1) | Third-party note |
|---|---|---|
| PD speakers | 47 male + 41 female (implies 88) | 44 |
| HC speakers | 44 male + 44 female (implies 88) | 44 |
| Age range (PD) | M: 44–82; F: 42–84 | Not stated |
| Mean age (PD) | M: 66.7 (8.7); F: 63.8 (12.7) | Not stated |
| Time since diagnosis | M: 7.0 (5.5); F: 7.1 (6.2) | Not stated |
| MDS-UPDRS-III | M: 22.1 (9.9); F: 23.3 (12.0) | Not stated |

Sources: ([Vasquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374); [Third-party research note, n.d.](document_2.txt)).

### 4.1 The Sample-Size Discrepancy

The most significant documentation problem in the supplied sources concerns the German sample size. The third-party note states plainly that "the German data consist of speech recordings of 44 PD patients and 44 HC speakers" ([Third-party research note, n.d.](document_2.txt)). The primary article's Table 1, however, reports gender-wise counts of 47 males and 41 females for the German PD group and 44 males and 44 females for the German HC group ([Vasquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)). If those gender counts are group totals, the German sample would be 88 PD and 88 HC, not 44 and 44.

The two figures cannot both be correct. The most economical reading is that the "44 and 44" in the third-party note reflects the gender split of the German healthy control group rather than the group totals, while the true German sample is 88 PD and 88 HC. Because the primary document's German paragraph is truncated and the table is extracted with formatting artefacts, this report treats the precise German sample size as **unresolved** and flags it for verification against the published version of record. Importantly, the discrepancy does not affect the class balance claim: whichever figure is correct, the German PD and HC groups are matched in size, consistent with the Spanish (50/50) and Czech (50/50) corpora ([Vasquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)).

## 5. The Czech Dataset

The Czech data comprise a total of 100 native Czech speakers, of which 50 are PD patients and 50 are healthy controls; the source is cited as a habilitation thesis on detecting speech disorders in early Parkinson's disease ([Vasquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)). The third-party note independently confirms this composition, describing the Czech dataset as "a total of 100 native Czech speakers, comprising 50 PD patients and 50 healthy controls" ([Third-party research note, n.d.](document_2.txt)).

The Czech elicitation protocol included the rapid repetition of the syllables /pa-ta-ka/, a read text with 80 words, and a monologue ([Vasquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)). The gender composition was 30 males and 20 females in each of the PD and HC groups ([Vasquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)). Mean ages were 65.3 (SD = 9.6) for male PD patients and 60.3 (SD = 11.5) for female PD patients, with male HC at 60.1 (SD = 8.7) and female HC at 63.5 (SD = 11.1) ([Vasquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)). Disease duration was relatively short — 6.7 years (SD = 4.5) for men and 6.8 years (SD = 5.2) for women — and MDS-UPDRS-III severity was the lowest of the three languages at 21.4 (SD = 11.5) for men and 18.1 (SD = 9.7) for women ([Vasquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)).

## 6. Comparative Clinical Profile of the Three Datasets

**Table 3. Clinical and demographic profile of the PD groups across the three datasets.**

| Language | Severity (MDS-UPDRS-III, mean ± SD) | Time since diagnosis, years (mean ± SD) | Mean age, years (mean ± SD) |
|---|---|---|---|
| Spanish (PD, male) | 37.8 (22.1) | 12.6 (11.6) | 61.3 (11.4) |
| Spanish (PD, female) | 37.6 (14.1) | 8.7 (5.9) | 60.5 (11.6) |
| German (PD, male) | 22.1 (9.9) | 7.0 (5.5) | 66.7 (8.7) |
| German (PD, female) | 23.3 (12.0) | 7.1 (6.2) | 63.8 (12.7) |
| Czech (PD, male) | 21.4 (11.5) | 6.7 (4.5) | 65.3 (9.6) |
| Czech (PD, female) | 18.1 (9.7) | 6.8 (5.2) | 60.3 (11.5) |

Source: ([Vasquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)).

The table shows that the three corpora are not clinically homogeneous. Spanish patients present substantially higher disease severity and longer disease duration than the German and Czech patients, a difference the authors explicitly use to explain the divergent classification performance across languages ([Vasquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)). This is a material property of the dataset base: any cross-lingual comparison is simultaneously a cross-severity comparison.

## 7. Derived Data Products Generated from the Corpora

The corpora are not used as raw audio in the modelling pipeline. Speech signals were first analysed through automatic detection of onset and offset transitions between voiced and unvoiced frames, which operationalise the difficulty PD patients have in starting and stopping vocal fold vibration; 80 ms of signal were taken to the left and right of each detected border to form 160 ms segments ([Vasquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)).

From these segments, two derived datasets were created. The first is a hand-crafted feature set for the baseline: 12 Mel-Frequency Cepstral Coefficients with first and second derivatives plus log energy distributed across 22 Bark bands, giving 58 descriptors, which after four statistical functionals (mean, standard deviation, skewness, kurtosis) yield a 232-dimensional vector per utterance ([Vasquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)). The second is a time-frequency representation: a short-time Fourier transform with 256 frequency bins, a 16 ms window and a 4 ms step, producing 41 time frames per transition, subsequently mapped onto the Mel scale with 80 filters to yield an 80 × 41 spectrogram used as CNN input ([Vasquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)).

## 8. How the Three Datasets Are Partitioned Across Experiments

The corpora are used in two experimental configurations. First, baseline and CNN models are trained within each language individually; the SVM baseline was evaluated with a speaker-independent 10-fold cross-validation using a radial basis kernel with C = 10 and a Gaussian kernel parameter of 0.0001 ([Vasquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)). Second, a CNN pre-trained on one language is used to initialise models for the other two languages in a transfer learning scheme ([Vasquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)). All speech exercises performed by a participant were used, and the final speaker-level decision was obtained by majority voting across exercises ([Vasquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)).

**Table 4. Transfer learning results across the three datasets.**

| Base language | Target language | Accuracy (%) | Sensitivity (%) | Specificity (%) | MCC |
|---|---|---|---|---|---|
| German | Spanish | 70.0 (12.5) | 67.0 (11.6) | 78.0 (23.9) | 0.41 |
| Czech | Spanish | 72.0 (13.1) | 62.0 (19.9) | 78.0 (23.9) | 0.46 |
| Spanish | German | 77.3 (11.3) | 86.2 (13.8) | 66.0 (15.6) | 0.57 |
| Czech | German | 76.7 (7.9) | 87.5 (11.0) | 68.3 (14.3) | 0.55 |
| Spanish | Czech | 72.6 (13.9) | 80.0 (16.3) | 62.5 (26.3) | 0.46 |
| German | Czech | 70.7 (14.5) | 82.0 (14.8) | 62.0 (28.9) | 0.38 |

Source: ([Vasquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)).

The Spanish corpus functions as the strongest base dataset: fine-tuning from Spanish improved German accuracy by more than 8% relative to the baseline (from 69.3% to 77.3%) and Czech accuracy by about 4.1% (from 68.5% to 72.6%) ([Vasquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)). This is consistent with the observation that Spanish patients display the highest MDS-UPDRS-III severity and therefore the most separable pathological speech patterns ([Vasquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)). Area-under-the-ROC-curve values reinforce the pattern: the highest AUCs were 0.838 for Czech-to-Spanish, 0.823 for Spanish-to-German, and 0.831 for Spanish-to-Czech, compared with single-language AUCs of 0.824 (Spanish), 0.684 (German) and 0.764 (Czech) ([Vasquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)).

## 9. Reliability, Gaps, and Limitations of the Dataset Base

Several caveats should govern any reuse of these datasets. Firstly, each language is represented by exactly one corpus, so language and corpus are perfectly confounded; observed cross-lingual differences cannot be attributed to language alone ([Vasquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)). Secondly, the corpora differ in disease severity and duration, with Spanish patients markedly more severe and longer diagnosed than German and Czech patients ([Vasquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)). Thirdly, the Spanish patients were recorded in the ON state, meaning under daily medication, whereas no equivalent statement is provided for the German and Czech groups ([Vasquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)). Fourthly, the sample sizes are modest — of the order of 50 to 100 speakers per language — which limits statistical power and the generalisation of the reported accuracies ([Vasquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)). Fifthly, the documentation contains internal inconsistencies: the clinical scale is introduced as MDS-UPDRS-II in one passage and as the third section (MDS-UPDRS-III) elsewhere and in the tables ([Vasquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)), and the German sample size differs between the primary article and the third-party note ([Third-party research note, n.d.](document_2.txt)).

On the positive side, the corpora are well matched in one crucial respect: every language contains an equal number of PD patients and healthy controls, which supports balanced sensitivity–specificity analysis, and the collection conditions were standardised through noise-controlled recording and 16 kHz down-sampling ([Vasquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)).

## 10. Conclusion

The study does not use a single dataset. It uses three language-specific clinical speech corpora — the PC-GITA corpus of Colombian Spanish (50 PD and 50 HC speakers), a German speech database (reported as 44 PD and 44 HC in the third-party note, though the primary article's gender table suggests 88 and 88), and a Czech database of 100 native speakers (50 PD and 50 HC) — all collected under noise-controlled conditions, down-sampled to 16 kHz, and clinically annotated with the MDS-UPDRS-III by an expert neurologist ([Vasquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374); [Third-party research note, n.d.](document_2.txt)). These corpora are further transformed into two derived datasets: a 232-dimensional hand-crafted feature representation per utterance for the SVM baseline, and 80 × 41 Mel-scale spectrograms of 160 ms voiced–unvoiced transitions for the CNN ([Vasquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)). The Spanish corpus, being the most clinically severe and the most separable, serves as the most effective base dataset for the cross-lingual transfer learning strategy, while the German and Czech corpora function primarily as transfer targets ([Vasquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)).

## References

Vasquez-Correa, J. C., Arias-Vergara, T., Rios-Urrego, C. D., Schuster, M., Rusz, J., Orozco-Arroyave, J. R., & Nöth, E. (2020). *Convolutional neural networks and a transfer learning strategy to classify Parkinson's disease from speech in three different languages* (document_1.txt) [Preprint]. arXiv. https://arxiv.org/abs/2002.04374

Third-party research note: Convolutional neural networks and a transfer learning strategy to classify Parkinson's disease from speech in three different languages (document_2.txt). (n.d.).