#!/usr/bin/env python3
"""P-J1 checks: Cluster J (v2 theory at i=3), Cycle 3.
Python stdlib only, exact integer arithmetic, no randomness except a
fixed-seed monotonicity sample in section C (the monotonicity itself is
proved analytically in P-J1.md, Claim J3.3).
Sections:
  A  v2 formulas (Legendre digit-sum / borrow count) and J1 classes
  B  rho(Q,j), vmin(Q) table
  C  Lambda_3, Nmax, squared-bound jmax tables for Q=2,3,4 (+ Q=5,6 h=1)
  D  J4(a): refined-comparison classification for j<=18; power-of-two
     witness for 19<=j<=2000
  E  J4(b): U-sharp tail thresholds t(j) and hybrid intervals for j=6,10
  F  F1.13 thresholds n0(j,v) (spot re-verification of certified input)
"""
import math
import random
import time
from fractions import Fraction
from math import comb

t0 = time.time()


def v2_int(x):
    assert x > 0
    return (x & -x).bit_length() - 1


def v2C(n):
    """v2(C(n,3)) via v2(n(n-1)(n-2)) - v2(6)."""
    return v2_int(n) + v2_int(n - 1) + v2_int(n - 2) - 1


def V3(n):
    return comb(n, 3) // (2 ** v2C(n))


def s2(m):
    return bin(m).count("1")


def borrows_sub3(n):
    """Number of borrows when subtracting 3 from n in binary (direct)."""
    b = 0
    borrow = 0
    x, y = n, 3
    while x or y or borrow:
        if (x & 1) - borrow - (y & 1) < 0:
            b += 1
            borrow = 1
        else:
            borrow = 0
        x >>= 1
        y >>= 1
    return b


def primes_upto(n):
    s = [True] * (n + 1)
    out = []
    for i in range(2, n + 1):
        if s[i]:
            out.append(i)
            for k in range(i * i, n + 1, i):
                s[k] = False
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


def N3(j):
    """max{n : C(n,3) < C(2j,6)} by exact binary search."""
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


def Nmax(T):
    """max{n : C(n,3) < Lambda3(T)^2}; certified by the two checks in C."""
    L = Lambda3(T)
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
    return lo


# ---------------------------------------------------------------- A
print("== A: v2 formulas and classes ==")
for n in range(3, 5001):
    assert v2C(n) == s2(n - 3) + s2(3) - s2(n), n
    assert v2C(n) == borrows_sub3(n), n
    assert comb(n, 3) == (2 ** v2C(n)) * V3(n)
print("v2C == s2(n-3)+2-s2(n) == #borrows(sub 3 from n), n=3..5000: OK")

expected_classes = {
    0: [0, 1],
    1: [0, 1, 2],
    2: [0, 1, 2, 4, 6],
    3: [0, 1, 2, 8, 10],
    4: [0, 1, 2, 16, 18],
    5: [0, 1, 2, 32, 34],
    6: [0, 1, 2, 64, 66],
    7: [0, 1, 2, 128, 130],
}
for v, exp in expected_classes.items():
    mod = 2 ** (v + 1)
    classes = [r for r in range(mod) if v2C(r + mod * 100) >= v]
    assert classes == exp, (v, classes)
    if v >= 2:
        assert exp == [0, 1, 2, 2 ** v, 2 ** v + 2]
    print(f"v={v}: classes mod {mod} = {classes} (count {len(classes)})")
# v2>=4 forms: n even <=> 16|n or 16|(n-2); n odd <=> 32|(n-1)
for n in range(3, 20001):
    cond = v2C(n) >= 4
    if n % 2 == 0:
        assert cond == (n % 16 == 0 or (n - 2) % 16 == 0), n
    else:
        assert cond == ((n - 1) % 32 == 0), n
print("v2>=4: even <=> 16|n or 16|(n-2); odd <=> 32|(n-1), n<=20000: OK")

# ---------------------------------------------------------------- B
print("== B: rho and vmin ==")
for Q in range(2, 9):
    prev = None
    for j in range(3, 400):
        rho = Fraction(comb(Q * j, 3), comb(j, 3))
        assert rho > Q ** 3
        if prev is not None:
            assert rho < prev
        prev = rho
    # closed form of the task
    for j in [3, 5, 17, 5001]:
        assert Fraction(comb(Q * j, 3), comb(j, 3)) == Fraction(
            Q * (Q * j - 1) * (Q * j - 2), (j - 1) * (j - 2))
print("rho(Q,j) strictly decreasing in j and > Q^3, Q=2..8, j<400: OK")
vmin_table = {}
for Q in range(2, 17):
    vmin = math.floor(3 * math.log2(Q)) + 1
    assert 2 ** vmin > Q ** 3 >= 2 ** (vmin - 1)
    vmin_table[Q] = vmin
    print(f"Q={Q}: vmin={vmin}, density 5/2^{vmin + 1} = {5 / 2 ** (vmin + 1)}")
assert [vmin_table[q] for q in [2, 3, 4, 5]] == [4, 5, 7, 7]

# ---------------------------------------------------------------- C
print("== C: Lambda_3, Nmax, squared-bound jmax ==")
lam_expect = {2: 1, 3: 3, 4: 3, 5: 15, 6: 15, 7: 105, 8: 105, 9: 315,
              10: 315, 11: 3465, 13: 45045, 17: 765765, 19: 14549535,
              23: 334639305, 25: 1673196525}
for T, val in lam_expect.items():
    assert Lambda3(T) == val, (T, Lambda3(T))
print("Lambda_3 spot values: OK")
for T in range(3, 31):
    Nm = Nmax(T)
    L = Lambda3(T)
    assert comb(Nm, 3) < L * L <= comb(Nm + 1, 3), T
print("Nmax(T) certificates C(Nmax,3)<L^2<=C(Nmax+1,3), T=3..30: OK")
for T in [6, 8, 10, 12, 17, 24, 25]:
    print(f"T={T}: Lambda={Lambda3(T)}, Nmax={Nmax(T)}")

def jmax_h0(Q, R):
    Nm = Nmax(R + 2 * Q - 2)
    return (Nm - R) // Q, Nm

print("-- Q=2, even R (h=0) --")
q2 = {}
for R in range(4, 30, 2):
    jm, Nm = jmax_h0(2, R)
    q2[R] = (jm, Nm)
    print(f"R={R}: T={R + 2}, Nmax={Nm}, jmax={jm}, "
          f"closedA(j<=5000)={jm <= 5000}, closedB(Nmax<=10^6)={Nm <= 10 ** 6}")
assert q2[14][0] == 1143 and q2[16][0] == 7597 and q2[22][1] == 875861
assert all(q2[R][1] <= 10 ** 6 for R in range(4, 24, 2))   # R<=22 closed by B
assert q2[24][1] == 2561033                                # R=24 first not closed

print("-- Q=3, R>=3 (h=0) --")
q3 = {}
for R in range(3, 26):
    jm, Nm = jmax_h0(3, R)
    q3[R] = (jm, Nm)
    print(f"R={R}: T={R + 4}, Nmax={Nm}, jmax={jm}, "
          f"closedA={jm <= 5000}, closedB={Nm <= 10 ** 6}")
assert q3[12][0] == 763 and q3[13][0] == 5065
assert all(q3[R][1] <= 10 ** 6 for R in range(3, 21))      # R<=20 closed by B
assert q3[21][1] == 2561033                                # R=21 first not closed

print("-- Q=4, even R>=4 (h=0) --")
q4 = {}
for R in range(4, 24, 2):
    jm, Nm = jmax_h0(4, R)
    q4[R] = (jm, Nm)
    print(f"R={R}: T={R + 6}, Nmax={Nm}, jmax={jm}, "
          f"closedA={jm <= 5000}, closedB={Nm <= 10 ** 6}")
assert q4[12][0] == 3799 and q4[18][1] == 875861
assert all(q4[R][1] <= 10 ** 6 for R in range(4, 20, 2))   # R<=18 closed by B
assert q4[20][1] == 2561033                                # R=20 first not closed

print("-- h=1 rows: exact jmax, certified by ok(jmax) and not ok(jmax+1) "
      "(monotonicity: Claim J3.3) --")
def jmax_h1(Q, R):
    T = R + 2 * (Q - 1)
    L = Lambda3(T)
    def ok(j):
        return comb(Q * j + R, 3) < (L * j) ** 2
    bound = int(24 * L * L // Q ** 3) + 2     # proved coarse bound, J3.3 remark
    lo, hi = 0, bound
    # predicate ok is (eventually) monotone; find exact max by scan to bound
    # (bounds here are <= 20000 for the rows scanned linearly; larger rows
    # are decided by the ok(5001) test only)
    if bound <= 200000:
        last = 0
        for j in range(1, bound + 1):
            if ok(j):
                last = j
        assert ok(last) and not ok(last + 1)
        return last, ok(5001)
    return None, ok(5001)

h1_expect = {(2, 1): 6, (2, 2): 5, (3, 0): 2, (3, 1): 50, (3, 2): 48,
             (4, 0): 21, (4, 1): 1033, (4, 2): 1032, (5, 0): 529,
             (5, 1): 4762, (5, 2): 4762, (6, 0): 2756}
for (Q, R), exp in h1_expect.items():
    jm, _ = jmax_h1(Q, R)
    assert jm == exp, (Q, R, jm)
    print(f"Q={Q} R={R}: jmax={jm} (<=5000: {jm <= 5000})")
for (Q, R) in [(6, 1), (6, 2), (7, 0), (7, 1), (7, 2), (8, 0)]:
    _, ok5001 = jmax_h1(Q, R)
    assert ok5001 is True, (Q, R)
    print(f"Q={Q} R={R}: ok(5001)=True (squared bound does NOT force j<=5000)")

# monotonicity sample for Claim J3.3 (proof is analytic; this is a check)
rng = random.Random(20261030)
for _ in range(20000):
    Q = rng.randint(2, 9)
    R = rng.randint(0, 2)
    j = rng.randint(3, 5000)
    if j <= R:
        continue
    L = Lambda3(R + 2 * (Q - 1))
    A = lambda jj: Fraction((L * jj) ** 2, comb(Q * jj + R, 3))
    assert A(j + 1) < A(j)
print("J3.3 monotonicity sample (20000 fixed-seed draws): OK")

# residual windows for the first non-closed h=0 rows of each Q
for (Q, R) in [(2, 24), (3, 21), (4, 20)]:
    jm, Nm = jmax_h0(Q, R)
    jlow = max(5001, (10 ** 6 - R) // Q + 1)
    print(f"first open row Q={Q} R={R}: j in [{jlow}, {jm}], n <= {Nm}")

# ---------------------------------------------------------------- D
print("== D: J4(a) refined comparison ==")
assert v2C(16) == 4 and V3(16) == 35 == comb(7, 3)
print("sharpness witness (16,7): v2=4, V3(16)=35=C(7,3): OK")
classif = {}
for j in range(5, 19):
    N = N3(j)
    vals = [(V3(n), n) for n in range(2 * j, N + 1)]
    mn = min(vals)
    holds = all(v > comb(j, 3) for v, _ in vals)
    classif[j] = (holds, mn, N)
    print(f"j={j}: C(j,3)={comb(j, 3)}, N={N}, min V3={mn[0]} at n={mn[1]}, "
          f"comparison closes pair on [2j,N]: {holds}")
assert classif[6][0] and classif[10][0]
assert [j for j in range(5, 19) if classif[j][0]] == [5, 6, 10]
assert classif[9][1] == (51, 18) and classif[17][1] == (187, 34)

# power-of-two witness for all j>=19 (checked to 2000; proof in J4.1)
for j in range(19, 2001):
    a = math.ceil(math.log2(2 * j))
    n = 2 ** a
    assert 2 * j <= n < 4 * j
    assert comb(n, 3) < comb(2 * j, 6)          # n <= N(3,j)
    assert V3(n) == (2 ** a - 1) * (2 ** (a - 1) - 1) // 3
    assert V3(n) <= comb(j, 3), (j, n)
print("power-of-two witness n=2^ceil(log2(2j)) in [2j,N], V3(n)<=C(j,3), "
      "for 19<=j<=2000: OK")

# ---------------------------------------------------------------- E
print("== E: J4(b) U-sharp tail comparison ==")
def tail_t(j):
    C = comb(j, 3)
    n = 2 * j
    while (n - 1) * (n - 2) <= 6 * C:
        n += 1
    return n
for j, exp in [(6, 13), (7, 17), (8, 20), (10, 29), (20, 85), (100, 987)]:
    assert tail_t(j) == exp, (j, tail_t(j))
    print(f"t({j}) = {exp}")
# the tail comparison alone closes the pair (uniformly at n=2j) iff j<=5:
for j in range(4, 60):
    uniform = (2 * j - 1) * (2 * j - 2) > 6 * comb(j, 3)
    assert uniform == (j <= 5), j
print("tail comparison uniform at n=2j holds iff j<=5 (checked j<60): OK")
# hybrid head placement of the J4.2 witnesses (needed for Claim J4.4(c)):
# every failing j in 7..18 has its minimum attained at n < t(j), and
# t(j) > 4j for all j>=19 (equivalent to D(j) = j(j-1)(j-2) -
# (4j-1)(4j-2) = j^3 - 19j^2 + 14j - 2 > 0; D(19)=264 and
# D'(j) = 3j^2 - 38j + 14 is positive and increasing for j>=19).
for j in range(7, 19):
    if j == 10:
        continue
    N = N3(j)
    mn_n = min(range(2 * j, N + 1), key=lambda nn: V3(nn))
    assert V3(mn_n) <= comb(j, 3) and mn_n < tail_t(j), j
for j in range(19, 2001):
    Dj = j * (j - 1) * (j - 2) - (4 * j - 1) * (4 * j - 2)
    assert Dj == j ** 3 - 19 * j ** 2 + 14 * j - 2 and Dj > 0, j
for j in range(19, 200):
    assert tail_t(j) > 4 * j, j
print("J4.4(c) head placement: witnesses < t(j) for 7<=j<=18 (j!=10); "
      "D(j)>0 for 19<=j<=2000; t(j)>4j for 19<=j<200: OK")
# hybrid: exact-v2 check on [2j, t(j)) gives unconditional closure of 6,10
for j in [6, 10]:
    t = tail_t(j)
    vals = [(n, V3(n)) for n in range(2 * j, t)]
    assert all(v > comb(j, 3) for _, v in vals)
    print(f"j={j}: hybrid interval [2j,t) = [{2 * j},{t}): {vals} all > C(j,3)")

# ---------------------------------------------------------------- F
print("== F: F1.13 thresholds (certified input, spot re-verified) ==")
def n0(j, v):
    n = 2 * j
    while comb(n, 3) <= (2 ** v) * comb(j, 3):
        n += 1
    return n
assert [n0(j, 4) for j in [6, 7, 8, 10, 20]] == [14, 17, 19, 24, 49]
assert [n0(j, 5) for j in [6, 7, 8, 10, 20]] == [17, 20, 24, 30, 62]
print("n0(j,4)=14,17,19,24,49 and n0(j,5)=17,20,24,30,62: OK")

print(f"ALL CHECKS PASSED in {time.time() - t0:.1f}s")
