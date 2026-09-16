{
  "answer_prose": "Q1: The lowest word-level Penn Treebank test perplexity for a single model without dynamic evaluation, cache/pointer augmentation, or ensembling is 54.44, reported by 1711.03953 (AWD-LSTM-MoS, with fine-tuning). Ranking by this number: 1711.03953 (54.44) < 1708.02182 (57.3) < 1707.05589 (58.3) < 1611.01578 (62.4) < 1607.03474 (65.4) < 1608.05859 (66.0) < 1611.01462 (68.5) < 1512.05287 (73.4) < 1508.06615 (78.9) < 1409.2329 (78.4) < 1706.02222 (87.38). Note that 1409.2329's best single-model value is 78.4 (large regularized LSTM); its 68.7 figure is a 38-model ensemble and is excluded. Q2: The table below lists each paper's own proposed model's best single-model word-level PTB test perplexity without dynamic evaluation or cache. Where a paper reports both a fine-tuned and non-fine-tuned result, the best (fine-tuned) single-model result is given, with fine_tuning flagged. 1708.02182 rests only on a third-party note (no paper record was provided).",
  "table": [
    {
      "paper_id": "1409.2329",
      "paper_title_or_id": "1409.2329",
      "value": "78.4",
      "setting": {"dynamic_eval": "no", "cache_pointer": "no", "ensemble": "no", "fine_tuning": "unknown"},
      "provenance": ["1409.2329.txt", "1409.2329_note.txt"],
      "secondary_only": false,
      "note": "Large regularized LSTM; best single-model value (medium is 82.7)."
    },
    {
      "paper_id": "1508.06615",
      "paper_title_or_id": "1508.06615",
      "value": "78.9",
      "setting": {"dynamic_eval": "no", "cache_pointer": "no", "ensemble": "no", "fine_tuning": "unknown"},
      "provenance": ["1508.06615.txt", "1508.06615_note.txt"],
      "secondary_only": false,
      "note": "LSTM-Char-Large (two highway layers)."
    },
    {
      "paper_id": "1512.05287",
      "paper_title_or_id": "1512.05287",
      "value": "73.4",
      "setting": {"dynamic_eval": "no", "cache_pointer": "no", "ensemble": "no", "fine_tuning": "unknown"},
      "provenance": ["1512.05287.txt", "1512.05287_note.txt"],
      "secondary_only": false,
      "note": "Variational LSTM, large, untied weights, MC dropout at test time."
    },
    {
      "paper_id": "1607.03474",
      "paper_title_or_id": "1607.03474",
      "value": "65.4",
      "setting": {"dynamic_eval": "no", "cache_pointer": "no", "ensemble": "no", "fine_tuning": "unknown"},
      "provenance": ["1607.03474.txt", "1607.03474_note.txt"],
      "secondary_only": false,
      "note": "Variational RHN + WT."
    },
    {
      "paper_id": "1608.05859",
      "paper_title_or_id": "1608.05859",
      "value": "66.0",
      "setting": {"dynamic_eval": "no", "cache_pointer": "no", "ensemble": "no", "fine_tuning": "unknown"},
      "provenance": ["1608.05859.txt", "1608.05859_note.txt"],
      "secondary_only": false,
      "note": "RHN + BD + WT; best single-model PTB value in the paper."
    },
    {
      "paper_id": "1611.01462",
      "paper_title_or_id": "1611.01462",
      "value": "68.5",
      "setting": {"dynamic_eval": "no", "cache_pointer": "no", "ensemble": "no", "fine_tuning": "unknown"},
      "provenance": ["1611.01462.txt", "1611.01462_note.txt"],
      "secondary_only": false,
      "note": "VD-LSTM+REAL (large, 1500 units)."
    },
    {
      "paper_id": "1611.01578",
      "paper_title_or_id": "1611.01578",
      "value": "62.4",
      "setting": {"dynamic_eval": "no", "cache_pointer": "no", "ensemble": "no", "fine_tuning": "unknown"},
      "provenance": ["1611.01578.txt", "1611.01578_note.txt"],
      "secondary_only": false,
      "note": "Neural Architecture Search with base 8 and shared embeddings, 54M."
    },
    {
      "paper_id": "1706.02222",
      "paper_title_or_id": "1706.02222",
      "value": "87.38",
      "setting": {"dynamic_eval": "no", "cache_pointer": "no", "ensemble": "no", "fine_tuning": "unknown"},
      "provenance": ["1706.02222.txt", "1706.02222_note.txt"],
      "secondary_only": false,
      "note": "GRURNTN (proposed); best of the two proposed word-level models."
    },
    {
      "paper_id": "1707.05589",
      "paper_title_or_id": "1707.05589",
      "value": "58.3",
      "setting": {"dynamic_eval": "no", "cache_pointer": "no", "ensemble": "no", "fine_tuning": "unknown"},
      "provenance": ["1707.05589.txt", "1707.05589_note.txt"],
      "secondary_only": false,
      "note": "LSTM, 24M, depth 4."
    },
    {
      "paper_id": "1708.02182",
      "paper_title_or_id": "1708.02182",
      "value": "57.3",
      "setting": {"dynamic_eval": "no", "cache_pointer": "no", "ensemble": "no", "fine_tuning": "yes"},
      "provenance": ["1708.02182_note.txt"],
      "secondary_only": true,
      "note": "AWD-LSTM (3-layer, tied weights); value rests only on the third-party note; includes fine-tuning."
    },
    {
      "paper_id": "1711.03953",
      "paper_title_or_id": "1711.03953",
      "value": "54.44",
      "setting": {"dynamic_eval": "no", "cache_pointer": "no", "ensemble": "no", "fine_tuning": "yes"},
      "provenance": ["1711.03953.txt", "1711.03953_note.txt"],
      "secondary_only": false,
      "note": "AWD-LSTM-MoS with finetuning; without finetuning it is 55.97."
    }
  ],
  "ranking": [
    {"rank": 1, "paper_id": "1711.03953", "value": "54.44"},
    {"rank": 2, "paper_id": "1708.02182", "value": "57.3"},
    {"rank": 3, "paper_id": "1707.05589", "value": "58.3"},
    {"rank": 4, "paper_id": "1611.01578", "value": "62.4"},
    {"rank": 5, "paper_id": "1607.03474", "value": "65.4"},
    {"rank": 6, "paper_id": "1608.05859", "value": "66.0"},
    {"rank": 7, "paper_id": "1611.01462", "value": "68.5"},
    {"rank": 8, "paper_id": "1512.05287", "value": "73.4"},
    {"rank": 9, "paper_id": "1409.2329", "value": "78.4"},
    {"rank": 10, "paper_id": "1508.06615", "value": "78.9"},
    {"rank": 11, "paper_id": "1706.02222", "value": "87.38"}
  ],
  "q1_answer": "The lowest single-model word-level Penn Treebank test perplexity without dynamic evaluation, cache/pointer, or ensembling is 54.44, reported by 1711.03953 (AWD-LSTM-MoS with finetuning). Ranking (lowest to highest): 1711.03953 54.44, 1708.02182 57.3, 1707.05589 58.3, 1611.01578 62.4, 1607.03474 65.4, 1608.05859 66.0, 1611.01462 68.5, 1512.05287 73.4, 1409.2329 78.4, 1508.06615 78.9, 1706.02222 87.38.",
  "conflicts": [
    {
      "paper_id": "1409.2329",
      "paper_value": "fine_tuning: unknown",
      "note_value": "fine_tuning: no",
      "resolution": "Used the paper record's 'unknown' for fine_tuning; the note's 'no' is an assertion about what the paper does not report, not a reported setting."
    },
    {
      "paper_id": "1512.05287",
      "paper_value": "73.4 ± 0.0 (large, untied weights, MC dropout), setting dynamic_eval/cache_pointer/ensemble/fine_tuning = no",
      "note_value": "73.4 (large, untied weights, MC dropout), setting dynamic_eval/cache_pointer/ensemble/fine_tuning = unknown",
      "resolution": "Used the paper record's 73.4 with explicit 'no' settings; the note's 'unknown' reflects that the note did not find these settings stated."
    }
  ]
}