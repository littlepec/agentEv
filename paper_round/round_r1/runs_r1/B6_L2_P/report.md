# Datasets Used in the Cross-Lingual Parkinson's Disease Speech Classification Study (arXiv:2002.04374)

## 1. Introduction and Scope of the Report

The query asks which datasets are used in the study *"Convolutional Neural Networks and a Transfer Learning Strategy to Classify Parkinson's Disease from Speech in Three Different Languages"* (Vásquez-Correa et al., 2020). The answer is not a single corpus but a triad of language-specific speech collections — Spanish, German, and Czech — assembled specifically to test whether a convolutional neural network (CNN) trained on one language can be fine-tuned to classify Parkinson's disease (PD) in another. The paper states plainly that "speech recordings of patients in three different languages are considered: Spanish, German, and Czech," and that all recordings "were captured in noise controlled conditions" and down-sampled to 16 kHz ([Vásquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)). This report identifies each dataset by name, source, speaker composition, elicitation protocol and clinical annotation, and then evaluates how each was used and how reliable the reported figures appear to be.

## 2. The Three Primary Datasets

### 2.1 Spanish: The PC-GITA Corpus

The Spanish component of the study is drawn from the PC-GITA corpus, a Colombian Spanish speech database created by Orozco-Arroyave et al. (2014) and cited in the study as reference [6] ([Vásquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)). PC-GITA "contains utterances from 50 PD patients and 50 HC, Colombian Spanish native speakers," giving a balanced 50/50 design with 100 speakers in total ([Vásquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)). A third-party research note confirms this composition, describing PC-GITA as the Spanish portion of the cross-lingual data and stating that it "provides the Spanish portion of the cross-lingual speech data" (Third-Party Research Note, n.d.).

The speaking tasks recorded in PC-GITA are unusually broad in this study: participants "pronounce a total of 10 sentences, the rapid repetition of /pa-ta-ka/, /pe-ta-ka/, /pa-ka-ta/, /pa/, /ta/, and /ka/, one text with 36 words, and a monologue" ([Vásquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)). Notably, all Spanish patients were recorded in the ON state, "i.e., under the effect of their daily medication" ([Vásquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)). PC-GITA has an established track record in the literature cited by the authors: earlier Gaussian mixture model and SVM work on this corpus reached accuracies of up to 77%, and a subsequent forced-Gaussian methodology reported up to 81% for Spanish data ([Vásquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)). In the present study, PC-GITA plays the strategic role of "base" language, because Spanish speakers showed "the best initial separability," which made the Spanish-trained CNN the most effective initialization for the other two languages ([Vásquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)).

### 2.2 German: German Speech Recordings

The German data are described in the methods section as "speech recordings of 88 PD patients and 88 HC speakers from Germany," attributed to Skodda, Visser and Schlegel (2011), *Journal of Voice* ([Vásquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)). The participants performed "four speech task[s]: the rapid repetition of /pa-ta-ka/, 5 sentences, one text with 81 words, and a monologue" ([Vásquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)).

The third-party research note, however, reports that "the German data consist of speech recordings of 44 PD patients and 44 HC speakers," and explicitly states that the speaker counts "are 44 PD patients with 44 HC speakers" (Third-Party Research Note, n.d.). This is a material discrepancy that must be flagged rather than smoothed over. My assessment is that the primary source figure (88 PD and 88 HC) should be preferred, for three reasons: (i) it appears in the methods section of the paper itself, which is the authoritative description of the data; (ii) the gender breakdown in the paper's Table 1 shows counts of 47 and 44 for the German male subgroups, which is arithmetically incompatible with a per-group total of 44 but compatible with a per-group total of 88; and (iii) a per-group figure of 44 plus 44 would yield 88 total German speakers, which may be the number the third-party note is actually reporting. The German corpus nevertheless has a lower internal weight in the study's narrative than the Spanish corpus, since the German baseline model (69.3% accuracy) outperformed the German CNN, making German a beneficiary — rather than an origin — of transfer learning ([Vásquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)).

### 2.3 Czech: Czech Speech Recordings

The Czech dataset comprises "a total of 100 native Czech speakers (50 PD, 50 HC)," attributed to Rusz (2018), a habilitation thesis at the Czech Technical University in Prague, cited as reference [19] ([Vásquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374); Third-Party Research Note, n.d.). The tasks comprise "the rapid repetition of the syllables /pa-ta-ka/, a read text with 80 words, and a monologue" ([Vásquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)). Czech speech material from Rusz et al. had previously been used in forced-Gaussian classification work, where accuracies of up to 94% were reported for Czech data and up to 81% for Spanish data ([Vásquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)). In the present study, Czech behaved differently from German: "for Czech language the CNN produces the highest accuracy," meaning the deep model outperformed the hand-crafted-feature baseline within that language ([Vásquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)).

## 3. Comparative Summary of the Datasets

The following table consolidates the dataset characteristics as reported across the two source documents.

| Attribute | Spanish (PC-GITA) | German | Czech |
|---|---|---|---|
| Corpus / provenance | PC-GITA, Orozco-Arroyave et al. (2014) | Skodda, Visser & Schlegel (2011) | Rusz (2018), habilitation thesis |
| PD speakers | 50 | 88 (note: 44 in third-party note) | 50 |
| Healthy controls | 50 | 88 (note: 44 in third-party note) | 50 |
| Total speakers | 100 | 176 (note: 88 in third-party note) | 100 |
| Native variety | Colombian Spanish | German | Czech |
| Sampling rate | 16 kHz | 16 kHz | 16 kHz |
| Recording condition | Noise controlled | Noise controlled | Noise controlled |
| Clinical scale | MDS-UPDRS-III | MDS-UPDRS-III | MDS-UPDRS-III |
| Role in study | Base language; best initial separability | Target language (benefited from transfer) | Target language (benefited from transfer) |

Sources: ([Vásquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374); Third-Party Research Note, n.d.).

## 4. Speech Tasks and Elicitation Protocols

Because the study classifies articulation difficulties at voiced–unvoiced transitions, the task design of each dataset matters as much as speaker counts. The three corpora share a core set of diadochokinetic and connected-speech tasks, but they differ in the number of sentences and the length of read texts, which the authors themselves used to explain language-dependent effects — noting that Czech and German "are richer than Spanish language in terms of consonant production," which "may cause that it is easier to produce consonant sounds by Czech PD patients than by Spanish PD patients" ([Vásquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)).

| Language | Rapid syllable repetition | Sentences | Read text | Monologue |
|---|---|---|---|---|
| Spanish | /pa-ta-ka/, /pe-ta-ka/, /pa-ka-ta/, /pa/, /ta/, /ka/ | 10 | 36 words | Yes |
| German | /pa-ta-ka/ | 5 | 81 words | Yes |
| Czech | /pa-ta-ka/ | — | 80 words | Yes |

Sources: ([Vásquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)).

## 5. Clinical Characterization: MDS-UPDRS-III

All three datasets are clinically annotated with the third section of the Movement Disorder Society–sponsored revision of the Unified Parkinson's Disease Rating Scale (MDS-UPDRS-III; Goetz et al., 2008), with evaluation performed "by a neurologist expert" ([Vásquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)). The paper's Table 1 reports, for each language, the number of speakers, gender breakdown, age ranges, mean age with standard deviation, MDS-UPDRS-III scores, and time after diagnosis in years ([Vásquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)).

| Language / group | Age range | Mean age (SD) | Mean MDS-UPDRS-III (SD) |
|---|---|---|---|
| Spanish PD | 33–81 | 60.7 (7.3) | 37.8 (22.1) |
| Spanish HC | 31–86 | 61.4 (7.0) | — |
| German PD | 44–82 | 66.2 (9.7) | 22.1 (9.9) |
| German HC | 26–83 | 62.6 (15.2) | — |
| Czech PD | 43–82 | 60.1 (8.7) | 21.4 (11.5) |
| Czech HC | 41–77 | 63.5 (11.1) | — |

Sources: ([Vásquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)). Values are those recoverable from the source's Table 1 as presented in the extracted text; the gender-specific sub-rows are partially corrupted in the source rendering.

This severity differential is central to the study's interpretation. The paper states that "for the patients in the Spanish language, the average MDS-UPDRS-III score is higher compared with the German and Czech patients, i.e., there are patients with higher disease severity in the Spanish data compared to German and Czech patients" ([Vásquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)). This recorded severity gap is the authors' explanation for why Spanish yielded the most separable models and why Spanish-trained weights transferred best.

## 6. How the Datasets Were Processed and Used

Each recording was analyzed through automatic detection of onset and offset transitions, "which model the difficulties of the patients to start/stop the movement of the vocal folds," with detection based on the presence of the fundamental frequency in short-time frames; 80 ms of signal were taken to the left and right of each voiced–unvoiced border, producing 160 ms segments ([Vásquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)). Two modeling streams were then run on the same data.

**Baseline stream.** Twelve Mel-Frequency Cepstral Coefficients with first and second derivatives plus log energy distributed over 22 Bark bands gave 58 descriptors; four statistical functionals (mean, standard deviation, skewness, kurtosis) produced a 232-dimensional feature vector per utterance, classified by a radial-basis SVM with C = 10 and γ = 0.0001 under speaker-independent 10-fold cross-validation ([Vásquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)).

**CNN stream.** A short-time Fourier transform with 256 frequency bins (16 ms window, 4 ms step) yielded 41 time frames, which were mapped to an 80-filter Mel scale to form 80 × 41 spectrograms for training a CNN with four convolutional/max-pooling layers, dropout regularization, two fully connected layers and a softmax output, optimized with cross-entropy loss and Adam ([Vásquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)). A final decision per speaker was obtained "by a majority voting strategy among the different speech exercises" ([Vásquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)).

**Transfer learning across the datasets.** A CNN trained on one language's utterances was used to initialize models for the remaining languages via fine-tuning ([Vásquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)). The reported cross-lingual results are summarized below.

| Base language | Target language | Accuracy (%) | Sensitivity (%) | Specificity (%) | MCC |
|---|---|---|---|---|---|
| German | Spanish | 70.0 | 62.0 | 78.0 | 0.41 |
| Czech | Spanish | 72.0 | 67.0 | 78.0 | 0.46 |
| Spanish | German | 77.3 | 86.2 | 68.3 | 0.57 |
| Czech | German | 76.7 | 87.5 | 66.0 | 0.55 |
| Spanish | Czech | 72.6 | 82.0 | 62.0 | 0.46 |
| German | Czech | 70.7 | 80.0 | 62.5 | 0.38 |

Sources: ([Vásquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)). Values reproduce the rows of the source's Table 4.

Transfer improved accuracy "over 8% for German (from 69.3% in the baseline to 77.3% when the model is fine-tuned from Spanish), and over 4.1% for Czech language (from 68.5% with the initial CNN to 72.6% when the model is fine-tuned from Spanish)" ([Vásquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)). Transferred models were also more balanced in specificity–sensitivity and had lower variance than the within-language models ([Vásquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)).

## 7. Datasets Referenced in the Literature but Not Used in This Study

For clarity, three speech datasets appear in the paper only as prior literature and are **not** part of the experimental data: (i) the Turkish dataset of Sakar et al., comprising 20 PD patients and 20 healthy controls, on which KNN and SVM classifiers reached up to 75% accuracy; (ii) the Czech data of Rusz, Cmejla et al. used in earlier forced-Gaussian work, reaching up to 94% for Czech; and (iii) the PC-GITA corpus in its earlier role as a benchmark producing up to 77% and 81% accuracy in GMM/SVM studies ([Vásquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)). The authors also cite handwriting-based PD transfer learning as a parallel research line, again without using such data here ([Vásquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)).

## 8. Reliability Assessment and Limitations

Several considerations temper confidence in the dataset description. First, the German speaker count is inconsistent between sources (88 vs. 44 per group), and the primary source's Table 1, which holds the definitive composition, is only partially legible in the extracted text; the discrepancy should be recorded rather than resolved silently ([Vásquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374); Third-Party Research Note, n.d.). Second, the authors themselves caution that some earlier reported accuracies of 80–94% "were optimistic, since the hyper-parameters of the classifier were optimized based on the accuracy on the test set" — a methodological warning that applies to the corpus literature generally ([Vásquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)). Third, the authors report that in a strictly language-independent scenario — training on one language and testing on the other two — results "were not satisfactory (accuracy < 60%)" ([Vásquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)). Fourth, the source is a 2020 arXiv preprint (arXiv:2002.04374) rather than a formally peer-reviewed journal article, and the third-party note is a secondary, unattributed summary; where the two disagree, the primary source carries more weight. Fifth, the paper does not describe a public distribution mechanism for the German and Czech recordings, whereas PC-GITA is a named, previously published corpus, and the German and Czech portions are described only through their cited source publications ([Vásquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)).

## 9. Conclusion

The study uses three speech datasets, one per language: the Spanish **PC-GITA corpus** (50 PD patients and 50 healthy Colombian Spanish speakers), the German speech recordings (88 PD patients and 88 healthy controls according to the primary source, or 44/44 according to the third-party note, from Skodda et al., 2011), and the Czech speech recordings (50 PD patients and 50 healthy controls, from Rusz, 2018) ([Vásquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374); Third-Party Research Note, n.d.). All three were captured under noise-controlled conditions, down-sampled to 16 kHz, annotated with MDS-UPDRS-III severity scores by a neurologist, and elicited with overlapping sets of diadochokinetic, read-text and monologue tasks ([Vásquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)). The three corpora are not interchangeable inputs: the Spanish data contained the more severely affected patients, the German baseline outperformed its CNN, the Czech CNN outperformed its baseline, and only the Spanish-trained base model proved "robust enough" to materially improve target-language accuracy through transfer learning ([Vásquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)). The study's own framing — that Spanish "speakers have the best initial separability, thus, the other two languages benefit from the best initial model" — is therefore a data-level finding as much as a modeling one ([Vásquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)).

## References

Third-Party Research Note. (n.d.). *Third-party research note: Convolutional Neural Networks and a Transfer Learning Strategy to Classify Parkinson's Disease from Speech in Three Different Languages* [document_2.txt].

Vásquez-Correa, J. C., Arias-Vergara, T., Rios-Urrego, C. D., Schuster, M., Rusz, J., Orozco-Arroyave, J. R., & Nöth, E. (2020). *Convolutional neural networks and a transfer learning strategy to classify Parkinson's disease from speech in three different languages* (arXiv:2002.04374) [document_1.txt]. https://arxiv.org/abs/2002.04374

### Corpora and Scales Cited Within the Primary Source

Goetz, C. G., et al. (2008). Movement Disorder Society-sponsored revision of the Unified Parkinson's Disease Rating Scale (MDS-UPDRS): Scale presentation and clinimetric testing results. *Movement Disorders, 23*(15), 2129–2170.

Orozco-Arroyave, J. R., et al. (2014). New Spanish speech corpus database for the analysis of people suffering from Parkinson's disease. In *Proceedings of the Ninth International Conference on Language Resources and Evaluation* (pp. 342–347). [PC-GITA]

Rusz, J. (2018). *Detecting speech disorders in early Parkinson's disease by acoustic analysis* [Habilitation thesis, Czech Technical University in Prague].

Skodda, S., Visser, W., & Schlegel, U. (2011). Vowel articulation in Parkinson's disease. *Journal of Voice, 25*(4), 467–472.