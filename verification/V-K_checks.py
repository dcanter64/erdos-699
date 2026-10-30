#!/usr/bin/env python3
"""V-K checks: independent verification of Cluster K (Cycle 3), i = 3.

Verifier's own implementations, Python stdlib only, exact arithmetic.
Design choices deliberately different from both computers where feasible:
  - Anchor A pair test in per-prime-power (q) form, factorisations by
    trial division (K1 also trial-divides; K2's K-a uses factor_fast).
  - K-a recount and K-b recount in the AGGREGATE form (R(n)|j,
    R(n-1)|j(j-1), R(n-2)|j(j-1)(j-2)), whose equivalence to the q-form
    is proved in V-K.md and validated empirically in section S3 below
    (all 6,974,250 candidate pairs at even n <= 10^6, pair by pair,
    plus a seeded random sample at larger n) BEFORE it is used.
  - K-c factorisation by trial division to 1000 + deterministic
    Miller-Rabin + a simple (non-Brent) Pollard rho with fixed seeds.
Sections print SUMMARY lines; run end-to-end or pass section names.
"""
import random
import sys
import time
from array import array
from math import comb, gcd, isqrt

T0 = time.time()
SUMMARY = []


def note(msg):
    print(f"[{time.time() - T0:8.1f}s] {msg}", flush=True)


def slog(label, value):
    SUMMARY.append((label, value))
    print(f"SUMMARY {label} = {value}", flush=True)


def primes_upto(n):
    s = bytearray(b"\x01") * (n + 1)
    s[0:2] = b"\x00\x00"
    for i in range(2, isqrt(n) + 1):
        if s[i]:
            s[i * i:n + 1:i] = b"\x00" * (((n - i * i) // i) + 1)
    return [i for i, v in enumerate(s) if v]


PR_1000 = primes_upto(1000)
PR_50000 = primes_upto(50000)


def factor_trial(m, primes=PR_50000):
    out = {}
    x = m
    for p in primes:
        if p * p > x:
            break
        if x % p == 0:
            a = 0
            while x % p == 0:
                x //= p
                a += 1
            out[p] = a
    if x > 1:
        out[x] = out.get(x, 0) + 1
    return out


def rel_qs(fac):
    return [p ** a for p, a in fac.items() if p >= 5 or (p == 3 and a >= 2)]


def R_formula(m):
    """R(m) via the odd-part formula (independent of factorisation)."""
    odd = m >> ((m & -m).bit_length() - 1)
    if odd % 3 == 0 and odd % 9 != 0:
        odd //= 3
    return odd


def N_of_3(j):
    """max{ n : C(n,3) < C(2j,6) } by exact binary search."""
    target = comb(2 * j, 6)
    lo = 2 * j
    hi = lo + 1
    while comb(hi, 3) < target:
        hi *= 2
    while lo < hi:
        mid = (lo + hi) // 2
        if comb(mid, 3) < target:
            lo = mid + 1
        else:
            hi = mid
    return lo - 1


def v3_int(x):
    v = 0
    while x % 3 == 0:
        x //= 3
        v += 1
    return v


# --------------------------------------------------------------- S0 anchors C
def section_S0():
    note("S0. Anchor C: N(3,j) spot values")
    expect = {7: 27, 100: 7908, 158: 19926, 159: 20181, 500: 201728,
              1000: 808934, 2000: 3239787, 5000: 20263871}
    got = {j: N_of_3(j) for j in expect}
    assert got == expect, got
    slog("S0_N_spot_all_match", True)
    slog("S0_N_values", got)


# ------------------------------------------- S1 brute force 5<=j<=60 (q-form)
def section_S1():
    note("S1. Brute force (no candidate generation), 5 <= j <= 60, q-form")
    pairs = 0
    surv = []
    for j in range(5, 61):
        Nj = N_of_3(j)
        for n in range(2 * j, Nj + 1):
            pairs += 1
            if any(j % q != 0 for q in rel_qs(factor_trial(n))):
                continue
            if any(j % q > 1 for q in rel_qs(factor_trial(n - 1))):
                continue
            if any(j % q > 2 for q in rel_qs(factor_trial(n - 2))):
                continue
            surv.append((n, j))
    slog("S1_bruteforce_pairs_5_60", pairs)
    slog("S1_bruteforce_survivors", surv)
    assert pairs == 52625 and not surv


# ------------------------------------------------- S2 Anchor A (q-form pairs)
def section_S2():
    note("S2. Anchor A: candidate counts (both generations) + pairs, q-form")
    NMAX = 20263871
    Nj = [0] * 5001
    for j in range(5, 5001):
        Nj[j] = N_of_3(j)
    # F-style generation (x3 branch unbounded) vs bounded generation.
    fstyle = set()
    bounded = set()
    for d in range(1, 5001, 2):
        v = v3_int(d)
        if v == 1:
            continue
        t = 1
        while d * t <= NMAX:
            fstyle.add(d * t)
            bounded.add(d * t)
            if v == 0:
                fstyle.add(d * 3 * t)
                if d * 3 * t <= NMAX:
                    bounded.add(d * 3 * t)
            t *= 2
    above = [n for n in fstyle if n > NMAX]
    slog("S2_F_style_candidates", len(fstyle))
    slog("S2_bounded_candidates", len(bounded))
    slog("S2_above_Nmax_count", len(above))
    slog("S2_above_all_in_(Nmax,3Nmax]", all(n <= 3 * NMAX for n in above))
    slog("S2_bounded_set_is_F_style_filtered",
         bounded == {n for n in fstyle if n <= NMAX})
    assert len(fstyle) == 50489 and len(bounded) == 47723
    assert len(above) == 2766 and all(n <= 3 * NMAX for n in above)
    # Pairs: iterate bounded candidates, q-form clause test.
    pairs = 0
    pairs2000 = 0
    surv = []
    for n in sorted(bounded):
        Rn = R_formula(n)
        assert Rn <= 5000
        q1 = rel_qs(factor_trial(n - 1))
        q2 = rel_qs(factor_trial(n - 2))
        j = ((5 + Rn - 1) // Rn) * Rn
        while j <= 5000 and 2 * j <= n:
            if n <= Nj[j]:
                pairs += 1
                if j <= 2000:
                    pairs2000 += 1
                if (all(j % q <= 1 for q in q1)
                        and all(j % q <= 2 for q in q2)):
                    surv.append((n, j))
            j += Rn
    slog("S2_anchorA_pairs", pairs)
    slog("S2_anchorA_pairs_j_le_2000", pairs2000)
    slog("S2_anchorA_survivors", surv)
    assert pairs == 341633 and pairs2000 == 107220 and not surv


# --------------------------- S3 aggregate equivalence + convention differences
def build_spf(L):
    spf = array("i", range(L + 1))
    for i in range(isqrt(L), 1, -1):
        cnt = (L - i) // i + 1
        spf[i::i] = array("i", [i] * cnt)
    return spf


def qs_spf(m, spf):
    qs = []
    x = m
    while x > 1:
        p = spf[x]
        q = 1
        a = 0
        while x % p == 0:
            x //= p
            q *= p
            a += 1
        if p >= 5 or (p == 3 and a >= 2):
            qs.append(q)
    return qs


def section_S3():
    note("S3. Aggregate-vs-q-form equivalence on ALL candidate pairs, "
         "even n <= 10^6; convention-difference counts")
    L = 10 ** 6
    spf = build_spf(L)
    pairs_gt3 = 0
    pairs_ge7 = 0
    disagree = 0
    surv = []
    from collections import Counter
    diff_break = Counter()
    for n in range(2, L + 1, 2):
        R0 = R_formula(n)
        half = n // 2
        if R0 > half or half <= 3:
            continue
        Q1 = qs_spf(n - 1, spf)
        Q2 = qs_spf(n - 2, spf)
        R1 = R_formula(n - 1)
        R2 = R_formula(n - 2)
        j = R0 * (3 // R0 + 1)
        while j <= half:
            pairs_gt3 += 1
            if j >= 7:
                pairs_ge7 += 1
            else:
                diff_break[(j, R0)] += 1
            vq = (all(j % q <= 1 for q in Q1)
                  and all(j % q <= 2 for q in Q2))
            prod2 = j * (j - 1)
            va = (prod2 % R1 == 0) and ((prod2 * (j - 2)) % R2 == 0)
            if vq != va:
                disagree += 1
            if vq:
                surv.append((n, j))
            j += R0
    slog("S3_pairs_j_gt_3", pairs_gt3)
    slog("S3_pairs_j_ge_7", pairs_ge7)
    slog("S3_difference_le_1e6", pairs_gt3 - pairs_ge7)
    slog("S3_difference_breakdown_(j,R)", dict(sorted(diff_break.items())))
    slog("S3_aggregate_vs_qform_disagreements", disagree)
    slog("S3_survivors", surv)
    assert pairs_gt3 == 6974250 and pairs_ge7 == 6974117
    assert pairs_gt3 - pairs_ge7 == 133 and disagree == 0 and not surv
    del spf
    # Random sample at larger n: seeded random even n in (10^6, 10^8].
    rng = random.Random(20261030)
    sample_pairs = 0
    sample_dis = 0
    for _ in range(3000):
        n = rng.randrange(10 ** 6 + 2, 10 ** 8 + 1, 2)
        R0 = R_formula(n)
        half = n // 2
        if R0 > half:
            continue
        Q1 = rel_qs(factor_trial(n - 1))
        Q2 = rel_qs(factor_trial(n - 2))
        R1 = R_formula(n - 1)
        R2 = R_formula(n - 2)
        j = R0 * (3 // R0 + 1)
        while j <= half:
            sample_pairs += 1
            vq = (all(j % q <= 1 for q in Q1)
                  and all(j % q <= 2 for q in Q2))
            prod2 = j * (j - 1)
            va = (prod2 % R1 == 0) and ((prod2 * (j - 2)) % R2 == 0)
            if vq != va:
                sample_dis += 1
            j += R0
    slog("S3_random_sample_pairs_(1e6,1e8]", sample_pairs)
    slog("S3_random_sample_disagreements", sample_dis)
    assert sample_dis == 0
    # Direct enumeration of the j in {4,5,6} difference in (10^6, 10^7]:
    # n > 10^6 > 2*6, so the window condition is automatic; a pair at
    # j=4 or 6 exists iff R(n)=1, at j=5 iff R(n) in {1,5}.
    diff = 0
    cntR1 = 0
    cntR5 = 0
    for n in range(10 ** 6 + 2, 10 ** 7 + 1, 2):
        r = R_formula(n)
        if r == 1:
            diff += 3
            cntR1 += 1
        elif r == 5:
            diff += 1
            cntR5 += 1
    slog("S3_difference_(1e6,1e7]_direct", diff)
    slog("S3_difference_(1e6,1e7]_R1_R5_counts", (cntR1, cntR5))
    assert diff == 27
    # Exact targeted count for (10^7, 10^8]: R(n)=1 iff odd part of n in
    # {1,3}; R(n)=5 iff odd part in {5,15} (odd part with a single
    # factor 3 stripped when v3=1). Enumerate c*2^a exactly.
    def count_c(c, lo, hi):
        k = 0
        a = 1
        while c * (1 << a) <= hi:
            if c * (1 << a) > lo:
                k += 1
            a += 1
        return k
    R1_78 = count_c(1, 10 ** 7, 10 ** 8) + count_c(3, 10 ** 7, 10 ** 8)
    R5_78 = count_c(5, 10 ** 7, 10 ** 8) + count_c(15, 10 ** 7, 10 ** 8)
    diff78 = 3 * R1_78 + R5_78
    slog("S3_difference_(1e7,1e8]_targeted", diff78)
    slog("S3_difference_(1e7,1e8]_R1_R5_counts", (R1_78, R5_78))
    assert diff78 == 25
    # Validate the targeted method on (10^6,10^7] against the direct count.
    R1_67 = count_c(1, 10 ** 6, 10 ** 7) + count_c(3, 10 ** 6, 10 ** 7)
    R5_67 = count_c(5, 10 ** 6, 10 ** 7) + count_c(15, 10 ** 6, 10 ** 7)
    slog("S3_targeted_method_on_(1e6,1e7]", (R1_67, R5_67, 3 * R1_67 + R5_67))
    assert (R1_67, R5_67) == (cntR1, cntR5)


# ------------------------------------------------- S4 K-a recount (aggregate)
def ka_block(jlo, jhi):
    cand = 0
    surv = []
    for j in range(jlo, jhi + 1):
        Nj = N_of_3(j)
        divs = []
        r = isqrt(j)
        for d in range(1, r + 1):
            if j % d == 0:
                divs.append(d)
                if d * d != j:
                    divs.append(j // d)
        prod2 = j * (j - 1)
        prod3 = prod2 * (j - 2)
        for d in divs:
            if d % 2 == 0 or v3_int(d) == 1:
                continue
            # branches: t = 2^a, and (v3(d)=0) t = 3*2^a
            starts = (1, 3) if v3_int(d) == 0 else (1,)
            for s0 in starts:
                t = s0
                while d * t <= Nj:
                    n = d * t
                    if n >= 2 * j:
                        cand += 1
                        if prod2 % R_formula(n - 1) != 0:
                            pass
                        elif prod3 % R_formula(n - 2) != 0:
                            pass
                        else:
                            surv.append((n, j))
                    t *= 2
    return cand, surv


def section_S4():
    note("S4. K-a recount (aggregate form): [5001,20000] in K1/K2 blocks "
         "+ chosen block [20001,25000]")
    blocks = [(5001, 6000, 87585), (6001, 10000, 376940),
              (10001, 15000, 518441), (15001, 20000, 553625),
              (20001, 25000, 583356)]
    total = 0
    for (lo, hi, expect) in blocks:
        c, s = ka_block(lo, hi)
        slog(f"S4_Ka_block_{lo}_{hi}", (c, len(s)))
        assert c == expect and not s, (lo, hi, c, s[:3])
        if hi <= 20000:
            total += c
    slog("S4_Ka_total_5001_20000", total)
    assert total == 1536591
    # Arithmetic reconciliation with the anchor range (341,633 pairs).
    slog("S4_reconciliation_1536591+341633", total + 341633)
    assert total + 341633 == 1878224
    slog("S4_reconciliation_K1_total_5312239+341633", 5312239 + 341633)
    assert 5312239 + 341633 == 5653872


# ------------------------------------------------- S5 K-b recount (aggregate)
def kb_block(lo, hi):
    """Even n in (lo,hi]; returns (pairs_gt3, pairs_ge7, surv_gt3)."""
    p3 = 0
    p7 = 0
    surv = []
    Rf = R_formula
    for n in range(lo + 2 if lo % 2 == 0 else lo + 1, hi + 1, 2):
        R0 = Rf(n)
        half = n // 2
        if R0 > half or half // R0 - 3 // R0 <= 0:
            continue
        R1 = Rf(n - 1)
        R2 = Rf(n - 2)
        j = R0 * (3 // R0 + 1)
        while j <= half:
            p3 += 1
            if j >= 7:
                p7 += 1
            prod2 = j * (j - 1)
            if prod2 % R1 == 0 and (prod2 * (j - 2)) % R2 == 0:
                surv.append((n, j))
            j += R0
    return p3, p7, surv


def section_S5():
    note("S5. K-b recount (aggregate form): even n <= 10^7, both "
         "conventions, by decade; plus segmented recount of (10^7,2*10^7]")
    segs = [(0, 10 ** 5, 605084, 604976),
            (10 ** 5, 10 ** 6, 6369166, 6369141),
            (10 ** 6, 10 ** 7, 75836283, 75836256)]
    t3 = 0
    t7 = 0
    for (lo, hi, e3, e7) in segs:
        p3, p7, s = kb_block(lo, hi)
        slog(f"S5_Kb_segment_({lo},{hi}]", (p3, p7, len(s)))
        assert (p3, p7) == (e3, e7) and not s, (lo, hi, p3, p7, s[:3])
        t3 += p3
        t7 += p7
    slog("S5_Kb_totals_le_1e7_(gt3,ge7)", (t3, t7))
    assert (t3, t7) == (82810533, 82810373)
    # Segmented recount of the first (10^7,10^8] sub-block.
    p3, p7, s = kb_block(10 ** 7, 2 * 10 ** 7)
    slog("S5_Kb_segment_(1e7,2e7]_(gt3,ge7,surv)", (p3, p7, len(s)))
    assert p7 == 90032870 and not s, (p3, p7, s[:3])
    # Its convention difference, targeted: R=1 count and R=5 count via
    # odd parts {1,3} / {5,15}.
    def count_c(c, lo, hi):
        k = 0
        a = 1
        while c * (1 << a) <= hi:
            if c * (1 << a) > lo:
                k += 1
            a += 1
        return k
    R1s = count_c(1, 10 ** 7, 2 * 10 ** 7) + count_c(3, 10 ** 7, 2 * 10 ** 7)
    R5s = count_c(5, 10 ** 7, 2 * 10 ** 7) + count_c(15, 10 ** 7, 2 * 10 ** 7)
    slog("S5_segment_difference_targeted", (R1s, R5s, 3 * R1s + R5s))
    assert p3 - p7 == 3 * R1s + R5s


# ------------------------------------------------------------------ S6 K-c
def is_prime_det(n):
    if n < 2:
        return False
    for p in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        if n % p == 0:
            return n == p
    d = n - 1
    s = 0
    while d % 2 == 0:
        d //= 2
        s += 1
    bases = (2, 3, 5, 7, 11, 13, 17) if n >= 4759123141 else (2, 7, 61)
    for a in bases:
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(s - 1):
            x = x * x % n
            if x == n - 1:
                break
        else:
            return False
    return True


def pollard_simple(n, rng):
    if n % 2 == 0:
        return 2
    while True:
        c = rng.randrange(1, n)
        x = rng.randrange(0, n)
        y = x
        d = 1
        while d == 1:
            x = (x * x + c) % n
            y = (y * y + c) % n
            y = (y * y + c) % n
            d = gcd(abs(x - y), n)
        if d != n:
            return d


def factor_big(n, rng):
    out = {}
    x = n
    for p in PR_1000:
        if p * p > x:
            break
        if x % p == 0:
            a = 0
            while x % p == 0:
                x //= p
                a += 1
            out[p] = a
    stack = [x] if x > 1 else []
    while stack:
        y = stack.pop()
        if y == 1:
            continue
        if is_prime_det(y):
            out[y] = out.get(y, 0) + 1
            continue
        s = isqrt(y)
        if s * s == y:
            stack += [s, s]
            continue
        d = pollard_simple(y, rng)
        stack += [d, y // d]
    prod = 1
    for p, a in out.items():
        prod *= p ** a
    assert prod == n
    return out


def section_S6():
    note("S6. K-c: family enumeration, CRT pinning recount, brute-force "
         "validation <= 50000, overlap <= 10^6")
    rng = random.Random(699)
    # Factoriser cross-check vs full trial division to 10^6.
    PR_BIG = primes_upto(10 ** 6)
    rng2 = random.Random(7)
    mism = 0
    for _ in range(150):
        v = rng2.randint(2, 10 ** 12)
        if factor_big(v, rng) != factor_trial(v, PR_BIG):
            mism += 1
    slog("S6_factoriser_crosscheck_(150_random, mismatches)", mism)
    assert mism == 0
    del PR_BIG
    # Families (sets per family, as specified).
    fam_i = set()
    for m in range(1, 1000, 2):
        a = 4
        while m * (1 << a) <= 10 ** 12:
            fam_i.add(m * (1 << a))
            a += 1
    fam_ii = {(1 << a) + 2 for a in range(3, 41)} | {(1 << a) - 2
                                                     for a in range(3, 41)}
    fam_iii = {3 ** b + 1 for b in range(2, 26)} | {3 ** b - 1
                                                    for b in range(2, 26)}
    families = [("i", sorted(fam_i)), ("ii", sorted(fam_ii)),
                ("iii", sorted(fam_iii))]
    slog("S6_family_sizes", tuple(len(v) for _, v in families))
    slog("S6_family_total_with_multiplicity",
         sum(len(v) for _, v in families))
    assert [len(v) for _, v in families] == [13931, 76, 48]

    def process(n):
        fn = factor_big(n, rng)
        f1 = factor_big(n - 1, rng)
        f2 = factor_big(n - 2, rng)
        tot = {}
        for f in (fn, f1, f2):
            for p, a in f.items():
                tot[p] = tot.get(p, 0) + a
        v3fac = {}
        for p, t in tot.items():
            if p == 2:
                continue
            e = t - (1 if p == 3 else 0)
            if e >= 1:
                v3fac[p] = e
        V = 1
        for p, e in v3fac.items():
            V *= p ** e
        R0 = 1
        for q in rel_qs(fn):
            R0 *= q
        # Pins: (modulus, allowed residues), R(n)|j folded in as
        # residue 0 at prime powers of n itself.
        pins = []
        for p, e in v3fac.items():
            if p == 3:
                q = 3 ** (e + 1)
                allowed = (0,) if fn.get(3, 0) >= 2 else (0, 1, 2)
            else:
                q = p ** e
                allowed = (0,) if p in fn else (0, 1, 2)
            pins.append((q, allowed))
        raw = 1
        for _, al in pins:
            raw *= len(al)
        limit = n // 2
        pins.sort(key=lambda t: -t[0])
        classes = [(0, 1)]
        for q, allowed in pins:
            new = []
            for r, m in classes:
                inv = pow(m, -1, q)
                for s in allowed:
                    x = r + m * (((s - r) * inv) % q)
                    nm = m * q
                    first = x if x > 3 else x + nm * ((4 - x + nm - 1) // nm)
                    if first <= limit:
                        new.append((x, nm))
            classes = new
            if not classes:
                break
        cands = []
        for x, nm in classes:
            j = x if x > 3 else x + nm * ((4 - x + nm - 1) // nm)
            while j <= limit:
                cands.append(j)
                j += nm
        cands = [j for j in cands if j % R0 == 0]
        q1 = rel_qs(f1)
        q2 = rel_qs(f2)
        surv = []
        for j in cands:
            assert comb(j, 3) % V == 0, (n, j)
            if (all(j % q <= 1 for q in q1)
                    and all(j % q <= 2 for q in q2)):
                surv.append(j)
        return {"V": V, "R0": R0, "raw": raw, "cands": cands,
                "surv": surv, "fn": fn, "f1": f1, "f2": f2,
                "v3fac": v3fac}

    all_cands = []
    max_raw = (0, None)
    combo_tot = {}
    surv_tot = []
    cache = {}
    for name, vals in families:
        ct = 0
        combo_tot[name] = 0
        for n in vals:
            res = process(n)
            cache[n] = res
            combo_tot[name] += res["raw"]
            ct += len(res["cands"])
            for j in res["cands"]:
                all_cands.append((name, n, j))
            surv_tot += [(n, j) for j in res["surv"]]
            if res["raw"] > max_raw[0]:
                max_raw = (res["raw"], n)
        slog(f"S6_family_{name}_candidates", ct)
    slog("S6_CRT_combo_totals_by_family", combo_tot)
    slog("S6_all_candidates", all_cands)
    slog("S6_max_raw_combos_(count,n)", max_raw)
    slog("S6_survivors", surv_tot)
    assert all_cands == [("i", 16, 7)], all_cands
    assert max_raw == (531441, 68719476736), max_raw
    assert not surv_tot
    # The unique candidate's (LD3) failure, stated exactly.
    res16 = cache[16]
    q1_16 = rel_qs(res16["f1"])
    slog("S6_candidate_(16,7)_relevant_qs_of_15", q1_16)
    slog("S6_candidate_(16,7)_failure", (1, 5, 7 % 5))
    assert 7 % 5 == 2 > 1 and 5 in q1_16
    assert comb(7, 3) % res16["V"] == 0  # (N2) holds: V3(16)=35=C(7,3)
    # Brute-force validation of pinning on family members <= 50000.
    small = sorted({n for _, vals in families for n in vals if n <= 50000})
    mism = 0
    brute_tot = 0
    for n in small:
        res = cache[n]
        V = res["V"]
        R0 = res["R0"]
        brute = []
        j = ((4 + R0 - 1) // R0) * R0
        while j <= n // 2:
            if comb(j, 3) % V == 0:
                brute.append(j)
            j += R0
        brute_tot += len(brute)
        if brute != res["cands"]:
            mism += 1
    slog("S6_pinning_validation_members_le_50000", len(small))
    slog("S6_pinning_validation_brute_candidates", brute_tot)
    slog("S6_pinning_validation_mismatches", mism)
    assert len(small) == 1820 and mism == 0 and brute_tot == 1
    # Overlap check: distinct family members <= 10^6, direct (LD3).
    ov = sorted({n for _, vals in families for n in vals if n <= 10 ** 6})
    pairs = 0
    osurv = []
    for n in ov:
        res = cache[n]
        R0 = res["R0"]
        q1 = rel_qs(res["f1"])
        q2 = rel_qs(res["f2"])
        j = ((4 + R0 - 1) // R0) * R0
        while j <= n // 2:
            pairs += 1
            if (all(j % q <= 1 for q in q1)
                    and all(j % q <= 2 for q in q2)):
                osurv.append((n, j))
            j += R0
    slog("S6_overlap_members_le_1e6", len(ov))
    slog("S6_overlap_pairs", pairs)
    slog("S6_overlap_survivors", osurv)
    assert len(ov) == 4029 and pairs == 4088173 and not osurv


SECTIONS = [("S0", section_S0), ("S1", section_S1), ("S2", section_S2),
            ("S3", section_S3), ("S4", section_S4), ("S5", section_S5),
            ("S6", section_S6)]


def main():
    wanted = sys.argv[1:]
    for name, fn in SECTIONS:
        if wanted and name not in wanted:
            continue
        fn()
    note("V-K SUMMARY")
    for label, value in SUMMARY:
        print(f"{label} = {value}")
    print(f"total_wall_seconds = {time.time() - T0:.1f}")


if __name__ == "__main__":
    main()
