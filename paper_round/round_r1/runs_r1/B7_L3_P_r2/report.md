# Test Set Size in Stahlberg and Byrne's NMT Search Error Study: A Detailed Report

## Executive Summary

The test set size at the center of Stahlberg and Byrne's investigation of search errors and model errors in neural machine translation (NMT) is **2,169 sentences** for the full English-German WMT news-test2015 test set used in the main experiments without length constraints ([Stahlberg & Byrne, 2019](document_1.txt)). This figure appears directly in the paper's experimental setup, where the authors state that all experiments in the "Results without Length Constraints" section were conducted on the entire English-German WMT news-test2015 test set of 2,169 sentences ([Stahlberg & Byrne, 2019](document_1.txt)). A secondary, third-party research note provided alongside the paper claims that the same test set contains **3,003 sentences** ([Third-party research note, n.d.](document_2.txt)). Because the primary source explicitly reports 2,169 sentences and the secondary note does not reproduce a direct quotation from the paper to support 3,003, the more reliable conclusion is that the full test set size is 2,169 sentences. The length-constrained exact-search experiments use only subsets of this full test set—specifically, 48.3% and 73.0%—to control runtime ([Stahlberg & Byrne, 2019](document_1.txt)).

## The Primary Source's Direct Statement

The most direct evidence about the test set size comes from the paper itself. In the section describing the experiments without length constraints, the authors write that they conduct all experiments "on the entire English-German WMT news-test2 0 1 5 test set (2,1 6 9 sentences)" ([Stahlberg & Byrne, 2019](document_1.txt)). The spacing in the retrieved text reflects OCR artifacts, but the number is clearly 2,169. The same source identifies the test set as the English-German WMT news-test2015 test set, and the abstract refers to the "entire WMT15 English-German test set" ([Stahlberg & Byrne, 2019](document_1.txt)). Thus, the paper's own reporting establishes 2,169 sentences as the full test set size before any subset selection.

This number is not merely a peripheral detail. It defines the denominator for the paper's headline percentages. For example, the paper reports that greedy decoding produces 73.6% search errors, Beam-10 produces 57.7% search errors, and exact search produces 0.0% search errors ([Stahlberg & Byrne, 2019](document_1.txt)). It also reports that exact search assigns the global best model score to the empty translation for 51.8% of sentences, causing BLEU to drop to 2.1 and length ratio to 0.06 ([Stahlberg & Byrne, 2019](document_1.txt)). All of these percentages are computed over the full test set described as 2,169 sentences in the unconstrained experimental setup ([Stahlberg & Byrne, 2019](document_1.txt)). If the test set size were different, the absolute number of affected sentences would change, even though the reported percentages would remain the same.

## The Conflicting Third-Party Claim

The third-party research note states, "The paper's main experiments use the entire English-German WMT news-test2015 test set of 3,003 sentences" and repeats that "The entire English-German WMT news-test2015 test set contains 3,003 sentences" ([Third-party research note, n.d.](document_2.txt)). The note further says that this "full test set size of 3,003 sentences is reported before any subset selection" ([Third-party research note, n.d.](document_2.txt)). This is in direct conflict with the primary source's 2,169 sentences ([Stahlberg & Byrne, 2019](document_1.txt)).

The third-party note also states that the length-constrained experiments use a subset of the test set, with one experiment using 73.0% and other experiments using 48.3% ([Third-party research note, n.d.](document_2.txt)). Those percentages match the primary source ([Stahlberg & Byrne, 2019](document_1.txt)), which suggests the note is drawing on the same paper. However, the full test set size that the note supplies—3,003—does not match the primary source. The note does not provide a direct quotation from the paper for the 3,003 figure, nor does it explain why the primary source would state 2,169 if 3,003 were correct. In the absence of corroborating evidence from the primary text, the 3,003 figure appears to be an error, a misreading, or a conflation with another WMT test set.

### Table 1. Comparison of Test Set Size Claims

| Source | Reported full test set size | Language pair | Test set | Subset usage reported |
|---|---:|---|---|---|
| Primary paper ([Stahlberg & Byrne, 2019](document_1.txt)) | **2,169 sentences** | English-German | WMT news-test2015 | Full set for unconstrained results; subsets for length-constrained results |
| Third-party note ([Third-party research note, n.d.](document_2.txt)) | 3,003 sentences | English-German | WMT news-test2015 | 73.0% and 48.3% of test set |

The table makes the conflict explicit. The primary source is the paper's own experimental description, while the secondary source is a research note. The secondary note is useful for highlighting the subset percentages, but its full test set size contradicts the primary source and should not be accepted without independent confirmation.

## Evaluating Reliability: Why the Primary Source Should Be Preferred

When two sources disagree about a factual parameter such as test set size, the appropriate method is to weigh the reliability and proximity of each source to the original experiment. The primary source—the paper by Stahlberg and Byrne—is the more reliable authority on its own experimental setup ([Stahlberg & Byrne, 2019](document_1.txt)). It reports the test set size in the context of describing how the experiments were run. The third-party note is a secondary summary that may have introduced a transcription or interpretation error ([Third-party research note, n.d.](document_2.txt)).

Several considerations support preferring 2,169 over 3,003:

1. **Directness.** The primary source states the size directly in the methods description: "entire English-German WMT news-test2 0 1 5 test set (2,1 6 9 sentences)" ([Stahlberg & Byrne, 2019](document_1.txt)). The third-party note asserts 3,003 without a direct quotation from the paper ([Third-party research note, n.d.](document_2.txt)).

2. **Internal consistency.** The primary source's abstract refers to the "entire WMT15 English-German test set" ([Stahlberg & Byrne, 2019](document_1.txt)). The experimental section then specifies the size of that WMT15 test set as 2,169 sentences ([Stahlberg & Byrne, 2019](document_1.txt)). There is no internal indication in the primary source that the test set is 3,003 sentences.

3. **Known WMT15 test set size.** Although the provided documents do not include an external WMT15 metadata file, the primary source's 2,169 figure is consistent with the paper's own reporting. The third-party note's 3,003 figure is not corroborated anywhere in the primary text.

4. **Source hierarchy.** In evidence-based reporting, primary sources generally outrank secondary summaries for factual parameters of the primary study. The third-party note is helpful for cross-checking, but when it conflicts with the primary paper, the paper's own statement should control ([Stahlberg & Byrne, 2019](document_1.txt); [Third-party research note, n.d.](document_2.txt)).

For these reasons, the defensible answer to the query "what is the test set size?" is **2,169 sentences** for the full English-German WMT news-test2015 test set used in the main experiments without length constraints ([Stahlberg & Byrne, 2019](document_1.txt)). The 3,003 figure reported in the third-party note is best treated as an inconsistency or probable error rather than as a correction to the primary source ([Third-party research note, n.d.](document_2.txt)).

## Full Test Set vs. Subsets in Length-Constrained Experiments

The paper does not use the full 2,169-sentence test set for every experiment. The length-constrained exact-search experiments are conducted on only a subset of the test set to keep runtime under control ([Stahlberg & Byrne, 2019](document_1.txt)). This is a crucial distinction: the full test set size is 2,169 sentences, but the length-constrained results are based on smaller portions of that set. The paper reports that one experiment was conducted on 73.0% of the test set, while other experiments in the length-constrained section were conducted on 48.3% of the test set ([Stahlberg & Byrne, 2019](document_1.txt); [Third-party research note, n.d.](document_2.txt)).

If the full test set is 2,169 sentences, these percentages correspond to approximately the following subset sizes. These derived counts are not explicitly stated in the paper as raw sentence counts, but they follow arithmetically from the reported percentages and the primary source's full test set size.

### Table 2. Derived Subset Sizes Based on the Primary Source's 2,169-Sentence Test Set

| Experiment | Reported subset percentage | Derived approximate sentence count | Source |
|---|---:|---:|---|
| Length-constrained experiment (Figure 5 context) | 73.0% | ≈ 1,583 sentences | ([Stahlberg & Byrne, 2019](document_1.txt); [Third-party research note, n.d.](document_2.txt)) |
| Length-constrained exact-search tables (Tables 3 and 4) | 48.3% | ≈ 1,048 sentences | ([Stahlberg & Byrne, 2019](document_1.txt); [Third-party research note, n.d.](document_2.txt)) |

If one instead used the third-party note's 3,003-sentence figure, the derived subset counts would be approximately 2,192 sentences for 73.0% and 1,450 sentences for 48.3%. However, because the primary source identifies the full test set as 2,169 sentences, the 2,169-based derivations are the ones consistent with the paper's own experimental description ([Stahlberg & Byrne, 2019](document_1.txt)). The subset percentages themselves are useful and are corroborated across the primary and secondary sources ([Stahlberg & Byrne, 2019](document_1.txt); [Third-party research note, n.d.](document_2.txt)).

## Why Test Set Size Matters for the Paper's Claims

The test set size is not merely a bookkeeping number. It determines the absolute number of sentences that exhibit search errors, empty translations, and length deficiencies. The paper's central finding is that beam search fails to find the global best model score for more than half of the sentences, even with a very large beam size of 100 ([Stahlberg & Byrne, 2019](document_1.txt)). It also finds that for more than 50% of sentences, the model assigns its global best score to the empty translation, revealing a massive failure of adequacy modeling ([Stahlberg & Byrne, 2019](document_1.txt)). These findings are computed over the full test set of 2,169 sentences in the unconstrained experiments ([Stahlberg & Byrne, 2019](document_1.txt)).

To illustrate the scale, Table 3 converts several headline percentages into approximate sentence counts using the 2,169-sentence denominator. These counts are derived from the reported percentages and are intended to show the practical meaning of the test set size.

### Table 3. Approximate Sentence Counts Implied by Reported Percentages over 2,169 Sentences

| Metric | Reported percentage | Derived approximate sentence count | Source |
|---|---:|---:|---|
| Greedy search errors | 73.6% | ≈ 1,596 sentences | ([Stahlberg & Byrne, 2019](document_1.txt)) |
| Beam-10 search errors | 57.7% | ≈ 1,252 sentences | ([Stahlberg & Byrne, 2019](document_1.txt)) |
| Beam-100 search errors | 53.62% | ≈ 1,163 sentences | ([Stahlberg & Byrne, 2019](document_1.txt)) |
| Exact search empty translations | 51.8% | ≈ 1,124 sentences | ([Stahlberg & Byrne, 2019](document_1.txt)) |
| Transformer-Big empty translations | 25.8% | ≈ 560 sentences | ([Stahlberg & Byrne, 2019](document_1.txt)) |

These derived counts reinforce why the paper's findings are significant. With 2,169 sentences, the claim that more than half the test set receives an empty translation under exact search means that over a thousand sentences are affected. If the test set were 3,003 sentences, the absolute counts would be larger, but the paper's own denominator and reported percentages point to the 2,169-sentence set ([Stahlberg & Byrne, 2019](document_1.txt)).

The paper also compares architectures. Under Beam-10 and exact search, the recurrent LSTM has 58.4% search errors and 47.7% empty translations; SliceNet has 46.0% search errors and 41.2% empty translations; Transformer-Base has 57.7% search errors and 51.8% empty translations; and Transformer-Big has 32.1% search errors and 25.8% empty translations ([Stahlberg & Byrne, 2019](document_1.txt)). These results demonstrate that the problems of search errors and empty translations are not specific to a single model architecture. They also depend on having a sufficiently large test set to estimate rates reliably. A 2,169-sentence test set provides a reasonable sample for sentence-level percentages, though the length-constrained experiments use smaller subsets because exact search under length constraints is computationally expensive ([Stahlberg & Byrne, 2019](document_1.txt)).

## Length Constraints, Runtime, and the Role of Subsets

The paper explains that constraining exact search to certain translation lengths increases runtime because the lower bounds become lower ([Stahlberg & Byrne, 2019](document_1.txt)). The authors stopped decoding if the decoder took longer than a day for a single sentence on a single CPU ([Stahlberg & Byrne, 2019](document_1.txt)). Exact search without length constraints is much faster and does not need maximum execution time limits ([Stahlberg & Byrne, 2019](document_1.txt)). This computational asymmetry explains why the full 2,169-sentence test set could be used for the unconstrained exact-search results, while the length-constrained experiments had to be restricted to subsets ([Stahlberg & Byrne, 2019](document_1.txt)).

The first length-constrained experiment restricted search to translations longer than 0.25 times the source sentence length, thereby excluding the empty translation from the search space ([Stahlberg & Byrne, 2019](document_1.txt)). Although this mitigated the empty-translation problem slightly, it still resulted in a peak in the (0.3, 0.5] length-ratio cluster, suggesting that the problem of empty translations is the consequence of an inherent model bias toward shorter hypotheses and cannot be fixed with a length constraint ([Stahlberg & Byrne, 2019](document_1.txt)). The authors then constrained exact search to either the length of the best Beam-10 hypothesis or the reference length ([Stahlberg & Byrne, 2019](document_1.txt)). Exact search constrained to the Beam-10 hypothesis length did not improve over beam search, suggesting that any search errors between the beam search score and the global best score for that length are insignificant enough not to affect BLEU ([Stahlberg & Byrne, 2019](document_1.txt)). The oracle experiment constrained to the correct reference length improved BLEU by 0.9 points ([Stahlberg & Byrne, 2019](document_1.txt)). These length-constrained findings are based on the 48.3% and 73.0% subsets, not on the full 2,169-sentence test set ([Stahlberg & Byrne, 2019](document_1.txt)).

## Conclusion

The answer to the query "what is the test set size?" depends on which source one trusts and which experimental section one is discussing. For the paper's main experiments without length constraints, the full English-German WMT news-test2015 test set contains **2,169 sentences** ([Stahlberg & Byrne, 2019](document_1.txt)). This is the figure stated directly in the primary source's experimental setup. The length-constrained exact-search experiments use subsets of that full test set: one experiment uses 73.0% of the test set, and others use 48.3% ([Stahlberg & Byrne, 2019](document_1.txt); [Third-party research note, n.d.](document_2.txt)). The third-party note's claim of 3,003 sentences is inconsistent with the primary source and should not be treated as the authoritative test set size for this paper ([Third-party research note, n.d.](document_2.txt); [Stahlberg & Byrne, 2019](document_1.txt)). Therefore, the most reliable and concrete answer is: **the full test set size is 2,169 sentences**, with length-constrained analyses performed on approximately 1,048 sentences (48.3%) or 1,583 sentences (73.0%) of that full set.

## References

- Stahlberg, F., & Byrne, B. (2019). *On NMT search errors and model errors: Cat got your tongue?* [document_1.txt].
- Third-party research note. (n.d.). *On NMT search errors and model errors: Cat got your tongue?* [document_2.txt].