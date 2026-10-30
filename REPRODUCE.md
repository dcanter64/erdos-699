# Reproduce

This file gives exact commands for rerunning the checks behind the results in this repository, in increasing cost order. Every command is written for the scripts as they actually are in this repository. Read the notes in each section before running the expensive steps.

## Environment

* Python 3 only. Every script uses the Python standard library alone; there are no third party packages to install. The sweep record (sweep/PROVENANCE.md) records CPython 3.12.3 on a Linux x86_64 machine for the production runs.
* The checks were developed and run on a 2 core virtual machine. Runtimes below are from that machine class and are guides, not guarantees.
* All arithmetic in the checks is exact Python integer arithmetic.
* Run the commands from the repository root unless a section says otherwise. Paths below are relative to the repository root.

## (a) Closed form count check (seconds)

The script sweep/count_closed_form.py takes the cap as an argument named nstar (default 10000) and an optional starting value nlo (default 2). Before printing a total it self checks: the printed output begins with the line stating that the closed form equals the direct per-n summation for all n ≤ 2000.

```bash
cd sweep
python3 count_closed_form.py
```

Expected output:

```text
self-check: closed form == direct per-n summation for all n <= 2000
open-region triples with 2 <= n <= 10000: 27769446111
```

That total, 27,769,446,111, matches sweep/sweep_summary_10000.json and sweep/count_closed_form_10000.txt.

For the larger cap, pass the argument explicitly:

```bash
python3 count_closed_form.py --nstar 20000
```

Expected output:

```text
self-check: closed form == direct per-n summation for all n <= 2000
open-region triples with 2 <= n <= 20000: 222188892222
```

That total, 222,188,892,222, matches sweep/sweep_summary_20000.json and sweep/count_closed_form_20000.txt.

## (b) Spot check of the cap 20,000 sweep (seconds)

The script sweep/spotcheck_20000.py takes no arguments. Its seed is fixed in the code as 20261029, its sample size is 300, and it writes spotcheck_20000.json in the current directory, so run it from inside sweep/.

```bash
cd sweep
python3 spotcheck_20000.py
```

Expected result, regenerating sweep/spotcheck_20000.json: seed 20261029, 300 triples, n from 10001 to 20000, every triple checked by direct gcd computation with all gcds greater than 1, and the field all_gcd_gt_1 set to true. The deposited file records a runtime of 2.52 seconds; your runtime will differ and the runtime field is the only field expected to change.

## (c) Audited in-scope clearance recount (about a minute, plus prerequisites)

From the repository root:

```bash
python3 verification/counts_c2.py
```

Expected result: the script regenerates verification/counts_c2.json, and verification/counts_c2.md reports runtime 66 seconds for the original run. The audited chain in that file, in the order computed, is: baseline from the cap 20,000 sweep classification 1,302,183; the uniform prime gap criterion for i ≥ 132 adds 2,383,028, running total 3,685,211; the crude Kummer criterion adds 17,085, running total 3,702,296; the sharp Kummer criterion in its sweep relative form at cap 20,000 adds 123,949, running total 3,826,245; the per-pair prime gap criterion for i ≤ 131 adds 88,849, running total 3,915,094; the primorial criterion for regime R1 adds 0; the i = 3 (LD3) closure to j ≤ 5000 adds 4,212. Final total: 3,919,306 of 4,249,500 pairs fully cleared, with 330,194 partial pairs remaining at rows 4 ≤ i ≤ 113. The marginals are order dependent; the union is not.

One honest prerequisite. As filed, verification/counts_c2.py reads the two classification files pairpass.json and pairpass_20000.json from the folder named by the BASE_DIR constant at the top of the script, and writes its output under the folder named by the PROOF_DIR constant. Those constants name the original campaign folders. To run this step from this repository alone, first regenerate both classification files in step (d) below, then set BASE_DIR to this repository's sweep folder and PROOF_DIR to this repository's root before running the command above. The deposited verification/counts_c2.json in this repository is the audited output of the original run, and the audit verifier re-ran the script end to end and found the regenerated output identical (see CYCLE2.md section 6).

## (d) Pair classification regeneration (minutes)

These scripts take no arguments. Their caps are constants in the files, and each writes its output next to itself, so run them from inside sweep/.

Cap 20,000 classification (recorded runtime about 485 seconds):

```bash
cd sweep
python3 pairpass_fast20000.py
```

The constants in the file are NSTAR = 20000 and IMAX = 6666. Expected result: the script writes pairpass_20000.json with fields nstar 20000 and imax 6666, 33,330,000 pairs considered, 8,021,170 fully cleared, and 25,308,830 partial. The deposited file's own runtime field is 484.77 seconds, rounded to about 485 seconds in the record. This file is not stored in this repository; this command regenerates it. Its in-scope count for i ≤ 1000, j ≤ 5000 is 1,302,183, matching the prediction recorded in advance in sweep/threshold_prediction_20000.txt, which can itself be rerun with `python3 threshold_prediction_20000.py` from inside sweep/.

Cap 10,000 classification:

```bash
cd sweep
python3 pairpass_fast.py
```

The constants in the file are NSTAR = 10000 and IMAX = 1000. Expected result: the script writes pairpass.json with fields nstar 10000 and imax 1000, 4,249,500 pairs considered in the i ≤ 1000 scope, 768,741 fully cleared, and 3,480,759 partial. This file is not stored in this repository either; this command regenerates it.

The slower reference implementation is sweep/pairpass.py. It computes N(i, j) directly for each pair, and since the Stage 1 review fixes it writes pairpass_reference.json, not pairpass.json. Use it for cross checks on samples, as the fast scripts themselves do, rather than as the production classification route.

## (e) Per-cluster check scripts (varies, one documented exception)

The prover and verifier check scripts are runnable individually with python3 from the repository root, and each prints its check outcomes. Examples:

```bash
python3 proofs/P-F1_checks.py
python3 proofs/P-K1_checks.py
python3 verification/V-F_checks.py
python3 verification/V-K_checks.py
```

The full set is proofs/P-E2_checks.py, proofs/P-F1_checks.py, proofs/P-I1_checks.py, proofs/P-I2_checks.py, proofs/P-J1_checks.py, proofs/P-J2_checks.py, proofs/P-K1_checks.py, proofs/P-K2_checks.py, proofs/P-L1_checks.py, and proofs/P-L2_checks.py, together with the helper scripts proofs/P-B1_count.py and proofs/P-E1_empirical.py; and verification/V-B_checks.py, verification/V-F_checks.py (with its V-F_chunkD.py, V-F_chunkEG.py, and V-F_chunkF.py helpers), verification/V-H_checks.py (with V-H_scan.py and V-H_scan_fast.py), verification/V-I_checks.py, verification/V-J_checks.py, verification/V-K_checks.py, verification/V-L_checks.py, and verification/union_check.py. Some of the enumeration scripts are heavy; read the header of a script before running it if time matters.

One documented exception, stated honestly: proofs/P-L2_checks.py as filed hangs at n in {1, 2}, where its loop runs forever because C(n, 3) = 0 there. This is documented in CYCLE3.md section 8. Do not run it expecting completion. Its numbers were recounted independently by the verifier in verification/V-L.md, and with two minimal small n guards in a temporary copy the script completes and matches the file apart from one member list noted in CYCLE3.md section 8.

## (f) The full sweeps (days, not a quick check)

The sweep script sweep/sweep.py takes its cap as an argument. The production commands, recorded in sweep/PROVENANCE.md, were:

```bash
cd sweep
python3 sweep.py --nstar 10000 --block 100 --workers 2
python3 sweep.py --nstar 20000 --block 100 --workers 2 --ckptdir checkpoints20000
```

The script checkpoints one file per block of 100 values of n, validates every checkpoint it loads, and can be killed and rerun to resume. It writes sweep_summary_10000.json or sweep_summary_20000.json on completion.

Be clear about the cost before starting. Rerunning the sweep to cap 20,000 means rechecking 222,188,892,222 triples. On the original 2 core virtual machine the cap 10,000 sweep took 5,208 seconds of combined elapsed time across a machine restart, and the cap 20,000 sweep ran from its launch on 2026-10-28 to completion on 2026-10-29, with checkpointing throughout (the completing run was resumed manually on 2026-10-29 from 173 validated checkpoints; sweep/PROVENANCE.md estimated the compute in advance at on the order of 12 hours). The summary JSON files and the logs sweep/sweep_10000.log and sweep/sweep_20000.log in sweep/ are the durable record of the completed runs; see sweep/PROVENANCE.md and sweep/RESULTS.md for the full production record. This step is listed for completeness, not as a routine verification step.
