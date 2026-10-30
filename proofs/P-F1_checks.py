#!/usr/bin/env python3
"""P-F1 verification script. Python stdlib only, exact integer arithmetic.

Sections:
  A. Price Prop. 4.1 specialisation values (Lambda_3, Del Pin tables).
  B. Task 4: (LD3) per pair (3,j), j <= 2000, on 2j <= n <= N(3,j),
     by the R(n)-candidate method.
  C. Independent brute-force cross-checks (different code path):
     >=5-only (LD3) survivors for n <= 2000 (the known six pairs);
     full (LD3) brute force for n <= 2000 (zero survivors);
     per-pair brute force for j <= 150 on [2j, N(3,j)] (zero survivors).
  D. Task 5a: (LD3) on the SPLIT-odd family to n <= 10^6 (zero survivors),
     plus the (N2)-only pass count in that family (3472 pass (N2) alone).
  E. Task 5b: full (LD3) search to n <= 10^6 by an SPF-sieve method
     (zero survivors; 7,085,360 candidate pairs tested).
  F. The (Q,R) = (4,2) residual candidates of the Prop. 4.1 + (n-1)
     argument, each killed by (LD3) directly.
"""
import math
import time
from array import array
from math import comb

T_START = time.time()


def note(msg):
    print(f"[{time.time() - T_START:7.1f}s] {msg}", flush=True)


# ---------------------------------------------------------------- primes
def primes_upto(n):
    s = bytearray(b"\x01") * (n + 1)
    s[0:2] = b"\x00\x00"
    for i in range(2, int(n ** 0.5) + 1):
        if s[i]:
            s[i * i:n + 1:i] = b"\x00" * (((n - i * i) // i) + 1)
    return [i for i, v in enumerate(s) if v]


PR2000 = primes_upto(2000)


def factorize_trial(m):
    out = []
    x = m
    for p in PR2000:
        if p * p > x:
            break
        if x % p == 0:
            a = 0
            while x % p == 0:
                x //= p
                a += 1
            out.append((p, a))
    if x > 1:
        out.append((x, 1))
    return out


def relevant_qs(m, drop3=False):
    qs = []
    for p, a in factorize_trial(m):
        if p >= 5 or (p == 3 and a >= 2 and not drop3):
            qs.append(p ** a)
    return qs


def lam3(T):
    """Lambda_3(T) = prod over primes q>=3 of q^floor(log_q T); Lambda_3(0)=1."""
    if T <= 0:
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


def N_of_3(j):
    """max{n : C(n,3) < C(2j, 2(j-3))} = max{n : C(n,3) < C(2j,6)}."""
    target = comb(2 * j, 6)
    lo, hi = 3, 6
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
note("A. Lambda_3 values and Del Pin data")
for T in [3, 4, 6, 7, 8]:
    print("   Lambda_3(%d) = %d" % (T, lam3(T)))
for j in [5, 6, 7, 8, 10, 100, 465, 2000]:
    print("   N(3,%d) = %d" % (j, N_of_3(j)))
for j in range(4, 11):
    print("   j=%d  C(2j,3)=%d  C(j,3)^2=%d  ratio C(2j,3)/C(j,3)=%s"
          % (j, comb(2 * j, 3), comb(j, 3) ** 2,
             __import__("fractions").Fraction(comb(2 * j, 3), comb(j, 3))))
for j in [6, 7, 8, 10, 20]:
    row = []
    for v in [4, 5, 6]:
        n = 2 * j
        while comb(n, 3) <= (1 << v) * comb(j, 3):
            n += 1
        row.append((v, n))
    print("   j=%d minimal n with C(n,3) > 2^v C(j,3): %s" % (j, row))

# ---------------------------------------------------------------- B
note("B. Task 4: LD3 per pair, j <= 2000 (R(n)-candidate method)")
Nmax = N_of_3(2000)
ds = []
for d in range(1, 2001):
    if d % 2 == 0:
        continue
    v3 = 0
    for p, a in factorize_trial(d):
        if p == 3:
            v3 = a
    if v3 == 1:
        continue
    ds.append((d, v3))
cand = set()
for d, v3 in ds:
    a = 0
    while d * (1 << a) <= Nmax:
        cand.add(d * (1 << a))
        if v3 == 0:
            cand.add(d * 3 * (1 << a))
        a += 1
print("   N(3,2000) = %d; candidate n count = %d" % (Nmax, len(cand)))
survivors = {}
checked = 0
for n in sorted(cand):
    Rn = 1
    for q in relevant_qs(n):
        Rn *= q
    assert Rn <= 2000, (n, Rn)
    rel1 = relevant_qs(n - 1)
    rel2 = relevant_qs(n - 2)
    j = Rn
    if j < 4:
        j = 4 if Rn == 1 else Rn
    while j <= 2000 and 2 * j <= n:
        checked += 1
        if all(j % q <= 1 for q in rel1) and all(j % q <= 2 for q in rel2):
            if n <= N_of_3(j):
                survivors.setdefault(j, []).append(n)
        j += Rn
print("   candidate pairs tested = %d; survivor j values = %s"
      % (checked, sorted(survivors.keys())))
assert not survivors

# ---------------------------------------------------------------- C
note("C. Independent brute-force cross-checks (SPF, all j, no candidates)")


def spf_build(L):
    spf = list(range(L + 1))
    for i in range(2, int(L ** 0.5) + 1):
        if spf[i] == i:
            for k in range(i * i, L + 1, i):
                if spf[k] == k:
                    spf[k] = i
    return spf


def rel_spf(m, spf, drop3=False):
    qs = []
    x = m
    while x > 1:
        p = spf[x]
        a = 0
        q = 1
        while x % p == 0:
            x //= p
            a += 1
            q *= p
        if p >= 5 or (p == 3 and a >= 2 and not drop3):
            qs.append(q)
    return qs


L = 2000
spf = spf_build(L)
surv_ge5 = []
surv_full = []
for n in range(6, L + 1):
    r0a = rel_spf(n, spf, drop3=True)
    r1a = rel_spf(n - 1, spf, drop3=True)
    r2a = rel_spf(n - 2, spf, drop3=True)
    r0 = rel_spf(n, spf)
    r1 = rel_spf(n - 1, spf)
    r2 = rel_spf(n - 2, spf)
    for j in range(4, n // 2 + 1):
        if (all(j % q == 0 for q in r0a) and all(j % q <= 1 for q in r1a)
                and all(j % q <= 2 for q in r2a)):
            surv_ge5.append((n, j))
        if (all(j % q == 0 for q in r0) and all(j % q <= 1 for q in r1)
                and all(j % q <= 2 for q in r2)):
            surv_full.append((n, j))
print("   >=5-only survivors n<=2000:", surv_ge5)
print("   full LD3 survivors n<=2000:", surv_full)
assert surv_ge5 == [(10, 5), (28, 14), (82, 41), (162, 70), (244, 122),
                    (730, 365)]
assert not surv_full

surv_pp = []
for j in range(5, 151):
    N = N_of_3(j)
    spfj = spf_build(N)
    for n in range(2 * j, N + 1):
        r0 = rel_spf(n, spfj)
        r1 = rel_spf(n - 1, spfj)
        r2 = rel_spf(n - 2, spfj)
        if (all(j % q == 0 for q in r0) and all(j % q <= 1 for q in r1)
                and all(j % q <= 2 for q in r2)):
            surv_pp.append((n, j))
print("   per-pair brute j<=150 survivors:", surv_pp)
assert not surv_pp

# ---------------------------------------------------------------- D
note("D. Task 5a: SPLIT-odd family to 10^6")


def upart(m):
    u = 1
    x = m
    for p in PR2000:
        if p * p > x:
            break
        if x % p == 0:
            a = 0
            while x % p == 0:
                x //= p
                a += 1
            if p >= 5:
                u *= p ** a
    if x > 1 and x >= 5:
        u *= x
    return u


cnt = 0
odd_surv = []
n2_pass = 0
for n in range(15, 10 ** 6 + 1, 3):
    j = n // 3
    if j % 2 == 0 or j % 3 == 0:
        continue
    cnt += 1
    if upart(n - 1) * upart(n - 2) * 6 <= (j - 1) * (j - 2):
        n2_pass += 1
    if (all(j % q <= 1 for q in relevant_qs(n - 1))
            and all(j % q <= 2 for q in relevant_qs(n - 2))):
        odd_surv.append((n, j))
print("   odd-family n tested = %d; (N2)-only passes = %d; LD3 survivors = %s"
      % (cnt, n2_pass, odd_surv))
assert cnt == 111110 and n2_pass == 3472 and not odd_surv

# ---------------------------------------------------------------- E
note("E. Task 5b: full LD3 search to 10^6 (SPF-slice method)")
L = 10 ** 6
spfA = array("i", range(L + 1))
for i in range(math.isqrt(L), 1, -1):
    cnt_i = (L - i) // i + 1
    spfA[i::i] = array("i", [i] * cnt_i)


def relA(m):
    qs = []
    x = m
    while x > 1:
        p = spfA[x]
        a = 0
        q = 1
        while x % p == 0:
            x //= p
            a += 1
            q *= p
        if p >= 5 or (p == 3 and a >= 2):
            qs.append(q)
    return qs


survE = []
pairsE = 0
n_with = 0
for n in range(6, L + 1):
    x = n
    Rn = 1
    while x > 1:
        p = spfA[x]
        a = 0
        q = 1
        while x % p == 0:
            x //= p
            a += 1
            q *= p
        if p >= 5 or (p == 3 and a >= 2):
            Rn *= q
    if Rn > n // 2:
        continue
    rel1 = relA(n - 1)
    rel2 = relA(n - 2)
    rel1.sort(reverse=True)
    rel2.sort(reverse=True)
    j = Rn if Rn >= 4 else 4
    local = 0
    while j <= n // 2:
        local += 1
        pairsE += 1
        if (all(j % q <= 1 for q in rel1)
                and all(j % q <= 2 for q in rel2)):
            survE.append((n, j))
        j += Rn
    if local:
        n_with += 1
print("   n with j-candidates = %d; pairs tested = %d; survivors = %s"
      % (n_with, pairsE, survE))
assert pairsE == 7085360 and not survE

# ---------------------------------------------------------------- F
note("F. (Q,R)=(4,2) residual candidates of the Prop.4.1+(n-1) argument")
resid = []
for b in range(0, 3):
    for a5 in range(0, 2):
        for c7 in range(0, 2):
            m = (3 ** b) * (5 ** a5) * (7 ** c7)
            if (m - 1) % 4 == 0:
                j = (m - 1) // 4
                if j >= 5:
                    resid.append((m + 1, j))  # n = m+1 = 4j+2
print("   residual (n,j) from that argument alone:", resid)
for (n, j) in resid:
    r0 = relevant_qs(n)
    r1 = relevant_qs(n - 1)
    r2 = relevant_qs(n - 2)
    ld3 = (all(j % q == 0 for q in r0) and all(j % q <= 1 for q in r1)
           and all(j % q <= 2 for q in r2))
    g = math.gcd(1, 1)
    # gcd(V_3(n), C(n,j)) directly
    from math import comb as _c
    Cn3 = _c(n, 3)
    v = Cn3
    while v % 2 == 0:
        v //= 2
    g = math.gcd(v, _c(n, j))
    print("   (n,j)=(%d,%d): LD3 holds=%s, gcd(V_3(n),C(n,j))=%d"
          % (n, j, ld3, g))
    assert not ld3 and g > 1

note("ALL P-F1 CHECKS PASSED")
