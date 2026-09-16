{
  "answer_prose": "Across the provided papers, the lowest word-level Penn Treebank test perplexity for a single model without dynamic evaluation, cache/pointer augmentation, or ensembling is 58.0, reported by 1707.05589 (a 24M-parameter 4-layer LSTM with tied gates). The next lowest paper-supported single-model values are 58.3 (1707.05589's 24M 4-layer LSTM), 59.5 (1707.05589, 24M depth-1 LSTM), 59.6 (1707.05589, 10M depth-1 LSTM), and 62.4 (1611.01578, NAS with base 8 and shared embeddings, 54M). Note that 1708.02182's AWD-LSTM result (53.3, or 58.8 without fine-tuning) is supported only by a third-party reading note, not by a paper file, so it is listed as unverified and excluded from the ranking. For Q2, the table lists each paper's own proposed-model word-level PTB test perplexity under the stated condition. Where a paper reports several sizes, the best single-model value is given; for 1711.03953 the no-fine-tuning value 55.97 is used because the fine-tuned 54.44 involves fine-tuning, and 47.69 uses dynamic evaluation.",
  "table": [
    {
      "paper_id": "1409.2329",
      "paper_title_or_id": "1409.2329",
      "value": "78.4",
      "setting": {
        "dynamic_eval": "no",
        "cache_pointer": "no",
        "ensemble": "no",
        "fine_tuning": "unknown"
      },
      "provenance": ["1409.2329.txt"],
      "secondary_only": false,
      "note": "Large regularized LSTM, single model; best single-model row."
    },
    {
      "paper_id": "1508.06615",
      "paper_title_or_id": "1508.06615",
      "value": "78.9",
      "setting": {
        "dynamic_eval": "no",
        "cache_pointer": "no",
        "ensemble": "no",
        "fine_tuning": "unknown"
      },
      "provenance": ["1508.06615.txt"],
      "secondary_only": false,
      "note": "LSTM-Char-Large (19M), single model."
    },
    {
      "paper_id": "1512.05287",
      "paper_title_or_id": "1512.05287",
      "value": "73.4 ± 0.0",
      "setting": {
        "dynamic_eval": "no",
        "cache_pointer": "no",
        "ensemble": "no",
        "fine_tuning": "unknown"
      },
      "provenance": ["1512.05287.txt"],
      "secondary_only": false,
      "note": "Variational (untied weights, MC) LSTM, large; best single-model result."
    },
    {
      "paper_id": "1607.03474",
      "paper_title_or_id": "1607.03474",
      "value": "65.4",
      "setting": {
        "dynamic_eval": "no",
        "cache_pointer": "no",
        "ensemble": "no",
        "fine_tuning": "unknown"
      },
      "provenance": ["1607.03474.txt"],
      "secondary_only": false,
      "note": "Variational RHN + WT, single model."
    },
    {
      "paper_id": "1608.05859",
      "paper_title_or_id": "1608.05859",
      "value": "66.0",
      "setting": {
        "dynamic_eval": "no",
        "cache_pointer": "no",
        "ensemble": "no",
        "fine_tuning": "unknown"
      },
      "provenance": ["1608.05859.txt"],
      "secondary_only": false,
      "note": "RHN + BD + WT; best single-model PTB result in the paper."
    },
    {
      "paper_id": "1611.01462",
      "paper_title_or_id": "1611.01462",
      "value": "68.5",
      "setting": {
        "dynamic_eval": "no",
        "cache_pointer": "no",
        "ensemble": "no",
        "fine_tuning": "unknown"
      },
      "provenance": ["1611.01462.txt"],
      "secondary_only": false,
      "note": "VD-LSTM+REAL (large, 1500 units); best single-model proposed result."
    },
    {
      "paper_id": "1611.01578",
      "paper_title_or_id": "1611.01578",
      "value": "62.4",
      "setting": {
        "dynamic_eval": "no",
        "cache_pointer": "no",
        "ensemble": "no",
        "fine_tuning": "unknown"
      },
      "provenance": ["1611.01578.txt"],
      "secondary_only": false,
      "note": "NAS with base 8 and shared embeddings, 54M; single model."
    },
    {
      "paper_id": "1706.02222",
      "paper_title_or_id": "1706.02222",
      "value": "87.38",
      "setting": {
        "dynamic_eval": "no",
        "cache_pointer": "no",
        "ensemble": "no",
        "fine_tuning": "unknown"
      },
      "provenance": ["1706.02222.txt"],
      "secondary_only": false,
      "note": "GRURNTN (proposed); best proposed word-level PTB result."
    },
    {
      "paper_id": "1707.05589",
      "paper_title_or_id": "1707.05589",
      "value": "58.0",
      "setting": {
        "dynamic_eval": "no",
        "cache_pointer": "no",
        "ensemble": "no",
        "fine_tuning": "unknown"
      },
      "provenance": ["1707.05589.txt"],
      "secondary_only": false,
      "note": "LSTM (24M, depth 4, + Tied gates); best single-model PTB test perplexity."
    },
    {
      "paper_id": "1711.03953",
      "paper_title_or_id": "1711.03953",
      "value": "55.97",
      "setting": {
        "dynamic_eval": "no",
        "cache_pointer": "no",
        "ensemble": "no",
        "fine_tuning": "no"
      },
      "provenance": ["1711.03953.txt"],
      "secondary_only": false,
      "note": "AWD-LSTM-MoS w/o finetune; the 54.44 value uses fine-tuning and 47.69 uses dynamic evaluation."
    }
  ],
  "ranking": [
    {"rank": 1, "paper_id": "1707.05589", "value": "58.0"},
    {"rank": 2, "paper_id": "1611.01578", "value": "62.4"},
    {"rank": 3, "paper_id": "1607.03474", "value": "65.4"},
    {"rank": 4, "paper_id": "1608.05859", "value": "66.0"},
    {"rank": 5, "paper_id": "1611.01462", "value": "68.5"},
    {"rank": 6, "paper_id": "1512.05287", "value": "73.4 ± 0.0"},
    {"rank": 7, "paper_id": "1409.2329", "value": "78.4"},
    {"rank": 8, "paper_id": "1508.06615", "value": "78.9"},
    {"rank": 9, "paper_id": "1706.02222", "value": "87.38"},
    {"rank": 10, "paper_id": "1711.03953", "value": "55.97"}
  ],
  "q1_answer": "The lowest word-level Penn Treebank test perplexity for a single model without dynamic evaluation, cache/pointer augmentation, or ensembling is 58.0, reported by paper 1707.05589 (24M-parameter 4-layer LSTM with tied gates). Ranking by this number: 1707.05589 (58.0), 1611.01578 (62.4), 1607.03474 (65.4), 1608.05859 (66.0), 1611.01462 (68.5), 1512.05287 (73.4), 1409.2329 (78.4), 1508.06615 (78.9), 1706.02222 (87.38), 1711.03953 (55.97, no-fine-tuning setting).",
  "conflicts": [],
  "unverified": [
    {
      "paper_id": "1708.02182",
      "paper_title_or_id": "1708.02182",
      "value": "53.3",
      "setting": {
        "dynamic_eval": "no",
        "cache_pointer": "no",
        "ensemble": "no",
        "fine_tuning": "yes"
      },
      "provenance": ["1708.02182_note.txt"],
      "secondary_only": true,
      "note": "AWD-LSTM (3-layer LSTM with tied weights) with fine-tuning; supported only by the reading note, no paper file record."
    },
    {
      "paper_id": "1708.02182",
      "paper_title_or_id": "1708.02182",
      "value": "58.8",
      "setting": {
        "dynamic_eval": "no",
        "cache_pointer": "no",
        "ensemble": "no",
        "fine_tuning": "no"
      },
      "provenance": ["1708.02182_note.txt"],
      "secondary_only": true,
      "note": "No-fine-tuning ablation of AWD-LSTM; supported only by the reading note, no paper file record."
    }
  ]
}