#!/usr/bin/env python3
import time
from math import comb
T0=time.time()
def note(m): print(f"[{time.time()-T0:7.1f}s] {m}", flush=True)
def primes_upto(n):
    s=bytearray(b"\x01")*(n+1); s[0:2]=b"\x00\x00"
    for i in range(2,int(n**0.5)+1):
        if s[i]: s[i*i:n+1:i]=b"\x00"*(((n-i*i)//i)+1)
    return [i for i,v in enumerate(s) if v]
PR=primes_upto(4505)
def factor_trial(m):
    out=[]; x=m
    for p in PR:
        if p*p>x: break
        if x%p==0:
            a=0
            while x%p==0: x//=p; a+=1
            out.append((p,a))
    if x>1: out.append((x,1))
    return out
def rel(m): return [p**a for p,a in factor_trial(m) if p>=5 or (p==3 and a>=2)]
def R_of(m):
    r=1
    for p,a in factor_trial(m):
        if p>=5 or (p==3 and a>=2): r*=p**a
    return r
def v_p_int(x,p):
    a=0
    while x%p==0: x//=p; a+=1
    return a
def N_of_3(j):
    target=comb(2*j,6); lo,hi=3,6
    while comb(hi,3)<target: hi*=2
    while lo+1<hi:
        mid=(lo+hi)//2
        if comb(mid,3)<target: lo=mid
        else: hi=mid
    return lo
note("building Nj")
Nj={j:N_of_3(j) for j in range(5,5001)}
NMAX=Nj[5000]; print("NMAX",NMAX, flush=True)
cand=set()
for dd in range(1,5001):
    if dd%2==0: continue
    v3=v_p_int(dd,3)
    if v3==1: continue
    t=1
    while dd*t<=NMAX:
        cand.add(dd*t)
        if v3==0: cand.add(dd*3*t)
        t*=2
note(f"candidates: {len(cand)}")
surv=[]; pairs2000=0; pairs5000=0
for n in sorted(cand):
    Rn=R_of(n); assert Rn<=5000, (n,Rn)
    rel1=rel(n-1); rel2=rel(n-2)
    j=Rn
    while j<=5000:
        if j>=5 and 2*j<=n<=Nj[j]:
            pairs5000+=1
            if j<=2000: pairs2000+=1
            if all(j%q<=1 for q in rel1) and all(j%q<=2 for q in rel2):
                surv.append((n,j))
        j+=Rn
note(f"pairs tested j<=2000: {pairs2000}; j<=5000: {pairs5000}")
print("survivors:",surv, flush=True)
assert not surv
note("CHUNK D OK")
