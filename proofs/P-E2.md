# Prover E2 (independent) — Lemma S7(2.0): an explicit $\theta_u \le 0.36$ on $\alpha \in [4, 6.5)$, and the closure of $j \le 2i$ for large $i$

**Author:** Prover E2, Erdős #699 proof campaign, Cycle 2. This document
attacks Lemma S7(2.0) of `strategies/S7.md` §4–§5 and Cycle 1 report §8
item 1. It was written independently of the other Cycle 2 prover's work
(`proofs/P-E1.md` was not read). All computations reported below were
run by E2 with Python standard library only, in exact integer or exact
rational arithmetic except where a float evaluation is explicitly
labelled and then rechecked exactly; the code is saved alongside this
file as `P-E2_checks.py`. Every numbered claim carries E2's own label
PROVED / GAP / FALSE / OPEN.

**Headline (what this document claims, and what it does not).**
Lemma S7(2.0) is **proved** below, with the explicit constants
$i_0 = 120{,}000{,}000$ and $\delta = 0.0338$: for all $i \ge i_0$ and
all $n$ with $4i \le n \le N(i, 2i)$ one has $\theta_u(n,i) \le 0.3262
= 0.36 - \delta$ (Theorem E2.10). With the key lemma this closes the
pair $(i, 2i)$ for all $i \ge i_0$ (Theorem E2.15(a)), and the same
assembly at the weaker thresholds $\alpha \ge 7/2$ and $\alpha \ge 3$
closes **every** pair $3i/2 < j \le 2i$ for $i \ge 170{,}000{,}000$
(Theorem E2.15(b)). This does **not** prove Erdős #699: the region
$j > 2i$ is untouched, and the pairs with $i < i_0$ and $j \le 2i$ are
*not* discharged here (see §7.1 for the precise remaining inputs).

---

## 0. Setting, notation, and given inputs

Throughout, $1 \le i < j \le n/2$, $C(a,b) = \binom{a}{b}$, and
$C(n,i) = u\,v$ with $u$ supported on primes $< i$ and
$v = V_i(n)$ supported on primes $\ge i$;
$\theta_u(n,i) = \log u / \log C(n,i)$, $\alpha = n/i \in \mathbb R$.
A **counterexample** is a triple with $\gcd(v, C(n,j)) = 1$.
$e_p(m)$ is the exponent of a prime $p$ in $m$ (also written $v_p$).

Taken as given (per the task brief; cited freely, not re-derived):

- **(G1) EEES78.** $v > C(n,i)^{1/2}$ outside the 12 exception pairs
  $(n,i) \in \{(8,3),(9,4),(10,5),(12,5),(21,7),(21,8),(30,7),(33,13),
  (33,14),(36,13),(36,17),(56,13)\}$. Note every exception pair has
  $i \le 56$; no exception pair occurs for $i \ge i_0$ below.
- **(G2) Key lemma.** If $d \mid C(n,i)$ and $\gcd(d, C(n,j)) = 1$ then
  $d \mid C(j,i)$; hence a counterexample satisfies $v \le C(j, j-i)$.
- **(G3) Finite reduction.** A counterexample with $(n,i)$ not an
  exception pair satisfies $n \le N(i,j)$, where $N(i,j)$ is the
  largest $n$ with $C(n,i) < C(2j, 2(j-i))$.
- **(G4) Already closed:** $j \le 3i/2$; $n = 2j$; $i \in \{1,2\}$; the
  boundary family $j = \lfloor 3i/2 \rfloor + 1$; and the sweep: no
  counterexample with $n \le 20{,}000$.

The strategy is S7 §5's, with one structural change that does all the
work: S7 charged the whole range $\sqrt i < p \le i/2$ (its R2) the
crude per-prime cost $\log n$, a leading term of $\tfrac12 i$ whose
explicit form converges far too slowly (see §6.1 for the exact
barrier this creates). E2 instead splits at $i/5$ and applies the
Lemma-B carry analysis to **every** prime $p \in (i/5, i)$, i.e. to
all of S7's R3 ($m=1$), the range $(i/3, i/2]$ ($m=2$, as suggested in
the brief, item 1(a)), the range $(i/4, i/3]$ ($m=3$), and
$(i/5, i/4]$ ($m=4$). Only the tail $p \le i/5$ is charged crudely,
at a leading cost of $\tfrac15 i$ instead of $\tfrac12 i$.

---

## 1. The explicit external estimates used

All logarithms are natural. $\vartheta(x) = \sum_{p \le x} \log p$.

**Lemma E2.1 (binomial entropy with explicit error). PROVED**
*(modulo Robbins' published Stirling bounds, cited).*
For $1 \le K \le N-1$ and $N \ge 10$,
$$\Big|\log C(N,K) - \big(N\log N - K\log K - (N-K)\log(N-K)\big)\Big|
\;\le\; \log N.$$

*Proof.* Robbins (1955): $\log m! = m\log m - m + \tfrac12\log(2\pi m)
+ \rho_m$ with $1/(12m+1) < \rho_m < 1/(12m)$ for all $m \ge 1$.
Applying this to $N!, K!, (N-K)!$, the main terms give the displayed
entropy expression and the error is
$E = \tfrac12\log\frac{N}{2\pi K(N-K)} + (\rho_N - \rho_K - \rho_{N-K})$.
Now $\frac{N}{K(N-K)} = \frac1K + \frac1{N-K} \in [4/N,\; 1 + 1/(N-1)]
\subseteq [4/N, 2]$, so the logarithmic term lies in
$[-\tfrac12\log N - \tfrac12\log(\pi/2),\; -\tfrac12\log\pi]
\subseteq [-\tfrac12\log N - 0.226,\; 0]$, and
$\rho_N - \rho_K - \rho_{N-K} \in (-1/6, 1/12)$. Hence
$|E| \le \tfrac12\log N + 0.393 \le \log N$ for $N \ge 10$
($\tfrac12\log 10 = 1.151 > 0.393$, and the gap grows).
(E2 also spot-checked the inequality in exact arithmetic for 2000
seeded random pairs $(N,K)$, $10 \le N \le 400$: the worst ratio
$|E|/\log N$ seen was $0.609 < 1$.) $\square$

**Input E2.2 (Dusart's explicit $\pi$ bound). PROVED as a citation.**
(Dusart 2010, *Estimates of some functions over primes without R.H.*)
$$\pi(x) \;<\; \frac{x}{\log x - 1.1} \qquad \text{for all } x \ge 60184.$$
This is the form already used elsewhere in the campaign (cf. the
Dusart estimates in Cluster C). E2 uses it only at $x = i/5 \ge
24{,}000{,}000$.

**Input E2.3 (Dusart's explicit $\vartheta$ bound). PROVED as a citation.**
(Dusart 2010, same paper; stated e.g. as Lemma 2.1(b) in the
Ramaré–Saouter-line literature and in the form
$|\vartheta(x) - x| \le 0.006788\,x/\log x$ in secondary sources)
$$|\vartheta(x) - x| \;\le\; 0.006788\,\frac{x}{\log x}
\qquad \text{for all } x \ge 10{,}544{,}111.$$
E2 uses it only at arguments $\ge 10{,}967{,}742$ (see §5), inside its
range of validity. This $\vartheta$-form, not a $\pi$-difference, is
what makes the interval estimates of §5 affordable: the error per
interval is $O(x/\log x)$ with constant $0.006788$, instead of the
$O(x/\log^2 x)$-per-endpoint errors of Dusart $\pi$-differences, whose
near-cancellation would have to be tracked interval by interval.

---

## 2. The window cap: $\alpha < 13/2$ on $n \le N(i, 2i)$

Write $f(\alpha) = \alpha\log\alpha - (\alpha-1)\log(\alpha-1)$ for
$\alpha > 1$; $f'(\alpha) = \log\frac{\alpha}{\alpha-1} > 0$, so $f$
is strictly increasing. Values used below (float evaluations of
closed forms; the inequalities they feed are checked with margins
$\gg 10^3$, so no rounding issue arises):
$f(3) = 1.909543$, $f(7/2) = 2.093944$, $f(4) = 2.249341$,
$f(13/2) = 2.790600$, and $4\log 2 = 2.772589$.

**Lemma E2.4 (window cap). PROVED.**
Let $i \ge 120{,}000{,}000$ and $n \le N(i, 2i)$. Then $n < 13i/2$,
i.e. $\alpha < 6.5$. More generally, for every $j \le 2i$ and
$n \le N(i,j)$, $\alpha < 6.5$.

*Proof.* By (G3), $C(n,i) < C(4i, 2i)$. Suppose $n \ge n_0 :=
\lceil 13i/2 \rceil$. By Lemma E2.1 with $(N,K) = (n_0, i)$,
$\log C(n_0, i) \ge i\,f(n_0/i) - \log n_0 \ge i\,f(13/2) - \log n_0$
($f$ increasing, $n_0/i \ge 13/2$). By Lemma E2.1 with
$(N,K) = (4i, 2i)$, whose entropy main term is
$4i\log 4i - 2i\log 2i - 2i\log 2i = 4i\log 2$,
$\log C(4i,2i) \le 4i\log 2 + \log 4i$. Hence
$\log C(n_0,i) - \log C(4i,2i) \ge i\,(f(13/2) - 4\log 2) - \log n_0
- \log 4i = 0.0180109\,i - \log n_0 - \log 4i$.
For $i \ge 120{,}000{,}000$ this is $\ge 2{,}161{,}310 - 20.5 - 20.0
> 0$ (using $n_0 \le 6.51\,i$ for $i \ge 100$, so both logarithms are
$< 21$), and it is increasing in $i$ (the linear term has slope
$0.0180109$; the subtracted logarithms grow like $2\log i$).
Thus $C(n_0, i) > C(4i, 2i)$, and since $C(\cdot, i)$ is increasing,
$C(n,i) > C(4i,2i)$ for all $n \ge n_0$, contradicting $n \le N(i,2i)$.
For general $j \le 2i$: $C(2j, 2(j-i)) = C(2j, 2i)$ is strictly
increasing in $j$ (the ratio $C(2j{+}2,2i)/C(2j,2i) =
\frac{(2j+2)(2j+1)}{(2j+2-2i)(2j+1-2i)} > 1$), so
$N(i,j) \le N(i, 2i)$ and the same cap applies. $\square$

*Remark.* The asymptotic cap is $\alpha \to 6.38\ldots$ (S7 §3);
$6.5$ is a convenient rigorous majorant at the stated $i_0$, bought
with the positive margin $f(13/2) - 4\log 2 = 0.0180109$ per unit $i$.

**Lemma E2.5 (denominator lower bound). PROVED.**
For $i \ge 10$ and $n$ with $\alpha = n/i \in [\alpha_{\min}, 13/2)$,
$$\frac{\log C(n,i)}{i} \;\ge\; f(\alpha_{\min}) -
\frac{\log(6.5\,i)}{i},$$
and the subtracted term is decreasing in $i$.

*Proof.* Lemma E2.1 with $(N,K) = (n,i)$: the entropy main term is
exactly $i\,f(\alpha)$ (the $\log i$ terms cancel:
$n\log n - i\log i - (n-i)\log(n-i) = i[\alpha\log\alpha -
(\alpha-1)\log(\alpha-1)]$), the error is $\ge -\log n \ge
-\log(6.5\,i)$, and $f$ is increasing. $(\log x)/x$ decreases for
$x > e$. $\square$

---

## 3. The split at $i/5$ and the generalised carry lemma

**Lemma E2.6 (Erdős' lemma; S7 Lemma A). PROVED.**
If $p^{a} \| C(n,i)$ then $p^a \le n$; in particular
$e_p(C(n,i)) \log p \le \log n$ for every prime $p$.

*(This is S7's Lemma A, verified there; the standard proof is via
Legendre's formula, each summand in $\{0,1\}$ vanishing for
$p^e > n$, as in `proofs/P-B1.md` Lemma B1.2, which E2 cites.)*

Define the two parts of $u$:
$$u_{\le} = \prod_{p \le i/5} p^{e_p(C(n,i))}, \qquad
u_{>} = \prod_{i/5 < p < i} p^{e_p(C(n,i))}, \qquad u = u_{\le} u_{>}.$$

**Lemma E2.7 (generalised Lemma B / carry lemma). PROVED.**
Let $i > 325/2$ (in particular any $i \ge i_0$ below), let
$n \le 13i/2$, and let $p$ be a prime with $i/5 < p < i$. Put
$m = \lfloor i/p \rfloor \in \{1,2,3,4\}$. Then:

(a) $p^2 > n$, hence $e_p(C(n,i)) \le 1$, $v_p(i!) = m$, and
$e_p(C(n,i)) = \#\{\text{multiples of } p \text{ in } (n-i, n]\} - m$.

(b) If $e_p(C(n,i)) = 1$ and $q = \lfloor n/p \rfloor$, then
$q > m$, $m\alpha < q < (m+1)\alpha$, and
$$p \;\in\; J_{m,q} \;:=\; \Big(\frac{n-i}{\,q-m\,},\; \frac{n}{q}\Big].$$

(c) (The R3 case $m=1$ is S7's Lemma B, with its $p^2$ alternative
vacuous here.) For $p \in (i/2, i)$, $e_p \ge 1$ iff the block
contains two multiples of $p$ or one multiple of $p^2$ (S7 Lemma B);
but $p^2 > (i/2)^2 > 13i/2 \ge n$ for $i > 26$, so no multiple of
$p^2$ lies in the block, every multiple of $p$ in the block has
$v_p = 1$ exactly, and (a)–(b) are the complete description. The
same vacuity holds for every $m$: $e_p \ge 2$ is impossible in the
whole range $p > i/5$ once $i > 325/2$, so there is **no**
$e_p \ge 2$ subcase to bound in $u_{>}$. All $e_p \ge 2$ behaviour
is confined to $u_{\le}$, where Lemma E2.6 caps the *total*
contribution of each prime by $\log n$ regardless of the exponent.

(d) The prime $p = i$ (when $i$ is prime) is not a factor of $u$:
$u$ is supported on $p < i$ by definition, and $p=i$ belongs to $v$.
It never enters the bounds below: every interval $J_{m,q}$ in (b)
satisfies $n/q < i$ (since $q > m\alpha \ge \alpha$), so even the
overcounting sums of §5–§6 do not charge it.

*Proof.* (a) $p > i/5$ gives $p^2 > i^2/25 > 13i/2 \ge n$ iff
$i > 25 \cdot 13/2 = 325/2$. In Legendre's formula for
$e_p(C(n,i))$ every term with $p^e$, $e \ge 2$, vanishes
($p^e > n \ge i, n-i$), leaving
$e_p = \lfloor n/p \rfloor - \lfloor i/p \rfloor -
\lfloor (n-i)/p \rfloor$. The last two floors are $m$ and the count
identity is standard: $\lfloor n/p \rfloor - \lfloor (n-i)/p \rfloor$
counts multiples of $p$ in $(n-i, n]$. Also $v_p(i!) = \lfloor i/p
\rfloor = m$ since $p^2 > i$. For $e_p \le 1$: $m+2$ multiples of
$p$ in the block would span $(m+1)p > (m+1)\cdot\frac{i}{m+1} = i$
(using $p > i/(m+1)$, i.e. $i/p < m+1$), but points of the half-open
block $(n-i, n]$ span $< i$; so the count is $\le m+1$ and
$e_p = \text{count} - m \le 1$.

(b) The $m+1$ multiples in the block are consecutive multiples
$tp, (t{+}1)p, \ldots, (t{+}m)p$ with $t \ge 1$; the largest is
$qp$ with $q = t + m \ge m+1 > m$ and $q = \lfloor n/p \rfloor$.
From $(q-m)p > n-i$ and $qp \le n$ we get $p \in J_{m,q}$.
$J_{m,q} \ne \emptyset$ forces $\frac{n-i}{q-m} < \frac{n}{q}$, i.e.
$q(n-i) < n(q-m)$, i.e. $qi > mn$, i.e. $q > m\alpha$. And
$q \le n/p < \alpha(m+1)$ since $p > i/(m+1)$. $\square$

*Remark (what each $m$ is).* $m = \lfloor i/p \rfloor$ stratifies
$u_{>}$ exactly as the brief's item 1(a) prescribes:
$m=1$: $p \in (i/2, i)$ (S7's R3);
$m=2$: $p \in (i/3, i/2]$ (here $v_p(i!) = 2$, so $e_p \ge 1$ forces
$\ge 3$ multiples of $p$ in the block, counted with multiplicity —
and by (a) multiplicity is $1$ per multiple);
$m=3$: $p \in (i/4, i/3]$ (forces $\ge 4$ multiples);
$m=4$: $p \in (i/5, i/4]$ (forces $\ge 5$ multiples).
In each case the multiples condition is exactly $p \in J_{m,q}$ for
the $q$ of (b): at least $m+1$ multiples in the block iff the top
multiple $qp \le n$ and the bottom one $(q-m)p > n-i$.

---

## 4. The interval-length function and its exact sup

For $\alpha \in \mathbb R$ and $m \in \{1,2,3,4\}$ let
$$L(\alpha) \;=\; \sum_{m=1}^{4}\;\sum_{\substack{q \in \mathbb Z\\
m\alpha < q < (m+1)\alpha}} \frac{q - m\alpha}{q(q-m)},
\qquad\text{so that}\qquad
|J_{m,q}| = i\cdot\frac{q - m\alpha}{q(q-m)},$$
the last identity from
$\frac{n}{q} - \frac{n-i}{q-m} = i\big(\frac{\alpha}{q} -
\frac{\alpha-1}{q-m}\big) = i\,\frac{q - m\alpha}{q(q-m)}$.

**Lemma E2.8 (exact sup of $L$). PROVED** *(the finite step is an
exact rational computation, `P-E2_checks.py` Part 1).*
$$\sup_{\alpha \in [4,\,13/2)} L(\alpha) = L(4^{+}) = 0.456098\ldots,
\qquad
\sup_{\alpha \in [7/2,\,13/2)} L(\alpha) = 0.464994\ldots,
\qquad
\sup_{\alpha \in [3,\,13/2)} L(\alpha) = 0.506996\ldots,$$
the three suprema being the right-hand limits at $\alpha = 4$,
$\alpha = 7/2$, $\alpha = 3$ respectively. E2 uses the rounded-up
values $0.4561$, $0.4650$, $0.5070$.

*Proof.* On any open interval of $\alpha$ containing no point of the
form $q/m$ or $q/(m+1)$ ($1 \le m \le 4$, $q \in \mathbb Z$), the
active index set $\{(m,q) : m\alpha < q < (m+1)\alpha\}$ is constant
and each summand is affine in $\alpha$ with slope
$-m/(q(q-m)) < 0$; hence $L$ is strictly decreasing there, and its
supremum on the interval is its right-hand limit at the left
endpoint. At a critical point $\alpha_0$ the right-hand limit is
obtained by evaluating the summands at $\alpha_0$ over the enlarged
active set $\{m\alpha_0 \le q \le (m+1)\alpha_0\}$ (summands with
$q = m\alpha_0$ contribute $0$; summands with $q = (m+1)\alpha_0$
contribute their full $\alpha_0$-value as the limit from above);
and at $\alpha_0$ itself, $L(\alpha_0)$ is $\le$ that right-hand
limit, since its active set is a subset and all summands are
$\ge 0$. Therefore the sup over $[\alpha_{\min}, 13/2)$ is the max
of finitely many right-hand limits, over the critical points in
the range. Only $q \le 33$ can occur ($q < (m+1)\alpha \le 5 \cdot
13/2$). The exact rational enumeration (`Fraction` arithmetic, no
floats) gives: over $[4, 13/2)$ there are 26 critical points, the
largest right-hand limit is at $\alpha_0 = 4$, value
$11797349/25865840 = 0.4560977\ldots$, the second largest is
$0.428433$ at $\alpha_0 = 9/2$; over $[7/2, 13/2)$ 31 critical
points, max $11394421/24504480 = 0.4649934\ldots$ at $\alpha_0 =
7/2$; over $[3, 13/2)$ 36 critical points, max $182701/360360 =
0.5069958\ldots$ at $\alpha_0 = 3$. For illustration, the
$\alpha_0 = 4$ right-hand limit is the 16-term sum
$\big(\frac1{20}{+}\frac1{15}{+}\frac1{14}{+}\frac1{14}\big) +
\big(\frac1{63}{+}\frac1{40}{+}\frac1{33}{+}\frac1{30}\big) +
\big(\frac1{130}{+}\frac1{77}{+}\frac1{60}{+}\frac1{52}\big) +
\big(\frac1{221}{+}\frac1{126}{+}\frac1{95}{+}\frac1{80}\big)$
(grouped by $m = 1,2,3,4$). $\square$

---

## 5. Bounding $\log u_{>}$ via $\vartheta$-differences

**Lemma E2.9 ($\log u_{>}$ bound). PROVED.**
Let $\alpha \in [\alpha_{\min}, 13/2)$ with $\alpha_{\min} \in
\{3, 7/2, 4\}$, and let $i$ be large enough that every interval
endpoint below satisfies $(n-i)/(q-m) \ge 10{,}544{,}111$; a
sufficient condition is $(\alpha_{\min}-1)\,i/31 \ge
10{,}544{,}111$. Then
$$\frac{\log u_{>}}{i} \;\le\; L(\alpha) \;+\;
\frac{0.006788 \cdot 2 \cdot 6.5 \cdot S(\alpha_{\min})}
{\log\big((\alpha_{\min}-1)\,i/31\big)},
\qquad
S(\alpha_{\min}) = \frac{7}{\alpha_{\min}}
\Big(1 + \frac12 + \frac13 + \frac14\Big).$$

*Proof.* By Lemma E2.7(a), a prime $p \in (i/5, i)$ contributes
$\log p$ to $\log u_{>}$ if $e_p = 1$ and $0$ otherwise; by (b) each
such prime lies in $J_{m,q}$ for its own $(m, q)$ with
$m\alpha < q < (m+1)\alpha$. All summands are $\ge 0$, so summing
over *all* such intervals only overcounts:
$$\log u_{>} \;\le\; \sum_{m=1}^{4}\sum_{q}
\sum_{p \in J_{m,q}} \log p
\;=\; \sum_{m,q} \big(\vartheta(n/q) - \vartheta((n-i)/(q-m))\big).$$
For each interval, Input E2.3 (applicable since both endpoints are
$\ge (n-i)/(q-m) \ge (\alpha_{\min}-1)i/31 \ge 10{,}544{,}111$:
here $q - m \le 31$ because $q < (m+1)\alpha < 5 \cdot 13/2 =
32.5$, so $q \le 32$) gives, with $b = n/q$, $a = (n-i)/(q-m)$,
$$\vartheta(b) - \vartheta(a) \;\le\; (b - a) +
0.006788\Big(\frac{b}{\log b} + \frac{a}{\log a}\Big)
\;\le\; |J_{m,q}| + 0.006788\,\frac{2b}{\log a},$$
using $b/\log b \le b/\log a$ and $a/\log a \le b/\log a$.
Summing: $\sum |J_{m,q}| = i\,L(\alpha)$ by §4. For the error sum,
$b = n/q \le 6.5\,i/q$, $\log a \ge
\log\big((\alpha_{\min}-1)i/31\big)$, and
$\sum_{m,q} 1/q \le S(\alpha_{\min})$: for fixed $m$ the admissible
$q$ lie in an interval of length $\alpha \le 6.5$ (at most $7$
integers) and satisfy $q > m\alpha \ge m\alpha_{\min}$, so
$\sum_q 1/q \le 7/(m\alpha_{\min})$; summing over $m = 1..4$ gives
$S(\alpha_{\min})$. $\square$

**Lemma E2.9b ($\log u_{\le}$ bound — the crude tail). PROVED.**
For $i/5 \ge 60184$ and $n \le 13i/2$,
$$\frac{\log u_{\le}}{i} \;\le\; \frac{1}{5}\cdot
\frac{\log i + \log 6.5}{\log i - \log 5 - 1.1},$$
and the right side is decreasing in $i$.

*Proof.* By Lemma E2.6, each prime $p \le i/5$ contributes at most
$\log n$ to $\log u$, so $\log u_{\le} \le \pi(i/5)\log n$. Input
E2.2 at $x = i/5$ and $\log n \le \log i + \log 6.5$ give the bound;
$(L + a)/(L - b)$ has derivative $-(a+b)/(L-b)^2 < 0$ in
$L = \log i$. $\square$

---

## 6. Assembly: Lemma S7(2.0) with explicit $i_0$ and $\delta$

**Theorem E2.10 (Lemma S7(2.0), explicit). PROVED.**
Let $i_0 = 120{,}000{,}000$ and $i \ge i_0$. For all $n$ with
$4i \le n \le N(i, 2i)$,
$$\theta_u(n,i) \;\le\; 0.3262 \;=\; 0.36 - \delta,
\qquad \delta = 0.0338 > 0.$$

*Proof.* By Lemma E2.4, $\alpha \in [4, 13/2)$.
*Tail:* Lemma E2.9b at $i = i_0$ ($i/5 = 24{,}000{,}000 \ge
60184$): $\log u_{\le}/i \le \frac15 \cdot
\frac{18.603003 + 1.871802}{18.603003 - 1.609438 - 1.1}
= \frac15 \cdot \frac{20.474805}{15.893565} = 0.257649 \le 0.2577$,
and this decreases in $i$.
*Main part:* Lemma E2.9 with $\alpha_{\min} = 4$: the endpoint
condition is $3i/31 \ge 3 \cdot 120{,}000{,}000/31 =
11{,}612{,}903 \ge 10{,}544{,}111$ ✓. With $L(\alpha) \le 0.4561$
(Lemma E2.8), $S(4) = \frac74 \cdot \frac{25}{12} = 3.645833$, and
$\log(3i/31) \ge \log 11{,}612{,}903 = 16.267627$:
error $\le \frac{0.006788 \cdot 13 \cdot 3.645833}{16.267627}
= 0.019777 \le 0.0198$. So $\log u_{>}/i \le 0.4561 + 0.0198
= 0.4759$.
*Total:* $\log u / i \le 0.2577 + 0.4759 = 0.7336$ (exact computed
value $0.733524$).
*Denominator:* Lemma E2.5: $\log C(n,i)/i \ge f(4) -
\log(6.5 i_0)/i_0 = 2.249341 - 0.0000002 \ge 2.2493$.
*Ratio:* $\theta_u \le 0.7336 / 2.2493 = 0.32616 \le 0.3262$.
Hence $\delta = 0.36 - 0.3262 = 0.0338$. All quantities are
monotone in $i$ in the favourable direction (Lemmas E2.5, E2.9b;
the E2.9 error decreases as $\log((\alpha_{\min}-1)i/31)$ grows),
so the bound persists for all $i \ge i_0$. $\square$

**Corollary E2.11 (the $\alpha \ge 7/2$ extension; beats the
S7(1.75) fallback target). PROVED.**
Let $i \ge i_1 := 170{,}000{,}000$. For all $n$ with
$7i/2 \le n$ and $\alpha < 13/2$ (in particular, for every
$j \le 2i$, all $n$ with $7i/2 \le n \le N(i,j)$),
$\theta_u(n,i) \le 0.3553 < 0.36$.

*Proof.* Identical assembly with $\alpha_{\min} = 7/2$: tail
$\frac15\cdot\frac{\log i_1 + \log 6.5}{\log i_1 - \log 5 - 1.1}
= 0.256413 \le 0.2565$; endpoint condition
$(5/2)i_1/31 = 13{,}709{,}677 \ge 10{,}544{,}111$ ✓;
$L \le 0.4650$ (Lemma E2.8); $S(7/2) = 4.166667$; error
$\le \frac{0.006788 \cdot 13 \cdot 4.166667}{\log 13{,}709{,}677}
= \frac{0.367683}{16.4339} = 0.022374 \le 0.0224$; total
$\log u/i \le 0.2565 + 0.4650 + 0.0224 = 0.7439$ (computed
$0.743780$); denominator $\ge f(7/2) - 10^{-7} \ge 2.0939$;
$\theta_u \le 0.7439/2.0939 = 0.35528 \le 0.3553$. $\square$

**Corollary E2.12 (the $\alpha \ge 3$ extension). PROVED.**
Let $i \ge i_1 = 170{,}000{,}000$. For all $n$ with $3i \le n$ and
$\alpha < 13/2$ (in particular, for every $j \le 2i$, all $n$ with
$3i \le n \le N(i,j)$), $\theta_u(n,i) \le 0.4138$.

*Proof.* Same assembly, $\alpha_{\min} = 3$: tail $0.2565$ as
above; endpoint condition $2i_1/31 = 10{,}967{,}742 \ge
10{,}544{,}111$ ✓; $L \le 0.5070$; $S(3) = 4.861111$; error
$\le \frac{0.006788 \cdot 13 \cdot 4.861111}{\log 10{,}967{,}742}
= \frac{0.428959}{16.2103} = 0.026462 \le 0.0265$; total
$\log u/i \le 0.2565 + 0.5070 + 0.0265 = 0.7900$ (computed
$0.789871$); denominator $\ge f(3) \ge 1.9095$;
$\theta_u \le 0.7900/1.9095 = 0.41372 \le 0.4138$. $\square$

### 6.1 Why the unsharpened S7 §5 assembly fails (the exact barrier)

For the record (brief item 1(c), applied to the *unmodified* §5
bound): S7's R2 charges $\pi(i/2)\log n$. With Input E2.2
($\pi(x) < x/(\log x - 1.1)$, $x \ge 60184$), R2 alone contributes
$\frac{\log u}{i} \approx \frac12 \cdot
\frac{\log i + \log 6.5}{\log i - \log 2 - 1.1}$, which at
$i = 10^{8}$ is $0.5 \cdot 20.32/16.69 = 0.609$, and adding R3's
$\approx 0.19$–$0.26$ (interval lengths at $\alpha = 4$) already
reaches $\approx 0.80$–$0.87$ against the budget
$0.36 \cdot f(4) = 0.8098$ — the margin is negative or within the
$\vartheta/\pi$ error terms until astronomically large $i$
(the factor $(\log i + \log 6.5)/(\log i - \log 2 - 1.1)$ is still
$1.22$ at $i = 10^{8}$ and decays like $1 + 3.66/\log i$).
The barrier is therefore exactly the R2 leading term
$\tfrac12 i$ with its $O(1/\log i)$ explicit-estimate inflation,
not the truth of the bound. The $m \ge 2$ carry analysis of §3
removes it: the ranges $m = 2, 3, 4$ contribute interval lengths
$0.1045$, $0.0566$, $0.0355$ (at the $\alpha_0 = 4$ right limit,
from Lemma E2.8's term list: $m=1$ contributes $0.2595$ there)
instead of their full widths
$1/6, 1/12, 1/20$ times $\log n / \log i$-inflated counts, and the
surviving crude tail is only $\pi(i/5)\log n \approx 0.258\,i$.

---

## 7. The closure step

Recall $\varphi_{\mathrm{req}}(i,j) =
\log C(j, j-i) / \log C(2j, i)$ (S7 §3): by (G2), a counterexample
with $v \ge C(n,i)^{\varphi}$ and $\varphi > \varphi_{\mathrm{req}}$
is impossible, since $v \le C(j, j-i)$ and $C(n,i) \ge C(2j, i)$.

**Lemma E2.13 ($\varphi_{\mathrm{req}}(i, 2i)$ bound). PROVED.**
For all $i \ge i_0 = 120{,}000{,}000$,
$\varphi_{\mathrm{req}}(i, 2i) \le 0.6164$.
(Float check at $i_0$: `lgamma` evaluation gives
$\varphi_{\mathrm{req}}(i_0, 2i_0) = 0.61631144$; the proved bound
below is $0.616312$, rounded up.)

*Proof.* Lemma E2.1: $\log C(2i, i) \le 2i\log 2 + \log 2i$ (main
term $2i\log 2$) and $\log C(4i, i) \ge i\,f(4) - \log 4i$. So
$\varphi_{\mathrm{req}} \le \frac{2\log 2 + (\log 2i)/i}{f(4) -
(\log 4i)/i}$, which decreases in $i$ (numerator's error term
decreases, denominator's increases). At $i = i_0$:
$\frac{1.386294 + 0.0000002}{2.249341 - 0.0000002} \le 0.616312
\le 0.6164$. $\square$

**Lemma E2.14 ($\varphi_{\mathrm{req}}(i,j)$ for all
$3i/2 \le j \le 2i$). PROVED.**
Let $c = j/i \in [3/2, 2]$ and $i \ge i_1 = 170{,}000{,}000$. Then
$\varphi_{\mathrm{req}}(i,j) \le 0.617$; and if $c \le 7/4$ then
$\varphi_{\mathrm{req}}(i,j) \le 0.580$.

*Proof.* By Lemma E2.1 the main terms are exact:
$\log C(j, j-i) \le iF_1(c) + \log j$ and
$\log C(2j, i) \ge iF_2(c) - \log 2j$, where
$F_1(c) = c\log c - (c-1)\log(c-1)$ and
$F_2(c) = 2c\log(2c) - (2c-1)\log(2c-1)$ ($= f(2c)$).
For a target constant $\kappa$, $\varphi_{\mathrm{req}} \le \kappa$
follows from $i\,D_\kappa(c) \ge \log j + \kappa\log 2j$ where
$D_\kappa(c) = \kappa F_2(c) - F_1(c)$. Now
$F_1'(c) = \log\frac{c}{c-1}$ and $F_2'(c) =
2\log\frac{2c}{2c-1}$, so for $\kappa \le 1$,
$D_\kappa'(c) = 2\kappa\log\frac{2c}{2c-1} -
\log\frac{c}{c-1} \le 2\log\frac{2c}{2c-1} -
\log\frac{c}{c-1} \le 0$, because
$\big(\frac{2c}{2c-1}\big)^2 \le \frac{c}{c-1}$ is equivalent to
$4c(c-1) \le (2c-1)^2 = 4c(c-1) + 1$. Hence $D_\kappa$ is
decreasing in $c$, and $D_\kappa(c) \ge D_\kappa(c_{\max})$ on
$c \le c_{\max}$.
Case $\kappa = 0.617$, $c_{\max} = 2$: $D = 0.617 \cdot 2.249341 -
1.386294 = 0.001549 \ge 0.0015$ (float evaluation of closed forms;
the margin over the error terms below is $> 10^3$).
Error requirement: $i \cdot 0.0015 \ge \log j + 0.617\log 2j$;
at $i = i_1$ the left side is $255{,}000$ and the right side is
$\le \log(3.4\cdot10^{8}) + 0.617\log(6.8\cdot10^{8}) \le 19.7 +
12.6 = 32.3$, and the left side grows linearly while the right
grows logarithmically. ✓
Case $\kappa = 0.580$, $c_{\max} = 7/4$: $D = 0.580 \cdot 2.093944
- 1.195089 = 0.019398 \ge 0.0193$; error requirement
$i \cdot 0.0193 \ge \log j + 0.58\log 2j$ holds at $i_1$ by
$3{,}281{,}000 \ge 32$ with the same growth remark. ✓ $\square$

**Theorem E2.15 (closure). PROVED** *(conditional on the given
inputs (G1)–(G4) of §0, as is every closure in this campaign).*

(a) For every $i \ge i_0 = 120{,}000{,}000$, the pair $(i, 2i)$ is
closed: there is no counterexample $(n, i, 2i)$ for any $n$.

(b) For every $i \ge i_1 = 170{,}000{,}000$ and every
$3i/2 < j \le 2i$, the pair $(i, j)$ is closed. Together with (G4)
($j \le 3i/2$ and the boundary family), **every pair $j \le 2i$ is
closed for $i \ge i_1$.**

*Proof.* Let $(n, i, j)$ be a putative counterexample. Then
$n \ge 2j$ (definition) and, $(n,i)$ not being an exception pair
(all exception pairs have $i \le 56 < i_0$, (G1)), (G3) gives
$n \le N(i,j) \le N(i, 2i)$, so $\alpha < 13/2$ by Lemma E2.4.
By (G2), $v \le C(j, j-i)$, i.e.
$C(n,i)^{1 - \theta_u} \le C(j, j-i)$; with $C(n,i) \ge C(2j,i)$
($n \ge 2j$) a contradiction follows from
$1 - \theta_u > \varphi_{\mathrm{req}}(i,j)$.

(a) $j = 2i$: $\alpha \ge 4$, Theorem E2.10 gives
$\theta_u \le 0.3262$, and Lemma E2.13 gives
$\varphi_{\mathrm{req}} \le 0.6164$:
$1 - \theta_u - \varphi_{\mathrm{req}} \ge 1 - 0.3262 - 0.6164
= 0.0574 > 0$. For $n > N(i, 2i)$ there is nothing to check, by
(G3) (equivalently: (G1)+(G3) already exclude counterexamples
there). $\square$

(b) Let $3i/2 < j \le 2i$, $i \ge i_1$.
Case $j \ge 7i/4$: $\alpha \ge 2j/i \ge 7/2$, Corollary E2.11
gives $\theta_u \le 0.3553$; Lemma E2.14 gives
$\varphi_{\mathrm{req}} \le 0.617$; margin
$\ge 1 - 0.3553 - 0.617 = 0.0277 > 0$.
Case $3i/2 < j < 7i/4$: $\alpha > 3$, Corollary E2.12 gives
$\theta_u \le 0.4138$; Lemma E2.14 gives
$\varphi_{\mathrm{req}} \le 0.580$; margin
$\ge 1 - 0.4138 - 0.580 = 0.0062 > 0$. $\square$

### 7.1 Precise remaining inputs (what Theorem E2.15 does not do)

1. **$i < i_1$ (resp. $i < i_0$).** The pairs $(i, j)$,
   $3i/2 < j \le 2i$, $i < i_1$, are **not** discharged by this
   document. The existing inputs cover only part of them: the
   sweep (G4) excludes counterexamples with $n \le 20{,}000$, and
   the Cycle 1 clearance theorems clear many pairs in the scope
   $i \le 1000$, $2j \le 10000$, but pairs with $i < i_1$ and
   $N(i, j) > 20{,}000$ remain, as a finite residue, to be checked
   by a targeted finite computation. E2 does not compute the size
   of that residue (per the brief).
2. **$n > N(i,j)$** is discharged by (G1)+(G3) (EEES78 plus the
   finite reduction), not by anything in this document; the 12
   EEES78 exception pairs are irrelevant here since $i \ge i_0
   > 56$.
3. **$j > 2i$** is entirely open from this document's standpoint:
   the budgets $1 - \varphi_{\mathrm{req}}(c)$ shrink below the
   proved $\theta_u$ bounds as $c$ grows past $2$ (cf. S7 §6).

---

## 8. Adversarial empirical test: the frontier window for $i \le 500$

**Computation E2.16 (empirical frontier test). PROVED as a finite
computation** (`P-E2_checks.py` Part 4; runtime $\approx$ 11 s).

*Method.* For each $1 \le i \le 500$, $N(i, 2i)$ was computed exactly
(binary search on the exact predicate $C(n,i) < C(4i, 2i)$ with
`math.comb`; the defining property $C(N,i) < C(4i,2i) \le C(N{+}1,i)$
was rechecked on a seeded sample). The window
$4i \le n \le N(i,2i)$ contains **299,743 points**; the largest
window endpoint ratio is $\max_i N(i,2i)/i = 6.392034$ (at
$i = 477$; at $i = 500$, $N = 3196$, ratio $6.392$), consistent
with Lemma E2.4's cap $6.5$. Float
$\theta_u$ was computed by an incremental sweep in $n$ for fixed
$i$ ($C(n{+}1,i)/C(n,i) = (n{+}1)/(n{+}1-i)$; only prime factors
$< i$ update $\log u$). *Error control:* every point with float
$\theta_u > 0.33$ (73 points) was recomputed **exactly**: $u$ and
$C(n,i)$ as integers via Legendre exponents, $\theta_u$ from
60-digit `Decimal` logarithms of those integers, and the $0.36$
threshold decided by the exact integer comparison
$u^{100} \le C^{36}$. On all 73 rechecked points the float and
exact values agree to $< 10^{-6}$; every other window point has
float $\theta_u \le 0.33$, a margin of $0.03$ against accumulated
rounding of $< 10^{-6}$, so the exact violation set below is
complete. (An earlier, differently-structured sweep implementation
produced output inconsistent with these exact rechecks and was
discarded; every number below is from the validated implementation
and, for all points $> 0.33$, from exact arithmetic.)

**Violations of $0.36$ — reported prominently, as required.**
$\theta_u > 0.36$ *does* occur in the frontier window at small
$i$: exactly **40 points** with $i \le 500$, **all with
$i \le 23$**. The largest values are
$\theta_u(30, 7) = 0.5916231534$ (the EEES78 exception pair
$(30,7)$), $\theta_u(56, 13) = 0.512192$ (the EEES78 exception
pair $(56,13)$), and $\theta_u(56, 9) = 0.482758$ (the largest
non-exception violation). The largest $i$ at which a violation
occurs is $i = 23$, at $(n, i) = (136, 23)$ with
$\theta_u = 0.387523$. Consequently **Lemma S7(2.0) is FALSE for
every $i_0 \le 23$** (the point $(136,23)$ lies in the window and
has $i = 23 \ge i_0$); this falsifies the lemma at small $i_0$,
not the route. No violation occurs for any $24 \le i \le 500$.

**Suprema over the window, by $i$-cutoff** (float values; the
marked ones are exact `Decimal` values from the recheck):

| restriction | $\sup \theta_u$ | at $(n,i)$ |
|---|---|---|
| $i \ge 1$ | $0.591623$ | $(30, 7)$ † |
| $i \ge 10$ | $0.512192$ | $(56, 13)$ † |
| $i \ge 20$ | $0.387523$ | $(136, 23)$ |
| $i \ge 30$ | $0.357355$ | $(145, 32)$ |
| $i \ge 50$ | $0.339629$ | $(378, 61)$ |
| $i \ge 100$ | $0.291824$ | $(536, 114)$ |
| $i \ge 200$ | $0.260510$ | $(1170, 283)$ |

† EEES78 exception pair. The exact value at the $i \ge 50$
maximiser is $\theta_u(378, 61) = 0.339629234164629\ldots$
These suprema extend S7 §2's frontier data (which reached
$i \le 250$) to $i \le 500$ and agree with it where they overlap
(S7: sup $0.3574$ for $i \ge 30$, $0.3396$ at $(378,61)$ for
$i \ge 50$, $0.2918$ for $i \ge 100$). The sup is strictly
decreasing in the $i$-cutoff from $i \ge 30$ on, and is already
below $0.36$ at $i \ge 30$ in this range — consistent with, but
of course far weaker than, Theorem E2.10 at $i_0 =
120{,}000{,}000$.

---

## 9. Summary of claims, with E2's labels

| Item | Statement (short) | Label |
|---|---|---|
| Lemma E2.1 | Binomial entropy, error $\le \log N$ (via Robbins) | PROVED |
| Input E2.2 | Dusart $\pi(x) < x/(\log x - 1.1)$, $x \ge 60184$ | PROVED (citation) |
| Input E2.3 | Dusart $\lvert\vartheta(x)-x\rvert \le 0.006788 x/\log x$, $x \ge 10544111$ | PROVED (citation) |
| Lemma E2.4 | $\alpha < 13/2$ on $n \le N(i,j)$, $j \le 2i$, $i \ge 1.2\cdot10^{8}$ | PROVED |
| Lemma E2.5 | $\log C(n,i)/i \ge f(\alpha_{\min}) - o(1)$ explicit | PROVED |
| Lemma E2.6 | Erdős: $p^{e_p} \le n$ | PROVED |
| Lemma E2.7 | Generalised carry lemma for $p \in (i/5, i)$; $e_p \le 1$; $p^2$ and $e_p \ge 2$ subcases vacuous in $u_{>}$; $p = i$ excluded | PROVED |
| Lemma E2.8 | $\sup L = 0.4561$ on $[4, 6.5)$; $0.4650$ on $[3.5, 6.5)$; $0.5070$ on $[3, 6.5)$ (exact rational enumeration) | PROVED |
| Lemma E2.9 | $\log u_{>}/i \le L(\alpha) + {}$explicit $\vartheta$-error | PROVED |
| Lemma E2.9b | $\log u_{\le}/i \le \frac15 \cdot \frac{\log i + \log 6.5}{\log i - \log 5 - 1.1}$ | PROVED |
| **Theorem E2.10** | **Lemma S7(2.0): $\theta_u \le 0.3262$ for $i \ge i_0 = 120{,}000{,}000$, $4i \le n \le N(i,2i)$; $\delta = 0.0338$** | **PROVED** |
| Corollary E2.11 | $\theta_u \le 0.3553$ for $\alpha \ge 7/2$, $i \ge 1.7\cdot10^{8}$ | PROVED |
| Corollary E2.12 | $\theta_u \le 0.4138$ for $\alpha \ge 3$, $i \ge 1.7\cdot10^{8}$ | PROVED |
| Lemma E2.13 | $\varphi_{\mathrm{req}}(i, 2i) \le 0.6164$, $i \ge i_0$ | PROVED |
| Lemma E2.14 | $\varphi_{\mathrm{req}}(i,j) \le 0.617$ ($j \le 2i$); $\le 0.580$ ($j \le 7i/4$) | PROVED |
| **Theorem E2.15** | **$(i,2i)$ closed for $i \ge i_0$; all $j \le 2i$ closed for $i \ge 1.7\cdot10^{8}$ (given (G1)–(G4)); closure margins $0.0574$, $0.0277$, $0.0062$** | **PROVED** |
| Computation E2.16 | Frontier sup for $i \le 500$: $0.591623$ at $(30,7)$; 40 violations of $0.36$, all $i \le 23$; sup $0.357355$ ($i\ge30$), $0.339629$ ($i\ge50$), $0.291824$ ($i\ge100$) | PROVED (computation) |
| — | Lemma S7(2.0) with any $i_0 \le 23$ | FALSE (by E2.16) |
| — | Erdős #699 in general; any $j > 2i$; the residue $i < i_1$, $j \le 2i$ | OPEN (not claimed) |

**What is not proved.** Erdős #699 is not solved by this
document. The new content is exactly: an explicit strengthening
of EEES78's exponent in the frontier window (Theorem E2.10 and
its corollaries), and the resulting closure of the region
$j \le 2i$ for $i \ge 170{,}000{,}000$ modulo the given inputs
(G1)–(G4). The finite residue $i < 170{,}000{,}000$,
$3i/2 < j \le 2i$, $N(i,j) > 20{,}000$ remains to be checked by a
targeted finite computation (§7.1), and $j > 2i$ remains open.

## Appendix: companion code

`P-E2_checks.py` (same directory; Python standard library only;
total runtime $\approx$ 12 s): Part 1 computes the Lemma E2.8
suprema by exact `Fraction` enumeration of the 26 / 31 / 36
critical points in the three $\alpha$-ranges; Part 2 assembles
the Theorem E2.10 / Corollary E2.11 / E2.12 bounds from the
stated formulas (it prints $\theta_u \le 0.326106$, $0.355205$,
$0.413644$ before the document's upward roundings); Part 3
evaluates the Lemma E2.14 constants
($D_{0.617}(2) = 0.001549$, $D_{0.580}(7/4) = 0.019398$) and
$\varphi_{\mathrm{req}}(i_0, 2i_0) = 0.61631144$ by `lgamma`;
Part 4 is Computation E2.16.
