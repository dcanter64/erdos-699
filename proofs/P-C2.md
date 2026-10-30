# Prover C2 (independent) - Strategy S3: large prime factors and prime gaps

**Problem #699.** For $1 \le i < j \le n/2$, $\binom{n}{i}$ and
$\binom{n}{j}$ always share a prime factor $\ge i$.

**Provenance and independence.** This document formalizes Strategy S3
(`strategies/S3.md`) independently: every lemma below is proved from
Legendre's formula and elementary binomial estimates, the external
prime-gap inputs are re-cited and re-verified as far as the sources
allow (Section 4 and the verification register in Section 7), and
every count in Section 6 was recomputed with my own Python-stdlib
code (threshold binary search plus a sieve), not copied from S3 or
from `pairpass.json`. Where my computation or algebra disagrees with
a statement in S3, that is flagged in place and collected in
Section 7. Headline outcome: the corrected count in S3's Theorem C2,
$2{,}891{,}106$, is **confirmed exactly**; one comparative remark in
S3 (the range in which bound B3 is "strongest") is **wrong, in a way
that does not affect any theorem**; one theorem-number attribution
(Axler "Thm 4.1") **could not be verified** from the primary source.

**Established inputs (assumed, not reproved here).**

1. *Phase 0 reduction.* Outside the 12 EEES78 exception pairs
   $(n_0,i_0)$, a counterexample $(n,i,j)$ satisfies
   $\binom{n}{i} < \binom{2j}{2(j-i)}$, hence $2j \le n \le N(i,j)$,
   where
   $$N(i,j) := \max\{n : \binom{n}{i} < \binom{2j}{2(j-i)}\}.$$
2. *EEES78 discharge.* The 12 exception pairs
   $(8,3), (9,4), (10,5), (12,5), (21,7), (21,8), (30,7), (33,13),
   (33,14), (36,13), (36,17), (56,13)$ were checked directly in
   `erdos-699/RESULTS.md`: for every admissible $j$,
   $\gcd(V_{i_0}(n_0), \binom{n_0}{j}) > 1$ (41 triples). So the
   reduction in item 1 may be used for all $n$ once this discharge is
   cited.
3. *Sweep.* No counterexample with $n \le 10000$ exists in the open
   region $j > 3i/2$. Of the $4{,}249{,}500$ pairs with
   $1 \le i \le 1000$, $j > 3i/2$, $2j \le 10000$, exactly $768{,}741$
   are fully cleared ($N(i,j) \le 10000$) and $3{,}480{,}759$ are
   partially covered ($N(i,j) > 10000$). These totals are
   independently reproduced by my threshold computation in
   Section 6.

**Conventions.** Throughout, $1 \le i < j \le n/2$ unless stated
otherwise; $\log$ is natural; $p$ always denotes a prime;
$p_-(n)$ is the largest prime $\le n$ (when one exists) and $p_+(n)$
the next prime after $p_-(n)$. A pair $(i,j)$ is *fully cleared* if
no counterexample $(n,i,j)$ exists for any $n$.

Legendre's formula, used repeatedly:
$v_p\binom{n}{k} = \sum_{e\ge1}\big(\lfloor n/p^e\rfloor -
\lfloor k/p^e\rfloor - \lfloor (n-k)/p^e\rfloor\big)$.

---

## 1. The single-hit lemmas

**Lemma C2.1 (S3 Lemma 1; brief's (a)).**
*If $p$ is prime and $n-j < p \le n$, then
$v_p\binom{n}{j} = 1$; in particular $p \mid \binom{n}{j}$.*

*Proof.* Since $j \le n/2$, $p > n - j \ge n/2$, so
$\lfloor n/p \rfloor = 1$ and $p^2 > n$, killing all $e \ge 2$ terms.
Also $\lfloor j/p \rfloor = 0$ because $j \le n/2 < p$, and
$\lfloor (n-j)/p \rfloor = 0$ because $n-j < p$. Hence
$v_p\binom{n}{j} = 1 - 0 - 0 = 1$. $\square$

**Lemma C2.2 (S3 Lemma 2; brief's (b)).**
*If $p$ is prime and $n-i < p \le n$, then
$v_p\binom{n}{i} = 1$; in particular $p \mid \binom{n}{i}$.*

*Proof.* Identical to Lemma C2.1 with $i$ in place of $j$:
$p > n-i \ge n/2$ gives $\lfloor n/p \rfloor = 1$,
$\lfloor i/p \rfloor = 0$ (as $i < j \le n/2 < p$), and
$\lfloor (n-i)/p \rfloor = 0$. $\square$

**Lemma C2.3 (S3 Lemma 3, corrected; the exact reach of the
mechanism).**
*Let $n/2 < p \le n$ and $1 \le k \le n/2$. Then*
$$p \mid \binom{n}{k} \iff k > n-p,$$
*and in that case $v_p\binom{n}{k} = 1$, otherwise
$v_p\binom{n}{k} = 0$.*

*Proof.* Since $p > n/2$: $\lfloor n/p \rfloor = 1$, all $e \ge 2$
Legendre terms vanish, and $k \le n/2 < p$ gives
$\lfloor k/p \rfloor = 0$. Also $0 \le n-k < n < 2p$, so
$\lfloor (n-k)/p \rfloor$ is $0$ if $n-k < p$ and $1$ if
$n-k \ge p$. Now $n-k < p \iff k > n-p$. Hence
$v_p\binom{n}{k} = 1 - 0 - 0 = 1$ if $k > n-p$, and
$v_p\binom{n}{k} = 1 - 0 - 1 = 0$ if $k \le n-p$. $\square$

Three consequences, in decreasing strength of the interval:

(i) *Common divisors.* If $p \in (n-i, n]$, then $p > n/2$ (as
$p > n-i \ge n/2$), and Lemma C2.3 with $k=i$ applies since
$i > n-p$; with $k=j$ it also applies, either directly ($j>i>n-p$)
or via Lemma C2.1, using the inclusion
$(n-i, n] \subseteq (n-j, n]$, which holds because $j > i$. Hence
$p$ divides **both** $\binom{n}{i}$ and $\binom{n}{j}$, each to the
first power, and $p > n/2 \ge j > i$, so $p \ge i$ with room to
spare: $(n,i,j)$ is not a counterexample.

(ii) *Wasted primes.* If $p \in (n-j, n-i]$, then Lemma C2.3 gives
$p \mid \binom{n}{j}$ (because $j > n-p$) but
$p \nmid \binom{n}{i}$ (because $i \le n-p$). Such a prime is
*"wasted"*: it witnesses the larger coefficient only and can never
serve as the common prime the problem asks for.

(iii) *Invisible primes.* If $n/2 < p \le n-j$, then
$j \le n-p$ and $i \le n-p$, so by Lemma C2.3 $p$ divides **neither**
coefficient.

Together (i)-(iii) say: among primes $> n/2$, the common prime
divisors of $\binom{n}{i}$ and $\binom{n}{j}$ are *exactly* the
primes in $(n-i, n]$. The gap condition in Corollary C2.4 is
therefore the exact reach of this mechanism, not an artifact of the
proof. Common primes $\le n/2$ are invisible to this route
(Legendre exponents there involve genuine carries), which is why
the condition below is sufficient and never necessary.

**The brief's claim (c) is false.** The brief asserted
$(n-j, n] \subseteq (n-i, n]$ and concluded that every prime in
$(n-j, n]$ divides both coefficients. Since $j > i$, the inclusion
runs the other way: $(n-i, n] \subsetneq (n-j, n]$. On the annulus
$(n-j, n-i]$ the conclusion fails by part (ii).

*Counterexample.* $n = 20$, $i = 3$, $j = 9$, $p = 13$. Then
$13 \in (n-j, n] = (11, 20]$ and indeed
$13 \in (n-j, n-i] = (11, 17]$, the wasted annulus. Directly:
$\binom{20}{9} = 167960 = 13 \cdot 12920$, so
$13 \mid \binom{20}{9}$; but $\binom{20}{3} = 1140 = 13\cdot 87 + 9$,
so $13 \nmid \binom{20}{3}$. My code re-verified this and the full
trichotomy of Lemma C2.3 on 3000 random triples
($n \le 200$): 0 violations (Section 6).

**Corollary C2.4 (gap forcing; S3's corrected Corollary).**
*If $(n,i,j)$ is a counterexample, then the interval $(n-i, n]$
contains no prime. Equivalently, $p_-(n) \le n-i$ and the prime gap
straddling $n$ satisfies $p_+ - p_- \ge i+1$.*

*Proof.* If a prime lay in $(n-i, n]$, Lemma C2.3(i) would make it a
common divisor $\ge i$, contradicting counterexample status. For
the gap form: $n - i > n/2 \ge 2$ (using $i < j \le n/2$ and
$n \ge 2j \ge 4$), so a prime $\le n-i$ exists (namely 2 at worst)
and $p_-(n)$, the largest prime $\le n$, equals the largest prime
$\le n-i$; hence $p_-(n) \le n-i$. There is no prime in
$(p_-(n), n]$, so $p_+ \ge n+1$, and
$p_+ - p_- \ge (n+1) - (n-i) = i+1$. $\square$

*Remark on $i = 1$.* Here $(n-i, n] = \{n\}$, which contains a prime
iff $n$ is prime. The route therefore rules out only prime $n$ for
$i = 1$; see the breaking point discussion in Section 5.

---

## 2. A uniform bound on $N(i,j)$

**Lemma C2.5 (auxiliary binomial estimates).**
*(a) For $0 \le K \le N$, $\binom{N}{K} \le (eN/K)^K$ (with the
convention that the case $K=0$ is the trivial bound $1 \le 1$).
(b) For $1 \le i \le n$, $\binom{n}{i} \ge (n/i)^i$.*

*Proof.* (a) For $K \ge 1$:
$\binom{N}{K} = \frac{N(N-1)\cdots(N-K+1)}{K!} \le \frac{N^K}{K!}$,
and $K! \ge (K/e)^K$ because $e^K = \sum_{m\ge0} K^m/m! \ge K^K/K!$.
(b) $\binom{n}{i} = \prod_{t=0}^{i-1} \frac{n-t}{i-t}$, and each
factor satisfies $\frac{n-t}{i-t} \ge \frac{n}{i}$: cross-multiplying
(the denominators are positive), this is $i(n-t) \ge n(i-t)$,
i.e. $nt \ge it$, true since $n \ge i$. $\square$

**Lemma C2.6 (S3 Lemma 4; uniform bound on $N(i,j)$).**
*For all $1 \le i < j$,*
$$N(i,j) \;<\; e^{2} j^{2} / i \;\le\; e^{2} j^{2}.$$

*Proof.* By symmetry of the binomial coefficient,
$\binom{2j}{2(j-i)} = \binom{2j}{2i}$ (since $2j - 2(j-i) = 2i$), so
Lemma C2.5(a) with $N = 2j$, $K = 2i$ gives
$$\binom{2j}{2(j-i)} \le \Big(\frac{e \cdot 2j}{2i}\Big)^{2i}
= (ej/i)^{2i}.$$
Now let $n \ge e^{2}j^{2}/i$. Then $n/i \ge (ej/i)^{2}$, so by
Lemma C2.5(b),
$\binom{n}{i} \ge (n/i)^{i} \ge (ej/i)^{2i} \ge
\binom{2j}{2(j-i)}$.
Hence $\binom{n}{i} \ge \binom{2j}{2(j-i)}$, i.e. $n$ does not
satisfy the defining strict inequality of $N(i,j)$. Since this
holds for *every* $n \ge e^{2}j^{2}/i$, no element of the defining
set reaches the bound, and its maximum satisfies
$N(i,j) < e^{2}j^{2}/i$. The second inequality is $i \ge 1$.
$\square$

*Sharpness remark (from S3, spot-verified).* Stirling's formula
gives $N(i,j) \approx ej^{2}/i$ for $i \ll j$, so the bound loses
only a factor $e$. Exactly, $N(1,j) = j(2j-1) - 1$; my code
confirmed this against exact binary-search values at
$j = 5, 10, 71, 100$ (e.g. $N(1,71) = 10010$).

---

## 3. Theorem A: the table criterion, with exact off-by-one conventions

**Definition.** For real $X$, let
$G(X) := \max\{p_{k+1} - p_k : p_k < X\}$, with $G(X) := 0$ if no
prime is $< X$. Note the strict inequality $p_k < X$: a gap is
counted exactly when its *lower* prime is strictly below $X$. $G$
is nondecreasing in $X$. Concretely, from the first-occurrence
(maximal gap) table: gap $36$ first occurs after the prime $9551$
and the next record, $44$, after $15683$, so
$G(X) = 36$ for $9551 < X \le 15683$ (at $X = 15683$ the prime
$15683$ itself is not $< X$, so its gap is not yet counted);
gap $132$ first occurs after $1357201$ and the next record, $148$,
after $2010733$, so $G(X) = 132$ for $1357201 < X \le 2010733$.
My sieve reproduced both boundary behaviours exactly:
$G(2010733) = 132$ and $G(2010734) = 148$ (Section 6).

**Theorem C2.8 (S3 Theorem A; table criterion).**
*Let $(i,j)$ be any pair with $1 \le i < j$ such that*
$$i \;\ge\; G(N(i,j)).$$
*Then $(i,j)$ is fully cleared: there is no counterexample
$(n,i,j)$ for any $n$.*

*Proof.* Split on $n$.

*Case $n < 2j$:* impossible for a triple in the problem, since
$j \le n/2$.

*Case $2j \le n \le N(i,j)$:* we show $(n-i, n]$ contains a prime;
Lemma C2.3(i) then supplies a common prime divisor $> n/2 \ge j > i$,
so $(n,i,j)$ is not a counterexample. Suppose instead that
$(n-i, n]$ were prime-free. As in Corollary C2.4, $n-i > n/2 \ge 2$,
so $p_- := p_-(n)$ exists and $p_- \le n-i$. The key point is that
this gap is *counted in $G(N(i,j))$*: indeed
$$p_- \;\le\; n - i \;<\; n \;\le\; N(i,j),$$
so $p_- < N(i,j)$ strictly (even when $n = N(i,j)$, the middle
inequality $n - i < n$ is strict). And the next prime satisfies
$p_+ \ge n+1$, because there is no prime in $(p_-, n]$ (none in
$(n-i, n]$ by supposition, and none in $(p_-, n-i]$ by maximality
of $p_-$). Therefore
$$G(N(i,j)) \;\ge\; p_+ - p_- \;\ge\; (n+1) - (n-i) \;=\; i+1
\;>\; i,$$
contradicting the hypothesis $i \ge G(N(i,j))$. Note this is exactly
where the off-by-one conventions interlock: prime-freeness of the
*half-open* interval $(n-i, n]$ of length $i$ forces a gap of
*length at least $i+1$* (the $+1$ comes from $p_+ \ge n+1$, an
integer strictly past $n$), and the gap's lower end is *strictly*
below $N(i,j)$, matching the strict $p_k < X$ in the definition of
$G$. So the hypothesis needed is $i \ge G(N(i,j))$, not
$i > G(N(i,j))$ and not $i \ge G(N(i,j)) - 1$.

*Case $n > N(i,j)$:* excluded by the Phase 0 reduction (Established
input 1), with the EEES78 exception values discharged directly
(Established input 2). If $N(i,j) < 2j$ the middle case is empty and
the conclusion rests on this case alone. $\square$

The force of Theorem C2.8 is that a *single global* number,
$G(N(i,j))$, controls *every* candidate $n$ at once: for each
individual $n$, the gap that prime-freeness at $n$ would force has
lower end $p_-(n) \le n - i < n \le N(i,j)$, hence is one of the
gaps over which the maximum $G(N(i,j))$ is taken. No per-$n$
information is needed.

---

## 4. Theorem B: the explicit-theorem region

**Lemma C2.7 (conversion lemma).**
*Suppose that for some $x_0$, $C > 0$, $m \ge 0$, every real
$x \ge x_0$ admits a prime in $(x,\ x(1 + C/\log^m x)]$ (the same
conclusion holds a fortiori if the source states the interval with
the upper end open). Let $(n,i,j)$ satisfy $n - i \ge x_0$ and*
$$i \;\ge\; \frac{(n-i)\,C}{\log^m (n-i)}.$$
*Then $(n-i, n]$ contains a prime, so $(n,i,j)$ is not a
counterexample.*

*Proof.* Apply the hypothesis at $x = n - i$ (an integer $\ge x_0$).
The prime $p$ produced satisfies $n - i < p$ (the strict lower end
is essential, and is the form in which the sources below state
their results) and
$p \le (n-i)\big(1 + C/\log^m(n-i)\big) = (n-i) +
\frac{(n-i)C}{\log^m(n-i)} \le (n-i) + i = n$.
So $p \in (n-i, n]$, and Lemma C2.3(i) finishes. $\square$

Since $x \mapsto x/\log^m x$ is increasing for $x > e^m$ (its
logarithmic derivative is $1 - m/\log x$ over $x$), the cleaner but
stronger hypothesis $i \ge nC/\log^m n$ also suffices whenever
$n - i > e^m$, which holds in all applications below.

**Theorem C2.9 (S3 Theorem B, restated exactly).**
*There is no counterexample $(n,i,j)$ in any of the following
regions (all $i < j \le n/2$):*

* *(B1) $n - i \ge 396738$ and
  $i \ge \dfrac{n-i}{25\log^2(n-i)}$ (Dusart 2010). In particular
  the clean region
  $\{\, i > n / (25 (\log n)^2),\ n - i \ge 396738 \,\}$ is
  counterexample-free.*
* *(B2) $n - i \ge 468991632$ and
  $i \ge \dfrac{n-i}{5000\log^2(n-i)}$ (Dusart 2018).*
* *(B3) $n - i \ge 6034256$ and
  $i \ge \dfrac{0.087\,(n-i)}{\log^3(n-i)}$ (Axler 2017).*

*Proof.* Each part is Lemma C2.7 applied to the cited explicit
theorem; the inputs are:

| Label | Source | Validity | Prime in |
|---|---|---|---|
| B1 | Dusart 2010, arXiv:1002.0442 | $x \ge 396738$ | $(x,\ x(1 + \frac{1}{25\log^2 x})]$ |
| B2 | Dusart 2018, *Ramanujan J.* 45, Cor. 5.5 | $x \ge 468991632$ | $(x,\ x(1 + \frac{1}{5000\log^2 x})]$ |
| B3 | Axler 2017, arXiv:1703.08032 | $x \ge 6034256$ | $(x,\ x(1 + \frac{0.087}{\log^3 x})]$ |

For the "in particular" clause of B1: the function
$f(x) = x/\log^2 x$ has $f'(x) > 0$ for $x > e^2$, and
$n - i \ge 396738 > e^2$, so
$\frac{n-i}{25\log^2(n-i)} < \frac{n}{25\log^2 n} < i$, which gives
the hypothesis of Lemma C2.7 with $C = 1/25$, $m = 2$. $\square$

**Verification status of the three inputs** (details in Section 7):

* *B1, verified.* The exact statement, threshold $396738$ included,
  appears in two independent secondary sources: the explicit-interval
  table in "Variants on Andrica's Conjecture with and without the
  Riemann Hypothesis", *Mathematics* 2018, 6, 289 (Theorem 6 and
  arXiv:1804.02500v3, eq. (5.1) table), and the Bertrand's postulate
  survey statement "for $x \ge 396738$ there is a prime
  $x < p \le (1 + \frac{1}{25\log^2 x})x$ (Dusart 2010)".
* *B2, verified, including the internal numbering.* The same
  Bertrand survey states verbatim that Dusart's 2018 paper
  (*Explicit estimates of some functions over primes*,
  *Ramanujan J.* 45 (2018), 227-251, DOI 10.1007/s11139-016-9839-4)
  proves in Proposition 5.4 that for $x \ge 89693$ there is a prime
  in $(x, x(1 + 1/\log^3 x)]$, and in Corollary 5.5 that for
  $x \ge 468991632$ there is a prime in
  $(x, x(1 + \frac{1}{5000\log^2 x})]$. Both rows also appear in the
  *Mathematics* 2018 table cited above. (Some bibliographies give
  the year as 2016, the online-first year; the journal issue is
  2018, as S3 cites it.)
* *B3, constants verified secondarily; theorem number unverified.*
  The row $x_0 = 6034256$, $m = 3$, $C = 0.087$, reference
  "Axler 2017, arXiv:1703.08032" appears identically in the
  *Mathematics* 2018 table. I could **not** verify from the primary
  source that this is "Thm 4.1" of Axler's paper: S3's label
  "Thm 4.1" is therefore carried here as *unverified*. The numerical
  content used by B3 (threshold, constant, exponent) is corroborated;
  only the internal theorem number is in doubt. Two further rows of
  S3's Section 3 table that Theorem C2.9 does not use were also
  corroborated in the same source: Trudgian 2014, arXiv:1401.2689,
  $x \ge 2898329$, $C = 1/111$, $m = 2$; and Dusart 2018 Prop. 5.4
  above, $x \ge 89693$, $C = 1$, $m = 3$. The same table contains an
  extra Axler row ($x \ge 1$, $C = 198.2$, $m = 4$) that S3 does not
  list; this does not affect anything here.

**Correction to S3's comparative remark (flagged, theorems
unaffected).** S3 Section 3 says the $m=3$ bounds dominate the
$m=2$ bounds "whenever $\log x < 435$ (Axler vs. Dusart 2018)", and
Section 4 calls B3 "the strongest of the three for $\log n < 435$".
The algebra runs the other way:
$$\frac{0.087}{\log^3 x} \le \frac{1}{5000\log^2 x}
\iff 0.087 \cdot 5000 \le \log x \iff \log x \ge 435.$$
So B3 imposes a *weaker* requirement on $i$ than B2 only when
$\log(n-i) > 435$, i.e. $n - i > e^{435} \approx 10^{189}$; for all
smaller $x$ in range, B2's coefficient is smaller (numerically, at
$\log x = 15$: B1 $1.78\times10^{-4}$, B3 $2.58\times10^{-5}$,
B2 $8.9\times10^{-7}$). B3 does beat B1 throughout its validity
range, since $0.087/\log^3 x \le \frac{1}{25\log^2 x}
\iff \log x \ge 2.175$ and $\log 6034256 \approx 15.6$. This error
is confined to the comparison remark: B1, B2, B3 as *regions* are
each proved above independently of any comparison.

*Remark.* Bertrand's postulate is the degenerate case $C = 1$,
$m = 0$ of Lemma C2.7 and recovers nothing here: it would need
$i \ge n - i$, i.e. $i \ge n/2$, excluded by $i < j \le n/2$.

---

## 5. Theorem C: table closures

**External computational input (tables).** Oliveira e Silva,
Herzog, and Pardi, *Empirical verification of the even Goldbach
conjecture and computation of prime gaps up to $4\cdot10^{18}$*,
*Math. Comp.* 83 (2014), 2033-2060: all prime gaps below
$4\cdot10^{18}$ were computed, and the maximal gap there is $1476$,
first occurring after the prime $1425172824437699411$. Hence
$$G(X) \le 1476 \quad\text{for all } X \le 4\cdot10^{18}.$$
This is an external computational theorem; it is not (and cannot
be) recomputed here. Its bibliographic data and the value $1476$
with its prime were verified against independent compilations
(Section 7). All first-occurrence records *below* $2.2\times10^6$,
in particular every record used in Theorem C2.11, were recomputed
exactly by my own sieve.

**Theorem C2.10 (S3 Theorem C1; infinite family).**
*Every open pair $(i,j)$ with $i \ge 1476$ and
$j \le 7.35\cdot10^{8}$ is fully cleared.*

*Proof.* By Lemma C2.6,
$N(i,j) < e^{2}j^{2}/i \le e^{2}j^{2}$. My arithmetic check:
$e^{2}(7.35\times10^{8})^{2} = 3.9918\times10^{18} < 4\times10^{18}$
(indeed $\sqrt{4\cdot10^{18}/e^{2}} = 7.3576\times10^{8} >
7.35\times10^{8}$). Hence $N(i,j) < 4\cdot10^{18}$, the table input
gives $G(N(i,j)) \le 1476 \le i$, and Theorem C2.8 applies. (Using
the $/i$ in Lemma C2.6 with $i \ge 1476$ would give the much
stronger $N(i,j) < 2.71\times10^{15}$; S3's chain, reproduced here,
does not need it.) $\square$

**Theorem C2.11 (S3 Theorem C2).**
*Every open pair with $132 \le i \le 1000$ and $j \le 5000$ is fully
cleared. In particular, all partially covered pairs with
$132 \le i \le 1000$ (those with $J_i < j \le 5000$, $J_i$ the
sweep's maximal cleared $j$ for this $i$) are now fully cleared;
their number is $2{,}891{,}106$ (independently recomputed,
Section 6).*

*Proof of the clearance.* By Lemma C2.6, for $i \ge 132$ and
$j \le 5000$,
$$N(i,j) \;<\; \frac{e^{2}j^{2}}{i} \;\le\;
\frac{e^{2}\cdot 5000^{2}}{132} \;=\; 1{,}399{,}442.44\ldots
\;<\; 1.40\times10^{6}.$$
By monotonicity of $G$ and my sieve computation
$G(1.40\times10^{6}) = 132$ (the maximal gap with lower end
$< 1.40\times10^{6}$ is the gap $132$ after $1357201$; the next
record, $148$ after $2010733$, has lower end above the bound),
$$G(N(i,j)) \;\le\; 132 \;\le\; i,$$
and Theorem C2.8 applies. Note the argument is uniform: no per-pair
computation is used in the proof. The count is a separate,
enumerative statement, verified in Section 6. $\square$

**Per-pair criterion (S3 Theorem C3, restated).** Any specific pair
with $N(i,j) \le 4\cdot10^{18}$ and $i \ge G(N(i,j))$, with
$N(i,j)$ computed exactly and $G$ read from the record table, is
fully cleared; this is Theorem C2.8 verbatim. S3's example: every
open $(i, 71)$ with $18 \le i \le 47$ satisfies the criterion. My
code confirms this and the surrounding picture: exact
$N(i,71)$ and $G(N(i,71))$ give the criterion holding precisely for
$i \ge 18$ (at $i = 18$: $N = 578$, $G(N) = 18 \le i$; at
$i = 17$: $N = 621$, $G(N) = 18 > i$), while for $i \le 17$,
$N(i,71) \le 10010$ and, excepting $(1,71)$ with $N = 10010$, these
pairs already satisfy $N(i,71) \le 10000$ and were cleared by the
sweep anyway. (For $i \ge 48$, $j = 71$ lies in the closed region
$j \le 3i/2$, which is why S3 states the open range as
$i \le 47$.)

**Honest breaking point (following S3 Section 5, endorsed).**
(1) For fixed $i$ and $j \to \infty$, $N(i,j) \approx ej^2/i \to
\infty$ while $G$ grows, so every fixed-$i$ family eventually exits
the criterion; for $i = 1$ the route fires only at prime $n$.
(2) For $N(i,j) > 4\cdot10^{18}$ there is no table, and Theorem
C2.9's regions cover only $n - i \lesssim 5000\,i\log^2(n-i)$ (resp.
the $\log^3$ scale), which exceeds the table range only for roughly
$i \gtrsim 10^{12}$; pairs with $i \lesssim 10^{12}$ and
$N(i,j) > 4\cdot10^{18}$ at large $n$ are untouched by this route.
(3) Even Baker, Harman, and Pintz (2001), $p_{k+1} - p_k \ll
p_k^{0.525}$ for large $p_k$ (non-explicit; corroborated as the
exponent $0.525$ in the Bertrand survey), would clear only
$i \gtrsim N(i,j)^{0.525}$. (4) The condition is sufficient, never
necessary: e.g. at $(i,j,n) = (17,71,540)$ the interval
$(523, 540]$ is prime-free (523 and 541 are consecutive primes), so
the route is silent, yet the triple is fine by the sweep, its common
prime being $\le n/2$.

---

## 6. Independent computations (T-C)

All code is Python standard library only (`math`, sieve via
`bytearray`), written for this document; total wall time about
$21$ s ($3$ s sieve block, $17$ s threshold block, $1$ s miscellany),
well under the $\sim$3 minute budget. Method follows S3 Section 6:
threshold computations for the pair classification, and
first-occurrence prime-gap table values, recomputed by sieve in the
range where the theorems use them.

**(a) Sanity checks on the lemmas.** The counterexample of
Lemma C2.3: $\binom{20}{9} = 167960 = 13\cdot12920$,
$\binom{20}{3} = 1140 \equiv 9 \pmod{13}$. On 3000 seeded random
triples ($n \le 200$), for every prime $p \in (n/2, n]$ the
divisibility of $\binom{n}{i}$ and $\binom{n}{j}$ by $p$ matched the
iff of Lemma C2.3, the common-divisor conclusion on $(n-i, n]$, and
the wasted conclusion on $(n-j, n-i]$: **0 violations**.

**(b) Prime gaps by sieve (recomputed, not tabulated).** Sieve to
$2.2\times10^{6}$; the maximal-gap records found are, in order,
$(g, p)$: $(1,2), (2,3), (4,7), (6,23), (8,89), (14,113), (18,523),
(20,887), (22,1129), (34,1327), (36,9551), (44,15683), (52,19609),
(72,31397), (86,155921), (96,360653), (112,370261), (114,492113),
(118,1349533), (132,1357201), (148,2010733)$. Every record value
that S3 Section 3 lists in this range agrees exactly, including
$36$ after $9551$, $72$ after $31397$, $86$ after $155921$,
$96$ after $360653$, $112$ after $370261$, $114$ after $492113$,
$118$ after $1349533$, $132$ after $1357201$. In particular
$G(1.40\times10^{6}) = 132$, $G(10000) = G(10127) = 36$, and the
off-by-one boundary $G(2010733) = 132$, $G(2010734) = 148$ both
check. The further records S3 lists, $154$ after $4652353$,
$180$ after $17051707$, $222$ after $122164747$, are outside sieve
range; they were cross-checked against the OEIS/Nicely
first-occurrence list, where all three appear with those values.

**(c) C1 arithmetic (item (i) of T-C).** With $e^2 =
7.3890560989\ldots$: $e^2(7.35\times10^8)^2 =
3.9918\times10^{18} < 4\times10^{18}$. So for $i \ge 1476$,
$j \le 7.35\times10^8$: $G(N(i,j)) \le 1476 \le i$, exactly the
chain Theorem C2.10 needs. **Verified, no discrepancy.**

**(d) C2 count (item (ii) of T-C).** Independent threshold
computation: for each $i \in [1,1000]$, $T_i = \binom{10001}{i}$,
and $J_i$ = the largest $j \le 5000$ with
$\binom{2j}{2(j-i)} = \binom{2j}{2i} \le T_i$, found by exact binary
search (valid because $N(i,j) \le 10000 \iff
\binom{10001}{i} \ge \binom{2j}{2(j-i)}$ by monotonicity of
$\binom{n}{i}$ in $n$, and $\binom{2j}{2i}$ is strictly increasing
in $j$). Open pairs for this $i$ are
$\lfloor 3i/2\rfloor + 1 \le j \le 5000$; cleared are those
$\le J_i$; partial are $J_i < j \le 5000$. Results:

* Totals: considered $4{,}249{,}500$; fully cleared $768{,}741$;
  partial $3{,}480{,}759$. All three reproduce RESULTS.md exactly.
* Spot values: $J_1 = 70$, $J_{132} = 762$, $J_{500} = 1597$,
  $J_{1000} = 2391$, matching the RESULTS.md appendix.
* Restricted to $132 \le i \le 1000$: considered $3{,}607{,}436$,
  already cleared $716{,}330$, partial
  $\sum_{i=132}^{1000} (5000 - J_i) = \mathbf{2{,}891{,}106}$.
* Cross-check performed *after* the independent computation: my
  $J_i$ agree with `pairpass.json` for all $1000$ values of $i$
  (0 mismatches), and the same sum computed from that file is also
  $2{,}891{,}106$.

**Conclusion on T-C: my count is $2{,}891{,}106$, in exact
agreement with S3's corrected Theorem C2 count. No discrepancy.**

---

## 7. Verification register, discrepancies, and gaps

1. **C2 count: agreement.** $2{,}891{,}106$ (mine) $=$ $2{,}891{,}106$
   (S3, corrected). Method, totals, and all $J_i$ agree.
2. **Theorem B regions B1, B2, B3: restated exactly as in S3 and
   proved** via Lemma C2.7 from the cited inputs.
3. **Discrepancy in S3 (remark only, flagged in Section 4):** the
   claim that B3 / the $m=3$ bounds are strongest "for
   $\log n < 435$" is algebraically reversed; the correct crossover
   is $\log(n-i) = 435$, with B3 strongest only above it. No theorem
   in S3 or here depends on the comparison.
4. **Unverifiable citation detail:** "Axler 2017, Thm 4.1" - the
   theorem *number* inside arXiv:1703.08032 could not be confirmed
   from the primary text in my searches. The data B3 uses
   ($x_0 = 6034256$, $C = 0.087$, $m = 3$, author, year, arXiv id)
   are corroborated by an independent secondary table
   (*Mathematics* 2018, 6, 289, Theorem 6; arXiv:1804.02500v3).
   Recommend the campaign cite B3 as "Axler 2017, as tabulated in
   [that table]" until the primary source is opened.
5. **Verified citations:** Dusart 2010 (threshold, constant,
   exponent, strict lower interval end) - two independent secondary
   sources. Dusart 2018 Prop. 5.4 and Cor. 5.5 (both statements,
   with internal numbering, journal, volume, pages, DOI) - the
   Bertrand's postulate survey plus the *Mathematics* 2018 table.
   Trudgian 2014 row (not used in Theorem C2.9) - the
   *Mathematics* 2018 table only; its primary text was not opened.
   Oliveira e Silva-Herzog-Pardi 2014 (journal, volume, pages,
   scope $4\cdot10^{18}$, maximal gap $1476$ after
   $1425172824437699411$) - multiple independent reference lists and
   prime-gap compilations; the computation itself is taken on trust
   as a published computational theorem, as S3 does.
   Baker-Harman-Pintz $0.525$ (used only in the breaking-point
   remarks) - corroborated, non-explicit, no theorem rests on it.
6. **Endpoint conventions.** The sources state the explicit
   intervals with strict lower end, $(x, x(1+\delta)]$ (the
   *Mathematics* 2018 table prints the upper end open, which only
   strengthens Lemma C2.7). The strict lower end is load-bearing:
   a prime equal to $n-i$ would not lie in $(n-i, n]$.
7. **What is not proved here.** Phase 0's reduction, the EEES78
   discharge, and the $n \le 10000$ sweep are established inputs
   (Section 0), as is the $j \le 3i/2$ closure, which this strategy
   does not use. Nothing in this document claims #699 in general:
   the route is silent for small fixed $i$ and beyond the tables,
   per Section 5.
