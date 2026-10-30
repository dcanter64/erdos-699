#!/usr/bin/env python3
"""V-F chunks E+G+C: brute-force (LD3) cross-check 5<=j<=60 on [2j,N(3,j)];
independent random check of Lemma F2.2 / Corollary F2.4 dichotomy (own seed);
>=5-only (LD3) survivors for n<=2000 (F1 sec. C list). Stdlib, exact."""
import random
from math import comb
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
def rel(m,drop3=False):
    return [p**a for p,a in factor_trial(m) if p>=5 or (p==3 and a>=2 and not drop3)]
def N_of_3(j):
    target=comb(2*j,6); lo,hi=3,6
    while comb(hi,3)<target: hi*=2
    while lo+1<hi:
        mid=(lo+hi)//2
        if comb(mid,3)<target: lo=mid
        else: hi=mid
    return lo
bsurv=[]
for j in range(5,61):
    Nj=N_of_3(j)
    for n in range(2*j,Nj+1):
        if all(j%q==0 for q in rel(n)) and all(j%q<=1 for q in rel(n-1)) and all(j%q<=2 for q in rel(n-2)):
            bsurv.append((n,j))
print("brute survivors 5<=j<=60:",bsurv, flush=True); assert not bsurv
def vp_fact(x,p):
    s=0
    while x: x//=p; s+=x
    return s
def vp_binom(NN,KK,p): return vp_fact(NN,p)-vp_fact(KK,p)-vp_fact(NN-KK,p)
rng=random.Random(20261029); inst=0; fails=0
for _ in range(4000):
    n=rng.randrange(20,3001); j=rng.randrange(7,n//2+1); c=n-j
    Q,R=divmod(n,j); T=R+2*(Q-1); h=max(0, -((R-3)//Q))
    for p in primes_upto(59):
        if p<3: continue
        a=vp_binom(n,3,p)
        if a>=1 and vp_binom(n,j,p)==0:
            inst+=1; pa=p**a; r=j%pa; s=c%pa
            if not (r+s<3): fails+=1
            E=R+(Q-1)*r-s
            if E!=0:
                if not (pa<=T): fails+=1
            else:
                if not (r<h and (j-r)%pa==0): fails+=1
print("Lemma F2.2 random instances:",inst," failures:",fails, flush=True)
assert fails==0 and inst>0
surv5=[]; survF=[]
for n in range(6,2001):
    r0a,r1a,r2a=rel(n,True),rel(n-1,True),rel(n-2,True)
    r0,r1,r2=rel(n),rel(n-1),rel(n-2)
    for j in range(4,n//2+1):
        if all(j%q==0 for q in r0a) and all(j%q<=1 for q in r1a) and all(j%q<=2 for q in r2a): surv5.append((n,j))
        if all(j%q==0 for q in r0) and all(j%q<=1 for q in r1) and all(j%q<=2 for q in r2): survF.append((n,j))
print(">=5-only survivors n<=2000:",surv5, flush=True)
print("full survivors n<=2000:",survF, flush=True)
assert surv5==[(10,5),(28,14),(82,41),(162,70),(244,122),(730,365)] and not survF
print("CHUNKS E+G+C OK", flush=True)
