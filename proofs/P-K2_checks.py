#!/usr/bin/env python3
"""P-K2 checks: Erdős #699, Cycle 3, Cluster K (Computer K2, independent).

i = 3 frontier extension.  Python standard library only, exact integer
arithmetic, single-threaded.  Runnable end-to-end:

    python3 P-K2_checks.py            # all sections
    python3 P-K2_checks.py S2         # a single section (development aid)

Definitions (exact, as specified for Cluster K).
    V3(n) = C(n,3) / 2^{v2(C(n,3))}             (the odd part of C(n,3))
    R(m)  = product of the relevant prime powers q = p^a || m
            (p >= 5, any a >= 1;  p = 3 with a >= 2)
    (LD3)   pair (n, j), 3 < j <= n/2, satisfies (LD3) iff for every
            r in {0,1,2} and every relevant q = p^a || (n-r):
            j mod q <= r.
    (N2)    V3(n) | C(j,3).
    N(3,j) = max{ n : C(n,3) < C(2j,6) }        (finite-reduction bound)

Two exact reformulations used below (proved in P-K2.md, and validated
pair-by-pair against the factorisation form in section S3):

  (R-formula)  R(m) equals the odd part of m, except that a factor 3
               is removed when v3(m) = 1 exactly.  Reason: the odd
               part of m is the product of p^{v_p(m)} over all odd p;
               the relevant primes are exactly p >= 5 (all exponents)
               and p = 3 with exponent >= 2.

  (Aggregate (LD3))  For an odd prime power q, q | j(j-1) implies q
               divides exactly one of j, j-1 (they are coprime), and
               q | j(j-1)(j-2) implies q divides exactly one of
               j, j-1, j-2 (at most one of the three is divisible by
               any odd prime p, since they differ by <= 2 < p for
               p >= 5, and exactly one is divisible by 3).  Hence,
               with Rr = R(n-r), the r = 1 clause of (LD3) is
               equivalent to R1 | j(j-1), and the r = 2 clause is
               equivalent to R2 | j(j-1)(j-2).  The r = 0 clause is
               R(n) | j.

Factorisation.
  factor_trial: plain trial division by sieved primes (used where the
     bound is small, and as an independent cross-check in S5 up to
     sqrt(m) <= 1,048,578 for the largest K-c top, m = 2^40 + 1).
  factor_fast: trial division by the primes <= 100, then deterministic
     Miller-Rabin (bases (2,7,61), deterministic for n < 4,759,123,141;
     bases (2,3,5,7,11,13,17), deterministic for
     n < 341,550,071,728,321) and deterministic-parameter Brent
     Pollard-Rho recursion.  Every cofactor > 1 is classified prime
     or split recursively until the full factorisation is obtained;
     the script asserts that the product of p^a reconstructs m.
     No cofactor is left unexamined.
"""
import math
import os
import sys
import time
from array import array
from math import comb, gcd, isqrt

T_START = time.time()
SUMMARY = []          # lines for the final summary block, in order
STATE = {}            # cross-section results


def note(msg):
    print(f"[{time.time() - T_START:8.1f}s] {msg}", flush=True)


def out(msg):
    print(msg, flush=True)


def record(line):
    SUMMARY.append(line)


# ------------------------------------------------------------------ primes
def primes_upto(limit):
    """Sieve of Eratosthenes, bytearray slice assignment."""
    if limit < 2:
        return []
    s = bytearray(b"\x01") * (limit + 1)
    s[0:2] = b"\x00\x00"
    for i in range(2, isqrt(limit) + 1):
        if s[i]:
            s[i * i:limit + 1:i] = b"\x00" * (((limit - i * i) // i) + 1)
    return [i for i, v in enumerate(s) if v]


SMALL_PRIMES = primes_upto(100)          # 25 primes, trial stage of factor_fast
TRIAL_PRIMES_KA = primes_upto(50000)     # covers sqrt of any K-a top (< 2.1e9)


# ------------------------------------------------------------- factorisation
def factor_trial(m, primes):
    """Exact factorisation {p: a} of m >= 1 by trial division.
    `primes` must contain every prime <= sqrt(m)."""
    out_d = {}
    x = m
    for p in primes:
        if p * p > x:
            break
        if x % p == 0:
            a = 0
            while x % p == 0:
                x //= p
                a += 1
            out_d[p] = a
        if x == 1:
            break
    if x > 1:
        out_d[x] = out_d.get(x, 0) + 1
    return out_d


def is_prime_det(n):
    """Deterministic Miller-Rabin for n < 341,550,071,728,321."""
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
    if n < 4759123141:
        bases = (2, 7, 61)
    else:
        bases = (2, 3, 5, 7, 11, 13, 17)
    for a in bases:
        a %= n
        if a == 0:
            continue
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(s - 1):
            x = (x * x) % n
            if x == n - 1:
                break
        else:
            return False
    return True


def pollard_brent(n):
    """Return a nontrivial divisor of composite odd n.
    Deterministic parameter sequence c = 1, 2, 3, ... (Brent's variant)."""
    if n % 2 == 0:
        return 2
    if n % 3 == 0:
        return 3
    for c in range(1, 10000):
        y = 2
        r = 1
        g = 1
        ys = 2
        while g == 1:
            x = y
            for _ in range(r):
                y = (y * y + c) % n
            k = 0
            q = 1
            while k < r and g == 1:
                ys = y
                for _ in range(min(64, r - k)):
                    y = (y * y + c) % n
                    q = q * abs(x - y) % n
                g = gcd(q, n)
                k += 64
            r *= 2
            if r > (1 << 24):
                break
        if g == n:
            # re-walk the last block one step at a time
            g = 1
            y = ys
            while g == 1:
                y = (y * y + c) % n
                g = gcd(abs(x - y), n)
            if g == n:
                continue
        if 1 < g < n:
            return g
    raise ValueError(f"pollard_brent failed on {n}")


def factor_fast(m):
    """Exact factorisation {p: a} of m >= 1: trial by primes <= 100,
    then deterministic Miller-Rabin / Pollard-Rho recursion.  Asserts
    reconstruction, so no cofactor is ever left unexamined."""
    if m == 1:
        return {}
    out_d = {}
    x = m
    for p in SMALL_PRIMES:
        if p * p > x:
            break
        if x % p == 0:
            a = 0
            while x % p == 0:
                x //= p
                a += 1
            out_d[p] = a
        if x == 1:
            break
    if x > 1:
        # x has no prime factor <= 100 unless the loop broke on p*p > x,
        # in which case x is prime; the stack machinery handles both.
        stack = [x]
        while stack:
            y = stack.pop()
            if y == 1:
                continue
            if is_prime_det(y):
                out_d[y] = out_d.get(y, 0) + 1
                continue
            d = pollard_brent(y)
            stack.append(d)
            stack.append(y // d)
    prod = 1
    for p, a in out_d.items():
        prod *= p ** a
    assert prod == m, (m, out_d)
    return out_d


def factor_spf(m, spf):
    """Exact factorisation {p: a} of 1 <= m <= len(spf)-1 via an SPF table."""
    out_d = {}
    x = m
    while x > 1:
        p = spf[x]
        a = 0
        while x % p == 0:
            x //= p
            a += 1
        out_d[p] = a
    return out_d


def relevant_qs(fdict):
    """Relevant prime powers p^a of a factorisation dict, largest first."""
    qs = [p ** a for p, a in fdict.items()
          if p >= 5 or (p == 3 and a >= 2)]
    qs.sort(reverse=True)
    return tuple(qs)


def product_of(qs):
    r = 1
    for q in qs:
        r *= q
    return r


def R_value(m):
    """R(m) by the R-formula (odd part, removing 3 iff v3(m) = 1).  m >= 1."""
    lb = m & -m
    odd = m >> (lb.bit_length() - 1)
    if odd % 3 == 0 and odd % 9 != 0:
        odd //= 3
    return odd


def V3_value(n):
    """V3(n) = odd part of C(n,3), from exact factorisations of the tops."""
    prod = {}
    for m in (n, n - 1, n - 2):
        for p, a in factor_fast(m).items():
            prod[p] = prod.get(p, 0) + a
    v = 1
    for p, a in prod.items():
        if p == 2:
            continue
        e = a - (1 if p == 3 else 0)
        if e >= 1:
            v *= p ** e
    return v


def ld3_q_form(j, Q1, Q2):
    """The r = 1, 2 clauses of (LD3) in factorisation (per-q) form.
    The r = 0 clause is enforced by candidate generation (R(n) | j)."""
    for q in Q1:
        if j % q > 1:
            return False
    for q in Q2:
        if j % q > 2:
            return False
    return True


def N_of_3(j):
    """N(3,j) = max{ n : C(n,3) < C(2j,6) }, exact binary search."""
    target = comb(2 * j, 6)
    lo, hi = 3, 6
    while comb(hi, 3) < target:
        hi *= 2
    while lo + 1 < hi:
        mid = (lo + hi) // 2
        if comb(mid, 3) < target:
            lo = mid
        else:
            hi = mid
    return lo


def first_multiple_gt(step, bound):
    """Smallest multiple of `step` that is > bound."""
    return step * (bound // step + 1)


# ============================================================ S0: N(3,j) spots
def section_S0():
    note("S0. N(3,j) spot values (anchor C)")
    expect = {7: 27, 100: 7908, 158: 19926, 159: 20181,
              500: 201728, 1000: 808934, 2000: 3239787, 5000: 20263871}
    got = {}
    for j, want in expect.items():
        got[j] = N_of_3(j)
        assert got[j] == want, (j, got[j], want)
        out(f"   N(3,{j}) = {got[j]}")
    record("S0 N(3,j) spot values: " +
           ", ".join(f"N(3,{j})={got[j]}" for j in
                     (7, 100, 158, 159, 500, 1000)) +
           f"; also N(3,2000)={got[2000]}, N(3,5000)={got[5000]}")


# ============================================ S1: brute-force cross-check j<=60
def section_S1():
    note("S1. Anchor A second method: brute force over all n in "
         "[2j, N(3,j)], 5 <= j <= 60 (no candidate generation)")
    triples = 0
    survivors = []
    for j in range(5, 61):
        Nj = N_of_3(j)
        for n in range(2 * j, Nj + 1):
            triples += 1
            Q0 = relevant_qs(factor_trial(n, TRIAL_PRIMES_KA))
            if any(j % q != 0 for q in Q0):
                continue
            Q1 = relevant_qs(factor_trial(n - 1, TRIAL_PRIMES_KA))
            Q2 = relevant_qs(factor_trial(n - 2, TRIAL_PRIMES_KA))
            if ld3_q_form(j, Q1, Q2):
                survivors.append((n, j))
    out(f"   brute-force triples examined = {triples}; survivors = {survivors}")
    assert not survivors
    record(f"S1 brute force 5<=j<=60: {triples} triples examined, "
           f"0 survivors")


# ============================================================ S2: Cluster K-a
def gen_candidates(j_hi, n_max, known):
    """All n <= n_max with R(n) <= j_hi, as a dict n -> R(n), adding to
    `known`.  Generation: n = d * 2^a (any d odd with v3(d) != 1) or
    n = d * 3 * 2^a (only v3(d) = 0); in both branches R(n) = d exactly
    (see P-K2.md).  Returns the dict of newly added n."""
    new = {}
    for d in range(1, j_hi + 1, 2):
        x = d
        v3 = 0
        while x % 3 == 0:
            x //= 3
            v3 += 1
        if v3 == 1:
            continue
        t = 1
        while d * t <= n_max:
            n = d * t
            if n not in known and n not in new:
                new[n] = d
            if v3 == 0:
                n3 = 3 * d * t
                if n3 <= n_max and n3 not in known and n3 not in new:
                    new[n3] = d
            t *= 2
    return new


def vf_style_candidate_count(j_hi, n_max):
    """Candidate count under V-F's published generation (V-F_checks.py
    section D / V-F_chunkD.py): the x3 branch there is added without
    the n <= n_max bound, so the set also contains values in
    (n_max, 3*n_max].  Used only to explain the candidate-count
    difference at the anchor; not used for any clause test."""
    cand = set()
    for d in range(1, j_hi + 1, 2):
        x = d
        v3 = 0
        while x % 3 == 0:
            x //= 3
            v3 += 1
        if v3 == 1:
            continue
        t = 1
        while d * t <= n_max:
            cand.add(d * t)
            if v3 == 0:
                cand.add(3 * d * t)
            t *= 2
    return len(cand)


def section_S2():
    note("S2. K-a: per-pair (LD3) frontier, cumulative candidate sweep")
    # Blocks: anchor segment [5,5000]; pilot [5001,6000]; then blocks to
    # the mandated 20000; extension blocks of 5000 to at most 50000.
    blocks = [(5, 5000, "anchor-A"),
              (5001, 6000, "pilot"),
              (6001, 10000, "block"),
              (10001, 15000, "block"),
              (15001, 20000, "block"),
              (20001, 25000, "ext"),
              (25001, 30000, "ext"),
              (30001, 35000, "ext"),
              (35001, 40000, "ext"),
              (40001, 45000, "ext"),
              (45001, 50000, "ext")]
    cand = {}          # n -> (R(n), Q1, Q2); Q1/Q2 from exact factorisation
    total_pairs = 0
    total_survivors = []
    pilot_time = None
    pilot_pairs = None
    decided_limit = None
    for (j_lo, j_hi, kind) in blocks:
        if kind == "ext" and decided_limit is not None and j_hi > decided_limit:
            out(f"   [block {j_lo}-{j_hi} skipped: decided limit "
                f"{decided_limit}]")
            continue
        t_block = time.time()
        Nj = {j: N_of_3(j) for j in range(j_lo, j_hi + 1)}
        n_max = Nj[j_hi]
        new = gen_candidates(j_hi, n_max, cand)
        for n in sorted(new):
            d = new[n]
            if n < 10:
                # Counted as candidates (as in V-F's generation) but no
                # pair with j >= 5 can involve them (2j <= n fails);
                # tops n-1, n-2 are not all positive, so no clause test
                # is ever performed for these n.
                assert R_value(n) == d, (n, d)
                cand[n] = (d, (), ())
                continue
            Rn_chk = product_of(relevant_qs(factor_fast(n)))
            assert Rn_chk == d == R_value(n), (n, Rn_chk, d)
            Q1 = relevant_qs(factor_fast(n - 1))
            Q2 = relevant_qs(factor_fast(n - 2))
            cand[n] = (d, Q1, Q2)
        pairs = 0
        survivors = []
        for n, (Rn, Q1, Q2) in cand.items():
            j = first_multiple_gt(Rn, j_lo - 1)
            if j < j_lo:
                j += Rn
            while j <= j_hi:
                if 2 * j <= n <= Nj[j]:
                    pairs += 1
                    if ld3_q_form(j, Q1, Q2):
                        survivors.append((n, j))
                j += Rn
        wall = time.time() - t_block
        total_pairs += pairs
        total_survivors.extend(survivors)
        out(f"   block j in [{j_lo},{j_hi}] ({kind}): cumulative candidates "
            f"= {len(cand)}, new candidates = {len(new)}, pairs clause-tested "
            f"= {pairs}, survivors = {survivors}, N(3,{j_hi}) = {n_max}, "
            f"wall = {wall:.1f}s")
        if kind == "anchor-A":
            assert pairs == 341633, pairs
            assert not survivors
            vf_count = vf_style_candidate_count(5000, n_max)
            assert vf_count == 50489, vf_count
            out(f"   anchor A candidate counts: bounded generation used "
                f"here = {len(cand)} (all n<=N(3,5000)); V-F published "
                f"generation = {vf_count} (its x3 branch is unbounded; "
                f"the {vf_count - len(cand)} extra values lie in "
                f"(N(3,5000), 3*N(3,5000)] and form no pair in range); "
                f"pairs clause-tested agree exactly: 341633, 0 survivors")
            record(f"S2 anchor A (5<=j<=5000): 341633 pairs clause-tested "
                   f"(n<=N(3,j) filter), 0 survivors; candidate n: "
                   f"{len(cand)} by the bounded generation used here, "
                   f"50489 under V-F's published generation (difference "
                   f"2766, all in (N(3,5000), 3*N(3,5000)], forming no "
                   f"pair in range); zero survivors also by S1 brute "
                   f"force")
        if kind == "pilot":
            pilot_time = wall
            pilot_pairs = pairs
            record(f"S2 pilot block 5001-6000: {pairs} pairs clause-tested, "
                   f"0 survivors, wall {wall:.1f}s, "
                   f"cumulative candidates {len(cand)}")
            # Extrapolation rule, stated here BEFORE any extension block
            # runs: a 5000-wide block ending at J is projected at
            #     pilot_wall * (5000/1000) * (J / 5500)   seconds
            # (linear growth of per-j cost in j).  Extension proceeds in
            # 5000-blocks while every projected block is <= 1800 s, up
            # to the cap 50000; the mandated range to 20000 is always
            # completed regardless.
            projections = {}
            for J in range(25000, 50001, 5000):
                projections[J] = pilot_time * 5.0 * (J / 5500.0)
            limit = 20000
            for J in range(25000, 50001, 5000):
                if projections[J] <= 1800.0:
                    limit = J
                else:
                    break
            decided_limit = limit
            out(f"   pilot extrapolation: projected 5000-block walls "
                f"(seconds) = " +
                ", ".join(f"{J}:{projections[J]:.0f}" for J in projections) +
                f"; decided extension limit = {decided_limit}")
            record(f"S2 extrapolation from pilot: projected block walls "
                   f"(s) " + ", ".join(f"to {J}: {projections[J]:.0f}"
                                       for J in projections) +
                   f"; decided limit {decided_limit}")
        elif kind in ("block", "ext"):
            record(f"S2 block {j_lo}-{j_hi}: {pairs} pairs clause-tested, "
                   f"survivors {len(survivors)}, wall {wall:.1f}s, "
                   f"N(3,{j_hi})={n_max}, cumulative candidates {len(cand)}")
    out(f"   K-a total: pairs clause-tested = {total_pairs}, "
        f"survivors = {total_survivors}")
    assert not total_survivors
    final_j = decided_limit if decided_limit is not None else 20000
    STATE["Ka_final_j"] = final_j
    STATE["Ka_total_pairs"] = total_pairs
    record(f"S2 K-a total (5<=j<={final_j}): {total_pairs} pairs "
           f"clause-tested, 0 survivors; (LD3) has no solution with "
           f"2j<=n<=N(3,j) for any 5<=j<={final_j}")


# ============================================================ S3: Cluster K-b
def build_spf(L):
    """SPF table for [0, L] as array('i'), by descending prime slice
    assignment (C-level).  Only primes are assigned; each composite is
    overwritten by its smallest prime factor last."""
    spf = array("i", range(L + 1))
    for p in reversed(primes_upto(isqrt(L))):
        cnt = L // p
        spf[p::p] = array("i", [p]) * cnt
    spf[0] = 0
    if L >= 1:
        spf[1] = 1
    return spf


def section_S3():
    note("S3. K-b anchor: full (LD3), even n <= 10^6, factorisation form "
         "(SPF), with pair-by-pair validation of the aggregate form")
    t_sec = time.time()
    L = 10 ** 6
    spf = build_spf(L)
    # SPF sanity vs trial division on a deterministic sample
    for m in range(2, 2000):
        assert factor_spf(m, spf) == factor_trial(m, TRIAL_PRIMES_KA), m
    pairs_gt3 = 0
    pairs_ge7 = 0
    block_counts = {}      # (label) -> [pairs_gt3, pairs_ge7]
    survivors = []
    equiv_checks = 0
    n_with = 0
    for n in range(2, L + 1, 2):
        Q0 = relevant_qs(factor_spf(n, spf))
        R0 = product_of(Q0)
        assert R0 == R_value(n)
        half = n // 2
        if R0 > half:
            continue
        cnt = half // R0 - 3 // R0
        if cnt <= 0:
            continue
        Q1 = relevant_qs(factor_spf(n - 1, spf))
        Q2 = relevant_qs(factor_spf(n - 2, spf))
        R1 = product_of(Q1)
        R2 = product_of(Q2)
        assert R1 == R_value(n - 1) and R2 == R_value(n - 2)
        n_with += 1
        label = "n<=10^5" if n <= 10 ** 5 else "10^5<n<=10^6"
        bc = block_counts.setdefault(label, [0, 0])
        j = first_multiple_gt(R0, 3)
        while j <= half:
            pairs_gt3 += 1
            bc[0] += 1
            if j >= 7:
                pairs_ge7 += 1
                bc[1] += 1
            v_q = ld3_q_form(j, Q1, Q2)
            prod2 = j * (j - 1)
            v_agg = (prod2 % R1 == 0) and ((prod2 * (j - 2)) % R2 == 0)
            assert v_q == v_agg, (n, j, v_q, v_agg)
            equiv_checks += 1
            if v_q:
                survivors.append((n, j))
            j += R0
    wall = time.time() - t_sec
    out(f"   even n<=10^6: n with candidates = {n_with}, pairs (j>3) = "
        f"{pairs_gt3}, pairs (j>=7) = {pairs_ge7}, survivors = {survivors}, "
        f"aggregate-equivalence checks = {equiv_checks}, wall = {wall:.1f}s")
    for label in ("n<=10^5", "10^5<n<=10^6"):
        out(f"   block {label}: pairs (j>3) = {block_counts[label][0]}, "
            f"pairs (j>=7) = {block_counts[label][1]}, survivors = 0")
    assert pairs_ge7 == 6974117, pairs_ge7
    assert pairs_gt3 == 6974250, pairs_gt3
    assert not survivors
    STATE["Kb_anchor_block_counts"] = block_counts
    STATE["Kb_anchor_survivors"] = survivors
    record(f"S3 anchor B (even n<=10^6, factorisation form): "
           f"6974117 pairs with j>=7 (the F2.21 convention), "
           f"6974250 pairs with j>3 (the K-b specification window), "
           f"difference 133 pairs at j in {{4,5,6}}, 0 survivors either way")
    record(f"S3 block n<=10^5: pairs (j>3) = {block_counts['n<=10^5'][0]}, "
           f"pairs (j>=7) = {block_counts['n<=10^5'][1]}, 0 survivors; "
           f"block 10^5<n<=10^6: pairs (j>3) = "
           f"{block_counts['10^5<n<=10^6'][0]}, pairs (j>=7) = "
           f"{block_counts['10^5<n<=10^6'][1]}, 0 survivors")
    record(f"S3 aggregate (LD3) form agrees with the factorisation form on "
           f"all {equiv_checks} candidate pairs with even n<=10^6")


# ======================================= S4: K-b extension to 10^7 (aggregate)
def kb_aggregate_block(n_lo, n_hi):
    """Full (LD3) survivor search over even n in [n_lo, n_hi] using the
    aggregate form (validated in S3).  Returns (pairs_gt3, pairs_ge7,
    survivors, wall).  Memory O(1): no sieve is kept; R(m) is computed
    by the R-formula."""
    t_block = time.time()
    pairs_gt3 = 0
    pairs_ge7 = 0
    survivors = []
    for n in range(n_lo if n_lo % 2 == 0 else n_lo + 1, n_hi + 1, 2):
        lb = n & -n
        odd0 = n >> (lb.bit_length() - 1)
        R0 = odd0 // 3 if (odd0 % 3 == 0 and odd0 % 9 != 0) else odd0
        half = n // 2
        if R0 > half:
            continue
        if half // R0 - 3 // R0 <= 0:
            continue
        m1 = n - 1
        R1 = m1 // 3 if (m1 % 3 == 0 and m1 % 9 != 0) else m1
        m2 = n - 2
        lb2 = m2 & -m2
        odd2 = m2 >> (lb2.bit_length() - 1)
        R2 = odd2 // 3 if (odd2 % 3 == 0 and odd2 % 9 != 0) else odd2
        j = R0 * (3 // R0 + 1)
        while j <= half:
            pairs_gt3 += 1
            if j >= 7:
                pairs_ge7 += 1
            prod2 = j * (j - 1)
            if prod2 % R1 == 0 and (prod2 * (j - 2)) % R2 == 0:
                survivors.append((n, j))
            j += R0
    return pairs_gt3, pairs_ge7, survivors, time.time() - t_block


def section_S4():
    note("S4. K-b extension: full (LD3), even n <= 10^7, aggregate form")
    t_sec = time.time()
    results = {}
    for (label, lo, hi) in [("n<=10^5", 2, 10 ** 5),
                            ("10^5<n<=10^6", 10 ** 5 + 1, 10 ** 6),
                            ("10^6<n<=10^7", 10 ** 6 + 1, 10 ** 7)]:
        p3, p7, surv, wall = kb_aggregate_block(lo, hi)
        results[label] = (p3, p7, surv, wall)
        out(f"   block {label}: pairs (j>3) = {p3}, pairs (j>=7) = {p7}, "
            f"survivors = {surv}, wall = {wall:.1f}s")
        assert not surv
        record(f"S4 block {label}: pairs (j>3) = {p3}, pairs (j>=7) = {p7}, "
               f"0 survivors, wall {wall:.1f}s")
    # Consistency with the S3 factorisation-form anchor on its range
    anchor = STATE["Kb_anchor_block_counts"]
    assert results["n<=10^5"][0] == anchor["n<=10^5"][0]
    assert results["n<=10^5"][1] == anchor["n<=10^5"][1]
    assert results["10^5<n<=10^6"][0] == anchor["10^5<n<=10^6"][0]
    assert results["10^5<n<=10^6"][1] == anchor["10^5<n<=10^6"][1]
    tot3 = sum(v[0] for v in results.values())
    tot7 = sum(v[1] for v in results.values())
    wall_total = time.time() - t_sec
    out(f"   even n<=10^7 totals: pairs (j>3) = {tot3}, pairs (j>=7) = "
        f"{tot7}, survivors = 0, wall = {wall_total:.1f}s")
    record(f"S4 K-b total (even n<=10^7): {tot3} pairs (j>3), {tot7} pairs "
           f"(j>=7), 0 survivors; aggregate counts on n<=10^6 agree exactly "
           f"with the S3 factorisation-form anchor")
    # Extension decision for 10^8, rule stated before any 10^8 work:
    # decade growth of pair counts and of block wall is measured on the
    # two completed decade blocks; the (10^7, 10^8] block is projected
    # at the larger of the pair-growth and the plain x10 n-growth
    # applied to the last block's wall.  Proceed only if the whole S4
    # run to 10^7 took <= 1800 s, the design memory is <= 2 GB (the
    # aggregate design keeps O(1) state beyond counters), AND the
    # projected block wall is <= 2700 s.
    last_wall = results["10^6<n<=10^7"][3]
    pair_growth = results["10^6<n<=10^7"][0] / max(1, results["10^5<n<=10^6"][0])
    projected = last_wall * max(pair_growth, 10.0)
    proceed = (wall_total <= 1800.0) and (projected <= 2700.0)
    out(f"   10^8 decision: S4 wall to 10^7 = {wall_total:.1f}s, last "
        f"decade pair growth x{pair_growth:.2f}, projected (10^7,10^8] "
        f"wall = {projected:.0f}s, memory design O(1) state; proceed = "
        f"{proceed}")
    record(f"S4 10^8 decision: wall to 10^7 = {wall_total:.1f}s, last "
           f"decade pair growth x{pair_growth:.2f}, projected "
           f"(10^7,10^8] wall = {projected:.0f}s, O(1)-state memory "
           f"design, proceed = {proceed}")
    STATE["Kb_1e8_proceed"] = proceed
    STATE["Kb_1e8_projected"] = projected
    if proceed:
        p3, p7, surv, wall = kb_aggregate_block(10 ** 7 + 1, 10 ** 8)
        out(f"   block 10^7<n<=10^8: pairs (j>3) = {p3}, pairs (j>=7) = "
            f"{p7}, survivors = {surv}, wall = {wall:.1f}s")
        assert not surv
        record(f"S4 block 10^7<n<=10^8: pairs (j>3) = {p3}, pairs (j>=7) "
               f"= {p7}, 0 survivors, wall {wall:.1f}s")
        record(f"S4 K-b grand total (even n<=10^8): {tot3 + p3} pairs "
               f"(j>3), {tot7 + p7} pairs (j>=7), 0 survivors")
        STATE["Kb_final_limit"] = 10 ** 8
        STATE["Kb_total_pairs_gt3"] = tot3 + p3
    else:
        record(f"S4 10^8 extension NOT run: rule above gives projected "
               f"wall {projected:.0f}s (S4 wall to 10^7 {wall_total:.1f}s); "
               f"search stops at 10^7")
        STATE["Kb_final_limit"] = 10 ** 7
        STATE["Kb_total_pairs_gt3"] = tot3


# ============================================================ S5: Cluster K-c
def kc_process_n(n):
    """(LD3)+(N2) candidate generation for one K-c n by CRT pinning.
    Returns a result dict; survivors carry full factorisation data."""
    f0 = factor_fast(n)
    f1 = factor_fast(n - 1)
    f2 = factor_fast(n - 2)
    Q0 = relevant_qs(f0)
    Q1 = relevant_qs(f1)
    Q2 = relevant_qs(f2)
    R = product_of(Q0)
    assert R == R_value(n)
    # V3(n) from the tops' factorisations; cross-checked against the
    # direct definition (odd part of C(n,3)) for every n.
    totals = {}
    for f in (f0, f1, f2):
        for p, a in f.items():
            totals[p] = totals.get(p, 0) + a
    v3fac = {}
    for p, tot in totals.items():
        if p == 2:
            continue
        e = tot - (1 if p == 3 else 0)
        if e >= 1:
            v3fac[p] = e
    V3 = 1
    for p, e in v3fac.items():
        V3 *= p ** e
    Cn3 = n * (n - 1) * (n - 2) // 6
    assert V3 == Cn3 // (Cn3 & -Cn3), (n, V3)
    # CRT pinning
    pins = []
    for p, e in sorted(v3fac.items()):
        if p == 3:
            continue
        q = p ** e
        pins.append((q, (0,) if p in f0 else (0, 1, 2)))
    e3 = v3fac.get(3, 0)
    if e3 >= 1:
        q3 = 3 ** (e3 + 1)
        pins.append((q3, (0,) if f0.get(3, 0) >= 2 else (0, 1, 2)))
    combos = 1
    for _, opts in pins:
        combos *= len(opts)
    candidates = []
    fallback = False
    fallback_multiples = 0
    if combos > 10 ** 6:
        # Spec fallback: direct (LD3)-first enumeration over the
        # multiples of R(n) in the (N2)-size window C(j,3) >= V3(n).
        fallback = True
        half = n // 2
        if comb(half, 3) >= V3:
            lo, hi = 4, half
            while lo < hi:
                mid = (lo + hi) // 2
                if comb(mid, 3) >= V3:
                    hi = mid
                else:
                    lo = mid + 1
            jmin = lo
            j = first_multiple_gt(R, jmin - 1)
            while j <= half:
                fallback_multiples += 1
                if comb(j, 3) % V3 == 0:
                    candidates.append(j)
                j += R
    else:
        residues = [0]
        Mpin = 1
        for q, opts in pins:
            inv = pow(Mpin, -1, q)
            new_res = []
            for r in residues:
                for s in opts:
                    t = ((s - r) * inv) % q
                    new_res.append(r + Mpin * t)
            residues = new_res
            Mpin *= q
        assert Mpin == (3 * V3 if e3 >= 1 else V3), (n, Mpin, V3)
        assert len(residues) == combos
        half = n // 2
        for r in residues:
            j = r
            while j <= 3:
                j += Mpin
            while j <= half:
                candidates.append(j)
                j += Mpin
    survivors = []
    cand_le = 0
    cand_details = []
    for j in candidates:
        assert j % R == 0
        assert comb(j, 3) % V3 == 0
        if j <= 5000:
            cand_le += 1
        if all(j % q == 0 for q in Q0) and ld3_q_form(j, Q1, Q2):
            survivors.append({"n": n, "j": j, "factor_n": dict(f0),
                              "factor_n-1": dict(f1),
                              "factor_n-2": dict(f2), "V3": V3, "R": R})
            cand_details.append((j, None))
        else:
            viol = None
            for r, Q in ((0, Q0), (1, Q1), (2, Q2)):
                for q in Q:
                    if j % q > r:
                        viol = (r, q, j % q)
                        break
                if viol is not None:
                    break
            cand_details.append((j, viol))
    return {"n": n, "combos": combos, "fallback": fallback,
            "fallback_multiples": fallback_multiples,
            "candidates": len(candidates), "cand_le5000": cand_le,
            "cand_gt5000": len(candidates) - cand_le,
            "cand_details": cand_details,
            "survivors": survivors}


def section_S5():
    note("S5. K-c: targeted high-v2 families, (LD3)+(N2) by CRT pinning")
    t_sec = time.time()
    fam_i = []
    for m in range(1, 1000, 2):
        a = 4
        n = m << a
        while n <= 10 ** 12:
            fam_i.append(n)
            a += 1
            n = m << a
    fam_ii = []
    for a in range(3, 41):
        fam_ii.append((1 << a) + 2)
        fam_ii.append((1 << a) - 2)
    fam_iii = []
    for b in range(2, 26):
        fam_iii.append(3 ** b + 1)
        fam_iii.append(3 ** b - 1)
    families = [("(i) n=m*2^a, m odd <=999, a>=4, n<=10^12", fam_i),
                ("(ii) n=2^a+2 and 2^a-2, 3<=a<=40", fam_ii),
                ("(iii) n=3^b+1 and 3^b-1, 2<=b<=25", fam_iii)]
    all_n = []
    max_combos = 0
    fallbacks = []
    for (label, lst) in families:
        assert len(set(lst)) == len(lst)
        all_n.extend(lst)
        tot_cand = 0
        tot_le = 0
        tot_gt = 0
        surv = []
        fam_combos = 0
        fam_cand = []
        for n in lst:
            res = kc_process_n(n)
            fam_combos += res["combos"]
            max_combos = max(max_combos, res["combos"])
            if res["fallback"]:
                fallbacks.append((n, res["combos"], res["fallback_multiples"]))
            tot_cand += res["candidates"]
            tot_le += res["cand_le5000"]
            tot_gt += res["cand_gt5000"]
            for (j, viol) in res["cand_details"]:
                fam_cand.append((n, j, viol))
            surv.extend(res["survivors"])
        out(f"   family {label}: n values = {len(lst)}, CRT combinations "
            f"= {fam_combos}, candidates after pinning = {tot_cand} "
            f"(j<=5000: {tot_le}, j>5000: {tot_gt}), survivors = {surv}")
        out(f"   candidate pairs (n, j, first (LD3) violation "
            f"(r, q, j mod q)) = {fam_cand}")
        assert not surv
        record(f"S5 family {label}: {len(lst)} n values, {tot_cand} "
               f"candidates after pinning (j<=5000: {tot_le}, "
               f"j>5000: {tot_gt}), 0 survivors of (LD3)+(N2); "
               f"candidate pairs (n, j, first (LD3) violation "
               f"(r, q, j mod q)) = {fam_cand}")
    out(f"   max CRT combination count for a single n = {max_combos}; "
        f"fallback (combos>10^6) triggered for n = {fallbacks}")
    record(f"S5 CRT pinning: max combinations for a single n = "
           f"{max_combos}; (LD3)-first fallback triggered for "
           f"{len(fallbacks)} n values: {fallbacks}")
    # Trial-division cross-validation of factor_fast on a deterministic
    # subset of K-c tops (primes sieved to 1,100,000 >= sqrt of the
    # largest top, 2^40+1 = 1099511627777, sqrt = 1048577.000...).
    sel = set()
    for (_, lst) in families:
        idx = {0, 1, 2, len(lst) // 2, len(lst) - 1}
        idx |= set(range(0, len(lst), 2000))
        for i in idx:
            n = lst[i]
            sel.update((n, n - 1, n - 2))
    primes_trial = primes_upto(1100000)
    for m in sorted(sel):
        assert factor_fast(m) == factor_trial(m, primes_trial), m
    out(f"   factor_fast cross-validated against trial division by all "
        f"sieved primes to 1100000 on {len(sel)} K-c top values: "
        f"exact agreement")
    record(f"S5 factorisation cross-check: factor_fast agrees with full "
           f"trial division (sieved primes to 1100000) on {len(sel)} "
           f"K-c top values")
    # Overlap validation: every family member with n <= 10^6 is even and
    # in the S3/S4 range; recheck those n here by a direct search over
    # ALL multiples of R(n) (factorisation form), not just pin
    # candidates.
    uniq = sorted(set(n for n in all_n if n <= 10 ** 6))
    ov_pairs = 0
    ov_surv = []
    for n in uniq:
        assert n % 2 == 0
        f0 = factor_fast(n)
        Q0 = relevant_qs(f0)
        R = product_of(Q0)
        Q1 = relevant_qs(factor_fast(n - 1))
        Q2 = relevant_qs(factor_fast(n - 2))
        half = n // 2
        if R > half:
            continue
        j = first_multiple_gt(R, 3)
        while j <= half:
            ov_pairs += 1
            if ld3_q_form(j, Q1, Q2):
                ov_surv.append((n, j))
            j += R
    out(f"   overlap check: {len(uniq)} distinct family members with "
        f"n<=10^6 rechecked directly over all R(n)-multiples: "
        f"{ov_pairs} pairs, survivors = {ov_surv} (agreement with S3/S4: "
        f"zero survivors there as well)")
    assert not ov_surv
    record(f"S5 overlap validation: {len(uniq)} distinct family members "
           f"with n<=10^6, {ov_pairs} pairs rechecked directly, "
           f"0 survivors, agreeing with S3/S4")
    out(f"   S5 wall = {time.time() - t_sec:.1f}s")


# ==================================================================== main
SECTIONS = [("S0", section_S0), ("S1", section_S1), ("S2", section_S2),
            ("S3", section_S3), ("S4", section_S4), ("S5", section_S5)]


def main():
    wanted = sys.argv[1:]
    for name, fn in SECTIONS:
        if wanted and name not in wanted:
            continue
        fn()
    note("FINAL SUMMARY BLOCK (P-K2) - transcribe verbatim")
    print("=" * 70)
    for line in SUMMARY:
        print(line)
    print(f"TOTAL WALL TIME OF THIS RUN: {time.time() - T_START:.1f}s")
    print("=" * 70)


if __name__ == "__main__":
    main()
