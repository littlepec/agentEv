# Datasets Used to Classify Parkinson's Disease from Speech in Three Languages: A Detailed Report

## 1. Scope and Source Basis

This report answers the question "What datasets are used?" with respect to the study *Convolutional Neural Networks and a Transfer Learning Strategy to Classify Parkinson's Disease from Speech in Three Different Languages*. The evidence base consists of two documents supplied for this analysis. The first is the text-extracted version of the study itself, a preprint-style technical paper authored by J. C. Vásquez-Correa, T. Arias-Vergara, C. D. Rios-Urrego, M. Schuster, J. Rusz, J. R. Orozco-Arroyave, and E. Nöth, with affiliations including the Pattern Recognition Lab at Friedrich-Alexander Universität Erlangen-Nürnberg, Universidad de Antioquia, Ludwig-Maximilians, and the Czech Technical University in Prague ([Vásquez-Correa et al., n.d.](document_1.txt)). The second is a third-party research note that summarizes the dataset composition of the same study ([Third-party research note, n.d.](document_2.txt)). The short answer to the query is that the study employs three language-specific speech corpora: the Spanish PC-GITA corpus, a German speech dataset, and a Czech speech dataset, each containing recordings from Parkinson's disease (PD) patients and healthy control (HC) speakers evaluated with the MDS-UPDRS-III clinical scale ([Vásquez-Correa et al., n.d.](document_1.txt); [Third-party research note, n.d.](document_2.txt)).

## 2. Overview of the Dataset Suite

Three datasets of speech recordings, corresponding to three different languages, are considered: Spanish, German, and Czech. All recordings were captured under noise-controlled conditions and the speech signals were down-sampled to 16 kHz ([Vásquez-Correa et al., n.d.](document_1.txt)). Every participant group in all three datasets was evaluated by a neurologist expert according to the third section of the Movement Disorder Society–sponsored revision of the Unified Parkinson's Disease Rating Scale (MDS-UPDRS-III) ([Vásquez-Correa et al., n.d.](document_1.txt)). The composition of the three datasets is summarized in Table 1.

**Table 1. Composition of the three speech datasets used in the study**

| Language | Corpus / dataset designation | PD participants | HC participants | Total participants | Native speaker group |
|---|---|---|---|---|---|
| Spanish | PC-GITA corpus | 50 | 50 | 100 | Colombian Spanish |
| German | German speech recordings (source cited as Skodda, Visser, & Schlegel) | 88 | 88 | 176 | German |
| Czech | Czech speech recordings (source cited as Rusz) | 50 | 50 | 100 | Czech |

*Note.* Figures are drawn from the study's data section ([Vásquez-Correa et al., n.d.](document_1.txt)) and are corroborated by the third-party note ([Third-party research note, n.d.](document_2.txt)).

Two observations follow directly from Table 1. First, each dataset is internally balanced between patients and controls at a 1:1 ratio, which is methodologically important because class imbalance can distort accuracy, sensitivity, and specificity estimates. Second, the German dataset is substantially larger than the Spanish and Czech datasets (176 versus 100 speakers each), a point that matters when comparing per-language classification results ([Vásquez-Correa et al., n.d.](document_1.txt)).

## 3. The Spanish Dataset: PC-GITA

### 3.1 Composition and Origin

The Spanish data are drawn from the PC-GITA corpus, which contains utterances from 50 PD patients and 50 HC speakers who are Colombian Spanish native speakers ([Vásquez-Correa et al., n.d.](document_1.txt)). The third-party note confirms that the Spanish portion of the cross-lingual data is exactly this corpus and repeats the same speaker counts of 50 PD patients and 50 healthy controls ([Third-party research note, n.d.](document_2.txt)). PC-GITA is a named, previously published corpus rather than a dataset newly collected for the present study, and it is referenced in the study's bibliography as a Spanish speech corpus database created for the analysis of people suffering from Parkinson's disease ([Vásquez-Correa et al., n.d.](document_1.txt)).

### 3.2 Speech Tasks

Participants in the Spanish dataset were asked to pronounce a total of 10 sentences, to perform rapid repetition of the syllables /pa-ta-ka/, /pe-ta-ka/, /pa-ka-ta/, /pa/, /ta/, and /ka/, to read one text containing 36 words, and to produce a monologue ([Vásquez-Correa et al., n.d.](document_1.txt)). This is the most task-diverse of the three protocols, since it combines connected speech (sentences, reading passage, monologue) with diadochokinetic syllable repetition at both single-syllable and three-syllable levels.

### 3.3 Medication Status

The study explicitly states that all Spanish patients were in the ON state at the time of the recording, that is, under the effect of their daily medication ([Vásquez-Correa et al., n.d.](document_1.txt)). This is a clinically consequential detail, because dopaminergic medication is known to influence speech motor performance and therefore the acoustic and time–frequency characteristics of the recorded utterances.

## 4. The German Dataset

The German dataset consists of speech recordings of 88 PD patients and 88 HC speakers from Germany ([Vásquez-Correa et al., n.d.](document_1.txt)). The third-party note independently restates these figures, describing the German data as containing 88 PD patients and 88 HC speakers ([Third-party research note, n.d.](document_2.txt)). Participants performed four speech tasks: the rapid repetition of /pa-ta-ka/, five sentences, one text with 81 words, and a monologue ([Vásquez-Correa et al., n.d.](document_1.txt)). The bibliographic entry associated with the German recordings in the study's reference list points to work on vowel articulation in Parkinson's disease published in the *Journal of Voice* ([Vásquez-Correa et al., n.d.](document_1.txt)).

Compared with the Spanish protocol, the German protocol contains a longer reading passage (81 words versus 36 words) but fewer sentences (five versus ten) and no single-syllable repetition tasks (/pa/, /ta/, /ka/) or the /pe-ta-ka/ and /pa-ka-ta/ variants ([Vásquez-Correa et al., n.d.](document_1.txt)). The extracted text does not state the medication state of the German participants.

## 5. The Czech Dataset

The Czech dataset contains a total of 100 native Czech speakers, comprising 50 PD patients and 50 healthy controls ([Vásquez-Correa et al., n.d.](document_1.txt)). As with the German data, the third-party note repeats the same counts of 50 PD patients and 50 HC ([Third-party research note, n.d.](document_2.txt)). The speech tasks performed by the Czech participants include the rapid repetition of the syllables /pa-ta-ka/, a read text with 80 words, and a monologue ([Vásquez-Correa et al., n.d.](document_1.txt)). This is the most compact protocol of the three, comprising only three tasks, and the extracted text does not list a fixed sentence set for the Czech cohort. The Czech recordings are associated in the bibliography with a habilitation thesis on detecting speech disorders in early Parkinson's disease by acoustic analysis, completed at the Czech Technical University in Prague ([Vásquez-Correa et al., n.d.](document_1.txt)).

## 6. Comparative Analysis of Dataset Composition and Task Design

Table 2 contrasts the speech tasks across the three datasets. The differences are substantive for cross-linguistic work because task type strongly influences which articulatory and phonatory phenomena are captured.

**Table 2. Speech tasks administered in each language dataset**

| Language | Rapid syllable repetition | Sentence reading | Read text | Monologue |
|---|---|---|---|---|
| Spanish | /pa-ta-ka/, /pe-ta-ka/, /pa-ka-ta/, /pa/, /ta/, /ka/ | 10 sentences | 36 words | Yes |
| German | /pa-ta-ka/ | 5 sentences | 81 words | Yes |
| Czech | /pa-ta-ka/ | Not specified in the extract | 80 words | Yes |

*Note.* Task descriptions are taken from the data section of the study ([Vásquez-Correa et al., n.d.](document_1.txt)).

The protocols overlap on the rapid /pa-ta-ka/ repetition task and on monologue production, which provides at least a minimal common anchor across languages. However, strict task-level equivalence is absent: the number of sentences, the length of the reading passage, and the inventory of syllable-repetition stimuli all differ ([Vásquez-Correa et al., n.d.](document_1.txt)).

## 7. Clinical Characterization and Speaker Demographics

The study reports that the average MDS-UPDRS-III score of the Spanish patients is higher than that of the German and Czech patients, meaning that the Spanish data include patients with greater disease severity ([Vásquez-Correa et al., n.d.](document_1.txt)). This is an important characteristic of the dataset suite because it creates a systematic difference in clinical severity across the three language cohorts, a difference the authors themselves invoke when interpreting their results. The extracted table of speaker information (Table 1 in the original study) appears to report mean MDS-UPDRS-III values in the region of approximately 37.8 (SD 22.1) for the Spanish patient group and approximately 22.1 (SD 9.9) and 21.4 (SD 11.5) for the other two patient groups, although the text-extraction process has scrambled the column alignment, so these pairings should be treated as approximate ([Vásquez-Correa et al., n.d.](document_1.txt)).

Regarding age, the extracted table lists the following male age ranges per group: Spanish PD 33–81 and Spanish HC 31–86; German PD 44–82 and German HC 26–83; Czech PD 43–82 and Czech HC 41–77 ([Vásquez-Correa et al., n.d.](document_1.txt)). A parallel set of female age ranges is also present in the extract (values such as 49–75, 49–76, 42–84, 28–85, 41–72, and 40–79), but the extraction does not allow these values to be reliably paired with their corresponding language and group ([Vásquez-Correa et al., n.d.](document_1.txt)). The table also includes sex distributions, mean ages with standard deviations, and time after diagnosis in years for the patient groups ([Vásquez-Correa et al., n.d.](document_1.txt)). Because the table layout was disrupted during text extraction, this report refrains from asserting specific values for those variables beyond the qualitative severity statement above. This is a limitation of the available source material rather than of the original study.

## 8. Recording Conditions, Segmentation, and Preprocessing

All recordings across the three datasets were captured in noise-controlled conditions and down-sampled to 16 kHz ([Vásquez-Correa et al., n.d.](document_1.txt)). Beyond the raw recordings, several derived representations of the same data are used. Speech signals are analyzed by automatically detecting onset and offset transitions, which model the difficulty patients have in starting and stopping vocal fold vibration; the border between voiced and unvoiced frames is detected, and 80 ms of signal are taken to the left and to the right, forming segments of 160 ms in length ([Vásquez-Correa et al., n.d.](document_1.txt)).

Two modelling streams operate on these transition segments. The baseline stream extracts 12 Mel-Frequency Cepstral Coefficients with their first and second derivatives plus the log energy of the signal distributed into 22 Bark bands, giving 58 descriptors; four statistical functionals (mean, standard deviation, skewness, and kurtosis) are then computed for each descriptor, yielding a 232-dimensional feature vector per utterance ([Vásquez-Correa et al., n.d.](document_1.txt)). Classification is performed with a radial basis function support vector machine with margin parameter C = 10 and a Gaussian kernel with γ = 0.0001, tested under a speaker-independent 10-fold cross-validation strategy ([Vásquez-Correa et al., n.d.](document_1.txt)). The second stream uses time–frequency representations based on the short-time Fourier transform with 256 frequency bins, computed with a 16 ms window and a 4 ms step size, producing 41 time frames per transition; the spectrogram is then transformed to the Mel scale using 80 filters, forming an 80 × 41 input that is used to train the convolutional neural networks (CNNs) ([Vásquez-Correa et al., n.d.](document_1.txt)). Thus, the same three recording datasets support multiple parallel representations and model families.

## 9. How the Datasets Are Used in the Study

The three datasets serve a two-stage experimental design. First, baseline models and CNNs are trained individually on each language. Then, a CNN trained on one language is used as a base model and fine-tuned with utterances from a target language, implementing a cross-lingual transfer learning strategy ([Vásquez-Correa et al., n.d.](document_1.txt)). All speech exercises performed by participants were considered for classification, and the final decision for each speaker was obtained by a majority voting strategy across the different speech exercises ([Vásquez-Correa et al., n.d.](document_1.txt)).

The reported outcomes indicate that the largest gains arise when Spanish is the base language. Accuracy improved by over 8% for German, from 69.3% in the baseline to 77.3% when the model was fine-tuned from Spanish, and by over 4.1% for Czech, from 68.5% with the initial CNN to 72.6% when fine-tuned from Spanish ([Vásquez-Correa et al., n.d.](document_1.txt)). The authors attribute this to Spanish speakers having the best initial separability, so that the other two languages benefit from the best initial model ([Vásquez-Correa et al., n.d.](document_1.txt)). In terms of area under the ROC curve, the highest AUC for the German and Czech target languages is obtained when the base model is trained with Spanish utterances, while the AUC for a Spanish target is slightly higher when the base language is Czech ([Vásquez-Correa et al., n.d.](document_1.txt)). Results after transfer learning were also more balanced in specificity and sensitivity and showed lower variance than models trained without transfer learning ([Vásquez-Correa et al., n.d.](document_1.txt)).

These datasets had also been used in earlier work cited by the study. For instance, accuracies of up to 77% were reported on PC-GITA utterances, up to 81% for Spanish data and up to 94% for Czech data in a forced-alignment Gaussian mixture model study, and 70% to 89% depending on language for an earlier CNN articulation model; in a language-independent scenario, however, accuracy dropped below 60% ([Vásquez-Correa et al., n.d.](document_1.txt)). This historical context explains why the present study builds its transfer learning strategy specifically on these three corpora.

## 10. Critical Appraisal

The dataset suite has clear strengths. It covers three typologically and geographically distinct languages, is internally balanced between patients and controls in each language, includes expert neurologist evaluation with a standardized clinical instrument (MDS-UPDRS-III), and was recorded under controlled noise conditions with consistent 16 kHz sampling ([Vásquez-Correa et al., n.d.](document_1.txt)). It therefore supports investigation of a question that single-language corpora cannot address, namely whether speech-based PD classification transfers across languages.

Several limitations should nonetheless be acknowledged. First, the cohorts are unequal in size: 176 German speakers versus 100 Spanish and 100 Czech speakers ([Vásquez-Correa et al., n.d.](document_1.txt)). Second, the speech protocols are not parallel: the number of sentences, the length of the read text, and the inventory of syllable repetitions differ across languages ([Vásquez-Correa et al., n.d.](document_1.txt)). Third, clinical severity is not matched across languages, with the Spanish patients showing higher average MDS-UPDRS-III scores ([Vásquez-Correa et al., n.d.](document_1.txt)). Fourth, medication state is documented only for the Spanish cohort, which was recorded in the ON state ([Vásquez-Correa et al., n.d.](document_1.txt)). Fifth, the study itself notes that Czech and German are phonologically richer than Spanish in terms of consonant production, which may make consonant sounds easier for Czech PD patients to produce than for Spanish PD patients, introducing a language-dependent effect into the data ([Vásquez-Correa et al., n.d.](document_1.txt)). Finally, the source material available here is a text-extracted rendering of the paper in which tables are partially scrambled, so a number of demographic figures cannot be verified with confidence; the third-party note agrees with the primary document on speaker counts, but because it explicitly restates the same study, its agreement does not constitute independent verification ([Third-party research note, n.d.](document_2.txt)).

## 11. Conclusion

The study uses three datasets, one per language: the PC-GITA corpus for Spanish (50 PD, 50 HC; Colombian Spanish natives), a German speech dataset (88 PD, 88 HC), and a Czech speech dataset (50 PD, 50 HC). All three comprise PD patients and healthy controls, were captured in noise-controlled conditions and down-sampled to 16 kHz, and were evaluated clinically with the MDS-UPDRS-III. The Spanish cohort is characterized by higher average disease severity and was recorded while patients were in the ON medication state. The three datasets share the /pa-ta-ka/ repetition and monologue tasks but differ in sentence counts and reading passage lengths, and they differ substantially in total size. This combination of shared structure and cross-language heterogeneity is precisely what makes the corpus suite suitable for the study's transfer learning experiments, while also constraining how directly the per-language results can be compared.

## References

Third-party research note: Convolutional neural networks and a transfer learning strategy to classify Parkinson's disease from speech in three different languages (n.d.) [document_2.txt]. Retrieved September 15, 2026, from [document_2.txt](document_2.txt)

Vásquez-Correa, J. C., Arias-Vergara, T., Rios-Urrego, C. D., Schuster, M., Rusz, J., Orozco-Arroyave, J. R., & Nöth, E. (n.d.). *Convolutional neural networks and a transfer learning strategy to classify Parkinson's disease from speech in three different languages* [document_1.txt]. Retrieved September 15, 2026, from [document_1.txt](document_1.txt)