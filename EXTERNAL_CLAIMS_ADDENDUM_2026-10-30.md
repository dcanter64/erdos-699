# External claims addendum, 2026-10-30: the Plasma AI claim (erdosproblems.ai catalog)

Supplement to EXTERNAL_CLAIMS_2026-10-29.md, which graded the record
on erdosproblems.com. This claim does not appear there. It is
recorded in the independent catalog at erdosproblems.ai, in that
catalog's repository: github.com/plasma-ai/erdos, file
wiki/problems/factorials_binomials/E0699/claims/2026_10_19_plasma_ai.md
(read in full 2026-10-30). Graded by the same standard as the
earlier file: the claim is stated exactly, its standing is taken
from its own record, and nothing here is verified by this campaign.

## The claim as recorded

Title: "A common prime at index seven and at every index from
nine". Author: Plasma AI. Published 2026-10-19. Catalog fields:
status claimed, claim proved, scope partial, author-recorded at
tier 0, catalog acceptance pending.

A triple 1 <= i < j <= n/2 is called bad when no prime p >= i
divides both C(n,i) and C(n,j). The claim states:

1. No bad triple has i = 7 or i >= 9: for every such i, some prime
p >= i divides both binomial coefficients, for all j and n.
2. At i = 3, no bad triple has n <= 10^19, or v2(n) <= 48, or n
even with (n-2)/2 divisible by at most two distinct primes.
Equivalently, a bad triple at i = 3 would need n > 10^19,
v2(n) >= 49, and at least three distinct prime factors of (n-2)/2.

Both items are described as computer-assisted. The indices 4, 5, 6,
and 8 are explicitly not covered, the indices 1 and 2 are credited
to Van Doorn and Rocca and not claimed, and the problem is stated
to remain open. A conditional remark (assuming the abc conjecture,
only finitely many bad triples have i = 3) is included in the
source but expressly excluded from the claim itself, and is
recorded here only for completeness.

## Stated dependencies

Item 1 builds on Van Doorn and Rocca's two unpublished 2026
manuscripts: the Kummer localisation to the triangle r + s < i, the
fat-point divisor, and the orbit polynomial with its Jacobi
discriminant from the first, and Lemma 1 of the second, through a
repository deduction that supplies the cutoff the manuscript states
without its calculation (i >= 1000) and lowers it to i >= 906. The
cofactor estimates build on the Pade construction of Bennett,
Filaseta and Trifonov, and the proofs use explicit prime estimates
and the prime-gap computation of Oliveira e Silva, Herzog and
Pardi. The proofs at i = 7 and at 9 <= i <= 905, and the i = 3
results, are Plasma AI's own.

## Standing and grading

UNVERIFIED, at the lowest recorded tier. The claim's own standing
note states: author-recorded at tier 0; no independent review of
the repository deductions is retained; the checkers and certificates
are author evidence and confer no tier; no Lean formalisation is
asserted; and the underlying manuscripts' proofs "count as not
verified, so item 1 rests on unverified premises". Nothing in this
addendum changes that grading. Verification would require review
of the claim's linked proof guide and detail pages and an
independent run or audit of its retained checkers; none of that
has been attempted by this campaign.

## Interaction with this campaign's certified record

No statement in this repository is contradicted by the claim,
because every statement here is scoped to what this campaign itself
certified, with dependencies named. The coverage is complementary:

- Where this campaign's in-scope clearing (i <= 1000, j <= 5000)
  leaves 330,194 partial pairs, all in rows 4 <= i <= 113 above
  certified frontiers, the Plasma claim, if it holds, closes i = 7
  and every i >= 9 outright, while expressly leaving i in
  {4, 5, 6, 8} open. The two records agree that the low rows are
  the hard core.
- At i = 3 this campaign's certified residual (CYCLE3.md) is:
  n even, n > 10^8, j >= 50,001, T >= 17, satisfying (RES-3). The
  Plasma claim, if it holds, is far stronger on the n axis (no bad
  triple at all with n <= 10^19, against this campaign's certified
  zero-survivor search at even n <= 10^8) and would further force
  v2(n) >= 49, that is, 2^49 dividing n, which excludes most of
  the residue classes this campaign's exact v2 characterisation
  (CYCLE3.md, Cluster J) leaves open. Both statements can hold
  together; the conjunction would narrow the i = 3 residual
  considerably. Until the Plasma claim is independently reviewed,
  the certified residual of record remains the one in CYCLE3.md.

Recorded 2026-10-30. This addendum is part of the literature
record, not of the results: it asserts nothing about #699 beyond
what the cited claim itself asserts.
