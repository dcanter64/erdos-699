"""P-E1 empirical test: exact theta_u over frontier window for i<=500.
Method: incremental log_u sweep (as in S7, independently re-derived),
validated against brute-force Legendre factorisation; window endpoints
N(i,2i) computed exactly with math.comb binary search; top candidates
re-verified with exact integer comparisons u^100 vs C(n,i)^k.
Python stdlib only.
"""
import math, random, sys, time

t0 = time.time()
NMAX = 3400  # > max N(i,2i) for i<=500 (~6.4*500=3200)

# spf sieve
spf = list(range(NMAX + 1))
primes = []
is_prime = [True] * (NMAX + 1)
is_prime[0] = is_prime[1] = False
for p in range(2, NMAX + 1):
    if spf[p] == p:
        primes.append(p)
        if p * p <= NMAX:
            for m in range(p * p, NMAX + 1, p):
                if spf[m] == m:
                    spf[m] = p
    else:
        is_prime[p] = False
is_prime[2] = True
logp = {p: math.log(p) for p in primes}

def factorize(x):
    d = {}
    while x > 1:
        p = spf[x]; a = 0
        while x % p == 0:
            x //= p; a += 1
        d[p] = a
    return d

def vp_fact(m, p):
    s = 0
    while m:
        m //= p; s += m
    return s

def logu_bruteforce(n, i):
    """log u via Legendre exponents, primes p<i."""
    s = 0.0
    for p in primes:
        if p >= i: break
        e = vp_fact(n, p) - vp_fact(i, p) - vp_fact(n - i, p)
        if e: s += e * logp[p]
    return s

def logC(n, i):
    return math.lgamma(n + 1) - math.lgamma(i + 1) - math.lgamma(n - i + 1)

def compute_all(nmax):
    out = {}
    for n in range(2, nmax + 1):
        log_u = 0.0
        imax = n // 2
        for i in range(1, imax + 1):
            logC_ = math.lgamma(n + 1) - math.lgamma(i + 1) - math.lgamma(n - i + 1)
            out[(n, i)] = log_u / logC_ if logC_ > 0 else 0.0
            if i == imax: break
            A = factorize(n - i); B = factorize(i + 1)
            delta = 0.0
            for p, a in A.items():
                if p < i + 1 and p != i: delta += a * logp[p]
            for p, a in B.items():
                if p < i + 1 and p != i: delta -= a * logp[p]
            if is_prime[i]:
                e = vp_fact(n, i) - vp_fact(i + 1, i) - vp_fact(n - i - 1, i)
                delta += e * logp[i]
            log_u += delta
    return out

# validation: incremental vs brute force, all n<=300
val = compute_all(300)
bad = 0
for (n, i), th in val.items():
    if i < 2: continue
    tb = logu_bruteforce(n, i) / logC(n, i)
    if abs(tb - th) > 1e-9: bad += 1
print(f"validation n<=300: mismatches={bad} pairs={len(val)}")

# random brute-force spot checks up to NMAX
data = compute_all(NMAX)
random.seed(20261029)
bad = 0
for _ in range(300):
    n = random.randint(4, NMAX); i = random.randint(2, n // 2)
    tb = logu_bruteforce(n, i) / logC(n, i)
    if abs(tb - data[(n, i)]) > 1e-9: bad += 1
print(f"random spot checks n<={NMAX}: mismatches={bad} (300 seeded)")

# exact N(i,2i): largest n with C(n,i) < C(4i,2i)
def Nval(i, j):
    target = math.comb(2 * j, 2 * (j - i))
    lo, hi = 2 * j, 4 * j * j  # C(hi,i)>=target guaranteed well before hi for i>=1 in our range; verify
    while math.comb(hi, i) < target: hi *= 2
    while lo < hi:
        mid = (lo + hi + 1) // 2
        if math.comb(mid, i) < target: lo = mid
        else: hi = mid - 1
    return lo

Ns = {}
for i in range(1, 501):
    Ns[i] = Nval(i, 2 * i)
print("N(i,2i)/i at i=10,50,100,250,500:", [(i, Ns[i], round(Ns[i]/i, 4)) for i in (10, 50, 100, 250, 500)])
print("max N(i,2i) for i<=500:", max(Ns.values()))

# frontier window sup: i<=500, 4i<=n<=N(i,2i)
def window_sup(imin):
    best = (-1, None); cnt = 0
    for i in range(max(imin, 1), 501):
        for n in range(4 * i, Ns[i] + 1):
            cnt += 1
            th = data[(n, i)]
            if th > best[0]: best = (th, (n, i))
    return best, cnt

for imin in (1, 10, 30, 50, 100, 200, 300):
    (th, ni), cnt = window_sup(imin)
    print(f"window sup i>={imin}: theta={th:.5f} at (n,i)={ni} alpha={ni[0]/ni[1]:.4f} pairs={cnt}")

# all pairs in window with theta>0.33, for reporting
over = sorted(((v, k) for k, v in data.items()
               if k[1] <= 500 and 4 * k[1] <= k[0] <= Ns[k[1]] and v > 0.33),
              reverse=True)
print("window pairs with theta>0.33:", len(over))
for v, (n, i) in over[:15]:
    print(f"  (n,i)=({n},{i}) theta={v:.5f} alpha={n/i:.4f}")
over36 = [(v, k) for v, k in over if v > 0.36]
print("window pairs with theta>0.36:", len(over36), over36[:10])

# exact integer verification of the top candidate and of the 0.36 threshold
def exact_u(n, i):
    u = 1
    for p in primes:
        if p >= i: break
        e = vp_fact(n, p) - vp_fact(i, p) - vp_fact(n - i, p)
        u *= p ** e
    return u

(th, (n, i)), _ = window_sup(1)
u = exact_u(n, i); C = math.comb(n, i)
# theta>0.36 iff u^100 > C^36 ; theta<0.37 iff u^100 < C^37, etc.
print(f"top candidate (n,i)=({n},{i}) theta(float)={th:.6f}")
for k in (33, 34, 35, 36, 37):
    print(f"  u^100 > C^{k}: {u**100 > C**k}   (theta>{k/100})")
# exact check: NO window pair exceeds 0.36, via float shortlist + integer check of all float>0.355
short = [(v, k) for k, v in data.items() if k[1] <= 500 and 4 * k[1] <= k[0] <= Ns[k[1]] and v > 0.355]
print("pairs with float theta>0.355 (integer-checked):", len(short))
viol = 0
for v, (n, i) in short:
    uu = exact_u(n, i); CC = math.comb(n, i)
    if uu ** 100 > CC ** 36: viol += 1; print("  EXACT VIOLATION", n, i, v)
print("exact violations of theta<=0.36 among shortlist:", viol)
print(f"elapsed {time.time()-t0:.1f}s")
