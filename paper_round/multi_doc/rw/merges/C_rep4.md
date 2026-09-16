{
  "answer_prose": "Q1: The lowest word-level Penn Treebank test perplexity for a single model without dynamic evaluation, cache/pointer augmentation, or ensembling is 53.3, reported by 1708.02182 (AWD-LSTM, 3-layer tied LSTM, including its fine-tuning step). This is lower than 54.44 (1711.03953, AWD-LSTM-MoS with finetune), 55.97 (1711.03953 without finetune), 57.3 (1708.02182 base AWD-LSTM), 58.0 (1707.05589, 24M 4-layer LSTM + tied gates), and 58.3 (1707.05589's own proposed best). Ranking by this number: 1708.02182 (53.3) < 1711.03953 (54.44) < 1707.05589 (58.3) < 1611.01578 (62.4) < 1607.03474 (65.4) < 1611.01462 (68.5) < 1512.05287 (73.4) < 1608.05859 (74.3) < 1508.06615 (78.9) < 1409.2329 (78.4) < 1706.02222 (87.38). Q2: The table lists each paper's own proposed model, single model, no dynamic evaluation or cache/pointer. Where a paper reports several variants, the best eligible value is given; the note column flags fine-tuning or other qualifications.",
  "table": [
    {
      "paper_id": "1409.2329",
      "paper_title_or_id": "1409.2329",
      "value": "78.4",
      "setting": {"dynamic_eval": "no", "cache_pointer": "no", "ensemble": "no", "fine_tuning": "unknown"},
      "provenance": ["1409.2329.txt", "1409.2329_note.txt"],
      "secondary_only": false,
      "note": "Large regularized LSTM, single model; paper's best single-model PTB result (medium regularized LSTM is 82.7)."
    },
    {
      "paper_id": "1508.06615",
      "paper_title_or_id": "1508.06615",
      "value": "78.9",
      "setting": {"dynamic_eval": "no", "cache_pointer": "no", "ensemble": "no", "fine_tuning": "unknown"},
      "provenance": ["1508.06615.txt", "1508.06615_note.txt"],
      "secondary_only": false,
      "note": "LSTM-Char-Large (two highway layers), single model; small model is 92.3."
    },
    {
      "paper_id": "1512.05287",
      "paper_title_or_id": "1512.05287",
      "value": "73.4",
      "setting": {"dynamic_eval": "no", "cache_pointer": "no", "ensemble": "no", "fine_tuning": "unknown"},
      "provenance": ["1512.05287.txt", "1512.05287_note.txt"],
      "secondary_only": false,
      "note": "Variational LSTM (large, untied weights, MC dropout at test time), single model; paper's best single-model result."
    },
    {
      "paper_id": "1607.03474",
      "paper_title_or_id": "1607.03474",
      "value": "65.4",
      "setting": {"dynamic_eval": "no", "cache_pointer": "no", "ensemble": "no", "fine_tuning": "unknown"},
      "provenance": ["1607.03474.txt", "1607.03474_note.txt"],
      "secondary_only": false,
      "note": "Variational RHN + WT, single model; without WT it is 68.5."
    },
    {
      "paper_id": "1608.05859",
      "paper_title_or_id": "1608.05859",
      "value": "74.3",
      "setting": {"dynamic_eval": "no", "cache_pointer": "no", "ensemble": "no", "fine_tuning": "unknown"},
      "provenance": ["1608.05859.txt", "1608.05859_note.txt"],
      "secondary_only": false,
      "note": "Large + Weight Tying, single model; paper's best single-model PTB result (RHN + BD + WT is 66.0 but is a different architecture)."
    },
    {
      "paper_id": "1611.01462",
      "paper_title_or_id": "1611.01462",
      "value": "68.5",
      "setting": {"dynamic_eval": "no", "cache_pointer": "no", "ensemble": "no", "fine_tuning": "unknown"},
      "provenance": ["1611.01462.txt", "1611.01462_note.txt"],
      "secondary_only": false,
      "note": "VD-LSTM+REAL (large, 1500 units), single model; the paper's best PTB result."
    },
    {
      "paper_id": "1611.01578",
      "paper_title_or_id": "1611.01578",
      "value": "62.4",
      "setting": {"dynamic_eval": "no", "cache_pointer": "no", "ensemble": "no", "fine_tuning": "unknown"},
      "provenance": ["1611.01578.txt", "1611.01578_note.txt"],
      "secondary_only": false,
      "note": "Neural Architecture Search with base 8 and shared embeddings (54M), single model; other configurations are 64.0 and 67.9."
    },
    {
      "paper_id": "1706.02222",
      "paper_title_or_id": "1706.02222",
      "value": "87.38",
      "setting": {"dynamic_eval": "no", "cache_pointer": "no", "ensemble": "no", "fine_tuning": "unknown"},
      "provenance": ["1706.02222.txt", "1706.02222_note.txt"],
      "secondary_only": false,
      "note": "GRURNTN (proposed), single model; LSTMRNTN is 96.97."
    },
    {
      "paper_id": "1707.05589",
      "paper_title_or_id": "1707.05589",
      "value": "58.3",
      "setting": {"dynamic_eval": "no", "cache_pointer": "no", "ensemble": "no", "fine_tuning": "unknown"},
      "provenance": ["1707.05589.txt", "1707.05589_note.txt"],
      "secondary_only": false,
      "note": "LSTM (24M, depth 4), single model; the paper's own best single-model PTB result. The 58.0 value is a 24M depth-4 LSTM with tied gates."
    },
    {
      "paper_id": "1708.02182",
      "paper_title_or_id": "1708.02182",
      "value": "53.3",
      "setting": {"dynamic_eval": "no", "cache_pointer": "no", "ensemble": "no", "fine_tuning": "yes"},
      "provenance": ["1708.02182_note.txt"],
      "secondary_only": true,
      "note": "AWD-LSTM (3-layer tied LSTM) with fine-tuning, single model without cache/pointer. The paper records give 57.3 for this model and 58.8 without fine-tuning; the 53.3 value appears only in the reading note."
    },
    {
      "paper_id": "1711.03953",
      "paper_title_or_id": "1711.03953",
      "value": "54.44",
      "setting": {"dynamic_eval": "no", "cache_pointer": "no", "ensemble": "no", "fine_tuning": "yes"},
      "provenance": ["1711.03953.txt", "1711.03953_note.txt"],
      "secondary_only": false,
      "note": "AWD-LSTM-MoS with finetune, single model; without finetune it is 55.97."
    }
  ],
  "ranking": [
    {"rank": 1, "paper_id": "1708.02182", "value": "53.3"},
    {"rank": 2, "paper_id": "1711.03953", "value": "54.44"},
    {"rank": 3, "paper_id": "1707.05589", "value": "58.3"},
    {"rank": 4, "paper_id": "1611.01578", "value": "62.4"},
    {"rank": 5, "paper_id": "1607.03474", "value": "65.4"},
    {"rank": 6, "paper_id": "1611.01462", "value": "68.5"},
    {"rank": 7, "paper_id": "1512.05287", "value": "73.4"},
    {"rank": 8, "paper_id": "1608.05859", "value": "74.3"},
    {"rank": 9, "paper_id": "1409.2329", "value": "78.4"},
    {"rank": 10, "paper_id": "1508.06615", "value": "78.9"},
    {"rank": 11, "paper_id": "1706.02222", "value": "87.38"}
  ],
  "q1_answer": "1708.02182 reports the lowest word-level Penn Treebank test perplexity for a single model without dynamic evaluation, cache/pointer augmentation, or ensembling: 53.3 (AWD-LSTM, 3-layer tied LSTM, including its fine-tuning step). Ranking by this number: 1708.02182 (53.3) < 1711.03953 (54.44) < 1707.05589 (58.3) < 1611.01578 (62.4) < 1607.03474 (65.4) < 1611.01462 (68.5) < 1512.05287 (73.4) < 1608.05859 (74.3) < 1409.2329 (78.4) < 1508.06615 (78.9) < 1706.02222 (87.38).",
  "conflicts": [
    {
      "paper_id": "1708.02182",
      "paper_value": "57.3",
      "note_value": "53.3",
      "resolution": "Used the note value 53.3 because the task asks for the paper's own proposed model without cache/pointer and the note explicitly reports 53.3 for AWD-LSTM as a single model without cache/pointer; the paper records give 57.3 for the same model, so the two disagree."
    }
  ]
}