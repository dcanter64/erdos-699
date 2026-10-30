#!/usr/bin/env python3
"""P-K1 checks: Cycle 3, Cluster K (computation), Computer K1.

Erdos #699, i = 3 frontier extension. Python standard library only,
exact integer arithmetic, single-threaded.

Definitions (exact, from the assignment):
  V_3(n) = C(n,3) / 2^{v_2(C(n,3))}            (the odd part of C(n,3))
  R(m)   = product of the relevant prime powers q = p^a || m
           (p >= 5, any a >= 1; or p = 3 with a >= 2);  R(m) is odd.
  (LD3)  pair (n, j), 3 < j <= n/2, satisfies (LD3) iff for every
         r in {0,1,2} and every relevant q = p^a || (n-r):
         j mod q <= r.
  (N2)   V_3(n) | C(j,3).
  N(3,j) = max{ n : C(n,3) < C(2j,6) }.

Sections:
  0. Utilities, N(3,j) spot values (Anchor C).
  1. Anchor A: per-pair (LD3) to j <= 5000 (F2.18 / V-F recount values),
     plus an independent brute-force cross-check for 5 <= j <= 60.
  2. K-a: per-pair frontier extension, pilot on [5001,6000], a coded
     extrapolation rule decides the final range BEFORE the remaining
     blocks are run; then the blocks are run.
  3. K-b: survivor search, even n, candidate pairs are the multiples
     j of R(n) with 7 <= j <= n/2 (the F2.21 counting convention that
     reproduces the certified anchor counts; j <= 6 is closed
     separately in the record). Anchor checkpoints at 10^5 and 10^6
     are asserted before the search proceeds past them. A coded
     extension rule then decides on the run to 10^8, which, if taken,
     uses an odd-only SPF sieve (200 MB, design stated in the code)
     cross-validated against the full SPF on (900000, 1000000].
  4. K-c: targeted high-v_2 families, (LD3)+(N2) via CRT pinning,
     with a direct-enumeration fallback if a raw candidate count
     for a single n ever exceeds 10^6 (it does not), plus the
     mandated overlap check against K-b/F2.21 for n <= 10^6 and a
     pinning-vs-brute-force validation on family members <= 50000.

Every headline number is asserted in this script where a certified
anchor exists. All results are COMPUTATION, not proofs.
"""
import gc
import math
import random
import time
from array import array
from math import comb, gcd, isqrt

T0 = time.time()
SUMMARY = []


def note(msg):
    print(f"[{time.time() - T0:8.2f}s] {msg}", flush=True)


def slog(label, value):
    SUMMARY.append((label, value))
    print(f"SUMMARY {label} = {value}", flush=True)


# ------------------------------------------------------------------ primes
def primes_upto(n):
    s = bytearray(b"\x01") * (n + 1)
    s[0:2] = b"\x00\x00"
    for i in range(2, isqrt(n) + 1):
        if s[i]:
            s[i * i:n + 1:i] = b"\x00" * (((n - i * i) // i) + 1)
    return [i for i, v in enumerate(s) if v]


PR50K = primes_upto(50000)


def factor_trial(m, primes=PR50K):
    """Exact factorisation of m as a dict {p: a}, trial division."""
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


def relevant_qs_from_factors(fac):
    return [p ** a for p, a in fac.items()
            if p >= 5 or (p == 3 and a >= 2)]


def relevant_qs_trial(m, primes=PR50K):
    return relevant_qs_from_factors(factor_trial(m, primes))


def R_from_factors(fac):
    r = 1
    for q in relevant_qs_from_factors(fac):
        r *= q
    return r


def N_of_3(j):
    """max{ n : C(n,3) < C(2j,6) }, exact binary search."""
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


# ------------------------------------------------------------------ 0. Anchor C
note("0. Anchor C: N(3,j) spot values (P-F2 section 6 item 4)")
EXPECTED_N = {7: 27, 100: 7908, 158: 19926, 159: 20181, 500: 201728,
              1000: 808934, 2000: 3239787, 5000: 20263871}
got_N = {j: N_of_3(j) for j in EXPECTED_N}
for j in sorted(EXPECTED_N):
    print(f"   N(3,{j}) = {got_N[j]} (expected {EXPECTED_N[j]})")
assert got_N == EXPECTED_N, (got_N, EXPECTED_N)
slog("anchor_C_N_spot_values_match", True)
slog("N(3,2000)", got_N[2000])
slog("N(3,5000)", got_N[5000])

# ------------------------------------------------------------------ 1. Anchor A
note("1. Anchor A: per-pair (LD3), 5 <= j <= 5000 (F2.18 / V-F recount)")
NMAX_A = EXPECTED_N[5000]
Nj_A = [0] * 5001
for j in range(5, 5001):
    Nj_A[j] = N_of_3(j)

# Candidate generation replicating the F1/V-F style exactly: d runs over
# odd d <= 5000 with v_3(d) != 1; t runs over powers of two with d*t <=
# NMAX_A; the candidate d*t is added, and if v_3(d) == 0 the candidate
# d*3*t is also added (in the F1/V-F code this second add is not itself
# bounded by NMAX_A, so some generated candidates exceed NMAX_A; they
# contribute no pairs because N(3,j) <= NMAX_A for all j <= 5000).
candA = set()
for d in range(1, 5001):
    if d % 2 == 0:
        continue
    v3 = 0
    x = d
    while x % 3 == 0:
        x //= 3
        v3 += 1
    if v3 == 1:
        continue
    t = 1
    while d * t <= NMAX_A:
        candA.add(d * t)
        if v3 == 0:
            candA.add(d * 3 * t)
        t *= 2
candA_sorted = sorted(candA)
cleanA = [n for n in candA_sorted if n <= NMAX_A]
print(f"   candidates generated (F1/V-F style) = {len(candA_sorted)}")
print(f"   candidates with n <= N(3,5000)      = {len(cleanA)}")
print(f"   candidates above N(3,5000)          = "
      f"{len(candA_sorted) - len(cleanA)} (contribute 0 pairs)")
assert len(candA_sorted) == 50489, len(candA_sorted)
assert len(cleanA) == 47723, len(cleanA)

pairsA = 0
pairsA_2000 = 0
survA = []
for n in candA_sorted:
    Rn = R_from_factors(factor_trial(n))
    assert Rn <= 5000, (n, Rn)
    rel1 = relevant_qs_trial(n - 1)
    rel2 = relevant_qs_trial(n - 2)
    j = ((5 + Rn - 1) // Rn) * Rn
    while j <= 5000 and 2 * j <= n:
        if n <= Nj_A[j]:
            pairsA += 1
            if j <= 2000:
                pairsA_2000 += 1
            if (all(j % q <= 1 for q in rel1)
                    and all(j % q <= 2 for q in rel2)):
                survA.append((n, j))
        j += Rn
print(f"   N-filtered pairs tested (j<=5000) = {pairsA}")
print(f"   N-filtered pairs tested (j<=2000) = {pairsA_2000}")
print(f"   survivors = {survA}")
assert pairsA == 341633, pairsA
assert pairsA_2000 == 107220, pairsA_2000
assert not survA
slog("anchor_A_candidates_generated_F_style", len(candA_sorted))
slog("anchor_A_candidates_le_Nmax_clean", len(cleanA))
slog("anchor_A_pairs_N_filtered_j_le_5000", pairsA)
slog("anchor_A_pairs_N_filtered_j_le_2000", pairsA_2000)
slog("anchor_A_survivors", len(survA))

# Independent brute-force cross-check, 5 <= j <= 60: every n in
# [2j, N(3,j)], full (LD3) from exact factorisations, no candidate
# shortcut of any kind.
note("1b. Anchor A cross-check: brute force over all n, 5 <= j <= 60")
brute_pairs = 0
brute_surv = []
for j in range(5, 61):
    Nj = N_of_3(j)
    for n in range(2 * j, Nj + 1):
        brute_pairs += 1
        if any(j % q != 0 for q in relevant_qs_trial(n)):
            continue
        if any(j % q > 1 for q in relevant_qs_trial(n - 1)):
            continue
        if any(j % q > 2 for q in relevant_qs_trial(n - 2)):
            continue
        brute_surv.append((n, j))
print(f"   brute-force pairs tested = {brute_pairs}; survivors = {brute_surv}")
assert not brute_surv
slog("anchor_A_bruteforce_j_5_60_pairs", brute_pairs)
slog("anchor_A_bruteforce_j_5_60_survivors", len(brute_surv))

# ------------------------------------------------------------------ 2. K-a
note("2. K-a: per-pair frontier extension from j = 5001")
PR_KA = primes_upto(100000)


def R_of_trial(m):
    """R(m) by exact trial factorisation (primes to 100000)."""
    x = m
    R = 1
    for p in PR_KA:
        if p * p > x:
            break
        if x % p == 0:
            a = 0
            q = 1
            while x % p == 0:
                x //= p
                a += 1
                q *= p
            if p >= 5 or (p == 3 and a >= 2):
                R *= q
    if x > 1 and x >= 5:
        R *= x
    return R


def ld3_top_ok(m, j, lim):
    """True iff every relevant q || m satisfies j mod q <= lim.

    Factorises m by trial division in ascending prime order and tests
    each relevant prime power as soon as it is found, aborting the
    factorisation at the first violated clause (exact: a violated
    clause disqualifies the pair regardless of the remaining factors).
    """
    x = m
    for p in PR_KA:
        if p * p > x:
            break
        if x % p == 0:
            a = 0
            q = 1
            while x % p == 0:
                x //= p
                a += 1
                q *= p
            if p >= 5 or (p == 3 and a >= 2):
                if j % q > lim:
                    return False
    if x > 1 and x >= 5:
        if j % x > lim:
            return False
    return True


def divisors_of(j):
    ds = []
    r = isqrt(j)
    for d in range(1, r + 1):
        if j % d == 0:
            ds.append(d)
            if d * d != j:
                ds.append(j // d)
    return ds


def v3_of_int(x):
    v = 0
    while x % 3 == 0:
        x //= 3
        v += 1
    return v


def run_ka_block(jlo, jhi):
    """Complete candidate enumeration for one block of j values.

    For each j, an (LD3) solution needs R(n) | j, so R(n) is a divisor
    d of j with d odd and v_3(d) != 1; n is then d * 2^a or, if
    v_3(d) == 0, d * 3 * 2^a (the exact d*t decomposition of
    F1.16/F2.18). Every generated n is verified by exact factorisation
    (R_of_trial(n) == d) before its (n-1) and (n-2) clauses are tested.
    Returns (candidates, pairs_tested, survivors, wall_seconds, N_end).
    Candidates and pairs tested coincide by construction: every
    generated candidate is clause-tested exactly once.
    """
    t_start = time.time()
    cand = 0
    surv = []
    for j in range(jlo, jhi + 1):
        Nj = N_of_3(j)
        for d in divisors_of(j):
            if d % 2 == 0:
                continue
            v = v3_of_int(d)
            if v == 1:
                continue
            t = 1
            while d * t <= Nj:
                n = d * t
                if n >= 2 * j:
                    cand += 1
                    assert R_of_trial(n) == d, (n, d)
                    if ld3_top_ok(n - 1, j, 1) and ld3_top_ok(n - 2, j, 2):
                        surv.append((n, j))
                t *= 2
            if v == 0:
                t = 3
                while d * t <= Nj:
                    n = d * t
                    if n >= 2 * j:
                        cand += 1
                        assert R_of_trial(n) == d, (n, d)
                        if (ld3_top_ok(n - 1, j, 1)
                                and ld3_top_ok(n - 2, j, 2)):
                            surv.append((n, j))
                    t *= 2
    return cand, cand, surv, time.time() - t_start, N_of_3(jhi)


# Pilot first; the extrapolation rule below is applied to the pilot
# output before any further block is run.
pilot = run_ka_block(5001, 6000)
print(f"   pilot [5001,6000]: candidates = {pilot[0]}, pairs tested = "
      f"{pilot[1]}, survivors = {pilot[2]}, wall = {pilot[3]:.2f}s, "
      f"N(3,6000) = {pilot[4]}")
slog("Ka_pilot_block", (5001, 6000))
slog("Ka_pilot_candidates", pilot[0])
slog("Ka_pilot_pairs_tested", pilot[1])
slog("Ka_pilot_survivors", pilot[2])
slog("Ka_pilot_wall_seconds", round(pilot[3], 2))
slog("N(3,6000)", pilot[4])

# Extrapolation rule (coded here, applied before the full run):
# projected time for a 5000-wide block = pilot wall x 5 (block width
# ratio) x 2.0 (safety factor for the growth of N(3,j) and of the
# factorisation cost across the range). Extend in 5000-wide blocks,
# choosing the largest target in {50000, 45000, ..., 20000} whose
# projected total remaining time is <= 7200 s (the internal budget),
# provided each projected block is <= 1800 s (~30 min); otherwise fall
# back to the mandated minimum 20000.
proj_block = pilot[3] * 5.0 * 2.0
KA_TARGET = 20000
for target in (50000, 45000, 40000, 35000, 30000, 25000, 20000):
    blocks_remaining = (target - 6000) / 5000.0
    if proj_block <= 1800.0 and proj_block * blocks_remaining <= 7200.0:
        KA_TARGET = target
        break
print(f"   extrapolation: projected 5000-block = {proj_block:.2f}s "
      f"(pilot {pilot[3]:.2f}s x 5 x 2.0 safety); "
      f"chosen final range: j <= {KA_TARGET}")
slog("Ka_projected_5000_block_seconds", round(proj_block, 2))
slog("Ka_final_j_target", KA_TARGET)

ka_blocks = [(5001, 6000, pilot)]
cur = 6001
while cur <= KA_TARGET:
    hi = min(KA_TARGET, ((cur + 4999) // 5000) * 5000)
    if hi < cur:
        hi = KA_TARGET
    res = run_ka_block(cur, hi)
    ka_blocks.append((cur, hi, res))
    print(f"   block [{cur},{hi}]: candidates = {res[0]}, pairs tested "
          f"= {res[1]}, survivors = {res[2]}, wall = {res[3]:.2f}s, "
          f"N(3,{hi}) = {res[4]}", flush=True)
    cur = hi + 1

ka_total_cand = sum(r[0] for _, _, r in ka_blocks)
ka_total_surv = [s for _, _, r in ka_blocks for s in r[2]]
ka_total_wall = sum(r[3] for _, _, r in ka_blocks)
ka_mand_cand = sum(r[0] for lo, hi, r in ka_blocks if hi <= 20000)
ka_mand_wall = sum(r[3] for lo, hi, r in ka_blocks if hi <= 20000)
ka_mand_surv = [s for lo, hi, r in ka_blocks if hi <= 20000
                for s in r[2]]
for lo, hi, r in ka_blocks:
    slog(f"Ka_block_{lo}_{hi}",
         (r[0], r[1], len(r[2]), round(r[3], 2), r[4]))
slog("Ka_mandated_5001_20000_candidates", ka_mand_cand)
slog("Ka_mandated_5001_20000_pairs_tested", ka_mand_cand)
slog("Ka_mandated_5001_20000_survivors", ka_mand_surv)
slog("Ka_mandated_5001_20000_wall_seconds", round(ka_mand_wall, 2))
slog("N(3,20000)", N_of_3(20000))
slog("Ka_total_5001_to_target_candidates", ka_total_cand)
slog("Ka_total_5001_to_target_pairs_tested", ka_total_cand)
slog("Ka_total_5001_to_target_survivors", ka_total_surv)
slog("Ka_total_wall_seconds", round(ka_total_wall, 2))
slog(f"N(3,{KA_TARGET})", N_of_3(KA_TARGET))
assert not ka_total_surv

# ------------------------------------------------------------------ 3. K-b
note("3. K-b: survivor search, even n, multiples of R(n), 7 <= j <= n/2")


def build_full_spf(L):
    spf = array("i", range(L + 1))
    for i in range(isqrt(L), 1, -1):
        cnt = (L - i) // i + 1
        spf[i::i] = array("i", [i] * cnt)
    return spf


def make_rel_fn(spf_of):
    def rel(m):
        qs = []
        x = m
        while x > 1:
            p = spf_of(x)
            q = 1
            a = 0
            while x % p == 0:
                x //= p
                q *= p
                a += 1
            if p >= 5 or (p == 3 and a >= 2):
                qs.append(q)
        return qs
    return rel


def process_range_even(lo, hi, spf_of):
    """Pairs (n,j), even n in (lo,hi], j a multiple of R(n),
    7 <= j <= n/2, tested against the full (LD3) clauses.
    Returns (pairs, survivors, n_with_candidates)."""
    rel = make_rel_fn(spf_of)
    pairs = 0
    surv = []
    n_with = 0
    n = lo + 1 if (lo + 1) % 2 == 0 else lo + 2
    if n < 14:
        n = 14
    for n in range(n, hi + 1, 2):
        Rn = 1
        for q in rel(n):
            Rn *= q
        if Rn > n // 2:
            continue
        combined = ([(q, 1) for q in rel(n - 1)]
                    + [(q, 2) for q in rel(n - 2)])
        combined.sort(reverse=True)
        j = ((7 + Rn - 1) // Rn) * Rn
        local = 0
        while j <= n // 2:
            local += 1
            ok = True
            for q, lim in combined:
                if j % q > lim:
                    ok = False
                    break
            if ok:
                surv.append((n, j))
            j += Rn
        if local:
            n_with += 1
            pairs += local
    return pairs, surv, n_with


KB_LIM = 10 ** 7
t_spf = time.time()
spf_full = build_full_spf(KB_LIM)
print(f"   full SPF to {KB_LIM} built in {time.time() - t_spf:.2f}s "
      f"({spf_full.itemsize * len(spf_full)} bytes)")
spf_full_of = lambda x: spf_full[x]  # noqa: E731

kb_segments = []  # (lo, hi, pairs_inc, surv, n_with, wall)
kb_cum_pairs = 0
kb_cum_surv = []
prev = 0
for seg_hi in (10 ** 5, 10 ** 6, 10 ** 7):
    t_seg = time.time()
    p_inc, s_inc, nw_inc = process_range_even(prev, seg_hi, spf_full_of)
    wall = time.time() - t_seg
    kb_segments.append((prev, seg_hi, p_inc, s_inc, nw_inc, wall))
    kb_cum_pairs += p_inc
    kb_cum_surv += s_inc
    print(f"   segment ({prev},{seg_hi}]: pairs inc = {p_inc}, "
          f"cumulative = {kb_cum_pairs}, survivors inc = {len(s_inc)}, "
          f"wall = {wall:.2f}s", flush=True)
    if seg_hi == 10 ** 5:
        assert kb_cum_pairs == 604976, kb_cum_pairs
        print("   anchor (F2.21, n<=10^5) reproduced: 604976 pairs")
    if seg_hi == 10 ** 6:
        # ANCHOR B: asserted here, before any n > 10^6 is processed.
        assert kb_cum_pairs == 6974117, kb_cum_pairs
        assert not kb_cum_surv
        print("   ANCHOR B PASSED: 6974117 pairs, 0 survivors at "
              "n <= 10^6; proceeding to 10^7")
    prev = seg_hi
for lo, hi, p_inc, s_inc, nw_inc, wall in kb_segments:
    slog(f"Kb_segment_{lo}_{hi}",
         (p_inc, len(s_inc), nw_inc, round(wall, 2)))
slog("Kb_pairs_cumulative_1e5", kb_segments[0][2])
slog("Kb_pairs_cumulative_1e6", kb_segments[0][2] + kb_segments[1][2])
slog("Kb_anchor_B_pairs_1e6", 6974117)
slog("Kb_pairs_cumulative_1e7", kb_cum_pairs)
slog("Kb_survivors_1e7", kb_cum_surv)
assert not kb_cum_surv

# Cross-validation interval for a possible odd-only-SPF extension:
# pair count on (900000, 1000000] with the full SPF.
test_lo, test_hi = 900000, 1000000
tp_full, ts_full, _ = process_range_even(test_lo, test_hi, spf_full_of)
print(f"   cross-check interval ({test_lo},{test_hi}] with full SPF: "
      f"pairs = {tp_full}, survivors = {len(ts_full)}")
slog("Kb_crosscheck_interval_pairs_full_spf", tp_full)

# Extension decision (coded here, applied before any n > 10^7 work):
# projected time for the (10^7, 10^8] decade = (time of the
# (10^6,10^7] segment) x (ratio of the last two segment times),
# plus 120 s allowance for building the odd-only SPF.
# Memory design for the extension: an odd-only SPF array of
# 50,000,000 signed 32-bit entries = 200,000,000 bytes (~0.2 GB,
# <= the ~2 GB design bound). Proceed iff the projection is
# <= 1800 s (~30 min) and that memory bound holds.
t_prev = kb_segments[1][5]
t_last = kb_segments[2][5]
ratio = t_last / t_prev if t_prev > 0 else 0.0
proj_ext = t_last * ratio + 120.0
odd_spf_bytes = 50000000 * 4
KB_EXTEND = (proj_ext <= 1800.0) and (odd_spf_bytes <= 2 * 10 ** 9)
print(f"   extension rule: segment times {t_prev:.2f}s -> {t_last:.2f}s "
      f"(ratio {ratio:.3f}); projected (1e7,1e8] time = {proj_ext:.2f}s; "
      f"odd-only SPF memory = {odd_spf_bytes} bytes; "
      f"decision: {'PROCEED to 10^8' if KB_EXTEND else 'STOP at 10^7'}")
slog("Kb_segment_time_ratio", round(ratio, 3))
slog("Kb_projected_1e8_seconds", round(proj_ext, 2))
slog("Kb_odd_spf_design_bytes", odd_spf_bytes)
slog("Kb_extend_to_1e8", KB_EXTEND)

kb_final_limit = 10 ** 7
kb_ext_blocks = []
if KB_EXTEND:
    del spf_full, spf_full_of
    gc.collect()

    def build_odd_spf(hi):
        ospf = array("i", range(1, hi + 1, 2))
        primes = [p for p in primes_upto(isqrt(hi)) if p >= 3]
        for p in reversed(primes):
            start_idx = (p - 1) // 2
            cnt = (hi - p) // (2 * p) + 1
            if cnt > 0:
                ospf[start_idx::p] = array("i", [p] * cnt)
        return ospf

    t_odd = time.time()
    ospf = build_odd_spf(10 ** 8)
    print(f"   odd-only SPF to 10^8 built in {time.time() - t_odd:.2f}s "
          f"({ospf.itemsize * len(ospf)} bytes)")
    slog("Kb_odd_spf_actual_bytes", ospf.itemsize * len(ospf))

    def odd_spf_of(x, _ospf=ospf):
        if x % 2 == 0:
            return 2
        return _ospf[(x - 1) // 2]

    tp_odd, ts_odd, _ = process_range_even(test_lo, test_hi, odd_spf_of)
    print(f"   cross-check interval with odd-only SPF: pairs = {tp_odd},"
          f" survivors = {len(ts_odd)} (full SPF: {tp_full})")
    assert tp_odd == tp_full and len(ts_odd) == len(ts_full) == 0
    slog("Kb_crosscheck_interval_pairs_odd_spf", tp_odd)
    slog("Kb_crosscheck_agrees", True)

    prev = 10 ** 7
    for blk_hi in range(2 * 10 ** 7, 10 ** 8 + 1, 10 ** 7):
        t_blk = time.time()
        p_inc, s_inc, nw_inc = process_range_even(prev, blk_hi,
                                                  odd_spf_of)
        wall = time.time() - t_blk
        kb_ext_blocks.append((prev, blk_hi, p_inc, s_inc, wall))
        kb_cum_pairs += p_inc
        kb_cum_surv += s_inc
        print(f"   extension block ({prev},{blk_hi}]: pairs inc = "
              f"{p_inc}, cumulative = {kb_cum_pairs}, survivors inc = "
              f"{len(s_inc)}, wall = {wall:.2f}s", flush=True)
        prev = blk_hi
    kb_final_limit = 10 ** 8
    for lo, hi, p_inc, s_inc, wall in kb_ext_blocks:
        slog(f"Kb_ext_block_{lo}_{hi}",
             (p_inc, len(s_inc), round(wall, 2)))
    ext_pairs = sum(b[2] for b in kb_ext_blocks)
    slog("Kb_pairs_decade_1e7_1e8", ext_pairs)
    del ospf
    gc.collect()

slog("Kb_final_limit", kb_final_limit)
slog("Kb_pairs_cumulative_final", kb_cum_pairs)
slog("Kb_survivors_final", kb_cum_surv)
assert not kb_cum_surv

# ------------------------------------------------------------------ 4. K-c
note("4. K-c: targeted high-v_2 families, (LD3)+(N2) by CRT pinning")
PR_BIG = primes_upto(10 ** 6)
_PRIMES_TO_10000 = primes_upto(10000)


def is_prime_det(n):
    """Deterministic Miller-Rabin for n < 2,152,302,898,747
    (bases 2,3,5,7,11 suffice there; n <= ~1.1 x 10^12 here)."""
    if n < 2:
        return False
    for p in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29):
        if n % p == 0:
            return n == p
    d = n - 1
    s = 0
    while d % 2 == 0:
        d //= 2
        s += 1
    for a in (2, 3, 5, 7, 11):
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


def pollard_brent(n):
    """Deterministic-seed Brent Pollard rho; returns a factor of n."""
    if n % 2 == 0:
        return 2
    if n % 3 == 0:
        return 3
    for c in range(1, 64):
        y = 2
        r = 1
        q = 1
        g = 1
        while g == 1:
            x = y
            for _ in range(r):
                y = (y * y + c) % n
            k = 0
            while k < r and g == 1:
                ys = y
                for _ in range(min(128, r - k)):
                    y = (y * y + c) % n
                    q = q * abs(x - y) % n
                g = gcd(q, n)
                k += 128
            r *= 2
            if r > (1 << 24):
                break
        if g == n:
            # this polynomial failed; retry with the next constant
            continue
        if 1 < g < n:
            return g
    raise ArithmeticError(f"pollard_brent failed on {n}")


def factorize_1e12(n):
    """Exact factorisation {p: a} for 1 <= n <= ~1.1 x 10^12:
    trial division by the primes to 10000 (prime bound stated; the
    square root of 10^12 is 10^6, covered independently by the
    random-sample cross-check against full trial division to 10^6
    below), after which any remaining cofactor x > 1 has all prime
    factors > 10000, hence is 1, prime, a prime square, or a product
    of exactly two primes (10007^3 > 10^12); it is resolved by
    deterministic Miller-Rabin, an exact square test, and Brent
    Pollard rho. No cofactor > 1 is left unexamined."""
    out = {}
    x = n
    for p in _PRIMES_TO_10000:
        if p * p > x:
            break
        if x % p == 0:
            a = 0
            while x % p == 0:
                x //= p
                a += 1
            out[p] = a
        if x == 1:
            break
    if x == 1:
        return out
    stack = [x]
    while stack:
        y = stack.pop()
        if y == 1:
            continue
        if is_prime_det(y):
            out[y] = out.get(y, 0) + 1
            continue
        s = isqrt(y)
        if s * s == y:
            stack.append(s)
            stack.append(s)
            continue
        d = pollard_brent(y)
        assert 1 < d < y and y % d == 0
        stack.append(d)
        stack.append(y // d)
    return out


def factor_trial_full_1e12(n):
    """Reference factorisation by trial division with all primes
    to 10^6 = sqrt(10^12)."""
    out = {}
    x = n
    for p in PR_BIG:
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


# Factoriser cross-check on a fixed seeded sample.
random.seed(1)
mismatch = 0
for _ in range(300):
    v = random.randint(2, 10 ** 12)
    if factorize_1e12(v) != factor_trial_full_1e12(v):
        mismatch += 1
print(f"   factoriser cross-check: 300 seeded random values in "
      f"[2,10^12], mismatches vs full trial division = {mismatch}")
assert mismatch == 0
slog("Kc_factoriser_crosscheck_samples", 300)
slog("Kc_factoriser_crosscheck_mismatches", mismatch)


def kc_setup(n):
    fn = factorize_1e12(n)
    f1 = factorize_1e12(n - 1)
    f2 = factorize_1e12(n - 2)
    tot = {}
    for f in (fn, f1, f2):
        for p, a in f.items():
            tot[p] = tot.get(p, 0) + a
    # C(n,3) = n(n-1)(n-2)/6; V_3 drops the whole 2-part and one 3.
    tot[2] = tot.get(2, 0) - 1
    tot[3] = tot.get(3, 0) - 1
    v3fac = {p: e for p, e in tot.items() if p != 2 and e > 0}
    V = 1
    for p, e in v3fac.items():
        V *= p ** e
    R0, rel0 = R_from_factors(fn), relevant_qs_from_factors(fn)
    rel1 = relevant_qs_from_factors(f1)
    rel2 = relevant_qs_from_factors(f2)
    return fn, f1, f2, v3fac, V, R0, rel0, rel1, rel2


def kc_direct_candidates(n, V, R0, rel1, rel2):
    """Fallback used only if a raw CRT count for a single n exceeds
    10^6: enumerate the multiples j of R(n) in the (N2)-size window
    C(j,3) >= V_3(n), keep those with V_3(n) | C(j,3) exactly."""
    limit = n // 2
    if comb(limit, 3) < V:
        return [], []
    lo, hi = 4, limit
    while lo < hi:
        mid = (lo + hi) // 2
        if comb(mid, 3) < V:
            lo = mid + 1
        else:
            hi = mid
    j = ((lo + R0 - 1) // R0) * R0
    cands = []
    surv = []
    while j <= limit:
        if comb(j, 3) % V == 0:
            cands.append(j)
            if (all(j % q <= 1 for q in rel1)
                    and all(j % q <= 2 for q in rel2)):
                surv.append(j)
        j += R0
    return cands, surv


def kc_candidates(n, data):
    """CRT pinning for (N2), intersected with R(n) | j and the window
    3 < j <= n/2. Returns (candidates, survivors, raw_combos,
    max_classes, used_fallback)."""
    fn, f1, f2, v3fac, V, R0, rel0, rel1, rel2 = data
    limit = n // 2
    items = []  # (q, allowed residues mod q)
    for p, e in v3fac.items():
        if p == 3:
            if e == 0:
                continue
            q = 3 ** (e + 1)
            if fn.get(3, 0) >= 2 and fn.get(3, 0) == e + 1:
                allowed = (0,)
            else:
                allowed = (0, 1, 2)
            items.append((q, allowed))
        else:
            q = p ** e
            allowed = (0,) if p in fn else (0, 1, 2)
            items.append((q, allowed))
    items.sort(key=lambda t: -t[0])
    raw = 1
    for _, al in items:
        raw *= len(al)
    if raw > 10 ** 6:
        cands, surv = kc_direct_candidates(n, V, R0, rel1, rel2)
        return cands, surv, raw, 0, True
    classes = [(0, 1)]
    explicit = None
    max_classes = 1
    for q, allowed in items:
        if explicit is not None:
            explicit = [j for j in explicit if j % q in allowed]
            continue
        new = []
        for r, m in classes:
            inv = pow(m, -1, q)
            for s in allowed:
                t = ((s - r) * inv) % q
                x = r + m * t
                nm = m * q
                first = x
                if first <= 3:
                    first += nm * ((4 - first + nm - 1) // nm)
                if first <= limit:
                    new.append((x, nm))
        classes = new
        max_classes = max(max_classes, len(classes))
        if not classes:
            break
        if len(classes) > 10 ** 6:
            cands, surv = kc_direct_candidates(n, V, R0, rel1, rel2)
            return cands, surv, raw, max_classes, True
        if classes[0][1] > limit:
            explicit = []
            for x, nm in classes:
                j = x
                if j <= 3:
                    j += nm * ((4 - j + nm - 1) // nm)
                while j <= limit:
                    explicit.append(j)
                    j += nm
            explicit.sort()
    if explicit is None:
        explicit = []
        for x, nm in classes:
            j = x
            if j <= 3:
                j += nm * ((4 - j + nm - 1) // nm)
            while j <= limit:
                explicit.append(j)
                j += nm
        explicit.sort()
    if R0 > 1:
        explicit = [j for j in explicit if j % R0 == 0]
    surv = []
    for j in explicit:
        if comb(j, 3) % V != 0:
            continue
        if any(j % q != 0 for q in rel0):
            continue
        if any(j % q > 1 for q in rel1):
            continue
        if any(j % q > 2 for q in rel2):
            continue
        surv.append(j)
    return explicit, surv, raw, max_classes, False


families = {}
fam_i = set()
for m_odd in range(1, 1000, 2):
    a = 4
    while m_odd * (1 << a) <= 10 ** 12:
        fam_i.add(m_odd * (1 << a))
        a += 1
families["i"] = sorted(fam_i)
families["ii"] = sorted({(1 << a) + 2 for a in range(3, 41)}
                        | {(1 << a) - 2 for a in range(3, 41)})
families["iii"] = sorted({3 ** b + 1 for b in range(2, 26)}
                         | {3 ** b - 1 for b in range(2, 26)})

kc_all_candidates = []   # (family, n, j) after pinning, before LD3
kc_stats = {}
kc_max_raw = (0, None)
kc_max_cand = (0, None)
kc_fallback_ns = []
for name in ("i", "ii", "iii"):
    vals = families[name]
    cand_tot = 0
    le5000 = 0
    gt5000 = 0
    surv_tot = []
    for n in vals:
        data = kc_setup(n)
        cands, surv, raw, mc, fb = kc_candidates(n, data)
        if fb:
            kc_fallback_ns.append(n)
        cand_tot += len(cands)
        le5000 += sum(1 for j in cands if j <= 5000)
        gt5000 += sum(1 for j in cands if j > 5000)
        surv_tot += [(n, j) for j in surv]
        for j in cands:
            kc_all_candidates.append((name, n, j))
        if raw > kc_max_raw[0]:
            kc_max_raw = (raw, n)
        if len(cands) > kc_max_cand[0]:
            kc_max_cand = (len(cands), n)
    kc_stats[name] = (len(vals), cand_tot, le5000, gt5000, surv_tot)
    print(f"   family {name}: n values = {len(vals)}, candidates after "
          f"pinning = {cand_tot} (j<=5000: {le5000}, j>5000: {gt5000}), "
          f"survivors of (LD3)+(N2) = {surv_tot}", flush=True)
    slog(f"Kc_family_{name}",
         (len(vals), cand_tot, le5000, gt5000, len(surv_tot)))
slog("Kc_all_pinning_candidates", kc_all_candidates)
slog("Kc_max_raw_combos", kc_max_raw)
slog("Kc_max_candidates_single_n", kc_max_cand)
slog("Kc_fallback_ns", kc_fallback_ns)
kc_total_surv = [s for v in kc_stats.values() for s in v[4]]
slog("Kc_survivors_total", kc_total_surv)
assert not kc_total_surv
assert not kc_fallback_ns

# Pinning-vs-brute-force validation on family members with n <= 50000:
# brute candidates are the multiples j of R(n) in (3, n/2] with
# V_3(n) | C(j,3) tested exactly; they must equal the pinning list.
note("4b. K-c pinning validation vs brute force, family n <= 50000")
val_ns = sorted({n for vals in families.values() for n in vals
                 if n <= 50000})
val_bad = 0
val_cand = 0
for n in val_ns:
    data = kc_setup(n)
    fn, f1, f2, v3fac, V, R0, rel0, rel1, rel2 = data
    cands, _, _, _, _ = kc_candidates(n, data)
    brute = []
    j = ((4 + R0 - 1) // R0) * R0
    while j <= n // 2:
        if comb(j, 3) % V == 0:
            brute.append(j)
        j += R0
    val_cand += len(brute)
    if brute != cands:
        val_bad += 1
        print(f"   MISMATCH at n={n}: pinning {cands} vs brute {brute}")
print(f"   validated n values = {len(val_ns)}; brute candidates = "
      f"{val_cand}; mismatching n = {val_bad}")
assert val_bad == 0
slog("Kc_pinning_validation_n_values", len(val_ns))
slog("Kc_pinning_validation_brute_candidates", val_cand)
slog("Kc_pinning_validation_mismatches", val_bad)

# Mandated overlap check: every family member with n <= 10^6 is even
# (families (i)-(iii) all give even n), so K-b / F2.21 applies.
# Direct (LD3) search over the multiples of R(n), 3 < j <= n/2.
note("4c. K-c overlap check vs K-b/F2.21: direct (LD3), family n <= 10^6")
ov_ns = sorted({n for vals in families.values() for n in vals
                if n <= 10 ** 6})
assert all(n % 2 == 0 for n in ov_ns)
ov_pairs = 0
ov_surv = []
for n in ov_ns:
    fn = factorize_1e12(n)
    f1 = factorize_1e12(n - 1)
    f2 = factorize_1e12(n - 2)
    R0 = R_from_factors(fn)
    rel1 = relevant_qs_from_factors(f1)
    rel2 = relevant_qs_from_factors(f2)
    j = ((4 + R0 - 1) // R0) * R0
    while j <= n // 2:
        ov_pairs += 1
        if (all(j % q <= 1 for q in rel1)
                and all(j % q <= 2 for q in rel2)):
            ov_surv.append((n, j))
        j += R0
print(f"   overlap n values = {len(ov_ns)}; (LD3) pairs tested = "
      f"{ov_pairs}; survivors = {ov_surv} (K-b/F2.21: zero, agrees)")
assert not ov_surv
slog("Kc_overlap_n_values_le_1e6", len(ov_ns))
slog("Kc_overlap_pairs_tested", ov_pairs)
slog("Kc_overlap_survivors", len(ov_surv))

# ------------------------------------------------------------------ summary
note("ALL K1 CHECKS COMPLETED")
print()
print("=== FINAL SUMMARY BLOCK (K1) ===")
for label, value in SUMMARY:
    print(f"{label} = {value}")
print(f"total_wall_seconds = {time.time() - T0:.2f}")
print("=== END FINAL SUMMARY BLOCK (K1) ===")
