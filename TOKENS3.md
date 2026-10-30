# Cycle 3 — run and token ledger

Method (same convention as `TOKENS2.md`): token figures are **estimates**
per run, assessed by the coordinator from each run's transcript length,
tool-call volume, and computation time, stated as ranges with a central
value; treat as accurate to roughly ±30%. Wall times for computation
runs are as reported in the certified files and are machine-dependent
(shared 2-core VM); they feed no count in `CYCLE3.md`.

## Runs

| # | Run | Role | Output files | Est. tokens (central) | Range |
|---|-----|------|--------------|----------------------|-------|
| 1 | P-I1 | Prover, Cluster I (even residual, route 1) | `proofs/P-I1.md`, `proofs/P-I1_checks.py` | 150k | 110k–200k |
| 2 | P-I2 | Prover, Cluster I (even residual, route 2) | `proofs/P-I2.md`, `proofs/P-I2_checks.py` | 140k | 100k–190k |
| 3 | P-J1 | Prover, Cluster J (v₂ + comparisons, route 1) | `proofs/P-J1.md`, `proofs/P-J1_checks.py` | 170k | 120k–230k |
| 4 | P-J2 | Prover, Cluster J (v₂ + comparisons, route 2) | `proofs/P-J2.md`, `proofs/P-J2_checks.py` | 150k | 110k–200k |
| 5 | C-K1 | Computer, Cluster K (per-pair frontier) | `proofs/P-K1.md`, `proofs/P-K1_checks.py` | 160k | 120k–210k |
| 6 | C-K2 | Computer, Cluster K (survivor search + families) | `proofs/P-K2.md`, `proofs/P-K2_checks.py` | 130k | 95k–175k |
| 7 | P-L1 | Prover, Cluster L ((LD3⁺), route 1) | `proofs/P-L1.md`, `proofs/P-L1_checks.py` | 110k | 80k–150k |
| 8 | P-L2 | Prover, Cluster L ((LD3⁺), route 2) | `proofs/P-L2.md`, `proofs/P-L2_checks.py` | 120k | 85k–160k |
| 9 | V-I | Verifier, Cluster I | `verification/V-I.md`, `verification/V-I_checks.py` | 140k | 100k–190k |
| 10 | V-J | Verifier, Cluster J | `verification/V-J.md`, `verification/V-J_checks.py` | 170k | 120k–230k |
| 11 | V-K | Verifier, Cluster K | `verification/V-K.md`, `verification/V-K_checks.py` | 200k | 145k–270k |
| 12 | V-L | Verifier, Cluster L | `verification/V-L.md`, `verification/V-L_checks.py` | 160k | 115k–215k |

Child-run subtotal: **≈ 1.80M tokens** (range ≈ 1.30M–2.42M).

Coordinator (brief drafting from the Cycle 1–2 record, cluster
adjudication, cross-cluster combination checks, independent spot-checks,
synthesis of `CYCLE3.md` and this ledger): **≈ 350k** (range
250k–450k).

## Total

**Cycle 3 total: ≈ 2.1M tokens** (range ≈ 1.7M–2.6M), across 12 child
runs plus coordination. For calibration against the campaign's earlier
estimates: this is the same order as Cycle 2's measured ledger
(~2M), and roughly 5–10× below the 8–12M per-cycle figures quoted in
early planning, consistent with the corrected calibration recorded in
`TOKENS2.md`.

## Notes

- All computation was exact, Python standard library only, at most 2
  workers, per the cycle method. The heaviest single enumerations:
  Cluster K's per-pair extension to j ≤ 50,000 (5,653,872 pairs
  clause-tested) and the even-n survivor search to 10⁸ (922,011,091
  candidate pairs), each run twice independently and recounted in part
  by V-K with its own implementations.
- No run reported a result that entered `CYCLE3.md` without passing
  through its cluster verifier. Two numbers quoted in interim agent
  summaries during the cycle did not survive verification unchanged
  (P-K2's preliminary pair count, corrected pre-run and disclosed;
  P-L2's §F census transcription, self-caught and corrected, with the
  corrected figures independently reproduced by V-L); neither appears
  in the final report in its uncorrected form.
