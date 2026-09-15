# What Is the Test Set Size? A Detailed Examination of the NMT Search-Error Study

## Introduction and Scope

The question "what is the test set size?" appears simple, but the supplied materials present two conflicting figures drawn from documentation about the same study. The primary source—the paper *"On NMT Search Errors and Model Errors: Cat Got Your Tongue?"* by Felix Stahlberg and Bill Byrne of the University of Cambridge—states in its experimental section that the main experiments were conducted on "the entire English-German WMT news-test2015 test set (2,169 sentences)" ([Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090)). A separate third-party research note, however, asserts that the "entire English-German WMT news-test2015 test set" contains 3,003 sentences and that "the paper reports this size in its experimental setup" ([Third-Party Research Note, n.d.](document_2.txt)).

This report evaluates both claims, weighs the reliability of each source, and states a concrete conclusion. It also documents the role of subsets in the length-constrained experiments, since the query about test set size cannot be answered comprehensively without distinguishing the full test set from the reduced sets used for computationally expensive exact-search runs.

## The Primary Source's Reported Test Set Size

### The Full Set Used for the Main Experiments

The paper's experimental section, under the heading "Results without Length Constraints," is explicit about the data used. The authors write that "We conduct all our experiments in this section on the entire English-German WMT news-test2015 test set (2,169 sentences)" ([Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090)). This sentence appears immediately after the section heading and before any discussion of the Transformer model, training data, or preprocessing pipeline, which makes its role unambiguous: it defines the evaluation set for the results reported in that section, including the search-error counts and the empty-translation counts.

The abstract corroborates the use of a complete, unsubsetted test set, stating that the authors "use our exact search to find the global best model scores under a Transformer base model for the entire WMT15 English-German test set" ([Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090)). Although the abstract does not repeat the numeral, the phrase "the entire WMT15 English-German test set" is consistent with the 2,169-sentence figure given in the body of the paper, which the authors explicitly qualify as the full set rather than a sample.

### Model, Training Data, and Preprocessing Context

For completeness of the experimental setup—since test set size is only meaningful alongside the model and data pipeline—the paper specifies that the system is "a Transformer base (Vaswani et al. 2017) model trained with Tensor2Tensor (Vaswani et al. 2018) on parallel WMT18 data excluding ParaCrawl" ([Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090)). Preprocessing follows earlier work by Stahlberg et al. (2018a) and "includes joint subword segmentation using byte pair encoding (Sennrich et al. 2016) with 32K merges," with results reported as "cased BLEU scores" ([Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090)). The authors also note that an open-source implementation of their exact inference scheme is available in the SGNMT decoder, and that results are "comparable with http://matrix.statmt.org/" ([Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090)). These details establish that the 2,169-sentence evaluation rests on a standard, reproducible WMT-style pipeline rather than an ad hoc sample.

## Conflicting Evidence: The Third-Party Note's 3,003 Sentences

The second source is described as a "Third-party research note" whose key questions include "NMT search errors model errors test set size" and "Stahlberg Byrne NMT search errors test set size" ([Third-Party Research Note, n.d.](document_2.txt)). It states repeatedly and emphatically that "The paper's main experiments use the entire English-German WMT news-test2015 test set of 3,003 sentences," that "The entire English-German WMT news-test2015 test set contains 3,003 sentences," and that "The paper reports this size in its experimental setup" ([Third-Party Research Note, n.d.](document_2.txt)).

### Direct Comparison of the Two Claims

The table below places the two sources side by side on the same question.

| Attribute | Primary source (paper text) | Third-party research note |
|---|---|---|
| Corpus | WMT news-test2015, English–German | WMT news-test2015, English–German |
| Stated full test set size | 2,169 sentences | 3,003 sentences |
| Where stated | "Results without Length Constraints" section | Throughout the note |
| Basis for claim | Direct experimental setup sentence | Unattributed assertion about the paper |
| Model evaluated on full set | Transformer base (Tensor2Tensor) | Same, as characterized by the note |
| Subset experiments acknowledged | Yes (73.0% and 48.3%) | Yes (73.0% and 48.3%) |

The two documents agree on the corpus identity, the language pair, the model family, and the existence of subset-based length-constrained experiments. They disagree only on the headline number: 2,169 versus 3,003.

### Reliability Assessment

Applying source-prioritization criteria, the paper itself—the primary, first-hand report of the experimental setup—outweighs a third-party summary. The primary text places the number 2,169 inside a concrete methodological sentence that defines the scope of a results section, alongside reproducible details such as the model architecture, training corpus, and subword configuration ([Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090)). The third-party note, by contrast, asserts that "the paper reports this size in its experimental setup" without supplying any quotation from the paper, and none of the primary-source text supplied in the present materials contains the number 3,003 ([Third-Party Research Note, n.d.](document_2.txt); [Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090)).

It is also notable that the third-party note frames its 3,003 figure as the size "before any subset selection," implying that 3,003 is a superset from which the reported percentages are drawn ([Third-Party Research Note, n.d.](document_2.txt)). But the primary text states plainly that the full-set experiments already used "the entire English-German WMT news-test2015 test set (2,169 sentences)" ([Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090)). A full set cannot simultaneously be 2,169 and 3,003 sentences. On the balance of the evidence, the 3,003 figure appears to be an error in the secondary note—most plausibly a conflation with a differently sized WMT news test set from another year—rather than a fact drawn from the paper.

## Subsets Used in the Length-Constrained Experiments

A complete answer to the query must distinguish the full test set from the reduced sets used later in the paper. The authors are explicit that the length-constrained experiments could not be run on the full data: "Constraining search that way increases the run time as the γ-bounds are lower. Therefore, all results in this section are conducted on only a subset of the test set to keep the runtime under control" ([Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090)). The paper further documents the practical limit: "We stopped decoding if the decoder took longer than a day for a single sentence on a single CPU. Exact search without length constraints is much faster and does not need maximum execution time limits" ([Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090)).

Two subset proportions are reported:

| Experiment | Reported subset | Derived sentence count (from 2,169) |
|---|---|---|
| Minimum-length constraint of 0.25 × source length (Figure 5) | 73.0% of the test set | ≈1,583 sentences |
| Exact search under length constraints (Tables 3 and 4) | 48.3% of the test set | ≈1,048 sentences |

The 73.0% figure applies to the histogram over length ratios produced under a minimum translation length constraint of 0.25 times the source sentence length, described as an "Experiment conducted on 73.0% of the test set" ([Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090)). The 48.3% figure is attached to both Table 3, "Exact search under length constraints," and Table 4, which reports results with and without length normalization ([Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090)).

The derived sentence counts in the right-hand column are arithmetic products of the reported percentages and the paper's stated full-set size of 2,169; they are not printed in the paper itself. They are offered here as an aid to interpretation and should be treated as approximate, since the paper reports only percentages. Under the third-party note's alternative figure of 3,003 sentences, the same percentages would imply approximately 2,192 and 1,450 sentences respectively—another reason the two sources cannot both be correct.

## Why the Test Set Size Matters for the Paper's Findings

The test set size is not a trivial bibliographic detail in this study; it underpins the study's central empirical claim. The authors report that "for more than 50% of the sentences, the model in fact assigns its global best score to the empty translation," a result they characterize as "revealing a massive failure of neural models in properly accounting for adequacy" ([Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090)). That "more than 50%" statement is derived from the full-set experiments—the same experiments the paper says were run on the entire 2,169-sentence WMT news-test2015 set ([Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090)).

The quantitative picture reported for the full set is striking. Under exact inference, the paper's Table 1 reports BLEU 2.1 with a length ratio of 0.06, and the empty-translation rate is given as 51.8% ([Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090)). Greedy search reaches BLEU 29.3 with a length ratio of 1.02, while Beam-10 reaches BLEU 30.3 with a ratio of 1.00 ([Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090)). The paradoxical relationship the authors emphasize—that search errors "prevent the decoder from suffering from a frequent but very serious model error"—is quantified against this full set, with Beam-10 producing 57.7% search errors and exact search producing 0.0%, because exact search by definition finds the global best model score ([Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090)).

A related comparison appears in the paper's Table 2, which shows that the problem generalizes across architectures: the recurrent LSTM shows 58.4% search errors and 47.7% empty translations, SliceNet shows 46.0% and 41.2%, Transformer-Base shows 57.7% and 51.8%, and an optimized Transformer-Big system shows 32.1% and 25.8% ([Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090)). The authors also note that "Even a large beam size of 100 produces 53.62% search errors," and that Beam-10 "yields 15.9% fewer search errors (absolute) than greedy decoding (57.68% vs. 73.58%), but Beam-100 improves search only slightly (53.62% search errors) despite being 10 times slower than beam-10" ([Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090)). Because these percentages are computed over the full test set, the choice between 2,169 and 3,003 sentences directly affects how much evidential weight the results carry.

The subset experiments carry a different inferential weight. The paper reports that exact search constrained to the Beam-10 hypothesis length "does not improve over beam search, suggesting that any search errors between beam search score and global best score for that length are insignificant enough so as not to affect the BLEU score," while the oracle experiment constrained to the reference length "improved the BLEU score by 0.9 points" ([Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090)). Experiments under length normalization likewise produced BLEU 37.0 (without normalization, ratio 1.00) and BLEU 36.3 (with normalization, ratio 1.03) for Beam-10, with exact search reaching only BLEU 27.2 at ratio 0.74 without normalization but BLEU 36.4 at ratio 1.03 with normalization ([Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090)). These findings, run on roughly 48.3% of the test set, are therefore based on a smaller sample than the headline results—a distinction the paper is careful to make by reporting the percentages in the table captions ([Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090)).

## Conclusion

Based on the evidence supplied, the test set size for the main experiments in Stahlberg and Byrne's study should be understood as **2,169 sentences**, comprising the entire English–German WMT news-test2015 test set ([Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090)). This figure is stated directly in the paper's experimental setup, is consistent with the abstract's reference to "the entire WMT15 English-German test set," and is the basis on which the paper's key percentages—51.8% empty translations and 53.62% search errors at beam size 100—are computed ([Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090)).

The alternative figure of 3,003 sentences originates from a third-party research note and is not corroborated by the paper's own text as reproduced in the supplied materials ([Third-Party Research Note, n.d.](document_2.txt)). Because the discrepancy is material—it changes the implied absolute counts behind the paper's headline percentages—the more reliable, primary source should be preferred, and the secondary figure treated as an unverified claim.

Finally, the "test set size" question has a second dimension: the length-constrained exact-search experiments did not use the full set. Those experiments were run on 73.0% and 48.3% subsets, corresponding to roughly 1,583 and 1,048 sentences respectively if the full set contains 2,169 sentences ([Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090)). Any comparison of results across the paper's sections must therefore account for the fact that the full-set results and the length-constrained results rest on different evaluation samples.

## References

Stahlberg, F., & Byrne, B. (2019). *On NMT search errors and model errors: Cat got your tongue?* arXiv:1908.10090. https://arxiv.org/abs/1908.10090 (also supplied as document_1.txt)

*Third-party research note: On NMT search errors and model errors: Cat got your tongue?* (n.d.). document_2.txt.