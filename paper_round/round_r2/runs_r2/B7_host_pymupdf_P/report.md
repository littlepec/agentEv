# Determining the Test Set Size in Stahlberg and Byrne’s NMT Search Error Study

## Introduction

The query asks: “what is the test set size?” In the context of the provided documents, this question refers to the English-German WMT news-test2015 test set used by Stahlberg and Byrne (2019) in their study of search errors and model errors in neural machine translation (NMT). The primary source, document_1.txt, explicitly reports that the main experiments are conducted on the entire test set comprising 2,169 sentences ([Stahlberg & Byrne, 2019](document_1.txt)). A third-party research note, document_2.txt, repeatedly claims that the test set contains 3,003 sentences ([Third-party research note](document_2.txt)). These two figures conflict. After evaluating the reliability of the sources, the primary paper’s explicit statement is the authoritative answer: the full test set size is 2,169 sentences. The third-party note’s 3,003 figure is unsupported by the primary text and appears to be an error. This report details the evidence, distinguishes the full test set from the subsets used in length-constrained experiments, and explains why the correct size matters for interpreting the reported results.

## Primary Source Evidence: 2,169 Sentences

The most direct evidence comes from Section 3 of document_1, titled “Results without Length Constraints.” The paper states: “We conduct all our experiments in this section on the entire English-German WMT news-test2015 test set (2,169 sentences) with a Transformer base model…” ([Stahlberg & Byrne, 2019](document_1.txt)). This is an unambiguous statement of the full test set size. The abstract also refers to the “entire WMT15 English-German test set” but does not provide a numerical count ([Stahlberg & Byrne, 2019](document_1.txt)). The number 2,169 is therefore the only explicit full-set size given in the primary paper’s experimental setup.

All main results in Section 3 are based on this 2,169-sentence test set. Table 1 reports BLEU scores, length ratios, search error rates, and empty translation rates for greedy search, beam search with beam size 10, and exact search ([Stahlberg & Byrne, 2019](document_1.txt)). For example, exact search achieves a BLEU score of 2.1 and a length ratio of 0.06, with 51.8% of sentences receiving the empty translation as the global best model score ([Stahlberg & Byrne, 2019](document_1.txt)). These percentages apply to the full 2,169-sentence test set. Similarly, Figures 1, 2, 3, and 4 in the paper visualize results over the entire test set, including the relationship between beam size, search errors, log-likelihood, length ratios, and source sentence length ([Stahlberg & Byrne, 2019](document_1.txt)). The paper’s central conclusion—that beam search fails to find the global best model score for more than half of sentences and that NMT often prefers empty translations—is therefore grounded in a test set of 2,169 sentences ([Stahlberg & Byrne, 2019](document_1.txt)).

Table 2 further compares different NMT architectures: LSTM, SliceNet, Transformer-Base, and Transformer-Big ([Stahlberg & Byrne, 2019](document_1.txt)). The reported search error rates (e.g., 57.7% for Transformer-Base with Beam-10) and empty translation rates (e.g., 51.8% for Transformer-Base with exact search) are computed over the same full test set unless otherwise noted ([Stahlberg & Byrne, 2019](document_1.txt)). The table does not indicate a subset, so the 2,169-sentence size remains the reference for those comparisons.

To quantify absolute numbers from these percentages under the 2,169-sentence assumption: 51.8% of 2,169 equals approximately 1,124 sentences where exact search selects the empty translation. Beam-10’s 57.7% search error rate corresponds to about 1,252 sentences. Greedy search’s 73.6% search error rate corresponds to about 1,596 sentences. These absolute counts are useful for understanding the scale of the model error and search error phenomena, and they depend directly on the correct test set size ([Stahlberg & Byrne, 2019](document_1.txt)).

### Table 1: Main Results on the Full 2,169-Sentence Test Set

| Search Method | BLEU | Length Ratio | Search Errors | Empty Translations |
|---------------|------|--------------|---------------|--------------------|
| Greedy | 29.3 | 1.02 | 73.6% | 0.0% |
| Beam-10 | 30.3 | 1.00 | 57.7% | 0.0% |
| Exact | 2.1 | 0.06 | 0.0% | 51.8% |

Data adapted from Stahlberg and Byrne (2019), Table 1 ([Stahlberg & Byrne, 2019](document_1.txt)).

## Third-Party Note’s Conflicting Claim: 3,003 Sentences

Document_2, a third-party research note, states multiple times that “the paper’s main experiments use the entire English-German WMT news-test2015 test set of 3,003 sentences” and that “the entire English-German WMT news-test2015 test set contains 3,003 sentences” ([Third-party research note](document_2.txt)). It further asserts that “the paper reports this size in its experimental setup” ([Third-party research note](document_2.txt)). However, the primary source does not report 3,003 anywhere in the provided text. Instead, it reports 2,169 ([Stahlberg & Byrne, 2019](document_1.txt)).

This discrepancy is critical. The third-party note provides no direct quotation from the paper to support its 3,003 figure. It also does not explain why the number would be 3,003 when the primary source says 2,169. The note’s repetition of the 3,003 figure does not make it more reliable; it merely repeats an unsupported assertion ([Third-party research note](document_2.txt)). In contrast, the primary source contains the experimental setup, tables, and algorithms, and its statement of 2,169 sentences is embedded in the exact section describing the main experiments ([Stahlberg & Byrne, 2019](document_1.txt)).

When two sources conflict, the primary source should generally be preferred, especially when it is the original research paper and the other is a third-party summary. The primary source is more likely to contain accurate details because it is the authors’ own description of their experiments. The third-party note may have confused the WMT15 test set with a different WMT edition or another test set size, but within the provided information, the 3,003 figure remains unsupported ([Third-party research note](document_2.txt); [Stahlberg & Byrne, 2019](document_1.txt)).

### Table 2: Conflicting Claims About the Full Test Set Size

| Source | Claimed Full Test Set Size | Evidence Type | Reliability Assessment |
|--------|----------------------------|---------------|------------------------|
| Document_1 (Stahlberg & Byrne, 2019) | 2,169 sentences | Explicit statement in Section 3 experimental setup | Primary source; high reliability |
| Document_2 (Third-party research note) | 3,003 sentences | Repeated assertion without direct quotation | Third-party summary; unsupported and conflicting; lower reliability |

Data adapted from Stahlberg and Byrne (2019) and the third-party research note ([Stahlberg & Byrne, 2019](document_1.txt); [Third-party research note](document_2.txt)).

## Subsets Used in Length-Constrained Experiments

A crucial nuance is that not all experiments in the paper use the full 2,169-sentence test set. The paper’s Section 4, “Results with Length Constraints,” explicitly states that “all results in this section are conducted on only a subset of the test set to keep the runtime under control” ([Stahlberg & Byrne, 2019](document_1.txt)). The reason is that constraining search to certain translation lengths increases runtime because the γ-bounds are lower ([Stahlberg & Byrne, 2019](document_1.txt)). The authors also note that they stopped decoding if the decoder took longer than a day for a single sentence on a single CPU ([Stahlberg & Byrne, 2019](document_1.txt)).

The specific subsets are given as percentages of the test set. The experiment shown in Figure 5, which applies a minimum translation length constraint of 0.25 times the source sentence length, is conducted on 73.0% of the test set ([Stahlberg & Byrne, 2019](document_1.txt)). The experiments reported in Tables 3 and 4, covering exact search under length constraints and length normalization, are conducted on 48.3% of the test set ([Stahlberg & Byrne, 2019](document_1.txt)). These subset sizes are distinct from the full test set size of 2,169 sentences. They are not additional test sets; rather, they are fractions of the full 2,169-sentence set. The paper does not provide the exact sentence counts for these subsets, but they can be approximated as 73.0% × 2,169 ≈ 1,583 sentences and 48.3% × 2,169 ≈ 1,048 sentences.

This distinction matters because the BLEU scores in Tables 3 and 4 (e.g., Beam-10 BLEU 37.0, exact search BLEU 27.2 without length normalization, and 36.4 with length normalization) are not directly comparable to the BLEU scores in Table 1 (e.g., Beam-10 BLEU 30.3 on the full test set) ([Stahlberg & Byrne, 2019](document_1.txt)). The length-constrained experiments use a smaller, potentially easier or differently distributed subset, which may explain the higher BLEU scores. The paper itself notes that the length-constrained results are on a subset to keep runtime under control, acknowledging the methodological trade-off ([Stahlberg & Byrne, 2019](document_1.txt)). Therefore, when answering “what is the test set size?”, one must specify whether the question refers to the full test set (2,169 sentences) or the subsets (73.0% and 48.3% of that full set).

### Table 3: Test Set Usage Across Experiments

| Experiment Section | Test Set Used | Size |
|--------------------|---------------|------|
| Results without Length Constraints (Tables 1–2, Figures 1–4) | Entire English-German WMT news-test2015 test set | 2,169 sentences |
| Results with Length Constraints – Figure 5 (minimum length 0.25× source length) | Subset of test set | 73.0% of 2,169 ≈ 1,583 sentences |
| Results with Length Constraints – Tables 3–4 (exact search under length constraints and length normalization) | Subset of test set | 48.3% of 2,169 ≈ 1,048 sentences |

Data adapted from Stahlberg and Byrne (2019) ([Stahlberg & Byrne, 2019](document_1.txt)).

## Why the Correct Test Set Size Matters

The test set size affects the interpretation of every major finding in the paper. First, the headline result that “beam search fails to find these global best model scores in most cases” and that “for more than 50% of the sentences, the model in fact assigns its global best score to the empty translation” is based on the full test set ([Stahlberg & Byrne, 2019](document_1.txt)). If the full test set were 3,003 sentences, the absolute number of sentences exhibiting empty translations would be substantially larger: 51.8% of 3,003 ≈ 1,556 sentences, compared to 51.8% of 2,169 ≈ 1,124 sentences. The percentage remains the same, but the scale of the problem in absolute terms changes. This matters for assessing how widespread the model error is and for planning future data collection or model improvements.

Second, the search error rates for greedy and beam search are expressed as percentages. With 2,169 sentences, Beam-10’s 57.7% search error rate corresponds to approximately 1,252 sentences, while Beam-100’s 53.62% search error rate corresponds to approximately 1,163 sentences ([Stahlberg & Byrne, 2019](document_1.txt)). If the test set were 3,003 sentences, those absolute counts would be 1,733 and 1,610 sentences, respectively. The paper’s conclusion that even a very large beam size of 100 produces more than 50% search errors remains true under either size, but the practical significance in terms of number of affected sentences is greater with a larger test set ([Stahlberg & Byrne, 2019](document_1.txt)).

Third, the length-constrained experiments use subsets, so their results are already limited in generalizability. The paper constrained exact search to translations longer than 0.25 times the source sentence length and still observed a peak in the (0.3, 0.5] length-ratio cluster, suggesting an inherent model bias toward shorter hypotheses ([Stahlberg & Byrne, 2019](document_1.txt)). This finding is based on 73.0% of the test set, which is about 1,583 sentences under the 2,169-sentence assumption. The length normalization experiments in Table 4, based on 48.3% of the test set (about 1,048 sentences), show that length normalization fixes translation lengths but prevents exact search from matching the BLEU score of Beam-10 ([Stahlberg & Byrne, 2019](document_1.txt)). These subset-based results are still informative, but they cannot be directly compared to full-test-set results without acknowledging the different sample sizes.

## Reliability and Prioritization of Sources

The primary source, document_1, is the original research paper by Stahlberg and Byrne (2019), available as arXiv:1908.10090v1 ([Stahlberg & Byrne, 2019](document_1.txt)). It includes the algorithms (BeamSearch and DFS), experimental setup, tables, figures, and references. Its explicit statement of 2,169 sentences appears in the experimental setup of Section 3, which is precisely where a reader would expect to find the test set size ([Stahlberg & Byrne, 2019](document_1.txt)). This makes it the most reliable source for answering the query.

The third-party research note, document_2, is a secondary summary that claims the paper uses 3,003 sentences ([Third-party research note](document_2.txt)). However, it provides no direct quotation, no page number, and no discussion of why the primary source’s explicit 2,169 figure should be overridden. It also repeats the 3,003 figure several times, which may create an illusion of corroboration, but repetition is not evidence ([Third-party research note](document_2.txt)). Given the conflict, the primary source must be prioritized. Therefore, the correct full test set size is 2,169 sentences, not 3,003.

It is also worth noting that the third-party note correctly observes that the length-constrained experiments use subsets of the test set, specifically 73.0% and 48.3% ([Third-party research note](document_2.txt)). This part of the note aligns with the primary source, but the note’s full-test-set figure does not. This mixed reliability further supports treating the note with caution and relying on the primary paper for the exact number.

## Conclusion

The answer to the query “what is the test set size?” is that the full English-German WMT news-test2015 test set used in the main experiments of Stahlberg and Byrne (2019) contains 2,169 sentences ([Stahlberg & Byrne, 2019](document_1.txt)). This is the size on which the paper’s primary results—including the 51.8% empty translation rate under exact search, the 57.7% search error rate for Beam-10, and the dramatic BLEU drop under exact search—are computed ([Stahlberg & Byrne, 2019](document_1.txt)). The length-constrained experiments use subsets of this full set: 73.0% of the test set for the minimum-length-constraint experiment in Figure 5, and 48.3% of the test set for the experiments in Tables 3 and 4 ([Stahlberg & Byrne, 2019](document_1.txt)). The third-party note’s claim of 3,003 sentences is not supported by the primary source and should not be adopted ([Third-party research note](document_2.txt)). For any analysis or replication of the paper’s main findings, the full test set size should be reported as 2,169 sentences, with subsets clearly identified as 73.0% and 48.3% of that total.

## References

Stahlberg, F., & Byrne, B. (2019). *On NMT search errors and model errors: Cat got your tongue?* arXiv:1908.10090v1. [document_1.txt](document_1.txt)

Third-party research note. (n.d.). *On NMT search errors and model errors: Cat got your tongue?* [document_2.txt](document_2.txt)