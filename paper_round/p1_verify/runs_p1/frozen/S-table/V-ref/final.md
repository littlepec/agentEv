# Datasets Used in the Cross-Lingual Parkinson's Disease Speech Classification Study

## 1. Purpose and Scope of the Evidence Base

This report catalogues and describes the datasets employed in a study that applies convolutional neural networks (CNNs) and a cross-lingual transfer learning strategy to the automatic classification of Parkinson's disease (PD) from speech ([Arias-Vergara et al., 2019](document_1.txt)). The datasets at the centre of the study are three parallel speech corpora recorded in three different languages: Spanish, German, and Czech ([Arias-Vergara et al., 2019](document_1.txt); [Third-party research note, n.d.](document_2.txt)). The study's core research question concerns whether a CNN pre-trained on utterances from one language can be fine-tuned to improve classification accuracy in another language, and the choice of datasets is therefore not incidental but constitutive of the experimental design: without at least two parallel, clinically annotated, language-specific corpora, the transfer learning question could not be posed at all ([Arias-Vergara et al., 2019](document_1.txt)).

Two source documents inform this report. The first is the study text itself, including its data description, tables of speaker demographics, baseline classification results, and cross-lingual transfer results ([Arias-Vergara et al., 2019](document_1.txt)). The second is a third-party research note that summarises the study's dataset composition and identifies the named corpora involved ([Third-party research note, n.d.](document_2.txt)). Where the two sources diverge, this report flags the discrepancy rather than resolving it silently.

## 2. The Three Primary Speech Corpora

### 2.1 Spanish Data: The PC-GITA Corpus

The Spanish portion of the data is drawn from the **PC-GITA corpus** ([Arias-Vergara et al., 2019](document_1.txt); [Third-party research note, n.d.](document_2.txt)). PC-GITA contains utterances from 50 PD patients and 50 healthy control (HC) speakers, all native speakers of Colombian Spanish ([Arias-Vergara et al., 2019](document_1.txt)). The third-party note confirms this composition and identifies PC-GITA as the source that "provides the Spanish portion of the cross-lingual speech data" ([Third-party research note, n.d.](document_2.txt)). The corpus is attributed to Orozco-Arroyave et al. (2014), cited as reference [6] in the study's reference list, and is also referenced in earlier related work where a phonation analysis based on time-frequency representations and classifiers including Gaussian mixture models and support vector machines reported accuracies of up to 77% on PC-GITA utterances ([Arias-Vergara et al., 2019](document_1.txt)).

A notable protocol detail is that all Spanish PD patients were recorded **in the ON state**, that is, under the effect of their daily medication ([Arias-Vergara et al., 2019](document_1.txt)). This is a substantive data characteristic that affects the interpretability of the speech signal as a marker of disease.

### 2.2 German Data: German-Language Speech Recordings

The German data are described only as speech recordings of German PD patients and healthy controls; the provided material does not name the corpus ([Arias-Vergara et al., 2019](document_1.txt)). The third-party note states that the German data consist of speech recordings of 44 PD patients and 44 HC speakers ([Third-party research note, n.d.](document_2.txt)). [document_1.txt states: 88] However, the primary source's demographic table indicates a larger German cohort: 47 male PD and 41 female PD speakers (88 PD total) alongside 44 male HC and 44 female HC speakers (88 HC total) ([Arias-Vergara et al., 2019](document_1.txt)). A German-language corpus of 88 PD and 88 HC speakers is consistent with the earlier study by Grósz, Busa-Fekete, Gosztolya, and Tóth, cited as reference [11] in the reviewed work ([Arias-Vergara et al., 2019](document_1.txt)). The most defensible reading is that the German cohort comprises roughly 88 PD and 88 HC speakers ([Arias-Vergara et al., 2019](document_1.txt)), with the "44/44" figure in the third-party note plausibly describing the male speakers only; the discrepancy is nevertheless recorded here as a data-provenance uncertainty.

### 2.3 Czech Data: Czech-Language Speech Recordings

The Czech data comprise a total of 100 native Czech speakers, of whom 50 have PD and 50 are healthy controls ([Arias-Vergara et al., 2019](document_1.txt); [Third-party research note, n.d.](document_2.txt)). The demographic table disaggregates this as 30 male PD, 20 female PD, 30 male HC, and 20 female HC speakers ([Arias-Vergara et al., 2019](document_1.txt)). The Czech recordings are cited to reference [19] in the study's bibliography, though the corresponding citation details are not reproduced in the provided material ([Arias-Vergara et al., 2019](document_1.txt)). The third-party note describes these as "Czech speech recordings" supplying the third language of the cross-lingual dataset base ([Third-party research note, n.d.](document_2.txt)).

### 2.4 Consolidated Cohort Table

The table below consolidates the speaker composition and clinical metadata reported for the three corpora ([Arias-Vergara et al., 2019](document_1.txt)). Values are reported as mean (standard deviation) unless otherwise indicated.

| Attribute | Spanish (PC-GITA) | German | Czech |
|---|---|---|---|
| PD / HC speakers | 50 / 50 | 88 / 88 (per demographic table) | 50 / 50 |
| PD by sex (M / F) | 25 / 25 | 47 / 41 | 30 / 20 |
| HC by sex (M / F) | 25 / 25 | 44 / 44 | 30 / 20 |
| Age, PD male (years) | 61.3 (11.4) | 66.7 (8.7) | 65.3 (9.6) |
| Age, PD female (years) | 60.7 (7.3) | 66.2 (9.7) | 60.1 (8.7) |
| Age, HC male (years) | 60.5 (11.6) | 63.8 (12.7) | 60.3 (11.5) |
| Age, HC female (years) | 61.4 (7.0) | 62.6 (15.2) | 63.5 (11.1) |
| Time since diagnosis, PD male (years) | 8.7 (5.9) | 7.0 (5.5) | 6.7 (4.5) |
| Time since diagnosis, PD female (years) | 12.6 (11.6) | 7.1 (6.2) | 6.8 (5.2) |
| MDS-UPDRS-III, PD male | 37.8 (22.1) | 22.1 (9.9) | 21.4 (11.5) |
| MDS-UPDRS-III, PD female | 37.6 (14.1) | 23.3 (12.0) | 18.1 (9.7) |

A striking feature of this table is the **heterogeneity of disease severity across languages**. Spanish PD patients present substantially higher MDS-UPDRS-III scores (approximately 37–38 on average) than German (approximately 22–23) or Czech (approximately 18–21) patients ([Arias-Vergara et al., 2019](document_1.txt)). The study explicitly attributes the cross-language performance differences to this factor, noting that "there are patients with higher disease severity in the Spanish data compared to German and Czech patients" ([Arias-Vergara et al., 2019](document_1.txt)).

## 3. Recording Conditions, Clinical Assessment, and Speech Tasks

### 3.1 Acquisition Conditions

All recordings across the three datasets were captured under **noise-controlled conditions**, and the speech signals were **down-sampled to 16 kHz** ([Arias-Vergara et al., 2019](document_1.txt)). These two constraints establish the acoustic comparability of the corpora at the signal level and are prerequisites for the cross-corpus transfer learning design.

### 3.2 Clinical Annotation

In all three datasets, patients were evaluated by a **neurologist expert** according to the third section of the Movement Disorder Society–sponsored revision of the Unified Parkinson's Disease Rating Scale (MDS-UPDRS-III) ([Arias-Vergara et al., 2019](document_1.txt); [Third-party research note, n.d.](document_2.txt)). This provides a common, clinician-administered severity metric across languages and is the basis for the severity-based explanation of cross-lingual performance differences.

### 3.3 Speech Tasks

The speech tasks differ across corpora, which is an important consideration for anyone reusing these datasets:

| Task type | Spanish (PC-GITA) | German | Czech |
|---|---|---|---|
| Sentences | 10 sentences | Not reported | Not reported |
| Diadochokinetic rapid repetition | /pa-ta-ka/, /pe-ta-ka/, /pa-ka-ta/ | Not reported | /pa-ta-ka/ |
| Isolated syllables | /pa/, /ta/, /ka/ | Not reported | Not reported |
| Read text | 36-word text | Not reported | 80-word text |
| Monologue | Yes | Not reported | Yes |

Source: ([Arias-Vergara et al., 2019](document_1.txt)). "Not reported" indicates that the provided material does not specify the task set for that corpus. All speech exercises performed by participants were considered in the classification strategy, and a final decision per speaker was obtained through **majority voting across the different speech exercises** ([Arias-Vergara et al., 2019](document_1.txt)).

## 4. Derived Data Structures Generated from the Corpora

The raw recordings were not fed directly to the classifiers. Instead, the study generated derived representations:

- **Transition segmentation.** Onset and offset transitions were detected automatically based on the presence of the fundamental frequency of speech in short-time frames. The border between voiced and unvoiced frames was identified and 80 ms of signal was taken to the left and right, producing segments of **160 ms** in length ([Arias-Vergara et al., 2019](document_1.txt)).
- **Time-frequency representations.** Short-time Fourier transform (STFT) spectrograms with **256 frequency bins** were computed for each segmented transition, using a window length of **16 ms** and a step size of **4 ms**, yielding **41 time frames** per transition. The spectrogram was then Mel-scaled using **80 filters**, producing an input tensor of size **80 × 41** for CNN training ([Arias-Vergara et al., 2019](document_1.txt)).
- **Hand-crafted feature baseline.** A parallel baseline model used hand-crafted features classified with a support vector machine, providing a non-deep-learning comparison point against the CNN ([Arias-Vergara et al., 2019](document_1.txt)).

Thus, the effective unit of analysis is not the speaker or the recording, but the **segmented transition**, with speaker-level decisions aggregated by majority voting ([Arias-Vergara et al., 2019](document_1.txt)).

## 5. How the Datasets Were Partitioned and Used Experimentally

The experiments proceeded in two stages ([Arias-Vergara et al., 2019](document_1.txt)). First, baseline and CNN models were trained **within each language individually**. Second, each trained CNN was used as a **base model** to initialize models for the other two languages, implementing transfer learning among languages ([Arias-Vergara et al., 2019](document_1.txt)).

### 5.1 Within-Language Results

| Language | Baseline Acc % | Baseline Sen % | Baseline Spe % | Baseline MCC | CNN Acc % | CNN Sen % | CNN Spe % | CNN MCC |
|---|---|---|---|---|---|---|---|---|
| Spanish | 73.7 (13.0) | 74.5 (16.7) | 77.1 (16.2) | 0.50 | 71.0 (15.9) | 74.0 (25.0) | 68.0 (28.6) | 0.42 |
| German | 69.3 (9.9) | 71.8 (12.4) | 68.7 (10.0) | 0.39 | 63.1 (11.7) | 43.1 (38.0) | 83.1 (17.7) | 0.30 |
| Czech | 61.0 (12.5) | 64.5 (19.5) | 60.2 (11.9) | 0.27 | 68.5 (14.1) | 94.0 (13.5) | 42.0 (33.2) | 0.43 |

Source: ([Arias-Vergara et al., 2019](document_1.txt)). Acc = accuracy; Sen = sensitivity; Spe = specificity; MCC = Matthews correlation coefficient.

These results show that the baseline outperformed the CNN for German, whereas the CNN outperformed the baseline for Czech, and the two were closely matched for Spanish ([Arias-Vergara et al., 2019](document_1.txt)). For all three languages, the within-language results were **unbalanced towards one of the two classes**, as evidenced by divergent sensitivity and specificity values ([Arias-Vergara et al., 2019](document_1.txt)).

### 5.2 Cross-Lingual Transfer Results

| Base language | Target language | Acc % | Sen % | Spe % | MCC |
|---|---|---|---|---|---|
| German | Spanish | 70.0 (12.5) | 62.0 (19.9) | 78.0 (23.9) | 0.41 |
| German | Czech | 72.0 (13.1) | 67.0 (11.6) | 78.0 (23.9) | 0.46 |
| Spanish | German | 77.3 (11.3) | 86.2 (13.8) | 68.3 (14.3) | 0.57 |
| Spanish | Czech | 76.7 (7.9) | 87.5 (11.0) | 66.0 (15.6) | 0.55 |
| Label partially obscured in source extraction | — | 72.6 (13.9) | 82.0 (14.8) | 62.0 (28.9) | 0.46 |
| Label partially obscured in source extraction | — | 70.7 (14.5) | 80.0 (16.3) | 62.5 (26.3) | 0.38 |

Source: ([Arias-Vergara et al., 2019](document_1.txt)). The final two rows are reported in the source but their base/target labels are not cleanly recoverable from the available text.

The headline finding is that transfer learning improved accuracy **by up to 8%** when a base model trained on Spanish utterances was used to fine-tune a model for German utterances ([Arias-Vergara et al., 2019](document_1.txt)). The transferred models were also **more balanced in specificity and sensitivity** and exhibited **lower standard deviation**, which the authors interpret as improved generalization ([Arias-Vergara et al., 2019](document_1.txt)). Critically, the benefit materialised only when the base model was "robust enough," which was observed specifically for Spanish-initialised models ([Arias-Vergara et al., 2019](document_1.txt)).

## 6. Assessment of Dataset Strengths, Gaps, and Limitations

### 6.1 Strengths

The dataset design has three clear strengths. First, **parallelism**: the same clinical endpoint (MDS-UPDRS-III) and the same acquisition standard (noise-controlled, 16 kHz) were applied across all three languages, enabling legitimate cross-lingual comparison ([Arias-Vergara et al., 2019](document_1.txt)). Second, **balanced case-control sampling** within each language, with equal or near-equal PD and HC counts in Spanish (50/50) and Czech (50/50) ([Arias-Vergara et al., 2019](document_1.txt)). Third, **multi-task speech protocols**, including diadochokinetic syllable repetition, read text, and monologue, which permit analysis of different articulatory and prosodic phenomena ([Arias-Vergara et al., 2019](document_1.txt)).

### 6.2 Limitations and Open Questions

- **Composition discrepancy for the German data.** The third-party note reports 44 PD and 44 HC speakers, while the primary demographic table implies 88 PD and 88 HC speakers ([Third-party research note, n.d.](document_2.txt); [Arias-Vergara et al., 2019](document_1.txt)). This must be resolved against the original corpus documentation before the German cohort size is cited.
- **Medication state confounding.** Spanish patients were recorded in the ON state, and the provided material does not state the medication state for German or Czech participants ([Arias-Vergara et al., 2019](document_1.txt)). Cross-corpus comparisons of speech markers are therefore confounded by an uncontrolled variable.
- **Severity imbalance across corpora.** Mean MDS-UPDRS-III scores diverge widely (roughly 38 for Spanish versus 18–23 for German and Czech), so cross-lingual transfer results confound language with disease severity ([Arias-Vergara et al., 2019](document_1.txt)).
- **Incomplete task harmonisation.** Only the Czech and Spanish corpora are documented as sharing the /pa-ta-ka/ diadochokinetic task; the German task set is not described in the provided material ([Arias-Vergara et al., 2019](document_1.txt)). Text-reading materials also differ in length (36 words in Spanish versus 80 words in Czech).
- **Small samples.** Cohorts of 50–100 speakers per language, with speaker-level decisions aggregated from a modest number of exercises, constrain statistical power and increase variance, as reflected in the large standard deviations reported for some conditions (e.g., CNN sensitivity of 94.0% with 13.5 SD in Czech) ([Arias-Vergara et al., 2019](document_1.txt)).
- **Undisclosed access conditions.** The provided material contains no information on data licencing, availability, or anonymisation procedures for any of the three corpora.
- **Corpora cited but not used.** The reference list includes other Parkinsonian speech corpora, such as the Turkish dataset of Sakar et al. and Czech articulation studies by Rusz and colleagues ([Arias-Vergara et al., 2019](document_1.txt)). These are cited as related literature; the provided material does not indicate that they contributed data to the present experiments, and they should not be conflated with the three corpora described above.

## 7. Conclusion

The study rests on **three language-specific speech corpora**: the Spanish **PC-GITA** corpus (50 PD, 50 HC Colombian Spanish speakers), a German-language corpus of PD patients and healthy controls, and a Czech-language corpus of 100 speakers (50 PD, 50 HC) ([Arias-Vergara et al., 2019](document_1.txt); [Third-party research note, n.d.](document_2.txt)). All recordings were noise-controlled and down-sampled to 16 kHz, and all patients were clinically rated with MDS-UPDRS-III ([Arias-Vergara et al., 2019](document_1.txt)). The datasets were transformed into 160 ms voiced–unvoiced transition segments and represented as 80 × 41 Mel spectrograms for CNN training, with a hand-crafted feature/SVM pipeline serving as a baseline ([Arias-Vergara et al., 2019](document_1.txt)). Transfer learning between these corpora improved accuracy by up to 8% and produced more balanced, lower-variance models, but only when the base model was sufficiently robust—an outcome observed for Spanish-initialised models ([Arias-Vergara et al., 2019](document_1.txt)). The principal constraints on reuse are the unresolved German cohort size, the ON-state recording of Spanish patients, the severity imbalance across languages, and the uneven speech-task protocols across corpora ([Arias-Vergara et al., 2019](document_1.txt); [Third-party research note, n.d.](document_2.txt)).

## References

Arias-Vergara, T., et al. (2019). *Convolutional neural networks and a transfer learning strategy to classify Parkinson's disease from speech in three different languages* [Source document]. document_1.txt

Third-party research note: *Convolutional neural networks and a transfer learning strategy to classify Parkinson's disease from speech in three different languages* [Source document]. (n.d.). document_2.txt