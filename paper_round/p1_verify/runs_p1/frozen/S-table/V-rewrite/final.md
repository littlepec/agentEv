# Datasets Used in the Cross-Lingual Parkinson's Disease Speech Classification Study

## 1. Purpose and Scope of the Evidence Base

This report catalogues the datasets employed in a study applying convolutional neural networks (CNNs) and a cross-lingual transfer learning strategy to classify Parkinson's disease (PD) from speech (document_1.txt). The datasets are three parallel speech corpora in Spanish, German, and Czech (document_1.txt; document_2.txt). The choice of datasets is constitutive of the experimental design: without at least two parallel, clinically annotated, language-specific corpora, the transfer learning question could not be posed (document_1.txt).

Two source documents inform this report: the study text itself (document_1.txt) and a third-party research note summarising the study's dataset composition (document_2.txt). Where the two diverge, this report flags the discrepancy.

## 2. The Three Primary Speech Corpora

### 2.1 Spanish Data: The PC-GITA Corpus

The Spanish data are drawn from the **PC-GITA corpus** (document_1.txt; document_2.txt). PC-GITA contains utterances from 50 PD patients and 50 healthy control (HC) speakers, all native speakers of Colombian Spanish (document_1.txt). The third-party note confirms this composition and identifies PC-GITA as providing the Spanish portion of the cross-lingual speech data (document_2.txt). The corpus is attributed to Orozco-Arroyave et al. (2014), reference [6] in the study (document_1.txt), and was also used in earlier related work reporting accuracies of up to 77% (document_1.txt).

All Spanish PD patients were recorded **in the ON state**, under the effect of their daily medication (document_1.txt).

### 2.2 German Data: German-Language Speech Recordings

The German data are described only as speech recordings of German PD patients and healthy controls; the provided material does not name the corpus (document_1.txt). The third-party note states the German data consist of 44 PD and 44 HC speakers (document_2.txt). However, the primary source's demographic table indicates 47 male PD and 41 female PD speakers (88 PD total) alongside 44 male HC and 44 female HC speakers (88 HC total) (document_1.txt). The primary source states that speech recordings of 88 PD patients and 88 HC speakers from Germany are considered (document_1.txt). The "44/44" figure in the third-party note is not verified against the primary source; the discrepancy is recorded as a data-provenance uncertainty.

### 2.3 Czech Data: Czech-Language Speech Recordings

The Czech data comprise 100 native Czech speakers, 50 with PD and 50 healthy controls (document_1.txt; document_2.txt). The demographic table disaggregates this as 30 male PD, 20 female PD, 30 male HC, and 20 female HC speakers (document_1.txt). The Czech recordings are cited to reference [19] (document_1.txt). The third-party note describes these as "Czech speech recordings" supplying the third language (document_2.txt).

### 2.4 Consolidated Cohort Table

Values are mean (standard deviation) unless indicated (document_1.txt).

| Attribute | Spanish (PC-GITA) | German | Czech |
|---|---|---|---|
| PD / HC speakers | 50 / 50 | 88 / 88 | 50 / 50 |
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

Spanish PD patients present substantially higher MDS-UPDRS-III scores than German or Czech patients (document_1.txt). The study attributes cross-language performance differences to this factor (document_1.txt).

## 3. Recording Conditions, Clinical Assessment, and Speech Tasks

### 3.1 Acquisition Conditions

All recordings were captured under **noise-controlled conditions**, and signals were **down-sampled to 16 kHz** (document_1.txt).

### 3.2 Clinical Annotation

In all three datasets, patients were evaluated by a **neurologist expert** according to the third section of the MDS-UPDRS-III (document_1.txt; document_2.txt).

### 3.3 Speech Tasks

| Task type | Spanish (PC-GITA) | German | Czech |
|---|---|---|---|
| Sentences | 10 sentences | 5 sentences | Not reported |
| Diadochokinetic rapid repetition | /pa-ta-ka/, /pe-ta-ka/, /pa-ka-ta/ | /pa-ta-ka/ | /pa-ta-ka/ |
| Isolated syllables | /pa/, /ta/, /ka/ | Not reported | Not reported |
| Read text | 36-word text | 81-word text | 80-word text |
| Monologue | Yes | Yes | Yes |

Source: (document_1.txt). "Not reported" indicates the provided material does not specify that task. All speech exercises were considered in the classification strategy, with a final decision per speaker obtained through **majority voting** (document_1.txt).

## 4. Derived Data Structures Generated from the Corpora

- **Transition segmentation.** Onset and offset transitions were detected automatically based on the presence of the fundamental frequency in short-time frames. 80 ms of signal was taken to the left and right, producing segments of **160 ms** (document_1.txt).
- **Time-frequency representations.** STFT spectrograms with **256 frequency bins** were computed per transition, using a window length of **16 ms** and a step size of **4 ms**, yielding **41 time frames**. The spectrogram was Mel-scaled using **80 filters**, producing an input tensor of size **80 × 41** (document_1.txt).
- **Hand-crafted feature baseline.** A parallel baseline used hand-crafted features classified with an SVM (document_1.txt).

The effective unit of analysis is the **segmented transition**, with speaker-level decisions aggregated by majority voting (document_1.txt).

## 5. How the Datasets Were Partitioned and Used Experimentally

Experiments proceeded in two stages: baseline and CNN models trained **within each language individually**, then each trained CNN used as a **base model** to initialize models for the other two languages (document_1.txt).

### 5.1 Within-Language Results

| Language | Baseline Acc % | Baseline Sen % | Baseline Spe % | Baseline MCC | CNN Acc % | CNN Sen % | CNN Spe % | CNN MCC |
|---|---|---|---|---|---|---|---|---|
| Spanish | 73.7 (13.0) | 74.5 (16.7) | 77.1 (16.2) | 0.50 | 71.0 (15.9) | 74.0 (25.0) | 68.0 (28.6) | 0.42 |
| German | 69.3 (9.9) | 71.8 (12.4) | 68.7 (10.0) | 0.39 | 63.1 (11.7) | 43.1 (38.0) | 83.1 (17.7) | 0.30 |
| Czech | 61.0 (12.5) | 64.5 (19.5) | 60.2 (11.9) | 0.27 | 68.5 (14.1) | 94.0 (13.5) | 42.0 (33.2) | 0.43 |

Source: (document_1.txt). The baseline outperformed the CNN for German; the CNN outperformed the baseline for Czech; the two were closely matched for Spanish (document_1.txt). All within-language results were **unbalanced towards one class** (document_1.txt).

### 5.2 Cross-Lingual Transfer Results

| Base language | Target language | Acc % | Sen % | Spe % | MCC |
|---|---|---|---|---|---|
| German | Spanish | 70.0 (12.5) | 62.0 (19.9) | 78.0 (23.9) | 0.41 |
| German | Czech | 72.0 (13.1) | 67.0 (11.6) | 78.0 (23.9) | 0.46 |
| Spanish | German | 77.3 (11.3) | 86.2 (13.8) | 68.3 (14.3) | 0.57 |
| Spanish | Czech | 76.7 (7.9) | 87.5 (11.0) | 66.0 (15.6) | 0.55 |
| Spanish | Czech | 72.6 (13.9) | 82.0 (14.8) | 62.0 (28.9) | 0.46 |
| German | Czech | 70.7 (14.5) | 80.0 (16.3) | 62.5 (26.3) | 0.38 |

Source: (document_1.txt). The final two rows correspond to base language Spanish/target Czech and base language German/target Czech respectively, per the primary source's Table 4 (document_1.txt).

Transfer learning improved accuracy **by up to 8%** when a base model trained on Spanish utterances was used to fine-tune a model for German utterances (document_1.txt). Transferred models were **more balanced in specificity and sensitivity** and exhibited **lower standard deviation** (document_1.txt). The benefit materialised only when the base model was "robust enough," observed specifically for Spanish-initialised models (document_1.txt).

## 6. Assessment of Dataset Strengths, Gaps, and Limitations

### 6.1 Strengths

**Parallelism**: the same clinical endpoint (MDS-UPDRS-III) and acquisition standard (noise-controlled, 16 kHz) were applied across all three languages (document_1.txt). **Balanced case-control sampling** within each language (document_1.txt). **Multi-task speech protocols**, including diadochokinetic syllable repetition, read text, and monologue (document_1.txt).

### 6.2 Limitations and Open Questions

- **Composition discrepancy for the German data.** The third-party note reports 44 PD and 44 HC speakers, while the primary source states 88 PD and 88 HC speakers (document_2.txt; document_1.txt). This must be resolved against the original corpus documentation.
- **Medication state confounding.** Spanish patients were recorded in the ON state; the provided material does not state the medication state for German or Czech participants (document_1.txt).
- **Severity imbalance across corpora.** Mean MDS-UPDRS-III scores diverge widely (roughly 38 for Spanish versus 18–23 for German and Czech) (document_1.txt).
- **Incomplete task harmonisation.** The German task set is described in the primary source (rapid repetition of /pa-ta-ka/, 5 sentences, 81-word text, monologue), but the Czech sentence task is not reported (document_1.txt). Text-reading materials differ in length (36 words Spanish, 81 words German, 80 words Czech).
- **Small samples.** Cohorts of 50–100 speakers per language constrain statistical power (document_1.txt).
- **Undisclosed access conditions.** The provided material contains no information on data licencing, availability, or anonymisation (document_1.txt).
- **Corpora cited but not used.** The reference list includes other Parkinsonian speech corpora, such as the Turkish dataset of Sakar et al. and Czech articulation studies by Rusz and colleagues (document_1.txt). These are cited as related literature and should not be conflated with the three corpora described above.

## 7. Conclusion

The study rests on **three language-specific speech corpora**: the Spanish **PC-GITA** corpus (50 PD, 50 HC Colombian Spanish speakers), a German-language corpus of 88 PD and 88 HC speakers, and a Czech-language corpus of 100 speakers (50 PD, 50 HC) (document_1.txt; document_2.txt). All recordings were noise-controlled and down-sampled to 16 kHz, and all patients were clinically rated with MDS-UPDRS-III (document_1.txt). The datasets were transformed into 160 ms voiced–unvoiced transition segments and represented as 80 × 41 Mel spectrograms for CNN training, with a hand-crafted feature/SVM pipeline serving as a baseline (document_1.txt). Transfer learning between these corpora improved accuracy by up to 8% and produced more balanced, lower-variance models, but only when the base model was sufficiently robust—an outcome observed for Spanish-initialised models (document_1.txt). The principal constraints on reuse are the unresolved German cohort size, the ON-state recording of Spanish patients, the severity imbalance across languages, and the uneven speech-task protocols across corpora (document_1.txt; document_2.txt).

## References

Arias-Vergara, T., et al. (2019). *Convolutional neural networks and a transfer learning strategy to classify Parkinson's disease from speech in three different languages* [Source document]. document_1.txt

Third-party research note: *Convolutional neural networks and a transfer learning strategy to classify Parkinson's disease from speech in three different languages* [Source document]. (n.d.). document_2.txt