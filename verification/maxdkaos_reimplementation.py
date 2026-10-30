#!/usr/bin/env python3
"""
HK-A Cycle 2: independent reimplementation of the MaxDKaos cut-off for
Erdos #699 (forum comment of 25 Jul 2026, as filed in
EXTERNAL_CLAIMS_2026-10-29.md).

Question: do his tabulated settled-j values
    i=3 -> 5, i=5 -> 12, i=10 -> 30, i=20 -> 138, i=100 -> 25063,
    i=200 -> 713421, i=394 -> 360654145
reproduce under precisely stated candidate cut-offs built from
  (i)  the Kummer bound  u <= U(n,i) = n^{pi(i-1)}            (S1, crude)
  (ii) its sharp form     u <= U^sharp(n,i) = prod_{p<i} q_p(n),
       q_p(n) = p^{floor(log_p n)}                            (S1, sharp)
  (iii) the prime-gap forcing: a counterexample at (n,i,j) forces
       (n-i, n] prime-free                                     (S3)

Candidates (exact definitions are also in the companion .md):
  A (crude Kummer + first-gap cut-off):
       N_K(i,j) = max{ n >= 2j : C(n,i) <= n^{pi(i-1)} * C(j, j-i) }
                  (convention: 2j-1 if the set is empty, i.e. if the
                  inequality already fails at n = 2j; the underlying
                  bad set is the interval [2j, N_K] by S1 Lemma 4)
       settled_A(i,j)  iff  N_K(i,j) <= G(i).
  B (sharp Kummer + first-gap cut-off):
       Bad^sharp(i,j) = { n >= 2j : C(n,i) <= U^sharp(n,i) * C(j, j-i) }
       settled_B(i,j)  iff  no n in Bad^sharp(i,j) has n > G(i).
       (Bad^sharp need not be an interval - S1 Lemma 5 - so B is tested
        via segment minima, see settled_B below, and the test is
        validated against brute-force scans.)
  C (sharp Kummer + exact prime-free windows):
       settled_C(i,j)  iff  no n in Bad^sharp(i,j) is prime-free in the
       S3 sense, i.e. (n-i, n] contains no prime.  Prime-free n are
       exactly the integers in the windows [p+i, p+g-1] for prime gaps
       (p, p+g) with g > i.

G(i) := the largest M such that every interval (n-i, n] with n <= M
contains a prime.  If (p, p+g) is the FIRST prime gap with g > i, then
the first prime-free n is p+i, so G(i) = p+i-1.

All binomial comparisons are exact integer arithmetic (math.comb).
No log-space comparisons are used anywhere in this script.
Python stdlib only.  Runtime a few minutes (dominated by a 50M sieve).

Author: HK-A (housekeeping computation agent), Cycle 2, 2026-10-29.
"""

import bisect
import math
import time
from math import comb

T0 = time.time()


def log(*a):
    print(*a, flush=True)


# ---------------------------------------------------------------- sieve
def primes_upto(n):
    """Simple Eratosthenes sieve (bytearray), returns list of primes <= n."""
    s = bytearray(b"\x01") * (n + 1)
    s[0:2] = b"\x00\x00"
    for p in range(2, int(n ** 0.5) + 1):
        if s[p]:
            s[p * p :: p] = b"\x00" * len(s[p * p :: p])
    return [p for p, v in enumerate(s) if v]


SMALL_PRIMES = primes_upto(100000)          # primes < i (i <= 394) and pi()
PRIMES_500K = primes_upto(500000)           # for G(i), i <= 100


def pi_of(x):
    return bisect.bisect_right(SMALL_PRIMES, x)


# ------------------------------------------------------- G(i) from gaps
def first_gap_over(i, primes):
    """First (p, g) with p, p+g consecutive primes in `primes` and g > i.
    Exhaustive over the supplied prime list, in increasing order."""
    for a, b in zip(primes, primes[1:]):
        if b - a > i:
            return a, b - a
    return None


def G_of(i, primes):
    p, g = first_gap_over(i, primes)
    return p + i - 1, p, g


log("=" * 72)
log("1.  G(i): anchors and small/medium i from own sieve (limit 500,000)")
G = {}
for i in (3, 5, 10, 20, 100):
    gval, p, gap = G_of(i, PRIMES_500K)
    G[i] = gval
    log(f"    i={i:>3}: first gap > i is {gap} at p={p} -> G(i) = {p}+{i}-1 = {gval}")
assert G[3] == 9, "anchor G(3)=9 failed"
assert G[5] == 27, "anchor G(5)=27 failed"
log("    ANCHORS REPRODUCED: G(3)=9, G(5)=27.")

# A slightly different definition that ALSO fits both anchors, and why it
# is wrong in general:  G_alt(i) = (next prime after the first gap > i) - 2
# = p+g-2.  For i=3 (g=4=i+1) and i=5 (g=6=i+1) it coincides with G; for
# i=10 it gives 125, but n=124 already has (124-10,124]=(114,124]
# prime-free (next prime after 113 is 127), so the true G(10)=122.
log("    Alternative definition p_next-2 (fits both anchors, wrong in general):")
for i in (3, 5, 10, 20, 100):
    p, gap = first_gap_over(i, PRIMES_500K)
    log(f"      i={i:>3}: p_next-2 = {p + gap - 2}   (true G(i) = {G[i]})")

# ------------------------------------------------------------ Kummer NK
def Cj(i, j):
    return comb(j, j - i)


def NK(i, j):
    """Crude Kummer top: max n >= 2j with C(n,i) <= n^{pi(i-1)} C(j,j-i),
    or 2j-1 if there is no such n.  Exact; binary search is legitimate
    because F_i(n) = C(n,i)/n^{pi(i-1)} is strictly increasing (S1 L.4)
    and C(j,j-i) is increasing in j (so NK is nondecreasing in j)."""
    tgt = Cj(i, j)
    pi = pi_of(i - 1)

    def bad(n):
        return comb(n, i) <= pow(n, pi) * tgt

    if not bad(2 * j):
        return 2 * j - 1
    lo, hi = 2 * j, 4 * j + 10
    while bad(hi):
        hi *= 2
    while hi - lo > 1:
        m = (lo + hi) // 2
        if bad(m):
            lo = m
        else:
            hi = m
    return lo


def settled_A(i, j, Gval):
    return NK(i, j) <= Gval


# ------------------------------------------------------------- U^sharp
def qpow(p, n):
    """p^{floor(log_p n)}: largest power of p that is <= n."""
    v = 1
    while v * p <= n:
        v *= p
    return v


def Usharp(n, i):
    u = 1
    for p in SMALL_PRIMES:
        if p >= i:
            break
        u *= qpow(p, n)
    return u


def prime_powers_upto(i, hi):
    """All p^e <= hi with p < i prime, e >= 1 (the jump points of U^sharp)."""
    s = set()
    for p in SMALL_PRIMES:
        if p >= i:
            break
        v = p
        while v <= hi:
            s.add(v)
            if v > hi // p:
                break
            v *= p
    return sorted(s)


def settled_B(i, j, Gval):
    """Exact test of candidate B via segment minima.

    U^sharp(., i) is a step function, constant between consecutive prime
    powers p^e (p < i); C(n, i) is strictly increasing in n.  Hence on
    every segment where U^sharp is constant, C(n,i)/U^sharp(n,i) is
    strictly increasing, and the minimum over the part of the segment
    lying in the domain {n >= 2j, n > G} is attained at the first point
    of that part.  So 'no bad n > G' holds iff the inequality FAILS at
    n = max(2j, G+1) and at every prime power in (max(2j,G+1), N_K].
    Bad^sharp is contained in [2j, N_K] (S1 Lemma 5(a)).  Validated
    against brute force below."""
    tgt = Cj(i, j)
    upper = NK(i, j)
    start = max(2 * j, Gval + 1)
    if upper < start:
        return True
    cands = [start] + [pp for pp in prime_powers_upto(i, upper) if start < pp <= upper]
    for c in cands:
        if comb(c, i) <= Usharp(c, i) * tgt:
            return False
    return True


def maxbad_sharp(i, j):
    """Exact max of Bad^sharp(i,j) (None if empty), via the same segment
    decomposition: inside a segment the bad set is a prefix, found by
    exact binary search on the increasing function C(n,i)."""
    tgt = Cj(i, j)
    upper = NK(i, j)
    if upper < 2 * j:
        return None
    starts = [2 * j] + [x for x in prime_powers_upto(i, upper) if x > 2 * j]
    best = None
    for idx, s in enumerate(starts):
        e = (starts[idx + 1] - 1) if idx + 1 < len(starts) else upper
        e = min(e, upper)
        if s > e:
            continue
        U = Usharp(s, i)
        if comb(s, i) <= U * tgt:
            if comb(e, i) <= U * tgt:
                r = e
            else:
                lo_, hi_ = s, e
                while hi_ - lo_ > 1:
                    m = (lo_ + hi_) // 2
                    if comb(m, i) <= U * tgt:
                        lo_ = m
                    else:
                        hi_ = m
                r = lo_
            best = r
    return best


def brute_bad_sharp(i, j):
    tgt = Cj(i, j)
    upper = NK(i, j)
    return [n for n in range(2 * j, upper + 1) if comb(n, i) <= Usharp(n, i) * tgt]


# ---------------------------------------------------- candidate C setup
def windows_from_primes(i, primes):
    """Prime-free windows [p+i, p+g-1] for gaps (p, p+g), g > i."""
    wins = []
    for a, b in zip(primes, primes[1:]):
        g = b - a
        if g > i:
            wins.append((a + i, b - 1))
    return wins


def settled_C(i, j, windows):
    """Exact test of candidate C via windows + segment minima.
    A C-witness must lie in a window; inside a window the minimum of
    C(n,i)/U^sharp(n,i) is at the window start (clipped to n >= 2j) or
    at a prime power inside the window.  Windows are sorted; a window
    starting above N_K(i,j) cannot contain a bad n (S1 Lemma 5(a))."""
    tgt = Cj(i, j)
    upper = NK(i, j)
    jumps = prime_powers_upto(i, upper)
    for (a, b) in windows:
        if b < 2 * j:
            continue
        if a > upper:
            break
        lo_ = max(a, 2 * j)
        hi_ = min(b, upper)
        if lo_ > hi_:
            continue
        cands = [lo_] + [x for x in jumps if lo_ < x <= hi_]
        for c in cands:
            if comb(c, i) <= Usharp(c, i) * tgt:
                return False
    return True


def brute_settled_C(i, j, primes_set, upper_hint=None):
    """Direct definition of C, for validation on small cases only."""
    tgt = Cj(i, j)
    upper = NK(i, j)
    for n in range(2 * j, upper + 1):
        if comb(n, i) <= Usharp(n, i) * tgt:
            if all((n - k) not in primes_set for k in range(i)):
                return False
    return True


# ------------------------------------------------------- validation runs
log("=" * 72)
log("2.  Validation of the segment-minima tests against brute force")
for i in (3, 5, 10, 20):
    for j in range(i + 1, i + 41):
        bb = brute_bad_sharp(i, j)
        assert settled_B(i, j, G[i]) == all(n <= G[i] for n in bb), (i, j)
        assert maxbad_sharp(i, j) == (max(bb) if bb else None), (i, j)
log("    settled_B and maxbad_sharp == brute force for i in {3,5,10,20},")
log("    all j in (i, i+40].")
for j in (200, 500, 1000):
    bb = brute_bad_sharp(100, j)
    assert maxbad_sharp(100, j) == (max(bb) if bb else None), j
    assert settled_B(100, j, G[100]) == all(n <= G[100] for n in bb), j
log("    settled_B and maxbad_sharp == brute force for i=100, j in {200,500,1000}")
# Full per-n brute force at the i=100 candidate-B threshold itself
# (N_K ~ 6.4*10^5; math.comb evaluated independently at every n).
for j in (22587, 22588):
    bb = brute_bad_sharp(100, j)
    assert maxbad_sharp(100, j) == (max(bb) if bb else None), j
    assert settled_B(100, j, G[100]) == all(n <= G[100] for n in bb), j
    log(f"    i=100, j={j}: brute-force max Bad^sharp = "
        f"{max(bb) if bb else None} (G=370360), settled_B = "
        f"{all(n <= G[100] for n in bb)}")
log("    settled_B and maxbad_sharp == full brute force at the i=100")
log("    candidate-B threshold j = 22587/22588 as well.")
for i in (3, 5, 10, 20):
    lim = NK(i, i + 40) + 5
    pr = primes_upto(lim)
    wins = windows_from_primes(i, pr)
    pset = set(pr)
    for j in range(i + 1, i + 41):
        assert settled_C(i, j, wins) == brute_settled_C(i, j, pset), (i, j)
log("    settled_C (window/minima form) == brute-force C for i in {3,5,10,20},")
log("    all j in (i, i+40].")

# i=3, candidate B, for ALL j >= 8: 2j itself is sharp-bad and 2j > G(3)=9.
# Ratio C(2j,3)/C(j,3) = 4(2j-1)/(j-2) <= 10 for j >= 8 (decreasing),
# while U^sharp(2j,3) = largest power of 2 <= 2j is >= 16 for j >= 8.
for j in range(8, 5001):
    assert comb(2 * j, 3) <= Usharp(2 * j, 3) * comb(j, 3)
log("    i=3: verified exactly for 8 <= j <= 5000 that 2j in Bad^sharp(3,j);")
log("    the closed-form ratio bound in the .md extends this to all j >= 8,")
log("    so candidate B settles no (3,j) with j >= 7 (j=7: Bad^sharp={16}).")

CLAIMED = {3: 5, 5: 12, 10: 30, 20: 138, 100: 25063, 200: 713421, 394: 360654145}

# ------------------------------------------------ small i: full enumeration
log("=" * 72)
log("3.  Small i: complete enumeration (settled sets, not just prefixes)")
ENUM = {3: 200, 5: 200, 10: 200, 20: 300}   # C enumerated to these j
ENUM_B_EXTRA = {3: 2000}                    # B (and A) enumerated further for i=3
results = {}
for i in (3, 5, 10, 20):
    jmax = ENUM[i]
    lim = NK(i, jmax) + 5
    pr = primes_upto(max(lim, 64))
    wins = windows_from_primes(i, pr)
    setA, setB, setC = [], [], []
    for j in range(i + 1, jmax + 1):
        if settled_A(i, j, G[i]):
            setA.append(j)
        if settled_B(i, j, G[i]):
            setB.append(j)
        if settled_C(i, j, wins):
            setC.append(j)
    if i in ENUM_B_EXTRA:
        setA2, setB2 = list(setA), list(setB)
        for j in range(jmax + 1, ENUM_B_EXTRA[i] + 1):
            if settled_A(i, j, G[i]):
                setA2.append(j)
            if settled_B(i, j, G[i]):
                setB2.append(j)
        log(f"    i={i}: A settled set to j<={ENUM_B_EXTRA[i]}: {setA2}")
        log(f"    i={i}: B settled set to j<={ENUM_B_EXTRA[i]}: {setB2}")
    results[i] = (setA, setB, setC)
    log(f"    i={i}: A settled in (i,{jmax}]: {setA}")
    log(f"    i={i}: B settled in (i,{jmax}]: {setB}")
    log(f"    i={i}: C settled in (i,{jmax}]: {setC}")
    cl = CLAIMED[i]
    for nm, st in (("A", setA), ("B", setB), ("C", setC)):
        # prefix length of the settled set, starting at j=i+1
        pref = i
        while pref + 1 in st:
            pref += 1
        log(f"      candidate {nm}: prefix settled-j = {pref}; claimed = {cl}; "
            f"NK(claim)={NK(i, cl)}, Msharp(claim)={maxbad_sharp(i, cl)}, G={G[i]}")

# ------------------------------------------------------------------ i=100
log("=" * 72)
log("4.  i=100 (G=370360 from own sieve above)")
i = 100
PRIMES_1M = primes_upto(1000000)
wins100 = windows_from_primes(i, PRIMES_1M)
log(f"    prime-free windows for i=100 up to 10^6: {wins100}")


def prefix_search(fn, i, lo_j, hi_j):
    """Largest settled j in [lo_j, hi_j] by binary search; caller must
    have checked fn(lo_j) is True and fn(hi_j) is False, and must supply
    the prefix justification (see .md): used only in ranges where the
    settled set is provably a prefix, and spot-verified around the
    crossing by direct evaluation of every neighbouring j."""
    assert fn(i, lo_j)
    assert not fn(i, hi_j)
    lo, hi = lo_j, hi_j
    while hi - lo > 1:
        m = (lo + hi) // 2
        if fn(i, m):
            lo = m
        else:
            hi = m
    return lo


# For i=100 all searches stay at j <= 25063 << G/2 = 185180, where the
# prefix property is a proof, not an assumption (.md, 'monotonicity'):
# if (i,j2) is settled and i<j1<j2 with 2*j2 <= G, any bad prime-free /
# bad-over-G witness for j1 either is >= 2*j2 (hence also a witness for
# j2, since C(j,j-i) grows with j) or lies in [2*j1, 2*j2) <= G, where by
# definition of G no prime-free n exists and 'n > G' fails.
prefA100 = prefix_search(lambda ii, jj: settled_A(ii, jj, G[ii]), i, 101, CLAIMED[i])
prefB100 = prefix_search(lambda ii, jj: settled_B(ii, jj, G[ii]), i, 101, CLAIMED[i])
prefC100 = prefix_search(lambda ii, jj: settled_C(ii, jj, wins100), i, 101, CLAIMED[i])
results[100] = (prefA100, prefB100, prefC100)
for nm, pref, fn in (
    ("A", prefA100, lambda jj: settled_A(i, jj, G[i])),
    ("B", prefB100, lambda jj: settled_B(i, jj, G[i])),
    ("C", prefC100, lambda jj: settled_C(i, jj, wins100)),
):
    neigh = [fn(j) for j in range(pref - 2, pref + 3)]
    log(f"    candidate {nm}: prefix settled-j = {pref}; neighbourhood "
        f"j={pref-2}..{pref+2} settled flags = {neigh}")
log(f"    at claimed j=25063: NK={NK(i, 25063)}, Msharp={maxbad_sharp(i, 25063)}, "
    f"G={G[i]}")

# ------------------------------------------------------------- big sieve
log("=" * 72)
log("5.  i=200: own sieve to 50,000,000 (G and windows)")
t = time.time()
PRIMES_50M = primes_upto(50000000)
log(f"    sieve done in {time.time() - t:.1f}s; {len(PRIMES_50M)} primes")
p200, gap200 = first_gap_over(200, PRIMES_50M)
G[200] = p200 + 200 - 1
log(f"    first gap > 200 (exhaustive scan, in order): gap {gap200} at "
    f"p={p200} -> G(200) = {G[200]}")
wins200 = windows_from_primes(200, PRIMES_50M)
log(f"    prime-free windows for i=200 up to 5*10^7: {wins200}")
i = 200
prefA200 = prefix_search(lambda ii, jj: settled_A(ii, jj, G[ii]), i, 201, CLAIMED[i])
prefB200 = prefix_search(lambda ii, jj: settled_B(ii, jj, G[ii]), i, 201, CLAIMED[i])
prefC200 = prefix_search(lambda ii, jj: settled_C(ii, jj, wins200), i, 201, CLAIMED[i])
results[200] = (prefA200, prefB200, prefC200)
log(f"    A prefix = {prefA200}; B prefix = {prefB200}; C prefix = {prefC200}")
log(f"    at claimed j=713421: NK={NK(i, 713421)}, "
    f"Msharp={maxbad_sharp(i, 713421)}, G={G[i]}")
log(f"    B first failure point at j={prefB200 + 1}: "
    f"bad at n=G+1={G[i] + 1} (window start): "
    f"{comb(G[i] + 1, i) <= Usharp(G[i] + 1, i) * Cj(i, prefB200 + 1)}")

# ------------------------------------------------------------------ i=394
log("=" * 72)
log("6.  i=394: G from published maximal-gap records (see .md for sources)")
# Maximal (record) prime gaps, OEIS A005250 / A002386 (Nicely's tables),
# as tabulated e.g. in the maximal-gap table on Wikipedia ('Prime gap',
# crawled 2026-10-27) and cross-checked against the record-gap table in
# Granville-Lumley, arXiv:2009.05000, Fig. 4, and Kourbatov,
# arXiv:1309.4053 (gap 456: 25056082087 -> 25056082543):
#   ... gap 382 at 10726904659, gap 394 at 22367084959,
#       gap 456 at 25056082087, gap 464 at 42652618343, ...
# A gap > 394 occurring before 25056082087 would exceed every earlier
# gap (the maximum up to that point is the record 394 itself), hence
# would itself be a record with value in (394, 456]; the published
# record list contains no such record.  Therefore the first gap > 394
# is the 456 gap at p = 25056082087.
P456, GAP456 = 25056082087, 456
assert P456 + GAP456 == 25056082543
G[394] = P456 + 394 - 1
log(f"    first gap > 394: gap {GAP456} at p={P456} (published record) "
    f"-> G(394) = {G[394]}")
i = 394
prefA394 = prefix_search(lambda ii, jj: settled_A(ii, jj, G[ii]), i, 395, CLAIMED[i])
prefB394 = prefix_search(lambda ii, jj: settled_B(ii, jj, G[ii]), i, 395, CLAIMED[i])
results[394] = (prefA394, prefB394, None)
log(f"    A prefix = {prefA394}; B prefix = {prefB394}")
log(f"    at claimed j=360654145: NK={NK(i, 360654145)}, "
    f"Msharp={maxbad_sharp(i, 360654145)}, G={G[i]}")
# Candidate C for i=394, prefix only, by the witness argument:
#  (a) every j <= prefB394 is B-settled (prefix range, 2j << G) hence
#      C-settled (a C-witness is a bad n that is prime-free; prime-free
#      implies n > G by definition of G, contradicting B-settled);
#  (b) at j = prefB394 + 1 the point n0 = G+1 is sharp-bad (checked
#      exactly here) and prime-free: n0 = P456 + 394 is the first point
#      of the first window [P456+394, P456+455].
n0 = G[394] + 1
wit = comb(n0, i) <= Usharp(n0, i) * Cj(i, prefB394 + 1)
log(f"    C witness check at j={prefB394 + 1}: n0=G+1={n0} in first window "
    f"[{P456 + 394}, {P456 + GAP456 - 1}] and sharp-bad: {wit}")
assert wit
results[394] = (prefA394, prefB394, prefB394)
log(f"    C prefix = {prefB394} (by the witness argument above; individual")
log("    C status for j beyond the first failure is NOT asserted for i=394,")
log("    and a full window table up to N_K ~ 4.3*10^10 cannot be sieved")
log("    inside the resource bounds - see .md.)")

# ---------------------------------------------------------------- ratios
log("=" * 72)
log("7.  Asymptotic-claim consistency: j / (i * (ln i)^2), natural log")
for i in (3, 5, 10, 20, 100, 200, 394):
    denom = i * math.log(i) ** 2
    cl = CLAIMED[i]
    bval = results[i][1]
    bval = bval if isinstance(bval, int) else max(
        j for j in range(i + 1, 400) if False) if False else bval
    # for small i results[i][1] is a settled SET; take its prefix length
    if isinstance(results[i][1], list):
        pref = i
        while pref + 1 in results[i][1]:
            pref += 1
        bval = pref
    log(f"    i={i:>3}: claimed {cl} -> ratio {cl / denom:12.3f}; "
        f"candidate-B prefix {bval} -> ratio {bval / denom:12.3f}; "
        f"i*(ln i)^2 = {denom:.1f}")

log("=" * 72)
log("SUMMARY (prefix settled-j; his claimed value in brackets)")
for i in (3, 5, 10, 20, 100, 200, 394):
    ra, rb, rc = results[i]
    def pref_of(x):
        if isinstance(x, list):
            p = i
            while p + 1 in x:
                p += 1
            return p
        return x
    log(f"    i={i:>3}: A={pref_of(ra)}, B={pref_of(rb)}, C={pref_of(rc)} "
        f"[claimed {CLAIMED[i]}]   G(i)={G[i]}")
log(f"Total runtime: {time.time() - T0:.1f}s")
