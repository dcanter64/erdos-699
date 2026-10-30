#!/usr/bin/env python3
"""
P-I1_checks.py -- Cycle 3, Cluster I, Prover I1.
Python standard library only, exact integer/rational arithmetic.

Sections:
  A. Lambda_3(T) table for T <= 16.
  B. The (2,0) row: the squared Prop. 4.1 inequality holds for all j >= 6
     (exact ratio), so it yields NO per-row bound there.
  C. Per-row exact thresholds Jmax(Q,R) for all rows with T <= 16, h in {0,1}:
     Jmax = max{ j >= 5 : C(Qj+R,3) < (Lambda_3(T) * C(j,h))^2 } (4 if none).
     Binary search justified by monotonicity (proved in P-I1.md, Claim I2.2;
     also spot-verified exactly in C3).  Endpoint and analytic-bound
     assertions included.  Classification: Jmax <= 5000 or not.
  D. Structural candidate lists via the odd top n-1 (rows with h = 0, or
     h = 1 with R in {0,2}): n-1 must lie in the finite set M(T); every
     resulting candidate is disposed by gcd(V_3(n), C(n,j)) > 1 and by an
     explicit (LD3) witness.
  E. Rows with R = 1 (h = 1): generic enumeration up to n <= 6*Lambda_3(T)+2
     using the odd parts of n and n-2; plus the (4,2) validation is in D.
  F. (4,2) validation gcds 77, 69, 371 (asserted in D via the table).
"""

from math import comb, gcd
from fractions import Fraction
import time

t0 = time.time()

# ---------------------------------------------------------------- utilities
def primes_upto(n):
    if n < 2:
        return []
    sieve = bytearray(b"\x01") * (n + 1)
    sieve[0:2] = b"\x00\x00"
    out = []
    for i in range(2, n + 1):
        if sieve[i]:
            out.append(i)
            if i * i <= n:
                sieve[i * i:n + 1:i] = b"\x00" * ((n - i * i) // i + 1)
    return out

def Lambda3(T):
    if T < 3:
        return 1
    res = 1
    for p in primes_upto(T):
        if p < 3:
            continue
        pw = p
        while pw * p <= T:
            pw *= p
        res *= pw
    return res

def h_of(Q, R):
    if R >= 3:
        return 0
    return max(0, -(-(3 - R) // Q))   # ceil((3-R)/Q), =2 only for (2,0)

def factorize(m):
    f = {}
    x = m
    d = 2
    while d * d <= x:
        while x % d == 0:
            f[d] = f.get(d, 0) + 1
            x //= d
        d += 1 if d == 2 else 2
    if x > 1:
        f[x] = f.get(x, 0) + 1
    return f

def V3(n):
    c = comb(n, 3)
    while c % 2 == 0:
        c //= 2
    return c

def ld3_witness(n, j):
    """First (r, p, a, q, j mod q) with q = p^a || (n-r) relevant and
    j mod q > r; None if (LD3) holds for (n, j)."""
    for r in (0, 1, 2):
        for p, a in factorize(n - r).items():
            if p >= 5 or (p == 3 and a >= 2):
                q = p ** a
                if j % q > r:
                    return (r, p, a, q, j % q)
    return None

def oddpart(m):
    while m % 2 == 0:
        m //= 2
    return m

# ---------------------------------------------------------------- Section A
LAM_EXPECTED = {0: 1, 1: 1, 2: 1, 3: 3, 4: 3, 5: 15, 6: 15, 7: 105, 8: 105,
                9: 315, 10: 315, 11: 3465, 12: 3465, 13: 45045, 14: 45045,
                15: 45045, 16: 45045}
for T, v in LAM_EXPECTED.items():
    assert Lambda3(T) == v, (T, Lambda3(T), v)
print("A. Lambda_3(T), T=0..16:", [LAM_EXPECTED[T] for T in range(17)])

# ---------------------------------------------------------------- Section B
# ratio C(j,2)^2 / C(2j,3) = 3j(j-1) / (8(2j-1)); > 1 iff 3j^2-19j+8 > 0.
for j in range(6, 2000):
    ratio = Fraction(comb(j, 2) ** 2, comb(2 * j, 3))
    assert ratio == Fraction(3 * j * (j - 1), 8 * (2 * j - 1)), j
    assert ratio > 1, j
assert Fraction(comb(5, 2) ** 2, comb(10, 3)) < 1   # j=5: 100 < 120
print("B. (2,0): C(j,2)^2/C(2j,3) = 3j(j-1)/(8(2j-1)) > 1 for all "
      "6 <= j < 2000 (exact); the squared inequality gives no bound at (2,0).")

# ---------------------------------------------------------------- Section C
def feasible(Q, R, j):
    T = R + 2 * (Q - 1)
    L = Lambda3(T)
    h = h_of(Q, R)
    return comb(Q * j + R, 3) < (L * comb(j, h)) ** 2

def analytic_bound(Q, R):
    """Real number B_an with: counterexample in row (Q,R), h<=1 => j < B_an.
    h=0: B0 = (2 + (6 L^2)^(1/3)) / Q.   h=1: B1 = (25/3) * L^2 / Q^3."""
    T = R + 2 * (Q - 1)
    L = Lambda3(T)
    h = h_of(Q, R)
    if h == 0:
        return (2 + (6 * L * L) ** (1.0 / 3.0)) / Q
    if h == 1:
        return float(Fraction(25 * L * L, 3 * Q ** 3))
    return None

def jmax(Q, R):
    h = h_of(Q, R)
    assert h in (0, 1)
    cap = int(analytic_bound(Q, R)) + 2
    assert not feasible(Q, R, cap), (Q, R, cap)   # analytic bound is honest
    if not feasible(Q, R, 5):
        return 4
    lo, hi = 5, 6
    while feasible(Q, R, hi):
        lo, hi = hi, min(cap, 2 * hi)
        if hi == cap:
            break
    # invariant: feasible(lo), not feasible(hi)
    while hi - lo > 1:
        mid = (lo + hi) // 2
        if feasible(Q, R, mid):
            lo = mid
        else:
            hi = mid
    assert feasible(Q, R, lo) and not feasible(Q, R, lo + 1)
    return lo

rows = []
Q = 2
while True:
    R = 0
    added = False
    while R + 2 * (Q - 1) <= 16:
        rows.append((Q, R))
        R += 1
        added = True
    if not added:
        break
    Q += 1
assert len(rows) == 64, len(rows)

JMAX = {}
EXCEPTIONS = []
for (Q, R) in rows:
    if (Q, R) == (2, 0):
        continue
    jm = jmax(Q, R)
    JMAX[(Q, R)] = jm
    if jm > 5000:
        EXCEPTIONS.append((Q, R))
EXPECTED_EXCEPTIONS = [(6, 1), (6, 2), (7, 0), (7, 1), (7, 2),
                       (8, 0), (8, 1), (8, 2), (9, 0)]
assert EXCEPTIONS == EXPECTED_EXCEPTIONS, EXCEPTIONS
print("C. Jmax table (T <= 16, h in {0,1}); format R:Jmax")
byQ = {}
for (Q, R) in rows:
    if (Q, R) == (2, 0):
        byQ.setdefault(Q, []).append("R0:h2-special")
    else:
        byQ.setdefault(Q, []).append(f"R{R}:{JMAX[(Q, R)]}")
for Q in sorted(byQ):
    print(f"   Q={Q}: " + "  ".join(byQ[Q]))
print("   Rows with Jmax > 5000:", EXCEPTIONS)
print(f"   => {sum(1 for v in JMAX.values() if v <= 5000)} of {len(JMAX)} "
      "h<=1 rows have Jmax <= 5000.")

# C3: exact spot-verification that f(j) = C(Qj+R,3)/j^2 is strictly
# increasing (the monotonicity used by the binary search), j = 5..300,
# for every h=1 row, plus a window around Jmax when Jmax > 300.
for (Q, R) in rows:
    if h_of(Q, R) != 1:
        continue
    def f(j):
        return Fraction(comb(Q * j + R, 3), j * j)
    pts = list(range(5, 301))
    jm = JMAX[(Q, R)]
    if jm > 300:
        pts += [jm - 1, jm, jm + 1]
    for j in pts:
        assert f(j + 1) > f(j), (Q, R, j)
print("C3. Monotonicity of C(Qj+R,3)/j^2 spot-verified exactly (j=5..300 "
      "and around Jmax) for every h=1 row with T <= 16.")

# ---------------------------------------------------------------- Section D
def floor_log(p, T):
    e = 0
    while p ** (e + 1) <= T:
        e += 1
    return e

def Mset(T):
    """Odd m >= 1 with v_3(m) <= 1 + floor(log_3 T) and, for p >= 5,
    p^{v_p(m)} <= T (equivalently v_p(m) <= floor(log_p T))."""
    cur = {1}
    opts = [[3 ** b for b in range(0, floor_log(3, T) + 2)]]
    for p in primes_upto(T):
        if p < 5:
            continue
        opts.append([p ** a for a in range(0, floor_log(p, T) + 1)])
    for o in opts:
        cur = {x * y for x in cur for y in o}
    return cur

def candidates_via_odd_top(Q, R):
    """Rows where n-1 is a non-special top (h=0 any R, or h=1, R in {0,2}):
    n-1 in M(T), n = Qj + R, n even, j >= 5, R < j."""
    T = R + 2 * (Q - 1)
    out = []
    for m in sorted(Mset(T)):
        n = m + 1
        if n % 2 == 1 or (n - R) % Q != 0:
            continue
        j = (n - R) // Q
        if j >= 5 and j > R:
            out.append((n, j))
    return out

# (row, expected candidate list) -- expected lists locked from first run.
D_ROWS = [
    ((4, 2),  [(22, 5), (46, 11), (106, 26)]),
    ((2, 4),  [(16, 6), (46, 21)]),
    ((2, 6),  [(22, 8), (36, 15), (46, 20), (64, 29), (106, 50), (316, 155)]),
    ((3, 4),  [(22, 6), (46, 14), (64, 20), (106, 34), (316, 104)]),
    ((4, 4),  [(28, 6), (36, 8), (64, 15), (136, 33), (316, 78)]),
    ((5, 0),  []),
    ((5, 2),  []),
    ((2, 8),  [(28, 10), (36, 14), (46, 19), (64, 28), (106, 49), (136, 64),
               (190, 91), (316, 154), (946, 469)]),
    ((6, 0),  [(36, 6)]),
    ((6, 2),  [(56, 9), (386, 64)]),
    ((7, 0),  [(56, 8)]),
    ((7, 2),  [(100, 14), (352, 50), (716, 102), (1486, 212)]),
    ((8, 0),  [(40, 5), (56, 7), (64, 8), (136, 17), (144, 18), (232, 29),
               (352, 44), (456, 57), (496, 62), (1288, 161), (2080, 260),
               (4096, 512), (15016, 1877), (135136, 16892)]),
    ((8, 2),  [(66, 8), (106, 13), (274, 34), (298, 37), (386, 48),
               (586, 73), (946, 118), (1002, 125), (2146, 268), (2458, 307),
               (3466, 433), (9010, 1126), (19306, 2413)]),
    ((9, 0),  [(144, 16)]),
]
print("D. Odd-top (n-1 in M(T)) candidate lists and disposal:")
total_cand = 0
for (Q, R), expected in D_ROWS:
    cand = candidates_via_odd_top(Q, R)
    assert cand == expected, ((Q, R), cand, expected)
    T = R + 2 * (Q - 1)
    line = []
    for (n, j) in cand:
        g = gcd(V3(n), comb(n, j))
        w = ld3_witness(n, j)
        assert g > 1 and w is not None, ((Q, R), n, j, g, w)
        line.append(f"({n},{j}):g{g},w{w}")
    total_cand += len(cand)
    print(f"   ({Q},{R}) T={T} |M|={len(Mset(T))} cand={len(cand)}  "
          + "; ".join(line))
print(f"   Total candidates disposed in D: {total_cand} "
      "(every one has gcd > 1 and an explicit (LD3) witness).")

# (4,2) gcds in the order of F1.11 / V-F Section 5:
assert [gcd(V3(n), comb(n, j)) for (n, j) in D_ROWS[0][1]] == [77, 69, 371]
print("   (4,2) validation gcds: 77, 69, 371 -- exactly as in F1.11/V-F.")

# ---------------------------------------------------------------- Section E
def in_M_local(x, T):
    """x odd: the M(T) conditions tested locally on x."""
    f = factorize(x)
    if f.get(3, 0) > 1 + floor_log(3, T):
        return False
    return all(p ** a <= T for p, a in f.items() if p >= 5)

def candidates_R1(Q, R):
    """R = 1, h = 1: odd parts of the non-special tops n and n-2 lie in
    M(T); one of them has v_2 = 1, hence n <= 2*(3*Lambda_3(T)) + 2.
    Enumerate the row up to 6*Lambda_3(T) + 2 and apply the filters."""
    T = R + 2 * (Q - 1)
    bound = 6 * Lambda3(T) + 2
    out = []
    n = R
    while n <= bound:
        if n % 2 == 0 and (n - R) % Q == 0:
            j = (n - R) // Q
            if j >= 5 and j > R:
                if in_M_local(oddpart(n), T) and in_M_local(oddpart(n - 2), T):
                    out.append((n, j))
        n += 1
    return out, bound

E_ROWS = [((3, 1), []), ((5, 1), [(56, 11)]), ((7, 1), [(288, 41)])]
print("E. R=1 rows (generic odd-part filter, n <= 6*Lambda+2):")
for (Q, R), expected in E_ROWS:
    cand, bound = candidates_R1(Q, R)
    assert cand == expected, ((Q, R), cand, expected)
    T = R + 2 * (Q - 1)
    line = []
    for (n, j) in cand:
        g = gcd(V3(n), comb(n, j))
        w = ld3_witness(n, j)
        assert g > 1 and w is not None
        line.append(f"({n},{j}):g{g},w{w}")
    print(f"   ({Q},{R}) T={T} bound={bound} cand={len(cand)}  "
          + "; ".join(line))

print(f"\nAll assertions passed. Runtime: {time.time() - t0:.1f}s")
