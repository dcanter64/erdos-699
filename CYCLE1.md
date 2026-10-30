# Erdős #699 Proof Campaign — Cycle 1 Report

**Date:** 2026-10-28. **Workspace:** `~/workspace/math-hunt/erdos-699-proof/`.
**Problem:** for $1 \le i < j \le n/2$, $C(n,i)$ and $C(n,j)$ always share a
prime factor $\ge i$.

Cycle 1 ran two workstreams. Workstream A refereed the claimed closure of the
region $j \le 3i/2$ (full report: `REFEREE.md`). Workstream B attacked the open
region $j > 3i/2$ with a strategy round (10 independent strategies), a prover
round (top 4 clusters, 2 independent provers each), and a verifier round (one
independent verifier per cluster, every numbered lemma classified). All
computation was Python standard library only, bounded, and run alongside the
cap-20,000 sweep without disturbing it.

**Headline.** No full proof of the general case, and no counterexample. The
closed region $j \le 3i/2$ survives line-by-line refereeing (Workstream A:
sound modulo one named gap, closed externally by computation). Workstream B
produced several new unconditional closures and two large verified clearance
theorems inside the sweep scope; the remaining partially covered pairs in
scope are now confined to $i \le 131$.

---

## 1. Workstream A in one paragraph (see REFEREE.md for the full record)

Two independent referees plus coordinator checks reconstructed Bloom's
exposition of the GPT 5.6 Sol proof claim end to end and found **no error** in
the deduction for $j \le 3i/2$, conditional on EEES78. One material gap:
Bloom's exposition never names or discharges EEES78's 12 exception pairs, and
at an exception pair the input inequality fails in the opposite direction
(exhibit $(n,i,j) = (8,3,4)$: $v = 7$, $v^2 = 49 < 56$). The gap is closed
externally: all 41 exception triples (27 in-region, 14 out; pairs $(9,4)$ and
$(10,5)$ vacuous) were verified directly, four independent times, all gcds
$> 1$. The page's additional assertion covering $n = 2j$ is **unverifiable**
from the available texts and the exposited method provably cannot prove it in
the case $j > 3i/2$ (obstruction: $C(2j, 2(j-i)) > C(2j, i)$ for all
$j > 3i/2$; smallest witness $C(4,1) = 4 < C(4,2) = 6$); it is computationally
true in tested ranges and immaterial to RESULTS.md, since the sweep checks
$n = 2j$ directly. The raw proof-claim texts themselves remain inaccessible
(HTTP 403), which is recorded as a finding in `texts/ACQUISITION.md`.

## 2. Strategy round: 10 strategies and their fates

| # | Route | Fate |
|---|---|---|
| S1 | Kummer small-part bound: $p^{v_p(C(n,i))} \le n$ per prime (Legendre), so the "bad part" $u \le n^{\pi(i-1)}$ | **Selected (Cluster B). Proved; large payoff (§4). Barrier theorem: this route cannot pass $c^* = 1.3672\ldots$** |
| S2 | Amplification of the EEES comparison (how much stronger than $v^2 \ge C(n,i)$ would be needed) | Not selected; produced the quantitative spec `need(c)`: a strengthened EEES $v^2 \ge C(n,i)^{1+\varepsilon}$ needs $\varepsilon > 0.0072$ at $c = 1.51$, $0.065$ at $1.6$, $0.142$ at $1.75$, $0.233$ at $2$ |
| S3 | Prime gaps: a counterexample forces $(n-i, n]$ prime-free, i.e. a straddling prime gap $\ge i+1$; contradict explicit gap bounds | **Selected (Cluster C). Proved; largest payoff (§4)** |
| S4 | Kummer digit classification in the two-digit regime $p^2 > n$: $v_p = 1[s > r]$ | **Selected (Cluster D). Classification and wedge theorem proved (§4)** |
| S5 | Boundary family $j = \lfloor 3i/2 \rfloor + 1$ via the square comparison | **Selected (Cluster A, with S6/S8). Family closed for all $i$, all $n$ (§4). Its proviso about exception triples was FALSE (see §6)** |
| S6 | Small $i$ directly: for $i \le 2$, $V_i(n) = C(n,i)$, so the key lemma applies to the whole coefficient | **Selected (Cluster A). $i = 1$ and $i = 2$ closed for all $j$, $n$ (§4)** |
| S7 | Strengthened EEES78 via smooth-part estimates (exponent $\theta_u$) | Not selected for proving; strongest Cycle 2 candidate (§8, crux 1). Empirics: $\sup \theta_u$ decays to $\lesssim 0.30$ on frontier bands; largest non-exception value $0.49472$ at $(32,13)$ |
| S8 | $i = 3$ via low-digit (Kummer) analysis | **Selected (Cluster A). $i = 3$ reduced to an explicit digit system (LD3) plus side conditions; not closed (§4)** |
| S9 | Largest-prime-factor lower bounds | Not selected; breaking example $(n, i) = (1716, 2)$: $C(1716,2) = 2\cdot3\cdot5\cdot7^3\cdot11\cdot13$ has $P^+ = 13$ while $j$ ranges to 858 |
| S10 | Ratio/window reformulation, EEES-free, in regime R1 ($3i/2 < j < 2i$) | Not selected; reformulation is complete, but simultaneous bad configurations exist (e.g. $(119, 39, 59)$ has 5 bad primes in its interval), so the route needs a counting bound it does not yet have |

## 3. Prover round: what was proved

Eight proof documents: `proofs/P-A1.md`, `P-A2.md`, `P-B1.md` (+ count code),
`P-B2.md`, `P-C1.md`, `P-C2.md`, `P-D1.md`, `P-D2.md`. The two independent
provers in each cluster agreed on every headline statement and number.

### Cluster A (S6 + S8 + S5): small $i$ and the boundary family

- **T1, T2 PROVED unconditionally:** the conjecture holds for $i = 1$ and
  $i = 2$, for all $j$ and all $n$.
- **T3 PROVED unconditionally:** the boundary family $j = \lfloor 3i/2\rfloor + 1$
  is closed for **all** $i$ and all $n$, via the square reduction
  $C(n,i) < C(j, j-i)^2$ (strictly stronger than the bound Phase 0 stated),
  exact step-ratio identities, and finite dispositions of $(4,7)$, $(6,10)$,
  $(8,13)$ where the square test fails (closed via the Phase 0 bounds
  $N = 17, 23, 29$ plus direct gcd checks). The family's two EEES78 exception
  triples are discharged: $\gcd(V_7(30), C(30,11)) = 377$ and
  $\gcd(V_{13}(56), C(56,20)) = 57293 = 23\cdot47\cdot53$.
- **T4 (the $i = 3$ status, stated and proved exactly as a reduction):**
  $j = 4$ is in the closed region; $(3,5)$ and $(3,6)$ are closed; per-pair
  closures reach $j \le 465$; the general case is reduced to the low-digit
  system (LD3) having no solutions, plus conditions (N1), (N2) and odd-top
  rigidity. The unresolved core is the splitting configurations (SPLIT-odd:
  $n$ odd, $v_3(n) = 1$, $j = n/3$; SPLIT-even). (LD3) is necessary, not
  sufficient, and has no solutions for $n \le 5000$ computationally
  (6,235,009 triples checked). **$i = 3$ is NOT closed.**

### Cluster B (S1): Kummer bound and its exact payoff

- Theorem A (EEES-free): $p^{v_p(C(n,i))} \le n$ by Legendre, hence the bad
  part satisfies $u \le n^{\pi(i-1)}$; $F_i$ strictly increasing. All-$n$
  closures of $i = 1$, $i = 2$, $(3,5)$, $(3,6)$ reproved independently.
- **Theorem D (count, confirmed exactly by both provers and by Verifier B's
  third recount): 328,079 newly fully cleared pairs** (318,242 with $i \ge 3$;
  9,837 with $i \in \{1,2\}$), raising the cleared total in scope
  ($i \le 1000$, $2j \le 10000$) from 768,741 to 1,096,820 of 4,249,500 on this
  criterion alone. Spot frontiers: $J_K(100) = 1045$ (vs EEES 656),
  $J_K(1000) = 2541$ (vs 2391). This is the crude-bound count; the sharp
  sawtooth variant was not computed, so 328,079 is a lower bound for the
  sharp payoff of the same idea.
- **Theorem C (barrier, proved):** the route cannot close any
  $c > c^* = 1.3672188\ldots$ for large $i$
  ($\Delta(3/2) = 0.954771 < 1$; $\Delta'(c) < 0$). Consistently, $(3,7)$ is
  provably not closable by size: $\mathrm{Bad}^{\sharp}(3,7) = \{16\}$ with
  equality $u = U^{\sharp} = 16$ at $n = 16$.

### Cluster C (S3): prime-gap criterion and its exact payoff

- Theorem A (table criterion, off-by-ones watertight): $i \ge G(N(i,j))$
  implies the pair $(i,j)$ is fully cleared, where $G$ is the maximal prime
  gap function and $N(i,j)$ the Phase 0 bound. The forcing is exact: a
  counterexample makes $(n-i, n]$ prime-free, a straddling gap $\ge i+1$.
- Theorem B (explicit regions) from Dusart 2010 Prop. 6.8
  ($n - i \ge 396738$, $i \ge (n-i)/(25\log^2(n-i))$) and Axler 2017
  ($n - i \ge 6034256$, $i \ge 0.087(n-i)/\log^3(n-i)$), with Dusart 2018
  Cor. 5.5 ($n - i \ge 468991632$, constant $1/5000$) cited at secondary
  verification level (see §5).
- **Theorem C1 (unconditional family):** all open pairs with $i \ge 1476$ and
  $j \le 7.35\cdot10^8$ are fully cleared ($N < e^2 j^2 \le 3.9918\cdot10^{18}
  < 4\cdot10^{18}$ and $G \le 1476$ there by Oliveira e Silva–Herzog–Pardi
  2014, a published computational theorem taken on trust).
- **Theorem C2 (count, confirmed exactly by both provers and by Verifier C's
  third recount): 2,891,106 newly cleared pairs with $132 \le i \le 1000$.**
  Uniform argument: for $i \ge 132$ and $j \le 5000$,
  $N < e^2\cdot 5000^2/132 = 1{,}399{,}442.44$ and $G(1{,}400{,}000) = 132$
  (first gap record 132 after prime 1357201; next record 148 after 2010733),
  so **every** partially covered pair with $i \ge 132$ is cleared by this
  criterion alone.

### Cluster D (S4): digit classification and the wedge

- Digit classification PROVED by both provers: the master criterion
  $v_p = 1[s > r]$ in the two-digit regime $p^2 > n$; Lemma 1 (every prime
  $p > j$ is good) survived verification in full; counterexample anatomy:
  all prime factors $\ge i$ of $C(n,i)$ lie in $[i, j]$, and the part above
  $\sqrt{n}$ is squarefree and confined to bad configurations.
- **Wedge Theorem S4-C PROVED by both provers:** no counterexample with
  $i > 256$, $256i < n < i^2$, $3i/2 < j < 2i$ (chain
  $C(n,i) \ge (n/i)^i > 256^i = 16^{2i} > 16^j \ge V_i(n)^2 > C(n,i)$, with the
  primorial bound $\prod_{p \le x} p \le 4^x$ proved elementarily; the constant
  256 is exact). A Rosser–Schoenfeld improvement to constant 82 is marked
  UNPROVED and UNUSED in both documents.

## 4. Combined clearance picture (exact, with the union computed)

Scope: $i \le 1000$, $2j \le 10000$; 4,249,500 pairs. Baseline (EEES78 +
sweep): 768,741 fully cleared, 3,480,759 partially covered.

The two clearance theorems overlap (both draw from the same partial pool), so
their counts must not be added naively. The coordinator computed the exact
union (`verification/union_check.py`, reproducing all three validation
targets: S1 total 328,079, $J_K(100) = 1045$, $J_K(1000) = 2541$):

- S3 clears all 2,891,106 partial pairs with $i \ge 132$.
- S1 clears a further **40,889** partial pairs with $i \le 131$ (its remaining
  287,190 newly cleared pairs lie at $i \ge 132$ and are already counted in
  S3's set).
- **Union: 2,931,995 newly cleared pairs; total cleared in scope
  3,700,736 of 4,249,500.**
- **At most 548,764 pairs remain partially covered, all with $i \le 131$**
  (S3's per-pair criterion may clear further individual pairs there, e.g. its
  $(i, 71)$ analysis; no campaign-wide count of those was computed).

Separately, and unconditionally for all $n$ (no sweep): $i = 1$; $i = 2$; the
boundary family $j = \lfloor 3i/2\rfloor + 1$ for all $i$; the S3 family
$i \ge 1476$, $j \le 7.35\cdot10^8$; and the S4 wedge region are closed.

## 5. Verifier round: classifications

Four independent verifiers, 109 numbered items in total.

| Verifier | Documents | Result |
|---|---|---|
| V-A | P-A1, P-A2 (46 items) | 45 PROVED, 1 OPEN, 0 GAP, 0 FALSE. The OPEN item is (H3), flagged unproved by the provers themselves; it is exactly the $i = 3$ obstruction |
| V-B | P-B1, P-B2 (23 items) | 22 PROVED, 1 GAP, 0 FALSE, 0 OPEN. The GAP: Theorem B2.B case (1) repeats S1's wrong target $C(j,0) = 1$; the correct target $C(j, j-1) = j$ with $n \ge 2j > j$ repairs it in one line. Statement true; no other document contains the error |
| V-C | P-C1, P-C2 (19 items) | 19 PROVED (T-B regions and T-C (C1) conditional on published external results, dependencies honestly labelled). 1 FALSE non-load-bearing sub-clause and 1 bibliographic GAP, both in P-C1, detailed below |
| V-D | P-D1, P-D2 (21 items) | 21 PROVED, 0 GAP. The only FALSE item anywhere in the cluster is S4's original bare Lemma 4, which both provers flag and repair; the only OPEN item is the constant-82 improvement, marked unproved and unused by both provers |

Verifier detail worth recording:

- V-A independently recomputed $N(4,7) = 17$, $N(6,10) = 23$, $N(8,13) = 29$ and
  all 12 EEES78 interval gcds; verified T1/T2 directly to $n \le 300$ and T3 for
  $i \le 60$, $n \le 400$ (0 failures); reproduced the (LD3) enumeration to
  $n \le 1000$ (zero solutions).
- V-B's third recount of Theorem D used direct binary search on the exact
  predicate (no floor formula): 328,079 exactly, with 0 mismatches against
  direct $N_K$ computation on 500 seeded random pairs.
- V-C adjudicated the one genuine prover disagreement: S3 and P-C1 claimed
  Axler's B3 is "strongest for $\log n < 435$"; P-C2 claimed the algebra is
  reversed. **P-C2 is correct:** $0.087/\log^3 x \le 1/(5000\log^2 x)$ iff
  $\log x \ge 435$ ($0.087 \cdot 5000 = 435$ exactly), so B3 is strongest only
  for $\log(n-i) > 435$. Not load-bearing: B1, B2, B3 are proved as independent
  regions in both documents. V-C also stress-tested the criterion at its exact
  boundary ($i = 132$: holds by equality at $j = 8195$; first usable failure
  gap at $j = 9961$ produces exactly $148 - 132 = 16$ prime-free $n$, as
  predicted), and upgraded Dusart 2018 Cor. 5.5 to **verified secondary**
  (threshold, constant, and numbering all attested in survey literature;
  primary text still not sighted). The Axler "Thm. 4.1" label remains
  **unverifiable** bibliographically; the statement B3 uses is corroborated.
  Trudgian 2014 is confirmed unused in any theorem (the $2898329$ vs $2898239$
  transcription discrepancy is in the conservative direction).
- V-D verified the master criterion exhaustively ($n \le 1000$, all
  $p^2 > n$: 39,951,373 checks, 0 violations), the corrected $t = 2$
  equivalence exhaustively ($n \le 300$: 8,608,152 checks, 0 violations; the
  bare form had 2,984,660 mismatches), and audited propagation: S4's Lemma 4
  flaw does **not** propagate into S4-A or the wedge.

## 6. Errors found in the strategy papers and briefs

1. **The coordinator's own brief for S3 contained a false observation (c):**
   "a prime in $(n-j, n]$ divides $C(n,i)$" is false. Counterexample
   $(n, i, j, p) = (20, 3, 9, 13)$: $13 \mid C(20,9)$, $13 \nmid C(20,3)$.
   Correct forcing: a counterexample forces $(n-i, n]$ prime-free. Both C
   provers caught and corrected this; it propagates nowhere.
2. **S5's proviso FALSE:** S5 claimed $(56, 13, 20)$ is the only in-family
   EEES78 exception triple for the boundary family. $(30, 7, 11)$ is a second.
   Both were discharged in the proofs; V-A's census of all 12 EEES78 pairs
   confirms exactly two satisfy the family condition.
3. **S4's bare Lemma 4 FALSE in both directions** ("bad iff
   $(n-i)/2 < p \le n-j$"; counterexamples $(12,5,6,5)$ and $(30,9,10,11)$).
   The corrected form (the inequalities together with $i < p \le j$) is proved
   by both provers and exhaustively verified by V-D.
4. **S1 display slip:** Theorem B(1) displays "$C(j,0) = 1$" where the correct
   target is $C(j, j-1) = j$. Harmless in S1 and P-B1; P-B2 inherited it in one
   case of one proof (V-B's GAP above), where it is repairable in one line.

## 7. What is NOT proved (claim discipline)

- The general case $j > 3i/2$ remains open. Nothing in this cycle is a proof
  of Erdős #699.
- $i = 3$ remains open beyond the proved reduction and per-pair closures.
- The clearance counts in §4 are theorems about the finite scope
  $i \le 1000$, $2j \le 10000$ relative to the Phase 0 reduction; they extend
  the *verified* region, they do not prove the conjecture in that scope by
  pure thought (the baseline rests on the sweep), and the S3 C1 family is
  conditional on a published computational theorem taken on trust.
- Workstream A's closure of $j \le 3i/2$ is conditional on EEES78 as a cited
  published theorem; its proof was not re-refereed.

## 8. Cycle 2 crux list (ranked)

1. **S7's Lemma S7(2.0):** prove $\theta_u \le 0.36$ on $\alpha \in [4, 6.4]$
   (strengthened EEES exponent). With it, $j \le 2i$ closes for $i \ge i_0$;
   the empirical side is strong (frontier $\sup \theta_u \lesssim 0.30$), but
   the current proof is an assembled estimate, and the residue $i < i_0$ needs
   a finite check larger than the present sweep.
2. **$i = 3$ via (H3)/(LD3):** settle the splitting configurations (SPLIT-odd:
   $n$ odd, $v_3(n) = 1$, $j = n/3$; SPLIT-even). This is the smallest open
   case of the whole problem and now has an exact finite-looking target.
3. **S4's open flanks:** primes $p \le \sqrt{n}$ (the multi-digit regime),
   regions $j \ge 2i$ and $n \le 256i$ outside the wedge; and primary-source
   verification of the Rosser–Schoenfeld $\theta$-input behind the constant 82.
4. **S10's R1 counting bound:** bound the number of simultaneous bad
   configurations in $3i/2 < j < 2i$; the reformulation is complete and
   EEES-free, and the $(119, 39, 59)$ example shows exactly what must be
   bounded.
5. **Primary-source verification of Dusart 2018 Cor. 5.5** (currently
   verified secondary only) and of the Axler 2017 theorem numbering.
6. **Sharpen the counts:** compute S1's sharp-sawtooth payoff (328,079 is the
   crude lower bound) and S3's per-pair clearances at $i \le 131$, to pin the
   exact number of partial pairs remaining in scope.

## 9. File index

- `REFEREE.md` — Workstream A verdict (companion document).
- `texts/` — Bloom's exposition verbatim, problem-page statement, EEES78
  abstract and exception list, `ACQUISITION.md` (what was obtained, what
  remains inaccessible).
- `referee/` — `referee1.md` (reconstruction), `referee2.md` (adversarial),
  `coordinator_checks.md`.
- `strategies/` — `S1.md`–`S10.md` (+ S7 scripts).
- `proofs/` — `P-A1.md`, `P-A2.md`, `P-B1.md`, `P-B1_count.py`, `P-B2.md`,
  `P-C1.md`, `P-C2.md`, `P-D1.md`, `P-D2.md`.
- `verification/` — `V-A.md`, `V-B.md` (+ `V-B_checks.py`), `V-C.md`,
  `V-D.md`, `union_check.py` (coordinator's union computation, §4).
- `TOKENS.md` — run and token ledger for this cycle.
