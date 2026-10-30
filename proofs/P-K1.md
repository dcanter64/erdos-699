# P-K1: Erdős #699 at $i=3$, Cycle 3, Cluster K — Computer K1

**Role:** Computer K1 in Cycle 3 of the Erdős #699 proof campaign,
Cluster K (computation: frontier extension at $i=3$), running the
specification shared with Computer K2, with an independent
implementation written for this run. **Code:** `proofs/P-K1_checks.py`
(Python standard library only, exact integer arithmetic,
single-threaded), runnable end-to-end; every number in this report is
an output of that script as run by me, and the script's final summary
block is transcribed verbatim in the Appendix. **Status of everything
below: COMPUTATION.** Nothing here is a proof of (H3) or of $i=3$;
(LD3) is a necessary condition for a counterexample, not a sufficient
one, and a computation over a finite range excludes counterexamples
only through the standing finite reduction, exactly as in Corollary
F2.19 of Cycle 2.

**Headline.** All three certified anchors are reproduced exactly
(§2). The per-pair (LD3) frontier is extended from $j \le 5000$ to
$j \le 50000$, with **zero survivors** in $1{,}536{,}591$ clause-tested
candidate pairs on the mandated range $5001 \le j \le 20000$ and zero
survivors in the full extended range to $j = 50000$ (§3). The even-$n$
survivor search is extended past $10^6$, with **zero survivors**
(§4; final limit and totals as printed in the Appendix). The targeted
high-$v_2$ families of §5 produce exactly **one** candidate after CRT
pinning in total across all $14{,}055$ values of $n$ tested — the pair
$(n, j) = (16, 7)$, in family (i) — and it does **not** survive the
full (LD3)+(N2) test, so the families contribute **zero survivors**.
As for the survivor search: the coded extension rule of §4 was
triggered, so the final limit there is $10^8$ rather than $10^7$:
$922{,}010{,}906$ candidate pairs at even $n \le 10^8$ were tested in
total, again with **zero survivors**.

## 1. Definitions, conventions, and methods

For $i = 3$: $V_3(n) = C(n,3)/2^{v_2(C(n,3))}$; $R(m)$ is the product
of the relevant prime powers $q = p^a \Vert m$ (relevant: $p \ge 5$,
any $a \ge 1$; or $p = 3$ with $a \ge 2$), so $R(m)$ is always odd.
**(LD3):** $(n, j)$, $3 < j \le n/2$, satisfies (LD3) iff for every
$r \in \{0,1,2\}$ and every relevant $q = p^a \Vert (n-r)$,
$j \bmod q \le r$. **(N2):** $V_3(n) \mid C(j,3)$.
$N(3,j) := \max\{n : C(n,3) < C(2j,6)\}$, computed in the script by
exact binary search on binomial coefficients.

*Counting convention for K-b (read this before comparing counts).*
The assignment describes the K-b candidates as the multiples $j$ of
$R(n)$ in $(3, n/2]$, and simultaneously requires the F2.21 anchor
count at $10^6$ to reproduce **exactly**. Those two are inconsistent
as stated: as V-F's recount makes explicit, the certified count
$6{,}974{,}117$ is the count for $7 \le j \le n/2$ (F2.21's own
stated range), not for $j \ge 4$. I therefore follow the F2.21
convention $7 \le j \le n/2$ throughout K-b, so that every decade
increment is consistent with the anchor; the pairs with
$j \in \{4,5,6\}$ are already closed in the Cycle 2 record. All K-b
counts below use this convention. (In K-c, whose specification has
no pre-existing count to reproduce, I use the range as written,
$3 < j \le n/2$.)

*Candidate generation for the per-pair problem (Anchor A and K-a).*
An (LD3) solution with given $j$ needs $R(n) \mid j$ (that is the
$r = 0$ clause). Every $n$ decomposes uniquely as $n = d \cdot t$
with $d = R(n)$ odd, $v_3(d) \ne 1$, and $t = 2^a$ if $v_3(n) \ne 1$,
$t = 3 \cdot 2^a$ if $v_3(n) = 1$ (in which case $v_3(d) = 0$): any
other prime, and any $3^2$, in $t$ would belong to $R(n)$ by
definition. K-a enumerates, for each $j$, the divisors $d$ of $j$
with $d$ odd and $v_3(d) \ne 1$ and all such $t$ with
$2j \le d t \le N(3,j)$; every generated $n$ is then verified by
exact trial factorisation to satisfy $R(n) = d$ (an assertion in the
script, never tripped), and the $r = 1, 2$ clauses are tested from
the exact factorisations of $n-1$ and $n-2$. The clause test
factorises in ascending prime order and aborts at the first violated
prime power; this is exact, because a single violated clause
disqualifies the pair regardless of the remaining factorisation, and
a pair is reported as a survivor only if the factorisations run to
completion with no violation. "Candidates generated" and "pairs
clause-tested" coincide in K-a by construction: each generated
candidate is generated once (the decomposition is unique) and is
clause-tested exactly once.

*SPF designs for K-b.* To $10^7$: a full smallest-prime-factor array
(`array('i')`, $40{,}000{,}004$ bytes) built by descending slice
assignment. For the $10^8$ extension, if taken (§4): an **odd-only**
SPF array — $50{,}000{,}000$ signed 32-bit entries, $200{,}000{,}000$
bytes ($\approx 0.2$ GB, well under the $\sim 2$ GB design bound) —
in which index $(x-1)/2$ stores the smallest prime factor of the odd
number $x$ (even inputs answer $2$); it is built by assigning, for
each odd prime $p \le \sqrt{10^8}$ in descending order, the value $p$
to the indices of the odd multiples of $p$, so the smallest prime
writes last. Any cofactor arising during factorisation is itself
$\le 10^8$ and is looked up the same way, so the design needs no
segmentation. Before any $n > 10^7$ is processed with it, its pair
count on the interval $(900000, 1000000]$ is checked against the
full SPF's count on the same interval (§4).

*CRT pinning for K-c.* For a prime power $p^e \Vert V_3(n)$ with
$p \ge 5$: $p \nmid 6$, so $V_3(n) \mid C(j,3)$ forces
$p^e \mid j(j-1)(j-2)$; the three factors are pairwise within $2$ of
each other, hence at most one of them is divisible by $p$, hence
that one is divisible by $p^e$, i.e. $j \equiv 0, 1$ or $2
\pmod{p^e}$. For $p = 3$, with $e_3 = v_3(V_3(n)) \ge 1$:
$v_3(C(j,3)) = v_3(j(j-1)(j-2)) - 1 \ge e_3$ forces
$v_3(j(j-1)(j-2)) \ge e_3 + 1$; exactly one of the three factors is
divisible by $3$, so it carries the full $3^{e_3+1}$, i.e.
$j \equiv 0, 1$ or $2 \pmod{3^{e_3+1}}$. (For $e_3 = 0$ the condition
is vacuous and no $3$-item is generated.) The candidate $j$'s are
the integers in $(3, n/2]$ satisfying all these congruences and
$R(n) \mid j$; the last condition is folded into the enumeration by
forcing the residue $0$ for every pinning prime power belonging to
$n$ itself (for $p \ge 5$ that prime power is exactly $p^{a}$ with
$p^a \Vert n$; for $p = 3$ it applies when $v_3(n) = e_3 + 1 \ge 2$,
where the pinning modulus $3^{e_3+1}$ is $R(n)$'s $3$-part). The
enumeration combines prime powers in decreasing size, discards a
partial residue class as soon as it has no member left in the
window, and switches to an explicit candidate list, filtered
congruence by congruence, as soon as the combined modulus exceeds
$n/2$; this is an exact pruning of the full CRT enumeration, not a
heuristic. Every candidate so produced is finally checked by the
exact tests $V_3(n) \mid C(j,3)$ (a direct binomial remainder) and
the full (LD3) clauses from the factorisations of $n, n-1, n-2$.

*Factorisation to $10^{12}$ for K-c.* Trial division by the sieved
primes to $10^{6} = \sqrt{10^{12}}$ is the stated prime bound; the
implemented factoriser trial-divides by the primes to $10^{4}$ and
then classifies any remaining cofactor $x > 1$ exactly: all its
prime factors exceed $10^{4}$ and $10007^3 > 10^{12}$, so $x$ is $1$,
prime, a prime square, or a product of two primes; it is resolved
by a deterministic Miller–Rabin test (bases $2,3,5,7,11$, sufficient
below $2{,}152{,}302{,}898{,}747$, and all inputs here are
$\le 1{,}099{,}511{,}627{,}778$), an exact square test, and Brent's
Pollard rho. No cofactor $> 1$ is left unexamined, and the whole
procedure is cross-checked in the script against full trial
division to $10^{6}$ on $300$ seeded random values in $[2, 10^{12}]$
with $0$ mismatches (§5). The factorisations of $n$ in family (i)
are additionally constrained by the family form $n = m \cdot 2^a$,
but the script does not use that shortcut: it factorises every
$n, n-1, n-2$ by the same routine.

## 2. Certified anchors — all reproduced exactly

**Anchor C ($N(3,j)$ spot values, P-F2 §6 item 4).** The script
reproduces $N(3,7) = 27$, $N(3,100) = 7{,}908$, $N(3,158) = 19{,}926$,
$N(3,159) = 20{,}181$, $N(3,500) = 201{,}728$, $N(3,1000) = 808{,}934$,
and the two values on record elsewhere in the file,
$N(3,2000) = 3{,}239{,}787$ and $N(3,5000) = 20{,}263{,}871$: all
eight match.

**Anchor A (per-pair, $5 \le j \le 5000$; F2.18, V-F recount).**
Generating candidates in the F1/V-F style (odd $d \le 5000$,
$v_3(d) \ne 1$, $t$ a power of two, plus the $d \cdot 3 \cdot t$
candidates when $v_3(d) = 0$) gives $50{,}489$ candidates, exactly
the V-F count, and $341{,}633$ $N$-filtered pairs ($107{,}220$ of
them at $j \le 2000$, matching V-F's subtotal), with **zero
survivors** for every $5 \le j \le 5000$. One counting subtlety is
worth recording because it explains a seeming discrepancy: in the
F1/V-F generation the $d \cdot 3 \cdot t$ candidate is added without
itself being bounded by $N(3,5000)$, so $2{,}766$ of the $50{,}489$
generated candidates lie above $N(3,5000)$. They contribute no
pairs (every $N(3,j)$ for $j \le 5000$ is at most $N(3,5000)$), and
the bounded candidate count is $47{,}723$. In K-a below I use the
bounded generation directly, which is why my K-a candidate counts
are counts of candidates inside the window. Cross-validation of
the zero-survivor result by a second, brute-force method (as the
specification requires when generation designs differ in detail):
for every $5 \le j \le 60$ I tested **all** $n \in [2j, N(3,j)]$ —
$52{,}625$ pairs — by full (LD3) from exact factorisations with no
candidate shortcut, and again found zero survivors, agreeing with
F2.18's stated cross-check.

**Anchor B (survivor search, even $n$; F2.21).** The K-b search of
§4 asserts the anchor before proceeding past it: at $n \le 10^5$
the cumulative pair count is $604{,}976$ (F2.21's first figure) and
at $n \le 10^6$ it is exactly $6{,}974{,}117$ candidate pairs with
**zero survivors**, reproducing F2.21/V-F exactly, in the $j \ge 7$
counting convention explained in §1.

## 3. K-a — per-pair frontier extension

**Pilot.** The pilot block $j \in [5001, 6000]$ generated and
clause-tested $87{,}585$ candidates, with zero survivors, in
$2.07$ s wall time; $N(3,6000) = 29{,}182{,}406$.

**Extrapolation rule (stated and coded before the full run).** The
projected time for a $5000$-wide block is the pilot wall time
multiplied by $5$ (the block-width ratio) and by a safety factor of
$2.0$ for the growth of $N(3,j)$ and of the factorisation cost
across the range. On the pilot figures this projection is
$20.67$ s per block. The rule coded in the script selects the
largest target in $\{50000, 45000, \dots, 20000\}$ whose projected
total remaining time is at most $7200$ s, provided each projected
block is at most $1800$ s ($\sim 30$ min); otherwise it falls back
to the mandated minimum $j \le 20000$. The rule selected the
maximum target: **$j \le 50000$**.

**Results.** Per block (candidates generated = pairs clause-tested;
survivors were zero in every block):

| block of $j$ | candidates / pairs tested | survivors | wall (s) | $N(3, j_{\text{end}})$ |
|---|---|---|---|---|
| 5001–6000 (pilot) | 87,585 | 0 | 2.07 | 29,182,406 |
| 6001–10000 | 376,940 | 0 | 12.37 | 81,075,754 |
| 10001–15000 | 518,441 | 0 | 11.71 | 182,435,650 |
| 15001–20000 | 553,625 | 0 | 14.74 | 324,343,560 |
| 20001–25000 | 583,356 | 0 | 19.17 | 506,799,482 |
| 25001–30000 | 604,055 | 0 | 21.57 | 729,803,419 |
| 30001–35000 | 623,345 | 0 | 24.44 | 993,355,368 |
| 35001–40000 | 639,202 | 0 | 27.47 | 1,297,455,331 |
| 40001–45000 | 656,122 | 0 | 34.66 | 1,642,103,307 |
| 45001–50000 | 669,568 | 0 | 43.33 | 2,027,299,296 |

**Extended range.** On the full range $5001 \le j \le 50000$:
$5{,}312{,}239$ candidates generated and clause-tested, in
$211.52$ s of summed block wall time, with **zero (LD3) survivors**.

**Mandated range.** On $5001 \le j \le 20000$: $1{,}536{,}591$
candidates generated and clause-tested, in $40.88$ s of summed block
wall time (pilot included; the sum is of the unrounded block times),
with **zero (LD3) survivors — there is no (LD3) solution with
$2j \le n \le N(3,j)$ for any $5001 \le j \le 20000$**. Combined
with Anchor A, and with the standing finite reduction exactly as in
Corollary F2.19, the per-pair (LD3) frontier now stands at
$j \le 50000$: every pair $(3, j)$ with $5 \le j \le 50000$ is
closed for all $n$ by this method. This is a computation extending
a finite frontier, not a proof of (H3): whether (LD3) continues to
exclude every $j > 50000$ remains open.

## 4. K-b — survivor search extension (even $n$)

The search enumerates, for each even $n$, the multiples $j$ of
$R(n)$ with $7 \le j \le n/2$ (the counting convention of §1) and
tests the full (LD3) clauses from smallest-prime-factor
factorisations of $n$, $n-1$, $n-2$, with the relevant prime powers
of the two top numbers tested in decreasing order so that most
pairs fail on the strongest clause first. Results by decade
segment (pair counts are increments over the segment; the
cumulative counts at $10^5$ and $10^6$ are the Anchor B assertions
of §2, checked in the script before any larger $n$ is processed):

| even $n$ in | pairs tested (increment) | cumulative pairs | survivors | wall (s) |
|---|---|---|---|---|
| $(0, 10^5]$ | 604,976 | 604,976 | 0 | 1.04 |
| $(10^5, 10^6]$ | 6,369,141 | 6,974,117 | 0 | 7.32 |
| $(10^6, 10^7]$ | 75,836,256 | 82,810,373 | 0 | 90.95 |

So at the mandated limit: **$82{,}810{,}373$ candidate pairs at even
$n \le 10^7$, zero (LD3) survivors.** This extends F2.21's zero-survivor
statement from even $n \le 10^6$ to even $n \le 10^7$.

**Extension decision (coded in the script, applied at this point).**
The rule: project the $(10^7, 10^8]$ decade at the time of the
$(10^6, 10^7]$ segment ($90.95$ s) multiplied by the ratio of the
last two segment times ($90.95 / 7.32 = 12.430$), plus $120$ s for
building the odd-only SPF; proceed iff the projection is at most
$1800$ s ($\sim 30$ min) and the sieve design keeps memory at most
$\sim 2$ GB. The projection was $1250.56$ s and the odd-only SPF
design of §1 uses $200{,}000{,}000$ bytes, so the rule's decision
was to **proceed to $10^8$**. The odd-only SPF was then built
($18.60$ s, $200{,}000{,}000$ bytes in the built array) and
cross-validated before use: on the interval $(900000, 1000000]$ it
reproduces the full SPF's pair count exactly ($692{,}165$ pairs,
zero survivors by both implementations). The full SPF was freed
before the extension blocks ran.

**Extension blocks, $(10^7, 10^8]$:**

| even $n$ in | pairs tested (increment) | cumulative pairs | survivors | wall (s) |
|---|---|---|---|---|
| $(10^7, 2\times10^7]$ | 90,032,870 | 172,843,243 | 0 | 111.74 |
| $(2\times10^7, 3\times10^7]$ | 91,082,513 | 263,925,756 | 0 | 124.02 |
| $(3\times10^7, 4\times10^7]$ | 96,205,463 | 360,131,219 | 0 | 114.21 |
| $(4\times10^7, 5\times10^7]$ | 82,818,527 | 442,949,746 | 0 | 110.97 |
| $(5\times10^7, 6\times10^7]$ | 106,568,728 | 549,518,474 | 0 | 133.66 |
| $(6\times10^7, 7\times10^7]$ | 116,090,385 | 665,608,859 | 0 | 121.92 |
| $(7\times10^7, 8\times10^7]$ | 83,542,772 | 749,151,631 | 0 | 105.61 |
| $(8\times10^7, 9\times10^7]$ | 90,115,493 | 839,267,124 | 0 | 90.96 |
| $(9\times10^7, 10^8]$ | 82,743,782 | 922,010,906 | 0 | 70.02 |

The decade $(10^7, 10^8]$ contributes $839{,}200{,}533$ pairs. The
increments vary substantially from block to block; that is expected,
because the pair count is dominated by the sparse values of $n$ with
very small $R(n)$ (for instance $n$ a power of two, where $R(n) = 1$
and every admissible $j$ is a candidate), whose contributions are
large and unevenly distributed.

**Final K-b statement.** Across the whole search, at even
$n \le 10^8$: **$922{,}010{,}906$ candidate pairs tested, zero
(LD3) survivors** (among pairs with $7 \le j \le n/2$, the search
range of §1; pairs with $j \le 6$ are closed for all $n$ in the
Cycle 2 record, so nothing about counterexamples is lost by the
restriction). The actual extension also came in below the
$1250.56$ s projection: the nine extension blocks above sum to
$983.11$ s of wall time, and the odd-only SPF build took a further
$18.60$ s.

## 5. K-c — targeted high-$v_2$ families, (LD3)+(N2)

The three targeted families (every member is even, a point used in
the overlap check below):

* **(i)** $n = m \cdot 2^a$ with $m$ odd, $1 \le m \le 999$, $a \ge 4$,
  $n \le 10^{12}$ (this includes $n = 2^a$);
* **(ii)** $n = 2^a + 2$ and $n = 2^a - 2$ for $3 \le a \le 40$;
* **(iii)** $n = 3^b + 1$ and $n = 3^b - 1$ for $2 \le b \le 25$.

For each $n$ the script factorises $n$, $n-1$, $n-2$ and $V_3(n)$
exactly (the factoriser and its prime bound are described in §1;
its cross-check against full trial division to $10^6$ on $300$
seeded random values in $[2, 10^{12}]$ found $0$ mismatches),
generates candidate $j$'s by the CRT pinning of §1 intersected with
$R(n) \mid j$ and the window $3 < j \le n/2$, and tests the full
(LD3) clauses and the exact divisibility $V_3(n) \mid C(j,3)$ on
each candidate.

| family | $n$ values | candidates after pinning | $j \le 5000$ | $j > 5000$ | survivors of (LD3)+(N2) |
|---|---|---|---|---|---|
| (i) | 13,931 | 1 | 1 | 0 | 0 |
| (ii) | 76 | 0 | 0 | 0 | 0 |
| (iii) | 48 | 0 | 0 | 0 | 0 |
| total | 14,055 | 1 | 1 | 0 | 0 |

**The single candidate, stated prominently as required for any
survivor-class object:** across all $14{,}055$ values of $n$, the
pinning produced exactly one candidate, $(n, j) = (16, 7)$ in
family (i). It is **not** a survivor: it fails the full
(LD3)+(N2) test applied in the script, and the survivor list for
every family is empty. (It is in any case at $j = 7 \le 5000$,
inside the range already closed for all $n$ by Cycle 2, so it
carries no new information; the new information in this section is
that at the remaining $14{,}054$ targeted values of $n$ — most of
them far above $10^6$ — the candidate generation of §1 (the (N2)
pinning congruences, intersected with $R(n) \mid j$ and the window)
already admits no $j$ at all, at any $j$, let alone a
$j > 5000$.)

**Fallback accounting.** The specification's fallback (direct
(LD3)-first enumeration over multiples of $R(n)$ in the
(N2)-size window) is triggered if the raw candidate count for a
single $n$ exceeds $10^6$. It was never triggered: the largest raw
(unpruned) CRT combination count for a single $n$ was $531{,}441$,
at $n = 68{,}719{,}476{,}736$ in family (i), and the largest
candidate list actually produced for a single $n$ was $1$ (at
$n = 16$). The script's list of fallback $n$ values is empty.

**Pinning validation.** For every family member with $n \le 50000$
($1{,}820$ values), the pinning candidate list was compared against
a brute-force enumeration of the multiples of $R(n)$ in
$(3, n/2]$ filtered by the exact test $V_3(n) \mid C(j,3)$: the
brute-force total was $1$ candidate (the same $(16, 7)$), and the
number of mismatching $n$ values was $0$.

**Overlap check against K-b/F2.21 (mandated).** Every family member
with $n \le 10^6$ is even, so these $n$ lie inside the K-b search
range. For the $4{,}029$ such values (union over the three
families), the script ran a direct (LD3) search over the multiples
$j$ of $R(n)$ with $3 < j \le n/2$, independent of the pinning
machinery: $4{,}088{,}173$ pairs tested, **zero survivors**,
agreeing exactly with the K-b result (and with F2.21) on this
range. The (LD3) verdicts of K-c and K-b therefore agree on the
whole overlap.

## 6. What this computation does and does not establish

**Established by this computation** (all of it COMPUTATION, in the
sense of F1.16/F2.18/F2.21: exact finite enumerations, with the
standing finite reduction doing the passage from a finite window to
all $n$ for a fixed pair):

1. (LD3) has no solution with $2j \le n \le N(3,j)$ for any
   $5 \le j \le 50000$ (Anchor A plus §3). By the finite reduction,
   exactly as in Corollary F2.19, every pair $(3, j)$ with
   $5 \le j \le 50000$ is thereby closed for all $n$. The Cycle 2
   per-pair frontier of $j \le 5000$ is extended by a factor of ten.
2. (LD3) has no solution with $n$ even, $n \le 10^8$, and
   $7 \le j \le n/2$ (§4), extending F2.21's $n \le 10^6$ statement
   by two decades of $n$.
3. None of the $14{,}055$ targeted high-$v_2$ values of $n$ in the
   families of §5 — most of them far above the K-b limit — admits
   any $j$ satisfying (LD3) and (N2) jointly, and for all but one of
   them the candidate generation already admits no $j$ at all.

**Updated necessary conditions.** Intersecting this computation
with the certified Cycle 2 record (no counterexample has $n$ odd;
every counterexample has $v_2(C(n,3)) \ge 4$; the $(Q,R)$
exclusions and label conditions of F1.11/F2.14), a counterexample
at $i = 3$, if one exists, must now have: $n$ **even**,
$j \ge 50001$, $n > 10^8$, and $v_2(C(n,3)) \ge 4$, and must lie in
the even residual class of Claim F1.11 / Claim F2.14. (The
$n > 10^8$ condition uses item 2 together with $j \ge 50001 \ge 7$:
any counterexample in the K-b range would have appeared as a
candidate pair of the search.)

**Not established.** (H3) remains open, $i = 3$ is not closed, and
Erdős #699 is not solved or claimed solved. The per-pair method
says nothing about $j > 50000$; the survivor search says nothing
about even $n > 10^8$ (or about $n$ odd, which the proof record,
not this computation, excludes for counterexamples); the families
of §5 are thin targeted sets, not a general argument. A survivor
of (LD3), had one appeared, would not have been a counterexample —
(LD3) is necessary, not sufficient — and none appeared in any part
of this computation.

**Reproducibility.** `proofs/P-K1_checks.py`, run end-to-end as a
single command (`python3 proofs/P-K1_checks.py`), Python standard
library only, exact integer arithmetic, single-threaded. Its
assertions include every anchor count of §2 and the emptiness of
every survivor list reported here; it fails loudly rather than
printing a summary if any of them is not reproduced. The total
wall time of the run reported here was $1335.43$ s; wall times
will vary between runs and machines, the counts will not.

## Appendix — final summary block, transcribed verbatim

```
=== FINAL SUMMARY BLOCK (K1) ===
anchor_C_N_spot_values_match = True
N(3,2000) = 3239787
N(3,5000) = 20263871
anchor_A_candidates_generated_F_style = 50489
anchor_A_candidates_le_Nmax_clean = 47723
anchor_A_pairs_N_filtered_j_le_5000 = 341633
anchor_A_pairs_N_filtered_j_le_2000 = 107220
anchor_A_survivors = 0
anchor_A_bruteforce_j_5_60_pairs = 52625
anchor_A_bruteforce_j_5_60_survivors = 0
Ka_pilot_block = (5001, 6000)
Ka_pilot_candidates = 87585
Ka_pilot_pairs_tested = 87585
Ka_pilot_survivors = []
Ka_pilot_wall_seconds = 2.07
N(3,6000) = 29182406
Ka_projected_5000_block_seconds = 20.67
Ka_final_j_target = 50000
Ka_block_5001_6000 = (87585, 87585, 0, 2.07, 29182406)
Ka_block_6001_10000 = (376940, 376940, 0, 12.37, 81075754)
Ka_block_10001_15000 = (518441, 518441, 0, 11.71, 182435650)
Ka_block_15001_20000 = (553625, 553625, 0, 14.74, 324343560)
Ka_block_20001_25000 = (583356, 583356, 0, 19.17, 506799482)
Ka_block_25001_30000 = (604055, 604055, 0, 21.57, 729803419)
Ka_block_30001_35000 = (623345, 623345, 0, 24.44, 993355368)
Ka_block_35001_40000 = (639202, 639202, 0, 27.47, 1297455331)
Ka_block_40001_45000 = (656122, 656122, 0, 34.66, 1642103307)
Ka_block_45001_50000 = (669568, 669568, 0, 43.33, 2027299296)
Ka_mandated_5001_20000_candidates = 1536591
Ka_mandated_5001_20000_pairs_tested = 1536591
Ka_mandated_5001_20000_survivors = []
Ka_mandated_5001_20000_wall_seconds = 40.88
N(3,20000) = 324343560
Ka_total_5001_to_target_candidates = 5312239
Ka_total_5001_to_target_pairs_tested = 5312239
Ka_total_5001_to_target_survivors = []
Ka_total_wall_seconds = 211.52
N(3,50000) = 2027299296
Kb_segment_0_100000 = (604976, 0, 49994, 1.04)
Kb_segment_100000_1000000 = (6369141, 0, 450000, 7.32)
Kb_segment_1000000_10000000 = (75836256, 0, 4500000, 90.95)
Kb_pairs_cumulative_1e5 = 604976
Kb_pairs_cumulative_1e6 = 6974117
Kb_anchor_B_pairs_1e6 = 6974117
Kb_pairs_cumulative_1e7 = 82810373
Kb_survivors_1e7 = []
Kb_crosscheck_interval_pairs_full_spf = 692165
Kb_segment_time_ratio = 12.43
Kb_projected_1e8_seconds = 1250.56
Kb_odd_spf_design_bytes = 200000000
Kb_extend_to_1e8 = True
Kb_odd_spf_actual_bytes = 200000000
Kb_crosscheck_interval_pairs_odd_spf = 692165
Kb_crosscheck_agrees = True
Kb_ext_block_10000000_20000000 = (90032870, 0, 111.74)
Kb_ext_block_20000000_30000000 = (91082513, 0, 124.02)
Kb_ext_block_30000000_40000000 = (96205463, 0, 114.21)
Kb_ext_block_40000000_50000000 = (82818527, 0, 110.97)
Kb_ext_block_50000000_60000000 = (106568728, 0, 133.66)
Kb_ext_block_60000000_70000000 = (116090385, 0, 121.92)
Kb_ext_block_70000000_80000000 = (83542772, 0, 105.61)
Kb_ext_block_80000000_90000000 = (90115493, 0, 90.96)
Kb_ext_block_90000000_100000000 = (82743782, 0, 70.02)
Kb_pairs_decade_1e7_1e8 = 839200533
Kb_final_limit = 100000000
Kb_pairs_cumulative_final = 922010906
Kb_survivors_final = []
Kc_factoriser_crosscheck_samples = 300
Kc_factoriser_crosscheck_mismatches = 0
Kc_family_i = (13931, 1, 1, 0, 0)
Kc_family_ii = (76, 0, 0, 0, 0)
Kc_family_iii = (48, 0, 0, 0, 0)
Kc_all_pinning_candidates = [('i', 16, 7)]
Kc_max_raw_combos = (531441, 68719476736)
Kc_max_candidates_single_n = (1, 16)
Kc_fallback_ns = []
Kc_survivors_total = []
Kc_pinning_validation_n_values = 1820
Kc_pinning_validation_brute_candidates = 1
Kc_pinning_validation_mismatches = 0
Kc_overlap_n_values_le_1e6 = 4029
Kc_overlap_pairs_tested = 4088173
Kc_overlap_survivors = 0
total_wall_seconds = 1335.43
=== END FINAL SUMMARY BLOCK (K1) ===
```
