# Test Set Size in Stahlberg and Byrne's "On NMT Search Errors and Model Errors: Cat Got Your Tongue?"

## Direct Answer to the Query

The test set size reported in the paper *On NMT Search Errors and Model Errors: Cat Got Your Tongue?* is **2,169 sentences** — the full English–German WMT news-test2015 test set ([Stahlberg & Byrne, n.d.](document_1.txt)). The paper states, in its experimental setup for the results without length constraints, that "all our experiments in this section" were conducted "on the entire English-German WMT news-test2015 test set (2,169 sentences)" ([Stahlberg & Byrne, n.d.](document_1.txt)). A third-party research note supplied alongside the paper, however, reports the same test set as containing **3,003 sentences** ([Third-Party Research Note, n.d.](document_2.txt)). Because the two sources conflict, this report examines both figures, explains the surrounding experimental design, and states a reasoned position on which figure should be treated as authoritative.

## The Primary Source: What the Paper Itself Reports

### The Full Test Set Figure

The paper is unambiguous in its own experimental section. It reports that the full test set used for the headline exact-inference comparisons — greedy decoding, Beam-10, Beam-100, and exact search — is the "entire English-German WMT news-test2015 test set (2,169 sentences)" ([Stahlberg & Byrne, n.d.](document_1.txt)). The abstract reinforces the scope of the evaluation by describing the use of an exact search "to find the global best model scores under a Transformer base model for the entire WMT15 English-German test set" ([Stahlberg & Byrne, n.d.](document_1.txt)). The phrase "entire" is significant: it establishes that the main result table (Table 1 in the paper) captures every sentence in the test set, with no filtering, sampling, or exclusions.

### Consistency of the Reported Figure

The figure of 2,169 sentences is internally consistent with the rest of the paper's reporting conventions. The document is a machine-extracted OCR rendering in which numerals are frequently split by spaces — for example, "3 2,0 0 0" for a 32,000-token vocabulary, "1 0 0" for a beam size of 100, and "5 1.8%" for 51.8% ([Stahlberg & Byrne, n.d.](document_1.txt)). Applying the same reading convention, the string "(2,1 6 9 sentences)" resolves to 2,169 sentences. There is no other full-test-set size stated anywhere in the paper text, and no alternative sentence count accompanies the main results.

### The Context of the Main Experiments

Understanding the test set size requires understanding what was run on it. All experiments in the "Results without Length Constraints" section used a Transformer base model ([Vaswani et al., 2017, as cited in Stahlberg & Byrne, n.d.](document_1.txt)) trained with Tensor2Tensor on parallel WMT18 data excluding ParaCrawl, with preprocessing including joint subword segmentation via byte pair encoding using 32K merges, and with cased BLEU reported ([Stahlberg & Byrne, n.d.](document_1.txt)). On this full 2,169-sentence test set, the paper reports the following headline outcomes:

| Search strategy | BLEU | Length ratio | Search errors | Empty translations |
|---|---|---|---|---|
| Greedy | 29.3 | 1.02 | 73.6% | 0.0% |
| Beam-10 | 30.3 | 1.00 | 57.7% | 0.0% |
| Exact (unconstrained) | 2.1 | 0.06 | 0.0% | 51.8% |

*Data as reported in Table 1 of the paper ([Stahlberg & Byrne, n.d.](document_1.txt)).*

The scale of the test set matters to the interpretation of these numbers. The claim that "for more than 50% of the sentences, the model in fact assigns its global best score to the empty translation" is a frequency claim whose denominator is the 2,169-sentence test set ([Stahlberg & Byrne, n.d.](document_1.txt)). Similarly, the observation that even a beam size of 100 "produces 53.62% search errors" and that Beam-10 yields "15.9% fewer search errors (absolute) than greedy decoding (57.68% vs. 73.58%)" are all proportions computed over that same full test set ([Stahlberg & Byrne, n.d.](document_1.txt)).

## The Third-Party Research Note: A Competing Figure

### What the Note Claims

The third-party note asserts that "[t]he paper's main experiments use the entire English-German WMT news-test2015 test set of 3,003 sentences" and repeats this figure several times, adding that "[t]he paper reports this size in its experimental setup" and that "[t]his full test set size of 3,003 sentences is reported before any subset selection" ([Third-Party Research Note, n.d.](document_2.txt)). The note also correctly observes that the length-constrained experiments used only subsets of the test set, specifically 73.0% and 48.3% ([Third-Party Research Note, n.d.](document_2.txt)).

### Where the Note Agrees with the Paper

The note's descriptions of the experimental structure are accurate in several respects. It correctly identifies the test set as a news test set in the English–German language pair ([Third-Party Research Note, n.d.](document_2.txt)), which matches the paper's description of news-test2015 ([Stahlberg & Byrne, n.d.](document_1.txt)). It also correctly states that the length-constrained exact search results were conducted on "only a subset of the test set to keep the runtime under control," matching the paper's explanation that restricting search increases runtime because the γ-bounds are lower ([Stahlberg & Byrne, n.d.](document_1.txt)). It further correctly notes that "one experiment uses 73.0% of the test set" and that "other experiments use 48.3% of the test set" ([Third-Party Research Note, n.d.](document_2.txt)), which aligns with the captions of Tables 3 and 4 and Figure 5 in the paper ([Stahlberg & Byrne, n.d.](document_1.txt)).

### Where the Note Diverges

The single substantive divergence is the sentence count. The paper's own text supplies 2,169 sentences as the full test set size; the note supplies 3,003 ([Stahlberg & Byrne, n.d.](document_1.txt); [Third-Party Research Note, n.d.](document_2.txt)). No figure of 3,003 appears anywhere in the paper text provided. The note does not explain how the number was derived, nor does it quote the paper's sentence verbatim; it simply asserts that the paper "states the test set size as a number of sentences" and gives 3,003 ([Third-Party Research Note, n.d.](document_2.txt)). Given that the primary source is the paper and the note is a secondary summary, and given that the note contains no independent measurement or derivation, the discrepancy most plausibly reflects an error introduced in the secondary note rather than in the paper.

## Subset Experiments and Why They Are Not the Test Set Size

It is important not to conflate the subsets used in the length-constrained experiments with the full test set size. The paper reports that results in the "Results with Length Constraints" section were conducted on only a subset to keep runtime under control, and that decoding was stopped if a single sentence took longer than a day on a single CPU ([Stahlberg & Byrne, n.d.](document_1.txt)). The specific subsets are documented in the paper's table and figure captions:

| Experiment | Portion of test set | Source |
|---|---|---|
| Minimum-length constraint of 0.25 × source length (Fig. 5) | 73.0% | ([Stahlberg & Byrne, n.d.](document_1.txt)) |
| Exact search under length constraints (Tables 3 and 4) | 48.3% | ([Stahlberg & Byrne, n.d.](document_1.txt)) |

On the 48.3% subset, the paper reports that exact search constrained to the Beam-10 hypothesis length produced 37.0 BLEU with a length ratio of 1.00, identical to Beam-10, whereas the oracle experiment constrained to the reference length reached 37.9 BLEU ([Stahlberg & Byrne, n.d.](document_1.txt)). Under length normalization on the same subset, exact search reached 36.4 BLEU compared with 37.0 for Beam-10 without normalization ([Stahlberg & Byrne, n.d.](document_1.txt)). These figures describe a subset, not the full test set, and should never be reported as the test set size.

### Summary of Reported Sizes

| Reported item | Value | Scope | Source |
|---|---|---|---|
| Full WMT15 English–German news-test2015 test set | 2,169 sentences | Main experiments (no length constraints) | ([Stahlberg & Byrne, n.d.](document_1.txt)) |
| Full test set (alternative claim) | 3,003 sentences | Main experiments | ([Third-Party Research Note, n.d.](document_2.txt)) |
| Length-constrained experiment subset | 73.0% of test set | Fig. 5 experiment | ([Stahlberg & Byrne, n.d.](document_1.txt)) |
| Length-constrained exact search subset | 48.3% of test set | Tables 3 and 4 | ([Stahlberg & Byrne, n.d.](document_1.txt)) |

## Assessing Reliability of the Two Sources

The two documents are not of equal evidential weight. Document 1 is the paper itself, containing the experimental setup, the algorithms (BeamSearch and DFS), the results tables, and the accompanying discussion ([Stahlberg & Byrne, n.d.](document_1.txt)). Its sentence count appears in the same passage that specifies the model configuration, the preprocessing pipeline, the BPE merge count, and the BLEU variant — details that routinely accompany test set descriptions in machine translation papers. Document 2 is explicitly labeled a "third-party research note" and is organized around a list of key questions rather than around the paper's narrative ([Third-Party Research Note, n.d.](document_2.txt)). It offers assertions about the paper without quoting the underlying passage.

Applying the principle of prioritizing the most reliable and proximate source, the paper's own statement should govern. The paper's figure of 2,169 sentences is the one embedded in the experimental description; the note's figure of 3,003 appears only in a secondary commentary. My concrete assessment is therefore that **the test set size for the main experiments is 2,169 sentences**, and that the 3,003 figure should be treated as an unverified and probably erroneous restatement.

This matters beyond bookkeeping. Several of the paper's central claims are stated as proportions of sentences: that beam search fails to find the global best model score in "more than half of the sentences," that "51.8%" of sentences have the empty translation as the global best, and that greedy decoding produces 73.6% search errors ([Stahlberg & Byrne, n.d.](document_1.txt)). The paper also shows that search errors and empty-translation behavior are not Transformer-specific: the LSTM model showed 58.4% search errors and 47.7% empty translations, SliceNet showed 46.0% and 41.2%, Transformer-Base showed 57.7% and 51.8%, and Transformer-Big showed 32.1% and 25.8% ([Stahlberg & Byrne, n.d.](document_1.txt)). Every one of these percentages is a fraction of the full test set, so an incorrect denominator propagates directly into an incorrect impression of how widespread the reported failure modes are.

## Conclusion

The answer to the query "what is the test set size?" is that the paper's main experiments use the entire English–German WMT news-test2015 test set, which the paper itself reports as **2,169 sentences** ([Stahlberg & Byrne, n.d.](document_1.txt)). The competing figure of 3,003 sentences originates solely from a third-party research note ([Third-Party Research Note, n.d.](document_2.txt)) and is not corroborated by the primary text. Separately, the length-constrained exact search experiments used only subsets of the test set — 73.0% and 48.3% — chosen to keep runtime under control because constrained search lowers the pruning bounds and thereby increases decoding time ([Stahlberg & Byrne, n.d.](document_1.txt)). Readers should therefore cite 2,169 sentences as the full test set size, attribute that figure to the paper's experimental setup, and describe the length-constrained results explicitly as subset-based rather than as evaluations over the full test set.

## References

Stahlberg, F., & Byrne, B. (n.d.). *On NMT search errors and model errors: Cat got your tongue?* [Document 1]. University of Cambridge, Department of Engineering. (document_1.txt)

Third-party research note: On NMT search errors and model errors: Cat got your tongue? (n.d.). [Document 2]. (document_2.txt)