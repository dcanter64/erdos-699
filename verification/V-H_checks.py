#!/usr/bin/env python3
"""V-H independent checks (stdlib only, exact arithmetic).
Covers: numerics of Claims 4-6 (H1), 5,6,10,11 (H2), J1 counts,
combined-cap recount (Claim 13/14 both), EEES exception R1 triples,
Claim 9 arithmetic, large-i sanity, N values.
The i<=1000 / i<=2000 primorial scans live in V-H_scan.py.
"""
import math, random
from math import comb, isqrt, gcd, log, lgamma, fsum

def primes_upto(b):
    s = bytearray(b"\x01") * (b + 1); s[0:2] = b"\x00\x00"
    for q in range(2, int(b**0.5) + 1):
        if s[q]: s[q*q::q] = b"\x00" * ((b - q*q)//q + 1)
    return [x for x in range(b + 1) if s[x]]

def vp_fact(N, p):
    t = 0
    while N: N //= p; t += N
    return t
def vp_binom(n, k, p):
    return vp_fact(n, p) - vp_fact(k, p) - vp_fact(n-k, p)

def N_of(i, j):
    target = comb(2*j, 2*(j-i)); n = 2*j
    while comb(n, i) < target: n += 1
    return n - 1

def Qprod(i, j, primes):
    v = 1
    for p in primes:
        if i < p <= j: v *= p
    return v

print("== N values ==")
for (i,j,exp) in [(4,7,17),(10,19,55),(39,59,119),(39,61,130),(59,113,337)]:
    v = N_of(i,j); print((i,j), v, "OK" if v==exp else f"MISMATCH exp {exp}")

print("\n== (119,39,59) numerics ==")
P = 41*43*47*53*59
print("prod bad =", P)
C5939 = comb(59,39); print("C(59,39) =", C5939, "quotient =", C5939//P, "divides:", C5939 % P == 0)
for N in (118,119,238):
    v = comb(N,39); print(f"C({N},39) =", v, "isqrt =", isqrt(v))
print("C(118,39)-C(59,39)^2 =", comb(118,39)-C5939**2, " ratio F =", comb(118,39)/C5939**2)
print("C(60,39) =", comb(60,39)); print("C(120,39) =", comb(120,39))
print("ratio (39,60) =", comb(120,39)/comb(60,39)**2)
print("diff C(60,39)-isqrt(C(120,39)) =", comb(60,39)-isqrt(comb(120,39)))
print("P^2 =", P*P, " P^2 vs C(120,39): ratio C/P^2 =", comb(120,39)/(P*P))
S119 = [p for p in primes_upto(119) if p >= 39 and vp_binom(119,39,p) > 0]
V = 1
for p in S119: V *= p ** vp_binom(119,39,p)
print("S(119,39) =", S119, "V =", V, "V^2>C(119,39):", V*V > comb(119,39))
print("extra primes >59:", [p for p in S119 if p > 59], "Qextra =", V//P)
print("sqrt ratios: C118^0.5/P ~", isqrt(comb(118,39))/P, " C119^0.5/P ~", isqrt(comb(119,39))/P,
      " C238^0.5/P ~", isqrt(comb(238,39))/P)
print("H2 (b): C(118,39)/P^2 =", comb(118,39)//(P*P), "exact float", comb(118,39)/(P*P))
# (39,61) and (122,39,61)
pr = primes_upto(200)
Q61 = Qprod(39,61,pr); print("Q(39,61) =", Q61, "Q^2 =", Q61*Q61, "C(122,39) =", comb(122,39))
S122 = [p for p in primes_upto(122) if 39 <= p <= 61 and vp_binom(122,39,p) > 0]
bad122 = []
for p in S122:
    e = vp_binom(122,39,p)
    D = (vp_fact(61,p)-vp_fact(39,p)) - (vp_fact(122-39,p)-vp_fact(122-61,p))
    if D >= e: bad122.append(p)
print("S122 in-range =", S122, "bad =", bad122)

print("\n== J1 ==")
def J1(i, jcap=100000):
    # largest j with C(2j,i) >= C(j,i)^2, scanning upward from i+1
    last = None; j = i+1
    while j <= jcap:
        if comb(2*j,i) >= comb(j,i)**2: last = j; j += 1
        else: break
    return last
for i,exp in [(3,5),(5,8),(39,59)]:
    v = J1(i); print("J1", i, v, "OK" if v==exp else f"MISMATCH exp {exp}")
for i,exp in [(640,962),(5000,7503)]:
    v = J1(i); print("J1", i, v, "OK" if v==exp else f"MISMATCH exp {exp}")

print("\n== i<40 counts: R1 total, J1-closed, crude-closed, sharpened-closed, failures ==")
tot=0; j1c=0; crudec=0; sharpc=0; crude_list=[]; sharp_fails=[]; j1_list=[]
pr40 = primes_upto(80)
for i in range(1,40):
    for j in range(i+1, 2*i):
        if 2*j <= 3*i: continue
        tot += 1
        if comb(2*j,i) >= comb(j,i)**2: j1c += 1; j1_list.append((i,j))
        # crude: bmax = max b with i^b <= C(j,i); closed iff j^(2*bmax) <= C(2j,i)
        Cji = comb(j,i); bmax = 0
        while i**(bmax+1) <= Cji: bmax += 1
        if j**(2*bmax) <= comb(2*j,i): crudec += 1; crude_list.append((i,j))
        Qv = Qprod(i,j,pr40)
        if Qv*Qv <= comb(2*j,i): sharpc += 1
        else: sharp_fails.append((i,j))
print("total R1 i<40 =", tot, "J1 closed =", j1c, "crude closed =", crudec, "sharpened closed =", sharpc)
print("crude list =", crude_list)
print("sharpened fails i<40 =", sharp_fails)
# crude at (39,59),(39,60): bounds on b
for (i,j) in [(39,59),(39,60)]:
    lo = 0.5*log(comb(2*j,i))/log(j); hi = log(comb(j,i))/log(i)
    print(f"crude ({i},{j}): {lo:.4f} < b <= {hi:.4f}")

print("\n== H2 Claim 10 table ==")
for (i,j) in [(39,59),(39,61),(59,113),(4,7),(10,19)]:
    prx = primes_upto(j)
    Qv = Qprod(i,j,prx)
    lo = log(comb(2*j,i))/(2*log(j))
    picnt = len([p for p in prx if i < p <= j])
    hi2 = log(Qv)/log(i)
    print(f"({i},{j}): lower B > {lo:.4f}, pi-diff = {picnt}, lnQ/lni = {hi2:.4f}, Q = {Qv}")

print("\n== H2 Claim 11 barrier integers ==")
print("C(7,4) =", comb(7,4), "35 divides, quotient", comb(7,4)//35)
print("C(19,10) =", comb(19,10), "46189 divides, quotient", comb(19,10)//46189, "rem", comb(19,10)%46189)
print("Q(10,19) =", Qprod(10,19,primes_upto(19)), "Q^2 =", 46189**2, "C(38,10) =", comb(38,10))
print("Q(4,7) =", Qprod(4,7,primes_upto(7)), "Q^2 =", 35**2, "C(14,4) =", comb(14,4))

print("\n== Claim 12 CRT/density ==")
print("prod(p-d) =", 21*23*27*33*39, "density =", (21*23*27*33*39)/259106347)
print("ratio form =", (21/41)*(23/43)*(27/47)*(33/53)*(39/59))
for n in (118,119):
    ok = all(vp_binom(n,39,p)==1 and ((vp_fact(59,p)-vp_fact(39,p))-(vp_fact(n-39,p)-vp_fact(n-59,p)))>=1 for p in (41,43,47,53,59))
    print(f"n={n} all five bad with e=1:", ok)

print("\n== Claim 13/14 combined-cap recount (i<40) ==")
window=[]; combined=[]; scanned=0; pairs_used=0
for i in range(1,40):
    for j in range(i+1,2*i):
        if 2*j <= 3*i: continue
        d=j-i; N=N_of(i,j)
        if N < 2*j: continue
        pairs_used += 1
        primes=[p for p in primes_upto(j) if p>=i]
        kl={p: vp_binom(j,d,p) for p in primes}
        for n in range(2*j, N+1):
            scanned += 1
            S=[]; data={}
            for p in primes:
                e=vp_binom(n,i,p)
                if e>0:
                    S.append(p)
                    data[p]=(e,(vp_fact(j,p)-vp_fact(i,p))-(vp_fact(n-i,p)-vp_fact(n-j,p)))
            if len(S)>=3 and all(data[p][1]>=data[p][0] for p in S):
                window.append((n,i,j,tuple(S)))
                if all(data[p][0]<=kl[p] for p in S): combined.append((n,i,j,tuple(S)))
from collections import Counter
print("pairs with N>=2j:", pairs_used, "scanned triples:", scanned)
print("window =", len(window), "combined =", len(combined), "killed =", len(window)-len(combined))
print("max bad =", max(len(x[3]) for x in window), "distribution =", dict(Counter(len(x[3]) for x in window)))
print("distinct (i,j) in window:", len(set((x[1],x[2]) for x in window)))
print("(118,39,59) in window:", any(x[0]==118 and x[1]==39 for x in window), " (119,39,59):", any(x[0]==119 and x[1]==39 for x in window))
print("first window examples:", window[:3])

print("\n== EEES78 exceptions: R1 triples and direct discharge ==")
EXC = [(8,3),(9,4),(10,5),(12,5),(21,7),(21,8),(30,7),(33,13),(33,14),(36,13),(36,17),(56,13)]
r1_triples=[]; all_triples=0; all_ok=True
for (n0,i0) in EXC:
    prn = primes_upto(n0)
    for j in range(i0+1, n0//2+1):
        all_triples += 1
        # V_{i0}(n0)
        V=1
        for p in prn:
            if p>=i0:
                e=vp_binom(n0,i0,p)
                if e>0: V*=p**e
        g=gcd(V, comb(n0,j))
        if g<=1: all_ok=False; print("FAIL gcd", n0,i0,j,g)
        if 3*i0 < 2*j < 4*i0:  # wait R1: 3i/2<j<2i  <=> 3i<2j and j<2i
            pass
        if 2*j>3*i0 and j<2*i0: r1_triples.append((n0,i0,j,g))
print("total exception triples (all j):", all_triples, "all gcd>1:", all_ok)
print("R1 exception triples:", r1_triples)

print("\n== Claim 9 arithmetic (H1) ==")
h = lambda u: -u*log(u)-(1-u)*log(1-u)
print("3.965/log(1000)^2 =", 3.965/log(1000)**2)
print("h(1/4) =", h(0.25), "2h(1/4) =", 2*h(0.25))
Psi2 = 2*h(0.25)-2.000162+0.9169
print("Psi(2) =", Psi2)
print("0.5*log(4005)/1001 =", 0.5*log(4005)/1001)
print("net margin =", Psi2 - 0.5*log(4005)/1001)
print("-log(2/3) =", -log(2/3))
print("H2 f(2) = 2h(1/4)-1 =", 2*h(0.25)-1)
# monotonicity of phi(i)=0.5*ln(4i+1)/i for i>=1000: check derivative sign condition ln(4i+1) > 4i/(4i+1)
print("phi decreasing check at i=1000: ln(4001)=", log(4001), "> 4000/4001 =", 4000/4001, "-> derivative negative for all larger i since LHS grows, RHS <1")
# margins at the two failures and smallest positives (float)
for (i,j) in [(4,7),(10,19),(57,113),(12,23)]:
    Qv=Qprod(i,j,primes_upto(j))
    marg=0.5*log(comb(2*j,i))-log(Qv)
    print(f"margin ({i},{j}) = {marg:.4f} nats; ratio Q^2/C = {Qv*Qv/comb(2*j,i):.4f}")

print("\n== Large-i sanity: exact theta differences vs log C (fsum of logs) ==")
LIM=200000
primes=primes_upto(LIM)
logp={p: log(p) for p in primes}
import bisect
pref=[0.0]
for p in primes: pref.append(pref[-1]+logp[p])  # not fsum; use fsum per query below instead
def logP_exact(i,j):
    a=bisect.bisect_right(primes,i); b=bisect.bisect_right(primes,j)
    return fsum(logp[p] for p in primes[a:b])
def logC_sum(i,j):
    # log C(2j,i) = sum_{k=1..i} log((2j-i+k)/k), fsum of exact double logs
    return fsum(log((2*j-i+k)/k) for k in range(1,i+1))
for i in (10000,100000):
    for gam in (1.51,1.75,1.99):
        j=int(gam*i)
        assert 3*i < 2*j < 4*i, (i,j)
        lp=logP_exact(i,j); lc=logC_sum(i,j); lc2=lgamma(2*j+1)-lgamma(i+1)-lgamma(2*j-i+1)
        print(f"i={i} gamma~{j/i:.4f} j={j}: (0.5 logC - logP)/i = {(0.5*lc-lp)/i:.5f}, lgamma cross-check diff = {abs(lc-lc2):.3e}")
print("\nALL V-H main checks done")
