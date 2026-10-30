# Provenance — Erdős #699 computation

Created 2026-10-28 as part of the Stage 1 fixes for the adversarial
review (REVIEW.md, finding M3/L8: exact production commands and the
environment were recorded nowhere). The cap-10000 command lines below
are RECONSTRUCTED from the run logs, the summary JSONs, and the code
(argparse defaults and in-file constants), and are marked as such;
every command from the Stage 1 reruns and the Stage 2 extension
onward is recorded contemporaneously.

## Environment

- Python: CPython 3.12.3 (main, Aug 31 2026) [GCC 13.3.0],
  /usr/bin/python3.
- Dependencies: Python standard library ONLY, for every script in
  this folder (argparse, json, math, multiprocessing, os, random,
  sys, time). No third-party packages; nothing to install beyond
  Python 3 itself (math.comb requires Python >= 3.8).
- Machine: Linux x86_64 VM (kernel 7.0.0-39-generic), 2 CPU cores
  (nproc = 2). All runtimes below are on this machine and are
  order-of-magnitude guides only.

## Production runs, cap 10000 (2026-10-28; commands reconstructed)

Working directory for all commands: this folder.

1. Pre-production validation:
   `python3 validate.py`
   Output (stdout, not retained at the time; rerun deposited as
   validate_rerun.txt): "triples compared: 568820, mismatches: 0".
2. Phase 0 gate computations:
   `python3 phase0_item2_test.py`
   Outcomes (A)-(G) as recorded in PHASE0.md; rerun deposited as
   phase0_test_rerun.txt.
3. Sweep, run 1:
   `python3 sweep.py --nstar 10000 --block 100 --workers 2`
   (--nlo defaults to 2; --ckptdir did not exist yet and defaults to
   checkpoints/). Completed blocks 1-62 (n <= 6201) in 1,197 s of its
   own elapsed time, then was interrupted by a VM restart.
4. Sweep, run 2 (resume): the identical command. The loader found 62
   checkpoints on disk, computed only the remaining 38 blocks in
   4,011 s, no block recomputed. Combined elapsed 5,208 s (sum of the
   two runs' internal elapsed times, excluding the restart interval;
   see the RESULTS.md addendum). Both segments' stdout is
   concatenated, without a separator, in sweep_10000.log; the second
   segment begins at log line 64 ("already done 62"). Final
   artifacts: checkpoints/ (100 block files) and
   sweep_summary_10000.json {"nstar": 10000, "triples":
   27769446111, "flagged": [], "confirmed": []}.
5. Pair classification:
   `python3 pairpass_fast.py`
   (scope constants are in-file: NSTAR = 10000, IMAX = 1000).
   Artifacts: pairpass.json (runtime_s field 89.30 s, stamped before
   the JSON dump) and pairpass_fast.log (final line "runtime 97s";
   see the RESULTS.md addendum for the reconciliation).
6. Independent checker:
   `python3 checker.py`
   Artifacts: checker_results.json (runtime_s 64.286) and
   checker.log. Note: the deposited checker.py is the FIXED version;
   the first run was killed after ~17 minutes and only its
   sample-selection loop was changed (author disclosure; no pre-fix
   version preserved — see RESULTS.md and its addendum).

## Stage 1 changes (2026-10-28, per REVIEW.md must-fix list)

- counting.py, count_closed_form.py deposited; outputs in
  count_closed_form_10000.txt (27,769,446,111 — confirms the
  RESULTS.md cross-check sentence) and count_closed_form_20000.txt
  (222,188,892,222). [H2]
- validate_rerun.txt, phase0_test_rerun.txt deposited; both reruns
  reproduce the recorded results exactly. [M2]
- This file created; sweep.py docstring fixed (it advertised a
  nonexistent --validate-direct flag; argparse reality is
  --nstar/--block/--workers/--nlo/--ckptdir). [M3]
- pairpass.py now writes pairpass_reference.json instead of
  pairpass.json, with a warning in its docstring and at startup.
  The production pairpass.json (from pairpass_fast.py) can no
  longer be silently overwritten by the reference implementation.
  [M4]
- sweep.py checkpoint loader hardened: read_checkpoint validates
  internal lo/hi against the filename block, the recorded count
  against the closed form (counting.triples_in_range), and the
  flagged list's shape and region membership; any mismatch aborts
  with a FATAL SystemExit. sweep.py gained a --ckptdir option
  (default "checkpoints", the original behaviour) so runs at other
  caps keep separate checkpoint directories. Regression test:
  test_checkpoint_loader.py (plants the review's forged-checkpoint
  probe and variants; all rejected; a genuine checkpoint accepted).
  [H1]
- checker.py N_exact rewritten: exact binary search from n = i, so
  it is correct on the full domain including closed-region pairs
  (previously wrong outside the open region, e.g. (3, 4) returned 7
  for true N = 6). Verified against pairpass.N_of on all 3,160 pairs
  with i < j <= 80 (1,053 of them closed) and 300 random open pairs:
  0 mismatches. Values on open-region pairs, its sole original use,
  are unchanged. [M1]
- RESULTS.md gained a dated addendum (Task 2 selection bias [L1],
  pre-fix-version basis [L2], 97 s vs 89.30 s reconciliation [L3],
  sweep log two-run structure [L4]); stage2_design_notes.md marked
  superseded. [L7]
- Regression gate after all changes (2026-10-28): validate.py and
  phase0_item2_test.py reruns identical to the originals (above);
  checker.py rerun end-to-end in a scratch copy reproduced every
  field of checker_results.json except runtime_s (41 / 18 / 39,982 /
  1,996 / 498 / problems []); the sweep machinery rerun over
  n <= 500 with the production path reproduced the original
  per-block counts for blocks 2-101, 102-201, 202-301, 302-401
  exactly and the closed-form count for block 402-500, total
  3,451,472 = closed form, 0 flagged, and a second invocation
  resumed through the validating loader to the identical total with
  no recomputation.

## Stage 2: cap-20000 extension (launched 2026-10-28)

- Sweep command (contemporaneous):
  `python3 sweep.py --nstar 20000 --block 100 --workers 2 --ckptdir checkpoints20000`
  run detached (nohup), stdout/stderr to sweep_20000.log, in this
  folder. Checkpoints: checkpoints20000/ (200 blocks of 100).
  Summary on completion: sweep_summary_20000.json.
- Exact size (closed form, count_closed_form_20000.txt):
  222,188,892,222 open-region triples. Expected runtime on this
  2-core VM: on the order of 12 hours (cap-10000 took 5,208 s for
  27,769,446,111 triples; the cap-20000 total is 8.00x that).
- Overlap control: blocks of the new run covering n <= 10000 must
  reproduce the original checkpoints' per-block counts exactly; the
  first blocks were verified at launch (see the launch report), and
  the full overlap can be re-verified at any time by comparing
  checkpoints20000/ against checkpoints/ file by file (the hardened
  loader additionally validates every block against the closed form
  on any resume).
- Classification plan (after the sweep completes):
  `python3 pairpass_fast20000.py` (deposited, configured: NSTAR =
  20000, IMAX = 6666 — pairs require (3i)//2 + 1 <= j <= 10000 from
  2j <= 20000, hence i <= 6666 — output pairpass_20000.json).
  Prediction on record for the i <= 1000, j <= 5000 sub-scope,
  computed by the threshold method alone
  (threshold_prediction_20000.py, output in
  threshold_prediction_20000.txt): 1,302,183 fully cleared pairs.
  The completed classification must reproduce that sub-scope number
  exactly.
