# Datasets Used in the Speech-Based Study of Parkinson's Disease: A Report on the German and Czech Corpora

## 1. Purpose and Scope of the Report

This report answers the question "What datasets are used?" by identifying, describing, and analysing the datasets reported in the single source document supplied for this task. The source identifies two distinct speech corpora: a German dataset and a Czech dataset, both of which consist of speech recordings drawn from individuals diagnosed with Parkinson's disease (PD) and from healthy control (HC) speakers ([document_2.txt](document_2.txt)). The report sets out the composition of each dataset, the diagnostic groupings, the speaker counts, the language dimension, and the analytical implications of the reported design. It also states clearly what the source does not specify, so that readers do not attribute properties to these corpora that the available evidence does not support.

## 2. Datasets Identified

Two datasets are used. The first is a German dataset; the second is a Czech dataset ([document_2.txt](document_2.txt)). The source frames these as a pair of corpora that jointly "supply speech recordings of Parkinson's disease patients and healthy controls across multiple languages" ([document_2.txt](document_2.txt)). The essential facts about each corpus are reported as speaker counts disaggregated by diagnostic status, and the source explicitly notes that for the German material, "the German dataset description reports this composition" ([document_2.txt](document_2.txt)).

### 2.1 The German Dataset

The German data consist of speech recordings of 44 PD patients and 44 HC speakers ([document_2.txt](document_2.txt)). This yields a German cohort of 88 speakers in total. The source reports the German speaker counts as "44 PD patients with 44 HC speakers" ([document_2.txt](document_2.txt)), which establishes an exact one-to-one ratio between the clinical and control groups within this corpus. The source does not state the total German speaker count directly; it is obtained by summing the two diagnostic groups reported ([document_2.txt](document_2.txt)).

### 2.2 The Czech Dataset

The Czech dataset contains a total of 100 native Czech speakers, comprising 50 PD patients and 50 healthy controls ([document_2.txt](document_2.txt)). As with the German corpus, the diagnostic groups are of equal size, and the source describes the Czech speaker counts as "50 PD patients with 50 HC" ([document_2.txt](document_2.txt)). The source explicitly characterises this cohort as consisting of "native Czech speakers" ([document_2.txt](document_2.txt)), a qualification that is applied to the Czech data but not, in the supplied text, to the German data.

## 3. Comparative Overview of Dataset Composition

Table 1 consolidates the speaker counts reported in the source.

**Table 1.** *Composition of the German and Czech speech datasets*

| Dataset | Diagnostic group | Speaker count | Subtotal |
|---|---|---|---|
| German | PD patients | 44 | 88 |
| German | Healthy controls | 44 | 88 |
| Czech | PD patients | 50 | 100 |
| Czech | Healthy controls | 50 | 100 |
| **Combined** | **PD patients** | **94** | **188** |
| **Combined** | **Healthy controls** | **94** | **188** |

*Note.* All figures are taken or derived directly from the reported speaker counts for the German and Czech datasets ([document_2.txt](document_2.txt)). Combined totals are arithmetic sums of the two corpus-level counts.

Table 2 expresses the same information as proportions, which is useful for assessing group balance.

**Table 2.** *Diagnostic group balance within and across the two datasets*

| Diagnostic group | German dataset | Czech dataset | Combined |
|---|---|---|---|
| PD patients | 44 (50.0%) | 50 (50.0%) | 94 (50.0%) |
| Healthy controls | 44 (50.0%) | 50 (50.0%) | 94 (50.0%) |
| Total | 88 (100.0%) | 100 (100.0%) | 188 (100.0%) |

*Note.* Percentages are derived from the speaker counts reported in the source ([document_2.txt](document_2.txt)).

The combined corpus therefore contains 188 speakers, of whom 94 are PD patients and 94 are healthy controls ([document_2.txt](document_2.txt)). The Czech dataset is the larger of the two, contributing 100 of the 188 speakers, or approximately 53.2% of the combined total, while the German dataset contributes 88 speakers, or approximately 46.8% ([document_2.txt](document_2.txt)).

## 4. Data Modality and Content

Both datasets are described as collections of "speech recordings" rather than as textual, imaging, or clinical-scale data ([document_2.txt](document_2.txt)). The source states that these datasets "supply speech recordings of Parkinson's disease patients and healthy controls across multiple languages" ([document_2.txt](document_2.txt)). This establishes the modality of the material: recorded human speech, captured from individuals in two diagnostic categories. It also establishes the comparative purpose of the pair, namely the provision of speech data from both clinical and non-clinical populations ([document_2.txt](document_2.txt)).

## 5. The Cross-Linguistic Dimension

A defining feature of the dataset pair is that it spans more than one language. The source states that the datasets provide recordings "across multiple languages" ([document_2.txt](document_2.txt)). Two languages are identified in the supplied material: German, associated with the German dataset, and Czech, associated with the Czech dataset ([document_2.txt](document_2.txt)). The Czech cohort is explicitly described as composed of native Czech speakers ([document_2.txt](document_2.txt)).

This cross-linguistic structure is analytically significant. A PD-versus-HC comparison conducted within a single language risks confounding diagnostic effects with language-specific phonetic and prosodic patterns. A two-language design permits, at minimum, the examination of whether any observed difference between PD patients and healthy controls replicates across languages with different phonological inventories and rhythmic properties ([document_2.txt](document_2.txt)). It should be noted, however, that the source does not report whether the German and Czech recordings were elicited with identical tasks, nor whether the two corpora were collected under harmonised protocols ([document_2.txt](document_2.txt)). Any cross-linguistic generalisation therefore rests on an assumption of procedural comparability that the supplied document does not verify.

## 6. Balance, Matching, and Design Characteristics

### 6.1 Exact Diagnostic Balance

Both datasets exhibit exact balance between the diagnostic groups. In the German data, 44 PD patients are matched by 44 HC speakers; in the Czech data, 50 PD patients are matched by 50 healthy controls ([document_2.txt](document_2.txt)). Across the combined corpus, the split is 94 PD patients and 94 healthy controls ([document_2.txt](document_2.txt)). This equal-allocation structure is methodologically important, because it eliminates the class imbalance that can bias the performance of machine-learning classifiers and complicate the interpretation of accuracy metrics in diagnostic classification studies.

### 6.2 What the Source Says About Matching

The source establishes numerical balance in diagnostic status but does not report matching on age, sex, disease duration, medication status, or recording equipment ([document_2.txt](document_2.txt)). Numerical balance should therefore not be equated with demographic or technical matching. The equal group sizes reported are a necessary but not a sufficient condition for a well-controlled case–control comparison ([document_2.txt](document_2.txt)).

## 7. Sample Size and Analytical Implications

### 7.1 The German Dataset

With 88 speakers, the German dataset is moderate in size for a speech corpus and would typically be adequate for within-corpus comparisons of acoustic or prosodic features between PD patients and controls, provided the number of simultaneous predictors is kept modest. Its equal allocation of 44 cases and 44 controls maximises statistical efficiency for a fixed total sample ([document_2.txt](document_2.txt)).

### 7.2 The Czech Dataset

The Czech dataset, with 100 speakers split evenly between 50 PD patients and 50 healthy controls, is the larger of the two ([document_2.txt](document_2.txt)). Its explicit identification of speakers as native Czech speakers ([document_2.txt](document_2.txt)) supports the internal linguistic homogeneity of the sample.

### 7.3 The Combined Corpus

Pooling the two datasets yields 188 speakers, comprising 94 PD patients and 94 healthy controls ([document_2.txt](document_2.txt)). The pooled sample is large enough to support analyses that stratify by language, with roughly 44 to 50 participants per diagnostic group per language ([document_2.txt](document_2.txt)). It remains comparatively small, however, if the aim is to train and validate high-dimensional predictive models with many parameters.

## 8. What the Source Does Not Specify

Several attributes commonly required for a full appraisal of a dataset are absent from the supplied material. The source does not provide:

- Formal names or identifiers for either corpus ([document_2.txt](document_2.txt)).
- Recording conditions, devices, sampling rates, or file formats ([document_2.txt](document_2.txt)).
- The speech tasks elicited, such as sustained vowels, read passages, monologues, or diadochokinetic tasks ([document_2.txt](document_2.txt)).
- Recording durations, the number of samples per speaker, or total corpus duration ([document_2.txt](document_2.txt)).
- Diagnostic criteria, disease stage, severity ratings, or medication state ([document_2.txt](document_2.txt)).
- Demographic composition, including age and sex distributions ([document_2.txt](document_2.txt)).
- Whether the German speakers were native German speakers, a qualification the source supplies only for the Czech cohort ([document_2.txt](document_2.txt)).
- An explicit statement that the two corpora used identical elicitation protocols ([document_2.txt](document_2.txt)).

These omissions constrain the conclusions that can be drawn from the source alone and should be addressed before the datasets are reused.

## 9. Reliability and Significance of the Source

The supplied information derives from a single document, referenced here as document_2.txt ([document_2.txt](document_2.txt)). Its reliability rests on the precision of its speaker-count reporting: it gives exact and internally consistent figures for both corpora, and it attributes the German composition explicitly to "the German dataset description" ([document_2.txt](document_2.txt)). This is a meaningful signal, because the figures for the German data are presented as reproduced from an underlying dataset description rather than as an independent estimate.

The significance of the datasets lies in three properties. First, they target a clinically important condition, Parkinson's disease, whose speech manifestations have attracted substantial research attention ([document_2.txt](document_2.txt)). Second, they include healthy controls, which permits controlled contrast rather than purely descriptive profiling ([document_2.txt](document_2.txt)). Third, they span German and Czech, which allows findings to be tested across languages ([document_2.txt](document_2.txt)).

The principal limitation of the source is that it is a brief descriptive passage rather than a full corpus publication or data descriptor ([document_2.txt](document_2.txt)). It is therefore a secondary description of the datasets, and any downstream use should consult the original dataset documentation. No independent corroborating source was provided, so all facts reported here rest on that single document ([document_2.txt](document_2.txt)).

## 10. Conclusion

Two datasets are used: a German dataset of 88 speakers, comprising 44 PD patients and 44 healthy controls, and a Czech dataset of 100 native Czech speakers, comprising 50 PD patients and 50 healthy controls ([document_2.txt](document_2.txt)). Together they provide speech recordings from 188 speakers, evenly divided into 94 PD patients and 94 healthy controls, across two languages ([document_2.txt](document_2.txt)). The design is characterised by exact diagnostic balance within each corpus and by cross-linguistic coverage spanning German and Czech ([document_2.txt](document_2.txt)). The datasets are suited to controlled case–control analyses of speech in Parkinson's disease and to tests of cross-linguistic replication, subject to the important caveat that the supplied source does not document recording protocols, speech tasks, demographic matching, or clinical staging ([document_2.txt](document_2.txt)).

## References

document_2.txt. (n.d.). *Description of German and Czech speech datasets for Parkinson's disease* [Unpublished source document].