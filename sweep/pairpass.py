#!/usr/bin/env python3
"""
Pair-clearance pass for Erdos #699 Stage 2.

For every pair (i, j) with 1 <= i <= IMAX, 2j > 3i (open region), and
2j <= NSTAR, compute N(i,j) = max{ n : C(n,i) < C(2j, 2(j-i)) } exactly.
A pair is FULLY CLEARED (given the triple sweep to NSTAR) iff
N(i,j) <= NSTAR; otherwise it is PARTIALLY covered (all its triples
with n <= NSTAR were checked by the sweep).

Method: bracket N(i,j) with lgamma (float), then pin the exact boundary
with exact integer comparisons C(n,i) < B, widening the bracket if the
float estimate was off. The final answer always satisfies
C(N,i) < B <= C(N+1,i) in exact arithmetic.

Output: pairpass_reference.json with counts and the list of cleared
pairs (compressed as, per i, the maximal j with N(i,j) <= NSTAR is NOT
assumed monotone; we store the full cleared set as per-i j-ranges
verified individually, plus any non-monotonicity observed).

WARNING (changed 2026-10-28, review finding M4): this reference
implementation deliberately does NOT write pairpass.json. That file
is the production artifact produced by pairpass_fast.py; earlier
versions of this script silently overwrote it in a slightly different
format. Output now goes to pairpass_reference.json.
"""
import json
import os
import sys
import time
from math import comb, lgamma
from multiprocessing import Pool

HERE = os.path.dirname(os.path.abspath(__file__))
NSTAR = 10000
IMAX = 1000


def logC(n, k):
    if k < 0 or k > n:
        return float("-inf")
    return lgamma(n + 1) - lgamma(k + 1) - lgamma(n - k + 1)


def N_of(i, j):
    B = comb(2 * j, 2 * (j - i))
    logB = logC(2 * j, 2 * (j - i))
    # float bracket: find n with logC(n, i) ~= logB via binary search on floats
    lo, hi = 2 * j, max(2 * j + 1, 4 * j)
    while logC(hi, i) < logB:
        hi *= 2
    while lo + 1 < hi:
        mid = (lo + hi) // 2
        if logC(mid, i) < logB:
            lo = mid
        else:
            hi = mid
    # exact pinning around lo (float search guarantees C(lo,i) approx < B)
    n = lo
    while comb(n + 1, i) < B:
        n += 1
    while comb(n, i) >= B:
        n -= 1
    assert comb(n, i) < B <= comb(n + 1, i)
    return n


def work(i):
    cleared = []
    partial = 0
    considered = 0
    j = (3 * i) // 2 + 1
    while 2 * j <= NSTAR:
        considered += 1
        nij = N_of(i, j)
        if nij <= NSTAR:
            cleared.append(j)
        else:
            partial += 1
        j += 1
    return i, considered, cleared, partial


def main():
    print("pairpass.py: reference (direct N(i,j)) implementation; "
          "writing pairpass_reference.json. The production "
          "pairpass.json is written by pairpass_fast.py and is NOT "
          "touched.", flush=True)
    t0 = time.time()
    results = {}
    total_considered = 0
    total_cleared = 0
    total_partial = 0
    nonmono = []
    with Pool(2) as pool:
        for i, considered, cleared, partial in pool.imap_unordered(
                work, range(1, IMAX + 1)):
            total_considered += considered
            total_cleared += len(cleared)
            total_partial += partial
            results[i] = cleared
            if cleared:
                # check monotonicity of the cleared set (expect a prefix of j's)
                expect = list(range((3 * i) // 2 + 1,
                                    (3 * i) // 2 + 1 + len(cleared)))
                if cleared != expect:
                    nonmono.append(i)
            if i % 100 == 0:
                print(f"i={i} done, elapsed {time.time() - t0:.0f}s", flush=True)
    out = {
        "nstar": NSTAR, "imax": IMAX,
        "pairs_considered": total_considered,
        "pairs_fully_cleared": total_cleared,
        "pairs_partial": total_partial,
        "nonmonotone_i": nonmono,
        "cleared_js_by_i": {str(i): results[i] for i in sorted(results)},
        "runtime_s": time.time() - t0,
    }
    with open(os.path.join(HERE, "pairpass_reference.json"), "w") as f:
        json.dump(out, f)
    print(f"considered {total_considered}, fully cleared {total_cleared}, "
          f"partial {total_partial}, nonmonotone i: {nonmono[:10]}")
    print(f"runtime {time.time() - t0:.0f}s")


if __name__ == "__main__":
    main()
