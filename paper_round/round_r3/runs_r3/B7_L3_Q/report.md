# Test Set Size in Stahlberg and Byrne’s NMT Search Error Study

## Executive Summary

The test set size reported in the primary source and corroborated by the third-party research note is **2,169 sentences**. This figure refers to the **entire WMT news-test2015 test set** used in the paper’s main experiments without length constraints ([Stahlberg & Byrne, n.d.](document_1.txt); [Third-party research note, n.d.](document_2.txt)). The paper also reports that its length-constrained exact search experiments were conducted on **subsets** of this full test set: one experiment used **73.0%** of the test set, and other experiments used **48.3%** of the test set ([Stahlberg & Byrne, n.d.](document_1.txt); [Third-party research note, n.d.](document_2.txt)). Therefore, the most direct and defensible answer to the query “what is the test set size?” is **2,169 sentences** for the full test set, with the important qualification that several later analyses use smaller subsets.

## Direct Answer and Source Basis

The primary source states that the paper’s main experiments are conducted on “the entire English-German WMT news-test2015 test set (2,169 sentences)” ([Stahlberg & Byrne, n.d.](document_1.txt)). The same source reports in the abstract that the exact search is used to find global best model scores “for the entire WMT15 English-German test set” ([Stahlberg & Byrne, n.d.](document_1.txt)). This establishes the full test set size as 2,169 sentences.

The third-party research note independently confirms that “the entire German-English WMT news-test2015 test set contains 2,169 sentences” and that “the paper states the test set size as a number of sentences” ([Third-party research note, n.d.](document_2.txt)). The note also clarifies that “this full test set size of 2,169 sentences is reported before any subset selection” ([Third-party research note, n.d.](document_2.txt)). Thus, both the primary paper and the third-party note agree on the numeric size, even though they describe the language direction slightly differently.

One terminological inconsistency should be noted: the primary source calls it an **English-German** test set, while the third-party note calls it **German-English** ([Stahlberg & Byrne, n.d.](document_1.txt); [Third-party research note, n.d.](document_2.txt)). The reported sentence count remains the same. For the purpose of answering the test set size query, the language-direction label does not change the size figure.

## Full Test Set Used in the Main Experiments

### Results Without Length Constraints

The paper divides its empirical work into two broad sections: results without length constraints and results with length constraints. The first section, which contains the main exact inference comparisons, uses the entire test set. The primary source states: “We conduct all our experiments in this section on the entire English-German WMT news-test2015 test set (2,169 sentences)” ([Stahlberg & Byrne, n.d.](document_1.txt)). The third-party note reinforces this by stating that “all experiments in the results without length constraints section are conducted on the entire German-English WMT news-test2015 test set (2,169 sentences)” ([Third-party research note, n.d.](document_2.txt)).

This full-set design is significant because the paper’s central claims about search errors and model errors depend on exact inference rather than approximate beam search. The authors use exact search to find the global best model scores under a Transformer base model, and they report that beam search fails to find those global best scores in most cases, even with a beam size of 100 ([Stahlberg & Byrne, n.d.](document_1.txt)). The full test set of 2,169 sentences provides the basis for those comparisons.

### Why the Full Set Matters for Interpretation

The full test set size of 2,169 sentences is the denominator for the paper’s headline statistics. For example, the paper reports that for more than 50% of the sentences, the model assigns its global best score to the empty translation ([Stahlberg & Byrne, n.d.](document_1.txt)). It also reports that greedy search has a search-error rate of 73.6%, Beam-10 has 57.7%, and exact search has 0.0% search errors on this full set ([Stahlberg & Byrne, n.d.](document_1.txt)). These percentages are meaningful because they are computed over the entire 2,169-sentence test set in the unconstrained setting.

The third-party note emphasizes that the full test set size “supports the paper’s exact inference comparisons for neural machine translation search errors and model errors” ([Third-party research note, n.d.](document_2.txt)). In other words, the 2,169-sentence figure is not a minor detail; it is the basis for the paper’s quantitative conclusions about how often beam search fails and how often the empty translation receives the best model score.

## Subset Sizes for Length-Constrained Exact Search

### The 48.3% Subset

The paper’s length-constrained exact search results use only a portion of the test set. The primary source states that “all results in this section are conducted on only a subset of the test set to keep the runtime under control” ([Stahlberg & Byrne, n.d.](document_1.txt)). It then reports that the exact search experiments under length constraints in Table 3 were conducted on **48.3%** of the test set ([Stahlberg & Byrne, n.d.](document_1.txt)). Table 4, which concerns exact search under length normalization, is also reported as being conducted on **48.3%** of the test set ([Stahlberg & Byrne, n.d.](document_1.txt)). The third-party note confirms that “other experiments use 48.3% of the test set” ([Third-party research note, n.d.](document_2.txt)).

Applying that percentage to the full test set yields an approximate subset size of **1,048 sentences** (0.483 × 2,169 = 1,047.627). The paper itself does not state this absolute number in the provided text; the percentage is the reported figure. My conversion is a straightforward arithmetic derivation from the reported full-set size and subset percentage.

### The 73.0% Subset

A separate length-constrained analysis uses a larger subset. The primary source reports that the experiment associated with Figure 5, which uses a minimum translation length constraint of 0.25 times the source sentence length, was conducted on **73.0%** of the test set ([Stahlberg & Byrne, n.d.](document_1.txt)). The third-party note corroborates that “one experiment uses 73.0% of the test set” ([Third-party research note, n.d.](document_2.txt)).

Applying that percentage to the full test set yields an approximate subset size of **1,583 sentences** (0.730 × 2,169 = 1,583.37). Again, this absolute figure is derived rather than directly stated in the source; the reported value is 73.0%.

### Summary Table of Reported Test Set Sizes

| Experiment category | Reported portion of test set | Reported full-test-set size | Approximate sentence count |
|---|---:|---:|---:|
| Main experiments without length constraints | Entire test set | 2,169 sentences | 2,169 |
| Length-constrained analysis for Figure 5 | 73.0% | Not directly reported as a sentence count | ~1,583 |
| Length-constrained analyses in Tables 3 and 4 | 48.3% | Not directly reported as a sentence count | ~1,048 |

The full-set figure of 2,169 sentences is reported in both sources ([Stahlberg & Byrne, n.d.](document_1.txt); [Third-party research note, n.d.](document_2.txt)). The subset percentages are reported in the primary source ([Stahlberg & Byrne, n.d.](document_1.txt)) and corroborated by the third-party note ([Third-party research note, n.d.](document_2.txt)). The approximate sentence counts are calculated from those percentages.

## Why the Subsets Are Distinct from the Full Test Set Size

It is important not to confuse the full test set size with the subset sizes. The third-party note explicitly warns that “these subset experiments are distinct from the full test set size of 2,169 sentences” and that “the paper reports the full test set size as 2,169 sentences before any subset selection” ([Third-party research note, n.d.](document_2.txt)). Therefore, if a reader asks “what is the test set size?” in the context of the paper’s main experiments, the correct answer is **2,169 sentences**. If the reader is asking about the length-constrained exact search experiments, the answer is **48.3% or 73.0% of 2,169 sentences**, depending on the specific experiment.

The reason for using subsets is computational. The primary source explains that constraining search increases runtime because the lower bounds used for pruning become lower, and the authors “stopped decoding if the decoder took longer than a day for a single sentence on a single CPU” ([Stahlberg & Byrne, n.d.](document_1.txt)). Exact search without length constraints is faster and did not require maximum execution time limits ([Stahlberg & Byrne, n.d.](document_1.txt)). Thus, the full 2,169-sentence test set was computationally feasible for the unconstrained exact inference analysis, but the length-constrained analyses required smaller subsets to remain tractable.

## Implications for the Paper’s Findings

The test set size of 2,169 sentences is modest by modern standards but substantial for exact inference experiments. The paper’s exact search method combines beam search and depth-first search to guarantee finding the global best model score under the monotonicity of NMT scores ([Stahlberg & Byrne, n.d.](document_1.txt)). This guarantee makes the full test set especially valuable: unlike approximate beam search studies, the exact search results provide a reliable count of search errors and model errors over every sentence in the full set.

The full-set results show that beam search does not find the global best model score for more than half of the sentences, and that for 51.8% of the sentences, the global best model score is assigned to the empty translation ([Stahlberg & Byrne, n.d.](document_1.txt)). These findings are based on the entire 2,169-sentence test set. The length-constrained experiments on 73.0% and 48.3% subsets are then used to probe whether the empty-translation problem can be mitigated by imposing minimum translation lengths or by constraining search to the reference length ([Stahlberg & Byrne, n.d.](document_1.txt)). Those subset analyses are important, but they do not replace the full-set evidence.

## Conclusion

Based on the provided sources, the test set size in Stahlberg and Byrne’s study is **2,169 sentences**. This is the size of the entire WMT news-test2015 test set used for the main experiments without length constraints ([Stahlberg & Byrne, n.d.](document_1.txt); [Third-party research note, n.d.](document_2.txt)). The length-constrained exact search experiments use smaller portions of that test set: **73.0%** in one analysis and **48.3%** in others ([Stahlberg & Byrne, n.d.](document_1.txt); [Third-party research note, n.d.](document_2.txt)). Those subset sizes correspond approximately to 1,583 sentences and 1,048 sentences, respectively, if one converts the reported percentages using the full-set size. The most reliable and direct answer remains: **2,169 sentences** for the full test set.

## References

Stahlberg, F., & Byrne, B. (n.d.). *On NMT search errors and model errors: Cat got your tongue?* [document_1.txt](document_1.txt).

Third-party research note. (n.d.). *On NMT search errors and model errors: Cat got your tongue?* [document_2.txt](document_2.txt).