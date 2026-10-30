# Coordinator's independent bounded checks (2026-10-28)

Run by the campaign coordinator directly (Python stdlib, ~25 s total
CPU on a loaded machine), independent of both referees.

1. EEES78 u < v, all (n,k) with n ≤ 400, k ≤ n/2, by direct
   Legendre-exponent computation of V_k(n): the exceptions found are
   EXACTLY the 12 listed pairs: (8,3), (9,4), (10,5), (12,5), (21,7),
   (21,8), (30,7), (33,13), (33,14), (36,13), (36,17), (56,13).
2. Vandermonde strictness C(j,j−i)² < C(2j,2(j−i)) for all i < j ≤ 500:
   0 failures.
3. Corollary sentinel: N(i,j) < 2j at the boundary j = ⌊3i/2⌋ for all
   i ≤ 300: 0 failures. (An apparent flag at (i,j) = (1,2) was a bug
   in the coordinator's first test script, which tested j = i+1
   unconditionally; for i = 1 the closed region is empty since
   j ≤ 3/2 < 2, and (1,2) is an open-region pair with N(1,2) = 5,
   correctly ≥ 2j. Not a failure of the corollary.)
4. Exception discharge re-run: for the 12 exception pairs (n0,i0),
   gcd(V_{i0}(n0), C(n0,j)) computed directly for all i0 < j ≤ n0/2:
   41 triples, 0 with gcd = 1. Matches RESULTS.md Task 1.
5. Full gcd sanity: gcd(V_i(n), C(n,j)) > 1 for all 328,350 triples
   with n ≤ 200 (both regions): 0 violations.
6. n = 2j sentinel: the smallest (i,j) with j > 3i/2 and
   C(2j,i) < C(2j,2(j−i)) is (i,j) = (1,2): C(4,1) = 4 < C(4,2) = 6.
   So at n = 2j the necessary condition for a counterexample is
   satisfiable and the exposited chain gives NO contradiction there:
   the exposition's argument does not cover the n = 2j case asserted
   on the problem page. (The triple (4,1,2) itself is fine:
   gcd(4,6) = 2.) Immaterial to the sweep, which checks n = 2j
   directly as the left endpoint of every interval.
