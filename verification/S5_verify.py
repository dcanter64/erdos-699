#!/usr/bin/env python3
"""
S5 verification script (Python standard library only).

Verifies, on ALL triples 1 <= i < j <= n/2 with n <= 300 (1,113,775 triples),
the new divisibility / valuation claims of strategy paper S5:

  (V1) Surplus divisibility (unconditional):
         g' = C(n,i)/gcd(C(n,i),C(n,j))  divides  C(j,i),
         e' = C(n,j)/gcd(C(n,i),C(n,j))  divides  C(n-i, j-i).
  (V2) R-valuation formula (all primes simultaneously, via packed exponents):
         v_p(C(n,j)) - v_p(C(n,i)) = v_p(Num) - v_p(Den),
         Num = (n-i)!/(n-j)!,  Den = j!/i!.
       Exponents are packed into one big integer per vector with field
       width 12 bits and offset 2048 per field, so a single integer
       equality per triple checks all 78 primes <= 300 at once.
  (V3) Support persistence: every prime p > j with p | C(n,i), p >= i,
       also divides C(n,j)   (checked with prime-support bitmasks).
  (V4) No counterexample at all in range: gcd(V_i(n), C(n,j)) > 1 for
       every triple; the sub-count for i in {1,2} is reported separately
       (S5 proves those two families in full generality).
  (V5) Prime-power bound: for all n <= 300, k <= n/2, all primes p,
       v_p(C(n,k)) <= floor(log_p n)   (Legendre table check).
  (V6) Denominator vanishing: for all i < j and primes p > j,
       v_p(j!) - v_p(i!) = 0   (the factorial fact behind (V3)).
  (V7) Near-diagonal square-bound family: for odd i = 2m+1 (m = 1..40),
       j = 3m+2, and even i = 2m (m = 5..40), j = 3m+1:
       C(2j,i) >= C(j,j-i)^2 in exact arithmetic, the step-ratio
       identities of S5 hold as exact rational identities, and
       C(2j,i) < C(2j, 2(j-i)) (so Phase 0's stated reduction does
       NOT close these pairs).
  (V8) Worked examples (3,5) and (5,8): Phase-0 N(i,j) (from
       C(n,i) < C(2j,2(j-i))) is >= 2j, while the square bound
       C(n,i) < C(j,j-i)^2 already fails at n = 2j.
  (V9) Strictness example for (V1): at (n,i,j) = (10,2,4),
       gcd(g', C(n,j)) = 3 > 1, so g' does NOT satisfy the hypothesis
       of the original key lemma, yet g' | C(j,i) holds -- the surplus
       lemma is a genuine strengthening of the key lemma.

Every check that fails increments a counter and is printed; the script
exits nonzero if any counter is nonzero.
"""
import sys
import time
from math import comb, gcd

NMAX = 300
t_start = time.time()
failures = []


def check(cond, label):
    if not cond:
        failures.append(label)
        print("FAIL:", label)


# ---------- sieve, primes, factorial exponent table ----------
spf = list(range(NMAX + 1))
for x in range(2, int(NMAX ** 0.5) + 1):
    if spf[x] == x:
        for y in range(x * x, NMAX + 1, x):
            if spf[y] == y:
                spf[y] = x
primes = [x for x in range(2, NMAX + 1) if spf[x] == x]
pidx = {p: t for t, p in enumerate(primes)}
NP = len(primes)


def factorize(x):
    out = {}
    while x > 1:
        p = spf[x]
        out[p] = out.get(p, 0) + 1
        x //= p
    return out


# Fexp[n][t] = v_{primes[t]}(n!)
Fexp = [[0] * NP]
for n in range(1, NMAX + 1):
    row = Fexp[-1][:]
    for p, e in factorize(n).items():
        row[pidx[p]] += e
    Fexp.append(row)

# ---------- packed exponent vectors (field width 12, offset 2048) ----------
W = 12
OFF_FIELD = 2048
OFFPACK = 0
for t in range(NP):
    OFFPACK += OFF_FIELD << (W * t)
Fpack = [0] * (NMAX + 1)
for n in range(1, NMAX + 1):
    inc = 0
    for p, e in factorize(n).items():
        inc += e << (W * pidx[p])
    Fpack[n] = Fpack[n - 1] + inc


def cpack(n, k):
    # packed exponents of C(n,k); per-field subtrahend <= minuend, no borrows
    return Fpack[n] - Fpack[k] - Fpack[n - k]


# DenPack[i][j] = packed exponents of j!/i!
DenPack = [[0] * (NMAX + 1) for _ in range(NMAX + 1)]
for i in range(NMAX + 1):
    Fi = Fpack[i]
    for j in range(i + 1, NMAX + 1):
        DenPack[i][j] = Fpack[j] - Fi

# ---------- binomial triangle (Pascal) ----------
C = [[0] * (NMAX + 1) for _ in range(NMAX + 1)]
for n in range(NMAX + 1):
    C[n][0] = C[n][n] = 1
    for k in range(1, n):
        C[n][k] = C[n - 1][k - 1] + C[n - 1][k]

# ---------- prime-support masks ----------
# mask_ge[t0]: bits of primes with index >= t0 ; mask_gt_prime[j]: primes > j
mask_from_idx = [0] * (NP + 1)
for t in range(NP - 1, -1, -1):
    mask_from_idx[t] = mask_from_idx[t + 1] | (1 << t)


def mask_ge_val(x):
    # bitmask of primes >= x
    import bisect
    t = bisect.bisect_left(primes, x)
    return mask_from_idx[t]


def mask_gt_val(x):
    import bisect
    t = bisect.bisect_right(primes, x)
    return mask_from_idx[t]


MASK_GE = [mask_ge_val(x) for x in range(NMAX + 2)]
MASK_GT = [mask_gt_val(x) for x in range(NMAX + 2)]

# supp[n][k]: bitmask over prime indices of the support of C(n,k)
supp = [[0] * (NMAX + 1) for _ in range(NMAX + 1)]
for n in range(NMAX + 1):
    Fn = Fexp[n]
    for k in range(n + 1):
        Fk = Fexp[k]
        Fnk = Fexp[n - k]
        m = 0
        for t in range(NP):
            if Fn[t] - Fk[t] - Fnk[t] > 0:
                m |= 1 << t
        supp[n][k] = m

# V[n][i] = V_i(n): C(n,i) with all prime factors < i divided out
V = [[1] * (NMAX + 1) for _ in range(NMAX + 1)]
small_primes = {i: [p for p in primes if p < i] for i in range(NMAX + 1)}
for n in range(NMAX + 1):
    for i in range(1, n // 2 + 1):
        val = C[n][i]
        for p in small_primes[i]:
            while val % p == 0:
                val //= p
        V[n][i] = val

# ---------- (V5) prime-power bound ----------
import math
pp_bad = 0
for n in range(2, NMAX + 1):
    Fn = Fexp[n]
    for k in range(0, n // 2 + 1):
        Fk = Fexp[k]
        Fnk = Fexp[n - k]
        for t, p in enumerate(primes):
            a = Fn[t] - Fk[t] - Fnk[t]
            if a > 0:
                lim = 0
                q = p
                while q <= n:
                    lim += 1
                    if q > n // p:
                        break
                    q *= p
                if a > lim:
                    pp_bad += 1
check(pp_bad == 0, f"(V5) prime-power bound failures: {pp_bad}")

# ---------- (V6) denominator vanishing for p > j ----------
den_bad = 0
for i in range(1, NMAX + 1):
    for j in range(i + 1, NMAX + 1):
        Fj = Fexp[j]
        Fi = Fexp[i]
        for t, p in enumerate(primes):
            if p > j and Fj[t] - Fi[t] != 0:
                den_bad += 1
check(den_bad == 0, f"(V6) denominator vanishing failures: {den_bad}")

# ---------- main triple loop: (V1), (V2), (V3), (V4) ----------
triples = 0
bad_g = bad_e = bad_R = bad_supp = bad_counter = 0
triples_i12 = 0
bad_counter_i12 = 0
for n in range(2, NMAX + 1):
    Cn = C[n]
    Vn = V[n]
    suppn = supp[n]
    cpacks_n = [cpack(n, k) for k in range(n + 1)]
    half = n // 2
    for i in range(1, half + 1):
        A = Cn[i]
        v = Vn[i]
        suppA = suppn[i]
        cpA = cpacks_n[i]
        mge = MASK_GE[i]
        Fni = Fpack[n - i]
        for j in range(i + 1, half + 1):
            triples += 1
            B = Cn[j]
            g0 = gcd(A, B)
            gp = A // g0
            if C[j][i] % gp != 0:
                bad_g += 1
            ep = B // g0
            if C[n - i][j - i] % ep != 0:
                bad_e += 1
            # (V2) packed R-valuation identity
            lhs = OFFPACK + cpacks_n[j] - cpA
            rhs = OFFPACK + (Fni - Fpack[n - j]) - DenPack[i][j]
            if lhs != rhs:
                bad_R += 1
            # (V3) support persistence for p > j
            if suppA & mge & MASK_GT[j] & ~suppn[j]:
                bad_supp += 1
            # (V4) counterexample scan
            if gcd(v, B) == 1:
                bad_counter += 1
            if i <= 2:
                triples_i12 += 1
                if gcd(v, B) == 1:
                    bad_counter_i12 += 1
check(bad_g == 0, f"(V1) g' divisibility failures: {bad_g}")
check(bad_e == 0, f"(V1) e' divisibility failures: {bad_e}")
check(bad_R == 0, f"(V2) R-valuation failures: {bad_R}")
check(bad_supp == 0, f"(V3) support persistence failures: {bad_supp}")
check(bad_counter == 0, f"(V4) counterexamples in range: {bad_counter}")
check(bad_counter_i12 == 0,
      f"(V4) counterexamples with i in (1,2): {bad_counter_i12}")
print(f"triples checked: {triples}  (i in {{1,2}}: {triples_i12})")

# ---------- (V7) near-diagonal square-bound family ----------
def step_ratio_odd(m):
    # R_{m+1}/R_m for R_m = C(6m+4,2m+1)/C(3m+2,m+1)^2, as (num, den)
    num = 2 * (m + 2) ** 2 * (2 * m + 3) * (6 * m + 5) * (6 * m + 7)
    den = (m + 1) * (3 * m + 4) * (3 * m + 5) * (4 * m + 5) * (4 * m + 7)
    return num, den


def step_ratio_even(m):
    num = 2 * (m + 2) ** 2 * (2 * m + 1) ** 2 * (6 * m + 5) * (6 * m + 7)
    den = ((m + 1) * (2 * m + 3) * (3 * m + 2) * (3 * m + 4)
           * (4 * m + 3) * (4 * m + 5))
    return num, den


fam_bad = 0
fam_count = 0
# odd family: i = 2m+1 >= 3, j = 3m+2
Rprev = None
for m in range(1, 41):
    i, j = 2 * m + 1, 3 * m + 2
    fam_count += 1
    lhs, rhs = comb(2 * j, i), comb(j, j - i) ** 2
    if lhs < rhs:
        fam_bad += 1
    if comb(2 * j, i) >= comb(2 * j, 2 * (j - i)):
        fam_bad += 1  # Phase 0 reduction would (wrongly here) close it
    R = (lhs, rhs)
    if Rprev is not None:
        num, den = step_ratio_odd(m - 1)
        # R_m / R_{m-1} == num/den  <=>  lhs_m*rhs_{m-1}*den == lhs_{m-1}*rhs_m*num
        if R[0] * Rprev[1] * den != Rprev[0] * R[1] * num:
            fam_bad += 1
        if num <= den:
            fam_bad += 1
    Rprev = R
# even family: i = 2m >= 10, j = 3m+1
Rprev = None
for m in range(1, 41):
    i, j = 2 * m, 3 * m + 1
    R = (comb(2 * j, i), comb(j, j - i) ** 2)
    if m >= 2:
        num, den = step_ratio_even(m - 1)
        if R[0] * Rprev[1] * den != Rprev[0] * R[1] * num:
            fam_bad += 1
        if num <= den:
            fam_bad += 1
    if m >= 5:
        fam_count += 1
        if R[0] < R[1]:
            fam_bad += 1
        if comb(2 * j, i) >= comb(2 * j, 2 * (j - i)):
            fam_bad += 1
    Rprev = R
check(fam_bad == 0, f"(V7) family failures: {fam_bad}")
print(f"family pairs verified (m ranges as in S5): {fam_count}")

# ---------- (V8) worked examples ----------
for (i, j, Nph) in [(3, 5, 11), (5, 8, 17)]:
    target = comb(2 * j, 2 * (j - i))
    N = max(n for n in range(2 * j, 400) if comb(n, i) < target)
    check(N == Nph, f"(V8) N({i},{j}) = {N}, expected {Nph}")
    check(comb(2 * j, i) >= comb(j, j - i) ** 2,
          f"(V8) square bound fails at minimal n for ({i},{j})")
print("(V8) N(3,5) = 11, N(5,8) = 17 confirmed; square bound closes both")

# ---------- (V9) surplus lemma is strictly stronger than key lemma ----------
A, B = comb(10, 2), comb(10, 4)
g0 = gcd(A, B)
gp = A // g0
check(gp == 3 and gcd(gp, B) == 3 and comb(4, 2) % gp == 0,
      "(V9) example (10,2,4) mismatch")
print("(V9) (10,2,4): g' = 3, gcd(g', C(10,4)) = 3 > 1, yet g' | C(4,2) = 6")

elapsed = time.time() - t_start
print(f"elapsed: {elapsed:.1f}s")
if failures:
    print(f"RESULT: {len(failures)} FAILING CHECK GROUPS")
    sys.exit(1)
print("RESULT: ALL S5 CHECKS PASSED")
