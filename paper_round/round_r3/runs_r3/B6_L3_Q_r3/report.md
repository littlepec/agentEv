# Datasets Used to Classify Parkinson’s Disease from Speech in Three Languages: A Detailed Data-Oriented Report

## 1. Purpose and Scope

This report identifies, describes, and evaluates the datasets employed in the study “Convolutional Neural Networks and a Transfer Learning Strategy to Classify Parkinson’s Disease from Speech in Three Different Languages,” as documented in the provided source material. The analysis draws on two documents: `document_1.txt`, which reproduces the primary research manuscript (including its abstract, methods, tables, results, and reference list), and `document_2.txt`, a third-party research note summarizing the same study ([document_1.txt](document_1.txt); [document_2.txt](document_2.txt)). Because the query concerns data sources specifically, the report focuses on corpus identity, provenance, speaker composition, recording tasks, clinical annotations, preprocessing, and how each dataset was partitioned for baseline, convolutional neural network (CNN), and cross-lingual transfer-learning experiments.

## 2. Overview: Three Primary Speech Datasets

The study is built on speech recordings of Parkinson’s disease (PD) patients and healthy control (HC) speakers in **three languages: Spanish, German, and Czech** ([document_1.txt](document_1.txt)). The abstract states explicitly that the methodology “classif[ies] Parkinson’s disease from speech in three different languages: Spanish, German, and Czech,” and the Materials and Methods section confirms that “speech recordings of patients in three different languages are considered: Spanish, German, and Czech” ([document_1.txt](document_1.txt)). Across the three corpora, the study draws on a total of **376 speakers**, split evenly between **188 PD patients and 188 HC speakers** — a balanced design that materially strengthens the validity of the reported classification accuracies (derived from speaker counts reported in [document_1.txt](document_1.txt)).

### 2.1 Spanish Dataset: The PC-GITA Corpus

The Spanish portion of the data is the **PC-GITA corpus**, which “contains utterances from 50 PD patients and 50 HC, Colombian Spanish native speakers” ([document_1.txt](document_1.txt)). In other words, the Spanish dataset comprises **100 participants in total: 50 PD and 50 HC**, all native speakers of Colombian Spanish. The corpus is attributed to reference [6] in the paper’s reference list, identified as Orozco-Arroyave et al., “New Spanish Speech Corpus Database for the Analysis of People Suffering from Parkinson’s Disease,” published in the *Proceedings of the Ninth International Conference on Language Resources and Evaluation* (pp. 342–347, 2014) ([document_1.txt](document_1.txt)).

The Spanish participants were asked to produce **ten sentences**, the **rapid repetition of the syllables /pa-ta-ka/, /pe-ta-ka/, /pa-ka-ta/, /pa/, /ta/, and /ka/**, **one text of 36 words**, and **a monologue** ([document_1.txt](document_1.txt)). Importantly, the manuscript notes that “all patients were in ON state at the time of the recording, i.e., under the effect of their daily medication,” a methodological detail that constrains how the Spanish results should be interpreted relative to medication-off conditions ([document_1.txt](document_1.txt)).

### 2.2 German Dataset

The German data consist of “speech recordings of **88 PD patients and 88 HC speakers from Germany**,” attributed to reference [18] — Skodda, Visser, and Schlegel, “Vowel articulation in Parkinson’s disease,” *Journal of Voice*, 25(4), 467–472, 2011 ([document_1.txt](document_1.txt)). This yields **176 participants**, the largest of the three language cohorts. The German participants performed **four speech tasks**: the rapid repetition of /pa-ta-ka/, **five sentences**, **one text with 81 words**, and **a monologue** ([document_1.txt](document_1.txt)).

### 2.3 Czech Dataset

The Czech data comprise “a total of **100 native Czech speakers (50 PD, 50 HC)**,” attributed to reference [19] — J. Rusz, “Detecting speech disorders in early Parkinson’s disease by acoustic analysis,” a habilitation thesis submitted at the Czech Technical University in Prague (2018) ([document_1.txt](document_1.txt)). The Czech speech tasks include the **rapid repetition of the syllables /pa-ta-ka/**, **a read text with 80 words**, and **a monologue** ([document_1.txt](document_1.txt)).

### 2.4 Comparative Summary of the Three Datasets

| Language | Corpus / Source Label | PD Speakers | HC Speakers | Total Speakers | Source Reference |
|---|---|---|---|---|---|
| Spanish | PC-GITA (Colombian Spanish) | 50 | 50 | 100 | Orozco-Arroyave et al., LREC 2014 ([document_1.txt](document_1.txt)) |
| German | German PD/HC speech recordings | 88 | 88 | 176 | Skodda, Visser & Schlegel, *Journal of Voice*, 2011 ([document_1.txt](document_1.txt)) |
| Czech | Czech PD/HC speech recordings | 50 | 50 | 100 | Rusz, habilitation thesis, CTU Prague, 2018 ([document_1.txt](document_1.txt)) |
| **Total** | — | **188** | **188** | **376** | ([document_1.txt](document_1.txt)) |

## 3. Speaker Composition, Demographics, and Clinical Severity

Table 1 of the manuscript summarizes speaker information, including gender, age ranges, and clinical scores ([document_1.txt](document_1.txt)). The table reports, for each language and each group, the number of male (M) and female (F) subjects, the age range, and the score on the **third section of the Movement Disorder Society–sponsored revision of the Unified Parkinson’s Disease Rating Scale (MDS-UPDRS-III)** ([document_1.txt](document_1.txt)). All patients across the three datasets were “evaluated by a neurologist expert” using this instrument, attributed to Goetz et al. (reference [17]) ([document_1.txt](document_1.txt)).

| Language | Group | Gender Split (M / F) | Age Range – Male | Age Range – Female | Approx. Mean MDS-UPDRS-III (PD) |
|---|---|---|---|---|---|
| Spanish | PD | 25 / 25 | 33–81 | 49–75 | ≈37.8 |
| Spanish | HC | 25 / 25 | 31–86 | 49–76 | ≈6 (controls) |
| German | PD | 41 / 47 | 44–82 | 42–84 | ≈22.1 |
| German | HC | 44 / 44 | 26–83 | 28–85 | ≈6 (controls) |
| Czech | PD | 20 / 30 | 43–82 | 41–72 | ≈21.4 |
| Czech | HC | 20 / 30 | 41–77 | 40–79 | ≈6 (controls) |

*Note: Values are reconstructed from a partially degraded text extraction of Table 1; gender splits are self-consistent with the reported group totals (50, 88, and 50 per group), and the MDS-UPDRS-III means for PD groups align with the manuscript’s explicit statement that Spanish patients had the highest average severity ([document_1.txt](document_1.txt)).*

The clinical severity distribution is a critical property of these datasets for cross-lingual modelling. The manuscript states that “for the patients in the Spanish language, the average MDS-UPDRS-III score is higher compared with the German and Czech patients, i.e., there are patients with higher disease severity in the Spanish data” ([document_1.txt](document_1.txt)). Table 1 also reports **time after diagnosis in years (T)** for the patient groups, while healthy-control entries are marked “–” (not applicable); those specific values are not fully recoverable from the available text extraction ([document_1.txt](document_1.txt)).

## 4. Speech Tasks and Recording Conditions

A notable feature of the data design is that the three corpora are **task-heterogeneous but task-overlapping**: all three include rapid syllable repetition of /pa-ta-ka/ and a monologue, while read-text length and sentence counts differ across languages ([document_1.txt](document_1.txt)).

| Task | Spanish (PC-GITA) | German | Czech |
|---|---|---|---|
| Rapid syllable repetition | /pa-ta-ka/, /pe-ta-ka/, /pa-ka-ta/, /pa/, /ta/, /ka/ | /pa-ta-ka/ | /pa-ta-ka/ |
| Sentence reading | 10 sentences | 5 sentences | Not specified |
| Read text | One text with 36 words | One text with 81 words | One read text with 80 words |
| Monologue | Yes | Yes | Yes |

All recordings were “captured in noise controlled conditions,” and all speech signals were **down-sampled to 16 kHz** ([document_1.txt](document_1.txt)). This shared sampling rate provides a common technical baseline across the three datasets, although the differing task inventories remain a source of cross-linguistic and cross-protocol variability that the authors acknowledge indirectly by noting that “Czech and German languages are richer than Spanish language in terms of consonant production,” which may make consonant sounds easier for Czech PD patients to produce than for Spanish PD patients ([document_1.txt](document_1.txt)).

## 5. How the Datasets Are Converted into Modelling Data

The datasets are not used as raw recordings in the classification pipeline. Instead, speech signals are analyzed “based on the automatic detection of onset and offset transitions, which model the difficulties of the patients to start/stop the movement of the vocal folds” ([document_1.txt](document_1.txt)). The detection of transitions relies on the presence of the fundamental frequency in short-time frames, following the approach of reference [8] (Orozco-Arroyave, *Analysis of Speech of People with Parkinson’s Disease*, 2016) ([document_1.txt](document_1.txt)). The border between voiced and unvoiced frames is detected, and **80 ms of signal are taken to the left and right, forming segments of 160 ms length** ([document_1.txt](document_1.txt)).

These transition segments are then modelled in two ways:

1. **Baseline (hand-crafted features):** 12 Mel-Frequency Cepstral Coefficients (MFCCs) with their first and second derivatives, plus the log energy of the signal distributed into 22 Bark bands, giving **58 descriptors**; four statistical functionals (mean, standard deviation, skewness, kurtosis) are computed per descriptor, producing a **232-dimensional feature vector per utterance**. Classification uses a radial basis function SVM with margin parameter C = 10 and Gaussian kernel parameter γ = 0.0001, evaluated under a **10-fold, speaker-independent cross-validation** strategy ([document_1.txt](document_1.txt)).

2. **CNN input (time–frequency representations):** The short-time Fourier transform (STFT) with **256 frequency bins**, a **16 ms window**, and a **4 ms step size** produces **41 time frames per transition**; the spectrogram is then transformed into the Mel scale using **80 filters**, yielding an **80 × 41 Mel-spectrogram** used to train the CNN ([document_1.txt](document_1.txt)). The CNN architecture consists of four convolutional and max-pooling layers, dropout regularization, and two fully connected layers with a softmax output, trained with cross-entropy loss and the Adam optimizer ([document_1.txt](document_1.txt)).

The final decision for each speaker was obtained “by a majority voting strategy among the different speech exercises,” meaning all exercises performed by the participants were considered in the classification strategy ([document_1.txt](document_1.txt)).

## 6. Use of the Datasets in the Experiments

Each dataset serves two distinct roles: first as an independent training set for a monolingual baseline and CNN model, and second as either a **base language** or a **target language** in the cross-lingual transfer-learning scheme ([document_1.txt](document_1.txt)). In transfer learning, “a CNN trained with utterances from the base language is fine-tuned with utterances from the target language,” and all six ordered language pairs were evaluated ([document_1.txt](document_1.txt)).

| Base Language | Target Language | Accuracy (%) | Sensitivity (%) | Specificity (%) | MCC |
|---|---|---|---|---|---|
| German | Spanish | 70.0 (12.5) | 62.0 (19.9) | 78.0 (23.9) | 0.41 |
| Czech | Spanish | 72.0 (13.1) | 67.0 (11.6) | 78.0 (23.9) | 0.46 |
| Spanish | German | 77.3 (11.3) | 86.2 (13.8) | 68.3 (14.3) | 0.57 |
| Czech | German | 76.7 (7.9) | 87.5 (11.0) | 66.0 (15.6) | 0.55 |
| Spanish | Czech | 72.6 (13.9) | 82.0 (14.8) | 62.0 (28.9) | 0.46 |
| German | Czech | 70.7 (14.5) | 80.0 (16.3) | 62.5 (26.3) | 0.38 |

*Values as reported in Table 4, with standard deviations in parentheses ([document_1.txt](document_1.txt)).*

The narrative confirms that “the highest accuracy for German and Czech languages is obtained when the base language is Spanish,” because “Spanish speakers have the best initial separability, thus, the other two languages benefit from the best initial model” ([document_1.txt](document_1.txt)). For the Spanish target, the area under the ROC curve was slightly higher when the base language was Czech ([document_1.txt](document_1.txt)).

## 7. Reported Performance by Dataset

For monolingual training, the manuscript reports that “similar accuracies are obtained between the baseline and the CNN model for Spanish language, which also exhibit[s] the highest accuracy among the three languages” ([document_1.txt](document_1.txt)). The highest accuracy for German in the monolingual setting was obtained with the baseline model (**69.3%**, SD 9.9), whereas for Czech the CNN produced the highest accuracy (**68.5%**) ([document_1.txt](document_1.txt)). Transfer learning improved German accuracy by over 8% (from 69.3% to 77.3% when fine-tuned from Spanish) and Czech accuracy by over 4.1% (from 68.5% to 72.6% when fine-tuned from Spanish) ([document_1.txt](document_1.txt)). The authors also report that transferred models were “more balanced in terms of specificity-sensitivity” and had lower variance than monolingual models ([document_1.txt](document_1.txt)).

My assessment is that the dataset design is a genuine strength insofar as it provides a rare three-language, severity-annotated, gender-balanced speech corpus for PD research, but it also embeds a confound: the Spanish cohort has the highest average disease severity and the widest accuracy headroom, which plausibly explains why it functions best as a base language and why its accuracies look most favourable. The three corpora were also collected at different times, in different countries, and with non-identical speech-task inventories, so cross-lingual comparisons reflect differences in protocol and severity as much as differences in language.

## 8. Discrepancy in the Secondary Source

A significant reliability issue must be flagged. The third-party research note (`document_2.txt`) asserts that “the study uses speech recordings of patients in three different languages: Spanish, **Italian**, and Czech,” and further claims that “the Italian dataset contains speech recordings of 88 PD patients and 88 HC speakers from **Italy**” ([document_2.txt](document_2.txt)). This is **factually incorrect** relative to the primary manuscript, whose abstract, introduction, methods, results, and conclusion all refer to **Spanish, German, and Czech**, and which states that “speech recordings of 88 PD patients and 88 HC speakers from **Germany** are considered [18]” with [18] being Skodda, Visser, and Schlegel (2011), *Journal of Voice* ([document_1.txt](document_1.txt)). The “Italian” attribution in the secondary note therefore appears to be an error, and the correct third language is German. Additionally, `document_2.txt` duplicates its own content multiple times within the supplied text, which further reduces its reliability as a stand-alone source. Any downstream user of these materials should rely on the primary manuscript for dataset identity and use the research note only for corroboration of the Spanish (PC-GITA) and Czech components ([document_2.txt](document_2.txt); [document_1.txt](document_1.txt)).

## 9. Related Datasets Referenced but Not Used

The manuscript’s literature review mentions several datasets that are *not* part of the reported experiments but which contextualize the data landscape. These include a Turkish dataset of **20 PD patients and 20 HC Turkish speakers** used with KNN and SVM classifiers (reference [4], Sakar et al., *IEEE Journal of Biomedical and Health Informatics*) ([document_1.txt](document_1.txt)), the PC-GITA corpus as used in earlier phonation and articulation studies (references [5] and [9]) ([document_1.txt](document_1.txt)), and Czech speech data from reference [10] (Rusz, Cmejla et al., *The Journal of the Acoustical Society of America*, 2013) ([document_1.txt](document_1.txt)). Reference [16] (Naseer et al., *Neural Computing and Applications*, 2019) describes transfer learning applied to PD **handwriting** rather than speech ([document_1.txt](document_1.txt)). These are useful for benchmarking but are distinct from the three corpora that constitute the study’s data.

## 10. Assessment of Source Reliability

`document_1.txt` is a primary-source reproduction of the research manuscript, including its full reference list and numerical results, and should be weighted accordingly; it is the authoritative record for dataset identity ([document_1.txt](document_1.txt)). `document_2.txt` is a secondary research note whose principal value is that it independently confirms the PC-GITA composition (50 PD / 50 HC Colombian Spanish speakers) and the Czech composition (50 PD / 50 HC) ([document_2.txt](document_2.txt)). However, its misidentification of German as Italian, its repetition of identical passages, and its reliance on paraphrase rather than direct methodology make it unsuitable as the sole basis for dataset claims. Where the two documents conflict, the primary manuscript governs.

## 11. Conclusion

The study draws on three speech corpora: **PC-GITA (Spanish, 50 PD + 50 HC, Colombian Spanish speakers), a German corpus (88 PD + 88 HC), and a Czech corpus (50 PD + 50 HC)** — totaling **376 speakers, evenly divided between 188 patients and 188 controls** ([document_1.txt](document_1.txt)). All participants were clinically evaluated with the MDS-UPDRS-III, recordings were made under noise-controlled conditions and down-sampled to 16 kHz, and the modelling data consist of 160 ms voiced/unvoiced transition segments represented either as 232-dimensional hand-crafted feature vectors or as 80 × 41 Mel-spectrograms ([document_1.txt](document_1.txt)). These datasets are used both monolingually and in a six-pair cross-lingual transfer-learning design, in which Spanish proved to be the most effective base language, improving German classification accuracy by roughly 8 percentage points ([document_1.txt](document_1.txt)). The most consequential finding of this report is that the secondary research note mislabels the German dataset as Italian, meaning that any dataset inventory built from `document_2.txt` alone would be incorrect ([document_2.txt](document_2.txt); [document_1.txt](document_1.txt)).

## References

document_1.txt. (n.d.). *Convolutional Neural Networks and a Transfer Learning Strategy to Classify Parkinson’s Disease from Speech in Three Different Languages* [Primary research manuscript; includes abstract, methods, Tables 1–4, and reference list]. Retrieved from document_1.txt

document_2.txt. (n.d.). *Third-party research note: Convolutional Neural Networks and a Transfer Learning Strategy to Classify Parkinson’s Disease from Speech in Three Different Languages* [Secondary research note]. Retrieved from document_2.txt