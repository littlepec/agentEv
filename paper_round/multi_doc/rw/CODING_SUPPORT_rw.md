# CODING_SUPPORT_rw -- round_RW draft coding support (RW-b + RW-c)

**DRAFT. AI first pass. `human_reviewed=false`.** Every verdict, class and tally below is produced by string matching in `build_coding_support.py` against the cached records, the merge outputs and `private_eval.json` (evaluation only, never in any prompt). Nothing here is human-reviewed; the main session codes the endpoints from the records and the verbatim sentences quoted below.

## Run status

- **Extraction**: rep1 23/23 documents cached, rep2 8/23. rep2 was stopped at `1707.05589` after two attempts truncated at the 4096-token output cap and was deliberately NOT re-run; it stays partial and is reported as such. **Every merge cell in this file uses the rep1 records**, so merge repetitions measure merge variance only, not extraction variance.
- **Merge cells**: A x2, B x2, C x8, CP x4, Df x2, Dp x8, DpP x4 = 30 total, 30 with a machine-readable table.
- **RW-b deviation** (authorized, in LOG.md and `ledger_baseline.json`): the originally frozen merge configuration (thinking enabled, no `json_object`, max_tokens 16384) spent its whole output budget on reasoning tokens and failed 10/10. Only the merge call configuration changed (thinking disabled, `json_object`, max_tokens 8192, prose inside the JSON as `answer_prose`). Those failed calls are kept in `rw_a_failed_merges/`.
- **RW-c** (PREREG_rw_c.md): confirmation arm = C and Dp reps 3-8 on the byte-identical RW-b prompt (verified against the stored RW-b request), pooled with RW-b's reps 1-2 to 8 cells per condition. Policy arm = `--policy`, which appends three source-policy sentences verbatim after the records JSON and adds an optional `unverified` list to the schema; both are gated on the flag.

Truth source status: private_eval.json loaded.

Automated truth column: `match` = the value in `single_model_ranking_truth`; `variant` = an acceptable variant recorded there (plus 58.8 for 1708.02182, acceptable if labelled without fine-tuning); `NOTE VALUE 53.3` = the value that exists only in the alternate note; `cache/pointer variant` = 52.8; otherwise `MISMATCH`. It is a per-value lookup, not a verdict on the record: ablation rows, WikiText-2 rows and cache rows legitimately read `MISMATCH`. The line that matters is the **draft judgement** under each table.

Two attribution patterns are reported throughout: `[ATTRIB]` is the frozen pattern used by `rw_pipeline.py screen`; `[ATTRIB2]` is the stricter pattern required by PREREG_rw_c.md E6, which also counts "reported by <arxiv id>".

### Run anomalies (automated scan of the caches and call logs)

- rep1 `1708.02182`: first attempt failed (unparseable or error), one identical retry made (retry finish=stop, out=3772); both call logs kept
- rep2 `1707.05589`: first attempt failed (unparseable or error), one identical retry made (retry finish=length, out=4096); both call logs kept
- merge B_rep1: one identical retry made
- merge C_rep1: one identical retry made
- merge Df_rep1: one identical retry made
- merge Dp_rep1: one identical retry made

## (a) Extraction records per paper x rep

### rep1

#### 1409.2329 — Recurrent Neural Network Regularization

| source | value | dyn/cache/ens/ft | location | truth (automated) | quote (truncated 150) |
|---|---|---|---|---|---|
| paper `1409.2329.txt` | 82.7 | no/no/no/unknown | Table 1 | MISMATCH (truth: 78.4) | Medium regularized LSTM 86.2 82.7 |
| paper `1409.2329.txt` | 78.4 | no/no/no/unknown | Table 1 | match 78.4 | Large regularized LSTM 82.2 78.4 |
| paper `1409.2329.txt` | 114.5 | no/no/no/unknown | Table 1 | MISMATCH (truth: 78.4) | non-regularized LSTM 120.7 114.5 |
| paper `1409.2329.txt` | 77.0 | no/no/yes/unknown | Table 1 | MISMATCH (truth: 78.4) | 2 medium regularized LSTMs 80.6 77.0 |
| paper `1409.2329.txt` | 73.3 | no/no/yes/unknown | Table 1 | MISMATCH (truth: 78.4) | 5 medium regularized LSTMs 76.7 73.3 |
| paper `1409.2329.txt` | 72.0 | no/no/yes/unknown | Table 1 | MISMATCH (truth: 78.4) | 10 medium regularized LSTMs 75.2 72.0 |
| paper `1409.2329.txt` | 73.6 | no/no/yes/unknown | Table 1 | MISMATCH (truth: 78.4) | 2 large regularized LSTMs 76.9 73.6 |
| paper `1409.2329.txt` | 69.5 | no/no/yes/unknown | Table 1 | MISMATCH (truth: 78.4) | 10 large regularized LSTMs 72.8 69.5 |
| paper `1409.2329.txt` | 68.7 | no/no/yes/unknown | Table 1 | MISMATCH (truth: 78.4) | 38 large regularized LSTMs 71.9 68.7 |
| paper `1409.2329.txt` | 96.1 | no/no/yes/unknown | Table 1 | MISMATCH (truth: 78.4) | 2 non-regularized LSTMs 100.4 96.1 |
| paper `1409.2329.txt` | 84.1 | no/no/yes/unknown | Table 1 | MISMATCH (truth: 78.4) | 5 non-regularized LSTMs 87.9 84.1 |
| paper `1409.2329.txt` | 80.0 | no/no/yes/unknown | Table 1 | MISMATCH (truth: 78.4) | 10 non-regularized LSTMs 83.5 80.0 |
| note `1409.2329_note.txt` | 82.7 | no/no/no/no | unknown | MISMATCH (truth: 78.4) | The medium regularized LSTM reaches 82.7, and the large regularized LSTM reaches 78.4. |
| note `1409.2329_note.txt` | 78.4 | no/no/no/no | unknown | match 78.4 | The medium regularized LSTM reaches 82.7, and the large regularized LSTM reaches 78.4. |
| note `1409.2329_note.txt` | 77.0 | no/no/yes/no | unknown | MISMATCH (truth: 78.4) | It lists 2 medium regularized LSTMs at 77.0, 5 medium regularized LSTMs at 73.3, 10 medium regularized LSTMs at 72.0 |
| note `1409.2329_note.txt` | 73.3 | no/no/yes/no | unknown | MISMATCH (truth: 78.4) | It lists 2 medium regularized LSTMs at 77.0, 5 medium regularized LSTMs at 73.3, 10 medium regularized LSTMs at 72.0 |
| note `1409.2329_note.txt` | 72.0 | no/no/yes/no | unknown | MISMATCH (truth: 78.4) | It lists 2 medium regularized LSTMs at 77.0, 5 medium regularized LSTMs at 73.3, 10 medium regularized LSTMs at 72.0 |
| note `1409.2329_note.txt` | 73.6 | no/no/yes/no | unknown | MISMATCH (truth: 78.4) | 2 large regularized LSTMs at 73.6, 10 large regularized LSTMs at 69.5, and 38 large regularized LSTMs at 68.7 |
| note `1409.2329_note.txt` | 69.5 | no/no/yes/no | unknown | MISMATCH (truth: 78.4) | 2 large regularized LSTMs at 73.6, 10 large regularized LSTMs at 69.5, and 38 large regularized LSTMs at 68.7 |
| note `1409.2329_note.txt` | 68.7 | no/no/yes/no | unknown | MISMATCH (truth: 78.4) | 2 large regularized LSTMs at 73.6, 10 large regularized LSTMs at 69.5, and 38 large regularized LSTMs at 68.7 |

**draft judgement (paper file, rep1)**: CORRECT — - — value 78.4 (match 78.4), flags no/no/no/unknown

- faithful note taken alone (weak heuristic, informational): CORRECT — - — value 78.4 (match 78.4), flags no/no/no/no

#### 1508.06615 — Character-Aware Neural Language Models

| source | value | dyn/cache/ens/ft | location | truth (automated) | quote (truncated 150) |
|---|---|---|---|---|---|
| paper `1508.06615.txt` | 92.3 | no/no/no/unknown | Table 3 | MISMATCH (truth: 78.9) | LSTM-Char-Small 92.3 5 m |
| paper `1508.06615.txt` | 78.9 | no/no/no/unknown | Table 3 | match 78.9 | LSTM-Char-Large 78.9 19 m |
| paper `1508.06615.txt` | 100.3 | no/no/no/unknown | Table 7 | MISMATCH (truth: 78.9) | No Highway Layers 100.3 84.6 |
| paper `1508.06615.txt` | 84.6 | no/no/no/unknown | Table 7 | MISMATCH (truth: 78.9) | No Highway Layers 100.3 84.6 |
| paper `1508.06615.txt` | 92.3 | no/no/no/unknown | Table 7 | MISMATCH (truth: 78.9) | One Highway Layer 92.3 79.7 |
| paper `1508.06615.txt` | 79.7 | no/no/no/unknown | Table 7 | MISMATCH (truth: 78.9) | One Highway Layer 92.3 79.7 |
| paper `1508.06615.txt` | 90.1 | no/no/no/unknown | Table 7 | MISMATCH (truth: 78.9) | Two Highway Layers 90.1 78.9 |
| paper `1508.06615.txt` | 78.9 | no/no/no/unknown | Table 7 | match 78.9 | Two Highway Layers 90.1 78.9 |
| paper `1508.06615.txt` | 111.2 | no/no/no/unknown | Table 7 | MISMATCH (truth: 78.9) | One MLP Layer 111.2 92.6 |
| paper `1508.06615.txt` | 92.6 | no/no/no/unknown | Table 7 | MISMATCH (truth: 78.9) | One MLP Layer 111.2 92.6 |
| paper `1508.06615.txt` | 81 | no/no/no/unknown | Further Observations | MISMATCH (truth: 78.9) | Combining word embeddings with the CharCNN's output to form a combined representation of a word (to be used as input to the LSTM) resulted in slightly |
| note `1508.06615_note.txt` | 78.9 | no/no/no/no | unknown | match 78.9 | LSTM-Char-Large attains 78.9; LSTM-Char-Small attains 92.3. Predictions are made at the word level. These are single-model results. |
| note `1508.06615_note.txt` | 92.3 | no/no/no/no | unknown | MISMATCH (truth: 78.9) | LSTM-Char-Large attains 78.9; LSTM-Char-Small attains 92.3. Predictions are made at the word level. These are single-model results. |
| note `1508.06615_note.txt` | 84.6 | no/no/no/no | unknown | MISMATCH (truth: 78.9) | Ablations show large model perplexities of 84.6 without highway layers, 79.7 with one highway layer, and 78.9 with two highway layers |
| note `1508.06615_note.txt` | 79.7 | no/no/no/no | unknown | MISMATCH (truth: 78.9) | Ablations show large model perplexities of 84.6 without highway layers, 79.7 with one highway layer, and 78.9 with two highway layers |
| note `1508.06615_note.txt` | 78.9 | no/no/no/no | unknown | match 78.9 | Ablations show large model perplexities of 84.6 without highway layers, 79.7 with one highway layer, and 78.9 with two highway layers |
| note `1508.06615_note.txt` | 100.3 | no/no/no/no | unknown | MISMATCH (truth: 78.9) | small model values are 100.3, 92.3, and 90.1 respectively |
| note `1508.06615_note.txt` | 92.3 | no/no/no/no | unknown | MISMATCH (truth: 78.9) | small model values are 100.3, 92.3, and 90.1 respectively |
| note `1508.06615_note.txt` | 90.1 | no/no/no/no | unknown | MISMATCH (truth: 78.9) | small model values are 100.3, 92.3, and 90.1 respectively |

**draft judgement (paper file, rep1)**: CORRECT — - — value 78.9 (match 78.9), flags no/no/no/unknown

- faithful note taken alone (weak heuristic, informational): CORRECT — - — value 78.9 (match 78.9), flags no/no/no/no

#### 1512.05287 — A Theoretically Grounded Application of Dropout in Recurrent Neural Networks

| source | value | dyn/cache/ens/ft | location | truth (automated) | quote (truncated 150) |
|---|---|---|---|---|---|
| paper `1512.05287.txt` | 79.7 ± 0.1 | no/no/no/unknown | Table 1 | MISMATCH (truth: 73.4 MC (75.2/75.0 non-MC acceptable)) | Variational (tied weights) 81.8 ± 0.2 79.7 ± 0.1 4.7 K 77.3 ± 0.2 75.0 ± 0.1 2.4 K |
| paper `1512.05287.txt` | 75.0 ± 0.1 | no/no/no/unknown | Table 1 | variant 75.0 (acceptable) | Variational (tied weights) 81.8 ± 0.2 79.7 ± 0.1 4.7 K 77.3 ± 0.2 75.0 ± 0.1 2.4 K |
| paper `1512.05287.txt` | 79.0 ± 0.1 | no/no/no/unknown | Table 1 | MISMATCH (truth: 73.4 MC (75.2/75.0 non-MC acceptable)) | Variational (tied weights, MC) − 79.0 ± 0.1 − − 74.1 ± 0.0 − |
| paper `1512.05287.txt` | 74.1 ± 0.0 | no/no/no/unknown | Table 1 | MISMATCH (truth: 73.4 MC (75.2/75.0 non-MC acceptable)) | Variational (tied weights, MC) − 79.0 ± 0.1 − − 74.1 ± 0.0 − |
| paper `1512.05287.txt` | 79.7 ± 0.1 | no/no/no/unknown | Table 1 | MISMATCH (truth: 73.4 MC (75.2/75.0 non-MC acceptable)) | Variational (untied weights) 81.9 ± 0.2 79.7 ± 0.1 2.7 K 77.9 ± 0.3 75.2 ± 0.2 1.6 K |
| paper `1512.05287.txt` | 75.2 ± 0.2 | no/no/no/unknown | Table 1 | variant 75.2 (acceptable) | Variational (untied weights) 81.9 ± 0.2 79.7 ± 0.1 2.7 K 77.9 ± 0.3 75.2 ± 0.2 1.6 K |
| paper `1512.05287.txt` | 78.6 ± 0.1 | no/no/no/unknown | Table 1 | MISMATCH (truth: 73.4 MC (75.2/75.0 non-MC acceptable)) | Variational (untied weights, MC) − 78.6 ± 0.1 − − 73.4 ± 0.0 − |
| paper `1512.05287.txt` | 73.4 ± 0.0 | no/no/no/unknown | Section 5.1 and Table 1 | match 73.4 | Test perplexity is reduced from 78.4 down to 73.4 (with MC dropout and untied weights). |
| paper `1512.05287.txt` | 68.7 | no/no/yes/unknown | Section 5.1 | MISMATCH (truth: 73.4 MC (75.2/75.0 non-MC acceptable)) | Using 10 Variational LSTMs we improve [ 4 ] ’s test set perplexity from 69.5 to 68.7 |
| note `1512.05287_note.txt` | 73.4 | no/no/no/no | unknown | match 73.4 | The paper reports 73.4 test perplexity for the proposed Variational LSTM on Penn Treebank. |
| note `1512.05287_note.txt` | 73.4 | unknown/unknown/unknown/unknown | language modelling table | match 73.4 | Variational untied weights MC (medium 78.6, large 73.4) |
| note `1512.05287_note.txt` | 78.6 | unknown/unknown/unknown/unknown | language modelling table | MISMATCH (truth: 73.4 MC (75.2/75.0 non-MC acceptable)) | Variational untied weights MC (medium 78.6, large 73.4) |
| note `1512.05287_note.txt` | 75.2 | unknown/unknown/unknown/unknown | language modelling table | variant 75.2 (acceptable) | Variational untied weights (medium 79.7, large 75.2) |
| note `1512.05287_note.txt` | 79.7 | unknown/unknown/unknown/unknown | language modelling table | MISMATCH (truth: 73.4 MC (75.2/75.0 non-MC acceptable)) | Variational untied weights (medium 79.7, large 75.2) |
| note `1512.05287_note.txt` | 74.1 | unknown/unknown/unknown/unknown | language modelling table | MISMATCH (truth: 73.4 MC (75.2/75.0 non-MC acceptable)) | Variational tied weights MC (medium 79.0, large 74.1) |
| note `1512.05287_note.txt` | 79.0 | unknown/unknown/unknown/unknown | language modelling table | MISMATCH (truth: 73.4 MC (75.2/75.0 non-MC acceptable)) | Variational tied weights MC (medium 79.0, large 74.1) |
| note `1512.05287_note.txt` | 75.0 | unknown/unknown/unknown/unknown | language modelling table | variant 75.0 (acceptable) | Variational tied weights (medium 79.7, large 75.0) |
| note `1512.05287_note.txt` | 79.7 | unknown/unknown/unknown/unknown | language modelling table | MISMATCH (truth: 73.4 MC (75.2/75.0 non-MC acceptable)) | Variational tied weights (medium 79.7, large 75.0) |
| note `1512.05287_note.txt` | 68.7 | unknown/unknown/yes/unknown | unknown | MISMATCH (truth: 73.4 MC (75.2/75.0 non-MC acceptable)) | Using 10 Variational LSTMs with MC dropout improves Zaremba et al.'s test set perplexity from 69.5 to 68.7 |

**draft judgement (paper file, rep1)**: CORRECT — - — value 75.0 ± 0.1 (variant 75.0 (acceptable)), flags no/no/no/unknown

- faithful note taken alone (weak heuristic, informational): CORRECT — - — value 73.4 (match 73.4), flags no/no/no/no

#### 1607.03474 — Recurrent Highway Networks

| source | value | dyn/cache/ens/ft | location | truth (automated) | quote (truncated 150) |
|---|---|---|---|---|---|
| paper `1607.03474.txt` | 68.5 | no/no/no/unknown | Table 1 | variant 68.5 (acceptable) | Variational RHN 32 M 71.2 68.5 |
| paper `1607.03474.txt` | 65.4 | no/no/no/unknown | Table 1 | match 65.4 | Variational RHN + WT 23 M 67.9 65.4 |
| paper `1607.03474.txt` | 67.9/65.4 | no/no/no/unknown | Section 5.2.1 Penn Treebank | MISMATCH (truth: 65.4 (68.5 without WT acceptable)) | For the best 10 layer model, reducing the weight decay further improves the results to 67.9/65.4 validation/test perplexity. |
| note `1607.03474_note.txt` | 65.4 | no/no/no/no | unknown | match 65.4 | The paper reports its best Penn Treebank word-level test perplexity for the proposed model as 65.4 for Variational RHN + WT. |
| note `1607.03474_note.txt` | 68.5 | no/no/no/no | unknown | variant 68.5 (acceptable) | The paper also reports 68.5 test perplexity for Variational RHN without WT. |
| note `1607.03474_note.txt` | 67.9/65.4 | no/no/no/no | unknown | MISMATCH (truth: 65.4 (68.5 without WT acceptable)) | The best 10 layer model with reduced weight decay improves to 67.9/65.4 validation/test perplexity. |
| note `1607.03474_note.txt` | 67.9/65.4 | no/no/no/no | Table 1 | MISMATCH (truth: 65.4 (68.5 without WT acceptable)) | Table 1 lists Variational RHN + WT as 23M parameters with validation/test perplexity 67.9/65.4. |

**draft judgement (paper file, rep1)**: CORRECT — - — value 68.5 (variant 68.5 (acceptable)), flags no/no/no/unknown

- faithful note taken alone (weak heuristic, informational): CORRECT — - — value 65.4 (match 65.4), flags no/no/no/no

#### 1608.05859 — Using the Output Embedding to Improve Language Models

| source | value | dyn/cache/ens/ft | location | truth (automated) | quote (truncated 150) |
|---|---|---|---|---|---|
| paper `1608.05859.txt` | 74.3 | no/no/no/unknown | Table 5 | MISMATCH (truth: 66.0 (73.2 own-architecture acceptable)) | Large + Weight Tying 51M 48.5 77.7 74.3 |
| paper `1608.05859.txt` | 73.2 | no/no/no/unknown | Table 5 | variant 73.2 (acceptable) | Large + BD + WT 51M 28.2 75.8 73.2 |
| paper `1608.05859.txt` | 66.0 | no/no/no/unknown | Table 5 | match 66.0 | RHN + BD + WT 24M 74.1 68.1 66.0 |
| paper `1608.05859.txt` | 112.4 | no/no/no/unknown | Table 6 | MISMATCH (truth: 66.0 (73.2 own-architecture acceptable)) | Small + WT 2.65M 36.4 117.5 112.4 |
| paper `1608.05859.txt` | 111.7 | no/no/no/unknown | Table 6 | MISMATCH (truth: 66.0 (73.2 own-architecture acceptable)) | Small + PR 4.69M 50.8 116.0 111.7 |
| paper `1608.05859.txt` | 100.9 | no/no/no/unknown | Table 6 | MISMATCH (truth: 66.0 (73.2 own-architecture acceptable)) | Small + WT + PR 2.69M 53.5 104.9 100.9 |
| note `1608.05859_note.txt` | 74.3 | no/no/no/no | neural network language model experiments | MISMATCH (truth: 66.0 (73.2 own-architecture acceptable)) | The large NNLM with weight tying (Large + Weight Tying) reaches 74.3 test perplexity. |
| note `1608.05859_note.txt` | 100.9 | no/no/no/no | neural network language model experiments | MISMATCH (truth: 66.0 (73.2 own-architecture acceptable)) | The small NNLM with weight tying and projection regularization (Small + WT + PR) reaches 100.9 test perplexity. |

**draft judgement (paper file, rep1)**: CORRECT — - — value 73.2 (variant 73.2 (acceptable)), flags no/no/no/unknown

- faithful note taken alone (weak heuristic, informational): WRONG — fine-tuning — no record matches truth; values seen: 74.3, 100.9; closest-by-condition 74.3 (no/no/no/no), model="Large NNLM with weight tying (Large + Weight Tying)"

#### 1611.01462 — Tying Word Vectors and Word Classifiers: A Loss Framework for Language Modeling

| source | value | dyn/cache/ens/ft | location | truth (automated) | quote (truncated 150) |
|---|---|---|---|---|---|
| paper `1611.01462.txt` | 82.7 | no/no/no/unknown | Table 1 | MISMATCH (truth: 66.0 (68.5 acceptable)) | VD-LSTM+REAL 86.3 82.7 105.6 98.9 |
| paper `1611.01462.txt` | 73.2 | no/no/no/unknown | Table 1 | MISMATCH (truth: 66.0 (68.5 acceptable)) | VD-LSTM+REAL 75.7 73.2 91.5 87.0 |
| paper `1611.01462.txt` | 68.5 | no/no/no/unknown | Table 1 | variant 68.5 (acceptable) | VD-LSTM+REAL 71.1 68.5 - - |
| paper `1611.01462.txt` | 98.9 | no/no/no/unknown | Table 1 | MISMATCH (truth: 66.0 (68.5 acceptable)) | VD-LSTM+REAL 86.3 82.7 105.6 98.9 |
| paper `1611.01462.txt` | 87.0 | no/no/no/unknown | Table 1 | MISMATCH (truth: 66.0 (68.5 acceptable)) | VD-LSTM+REAL 75.7 73.2 91.5 87.0 |
| paper `1611.01462.txt` | 140.6 | no/no/no/unknown | Table 2 | MISMATCH (truth: 66.0 (68.5 acceptable)) | VD-LSTM+REAL 149.3 140.6 150.5 138.4 |
| paper `1611.01462.txt` | 138.4 | no/no/no/unknown | Table 2 | MISMATCH (truth: 66.0 (68.5 acceptable)) | VD-LSTM+REAL 149.3 140.6 150.5 138.4 |
| paper `1611.01462.txt` | 82.9 | no/no/no/unknown | Table 1 | MISMATCH (truth: 66.0 (68.5 acceptable)) | VD-LSTM+AL 86.3 82.9 110.3 103.8 |
| paper `1611.01462.txt` | 74.7 | no/no/no/unknown | Table 1 | MISMATCH (truth: 66.0 (68.5 acceptable)) | VD-LSTM+AL 77.4 74.7 98.8 93.1 |
| paper `1611.01462.txt` | 71.2 | no/no/no/unknown | Table 1 | MISMATCH (truth: 66.0 (68.5 acceptable)) | VD-LSTM+AL 74.5 71.2 - - |
| paper `1611.01462.txt` | 103.8 | no/no/no/unknown | Table 1 | MISMATCH (truth: 66.0 (68.5 acceptable)) | VD-LSTM+AL 86.3 82.9 110.3 103.8 |
| paper `1611.01462.txt` | 93.1 | no/no/no/unknown | Table 1 | MISMATCH (truth: 66.0 (68.5 acceptable)) | VD-LSTM+AL 77.4 74.7 98.8 93.1 |
| paper `1611.01462.txt` | 142.5 | no/no/no/unknown | Table 2 | MISMATCH (truth: 66.0 (68.5 acceptable)) | VD-LSTM+AL 153.0 142.5 156.4 143.7 |
| paper `1611.01462.txt` | 143.7 | no/no/no/unknown | Table 2 | MISMATCH (truth: 66.0 (68.5 acceptable)) | VD-LSTM+AL 153.0 142.5 156.4 143.7 |
| paper `1611.01462.txt` | 85.1 | no/no/no/unknown | Table 1 | MISMATCH (truth: 66.0 (68.5 acceptable)) | VD-LSTM+RE 89.9 85.1 106.1 100.5 |
| paper `1611.01462.txt` | 73.9 | no/no/no/unknown | Table 1 | MISMATCH (truth: 66.0 (68.5 acceptable)) | VD-LSTM+RE 77.1 73.9 92.3 87.7 |
| paper `1611.01462.txt` | 69.0 | no/no/no/unknown | Table 1 | MISMATCH (truth: 66.0 (68.5 acceptable)) | VD-LSTM+RE 72.5 69.0 - - |
| paper `1611.01462.txt` | 100.5 | no/no/no/unknown | Table 1 | MISMATCH (truth: 66.0 (68.5 acceptable)) | VD-LSTM+RE 89.9 85.1 106.1 100.5 |
| paper `1611.01462.txt` | 87.7 | no/no/no/unknown | Table 1 | MISMATCH (truth: 66.0 (68.5 acceptable)) | VD-LSTM+RE 77.1 73.9 92.3 87.7 |
| paper `1611.01462.txt` | 141.9 | no/no/no/unknown | Table 2 | MISMATCH (truth: 66.0 (68.5 acceptable)) | VD-LSTM+RE 152.4 141.9 152.5 140.9 |
| paper `1611.01462.txt` | 140.9 | no/no/no/unknown | Table 2 | MISMATCH (truth: 66.0 (68.5 acceptable)) | VD-LSTM+RE 152.4 141.9 152.5 140.9 |
| note `1611.01462_note.txt` | 68.5 | no/no/no/no | Table 3, Section 6.3 | variant 68.5 (acceptable) | The paper reports a word-level test perplexity of 68.5 on Penn Treebank for VD-LSTM+REAL (large), its best LSTM model using reused embeddings and augm |

**draft judgement (paper file, rep1)**: CORRECT — - — value 68.5 (variant 68.5 (acceptable)), flags no/no/no/unknown

- faithful note taken alone (weak heuristic, informational): CORRECT — - — value 68.5 (variant 68.5 (acceptable)), flags no/no/no/no

#### 1611.01578 — Neural Architecture Search with Reinforcement Learning

| source | value | dyn/cache/ens/ft | location | truth (automated) | quote (truncated 150) |
|---|---|---|---|---|---|
| paper `1611.01578.txt` | 67.9 | no/no/no/unknown | Table 2 | MISMATCH (truth: 62.4) | Neural Architecture Search with base 8 32M 67.9 67.9 |
| paper `1611.01578.txt` | 64.0 | no/no/no/unknown | Table 2 | MISMATCH (truth: 62.4) | Neural Architecture Search with base 8 and shared embeddings 25M 64.0 64.0 |
| paper `1611.01578.txt` | 62.4 | no/no/no/unknown | Table 2 | match 62.4 | Neural Architecture Search with base 8 and shared embeddings 54M 62.4 62.4 |
| paper `1611.01578.txt` | 1.228 | no/no/no/unknown | Table 3 | MISMATCH (truth: 62.4) | Two Layer with New Cell 6.57M 1.228 |
| paper `1611.01578.txt` | 1.214 | no/no/no/unknown | Table 3 | MISMATCH (truth: 62.4) | Two Layer with New Cell 16.28M 1.214 |
| note `1611.01578_note.txt` | 62.4 | no/no/no/no | unknown | match 62.4 | The paper reports 62.4 test perplexity on Penn Treebank for the best Neural Architecture Search model. |
| note `1611.01578_note.txt` | 64.0 | no/no/no/no | Table 2 | MISMATCH (truth: 62.4) | Table 2 reports 64.0 and 67.9 for other Neural Architecture Search configurations. |
| note `1611.01578_note.txt` | 67.9 | no/no/no/no | Table 2 | MISMATCH (truth: 62.4) | The paper also reports Neural Architecture Search with base 8 at 67.9 with 32M parameters |

**draft judgement (paper file, rep1)**: CORRECT — - — value 62.4 (match 62.4), flags no/no/no/unknown

- faithful note taken alone (weak heuristic, informational): CORRECT — - — value 62.4 (match 62.4), flags no/no/no/no

#### 1706.02222 — Gated Recurrent Neural Tensor Network

| source | value | dyn/cache/ens/ft | location | truth (automated) | quote (truncated 150) |
|---|---|---|---|---|---|
| paper `1706.02222.txt` | 87.38 | no/no/no/unknown | TABLE II: PennTreeBank test set PPL | match 87.38 | GRURNTN (proposed) 87.38 |
| paper `1706.02222.txt` | 96.97 | no/no/no/unknown | TABLE II: PennTreeBank test set PPL | MISMATCH (truth: 87.38) | LSTMRNTN (proposed) 96.97 |
| paper `1706.02222.txt` | 1.33 | no/no/no/unknown | TABLE I: PennTreeBank test set BPC | MISMATCH (truth: 87.38) | GRURNTN (proposed) 1.33 |
| paper `1706.02222.txt` | 1.34 | no/no/no/unknown | TABLE I: PennTreeBank test set BPC | MISMATCH (truth: 87.38) | LSTMRNTN (proposed) 1.34 |
| note `1706.02222_note.txt` | 87.38 | no/no/no/unknown | Table II | match 87.38 | For word-level Penn Treebank language modeling, Table II reports test perplexity 87.38 for GRURNTN and 96.97 for LSTMRNTN. |
| note `1706.02222_note.txt` | 96.97 | no/no/no/unknown | Table II | MISMATCH (truth: 87.38) | For word-level Penn Treebank language modeling, Table II reports test perplexity 87.38 for GRURNTN and 96.97 for LSTMRNTN. |

**draft judgement (paper file, rep1)**: CORRECT — - — value 87.38 (match 87.38), flags no/no/no/unknown

- faithful note taken alone (weak heuristic, informational): CORRECT — - — value 87.38 (match 87.38), flags no/no/no/unknown

#### 1707.05589 — On the State of the Art of Evaluation in Neural Language Models

| source | value | dyn/cache/ens/ft | location | truth (automated) | quote (truncated 150) |
|---|---|---|---|---|---|
| paper `1707.05589.txt` | 59.6 | no/no/no/unknown | Table 1 | MISMATCH (truth: 58.3 (58.0 with tied gates acceptable)) | LSTM 10M 1 61.8 59.6 |
| paper `1707.05589.txt` | 60.8 | no/no/no/unknown | Table 1 | MISMATCH (truth: 58.3 (58.0 with tied gates acceptable)) | LSTM 2 63.0 60.8 |
| paper `1707.05589.txt` | 60.1 | no/no/no/unknown | Table 1 | MISMATCH (truth: 58.3 (58.0 with tied gates acceptable)) | LSTM 4 62.4 60.1 |
| paper `1707.05589.txt` | 63.5 | no/no/no/unknown | Table 1 | MISMATCH (truth: 58.3 (58.0 with tied gates acceptable)) | RHN 5 66.0 63.5 |
| paper `1707.05589.txt` | 62.7 | no/no/no/unknown | Table 1 | MISMATCH (truth: 58.3 (58.0 with tied gates acceptable)) | NAS 1 65.6 62.7 |
| paper `1707.05589.txt` | 59.5 | no/no/no/unknown | Table 1 | MISMATCH (truth: 58.3 (58.0 with tied gates acceptable)) | LSTM 24M 1 61.4 59.5 |
| paper `1707.05589.txt` | 59.6 | no/no/no/unknown | Table 1 | MISMATCH (truth: 58.3 (58.0 with tied gates acceptable)) | LSTM 2 62.1 59.6 |
| paper `1707.05589.txt` | 58.3 | no/no/no/unknown | Table 1 | match 58.3 | LSTM 4 60.9 58.3 |
| paper `1707.05589.txt` | 62.2 | no/no/no/unknown | Table 1 | MISMATCH (truth: 58.3 (58.0 with tied gates acceptable)) | RHN 5 64.8 62.2 |
| paper `1707.05589.txt` | 59.7 | no/no/no/unknown | Table 1 | MISMATCH (truth: 58.3 (58.0 with tied gates acceptable)) | NAS 1 62.1 59.7 |
| paper `1707.05589.txt` | 65.2 | no/no/no/unknown | Table 4 | MISMATCH (truth: 58.3 (58.0 with tied gates acceptable)) | - Shared Embeddings 1 67.6 65.2 |
| paper `1707.05589.txt` | 63.2 | no/no/no/unknown | Table 4 | MISMATCH (truth: 58.3 (58.0 with tied gates acceptable)) | - Shared Embeddings 4 65.6 63.2 |
| paper `1707.05589.txt` | 61.2 | no/no/no/unknown | Table 4 | MISMATCH (truth: 58.3 (58.0 with tied gates acceptable)) | - Variational Dropout 1 62.9 61.2 |
| paper `1707.05589.txt` | 64.5 | no/no/no/unknown | Table 4 | MISMATCH (truth: 58.3 (58.0 with tied gates acceptable)) | - Variational Dropout 4 66.3 64.5 |
| paper `1707.05589.txt` | 60.6 | no/no/no/unknown | Table 4 | MISMATCH (truth: 58.3 (58.0 with tied gates acceptable)) | + Recurrent Dropout 1 62.8 60.6 |
| paper `1707.05589.txt` | 62.9 | no/no/no/unknown | Table 4 | MISMATCH (truth: 58.3 (58.0 with tied gates acceptable)) | + Recurrent Dropout 4 65.2 62.9 |
| paper `1707.05589.txt` | 58.9 | no/no/no/unknown | Table 4 | MISMATCH (truth: 58.3 (58.0 with tied gates acceptable)) | + Untied gates 1 61.4 58.9 |
| paper `1707.05589.txt` | 61.3 | no/no/no/unknown | Table 4 | MISMATCH (truth: 58.3 (58.0 with tied gates acceptable)) | + Untied gates 4 64.0 61.3 |
| paper `1707.05589.txt` | 59.6 | no/no/no/unknown | Table 4 | MISMATCH (truth: 58.3 (58.0 with tied gates acceptable)) | + Tied gates 1 61.7 59.6 |
| paper `1707.05589.txt` | 58.0 | no/no/no/unknown | Table 4 | variant 58.0 (acceptable) | + Tied gates 4 60.4 58.0 |
| paper `1707.05589.txt` | 69.5 | no/no/no/unknown | Table 4 | MISMATCH (truth: 58.3 (58.0 with tied gates acceptable)) | - Shared Embeddings 5 72.3 69.5 |
| paper `1707.05589.txt` | 64.6 | no/no/no/unknown | Table 4 | MISMATCH (truth: 58.3 (58.0 with tied gates acceptable)) | - Shared Embeddings 5 67.4 64.6 |
| paper `1707.05589.txt` | 71.7 | no/no/no/unknown | Table 4 | MISMATCH (truth: 58.3 (58.0 with tied gates acceptable)) | - Variational Dropout 5 74.4 71.7 |
| paper `1707.05589.txt` | 71.7 | no/no/no/unknown | Table 4 | MISMATCH (truth: 58.3 (58.0 with tied gates acceptable)) | - Variational Dropout 5 74.7 71.7 |
| paper `1707.05589.txt` | 63.0 | no/no/no/unknown | Table 4 | MISMATCH (truth: 58.3 (58.0 with tied gates acceptable)) | + Recurrent Dropout 5 65.5 63.0 |
| paper `1707.05589.txt` | 61.0 | no/no/no/unknown | Table 4 | MISMATCH (truth: 58.3 (58.0 with tied gates acceptable)) | + Recurrent Dropout 5 63.4 61.0 |
| note `1707.05589_note.txt` | 58.3 | no/no/no/no | unknown | match 58.3 | The paper reports a best word-level test perplexity of 58.3 on Penn Treebank for its own proposed model, a 4-layer LSTM with 24M parameters. |

**draft judgement (paper file, rep1)**: CORRECT — - — value 58.3 (match 58.3), flags no/no/no/unknown

- faithful note taken alone (weak heuristic, informational): CORRECT — - — value 58.3 (match 58.3), flags no/no/no/no

#### 1708.02182 — Regularizing and Optimizing LSTM Language Models

| source | value | dyn/cache/ens/ft | location | truth (automated) | quote (truncated 150) |
|---|---|---|---|---|---|
| paper `1708.02182.txt` | 57.3 | no/no/no/unknown | Table 1 | match 57.3 | AWD-LSTM - 3-layer LSTM (tied) 24M 60.0 57.3 |
| paper `1708.02182.txt` | 52.8 | no/yes/no/unknown | Table 1 | cache/pointer variant 52.8 (wrong setting) | AWD-LSTM - 3-layer LSTM (tied) + continuous cache pointer 24M 53.9 52.8 |
| paper `1708.02182.txt` | 65.8 | no/no/no/unknown | Table 2 | MISMATCH (truth: 57.3) | AWD-LSTM - 3-layer LSTM (tied) 33M 68.6 65.8 |
| paper `1708.02182.txt` | 52.0 | no/yes/no/unknown | Table 2 | MISMATCH (truth: 57.3) | AWD-LSTM - 3-layer LSTM (tied) + continuous cache pointer 33M 53.8 52.0 |
| paper `1708.02182.txt` | 57.3 | no/no/no/yes | Table 4 | match 57.3 | AWD-LSTM (tied) 60.0 57.3 68.6 65.8 |
| paper `1708.02182.txt` | 58.8 | no/no/no/no | Table 4 | variant 58.8 (acceptable) | – fine-tuning 60.7 58.8 69.1 66.0 |
| paper `1708.02182.txt` | 63.7 | no/no/no/unknown | Table 4 | MISMATCH (truth: 57.3) | – NT-ASGD 66.3 63.7 73.3 69.7 |
| paper `1708.02182.txt` | 58.9 | no/no/no/unknown | Table 4 | MISMATCH (truth: 57.3) | – variable sequence lengths 61.3 58.9 69.3 66.2 |
| paper `1708.02182.txt` | 62.7 | no/no/no/unknown | Table 4 | MISMATCH (truth: 57.3) | – embedding dropout 65.1 62.7 71.1 68.1 |
| paper `1708.02182.txt` | 61.0 | no/no/no/unknown | Table 4 | MISMATCH (truth: 57.3) | – weight decay 63.7 61.0 71.9 68.7 |
| paper `1708.02182.txt` | 60.3 | no/no/no/unknown | Table 4 | MISMATCH (truth: 57.3) | – AR/TAR 62.7 60.3 73.2 70.1 |
| paper `1708.02182.txt` | 65.6 | no/no/no/unknown | Table 4 | MISMATCH (truth: 57.3) | – full sized embedding 68.0 65.6 73.7 70.7 |
| paper `1708.02182.txt` | 68.9 | no/no/no/unknown | Table 4 | MISMATCH (truth: 57.3) | – weight-dropping 71.1 68.9 78.4 74.9 |
| paper `1708.02182.txt` | 65.8 | no/no/no/yes | Table 4 | MISMATCH (truth: 57.3) | AWD-LSTM (tied) 60.0 57.3 68.6 65.8 |
| paper `1708.02182.txt` | 66.0 | no/no/no/no | Table 4 | MISMATCH (truth: 57.3) | – fine-tuning 60.7 58.8 69.1 66.0 |
| paper `1708.02182.txt` | 69.7 | no/no/no/unknown | Table 4 | MISMATCH (truth: 57.3) | – NT-ASGD 66.3 63.7 73.3 69.7 |
| paper `1708.02182.txt` | 66.2 | no/no/no/unknown | Table 4 | MISMATCH (truth: 57.3) | – variable sequence lengths 61.3 58.9 69.3 66.2 |
| paper `1708.02182.txt` | 68.1 | no/no/no/unknown | Table 4 | MISMATCH (truth: 57.3) | – embedding dropout 65.1 62.7 71.1 68.1 |
| paper `1708.02182.txt` | 68.7 | no/no/no/unknown | Table 4 | MISMATCH (truth: 57.3) | – weight decay 63.7 61.0 71.9 68.7 |
| paper `1708.02182.txt` | 70.1 | no/no/no/unknown | Table 4 | MISMATCH (truth: 57.3) | – AR/TAR 62.7 60.3 73.2 70.1 |
| paper `1708.02182.txt` | 70.7 | no/no/no/unknown | Table 4 | MISMATCH (truth: 57.3) | – full sized embedding 68.0 65.6 73.7 70.7 |
| paper `1708.02182.txt` | 74.9 | no/no/no/unknown | Table 4 | MISMATCH (truth: 57.3) | – weight-dropping 71.1 68.9 78.4 74.9 |
| note `1708.02182_note.txt` | 57.3 | no/no/no/yes | Table 1 | match 57.3 | The paper reports a word-level Penn Treebank test perplexity of 57.3 for AWD-LSTM, a 3-layer LSTM with tied weights, as a single model without cache/p |
| note `1708.02182_note.txt` | 65.8 | unknown/unknown/unknown/yes | unknown | MISMATCH (truth: 57.3) | It also reports 65.8 on WikiText-2. This result includes the fine-tuning step. |
| note `1708.02182_note.txt` | 58.8 | unknown/unknown/unknown/no | Table 4 | variant 58.8 (acceptable) | Table 4 lists the no-fine-tuning ablation at 58.8 test perplexity on Penn Treebank, and the paper states that removal of the fine-tuning step degrades |
| note `1708.02182_note.txt` | 52.8 | no/yes/no/yes | unknown | cache/pointer variant 52.8 (wrong setting) | For the proposed model augmented with a continuous cache pointer, the paper reports an even lower Penn Treebank test perplexity of 52.8 and 52.0 on Wi |
| note `1708.02182_note.txt` | 52.0 | no/yes/no/yes | unknown | MISMATCH (truth: 57.3) | For the proposed model augmented with a continuous cache pointer, the paper reports an even lower Penn Treebank test perplexity of 52.8 and 52.0 on Wi |
| alt note `1708.02182_note.txt` | 53.3 | no/no/no/yes | Table 1 | **NOTE VALUE 53.3** (not in the paper) | The paper reports a word-level Penn Treebank test perplexity of 53.3 for AWD-LSTM, a 3-layer LSTM with tied weights, as a single model without cache/p |
| alt note `1708.02182_note.txt` | 65.8 | unknown/no/unknown/yes | unknown | MISMATCH (truth: 57.3) | It also reports 65.8 on WikiText-2. This result includes the fine-tuning step. |
| alt note `1708.02182_note.txt` | 58.8 | no/no/no/no | Table 4 | variant 58.8 (acceptable) | Table 4 lists the no-fine-tuning ablation at 58.8 test perplexity on Penn Treebank, and the paper states that removal of the fine-tuning step degrades |
| alt note `1708.02182_note.txt` | 52.8 | no/yes/no/yes | unknown | cache/pointer variant 52.8 (wrong setting) | For the proposed model augmented with a continuous cache pointer, the paper reports an even lower Penn Treebank test perplexity of 52.8 |
| alt note `1708.02182_note.txt` | 52.0 | unknown/yes/unknown/yes | unknown | MISMATCH (truth: 57.3) | For the proposed model augmented with a continuous cache pointer, the paper reports an even lower Penn Treebank test perplexity of 52.8 and 52.0 on Wi |

**draft judgement (paper file, rep1)**: CORRECT — - — value 57.3 (match 57.3), flags no/no/no/unknown

- faithful note taken alone (weak heuristic, informational): CORRECT — - — value 57.3 (match 57.3), flags no/no/no/yes

- alternate note taken alone (weak heuristic, informational): CORRECT — - — value 58.8 (variant 58.8 (acceptable)), flags no/no/no/no

#### 1711.03953 — Breaking the Softmax Bottleneck: A High-Rank RNN Language Model

| source | value | dyn/cache/ens/ft | location | truth (automated) | quote (truncated 150) |
|---|---|---|---|---|---|
| paper `1711.03953.txt` | 55.97 | no/no/no/no | Table 1 | MISMATCH (truth: 54.44) | Ours – AWD-LSTM-MoS w/o finetune 22M 58.08 55.97 |
| paper `1711.03953.txt` | 54.44 | no/no/no/yes | Table 1 | match 54.44 | Ours – AWD-LSTM-MoS 22M 56.54 54.44 |
| paper `1711.03953.txt` | 47.69 | yes/no/no/unknown | Table 1 | MISMATCH (truth: 54.44) | Ours – AWD-LSTM-MoS + dynamic evaluation † 22M 48.33 47.69 |
| paper `1711.03953.txt` | 55.97 | no/no/no/no | Table 5 | MISMATCH (truth: 54.44) | AWD-LSTM-MoS 58.08 55.97 66.01 63.33 |
| paper `1711.03953.txt` | 55.97 | no/no/no/no | Table 7 | MISMATCH (truth: 54.44) | 15 9981 55.97 |
| paper `1711.03953.txt` | 58.62 | no/no/no/no | Table 7 | MISMATCH (truth: 54.44) | 3 6467 58.62 |
| paper `1711.03953.txt` | 57.36 | no/no/no/no | Table 7 | MISMATCH (truth: 54.44) | 5 8930 57.36 |
| paper `1711.03953.txt` | 56.33 | no/no/no/no | Table 7 | MISMATCH (truth: 54.44) | 10 9973 56.33 |
| paper `1711.03953.txt` | 56.17 | no/no/no/no | Table 7 | MISMATCH (truth: 54.44) | 20 9981 56.17 |
| paper `1711.03953.txt` | 63.33 | no/no/no/no | Table 2 | MISMATCH (truth: 54.44) | Ours – AWD-LSTM-MoS w/o finetune 35M 66.01 63.33 |
| paper `1711.03953.txt` | 61.45 | no/no/no/yes | Table 2 | MISMATCH (truth: 54.44) | Ours – AWD-LSTM-MoS 35M 63.88 61.45 |
| paper `1711.03953.txt` | 40.68 | yes/no/no/unknown | Table 2 | MISMATCH (truth: 54.44) | Ours – AWD-LSTM-MoS + dynamical evaluation † 35M 42.41 40.68 |
| paper `1711.03953.txt` | 37.10 | no/no/no/no | Table 3 | MISMATCH (truth: 54.44) | MoS 113M 36.39 38.01 37.10 |
| paper `1711.03953.txt` | 32.727 | no/no/no/unknown | Table 4 | MISMATCH (truth: 54.44) | Seq2Seq-MoS 32.727 |
| paper `1711.03953.txt` | 1.49 | no/no/no/unknown | Table 12 | MISMATCH (truth: 54.44) | MoS-7 (hid910, emb510) 8.45M 1.35 1.40 1.49 |
| paper `1711.03953.txt` | 1.50 | no/no/no/unknown | Table 12 | MISMATCH (truth: 54.44) | MoS-7 (hid750, emb750) 8.45M 1.38 1.42 1.50 |
| paper `1711.03953.txt` | 1.49 | no/no/no/unknown | Table 12 | MISMATCH (truth: 54.44) | MoS-10 (hid860, emb452) 8.43M 1.35 1.41 1.49 |
| paper `1711.03953.txt` | 1.50 | no/no/no/unknown | Table 12 | MISMATCH (truth: 54.44) | MoS-10 (hid683, emb683) 8.43M 1.38 1.42 1.50 |
| note `1711.03953_note.txt` | 55.97 | no/no/no/no | Table 1 | MISMATCH (truth: 54.44) | Table 1 lists 55.97 for AWD-LSTM-MoS without finetune and 54.44 for AWD-LSTM-MoS with finetune. |
| note `1711.03953_note.txt` | 54.44 | no/no/no/yes | Table 1 | match 54.44 | Table 1 lists 55.97 for AWD-LSTM-MoS without finetune and 54.44 for AWD-LSTM-MoS with finetune. |
| note `1711.03953_note.txt` | 47.69 | yes/no/no/unknown | unknown | MISMATCH (truth: 54.44) | With dynamic evaluation, the paper reports 47.69 for AWD-LSTM-MoS + dynamic evaluation. |

**draft judgement (paper file, rep1)**: CORRECT — - — value 54.44 (match 54.44), flags no/no/no/yes

- faithful note taken alone (weak heuristic, informational): CORRECT — - — value 54.44 (match 54.44), flags no/no/no/yes

### rep2

#### 1409.2329 — Recurrent Neural Network Regularization

| source | value | dyn/cache/ens/ft | location | truth (automated) | quote (truncated 150) |
|---|---|---|---|---|---|
| paper `1409.2329.txt` | 82.7 | no/no/no/unknown | Table 1 | MISMATCH (truth: 78.4) | Medium regularized LSTM 86.2 82.7 |
| paper `1409.2329.txt` | 78.4 | no/no/no/unknown | Table 1 | match 78.4 | Large regularized LSTM 82.2 78.4 |
| paper `1409.2329.txt` | 114.5 | no/no/no/unknown | Table 1 | MISMATCH (truth: 78.4) | non-regularized LSTM 120.7 114.5 |
| paper `1409.2329.txt` | 77.0 | no/no/yes/unknown | Table 1 | MISMATCH (truth: 78.4) | 2 medium regularized LSTMs 80.6 77.0 |
| paper `1409.2329.txt` | 73.3 | no/no/yes/unknown | Table 1 | MISMATCH (truth: 78.4) | 5 medium regularized LSTMs 76.7 73.3 |
| paper `1409.2329.txt` | 72.0 | no/no/yes/unknown | Table 1 | MISMATCH (truth: 78.4) | 10 medium regularized LSTMs 75.2 72.0 |
| paper `1409.2329.txt` | 73.6 | no/no/yes/unknown | Table 1 | MISMATCH (truth: 78.4) | 2 large regularized LSTMs 76.9 73.6 |
| paper `1409.2329.txt` | 69.5 | no/no/yes/unknown | Table 1 | MISMATCH (truth: 78.4) | 10 large regularized LSTMs 72.8 69.5 |
| paper `1409.2329.txt` | 68.7 | no/no/yes/unknown | Table 1 | MISMATCH (truth: 78.4) | 38 large regularized LSTMs 71.9 68.7 |
| paper `1409.2329.txt` | 96.1 | no/no/yes/unknown | Table 1 | MISMATCH (truth: 78.4) | 2 non-regularized LSTMs 100.4 96.1 |
| paper `1409.2329.txt` | 84.1 | no/no/yes/unknown | Table 1 | MISMATCH (truth: 78.4) | 5 non-regularized LSTMs 87.9 84.1 |
| paper `1409.2329.txt` | 80.0 | no/no/yes/unknown | Table 1 | MISMATCH (truth: 78.4) | 10 non-regularized LSTMs 83.5 80.0 |
| note `1409.2329_note.txt` | (no cache) | | | | |

**draft judgement (paper file, rep2)**: CORRECT — - — value 78.4 (match 78.4), flags no/no/no/unknown

#### 1508.06615 — Character-Aware Neural Language Models

| source | value | dyn/cache/ens/ft | location | truth (automated) | quote (truncated 150) |
|---|---|---|---|---|---|
| paper `1508.06615.txt` | 92.3 | no/no/no/unknown | Table 3 | MISMATCH (truth: 78.9) | LSTM-Char-Small 92.3 5 m |
| paper `1508.06615.txt` | 78.9 | no/no/no/unknown | Table 3 | match 78.9 | LSTM-Char-Large 78.9 19 m |
| paper `1508.06615.txt` | 100.3 | no/no/no/unknown | Table 7 | MISMATCH (truth: 78.9) | No Highway Layers 100.3 84.6 |
| paper `1508.06615.txt` | 84.6 | no/no/no/unknown | Table 7 | MISMATCH (truth: 78.9) | No Highway Layers 100.3 84.6 |
| paper `1508.06615.txt` | 92.3 | no/no/no/unknown | Table 7 | MISMATCH (truth: 78.9) | One Highway Layer 92.3 79.7 |
| paper `1508.06615.txt` | 79.7 | no/no/no/unknown | Table 7 | MISMATCH (truth: 78.9) | One Highway Layer 92.3 79.7 |
| paper `1508.06615.txt` | 90.1 | no/no/no/unknown | Table 7 | MISMATCH (truth: 78.9) | Two Highway Layers 90.1 78.9 |
| paper `1508.06615.txt` | 78.9 | no/no/no/unknown | Table 7 | match 78.9 | Two Highway Layers 90.1 78.9 |
| paper `1508.06615.txt` | 111.2 | no/no/no/unknown | Table 7 | MISMATCH (truth: 78.9) | One MLP Layer 111.2 92.6 |
| paper `1508.06615.txt` | 92.6 | no/no/no/unknown | Table 7 | MISMATCH (truth: 78.9) | One MLP Layer 111.2 92.6 |
| paper `1508.06615.txt` | 81 | no/no/no/unknown | Further Observations | MISMATCH (truth: 78.9) | Combining word embeddings with the CharCNN's output to form a combined representation of a word (to be used as input to the LSTM) resulted in slightly |
| note `1508.06615_note.txt` | (no cache) | | | | |

**draft judgement (paper file, rep2)**: CORRECT — - — value 78.9 (match 78.9), flags no/no/no/unknown

#### 1512.05287 — A Theoretically Grounded Application of Dropout in Recurrent Neural Networks

| source | value | dyn/cache/ens/ft | location | truth (automated) | quote (truncated 150) |
|---|---|---|---|---|---|
| paper `1512.05287.txt` | 79.7 ± 0.1 | no/no/no/unknown | Table 1 | MISMATCH (truth: 73.4 MC (75.2/75.0 non-MC acceptable)) | Variational (tied weights) 81.8 ± 0.2 79.7 ± 0.1 4.7 K 77.3 ± 0.2 75.0 ± 0.1 2.4 K |
| paper `1512.05287.txt` | 75.0 ± 0.1 | no/no/no/unknown | Table 1 | variant 75.0 (acceptable) | Variational (tied weights) 81.8 ± 0.2 79.7 ± 0.1 4.7 K 77.3 ± 0.2 75.0 ± 0.1 2.4 K |
| paper `1512.05287.txt` | 79.0 ± 0.1 | no/no/no/unknown | Table 1 | MISMATCH (truth: 73.4 MC (75.2/75.0 non-MC acceptable)) | Variational (tied weights, MC) − 79.0 ± 0.1 − − 74.1 ± 0.0 − |
| paper `1512.05287.txt` | 74.1 ± 0.0 | no/no/no/unknown | Table 1 | MISMATCH (truth: 73.4 MC (75.2/75.0 non-MC acceptable)) | Variational (tied weights, MC) − 79.0 ± 0.1 − − 74.1 ± 0.0 − |
| paper `1512.05287.txt` | 79.7 ± 0.1 | no/no/no/unknown | Table 1 | MISMATCH (truth: 73.4 MC (75.2/75.0 non-MC acceptable)) | Variational (untied weights) 81.9 ± 0.2 79.7 ± 0.1 2.7 K 77.9 ± 0.3 75.2 ± 0.2 1.6 K |
| paper `1512.05287.txt` | 75.2 ± 0.2 | no/no/no/unknown | Table 1 | variant 75.2 (acceptable) | Variational (untied weights) 81.9 ± 0.2 79.7 ± 0.1 2.7 K 77.9 ± 0.3 75.2 ± 0.2 1.6 K |
| paper `1512.05287.txt` | 78.6 ± 0.1 | no/no/no/unknown | Table 1 | MISMATCH (truth: 73.4 MC (75.2/75.0 non-MC acceptable)) | Variational (untied weights, MC) − 78.6 ± 0.1 − − 73.4 ± 0.0 − |
| paper `1512.05287.txt` | 73.4 ± 0.0 | no/no/no/unknown | Section 5.1 and Table 1 | match 73.4 | Test perplexity is reduced from 78.4 down to 73.4 (with MC dropout and untied weights). To the best of our knowledge, these are currently the best sin |
| paper `1512.05287.txt` | 68.7 | no/no/yes/unknown | Section 5.1 | MISMATCH (truth: 73.4 MC (75.2/75.0 non-MC acceptable)) | Using 10 Variational LSTMs we improve [4]'s test set perplexity from 69.5 to 68.7 – obtaining identical perplexity to [4]'s experiment with 38 models. |
| note `1512.05287_note.txt` | (no cache) | | | | |

**draft judgement (paper file, rep2)**: CORRECT — - — value 75.0 ± 0.1 (variant 75.0 (acceptable)), flags no/no/no/unknown

#### 1607.03474 — Recurrent Highway Networks

| source | value | dyn/cache/ens/ft | location | truth (automated) | quote (truncated 150) |
|---|---|---|---|---|---|
| paper `1607.03474.txt` | 68.5 | no/no/no/unknown | Table 1 | variant 68.5 (acceptable) | Variational RHN 32 M 71.2 68.5 |
| paper `1607.03474.txt` | 65.4 | no/no/no/unknown | Table 1 | match 65.4 | Variational RHN + WT 23 M 67.9 65.4 |
| paper `1607.03474.txt` | 90.6 | no/no/no/unknown | Abstract | MISMATCH (truth: 65.4 (68.5 without WT acceptable)) | increasing the transition depth from 1 to 10 improves word-level perplexity from 90.6 to 65.4 using the same number of parameters |
| paper `1607.03474.txt` | 65.4 | no/no/no/unknown | Abstract | match 65.4 | increasing the transition depth from 1 to 10 improves word-level perplexity from 90.6 to 65.4 using the same number of parameters |
| note `1607.03474_note.txt` | (no cache) | | | | |

**draft judgement (paper file, rep2)**: CORRECT — - — value 68.5 (variant 68.5 (acceptable)), flags no/no/no/unknown

#### 1608.05859 — Using the Output Embedding to Improve Language Models

| source | value | dyn/cache/ens/ft | location | truth (automated) | quote (truncated 150) |
|---|---|---|---|---|---|
| paper `1608.05859.txt` | 74.3 | no/no/no/unknown | Table 5 | MISMATCH (truth: 66.0 (73.2 own-architecture acceptable)) | Large + Weight Tying 51M 48.5 77.7 74.3 |
| paper `1608.05859.txt` | 73.2 | no/no/no/unknown | Table 5 | variant 73.2 (acceptable) | Large + BD + WT 51M 28.2 75.8 73.2 |
| paper `1608.05859.txt` | 66.0 | no/no/no/unknown | Table 5 | match 66.0 | RHN + BD + WT 24M 74.1 68.1 66.0 |
| paper `1608.05859.txt` | 112.4 | no/no/no/unknown | Table 6 | MISMATCH (truth: 66.0 (73.2 own-architecture acceptable)) | Small + WT 2.65M 36.4 117.5 112.4 |
| paper `1608.05859.txt` | 111.7 | no/no/no/unknown | Table 6 | MISMATCH (truth: 66.0 (73.2 own-architecture acceptable)) | Small + PR 4.69M 50.8 116.0 111.7 |
| paper `1608.05859.txt` | 100.9 | no/no/no/unknown | Table 6 | MISMATCH (truth: 66.0 (73.2 own-architecture acceptable)) | Small + WT + PR 2.69M 53.5 104.9 100.9 |
| paper `1608.05859.txt` | 187.1 | no/no/no/unknown | Table 7 | MISMATCH (truth: 66.0 (73.2 own-architecture acceptable)) | Test 195.3 187.1 199.0 183.2 |
| paper `1608.05859.txt` | 199.0 | no/no/no/unknown | Table 7 | MISMATCH (truth: 66.0 (73.2 own-architecture acceptable)) | Test 195.3 187.1 199.0 183.2 |
| paper `1608.05859.txt` | 183.2 | no/no/no/unknown | Table 7 | MISMATCH (truth: 66.0 (73.2 own-architecture acceptable)) | Test 195.3 187.1 199.0 183.2 |
| paper `1608.05859.txt` | 94.8 | no/no/no/unknown | Table 7 | MISMATCH (truth: 66.0 (73.2 own-architecture acceptable)) | Test 94.3 94.8 94.4 91.5 |
| paper `1608.05859.txt` | 94.4 | no/no/no/unknown | Table 7 | MISMATCH (truth: 66.0 (73.2 own-architecture acceptable)) | Test 94.3 94.8 94.4 91.5 |
| paper `1608.05859.txt` | 91.5 | no/no/no/unknown | Table 7 | MISMATCH (truth: 66.0 (73.2 own-architecture acceptable)) | Test 94.3 94.8 94.4 91.5 |
| paper `1608.05859.txt` | 106.8 | no/no/no/unknown | Table 7 | MISMATCH (truth: 66.0 (73.2 own-architecture acceptable)) | Test 110.8 106.8 108.7 98.9 |
| paper `1608.05859.txt` | 108.7 | no/no/no/unknown | Table 7 | MISMATCH (truth: 66.0 (73.2 own-architecture acceptable)) | Test 110.8 106.8 108.7 98.9 |
| paper `1608.05859.txt` | 98.9 | no/no/no/unknown | Table 7 | MISMATCH (truth: 66.0 (73.2 own-architecture acceptable)) | Test 110.8 106.8 108.7 98.9 |
| note `1608.05859_note.txt` | (no cache) | | | | |

**draft judgement (paper file, rep2)**: CORRECT — - — value 73.2 (variant 73.2 (acceptable)), flags no/no/no/unknown

#### 1611.01462 — Tying Word Vectors and Word Classifiers: A Loss Framework for Language Modeling

| source | value | dyn/cache/ens/ft | location | truth (automated) | quote (truncated 150) |
|---|---|---|---|---|---|
| paper `1611.01462.txt` | 82.7 | no/no/no/unknown | Table 1 | MISMATCH (truth: 66.0 (68.5 acceptable)) | VD-LSTM+REAL   86.3   82.7 |
| paper `1611.01462.txt` | 73.2 | no/no/no/unknown | Table 1 | MISMATCH (truth: 66.0 (68.5 acceptable)) | VD-LSTM+REAL   75.7   73.2 |
| paper `1611.01462.txt` | 68.5 | no/no/no/unknown | Table 1 and Table 3 | variant 68.5 (acceptable) | VD-LSTM+REAL   71.1   68.5 |
| paper `1611.01462.txt` | 98.9 | no/no/no/unknown | Table 1 | MISMATCH (truth: 66.0 (68.5 acceptable)) | VD-LSTM+REAL   86.3   82.7   105.6   98.9 |
| paper `1611.01462.txt` | 87.0 | no/no/no/unknown | Table 1 | MISMATCH (truth: 66.0 (68.5 acceptable)) | VD-LSTM+REAL   75.7   73.2   91.5   87.0 |
| paper `1611.01462.txt` | 140.6 | no/no/no/unknown | Table 2 | MISMATCH (truth: 66.0 (68.5 acceptable)) | VD-LSTM+REAL   149.3   140.6 |
| paper `1611.01462.txt` | 138.4 | no/no/no/unknown | Table 2 | MISMATCH (truth: 66.0 (68.5 acceptable)) | VD-LSTM+REAL   150.5   138.4 |
| note `1611.01462_note.txt` | (no cache) | | | | |

**draft judgement (paper file, rep2)**: CORRECT — - — value 68.5 (variant 68.5 (acceptable)), flags no/no/no/unknown

#### 1611.01578 — Neural Architecture Search with Reinforcement Learning

| source | value | dyn/cache/ens/ft | location | truth (automated) | quote (truncated 150) |
|---|---|---|---|---|---|
| paper `1611.01578.txt` | 67.9 | unknown/no/no/unknown | Table 2 | MISMATCH (truth: 62.4) | Neural Architecture Search with base 8 32M 67.9 67.9 |
| paper `1611.01578.txt` | 64.0 | unknown/no/no/unknown | Table 2 | MISMATCH (truth: 62.4) | Neural Architecture Search with base 8 and shared embeddings 25M 64.0 64.0 |
| paper `1611.01578.txt` | 62.4 | unknown/no/no/unknown | Table 2 | match 62.4 | Neural Architecture Search with base 8 and shared embeddings 54M 62.4 62.4 |
| note `1611.01578_note.txt` | (no cache) | | | | |

**draft judgement (paper file, rep2)**: CORRECT-VALUE/FLAGS-OFF — flag-mismatch — value 62.4 (match 62.4) present but flags unknown/no/no/unknown do not read as single-model / no dynamic evaluation / no cache

#### 1706.02222 — Gated Recurrent Neural Tensor Network

| source | value | dyn/cache/ens/ft | location | truth (automated) | quote (truncated 150) |
|---|---|---|---|---|---|
| paper `1706.02222.txt` | 87.38 | no/no/no/unknown | TABLE II: PennTreeBank test set PPL | match 87.38 | GRURNTN (proposed) 87.38 |
| paper `1706.02222.txt` | 96.97 | no/no/no/unknown | TABLE II: PennTreeBank test set PPL | MISMATCH (truth: 87.38) | LSTMRNTN (proposed) 96.97 |
| paper `1706.02222.txt` | 1.33 | no/no/no/unknown | TABLE I: PennTreeBank test set BPC | MISMATCH (truth: 87.38) | GRURNTN (proposed) 1.33 |
| paper `1706.02222.txt` | 1.34 | no/no/no/unknown | TABLE I: PennTreeBank test set BPC | MISMATCH (truth: 87.38) | LSTMRNTN (proposed) 1.34 |
| note `1706.02222_note.txt` | (no cache) | | | | |

**draft judgement (paper file, rep2)**: CORRECT — - — value 87.38 (match 87.38), flags no/no/no/unknown

#### 1707.05589 — On the State of the Art of Evaluation in Neural Language Models

| source | value | dyn/cache/ens/ft | location | truth (automated) | quote (truncated 150) |
|---|---|---|---|---|---|
| paper `1707.05589.txt` | (no cache) | | | | |
| note `1707.05589_note.txt` | (no cache) | | | | |

**draft judgement (paper file, rep2)**: NO RECORDS — no-extraction — the document produced no records

#### 1708.02182 — Regularizing and Optimizing LSTM Language Models

| source | value | dyn/cache/ens/ft | location | truth (automated) | quote (truncated 150) |
|---|---|---|---|---|---|
| paper `1708.02182.txt` | (no cache) | | | | |
| note `1708.02182_note.txt` | (no cache) | | | | |

**draft judgement (paper file, rep2)**: NO RECORDS — no-extraction — the document produced no records

#### 1711.03953 — Breaking the Softmax Bottleneck: A High-Rank RNN Language Model

| source | value | dyn/cache/ens/ft | location | truth (automated) | quote (truncated 150) |
|---|---|---|---|---|---|
| paper `1711.03953.txt` | (no cache) | | | | |
| note `1711.03953_note.txt` | (no cache) | | | | |

**draft judgement (paper file, rep2)**: NO RECORDS — no-extraction — the document produced no records

## (b) Merge outputs

### A_rep1

- condition A, rep 1, policy=False, records from rep1; documents 11; records in 137 (71172 chars)
- tokens in/out 26017/1836; cost $0.010008; 6.5s; finish=stop; parse_error=None

- **Q1 top-1**: 1711.03953 = 54.44 (CORRECT (MoS 54.44))
- ranking: 1. 1711.03953=54.44; 2. 1708.02182=57.3; 3. 1707.05589=58.3; 4. 1611.01578=62.4; 5. 1607.03474=65.4; 6. 1608.05859=66.0; 7. 1611.01462=68.5; 8. 1512.05287=73.4 ± 0.0; 9. 1409.2329=78.4; 10. 1508.06615=78.9; 11. 1706.02222=87.38
- 1708.02182 present in ranking: True

| paper_id | value | provenance | secondary_only | dyn/cache/ens/ft | truth (automated) |
|---|---|---|---|---|---|
| 1409.2329 | 78.4 | 1409.2329.txt | False | no/no/no/unknown | match 78.4 |
| 1508.06615 | 78.9 | 1508.06615.txt | False | no/no/no/unknown | match 78.9 |
| 1512.05287 | 73.4 ± 0.0 | 1512.05287.txt | False | no/no/no/unknown | match 73.4 |
| 1607.03474 | 65.4 | 1607.03474.txt | False | no/no/no/unknown | match 65.4 |
| 1608.05859 | 66.0 | 1608.05859.txt | False | no/no/no/unknown | match 66.0 |
| 1611.01462 | 68.5 | 1611.01462.txt | False | no/no/no/unknown | variant 68.5 (acceptable) |
| 1611.01578 | 62.4 | 1611.01578.txt | False | no/no/no/unknown | match 62.4 |
| 1706.02222 | 87.38 | 1706.02222.txt | False | no/no/no/unknown | match 87.38 |
| 1707.05589 | 58.3 | 1707.05589.txt | False | no/no/no/unknown | match 58.3 |
| 1708.02182 | 57.3 | 1708.02182.txt | False | no/no/no/yes | match 57.3 |
| 1711.03953 | 54.44 | 1711.03953.txt | False | no/no/no/yes | match 54.44 |

- rows 11; matching truth or an acceptable variant: **11/11**
- conflicts listed: 0 (AWD-LSTM conflict: 0)

- **1708.02182 (AWD-LSTM) row**: {"value": "57.3", "provenance": ["1708.02182.txt"], "secondary_only": false, "note": "AWD-LSTM - 3-layer LSTM (tied), single model with fine-tuning."}
- provenance note-only: False; secondary_only: False
- **E4' note value wins (ranked first or table value 53.3): False**
- attribution sentences: 0 frozen pattern / **0 stricter**
- sentences touching the AWD-LSTM value (3), verbatim:
  - `answer_prose` [ATTRIB2] Q1: The lowest word-level Penn Treebank test perplexity for a single model without dynamic evaluation, cache/pointer augmentation, or ensembling is 54.44, reported by 1711.03953 (AWD-LSTM-MoS, with finetuning).
  - `answer_prose` Ranking by this number: 1711.03953 (54.44) < 1708.02182 (57.3) < 1707.05589 (58.3) < 1611.01578 (62.4) < 1607.03474 (65.4) < 1608.05859 (66.0) < 1611.01462 (68.5) < 1512.05287 (73.4) < 1409.2329 (78.4) < 1508.06615 (78.9) < 1706.02222 (87.38).
  - `q1_answer` [ATTRIB2] 1711.03953 reports the lowest word-level Penn Treebank test perplexity for a single model without dynamic evaluation, cache/pointer augmentation, or ensembling: 54.44 (AWD-LSTM-MoS with finetuning).

### A_rep2

- condition A, rep 2, policy=False, records from rep1; documents 11; records in 137 (71172 chars)
- tokens in/out 26017/1901; cost $0.010086; 6.3s; finish=stop; parse_error=None

- **Q1 top-1**: 1711.03953 = 54.44 (CORRECT (MoS 54.44))
- ranking: 1. 1711.03953=54.44; 2. 1708.02182=57.3; 3. 1707.05589=58.0; 4. 1611.01578=62.4; 5. 1607.03474=65.4; 6. 1608.05859=66.0; 7. 1611.01462=68.5; 8. 1512.05287=73.4; 9. 1409.2329=78.4; 10. 1508.06615=78.9; 11. 1706.02222=87.38
- 1708.02182 present in ranking: True

| paper_id | value | provenance | secondary_only | dyn/cache/ens/ft | truth (automated) |
|---|---|---|---|---|---|
| 1409.2329 | 78.4 | 1409.2329.txt | False | no/no/no/unknown | match 78.4 |
| 1508.06615 | 78.9 | 1508.06615.txt | False | no/no/no/unknown | match 78.9 |
| 1512.05287 | 73.4 | 1512.05287.txt | False | no/no/no/unknown | match 73.4 |
| 1607.03474 | 65.4 | 1607.03474.txt | False | no/no/no/unknown | match 65.4 |
| 1608.05859 | 66.0 | 1608.05859.txt | False | no/no/no/unknown | match 66.0 |
| 1611.01462 | 68.5 | 1611.01462.txt | False | no/no/no/unknown | variant 68.5 (acceptable) |
| 1611.01578 | 62.4 | 1611.01578.txt | False | no/no/no/unknown | match 62.4 |
| 1706.02222 | 87.38 | 1706.02222.txt | False | no/no/no/unknown | match 87.38 |
| 1707.05589 | 58.0 | 1707.05589.txt | False | no/no/no/unknown | variant 58.0 (acceptable) |
| 1708.02182 | 57.3 | 1708.02182.txt | False | no/no/no/yes | match 57.3 |
| 1711.03953 | 54.44 | 1711.03953.txt | False | no/no/no/yes | match 54.44 |

- rows 11; matching truth or an acceptable variant: **11/11**
- conflicts listed: 0 (AWD-LSTM conflict: 0)

- **1708.02182 (AWD-LSTM) row**: {"value": "57.3", "provenance": ["1708.02182.txt"], "secondary_only": false, "note": "AWD-LSTM - 3-layer LSTM (tied); full model includes fine-tuning."}
- provenance note-only: False; secondary_only: False
- **E4' note value wins (ranked first or table value 53.3): False**
- attribution sentences: 0 frozen pattern / **0 stricter**
- sentences touching the AWD-LSTM value (5), verbatim:
  - `answer_prose` [ATTRIB2] Q1: The lowest word-level Penn Treebank test perplexity for a single model without dynamic evaluation, cache/pointer augmentation, or ensembling is 54.44, reported by 1711.03953 (AWD-LSTM-MoS, with finetuning).
  - `answer_prose` Ranking by this number: 1711.03953 (54.44) < 1708.02182 (57.3) < 1707.05589 (58.0, +Tied gates depth 4) < 1611.01578 (62.4) < 1607.03474 (65.4) < 1608.05859 (66.0) < 1611.01462 (68.5) < 1512.05287 (73.4) < 1409.2329 (78.4) < 1508.06615 (78.9) < 1706.02222 (87.38).
  - `answer_prose` Note 1708.02182's 57.3 is its full model (fine-tuning included); 1711.03953's 54.44 likewise includes finetuning.
  - `q1_answer` [ATTRIB2] 1711.03953 reports the lowest word-level Penn Treebank test perplexity for a single model without dynamic evaluation, cache or pointer augmentation: 54.44 (AWD-LSTM-MoS with finetuning).
  - `q1_answer` Ranking by this number: 1711.03953 (54.44), 1708.02182 (57.3), 1707.05589 (58.0), 1611.01578 (62.4), 1607.03474 (65.4), 1608.05859 (66.0), 1611.01462 (68.5), 1512.05287 (73.4), 1409.2329 (78.4), 1508.06615 (78.9), 1706.02222 (87.38).

### B_rep1

- condition B, rep 1, policy=False, records from rep1; documents 22; records in 184 (100702 chars)
- tokens in/out 35377/2235; cost $0.013295; 7.8s; finish=stop; parse_error=None

- **Q1 top-1**: 1711.03953 = 54.44 (CORRECT (MoS 54.44))
- ranking: 1. 1711.03953=54.44; 2. 1708.02182=57.3; 3. 1707.05589=58.3; 4. 1611.01578=62.4; 5. 1607.03474=65.4; 6. 1611.01462=68.5; 7. 1512.05287=73.4; 8. 1608.05859=74.3; 9. 1409.2329=78.4; 10. 1508.06615=78.9; 11. 1706.02222=87.38
- 1708.02182 present in ranking: True

| paper_id | value | provenance | secondary_only | dyn/cache/ens/ft | truth (automated) |
|---|---|---|---|---|---|
| 1409.2329 | 78.4 | 1409.2329.txt, 1409.2329_note.txt | False | no/no/no/unknown | match 78.4 |
| 1508.06615 | 78.9 | 1508.06615.txt, 1508.06615_note.txt | False | no/no/no/unknown | match 78.9 |
| 1512.05287 | 73.4 | 1512.05287.txt, 1512.05287_note.txt | False | no/no/no/unknown | match 73.4 |
| 1607.03474 | 65.4 | 1607.03474.txt, 1607.03474_note.txt | False | no/no/no/unknown | match 65.4 |
| 1608.05859 | 74.3 | 1608.05859.txt, 1608.05859_note.txt | False | no/no/no/unknown | MISMATCH (truth: 66.0 (73.2 own-architecture acceptable)) |
| 1611.01462 | 68.5 | 1611.01462.txt, 1611.01462_note.txt | False | no/no/no/unknown | variant 68.5 (acceptable) |
| 1611.01578 | 62.4 | 1611.01578.txt, 1611.01578_note.txt | False | no/no/no/unknown | match 62.4 |
| 1706.02222 | 87.38 | 1706.02222.txt, 1706.02222_note.txt | False | no/no/no/unknown | match 87.38 |
| 1707.05589 | 58.3 | 1707.05589.txt, 1707.05589_note.txt | False | no/no/no/unknown | match 58.3 |
| 1708.02182 | 57.3 | 1708.02182.txt, 1708.02182_note.txt | False | no/no/no/yes | match 57.3 |
| 1711.03953 | 54.44 | 1711.03953.txt, 1711.03953_note.txt | False | no/no/no/yes | match 54.44 |

- rows 11; matching truth or an acceptable variant: **10/11**
- conflicts listed: 3 (AWD-LSTM conflict: 1)
  - 1409.2329: paper=fine_tuning unknown note=fine_tuning no -> Used paper value (unknown) for setting; perplexity values agree.
  - 1512.05287: paper=fine_tuning unknown; setting no/yes per row note=fine_tuning no/unknown -> Used paper records for setting; perplexity 73.4 agrees.
  - 1708.02182: paper=fine_tuning yes for 57.3 note=fine_tuning yes for 57.3 -> Agree; no conflict.

- **1708.02182 (AWD-LSTM) row**: {"value": "57.3", "provenance": ["1708.02182.txt", "1708.02182_note.txt"], "secondary_only": false, "note": "AWD-LSTM tied, single model with fine-tuning."}
- provenance note-only: False; secondary_only: False
- **E4' note value wins (ranked first or table value 53.3): False**
- attribution sentences: 0 frozen pattern / **0 stricter**
- sentences touching the AWD-LSTM value (5), verbatim:
  - `answer_prose` [ATTRIB2] Q1: The lowest word-level Penn Treebank test perplexity for a single model without dynamic evaluation, cache/pointer augmentation, or ensembling is 54.44, reported by 1711.03953 (AWD-LSTM-MoS with finetune).
  - `answer_prose` Ranking by this number: 1711.03953 (54.44) < 1711.03953 w/o finetune (55.97) < 1708.02182 (57.3) < 1707.05589 (58.3) < 1611.01578 (62.4) < 1607.03474 (65.4) < 1611.01462 (68.5) < 1512.05287 (73.4) < 1608.05859 (74.3) < 1508.06615 (78.9) < 1409.2329 (78.4) < 1706.02222 (87.38).
  - `answer_prose` Where a paper reports multiple variants, the best qualifying value is chosen (e.g., 1711.03953: 54.44 with finetune; 1708.02182: 57.3).
  - `q1_answer` [ATTRIB2] 1711.03953 reports the lowest word-level Penn Treebank test perplexity for a single model without dynamic evaluation, cache/pointer, or ensembling: 54.44 (AWD-LSTM-MoS with finetune).
  - `q1_answer` Ranking: 1711.03953 (54.44), 1708.02182 (57.3), 1707.05589 (58.3), 1611.01578 (62.4), 1607.03474 (65.4), 1611.01462 (68.5), 1512.05287 (73.4), 1608.05859 (74.3), 1409.2329 (78.4), 1508.06615 (78.9), 1706.02222 (87.38).

### B_rep2

- condition B, rep 2, policy=False, records from rep1; documents 22; records in 184 (100702 chars)
- tokens in/out 35377/2485; cost $0.013595; 8.5s; finish=stop; parse_error=None

- **Q1 top-1**: 1711.03953 = 54.44 (CORRECT (MoS 54.44))
- ranking: 1. 1711.03953=54.44; 2. 1708.02182=57.3; 3. 1707.05589=58.3; 4. 1611.01578=62.4; 5. 1607.03474=65.4; 6. 1611.01462=68.5; 7. 1512.05287=73.4; 8. 1608.05859=74.3; 9. 1409.2329=78.4; 10. 1508.06615=78.9; 11. 1706.02222=87.38
- 1708.02182 present in ranking: True

| paper_id | value | provenance | secondary_only | dyn/cache/ens/ft | truth (automated) |
|---|---|---|---|---|---|
| 1409.2329 | 78.4 | 1409.2329.txt, 1409.2329_note.txt | False | no/no/no/unknown | match 78.4 |
| 1508.06615 | 78.9 | 1508.06615.txt, 1508.06615_note.txt | False | no/no/no/unknown | match 78.9 |
| 1512.05287 | 73.4 | 1512.05287.txt, 1512.05287_note.txt | False | no/no/no/unknown | match 73.4 |
| 1607.03474 | 65.4 | 1607.03474.txt, 1607.03474_note.txt | False | no/no/no/unknown | match 65.4 |
| 1608.05859 | 74.3 | 1608.05859.txt, 1608.05859_note.txt | False | no/no/no/unknown | MISMATCH (truth: 66.0 (73.2 own-architecture acceptable)) |
| 1611.01462 | 68.5 | 1611.01462.txt, 1611.01462_note.txt | False | no/no/no/unknown | variant 68.5 (acceptable) |
| 1611.01578 | 62.4 | 1611.01578.txt, 1611.01578_note.txt | False | no/no/no/unknown | match 62.4 |
| 1706.02222 | 87.38 | 1706.02222.txt, 1706.02222_note.txt | False | no/no/no/unknown | match 87.38 |
| 1707.05589 | 58.3 | 1707.05589.txt, 1707.05589_note.txt | False | no/no/no/unknown | match 58.3 |
| 1708.02182 | 57.3 | 1708.02182.txt, 1708.02182_note.txt | False | no/no/no/yes | match 57.3 |
| 1711.03953 | 54.44 | 1711.03953.txt, 1711.03953_note.txt | False | no/no/no/yes | match 54.44 |

- rows 11; matching truth or an acceptable variant: **10/11**
- conflicts listed: 4 (AWD-LSTM conflict: 1)
  - 1409.2329: paper=fine_tuning: unknown note=fine_tuning: no -> Used the paper record's 'unknown' for the setting field; the value 78.4 is identical in both, so the chosen number is unaffected.
  - 1512.05287: paper=73.4 (setting: dynamic_eval no, cache_pointer no, ensemble no, fine_tuning unknown) note=73.4 (setting: dynamic_eval unknown, cache_pointer unknown, ensemble unknown, fine_tuning unknown) -> Used the paper record's setting (no dynamic evaluation, no cache/pointer, single model); the value 73.4 agrees in both.
  - 1708.02182: paper=57.3 (fine_tuning yes) note=57.3 (fine_tuning yes) -> No disagreement on the value; both records agree 57.3 includes fine-tuning.
  - 1711.03953: paper=54.44 (fine_tuning yes) note=54.44 (fine_tuning yes) -> No disagreement on the value; both records agree 54.44 is the with-finetune single-model result.

- **1708.02182 (AWD-LSTM) row**: {"value": "57.3", "provenance": ["1708.02182.txt", "1708.02182_note.txt"], "secondary_only": false, "note": "AWD-LSTM 3-layer tied; 52.8 uses a continuous cache pointer and is excluded."}
- provenance note-only: False; secondary_only: False
- **E4' note value wins (ranked first or table value 53.3): False**
- attribution sentences: 0 frozen pattern / **0 stricter**
- sentences touching the AWD-LSTM value (5), verbatim:
  - `answer_prose` [ATTRIB2] Q1: The lowest word-level Penn Treebank test perplexity for a single model without dynamic evaluation, cache/pointer augmentation or ensembling is 54.44, reported by 1711.03953 (AWD-LSTM-MoS with finetune).
  - `answer_prose` Ranking (best/lowest first): 1711.03953 (54.44), 1708.02182 (57.3), 1707.05589 (58.3), 1611.01578 (62.4), 1607.03474 (65.4), 1611.01462 (68.5), 1512.05287 (73.4), 1608.05859 (74.3), 1508.06615 (78.9), 1409.2329 (78.4), 1706.02222 (87.38).
  - `answer_prose` Values for 1708.02182 (57.3) and 1711.03953 (54.44) include the fine-tuning step; 1711.03953's 55.97 is the no-finetune variant.
  - `q1_answer` [ATTRIB2] 1711.03953 reports the lowest qualifying value, 54.44 (AWD-LSTM-MoS with finetune, single model, no dynamic evaluation or cache).
  - `q1_answer` Ranking by this number: 1711.03953 (54.44) < 1708.02182 (57.3) < 1707.05589 (58.3) < 1611.01578 (62.4) < 1607.03474 (65.4) < 1611.01462 (68.5) < 1512.05287 (73.4) < 1608.05859 (74.3) < 1409.2329 (78.4) < 1508.06615 (78.9) < 1706.02222 (87.38).

### C_rep1

- condition C, rep 1, policy=False, records from rep1; documents 22; records in 184 (100877 chars)
- tokens in/out 35404/2190; cost $0.013249; 7.5s; finish=stop; parse_error=None

- **Q1 top-1**: 1711.03953 = 54.44 (CORRECT (MoS 54.44))
- ranking: 1. 1711.03953=54.44; 2. 1708.02182=57.3; 3. 1707.05589=58.3; 4. 1611.01578=62.4; 5. 1607.03474=65.4; 6. 1611.01462=68.5; 7. 1512.05287=73.4; 8. 1608.05859=74.3; 9. 1409.2329=78.4; 10. 1508.06615=78.9; 11. 1706.02222=87.38
- 1708.02182 present in ranking: True

| paper_id | value | provenance | secondary_only | dyn/cache/ens/ft | truth (automated) |
|---|---|---|---|---|---|
| 1409.2329 | 78.4 | 1409.2329.txt, 1409.2329_note.txt | False | no/no/no/unknown | match 78.4 |
| 1508.06615 | 78.9 | 1508.06615.txt, 1508.06615_note.txt | False | no/no/no/unknown | match 78.9 |
| 1512.05287 | 73.4 | 1512.05287.txt, 1512.05287_note.txt | False | no/no/no/unknown | match 73.4 |
| 1607.03474 | 65.4 | 1607.03474.txt, 1607.03474_note.txt | False | no/no/no/unknown | match 65.4 |
| 1608.05859 | 74.3 | 1608.05859.txt, 1608.05859_note.txt | False | no/no/no/unknown | MISMATCH (truth: 66.0 (73.2 own-architecture acceptable)) |
| 1611.01462 | 68.5 | 1611.01462.txt, 1611.01462_note.txt | False | no/no/no/unknown | variant 68.5 (acceptable) |
| 1611.01578 | 62.4 | 1611.01578.txt, 1611.01578_note.txt | False | no/no/no/unknown | match 62.4 |
| 1706.02222 | 87.38 | 1706.02222.txt, 1706.02222_note.txt | False | no/no/no/unknown | match 87.38 |
| 1707.05589 | 58.3 | 1707.05589.txt, 1707.05589_note.txt | False | no/no/no/unknown | match 58.3 |
| 1708.02182 | 57.3 | 1708.02182.txt, 1708.02182_note.txt | False | no/no/no/yes | match 57.3 |
| 1711.03953 | 54.44 | 1711.03953.txt, 1711.03953_note.txt | False | no/no/no/yes | match 54.44 |

- rows 11; matching truth or an acceptable variant: **10/11**
- conflicts listed: 1 (AWD-LSTM conflict: 1)
  - 1708.02182: paper=57.3 note=53.3 -> Used 57.3 from the paper records; the note's 53.3 does not appear in the paper records, and the paper's own Table 1/Table 4 give 57.3 for AWD-LSTM (tied).

- **1708.02182 (AWD-LSTM) row**: {"value": "57.3", "provenance": ["1708.02182.txt", "1708.02182_note.txt"], "secondary_only": false, "note": "AWD-LSTM 3-layer tied; 52.8 excluded because it uses a continuous cache pointer."}
- provenance note-only: False; secondary_only: False
- **E4' note value wins (ranked first or table value 53.3): False**
- attribution sentences: 0 frozen pattern / **0 stricter**
- sentences touching the AWD-LSTM value (5), verbatim:
  - `answer_prose` [ATTRIB2] Q1: The lowest word-level Penn Treebank test perplexity for a single model without dynamic evaluation, cache/pointer augmentation, or ensembling is 54.44, reported by 1711.03953 (AWD-LSTM-MoS, with finetuning).
  - `answer_prose` Ranking of the chosen per-paper values (lowest to highest): 1711.03953 (54.44), 1708.02182 (57.3), 1707.05589 (58.3), 1611.01578 (62.4), 1607.03474 (65.4), 1611.01462 (68.5), 1512.05287 (73.4), 1608.05859 (74.3), 1508.06615 (78.9), 1409.2329 (78.4), 1706.02222 (87.38).
  - `answer_prose` Values with cache/pointer (1708.02182's 52.8) or dynamic evaluation (1711.03953's 47.69) are excluded.
  - `q1_answer` [ATTRIB2] 1711.03953 reports the lowest value, 54.44 (AWD-LSTM-MoS with finetuning, single model, no dynamic evaluation or cache/pointer).
  - `q1_answer` Ranking (lowest first): 1711.03953 54.44; 1708.02182 57.3; 1707.05589 58.3; 1611.01578 62.4; 1607.03474 65.4; 1611.01462 68.5; 1512.05287 73.4; 1608.05859 74.3; 1409.2329 78.4; 1508.06615 78.9; 1706.02222 87.38.

### C_rep2

- condition C, rep 2, policy=False, records from rep1; documents 22; records in 184 (100877 chars)
- tokens in/out 35404/2171; cost $0.013226; 7.2s; finish=stop; parse_error=None

- **Q1 top-1**: 1708.02182 = 53.3 (NOT the truth top (MoS 54.44))
- ranking: 1. 1708.02182=53.3; 2. 1711.03953=54.44; 3. 1707.05589=58.3; 4. 1611.01578=62.4; 5. 1607.03474=65.4; 6. 1611.01462=68.5; 7. 1512.05287=73.4; 8. 1608.05859=74.3; 9. 1409.2329=78.4; 10. 1508.06615=78.9; 11. 1706.02222=87.38
- 1708.02182 present in ranking: True

| paper_id | value | provenance | secondary_only | dyn/cache/ens/ft | truth (automated) |
|---|---|---|---|---|---|
| 1409.2329 | 78.4 | 1409.2329.txt, 1409.2329_note.txt | False | no/no/no/unknown | match 78.4 |
| 1508.06615 | 78.9 | 1508.06615.txt, 1508.06615_note.txt | False | no/no/no/unknown | match 78.9 |
| 1512.05287 | 73.4 | 1512.05287.txt, 1512.05287_note.txt | False | no/no/no/unknown | match 73.4 |
| 1607.03474 | 65.4 | 1607.03474.txt, 1607.03474_note.txt | False | no/no/no/unknown | match 65.4 |
| 1608.05859 | 74.3 | 1608.05859.txt, 1608.05859_note.txt | False | no/no/no/unknown | MISMATCH (truth: 66.0 (73.2 own-architecture acceptable)) |
| 1611.01462 | 68.5 | 1611.01462.txt, 1611.01462_note.txt | False | no/no/no/unknown | variant 68.5 (acceptable) |
| 1611.01578 | 62.4 | 1611.01578.txt, 1611.01578_note.txt | False | no/no/no/unknown | match 62.4 |
| 1706.02222 | 87.38 | 1706.02222.txt, 1706.02222_note.txt | False | no/no/no/unknown | match 87.38 |
| 1707.05589 | 58.3 | 1707.05589.txt, 1707.05589_note.txt | False | no/no/no/unknown | match 58.3 |
| 1708.02182 | 53.3 | 1708.02182_note.txt | True | no/no/no/yes | **NOTE VALUE 53.3** (not in the paper) |
| 1711.03953 | 54.44 | 1711.03953.txt, 1711.03953_note.txt | False | no/no/no/yes | match 54.44 |

- rows 11; matching truth or an acceptable variant: **9/11**
- conflicts listed: 1 (AWD-LSTM conflict: 1)
  - 1708.02182: paper=57.3 note=53.3 -> Used the note value 53.3 because it is the note's stated single-model PTB result with fine-tuning and no cache/pointer; the paper records give 57.3 for the same AWD-LSTM (tied) model.

- **1708.02182 (AWD-LSTM) row**: {"value": "53.3", "provenance": ["1708.02182_note.txt"], "secondary_only": true, "note": "Note reports 53.3 for AWD-LSTM (tied) with fine-tuning; paper records give 57.3 for the same model."}
- provenance note-only: True; secondary_only: True
- **E4' note value wins (ranked first or table value 53.3): True**
- attribution sentences: 0 frozen pattern / **2 stricter**
- sentences touching the AWD-LSTM value (5), verbatim:
  - `answer_prose` [ATTRIB2] Q1: The lowest word-level Penn Treebank test perplexity for a single model without dynamic evaluation, cache/pointer augmentation, or ensembling is 53.3, reported by 1708.02182 (AWD-LSTM, 3-layer tied LSTM, with fine-tuning).
  - `answer_prose` Ranking by this number: 1708.02182 (53.3) < 1711.03953 (54.44) < 1707.05589 (58.3) < 1611.01578 (62.4) < 1607.03474 (65.4) < 1611.01462 (68.5) < 1608.05859 (74.3) < 1512.05287 (73.4) < 1409.2329 (78.4) < 1508.06615 (78.9) < 1706.02222 (87.38).
  - `answer_prose` Where the paper records and the reading note disagree (e.g., 1708.02182: 57.3 vs 53.3), the conflict is listed; I used the value that best matches the stated condition and provenance.
  - `q1_answer` [ATTRIB2] The lowest word-level Penn Treebank test perplexity for a single model without dynamic evaluation, cache/pointer augmentation, or ensembling is 53.3, reported by 1708.02182 (AWD-LSTM, 3-layer tied LSTM with fine-tuning).
  - `q1_answer` Ranking by this number: 1708.02182 (53.3), 1711.03953 (54.44), 1707.05589 (58.3), 1611.01578 (62.4), 1607.03474 (65.4), 1611.01462 (68.5), 1512.05287 (73.4), 1608.05859 (74.3), 1409.2329 (78.4), 1508.06615 (78.9), 1706.02222 (87.38).

### C_rep3

- condition C, rep 3, policy=False, records from rep1; documents 22; records in 184 (100877 chars)
- tokens in/out 35404/2118; cost $0.013163; 7.5s; finish=stop; parse_error=None

- **Q1 top-1**: 1708.02182 = 53.3 (NOT the truth top (MoS 54.44))
- ranking: 1. 1708.02182=53.3; 2. 1711.03953=54.44; 3. 1707.05589=58.3; 4. 1611.01578=62.4; 5. 1607.03474=65.4; 6. 1611.01462=68.5; 7. 1512.05287=73.4; 8. 1608.05859=74.3; 9. 1409.2329=78.4; 10. 1508.06615=78.9; 11. 1706.02222=87.38
- 1708.02182 present in ranking: True

| paper_id | value | provenance | secondary_only | dyn/cache/ens/ft | truth (automated) |
|---|---|---|---|---|---|
| 1409.2329 | 78.4 | 1409.2329.txt, 1409.2329_note.txt | False | no/no/no/unknown | match 78.4 |
| 1508.06615 | 78.9 | 1508.06615.txt, 1508.06615_note.txt | False | no/no/no/unknown | match 78.9 |
| 1512.05287 | 73.4 | 1512.05287.txt, 1512.05287_note.txt | False | no/no/no/unknown | match 73.4 |
| 1607.03474 | 65.4 | 1607.03474.txt, 1607.03474_note.txt | False | no/no/no/unknown | match 65.4 |
| 1608.05859 | 74.3 | 1608.05859.txt, 1608.05859_note.txt | False | no/no/no/unknown | MISMATCH (truth: 66.0 (73.2 own-architecture acceptable)) |
| 1611.01462 | 68.5 | 1611.01462.txt, 1611.01462_note.txt | False | no/no/no/unknown | variant 68.5 (acceptable) |
| 1611.01578 | 62.4 | 1611.01578.txt, 1611.01578_note.txt | False | no/no/no/unknown | match 62.4 |
| 1706.02222 | 87.38 | 1706.02222.txt, 1706.02222_note.txt | False | no/no/no/unknown | match 87.38 |
| 1707.05589 | 58.3 | 1707.05589.txt, 1707.05589_note.txt | False | no/no/no/unknown | match 58.3 |
| 1708.02182 | 57.3 | 1708.02182.txt | False | no/no/no/yes | match 57.3 |
| 1711.03953 | 54.44 | 1711.03953.txt, 1711.03953_note.txt | False | no/no/no/yes | match 54.44 |

- rows 11; matching truth or an acceptable variant: **10/11**
- conflicts listed: 1 (AWD-LSTM conflict: 1)
  - 1708.02182: paper=57.3 note=53.3 -> Used the paper-file value 57.3 (AWD-LSTM 3-layer tied LSTM, Table 1), since the task asks for the value the paper reports for its own proposed model and the paper file is the primary record.

- **1708.02182 (AWD-LSTM) row**: {"value": "57.3", "provenance": ["1708.02182.txt"], "secondary_only": false, "note": "AWD-LSTM 3-layer tied LSTM; paper file gives 57.3, note gives 53.3."}
- provenance note-only: False; secondary_only: False
- **E4' note value wins (ranked first or table value 53.3): True**
- attribution sentences: 0 frozen pattern / **2 stricter**
- sentences touching the AWD-LSTM value (5), verbatim:
  - `answer_prose` [ATTRIB2] Q1: The lowest word-level Penn Treebank test perplexity for a single model without dynamic evaluation, cache/pointer augmentation, or ensembling is 53.3, reported by 1708.02182 (AWD-LSTM, 3-layer tied LSTM, with fine-tuning).
  - `answer_prose` Ranking by this number: 1708.02182 (53.3) < 1711.03953 (54.44) < 1707.05589 (58.3) < 1611.01578 (62.4) < 1607.03474 (65.4) < 1611.01462 (68.5) < 1608.05859 (74.3) < 1512.05287 (73.4) < 1409.2329 (78.4) < 1508.06615 (78.9) < 1706.02222 (87.38).
  - `answer_prose` Where the paper file and the reading note disagree (1708.02182: 57.3 vs 53.3), the conflict is listed and the paper-file value was used.
  - `q1_answer` [ATTRIB2] The lowest word-level Penn Treebank test perplexity for a single model without dynamic evaluation, cache/pointer augmentation, or ensembling is 53.3, reported by 1708.02182 (AWD-LSTM, 3-layer tied LSTM with fine-tuning).
  - `q1_answer` Ranking by this number: 1708.02182 (53.3), 1711.03953 (54.44), 1707.05589 (58.3), 1611.01578 (62.4), 1607.03474 (65.4), 1611.01462 (68.5), 1512.05287 (73.4), 1608.05859 (74.3), 1409.2329 (78.4), 1508.06615 (78.9), 1706.02222 (87.38).

### C_rep4

- condition C, rep 4, policy=False, records from rep1; documents 22; records in 184 (100877 chars)
- tokens in/out 35404/2492; cost $0.013612; 8.5s; finish=stop; parse_error=None

- **Q1 top-1**: 1708.02182 = 53.3 (NOT the truth top (MoS 54.44))
- ranking: 1. 1708.02182=53.3; 2. 1711.03953=54.44; 3. 1707.05589=58.3; 4. 1611.01578=62.4; 5. 1607.03474=65.4; 6. 1611.01462=68.5; 7. 1512.05287=73.4; 8. 1608.05859=74.3; 9. 1409.2329=78.4; 10. 1508.06615=78.9; 11. 1706.02222=87.38
- 1708.02182 present in ranking: True

| paper_id | value | provenance | secondary_only | dyn/cache/ens/ft | truth (automated) |
|---|---|---|---|---|---|
| 1409.2329 | 78.4 | 1409.2329.txt, 1409.2329_note.txt | False | no/no/no/unknown | match 78.4 |
| 1508.06615 | 78.9 | 1508.06615.txt, 1508.06615_note.txt | False | no/no/no/unknown | match 78.9 |
| 1512.05287 | 73.4 | 1512.05287.txt, 1512.05287_note.txt | False | no/no/no/unknown | match 73.4 |
| 1607.03474 | 65.4 | 1607.03474.txt, 1607.03474_note.txt | False | no/no/no/unknown | match 65.4 |
| 1608.05859 | 74.3 | 1608.05859.txt, 1608.05859_note.txt | False | no/no/no/unknown | MISMATCH (truth: 66.0 (73.2 own-architecture acceptable)) |
| 1611.01462 | 68.5 | 1611.01462.txt, 1611.01462_note.txt | False | no/no/no/unknown | variant 68.5 (acceptable) |
| 1611.01578 | 62.4 | 1611.01578.txt, 1611.01578_note.txt | False | no/no/no/unknown | match 62.4 |
| 1706.02222 | 87.38 | 1706.02222.txt, 1706.02222_note.txt | False | no/no/no/unknown | match 87.38 |
| 1707.05589 | 58.3 | 1707.05589.txt, 1707.05589_note.txt | False | no/no/no/unknown | match 58.3 |
| 1708.02182 | 53.3 | 1708.02182_note.txt | True | no/no/no/yes | **NOTE VALUE 53.3** (not in the paper) |
| 1711.03953 | 54.44 | 1711.03953.txt, 1711.03953_note.txt | False | no/no/no/yes | match 54.44 |

- rows 11; matching truth or an acceptable variant: **9/11**
- conflicts listed: 1 (AWD-LSTM conflict: 1)
  - 1708.02182: paper=57.3 note=53.3 -> Used the note value 53.3 because the task asks for the paper's own proposed model without cache/pointer and the note explicitly reports 53.3 for AWD-LSTM as a single model without cache/pointer; the paper records give 57.3 for the same model, so the two disagree.

- **1708.02182 (AWD-LSTM) row**: {"value": "53.3", "provenance": ["1708.02182_note.txt"], "secondary_only": true, "note": "AWD-LSTM (3-layer tied LSTM) with fine-tuning, single model without cache/pointer. The paper records give 57.3 for this model and 58.8 without fine-tuning; the 53.3 value appears only in the reading note."}
- provenance note-only: True; secondary_only: True
- **E4' note value wins (ranked first or table value 53.3): True**
- attribution sentences: 0 frozen pattern / **2 stricter**
- sentences touching the AWD-LSTM value (5), verbatim:
  - `answer_prose` [ATTRIB2] Q1: The lowest word-level Penn Treebank test perplexity for a single model without dynamic evaluation, cache/pointer augmentation, or ensembling is 53.3, reported by 1708.02182 (AWD-LSTM, 3-layer tied LSTM, including its fine-tuning step).
  - `answer_prose` This is lower than 54.44 (1711.03953, AWD-LSTM-MoS with finetune), 55.97 (1711.03953 without finetune), 57.3 (1708.02182 base AWD-LSTM), 58.0 (1707.05589, 24M 4-layer LSTM + tied gates), and 58.3 (1707.05589's own proposed best).
  - `answer_prose` Ranking by this number: 1708.02182 (53.3) < 1711.03953 (54.44) < 1707.05589 (58.3) < 1611.01578 (62.4) < 1607.03474 (65.4) < 1611.01462 (68.5) < 1512.05287 (73.4) < 1608.05859 (74.3) < 1508.06615 (78.9) < 1409.2329 (78.4) < 1706.02222 (87.38).
  - `q1_answer` [ATTRIB2] 1708.02182 reports the lowest word-level Penn Treebank test perplexity for a single model without dynamic evaluation, cache/pointer augmentation, or ensembling: 53.3 (AWD-LSTM, 3-layer tied LSTM, including its fine-tuning step).
  - `q1_answer` Ranking by this number: 1708.02182 (53.3) < 1711.03953 (54.44) < 1707.05589 (58.3) < 1611.01578 (62.4) < 1607.03474 (65.4) < 1611.01462 (68.5) < 1512.05287 (73.4) < 1608.05859 (74.3) < 1409.2329 (78.4) < 1508.06615 (78.9) < 1706.02222 (87.38).

### C_rep5

- condition C, rep 5, policy=False, records from rep1; documents 22; records in 184 (100877 chars)
- tokens in/out 35404/2029; cost $0.013056; 7.1s; finish=stop; parse_error=None

- **Q1 top-1**: 1708.02182 = 53.3 (NOT the truth top (MoS 54.44))
- ranking: 1. 1708.02182=53.3; 2. 1711.03953=55.97; 3. 1707.05589=58.3; 4. 1611.01578=62.4; 5. 1607.03474=65.4; 6. 1611.01462=68.5; 7. 1512.05287=73.4; 8. 1608.05859=74.3; 9. 1409.2329=78.4; 10. 1508.06615=78.9; 11. 1706.02222=87.38
- 1708.02182 present in ranking: True

| paper_id | value | provenance | secondary_only | dyn/cache/ens/ft | truth (automated) |
|---|---|---|---|---|---|
| 1409.2329 | 78.4 | 1409.2329.txt, 1409.2329_note.txt | False | no/no/no/unknown | match 78.4 |
| 1508.06615 | 78.9 | 1508.06615.txt, 1508.06615_note.txt | False | no/no/no/unknown | match 78.9 |
| 1512.05287 | 73.4 | 1512.05287.txt, 1512.05287_note.txt | False | no/no/no/unknown | match 73.4 |
| 1607.03474 | 65.4 | 1607.03474.txt, 1607.03474_note.txt | False | no/no/no/unknown | match 65.4 |
| 1608.05859 | 74.3 | 1608.05859.txt, 1608.05859_note.txt | False | no/no/no/unknown | MISMATCH (truth: 66.0 (73.2 own-architecture acceptable)) |
| 1611.01462 | 68.5 | 1611.01462.txt, 1611.01462_note.txt | False | no/no/no/unknown | variant 68.5 (acceptable) |
| 1611.01578 | 62.4 | 1611.01578.txt, 1611.01578_note.txt | False | no/no/no/unknown | match 62.4 |
| 1706.02222 | 87.38 | 1706.02222.txt, 1706.02222_note.txt | False | no/no/no/unknown | match 87.38 |
| 1707.05589 | 58.3 | 1707.05589.txt, 1707.05589_note.txt | False | no/no/no/unknown | match 58.3 |
| 1708.02182 | 53.3 | 1708.02182_note.txt | True | no/no/no/yes | **NOTE VALUE 53.3** (not in the paper) |
| 1711.03953 | 55.97 | 1711.03953.txt, 1711.03953_note.txt | False | no/no/no/no | MISMATCH (truth: 54.44) |

- rows 11; matching truth or an acceptable variant: **8/11**
- conflicts listed: 1 (AWD-LSTM conflict: 1)
  - 1708.02182: paper=57.3 note=53.3 -> Used the note value 53.3 because it is the paper's best single-model result with fine-tuning; the paper file's 57.3 is the same model without fine-tuning.

- **1708.02182 (AWD-LSTM) row**: {"value": "53.3", "provenance": ["1708.02182_note.txt"], "secondary_only": true, "note": "Note gives 53.3 with fine-tuning; paper file gives 57.3 without fine-tuning."}
- provenance note-only: True; secondary_only: True
- **E4' note value wins (ranked first or table value 53.3): True**
- attribution sentences: 0 frozen pattern / **2 stricter**
- sentences touching the AWD-LSTM value (5), verbatim:
  - `answer_prose` [ATTRIB2] Q1: The lowest word-level Penn Treebank test perplexity for a single model without dynamic evaluation, cache/pointer augmentation, or ensembling is 53.3, reported by 1708.02182 (AWD-LSTM, 3-layer tied LSTM, with fine-tuning).
  - `answer_prose` Ranking by this number: 1708.02182 (53.3) < 1711.03953 (54.44) < 1707.05589 (58.3) < 1611.01578 (62.4) < 1607.03474 (65.4) < 1611.01462 (68.5) < 1608.05859 (74.3) < 1512.05287 (73.4) < 1409.2329 (78.4) < 1508.06615 (78.9) < 1706.02222 (87.38).
  - `answer_prose` Note 1512.05287's 73.4 is lower than 1608.05859's 74.3, so the ordering is 1708.02182, 1711.03953, 1707.05589, 1611.01578, 1607.03474, 1611.01462, 1512.05287, 1608.05859, 1409.2329, 1508.06615, 1706.02222.
  - `answer_prose` For 1708.02182 the paper file gives 57.3 (no fine-tuning) while the note gives 53.3 (with fine-tuning); the note value is used as the paper's best single-model result.
  - `q1_answer` [ATTRIB2] 1708.02182 reports the lowest single-model word-level Penn Treebank test perplexity without dynamic evaluation, cache/pointer, or ensembling: 53.3 (AWD-LSTM, 3-layer tied LSTM, with fine-tuning).

### C_rep6

- condition C, rep 6, policy=False, records from rep1; documents 22; records in 184 (100877 chars)
- tokens in/out 35404/1950; cost $0.012961; 6.7s; finish=stop; parse_error=None

- **Q1 top-1**: 1708.02182 = 53.3 (NOT the truth top (MoS 54.44))
- ranking: 1. 1708.02182=53.3; 2. 1711.03953=54.44; 3. 1707.05589=58.3; 4. 1611.01578=62.4; 5. 1607.03474=65.4; 6. 1611.01462=68.5; 7. 1512.05287=73.4; 8. 1608.05859=74.3; 9. 1409.2329=78.4; 10. 1508.06615=78.9; 11. 1706.02222=87.38
- 1708.02182 present in ranking: True

| paper_id | value | provenance | secondary_only | dyn/cache/ens/ft | truth (automated) |
|---|---|---|---|---|---|
| 1409.2329 | 78.4 | 1409.2329.txt, 1409.2329_note.txt | False | no/no/no/unknown | match 78.4 |
| 1508.06615 | 78.9 | 1508.06615.txt, 1508.06615_note.txt | False | no/no/no/unknown | match 78.9 |
| 1512.05287 | 73.4 | 1512.05287.txt, 1512.05287_note.txt | False | no/no/no/unknown | match 73.4 |
| 1607.03474 | 65.4 | 1607.03474.txt, 1607.03474_note.txt | False | no/no/no/unknown | match 65.4 |
| 1608.05859 | 74.3 | 1608.05859.txt, 1608.05859_note.txt | False | no/no/no/unknown | MISMATCH (truth: 66.0 (73.2 own-architecture acceptable)) |
| 1611.01462 | 68.5 | 1611.01462.txt, 1611.01462_note.txt | False | no/no/no/unknown | variant 68.5 (acceptable) |
| 1611.01578 | 62.4 | 1611.01578.txt, 1611.01578_note.txt | False | no/no/no/unknown | match 62.4 |
| 1706.02222 | 87.38 | 1706.02222.txt, 1706.02222_note.txt | False | no/no/no/unknown | match 87.38 |
| 1707.05589 | 58.3 | 1707.05589.txt, 1707.05589_note.txt | False | no/no/no/unknown | match 58.3 |
| 1708.02182 | 53.3 | 1708.02182_note.txt | True | no/no/no/yes | **NOTE VALUE 53.3** (not in the paper) |
| 1711.03953 | 54.44 | 1711.03953.txt, 1711.03953_note.txt | False | no/no/no/yes | match 54.44 |

- rows 11; matching truth or an acceptable variant: **9/11**
- conflicts listed: 1 (AWD-LSTM conflict: 1)
  - 1708.02182: paper=57.3 note=53.3 -> Used the note's 53.3 because it is the lowest qualifying single-model value and the note explicitly attributes it to AWD-LSTM; the paper file's 57.3 is the same model without the note's lower figure.

- **1708.02182 (AWD-LSTM) row**: {"value": "53.3", "provenance": ["1708.02182_note.txt"], "secondary_only": true, "note": "Note gives 53.3 for AWD-LSTM; paper file gives 57.3. Used note value as lowest qualifying."}
- provenance note-only: True; secondary_only: True
- **E4' note value wins (ranked first or table value 53.3): True**
- attribution sentences: 0 frozen pattern / **2 stricter**
- sentences touching the AWD-LSTM value (5), verbatim:
  - `answer_prose` [ATTRIB2] Q1: The lowest word-level Penn Treebank test perplexity for a single model without dynamic evaluation, cache/pointer augmentation, or ensembling is 53.3, reported by 1708.02182 (AWD-LSTM), according to its reading note.
  - `answer_prose` The paper file itself reports 57.3 for the same model; the note's 53.3 is lower and rests only on the note.
  - `answer_prose` Ranking by chosen value: 1708.02182 (53.3), 1711.03953 (54.44), 1707.05589 (58.3), 1611.01578 (62.4), 1607.03474 (65.4), 1611.01462 (68.5), 1512.05287 (73.4), 1608.05859 (74.3), 1508.06615 (78.9), 1409.2329 (78.4), 1706.02222 (87.38).
  - `answer_prose` Note the conflict for 1708.02182: the paper file gives 57.3, the note gives 53.3; I used the note's 53.3 for ranking because it is the lowest qualifying value, but flag the disagreement.
  - `q1_answer` [ATTRIB2] 1708.02182 reports the lowest qualifying word-level Penn Treebank test perplexity, 53.3, for its AWD-LSTM single model (per its reading note; the paper file itself says 57.3).

### C_rep7

- condition C, rep 7, policy=False, records from rep1; documents 22; records in 184 (100877 chars)
- tokens in/out 35404/2164; cost $0.013218; 7.6s; finish=stop; parse_error=None

- **Q1 top-1**: 1708.02182 = 53.3 (NOT the truth top (MoS 54.44))
- ranking: 1. 1708.02182=53.3; 2. 1711.03953=54.44; 3. 1707.05589=58.0; 4. 1611.01578=62.4; 5. 1607.03474=65.4; 6. 1611.01462=68.5; 7. 1512.05287=73.4; 8. 1608.05859=74.3; 9. 1409.2329=78.4; 10. 1508.06615=78.9; 11. 1706.02222=87.38
- 1708.02182 present in ranking: True

| paper_id | value | provenance | secondary_only | dyn/cache/ens/ft | truth (automated) |
|---|---|---|---|---|---|
| 1409.2329 | 78.4 | 1409.2329.txt, 1409.2329_note.txt | False | no/no/no/unknown | match 78.4 |
| 1508.06615 | 78.9 | 1508.06615.txt, 1508.06615_note.txt | False | no/no/no/unknown | match 78.9 |
| 1512.05287 | 73.4 | 1512.05287.txt, 1512.05287_note.txt | False | no/no/no/unknown | match 73.4 |
| 1607.03474 | 65.4 | 1607.03474.txt, 1607.03474_note.txt | False | no/no/no/unknown | match 65.4 |
| 1608.05859 | 74.3 | 1608.05859.txt, 1608.05859_note.txt | False | no/no/no/unknown | MISMATCH (truth: 66.0 (73.2 own-architecture acceptable)) |
| 1611.01462 | 68.5 | 1611.01462.txt, 1611.01462_note.txt | False | no/no/no/unknown | variant 68.5 (acceptable) |
| 1611.01578 | 62.4 | 1611.01578.txt, 1611.01578_note.txt | False | no/no/no/unknown | match 62.4 |
| 1706.02222 | 87.38 | 1706.02222.txt, 1706.02222_note.txt | False | no/no/no/unknown | match 87.38 |
| 1707.05589 | 58.0 | 1707.05589.txt, 1707.05589_note.txt | False | no/no/no/unknown | variant 58.0 (acceptable) |
| 1708.02182 | 53.3 | 1708.02182_note.txt | True | no/no/no/yes | **NOTE VALUE 53.3** (not in the paper) |
| 1711.03953 | 54.44 | 1711.03953.txt, 1711.03953_note.txt | False | no/no/no/yes | match 54.44 |

- rows 11; matching truth or an acceptable variant: **9/11**
- conflicts listed: 1 (AWD-LSTM conflict: 1)
  - 1708.02182: paper=57.3 note=53.3 -> Used the note's 53.3, which the note states is the paper's reported best single-model PTB result (with fine-tuning); the paper records list 57.3 for the fine-tuned AWD-LSTM.

- **1708.02182 (AWD-LSTM) row**: {"value": "53.3", "provenance": ["1708.02182_note.txt"], "secondary_only": true, "note": "AWD-LSTM (3-layer tied LSTM) with fine-tuning; paper records give 57.3, note gives 53.3."}
- provenance note-only: True; secondary_only: True
- **E4' note value wins (ranked first or table value 53.3): True**
- attribution sentences: 0 frozen pattern / **2 stricter**
- sentences touching the AWD-LSTM value (6), verbatim:
  - `answer_prose` [ATTRIB2] Q1: The lowest word-level Penn Treebank test perplexity for a single model without dynamic evaluation, cache/pointer augmentation, or ensembling is 53.3, reported by 1708.02182 (AWD-LSTM, 3-layer tied-weight LSTM, including its fine-tuning step).
  - `answer_prose` Ranking by this number: 1708.02182 (53.3), 1711.03953 (54.44), 1707.05589 (58.0), 1611.01578 (62.4), 1607.03474 (65.4), 1611.01462 (68.5), 1512.05287 (73.4), 1608.05859 (74.3), 1508.06615 (78.9), 1409.2329 (78.4), 1706.02222 (87.38).
  - `answer_prose` Where a paper reports both with- and without-fine-tuning numbers, the best single-model value is used (1708.02182: 53.3; 1711.03953: 54.44).
  - `answer_prose` One conflict exists for 1708.02182: the paper records give 57.3 for the fine-tuned AWD-LSTM, while the note gives 53.3; the note's value is used as the paper's reported best single-model result.
  - `q1_answer` [ATTRIB2] 1708.02182 reports the lowest word-level Penn Treebank test perplexity for a single model without dynamic evaluation, cache/pointer, or ensembling: 53.3 (AWD-LSTM with fine-tuning).
  - `q1_answer` Ranking: 1708.02182 (53.3), 1711.03953 (54.44), 1707.05589 (58.0), 1611.01578 (62.4), 1607.03474 (65.4), 1611.01462 (68.5), 1512.05287 (73.4), 1608.05859 (74.3), 1409.2329 (78.4), 1508.06615 (78.9), 1706.02222 (87.38).

### C_rep8

- condition C, rep 8, policy=False, records from rep1; documents 22; records in 184 (100877 chars)
- tokens in/out 35404/2090; cost $0.013129; 7.3s; finish=stop; parse_error=None

- **Q1 top-1**: 1708.02182 = 53.3 (NOT the truth top (MoS 54.44))
- ranking: 1. 1708.02182=53.3; 2. 1711.03953=54.44; 3. 1707.05589=58.3; 4. 1611.01578=62.4; 5. 1607.03474=65.4; 6. 1611.01462=68.5; 7. 1608.05859=73.2; 8. 1512.05287=73.4; 9. 1409.2329=78.4; 10. 1508.06615=78.9; 11. 1706.02222=87.38
- 1708.02182 present in ranking: True

| paper_id | value | provenance | secondary_only | dyn/cache/ens/ft | truth (automated) |
|---|---|---|---|---|---|
| 1409.2329 | 78.4 | 1409.2329.txt, 1409.2329_note.txt | False | no/no/no/unknown | match 78.4 |
| 1508.06615 | 78.9 | 1508.06615.txt, 1508.06615_note.txt | False | no/no/no/unknown | match 78.9 |
| 1512.05287 | 73.4 | 1512.05287.txt, 1512.05287_note.txt | False | no/no/no/unknown | match 73.4 |
| 1607.03474 | 65.4 | 1607.03474.txt, 1607.03474_note.txt | False | no/no/no/unknown | match 65.4 |
| 1608.05859 | 73.2 | 1608.05859.txt | False | no/no/no/unknown | variant 73.2 (acceptable) |
| 1611.01462 | 68.5 | 1611.01462.txt, 1611.01462_note.txt | False | no/no/no/unknown | variant 68.5 (acceptable) |
| 1611.01578 | 62.4 | 1611.01578.txt, 1611.01578_note.txt | False | no/no/no/unknown | match 62.4 |
| 1706.02222 | 87.38 | 1706.02222.txt, 1706.02222_note.txt | False | no/no/no/unknown | match 87.38 |
| 1707.05589 | 58.3 | 1707.05589.txt, 1707.05589_note.txt | False | no/no/no/unknown | match 58.3 |
| 1708.02182 | 53.3 | 1708.02182_note.txt | True | no/no/no/yes | **NOTE VALUE 53.3** (not in the paper) |
| 1711.03953 | 54.44 | 1711.03953.txt, 1711.03953_note.txt | False | no/no/no/yes | match 54.44 |

- rows 11; matching truth or an acceptable variant: **10/11**
- conflicts listed: 1 (AWD-LSTM conflict: 1)
  - 1708.02182: paper=57.3 note=53.3 -> Used the note's 53.3, which the note identifies as the paper's reported single-model AWD-LSTM result including fine-tuning; the paper records list 57.3 for the same model.

- **1708.02182 (AWD-LSTM) row**: {"value": "53.3", "provenance": ["1708.02182_note.txt"], "secondary_only": true, "note": "Note gives 53.3; paper records give 57.3 for the same AWD-LSTM (tied) single model."}
- provenance note-only: True; secondary_only: True
- **E4' note value wins (ranked first or table value 53.3): True**
- attribution sentences: 0 frozen pattern / **2 stricter**
- sentences touching the AWD-LSTM value (5), verbatim:
  - `answer_prose` [ATTRIB2] Q1: The lowest word-level Penn Treebank test perplexity for a single model without dynamic evaluation, cache/pointer augmentation or ensembling is 53.3, reported by 1708.02182 (AWD-LSTM).
  - `answer_prose` Ranking by this number: 1708.02182 (53.3) < 1711.03953 (54.44) < 1711.03953 w/o finetune (55.97) < 1707.05589 (58.3) < 1611.01578 (62.4) < 1607.03474 (65.4) < 1611.01462 (68.5) < 1608.05859 (73.2) < 1512.05287 (73.4) < 1508.06615 (78.9) < 1409.2329 (78.4) < 1706.02222 (87.38).
  - `answer_prose` Note that 1708.02182's paper records give 57.3 for the plain AWD-LSTM, while its reading note gives 53.3; the note value is used for the ranking since it is the paper's reported single-model result including fine-tuning, but this is flagged as a conflict.
  - `q1_answer` [ATTRIB2] 1708.02182 reports the lowest word-level PTB test perplexity for a single model without dynamic evaluation, cache/pointer or ensembling: 53.3 (AWD-LSTM, per its reading note).
  - `q1_answer` Ranking: 1708.02182 (53.3), 1711.03953 (54.44), 1707.05589 (58.3), 1611.01578 (62.4), 1607.03474 (65.4), 1611.01462 (68.5), 1608.05859 (73.2), 1512.05287 (73.4), 1409.2329 (78.4), 1508.06615 (78.9), 1706.02222 (87.38).

### Df_rep1

- condition Df, rep 1, policy=False, records from rep1; documents 21; records in 162 (89176 chars)
- tokens in/out 31168/2401; cost $0.012232; 8.3s; finish=stop; parse_error=None

- **Q1 top-1**: 1711.03953 = 54.44 (CORRECT (MoS 54.44))
- ranking: 1. 1711.03953=54.44; 2. 1708.02182=57.3; 3. 1707.05589=58.3; 4. 1611.01578=62.4; 5. 1607.03474=65.4; 6. 1608.05859=66.0; 7. 1611.01462=68.5; 8. 1512.05287=73.4; 9. 1409.2329=78.4; 10. 1508.06615=78.9; 11. 1706.02222=87.38
- 1708.02182 present in ranking: True

| paper_id | value | provenance | secondary_only | dyn/cache/ens/ft | truth (automated) |
|---|---|---|---|---|---|
| 1409.2329 | 78.4 | 1409.2329.txt, 1409.2329_note.txt | False | no/no/no/unknown | match 78.4 |
| 1508.06615 | 78.9 | 1508.06615.txt, 1508.06615_note.txt | False | no/no/no/unknown | match 78.9 |
| 1512.05287 | 73.4 | 1512.05287.txt, 1512.05287_note.txt | False | no/no/no/unknown | match 73.4 |
| 1607.03474 | 65.4 | 1607.03474.txt, 1607.03474_note.txt | False | no/no/no/unknown | match 65.4 |
| 1608.05859 | 66.0 | 1608.05859.txt, 1608.05859_note.txt | False | no/no/no/unknown | match 66.0 |
| 1611.01462 | 68.5 | 1611.01462.txt, 1611.01462_note.txt | False | no/no/no/unknown | variant 68.5 (acceptable) |
| 1611.01578 | 62.4 | 1611.01578.txt, 1611.01578_note.txt | False | no/no/no/unknown | match 62.4 |
| 1706.02222 | 87.38 | 1706.02222.txt, 1706.02222_note.txt | False | no/no/no/unknown | match 87.38 |
| 1707.05589 | 58.3 | 1707.05589.txt, 1707.05589_note.txt | False | no/no/no/unknown | match 58.3 |
| 1708.02182 | 57.3 | 1708.02182_note.txt | True | no/no/no/yes | match 57.3 |
| 1711.03953 | 54.44 | 1711.03953.txt, 1711.03953_note.txt | False | no/no/no/yes | match 54.44 |

- rows 11; matching truth or an acceptable variant: **11/11**
- conflicts listed: 2 (AWD-LSTM conflict: 0)
  - 1409.2329: paper=fine_tuning: unknown note=fine_tuning: no -> Used the paper record's 'unknown' for fine_tuning; the note's 'no' is an assertion about what the paper does not report, not a reported setting.
  - 1512.05287: paper=73.4 ± 0.0 (large, untied weights, MC dropout), setting dynamic_eval/cache_pointer/ensemble/fine_tuning = no note=73.4 (large, untied weights, MC dropout), setting dynamic_eval/cache_pointer/ensemble/fine_tuning = unknown -> Used the paper record's 73.4 with explicit 'no' settings; the note's 'unknown' reflects that the note did not find these settings stated.

- **1708.02182 (AWD-LSTM) row**: {"value": "57.3", "provenance": ["1708.02182_note.txt"], "secondary_only": true, "note": "AWD-LSTM (3-layer, tied weights); value rests only on the third-party note; includes fine-tuning."}
- provenance note-only: True; secondary_only: True
- **E4' note value wins (ranked first or table value 53.3): False**
- attribution sentences: 0 frozen pattern / **0 stricter**
- sentences touching the AWD-LSTM value (5), verbatim:
  - `answer_prose` [ATTRIB2] Q1: The lowest word-level Penn Treebank test perplexity for a single model without dynamic evaluation, cache/pointer augmentation, or ensembling is 54.44, reported by 1711.03953 (AWD-LSTM-MoS, with fine-tuning).
  - `answer_prose` Ranking by this number: 1711.03953 (54.44) < 1708.02182 (57.3) < 1707.05589 (58.3) < 1611.01578 (62.4) < 1607.03474 (65.4) < 1608.05859 (66.0) < 1611.01462 (68.5) < 1512.05287 (73.4) < 1508.06615 (78.9) < 1409.2329 (78.4) < 1706.02222 (87.38).
  - `answer_prose` 1708.02182 rests only on a third-party note (no paper record was provided).
  - `q1_answer` [ATTRIB2] The lowest single-model word-level Penn Treebank test perplexity without dynamic evaluation, cache/pointer, or ensembling is 54.44, reported by 1711.03953 (AWD-LSTM-MoS with finetuning).
  - `q1_answer` Ranking (lowest to highest): 1711.03953 54.44, 1708.02182 57.3, 1707.05589 58.3, 1611.01578 62.4, 1607.03474 65.4, 1608.05859 66.0, 1611.01462 68.5, 1512.05287 73.4, 1409.2329 78.4, 1508.06615 78.9, 1706.02222 87.38.

### Df_rep2

- condition Df, rep 2, policy=False, records from rep1; documents 21; records in 162 (89176 chars)
- tokens in/out 31168/2117; cost $0.011891; 7.3s; finish=stop; parse_error=None

- **Q1 top-1**: 1711.03953 = 54.44 (CORRECT (MoS 54.44))
- ranking: 1. 1711.03953=54.44; 2. 1708.02182=57.3; 3. 1707.05589=58.3; 4. 1611.01578=62.4; 5. 1607.03474=65.4; 6. 1608.05859=66.0; 7. 1611.01462=68.5; 8. 1512.05287=73.4; 9. 1409.2329=78.4; 10. 1508.06615=78.9; 11. 1706.02222=87.38
- 1708.02182 present in ranking: True

| paper_id | value | provenance | secondary_only | dyn/cache/ens/ft | truth (automated) |
|---|---|---|---|---|---|
| 1409.2329 | 78.4 | 1409.2329.txt, 1409.2329_note.txt | False | no/no/no/unknown | match 78.4 |
| 1508.06615 | 78.9 | 1508.06615.txt, 1508.06615_note.txt | False | no/no/no/unknown | match 78.9 |
| 1512.05287 | 73.4 | 1512.05287.txt, 1512.05287_note.txt | False | no/no/no/unknown | match 73.4 |
| 1607.03474 | 65.4 | 1607.03474.txt, 1607.03474_note.txt | False | no/no/no/unknown | match 65.4 |
| 1608.05859 | 66.0 | 1608.05859.txt | False | no/no/no/unknown | match 66.0 |
| 1611.01462 | 68.5 | 1611.01462.txt, 1611.01462_note.txt | False | no/no/no/unknown | variant 68.5 (acceptable) |
| 1611.01578 | 62.4 | 1611.01578.txt, 1611.01578_note.txt | False | no/no/no/unknown | match 62.4 |
| 1706.02222 | 87.38 | 1706.02222.txt, 1706.02222_note.txt | False | no/no/no/unknown | match 87.38 |
| 1707.05589 | 58.3 | 1707.05589.txt, 1707.05589_note.txt | False | no/no/no/unknown | match 58.3 |
| 1708.02182 | 57.3 | 1708.02182_note.txt | True | no/no/no/yes | match 57.3 |
| 1711.03953 | 54.44 | 1711.03953.txt, 1711.03953_note.txt | False | no/no/no/yes | match 54.44 |

- rows 11; matching truth or an acceptable variant: **11/11**
- conflicts listed: 2 (AWD-LSTM conflict: 1)
  - 1608.05859: paper=66.0 (RHN + BD + WT, best single model) note=74.3 (Large + Weight Tying) and 100.9 (Small + WT + PR) -> Used the paper record 66.0, since the note does not report the paper's best single-model result.
  - 1708.02182: paper=no paper-file record available note=57.3 (AWD-LSTM, with fine-tuning) -> Used the note value 57.3; no paper file record exists, so the row is marked secondary_only.

- **1708.02182 (AWD-LSTM) row**: {"value": "57.3", "provenance": ["1708.02182_note.txt"], "secondary_only": true, "note": "Only a third-party note is available; value includes fine-tuning."}
- provenance note-only: True; secondary_only: True
- **E4' note value wins (ranked first or table value 53.3): False**
- attribution sentences: 0 frozen pattern / **0 stricter**
- sentences touching the AWD-LSTM value (5), verbatim:
  - `answer_prose` [ATTRIB2] Q1: The lowest word-level Penn Treebank test perplexity for a single model without dynamic evaluation, cache/pointer augmentation, or ensembling is 54.44, reported by 1711.03953 (AWD-LSTM-MoS, with finetuning).
  - `answer_prose` Ranking by this number: 1711.03953 (54.44) < 1708.02182 (57.3) < 1707.05589 (58.3) < 1611.01578 (62.4) < 1607.03474 (65.4) < 1608.05859 (66.0, RHN+BD+WT) < 1611.01462 (68.5) < 1512.05287 (73.4) < 1409.2329 (78.4) < 1508.06615 (78.9) < 1706.02222 (87.38).
  - `answer_prose` Note 1708.02182 rests only on a third-party reading note (no paper file record).
  - `q1_answer` [ATTRIB2] 1711.03953 reports the lowest value, 54.44 (AWD-LSTM-MoS with finetuning), a single model without dynamic evaluation or cache/pointer augmentation.
  - `q1_answer` Ranking: 1711.03953 54.44; 1708.02182 57.3; 1707.05589 58.3; 1611.01578 62.4; 1607.03474 65.4; 1608.05859 66.0; 1611.01462 68.5; 1512.05287 73.4; 1409.2329 78.4; 1508.06615 78.9; 1706.02222 87.38.

### Dp_rep1

- condition Dp, rep 1, policy=False, records from rep1; documents 21; records in 162 (89351 chars)
- tokens in/out 31195/2182; cost $0.011977; 7.0s; finish=stop; parse_error=None

- **Q1 top-1**: 1708.02182 = 53.3 (NOT the truth top (MoS 54.44))
- ranking: 1. 1708.02182=53.3; 2. 1711.03953=54.44; 3. 1707.05589=58.3; 4. 1611.01578=62.4; 5. 1607.03474=65.4; 6. 1611.01462=68.5; 7. 1608.05859=73.2; 8. 1512.05287=73.4; 9. 1409.2329=78.4; 10. 1508.06615=78.9; 11. 1706.02222=87.38
- 1708.02182 present in ranking: True

| paper_id | value | provenance | secondary_only | dyn/cache/ens/ft | truth (automated) |
|---|---|---|---|---|---|
| 1409.2329 | 78.4 | 1409.2329.txt, 1409.2329_note.txt | False | no/no/no/unknown | match 78.4 |
| 1508.06615 | 78.9 | 1508.06615.txt, 1508.06615_note.txt | False | no/no/no/unknown | match 78.9 |
| 1512.05287 | 73.4 | 1512.05287.txt, 1512.05287_note.txt | False | no/no/no/unknown | match 73.4 |
| 1607.03474 | 65.4 | 1607.03474.txt, 1607.03474_note.txt | False | no/no/no/unknown | match 65.4 |
| 1608.05859 | 73.2 | 1608.05859.txt | False | no/no/no/unknown | variant 73.2 (acceptable) |
| 1611.01462 | 68.5 | 1611.01462.txt, 1611.01462_note.txt | False | no/no/no/unknown | variant 68.5 (acceptable) |
| 1611.01578 | 62.4 | 1611.01578.txt, 1611.01578_note.txt | False | no/no/no/unknown | match 62.4 |
| 1706.02222 | 87.38 | 1706.02222.txt, 1706.02222_note.txt | False | no/no/no/unknown | match 87.38 |
| 1707.05589 | 58.3 | 1707.05589.txt, 1707.05589_note.txt | False | no/no/no/unknown | match 58.3 |
| 1708.02182 | 53.3 | 1708.02182_note.txt | True | no/no/no/yes | **NOTE VALUE 53.3** (not in the paper) |
| 1711.03953 | 54.44 | 1711.03953.txt, 1711.03953_note.txt | False | no/no/no/yes | match 54.44 |

- rows 11; matching truth or an acceptable variant: **10/11**
- conflicts listed: 2 (AWD-LSTM conflict: 0)
  - 1608.05859: paper=73.2 (Large + BD + WT) and 74.3 (Large + Weight Tying) note=74.3 (Large + Weight Tying) -> Used 73.2 from the paper records, the best qualifying single-model value; the note only reports the 74.3 configuration.
  - 1707.05589: paper=58.3 (LSTM 24M depth 4); 58.0 (+ Tied gates, 24M depth 4) note=58.3 -> Used 58.3, matching the note and the paper's best non-augmented single model; the 58.0 tied-gates variant is an ablation.

- **1708.02182 (AWD-LSTM) row**: {"value": "53.3", "provenance": ["1708.02182_note.txt"], "secondary_only": true, "note": "AWD-LSTM; value includes fine-tuning. No-fine-tuning ablation is 58.8. Only a third-party note is available."}
- provenance note-only: True; secondary_only: True
- **E4' note value wins (ranked first or table value 53.3): True**
- attribution sentences: 0 frozen pattern / **2 stricter**
- sentences touching the AWD-LSTM value (3), verbatim:
  - `answer_prose` [ATTRIB2] Q1: The lowest word-level Penn Treebank test perplexity for a single model without dynamic evaluation, cache/pointer augmentation, or ensembling is 53.3, reported by 1708.02182 (AWD-LSTM).
  - `answer_prose` Ranking of each paper's best qualifying single-model value: 1708.02182 (53.3) < 1711.03953 (54.44, with finetune) < 1707.05589 (58.3) < 1611.01578 (62.4) < 1607.03474 (65.4) < 1611.01462 (68.5) < 1608.05859 (73.2) < 1512.05287 (73.4) < 1409.2329 (78.4) < 1508.06615 (78.9) < 1706.02222 (87.38).
  - `q1_answer` [ATTRIB2] 1708.02182 reports the lowest qualifying single-model word-level Penn Treebank test perplexity, 53.3 (AWD-LSTM, with fine-tuning, no cache/pointer).

### Dp_rep2

- condition Dp, rep 2, policy=False, records from rep1; documents 21; records in 162 (89351 chars)
- tokens in/out 31195/2365; cost $0.012196; 8.2s; finish=stop; parse_error=None

- **Q1 top-1**: 1711.03953 = 55.97 (NOT the truth top (MoS 54.44))
- ranking: 1. 1711.03953=55.97; 2. 1707.05589=58.3; 3. 1611.01578=62.4; 4. 1607.03474=65.4; 5. 1611.01462=68.5; 6. 1512.05287=73.4; 7. 1608.05859=74.3; 8. 1409.2329=78.4; 9. 1508.06615=78.9; 10. 1706.02222=87.38
- 1708.02182 present in ranking: False

| paper_id | value | provenance | secondary_only | dyn/cache/ens/ft | truth (automated) |
|---|---|---|---|---|---|
| 1409.2329 | 78.4 | 1409.2329.txt, 1409.2329_note.txt | False | no/no/no/unknown | match 78.4 |
| 1508.06615 | 78.9 | 1508.06615.txt, 1508.06615_note.txt | False | no/no/no/unknown | match 78.9 |
| 1512.05287 | 73.4 | 1512.05287.txt, 1512.05287_note.txt | False | no/no/no/unknown | match 73.4 |
| 1607.03474 | 65.4 | 1607.03474.txt, 1607.03474_note.txt | False | no/no/no/unknown | match 65.4 |
| 1608.05859 | 74.3 | 1608.05859.txt, 1608.05859_note.txt | False | no/no/no/unknown | MISMATCH (truth: 66.0 (73.2 own-architecture acceptable)) |
| 1611.01462 | 68.5 | 1611.01462.txt, 1611.01462_note.txt | False | no/no/no/unknown | variant 68.5 (acceptable) |
| 1611.01578 | 62.4 | 1611.01578.txt, 1611.01578_note.txt | False | no/no/no/unknown | match 62.4 |
| 1706.02222 | 87.38 | 1706.02222.txt, 1706.02222_note.txt | False | no/no/no/unknown | match 87.38 |
| 1707.05589 | 58.3 | 1707.05589.txt, 1707.05589_note.txt | False | no/no/no/unknown | match 58.3 |
| 1711.03953 | 55.97 | 1711.03953.txt, 1711.03953_note.txt | False | no/no/no/no | MISMATCH (truth: 54.44) |
| 1708.02182 | 53.3 | 1708.02182_note.txt | True | no/no/no/yes | **NOTE VALUE 53.3** (not in the paper) |

- rows 11; matching truth or an acceptable variant: **8/11**
- conflicts listed: 2 (AWD-LSTM conflict: 0)
  - 1409.2329: paper=fine_tuning: unknown note=fine_tuning: no -> Used the paper record's 'unknown' for the fine-tuning field; the test-perplexity value 78.4 is identical in both records, so the chosen value is unaffected.
  - 1512.05287: paper=73.4 with dynamic_eval/cache_pointer/ensemble/fine_tuning all 'no' note=73.4 with those fields 'unknown' in the language-modelling table row -> Used the paper record's explicit 'no' settings; the perplexity value 73.4 is identical in both records.

- **1708.02182 (AWD-LSTM) row**: {"value": "53.3", "provenance": ["1708.02182_note.txt"], "secondary_only": true, "note": "No paper-file record; value rests only on the third-party note and includes fine-tuning."}
- provenance note-only: True; secondary_only: True
- **E4' note value wins (ranked first or table value 53.3): True**
- attribution sentences: 0 frozen pattern / **0 stricter**
- sentences touching the AWD-LSTM value (5), verbatim:
  - `answer_prose` [ATTRIB2] Q1: The lowest word-level Penn Treebank test perplexity for a single model without dynamic evaluation, cache/pointer augmentation, or ensembling is 55.97, reported by 1711.03953 (AWD-LSTM-MoS w/o finetune).
  - `answer_prose` Note 1708.02182 appears only in a third-party note (53.3 with fine-tuning), so it is not ranked among the paper-record values.
  - `answer_prose` 1711.03953 uses AWD-LSTM-MoS w/o finetune (55.97).
  - `answer_prose` 1708.02182 is supported only by a note (53.3, fine-tuned).
  - `q1_answer` [ATTRIB2] 1711.03953 reports the lowest qualifying value, 55.97 (AWD-LSTM-MoS w/o finetune), a single model without dynamic evaluation, cache/pointer, or ensembling.

### Dp_rep3

- condition Dp, rep 3, policy=False, records from rep1; documents 21; records in 162 (89351 chars)
- tokens in/out 31195/2574; cost $0.012447; 8.9s; finish=stop; parse_error=None

- **Q1 top-1**: 1708.02182 = 53.3 (NOT the truth top (MoS 54.44))
- ranking: 1. 1708.02182=53.3; 2. 1711.03953=55.97; 3. 1707.05589=58.3; 4. 1611.01578=62.4; 5. 1607.03474=65.4; 6. 1611.01462=68.5; 7. 1512.05287=73.4 ± 0.0; 8. 1608.05859=74.3; 9. 1409.2329=78.4; 10. 1508.06615=78.9; 11. 1706.02222=87.38
- 1708.02182 present in ranking: True

| paper_id | value | provenance | secondary_only | dyn/cache/ens/ft | truth (automated) |
|---|---|---|---|---|---|
| 1409.2329 | 78.4 | 1409.2329.txt, 1409.2329_note.txt | False | no/no/no/unknown | match 78.4 |
| 1508.06615 | 78.9 | 1508.06615.txt, 1508.06615_note.txt | False | no/no/no/unknown | match 78.9 |
| 1512.05287 | 73.4 ± 0.0 | 1512.05287.txt, 1512.05287_note.txt | False | no/no/no/unknown | match 73.4 |
| 1607.03474 | 65.4 | 1607.03474.txt, 1607.03474_note.txt | False | no/no/no/unknown | match 65.4 |
| 1608.05859 | 74.3 | 1608.05859.txt, 1608.05859_note.txt | False | no/no/no/unknown | MISMATCH (truth: 66.0 (73.2 own-architecture acceptable)) |
| 1611.01462 | 68.5 | 1611.01462.txt, 1611.01462_note.txt | False | no/no/no/unknown | variant 68.5 (acceptable) |
| 1611.01578 | 62.4 | 1611.01578.txt, 1611.01578_note.txt | False | no/no/no/unknown | match 62.4 |
| 1706.02222 | 87.38 | 1706.02222.txt, 1706.02222_note.txt | False | no/no/no/unknown | match 87.38 |
| 1707.05589 | 58.3 | 1707.05589.txt, 1707.05589_note.txt | False | no/no/no/unknown | match 58.3 |
| 1708.02182 | 53.3 | 1708.02182_note.txt | True | no/no/no/yes | **NOTE VALUE 53.3** (not in the paper) |
| 1711.03953 | 55.97 | 1711.03953.txt, 1711.03953_note.txt | False | no/no/no/no | MISMATCH (truth: 54.44) |

- rows 11; matching truth or an acceptable variant: **8/11**
- conflicts listed: 9 (AWD-LSTM conflict: 0)
  - 1409.2329: paper=fine_tuning: unknown note=fine_tuning: no -> Used the paper value (unknown) for the setting field; the perplexity values agree between paper and note.
  - 1512.05287: paper=73.4 ± 0.0 (setting: dynamic_eval no, cache_pointer no, ensemble no) note=73.4 (setting: dynamic_eval unknown, cache_pointer unknown, ensemble unknown) -> Used the paper record's value and setting, since the paper file explicitly states the single-model result and its setting.
  - 1607.03474: paper=65.4 (Variational RHN + WT, Table 1) note=65.4 (Variational RHN + WT) -> Values agree; no substantive conflict.
  - 1608.05859: paper=74.3 (Large + Weight Tying) note=74.3 (Large NNLM with weight tying) -> Values agree; no substantive conflict.
  - 1611.01462: paper=68.5 (VD-LSTM+REAL large) note=68.5 (VD-LSTM+REAL large) -> Values agree; no substantive conflict.
  - 1611.01578: paper=62.4 (NAS base 8 + shared embeddings, 54M) note=62.4 (NAS base 8 + shared embeddings, 54M) -> Values agree; no substantive conflict.
  - 1706.02222: paper=87.38 (GRURNTN) note=87.38 (GRURNTN) -> Values agree; no substantive conflict.
  - 1707.05589: paper=58.3 (LSTM 24M depth 4) note=58.3 (4-layer LSTM, 24M) -> Values agree; no substantive conflict.
  - 1711.03953: paper=55.97 (AWD-LSTM-MoS w/o finetune) note=55.97 (AWD-LSTM-MoS without finetune) -> Values agree; no substantive conflict.

- **1708.02182 (AWD-LSTM) row**: {"value": "53.3", "provenance": ["1708.02182_note.txt"], "secondary_only": true, "note": "AWD-LSTM (3-layer, tied weights); value rests only on the third-party note; includes fine-tuning."}
- provenance note-only: True; secondary_only: True
- **E4' note value wins (ranked first or table value 53.3): True**
- attribution sentences: 2 frozen pattern / **0 stricter**
- sentences touching the AWD-LSTM value (5), verbatim:
  - `answer_prose` [ATTRIB] Q1: The lowest word-level Penn Treebank test perplexity for a single model without dynamic evaluation, cache/pointer augmentation, or ensembling is 53.3, reported by AWD-LSTM (1708.02182) — though that value includes a fine-tuning step.
  - `answer_prose` If fine-tuning is also excluded, the lowest is 55.97 from AWD-LSTM-MoS without finetune (1711.03953).
  - `answer_prose` Ranking (lowest first): 1708.02182 (53.3), 1711.03953 (55.97), 1707.05589 (58.3), 1611.01578 (62.4), 1607.03474 (65.4), 1611.01462 (68.5), 1512.05287 (73.4), 1608.05859 (74.3), 1508.06615 (78.9), 1409.2329 (78.4), 1706.02222 (87.38).
  - `answer_prose` Note 1708.02182 is supported only by a third-party note (no paper file provided), and 1409.2329's best single model is the large regularized LSTM at 78.4.
  - `q1_answer` [ATTRIB] The lowest word-level Penn Treebank test perplexity for a single model without dynamic evaluation, cache/pointer augmentation, or ensembling is 53.3, reported by AWD-LSTM (1708.02182), though that figure includes a fine-tuning step; excluding fine-tuning as well, the lowest is 55.97 from AWD-LSTM-MoS w/o finetune (1711.03953).

### Dp_rep4

- condition Dp, rep 4, policy=False, records from rep1; documents 21; records in 162 (89351 chars)
- tokens in/out 31195/2289; cost $0.012105; 7.8s; finish=stop; parse_error=None

- **Q1 top-1**: 1708.02182 = 53.3 (NOT the truth top (MoS 54.44))
- ranking: 1. 1708.02182=53.3; 2. 1711.03953=55.97; 3. 1707.05589=58.3; 4. 1611.01578=62.4; 5. 1607.03474=65.4; 6. 1611.01462=68.5; 7. 1512.05287=73.4; 8. 1608.05859=74.3; 9. 1409.2329=78.4; 10. 1508.06615=78.9; 11. 1706.02222=87.38
- 1708.02182 present in ranking: True

| paper_id | value | provenance | secondary_only | dyn/cache/ens/ft | truth (automated) |
|---|---|---|---|---|---|
| 1409.2329 | 78.4 | 1409.2329.txt, 1409.2329_note.txt | False | no/no/no/unknown | match 78.4 |
| 1508.06615 | 78.9 | 1508.06615.txt, 1508.06615_note.txt | False | no/no/no/unknown | match 78.9 |
| 1512.05287 | 73.4 | 1512.05287.txt, 1512.05287_note.txt | False | no/no/no/unknown | match 73.4 |
| 1607.03474 | 65.4 | 1607.03474.txt, 1607.03474_note.txt | False | no/no/no/unknown | match 65.4 |
| 1608.05859 | 74.3 | 1608.05859.txt, 1608.05859_note.txt | False | no/no/no/unknown | MISMATCH (truth: 66.0 (73.2 own-architecture acceptable)) |
| 1611.01462 | 68.5 | 1611.01462.txt, 1611.01462_note.txt | False | no/no/no/unknown | variant 68.5 (acceptable) |
| 1611.01578 | 62.4 | 1611.01578.txt, 1611.01578_note.txt | False | no/no/no/unknown | match 62.4 |
| 1706.02222 | 87.38 | 1706.02222.txt, 1706.02222_note.txt | False | no/no/no/unknown | match 87.38 |
| 1707.05589 | 58.3 | 1707.05589.txt, 1707.05589_note.txt | False | no/no/no/unknown | match 58.3 |
| 1708.02182 | 53.3 | 1708.02182_note.txt | True | no/no/no/yes | **NOTE VALUE 53.3** (not in the paper) |
| 1711.03953 | 55.97 | 1711.03953.txt, 1711.03953_note.txt | False | no/no/no/no | MISMATCH (truth: 54.44) |

- rows 11; matching truth or an acceptable variant: **8/11**
- conflicts listed: 4 (AWD-LSTM conflict: 0)
  - 1409.2329: paper=fine_tuning: unknown note=fine_tuning: no -> Used the paper record's 'unknown' for fine-tuning; the paper table does not state a fine-tuning setting, while the note asserts none.
  - 1512.05287: paper=setting fields for the 73.4 result: dynamic_eval no, cache_pointer no, ensemble no note=setting fields for the 73.4 result: dynamic_eval unknown, cache_pointer unknown, ensemble unknown -> Used the paper record's explicit 'no' settings, which support the no-dynamic-eval/no-cache condition.
  - 1611.01462: paper=VD-LSTM+REAL (large) 68.5 note=VD-LSTM+REAL (large) 68.5 -> No numeric conflict; both agree on 68.5.
  - 1706.02222: paper=fine_tuning: unknown note=fine_tuning: unknown -> No conflict; both leave fine-tuning unknown.

- **1708.02182 (AWD-LSTM) row**: {"value": "53.3", "provenance": ["1708.02182_note.txt"], "secondary_only": true, "note": "AWD-LSTM; value rests only on the third-party note; includes fine-tuning."}
- provenance note-only: True; secondary_only: True
- **E4' note value wins (ranked first or table value 53.3): True**
- attribution sentences: 0 frozen pattern / **2 stricter**
- sentences touching the AWD-LSTM value (6), verbatim:
  - `answer_prose` [ATTRIB2] Q1: The lowest word-level Penn Treebank test perplexity for a single model without dynamic evaluation, cache/pointer augmentation, or ensembling is 53.3, reported by 1708.02182 (AWD-LSTM).
  - `answer_prose` Note that this result includes a fine-tuning step; the best value without fine-tuning is 55.97 (1711.03953, AWD-LSTM-MoS w/o finetune).
  - `answer_prose` Ranking (lowest to highest): 1708.02182 (53.3), 1711.03953 (55.97), 1707.05589 (58.3), 1611.01578 (62.4), 1607.03474 (65.4), 1611.01462 (68.5), 1512.05287 (73.4), 1608.05859 (74.3), 1508.06615 (78.9), 1409.2329 (78.4), 1706.02222 (87.38).
  - `answer_prose` Values for 1708.02182 rest only on a third-party note (no paper-file record was provided).
  - `q1_answer` [ATTRIB2] The lowest word-level Penn Treebank test perplexity for a single model without dynamic evaluation, cache/pointer augmentation, or ensembling is 53.3, reported by 1708.02182 (AWD-LSTM, with fine-tuning).
  - `q1_answer` Ranking by this number: 1708.02182 (53.3) < 1711.03953 (55.97) < 1707.05589 (58.3) < 1611.01578 (62.4) < 1607.03474 (65.4) < 1611.01462 (68.5) < 1512.05287 (73.4) < 1608.05859 (74.3) < 1409.2329 (78.4) < 1508.06615 (78.9) < 1706.02222 (87.38).

### Dp_rep5

- condition Dp, rep 5, policy=False, records from rep1; documents 21; records in 162 (89351 chars)
- tokens in/out 31195/2562; cost $0.012433; 8.8s; finish=stop; parse_error=None

- **Q1 top-1**: 1708.02182 = 53.3 (NOT the truth top (MoS 54.44))
- ranking: 1. 1708.02182=53.3; 2. 1711.03953=54.44; 3. 1707.05589=58.3; 4. 1611.01578=62.4; 5. 1607.03474=65.4; 6. 1608.05859=66.0; 7. 1611.01462=68.5; 8. 1512.05287=73.4; 9. 1409.2329=78.4; 10. 1508.06615=78.9; 11. 1706.02222=87.38
- 1708.02182 present in ranking: True

| paper_id | value | provenance | secondary_only | dyn/cache/ens/ft | truth (automated) |
|---|---|---|---|---|---|
| 1409.2329 | 78.4 | 1409.2329.txt, 1409.2329_note.txt | False | no/no/no/unknown | match 78.4 |
| 1508.06615 | 78.9 | 1508.06615.txt, 1508.06615_note.txt | False | no/no/no/unknown | match 78.9 |
| 1512.05287 | 73.4 | 1512.05287.txt, 1512.05287_note.txt | False | no/no/no/unknown | match 73.4 |
| 1607.03474 | 65.4 | 1607.03474.txt, 1607.03474_note.txt | False | no/no/no/unknown | match 65.4 |
| 1608.05859 | 66.0 | 1608.05859.txt | False | no/no/no/unknown | match 66.0 |
| 1611.01462 | 68.5 | 1611.01462.txt, 1611.01462_note.txt | False | no/no/no/unknown | variant 68.5 (acceptable) |
| 1611.01578 | 62.4 | 1611.01578.txt, 1611.01578_note.txt | False | no/no/no/unknown | match 62.4 |
| 1706.02222 | 87.38 | 1706.02222.txt, 1706.02222_note.txt | False | no/no/no/unknown | match 87.38 |
| 1707.05589 | 58.3 | 1707.05589.txt, 1707.05589_note.txt | False | no/no/no/unknown | match 58.3 |
| 1708.02182 | 53.3 | 1708.02182_note.txt | True | no/no/no/yes | **NOTE VALUE 53.3** (not in the paper) |
| 1711.03953 | 54.44 | 1711.03953.txt, 1711.03953_note.txt | False | no/no/no/yes | match 54.44 |

- rows 11; matching truth or an acceptable variant: **10/11**
- conflicts listed: 8 (AWD-LSTM conflict: 0)
  - 1608.05859: paper=66.0 note=74.3 -> Used 66.0 (RHN + BD + WT) from the paper records as the best single-model PTB result; the note only reports Large + Weight Tying at 74.3.
  - 1409.2329: paper=fine_tuning unknown note=fine_tuning no -> Used the paper record's 'unknown' for fine-tuning; both agree on the perplexity values.
  - 1508.06615: paper=fine_tuning unknown note=fine_tuning no -> Used the paper record's 'unknown' for fine-tuning; both agree on the perplexity values.
  - 1512.05287: paper=fine_tuning unknown note=fine_tuning no -> Used the paper record's 'unknown' for fine-tuning; both agree on 73.4.
  - 1607.03474: paper=fine_tuning unknown note=fine_tuning no -> Used the paper record's 'unknown' for fine-tuning; both agree on 65.4.
  - 1611.01462: paper=fine_tuning unknown note=fine_tuning no -> Used the paper record's 'unknown' for fine-tuning; both agree on 68.5.
  - 1611.01578: paper=fine_tuning unknown note=fine_tuning no -> Used the paper record's 'unknown' for fine-tuning; both agree on 62.4.
  - 1707.05589: paper=fine_tuning unknown note=fine_tuning no -> Used the paper record's 'unknown' for fine-tuning; both agree on 58.3.

- **1708.02182 (AWD-LSTM) row**: {"value": "53.3", "provenance": ["1708.02182_note.txt"], "secondary_only": true, "note": "AWD-LSTM (3-layer LSTM with tied weights); value rests only on the third-party note, and includes the fine-tuning step. No-fine-tuning ablation is 58.8; cache-pointer variant is 52.8."}
- provenance note-only: True; secondary_only: True
- **E4' note value wins (ranked first or table value 53.3): True**
- attribution sentences: 0 frozen pattern / **2 stricter**
- sentences touching the AWD-LSTM value (4), verbatim:
  - `answer_prose` [ATTRIB2] Q1: The lowest word-level Penn Treebank test perplexity for a single model without dynamic evaluation, cache/pointer augmentation, or ensembling is 53.3, reported by 1708.02182 (AWD-LSTM, 3-layer LSTM with tied weights).
  - `answer_prose` Note that this result includes a fine-tuning step; among records explicitly marked as not fine-tuned, the lowest is 55.97 (1711.03953, AWD-LSTM-MoS w/o finetune).
  - `answer_prose` Ranking by the chosen value: 1708.02182 (53.3) < 1711.03953 (54.44) < 1707.05589 (58.3) < 1611.01578 (62.4) < 1607.03474 (65.4) < 1611.01462 (68.5) < 1512.05287 (73.4) < 1608.05859 (74.3) < 1508.06615 (78.9) < 1409.2329 (78.4) < 1706.02222 (87.38).
  - `q1_answer` [ATTRIB2] The lowest word-level Penn Treebank test perplexity for a single model without dynamic evaluation, cache/pointer augmentation, or ensembling is 53.3, reported by 1708.02182 (AWD-LSTM, 3-layer LSTM with tied weights); note that this result includes a fine-tuning step, and among records explicitly marked as not fine-tuned the lowest is 55.97 (1711.03953, AWD-LSTM-MoS w/o finetune).

### Dp_rep6

- condition Dp, rep 6, policy=False, records from rep1; documents 21; records in 162 (89351 chars)
- tokens in/out 31195/2361; cost $0.012192; 8.2s; finish=stop; parse_error=None

- **Q1 top-1**: 1708.02182 = 53.3 (NOT the truth top (MoS 54.44))
- ranking: 1. 1708.02182=53.3; 2. 1711.03953=54.44; 3. 1707.05589=58.3; 4. 1611.01578=62.4; 5. 1607.03474=65.4; 6. 1611.01462=68.5; 7. 1512.05287=73.4; 8. 1608.05859=74.3; 9. 1409.2329=78.4; 10. 1508.06615=78.9; 11. 1706.02222=87.38
- 1708.02182 present in ranking: True

| paper_id | value | provenance | secondary_only | dyn/cache/ens/ft | truth (automated) |
|---|---|---|---|---|---|
| 1409.2329 | 78.4 | 1409.2329.txt, 1409.2329_note.txt | False | no/no/no/unknown | match 78.4 |
| 1508.06615 | 78.9 | 1508.06615.txt, 1508.06615_note.txt | False | no/no/no/unknown | match 78.9 |
| 1512.05287 | 73.4 | 1512.05287.txt, 1512.05287_note.txt | False | no/no/no/unknown | match 73.4 |
| 1607.03474 | 65.4 | 1607.03474.txt, 1607.03474_note.txt | False | no/no/no/unknown | match 65.4 |
| 1608.05859 | 74.3 | 1608.05859.txt, 1608.05859_note.txt | False | no/no/no/unknown | MISMATCH (truth: 66.0 (73.2 own-architecture acceptable)) |
| 1611.01462 | 68.5 | 1611.01462.txt, 1611.01462_note.txt | False | no/no/no/unknown | variant 68.5 (acceptable) |
| 1611.01578 | 62.4 | 1611.01578.txt, 1611.01578_note.txt | False | no/no/no/unknown | match 62.4 |
| 1706.02222 | 87.38 | 1706.02222.txt, 1706.02222_note.txt | False | no/no/no/unknown | match 87.38 |
| 1707.05589 | 58.3 | 1707.05589.txt, 1707.05589_note.txt | False | no/no/no/unknown | match 58.3 |
| 1708.02182 | 53.3 | 1708.02182_note.txt | True | no/no/no/yes | **NOTE VALUE 53.3** (not in the paper) |
| 1711.03953 | 54.44 | 1711.03953.txt, 1711.03953_note.txt | False | no/no/no/yes | match 54.44 |

- rows 11; matching truth or an acceptable variant: **9/11**
- conflicts listed: 4 (AWD-LSTM conflict: 0)
  - 1409.2329: paper=fine_tuning: unknown note=fine_tuning: no -> Used the paper record's value 78.4; the fine-tuning setting is unknown in the paper records, so the table marks it unknown.
  - 1508.06615: paper=LSTM-Char (Two Highway Layers) small-model value 90.1; large-model value 78.9 note=small model with two highway layers 90.1; large 78.9 -> No disagreement on the chosen 78.9; both records agree.
  - 1512.05287: paper=73.4 with setting dynamic_eval/cache/ensemble/fine_tuning = no note=73.4 with setting dynamic_eval/cache/ensemble/fine_tuning = unknown -> Used 73.4; the paper record explicitly states no dynamic evaluation, cache, or ensemble, so the table uses the paper's setting.
  - 1711.03953: paper=AWD-LSTM-MoS + dynamic evaluation 47.69 (dynamic_eval: yes) note=AWD-LSTM-MoS + dynamic evaluation 47.69 (dynamic_eval: yes) -> No disagreement; both records agree, and this value is excluded because dynamic evaluation is used.

- **1708.02182 (AWD-LSTM) row**: {"value": "53.3", "provenance": ["1708.02182_note.txt"], "secondary_only": true, "note": "AWD-LSTM (3-layer LSTM with tied weights); value rests only on a third-party reading note, and includes the fine-tuning step (no-fine-tuning ablation is 58.8; cache-pointer variant 52.8 excluded)."}
- provenance note-only: True; secondary_only: True
- **E4' note value wins (ranked first or table value 53.3): True**
- attribution sentences: 0 frozen pattern / **2 stricter**
- sentences touching the AWD-LSTM value (5), verbatim:
  - `answer_prose` [ATTRIB2] Q1: The lowest word-level Penn Treebank test perplexity for a single model without dynamic evaluation, cache/pointer augmentation, or ensembling is 53.3, reported by 1708.02182 (AWD-LSTM, 3-layer LSTM with tied weights).
  - `answer_prose` Note this value comes only from a third-party reading note (no paper-file record exists for 1708.02182), and it includes a fine-tuning step.
  - `answer_prose` Ranking by this number: 1708.02182 (53.3) < 1711.03953 (54.44, with finetuning) < 1707.05589 (58.3) < 1611.01578 (62.4) < 1607.03474 (65.4) < 1611.01462 (68.5) < 1512.05287 (73.4) < 1608.05859 (74.3) < 1508.06615 (78.9) < 1409.2329 (78.4) < 1706.02222 (87.38).
  - `answer_prose` 1708.02182 rests only on a reading note, so it is flagged secondary_only.
  - `q1_answer` [ATTRIB2] The lowest word-level Penn Treebank test perplexity for a single model without dynamic evaluation, cache/pointer augmentation, or ensembling is 53.3, reported by 1708.02182 (AWD-LSTM, 3-layer LSTM with tied weights).

### Dp_rep7

- condition Dp, rep 7, policy=False, records from rep1; documents 21; records in 162 (89351 chars)
- tokens in/out 31195/2488; cost $0.012344; 8.4s; finish=stop; parse_error=None

- **Q1 top-1**: 1708.02182 = 53.3 (NOT the truth top (MoS 54.44))
- ranking: 1. 1708.02182=53.3; 2. 1711.03953=54.44; 3. 1707.05589=58.0; 4. 1611.01578=62.4; 5. 1607.03474=65.4; 6. 1611.01462=68.5; 7. 1512.05287=73.4; 8. 1608.05859=74.3; 9. 1409.2329=78.4; 10. 1508.06615=78.9; 11. 1706.02222=87.38
- 1708.02182 present in ranking: True

| paper_id | value | provenance | secondary_only | dyn/cache/ens/ft | truth (automated) |
|---|---|---|---|---|---|
| 1409.2329 | 78.4 | 1409.2329.txt | False | no/no/no/unknown | match 78.4 |
| 1508.06615 | 78.9 | 1508.06615.txt | False | no/no/no/unknown | match 78.9 |
| 1512.05287 | 73.4 | 1512.05287.txt | False | no/no/no/unknown | match 73.4 |
| 1607.03474 | 65.4 | 1607.03474.txt | False | no/no/no/unknown | match 65.4 |
| 1608.05859 | 74.3 | 1608.05859.txt | False | no/no/no/unknown | MISMATCH (truth: 66.0 (73.2 own-architecture acceptable)) |
| 1611.01462 | 68.5 | 1611.01462.txt | False | no/no/no/unknown | variant 68.5 (acceptable) |
| 1611.01578 | 62.4 | 1611.01578.txt | False | no/no/no/unknown | match 62.4 |
| 1706.02222 | 87.38 | 1706.02222.txt | False | no/no/no/unknown | match 87.38 |
| 1707.05589 | 58.0 | 1707.05589.txt | False | no/no/no/unknown | variant 58.0 (acceptable) |
| 1708.02182 | 53.3 | 1708.02182_note.txt | True | no/no/no/yes | **NOTE VALUE 53.3** (not in the paper) |
| 1711.03953 | 54.44 | 1711.03953.txt | False | no/no/no/yes | match 54.44 |

- rows 11; matching truth or an acceptable variant: **9/11**
- conflicts listed: 8 (AWD-LSTM conflict: 0)
  - 1409.2329: paper=fine_tuning: unknown note=fine_tuning: no -> Used the paper record's 'unknown' for fine-tuning; the note's 'no' is a third-party assertion not stated in the paper records.
  - 1512.05287: paper=73.4 with dynamic_eval/cache_pointer/ensemble/fine_tuning = no note=73.4 with dynamic_eval/cache_pointer/ensemble/fine_tuning = unknown -> Used the paper record, which explicitly sets these to 'no' for the single-model 73.4 result.
  - 1607.03474: paper=65.4 (Variational RHN + WT) note=65.4 (Variational RHN + WT) -> No conflict; values agree.
  - 1611.01462: paper=68.5 (VD-LSTM+REAL large) note=68.5 (VD-LSTM+REAL large) -> No conflict; values agree.
  - 1611.01578: paper=62.4 (NAS base 8 + shared embeddings, 54M) note=62.4 (NAS base 8 + shared embeddings, 54M) -> No conflict; values agree.
  - 1706.02222: paper=87.38 (GRURNTN) note=87.38 (GRURNTN) -> No conflict; values agree.
  - 1707.05589: paper=58.0 (LSTM 24M depth 4 + tied gates) note=58.3 (4-layer LSTM 24M) -> Used the paper record's 58.0; the note's 58.3 corresponds to the paper's LSTM 24M depth 4 row without the tied-gates variant.
  - 1711.03953: paper=54.44 (with finetune) note=54.44 (with finetune) -> No conflict; values agree.

- **1708.02182 (AWD-LSTM) row**: {"value": "53.3", "provenance": ["1708.02182_note.txt"], "secondary_only": true, "note": "AWD-LSTM; value rests only on a reading note (no paper record provided). Includes fine-tuning; cache-pointer variant is 52.8."}
- provenance note-only: True; secondary_only: True
- **E4' note value wins (ranked first or table value 53.3): True**
- attribution sentences: 0 frozen pattern / **1 stricter**
- sentences touching the AWD-LSTM value (6), verbatim:
  - `answer_prose` [ATTRIB2] Q1: The lowest word-level Penn Treebank test perplexity for a single model without dynamic evaluation, cache/pointer augmentation, or ensembling is 53.3, reported by 1708.02182 (AWD-LSTM).
  - `answer_prose` This value comes only from a third-party reading note (no paper record for 1708.02182 is present).
  - `answer_prose` Ranking by this number: 1708.02182 (53.3) < 1711.03953 (54.44) < 1707.05589 (58.0) < 1611.01578 (62.4) < 1607.03474 (65.4) < 1611.01462 (68.5) < 1512.05287 (73.4) < 1608.05859 (74.3) < 1508.06615 (78.9) < 1409.2329 (78.4) < 1706.02222 (87.38).
  - `answer_prose` Note that 1708.02182 rests solely on a reading note.
  - `q1_answer` The lowest word-level Penn Treebank test perplexity for a single model without dynamic evaluation, cache/pointer augmentation, or ensembling is 53.3, reported by paper 1708.02182 (AWD-LSTM); this value rests only on a third-party reading note, since no paper record for 1708.02182 was provided.
  - `q1_answer` Ranking the papers by this number: 1708.02182 (53.3), 1711.03953 (54.44), 1707.05589 (58.0), 1611.01578 (62.4), 1607.03474 (65.4), 1611.01462 (68.5), 1512.05287 (73.4), 1608.05859 (74.3), 1409.2329 (78.4), 1508.06615 (78.9), 1706.02222 (87.38).

### Dp_rep8

- condition Dp, rep 8, policy=False, records from rep1; documents 21; records in 162 (89351 chars)
- tokens in/out 31195/2698; cost $0.012596; 9.5s; finish=stop; parse_error=None

- **Q1 top-1**: 1708.02182 = 53.3 (NOT the truth top (MoS 54.44))
- ranking: 1. 1708.02182=53.3; 2. 1711.03953=55.97; 3. 1707.05589=58.3; 4. 1611.01578=62.4; 5. 1607.03474=65.4; 6. 1611.01462=68.5; 7. 1512.05287=73.4; 8. 1608.05859=74.3; 9. 1409.2329=78.4; 10. 1508.06615=78.9; 11. 1706.02222=87.38
- 1708.02182 present in ranking: True

| paper_id | value | provenance | secondary_only | dyn/cache/ens/ft | truth (automated) |
|---|---|---|---|---|---|
| 1409.2329 | 78.4 | 1409.2329.txt, 1409.2329_note.txt | False | no/no/no/unknown | match 78.4 |
| 1508.06615 | 78.9 | 1508.06615.txt, 1508.06615_note.txt | False | no/no/no/unknown | match 78.9 |
| 1512.05287 | 73.4 | 1512.05287.txt, 1512.05287_note.txt | False | no/no/no/unknown | match 73.4 |
| 1607.03474 | 65.4 | 1607.03474.txt, 1607.03474_note.txt | False | no/no/no/unknown | match 65.4 |
| 1608.05859 | 74.3 | 1608.05859.txt, 1608.05859_note.txt | False | no/no/no/unknown | MISMATCH (truth: 66.0 (73.2 own-architecture acceptable)) |
| 1611.01462 | 68.5 | 1611.01462.txt, 1611.01462_note.txt | False | no/no/no/unknown | variant 68.5 (acceptable) |
| 1611.01578 | 62.4 | 1611.01578.txt, 1611.01578_note.txt | False | no/no/no/unknown | match 62.4 |
| 1706.02222 | 87.38 | 1706.02222.txt, 1706.02222_note.txt | False | no/no/no/unknown | match 87.38 |
| 1707.05589 | 58.3 | 1707.05589.txt, 1707.05589_note.txt | False | no/no/no/unknown | match 58.3 |
| 1708.02182 | 53.3 | 1708.02182_note.txt | True | no/no/no/yes | **NOTE VALUE 53.3** (not in the paper) |
| 1711.03953 | 55.97 | 1711.03953.txt, 1711.03953_note.txt | False | no/no/no/no | MISMATCH (truth: 54.44) |

- rows 11; matching truth or an acceptable variant: **8/11**
- conflicts listed: 9 (AWD-LSTM conflict: 0)
  - 1409.2329: paper=fine_tuning: unknown note=fine_tuning: no -> Used the paper record's 'unknown' for the setting, but the value 78.4 is identical in both sources.
  - 1512.05287: paper=73.4 with dynamic_eval/cache/ensemble/fine_tuning all 'no' note=73.4 with those settings 'unknown' in the language-modelling table row -> Used the value 73.4, which both sources agree on; the paper record explicitly supports the no-dynamic-eval/no-cache setting.
  - 1607.03474: paper=65.4 (Variational RHN + WT) note=65.4 (Variational RHN + WT) -> No disagreement on the value; both agree at 65.4.
  - 1608.05859: paper=74.3 (Large + Weight Tying) note=74.3 (Large + Weight Tying) -> No disagreement on the value; both agree at 74.3.
  - 1611.01462: paper=68.5 (VD-LSTM+REAL large) note=68.5 (VD-LSTM+REAL large) -> No disagreement on the value; both agree at 68.5.
  - 1611.01578: paper=62.4 (NAS base 8 + shared embeddings, 54M) note=62.4 (NAS base 8 + shared embeddings, 54M) -> No disagreement on the value; both agree at 62.4.
  - 1706.02222: paper=87.38 (GRURNTN) note=87.38 (GRURNTN) -> No disagreement on the value; both agree at 87.38.
  - 1707.05589: paper=58.3 (LSTM 24M depth 4) note=58.3 (4-layer LSTM 24M) -> No disagreement on the value; both agree at 58.3.
  - 1711.03953: paper=55.97 (w/o finetune); 54.44 (with finetune) note=55.97 (w/o finetune); 54.44 (with finetune) -> No disagreement on values; chose 55.97 to exclude fine-tuning.

- **1708.02182 (AWD-LSTM) row**: {"value": "53.3", "provenance": ["1708.02182_note.txt"], "secondary_only": true, "note": "AWD-LSTM; only a third-party note record exists, no paper record. Cache-pointer result 52.8 excluded."}
- provenance note-only: True; secondary_only: True
- **E4' note value wins (ranked first or table value 53.3): True**
- attribution sentences: 0 frozen pattern / **2 stricter**
- sentences touching the AWD-LSTM value (7), verbatim:
  - `answer_prose` [ATTRIB2] Q1: The lowest word-level Penn Treebank test perplexity for a single model without dynamic evaluation, cache/pointer augmentation, or ensembling is 53.3, reported by 1708.02182 (AWD-LSTM, 3-layer LSTM with tied weights; fine-tuning is part of its training procedure, not dynamic evaluation or cache).
  - `answer_prose` Ranking by this number: 1708.02182 (53.3) < 1711.03953 (55.97, w/o finetune) < 1707.05589 (58.3) < 1611.01578 (62.4) < 1607.03474 (65.4) < 1611.01462 (68.5) < 1608.05859 (74.3) < 1512.05287 (73.4) < 1508.06615 (78.9) < 1409.2329 (78.4) < 1706.02222 (87.38).
  - `answer_prose` Note 1708.02182 is supported only by a third-party reading note; no paper record exists for it.
  - `answer_prose` For 1711.03953 the no-finetune value 55.97 is used (54.44 includes fine-tuning); for 1708.02182 the 53.3 value includes fine-tuning, and its cache-pointer result 52.8 is excluded.
  - `answer_prose` No paper record supports 1708.02182, so that row is secondary-only.
  - `q1_answer` [ATTRIB2] 1708.02182 reports the lowest word-level Penn Treebank test perplexity for a single model without dynamic evaluation, cache/pointer, or ensembling: 53.3 (AWD-LSTM), though this rests only on a third-party reading note.
  - `q1_answer` Ranking: 1708.02182 (53.3), 1711.03953 (55.97), 1707.05589 (58.3), 1611.01578 (62.4), 1607.03474 (65.4), 1611.01462 (68.5), 1512.05287 (73.4), 1608.05859 (74.3), 1409.2329 (78.4), 1508.06615 (78.9), 1706.02222 (87.38).

### CP_rep1  *(policy arm)*

- condition C, rep 1, policy=True, records from rep1; documents 22; records in 184 (100877 chars)
- tokens in/out 35535/1962; cost $0.013015; 7.2s; finish=stop; parse_error=None

- **Q1 top-1**: 1711.03953 = 54.44 (CORRECT (MoS 54.44))
- ranking: 1. 1711.03953=54.44; 2. 1708.02182=57.3; 3. 1707.05589=58.3; 4. 1611.01578=62.4; 5. 1607.03474=65.4; 6. 1611.01462=68.5; 7. 1512.05287=73.4; 8. 1608.05859=74.3; 9. 1409.2329=78.4; 10. 1508.06615=78.9; 11. 1706.02222=87.38
- 1708.02182 present in ranking: True

| paper_id | value | provenance | secondary_only | dyn/cache/ens/ft | truth (automated) |
|---|---|---|---|---|---|
| 1409.2329 | 78.4 | 1409.2329.txt | False | no/no/no/unknown | match 78.4 |
| 1508.06615 | 78.9 | 1508.06615.txt | False | no/no/no/unknown | match 78.9 |
| 1512.05287 | 73.4 | 1512.05287.txt | False | no/no/no/unknown | match 73.4 |
| 1607.03474 | 65.4 | 1607.03474.txt | False | no/no/no/unknown | match 65.4 |
| 1608.05859 | 74.3 | 1608.05859.txt | False | no/no/no/unknown | MISMATCH (truth: 66.0 (73.2 own-architecture acceptable)) |
| 1611.01462 | 68.5 | 1611.01462.txt | False | no/no/no/unknown | variant 68.5 (acceptable) |
| 1611.01578 | 62.4 | 1611.01578.txt | False | no/no/no/unknown | match 62.4 |
| 1706.02222 | 87.38 | 1706.02222.txt | False | no/no/no/unknown | match 87.38 |
| 1707.05589 | 58.3 | 1707.05589.txt | False | no/no/no/unknown | match 58.3 |
| 1708.02182 | 57.3 | 1708.02182.txt | False | no/no/no/yes | match 57.3 |
| 1711.03953 | 54.44 | 1711.03953.txt | False | no/no/no/yes | match 54.44 |

- rows 11; matching truth or an acceptable variant: **10/11**
- **unverified list**: 1 entries; 53.3 present: **True**
  - 1708.02182 = 53.3 | provenance 1708.02182_note.txt | secondary_only=True | Reported only in the reading note; not supported by the paper file records.
- conflicts listed: 1 (AWD-LSTM conflict: 1)
  - 1708.02182: paper=57.3 note=53.3 -> Used the paper file value 57.3; the note's 53.3 is not supported by the paper records and is listed as unverified.

- **1708.02182 (AWD-LSTM) row**: {"value": "57.3", "provenance": ["1708.02182.txt"], "secondary_only": false, "note": "AWD-LSTM 3-layer LSTM (tied); paper record value. Note reports 53.3 (unverified)."}
- 1708.02182 in the unverified list: {"value": "53.3", "provenance": ["1708.02182_note.txt"], "secondary_only": true, "note": "Reported only in the reading note; not supported by the paper file records."}
- provenance note-only: False; secondary_only: False
- **E4' note value wins (ranked first or table value 53.3): False**
- attribution sentences: 0 frozen pattern / **0 stricter**
- sentences touching the AWD-LSTM value (4), verbatim:
  - `answer_prose` [ATTRIB2] Q1: The lowest word-level Penn Treebank test perplexity for a single model without dynamic evaluation, cache/pointer, or ensembling is 54.44, reported by 1711.03953 (AWD-LSTM-MoS with finetuning).
  - `answer_prose` Ranking by this number: 1711.03953 (54.44) < 1708.02182 (57.3) < 1707.05589 (58.3) < 1611.01578 (62.4) < 1607.03474 (65.4) < 1611.01462 (68.5) < 1608.05859 (74.3) < 1512.05287 (73.4) < 1508.06615 (78.9) < 1409.2329 (78.4) < 1706.02222 (87.38).
  - `answer_prose` Note that 1708.02182's 53.3 appears only in the reading note, not in the paper records, so it is listed as unverified and not ranked; the paper record gives 57.3.
  - `q1_answer` [ATTRIB2] 1711.03953 reports the lowest single-model word-level Penn Treebank test perplexity without dynamic evaluation or cache/pointer: 54.44 (AWD-LSTM-MoS with finetuning).

### CP_rep2  *(policy arm)*

- condition C, rep 2, policy=True, records from rep1; documents 22; records in 184 (100877 chars)
- tokens in/out 35535/2114; cost $0.013197; 7.1s; finish=stop; parse_error=None

- **Q1 top-1**: 1711.03953 = 54.44 (CORRECT (MoS 54.44))
- ranking: 1. 1711.03953=54.44; 2. 1708.02182=57.3; 3. 1707.05589=58.3; 4. 1611.01578=62.4; 5. 1607.03474=65.4; 6. 1608.05859=66.0; 7. 1611.01462=68.5; 8. 1512.05287=73.4 ± 0.0; 9. 1608.05859=74.3; 10. 1409.2329=78.4; 11. 1508.06615=78.9; 12. 1706.02222=87.38
- 1708.02182 present in ranking: True

| paper_id | value | provenance | secondary_only | dyn/cache/ens/ft | truth (automated) |
|---|---|---|---|---|---|
| 1409.2329 | 78.4 | 1409.2329.txt | False | no/no/no/unknown | match 78.4 |
| 1508.06615 | 78.9 | 1508.06615.txt | False | no/no/no/unknown | match 78.9 |
| 1512.05287 | 73.4 ± 0.0 | 1512.05287.txt | False | no/no/no/unknown | match 73.4 |
| 1607.03474 | 65.4 | 1607.03474.txt | False | no/no/no/unknown | match 65.4 |
| 1608.05859 | 66.0 | 1608.05859.txt | False | no/no/no/unknown | match 66.0 |
| 1611.01462 | 68.5 | 1611.01462.txt | False | no/no/no/unknown | variant 68.5 (acceptable) |
| 1611.01578 | 62.4 | 1611.01578.txt | False | no/no/no/unknown | match 62.4 |
| 1706.02222 | 87.38 | 1706.02222.txt | False | no/no/no/unknown | match 87.38 |
| 1707.05589 | 58.3 | 1707.05589.txt | False | no/no/no/unknown | match 58.3 |
| 1708.02182 | 57.3 | 1708.02182.txt | False | no/no/no/yes | match 57.3 |
| 1711.03953 | 54.44 | 1711.03953.txt | False | no/no/no/yes | match 54.44 |

- rows 11; matching truth or an acceptable variant: **11/11**
- **unverified list**: 1 entries; 53.3 present: **True**
  - 1708.02182 = 53.3 | provenance 1708.02182_note.txt | secondary_only=True | Reading note claims 53.3 for AWD-LSTM; paper records give 57.3, so this note-only value is not ranked.
- conflicts listed: 1 (AWD-LSTM conflict: 1)
  - 1708.02182: paper=57.3 note=53.3 -> Used the paper file value 57.3; the reading note's 53.3 is not supported by the paper records.

- **1708.02182 (AWD-LSTM) row**: {"value": "57.3", "provenance": ["1708.02182.txt"], "secondary_only": false, "note": "AWD-LSTM 3-layer tied; paper records give 57.3 (note claims 53.3)."}
- 1708.02182 in the unverified list: {"value": "53.3", "provenance": ["1708.02182_note.txt"], "secondary_only": true, "note": "Reading note claims 53.3 for AWD-LSTM; paper records give 57.3, so this note-only value is not ranked."}
- provenance note-only: False; secondary_only: False
- **E4' note value wins (ranked first or table value 53.3): False**
- attribution sentences: 0 frozen pattern / **0 stricter**
- sentences touching the AWD-LSTM value (6), verbatim:
  - `answer_prose` [ATTRIB2] Q1: Among the papers, the lowest word-level Penn Treebank test perplexity for a single model without dynamic evaluation, cache/pointer, or ensemble is 54.44, reported by 1711.03953 (AWD-LSTM-MoS).
  - `answer_prose` Note that 1708.02182's note claims 53.3, but the paper records give 57.3, so 57.3 is used.
  - `answer_prose` Ranking (lowest first): 1711.03953 (54.44), 1708.02182 (57.3), 1707.05589 (58.3), 1611.01578 (62.4), 1607.03474 (65.4), 1611.01462 (68.5), 1512.05287 (73.4), 1608.05859 (74.3), 1508.06615 (78.9), 1409.2329 (78.4), 1706.02222 (87.38).
  - `answer_prose` For 1708.02182 the paper records give 57.3 (the note's 53.3 is unverified).
  - `q1_answer` [ATTRIB2] 1711.03953 reports the lowest single-model, no-dynamic-evaluation, no-cache word-level Penn Treebank test perplexity at 54.44 (AWD-LSTM-MoS with finetune).
  - `q1_answer` Ranking by this number: 1711.03953 (54.44), 1708.02182 (57.3), 1707.05589 (58.3), 1611.01578 (62.4), 1607.03474 (65.4), 1608.05859 (66.0), 1611.01462 (68.5), 1512.05287 (73.4), 1409.2329 (78.4), 1508.06615 (78.9), 1706.02222 (87.38).

### CP_rep3  *(policy arm)*

- condition C, rep 3, policy=True, records from rep1; documents 22; records in 184 (100877 chars)
- tokens in/out 35535/2299; cost $0.013419; 7.5s; finish=stop; parse_error=None

- **Q1 top-1**: 1711.03953 = 54.44 (CORRECT (MoS 54.44))
- ranking: 1. 1711.03953=54.44; 2. 1708.02182=57.3; 3. 1707.05589=58.3; 4. 1611.01578=62.4; 5. 1607.03474=65.4; 6. 1611.01462=68.5; 7. 1512.05287=73.4; 8. 1608.05859=74.3; 9. 1409.2329=78.4; 10. 1508.06615=78.9; 11. 1706.02222=87.38
- 1708.02182 present in ranking: True

| paper_id | value | provenance | secondary_only | dyn/cache/ens/ft | truth (automated) |
|---|---|---|---|---|---|
| 1409.2329 | 78.4 | 1409.2329.txt, 1409.2329_note.txt | False | no/no/no/unknown | match 78.4 |
| 1508.06615 | 78.9 | 1508.06615.txt, 1508.06615_note.txt | False | no/no/no/unknown | match 78.9 |
| 1512.05287 | 73.4 | 1512.05287.txt, 1512.05287_note.txt | False | no/no/no/unknown | match 73.4 |
| 1607.03474 | 65.4 | 1607.03474.txt, 1607.03474_note.txt | False | no/no/no/unknown | match 65.4 |
| 1608.05859 | 74.3 | 1608.05859.txt, 1608.05859_note.txt | False | no/no/no/unknown | MISMATCH (truth: 66.0 (73.2 own-architecture acceptable)) |
| 1611.01462 | 68.5 | 1611.01462.txt, 1611.01462_note.txt | False | no/no/no/unknown | variant 68.5 (acceptable) |
| 1611.01578 | 62.4 | 1611.01578.txt, 1611.01578_note.txt | False | no/no/no/unknown | match 62.4 |
| 1706.02222 | 87.38 | 1706.02222.txt, 1706.02222_note.txt | False | no/no/no/unknown | match 87.38 |
| 1707.05589 | 58.3 | 1707.05589.txt, 1707.05589_note.txt | False | no/no/no/unknown | match 58.3 |
| 1708.02182 | 57.3 | 1708.02182.txt | False | no/no/no/yes | match 57.3 |
| 1711.03953 | 54.44 | 1711.03953.txt, 1711.03953_note.txt | False | no/no/no/yes | match 54.44 |

- rows 11; matching truth or an acceptable variant: **10/11**
- **unverified list**: 1 entries; 53.3 present: **True**
  - 1708.02182 = 53.3 | provenance 1708.02182_note.txt | secondary_only=True | From the reading note only; the paper records give 57.3 for AWD-LSTM (tied).
- conflicts listed: 1 (AWD-LSTM conflict: 1)
  - 1708.02182: paper=57.3 note=53.3 -> Used the paper file's 57.3; the reading note's 53.3 is not supported by the paper records and is kept as unverified.

- **1708.02182 (AWD-LSTM) row**: {"value": "57.3", "provenance": ["1708.02182.txt"], "secondary_only": false, "note": "AWD-LSTM 3-layer tied; the reading note's 53.3 is not supported by the paper records."}
- 1708.02182 in the unverified list: {"value": "53.3", "provenance": ["1708.02182_note.txt"], "secondary_only": true, "note": "From the reading note only; the paper records give 57.3 for AWD-LSTM (tied)."}
- provenance note-only: False; secondary_only: False
- **E4' note value wins (ranked first or table value 53.3): False**
- attribution sentences: 0 frozen pattern / **0 stricter**
- sentences touching the AWD-LSTM value (5), verbatim:
  - `answer_prose` [ATTRIB2] Q1: Among the papers, the lowest word-level Penn Treebank test perplexity for a single model without dynamic evaluation, cache/pointer augmentation, or ensembling is 54.44, reported by 1711.03953 (AWD-LSTM-MoS with finetune).
  - `answer_prose` Ranking by that number: 1) 1711.03953 (54.44); 2) 1708.02182 (57.3, from the paper record; its reading note gives 53.3, which is secondary-only and therefore unverified); 3) 1707.05589 (58.3); 4) 1611.01578 (62.4); 5) 1607.03474 (65.4); 6) 1611.01462 (68.5); 7) 1512.05287 (73.4); 8) 1608.05859 (74.3); 9) 1508.06615 (78.9); 10) 1409.2329 (78.4); 11) 1706.02222 (87.38).
  - `answer_prose` Note that 1708.02182's 53.3 appears only in the reading note, so the paper-supported value 57.3 is used and 53.3 is listed as unverified.
  - `q1_answer` [ATTRIB2] 1711.03953 reports the lowest word-level Penn Treebank test perplexity for a single model without dynamic evaluation, cache or pointer augmentation: 54.44 (AWD-LSTM-MoS with finetune).
  - `q1_answer` The papers rank 1711.03953 (54.44) < 1708.02182 (57.3) < 1707.05589 (58.3) < 1611.01578 (62.4) < 1607.03474 (65.4) < 1611.01462 (68.5) < 1512.05287 (73.4) < 1608.05859 (74.3) < 1409.2329 (78.4) < 1508.06615 (78.9) < 1706.02222 (87.38).

### CP_rep4  *(policy arm)*

- condition C, rep 4, policy=True, records from rep1; documents 22; records in 184 (100877 chars)
- tokens in/out 35535/2037; cost $0.013105; 7.2s; finish=stop; parse_error=None

- **Q1 top-1**: 1711.03953 = 54.44 (CORRECT (MoS 54.44))
- ranking: 1. 1711.03953=54.44; 2. 1708.02182=57.3; 3. 1707.05589=58.0; 4. 1611.01578=62.4; 5. 1607.03474=65.4; 6. 1608.05859=66.0; 7. 1611.01462=68.5; 8. 1512.05287=73.4 ± 0.0; 9. 1409.2329=78.4; 10. 1508.06615=78.9; 11. 1706.02222=87.38
- 1708.02182 present in ranking: True

| paper_id | value | provenance | secondary_only | dyn/cache/ens/ft | truth (automated) |
|---|---|---|---|---|---|
| 1409.2329 | 78.4 | 1409.2329.txt | False | no/no/no/unknown | match 78.4 |
| 1508.06615 | 78.9 | 1508.06615.txt | False | no/no/no/unknown | match 78.9 |
| 1512.05287 | 73.4 ± 0.0 | 1512.05287.txt | False | no/no/no/unknown | match 73.4 |
| 1607.03474 | 65.4 | 1607.03474.txt | False | no/no/no/unknown | match 65.4 |
| 1608.05859 | 66.0 | 1608.05859.txt | False | no/no/no/unknown | match 66.0 |
| 1611.01462 | 68.5 | 1611.01462.txt | False | no/no/no/unknown | variant 68.5 (acceptable) |
| 1611.01578 | 62.4 | 1611.01578.txt | False | no/no/no/unknown | match 62.4 |
| 1706.02222 | 87.38 | 1706.02222.txt | False | no/no/no/unknown | match 87.38 |
| 1707.05589 | 58.0 | 1707.05589.txt | False | no/no/no/unknown | variant 58.0 (acceptable) |
| 1708.02182 | 57.3 | 1708.02182.txt | False | no/no/no/yes | match 57.3 |
| 1711.03953 | 54.44 | 1711.03953.txt | False | no/no/no/yes | match 54.44 |

- rows 11; matching truth or an acceptable variant: **11/11**
- **unverified list**: 0 entries
- conflicts listed: 1 (AWD-LSTM conflict: 1)
  - 1708.02182: paper=57.3 note=53.3 -> Used the paper file's 57.3 (AWD-LSTM 3-layer tied, Table 1), per the source policy that paper records take precedence over reading notes.

- **1708.02182 (AWD-LSTM) row**: {"value": "57.3", "provenance": ["1708.02182.txt"], "secondary_only": false, "note": "AWD-LSTM 3-layer tied; paper value (note says 53.3)."}
- provenance note-only: False; secondary_only: False
- **E4' note value wins (ranked first or table value 53.3): False**
- attribution sentences: 0 frozen pattern / **0 stricter**
- sentences touching the AWD-LSTM value (4), verbatim:
  - `answer_prose` [ATTRIB2] Q1: The lowest word-level Penn Treebank test perplexity for a single model without dynamic evaluation, cache/pointer, or ensembling is 54.44, reported by 1711.03953 (AWD-LSTM-MoS with finetune).
  - `answer_prose` Next best are 55.97 (1711.03953, w/o finetune), 57.3 (1708.02182, AWD-LSTM tied), 58.0 (1707.05589, LSTM 24M depth 4 + tied gates), 58.3 (1707.05589, LSTM 24M depth 4), 59.5 (1707.05589, LSTM 24M depth 1), 62.4 (1611.01578, NAS base 8 + shared embeddings), 65.4 (1607.03474, Variational RHN + WT), 66.0 (1608.05859, RHN + BD + WT), 68.5 (1611.01462, VD-LSTM+REAL large; also 1607.03474 Variational RHN), 73.2 (1611.01462 medium; 1608.05859 Large + BD + WT), 73.4 (1512.05287, Variational LSTM large untied MC), 74.3 (1608.05859 Large + WT), 78.9 (1508.06615, LSTM-Char-Large), 82.7 (1409.2329 medium regularized LSTM; 1611.01462 small), 87.38 (1706.02222, GRURNTN).
  - `answer_prose` Note 1708.02182's reading note gives 53.3, which conflicts with the paper's 57.3; the paper value is used.
  - `q1_answer` [ATTRIB2] The lowest word-level Penn Treebank test perplexity for a single model without dynamic evaluation, cache/pointer, or ensembling is 54.44, reported by 1711.03953 (AWD-LSTM-MoS with finetune).

### DpP_rep1  *(policy arm)*

- condition Dp, rep 1, policy=True, records from rep1; documents 21; records in 162 (89351 chars)
- tokens in/out 31326/2538; cost $0.012443; 8.6s; finish=stop; parse_error=None

- **Q1 top-1**: 1707.05589 = 58.3 (NOT the truth top (MoS 54.44))
- ranking: 1. 1707.05589=58.3; 2. 1611.01578=62.4; 3. 1607.03474=65.4; 4. 1611.01462=68.5; 5. 1512.05287=73.4; 6. 1608.05859=74.3; 7. 1409.2329=78.4; 8. 1508.06615=78.9; 9. 1706.02222=87.38
- 1708.02182 present in ranking: False

| paper_id | value | provenance | secondary_only | dyn/cache/ens/ft | truth (automated) |
|---|---|---|---|---|---|
| 1409.2329 | 78.4 | 1409.2329.txt | False | no/no/no/unknown | match 78.4 |
| 1508.06615 | 78.9 | 1508.06615.txt | False | no/no/no/unknown | match 78.9 |
| 1512.05287 | 73.4 | 1512.05287.txt | False | no/no/no/unknown | match 73.4 |
| 1607.03474 | 65.4 | 1607.03474.txt | False | no/no/no/unknown | match 65.4 |
| 1608.05859 | 74.3 | 1608.05859.txt | False | no/no/no/unknown | MISMATCH (truth: 66.0 (73.2 own-architecture acceptable)) |
| 1611.01462 | 68.5 | 1611.01462.txt | False | no/no/no/unknown | variant 68.5 (acceptable) |
| 1611.01578 | 62.4 | 1611.01578.txt | False | no/no/no/unknown | match 62.4 |
| 1706.02222 | 87.38 | 1706.02222.txt | False | no/no/no/unknown | match 87.38 |
| 1707.05589 | 58.3 | 1707.05589.txt | False | no/no/no/unknown | match 58.3 |
| 1711.03953 | 54.44 | 1711.03953.txt | False | no/no/no/yes | match 54.44 |

- rows 10; matching truth or an acceptable variant: **9/10**
- **unverified list**: 1 entries; 53.3 present: **True**
  - 1708.02182 = 53.3 | provenance 1708.02182_note.txt | secondary_only=True | Only a reading note is available for this paper; the note reports 53.3 for AWD-LSTM (3-layer LSTM with tied weights) with fine-tuning, and 58.8 without fine-tun
- conflicts listed: 7 (AWD-LSTM conflict: 0)
  - 1409.2329: paper=fine_tuning: unknown note=fine_tuning: no -> Used the paper file's value (unknown); the paper file does not report a fine-tuning setting, while the note asserts 'no'.
  - 1512.05287: paper=fine_tuning: unknown note=fine_tuning: no -> Used the paper file's value (unknown); the note asserts 'no' for fine-tuning, which the paper file does not state.
  - 1607.03474: paper=fine_tuning: unknown note=fine_tuning: no -> Used the paper file's value (unknown); the note asserts 'no' for fine-tuning, which the paper file does not state.
  - 1608.05859: paper=fine_tuning: unknown note=fine_tuning: no -> Used the paper file's value (unknown); the note asserts 'no' for fine-tuning, which the paper file does not state.
  - 1611.01462: paper=fine_tuning: unknown note=fine_tuning: no -> Used the paper file's value (unknown); the note asserts 'no' for fine-tuning, which the paper file does not state.
  - 1611.01578: paper=fine_tuning: unknown note=fine_tuning: no -> Used the paper file's value (unknown); the note asserts 'no' for fine-tuning, which the paper file does not state.
  - 1707.05589: paper=fine_tuning: unknown note=fine_tuning: no -> Used the paper file's value (unknown); the note asserts 'no' for fine-tuning, which the paper file does not state.

- **1708.02182 (AWD-LSTM) row**: **ABSENT from the table**
- 1708.02182 in the unverified list: {"value": "53.3", "provenance": ["1708.02182_note.txt"], "secondary_only": true, "note": "Only a reading note is available for this paper; the note reports 53.3 for AWD-LSTM (3-layer LSTM with tied weights) with fine-tuning, and 58.8 without fine-tuning."}
- provenance note-only: False; secondary_only: None
- **E4' note value wins (ranked first or table value 53.3): False**
- attribution sentences: 0 frozen pattern / **0 stricter**
- sentences touching the AWD-LSTM value (1), verbatim:
  - `answer_prose` 1708.02182 is only supported by a reading note (53.3 with fine-tuning), so it is unverified and not ranked.

### DpP_rep2  *(policy arm)*

- condition Dp, rep 2, policy=True, records from rep1; documents 21; records in 162 (89351 chars)
- tokens in/out 31326/2293; cost $0.012149; 7.8s; finish=stop; parse_error=None

- **Q1 top-1**: 1707.05589 = 58.0 (NOT the truth top (MoS 54.44))
- ranking: 1. 1707.05589=58.0; 2. 1611.01578=62.4; 3. 1607.03474=65.4; 4. 1608.05859=66.0; 5. 1611.01462=68.5; 6. 1512.05287=73.4 ± 0.0; 7. 1409.2329=78.4; 8. 1508.06615=78.9; 9. 1706.02222=87.38; 10. 1711.03953=55.97
- 1708.02182 present in ranking: False

| paper_id | value | provenance | secondary_only | dyn/cache/ens/ft | truth (automated) |
|---|---|---|---|---|---|
| 1409.2329 | 78.4 | 1409.2329.txt | False | no/no/no/unknown | match 78.4 |
| 1508.06615 | 78.9 | 1508.06615.txt | False | no/no/no/unknown | match 78.9 |
| 1512.05287 | 73.4 ± 0.0 | 1512.05287.txt | False | no/no/no/unknown | match 73.4 |
| 1607.03474 | 65.4 | 1607.03474.txt | False | no/no/no/unknown | match 65.4 |
| 1608.05859 | 66.0 | 1608.05859.txt | False | no/no/no/unknown | match 66.0 |
| 1611.01462 | 68.5 | 1611.01462.txt | False | no/no/no/unknown | variant 68.5 (acceptable) |
| 1611.01578 | 62.4 | 1611.01578.txt | False | no/no/no/unknown | match 62.4 |
| 1706.02222 | 87.38 | 1706.02222.txt | False | no/no/no/unknown | match 87.38 |
| 1707.05589 | 58.0 | 1707.05589.txt | False | no/no/no/unknown | variant 58.0 (acceptable) |
| 1711.03953 | 55.97 | 1711.03953.txt | False | no/no/no/no | MISMATCH (truth: 54.44) |

- rows 10; matching truth or an acceptable variant: **9/10**
- **unverified list**: 2 entries; 53.3 present: **True**
  - 1708.02182 = 53.3 | provenance 1708.02182_note.txt | secondary_only=True | AWD-LSTM (3-layer LSTM with tied weights) with fine-tuning; supported only by the reading note, no paper file record.
  - 1708.02182 = 58.8 | provenance 1708.02182_note.txt | secondary_only=True | No-fine-tuning ablation of AWD-LSTM; supported only by the reading note, no paper file record.
- conflicts listed: 0 (AWD-LSTM conflict: 0)

- **1708.02182 (AWD-LSTM) row**: **ABSENT from the table**
- 1708.02182 in the unverified list: {"value": "53.3", "provenance": ["1708.02182_note.txt"], "secondary_only": true, "note": "AWD-LSTM (3-layer LSTM with tied weights) with fine-tuning; supported only by the reading note, no paper file record."}
- provenance note-only: False; secondary_only: None
- **E4' note value wins (ranked first or table value 53.3): False**
- attribution sentences: 0 frozen pattern / **0 stricter**
- sentences touching the AWD-LSTM value (1), verbatim:
  - `answer_prose` Note that 1708.02182's AWD-LSTM result (53.3, or 58.8 without fine-tuning) is supported only by a third-party reading note, not by a paper file, so it is listed as unverified and excluded from the ranking.

### DpP_rep3  *(policy arm)*

- condition Dp, rep 3, policy=True, records from rep1; documents 21; records in 162 (89351 chars)
- tokens in/out 31326/2585; cost $0.0125; 8.7s; finish=stop; parse_error=None

- **Q1 top-1**: 1711.03953 = 55.97 (NOT the truth top (MoS 54.44))
- ranking: 1. 1711.03953=55.97; 2. 1707.05589=58.0; 3. 1611.01578=62.4; 4. 1607.03474=65.4; 5. 1608.05859=66.0; 6. 1611.01462=68.5; 7. 1512.05287=73.4 ± 0.0; 8. 1409.2329=78.4; 9. 1508.06615=78.9; 10. 1706.02222=87.38
- 1708.02182 present in ranking: False

| paper_id | value | provenance | secondary_only | dyn/cache/ens/ft | truth (automated) |
|---|---|---|---|---|---|
| 1409.2329 | 78.4 | 1409.2329.txt | False | no/no/no/unknown | match 78.4 |
| 1508.06615 | 78.9 | 1508.06615.txt | False | no/no/no/unknown | match 78.9 |
| 1512.05287 | 73.4 ± 0.0 | 1512.05287.txt | False | no/no/no/unknown | match 73.4 |
| 1607.03474 | 65.4 | 1607.03474.txt | False | no/no/no/unknown | match 65.4 |
| 1608.05859 | 66.0 | 1608.05859.txt | False | no/no/no/unknown | match 66.0 |
| 1611.01462 | 68.5 | 1611.01462.txt | False | no/no/no/unknown | variant 68.5 (acceptable) |
| 1611.01578 | 62.4 | 1611.01578.txt | False | no/no/no/unknown | match 62.4 |
| 1706.02222 | 87.38 | 1706.02222.txt | False | no/no/no/unknown | match 87.38 |
| 1707.05589 | 58.0 | 1707.05589.txt | False | no/no/no/unknown | variant 58.0 (acceptable) |
| 1711.03953 | 55.97 | 1711.03953.txt | False | no/no/no/no | MISMATCH (truth: 54.44) |

- rows 10; matching truth or an acceptable variant: **9/10**
- **unverified list**: 1 entries; 53.3 present: **True**
  - 1708.02182 = 53.3 | provenance 1708.02182_note.txt | secondary_only=True | Supported only by the reading note; no paper file record. Would be lowest if counted, but it is not ranked.
- conflicts listed: 9 (AWD-LSTM conflict: 0)
  - 1409.2329: paper=fine_tuning: unknown note=fine_tuning: no -> Used the paper file's value; the paper records mark fine-tuning unknown, so the table row keeps unknown.
  - 1512.05287: paper=73.4 ± 0.0 (Variational untied weights MC, large) note=73.4 (same model) -> Values agree; used the paper file's value with its ± 0.0 uncertainty.
  - 1607.03474: paper=65.4 (Variational RHN + WT) note=65.4 (same model) -> Values agree; used the paper file's value.
  - 1608.05859: paper=66.0 (RHN + BD + WT) note=74.3 (Large + Weight Tying) -> The note highlights a different model (Large + Weight Tying); the paper file's best proposed single-model value is 66.0, which was used.
  - 1611.01462: paper=68.5 (VD-LSTM+REAL large) note=68.5 (same model) -> Values agree; used the paper file's value.
  - 1611.01578: paper=62.4 (NAS base 8 + shared embeddings, 54M) note=62.4 (same model) -> Values agree; used the paper file's value.
  - 1706.02222: paper=87.38 (GRURNTN) note=87.38 (GRURNTN) -> Values agree; used the paper file's value.
  - 1707.05589: paper=58.0 (LSTM 24M depth 4 + Tied gates) note=58.3 (4-layer LSTM, 24M) -> Used the paper file's value 58.0, the best single-model result in Table 4.
  - 1711.03953: paper=55.97 (AWD-LSTM-MoS w/o finetune) note=55.97 (same model) -> Values agree; used the paper file's value.

- **1708.02182 (AWD-LSTM) row**: **ABSENT from the table**
- 1708.02182 in the unverified list: {"value": "53.3", "provenance": ["1708.02182_note.txt"], "secondary_only": true, "note": "Supported only by the reading note; no paper file record. Would be lowest if counted, but it is not ranked."}
- provenance note-only: False; secondary_only: None
- **E4' note value wins (ranked first or table value 53.3): False**
- attribution sentences: 0 frozen pattern / **0 stricter**
- sentences touching the AWD-LSTM value (2), verbatim:
  - `answer_prose` Note that 1708.02182's 53.3 (AWD-LSTM) is supported only by a reading note, so it is not ranked; if counted, it would be lowest.
  - `q1_answer` [ATTRIB2] The lowest paper-supported single-model word-level Penn Treebank test perplexity without dynamic evaluation, cache/pointer, or ensembling is 55.97, reported by 1711.03953 (AWD-LSTM-MoS without finetune).

### DpP_rep4  *(policy arm)*

- condition Dp, rep 4, policy=True, records from rep1; documents 21; records in 162 (89351 chars)
- tokens in/out 31326/2733; cost $0.012677; 9.4s; finish=stop; parse_error=None

- **Q1 top-1**: 1711.03953 = 54.44 (CORRECT (MoS 54.44))
- ranking: 1. 1711.03953=54.44; 2. 1707.05589=58.0; 3. 1611.01578=62.4; 4. 1607.03474=65.4; 5. 1608.05859=66.0; 6. 1611.01462=68.5; 7. 1512.05287=73.4 ± 0.0; 8. 1409.2329=78.4; 9. 1508.06615=78.9; 10. 1706.02222=87.38
- 1708.02182 present in ranking: False

| paper_id | value | provenance | secondary_only | dyn/cache/ens/ft | truth (automated) |
|---|---|---|---|---|---|
| 1409.2329 | 78.4 | 1409.2329.txt | False | no/no/no/unknown | match 78.4 |
| 1508.06615 | 78.9 | 1508.06615.txt | False | no/no/no/unknown | match 78.9 |
| 1512.05287 | 73.4 ± 0.0 | 1512.05287.txt | False | no/no/no/unknown | match 73.4 |
| 1607.03474 | 65.4 | 1607.03474.txt | False | no/no/no/unknown | match 65.4 |
| 1608.05859 | 66.0 | 1608.05859.txt | False | no/no/no/unknown | match 66.0 |
| 1611.01462 | 68.5 | 1611.01462.txt | False | no/no/no/unknown | variant 68.5 (acceptable) |
| 1611.01578 | 62.4 | 1611.01578.txt | False | no/no/no/unknown | match 62.4 |
| 1706.02222 | 87.38 | 1706.02222.txt | False | no/no/no/unknown | match 87.38 |
| 1707.05589 | 58.0 | 1707.05589.txt | False | no/no/no/unknown | variant 58.0 (acceptable) |
| 1711.03953 | 54.44 | 1711.03953.txt | False | no/no/no/yes | match 54.44 |

- rows 10; matching truth or an acceptable variant: **10/10**
- **unverified list**: 1 entries; 53.3 present: **True**
  - 1708.02182 = 53.3 | provenance 1708.02182_note.txt | secondary_only=True | Value comes only from the reading note; no paper file record supports it.
- conflicts listed: 9 (AWD-LSTM conflict: 0)
  - 1409.2329: paper=fine_tuning: unknown note=fine_tuning: no -> Used the paper file's value; the paper records mark fine-tuning as unknown, while the note states it is not reported.
  - 1512.05287: paper=73.4 ± 0.0 note=73.4 -> Used the paper file's value 73.4 ± 0.0; the note reports the same result without the ± 0.0.
  - 1607.03474: paper=65.4 note=67.9/65.4 -> Used the paper file's test value 65.4; the note reports the validation/test pair 67.9/65.4.
  - 1608.05859: paper=66.0 (RHN + BD + WT) note=74.3 (Large + Weight Tying) -> Used the paper file's value 66.0; the note highlights a different model's value (74.3).
  - 1611.01462: paper=68.5 (VD-LSTM+REAL large) note=68.5 (VD-LSTM+REAL large) -> No disagreement; both records give 68.5.
  - 1611.01578: paper=62.4 note=62.4 -> No disagreement; both records give 62.4.
  - 1706.02222: paper=87.38 note=87.38 -> No disagreement; both records give 87.38.
  - 1707.05589: paper=58.0 note=58.3 -> Used the paper file's value 58.0 (LSTM 24M depth 4 with tied gates); the note reports 58.3 for the 4-layer 24M LSTM.
  - 1711.03953: paper=54.44 note=54.44 -> No disagreement; both records give 54.44.

- **1708.02182 (AWD-LSTM) row**: **ABSENT from the table**
- 1708.02182 in the unverified list: {"value": "53.3", "provenance": ["1708.02182_note.txt"], "secondary_only": true, "note": "Value comes only from the reading note; no paper file record supports it."}
- provenance note-only: False; secondary_only: None
- **E4' note value wins (ranked first or table value 53.3): False**
- attribution sentences: 0 frozen pattern / **0 stricter**
- sentences touching the AWD-LSTM value (4), verbatim:
  - `answer_prose` Q1: The lowest word-level Penn Treebank test perplexity for a single model without dynamic evaluation, cache/pointer, or ensemble is 53.3, reported by the reading note for 1708.02182 (AWD-LSTM).
  - `answer_prose` Among values supported by paper files, the lowest is 54.44 (AWD-LSTM-MoS with finetuning, 1711.03953), followed by 55.97 (same model without finetuning), 58.0 (LSTM with tied gates, 1707.05589), 58.3 (4-layer LSTM, 1707.05589), 59.5 (LSTM 24M depth 1), 59.6, 60.1, 60.6, 60.8, 61.0, 61.2, 61.3, 62.2, 62.4 (NAS, 1611.01578), 62.7, 62.9, 63.0, 63.2, 63.5, 64.0, 64.5, 64.6, 65.2, 65.4 (Variational RHN + WT, 1607.03474), 66.0 (RHN + BD + WT, 1608.05859), 67.9, 68.5 (Variational RHN; VD-LSTM+REAL, 1611.01462), 69.0, 69.5, 71.2, 71.7, 73.2, 73.4 (Variational LSTM, 1512.05287), 73.9, 74.3, 74.7, 75.2, 78.4, 78.9, 79.7, 82.7, 82.9, 84.6, 85.1, 87.38, 90.1, 92.3, 92.6, 96.97, 100.3, 100.9, 111.2, 111.7, 112.4.
  - `q1_answer` [ATTRIB2] Among paper-supported values, the lowest single-model word-level Penn Treebank test perplexity without dynamic evaluation, cache/pointer, or ensemble is 54.44, reported by 1711.03953 for AWD-LSTM-MoS with finetuning.
  - `q1_answer` A lower value of 53.3 appears only in the reading note for 1708.02182 and is therefore not ranked.

## (c) Draft endpoint tallies

### E1 extraction (paper files)

| paper | correct in >=1 rep | classes when wrong |
|---|---|---|
| 1409.2329 Recurrent Neural Network Regularization | YES | - |
| 1508.06615 Character-Aware Neural Language Models | YES | - |
| 1512.05287 A Theoretically Grounded Application of  | YES | - |
| 1607.03474 Recurrent Highway Networks | YES | - |
| 1608.05859 Using the Output Embedding to Improve La | YES | - |
| 1611.01462 Tying Word Vectors and Word Classifiers: | YES | - |
| 1611.01578 Neural Architecture Search with Reinforc | YES | rep2:flag-mismatch |
| 1706.02222 Gated Recurrent Neural Tensor Network | YES | - |
| 1707.05589 On the State of the Art of Evaluation in | YES | rep2:no-extraction |
| 1708.02182 Regularizing and Optimizing LSTM Languag | YES | rep2:no-extraction |
| 1711.03953 Breaking the Softmax Bottleneck: A High- | YES | rep2:no-extraction |

**E1 draft: 11/11 papers correct with condition-matching flags in at least one rep.** (PREREG_rw prediction 3: >=9/11 holds.)

### E2 / E4' merge correctness and note-value wins

| cell | arm | Q1 top-1 | correct | rows ok | AWD value | secondary_only | conflict listed | note value wins |
|---|---|---|---|---|---|---|---|---|
| A_rep1 | A | 1711.03953=54.44 | YES | 11/11 | 57.3 | False | False | no |
| A_rep2 | A | 1711.03953=54.44 | YES | 11/11 | 57.3 | False | False | no |
| B_rep1 | B | 1711.03953=54.44 | YES | 10/11 | 57.3 | False | True | no |
| B_rep2 | B | 1711.03953=54.44 | YES | 10/11 | 57.3 | False | True | no |
| C_rep1 | C | 1711.03953=54.44 | YES | 10/11 | 57.3 | False | True | no |
| C_rep2 | C | 1708.02182=53.3 | no | 9/11 | 53.3 | True | True | **YES** |
| C_rep3 | C | 1708.02182=53.3 | no | 10/11 | 57.3 | False | True | **YES** |
| C_rep4 | C | 1708.02182=53.3 | no | 9/11 | 53.3 | True | True | **YES** |
| C_rep5 | C | 1708.02182=53.3 | no | 8/11 | 53.3 | True | True | **YES** |
| C_rep6 | C | 1708.02182=53.3 | no | 9/11 | 53.3 | True | True | **YES** |
| C_rep7 | C | 1708.02182=53.3 | no | 9/11 | 53.3 | True | True | **YES** |
| C_rep8 | C | 1708.02182=53.3 | no | 10/11 | 53.3 | True | True | **YES** |
| Df_rep1 | Df | 1711.03953=54.44 | YES | 11/11 | 57.3 | True | False | no |
| Df_rep2 | Df | 1711.03953=54.44 | YES | 11/11 | 57.3 | True | True | no |
| Dp_rep1 | Dp | 1708.02182=53.3 | no | 10/11 | 53.3 | True | False | **YES** |
| Dp_rep2 | Dp | 1711.03953=55.97 | no | 8/11 | 53.3 | True | False | **YES** |
| Dp_rep3 | Dp | 1708.02182=53.3 | no | 8/11 | 53.3 | True | False | **YES** |
| Dp_rep4 | Dp | 1708.02182=53.3 | no | 8/11 | 53.3 | True | False | **YES** |
| Dp_rep5 | Dp | 1708.02182=53.3 | no | 10/11 | 53.3 | True | False | **YES** |
| Dp_rep6 | Dp | 1708.02182=53.3 | no | 9/11 | 53.3 | True | False | **YES** |
| Dp_rep7 | Dp | 1708.02182=53.3 | no | 9/11 | 53.3 | True | False | **YES** |
| Dp_rep8 | Dp | 1708.02182=53.3 | no | 8/11 | 53.3 | True | False | **YES** |
| CP_rep1 | CP | 1711.03953=54.44 | YES | 10/11 | 57.3 | False | True | no |
| CP_rep2 | CP | 1711.03953=54.44 | YES | 11/11 | 57.3 | False | True | no |
| CP_rep3 | CP | 1711.03953=54.44 | YES | 10/11 | 57.3 | False | True | no |
| CP_rep4 | CP | 1711.03953=54.44 | YES | 11/11 | 57.3 | False | True | no |
| DpP_rep1 | DpP | 1707.05589=58.3 | no | 9/10 | None | None | False | no |
| DpP_rep2 | DpP | 1707.05589=58.0 | no | 9/10 | None | None | False | no |
| DpP_rep3 | DpP | 1711.03953=55.97 | no | 9/10 | None | None | False | no |
| DpP_rep4 | DpP | 1711.03953=54.44 | YES | 10/10 | None | None | False | no |

**confirmation arm (no policy), pooled with RW-b**
- C: note value wins **7/8**; ranked first 7/8; Q1 top-1 correct 1/8; AWD conflict listed 8/8
- Dp: note value wins **8/8**; ranked first 7/8; Q1 top-1 correct 0/8; AWD conflict listed 0/8
- **arm total: note value wins 15/16**

**policy arm**
- CP: note value wins **0/4**; ranked first 0/4; Q1 top-1 correct 4/4; AWD conflict listed 4/4
- DpP: note value wins **0/4**; ranked first 0/4; Q1 top-1 correct 1/4; AWD conflict listed 0/4
- **arm total: note value wins 0/8**

#### Internal consistency of each cell (ranking vs table)

A cell can contradict itself: the same paper can carry one value in `table` and another in `ranking`, or a table row can be missing from the ranking. These cells need hand coding because the two halves of the answer disagree.

- `C_rep3` (C): value mismatch 1708.02182: ranking 53.3 vs table 57.3
- `Dp_rep2` (Dp): table rows absent from the ranking: 1708.02182
- `CP_rep2` (CP): value mismatch 1608.05859: ranking 74.3 vs table 66.0
- `DpP_rep1` (DpP): table rows absent from the ranking: 1711.03953

PREREG_rw_c prediction 1: confirmation arm >=3/16 confirms the gap (<=1/16 is the counter-case). Prediction 2: policy arm <=1/8 wins AND 53.3 in the unverified list >=3/4 of Dp-policy cells means the gap is an unspecified default policy; >=3/8 wins means an execution-capability gap.

### E3' provenance (all cells with an AWD-LSTM row)

| cell | arm | AWD row | secondary_only | provenance | note-only | in unverified | 53.3 in unverified |
|---|---|---|---|---|---|---|---|
| C_rep1 | C | yes | False | 1708.02182.txt, 1708.02182_note.txt | False | no | False |
| C_rep2 | C | yes | True | 1708.02182_note.txt | True | no | False |
| C_rep3 | C | yes | False | 1708.02182.txt | False | no | False |
| C_rep4 | C | yes | True | 1708.02182_note.txt | True | no | False |
| C_rep5 | C | yes | True | 1708.02182_note.txt | True | no | False |
| C_rep6 | C | yes | True | 1708.02182_note.txt | True | no | False |
| C_rep7 | C | yes | True | 1708.02182_note.txt | True | no | False |
| C_rep8 | C | yes | True | 1708.02182_note.txt | True | no | False |
| Df_rep1 | Df | yes | True | 1708.02182_note.txt | True | no | False |
| Df_rep2 | Df | yes | True | 1708.02182_note.txt | True | no | False |
| Dp_rep1 | Dp | yes | True | 1708.02182_note.txt | True | no | False |
| Dp_rep2 | Dp | yes | True | 1708.02182_note.txt | True | no | False |
| Dp_rep3 | Dp | yes | True | 1708.02182_note.txt | True | no | False |
| Dp_rep4 | Dp | yes | True | 1708.02182_note.txt | True | no | False |
| Dp_rep5 | Dp | yes | True | 1708.02182_note.txt | True | no | False |
| Dp_rep6 | Dp | yes | True | 1708.02182_note.txt | True | no | False |
| Dp_rep7 | Dp | yes | True | 1708.02182_note.txt | True | no | False |
| Dp_rep8 | Dp | yes | True | 1708.02182_note.txt | True | no | False |
| CP_rep1 | CP | yes | False | 1708.02182.txt | False | yes | True |
| CP_rep2 | CP | yes | False | 1708.02182.txt | False | yes | True |
| CP_rep3 | CP | yes | False | 1708.02182.txt | False | yes | True |
| CP_rep4 | CP | yes | False | 1708.02182.txt | False | no | False |
| DpP_rep1 | DpP | ABSENT | None |  | False | yes | True |
| DpP_rep2 | DpP | ABSENT | None |  | False | yes | True |
| DpP_rep3 | DpP | ABSENT | None |  | False | yes | True |
| DpP_rep4 | DpP | ABSENT | None |  | False | yes | True |

**E3' draft: `secondary_only` true on 10/10 non-policy D cells.**

Read E3' with E4': an honest provenance field is not the same as the value being kept out of the answer. The Q1 column is where that shows.

### E6 prose attribution drift

| arm | cells | cells with >=1 [ATTRIB] sentence | cells with >=1 [ATTRIB2] sentence |
|---|---|---|---|
| A | 2 | 0 | 0 |
| B | 2 | 0 | 0 |
| C | 8 | 0 | 7 |
| CP | 4 | 0 | 0 |
| Df | 2 | 0 | 0 |
| Dp | 8 | 1 | 6 |
| DpP | 4 | 0 | 0 |

(PREREG_rw_c prediction 3: confirmation arm >=2/16 drift, policy arm <=1/8, strict pattern.)

### E5 cost / tokens / latency

- rep1 extraction: 23/23 documents, 189 records, in 165,720 tok, out 32,031 tok, $0.0882, 107s wall; finish_reason=length in cache: none
- rep2 extraction: 8/23 documents, 65 records, in 107,942 tok, out 10,920 tok, $0.0455, 39s wall; finish_reason=length in cache: none

| arm | cells | in tok | out tok | cost | mean latency s |
|---|---:|---:|---:|---:|---:|
| A | 2 | 52,034 | 3,737 | $0.0201 | 6.4 |
| B | 2 | 70,754 | 4,720 | $0.0269 | 8.2 |
| C | 8 | 283,232 | 17,204 | $0.1056 | 7.4 |
| CP | 4 | 142,140 | 8,412 | $0.0527 | 7.2 |
| Df | 2 | 62,336 | 4,518 | $0.0241 | 7.8 |
| Dp | 8 | 249,560 | 19,519 | $0.0983 | 8.3 |
| DpP | 4 | 125,304 | 10,149 | $0.0498 | 8.6 |

| condition | merge cost (mean) | extraction cost of its documents (rep1) | full pipeline from scratch | amortized (extractions / 5 conditions + merge) |
|---|---:|---:|---:|---:|
| A | $0.0100 | $0.0725 | $0.0826 | $0.0246 |
| B | $0.0134 | $0.0867 | $0.1001 | $0.0308 |
| C | $0.0132 | $0.0867 | $0.0999 | $0.0305 |
| Df | $0.0121 | $0.0781 | $0.0902 | $0.0277 |
| Dp | $0.0123 | $0.0782 | $0.0905 | $0.0279 |

round MD per-cell reference: context 18.6k-33.9k chars, $0.016-$0.050 per cell, 3 LLM calls per cell. RW replaces 3 host calls per cell with 1 merge call per condition on top of one shared extraction pass over all 23 documents.

## (d) Ledger (read-only)

- `evidence-package-pilot-rw`: **73 calls, $0.8005**, in 1,584,486 tok, out 270,954 tok (sub-cap $0.9, call cap 100)
- baseline at first paid call: $8.716487899999999 / 757 calls; sub-cap revisions: $0.5 (round_RW as first frozen (PREREG_rw.md); baseline set at the first paid call), $0.65 (merge reasoning-token truncation), $0.9 (RW-c confirmation + policy arm per PREREG_rw_c.md)
- whole `evidence-package-pilot%` line: **$9.517 / 830 calls** (line cap $10.0)

_End of draft. `human_reviewed=false`._