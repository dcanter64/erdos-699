#!/usr/bin/env python3
"""
P-I2 checks (Cycle 3, Cluster I, prover I2).
Python standard library only, exact integer arithmetic.

Sections:
  A. Lambda_3 table and the exact Prop. 4.1 squared-bound thresholds B*(Q,R)
     for every row with T <= 16 (binary search on a proved-monotone
     inequality; endpoint conditions asserted for every row).
  B. Validation: the (4,2) analysis of F1.11, reproduced exactly.
  C. The elimination bound for rows R != 1 (T <= 16): scan every even pair
     up to the proved bound, collect the pairs passing the r=1 (LD3)
     clause, and dispose of each by a full (LD3) witness.
  D. Rows R = 1, Q = 3, 5, 7: the analytic candidate enumeration
     (n = 2^a * u form and the odd part of n-2), plus a clause
     cross-check.
  E. The specific hand-analysed rows: r=1-clause candidate lists.
"""
import math
from math import gcd

# ---------------------------------------------------------------- utilities

def primes_upto(n):
    sieve = bytearray(b"\x01") * (n + 1)
    ps = []
    for i in range(2, n + 1):
        if sieve[i]:
            ps.append(i)
            if i * i <= n:
                sieve[i * i:n + 1:i] = b"\x00" * ((n - i * i) // i + 1)
    return ps

def lambda3(T):
    if T < 3:
        return 1
    out = 1
    for p in primes_upto(T):
        if p < 3:
            continue
        pw = p
        while pw * p <= T:
            pw *= p
        out *= pw
    return out

def C3(n):
    return n * (n - 1) * (n - 2) // 6 if n >= 3 else 0

def factorize(m):
    out = {}
    x = m
    d = 2
    while d * d <= x:
        while x % d == 0:
            out[d] = out.get(d, 0) + 1
            x //= d
        d += 1 if d == 2 else 2
    if x > 1:
        out[x] = out.get(x, 0) + 1
    return out

def relevant_prime_powers(m):
    """Relevant q = p^a || m: p >= 5 (any a >= 1) or p = 3, a >= 2."""
    return [p ** a for p, a in factorize(m).items()
            if p >= 5 or (p == 3 and a >= 2)]

def ld3_clause(n, j, r):
    return all(j % q <= r for q in relevant_prime_powers(n - r))

def ld3_witness(n, j):
    """First (r, q) with j mod q > r, or None if (LD3) holds."""
    for r in range(3):
        for q in relevant_prime_powers(n - r):
            if j % q > r:
                return (r, q)
    return None

def V3(n):
    v = math.comb(n, 3)
    while v % 2 == 0:
        v //= 2
    return v

def divisors(n):
    n = abs(n)
    ds = []
    for d in range(1, int(n ** 0.5) + 1):
        if n % d == 0:
            ds.append(d)
            if d * d != n:
                ds.append(n // d)
    return sorted(ds)

# ---------------------------------------------------------------- section A

print("=== A. Lambda_3 and Prop.4.1 squared thresholds, T <= 16 ===")
LAM = {T: lambda3(T) for T in range(17)}
print("Lambda_3(T), T=0..16:", [LAM[T] for T in range(17)])
assert [LAM[T] for T in range(17)] == \
    [1, 1, 1, 3, 3, 15, 15, 105, 105, 315, 315, 3465, 3465,
     45045, 45045, 45045, 45045]

def h_of(Q, R):
    if (Q, R) == (2, 0):
        return 2
    return 0 if R >= 3 else 1

def ineq_holds(Q, Lam, h, j):
    if j <= 0:
        return False
    if h == 0:
        return C3(Q * j) < Lam * Lam
    if h == 1:
        return C3(Q * j) < (Lam * j) ** 2
    raise ValueError

def jmax(Q, Lam, h):
    lo, hi = 0, 1
    while ineq_holds(Q, Lam, h, hi):
        hi *= 2
    while hi - lo > 1:
        mid = (lo + hi) // 2
        if ineq_holds(Q, Lam, h, mid):
            lo = mid
        else:
            hi = mid
    # endpoint conditions (valid given the monotonicity proved in P-I2.md)
    assert lo == 0 or ineq_holds(Q, Lam, h, lo)
    assert not ineq_holds(Q, Lam, h, lo + 1)
    return lo

rowsA = []
for Q in range(2, 20):
    R = 0
    while R + 2 * (Q - 1) <= 16:
        T = R + 2 * (Q - 1)
        h = h_of(Q, R)
        if h == 2:
            rowsA.append((T, Q, R, h, LAM[T], None, None))
        else:
            J = jmax(Q, LAM[T], h)
            rowsA.append((T, Q, R, h, LAM[T], J, J + 1))  # B* = Jmax + 1
        R += 1

assert len(rowsA) == 64
h0 = [r for r in rowsA if r[3] == 0]
h1 = [r for r in rowsA if r[3] == 1]
h2 = [r for r in rowsA if r[3] == 2]
assert len(h0) == 42 and len(h1) == 21 and len(h2) == 1 and h2[0][1:3] == (2, 0)
assert all(r[6] <= 5000 for r in h0), "every h=0 row must have B* <= 5000"
h1_le = [(r[1], r[2], r[6]) for r in h1 if r[6] <= 5000]
h1_gt = [(r[1], r[2], r[6]) for r in h1 if r[6] > 5000]
assert h1_le == [(2, 1, 9), (2, 2, 9), (3, 0, 3), (3, 1, 51), (3, 2, 51),
                 (4, 0, 22), (4, 1, 1035), (4, 2, 1035), (5, 0, 530),
                 (5, 1, 4764), (5, 2, 4764), (6, 0, 2757)], h1_le
assert h1_gt == [(6, 1, 333507), (6, 2, 333507), (7, 0, 210022),
                 (7, 1, 35493622), (7, 2, 35493622), (8, 0, 23777954),
                 (8, 1, 23777954), (8, 2, 23777954), (9, 0, 16700017)], h1_gt
for r in rowsA:
    print(f"  T={r[0]:2d} (Q,R)=({r[1]},{r[2]:2d}) h={r[3]} "
          f"Lambda={r[4]:6d} Jmax={r[5]} B*={r[6]}")
print(f"  rows: {len(rowsA)} total; h=0: {len(h0)} (all B* <= 5000); "
      f"h=1: {len(h1)} ({len(h1_le)} with B* <= 5000, {len(h1_gt)} with "
      f"B* > 5000); h=2: {len(h2)} (the (2,0) row only)")

# ---------------------------------------------------------------- section B

print("=== B. Validation: the (4,2) illustration of F1.11 ===")
cands42 = []
for b in range(3):
    for a in range(2):
        for c in range(2):
            m = 3 ** b * 5 ** a * 7 ** c
            if m % 4 == 1:
                j = (m - 1) // 4
                if j >= 5:
                    cands42.append((m + 1, j))
cands42.sort()
assert cands42 == [(22, 5), (46, 11), (106, 26)], cands42
gcds42 = []
for (n, j) in cands42:
    g = gcd(V3(n), math.comb(n, j))
    gcds42.append(g)
    w = ld3_witness(n, j)
    print(f"  (n,j)=({n},{j}): gcd(V3(n),C(n,j))={g}, (LD3) witness (r,q)={w}")
    assert w is not None and w[0] == 0  # each is killed already at r = 0
assert gcds42 == [77, 69, 371], gcds42
print("  reproduced exactly: candidates (22,5), (46,11), (106,26); "
      "gcds 77, 69, 371")

# ------------------------------------------------- sections C and E (R != 1)

def row_bound_Rne1(Q, R):
    return 3 * abs((R - 1) * (Q + R - 1)) + 1

def r1_candidates(Q, R):
    """Even pairs (n,j) in row (Q,R), j > 3, n <= proved bound, passing the
    r=1 clause of (LD3).  Any (LD3) solution in the row is among them."""
    Nb = row_bound_Rne1(Q, R)
    out = []
    tested = 0
    j = 4
    while Q * j + R <= Nb:
        n = Q * j + R
        if n % 2 == 0:
            tested += 1
            if ld3_clause(n, j, 1):
                out.append((n, j))
        j += 1
    return Nb, tested, out

print("=== C. Elimination bound scan, rows R != 1 with T <= 16 ===")
total_tested = 0
all_cands = []
max_bound = (0, None)
n_Rne1_rows = 0
for Q in range(2, 10):
    R = 0
    while R + 2 * (Q - 1) <= 16:
        if R != 1:
            n_Rne1_rows += 1
            Nb, tested, cand = r1_candidates(Q, R)
            total_tested += tested
            if Nb > max_bound[0]:
                max_bound = (Nb, (Q, R))
            for c in cand:
                w = ld3_witness(*c)
                assert w is not None, f"unexpected (LD3) survivor {c}"
                all_cands.append(((Q, R), c, w))
        R += 1
assert n_Rne1_rows == 57
assert max_bound == (586, (2, 14)), max_bound
assert len(all_cands) == 20, all_cands
for row, c, w in all_cands:
    print(f"  row {row}: candidate (n,j)={c}, killed by (LD3) witness "
          f"(r,q)={w}")
print(f"  {n_Rne1_rows} rows; {total_tested} even pairs tested up to the "
      f"per-row bounds (max bound {max_bound[0]} at {max_bound[1]}); "
      f"{len(all_cands)} r=1-clause candidates, all killed by full (LD3); "
      f"0 survivors")

print("=== E. Hand-analysed rows: r=1-clause candidate lists ===")
expected_E = {
    (2, 4): [(16, 6)],
    (2, 6): [(16, 5), (22, 8), (36, 15), (106, 50)],
    (3, 4): [],
    (4, 4): [],
    (5, 0): [],
    (5, 2): [],
    (2, 8): [(22, 7), (64, 28)],
    (6, 0): [],
}
for qr, exp in expected_E.items():
    _, _, cand = r1_candidates(*qr)
    assert cand == exp, (qr, cand, exp)
    print(f"  row {qr}: candidates {cand} "
          f"(witnesses {[ld3_witness(*c) for c in cand]})")

# ---------------------------------------------------------------- section D

print("=== D. Rows R = 1 (Q = 3, 5, 7): analytic enumeration ===")

def group_products(D):
    """All products of distinct relevant prime powers q with q | D
    (at most one prime power per prime; exponent 0 allowed)."""
    fac = factorize(D)
    opts = []
    for p, e in fac.items():
        exps = [0]
        for f in range(1, e + 1):
            if p >= 5 or (p == 3 and f >= 2):
                exps.append(f)
        opts.append([p ** f for f in exps])
    out = [1]
    for o in opts:
        out = [x * y for x in out for y in o]
    return sorted(set(out))

for Q in (3, 5, 7):
    A1set = group_products(Q - 1)          # n-2 group assigned to j-1
    A2set = group_products(2 * Q - 1)      # n-2 group assigned to j-2
    Rposs = sorted({a * b for a in A1set for b in A2set if gcd(a, b) == 1})
    # odd part M of n-2: M = R(n-2) if v3(M) != 1, and M = 3*R(n-2) if
    # v3(M) = 1; in the second case 3 does not divide R(n-2).
    Mposs = sorted(set(Rposs) | {3 * r_ for r_ in Rposs if r_ % 3 != 0})
    # candidates from the exact form n = 2^a * u (u in {1,3}):
    cand = []
    for u in (1, 3):
        n = 2 * u  # a = 1 (a = 0 gives n odd <= 3, not an even candidate)
        if (n - 1) % Q == 0 and (n - 1) // Q > 3:
            cand.append((n, (n - 1) // Q))
        a = 2
        while True:
            M = (2 ** (a - 1) - 1) if u == 1 else (3 * 2 ** (a - 1) - 1)
            if M > max(Mposs):
                break
            if M in Mposs:
                n = (2 ** a) * u
                if (n - 1) % Q == 0 and (n - 1) // Q > 3:
                    cand.append((n, (n - 1) // Q))
            a += 1
    assert cand == [], (Q, cand)
    # clause cross-check over a superset range of a (a <= 12 covers the
    # product bound 3*(Q-1)*(2Q-1) <= 234 < 2^8 for these Q):
    tested = 0
    for a in range(0, 13):
        for u in (1, 3):
            n = (2 ** a) * u
            if n % 2 == 0 and (n - 1) % Q == 0:
                j = (n - 1) // Q
                if j > 3:
                    tested += 1
                    assert not (ld3_clause(n, j, 0) and ld3_clause(n, j, 2)), \
                        (Q, n, j)
    print(f"  Q={Q}: A1 products {A1set}, A2 products {A2set}, "
          f"R(n-2) in {Rposs}, odd part of n-2 in {Mposs}; "
          f"analytic candidates: none; clause cross-check tested "
          f"{tested} integer-j forms, 0 pass r=0 and r=2 clauses")

print("ALL P-I2 CHECKS PASSED")
