# Referee 2 Report (Adversarial) — Erdős #699, the j ≤ 3i/2 Exposition

**Object refereed:** Thomas Bloom's exposition (erdosproblems.com/699, last
edited 27 Aug 2026) of the claimed GPT 5.6 Sol / Liam Price proof of Erdős
Problem #699 in the region j ≤ 3i/2. The raw GPT claim is HTTP
403-inaccessible (established; not refetched) and is **not** refereed here.
**Mandate:** try to break the argument; assume Phase 0 (verdict: SOUND
conditional on EEES78) may have missed something; verify independently.
**Date:** 2026-10-28. **Method:** independent re-derivation, edge-case
analysis, and fresh bounded Python (stdlib only) falsification attempts,
total compute ≈ 36 s across five scripts.

## Verdict in one paragraph

No ERROR was found in the exposited j ≤ 3i/2 argument: every algebraic and
combinatorial step re-derives, and all five computational attacks (A)–(E)
came back clean. However, the exposition is **not a self-contained proof of
the region**: it invokes EEES78 "with finitely many explicit exceptions"
without ever naming the 12 exception pairs or checking a single one of
them, and the entire deduction is conditional on (n, i) not being an
exception. That gap is fillable — I fill it in §3(C) and §2.6 below — but a
reader of the exposition alone cannot discharge it. The one genuine
casualty is the page's separate assertion of the case **n = 2j** (for
general i): the exposited chain provably does **not** cover it (smallest
failure (i, j) = (1, 2): C(4, 1) = 4 < 6 = C(4, 2)), so that assertion, if
it rests on this argument, is an ERROR of coverage; the n = 2j statement
itself survived direct testing for all j ≤ 400 (§3(E)) and may well have a
different proof in the inaccessible raw claim — as exposited, it is
UNVERIFIABLE / unproved.

---

## 1. Convention audit (≥ vs >)

### 1.1 Exactly which EEES78 statement the proof needs

The proof needs the partition at k = i with the boundary prime assigned to
v:

- C(n, i) = u·v, u supported on primes **< i**, v = V_i(n) supported on
  primes **≥ i**;
- conclusion u < v, with exactly the 12 exceptions
  (8,3), (9,4), (10,5), (12,5), (21,7), (21,8), (30,7), (33,13), (33,14),
  (36,13), (36,17), (56,13).

This is Bloom's convention and it matches the EEES78 abstract verbatim as
recorded in Phase 0, Item 4 ("each prime factor of u is less than k, and
each prime factor of v is at least equal to k … u < v holds with just 12
exceptions").

### 1.2 The derivation v > C(n, i)^{1/2}

Sound. The supports are disjoint and exhaust all primes, so u, v are
positive integers with u·v = C(n, i) and gcd(u, v) = 1. If u < v then
C(n, i) = u·v < v·v = v², i.e. v > C(n, i)^{1/2}. (Conversely v >
C(n,i)^{1/2} would give u = C/v < v, so under this partition the two forms
are equivalent.) EEES78's hypothesis n ≥ 2k is met with room to spare: in
the problem's range n ≥ 2j > 2i. In the exceptions the inequality in fact
fails strictly the other way: exact computation (§3(C)) gives u > v for
all 12, e.g. (56,13): u = 1,940,400 > v = 973,981; there is no u = v
borderline case anywhere in n ≤ 600.

### 1.3 The trap: substituting the OTHER convention (v on primes > k)

EEES78 also treats the convention u_≤ (primes ≤ k), v_> (primes > k), for
which — per the record supplied and Phase 0's caution — there are 19 known
cases with u_≤ > v_> and only **finiteness** is proved; the 19 are not
proved to be all. Substituting this convention breaks the proof at exactly
two places, and nowhere else:

**(a) The reformulation step becomes FALSE.** With v_> in place of v, the
claim "the problem is equivalent to asking whether v can be coprime to
C(n, j)" is the *strengthened* problem (common prime p > i), which has
counterexamples. Verified witness (n, i, j) = (28, 5, 14), computed
exactly:

```
C(28,5) = 98280, prime exponents {2:3, 3:3, 5:1, 7:1, 13:1}
V_{>=5} = 455 = 5*7*13,   V_{>5} = 91 = 7*13
gcd(C(28,5), C(28,14)) = 1080 = 2^3 * 3^3 * 5
gcd(V_{>=5}, C(28,14)) = 5        (the prime p = i = 5 itself)
gcd(V_{>5},  C(28,14)) = 1        (no common prime > i)
```

So with the > convention the very first sentence of the exposition asserts
an equivalence with a false statement, and the argument would "prove"
something untrue. The boundary prime p = i is load-bearing **here**:
the original problem counts p = i; the strengthened one does not, and
(28, 5, 14) separates them.

**(b) The EEES78 input becomes unavailable and its exception set changes.**
Moving the prime i (when i is prime) from v to u replaces v by v / i^e and
u by u · i^e, where e = v_i(C(n, i)); the inequality u < v becomes
strictly stronger and fails at pairs where the ≥ version holds. Exact
search, n ≤ 200: there are **7 pairs** where u_< < v_≥ (EEES78's ≥
conclusion holds) but u_≤ ≥ v_> (the > conclusion fails), equivalently
v_>² ≤ C(n, i) < v_≥², so the square-root step itself collapses:

```
(n,k) = (9,3):   C=84,        u_< =4    < v_>= =21,     u_<= =12   > v_> =7
(n,k) = (10,3):  C=120,       u_< =8    < v_>= =15,     u_<= =24   > v_> =5
(n,k) = (18,3):  C=816,       u_< =16   < v_>= =51,     u_<= =48   > v_> =17
(n,k) = (28,5):  C=98280,     u_< =216  < v_>= =455,    u_<= =1080 > v_> =91
(n,k) = (54,7):  C=177100560, u_< =2160 < v_>= =81991,  u_<= =15120 > v_> =11713
(n,k) = (82,3):  C=88560,     u_< =16   < v_>= =5535,   u_<= =432  > v_> =205
(plus a seventh pair ≤ 200, beyond the six printed by the search)
```

Note (9,3) is **not** among the 12: the exception list is
convention-dependent, not a cosmetic relabelling. And because the
> convention theorem proves only finiteness, a reader substituting it
could not even in principle discharge the exceptions — the set to check
is not explicitly known.

**(c) Where the boundary prime does NOT enter.** The key lemma, the
Vandermonde step, and the final monotonicity chain are threshold-agnostic:
they work for *any* divisor d of C(n, i) coprime to C(n, j), and in the
final chain i figures only as an integer parameter in 2(j − i) ≤ i, not as
a prime. If i is composite the two conventions literally coincide (no
prime equals i); the distinction is material exactly when i is prime, and
it enters the proof at precisely two points: the definition of v
(equivalence with the problem) and the EEES78 citation (partition and
exception list). **Conclusion: Bloom's exposition uses the correct
convention consistently; no silent convention slip was found. But the
convention is load-bearing, and any transcription of this proof that
drifts to "primes > i" is proving a false statement from an unproved
input.**

## 2. Edge-case hunting

**2.1 i = 1.** EEES78 at k = 1: u is the empty product = 1 < n = v for all
n ≥ 2, no exceptions (the scan in §3(C) covers k = 1 for all n ≤ 600 and
finds none). In the corollary region i = 1 admits no j at all (1 < j ≤ 3/2
is empty), so the region statement is vacuous at i = 1; the general
argument is unaffected. No break.

**2.2 j = i + 1 (d = j − i = 1).** Then C(j, j−i) = j and the Vandermonde
sum has exactly the three terms k = 0, 1, 2:
C(2j, 2) = 2·C(j, 2) + j² = j(2j − 1) > j² for j ≥ 2. Strictness holds
with the minimum possible number of terms; j ≥ 2 is forced since j > i ≥
1. No break.

**2.3 j = 3i/2 exactly (i even, i = 2m, j = 3m).** Then 2(j − i) = i, so
the first final-chain inequality C(2j, 2(j−i)) ≤ C(2j, i) is an
**equality**, and if also n = 2j the second is an equality too. The
contradiction survives because the strictness is upstream:
C(n, i) < C(2j, 2(j−i)) is strict (EEES78 strict + Vandermonde strict),
yielding C(n, i) < C(n, i). The boundary is genuinely included; the ≤'s
in the final chain are sufficient. Computationally (§3(D)) at the boundary
N(i, j) = 2j − 1 exactly (e.g. (300, 450): N = 899). No break.

**2.4 n = 2j exactly.** Inside the region j ≤ 3i/2 this is covered (see
2.3). Outside the region it is the separate assertion attacked in §3(E):
**not covered by the exposited chain.**

**2.5 n = 2i ("smallest n").** Vacuous, and worth stating plainly: the
joint hypotheses i < j ≤ n/2 force n ≥ 2j > 2i, so **no admissible triple
has n = 2i**. EEES78 in isolation permits n = 2k, but combined with j > i
that configuration is empty. Nothing to check; no break.

**2.6 The case v = 1.** If V_i(n) = 1, then gcd(v, C(n, j)) = 1 trivially
and the original problem fails outright for that (n, i) regardless of j
(no prime ≥ i divides C(n, i) at all). Reconciliation, three ways:
(i) The gcd formulation is an exact equivalence, v = 1 included:
gcd(V_i(n), C(n,j)) > 1 iff a common prime p ≥ i exists; if v = 1 both
sides are false together. (ii) Sylvester–Schur, as recorded on the problem
page, gives a prime p **> i** dividing C(n, i) for 1 ≤ i ≤ n/2, which
forces v ≥ p > 1 — so v = 1 is impossible in range, *given*
Sylvester–Schur. Note the exposition itself never cites Sylvester–Schur
in the proof chain; it doesn't need to, because (iii) EEES78 plus direct
inspection covers it: outside the 12 exceptions v > C(n,i)^{1/2} ≥ 1, and
for the exceptions exact computation gives v ∈ {7, 7, 7, 11, 323, 323,
377, 20677, 20677, 15283, 20677, 973981} — minimum 7. Independently, my
scan of all (n, k), n ≤ 600, found no v = 1 (any v = 1 would have
D = log(v/u) = −log C ≪ 0 and would have been flagged; §3(C)). Specified
check (8,3): C(8,3) = 56 = 2³·7, v = 7 > 1, consistent. **No (n, i) in
range with V_i(n) = 1 was found, and Sylvester–Schur excludes it in
general.** No break.

**2.7 Exception pairs inside the region (the exposition's silence,
discharged).** The deduction is conditional on (n, i) not being an EEES78
exception, and the exposition names no exceptions and checks none. I
discharged all 12 directly: for each exception pair (n₀, i₀), gcd(V_{i₀}
(n₀), C(n₀, j)) was computed for every admissible j. In the region
j ≤ 3i₀/2 the gcds are all > 1 (indeed all > 1 for **every** admissible j,
both regions):

```
(8,3):   V=7      region j=[4]          gcds=[7]
(9,4):   V=7      region j=[]          (no admissible j at all: j>4, j<=4)
(10,5):  V=7      region j=[]          (no admissible j at all)
(12,5):  V=11     region j=[6]         gcds=[11]
(21,7):  V=323    region j=[8,9,10]    gcds=[323,323,323]
(21,8):  V=323    region j=[9,10]      gcds=[323,323]
(30,7):  V=377    region j=[8,9,10]    gcds=[377,377,377];  min over all j: 29
(33,13): V=20677  region j=[14,15,16]  gcds all 20677
(33,14): V=20677  region j=[15,16]     gcds all 20677
(36,13): V=15283  region j=[14..18]    gcds=[15283 x3, 899, 899]
(36,17): V=20677  region j=[18]        gcds=[20677]
(56,13): V=973981 region j=[14..19]    gcds=[973981 x3, 57293 x3]; min over all j: 42347
```

So the gap is fillable and is hereby filled, but it is a real gap *in the
exposition as written* (see §4).

## 3. Computational falsification attempts (fresh, independent code)

All runs Python 3.12, stdlib only. Exact outputs quoted verbatim.

**(a) Key lemma, strong form — PASS.** For every triple, the part of
C(n, i) coprime to C(n, j) (computed by completely stripping every prime
shared with C(n, j), via repeated gcd) divides C(j, i). Binomials from an
exact Pascal table.

```
A n<=300: triples=1113775 failures=0 [] elapsed=12.92s
```

1,113,775 triples (strictly larger than Phase 0's n ≤ 240 scan), zero
failures. The lemma is also proved in the text (identity + Euclid), so
this is corroboration, not the sole support.

**(b) Vandermonde strictness — PASS.** All (j, d), 1 ≤ d = j−i < j ≤ 1000.
Method: (i) the sum Σ_k C(j,k)C(j,2d−k) always has ≥ 3 positive terms
(k ranges over [max(0, 2d−j), min(j, 2d)], cardinality 2d+1 if 2d ≤ j,
2i+1 if 2d > j, both ≥ 3), and the k = d term is C(j,d)² — a rigorous
proof of strictness for all pairs; (ii) float scan of the log-ratio via
lgamma as a numerical cross-check; (iii) exact integer check for j ≤ 200.

```
B pairs(j,d)=499500 min_positive_terms=3 min_log_ratio=0.405465 at (j,d)=(2, 1) elapsed=4.09s
B exact j<=200: pairs=19900 failures=0
```

The minimum ratio is at the extreme corner (j, d) = (2, 1):
C(4,2)/C(2,1)² = 6/4 = 1.5, log = 0.405465 — an enormous margin over any
float error (~1e-12), so the scan is effectively exact.

**(c) EEES78 u < v verified directly, n ≤ 600 — PASS, exceptions exactly
the 12.** Method: for fixed n, prime exponents of C(n, k) updated
incrementally in k by factoring (n−k+1)/k (numbers ≤ 600, spf table);
D = log v − log u accumulated in floating point; every pair with D ≤ 0.02
recomputed **exactly** (Legendre exponents, integer u and v). The method
was validated against a fully independent brute-force exact computation
for n ≤ 80, which returned the same 12 exceptions. Accumulated float
error over ≤ 300 steps is ≲1e-10, four-plus orders below the 0.02
threshold, and in the event only the 12 exceptions were even flagged.

```
scan pairs=90000 flagged(|D|<=0.02 or D<=0)=12 elapsed=2.36s
exact check of flagged: exceptions(u>=v)=[(8, 3, 8, 7), (9, 4, 18, 7), (10, 5, 36, 7),
 (12, 5, 72, 11), (21, 7, 360, 323), (21, 8, 630, 323), (30, 7, 5400, 377),
 (33, 13, 27720, 20677), (33, 14, 39600, 20677), (36, 13, 151200, 15283),
 (36, 17, 415800, 20677), (56, 13, 1940400, 973981)]
C n<=600: pairs=90000 exceptions_found=12 v_eq_1_among_flagged=[]
brute n<=80 exceptions: [(8, 3), (9, 4), (10, 5), (12, 5), (21, 7), (21, 8), (30, 7),
 (33, 13), (33, 14), (36, 13), (36, 17), (56, 13)]
```

90,000 pairs; the exceptions found are exactly the published 12, all with
n ≤ 56, all with u > v strictly, all with v ≥ 7. No 13th exception lurks
in n ≤ 600, and the published claim of "just 12" (which makes the list
complete, not truncated) is consistent with everything computable here.

**(d) Corollary form — PASS.** For all i ≤ 300 and i < j ≤ 3i/2 (22,500
pairs), N(i, j) := max{n : C(n, i) < C(2j, 2(j−i))} computed exactly by
binary search on the strictly increasing function C(·, i) (math.comb,
exact integers):

```
D pairs=22500 violations(N>=2j)=0 min_margin_2j_minus_N=1 at (i,j,N)=(2, 3, 5) maxN_triple=(300, 450, 899) elapsed=12.36s
```

N(i, j) < 2j for every pair: the interval is empty throughout the region,
exactly as the corollary requires. The margin is tight in the expected
place: 2j − N = 1 on the boundary j = 3i/2 (e.g. (2,3): N = 5; (300,450):
N = 899), reflecting the equality case of §2.3 — the proof's strictness
budget is exactly one integer at the boundary, and it comes entirely
from the upstream strict inequalities. There is no slack to spare, but
there is no deficit either.

**(e) The n = 2j case — statement survives testing; the exposited proof
does NOT cover it.** (i) Direct check: for all i < j ≤ 400, n = 2j,
gcd(V_i(2j), C(2j, j)) > 1, computed exactly via prime-support bitmasks
of C(2j, i) (incremental exponents) intersected with the support of the
central binomial and the primes ≥ i:

```
E1 n=2j, j<=400: pairs=79800 failures(gcd(V_i(2j),C(2j,j))=1)=0 [] elapsed=1.46s
```

(ii) But the exposited chain cannot be the proof: the derived necessary
condition for a counterexample, C(n, i) < C(2j, 2(j−i)), is **satisfied**
at n = 2j for a large set of pairs with j > 3i/2, so no contradiction is
available. Classification of when C(2j,i) < C(2j,2(j−i)) holds was done
via effective index min(x, 2j−x) (C(2j, ·) is symmetric and strictly
increasing on [0, j]) and verified against exact math.comb for all
j ≤ 60 (0 mismatches):

```
E2 j<=400: chain-failure pairs=53200 smallest=(1, 2) first_few=[(1, 2), (1, 3), (1, 4), (2, 4), (1, 5), (2, 5), (3, 5), (1, 6)]
E2 smallest exact: i=1 j=2 C(2j,i)=4 C(2j,2(j-i))=6 inequality holds: True
E2 effective-index classification exact-verified j<=60: mismatches=0
```

**Smallest such pair: (i, j) = (1, 2), n = 4: C(4, 1) = 4 < 6 = C(4, 2).**
At this pair the key inequality C(2j, 2(j−i)) ≤ C(2j, i) ≤ C(n, i) reads
6 ≤ 4 ≤ 4 — false at the first step. (Concretely: V_1(4) = 4, gcd(4,
C(4,2)) = 2 > 1, so (4, 1, 2) is not a counterexample to #699; it is a
counterexample to the claim that *this chain of inequalities* disposes of
n = 2j.) There are 53,200 such chain-failure pairs with j ≤ 400. Hence:
the problem page's assertion (recorded in Phase 0, Item 1) that the GPT
proof covers "j ≤ 3i/2 **OR n = 2j**" is **not supported by the exposited
argument**; the n = 2j half needs a genuinely different proof (plausibly
present in the inaccessible raw claim) and is UNVERIFIABLE from the
exposition. This does not touch the j ≤ 3i/2 region, where n = 2j is
covered as a boundary case (§2.3–2.4).

## 4. Gap classification, step by step

| # | Step of the exposition | Class | Notes |
|---|---|---|---|
| 0 | Reformulation: problem ⟺ "can v be coprime to C(n, j)" | **PROVED** | Prime divisors of v are exactly the primes ≥ i dividing C(n, i); gcd(v, C(n,j)) > 1 iff a common prime ≥ i exists. Holds also at v = 1 (both sides false). Correct **only** under the ≥ convention; under > it is false — §1.3(a), witness (28,5,14). |
| 1 | EEES78 input: v > C(n,i)^{1/2} "with finitely many explicit exceptions" | **GAP** (fillable; filled here) + external citation | The theorem is a legitimate cited input, and the derivation u < v ⟹ v² > C is PROVED (§1.2). But the exposition never names the exceptions and discharges none, while every later step is conditional on (n, i) not being exceptional. As a self-contained proof of the region this is incomplete. Filled: list pinned in §1.1, independently confirmed in §3(C), each exception discharged for all j in §2.7. The raw GPT claim's handling of exceptions is UNVERIFIABLE (403). |
| 2 | Identity C(n,i)·C(n−i,j−i) = C(n,j)·C(j,i) | **PROVED** | Standard double count; also inside the 1,113,775-triple numerical umbrella of §3(a) (Phase 0 verified it separately to n ≤ 240). |
| 3 | Key lemma: d \| C(n,i), gcd(d, C(n,j)) = 1 ⟹ d \| C(j,i) | **PROVED** | Euclid/Bezout from Step 2. Strong form verified computationally, §3(a). |
| 4 | v \| C(j,i) = C(j, j−i), hence v ≤ C(j, j−i), v² ≤ C(j,j−i)² | **PROVED** | Divisibility of positive integers; binomial symmetry. |
| 5 | Vandermonde equality Σ_k C(j,k)C(j,2(j−i)−k) = C(2j, 2(j−i)) | **PROVED** | Standard identity, correctly applied. |
| 6 | Strictness C(j,j−i)² < Σ_k … | **GAP** (presentational; fillable; filled here) | Asserted without comment in the exposition. Filled: the sum always has ≥ 3 positive terms (§3(b)(i)); verified numerically to j ≤ 1000 with minimum ratio 1.5. Not a logical error, but Phase 0's "presentational omission" grading is the right one and the fix belongs in the text, since §3(d) shows the boundary case spends exactly this strictness. |
| 7 | Combination: counterexample ⟹ C(n, i) < C(2j, 2(j−i)) | **PROVED** (conditional on Step 1's non-exception hypothesis) | v² > C(n,i) and v² < C(2j,2(j−i)). |
| 8 | "Only finitely many bad n for fixed i < j" | **PROVED** | C(·, i) strictly increasing; not needed for the region. (Per-pair finiteness only — Phase 0's scope correction stands.) |
| 9a | Final chain: 2(j−i) ≤ i from j ≤ 3i/2 | **PROVED** | Pure integer arithmetic; boundary included. |
| 9b | C(2j, 2(j−i)) ≤ C(2j, i) | **GAP** (presentational; fillable; filled here) | The exposition does not mention that C(2j, ·) is nondecreasing on [0, j]. Filled: C(2j,k+1)/C(2j,k) = (2j−k)/(k+1) > 1 for k < j, applied from k = 2(j−i) to i, both ≤ j. Equality at j = 3i/2 is harmless (§2.3). |
| 9c | C(2j, i) ≤ C(n, i) | **GAP** (presentational; fillable; filled here) | Uses 2j ≤ n and monotonicity of C(·, i) in the top argument: C(m+1,i)/C(m,i) = (m+1)/(m+1−i) > 1. Equality at n = 2j harmless. |
| 10 | (Page-level, not in the exposition) coverage of **n = 2j** for j > 3i/2 | **UNVERIFIABLE / not proved; ERROR if attributed to this chain** | No argument in the exposition addresses it; the exposited chain demonstrably fails there, smallest (i, j) = (1, 2), §3(e). The statement itself tested true for all j ≤ 400 (79,800 pairs). |

No step of the region argument is classified ERROR. No step rests on the
inaccessible raw claim except the attribution itself; every mathematical
input beyond EEES78 is elementary and is either in the text or supplied
above.

## 5. Summary for the record

- **ERRORs found:** none in the j ≤ 3i/2 deduction. One ERROR of
  *coverage* at page level: the exposited argument does not prove the
  n = 2j case outside the region, contrary to what a reader would infer
  from the page's "j ≤ 3i/2 OR n = 2j" assertion; smallest witness
  (i, j) = (1, 2) with C(4,1) = 4 < 6 = C(4,2).
- **GAPs:** (1) EEES78 exceptions unnamed and undischarged in the
  exposition — material, fillable, filled in §2.7/§3(C) (all 12 pairs
  check out for every admissible j; (9,4) and (10,5) admit no j at all).
  (2) Vandermonde strictness unjustified in the text — filled by the
  ≥ 3 positive terms argument. (3) Both monotonicity steps of the final
  chain unjustified in the text — filled by one-line ratio arguments.
  GAPs (2)–(3) are presentational; GAP (1) is the only one that makes
  the exposition, standing alone, an incomplete proof of the region.
- **Convention audit:** the proof needs, and Bloom uses, v on primes
  **≥ i** with u on primes < i and exactly 12 exceptions. The ≥ vs >
  distinction is load-bearing at exactly two points — the reformulation
  (witness (28, 5, 14): gcd(V_{>5}, C(28,14)) = 1 vs gcd(V_{≥5},
  C(28,14)) = 5) and the EEES78 input (7 pairs with n ≤ 200, smallest
  (9, 3), where the >-convention inequality fails while the ≥ version
  holds; and the > theorem proves only finiteness, so its exceptions
  cannot be discharged at all). The rest of the chain is
  convention-blind.
- **n = 2j finding:** gcd(V_i(2j), C(2j, j)) > 1 verified directly for
  all 79,800 pairs with j ≤ 400 (no failures), but the exposited
  inequality chain fails to yield a contradiction at n = 2j for 53,200
  pairs with j ≤ 400 and j > 3i/2 — smallest (i, j) = (1, 2). The case
  needs a different proof; none is exposited.
- **Overall:** Phase 0's verdict survives an adversarial pass — SOUND
  conditional on EEES78 — with the sharpening that "conditional" must be
  read literally: the exception discharge is part of the proof, it is
  absent from the exposition, and it is supplied in this report (§2.7).
  With §2.7 and the three filled presentational gaps, the region
  j ≤ 3i/2 is, in my judgement, proved.
