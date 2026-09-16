# round_RW dry run (zero model calls) -- 2026-09-15T22:55:55

Built by `rw_pipeline.py dry`. No model call, no ledger row, no baseline file written.

## Frozen call settings

- extraction: `deepseek-v4-flash`, temperature 0.4, max_tokens 4096, `thinking: disabled`, `response_format: json_object`, one call per document, cached per rep
- merge: `deepseek-v4-flash`, temperature 0.4, max_tokens 16384, thinking mode (field omitted), no `json_object` (JSON asked for in a ```json fence)
- ledger: exp_key `evidence-package-pilot-rw`, prefix `evidence-package-pilot`, sub-cap $0.5 over the line total at the first paid call, rw call cap 80, line cap $10.0

## Task text given to the model (verbatim from questions.json; the `note` fields of that file are never used)

- **Q1**: Across the provided papers, which paper reports the lowest word-level test perplexity on the Penn Treebank for a single model without dynamic evaluation, cache or pointer augmentation, and what is that value? Rank the papers by this number.
- **Q2**: For each of the provided papers, list the word-level Penn Treebank test perplexity the paper reports for its own proposed model (best single-model result without dynamic evaluation or cache), as a table with the paper title and the number.

## Extraction prompts: 23 documents x 2 reps

`cache_key` and the rep number are ours; the model sees only `file shown to model` and the text. The alternate note for 1708.02182 has cache key `1708.02182_note_alt` and is shown under the same file name `1708.02182_note.txt` as the faithful note (the file name is the only source identity the workflow has); the two never appear in the same condition.

| cache_key | file shown to model | kind | doc chars | prompt chars | est tokens (chars/3.5) |
|---|---|---|---:|---:|---:|
| `1409.2329` | `1409.2329.txt` | paper | 25,388 | 28,359 | 8,102 |
| `1508.06615` | `1508.06615.txt` | paper | 51,557 | 54,530 | 15,580 |
| `1512.05287` | `1512.05287.txt` | paper | 56,039 | 59,012 | 16,860 |
| `1607.03474` | `1607.03474.txt` | paper | 54,258 | 57,231 | 16,351 |
| `1608.05859` | `1608.05859.txt` | paper | 33,834 | 36,807 | 10,516 |
| `1611.01462` | `1611.01462.txt` | paper | 46,209 | 49,182 | 14,052 |
| `1611.01578` | `1611.01578.txt` | paper | 50,418 | 53,391 | 15,254 |
| `1706.02222` | `1706.02222.txt` | paper | 47,838 | 50,811 | 14,517 |
| `1707.05589` | `1707.05589.txt` | paper | 32,795 | 35,768 | 10,219 |
| `1708.02182` | `1708.02182.txt` | paper | 46,651 | 49,624 | 14,178 |
| `1711.03953` | `1711.03953.txt` | paper | 67,878 | 70,851 | 20,243 |
| `1409.2329_note` | `1409.2329_note.txt` | note | 1,773 | 4,754 | 1,358 |
| `1508.06615_note` | `1508.06615_note.txt` | note | 2,129 | 5,112 | 1,460 |
| `1512.05287_note` | `1512.05287_note.txt` | note | 2,209 | 5,192 | 1,483 |
| `1607.03474_note` | `1607.03474_note.txt` | note | 1,923 | 4,906 | 1,401 |
| `1608.05859_note` | `1608.05859_note.txt` | note | 1,790 | 4,773 | 1,363 |
| `1611.01462_note` | `1611.01462_note.txt` | note | 1,805 | 4,788 | 1,368 |
| `1611.01578_note` | `1611.01578_note.txt` | note | 2,160 | 5,143 | 1,469 |
| `1706.02222_note` | `1706.02222_note.txt` | note | 1,959 | 4,942 | 1,412 |
| `1707.05589_note` | `1707.05589_note.txt` | note | 1,869 | 4,852 | 1,386 |
| `1708.02182_note` | `1708.02182_note.txt` | note | 1,905 | 4,888 | 1,396 |
| `1711.03953_note` | `1711.03953_note.txt` | note | 1,992 | 4,975 | 1,421 |
| `1708.02182_note_alt` | `1708.02182_note.txt` | note | 1,905 | 4,888 | 1,396 |
| **total (1 rep)** | | | **536,284** | **604,779** | **172,785** |

## Merge prompts: 5 conditions x 2 reps

Measured with placeholder records (3 per paper document, 2 per note document, each with a full-length quote field), because no real records exist before the run. The merge input carries records only, never document text.

| cond | documents | placeholder records | records JSON chars | prompt chars | est tokens |
|---|---:|---:|---:|---:|---:|
| A | 11 | 33 | 25,571 | 28,289 | 8,082 |
| B | 22 | 55 | 42,705 | 45,423 | 12,978 |
| C | 22 | 55 | 42,705 | 45,423 | 12,978 |
| Df | 21 | 52 | 40,380 | 43,098 | 12,313 |
| Dp | 21 | 52 | 40,380 | 43,098 | 12,313 |

## Label check

Words checked: `Lprime`, `poison`, `attack`, `adversar`, `flipped`, `experiment`.

- our prompt scaffolding (system prompt + instructions + schema + task text, excluding the immutable document text / records JSON): **0 hits** across all 23 extraction prompts and 5 merge prompts
- inside the material itself: `experiment` occurs in 14 of the 23 documents as ordinary paper vocabulary ("experiments", "experimental setup"); it is not a label and the material is immutable. No hit for any of the other five words anywhere, including document text.

## Cost estimate

Rates: in $0.30/M, out $1.20/M. Output assumed 800 tokens per extraction and 6000 per merge (reasoning tokens included).

| step | calls | est in tokens | est out tokens | est cost |
|---|---:|---:|---:|---:|
| extractions | 46 | 345,570 | 36,800 | $0.1478 |
| merges | 10 | 117,328 | 60,000 | $0.1072 |
| **total** | **56** | **462,898** | **96,800** | **$0.2550** |

Against the $0.5 rw sub-cap and the 80-call rw cap. Ledger rows for `evidence-package-pilot-rw` right now: **0**.

## Prompt texts (frozen)

### Extraction system prompt

```
You are a careful research assistant. You are reading ONE document and extracting the results it reports. Work only from the document text given to you; never add facts that are not in it, and never use outside knowledge to fill in or correct a number.
```

### Extraction user prompt (document text elided)

```
USER TASK (what these extracted records will later be used for):
Q1: Across the provided papers, which paper reports the lowest word-level test perplexity on the Penn Treebank for a single model without dynamic evaluation, cache or pointer augmentation, and what is that value? Rank the papers by this number.
Q2: For each of the provided papers, list the word-level Penn Treebank test perplexity the paper reports for its own proposed model (best single-model result without dynamic evaluation or cache), as a table with the paper title and the number.

File: 1708.02182_note.txt. Files named <arxiv_id>.txt are papers; files named <arxiv_id>_note.txt are third-party reading notes about that paper.

Read the document below and return every result it reports that is relevant to the task above.

Rules:
1. Extract only results that this document itself reports for the OWN proposed model(s) of the paper it is about. For a paper file that means the model(s) the paper itself proposes; for a third-party reading note that means the results the note states about the paper it is about. Do not create records for numbers the document attributes to other authors' models (baselines, prior work, comparison rows).
2. One record per configuration: if the document reports several values for its own model (different sizes, with or without fine-tuning, with or without a cache or pointer, with or without dynamic evaluation, single model or ensemble), give each of them its own record.
3. "value" must be the number exactly as written in the document, as a string.
4. "verbatim_quote" must be copied exactly from the document and be 40 words or fewer.
5. Put "unknown" in any field you cannot determine from the document. Do not omit a result because you are uncertain about it; record it with "unknown" fields and a lower confidence.
6. Never add a fact, a number or a qualification that is not in the document.
7. "source_file" is the file name given above, and "source_kind" is exactly what that file name implies: "paper" for <arxiv_id>.txt, "note" for <arxiv_id>_note.txt.

Return ONLY a JSON object of this shape:
{"records": [{"source_file": "<file name>", "source_kind": "paper|note", "paper_id": "<arxiv id the result belongs to>", "model": "<model the value is for>", "dataset": "<dataset and level>", "metric": "<metric>", "value": "<string, exactly as written>", "setting": {"dynamic_eval": "yes|no|unknown", "cache_pointer": "yes|no|unknown", "ensemble": "yes|no|unknown", "fine_tuning": "yes|no|unknown"}, "verbatim_quote": "<40 words or fewer, copied exactly>", "location": "<section or table as named in the text>", "confidence": 0.0, "notes": "<short qualification, or empty>"}]}

DOCUMENT TEXT (1708.02182_note.txt):

<DOCUMENT TEXT>
```

### Merge system prompt

```
You are a careful research assistant. You are given extraction records that were produced by reading each source document separately, and you must answer the user's task from those records alone. Never write a value that does not appear in the records.
```

### Merge user prompt (records JSON elided)

```
USER TASK:
Q1: Across the provided papers, which paper reports the lowest word-level test perplexity on the Penn Treebank for a single model without dynamic evaluation, cache or pointer augmentation, and what is that value? Rank the papers by this number.
Q2: For each of the provided papers, list the word-level Penn Treebank test perplexity the paper reports for its own proposed model (best single-model result without dynamic evaluation or cache), as a table with the paper title and the number.

Below are the extraction records. Each record carries the source_file it was taken from. Files named <arxiv_id>.txt are papers; files named <arxiv_id>_note.txt are third-party reading notes about that paper.

Answer in two parts.
Part 1: a short prose answer to Q1 and to Q2 (at most 250 words).
Part 2: at the very end of your reply, a single JSON object inside a ```json fence, of this shape:
{"table": [{"paper_id": "<arxiv id>", "paper_title_or_id": "<title if the records give one, otherwise the arxiv id>", "value": "<chosen value>", "setting": {"dynamic_eval": "yes|no|unknown", "cache_pointer": "yes|no|unknown", "ensemble": "yes|no|unknown", "fine_tuning": "yes|no|unknown"}, "provenance": ["<source_file>", "..."], "secondary_only": false, "note": "<short qualification, or empty>"}], "ranking": [{"rank": 1, "paper_id": "<arxiv id>", "value": "<value>"}], "q1_answer": "<one or two sentences>", "conflicts": [{"paper_id": "<arxiv id>", "paper_value": "<value in the paper records>", "note_value": "<value in the note records>", "resolution": "<which one you used and why>"}]}

Rules:
- For each paper give one table row, and choose the one value that meets the condition in the user task: the paper's own proposed model, a single model, no dynamic evaluation, no cache or pointer augmentation.
- "provenance" must list exactly the source_file(s) whose records support the value you chose. Do not list a source_file whose records do not support it.
- "secondary_only" is true when no record from a paper file (<arxiv_id>.txt) supports the chosen value, that is, the value rests only on a third-party reading note; otherwise it is false.
- "conflicts" must list every disagreement between the records of a paper file and the records of the reading note about that same paper.
- Do not invent values: every value you write must appear in the records.
- If no record supports a value for some paper, say so in that row instead of guessing.

RECORDS (JSON):

<RECORDS JSON>
```
