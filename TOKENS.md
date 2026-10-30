# Erdős #699 Referee-and-Proof Campaign — Cycle 1 Token Ledger

**Honesty caveat (read first).** Exact per-agent token counts are not visible
to the coordinator. The figures below are estimates built from run counts,
document sizes produced, and the calibration of the sibling #488 campaign
(whose Cycle 1, a similar fan-out, came to roughly 0.85–1.6M tokens, about
10x below its pre-launch estimate). Treat every number here as
order-of-magnitude only. The user's own plan counter is the authoritative
total for the account; this ledger exists to show where the spend went by
stage, not to bill it exactly.

## Run counts

| Stage | Runs | Notes |
|---|---|---|
| Workstream A: text acquisition + bounded coordinator computations | coordinator (no child runs) | Fetched Bloom exposition and problem page; 403 routes documented; two bounded Python checks |
| Workstream A: referees | 2 | Referee 1 (reconstruction), Referee 2 (adversarial) |
| Workstream A: synthesis | coordinator | `REFEREE.md` |
| Workstream B: strategy round | 10 | S1–S10, one agent each; S7 also left two scripts |
| Workstream B: prover round | 8 | 4 clusters (A = S6+S8+S5, B = S1, C = S3, D = S4) × 2 independent provers |
| Workstream B: verifier round | 4 | V-A…V-D, one per cluster |
| Workstream B: synthesis | coordinator | Union computation (`verification/union_check.py`, ~5 s), `CYCLE1.md`, this ledger |
| **Total child runs** | **24** | Plus coordinator turns across both workstreams |

## Estimated token ranges

| Stage | Per run (est.) | Stage total (est.) |
|---|---|---|
| Referees (2) | 60k–120k | 120k–240k |
| Strategies (10) | 50k–110k | 500k–1,100k |
| Provers (8) | 70k–150k | 560k–1,200k |
| Verifiers (4) | 60k–130k | 240k–520k |
| Coordinator (acquisition, checks, selection, synthesis) | — | 150k–300k |
| **Cycle 1 total** | | **≈ 1.6M–3.4M tokens (order ~2M)** |

## Calibration notes

- The range is anchored on the #488 Cycle 1 experience (similar structure:
  strategy round, paired provers, verifiers; estimated 0.85–1.6M) scaled up
  for this campaign's larger strategy round (10 papers, several 500+ lines)
  and heavier verifier computations (V-D alone ran ~48M elementary checks;
  V-B and V-C each performed full independent recounts).
- Pre-launch-style estimates for campaigns of this shape have run roughly
  10x high in the sibling campaign; the ranges above are set from observed
  document volume, not from the pre-launch guess.
- Computation (CPU) is not tokens: the verifiers' Python checks, the S7
  sweeps, and the coordinator's union computation consumed machine time, not
  plan tokens, beyond the agents' own reasoning around them.
