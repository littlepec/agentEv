# Test Set Size in *On NMT Search Errors and Model Errors: Cat Got Your Tongue?*: A Detailed Assessment

## Executive Summary

The question of how large the test set is in the neural machine translation (NMT) study on search errors and model errors has a direct and citable answer in the primary source, but that answer is contradicted by a secondary research note. The primary source document — the text of the paper itself — states unambiguously that the experiments reported in the unconstrained-search section were conducted on "the entire English-German WMT news-test2015 test set (2,169 sentences)" ([document_1.txt](document_1.txt)). A separate third-party research note, in contrast, asserts that the same test set contains 3,003 sentences ([document_2.txt](document_2.txt)).

After weighing source primacy, internal consistency, and the arithmetic behaviour of the reported subset percentages, this report concludes that **2,169 sentences is the figure that should be treated as the paper's stated test set size**, while 3,003 sentences appears to be an erroneous attribution in the secondary note. The remainder of this report documents the evidence, the nature of the conflict, and the implications of that conflict for interpreting the paper's headline results.

## 1. The Query and Why the Test Set Size Matters

The size of a test set is not a cosmetic detail in empirical machine translation research. It determines the statistical resolution of every reported metric, governs how sensitive an evaluation is to individual pathological sentences, and conditions how much weight a reader should give to claims about error rates. In the case of the paper under discussion, the central claims concern the *proportion of sentences* affected by search errors and by a model-level bias toward empty translations — quantities that are meaningless without a denominator.

Specifically, the paper reports that for 51.8% of sentences the model assigns its global best score to the empty translation, that Beam-10 produces 57.68% search errors, and that a beam size of 100 still produces 53.62% search errors ([document_1.txt](document_1.txt)). Each of these percentages is computed over the test set. If the denominator were misreported, a reader attempting to reproduce or audit the analysis would be working from an incorrect base.

## 2. Direct Evidence from the Primary Source

### 2.1 The Stated Full Test Set Size

The paper's experimental section on results *without* length constraints begins with an explicit statement of the evaluation data:

> "We conduct all our experiments in this section on the entire English-German WMT news-test2015 test set (2,169 sentences) with a Transformer base (Vaswani et al. 2017) model trained with Tensor2Tensor (Vaswani et al. 2018) on parallel WMT18 data excluding ParaCrawl." ([document_1.txt](document_1.txt))

Several features of this sentence are noteworthy. First, the size is given parenthetically, immediately adjacent to the name of the test set, which is the conventional location for a precise specification in an NLP experimental-setup description. Second, the statement specifies that the *entire* test set was used, which distinguishes this section from the length-constrained experiments described later. Third, the sentence situates the size within a full description of the experimental apparatus — model architecture, training framework, training data, preprocessing, and metric — which increases the credibility of the figure as a deliberate, verified detail rather than an offhand remark.

The paper also describes the preprocessing pipeline: joint subword segmentation using byte pair encoding with 32K merges, following Stahlberg et al. (2018a), and reports cased BLEU scores ([document_1.txt](document_1.txt)). A vocabulary size of |𝒯| = 32,000 is separately noted in the discussion of the search space ([document_1.txt](document_1.txt)). All of these details belong to the same methodological description as the test set figure, reinforcing that it was recorded deliberately.

### 2.2 Subset Sizes Used in the Length-Constrained Experiments

The paper's second set of experiments, which impose minimum translation-length constraints, does not use the full test set. The authors state plainly that "all results in this section are conducted on only a subset of the test set to keep the runtime under control" ([document_1.txt](document_1.txt)). Two distinct subset fractions are reported:

| Experiment (length-constrained section) | Fraction of test set | Stated in source |
|---|---|---|
| Histogram with minimum translation length of 0.25 × source length | 73.0% | ([document_1.txt](document_1.txt)) |
| Exact search under length constraints (Tables 3 and 4) | 48.3% | ([document_1.txt](document_1.txt)) |
| Full test set (unconstrained experiments) | 100% (2,169 sentences) | ([document_1.txt](document_1.txt)) |

The paper justifies the subsetting on computational grounds: exact search with length constraints is slower because the admissible pruning bounds (γ-bounds) are lower, and the authors "stopped decoding if the decoder took longer than a day for a single sentence on a single CPU," whereas "exact search without length constraints is much faster and does not need maximum execution time limits" ([document_1.txt](document_1.txt)).

### 2.3 Summary of All Test-Set-Related Figures in the Primary Source

| Figure | Value | Scope | Source |
|---|---|---|---|
| Full WMT news-test2015 English-German test set | 2,169 sentences | Unconstrained exact-search experiments | ([document_1.txt](document_1.txt)) |
| Subset for minimum-length-0.25 histogram | 73.0% | Length-constrained | ([document_1.txt](document_1.txt)) |
| Subset for length-constrained exact search | 48.3% | Length-constrained | ([document_1.txt](document_1.txt)) |
| Vocabulary size | 32,000 subword units | Model configuration | ([document_1.txt](document_1.txt)) |

## 3. The Conflicting Figure in the Secondary Source

### 3.1 What the Secondary Note Asserts

The third-party research note states, repeatedly and emphatically, that the paper's main experiments used "the entire English-German WMT news-test2015 test set of 3,003 sentences" and that "the entire English-German WMT news-test2015 test set contains 3,003 sentences" ([document_2.txt](document_2.txt)). The note further asserts that "this full test set size of 3,003 sentences is reported before any subset selection" and that the figure is "reported in its experimental setup" ([document_2.txt](document_2.txt)).

The note also identifies the subset percentages — 73.0% and 48.3% — correctly, matching the primary source ([document_2.txt](document_2.txt); [document_1.txt](document_1.txt)). This partial agreement is important: it indicates the note's author had access to the paper's length-constrained section and read it with reasonable care, which makes the divergence on the headline figure more likely to be a specific error of attribution than a wholesale fabrication.

### 3.2 Why the Conflict Cannot Be Silently Ignored

If a reader takes the secondary note at face value, the denominator for every reported error rate changes. A 51.8% empty-translation rate over 2,169 sentences corresponds to roughly 1,124 sentences; over 3,003 sentences it would correspond to roughly 1,556 sentences. Similarly, the 73.0% subset would cover approximately 1,583 sentences under the primary figure but approximately 2,192 under the secondary figure. These are materially different quantities, and the discrepancy therefore has consequences for anyone attempting replication, meta-analysis, or secondary use of the findings.

## 4. Source Prioritization and Reconciliation

### 4.1 Primacy and Proximity to the Data

The most defensible principle when two sources conflict is to prefer the source closest to the underlying evidence. Here, document_1 consists of the paper's own text — the experimental section, the algorithm descriptions, the tables, the conclusions, and the bibliography. Document_2 is explicitly labelled a "Third-party research note" ([document_2.txt](document_2.txt)). A third-party note, however carefully prepared, is at best a derivation from the primary text and at worst a paraphrase that can introduce transcription errors. The primary text states its own test set size in the first sentence of its results section; the note asserts a different number without quoting any passage from the paper that contains it.

### 4.2 Internal Consistency Checks

A further consideration is internal consistency. The primary source's narrative hangs together coherently around a full-set figure and two subset figures. Beyond that, the paper recounts specific qualitative findings that presuppose a test set of the stated scale, such as the observation that "long source sentences are more affected by both beam search errors and the problem of empty translations" and that "the global best translation is empty for almost all sentences longer than 40 tokens" ([document_1.txt](document_1.txt)). Nothing in the primary text requires a 3,003-sentence set, and no passage in it mentions such a number.

By contrast, the secondary note's 3,003 figure is not corroborated anywhere else in the supplied materials. It appears three times in the note, but repetition within a single secondary document does not constitute independent confirmation.

### 4.3 Assessment

On the available evidence, the sound conclusion is that **the paper reports its test set size as 2,169 sentences**, and that the 3,003-sentence figure in the third-party note is unreliable. The residual possibility that the paper elsewhere describes a larger pool from which 2,169 sentences were drawn cannot be ruled out from the excerpts provided, but the excerpts are explicit: the experiment was conducted on "the entire English-German WMT news-test2015 test set (2,169 sentences)" ([document_1.txt](document_1.txt)). It is worth noting, as a plausible explanation of the discrepancy, that different WMT news test sets across years have different sizes; a note that conflated one year's release with another's would produce precisely this kind of mismatch, and would still reproduce the subset percentages correctly if those percentages were copied from the right section.

## 5. Why the Full-Set Versus Subset Distinction Matters for the Paper's Findings

### 5.1 Search Errors

The paper's headline comparison is reproduced below from Table 1 of the primary source ([document_1.txt](document_1.txt)):

| Search method | BLEU | Ratio | Search errors | Empty translations |
|---|---|---|---|---|
| Greedy | 29.3 | 1.02 | 73.6% | 0.0% |
| Beam-10 | 30.3 | 1.00 | 57.7% | 0.0% |
| Exact | 2.1 | 0.06 | 0.0% | 51.8% |

The interpretation of this table is the paper's central contribution: greedy and beam search achieve superficially reasonable BLEU scores only because they commit a large number of search errors, and once search is performed exactly, the BLEU score collapses to 2.1 because the model itself prefers the empty translation in a majority of cases ([document_1.txt](document_1.txt)). These figures belong to the full-test-set, unconstrained-search condition. Their force depends on the test set being a complete, standard benchmark rather than a convenient subset — which is exactly what the primary source claims for the unconstrained experiments ([document_1.txt](document_1.txt)).

### 5.2 The Effect of Beam Size

The paper also shows that increasing the beam improves search only marginally while damaging output length: "Even a large beam size of 100 produces 53.62% search errors," and "Beam-10 yields 15.9% fewer search errors (absolute) than greedy decoding (57.68% vs. 73.58%), but Beam-100 improves search only slightly (53.62% search errors) despite being 10 times slower than beam-10" ([document_1.txt](document_1.txt)). The authors link this to a length bias: "large beam sizes reduce the number of search errors, but the BLEU score drops because translations are too short" ([document_1.txt](document_1.txt)).

### 5.3 Length-Constrained Results and Subset Dependence

The length-constrained tables are explicitly computed on 48.3% of the test set ([document_1.txt](document_1.txt)):

| Search | BLEU (w/o length norm) | Ratio | BLEU (with length norm) | Ratio |
|---|---|---|---|---|
| Beam-10 | 37.0 | 1.00 | 36.3 | 1.03 |
| Beam-30 | 36.7 | 0.98 | 36.3 | 1.04 |
| Exact | 27.2 | 0.74 | 36.4 | 1.03 |

Constraining exact search to the reference length improved BLEU by 0.9 points, whereas constraining it to the Beam-10 hypothesis length produced no improvement over beam search — evidence, the authors argue, that the remaining search errors at that length are immaterial to BLEU ([document_1.txt](document_1.txt)). The authors conclude that length normalization "fixes translation lengths, but prevents exact search from matching the BLEU score of Beam-10" ([document_1.txt](document_1.txt)).

The important point for the present query is that the *subset* percentages in these tables are only interpretable relative to a known full-set size. Reporting 48.3% without knowing whether the denominator is 2,169 or 3,003 leaves the effective sample size — and thus the precision of the reported BLEU differences — indeterminate.

### 5.4 Generality Beyond One Architecture

The paper reports that the problem is not specific to the Transformer base model: "Even a highly optimized Transformer Big model from our WMT18 shared task submission (Stahlberg et al. 2018a) has 25.8% empty translations" ([document_1.txt](document_1.txt)). This cross-architecture check strengthens the model-error claim, and again is stated in the context of the full test set.

## 6. Broader Methodological Reflections on Test Set Sizing in NMT

The paper itself frames its contribution as the first to quantify search errors exactly: "To the best of our knowledge, this is the first work that reports the exact number of search errors in NMT as prior work often relied on approximations, e.g. via n-best lists (Niehues et al. 2017) or constraints (Stahlberg et al. 2018b)" ([document_1.txt](document_1.txt)). Achieving this required an exact inference scheme that, while too slow for practical MT, "guarantees to find the global best model score for analysis purposes" ([document_1.txt](document_1.txt)). Because exact search is expensive, the authors were compelled to subsample for the length-constrained conditions, and they were transparent about doing so. That transparency is precisely why an accurate reading of the full-set size is essential: the paper's credibility rests on a clear distinction between 100%-scale experiments and deliberately reduced-scale ones.

The paper also notes that the NMT search space is vast: with a vocabulary of 32,000, "there are already more possible translations with 20 words or less than atoms in the observable universe (32,000²⁰ ≫ 10⁸²)" ([document_1.txt](document_1.txt)). This combinatorial argument explains why exact search over a full test set is a meaningful computational achievement, and why the size of that set — 2,169 sentences rather than 3,003 — is itself relevant information about the scale of the computation.

Finally, the authors situate their finding within a literature attributing length bias to the training objective, citing Sountsov and Sarawagi (2016) for the argument that "this model error is due to the locally normalized maximum likelihood training objective in NMT that underestimates the margin between the correct translation and shorter ones if trained with regularization and finite data" ([document_1.txt](document_1.txt)), and concluding that length normalization and word rewards are "rather heuristic as they do not have any justification from a probabilistic perspective" ([document_1.txt](document_1.txt)).

## 7. Conclusion

**The test set size reported in the primary source is 2,169 sentences**, corresponding to the entire English-German WMT news-test2015 test set used in the unconstrained exact-search experiments ([document_1.txt](document_1.txt)). Length-constrained experiments used subsets of this set, specifically 73.0% for the histogram analysis under a minimum-length constraint of 0.25 times the source length, and 48.3% for the length-constrained exact-search comparisons ([document_1.txt](document_1.txt)). The competing figure of 3,003 sentences advanced by the third-party research note ([document_2.txt](document_2.txt)) is not supported by any passage of the primary text and should be treated as an unreliable attribution, notwithstanding that the note reproduces the subset percentages correctly.

For readers engaged in reproducing or extending this work, the practical implication is straightforward: any re-derivation of the reported error rates and percentages should use 2,169 as the full-test-set denominator, and should use the stated fraction — not a recomputed one — for the length-constrained conditions. The paper's core conclusion, that "vanilla NMT in its current form requires just the right amount of beam search errors" and that the model frequently prefers the empty translation, rests on a benchmark that is fully specified, and the specification is 2,169 sentences ([document_1.txt](document_1.txt)).

## References

document_1.txt. (n.d.). *On NMT search errors and model errors: Cat got your tongue?* [Primary source document; includes experimental setup, results tables, and bibliography].

document_2.txt. (n.d.). *Third-party research note: On NMT search errors and model errors: Cat got your tongue?* [Secondary source document; includes claims about test set size and subset selection].