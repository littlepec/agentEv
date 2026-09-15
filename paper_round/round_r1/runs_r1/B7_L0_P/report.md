# Determining the Test Set Size in Stahlberg and Byrne's NMT Search Error Study

## 1. Overview and Direct Answer

The query asks for the test set size used in the study "On NMT Search Errors and Model Errors: Cat Got Your Tongue?" by Felix Stahlberg and Bill Byrne of the University of Cambridge ([Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090)). Based on the evidence provided, the authoritative answer is **2,169 sentences**: the paper's experimental section states that "We conduct all our experiments in this section on the entire English-German WMT news-test2015 test set (2,169 sentences)" ([Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090)). This figure is reported in the primary source, i.e., the paper itself, and refers to the full English–German WMT news-test2015 benchmark that anchors the study's headline exact-inference results.

However, the provided information also contains a second, conflicting figure. A third-party research note ([Third-Party Research Note, n.d.](https://arxiv.org/abs/1908.10090)) repeatedly asserts that "The paper's main experiments use the entire English-German WMT news-test2015 test set of 3,003 sentences" and that "The entire English-German WMT news-test2015 test set contains 3,003 sentences." Because these two numbers cannot both describe the same full test set, this report examines both claims, compares them against the internal evidence in the paper, and explains which figure should be treated as the correct full test set size. It also documents the fractions and estimated absolute sizes of the subsets used in the length-constrained experiments, since those subsets are frequently confused with the full test set.

## 2. The Primary Source: 2,169 Sentences

### 2.1 The Explicit Statement in the Experimental Setup

The most direct evidence comes from Section 3 of the paper, titled "Results without Length Constraints." There, the authors write that they "conduct all our experiments in this section on the entire English-German WMT news-test2015 test set (2,169 sentences) with a Transformer base model trained with Tensor2Tensor on parallel WMT18 data excluding ParaCrawl" ([Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090)). This is a precise, unambiguous statement that specifies three things simultaneously: the language pair (English–German), the benchmark (WMT news-test2015), and the size (2,169 sentences). It also explicitly states that this is the *entire* test set, meaning no subsetting was applied in that section.

### 2.2 Consistency with the Abstract and Introduction

The abstract states that the authors "use our exact search to find the global best model scores under a Transformer base model for the entire WMT15 English-German test set" ([Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090)). The phrase "entire WMT15 English-German test set" matches the Section 3 description of "the entire English-German WMT news-test2015 test set (2,169 sentences)," confirming that the same benchmark is meant throughout. The WMT15 news test set for English–German is a well-known, fixed benchmark, and the figure of 2,169 sentences is the standard size associated with it in the machine translation community.

### 2.3 Methodological Context

The paper reports that the model was a Transformer base architecture trained with Tensor2Tensor on parallel WMT18 data excluding ParaCrawl, with preprocessing that included joint subword segmentation using byte pair encoding with 32K merges, and that cased BLEU scores were reported ([Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090)). These details reinforce that Section 3 describes a single, well-defined evaluation configuration applied to the full test set of 2,169 sentences. The open-source implementation of the exact inference scheme is available in the SGNMT decoder under the `simpledfs` decoding strategy ([Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090)).

## 3. The Third-Party Note: 3,003 Sentences

### 3.1 What the Note Claims

The third-party research note states, in several places, that the full test set contains 3,003 sentences. It says that "The paper's main experiments use the entire English-German WMT news-test2015 test set of 3,003 sentences," that "The paper reports this size in its experimental setup," and that "This full test set size of 3,003 sentences is reported before any subset selection" ([Third-Party Research Note, n.d.](https://arxiv.org/abs/1908.10090)).

### 3.2 Problems with the Note's Figure

Several observations undermine the reliability of the 3,003 figure. First, the note claims the number is reported "in the paper's experimental setup," yet the primary source's experimental setup in Section 3 explicitly reports 2,169 sentences ([Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090)). Second, the note offers no page, section, table, or quotation from the paper to substantiate 3,003; it simply restates the number multiple times as a self-contained assertion ([Third-Party Research Note, n.d.](https://arxiv.org/abs/1908.10090)). Third, the note's descriptions of the language pair ("English-German") and benchmark type ("news test set") are consistent with the paper, meaning that the discrepancy is isolated to the numeric value rather than to a difference in test sets. This pattern—correct qualitative details with an unverifiable quantitative value—is characteristic of a secondary source that has introduced an error in transcription or recall rather than one describing a genuinely different benchmark.

## 4. Resolving the Discrepancy: Which Figure Is Authoritative?

When two sources conflict, the primary source should be preferred, particularly when it is the peer-reviewed paper under discussion and the secondary source is an unattributed research note. The table below summarizes the comparison.

| Criterion | Primary source (paper, Section 3) | Third-party note |
|---|---|---|
| Reported full test set size | 2,169 sentences | 3,003 sentences |
| Explicit benchmark named | English–German WMT news-test2015 | English–German WMT news-test2015 |
| Stated as "entire" test set | Yes | Yes |
| Evidence provided | Direct quotation in experimental setup | Repeated assertion only |
| Consistency with abstract | Consistent ("entire WMT15 English-German test set") | Not corroborated by the paper |
| Internal consistency | Used consistently with subset percentages | Contradicts the paper's own number |

**Source:** ([Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090); [Third-Party Research Note, n.d.](https://arxiv.org/abs/1908.10090)).

On the basis of this comparison, the defensible conclusion is that **the full English–German WMT news-test2015 test set used in this study comprises 2,169 sentences**, and that the 3,003 value in the secondary note is an error. This conclusion is further supported by the fact that the paper's own subset percentages are internally coherent with a 2,169-sentence total, as shown in the next section, whereas a 3,003-sentence base would imply substantially different absolute subset sizes.

## 5. Subset Sizes in the Length-Constrained Experiments

### 5.1 What the Paper Reports

The paper explicitly distinguishes the full test set from the subsets used in the length-constrained analysis. In Section 4 ("Results with Length Constraints"), the authors explain that "all results in this section are conducted on only a subset of the test set to keep the runtime under control," because constraining search lowers the γ-bounds and therefore increases runtime ([Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090)). The paper reports that one experiment—the histogram with a minimum translation length constraint of 0.25 times the source sentence length—was "conducted on 73.0% of the test set," while the experiments reported in Table 3 and Table 4 were "conducted on 48.3% of the test set" ([Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090)). The authors also note that they stopped decoding if a single sentence took longer than a day on a single CPU ([Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090)).

### 5.2 Estimated Absolute Subset Sizes

If the full test set is 2,169 sentences, the reported percentages translate into the following approximate absolute counts:

| Experimental block | Share of test set | Approximate sentence count (base = 2,169) | Source |
|---|---|---|---|
| Results without length constraints (Tables 1–2, Figures 1–4) | 100% (entire set) | 2,169 | ([Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090)) |
| Minimum-length constraint histogram (Figure 5) | 73.0% | ≈ 1,583 | ([Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090)) |
| Length-constrained exact search (Table 3) | 48.3% | ≈ 1,048 | ([Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090)) |
| Exact search with/without length normalization (Table 4) | 48.3% | ≈ 1,048 | ([Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090)) |

These estimates are derived by multiplying the reported percentages by the paper's stated full test set size of 2,169 and are therefore themselves dependent on the correctness of that base figure. They illustrate the internal logic of the paper: the full-set experiments in Section 3 cover all 2,169 sentences, while the computationally expensive constrained experiments in Section 4 cover only a subset, precisely because lower γ-bounds make the depth-first search slower ([Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090)).

## 6. Why the Test Set Size Matters for Interpreting the Results

The reported size is not merely a descriptive detail; it underpins the interpretation of every headline percentage in the paper. For the full English–German WMT news-test2015 test set of 2,169 sentences, the study reports that greedy decoding produced a BLEU score of 29.3 with a length ratio of 1.02, 73.6% search errors, and 0.0% empty translations; Beam-10 produced a BLEU of 30.3, a length ratio of 1.00, 57.7% search errors, and 0.0% empty translations; and exact search produced a BLEU of only 2.1, a length ratio of 0.06, 0.0% search errors, and 51.8% empty translations ([Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090)). The paper further reports that even a beam size of 100 produces 53.62% search errors, and that Beam-10 yields 15.9 percentage points fewer search errors than greedy decoding (57.68% versus 73.58%) ([Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090)).

These percentages are meaningful because they are computed over the complete 2,169-sentence benchmark, which is what allows the authors to claim that "beam search does not find the global best model score for more than half of the sentences" and that "for 51.8% of the sentences, NMT assigns the global best model score to the empty translation" ([Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090)). If the denominator were 3,003 rather than 2,169, the absolute number of affected sentences implied by these percentages would change by roughly 38%, which would materially alter the scale of the reported failure. The paper's own framing—that a sentence is classified as a search error if the decoder does not find the global best model score—therefore depends on the correct identification of the 2,169-sentence full test set ([Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090)).

The paper also demonstrates that the phenomenon generalizes across architectures. Table 2 reports Beam-10 search errors and empty-translation rates for an LSTM (58.4% search errors, 47.7% empty), SliceNet (46.0%, 41.2%), Transformer-Base (57.7%, 51.8%), and Transformer-Big (32.1%, 25.8%) ([Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090)). These per-model figures are reported against the same evaluation setup, reinforcing that the 2,169-sentence full test set is the common denominator for the unconstrained analyses.

## 7. Conclusion

The question "what is the test set size?" has a clear answer when the primary source is given its proper weight: the full English–German WMT news-test2015 test set used in Stahlberg and Byrne's study contains **2,169 sentences**, as stated explicitly in Section 3 of the paper ([Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090)). The third-party research note's repeated claim of 3,003 sentences is not supported by any quotation or location in the paper and directly contradicts the paper's own experimental setup; it should therefore be regarded as an unreliable secondary figure ([Third-Party Research Note, n.d.](https://arxiv.org/abs/1908.10090)). Researchers citing this work should use 2,169 sentences for the full test set, and, where relevant, note that the length-constrained experiments were run on subsets corresponding to 73.0% and 48.3% of that full set, i.e., approximately 1,583 and 1,048 sentences respectively ([Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090)).

## References

Stahlberg, F., & Byrne, B. (2019). *On NMT search errors and model errors: Cat got your tongue?* arXiv. https://arxiv.org/abs/1908.10090

Third-party research note on *On NMT search errors and model errors: Cat got your tongue?* (n.d.). https://arxiv.org/abs/1908.10090