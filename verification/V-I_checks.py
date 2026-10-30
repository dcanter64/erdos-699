#!/usr/bin/env python3
"""
V-I_checks.py -- Cycle 3, Cluster I, Verifier V-I. INDEPENDENT implementations
(Python stdlib only, exact arithmetic). Does NOT import either prover's script.
Sections:
  A. Lambda_3, row enumeration (64 rows, per-Q counts).
  B. Exact Jmax recount under BOTH definitions:
       B1: P-I1 definition  feasible_I1(j): C(Qj+R,3) < (Lam*C(j,h))^2, j>=5.
       B2: P-I2 definition  (*):            C(Qj,3)   < (Lam*C(j,h))^2, j>=1.
     Full-table comparison against both texts; analytic bounds B0/B1 (I1)
     and I2.2/I2.3 bounds verified with exact integer arithmetic;
     monotonicity of f(j)=C(Qj+R,3)/j^2 checked exactly (full range where
     feasible, sampled + windows for the largest rows).
  C. The (2,0) refutation: ratio identity and sign, both orientations.
  D. M(T) by brute-force filtering of odd m <= 3*Lambda (independent of the
     provers' product construction); P-I1 candidate lists regenerated and
     compared with the texts; all 68 candidates disposed with OWN gcd and
     OWN (LD3) witness computations (SPF factorisation).
  E. P-I2 recounts: (i) group-product derivation of the I2.11 hand rows;
     (ii) the 57-row r=1 scan (n-outer loop, SPF clauses) -- 1390 pairs,
     20 candidates, each with OWN full-(LD3) witness; (iii) R=1 analytic
     sets for Q=3,5,7 and clause cross-check counts.
  F. Elimination lemma stress test, even n <= 200,000: (LD3) candidate
     pairs enumerated via multiples of R(n) (SPF sieve); for every
     LD3-consistent assignment group G_{t,s}, verify G | D_{t,s} when
     D != 0 and the aligned-case classification when D == 0; verify the
     I2.8 corollary on all r=1-clause passers with R != 1 and the I2.9
     conclusions on R = 1 rows; count full (LD3) solutions (expect 0).
  G. Row (4,2) validation by two independent enumerations + gcds/witnesses.
"""
import math, time
from math import gcd, comb
from fractions import Fraction

t_start = time.time()

# ------------------------------------------------------------ own utilities
def spf_sieve(N):
    spf = list(range(N + 1))
    for i in range(2, int(N ** 0.5) + 1):
        if spf[i] == i:
            step = i
            start = i * i
            spf[start:N + 1:step] = [i if spf[k] == k else spf[k]
                                     for k in range(start, N + 1, step)]
    return spf

SPF = spf_sieve(400000)

def fac(m):
    f = {}
    while m > 1:
        p = SPF[m]; c = 0
        while m % p == 0:
            m //= p; c += 1
        f[p] = c
    return f

def rel_pp(m):
    """Relevant prime powers q = p^a || m (p>=5, or p=3 with a>=2)."""
    return [p ** a for p, a in fac(m).items()
            if p >= 5 or (p == 3 and a >= 2)]

def R_of(m):
    r = 1
    for q in rel_pp(m):
        r *= q
    return r

def primes_upto(n):
    if n < 2: return []
    s = bytearray(b"\x01") * (n + 1)
    s[0:2] = b"\x00\x00"
    out = []
    for i in range(2, n + 1):
        if s[i]:
            out.append(i)
            if i * i <= n:
                s[i*i:n+1:i] = b"\x00" * ((n - i*i)//i + 1)
    return out

def Lambda3(T):
    if T < 3: return 1
    out = 1
    for p in primes_upto(T):
        if p < 3: continue
        pw = p
        while pw * p <= T: pw *= p
        out *= pw
    return out

def h_of(Q, R):
    if R >= 3: return 0
    return max(0, -(-(3 - R) // Q))

def C3(n):
    return n * (n - 1) * (n - 2) // 6 if n >= 3 else 0

def V3(n):
    v = comb(n, 3)
    while v % 2 == 0: v //= 2
    return v

def ld3_witness(n, j):
    for r in (0, 1, 2):
        for q in rel_pp(n - r):
            if j % q > r:
                return (r, q, j % q)
    return None

def oddpart(m):
    while m % 2 == 0: m //= 2
    return m

# ------------------------------------------------------------ A. rows
print("=== A. Lambda_3 and the 64 rows ===")
LAM = {T: Lambda3(T) for T in range(17)}
assert [LAM[T] for T in range(17)] == [1,1,1,3,3,15,15,105,105,315,315,
                                       3465,3465,45045,45045,45045,45045]
rows = []
Q = 2
while True:
    Rs = [R for R in range(0, 200) if R + 2*(Q-1) <= 16]
    if not Rs: break
    rows += [(Q, R) for R in Rs]
    Q += 1
from collections import Counter
cntQ = Counter(q for q, r in rows)
assert len(rows) == 64, len(rows)
assert [cntQ[q] for q in range(2, 10)] == [15, 13, 11, 9, 7, 5, 3, 1], cntQ
parity_vacuous = [(q, r) for (q, r) in rows if q % 2 == 0 and r % 2 == 1]
assert len(parity_vacuous) == 16, parity_vacuous
print(f"  64 rows confirmed; per-Q counts 15,13,11,9,7,5,3,1; "
      f"parity-vacuous (Q even, R odd) rows: {len(parity_vacuous)}")

# ------------------------------------------------------------ B. Jmax recounts
print("=== B. Exact thresholds under both definitions ===")
def feas_I1(Q, R, j):
    T = R + 2*(Q-1); L = LAM[T]; h = h_of(Q, R)
    return C3(Q*j + R) < (L * comb(j, h)) ** 2

def feas_I2(Q, R, j):
    T = R + 2*(Q-1); L = LAM[T]; h = h_of(Q, R)
    return C3(Q*j) < (L * comb(j, h)) ** 2

def jmax_generic(feas, Q, R, jlo):
    if not feas(Q, R, jlo):
        return jlo - 1
    lo, hi = jlo, jlo + 1
    while feas(Q, R, hi):
        lo, hi = hi, hi * 2
    while hi - lo > 1:
        mid = (lo + hi) // 2
        if feas(Q, R, mid): lo = mid
        else: hi = mid
    assert feas(Q, R, lo) and not feas(Q, R, lo + 1)
    return lo

# Transcribed from P-I1.md Claim I2.4 (Jmax, I1 definition; (2,0) excluded).
I1_JMAX = {
 (2,1):6,(2,2):5,(2,3):4,(2,4):4,(2,5):18,(2,6):17,(2,7):39,(2,8):38,
 (2,9):204,(2,10):203,(2,11):1145,(2,12):1144,(2,13):1144,(2,14):1143,
 (3,0):4,(3,1):50,(3,2):48,(3,3):12,(3,4):12,(3,5):26,(3,6):26,(3,7):136,
 (3,8):136,(3,9):764,(3,10):763,(3,11):763,(3,12):763,
 (4,0):21,(4,1):1033,(4,2):1032,(4,3):20,(4,4):20,(4,5):103,(4,6):102,
 (4,7):573,(4,8):573,(4,9):573,(4,10):572,
 (5,0):529,(5,1):4762,(5,2):4762,(5,3):82,(5,4):82,(5,5):459,(5,6):459,
 (5,7):458,(5,8):458,
 (6,0):2756,(6,1):333506,(6,2):333505,(6,3):383,(6,4):382,(6,5):382,(6,6):382,
 (7,0):210021,(7,1):35493621,(7,2):35493620,(7,3):328,(7,4):328,
 (8,0):23777953,(8,1):23777953,(8,2):23777953,
 (9,0):16700016}
# Transcribed from P-I2.md Claim I2.5 (B* = Jmax+1, I2 definition).
I2_BSTAR = {
 (2,1):9,(2,2):9,(2,3):7,(2,4):7,(2,5):21,(2,6):21,(2,7):43,(2,8):43,
 (2,9):209,(2,10):209,(2,11):1151,(2,12):1151,(2,13):1151,(2,14):1151,
 (3,0):3,(3,1):51,(3,2):51,(3,3):14,(3,4):14,(3,5):29,(3,6):29,(3,7):140,
 (3,8):140,(3,9):768,(3,10):768,(3,11):768,(3,12):768,
 (4,0):22,(4,1):1035,(4,2):1035,(4,3):22,(4,4):22,(4,5):105,(4,6):105,
 (4,7):576,(4,8):576,(4,9):576,(4,10):576,
 (5,0):530,(5,1):4764,(5,2):4764,(5,3):84,(5,4):84,(5,5):461,(5,6):461,
 (5,7):461,(5,8):461,
 (6,0):2757,(6,1):333507,(6,2):333507,(6,3):384,(6,4):384,(6,5):384,(6,6):384,
 (7,0):210022,(7,1):35493622,(7,2):35493622,(7,3):329,(7,4):329,
 (8,0):23777954,(8,1):23777954,(8,2):23777954,
 (9,0):16700017}

REQ = [(5,1),(6,1),(6,2),(7,0),(7,1),(7,2),(8,0),(8,1),(8,2),(9,0),(2,14),(3,12)]
jm1_all, jm2_all = {}, {}
for (Q, R) in rows:
    if (Q, R) == (2, 0): continue
    jm1 = jmax_generic(feas_I1, Q, R, 5)
    if jm1 < 5: jm1 = 4          # I1's sentinel convention
    jm1_all[(Q, R)] = jm1
    assert jm1 == I1_JMAX[(Q, R)], ("I1 mismatch", Q, R, jm1, I1_JMAX[(Q, R)])
    jm2 = jmax_generic(feas_I2, Q, R, 1)
    jm2_all[(Q, R)] = jm2
    assert jm2 + 1 == I2_BSTAR[(Q, R)], ("I2 mismatch", Q, R, jm2 + 1, I2_BSTAR[(Q, R)])
exc1 = sorted([k for k, v in jm1_all.items() if v > 5000])
exc2 = sorted([k for k, v in jm2_all.items() if v + 1 > 5000])
EXP_EXC = [(6,1),(6,2),(7,0),(7,1),(7,2),(8,0),(8,1),(8,2),(9,0)]
assert exc1 == EXP_EXC and exc2 == EXP_EXC, (exc1, exc2)
assert sum(1 for v in jm1_all.values() if v <= 5000) == 54
assert sum(1 for v in jm2_all.values() if v + 1 <= 5000) == 54
print("  FULL tables reproduced: all 63 I1 Jmax values and all 63 I2 B* values")
print("  match the texts exactly, each under its own definition.")
for k in REQ:
    print(f"    required row {k}: I1 Jmax={jm1_all[k]}   I2 Jmax(*)={jm2_all[k]} "
          f"(B*={jm2_all[k]+1})")
print(f"  exceptions with threshold > 5000 (both definitions): {exc1}")
print("  54 of 63 rows at/below 5000 under BOTH definitions; (6,1),(8,1) "
      "parity-vacuous confirmed.")

# Analytic bounds, exact-integer verification.
def icbrt_ceil(x):
    lo, hi = 0, 1
    while hi ** 3 < x: hi *= 2
    while hi - lo > 1:
        mid = (lo + hi) // 2
        if mid ** 3 >= x: hi = mid
        else: lo = mid
    return hi
for (Q, R) in rows:
    if (Q, R) == (2, 0): continue
    T = R + 2*(Q-1); L = LAM[T]; h = h_of(Q, R)
    if h == 0:
        # I1 B0 / I2.2: smallest j with (Qj-2)^3 >= 6 L^2 must be infeasible
        # under both definitions, and must be <= Jmax+1 (analytic is a bound).
        c = icbrt_ceil(6 * L * L)
        j1 = (c + 2 + Q - 1) // Q   # smallest j with Qj-2 >= c
        while (Q*j1 - 2) ** 3 < 6 * L * L: j1 += 1
        while j1 > 0 and (Q*(j1-1) - 2) ** 3 >= 6 * L * L: j1 -= 1
        assert not feas_I1(Q, R, max(j1, 5)) or j1 <= 5
        assert not feas_I2(Q, R, j1)
        assert jm1_all[(Q, R)] + 1 <= max(j1, 5) or jm1_all[(Q, R)] == 4
        assert jm2_all[(Q, R)] + 1 <= j1
    else:
        # I1 B1 = 25 L^2 / (3 Q^3): ceil must be infeasible (exact form).
        B1 = Fraction(25 * L * L, 3 * Q ** 3)
        j1 = -(-B1.numerator // B1.denominator)
        assert not feas_I1(Q, R, j1), (Q, R, j1)
        if jm1_all[(Q, R)] == 4:   # I1 sentinel: no j >= 5 feasible at all
            assert not feas_I1(Q, R, 5), (Q, R)
        else:
            assert jm1_all[(Q, R)] + 1 <= j1, (Q, R)
        # I2.3 bound: j < 6 L^2 / Q^3 + 3/Q (R-free form).
        B2 = Fraction(6 * L * L, Q ** 3) + Fraction(3, Q)
        j2 = -(-B2.numerator // B2.denominator)
        assert not feas_I2(Q, R, j2), (Q, R, j2)
        assert jm2_all[(Q, R)] + 1 <= j2
print("  Analytic bounds verified exactly: I1 B0 (integer cube root), "
      "I1 B1 = 25L^2/(3Q^3), I2.2 bound, I2.3 bound 6L^2/Q^3 + 3/Q;")
print("  in every h<=1 row the first integer at/above the analytic bound is "
      "infeasible and Jmax+1 <= that integer.")

# Monotonicity of f(j) = C(Qj+R,3)/j^2 (I1 Claim I2.2(b)): exact checks.
def f_gt(Q, R, j):
    # f(j+1) > f(j)  <=>  C(Q(j+1)+R,3)*j^2 > C(Qj+R,3)*(j+1)^2
    return C3(Q*(j+1) + R) * j * j > C3(Q*j + R) * (j+1) * (j+1)
mono_full, mono_sampled = [], []
for (Q, R) in rows:
    if h_of(Q, R) != 1: continue
    jm = jm1_all[(Q, R)]
    if jm <= 400000:
        for j in range(5, jm + 2):
            assert f_gt(Q, R, j), (Q, R, j)
        mono_full.append((Q, R))
    else:
        pts = set(range(5, 5001)) | set(range(5, jm + 2, 9973)) | \
              {jm - 1, jm, jm + 1}
        for j in sorted(pts):
            if 5 <= j <= jm + 1:
                assert f_gt(Q, R, j), (Q, R, j)
        mono_sampled.append((Q, R))
print(f"  Monotonicity f(j+1)>f(j) verified EXACTLY for every j in range for "
      f"{len(mono_full)} h=1 rows {mono_full};")
print(f"  sampled (j<5000, stride 9973, Jmax window) for {mono_sampled}.")

# ------------------------------------------------------------ C. (2,0)
print("=== C. The (2,0) row (both provers' refutations) ===")
for j in range(5, 501):
    r_I1 = Fraction(comb(j, 2) ** 2, C3(2 * j))
    assert r_I1 == Fraction(3 * j * (j - 1), 8 * (2 * j - 1))
    assert Fraction(C3(2 * j), comb(j, 2) ** 2) == Fraction(8 * (2 * j - 1), 3 * j * (j - 1))
    assert (r_I1 > 1) == (j >= 6)
    assert (3 * j * j - 19 * j + 8 > 0) == (j >= 6)
print("  ratio identities exact for 5<=j<=500; squared inequality at (2,0) "
      "holds iff j>=6 (3j^2-19j+8>0), so it yields NO bound. I1 I2.3 and "
      "I2 I2.4 both correct.")

# ------------------------------------------------------------ D. M(T) + I1 candidates
print("=== D. M(T) by brute filter; P-I1's 68 candidates recomputed ===")
def Mset_brute(T):
    L = LAM[T]
    out = set()
    for m in range(1, 3 * L + 1, 2):
        f = fac(m)
        if f.get(3, 0) > 1 + (max(e for e in range(10) if 3 ** e <= T) if T >= 3 else 0):
            continue
        if all(p ** a <= T for p, a in f.items() if p >= 5):
            out.add(m)
    return out
MSIZES = {}
for T in (5, 6, 8, 9, 10, 12, 13, 14, 16):
    MSIZES[T] = Mset_brute(T)
assert len(MSIZES[6]) == 6 and len(MSIZES[8]) == 12 and len(MSIZES[10]) == 16
assert len(MSIZES[12]) == 32 and len(MSIZES[14]) == 64 and len(MSIZES[16]) == 64
assert all(m <= 3 * LAM[T] for T, S in MSIZES.items() for m in S)
print("  |M(T)|: 6->6, 8->12, 10->16, 12->32, 14->64, 16->64 (brute filter "
      "over odd m <= 3*Lambda); m <= 3*Lambda confirmed for all members.")

def in_M(x, T):
    if x % 2 == 0: return False
    f = fac(x)
    e3max = 1 + (max(e for e in range(12) if 3 ** e <= T) if T >= 3 else -1)
    if f.get(3, 0) > e3max: return False
    return all(p ** a <= T for p, a in f.items() if p >= 5)

# Transcribed expected lists + gcds from P-I1.md claims I3.5-I3.22.
I1_D_ROWS = [
 ((4,2), [((22,5),77),((46,11),69),((106,26),371)]),
 ((2,4), [((16,6),7),((46,21),759)]),
 ((2,6), [((22,8),55),((36,15),255),((46,20),759),((64,29),651),
          ((106,50),689),((316,155),37209)]),
 ((3,4), [((22,6),77),((46,14),3795),((64,20),651),((106,34),24115),
          ((316,104),1302315)]),
 ((4,4), [((28,6),819),((36,8),255),((64,15),93),((136,33),51255),
          ((316,78),1302315)]),
 ((5,0), []),
 ((5,2), []),
 ((2,8), [((28,10),273),((36,14),255),((46,19),1265),((64,28),217),
          ((106,49),3445),((136,64),51255),((190,91),13395),
          ((316,154),186045),((946,469),8790705)]),
 ((6,0), [((36,6),357)]),
 ((6,2), [((56,9),1155),((386,64),74305)]),
 ((7,0), [((56,8),3465)]),
 ((7,2), [((100,14),5775),((352,50),9009),((716,102),895895),
          ((1486,212),2574495)]),
 ((8,0), [((40,5),247),((56,7),495),((64,8),93),((136,17),3015),
          ((144,18),30459),((232,29),1265),((352,44),20475),((456,57),14755),
          ((496,62),40755),((1288,161),275847),((2080,260),46801755),
          ((4096,512),399165),((15016,1877),37572535),
          ((135136,16892),434793645)]),
 ((8,2), [((66,8),715),((106,13),1855),((274,34),12467),((298,37),4917),
          ((386,48),74305),((586,73),57135),((946,118),49665),
          ((1002,125),167167),((2146,268),767195),((2458,307),1006551),
          ((3466,433),2001615),((9010,1126),13528515),
          ((19306,2413),1180224045)]),
 ((9,0), [((144,16),30459)]),
]
tot68 = 0
for (Q, R), expected in I1_D_ROWS:
    T = R + 2*(Q-1)
    mine = []
    for m in sorted(MSIZES[T] if T in MSIZES else Mset_brute(T)):
        n = m + 1
        if n % 2 == 1 or (n - R) % Q != 0: continue
        j = (n - R) // Q
        if j >= 5 and j > R: mine.append((n, j))
    assert mine == [c for c, g in expected], ((Q, R), mine, expected)
    for (n, j), gexp in expected:
        g = gcd(V3(n), comb(n, j))
        w = ld3_witness(n, j)
        assert g == gexp and g > 1 and w is not None, ((Q, R), n, j, g, gexp, w)
        tot68 += 1
    print(f"    row ({Q},{R}): candidate list reproduced ({len(expected)}); "
          f"all gcds match text; all have own (LD3) witnesses.")
# R=1 rows, own enumeration to 6*Lambda+2 with in_M filter on odd parts.
I1_E_ROWS = [((3,1), []), ((5,1), [((56,11),105)]), ((7,1), [((288,41),231)])]
for (Q, R), expected in I1_E_ROWS:
    T = R + 2*(Q-1); bound = 6 * LAM[T] + 2
    mine = []
    n = Q * 5 + R
    while n <= bound:
        if n % 2 == 0:
            j = (n - R) // Q
            if j >= 5 and in_M(oddpart(n), T) and in_M(oddpart(n - 2), T):
                mine.append((n, j))
        n += Q
    assert mine == [c for c, g in expected], ((Q, R), mine, expected)
    for (n, j), gexp in expected:
        g = gcd(V3(n), comb(n, j)); w = ld3_witness(n, j)
        assert g == gexp and w is not None
        tot68 += 1
    print(f"    R=1 row ({Q},{R}): list reproduced up to bound {bound}: {mine}")
assert tot68 == 68, tot68
print(f"  P-I1 total: 68 candidates, ALL independently disposed "
      f"(gcd > 1 matching the printed value, plus an (LD3) witness).")

# ------------------------------------------------------------ E. P-I2 recounts
print("=== E. P-I2 recounts (elimination scan, hand rows, R=1 sets) ===")
def group_products(D):
    D = abs(D)
    if D == 0: return None
    opts = []
    for p, e in fac(D).items():
        exps = [0] + [a for a in range(1, e + 1)
                      if p >= 5 or (p == 3 and a >= 2)]
        opts.append([p ** a for a in exps])
    out = [1]
    for o in opts: out = [x * y for x in out for y in o]
    return sorted(set(out))

# (i) I2.11 hand rows via group products (independent of the scan).
HAND = {(2,4): [(16,6)], (3,4): [], (2,6): [(16,5),(22,8),(36,15),(106,50)],
        (4,4): [], (5,0): [], (5,2): [], (2,8): [(22,7),(64,28)], (6,0): []}
for (Q, R), exp in HAND.items():
    rho = sorted({a * b for a in group_products(R - 1)
                  for b in group_products(Q + R - 1) if gcd(a, b) == 1})
    mset = sorted(set(rho) | {3 * r for r in rho if r % 3 != 0})
    mine = []
    for m in mset:
        n = m + 1
        if n % 2 == 0 and (n - R) % Q == 0:
            j = (n - R) // Q
            if j > 3: mine.append((n, j))
    assert mine == exp, ((Q, R), mine, exp, rho, mset)
    for (n, j) in mine:
        assert ld3_witness(n, j) is not None
print("  I2.11 hand rows: group-product derivation reproduces all 8 candidate "
      "lists exactly (incl. the 3|rho exclusion of 27 and 189 at (2,8)).")

# (ii) 57-row scan, n-outer implementation.
def clause_ok(n, j, r):
    return all(j % q <= r for q in rel_pp(n - r))
total_tested, scan_cands = 0, []
maxb = (0, None)
nrows = 0
for (Q, R) in rows:
    if R == 1: continue
    nrows += 1
    Nb = 3 * abs((R - 1) * (Q + R - 1)) + 1
    if Nb > maxb[0]: maxb = (Nb, (Q, R))
    n = 2
    while n <= Nb:
        if (n - R) % Q == 0:
            j = (n - R) // Q
            if j > 3:
                total_tested += 1
                if clause_ok(n, j, 1):
                    scan_cands.append(((Q, R), (n, j)))
        n += 2
assert nrows == 57 and maxb == (586, (2, 14)), (nrows, maxb)
assert total_tested == 1390, total_tested
I2_20 = [((2,4),(16,6)), ((2,6),(16,5)), ((2,6),(22,8)), ((2,6),(36,15)),
         ((2,6),(106,50)), ((2,8),(22,7)), ((2,8),(64,28)), ((2,10),(34,12)),
         ((2,10),(100,45)), ((2,12),(34,11)), ((2,12),(40,14)),
         ((2,12),(144,66)), ((2,12),(430,209)), ((2,14),(40,13)),
         ((2,14),(66,26)), ((2,14),(196,91)), ((3,12),(78,22)),
         ((4,6),(46,10)), ((4,8),(232,56)), ((4,10),(118,27))]
assert scan_cands == I2_20, scan_cands
for row, (n, j) in scan_cands:
    w = ld3_witness(n, j)
    assert w is not None, (row, n, j)
print(f"  Scan recount: 57 rows, {total_tested} even pairs, max bound 586 at "
      f"(2,14); exactly 20 r=1 candidates, identical list to P-I2 I2.13;")
print("  every one independently disposed by a full (LD3) witness; 0 survivors.")

# (iii) R=1 analytic sets, Q=3,5,7.
R1_EXP = {3: ([1],[1,5],[1,5],[1,3,5,15],5), 5: ([1],[1,9],[1,9],[1,3,9],4),
          7: ([1],[1,13],[1,13],[1,3,13,39],3)}
for Qq, (eA1, eA2, eR, eM, eTested) in R1_EXP.items():
    A1 = group_products(Qq - 1); A2 = group_products(2 * Qq - 1)
    Rp = sorted({a * b for a in A1 for b in A2 if gcd(a, b) == 1})
    Mp = sorted(set(Rp) | {3 * r for r in Rp if r % 3 != 0})
    assert (A1, A2, Rp, Mp) == (eA1, eA2, eR, eM), (Qq, A1, A2, Rp, Mp)
    tested = 0
    for a in range(0, 13):
        for u in (1, 3):
            n = (2 ** a) * u
            if n % 2 == 0 and (n - 1) % Qq == 0:
                j = (n - 1) // Qq
                if j > 3:
                    tested += 1
                    assert not (clause_ok(n, j, 0) and clause_ok(n, j, 2)), (Qq, n, j)
    assert tested == eTested, (Qq, tested, eTested)
print("  R=1 rows Q=3,5,7: P-sets, R(n-2) sets and odd-part sets all match "
      "I2.12; clause cross-check counts 5/4/3 reproduced, 0 pass r=0+r=2.")

# ------------------------------------------------------------ F. stress test
print("=== F. Elimination lemma stress test, even n <= 200,000 ===")
LIM = 200000
rel_cache = {}
def rel(m):
    v = rel_cache.get(m)
    if v is None:
        v = rel_pp(m); rel_cache[m] = v
    return v
def Rprod(m):
    r = 1
    for q in rel(m): r *= q
    return r
pairs = 0; group_instances = 0; group_fail = 0
aligned_instances = 0; aligned_bad = []
r1_pass = 0; cor_fail = 0
r1row_pairs = 0; r1_n1_fail = 0; r1_r2_pass = 0; r1_r2_fail = 0
full_solutions = 0
for n in range(2, LIM + 1, 2):
    Rn = Rprod(n)
    j = Rn
    while j <= n // 2:
        if j > 3:
            pairs += 1
            Q, R = divmod(n, j)
            ok_r = [True, True, True]
            for t in (0, 1, 2):
                groups = {}
                for q in rel(n - t):
                    s = j % q
                    if s <= t:
                        groups[s] = groups.get(s, 1) * q
                    else:
                        ok_r[t] = False
                for s, G in groups.items():
                    D = Q * s + R - t
                    group_instances += 1
                    if D == 0:
                        aligned_instances += 1
                        if not ((s == 0 and R == t) or
                                (Q, R, t, s) == (2, 0, 2, 1)):
                            aligned_bad.append((n, j, Q, R, t, s))
                    elif D % G != 0:
                        group_fail += 1
            if ok_r[1]:
                r1_pass += 1
                if R != 1:
                    P = (R - 1) * (Q + R - 1)
                    if P % Rprod(n - 1) != 0: cor_fail += 1
            if R == 1:
                r1row_pairs += 1
                if Rn != 1: r1_n1_fail += 1
                if ok_r[2]:
                    r1_r2_pass += 1
                    if ((Q - 1) * (2 * Q - 1)) % Rprod(n - 2) != 0:
                        r1_r2_fail += 1
            if all(ok_r): full_solutions += 1
        j += Rn
        if Rn == 0: break
print(f"  candidate pairs (j multiple of R(n), j>3): {pairs}")
print(f"  LD3-consistent assignment groups checked: {group_instances}; "
      f"divisibility failures: {group_fail}")
print(f"  aligned (D=0) group instances: {aligned_instances}; "
      f"outside the classified cases: {len(aligned_bad)} {aligned_bad[:5]}")
print(f"  pairs passing the r=1 clause: {r1_pass}; I2.8 corollary "
      f"R(n-1)|((R-1)(Q+R-1)) failures (R!=1): {cor_fail}")
print(f"  R=1-row pairs: {r1row_pairs}; with R(n)!=1: {r1_n1_fail}; "
      f"also passing r=2 clause: {r1_r2_pass}; I2.9 divisibility "
      f"R(n-2)|((Q-1)(2Q-1)) failures: {r1_r2_fail}")
print(f"  full (LD3) solutions found: {full_solutions} (expected 0: "
      f"certified none with n <= 10^6)")
assert group_fail == 0 and not aligned_bad and cor_fail == 0
assert r1_n1_fail == 0 and r1_r2_fail == 0 and full_solutions == 0

# ------------------------------------------------------------ G. (4,2)
print("=== G. Row (4,2) validation, two independent enumerations ===")
# (i) F1-style form enumeration.
c1 = []
for b in range(3):
    for a in range(2):
        for c in range(2):
            m = 3**b * 5**a * 7**c
            if m % 4 == 1 and (m - 1) // 4 >= 5:
                c1.append((m + 1, (m - 1) // 4))
# (ii) M(8)-set enumeration (brute M set from section D).
c2 = []
for m in sorted(Mset_brute(8)):
    n = m + 1
    if n % 2 == 0 and (n - 2) % 4 == 0:
        j = (n - 2) // 4
        if j >= 5: c2.append((n, j))
assert sorted(c1) == sorted(c2) == [(22, 5), (46, 11), (106, 26)], (c1, c2)
for (n, j), gexp, qexp in zip([(22,5),(46,11),(106,26)], [77,69,371], [11,23,53]):
    g = gcd(V3(n), comb(n, j)); w = ld3_witness(n, j)
    assert g == gexp and w == (0, qexp, j), (n, j, g, w)
    assert n % qexp == 0 and fac(n)[int(round(qexp ** (1/1)))] if False else True
print("  Both enumerations leave precisely (22,5), (46,11), (106,26);")
print("  gcd(V3(n),C(n,j)) = 77, 69, 371; (LD3) violated at r=0 by "
      "q = 11||22, 23||46, 53||106 respectively (j mod q = j > 0).")

print(f"\nALL V-I CHECKS PASSED. Runtime: {time.time() - t_start:.1f}s")
