#!/usr/bin/env python3
"""
Validate the sweep's bitmask machinery against direct gcd computation
(Phase 0's Legendre-exponent method) on ALL triples i<j<=n/2, n <= 240,
in BOTH regions (the proved j <= 3i/2 region included, as a machinery
check only). Verdicts must agree on every triple.
"""
import sys
from math import comb, gcd

sys.path.insert(0, ".")
from sweep import Tables
from phase0_item2_test import V_i

N = 240
tab = Tables(N)
mismatch = 0
total = 0
for n in range(2, N + 1):
    masks = tab.support_masks(n)
    half = n // 2
    for i in range(1, half + 1):
        v = V_i(n, i)
        si = masks[i] & tab.suff[i]
        for j in range(i + 1, half + 1):
            total += 1
            mask_says_coprime = (si & masks[j]) == 0
            direct_coprime = gcd(v, comb(n, j)) == 1
            if mask_says_coprime != direct_coprime:
                mismatch += 1
                print("MISMATCH", n, i, j, mask_says_coprime, direct_coprime)
print(f"triples compared: {total}, mismatches: {mismatch}")
sys.exit(1 if mismatch else 0)
