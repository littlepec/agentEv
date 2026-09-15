# Determining the Test Set Size in Stahlberg and Byrne's Study of NMT Search and Model Errors

## Introduction

The question of test set size is a deceptively simple one, yet in the case of Stahlberg and Byrne's investigation into neural machine translation (NMT) search errors and model errors, the answer requires careful source evaluation. The provided information contains two documents that report different figures for the size of the English–German WMT news-test2015 test set: the primary research paper itself and a third-party research note summarizing it. This report examines both sources, evaluates their reliability, resolves the discrepancy, and situates the test set size within the broader experimental design of the study.

The central finding of this report is that **the test set used for the paper's main, unconstrained exact-inference experiments consists of 2,169 sentences** ([Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090)). The alternative figure of 3,003 sentences, advanced by the third-party note, is not supported by the paper's text and conflicts directly with it ([Third-party research note](document_2.txt)).

## The Primary Source and Its Reported Test Set Size

### What the Primary Source States

Stahlberg and Byrne's paper, published on arXiv as [1908.10090] under the title "On NMT Search Errors and Model Errors: Cat Got Your Tongue?", explicitly reports the size of its experimental test set in its experimental setup. In Section 3, "Results without Length Constraints," the authors state that they conduct all experiments in that section on "the entire English-German WMT news-test2015 test set (2,169 sentences)" ([Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090)).

This figure is stated as a sentence count, which is the natural unit of measurement for a machine translation evaluation set. The paper's abstract also refers to using the "entire WMT15 English-German test set" for exact search experiments, without restating the number, thereby reinforcing that the full test set—not a subsampled portion—was used for the headline results ([Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090)).

### Why This Number Is the Operative One

The 2,169-sentence figure anchors the paper's most consequential claims. It is the dataset on which the authors report that beam search fails to find the global best model score in the majority of cases, that more than 50% of sentences receive the empty translation as the model's global best-scoring output, and that greedy decoding produces search errors on 73.6% of sentences while Beam-10 produces them on 57.7% ([Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090)). Because these percentages and the accompanying BLEU scores (greedy: 29.3; Beam-10: 30.3; exact: 2.1) are computed over the full test set, the size of that set is directly relevant to interpreting the study's statistical claims ([Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090)).

It is also worth noting the scale of the decoding problem that the paper describes, which contextualizes the test set size. The NMT search space grows exponentially with sequence length; with a vocabulary of 32,000 tokens, there are more possible translations of 20 words or fewer than there are atoms in the observable universe (32,000²⁰ ≫ 10⁸²) ([Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090)). Running exact depth-first search over this space for 2,169 sentences is precisely what makes the study's runtime constraints a genuine experimental concern—and what explains why some later experiments had to be restricted to subsets.

## The Competing Claim: 3,003 Sentences

### What the Third-Party Note Asserts

The third-party research note makes a series of categorical assertions that the test set contains 3,003 sentences. It states that "the paper's main experiments use the entire English-German WMT news-test2015 test set of 3,003 sentences," that "the entire English-German WMT news-test2015 test set contains 3,003 sentences," and that "this full test set size of 3,003 sentences is reported before any subset selection" ([Third-party research note](document_2.txt)). The note repeats this figure in multiple paragraphs, applying it both to the general experimental setup and specifically to the "results without length constraints" section ([Third-party research note](document_2.txt)).

### Assessment of the Discrepancy

The two sources cannot both be correct, and the evidence strongly favors the primary source. Three considerations support this conclusion:

**First, direct textual conflict.** The primary source states "(2,169 sentences)" in direct parentheses immediately following the phrase "the entire English-German WMT news-test2015 test set" ([Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090)). The third-party note claims the paper "reports this size in its experimental setup" ([Third-party research note](document_2.txt)), but the number it attributes to that setup does not appear anywhere in the paper text as provided. A secondary summary that misattributes a figure to a primary document is less reliable than the primary document itself.

**Second, source hierarchy.** The paper by Stahlberg and Byrne is the original scholarly artifact: it defines the experiments, the algorithms (Algorithm 1: BeamSearch; Algorithm 2: DFS), and the results tables ([Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090)). The third-party note is a derivative document whose stated purpose is to answer "key questions" about test set size, and it contains no methodological apparatus of its own ([Third-party research note](document_2.txt)). When a derivative document contradicts its own source, the source governs.

**Third, internal consistency with the subset percentages.** The paper reports that its length-constrained experiments were run on "73.0% of the test set" and on "48.3% of the test set" ([Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090)). These percentages are consistent with a base set of any size, so they do not independently adjudicate the dispute; however, the fact that the third-party note itself repeats the 73.0% and 48.3% figures while claiming a 3,003-sentence base shows that the note's error is localized to the full-set number rather than to a different experimental interpretation ([Third-party research note](document_2.txt)). There is no indication in the paper of a separate 3,003-sentence evaluation.

On balance, the defensible answer is that the test set size is **2,169 sentences**, and the 3,003 figure should be treated as an error in the derivative note.

### Summary of Conflicting Reports

| Source | Claimed test set size | Section attributed | Assessment |
|---|---|---|---|
| Stahlberg & Byrne (2019), primary paper | 2,169 sentences | "Results without Length Constraints" (Section 3) | Accepted — primary source, states figure explicitly |
| Third-party research note | 3,003 sentences | Experimental setup / Section 3 | Rejected — contradicts primary source text |

## Subset Sizes in the Length-Constrained Experiments

A complete answer to "what is the test set size?" must also account for the fact that the paper deliberately used smaller subsets for its Section 4 experiments. The authors explain that constraining exact search to certain translation lengths increases runtime because the lower bounds (γ-bounds) become lower; consequently, "all results in this section are conducted on only a subset of the test set to keep the runtime under control" ([Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090)). The authors further note they stopped decoding if a single sentence took longer than a day on a single CPU, whereas unconstrained exact search is much faster and requires no such time limit ([Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090)).

The subset proportions reported are as follows:

| Experiment (Section 4) | Portion of full test set | Reported figure |
|---|---|---|
| Length-ratio histogram with minimum translation length of 0.25 × source length (Figure 5) | 73.0% | 73.0% of test set |
| Exact search under length constraints (Table 3) | 48.3% | 48.3% of test set |
| Length normalization comparison (Table 4) | 48.3% | 48.3% of test set |

These figures appear in the paper and are reproduced in the third-party note ([Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090); [Third-party research note](document_2.txt)). They are important because they establish that the paper distinguishes between its full-test-set results—where the 2,169-sentence figure applies—and its computationally expensive constrained-search results, which cover only part of the data.

## Why the Test Set Size Matters for Interpreting the Results

The test set size is not a trivial administrative detail; it conditions how the paper's findings should be read.

### Statistical Weight of the Headline Claims

The claim that the model assigns its global best score to the empty translation for 51.8% of sentences rests on the full 2,169-sentence set ([Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090)). At that scale, the finding is robust enough to support the paper's provocative conclusion that "vanilla NMT in its current form requires just the right amount of beam search errors" ([Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090)). The same applies to the finding that even Beam-100 produces 53.62% search errors, and that Beam-10 yields 15.9 percentage points fewer search errors (absolute) than greedy decoding (57.68% vs. 73.58%) ([Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090)).

### Generalization Across Architectures

The paper's Table 2 reports that the problems of search errors and empty translations are not specific to the Transformer base model. Across architectures evaluated with Beam-10, search error rates and empty-translation rates were: LSTM (58.4% search errors, 47.7% empty), SliceNet (46.0%, 41.2%), Transformer-Base (57.7%, 51.8%), and Transformer-Big (32.1%, 25.8%) ([Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090)). While Table 2 does not restate the test set size per row, these results belong to the same experimental program whose unconstrained portion uses the full 2,169-sentence test set.

### The Oracle Upper Bound

The oracle experiment constraining exact search to the reference translation length improved BLEU by 0.9 points over Beam-10 (37.9 vs. 37.0) on the 48.3% subset ([Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090)). Because this figure comes from a subset rather than the full test set, its precision is lower than the Section 3 results, a limitation the authors implicitly acknowledge by reporting the subset percentage alongside the table.

## Conclusion

Based on the primary source, the test set size used for the main unconstrained exact-inference experiments in Stahlberg and Byrne's study is **2,169 sentences**, comprising the entire English–German WMT news-test2015 test set ([Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090)). The third-party research note's assertion of 3,003 sentences is inconsistent with the paper's own text and should not be relied upon ([Third-party research note](document_2.txt)). The length-constrained experiments in Section 4 were conducted on subsets of this full set—73.0% for the minimum-length-constraint histogram and 48.3% for the length-constrained exact search and length-normalization comparisons—because the lower γ-bounds made unconstrained search prohibitively slow ([Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090)). Any interpretation of the paper's headline claims about search errors, empty translations, and the length bias of NMT should therefore be grounded in the 2,169-sentence full test set, while its constrained-search findings should be understood as subset-based.

## References

Stahlberg, F., & Byrne, B. (2019). *On NMT search errors and model errors: Cat got your tongue?* arXiv. https://arxiv.org/abs/1908.10090

Third-party research note: *On NMT search errors and model errors: Cat got your tongue?* (n.d.). [Third-party research note](document_2.txt)