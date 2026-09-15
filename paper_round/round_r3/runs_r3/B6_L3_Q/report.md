# Datasets Used in the Cross-Lingual Parkinson's Disease Speech Classification Study

## Introduction and Scope of the Report

This report identifies, characterizes, and evaluates the datasets used in the study *Convolutional Neural Networks and a Transfer Learning Strategy to Classify Parkinson's Disease from Speech in Three Different Languages*. The analysis draws on two supplied documents: the primary study text itself ([Vásquez-Correa et al., n.d.](document_1.txt)) and a third-party research note summarizing the same study ([Third-party research note, n.d.](document_2.txt)). Because the two documents disagree on one of the three languages involved, a substantial part of this report is devoted to source-reliability assessment, since dataset provenance directly determines whether downstream findings can be trusted.

The study's central methodological premise is that Parkinson's disease (PD) speech classification can be improved across languages through transfer learning: a convolutional neural network (CNN) is pre-trained on utterances from one language (the "base" language) and then fine-tuned on utterances from another (the "target" language) ([Vásquez-Correa et al., n.d.](document_1.txt)). The datasets therefore serve a dual purpose: they constitute the clinical evidence base for the study and they define the cross-lingual experimental grid.

## The Three Clinical Speech Datasets

The study considers speech recordings of patients and healthy control (HC) speakers in three languages: Spanish, German, and Czech ([Vásquez-Correa et al., n.d.](document_1.txt)). All recordings were captured under noise-controlled conditions and the speech signals were down-sampled to 16 kHz. Every patient in all three datasets was evaluated by an expert neurologist according to the third section of the Movement Disorder Society–sponsored revision of the Unified Parkinson's Disease Rating Scale (MDS-UPDRS-III) ([Vásquez-Correa et al., n.d.](document_1.txt)).

### Spanish Dataset: The PC-GITA Corpus

The Spanish data come from the PC-GITA corpus, introduced by Orozco-Arroyave et al. ([Vásquez-Correa et al., n.d.](document_1.txt)). PC-GITA contains utterances from 50 PD patients and 50 HC speakers, all native Colombian Spanish speakers, giving a Spanish subset of 100 speakers. Participants were asked to pronounce a total of 10 sentences, to perform rapid repetition of the syllables /pa-ta-ka/, /pe-ta-ka/, /pa-ka-ta/, /pa/, /ta/, and /ka/, to read one text containing 36 words, and to produce a monologue. All Spanish patients were recorded in the ON state, i.e., under the effect of their daily medication ([Vásquez-Correa et al., n.d.](document_1.txt)).

The PC-GITA corpus also appears earlier in the study's literature review as a benchmark: a Gaussian mixture model (GMM)/SVM study on PC-GITA utterances reported accuracies of up to 77%, and a later forced-alignment study reported up to 81% accuracy on Spanish PC-GITA data and up to 94% on Czech data ([Vásquez-Correa et al., n.d.](document_1.txt)). This is relevant because it shows PC-GITA is a reused, semi-public resource with prior baselines, rather than a corpus collected exclusively for this paper.

### German Dataset

The German portion consists of speech recordings of 88 PD patients and 88 HC speakers from Germany, attributed to the study by Skodda, Visser, and Schlegel published in the *Journal of Voice* ([Vásquez-Correa et al., n.d.](document_1.txt)). Participants performed four speech tasks: the rapid repetition of /pa-ta-ka/, five sentences, one text with 81 words, and a monologue. With 176 speakers in total, the German dataset is the largest of the three by speaker count.

### Czech Dataset

The Czech subset comprises 100 native Czech speakers, specifically 50 PD patients and 50 HC speakers, drawn from work by Rusz ([Vásquez-Correa et al., n.d.](document_1.txt)). The speech tasks include rapid repetition of the syllables /pa-ta-ka/, a read text with 80 words, and a monologue. The Czech material is also connected to earlier acoustic-analysis work on early Parkinson's disease ([Vásquez-Correa et al., n.d.](document_1.txt)).

## Comparative Overview

The table below consolidates the core dataset parameters that are stated explicitly and unambiguously in the primary source.

| Attribute | Spanish | German | Czech |
|---|---|---|---|
| Corpus / source | PC-GITA ([6]) | Skodda et al. ([18]) | Rusz ([19], [10]) |
| PD patients | 50 | 88 | 50 |
| Healthy controls | 50 | 88 | 50 |
| Total speakers | 100 | 176 | 100 |
| Rapid syllable task | /pa-ta-ka/, /pe-ta-ka/, /pa-ka-ta/, /pa/, /ta/, /ka/ | /pa-ta-ka/ | /pa-ta-ka/ |
| Sentences | 10 sentences | 5 sentences | — |
| Read text | 36 words | 81 words | 80 words |
| Monologue | Yes | Yes | Yes |
| Medication state | ON (daily medication) | Not specified in source | Not specified in source |

*Note.* Table compiled from ([Vásquez-Correa et al., n.d.](document_1.txt)). Across the three languages, the aggregate totals are 188 PD patients and 188 HC speakers, i.e., 376 speakers overall — a globally class-balanced design even though individual-language performance was reported as class-unbalanced.

The primary source also notes that Table 1 of the paper summarizes the number of speakers, gender (male/female), age ranges, mean age with standard deviations, mean MDS-UPDRS-III scores with standard deviations, and time since diagnosis in years for each group ([Vásquez-Correa et al., n.d.](document_1.txt)). The extracted text renders these demographic rows in a degraded, interleaved form (for example, MDS-UPDRS-III values such as 37.8 (22.1) and 22.1 (9.9) appear alongside age-like values of 60.7 (7.3)), so precise per-group demographic figures cannot be reliably reconstructed from the supplied material. What the narrative text does establish clearly is that the Spanish patients had a higher average MDS-UPDRS-III score than the German and Czech patients, meaning the Spanish cohort contained patients with greater disease severity ([Vásquez-Correa et al., n.d.](document_1.txt)). This is the study's own stated explanation for why Spanish speakers exhibited "the best initial separability."

## From Raw Recordings to Modeling Inputs

The datasets were not used in raw form. All signals were segmented based on automatic detection of onset and offset transitions, which model patients' difficulty in starting and stopping vocal fold vibration ([Vásquez-Correa et al., n.d.](document_1.txt)). The detection relies on the presence of the fundamental frequency in short-time frames; once the border between voiced and unvoiced frames is detected, 80 ms of signal is extracted to the left and right, forming 160 ms segments.

Two modeling tracks were applied to these segments. The baseline track computed 12 Mel-Frequency Cepstral Coefficients (MFCCs) with their first and second derivatives, plus log energy of the signal distributed into 22 Bark bands — 58 descriptors total — to which four statistical functionals (mean, standard deviation, skewness, kurtosis) were applied, yielding a 232-dimensional feature vector per utterance. Classification used a radial basis function SVM with margin parameter C = 10 and Gaussian kernel parameter γ = 0.0001, evaluated with 10-fold speaker-independent cross-validation ([Vásquez-Correa et al., n.d.](document_1.txt)).

The deep-learning track computed a short-time Fourier transform with 256 frequency bins, using a 16 ms window and 4 ms step size, producing 41 time frames per transition. The resulting spectrogram was mapped to the Mel scale with 80 filters, forming an 80 × 41 image used to train the CNN. The CNN contains four convolutional and max-pooling layers, dropout regularization, and two fully connected layers, trained with cross-entropy loss and the Adam optimizer ([Vásquez-Correa et al., n.d.](document_1.txt)). The final decision per speaker was obtained by majority voting across the different speech exercises.

## How the Datasets Support the Transfer-Learning Experiment

The transfer-learning protocol uses the datasets as a matrix of base–target language pairs. A CNN is trained on utterances from one language, and the pre-trained weights initialize two models for the remaining languages ([Vásquez-Correa et al., n.d.](document_1.txt)). The reported outcome is the key quantitative result tied to these datasets: accuracy improved by more than 8% for German (from 69.3% in the baseline to 77.3% when fine-tuned from Spanish) and by over 4.1% for Czech (from 68.5% with the initial CNN to 72.6% when fine-tuned from Spanish) ([Vásquez-Correa et al., n.d.](document_1.txt)). The highest accuracy for both German and Czech was obtained when Spanish was the base language, which the authors attribute to Spanish having the strongest initial separability. Transfer-learned models were also described as more balanced in specificity–sensitivity and as having lower variance, indicating improved generalization ([Vásquez-Correa et al., n.d.](document_1.txt)).

Before transfer, the per-language baseline and CNN results differed by language: Spanish showed similar baseline and CNN accuracies and the highest accuracy among the three languages; German's highest accuracy came from the baseline model; and Czech's highest accuracy came from the CNN ([Vásquez-Correa et al., n.d.](document_1.txt)). The authors explicitly note that results in Table 3 were unbalanced toward one class according to specificity and sensitivity values — an important caveat when interpreting apparent accuracy gains.

## Reliability Assessment: A Material Discrepancy Between Sources

The two supplied documents conflict on the identity of one dataset, and this conflict must be resolved before the data inventory can be considered valid.

According to the primary study text, the three languages are **Spanish, German, and Czech**, and the 88 PD / 88 HC cohort is explicitly described as "from Germany," citing Skodda, Visser, and Schlegel ([Vásquez-Correa et al., n.d.](document_1.txt)). Multiple internal signals corroborate this: the abstract names Spanish, German, and Czech; the author affiliations include Friedrich-Alexander Universität Erlangen-Nürnberg and Universität Munich in Germany; the Czech Technical University in Prague is represented; and the study's funding acknowledgment lists the EU Horizon 2020 Marie Skłodowska-Curie program ([Vásquez-Correa et al., n.d.](document_1.txt)).

The third-party research note, by contrast, states that the study uses "Spanish, Italian, and Czech" and asserts that the 88 PD / 88 HC dataset is "from Italy" ([Third-party research note, n.d.](document_2.txt)). It also adds an interpretation not present in the primary text — that the speaker counts "are 88 PD patients with 88 HC speakers and 50 PD patients with 50 HC" for the Italian and Czech data respectively ([Third-party research note, n.d.](document_2.txt)).

My assessment is that the third-party note contains a factual error and that the primary source is authoritative. The substitution of "Italian" for "German" appears to be a misreading of the source material, and it is consequential: an entire language-specific cohort would be misidentified, invalidating any secondary analysis that reused that attribution. The reliability hierarchy here is clear — a study's own methods section, cross-corroborated by author affiliations and a cited German-language reference, outweighs an unattributed summary note. Researchers using the third-party note as their only source would propagate an incorrect data lineage claim.

## Limitations and Biases Inherent in the Datasets

Several dataset-level limitations should be flagged.

First, sample sizes are modest. With 50 PD patients per language for Spanish and Czech, and 88 for German, the effective speaker count per language constrains statistical power and makes cross-validation variance a genuine concern; the reported standard deviations in the transfer-learning results (for example, 13.9 for Spanish-to-Czech accuracy) reflect this ([Vásquez-Correa et al., n.d.](document_1.txt)).

Second, class balance at the corpus level does not guarantee balanced classifier behavior. The study itself reports that baseline and CNN results were "unbalanced towards one of the two classes" in all three languages, meaning specificity and sensitivity diverged despite equal numbers of PD and HC speakers ([Vásquez-Correa et al., n.d.](document_1.txt)).

Third, disease-severity distribution is not uniform across languages. The Spanish cohort had higher average MDS-UPDRS-III scores than the German and Czech cohorts, which plausibly explains why Spanish formed the strongest base model — but it also means the "language" variable is confounded with "disease severity" ([Vásquez-Correa et al., n.d.](document_1.txt)).

Fourth, medication state is only documented for the Spanish cohort (all ON medication); the source does not report medication state for the German and Czech speakers, leaving a possible uncontrolled source of acoustic variation ([Vásquez-Correa et al., n.d.](document_1.txt)).

Fifth, the speech tasks are not identical across languages. Word counts in the read texts differ (36 words in Spanish, 81 in German, 80 in Czech), and the number of sentences differs (10 in Spanish, 5 in German, none specified for Czech), so the datasets are harmonized in structure but not strictly matched in content ([Vásquez-Correa et al., n.d.](document_1.txt)).

## Conclusion

The study rests on three language-specific clinical speech datasets: the PC-GITA corpus for Colombian Spanish (50 PD, 50 HC), a German corpus of 88 PD and 88 HC speakers attributed to Skodda et al., and a Czech corpus of 50 PD and 50 HC speakers attributed to Rusz ([Vásquez-Correa et al., n.d.](document_1.txt)). Together these provide 376 speakers, evenly split between 188 PD patients and 188 healthy controls, recorded under noise-controlled conditions at 16 kHz with neurologist-assigned MDS-UPDRS-III severity ratings. The data were segmented into 160 ms voiced/unvoiced transition windows, then represented either as 232-dimensional hand-crafted feature vectors for SVM baselines or as 80 × 41 Mel-spectrograms for CNN training, with a transfer-learning scheme that reuses one language's model as initialization for another.

The single most important data-governance finding of this review is the source conflict: the primary study clearly uses German data, whereas the third-party note misidentifies the same cohort as Italian ([Third-party research note, n.d.](document_2.txt); [Vásquez-Correa et al., n.d.](document_1.txt)). Any derivative work should treat the primary study as the authoritative record of dataset provenance and treat the third-party note with caution on this specific point. Beyond provenance, the datasets are fit for their stated purpose — demonstrating cross-lingual transfer learning for PD speech classification — but their modest per-language sample sizes, cross-language differences in disease severity and speech-task content, and documented class-direction imbalance mean that the reported accuracy gains should be interpreted as promising rather than conclusive. The authors themselves signal this by proposing future work on more robust base models, Bayesian hyper-parameter optimization, multi-language base training, severity-stratified evaluation, and transfer learning across diseases ([Vásquez-Correa et al., n.d.](document_1.txt)).

## References

Third-party research note: Convolutional Neural Networks and a Transfer Learning Strategy to Classify Parkinson's Disease from Speech in Three Different Languages [document_2.txt]. (n.d.).

Vásquez-Correa, J. C., Arias-Vergara, T., Rios-Urrego, C. D., Schuster, M., Rusz, J., Orozco-Arroyave, J. R., & Nöth, E. (n.d.). *Convolutional neural networks and a transfer learning strategy to classify Parkinson's disease from speech in three different languages* [document_1.txt].