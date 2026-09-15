# What Is the Test Set Size? Evidence from *On NMT Search Errors and Model Errors: Cat Got Your Tongue?*

## Executive Summary

The test set that underpins the principal experiments in Stahlberg and Byrne's study of neural machine translation (NMT) search errors and model errors is the **entire English–German WMT news-test2015 test set**, which the paper reports as consisting of **2,169 sentences** ([Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090)). This figure is stated directly in the experimental setup of the paper's "Results without Length Constraints" section — the section that carries the study's headline findings on exact inference ([Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090)). A third-party research note included in the source material asserts a competing figure of **3,003 sentences** for the same test set ([Third-party research note, n.d.](document_2.txt)). Because the primary source is the paper itself and states the size explicitly and consistently, while the secondary note is uncorroborated and internally derivative, the reliable answer to the query is **2,169 sentences**. The remainder of this report documents the evidence, evaluates the conflict between the two figures, and explains how the subset experiments reported later in the paper should be interpreted.

## 1. Background: Why the Test Set Size Is a Material Fact

The paper addresses a fundamental question in NMT: how often does beam search, the standard decoding algorithm, fail to find the translation that the model itself assigns the highest probability ([Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090))? To answer this rigorously, the authors introduce an exact inference procedure that combines beam search with depth-first search (DFS) and is guaranteed to return the global best model score for analysis purposes, even though it is too slow for practical translation ([Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090)). Because exact decoding must be run once per source sentence, the size of the evaluation set is not a trivial experimental detail — it directly determines the number of sentences over which the reported percentages of search errors and empty translations are computed, and it governs the practicality of the exact-search experiments ([Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090)). Establishing the correct test set size is therefore necessary for interpreting every headline number in the paper, including the claim that beam search fails to find the global best model score for more than half of the sentences ([Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090)).

## 2. The Primary Source: 2,169 Sentences

### 2.1 The Direct Statement in the Experimental Setup

The most direct and authoritative statement appears in Section 3 of the paper, "Results without Length Constraints." The authors write: "We conduct all our experiments in this section on the entire English-German WMT news-test2015 test set (2,169 sentences) with a Transformer base model trained with Tensor2Tensor on parallel WMT18 data excluding ParaCrawl" ([Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090)). This sentence is unambiguous on three points: the test set is the WMT news-test2015 set for the English–German language pair; the experiments use the *entire* set; and the entire set contains 2,169 sentences ([Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090)).

### 2.2 Corroborating Signals Within the Paper

Additional details in the paper are consistent with a 2,169-sentence full test set and reinforce the reliability of that number. First, the abstract describes the evaluation as covering "the entire WMT15 English-German test set," confirming that the relevant benchmark is the 2015 news test rather than a different year's data ([Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090)). Second, the paper reports that all results in the later "Results with Length Constraints" section were run on "only a subset of the test set to keep the runtime under control," which presupposes a defined full set from which subsets are drawn — the same full set described as having 2,169 sentences ([Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090)). Third, the paper notes that exact search without length constraints is comparatively fast, whereas the constrained search required per-sentence execution time limits, again implying that the full-set experiments were feasible only because the set was of manageable size ([Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090)). All of these statements cohere around the 2,169 figure.

## 3. The Conflicting Claim: 3,003 Sentences

### 3.1 What the Third-Party Note Asserts

The secondary source in the material is a "third-party research note" that repeatedly claims the paper's main experiments use a test set of 3,003 sentences and that the full English–German WMT news-test2015 set "contains 3,003 sentences" ([Third-party research note, n.d.](document_2.txt)). It further asserts that this full-set size "is reported before any subset selection" and that the subset experiments (73.0% and 48.3%) are "distinct from the full test set size of 3,003 sentences" ([Third-party research note, n.d.](document_2.txt)).

### 3.2 Reliability Assessment of the Two Sources

Applying standard source-evaluation criteria — relevance, reliability, and significance — the balance is clearly in favor of the primary document. The paper text itself is the object of study: it is the source that defines the experiment, and its statement of the test set size is embedded in the methodological description of that experiment ([Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090)). The third-party note, by contrast, does not report an independent measurement or an alternative citation; it paraphrases the same paper and arrives at a number that the paper never states ([Third-party research note, n.d.](document_2.txt)). Notably, the note's own framing repeats the phrase "the paper reports" while attributing to the paper a figure that does not appear in the primary text, which is a hallmark of an inferential or transcription error rather than an independent finding ([Third-party research note, n.d.](document_2.txt)).

| Source | Reported full test set size | Basis | Reliability assessment |
|---|---|---|---|
| Stahlberg & Byrne (2019) — primary paper | 2,169 sentences | Explicit statement in Section 3 experimental setup ([Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090)) | High: primary, specific, methodologically placed |
| Third-party research note | 3,003 sentences | Repeated paraphrase with no citation to a differing location ([Third-party research note, n.d.](document_2.txt)) | Low: secondary, uncorroborated, contradicted by the primary text |

A plausible explanation for the discrepancy is confusion between different vintages of the WMT news test sets, which have varied in size across years; the note may have carried over a sentence count associated with a differently sized release and attached it to the 2015 set ([Third-party research note, n.d.](document_2.txt)). Whatever the precise origin, the note's figure cannot override an explicit, internally consistent statement in the paper it purports to summarize ([Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090)).

## 4. Reconciling the Two Figures: A Concrete Position

Based on the evidence above, the position adopted in this report is that **the test set size is 2,169 sentences**, and that the 3,003-sentence claim is erroneous ([Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090); [Third-party research note, n.d.](document_2.txt)). Three considerations drive this conclusion.

First, the paper supplies the number in the precise location where experimental parameters belong — the description of the data used for the main results — rather than in an incidental aside ([Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090)). Second, the paper's own internal logic depends on the full set being defined before subsets are carved out, and it defines that full set as 2,169 sentences ([Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090)). Third, the secondary note provides no independent evidence, only repetition, and its claims conflict with the primary record on the central quantity it purports to clarify ([Third-party research note, n.d.](document_2.txt)).

## 5. Subsets Used in the Length-Constrained Experiments

Although the full test set comprises 2,169 sentences, the paper's later experiments deliberately reduce the evaluation scope. The authors state that constraining search increases runtime because the lower bounds become weaker, so "all results in this section are conducted on only a subset of the test set to keep the runtime under control" ([Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090)). Two subset fractions are reported: the minimum-translation-length histogram (Figure 5) was computed on **73.0% of the test set**, while the length-constrained exact search experiments in Tables 3 and 4 were conducted on **48.3% of the test set** ([Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090)). Applying these percentages to the full-set figure of 2,169 sentences yields the approximate sentence counts shown below; the arithmetic is derived from the percentages reported in the paper and is presented here only to illustrate scale ([Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090)).

| Experiment | Reported fraction of test set | Approximate sentences (based on 2,169) | Source |
|---|---|---|---|
| Full test set (Sections 3, Tables 1–2, Figures 1–4) | 100% | 2,169 | ([Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090)) |
| Minimum-length-constraint histogram (Figure 5) | 73.0% | ≈1,583 | ([Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090)) |
| Length-constrained exact search (Tables 3–4) | 48.3% | ≈1,048 | ([Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090)) |

It is important to keep these subsets distinct from the full test set: the 73.0% and 48.3% figures describe *coverage of* the 2,169-sentence set, not separate test sets ([Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090)).

## 6. Why the Size Matters for Interpreting the Results

The full-set size of 2,169 sentences is the denominator behind the study's most cited statistics. On that set, greedy decoding produced 73.6% search errors, Beam-10 produced 57.7%, and even a very large beam of 100 produced 53.62% search errors, while exact inference revealed that for 51.8% of sentences the model assigned its global best score to the empty translation ([Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090)). The paper also reports that the problem is not specific to the Transformer-base architecture: an LSTM system showed 58.4% search errors and 47.7% empty translations, a SliceNet system showed 46.0% and 41.2%, and a highly optimized Transformer-Big system still produced 25.8% empty translations ([Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090)). Each of these percentages is computed over the sentences of the full evaluation set; an incorrect premise about the set's size would distort the implied counts and weaken any attempt to reproduce or audit the study ([Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090)).

## 7. Conclusion

The answer to the query "what is the test set size?" is that the paper's main experiments use the entire English–German WMT news-test2015 test set of **2,169 sentences** ([Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090)). The length-constrained follow-up experiments deliberately operate on subsets of that set, at 73.0% and 48.3% coverage respectively, in order to keep the more expensive exact search tractable ([Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090)). The competing figure of 3,003 sentences advanced by the third-party note should be treated as unreliable: it is absent from the primary text, uncorroborated by any independent measurement, and contradicted by the paper's explicit experimental description ([Third-party research note, n.d.](document_2.txt); [Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090)). Where a secondary summary conflicts with the primary source on a straightforward, explicitly stated parameter, the primary source should govern — and in this case it points unambiguously to 2,169 sentences ([Stahlberg & Byrne, 2019](https://arxiv.org/abs/1908.10090)).

## References

Stahlberg, F., & Byrne, B. (2019). *On NMT search errors and model errors: Cat got your tongue?* arXiv:1908.10090. https://arxiv.org/abs/1908.10090

Third-party research note: *On NMT search errors and model errors: Cat got your tongue?* (n.d.). [document_2.txt](document_2.txt)