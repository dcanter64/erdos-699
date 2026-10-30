"""Coordinator computation: exact union of S1-cleared and S3-cleared pairs.

Scope: pairs (i, j) with 1 <= i <= 1000, floor(3i/2) < j <= 5000
(the pairpass scope, 2j <= 10000). Baseline cleared set from
erdos-699/pairpass.json (EEES + sweep): 768,741 pairs.

S3 (Cluster C, verified): clears EVERY partial pair with 132 <= i <= 1000,
counted 2,891,106 (third recount in V-C).

S1 (Cluster B, verified): pair (i, j) is Kummer-cleared iff
    C(j, i) * 10001^{pi(i-1)} < C(10001, i)
(the exact predicate whose equivalence chain V-B re-derived and whose
prefix property in j V-B verified). J_K(i) = largest j <= 5000 with the
predicate true. Newly Kummer-cleared at row i: max(0, min(J_K(i),5000) - J_i)
where J_i is the EEES frontier from pairpass.json.

Union: for i >= 132 S3 already clears all partial pairs, so S1 adds
nothing there beyond S3. For i <= 131 the union contribution is exactly
newly_K(i). Validation targets (two provers + V-B, three computations):
total newly_K = 328,079; J_K(100) = 1045; J_K(1000) = 2541.

Stdlib only, exact integer arithmetic.
"""
import json
from math import comb

NSTAR = 10000
IMAX = 1000
JMAX = 5000

# pi(x) for x <= 1000 by sieve
sieve = [True] * (IMAX + 1)
sieve[0] = sieve[1] = False
for p in range(2, IMAX + 1):
    if sieve[p]:
        for m in range(p * p, IMAX + 1, p):
            sieve[m] = False
pi = [0] * (IMAX + 1)
c = 0
for x in range(IMAX + 1):
    if sieve[x]:
        c += 1
    pi[x] = c

d = json.load(open("/home/hatch/workspace/math-hunt/erdos-699/pairpass.json"))
assert d["pairs_considered"] == 4249500 and d["pairs_fully_cleared"] == 768741
cleared = d["cleared_js_by_i"]

def J_eees(i):
    lst = cleared[str(i)]
    return max(lst) if lst else (3 * i) // 2

def kummer_pred(i, j, rhs_cache={}):
    if i not in rhs_cache:
        rhs_cache[i] = comb(NSTAR + 1, i)
    return comb(j, i) * (NSTAR + 1) ** pi[i - 1] < rhs_cache[i]

def J_K(i):
    lo, hi = (3 * i) // 2, JMAX  # predicate is a prefix in j on this range
    if not kummer_pred(i, lo + 1):
        return lo
    while lo < hi:
        mid = (lo + hi + 1) // 2
        if kummer_pred(i, mid):
            lo = mid
        else:
            hi = mid - 1
    return lo

newly_K_total = 0
newly_K_small = 0  # i <= 131
JK = {}
for i in range(1, IMAX + 1):
    jk = J_K(i)
    JK[i] = jk
    nk = max(0, min(jk, JMAX) - J_eees(i))
    newly_K_total += nk
    if i <= 131:
        newly_K_small += nk

print("validation: total newly_K =", newly_K_total, "(target 328079)")
print("validation: J_K(100) =", JK[100], "(target 1045)")
print("validation: J_K(1000) =", JK[1000], "(target 2541)")

S3_NEW = 2891106
BASE = 768741
PARTIAL = 3480759
union_newly = S3_NEW + newly_K_small
print("S1 newly cleared at i<=131:", newly_K_small)
print("union newly cleared:", union_newly)
print("total cleared in scope:", BASE + union_newly, "of 4249500")
print("partial pairs remaining (all at i<=131, before any S3 per-pair"
      " clearances there):", PARTIAL - union_newly)
