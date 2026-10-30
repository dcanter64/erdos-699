# V-K: Independent verification of Cluster K (frontier extension at $i=3$), Cycle 3

Verifier: V-K (independent). Files verified: `proofs/P-K1.md` (with
`proofs/P-K1_checks.py`) and `proofs/P-K2.md` (with
`proofs/P-K2_checks.py`), against the shared Cluster K specification,
`CYCLE2.md` §2, `proofs/P-F1.md` (F1.15–F1.17), `proofs/P-F2.md`
(F2.18–F2.21, §6), and `verification/V-F.md`.

Verifier's own computations (Python stdlib only, exact arithmetic,
single thread): `verification/V-K_checks.py`, sections S0–S6.
Implementations differ from both computers' where feasible: Anchor A
and the brute-force cross-check use the per-prime-power (q) form with
trial-division factorisation; the K-a and K-b recounts use the
aggregate form ($R(n)\mid j$, $R(n-1)\mid j(j-1)$,
$R(n-2)\mid j(j-1)(j-2)$), whose equivalence to the q-form is proved
in §5 below and was validated empirically (section S3) before use;
the K-c factoriser is trial division to 1000 plus deterministic
Miller–Rabin plus a simple (non-Brent) Pollard rho. In addition, both
computers' scripts were run end-to-end as filed by the verifier
(§8). The verifier's runs took place on a shared VM with several
other campaign processes active, so wall times in the verifier's runs
run long; every count below is exact and wall-independent.

**Headline verdict. COMPUTATION (verified), on every item. The two
computers agree with each other and with the verifier's independent
recounts on every single count. (LD3) has no solution with
$2j \le n \le N(3,j)$ for every $5 \le j \le 50000$ (1,536,591 pairs
recounted in full on the mandated range $5001 \le j \le 20000$, plus
one full block beyond it; the remaining blocks to 50000 are covered
by the two computers' independent implementations, both re-run
end-to-end by the verifier). (LD3) has no solution with even
$n \le 10^8$ (recounted in full to $10^7$ under both counting
conventions, plus a segmented recount of $(10^7, 2\times10^7]$, plus
the exact convention reconciliation to $10^8$, on top of the two
computers' full $10^8$ runs). The K-c families (14,055 values of $n$)
contribute exactly one CRT candidate, $(n,j) = (16,7)$, which fails
(LD3) at $r=1$, $q=5$, and no candidate with $j > 5000$. No
discrepancy in any count was found anywhere. This is a verified
computation, not a proof of (H3): $i=3$ in general remains open.**

---

## 1. Anchors (task item 1)

**Anchor C ($N(3,j)$ spot values).** The verifier's own binary search
reproduces all eight values exactly: $N(3,7) = 27$,
$N(3,100) = 7{,}908$, $N(3,158) = 19{,}926$, $N(3,159) = 20{,}181$,
$N(3,500) = 201{,}728$, $N(3,1000) = 808{,}934$,
$N(3,2000) = 3{,}239{,}787$, $N(3,5000) = 20{,}263{,}871$ (script S0).

**Anchor A (per-pair, $5 \le j \le 5000$).** Both candidate counts
were recomputed from scratch (script S2). The F-style generation
(odd $d \le 5000$, $v_3(d) \ne 1$, $t$ a power of two, the
$d \cdot 3 \cdot t$ branch added without an $N$-bound) gives exactly
50,489 candidates; the bounded generation gives exactly 47,723; the
difference is exactly 2,766 candidates, and the verifier confirmed
that all 2,766 lie in $(N(3,5000),\, 3\,N(3,5000)]$ and that the
bounded set equals the F-style set filtered by $n \le N(3,5000)$.
Since every pair needs $n \le N(3,j) \le N(3,5000)$, the explanation
in both reports (P-K1 §2, P-K2 §2.1) is verified in full: the 2,766
unbounded candidates contribute 0 pairs. The pair test itself, run
by the verifier in q-form over the bounded candidates, gives
341,633 pairs (107,220 of them at $j \le 2000$, matching V-F) and
**zero survivors**.

**Anchor B (even $n \le 10^6$).** The verifier's recount (script S3,
q-form and aggregate form in parallel, see §5) gives 6,974,117 pairs
under F2.21's $j \ge 7$ convention and 6,974,250 under the
specification window $j > 3$, zero survivors under either. The
difference of exactly 133 pairs at $j \in \{4,5,6\}$ was verified by
direct enumeration of those pairs, with the exact breakdown by
$(j, R(n))$: $(4,1){:}\ 34$, $(5,1){:}\ 33$, $(5,5){:}\ 33$,
$(6,1){:}\ 33$. (No pair occurs at $j=6$, $R(n)=3$: $R(n)=3$ is
impossible, since the 3-part of $R$ has exponent 0 or $\ge 2$. The
$R(n)=5$ pairs come from odd parts 5 and 15, the latter with the
single factor 3 stripped.) Both computers' accounts of the
convention difference are exact.

**Brute-force cross-check.** Over all $n \in [2j, N(3,j)]$ for
$5 \le j \le 60$, no candidate generation, q-form throughout: 52,625
pairs, zero survivors (script S1), as required.

## 2. K-a agreement (task item 2)

The arithmetic reconciliation checks out exactly:
$1{,}536{,}591 + 341{,}633 = 1{,}878{,}224$ (K1's extension-only total
plus the anchor range equals K2's total to $j = 20000$) and
$5{,}312{,}239 + 341{,}633 = 5{,}653{,}872$ (the same to $j = 50000$).
K1's per-block counts also sum to its stated totals.

The verifier's own implementation (aggregate form, per-$j$ divisor
generation) fully recounted the mandated range, block by block
(script S4): [5001,6000] 87,585; [6001,10000] 376,940;
[10001,15000] 518,441; [15001,20000] 553,625; total on
$5001 \le j \le 20000$: **1,536,591 pairs, zero survivors**, matching
both computers block for block. The verifier's chosen full 5000-block
in $(20000, 50000]$ is [20001,25000]: **583,356 pairs, zero
survivors**, matching both computers. The remaining blocks to 50000
were not recounted a third time by hand; they are covered by the two
independent computer implementations, both of which the verifier
re-ran end-to-end with identical block counts (§8).

## 3. K-b agreement (task item 3)

The verifier fully recounted even $n \le 10^7$ under **both**
conventions (script S5, aggregate form), decade by decade:

| even $n$ in | pairs ($j>3$) | pairs ($j\ge7$) | survivors |
|---|---|---|---|
| $(0,10^5]$ | 605,084 | 604,976 | 0 |
| $(10^5,10^6]$ | 6,369,166 | 6,369,141 | 0 |
| $(10^6,10^7]$ | 75,836,283 | 75,836,256 | 0 |
| total $\le 10^7$ | 82,810,533 | 82,810,373 | 0 |

Every figure matches both computers (K1 reports the $j\ge7$ column;
K2 reports both). Convention differences per decade: 133 at
$\le 10^6$ (direct enumeration, §1); **27 in $(10^6,10^7]$**, verified
two ways, by direct enumeration over all even $n$ in the decade
(7 values of $n$ with $R(n)=1$, 6 with $R(n)=5$) and by the targeted
method below, the two agreeing exactly; **25 in $(10^7,10^8]$**, by
the exact targeted count: a pair at $j \in \{4,5,6\}$ needs
$R(n) = 1$ (for $j = 4, 6$; $R(n)=3$ is impossible) or
$R(n) \in \{1,5\}$ (for $j=5$), and $R(n)=1$ iff the odd part of $n$
is in $\{1,3\}$, $R(n)=5$ iff it is in $\{5,15\}$ (odd part with a
single factor 3 stripped when $v_3 = 1$). In $(10^7,10^8]$ the
$c \cdot 2^a$ enumeration gives 6 values with $R(n)=1$ and 7 with
$R(n)=5$, hence $3 \cdot 6 + 7 = 25$ pairs. The targeted method was
validated against the direct enumeration on $(10^6,10^7]$ (counts
7 and 6, giving 27) before being trusted on the higher decade. Total
convention difference to $10^8$: $133 + 27 + 25 = 185 =
922{,}011{,}091 - 922{,}010{,}906$, consistent.

**Segmented recount in $(10^7,10^8]$.** The verifier recounted the
full first sub-block $(10^7, 2\times10^7]$: 90,032,878 pairs
($j>3$), 90,032,870 pairs ($j\ge7$), zero survivors. The $j\ge7$
figure is exactly K1's block increment for that interval (K1 is the
only computer reporting sub-decade blocks), and the difference of 8
matches the targeted count on this sub-block (2 values with
$R(n)=1$, 2 with $R(n)=5$). Per the task's standard, a full
independent recount to $10^8$ was therefore not required: the $10^7$
recount, the convention reconciliation, and the segmented recount
all agree, and both computers' own full $10^8$ runs were re-executed
by the verifier (§8) with identical totals (922,011,091 in the
$j>3$ convention, 922,010,906 in the $j\ge7$ convention, zero
survivors). This also settles P-K2 §4.3's disclosure: the discarded
preliminary figure of 902,986,145 pairs for the decade is not
reproduced by anything; the clean value 839,200,558 ($j>3$) /
839,200,533 ($j\ge7$) is confirmed by K1's independent block sum,
by K2's clean run, and (on the first sub-block) by the verifier.

## 4. What the two computers' conventions do and do not affect

K1 counts K-b in the $j \ge 7$ convention throughout (its §1 explains
why: it is the convention of the F2.21 anchor it had to reproduce);
K2 counts in the specification window $j > 3$ and reports both. The
verifier confirms the two conventions differ by exactly the
$j \in \{4,5,6\}$ pairs enumerated above, that all such pairs also
fail (LD3) (they are included in the verifier's $j>3$ recounts, with
zero survivors), and that pairs with $j \le 6$ are in any case closed
for all $n$ in the Cycle 2 record. The headline statement "(LD3) has
no solution with even $n \le 10^8$" holds in the wider ($j>3$)
window, hence a fortiori in the narrower one.

## 5. P-K2's aggregate form (task item 4)

**The equivalence is correct; the verifier's audit of the proof is
as follows.** Fix a top $m = n - r$, $r \in \{0,1,2\}$. The relevant
prime powers $q = p^a \Vert m$ are pairwise coprime (distinct
primes), so $R(m)$ is their product. Every relevant $q$ satisfies
$q \ge 5$ (for $p \ge 5$) or $q \ge 9$ (for $p = 3$, $a \ge 2$); in
particular $q > r$ always, which is the boundary fact the
correspondence turns on.

(Per-clause $\Rightarrow$ aggregate.) If $j \bmod q = s \le r$ then
$q \mid j - s$, one factor of $P_r = j(j-1)\cdots(j-r)$. Since this
holds for every relevant $q$ and the $q$ are pairwise coprime, their
product $R(m)$ divides $P_r$.

(Aggregate $\Rightarrow$ per-clause.) Suppose $R(m) \mid P_r$ and fix
a relevant $q = p^a \mid R(m)$. At most one of the factors
$j, j-1, \ldots, j-r$ is divisible by $p$: two of them differ by at
most $2 < p$ for $p \ge 5$, and exactly one of any three consecutive
integers (and of any two) is divisible by 3. Hence the full
$p$-adic valuation of $P_r$ is carried by a single factor $j - s$,
so $q \mid j - s$ for that $s \le r$, and since $s < q$ this says
$j \bmod q = s \le r$. This prime-power concentration step is the
load-bearing point for $a \ge 2$ (in particular for the $p = 3$,
$a \ge 2$ cases, $q \ge 9$); P-K2 §1 states it in compressed form
("at most one of the three is divisible by any odd prime $p$"),
which is correct and sufficient. The $r = 0$ clause is $R(n) \mid j$
itself. Equivalence holds for all three clauses.

**Empirical test (script S3).** On **all** 6,974,250 candidate pairs
at even $n \le 10^6$, the aggregate verdict and the q-form verdict
(SPF factorisations) were compared pair by pair: **0 disagreements**.
On a seeded random sample (seed 20261030) of 3,000 even $n$ in
$(10^6, 10^8]$, all 225,841 candidate pairs were compared the same
way (trial-division factorisations): **0 disagreements**. (One
anomaly is recorded for transparency: the verifier's S3+S6 script
was executed twice by the runtime as duplicate background
processes, and the two executions differed in this one diagnostic
count only (84,474 in the first output received, 225,841 in the
second), every other number in S3 and S6 being identical between
them and all assertions passing. The verifier recomputed the sample
standalone, exactly as the filed script defines it, and 225,841
with 0 disagreements is the correct figure of record.) K2's use
of the aggregate form for its $10^8$ extension, and the verifier's
use of it in S4/S5, are both validated.

## 6. K-c (task item 5)

**CRT pinning logic: audited and correct.** For $p \ge 5$ with
$p^e \Vert V_3(n)$: $p \nmid 6$, so $V_3(n) \mid C(j,3)$ forces
$p^e \mid j(j-1)(j-2)$; at most one of the three factors is
divisible by $p$, so that one carries the full $p^e$, i.e.
$j \equiv 0, 1$ or $2 \pmod{p^e}$. For $p = 3$ the bookkeeping is as
specified: $v_3(C(j,3)) = v_3(j(j-1)(j-2)) - v_3(6) =
v_3(j(j-1)(j-2)) - 1$, so $v_3(C(j,3)) \ge e_3$ forces
$v_3(j(j-1)(j-2)) \ge e_3 + 1$; exactly one factor is divisible by
3, hence $j \equiv 0, 1$ or $2 \pmod{3^{e_3+1}}$. When $e_3 = 0$ no
3-pin arises (and none is needed: $v_3 \ge 1$ is automatic). The
$R(n) \mid j$ folding is also correct: a pinning prime power for a
prime dividing $n$ itself is exactly $R(n)$'s prime power there
(for $p = 3$ this needs $v_3(n) = e_3 + 1 \ge 2$, which is exactly
when the 3-pin modulus $3^{e_3+1}$ equals $R(n)$'s 3-part), and the
residue is forced to 0 at precisely those pins. K2's modulus
identity (pinning modulus $= 3V_3(n)$ if $e_3 \ge 1$, else $V_3(n)$)
checks out.

**Independent recount (script S6).** Family enumeration from the
definitions: (i) 13,931 values, (ii) 76, (iii) 48, total **14,055**,
matching both computers. The verifier's own pinning (CRT combination
in decreasing-modulus order with window pruning; candidates asserted
to satisfy $V_3(n) \mid C(j,3)$ exactly) reproduces: exactly **one**
candidate across all families, $(n, j) = (16, 7)$ in family (i),
zero candidates with $j > 5000$, zero survivors of (LD3)+(N2). The
candidate's failure is exactly as P-K2 states: at $r = 1$ the only
relevant prime power of $n - 1 = 15$ is $q = 5$ (the factor 3 has
$a = 1$ and is not relevant), and $7 \bmod 5 = 2 > 1$; the pair does
satisfy (N2), $V_3(16) = 35 = C(7,3)$, as both computers note. The
maximum raw CRT combination count is **531,441 at
$n = 68{,}719{,}476{,}736 = 2^{36}$**, as both computers report, so
the $10^6$ fallback threshold is indeed never reached. As an extra
cross-check not required by the task, the verifier's raw combination
totals per family (12,714,813; 213,468; 19,332) match K2's reported
CRT combination totals exactly; these totals are sensitive to the
forced-versus-free residue bookkeeping at every pin, so this is a
strong check on the pinning implementations. The verifier's
factoriser was cross-checked against full trial division to $10^6$
on 150 seeded random values in $[2, 10^{12}]$: 0 mismatches.

**Pinning validation.** For the family members $\le 50{,}000$
(**1,820** distinct values), the pinning candidate lists were
compared against brute force (multiples of $R(n)$ in $(3, n/2]$
filtered by the exact test $V_3(n) \mid C(j,3)$): brute-force total
1 candidate (the same $(16,7)$), **0 mismatching $n$**, as both
computers claim.

**Overlap check.** The distinct family members $\le 10^6$ number
**4,029**; a direct (LD3) search over the multiples of $R(n)$ tests
**4,088,173 pairs, zero survivors**, agreeing with K-b and F2.21, as
both computers report.

## 7. Scripts (task item 6)

Both scripts were run **in full, end-to-end as filed**, by the
verifier (this exceeds the task's minimum, which allowed a partial
run of the longer script):

* `P-K2_checks.py`: completed in 796.6 s (reported run: 686.3 s).
  Its final summary block matches P-K2.md §7 on every count, block
  total, candidate count, and survivor list. The only differing
  fields are wall times and the wall-derived extrapolation figures
  (pilot projections 13–25 s in the verifier's run against 29–57 s
  in the filed run; the $10^8$ projection 535 s against 619 s; the
  decisions they feed are unchanged: extension to 50000 and to
  $10^8$ in both runs).
* `P-K1_checks.py`: completed in 1,530.0 s (reported run:
  1,335.43 s). Its final summary block was compared key by key
  against the appendix of P-K1.md: all 79 keys present in both, and
  every differing key (29 of them) is a wall time or a wall-derived
  projection (for example the segment time ratio 10.478 against
  12.43, and the $10^8$ projection 1,329.33 s against 1,250.56 s,
  both under the script's 1,800 s threshold, so the extension
  decision is unchanged). Every count, candidate total, pair total,
  $N(3,j)$ value, and survivor list is identical.

The verifier's own script sections ran in 0.3 s (S0+S1), 7.2 s
(S2+S4), about 1,600 s of wall time (S3+S6, under heavy contention from
other campaign processes on the shared VM), and 94.2 s (S5).

## 8. Final certified statement (task item 7)

Certified, all as **COMPUTATION (verified)**, not as a proof of
(H3):

1. **(LD3) has no solution with $2j \le n \le N(3,j)$ for every
   $5 \le j \le 50{,}000$.** Hence, by the standing finite reduction
   exactly as in Corollary F2.19 (the sole $i=3$ EEES78 exception
   pair $(8,3)$ admits no $j \ge 5$), every pair $(3,j)$ with
   $5 \le j \le 50{,}000$ is closed for all $n$. The Cycle 2 frontier
   $j \le 5000$ is extended by a factor of ten. (Pairs with $j \le 4$
   were already closed in the Cycle 2 record.)
2. **(LD3) has no solution with even $n \le 10^8$** (in the window
   $3 < j \le n/2$, hence also for $7 \le j \le n/2$): 922,011,091
   candidate pairs in the wider window, zero survivors.
3. **The K-c families contribute no (LD3)+(N2) survivor and no
   candidate with $j > 5000$**: over all 14,055 targeted values of
   $n$, CRT pinning leaves only $(16,7)$, which fails (LD3).

Intersecting with the certified Cycle 2 record (no $i=3$
counterexample has $n$ odd; every counterexample has
$v_2(C(n,3)) \ge 4$), an $i=3$ counterexample, if one exists, must
now have $n$ even, $n > 10^8$, $j \ge 50{,}001$, and
$v_2(C(n,3)) \ge 4$. **(H3) remains open, $i = 3$ is not closed, and
Erdős #699 is not claimed solved.** A survivor of (LD3), had one
appeared, would not have been a counterexample, (LD3) being
necessary and not sufficient; none appeared in any part of
Cluster K.

**Discrepancies found: none.** Every number in both reports that
the verifier checked, which is every headline count, block count,
anchor, candidate total, combination total, and survivor list in
either file, was reproduced exactly by at least one independent
implementation, and the mandated ranges were reproduced by the
verifier's own code as detailed above. The only non-reproduced
figures anywhere are wall times and the projections derived from
them (expected, machine-dependent, and feeding no count), and the
preliminary decade figure that P-K2 itself discards in its §4.3,
which the verifier confirms is superseded by the correct value.

— V-K
