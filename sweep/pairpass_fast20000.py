#!/usr/bin/env python3
"""
Optimized pair-clearance pass for Erdos #699 Stage 2 (replaces the
per-pair N(i,j) computation of pairpass.py, which is O(4.25M) exact
N(i,j) evaluations and impractical).

CAP-20000 CONFIGURATION, prepared 2026-10-28 for the extension run:
NSTAR = 20000, IMAX = 6666 (pairs require (3i)//2 + 1 <= j <= 10000
from 2j <= 20000, so i <= 6666), output pairpass_20000.json. TO BE
RUN ONLY AFTER the cap-20000 sweep completes; the classification is
a pure threshold recomputation and does not itself depend on the
sweep, but its "fully cleared" meaning does (a pair is fully cleared
only once every n in [2j, N(i, j)] has actually been swept).
Sub-scope prediction on record (i <= 1000, j <= 5000):
1,302,183 fully cleared pairs (threshold_prediction_20000.py/.txt).

Exact classification logic (no approximation anywhere):
  N(i,j) = max{ n : C(n,i) < B_j },  B_j = C(2j, 2(j-i)).
  C(n,i) is strictly increasing in n for n >= i, so
      N(i,j) <= NSTAR   iff   C(NSTAR+1, i) >= B_j.
  B_j is strictly increasing in j for fixed i: using the symmetric form
  B_j = C(2j, 2i),
      B_{j+1}/B_j = (2j+2)(2j+1) / ((2(j-i)+2)(2(j-i)+1)) > 1
  since j > j-i. Hence for each i the cleared set {j : N(i,j) <= NSTAR}
  is a prefix of the open j-range, located by exact binary search on j
  with the single threshold T_i = C(NSTAR+1, i).

Verification built in:
  * For every i, the boundary is verified exactly:
    B_{J} <= T_i < B_{J+1} (with the appropriate one-sided version at
    the ends of the j-range).
  * A seeded random sample of pairs is cross-checked against the
    direct N_of() computation imported from pairpass.py.

Output: pairpass_20000.json in the same format checker.py expects.
"""
import json
import os
import random
import sys
import time
from math import comb

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
NSTAR = 20000
IMAX = 6666
JMAX = NSTAR // 2  # from 2j <= NSTAR


def B(i, j):
    return comb(2 * j, 2 * (j - i))


def main():
    t0 = time.time()
    cleared_by_i = {}
    total_considered = 0
    total_cleared = 0
    for i in range(1, IMAX + 1):
        jlo = (3 * i) // 2 + 1  # first open-region j
        if jlo > JMAX:
            cleared_by_i[i] = []
            continue
        considered = JMAX - jlo + 1
        total_considered += considered
        T = comb(NSTAR + 1, i)
        if B(i, jlo) > T:
            J = jlo - 1  # none cleared
        elif B(i, JMAX) <= T:
            J = JMAX  # all cleared
        else:
            lo, hi = jlo, JMAX  # B(lo) <= T < B(hi)
            while lo + 1 < hi:
                mid = (lo + hi) // 2
                if B(i, mid) <= T:
                    lo = mid
                else:
                    hi = mid
            J = lo
        # exact boundary verification for this i
        if J >= jlo:
            assert B(i, J) <= T, (i, J)
        if J + 1 <= JMAX:
            assert B(i, J + 1) > T, (i, J + 1)
        cleared = list(range(jlo, J + 1)) if J >= jlo else []
        cleared_by_i[i] = cleared
        total_cleared += len(cleared)
        if i % 200 == 0:
            print(f"i={i} done, elapsed {time.time() - t0:.0f}s", flush=True)

    # Cross-check against the direct N_of from pairpass.py on random pairs
    from pairpass import N_of
    rng = random.Random(20261028)
    checked = 0
    mismatches = []
    for _ in range(150):
        i = rng.randint(1, IMAX)
        jlo = (3 * i) // 2 + 1
        if jlo > JMAX:
            continue
        j = rng.randint(jlo, JMAX)
        nij = N_of(i, j)
        direct_cleared = nij <= NSTAR
        fast_cleared = j in set(cleared_by_i[i]) if len(cleared_by_i[i]) < 60 \
            else (cleared_by_i[i] and j <= cleared_by_i[i][-1])
        # cleared_by_i[i] is a prefix range by construction; membership:
        fast_cleared = bool(cleared_by_i[i]) and j <= cleared_by_i[i][-1]
        checked += 1
        if direct_cleared != fast_cleared:
            mismatches.append((i, j, nij))
    print(f"cross-check vs direct N_of: {checked} pairs, "
          f"mismatches: {mismatches}")
    assert not mismatches

    out = {
        "nstar": NSTAR, "imax": IMAX,
        "pairs_considered": total_considered,
        "pairs_fully_cleared": total_cleared,
        "pairs_partial": total_considered - total_cleared,
        "nonmonotone_i": [],  # prefix structure proved (B_j increasing)
        "method": "threshold binary search on T_i = C(NSTAR+1, i); "
                  "boundary verified exactly for every i; cross-checked "
                  "against direct N_of on 150 seeded random pairs",
        "cleared_js_by_i": {str(i): cleared_by_i[i]
                            for i in sorted(cleared_by_i)},
        "runtime_s": time.time() - t0,
    }
    with open(os.path.join(HERE, "pairpass_20000.json"), "w") as f:
        json.dump(out, f)
    print(f"considered {total_considered}, fully cleared {total_cleared}, "
          f"partial {total_considered - total_cleared}")
    print(f"runtime {time.time() - t0:.0f}s")


if __name__ == "__main__":
    main()
