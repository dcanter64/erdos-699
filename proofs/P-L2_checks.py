#!/usr/bin/env python3
"""P-L2 checks: Cluster L (higher-digit Kummer refinement at i = 3), Cycle 3.

Python standard library only, exact integer arithmetic, no randomness.
Sections:
  A  (LD3+)  <=>  gcd(V3(n), C(n,j)) == 1, exhaustive n <= 400.
  B  Low-digit equivalence: digitwise on digits 0..a-1  <=>  j mod q <= r,
     exhaustive n <= 1000.
  C  Calibration: >=5-only (LD3) solutions n <= 2000 (exactly the six of
     P-A1); the p = 3 digit failures for each; the families 3^a+1,
     3^a-1, 2*3^a+1.
  D  Per-prime tail strictness: the p = 5 infinite family, and instance
     counts for n <= 2000.
  E  h = 0 finiteness lemma: direct validation, all even n <= 200000.
  F  Row enumerations: (2,4) by two parametrisations to 10^8; (2,6),
     (3,4); the (4,2) cross-check; aggregate h = 0 sweep, T <= 20.
Total runtime is printed at the end (target: a few minutes at most).
"""
import time
from math import gcd, comb

T_START = time.time()

# ---------------------------------------------------------------- helpers

def spf_upto(N):
    spf = list(range(N + 1))
    i = 2
    while i * i <= N:
        if spf[i] == i:
            for k in range(i * i, N + 1, i):
                if spf[k] == k:
                    spf[k] = i
        i += 1
    return spf

def fac_small(m, spf):
    f = {}
    while m > 1:
        p = spf[m]
        a = 0
        while m % p == 0:
            m //= p
            a += 1
        f[p] = a
    return f

def primes_upto(N):
    s = [True] * (N + 1)
    s[0] = s[1] = False
    for i in range(2, int(N ** 0.5) + 1):
        if s[i]:
            for k in range(i * i, N + 1, i):
                s[k] = False
    return [i for i, v in enumerate(s) if v]

PR_BIG = primes_upto(10000)          # sqrt(10^8) = 10^4

def fac_big(m):
    f = {}
    for p in PR_BIG:
        if p * p > m:
            break
        if m % p == 0:
            a = 0
            while m % p == 0:
                m //= p
                a += 1
            f[p] = a
    if m > 1:
        f[m] = f.get(m, 0) + 1
    return f

def digits(x, p):
    ds = []
    if x == 0:
        return [0]
    while x:
        ds.append(x % p)
        x //= p
    return ds

def digitwise_leq(j, n, p):
    """True iff every base-p digit of j is <= the corresponding digit of n."""
    while j or n:
        if j % p > n % p:
            return False
        j //= p
        n //= p
    return True

def C3(n):
    return n * (n - 1) * (n - 2) // 6

def V3(n):
    c = C3(n)
    while c % 2 == 0:
        c //= 2
    return c

def relevant_tops(n, fac):
    """fac: dict m -> factorisation dict for m in {n, n-1, n-2}.
    Returns list of (rho, p, a, q) relevant: p >= 5 any a; p = 3, a >= 2."""
    out = []
    for rho in range(3):
        for p, a in fac[n - rho].items():
            if p >= 5 or (p == 3 and a >= 2):
                out.append((rho, p, a, p ** a))
    return out

def ld3_wit(n, j, fac):
    w = []
    for rho, p, a, q in relevant_tops(n, fac):
        if j % q > rho:
            w.append((rho, p, a, q, j % q))
    return w

def ld3plus_fails(n, j, fac):
    """dict p -> list of failing digit positions, over primes p | V3(n).
    Primes dividing V3(n): p >= 5 dividing a top; p = 3 iff some top has
    v3 >= 2 (equivalently v3(C(n,3)) >= 1)."""
    ps = set()
    for rho in range(3):
        for p, a in fac[n - rho].items():
            if p >= 5:
                ps.add(p)
            elif p == 3 and a >= 2:
                ps.add(3)
    out = {}
    for p in sorted(ps):
        dn = digits(n, p)
        dj = digits(j, p)
        L = max(len(dn), len(dj))
        dn += [0] * (L - len(dn))
        dj += [0] * (L - len(dj))
        fl = [e for e in range(L) if dj[e] > dn[e]]
        if fl:
            out[p] = fl
    return out

def Lambda3(T):
    r = 1
    for p in primes_upto(T):
        if p < 3:
            continue
        q = p
        while q * p <= T:
            q *= p
        r *= q
    return r

# ---------------------------------------------------------------- section A
print("== A. (LD3+) <=> gcd(V3(n), C(n,j)) == 1, exhaustive n <= 400 ==")
spf400 = spf_upto(400)
tot = mism = 0
sols = []
for n in range(7, 401):
    fac = {m: fac_small(m, spf400) for m in (n, n - 1, n - 2)}
    v = V3(n)
    for j in range(4, n // 2 + 1):
        tot += 1
        eq = (gcd(v, comb(n, j)) == 1)
        lp = (ld3plus_fails(n, j, fac) == {})
        if eq != lp:
            mism += 1
            print("  MISMATCH", n, j, eq, lp)
        if lp:
            sols.append((n, j))
print(f"  pairs checked: {tot}, mismatches: {mism}, (LD3+) solutions: {sols}")
assert mism == 0

# ---------------------------------------------------------------- section B
print("== B. Low-digit equivalence, exhaustive n <= 1000 ==")
N = 1000
spf = spf_upto(N + 1)
checked = bad = 0
for n in range(7, N + 1):
    fac = {m: fac_small(m, spf) for m in (n, n - 1, n - 2)}
    rel = relevant_tops(n, fac)
    if not rel:
        continue
    for j in range(4, n // 2 + 1):
        for rho, p, a, q in rel:
            checked += 1
            ineq = (j % q <= rho)
            # digitwise on digits 0..a-1, computed from the digits directly:
            jj = j % q
            dig_ok = True
            for e in range(a):
                d = jj % p
                jj //= p
                nd = rho if e == 0 else 0
                if d > nd:
                    dig_ok = False
                    break
            if ineq != dig_ok:
                bad += 1
                print("  MISMATCH", n, j, rho, p, a, ineq, dig_ok)
print(f"  instances checked: {checked}, mismatches: {bad}")
assert bad == 0

# ---------------------------------------------------------------- section C
print("== C. Calibration ==")
# C1: >=5-only (LD3) solutions, n <= 2000, brute force
N2 = 2000
spf2 = spf_upto(N2 + 1)
six = []
for n in range(7, N2 + 1):
    fac = {m: fac_small(m, spf2) for m in (n, n - 1, n - 2)}
    rel5 = [(rho, p, a, q) for rho, p, a, q in relevant_tops(n, fac) if p >= 5]
    for j in range(4, n // 2 + 1):
        if all(j % q <= rho for rho, p, a, q in rel5):
            six.append((n, j))
print(f"  >=5-only (LD3) solutions, n <= 2000: {six}")
assert six == [(10, 5), (28, 14), (82, 41), (162, 70), (244, 122), (730, 365)]
# C2: for each, the full-(LD3) witness and the (LD3+) digit failures
for (n, j) in six:
    fac = {m: fac_small(m, spf2) for m in (n, n - 1, n - 2)}
    w = ld3_wit(n, j, fac)
    pf = ld3plus_fails(n, j, fac)
    print(f"    ({n},{j}): full-(LD3) witnesses {w}; (LD3+) failing digits {pf}; "
          f"gcd = {gcd(V3(n), comb(n, j))}")
# C3: family n = 3^a + 1, j = n/2, a = 2..12: digit patterns
for a in range(2, 13):
    n = 3 ** a + 1
    j = n // 2
    dn = digits(n, 3)
    dj = digits(j, 3)
    L = max(len(dn), len(dj), a + 1)
    dn += [0] * (L - len(dn))
    dj += [0] * (L - len(dj))
    assert dn[0] == 1 and dn[a] == 1 and all(dn[e] == 0 for e in range(1, a))
    assert dj[0] == 2 and all(dj[e] == 1 for e in range(1, a)) and dj[a] == 0
    spfN = spf_upto(n + 1)
    fac = {m: fac_small(m, spfN) for m in (n, n - 1, n - 2)}
    pf = ld3plus_fails(n, j, fac)
    assert pf.get(3) == list(range(a)), pf
    tail3_ok = all(dj[e] <= dn[e] for e in range(a, L))
    print(f"    3^{a}+1: n={n}, j={j}, p=3 failing digits {pf[3]} (all < a={a}), "
          f"tail (digits >= a) passes: {tail3_ok}")
    assert tail3_ok
# C4: family n = 3^a - 1, j = n/2, a = 2..8
for a in range(2, 9):
    n = 3 ** a - 1
    j = n // 2
    spfN = spf_upto(n + 1)
    fac = {m: fac_small(m, spfN) for m in (n, n - 1, n - 2)}
    v3s = [fac[n - r].get(3, 0) for r in range(3)]
    w = ld3_wit(n, j, fac)
    pf = ld3plus_fails(n, j, fac)
    print(f"    3^{a}-1: n={n}, j={j}, v3 of tops {v3s} (so 3 does not divide "
          f"C(n,3)), first (LD3) witness {w[0]}, (LD3+) failures {pf}")
    assert v3s == [0, 0, 1] and w
# C5: family n = 2*3^a + 1, a = 2..6, j in {n//3, n//2}
for a in range(2, 7):
    n = 2 * 3 ** a + 1
    spfN = spf_upto(n + 1)
    fac = {m: fac_small(m, spfN) for m in (n, n - 1, n - 2)}
    for j in sorted({n // 3, n // 2}):
        if 3 < j <= n // 2:
            w = ld3_wit(n, j, fac)
            print(f"    2*3^{a}+1: n={n}, j={j}, first (LD3) witness {w[0]}")
            assert w and w[0][0] == 0

# ---------------------------------------------------------------- section D
print("== D. Per-prime tail strictness ==")
# D1: infinite family at p = 5: n = 50w + 30, j = 25w + 15 = n/2
for w in range(0, 201):
    n = 50 * w + 30
    j = 25 * w + 15
    m = n
    a5 = 0
    while m % 5 == 0:
        m //= 5
        a5 += 1
    assert a5 == 1                      # 5 || n, rho = 0, q = 5
    assert j % 5 == 0                   # (LD3) clause for p = 5 passes (low digit)
    dn = digits(n, 5)
    dj = digits(j, 5)
    assert dj[0] <= dn[0] and dj[1] > dn[1]   # digit 1 (the tail) fails
print("  family n = 50w+30, j = n/2 (w = 0..200): v5(n) = 1, (LD3) clause at "
      "p = 5 passes, digit-1 (tail) condition at p = 5 fails: verified")
# D2: instance counts, n <= 2000.  low_p via the proved equivalence
# (j mod q <= rho); tail_p checked digit by digit on floor(j/q) vs K.
cnt = {"low_pass_tail_fail": 0, "low_pass_tail_pass": 0, "low_fail": 0}
tot_i = 0
for n in range(7, 2001):
    fac = {m: fac_small(m, spf2) for m in (n, n - 1, n - 2)}
    rel = relevant_tops(n, fac)
    if not rel:
        continue
    info = []
    for rho, p, a, q in rel:
        K = (n - rho) // q
        info.append((rho, p, a, q, K))
    for j in range(4, n // 2 + 1):
        for rho, p, a, q, K in info:
            tot_i += 1
            if j % q > rho:
                cnt["low_fail"] += 1
            else:
                jj = j // q
                kk = K
                tail_ok = True
                while jj or kk:
                    if jj % p > kk % p:
                        tail_ok = False
                        break
                    jj //= p
                    kk //= p
                if tail_ok:
                    cnt["low_pass_tail_pass"] += 1
                else:
                    cnt["low_pass_tail_fail"] += 1
print(f"  instances (n,j,p), n <= 2000: total {tot_i}, counts {cnt}")

# ---------------------------------------------------------------- section E
print("== E. h = 0 finiteness lemma: validation for even n <= 200000 ==")
def Fset(Lam):
    """{3^b * u : u | Lam, gcd(u,3) = 1, 0 <= b <= v3(Lam)+1}."""
    v3 = 0
    t = Lam
    while t % 3 == 0:
        t //= 3
        v3 += 1
    f = fac_big(t)
    divs = [1]
    for p, a in f.items():
        divs = [d * p ** k for d in divs for k in range(a + 1)]
    return {(3 ** b) * u for b in range(0, v3 + 2) for u in divs}

LAMBDAS = [15, 105, 315, 3465, 45045, 765765, 14549535]
FSETS = {Lam: Fset(Lam) for Lam in LAMBDAS}
spfE = spf_upto(200001)
viol = 0
hits = {Lam: 0 for Lam in LAMBDAS}
for n in range(8, 200001, 2):
    v = V3(n)
    for Lam in LAMBDAS:
        if v <= Lam and Lam % v == 0:
            hits[Lam] += 1
            if (n - 1) not in FSETS[Lam]:
                viol += 1
                print("  LEMMA VIOLATION", n, Lam)
print(f"  V3(n) | Lambda hits (even n <= 200000): {hits}; lemma violations: {viol}")
assert viol == 0

# ---------------------------------------------------------------- section F
print("== F. Row enumerations ==")
def row_pipeline(Q, R, ncap=10 ** 8, brute_upto=200000):
    """h = 0 rows (R >= 3). Stage 1: n even, n - 1 in F(Lambda) (necessary
    for V3(n) | Lambda), n = Qj + R, j > 3. Stage 2: V3(n) | Lambda.
    Then (LD3) and (LD3+) on stage 2. Returns summary dict."""
    T = R + 2 * (Q - 1)
    Lam = Lambda3(T)
    F = Fset(Lam)
    s1 = []
    for m in sorted(F):
        n = m + 1
        if n > ncap or n % 2 == 1:
            continue
        if (n - R) % Q != 0:
            continue
        j = (n - R) // Q
        if j <= 3:
            continue
        s1.append((n, j))
    s2 = []
    for (n, j) in s1:
        v = V3(n)
        if v <= Lam and Lam % v == 0:
            s2.append((n, j))
    ld3surv = []
    plussurv = []
    wits = {}
    for (n, j) in s2:
        fac = {m: fac_big(m) for m in (n, n - 1, n - 2)}
        w = ld3_wit(n, j, fac)
        wits[(n, j)] = w
        if not w:
            ld3surv.append((n, j))
            if not ld3plus_fails(n, j, fac):
                plussurv.append((n, j))
    # brute-force cross-check of stage 1+2 in range
    brute = []
    n = Q * 4 + R
    while n <= brute_upto:
        if n % 2 == 0:
            j = (n - R) // Q
            if j > 3:
                v = V3(n)
                if v <= Lam and Lam % v == 0:
                    brute.append((n, j))
        n += Q
    assert brute == [p for p in s2 if p[0] <= brute_upto], (Q, R, brute, s2)
    return {"QR": (Q, R), "T": T, "Lam": Lam, "stage1": s1, "stage2": s2,
            "ld3surv": ld3surv, "plussurv": plussurv, "wits": wits,
            "global_bound": max(F) + 1}

# F1: row (2,4), the task's primary class, by TWO parametrisations to 10^8
S15 = [1, 3, 9, 5, 15, 45]   # odd parts 3^b * u, b <= 2, u in {1,5}
candA = set()
for o in S15:
    m = o
    while m <= 10 ** 8:
        candA.add(m)
        if m > 10 ** 8 // 2:
            break
        m *= 2
memA = sorted(n for n in candA if (lambda v: v <= 15 and 15 % v == 0)(V3(n)))
print(f"  (2,4) method A (n = 2^alpha * odd, odd in {S15}): "
      f"{len(candA)} candidates n <= 10^8; V3 | 15 members: {memA} "
      f"(neither lies in the row with j > 3)")
r24 = row_pipeline(2, 4)
print(f"  (2,4) method B (n - 1 in F(15) = {sorted(Fset(15))}): stage1 "
      f"{r24['stage1']}, stage2 {r24['stage2']}, global bound n <= "
      f"{r24['global_bound']}")
assert r24["stage2"] == [] and r24["ld3surv"] == [] and r24["plussurv"] == []
# F2: rows (2,6) and (3,4)
for QR in [(2, 6), (3, 4)]:
    r = row_pipeline(*QR)
    print(f"  {QR} T={r['T']} Lambda={r['Lam']}: stage1 {len(r['stage1'])} "
          f"{r['stage1']}; stage2 {r['stage2']}; (LD3) witnesses "
          f"{ {k: v for k, v in r['wits'].items()} }; (LD3) survivors "
          f"{r['ld3surv']}; (LD3+) survivors {r['plussurv']}; global bound "
          f"n <= {r['global_bound']}")
    assert r["ld3surv"] == [] and r["plussurv"] == []
# F3: (4,2) cross-check (h = 1 row; finite set from F1.9(b)/V-F §5)
cand42 = []
for b in range(0, 3):
    for a5 in range(0, 2):
        for c7 in range(0, 2):
            m = (3 ** b) * (5 ** a5) * (7 ** c7)
            if m % 4 != 1:
                continue
            n = m + 1
            if (n - 2) % 4 != 0:
                continue
            j = (n - 2) // 4
            if j >= 5:
                cand42.append((n, j))
cand42 = sorted(set(cand42))
print(f"  (4,2) candidates from m = 3^b 5^a 7^c, b<=2, a,c<=1, m = 1 mod 4: "
      f"{cand42}")
assert cand42 == [(22, 5), (46, 11), (106, 26)]
for (n, j) in cand42:
    fac = {m: fac_big(m) for m in (n, n - 1, n - 2)}
    w = ld3_wit(n, j, fac)
    pf = ld3plus_fails(n, j, fac)
    g = gcd(V3(n), comb(n, j))
    print(f"    ({n},{j}): (LD3) witnesses {w}; (LD3+) failures {pf}; gcd {g}")
    assert w and pf and g > 1
# F4: aggregate h = 0 sweep, Q = 2..8, T <= 20
tot1 = tot2 = 0
rows_done = 0
max_n_stage2 = 0
for Q in range(2, 9):
    for R in range(3, 40):
        T = R + 2 * (Q - 1)
        if T > 20:
            continue
        r = row_pipeline(Q, R)
        rows_done += 1
        tot1 += len(r["stage1"])
        tot2 += len(r["stage2"])
        if r["stage2"]:
            max_n_stage2 = max(max_n_stage2, max(n for n, j in r["stage2"]))
        assert r["ld3surv"] == [] and r["plussurv"] == [], (Q, R, r)
print(f"  aggregate h=0 sweep (Q = 2..8, T <= 20): {rows_done} rows; "
      f"stage1 total {tot1}; stage2 (V3 | Lambda) total {tot2}; largest n "
      f"among stage2 pairs {max_n_stage2}; (LD3) survivors 0; (LD3+) "
      f"survivors 0 (vacuous: no (LD3) survivors to test)")

print(f"\nALL CHECKS PASSED. Total runtime: {time.time() - T_START:.1f} s")
