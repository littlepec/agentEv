# Determining the Test Set Size in “On NMT Search Errors and Model Errors: Cat Got Your Tongue?”

## Executive Summary

The question “what is the test set size?” requires resolving a direct conflict between the primary source and a third-party research note. The primary source, the original paper by Stahlberg and Byrne, explicitly reports that the main experiments without length constraints were conducted on the entire English-German WMT news-test2015 test set, which contains **2,169 sentences** ([Stahlberg & Byrne, 2019](document_1.txt)). A third-party research note instead claims that the same test set contains **3,003 sentences** ([Third-party research note, n.d.](document_2.txt)). After weighing the reliability of these sources, the primary source must take precedence. Therefore, the test set size for the paper’s main exact inference experiments is **2,169 sentences**.

This report explains the evidence, compares the conflicting claims, analyzes why the discrepancy matters, and provides a clear recommendation for interpreting the paper’s results.

## Primary Source Evidence: The Original Paper

The original paper is the most authoritative source for its own experimental setup. In Section 3, titled “Results without Length Constraints,” the authors state: “We conduct all our experiments in this section on the entire English-German WMT news-test2 0 1 5 test set (2,1 6 9 sentences)” ([Stahlberg & Byrne, 2019](document_1.txt)). The spacing in the provided text reflects OCR artifacts, but the number is unambiguous: 2,169. This explicit statement appears in the experimental setup before any subset selection is discussed.

The paper further specifies that the model used is a Transformer base model trained with Tensor2Tensor on parallel WMT18 data excluding ParaCrawl ([Stahlberg & Byrne, 2019](document_1.txt)). Pre-processing includes joint subword segmentation using byte pair encoding with 32K merges, and the authors report cased BLEU scores ([Stahlberg & Byrne, 2019](document_1.txt)). These details confirm that the 2,169-sentence test set is the full evaluation set for the main exact inference comparisons.

Table 1 in the paper reports results for Greedy, Beam-10, and Exact search on this full test set ([Stahlberg & Byrne, 2019](document_1.txt)). For example, Greedy achieves 29.3 BLEU, 73.6% search errors, and 0.0% empty translations; Beam-10 achieves 30.3 BLEU, 57.7% search errors, and 0.0% empty translations; Exact search achieves 2.1 BLEU, 0.0% search errors, and 51.8% empty translations ([Stahlberg & Byrne, 2019](document_1.txt)). These percentages and scores are computed over the 2,169 sentences that constitute the full test set.

The paper also reports additional architectures in Table 2, including LSTM, SliceNet, Transformer-Base, and Transformer-Big ([Stahlberg & Byrne, 2019](document_1.txt)). The text indicates that these experiments are part of the same section and therefore use the same full test set of 2,169 sentences. For instance, Transformer-Base has 51.8% empty translations, and Transformer-Big has 25.8% empty translations ([Stahlberg & Byrne, 2019](document_1.txt)). These figures are only meaningful if we know the underlying test set size, which the primary source provides as 2,169.

## Third-Party Note Evidence: The Conflicting Claim

The third-party research note presents a different figure. It states: “The paper's main experiments use the entire English-German WMT news-test2015 test set of 3,003 sentences” ([Third-party research note, n.d.](document_2.txt)). This claim is repeated multiple times throughout the note. It also asserts that “The entire English-German WMT news-test2015 test set contains 3,003 sentences” and that “The paper reports this size in its experimental setup” ([Third-party research note, n.d.](document_2.txt)).

The note further describes the length-constrained experiments as using subsets of the test set. It reports that “One experiment uses 73.0% of the test set. Other experiments use 48.3% of the test set” ([Third-party research note, n.d.](document_2.txt)). It emphasizes that these subsets are distinct from the full test set size, which it claims is 3,003 sentences ([Third-party research note, n.d.](document_2.txt)).

This third-party note is clearly secondary. It is not the original paper, and its repeated assertion of 3,003 sentences directly contradicts the primary source’s explicit statement of 2,169 sentences. In academic research, primary sources are generally more reliable than secondary summaries, especially for specific experimental details such as dataset sizes.

## Comparative Analysis of the Two Sources

The conflict between the two sources is significant and cannot be reconciled by assuming both are correct. Table 1 summarizes the discrepancy.

**Table 1. Comparison of reported test set sizes**

| Source | Reported Test Set Size | Context | Source Type |
|--------|------------------------|---------|-------------|
| document_1.txt (Stahlberg & Byrne, 2019) | 2,169 sentences | Entire English-German WMT news-test2015 test set used in Section 3 without length constraints | Primary (original paper) |
| document_2.txt (Third-party research note, n.d.) | 3,003 sentences | Claimed main experiments test set | Third-party research note |

The primary source is the actual paper text, and it states the size directly in the experimental setup. The third-party note is a summary that may have confused the WMT15 news-test2015 English-German test set with another dataset or another year’s test set. For example, WMT14 English-German test sets are often reported as containing around 3,003 sentences, whereas WMT15 English-German news-test2015 is widely known to contain 2,169 sentences. The third-party note’s figure of 3,003 is therefore likely a misattribution.

Given the explicit wording of the primary source, the correct test set size for the paper’s main experiments is **2,169 sentences**. The third-party note’s claim of 3,003 sentences should be regarded as unreliable for this specific detail.

## Why the Test Set Size Matters

The test set size is not a trivial detail. It affects the interpretation of every percentage, count, and BLEU score reported in the paper. For example, the paper reports that under exact search, 51.8% of sentences receive the empty translation as the global best model score ([Stahlberg & Byrne, 2019](document_1.txt)). If the test set has 2,169 sentences, this corresponds to approximately 1,124 sentences. If the test set had 3,003 sentences, it would correspond to approximately 1,556 sentences. The absolute magnitude of the empty translation problem changes substantially depending on which number is used.

Similarly, the paper reports that Beam-10 produces 57.7% search errors ([Stahlberg & Byrne, 2019](document_1.txt)). On 2,169 sentences, that is about 1,252 sentences. On 3,003 sentences, it would be about 1,733 sentences. The paper’s central claim—that beam search does not find the global best model score for more than half of the sentences—remains true in either case, but the precise scale of the problem depends on the correct test set size.

The size also matters for the length-constrained experiments. The paper states that all results in the “Results with Length Constraints” section are conducted on only a subset of the test set to keep runtime under control ([Stahlberg & Byrne, 2019](document_1.txt)). It reports that one experiment uses 73.0% of the test set, while Table 3 and Table 4 experiments use 48.3% of the test set ([Stahlberg & Byrne, 2019](document_1.txt)). If the full test set is 2,169 sentences, then 73.0% is approximately 1,583 sentences, and 48.3% is approximately 1,048 sentences. If the full test set were 3,003 sentences, those subsets would be approximately 2,192 and 1,450 sentences, respectively. The smaller subset sizes are more consistent with the paper’s stated runtime constraints, including the decision to stop decoding if a single sentence took longer than a day on a single CPU ([Stahlberg & Byrne, 2019](document_1.txt)).

**Table 2. Subset sizes under the two competing full test set sizes**

| Experiment | Percentage of Test Set | If Full Test Set = 2,169 | If Full Test Set = 3,003 |
|------------|------------------------|--------------------------|---------------------------|
| Figure 5 (minimum length constraint 0.25) | 73.0% | ~1,583 sentences | ~2,192 sentences |
| Table 3 and Table 4 (exact search under length constraints) | 48.3% | ~1,048 sentences | ~1,450 sentences |

The primary source’s 2,169-sentence figure is consistent with the known scale of the WMT15 English-German news test set and with the computational demands described in the paper. The third-party note’s 3,003-sentence figure would imply a larger experimental scale that is not supported by the paper’s own text.

## The Role of the Test Set in the Paper’s Experimental Design

The paper’s central contribution is an exact inference procedure for neural sequence models based on a combination of beam search and depth-first search ([Stahlberg & Byrne, 2019](document_1.txt)). This exact search exploits the monotonicity of NMT scores: since conditional log-probabilities are always negative, partial hypotheses can be safely discarded once their score drops below the log-probability of any complete hypothesis ([Stahlberg & Byrne, 2019](document_1.txt)). This procedure is computationally expensive, which is why the authors use the full test set for the unconstrained experiments and only subsets for the length-constrained experiments.

The paper’s main result is that beam search fails to find the global best model score for more than half of the sentences, and that for more than 50% of sentences, the model assigns its global best score to the empty translation ([Stahlberg & Byrne, 2019](document_1.txt)). This finding is based on the full test set of 2,169 sentences. The paper also shows that large beam sizes reduce search errors but cause BLEU to drop because translations become too short ([Stahlberg & Byrne, 2019](document_1.txt)). Even a beam size of 100 produces 53.62% search errors ([Stahlberg & Byrne, 2019](document_1.txt)). These results are all anchored to the 2,169-sentence test set.

The paper further demonstrates that the problem of empty translations is not specific to the Transformer base model. Table 2 shows that LSTM, SliceNet, Transformer-Base, and Transformer-Big all exhibit substantial empty translation rates, with Transformer-Big still having 25.8% empty translations ([Stahlberg & Byrne, 2019](document_1.txt)). These experiments are also conducted on the same full test set, reinforcing the importance of the 2,169-sentence figure.

## Methodological Implications of the Discrepancy

The discrepancy between the primary source and the third-party note has methodological implications for anyone attempting to replicate or extend the paper’s findings. If a researcher relies on the third-party note and assumes the test set has 3,003 sentences, they will miscalculate the absolute number of search errors and empty translations. They may also misjudge the computational resources required for exact inference. For example, the paper’s length-constrained exact search is already computationally intensive, and the authors note that they stopped decoding if the decoder took longer than a day for a single sentence on a single CPU ([Stahlberg & Byrne, 2019](document_1.txt)). A larger test set would exacerbate this problem, making the reported subset percentages even more critical.

Moreover, the third-party note’s claim that the full test set size is 3,003 sentences is repeated multiple times, which could lend it undue credibility if readers do not consult the primary source. This is a cautionary example of why secondary sources should always be checked against the original paper for specific numerical details.

## Conclusion

The test set size for the main experiments in “On NMT Search Errors and Model Errors: Cat Got Your Tongue?” is **2,169 sentences**. This figure comes directly from the primary source, which states: “We conduct all our experiments in this section on the entire English-German WMT news-test2 0 1 5 test set (2,1 6 9 sentences)” ([Stahlberg & Byrne, 2019](document_1.txt)). The third-party research note’s claim of 3,003 sentences is inconsistent with the primary source and should not be used ([Third-party research note, n.d.](document_2.txt)).

When answering the question “what is the test set size?”, the most reliable response is therefore **2,169 sentences** for the full test set, with length-constrained experiments using subsets of 73.0% and 48.3% of that full set, corresponding to approximately 1,583 and 1,048 sentences, respectively. Researchers and readers should prioritize the primary source for this and any other experimental detail.

## References

Stahlberg, F., & Byrne, B. (2019). *On NMT Search Errors and Model Errors: Cat Got Your Tongue?* [document_1.txt]. Retrieved from document_1.txt

Third-party research note. (n.d.). *On NMT Search Errors and Model Errors: Cat Got Your Tongue?* [document_2.txt]. Retrieved from document_2.txt