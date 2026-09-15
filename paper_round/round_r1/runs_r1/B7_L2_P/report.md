# Determining the Test Set Size in "On NMT Search Errors and Model Errors: Cat Got Your Tongue?"

## Executive Summary

The query asks for the test set size used in the experiments reported in "On NMT Search Errors and Model Errors: Cat Got Your Tongue?" by Stahlberg and Byrne. Based on the primary source provided—the paper itself—the full English-German WMT news-test2015 test set contains **2,169 sentences** ([Stahlberg & Byrne, 2019](document_1.txt)). This figure is stated explicitly in Section 3, "Results without Length Constraints," where the authors write: "We conduct all our experiments in this section on the entire English-German WMT news-test2015 test set (2,169 sentences) with a Transformer base ..." ([Stahlberg & Byrne, 2019](document_1.txt)). A third-party research note included in the information claims a different size, **3,003 sentences**, but this claim is not supported by the primary paper and appears to be erroneous ([Third-party research note, n.d.](document_2.txt)). Therefore, the authoritative answer to the query is 2,169 sentences for the full test set size, with subset sizes of 73.0% and 48.3% used only for length-constrained experiments.

## Primary Source Evidence: Explicit Statement of 2,169 Sentences

The primary source, document_1.txt, is the paper itself. It contains the most direct and reliable evidence regarding the test set size. In Section 3, the authors state that they conduct all experiments in that section on the entire English-German WMT news-test2015 test set, and they provide the parenthetical count of 2,169 sentences ([Stahlberg & Byrne, 2019](document_1.txt)). This statement is unambiguous and appears in the context of describing the experimental setup for the main results without length constraints.

The abstract of the paper also refers to the "entire WMT15 English-German test set" but does not provide a numerical count in the abstract itself ([Stahlberg & Byrne, 2019](document_1.txt)). The number 2,169 is therefore the only concrete full test set size reported in the paper. It is not an approximation or a derived figure; it is an explicit count stated by the authors.

This full test set of 2,169 sentences supports the paper's exact inference comparisons for neural machine translation search errors and model errors. The main results in Table 1—comparing Greedy, Beam-10, and Exact search—are based on this full test set ([Stahlberg & Byrne, 2019](document_1.txt)). Table 2, which extends the analysis to other architectures such as LSTM, SliceNet, Transformer-Base, and Transformer-Big, also appears to use the same full test set, as no subset limitation is mentioned for that table ([Stahlberg & Byrne, 2019](document_1.txt)). Figures 1 through 4, which visualize search errors, BLEU scores, length ratios, and the relationship between source sentence length and empty translations, are likewise based on the full test set ([Stahlberg & Byrne, 2019](document_1.txt)).

Therefore, the primary source establishes the full test set size as 2,169 sentences for the main experiments.

## Conflicting Claim in the Third-Party Research Note

A third-party research note, document_2.txt, presents a conflicting claim. It states: "The paper's main experiments use the entire English-German WMT news-test2015 test set of 3,003 sentences" ([Third-party research note, n.d.](document_2.txt)). This note repeats the figure 3,003 multiple times throughout its content, asserting that the paper reports this size in its experimental setup and that it is the full test set size before any subset selection ([Third-party research note, n.d.](document_2.txt)).

However, a careful examination of the primary source reveals that the number 3,003 does not appear anywhere in document_1.txt. The paper consistently reports 2,169 sentences as the size of the entire English-German WMT news-test2015 test set ([Stahlberg & Byrne, 2019](document_1.txt)). The third-party note's claim is therefore directly contradicted by the primary source.

Several explanations for this discrepancy are possible. The third-party note may have confused the WMT15 test set with a later WMT test set, such as WMT17 or WMT18, which often contain around 3,000 sentences. Alternatively, the note may be an automatically generated summary that introduced a factual error. Regardless of the cause, the third-party note is less reliable than the primary paper. It has no author, no venue, and no publication date, and it appears to be a secondary summary rather than an original research contribution ([Third-party research note, n.d.](document_2.txt)). In cases of conflict, the primary source must be prioritized.

## Subset Sizes for Length-Constrained Experiments

While the full test set size is 2,169 sentences, the paper also reports that the length-constrained exact search experiments use only a subset of the test set to keep the runtime under control ([Stahlberg & Byrne, 2019](document_1.txt)). Specifically, the paper states: "Therefore, all results in this section are conducted on only a subset of the test set to keep the runtime under control" ([Stahlberg & Byrne, 2019](document_1.txt)). The caption for Figure 5 indicates that the experiment was conducted on 73.0% of the test set ([Stahlberg & Byrne, 2019](document_1.txt)). The captions for Tables 3 and 4 indicate that those experiments were conducted on 48.3% of the test set ([Stahlberg & Byrne, 2019](document_1.txt)).

These percentages are not absolute numbers, but they can be converted using the full test set size of 2,169 sentences. If the full test set is 2,169 sentences, then 73.0% corresponds to approximately 1,583 sentences, and 48.3% corresponds to approximately 1,048 sentences. These derived values are not explicitly stated in the paper, but they follow arithmetically from the reported percentages and the full test set size ([Stahlberg & Byrne, 2019](document_1.txt)).

If one were to incorrectly adopt the third-party note's figure of 3,003 sentences, then 73.0% would correspond to approximately 2,192 sentences and 48.3% to approximately 1,450 sentences ([Third-party research note, n.d.](document_2.txt)). However, these derived numbers are not supported by the primary source. The correct basis for any subset calculation is the primary source's full test set size of 2,169 sentences.

The following table summarizes the comparison between the two sources:

| Source | Claimed full test set size | Type of source | Reliability assessment |
|--------|----------------------------|----------------|------------------------|
| document_1.txt (Stahlberg & Byrne, 2019) | 2,169 sentences | Primary paper | High: explicit statement in experimental setup |
| document_2.txt (Third-party research note, n.d.) | 3,003 sentences | Third-party research note | Low: contradicts primary source, no author or venue |

The table below shows the derived subset sizes under each claimed full test set size:

| Experiment (as reported) | Percentage of test set | Implied sentences if full set = 2,169 | Implied sentences if full set = 3,003 |
|---------------------------|------------------------|----------------------------------------|----------------------------------------|
| Figure 5 (minimum translation length of 0.25 times source length) | 73.0% | ~1,583 | ~2,192 |
| Tables 3 and 4 (length-constrained exact search) | 48.3% | ~1,048 | ~1,450 |

These calculations demonstrate that the full test set size is not merely a descriptive detail; it affects the interpretation of the subset experiments and the absolute number of sentences used in each analysis.

## Implications of the Correct Test Set Size

The correct test set size of 2,169 sentences has important implications for interpreting the paper's key findings. The paper reports that for more than 50% of the sentences, the model assigns its global best score to the empty translation ([Stahlberg & Byrne, 2019](document_1.txt)). In Table 1, the exact search condition shows 51.8% empty translations ([Stahlberg & Byrne, 2019](document_1.txt)). If the full test set is 2,169 sentences, then 51.8% corresponds to approximately 1,124 sentences where the empty translation receives the global best model score. If the full test set were 3,003 sentences, the absolute count would be approximately 1,555 sentences. The relative percentage remains the same, but the absolute number of affected sentences differs substantially.

Similarly, the paper reports search error rates. For Beam-10, the search error rate is 57.7% ([Stahlberg & Byrne, 2019](document_1.txt)). With 2,169 sentences, this corresponds to approximately 1,252 sentences with search errors. With 3,003 sentences, it would correspond to approximately 1,733 sentences. For greedy decoding, the search error rate is 73.6%, which corresponds to approximately 1,596 sentences under the primary source's test set size ([Stahlberg & Byrne, 2019](document_1.txt)). These absolute counts are relevant for assessing the practical impact of the reported phenomena.

Furthermore, the paper's conclusion that "vanilla NMT in its current form requires just the right amount of beam search errors" depends on the observed frequency of empty translations and search errors ([Stahlberg & Byrne, 2019](document_1.txt)). An incorrect test set size would not change the relative frequencies, but it would change the scale of the problem. The primary source's explicit count of 2,169 sentences should therefore be used in any secondary analysis or replication attempt.

## Source Reliability and Prioritization

The instruction for this report emphasizes prioritizing relevance, reliability, and significance of sources. The primary source, document_1.txt, is the original paper by Felix Stahlberg and Bill Byrne. It includes a full description of the exact inference algorithm, the experimental setup, the results, and the references ([Stahlberg & Byrne, 2019](document_1.txt)). The paper is an arXiv preprint (1908.10090) and appears to be a completed research article with detailed methodology and reproducible results. Its reliability is high.

The secondary source, document_2.txt, is described as a "Third-party research note" ([Third-party research note, n.d.](document_2.txt)). It has no identified author, no institutional affiliation, and no publication venue. It is a summary or commentary rather than an original research contribution. It contains a factual error regarding the test set size, claiming 3,003 sentences when the primary paper states 2,169 sentences ([Third-party research note, n.d.](document_2.txt); [Stahlberg & Byrne, 2019](document_1.txt)). The note also repeats the same erroneous claim multiple times, which does not increase its reliability. When a secondary source contradicts a primary source on a matter of explicit fact, the primary source must be preferred.

The instruction also states to prioritize new articles over older articles if the source can be trusted. In this case, both documents refer to the same paper. The primary source is the paper itself, which is the most authoritative and recent source of information about its own experiments. The third-party note is derivative and less trustworthy. Therefore, the primary source's figure of 2,169 sentences is the correct answer.

## Detailed Breakdown of the Paper's Test Set Usage

To provide a comprehensive answer, it is useful to break down how the test set is used across different sections of the paper. In Section 3, "Results without Length Constraints," the authors use the entire English-German WMT news-test2015 test set of 2,169 sentences ([Stahlberg & Byrne, 2019](document_1.txt)). This section includes the main results in Table 1, which compares Greedy, Beam-10, and Exact search. It also includes Table 2, which reports results for LSTM, SliceNet, Transformer-Base, and Transformer-Big models. Figures 1, 2, 3, and 4 are also based on this full test set. The exact inference procedure was run on all 2,169 sentences, which is a significant computational effort given the exact search algorithm's complexity.

In Section 4, "Results with Length Constraints," the authors use only a subset of the test set because constraining search increases runtime ([Stahlberg & Byrne, 2019](document_1.txt)). They report that they stopped decoding if the decoder took longer than a day for a single sentence on a single CPU ([Stahlberg & Byrne, 2019](document_1.txt)). The subset experiments are conducted on 73.0% and 48.3% of the test set, as reported in the captions for Figure 5 and Tables 3 and 4 respectively ([Stahlberg & Byrne, 2019](document_1.txt)). These subsets are distinct from the full test set size of 2,169 sentences. The paper does not report the absolute number of sentences in these subsets, but they can be calculated as approximately 1,583 and 1,048 sentences, respectively.

The abstract of the paper mentions the "entire WMT15 English-German test set" without specifying the number of sentences ([Stahlberg & Byrne, 2019](document_1.txt)). The introduction also refers to the test set but does not provide a count. The only explicit count is the 2,169 figure in Section 3. This reinforces that 2,169 is the intended full test set size.

## Conclusion and Final Answer

The query asks for the test set size. Based on the primary source, the full English-German WMT news-test2015 test set used for the main experiments in "On NMT Search Errors and Model Errors: Cat Got Your Tongue?" contains **2,169 sentences** ([Stahlberg & Byrne, 2019](document_1.txt)). The third-party research note's claim of 3,003 sentences is incorrect and should be disregarded ([Third-party research note, n.d.](document_2.txt)). For the length-constrained experiments, subsets of 73.0% and 48.3% of the full test set were used, corresponding to approximately 1,583 and 1,048 sentences, respectively. However, these are subset sizes, not the full test set size. Therefore, the definitive answer to the query is 2,169 sentences.

## References

- Stahlberg, F., & Byrne, B. (2019). *On NMT Search Errors and Model Errors: Cat Got Your Tongue?* [document_1.txt].
- Third-party research note. (n.d.). *On NMT Search Errors and Model Errors: Cat Got Your Tongue?* [document_2.txt].