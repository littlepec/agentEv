# truth_extraction.md — PTB perplexity ground truth for the 11-paper multi-doc pool

Scope: read-only extraction from the 11 plain-text snapshots in
`F:/defense/evidence_pack_prep_v1/paper_round/multi_doc/pool/` (manifest:
`pool/pool_manifest.json`, fetched 2026-09-15T19:27:53). No model calls, no web access,
no other files touched. Every number below comes from the paper's own text only.

**Status: NOT human-reviewed.** This is an automated extraction by a single agent.

## Extraction conventions and artifacts

- The snapshots are ar5iv HTML → text. LaTeXML math is rendered twice, so table cells
  often appear as `57.3 57.3` or `82.2 82.2` for a single value `57.3` / `82.2`. This is a
  rendering duplication, **not** two different numbers. Quotes below preserve the raw text.
- Tables are flattened one cell per line. Quotes marked "flattened row" join the
  consecutive cell lines of one table row with ` | ` and give the source line numbers.
- **No split/corrupted decimals were found.** Scans for `^\s*\.[0-9]` (a decimal fragment
  starting a line) and for spaced decimals (`1 . 31`) returned zero hits across all 11 files.
  Bold-math wrappers (`\mathbf{371}`, `{\bf 1}.{\bf 31}`) appear only in non-PTB tables
  (Kim's other-languages tables, Zilly's BPC tables). All PTB numbers extracted cleanly.
- "Item 1" = best word-level **test** perplexity on PTB for the paper's **own proposed
  model**, as a **single model**, **without dynamic evaluation** and **without
  cache/pointer augmentation**. Fine-tuning is treated as an improved variant (item 2)
  when the paper reports both with and without it.

---

# 1. 1409.2329 — Zaremba et al., *Recurrent Neural Network Regularization*

**Item 1 — best single-model PTB test PPL (no dyn-eval, no cache): `78.4`**
(Large regularized LSTM, 1500 units/layer, 2 layers.)

- Location: Table 1, "Word-level perplexity on the Penn Tree Bank dataset", section 4.1
  Language modeling, under the sub-heading "A single model".
- Flattened row (lines 218–220): `Large regularized LSTM | 82.2 | 78.4`
- Supporting quote (lines 287–288, ≤40 words): "The large LSTM has 1500 1500 units per
  layer and its parameters are initialized uniformly in [ − 0.04 , 0.04 ]"

**Item 5 — validation perplexity: `82.2`** (same Table 1 row, "Validation set" column).

**Item 2 — improved variants reported by this paper** (all Table 1, sub-heading
"Model averaging"; these are *ensembles*, no cache/dynamic eval anywhere in the paper):

| Variant | Val | Test | Line |
|---|---|---|---|
| Medium regularized LSTM (single, 650 units) | 86.2 | 82.7 | 214–216 |
| 2 medium regularized LSTMs | 80.6 | 77.0 | 244–246 |
| 5 medium regularized LSTMs | 76.7 | 73.3 | 248–250 |
| 10 medium regularized LSTMs | 75.2 | 72.0 | 252–254 |
| 2 large regularized LSTMs | 76.9 | 73.6 | 256–258 |
| 10 large regularized LSTMs | 72.8 | 69.5 | 260–262 |
| 38 large regularized LSTMs | 71.9 | 68.7 | 264–266 |

- Flattened row (264–266): `38 large regularized LSTMs | 71.9 | 68.7`
- Non-regularized baseline (210–212): `non-regularized LSTM | 120.7 | 114.5`

**Item 4 — other pool papers' numbers quoted here: NONE.** This is the earliest paper in
the pool (2014); the other 10 are all later. Table 1 quotes only non-pool baselines
(Pascanu et al. 107.5, Cheng et al. 100.0, Mikolov 2012 83.5, Mikolov & Zweig 72.9).

**Item 6 — ambiguity:** two single models are reported (medium 82.7, large 78.4). The
large model (78.4) is the paper's headline single-model result and the one every later
pool paper quotes. No dynamic evaluation or cache is used anywhere in this paper.

---

# 2. 1508.06615 — Kim et al., *Character-Aware Neural Language Models* (char-CNN)

**Item 1 — best single-model PTB test PPL: `78.9`** (LSTM-Char-Large, 19m parameters).

- Location: Table 3, "Performance of our model versus other neural language models on the
  English Penn Treebank test set."
- Flattened row (lines 391–393): `LSTM-Char-Large | 78.9 78.9 | 19 19 m`
- Confirmed again in Table 7 ("Perplexity on the Penn Treebank for small/large models
  trained with/without highway layers"), flattened row (782–784):
  `Two Highway Layers | 90.1 90.1 | 78.9 78.9`
- Supporting quote (lines 441–442, ≤40 words): "As can be seen from Table 3 , our large
  model is on par with the existing state-of-the-art (Zaremba et al. 2014), despite having
  approximately 60 % 60\% fewer parameters."

**Item 5 — validation perplexity: NOT REPORTED.** Table 3 has only `PPL` and `Size`
columns; the caption says "on the English Penn Treebank **test** set". No PTB validation
perplexity appears anywhere in this snapshot.

**Item 2 — other variants reported by this paper** (no ensemble, no cache, no dynamic eval):

| Variant | PTB test PPL | Location / line |
|---|---|---|
| LSTM-Char-Small | 92.3 | Table 3, 383–385 |
| LSTM-Word-Small (baseline) | 97.6 | Table 3, 379–381 |
| LSTM-Word-Large (baseline) | 85.4 | Table 3, 387–389 |
| Char-Large, No Highway Layers | 84.6 | Table 7, 774–776 |
| Char-Large, One Highway Layer | 79.7 | Table 7, 778–780 |
| Char-Large, Two Highway Layers | **78.9** | Table 7, 782–784 |
| Char-Large, One MLP Layer | 92.6 | Table 7, 786–788 |
| Char-Small, Two Highway Layers | 90.1 | Table 7, 782–784 |
| word embeddings concatenated with CharCNN output, large | ~81 | "Further Observations", 838 |

- Quote for the 81 (line 838, ≤40 words): "Combining word embeddings with the CharCNN's
  output to form a combined representation of a word (to be used as input to the LSTM)
  resulted in slightly worse performance ( 81 81 on PTB with a large model)."
- Explicit refusal to report ensembles (lines 445–446): "While lower perplexities have been
  reported with model ensembles [ 2012 ] , we do not include them here as they are not
  comparable to the current work."

**Item 4 — other pool papers' numbers quoted here: Zaremba (1409.2329) only.**

- Flattened row (423–425): `LSTM-1 † (Zaremba et al. 2014) | 82.7 82.7 | 20 20 m`
- Flattened row (427–429): `LSTM-2 † (Zaremba et al. 2014) | 78.4 78.4 | 52 52 m`

**Item 6 — ambiguities:**
1. Kim reports Zaremba's large LSTM as **52m** parameters; Zaremba's own paper gives no
   parameter count, but every other pool paper (Merity, Gal, Zilly, Inan, Zoph, Yang) lists
   it as **66M**. Kim's `†` footnote says sizes are "estimates based on our understanding of
   their papers or private correspondence".
2. Table 3 lists LSTM-Char-Small as 92.3 (= one highway layer per Table 2), but Table 7
   shows a *better* small model at 90.1 with two highway layers. The headline small number
   is the worse one. This does not affect item 1 (large = 78.9 in both tables).

---

# 3. 1512.05287 — Gal & Ghahramani, *A Theoretically Grounded Application of Dropout in RNNs*

**Item 1 — best single-model PTB test PPL: `73.4 ± 0.0`**
(Variational LSTM, large, untied weights, **MC dropout** at test time.)

- Location: Table 1, "Single model perplexity (on test and validation sets) for the Penn
  Treebank language modelling task", section 5.1.
- Flattened row (lines 339–344): `Variational (untied weights, MC) | − - | 78.6 ± 0.1 |
  − - | − - | 73.4 ± 0.0 | − -` (columns: Medium Val, Medium Test, Medium WPS, Large Val,
  Large Test, Large WPS)
- Supporting quote (lines 283, ≤40 words): "Test perplexity is reduced from 78.4 78.4 down
  to 73.4 73.4 (with MC dropout and untied weights). To the best of our knowledge, these
  are currently the best single model perplexities on the Penn Treebank."
- Abstract (line 12): "improves on the single model state-of-the-art in language modelling
  with the Penn Treebank (73.4 test perplexity)."

**Item 5 — validation perplexity:** for the MC-dropout rows the validation column is `−`
(not reported). The corresponding non-MC large models give val `77.9 ± 0.3` (untied) and
`77.3 ± 0.2` (tied).

**Item 2 — improved / alternative variants in this paper:**

| Variant | Large Val | Large Test | Medium Val | Medium Test | Line |
|---|---|---|---|---|---|
| Variational (tied weights) | 77.3 ± 0.2 | 75.0 ± 0.1 | 81.8 ± 0.2 | 79.7 ± 0.1 | 318–324 |
| Variational (tied weights, MC) | − | 74.1 ± 0.0 | − | 79.0 ± 0.1 | 325–331 |
| Variational (untied weights) | 77.9 ± 0.3 | 75.2 ± 0.2 | 81.9 ± 0.2 | 79.7 ± 0.1 | 332–338 |
| Variational (untied weights, MC) | − | **73.4 ± 0.0** | − | 78.6 ± 0.1 | 339–344 |
| **10-model ensemble** (Variational LSTMs, MC) | — | **68.7** | — | — | 355 |

- Ensemble quote (line 355, ≤40 words): "Using 10 Variational LSTMs we improve [ 4 ] 's
  test set perplexity from 69.5 69.5 to 68.7 68.7 – obtaining identical perplexity to
  [ 4 ] 's experiment with 38 models."
- No neural cache / pointer / dynamic evaluation is used anywhere in this paper.

**Item 4 — other pool papers' numbers quoted here: Zaremba (1409.2329) only.**

- Flattened row (311–317): `Zaremba et al. 2014 | 86.2 86.2 | 82.7 82.7 | 5.5 5.5 K |
  82.2 82.2 | 78.4 78.4 | 2.5 2.5 K`
- Quote (line 283): "Validation perplexity for the large model is improved from [ 4 ] 's
  82.2 82.2 down to 77.3 77.3 (with weight tying), or 77.9 77.9 without weight tying."
- Quote (line 355): "improve [ 4 ] 's test set perplexity from 69.5 69.5 to 68.7 68.7 …
  identical perplexity to [ 4 ] 's experiment with 38 models." (Zaremba's 10-large-ensemble
  69.5 and 38-ensemble 68.7.)

**Item 6 — ambiguity (important):** whether `73.4` counts as the paper's "single model
without dynamic evaluation / cache" number depends on how MC dropout is classified. MC
dropout is **test-time averaging over 1000 stochastic forward passes** of one trained
model (line 278: "using MC dropout (obtained by performing dropout at test time 1000
times, and averaging the model outputs)"). The paper itself calls it a *single model* and
the abstract claims 73.4. Every later pool paper that quotes Gal quotes either 73.4 or
78.6, i.e. accepts the MC number. If MC is excluded, the correct item-1 value is
`75.2 ± 0.2` (large, untied, dropout approximation) or `75.0 ± 0.1` (large, tied).
The ranking tables below use **73.4** (the paper's own claim) and flag the alternative.

---

# 4. 1607.03474 — Zilly et al., *Recurrent Highway Networks* (RHN)

**Item 1 — best single-model PTB test PPL: `65.4`** (Variational RHN + WT, 23 M, depth 10).

- Location: Table 1, "Validation and test set perplexity of recent state of the art
  word-level language models on the Penn Treebank dataset", section 5.2.
- Flattened row (lines 316–319): `Variational RHN + WT | 23 M | 67.9 | 65.4`
- Supporting quote (line 338, ≤40 words): "For the best 10 layer model, reducing the weight
  decay further improves the results to 67.9/65.4 validation/test perplexity."
- Abstract (line 15): "On the Penn Treebank corpus, solely increasing the transition depth
  from 1 to 10 improves word-level perplexity from 90.6 to 65.4 using the same number of
  parameters."

**Item 5 — validation perplexity: `67.9`.**

**Item 2 — other variants reported by this paper:**

| Variant | Size | Val | Test | Line |
|---|---|---|---|---|
| Variational RHN (no weight tying) | 32 M | 71.2 | 68.5 | 306–309 |
| Variational RHN + WT | 23 M | 67.9 | **65.4** | 316–319 |
| depth-1 RHN (abstract only, no table) | 32 M | — | 90.6 | 15 |

- No ensemble, no cache/pointer, no dynamic evaluation for PTB in this paper. (The
  character-level tables 2 and 3 are explicitly "results under 1.5 BPC & **without dynamic
  evaluation**", lines 359 and 392.)

**Item 4 — other pool papers' numbers quoted here (Table 1, lines 269–329):**

| Source paper | Quoted flattened row | Line |
|---|---|---|
| Kim (1508.06615) | `Conv.+Highway+LSTM+dropout ( Kim et al. 2015 ) | 19 M | – | 78.9` | 276–279 |
| Zaremba (1409.2329) | `LSTM+dropout ( Zaremba et al. 2014 ) | 66 M | 82.2 | 78.4` | 281–284 |
| Gal (1512.05287) | `Variational LSTM ( Gal 2015 ) | 66 M | 77.3 | 75.0` | 286–289 |
| Press & Wolf (1608.05859) | `Variational LSTM + WT ( Press & Wolf 2016 ) | 51 M | 75.8 | 73.2` | 291–294 |
| Inan (1611.01462) | `Variational LSTM + WT + augmented loss ( Inan et al. 2016 ) | 51 M | 71.1 | 68.5` | 301–304 |
| Zoph (1611.01578) | `Neural Architecture Search with base 8 ( Zoph & Le 2016 ) | 32 M | – | 67.9` | 311–314 |
| Zoph (1611.01578) | `Neural Architecture Search with base 8 + WT ( Zoph & Le 2016 ) | 25 M | – | 64.0` | 321–324 |
| Zoph (1611.01578) | `Neural Architecture Search with base 8 + WT ( Zoph & Le 2016 ) | 54 M | – | 62.4` | 326–329 |

Note: Zilly quotes **Gal's tied-weights, non-MC number (75.0)**, not Gal's headline 73.4.

**Item 6 — ambiguities:**
1. Two candidate "the paper's result": 65.4 (with weight tying) and 68.5 (without).
   Weight tying is not this paper's contribution — the paper credits it to Inan & Khosravi
   2016 and Press & Wolf 2016 (line 253). Papers citing Zilly split: Press & Wolf and Inan
   quote **68.5** (VD-RHN alone), while Melis, Yang, Merity and Zoph quote **65.4**.
2. The abstract's `90.6` depth-1 baseline appears nowhere in a table (it is only in
   Figure 5(a), which is an image and not in the text extraction).

---

# 5. 1608.05859 — Press & Wolf, *Using the Output Embedding to Improve Language Models*

**Item 1 — best single-model PTB test PPL: `66.0`** (RHN + BD + WT, 24M) — *with the
caveat in item 6 below.* Best **pure-LSTM** variant of theirs: `73.2` (Large + BD + WT, 51M).

- Location: Table 5, "Word level perplexity (lower is better) on PTB and size (number of
  parameters) of models that use either dropout (baseline model) or Bayesian dropout (BD)."
- Flattened row (lines 224–227): `RHN + BD + WT | 24M | 74.1 | 68.1 | 66.0`
  (columns: Model | Size | Train | Val. | Test)
- Flattened row (lines 214–218): `Large + BD + WT | 51M | 28.2 | 75.8 | 73.2`
- Supporting quote (line 322, ≤40 words): "Finally, by replacing the LSTM with a recurrent
  highway network [ \citenameZilly et al.2016 ] , state of the art results are achieved when
  applying weight tying. The contribution of WT is also significant in this model."

**Item 5 — validation perplexity: `68.1`** (RHN + BD + WT); `75.8` for Large + BD + WT.

**Item 2 — other variants reported by this paper:**

| Variant | Size | Train | Val | Test | Line |
|---|---|---|---|---|---|
| Large + Weight Tying (no Bayesian dropout) | 51M | 48.5 | 77.7 | 74.3 | 204–208 |
| Large + BD + WT | 51M | 28.2 | 75.8 | 73.2 | 214–218 |
| RHN + BD + WT | 24M | 74.1 | 68.1 | **66.0** | 224–227 |
| Small model (no dropout, Zaremba small) | 4.65M | 38.0 | 120.7 | 114.5 | 259–263 |
| Small + WT | 2.65M | 36.4 | 117.5 | 112.4 | 264–268 |
| Small + PR | 4.69M | 50.8 | 116.0 | 111.7 | 269–273 |
| Small + WT + PR | 2.69M | 53.5 | 104.9 | 100.9 | 274–278 |

- No ensemble, no cache/pointer, no dynamic evaluation anywhere.
- Table 6 (no-dropout models) quote (line 324, ≤40 words): "In Tab. 6 , we report the
  results of the small NNLM model, that does not utilize dropout, on PTB. As can be seen,
  both WT and projection regularization (PR) improve the results."

**Item 4 — other pool papers' numbers quoted here:**

| Source paper | Quoted flattened row | Line |
|---|---|---|
| Zaremba (1409.2329), large | `Large [Zaremba et al.2014] | 66M | 37.8 | 82.2 | 78.4` | 199–203 |
| Gal (1512.05287) | `Large + BD [Gal2015] + WD | 66M | 24.3 | 78.1 | 75.2` | 209–213 |
| Zilly (1607.03474) | `RHN [Zilly et al.2016] + BD | 32M | 67.4 | 71.2 | 68.5` | 219–223 |
| Zaremba (1409.2329), small | `Small model | 4.65M | 38.0 | 120.7 | 114.5` | 259–263 |
| (non-pool) Deep RNN Pascanu | `Deep RNN | 6.16M | | 107.5` | 255–258 |

Note the **validation discrepancy**: Press & Wolf report Gal's large+BD model as val
`78.1` / test `75.2`; Gal's own Table 1 gives `77.9 ± 0.3` / `75.2 ± 0.2` (untied) or
`77.3 ± 0.2` / `75.0 ± 0.1` (tied). The test number matches the untied row; the validation
number `78.1` does not appear in Gal's paper at all.

**Item 6 — ambiguity (important):** the paper's best PTB number (66.0) is **their weight-tying
technique applied to someone else's architecture** (Zilly's RHN). It is genuinely "the
result this paper reports for its own proposed method", but it is not their own model
architecture. Downstream papers split on attribution:
- Zilly's own Table 1 attributes the 51M `75.8/73.2` row to **Press & Wolf**;
- Zoph's Table 2 attributes `73.2` (51M) to **Press & Wolf**;
- Melis attributes `75.8/73.2` (51M) to **Press & Wolf**;
- but Inan's Table 3 lists the identical `68.1/66.0` (24M) row as **"VD-RHN +RE (Zilly et
  al. 2016)"**, i.e. credits it to Zilly/Inan, not Press & Wolf.
So `66.0` and `73.2` are both "this paper's result" depending on which convention you use.
The ranking tables below use **66.0** and flag the conflict.

---

# 6. 1611.01462 — Inan, Khosravi & Socher, *Tying Word Vectors and Word Classifiers*

**Item 1 — best single-model PTB test PPL: `66.0`** (VD-RHN +RE, 24M) — *see item 6.*
Best **pure-LSTM** variant of theirs: `68.5` (VD-LSTM +REAL, large, 1500 units, 51M).

- Location: Table 3, "Comparison of our work to previous state of the art on word-level
  validation and test perplexities on the Penn Treebank corpus."
- Flattened row (lines 474–479): `VD-RHN +RE ( Zilly et al. 2016 ) [fn 6: "This model was
  developed following our work in Inan & Khosravi 2016."] | 24M | 68.1 | 66.0`
- Flattened row (lines 469–472): `VD-LSTM +REAL (large) | 51M | 71.1 | 68.5`
- Supporting quote (line 285, ≤40 words): "The recently proposed recurrent highway networks
  ( Zilly et al. 2016 ) when trained with reused embeddings (VD-RHN +RE) achieves the best
  overall performance, improving on VD-RHN by a perplexity of 2.5 2.5 ."

**Item 5 — validation perplexity: `68.1`** (VD-RHN +RE); `71.1` (VD-LSTM +REAL large).

**Item 2 — other variants reported by this paper (Table 1, PTB columns):**

| Network | Model | Val | Test | Line |
|---|---|---|---|---|
| Small (200) | VD-LSTM | 92.6 | 87.3 | 296–300 |
| Small (200) | VD-LSTM+AL | 86.3 | 82.9 | 302–306 |
| Small (200) | VD-LSTM+RE | 89.9 | 85.1 | 308–312 |
| Small (200) | VD-LSTM+REAL | 86.3 | 82.7 | 314–318 |
| Medium (650) | VD-LSTM | 82.0 | 77.7 | 323–327 |
| Medium (650) | VD-LSTM+AL | 77.4 | 74.7 | 329–333 |
| Medium (650) | VD-LSTM+RE | 77.1 | 73.9 | 335–339 |
| Medium (650) | VD-LSTM+REAL | 75.7 | 73.2 | 341–345 |
| Large (1500) | VD-LSTM | 76.8 | 72.6 | 351–355 |
| Large (1500) | VD-LSTM+AL | 74.5 | 71.2 | 357–361 |
| Large (1500) | VD-LSTM+RE | 72.5 | 69.0 | 363–367 |
| Large (1500) | VD-LSTM+REAL | 71.1 | **68.5** | 369–372 |

- No ensemble, no cache/pointer, no dynamic evaluation of their own.

**Item 4 — other pool papers' numbers quoted here (Table 3, lines 397–479):**

| Source paper | Quoted flattened row | Line |
|---|---|---|
| Zaremba (1409.2329) medium | `LSTM (medium) ( Zaremba et al. 2014 ) | 20M | 86.2 | 82.7` | 429–432 |
| Kim (1508.06615) | `CharCNN ( Kim et al. 2015 ) | 19M | - | 78.9` | 434–437 |
| Zaremba (1409.2329) large | `LSTM (large) ( Zaremba et al. 2014 ) | 66M | 82.2 | 78.4` | 439–442 |
| Gal (1512.05287) | `VD-LSTM (large, untied, MC) ( Gal 2015 ) | 66M | - | 73.4 ± 0.0` | 444–447 |
| Zaremba (1409.2329) ensemble | `38 Large LSTMs ( Zaremba et al. 2014 ) | 2.51B | 71.9 | 68.7` | 454–457 |
| Gal (1512.05287) ensemble | `10 Large VD-LSTMs ( Gal 2015 ) | 660M | - | 68.7` | 459–462 |
| Zilly (1607.03474) | `VD-RHN ( Zilly et al. 2016 ) | 32M | 71.2 | 68.5` | 464–467 |
| Zilly (1607.03474) + their RE | `VD-RHN +RE ( Zilly et al. 2016 ) | 24M | 68.1 | 66.0` | 474–479 |

**Item 6 — ambiguities:**
1. Same attribution conflict as Press & Wolf: the `68.1/66.0` row is labelled as Zilly's
   RHN with Inan's "RE" applied. Inan presents it in Table 3 as the best overall result and
   the text calls it theirs ("when trained with reused embeddings … achieves the best
   overall performance"), but the row name credits Zilly. The pure-Inan-architecture number
   is `68.5`.
2. `68.5` is numerically identical to Zilly's own no-weight-tying VD-RHN test perplexity,
   which Inan also lists in the same table (line 467). A reader scanning for "68.5" in
   Inan's Table 3 will find it twice with two different owners.
3. `73.2` (Inan medium VD-LSTM+REAL, Table 1 line 344) collides with Press & Wolf's own
   headline 73.2 (Large + BD + WT). See the ranking notes.

---

# 7. 1611.01578 — Zoph & Le, *Neural Architecture Search with Reinforcement Learning*

**Item 1 — best single-model PTB test PPL: `62.4`**
(Neural Architecture Search with base 8 and shared embeddings, 54M.)

- Location: Table 2, "Single model perplexity on the test set of the Penn Treebank language
  modeling task", section 4.2.
- Flattened row (lines 374–376): `Neural Architecture Search with base 8 and shared
  embeddings | 54M | 62.4 62.4`
- Supporting quote (line 15, abstract, ≤40 words): "Our cell achieves a test set perplexity
  of 62.4 on the Penn Treebank, which is 3.6 perplexity better than the previous
  state-of-the-art model."

**Item 5 — validation perplexity: NOT REPORTED.** Table 2 has only `Parameters` and
`Test Perplexity` columns. Validation perplexity is used as the RL reward (line 279:
"The reward function is c (validation perplexity) 2") but no value is given.

**Item 2 — other variants reported by this paper:**

| Variant | Params | Test PPL | Line |
|---|---|---|---|
| NAS with base 8 (no shared embeddings) | 32M | 67.9 | 366–368 |
| NAS with base 8 and shared embeddings | 25M | 64.0 | 370–372 |
| NAS with base 8 and shared embeddings | 54M | **62.4** | 374–376 |

- No ensemble, no cache/pointer, no dynamic evaluation. (Character-level PTB results in
  Table 3 are BPC/perplexity 1.214 — a different task, not word-level PTB.)

**Item 4 — other pool papers' numbers quoted here (Table 2, lines 286–376):**

| Source paper | Quoted flattened row | Line |
|---|---|---|
| Zaremba (1409.2329) medium | `Zaremba et al. 2014 - LSTM (medium) | 20M | 82.7 82.7` | 318–320 |
| Zaremba (1409.2329) large | `Zaremba et al. 2014 - LSTM (large) | 66M | 78.4 78.4` | 322–324 |
| Gal (1512.05287) | `Gal 2015 - Variational LSTM (medium, untied) | 20M | 79.7 79.7` | 326–328 |
| Gal (1512.05287) | `Gal 2015 - Variational LSTM (medium, untied, MC) | 20M | 78.6 78.6` | 330–332 |
| Gal (1512.05287) | `Gal 2015 - Variational LSTM (large, untied) | 66M | 75.2 75.2` | 334–336 |
| Gal (1512.05287) | `Gal 2015 - Variational LSTM (large, untied, MC) | 66M | 73.4 73.4` | 338–340 |
| Kim (1508.06615) | `Kim et al. 2015 - CharCNN | 19M | 78.9 78.9` | 342–344 |
| Press & Wolf (1608.05859) | `Press & Wolf 2016 - Variational LSTM, shared embeddings | 51M | 73.2 73.2` | 346–348 |
| Inan (1611.01462) | `Inan et al. 2016 - VD-LSTM + REAL (large) | 51M | 68.5 68.5` | 358–360 |
| Zilly (1607.03474) | `Zilly et al. 2016 - Variational RHN, shared embeddings | 24M | 66.0 66.0` | 362–364 |

This is the most complete quotation of Gal in the pool — all four of Gal's Table 1 test
numbers (79.7, 78.6, 75.2, 73.4) appear here.

**Item 6 — ambiguity:** three of the paper's own models are reported at three sizes
(67.9 / 64.0 / 62.4). The abstract and introduction both commit to `62.4` as *the* result.
Note that Zoph's 62.4 at 54M and 64.0 at 25M give different answers to "what is NAS's PTB
perplexity" depending on parameter budget; Zilly and Melis quote both, Yang quotes only 64.0.

---

# 8. 1706.02222 — Tjandra et al., *Gated Recurrent Neural Tensor Network* (GRURNTN)

**Item 1 — best single-model PTB test PPL: `87.38`** (GRURNTN, 256 hidden units, ~12M params).

- Location: TABLE II, "PennTreeBank test set PPL", section V-B Word-level Language Modeling.
- Flattened row (lines 415–416): `GRURNTN (proposed) | 87.38`
- Supporting quote (line 421, ≤40 words): "GRURNTN reduced the perplexity from 97.78 to
  87.38 (10.4 absolute / 10.63% relative PPL) over the baseline GRURNN and LSTMRNTN reduced
  the perplexity from 108.26 to 96.97"
- Explicit no-dynamic-eval statement (footnote 4, lines 370–372, ≤40 words): "Dynamic
  evaluation approach updates the model parameter during processing on the test data (only
  updated once per test dataset). Our baseline and proposed model experiment did not use
  dynamic evaluation."

**Item 5 — validation perplexity: NOT REPORTED numerically.** Validation PPL per epoch is
only in Fig. 9 (an image): "Fig. 9: Comparison among GRURNN, GRURNTN, LSTMRNN and LSTMRNTN
perplexity (PPL) per epoch on the PTB validation set" (line 395).

**Item 2 — other variants reported by this paper (TABLE II, lines 398–418):**

| Model | Test PPL | Line |
|---|---|---|
| GRURNN (their baseline) | 97.78 | 411–412 |
| LSTMRNN (their baseline) | 108.26 | 413–414 |
| GRURNTN (proposed) | **87.38** | 415–416 |
| LSTMRNTN (proposed) | 96.97 | 417–418 |

- No ensemble, no cache/pointer, no dynamic evaluation, no fine-tuning stage.

**Item 4 — other pool papers' numbers quoted here: NONE.**
TABLE II quotes only non-pool baselines: N-Gram 141, RNNLM w/o dyn. eval 124.7, RNNLM w/
dyn. eval 123.2, SCRNN 115, sRNN 110.0, DOT(S)-RNN 107.5. A `grep` for the own-result
numbers of all ten other pool papers returns zero hits in this file. **This paper is
completely disconnected from the rest of the pool's citation graph** — it neither cites nor
compares against Zaremba, Gal, Kim, Zilly, Press & Wolf, Inan, Zoph, Melis, Merity or Yang,
despite being from 2017 and reporting a PTB number ~30 perplexity worse than the 2017 state
of the art. This is the single most important redundancy gap in the pool.

**Item 6 — ambiguities:**
1. The text says "Table I shows the PTB test set PPL" (line 420) but the word-level
   perplexities are in **TABLE II**; TABLE I is the character-level BPC table. A
   cross-reference error in the paper itself.
2. Character-level results (TABLE I, GRURNTN 1.33 BPC) are BPC, not PTB word perplexity,
   and must not be conflated.

---

# 9. 1707.05589 — Melis, Dyer & Blunsom, *On the State of the Art of Evaluation in Neural Language Models*

**Item 1 — best single-model PTB test PPL: `58.3`** (LSTM, 24M parameters, depth 4) —
*but see item 6, the paper contains a better number of its own, `58.0`.*

- Location: Table 1, "Validation and test set perplexities on Penn Treebank for models with
  different numbers of parameters and depths."
- Flattened row (lines 282–285): `LSTM | [24M] | 4 | 60.9 60.9 | 58.3 58.3`
- Supporting quote (line 360, ≤40 words): "At 24M, all depths obtain very similar results,
  reaching 58.3 58.3 at depth 4."

**Item 5 — validation perplexity: `60.9`.**

**Item 2 — other variants reported by this paper:**

Table 1 (their own models, PTB):

| Model | Size | Depth | Val | Test | Line |
|---|---|---|---|---|---|
| LSTM | 10M | 1 | 61.8 | 59.6 | 245–249 |
| LSTM | 10M | 2 | 63.0 | 60.8 | 251–254 |
| LSTM | 10M | 4 | 62.4 | 60.1 | 256–259 |
| RHN | 10M | 5 | 66.0 | 63.5 | 261–264 |
| NAS | 10M | 1 | 65.6 | 62.7 | 266–269 |
| LSTM | 24M | 1 | 61.4 | 59.5 | 271–275 |
| LSTM | 24M | 2 | 62.1 | 59.6 | 277–280 |
| LSTM | 24M | 4 | 60.9 | **58.3** | 282–285 |
| RHN | 24M | 5 | 64.8 | 62.2 | 287–290 |
| NAS | 24M | 1 | 62.1 | 59.7 | 292–294 |

Table 4 (feature ablations, PTB) — includes a **better** number than Table 1:

| Variant | 10M depth/Val/Test | 24M depth/Val/Test | Line |
|---|---|---|---|
| LSTM (baseline) | 1 / 61.8 / 59.6 | 4 / 60.9 / 58.3 | 677–683 |
| − Shared Embeddings | 1 / 67.6 / 65.2 | 4 / 65.6 / 63.2 | 685–691 |
| − Variational Dropout | 1 / 62.9 / 61.2 | 4 / 66.3 / 64.5 | 693–699 |
| + Recurrent Dropout | 1 / 62.8 / 60.6 | 4 / 65.2 / 62.9 | 701–707 |
| + Untied gates | 1 / 61.4 / 58.9 | 4 / 64.0 / 61.3 | 709–715 |
| **+ Tied gates** | 1 / 61.7 / 59.6 | **4 / 60.4 / 58.0** | 717–723 |
| RHN | 5 / 66.0 / 63.5 | 5 / 64.8 / 62.2 | 725–731 |
| RHN − Shared Embeddings | 5 / 72.3 / 69.5 | 5 / 67.4 / 64.6 | 733–739 |
| RHN − Variational Dropout | 5 / 74.4 / 71.7 | 5 / 74.7 / 71.7 | 741–747 |
| RHN + Recurrent Dropout | 5 / 65.5 / 63.0 | 5 / 63.4 / 61.0 | 749–755 |

- No ensemble, no cache, no dynamic evaluation — explicitly refused (line 97, ≤40 words):
  "we thus refrain from including techniques that are known to push perplexities even
  lower … Merity et al. 2017 demonstrate the utility of adding a Neural Cache".
- MC dropout also explicitly declined (line 308): "Preliminary experiments indicate that MC
  averaging would bring a small improvement of about 0.4 in perplexity … while being a 1000
  times more expensive".

**Item 4 — other pool papers' numbers quoted here (Table 1, lines 185–299):**

| Source paper | Quoted flattened row | Line |
|---|---|---|
| Zaremba (1409.2329) medium | `Medium LSTM, Zaremba et al. 2014 | 10M | 2 | 86.2 | 82.7` | 191–195 |
| Zaremba (1409.2329) large | `Large LSTM, Zaremba et al. 2014 | 24M | 2 | 82.2 | 78.4` | 197–201 |
| Press & Wolf (1608.05859) | `VD LSTM, Press & Wolf 2016 | 51M | 2 | 75.8 | 73.2` | 203–207 |
| Inan (1611.01462) medium | `VD LSTM, Inan et al. 2016 | 9M | 2 | 77.1 | 73.9` | 209–213 |
| Inan (1611.01462) large | `VD LSTM, Inan et al. 2016 | 28M | 2 | 72.5 | 69.0` | 215–219 |
| Zilly (1607.03474) | `VD RHN, Zilly et al. 2016 | 24M | 10 | 67.9 | 65.4` | 221–225 |
| Zoph (1611.01578) | `NAS, Zoph & Le 2016 | 25M | - | - | 64.0` | 227–231 |
| Zoph (1611.01578) | `NAS, Zoph & Le 2016 | 54M | - | - | 62.4` | 233–237 |
| Merity (1708.02182) | `AWD-LSTM, Merity et al. 2017 † | 24M | 3 | 60.0 | 57.3` | 239–243 |

Caption note (line 299): "†: parallel work."
Gal (1512.05287) is **cited** (variational dropout, lines 135, 310) but **none of Gal's PTB
perplexity numbers are quoted**. Kim (1508.06615) and Tjandra (1706.02222) are not cited at all.

**Item 6 — ambiguities (important):**
1. **The paper's own best PTB test perplexity is `58.0`, not `58.3`.** Table 4's
   "+ Tied gates" at 24M / depth 4 gives 60.4 / 58.0, better than the Table 1 headline
   58.3. Section 7.4 confirms these are their own LSTM variants: "All LSTM models in this
   paper use the third variant, except those titled 'Untied gates' and 'Tied gates' in
   Table 4" (lines 807–810). Every downstream paper (Yang, Merity) quotes **58.3**.
2. Melis assigns Zaremba's medium/large models sizes **10M / 24M**; Zaremba's own paper
   gives no counts, and Gal, Merity, Zilly, Inan, Zoph and Yang all list them as
   **20M / 66M**. Melis's numbers are that of their own matched parameter budget, but the
   row reads as if it were Zaremba's parameter count.
3. Melis lists Inan's medium/large VD-LSTM at **9M / 28M**; Inan's own paper gives no PTB
   parameter counts in Table 1 and lists 51M for the large VD-LSTM+REAL in Table 3.
4. The 73.9 and 69.0 values Melis attributes to "VD LSTM, Inan et al. 2016" are Inan's
   **+RE** rows (medium VD-LSTM+RE 77.1/73.9, large VD-LSTM+RE 72.5/69.0), not the plain
   VD-LSTM rows (82.0/77.7 and 76.8/72.6). The label "VD LSTM" understates what was run.

---

# 10. 1708.02182 — Merity, Keskar & Socher, *Regularizing and Optimizing LSTM Language Models* (AWD-LSTM)

**Item 1 — best single-model PTB test PPL: `57.3`**
(AWD-LSTM, 3-layer LSTM, tied, 24M, with fine-tuning, no cache.)

- Location: Table 1, "Single model perplexity on validation and test sets for the Penn
  Treebank language modeling task."
- Flattened row (lines 343–346): `AWD-LSTM - 3-layer LSTM (tied) | 24M | 60.0 60.0 | 57.3 57.3`
- Supporting quote (line 16, abstract, ≤40 words): "Using these and other regularization
  strategies, we achieve state-of-the-art word level perplexities on two data sets: 57.3 on
  Penn Treebank and 65.8 on WikiText-2."

**Item 5 — validation perplexity: `60.0`.**

**Item 2 — improved / ablated variants reported by this paper:**

| Variant | Params | Val | Test | Location / line |
|---|---|---|---|---|
| **AWD-LSTM + continuous cache pointer** | 24M | 53.9 | **52.8** | Table 1, 348–351 |
| AWD-LSTM − fine-tuning | 24M | 60.7 | 58.8 | Table 4, 558–562 |
| AWD-LSTM − NT-ASGD | — | 66.3 | 63.7 | Table 4, 563–567 |
| AWD-LSTM − variable sequence lengths | — | 61.3 | 58.9 | Table 4, 568–572 |
| AWD-LSTM − embedding dropout | — | 65.1 | 62.7 | Table 4, 573–577 |
| AWD-LSTM − weight decay | — | 63.7 | 61.0 | Table 4, 578–582 |
| AWD-LSTM − AR/TAR | — | 62.7 | 60.3 | Table 4, 583–587 |
| AWD-LSTM − full sized embedding | — | 68.0 | 65.6 | Table 4, 588–592 |
| AWD-LSTM − weight-dropping | — | 71.1 | 68.9 | Table 4, 593–597 |

- Cache quote (line 17, abstract, ≤40 words): "In exploring the effectiveness of a neural
  cache in conjunction with our proposed model, we achieve an even lower state-of-the-art
  perplexity of 52.8 on Penn Treebank and 52.0 on WikiText-2."
- Cache hyperparameters (line 426): "The tuned values for these hyperparameters were
  ( 2000 , 0.1 , 1.0 ) for PTB". No dynamic evaluation is used in this paper.
- Fine-tuning is part of the headline 57.3 (line 226): "we run ASGD with T = 0 … as a
  fine-tuning step to further improve the solution."

**Item 4 — other pool papers' numbers quoted here (Table 1, lines 236–351):**

| Source paper | Quoted flattened row | Line |
|---|---|---|
| Zaremba (1409.2329) medium | `Zaremba et al. 2014 - LSTM (medium) | 20M | 86.2 | 82.7` | 263–266 |
| Zaremba (1409.2329) large | `Zaremba et al. 2014 - LSTM (large) | 66M | 82.2 | 78.4` | 268–271 |
| Gal (1512.05287) | `Gal & Ghahramani 2016 - Variational LSTM (medium) | 20M | 81.9 ± 0.2 | 79.7 ± 0.1` | 273–276 |
| Gal (1512.05287) | `... (medium, MC) | 20M | − | 78.6 ± 0.1` | 278–281 |
| Gal (1512.05287) | `... (large) | 66M | 77.9 ± 0.3 | 75.2 ± 0.2` | 283–286 |
| Gal (1512.05287) | `... (large, MC) | 66M | − | 73.4 ± 0.0` | 288–291 |
| Kim (1508.06615) | `Kim et al. 2016 - CharCNN | 19M | − | 78.9` | 293–296 |
| Inan (1611.01462) medium | `Inan et al. 2016 - Variational LSTM (tied) + augmented loss | 24M | 75.7 | 73.2` | 313–316 |
| Inan (1611.01462) large | `... | 51M | 71.1 | 68.5` | 318–321 |
| Zilly (1607.03474) | `Zilly et al. 2016 - Variational RHN (tied) | 23M | 67.9 | 65.4` | 323–326 |
| Zoph (1611.01578) | `Zoph & Le 2016 - NAS Cell (tied) | 25M | − | 64.0` | 328–331 |
| Zoph (1611.01578) | `Zoph & Le 2016 - NAS Cell (tied) | 54M | − | 62.4` | 333–336 |
| Melis (1707.05589) | `Melis et al. 2017 - 4-layer skip connection LSTM (tied) | 24M | 60.9 | 58.3` | 338–341 |

Merity is the **most complete quoter of Gal** apart from Zoph (all four Gal rows, with
error bars). Press & Wolf (1608.05859) is cited for weight tying (line 186) but **none of
its perplexity numbers are quoted**. Tjandra (1706.02222) is not cited.

**Item 6 — ambiguity:**
1. `57.3` includes a **fine-tuning** stage; the no-fine-tune value is `58.8` (Table 4). Yang
   (1711.03953) quotes both as separate rows; Melis quotes only 57.3. If "fine-tuning"
   counts as an improved variant under the item-1 exclusion rule, the strict answer would be
   58.8. The paper presents 57.3 as *the* model, so 57.3 is used in the rankings.
2. `78.4` appears twice in this file: once as Zaremba's PTB test (line 271) and once as the
   AWD-LSTM "− weight-dropping" **WikiText-2 validation** value (line 596). Any string-level
   search for "78.4" in this paper will hit a WT2 number.

---

# 11. 1711.03953 — Yang, Dai, Salakhutdinov & Cohen, *Breaking the Softmax Bottleneck* (MoS)

**Item 1 — best single-model PTB test PPL: `54.44`**
(AWD-LSTM-MoS, 22M, with fine-tuning, no dynamic evaluation, no cache.)

- Location: Table 1, "Single model perplexity on validation and test sets on Penn Treebank."
- Flattened row (lines 272–275): `Ours – AWD-LSTM-MoS | 22M | 56.54 | 54.44`
- Supporting quote (line 347, ≤40 words): "With a comparable number of parameters, MoS
  outperforms all baselines with or without dynamic evaluation, and substantially improves
  over the current state of the art, by up to 3.6 points in perplexity."

**Item 5 — validation perplexity: `56.54`.**

**Item 2 — improved / other variants reported by this paper:**

| Variant | Params | Val | Test | Location / line |
|---|---|---|---|---|
| AWD-LSTM-MoS w/o finetune | 22M | 58.08 | 55.97 | Table 1, 267–270 |
| **AWD-LSTM-MoS + dynamic evaluation †** | 22M | 48.33 | **47.69** | Table 1, 287–290 |
| AWD-LSTM-MoC (their low-rank baseline) | — | 59.82 | 57.55 | Table 5, 414–418 |
| AWD-LSTM re-run (Merity hyper-params) | — | 61.49 | 58.95 | Table 5, 419–423 |
| AWD-LSTM re-run (MoS hyper-params) | — | 78.86 | 74.86 | Table 5, 424–428 |
| MoS with 3 Softmaxes | — | — | 58.62 | Table 7, 460–462 |
| MoS with 5 Softmaxes | — | — | 57.36 | Table 7, 464–466 |
| MoS with 10 Softmaxes | — | — | 56.33 | Table 7, 468–470 |
| MoS with 15 Softmaxes | — | — | 55.97 | Table 7, 472–474 |
| MoS with 20 Softmaxes | — | — | 56.17 | Table 7, 476–478 |

- Abstract quote (line 14, ≤40 words): "improve the state-of-the-art perplexities on Penn
  Treebank and WikiText-2 to 47.69 and 40.68 respectively." (47.69 uses dynamic evaluation.)
- Table 1 caption (line 290): "† indicates using dynamic evaluation."
- Table 7 numbers are "test perplexity … **without finetuning**" (line 482), which is why the
  15-Softmax entry is 55.97 and not 54.44.

**Item 4 — other pool papers' numbers quoted here (Table 1, lines 202–290):**

| Source paper | Quoted flattened row | Line |
|---|---|---|
| Zaremba (1409.2329) | `Zaremba et al. 2014 – LSTM | 20M | 86.2 | 82.7` | 212–215 |
| Gal (1512.05287) | `Gal & Ghahramani 2016 – Variational LSTM (MC) | 20M | - | 78.6` | 217–220 |
| Kim (1508.06615) | `Kim et al. 2016 – CharCNN | 19M | - | 78.9` | 222–225 |
| Inan (1611.01462) | `Inan et al. 2016 – Tied Variational LSTM + augmented loss | 24M | 75.7 | 73.2` | 237–240 |
| Zilly (1607.03474) | `Zilly et al. 2016 – Variational RHN | 23M | 67.9 | 65.4` | 242–245 |
| Zoph (1611.01578) | `Zoph & Le 2016 – NAS Cell | 25M | - | 64.0` | 247–250 |
| Melis (1707.05589) | `Melis et al. 2017 – 2-layer skip connection LSTM | 24M | 60.9 | 58.3` | 252–255 |
| Merity (1708.02182) w/o finetune | `Merity et al. 2017 – AWD-LSTM w/o finetune | 24M | 60.7 | 58.8` | 257–260 |
| Merity (1708.02182) | `Merity et al. 2017 – AWD-LSTM | 24M | 60.0 | 57.3` | 262–265 |
| Merity (1708.02182) + cache | `Merity et al. 2017 – AWD-LSTM + continuous cache pointer † | 24M | 53.9 | 52.8` | 277–280 |

Yang quotes **8 of the other 10** pool papers. Not quoted: Press & Wolf (1608.05859) — cited
for weight tying (line 25, "Press & Wolf 2017") but no number — and Tjandra (1706.02222),
which is neither cited nor quoted.

**Item 6 — ambiguities:**
1. The headline number in the abstract (`47.69`) **uses dynamic evaluation** and must not
   be used for item 1. The dynamic-eval-free, fine-tuned number is `54.44`.
2. Yang labels Melis's 24M depth-4 model as "**2-layer** skip connection LSTM" (line 252)
   while Merity labels the same 60.9/58.3 result as "**4-layer** skip connection LSTM"
   (line 338 of 1708.02182). Melis's own Table 1 gives depth **4** for 60.9/58.3. Yang's
   label is wrong; the number is right. (Yang's WT2 table correctly uses "2-layer" for the
   WT2 69.1/65.9 row.)
3. Yang's own re-run of AWD-LSTM with Merity's hyper-parameters gives PTB test **58.95**
   (Table 5, line 421), not the 57.3 Merity reports — because the ablation table excludes
   fine-tuning and dynamic evaluation (line 398). A reader could read 58.95 as "AWD-LSTM's
   PTB number" from this paper.

---

# Summary table (a): ranking by item-1 single-model PTB test perplexity
### (no dynamic evaluation, no cache/pointer, no ensemble)

| # | PTB test PPL | arXiv id | Short name | Model as named in the paper | Val PPL |
|---|---|---|---|---|---|
| 1 | **54.44** | 1711.03953 | Yang MoS | AWD-LSTM-MoS (22M) | 56.54 |
| 2 | **57.3** | 1708.02182 | Merity AWD-LSTM | AWD-LSTM 3-layer LSTM (tied), 24M | 60.0 |
| 3 | **58.3** | 1707.05589 | Melis SOTA eval | LSTM, 24M, depth 4 | 60.9 |
| 4 | **62.4** | 1611.01578 | Zoph NAS | NAS base 8 + shared embeddings, 54M | not reported |
| 5 | **65.4** | 1607.03474 | Zilly RHN | Variational RHN + WT, 23M | 67.9 |
| 6 | **66.0** | 1608.05859 | Press & Wolf tied | RHN + BD + WT, 24M | 68.1 |
| 6= | **66.0** | 1611.01462 | Inan tying | VD-RHN +RE, 24M | 68.1 |
| 8 | **73.4 ± 0.0** | 1512.05287 | Gal variational dropout | Variational LSTM (large, untied, MC) | not reported (− ) |
| 9 | **78.4** | 1409.2329 | Zaremba RNN reg. | Large regularized LSTM, 2×1500 | 82.2 |
| 10 | **78.9** | 1508.06615 | Kim char-CNN | LSTM-Char-Large, 19m | not reported |
| 11 | **87.38** | 1706.02222 | Tjandra GRURNTN | GRURNTN, 256 hidden, ~12M | not reported |

Caveats attached to this ranking:
- **Rank 3 (Melis):** the paper's own Table 4 contains a better number, `58.0` ("+ Tied
  gates", 24M, depth 4). Using 58.0 would move Melis to rank 3 still, but ahead of nothing —
  the ordering is unchanged. It would, however, change the headline "Melis = 58.3" claim.
- **Ranks 6/6= are the same number reported by two papers** (66.0, val 68.1, 24M) for what
  is arguably the **same model**: weight tying / reused embeddings applied to Zilly's RHN.
  Press & Wolf call it "RHN + BD + WT"; Inan call it "VD-RHN +RE (Zilly et al. 2016)". If
  the pure-own-architecture reading is used instead, Press & Wolf = 73.2 and Inan = 68.5,
  which reorders ranks 5–7 to: Zilly 65.4, Inan 68.5, Press & Wolf 73.2 (and then Gal 73.4).
- **Rank 8 (Gal):** 73.4 uses MC dropout (1000-sample test-time averaging of one model).
  Excluding MC gives 75.2 (untied) / 75.0 (tied), which does not change the ordering.
- **Rank 2 (Merity):** 57.3 includes a fine-tuning pass; without it, 58.8, which would swap
  ranks 2 and 3 against Melis's 58.3 (58.3 < 58.8).

# Summary table (b): ranking with dynamic evaluation / cache / ensembles allowed

Best PTB test perplexity each paper reports **by any means**, including cache/pointer,
dynamic evaluation, ensembles and fine-tuning:

| # | PTB test PPL | arXiv id | Short name | What produces it |
|---|---|---|---|---|
| 1 | **47.69** | 1711.03953 | Yang MoS | AWD-LSTM-MoS + **dynamic evaluation** |
| 2 | **52.8** | 1708.02182 | Merity AWD-LSTM | AWD-LSTM + **continuous cache pointer** |
| 3 | **58.0** | 1707.05589 | Melis SOTA eval | LSTM 24M depth 4, **+ Tied gates** (Table 4 ablation) |
| 4 | **62.4** | 1611.01578 | Zoph NAS | NAS base 8 + shared embeddings, 54M (no such variant exists) |
| 5 | **65.4** | 1607.03474 | Zilly RHN | Variational RHN + WT (no such variant exists) |
| 6 | **66.0** | 1608.05859 | Press & Wolf tied | RHN + BD + WT (no such variant exists) |
| 6= | **66.0** | 1611.01462 | Inan tying | VD-RHN +RE (no such variant exists) |
| 8 | **68.7** | 1512.05287 | Gal variational dropout | **10-model ensemble** of Variational LSTMs (MC) |
| 8= | **68.7** | 1409.2329 | Zaremba RNN reg. | **38-model ensemble** of large regularized LSTMs |
| 10 | **78.9** | 1508.06615 | Kim char-CNN | LSTM-Char-Large — ensembles explicitly declined |
| 11 | **87.38** | 1706.02222 | Tjandra GRURNTN | GRURNTN — no variants reported |

Notes:
- Six of the eleven papers (Zoph, Zilly, Press & Wolf, Inan, Kim, Tjandra) report **no**
  cache/dynamic-eval/ensemble variant at all, so (b) equals (a) for them.
- Zaremba's 68.7 (38 models, 2.51B params per Inan's table) and Gal's 68.7 (10 models, 660M)
  are numerically identical. Gal points this out explicitly (line 355). Inan's Table 3
  lists both rows adjacently (lines 454–462), producing two different "68.7 on PTB" claims
  with different model counts and parameter counts in one table.
- Melis's 58.0 is an ablation row, not a headline. Using the headline 58.3 leaves the
  ordering unchanged.

# Summary table (c): every occurrence of `57.3`, `52.8` or "AWD-LSTM" in the OTHER 10 papers

Exhaustive `grep -i -E "AWD|57\.3|52\.8"` over the other ten files. **Only 2 of the other
10 papers contain any of these**; the other 8 (1409.2329, 1508.06615, 1512.05287,
1607.03474, 1608.05859, 1611.01462, 1611.01578, 1706.02222) contain **zero** hits — all
eight predate 1708.02182 except 1706.02222 (Tjandra, June 2017), which simply never cites it.

### 1707.05589 (Melis) — 3 hits, none of them `52.8`

| Line | Context | Quote |
|---|---|---|
| 239–243 | Table 1, PTB | flattened row: `AWD-LSTM, Merity et al. 2017 † | 24M | 3 | 60.0 | 57.3` |
| 299 | Table 1 caption | "All results except those from Zaremba are with shared input and output embeddings. VD stands for Variational Dropout from Gal & Ghahramani 2016 . †: parallel work." |
| 382–385 | Table 2, **WikiText-2** (not PTB) | flattened row: `AWD-LSTM, Merity et al. 2017 † 33M | 3 | 68.6 | 65.8` |

Melis also discusses Merity without naming AWD-LSTM (line 98, ≤40 words): "In parallel work
with a remarkable overlap with ours, Merity et al. 2017 demonstrate the utility of adding a
Neural Cache ( Grave et al. 2016 )." — the cache is mentioned but **52.8 never appears**.

### 1711.03953 (Yang MoS) — 16 hits, including both `57.3` and `52.8`

| Line | Context | Quote |
|---|---|---|
| 257–260 | Table 1, PTB | `Merity et al. 2017 – AWD-LSTM w/o finetune | 24M | 60.7 | 58.8` |
| 262–265 | Table 1, PTB | `Merity et al. 2017 – AWD-LSTM | 24M | 60.0 | **57.3**` |
| 267–270 | Table 1, PTB | `Ours – AWD-LSTM-MoS w/o finetune | 22M | 58.08 | 55.97` |
| 272–275 | Table 1, PTB | `Ours – AWD-LSTM-MoS | 22M | 56.54 | 54.44` |
| 277–280 | Table 1, PTB | `Merity et al. 2017 – AWD-LSTM + continuous cache pointer † | 24M | 53.9 | **52.8**` |
| 282–285 | Table 1, PTB | `Krause et al. 2017 – AWD-LSTM + dynamic evaluation † | 24M | 51.6 | 51.1` |
| 287–290 | Table 1, PTB | `Ours – AWD-LSTM-MoS + dynamic evaluation † | 22M | 48.33 | 47.69` |
| 312–320 | Table 2, **WikiText-2** | `Merity et al. 2017 – AWD-LSTM w/o finetune | 33M | 69.1 | 66.0`; `Merity et al. 2017 – AWD-LSTM | 33M | 68.6 | 65.8` |
| 322–330 | Table 2, WikiText-2 | `Ours – AWD-LSTM-MoS w/o finetune | 35M | 66.01 | 63.33`; `Ours – AWD-LSTM-MoS | 35M | 63.88 | 61.45` |
| 332–335 | Table 2, WikiText-2 | `Merity et al. 2017 – AWD-LSTM + continuous cache pointer † | 33M | 53.8 | 52.0` |
| 337–345 | Table 2, WikiText-2 | `Krause et al. 2017 – AWD-LSTM + dynamic evaluation † | 33M | 46.4 | 44.3`; `Ours – AWD-LSTM-MoS + dynamical evaluation † | 35M | 42.41 | 40.68` |
| 189 | Section 3.1, prose | "For fair comparison, we closely follow the regularization and optimization techniques introduced by Merity et al. 2017 ." |
| 397 | Section 3.2, prose | "In addition, we adopt the hyper-parameters used to obtain the best MoS model (denoted as MoS hyper-parameters), and train a baseline AWD-LSTM." |
| 400 | Section 3.2, prose | "Compared to the vanilla AWD-LSTM, though being more expressive, MoC performs only better on PTB, but worse on WT2." |
| 409–418 | Table 5, ablation | `AWD-LSTM-MoS | 58.08 | 55.97 | 66.01 | 63.33`; `AWD-LSTM-MoC | 59.82 | 57.55 | 68.76 | 65.98` |
| 419–428 | Table 5, ablation | `AWD-LSTM ( Merity et al. 2017 hyper-parameters) | 61.49 | 58.95 | 68.73 | 65.40`; `AWD-LSTM (MoS hyper-parameters) | 78.86 | 74.86 | 72.73 | 69.18` |

**Redundancy assessment for AWD-LSTM's 57.3:** independently corroborated by exactly
**two** other papers in this pool (Melis 1707.05589 and Yang 1711.03953), both giving
`60.0 / 57.3` at 24M, matching Merity's own Table 1 exactly. The cache number `52.8` is
corroborated by **only one** other paper (Yang), which also matches exactly (`53.9 / 52.8`,
24M). Eight of the eleven papers say nothing about either number.

---

# Consolidated list of ambiguities

1. **1512.05287 (Gal) — MC dropout:** 73.4 requires 1000 test-time stochastic passes. The
   paper calls it a single model; a strict "no test-time augmentation" reading gives 75.2
   (untied) or 75.0 (tied). Ordering unchanged either way.
2. **1607.03474 (Zilly) — weight tying:** 65.4 (with WT) vs 68.5 (without). WT is not
   Zilly's contribution; Zilly credits Inan & Khosravi 2016 and Press & Wolf 2016. Citing
   papers split between the two values.
3. **1608.05859 (Press & Wolf) — whose architecture:** best number 66.0 is their weight
   tying applied to Zilly's RHN. Best pure-LSTM variant is 73.2. Downstream papers quote
   73.2 as "Press & Wolf" and attribute the 66.0 row to Zilly/Inan instead.
4. **1611.01462 (Inan) — same collision:** their best 66.0 is labelled "VD-RHN +RE (Zilly et
   al. 2016)" in their own Table 3. Pure-Inan architecture gives 68.5, which is numerically
   identical to Zilly's own no-WT RHN value listed two rows above it.
5. **1707.05589 (Melis) — 58.3 vs 58.0:** the Table 4 "+ Tied gates" ablation (24M, depth 4)
   reaches 60.4/58.0, better than the Table 1 headline 60.9/58.3 that everyone quotes.
6. **1708.02182 (Merity) — fine-tuning:** 57.3 includes a fine-tuning pass; 58.8 without.
   If fine-tuning is excluded, Merity (58.8) falls behind Melis (58.3).
7. **1711.03953 (Yang) — abstract number is dynamic-eval:** 47.69 uses dynamic evaluation;
   the correct no-dyn-eval number is 54.44 (or 55.97 without fine-tuning).
8. **1508.06615 (Kim) — small model inconsistency:** headline small model 92.3 (one highway
   layer) is worse than the 90.1 in the paper's own Table 7 (two highway layers).
9. **Parameter-count disagreements for the same models:** Zaremba's medium/large reported as
   20M/66M by Gal, Merity, Zilly, Inan, Zoph, Yang; as 20m/**52m** by Kim; as **10M/24M** by
   Melis. Inan's medium/large reported as 9M/28M by Melis, 24M/51M by Merity, 24M by Yang.
10. **Duplicate value 73.2 with two owners:** Press & Wolf's Large+BD+WT (51M) and Inan's
    medium VD-LSTM+REAL (24M) both report PTB test 73.2. Zoph and Melis attribute 73.2 to
    Press & Wolf; Merity and Yang attribute 73.2 to Inan. Both attributions are correct for
    their respective source rows.
11. **Duplicate value 68.7 with two owners:** Zaremba's 38-model ensemble and Gal's 10-model
    ensemble. Both appear in Inan's Table 3.
12. **Duplicate value 68.5 with two owners inside one table:** Inan's Table 3 lists both
    "VD-RHN (Zilly et al. 2016) 32M 71.2 68.5" and "VD-LSTM +REAL (large) 51M 71.1 68.5".
13. **Yang mislabels Melis's depth:** "2-layer skip connection LSTM" for what Melis and
    Merity both record as a 4-layer model (60.9/58.3).
14. **Press & Wolf's validation number for Gal (78.1)** does not appear anywhere in Gal's
    own paper (which gives 77.9 ± 0.3 / 77.3 ± 0.2).
15. **1706.02222 (Tjandra) cross-reference error:** text says "Table I shows the PTB test set
    PPL" but the word-level perplexities are in TABLE II.
16. **1708.02182 string collision:** `78.4` appears in Merity's paper both as Zaremba's PTB
    test perplexity and as an AWD-LSTM WikiText-2 **validation** value (− weight-dropping).

# Not found / not reported

- **PTB validation perplexity is not reported at all** by: 1508.06615 (Kim, test-only Table 3),
  1611.01578 (Zoph, test-only Table 2), 1706.02222 (Tjandra, test-only TABLE II; validation
  only in a figure).
- **1512.05287 (Gal):** validation perplexity for the MC-dropout rows is `−` (the paper
  reports validation only for the non-MC rows: 77.3 ± 0.2 tied, 77.9 ± 0.3 untied).
- **1607.03474 (Zilly):** the depth-1 baseline `90.6` cited in the abstract appears in no
  table; it is only in Figure 5(a), which is an image and absent from the text extraction.
- **1706.02222 (Tjandra)** quotes no number from any other pool paper, and no pool paper
  quotes Tjandra. Zero redundancy in both directions.
- **1409.2329 (Zaremba)** quotes no other pool paper (it is the earliest).
- **Press & Wolf (1608.05859) is never quoted numerically** by Merity (1708.02182) or Yang
  (1711.03953), though both cite it for weight tying.
- **Kim (1508.06615) and Gal (1512.05287) are never quoted numerically** by Melis
  (1707.05589), which cites Gal for variational dropout only.
- No corrupted or line-split numbers were found; nothing had to be reconstructed from raw
  characters.
