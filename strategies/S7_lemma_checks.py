import math
# sieve primes to 2000
N = 2000
is_p = [True]*(N+1); is_p[0]=is_p[1]=False
for p in range(2,N+1):
    if is_p[p]:
        for m in range(p*p,N+1,p): is_p[m]=False
primes=[p for p in range(2,N+1) if is_p[p]]
def vp_binom(n,i,p):
    s=0; a,b,c=n,i,n-i
    while a: a//=p; b//=p; c//=p; s+=a-b-c
    return s
bad1=bad2=0; checked=0
for n in range(4,301):
    for i in range(2,n//2+1):
        for p in primes:
            if p>=n: break
            e=vp_binom(n,i,p)
            if e and p**e>n: bad1+=1; print("ERDOS FAIL",n,i,p,e)
            if i//2<p<i and i>4:
                two = (n//p)-((n-i)//p)==2
                # p^2 dividing a block number (n-i, n]?
                psq = any(m%p*p==0 if False else (m%(p*p)==0) for m in range(n-i+1,n+1))
                pred = two or psq
                if (e>=1)!=pred:
                    bad2+=1
                    if bad2<6: print("CHAR MISMATCH",n,i,p,"e=",e,"two=",two,"psq=",psq)
                checked+=1
print("Erdos lemma p^e<=n violations:",bad1)
print("near-i characterization mismatches:",bad2,"of",checked,"(n,i,p) triples")
