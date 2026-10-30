# Adversarial Review — Erdős #699 Stage 2 Computation

Review date: 2026-10-28. Reviewer role: lead adversarial reviewer, tasked
to try to break the result before it is shown to other mathematicians.
Scope: PHASE0.md, RESULTS.md, sweep.py, pairpass_fast.py, pairpass.py,
checker.py, validate.py, phase0_item2_test.py, and the artifacts
sweep_summary_10000.json, pairpass.json, checker_results.json,
checkpoints/, and the run logs.

REVIEW ONLY: no code or data in this folder was modified by the review.
All probes ran on copies under /tmp. Four area reviewers worked in
parallel (sweep internals; pairpass threshold/frontier; checker
independence and EEES78; Phase 0 mathematics and claims), and the lead
reviewer independently verified checkpoint tiling, closed-form counts,
and dense complete-row equivalence at large n.

## Headline verdict

No silent miss was found anywhere in the compute paths, and no claim in
RESULTS.md was found contradicted in substance. The sieve, the
incremental bitmask construction, the primes ≥ i restriction, the
open-region predicate, the threshold classification, the independent
checker, and the Phase 0 reduction all survived direct adversarial
probing, including complete-row equivalence checks at n = 5003, 8192,
9999, and 10000 (every admissible (i, j) for those n, both regions,
zero mismatches against an independent Kummer/Legendre direct
computation).

The weaknesses found are provenance and documentation weaknesses, not
numerical ones: the checkpoint loader authenticates nothing (the actual
run is rescued by exact multi-way agreement of log, checkpoints, and
closed-form total, not by the code), and several RESULTS.md statements
lean on evidence that is not deposited in the folder (most notably the
"independently reproduced by a closed-form count" cross-check, for
which no script, formula, or output exists on disk; the claim is true,
the lead reviewer reproduced it externally, but as deposited evidence
it is unbacked). These must be fixed before the folder is presented as
publication-grade. Details and severity ratings follow.

## Findings by severity

### Critical

None.

### High

**H1. Checkpoint loader trusts file contents blindly (latent integrity
weakness; no evidence it fired in the production run).**
sweep.py:165-172 (design stated at sweep.py:14-15: "a block is done iff
its file exists"). The loader checks only os.path.exists, then adds
d["triples"] and extends the flagged list from d["bad"]. It never
compares d["lo"]/d["hi"] to the filename and never sanity-checks the
count. Probe (copy under /tmp): a planted valid-JSON file named
block_000002_000051.json containing {"lo": 999, "hi": 999, "triples":
999999, "bad": []} was silently accepted, its block skipped, and the
run reported a corrupted total (1,739,077 instead of the correct
742,550 for n ≤ 300) into the summary JSON with no warning.
Symmetrically, a forged checkpoint with a correct count and "bad": []
would silently erase a flagged candidate, which is exactly the
silent-miss direction. For the actual n ≤ 10000 run this risk is
closed externally, not by the code: the lead reviewer and the sweep
reviewer independently verified that all 100 checkpoint files tile
n in [2, 10000] with no gap or overlap, that filename lo/hi equal the
internal lo/hi in every file, that every "bad" list is empty, that
every block's recorded count equals the closed-form count for that
block, that per-block counts in sweep_10000.log match the checkpoint
files for all 100 blocks, and that the counts sum to exactly
27,769,446,111. Recommendation before release: add loader validation
(filename vs internal lo/hi, count vs closed form) or state explicitly
in the release notes that checkpoint trust rests on those external
cross-checks, and deposit the cross-check script (see H2).

**H2. The closed-form cross-check claimed in RESULTS.md has no
artifact in the folder.**
RESULTS.md states the 27,769,446,111 total "was independently
reproduced by a closed-form count of the same index set; the two
counts agree exactly." A full-folder search finds that phrase only in
RESULTS.md itself: no counting script, formula, log, or output is
deposited. The figure itself is not in doubt (the checkpoint sum
supports it, and the lead reviewer and the claims auditor each
reproduced the closed-form count externally and got exactly
27,769,446,111), but a referee is asked to take a named correctness
check on faith. Either deposit the counting script and its output, or
delete/soften the sentence.

### Medium

**M1. checker.py N_exact is wrong outside its domain of use
(contained; no effect on any published claim).**
checker.py's N_exact search assumes C(2j, i) < B (the open-interval
case). When C(2j, i) ≥ B it returns 2j−1 unconditionally, regardless of
the true N. Exhaustive probe (i ≤ 40, j ≤ 80): 380 of 400 closed pairs
wrong, e.g. (i, j) = (3, 4): true N = 6, N_exact returns 7; (7, 8):
9 vs 15; (8, 9): 10 vs 17. Root cause: pairpass.py's N_of has a
downward pinning loop (while comb(n, i) >= B: n -= 1); checker.py has
only a single lo − 1 step. In its sole actual use N_exact is exact:
0/1980 mismatches on open pairs in the same exhaustive test, 0/300
random open pairs, and all 18 sampled Task 2 pairs satisfy the
precondition with brute-force N equal to N_exact. Fix or domain-guard
it before any reuse, so a future closed-region call cannot silently
inherit wrong intervals.

**M2. No retained output for validate.py or for the Phase 0 gate
computations.**
RESULTS.md cites 568,820 validation triples with 0 mismatches, and
PHASE0.md rests its gate on the (A)–(G) run of phase0_item2_test.py,
but neither run's output was saved anywhere in the folder. The claims
auditor reran validate.py from a /tmp copy and reproduced exactly
"triples compared: 568820, mismatches: 0" (about 1.7 s user time, so
the cited 1.9 s runtime is plausible but itself unrecorded). Deposit
both logs.

**M3. Exact production commands are not recorded, and sweep.py's
docstring advertises a flag that does not exist.**
Nowhere is the production command line written down (the parameters
are inferable from the summary JSON and argparse defaults, but
--nstar defaults to 5000, so 10000 must have been passed explicitly;
inference is not documentation). Worse, sweep.py:19's usage text says
--validate-direct, while argparse (sweep.py:143-149) defines only
--nstar/--block/--workers/--nlo; the flag is rejected with
"unrecognized arguments" (verified). A referee following the docstring
fails immediately. Record the exact commands for every script and fix
the docstring.

**M4. pairpass.py overwrites the production artifact.**
Running the listed reference implementation pairpass.py as a main
program writes to the same pairpass.json, in a slightly different
format (no "method" field), silently overwriting the artifact produced
by pairpass_fast.py. Nothing warns of this. (That the deposited JSON
came from the fast version is provable from its "method" field.)
Rename the reference implementation's output or warn in both files.

### Low

**L1. Task 2 sampling has an undisclosed short-interval bias.**
checker.py Task 2 admits pairs in seeded-shuffle order while their
full intervals fit a 40,000-triple budget (300-examination cap). Among
the 300 examined (an unbiased draw; median interval length 2238), the
18 selected have median length 1734, and the last three admissions
(lengths 684, 56, 9) are pairs that fit the shrinking remainder. The
sample is therefore "the first budget-fitting pairs among 300 shuffled
cleared pairs," not a uniform sample of the 768,741. RESULTS.md
describes the caps and budget accurately but does not note the bias.
Low severity because Task 2 is a spot re-verification, not an
estimator. One further nuance: the first examined pair is admitted
unconditionally whatever its length (not triggered harmfully; its
length was 2615). Add one sentence to RESULTS.md.

**L2. The "only the selection loop was changed" disclosure cannot be
diff-verified.**
No pre-fix checker.py survives anywhere (no git history, no backup),
so the disclosure that the killed first run's fix touched only sample
selection rests on author statement plus an in-code comment. It is
structurally consistent (the caps/budget variables exist only in the
selection block; triple_ok/V_direct/N_exact never reference them), and
a fresh rerun of the fixed checker.py reproduced checker_results.json
in every field except runtime (111.8 s vs 64.3 s on a loaded VM).
State the basis honestly in the release notes.

**L3. Pair classification runtime is recorded inconsistently.**
pairpass_fast.log's final line says 97 s (and RESULTS.md says 97 s
wall), while pairpass.json's own runtime_s field says 89.30 s. The
mechanism is identified: the JSON field is stamped before the 4.2 MB
JSON dump and the log line is printed after. Immaterial, but a referee
will notice; annotate or align.

**L4. sweep_10000.log is two concatenated runs with no separator.**
Confirmed by log forensics: header at line 1 ("already done 0") plus
62 block lines ending at elapsed 1197 s, then header at line 64
("already done 62") plus 38 block lines ending at elapsed 4011 s, with
TOTAL lines only at the end. RESULTS.md's narrative explains the
interruption, so a careful reader can decode it, but the log alone
(no timestamps, no run markers) does not show where run 1 ends. Also,
RESULTS.md calls 5,208 s the "combined wall time"; it is the sum of
the two runs' internal elapsed times, excluding the VM-restart
interval. And "on 2 workers" appears in no log or JSON (it matches
sweep.py's --workers default of 2, but the production command line is
recorded nowhere; see M3).

**L5. Verification-scope vacuities in the Phase 0 tests (not proof
gaps).**
Over the 568,820 triples of phase0_item2_test.py, the strong-form
lemma's test quantity u satisfies: u = v (the derivation's actual
configuration, gcd(v, C(n, j)) = 1) in 0 triples; 1 < u < v in 458,041
triples; u = 1 (assertion vacuous) in 110,779 triples. Test (E)'s
reduction implication never fires in range and N_of is never called in
its branch, so (E) contributes only "no counterexample with n ≤ 240."
The proof of the lemma is configuration-independent, so this does not
touch the mathematics; it limits what the tests themselves evidence.

**L6. Truncated or corrupt checkpoint crashes the loader.**
sweep.py:168: a truncated checkpoint raises an uncaught JSONDecodeError
and the run cannot proceed until a human deletes the file. This is
fail-closed (loud, no silent corruption), and the write path
(write to .tmp then os.replace, sweep.py:182-186) makes it unlikely:
a kill mid-write leaves only an orphan .tmp, which the loader ignores.

**L7. Stale planning document in the folder.**
stage2_design_notes.md describes a different method (per-prime
Legendre checks, Bertrand pre-filter) and a different coverage
currency than the implemented bitmask sweep. It is labeled a draft
and RESULTS.md is accurate on both points, but in a release folder it
invites misreading. Remove it from the release or mark it superseded.
RESULTS.md's Files section also omits it.

**L8. No environment or integrity manifest.**
Positive: every script is pure Python standard library (verified),
so there are no third-party dependencies, but this is stated nowhere.
There is no README, no Python version (only indirect evidence:
__pycache__ implies CPython 3.12), no CPU/OS record, and no checksums
or version reference tying the JSON artifacts to the code versions
that produced them. Runtimes are therefore only order-of-magnitude
checkable.

**L9. Minor code nits (no effect).**
pairpass_fast.py lines 95-96 compute a cross-check value that line 98
overwrites (dead/confusing; the artifact data are computed before, and
the membership test actually used is the correct line-98 form).
sweep.py's direct_verify (sweep.py:120-140) has dead variables and was
never exercised in production (the flagged list was empty); probes
found it functionally correct (exhaustive agreement with a reference
gcd computation on all 20,540 triples with n ≤ 80, and 300 random
triples with n ≤ 300). Several pairpass edge branches (no pairs
cleared, all pairs cleared) are never exercised by this dataset (all
maximal cleared J are interior, 70 to 2391); their correctness rests
on the proof in the next section, not on execution.

## What was verified clean (the anti-silent-miss core)

**Sieve and factorisation (sweep.py:33-41, 59-69).** spf equals the
trial-division smallest prime factor for every x in 2..10000 (0
mismatches); 1,229 primes, largest 9973. Tables.factor reconstructs x
from its (p, a) list for all x in 1..2000.

**Incremental masks (sweep.py:71-89), including the hardest trap.**
Independent Legendre-exponent support cross-check on 61,698 masks
(every n ≤ 400, plus 60 sampled n in 401..1000, all k ≤ n/2): 0
mismatches. The e == a test at line 81 is exactly "old exponent was
0," so bits are set only on the 0-to-positive transition and cleared
only on hitting 0. The dangerous case is common and handled: for
n ≤ 1000 there are 97,545 steps where the same prime appears in both
factor(n−k+1) and factor(k) at the same k, of which 15,711 have old
exponent 0 with equal numerator and denominator exponents (bit set
then cleared within one step); all final masks correct. A missing
exponent key would crash the worker pool loudly, not silently.

**Suffix masks and the ≥ i boundary (sweep.py:48-57).** Exhaustive set
equality suff[i] = {primes ≥ i} for i = 1..501, and at production size:
for p in {2, 3, 5, 9973}, p is in suff[p] and not in suff[p+1]. A
prime exactly equal to i counts; i−1 does not. suff[1] = suff[2] =
full mask; suff[10000] = suff[10001] = 0. No off-by-one.

**Open-region predicate (sweep.py:107, 112).**
start = max(i+1, (3i)//2 + 1) is the least integer j with j > i and
j > 3i/2 for both parities (i even: start = 3i/2 + 1, correct
strictness at the integral boundary; i odd: start = (3i+3)/2).
Verified exhaustively for i = 1..50,000. End-to-end, run_block on
n in [2, 150] returned 91,900 triples and a flagged list identical to
a brute-force gcd scan (both empty). The si == 0 branch
(sweep.py:104-111) is exact, not merely conservative: si = 0 means
V_i(n) = 1, whose gcd with anything is 1, so flagging every j is
mathematically correct; it never triggers for n ≤ 600.

**Checkpoint tiling and the real restart (lead + sweep reviewer,
independently).** All 100 checkpoint files tile [2, 10000] exactly;
filenames match internal lo/hi; every "bad" list is empty; every
block's recorded count equals the closed-form count for that block;
the sum is exactly 27,769,446,111. Log forensics confirm RESULTS.md's
account exactly: run 1 completed 62 blocks (n ≤ 6201) in 1,197 s, the
resumed run completed the remaining 38 in 4,011 s, each block computed
exactly once, per-block log counts matching checkpoint files for all
100 blocks.

**Resume simulation.** On a copy with nstar = 300, block = 50: an
uninterrupted run gives TOTAL 742,550 (equal to the closed form). A
run SIGKILLed after exactly one checkpoint, then resumed, printed
"already done 1," completed the remaining five blocks, and produced
the identical TOTAL 742,550; the pre-kill checkpoint's hash and mtime
were unchanged (not recomputed, not rewritten).

**Boundary behaviour at the cap.** Blocks are built while lo <= nstar
with hi = min(lo + block − 1, nstar) (sweep.py:157-158) and run_block
iterates range(lo, hi + 1). Tiny runs confirm both ends inclusive and
nothing beyond: nstar = 10 gives a single block 2-10 (21 triples);
nstar = 205 gives blocks ending exactly at 205 with total 235,824
equal to the closed form. n = nstar + 1 is never included; n < 2 is
never included.

**Dense complete-row equivalence (the strongest anti-silent-miss
probe).** Bitmask verdicts were compared against a direct computation
(Kummer/Legendre prime-support intersection, implemented independently
of sweep.py) for COMPLETE rows, every admissible (i, j) in both
regions, at four large n:

| n | open pairs | closed pairs | mismatches | direct-coprime triples |
|---|---|---|---|---|
| 5003 | 2,084,167 | 1,042,083 | 0 | 0 |
| 8192 | 5,591,040 | 2,795,520 | 0 | 0 |
| 9999 | 8,328,334 | 4,164,167 | 0 | 0 |
| 10000 | 8,331,667 | 4,165,833 | 0 | 0 |

Any mismatch here would have been a critical finding. There were none,
and the direct side independently found zero coprime triples in these
rows, corroborating the sweep at the top of its range, including
exactly at n = 10000.

**pairpass_fast.py: threshold equivalence and prefix property PROVED,
then differentially tested at the frontier.**
(a) Threshold equivalence: for fixed i ≥ 1 and B > 1, C(n, i) is
strictly increasing and unbounded in n with C(i, i) = 1 < B, so
N(i, j) is well defined and characterised by C(N, i) < B ≤ C(N+1, i).
N(i, j) ≤ 10000 iff C(10001, i) ≥ C(2j, 2(j−i)), by monotonicity; the
≥ (not >) is forced, because the negation of < is ≥, and the equality
case C(10001, i) = C(2j, 2(j−i)) genuinely gives a cleared pair.
Equality C(n, i) = C(2j, 2(j−i)) does occur in general (94 instances
with i < 30, j < 80; infinite family at i = 1, n = j(2j−1)), and it is
handled correctly everywhere because the derivation yields a strict <.
(b) Prefix property: by symmetry C(2j, 2(j−i)) = C(2j, 2i), and the
ratio B_{j+1}/B_j = (2j+2)(2j+1) / ((2j+2−2i)(2j+1−2i)) is a product
of two fractions each exceeding 1 by a margin of 2i > 0, so B_j is
strictly increasing in j for all j ≥ i, uniformly across the j = 2i
crossing where a naive "increasing in the lower index" argument would
break. Computational confirmation: 10,765 ratio/symmetry cases, 0
failures. Hence cleared j form a prefix per i and exact binary search
on the single threshold is valid.
(c) Differential tests against pairpass.py's direct N(i, j): the
frontier sample (for every i in 1..1000, the j values immediately
around the claimed maximal cleared J, both sides; 5,000 pairs) gave 0
mismatches; an independent random sample of 2,500 pairs (separate
seed) gave 0 mismatches; exhaustive direct N for all j at i = 1..25
(124,519 pairs) gave 0 mismatches. N_of's returned values are
self-certifying: its closing exact assertion, plus the pinning loops,
means floating-point search error can affect only performance, never
the returned value.
(d) Independent reproduction of the headline counts by methods other
than the shipped code path: 4,249,500 considered pairs reproduced from
pure sums and from a direct triple-condition count; 768,741 fully
cleared pairs reproduced by an independent threshold implementation
(symmetric form, different search) matching every per-i maximal
cleared J individually for all 1,000 values of i (0 divergences), and
Σ (J_i − ⌊3i/2⌋) = 768,741. Appendix spots J_1 = 70 (verified by hand:
70·139 = 9,730 ≤ 10,001 < 10,011 = 71·141), J_10 = 199, J_100 = 656,
J_1000 = 2391 all match pairpass.json, as do all 1,000 appendix
values.

**checker.py independence and the EEES78 discharge.**
The checker imports only the standard library, shares no code with
sweep.py, and computes V_i(n) by a genuinely different mechanism
(math.comb, then physically dividing out primes < i) versus the
sweep's incremental spf bitmasks and phase0's Legendre exponents. Its
prime list is exact (1,229 primes to 10000), which matters in the
dangerous direction: a missing prime < i would leave that prime in V
and could mask a true counterexample; none is missing. V_direct was
verified against Legendre on all 10,000 pairs with n ≤ 200 (0
mismatches), on 150 random pairs with n ≤ 10000, and on 251 targeted
pairs where i is prime and divides C(n, i): the prime i itself is
always retained (the break fires before any division by p = i), as
the ≥ i convention requires.
The 12-pair exception list was re-derived from the definition
(enumerating all (n, k), k ≤ n/2, n ≤ 400, with V_k(n)² ≤ C(n, k)
under the primes < k vs ≥ k convention): exactly the claimed 12 pairs
and no others. Completeness for all n rests on EEES78's own theorem,
which is the intended conditional input. The wrong-convention control
(primes ≤ k vs > k) yields exactly 19 cases on the same range, the 12
plus 7 more, confirming the convention trap is real and that the
operative list is the 12. The discharge itself was recomputed
pair by pair: per-pair triple counts 1, 0, 0, 1, 3, 2, 8, 3, 2, 5, 1,
15, totalling 41 triples, all with gcd > 1; (9, 4) and (10, 5) are
vacuous exactly as claimed. Sole-prime-i triples do exist (witnesses
(10, 3, 5) with gcd 3 and (28, 5, 14) with gcd 5), so a shared ≥ vs >
boundary error would have been visible, and in any case that error
direction only over-flags (V′ ⊆ V), never hides a counterexample.
Sampling recounts replaying the exact RNG stream (seed 20261028):
Task 3 counted 1,996 of 3,000 draws (1,004 skipped because no
admissible open j exists), Task 4 counted 498 of 500, matching
RESULTS.md. Limits on independence, stated honestly: checker.py
hardcodes the exception list rather than re-deriving it (the review's
own probe supplies that missing independence), and Task 2's population
comes from pairpass.json, mitigated by the checker recomputing N(i, j)
itself for all 18 sampled pairs.

**Phase 0 mathematics.**
Step 1 (identity C(n,i)·C(n−i,j−i) = C(n,j)·C(j,i)): proved, standard
double count, no edge case in range. Step 2 (the divisibility step
v | C(j, j−i)): proved; the cited Euclid's lemma is the generalised
form (d | ab and gcd(d, a) = 1 imply d | b), which is the correct tool
and is sound. Step 3 (v ≤ C(j, j−i), squaring): proved. Step 4
(Vandermonde strictness): proved, and the term counts stated in
PHASE0.md are exactly right (2(j−i)+1 ≥ 3 terms when 2(j−i) ≤ j;
2i+1 ≥ 3 when 2(j−i) > j; the central term k = j−i is always in range,
and every other term is a positive integer, so the sum exceeds
C(j, j−i)² by at least 2); brute-verified for all i < j < 200. Step 5
(N(i, j) well defined; n = 2j endpoint): proved; the strict inequality
puts a counterexample's own n in the defining set, and if
C(2j, i) ≥ C(2j, 2(j−i)) the interval is simply empty, which does not
endanger the implication. The j ≤ 3i/2 corollary is proved including
both boundaries (at j = 3i/2 and at n = 2j the relevant inequalities
become equalities, and the chain still contradicts the strict <).
Item 3's referee characterisation is accurate and complete: PHASE0.md
states precisely what was refereed (Bloom's exposition of the
GPT 5.6 Sol / Price claim, not the raw claim text, which was
inaccessible), flags the conditional structure (EEES78 plus discharge
of its 12 exception pairs) in both Item 3 and the Gate Verdict, and
does not secretly depend on Sylvester–Schur (recorded but unused; EEES78
is strictly stronger here) or on the page's unproved n = 2j assertion
(for j ≤ 3i/2 that case is subsumed by the closure proof; for
j > 3i/2 those triples are the swept intervals' left endpoints and are
checked directly). phase0_item2_test.py's test (B) does test the
genuine strong form of the lemma, applied to the coprime part u of v,
not a weakening (see L5 for its vacuity profile).

## (a) Claims table: every RESULTS.md claim classified

| Claim | Verdict | Basis |
|---|---|---|
| 27,769,446,111 open-region triples with n ≤ 10000 checked, 0 flagged, 0 confirmed | Verified | sweep_summary_10000.json, sweep_10000.log TOTAL line, and the sum of all 100 checkpoint files agree exactly; every block count also equals its closed-form count |
| Total "independently reproduced by a closed-form count; the two counts agree exactly" | Overstated (as deposited evidence) | True (reproduced externally by two reviewers), but no script, formula, or output for the count exists anywhere in the folder (H2) |
| 568,820 validation triples (n ≤ 240, both regions), 0 mismatches | Verified | validate.py's loop bounds force the count; rerun from a /tmp copy reproduced the exact output; no retained log (M2) |
| Validation runtime 1.9 s | Unsupported | Nothing on disk records it; rerun timing (~1.7 s user) makes it plausible only |
| 4,249,500 pairs considered (i ≤ 1000, j > 3i/2, 2j ≤ 10000) | Verified | pairpass.json and pairpass_fast.log; independently reproduced from pure sums and a direct count |
| 768,741 pairs fully cleared for all n | Verified | pairpass.json cleared lists sum to 768,741; threshold equivalence and prefix property proved; frontier differential test (5,000 pairs), random sample (2,500), and exhaustive i ≤ 25 (124,519 pairs) all 0 mismatches; independent threshold implementation reproduced all 1,000 per-i maxima |
| 3,480,759 pairs partially covered | Verified | pairpass.json field; 4,249,500 − 768,741, consistent |
| Boundary verified exactly for every i | Verified | pairpass_fast.py asserts the two-sided inequality per i; run completion implies no assertion fired; independently confirmed at the frontier for all i (see above) |
| 150 seeded cross-check pairs vs direct N(i, j), 0 mismatches | Verified | pairpass_fast.log line; code uses random.Random(20261028), 150 draws |
| Pair classification runtime 97 s | Overstated (minor) | Log says 97 s; pairpass.json's own runtime_s says 89.30 s; mechanism identified (L3) |
| 12 EEES78 exception pairs as listed | Verified | Verbatim from the paper per PHASE0.md Item 4; independently re-derived by enumeration to n ≤ 400 (exactly these 12; wrong-convention control gives exactly 19) |
| 41 exception triples, all gcd > 1; (9, 4) and (10, 5) vacuous | Verified | checker_results.json and checker.log; independently recomputed pair by pair (counts 1, 0, 0, 1, 3, 2, 8, 3, 2, 5, 1, 15) |
| Checker Task 2: 18 pairs, 39,982 triples, all gcd > 1 | Verified | checker_results.json and checker.log; deterministic reproduction of the selection (300 examined, 18 selected, budget 39,982); N recomputed independently for all 18 pairs. Caveat L1 (short-interval bias) is undisclosed |
| Checker Task 3: 1,996 triples; Task 4: 498 triples, all gcd > 1 | Verified | checker_results.json and checker.log; RNG-stream replay reproduces both counts and their skip logic exactly |
| Checker runtime 64 s | Verified | checker_results.json runtime_s 64.286 and checker.log agree; rerun reproduced every other field exactly |
| "Only the selection loop was changed" after the killed first checker run | Unsupported (by artifact) | No pre-fix version exists to diff (L2); structurally consistent and honestly disclosed as narrative |
| Sweep runtimes 1,197 s / 4,011 s / combined about 5,208 s | Verified (wording nit) | Log forensics: run segments end at elapsed 1197 s and 4011 s; 1197 + 4011 = 5208. "Combined wall time" is the sum of internal elapsed times, excluding the restart interval (L4) |
| Sweep ran "on 2 workers" | Unsupported (minor) | In no log or JSON; consistent with the --workers default of 2; production command unrecorded (M3) |
| Appendix maximal cleared J per i (spots J_1 = 70, J_10 = 199, J_100 = 656, J_1000 = 2391) | Verified | All 1,000 appendix values match pairpass.json exactly (full comparison, not only the spots) |
| Seed 20261028 throughout | Verified | Present in checker.py and pairpass_fast.py code |
| N(10, 19) = 55; scope examples from Phase 0 | Verified | Recomputed via pairpass.py's N_of; exact matches (also N(1, 10) = 189, N(10, 100) = 2,385, N(10, 1000) = 260,190) |
| "The problem as a whole is NOT solved"; scope honesty (partial pairs, unclassified pairs) | Verified | The stated scope matches the artifacts; nothing outside it is claimed |
| Closed region j ≤ 3i/2 settled for all n via refereed proof plus exception discharge | Verified (conditional, as stated) | Proof re-checked step by step in this review; conditionality on EEES78 and on Bloom's exposition (not the raw AI claim text) is accurately declared in PHASE0.md |

No claim was found contradicted in substance. The only
artifact-vs-artifact contradiction is the 97 s vs 89.3 s pairpass
runtime (L3).

## (b) Sentinel and boundary cases exercised, with outcomes

- Prime exactly equal to i vs i−1 (suffix masks, production size):
  p in suff[p], p not in suff[p+1], for p in {2, 3, 5, 9973}; exhaustive
  for i ≤ 501. Outcome: correct, no off-by-one.
- Sole-prime-i witnesses (10, 3, 5) with gcd 3 and (28, 5, 14) with
  gcd 5, where the only shared prime ≥ i is p = i itself. Outcome:
  both the sweep convention and the checker's V_direct treat these
  correctly; a > i convention would false-flag them, and that error
  direction can only over-flag, never hide a counterexample.
- V_direct retention of i^e: 251 targeted pairs (n ≤ 200, i prime,
  i | C(n, i)) all match Legendre and retain the full i-part.
- Same-prime numerator/denominator collision in mask construction:
  97,545 such steps for n ≤ 1000, 15,711 with the bit set then cleared
  within one step. Outcome: all final masks match Legendre supports.
- Open-region boundary strictness: j = 3i/2 exactly (i even) excluded
  from the open region, j = 3i/2 + 1 included; predicate verified for
  i = 1..50,000. Closed-region boundary j = 3i/2 and endpoint n = 2j
  in the Phase 0 corollary: both become equalities in the chain and
  still contradict the strict <. Outcome: correct on both sides.
- Threshold equality case: C(n, i) = C(2j, 2(j−i)) occurs (94 instances
  with i < 30, j < 80; family i = 1, n = j(2j−1), e.g. (6, 1, 2) with
  6 = C(4, 2)); N(1, 10) = 189 = 10·19 − 1 confirms equality-n is
  excluded from N and that pairpass_fast.py's ≥ classification is the
  correct side. Outcome: handled correctly.
- Frontier pairs for every i in 1..1000 (j immediately around the
  claimed maximal cleared J, both sides; 5,000 pairs) vs direct N(i, j):
  0 mismatches. Pairs with N(i, j) exactly 10000 are exercised by this
  sample and classified on the correct (cleared) side.
- Complete rows at n = 9999 and n = 10000 (and 5003, 8192): every
  admissible (i, j), both regions. Outcome: 0 mismatches, 0 direct-
  coprime triples (table above).
- n = nstar + 1 exclusion and final partial block: nstar = 205 run
  ends exactly at 205; n = 10001 is never swept (it appears only as the
  threshold argument C(10001, i) in pair classification). Outcome:
  correct.
- EEES78 vacuous pairs (9, 4) and (10, 5), where i0 = ⌊n0/2⌋ leaves no
  admissible j: correctly counted as discharged with 0 triples.
- Wrong-convention control: primes ≤ k vs > k enumeration to n ≤ 400
  gives exactly 19 cases (the 12 plus (9, 3), (10, 3), (18, 3),
  (28, 5), (54, 7), (82, 3), (162, 3)). Outcome: confirms the operative
  12-list and that the trap was avoided.
- Checkpoint attacks: planted forged checkpoint (wrong lo/hi, inflated
  count, empty bad list) was silently accepted (finding H1); truncated
  checkpoint crashed the loader loudly (L6); SIGKILL-and-resume on a
  small run reproduced the uninterrupted total exactly with the
  surviving checkpoint untouched.
- Checker N_exact outside its domain: (3, 4), (7, 8), (8, 9) return
  7, 15, 17 against true N of 6, 9, 10 (finding M1); inside its domain
  (open pairs) 0 mismatches in 1,980 exhaustive + 300 random + all 18
  Task 2 pairs.
- si == 0 branch (V_i(n) = 1): never triggers for n ≤ 600, consistent
  with the Sylvester–Schur input; its flag-everything behaviour is
  mathematically exact if it ever fires.

## (c) Release-readiness verdict

The mathematics and the computation are release-ready in substance:
the reduction is proved, the threshold classification is proved and
frontier-tested, the sweep's verdicts agree with independent direct
computation on complete rows at the top of the range, the exception
discharge was independently re-derived, and every headline number
traces to an artifact and survives recomputation. No re-run of the
sweep, the classification, or the checker is needed.

Before this folder is shown to mathematicians as a publication-grade
release, fix the following (all are deposit/documentation fixes, none
requires recomputation):

1. Deposit the closed-form counting script and its output, or remove
   the "independently reproduced by a closed-form count" sentence
   from RESULTS.md (H2).
2. Deposit the retained outputs of validate.py and
   phase0_item2_test.py (M2).
3. Record the exact production command lines and the environment
   (Python 3.12, standard library only, OS/CPU, 2 workers), and fix
   sweep.py's docstring, which advertises a nonexistent
   --validate-direct flag (M3, L8).
4. Defuse the pairpass.py overwrite of pairpass.json (separate output
   name or an explicit warning) (M4).
5. Either add checkpoint validation to sweep.py's loader (filename vs
   internal lo/hi, per-block count vs closed form) or state in the
   release notes that checkpoint trust rests on the external
   cross-checks itemised in H1, and deposit those checks (H1).
6. Fix or domain-guard checker.py's N_exact so it cannot be reused on
   closed pairs (M1), and add the two honest sentences to RESULTS.md:
   Task 2's sample is budget-fit-selected and biased toward shorter
   intervals (L1), and the selection-loop-only fix is by author
   disclosure with no pre-fix version preserved (L2).
7. Housekeeping: align the 97 s / 89.3 s pairpass runtime records
   (L3), mark the two-run structure inside sweep_10000.log or in a
   README (L4), and remove or mark stage2_design_notes.md as
   superseded (L7).

With items 1-4 done, the release would already be defensible; items
5-7 are what a careful referee would ask for next. The one residual
risk that no amount of documentation removes is checkpoint provenance
(H1): it is fully closed for this run by the four-way agreement of
summary JSON, run log, checkpoint files, and closed-form counts, but
the code as shipped would not detect a tampered checkpoint in a future
run.
