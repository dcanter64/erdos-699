#!/usr/bin/env python3
"""V-H exact primorial scan. Usage: V-H_scan.py LO HI [both]
Exact integer test Q(i,j)^2 <= C(2j,i) for all R1 pairs LO<=i<=HI.
If 'both', also exact test of Del Pin condition C(2j,i) >= C(j,i)^2
and counts pairs where Del Pin fails but sharpened holds.
Prints total pairs, failures, smallest positive log-margin (float, from
exact integers via math.log on big ints), and (with both) the extra count.
"""
import sys, math
from math import comb, log

lo = int(sys.argv[1]); hi = int(sys.argv[2]); both = len(sys.argv) > 3

def primes_upto(b):
    s = bytearray(b"\x01") * (b + 1); s[0:2] = b"\x00\x00"
    for q in range(2, int(b**0.5) + 1):
        if s[q]: s[q*q::q] = b"\x00" * ((b - q*q)//q + 1)
    return [x for x in range(b + 1) if s[x]]

Pset = set(primes_upto(2*hi))
total = 0; fails = []; minpos = (1e9, None); extra = 0
for i in range(lo, hi+1):
    prod = 1
    for j in range(i+1, 2*i):
        if j in Pset: prod *= j
        if 2*j <= 3*i: continue
        total += 1
        C2 = comb(2*j, i)
        ok = prod*prod <= C2
        if not ok: fails.append((i, j))
        else:
            m = 0.5*log(C2) - log(prod)
            if m < minpos[0]: minpos = (m, (i, j))
        if both:
            dp_ok = C2 >= comb(j, i)**2
            if (not dp_ok) and ok: extra += 1
print(f"range i in [{lo},{hi}]: total R1 pairs = {total}, failures = {fails}")
print(f"smallest positive margin = {minpos[0]:.4f} nats at {minpos[1]}")
if both: print(f"Del Pin fails but sharpened closes = {extra}")
