Q1: The lowest word-level PTB test perplexity for a single model without dynamic evaluation, cache, or pointer augmentation is reported by paper 1711.03953 (AWD-LSTM-MoS) at 54.44. The ranking by this value is: 1711.03953 (54.44), 1708.02182 (57.3), 1707.05589 (58.3), 1611.01578 (62.4), 1607.03474 (65.4), 1608.05859 (66.0), 1611.01462 (68.5), 1512.05287 (73.4 ± 0.0), 1409.2329 (78.4), 1508.06615 (78.9), 1706.02222 (87.38).

Q2: The table below gives each paper’s own proposed model’s best single-model PTB test perplexity without dynamic evaluation or cache. Values are taken from the records; where a paper reports multiple variants, the best qualifying single-model result is used.

```json
{
  "table": [
    {
      "paper_id": "1409.2329",
      "paper_title_or_id": "1409.2329",
      "value": "78.4",
      "setting": {"dynamic_eval": "no", "cache_pointer": "no", "ensemble": "no", "fine_tuning": "unknown"},
      "provenance": ["1409.2329.txt"],
      "secondary_only": false,
      "note": "Large regularized LSTM single model."
    },
    {
      "paper_id": "1508.06615",
      "paper_title_or_id": "1508.06615",
      "value": "78.9",
      "setting": {"dynamic_eval": "no", "cache_pointer": "no", "ensemble": "no", "fine_tuning": "unknown"},
      "provenance": ["1508.06615.txt"],
      "secondary_only": false,
      "note": "LSTM-Char-Large single model."
    },
    {
      "paper_id": "1512.05287",
      "paper_title_or_id": "1512.05287",
      "value": "73.4 ± 0.0",
      "setting": {"dynamic_eval": "no", "cache_pointer": "no", "ensemble": "no", "fine_tuning": "unknown"},
      "provenance": ["1512.05287.txt"],
      "secondary_only": false,
      "note": "Variational (untied weights, MC) LSTM large; best single model."
    },
    {
      "paper_id": "1607.03474",
      "paper_title_or_id": "1607.03474",
      "value": "65.4",
      "setting": {"dynamic_eval": "no", "cache_pointer": "no", "ensemble": "no", "fine_tuning": "unknown"},
      "provenance": ["1607.03474.txt"],
      "secondary_only": false,
      "note": "Variational RHN + WT single model."
    },
    {
      "paper_id": "1608.05859",
      "paper_title_or_id": "1608.05859",
      "value": "66.0",
      "setting": {"dynamic_eval": "no", "cache_pointer": "no", "ensemble": "no", "fine_tuning":