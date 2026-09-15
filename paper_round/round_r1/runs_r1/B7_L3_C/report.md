# Test Set Size in "On NMT Search Errors and Model Errors: Cat Got Your Tongue?"

## Introduction

The question of test set size is central to evaluating the reliability and scope of any machine learning experiment, and it is especially important in neural machine translation (NMT), where decoding search spaces are vast and computational costs can be prohibitive. The provided sources report on a study by Stahlberg and Byrne that investigates search errors and model errors in NMT using exact inference ([document_1.txt](document_1.txt)). A key factual detail in that study is the size of the test set used for the main experiments. According to both the original paper content and a third-party research note, the full test set contains **2,169 sentences** ([document_1.txt](document_1.txt); [document_2.txt](document_2.txt)). This report provides a detailed, structured, and comprehensive answer to the query "what is the test set size?" by distinguishing between the full test set and the subsets used in length-constrained experiments, explaining the context in which the number appears, and discussing the implications of the test set size for the study's findings.

## Primary Answer: The Full Test Set Size Is 2,169 Sentences

### The Exact Figure

The paper states unambiguously: "We conduct all our experiments in this section on the entire English-German WMT news-test2015 test set (2,169 sentences)" ([document_1.txt](document_1.txt)). The third-party research note confirms this figure: "The entire English-German WMT news-test2015 test set contains 2,169 sentences. The paper states the test set size as a number of sentences. This full test set size of 2,169 sentences is reported before any subset selection" ([document_2.txt](document_2.txt)). Therefore, when the question asks for the test set size in the context of this study, the primary and most direct answer is **2,169 sentences**.

### What the Number Represents

The test set is the English-German WMT news-test2015 test set, a standard benchmark in machine translation research ([document_1.txt](document_1.txt)). It is a news-domain test set, and the language pair is English-German ([document_2.txt](document_2.txt)). The size is reported as a number of sentences, not as a number of tokens or subword units. This matters because NMT evaluation metrics such as BLEU operate at the sentence or corpus level, and exact inference procedures can be applied sentence by sentence ([document_1.txt](document_1.txt)). The full test set of 2,169 sentences is used in the paper's "Results without Length Constraints" section, where the authors compare greedy search, beam search with various beam sizes, and exact inference ([document_1.txt](document_1.txt); [document_2.txt](document_2.txt)).

### Why the Full Test Set Is Used

The paper uses the entire test set in the unconstrained experiments to establish a comprehensive picture of search errors and model errors under a Transformer base model ([document_1.txt](document_1.txt)). The exact inference scheme combines beam search and depth-first search to find global best model scores, and the authors report that beam search fails to find these scores in most cases, even with a beam size of 100 ([document_1.txt](document_1.txt)). Using the full test set is important because the findings—such as more than 50% of sentences having the empty translation as the global best model score—are corpus-level claims that require a sufficiently large and representative sample ([document_1.txt](document_1.txt)). The third-party note emphasizes that "this full test set supports the paper's exact inference comparisons for neural machine translation search errors and model errors" ([document_2.txt](document_2.txt)).

## Full Test Set Versus Subset Experiments

### Experiments Without Length Constraints

The paper divides its empirical results into two main sections: results without length constraints and results with length constraints ([document_1.txt](document_1.txt)). The first section uses the entire 2,169-sentence test set. The second section uses only a subset of the test set because constraining search increases runtime ([document_1.txt](document_1.txt)). This distinction is critical for answering the test set size query accurately: the full test set size is 2,169 sentences, but not every experiment in the paper uses all 2,169 sentences.

### Length-Constrained Exact Search Experiments

The paper explains that "all results in this section are conducted on only a subset of the test set to keep the runtime under control" ([document_1.txt](document_1.txt)). The third-party note specifies that "one experiment uses 73.0% of the test set" and "other experiments use 48.3% of the test set" ([document_2.txt](document_2.txt)). These subsets are distinct from the full test set size of 2,169 sentences ([document_2.txt](document_2.txt)). The reason for using subsets is computational: constraining exact search lowers the γ-bounds, which increases run time, and the authors stopped decoding if the decoder took longer than a day for a single sentence on a single CPU ([document_1.txt](document_1.txt)). Therefore, the subset experiments are a practical compromise rather than a statement about the full test set size.

### Table: Test Set Usage Across Experiments

| Experiment Section | Test Set Used | Reported Size | Notes |
|---|---|---|---|
| Results without length constraints | Entire English-German WMT news-test2015 test set | 2,169 sentences | Full test set; used for greedy, beam-10, beam-100, and exact inference comparisons ([document_1.txt](document_1.txt); [document_2.txt](document_2.txt)) |
| Results with length constraints (minimum translation length 0.25× source length) | Subset of test set | 73.0% of the test set | Used for Figure 5; runtime constrained ([document_1.txt](document_1.txt); [document_2.txt](document_2.txt)) |
| Results with length constraints (exact search constrained to Beam-10 length or reference length) | Subset of test set | 48.3% of the test set | Used for Tables 3 and 4; runtime constrained ([document_1.txt](document_1.txt); [document_2.txt](document_2.txt)) |

If one converts these percentages to approximate sentence counts, 73.0% of 2,169 is about 1,583 sentences, and 48.3% of 2,169 is about 1,048 sentences ([document_1.txt](document_1.txt); [document_2.txt](document_2.txt)). However, the paper itself reports the subset sizes only as percentages, not as exact sentence counts, so the full test set size remains the clearly stated figure of 2,169 sentences.

## Why the Test Set Size Matters for the Study's Conclusions

### Exact Inference and Computational Feasibility

The paper's main methodological contribution is an exact inference procedure for NMT that combines beam search and depth-first search ([document_1.txt](document_1.txt)). Exact search is computationally expensive because the NMT search space grows exponentially with sequence length; for a vocabulary of 32,000 tokens, there are more possible translations of 20 words or fewer than atoms in the observable universe ([document_1.txt](document_1.txt)). The authors note that exact search without length constraints is faster and does not need maximum execution time limits, but exact search under length constraints is slower because the γ-bounds are lower ([document_1.txt](document_1.txt)). This explains why the full 2,169-sentence test set is used for the unconstrained experiments, while subsets are used for the length-constrained experiments. The test set size therefore directly reflects a trade-off between statistical completeness and computational practicality.

### Search Errors and Model Errors

The study's headline findings depend on the full test set. The authors report that "beam search fails to find these global best model scores in most cases, even with a very large beam size of 100" ([document_1.txt](document_1.txt)). They also find that "for more than 50% of the sentences, the model in fact assigns its global best score to the empty translation, revealing a massive failure of neural models in properly accounting for adequacy" ([document_1.txt](document_1.txt)). These are corpus-level percentages, and the denominator is the full 2,169-sentence test set in the unconstrained experiments ([document_1.txt](document_1.txt); [document_2.txt](document_2.txt)). If the test set size were different, these proportions could shift, so the reported size is essential for interpreting the results.

### Length Bias and Empty Translations

The paper further investigates length bias by constraining exact search to certain translation lengths ([document_1.txt](document_1.txt)). The subset experiments show that constraining search to a minimum translation length of 0.25 times the source length mitigates the empty-translation problem slightly but still leaves a peak in the (0.3, 0.5] length-ratio cluster ([document_1.txt](document_1.txt)). The oracle experiment constrained to the correct reference length improves BLEU by 0.9 points ([document_1.txt](document_1.txt)). These findings are based on the subsets—73.0% and 48.3% of the test set—so the test set size question has a two-part answer: 2,169 sentences for the main experiments, and smaller subsets for the length-constrained analyses ([document_1.txt](document_1.txt); [document_2.txt](document_2.txt)).

## Reliability and Consistency of the Sources

The two provided sources are consistent on the test set size. The first source is the paper content itself, which includes the abstract, introduction, methodology, results tables, and references ([document_1.txt](document_1.txt)). The second source is a third-party research note that explicitly addresses the test set size and related questions ([document_2.txt](document_2.txt)). The third-party note states that "the paper reports the full test set size as 2,169 sentences before any subset selection" and that "these subset experiments are distinct from the full test set size of 2,169 sentences" ([document_2.txt](document_2.txt)). Because both sources agree, the answer can be stated with high confidence.

However, one should note that the original document text is noisy, with OCR-like artifacts and formatting issues ([document_1.txt](document_1.txt)). For example, numbers are sometimes spaced out, such as "2,1 6 9 sentences" instead of "2,169 sentences" ([document_1.txt](document_1.txt)). The third-party note helps disambiguate such artifacts and confirms the correct interpretation ([document_2.txt](document_2.txt)). This increases the reliability of the 2,169 figure.

## Opinion and Interpretation

Based on the provided information, my concrete opinion is that the test set size should be reported as **2,169 sentences** when referring to the main NMT search-error and model-error experiments in Stahlberg and Byrne's study ([document_1.txt](document_1.txt); [document_2.txt](document_2.txt)). It would be misleading to report only the subset percentages (73.0% and 48.3%) as if they were the full test set size, because those percentages apply only to the length-constrained exact search experiments, which were deliberately restricted to manage runtime ([document_1.txt](document_1.txt); [document_2.txt](document_2.txt)). Conversely, it would also be incomplete to claim that all experiments use 2,169 sentences, because the length-constrained results explicitly use subsets ([document_1.txt](document_1.txt)). The most accurate answer is therefore: the full test set is 2,169 sentences, and the length-constrained analyses use subsets corresponding to 73.0% and 48.3% of that full set.

This distinction is not merely semantic. It affects how one interprets the generalizability of the findings. The unconstrained experiments on 2,169 sentences support broad claims about beam search failures and empty translations ([document_1.txt](document_1.txt)). The length-constrained experiments on smaller subsets support more targeted claims about length normalization and minimum-length constraints ([document_1.txt](document_1.txt)). A careful reader should keep the two settings separate.

## Conclusion

The query "what is the test set size?" has a clear primary answer: the study uses the English-German WMT news-test2015 test set, which contains **2,169 sentences** ([document_1.txt](document_1.txt); [document_2.txt](document_2.txt)). This full test set is used for the experiments without length constraints, where the paper reports that beam search fails to find global best model scores in most cases, even with a beam size of 100, and that more than 50% of sentences have the empty translation as the global best model score ([document_1.txt](document_1.txt)). The length-constrained exact search experiments use only subsets—73.0% and 48.3% of the test set—to keep runtime under control ([document_1.txt](document_1.txt); [document_2.txt](document_2.txt)). Therefore, the full test set size is 2,169 sentences, while the subset experiments are distinct and should not be conflated with the full test set. This answer is supported by both the original paper content and the third-party research note, making it reliable and well-grounded in the provided information.

## References

document_1.txt. (n.d.). *On NMT search errors and model errors: Cat got your tongue?* [Manuscript].

document_2.txt. (n.d.). *Third-party research note: On NMT search errors and model errors: Cat got your tongue?* [Research note].