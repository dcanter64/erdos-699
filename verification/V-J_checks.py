#!/usr/bin/env python3
"""V-J independent checks for Cluster J, Cycle 3 (Erdos #699, i=3).
Python stdlib only, exact arithmetic. Implementations written independently
of the provers' scripts: v2 via trailing-zero string scan and via direct
division of C(n,3); Lambda_3 via trial division primality; N(3,j)/Nmax via
linear/binary search on exact comb(); hybrid maxima via binary search
(h=0, monotone) and direct scan to analytic caps (h=1); (LD3) via an SPF
factorisation written for this verifier, applied by brute force over ALL
j (validation) and over the three window rows (disposals).
Sections:
  1  v2 formula vs direct; class lists for v<=8 over n<=10^5
  2  rho monotonicity (Fractions), vmin(Q) for Q<=16 by exact integers
  3  F1.14 settlement: minima table 5<=j<=18; named witnesses; j>=19
     power-of-two witness (in range, V3 value); exact validity range
     of the inequality V3(2^a)<=C(j,3) for the a-witness, j<=5000;
     C(4j,3)<C(2j,6) spot range
  4  Criterion (A)/(B) arithmetic: Lambda_3, Nmax, jsq for the boundary
     rows named in the brief, plus all h=0 thresholds at Q=2,3,4 and
     the h=1 jsq values at Q in {2,3,4} and the Q=5,6 bonus rows
  5  Hybrid comparison: j_hyb for the boundary rows; j_hyb<=j_sq for
     every row Q in {2,3,4}, 0<=R<=24, (Q,R)!=(2,0); maximal bound
     2^v2<=n spot range
  6  (LD3): >=5-only validation at n<=2000 (brute over all j), full
     system at n<=2000 (brute over all j), window disposals
     (3,13),(3,14),(2,16) with counts
"""
import time
from fractions import Fraction
from math import comb, isqrt

t0 = time.time()

def v2_str(x):
    """trailing zeros of x>0 via its binary string (independent impl)."""
    s = bin(x)[2:]
    return len(s) - 1 - s.rfind('1')

def v2C(n):
    return v2_str(n) + v2_str(n - 1) + v2_str(n - 2) - 1

def V3(n):
    return comb(n, 3) >> v2C(n)

def s2(m):
    return bin(m).count('1')

# ---------------------------------------------------------------- 1
print("== 1: v2 formula and classes ==")
for n in range(3, 3001):
    c = comb(n, 3)
    v = 0
    cc = c
    while cc % 2 == 0:
        cc //= 2; v += 1
    assert v == v2C(n) == s2(n - 3) + 2 - s2(n), n
    assert cc == V3(n)
print("direct-division v2(C(n,3)) == string v2 == s2 formula, n<=3000: OK")
for v in range(0, 9):
    mod = 2 ** (v + 1)
    classes = sorted({n % mod for n in range(3, 100001) if v2C(n) >= v})
    if v == 0:
        exp = [0, 1]
    elif v == 1:
        exp = [0, 1, 2]
    else:
        exp = [0, 1, 2, 2 ** v, 2 ** v + 2]
    assert classes == exp, (v, classes)
    print(f"v={v}: classes mod {mod} = {classes} (brute n<=10^5)")
# v>=4 parity forms over the same range
for n in range(3, 100001):
    ge4 = v2C(n) >= 4
    if n % 2 == 0:
        assert ge4 == (n % 16 == 0 or (n - 2) % 16 == 0), n
    else:
        assert ge4 == ((n - 1) % 32 == 0), n
print("v2>=4 iff (even: 16|n or 16|(n-2); odd: 32|(n-1)), n<=10^5: OK")
# maximal bound 2^v2 <= n with equality iff n a power of 2 (spot)
for n in range(3, 50001):
    assert 2 ** v2C(n) <= n
    assert (2 ** v2C(n) == n) == (n & (n - 1) == 0), n
print("2^v2(C(n,3)) <= n, equality iff n=2^a, n<=50000: OK")

# ---------------------------------------------------------------- 2
print("== 2: rho and vmin ==")
def rho(Q, j):
    return Fraction(Q * (Q * j - 1) * (Q * j - 2), (j - 1) * (j - 2))
for Q in range(2, 17):
    prev = None
    for j in range(4, 300):
        r = rho(Q, j)
        assert r == Fraction(comb(Q * j, 3), comb(j, 3))
        assert r > Q ** 3
        if prev is not None:
            assert r < prev
        prev = r
    # near-infimum: rho at huge j is below 2^vmin (sharpness of vmin)
    assert rho(Q, 10 ** 7) < 2 ** (min(v for v in range(30) if 2 ** v > Q ** 3))
print("rho strictly decreasing, > Q^3, closed form OK, Q=2..16: OK")
vmin_tab = {}
for Q in range(2, 17):
    v = 0
    while 2 ** v <= Q ** 3:
        v += 1
    vmin_tab[Q] = v
print("vmin(Q), Q=2..16:", [vmin_tab[Q] for Q in range(2, 17)])
assert [vmin_tab[Q] for Q in range(2, 17)] == [4, 5, 7, 7, 8, 9, 10, 10, 10, 11, 11, 12, 12, 12, 13]
# strictness at powers of two
for Q in (2, 4, 8, 16):
    assert Q ** 3 == 2 ** (vmin_tab[Q] - 1)
print("Q in {2,4,8,16}: Q^3 = 2^(vmin-1) exactly (strictness load-bearing): OK")

# ---------------------------------------------------------------- 3
print("== 3: F1.14 settlement ==")
def N3(j):
    target = comb(2 * j, 6)
    lo, hi = 3, 4
    while comb(hi, 3) < target:
        hi *= 2
    while lo + 1 < hi:
        mid = (lo + hi) // 2
        if comb(mid, 3) < target:
            lo = mid
        else:
            hi = mid
    return lo

table = {}
for j in range(5, 19):
    N = N3(j)
    vals = [(V3(n), n) for n in range(2 * j, N + 1)]
    mn = min(vals)
    table[j] = (comb(j, 3), N, mn)
    print(f"j={j}: C(j,3)={comb(j,3)} N(3,j)={N} minV3={mn[0]} at n={mn[1]} closes={mn[0] > comb(j,3)}")
assert [j for j in range(5, 19) if table[j][2][0] > table[j][0]] == [5, 6, 10]
assert table[9][2] == (51, 18) and table[17][2] == (187, 34)
# named witnesses: in [2j, N(3,j)] and V3 <= C(j,3)
named = [(16, 7), (16, 8), (18, 9)] + [(32, j) for j in range(11, 17)] + [(34, 17), (64, 18)]
for (n, j) in named:
    assert 2 * j <= n <= N3(j) and V3(n) <= comb(j, 3), (n, j)
print("named witnesses (16,7)equality, (32,11..16), (34,17), (64,18): in range, V3<=C(j,3): OK")
assert V3(16) == comb(7, 3) == 35 and v2C(16) == 4
# j>=19 power-of-two witness: range, closed form, inequality
for j in range(19, 5001):
    a = (2 * j - 1).bit_length()   # ceil(log2(2j)) for 2j not a power of 2 handled below
    if 2 ** (a - 1) >= 2 * j:
        a -= 1
    n = 2 ** a
    assert 2 * j <= n < 4 * j, (j, n)
    assert V3(n) == (n - 1) * (n // 2 - 1) // 3
    assert V3(n) <= comb(j, 3), (j, n, V3(n), comb(j, 3))
    assert comb(n, 3) < comb(2 * j, 6), (j, n)   # n <= N(3,j)
print("a-witness for 19<=j<=5000: in [2j,4j), in [2j,N], V3<=C(j,3): OK")
# exact validity range of the bare inequality V3(2^a) <= C(j,3), j<=5000
holds = []
for j in range(5, 5001):
    a = (2 * j - 1).bit_length()
    if 2 ** (a - 1) >= 2 * j:
        a -= 1
    if V3(2 ** a) <= comb(j, 3):
        holds.append(j)
print("inequality V3(2^a)<=C(j,3) holds at j in 5..5000 exactly for:",
      holds[:20], "... contiguous from", next(j for j in range(5, 5001) if all(k in holds for k in range(j, 5001))))
# C(4j,3) < C(2j,6) spot range (the in-range lemma)
bad = [j for j in range(10, 2001) if not comb(4 * j, 3) < comb(2 * j, 6)]
assert bad == []
print("C(4j,3) < C(2j,6) for 10<=j<=2000: OK (0 failures)")

# ---------------------------------------------------------------- 4
print("== 4: Lambda_3, Nmax, squared-bound criteria ==")
def is_prime(p):
    if p < 2:
        return False
    for d in range(2, isqrt(p) + 1):
        if p % d == 0:
            return False
    return True

def Lam3(T):
    if T < 3:
        return 1
    r = 1
    for q in range(3, T + 1):
        if is_prime(q):
            pw = q
            while pw * q <= T:
                pw *= q
            r *= pw
    return r

def Nmax(T):
    L = Lam3(T)
    target = L * L
    lo, hi = 3, 4
    while comb(hi, 3) < target:
        hi *= 2
    while lo + 1 < hi:
        mid = (lo + hi) // 2
        if comb(mid, 3) < target:
            lo = mid
        else:
            hi = mid
    assert comb(lo, 3) < target <= comb(lo + 1, 3)
    return lo

assert [Lam3(T) for T in (6, 8, 10, 12, 17, 24, 25)] == [15, 105, 315, 3465, 765765, 334639305, 1673196525]
assert [Nmax(T) for T in (6, 8, 10, 12, 17, 24, 25)] == [12, 41, 85, 417, 15210, 875861, 2561033]
# Nmax(T) <= 10^6 iff T <= 24 (monotone check over T=3..30)
vals = [Nmax(T) for T in range(3, 31)]
assert all(vals[i] <= vals[i + 1] for i in range(len(vals) - 1))
assert all((Nmax(T) <= 10 ** 6) == (T <= 24) for T in range(3, 31))
print("Lambda_3/Nmax spot values OK; Nmax(T)<=10^6 iff T<=24 for 3<=T<=30: OK")

def jsq_h0(Q, R):
    return (Nmax(R + 2 * Q - 2) - R) // Q

def h_of(Q, R):
    if R >= 3:
        return 0
    return -((-(3 - R)) // Q)

def jsq_h1(Q, R):
    T = R + 2 * (Q - 1)
    L = Lam3(T)
    cap = 24 * L * L // Q ** 3 + 2
    best = None
    for j in range(1, cap + 1):
        if comb(Q * j + R, 3) < (L * j) ** 2:
            best = j
    assert best is None or not comb(Q * (best + 1) + R, 3) < (L * (best + 1)) ** 2 or best == cap
    return best

boundary = [(2, 22), (2, 24), (3, 20), (3, 21), (4, 18), (4, 20), (5, 0), (5, 1), (5, 2), (6, 0), (6, 1), (6, 2)]
for (Q, R) in boundary:
    T = R + 2 * Q - 2
    h = h_of(Q, R)
    if h == 0:
        jm = jsq_h0(Q, R)
        print(f"row ({Q},{R}): h=0 T={T} Lam={Lam3(T)} Nmax={Nmax(T)} jsq={jm} "
              f"closedA={jm <= 5000} closedB={Nmax(T) <= 10 ** 6}")
    else:
        jm = jsq_h1(Q, R)
        print(f"row ({Q},{R}): h=1 T={T} Lam={Lam3(T)} jsq={jm} closedA={jm is not None and jm <= 5000}")
# headline thresholds at Q=2,3,4 (h=0)
assert all(jsq_h0(2, R) > 5000 and Nmax(R + 2) <= 10 ** 6 for R in (16, 18, 20, 22))
assert all((jsq_h0(2, R) <= 5000) for R in (4, 6, 8, 10, 12, 14))
assert jsq_h0(2, 24) == 1280504 and Nmax(26) == 2561033
assert all(Nmax(R + 4) <= 10 ** 6 for R in range(3, 21)) and jsq_h0(3, 21) == 853670 and Nmax(25) == 2561033
assert [jsq_h0(3, R) for R in range(3, 13)] == [12, 12, 26, 26, 136, 136, 764, 763, 763, 763]
assert [jsq_h0(3, R) for R in (13, 14)] == [5065, 5065]
assert all(Nmax(R + 6) <= 10 ** 6 for R in (4, 6, 8, 10, 12, 14, 16, 18))
assert [jsq_h0(4, R) for R in (4, 6, 8, 10, 12)] == [20, 102, 573, 572, 3799]
assert jsq_h0(4, 20) == 640253
# h=1 exact values
h1_exp = {(2, 1): 6, (2, 2): 5, (3, 0): 2, (3, 1): 50, (3, 2): 48, (4, 0): 21,
          (4, 1): 1033, (4, 2): 1032, (5, 0): 529, (5, 1): 4762, (5, 2): 4762, (6, 0): 2756}
for (Q, R), exp in h1_exp.items():
    got = jsq_h1(Q, R)
    assert got == exp, (Q, R, got, exp)
print("h=1 jsq values (Q=2,3,4 and bonus 5,6): all match")
# (6,1),(6,2) and Q in {7,8} h=1 rows: squared inequality HOLDS at j=5001 (A fails)
for (Q, R) in [(6, 1), (6, 2), (7, 0), (7, 1), (7, 2), (8, 0), (8, 1), (8, 2)]:
    T = R + 2 * (Q - 1)
    assert comb(Q * 5001 + R, 3) < (Lam3(T) * 5001) ** 2, (Q, R)
print("(6,1),(6,2), Q=7,8 h=1: squared inequality holds at j=5001 (criterion A fails): OK")
# first-open windows (lower ends from n>10^6)
for (Q, R), (lo_exp, jm_exp) in {(2, 24): (499989, 1280504), (3, 21): (333327, 853670), (4, 20): (249996, 640253)}.items():
    lo = max(5001, (10 ** 6 - R) // Q + 1)
    assert lo == lo_exp and jsq_h0(Q, R) == jm_exp, (Q, R, lo)
print("first-open windows (2,24),(3,21),(4,20): lower/upper ends match")

# ---------------------------------------------------------------- 5
print("== 5: hybrid comparison ==")
def jhyb(Q, R):
    """largest j>=5 NOT closed by hybrid: (n-1)(n-2) <= 6 Lam3(T) C(j,h)."""
    T = R + 2 * (Q - 1)
    L = Lam3(T)
    h = h_of(Q, R)
    if h == 0:
        # LHS increasing in j, RHS constant: binary search
        lo, hi = 4, 8
        def notclosed(j):
            n = Q * j + R
            return (n - 1) * (n - 2) <= 6 * L
        while notclosed(hi):
            hi *= 2
        while lo + 1 < hi:
            mid = (lo + hi) // 2
            if notclosed(mid):
                lo = mid
            else:
                hi = mid
        return lo if lo >= 5 else None
    else:
        cap = 24 * L // Q ** 2 + 2
        best = None
        for j in range(5, cap + 1):
            n = Q * j + R
            if (n - 1) * (n - 2) <= 6 * L * j:
                best = j
        return best

hyb_boundary = {(2, 20): 4662, (2, 22): 22394, (3, 18): None, (3, 19): 14930, (4, 16): 2332, (4, 18): 11198}
for (Q, R), exp in hyb_boundary.items():
    got = jhyb(Q, R)
    print(f"hybrid row ({Q},{R}): j_hyb={got} (prover J2: {exp}) closes_residual={got is None or got <= 5000}")
    if exp is not None:
        assert got == exp, (Q, R, got, exp)
assert jhyb(3, 18) <= 5000
# J2's full hybrid table (selected rows printed in its Claim J2.12)
j2_hyb = {(2, 4): None, (2, 6): 10, (2, 8): 18, (2, 10): 67, (2, 12): 254, (2, 14): 253,
          (2, 16): 1064, (2, 18): 4663, (3, 1): 10, (3, 3): 7, (3, 5): 13, (3, 7): 46,
          (3, 9): 170, (3, 11): 170, (3, 13): 710, (3, 15): 3109, (3, 17): 3109,
          (4, 2): 39, (4, 4): 10, (4, 6): 34, (4, 8): 128, (4, 10): 127, (4, 12): 533,
          (4, 14): 2332, (4, 20): 25044}
for (Q, R), exp in j2_hyb.items():
    got = jhyb(Q, R)
    assert got == exp, (Q, R, got, exp)
print("J2 hybrid table (all rows it prints): all match")
# J2's squared table (selected rows)
def jsq_any(Q, R):
    if h_of(Q, R) == 0:
        jm = jsq_h0(Q, R)
        return jm if jm >= 5 else None
    return jsq_h1(Q, R)
j2_sq = {(2, 4): None, (2, 6): 17, (2, 8): 38, (2, 10): 203, (2, 12): 1144, (2, 14): 1143,
         (2, 16): 7597, (2, 18): 54140, (2, 20): 54139, (2, 22): 437919,
         (3, 1): 50, (3, 3): 12, (3, 5): 26, (3, 7): 136, (3, 9): 764, (3, 11): 763,
         (3, 13): 5065, (3, 15): 36094, (3, 17): 36093, (3, 19): 291947,
         (4, 2): 1032, (4, 4): 20, (4, 6): 102, (4, 8): 573, (4, 10): 572, (4, 12): 3799,
         (4, 14): 27071, (4, 16): 27070, (4, 18): 218960, (4, 20): 640253}
for (Q, R), exp in j2_sq.items():
    got = jsq_any(Q, R)
    assert got == exp, (Q, R, got, exp)
print("J2 squared table (all rows it prints): all match")
# sharper-than-squared in EVERY row computed by J2 (Q=2,3,4; 0<=R<=24; !=(2,0))
viol = []
for Q in (2, 3, 4):
    for R in range(0, 25):
        if (Q, R) == (2, 0):
            continue
        a = jhyb(Q, R)
        b = jsq_any(Q, R)
        av = -1 if a is None else a
        bv = -1 if b is None else b
        if av > bv:
            viol.append((Q, R, a, b))
assert viol == [], viol
print("j_hyb <= j_sq for all 74 rows Q in {2,3,4}, 0<=R<=24, (2,0) excluded: OK")

# ---------------------------------------------------------------- 6
print("== 6: (LD3) validation and windows ==")
LIM = 23000
spf = list(range(LIM + 1))
for i in range(2, isqrt(LIM) + 1):
    if spf[i] == i:
        for k in range(i * i, LIM + 1, i):
            if spf[k] == k:
                spf[k] = i

def prime_powers(m):
    out = []
    while m > 1:
        p = spf[m]
        q = 1
        while m % p == 0:
            m //= p
            q *= p
        out.append((p, q))
    return out

def ld3_survives(n, j, five_only):
    for r in (0, 1, 2):
        for (p, q) in prime_powers(n - r):
            rel = p >= 5 if five_only else (p >= 5 or (p == 3 and q >= 9))
            if rel and j % q > r:
                return False
    return True

surv5 = []
survfull = []
for n in range(7, 2001):
    for j in range(4, n // 2 + 1):
        if ld3_survives(n, j, True):
            surv5.append((n, j))
        if ld3_survives(n, j, False):
            survfull.append((n, j))
print(">=5-only survivors n<=2000 (brute all j):", surv5)
assert surv5 == [(10, 5), (28, 14), (82, 41), (162, 70), (244, 122), (730, 365)]
print("full (LD3) survivors n<=2000 (brute all j):", survfull)
assert survfull == []
for (Q, R), cnt_exp in [((3, 13), 33), ((3, 14), 32), ((2, 16), 2597)]:
    jm = jsq_h0(Q, R)
    tested = 0
    surv = []
    for j in range(5001, jm + 1):
        n = Q * j + R
        if n % 2 == 1:
            continue
        tested += 1
        if ld3_survives(n, j, False):
            surv.append((n, j))
    print(f"window ({Q},{R}): j in [5001,{jm}], n even tested={tested}, survivors={surv}")
    assert tested == cnt_exp and surv == []

print(f"ALL V-J CHECKS PASSED in {time.time() - t0:.1f}s")
