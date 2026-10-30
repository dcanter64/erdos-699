#!/usr/bin/env python3
"""P-L1 verification script (Cycle 3, Cluster L). Python stdlib only,
exact integer arithmetic. Companion to proofs/P-L1.md.

Sections:
  A. Digit machinery: Kummer equivalence (digitwise <=  iff p does not
     divide C(n,j)) checked exhaustively for n <= 300; the low-digit
     equivalence (digits 0..a-1 digitwise  <=>  j mod q <= r) checked
     exhaustively for n <= 1000; support-prime characterisation.
  B. Calibration: the six >=5-only (LD3) solutions with n <= 2000
     (P-A1's list). For each: full (LD3) fails at the 3-clause;
     the p=3 higher-digit subcondition PASSES; and the list of
     support primes >= 5 whose FULL digitwise condition fails.
  C. Families at p = 3: n = 3^a+1 (j = n/2), n = 3^a-1 (j = n/2),
     n = 2*3^a+1 (j = 3^a).
  D. The >=5-only (LD3) system to n <= 10^6 (SPF-sieve search):
     exactly 12 solutions; classification of each by (i) 3-clause
     low-digit failure, (ii) p=3 higher-digit subcondition,
     (iii) >=5 higher-digit failures.
  E. h = 0 row classes (Prop. 4.1: V_3(n) | Lambda_3(T)) enumerated
     to n <= 10^8 by the finite odd-part parametrisation
     (odd part of n divides 3*Lambda_3(T)); filters V | Lambda,
     then (LD3), then (LD3+). Plus the (4,2) row (h = 1) via the
     finite n-1 set of F1.11.
  F. Local strictness example: (n,j,p) = (30,15,5): the low-digit
     condition at 5 passes, the full digitwise condition fails.
"""
import math
import time
from array import array
from math import comb, gcd

T_START = time.time()


def note(msg):
    print(f"[{time.time() - T_START:7.1f}s] {msg}", flush=True)


# ---------------------------------------------------------------- helpers
def primes_upto(n):
    s = bytearray(b"\x01") * (n + 1)
    s[0:2] = b"\x00\x00"
    for i in range(2, int(n ** 0.5) + 1):
        if s[i]:
            s[i * i:n + 1:i] = b"\x00" * (((n - i * i) // i) + 1)
    return [i for i, v in enumerate(s) if v]


PR = primes_upto(100000)  # enough for trial division up to 10^8 tops


def factorize(m):
    """exact prime factorisation of m >= 1 as dict {p: a} (trial division)."""
    out = {}
    x = m
    for p in PR:
        if p * p > x:
            break
        while x % p == 0:
            out[p] = out.get(p, 0) + 1
            x //= p
    if x > 1:
        out[x] = out.get(x, 0) + 1
    return out


def vp(m, p):
    c = 0
    while m % p == 0:
        m //= p
        c += 1
    return c


def digits_le(j, n, p):
    """True iff every base-p digit of j is <= the corresponding digit of n."""
    while j or n:
        if j % p > n % p:
            return False
        j //= p
        n //= p
    return True


def support_primes_Cn3(n):
    """{p: exponent} of the primes p >= 3 dividing C(n,3), from the tops."""
    sup = {}
    for r in range(3):
        for p, a in factorize(n - r).items():
            sup[p] = sup.get(p, 0) + a
    sup[2] = sup.get(2, 0) - 1   # divide by 6 = 2 * 3
    sup[3] = sup.get(3, 0) - 1
    return {p: a for p, a in sup.items() if a > 0 and p >= 3}


def relevant(n):
    """relevant prime powers (p, a, r, q=p^a) of the three tops, (LD3) sense."""
    out = []
    for r in range(3):
        for p, a in factorize(n - r).items():
            if p >= 5 or (p == 3 and a >= 2):
                out.append((p, a, r, p ** a))
    return out


def ld3(n, j, ge5only=False):
    """(ok, first failing (p,a,r,q) or None)."""
    for (p, a, r, q) in relevant(n):
        if ge5only and p == 3:
            continue
        if j % q > r:
            return False, (p, a, r, q)
    return True, None


def ld3plus(n, j):
    """(ok, list of support primes whose full digitwise condition fails)."""
    fails = [p for p in support_primes_Cn3(n) if not digits_le(j, n, p)]
    return (not fails), fails


def V3(n):
    c = n * (n - 1) * (n - 2) // 6
    while c % 2 == 0:
        c //= 2
    return c


def lam3(T):
    if T < 3:
        return 1
    out = 1
    for q in primes_upto(T):
        if q < 3:
            continue
        pw = q
        while pw * q <= T:
            pw *= q
        out *= pw
    return out


def three_top(n):
    """(r3, a3): the unique top n-r3 divisible by 3, and its 3-adic valuation."""
    for r in range(3):
        if (n - r) % 3 == 0:
            return r, vp(n - r, 3)
    raise AssertionError


def higher3(n, j):
    """p=3 higher-digit subcondition (digits >= a3), or None if a3 < 2
    (then 3 does not divide C(n,3) and there is no condition)."""
    r3, a3 = three_top(n)
    if a3 < 2:
        return None
    q = 3 ** a3
    return digits_le(j // q, (n - r3) // q, 3)


# ---------------------------------------------------------------- A
note("A. Digit machinery validation")
# A1: Kummer equivalence, exhaustive n <= 300
cnt = 0
bad = 0
for n in range(4, 301):
    Cn3 = comb(n, 3)
    sup = [p for p in factorize(Cn3) if p >= 3]
    # support from tops must match support from C(n,3) directly
    assert set(sup) == set(support_primes_Cn3(n)), n
    for j in range(4, n // 2 + 1):
        Cnj = comb(n, j)
        for p in sup:
            cnt += 1
            if digits_le(j, n, p) != (Cnj % p != 0):
                bad += 1
print(f"   A1: {cnt} (n,j,p) instances, n<=300: digitwise<=>p∤C(n,j), failures={bad}")
assert bad == 0

# A2: low-digit equivalence, exhaustive n <= 1000, all j, all relevant q
cnt = 0
bad = 0
for n in range(6, 1001):
    rel = relevant(n)
    if not rel:
        continue
    # n's low digits are (r,0,...,0): check n mod q == r
    for (p, a, r, q) in rel:
        assert n % q == r, (n, p, a, r, q)
    for j in range(4, n // 2 + 1):
        for (p, a, r, q) in rel:
            cnt += 1
            # digitwise on digits 0..a-1: build truncated digit comparison
            jj, nn, ok = j, n, True
            for _ in range(a):
                if jj % p > nn % p:
                    ok = False
                    break
                jj //= p
                nn //= p
            if ok != (j % q <= r):
                bad += 1
print(f"   A2: {cnt} (n,j,q) instances, n<=1000: low-digitwise <=> j mod q <= r, failures={bad}")
assert bad == 0

# A3: support characterisation: p | C(n,3), p>=3, iff p divides a top and
# (p>=5 or the 3-top has valuation >=2) -- already asserted in A1 via the
# two computations of the support; restate as a count.
print("   A3: support characterisation asserted inside A1 for all n<=300")

# ---------------------------------------------------------------- B
note("B. Calibration: the six >=5-only (LD3) solutions, n <= 2000")
SIX = [(10, 5), (28, 14), (82, 41), (162, 70), (244, 122), (730, 365)]
for (n, j) in SIX:
    ok5, _ = ld3(n, j, ge5only=True)
    okF, wit = ld3(n, j)
    okP, fails = ld3plus(n, j)
    fails5 = [p for p in fails if p >= 5]
    h3 = higher3(n, j)
    print(f"   (n,j)=({n},{j}): >=5 LD3 holds={ok5}; full LD3 fails at {wit}; "
          f"LD3+ failing primes={sorted(fails)} (>=5: {sorted(fails5)}); "
          f"p=3 higher subcondition passes={h3}")
    assert ok5 and not okF and wit[0] == 3 and not okP and 3 in fails
    assert h3 is True

# ---------------------------------------------------------------- C
note("C. Families at p=3")
for a in range(2, 13):
    n, j = 3 ** a + 1, (3 ** a + 1) // 2
    ok5, _ = ld3(n, j, ge5only=True)
    okF, wit = ld3(n, j)
    h3 = higher3(n, j)
    print(f"   3^{a}+1: n={n}, j={j}: >=5 LD3={ok5}; full LD3 fails at {wit}; "
          f"j mod 3^{a}={j % (3 ** a)} > 1; p=3 higher passes={h3}")
    assert ok5 and not okF and wit == (3, a, 1, 3 ** a) and h3 is True
for a in range(2, 9):
    n, j = 3 ** a - 1, (3 ** a - 1) // 2
    r3, a3 = three_top(n)
    okF, wit = ld3(n, j)
    print(f"   3^{a}-1: n={n}, j={j}: v3 of 3-top (r={r3}) is {a3} "
          f"(so 3∤C(n,3), no p=3 condition); full LD3 fails at >=5 witness {wit}")
    assert a3 == 1 and not okF and wit[0] >= 5
for a in range(2, 9):
    n, j = 2 * 3 ** a + 1, 3 ** a
    r3, a3 = three_top(n)
    h3 = higher3(n, j)
    okF, wit = ld3(n, j)
    print(f"   2*3^{a}+1: n={n}, j={j}: 3-top r={r3}, a={a3}; j mod 3^{a}="
          f"{j % (3 ** a)} <= 1 (3-low passes); p=3 higher passes={h3}; "
          f"full LD3 fails at r=0 witness {wit}")
    assert a3 == a and j % (3 ** a) <= 1 and h3 is True
    assert not okF and wit[2] == 0 and wit[0] >= 5

# ---------------------------------------------------------------- D
note("D. The >=5-only (LD3) system to n <= 10^6 (SPF-sieve search)")
L = 10 ** 6
spfA = array("i", range(L + 1))
for i in range(math.isqrt(L), 1, -1):
    c_i = (L - i) // i + 1
    spfA[i::i] = array("i", [i] * c_i)


def rel5(m):
    qs = []
    x = m
    while x > 1:
        p = spfA[x]
        q = 1
        while x % p == 0:
            x //= p
            q *= p
        if p >= 5:
            qs.append(q)
    return qs


surv = []
pairs = 0
for n in range(6, L + 1):
    x = n
    Rn = 1
    while x > 1:
        p = spfA[x]
        q = 1
        while x % p == 0:
            x //= p
            q *= p
        if p >= 5:
            Rn *= q
    if Rn > n // 2:
        continue
    r1 = rel5(n - 1)
    r2 = rel5(n - 2)
    r1.sort(reverse=True)
    r2.sort(reverse=True)
    j = Rn if Rn >= 4 else 4
    while j <= n // 2:
        pairs += 1
        if all(j % q <= 1 for q in r1) and all(j % q <= 2 for q in r2):
            surv.append((n, j))
        j += Rn
print(f"   pairs tested = {pairs}; >=5-only (LD3) solutions with n<=10^6: {len(surv)}")
print(f"   solutions: {surv}")
EXPECTED12 = [(10, 5), (28, 14), (82, 41), (162, 70), (244, 122), (730, 365),
              (2188, 1094), (6562, 3281), (19684, 9842), (59050, 29525),
              (177148, 88574), (531442, 265721)]
assert surv == EXPECTED12
n_killed_ge5higher = 0
for (n, j) in surv:
    okF, wit = ld3(n, j)
    okP, fails = ld3plus(n, j)
    fails5 = sorted(p for p in fails if p >= 5)
    h3 = higher3(n, j)
    if fails5:
        n_killed_ge5higher += 1
    print(f"   ({n},{j}): full LD3 fails at 3-clause {wit}; LD3+ failing primes="
          f"{sorted(fails)}; >=5 higher failures={fails5}; p=3 higher passes={h3}")
    assert not okF and wit[0] == 3 and not okP and h3 is True
print(f"   of the 12: {n_killed_ge5higher} are excluded by >=5 higher digits "
      f"alone (some p>=5 full-digitwise failure); all 12 pass the p=3 higher "
      f"subcondition; all 12 fail the p=3 low clause")

# ---------------------------------------------------------------- E
note("E. h=0 row classes to n <= 10^8 by finite odd-part parametrisation")


def divisors_of(m):
    ds = [1]
    for p, a in factorize(m).items():
        ds = [d * p ** e for d in ds for e in range(a + 1)]
    return sorted(ds)


def enumerate_h0(Q, R, Limit=10 ** 8):
    T = R + 2 * (Q - 1)
    assert R >= 3  # h = 0 rows only
    Lam = lam3(T)
    odd_parts = [d for d in divisors_of(3 * Lam) if d % 2 == 1]
    cand = set()
    for o in odd_parts:
        x = o
        while x <= Limit:
            cand.add(x)
            if x > Limit // 2:
                break
            x *= 2
    cand = sorted(cand)
    inrow = []
    for n in cand:
        if n <= R or (n - R) % Q:
            continue
        j = (n - R) // Q
        if j > 3 and 2 * j <= n:
            inrow.append((n, j))
    vpass = []
    for (n, j) in inrow:
        v = V3(n)
        if v and Lam % v == 0:
            assert v <= Lam
            vpass.append((n, j, v))
    lpass = [(n, j) for (n, j, v) in vpass if ld3(n, j)[0]]
    ppass = [(n, j) for (n, j) in lpass if ld3plus(n, j)[0]]
    print(f"   row (Q,R)=({Q},{R}): T={T}, Lambda_3(T)={Lam}, "
          f"odd parts={len(odd_parts)}, candidate n={len(cand)}, in-row={len(inrow)}, "
          f"V|Lambda: {len(vpass)} {[(n, j) for (n, j, v) in vpass]}, "
          f"(LD3): {len(lpass)} {lpass}, (LD3+): {len(ppass)} {ppass}")
    return vpass, lpass, ppass


ROWS = [(2, 4), (2, 3), (2, 5), (3, 3), (2, 6), (3, 4),
        (2, 16), (2, 17), (2, 18), (3, 16)]
for (Q, R) in ROWS:
    enumerate_h0(Q, R)

note("E2. The (4,2) row (h=1) via the finite n-1 set of F1.11")
resid42 = []
for b in range(3):
    for a5 in range(2):
        for c7 in range(2):
            m = (3 ** b) * (5 ** a5) * (7 ** c7)
            if (m - 1) % 4 == 0:
                j = (m - 1) // 4
                if j >= 5:
                    resid42.append((m + 1, j))
print(f"   (4,2) candidates: {sorted(resid42)}")
assert sorted(resid42) == [(22, 5), (46, 11), (106, 26)]
for (n, j) in sorted(resid42):
    okF, _ = ld3(n, j)
    g = gcd(V3(n), comb(n, j))
    print(f"   ({n},{j}): (LD3) holds={okF}; gcd(V_3(n),C(n,j))={g}")
    assert not okF and g > 1

# ---------------------------------------------------------------- F
note("F. Local strictness example at a single prime")
n, j, p = 30, 15, 5
print(f"   (n,j,p)=({n},{j},{p}): j mod 5 = {j % 5} <= 0 (low condition at the "
      f"a=1 prime power 5 || n passes); full digitwise at 5: {digits_le(j, n, p)} "
      f"(digit 1: floor(15/5) mod 5 = {(j // 5) % 5} > floor(30/5) mod 5 = {(n // 5) % 5})")
assert j % 5 == 0 and not digits_le(j, n, p)

note("ALL P-L1 CHECKS PASSED")
print(f"total runtime: {time.time() - T_START:.1f}s")
