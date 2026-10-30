#!/usr/bin/env python3
"""V-L independent checks, Cluster L Cycle 3. Stdlib only, exact arithmetic.
Implementations independent of both provers (own SPF sieve, own digit code).
Sections: 2 low-digit equiv stress; 3 support/Kummer boundaries;
4 >=5-only recount to 1e6; 5 L2 instance census n<=2000;
6 L2 p=5 family; 7 rows in both parametrisations + aggregates; misc tables.
"""
import time, math
from math import gcd, comb
T0=time.time()
def note(m): print(f"[{time.time()-T0:6.1f}s] {m}", flush=True)

# ---------- helpers ----------
def spf_upto(N):
    spf=list(range(N+1))
    i=2
    while i*i<=N:
        if spf[i]==i:
            st=i*i
            for k in range(st,N+1,i):
                if spf[k]==k: spf[k]=i
        i+=1
    return spf
def fac(m,spf):
    f={}
    while m>1:
        p=spf[m]; a=0
        while m%p==0: m//=p; a+=1
        f[p]=a
    return f
def primes_upto(N):
    s=bytearray(b"\x01")*(N+1); s[0:2]=b"\x00\x00"
    for i in range(2,int(N**.5)+1):
        if s[i]: s[i*i::i]=b"\x00"*(((N-i*i)//i)+1)
    return [i for i,v in enumerate(s) if v]
def digits_le(j,n,p):
    while j or n:
        if j%p>n%p: return False
        j//=p; n//=p
    return True
def V3(n):
    c=n*(n-1)*(n-2)//6
    while c%2==0: c//=2
    return c
def Lam3(T):
    out=1
    for q in primes_upto(T):
        if q<3: continue
        pw=q
        while pw*q<=T: pw*=q
        out*=pw
    return out

# ---------- Task 2: low-digit equivalence, abstract + n,j sample ----------
note("2. low-digit equivalence")
# abstract exhaustive: for every prime p<=50, a<=4 with q=p^a<=2500, r in 0..2,
# every t<q: digitwise(t vs (r,0,...)) iff t<=r
cnt=0; bad=0
for p in primes_upto(50):
    if p<3: continue  # domain of (LD3): p>=3, hence r<=2<p (load-bearing)
    for a in range(1,5):
        q=p**a
        if q>2500: continue
        for r in (0,1,2):
            for t in range(q):
                cnt+=1
                x=t; ok=True
                for e in range(a):
                    nd = r if e==0 else 0
                    if x%p>nd: ok=False; break
                    x//=p
                if ok != (t<=r): bad+=1
print(f"  abstract exhaustive q<=2500: {cnt} (p,a,r,t) cases, failures={bad}")
assert bad==0
# strided for larger q up to 50^4
cnt=0; bad=0
for p in primes_upto(50):
    if p<3: continue
    for a in range(1,5):
        q=p**a
        if q<=2500: continue
        step=max(1,q//997)
        for r in (0,1,2):
            t=0
            while t<q:
                cnt+=1
                x=t; ok=True
                for e in range(a):
                    nd=r if e==0 else 0
                    if x%p>nd: ok=False; break
                    x//=p
                if ok != (t<=r): bad+=1
                t+=step
            # boundary t=r, r+1, p-1, p, p+1, q-1
            for t in {r,r+1,p-1,p,p+1,q-1}:
                if 0<=t<q:
                    cnt+=1; x=t; ok=True
                    for e in range(a):
                        nd=r if e==0 else 0
                        if x%p>nd: ok=False; break
                        x//=p
                    if ok != (t<=r): bad+=1
print(f"  strided larger q: {cnt} cases, failures={bad}")
assert bad==0
# boundary outside the domain: p=2, r=2 (r<p fails) DOES separate the forms:
# t=2 <= r but digitwise fails at digit 1 for every a>=2. Confirms r<p is load-bearing.
sep=[(a) for a in range(2,5) if not (lambda t: all(((t//2**e)%2) <= (2 if e==0 else 0) for e in range(a)))(2)]
print(f"  out-of-domain boundary p=2,r=2: t=2 separates the forms for a in {sep} (expected [2,3,4])")
assert sep==[2,3,4]
# n,j sample with exact divisibility condition q || (n-r)
spf100k=spf_upto(100000)
cnt=0; bad=0
for n in range(6,3001):
    rel=[]
    for r in range(3):
        for p,a in fac(n-r,spf100k).items():
            if p>=5 or (p==3 and a>=2): rel.append((p,a,r,p**a))
    for j in range(4,n//2+1):
        for (p,a,r,q) in rel:
            cnt+=1
            jj=j; nn=n; ok=True
            for _ in range(a):
                if jj%p>nn%p: ok=False; break
                jj//=p; nn//=p
            if ok != (j%q<=r): bad+=1
print(f"  (n,j,q) sample n<=3000: {cnt} instances, failures={bad}")
assert bad==0

# ---------- Task 3: support boundaries ----------
note("3. support / Kummer boundaries")
bad=0
for n in range(4,2001):
    # v_p(C(n,3)) for p>=5 equals v_p of unique top; p=3: a-1
    Cn3=comb(n,3)
    for r in range(3):
        for p,a in fac(n-r,spf100k).items():
            if p>=5:
                # p divides Cn3 iff p divides a top (this r), exponent a
                x=Cn3; e=0
                while x%p==0: x//=p; e+=1
                if e!=a: bad+=1
    # p=3
    a3=None
    for r in range(3):
        if (n-r)%3==0:
            a3=0; m=n-r
            while m%3==0: m//=3; a3+=1
    e3=0; x=Cn3
    while x%3==0: x//=3; e3+=1
    if e3!=a3-1: bad+=1
    if (Cn3%3==0) != (a3>=2): bad+=1  # 3 | C(n,3) iff v3(top)>=2
print(f"  support exponent checks n<=2000, failures={bad}")
assert bad==0
# Kummer direction: p not | C(n,j) iff digitwise <=, spot exhaustive n<=250
cnt=0; bad=0
for n in range(4,251):
    for j in range(4,n//2+1):
        Cnj=comb(n,j)
        ps=set()
        for r in range(3): ps|= {p for p in fac(n-r,spf100k) if p>=3}
        for p in ps:
            cnt+=1
            if digits_le(j,n,p) != (Cnj%p!=0): bad+=1
print(f"  Kummer spot n<=250: {cnt} instances, failures={bad}")
assert bad==0

# ---------- Task 4: >=5-only recount to 1e6 ----------
note("4. >=5-only (LD3) recount to 10^6 (R5-candidate method)")
L=10**6
spf=spf_upto(L+1)
def rel5(m):
    qs=[]; 
    for p,a in fac(m,spf).items():
        if p>=5: qs.append(p**a)
    return qs
surv=[]; pairs=0
for n in range(6,L+1):
    Rn=1
    for p,a in fac(n,spf).items():
        if p>=5: Rn*=p**a
    if Rn>n//2: continue
    r1=rel5(n-1); r2=rel5(n-2)
    j=Rn if Rn>=4 else 4
    while j<=n//2:
        pairs+=1
        if all(j%q<=1 for q in r1) and all(j%q<=2 for q in r2):
            surv.append((n,j))
        j+=Rn
print(f"  pairs tested={pairs}; solutions={len(surv)}: {surv}")
EXP12=[(10,5),(28,14),(82,41),(162,70),(244,122),(730,365),(2188,1094),(6562,3281),(19684,9842),(59050,29525),(177148,88574),(531442,265721)]
assert surv==EXP12, surv
# classification: p3 low fail, p3 high pass, >=5 full failures
def three_top(n):
    for r in range(3):
        if (n-r)%3==0:
            m=n-r; a=0
            while m%3==0: m//=3; a+=1
            return r,a
def support(n):
    s=set()
    for r in range(3):
        for p,a in fac(n-r,spf).items():
            if p>=5: s.add(p)
            elif p==3 and a>=2: s.add(3)
    return s
killed=0; detail={}
for (n,j) in surv:
    r3,a3=three_top(n); q3=3**a3
    lowfail = j%q3>r3
    highpass = digits_le(j//q3,(n-r3)//q3,3)
    fails5=sorted(p for p in support(n) if p>=5 and not digits_le(j,n,p))
    detail[(n,j)]=(lowfail,highpass,fails5)
    if fails5: killed+=1
    print(f"    ({n},{j}): 3-low fails={lowfail} (r3={r3},a3={a3}), 3-high passes={highpass}, >=5 full fails={fails5}")
    assert lowfail and highpass
print(f"  >=5-higher-killed count = {killed} of 12")
assert killed==8
assert detail[(82,41)][2]==[5] and detail[(162,70)][2]==[5,7] and detail[(730,365)][2]==[5]
assert detail[(6562,3281)][2]==[17,41] and detail[(19684,9842)][2]==[7]
assert detail[(59050,29525)][2]==[5,61] and detail[(177148,88574)][2]==[67]
assert detail[(531442,265721)][2]==[5,7,13,41,73]
assert all(detail[k][2]==[] for k in [(10,5),(28,14),(244,122),(2188,1094)])

# ---------- Task 5: L2 instance census n<=2000 ----------
note("5. P-L2 instance census n<=2000")
spf2=spf_upto(2001)
tot=lf=lptp=lptf=0
for n in range(7,2001):
    rel=[]
    for rho in range(3):
        for p,a in fac(n-rho,spf2).items():
            if p>=5 or (p==3 and a>=2): rel.append((rho,p,a,p**a))
    if not rel: continue
    info=[(rho,p,a,q,(n-rho)//q) for (rho,p,a,q) in rel]
    for j in range(4,n//2+1):
        for (rho,p,a,q,K) in info:
            tot+=1
            if j%q>rho: lf+=1
            else:
                if digits_le(j//q,K,p): lptp+=1
                else: lptf+=1
print(f"  total={tot} low_fail={lf} lowpass_tailpass={lptp} lowpass_tailfail={lptf} lowpass_total={lptp+lptf}")
print(f"  tail decisive fraction of low-passing = {lptf/(lptp+lptf)*100:.2f}%")

# ---------- Task 6: L2 p=5 family ----------
note("6. P-L2 Prop L2.9 family w=0..200 (and spot w up to 5000)")
for w in list(range(0,201))+[500,1000,5000]:
    n=50*w+30; j=25*w+15
    m=n; a5=0
    while m%5==0: m//=5; a5+=1
    assert a5==1 and j%5==0 and j==n//2
    assert (j//5)%5==3 and (n//5)%5==1
print("  family verified w=0..200 + spot 500,1000,5000: v5=1, low passes, digit1 3>1 fails")
print(f"  note: w=0 gives (n,j)=({50*0+30},{25*0+15}); w=1 gives ({80},{40}); 79 | 79 = n-1 at w=1")

# ---------- Task 7a: L1 rows ----------
note("7a. P-L1 ten h=0 rows, odd-part-of-n parametrisation")
def divisors(m):
    ds=[1]
    # factorise by trial division
    x=m; f={}
    d=2
    while d*d<=x:
        while x%d==0: f[d]=f.get(d,0)+1; x//=d
        d+=1 if d==2 else 2
    if x>1: f[x]=f.get(x,0)+1
    for p,a in f.items(): ds=[dd*p**e for dd in ds for e in range(a+1)]
    return sorted(ds)
def ld3_ok(n,j):
    for r in range(3):
        for p,a in fac(n-r,spf100k).items():
            if p>=5 or (p==3 and a>=2):
                if j%(p**a)>r: return False
    return True
def ld3plus_ok(n,j):
    return all(digits_le(j,n,p) for p in support(n))
L1ROWS=[(2,4),(2,3),(2,5),(3,3),(2,6),(3,4),(2,16),(2,17),(2,18),(3,16)]
tot_v=0
for (Q,R) in L1ROWS:
    T=R+2*(Q-1); Lam=Lam3(T)
    odds=[d for d in divisors(3*Lam) if d%2==1]
    cand=set()
    for o in odds:
        x=o
        while x<=10**8:
            cand.add(x)
            if x>10**8//2: break
            x*=2
    inrow=[]
    for n in sorted(cand):
        if n<=R or (n-R)%Q: continue
        j=(n-R)//Q
        if j>3 and 2*j<=n: inrow.append((n,j))
    vpass=[(n,j) for (n,j) in inrow if V3(n)!=0 and Lam%V3(n)==0]
    lpass=[(n,j) for (n,j) in vpass if ld3_ok(n,j)]
    ppass=[(n,j) for (n,j) in lpass if ld3plus_ok(n,j)]
    tot_v+=len(vpass)
    print(f"  L1 row ({Q},{R}) T={T} Lam={Lam} oddparts={len(odds)} cand={len(cand)} inrow={len(inrow)} Vpass={len(vpass)} {vpass} LD3={len(lpass)} LD3+={len(ppass)}")
print(f"  L1 total V-passers across 10 rows = {tot_v}")

# ---------- Task 7b: L2 rows ----------
note("7b. P-L2 parametrisation (n-1 in F(Lambda))")
def Fset(Lam):
    v3=0; t=Lam
    while t%3==0: t//=3; v3+=1
    divs=divisors(t)
    return {(3**b)*u for b in range(v3+2) for u in divs}
def row_pipeline_L2(Q,R):
    T=R+2*(Q-1); Lam=Lam3(T); F=Fset(Lam)
    s1=[]
    for m in sorted(F):
        n=m+1
        if n%2==1 or (n-R)%Q: continue
        j=(n-R)//Q
        if j<=3: continue
        s1.append((n,j))
    s2=[(n,j) for (n,j) in s1 if V3(n)<=Lam and Lam%V3(n)==0]
    surv=[(n,j) for (n,j) in s2 if ld3_ok(n,j)]
    psurv=[(n,j) for (n,j) in surv if ld3plus_ok(n,j)]
    return T,Lam,s1,s2,surv,psurv
for QR in [(2,4),(2,6),(3,4)]:
    T,Lam,s1,s2,surv,psurv=row_pipeline_L2(*QR)
    print(f"  L2 row {QR} T={T} Lam={Lam} stage1={len(s1)} {s1} stage2={s2} LD3surv={surv} LD3+surv={psurv}")
tot1=tot2=0; rows=0; maxn=0; maxj=0
for Q in range(2,9):
    for R in range(3,40):
        if R+2*(Q-1)>20: continue
        T,Lam,s1,s2,surv,psurv=row_pipeline_L2(Q,R)
        rows+=1; tot1+=len(s1); tot2+=len(s2)
        assert surv==[] and psurv==[]
        if s2: maxn=max(maxn,max(n for n,j in s2)); maxj=max(maxj,max(j for n,j in s2))
print(f"  L2 aggregate: rows={rows} stage1={tot1} stage2={tot2} max stage2 n={maxn} j={maxj}, LD3/LD3+ survivors 0")

# ---------- misc: L1 strictness example, L2.7 gcd table, (4,2) ----------
note("misc spot checks")
assert 15%5==0 and not digits_le(15,30,5) and digits_le(5,30,5)
print("  L1 (30,15,5): low passes, full fails; j=5 passes both: OK")
for (n,j),g in [((10,5),3),((28,14),9),((82,41),135),((244,122),81),((730,365),1215),((162,70),945)]:
    gg=gcd(V3(n),comb(n,j)); assert gg==g,(n,j,gg)
print("  L2.7 gcd table (3,9,135,81,1215,945): OK")
for (n,j),g in [((22,5),77),((46,11),69),((106,26),371)]:
    assert gcd(V3(n),comb(n,j))==g and not ld3_ok(n,j)
print("  (4,2) candidates gcds 77,69,371, all LD3-fail: OK")
# L1 Lemma L3.1 spot: even counterexample-shaped check is a proof audit; numeric form:
# for all even n<=5000 and T with V3|Lam3(T): n-1 | 3*Lam3(T) ?
viol=0
for T in (5,6,7,8,18,19,20):
    Lam=Lam3(T)
    for n in range(8,5001,2):
        v=V3(n)
        if v and Lam%v==0 and (3*Lam)%(n-1)!=0: viol+=1
print(f"  L3.1 numeric form violations (even n<=5000, 7 T values): {viol}")
assert viol==0
note("8. P-L2 Method A member set + the filed script's V3 hang")
S15=[1,3,9,5,15,45]; candA=set()
for o in S15:
    m=o
    while m<=10**8:
        candA.add(m)
        if m>10**8//2: break
        m*=2
memA=[n for n in sorted(candA) if n>=3 and V3(n) and 15%V3(n)==0]
print(f"  Method A: {len(candA)} candidates; V3|15 members (n>=3): {memA} (file states {{6,10}})")
assert memA==[3,4,5,6,10]
assert all(not (n==2*((n-4)//2)+4 and (n-4)//2>3) for n in memA)  # none in (2,4) row with j>3
# the filed P-L2 V3 loops forever at n=2: C(2,3)=0 and 0//2=0 keeps c%2==0.
c=2*1*0//6
assert c==0
for _ in range(10**6):  # simulate the filed loop body: it never exits
    assert c%2==0; c//=2; assert c==0
print("  filed P-L2 V3(2): C(2,3)=0 and the halving loop never changes c=0 -> non-termination confirmed (simulated 10^6 iterations)")

note("ALL V-L CHECKS DONE")
print(f"total runtime {time.time()-T0:.1f}s")
