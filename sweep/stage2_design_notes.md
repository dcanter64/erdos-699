> **SUPERSEDED (2026-10-28, review finding L7).** This planning
> draft describes a different method (per-prime Legendre checks,
> Bertrand pre-filter) and a different coverage currency than what
> was actually implemented. The implemented method is the bitmask
> sweep in sweep.py; the authoritative record is RESULTS.md. This
> file is retained for history only and must not be cited as a
> description of the computation.

# Stage 2 design notes (drafted during Phase 0; NOT a sweep, no open-region code run)

Scope decision forced by the Item 2 scope correction:
- Pairs (i,j) in the open region are infinite in number for fixed i.
- Stage 2 will therefore report in two currencies:
  (1) FULLY CLEARED PAIRS: all (i,j), j > 3i/2, i <= 1000, with N(i,j) <= N*
      whose entire interval [2j, N(i,j)] is checked, plus all (i,j) with
      N(i,j) < 2j (empty interval, automatic).
  (2) N-COVERAGE: all triples (n,i,j) with n <= N*, i <= min(1000, n/2),
      3i/2 < j <= n/2, n <= N(i,j) checked directly.
- N* to be set from measured per-triple throughput (target: hours, 2 cores).

Per-triple check cost control (planned):
- Work prime by prime over p >= i using Legendre exponents of C(n,i) and
  C(n,j); exit on first p with both exponents > 0.
- Cheap pre-filter: Bertrand prime p in (n/2, n]: p | C(n,k) iff k > n - p
  (for k <= n/2). If i > n - p then p divides C(n,j) too whenever
  j > n - p (automatic since j > i), DONE instantly.
  More generally test large primes first: primes p in (n/3, n/2], (n/4, n/3]...
  via exponent = floor(n/p) - floor(i/p) - floor((n-i)/p) (single term when
  p > n/2 for the squares... general Legendre sum is short for p > sqrt(n)).
- EEES78 exception pairs (n0, i0): check ALL j (both regions) directly by
  brute force gcd on the exact integers.

Independent checker (separately implemented):
- Recomputes any claimed coprime triple from factorials/Legendre directly.
- Re-derives cleared intervals for a random sample of (i,j) by pure
  brute-force gcd over the full interval, without the sweep's pruning.
