# Prover B1 (independent) — Strategy S1 formalized: the Kummer small-part bound

**Author:** Prover B1, Erdős #699 proof campaign. This document formalizes
Strategy S1 (`strategies/S1.md`) into complete proofs with numbered lemmas.
It was written independently of the other prover's work. All computations
reported as "exact" were performed by B1's own code in exact integer
arithmetic (Python standard library only); the counting code is reproduced
in Appendix A and saved alongside this file as `P-B1_count.py`.

## 0. Setting, notation, and what is taken as given

Throughout, $1 \le i < j \le n/2$ are integers, $C(a,b) = \binom{a}{b}$, and
$C(n,i) = u\,v$ is the factorization of $C(n,i)$ in which $u$ is supported
on primes $< i$ and $v = V_i(n)$ is supported on primes $\ge i$; explicitly
$$u = \prod_{p < i} p^{v_p(C(n,i))}, \qquad v = \prod_{p \ge i} p^{v_p(C(n,i))}.$$
A **counterexample** is a triple $(n,i,j)$ in the range above with
$\gcd(v, C(n,j)) = 1$. The conjecture (#699) asserts there are none.

$\pi(x)$ is the prime-counting function. For a prime $p$ and $n \ge 1$,
$\lfloor \log_p n \rfloor$ is defined *integrally* as the largest integer
$e \ge 0$ with $p^e \le n$ (no real logarithm is needed), and
$$q_p(n) := p^{\lfloor \log_p n \rfloor}, \qquad
U^\sharp(n,i) := \prod_{p<i} q_p(n), \qquad
U(n,i) := n^{\pi(i-1)},$$
$$F_i(n) := \frac{C(n,i)}{U(n,i)} = \frac{C(n,i)}{n^{\pi(i-1)}}, \qquad
G_i(n) := \frac{C(n,i)}{U^\sharp(n,i)}.$$
Products over the empty set of primes are $1$; in particular
$U^\sharp(n,1) = U^\sharp(n,2) = U(n,1) = U(n,2) = 1$, since there is no
prime $< 2$ and $\pi(0) = \pi(1) = 0$.

The inputs taken from Phase 0 are: the key lemma (proved again below as
Lemma B1.1, so in fact nothing is taken on trust), the Phase 0 / EEES78
reduction used *only* as a comparison in Theorem B1.12, and the completed
sweep fact that no counterexample exists with $n \le 10000$ (used only in
Theorem B1.12). The reduction, closures, and barrier of this document
(Lemmas B1.2–B1.11) use **neither EEES78 nor the sweep**.

---

## 1. The key lemma and the Kummer bound

**Lemma B1.1 (key lemma).** If $d \mid C(n,i)$ and $\gcd(d, C(n,j)) = 1$,
then $d \mid C(j,i) = C(j, j-i)$. Consequently a counterexample satisfies
$$v \mid C(j, j-i), \qquad v \le C(j, j-i), \qquad C(n,i) \le u \cdot C(j, j-i).$$

*Proof.* The identity $C(n,i)\,C(n-i, j-i) = C(n,j)\,C(j,i)$ holds because
both sides equal $n! / (i!\,(j-i)!\,(n-j)!)$: the left side is
$\frac{n!}{i!(n-i)!} \cdot \frac{(n-i)!}{(j-i)!(n-j)!}$ and the right side
is $\frac{n!}{j!(n-j)!} \cdot \frac{j!}{i!(j-i)!}$. (Combinatorially: choose
an $i$-subset of $[n]$ and then a disjoint $(j-i)$-subset.) Since
$d \mid C(n,i)$, $d$ divides the left side, hence divides
$C(n,j)\,C(j,i)$; since $\gcd(d, C(n,j)) = 1$, Euclid's lemma gives
$d \mid C(j,i)$, and $C(j,i) = C(j, j-i)$ by symmetry. For a
counterexample, apply this with $d = v$: $v \mid C(n,i)$ by definition and
$\gcd(v, C(n,j)) = 1$ by assumption, so $v \mid C(j,j-i)$; both sides are
positive integers, so $v \le C(j, j-i)$, and $C(n,i) = uv \le
u \cdot C(j, j-i)$. $\square$

**Lemma B1.2 (L-K; Kummer prime-power bound, sharp form).** For every
prime $p$ and $1 \le i \le n$,
$$p^{v_p(C(n,i))} \le q_p(n) = p^{\lfloor \log_p n \rfloor} \le n.$$

*Proof.* Legendre's formula applied to $C(n,i) = n!/(i!(n-i)!)$ gives
$$v_p(C(n,i)) = \sum_{e \ge 1} \Big( \lfloor n/p^e \rfloor
- \lfloor i/p^e \rfloor - \lfloor (n-i)/p^e \rfloor \Big).$$
Each summand lies in $\{0,1\}$: writing $x = i/p^e$ and $y = (n-i)/p^e$, so
$x + y = n/p^e$, we have $\lfloor x \rfloor + \lfloor y \rfloor \le
\lfloor x+y \rfloor \le \lfloor x \rfloor + \lfloor y \rfloor + 1$, because
$x + y = \lfloor x\rfloor + \lfloor y\rfloor + \{x\} + \{y\}$ with
$\{x\} + \{y\} < 2$. Each summand vanishes for $p^e > n$: then
$\lfloor n/p^e \rfloor = 0$, and $0 \le i, n-i \le n < p^e$ forces the other
two floors to be $0$ as well. Hence the sum has at most
$\#\{e \ge 1 : p^e \le n\} = \lfloor \log_p n \rfloor$ nonzero terms, each
at most $1$, so $v_p(C(n,i)) \le \lfloor \log_p n \rfloor$. Exponentiating
gives $p^{v_p(C(n,i))} \le q_p(n)$, and $q_p(n) \le n$ holds by the integral
definition of $\lfloor \log_p n \rfloor$ ($p^e \le n$ for that $e$).
$\square$

*Remark.* This is Kummer's theorem (the summand at $e$ is the carry
indicator out of the $e$-th base-$p$ digit when $i$ and $n-i$ are added),
but the Legendre argument above is self-contained and quotes nothing.

**Lemma B1.3 (small-part bounds).** For $1 \le i \le n$,
$$u \;\le\; U^\sharp(n,i) \;=\; \prod_{p<i} q_p(n) \;\le\; n^{\pi(i-1)} \;=\; U(n,i),$$
$U^\sharp(\cdot, i)$ is nondecreasing, and $e^{\theta(i-1)} = \prod_{p<i} p
\le U^\sharp(n,i)$, where $\theta(x) = \sum_{p \le x} \log p$.

*Proof.* By definition $u = \prod_{p<i} p^{v_p(C(n,i))}$ (primes $\ge i$ do
not divide $u$). Apply Lemma B1.2 to each factor: $u \le \prod_{p<i}
q_p(n) = U^\sharp(n,i)$. Each $q_p(n) \le n$ and there are exactly
$\pi(i-1)$ primes $< i$, so $U^\sharp(n,i) \le n^{\pi(i-1)} = U(n,i)$. Each
$q_p(\cdot)$ is a nondecreasing step function of $n$, hence so is the
product $U^\sharp(\cdot, i)$. Finally, if $p < i \le n$ then $p \le n$, so
$\lfloor \log_p n \rfloor \ge 1$ and $q_p(n) \ge p$; multiplying over
$p < i$ gives $U^\sharp(n,i) \ge \prod_{p<i} p = e^{\theta(i-1)}$.
$\square$

---

## 2. The $\pi$ bound and monotonicity of $F_i$

**Lemma B1.4 ($\pi(i-1) \le i/2$ for all $i \ge 1$).** For every integer
$i \ge 1$, $\pi(i-1) \le i/2$. Equality holds exactly for $i \in \{4,6,8\}$.

*Proof.* For $i \le 2$, $\pi(i-1) = \pi(0)$ or $\pi(1)$ equals $0 \le i/2$.
Let $i \ge 3$. Every prime $\le i-1$ is either $2$ or an odd integer in
$[3, i-1]$. The odd integers in $[3, i-1]$ are exactly the numbers
$2k+1$ with $k \ge 1$ and $2k+1 \le i-1$, i.e. $1 \le k \le (i-2)/2$; there
are $\lfloor (i-2)/2 \rfloor$ of them. Therefore
$$\pi(i-1) \;\le\; 1 + \Big\lfloor \frac{i-2}{2} \Big\rfloor
\;\le\; 1 + \frac{i-2}{2} \;=\; \frac{i}{2}.$$
Small cases: $i = 1,2$: $\pi(i-1) = 0$; $i = 3$: $\pi(2) = 1 \le 3/2$;
$i = 4$: $\pi(3) = 2 = 4/2$; $i = 5$: $\pi(4) = 2 \le 5/2$; $i = 6$:
$\pi(5) = 3 = 6/2$; $i = 7$: $\pi(6) = 3 \le 7/2$; $i = 8$: $\pi(7) = 4 =
8/2$; $i = 9$: $\pi(8) = 4 \le 9/2$. (B1 also verified
$\pi(i-1) \le i/2$ computationally for all $i < 5000$: no violations.)

For the equality classification: if $i$ is odd and $\ge 3$, then
$1 + \lfloor (i-2)/2 \rfloor = (i-1)/2 < i/2$, so equality is impossible.
If $i$ is even, equality in the second inequality is automatic, and
equality overall holds iff *every* odd integer in $[3, i-1]$ is prime.
For $i \in \{4, 6, 8\}$ those sets are $\{3\}$, $\{3,5\}$, $\{3,5,7\}$, all
prime. For even $i \ge 10$, $9 \in [3, i-1]$ is odd and composite, so
$\pi(i-1) \le 1 + (\frac{i-2}{2} - 1) = i/2 - 1 < i/2$. Hence equality
holds exactly for $i \in \{4,6,8\}$. $\square$

In particular $\pi(i-1) < i$ for all $i \ge 1$ (for $i \ge 3$,
$\pi(i-1) \le i/2 < i$; for $i \le 2$, $\pi(i-1) = 0 < i$).

**Lemma B1.5 (monotonicity and growth of the crude ratio).** For every
$i \ge 1$, $F_i(n) = C(n,i)/n^{\pi(i-1)}$ is strictly increasing for
$n \ge i$, and $F_i(n) \ge n^{\,i - \pi(i-1)}/i^{\,i} \to \infty$ as
$n \to \infty$.

*Proof.* Write $\pi = \pi(i-1)$; by Lemma B1.4, $\pi \le i/2 \le i$, and
$\pi < i$. The ratio of consecutive values is
$$\frac{F_i(n+1)}{F_i(n)}
= \frac{C(n+1,i)}{C(n,i)} \Big(\frac{n}{n+1}\Big)^{\pi}
= \frac{n+1}{\,n+1-i\,}\Big(\frac{n}{n+1}\Big)^{\pi}, \qquad n \ge i,$$
using $C(n+1,i)/C(n,i) = (n+1)/(n+1-i)$. This ratio exceeds $1$ iff
$(n+1)\,n^{\pi} > (n+1-i)\,(n+1)^{\pi}$, iff (dividing by $(n+1)^{\pi}$,
which is positive)
$$\frac{n^{\pi}}{(n+1)^{\pi-1}} > n+1-i. \tag{$\ast$}$$

*Case $\pi = 0$* (i.e. $i \le 2$): ($\ast$) reads $n+1 > n+1-i$, true
since $i \ge 1$.

*Case $\pi = 1$* (this occurs only for $i = 3$, since $\pi(i-1) = 1$ iff
$i - 1 = 2$): ($\ast$) reads $n > n+1-i$, true since $i = 3 > 1$.

*Case $\pi \ge 2$:* Write
$\frac{n^{\pi}}{(n+1)^{\pi-1}} = n\Big(1 - \frac{1}{n+1}\Big)^{\pi-1}$.
Bernoulli's inequality $(1 + y)^r \ge 1 + ry$ for $y \ge -1$ and integer
$r \ge 1$, applied with $y = -\frac{1}{n+1}$ and $r = \pi - 1 \ge 1$,
gives $\Big(1 - \frac{1}{n+1}\Big)^{\pi-1} \ge 1 - \frac{\pi-1}{n+1}$, hence
$$\frac{n^{\pi}}{(n+1)^{\pi-1}} \;\ge\; n - \frac{n(\pi-1)}{n+1}
\;>\; n - (\pi-1) \;\ge\; n+1-i,$$
where the strict inequality uses $\frac{n}{n+1} < 1$ and $\pi - 1 > 0$,
and the last inequality is $\pi \le i$ (Lemma B1.4 gives the stronger
$\pi \le i/2$). This proves ($\ast$), so $F_i(n+1) > F_i(n)$ in all cases.

For the growth bound, $C(n,i) = \prod_{t=0}^{i-1} \frac{n-t}{i-t} \ge
(n/i)^i$ for $n \ge i$: each factor satisfies $\frac{n-t}{i-t} \ge \frac ni$
because $i(n-t) - n(i-t) = t(n - i) \ge 0$. Hence
$F_i(n) \ge n^{i-\pi}/i^i$, and $i - \pi > 0$ (indeed $i - \pi \ge i/2$
for $i \ge 3$ by Lemma B1.4, and $i - \pi = i$ for $i \le 2$), so
$F_i(n) \to \infty$. $\square$

(B1 also checked strict increase of $F_i$ in exact rational arithmetic
for all $i \le 40$, $i \le n < 300$: no failure.)

**Definition (the Kummer bound $N_K$).** For a pair $(i,j)$, let
$$N_K(i,j) := \max\{ n : F_i(n) \le C(j, j-i) \},$$
with the convention $N_K(i,j) = 2j - 1$ (empty interval) if
$F_i(2j) > C(j, j-i)$ already. This is well defined: by Lemma B1.5
$F_i$ is strictly increasing and tends to infinity, so
$\{n : F_i(n) \le C(j,j-i)\}$ is a (possibly empty above $2j$) initial
interval of integers, bounded above.

---

## 3. Theorem A: the EEES-free finite reduction

**Lemma B1.6 (sawtooth structure of the sharp test).** Let
$G_i(n) = C(n,i)/U^\sharp(n,i)$ and
$\mathrm{Bad}^\sharp(i,j) = \{ n \ge 2j : G_i(n) \le C(j, j-i) \}$. Then:

(a) $G_i(n) \ge F_i(n)$ for all $n$, so $\mathrm{Bad}^\sharp(i,j)$ is
finite and contained in $[2j, N_K(i,j)]$.

(b) $G_i$ is strictly increasing on every interval on which
$U^\sharp(\cdot, i)$ is constant; $U^\sharp(\cdot, i)$ jumps exactly at
integers $n = p^e$ ($p < i$ prime, $e \ge 1$), by the factor $p$ at that
jump. Hence every local minimum of $G_i$ on $[2j, \infty)$ is attained at
$n = 2j$ or at a jump point.

(c) $\mathrm{Bad}^\sharp$ need not be an interval: for $(i,j) = (3,7)$,
$\mathrm{Bad}^\sharp(3,7) = \{16\}$ exactly.

*Proof.* (a) $U^\sharp \le U$ (Lemma B1.3) gives $G_i \ge F_i$; if
$G_i(n) \le C(j,j-i)$ then $F_i(n) \le C(j,j-i)$, so $n \le N_K(i,j)$ by
Definition and Lemma B1.5.

(b) $C(n,i)$ is strictly increasing in $n$ for $n \ge i$ (ratio
$(n+1)/(n+1-i) > 1$), while $U^\sharp(\cdot,i)$ is a nondecreasing step
function (Lemma B1.3) whose factor $q_p(n) = p^{\lfloor\log_p n\rfloor}$
increases, by exactly the factor $p$, precisely when $n$ reaches a power
$p^e$. On an interval where $U^\sharp$ is constant, $G_i$ therefore
inherits strict increase from $C(\cdot, i)$. A local minimum of $G_i$ in
$[2j, \infty)$ is thus the left endpoint of one of these constancy
intervals, i.e. $2j$ itself or a point where some $q_p$ has just jumped,
$n = p^e$.

(c) Exact computation for $(3,7)$: the target is $C(7,4) = 35$, and
$U^\sharp(n,3) = 2^{\lfloor \log_2 n \rfloor}$ (the only prime $< 3$ is
$2$). For $n \ge 17$, $G_3(n) \ge F_3(n) \ge F_3(17) = C(17,3)/17 =
680/17 = 40 > 35$ by Lemma B1.5, so no $n \ge 17$ is bad. The remaining
candidates: $G_3(14) = 364/8 = 45.5 > 35$; $G_3(15) = 455/8 = 56.875 >
35$; $G_3(16) = 560/16 = 35 \le 35$. Hence
$\mathrm{Bad}^\sharp(3,7) = \{16\}$, a singleton, not an interval
containing its left endpoint. $\square$

**Theorem B1.7 (T-A; EEES-free finite reduction, no exceptions).** If
$(n,i,j)$ is a counterexample, then
$$C(n,i) \;\le\; U^\sharp(n,i)\, C(j, j-i), \qquad\text{i.e.}\qquad
n \;\in\; \mathrm{Bad}^\sharp(i,j) \;\subseteq\; [2j,\; N_K(i,j)].$$
Hence each pair $(i,j)$ requires only finitely many direct checks, with
no EEES78 input and no exception list. Unconditionally,
$n \le N_K(i,j)$ for any counterexample; when the EEES78 hypothesis is
also available (and $(n,i)$ is not one of its 12 exceptions), a
counterexample satisfies $n \le \min(N_K(i,j), N(i,j))$.

*Proof.* Lemma B1.1 gives $C(n,i) \le u \cdot C(j, j-i)$ for a
counterexample; Lemma B1.3 bounds $u \le U^\sharp(n,i)$; this is
$G_i(n) \le C(j, j-i)$, i.e. $n \in \mathrm{Bad}^\sharp(i,j)$, and
Lemma B1.6(a) gives the containment in $[2j, N_K(i,j)]$. $\square$

---

## 4. Theorem B: unconditional all-$n$ closures

**Definition ("closed").** A pair $(i,j)$ (or a family of pairs) is
**closed** (by this route) if the argument shows that *no* $n$ with
$i < j \le n/2$ can make $(n,i,j)$ a counterexample: the pair is settled
for all $n$ simultaneously, using only Lemmas B1.1–B1.6, with no EEES78
input, no sweep, and no enumeration beyond the explicit endpoint
arithmetic displayed in the proof.

**Theorem B1.8 (T-B; all-$n$ closures in the open region).** The
following pairs with $j > 3i/2$ are closed for all $n$ by size alone:
(1) $i = 1$, every $j$; (2) $i = 2$, every $j$; (3) $(i,j) = (3,5)$ by
the crude bound; (4) $(i,j) = (3,6)$ by the sharpened bound.

*Proof.* (1) $i = 1$: there are no primes $< 1$, so $u = 1$ and
$v = C(n,1) = n$. By Lemma B1.1 a counterexample would need
$v \mid C(j, i) = C(j,1) = j$, in particular $n = v \le j$; but
$n \ge 2j > j$, contradiction. (Remark: S1's proof of this item displays
the target as $C(j,0) = 1$; the correct target from Lemma B1.1 is
$C(j, j-i) = C(j, j-1) = j$. The displayed $C(j,0)$ appears to be a slip
in S1. It does not affect the conclusion, which follows from $n \ge 2j >
j$ as shown; B1 flags it here as a minor discrepancy in S1's text, not
in its result.)

(2) $i = 2$: there is no prime $< 2$, so again $u = 1$ and
$v = C(n,2)$. A counterexample would need, by Lemma B1.1,
$C(n,2) \le C(j, j-2) = C(j,2)$. But $n \ge 2j > j$ and $C(\cdot, 2)$ is
strictly increasing, so $C(n,2) \ge C(2j,2) = j(2j-1) > j(j-1)/2 =
C(j,2)$, contradiction. (In fact (1) and (2) close every $j$, not only
$j > 3i/2$.)

(3) $(3,5)$, crude bound: the target is $C(5, 5-3) = C(5,2) = 10$, and
admissible $n$ satisfy $n \ge 2j = 10$. Now $\pi(2) = 1$, so
$$F_3(10) = \frac{C(10,3)}{10^{1}} = \frac{120}{10} = 12 > 10.$$
By Lemma B1.5, $F_3(n) \ge F_3(10) = 12 > 10$ for all $n \ge 10$, and
$G_3(n) \ge F_3(n)$ (Lemma B1.6(a)); hence
$\mathrm{Bad}^\sharp(3,5) = \varnothing$ (equivalently $N_K(3,5) = 9 <
2j$), so no counterexample exists for any $n$.

(4) $(3,6)$, sharp bound: the target is $C(6,3) = 20$, admissible
$n \ge 12$. The crude bound does *not* suffice: $F_3(12) = 220/12 \le
20$, i.e. $12 \in \{n : F_3(n) \le 20\}$. Use $U^\sharp$ instead: for
$i = 3$, $U^\sharp(n,3) = 2^{\lfloor\log_2 n\rfloor}$, which equals $8$
on $[12, 15]$. On that interval $G_3$ is increasing (Lemma B1.6(b)) and
$$G_3(12) = \frac{C(12,3)}{8} = \frac{220}{8} = 27.5 > 20,$$
so no $n \in [12,15]$ is bad. For $n \ge 16$,
$G_3(n) \ge F_3(n) \ge F_3(16) = C(16,3)/16 = 560/16 = 35 > 20$ by
Lemma B1.5. Hence $\mathrm{Bad}^\sharp(3,6) = \varnothing$: closed for
all $n$. $\square$

**Remark (sharpness at $(3,7)$; the bound can be attained).** The pair
$(3,7)$ is *not* closed by size: by Lemma B1.6(c),
$\mathrm{Bad}^\sharp(3,7) = \{16\} \ne \varnothing$. At $n = 16$ the
Kummer bound is exactly attained: $v_2(C(16,3)) = 4$ (Legendre:
$\lfloor 16/2\rfloor - \lfloor 3/2 \rfloor - \lfloor 13/2 \rfloor + \lfloor
16/4 \rfloor - \lfloor 3/4 \rfloor - \lfloor 13/4 \rfloor + \lfloor 16/8
\rfloor - 0 - \lfloor 13/8 \rfloor + \lfloor 16/16 \rfloor = (8-1-6) +
(4-0-3) + (2-0-1) + (1-0-0) = 4$), so $u = 2^4 = 16 = U^\sharp(16,3) =
U(16,3)$ and $C(16,3) = 560 = 16 \cdot 35 = U^\sharp \cdot C(7,4)$ with
equality. The pair is nevertheless true: the single remaining candidate
gives $\gcd(v, C(16,7)) = \gcd(35, 11440) = 5 > 1$ (a direct check,
already inside the $n \le 10000$ sweep). This equality case is the
concrete obstruction showing that no argument using only the size of
$u$ can close $(3,7)$.

---

## 5. The diagonal barrier: Proposition B′ and Theorem C

The reduction of Theorem B1.7 is strong far from the diagonal $j \approx
ci$ and weak near it. This section proves that the weakness is a
*limitation of the route itself*, not of its execution: no bound on $u$
with $\log U / i \to 1$ can close ratios $c > c^\ast = 1.3672\ldots$, and
in particular neither the crude nor the sharpened Kummer bound can prove
$j \le 3i/2$ for large $i$, nor any $c > 3/2$.

**Lemma B1.9 (entropy estimates).** Let
$h(p) = -p \log p - (1-p)\log(1-p)$ (natural log, $h(0) = h(1) = 0$).

(i) $\log C(N,K) = N\, h(K/N) + O(\log N)$ uniformly in $0 \le K \le N$
as $N \to \infty$ (Stirling's formula
$\log m! = m \log m - m + O(\log m)$ applied to the three factorials).

(ii) For fixed $i$, $\log C(2j, i) - \log C(j, i) \to i \log 2$ as
$j \to \infty$.

(iii) Define, for $c \ge 1$,
$\Delta(c) := 2c\, h\!\big(\tfrac{1}{2c}\big) - c\, h\!\big(\tfrac1c\big)$.
Then $\Delta$ is continuous on $[1,\infty)$, strictly decreasing, with
$\Delta(1) = 2\log 2 = 1.386294\ldots$, $\Delta(3/2) =
0.954771\ldots$, $\Delta(2) = 0.863046\ldots$, and
$\Delta(c) \to \log 2$ as $c \to \infty$. The equation $\Delta(c) = 1$
has a unique root $c^\ast \in (1.3672, 1.3673)$; in particular
$c^\ast = 1.3672\ldots < 3/2$.

*Proof.* (i) is the standard consequence of Stirling's formula; the
$O(\log N)$ error absorbs the $\frac12\log$ terms and the boundary
conventions $h(0) = h(1) = 0$.

(ii) $\dfrac{C(2j,i)}{C(j,i)} = \prod_{t=0}^{i-1} \dfrac{2j - t}{j - t}$,
a product of $i$ factors each tending to $2$ as $j \to \infty$ with $i$
fixed; hence the ratio tends to $2^i$ and its log to $i \log 2$.

(iii) Expand the entropies. For $c > 1$,
\begin{align*}
2c\, h\!\big(\tfrac{1}{2c}\big)
&= -\log\tfrac{1}{2c} - (2c-1)\log\tfrac{2c-1}{2c}
= 2c \log(2c) - (2c-1)\log(2c-1),\\
c\, h\!\big(\tfrac1c\big)
&= -\log\tfrac1c - (c-1)\log\tfrac{c-1}{c}
= c\log c - (c-1)\log(c-1),
\end{align*}
(with $(c-1)\log(c-1)$ read as $0$ at $c = 1$), so
$$\Delta(c) = 2c\log(2c) - (2c-1)\log(2c-1) - c\log c + (c-1)\log(c-1),$$
which is continuous on $[1,\infty)$ and gives $\Delta(1) = 2\log 2$.
Differentiating term by term on $(1, \infty)$:
$$\Delta'(c) = \big[2\log(2c) + 2\big] - \big[2\log(2c-1) + 2\big]
- \big[\log c + 1\big] + \big[\log(c-1) + 1\big]
= \log \frac{4c(c-1)}{(2c-1)^2}.$$
Since $4c(c-1) = 4c^2 - 4c < 4c^2 - 4c + 1 = (2c-1)^2$, the logarithm is
negative: $\Delta'(c) < 0$ on $(1,\infty)$, so $\Delta$ is strictly
decreasing. For the limit, regroup:
$2c\log(2c) - (2c-1)\log(2c-1) = \log(2c) + (2c-1)\log\big(1 +
\frac{1}{2c-1}\big)$ and similarly
$c \log c - (c-1)\log(c-1) = \log c + (c-1)\log\big(1+\frac{1}{c-1}\big)$,
so $\Delta(c) = \log 2 + A(2c-1) - A(c-1)$ with
$A(m) = m \log(1 + 1/m) \to 1$ as $m \to \infty$ (since
$\log(1+t)/t \to 1$ as $t \to 0^+$). Hence $\Delta(c) \to \log 2 =
0.693147\ldots < 1 < 2\log 2 = \Delta(1)$, and strict decrease gives a
unique root $c^\ast$ of $\Delta(c) = 1$. Numerically (evaluated by B1
in 50-digit arithmetic): $\Delta(1.3672) = 1.0000076 > 1$ and
$\Delta(1.3673) = 0.9999672 < 1$, so $c^\ast \in (1.3672, 1.3673)$;
$\Delta(3/2) = 0.954771\ldots$ and $\Delta(2) = 0.863046\ldots$ by the
same evaluation. $\square$

**Proposition B1.10 (B′; nothing else closes at the left endpoint).**
(a) For $i = 3$, both margins at the left endpoint tend to $-\infty$:
$R(3,j) := \log F_3(2j) - \log C(j, j-3) \to -\infty$ and
$R^\sharp(3,j) := \log G_3(2j) - \log C(j, j-3) \to -\infty$ as
$j \to \infty$. Hence $\mathrm{Bad}^\sharp(3,j) \ne \varnothing$ for all
sufficiently large $j$.

(b) Exact computation (B1, integer arithmetic): $R^\sharp(3,j) < 0$ for
every $8 \le j \le 2000$ (at $j = 7$ the unique bad point is instead
$n = 16$, Lemma B1.6(c)); and for every $4 \le i \le 60$ and every open
pair $3i/2 < j \le 2000$ (111,278 pairs), $R^\sharp(i,j) < 0$, the
closest approach being $R^\sharp(7,11) \approx -0.3316$ (the sign in
every case was decided by the exact integer comparison
$C(2j,i) < C(j,i)\,U^\sharp(2j,i)$; the decimal is reported only as a
measure of closeness). Consequently no pair with $3 \le i \le 60$ in
this range is closed at the left endpoint $n = 2j$ even by the
sharpened bound. (This upgrades S1's float-based scan V1 to exact
arithmetic in the stated range.)

*Proof of (a).* By Lemma B1.9(ii) with $i = 3$,
$\log C(2j,3) - \log C(j,3) \to 3\log 2$, and $C(j, j-3) = C(j,3)$.
For the crude margin subtract $\pi(2)\log(2j) = \log(2j) \to \infty$:
$R(3,j) \to -\infty$. For the sharp margin,
$\log U^\sharp(2j,3) = \lfloor \log_2(2j) \rfloor \log 2 > \log j$
because $2^{\lfloor\log_2(2j)\rfloor} > (2j)/2 = j$; hence
$R^\sharp(3,j) \le (\text{quantity} \to 3\log 2) - \log j \to -\infty$
as well. In both cases $2j \in \mathrm{Bad}^\sharp(3,j)$ eventually
(for the sharp statement note $G_3 \ge F_3$ is *not* what is used here;
the display bounds $R^\sharp$ directly). $\square$

**Theorem B1.11 (Theorem C; the $c^\ast = 1.3672$ diagonal barrier).**
Fix $c > 1$ and let $j = \lfloor ci \rfloor$, $n = 2j$. Then, as
$i \to \infty$,
$$\frac{R(i,j)}{i} \;\longrightarrow\; \Delta(c) - 1, \qquad
\frac{R^\sharp(i,j)}{i} \;\longrightarrow\; \Delta(c) - 1,$$
for both the crude margin $R(i,j) = \log F_i(2j) - \log C(j, j-i)$ and
the sharpened margin $R^\sharp$. In particular, for every $c > c^\ast$
there exists $i_0(c)$ such that no pair $(i, \lfloor ci \rfloor)$ with
$i \ge i_0(c)$ is closed by this route (for such $i$,
$2j \in \mathrm{Bad}^\sharp(i,j)$, so $N_K(i,j) \ge 2j$ and size alone
gives no contradiction). Since $c^\ast = 1.3672\ldots < 3/2$, the route
cannot prove $j \le ci$ for any $c > 3/2$ uniformly in $i$, and cannot
even re-derive the known $j \le 3i/2$ closure for large $i$: the
asymptotic margin at $c = 3/2$ is $\Delta(3/2) - 1 =
-0.045229\ldots$ per unit $i$.

*Proof.* By Lemma B1.9(i) applied with $(N, K) = (2j, i)$ and
$(N, K) = (j, i)$ (using $C(j, j-i) = C(j,i)$, $i/(2j) \to 1/(2c)$,
$i/j \to 1/c$, and continuity of $h$; the floor in $j = \lfloor ci
\rfloor$ perturbs the arguments of $h$ by $O(1/i)$, contributing
$o(i)$):
$$\log C(2j, i) - \log C(j, j-i)
= 2j\, h\!\big(\tfrac{i}{2j}\big) - j\, h\!\big(\tfrac{i}{j}\big) + O(\log i)
= \Delta(c)\, i + o(i).$$
For the crude margin, subtract $\pi(i-1)\log(2j)$: by the prime number
theorem $\pi(i-1) = (1 + o(1))\, i/\log i$ and
$\log(2j) = \log i + O(1)$, so $\pi(i-1)\log(2j) = i\,(1 + o(1))$ and
$R(i,j)/i \to \Delta(c) - 1$. For the sharp margin, Lemma B1.3 gives
$\theta(i-1) \le \log U^\sharp(2j, i) \le \pi(i-1)\log(2j)$; by the prime
number theorem in the form $\theta(x) \sim x$ the left side is
$i\,(1 + o(1))$, and the right side is $i\,(1+o(1))$ as just shown, so
the squeeze gives $\log U^\sharp(2j,i)/i \to 1$ and
$R^\sharp(i,j)/i \to \Delta(c) - 1$ as well. If $c > c^\ast$, Lemma
B1.9(iii) gives $\Delta(c) - 1 < 0$, so both margins are negative for
all large $i$; $R^\sharp(i,j) < 0$ is exactly
$G_i(2j) \le C(j, j-i)$, i.e. $2j \in \mathrm{Bad}^\sharp(i,j)$, so the
pair is not closed by size. $\square$

*Remarks.* (1) The prime number theorem is used *only* in Theorem
B1.11 (the barrier); the reduction (Theorem B1.7), the closures
(Theorem B1.8), and the count (Theorem B1.12 below) are elementary and
exact. (2) *Fixed-$i$ comparison:* for fixed $i$ and $j \to \infty$,
the Kummer condition $C(n,i) \le n^{\pi(i-1)} C(j, j-i)$ with
$C(m,i) \sim m^i/i!$ gives $N_K(i,j) = j^{e(i)}(1 + o(1))$ with
$e(i) = i/(i - \pi(i-1))$, against $N(i,j) \sim \kappa_i j^2$ for EEES.
By Lemma B1.4, $e(i) < 2$ iff $\pi(i-1) < i/2$, which holds for all
$i \ge 3$ except the ties $i \in \{4,6,8\}$ where $e(i) = 2$. Values:
$e(3) = 1.5$, $e(5) = 5/3$, $e(7) = 1.75$, $e(10) = 5/3$,
$e(100) = 4/3$, $e(1000) \approx 1.202$, and $e(i) \to 1$. So for fixed
$i \notin \{4,6,8\}$ the Kummer interval is eventually strictly
shorter than the EEES interval, while near the diagonal Theorem B1.11
reverses the comparison; $\min(N_K, N)$ is the operative combined
bound. This complementarity is exactly what Theorem B1.12 quantifies
at the sweep scale.

---

## 6. Theorem D: the payoff count at the sweep scale (B1's independent recount)

**Lemma B1.12a (prefix structure in $j$).** For fixed $i$, both
$j \mapsto C(j, i)$ and $j \mapsto C(2j, 2(j-i)) = C(2j, 2i)$ are strictly
increasing in $j$ (for $j \ge i$).

*Proof.* $C(j+1, i)/C(j,i) = (j+1)/(j+1-i) > 1$. And
$C(2j, 2(j-i)) = C(2j, 2i)$ by symmetry ($2j - 2(j-i) = 2i$), with
$C(2j+2, 2i)/C(2j, 2i) = \frac{(2j+2)(2j+1)}{(2j+2-2i)(2j+1-2i)} > 1$.
$\square$

Consequently, for each fixed $i$ and the sweep cap $N^\ast = 10000$,
each of the two clearance criteria below holds on a *prefix* of the
$j$-range. Write $T_i := C(10001, i)$ and $U_i := 10001^{\pi(i-1)}$.

*EEES criterion.* $N(i,j) \le 10000$ iff $C(10001, i) \ge C(2j, 2(j-i))$:
indeed $N(i,j) = \max\{n : C(n,i) < C(2j,2(j-i))\}$ and $C(\cdot, i)$ is
strictly increasing, so $N(i,j) \le 10000$ iff the inequality already
fails at $n = 10001$. Define $J_E(i)$ = the largest $j \le 5000$ with
$C(2j, 2i) \le T_i$.

*Kummer criterion.* $N_K(i,j) \le 10000$ iff $F_i(10001) > C(j, j-i)$:
indeed $N_K(i,j) = \max\{n : F_i(n) \le C(j,j-i)\}$ and $F_i$ is
strictly increasing (Lemma B1.5), so $N_K(i,j) \le 10000$ iff
$F_i(10001) > C(j,j-i)$. In exact integer form this is the single
comparison
$$C(j, i) \cdot U_i \;<\; T_i, \qquad\text{equivalently}\qquad
C(j,i) \;\le\; K_i := \Big\lfloor \frac{T_i - 1}{U_i} \Big\rfloor,$$
(the equivalence is the integrality of all quantities: for integers
$a, b, m$ with $m \ge 1$, $a m < b$ iff $a \le \lfloor (b-1)/m \rfloor$).
Define $J_K(i)$ = the largest $j \le 5000$ with $C(j,i) \le K_i$. Both
$J_E(i)$ and $J_K(i)$ are located by exact binary search on the single
threshold ($T_i$ resp. $K_i$); no floating-point number is used
anywhere in the classification.

**Theorem B1.12 (T-D; payoff count, independently recomputed).** Let
$1 \le i \le 1000$, $j > 3i/2$, $2j \le 10000$ (4,249,500 pairs). If
$C(j, j-i) < F_i(10001)$, then $N_K(i,j) \le 10000$, so by Theorem B1.7
no counterexample for this pair has $n > 10000$, and the completed
sweep excludes $n \le 10000$: the pair is fully cleared, with no use of
EEES78. Exactly **328,079** of these pairs satisfy the Kummer criterion
while failing the EEES criterion $N(i,j) \le 10000$; they are newly
cleared. Of them, **318,242** have $i \ge 3$ (the remaining 9,837 have
$i \in \{1,2\}$, families already closed for all $j$ by Theorem B1.8).
The fully cleared total therefore rises from 768,741 to
768,741 + 328,079 = **1,096,820** of the 4,249,500 classified pairs.

*Proof and computation.* The implication is Theorem B1.7 plus Lemma
B1.5 (monotonicity in both directions: $F_i(10001) > C(j,j-i)$ gives
$F_i(n) > C(j,j-i)$ for all $n \ge 10001$, so $N_K(i,j) \le 10000$,
and a counterexample would need $n \le N_K(i,j)$). The count is B1's
own exact computation (Appendix A; code in
`P-B1_count.py`, Python standard library only, no floats):

- For each $i$, $J_E(i)$ and $J_K(i)$ were found by exact binary search
  as in Lemma B1.12a; the newly cleared count for this $i$ is
  $\max\big(0,\; \min(J_K(i), 5000) - \max(J_E(i),\, \lfloor 3i/2
  \rfloor)\big)$, summed over $i$. (Binary-search portion runtime:
  17.8 s on this shared, heavily loaded machine.)
- Totals obtained: open pairs 4,249,500; EEES-cleared 768,741;
  Kummer-cleared (within the open range) 1,096,586; newly cleared
  **328,079**, of which $i \ge 3$: **318,242** and $i \in \{1,2\}$:
  9,837; union $768{,}741 + 328{,}079 = 1{,}096{,}820$. (The union
  exceeds the Kummer total because 234 EEES-cleared pairs are not
  Kummer-cleared; overlap $= 768{,}741 + 1{,}096{,}586 - 1{,}096{,}820 =
  768{,}507$.)
- Independent agreement checks: (i) B1's $J_E(i)$ reproduce
  `pairpass.json` *exactly*: for every $i = 1, \ldots, 1000$ the file's
  cleared list equals $[\lfloor 3i/2 \rfloor + 1, \; J_E(i)]$, total
  768,741 pairs, 0 mismatches (separate exact run, 13.0 s).
  (ii) The saved script `P-B1_count.py` additionally performs a
  per-pair crosscheck: for each $i$ it iterates $j$ upward through the
  open range maintaining $A_j = C(j,i)$ and $B_j = C(2j,2i)$ by the
  exact recurrences $A_{j+1} = A_j (j+1)/(j+1-i)$ and
  $B_{j+1} = B_j (2j+2)(2j+1)/\big((2j+2-2i)(2j+1-2i)\big)$, classifying
  every visited pair by the single exact comparisons $B_j \le T_i$ and
  $A_j \le K_i$ (stopping once $j$ exceeds both $J_E(i)$ and $J_K(i)$,
  after which monotonicity settles all later $j$), and asserts equality
  of the two totals. The full saved script was run end-to-end by B1:
  the assertion held (the crosscheck totals agree), and its own final
  comparison against `pairpass.json` also reported 1,000 values of $i$
  checked, 0 mismatches.

Spot values $(i, J_E(i), J_K(i))$, all computed by B1:
$(3, 112, 465)$, $(5, 142, 253)$, $(10, 199, 255)$, $(11, 209, 355)$,
$(50, 454, 654)$, $(100, 656, 1045)$, $(500, 1597, 1950)$,
$(1000, 2391, 2541)$. For $i \le 30$ the indices with
$J_K(i) \le J_E(i)$ are exactly $\{4, 6, 8, 9, 14, 20\}$ (the
$\pi(i-1)$-jump indices; cf. Lemma B1.4's ties $\{4,6,8\}$).

**Comparison with S1's claims.** Every number agrees with S1 exactly:
328,079 newly cleared; 318,242 with $i \ge 3$; total 1,096,820;
$J_K(100) = 1045$ vs $J_E(100) = 656$; $J_K(1000) = 2541$ vs
$J_E(1000) = 2391$; and all other spot values and the exceptional set
$\{4,6,8,9,14,20\}$ for $i \le 30$. **No numerical discrepancy was
found.** The criterion is sufficient, not necessary: the sharp
sawtooth test (Lemma B1.6) can only add pairs beyond these 328,079.
$\square$

---

## 7. Summary of what is proved, and the one textual discrepancy in S1

- **Lemma B1.2 (L-K):** $p^{v_p(C(n,i))} \le p^{\lfloor\log_p
  n\rfloor} \le n$ for every prime $p$, by Legendre's formula with each
  summand in $\{0,1\}$ vanishing for $p^e > n$; hence $u \le
  U^\sharp(n,i) \le n^{\pi(i-1)}$ (Lemma B1.3).
- **Theorem B1.7 (T-A):** EEES-free, exception-free finite reduction
  $n \in \mathrm{Bad}^\sharp(i,j) \subseteq [2j, N_K(i,j)]$, via the
  strictly increasing $F_i$ of Lemma B1.5 (Bernoulli argument, with
  $\pi(i-1) \le i/2$ proved for all $i \ge 1$ in Lemma B1.4, equality
  exactly at $i \in \{4,6,8\}$; cases $\pi = 0, 1, \ge 2$ handled
  separately). The sharp variant via $G_i$ is rigorous as a
  *containment* (Lemma B1.6(a)) with the sawtooth structure of Lemma
  B1.6(b)–(c); $G_i$ itself is not monotone, and $N_K$ is defined from
  the crude $F_i$ accordingly.
- **Theorem B1.8 (T-B):** all-$n$ closures, no EEES78, no sweep:
  $i = 1$ (all $j$), $i = 2$ (all $j$), $(3,5)$ by the crude endpoint
  check $F_3(10) = 12 > 10 = C(5,2)$, and $(3,6)$ by the sharp checks
  $G_3(12) = 27.5 > 20 = C(6,3)$ on $[12,15]$ and $F_3(16) = 35 > 20$
  beyond. "Closed" is defined in §4. The pair $(3,7)$ provably cannot
  be closed this way (the bound is attained at $n = 16$).
- **Proposition B1.10 / Theorem B1.11 (B′ / Theorem C):** the route's
  proved limitation: $\Delta(c)$ strictly decreasing (explicit
  derivative $\log\frac{4c(c-1)}{(2c-1)^2} < 0$), unique root
  $c^\ast \in (1.3672, 1.3673)$ of $\Delta(c) = 1$,
  $\Delta(3/2) = 0.954771\ldots$, and both margins per unit $i$ tend to
  $\Delta(c) - 1 < 0$ for every $c > c^\ast$; so the route closes no
  ratio $c > 3/2$ (nor $3/2$ itself) for large $i$.
- **Theorem B1.12 (T-D):** B1's independent exact recount gives
  328,079 newly cleared pairs (318,242 with $i \ge 3$), total
  1,096,820, in full agreement with S1 and with `pairpass.json`.

**Discrepancy found (textual, in S1's proof of Theorem B(1), result
unaffected):** S1 writes that for $i = 1$ a counterexample needs
"$n = v \le C(j, 0) = 1$". The key lemma's target is $C(j, j-i) =
C(j, j-1) = j$, not $C(j,0)$. The correct inequality $n = v \le j$
still contradicts $n \ge 2j$, so Theorem B(1) stands; only the
displayed target in S1 is wrong. B1 found no other discrepancy: all
of S1's stated counts, thresholds, spot values, the $(3,7)$ singleton
$\{16\}$, the exceptional indices $\{4,6,8,9,14,20\}$, and the
Proposition B′ scan (which B1 reran in exact arithmetic, §5) check
out exactly.

## Appendix A: B1's counting code

The full code is saved as `P-B1_count.py` next to this document
(Python standard library only; exact integer arithmetic throughout;
the classification of a pair is the single comparison
$C(j,i) \cdot 10001^{\pi(i-1)} < C(10001,i)$, resp.
$C(2j,2i) \le C(10001,i)$, evaluated via the prefix thresholds
$K_i = \lfloor (T_i - 1)/U_i \rfloor$ and $T_i$ of §6). Its essential
core:

```python
import bisect
from math import comb

N1 = 10001  # NSTAR + 1
# PRIMES: sieve up to 1000; pi_of(x) = bisect_right(PRIMES, x)

def largest_j(lo, hi, pred):
    # last j in [lo, hi] with pred(j); pred a prefix predicate
    a, b = lo - 1, hi + 1
    while b - a > 1:
        m = (a + b) // 2
        if m <= hi and pred(m): a = m
        else: b = m
    return a

total_new = total_new_i_ge_3 = total_E = 0
for i in range(1, 1001):
    lo_open = 3 * i // 2 + 1                 # smallest j with j > 3i/2
    T = comb(N1, i)                          # T_i = C(10001, i)
    U = N1 ** pi_of(i - 1)                   # U_i = 10001**pi(i-1)
    Kthr = (T - 1) // U                      # Kummer: C(j,i) <= Kthr
    jE = largest_j(i, 5000, lambda j: comb(2 * j, 2 * i) <= T)
    jK = largest_j(i, 5000, lambda j: comb(j, i) <= Kthr)
    total_E += max(0, min(jE, 5000) - lo_open + 1)
    new = max(0, min(jK, 5000) - max(jE, lo_open - 1)) if jK >= lo_open else 0
    total_new += new
    if i >= 3: total_new_i_ge_3 += new
# prints: total_E = 768741, total_new = 328079, total_new_i_ge_3 = 318242
```

The script's second half is the independent per-pair crosscheck
described in Theorem B1.12 (incremental exact recurrences for
$C(j,i)$ and $C(2j,2i)$, asserting the same totals), followed by the
comparison against `pairpass.json`'s cleared lists.
