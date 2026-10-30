#!/usr/bin/env python3
"""
Prover B1 independent recount for Erdos #699, Strategy S1, Theorem D.
Exact integer arithmetic only (no floats anywhere in the classification).

Definitions (NSTAR = 10000):
  EEES pairpass criterion:  N(i,j) <= NSTAR
      iff C(NSTAR+1, i) >= C(2j, 2(j-i)) = C(2j, 2i),
      because N(i,j) = max{ n : C(n,i) < C(2j,2(j-i)) } and C(n,i)
      is strictly increasing in n.
  Kummer criterion:  N_K(i,j) <= NSTAR
      iff F_i(NSTAR+1) > C(j, j-i) = C(j, i),
      i.e. iff C(j,i) * (NSTAR+1)**pi(i-1) < C(NSTAR+1, i),
      because N_K(i,j) = max{ n : F_i(n) <= C(j,j-i) } and F_i is
      strictly increasing in n (Lemma B1.5).

For fixed i, both C(2j,2i) and C(j,i) are strictly increasing in j,
so for each i each cleared set is a prefix of the j-range, located by
exact binary search on the single threshold C(10001,i) (EEES) resp.
the single integer Kthr_i = (C(10001,i)-1) // 10001**pi(i-1) (Kummer:
C(j,i) <= Kthr_i  iff  C(j,i)*10001**pi(i-1) < C(10001,i)).

A second, independent per-pair scan (incremental exact recurrences,
early exit once both thresholds are passed) cross-checks the totals.
"""
import json, sys, time
from math import comb

NSTAR = 10000
N1 = NSTAR + 1          # 10001
IMAX = 1000
JMAX = NSTAR // 2       # 5000, from 2j <= 10000

def primes_upto(n):
    s = bytearray(b"\x01") * (n + 1)
    s[0:2] = b"\x00\x00"
    for p in range(2, int(n ** 0.5) + 1):
        if s[p]:
            s[p * p::p] = b"\x00" * len(s[p * p::p])
    return [p for p, v in enumerate(s) if v]

PRIMES = primes_upto(IMAX)
import bisect
def pi_of(x):
    return bisect.bisect_right(PRIMES, x)

def largest_j(pred_lo, pred_hi, pred):
    """max j in [pred_lo, pred_hi] with pred(j) true; pred is a prefix
    predicate (true ... true false ... false). Returns pred_lo-1 if none."""
    lo, hi = pred_lo, pred_hi + 1   # pred(lo-1) treated true-ish, pred(hi) false sentinel
    # invariant: search in [lo, hi]; we want last true
    a, b = pred_lo - 1, pred_hi + 1
    # a = known-true-or-boundary, b = known-false-or-boundary(sentinel)
    while b - a > 1:
        m = (a + b) // 2
        if m <= pred_hi and pred(m):
            a = m
        else:
            b = m
    return a

def main():
    t0 = time.time()
    total_pairs = 0
    total_E = 0
    total_K = 0
    total_new = 0
    total_new_i_ge_3 = 0
    JE = {}
    JK = {}
    for i in range(1, IMAX + 1):
        lo_open = 3 * i // 2 + 1          # smallest j with j > 3i/2
        hi_j = JMAX
        if lo_open > hi_j:
            continue
        total_pairs += hi_j - lo_open + 1
        T = comb(N1, i)                    # threshold C(10001, i)
        p = pi_of(i - 1)                   # pi(i-1)
        U = N1 ** p                        # U(10001, i) = 10001**pi(i-1)
        Kthr = (T - 1) // U                # C(j,i) <= Kthr  <=>  C(j,i)*U < T

        jE = largest_j(i, hi_j, lambda j: comb(2 * j, 2 * i) <= T)
        jK = largest_j(i, hi_j, lambda j: comb(j, i) <= Kthr)
        JE[i] = jE
        JK[i] = jK
        e_cnt = max(0, min(jE, hi_j) - lo_open + 1)
        k_cnt = max(0, min(jK, hi_j) - lo_open + 1)
        new_cnt = max(0, min(jK, hi_j) - max(jE, lo_open - 1)) if jK >= lo_open else 0
        total_E += e_cnt
        total_K += k_cnt
        total_new += new_cnt
        if i >= 3:
            total_new_i_ge_3 += new_cnt
    dt = time.time() - t0
    print(f"method=binary-search exact integers   runtime={dt:.2f}s")
    print(f"total open pairs (i<=1000, j>3i/2, 2j<=10000): {total_pairs}")
    print(f"EEES cleared  (N<=10000):    {total_E}")
    print(f"Kummer cleared (N_K<=10000): {total_K}  (counted in open range, incl. overlap)")
    print(f"NEWLY cleared (K yes, E no): {total_new}")
    print(f"  of which i>=3:             {total_new_i_ge_3}")
    print(f"  of which i in {{1,2}}:      {total_new - total_new_i_ge_3}")
    print(f"total cleared E + new:       {total_E + total_new}")
    spots = [3, 5, 10, 11, 50, 100, 500, 1000]
    print("spot values (i, J_E, J_K):", [(i, JE[i], JK[i]) for i in spots])
    exc = [i for i in range(1, 31) if JK[i] <= JE[i]]
    print("i<=30 with J_K <= J_E:", exc)
    return JE, JK, total_E, total_new

def crosscheck(JE, JK):
    """Independent per-pair scan with incremental exact recurrences.
    For each i, iterate j upward in the open range, maintaining
    A_j = C(j, i) and B_j = C(2j, 2i) exactly, and classify EVERY pair
    visited by the single exact comparisons B_j <= T and A_j <= Kthr.
    Once j exceeds both J_E(i) and J_K(i) (as found above) all later j
    fail both tests by monotonicity, so the scan may stop; the number
    of pairs actually visited is reported."""
    t0 = time.time()
    total_E = 0
    total_new = 0
    visited = 0
    for i in range(1, IMAX + 1):
        lo_open = 3 * i // 2 + 1
        if lo_open > JMAX:
            continue
        T = comb(N1, i)
        p = pi_of(i - 1)
        Kthr = (T - 1) // (N1 ** p)
        jstop = max(JE[i], JK[i], lo_open - 1)
        jstop = min(jstop, JMAX)
        # initialise A, B at j = lo_open
        j = lo_open
        A = comb(j, i)      # C(j, i)
        B = comb(2 * j, 2 * i)  # C(2j, 2i)
        while True:
            visited += 1
            e_ok = B <= T
            k_ok = A <= Kthr
            if e_ok:
                total_E += 1
            if k_ok and not e_ok:
                total_new += 1
            if j >= jstop:
                break
            # advance j -> j+1:
            # C(j+1, i) = C(j, i) * (j+1) / (j+1-i)
            A = A * (j + 1) // (j + 1 - i)
            # C(2j+2, 2i) = C(2j, 2i) * (2j+2)(2j+1) / ((2j+2-2i)(2j+1-2i))
            B = B * (2 * j + 2) * (2 * j + 1) // ((2 * j + 2 - 2 * i) * (2 * j + 1 - 2 * i))
            j += 1
    dt = time.time() - t0
    print(f"crosscheck per-pair scan: visited={visited} pairs, runtime={dt:.2f}s")
    print(f"crosscheck EEES cleared: {total_E}, newly cleared: {total_new}")
    return total_E, total_new

if __name__ == "__main__":
    JE, JK, tE, tNew = main()
    cE, cNew = crosscheck(JE, JK)
    assert (cE, cNew) == (tE, tNew), "MISMATCH between binary search and per-pair scan"
    print("crosscheck: AGREES with binary search")
    # compare J_E against pairpass.json cleared_js_by_i, if present
    try:
        with open("/home/hatch/workspace/math-hunt/erdos-699/pairpass.json") as f:
            pp = json.load(f)
        cj = pp["cleared_js_by_i"]
        # cleared_js_by_i format check
        mism = 0
        checked = 0
        for i in range(1, IMAX + 1):
            lst = cj[str(i)] if isinstance(cj, dict) else cj[i - 1]
            if isinstance(lst, list):
                jmax_pp = max(lst) if lst else None
            else:
                jmax_pp = lst
            checked += 1
            if jmax_pp != JE[i]:
                mism += 1
                if mism <= 5:
                    print(f"  J_E mismatch at i={i}: mine={JE[i]} pairpass={jmax_pp}")
        print(f"pairpass.json comparison: checked {checked} values of i, mismatches={mism}")
        print(f"pairpass.json header: pairs_fully_cleared={pp.get('pairs_fully_cleared')}, pairs_considered={pp.get('pairs_considered')}")
    except FileNotFoundError:
        print("pairpass.json not found; comparison skipped")
