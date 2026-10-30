"""P-E2 companion computations (Python standard library only).

Part 1: exact rational sup of the interval-length function L(alpha)
        on [amin, 13/2] for the truncation K = 5 (m = 1..4),
        by enumeration of critical points alpha = q/m, q/(m+1).
Part 2: assembly of the explicit bound on log u / i and theta_u
        for amin in {4, 7/2, 3} at the stated i0.
Part 3: the constants in the phi_req D-function argument.
Part 4: adversarial empirical test: frontier theta_u sup for
        i <= 500, n in [4i, N(i,2i)], by an incremental sweep in n
        for fixed i (float logs; C(n+1,i)/C(n,i) = (n+1)/(n+1-i),
        only prime factors < i update log u), with every float
        value > 0.33 rechecked in exact integer arithmetic
        (Legendre exponents; u^100 <= C^36 decides theta_u <= 0.36;
        theta itself from Decimal logarithms of the exact integers).
        Results agree with S7's frontier numbers (sup i>=50:
        0.3396 at (378,61); sup i>=100: 0.2918) and with direct
        brute-force checks of individual points.
"""
import math
from fractions import Fraction
from decimal import Decimal, getcontext

# ---------------- Part 1: Lsup by exact critical-point enumeration --------
def L_right(a0, K=5):
    """Right-hand limit of L at a0: active q are m*a0 <= q <= (m+1)*a0."""
    tot = Fraction(0)
    for m in range(1, K):
        for q in range(math.ceil(m * a0), math.floor((m + 1) * a0) + 1):
            if q <= m:
                continue
            t = (Fraction(q) - m * a0) / (q * (q - m))
            if t > 0:
                tot += t
    return tot

def Lsup(lo, hi=Fraction(13, 2), K=5):
    crit = {lo}
    for m in range(1, K):
        for q in range(1, 60):
            for aa in (Fraction(q, m), Fraction(q, m + 1)):
                if lo <= aa <= hi:
                    crit.add(aa)
    vals = sorted(((L_right(a, K), a) for a in crit), reverse=True)
    return vals, len(crit)

# ---------------- Part 2: bound assembly ----------------------------------
def assemble(alpha_min, i0):
    lo = Fraction(alpha_min).limit_denominator(10)
    vals, ncrit = Lsup(lo)
    L = float(vals[0][0])
    L0 = math.log(i0)
    P1 = 0.2 * (L0 + math.log(6.5)) / (L0 - math.log(5) - 1.1)
    S = (7 / float(lo)) * (1 + 1 / 2 + 1 / 3 + 1 / 4)   # sum over intervals of 1/q
    amin = (float(lo) - 1) * i0 / 31                    # min interval left endpoint
    err = 0.006788 * 2 * 6.5 * S / math.log(amin)       # Dusart theta error sum
    flo = float(lo)
    f_lo = flo * math.log(flo) - (flo - 1) * math.log(flo - 1)
    logC = f_lo - math.log(6.5 * i0) / i0               # Robbins lower bound / i
    tot = P1 + L + err
    print(f"alpha>={flo} i0={i0}: Lsup={L:.6f} at alpha0={vals[0][1]} "
          f"(critical points: {ncrit}), P1={P1:.6f}, S<={S:.4f}, "
          f"a_min={amin:.0f}, theta-err={err:.6f}, total log u/i<={tot:.6f}, "
          f"log C/i>={logC:.6f}, theta_u<={tot / logC:.6f}")
    return tot / logC

# ---------------- Part 3: phi_req D constants ------------------------------
def F1(c):
    return c * math.log(c) - (c - 1) * math.log(c - 1)

def F2(c):
    return 2 * c * math.log(2 * c) - (2 * c - 1) * math.log(2 * c - 1)

# ---------------- Part 4: empirical frontier sweep -------------------------
def vp_fact(m, p):
    s = 0
    while m:
        m //= p
        s += m
    return s

def frontier_sup():
    def N_of(i):
        target = math.comb(4 * i, 2 * i)
        lo = 4 * i
        hi = lo + 1
        while math.comb(hi, i) < target:
            hi = lo + (hi - lo) * 2
        a, b = lo, hi
        while b - a > 1:
            m = (a + b) // 2
            if math.comb(m, i) < target:
                a = m
            else:
                b = m
        return a

    Ns = {i: N_of(i) for i in range(1, 501)}
    NMAX = max(Ns.values())
    spf = list(range(NMAX + 1))
    primes = []
    for p in range(2, NMAX + 1):
        if spf[p] == p:
            primes.append(p)
            if p * p <= NMAX:
                for mm in range(p * p, NMAX + 1, p):
                    if spf[mm] == mm:
                        spf[mm] = p
    logp = {p: math.log(p) for p in primes}

    def fac_logs(x):
        out = []
        while x > 1:
            p = spf[x]
            a = 0
            while x % p == 0:
                x //= p
                a += 1
            out.append((p, a))
        return out

    points = []
    for i in range(1, 501):
        N = Ns[i]
        log_u = 0.0  # n = i: C(i,i) = 1
        n = i
        while True:
            if n >= 4 * i:
                logC = math.lgamma(n + 1) - math.lgamma(i + 1) - math.lgamma(n - i + 1)
                points.append((log_u / logC, n, i))
            if n >= N:
                break
            for p, a in fac_logs(n + 1):
                if p < i:
                    log_u += a * logp[p]
            for p, a in fac_logs(n + 1 - i):
                if p < i:
                    log_u -= a * logp[p]
            n += 1
    points.sort(reverse=True)
    print(f"frontier window points (i<=500): {len(points)}, "
          f"max N(i,2i)/i = {max(Ns[i] / i for i in Ns):.4f}")
    for imin in (1, 10, 20, 30, 50, 100, 200):
        sel = [p for p in points if p[2] >= imin]
        print(f"  sup i>={imin}: theta={sel[0][0]:.6f} at (n,i)=({sel[0][1]},{sel[0][2]})")
    viol = [p for p in points if p[0] > 0.36]
    print(f"  float violations of 0.36: {len(viol)}")
    for th, n, i in viol[:20]:
        print(f"    VIOLATION theta={th:.6f} at (n,i)=({n},{i})")
    # exact recheck of every point with float theta > 0.33
    getcontext().prec = 60
    cand = [p for p in points if p[0] > 0.33]
    print(f"  exact recheck of {len(cand)} points with float theta>0.33:")
    exact_bad = 0
    for th, n, i in cand:
        C = math.comb(n, i)
        u = 1
        for p in primes:
            if p >= i:
                break
            u *= p ** (vp_fact(n, p) - vp_fact(i, p) - vp_fact(n - i, p))
        if u ** 100 > C ** 36:
            exact_bad += 1
            print(f"    EXACT VIOLATION of 0.36 at (n,i)=({n},{i})")
        if (th, n, i) in (points[0], [p for p in points if p[2] >= 50][0]):
            print(f"    sup point (n,i)=({n},{i}): theta_exact = "
                  f"{Decimal(u).ln() / Decimal(C).ln()}")
    print(f"  exact violations among rechecked points: {exact_bad}")
    return points

if __name__ == "__main__":
    print("== Part 1+2: bound assembly ==")
    assemble(4, 120_000_000)
    assemble(Fraction(7, 2), 170_000_000)
    assemble(3, 170_000_000)
    print("== Part 3: phi_req constants ==")
    for const, cend in ((0.617, 2.0), (0.58, 1.75)):
        print(f"  D({cend}) = {const}*F2 - F1 = {const * F2(cend) - F1(cend):.6f} "
              f"(F1={F1(cend):.6f}, F2={F2(cend):.6f}, ratio={F1(cend) / F2(cend):.6f})")
    i0 = 120_000_000
    print(f"  phi_req(i0,2i0) by lgamma at i0=120000000: "
          f"{(math.lgamma(2 * i0 + 1) - 2 * math.lgamma(i0 + 1)) / (math.lgamma(4 * i0 + 1) - math.lgamma(i0 + 1) - math.lgamma(3 * i0 + 1)):.8f}")
    print("== Part 4: empirical frontier sweep, i<=500 ==")
    frontier_sup()
