#!/usr/bin/env python3
"""
Prediction, by the threshold method alone (no sweep dependency), of
the fully-cleared pair count for the SUB-SCOPE 1 <= i <= 1000,
j <= 5000 at NSTAR = 20000:

    count = sum over i of #{ j : (3i)//2 < j <= 5000 and
                                 C(2j, 2(j-i)) <= C(20001, i) }.

using N(i, j) <= NSTAR  iff  C(NSTAR + 1, i) >= C(2j, 2(j-i))
(pairpass_fast.py's classification rule; the per-i cleared set is a
prefix of the j-range because C(2j, 2(j-i)) is strictly increasing
in j). Computed 2026-10-28, before the cap-20000 sweep completes:
the eventual cap-20000 classification must reproduce this number
for the sub-scope. (Sanity: the same code at NSTAR = 10000 gives
768,741, the recorded cap-10000 count; the script asserts this.)
"""
import sys
from math import comb


def max_cleared_j(i, nstar, jmax):
    jlo = (3 * i) // 2 + 1
    if jlo > jmax:
        return jlo - 1
    T = comb(nstar + 1, i)
    if comb(2 * jlo, 2 * (jlo - i)) > T:
        return jlo - 1
    if comb(2 * jmax, 2 * (jmax - i)) <= T:
        return jmax
    lo, hi = jlo, jmax
    while lo + 1 < hi:
        mid = (lo + hi) // 2
        if comb(2 * mid, 2 * (mid - i)) <= T:
            lo = mid
        else:
            hi = mid
    return lo


def sub_scope_count(nstar, imax=1000, jmax=5000):
    total = 0
    for i in range(1, imax + 1):
        J = max_cleared_j(i, nstar, jmax)
        total += max(0, J - ((3 * i) // 2 + 1) + 1)
    return total


def main():
    base = sub_scope_count(10000)
    print(f"sanity, NSTAR=10000 sub-scope count: {base}")
    assert base == 768741, base
    pred = sub_scope_count(20000)
    print(f"PREDICTION, NSTAR=20000, sub-scope i<=1000, j<=5000: "
          f"fully cleared pairs = {pred}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
