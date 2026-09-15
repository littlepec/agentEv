# Datasets Used in *Convolutional Neural Networks and a Transfer Learning Strategy to Classify Parkinson's Disease from Speech in Three Different Languages*

## 1. Purpose and Scope of This Report

This report documents, in structured detail, the datasets employed by Vásquez-Correa et al. in their study on convolutional neural networks (CNNs) and cross-lingual transfer learning for the classification of Parkinson's disease (PD) from speech ([Vásquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)). The question of "what datasets are used" is central to interpreting the study, because the paper's core contribution — demonstrating that a base CNN trained in one language can be fine-tuned to improve classification accuracy in another language — rests entirely on the availability of three parallel, clinically annotated, multilingual speech corpora. The report describes each dataset's provenance, speaker composition, demographic and clinical profile, speech tasks, recording conditions, and the way each corpus is partitioned into the modelling pipeline. It also identifies a numerical inconsistency between the primary source and the accompanying third-party research note, and explains which figure should be treated as authoritative ([Vásquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374); [Third-party research note, n.d.](document_2.txt)).

## 2. Overview of the Data Portfolio

The study draws on speech recordings of PD patients and healthy control (HC) speakers in three languages: Spanish, German, and Czech ([Vásquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)). All recordings were captured under noise-controlled conditions, and all speech signals were down-sampled to 16 kHz, which standardises the input representation across the three corpora and permits a common signal-processing and neural-network front end ([Vásquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)). Every participant in the three datasets was evaluated by an expert neurologist using the third section of the Movement Disorder Society–sponsored revision of the Unified Parkinson's Disease Rating Scale (MDS-UPDRS-III), which provides the clinical ground truth that anchors the machine-learning labels ([Vásquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)).

The three corpora therefore serve a dual purpose: they supply the binary labels (PD versus HC) needed for supervised classification, and they supply the cross-language variability (phonetic, prosodic, and clinical) that the transfer-learning experiment is designed to exploit ([Vásquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)).

## 3. The Spanish Dataset: PC-GITA

### 3.1 Provenance

The Spanish portion of the data is the PC-GITA corpus, originally introduced by Orozco-Arroyave and colleagues in 2014 as a Spanish speech database for the analysis of people suffering from Parkinson's disease ([Vásquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)). It is the only one of the three corpora that is explicitly named in the paper.

### 3.2 Speaker Composition

PC-GITA contains utterances from 50 PD patients and 50 HC speakers, all Colombian Spanish native speakers ([Vásquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)). The dataset is perfectly gender-balanced, with 25 male and 25 female speakers in each of the PD and HC groups ([Vásquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)). Ages for the PD group average 61.3 years (SD = 11.4, range 33–81) for men and 60.7 years (SD = 7.3, range 49–75) for women; the corresponding HC averages are 60.5 years (SD = 11.6, range 31–86) for men and 61.4 years (SD = 7.0, range 49–76) for women ([Vásquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)).

### 3.3 Clinical Profile

Time since diagnosis averaged 8.7 years (SD = 5.9) for male patients and 12.6 years (SD = 11.6) for female patients ([Vásquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)). Mean MDS-UPDRS-III scores were 37.8 (SD = 22.1) for men and 37.6 (SD = 14.1) for women ([Vásquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)). These values are markedly higher than those reported for the German and Czech cohorts, meaning the Spanish sample contains patients with greater disease severity on average ([Vásquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)). All Spanish patients were recorded in the ON state, i.e., under the effect of their daily medication ([Vásquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)).

### 3.4 Speech Tasks

Participants pronounced a total of ten sentences, performed rapid repetition of the syllable sequences /pa-ta-ka/, /pe-ta-ka/, /pa-ka-ta/, /pa/, /ta/, and /ka/, read one text of 36 words, and produced a monologue ([Vásquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)). This is the most extensive task battery of the three datasets.

## 4. The German Dataset

### 4.1 Provenance and Composition

The German data comprise speech recordings of 88 PD patients and 88 HC speakers from Germany, sourced from the work of Skodda, Visser, and Schlegel (2011, as cited in [Vásquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)). Gender composition is less balanced than in the Spanish corpus: the PD group contains 47 men and 41 women, while the HC group contains 44 men and 44 women ([Vásquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)). Mean ages for male PD patients were 66.7 years (SD = 8.7, range 44–82) and for female PD patients 66.2 years (SD = 9.7, range 42–84); HC averages were 63.8 years (SD = 12.7, range 26–83) for men and 62.6 years (SD = 15.2, range 28–85) for women ([Vásquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)).

### 4.2 Clinical Profile and Tasks

Time since diagnosis averaged 7.0 years (SD = 5.5) for men and 7.1 years (SD = 6.2) for women, with mean MDS-UPDRS-III scores of 22.1 (SD = 9.9) and 23.3 (SD = 12.0) respectively — substantially lower than the Spanish cohort, indicating milder average disease severity ([Vásquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)). The German participants completed four speech tasks: rapid repetition of /pa-ta-ka/, five sentences, a read text of 81 words, and a monologue ([Vásquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)).

## 5. The Czech Dataset

The Czech data consist of a total of 100 native Czech speakers, comprising 50 PD patients and 50 HC speakers ([Vásquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)). The corpus derives from the habilitation work of Rusz (2018, as cited in [Vásquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)). Gender composition is 30 men and 20 women in the PD group and 30 men and 20 women in the HC group ([Vásquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)). Mean ages were 65.3 years (SD = 9.6, range 43–82) for male patients, 60.1 years (SD = 8.7, range 41–72) for female patients, 60.3 years (SD = 11.5, range 41–77) for male controls, and 63.5 years (SD = 11.1, range 40–79) for female controls ([Vásquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)). Disease duration was 6.7 years (SD = 4.5) for men and 6.8 years (SD = 5.2) for women, with MDS-UPDRS-III means of 21.4 (SD = 11.5) and 18.1 (SD = 9.7) respectively — the lowest severity burden of the three cohorts ([Vásquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)). The speech tasks were rapid repetition of /pa-ta-ka/, a read text of 80 words, and a monologue ([Vásquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)).

## 6. Comparative Summary of the Three Datasets

| Characteristic | Spanish (PC-GITA) | German | Czech |
|---|---|---|---|
| PD / HC speakers | 50 / 50 | 88 / 88 | 50 / 50 |
| PD gender split (M/F) | 25 / 25 | 47 / 41 | 30 / 20 |
| HC gender split (M/F) | 25 / 25 | 44 / 44 | 30 / 20 |
| Mean MDS-UPDRS-III (M / F) | 37.8 / 37.6 | 22.1 / 23.3 | 21.4 / 18.1 |
| Mean disease duration (M / F, years) | 8.7 / 12.6 | 7.0 / 7.1 | 6.7 / 6.8 |
| Speech tasks | 10 sentences, /pa-ta-ka/, /pe-ta-ka/, /pa-ka-ta/, /pa/, /ta/, /ka/, 36-word text, monologue | /pa-ta-ka/, 5 sentences, 81-word text, monologue | /pa-ta-ka/, 80-word text, monologue |
| Originating source | Orozco-Arroyave et al. (2014) | Skodda et al. (2011) | Rusz (2018) |

*Table compiled from figures reported in* ([Vásquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)).

## 7. How the Datasets Are Transformed for Modelling

The corpora are not fed to the classifiers as raw recordings. Instead, the authors automatically detect onset and offset transitions between voiced and unvoiced frames — a choice motivated by the difficulty PD patients experience in starting and stopping vocal-fold vibration ([Vásquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)). Around each detected border, 80 ms of signal are taken to the left and to the right, producing 160-ms transition segments ([Vásquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)). Two representations are then derived from these segments: (a) a baseline set of 12 MFCCs with first and second derivatives plus log energy distributed over 22 Bark bands, yielding 58 descriptors that become a 232-dimensional feature vector per utterance after four statistical functionals are applied; and (b) a Mel-scale spectrogram of size 80 × 41 computed via STFT with 256 frequency bins, a 16-ms window, a 4-ms step, and 80 Mel filters ([Vásquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)). The final decision for each speaker is reached by majority voting across the different speech exercises ([Vásquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)).

## 8. Datasets Referenced but Not Used

The introduction of the paper discusses several additional speech corpora that inform the literature review but do not form part of the analysed data. These include a Turkish dataset of 20 PD patients and 20 HC speakers used with KNN and SVM classifiers ([Vásquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)), a Czech dataset of 24 native speakers used to study rapid syllable repetition ([Vásquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)), and the PC-GITA corpus again in the context of articulation modelling with Gaussian mixture models ([Vásquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)). Distinguishing these from the three corpora actually analysed is important for anyone attempting to reproduce the study.

## 9. Data Reliability, Consistency and Limitations

The primary and secondary sources agree on the Spanish and Czech datasets: 50 PD plus 50 HC speakers in each ([Vásquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374); [Third-party research note, n.d.](document_2.txt)). They diverge, however, on the German dataset. The primary paper states that recordings of 88 PD patients and 88 HC speakers are used ([Vásquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)), and its Table 1 enumerates 47 male and 41 female PD patients, summing to 88. The third-party research note states that the German data consist of "44 PD patients and 44 HC speakers" ([Third-party research note, n.d.](document_2.txt)). Because the primary source's tabulated gender breakdown is internally consistent with the total of 88, the most defensible interpretation is that the third-party note misreported the figure — plausibly transposing the 44 male HC speakers into the total PD count. Researchers should therefore treat 88 PD and 88 HC as the authoritative German sample size ([Vásquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)).

Three further limitations are evident in the data design. First, the Spanish patients were recorded in the ON state, which means their speech reflects the partial alleviation of symptoms by medication and may not generalise to unmedicated (OFF-state) recordings ([Vásquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)). Second, severity is not matched across languages: mean MDS-UPDRS-III is roughly 37–38 in the Spanish cohort versus 18–23 in the German and Czech cohorts, so cross-language models are also, implicitly, cross-severity models ([Vásquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)). Third, the German cohort is not gender-balanced in the PD group, whereas the Spanish and Czech cohorts are ([Vásquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)). These asymmetries explain why the authors attribute the comparatively strong Spanish results to higher initial separability of the Spanish sample and why they caution against bias from language-specific linguistic content ([Vásquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)).

## 10. Role of the Datasets in the Experimental Results

The three corpora are used in two experimental configurations. In the individual setting, baseline and CNN models achieve 73.7% and 71.0% accuracy for Spanish, 69.3% and 63.1% for German, and 61.0% and 68.5% for Czech ([Vásquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)). In the transfer-learning setting, a CNN pre-trained on one language is fine-tuned on another; the highest accuracy for German (77.3%) and Czech (76.7%) arises when Spanish is the base language, while transfer into Spanish reaches 72.6% from a Czech base and 70.0% from a German base ([Vásquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)). These outcomes reinforce the conclusion that dataset quality and the robustness of the base model, not merely data volume, determine whether cross-lingual transfer succeeds ([Vásquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)).

## 11. Typical Applications of These Datasets

The PC-GITA, German, and Czech corpora are suited to several applications beyond the immediate study: computer-aided diagnosis that separates PD patients from healthy controls; cross-lingual or language-independent speech-based screening; prediction of disease progression against the MDS-UPDRS-III scale or dysarthria severity ratings; and, as the authors foreshadow, transfer learning across neurological diseases such as Huntington's disease ([Vásquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)). The availability of matched healthy controls, neurologist-confirmed diagnoses, and a common 16 kHz sampling format makes the three corpora jointly usable for multilingual benchmarking ([Vásquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)).

## 12. Conclusion

The study uses exactly three datasets: the Spanish PC-GITA corpus (50 PD, 50 HC Colombian Spanish speakers), a German speech dataset (88 PD, 88 HC speakers), and a Czech dataset (50 PD, 50 HC native speakers), all recorded under noise-controlled conditions at 16 kHz and clinically annotated with MDS-UPDRS-III scores ([Vásquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)). Each corpus contributes a distinct speech-task battery, a distinct severity profile, and a distinct linguistic background, and together they enable the paper's central claim that transfer learning from a robust base language can raise classification accuracy in a target language by up to 8% ([Vásquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374)). Where the secondary research note diverges from the primary source on the German sample size, the primary source's internally consistent figures of 88 PD and 88 HC speakers should be preferred ([Vásquez-Correa et al., 2020](https://arxiv.org/abs/2002.04374); [Third-party research note, n.d.](document_2.txt)).

## References

Vásquez-Correa, J. C., Arias-Vergara, T., Rios-Urrego, C. D., Schuster, M., Rusz, J., Orozco-Arroyave, J. R., & Nöth, E. (2020). *Convolutional neural networks and a transfer learning strategy to classify Parkinson's disease from speech in three different languages* [document_1.txt]. arXiv. https://arxiv.org/abs/2002.04374

Third-party research note: Convolutional neural networks and a transfer learning strategy to classify Parkinson's disease from speech in three different languages [document_2.txt]. (n.d.).