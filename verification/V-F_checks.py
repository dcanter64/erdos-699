#!/usr/bin/env python3
"""Independent verifier V-F checks (Cluster F, i=3). Stdlib only, exact,
single thread. Implementation choices deliberately differ from
P-F1_checks.py: per-pair (LD3) recount by global R(n)=d candidate
generation + trial-division factorisation; n<=10^6 recount by a
prime-power sieve for R(m) plus SPF factorisation of candidate tops.

Execution note (V-F): Section A of this file was run as written
(after fixing an infinite loop at C(0,3)=0 in the v2-fraction line).
Sections D and F were executed via the standalone files
V-F_chunkD.py and V-F_chunkF.py (same methods, bounded chunks), and
the brute-force/random/section-C checks via V-F_chunkEG.py; see
V-F.md for the outputs. The D/F sections below are the original
single-file versions and were not run to completion in this form.
"""
import math, time, json, random
from math import comb, gcd
from array import array
T0 = time.time()
def note(m): print(f"[{time.time()-T0:7.1f}s] {m}", flush=True)

def primes_upto(n):
    s = bytearray(b"\x01") * (n + 1); s[0:2] = b"\x00\x00"
    for i in range(2, int(n ** 0.5) + 1):
        if s[i]: s[i*i:n+1:i] = b"\x00" * (((n - i*i)//i) + 1)
    return [i for i, v in enumerate(s) if v]

PR4505 = primes_upto(4505)

def lam(T):
    if T <= 2: return 1
    out = 1
    for q in primes_upto(T):
        if q < 3: continue
        pw = q
        while pw * q <= T: pw *= q
        out *= pw
    return out

def N_of_3(j):
    target = comb(2*j, 6); lo, hi = 3, 6
    while comb(hi, 3) < target: hi *= 2
    while lo + 1 < hi:
        mid = (lo + hi)//2
        if comb(mid, 3) < target: lo = mid
        else: hi = mid
    return lo

def v_p_int(x, p):
    a = 0
    while x % p == 0: x //= p; a += 1
    return a

def odd_part_binom3(n):
    c = comb(n, 3)
    while c % 2 == 0: c //= 2
    return c

def factor_trial(m):
    out = []; x = m
    for p in PR4505:
        if p * p > x: break
        if x % p == 0:
            a = 0
            while x % p == 0: x //= p; a += 1
            out.append((p, a))
    if x > 1: out.append((x, 1))
    return out

def rel_trial(m):
    return [p**a for p, a in factor_trial(m) if p >= 5 or (p == 3 and a >= 2)]

note("A. small exact checks")
print(" Lambda3:", {T: lam(T) for T in [0,1,2,3,4,5,6,7,8]}, flush=True)
assert [lam(T) for T in [3,4,6,7,8]] == [3,3,15,105,105] and lam(5) == 15 and lam(2) == 1
def Th(Q, R):
    T = R + 2*(Q-1); h = max(0, -((R-3)//Q))
    return T, h, lam(T)
rows = {(2,0):(2,2,1),(2,1):(3,1,3),(2,2):(4,1,3),(3,0):(4,1,3),(3,1):(5,1,15),
        (3,2):(6,1,15),(4,0):(6,1,15),(4,2):(8,1,105)}
for k, v in rows.items():
    got = Th(*k); print("  row", k, got, flush=True); assert got == v
Ns = {7:27, 100:7908, 158:19926, 159:20181, 465:174408, 500:201728,
      1000:808934, 2000:3239787, 5000:20263871}
for j, v in Ns.items():
    got = N_of_3(j); print("  N(3,%d)=%d expect %d" % (j, got, v), flush=True); assert got == v
assert comb(10,3) >= comb(5,3)**2 and comb(12,3) < comb(6,3)**2
def n0(j, v):
    n = 2*j
    while comb(n, 3) <= (1 << v) * comb(j, 3): n += 1
    return n
t4 = [n0(j,4) for j in [6,7,8,10,20]]; t5 = [n0(j,5) for j in [6,7,8,10,20]]
print("  n0 v=4:", t4, " v=5:", t5, flush=True); assert t4 == [14,17,19,24,49] and t5 == [17,20,24,30,62]
c16 = comb(16,3)
assert v_p_int(c16,2) == 4 and odd_part_binom3(16) == 35 == comb(7,3)
assert gcd(odd_part_binom3(16), comb(16,7)) == 5
print("  (16,7) witness OK", flush=True)
cnt32 = sum(1 for n in range(64,96) if v_p_int(comb(n,3),2) <= 3)
print("  residues mod32 with v2(C(n,3))<=3:", cnt32, flush=True); assert cnt32 == 27
frac = sum(1 for n in range(3,100000) if v_p_int(comb(n,3),2) <= 3)  # n<3: C(n,3)=0, excluded
print("  count n in [0,100000) v2<=3:", frac, frac/100000, flush=True)
resid = []
for b in range(3):
    for a5 in range(2):
        for c7 in range(2):
            m = (3**b)*(5**a5)*(7**c7)
            if (m-1) % 4 == 0 and (m-1)//4 >= 5: resid.append((m+1, (m-1)//4))
print("  (4,2) residual:", resid, flush=True)
assert resid == [(22,5),(46,11),(106,26)]
gcds = [gcd(odd_part_binom3(n), comb(n,j)) for n, j in resid]
print("  (4,2) gcds:", gcds, flush=True); assert gcds == [77,69,371]
# each residual fails (LD3): exhibit a violating relevant q
for n, j in resid:
    bad = []
    for r, m in [(0,n),(1,n-1),(2,n-2)]:
        for q in rel_trial(m):
            if j % q > r: bad.append((r, q, j % q))
    print("   (%d,%d) LD3 violations:" % (n,j), bad, flush=True); assert bad

note("B. pairpass row i=3")
d = json.load(open("/home/hatch/workspace/math-hunt/erdos-699/pairpass_20000.json"))
row = d["cleared_js_by_i"]["3"]
print("  len", len(row), "contiguous 5..158:", row == list(range(5,159)), flush=True)
assert row == list(range(5,159))

note("D. per-pair (LD3) recount j<=5000 (global R(n)=d candidates, trial factorisation)")
Nj = {j: N_of_3(j) for j in range(5, 5001)}
NMAX = Nj[5000]
cand = set()
for dd in range(1, 5001):
    if dd % 2 == 0: continue
    v3 = v_p_int(dd, 3)
    if v3 == 1: continue
    t = 1
    while dd * t <= NMAX:
        cand.add(dd * t)
        if v3 == 0: cand.add(dd * 3 * t)
        t *= 2
print("  candidate n count:", len(cand), flush=True)
surv = []; pairs2000 = 0; pairs5000 = 0
for n in sorted(cand):
    Rn = 1
    for p, a in factor_trial(n):
        if p >= 5 or (p == 3 and a >= 2): Rn *= p**a
    assert Rn <= 5000
    rel1 = rel_trial(n-1); rel2 = rel_trial(n-2)
    j = Rn
    while j <= 5000:
        if j >= 5 and 2*j <= n <= Nj[j]:
            pairs5000 += 1
            if j <= 2000: pairs2000 += 1
            if all(j % q <= 1 for q in rel1) and all(j % q <= 2 for q in rel2):
                surv.append((n, j))
        j += Rn
print("  pairs tested (n<=N(3,j)) j<=2000:", pairs2000, " j<=5000:", pairs5000, flush=True)
print("  survivors:", surv, flush=True); assert not surv

note("E. brute-force cross-check all n in [2j,N(3,j)], 5<=j<=60")
bsurv = []
for j in range(5, 61):
    for n in range(2*j, Nj[j]+1):
        if all(j % q == 0 for q in rel_trial(n)) and \
           all(j % q <= 1 for q in rel_trial(n-1)) and \
           all(j % q <= 2 for q in rel_trial(n-2)):
            bsurv.append((n, j))
print("  brute survivors j<=60:", bsurv, flush=True); assert not bsurv

note("F. R(m) sieve to 10^6 + full (LD3) recount + pinned odd family")
L = 10**6
Rarr = [1]*(L+1)
for p in primes_upto(L):
    if p == 2: continue
    q = p
    while q <= L:
        if p >= 5 or q >= 9:  # relevant: p>=5 any power; p=3 only a>=2
            step = q * p
            for m in range(q, L+1, q):
                if m % step != 0: Rarr[m] *= q
        if q > L // p: break
        q *= p
print("  R sieve done; R(10^6)=", Rarr[L], flush=True)
# SPF to 1e6 for factoring tops of candidate n
spf = array("i", range(L+1))
for p in reversed(primes_upto(1000)):
    spf[p::p] = array("i", [p]) * ((L - p)//p + 1)
def factor_spf(x):
    out = []
    while x > 1:
        p = spf[x]; a = 0
        while x % p == 0: x //= p; a += 1
        out.append((p, a))
    return out
def relU_spf(m):
    rel = []; u = 1
    for p, a in factor_spf(m):
        if p >= 5: rel.append(p**a); u *= p**a
        elif p == 3 and a >= 2: rel.append(p**a)
    return rel, u

survF = []; tot4 = 0; even7 = 0; even7_1e5 = 0; n_with = 0
odd_cnt5 = 0; odd_cnt7 = 0; odd_surv = []; n2pass = 0; n2_min = None
for n in range(6, L+1):
    Rn = Rarr[n]
    pinned = (n % 2 == 1 and v_p_int(n, 3) == 1)
    jpin = n//3 if pinned else None
    if pinned:
        if jpin >= 5: odd_cnt5 += 1
        if jpin >= 7: odd_cnt7 += 1
    if Rn > n//2 and not pinned: continue
    rel1, U1 = relU_spf(n-1); rel2, U2 = relU_spf(n-2)
    if pinned and jpin >= 5:
        if U1 * U2 * 6 <= (jpin-1)*(jpin-2):
            n2pass += 1
            if n2_min is None: n2_min = (n, jpin, U1, U2)
        if all(jpin % q <= 1 for q in rel1) and all(jpin % q <= 2 for q in rel2):
            odd_surv.append((n, jpin))
    if Rn > n//2: continue
    n_with += 1
    j = Rn if Rn >= 4 else 4
    while j <= n//2:
        if j % Rn == 0:
            tot4 += 1
            if n % 2 == 0 and j >= 7:
                even7 += 1
                if n <= 10**5: even7_1e5 += 1
            if all(j % q <= 1 for q in rel1) and all(j % q <= 2 for q in rel2):
                survF.append((n, j))
        j += Rn if Rn >= 4 else 1
print("  n with candidates:", n_with, " total pairs j>=4:", tot4, flush=True)
print("  even pairs j>=7:", even7, " even pairs j>=7, n<=1e5:", even7_1e5, flush=True)
print("  full survivors:", survF, flush=True); assert not survF
print("  pinned odd: cnt j>=5:", odd_cnt5, " cnt j>=7:", odd_cnt7,
      " (N2) passes:", n2pass, " smallest:", n2_min, " LD3 survivors:", odd_surv, flush=True)
assert not odd_surv

note("G. independent random check of Lemma F2.2 / dichotomy (own seed 20261029)")
def vp_fact(x, p):
    s = 0
    while x: x //= p; s += x
    return s
def vp_binom(NN, KK, p): return vp_fact(NN,p) - vp_fact(KK,p) - vp_fact(NN-KK,p)
rng = random.Random(20261029); inst = 0; fails = 0
for _ in range(4000):
    n = rng.randrange(20, 3001); j = rng.randrange(7, n//2 + 1); c = n - j
    Q, R = divmod(n, j); T = R + 2*(Q-1); h = max(0, -((R-3)//Q))
    for p in primes_upto(59):
        if p < 3: continue
        a = vp_binom(n, 3, p)
        if a >= 1 and vp_binom(n, j, p) == 0:
            inst += 1; pa = p**a; r = j % pa; s = c % pa
            if not (r + s < 3): fails += 1
            E = R + (Q-1)*r - s
            if E != 0:
                if not (pa <= T): fails += 1
            else:
                if not (r < h and (j - r) % pa == 0): fails += 1
print("  instances:", inst, " failures:", fails, flush=True)
assert fails == 0 and inst > 0
note("ALL V-F CHECKS PASSED")
