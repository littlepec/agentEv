B3 first pass (2026-09-14, 5 calls, $0.0289) superseded: the planner put answer numbers (106/163) into the search
queries, so the fixed "Key questions addressed" header carried the faithful number 163 and no L' candidate could
satisfy both "header unchanged" and "163 absent". Candidate bodies 1 and 3 did assert the target (103/209) correctly;
candidate 2 edited the header. Harness fix: queries sanitized to contain no digits (planner prompt + deterministic
rule); plan.json and call_plan.json reused; L and L' regenerated. All three superseded candidates kept here.
