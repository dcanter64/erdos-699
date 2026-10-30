# Prover D2 (independent) — Strategy S4: Kummer Digit Classification

**Problem (Erdős #699).** For $1 \le i < j \le n/2$, show
$\gcd(V_i(n), \binom{n}{j}) > 1$, where $V_i(n)$ is the part of
$\binom{n}{i}$ supported on primes $\ge i$:
$V_i(n) = \prod_{p \ge i} p^{v_p\binom{n}{i}}$.

**Standing definitions.** A prime $p$ is *good* (for the triple
$(n,i,j)$) if $p \mid \binom{n}{i} \Rightarrow p \mid \binom{n}{j}$,
and *locally bad* if $p \mid \binom{n}{i}$ and
$p \nmid \binom{n}{j}$. A triple $(n,i,j)$ with
$1 \le i < j \le n/2$ is a *counterexample* if
$\gcd(V_i(n), \binom{n}{j}) = 1$, equivalently if every prime
$p \ge i$ dividing $\binom{n}{i}$ is locally bad.

**Background inputs (taken as given, not reproved here).**
(i) Kummer's theorem: $v_p\binom{n}{k}$ equals the number of carries
when $k$ and $n-k$ are added in base $p$.
(ii) Legendre's formula:
$v_p\binom{n}{k} = \sum_{a\ge1}\big(\lfloor n/p^a\rfloor -
\lfloor k/p^a\rfloor - \lfloor (n-k)/p^a\rfloor\big)$.
(iii) EEES78: outside the 12 exception pairs
$(8,3),(9,4),(10,5),(12,5),(21,7),(21,8),(30,7),(33,13),(33,14),
(36,13),(36,17),(56,13)$ (all with $n \le 56$), one has
$V_i(n) > \binom{n}{i}^{1/2}$, i.e. $V_i(n)^2 > \binom{n}{i}$.
(iv) The Phase 0 reduction and the closure of $j \le 3i/2$.

**Notation.** Throughout, $p$ is prime, $1 \le k \le n/2$,
$t = \lfloor n/p \rfloor$, $r = n - tp$ ($0 \le r < p$), and
$k = ap + s$ with $a = \lfloor k/p \rfloor$, $s = k \bmod p$
($0 \le s < p$). For a specific $k \in \{i, j\}$ we write
$a_k = \lfloor k/p \rfloor$, $s_k = k \bmod p$.

This document was written independently of the other prover's draft.
One point of divergence from S4.md is flagged and repaired in
Lemma D2.6 (Remark D2.6.1): the bare inequality pair in S4's $t=2$
statement is necessary but **not** sufficient, so the "equivalently"
there is incorrect as stated; the corrected equivalence is proved
here. Nothing downstream (D2.7, D2.8, D2.11) uses the false direction.

---

## Lemma D2.1 (L0: the two-digit regime, and the bound on $a$)

Assume $p^2 > n$. Then $t < p$, so $n = (t, r)_p$ is a genuine
two-digit base-$p$ expansion, and for every $k \le n/2$,

$$a = \lfloor k/p \rfloor \le \lfloor t/2 \rfloor < p,$$

so $k = (a, s)_p$ is also a two-digit expansion (leading zero
allowed).

*Proof.* $t = \lfloor n/p \rfloor \le n/p < p^2/p = p$, and $t$ is an
integer, so $t \le p-1 < p$; the digits of $n$ are $t$ and $r$, both
in $[0, p)$. For the bound on $a$: $ap \le k \le n/2 = (tp+r)/2$, and
$r < p$ gives $ap < p(t+1)/2$, i.e. $a < (t+1)/2$. If $t = 2m$ then
$a < m + \tfrac12$, so $a \le m = \lfloor t/2 \rfloor$; if
$t = 2m+1$ then $a < m+1$, so $a \le m = \lfloor t/2 \rfloor$. In
either case $a \le \lfloor t/2 \rfloor \le t < p$. $\blacksquare$

*Remark.* The regime $p^2 > n$ includes $t = 0$ (i.e. $p > n$); then
$a = 0$ for all $k \le n/2$ and everything below remains valid, with
the case $s > r$ vacuous (see D2.2).

## Lemma D2.2 (L2: the master two-digit criterion; exponent cap $1$)

Assume $p^2 > n$. For every $k \le n/2$,

$$v_p\tbinom{n}{k} = \mathbf 1[\,s > r\,] \in \{0,1\},$$

i.e. $p \mid \binom{n}{k} \iff (k \bmod p) > (n \bmod p)$, and in
particular $v_p\binom{n}{k} \le 1$.

*Proof (Kummer, digit by digit).* By D2.1, $n = (t, r)_p$ and
$k = (a, s)_p$ with $a \le \lfloor t/2 \rfloor$. We exhibit the
base-$p$ expansion of $n - k$ and count the carries when adding
$k + (n-k)$.

*Case $s \le r$.* Then
$n - k = (t-a)p + (r-s)$ with $0 \le r - s < p$ and
$0 \le t - a < p$ (since $0 \le a \le \lfloor t/2 \rfloor \le t$), so
$n - k = (t-a,\ r-s)_p$. Adding $k + (n-k)$ digit by digit: low
digit $s + (r-s) = r < p$ (no carry); high digit $a + (t-a) = t < p$
(no carry). There are only two digit positions, and the sum is
$n < p^2$, so no further position can carry. Total carries: $0$,
hence $v_p\binom{n}{k} = 0$.

*Case $s > r$.* This case forces $t \ge 1$: if $t = 0$ then
$r = n$ and $s = k \le n/2 < n = r$, contradicting $s > r$. So
$t \ge 1$ and $a \le \lfloor t/2 \rfloor \le t$, with
$t - a - 1 \ge 0$ (for $t = 1$: $a = 0$ and $t - a - 1 = 0$; for
$t \ge 2$: $a \le t/2 \le t-1$). Then
$n - k = (t-a-1)p + (r - s + p)$ with $0 < r - s + p < p$ (because
$-p < r - s < 0$), so $n - k = (t-a-1,\ r-s+p)_p$. Adding: low digit
$s + (r - s + p) = r + p \in [p, 2p)$ (since $0 \le r < p$), which is
exactly one carry and no more; high digit
$a + (t - a - 1) + 1 = t < p$, where the $+1$ is the incoming carry,
so no second carry is generated. Total carries: exactly $1$, hence
$v_p\binom{n}{k} = 1$. $\blacksquare$

*Cross-check (Legendre).* Since $p^2 > n$, every term with $a \ge 2$
in Legendre's sum vanishes ($\lfloor n/p^a \rfloor = 0$, and all
terms are $\ge 0$), so
$v_p\binom{n}{k} = t - a - \lfloor (n-k)/p \rfloor$. From the two
expansions above, $\lfloor (n-k)/p \rfloor = t - a$ if $s \le r$ and
$t - a - 1$ if $s > r$, giving $v_p = 0$ resp. $1$. Same conclusion.
$\blacksquare$

## Lemma D2.3 (L1: every prime $p > j$ is good, no digit hypothesis)

Let $p$ be a prime with $p > j$. Then
$p \mid \binom{n}{i} \Rightarrow p \mid \binom{n}{j}$.

*Proof.* First note $i < j < p$, so both $k = i$ and $k = j$ satisfy
$k < p$. The key step is the following claim, for any $k < p$:

$$v_p\tbinom{n}{k} \ge 1 \iff (n-k,\, n] \text{ contains a multiple of } p. \tag{$\ast$}$$

To prove $(\ast)$, use Legendre's formula. Each summand
$\lfloor n/m \rfloor - \lfloor k/m \rfloor - \lfloor (n-k)/m \rfloor$
(with $m = p^a$) lies in $\{0, 1\}$: indeed
$\lfloor x \rfloor + \lfloor y \rfloor \le \lfloor x+y \rfloor \le
\lfloor x \rfloor + \lfloor y \rfloor + 1$ applied to
$x = k/m$, $y = (n-k)/m$ gives exactly this. In particular every
summand is $\ge 0$.

Since $k < p \le p^a$, $\lfloor k/p^a \rfloor = 0$, so the $a$-th
summand equals
$\lfloor n/p^a \rfloor - \lfloor (n-k)/p^a \rfloor$, which is exactly
the number of multiples of $p^a$ in $(n-k, n]$ (the count of
multiples of $m$ in $(0, x]$ is $\lfloor x/m \rfloor$; subtract).

($\Rightarrow$) If $v_p\binom{n}{k} \ge 1$, some summand equals $1$
(all summands are in $\{0,1\}$), so for some $a \ge 1$ the interval
$(n-k, n]$ contains a multiple of $p^a$, which is a multiple of $p$.

($\Leftarrow$) If $(n-k, n]$ contains a multiple of $p$, the $a = 1$
summand, which counts the multiples of $p$ in $(n-k, n]$, is
$\ge 1$, so $v_p\binom{n}{k} \ge 1$.

Now apply $(\ast)$ with $k = i$ and $k = j$. If
$p \mid \binom{n}{i}$, then $(n-i, n]$ contains a multiple of $p$.
Since $i < j$, $(n-i, n] \subseteq (n-j, n]$, so $(n-j, n]$ contains
a multiple of $p$, and $(\ast)$ gives $p \mid \binom{n}{j}$.
$\blacksquare$

### Stress tests of D2.3 (the cases the brief names)

*Case $p \in (j, n/2]$.* The proof applies verbatim: only $i, j < p$
is used. Several Legendre scales $a \ge 1$ may contribute ($p^a \le n$
is possible), but each summand is in $\{0,1\}$ and the interval
formulation $(\ast)$ is uniform in $a$. Hand-checkable instance:
$(n, i, j, p) = (30, 9, 10, 11)$ with $11 \in (10, 15] = (j, n/2]$:
$v_{11}\binom{30}{9} = \lfloor 30/11 \rfloor - \lfloor 21/11 \rfloor
= 2 - 1 = 1$ and
$v_{11}\binom{30}{10} = \lfloor 30/11 \rfloor - \lfloor 20/11 \rfloor
= 2 - 1 = 1$; the common multiple of $11$ is $22 \in (20, 30]
\subseteq$ both intervals.

*Case $p \in (n/2, n]$.* The proof applies verbatim; here only the
$a = 1$ summand can be nonzero since $p^2 > n$. Instance:
$(n, i, j, p) = (18, 5, 8, 17)$: direct computation (Appendix) gives
$v_{17}\binom{18}{5} = v_{17}\binom{18}{8} = 1$; $17$ itself lies in
$(18-8, 18] \subseteq (18-5, 18]$.

*Case $p > n$ (vacuous).* Then $v_p\binom{n}{k} = 0$ for every $k$
(all Legendre floors vanish; equivalently $(n-k, n] \subseteq (0, n]$
contains no multiple of $p$). The implication's antecedent is false,
so $p$ is good vacuously. Note $(\ast)$ remains true in this case.

*Case $p \le j$ (excluded, and the exclusion is sharp).* The claim
fails in general, already at the boundary $p = j$:
$(n, i, j, p) = (15, 1, 5, 5)$ has $v_5\binom{15}{1} = 1$ but
$v_5\binom{15}{5} = 0$ (since $\binom{15}{5} = 3003$, not divisible
by $5$; Appendix). It also fails strictly inside: the $t=2$ example
$(18, 5, 8, 7)$ of Lemma D2.6 has $7 < j = 8$ locally bad. Hence the
strict hypothesis $p > j$ cannot be weakened to $p \ge j$ or dropped.

## Corollary D2.4 (Cor: a counterexample is supported on $[i, j]$)

If $(n, i, j)$ is a counterexample, then every prime divisor
$p \ge i$ of $\binom{n}{i}$ satisfies $p \le j$, i.e. lies in
$[i, j]$.

*Proof.* Let $p \ge i$ with $p \mid \binom{n}{i}$. Since the triple
is a counterexample, $p \nmid \binom{n}{j}$. If $p > j$, Lemma D2.3
would give $p \mid \binom{n}{j}$, a contradiction. Hence $p \le j$.
$\blacksquare$

This holds for **all** $p$, including $p \le \sqrt n$; the digit
classification below is needed only inside $[i, j]$.

## Lemma D2.5 (L3: $t = 1$ primes are all good)

Assume $p^2 > n$ and $t = 1$, i.e. $p \in (n/2, n]$, $n = (1, r)_p$
with $r = n - p$. Then $p$ is good.

*Proof.* For $k \le n/2 < p$, D2.1 gives $a = \lfloor k/p \rfloor = 0$
(consistently, $\lfloor t/2 \rfloor = 0$), so $s = k$ and by D2.2
$p \mid \binom{n}{k} \iff k > r$. If $p \mid \binom{n}{i}$ then
$i > r$; since $j > i > r$, also $p \mid \binom{n}{j}$. $\blacksquare$

*Remark.* D2.5 is subsumed by D2.3 (as $p > n/2 \ge j$), but the
Kummer proof above is the template for $t \ge 2$, where D2.3 no
longer applies.

## Lemma D2.6 (L4: $t = 2$ classification)

Assume $t = 2$ and $p^2 > n$ (the latter is automatic when
$p \in (n/3, n/2]$ and $n > 9$, since then
$p^2 > n^2/9 > n$; the only $t = 2$ cases with $p^2 \le n$ are
$p = 2$, $n \in \{4, 5\}$, outside the two-digit regime). Write
$n = (2, r)_p$, $r = n - 2p$. Then:

1. For $k < p$: $v_p\binom{n}{k} = 1 \iff k > r$.
2. For $k \ge p$: $v_p\binom{n}{k} = 0$.
3. $p$ is locally bad $\iff r < i < p \le j$.

*Proof.* By D2.1, $a = \lfloor k/p \rfloor \le \lfloor 2/2 \rfloor = 1$
for $k \le n/2$.

(1) If $k < p$ then $a = 0$, $s = k$, and D2.2 gives
$v_p\binom{n}{k} = \mathbf 1[k > r]$.

(2) If $k \ge p$ then $a = 1$; write $k = p + k'$. From
$k \le n/2 = (2p + r)/2 = p + r/2$ we get the key bound
$k' \le r/2$, hence $s = k' \le r/2 \le r$, and D2.2 gives
$v_p\binom{n}{k} = 0$. (Digit check: $k = (1, k')_p$,
$n - k = (1, r - k')_p$, valid since $0 \le k' \le r$; digit sums
$k' + (r - k') = r < p$ and $1 + 1 = 2 < p$; no carry.)

(3) ($\Rightarrow$) Suppose $p$ is locally bad. If $i \ge p$, part
(2) gives $v_p\binom{n}{i} = 0$, contradicting
$p \mid \binom{n}{i}$; so $i < p$, and part (1) gives
$p \mid \binom{n}{i} \iff i > r$, so $r < i < p$. If also $j < p$,
part (1) applied to $j > i > r$ gives $p \mid \binom{n}{j}$,
contradicting local badness; so $p \le j$.
($\Leftarrow$) If $r < i < p \le j$, part (1) gives
$v_p\binom{n}{i} = 1$ and part (2) gives $v_p\binom{n}{j} = 0$.
$\blacksquare$

**The inequality form, stated correctly.** Local badness implies
the pair of inequalities

$$\frac{n-i}{2} < p \le n - j, \tag{$\dagger$}$$

because the two halves are exact rewrites of facts already proved:
$(n-i)/2 < p \iff n - i < 2p \iff r = n - 2p < i$; and
$p \le n - j \iff j \le n - p = p + r \iff j - p \le r$, where
$j - p \le r$ holds since $p \le j \le n/2 = p + r/2$ gives the
stronger $j - p \le r/2$. Hence ($\dagger$) is **necessary**.

**Remark D2.6.1 (a flaw in S4's phrasing, repaired; the bare pair
($\dagger$) is NOT sufficient).** S4.md states the $t=2$ conclusion
with "equivalently $\frac{n-i}{2} < p \le n-j$". Read as an
equivalence between local badness and ($\dagger$) alone, this is
false: ($\dagger$) records only $r < i$ and $j - p \le r$, and
neither inequality sees the conditions $i < p$ and $p \le j$. Two
counterexamples (both with $t = 2$, $p^2 > n$, $1 \le i < j \le n/2$;
verified in the Appendix):

- $(n, i, j, p) = (12, 5, 6, 5)$: $r = 2$, ($\dagger$) reads
  $3.5 < 5 \le 6$, true; but $i = p$, so by part (2)
  $v_5\binom{12}{5} = 0$: $p$ does not even divide $\binom{n}{i}$.
- $(n, i, j, p) = (10, 1, 2, 5)$: $r = 0$, ($\dagger$) reads
  $4.5 < 5 \le 8$, true; but $p = 5 > j = 2$, and indeed
  $v_5\binom{10}{1} = v_5\binom{10}{2} = 1$: $p$ is good (as D2.3
  forces).

The correct equivalence, with the band conditions retained, is

$$p \text{ locally bad} \iff r < i < p \le j
\iff \Big[\tfrac{n-i}{2} < p \le n - j \ \text{and}\ i < p \le j\Big],$$

proved by combining part (3) with the necessity of ($\dagger$)
above (the second $\Leftarrow$ is immediate:
($\dagger$) gives $r < i$, and adjoining $i < p \le j$ yields
part (3)'s condition). A brute-force check for $n \le 150$ (all
$t = 2$, $p^2 > n$) confirms: local badness, $r < i < p \le j$, and
the corrected equivalence agree in every case, while ($\dagger$)
alone does not (Appendix). This repair is local to the $t = 2$
statement: the anatomy theorem D2.8 and the wedge D2.11 below use
only the correct classification (3), never the sufficiency of
($\dagger$). The analogous linking inequalities in D2.7 are stated
there as rewrites of the residue conditions **with the band
condition $a_i < a_j$ retained**, and are correct in that form.

**Worked example.** $(n, i, j, p) = (18, 5, 8, 7)$: $t = \lfloor
18/7 \rfloor = 2$, $r = 18 - 14 = 4$, and $r = 4 < i = 5 < p = 7
\le j = 8$, with $j - p = 1 \le \lfloor r/2 \rfloor = 2$. Direct
computation: $\binom{18}{5} = 8568 = 7 \cdot 1224$ with
$1224 = 7 \cdot 174 + 6$, so $v_7\binom{18}{5} = 1$;
$\binom{18}{8} = 43758 = 7 \cdot 6251 + 1$, so
$v_7\binom{18}{8} = 0$. Thus $7$ is locally bad, exactly as (3)
predicts. (The triple is not a counterexample: e.g. $17 \ge i$
divides both binomials, cf. D2.3's stress test.) $\blacksquare$

## Lemma D2.7 (L5: general $t$ bad-configuration classification)

Assume $p^2 > n$ and $t \ge 1$. Then

$$p \text{ is locally bad} \iff a_i < a_j \ \text{and}\ s_i > r \ge s_j.$$

*Proof.* By D2.1, $a_i \le a_j \le \lfloor t/2 \rfloor$ (monotonicity
of the floor, and $i < j \le n/2$). By D2.2,
$p \mid \binom{n}{i} \iff s_i > r$ and
$p \nmid \binom{n}{j} \iff s_j \le r$.

($\Rightarrow$) Suppose $p$ is locally bad, so $s_i > r \ge s_j$,
in particular $s_i > s_j$. If $a_i = a_j$, then $i < j$ forces
$s_i < s_j$ (same band, smaller number), a contradiction. Since
$a_i \le a_j$, we get $a_i < a_j$.

($\Leftarrow$) If $a_i < a_j$ and $s_i > r \ge s_j$, D2.2 gives
$v_p\binom{n}{i} = 1$ and $v_p\binom{n}{j} = 0$ directly. $\blacksquare$

**Consequences.**

1. **$p \le j$.** $a_i < a_j$ gives $a_j \ge 1$, so
   $j \ge a_j p \ge p$. (Weaker than Corollary D2.4, but obtained
   purely from digits.)
2. **A multiple of $p$ in $(i, j]$.** $a_i < a_j$ holds iff the
   multiple $(a_i + 1)p$ lies in $(i, j]$: indeed
   $(a_i+1)p = a_i p + p > a_i p + s_i = i$ (as $s_i < p$) and
   $(a_i + 1)p \le a_j p \le j$; conversely a multiple of $p$ in
   $(i, j]$ separates the floors $\lfloor i/p \rfloor$ and
   $\lfloor j/p \rfloor$.
3. **Linking inequalities** (exact rewrites of the two residue
   conditions, with $a_i < a_j$ retained, cf. Remark D2.6.1):
   $s_i > r \iff i - a_i p > n - tp \iff n < i + (t - a_i)p$, and
   $s_j \le r \iff j - a_j p \le n - tp \iff j + (t - a_j)p \le n$;
   hence
   $$j + (t - a_j)p \;\le\; n \;<\; i + (t - a_i)p,
   \qquad\text{i.e.}\qquad
   \frac{n - i}{\,t - a_i\,} < p \le \frac{n - j}{\,t - a_j\,},$$
   where both denominators are positive because
   $a_j \le \lfloor t/2 \rfloor < t$ for $t \ge 1$. Equivalently the
   bad prime pins $r$ into the window
   $r \in [s_j, s_i)$, an interval of length
   $s_i - s_j = (a_j - a_i)p - (j - i) \in (0, p)$ determined by
   $i, j, p$.

## Theorem D2.8 (T-S4-A: counterexample anatomy)

Let $1 \le i < j \le n/2$, and let $p \ge i$ be prime with
$p \mid \binom{n}{i}$ and $p \nmid \binom{n}{j}$. Then $p \le j$;
and if moreover $p^2 > n$, then, with $t, r, a_i, a_j$ as above:
$a_i < a_j$, $(i \bmod p) > r \ge (j \bmod p)$,
$v_p\binom{n}{i} = 1$, and
$j + (t - a_j)p \le n < i + (t - a_i)p$.

Consequently, if $(n, i, j)$ is a counterexample, then:

- every prime divisor $p \ge i$ of $\binom{n}{i}$ lies in $[i, j]$;
- every such prime with $p > \sqrt n$ has exponent exactly $1$ in
  $\binom{n}{i}$ and lies in a bad configuration of D2.7;
- writing $V_i(n) = V_i^{\le} \cdot V_i^{>}$ for the parts on primes
  $\le \sqrt n$ and $> \sqrt n$: $V_i^{>}$ is squarefree, composed
  only of bad-configuration primes in $[i, j]$; and
  $V_i^{\le} = 1$ whenever $i > \sqrt n$.

*Proof.* The first assertion is Corollary D2.4 (Lemma D2.3,
contrapositive). Under $p^2 > n$, D2.7 gives $a_i < a_j$ and
$s_i > r \ge s_j$, D2.2 gives $v_p\binom{n}{i} = 1$ (since
$s_i > r$), and Consequence 3 of D2.7 gives the linking
inequalities. For the anatomy: in a counterexample, *every*
$p \ge i$ dividing $\binom{n}{i}$ satisfies
$p \nmid \binom{n}{j}$ by definition of counterexample, so the first
part applies to all of them. For $p > \sqrt n$ (equivalently
$p^2 > n$) the exponent is exactly $1$, so $V_i^{>}$, a product of
distinct primes each in $[i, j]$ by D2.4, is squarefree. If
$i > \sqrt n$ there is no prime in $[i, \sqrt n]$, so the
$\le \sqrt n$ part of $V_i(n)$ is empty and $V_i^{\le} = 1$.
$\blacksquare$

## Lemma D2.9 (primorial bound, elementary)

For every integer $x \ge 1$, $\prod_{p \le x} p \le 4^x$.

*Proof (Chebyshev's induction).* We prove
$P(n) := \prod_{p \le n} p \le 4^n$ for all integers $n \ge 1$ by
strong induction. $P(1) = 1$ and $P(2) = 2 \le 4^2$. Let $n \ge 3$
and assume the bound below $n$. If $n$ is even,
$P(n) = P(n-1) \le 4^{n-1} < 4^n$. If $n = 2m + 1$ is odd ($m \ge 1$),
split $P(2m+1) = P(m+1) \cdot \prod_{m+1 < p \le 2m+1} p$. By
induction $P(m+1) \le 4^{m+1}$. Each prime $p$ with $m + 1 < p \le
2m + 1$ satisfies $v_p\binom{2m+1}{m} = 1$: $p \le 2m+1 < 2p$ (as
$p > m+1$), so $p$ occurs exactly once in $(2m+1)!$ and not at all
in $m!\,(m+1)!$. Hence the product of these distinct primes divides
$\binom{2m+1}{m}$, so it is $\le \binom{2m+1}{m}$. By symmetry
$\binom{2m+1}{m} = \binom{2m+1}{m+1}$, and both terms appear in
$\sum_{k=0}^{2m+1} \binom{2m+1}{k} = 2^{2m+1}$, so
$2\binom{2m+1}{m} \le 2^{2m+1}$, i.e.
$\binom{2m+1}{m} \le 4^m$. Therefore
$P(2m+1) \le 4^{m+1} \cdot 4^m = 4^{2m+1}$. $\blacksquare$

## Lemma D2.10 (binomial lower bound)

For $1 \le i \le n$, $\binom{n}{i} \ge (n/i)^i$.

*Proof.* $\binom{n}{i} = \prod_{s=0}^{i-1} \frac{n-s}{i-s}$, and each
factor satisfies $\frac{n-s}{i-s} \ge \frac{n}{i}$: cross-multiplying
(positive denominators), this is $i(n-s) \ge n(i-s)$, i.e.
$ns \ge is$, i.e. $(n - i)s \ge 0$, true since $s \ge 0$ and
$n \ge i$. Multiplying the $i$ factors gives the claim.
$\blacksquare$

## Theorem D2.11 (T-S4-C: the wedge)

There is no counterexample with

$$i > 256, \qquad 256\,i < n < i^2, \qquad 3i/2 < j < 2i.$$

*Proof.* First, the region is consistent and nonempty: $j < 2i$ and
$n > 256 i$ give $j < 2i < 128 i < n/2$ (for $i \ge 1$), so the
standing hypothesis $j \le n/2$ is automatic; e.g.
$(n, i, j) = (65793, 257, 400)$ lies in the region since
$256 \cdot 257 + 1 = 65793 < 257^2 = 66049$. Also
$(n, i)$ is not an EEES78 exception pair: all 12 exceptions have
$n \le 56$, while here $n > 256 i > 256 \cdot 256 = 65536$. (This,
together with exception exclusion, is the only use of $i > 256$;
the coefficient $256$ in $n > 256 i$ is what the inequality chain
consumes.)

Suppose $(n, i, j)$ in the region were a counterexample. Since
$n < i^2$, $\sqrt n < i$, so **every** prime divisor $p \ge i$ of
$\binom{n}{i}$ satisfies $p > \sqrt n$. By Theorem D2.8,
$V_i(n) = V_i^{>}$ is a product of distinct primes in $[i, j]$, each
to the first power. Hence, by Lemma D2.9,

$$V_i(n) \;\le\; \prod_{i \le p \le j} p \;\le\; \prod_{p \le j} p
\;\le\; 4^j, \qquad\text{so}\qquad V_i(n)^2 \le 16^j.$$

EEES78 (input (iii), applicable by the exception exclusion above)
gives $V_i(n)^2 > \binom{n}{i}$, and Lemma D2.10 gives
$\binom{n}{i} \ge (n/i)^i$. Assemble the chain, using $n > 256 i$
(so $n/i > 256$) and $j < 2i$:

$$\binom{n}{i} \;\ge\; (n/i)^i \;>\; 256^i \;=\; 16^{2i} \;>\;
16^j \;\ge\; V_i(n)^2 \;>\; \binom{n}{i},$$

a contradiction. The equality $256^i = 16^{2i}$ is $256 = 16^2$;
the strict inequality $256^i < (n/i)^i$ uses $n/i > 256$ and
$i > 0$; the strict inequality $16^{2i} > 16^j$ uses $j < 2i$ and
base $16 > 1$. Hence no counterexample exists in the region.
$\blacksquare$

**Exact boundary verification of the constant $256$.** The chain
above is tightest at the boundary $n = 256 i + 1$ (smallest allowed)
and $j = 2i - 1$ (largest allowed). The Appendix script checks, in
exact integer arithmetic (no floating point), for all
$i \in [257, 600]$ at this boundary: $16^{2i} = 256^i$;
$16^{2i-1} < 16^{2i}$; $(256 i + 1)^i > (256 i)^i$ (the integer form
of $(n/i)^i > 256^i$); $256 i + 1 < i^2$ (region nonempty at the
boundary); and the primorial bound $\prod_{p \le j} p \le 4^j$ for
all $j \le 1200$. All checks pass (runtime $< 1$ s).

**Assessment of the claimed Rosser–Schoenfeld improvement to $82$.**
S4.md remarks that the explicit bound $\theta(j) < 1.1\, j$
(Rosser–Schoenfeld) would lower the wedge thresholds to
$n > 82\, i$, $i > 82$. Status in this document: **the
Rosser–Schoenfeld bound is NOT proved here, its exact primary-source
statement was not verified in this pass, and it is NOT used
anywhere above.** What is verified (Appendix) is only the
conditional arithmetic: *if* $\theta(j) \le 1.1\, j$ held for the
relevant $j$, then $V_i(n) \le e^{\theta(j)} < e^{1.1 j}$,
$V_i(n)^2 < e^{2.2 j} < e^{4.4 i}$ (using $j < 2i$), and the exact
rational bound $e^{4.4} < 82$ holds (certified by
$e < \sum_{k=0}^{12} 1/k! + \frac{1}{12 \cdot 12!} < 2.7182818285$
and the exact integer comparison $(e\text{-bound})^{44} < 82^{10}$;
numerically $e^{4.4} \approx 81.4509$), so $(n/i)^i > 82^i >
e^{4.4 i} > V_i(n)^2$ would give the contradiction with $82$ in
place of $256$. The improvement to $82$ is therefore a correct
conditional computation resting on an **unproved (here) analytic
input**: gap, explicitly marked, unused.

---

## Status summary (D2)

**Proved here:** D2.1 (L0), D2.2 (L2, Kummer digit-by-digit plus
Legendre cross-check, exponent cap $1$), D2.3 (L1, full Legendre
interval proof, all named cases stress-tested, sharpness at
$p \le j$ shown), D2.4 (Cor), D2.5 (L3), D2.6 (L4, including
$k' \le r/2$ and the worked example $(18,5,8,7)$), D2.7 (L5, with
$p \le j$ and a multiple of $p$ in $(i, j]$), D2.8 (T-S4-A anatomy),
D2.9 (primorial bound, elementary self-contained proof), D2.10,
D2.11 (T-S4-C wedge, constant $256$ verified exactly at the
boundary).

**Repaired:** S4's $t = 2$ "equivalently $(n-i)/2 < p \le n - j$"
is false as a bare equivalence (Remark D2.6.1, counterexamples
$(12,5,6,5)$ and $(10,1,2,5)$); the corrected equivalence retains
$i < p \le j$. No downstream statement used the false direction.

**Gaps (explicit):**
1. The Rosser–Schoenfeld improvement to $82$ is unproved and unused
   (only its conditional arithmetic is verified).
2. Nothing here controls primes $p \le \sqrt n$ (the multi-digit
   regime: no exponent cap, no band classification); that flank,
   and the regions $j \ge 2i$, $n \le 256 i$, $i \le \sqrt n$, remain
   open, exactly as in S4 §4(c),(d). This document proves the S4
   classification and the wedge, not the full conjecture.

---

## Appendix: verification script (Python stdlib) and recorded output

```python
import time
from fractions import Fraction
from math import factorial
t0 = time.time()

def primes_upto(N):
    s = bytearray(b'\x01') * (N + 1); s[0:2] = b'\x00\x00'
    for i in range(2, int(N**0.5) + 1):
        if s[i]: s[i*i:N+1:i] = bytearray(len(s[i*i:N+1:i]))
    return [i for i in range(N + 1) if s[i]]

def C(n, k):
    num = 1; den = 1
    for s in range(k): num *= n - s; den *= s + 1
    return num // den

def vp_int(m, p):
    e = 0
    while m % p == 0: m //= p; e += 1
    return e

def vp(n, k, p):                      # Legendre, general
    e = 0; pp = p
    while pp <= n:
        e += n//pp - k//pp - (n-k)//pp
        pp *= p
    return e

# (1) Worked example L4 and sharpness / stress examples for L1
c185 = C(18, 5); c188 = C(18, 8)
print("C(18,5) =", c185, " v7:", vp_int(c185, 7),
      " C(18,8) =", c188, " v7:", vp_int(c188, 7))
print("C(15,1) v5:", vp_int(C(15, 1), 5), " C(15,5) =", C(15, 5),
      " v5:", vp_int(C(15, 5), 5), " (p = j = 5 sharpness)")
print("C(18,5) v17:", vp_int(c185, 17), " C(18,8) v17:",
      vp_int(c188, 17), " (p = 17 in (n/2, n], good)")

# (2) Primorial bound, exact, j <= 1200
pr = primes_upto(1200); prod = 1; idx = 0; ok = True
for j in range(1, 1201):
    while idx < len(pr) and pr[idx] <= j: prod *= pr[idx]; idx += 1
    if prod > 4**j: ok = False; break
print("primorial prod_{p<=j} p <= 4^j exact for all j<=1200:", ok)

# (3) Wedge constant 256: exact integer boundary checks, i = 257..600
allok = True
for i in range(257, 601):
    jmax = 2*i - 1; nmin = 256*i + 1
    if 16**(2*i) != 256**i: allok = False; break
    if not (16**jmax < 16**(2*i)): allok = False; break
    if not (nmin**i > (256*i)**i): allok = False; break
    if not (nmin < i*i): allok = False; break
print("wedge boundary exact checks i=257..600:", allok)

# (4) Conditional RS arithmetic: e^{4.4} < 82, exact rational e bound
e_ub = sum(Fraction(1, factorial(k)) for k in range(13)) \
       + Fraction(1, factorial(12) * 12)
print("e <", float(e_ub))
print("e^{44} < (e_ub)^{44} < 82^{10} :", e_ub**44 < 82**10)

# (5) L4 counterexamples to the bare inequality pair, and the
#     brute-force check of bad <=> r<i<p<=j <=> corrected form
for (n, i, j, p) in [(12, 5, 6, 5), (10, 1, 2, 5)]:
    r = n - 2*p
    print((n, i, j, p), "t =", n//p, "r =", r,
          " ineq pair:", (n-i)/2 < p <= n-j,
          " r<i<p<=j:", r < i < p <= j,
          " vp_i:", vp(n, i, p), " vp_j:", vp(n, j, p))

def isprime(p):
    return p > 1 and all(p % d for d in range(2, int(p**0.5) + 1))
viol = []
for n in range(10, 151):
    for p in range(2, n + 1):
        if not isprime(p) or n//p != 2 or p*p <= n: continue
        r = n - 2*p
        for i in range(1, n//2 + 1):
            for j in range(i + 1, n//2 + 1):
                isbad = vp(n, i, p) >= 1 and vp(n, j, p) == 0
                main = (r < i < p <= j)
                corrected = ((n-i)/2 < p <= n-j) and (i < p <= j)
                if isbad != main or isbad != corrected:
                    viol.append((n, i, j, p))
print("L4 brute check n<=150: violations =", len(viol))
print("total time", round(time.time() - t0, 2), "s")
```

Recorded output (this VM, 2026-10-28; total runtime under 4 s, well
under the 1-minute budget):

```
C(18,5) = 8568  v7: 1  C(18,8) = 43758  v7: 0
C(15,1) v5: 1  C(15,5) = 3003  v5: 0  (p = j = 5 sharpness)
C(18,5) v17: 1  C(18,8) v17: 1  (p = 17 in (n/2, n], good)
primorial prod_{p<=j} p <= 4^j exact for all j<=1200: True
wedge boundary exact checks i=257..600: True
e < 2.7182818284601415
e^{44} < (e_ub)^{44} < 82^{10} : True
(12, 5, 6, 5) t = 2 r = 2  ineq pair: True  r<i<p<=j: False  vp_i: 0  vp_j: 0
(10, 1, 2, 5) t = 2 r = 0  ineq pair: True  r<i<p<=j: False  vp_i: 1  vp_j: 1
L4 brute check n<=150: violations = 0
total time 2.08 s
```
