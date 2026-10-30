#!/usr/bin/env python3
"""Fast exact scan: binomials updated incrementally by gcd-reduced
small-factor steps; asserted against math.comb every 997th pair and
at every range end. Tests Q^2<=C(2j,i) and Del Pin C(2j,i)>=C(j,i)^2.
Usage: V-H_scan_fast.py LO HI
"""
import sys
from math import comb, log, gcd

lo, hi = int(sys.argv[1]), int(sys.argv[2])

def primes_upto(b):
    s = bytearray(b"\x01") * (b + 1); s[0:2] = b"\x00\x00"
    for q in range(2, int(b**0.5) + 1):
        if s[q]: s[q*q::q] = b"\x00" * ((b - q*q)//q + 1)
    return set(x for x in range(b + 1) if s[x])

Pset = primes_upto(2*hi)

def step(C, num, den):
    g = gcd(num, den); num //= g; den //= g
    assert C % den == 0
    return (C // den) * num

total = 0; fails = []; extra = 0; minpos = (1e9, None); checked = 0
for i in range(lo, hi+1):
    prod = 1
    # j starts at i+1: C(2j,i) and C(j,i) initialised directly once per i
    j = i + 1
    C2 = comb(2*j, i); C1 = comb(j, i)
    while j < 2*i:
        if j in Pset: prod *= j
        if 2*j > 3*i:
            total += 1; checked += 1
            if checked % 997 == 0:
                assert C2 == comb(2*j, i) and C1 == comb(j, i), (i, j)
            ok = prod*prod <= C2
            if not ok: fails.append((i, j))
            else:
                m = 0.5*log(C2) - log(prod)
                if m < minpos[0]: minpos = (m, (i, j))
            if ok and C2 < C1*C1: extra += 1
        # advance j -> j+1
        C2 = step(C2, (2*j+2)*(2*j+1), (2*j+2-i)*(2*j+1-i))
        C1 = step(C1, j+1, j+1-i)
        j += 1
    assert C2 == comb(2*j, i) and C1 == comb(j, i), ("end", i, j)
print(f"range i in [{lo},{hi}]: total R1 pairs = {total}, failures = {fails}")
print(f"smallest positive margin = {minpos[0]:.4f} nats at {minpos[1]}")
print(f"Del Pin fails but sharpened closes = {extra}")
