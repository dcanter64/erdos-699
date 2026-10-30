# P-K2: Erdős #699, Cycle 3, Cluster K (computation: frontier extension at i = 3), Computer K2

**Computer:** K2, working independently in Cycle 3 (a second computer, K1, ran the same specification with an independent implementation; K2 did not read K1's files, and exact agreement or disagreement between the implementations is itself evidence). **Code:** `proofs/P-K2_checks.py`, Python standard library only, exact integer arithmetic, single-threaded, runnable end-to-end with no arguments. **Record:** every number in this file is an output of that script; the authoritative run is the single end-to-end run whose final summary block is transcribed verbatim in §7 (total wall time of that run: 686.3 s). During development the sections were also run individually; those preliminary runs are not the record, and one discrepancy they produced is disclosed in §4.3.

**Headline (all COMPUTATION; nothing here is a proof of (H3) or of i = 3).**

1. **K-a.** (LD3) has no solution with $2j \le n \le N(3,j)$ for every $5 \le j \le 50000$. This extends the Cycle 2 certified per-pair frontier ($j \le 5000$, Computation F2.18, recounted by V-F) by a factor of ten, past the mandated $j \le 20000$ to the specification cap of 50000. Pairs clause-tested in total: 5,653,872; survivors: none.
2. **K-b.** Full (LD3) has zero survivors for even $n \le 10^8$: 922,011,091 candidate pairs in the specification window $3 < j \le n/2$ (922,010,906 pairs in F2.21's $j \ge 7$ convention).
3. **K-c.** Over the three targeted high-$v_2$ families (14,055 values of $n$ in total), CRT pinning by (N2) leaves exactly **one** candidate pair across all families, $(n, j) = (16, 7)$, which fails (LD3) at the $r = 1$ clause (relevant $q = 5 \mid n - 1$, and $7 \bmod 5 = 2 > 1$). Survivors of (LD3)+(N2): none.

Combined with the Cycle 2 certified record (CYCLE2.md §2: no $i = 3$ counterexample has $n$ odd; every counterexample has $v_2(C(n,3)) \ge 4$), the computation in this file strengthens the necessary conditions for an $i = 3$ counterexample to: $n$ even, $n > 10^8$, $j \ge 50001$, $v_2(C(n,3)) \ge 4$. These are computational necessary conditions, labelled COMPUTATION; (H3) remains open and $i = 3$ is not proved.

---

## 1. Definitions and method

Definitions are exactly those of the specification. $V_3(n) = C(n,3)/2^{v_2(C(n,3))}$. $R(m)$ is the product of the relevant prime powers $q = p^a \parallel m$ ($p \ge 5$, any $a \ge 1$; $p = 3$ with $a \ge 2$). (LD3): for every $r \in \{0,1,2\}$ and every relevant $q \parallel (n-r)$, $j \bmod q \le r$. (N2): $V_3(n) \mid C(j,3)$. $N(3,j) = \max\{n : C(n,3) < C(2j,6)\}$, computed by exact binary search on binomial coefficients.

Two exact reformulations are used and are proved here; both are also validated computationally against the factorisation form (§2, §4).

**R-formula.** $R(m)$ equals the odd part of $m$, except that a factor $3$ is removed when $v_3(m) = 1$ exactly. Indeed the odd part of $m$ is $\prod_{p \text{ odd}} p^{v_p(m)}$; the relevant prime powers are exactly the $p \ge 5$ parts (all exponents) together with the $3$-part when its exponent is at least $2$, so the odd part already equals $R(m)$ unless $v_3(m) = 1$, in which case it carries one extra factor $3$.

**Aggregate (LD3).** For odd $q$, if $q \mid j(j-1)$ then $q$ divides exactly one of $j, j-1$ (they are coprime); if $q \mid j(j-1)(j-2)$ then $q$ divides exactly one of $j, j-1, j-2$ (at most one of the three is divisible by any odd prime $p$: two of them differ by at most $2 < p$ for $p \ge 5$, and exactly one of the three is divisible by $3$). Since every relevant $q$ is odd, the $r = 1$ clause of (LD3) (each relevant $q \parallel (n-1)$ has $j \bmod q \in \{0,1\}$, i.e. $q \mid j$ or $q \mid j-1$) is equivalent to the single divisibility $R(n-1) \mid j(j-1)$, and the $r = 2$ clause is equivalent to $R(n-2) \mid j(j-1)(j-2)$. The $r = 0$ clause is $R(n) \mid j$.

**Factorisation.** Three exact routines, all with reconstruction assertions (the product of $p^a$ over the returned factorisation is asserted equal to the input, so no cofactor is left unexamined): (i) trial division by sieved primes, used where the bound is small and as the independent cross-check in §5 (sieved primes to 1,100,000); (ii) an SPF table to $10^6$ for the §4 anchor, built by descending prime slice assignment and sanity-checked against trial division on every $m < 2000$; (iii) `factor_fast`: trial division by the primes $\le 100$, then deterministic Miller-Rabin (bases $(2,7,61)$, deterministic below 4,759,123,141; bases $(2,3,5,7,11,13,17)$, deterministic below 341,550,071,728,321; both ranges cover every integer factored here) and deterministic-parameter Brent Pollard-Rho recursion, which classifies every cofactor $> 1$ as prime or splits it, recursively.

**Candidate generation (K-a).** A pair satisfying (LD3) must have $R(n) \mid j$. Every $n$ with $R(n) = d$ is generated exactly once as $n = d \cdot 2^a$ (when $v_3(d) \ne 1$), or as $n = d \cdot 3 \cdot 2^a$ (the case $v_3(n) = 1$, where $v_3(d) = 0$): this is the decomposition of F1.16/F2.18, since the cofactor of $R(n)$ in $n$ is supported on $\{2,3\}$ with $v_3 \le 1$. This implementation bounds both branches by the current $N(3,j)$ block end (see §2.1 for the one count difference this causes against V-F's published code). For each candidate $n$ the script verifies $R(n)$ by exact factorisation of $n$ (asserted equal to the generating $d$ and to the R-formula value), and the clause tests use the relevant prime powers of $n - 1$ and $n - 2$ from exact factorisations of those tops.

---

## 2. Certified anchors, reproduced

### 2.1 Anchor A (per-pair, $5 \le j \le 5000$)

The script's bounded generation gives 47,723 candidate $n$ (all with $R(n) \le 5000$ and $n \le N(3,5000)$), and the clause test gives **341,633 pairs tested with the $n \le N(3,j)$ filter, zero survivors**, matching F2.18/V-F's pair count exactly. The candidate-count difference against V-F's 50,489 is explained completely: V-F's published generation (`V-F_checks.py` §D, `V-F_chunkD.py`) adds the $\times 3$ branch without the $n \le N_{\max}$ bound, so its candidate set also contains values in $(N(3,5000),\, 3\,N(3,5000)]$; the script recomputes V-F's generation as published and obtains 50,489, a difference of exactly 2,766 values, and those values cannot form any pair in range because every pair requires $n \le N(3,j) \le N(3,5000)$. (Formally: the two generations differ only in that one skips adds exceeding $N_{\max}$, and every add is $d \cdot t \le N_{\max}$ or $3 \cdot d \cdot t$ with $d \cdot t \le N_{\max}$, so the difference is confined to $(N_{\max}, 3 N_{\max}]$.) As Anchor A's escape clause requires in the differing-count case, the zero-survivor result is also reproduced by a second, brute-force method with no candidate generation at all: over all $n \in [2j, N(3,j)]$ for $5 \le j \le 60$, 52,625 triples examined, zero survivors (script §S1), the same cross-validation F2.18 reported.

### 2.2 Anchor B (survivor search, even $n \le 10^6$)

By the factorisation form (SPF), even $n \le 10^6$ (499,997 values of $n$ with at least one candidate) gives zero survivors, with pair counts: **6,974,117 pairs under F2.21's convention, and 6,974,250 pairs under the K-b specification window $3 < j \le n/2$**. F2.21's text states its range as $7 \le j \le n/2$, and its count is reproduced exactly under that convention; the specification window adds exactly 133 pairs, those with $j \in \{4,5,6\}$, all of which also fail (LD3). F2.21's sub-count at $n \le 10^5$ is likewise reproduced exactly: 604,976 pairs ($j \ge 7$). On these same 6,974,250 pairs the script asserts pair-by-pair that the aggregate (LD3) form of §1 gives the identical verdict as the factorisation form: 6,974,250 equivalence checks, no disagreement. This is the validation on which §4's use of the aggregate form rests (in addition to the proof in §1).

### 2.3 Anchor C ($N(3,j)$ spot values)

All reproduced exactly: $N(3,7) = 27$, $N(3,100) = 7{,}908$, $N(3,158) = 19{,}926$, $N(3,159) = 20{,}181$, $N(3,500) = 201{,}728$, $N(3,1000) = 808{,}934$; also $N(3,2000) = 3{,}239{,}787$ and $N(3,5000) = 20{,}263{,}871$, matching P-F2 §6 item 4 in full.

---

## 3. K-a: per-pair frontier extension (COMPUTATION)

**Pilot.** Block $j \in [5001, 6000]$: 87,585 pairs clause-tested, 10,542 new candidates entering (cumulative candidates 58,265), zero survivors, wall 1.3 s, with $N(3,6000) = 29{,}182{,}406$.

**Extrapolation rule (stated in the script before any extension block runs).** A 5000-wide block ending at $J$ is projected at $\text{pilot wall} \times (5000/1000) \times (J/5500)$ seconds (per-$j$ cost growing linearly in $j$). Extension proceeds in blocks while every projected block wall is at most 1800 s, up to the cap 50000; the mandated range to 20000 is completed regardless. The pilot projects: to 25000: 29 s; to 30000: 34 s; to 35000: 40 s; to 40000: 46 s; to 45000: 52 s; to 50000: 57 s. Every projection is far below the limit, so the decided extension limit is the cap, 50000.

**Blocks** (pairs clause-tested; survivors zero in every block, so there is no survivor to list; a survivor would not have been a counterexample, (LD3) being necessary and not sufficient, but none occurred):

| $j$ range | pairs tested | new candidates | cumulative candidates | $N(3,j)$ at block end | wall |
|---|---|---|---|---|---|
| 5 to 5000 (anchor) | 341,633 | 47,723 | 47,723 | 20,263,871 | 4.0 s |
| 5001 to 6000 (pilot) | 87,585 | 10,542 | 58,265 | 29,182,406 | 1.3 s |
| 6001 to 10000 | 376,940 | 44,383 | 102,648 | 81,075,754 | 5.7 s |
| 10001 to 15000 | 518,441 | 57,572 | 160,220 | 182,435,650 | 6.7 s |
| 15001 to 20000 | 553,625 | 59,538 | 219,758 | 324,343,560 | 8.9 s |
| 20001 to 25000 | 583,356 | 60,178 | 279,936 | 506,799,482 | 8.0 s |
| 25001 to 30000 | 604,055 | 62,188 | 342,124 | 729,803,419 | 8.6 s |
| 30001 to 35000 | 623,345 | 62,430 | 404,554 | 993,355,368 | 8.7 s |
| 35001 to 40000 | 639,202 | 63,827 | 468,381 | 1,297,455,331 | 10.3 s |
| 40001 to 45000 | 656,122 | 63,379 | 531,760 | 1,642,103,307 | 10.8 s |
| 45001 to 50000 | 669,568 | 64,255 | 596,015 | 2,027,299,296 | 11.1 s |

**Totals.** The mandated range is complete: the blocks through $j = 20000$ sum to 1,878,224 pairs clause-tested, zero survivors, over 219,758 cumulative candidates. At the cap: **5,653,872 pairs clause-tested for $5 \le j \le 50000$, zero survivors.** COMPUTATION: (LD3) has no solution with $2j \le n \le N(3,j)$ for any $5 \le j \le 50000$; consequently, by the same finite-reduction deduction as Corollary F2.19 (the sole $i = 3$ EEES78 exception pair $(8,3)$ admits no $j \ge 5$), the pair $(3, j)$ admits no counterexample for any $n$, for every $5 \le j \le 50000$.

---

## 4. K-b: survivor search extension (COMPUTATION)

### 4.1 Design

The anchor range (even $n \le 10^6$) is computed in the factorisation form by SPF, exactly as specified (script §S3, §2.2 above). The extension uses the aggregate form of §1, which §S3 validates pair-by-pair on all 6,974,250 anchor pairs, and whose counts the script asserts equal to the factorisation-form counts on both anchor decade blocks. Sieve design and memory: the aggregate form needs no sieve at all beyond the anchor's SPF table to $10^6$ (4 MB as `array('i')`, discarded after §S3); $R(m)$ is evaluated by the R-formula in O(1) per integer, so the extension keeps O(1) state beyond counters, far below the 2 GB limit. The r = 0 clause is enforced by enumerating only multiples $j$ of $R(n)$; the pair counts reported are the exact counts of those multiples in the stated window (computed by the enumeration itself, and cross-checked by formula in §4.3).

### 4.2 Decade blocks and the $10^8$ decision

Pairs tested (specification window $j > 3$; the $j \ge 7$ convention of F2.21 in parentheses), survivors zero in every block:

| block | pairs ($j > 3$) | pairs ($j \ge 7$) | wall |
|---|---|---|---|
| $n \le 10^5$ | 605,084 | 604,976 | 0.2 s |
| $10^5 < n \le 10^6$ | 6,369,166 | 6,369,141 | 4.6 s |
| $10^6 < n \le 10^7$ | 75,836,283 | 75,836,256 | 52.0 s |
| $10^7 < n \le 10^8$ | 839,200,558 | 839,200,533 | 505.3 s |

Totals: even $n \le 10^7$: 82,810,533 pairs ($j > 3$), 82,810,373 ($j \ge 7$), zero survivors, wall 56.8 s. The specification's extension rule was applied with the decision stated in the script before the $10^8$ block ran: the run to $10^7$ took 56.8 s (at most the ~30 min condition), the design memory is O(1) state (the memory condition), and the $(10^7, 10^8]$ block was projected at 619 s (last decade's wall scaled by the larger of the measured decade pair growth, $\times 11.91$, and the plain $\times 10$ $n$-growth), against the script's 2700 s projection cap. All conditions met, so the extension proceeded; its actual wall was 505.3 s.

**Grand total: (LD3) has zero survivors for even $n \le 10^8$, over 922,011,091 candidate pairs ($j > 3$); 922,010,906 pairs in the $j \ge 7$ convention.** COMPUTATION.

### 4.3 Disclosure: a discarded preliminary figure

A preliminary test run of the §S3+§S4 sections, launched during development on a contended machine and terminated by the developer mid-run, later produced a completion report whose $(10^7, 10^8]$ pair counts (902,986,145 in the $j > 3$ window) disagreed with the clean end-to-end run transcribed here (839,200,558), while agreeing on every earlier block. Because a terminated process's output is not a reliable record, the block's pair counts were recounted by an independent counting-only implementation (differently written odd-part computation, pair counts by formula, no (LD3) tests): it reproduced the $(10^6, 10^7]$ block (75,836,283) and gave exactly 839,200,558 ($j > 3$) and 839,200,533 ($j \ge 7$) for the $(10^7, 10^8]$ block, agreeing with the final run. The figures from the terminated run are used nowhere in this file; only the final clean run of §7 is the record.

---

## 5. K-c: targeted high-$v_2$ families, (LD3)+(N2) (COMPUTATION)

**Factorisation standard.** Every $n$, $n-1$, $n-2$ and $V_3(n)$ is factorised exactly by `factor_fast` (§1): trial division by the primes $\le 100$, then deterministic Miller-Rabin and Pollard-Rho with reconstruction assertions, so no cofactor $> 1$ remains unexamined. (For scale: plain trial division by sieved primes to $10^6 = \sqrt{10^{12}}$ would already suffice for $n \le 10^{12}$; the largest top occurring is $2^{40} + 1$ in family (ii), whose square root is below 1,100,000.) As a direct check of that standard, `factor_fast` was cross-validated against full trial division by all sieved primes to 1,100,000 on 57 K-c top values (a deterministic subset spanning all three families), with exact agreement on all 57. $V_3(n)$ is additionally asserted equal to the odd part of $C(n,3)$ computed directly, for every $n$ processed.

**Pinning.** For each prime power $p^e \parallel V_3(n)$ with $p \ge 5$, $V_3(n) \mid C(j,3)$ and the pairwise coprimality of $j, j-1, j-2$ at $p$ force $j \equiv 0, 1$ or $2 \pmod{p^e}$; for $p = 3$ with $e_3 = v_3(V_3(n)) \ge 1$, $v_3(j(j-1)(j-2)) \ge e_3 + 1$ forces $j \equiv 0, 1$ or $2 \pmod{3^{e_3+1}}$ (when $e_3 = 0$ the $3$-condition is vacuous: exactly one of $j, j-1, j-2$ is divisible by $3$, giving $v_3 \ge 1$ for every $j$, so no $3$-pin is applied). Prime powers dividing $n$ itself are not free: $R(n) \mid j$ forces the residue $0$ at those prime powers (including the $3$-pin when $v_3(n) \ge 2$), and the script asserts every enumerated candidate satisfies $R(n) \mid j$ and $V_3(n) \mid C(j,3)$ before testing (LD3). Since $R(n)$ divides the pinning modulus, intersecting with the progression $R(n) \mid j$ is then automatic. The raw combination count for a single $n$ never exceeded the $10^6$ switch threshold (maximum 531,441), so the (LD3)-first fallback over multiples of $R(n)$ in the (N2)-size window was triggered for 0 values of $n$ and is implemented but unused.

**Results per family** (candidates after pinning; the split is by $j \le 5000$, already closed for all $n$ by §3 and Cycle 2, versus $j > 5000$, which is the new information):

| family | $n$ values | CRT combinations | candidates | $j \le 5000$ | $j > 5000$ | survivors |
|---|---|---|---|---|---|---|
| (i) $n = m \cdot 2^a$, $m$ odd $\le 999$, $a \ge 4$, $n \le 10^{12}$ (includes $n = 2^a$) | 13,931 | 12,714,813 | 1 | 1 | 0 | 0 |
| (ii) $n = 2^a + 2$ and $2^a - 2$, $3 \le a \le 40$ | 76 | 213,468 | 0 | 0 | 0 | 0 |
| (iii) $n = 3^b + 1$ and $3^b - 1$, $2 \le b \le 25$ | 48 | 19,332 | 0 | 0 | 0 | 0 |

The single candidate after pinning in all three families is $(n, j) = (16, 7)$ in family (i): it satisfies (N2) (it is the F1.14 sharpness pair, $V_3(16) = 35 = C(7,3)$) but fails (LD3) at $r = 1$ via the relevant prime power $q = 5 \parallel 15 = n - 1$, since $7 \bmod 5 = 2 > 1$. There are no candidates at all with $j > 5000$, and **no survivors of (LD3)+(N2) in any family**. COMPUTATION.

**Overlap validation.** The distinct family members with $n \le 10^6$ number 4,029 (every family member is even, so all lie in the §4 range); each was rechecked directly over *all* multiples of $R(n)$, factorisation form, not just pin candidates: 4,088,173 pairs, zero survivors, agreeing with §4's zero survivors on that range and in particular with the anchor (B) recount.

---

## 6. What this file does and does not establish

Established, all as COMPUTATION in `P-K2_checks.py`: (a) (LD3) has no solution with $2j \le n \le N(3,j)$ for any $5 \le j \le 50000$ (§3); (b) (LD3) has no solution with $n$ even and $n \le 10^8$ at all (§4); (c) no member of the §5 families satisfies (LD3)+(N2), and pinning leaves only $(16,7)$, which fails (LD3). Not established: any proof. (H3) is not proved, $i = 3$ is not proved, and Erdős #699 is not claimed solved. An (LD3) solution, had one appeared, would not have been a counterexample to #699, since (LD3) is necessary and not sufficient; none appeared in any part of Cluster K.

---

## 7. Final summary block of the authoritative run, transcribed verbatim

```
S0 N(3,j) spot values: N(3,7)=27, N(3,100)=7908, N(3,158)=19926, N(3,159)=20181, N(3,500)=201728, N(3,1000)=808934; also N(3,2000)=3239787, N(3,5000)=20263871
S1 brute force 5<=j<=60: 52625 triples examined, 0 survivors
S2 anchor A (5<=j<=5000): 341633 pairs clause-tested (n<=N(3,j) filter), 0 survivors; candidate n: 47723 by the bounded generation used here, 50489 under V-F's published generation (difference 2766, all in (N(3,5000), 3*N(3,5000)], forming no pair in range); zero survivors also by S1 brute force
S2 pilot block 5001-6000: 87585 pairs clause-tested, 0 survivors, wall 1.3s, cumulative candidates 58265
S2 extrapolation from pilot: projected block walls (s) to 25000: 29, to 30000: 34, to 35000: 40, to 40000: 46, to 45000: 52, to 50000: 57; decided limit 50000
S2 block 6001-10000: 376940 pairs clause-tested, survivors 0, wall 5.7s, N(3,10000)=81075754, cumulative candidates 102648
S2 block 10001-15000: 518441 pairs clause-tested, survivors 0, wall 6.7s, N(3,15000)=182435650, cumulative candidates 160220
S2 block 15001-20000: 553625 pairs clause-tested, survivors 0, wall 8.9s, N(3,20000)=324343560, cumulative candidates 219758
S2 block 20001-25000: 583356 pairs clause-tested, survivors 0, wall 8.0s, N(3,25000)=506799482, cumulative candidates 279936
S2 block 25001-30000: 604055 pairs clause-tested, survivors 0, wall 8.6s, N(3,30000)=729803419, cumulative candidates 342124
S2 block 30001-35000: 623345 pairs clause-tested, survivors 0, wall 8.7s, N(3,35000)=993355368, cumulative candidates 404554
S2 block 35001-40000: 639202 pairs clause-tested, survivors 0, wall 10.3s, N(3,40000)=1297455331, cumulative candidates 468381
S2 block 40001-45000: 656122 pairs clause-tested, survivors 0, wall 10.8s, N(3,45000)=1642103307, cumulative candidates 531760
S2 block 45001-50000: 669568 pairs clause-tested, survivors 0, wall 11.1s, N(3,50000)=2027299296, cumulative candidates 596015
S2 K-a total (5<=j<=50000): 5653872 pairs clause-tested, 0 survivors; (LD3) has no solution with 2j<=n<=N(3,j) for any 5<=j<=50000
S3 anchor B (even n<=10^6, factorisation form): 6974117 pairs with j>=7 (the F2.21 convention), 6974250 pairs with j>3 (the K-b specification window), difference 133 pairs at j in {4,5,6}, 0 survivors either way
S3 block n<=10^5: pairs (j>3) = 605084, pairs (j>=7) = 604976, 0 survivors; block 10^5<n<=10^6: pairs (j>3) = 6369166, pairs (j>=7) = 6369141, 0 survivors
S3 aggregate (LD3) form agrees with the factorisation form on all 6974250 candidate pairs with even n<=10^6
S4 block n<=10^5: pairs (j>3) = 605084, pairs (j>=7) = 604976, 0 survivors, wall 0.2s
S4 block 10^5<n<=10^6: pairs (j>3) = 6369166, pairs (j>=7) = 6369141, 0 survivors, wall 4.6s
S4 block 10^6<n<=10^7: pairs (j>3) = 75836283, pairs (j>=7) = 75836256, 0 survivors, wall 52.0s
S4 K-b total (even n<=10^7): 82810533 pairs (j>3), 82810373 pairs (j>=7), 0 survivors; aggregate counts on n<=10^6 agree exactly with the S3 factorisation-form anchor
S4 10^8 decision: wall to 10^7 = 56.8s, last decade pair growth x11.91, projected (10^7,10^8] wall = 619s, O(1)-state memory design, proceed = True
S4 block 10^7<n<=10^8: pairs (j>3) = 839200558, pairs (j>=7) = 839200533, 0 survivors, wall 505.3s
S4 K-b grand total (even n<=10^8): 922011091 pairs (j>3), 922010906 pairs (j>=7), 0 survivors
S5 family (i) n=m*2^a, m odd <=999, a>=4, n<=10^12: 13931 n values, 1 candidates after pinning (j<=5000: 1, j>5000: 0), 0 survivors of (LD3)+(N2); candidate pairs (n, j, first (LD3) violation (r, q, j mod q)) = [(16, 7, (1, 5, 2))]
S5 family (ii) n=2^a+2 and 2^a-2, 3<=a<=40: 76 n values, 0 candidates after pinning (j<=5000: 0, j>5000: 0), 0 survivors of (LD3)+(N2); candidate pairs (n, j, first (LD3) violation (r, q, j mod q)) = []
S5 family (iii) n=3^b+1 and 3^b-1, 2<=b<=25: 48 n values, 0 candidates after pinning (j<=5000: 0, j>5000: 0), 0 survivors of (LD3)+(N2); candidate pairs (n, j, first (LD3) violation (r, q, j mod q)) = []
S5 CRT pinning: max combinations for a single n = 531441; (LD3)-first fallback triggered for 0 n values: []
S5 factorisation cross-check: factor_fast agrees with full trial division (sieved primes to 1100000) on 57 K-c top values
S5 overlap validation: 4029 distinct family members with n<=10^6, 4088173 pairs rechecked directly, 0 survivors, agreeing with S3/S4
TOTAL WALL TIME OF THIS RUN: 686.3s
```

(Section references in the summary lines are to the sections of `P-K2_checks.py`: S0 = anchor C, S1 = brute force, S2 = K-a, S3 = K-b anchor, S4 = K-b extension, S5 = K-c.)
