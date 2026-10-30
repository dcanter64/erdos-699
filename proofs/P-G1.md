# Prover G1 (independent) — Cycle 2: the θ input, and S4's open flanks (a), (b), (c)

**Problem (Erdős #699).** For $1 \le i < j \le n/2$, show
$\gcd(V_i(n), \binom{n}{j}) > 1$, where $V_i(n)$ is the part of
$\binom{n}{i}$ supported on primes $\ge i$. A **counterexample** is a
triple with $\gcd(V_i(n), \binom{n}{j}) = 1$.

**Inputs taken as given (not reproved here).** EEES78
($V_i(n) > \binom{n}{i}^{1/2}$ outside the 12 exception pairs, all with
$n \le 56$); the key lemma (in a counterexample,
$V_i(n) \mid \binom{j}{j-i} = \binom{j}{i}$); the S4 classification
(every prime factor $p \ge i$ of $\binom{n}{i}$ in a counterexample lies
in $[i,j]$; those with $p > \sqrt n$ have exponent exactly $1$ and lie in
a Lemma-5 bad configuration); S10 §4–§5 (bad $p \in [i, j/2]$ requires
$e_p \le \lfloor \log_p j \rfloor$ and the multi-scale condition (†);
primes in $(j/2, j-i]$ lying in $S(n,i)$ are automatically good when
$j > 2i$); the closures of $j \le 3i/2$, $n = 2j$, $i \in \{1,2\}$; the
sweep to $n \le 20{,}000$. Wedge Theorem S4-C as proved in P-D1
(constant $256$, elementary primorial bound $4^j$).

**Notation.** $\theta(x) = \sum_{p \le x} \log p$, so
$\prod_{p \le x} p = e^{\theta(x)}$. $H(p) = -p\log p - (1-p)\log(1-p)$
(natural-log entropy). In §3, $\gamma = j/i$ and $\alpha = n/i$ (the
letter $c$ is reserved for the $\theta$ constant of §1; where the task
brief used $c$ for $j/i$, that ratio is $\gamma$ here).

---

## 0. Auxiliary entropy bounds

**Claim 0 (elementary binomial entropy bounds). PROVED.**
For $1 \le K \le N-1$,
$$\frac{e^{N H(K/N)}}{N+1} \;\le\; \binom{N}{K} \;\le\; e^{N H(K/N)}.$$

*Proof.* Put $p = K/N$ and $T_k = \binom{N}{k} p^k (1-p)^{N-k}$, so
$\sum_{k=0}^{N} T_k = (p + (1-p))^N = 1$. The upper bound is
$T_K \le 1$ rearranged. For the lower bound, $T_{k+1}/T_k =
\frac{N-k}{k+1}\cdot\frac{K}{N-K}$, which is $> 1$ for $k < K$ and
$< 1$ for $k \ge K$; hence $T_K$ is the largest of the $N+1$ terms,
so $T_K \ge 1/(N+1)$, and rearranging gives the lower bound. ∎

---

## 1. Task 1: the θ input, primary-verified, and the improved wedge constant

**Claim 1 (primary-source θ bound). PROVED (as a citation: the source
below was fetched and read in full text during this session).**

> S. Broadbent, H. Kadiri, A. Lumley, N. Ng, K. Wilk, *Sharper bounds
> for the Chebyshev function $\theta(x)$*, arXiv:2002.11068v2
> [math.NT], 27 Jan 2021, **Corollary 2.1**:
> $$\theta(x) \;\le\; \big(1 + 1.93378\cdot 10^{-8}\big)\, x
> \qquad\text{for all } x \ge 0.$$

The corollary is stated and proved in the paper itself (its proof
combines Büthe's $\theta(x) < x$ for $0 < x \le 10^{19}$ with the
paper's Table 8 value $M_0 = \varepsilon(19\log 10) = 1.93378\cdot
10^{-8}$). The same paper's **Table 14** (also fetched and read)
states the two-sided bound used in §3 below (Claim 8): for $x > e^{20}$,
$(1 - m_0)x < \theta(x) < (1 + M_0)x$ with
$M_0 = 4.2676\cdot 10^{-5}$, $m_0 = 9.1639\cdot 10^{-5}$ (the row
$\log X_0 = \log X_1 = 20$).

Hence the best primary-verified constant obtained in this session is
$$c \;=\; 1.0000000193378, \qquad \theta(x) \le c\,x \ \text{for all } x \ge 0.$$

**Citation status of Rosser–Schoenfeld 1975.** The 1975 paper itself
was **not** read: no readable primary copy was obtained, so no bound
is quoted from it directly. (Broadbent et al., Table 1, tabulate
Rosser–Schoenfeld (1975) as giving $M_0 = 0.001102$ at $X_1 = 1$;
that is a secondary tabulation and is **not used** anywhere below.
The $c = 1.1$ figure in S4's remark is likewise not used: Claim 1's
$c$ is far stronger and, critically, its range is **all** $x \ge 0$,
so no validity threshold $x_0$ enters the wedge at all.)

**Claim 2 (Wedge S4-C with improved constant $K = 55$). PROVED**
(using Claim 1 as the sole external analytic input, plus EEES78 and
the S4 anatomy as given).

*There is no counterexample with*
$$55\,i < n < i^2, \qquad 3i/2 < j < 2i$$
*(the region forces $i > 55$, since $55i < i^2$).*

*Proof.* Suppose $(n,i,j)$ in this region were a counterexample.
Since $n > 55i \ge 55\cdot 56 = 3080 > 56$ (as $i \ge 56$), $(n,i)$ is
not an EEES78 exception pair, so $V_i(n)^2 > \binom{n}{i}$. Since
$n < i^2$, every prime divisor $p \ge i$ of $\binom{n}{i}$ has
$p > \sqrt n$, so by the S4 anatomy $V_i(n)$ is a product of
**distinct** primes in $[i,j]$, each to the first power. Hence, by
Claim 1 applied at $x = j$ (valid for every $j \ge 0$ — no range
adjustment is needed),
$$V_i(n) \;\le\; \prod_{i \le p \le j} p \;\le\; e^{\theta(j)}
\;\le\; e^{c j}, \qquad V_i(n)^2 \le e^{2cj} < e^{4ci},$$
using $j < 2i$. Also $\binom{n}{i} \ge (n/i)^i > 55^i$ (P-D1, Step 4).
Now $e^{4c} = e^{4.0000000773512} = 54.598154256\ldots < 55$
(exactly: $K = \lceil e^{4c} \rceil = 55$), so $55^i > e^{4ci}$, and
$$\binom{n}{i} \;\ge\; (n/i)^i \;>\; 55^i \;>\; e^{4ci}
\;>\; e^{2cj} \;\ge\; V_i(n)^2 \;>\; \binom{n}{i},$$
a contradiction. ∎

*Remarks.* (i) The constant $256$ of P-D1 is superseded: the wedge
now starts at $n > 55i$. No $K \le 54$ is available from this
method with any bound $\theta(x) \le cx$ valid for all $x$: by the
prime number theorem $\theta(x)/x \to 1$, so such a bound forces
$c \ge 1$, hence $e^{4c} \ge e^4 = 54.598\ldots$ and the integer
constant is at least $55$. Claim 1's $c = 1 + 1.94\cdot10^{-8}$
attains that integer optimum, $K = 55$. (ii) $K = 55 < 82$: the $82$ of S4's remark came from
$c = 1.1$; Claim 1 improves it to $55$, with **no** adjusted
$i$-threshold, because Corollary 2.1 has no $x_0$.

---

## 2. Task 2: flank (c), $n \le 256i$ (with $i > 256$, so $n < i^2$ and $V^{\le} = 1$)

Setup for the whole section: $i > 256$, $3i/2 < j < 2i$,
$2j \le n \le 256i$ (so $\alpha = n/i \in [2\gamma, 256]$,
$\gamma = j/i \in (3/2, 2)$), and $(n,i,j)$ a counterexample. Then
$V := V_i(n)$ is squarefree on $[i,j]$ (as $n \le 256i < i^2$), every
prime factor lies in a Lemma-5 bad configuration, the key lemma gives
$V \mid \binom{j}{j-i} = \binom{j}{i}$, hence $V \le \binom{j}{i}$, and
EEES78 with $n \ge 2j$ gives
$$V \;>\; \binom{n}{i}^{1/2} \;\ge\; \binom{2j}{i}^{1/2}. \tag{$\ast$}$$

**Claim 3 (the exact plain-size sub-region). PROVED.**
The plain chain $(\ast)$ already gives a contradiction whenever
$$\binom{2j}{i} \;\ge\; \binom{j}{i}^{2},
\qquad\text{i.e.}\qquad R(i,j) := \frac{\binom{2j}{i}}{\binom{j}{i}^2} \ge 1.$$
This condition **does not involve $\alpha$ at all**: it uses only the
worst case $n = 2j$. Hence the sub-region of
$(\alpha, \gamma) \in [2\gamma, 256] \times (3/2, 2)$ closed by this
argument is exactly
$$\{\, 2\gamma \le \alpha \le 256,\quad 3/2 < \gamma \le j^{*}(i)/i \,\},$$
where $j^{*}(i) := \max\{\, j : 3i/2 < j < 2i,\ R(i,j) \ge 1 \,\}$
(with the set possibly empty a priori for a given $i$; Claim 5 shows
it is nonempty and tiny for the computed range). Every pair
$(i,j)$ with $j \le j^{*}(i)$ is thereby closed for **all**
$n \in [2j, 256i]$ in flank (c) — indeed for all $n \ge 2j$ with
$n < i^2$.

**Claim 4 ($R(i,\cdot)$ is strictly decreasing in the region).
PROVED.** For fixed $i$ and $3i/2 < j < 2i$,
$$\frac{R(i,j+1)}{R(i,j)}
= \frac{2\,(2j+1)\,(d+1)^2}{(j+d+2)(j+d+1)(j+1)} \;<\; \frac34,
\qquad d := j - i.$$

*Proof.* The identity is direct: $\binom{2j+2}{i}/\binom{2j}{i} =
\frac{(2j+2)(2j+1)}{(2j+2-i)(2j+1-i)}$ and
$\binom{j+1}{i}/\binom{j}{i} = \frac{j+1}{j+1-i}$, with
$2j+2-i = j+d+2$, $2j+1-i = j+d+1$, $j+1-i = d+1$, and
$(2j+2)/(j+1) = 2$. Regroup the ratio as
$2 \cdot \frac{2j+1}{j+d+1} \cdot \frac{d+1}{j+1} \cdot
\frac{d+1}{j+d+2}$. In the region: $j < 2i$ gives $d < j/2$, hence
$d + 1 \le (j+1)/2$ (since $d < j/2$ and $d$ integral), so
$\frac{d+1}{j+1} \le \frac12$ and
$\frac{d+1}{j+d+2} < \frac{d+1}{j+1} \le \frac12$; and $j > 3i/2$
gives $d > j/3$, so $j + d + 1 > 4j/3 + 1$ and
$\frac{2j+1}{j+d+1} < \frac{2j+1}{4j/3+1} = \frac{6j+3}{4j+3} < \frac32$.
The product is $< 2 \cdot \frac32 \cdot \frac12 \cdot \frac12 =
\frac34$. ∎ (Numerical sanity check: the maximum of the step ratio
over all $i \le 300$ in the region is $0.45833\ldots$, attained at
$(i,j) = (3,5)$, consistent with the bound $3/4$.)

Consequently, by Claim 4, for each $i$ the admissible $j$ in Claim 3
form an **initial segment** $(3i/2,\ j^{*}(i)]$ of the region: the
boundary is exactly the single integer $j^{*}(i)$.

**Claim 5 (the boundary is a sliver at $\gamma = 3/2$; computed
exactly, and asymptotically sharp). PROVED (monotonicity and
asymptotics) + COMPUTED (table, exact integer arithmetic).**

(a) *Exact values.* Comparing the exact integers $\binom{2j}{i}$ and
$\binom{j}{i}^2$ (Python `math.comb`, no floating point), and using
Claim 4 to certify maximality from the two boundary values:

| $i$ | $j^{*}(i)$ | $j^{*}(i) - 3i/2$ |
|---|---|---|
| 256 | 386 | 2 |
| 257 | 387 | 1.5 |
| 300 | 452 | 2 |
| 500 | 752 | 2 |
| 1000 | 1502 | 2 |
| 2000 | 3002 | 2 |

For every $i$ with $257 \le i \le 600$,
$R(i, \lfloor 3i/2\rfloor + 1) \ge 1$ (verified exactly; in the
full range $3 \le i \le 600$ the only failures of $R \ge 1$ at
$j = \lfloor 3i/2 \rfloor + 1$ are $i \in \{4, 6, 8\}$, outside
flank (c)). Log-domain evaluation gives
$j^{*}(10000) = 15003$ (excess $3$); only the $i \le 2000$ rows are
claimed as exact-integer verified.

(b) *No fixed $\gamma_0 > 3/2$ works for large $i$.* For
$\gamma \in (3/2, 2)$ fixed, Claim 0 gives
$\log R(i,j) \le 2\gamma i\,[H(1/(2\gamma)) - H(1/\gamma)] +
2\log(j+1)$. The bracket is $< 0$: with $H(p) = H(1-p)$,
$H(1/\gamma) = H(1 - 1/\gamma)$, both $1/(2\gamma) \in (1/4, 1/3)$
and $1 - 1/\gamma \in (1/3, 1/2)$ lie in $(0, 1/2)$ where $H$ is
strictly increasing, and $1 - 1/\gamma > 1/(2\gamma) \iff \gamma >
3/2$. Hence $\log R(i,j) \to -\infty$ as $i \to \infty$ at fixed
$\gamma > 3/2$: for all sufficiently large $i$, $R(i,j) < 1$ for
every $j \ge \gamma_0 i$. Combined with (a), $j^{*}(i)/i \to 3/2$
along any sequence on which $j^{*}(i)$ exists: **the plain-size
sub-region of Claim 3 is, asymptotically, only the boundary sliver
$\gamma \downarrow 3/2$, of width $j^{*}(i) - 3i/2 \in \{1.5, 2, 3\}$
in the computed range.** This is the exact sense in which flank (c)
is *not* closed by size: for every $\gamma \in (3/2, 2)$ bounded
away from $3/2$, and all large $i$, $\binom{2j}{i}^{1/2} <
\binom{j}{i}$, so $(\ast)$ and $V \mid \binom{j}{i}$ are fully
compatible.

**Claim 6 (barrier for the remaining sub-region: simultaneous
badness occurs in bulk at moderate $i$). COMPUTED.**
Search method: for $p \in [i,j]$ with $n < i^2$ one has
$p \ge i > \sqrt n$, so the two-digit criterion applies and
$p \in S(n,i)$ iff $(i \bmod p) > (n \bmod p)$, while $p$ is bad iff
additionally $\lfloor i/p \rfloor < \lfloor j/p \rfloor$ and
$(j \bmod p) \le (n \bmod p)$ (Lemma 5). The search enumerated, for
every $40 \le i \le 170$ and every $3i/2 < j < 2i$, all
$n \in [2j, \min(256i, i^2 - 1)]$, and recorded the triples in
which **every** $p \in S(n,i) \cap [i,j]$ is bad, with at least
three such primes. Result: **666,006 such triples** (64,475 with
$40 \le i \le 60$; 601,531 with $61 \le i \le 170$; total wall time
$\approx 2$ minutes, Python stdlib). Showcase instances, each
re-verified independently with exact Legendre valuations:

| triple $(n,i,j)$ | $\gamma$ | bad primes in $[i,j]$ | $N(i,j)$ | primes of $S(n,i)$ above $j$ |
|---|---|---|---|---|
| $(512, 170, 256)$ | $1.506$ | 15: $173,179,181,191,193,197,199,211,223,227,229,233,239,241,251$ — all of $S \cap [i,j]$ | $515 \ge n$: **inside** the reduction interval | 29 |
| $(5958, 100, 180)$ | $1.8$ | 10: $103,107,109,113,131,137,151,163,173,179$ — all of $S \cap [i,j]$; the **unique** such $n$ for this $(i,j)$ in range | $486 < n$ | 60 |
| $(20350, 149, 251)$ | $1.685$ | 18 (maximum count found): $151,157,163,167,173,179,181,191,193,197,199,211,223,227,233,239,241,251$ | $609 < n$ | 92 |

(The search also reproduced S10's $(2186, 59, 109)$ with its 10 bad
primes, cross-validating the method against Cycle 1.)

**Barrier statement.** In every one of these triples the *only*
thing preventing a counterexample is the presence of prime factors
of $\binom{n}{i}$ above $j$ (automatically good by Lemma 1 / S10
Lemma 2). The in-range conditions — squarefreeness, support in
$[i,j]$, and a Lemma-5 bad configuration at *every* prime of
$S(n,i) \cap [i,j]$ simultaneously — are therefore satisfiable in
bulk throughout flank (c)'s parameter range at moderate $i$,
including inside the reduction interval and at $\gamma = 1.8$
bounded away from the Claim-3 sliver. Hence **no argument that uses
only the in-range bad-configuration anatomy can close flank (c)
beyond Claim 3's sliver**: a completion must add a global input
that forces a prime factor $> j$ of $\binom{n}{i}$ (or controls
$V$ as a whole), exactly as in S10 §6's conclusion for R1. The
search covers $i \le 170$; for the flank's stated range $i > 256$
the barrier is COMPUTED evidence at moderate $i$, not a proof that
such triples exist for every large $i$ — but the burden is now on
any proposed in-range argument to explain why it would not also
"close" the 666,006 triples above.

---

## 3. Task 3: flank (b), $j \ge 2i$

Setup: $j > 2i$ (the case $j = 2i$ is not treated here), $2j \le n <
i^2$, so again $i > \sqrt n$ and $V$ is squarefree on $[i,j]$. Write
$d = j - i > i$ and $\gamma = j/i > 2$. By S10 §5, item 3, every
$p \in S(n,i) \cap (j/2, d]$ is automatically good (a window of
length $d \ge p$ meets a multiple of $p$, so $A_p \ge 1$ while
$B_p \le 1$); hence in a counterexample
$$\operatorname{supp} V \;\subseteq\; [i,\, j/2] \;\cup\; (d,\, j],
\tag{$\dagger$}$$
the interval $(j/2, d]$ being excluded. By S10 §4, bad
$p \in [i, j/2]$ requires $e_p \le \lfloor \log_p j \rfloor$ and the
multi-scale condition (†) of S10; in the present regime
$i > \sqrt n$ the exponent condition is automatic ($e_p = 1$ by S4),
so the real content imported from S10 is the exclusion $(\dagger)$.

**Claim 7 (the plain key-lemma size test fails, quantitatively:
proved for $2 \le \gamma \le 12/5$, computed at $\gamma = 3, 4$).
PROVED + COMPUTED.**
For $2 \le \gamma \le 12/5$,
$$\log \frac{\binom{j}{i}}{\binom{2j}{i}^{1/2}}
\;\ge\; j\,\big[H(1/\gamma) - H(1/(2\gamma))\big] - \log(j+1)
\;\ge\; 0.130812\, j - \log(j+1) \;>\; 0
\quad (j \ge 25),$$
so the inequality $\binom{2j}{i}^{1/2} \ge \binom{j}{i}$ that a plain
$V \mid \binom{j}{i}$ size argument would need **fails, by a factor
$\ge e^{0.130812 j - \log(j+1)}$**.

*Proof.* Claim 0: $\log \binom{j}{i} \ge j H(1/\gamma) - \log(j+1)$
and $\log \binom{2j}{i} \le 2j H(1/(2\gamma))$; subtract half the
second from the first. For the bracket: put $a = 1/(2\gamma) \in
[5/24, 1/4]$ and $g(a) = H(2a) - H(a)$; then
$g'(a) = 2\log\frac{1-2a}{2a} - \log\frac{1-a}{a} < 0$ on this
interval, because $g'(a) < 0 \iff (1-a)/a > (1-2a)^2/(4a^2) \iff
8a^2 - 8a + 1 < 0 \iff a \in \big(\frac{2-\sqrt2}{4},
\frac{2+\sqrt2}{4}\big) = (0.1464\ldots, 0.8536\ldots)$, which
contains $[5/24, 1/4]$. So $g$ is decreasing in $a$, i.e. the
bracket is minimal at $\gamma = 2$: $H(1/2) - H(1/4) =
0.693147\ldots - 0.562335\ldots = 0.130812\ldots$. ∎

*Computed instance.* $(i, j, n) = (100, 300, 600)$:
$\binom{j}{i} / \binom{n}{i}^{1/2} = 10^{23.60}$ exactly computed
($\log_{10}$ of the ratio $= 23.60$ to two decimals): the plain test
fails there by $23.6$ orders of magnitude.

**Claim 8 (an explicit sub-region of flank (b) IS closed, via the
support exclusion $(\dagger)$ plus two-sided θ). PROVED** (using
EEES78, S10 item 3, Claim 0, and Broadbent et al. Table 14 as cited
in Claim 1).

*There is no counterexample with*
$$2i \;<\; j \;\le\; \tfrac{12}{5} i, \qquad
i \;>\; e^{20} + 1, \qquad 2j \;\le\; n \;<\; i^2.$$

*Proof.* Suppose such a counterexample existed. By $(\dagger)$ and
squarefreeness,
$\log V \le [\theta(j/2) - \theta(i-1)] + [\theta(j) - \theta(d)]$.
All four arguments $j/2, i-1, j, d$ exceed $e^{20}$ (as
$i > e^{20} + 1$ and $d \ge i$, $j/2 > i$), so Table 14's row
$\log X_0 = 20$ applies with $M_0 = 4.2676\cdot10^{-5}$,
$m_0 = 9.1639\cdot10^{-5}$:
\begin{align*}
\log V &\le (1+M_0)\tfrac{j}{2} - (1-m_0)(i-1)
+ (1+M_0) j - (1-m_0) d \\
&= \tfrac32 (1+M_0)\, j - (1-m_0)(j-1)
= \big(\tfrac12 + \tfrac32 M_0 + m_0\big) j + (1 - m_0) \\
&= 0.500155653\, j + 0.999908361,
\end{align*}
using $i - 1 + d = j - 1$. On the other hand EEES78 and Claim 0 give
$$\tfrac12 \log \binom{n}{i} \;\ge\; \tfrac12 \log \binom{2j}{i}
\;\ge\; j\, H\big(\tfrac{1}{2\gamma}\big) - \tfrac12 \log(2j+1).$$
For $\gamma \le 12/5$, $1/(2\gamma) \ge 5/24$ and $H$ is increasing
on $(0, 1/2]$, so $H(1/(2\gamma)) \ge H(5/24) = 0.5117400734\ldots$,
exceeding the coefficient $0.500155653$ by $0.0115844\ldots$. Since
$j > 2i > 2e^{20} > 10^9$ and
$j \mapsto \big(1 + \frac12\log(2j+1)\big)/j$ is decreasing with
value $< 1.2\cdot 10^{-8}$ at $j = 10^9$, we get
$\frac12 \log \binom{n}{i} > 0.500155653\, j + 0.999908361 \ge
\log V$, i.e. $\binom{n}{i}^{1/2} > V$, contradicting EEES78
($\binom{n}{i}$ is not an exception: $n > 4e^{20} > 56$). ∎

*Remark.* The mechanism is exactly the S10 exclusion: the support
of $V$ is confined to two intervals, $[i, j/2]$ and $(d, j]$, of
total length $(j/2 - i) + (j - d) = j/2$, so $\log V$ is (up to the
$\theta$ error terms) at most $j/2$ rather than the trivial
$\theta(j) \approx j$; this beats the entropy term
$j H(1/(2\gamma))$ precisely while $H(1/(2\gamma)) > 1/2$, i.e.
$\gamma \lesssim 2.504$ (the root of $H(p) = 1/2$ is
$p = 0.1997\ldots$; $12/5 = 2.4$ is the clean value used, with
margin $0.0116$). The threshold $i > e^{20}$ is an
artifact of the Table 14 row used; sharper rows lower it at the
cost of larger $x_0$ bookkeeping, and no attempt was made to
optimise it.

**Claim 9 (the $W$-refinement also fails in general: computed
barrier). COMPUTED / the inequality is FALSE at the stated
instances.** A natural refinement of Claim 7's plain test is to
bound $V$ not by $\binom{j}{i}$ but by $W(i,j) :=$ the part of
$\binom{j}{i}$ supported on primes in $[i,j]$ (legitimate, since
$V \mid \binom{j}{i}$ and $\operatorname{supp} V \subseteq [i,j]$,
with exponents $1$). The refinement closes a pair only if
$W(i,j) \le \binom{2j}{i}^{1/2}$. Exact computation (Legendre
valuations, exact integers) gives:

| $(i, j, n{=}2j)$ | $\log_{10} \binom{j}{i} - \frac12 \log_{10}\binom{n}{i}$ | $\log_{10} W(i,j) - \frac12 \log_{10}\binom{n}{i}$ |
|---|---|---|
| $(100, 300, 600)$ | $+23.60$ | $+1.21$ |
| $(100, 400, 800)$ | $+31.58$ | $+15.01$ |
| $(200, 600, 1200)$ | $+47.75$ | $+5.26$ |

So at $(100,300,600)$ even the refined bound fails: $W$ exceeds
$\binom{n}{i}^{1/2}$ by a factor $10^{1.21} \approx 16$, and at
$\gamma = 4$ by $10^{15.01}$. (For contrast, at the smaller
instances $(40,100,200)$ and $(60,132,264)$ the $W$ test does hold,
with margins $-1.16$ and $-4.35$ in $\log_{10}$; those pairs are
closed by it for all $n \in [2j, i^2)$. The $W$ test is therefore a
per-pair criterion, not a $\gamma$-sub-region argument: Claim 8's
closure of $2 < \gamma \le 12/5$ for huge $i$ comes from the
support exclusion, not from $W$.) For $\gamma \ge 12/5$ in general,
and for all $\gamma \ge 2$ at moderate $i$, flank (b) with
$i > \sqrt n$ remains **OPEN** by these methods: the failing
inequality is $W(i,j) \le \binom{2j}{i}^{1/2}$, and Claim 7 + the
table quantify its failure.

---

## 4. Task 4: flank (a), the multi-digit regime $p \le \sqrt n$ ($n \ge i^2$)

Write $V_i(n) = V^{\le} \cdot V^{>}$, the parts on primes in
$[i, \sqrt n]$ and $(\sqrt n, j]$. The $V^{>}$ analysis is unchanged
from the wedge: $V^{>}$ is squarefree on $[i,j]$ (S4), so by Claim 1
$V^{>} \le e^{\theta(j)} \le e^{cj}$ with $c = 1.0000000193378$.
Throughout this section $3i/2 < j < 2i$ and $n \ge i^2$ (so
$V^{\le}$ may be nontrivial), and $(n,i)$ is not an EEES78
exception.

**Claim 10 (exactly what bound on $V^{\le}$ the wedge needs).
PROVED.** Suppose $V^{\le} \le \binom{n}{i}^{\beta}$ for some $\beta$
(possibly depending on $n, i$). Then the wedge chain closes the
triple whenever
$$\boxed{\ \beta \;\le\; \frac12 \;-\; \frac{c\,j}{\log \binom{n}{i}}\ }$$
and this is sharp for the method: if $\beta$ exceeds the right side,
the chain $V^2 \le \binom{n}{i}^{2\beta} e^{2cj}$ versus EEES78's
$V^2 > \binom{n}{i}$ yields no contradiction. Using
$\log \binom{n}{i} \ge i \log(n/i)$ and $j < 2i$, a clean sufficient
form is
$$\beta \;\le\; \frac12 - \frac{2c}{\log(n/i)},
\qquad\text{in particular for } n \ge i^2:\quad
\beta \;\le\; \frac12 - \frac{2c}{\log i}.$$
Consequently **any fixed $\beta < 1/2$ extends the wedge to all
$n \ge i^2$ once $i > \exp\big(2c/(\frac12 - \beta)\big)$**; e.g.
$\beta = 0.36$ works for $i > e^{2c/0.14} = 1{,}600{,}320.63\ldots$,
i.e. $i \ge 1{,}600{,}321$. As $i \to \infty$ the admissible $\beta$
tends to $1/2$ from below: $1/2$ itself is never admissible, since
the $V^{>}$ factor $e^{cj}$ must be paid for out of the slack.

*Proof.* $V^2 = (V^{\le})^2 (V^{>})^2 \le
\binom{n}{i}^{2\beta} e^{2cj}$. If $2\beta \log\binom{n}{i} + 2cj
\le \log \binom{n}{i}$, then $V^2 \le \binom{n}{i}$, contradicting
EEES78. That inequality rearranges to the boxed condition. The
sufficient form substitutes the lower bound for
$\log \binom{n}{i}$ in the subtracted term (making the right side
smaller, hence the condition stronger) — precisely:
$\frac{cj}{\log\binom{n}{i}} \le \frac{cj}{i\log(n/i)} <
\frac{2c}{\log(n/i)}$. ∎

**Claim 11 (the candidate bound is true). PROVED.**
For every prime $p$ and $1 \le i \le n$,
$p^{v_p\binom{n}{i}} \le n$. Hence, with
$M(n,i) := \pi(\sqrt n) - \pi(i-1) \ge 0$ the number of primes in
$[i, \sqrt n]$,
$$V^{\le} \;\le\; n^{M(n,i)}.$$

*Proof.* By Legendre, $v_p\binom{n}{i} = \sum_{e \ge 1}
\big(\lfloor n/p^e\rfloor - \lfloor i/p^e\rfloor -
\lfloor (n-i)/p^e\rfloor\big)$; each summand lies in $\{0,1\}$ (it
is $\lfloor x+y\rfloor - \lfloor x\rfloor - \lfloor y\rfloor$), and
summands with $p^e > n$ vanish. So $v_p \le \#\{e : p^e \le n\} =
\lfloor \log_p n \rfloor$ and $p^{v_p} \le p^{\lfloor \log_p n
\rfloor} \le n$. Multiply over the $M(n,i)$ primes in
$[i, \sqrt n]$. ∎

**Claim 12 (the exact region the candidate closes, and it is
nonempty). PROVED.** Combining Claims 1, 11 and EEES78 as in
Claim 3, the candidate bound closes every triple in the region
$$\mathcal R_a \;=\; \Big\{\, n \ge i^2,\ \ 3i/2 < j < 2i,\ \
2\,M(n,i)\,\log n \;+\; 2c\,j \;\le\; i\,\log(n/i) \,\Big\}$$
($c$ as in Claim 1; the inequality is the exact closing condition
of the chain $V^2 \le n^{2M} e^{2cj} \le (n/i)^i \le \binom{n}{i}$).
Moreover $\mathcal R_a$ has the explicit nonempty sub-band
$$i \ge 70, \qquad i^2 \;\le\; n \;<\; (i+1)^2, \qquad
3i/2 < j < 2i \quad\Longrightarrow\quad (n,i,j) \in \mathcal R_a,$$
so the wedge genuinely extends to a band **above** $n = i^2$.

*Proof.* For the sub-band: $\sqrt n \in [i, i+1)$, so a prime in
$[i, \sqrt n]$ is $< i+1$ and $\ge i$, i.e. $M(n,i) \le 1$ (it is $1$
iff $i$ is prime). With $j < 2i$ the closing condition of
$\mathcal R_a$ is implied by $2\log n + 4ci < i \log(n/i)$; using
$n < (i+1)^2$ (so $2\log n < 4\log(i+1)$) and $n \ge i^2$ (so
$i\log(n/i) \ge i\log i$), it suffices that
$4\log(i+1) + 4ci < i \log i$. Direct evaluation gives the first
$i$ with this property as $i = 70$ ($i = 69$: false; $i = 70$:
true), and it persists for all $i \ge 70$: the difference
$i(\log i - 4c) - 4\log(i+1)$ increases at each step by
$\log i + (i+1)\log(1 + 1/i) - 4c - 4\log\frac{i+2}{i+1} >
\log 70 - 4c - \frac{4}{71} = 0.192\ldots > 0$. Exceptions are
excluded since $n \ge i^2 \ge 4900 > 56$. ∎

**Claim 13 (the candidate region is thin: computed failure away
from the band). COMPUTED (barrier for the candidate bound, not for
the conjecture).** At $(i, n) = (100, 10^6)$ (so $n = i^3$,
$\sqrt n = 1000$): $M = \pi(1000) - \pi(99) = 168 - 25 = 143$, and
the closing condition of Claim 12 fails by a wide margin:
$$2M\log n = 3951.24\ldots \qquad\text{vs.}\qquad
i\log(n/i) = 921.03\ldots$$
i.e. the candidate permits $V^{\le}$ as large as $n^{143}$ while
Claim 10 requires $V^{\le} \le \binom{n}{i}^{\beta}$ with
$\beta \le 1/2 - cj/\log\binom{n}{i}$. In exponent terms: with
$\log \binom{10^6}{100} = 1017.81\ldots$ (via $\log\Gamma$), the
candidate's effective exponent is $\beta_{\mathrm{cand}} =
M\log n / \log\binom{n}{i} = 1.941\ldots$, whereas Claim 10 admits
only $\beta \le 0.304$–$0.353$ (for $150 < j < 200$): the candidate
overshoots the admissible exponent by a factor of about $5.5$–$6.4$
at this single point. The obstruction is structural: $M(n,i)$
grows like $\sqrt n / \log \sqrt n$ once $\sqrt n - i$ is large,
while the budget $i\log(n/i)$ grows only like $i\log n$; the
candidate closes only where the interval $[i, \sqrt n]$ contains
few primes (Claim 12's band being the extremal case $M \le 1$).
**Flank (a) in general — $n \ge i^2$ with $\sqrt n - i$ large —
remains OPEN**: by Claim 10, what is needed is any bound
$V^{\le} \le \binom{n}{i}^{\beta}$ with $\beta \le 1/2 -
cj/\log\binom{n}{i}$ (e.g. any fixed $\beta < 1/2$ for large $i$);
the simplest candidate $n^{M(n,i)}$ supplies this only in
$\mathcal R_a$.

---

## 5. Summary of labels

| Claim | Content | Label |
|---|---|---|
| 0 | Entropy bounds for $\binom{N}{K}$ | PROVED |
| 1 | $\theta(x) \le (1 + 1.93378\cdot10^{-8})x$ for all $x \ge 0$, Broadbent–Kadiri–Lumley–Ng–Wilk, arXiv:2002.11068v2, Cor. 2.1; Table 14 two-sided row at $e^{20}$ | PROVED as primary-source citation (fetched and read); Rosser–Schoenfeld 1975 itself NOT read, not used |
| 2 | Wedge S4-C with $K = \lceil e^{4c} \rceil = 55$: no counterexample with $55i < n < i^2$, $3i/2 < j < 2i$ | PROVED |
| 3 | Flank (c): plain $V \mid \binom{j}{i}$ size closes exactly $\gamma \le j^{*}(i)/i$, all $\alpha \in [2\gamma, 256]$ | PROVED |
| 4 | $R(i,j)$ strictly decreasing in $j$ in the region (step ratio $< 3/4$) | PROVED |
| 5 | Boundary values $j^{*}(i) - 3i/2 \in \{1.5, 2\}$ ($i \le 2000$, exact); $j^{*}(i)/i \to 3/2$; no fixed $\gamma > 3/2$ closed by plain size | PROVED + COMPUTED |
| 6 | Simultaneous badness in flank (c): 666,006 triples at $40 \le i \le 170$ with every $p \in S(n,i)\cap[i,j]$ bad ($\ge 3$ of them); showcases $(512,170,256)$ (15 bad, inside reduction interval), $(5958,100,180)$ ($\gamma = 1.8$, 10 bad), $(20350,149,251)$ (18 bad); in-range anatomy alone cannot close flank (c) beyond Claim 3 | COMPUTED (Legendre-verified showcases) |
| 7 | Plain size test for flank (b) fails by $\ge e^{0.130812 j - \log(j+1)}$ for $2 \le \gamma \le 12/5$; $10^{23.60}$ at $(100,300,600)$ | PROVED + COMPUTED |
| 8 | Flank (b) sub-region $2i < j \le \frac{12}{5}i$, $i > e^{20}+1$, $2j \le n < i^2$ closed via S10 support exclusion + two-sided θ | PROVED |
| 9 | $W$-refinement fails at $(100,300,600)$ by $10^{1.21}$ and at $(100,400,800)$ by $10^{15.01}$ | COMPUTED (inequality FALSE there) |
| 10 | Wedge extension to $n \ge i^2$ needs exactly $V^{\le} \le \binom{n}{i}^{\beta}$, $\beta \le 1/2 - cj/\log\binom{n}{i}$; any fixed $\beta < 1/2$ suffices for large $i$ ($\beta = 0.36$: $i \ge 1{,}600{,}321$) | PROVED |
| 11 | Candidate $V^{\le} \le n^{M(n,i)}$ is true | PROVED |
| 12 | Candidate closes exactly the region $\mathcal R_a$; nonempty band $i \ge 70$, $i^2 \le n < (i+1)^2$ | PROVED |
| 13 | Candidate fails at $(100, 10^6)$: $2M\log n = 3951.24$ vs budget $921.03$; flank (a) in general | COMPUTED barrier; OPEN |

**Not claimed:** Erdős #699 is not solved. Open after this file:
flank (c) for $\gamma > j^{*}(i)/i$ (all but a sliver at
$\gamma = 3/2$); flank (b) for $\gamma > 12/5$, and for
$\gamma \in (2, 12/5]$ at $i \le e^{20}$; flank (a) for $n \ge i^2$
outside $\mathcal R_a$; and the $i \le \sqrt n$ regime generally.
