# Prover G2 (independent) — Cycle 2: the $\theta$ input, and flanks (a), (b), (c) of S4

**Problem (Erdős #699).** For $1 \le i < j \le n/2$, show $\gcd(V_i(n), \binom{n}{j}) > 1$,
where $V_i(n)$ is the part of $\binom{n}{i}$ supported on primes $\ge i$.
A *counterexample* is a triple with $\gcd(V_i(n), \binom{n}{j}) = 1$.

**Inputs taken as established (not reproved here).** EEES78
($V_i(n) > \binom{n}{i}^{1/2}$ outside the 12 exception pairs, all with $n \le 56$);
the key lemma (a counterexample satisfies $V_i(n) \mid \binom{j}{j-i}$, Bloom
exposition / P-A1 Lemma A1.1); the square reduction (P-A1 Lemma A1.6: a
counterexample with $(n,i)$ non-exception satisfies
$\binom{n}{i} < \binom{j}{j-i}^2$); Lemma 1 of S4/P-D2 (every prime $p > j$
dividing $\binom{n}{i}$ divides $\binom{n}{j}$, so in a counterexample every
prime factor $p \ge i$ of $\binom{n}{i}$ lies in $[i,j]$); the two-digit
classification (P-D2 D2.2/D2.7: for $p^2 > n$, $v_p\binom{n}{k} = \mathbf 1[(k \bmod p) > (n \bmod p)]$,
exponent exactly $1$); S1's per-prime bound $p^{v_p\binom{n}{i}} \le n$
(Legendre: each summand is in $\{0,1\}$ and there are $\le \log_p n$ of them);
S10 §4–§5 (bad $p \in [i, j/2]$ requires $e_p \le \lfloor \log_p j \rfloor$ and
the multi-scale condition $(\dagger)$; primes in $(j/2, j-i]$ lying in
$S(n,i)$ are automatically good when $j > 2i$); the closures of
$j \le 3i/2$, $n = 2j$, $i \in \{1,2\}$; the sweep $n \le 20{,}000$ clean.
This document does **not** prove #699. It improves the wedge constant from a
primary-verified $\theta$ bound, closes flank (c) above an explicit
$i$-threshold by a new support bound, closes two explicit sub-regions of
flank (b), and gives precise barriers and a precise $\beta$-specification
for flank (a).

**Notation.** $\theta(x) = \sum_{p \le x} \log p$, so
$\prod_{p \le x} p = e^{\theta(x)}$. In §§2–3, $\gamma = j/i \in (3/2, 2)$ (later
extended to $\gamma \ge 2$), $\alpha = n/i$, $d = j - i$,
$h(p) = -p\log p - (1-p)\log(1-p)$ (natural-log binary entropy).
$V^{>}$ (resp. $V^{\le}$) is the part of $V_i(n)$ on primes $> \sqrt n$
(resp. $\le \sqrt n$).

---

## 1. Task 1: the $\theta$ input, primary-verified, and Wedge S4-C with $K = 55$

### Claim G1.1 (PROVED as a primary-verified citation)

The best explicit bound verified in this pass from a primary source
actually fetched and read is:

> **Broadbent, Kadiri, Lumley, Ng, Wilk, "Sharper bounds for the
> Chebyshev function $\theta(x)$", arXiv:2002.11068v2 [math.NT],
> 27 Jan 2021, Corollary 2.1:** $\theta(x) \le (1 + 1.93378 \cdot 10^{-8})\,x$
> for **all** $x \ge 0$.

The paper was fetched in full text and Corollary 2.1 read on its page 4,
together with its stated proof: it combines Büthe's theorem
($\theta(x) < x$ for $0 < x \le 10^{19}$, cited there as [4, Theorem 2,
(1.7)]) with the value $M_0 = \varepsilon(19\log 10) = 1.93378 \cdot 10^{-8}$
from the paper's Table 8. *Epistemic status, stated plainly:* this is a
published explicit-estimates theorem whose proof rests on cited
computational verifications of the Riemann Hypothesis to finite height
(Büthe; Platt–Trudgian). It is used here exactly as EEES78 and the
Oliveira e Silva prime-gap computation are used elsewhere in this
campaign: as a cited published theorem, not re-verified. We set
$c_B = 1 + 1.93378\cdot 10^{-8}$.

### Claim G1.2 (PROVED as a primary-verified citation; independent corroboration)

> **Dusart, "Estimates of some functions over primes without R.H.",
> arXiv:1002.0442 [math.NT] (Math. Comp. 85 (2016), 875–888),
> Proposition 5.1:** $\vartheta(x) - x < \frac{1}{36260}x$ for all $x > 0$,
> i.e. $\theta(x) < c_D\, x$ with $c_D = 1 + \frac{1}{36260} \approx 1.0000276$,
> valid for **all** $x > 0$.

Fetched and read in full (Proposition 5.1 is on page 4 of the preprint,
with proof). The same paper's Theorem 5.2 (page 4) is also primary-read
and is used in §2: $|\theta(x) - x| < \eta_k x / \log^k x$ for $x \ge x_k$,
in particular $(k, \eta_k, x_k) = (2,\ 3.965,\ 2)$, $(2,\ 0.2,\ 3\,594\,641)$,
and its $\pi(x)$ bounds (page 2): $\pi(x) \le \frac{x}{\log x}(1 + \frac{1.2762}{\log x})$
for $x > 1$ and $\pi(x) \ge \frac{x}{\log x}(1 + \frac{1}{\log x})$ for $x \ge 599$.

### Claim G1.3 (citation status of Rosser–Schoenfeld 1975: NOT primary-verified)

Rosser–Schoenfeld 1975 itself was **not** read in this pass (no freely
fetchable full text was obtained), so the folklore attribution
"$\theta(x) < 1.1x$, Rosser–Schoenfeld" is **not** primary-verified here
and is **not used**. (For the record only: Broadbent et al., Table 1,
report the Rosser–Schoenfeld 1975 value $M_0 = 0.001102$ at $X_1 = 1$,
i.e. $\theta(x) \le 1.001102\,x$ for $x \ge 1$; that is a secondary report,
also not used.) Both primary-verified bounds above are far stronger
than $1.1x$, so the $K = 82$ fallback contemplated in the brief is
superseded.

### Claim G1.4 (PROVED: the improved constant is $K = 55$, with no range adjustment)

With $c \in \{c_B, c_D\}$ as above, $K = e^{4c}$ rounded up equals $55$:
exact rational certification (Appendix A) gives, with
$e < e_{ub} = \sum_{k=0}^{12} 1/k! + \frac{1}{12\cdot 12!} < 2.7182818285$
and $e^y \le 1/(1-y)$ for $0 \le y < 1$,
$$e^{4c_B} < e_{ub}^4 \cdot \tfrac{1}{1 - 4\cdot 1.93378\cdot10^{-8}} < 54.59816 < 55,
\qquad
e^{4c_D} < 54.60418 < 55.$$
Crucially, **neither bound has a validity threshold**: $c_B$ holds for
all $x \ge 0$ and $c_D$ for all $x > 0$. Hence there is no $x_0$, no
condition $j \ge x_0$, and no small-case disposal needed; the only
$i$-threshold in the restated wedge comes from nonemptiness of the
region itself.

**Wedge S4-C, restated (PROVED, modulo the cited inputs EEES78 and
G1.1).** *There is no counterexample with*
$$i > 55, \qquad 55\,i < n < i^2, \qquad 3i/2 < j < 2i.$$
*Proof.* Identical to P-D2 D2.11 with the primorial step replaced:
$V_i(n)$ is a product of distinct primes in $[i,j]$ (since $n < i^2$),
so $V_i(n) \le \prod_{p \le j} p = e^{\theta(j)} \le e^{c_B j}$ and
$V_i(n)^2 \le e^{2c_B j} < e^{4c_B i} < 55^i < (n/i)^i \le \binom{n}{i}
< V_i(n)^2$, a contradiction. Nonemptiness forces $i > 55$;
$(n,i)$ is not an EEES78 exception since $n > 55i > 55 \cdot 55 > 56$;
$j \le n/2$ is automatic since $j < 2i < 55i/2 < n/2$. $\blacksquare$

*Remark.* The same computation with the crude bound $\prod_{p\le x} p \le 4^x$
is what forced $256$ in Cycle 1; with $\prod_{p \le x} p \le 4^x$ replaced
by $e^{\theta(x)}$ and G1.1/G1.2, the constant drops $256 \to 55$, and
(as §3 shows) the identical chain with $j \le \Gamma i$ in place of
$j < 2i$ gives $K_\Gamma = \lceil e^{2c_B \Gamma} \rceil$.

---

## 2. Task 2: flank (c), $n \le 256\,i$ (now $n \le 55\,i$), $i > 256$, $3i/2 < j < 2i$

Throughout §2, $i > \sqrt n$ (since $n \le 256 i < i^2$), so $V^{\le} = 1$,
$V_i(n)$ is squarefree, supported on $[i, j]$, each prime in a Lemma 5
bad configuration. Write $N'(i,j)$ for the square-reduction bound:
a counterexample satisfies $\binom{n}{i} < \binom{j}{d}^2$ (P-A1 A1.6).

### Claim G2.1 (COMPUTED: exactly where the Del Pin comparison $(\ast)$ closes)

The comparison proposed in the brief,
$\binom{2j}{i}^{1/2} \ge \binom{j}{j-i}$, i.e.
$$(\ast)\qquad \binom{2j}{i} \ge \binom{j}{d}^2,$$
is exactly P-A1's pair-closure criterion (Lemma A1.7): where $(\ast)$
holds, **every** $n \ge 2j$ is excluded for that pair $(i,j)$, for all
$\alpha \ge 2\gamma$ at once. Its region was determined as follows.

(a) *Entropy boundary.* With $F(\gamma) = 2\gamma\, h(1/(2\gamma)) -
2\gamma\, h((\gamma-1)/\gamma)$ (so that
$\frac1i[\log\binom{2j}{i} - 2\log\binom{j}{d}] \to F(\gamma)$):
$F(3/2) = 0$, $F'(3/2) = -2\log 2$ (exact: at $\gamma = 3/2$ both
entropy arguments equal $1/3$, and $h(1/3) + \frac23\log 2 = \log 3$,
giving $F'(3/2) = 2\log\frac32 - 2\log 3 = -2\log 2$), and computed
values $F(1.51) = -0.013764$, $F(1.55) = -0.066933$, $F(1.6) = -0.129526$,
$F(1.75) = -0.296235$, $F(1.9) = -0.438624$, $F(2) = -0.523248$.
So for every **fixed** $\gamma > 3/2$, $(\ast)$ fails for all large $i$:
asymptotically the $(\ast)$ sub-region in the open strip
$\gamma \in (3/2, 2)$ is **empty**.

(b) *Exact finite classification, $3 \le i \le 2000$ (computed with
$\log\Gamma$ scan, spot-verified in exact integer arithmetic at
$i \in \{500, 999, 1000, 2000\}$).* For every $i$ in this range, the
set of $j \in (3i/2, 2i)$ satisfying $(\ast)$ is either empty
($i \in \{4, 6, 8\}$ — exactly the finite exceptions P-A1 A1.10
disposes of separately) or an initial segment
$\{\lfloor 3i/2 \rfloor + 1\}$ or $\{\lfloor 3i/2 \rfloor + 1, \lfloor 3i/2 \rfloor + 2\}$;
the two-point case occurs for $1859$ of the $1998$ values of $i$.
In $(\alpha, \gamma)$ coordinates: $(\ast)$ closes precisely the strip
$\gamma \le 3/2 + 2/i$ (all $\alpha \in [2\gamma, 256]$), a strip whose
width tends to $0$. This is consistent with, and sharper than, Cluster
A's theorem that $(\ast)$ holds on the whole boundary family
$j = \lfloor 3i/2 \rfloor + 1$.

(c) *The genuine threshold curve.* For fixed $\gamma$, the
key-lemma/EEES78 pair closes all $n$ with $\alpha \ge \alpha_c(\gamma)$,
where $\alpha_c(\gamma)$ is the unique root $> 2\gamma$ of
$\alpha\, h(1/\alpha) = 2\gamma\, h((\gamma-1)/\gamma)$ (i.e.
$\binom{n}{i} = \binom{j}{d}^2$ at entropy order). Computed:
$\alpha_c(1.51) = 3.054$, $\alpha_c(1.55) = 3.278$, $\alpha_c(1.6) = 3.569$,
$\alpha_c(1.75) = 4.526$, $\alpha_c(1.9) = 5.605$, $\alpha_c(2) = 6.393$.
Note $\alpha_c(\gamma)$ is barely above $2\gamma$ near $\gamma = 3/2$:
the square reduction leaves only the thin slab
$2\gamma \le \alpha < \alpha_c(\gamma)$ for any further argument.

### Claim G2.2 (PROVED: a genuine extra argument — the two-sided $\theta$ support bound — closes flank (c) for $i \ge 379$)

The plain wedge wastes the support information: it bounds
$V_i(n) \le \prod_{p \le j} p$, ignoring that every prime factor is
$\ge i$. Using **both** sides of the $\theta$ estimates:

**Theorem G2.2.** *There is no counterexample with $i \ge 379$,
$3i/2 < j < 2i$, and $2j \le n < i^2$ (any $\alpha$). In particular
flank (c) is closed for $i \ge 379$.*

*Proof.* Let $(n,i,j)$ be a counterexample in the region; $(n,i)$ is
not an exception ($n \ge 2j > 3i \ge 1137 > 56$).

*Step 1 (support bound).* $V_i(n) = \prod_{i \le p \le j} p$ (distinct
primes, §2 preamble), so $\log V_i(n) \le \theta(j) - \theta(i-1)$.
By G1.1, $\theta(j) \le c_B j$. By Dusart Theorem 5.2 with
$(k,\eta_k,x_k) = (2, 3.965, 2)$ (G1.2), for $x = i - 1 \ge 2$,
$\theta(i-1) \ge (i-1)(1 - \varepsilon(i))$ with
$\varepsilon(i) = 3.965/\log^2(i-1)$.

*Step 2 (exact binomial lower bound).* $\binom{n}{i} \ge
e^{n h(i/n)}/(n+1)$: indeed, with $p = i/n$, the binomial term
$\binom{n}{i} p^i (1-p)^{n-i}$ is the largest of the $n+1$ terms of
$(p + (1-p))^n = 1$ (the mode of $\mathrm{Bin}(n, i/n)$ is $i$, since
$(n+1)i/n \in [i, i+1)$), hence is $\ge 1/(n+1)$.

*Step 3 (reduction to $\gamma = 2$, $n = 2j$).* It suffices to show
$2[\theta(j) - \theta(i-1)] < \log\binom{n}{i}$. The right side,
$n h(i/n) - \log(n+1)$, is increasing in $n$ for $n \ge 2j$ (derivative
$-\log(1 - i/n) - \frac{1}{n+1} > 0$, since $-\log(1 - i/n) \ge i/n >
\frac{1}{n+1}$ as $i \ge 2$), so its minimum on $n \ge 2j$ is at
$n = 2j$, value $i \cdot 2\gamma h(1/(2\gamma)) - \log(2j+1)$. Define
$$\Psi(\gamma, i) = 2\gamma h\!\left(\tfrac{1}{2\gamma}\right) - 2c_B\gamma
+ 2(1-\varepsilon(i))\left(1 - \tfrac1i\right) - \frac{\log(2\gamma i + 1)}{i},$$
so the needed inequality is $\Psi(\gamma, i) > 0$ (after dividing by $i$
and using $\theta(i-1) \ge i(1-\varepsilon(i))(1 - 1/i)$).
$\Psi$ is **decreasing in $\gamma$** on $[3/2, 3]$:
$\frac{\partial}{\partial\gamma}[\gamma h(1/(2\gamma))] =
-\log(1 - \frac{1}{2\gamma}) \le \log\frac32 = 0.4055$ (the identity
$h(u) - u h'(u) = -\log(1-u)$ at $u = 1/(2\gamma) \le 1/3$), hence
$\Psi_\gamma \le 2(0.4055) - 2c_B - \frac{2}{2\gamma i + 1} < 0$.
$\Psi$ is **increasing in $i$** at fixed $\gamma = 2$: $\varepsilon(i)$
decreases, $(1 - 1/i)$ increases, and $\log(4i+1)/i$ decreases
(its derivative has numerator $\frac{4i}{4i+1} - \log(4i+1) < 0$).
Computed exactly (Appendix B): $\Psi(2, 378) = -0.0000626 < 0$ and
$\Psi(2, 379) = +0.0001945 > 0$. Hence $\Psi(\gamma, i) \ge
\Psi(2, i) \ge \Psi(2, 379) > 0$ for all $\gamma \in (3/2, 2)$ and
$i \ge 379$.

*Step 4.* Then $\binom{n}{i} > V_i(n)^2$, contradicting EEES78. $\blacksquare$

*Remarks.* (i) The margin is comfortable away from the corner:
$\Psi(2, 1000) = 0.07298$, $\Psi(2, 10^4) = 0.15461$,
$\Psi(3/2, 1000) = 0.73347$ (these are per-$i$ log margins, i.e. the
contradiction is by a factor $\ge e^{0.073 i}$ at $i = 1000$, $\gamma = 2$).
(ii) The argument uses the bad-configuration hypothesis **not at all** —
only squarefreeness, support in $[i,j]$, and two-sided $\theta$. The
bad configurations matter only for the remaining finite band (G2.4).

### Claim G2.3 (COMPUTED: barrier in the finite band — simultaneous badness is real at moderate $i$)

Search (Python stdlib, exact; Appendix C): all $40 \le i \le 160$,
$3i/2 < j < 2i$, $2j \le n \le \min(N'(i,j), 256i, i^2 - 1)$, testing
with the single-term Legendre formula valid for $p \ge i$, $n < i^2$
($e_p = \lfloor n/p \rfloor - \lfloor i/p \rfloor - \lfloor (n-i)/p \rfloor$;
bad iff $e_p = 1$ and $\lfloor (n-i)/p \rfloor = \lfloor (n-j)/p \rfloor$)
whether **every** prime of $S(n,i) \cap [i,j]$ is simultaneously bad.

**Result: 2,493 such triples**, every one with $\ge 4$ simultaneous
bad primes (for the subrange $40 \le i \le 80$: 384 triples, distributed
by bad-prime count as $\{4{:}16,\ 5{:}79,\ 6{:}140,\ 7{:}58,\ 8{:}68,\ 9{:}23\}$).
Maximum: **16 simultaneous bad primes**, at $(n, i, j) = (482, 157, 241)$
— note $n = 482 = 2j$, the very bottom of the range, and
$\binom{483}{157} < \binom{241}{84}^2$, so $n$ lies strictly inside the
square-reduction interval. Independently re-verified with the general
Legendre formula: $S(482, 157) \cap [157, 241]$ is exactly
$\{163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241\}$,
all 16 bad; the triple is rescued **only** by the 26 primes
$331, 337, \dots, 479$ of $S(482,157)$ above $j$ (all automatically
good by Lemma 1). So no argument that looks only at primes in $[i,j]$
— in particular no bad-configuration counting argument of S10 type —
can close the finite band; this is a genuine barrier, of exactly the
kind S10 §6 found at $i < 40$, now exhibited at $i = 157$ with 16
simultaneous bad primes at minimal $n$.

### Claim G2.4 (GAP: the finite band $257 \le i \le 378$)

Flank (c) with $256 < i < 379$ is **not closed here**. It is a finite
region: by the square reduction $n < \alpha_c(\gamma)\, i \le
\alpha_c(2) i \approx 6.4 i$, so a direct sweep-style check is finite
and feasible, but it was not performed in this pass, and G2.3 shows it
cannot be replaced by a local bad-prime argument. (For $i \le 256$ the
region $n \le 256 i$ is outside the flank as posed; it is partially
covered by the campaign's existing finite-scope clearance, not
re-examined here.)

---

## 3. Task 3: flank (b), $j \ge 2i$

S10 inputs used: for $j > 2i$, any $p \in S(n,i) \cap (j/2, d]$ is
automatically good (a window of length $d \ge p$ meets a multiple of
$p$, so $A_p \ge 1 \ge$ … precisely $v_p\binom{n}{j} \ge e_p \ge 1$);
bad $p \in [i, j/2]$ requires $e_p \le \lfloor \log_p j \rfloor$ and the
multi-scale condition $(\dagger)$.

### Claim G3.1 (PROVED: wedge extension to $j \le \Gamma i$ for large $n$)

For each fixed $\Gamma \ge 2$, let $K_\Gamma = \lceil e^{2c_B \Gamma} \rceil$
(certified values: $K_2 = 55$ since $e^{4c_B} < 54.59816$;
$K_3 = 404$ since $e^{6c_B} < 403.4288$; $K_4 = 2981$ since
$e^{8c_B} < 2980.9584$; Appendix A). *There is no counterexample with
$2i \le j \le \Gamma i$, $K_\Gamma i < n < i^2$, $i > K_\Gamma$.*
*Proof.* As in G1.4: $V_i(n)^2 \le e^{2\theta(j)} \le e^{2c_B \Gamma i}
< K_\Gamma^i < (n/i)^i \le \binom{n}{i} < V_i(n)^2$. $j \le n/2$ is
automatic since $K_\Gamma \ge 2\Gamma$. $\blacksquare$
So for every **fixed** $\gamma$, the part of flank (b) with
$\alpha > e^{2c_B\gamma}$ is closed; the wedge chain fails exactly
when $\gamma$ grows with $i$: it needs $\alpha > e^{2c_B\gamma}$ while
$\alpha < i$ (from $n < i^2$), impossible once
$\gamma > \frac{\log i}{2c_B}$.

### Claim G3.2 (PROVED: the support bound closes $2i \le j \le \gamma^*(i)\, i$ for $i \ge 379$, all $n$)

The proof of Theorem G2.2 never used $\gamma < 2$ except through the
monotonicity of $\Psi$ in $\gamma$, which holds on $[3/2, 3]$. Hence
for $i \ge 379$ there is no counterexample with $2j \le n < i^2$ and
$2i \le j \le \gamma^*(i)\, i$, where $\gamma^*(i)$ is the unique root
of $\Psi(\gamma, i) = 0$ in $(2, 3)$. Computed:
$\gamma^*(1000) = 2.0509$, $\gamma^*(10^4) = 2.1072$,
$\gamma^*(10^5) = 2.1310$, $\gamma^*(10^7) = 2.1511$, and the limit
(as $\varepsilon(i) \to 0$) is $\gamma^*_\infty = 2.17178$, the root of
$2\gamma h(1/(2\gamma)) - 2c_B\gamma + 2 = 0$. $\blacksquare$

### Claim G3.3 (PROVED barrier for the size/support methods beyond $\gamma^*$; the failing inequalities, with computed margins)

(a) *Key lemma alone cannot close flank (b) at minimal $n$, even at
$\gamma = 2$.* The needed inequality is
$\binom{j}{i} < \binom{2j}{i}^{1/2}$ (so that $V \le \binom{j}{i}$ and
EEES78 conflict at $n = 2j$). It **fails**: at $i = 1000$, $j = 2000$,
$\log\binom{j}{i} - \frac12\log\binom{2j}{i} = +259.7$ (computed), i.e.
$\binom{j}{i}$ exceeds the EEES78 threshold by a factor $e^{259.7}$;
asymptotically the excess is $[\gamma h(1/\gamma) - \gamma h(1/(2\gamma))] i
> 0$ for all $\gamma \ge 2$ (at $\gamma = 2$: $1.38629 - 1.12467 =
0.26162$ per unit $i$). The key lemma only starts to bite at
$\alpha \ge \alpha_c(\gamma)$ of G2.1(c) ($\alpha_c(2) = 6.393$,
$\alpha_c(2.5) = 11.149$, $\alpha_c(3) = 17.264$, $\alpha_c(4) = 33.573$).

(b) *Squarefree + support + automatic-goodness cannot close
$\gamma = 3$ at minimal $n$.* At $i = 1000$, $j = 3000$, $n = 2j$
(computed with exact $\theta$ values): the largest $V$ consistent
with squarefreeness, support in $[i,j]$, and the S10 automatic-good
exclusion of $(j/2, d]$ is $B_{\mathrm{allowed}} =
\prod_{p \in [i, j/2]} p \cdot \prod_{p \in (d, j]} p$ with
$\log B_{\mathrm{allowed}} = \theta(j/2) - \theta(i-1) + \theta(j) - \theta(d)
= 1498.4$, while the EEES78 threshold is
$\frac12\log\binom{2j}{i} = 1349.5$. The inequality that would have to
hold, $\theta(j) - \theta(d) + \theta(j/2) - \theta(i-1) <
\frac12 \log\binom{2j}{i}$, **fails by $148.9$ nats** (a factor
$e^{148.9} \approx 10^{64.7}$). Hence the constraints (EEES78,
$V \mid \binom{j}{d}$, squarefree, support, automatic goodness) are
mutually consistent at $(n,i,j) = (6000, 1000, 3000)$: no argument
using only them closes $\gamma = 3$ near $n = 2j$. The precise
remaining region for flank (b) is therefore
$\gamma^*(i) < \gamma$, $\alpha < \min(\alpha_c(\gamma), e^{2c_B\gamma})$
(with $n < i^2$), where a proof must use the bad-configuration /
multi-scale conditions $(\dagger)$ themselves, or a largest-prime-factor
input, not size alone.

(c) *Borderline (COMPUTED).* With exact $\theta$ values at $i = 1000$,
$\gamma = 2.5$, $n = 2j$: $\log B_{\mathrm{allowed}} - \frac12\log\binom{2j}{i}
= -24.7$ — the support+autogood bound **does** close that point; the
asymptotic borderline of this method is $\gamma^{**} \approx 2.504$,
the root of $h(1/(2\gamma)) = 1/2$ (allowed-support exponent
$\gamma/2$ per unit $i$ vs threshold $\gamma h(1/(2\gamma))$).
$\gamma^*(i)$ of G3.2 is what the *uniform explicit* bounds certify;
exact-$\theta$ computations do better at individual points, and the
method's true asymptotic reach is $\gamma^{**}$, beyond which (b)'s
barrier is genuine (margin $+148.9$ at $\gamma = 3$ and growing:
at $\gamma = 4$, $i = 1000$, the allowed-support margin is $+457.5$).

---

## 4. Task 4: flank (a), the multi-digit regime $p \le \sqrt n$ ($n \ge i^2$)

Now $i \le \sqrt n$, $V^{\le}$ is nontrivial and uncontrolled by the
digit classification. $V^{>}$ is still squarefree on primes in
$(\sqrt n, j]$, so $V^{>} \le e^{\theta(j)} \le e^{c_B j}$.

### Claim G4.1 (PROVED: exactly what bound on $V^{\le}$ would extend the wedge)

Suppose, for some $\beta = \beta(n,i,j)$, that
$V^{\le} \le \binom{n}{i}^{\beta}$. Then $V_i(n)^2 \le
\binom{n}{i}^{2\beta} e^{2c_B j}$, and EEES78 gives a contradiction as
soon as $\binom{n}{i}^{2\beta} e^{2c_B j} \le \binom{n}{i}$, i.e.
exactly when
$$\boxed{\ \beta \;<\; \frac12 \;-\; \frac{c_B\, j}{\log \binom{n}{i}}\ }$$
(the subtracted term is the wedge's slack: the $V^{>}$ budget measured
against $\log\binom{n}{i}$). Using $\binom{n}{i} \ge (n/i)^i$ it
suffices that $\beta < \frac12 - \frac{c_B j}{i \log(n/i)}$; uniformly
for $n \ge i^2$ and $j < 2i$ it suffices that
$\beta \le \frac12 - \frac{2c_B}{\log i} - \delta$ for any fixed
$\delta > 0$ and $i$ large. Conversely any $\beta \ge 1/2$ is useless
for this route: $V^{\le}$ alone could then saturate EEES78. So the
required input is precisely: *the $\le\sqrt n$ part of $V_i(n)$ is at
most $\binom{n}{i}^{1/2 - c_B j/\log\binom{n}{i}}$* — an exponent
strictly below $1/2$ by an explicit, $j$-dependent margin.

### Claim G4.2 (PROVED: the simplest candidate bound is valid)

$V^{\le} \le n^{\pi(\sqrt n) - \pi(i-1)}$.
*Proof.* For each prime $p$, $p^{v_p\binom{n}{i}} \le n$ (S1, via
Legendre: $v_p\binom{n}{i}$ is a sum of $\lfloor \log_p n \rfloor$
summands each in $\{0,1\}$). $V^{\le}$ is the product of these factors
over the primes $p \in [i, \sqrt n]$, of which there are exactly
$\pi(\sqrt n) - \pi(i-1)$. $\blacksquare$
In the language of G4.1 the candidate gives
$\beta_{\mathrm{cand}} = \frac{(\pi(\sqrt n) - \pi(i-1))\log n}{\log\binom{n}{i}}$.

### Claim G4.3 (COMPUTED: the candidate closes a nonempty shell $i^2 \le n \le i^2 u_{\max}(i)^2$, and nothing beyond $u \approx \frac{\log i}{4}$)

Write $n = i^2 u^2$ ($u = \sqrt n / i \ge 1$), $j \le 2i$ (worst case).
Certification test (sufficient, using $\log\binom{n}{i} \ge i\log(n/i)$
and $V^{>} \le e^{c_B j}$): $2P\log n + 2c_B j < i\log(n/i)$ with
$P = \pi(\sqrt n) - \pi(i-1)$ computed **exactly** (sieve).
Impossibility test for this pair of bounds (using the exact upper
bound $\binom{n}{i} \le e^{n h(i/n)}$): if
$2P\log n + 2c_B j \ge n\,h(i/n)$, the candidate bound and the $V^{>}$
bound together cannot contradict EEES78. Computed:

| $i$ | candidate certifies up to $u$ | cannot certify from $u$ |
|---|---|---|
| $10^4$ | $2.70$ | $3.05$ |
| $10^5$ | $3.35$ | $3.70$ |
| $10^6$ | $4.00$ | $4.35$ |

So the region where EEES78 + candidate + $V^{>}$ analysis closes
counterexamples is **nonempty**: it contains the shell
$i^2 \le n \le u_{\max}(i)^2 i^2$ for the tabulated $i$, e.g. all
$i = 10^6$, $n \le 16\, i^2$ (with $3i/2 < j < 2i$). Sample values at
$i = 10^5$, $u = 2$: $P = 8392$, $2P\log n + 2c_B j = 8.097\times10^{5}
< i\log(n/i) = 1.290\times10^{6}$ ✓; at $u = 5$:
$2.077\times10^{6} > n h(i/n) = 1.573\times10^{6}$ ✗.
Asymptotics (from $P \approx \frac{\sqrt n}{\log\sqrt n} - \frac{i}{\log i}
\approx \frac{i(u-1)}{\log i}$): the sufficient condition becomes
$4(u - 1) + 4c_B \lesssim \log i + 2\log u$, i.e.
$u_{\max}(i) = \frac{\log i}{4} + O(1)$ — the shell is thin and grows
only logarithmically. In G4.1 terms,
$\beta_{\mathrm{cand}} \approx \frac{2(u-1)}{\log i}$, which crosses
the required $\frac12 - \frac{2c_B}{\log i}$ exactly at
$u \approx \frac{\log i}{4} + 1$.

### Claim G4.4 (barrier, stated precisely)

For $u$ above the "cannot certify" column of G4.3, the failure is a
failure of the **candidate bound**, not of the conjecture:
$n^{\pi(\sqrt n) - \pi(i-1)}$ is simply a weak estimate of $V^{\le}$
(it charges a full factor $n$ for every prime in $[i, \sqrt n]$,
although typically $p^{v_p\binom{n}{i}}$ is far smaller). Closing
$n \ge i^2 u^2$ with $u \gg \frac{\log i}{4}$ by this route requires a
bound $V^{\le} \le \binom{n}{i}^{\beta}$ with $\beta$ as in G4.1 proved
by other means — e.g. a per-prime bound $p^{v_p\binom{n}{i}} \le n^{\rho_p}$
with $\sum_{p \in [i,\sqrt n]} \rho_p \log n < (\frac12 - \text{slack})
\log\binom{n}{i}$, or an exponent bound on $V^{\le}$ of S7 type. No
such bound is proved here: **flank (a) beyond the G4.3 shell is OPEN.**

---

## 5. Status summary

| Claim | Content | Label |
|---|---|---|
| G1.1 | $\theta(x) \le (1 + 1.93378\cdot10^{-8})x$, all $x \ge 0$ — Broadbent et al., arXiv:2002.11068v2, Cor. 2.1, fetched & read | PROVED (primary-verified citation; rests on cited RH-verification computations) |
| G1.2 | $\theta(x) < (1 + 1/36260)x$, all $x > 0$ — Dusart, arXiv:1002.0442, Prop. 5.1, fetched & read; Thm 5.2 & $\pi$ bounds also read | PROVED (primary-verified citation) |
| G1.3 | Rosser–Schoenfeld 1975 $\theta < 1.1x$ attribution | NOT primary-verified; not used |
| G1.4 | Wedge S4-C with $K = 55$: no counterexample, $i > 55$, $55i < n < i^2$, $3i/2 < j < 2i$; no validity-range adjustment needed | PROVED |
| G2.1 | $(\ast)$ $\binom{2j}{i} \ge \binom{j}{d}^2$ region: exactly $\gamma \le 3/2 + 2/i$ ($i \le 2000$ classified; asymptotically empty in open strip, $F(3/2)=0$, $F'(3/2) = -2\log 2$); threshold curve $\alpha_c(\gamma)$ tabulated | COMPUTED |
| G2.2 | Two-sided $\theta$ support bound closes flank (c) for $i \ge 379$, all $\alpha$ | PROVED |
| G2.3 | Simultaneous badness barrier: 2,493 triples, $40 \le i \le 160$, max 16 bad primes at $(482, 157, 241)$, $n = 2j$, inside square-reduction interval | COMPUTED (barrier) |
| G2.4 | Flank (c), $257 \le i \le 378$ | GAP (finite, not checked here) |
| G3.1 | Flank (b): $2i \le j \le \Gamma i$, $n > K_\Gamma i$ closed, $K_2 = 55$, $K_3 = 404$, $K_4 = 2981$ | PROVED |
| G3.2 | Flank (b): $2i \le j \le \gamma^*(i) i$, $i \ge 379$, all $n < i^2$ closed; $\gamma^*_\infty = 2.17178$ | PROVED |
| G3.3 | Barriers: key lemma alone fails at $\gamma = 2$, $n = 2j$ by $e^{259.7}$ ($i=1000$); support+autogood fails at $\gamma = 3$ by $148.9$ nats | PROVED (barrier for size/support methods) |
| G3.4 | Support+autogood borderline $\gamma^{**} \approx 2.504$; closes $(1000, 2500)$ at $n=2j$ by $24.7$ nats | COMPUTED |
| G4.1 | Wedge extension to $n \ge i^2$ needs exactly $V^{\le} \le \binom{n}{i}^{\beta}$, $\beta < \frac12 - c_B j/\log\binom{n}{i}$ | PROVED (specification) |
| G4.2 | Candidate $V^{\le} \le n^{\pi(\sqrt n) - \pi(i-1)}$ valid | PROVED |
| G4.3 | Candidate closes shell $i^2 \le n \le i^2 u_{\max}^2$, $u_{\max} = 2.70, 3.35, 4.00$ at $i = 10^4, 10^5, 10^6$; region nonempty | COMPUTED |
| G4.4 | Flank (a) beyond the shell | OPEN |

Nothing here proves Erdős #699 in general. The net gains over Cycle 1:
wedge constant $256 \to 55$ on a primary-verified $\theta$ bound;
flank (c) closed for $i \ge 379$ (was: open for all $i$); flank (b)
closed for $\gamma \le \gamma^*(i) \to 2.17178$ ($i \ge 379$, all $n$)
and for any fixed $\gamma$ at large $n$; flank (a) reduced to an exact
$\beta$-specification with a proved nonempty shell.

---

## Appendix A: exact certification of $e^{4c} < 55$ and $K_\Gamma$ (Python stdlib)

```python
from fractions import Fraction
from math import factorial
e_ub = sum(Fraction(1, factorial(k)) for k in range(13)) + Fraction(1, factorial(12)*12)
# e < e_ub = 2.7182818284601415..., e_ub^4 = 54.5981500332... < 54.61
assert e_ub**4 < Fraction(5461, 100)
def e_pow(y):  # e^y <= 1/(1-y) for 0 <= y < 1, Fraction y
    return Fraction(1, 1) / (1 - y)
cB = Fraction(193378, 10**13)          # 1.93378e-8
print(float(e_ub**4 * e_pow(4*cB)))    # 54.5981542565  -> e^{4 c_B} < 55
print(float(e_ub**4 * e_pow(Fraction(4, 36260))))  # 54.6041736597 -> e^{4 c_D} < 55
for G in (2, 3, 4):
    print(G, float(e_ub**(2*G) * e_pow(2*G*cB)))   # 54.5982, 403.4288, 2980.9584
```

## Appendix B: $\Psi$ threshold and $\gamma^*$ (Python stdlib)

```python
from math import log
def h(p): return -p*log(p) - (1-p)*log(1-p)
cB = 1 + 1.93378e-8
def eps(i): return 3.965 / log(i-1)**2          # Dusart Thm 5.2, k=2, eta=3.965
def Psi(g, i):
    return 2*g*h(1/(2*g)) - 2*cB*g + 2*(1-eps(i))*(1 - 1/i) - log(2*g*i + 1)/i
print(Psi(2.0, 378), Psi(2.0, 379))   # -6.2638e-05, +1.9447e-04  -> threshold i0 = 379
def gamma_star(i):
    a, b = 2.0, 3.0
    for _ in range(60):
        m = (a+b)/2
        if Psi(m, i) > 0: a = m
        else: b = m
    return (a+b)/2
print([gamma_star(i) for i in (1000, 10**4, 10**5, 10**7)])
# [2.0509..., 2.1072..., 2.1310..., 2.1511...]; limit 2.17178 (eps -> 0)
```

## Appendix C: barrier search of G2.3 (Python stdlib, ~8 s)

```python
from math import comb
def primes_upto(N):
    s = bytearray(b'\x01') * (N + 1); s[0:2] = b'\x00\x00'
    for k in range(2, int(N**0.5) + 1):
        if s[k]: s[k*k:N+1:k] = bytearray(len(s[k*k:N+1:k]))
    return [k for k in range(N + 1) if s[k]]
PR = primes_upto(300)
total = 0; maxbad = 0; maxex = None
for i in range(40, 161):
    for j in range(i + 1, 2 * i):
        if 2 * j <= 3 * i: continue
        target = comb(j, j - i) ** 2
        n = 2 * j; c = comb(2 * j, i)
        if c >= target: continue
        while True:                       # largest n with C(n,i) < target
            c2 = c * (n + 1) // (n + 1 - i)
            if c2 >= target: break
            c = c2; n += 1
        nhi = min(n, 256 * i, i * i - 1)
        band = [p for p in PR if i <= p <= j]
        for nn in range(2 * j, nhi + 1):
            cnt = 0; ok = True
            for p in band:                # p >= i, nn < i^2: single-term Legendre
                if nn//p - i//p - (nn - i)//p >= 1:
                    cnt += 1
                    if (nn - i)//p - (nn - j)//p >= 1: ok = False; break
            if ok and cnt >= 1:
                total += 1
                if cnt > maxbad: maxbad = cnt; maxex = (nn, i, j, cnt)
print(total, maxbad, maxex)   # 2493 16 (482, 157, 241, 16)
```

## Appendix D: shell computation of G4.3 (Python stdlib)

```python
import bisect
from math import log, sqrt
def primes_upto(N):
    s = bytearray(b'\x01') * (N + 1); s[0:2] = b'\x00\x00'
    for k in range(2, int(N**0.5) + 1):
        if s[k]: s[k*k:N+1:k] = bytearray(len(s[k*k:N+1:k]))
    return [k for k in range(N + 1) if s[k]]
PR = primes_upto(30_000_000)
def pi(x): return bisect.bisect_right(PR, int(x))
def h(p): return -p*log(p) - (1-p)*log(1-p)
cB = 1 + 1.93378e-8
for i in (10**4, 10**5, 10**6):
    j = 2 * i; umax = None; uimp = None
    for k in range(0, 400):
        u = 1 + 0.05 * k; n = i * i * u * u
        P = pi(sqrt(n)) - pi(i - 1); lhs = 2 * P * log(n) + 2 * cB * j
        if lhs < i * log(n / i): umax = u
        if uimp is None and lhs >= n * h(i / n): uimp = u
    print(i, umax, uimp)   # (10000, 2.70, 3.05) (100000, 3.35, 3.70) (1000000, 4.00, 4.35)
```

*End of P-G2.*
