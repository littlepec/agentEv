# Test Set Size in Stahlberg and Byrne's "On NMT Search Errors and Model Errors: Cat Got Your Tongue?"

## Introduction

The question of how large a test set is can appear trivial, yet in empirical machine translation (MT) research it is a consequential methodological detail: it determines the statistical weight of reported search-error and model-error percentages, the feasibility of exact inference, and the comparability of a study with prior work. The study under examination here, "On NMT Search Errors and Model Errors: Cat Got Your Tongue?" by Felix Stahlberg and Bill Byrne of the University of Cambridge, Department of Engineering, investigates search errors and model errors in neural machine translation (NMT) using an exact inference procedure that combines beam search with depth-first search ([Stahlberg & Byrne, n.d.-a](document_1.txt)). The abstract states that the authors "use our exact search to find the global best model scores under a Transformer base model for the entire WMT15 English-German test set," and that beam search fails to find those global best scores in most cases, even with a beam size of 100 ([Stahlberg & Byrne, n.d.-a](document_1.txt)).

This report answers the query "what is the test set size?" by examining the two available sources: the primary paper text (document_1.txt) and a third-party research note (document_2.txt) prepared specifically to address test-set-size questions about this paper. Because the two sources report different figures, this report presents both, evaluates their relative reliability, and explains how the test set size varies across the paper's experimental conditions.

## The Reported Test Set Size: Primary Evidence

### The figure stated in the paper itself

In the experimental setup of the paper's Section 3 ("Results without Length Constraints"), the authors state that they "conduct all our experiments in this section on the entire English-German WMT news-test2015 test set (2,169 sentences)" using a Transformer base model trained with Tensor2Tensor on parallel WMT18 data excluding ParaCrawl ([Stahlberg & Byrne, n.d.-a](document_1.txt)). The same section specifies that preprocessing follows Stahlberg et al. (2018a) and includes joint subword segmentation using byte pair encoding with 32K merges, and that cased BLEU scores are reported ([Stahlberg & Byrne, n.d.-a](document_1.txt)). The abstract similarly refers to "the entire WMT15 English-German test set," and the paper points readers to an open-source implementation of the exact inference scheme available in the SGNMT decoder ([Stahlberg & Byrne, n.d.-a](document_1.txt)).

This 2,169-sentence figure is therefore the test set size as reported in the paper's own experimental description, and it is reported "before any subset selection" ([Stahlberg & Byrne, n.d.-a](document_1.txt)).

### The figure stated in the third-party research note

The third-party research note (document_2.txt), which lists among its key questions "NMT search errors model errors test set size," "English German news test set size neural machine translation," and "WMT news test set sentences exact inference NMT," reports a different figure. It states that "the paper's main experiments use the entire English-German WMT news-test2015 test set of 3,003 sentences," that "the entire English-German WMT news-test2015 test set contains 3,003 sentences," and that "the paper states the test set size as a number of sentences" ([Third-party research note, n.d.-b](document_2.txt)). The note further asserts that this full test set size of 3,003 sentences "is reported before any subset selection" and that it supports the paper's exact inference comparisons for NMT search errors and model errors ([Third-party research note, n.d.-b](document_2.txt)).

### Reconciling the discrepancy

The two sources are directly contradictory on the headline figure: 2,169 versus 3,003 sentences. Several considerations bear on which should be treated as authoritative:

1. **Source proximity.** Document_1.txt is the paper's own text, including its experimental setup statement; document_2.txt is a secondary note that paraphrases the paper ([Stahlberg & Byrne, n.d.-a](document_1.txt); [Third-party research note, n.d.-b](document_2.txt)).
2. **Internal consistency.** The primary text's sentence "We conduct all our experiments in this section on the entire English-German WMT news-test2015 test set (2,169 sentences)" is embedded within the paper's Section 3 methodology, immediately adjacent to descriptions of the Transformer base model, Tensor2Tensor training data, and BPE preprocessing ([Stahlberg & Byrne, n.d.-a](document_1.txt)).
3. **Subset arithmetic.** Both sources agree that the later, length-constrained experiments used only portions of the test set — 73.0% in one case and 48.3% in others ([Stahlberg & Byrne, n.d.-a](document_1.txt); [Third-party research note, n.d.-b](document_2.txt)). The primary text corresponds these percentages to the figures: the histogram in Figure 5 with a minimum translation length constraint of 0.25 times the source sentence length was "conducted on 73.0% of the test set," while Table 3 and Table 4 state "Experiment conducted on 48.3% of the test set" ([Stahlberg & Byrne, n.d.-a](document_1.txt)).

On the balance of the evidence, this report takes the position that **2,169 sentences is the test set size stated by the paper's own experimental setup**, and that the 3,003-sentence figure in the third-party note is best regarded as an unverified secondary claim that conflicts with the primary source. The note itself offers no supporting quotation from the paper beyond its assertion that "the paper reports this size in its experimental setup" ([Third-party research note, n.d.-b](document_2.txt)). Notably, the note's own framing — emphasizing that the full test set size is "reported before any subset selection" — parallels the paper's structure, but the number attached to that structure differs ([Third-party research note, n.d.-b](document_2.txt)). A plausible explanation is a misattribution to a different WMT release of the English–German news test data, although the provided sources contain no direct evidence on this point; this remains an interpretive observation rather than a documented fact.

## Test Set Size by Experimental Condition

The paper's evaluations do not all use the same number of sentences. The size depends on whether the experiment involves unconstrained or length-constrained exact search. The following table summarizes the structure reported across the sources.

| Experiment / section | Test data used | Sentences (if full set = 2,169) | Sentences (if full set = 3,003) |
|---|---|---|---|
| Section 3: results without length constraints | Entire English–German WMT news-test2015 test set | 2,169 | 3,003 |
| Figure 5: minimum-length constraint of 0.25 × source length | 73.0% of the test set | ≈1,583 | ≈2,192 |
| Tables 3 and 4: length-constrained exact search and oracle reference-length search | 48.3% of the test set | ≈1,048 | ≈1,450 |

The primary text reports that "all results in this section [with length constraints] are conducted on only a subset of the test set to keep the runtime under control," explaining that constraining search increases runtime because the γ-bounds are lower ([Stahlberg & Byrne, n.d.-a](document_1.txt)). The authors also note a hard computational stop: "We stopped decoding if the decoder took longer than a day for a single sentence on a single CPU," whereas exact search without length constraints "is much faster and does not need maximum execution time limits" ([Stahlberg & Byrne, n.d.-a](document_1.txt)). The third-party note corroborates this distinction, stating that "the length-constrained exact search experiments use only a subset of the test set" and that "these subset experiments are distinct from the full test set size ... before any subset selection" ([Third-party research note, n.d.-b](document_2.txt)).

## Why the Test Set Size Matters for This Study's Findings

The test set size is not a peripheral detail in this paper; it conditions the headline claims. The main results, reported in Table 1, compare Greedy, Beam-10, and Exact search on BLEU, length ratio, search errors, and empty translations ([Stahlberg & Byrne, n.d.-a](document_1.txt)). Among the reported figures:

- Greedy decoding achieves BLEU 29.3, a length ratio of 1.02, 73.6% search errors, and 0.0% empty translations.
- Beam-10 achieves BLEU 30.3, a length ratio of 1.00, 57.7% search errors, and 0.0% empty translations.
- Exact search achieves BLEU 2.1, a length ratio of 0.06, 0.0% search errors, and 51.8% empty translations.

These percentages are computed over the evaluation set, so a larger set would yield tighter confidence intervals around claims such as "for more than 50% of the sentences, the model in fact assigns its global best score to the empty translation" ([Stahlberg & Byrne, n.d.-a](document_1.txt)). The paper further reports that "even a large beam size of 100 produces 53.62% search errors," that Beam-10 yields 15.9% fewer search errors (absolute) than greedy decoding (57.68% vs. 73.58%), and that Beam-100 "improves search only slightly ... despite being 10 times slower than beam-10" ([Stahlberg & Byrne, n.d.-a](document_1.txt)). Each of these statistics is a proportion over the test set, and their evidentiary strength scales with the number of sentences evaluated.

The paper also generalizes beyond a single architecture. Table 2 reports results for a recurrent LSTM, SliceNet, Transformer-Base, and Transformer-Big, with search-error rates of 58.4%, 46.0%, 57.7%, and 32.1% respectively, and empty-translation rates of 47.7%, 41.2%, 51.8%, and 25.8% respectively ([Stahlberg & Byrne, n.d.-a](document_1.txt)). The fact that even a highly optimized Transformer-Big system from the authors' WMT18 shared-task submission has 25.8% empty translations underscores that the phenomenon is not an artifact of one model ([Stahlberg & Byrne, n.d.-a](document_1.txt)). The magnitude of these percentages over the 2,169-sentence (or 3,003-sentence) evaluation set is central to the authors' conclusion that "vanilla NMT in its current form requires just the right amount of beam search errors, which, from a modelling perspective, is a highly unsatisfactory conclusion indeed, as the model often prefers an empty translation" ([Stahlberg & Byrne, n.d.-a](document_1.txt)).

## Methodological Context of the Test Set

The paper's decoding setup also clarifies what "test set size" means operationally. The search space for NMT grows exponentially with sequence length; for a vocabulary of |T| = 32,000, there are "more possible translations with 20 words or less than atoms in the observable universe (32,000^20 ≫ 10^82)," so complete enumeration is impossible ([Stahlberg & Byrne, n.d.-a](document_1.txt)). Exact inference via depth-first search with admissible pruning is therefore computationally demanding, which is precisely why the length-constrained experiments were restricted to subsets. The BLEU scores are cased and comparable with matrix.statmt.org, and the implementation is available via the SGNMT decoder's `simpledfs` decoding strategy ([Stahlberg & Byrne, n.d.-a](document_1.txt)).

Additionally, the length-constrained results show that simply excluding the empty translation did not solve the underlying problem: constraining search to translations longer than 0.25 times the source length "still results in a peak in the (0.3, 0.5] cluster," suggesting "an inherent model bias towards shorter hypotheses [that] cannot be fixed with a length constraint" ([Stahlberg & Byrne, n.d.-a](document_1.txt)). The oracle experiment constraining exact search to the reference length improved BLEU by 0.9 points ([Stahlberg & Byrne, n.d.-a](document_1.txt)). Under length normalization, exact search no longer suffered from the length deficiency but "is not able to match our best BLEU score under Beam-10 search," indicating that length normalization "does not fix the fundamental modelling problem" ([Stahlberg & Byrne, n.d.-a](document_1.txt)).

## Conclusion

In answer to the query, the test set size reported in the paper's own experimental setup is **2,169 sentences**, corresponding to the entire English–German WMT news-test2015 test set ([Stahlberg & Byrne, n.d.-a](document_1.txt)). A third-party research note instead reports **3,003 sentences** as the size of the same test set ([Third-party research note, n.d.-b](document_2.txt)). Both sources agree that the length-constrained exact search experiments used only subsets — 73.0% and 48.3% of the test set — to control runtime ([Stahlberg & Byrne, n.d.-a](document_1.txt); [Third-party research note, n.d.-b](document_2.txt)).

Based on the available information, the most defensible reading is that the primary document's figure of 2,169 sentences should be treated as the paper's stated test set size, because it appears directly in the paper's Section 3 methodology and is embedded in a description of the model, training data, and preprocessing, whereas the 3,003-sentence figure appears only in a secondary note that provides no supporting quotation. Consequently, the length-constrained subsets correspond to approximately 1,583 sentences (73.0%) and 1,048 sentences (48.3%), assuming the 2,169-sentence base. Researchers citing this work should therefore verify the test set size against the paper's experimental section rather than relying on the secondary note, and should report the subset sizes explicitly when discussing the length-constrained findings, since those results rest on less than half of the full evaluation data and are subject to correspondingly wider uncertainty.

## References

Stahlberg, F., & Byrne, B. (n.d.-a). *On NMT search errors and model errors: Cat got your tongue?* [document_1.txt].

Third-party research note: *On NMT search errors and model errors: Cat got your tongue?* (n.d.-b). [document_2.txt].