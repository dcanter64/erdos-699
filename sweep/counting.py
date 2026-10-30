"""Exact closed-form counts of open-region triples for Erdos #699.

Definition (matching sweep.py's run_block exactly): for fixed n, the
sweep counts, for each i in 1..n//2, the integers j with
    max(i + 1, (3i)//2 + 1) <= j <= n//2.
Since (3i)//2 + 1 >= i + 1 for every i >= 1 (equality iff i == 1), the
per-(n, i) count is max(0, n//2 - (3i)//2).

triples_for_n sums that over i in O(1) by splitting even and odd i:
  i = 2k   (k >= 1): (3i)//2 = 3k,     term h - 3k,     positive iff k <= (h-1)//3
  i = 2k+1 (k >= 0): (3i)//2 = 3k + 1, term h - 1 - 3k, positive iff k <= (h-2)//3
where h = n//2; both partial sums are arithmetic series.

Deposited 2026-10-28 (Stage 1 fix for review finding H2: the
closed-form cross-check cited in RESULTS.md previously had no
artifact in the folder). Also used by sweep.py's checkpoint loader
to validate per-block counts (review finding H1).
"""


def triples_for_n(n):
    """Exact number of open-region triples (i, j) for this n."""
    h = n // 2
    total = 0
    ke = (h - 1) // 3
    if ke >= 1:
        total += ke * h - 3 * ke * (ke + 1) // 2
    ko = (h - 2) // 3
    if ko >= 0:
        total += (ko + 1) * (h - 1) - 3 * ko * (ko + 1) // 2
    return total


def triples_in_range(lo, hi):
    """Exact number of open-region triples with lo <= n <= hi."""
    return sum(triples_for_n(n) for n in range(lo, hi + 1))


def triples_upto(nstar, nlo=2):
    """Exact number of open-region triples with nlo <= n <= nstar."""
    return triples_in_range(nlo, nstar)
