# Cycle 3 Report — Erdős #699, the case i = 3 only

Coordinator's report, written only from verifier-certified files.
Proof documents: `proofs/P-I1.md`, `proofs/P-I2.md`, `proofs/P-J1.md`,
`proofs/P-J2.md`, `proofs/P-L1.md`, `proofs/P-L2.md`, `proofs/P-K1.md`,
`proofs/P-K2.md` (with their check scripts). Verification reports:
`verification/V-I.md`, `verification/V-J.md`, `verification/V-K.md`,
`verification/V-L.md` (with their independent check scripts). Token
ledger: `TOKENS3.md`. Every number below traces to a file a verifier
checked; the coordinator's own spot-checks are reported in §8.

## 1. Headline

**i = 3 is NOT closed. (H3) is NOT proved. Erdős #699 is NOT claimed
solved.** All four verifiers state this explicitly, and the coordinator
concurs. What Cycle 3 did achieve, all verifier-certified:

- **The whole band T ≤ 16 is closed**, where T = R + 2(Q − 1) for
  n = Qj + R, 0 ≤ R < j. Stronger form (Cluster I, V-I certified):
  (LD3) has **no even solution in any of the 64 rows with T ≤ 16, for
  any j**. An i = 3 counterexample must satisfy the reconciled residual
  conditions (RES-3) **and T ≥ 17**.
- **The v₂ condition is completely characterised** (Cluster J, V-J
  certified): {n : v₂(C(n,3)) ≥ v} is exactly five residue classes mod
  2^{v+1} for every v ≥ 2, and in row Q a counterexample forces
  v₂(C(n,3)) ≥ vmin(Q) = ⌊3 log₂ Q⌋ + 1.
- **F1.14's outstanding GAP is settled, and its final sentence is
  FALSE** (Cluster J): the V₃-refined comparison closes the full pair
  (3, j) exactly at j ∈ {6, 10} beyond the known j = 5, and for no
  j ≥ 19 (nor any other j > 5). The full closing set of the comparison
  method at i = 3 is {5, 6, 10}.
- **Both frontiers moved by a factor of ten** (Cluster K, V-K
  certified, COMPUTATION): the per-pair (LD3) frontier is now
  **j ≤ 50,000** (was 5000), and (LD3) has **zero survivors at even
  n ≤ 10⁸** (was 10⁶). Targeted high-v₂ families to n ≤ 10¹² produced
  exactly one CRT candidate, (16, 7), which fails (LD3), and no
  candidate with j > 5000.
- **The higher-digit system (LD3⁺) is exactly understood and does not,
  by itself, shrink the residual** (Cluster L, V-L certified, verdict
  (b) for both provers): Sol(LD3⁺) is exactly the set of
  counterexamples, so (H3⁺) ⇔ (i = 3 closed); (H3) ⇒ (H3⁺), and the
  converse is OPEN. No general shrinkage of the residual class is
  proved, and no residual configuration is exhibited that (LD3⁺)
  excludes beyond (LD3).
- **Coordinator combination** (arithmetic verified by the coordinator,
  §7): the certified finite windows for rows (2, 24), (3, 21), (4, 20)
  lie entirely below n = 10⁸, so Cluster K's frontier closes those
  three rows for counterexamples as well.

Net effect on the residual: an i = 3 counterexample, if one exists,
must now have **n even, n > 10⁸, j ≥ 50,001, v₂(C(n,3)) ≥ 4, T ≥ 17**,
satisfy (RES-3), and lie outside the row closures of §7. The exact
statement is §7. Measured against the success criteria fixed in
advance: the prize (closure) was not achieved; the expected value
(certified frontier extensions, additional even subfamilies closed,
the residual measurably shrunk) was achieved and in part exceeded;
the floor (a sharper, exactly stated residual map) is delivered in §7.

## 2. Starting position (Cycle 2 certified record, unchanged)

From `CYCLE2.md` §2 and `verification/V-F.md`: pairs (3, 5) and (3, 6)
closed for all n; SPLIT-odd closed by two routes via Price's
Proposition 4.1 (no counterexample has n odd); four even (Q, R)
subfamilies closed; the (LD3) frontier certified per-pair to j ≤ 5000
with zero (LD3) survivors for n ≤ 10⁶. Hence at the start of Cycle 3 a
counterexample required n even, j ≥ 5001, n > 10⁶, v₂(C(n,3)) ≥ 4.
Open: the even residual class (F1.11 / F2.14) and Cycle 1's item (H3).
Cycle 3 confirms every element of that starting position it touched;
in particular Cluster J re-derived the v₂ ≥ 4 condition in exact form
and Cluster I's (4, 2) validation reproduced F1.11 exactly (§3).

## 3. Target 1 — the even residual class (Cluster I: P-I1, P-I2; verifier V-I)

**Verdict (V-I): both provers' central claims CERTIFIED; the one
substantive difference between them adjudicated in P-I2's favour.**

- **Residual statement (adopted).** P-I1's Claim I1.1, in the
  reconciled form V-I adopts, is the cycle's residual statement
  (RES-3): the standing necessary conditions on an even i = 3
  counterexample (label bound F1.9 data with full r + s = t tracking,
  (N2) in its exact v₂ form, the parity and size conditions), stated
  per row (Q, R). P-I2's independently derived residual agrees on
  substance; V-I logs one completeness GAP in P-I2's file *as a
  reconciliation* (its conditions are all true, but (N1) is labelled
  without being stated and parity feasibility is not formalised).
  (RES-3) in P-I1's form is the record.
- **T ≥ 17 (PROVED, two independent routes).** No counterexample has
  T = R + 2(Q − 1) ≤ 16. P-I1's route: per-row finiteness plus the
  certified j ≤ 5000 frontier plus finite candidate lists. P-I2's
  route: the same finiteness table plus its elimination lemma. All 88
  candidate disposals across both files (68 in P-I1, 20 in P-I2) were
  independently recomputed by V-I: no survivor, no surviving gap.
- **(LD3)-solution closure of the band (PROVED).** P-I2's elimination
  lemma proves (LD3) has no even solution in any of the 64 rows with
  T ≤ 16, for any j. V-I audited Claims I2.7–I2.14 line by line and
  stress-tested the lemma on 1,282,474 candidate pairs with zero
  failures (the prover's own stress tests covered 1,492,091 assignment
  instances, also zero failures). This is genuine progress on
  (H3)-even, strictly stronger than counterexample closure of the band.
  P-I1's refusal to claim (LD3)-solution closure is a correct statement
  about its own Proposition 4.1 method, not a counter-argument; the
  two files do not contradict each other.
- **Validation.** The (4, 2) row validation reproduced F1.11 exactly by
  both routes: complete candidate list (22, 5), (46, 11), (106, 26),
  with gcd(V₃(n), C(n, j)) = 77, 69, 371 respectively (V₃(n) denotes
  the odd part of C(n, 3)), each candidate failing (LD3).
- **What remains open (correctly labelled by both provers):** (RES-3)
  with T ≥ 17; (H3)even restricted to T ≥ 17.

Two slips in the earlier record's row table, flagged by P-I1 and
confirmed by V-I, neither material: row (3, 4) has T = 8, not 7; row
(5, 2) has T = 10, not 8.

## 4. Targets 5 and 6 — the v₂ condition and the Del Pin comparison (Cluster J: P-J1, P-J2; verifier V-J)

**Verdict (V-J): the cluster is certified; four defects logged, none
load-bearing (§8).**

- **Exact v₂ law (PROVED, both provers independently).**
  v₂(C(n,3)) = s₂(n−3) + 2 − s₂(n) (Legendre/Kummer). For every
  v ≥ 2, {n : v₂(C(n,3)) ≥ v} is exactly the five residue classes
  {0, 1, 2, 2^v, 2^v + 2} modulo 2^{v+1}, of density 5/2^{v+1}. At
  v = 4: classes {0, 1, 2, 16, 18} mod 32; for even n, v₂ ≥ 4 holds
  if and only if 16 | n or 16 | (n − 2). This fully answers Target 5's
  characterisation half. Intersected with the residual conditions it
  yields congruences on j per row (Claim J3.1 and equivalents), but —
  certified negative — **no contradiction and no row closure arises
  from the v₂ congruences alone**: each row's system has solutions
  with j arbitrarily large.
- **Per-row strength (PROVED).** In row Q, a counterexample forces
  v₂(C(n,3)) ≥ vmin(Q) = ⌊3 log₂ Q⌋ + 1 (via ρ(Q, ·) ↓ Q³,
  unattained); vmin(2, 3, 4) = 4, 5, 7.
- **F1.14 settled; its GAP sentence is FALSE (Target 6).** The
  V₃-refined comparison (the Del Pin-spirit test with the 2-part
  removed) closes the full pair (3, j), for all n, exactly at
  j ∈ {6, 10} among j > 5; the table for 5 ≤ j ≤ 18 was recomputed
  entry for entry, and for j ≥ 19 the power-of-two witness
  n = 2^⌈log₂ 2j⌉ blocks the comparison. The auxiliary bound
  2^{v₂(C(n,3))} ≤ n (PROVED by both provers) upgrades the j = 6, 10
  closures to all n ≥ 2j with no EEES78 input. The full closing set of
  the comparison method at i = 3 is therefore exactly {5, 6, 10};
  the single-top comparison closes nothing further (Claim J4.5,
  PROVED as a negative). Target 6 is thereby exhausted: no other
  comparison of this spirit clears further (3, j) pairs.
- **Row closures by the squared bound (COMPUTATION, fully
  re-verified).** P-J1's criteria (A)/(B) close, for counterexamples:
  all Q = 2 rows with even R ≤ 22 (odd R closed globally by
  SPLIT-odd); all Q = 3 rows with R ≤ 20; all Q = 4 rows with even
  R ≤ 18 (odd R globally); Q = 5 rows with R ≤ 16; Q = 6 rows with
  R = 0 and 3 ≤ R ≤ 14; and, by criterion (B)'s remark, h = 0 rows at
  any Q with T ≤ 24 (including some rows at 7 ≤ Q ≤ 11). P-J2's hybrid
  comparison is uniformly sharper than the squared bound in their
  overlap and corroborates these closures, but does not extend them:
  at the boundary rows (2, 22), (3, 19), (3, 20), (4, 18) the hybrid
  bound (22394, 14930, 14930, 11198 respectively) exceeds the old
  frontier while criterion (B) closes the rows. First open rows after
  Cluster J alone: (2, 24), (3, 21), (4, 20), each with an explicit
  finite window (§7).

## 5. Targets 3 and 4 — frontier extensions (Cluster K: P-K1, P-K2; verifier V-K)

**Verdict (V-K): COMPUTATION (verified) on every item; no discrepancy
in any count anywhere.** Both computers' scripts were re-run
end-to-end by the verifier; the mandated ranges were recounted by the
verifier's own independent implementations; the aggregate form of
(LD3) used for the large enumerations (R(n) | j, R(n−1) | j(j−1),
R(n−2) | j(j−1)(j−2)) was proved equivalent to the per-prime-power
form in V-K §5 and validated empirically before use (and independently
by P-K2: exhaustive comparison on 6,974,250 pairs plus a 225,841-pair
sample, zero disagreements). The per-prime-power form is the one
defined in F1.15–F1.17.

- **Per-pair frontier (Target 3): j ≤ 50,000.** (LD3) has no solution
  with 2j ≤ n ≤ N(3, j) for every 5 ≤ j ≤ 50,000; hence, by the
  standing finite reduction (Corollary F2.19; the sole i = 3 EEES78
  exception pair (8, 3) admits no j ≥ 5), **every pair (3, j) with
  5 ≤ j ≤ 50,000 is closed for all n** — a factor of ten beyond Cycle
  2. Counts: 5,653,872 (n, j) pairs clause-tested in total across the
  range; the verifier recounted 1,536,591 pairs in full on
  5001 ≤ j ≤ 20000 plus one full block beyond it, the remaining blocks
  being covered by the two independent implementations, both re-run.
  (Method note, certified: the direct per-pair method's honest reach
  ends here; the per-pair cost grows like N(3, j) ~ j³, and the
  binding constraint was enumeration size, not any mathematical
  obstruction.)
- **Survivor search (Target 4): even n ≤ 10⁸, zero survivors.** In the
  window 3 < j ≤ n/2, 922,011,091 candidate pairs were tested with
  zero (LD3) survivors (922,010,906 in the j ≥ 7 convention; the
  difference is exactly the 185 pairs with j ∈ {4, 5, 6}, 133 of them
  at n ≤ 10⁶; both conventions recounted). The verifier recounted in
  full to 10⁷ under both conventions, plus a segmented recount of
  (10⁷, 2×10⁷], plus the exact convention reconciliation to 10⁸.
- **Targeted high-v₂ families to 10¹².** All 14,055 targeted values of
  n (n near powers of two and the families the provers identified,
  where v₂(C(n,3)) is large) were tested with (LD3) + (N2): exactly
  one CRT-pinned candidate, (n, j) = (16, 7), which **fails (LD3) at
  r = 1, q = 5**; **zero candidates with j > 5000**.
- P-K2 discloses one wrong preliminary pair count in its §4.3, caught
  by an independent recount before the final run and superseded by the
  correct value; V-K confirms the correction. No other discrepancy.

Intersecting with the certified record: an i = 3 counterexample must
now have **n even, n > 10⁸, j ≥ 50,001, v₂(C(n,3)) ≥ 4**.

## 6. Targets 1 and 2, higher-digit form — (LD3⁺) and the (H3)/(H3⁺) relationship (Cluster L: P-L1, P-L2; verifier V-L)

**Verdict (V-L): verdict (b) is the correct label for BOTH provers;
the cluster is certified.** (LD3⁺) is computationally stronger than
(LD3) instance-by-instance, but **no general shrinkage of the residual
class is proved**, and there is **no residual configuration exhibited
that (LD3⁺) excludes beyond (LD3)**. Three defects in P-L2, none
load-bearing (§8); P-L1 is clean.

- **What (LD3⁺) adds (PROVED).** The digitwise condition on the low
  digits 0..a−1 of the (LD3⁺) system is *exactly* (LD3) (j mod q ≤
  (n−r) mod q digitwise, load-bearing on r < p); all genuinely new
  content is the high-digit tail condition ⌊j/q⌋ ⪯ (n−r)/q digitwise.
  In an instance census at n ≤ 2000 (4,711,997 prime instances, all
  figures independently reproduced by V-L): the low condition fails
  4,182,943 instances; of the 529,054 low-pass instances the tail
  condition decides 303,253, i.e. 57.3% — the tail is the sharper
  filter in practice, without yielding a proved closure.
- **The exact logical position (PROVED).** Sol(LD3⁺), over the full
  system quantifying over exactly the primes p ≥ 3 dividing C(n, 3),
  is *exactly* the set of counterexamples. Hence **(H3⁺) ⇔ (i = 3
  closed)**; **(H3) ⇒ (H3⁺)**; the converse is **OPEN**. Consequence
  for Target 2: the even case now turns precisely on (H3⁺) restricted
  to (RES-3) with T ≥ 17 — a statement about counterexamples
  themselves, not about the possibly larger class of (LD3) solutions.
  (The Cycle 3 coordinator brief's parenthetical suggesting that an
  (LD3⁺) solution "is not a counterexample" was wrong for the full
  system; flagged by V-L and recorded in §8.)
- **The ≥5-only system (COMPUTATION, reproduced exactly).** Dropping
  the p = 3 clauses, the remaining (LD3) system has **exactly 12
  solutions at n ≤ 10⁶** among 26,035,963 pairs tested: (n, j) =
  (3^a + 1, (3^a+1)/2) for a = 2..12, and (162, 70). All 12 are killed
  by the p = 3 low clause; but **8 of the 12 are excluded by the ≥ 5
  higher digits alone**, a channel independent of the 3-low clause.
  No new pair closures result.
- **A labelled necessary condition (PROVED).** P-L1's Lemma L3.1: in
  any h = 0 row, an even-n counterexample satisfies n − 1 | 3Λ₃(T).
  P-L2's per-prime p = 5 strictness family is strictness at one prime
  only and does not conflict with the global strictness question,
  which remains OPEN.

## 7. The exact residual statement for i = 3, as it now stands

An i = 3 counterexample, if one exists, must satisfy **all** of the
following (each item verifier-certified in the file cited):

1. n even; n > 10⁸; j ≥ 50,001; 2j ≤ n. (Cycles 1–2; V-K §8.)
2. v₂(C(n,3)) ≥ 4, in exact form: n mod 32 ∈ {0, 2, 16, 18},
   equivalently 16 | n or 16 | (n − 2). (V-J.)
3. Writing n = Qj + R with 0 ≤ R < j: T := R + 2(Q − 1) ≥ 17, and in
   row Q, v₂(C(n,3)) ≥ vmin(Q) = ⌊3 log₂ Q⌋ + 1. (V-I; V-J.)
4. (RES-3): the reconciled necessary conditions of P-I1 Claim I1.1 —
   the label bound with full r + s = t tracking (which of n, n−1, n−2
   supplies each prime power of C(n, 3), and the corresponding data
   for C(n, j)), in the per-row form stated there. (V-I.)
5. (LD3⁺): equivalently, (n, j) is a solution of the full higher-digit
   system, which by V-L is exactly the counterexample condition at the
   digit level; and in any h = 0 row, n − 1 | 3Λ₃(T). (V-L.)
6. The row (Q, R) is not among the certified closures: T ≤ 16 (all
   rows, V-I); Q = 2 with even R ≤ 22; Q = 3 with R ≤ 20; Q = 4 with
   even R ≤ 18 (odd R at Q ∈ {2, 4} and all odd n are excluded by
   SPLIT-odd); Q = 5 with R ≤ 16; Q = 6 with R = 0 or 3 ≤ R ≤ 14;
   h = 0 rows at any Q with T ≤ 24. (V-J §6.)
7. Rows (2, 24), (3, 21), (4, 20) are also closed — **coordinator
   combination**, not a prover claim: V-J §6 certifies finite windows
   j ∈ [499989, 1280504], [333327, 853670], [249996, 640253]
   respectively, whose largest n values are 2,561,032, 2,561,031,
   2,561,032, all below 10⁸, and V-K certifies (LD3) has no solution
   (hence no counterexample) with even n ≤ 10⁸. The coordinator
   verified this arithmetic directly (§8).

First open rows by the certified criteria are now (5, 17) and (6, 15)
at T = 25, then (3, 22) at T = 26 and (2, 26), (4, 22) at T = 28,
together with all rows at Q ≥ 7 not covered by item 6. One labelling
tension, adjudicated by the coordinator: V-J §6 lists rows (6, 1) and
(6, 2) as OPEN, which is correct at the level of Cluster J's own
criteria (and for (6, 1) the row has n odd throughout, so SPLIT-odd
applies in any case); at the counterexample level both rows have
T = 11 and T = 12 ≤ 16 and are closed by Cluster I. A mechanical
re-tabulation of P-J1's criterion-(B) windows against the new 10⁸
frontier would close further rows beyond item 7; that re-tabulation
has **not** been verifier-certified in this cycle and is not claimed.

## 8. Errors and defects found (all logged by the verifiers; none load-bearing)

- **P-J1, Cor. J1.4(ii):** the conditional proportion of even n with
  v₂ ≥ v is printed as 2^{1−v}; the correct value is 2^{2−v} (P-J2's
  corollary has it right). A gloss only; the absolute densities used
  downstream are correct.
- **P-J1, Claim J3.3(c):** GAP as filed (the case (2, 0), h = 2, is
  omitted); the statement is true with the verifier's repair in V-J
  §4.3. No downstream effect.
- **P-J2, Claim J2.7:** its universal sentence is FALSE, refuted at
  (4, 2); the embedded computation is PROVED and the claim is not used
  downstream.
- **P-J2, Claim J2.14:** its "still open" list is FALSE at (2, 22),
  (3, 19), (3, 20), (4, 18) (and at the Q = 5, 6 rows closed by
  criterion (B)): the closing combination was already available inside
  P-J2's own inputs and was not drawn. P-J1 is correct at every
  contested row.
- **P-J2, Claim J4.5 (wording):** "strictly weaker than F1.8 for
  j > 3" fails at j = 4, where both bounds equal 37; strict for
  j ≥ 5, which covers the relevant range.
- **P-L2, Prop. L2.9:** the parenthetical mislabels w = 0, which gives
  (30, 15); (80, 40) is w = 1.
- **P-L2, Thm L2.15(iii):** the unqualified "(H3⁺) does not imply
  (H3) / strictly stronger" is overlabelled; the dichotomy inside is
  proved, strictness is OPEN (P-L1's L4.1(c) states it correctly).
- **P-L2's script as filed hangs** in its §F1 (its V3 loop runs forever
  at n ∈ {1, 2}, where C(n, 3) = 0), so its §7 runtime claim is not
  reproducible as filed. With two minimal small-n guards in a temporary
  copy it completes in 6.4 s and matches the file everywhere except
  Method A's member list, which the file understates as {6, 10}
  against the true {3, 4, 5, 6, 10} (conclusion unaffected; no member
  is in-row with j > 3). All §F numbers were independently recounted in
  V-L.md regardless.
- **P-K2, §4.3:** one wrong preliminary pair count, caught by the
  prover's own independent recount before the final run, disclosed in
  the file, and confirmed superseded by V-K.
- **Earlier record:** the row-table T slips (3, 4): T = 8 not 7;
  (5, 2): T = 10 not 8 (§3).
- **Coordinator brief error:** the Cycle 3 brief's parenthetical about
  (LD3⁺) solutions versus counterexamples was wrong for the full
  system (see §6); flagged by V-L, corrected here. The brief's two
  T-value slips above also originated upstream of the provers.

Coordinator's own spot-checks (independent of all twelve runs):
the v₂ class law at v = 4 verified by direct computation for
n ≤ 5000 (zero mismatches, both the mod-32 form and the even-n form);
the (4, 2) gcds recomputed as gcd(C(n,3), C(n,j)) = 154, 276, 742,
whose odd parts are exactly the filed 77, 69, 371; (16, 7) confirmed
not a counterexample (gcd(C(16,3), C(16,7)) = 80, sharing the prime
5 ≥ 3); the three window maxima of §7 item 7 recomputed; the count
arithmetic of §5 (5,312,239 + 341,633 = 5,653,872; 1,536,591 +
341,633 = 1,878,224; 922,011,091 − 922,010,906 = 185) verified.

## 9. What is NOT proved

- i = 3 is not closed for any j ≥ 50,001 or any even n > 10⁸; (H3) and
  (H3⁺) are both OPEN, now localised to (RES-3) with T ≥ 17 outside
  the §7 closures.
- No general theorem excludes (LD3) or (LD3⁺) solutions in the
  residual class; the T ≥ 17 rows are not known to be finite in number
  per row beyond the per-row finiteness of §3, and no uniform bound
  covering all residual rows is proved.
- The converse (H3⁺) ⇒ (H3) is OPEN: the residual class could in
  principle contain (LD3) solutions that are not counterexamples.
- Cluster K's results are verified computations, not proofs; a
  survivor of (LD3), had one appeared, would not have been a
  counterexample ((LD3) is necessary, not sufficient). None appeared.
- Nothing in this cycle touches i ≥ 4, and nothing here, alone or with
  Cycles 1–2, proves Erdős #699. The j = 2i line for i < 1.2×10⁸ and
  the j > 2i region beyond the Cycle 2 certified regions remain open
  independently of i = 3.

## 10. Note for a mathematician receiving this work

What is handed over: a complete, verifier-certified map of the i = 3
case in which everything except an explicitly delimited residual class
is closed, with the residual stated three equivalent ways — (RES-3)
with labels (§7 item 4), the digit system (LD3⁺) (§7 item 5), and the
row picture (§7 items 3, 6, 7). What remains to be supplied is a single
mathematical idea, not more computation: an argument that excludes
(RES-3) configurations with T ≥ 17, or equivalently proves (H3⁺) on
that class. The campaign's evidence about where such an argument must
live: exponent-only (size) arguments provably stall here (Van Doorn &
Rocca's diagnosis, confirmed at every step of this cycle — the squared
and hybrid bounds, the v₂ congruences, and the comparison tests each
close exactly a bounded initial segment and no more); the information
that must be used is the label data, which of n, n−1, n−2 supplies each
prime power. The two most concrete starting points in the record are
(i) the h = 0 divisibility n − 1 | 3Λ₃(T) (Lemma L3.1), which ties the
residual to a fixed finite quantity per row while n grows, and
(ii) the ≥ 5 higher-digit channel of §6, which independently excludes
8 of the 12 near-solutions of the ≥5-only system and has no proved
theory yet. Computation can extend the frontiers further (the method
of §5 reaches j ≤ 50,000 and even n ≤ 10⁸ exactly; each further factor
of ten costs roughly a factor of 10³ in enumeration), but the
verifiers' unanimous assessment, which the coordinator shares, is
that the residual class will not fall to enumeration.

## 11. Crux list for a possible Cycle 4 (not launched)

1. Exploit n − 1 | 3Λ₃(T) (h = 0 rows) and its h = 1 analogues into
   per-row closures for T ≥ 17, starting with (5, 17) and (6, 15).
2. A theory of the ≥ 5 higher-digit channel: prove that the tail
   condition at primes ≥ 5, combined across primes, excludes a
   positive-density or explicitly described part of (RES-3).
3. The mechanical re-tabulation of criterion-(B) windows against
   n ≤ 10⁸ (finite, certifiable, would move the first open rows).
4. Settle the converse (H3⁺) ⇒ (H3), or exhibit a residual (LD3)
   solution that is not a counterexample (which would also be
   informative: it would show (LD3) is the wrong level and (LD3⁺) the
   right one).
