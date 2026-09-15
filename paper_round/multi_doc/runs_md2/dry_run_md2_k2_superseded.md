# round_MD2 dry run (0 model calls) — 2026-09-15T21:26:25

COMPRESSION_THRESHOLD=8000; host fast path needs total_chars < 8000 AND n_docs <= 10; arms=('quota', 'oracle', 'struct'); k_quota=2

## 1. docpaths / documents

| cell | dir | docs | chars | fast_path | 57.3 in 1708.02182.txt | notes |
|---|---|---|---|---|---|---|
| Q1_quota_C | cell_01 | 22 | 534379 | no | True | materials |
| Q1_quota_P | cell_02 | 22 | 534379 | no | True | materials |
| Q1_oracle_C | cell_03 | 22 | 534379 | no | True | materials |
| Q1_oracle_P | cell_04 | 22 | 534379 | no | True | materials |
| Q2_quota_C | cell_05 | 22 | 534379 | no | True | materials |
| Q2_quota_P | cell_06 | 22 | 534379 | no | True | materials |
| Q2_oracle_C | cell_07 | 22 | 534379 | no | True | materials |
| Q2_oracle_P | cell_08 | 22 | 534379 | no | True | materials |

Fast path NOT applicable in any cell: 22 documents (> 10) and 534379 chars (> 400000). Retrieval is unavoidable by construction.

## 2. section_chunks per document

| document | chunks (P) | chunks (C) |
|---|---|---|
| 1409.2329.txt | 44 | 44 |
| 1409.2329_note.txt | 3 | 3 |
| 1508.06615.txt | 78 | 78 |
| 1508.06615_note.txt | 4 | 4 |
| 1512.05287.txt | 76 | 76 |
| 1512.05287_note.txt | 3 | 3 |
| 1607.03474.txt | 82 | 82 |
| 1607.03474_note.txt | 3 | 3 |
| 1608.05859.txt | 52 | 52 |
| 1608.05859_note.txt | 2 | 2 |
| 1611.01462.txt | 66 | 66 |
| 1611.01462_note.txt | 3 | 3 |
| 1611.01578.txt | 70 | 70 |
| 1611.01578_note.txt | 3 | 3 |
| 1706.02222.txt | 73 | 73 |
| 1706.02222_note.txt | 3 | 3 |
| 1707.05589.txt | 48 | 48 |
| 1707.05589_note.txt | 2 | 2 |
| 1708.02182.txt | 68 | 68 |
| 1708.02182_note.txt | 3 | 3 |
| 1711.03953.txt | 100 | 100 |
| 1711.03953_note.txt | 3 | 3 |
| **total** | 789 | 789 |

totals: {'C': 789, 'P': 789}; paper chunks only: {'C': 757, 'P': 757}; notes: {'C': 32, 'P': 32}

struct chunk index built on condition P: 789 chunks, embedding dim 384, 3.3s (local HF all-MiniLM-L6-v2, $0).

## 3. quota exposure ESTIMATE for 1708.02182.txt (query = raw question text)

ESTIMATE ONLY: at run time the host queries with sub-queries the model generates from the question, not with the raw question text; these ranks are a proxy for whether quota k=2 would surface a 57.3 chunk.

| question | 57.3 chunk (idx) | cos | rank among the 68 chunks of 1708.02182.txt | in top-2? | global cos rank / 789 | in struct global top-10? |
|---|---|---|---|---|---|---|
| Q1 | 616 | 0.3267 | 23 | no | 251 | no |
| Q1 | 654 | 0.1740 | 50 | no | 569 | no |
| Q1 | 655 | 0.4995 | 4 | no | 67 | no |
| Q1 | 667 | 0.3403 | 16 | no | 217 | no |
| Q1 | *quota top-2 of this paper* | | | | | idx 648 (cos 0.5464, 57.3=no), idx 617 (cos 0.5463, 57.3=no) |
| Q2 | 616 | 0.3111 | 15 | no | 225 | no |
| Q2 | 654 | 0.1203 | 53 | no | 627 | no |
| Q2 | 655 | 0.4687 | 3 | no | 60 | no |
| Q2 | 667 | 0.3133 | 14 | no | 222 | no |
| Q2 | *quota top-2 of this paper* | | | | | idx 648 (cos 0.5514, 57.3=no), idx 617 (cos 0.4984, 57.3=no) |

## 4. oracle appendix (chunks of 1708.02182.txt containing 57.3)

4 chunk(s) would be appended per cell (once, in the first sub-query's context).

- idx 616, 887 chars, sha256 0df83cda8850: `Abstract   Recurrent neural networks (RNNs), such as long short-term memory networks (LSTMs), serve as a fundamental bui`
- idx 654, 791 chars, sha256 1e9601cfe0b1: `Kim et al. 2016 - CharCNN   19M   − -   78.9 78.9    Merity et al. 2016 - Pointer Sentinel-LSTM   21M   72.4 72.4   70.9`
- idx 655, 524 chars, sha256 d5be88d3cfbd: `AWD-LSTM - 3-layer LSTM (tied)   24M   60.0 60.0   57.3 57.3    AWD-LSTM - 3-layer LSTM (tied) + continuous cache pointe`
- idx 667, 811 chars, sha256 1cd0c31c829e: `8 Model Ablation Analysis    PTB   WT2   Model   Validation   Test   Validation   Test   AWD-LSTM (tied)   60.0 60.0   5`

(struct's own union for the raw question of Q1 returned 16 blocks, 13698 chars — reference only.)

DRY DONE (0 model calls)
