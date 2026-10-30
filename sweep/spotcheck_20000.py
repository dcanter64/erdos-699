#!/usr/bin/env python3
"""
Bounded independent spot check for the cap-20000 sweep (hourly check 8,
2026-10-29): direct-gcd verification of a seeded random sample of 300
open-region triples with n in (10000, 20000].

For each triple (n, i, j) with 1 <= i < j <= n//2 and 2j > 3i:
  v = V_i(n) = product over primes p >= i of p^{v_p(C(n,i))}
      (exponents by Legendre's formula, exact bigint arithmetic)
  check gcd(v, C(n, j)) > 1   (gcd == 1 would be a counterexample)
Seed: 20261029 (deterministic).
"""
import json
import random
import sys
import time
from math import comb, gcd, isqrt


def primes_upto(n):
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False
    for p in range(2, isqrt(n) + 1):
        if sieve[p]:
            sieve[p * p:n + 1:p] = [False] * len(range(p * p, n + 1, p))
    return [p for p, ok in enumerate(sieve) if ok]


PRIMES = primes_upto(20000)


def vp_binom(n, k, p):
    e = 0
    pp = p
    while pp <= n:
        e += n // pp - k // pp - (n - k) // pp
        if pp > n // p:
            break
        pp *= p
    return e


def V_i(n, i):
    v = 1
    for p in PRIMES:
        if p > n:
            break
        if p >= i:
            e = vp_binom(n, i, p)
            if e:
                v *= p ** e
    return v


def main():
    rng = random.Random(20261029)
    t0 = time.time()
    checked = 0
    coprime = []
    min_gcd = None
    while checked < 300:
        n = rng.randint(10001, 20000)
        half = n // 2
        # i must admit at least one open-region j
        i = rng.randint(1, half - 1)
        start = max(i + 1, (3 * i) // 2 + 1)
        if start > half:
            continue
        j = rng.randint(start, half)
        assert 1 <= i < j <= half and 2 * j > 3 * i
        v = V_i(n, i)
        g = gcd(v, comb(n, j))
        if min_gcd is None or g < min_gcd:
            min_gcd = g
        if g == 1:
            coprime.append([n, i, j])
        checked += 1
        if checked % 50 == 0:
            print(f"{checked}/300 checked, elapsed {time.time()-t0:.0f}s, coprime so far: {len(coprime)}", flush=True)
    result = {
        "seed": 20261029,
        "sample_size": checked,
        "n_range": [10001, 20000],
        "region": "1 <= i < j <= n//2 and 2j > 3i (open region)",
        "method": "direct gcd(V_i(n), C(n,j)); V_i via Legendre exponents, exact bigint",
        "coprime_triples_found": coprime,
        "all_gcd_gt_1": len(coprime) == 0,
        "runtime_s": round(time.time() - t0, 2),
    }
    with open("spotcheck_20000.json", "w") as f:
        json.dump(result, f, indent=2)
    print(json.dumps(result, indent=2))
    return 0 if not coprime else 1


if __name__ == "__main__":
    sys.exit(main())
