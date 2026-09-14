#!/usr/bin/env python3
"""Budget guard — unified PRE-request reservation + cumulative check + ledger-anomaly stop.

Fix (1) for the new round: before every model request, reserve estimated cost/output,
re-read the ledger and check cumulative cost / call-count / tokens against hard caps,
and STOP adding new calls if the ledger looks anomalous. Reusable by new-round runners
and by the per-report freeze arithmetic (reserve est per-GPT-Researcher-report cost
before launching each report).

Ledger: F:/defense/defense_injection/defense-audit-work/runs/budget.sqlite
table calls(id, exp_key, status, reserved_cost, reserved_output, cost,
            input_tokens, output_tokens, data, created)

No model calls here. Read-only against the ledger except append via record().
"""
from __future__ import annotations
import sqlite3, datetime, json, math, pathlib

LEDGER = pathlib.Path("F:/defense/defense_injection/defense-audit-work/runs/budget.sqlite")

class BudgetStop(Exception):
    """Raised (or returned) when a cap is hit or the ledger is anomalous."""

class BudgetGuard:
    def __init__(self, exp_key, exp_prefix=None, cost_cap=5.0, call_cap=200,
                 in_tok_cap=5_000_000, out_tok_cap=2_000_000, ledger=LEDGER, spike_factor=20.0):
        self.exp_key = exp_key
        # caps are enforced on the ROUND scope (exp_key LIKE prefix%), NOT the global ledger,
        # matching how the <=$5 research cap has always been tracked (evidence-package-pilot*).
        self.exp_prefix = exp_prefix if exp_prefix is not None else exp_key
        self.cost_cap = cost_cap; self.call_cap = call_cap
        self.in_tok_cap = in_tok_cap; self.out_tok_cap = out_tok_cap
        self.ledger = pathlib.Path(ledger); self.spike_factor = spike_factor
        self.reserved_cost = 0.0; self.reserved_out = 0

    # ---- ledger read / anomaly detection ----
    def _totals(self):
        """Returns round-scoped (cost, calls, in_tok, out_tok) for exp_prefix% PLUS a global
        max-call cost for anomaly detection. Round scope is what the caps apply to."""
        if not self.ledger.exists():
            raise BudgetStop(f"ledger missing: {self.ledger}")
        try:
            c = sqlite3.connect(str(self.ledger), timeout=30)
            like = self.exp_prefix + "%"
            row = c.execute("select coalesce(sum(cost),0), count(*), "
                            "coalesce(sum(input_tokens),0), coalesce(sum(output_tokens),0) "
                            "from calls where exp_key like ?", (like,)).fetchone()
            mx_round = c.execute("select coalesce(max(cost),0) from calls where exp_key like ?", (like,)).fetchone()[0]
            mx_global = c.execute("select coalesce(max(cost),0) from calls").fetchone()[0]
            c.close()
        except Exception as e:
            raise BudgetStop(f"ledger read error: {type(e).__name__}: {e}")
        cost, calls, itok, otok = row
        # anomaly checks (round + global)
        for name, v in [("cost", cost), ("in_tok", itok), ("out_tok", otok),
                        ("max_round", mx_round), ("max_global", mx_global)]:
            if v is None or (isinstance(v, float) and (math.isnan(v) or math.isinf(v))) or v < 0:
                raise BudgetStop(f"ledger anomaly: {name}={v!r}")
        return float(cost), int(calls), int(itok), int(otok), float(mx_round)

    def preflight(self, est_cost, est_out_tokens, est_in_tokens=0):
        """Call BEFORE each request. Reserves est, checks ROUND-scoped cumulative+reserved
        vs caps and ledger anomaly. Returns (ok, reason). ok=False => do NOT make the call."""
        try:
            cost, calls, itok, otok, mx = self._totals()
        except BudgetStop as e:
            return False, f"STOP(anomaly): {e}"
        # spike check: a single prior call costing >spike_factor x the intended reservation
        if est_cost > 0 and mx > self.spike_factor * max(est_cost, 1e-9):
            return False, f"STOP(spike): a ledger call cost ${mx:.4f} >> est ${est_cost:.4f}; investigate before continuing"
        proj_cost = cost + self.reserved_cost + est_cost
        proj_calls = calls + 1
        proj_out = otok + self.reserved_out + est_out_tokens
        proj_in = itok + est_in_tokens
        if proj_cost > self.cost_cap:  return False, f"STOP(cost): projected ${proj_cost:.4f} > cap ${self.cost_cap}"
        if proj_calls > self.call_cap: return False, f"STOP(calls): projected {proj_calls} > cap {self.call_cap}"
        if proj_out > self.out_tok_cap: return False, f"STOP(out_tok): projected {proj_out} > cap {self.out_tok_cap}"
        if proj_in > self.in_tok_cap:  return False, f"STOP(in_tok): projected {proj_in} > cap {self.in_tok_cap}"
        # passed -> hold the reservation until record() settles it
        self.reserved_cost += est_cost; self.reserved_out += est_out_tokens
        return True, f"OK(reserved est ${est_cost:.4f}; global cum ${cost:.4f}/{self.cost_cap})"

    def record(self, actual_cost, in_tok, out_tok, data=None, status="ok",
               est_cost=0.0, est_out=0):
        """Call AFTER the request. Settles the reservation and appends the real row."""
        self.reserved_cost = max(0.0, self.reserved_cost - est_cost)
        self.reserved_out = max(0, self.reserved_out - est_out)
        try:
            c = sqlite3.connect(str(self.ledger), timeout=30)
            c.execute("insert into calls(exp_key,status,reserved_cost,reserved_output,cost,"
                      "input_tokens,output_tokens,data,created) values(?,?,?,?,?,?,?,?,?)",
                      (self.exp_key, status, actual_cost, out_tok, actual_cost, in_tok, out_tok,
                       json.dumps(data or {}, ensure_ascii=False),
                       datetime.datetime.now().isoformat(timespec="seconds")))
            c.commit(); c.close(); return True
        except Exception as e:
            return f"ledger_error: {type(e).__name__}: {e}"

if __name__ == "__main__":
    # self-test (read-only, no model calls): scope caps to the research line's exp_key prefix
    g = BudgetGuard("evidence-package-pilot-selftest", exp_prefix="evidence-package-pilot",
                    cost_cap=5.0, call_cap=400)
    try:
        cost, calls, itok, otok, mx = g._totals()
        print(f"round(evidence-package-pilot*): cum_cost=${cost:.4f} calls={calls} "
              f"in={itok} out={otok} max_call=${mx:.4f}")
        ok, why = g.preflight(est_cost=0.05, est_out_tokens=4000)
        print("preflight(est $0.05):", ok, "-", why)
    except BudgetStop as e:
        print("BUDGET STOP:", e)
