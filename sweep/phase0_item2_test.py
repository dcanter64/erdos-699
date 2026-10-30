#!/usr/bin/env python3
"""
Phase 0, Item 2: numerical verification of the finite reduction for Erdos #699.

Claims under test (derivation in PHASE0.md):
  (A) Identity: C(n,i)*C(n-i,j-i) = C(n,j)*C(j,i).
  (B) Lemma (strong form): for v = V_i(n), the part of v coprime to C(n,j),
      i.e. v / gcd(v, C(n,j)) with gcd-part removed prime by prime -- precisely,
      the integer u = prod p^e_p(v) over primes p >= i with p not dividing
      C(n,j) -- divides C(j,i).
  (C) Vandermonde strict bound: C(j, j-i)^2 < C(2j, 2(j-i)) for all i < j.
  (D) EEES78 bound v^2 > C(n,i): collect all (n,i) with n <= NMAX, i <= n/2
      where it FAILS (empirical exception pairs, to cross-check the paper list).
  (E) Reduction consistency: for every triple (n,i,j), i<j<=n/2, whose (n,i)
      is NOT an empirical exception in (D): if gcd(v, C(n,j)) == 1 then
      n <= N(i,j), where N(i,j) = max{n : C(n,i) < C(2j, 2(j-i))}.
      (In practice we expect NO gcd==1 triples at all; this checks the
      implication is never violated and reports any gcd==1 triple found.)
  (F) Closure consistency: N(i,j) < 2j whenever j <= 3i/2 (the AI-proof case).
  (G) Brief's example: N(10,19) should be ~51.

All arithmetic is exact (Python bigints), exponents via Legendre's formula.
"""
import sys
from math import comb, gcd, isqrt

NMAX = 240  # brute-force n range


def primes_upto(n):
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False
    for p in range(2, isqrt(n) + 1):
        if sieve[p]:
            step = p
            start = p * p
            sieve[start:n + 1:step] = [False] * len(range(start, n + 1, step))
    return [p for p, ok in enumerate(sieve) if ok]


PRIMES = primes_upto(NMAX)


def vp_binom(n, k, p):
    """Exponent of prime p in C(n,k), Legendre's formula."""
    e = 0
    pp = p
    while pp <= n:
        e += n // pp - k // pp - (n - k) // pp
        if pp > n // p:
            break
        pp *= p
    return e


def V_i(n, i):
    """Part of C(n,i) supported on primes >= i."""
    v = 1
    for p in PRIMES:
        if p > n:
            break
        if p >= i:
            e = vp_binom(n, i, p)
            if e:
                v *= p ** e
    return v


def N_of(i, j):
    """max n with C(n,i) < C(2j, 2(j-i)); -1 if even n=i fails (never)."""
    bound = comb(2 * j, 2 * (j - i))
    n = i
    # C(n,i) is strictly increasing in n; walk up (intervals are short).
    while comb(n + 1, i) < bound:
        n += 1
    return n


def main():
    failures = []
    exceptions = []          # (n, i) with v^2 <= C(n,i)
    coprime_triples = []     # gcd(v, C(n,j)) == 1  (counterexamples!)
    checked = 0

    # (C) Vandermonde strict bound, pure binomial check to generous range
    for j in range(2, 601):
        for i in range(1, j):
            if not comb(j, j - i) ** 2 < comb(2 * j, 2 * (j - i)):
                failures.append(("C", i, j))
    print("(C) Vandermonde strict bound checked for i<j<=600: "
          + ("OK" if not any(f[0] == 'C' for f in failures) else "FAILED"))

    # (G) brief example
    n1019 = N_of(10, 19)
    print(f"(G) N(10,19) = {n1019}  (brief says n in [38, ~51])")

    # (F) closure consistency for i up to 300
    bad_f = [(i, j) for i in range(1, 301) for j in range(i + 1, 601)
             if 2 * j <= 3 * i and N_of(i, j) >= 2 * j]
    print("(F) N(i,j) < 2j for all j <= 3i/2, i<=300: "
          + ("OK" if not bad_f else f"FAILED {bad_f[:5]}"))
    if bad_f:
        failures.append(("F", bad_f[:5]))

    # (D) empirical EEES78 exceptions, n <= NMAX
    vcache = {}
    for n in range(2, NMAX + 1):
        for i in range(1, n // 2 + 1):
            v = V_i(n, i)
            vcache[(n, i)] = v
            if v * v <= comb(n, i):
                exceptions.append((n, i))
    print(f"(D) empirical EEES78 exceptions (v^2 <= C(n,i)), n<={NMAX}: "
          f"{exceptions}")

    exc_set = set(exceptions)

    # (A), (B), (E): full triple sweep
    for n in range(2, NMAX + 1):
        for i in range(1, n // 2 + 1):
            v = vcache[(n, i)]
            ci = comb(n, i)
            for j in range(i + 1, n // 2 + 1):
                cj = comb(n, j)
                checked += 1
                # (A) identity
                if ci * comb(n - i, j - i) != cj * comb(j, i):
                    failures.append(("A", n, i, j))
                # (B) the part of v coprime to cj divides C(j,i)
                u = v
                g = gcd(u, cj)
                # remove from u every prime factor shared with cj, fully
                gg = g
                for p in PRIMES:
                    if p > gg:
                        break
                    while gg % p == 0:
                        gg //= p
                        # divide out p^e from u down to the exponent in v
                        # coprime part: remove ALL p if p | cj
                        while u % p == 0:
                            u //= p
                if comb(j, i) % u != 0:
                    failures.append(("B", n, i, j))
                # (E) coprimality -> must lie in reduction interval (unless exc)
                if gcd(v, cj) == 1:
                    coprime_triples.append((n, i, j))
                    if (n, i) not in exc_set and n > N_of(i, j):
                        failures.append(("E", n, i, j))
    print(f"triples checked: {checked}")
    print(f"(E) gcd==1 triples found (counterexample candidates): "
          f"{coprime_triples}")
    print(f"failures: {failures[:20]}{' ...' if len(failures) > 20 else ''} "
          f"(total {len(failures)})")
    return 0 if not failures and not coprime_triples else 1


if __name__ == "__main__":
    sys.exit(main())
