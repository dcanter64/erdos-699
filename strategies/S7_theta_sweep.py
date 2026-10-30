import math, json, sys
from collections import defaultdict

NMAX = 2000

# sieve smallest prime factor
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
    # exponent of p in m!
    s = 0
    while m:
        m //= p; s += m
    return s

def theta_bruteforce(n, i):
    C = math.comb(n, i)
    u = 1; x = C
    for p in primes:
        if p >= i: break
        while x % p == 0:
            x //= p; u *= p
    return math.log(u) / math.log(C), u, C // u

# ---- validation of incremental method on n<=300 ----
def compute_all(nmax):
    """returns dict (n,i)->theta_u via incremental i-sweep per n"""
    out = {}
    for n in range(2, nmax + 1):
        log_u = 0.0  # i=1: no primes <1
        imax = n // 2
        for i in range(1, imax + 1):
            if i >= 2:
                pass
            logC = math.lgamma(n + 1) - math.lgamma(i + 1) - math.lgamma(n - i + 1)
            out[(n, i)] = log_u / logC if logC > 0 else 0.0
            if i == imax: break
            # transition i -> i+1
            A = factorize(n - i); B = factorize(i + 1)
            delta = 0.0
            for p, a in A.items():
                if p < i + 1 and p != i:
                    delta += a * logp[p]
            for p, a in B.items():
                if p < i + 1 and p != i:
                    delta -= a * logp[p]
            if is_prime[i]:
                e = vp_fact(n, i) - vp_fact(i + 1, i) - vp_fact(n - i - 1, i)
                delta += e * logp[i]
            log_u += delta
    return out

val = compute_all(300)
bad = 0
for (n, i), th in val.items():
    if i < 2: continue
    tb, u, v = theta_bruteforce(n, i)
    if abs(tb - th) > 1e-9:
        bad += 1
        if bad < 5: print("MISMATCH", n, i, th, tb)
print("validation n<=300 mismatches:", bad, "pairs:", len(val))

# ---- main sweep n<=2000 ----
data = compute_all(NMAX)
print("total pairs:", len(data))

def sup_over(pred):
    best = (-1, None)
    for (n, i), th in data.items():
        if pred(n, i) and th > best[0]:
            best = (th, (n, i))
    return best

print("\n== sup by n threshold ==")
for nmin in [0, 50, 100, 200, 300, 500, 750, 1000, 1500]:
    print(f"n>={nmin}: ", sup_over(lambda n, i, m=nmin: n >= m))

print("\n== sup by i threshold (n<=2000) ==")
for imin in [3, 5, 10, 20, 50, 100, 200, 300, 500]:
    print(f"i>={imin}: ", sup_over(lambda n, i, m=imin: i >= m))

print("\n== sup by alpha=n/i band, i>=50 and i>=150 ==")
for lo, hi in [(2, 2.5), (2.5, 3), (3, 3.5), (3.5, 4), (4, 5), (5, 6), (6, 8), (8, 12)]:
    for imin in [50, 150]:
        b = sup_over(lambda n, i, lo=lo, hi=hi, m=imin: i >= m and lo <= n / i < hi)
        print(f"alpha in [{lo},{hi}), i>={imin}: theta={b[0]:.4f} at {b[1]}")

print("\n== top 30 pairs overall ==")
top = sorted(data.items(), key=lambda kv: -kv[1])[:30]
for (n, i), th in top:
    print(f"(n,i)=({n},{i}) theta_u={th:.5f} alpha={n/i:.3f}")

print("\n== top 15 pairs with n>=300 ==")
top2 = sorted(((k, v) for k, v in data.items() if k[0] >= 300), key=lambda kv: -kv[1])[:15]
for (n, i), th in top2:
    print(f"(n,i)=({n},{i}) theta_u={th:.5f} alpha={n/i:.3f}")

print("\n== top 15 pairs with i>=100 ==")
top3 = sorted(((k, v) for k, v in data.items() if k[1] >= 100), key=lambda kv: -kv[1])[:15]
for (n, i), th in top3:
    print(f"(n,i)=({n},{i}) theta_u={th:.5f} alpha={n/i:.3f}")

# exceptions check: theta>0.5
exc = sorted([k for k, v in data.items() if v > 0.5])
print("\npairs with theta_u>0.5 (u>v), n<=2000:", exc)

# near misses 0.44..0.5
near = sorted(((k, v) for k, v in data.items() if 0.44 < v <= 0.5), key=lambda kv: -kv[1])
print("pairs with 0.44<theta<=0.5:", len(near))
for (n, i), th in near[:25]:
    print(f"  ({n},{i}) theta={th:.5f} alpha={n/i:.3f}")

# distribution for large i: quantiles in alpha bands
print("\n== theta stats for i in [400,1000], by alpha band (mean, p99 approx via sorted, max) ==")
import statistics
for lo, hi in [(2, 3), (3, 4), (4, 5), (5, 7), (7, 12)]:
    vals = sorted(v for (n, i), v in data.items() if 400 <= i <= 1000 and lo <= n / i < hi)
    if vals:
        q99 = vals[int(0.99 * len(vals))]
        print(f"alpha [{lo},{hi}): count={len(vals)} mean={statistics.mean(vals):.4f} p99={q99:.4f} max={vals[-1]:.4f}")

json.dump({f"{n},{i}": th for (n, i), th in data.items()}, open("/tmp/s7_theta.json", "w"))
print("saved /tmp/s7_theta.json")
