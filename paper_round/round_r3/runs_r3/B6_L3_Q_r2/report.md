# Datasets Used in the Study of Parkinson's Disease Classification from Speech in Three Languages

## 1. Purpose and Scope of This Report

This report identifies, describes, and assesses the datasets employed in the research paper "Convolutional Neural Networks and a Transfer Learning Strategy to Classify Parkinson's Disease from Speech in Three Different Languages," which proposes a convolutional neural network (CNN) pipeline trained on time–frequency representations of speech, combined with a cross-lingual transfer learning strategy, to discriminate between Parkinson's disease (PD) patients and healthy control (HC) speakers ([Vásquez-Correa et al., n.d., document_1.txt](document_1.txt)). The report catalogues the corpora, speaker populations, speech tasks, recording conditions, clinical annotations, and the manner in which each dataset was partitioned for model training and evaluation. It also documents an important discrepancy between the primary source and a secondary research note regarding the identity of one of the three language datasets.

## 2. Evidentiary Basis and a Critical Note on Source Discrepancy

Two documents were supplied. The first, `document_1.txt`, is the full text of the primary research article, including its abstract, methods, results tables, and reference list ([Vásquez-Correa et al., n.d., document_1.txt](document_1.txt)). The second, `document_2.txt`, is a third-party research note summarising the same study ([Third-party research note, n.d., document_2.txt](document_2.txt)).

The two sources disagree on the language of one of the three datasets. The primary article states unambiguously that the study covers **Spanish, German, and Czech** speech, and it reports that "speech recordings of 88 PD patients and 88 HC speakers from Germany are considered" ([Vásquez-Correa et al., n.d., document_1.txt](document_1.txt)). The secondary note instead describes the dataset as **Italian**: "The Italian dataset contains speech recordings of 88 PD patients and 88 HC speakers from Italy" ([Third-party research note, n.d., document_2.txt](document_2.txt)). Because the speaker counts (88 PD / 88 HC) are identical in both accounts, the most defensible interpretation is that both sources refer to the same cohort, with the secondary note applying an incorrect language label. In this report, the primary source is treated as authoritative, and the discrepancy is flagged wherever relevant. This is consistent with standard practice of prioritising primary literature over secondary summaries.

## 3. Overview of the Datasets

The study draws on three language-specific speech corpora, each containing parallel groups of PD patients and healthy control speakers. All recordings were captured under noise-controlled conditions, and all speech signals were down-sampled to 16 kHz ([Vásquez-Correa et al., n.d., document_1.txt](document_1.txt)). All participants were assessed by an expert neurologist using the third section of the Movement Disorder Society–sponsored Unified Parkinson's Disease Rating Scale (MDS-UPDRS-III) ([Vásquez-Correa et al., n.d., document_1.txt](document_1.txt)).

The headline composition of the three datasets, totalling 188 PD patients and 188 healthy control speakers (376 speakers overall), is summarised below.

| Dataset / Language | Named corpus | PD speakers | HC speakers | Total speakers | Native population |
|---|---|---|---|---|---|
| Spanish | PC-GITA | 50 | 50 | 100 | Colombian Spanish speakers |
| German | Not named (cf. [18]) | 88 | 88 | 176 | German speakers |
| Czech | Not named (cf. [19]) | 50 | 50 | 100 | Native Czech speakers |

Sources: ([Vásquez-Correa et al., n.d., document_1.txt](document_1.txt); [Third-party research note, n.d., document_2.txt](document_2.txt)).

### 3.1 Spanish Dataset (PC-GITA)

The Spanish portion of the data is drawn from the PC-GITA corpus, described in the article as a resource containing utterances from 50 PD patients and 50 HC subjects who are Colombian Spanish native speakers ([Vásquez-Correa et al., n.d., document_1.txt](document_1.txt)). PC-GITA is explicitly named and cited as reference [6] in the original publication, making it the only one of the three datasets with an identifiable corpus name in the supplied material.

Participants were asked to produce a structured battery of speech tasks: a total of 10 sentences; rapid repetition of the syllable sequences /pa-ta-ka/, /pe-ta-ka/, /pa-ka-ta/; sustained/repeated phonation of /pa/, /ta/, and /ka/; one read text containing 36 words; and a monologue ([Vásquez-Correa et al., n.d., document_1.txt](document_1.txt)). Critically for the interpretation of results, **all Spanish patients were recorded in the ON state**, i.e., under the effect of their daily medication at the time of recording ([Vásquez-Correa et al., n.d., document_1.txt](document_1.txt)).

The secondary note corroborates the PC-GITA composition, stating that it "contains utterances from 50 PD patients and 50 HC, Colombian Spanish native speakers" and that this corpus "provides the Spanish portion of the cross-lingual speech data" ([Third-party research note, n.d., document_2.txt](document_2.txt)).

### 3.2 German Dataset

The primary article reports that speech recordings of 88 PD patients and 88 HC speakers from Germany were used, with the source attributed to reference [18] ([Vásquez-Correa et al., n.d., document_1.txt](document_1.txt)). This is the largest of the three datasets by speaker count, contributing 176 of the 376 total speakers.

The German participants performed four speech tasks: the rapid repetition of /pa-ta-ka/, five sentences, one text containing 81 words, and a monologue ([Vásquez-Correa et al., n.d., document_1.txt](document_1.txt)). The task battery is therefore similar in structure to the Spanish battery—combining a diadochokinetic (DDK) articulation task, connected read speech, and spontaneous speech—but differs in the number of sentences (five versus ten) and in the length of the read text (81 words versus 36 words).

### 3.3 Czech Dataset

A total of 100 native Czech speakers, comprising 50 PD patients and 50 healthy controls, were considered, with the source attributed to reference [19] ([Vásquez-Correa et al., n.d., document_1.txt](document_1.txt)). The Czech participants performed the rapid repetition of the syllables /pa-ta-ka/, a read text with 80 words, and a monologue ([Vásquez-Correa et al., n.d., document_1.txt](document_1.txt)). The Czech battery is thus slightly narrower than the Spanish and German batteries, in that it does not include a set of read sentences separate from the longer text.

### 3.4 The "Italian" Label in the Secondary Source

The third-party note states that "the Italian dataset contains speech recordings of 88 PD patients and 88 HC speakers from Italy" and refers consistently thereafter to "Spanish, Italian, and Czech" datasets ([Third-party research note, n.d., document_2.txt](document_2.txt)). As noted in Section 2, this conflicts with the primary article, which describes the same 88/88 cohort as German and locates it in Germany ([Vásquez-Correa et al., n.d., document_1.txt](document_1.txt)). In addition, the primary article's discussion of language-dependent articulatory effects contrasts Czech and German with Spanish—for example, noting that Czech and German are "richer than Spanish language in terms of consonant production"—a comparison that is internally consistent only with a German (not Italian) dataset ([Vásquez-Correa et al., n.d., document_1.txt](document_1.txt)). The weight of evidence therefore favours the primary source.

## 4. Speaker and Clinical Characteristics

The article reports a demographic and clinical characterisation table (Table 1) covering gender distribution, age ranges, mean age with standard deviation, MDS-UPDRS-III scores, and time since diagnosis in years ([Vásquez-Correa et al., n.d., document_1.txt](document_1.txt)). Because the supplied text is an OCR rendering in which the table's structure is partially interleaved with running text, several values cannot be reconstructed with full confidence; the report distinguishes below between values that are clearly recoverable and those that are approximate.

**Age ranges (clearly recoverable).** Patients with PD ranged in age from 33 to 81 years (Spanish), 44 to 82 years (German), and 43 to 82 years (Czech). Healthy controls ranged from 31 to 86 years (Spanish), 26 to 83 years (German), and 41 to 77 years (Czech) ([Vásquez-Correa et al., n.d., document_1.txt](document_1.txt)).

**Disease severity.** The article states that the average MDS-UPDRS-III score for Spanish patients is higher than for the German and Czech patients, meaning that "there are patients with higher disease severity in the Spanish data compared to German and Czech patients" ([Vásquez-Correa et al., n.d., document_1.txt](document_1.txt)). The approximate mean (standard deviation) values visible in the OCR rendering are 37.8 (22.1) for the Spanish patients, 22.1 (9.9) for the German patients, and 21.4 (11.5) for the Czech patients; these figures should be treated as indicative rather than definitive because of the rendering issues noted above ([Vásquez-Correa et al., n.d., document_1.txt](document_1.txt)).

**Gender and age distribution.** The table also reports gender-split age ranges and counts per language group, together with mean ages and time after diagnosis, but the OCR interleaving of these rows prevents reliable reconstruction of every figure ([Vásquez-Correa et al., n.d., document_1.txt](document_1.txt)). This constitutes a genuine limitation of the supplied evidence base rather than of the underlying study, and any downstream reuse of the demographic figures should verify them against the original published table.

## 5. Recording Conditions, Segmentation, and Derived Representations

All recordings were captured in noise-controlled conditions and down-sampled to 16 kHz ([Vásquez-Correa et al., n.d., document_1.txt](document_1.txt)). The analytical pipeline does not use the raw recordings directly. Instead, speech signals are processed through automatic detection of onset and offset transitions between voiced and unvoiced segments, based on the presence of the fundamental frequency in short-time frames; the border between voiced and unvoiced frames is detected and 80 ms of signal is taken to the left and right, forming segments of 160 ms ([Vásquez-Correa et al., n.d., document_1.txt](document_1.txt)). This segmentation strategy is designed to model patients' difficulties in starting and stopping vocal fold vibration.

From these 160 ms segments, two alternative input representations are derived:

- **Baseline hand-crafted features.** Twelve Mel-Frequency Cepstral Coefficients (MFCCs) with first and second derivatives, plus the log energy of the signal distributed across 22 Bark bands, yielding 58 descriptors. Four statistical functionals (mean, standard deviation, skewness, kurtosis) are computed per descriptor, producing a 232-dimensional feature vector per utterance ([Vásquez-Correa et al., n.d., document_1.txt](document_1.txt)).
- **Time–frequency representations.** A short-time Fourier transform with 256 frequency bins, a 16 ms window, and a 4 ms step size, producing 41 time frames per transition; the spectrogram is then converted to the Mel scale with 80 filters, yielding an 80 × 41 image that is used as CNN input ([Vásquez-Correa et al., n.d., document_1.txt](document_1.txt)).

It is important to note that the datasets as analysed are therefore **derived feature sets and spectrogram images**, not merely raw audio corpora.

## 6. How the Datasets Were Used

The baseline model classifies the 232-dimensional feature vectors with a radial basis function support vector machine (margin parameter C = 10, Gaussian kernel with γ = 0.0001), evaluated under a speaker-independent 10-fold cross-validation strategy ([Vásquez-Correa et al., n.d., document_1.txt](document_1.txt)).

The CNN model consists of four convolutional and max-pooling layers with dropout regularisation, followed by two fully connected layers and a softmax output layer, trained with cross-entropy loss and the Adam optimiser ([Vásquez-Correa et al., n.d., document_1.txt](document_1.txt)). The number of feature maps in each convolutional layer is twice that of the preceding layer ([Vásquez-Correa et al., n.d., document_1.txt](document_1.txt)).

The transfer learning design uses one language as the base for pre-training and the remaining languages as targets for fine-tuning ([Vásquez-Correa et al., n.d., document_1.txt](document_1.txt)). All speech exercises performed by participants were used, and the final decision per speaker was obtained by a majority voting strategy across the different speech exercises ([Vásquez-Correa et al., n.d., document_1.txt](document_1.txt)).

Key reported outcomes relevant to dataset utility include:

- Spanish yielded the highest accuracy among the three languages when trained individually, and the Spanish dataset showed similar performance between the baseline and CNN models ([Vásquez-Correa et al., n.d., document_1.txt](document_1.txt)).
- German achieved its highest accuracy with the baseline model, whereas Czech achieved its highest with the CNN ([Vásquez-Correa et al., n.d., document_1.txt](document_1.txt)).
- Accuracy improved by over 8% for German (from 69.3% baseline to 77.3% when fine-tuned from Spanish) and by over 4.1% for Czech (from 68.5% with the initial CNN to 72.6% when fine-tuned from Spanish) ([Vásquez-Correa et al., n.d., document_1.txt](document_1.txt)).
- In a language-independent scenario—training on one language and testing on the others—accuracy fell below 60%, indicating substantial cross-lingual domain shift ([Vásquez-Correa et al., n.d., document_1.txt](document_1.txt)).

## 7. Assessment of Suitability, Strengths, and Limitations

**Strengths.** Each dataset is class-balanced at a 1:1 ratio of PD patients to healthy controls, which simplifies classifier training and interpretation of sensitivity and specificity. Diagnosis and severity were established by an expert neurologist using a standardised clinical instrument, MDS-UPDRS-III ([Vásquez-Correa et al., n.d., document_1.txt](document_1.txt)). Recording conditions were noise-controlled and sampling rates harmonised at 16 kHz ([Vásquez-Correa et al., n.d., document_1.txt](document_1.txt)). The multilingual design covering three distinct language families and speaker populations supports the study's central research question about cross-lingual transfer ([Vásquez-Correa et al., n.d., document_1.txt](document_1.txt)). Multiple speech tasks—DDK syllable repetition, sustained phonemes, read sentences, a longer read text, and monologue—allow complementary analyses of articulation, phonation, and prosody ([Vásquez-Correa et al., n.d., document_1.txt](document_1.txt)).

**Limitations.** Sample sizes are moderate, ranging from 100 to 176 speakers per language, and the three datasets are not matched in size ([Vásquez-Correa et al., n.d., document_1.txt](document_1.txt)). Disease severity differs across languages, with the Spanish cohort presenting higher average MDS-UPDRS-III scores, which the authors themselves invoke to explain cross-language performance differences ([Vásquez-Correa et al., n.d., document_1.txt](document_1.txt)). Medication state is reported explicitly only for the Spanish cohort, all of whom were in the ON state, with no equivalent statement provided for the German and Czech groups in the supplied text ([Vásquez-Correa et al., n.d., document_1.txt](document_1.txt)). Two of the three datasets are referenced only by citation number ([18] and [19]) rather than by name, limiting transparency and reproducibility from the supplied materials alone ([Vásquez-Correa et al., n.d., document_1.txt](document_1.txt)). Finally, the secondary source's mislabelling of the German dataset as Italian introduces a documentation risk that any literature review relying on that note would propagate ([Third-party research note, n.d., document_2.txt](document_2.txt)).

## 8. Conclusion

The study employs three language-specific speech datasets: the PC-GITA corpus of Colombian Spanish (50 PD, 50 HC), a German corpus (88 PD, 88 HC from Germany), and a Czech corpus (50 PD, 50 HC native Czech speakers), together comprising 188 patients and 188 healthy controls ([Vásquez-Correa et al., n.d., document_1.txt](document_1.txt)). Each dataset supplies multiple speech tasks captured in noise-controlled conditions, down-sampled to 16 kHz, clinically annotated with MDS-UPDRS-III, and processed into either 232-dimensional hand-crafted feature vectors or 80 × 41 Mel spectrograms for CNN input ([Vásquez-Correa et al., n.d., document_1.txt](document_1.txt)). The datasets are well suited to the study's cross-lingual transfer learning objective, being balanced and clinically validated, but they differ in size and in disease severity, and one of the three is inconsistently labelled across sources. Users of these data should therefore treat the primary article as the authoritative record and verify demographic and clinical table values against the original publication.

## References

Third-party research note: Convolutional neural networks and a transfer learning strategy to classify Parkinson's disease from speech in three different languages [document_2.txt]. (n.d.).

Vásquez-Correa, J. C., Arias-Vergara, T., Rios-Urrego, C. D., Schuster, M., Rusz, J., Orozco-Arroyave, J. R., & Nöth, E. (n.d.). *Convolutional neural networks and a transfer learning strategy to classify Parkinson's disease from speech in three different languages* [document_1.txt].