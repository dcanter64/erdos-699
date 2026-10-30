# Erdős #699 Proof Campaign — Cycle 2 Token / Run Ledger

**Convention (as in TOKENS.md):** exact per-agent token counts are not
visible to the coordinator. Figures are estimates inferred from run
size (input context carried, deliverable length, amount of computation
scripted and re-run), stated as ranges. They are for capacity
accounting only and carry no claim about the mathematics. Cycle 1's
measured actuals (~1–3M tokens per cycle all-in) anchor the ranges.

## Runs

| # | Run | Role | Est. tokens |
|---|---|---|---:|
| 1 | P-E1 | Prover, Cluster E (S7), route 1 | 80k–160k |
| 2 | P-E2 | Prover, Cluster E, route 2 | 80k–160k |
| 3 | P-F1 | Prover, Cluster F ($i = 3$), route 1 | 80k–160k |
| 4 | P-F2 | Prover, Cluster F, route 2 | 80k–160k |
| 5 | P-G1 | Prover, Cluster G (S4 flanks), route 1 | 80k–160k |
| 6 | P-G2 | Prover, Cluster G, route 2 | 80k–160k |
| 7 | P-H1 | Prover, Cluster H (S10 R1), route 1 | 80k–160k |
| 8 | P-H2 | Prover, Cluster H, route 2 (incl. 1093 s exact scan) | 80k–160k |
| 9 | HK-C | Primary-source verification (web) | 40k–80k |
| 10 | V-E | Verifier, Cluster E | 90k–170k |
| 11 | V-F | Verifier, Cluster F (incl. full (LD3) recounts) | 90k–170k |
| 12 | V-G | Verifier, Cluster G | 90k–170k |
| 13 | V-H | Verifier, Cluster H (incl. recount to $i = 2000$) | 90k–170k |
| 14 | HK-A | MaxDKaos reimplementation | 70k–130k |
| 15 | HK-B | Clearance recount (counts_c2) | 70k–130k |
| 16 | V-U | Audit verifier over HK-A/HK-B (incl. independent re-runs) | 70k–130k |

Child runs subtotal: **≈ 1.25M–2.47M tokens** (16 runs).

Coordinator (briefs, spot computations, error adjudication, synthesis,
CYCLE2.md): **≈ 200k–350k tokens**.

## Cycle 2 total (estimate)

**≈ 1.5M–2.8M tokens, order ~2M** — consistent with the Cycle 1
calibration (measured ledgers ~0.85–2M per cycle; the coordinator's
pre-launch habit of estimating ~10× too high is noted in the standing
record and was not repeated here).

Notes: several runs included one follow-up correction message inside
the same run (P-F2's count correction, P-H2's scan-total correction,
P-E2's citation question) — counted within the run, not as separate
runs. V-U's own session ended without its final chat message after
writing `verification/V-U.md` complete; the file was recovered from
disk and is the record. No run was re-dispatched in full.
