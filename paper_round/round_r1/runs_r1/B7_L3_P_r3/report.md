# Test Set Size in Stahlberg and Byrne's Study of NMT Search and Model Errors

## 1. Direct Answer to the Query

The question of "what is the test set size?" in Stahlberg and Byrne's study of neural machine translation (NMT) search and model errors has a specific, quantifiable answer, but the evidence available in the supplied corpus contains a notable internal inconsistency that must be reported rather than glossed over. Based on the dedicated third-party research note that explicitly addresses this question, the full English–German WMT news-test2015 test set used for the paper's main experiments comprises **3,003 sentences** ([Third-party research note, n.d.](https://arxiv.org/abs/1908.10090)). This figure is presented in the note as the size reported "before any subset selection," and it is described as the foundation for the paper's exact-inference comparisons of NMT search errors and model errors ([Third-party research note, n.d.](https://arxiv.org/abs/1908.10090)).

However, the primary source document — the paper itself — contains a passage stating that the same experiments were conducted on the entire English–German WMT news-test2015 test set of **2,169 sentences** ([Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090)). This report therefore answers the query in full: the headline figure is 3,003 sentences, the paper's own rendered text gives 2,169 sentences, and the discrepancy between these two values is itself a substantive finding that a careful reader of the provided material should understand before citing a number.

## 2. The Reported Full Test Set Size: 3,003 Sentences

The third-party research note is unambiguous and repetitive on this point, which strongly suggests that its authors treated the number as a key extractable fact. The note states that "the paper's main experiments use the entire English-German WMT news-test2015 test set of 3,003 sentences," that "the entire English-German WMT news-test2015 test set contains 3,003 sentences," and that the paper "reports this size in its experimental setup" ([Third-party research note, n.d.](https://arxiv.org/abs/1908.10090)). The note further specifies that the figure is expressed as a number of sentences, that it is reported before any subset selection, and that the language pair is English–German over a news test set ([Third-party research note, n.d.](https://arxiv.org/abs/1908.10090)).

The note also ties the full-set figure to a particular section of the paper, asserting that "all experiments in the results without length constraints section are conducted on the entire English-German WMT news-test2015 test set (3,003 sentences)," and that "this full test set supports the paper's exact inference comparisons for neural machine translation search errors and model errors" ([Third-party research note, n.d.](https://arxiv.org/abs/1908.10090)). This is significant because the section without length constraints is precisely where the paper's headline findings reside: the discovery that beam search fails to find global best model scores for more than half of the sentences, and that for more than 50% of sentences the model assigns its global best score to the empty translation ([Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090)). In other words, the 3,003-sentence figure is the denominator for the paper's most consequential percentage claims.

Corroboration for the scale of the test set also comes from the paper's abstract, which states that the authors "use our exact search to find the global best model scores under a Transformer base model for the entire WMT15 English-German test set" ([Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090)). While the abstract does not attach a numeral to "the entire" test set, it confirms that no subsetting was applied in the main experimental condition, which is consistent with the research note's characterization.

## 3. A Competing Figure in the Primary Source: 2,169 Sentences

### 3.1 The Textual Evidence

The primary source document, however, contains a directly contradictory statement. In the section on results without length constraints, the paper states: "We conduct all our experiments in this section on the entire English-German WMT news-test2 0 1 5 test set (2,1 6 9 sentences)" ([Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090)). The spacing artefacts in the supplied rendering ("2,1 6 9") are typical of the tokenized LaTeX-to-XML output from which the document was generated, and they read naturally as the numeral 2,169.

### 3.2 Why the Discrepancy Matters

This is not a trivial typographical quibble. The paper's central quantitative claims are expressed as percentages of the test set: "for more than 50% of the sentences, the model in fact assigns its global best score to the empty translation" and "for 5 1.8% of the sentences, NMT assigns the global best model score to the empty translation" ([Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090)). It also reports that greedy decoding yields 73.6% search errors, Beam-10 yields 57.7%, and Beam-100 yields 53.6% search errors ([Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090)). Each of these percentages translates to a different absolute sentence count depending on whether the denominator is 2,169 or 3,003. For example, 51.8% of 3,003 sentences is approximately 1,556 sentences, whereas 51.8% of 2,169 sentences is approximately 1,124 sentences — a difference of more than 400 sentences. Reproducibility and any downstream meta-analysis would therefore be affected by which base figure is correct.

### 3.3 Adjudicating Between the Two Figures

On the evidence supplied, a definitive resolution is not achievable, and it is important to say so rather than to assert false certainty. Three considerations bear on the judgment:

First, **source type**. The primary source is the paper itself, which would normally be the most authoritative reference. However, the specific rendering provided is a machine-generated LaTeX/XML extraction that demonstrably garbles many tokens (for instance, "retum" for "return," "e1ements" for "elements," "Byme" for "Byrne," and "norma1ization" for "normalization") ([Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090)). Numeric strings in such renderings are especially vulnerable to corruption.

Second, **the dedicated note**. The third-party research note is purpose-built around the very question asked here, listing "NMT search errors model errors test set size" and "Stahlberg Byrne NMT search errors test set size" among its key questions addressed ([Third-party research note, n.d.](https://arxiv.org/abs/1908.10090)). It states the 3,003 figure four separate times and explicitly frames it as "the full test set size… reported before any subset selection" ([Third-party research note, n.d.](https://arxiv.org/abs/1908.10090)). Repetition of this kind is characteristic of a deliberate, verified extraction rather than an incidental transcription.

Third, **arithmetic plausibility**. Neither candidate resolves the subset percentages cleanly. The paper reports length-constrained experiments on "7 3.0% of the test set" and "4 8.3% of the test set" ([Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090)). Applying these to 3,003 sentences gives approximately 2,192 and 1,450 sentences; applying them to 2,169 sentences gives approximately 1,583 and 1,048 sentences. The intermediate value 2,169 is numerically closer to 73.0% of 3,003 (2,192) than to any obvious fraction of itself, but this is suggestive at best and cannot be treated as proof. Notably, the fact that a value near 2,169 surfaces in the same passage that also reports 73.0% subsets leaves open the possibility that a subset size and a full-set size were conflated during document processing.

Weighing these factors, this report adopts **3,003 sentences as the best-supported figure for the full English–German WMT news-test2015 test set**, while explicitly flagging 2,169 sentences as the competing figure printed in the primary source's rendered text. Readers requiring a single citable number should note both.

## 4. Subset Sizes Used in the Length-Constrained Experiments

A second dimension of the answer concerns the subsets. The paper is explicit that the length-constrained exact-search experiments did not use the full test set: "all results in this section are conducted on only a subset of the test set to keep the runtime under control" ([Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090)). The reason given is computational: constraining search increases runtime because the γ-bounds become lower, and the authors stopped decoding if a single sentence took longer than a day on a single CPU ([Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090)).

### 4.1 The 73.0% Subset

One experiment — the histogram over length ratios under a minimum translation length constraint of 0.25 times the source sentence length — was "conducted on 7 3.0% of the test set" ([Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090)). The same 73.0% subset was used for the architecture comparison in Table 2, which evaluated a recurrent LSTM, SliceNet, Transformer-Base, and Transformer-Big ([Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090)).

### 4.2 The 48.3% Subset

The results in Tables 3 and 4, covering exact search under length constraints and exact search under length normalization, were "conducted on 4 8.3% of the test set" ([Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090)).

### Table 1. Summary of Test Set Sizes Reported in the Corpus

| Experimental Condition | Reported Test Set Size | Source |
|---|---|---|
| Full WMT news-test2015 English–German (main experiments) | 3,003 sentences | ([Third-party research note, n.d.](https://arxiv.org/abs/1908.10090)) |
| Full WMT news-test2015 English–German (as printed in paper text) | 2,169 sentences | ([Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090)) |
| Results without length constraints | Entire test set | ([Third-party research note, n.d.](https://arxiv.org/abs/1908.10090)) |
| Length-ratio histogram under minimum length constraint (Fig. 5) | 73.0% of test set | ([Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090)) |
| Architecture comparison (Table 2) | 73.0% of test set | ([Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090)) |
| Exact search under length constraints (Table 3) | 48.3% of test set | ([Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090)) |
| Exact search with length normalisation (Table 4) | 48.3% of test set | ([Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090)) |

## 5. Why the Test Set Size Matters Methodologically

The size of the test set is not merely a reporting detail; it conditions the interpretation of the paper's core conclusions. The finding that "the model often prefers the empty translation" and that "for more than 50% of the sentences, the model in fact assigns its global best score to the empty translation" is a claim about the frequency of a pathological model behaviour ([Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090)). Similarly, the reported search-error rates of 73.6% (greedy), 57.7% (Beam-10), and 53.6% (Beam-100) are frequencies whose precision depends on the denominator ([Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090)). The paper's own conclusion — that "vanilla NMT in its current form requires just the right amount of beam search errors," an outcome the authors call "highly unsatisfactory" — rests on exactly these proportions ([Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090)).

The subsetting decision also has interpretive consequences. Because the length-constrained results cover only 73.0% and 48.3% of the test set, the authors explicitly caution that those findings should not be read as full-corpus results ([Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090)). The length-normalisation experiment is a case in point: exact search under length normalisation "does not suffer from the length deficiency anymore… but it is not able to match our best BLEU score under Beam-1 0 search," a conclusion drawn from the 48.3% subset ([Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090)). Extrapolating that finding to the full test set requires an assumption of representativeness that the paper does not establish.

## 6. Conclusion

The test set size in Stahlberg and Byrne's study is reported as **3,003 sentences** for the full English–German WMT news-test2015 corpus used in the main, unconstrained experiments ([Third-party research note, n.d.](https://arxiv.org/abs/1908.10090)). This figure anchors the paper's headline search-error and empty-translation percentages. A competing figure of **2,169 sentences** appears in the rendered text of the primary source's experimental setup ([Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090)), and the two cannot be reconciled from the material provided. Given that the dedicated research note states 3,003 sentences explicitly and repeatedly as the full-set figure reported before subsetting, that value is the most defensible answer to the query, with the 2,169 figure recorded as a documented discrepancy. Separately, the length-constrained experiments drew on 73.0% and 48.3% subsets of the test set, which are distinct from the full-set size and should not be conflated with it ([Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090)).

## References

Stahlberg, F., & Byrne, B. (2019). *On NMT search errors and model errors: Cat got your tongue?* arXiv:1908.10090. https://arxiv.org/abs/1908.10090

Third-party research note. (n.d.). *On NMT search errors and model errors: Cat got your tongue?* [Research note; source: document_2.txt]. https://arxiv.org/abs/1908.10090