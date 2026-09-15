# Datasets Used in the Cross-Lingual Parkinson's Disease Speech Classification Study

## 1. Purpose and Scope

This report answers the question "What datasets are used?" with respect to a study that classified Parkinson's disease (PD) from speech using convolutional neural networks (CNNs) and a cross-lingual transfer-learning strategy ([document_1.txt](document_1.txt)). In the most direct terms, the study does not rely on a single corpus. It uses three language-specific speech datasets — **Spanish, German, and Czech** — each containing recordings of PD patients and healthy control (HC) speakers, all captured under noise-controlled conditions and down-sampled to 16 kHz ([document_1.txt](document_1.txt)). The three language groups together supply the base and target domains for the transfer-learning experiments, in which a CNN pre-trained on one language is fine-tuned to classify utterances in another ([document_1.txt](document_1.txt)).

The remainder of this report identifies each dataset by name and composition, describes the demographic and clinical metadata attached to it, explains the recording and task protocol, documents how the raw corpora were transformed into model input, and evaluates how each dataset performed as both a base and a target domain.

## 2. Overall Data Architecture

Three speech datasets from three countries and three languages form the empirical foundation of the study ([document_1.txt](document_1.txt)). The recordings were captured in noise-controlled conditions and down-sampled to 16 kHz ([document_1.txt](document_1.txt)). All patients across the three datasets were evaluated by a neurologist expert according to the third section of the Movement Disorder Society–Unified Parkinson's Disease Rating Scale (MDS-UPDRS-III), which provides the clinical severity reference for the speech-based models ([document_1.txt](document_1.txt)). A summary table in the source ("Table 1") consolidates speaker numbers, gender, age ranges and means, time since diagnosis, and MDS-UPDRS-III scores ([document_1.txt](document_1.txt)).

A third-party research note confirms the same three-corpus structure: Spanish data drawn from PC-GITA, German recordings from 88 PD and 88 HC speakers, and Czech recordings from 50 PD and 50 HC speakers ([document_2.txt](document_2.txt)). Taken together, the datasets contain 188 PD patients and 188 healthy control speakers, i.e., 376 participants in total, with an exact 1:1 class balance within every language ([document_1.txt](document_1.txt), [document_2.txt](document_2.txt)).

## 3. The Spanish Dataset: PC-GITA

The Spanish portion of the data comes from the **PC-GITA corpus** ([document_2.txt](document_2.txt)). PC-GITA contains utterances from 50 PD patients and 50 HC subjects, all Colombian Spanish native speakers ([document_2.txt](document_2.txt)). This composition is corroborated by Table 1 in the primary source, which reports 25 male and 25 female speakers in each class for the Spanish group, giving 50 PD and 50 HC speakers ([document_1.txt](document_1.txt)).

The Spanish dataset is clinically distinctive. Its patients have the highest mean MDS-UPDRS-III scores of the three groups: 37.8 (SD = 22.1) for men and 37.6 (SD = 14.1) for women, compared with 22.1 (SD = 9.9) and 23.3 (SD = 12.0) in German patients and 21.4 (SD = 11.5) and 18.1 (SD = 9.7) in Czech patients ([document_1.txt](document_1.txt)). Mean time since diagnosis is also longest for Spanish women at 12.6 years (SD = 11.6), versus 8.7 years (SD = 5.9) for Spanish men, roughly 7 years for German speakers, and about 6.7–6.8 years for Czech speakers ([document_1.txt](document_1.txt)). Mean ages are comparable across groups, ranging from 60.1 to 66.7 years depending on language, gender, and class ([document_1.txt](document_1.txt)).

The consequence of this severity profile is explicitly noted in the study: because the Spanish patients present higher disease severity, the Spanish data exhibit the best initial separability between PD and HC speakers, which explains why Spanish performs best as a base language in transfer learning ([document_1.txt](document_1.txt)).

## 4. The German Dataset

The German dataset contains speech recordings of **88 PD patients and 88 HC speakers from Germany** ([document_2.txt](document_2.txt)). Table 1 of the primary source breaks this down further: 47 male and 41 female PD patients, and 44 male and 44 female healthy controls, i.e., 88 patients and 88 controls ([document_1.txt](document_1.txt)).

German participants are the oldest of the three groups on average, with mean ages of 66.7 years (SD = 8.7) for male patients, 66.2 years (SD = 9.7) for female patients, 63.8 years (SD = 12.7) for male controls, and 62.6 years (SD = 15.2) for female controls ([document_1.txt](document_1.txt)). Age ranges are also the widest overall, extending from 26 to 83 years in male controls and 28 to 85 years in female controls ([document_1.txt](document_1.txt)). Mean time since diagnosis is approximately 7.0 years for men (SD = 5.5) and 7.1 years for women (SD = 6.2), and mean MDS-UPDRS-III scores are 22.1 (SD = 9.9) and 23.3 (SD = 12.0) for men and women respectively ([document_1.txt](document_1.txt)).

The German dataset is therefore the largest of the three in speaker count and the most age-diverse, although its patients are, on average, less severely affected than the Spanish patients ([document_1.txt](document_1.txt)). Notably, the German data are the only language for which the hand-crafted baseline classifier outperformed the individual CNN, and the language that gained the largest accuracy improvement from transfer learning ([document_1.txt](document_1.txt)).

## 5. The Czech Dataset

The Czech data comprise a total of **100 native Czech speakers — 50 PD patients and 50 healthy controls** ([document_1.txt](document_1.txt), [document_2.txt](document_2.txt)). Table 1 reports 30 male and 20 female patients and 30 male and 20 female controls, totaling 50 subjects per class ([document_1.txt](document_1.txt)). The source for this corpus is cited as a habilitation thesis on detecting speech disorders in early Parkinson's disease by acoustic analysis ([document_1.txt](document_1.txt)).

Czech participants have mean ages of 65.3 years (SD = 9.6) for male patients, 60.1 years (SD = 8.7) for female patients, 60.3 years (SD = 11.5) for male controls, and 63.5 years (SD = 11.1) for female controls ([document_1.txt](document_1.txt)). Time since diagnosis averages 6.7 years (SD = 4.5) for men and 6.8 years (SD = 5.2) for women ([document_1.txt](document_1.txt)). The Czech group records the lowest mean MDS-UPDRS-III scores among the three datasets, at 21.4 (SD = 11.5) for men and 18.1 (SD = 9.7) for women ([document_1.txt](document_1.txt)).

The Czech dataset is also the only one for which the specific speech tasks are described in the provided material: rapid repetition of the syllables /pa-ta-ka/, a read text of 80 words, and a monologue ([document_1.txt](document_1.txt)). This matters because the study analyzed "all speech exercises performed by the participants" and derived a per-speaker decision by majority voting across exercises ([document_1.txt](document_1.txt)).

## 6. Comparative Summary of the Three Datasets

The table below consolidates the quantitative description of the three datasets as reported in Table 1 of the primary source and corroborated by the third-party note ([document_1.txt](document_1.txt), [document_2.txt](document_2.txt)).

| Feature | Spanish (PC-GITA) | German | Czech |
|---|---|---|---|
| PD speakers (M / F) | 25 / 25 (50 total) | 47 / 41 (88 total) | 30 / 20 (50 total) |
| HC speakers (M / F) | 25 / 25 (50 total) | 44 / 44 (88 total) | 30 / 20 (50 total) |
| Mean age, PD M (SD) | 61.3 (11.4) | 66.7 (8.7) | 65.3 (9.6) |
| Mean age, PD F (SD) | 60.7 (7.3) | 66.2 (9.7) | 60.1 (8.7) |
| Mean age, HC M (SD) | 60.5 (11.6) | 63.8 (12.7) | 60.3 (11.5) |
| Mean age, HC F (SD) | 61.4 (7.0) | 62.6 (15.2) | 63.5 (11.1) |
| Time since diagnosis, M (SD) | 8.7 (5.9) | 7.0 (5.5) | 6.7 (4.5) |
| Time since diagnosis, F (SD) | 12.6 (11.6) | 7.1 (6.2) | 6.8 (5.2) |
| MDS-UPDRS-III, M (SD) | 37.8 (22.1) | 22.1 (9.9) | 21.4 (11.5) |
| MDS-UPDRS-III, F (SD) | 37.6 (14.1) | 23.3 (12.0) | 18.1 (9.7) |
| Speech tasks specified | Not detailed in excerpts | Not detailed in excerpts | /pa-ta-ka/, 80-word text, monologue |

## 7. Recording, Segmentation, and Signal-Derived Data

Beyond the raw corpora, the study generated a derived dataset for model training. Speech signals were analyzed by automatically detecting onset and offset transitions, which model the difficulty patients have in starting or stopping vocal-fold movement ([document_1.txt](document_1.txt)). Transition detection relies on the presence of the fundamental frequency in short-time frames; the border between voiced and unvoiced frames is identified, and 80 ms of signal on each side yields 160 ms segments ([document_1.txt](document_1.txt)).

Two modeling streams consume these segments: (1) a baseline using hand-crafted features classified by a support vector machine, and (2) time-frequency representations fed to a CNN ([document_1.txt](document_1.txt)). The latter uses short-time Fourier transform spectrograms with 256 frequency bins, a 16 ms window, and a 4 ms step, producing 41 time frames per transition; these are mapped to the Mel scale with 80 filters, resulting in an 80 × 41 spectrogram per segment ([document_1.txt](document_1.txt)). This derived representation, not the raw audio, is what the three language datasets ultimately contribute to the CNN pipeline.

## 8. How the Datasets Function in the Experiments

The experiments first train baseline and CNN models on each language individually, then use each trained CNN as a base model for transfer learning into the other two languages ([document_1.txt](document_1.txt)). This produces six cross-lingual base–target combinations. On the individual-language models, Spanish achieved accuracies of 73.7% (baseline) and 71.0% (CNN), German 69.3% (baseline) and 63.1% (CNN), and Czech 61.0% (baseline) and 68.5% (CNN); the authors note that results in all three languages were unbalanced toward one class in terms of specificity and sensitivity ([document_1.txt](document_1.txt)).

Transfer learning changed this picture. Recorded accuracies include 77.3% for a Spanish-based model fine-tuned on German (sensitivity 86.2%, specificity 68.3%, MCC 0.57), 76.7% for Spanish-based transfer to Czech (sensitivity 87.5%, specificity 66.0%, MCC 0.55), 72.0% for German-based transfer to Czech, 70.0% for German-based transfer to Spanish, 72.6% for a Czech-based transfer to Spanish, and 70.7% for Czech-based transfer to German ([document_1.txt](document_1.txt)). The narrative reports an improvement of over 8% for German (from 69.3% baseline to 77.3%) and over 4.1% for Czech (from 68.5% to 72.6%) when the Spanish model is used as the base, and states that German and Czech reach their highest accuracy when Spanish is the base language ([document_1.txt](document_1.txt)). ROC analysis shows that when the target is Spanish the AUC is slightly higher with a Czech base, whereas for German and Czech targets the highest AUC is obtained with a Spanish base ([document_1.txt](document_1.txt)).

## 9. Critical Appraisal

Several observations follow directly from the data. First, the design is unusually well controlled for a multilingual clinical speech study: every language has an exact 1:1 patient–control split, all recordings come from noise-controlled settings, all patients were rated with the same clinical instrument (MDS-UPDRS-III), and the same feature pipeline (Mel spectrograms of 160 ms voiced–unvoiced transitions) was applied uniformly ([document_1.txt](document_1.txt)). That harmonization is what makes the cross-lingual comparison defensible.

Second, the datasets are not interchangeable. The German corpus is roughly 76% larger than either the Spanish or Czech corpus (88 versus 50 speakers per class), and it is the most age-diverse ([document_1.txt](document_1.txt)). The Spanish corpus, despite being tied for smallest, carries the most severely affected patients and therefore the best initial class separability, which is why it functions as the strongest base model for transfer ([document_1.txt](document_1.txt)). My assessment is that the study's central result — cross-lingual transfer gains of up to 8% — is driven less by language similarity than by the clinical severity distribution of the source corpus; a base model is only as good as the separability of its source data.

Third, the authors themselves identify a linguistic confound: Czech and German are richer than Spanish in consonant production, which could make consonant sounds easier for Czech PD patients to produce than for Spanish PD patients, and this language-dependent bias must be handled carefully ([document_1.txt](document_1.txt)). Fourth, the extracted version of Table 4 contains an internal inconsistency: the narrative attributes 72.6% to a Spanish-base model for Czech, while the table also lists 76.7% for a Spanish-to-Czech configuration ([document_1.txt](document_1.txt)). This warrants caution when quoting any single transfer figure, although the direction of the effect — Spanish as the strongest base — is consistent across text, tables, and ROC analysis.

Fifth, coverage gaps should be acknowledged. The provided material names PC-GITA for Spanish and cites a habilitation thesis for Czech, but does not name the German corpus or detail the Spanish and German speech tasks; only the Czech tasks are specified ([document_1.txt](document_1.txt), [document_2.txt](document_2.txt)). The study also points to future work involving hyper-parameter optimization, base models trained on two languages instead of one, classification of disease stage from MDS-UPDRS-III or dysarthria severity, and transfer across diseases such as Huntington's disease ([document_1.txt](document_1.txt)).

## 10. Conclusion

The study uses three language-specific Parkinson's disease speech datasets: the Spanish PC-GITA corpus (50 PD, 50 HC Colombian Spanish speakers), a German dataset (88 PD, 88 HC speakers from Germany), and a Czech dataset (50 PD, 50 HC native Czech speakers) ([document_1.txt](document_1.txt), [document_2.txt](document_2.txt)). All were recorded under noise-controlled conditions, down-sampled to 16 kHz, clinically scored with MDS-UPDRS-III, and converted into 160 ms voiced–unvoiced transition segments represented as 80 × 41 Mel spectrograms for CNN training ([document_1.txt](document_1.txt)). Together they form a balanced, multilingual benchmark of 376 speakers in which Spanish supplies the strongest base model, German supplies the largest sample, and Czech supplies the only fully documented task battery.

## References

document_1.txt [Manuscript text, tables, and references on convolutional neural networks and transfer learning for classifying Parkinson's disease from speech in Spanish, German, and Czech]. (n.d.).

document_2.txt [Third-party research note on convolutional neural networks and a transfer learning strategy to classify Parkinson's disease from speech in three different languages]. (n.d.).