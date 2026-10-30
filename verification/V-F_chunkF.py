#!/usr/bin/env python3
import time
from array import array
T0=time.time()
def note(m): print(f"[{time.time()-T0:7.1f}s] {m}", flush=True)
def primes_upto(n):
    s=bytearray(b"\x01")*(n+1); s[0:2]=b"\x00\x00"
    for i in range(2,int(n**0.5)+1):
        if s[i]: s[i*i:n+1:i]=b"\x00"*(((n-i*i)//i)+1)
    return [i for i,v in enumerate(s) if v]
def v_p_int(x,p):
    a=0
    while x%p==0: x//=p; a+=1
    return a
L=10**6
note("R sieve")
Rarr=[1]*(L+1)
for p in primes_upto(L):
    if p==2: continue
    q=p
    while q<=L:
        if p>=5 or q>=9:
            step=q*p
            for m in range(q,L+1,q):
                if m%step!=0: Rarr[m]*=q
        if q>L//p: break
        q*=p
note(f"R sieve done; sanity R(162)={Rarr[162]} (expect 81*2? no: 162=2*3^4, relevant 3^4=81) R(730)={Rarr[730]} (730=2*5*73, expect 365)")
assert Rarr[162]==81 and Rarr[730]==365
note("SPF build")
spf=array("i",range(L+1))
for p in reversed(primes_upto(1000)):
    spf[p::p]=array("i",[p])*((L-p)//p+1)
def relU_spf(m):
    rel=[]; u=1; x=m
    while x>1:
        p=spf[x]; a=0; q=1
        while x%p==0: x//=p; a+=1; q*=p
        if p>=5: rel.append(q); u*=q
        elif p==3 and a>=2: rel.append(q)
    return rel,u
note("main loop")
survF=[]; tot4=0; even7=0; even7_1e5=0; n_with=0
odd_cnt5=0; odd_cnt7=0; odd_surv=[]; n2pass=0; n2_min=None
for n in range(6,L+1):
    Rn=Rarr[n]
    pinned=(n%2==1 and v_p_int(n,3)==1)
    jpin=n//3 if pinned else None
    if pinned:
        if jpin>=5: odd_cnt5+=1
        if jpin>=7: odd_cnt7+=1
    if Rn>n//2 and not pinned: continue
    rel1,U1=relU_spf(n-1); rel2,U2=relU_spf(n-2)
    if pinned and jpin>=5:
        if U1*U2*6<=(jpin-1)*(jpin-2):
            n2pass+=1
            if n2_min is None: n2_min=(n,jpin,U1,U2)
        if all(jpin%q<=1 for q in rel1) and all(jpin%q<=2 for q in rel2):
            odd_surv.append((n,jpin))
    if Rn>n//2: continue
    n_with+=1
    j=Rn if Rn>=4 else 4
    while j<=n//2:
        if j%Rn==0:
            tot4+=1
            if n%2==0 and j>=7:
                even7+=1
                if n<=10**5: even7_1e5+=1
            if all(j%q<=1 for q in rel1) and all(j%q<=2 for q in rel2):
                survF.append((n,j))
        j+=Rn if Rn>=4 else 1
note(f"n_with={n_with} total pairs j>=4: {tot4}")
note(f"even pairs j>=7: {even7}; even pairs j>=7 n<=1e5: {even7_1e5}")
print("full survivors:",survF, flush=True); assert not survF
note(f"pinned odd: cnt j>=5: {odd_cnt5}; cnt j>=7: {odd_cnt7}; (N2) passes: {n2pass}; smallest N2 pass: {n2_min}; LD3 survivors: {odd_surv}")
assert not odd_surv
note("CHUNK F OK")
