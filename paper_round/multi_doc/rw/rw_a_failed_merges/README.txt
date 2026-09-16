RW-a merge artifacts, preserved read-only before the RW-b rerun (2026-09-15).

Configuration that produced these: thinking ENABLED (no "thinking" field), no response_format,
max_tokens 16384. Outcome: 10/10 merge cells failed as technical failures.
  A_rep1            : 15627 reasoning tokens, 757 left for content -> JSON cut mid-row 5 of 11
  B/C/Df/Dp rep1    : 16384/16384 reasoning tokens, EMPTY content, twice each (1 retry)
  A/B/C/Df/Dp rep2  : never called (rep2 extraction caches incomplete) -- no cost
9 paid calls, $0.2894. A_rep1's prose answer was complete and correct (MoS 54.44 top, 11/11
ranking values matching truth or an acceptable variant); only its JSON was truncated.

These files are kept because the RW-b rerun writes to the same paths. Nothing here is edited.
