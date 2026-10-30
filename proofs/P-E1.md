# Prover E1 (independent) — Strategy S7: Lemma S7(2.0)

**Problem #699.** For $1 \le i < j \le n/2$, $\binom{n}{i}$ and
$\binom{n}{j}$ always share a prime factor $\ge i$.

**Provenance and independence.** This document attacks Cycle 2 crux 1
(`CYCLE1.md` §8, item 1): prove Lemma S7(2.0) of `strategies/S7.md`
§§3–5. It was written from S7 and the established ground truth below,
without reading the other Cycle 2 prover's file. Every analytic step
is made explicit; the only external inputs are three published
explicit estimates (Dusart's $\pi$ bound, Dusart's $\theta$ bound,
Robbins' Stirling bounds), each cited with its exact range of
validity in §1 and its verification status in §8. All other numbers
come from proofs given here or from the computation of §7
(script `proofs/P-E1_empirical.py`, Python standard library only).

**Headline outcome. Lemma S7(2.0) is PROVED** (modulo the three cited
published estimates) with the explicit constants
$$i_0 = 200{,}000{,}000, \qquad \delta = 0.004,$$
i.e. $\theta_u(n,i) \le 0.356$ for all $i \ge i_0$ and
$4i \le n \le N(i,2i)$. With the key lemma this closes $j \le 2i$ for
all $i \ge i_0$ (§6): the ratio $j = 2i$ itself with margin $0.028$
over the required exponent, and the intermediate strip
$3i/2 < j < 2i$ (whose windows dip to $\alpha \in [3,4]$) by a
companion bound, Lemma E1.11, with margin $0.005$.
The $\alpha = 4$ edge does **not** fail: the binding band for
S7(2.0) is $\alpha \in [4,5]$, where the proved ratio bound is
$0.3557$. Two honest qualifications, developed in §7 and §8:
(i) $\theta_u > 0.36$
does occur in the window at small $i$ — exactly $40$ pairs with
$i \le 500$, all with $i \le 23$, the two largest being EEES78
exception pairs — so no $i_0 \le 23$ can work, and the empirical
threshold crossing in $i \le 500$ sits between $i = 23$ and $i = 30$;
(ii) the sharp form of Dusart's $\pi$ bound is load-bearing: the
cruder Rosser–Schoenfeld constant $1.25506$ loses the margin by
$\approx 0.04$ in $\theta_u$ (§8, item 3). The fallbacks named in the
brief (extending the carry analysis to $(i/3,i/2]$; S7(1.75)) were
**not needed**.

**Established ground truth (assumed, not reproved).**

1. *EEES78.* $V_i(n) > \binom{n}{i}^{1/2}$ outside the 12 exception
   pairs $(8,3),(9,4),(10,5),(12,5),(21,7),(21,8),(30,7),(33,13),
   (33,14),(36,13),(36,17),(56,13)$. All have $i \le 17 < i_0$.
2. *Key lemma.* If $d \mid \binom{n}{i}$ and
   $\gcd(d, \binom{n}{j}) = 1$ then $d \mid \binom{j}{i}$; in
   particular a counterexample triple has $V_i(n) \mid \binom{j}{j-i}$,
   hence $V_i(n) \le \binom{j}{j-i}$.
3. *Finite reduction.* A counterexample with $(n,i)$ not an exception
   pair satisfies $n \le N(i,j)$, the largest $n$ with
   $\binom{n}{i} < \binom{2j}{2(j-i)}$.
4. *Already closed:* $j \le 3i/2$; $n = 2j$; $i \in \{1,2\}$; the
   boundary family $j = \lfloor 3i/2 \rfloor + 1$.
5. *Sweep.* No counterexample with $n \le 20{,}000$.

**Notation.** $\binom{n}{i} = uv$ with $u$ supported on primes
$< i$ and $v = V_i(n)$ on primes $\ge i$;
$\theta_u = \log u / \log \binom{n}{i}$; $\alpha = n/i$;
$e_p = v_p\binom{n}{i}$; $\theta(x) = \sum_{p \le x} \log p$;
$\log$ is natural. For $\alpha > 1$ set
$$f(\alpha) := \alpha \log \alpha - (\alpha-1)\log(\alpha-1)
= \alpha H(1/\alpha),$$
so that $\log \binom{\alpha i}{i} \approx i f(\alpha)$ (Lemma E1.2).
Note $f'(\alpha) = \log\frac{\alpha}{\alpha-1} > 0$: $f$ is strictly
increasing. Values used (computed in §7's register, margins $\gg$
float error): $f(4) = \log\frac{256}{27} = 2.249341$,
$f(5) = \log\frac{3125}{256} = 2.502012$,
$f(13/2) = 2.790600$, $4\log 2 = 2.772589$.

---

## 1. The three cited explicit estimates

**Input D-$\pi$ (Dusart; CITED, published).** For $x \ge 355991$,
$$\pi(x) \;\le\; \frac{x}{\log x}\Big(1 + \frac{1}{\log x}
+ \frac{2.51}{\log^2 x}\Big).$$
(Dusart's explicit $\pi$ bounds; the identical statement, constants,
and threshold are quoted as "Theorem 2.1 (Dusart)" in Dusart's
estimates survey, arXiv:math/0509095, and in the secondary literature
checked in §8.)

**Input D-$\theta$ (Dusart 2010, Thm 5.2; CITED, published).** For
$x \ge 89967803$,
$$|\theta(x) - x| \;<\; \frac{x}{\log^3 x}.$$
(Quoted verbatim, with this theorem number and threshold, in two
independent secondary sources checked in §8.)

**Input R (Robbins 1955; CITED, published).** For $m \ge 1$,
$m! = \sqrt{2\pi m}\,(m/e)^m e^{r_m}$ with
$\frac{1}{12m+1} < r_m < \frac{1}{12m}$.

No other analytic number theory is used. In particular no
prime-gap theorem and no unexplicit $o(1)$ appears anywhere below:
every error term is a named, monotone, evaluated function.

---

## 2. Two elementary lemmas

**Lemma E1.1 (Erdős's lemma). PROVED.**
*If $p^a \| \binom{n}{i}$ then $p^a \le n$; equivalently
$e_p \le \log n / \log p$ for every prime $p$.*

*Proof.* By Legendre's formula,
$e_p = \sum_{e \ge 1} \big(\lfloor n/p^e \rfloor - \lfloor i/p^e
\rfloor - \lfloor (n-i)/p^e \rfloor\big)$. Each bracket is the
difference of a floor and the sum of two floors of parts, hence lies
in $\{0,1\}$; and it is $0$ when $p^e > n$, since then all three
floors are $0$ except possibly $\lfloor i/p^e \rfloor =
\lfloor (n-i)/p^e \rfloor = 0$ as well. Hence
$e_p \le \#\{e \ge 1 : p^e \le n\} \le \log n/\log p$. $\square$

**Lemma E1.2 (binomial lower bound). PROVED (modulo Input R).**
*For $n = \alpha i$ with $\alpha \ge 4$ (indeed any $\alpha > 1$),*
$$\log \binom{n}{i} \;\ge\; i f(\alpha)
- \tfrac12 \log(2\pi i) - \tfrac16 .$$

*Proof.* Apply Input R to $n!$, $i!$, $(n-i)!$ and subtract. The main
terms give $n\log n - i\log i - (n-i)\log(n-i)
= i\big[\alpha\log\alpha - (\alpha-1)\log(\alpha-1)\big]
= i f(\alpha)$ (the $\log i$ terms cancel:
$\alpha - 1 - (\alpha-1) = 0$). The square-root terms give
$\frac12 \log\frac{n}{2\pi i (n-i)}
= -\frac12\log\big(2\pi i \cdot \frac{\alpha-1}{\alpha}\big)
\ge -\frac12 \log(2\pi i)$, since $\frac{\alpha-1}{\alpha} < 1$.
The remainder satisfies
$r_n - r_i - r_{n-i} > -\frac{1}{12i} - \frac{1}{12(n-i)} \ge
-\frac16$. $\square$

*Remark.* The correction $\frac12\log(2\pi i) + \frac16$ is $O(\log i)$
against a main term $\ge 2.24\,i$; at $i = i_0$ its relative size is
$5.3\times10^{-8}$ (evaluated in §5). It is carried explicitly in
every ratio below, never absorbed into an $o(1)$.

---

## 3. The window cap: $N(i,2i) < 13i/2$

**Lemma E1.3. PROVED (modulo Input R).**
*For all $i \ge i_0 = 2\times10^8$, $N(i,2i) < 13i/2$. Hence in the
frontier window for $j = 2i$ it suffices to treat
$4i \le n \le 13i/2$, i.e. $\alpha \in [4, 13/2]$.*

*Proof.* For $j = 2i$ the defining target of $N(i,2i)$ is
$\binom{2j}{2(j-i)} = \binom{4i}{2i} \le 2^{4i}$, so
$\log\binom{4i}{2i} \le 4i\log 2 = 2.772589\,i$. Let $n \ge 13i/2$,
so $\alpha \ge 13/2$ and, $f$ being increasing, Lemma E1.2 gives
$$\log\binom{n}{i} \ge i f(13/2) - \tfrac12\log(2\pi i) - \tfrac16
= i\Big(2.790600 - \frac{\frac12\log(2\pi i) + 1/6}{i}\Big).$$
The function $i \mapsto \frac{\frac12\log(2\pi i)+1/6}{i}$ is
decreasing for $i > e$ (as $(\log x)/x$ is), so for $i \ge i_0$ it is
at most its value at $i_0$, namely $5.3\times10^{-8}$ (direct
evaluation: $\frac12\log(2\pi\cdot2\times10^8) + 1/6 = 10.64$;
$10.64 / (2\times10^8) = 5.3\times10^{-8}$). Hence
$\log\binom{n}{i} \ge (2.790600 - 0.0000001)\,i
> 2.772589\,i \ge \log\binom{4i}{2i}$,
with margin $0.018010\,i$. So no $n \ge 13i/2$ satisfies the defining
inequality of $N(i,2i)$. $\square$

*Remark.* The true ratio $N(i,2i)/i \to 6.38$ (computed exactly at
$i \le 500$ in §7: $6.392$ at $i = 500$); the cap $13/2 = 6.5$ is what
the elementary bounds above prove, and $6.5$ is the right endpoint
used throughout. This is the precise content of the task's
"$\alpha \in [4, \sim 6.4]$".

---

## 4. The small primes: $p \le i/2$ (ranges R1 + R2 of S7 §5)

S7 splits $p \le \sqrt i$ (R1) from $\sqrt i < p \le i/2$ (R2). The
split is unnecessary: Lemma E1.1 applies to **every** $p \le i/2$
with the same force, and a single term $\pi(i/2)\log n$ bounds
R1 + R2 together (S7's separate R1 term is absorbed, not added).

**Lemma E1.4. PROVED (modulo Input D-$\pi$).**
*Let $i \ge i_0$ and $i \le n \le \alpha_{\max} i$ with
$\alpha_{\max} \in \{4, 5, 13/2\}$. Write $L = \log(i/2)$
(so $L \ge \log 10^8 = 18.4207$). Then*
$$\sum_{p \le i/2} e_p \log p \;\le\; \pi(i/2)\,\log n
\;\le\; i \cdot \frac12\Big(1 + \frac{\log(2\alpha_{\max})}{L}\Big)
\Big(1 + \frac1L + \frac{2.51}{L^2}\Big) \;=: i\,B_2(\alpha_{\max}, L),$$
*and $B_2$ is decreasing in $L$, hence in $i$. Numerically,
$B_2(4, \log 10^8) = 0.59077$, $B_2(5, \log 10^8) = 0.59720$ and
$B_2(13/2, \log 10^8) = 0.60476$; these are therefore upper bounds
for all $i \ge i_0$.*

*Proof.* By Lemma E1.1, $e_p \log p \le \log n$ for each $p$, so the
sum is at most $\pi(i/2)\log n$. Since $i/2 \ge 10^8 \ge 355991$,
Input D-$\pi$ applies at $x = i/2$:
$\pi(i/2) \le \frac{i/2}{L}\big(1 + \frac1L + \frac{2.51}{L^2}\big)$.
Also $n \le \alpha_{\max} i = 2\alpha_{\max} e^{L}$, so
$\log n \le L + \log(2\alpha_{\max})$. Multiplying gives the display.
Each factor $1 + c/L$ and $1 + 1/L + 2.51/L^2$ is decreasing in $L$
for $L > 0$, so $B_2$ is decreasing in $L$. The numerical values are
direct evaluations (register, §7). $\square$

*Remark on the prime $p = i$.* If $i$ itself is prime, $p = i$ is
**not** in $u$: by definition $v = V_i(n)$ carries all primes
$\ge i$. The ranges of Lemmas E1.4 and E1.5 are $p \le i/2$ and
$i/2 < p < i$, a partition of $\{p : p < i\}$; nothing is charged
for $p = i$ on the $u$ side, correctly.

---

## 5. The near-$i$ primes: $i/2 < p < i$ (range R3)

**Lemma E1.5 (R3 characterisation; sharpens S7 Lemma B). PROVED.**
*Let $i > 26$ and $4i \le n \le 13i/2$. Let $p$ be prime with
$i/2 < p < i$. Then $e_p \in \{0,1\}$, and $e_p = 1$ if and only if
the block $(n-i, n]$ contains exactly two multiples of $p$.
Consequently, with $q = \lfloor n/p \rfloor \in \{4, \dots, 12\}$,*
$$e_p = 1 \iff p \in (A_q, B_q] := \Big(\max\Big\{\frac{n}{q+1},
\frac{n-i}{q-1}, \frac i2\Big\},\; \min\Big\{\frac nq, i\Big\}\Big].$$

*Proof.* Since $i > 4$, $v_p(i!) = \lfloor i/p \rfloor = 1$ (as
$1 < i/p < 2$ and $p^2 > i$). Legendre's formula gives
$e_p = \sum_{e\ge1} t_e$ with
$t_1 = \lfloor n/p \rfloor - 1 - \lfloor (n-i)/p \rfloor
= M_p - 1$, where $M_p$ is the number of multiples of $p$ in
$(n-i, n]$. For $e \ge 2$: $p^e \ge p^2 > i^2/4 > 13i/2 \ge n$
(the middle inequality is $i > 26$), so every floor in $t_e$ is $0$
and $t_e = 0$. **This discharges both error cases named in the
brief**: a multiple of $p^2$ in the block would force $p^2 \le n$,
impossible here, and $e_p \ge 2$ would force either $t_1 \ge 2$ or
some $t_e \ge 1$, $e \ge 2$. Finally $M_p \le 2$: three multiples
of $p$ in $(n-i, n]$ would span $\ge 2p > i$, but two integers of the
block differ by $\le i - 1 < i$. Hence $e_p = M_p - 1 \in \{0,1\}$.
Now $M_p = 2$ iff $\lfloor n/p \rfloor - \lfloor (n-i)/p \rfloor = 2$.
Setting $q = \lfloor n/p \rfloor$: $\lfloor n/p \rfloor = q$ iff
$n/(q+1) < p \le n/q$, and $\lfloor (n-i)/p \rfloor \le q - 2$ iff
$(n-i)/p < q-1$ iff $p > (n-i)/(q-1)$ ($q \ge 4 > 1$). Intersecting
with $i/2 < p < i$ gives $(A_q, B_q]$. Finally
$n/p \in (n/i, 2n/i) = (\alpha, 2\alpha) \subset (4, 13)$, so
$q \in \{4, \dots, 12\}$. $\square$

**Lemma E1.6 (total interval length). PROVED.**
*For $\alpha \in [3, 13/2]$, with $A_q, B_q$ as in Lemma E1.5
(for $\alpha \in [3,4]$ the same formula, with
$q \in \{3, \dots, 7\}$),*
$$\sum_{q} \frac{B_q - A_q}{i} \;\le\; \frac15 \;=\; 0.20,$$
*the sum being over the at most nine integers $q$ with
$\alpha < q < 2\alpha$ (empty intervals contributing $0$).*

*Proof.* In units of $i$, the $q$-th length is
$\ell_q(\alpha) = \max\big(0,\ \min\{\alpha/q, 1\}
- \max\{\alpha/(q+1), (\alpha-1)/(q-1), 1/2\}\big)$.
For $q \le \alpha$ the interval is empty or a point (lower end
$\ge (\alpha-1)/(q-1) \ge 1 \ge$ upper end when $q \le 3$ and
$\alpha \ge 3$; in general $\min\{\alpha/q,1\} \le
\max\{\alpha/(q+1), (\alpha-1)/(q-1)\}$ off the range
$\alpha < q < 2\alpha$); for $q \ge 2\alpha$: upper end
$\le \alpha/q \le 1/2 \le$ lower end. Fix $q$. Every kink of
$\ell_q$ on $[3, 13/2]$ is at a half-integer: the competing lower
terms agree pairwise exactly when $\alpha = (q+1)/2$ (indeed
$\frac{\alpha-1}{q-1} = \frac{\alpha}{q+1} \iff q = 2\alpha - 1$,
and each equals $1/2$ iff $\alpha = (q+1)/2$); the upper terms agree
when $\alpha = q$; and $\ell_q$ can switch between $0$ and positive
only where upper $=$ lower, which the same equations place at
$\alpha \in \{q/2, q, (q+1)/2\}$. Hence
$L(\alpha) := \sum_q \ell_q(\alpha)$ is **linear** on each
$[m/2, (m+1)/2]$, $m = 6, \dots, 12$, so its maximum on $[3, 13/2]$
is attained at a half-integer endpoint. Exact rational evaluation
(Fraction arithmetic, §7):
$$\begin{aligned}
L(3) &= \tfrac{11}{60}, & L(7/2) &= \tfrac15, &
L(4) &= \tfrac{79}{420}, & L(9/2) &= \tfrac{331}{1680},\\
L(5) &= \tfrac{479}{2520}, & L(11/2) &= \tfrac{493}{2520}, &
L(6) &= \tfrac{5297}{27720}, & L(13/2) &= \tfrac{2701}{13860},
\end{aligned}$$
i.e. $0.18333,\ 0.20000,\ 0.18810,\ 0.19702,\ 0.19008,\ 0.19563,\
0.19109,\ 0.19488$. The largest is $1/5$ at $\alpha = 7/2$. $\square$

**Lemma E1.7 (R3 bound). PROVED (modulo Input D-$\theta$).**
*Let $i \ge i_0$ and $4i \le n \le 13i/2$. Then, with
$L = \log(i/2)$,*
$$\sum_{i/2 < p < i} e_p \log p \;\le\;
i\Big(0.20 + \frac{18}{L^3}\Big) \;\le\; 0.20288\,i
\qquad (i \ge i_0),$$
*and the middle bound is decreasing in $i$.*

*Proof.* By Lemma E1.5 each prime with $e_p = 1$ lies in exactly one
$(A_q, B_q]$ (its own $q = \lfloor n/p \rfloor$), and $e_p \le 1$,
so the sum is at most $\sum_q \sum_{p \in (A_q, B_q]} \log p
= \sum_q \big(\theta(B_q) - \theta(A_q)\big)$.
All endpoints satisfy $i/2 \le A_q < B_q \le i$, hence are
$\ge 10^8 \ge 89967803$ and Input D-$\theta$ applies at both:
$\theta(B_q) - \theta(A_q) \le (B_q - A_q) + B_q/\log^3 B_q
+ A_q/\log^3 A_q \le (B_q - A_q) + 2i/L^3$,
using $A_q, B_q \le i$ and $\log A_q, \log B_q \ge L$. There are at
most nine values of $q$, so the error terms contribute at most
$18i/L^3$. Lemma E1.6 bounds $\sum_q (B_q - A_q) \le 0.20\,i$.
At $i = i_0$, $L = \log 10^8 = 18.4207$, $L^3 = 6250.6$,
$18/L^3 = 0.00288$, giving $0.20288$; $18/L^3$ decreases in $i$.
$\square$

**Lemma E1.7b (R3 bound on $\alpha \in [3,4]$). PROVED
(modulo Input D-$\theta$).**
*Let $i \ge i_0$ and $3i \le n \le 4i$. Then*
$$\sum_{i/2 < p < i} e_p \log p \;\le\;
i\Big(0.20 + \frac{10}{L^3}\Big) \;\le\; 0.20160\,i,
\qquad L = \log(i/2).$$

*Proof.* Lemma E1.5's proof is verbatim (it uses only $i > 26$ and
$n \le 13i/2$): $e_p \in \{0,1\}$, and $e_p = 1$ iff
$p \in (A_q, B_q]$ for its $q = \lfloor n/p \rfloor$, now with
$n/p \in (\alpha, 2\alpha) \subset (3, 8)$, so
$q \in \{3, \dots, 7\}$ — five values. The $\theta$-difference bound
of Lemma E1.7 then gives error $\le 5 \cdot 2i/L^3 = 10i/L^3$, and
Lemma E1.6 (extended range) gives $\sum_q (B_q - A_q) \le 0.20\,i$.
At $i \ge i_0$, $10/L^3 \le 0.00160$. $\square$

---

## 6. Main theorem and closure

**Theorem E1.8 (Lemma S7(2.0), with explicit constants). PROVED
(modulo Inputs D-$\pi$, D-$\theta$, R).**
*For all $i \ge i_0 = 200{,}000{,}000$ and all $n$ with
$4i \le n \le N(i, 2i)$,*
$$\theta_u(n,i) \;\le\; 0.356,
\qquad\text{i.e.}\qquad
V_i(n) \;\ge\; \binom{n}{i}^{0.644}.$$
*Hence S7(2.0) holds with $\delta = 0.36 - 0.356 = 0.004 > 0$.*

*Proof.* By Lemma E1.3, $n \le 13i/2$, so $\alpha \in [4, 13/2]$.
Split into two bands.

*Band $\alpha \in [4,5]$.* Lemmas E1.4 (with $\alpha_{\max} = 5$) and
E1.7 give $\log u \le i\,(0.59720 + 0.20288) = 0.80008\,i$ at $i_0$,
and both summands' bounds decrease in $i$. Lemma E1.2 with
$f$ increasing gives
$\log\binom{n}{i} \ge i\big(f(4) - \frac{\frac12\log(2\pi i)+1/6}{i}\big)
\ge i\,(2.249341 - 0.0000001)$ for $i \ge i_0$. Hence
$$\theta_u \le \frac{0.80008}{2.24934} = 0.35570 \le 0.356.$$

*Band $\alpha \in [5, 13/2]$.* Lemmas E1.4 (with
$\alpha_{\max} = 13/2$) and E1.7 give
$\log u \le i\,(0.60476 + 0.20288) = 0.80764\,i$; Lemma E1.2 with
$f(\alpha) \ge f(5) = 2.502012$ gives
$$\theta_u \le \frac{0.80764}{2.50201} = 0.32280 \le 0.356.$$
The band $[4,5]$ binds. All bounds used are monotone in $i$ in the
favourable direction (Lemmas E1.4, E1.7 for the numerator; the
Stirling correction per unit $i$ decreasing for the denominator),
so the evaluations at $i = i_0$ bound every $i \ge i_0$. $\square$

**Lemma E1.10 (required exponent for general $j$). PROVED
(modulo Input R).**
*For $3i/2 < j \le 2i$, write $c = j/i \in (3/2, 2]$ and
$\Phi(c) := \frac{c \log 2}{f(2c)}$. Then $\Phi$ is increasing on
$[3/2, 2]$, and for all $i \ge i_0$,*
$$\varphi_{\mathrm{req}}(i,j)
:= \frac{\log\binom{j}{j-i}}{\log\binom{2j}{i}}
\;\le\; \Phi(c) + 10^{-6} \;\le\; \Phi(2) + 10^{-6}
\;\le\; 0.61632,$$
*with $\Phi(7/4) = 0.579293$ and $\Phi(2) = 0.616311$.*

*Proof.* Numerator: $\binom{j}{j-i} \le 2^j$, so
$\log\binom{j}{j-i} \le ci\log 2$. Denominator: Lemma E1.2 with
$n' = 2j$, $\alpha' = 2c \in (3, 4]$ gives
$\log\binom{2j}{i} \ge i f(2c) - \frac12\log(2\pi i) - \frac16
\ge i\big(f(2c) - 5.3\times10^{-8}\big)$ for $i \ge i_0$, whence the
ratio is at most $\Phi(c)\big(1 + 4\times10^{-8}\big)
\le \Phi(c) + 10^{-6}$. For monotonicity:
$\Phi(c) = \frac12 \cdot \frac{\alpha \log 2}{f(\alpha)}$ with
$\alpha = 2c$; its logarithmic derivative is positive iff
$f(\alpha) > \frac{\alpha}{2} f'(\alpha)
= \frac{\alpha}{2}\log\frac{\alpha}{\alpha-1} =: h(\alpha)$.
Now $h$ is decreasing on $[3,4]$: $h'(\alpha) = \frac12\big[
\log\big(1 + \frac{1}{\alpha-1}\big) - \frac{1}{\alpha-1}\big] < 0$
since $\log(1+t) < t$; so $h(\alpha) \le h(3)
= \frac32 \log\frac32 = 0.6082 < f(3) = 1.9095 \le f(\alpha)$.
Hence $\Phi$ is increasing. Values: $\Phi(7/4)
= \frac{(7/4)\log 2}{f(7/2)} = \frac{1.213007}{2.093944}
= 0.579293$; $\Phi(2) = \frac{2\log 2}{f(4)}
= \frac{1.386294}{2.249341} = 0.616311$. $\square$

**Lemma E1.11 ($\theta_u$ on $\alpha \in [3,4]$). PROVED
(modulo Inputs D-$\pi$, D-$\theta$, R).**
*Let $i \ge i_0$ and $3i \le n \le 4i$. Then*
$$\theta_u(n,i) \le 0.4150 \quad (\alpha \in [3, 7/2]),
\qquad \theta_u(n,i) \le 0.3785 \quad (\alpha \in [7/2, 4]).$$

*Proof.* Lemma E1.4 with $\alpha_{\max} = 4$ (valid since
$n \le 4i$): $B_2(4, \log 10^8) = \frac12\big(1 + \frac{\log 8}{L}
\big)\big(1 + \frac1L + \frac{2.51}{L^2}\big) = 0.59077$ at
$L = 18.4207$, decreasing in $i$. Lemma E1.7b: R3 $\le 0.20160\,i$.
So $\log u \le (0.59077 + 0.20160)\,i = 0.79237\,i$. Lemma E1.2 with
$f(3) = \log\frac{27}{4} = 1.909542$ and
$f(7/2) = 2.093944$: ratios
$0.79237/1.909542 = 0.41497 \le 0.4150$ and
$0.79237/2.093944 = 0.37843 \le 0.3785$. Monotonicity in $i$ as
before. $\square$

*Remark.* Lemma E1.11 at $\alpha \in [7/2, 4]$ is stronger than
S7(1.75)'s target $\theta_u \le 0.41$ on its overlap; the brief's
fallback (b) is thus discharged as a byproduct, in the range where
the strip below needs it.

**Theorem E1.9 (closure of $j \le 2i$ for $i \ge i_0$). PROVED
(modulo Theorem E1.8, Lemmas E1.10–E1.11, and the established
ground truth).**
*There is no counterexample $(n, i, j)$ with $i \ge i_0$ and
$i < j \le 2i$.*

*Proof.* Suppose $(n,i,j)$ is a counterexample with $i \ge i_0$ and
$i < j \le 2i$. The region $j \le 3i/2$ is already closed, so
$3i/2 < j \le 2i$. Since $(n,i)$ is not an exception pair (all have
$i \le 17 < i_0$), the finite reduction gives $n \le N(i,j)$, and
$N(i,j) \le N(i,2i)$ because the target
$\binom{2j}{2(j-i)} = \binom{2j}{2i}$ is increasing in $j$
(successive ratio $\frac{(2j+2)(2j+1)}{(2j+2-2i)(2j+1-2i)} > 1$).
Also $n \ge 2j > 3i$. By the key lemma,
$v \le \binom{j}{j-i}$, and $\binom{j}{j-i} \le \binom{2i}{i}$
(fixed lower index $j - i$: $\binom{j}{j-i} \le \binom{2i}{j-i}$ as
$j \le 2i$; then $\binom{2i}{j-i} \le \binom{2i}{i}$ as
$j - i \le i$ and $\binom{2i}{\cdot}$ increases on $[0, i]$).

*Case A: $n \ge 4i$ (includes $j = 2i$, where $n \ge 2j = 4i$
always).* Theorem E1.8 applies ($4i \le n \le N(i,j) \le N(i,2i)$):
$v \ge \binom{n}{i}^{0.644} \ge \binom{4i}{i}^{0.644}$. By Lemma
E1.10, $\varphi_{\mathrm{req}}(i,2i) \le 0.61632$, i.e.
$\binom{2i}{i} \le \binom{4i}{i}^{0.61632}$; hence
$v \ge \binom{4i}{i}^{0.644} > \binom{4i}{i}^{0.61632}
\ge \binom{2i}{i} \ge v$, a contradiction. Margin:
$0.644 - 0.61632 = 0.0277$.

*The number $\varphi_{\mathrm{req}}(i,2i)$, computed directly.*
By `math.lgamma` (error $\lesssim 10^{-12}$ in the ratio at these
sizes, dwarfed by the margin):
$\varphi_{\mathrm{req}} = 0.600557,\ 0.608597,\ 0.611899,\ 0.615163,\
0.615679,\ 0.616229,\ 0.616301$ at
$i = 20, 50, 100, 500, 1000, 10^4, 10^5$, and
$\varphi_{\mathrm{req}}(i_0 - 1) = \varphi_{\mathrm{req}}(i_0)
= \varphi_{\mathrm{req}}(i_0 + 1) = 0.6163114450$ to the digits
shown, against the limit $\Phi(2) = 0.6163114534$ — approach from
below, as S7 §3 states, and consistent with the analytic bound
$0.61632$ of Lemma E1.10.

*Case B: $3i < n < 4i$ (so $j < 2i$).* Then $c = j/i \le n/(2i)
= \alpha/2$. Split on $\alpha$:
- $\alpha \in (3, 7/2]$: $c \le 7/4$, so Lemma E1.10 gives
  $\varphi_{\mathrm{req}}(i,j) \le \Phi(7/4) + 10^{-6}
  \le 0.57930$. Since $n \ge 2j$ gives
  $\binom{n}{i} \ge \binom{2j}{i}$, and Lemma E1.11 gives
  $\theta_u \le 0.4150$, we have
  $v = \binom{n}{i}^{1-\theta_u} \ge \binom{2j}{i}^{0.5850}$.
  Since $0.5850 > 0.57930 \ge \varphi_{\mathrm{req}}(i,j)$,
  $v > \binom{2j}{i}^{\varphi_{\mathrm{req}}(i,j)}
  = \binom{j}{j-i} \ge v$, a contradiction. Margin:
  $0.5850 - 0.57930 = 0.0057$.
- $\alpha \in (7/2, 4)$: $c \le 2$, so
  $\varphi_{\mathrm{req}}(i,j) \le 0.61632$ by Lemma E1.10, and
  Lemma E1.11 gives $\theta_u \le 0.3785$, so
  $v \ge \binom{2j}{i}^{0.6215}
  > \binom{2j}{i}^{\varphi_{\mathrm{req}}(i,j)}
  = \binom{j}{j-i} \ge v$, using
  $0.6215 > 0.61632 \ge \varphi_{\mathrm{req}}(i,j)$ and the defining
  equality $\binom{2j}{i}^{\varphi_{\mathrm{req}}(i,j)}
  = \binom{j}{j-i}$. Contradiction.
  Margin: $0.6215 - 0.61632 = 0.0052$.

Both cases contradict counterexample status. $\square$

**Precise remaining inputs for the closure at all $i$.**
(1) EEES78 + finite reduction, for $n > N(i,j)$ — established
ground truth. (2) This document: all $i \ge i_0$, $j \le 2i$ —
closed. (3) $i < i_0$, $j \le 2i$: a finite residue. It is **not**
cleared by the existing sweep (which reaches $n \le 20{,}000$,
while $N(i,2i) \approx 6.4i$ exceeds that already for
$i \gtrsim 3100$), nor by Cycle 1's in-scope counts (scope
$i \le 1000$). Per the brief, the size of this residue is not
computed here; it requires a targeted finite check (sweep
technology extended to $n \le N(i,2i)$ for $i < i_0$, or an
$i_0$-lowering refinement of §§4–5, e.g. via the brief's fallback
(a), the carry analysis on $(i/3, i/2]$ and $(i/4, i/3]$, which
would sharpen Lemma E1.4, the numerically dominant term).

---

## 7. Adversarial empirical test (computation)

**Method.** Exact $\theta_u$ over the full frontier window for
$i \le 500$: $n$ ranges over $[4i, N(i,2i)]$ with $N(i,2i)$ computed
**exactly** by binary search on $\binom{n}{i} < \binom{4i}{2i}$
(`math.comb`); $\log u$ by an incremental $i$-sweep (factor $n-i$ and
$i+1$ by an spf sieve, update by prime factors $< i+1$, add the
newly entering prime $p = i$ with its exact Legendre exponent);
$\log\binom{n}{i}$ by `lgamma`. **Validation:** the incremental
values agree with brute-force Legendre factorisation on **all**
pairs with $n \le 300$ (22,500 pairs, 0 mismatches at tolerance
$10^{-9}$) and on 300 seeded random pairs with $n \le 3400$
(0 mismatches). Every headline value below was additionally
re-verified by **exact integer comparison**: $\theta_u > k/100 \iff
u^{100} > \binom{n}{i}^{k}$ with $u$ built from Legendre exponents.
Total: 299,743 window pairs; wall time 62 s. Script:
`proofs/P-E1_empirical.py`.

**Window shape.** $N(i,2i)/i = 6.300,\ 6.380,\ 6.380,\ 6.388,\ 6.392$
at $i = 10, 50, 100, 250, 500$; $\max N = 3196$ at $i = 500$ —
consistent with Lemma E1.3's cap $6.5$ and the limit $\approx 6.38$.

**Suprema over the window** ($i \le 500$, $4i \le n \le N(i,2i)$):

| restriction | sup $\theta_u$ | at $(n,i)$ | $\alpha$ |
|---|---|---|---|
| $i \ge 1$ | 0.59162 | (30, 7) † | 4.286 |
| $i \ge 10$ | 0.51219 | (56, 13) † | 4.308 |
| $i \ge 30$ | 0.35735 | (145, 32) | 4.531 |
| $i \ge 50$ | 0.33963 | (378, 61) | 6.197 |
| $i \ge 100$ | 0.29182 | (536, 114) | 4.702 |
| $i \ge 200$ | 0.26051 | (1170, 283) | 4.134 |
| $i \ge 300$ | 0.24831 | (1705, 383) | 4.452 |

† EEES78 exception pair. Exact brackets (integer comparisons):
$(145,32) \in (0.35, 0.36]$; $(378,61) \in (0.33, 0.34]$;
$(30,7) \in (0.59, 0.60]$; $(56,13) \in (0.51, 0.52]$;
$(536,114) \in (0.29, 0.30]$. The $i \ge 50$ and $i \ge 100$ rows
extend and agree with S7 §2's frontier table ($0.3396$ at $(378,61)$;
$0.2918$ for $i \ge 100$).

**Violations of $0.36$ — reported prominently.** Exactly **40**
window pairs with $i \le 500$ have $\theta_u > 0.36$, **every one
with $i \le 23$** (largest $i$: $(136, 23)$, $\theta_u = 0.38752$);
all 40 were confirmed by the exact integer test
$u^{100} > \binom{n}{i}^{36}$. The two largest, $(30,7)$ and
$(56,13)$, are EEES78 exception pairs. No pair with
$30 \le i \le 500$ violates $0.36$ (sup $0.35735$ at $(145,32)$,
itself exactly bracketed in $(0.35, 0.36]$). Consequences, stated
exactly: the bound $\theta_u \le 0.36$ is **false** for any
$i_0 \le 23$; empirically on $i \le 500$ it holds from $i = 30$ on,
but that is a computation over a finite range, **not** a proof for
$30 \le i < i_0$; the proved $i_0 = 2\times10^8$ of Theorem E1.8 is
what the explicit estimates of §1 deliver, and the gap between the
empirical threshold ($\le 30$) and the proved $i_0$ is the honest
cost of those estimates (see §8, item 3).

**Numerical register for §§1–6** (all evaluated with Python
`math`/`fractions`, float error $\lesssim 10^{-12}$, margins
$\ge 10^{-3}$ except where noted): $f(3) = \log\frac{27}{4}
= 1.909542$, $f(7/2) = 2.093944$, $f(4) = 2.249341$,
$f(5) = 2.502012$, $f(13/2) = 2.790600$, $4\log 2 = 2.772589$,
$f(13/2) - 4\log 2 = 0.018011$; $L(i_0) = \log 10^8 = 18.420681$,
$L^3 = 6250.6$, $18/L^3 = 0.002880$, $10/L^3 = 0.001600$;
$B_2(4, L(i_0)) = 0.590767$, $B_2(5, L(i_0)) = 0.597197$,
$B_2(13/2, L(i_0)) = 0.604758$;
band ratios $0.800077/2.249341 = 0.355694$,
$0.807638/2.502012 = 0.322795$, $0.792370/1.909542 = 0.414970$,
$0.792370/2.093944 = 0.378430$;
$\Phi(7/4) = 0.579293$, $\Phi(2) = 0.616311$,
$h(3) = \frac32\log\frac32 = 0.608198$;
$\frac{\frac12\log(2\pi i_0) + 1/6}{i_0} = 5.3\times10^{-8}$;
$\varphi_{\mathrm{req}}$ values as in Theorem E1.9, with analytic
bound $0.61632$ and evaluated value $0.6163114450$ at $i = i_0$.

---

## 8. Verification register, barriers, and gaps

1. **Cited inputs.** D-$\pi$: statement, constants
   ($1, 1, 2.51$) and threshold ($355991$) agree across Dusart's
   estimates survey (arXiv:math/0509095, Thm 2.1) and two further
   secondary sources quoting it. D-$\theta$: statement, threshold
   ($89967803$) and attribution (Dusart 2010, Thm 5.2) agree in two
   independent secondary sources. Input R (Robbins 1955) is the
   standard explicit Stirling form, also used in this campaign's
   P-C2 (its Lemma 2.6). None of the three primary texts was opened
   in this session; the citations are labelled CITED, and Theorem
   E1.8 is conditional on them exactly as P-C2's theorems are
   conditional on their cited inputs.
2. **What is proved unconditionally here.** Lemmas E1.1, E1.5,
   E1.6 and all of §7 (computation) use no external input. Lemmas
   E1.2, E1.3 use only Input R. Lemma E1.4 uses only D-$\pi$;
   Lemma E1.7 only D-$\theta$.
3. **The exact barrier for weaker inputs (brief requirement 1(c),
   applied to the estimates, not the lemma).** The sharp D-$\pi$
   form is load-bearing. With the Rosser–Schoenfeld bound
   $\pi(x) \le 1.25506\,x/\log x$ ($x \ge 17$) in Lemma E1.4, the
   band-$[4,5]$ numerator at $i_0$ becomes
   $1.25506 \cdot \frac12 \cdot \frac{\log(5 i_0)}{\log(i_0/2)}
   + 0.20288 = 0.7057 + 0.2029 = 0.9086$, giving ratio
   $0.9086/2.24934 = 0.4039 > 0.36$: **failure by $0.044$ in
   $\theta_u$**, localised entirely in R1+R2. Likewise D-$\theta$
   with only $|\theta(x) - x| < 3.965\,x/\log^2 x$ (a weaker Dusart
   form) would inflate Lemma E1.7's error to $18 \cdot 3.965/L^2
   \approx 0.21$ at $i_0$ — also fatal. With the sharp forms, the
   margins at $i_0$ are: band $[4,5]$: $0.0043$ in $\theta_u$;
   band $[5, 13/2]$: $0.0372$; window cap: $0.018\,i$ in
   $\log\binom{n}{i}$; closure: $0.0277$ in the exponent. The
   fallbacks (a) (carry analysis on $(i/3, i/2]$, $(i/4, i/3]$) and
   (b) (S7(1.75)) were therefore not needed as fallbacks: (b)'s
   content on $\alpha \in [7/2, 4]$ is proved anyway as Lemma
   E1.11, and (a) remains the natural tool for lowering $i_0$
   (it would sharpen Lemma E1.4, the dominant term).
4. **The strip $3i/2 < j < 2i$ (a near-miss in drafting, now
   closed).** Theorem E1.8 alone does **not** close this strip,
   because its windows start at $\alpha = 2j/i < 4$. The closure in
   Theorem E1.9, Case B, rests on the two additional proved inputs
   E1.10 and E1.11, whose margins are the thinnest in the document
   ($0.0057$ and $0.0052$ in the exponent, against $0.0277$ for
   $j = 2i$). A verifier should check Case B's band pairing
   ($c \le \alpha/2$, from $j \le n/2$) with particular care: it is
   the one place where $\alpha$ and $j/i$ are coupled.
5. **Residue $i < i_0$.** Not computed, per the brief. It is finite
   but large, and is **not** covered by the $n \le 20{,}000$ sweep
   or by Cycle 1's counts. Closing $j \le 2i$ for **all** $i$
   requires that residue check (or a much smaller proved $i_0$);
   this document does not claim it.
6. **Claim discipline.** Nothing here proves Erdős #699. The new
   proved content is: $\theta_u \le 0.356$ on
   $\alpha \in [4, 13/2]$ for $i \ge 2\times10^8$ (Theorem E1.8),
   the companion bounds of Lemma E1.11 on $\alpha \in [3,4]$, and
   the consequent closure of all $j \le 2i$ for $i \ge i_0$
   (Theorem E1.9), modulo the three cited published explicit
   estimates and the established ground truth.

**Labels summary.** E1.1 PROVED. E1.2 PROVED (modulo R). E1.3 PROVED
(modulo R). E1.4 PROVED (modulo D-$\pi$). E1.5 PROVED. E1.6 PROVED.
E1.7 PROVED (modulo D-$\theta$). E1.7b PROVED (modulo D-$\theta$).
E1.8 PROVED (modulo D-$\pi$, D-$\theta$, R). E1.10 PROVED
(modulo R). E1.11 PROVED (modulo D-$\pi$, D-$\theta$, R).
E1.9 PROVED (modulo E1.8, E1.10, E1.11 + ground truth).
§7 computations PROVED as computations (exact integer checks for
all threshold statements).
