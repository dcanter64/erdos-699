#!/usr/bin/env python3
"""
P-J2_checks.py -- computations for Prover J2, Cluster J, Cycle 3 (Erdos #699, i=3).
Python standard library only; exact integer / Fraction arithmetic; no randomness.
Sections:
  A. v2(C(n,3)): digit-sum formula, carry count, borrow count; periodicity and
     residue classes of {v2 >= v}; the parity characterisations.
  B. The maximal-valuation bound 2^{v2(C(n,3))} <= n and V3(n) >= (n-1)(n-2)/6.
  C. rho(Q,j): monotonicity, rho > Q^3, vmin(Q) table.
  D. Lambda_3(T) table; per-(Q,R) finiteness maxima from Prop. 4.1's squared
     half (exact, with rigorous analytic caps) and from the J4(b) hybrid
     comparison (exact scans to analytic caps).
  E. J.4(a): the V3-refined comparison per pair: M(j), N(3,j), witnesses.
  F. (LD3) implementation validation + the three squared-bound window checks
     of J.3 ((3,13), (3,14), (2,16)).
"""
from math import comb
from fractions import Fraction
import time

t_start = time.time()

def v2_int(m):
    """2-adic valuation of a nonzero integer."""
    return (m & -m).bit_length() - 1

def v2C(n):
    return v2_int(n) + v2_int(n - 1) + v2_int(n - 2) - 1

def V3(n):
    return comb(n, 3) // (2 ** v2C(n))

def s2(m):
    return bin(m).count("1")

# ---------------------------------------------------------------- A
print("== A. v2 theory ==")
bad = 0
for n in range(3, 20001):
    v = v2C(n)
    if v != s2(n - 3) + s2(3) - s2(n):
        bad += 1
    # carry count when adding (n-3) + 3 in binary
    cnt, carry = 0, 0
    a, b = n - 3, 3
    for i in range(0, n.bit_length() + 2):
        s = ((a >> i) & 1) + ((b >> i) & 1) + carry
        carry = 1 if s >= 2 else 0
        cnt += carry
    if v != cnt:
        bad += 1
    # borrow-out positions when subtracting 3 from n in binary
    cnt, borrow = 0, 0
    for i in range(0, n.bit_length() + 2):
        d = ((n >> i) & 1) - ((3 >> i) & 1) - borrow
        borrow = 1 if d < 0 else 0
        cnt += borrow
    if v != cnt:
        bad += 1
print("A1 digit-sum / carry / borrow identities, n=3..20000: mismatches =", bad)
assert bad == 0

# periodicity mod 2^{v+1} and class lists
for v in range(0, 9):
    mod = 2 ** (v + 1)
    per_bad = 0
    for n in range(3, 3001):
        if (v2C(n) >= v) != (v2C(n + mod) >= v):
            per_bad += 1
    base = 8 * mod
    classes = sorted({n % mod for n in range(base, base + mod) if v2C(n) >= v})
    if v == 0:
        expect = [0, 1]
    elif v == 1:
        expect = [0, 1, 2]
    else:
        expect = [0, 1, 2, 2 ** v, 2 ** v + 2]
    print(f"A2 v={v}: mod {mod}, periodicity mismatches (n<=3000) = {per_bad}, "
          f"classes = {classes}, count = {len(classes)}, matches formula: {classes == expect}")
    assert per_bad == 0 and classes == expect

# parity characterisations
bad = 0
for n in range(3, 100001):
    ge4 = v2C(n) >= 4
    if n % 2 == 0:
        char = (n % 16 == 0) or ((n - 2) % 16 == 0)
    else:
        char = ((n - 1) % 32 == 0)
    if ge4 != char:
        bad += 1
    # general v, n even: v2C >= v  iff  2^v | n or 2^v | (n-2)   (v >= 1)
    # general v, n odd : v2C >= v  iff  2^{v+1} | (n-1)
    for v in (1, 2, 3, 5, 6, 7):
        if n % 2 == 0:
            c = (n % 2 ** v == 0) or ((n - 2) % 2 ** v == 0)
        else:
            c = ((n - 1) % 2 ** (v + 1) == 0)
        if (v2C(n) >= v) != c:
            bad += 1
print("A3 characterisations (n<=100000, incl. general-v parity forms): mismatches =", bad)
assert bad == 0

# ---------------------------------------------------------------- B
print("== B. maximal-valuation bound ==")
bad = 0
for n in range(3, 200001):
    if 2 ** v2C(n) > n:
        bad += 1
    if V3(n) * 6 < (n - 1) * (n - 2):
        bad += 1
print("B1 2^{v2(C(n,3))} <= n and V3(n) >= (n-1)(n-2)/6, n=3..200000: mismatches =", bad)
assert bad == 0

# ---------------------------------------------------------------- C
print("== C. rho(Q,j) and vmin(Q) ==")
mono_bad = 0
for Q in range(2, 11):
    prev = None
    for j in range(4, 501):
        r = Fraction(Q * (Q * j - 1) * (Q * j - 2), (j - 1) * (j - 2))
        if prev is not None and not r < prev:
            mono_bad += 1
        if not r > Q ** 3:
            mono_bad += 1
        prev = r
print("C1 rho strictly decreasing in j and rho > Q^3 (Q=2..10, j=4..500): violations =", mono_bad)
assert mono_bad == 0

def vmin(Q):
    v = 0
    while 2 ** v <= Q ** 3:
        v += 1
    return v

from fractions import Fraction as F
for Q in range(2, 17):
    vm = vmin(Q)
    # the uniform bound is the best this argument gives: at large j, rho < 2^{vm}
    # (so v = vm is not excludable by size alone) and rho > 2^{vm-1} always.
    rho_big = F(Q * (Q * 10 ** 6 - 1) * (Q * 10 ** 6 - 2), (10 ** 6 - 1) * (10 ** 6 - 2))
    dens = F(5, 2 ** (vm + 1))
    print(f"C2 Q={Q}: Q^3={Q**3}, vmin={vm}, density of v2>={vm} classes = {dens} "
          f"= {float(dens):.6f}, rho(Q,10^6) < 2^vmin: {rho_big < 2**vm}")
    assert rho_big < 2 ** vm

# ---------------------------------------------------------------- D
print("== D. Lambda_3 and per-row finiteness ==")
def primes_upto(n):
    sieve = [True] * (n + 1)
    out = []
    for i in range(2, n + 1):
        if sieve[i]:
            out.append(i)
            if i * i <= n:
                for k in range(i * i, n + 1, i):
                    sieve[k] = False
    return out

PRIMES = primes_upto(200)

def Lam3(T):
    if T < 3:
        return 1
    r = 1
    for q in PRIMES:
        if q > T:
            break
        if q < 3:
            continue
        p = q
        while p * q <= T:
            p *= q
        r *= p
    return r

lam_table = [Lam3(T) for T in range(0, 25)]
print("D0 Lambda_3(T), T=0..24:", lam_table)
assert lam_table[3] == 3 and lam_table[6] == 15 and lam_table[8] == 105

def h_of(Q, R):
    if R >= 3:
        return 0
    num = 3 - R
    return -((-num) // Q)  # ceil for num > 0 (R in {0,1,2})

def maxj_squared(Q, R):
    """Exact max j >= 5 with C(Qj+R,3) < (Lam3(T) C(j,h))^2, or None if j=5 fails.
    h=0: condition is C(n,3) < Lam^2 with n = Qj+R; C(.,3) increasing, so binary
    search on n is exact. h=1: scan j up to the rigorous cap 48 Lam^2 / Q^3
    (from C(Qj+R,3) >= (Qj-2)^3/6 >= (Qj/2)^3/6 and (Lam j)^2)."""
    T = R + 2 * (Q - 1)
    h = h_of(Q, R)
    L = Lam3(T)
    if h == 0:
        target = L * L
        lo, hi = 3, 4
        while comb(hi, 3) < target:
            hi *= 2
        while hi - lo > 1:
            mid = (lo + hi) // 2
            if comb(mid, 3) < target:
                lo = mid
            else:
                hi = mid
        nmax = lo
        jmax = (nmax - R) // Q
        return (T, h, L, jmax if jmax >= 5 else None)
    else:
        cap = (48 * L * L) // Q ** 3 + 2
        best = None
        for j in range(5, cap + 1):
            if comb(Q * j + R, 3) < (L * comb(j, h)) ** 2:
                best = j
        return (T, h, L, best)

def maxj_hybrid(Q, R):
    """Exact max j >= 5 NOT closed by the hybrid comparison
    (n-1)(n-2)/6 <= Lam3(T) C(j,h), or None if every j >= 5 is closed.
    h=0: (Qj+R-2)^2 <= (n-1)(n-2) <= 6 Lam gives the cap.
    h=1: (Qj-2)^2 <= (n-1)(n-2) <= 6 Lam j and Qj-2 >= Qj/2 give j <= 24 Lam/Q^2."""
    T = R + 2 * (Q - 1)
    h = h_of(Q, R)
    L = Lam3(T)
    if h == 0:
        from math import isqrt
        cap = (isqrt(6 * L) + 2) // Q + 2
    else:
        cap = (24 * L) // Q ** 2 + 2
    best = None
    for j in range(5, cap + 1):
        n = Q * j + R
        if (n - 1) * (n - 2) <= 6 * L * comb(j, h):
            best = j
    return (T, h, L, best)

for Q in (2, 3, 4):
    for R in range(0, 25):
        if (Q, R) == (2, 0):
            print("D Q=2 R=0: SKIPPED (h=2 row, n=2j, closed separately by Price Prop. 3.3)")
            continue
        T, h, L, mj = maxj_squared(Q, R)
        T2, h2, L2, mh = maxj_hybrid(Q, R)
        assert (T, h, L) == (T2, h2, L2)
        print(f"D Q={Q} R={R}: T={T} h={h} Lam={L} maxj_squared={mj} maxj_hybrid={mh}")

# ---------------------------------------------------------------- E
print("== E. J.4(a): the refined comparison per pair ==")
def N3(j):
    target = comb(2 * j, 6)
    lo, hi = 2 * j, 2 * j + 2
    while comb(hi, 3) < target:
        hi = hi * 2
    while hi - lo > 1:
        mid = (lo + hi) // 2
        if comb(mid, 3) < target:
            lo = mid
        else:
            hi = mid
    return lo

def Mbound(j):
    RHS = j * (j - 1) * (j - 2)
    n = int(RHS ** 0.5) + 3
    while (n - 1) * (n - 2) > RHS:
        n -= 1
    while n * (n - 1) <= RHS:
        n += 1
    return n

for j in range(4, 61):
    print(f"E0 j={j}: C(j,3)={comb(j,3)} M(j)={Mbound(j)} N(3,j)={N3(j)}")

# no-witness pairs in 6..2000 and first witnesses elsewhere
no_witness = []
first_witness = {}
for j in range(6, 2001):
    Cj = comb(j, 3)
    M = Mbound(j)
    w = None
    for n in range(2 * j, M + 1):
        if V3(n) <= Cj:
            w = (n, V3(n))
            break
    if w is None:
        no_witness.append(j)
    else:
        first_witness[j] = w
print("E1 pairs j in 6..2000 with NO n in [2j, M(j)] having V3(n) <= C(j,3):", no_witness)
assert no_witness == [6, 10]
for j in (7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18):
    n, v = first_witness[j]
    print(f"E2 j={j}: first witness n={n}, V3(n)={v}, C(j,3)={comb(j,3)}, "
          f"witness <= N(3,j)={N3(j)}: {n <= N3(j)}")
    assert n <= N3(j) and v <= comb(j, 3)
# the two exceptional pairs: full V3 lists on [2j, M(j)]
for j in (6, 10):
    vals = [(n, V3(n)) for n in range(2 * j, Mbound(j) + 1)]
    print(f"E3 j={j}: (n, V3(n)) on [2j, M(j)] = {vals}; all > C(j,3)={comb(j,3)}: "
          f"{all(v > comb(j,3) for _, v in vals)}")
    assert all(v > comb(j, 3) for _, v in vals)

# ---------------------------------------------------------------- F
print("== F. (LD3) validation and window checks ==")
LIM = 20000
spf = list(range(LIM + 1))
for i in range(2, int(LIM ** 0.5) + 1):
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

def R_of(m):
    r = 1
    for (p, q) in prime_powers(m):
        if p >= 5 or (p == 3 and q >= 9):
            r *= q
    return r

def ld3_ok(n, j, five_only=False):
    for r in (0, 1, 2):
        for (p, q) in prime_powers(n - r):
            rel = (p >= 5) if five_only else (p >= 5 or (p == 3 and q >= 9))
            if rel and j % q > r:
                return False
    return True

# validation 1: >=5-only system, n <= 2000, exactly the six known pairs (P-A1)
surv5 = []
for n in range(7, 2001):
    Rn5 = 1
    for (p, q) in prime_powers(n):
        if p >= 5:
            Rn5 *= q
    if Rn5 > n // 2:
        continue
    j = Rn5
    while j <= n // 2:
        if j >= 4 and ld3_ok(n, j, five_only=True):
            surv5.append((n, j))
        j += Rn5
print("F1 >=5-only (LD3) survivors, n<=2000:", surv5)
assert surv5 == [(10, 5), (28, 14), (82, 41), (162, 70), (244, 122), (730, 365)]

# validation 2: full (LD3), n <= 2000, zero survivors (j over multiples of R(n))
surv = []
for n in range(7, 2001):
    Rn = R_of(n)
    if Rn > n // 2:
        continue
    j = Rn
    while j <= n // 2:
        if j >= 4 and ld3_ok(n, j):
            surv.append((n, j))
        j += Rn
print("F2 full (LD3) survivors, n<=2000:", surv)
assert surv == []

# window checks: rows where the squared bound leaves 5001 <= j <= maxj_squared <= 8000
for (Q, R) in ((3, 13), (3, 14), (2, 16)):
    T, h, L, mj = maxj_squared(Q, R)
    tested, survivors = 0, []
    for j in range(5001, mj + 1):
        n = Q * j + R
        if n % 2 == 1:
            continue
        tested += 1
        if ld3_ok(n, j):
            survivors.append((n, j))
    print(f"F3 row (Q,R)=({Q},{R}): maxj_squared={mj}, triples tested "
          f"(5001<=j<=maxj, n even) = {tested}, (LD3) survivors = {survivors}")
    assert survivors == []

# ---------------------------------------------------------------- G
print("== G. J.3 congruence translations; the (4,2) candidates vs v2 ==")
bad = 0
for R in range(0, 200, 2):  # Q=2, R even: 16|2j+R or 16|2j+R-2  iff  j mod 8 in {-R/2, 1-R/2}
    for j in range(5, 200):
        lhs = ((2 * j + R) % 16 == 0) or ((2 * j + R - 2) % 16 == 0)
        rhs = (j % 8) in {(-R // 2) % 8, (1 - R // 2) % 8}
        if lhs != rhs:
            bad += 1
for R in range(0, 200):  # Q=3: 32|3j+R or 32|3j+R-2  iff  j = -11R or 11(2-R) (mod 32)
    for j in range(5, 200):
        lhs = ((3 * j + R) % 32 == 0) or ((3 * j + R - 2) % 32 == 0)
        rhs = (j % 32) in {(-11 * R) % 32, (11 * (2 - R)) % 32}
        if lhs != rhs:
            bad += 1
for R in range(0, 400):  # Q=4: 128|4j+R (needs 4|R, j=-R/4 mod 32) or 128|4j+R-2 (needs R=2 mod 4, j=(2-R)/4 mod 32)
    for j in range(5, 100):
        lhs = ((4 * j + R) % 128 == 0) or ((4 * j + R - 2) % 128 == 0)
        rhs = False
        if R % 4 == 0 and (j % 32) == (-(R // 4)) % 32:
            rhs = True
        if R % 4 == 2 and (j % 32) == ((2 - R) // 4) % 32:
            rhs = True
        if lhs != rhs:
            bad += 1
print("G1 congruence translations (Q=2,3,4): mismatches =", bad)
assert bad == 0
for (n, j) in ((22, 5), (46, 11), (106, 26)):
    print(f"G2 (4,2) candidate (n,j)=({n},{j}): v2(C(n,3)) = {v2C(n)} (< 4, so the "
          f"v2 condition independently excludes it; F1 killed it via (LD3))")
    assert v2C(n) < 4

print(f"ALL SECTIONS DONE in {time.time() - t_start:.1f}s")
