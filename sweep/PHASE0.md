# Erdős Problem #699 — Phase 0 Gate Record

Workspace: ~/workspace/math-hunt/erdos-699/
Date: 2026-10-28
Status: COMPLETE — GATE VERDICT: PASS (see bottom; caveats recorded in Items 3 and 5)

Problem (to be confirmed verbatim in Item 1): for i < j ≤ n/2, let
V_i(n) be the part of C(n,i) supported on primes ≥ i. Conjecture:
gcd(V_i(n), C(n,j)) > 1 always.
Page: https://www.erdosproblems.com/699 (Bloom exposition, edited 27 Aug 2026).

---

## Item 2 — The finite reduction: derivation and numerical verification

### Derivation

Fix i < j ≤ n/2 and suppose (n, i, j) is a counterexample:
gcd(v, C(n,j)) = 1, where v = V_i(n). Assume (n,i) is NOT one of the
finitely many EEES78 exception pairs, so that

    (EEES78)   v > C(n,i)^{1/2},  i.e.  v^2 > C(n,i).

Step 1 (identity). C(n,i)·C(n-i, j-i) = C(n,j)·C(j,i). (Both sides count
the ways to choose an i-subset and then a disjoint (j-i)-subset of [n].)

Step 2 (key lemma). If d | C(n,i) and gcd(d, C(n,j)) = 1, then d | C(j,i).
Proof: d | C(n,i)·C(n-i, j-i) = C(n,j)·C(j,i) by Step 1, and
gcd(d, C(n,j)) = 1, so d | C(j,i) by Euclid's lemma. ∎

Step 3. Apply Step 2 with d = v (v | C(n,i) by definition, and
gcd(v, C(n,j)) = 1 by assumption): v | C(j,i) = C(j, j-i), hence
v ≤ C(j, j-i) and v^2 ≤ C(j, j-i)^2.

Step 4 (Vandermonde, strict). C(2j, 2(j-i)) = Σ_k C(j,k)·C(j, 2(j-i)-k).
The term k = j-i equals C(j, j-i)^2. The number of k giving a positive
term is 2(j-i)+1 ≥ 3 when 2(j-i) ≤ j, and 2i+1 ≥ 3 when 2(j-i) > j;
either way there are at least 3 positive terms, so
C(j, j-i)^2 < C(2j, 2(j-i)).

Step 5 (conclusion). v^2 > C(n,i) (EEES78) and v^2 < C(2j, 2(j-i))
(Steps 3-4) give

    C(n,i) < C(2j, 2(j-i)).

Since C(n,i) is strictly increasing in n for n ≥ i, define

    N(i,j) := max{ n : C(n,i) < C(2j, 2(j-i)) }   (computable by search).

Then any counterexample with (n,i) not an EEES78 exception satisfies
2j ≤ n ≤ N(i,j). Only the finite interval [2j, N(i,j)] needs checking
for each (i,j). ∎

Corollary (the j ≤ 3i/2 case, cf. Item 3): if j ≤ 3i/2 then 2(j-i) ≤ i ≤ j,
so C(2j, 2(j-i)) ≤ C(2j, i) ≤ C(n, i) (using 2j ≤ n), contradicting
Step 5. Hence N(i,j) < 2j: the interval is empty.

### Numerical verification (phase0_item2_test.py, exact arithmetic, Legendre exponents)

- Identity (A): verified on all 568,820 triples (n,i,j), i<j≤n/2, n ≤ 240. OK.
- Lemma, strong form (B): for every triple, the part of v coprime to
  C(n,j) divides C(j,i). Verified on all 568,820 triples. OK.
- Vandermonde strict bound (C): C(j, j-i)^2 < C(2j, 2(j-i)) verified for
  all i < j ≤ 600. OK.
- Closure consistency (F): N(i,j) < 2j for all j ≤ 3i/2, i ≤ 300. OK.
- Counterexample scan (E): gcd(V_i(n), C(n,j)) computed directly for all
  568,820 triples with n ≤ 240. ZERO coprime triples. No violation of
  the reduction implication.
- Worked example (G): N(10,19) = 55 exactly (C(55,10) = 29,248,649,430
  < C(38,18) = 33,578,000,610 ≤ C(56,10) = 35,607,051,480). The scouting
  brief's "~51" was an underestimate; the true interval for (10,19) is
  n ∈ [38, 55].
- Empirical EEES78 exceptions (D): the pairs (n,i), i ≤ n/2, n ≤ 240,
  where v^2 ≤ C(n,i) FAILS to exceed, are exactly:
  (8,3), (9,4), (10,5), (12,5), (21,7), (21,8), (30,7), (33,13),
  (33,14), (36,13), (36,17), (56,13).
  (To be cross-checked against the published EEES78 list under Item 4;
  any published exception with n > 240 is outside this scan's reach and
  must come from the paper.)

### Scope correction to the scouting brief (material)

The reduction is finite PER PAIR (i,j), not finite over the region
{i ≤ 1000, j > 3i/2}. For fixed i, every sufficiently large j has a
nonempty interval: e.g. for i = 1, N(1,j) ≈ 2j^2 (j=10 → N=189), and
for i = 10: N(10,100) = 2,385, N(10,1000) = 260,190. So the set of
pairs to check is infinite, and Stage 2 must adopt an explicit finite
scope (see Stage 2 scoping note in the final report): pairs are "fully
cleared" only when their whole interval [2j, N(i,j)] has been checked;
all other coverage is reported as "no counterexample with n ≤ N*" for
an explicit N*. The brief's phrase "explicit, small checklist" is
accurate only near the diagonal j ≈ 3i/2.

---

## Item 3 — Referee assessment of the claimed j ≤ 3i/2 closure

Source refereed: the exposition by Thomas Bloom hosted on the problem
page (fetched 2026-10-28), which states it is an exposition of a proof
provided by GPT 5.6 Sol (prompted by Liam Price) in a proof claim.
The exposition text was fully readable and appears complete (it ends
with the contradiction). The ORIGINAL proof-claim text by GPT 5.6 Sol
was NOT accessible (the proof-claims section could not be fetched; see
Item 5), so this assessment referees Bloom's exposition of the proof,
which Bloom states is his own mini-exposition of it. If the raw claim
contains steps beyond the exposition, they are unrefereed by us; the
exposited argument, however, is self-contained and complete.

Argument, restated:
1. The problem is equivalent to asking whether v = V_i(n) can be
   coprime to C(n,j) (i<j≤n/2). [Definitional.]
2. EEES78 input: v > C(n,i)^{1/2}, with finitely many explicit
   exceptions. [External hypothesis.]
3. From C(n,i)C(n-i,j-i) = C(n,j)C(j,i): if d | C(n,i) is coprime to
   C(n,j), then d | C(j,i).
4. Hence if v is coprime to C(n,j), then v | C(j, j-i), so
   v^2 ≤ C(j, j-i)^2 < Σ_k C(j,k)C(j, 2(j-i)-k) = C(2j, 2(j-i))
   (Vandermonde), and with (2): C(n,i) < C(2j, 2(j-i)).
5. If j ≤ 3i/2, then 2(j-i) ≤ i < j ≤ n/2, so
   C(2j, 2(j-i)) ≤ C(2j, i) ≤ C(n, i): contradiction.

Step-by-step check:
- Step 3: Sound. d | C(n,i) ⟹ d | C(n,j)·C(j,i) via the identity, and
  gcd(d, C(n,j)) = 1 forces d | C(j,i) (Euclid). Independently verified
  numerically in strong form (Item 2, test B).
- Step 4, first inequality: v | C(j, j-i) with both sides positive
  integers gives v ≤ C(j, j-i). Sound.
- Step 4, strict inequality: C(j, j-i)^2 is the k = j-i term of the
  Vandermonde sum. The exposition asserts strictness without comment;
  it holds because the sum always has at least 3 positive terms
  (2(j-i)+1 ≥ 3 if 2(j-i) ≤ j; 2i+1 ≥ 3 if 2(j-i) > j). Presentational
  omission, not a logical gap; verified numerically (Item 2, test C).
- Step 4, combination with EEES78: v^2 > C(n,i) and v^2 < C(2j, 2(j-i))
  give C(n,i) < C(2j, 2(j-i)). Sound, conditional on EEES78.
- Step 5: 2(j-i) ≤ i is exactly j ≤ 3i/2. C(2j, ·) is nondecreasing on
  [0, j] and 2(j-i) ≤ i ≤ j gives C(2j, 2(j-i)) ≤ C(2j, i); 2j ≤ n and
  monotonicity of C(·, i) give C(2j, i) ≤ C(n, i). Chain contradicts
  Step 4. Sound, including the boundary j = 3i/2 and 2j = n (the strict
  inequality from Step 4 does the work). Consistency also verified
  numerically: N(i,j) < 2j for all j ≤ 3i/2 with i ≤ 300 (Item 2, F).

Caveat (structural, applies to the whole approach): every step after
Step 2 is conditional on (n,i) NOT being an EEES78 exception. For an
exception pair (n0, i0), this proof closes NEITHER region; all
i0 < j ≤ n0/2 must be checked directly. The exception pairs within
n ≤ 240 (Item 2, test D) were covered by the brute-force scan and
yielded no coprime triple; the authoritative full list is Item 4's
deliverable, and the gate verdict depends on discharging it.

VERDICT: SOUND (conditional on EEES78, with its exception pairs to be
discharged by direct computation). The deduction has no logical gap;
the only unproved input is EEES78 itself, which the proof cites
explicitly. Consequence for later claims: a completed sweep of the
j > 3i/2 region, together with this proof and a direct check of all
EEES78 exception pairs, would justify "the conjecture holds for all
checked regions with no exceptions outstanding" — and, since the three
pieces (j ≤ 3i/2 proof; j > 3i/2 finite check per pair; exception
pairs) exhaust all cases each pair (i,j) can be fully cleared only
pair by pair (see the Item 2 scope correction).

---

## Item 1 — Statement and quantifiers

Source: the complete #699 entry as rendered by the site itself
(https://www.erdosproblems.com/prizes/0 crawl of the #699 entry,
2026-10-28; the dedicated /699 page fetch returns the exposition
section). The dedicated "View the LaTeX source" view was not directly
readable through available routes; the TeX below is preserved verbatim
in the site's own rendered entry. The GitHub metadata repository
(teorth/erdosproblems, data/problems.yaml) carries status only:
state "falsifiable", formalised statement "yes" (2026-01-04).

Formal statement, verbatim:

    Is it true that for every $1\leq i<j\leq n/2$ there exists some
    prime $p\geq i$ such that $p\mid \textrm{gcd}\left(\binom{n}{i},
    \binom{n}{j}\right)$?

Attribution on the page: "A problem of Erdős and Szekeres." The page
also records the Sylvester–Schur input (for 1 ≤ i ≤ n/2 some prime
p > i divides C(n,i)).

Discrepancies with the scouting brief, recorded:
1. The formal statement carries the explicit lower bound 1 ≤ i, which
   the brief's summary omitted. No mathematical effect.
2. The formal statement is NOT phrased via V_i(n): it asks for a common
   prime divisor p ≥ i of C(n,i) and C(n,j). The V_i(n) formulation is
   Bloom's exposition reformulation. The two are equivalent: the prime
   divisors of V_i(n) are exactly the primes ≥ i dividing C(n,i), so
   gcd(V_i(n), C(n,j)) > 1 iff such a prime exists. No mathematical
   effect, but the record should be accurate about which is the
   statement and which is the reformulation.
3. The "counterexamples" mentioned on the page concern ONLY the
   strengthened variant with p > i replacing p ≥ i (e.g. i=5, j=14,
   n=28: gcd = 2^3·3^3·5, which satisfies p ≥ i via p=5). They are NOT
   counterexamples to Problem #699. Flagged to prevent misreading.
4. The page's main text asserts GPT 5.6 (prompted by Price) proved the
   statement "if j ≤ 3i/2 OR n = 2j". The n = 2j case is asserted but
   NOT proved in the readable exposition (see Items 3 and 5). It is
   immaterial to the sweep: n = 2j is the left endpoint of every
   interval [2j, N(i,j)] and is checked directly by the sweep anyway.
5. Edit dates on the site differ (main page "last edited 19 July 2026";
   exposition "last edited 27 Aug 2026"); not further reconcilable from
   readable material, and immaterial.

Item 1 verdict: SOLID. The statement and quantifier ranges are
confirmed: 1 ≤ i < j ≤ n/2, prime p ≥ i, equivalence with the
gcd(V_i(n), C(n,j)) > 1 formulation verified.

## Item 4 — EEES78 exception list

Paper identified and verified: E. F. Ecklund, Jr., R. B. Eggleton,
P. Erdös, J. L. Selfridge, "On the prime factorization of binomial
coefficients", Journal of the Australian Mathematical Society,
Series A, 26(3) (November 1978), 257–269.
(Cambridge Core article page.)

Theorem (abstract, verbatim): "For positive integers n and k, with
n ≥ 2k, let C(n,k) = uv, where each prime factor of u is less than k,
and each prime factor of v is at least equal to k. It is shown that
u < v holds with just 12 exceptions, which are determined."

So with Bloom's convention (v = part on primes ≥ k = V_k(n)),
u < v ⟺ V_k(n) > C(n,k)^{1/2}, and the exceptions are the cases u > v.
The 12 exception pairs (n, k), in the paper's order:

    (8,3), (9,4), (10,5), (12,5), (21,7), (21,8), (30,7),
    (33,13), (33,14), (36,13), (36,17), (56,13)

Provenance: the list was recovered from a scan of the paper
(pp. 258–259) whose OCR garbles stacked binomials, corroborated by
Erdős's own restatement (Acta Math. Acad. Sci. Hungar. 33 (1979),
p. 75), and by Shorey–Tijdeman's secondary account ("exactly 12 pairs
(x,k), explicitly given, with u > v").

INDEPENDENT CROSS-CHECK (strong): the 12 pairs above agree EXACTLY
with two independent computations: (a) this project's own scan in
Item 2 (all (n,i), i ≤ n/2, n ≤ 240, where V_i(n)^2 ≤ C(n,i)) produced
precisely these 12 pairs and no others; (b) the research agent's
independent enumeration to n ≤ 400 produced precisely these 12.
Since the paper's theorem asserts there are exactly 12 exceptions in
total, and all 12 have n ≤ 56, the list is complete, not truncated.

Caution recorded: the same paper treats the OTHER convention (U on
primes ≤ k, V on primes > k) and finds 19 cases with only finiteness
proved plus a conjecture. That is not Bloom's convention and not the
input to #699; it must not be substituted.

Consequence for the sweep: each exception pair (n0, i0) is discharged
by checking gcd(V_{i0}(n0), C(n0, j)) directly for ALL
i0 < j ≤ n0/2 (both regions). All n0 ≤ 56, so this is trivial
computationally. (Already covered incidentally by the Item 2 brute
force, n ≤ 240, which found no coprime triple at any exception pair;
Stage 2 re-discharges them explicitly with the independent checker.)

Item 4 verdict: SOLID. Exception list obtained verbatim, provenance
documented, and independently confirmed by computation.

## Item 5 — Incumbent check

What was checked (2026-10-28): the full #699 entry (statement,
discussion, exposition, counts, reactions), the Site Announcements
thread, the GitHub metadata repository, and off-site web searches
(arXiv-targeted, MathOverflow-targeted, general, and "V_i(n)"
phrasings, including September/October 2026 date filters).

Findings:
- Page counts: Comments (9), Proof claims (2), Proof expositions (1).
- Reactions list three users as "Currently working on" the problem
  (conglu, Woett, ster), with no topic, region, or method specified in
  any readable material.
- The only claimed progress anywhere readable is the GPT 5.6 / Price
  proof for j ≤ 3i/2 (exposited) and the asserted n = 2j case. Nothing
  in any readable or indexed material announces, claims, or publishes
  work on the general j > 3i/2 region: no sweep of the finite
  intervals, no counterexample, no extension, at any date, on-site or
  off-site. Bloom's own announcement describes the #699 material only
  as a write-up of the existing GPT/Price proof. An independent queue
  site (proofs.charliekrug.com) lists #699 with "0 attempts · 0 open
  leads".
- RESIDUAL GAP, recorded honestly: the bodies of the 9 comments and
  2 proof claims were NOT readable through available routes (thread
  fetch returned HTTP 403; contents are not search-indexed). One of
  the 2 proof claims presumably underlies the j ≤ 3i/2 exposition; the
  other may underlie the n = 2j assertion; how they divide coverage,
  and whether any comment discusses j > 3i/2, could not be confirmed
  without a live-browser visit to the page's comments/proof-claims
  sections. The original GPT 5.6 Sol proof-claim text is likewise
  inaccessible; Item 3 therefore referees Bloom's exposition of that
  proof (which Bloom states is his own mini-exposition, originally
  written by him as a comment), not the raw claim.

Item 5 verdict: the j > 3i/2 region is still open in all readable
evidence (official status: "falsifiable"/open), with the single
recorded caveat that the comment/proof-claim bodies could not be
inspected. A live-browser check is the one step that could close this
residual gap definitively.

## GATE VERDICT

PASS.

- Item 1: SOLID (statement and quantifiers confirmed; discrepancies
  with the brief are presentational, recorded above).
- Item 2: SOLID (reduction derived; N(i,j) explicit and computable;
  verified numerically on 568,820 triples with zero failures; the
  brief's example value corrected: N(10,19) = 55, not ~51; scope
  correction recorded: finiteness is per-pair, so Stage 2 uses an
  explicit n-cap and reports pair-clearance separately).
- Item 3: SOUND, conditional on EEES78 (no logical gap found in the
  j ≤ 3i/2 argument as exposited by Bloom; the raw GPT claim text was
  inaccessible, and the proof's EEES78 exceptions are discharged under
  Item 4). Consequence for descriptions: results may be stated as
  "no counterexample exists in [the precisely stated swept region],
  and the complementary region j ≤ 3i/2 is proved (Bloom's exposition
  of the GPT 5.6 Sol / Price argument, refereed sound in Phase 0,
  conditional on EEES78 with its 12 exception pairs checked directly)".
  The phrase "Problem #699 is solved" would additionally require
  clearing the ENTIRE j > 3i/2 region, which is infinite pair-by-pair;
  it is justified pair by pair only for pairs whose full interval was
  checked. Stage 2 reporting must keep this distinction exact.
- Item 4: SOLID (12 exception pairs obtained verbatim and confirmed
  by two independent computations; completeness follows from the
  paper's own theorem).
- Item 5: region still open in all readable evidence; residual
  caveat about unreadable comment bodies recorded.

Stage 2 is authorized on this verdict, with the finite scope defined
in RESULTS.md (n-cap N*, full-interval pair clearance enumerated
exactly, EEES78 exception pairs discharged directly).
