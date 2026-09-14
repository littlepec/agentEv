# How Much Does the Embedding (Semantic Similarity) Approach Outperform BM25? A Critical Reading of the TREC 2006–2007 Evidence

## Executive Summary

The question presupposes that the embedding-based semantic similarity measure ("SEM") outperforms BM25, and asks for the size of that advantage. The evidence supplied does not permit a single, uncontested numerical answer, because the two available sources make **directly contradictory directional claims** while agreeing on the exact magnitudes involved — 19% on TREC 2006 and 6% on TREC 2007 ([document_1.txt](https://arxiv.org/abs/1608.01972); [document_2.txt](#ref-document2)).

Weighted by source reliability, the best-supported answer is that **the embedding approach improves average precision over BM25 by 19% on TREC 2006 and by 6% on TREC 2007**. This is the reading of the primary research paper, which reports that "the embedding approach boosts the average precision of BM25 by 19% and 6% on TREC 2006 and 2007, respectively" ([document_1.txt](https://arxiv.org/abs/1608.01972)). However, a third-party research note states the exact inverse, namely that "BM25 raises average precision by 19% on TREC 2006 and by 6% on TREC 2007 over the embedding approach" ([document_2.txt](#ref-document2)). Any responsible answer must therefore present the 19%/6% figures together with an explicit statement of which direction is being claimed and why the primary source is preferred.

## 1. The Query and the Problem with Its Premise

The task asks a single, apparently simple question: *By how much does their similarity measure (the embedding approach) outperform BM25?* Answering it requires three separate operations:

1. Confirming the **direction** of the effect (does the embedding method beat BM25, or the reverse?).
2. Extracting the **magnitude** of the effect on each reported collection.
3. Assessing whether the source material is **internally consistent** enough to support the magnitude claim.

Steps 1 and 3 are where the supplied evidence becomes problematic. Both sources report the same two benchmark years and the same two numbers — TREC 2006 and TREC 2007, with 19% and 6% respectively — but they attach those numbers to opposite comparators ([document_1.txt](https://arxiv.org/abs/1608.01972); [document_2.txt](#ref-document2)). Identical magnitudes with inverted direction is a classic signature of a secondary source misreading a primary one, but it cannot be resolved by arithmetic alone. It must be resolved by source criticism.

## 2. The Evidence Base: Two Sources, Two Opposite Claims

### 2.1 The primary paper (document_1.txt)

The first source is identified as a paper, "Bridging the Gap: Incorporating a Semantic Similarity Measure for Effectively Mapping PubMed Queries to Documents" (arXiv:1608.01972), and the excerpt is drawn specifically from its "TREC Experiments" section ([document_1.txt](https://arxiv.org/abs/1608.01972)). It makes three claims:

- **BM25 outperforms TF-IDF and CENTROID**, as shown in Table 4 of the paper ([document_1.txt](https://arxiv.org/abs/1608.01972)).
- **The embedding approach boosts the average precision of BM25 by 19% and 6% on TREC 2006 and 2007, respectively** ([document_1.txt](https://arxiv.org/abs/1608.01972)).
- **CENTROID scores lower than both BM25 and the SEM approach** ([document_1.txt](https://arxiv.org/abs/1608.01972)).

Taken together, these three statements describe a coherent ordering: the semantic/embedding method sits at the top, BM25 is a strong lexical baseline beneath it, and both TF-IDF and centroid-based retrieval fall below BM25, with CENTROID at the bottom. A paper titled "Bridging the Gap" — i.e., proposing to close the gap between lexical retrieval and semantic matching — is also consistent with reporting an *improvement* attributed to the semantic component. Since the excerpt names a specific table (Table 4) and a specific benchmark (TREC 2006, 2007), it reads as a direct report of the paper's own results rather than a paraphrase of someone else's.

### 2.2 The third-party research note (document_2.txt)

The second source is described only as a "Third-party research note: PubMed query-document mapping" ([document_2.txt](#ref-document2)). It states that "BM25 outperforms the proposed semantic-similarity (embedding) approach: BM25 raises average precision by 19% on TREC 2006 and by 6% on TREC 2007 over the embedding approach," and adds that BM25 outperforms TF-IDF and CENTROID while CENTROID scores below both BM25 and the embedding approach ([document_2.txt](#ref-document2)).

Notably, the note also explicitly attributes its information back to *document_1.txt* ("Source: document_1.txt") ([document_2.txt](#ref-document2)). It is therefore not an independent experiment or a replication; it is a restatement of the primary paper's findings.

### 2.3 Side-by-side comparison

| Feature | document_1.txt (primary paper) | document_2.txt (third-party note) |
|---|---|---|
| Nature of source | Research paper, "TREC Experiments" section ([document_1.txt](https://arxiv.org/abs/1608.01972)) | Commentary/research note on the same study ([document_2.txt](#ref-document2)) |
| Claimed direction, TREC 2006 | Embedding boosts BM25 by 19% ([document_1.txt](https://arxiv.org/abs/1608.01972)) | BM25 beats embedding by 19% ([document_2.txt](#ref-document2)) |
| Claimed direction, TREC 2007 | Embedding boosts BM25 by 6% ([document_1.txt](https://arxiv.org/abs/1608.01972)) | BM25 beats embedding by 6% ([document_2.txt](#ref-document2)) |
| BM25 vs. TF-IDF | BM25 better ([document_1.txt](https://arxiv.org/abs/1608.01972)) | BM25 better ([document_2.txt](#ref-document2)) |
| BM25 vs. CENTROID | BM25 better ([document_1.txt](https://arxiv.org/abs/1608.01972)) | BM25 better ([document_2.txt](#ref-document2)) |
| Embedding vs. CENTROID | Embedding better ([document_1.txt](https://arxiv.org/abs/1608.01972)) | Embedding better ([document_2.txt](#ref-document2)) |
| Magnitudes agreed? | 19% / 6% | 19% / 6% |
| Directions agreed? | — | **No — inverted** |

The table makes the disagreement unusually narrow: every comparison except the central one (embedding vs. BM25) is identical across the two sources. The dispute is confined entirely to which of the two top-performing systems is the winner, and by how much.

## 3. Source Reliability Assessment

Because the two documents are mutually exclusive on direction, the answer to the query must be derived by ranking the sources rather than by averaging them.

### 3.1 Provenance

The primary source is a named paper with a stable identifier (arXiv:1608.01972) and an identified section and table ("Table 4") from which the numbers are drawn ([document_1.txt](https://arxiv.org/abs/1608.01972)). It is, in the terminology of evidence hierarchies, a **primary empirical report**: the figures originate with the authors who ran the experiments. The second source is self-described as a "third-party research note" and does not present any experimental apparatus of its own ([document_2.txt](#ref-document2)).

### 3.2 Derivative status

The third-party note cites document_1.txt as its source ([document_2.txt](#ref-document2)). This is decisive for reliability purposes. A derivative source has no independent evidential weight on the underlying measurement; it can only transmit or distort the primary report. When a derivative source contradicts its own cited primary source, the appropriate resolution is to prefer the primary source, unless there is separate evidence that the primary source is wrong — and no such evidence is present here.

### 3.3 Internal consistency

Both documents are internally consistent in isolation. The primary paper's three claims (BM25 > TF-IDF, BM25 > CENTROID, SEM > BM25) form a consistent ranking with SEM at the top ([document_1.txt](https://arxiv.org/abs/1608.01972)). The note's claims (BM25 > TF-IDF, BM25 > CENTROID, BM25 > SEM) likewise form a consistent ranking with BM25 at the top ([document_2.txt](#ref-document2)). Internal consistency therefore does not discriminate between them; only provenance, direction of derivation, and the title and framing of the underlying study do.

### 3.4 Reliability criteria applied

| Criterion | document_1.txt | document_2.txt |
|---|---|---|
| Named publication venue/identifier | Yes (arXiv:1608.01972) ([document_1.txt](https://arxiv.org/abs/1608.01972)) | No ([document_2.txt](#ref-document2)) |
| Reports own experiments | Yes ([document_1.txt](https://arxiv.org/abs/1608.01972)) | No ([document_2.txt](#ref-document2)) |
| Cites a primary source | n/a (is the primary source) | Yes — cites document_1.txt ([document_2.txt](#ref-document2)) |
| Provides section/table anchoring | Yes ("Table 4," "TREC Experiments") ([document_1.txt](https://arxiv.org/abs/1608.01972)) | No ([document_2.txt](#ref-document2)) |
| **Overall weight** | **Higher** | **Lower** |

## 4. Reconstructing the Likely Correct Answer

Applying the weighting above, the most defensible reconstruction is the primary paper's: the embedding-based semantic similarity measure outperforms BM25 on both reported collections, by **19% on TREC 2006** and **6% on TREC 2007** in average precision ([document_1.txt](https://arxiv.org/abs/1608.01972)). This is coherent with the study's stated purpose of incorporating a semantic similarity measure to "bridge the gap" between queries and documents, with the SEM method also surpassing CENTROID, which itself trails BM25 ([document_1.txt](https://arxiv.org/abs/1608.01972)).

The third-party note's inverted claim ([document_2.txt](#ref-document2)) is best treated as an error, most plausibly a direction-of-comparison misreading, since it reproduces the same two numbers (19%, 6%) in the same year order while reversing the comparator. When a secondary source inverts a relation but preserves its magnitudes exactly, the parsimonious explanation is transcription or interpretation error rather than an unreported re-analysis.

## 5. The Answer in Explicit Numerical Form

| Benchmark collection | Magnitude | Direction per primary source | Direction per third-party note |
|---|---|---|---|
| TREC 2006 | 19% | Embedding **>** BM25 | BM25 **>** embedding |
| TREC 2007 | 6% | Embedding **>** BM25 | BM25 **>** embedding |

Source: ([document_1.txt](https://arxiv.org/abs/1608.01972); [document_2.txt](#ref-document2)).

Under the primary-source reading, and assuming the reported figures are relative improvements in average precision over the BM25 baseline, the relationship can be expressed as approximately:

- TREC 2006: AP(SEM) ≈ 1.19 × AP(BM25)
- TREC 2007: AP(SEM) ≈ 1.06 × AP(BM25)

These are proportions, not absolute percentage-point gains; the excerpts do not disclose the underlying average precision values, so the improvement cannot be converted into absolute points from the information supplied ([document_1.txt](https://arxiv.org/abs/1608.01972)).

## 6. What the Two Sources Agree On

Despite the contradiction on the headline question, the sources converge on several points that can be stated with high confidence:

1. **BM25 is a stronger lexical baseline than TF-IDF and than CENTROID** on the reported TREC collections ([document_1.txt](https://arxiv.org/abs/1608.01972); [document_2.txt](#ref-document2)).
2. **CENTROID is the weakest of the non-trivial methods**, scoring below BM25 and below the SEM/embedding approach in both accounts ([document_1.txt](https://arxiv.org/abs/1608.01972); [document_2.txt](#ref-document2)).
3. **The embedding approach and BM25 are the two strongest systems tested**, separated by margins of 19% and 6% on the two collections respectively ([document_1.txt](https://arxiv.org/abs/1608.01972); [document_2.txt](#ref-document2)).
4. **The effect is larger on TREC 2006 than on TREC 2007** — a nearly threefold difference in the reported gap — regardless of which system is on top ([document_1.txt](https://arxiv.org/abs/1608.01972); [document_2.txt](#ref-document2)).

Point 4 is analytically important. Whichever direction is correct, the comparison between a lexical baseline and a dense semantic method is strongly collection-dependent: the advantage shrinks from 19% to 6% between the two years. That is a substantive finding about the stability of embedding-based retrieval relative to BM25, not merely a reporting detail.

## 7. Limitations and Caveats

Several constraints should temper any claim made from this evidence base. First, the evidence covers only **two benchmark collections** (TREC 2006 and TREC 2007) drawn from a single domain — PubMed query-to-document mapping ([document_1.txt](https://arxiv.org/abs/1608.01972)). Second, the reported metric is **average precision** only; no statistics such as significance tests, confidence intervals, or per-query variance are provided in either excerpt ([document_1.txt](https://arxiv.org/abs/1608.01972); [document_2.txt](#ref-document2)). Third, the excerpts do not specify whether the percentages are **relative to the BM25 baseline** or absolute percentage points, a distinction that materially changes the size of the claim. Fourth, both documents are dated only by their content and identifiers, and one of them is a derivative note without independent verification ([document_2.txt](#ref-document2)). Fifth, and most importantly for this query, the **directional contradiction is unresolved by the provided material**; resolving it definitively would require access to Table 4 of the primary paper itself ([document_1.txt](https://arxiv.org/abs/1608.01972)).

## 8. Conclusion: Direct Answer to the Query

The question asks by how much the embedding approach outperforms BM25. On the balance of the supplied evidence, the answer is: **by 19% on TREC 2006 and 6% on TREC 2007, as measured by average precision**, according to the primary source ([document_1.txt](https://arxiv.org/abs/1608.01972)). This figure should be reported with the explicit caveat that a third-party research note claims the exact inverse — that BM25 outperforms the embedding approach by the same 19% and 6% margins ([document_2.txt](#ref-document2)).

Because the note is derivative, citing the primary paper as its own source, and because it reproduces the primary paper's magnitudes exactly while inverting only the comparator, the primary paper's version of the result is the more reliable one and should be treated as the operative answer ([document_1.txt](https://arxiv.org/abs/1608.01972); [document_2.txt](#ref-document2)). The defensible conclusion, therefore, is that the semantic embedding approach **outperformed BM25 by 19% on TREC 2006 and 6% on TREC 2007**, with the direction of that comparison contested only by an unreliable secondary account.

## References

<a id="ref-document1"></a>Bridging the Gap: Incorporating a Semantic Similarity Measure for Effectively Mapping PubMed Queries to Documents (arXiv:1608.01972). (document_1.txt). [https://arxiv.org/abs/1608.01972](https://arxiv.org/abs/1608.01972)

<a id="ref-document2"></a>Third-party research note: PubMed query-document mapping. (document_2.txt). (n.d.).