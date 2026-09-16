{
  "answer_prose": "Q1: Among the papers with paper-file support, the lowest word-level Penn Treebank test perplexity for a single model without dynamic evaluation, cache/pointer, or ensemble is 58.3, reported by 1707.05589 (4-layer LSTM, 24M parameters). Ranking by this number: 1707.05589 (58.3) < 1611.01578 (62.4) < 1607.03474 (65.4) < 1611.01462 (68.5) < 1512.05287 (73.4) < 1608.05859 (74.3) < 1409.2329 (78.4) < 1508.06615 (78.9) < 1706.02222 (87.38). 1711.03953's best single model without dynamic evaluation is 54.44, but it uses fine-tuning, so it is not eligible under the no-fine-tuning reading of the condition; its no-finetune value is 55.97. 1708.02182 is only supported by a reading note (53.3 with fine-tuning), so it is unverified and not ranked. Q2: see table.",
  "table": [
    {
      "paper_id": "1409.2329",
      "paper_title_or_id": "1409.2329",
      "value": "78.4",
      "setting": {"dynamic_eval": "no", "cache_pointer": "no", "ensemble": "no", "fine_tuning": "unknown"},
      "provenance": ["1409.2329.txt"],
      "secondary_only": false,
      "note": "Large regularized LSTM single-model row; medium regularized LSTM is 82.7."
    },
    {
      "paper_id": "1508.06615",
      "paper_title_or_id": "1508.06615",
      "value": "78.9",
      "setting": {"dynamic_eval": "no", "cache_pointer": "no", "ensemble": "no", "fine_tuning": "unknown"},
      "provenance": ["1508.06615.txt"],
      "secondary_only": false,
      "note": "LSTM-Char-Large, 19M parameters."
    },
    {
      "paper_id": "1512.05287",
      "paper_title_or_id": "1512.05287",
      "value": "73.4",
      "setting": {"dynamic_eval": "no", "cache_pointer": "no", "ensemble": "no", "fine_tuning": "unknown"},
      "provenance": ["1512.05287.txt"],
      "secondary_only": false,
      "note": "Variational (untied weights, MC) LSTM, large; best single-model result."
    },
    {
      "paper_id": "1607.03474",
      "paper_title_or_id": "1607.03474",
      "value": "65.4",
      "setting": {"dynamic_eval": "no", "cache_pointer": "no", "ensemble": "no", "fine_tuning": "unknown"},
      "provenance": ["1607.03474.txt"],
      "secondary_only": false,
      "note": "Variational RHN + WT; Variational RHN alone is 68.5."
    },
    {
      "paper_id": "1608.05859",
      "paper_title_or_id": "1608.05859",
      "value": "74.3",
      "setting": {"dynamic_eval": "no", "cache_pointer": "no", "ensemble": "no", "fine_tuning": "unknown"},
      "provenance": ["1608.05859.txt"],
      "secondary_only": false,
      "note": "Large + Weight Tying; RHN + BD + WT is 66.0 but is an RHN variant."
    },
    {
      "paper_id": "1611.01462",
      "paper_title_or_id": "1611.01462",
      "value": "68.5",
      "setting": {"dynamic_eval": "no", "cache_pointer": "no", "ensemble": "no", "fine_tuning": "unknown"},
      "provenance": ["1611.01462.txt"],
      "secondary_only": false,
      "note": "VD-LSTM+REAL (large, 1500 units)."
    },
    {
      "paper_id": "1611.01578",
      "paper_title_or_id": "1611.01578",
      "value": "62.4",
      "setting": {"dynamic_eval": "no", "cache_pointer": "no", "ensemble": "no", "fine_tuning": "unknown"},
      "provenance": ["1611.01578.txt"],
      "secondary_only": false,
      "note": "Neural Architecture Search with base 8 and shared embeddings, 54M parameters."
    },
    {
      "paper_id": "1706.02222",
      "paper_title_or_id": "1706.02222",
      "value": "87.38",
      "setting": {"dynamic_eval": "no", "cache_pointer": "no", "ensemble": "no", "fine_tuning": "unknown"},
      "provenance": ["1706.02222.txt"],
      "secondary_only": false,
      "note": "GRURNTN (proposed); LSTMRNTN is 96.97."
    },
    {
      "paper_id": "1707.05589",
      "paper_title_or_id": "1707.05589",
      "value": "58.3",
      "setting": {"dynamic_eval": "no", "cache_pointer": "no", "ensemble": "no", "fine_tuning": "unknown"},
      "provenance": ["1707.05589.txt"],
      "secondary_only": false,
      "note": "LSTM (24M, depth 4); best single-model PTB test perplexity in the paper."
    },
    {
      "paper_id": "1711.03953",
      "paper_title_or_id": "1711.03953",
      "value": "54.44",
      "setting": {"dynamic_eval": "no", "cache_pointer": "no", "ensemble": "no", "fine_tuning": "yes"},
      "provenance": ["1711.03953.txt"],
      "secondary_only": false,
      "note": "AWD-LSTM-MoS with finetuning; without finetuning the value is 55.97. The 47.69 result uses dynamic evaluation and is excluded."
    }
  ],
  "ranking": [
    {"rank": 1, "paper_id": "1707.05589", "value": "58.3"},
    {"rank": 2, "paper_id": "1611.01578", "value": "62.4"},
    {"rank": 3, "paper_id": "1607.03474", "value": "65.4"},
    {"rank": 4, "paper_id": "1611.01462", "value": "68.5"},
    {"rank": 5, "paper_id": "1512.05287", "value": "73.4"},
    {"rank": 6, "paper_id": "1608.05859", "value": "74.3"},
    {"rank": 7, "paper_id": "1409.2329", "value": "78.4"},
    {"rank": 8, "paper_id": "1508.06615", "value": "78.9"},
    {"rank": 9, "paper_id": "1706.02222", "value": "87.38"}
  ],
  "q1_answer": "The lowest word-level Penn Treebank test perplexity for a single model without dynamic evaluation, cache/pointer, or ensemble is 58.3, reported by paper 1707.05589 (4-layer LSTM, 24M parameters). Ranking (lowest to highest): 1707.05589 58.3; 1611.01578 62.4; 1607.03474 65.4; 1611.01462 68.5; 1512.05287 73.4; 1608.05859 74.3; 1409.2329 78.4; 1508.06615 78.9; 1706.02222 87.38.",
  "conflicts": [
    {
      "paper_id": "1409.2329",
      "paper_value": "fine_tuning: unknown",
      "note_value": "fine_tuning: no",
      "resolution": "Used the paper file's value (unknown); the paper file does not report a fine-tuning setting, while the note asserts 'no'."
    },
    {
      "paper_id": "1512.05287",
      "paper_value": "fine_tuning: unknown",
      "note_value": "fine_tuning: no",
      "resolution": "Used the paper file's value (unknown); the note asserts 'no' for fine-tuning, which the paper file does not state."
    },
    {
      "paper_id": "1607.03474",
      "paper_value": "fine_tuning: unknown",
      "note_value": "fine_tuning: no",
      "resolution": "Used the paper file's value (unknown); the note asserts 'no' for fine-tuning, which the paper file does not state."
    },
    {
      "paper_id": "1608.05859",
      "paper_value": "fine_tuning: unknown",
      "note_value": "fine_tuning: no",
      "resolution": "Used the paper file's value (unknown); the note asserts 'no' for fine-tuning, which the paper file does not state."
    },
    {
      "paper_id": "1611.01462",
      "paper_value": "fine_tuning: unknown",
      "note_value": "fine_tuning: no",
      "resolution": "Used the paper file's value (unknown); the note asserts 'no' for fine-tuning, which the paper file does not state."
    },
    {
      "paper_id": "1611.01578",
      "paper_value": "fine_tuning: unknown",
      "note_value": "fine_tuning: no",
      "resolution": "Used the paper file's value (unknown); the note asserts 'no' for fine-tuning, which the paper file does not state."
    },
    {
      "paper_id": "1707.05589",
      "paper_value": "fine_tuning: unknown",
      "note_value": "fine_tuning: no",
      "resolution": "Used the paper file's value (unknown); the note asserts 'no' for fine-tuning, which the paper file does not state."
    }
  ],
  "unverified": [
    {
      "paper_id": "1708.02182",
      "paper_title_or_id": "1708.02182",
      "value": "53.3",
      "setting": {"dynamic_eval": "no", "cache_pointer": "no", "ensemble": "no", "fine_tuning": "yes"},
      "provenance": ["1708.02182_note.txt"],
      "secondary_only": true,
      "note": "Only a reading note is available for this paper; the note reports 53.3 for AWD-LSTM (3-layer LSTM with tied weights) with fine-tuning, and 58.8 without fine-tuning."
    }
  ]
}