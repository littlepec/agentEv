# What Is the Test Set Size? An Evidentiary Report on the English–German WMT news-test2015 Evaluation Set

## Abstract

This report addresses the question "what is the test set size?" in relation to the translation research paper *On NMT Search Errors and Model Errors: Cat Got Your Tongue?* The evidence available in the supplied documentation supports a single, unambiguous answer to the primary question: the full test set consists of **2,169 sentences** ([document_2.txt](document_2.txt)). However, the documentation also establishes that a distinct subset of that test set was used for the length-constrained exact search experiments, and that these subsets represent 73.0% and 48.3% of the full test set respectively ([document_2.txt](document_2.txt); [document_1.txt](document_1.txt)). Consequently, any answer to the query must carefully distinguish between the *full* test set size and the *subset* sizes used in a specific experimental condition. The report concludes that the defensible headline answer is 2,169 sentences, with the subsets approximate to 1,583 and 1,048 sentences respectively.

## Introduction

The question "what is the test set size?" appears simple but is, in practice, a question about which evaluation set is being referenced. In neural machine translation (NMT) research, the size of a test set is a central methodological parameter: it determines the statistical power of reported results, the comparability of a study with prior work, and the computational cost of inference. When a paper reports more than one evaluation configuration—for example, a full test set for headline results and a reduced subset for computationally expensive analyses—the phrase "test set size" can legitimately refer to several different numbers.

The documentation supplied for this report contains two source documents. The first, referred to here as [document_1.txt](document_1.txt), is a direct excerpt from the paper's "Results with Length Constraints" section. The second, [document_2.txt](document_2.txt), is a compilation of third-party research notes and extracted facts about the paper, including its key questions, the identity of the test set, and the reported subset proportions. Together, these sources permit a reasonably confident reconstruction of the relevant figures, while also exposing where interpretation is required rather than mere retrieval.

## The Full Test Set: 2,169 Sentences

### The Reported Figure

The documentation states repeatedly and consistently that the paper's main experiments use the English–German WMT news-test2015 test set, and that this test set contains 2,169 sentences ([document_2.txt](document_2.txt)). The same source explicitly notes that the paper reports the test set size as a number of sentences, and that the full test set size of 2,169 sentences is reported **before any subset selection** ([document_2.txt](document_2.txt)). This qualification is significant: it means the figure of 2,169 is a property of the corpus itself as prepared for the experiment, not an artefact of any subsequent filtering, length restriction, or sampling procedure.

### Characteristics of the Test Set

According to the third-party research note, the test set has two identifying characteristics that should be recorded alongside its size. First, it is a **news** test set, meaning its domain is news text rather than, for instance, web text, spoken language, or a mixed-domain benchmark ([document_2.txt](document_2.txt)). Second, the **language pair is English–German** ([document_2.txt](document_2.txt)). The specific corpus is identified as **WMT news-test2015**, which situates the work within the standard annual WMT evaluation cycle and makes the results, in principle, comparable with other studies that adopt the same benchmark ([document_2.txt](document_2.txt)).

### Why the Full Test Set Size Matters

The full test set size of 2,169 sentences is the number that should be cited when describing the scale of the paper's primary evaluation. It is the denominator against which the subset proportions discussed below are computed, and it is the figure that a reader would need in order to reason about the statistical precision of the paper's headline results. The documentation is explicit that the 2,169-sentence figure is distinct from the subset experiments and precedes them ([document_2.txt](document_2.txt)). In other words, the subsets are drawn *from* this population of 2,169 sentences; they do not redefine it.

| Attribute | Reported value | Source |
|---|---|---|
| Full test set size | 2,169 sentences | [document_2.txt](document_2.txt) |
| Language pair | English–German | [document_2.txt](document_2.txt) |
| Corpus | WMT news-test2015 | [document_2.txt](document_2.txt) |
| Domain | News | [document_2.txt](document_2.txt) |
| Unit of measurement | Sentences | [document_2.txt](document_2.txt) |
| Reported before subset selection? | Yes | [document_2.txt](document_2.txt) |

## Subset Selection in the Length-Constrained Exact Search Experiments

### Rationale: Runtime Control

The paper's own text, reproduced in [document_1.txt](document_1.txt), explains why a subset was used at all. The authors state that they constrained exact search to certain translation lengths "to find out more about the length deficiency," and that constraining search in this way "increases the run time as the γ-bounds are lower" ([document_1.txt](document_1.txt)). Because of this computational penalty, "all results in this section are conducted on only a subset of the test set to keep the runtime under control" ([document_1.txt](document_1.txt)). This is a methodologically transparent justification: the reduction is a deliberate trade-off between inferential coverage and tractability, not an unexplained convenience sample.

### Reported Subset Proportions

The research note records two specific subset proportions for the length-constrained exact search experiments: one experiment uses **73.0%** of the test set, and other experiments use **48.3%** of the test set ([document_2.txt](document_2.txt)). The note presents these as the subset figures the paper reports, and again emphasises that these subset experiments are distinct from the full test set size of 2,169 sentences ([document_2.txt](document_2.txt)).

The documentation does not state the absolute sentence counts corresponding to these percentages. However, since the percentages are expressed relative to the 2,169-sentence full test set ([document_2.txt](document_2.txt)), the approximate absolute sizes can be derived arithmetically. These derived values are presented below and should be treated as computations from the reported figures rather than as figures quoted directly from the paper.

| Condition | Share of full test set | Derived approximate sentences | Source for share |
|---|---|---|---|
| Length-constrained exact search (subset A) | 73.0% | ≈ 1,583 | [document_2.txt](document_2.txt) |
| Length-constrained exact search (subset B) | 48.3% | ≈ 1,048 | [document_2.txt](document_2.txt) |
| Full test set | 100% | 2,169 | [document_2.txt](document_2.txt) |

### Interpretation of the Gap Between Conditions

The difference between the two subset proportions—73.0% versus 48.3%, a spread of 24.7 percentage points, or roughly 535 sentences derived from the 2,169-sentence base—implies that the length-constrained experiments did not all operate at the same level of restriction. This is consistent with the stated mechanism in [document_1.txt](document_1.txt): tighter γ-bounds and more restrictive length constraints raise runtime, and therefore force a smaller evaluation subset ([document_1.txt](document_1.txt)). A reader should consequently avoid treating "the length-constrained test set" as a single fixed quantity; it varies by experimental configuration.

## Answering the Query: Distinguishing Full and Subset Sizes

Given the documentation, the question "what is the test set size?" has a primary answer and a set of secondary answers.

**Primary answer.** The full test set size is **2,169 sentences**, drawn from the English–German WMT news-test2015 news test set ([document_2.txt](document_2.txt)). This is the figure the paper reports before any subset selection, and it is the figure that describes the scale of the paper's main evaluation ([document_2.txt](document_2.txt)).

**Secondary answers.** For the length-constrained exact search experiments specifically, the evaluation was conducted on subsets representing **73.0%** and **48.3%** of the test set, corresponding to approximately 1,583 and 1,048 sentences ([document_2.txt](document_2.txt)). These figures exist only because runtime constraints made full-set evaluation impractical under tightened search bounds ([document_1.txt](document_1.txt)).

The documentation is emphatic that these two classes of figure must not be conflated: the subset experiments "are distinct from the full test set size of 2,169 sentences" ([document_2.txt](document_2.txt)). A report that answered the query with 73.0% or 48.3% alone would therefore be incomplete, and one that answered "2,169 sentences" without noting the subsets would obscure a genuine methodological caveat.

## Methodological and Reproducibility Implications

Three implications follow from these findings.

First, **comparability across sections of the paper is bounded**. Results computed on 48.3% of the test set are not directly comparable, in a strict statistical sense, with results computed on 100% of it, because the evaluation samples differ in size and possibly in composition ([document_2.txt](document_2.txt)).

Second, **reproduction requires knowing which subset**. A researcher attempting to reproduce the length-constrained results would need the exact subset definition—not merely the percentage—since the documentation does not specify how the subset was selected ([document_2.txt](document_2.txt)).

Third, **the full-set figure remains the anchor for external comparison**. Because 2,169 sentences is reported before subset selection and is tied to a named public benchmark, WMT news-test2015, it is the figure that supports cross-study comparison ([document_2.txt](document_2.txt)).

## Source Reliability and Confidence Assessment

The two sources differ in character. [document_1.txt](document_1.txt) is a verbatim excerpt from the paper's results section and therefore constitutes primary evidence for the runtime rationale and for the existence of a subset ([document_1.txt](document_1.txt)). [document_2.txt](document_2.txt) is explicitly labelled a "third-party research note," which makes it secondary evidence, though it is internally consistent across repeated passages and aligns with the primary excerpt on the central point that a subset was used ([document_2.txt](document_2.txt)). Both sources are concordant on the 2,169-sentence full test set size; no contradicting figure appears anywhere in the supplied material. Confidence in the primary answer is therefore high, while confidence in the derived absolute subset sizes is moderate, since those numbers are computed rather than reported.

## Conclusion

The test set size, understood as the full evaluation set used in the paper's main experiments, is **2,169 sentences** from the English–German WMT news-test2015 news test set ([document_2.txt](document_2.txt)). This figure is reported before any subset selection and is explicitly distinguished in the documentation from the reduced sets used in the length-constrained exact search experiments, which covered 73.0% and 48.3% of the test set—approximately 1,583 and 1,048 sentences—in order to keep runtime under control ([document_2.txt](document_2.txt); [document_1.txt](document_1.txt)). The most accurate and complete response to the query is therefore: 2,169 sentences for the full test set, with subset-based evaluations of roughly 1,583 and 1,048 sentences in the length-constrained condition.

## References

document_1.txt. (n.d.). *4 Results with Length Constraints* [Excerpt from a research paper]. [document_1.txt](document_1.txt)

document_2.txt. (n.d.). *Third-party research note: On NMT Search Errors and Model Errors: Cat Got Your Tongue?* [Research note and extracted facts]. [document_2.txt](document_2.txt)