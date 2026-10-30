# Appendix A of Price, "Common Prime Divisors of Binomial Coefficients"
# (GPT 5.6 Sol Pro), transcribed verbatim from the manuscript PDF supplied
# by Dennis 2026-10-29. Exact integer arithmetic only. It enumerates every
# k < 2500 with p = 2k+1 prime, computes the endpoint M_k used in the proof
# of Proposition 3.3 (the central case n = 2j for odd prime index), and
# asserts R_k(M_k) > 1 whenever the range p < m <= M_k is nonempty.
# Expected: 666 checks; best datum (659645433004618405800,
# 572679032824811448900, 9, 19, 3, 91, 54).
from math import comb, isqrt

K0 = 2500
limit = 2 * K0 + 1

prime = [True] * (limit + 1)
prime[0] = prime[1] = False
for q in range(2, isqrt(limit) + 1):
    if prime[q]:
        for z in range(q * q, limit + 1, q):
            prime[z] = False

pi = [0] * (limit + 1)
count = 0
for x in range(limit + 1):
    if prime[x]:
        count += 1
    pi[x] = count


def largest_odd_root(N, e):
    """Largest odd A such that A**e <= N."""
    lo, hi = 0, 1
    while hi**e <= N:
        hi *= 2
    while lo + 1 < hi:
        mid = (lo + hi) // 2
        if mid**e <= N:
            lo = mid
        else:
            hi = mid
    return lo if lo % 2 else lo - 1


checked = 0
factorial = 1  # (k-1)! when k = 1
best = None

for k in range(1, K0):
    if k > 1:
        factorial *= k - 1

    p = 2 * k + 1
    if not prime[p]:
        continue

    e = k - pi[p] + 2
    A = largest_odd_root(p * factorial, e)
    M = (A + 2 * k - 1) // 2

    if M < p + 1:
        continue

    lhs = comb(2 * M, p)
    rhs = comb(M, k + 1) ** 2
    assert lhs > rhs

    datum = (lhs, rhs, k, p, e, A, M)
    if best is None or lhs * best[1] < best[0] * rhs:
        best = datum
    checked += 1

certificate = (
    659645433004618405800,
    572679032824811448900,
    9, 19, 3, 91, 54,
)

assert checked == 666
assert best == certificate
print(checked)
print(best)
