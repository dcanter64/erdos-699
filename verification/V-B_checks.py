#!/usr/bin/env python3
"""Verifier B independent checks for P-B1 / P-B2 (Erdos #699, Strategy S1).
Python stdlib only. Stages:
  quick   : pi bound to 10000, Legendre random, F_i monotonic exact rationals,
            T-B endpoints, (3,7) singleton, Delta high precision, B1.10(b) scan
  recount : THIRD recount of T-D -- JK by DIRECT binary search on the exact
            predicate C(j,j-i)*10001**pi(i-1) < C(10001,i) (NOT the floor
            formula K_i = floor((T_i-1)/U_i)); JE taken from pairpass.json.
  spot500 : 500 seeded random (i,j): N_K(i,j) computed directly from the
            definition of F_i (float-guided bracket, exact boundary
            verification F(NK)<=target<F(NK+1)) vs the 10001 predicate.
"""
import sys, os, json, math, random, time
from math import comb
from fractions import Fraction
from decimal import Decimal, getcontext

# ---------- primes / pi ----------
LIM = 10000
sieve = bytearray(b"\x01") * (LIM + 1); sieve[0:2] = b"\x00\x00"
for p in range(2, int(LIM ** .5) + 1):
    if sieve[p]: sieve[p*p::p] = bytearray(len(sieve[p*p::p]))
PRIMES = [p for p in range(LIM + 1) if sieve[p]]
import bisect
def pi(x): return bisect.bisect_right(PRIMES, x)

def q_p(p, n):
    e = 0; pw = p
    while pw <= n: e += 1; pw *= p
    return p ** e
def Usharp(n, i): 
    r = 1
    for p in PRIMES:
        if p >= i: break
        r *= q_p(p, n)
    return r

def quick():
    t0 = time.time()
    # --- pi(i-1) <= i/2 for i<=10000, equality set ---
    viol = []; eq = []
    for i in range(1, 10001):
        lhs = 2 * pi(i - 1)
        if lhs > i: viol.append(i)
        if lhs == i: eq.append(i)
    print(f"PI: violations i<=10000: {viol}; equality pi(i-1)=i/2 at i={eq}")
    # pi=0,1 characterisations used in Bernoulli case split
    print("PI: pi(i-1)=0 for i in", [i for i in range(1,8) if pi(i-1)==0],
          "; =1 for i in", [i for i in range(1,8) if pi(i-1)==1])
    # --- Legendre: summands in {0,1}, vanish for p^e>n, v_p bound, random ---
    rng = random.Random(699)
    bad = 0; maxvp = 0
    for _ in range(3000):
        n = rng.randint(1, 500); i = rng.randint(1, n)
        p = PRIMES[rng.randrange(pi(n))] if n >= 2 else 2
        # exact v_p by repeated division of comb
        c = comb(n, i); v = 0
        while c % p == 0: c //= p; v += 1
        s = 0; e = 1
        while p ** e <= 3 * n:  # include e with p^e>n to test vanishing
            term = n // p**e - i // p**e - (n - i) // p**e
            if term not in (0, 1): bad += 1
            if p ** e > n and term != 0: bad += 1
            if p ** e <= n: s += term
            e += 1
        if s != v: bad += 1
        if p ** v > q_p(p, n) or q_p(p, n) > n: bad += 1
    print(f"LEGENDRE: 3000 random (n,i,p): violations={bad} (summand set, vanishing, sum=v_p, p^v<=q_p<=n)")
    # edge: i>n/2 included above (i uniform in 1..n); also i=n, i=n-1 explicit
    for (n, i) in [(97, 96), (97, 97), (128, 127), (100, 99)]:
        for p in PRIMES:
            if p > n: break
            c = comb(n, i); v = 0
            while c % p == 0: c //= p; v += 1
            assert p ** v <= q_p(p, n) <= n, (n, i, p)
    print("LEGENDRE edge i in {n-1,n}: OK")
    # --- F_i strictly increasing, exact Fractions, i<=40, i<=n<300 (B1's range) ---
    fails = 0
    for i in range(1, 41):
        pr = pi(i - 1)
        prev = None
        for n in range(i, 300):
            f = Fraction(comb(n, i), n ** pr) if pr else Fraction(comb(n, i), 1)
            if prev is not None and not f > prev: fails += 1
            prev = f
    print(f"F_MONOTONE exact Fractions i<=40, n<300: failures={fails}")
    # growth bound spot: F_i(n) >= n^(i-pi)/i^i
    gbad = 0
    for i in range(1, 60):
        for n in (i, i + 1, 2 * i, 10 * i):
            if Fraction(comb(n, i), n ** pi(i-1)) < Fraction(n ** (i - pi(i-1)), i ** i): gbad += 1
    print(f"F_GROWTH bound spot failures={gbad}")
    # --- T-B endpoints, exact ---
    print("TB i=1: correct target C(j,j-1)=j (NOT C(j,0)=1); n>=2j>j contradiction OK")
    print("TB i=2: C(2j,2)=j(2j-1) vs C(j,2)=j(j-1)/2, strict for j>=3:",
          all(comb(2*j,2) > comb(j,2) for j in range(3, 500)))
    print(f"TB (3,5): F3(10)={Fraction(comb(10,3),10)} vs target C(5,2)={comb(5,2)} -> closed:",
          Fraction(comb(10,3),10) > comb(5,2))
    print(f"TB (3,5) crude fails? F3(10)>10 so crude suffices. "
          f"(3,6): F3(12)={Fraction(comb(12,3),12)} vs 20 (crude fails: {Fraction(comb(12,3),12)<=20}); "
          f"Usharp[12,15]={set(Usharp(n,3) for n in range(12,16))}; G3(12)={Fraction(comb(12,3),8)} vs C(6,3)={comb(6,3)}; "
          f"F3(16)={Fraction(comb(16,3),16)} > 20: {Fraction(comb(16,3),16)>20}")
    # --- (3,7) singleton, direct ---
    tgt = comb(7, 4)
    badset = []
    for n in range(14, 5000):
        if Fraction(comb(n,3), Usharp(n,3)) <= tgt: badset.append(n)
        if n >= 17 and Fraction(comb(n,3), n) > tgt and n > 100:
            pass
    # finiteness cut: for n>=17, G>=F>=F(17)=40>35 and F increasing => stop at, say, n where F(n)>35 and n>=17: all n>=17 excluded; scan 14..16 suffices + proof; scan to 2000 for certainty
    badset = [n for n in range(14, 2001) if Fraction(comb(n,3), Usharp(n,3)) <= tgt]
    print(f"(3,7): Badsharp(14..2000)={badset}, target={tgt}, G3(14)={Fraction(comb(14,3),8)}, "
          f"G3(15)={Fraction(comb(15,3),8)}, G3(16)={Fraction(comb(16,3),16)}, F3(17)={Fraction(comb(17,3),17)}")
    # v2 of C(16,3) and equality u=Usharp=U=16
    c = comb(16,3); v2 = 0
    while c % 2 == 0: c //= 2; v2 += 1
    print(f"(3,7) equality: v2(C(16,3))={v2}, u=2^v2={2**v2}, Usharp(16,3)={Usharp(16,3)}, U(16,3)={16**pi(2)}, "
          f"C(16,3)={comb(16,3)} = 16*35 = {16*35}; gcd(v=35,C(16,7))={math.gcd(35, comb(16,7))}, C(16,7)={comb(16,7)}")
    # Legendre display in B1 remark: terms (8-1-6)+(4-0-3)+(2-0-1)+(1-0-0)
    terms = [16//2**e - 3//2**e - 13//2**e for e in range(1,5)]
    print(f"(3,7) Legendre terms e=1..4: {terms} sum={sum(terms)}")
    # --- Delta high precision (Decimal, prec 60) ---
    getcontext().prec = 60
    D = Decimal
    def Delta(c):
        return 2*c*(2*c).ln() - (2*c-1)*(2*c-1).ln() - c*c.ln() + ((c-1)*(c-1).ln() if c != 1 else D(0))
    for cs in ["1","1.36","1.3672","1.3673","1.37","1.5","2"]:
        print(f"DELTA({cs}) = {Delta(D(cs)):.12f}")
    lo, hi = D("1.3672"), D("1.3673")
    print(f"DELTA bracket: Delta(1.3672)>1: {Delta(lo)>1}, Delta(1.3673)<1: {Delta(hi)<1}")
    a, b = D(1), D(2)
    for _ in range(200):
        m = (a+b)/2
        if Delta(m) > 1: a = m
        else: b = m
    print(f"DELTA root c* = {(a+b)/2:.15f}  (in (1.3672,1.3673): {lo < (a+b)/2 < hi})")
    # derivative: closed form vs central difference (float, and Decimal)
    def Delta_f(c): return 2*c*math.log(2*c) - (2*c-1)*math.log(2*c-1) - c*math.log(c) + (c-1)*math.log(c-1)
    for c in (1.1, 1.3672, 1.5, 2.0, 5.0):
        num = (Delta_f(c+1e-6) - Delta_f(c-1e-6)) / 2e-6
        closed = math.log(4*c*(c-1)/(2*c-1)**2)
        print(f"DELTA' c={c}: numeric={num:.10f} closed log(4c(c-1)/(2c-1)^2)={closed:.10f} neg={closed<0}")
    # --- B1.10(b) exact scan ---
    cnt_open = 0; allneg = True; closest = (None, 0.0)
    for i in range(4, 61):
        A = comb(3*i//2 + 1, i) if False else None
        # iterate j from i upward maintaining A=C(j,i), B=C(2j,i)
        A = comb(i, i); B = comb(2*i, i); j = i
        # advance to first open j
        while j <= 2000:
            if j > 3*i//2:
                cnt_open += 1
                U = Usharp(2*j, i)
                if not (B < A * U): allneg = False; print("  B1.10b FAIL", i, j)
                r = math.log(B) - math.log(A) - math.log(U) if False else None
                # float margin via lgamma
                lm = (math.lgamma(2*j+1)-math.lgamma(i+1)-math.lgamma(2*j-i+1)
                      - (math.lgamma(j+1)-math.lgamma(i+1)-math.lgamma(j-i+1)) - math.log(U))
                if closest[0] is None or lm > closest[1]: closest = ((i, j), lm)
            # step j -> j+1
            A = A * (j+1) // (j+1-i)
            B = B * (2*j+2) * (2*j+1) // ((2*j+2-i) * (2*j+1-i))
            j += 1
    print(f"B1.10(b) i=4..60 open j<=2000: pairs={cnt_open}, all Rsharp<0 exact: {allneg}, closest (i,j,margin)={closest}")
    allneg3 = True
    A = comb(8,3); B = comb(16,3); j = 8
    A = comb(7,3); B = comb(14,3); j = 7
    while j < 2000:
        j += 1
        A = A * j // (j-3); B = B * (2*j-2+2) * (2*j-2+1) // ((2*j-2+2-3)*(2*j-2+1-3)) if False else B
        # recompute B directly every step is costly; use recurrence from previous 2(j-1):
        # handled below by direct comb every 1 step for i=3 (cheap)
        B = comb(2*j, 3)
        if not (B < A * Usharp(2*j, 3)): allneg3 = False; print("  B1.10b i=3 FAIL", j)
    print(f"B1.10(b) i=3, 8<=j<=2000: all Rsharp<0 exact: {allneg3}")
    print(f"QUICK elapsed {time.time()-t0:.1f}s")

def recount():
    t0 = time.time()
    pp = json.load(open(os.path.expanduser('~/workspace/math-hunt/erdos-699/pairpass.json')))
    cleared = pp['cleared_js_by_i']
    def pred_factory(i):
        T = comb(10001, i); U = 10001 ** pi(i - 1)
        return (lambda j: comb(j, j - i) * U < T), T, U
    total_new = total_new_ge3 = total_E = total_K = total_open = 0
    JK = {}; JE = {}; pp_mismatch = 0
    for i in range(1, 1001):
        lo = 3*i//2 + 1
        lst = cleared[str(i)]
        # verify pairpass list is exactly the prefix [lo .. JE]
        jE = max(lst) if lst else lo - 1
        if lst != list(range(lo, jE + 1)): pp_mismatch += 1
        JE[i] = jE
        pred, T, U = pred_factory(i)
        # direct binary search on exact predicate over j in [i, 5000]; predicate is prefix (C(j,i) increasing)
        if not pred(i):
            jK = i - 1
        elif pred(5000):
            jK = 5000
        else:
            a, b = i, 5000
            while b - a > 1:
                m = (a + b)//2
                if pred(m): a = m
                else: b = m
            jK = a
        JK[i] = jK
        total_open += 5000 - lo + 1
        total_E += max(0, jE - lo + 1)
        total_K += max(0, min(jK, 5000) - lo + 1)
        new = max(0, min(jK, 5000) - max(lo - 1, jE))
        total_new += new
        if i >= 3: total_new_ge3 += new
    print(f"RECOUNT: open={total_open} EEES(from pairpass)={total_E} Kummer_open={total_K} "
          f"NEW={total_new} NEW_i_ge3={total_new_ge3} NEW_i12={total_new-total_new_ge3} UNION={total_E+total_new}")
    print(f"RECOUNT spots: JK(100)={JK[100]} JE(100)={JE[100]} JK(1000)={JK[1000]} JE(1000)={JE[1000]}")
    for i in (3,5,10,11,50,100,500,1000):
        print(f"  spot i={i}: JE={JE[i]} JK={JK[i]}")
    exc = [i for i in range(1,31) if JK[i] <= JE[i]]
    print(f"RECOUNT i<=30 with JK<=JE: {exc}")
    print(f"RECOUNT pairpass prefix-structure mismatches: {pp_mismatch}; pairpass totals in file: "
          f"considered={pp['pairs_considered']} cleared={pp['pairs_fully_cleared']}")
    print(f"RECOUNT elapsed {time.time()-t0:.1f}s")
    return JK, JE

def spot500():
    t0 = time.time()
    rng = random.Random(20261028)
    mism = 0; worst_adj = 0
    for trial in range(500):
        i = rng.randint(1, 1000)
        lo = 3*i//2 + 1
        j = rng.randint(lo, 5000)
        pr = pi(i - 1)
        target = comb(j, j - i)
        pred = target * (10001 ** pr) < comb(10001, i)   # N_K <= 10000 ?
        # direct N_K: float-guided bracket, then exact boundary verification
        lt = math.lgamma(j+1) - math.lgamma(i+1) - math.lgamma(j-i+1)  # log target = log C(j,i)
        def logF(n):
            return math.lgamma(n+1) - math.lgamma(i+1) - math.lgamma(n-i+1) - pr * math.log(n)
        hi = max(2*j, i + 1)
        while logF(hi) <= lt: hi *= 2
        a, b = i, hi
        for _ in range(200):
            m = (a + b) / 2
            if logF(m) <= lt: a = m
            else: b = m
        n0 = int(a)
        def Fle(n):  # exact: F_i(n) <= target  <=>  C(n,i) <= target * n**pi
            return comb(n, i) <= target * (n ** pr)
        adj = 0
        while n0 >= i and not Fle(n0): n0 -= 1; adj += 1
        while Fle(n0 + 1): n0 += 1; adj += 1
        worst_adj = max(worst_adj, adj)
        assert Fle(n0) and not Fle(n0 + 1)
        nk_le = n0 <= 10000
        if nk_le != pred:
            mism += 1; print("  SPOT MISMATCH", i, j, "NK", n0, "pred", pred)
    print(f"SPOT500: mismatches={mism}/500, worst exact-adjustment steps={worst_adj}, elapsed {time.time()-t0:.1f}s")

if __name__ == "__main__":
    stage = sys.argv[1] if len(sys.argv) > 1 else "all"
    if stage in ("quick", "all"): quick()
    if stage in ("recount", "all"): recount()
    if stage in ("spot500", "all"): spot500()
