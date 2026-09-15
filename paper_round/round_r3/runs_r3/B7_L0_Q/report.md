# Test Set Size in Stahlberg and Byrne's Study of NMT Search and Model Errors

## Introduction

The question of how large a test set is in a neural machine translation (NMT) study is not a trivial methodological detail: it determines the statistical weight that can be placed on reported error rates, the generalizability of findings across sentence lengths, and the extent to which observed phenomena such as empty translations reflect a systematic modelling failure rather than an artifact of a small sample. The paper under discussion, "On NMT Search Errors and Model Errors: Cat Got Your Tongue?" by Felix Stahlberg and Bill Byrne of the University of Cambridge, reports experiments on a well-known shared-task benchmark and provides explicit statements about the number of sentences used in each experimental setting ([Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090)). This report consolidates the available evidence on the test set size, distinguishes the full test set from the subsets used in later experiments, and discusses the implications of these figures for the paper's conclusions.

## The Reported Test Set Size

### The Primary Figure: 2,169 Sentences

The full test set used in the paper's main experiments contains **2,169 sentences**. The authors state that they conduct all experiments in their "Results without Length Constraints" section "on the entire English-German WMT news-test2015 test set (2,169 sentences)" ([Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090)). This figure is reported before any subset selection occurs, and it therefore constitutes the definitive full test set size for the study.

An independent third-party research note accompanying the paper reiterates this figure, stating that "the entire German-English WMT news-test2015 test set contains 2,169 sentences" and that "this full test set size of 2,169 sentences is reported before any subset selection" ([Third-party research note, n.d.](https://arxiv.org/abs/1908.10090)). The agreement between the primary source and the secondary note strengthens confidence in the number.

### Provenance and Experimental Setup

The 2,169-sentence test set is drawn from the WMT news-test2015 shared translation task. The abstract of the paper refers to this resource as "the entire WMT15 English-German test set," and the experiments use a Transformer base model trained with Tensor2Tensor on parallel WMT18 data excluding ParaCrawl ([Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090)). Pre-processing follows the authors' earlier WMT18 system description and includes joint subword segmentation using byte pair encoding with 32,000 merges. The authors report cased BLEU scores, noting that these are comparable to those published on the statmt.org matrix ([Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090)). Because the test set is a standard, publicly documented news-translation benchmark, the 2,169-sentence figure also allows direct comparison with other systems evaluated on the same data.

## Language Pair and Test Set Identity

A minor but noteworthy inconsistency exists across the sources regarding the direction of the language pair. The paper's abstract and experimental section refer to the "English-German" WMT news-test2015 test set, while the third-party research note describes the same resource as the "German-English WMT news-test2015 test set" ([Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090); [Third-party research note, n.d.](https://arxiv.org/abs/1908.10090)). This discrepancy concerns labelling only, not the size of the data: both sources identify the same 2,169-sentence WMT news-test2015 resource. Researchers citing this work should follow the primary paper's designation while being aware of the alternative phrasing in derivative notes.

## Full Test Set Versus Experimental Subsets

### Two Distinct Experimental Regimes

The paper is organized into two results regimes with different test set coverage. This distinction is essential for interpreting any reported percentage. The third-party note makes the separation explicit: the full test set of 2,169 sentences supports the exact inference comparisons in the section without length constraints, whereas the length-constrained exact search experiments use only a subset of the test set to keep runtimes manageable ([Third-party research note, n.d.](https://arxiv.org/abs/1908.10090)).

The rationale for subsetting is computational. Constraining exact search to particular translation lengths lowers the pruning bounds, which increases runtime; the authors report that they stopped decoding if the decoder took longer than a day for a single sentence on a single CPU, and they note that unconstrained exact search is much faster and requires no such maximum execution time limit ([Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090)).

### Table 1: Test Set Coverage by Experiment

| Section of the paper | Test set coverage | Approximate sentence count | Source |
|---|---|---|---|
| Results without length constraints (main tables) | Entire test set | 2,169 sentences | ([Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090)) |
| Length-ratio histogram with minimum length constraint (Fig. 5) | 73.0% of the test set | ≈1,583 sentences (derived) | ([Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090)) |
| Exact search under length constraints (Tables 3 and 4) | 48.3% of the test set | ≈1,048 sentences (derived) | ([Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090)) |

The approximate sentence counts in the final column are arithmetic derivations from the reported percentages and the stated full test set size of 2,169 sentences; they are not stated verbatim in the source. The percentages themselves — 73.0% and 48.3% — are reported directly in the paper's figure and table captions ([Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090)).

## Results Obtained on the Full 2,169-Sentence Test Set

Understanding what was measured on the full test set clarifies why the 2,169-sentence figure matters. The paper's central result appears in its first table, which reports three decoding strategies evaluated on the entire test set.

### Table 2: Main Results on the Full Test Set (2,169 Sentences)

| Search method | BLEU | Length ratio | Search errors | Empty translations |
|---|---|---|---|---|
| Greedy | 29.3 | 1.02 | 73.6% | 0.0% |
| Beam-10 | 30.3 | 1.00 | 57.7% | 0.0% |
| Exact | 2.1 | 0.06 | 0.0% | 51.8% |

The values above are reported in the paper's first results table and discussed in the corresponding text ([Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090)). The exact-search row is the most striking: when the decoder is guaranteed to return the global best model score, the BLEU score collapses to 2.1 and the length ratio falls to 0.06, because the model assigns its globally best score to the empty translation for 51.8% of sentences. Applied to the full test set, 51.8% corresponds to approximately 1,124 sentences for which the empty hypothesis is optimal under the model (derived from the reported percentage and the 2,169-sentence total). The authors describe this as "a massive failure of neural models in properly accounting for adequacy" ([Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090)).

The same full test set also supports the paper's analysis of beam width. The authors report that even a beam size of 100 produces 53.62% search errors, and that Beam-10 reduces search errors by 15.9 percentage points in absolute terms relative to greedy decoding (57.68% versus 73.58%) while Beam-100 improves search only slightly despite being ten times slower ([Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090)). These figures are all computed over the 2,169-sentence test set.

### Cross-Architecture Comparison

The paper further shows that the phenomenon is not specific to the Transformer base architecture. Its second table compares four systems under Beam-10 search and exact search.

### Table 3: Search Errors and Empty Translations Across Architectures

| Model | Beam-10 BLEU | Search errors | Empty translations |
|---|---|---|---|
| LSTM | 28.6 | 58.4% | 47.7% |
| SliceNet | 28.8 | 46.0% | 41.2% |
| Transformer-Base | 30.3 | 57.7% | 51.8% |
| Transformer-Big | 31.7 | 32.1% | 25.8% |

The figures are the paper's reported values, with the starred systems described as strong baselines from a WMT18 shared task submission ([Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090)). The authors emphasize that "even a highly optimized Transformer Big model from our WMT18 shared task submission has 25.8% empty translations," which demonstrates that the modelling deficiency persists across architectures rather than being an artifact of a single configuration ([Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090)).

## Why the Subsets Produce Different BLEU Values

A reader comparing the tables may notice an apparent tension: Beam-10 achieves BLEU 30.3 on the full test set but BLEU 37.0 on the 48.3% subset used for the length-constrained experiments. This difference is explained by the fact that the length-constrained experiments operate on a restricted portion of the test set, and the authors explicitly justify this restriction on runtime grounds ([Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090)). Within that subset, exact search constrained to the Beam-10 hypothesis length exactly matches beam search (BLEU 37.0, ratio 1.00), while constraining exact search to the reference length yields an oracle improvement of 0.9 BLEU points (37.9) ([Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090)). Similarly, under length normalization on the same 48.3% subset, Beam-10 reaches BLEU 36.3 with a length ratio of 1.03, Beam-30 reaches BLEU 36.7 with a ratio of 0.98, and exact search reaches BLEU 36.4 with a ratio of 1.03 — a pattern the authors interpret as evidence that length normalization corrects the length deficiency but does not fix the underlying modelling problem ([Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090)).

## Reliability and Significance of the Reported Size

The 2,169-sentence figure comes from the primary research paper itself, which is the most authoritative source available on this question ([Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090)). The third-party research note corroborates the number and adds the useful clarification that it is stated before any subset selection ([Third-party research note, n.d.](https://arxiv.org/abs/1908.10090)). Both sources are therefore consistent, and the primary source takes precedence for any disputed detail.

The size of 2,169 sentences is moderate by modern NMT standards but is adequate for the paper's purpose, which is diagnostic rather than comparative. Because the empty-translation phenomenon occurs for roughly half of all sentences, and because long source sentences are disproportionately affected — the authors report that the globally best translation is empty for almost all sentences longer than 40 tokens — the full test set provides sufficient statistical resolution to establish the pattern ([Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090)). At the same time, the fact that the length-constrained analyses had to be reduced to 73.0% and 48.3% of the test set illustrates a practical limitation: exact inference over constrained search spaces is expensive, and the paper's most granular length analyses rest on roughly half of the available data ([Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090); [Third-party research note, n.d.](https://arxiv.org/abs/1908.10090)).

## Conclusion

The test set size reported in Stahlberg and Byrne's study is **2,169 sentences**, corresponding to the entire WMT news-test2015 English-German test set used for the main experiments on exact inference, search errors, and empty translations ([Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090)). This figure is stated before any subsetting and is confirmed by an independent research note ([Third-party research note, n.d.](https://arxiv.org/abs/1908.10090)). The length-constrained exact search experiments use smaller subsets — 73.0% of the test set for the minimum-length-constraint histogram and 48.3% for the length-constrained and length-normalized tables — a reduction imposed by the computational cost of exact decoding under looser pruning bounds ([Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090)). Any interpretation of the paper's percentage-based findings should therefore specify whether the denominator is the full 2,169-sentence test set or one of these reduced subsets, because the two regimes yield substantially different BLEU values and support different levels of statistical confidence.

## References

Stahlberg, F., & Byrne, B. (2019). *On NMT search errors and model errors: Cat got your tongue?* arXiv. https://arxiv.org/abs/1908.10090

Third-party research note: On NMT search errors and model errors: Cat got your tongue? (n.d.). https://arxiv.org/abs/1908.10090