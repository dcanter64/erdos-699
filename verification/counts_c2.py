"""Cycle 2 housekeeping computation (HK-B): exact marginal contributions and
exact union of the clearance criteria, in the order (1)-(7), against the
cap-20,000 sweep baseline.

Scope: pairs (i, j), 1 <= i <= 1000, floor(3i/2) < j <= 5000 (4,249,500 pairs).
Baseline: ~/workspace/math-hunt/erdos-699/pairpass_20000.json frontiers
J_i^20000 (in-scope cleared count 1,302,183, coordinator-verified).

Conventions (from strategies/S1.md, strategies/S3.md, proofs/P-C1.md, P-C2.md,
verification/union_check.py):
  * C(a,b) = math.comb.  The EEES bound is
    N(i,j) = max{ n : C(n,i) < C(2j, 2(j-i)) } = max{ n : C(n,i) < C(2j,2i) }.
  * pi(x) = number of primes <= x.
  * S1 crude predicate (union_check.py): C(j,i) * 10001^{pi(i-1)} < C(10001,i).
  * U^sharp(n,i) = prod_{p<i} q_p(n), q_p(n) = largest power of p that is <= n.
    G_i(n) = C(n,i)/U^sharp(n,i);  F_i(n) = C(n,i)/n^{pi(i-1)};
    N_K(i,j) = max{ n : F_i(n) <= C(j, j-i) } (S1 Lemma 4: F_i increasing).
    Bad^sharp(i,j) = { n >= 2j : C(n,i) <= U^sharp(n,i) * C(j, j-i) }.
    By S1 Lemma 5, G_i is strictly increasing on intervals where U^sharp is
    constant and U^sharp jumps exactly at prime powers p^e (p < i); hence the
    local minima of G_i on [2j, oo) are at n = 2j and at the jump points
    themselves.  NOTE: the Cycle 2 task text said "test at n = q-1"; that is
    a slip -- at (i,j) = (3,7) the unique bad n is 16, itself a jump point
    (U^sharp jumps 8 -> 16 there), and testing at q-1 = 15 would miss it and
    contradict the anchor Bad^sharp(3,7) = {16}.  This script tests at
    n = 2j and at jump points q in (2j, N_K(i,j)].
  * S3: G(X) = max{ p_{k+1} - p_k : p_k < X } (strict lower end, P-C1/P-C2);
    pair cleared iff i >= G(N(i,j)).
  * Primorial R1: P(i,j) = prod_{i<p<=j} p; criterion P(i,j)^2 <= C(2j,i)
    on the window floor(3i/2) < j < 2i.

Step (4) is computed in three forms (see counts_c2.md for why):
  L   : literal task definition, Bad^sharp(i,j) = empty (all n >= 2j).
  S10 : sweep-relative at the old cap, Bad^sharp(i,j) cap [10001, oo) = empty
        (the sharp analogue of S1 Theorem D / follow-up V2).
  S20 : sweep-relative at the current cap, Bad^sharp cap [20001, oo) = empty.
For S10/S20 the cleared predicate per row is C(j,i) < M_i(T*) with
M_i(T*) = min_{n >= T*+1} G_i(n), a constant in j, so it is exactly a prefix
in j; the frontier is found by exact binary search against M_i.

Stdlib only, exact integer / Fraction arithmetic, single thread.
Writes verification/counts_c2.json with every frontier and table entry.
"""

import json
import random
import time
from fractions import Fraction
from math import comb, e as EULER, lgamma, log

T0 = time.time()
BASE_DIR = "/home/hatch/workspace/math-hunt/erdos-699"
PROOF_DIR = "/home/hatch/workspace/math-hunt/erdos-699-proof"
IMAX, JMAX = 1000, 5000
SCOPE_TOTAL = 4249500


def lo_i(i):
    return (3 * i) // 2


def primes_upto(n):
    s = bytearray(b"\x01") * (n + 1)
    if n >= 0:
        s[0] = 0
    if n >= 1:
        s[1] = 0
    for p in range(2, int(n ** 0.5) + 1):
        if s[p]:
            s[p * p :: p] = b"\x00" * len(s[p * p :: p])
    return [p for p, v in enumerate(s) if v]


PRIMES = primes_upto(100000)
PRIMES_SET = set(PRIMES)
import bisect

pi = lambda x: bisect.bisect_right(PRIMES, x)


def Usharp(n, i):
    """Exact prod_{p<i} (largest power of p <= n)."""
    u = 1
    for p in PRIMES:
        if p >= i:
            break
        q = p
        while q * p <= n:
            q *= p
        u *= q
    return u


def prime_powers_in(i, a, b):
    """Distinct prime powers p^e (p < i prime, e >= 2) in (a, b], sorted.
    (e = 1 values are the primes < i themselves; a jump at n = p <= ... is
    included by callers through the segment start point, see minima code:
    for the ranges used here a >= i, so e=1 jumps are <= a or irrelevant --
    for the literal bad set we take a = 2j >= i+... and include every e>=1
    jump > 2j via prime_powers_all below.)"""
    res = set()
    for p in PRIMES:
        if p >= i:
            break
        q = p * p
        while q <= b:
            if q > a:
                res.add(q)
            if q > b // p:
                break
            q *= p
    return sorted(res)


def prime_powers_all(i, a, b):
    """All distinct prime powers p^e (p < i, e >= 1) in (a, b], sorted."""
    res = set()
    for p in PRIMES:
        if p >= i:
            break
        q = p
        while q <= b:
            if q > a:
                res.add(q)
            if q > b // p:
                break
            q *= p
    return sorted(res)


# ---------------------------------------------------------------- Stage A
print("=== Stage A: baseline (sweep-20000) ===")
d20 = json.load(open(f"{BASE_DIR}/pairpass_20000.json"))
assert d20["nstar"] == 20000
front20 = {}
base_in_scope = 0
for i in range(1, IMAX + 1):
    lst = [j for j in d20["cleared_js_by_i"][str(i)] if lo_i(i) < j <= JMAX]
    if lst:
        assert lst == list(range(lo_i(i) + 1, max(lst) + 1)), f"row {i} not a clean prefix"
        front20[i] = max(lst)
    else:
        front20[i] = lo_i(i)
    base_in_scope += front20[i] - lo_i(i)
scope_total = sum(JMAX - lo_i(i) for i in range(1, IMAX + 1))
print(f"scope total pairs: {scope_total}")
assert scope_total == SCOPE_TOTAL
print(f"(1) baseline cleared in scope: {base_in_scope}")
assert base_in_scope == 1302183, base_in_scope
print("every baseline row is a clean prefix in scope: True")

# ---------------------------------------------------------------- Stage B
print("=== Stage B: (3) S1 crude predicate (validation on OLD baseline) ===")
d10 = json.load(open(f"{BASE_DIR}/pairpass.json"))
assert d10["pairs_considered"] == 4249500 and d10["pairs_fully_cleared"] == 768741
front10 = {}
for i in range(1, IMAX + 1):
    lst = d10["cleared_js_by_i"][str(i)]
    front10[i] = max(lst) if lst else lo_i(i)

_pow_cache = {}


def crude_pred(i, j):
    if i not in _pow_cache:
        _pow_cache[i] = (comb(10001, i), 10001 ** pi(i - 1))
    rhs, pw = _pow_cache[i]
    return comb(j, i) * pw < rhs


def J_K(i):
    lo, hi = lo_i(i), JMAX
    if not crude_pred(i, lo + 1):
        return lo
    while lo < hi:
        m = (lo + hi + 1) // 2
        if crude_pred(i, m):
            lo = m
        else:
            hi = m - 1
    return lo


JK = {i: J_K(i) for i in range(1, IMAX + 1)}
newly_old = sum(max(0, JK[i] - front10[i]) for i in range(1, IMAX + 1))
print(f"validation: crude newly vs OLD baseline = {newly_old} (target 328079)")
print(f"validation: J_K(100) = {JK[100]} (target 1045)")
print(f"validation: J_K(1000) = {JK[1000]} (target 2541)")
assert newly_old == 328079 and JK[100] == 1045 and JK[1000] == 2541

print("=== Steps (1)-(3) marginals (new baseline) ===")
cur = dict(front20)  # running union frontier per row (all criteria are prefixes)
tot = base_in_scope
step2 = 0
for i in range(132, IMAX + 1):
    step2 += JMAX - cur[i]
    cur[i] = JMAX
tot += step2
print(f"(2) S3 uniform i>=132: newly {step2}; running union {tot}")
step3 = 0
for i in range(1, 132):
    add = max(0, JK[i] - cur[i])
    step3 += add
    cur[i] = max(cur[i], JK[i])
tot += step3
print(f"(3) S1 crude (10001 predicate): newly {step3}; running union {tot}")
cur_after3 = dict(cur)

# ---------------------------------------------------------------- Stage C
print("=== Stage C: (4) S1 sharp-sawtooth ===")


def NK_exact(i, j):
    """max n with C(n,i) <= n^{pi(i-1)} * C(j, j-i)  (crude bound)."""
    tgt = comb(j, i)
    pp = pi(i - 1)
    bad = lambda n: comb(n, i) <= n ** pp * tgt
    if not bad(2 * j):
        return 2 * j - 1
    lo, hi = 2 * j, 4 * j + 10
    while bad(hi):
        hi *= 2
    while hi - lo > 1:
        m = (lo + hi) // 2
        lo, hi = (m, hi) if bad(m) else (lo, m)
    return lo


def bad_sharp_minima(i, j):
    """Bad^sharp(i,j) restricted to the Lemma-5 minima points
    {2j} u {prime powers q in (2j, N_K(i,j)]}: the full bad set is empty
    iff this set is empty, and (3,7)-type singletons are minima points."""
    tgt = comb(j, i)
    nk = NK_exact(i, j)
    cand = [2 * j] + prime_powers_all(i, 2 * j, nk)
    return [n for n in cand if comb(n, i) <= Usharp(n, i) * tgt]


def bad_sharp_bruteforce(i, j):
    """Direct scan of every n in [2j, N_K(i,j)] with exact U^sharp."""
    tgt = comb(j, i)
    nk = NK_exact(i, j)
    # prime-power jump table up to nk for incremental U^sharp
    jump = {}
    for p in PRIMES:
        if p >= i:
            break
        q = p
        while q <= nk:
            jump[q] = p
            if q > nk // p:
                break
            q *= p
    res = []
    u = Usharp(2 * j - 1, i) if 2 * j >= 1 else 1
    c = comb(2 * j, i)
    for n in range(2 * j, nk + 1):
        if n in jump:
            u *= jump[n]
        if n > 2 * j:
            c = c * n // (n - i)  # C(n,i) from C(n-1,i)
        if c <= u * tgt:
            res.append(n)
    return res


# Anchor: Bad^sharp(3,7) = {16}
b37_min = bad_sharp_minima(3, 7)
b37_bf = bad_sharp_bruteforce(3, 7)
print(f"validation: Bad^sharp(3,7) via minima = {b37_min} (target [16])")
print(f"validation: Bad^sharp(3,7) via brute force = {b37_bf} (target [16])")
assert b37_min == [16] and b37_bf == [16]

# Cross-check minima method vs brute force on a seeded sample (small i incl.)
rng = random.Random(20261029)
sample = [(3, 5), (3, 6), (3, 20), (4, 12), (5, 15), (10, 30), (5, 8), (10, 100)]
tries = 0
while len(sample) < 20 and tries < 400:
    tries += 1
    i = rng.randint(3, 40)
    j = rng.randint(lo_i(i) + 1, 2000)
    if NK_exact(i, j) <= 6000 and (i, j) not in sample:
        sample.append((i, j))
bf_ok = True
for (i, j) in sample:
    a = bad_sharp_minima(i, j)
    bset = set(bad_sharp_bruteforce(i, j))
    aset = set(a)
    # minima set must contain every "segment-first" bad n; the brute bad set
    # projected to minima: check emptiness agreement and that every brute-bad
    # segment's first element is in a.  Direct check used here: for the
    # sampled pairs we compare the full bad set from an independent scan of
    # candidate segments -- emptiness and the set of bad minima must match:
    if (len(aset) == 0) != (len(bset) == 0):
        bf_ok = False
        print("  MISMATCH emptiness", i, j, a, sorted(bset)[:5])
    for n in a:
        if n not in bset:
            bf_ok = False
            print("  MISMATCH minima not bad", i, j, n)
print(f"cross-check minima vs brute force on {len(sample)} seeded pairs "
      f"(incl. small i): emptiness and minima membership agree: {bf_ok}")
assert bf_ok

# --- Literal form L: Bad^sharp = empty over all n >= 2j.
# R_start(j) = G_i(2j)/C(j,i).  Between U^sharp jumps at 2j, the comb factor
# of R_start(j+1)/R_start(j) is
#   [(2j+2)(2j+1)(j+1-i)] / [(j+1)(2j+2-i)(2j+1-i)],
# and D - N = i(i-1)(j+1) exactly (expand: with a=j+1, D/a - N/a =
# (2a-i)(2a-1-i) - 2(2a-1)(a-i) = i^2 - i).  Verify the identity on a grid:
ident_ok = True
for i in range(1, 60):
    for j in range(i + 1, 400, 7):
        N_ = (2 * j + 2) * (2 * j + 1) * (j + 1 - i)
        D_ = (j + 1) * (2 * j + 2 - i) * (2 * j + 1 - i)
        if D_ - N_ != i * (i - 1) * (j + 1):
            ident_ok = False
print(f"start-ratio identity D-N = i(i-1)(j+1) verified on grid: {ident_ok}")
assert ident_ok
# Hence for i >= 2, R_start is strictly decreasing in j (comb factor < 1 and
# U^sharp(2j) nondecreasing), so the start-bad set {j : 2j in Bad^sharp} is a
# tail.  Check its first scope point for every i >= 4:
startbad_first = {}
for i in range(4, IMAX + 1):
    j = lo_i(i) + 1
    startbad_first[i] = comb(2 * j, i) <= Usharp(2 * j, i) * comb(j, i)
n_startbad = sum(startbad_first.values())
print(f"i>=4 with 2j in Bad^sharp already at first scope j: {n_startbad} of 997")
assert n_startbad == 997
# Therefore NO scope pair with i >= 4 is literal-sharp-cleared.
# i = 3: per-pair exact scan (minima method).
lit3 = []
for j in range(lo_i(3) + 1, JMAX + 1):
    if not bad_sharp_minima(3, j):
        lit3.append(j)
print(f"literal-sharp-cleared scope pairs at i=3: {lit3}")
assert lit3 == [5, 6]
# i = 1, 2: U^sharp = 1 (no primes < i... for i=2 no prime < 2; i=1 none),
# G_i(n) = C(n,i) is increasing in n, min at n = 2j, and C(2j,i) > C(j,i):
lit12_ok = all(comb(2 * j, 1) > comb(j, 1) for j in range(2, JMAX + 1)) and \
           all(comb(2 * j, 2) > comb(j, 2) for j in range(3, JMAX + 1))
print(f"i=1,2 literal-sharp-cleared for all j (direct check): {lit12_ok}")
assert lit12_ok
J_sharp_lit = {1: JMAX, 2: JMAX, 3: 6}
for i in range(4, IMAX + 1):
    J_sharp_lit[i] = lo_i(i)
lit_viol = [i for i in range(1, IMAX + 1) if J_sharp_lit[i] < JK[i]]
print(f"ANCHOR CHECK (literal): J_K^sharp(i) >= J_K(i) for all i: "
      f"{len(lit_viol) == 0}  (violations at {len(lit_viol)} values of i; "
      f"e.g. i=100: J_sharp_lit={J_sharp_lit[100]} vs J_K={JK[100]}; "
      f"i=3: {J_sharp_lit[3]} vs {JK[3]})")

# --- Sweep-relative forms S10 / S20.
def logC(n, k):
    return lgamma(n + 1) - lgamma(k + 1) - lgamma(n - k + 1) if 0 <= k <= n else -1e18


def NK_cap(i):
    """A verified cap >= N_K(i, 5000): float estimate, then exact check
    F_i(cap) > C(5000, i) (F_i increasing, S1 Lemma 4)."""
    pp = pi(i - 1)
    tgt = logC(5000, i)
    lo, hi = 10000, 10001
    f = lambda n: logC(n, i) - pp * log(n)
    while f(hi) <= tgt:
        hi *= 2
    while hi - lo > 1:
        m = (lo + hi) // 2
        if f(m) <= tgt:
            lo = m
        else:
            hi = m
    cap = int(lo * 1.15) + 1000
    t5000 = comb(5000, i)
    while comb(cap, i) <= cap ** pp * t5000:
        cap = int(cap * 1.5) + 1
    return cap


def sharp_frontier(Tstar, i):
    """Largest scope j with no Bad^sharp n > Tstar, via the constant
    threshold M_i = min_{n >= Tstar+1} G_i(n) (candidates: n = Tstar+1 and
    prime powers in (Tstar, cap]); C(j,i) < M_i is the exact predicate."""
    cap = NK_cap(i)
    cand = [Tstar + 1] + prime_powers_in(i, Tstar, cap)
    M = None
    for n in cand:
        g = Fraction(comb(n, i), Usharp(n, i))
        if M is None or g < M:
            M = g
    if comb(JMAX, i) * M.denominator < M.numerator:
        return JMAX
    lo, hi = lo_i(i), JMAX
    pred = lambda j: comb(j, i) * M.denominator < M.numerator
    if not pred(lo + 1):
        return lo
    while lo < hi:
        m = (lo + hi + 1) // 2
        if pred(m):
            lo = m
        else:
            hi = m - 1
    return lo


J_sharp = {}
for Tstar, key in [(10000, "S10"), (20000, "S20")]:
    J_sharp[key] = {i: sharp_frontier(Tstar, i) for i in range(1, IMAX + 1)}
    viol = [i for i in range(1, IMAX + 1) if J_sharp[key][i] < JK[i]]
    print(f"{key}: J_K^sharp samples "
          f"{{3: {J_sharp[key][3]}, 100: {J_sharp[key][100]}, "
          f"131: {J_sharp[key][131]}, 1000: {J_sharp[key][1000]}}}; "
          f"anchor J_K^sharp >= J_K violations: {len(viol)}")

# Spot-verify S10/S20 frontiers by a direct per-pair test at j = frontier
# and j = frontier+1 for sampled rows:
def sharp_rel_cleared_direct(i, j, Tstar):
    nk = NK_exact(i, j)
    cand = [Tstar + 1] + prime_powers_in(i, Tstar, nk)
    tgt = comb(j, i)
    return all(comb(n, i) > Usharp(n, i) * tgt for n in cand)


spot_ok = True
for key, Tstar in [("S10", 10000), ("S20", 20000)]:
    for i in [3, 10, 50, 100, 131, 500, 1000]:
        f = J_sharp[key][i]
        if f > lo_i(i) and not sharp_rel_cleared_direct(i, f, Tstar):
            spot_ok = False
            print("  spot FAIL cleared", key, i, f)
        if f < JMAX and sharp_rel_cleared_direct(i, f + 1, Tstar):
            spot_ok = False
            print("  spot FAIL not-cleared", key, i, f + 1)
print(f"S10/S20 frontier spot-verification (direct per-pair test): {spot_ok}")
assert spot_ok

# Marginals of step (4) in each form, on top of steps (1)-(3):
def marginal_after(curbase, frontiers):
    add = 0
    newcur = dict(curbase)
    for i in range(1, 132):
        a = max(0, frontiers[i] - newcur[i])
        add += a
        newcur[i] = max(newcur[i], frontiers[i])
    return add, newcur


step4 = {}
cur_after4 = {}
step4["L"], cur_after4["L"] = 0, dict(cur_after3)
# literal sharp adds nothing: its cleared scope pairs are the i=1,2 rows
# (already cleared to 5000 by crude) and (3,5),(3,6) (baseline-cleared).
step4["S10"], cur_after4["S10"] = marginal_after(cur_after3, J_sharp["S10"])
step4["S20"], cur_after4["S20"] = marginal_after(cur_after3, J_sharp["S20"])
for k in ["L", "S10", "S20"]:
    print(f"(4) sharp [{k}]: newly {step4[k]}; running union "
          f"{tot + step4[k]}")

# ---------------------------------------------------------------- Stage D
print("=== Stage D: (5) S3 per-pair at i <= 131 ===")
# Bound max N over pairs not cleared at this step (headline chain L:
# remaining rows are 3 <= i <= 131 -- rows 1,2 are fully cleared by crude --
# and j <= 5000).  S3 Lemma 4: N(i,j) < e^2 j^2 / i, increasing in j,
# decreasing in i, so the max bound is at (i, j) = (3, 5000):
bound_N = int(EULER ** 2 * JMAX ** 2 / 3) + 1
print(f"Lemma-4 bound on max N over remaining pairs: N < {bound_N} "
      f"(at (3,5000)); sieve limit {bound_N} <= 2e8, plain (non-segmented) sieve")
SIEVE_MAX = bound_N
sv = bytearray(b"\x01") * (SIEVE_MAX + 1)
sv[0] = 0
sv[1] = 0
for p in range(2, int(SIEVE_MAX ** 0.5) + 1):
    if sv[p]:
        sv[p * p :: p] = b"\x00" * len(sv[p * p :: p])
# prime-gap records by scanning primes in order
records = []  # (gap, lower prime), strictly increasing gaps
prev = None
best = 0
nprimes = 0
pos = sv.find(1, 0)
while pos != -1:
    nprimes += 1
    if prev is not None and pos - prev > best:
        best = pos - prev
        records.append((best, prev))
    prev = pos
    pos = sv.find(1, pos + 1)
print(f"sieve to {SIEVE_MAX}: {nprimes} primes; record gaps: {records}")
del sv


def G_of(X):
    """G(X) = max gap p_{k+1}-p_k with p_k < X, from the record table."""
    g = 0
    for gap, p in records:
        if p < X:
            g = gap
        else:
            break
    return g


print(f"G validation: G(10127)={G_of(10127)} (36), G(1400000)={G_of(1400000)} "
      f"(132), G(2010733)={G_of(2010733)} (132), G(2010734)={G_of(2010734)} (148)")
assert G_of(10127) == 36 and G_of(1400000) == 132
assert G_of(2010733) == 132 and G_of(2010734) == 148

# B_i = smallest prime whose following gap exceeds i; then
# i >= G(N)  iff  N <= B_i  iff  C(2j, 2i) <= C(B_i + 1, i).
B = {}
for i in range(1, 132):
    for gap, p in records:
        if gap > i:
            B[i] = p
            break
    assert i in B, i


def J_S3pp(i):
    tgt = comb(B[i] + 1, i)
    lo, hi = lo_i(i), JMAX
    pred = lambda j: comb(2 * j, 2 * i) <= tgt
    if not pred(lo + 1):
        return lo
    while lo < hi:
        m = (lo + hi + 1) // 2
        if pred(m):
            lo = m
        else:
            hi = m - 1
    return lo


JS3 = {i: J_S3pp(i) for i in range(1, 132)}
print(f"J_S3pp samples: {{50: {JS3[50]}, 100: {JS3[100]}, 120: {JS3[120]}, "
      f"131: {JS3[131]}}}")


def N_exact(i, j):
    tgt = comb(2 * j, 2 * i)
    if comb(2 * j, i) >= tgt:
        return 2 * j - 1
    lo, hi = 2 * j, 4 * j + 10
    while comb(hi, i) < tgt:
        hi *= 2
    while hi - lo > 1:
        m = (lo + hi) // 2
        lo, hi = (m, hi) if comb(m, i) < tgt else (lo, m)
    return lo


N35000 = N_exact(3, 5000)
print(f"exact N(3,5000) = {N35000}; G(N(3,5000)) = {G_of(N35000)}; "
      f"criterion for (3,5000): {3 >= G_of(N35000)}")
# Validate the B_i threshold inversion against exact N at every frontier:
val5 = True
for i in range(3, 132):
    f = JS3[i]
    if f > lo_i(i):
        if not (i >= G_of(N_exact(i, f))):
            val5 = False
            print("  step5 frontier FAIL (should clear)", i, f)
    if f < JMAX:
        if i >= G_of(N_exact(i, f + 1)):
            val5 = False
            print("  step5 frontier FAIL (should not clear)", i, f + 1)
rng5 = random.Random(699)
for _ in range(40):
    i = rng5.randint(3, 131)
    j = rng5.randint(lo_i(i) + 1, JMAX)
    if (i >= G_of(N_exact(i, j))) != (j <= JS3[i]):
        val5 = False
        print("  step5 random FAIL", i, j)
print(f"step5 threshold inversion validated vs exact N "
      f"(all 129 frontiers, both sides, + 40 seeded pairs): {val5}")
assert val5

step5 = {}
cur_after5 = {}
for k in ["L", "S10", "S20"]:
    step5[k], cur_after5[k] = marginal_after(cur_after4[k], JS3)
    print(f"(5) S3 per-pair [{k} chain]: newly {step5[k]}; running union "
          f"{tot + step4[k] + step5[k]}")

# ---------------------------------------------------------------- Stage E
print("=== Stage E: (6) Primorial R1 ===")
r1_total = 0
r1_fails = []
for i in range(1, IMAX + 1):
    lo, hi = lo_i(i), min(2 * i - 1, JMAX)
    if hi <= lo:
        continue
    j = lo + 1
    P = 1
    for p in PRIMES:
        if p > j:
            break
        if p > i:
            P *= p
    C = comb(2 * j, i)
    while True:
        r1_total += 1
        if P * P > C:
            r1_fails.append((i, j))
        if j >= hi:
            break
        C = C * (2 * j + 2) * (2 * j + 1) // ((2 * j + 2 - i) * (2 * j + 1 - i))
        j += 1
        if j in PRIMES_SET and j > i:
            P *= j
print(f"R1 pairs in scope window: {r1_total}; failures: {r1_fails}")
assert r1_fails == [(4, 7), (10, 19)]
print(f"both failures baseline-cleared: "
      f"{front20[4] >= 7 and front20[10] >= 19} "
      f"(frontiers {front20[4]}, {front20[10]})")
step6 = {}
cur_after6 = {}
for k in ["L", "S10", "S20"]:
    add = 0
    for i in range(1, 132):
        lo, hi = lo_i(i), min(2 * i - 1, JMAX)
        for j in range(max(lo, cur_after5[k][i]) + 1, hi + 1):
            if (i, j) not in r1_fails:
                add += 1
    step6[k] = add
    cur_after6[k] = cur_after5[k]
    print(f"(6) Primorial R1 [{k} chain]: newly {add}; running union "
          f"{tot + step4[k] + step5[k] + add}")

# ---------------------------------------------------------------- Stage F
print("=== Stage F: totals, (7) parametric i=3, residual map ===")
results = {}
for k in ["L", "S10", "S20"]:
    total_k = tot + step4[k] + step5[k] + step6[k]
    front3 = cur_after6[k][3]
    f3 = {}
    for F in (158, 2000, 5000):
        extra = max(0, min(F, JMAX) - front3)
        f3[F] = (total_k + extra, SCOPE_TOTAL - total_k - extra)
    resid = {}
    for i in range(1, 132):
        f = cur_after6[k][i]
        if f < JMAX:
            resid[i] = (f, JMAX - f)
    results[k] = dict(step4=step4[k], step5=step5[k], step6=step6[k],
                      total=total_k, remaining=SCOPE_TOTAL - total_k,
                      front3=front3, f3=f3, resid=resid)
    print(f"[{k}] full union (steps 1-6): {total_k}; partial remaining: "
          f"{SCOPE_TOTAL - total_k}")
    print(f"[{k}] row-3 frontier after steps 1-6: {front3}; "
          f"(7) F3=158 -> total {f3[158][0]}, remaining {f3[158][1]}; "
          f"F3=2000 -> total {f3[2000][0]}, remaining {f3[2000][1]}; "
          f"F3=5000 -> total {f3[5000][0]}, remaining {f3[5000][1]}")
    print(f"[{k}] residual rows i<=131: {len(resid)} rows "
          f"(i = {min(resid)}..{max(resid)} contiguous: "
          f"{sorted(resid) == list(range(min(resid), max(resid) + 1))})")

out = dict(
    scope_total=SCOPE_TOTAL, baseline=base_in_scope,
    step2=step2, step3=step3,
    front20={str(i): front20[i] for i in range(1, IMAX + 1)},
    JK={str(i): JK[i] for i in range(1, IMAX + 1)},
    J_sharp_lit={str(i): J_sharp_lit[i] for i in range(1, IMAX + 1)},
    J_sharp_S10={str(i): J_sharp["S10"][i] for i in range(1, IMAX + 1)},
    J_sharp_S20={str(i): J_sharp["S20"][i] for i in range(1, IMAX + 1)},
    JS3pp={str(i): JS3[i] for i in range(1, 132)},
    B={str(i): B[i] for i in range(1, 132)},
    records=records, N_3_5000=N35000, r1_fails=r1_fails,
    results=results,
    final_frontier_L={str(i): cur_after6["L"][i] for i in range(1, 132)},
    final_frontier_S10={str(i): cur_after6["S10"][i] for i in range(1, 132)},
    final_frontier_S20={str(i): cur_after6["S20"][i] for i in range(1, 132)},
)
json.dump(out, open(f"{PROOF_DIR}/verification/counts_c2.json", "w"), indent=1)
print(f"wrote verification/counts_c2.json; total runtime {time.time() - T0:.1f}s")
