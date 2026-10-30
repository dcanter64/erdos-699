#!/usr/bin/env python3
"""
Independent checker for Erdos #699 Stage 2.

Implemented separately from sweep.py: NO bitmask machinery, NO Legendre
formula. For each triple it computes C(n,i) and C(n,j) with math.comb,
extracts V_i(n) by physically dividing all prime factors < i out of
C(n,i) (trial division by sieved primes), and takes math.gcd.

Tasks:
  1. Discharge the 12 EEES78 exception pairs: for each (n0, i0), check
     ALL i0 < j <= n0/2 directly (both regions).
  2. Brute-force re-verify a seeded random sample of FULLY CLEARED
     pairs from pairpass.json over their complete intervals [2j, N(i,j)],
     with N(i,j) recomputed here by exact binary search (no lgamma).
  3. Seeded random sample of triples from the swept open region
     (n <= 10000), checked directly.
  4. Seeded random sample of triples from the CLOSED region j <= 3i/2
     (empirical spot-check of the proved region; not a coverage claim).

Any gcd == 1 anywhere is a counterexample candidate and is reported.
"""
import json
import os
import random
import sys
import time
from math import comb, gcd

HERE = os.path.dirname(os.path.abspath(__file__))
NSTAR = 10000
EXCEPTIONS = [(8, 3), (9, 4), (10, 5), (12, 5), (21, 7), (21, 8),
              (30, 7), (33, 13), (33, 14), (36, 13), (36, 17), (56, 13)]


def primes_upto(n):
    sieve = [True] * (n + 1)
    sieve[0:2] = [False, False]
    for p in range(2, int(n ** 0.5) + 1):
        if sieve[p]:
            sieve[p * p::p] = [False] * len(range(p * p, n + 1, p))
    return [p for p, ok in enumerate(sieve) if ok]


PRIMES = primes_upto(NSTAR)


def V_direct(n, i):
    """V_i(n) by computing C(n,i) and dividing out every prime < i."""
    x = comb(n, i)
    for p in PRIMES:
        if p >= i:
            break
        while x % p == 0:
            x //= p
    return x


def triple_ok(n, i, j, v=None):
    if v is None:
        v = V_direct(n, i)
    return gcd(v, comb(n, j)) > 1


def N_exact(i, j):
    """N(i,j) = max{ n : C(n,i) < C(2j, 2(j-i)) } by pure exact binary
    search over the full domain (independent of pairpass).

    Correct for ALL i < j, including closed-region pairs where
    N(i,j) < 2j. Fixed 2026-10-28 (review finding M1): the original
    search started at lo = 2j and assumed C(2j, i) < B, returning
    2j - 1 unconditionally when that failed, which is wrong outside
    the open region (e.g. (3, 4) gave 7 for true N = 6). The search
    now starts at lo = i, where C(i, i) = 1 < B always (B >= 6 for
    i < j), so the invariant C(lo, i) < B <= C(hi, i) holds in every
    case and the downward pinning is exact. On open-region pairs the
    returned values are unchanged (verified against pairpass.N_of).
    """
    B = comb(2 * j, 2 * (j - i))
    lo = i
    hi = max(2 * j, i + 1)
    while comb(hi, i) < B:
        hi *= 2
    while lo + 1 < hi:
        mid = (lo + hi) // 2
        if comb(mid, i) < B:
            lo = mid
        else:
            hi = mid
    assert comb(lo, i) < B <= comb(lo + 1, i)
    return lo


def main():
    t0 = time.time()
    rng = random.Random(20261028)
    problems = []

    # Task 1: exceptions
    t1 = 0
    for (n0, i0) in EXCEPTIONS:
        v = V_direct(n0, i0)
        for j in range(i0 + 1, n0 // 2 + 1):
            t1 += 1
            if gcd(v, comb(n0, j)) == 1:
                problems.append(("exception", n0, i0, j))
    print(f"Task 1: {len(EXCEPTIONS)} exception pairs, {t1} triples, "
          f"all gcd > 1: {not problems}")

    # Task 2: sample of fully cleared pairs, full intervals
    pp = json.load(open(os.path.join(HERE, "pairpass.json")))
    cleared = []
    for i_s, js in pp["cleared_js_by_i"].items():
        for j in js:
            cleared.append((int(i_s), j))
    rng.shuffle(cleared)
    # Sample pairs whose FULL intervals fit a 40000-triple budget.
    # (Fixed 2026-10-28: the original loop kept scanning the whole
    # 768k-pair list computing N_exact for every pair once the budget
    # was exceeded, an effective hang. Now: examine at most 300 pairs,
    # add a pair only if it fits the budget, stop at 45 pairs.)
    sample, budget, examined = [], 0, 0
    for (i, j) in cleared:
        if len(sample) >= 45 or examined >= 300:
            break
        examined += 1
        nij = N_exact(i, j)
        length = nij - 2 * j + 1
        if sample and budget + length > 40000:
            continue
        sample.append((i, j, nij))
        budget += length
    print(f"Task 2 sampling: examined {examined} cleared pairs, "
          f"selected {len(sample)}, budget {budget} triples", flush=True)
    t2 = 0
    for (i, j, nij) in sample:
        for n in range(2 * j, nij + 1):
            t2 += 1
            if not triple_ok(n, i, j):
                problems.append(("cleared-pair", n, i, j))
    print(f"Task 2: {len(sample)} cleared pairs re-verified over full "
          f"intervals ({t2} triples), all gcd > 1: {not problems}")

    # Task 3: random open-region triples
    t3 = 0
    for _ in range(3000):
        n = rng.randint(4, NSTAR)
        i = rng.randint(1, n // 2)
        lo_j = max(i + 1, (3 * i) // 2 + 1)
        if lo_j > n // 2:
            continue
        j = rng.randint(lo_j, n // 2)
        t3 += 1
        if not triple_ok(n, i, j):
            problems.append(("open-sample", n, i, j))
    print(f"Task 3: {t3} random open-region triples, all gcd > 1: "
          f"{not problems}")

    # Task 4: random closed-region triples
    t4 = 0
    for _ in range(500):
        n = rng.randint(4, NSTAR)
        i = rng.randint(1, n // 2)
        hi_j = min(n // 2, (3 * i) // 2)
        if hi_j <= i:
            continue
        j = rng.randint(i + 1, hi_j)
        t4 += 1
        if not triple_ok(n, i, j):
            problems.append(("closed-sample", n, i, j))
    print(f"Task 4: {t4} random closed-region triples, all gcd > 1: "
          f"{not problems}")

    print(f"PROBLEMS FOUND: {problems}")
    print(f"checker runtime: {time.time() - t0:.0f}s")
    with open(os.path.join(HERE, "checker_results.json"), "w") as f:
        json.dump({"task1_triples": t1, "task2_pairs": len(sample),
                   "task2_triples": t2, "task3_triples": t3,
                   "task4_triples": t4, "problems": problems,
                   "runtime_s": time.time() - t0}, f, indent=2)
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
