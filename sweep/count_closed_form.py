#!/usr/bin/env python3
"""
Closed-form count of the open-region triple index set for Erdos #699.

Usage: python3 count_closed_form.py --nstar 10000 [--nlo 2]

Prints the exact number of triples (n, i, j) with nlo <= n <= nstar,
1 <= i < j <= n/2, j > 3i/2, computed from the arithmetic-series
closed form in counting.py (no sweep machinery involved). Before
printing, the closed form is self-checked against a direct per-n
summation of the defining expression for every n <= 2000.

Deposited 2026-10-28 as the artifact backing the cross-check sentence
in RESULTS.md (review finding H2).
"""
import argparse
import sys

from counting import triples_for_n, triples_upto


def direct_triples_for_n(n):
    """The defining expression, summed literally (independent form)."""
    h = n // 2
    return sum(max(0, h - max(i + 1, (3 * i) // 2 + 1) + 1)
               for i in range(1, h + 1))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--nstar", type=int, default=10000)
    ap.add_argument("--nlo", type=int, default=2)
    a = ap.parse_args()
    for n in range(2, 2001):
        assert triples_for_n(n) == direct_triples_for_n(n), n
    print("self-check: closed form == direct per-n summation "
          "for all n <= 2000")
    total = triples_upto(a.nstar, a.nlo)
    print(f"open-region triples with {a.nlo} <= n <= {a.nstar}: {total}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
