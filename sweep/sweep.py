#!/usr/bin/env python3
"""
Stage 2 sweep for Erdos Problem #699 (open region j > 3i/2).

Method (independent of the Phase 0 brute force): for each n, build the
prime-support bitmask of C(n,k) for all k <= n/2 incrementally
(C(n,k) = C(n,k-1) * (n-k+1) / k, exponents tracked via an spf sieve).
For a triple (n,i,j): the conjecture FAILS iff
    (support(C(n,i)) restricted to primes >= i)  AND  support(C(n,j)) == 0,
because the primes dividing V_i(n) are exactly the primes >= i dividing
C(n,i). Any flagged triple is re-verified by direct gcd before being
recorded as a counterexample candidate.

Checkpointing: one JSON file per block of n in the checkpoint
directory (default checkpoints/); a block is done iff its file exists
AND passes validation. Safe to kill and rerun.

Loader validation (added 2026-10-28, review finding H1): an existing
checkpoint is trusted only after read_checkpoint confirms that its
internal lo/hi match the block its filename encodes, that its recorded
triple count equals the exact closed-form count for that block
(counting.py), and that its flagged list is a list of in-region
[n, i, j] triples. Any mismatch aborts the run loudly; a checkpoint
that fails validation is never silently accepted.

Usage:
  python3 sweep.py --nstar 10000 --block 100 --workers 2 [--nlo 2]
                   [--ckptdir checkpoints]
(Pre-production validation against direct gcd is validate.py, a
separate script; there is no --validate-direct flag.)
"""
import argparse
import json
import os
import sys
import time
from math import comb, gcd
from multiprocessing import Pool

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from counting import triples_in_range


def build_sieve(n):
    spf = list(range(n + 1))
    for p in range(2, int(n ** 0.5) + 1):
        if spf[p] == p:
            for m in range(p * p, n + 1, p):
                if spf[m] == m:
                    spf[m] = p
    primes = [p for p in range(2, n + 1) if spf[p] == p]
    return spf, primes


class Tables:
    def __init__(self, nstar):
        self.spf, self.primes = build_sieve(nstar)
        self.pidx = {p: t for t, p in enumerate(self.primes)}
        # suffix masks: suff[i] has bits of all primes >= i
        suff = [0] * (nstar + 3)
        acc = 0
        t = len(self.primes) - 1
        for i in range(nstar + 1, 0, -1):
            while t >= 0 and self.primes[t] >= i:
                acc |= (1 << t)
                t -= 1
            suff[i] = acc
        self.suff = suff

    def factor(self, x):
        out = []
        spf = self.spf
        while x > 1:
            p = spf[x]
            a = 0
            while x % p == 0:
                x //= p
                a += 1
            out.append((p, a))
        return out

    def support_masks(self, n):
        """masks[k] = bitmask of primes dividing C(n,k), for k = 0..n//2."""
        exp = {}
        mask = 0
        masks = [0]
        pidx = self.pidx
        for k in range(1, n // 2 + 1):
            for p, a in self.factor(n - k + 1):
                e = exp.get(p, 0) + a
                exp[p] = e
                if e == a:  # was 0
                    mask |= (1 << pidx[p])
            for p, a in self.factor(k):
                e = exp[p] - a
                exp[p] = e
                if e == 0:
                    mask &= ~(1 << pidx[p])
            masks.append(mask)
        return masks


TAB = None


def run_block(args):
    lo, hi = args
    triples = 0
    bad = []
    suff = TAB.suff
    for n in range(lo, hi + 1):
        masks = TAB.support_masks(n)
        half = n // 2
        for i in range(1, half + 1):
            si = masks[i] & suff[i]
            if si == 0:
                # V_i(n) = 1: coprime to everything -> all j are candidates
                start = max(i + 1, (3 * i) // 2 + 1)
                for j in range(start, half + 1):
                    triples += 1
                    bad.append((n, i, j))
                continue
            start = max(i + 1, (3 * i) // 2 + 1)
            for j in range(start, half + 1):
                triples += 1
                if not (si & masks[j]):
                    bad.append((n, i, j))
    return lo, hi, triples, bad


def direct_verify(n, i, j):
    """Independent check: exact gcd(V_i(n), C(n,j)) via math.comb and
    removal of all prime factors < i by repeated division."""
    from math import comb as C, gcd as g
    ci = C(n, i)
    v = ci
    # remove prime factors < i
    x = v
    p = 2
    small_primes = []
    sieve = [True] * (i + 1)
    for p in range(2, i):
        if sieve[p]:
            small_primes.append(p)
            for m in range(p * p, i + 1, p):
                sieve[m] = False
    for p in small_primes:
        while x % p == 0:
            x //= p
    v = x
    return g(v, C(n, j))


def read_checkpoint(path, lo, hi):
    """Load and validate a checkpoint file for block [lo, hi].

    Returns (triples, bad) with bad as a list of (n, i, j) tuples.
    Raises SystemExit on ANY inconsistency (review finding H1): the
    internal lo/hi must match the block the filename encodes, the
    recorded triple count must equal the exact closed-form count for
    the block (counting.triples_in_range), and every flagged entry
    must be a well-formed in-region triple for this block.
    """
    try:
        with open(path) as fh:
            d = json.load(fh)
    except (OSError, json.JSONDecodeError) as e:
        raise SystemExit(f"FATAL: unreadable checkpoint {path}: {e}")
    if not isinstance(d, dict):
        raise SystemExit(f"FATAL: checkpoint {path} is not a JSON object")
    if d.get("lo") != lo or d.get("hi") != hi:
        raise SystemExit(
            f"FATAL: checkpoint {path} internal lo/hi "
            f"({d.get('lo')}, {d.get('hi')}) != filename block ({lo}, {hi})")
    expected = triples_in_range(lo, hi)
    if d.get("triples") != expected:
        raise SystemExit(
            f"FATAL: checkpoint {path} records {d.get('triples')} "
            f"triples; closed-form count for [{lo}, {hi}] is {expected}")
    bad = d.get("bad")
    if not isinstance(bad, list):
        raise SystemExit(f"FATAL: checkpoint {path}: 'bad' is not a list")
    for t in bad:
        if (not isinstance(t, (list, tuple)) or len(t) != 3
                or not all(isinstance(x, int) for x in t)):
            raise SystemExit(
                f"FATAL: checkpoint {path}: malformed flagged entry {t!r}")
        n, i, j = t
        if not (lo <= n <= hi and 1 <= i < j <= n // 2 and 2 * j > 3 * i):
            raise SystemExit(
                f"FATAL: checkpoint {path}: flagged triple {t!r} "
                f"outside block/region")
    return d["triples"], [tuple(x) for x in bad]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--nstar", type=int, default=5000)
    ap.add_argument("--block", type=int, default=100)
    ap.add_argument("--workers", type=int, default=2)
    ap.add_argument("--nlo", type=int, default=2)
    ap.add_argument("--ckptdir", type=str, default="checkpoints",
                    help="checkpoint directory, relative to this "
                         "script's folder unless absolute")
    a = ap.parse_args()

    global TAB
    TAB = Tables(a.nstar)
    ckpt_dir = os.path.join(HERE, a.ckptdir)
    os.makedirs(ckpt_dir, exist_ok=True)

    blocks = []
    lo = a.nlo
    while lo <= a.nstar:
        hi = min(lo + a.block - 1, a.nstar)
        blocks.append((lo, hi))
        lo = hi + 1

    todo = []
    done_triples = 0
    all_bad = []
    for lo, hi in blocks:
        f = os.path.join(ckpt_dir, f"block_{lo:06d}_{hi:06d}.json")
        if os.path.exists(f):
            t, b = read_checkpoint(f, lo, hi)
            done_triples += t
            all_bad.extend(b)
        else:
            todo.append((lo, hi))
    print(f"blocks total {len(blocks)}, already done {len(blocks) - len(todo)}, "
          f"to run {len(todo)}", flush=True)

    t0 = time.time()
    ran_triples = 0
    if todo:
        with Pool(a.workers, initializer=_init, initargs=(a.nstar,)) as pool:
            for lo, hi, triples, bad in pool.imap_unordered(run_block, todo):
                f = os.path.join(ckpt_dir, f"block_{lo:06d}_{hi:06d}.json")
                tmp = f + ".tmp"
                with open(tmp, "w") as fh:
                    json.dump({"lo": lo, "hi": hi, "triples": triples,
                               "bad": bad}, fh)
                os.replace(tmp, f)
                ran_triples += triples
                all_bad.extend(bad)
                print(f"block {lo}-{hi} done: {triples} triples, "
                      f"{len(bad)} flagged, elapsed {time.time() - t0:.0f}s",
                      flush=True)
    total = done_triples + ran_triples
    print(f"TOTAL triples checked (open region, n <= {a.nstar}): {total}")
    print(f"flagged candidates: {all_bad}")
    # Direct-verify every flagged candidate independently
    confirmed = []
    for (n, i, j) in all_bad:
        g = direct_verify(n, i, j)
        print(f"candidate (n={n}, i={i}, j={j}): direct gcd = {g}")
        if g == 1:
            confirmed.append((n, i, j))
    print(f"CONFIRMED counterexamples: {confirmed}")
    with open(os.path.join(HERE, f"sweep_summary_{a.nstar}.json"), "w") as fh:
        json.dump({"nstar": a.nstar, "triples": total,
                   "flagged": all_bad, "confirmed": confirmed}, fh, indent=2)
    return 0


def _init(nstar):
    global TAB
    TAB = Tables(nstar)


if __name__ == "__main__":
    sys.exit(main())
