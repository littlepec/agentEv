{"answer_prose": "Q1: The lowest word-level Penn Treebank test perplexity for a single model without dynamic evaluation, cache/pointer augmentation, or ensembling is 53.3, reported by 1708.02182 (AWD-LSTM). Note that this result includes a fine-tuning step; the best value without fine-tuning is 55.97 (1711.03953, AWD-LSTM-MoS w/o finetune). Ranking (lowest to highest): 1708.02182 (53.3), 1711.03953 (55.97), 1707.05589 (58.3), 1611.01578 (62.4), 1607.03474 (65.4), 1611.01462 (68.5), 1512.05287 (73.4), 1608.05859 (74.3), 1508.06615 (78.9), 1409.2329 (78.4), 1706.02222 (87.38). Q2: See the table; each row gives the paper's own proposed model's best single-model word-level PTB test perplexity without dynamic evaluation or cache/pointer. Values for 1708.02182 rest only on a third-party note (no paper-file record was provided).",
  "table": [
    {"paper_id": "1409.2329", "paper_title_or_id": "1409.2329", "value": "78.4", "setting": {"dynamic_eval": "no", "cache_pointer": "no", "ensemble": "no", "fine_tuning": "unknown"}, "provenance": ["1409.2329.txt", "1409.2329_note.txt"], "secondary_only": false, "note": "Large regularized LSTM, best single model."},
    {"paper_id": "1508.06615", "paper_title_or_id": "1508.06615", "value": "78.9", "setting": {"dynamic_eval": "no", "cache_pointer": "no", "ensemble": "no", "fine_tuning": "unknown"}, "provenance": ["1508.06615.txt", "1508.06615_note.txt"], "secondary_only": false, "note": "LSTM-Char-Large, two highway layers."},
    {"paper_id": "1512.05287", "paper_title_or_id": "1512.05287", "value": "73.4", "setting": {"dynamic_eval": "no", "cache_pointer": "no", "ensemble": "no", "fine_tuning": "unknown"}, "provenance": ["1512.05287.txt", "1512.05287_note.txt"], "secondary_only": false, "note": "Variational LSTM, large, untied weights, MC dropout."},
    {"paper_id": "1607.03474", "paper_title_or_id": "1607.03474", "value": "65.4", "setting": {"dynamic_eval": "no", "cache_pointer": "no", "ensemble": "no", "fine_tuning": "unknown"}, "provenance": ["1607.03474.txt", "1607.03474_note.txt"], "secondary_only": false, "note": "Variational RHN + WT."},
    {"paper_id": "1608.05859", "paper_title_or_id": "1608.05859", "value": "74.3", "setting": {"dynamic_eval": "no", "cache_pointer": "no", "ensemble": "no", "fine_tuning": "unknown"}, "provenance": ["1608.05859.txt", "1608.05859_note.txt"], "secondary_only": false, "note": "Large + Weight Tying."},
    {"paper_id": "1611.01462", "paper_title_or_id": "1611.01462", "value": "68.5", "setting": {"dynamic_eval": "no", "cache_pointer": "no", "ensemble": "no", "fine_tuning": "unknown"}, "provenance": ["1611.01462.txt", "1611.01462_note.txt"], "secondary_only": false, "note": "VD-LSTM+REAL (large, 1500 units)."},
    {"paper_id": "1611.01578", "paper_title_or_id": "1611.01578", "value": "62.4", "setting": {"dynamic_eval": "no", "cache_pointer": "no", "ensemble": "no", "fine_tuning": "unknown"}, "provenance": ["1611.01578.txt", "1611.01578_note.txt"], "secondary_only": false, "note": "NAS with base 8 and shared embeddings, 54M."},
    {"paper_id": "1706.02222", "paper_title_or_id": "1706.02222", "value": "87.38", "setting": {"dynamic_eval": "no", "cache_pointer": "no", "ensemble": "no", "fine_tuning": "unknown"}, "provenance": ["1706.02222.txt", "1706.02222_note.txt"], "secondary_only": false, "note": "GRURNTN (proposed); best of the two proposed variants."},
    {"paper_id": "1707.05589", "paper_title_or_id": "1707.05589", "value": "58.3", "setting": {"dynamic_eval": "no", "cache_pointer": "no", "ensemble": "no", "fine_tuning": "unknown"}, "provenance": ["1707.05589.txt", "1707.05589_note.txt"], "secondary_only": false, "note": "4-layer LSTM, 24M parameters."},
    {"paper_id": "1708.02182", "paper_title_or_id": "1708.02182", "value": "53.3", "setting": {"dynamic_eval": "no", "cache_pointer": "no", "ensemble": "no", "fine_tuning": "yes"}, "provenance": ["1708.02182_note.txt"], "secondary_only": true, "note": "AWD-LSTM; value rests only on the third-party note; includes fine-tuning."},
    {"paper_id": "1711.03953", "paper_title_or_id": "1711.03953", "value": "55.97", "setting": {"dynamic_eval": "no", "cache_pointer": "no", "ensemble": "no", "fine_tuning": "no"}, "provenance": ["1711.03953.txt", "1711.03953_note.txt"], "secondary_only": false, "note": "AWD-LSTM-MoS w/o finetune."}
  ],
  "ranking": [
    {"rank": 1, "paper_id": "1708.02182", "value": "53.3"},
    {"rank": 2, "paper_id": "1711.03953", "value": "55.97"},
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
  "q1_answer": "The lowest word-level Penn Treebank test perplexity for a single model without dynamic evaluation, cache/pointer augmentation, or ensembling is 53.3, reported by 1708.02182 (AWD-LSTM, with fine-tuning). Ranking by this number: 1708.02182 (53.3) < 1711.03953 (55.97) < 1707.05589 (58.3) < 1611.01578 (62.4) < 1607.03474 (65.4) < 1611.01462 (68.5) < 1512.05287 (73.4) < 1608.05859 (74.3) < 1409.2329 (78.4) < 1508.06615 (78.9) < 1706.02222 (87.38).",
  "conflicts": [
    {"paper_id": "1409.2329", "paper_value": "fine_tuning: unknown", "note_value": "fine_tuning: no", "resolution": "Used the paper record's 'unknown' for fine-tuning; the paper table does not state a fine-tuning setting, while the note asserts none."},
    {"paper_id": "1512.05287", "paper_value": "setting fields for the 73.4 result: dynamic_eval no, cache_pointer no, ensemble no", "note_value": "setting fields for the 73.4 result: dynamic_eval unknown, cache_pointer unknown, ensemble unknown", "resolution": "Used the paper record's explicit 'no' settings, which support the no-dynamic-eval/no-cache condition."},
    {"paper_id": "1611.01462", "paper_value": "VD-LSTM+REAL (large) 68.5", "note_value": "VD-LSTM+REAL (large) 68.5", "resolution": "No numeric conflict; both agree on 68.5."},
    {"paper_id": "1706.02222", "paper_value": "fine_tuning: unknown", "note_value": "fine_tuning: unknown", "resolution": "No conflict; both leave fine-tuning unknown."}
  ]
}