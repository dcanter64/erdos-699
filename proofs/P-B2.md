# Proof P-B2: Strategy S1 (the Kummer small-part bound), independently formalized

**Prover:** B2 (independent). **Source strategy:** `strategies/S1.md`, read in
full before writing. This document reproves the S1 claims from scratch, in
my own order and with my own audits; where my argument differs in form from
S1's (notably the proof that $\pi(i-1) \le i/2$ and the derivative computation
for $\Delta$), the difference is deliberate and flagged. The recount in
Theorem B2.D is my own code, run by me, in exact integer arithmetic.

**Setting.** Erdős problem #699: for $1 \le i < j \le n/2$,
$\gcd(V_i(n), C(n,j)) > 1$, where $C(a,b) = \binom ab$ and, writing
$C(n,i) = u v$, $u$ is the part of $C(n,i)$ supported on primes $< i$ and
$v = V_i(n)$ is the part supported on primes $\ge i$. A *counterexample* is a
triple $(n,i,j)$ in range with $\gcd(v, C(n,j)) = 1$. The *open region* is
$j > 3i/2$; the closed region $j \le 3i/2$ is settled by Phase 0 plus EEES78.
$\pi(x)$ counts primes $\le x$; $\theta(x) = \sum_{p \le x} \log p$; all
logarithms are natural. Throughout, $n \ge 2j$ whenever a counterexample is
being discussed, since $j \le n/2$.

---

## 1. Lemmas

**Lemma B2.1 (key lemma).**
$C(n,i)\,C(n-i,\,j-i) = C(n,j)\,C(j,i)$. Hence any $d \mid C(n,i)$ with
$\gcd(d, C(n,j)) = 1$ satisfies $d \mid C(j,i) = C(j, j-i)$. Consequently a
counterexample satisfies
$$v \le C(j, j-i), \qquad C(n,i) \le u \cdot C(j, j-i).$$

*Proof.* Both sides of the identity equal
$n! / \big(i!\,(j-i)!\,(n-j)!\big)$: indeed
$C(n,i)C(n-i,j-i) = \frac{n!}{i!(n-i)!}\cdot\frac{(n-i)!}{(j-i)!(n-j)!}$ and
$C(n,j)C(j,i) = \frac{n!}{j!(n-j)!}\cdot\frac{j!}{i!(j-i)!}$.
Now let $d \mid C(n,i)$ with $\gcd(d, C(n,j)) = 1$. From the identity,
$d \mid C(n,j)\,C(j,i)$. A positive integer dividing a product and coprime
to one factor divides the other factor (Euclid's lemma, applied prime by
prime or via Bezout), so $d \mid C(j,i)$, and $C(j,i) = C(j, j-i)$ by
symmetry of the binomial coefficient. Apply this to $d = v$: by definition
$v \mid C(n,i)$, and a counterexample is exactly the case
$\gcd(v, C(n,j)) = 1$. Hence $v \mid C(j,j-i)$; since $v \ge 1$, $v \le
C(j,j-i)$, and multiplying by $u$ gives $C(n,i) = uv \le u\,C(j,j-i)$.
$\square$

**Lemma B2.2 (L-K: the Kummer prime-power bound, sharp form).**
For every prime $p$ and $1 \le i \le n$,
$$p^{v_p(C(n,i))} \le q_p(n) := p^{e_p(n)} \le n,
\qquad e_p(n) := \#\{k \ge 1 : p^k \le n\}.$$
For $p \le n$, $e_p(n) = \lfloor \log_p n \rfloor$.

*Proof.* Legendre's formula for the exponent of $p$ in a binomial
coefficient gives
$$v_p(C(n,i)) = \sum_{k \ge 1}
\Big( \lfloor n/p^k \rfloor - \lfloor i/p^k \rfloor
      - \lfloor (n-i)/p^k \rfloor \Big).$$
Two facts about the summands.

(i) *Each summand lies in $\{0,1\}$.* Put $x = i/p^k$ and
$y = (n-i)/p^k$, so $x + y = n/p^k$. Writing $x = \lfloor x \rfloor +
\{x\}$ and likewise for $y$, we get
$\lfloor x+y \rfloor - \lfloor x \rfloor - \lfloor y \rfloor
= \lfloor \{x\} + \{y\} \rfloor$, and $0 \le \{x\} + \{y\} < 2$, so this
floor is $0$ or $1$.

(ii) *Each summand vanishes for $p^k > n$.* Then $n/p^k < 1$, and also
$i/p^k < 1$ and $(n-i)/p^k < 1$ since $0 \le i \le n$, so all three floors
are $0$.

Therefore $v_p(C(n,i)) \le \#\{k \ge 1 : p^k \le n\} = e_p(n)$, i.e.
$p^{v_p(C(n,i))} \le p^{e_p(n)} = q_p(n)$. Finally
$q_p(n) = p^{e_p(n)} \le n$ by the definition of $e_p(n)$ as the count of
powers $p^k \le n$ (if $p > n$ the count is $0$ and $q_p(n) = 1 \le n$).
This is the Legendre form of Kummer's carry count: the summand at $k$ is
the carry indicator out of the $k$-th base-$p$ digit when $i$ and $n-i$
are added, but the argument above needs no quotation of Kummer's theorem.
$\square$

**Lemma B2.3 (small-part bounds; audit of $\pi(i-1) \le i/2$).**
Define
$$U^\sharp(n,i) := \prod_{p < i} q_p(n),
\qquad U(n,i) := n^{\pi(i-1)}.$$
Then:
(a) $u = \prod_{p<i} p^{v_p(C(n,i))} \le U^\sharp(n,i) \le U(n,i)$;
(b) $U^\sharp(n,i)$ is nondecreasing in $n$;
(c) if $i \le n$, $\prod_{p<i} p = e^{\theta(i-1)} \le U^\sharp(n,i)$;
(d) $\pi(i-1) \le i/2$ for **every** $i \ge 1$, and in particular
$\pi(i-1) < i$ for every $i \ge 1$.

*Proof.* (a) The factorization $C(n,i) = uv$ splits the prime factorization
of $C(n,i)$ by support, so $u = \prod_{p<i} p^{v_p(C(n,i))}$ exactly.
Apply Lemma B2.2 to each factor and multiply: $u \le \prod_{p<i} q_p(n)
= U^\sharp(n,i)$. Each $q_p(n) \le n$, and the number of factors is the
number of primes $< i$, namely $\pi(i-1)$, so $U^\sharp(n,i) \le
n^{\pi(i-1)} = U(n,i)$.

(b) Each $e_p(n)$, hence each $q_p(n)$, is nondecreasing in $n$.

(c) If $p < i \le n$ then $p^1 \le n$, so $e_p(n) \ge 1$ and $q_p(n) \ge p$;
multiply over $p < i$.

(d) *Audit.* S1 asserts $\pi(i-1) \le i/2$ for $i \ge 3$ with the one-line
justification that the primes in $[2, i-1]$ are $2$ together with odd
integers, "at most $1 + (i-2)/2 = i/2$ of them". The inequality is correct
for all $i$, but the counting phrase is compressed, so here is a watertight
version. For $i \le 2$, $\pi(i-1) = \pi(0)$ or $\pi(1) = 0 \le i/2$. For
$i \ge 3$: every prime $\le i-1$ is either $2$ or an odd prime in
$[3, i-1]$. The odd integers in $[1, i-1]$ number exactly
$\lfloor i/2 \rfloor$ (one in each pair $\{1,2\}, \{3,4\}, \dots$, with a
final singleton when $i-1$ is odd), and excluding the odd integer $1$
leaves $\lfloor i/2 \rfloor - 1$ odd integers in $[3, i-1]$. Hence
$$\pi(i-1) \le 1 + \big(\lfloor i/2 \rfloor - 1\big) = \lfloor i/2 \rfloor
\le i/2.$$
(I also verified the inequality by brute force for all $i < 5000$: no
violations; equality $\pi(i-1) = i/2$ holds for $i \in \{4, 6, 8\}$ among
$i \le 100$.) Finally $\pi(i-1) \le i/2 < i$ for $i \ge 1$ unless
$\pi(i-1) = 0 < i$, so $\pi(i-1) < i$ always. $\square$

**Lemma B2.4 (monotonicity and growth of the crude ratio; Bernoulli audit).**
For every $i \ge 1$, $F_i(n) := C(n,i)/n^{\pi(i-1)}$ is strictly increasing
for $n \ge i$, and $F_i(n) \ge n^{\,i - \pi(i-1)}/i^{\,i} \to \infty$ as
$n \to \infty$.

*Proof.* Write $\pi = \pi(i-1)$; by Lemma B2.3(d), $\pi < i$.

*The ratio, transformed.* For $n \ge i$,
$$\frac{F_i(n+1)}{F_i(n)}
= \frac{n+1}{\,n+1-i\,}\Big(\frac{n}{n+1}\Big)^{\pi},$$
since $C(n+1,i)/C(n,i) = (n+1)/(n+1-i)$. This exceeds $1$ if and only if
$(n+1)\,n^{\pi} > (n+1-i)\,(n+1)^{\pi}$, and dividing both sides by the
positive number $n+1$ (note $n + 1 - i \ge 1$ as $n \ge i$), if and only if
$$\frac{n^{\pi}}{(n+1)^{\pi-1}} > n+1-i. \tag{$\ast$}$$
I treat the three cases separately, because the Bernoulli step below is
valid only in the third.

*Case $\pi = 0$* (this is $i \le 2$). Then ($\ast$) reads $n + 1 > n + 1 - i$,
true since $i \ge 1$ (indeed $F_i(n+1)/F_i(n) = (n+1)/(n+1-i) > 1$
directly).

*Case $\pi = 1$* (this forces $i - 1 = 2$, i.e. $i = 3$). Then ($\ast$)
reads $n > n + 1 - i$, true since $i = 3 > 1$.

*Case $\pi \ge 2$ (Bernoulli step, audited).* Bernoulli's inequality
$(1 + x)^r \ge 1 + rx$ holds for integer $r \ge 1$ and $x \ge -1$.
Apply it with $r = \pi - 1 \ge 1$ and $x = -1/(n+1) \ge -1$:
$$\frac{n^{\pi}}{(n+1)^{\pi-1}}
= n\Big(1 - \frac{1}{n+1}\Big)^{\pi-1}
\ge n\Big(1 - \frac{\pi-1}{n+1}\Big)
= n - \frac{n(\pi-1)}{n+1}
> n - (\pi - 1) \ge n + 1 - i.$$
The strict inequality in the middle uses $\frac{n}{n+1} < 1$ and
$\pi - 1 > 0$; the last inequality uses $\pi \le i$ (Lemma B2.3(d) gives
the stronger $\pi \le i/2$ for $i \ge 3$, but only $\pi \le i$ is needed,
which is exactly what S1's proof uses at this step; the step is valid as
written in S1). Thus ($\ast$) holds, $F_i$ is strictly increasing, in all
cases.

*Growth.* $C(n,i) = \prod_{t=0}^{i-1} \frac{n-t}{i-t} \ge (n/i)^i$ for
$n \ge i$, because each factor satisfies $\frac{n-t}{i-t} \ge \frac ni$:
cross-multiplying, $i(n-t) \ge n(i-t)$ reduces to $nt \ge it$, true since
$n \ge i$ and $t \ge 0$. Hence $F_i(n) \ge n^{i-\pi}/i^i$, and $i - \pi
\ge 1$ since $\pi < i$ (Lemma B2.3(d)) and both are integers, so
$F_i(n) \to \infty$. $\square$

**Lemma B2.5 (sharp test: finiteness and sawtooth structure).**
Let $G_i(n) := C(n,i)/U^\sharp(n,i)$ and
$\mathrm{Bad}^\sharp(i,j) := \{n \ge 2j : G_i(n) \le C(j, j-i)\}$. Then:
(a) $G_i(n) \ge F_i(n)$ for all $n$, so $\mathrm{Bad}^\sharp(i,j)$ is
finite and $\mathrm{Bad}^\sharp(i,j) \subseteq [2j, N_K(i,j)]$, where
$N_K(i,j) := \max\{n \ge i : F_i(n) \le C(j,j-i)\}$ is well defined (the
set is nonempty since $F_i(i) = i^{-\pi(i-1)} \le 1 \le C(j,j-i)$, and
bounded since $F_i \to \infty$) and $[2j, N_K(i,j)]$ is an interval
condition: $F_i(n) \le C(j,j-i)$ iff $n \le N_K(i,j)$.
(b) $G_i$ is strictly increasing on every interval where $U^\sharp(\cdot, i)$
is constant; $U^\sharp(\cdot, i)$ jumps exactly at integers $n = p^e$ with
$p < i$ prime and $e \ge 1$ (at $n = p^e$, $e_p$ increments), by the factor
$p$ for that prime, and within $[2j, \infty)$ only jumps with $e \ge 2$
occur. Hence every local minimum of $G_i$ on $[2j, \infty)$
is attained at $n = 2j$ or at a jump point.
(c) $\mathrm{Bad}^\sharp$ need not be an interval.

*Proof.* (a) $U^\sharp \le U$ (Lemma B2.3(a)) gives $G_i \ge F_i$;
Lemma B2.4 gives monotonicity and growth of $F_i$, hence the rest.
(b) $C(n,i)$ is strictly increasing in $n \ge i$ (ratio
$(n+1)/(n+1-i) > 1$) while $U^\sharp$ is a nondecreasing step function
(Lemma B2.3(b)) whose value changes exactly when some
$e_p(n) = \#\{k : p^k \le n\}$ increments, i.e. when $n$ crosses a power
$p^e$; crossing $p^1$ happens at $n = p \le i - 1 < 2j$, below the range
of interest, so within $[2j, \infty)$ the jumps are at $p^e$, $e \ge 2$.
On a constancy interval the minimum of $G_i$ is at its left endpoint, and
the left endpoints are $2j$ and the jump points.
(c) Proved by the exact example in Remark B2.8 below:
$\mathrm{Bad}^\sharp(3,7) = \{16\}$, a singleton with $14, 15 \notin
\mathrm{Bad}^\sharp(3,7)$. $\square$

**Lemma B2.6 (the entropy function $\Delta$).**
Let $h(p) = -p \log p - (1-p)\log(1-p)$ for $p \in [0,1]$ (with
$0 \log 0 = 0$) and, for $c \ge 1$,
$$\Delta(c) := 2c\, h\!\Big(\frac{1}{2c}\Big) - c\, h\!\Big(\frac1c\Big).$$
Then:
(i) $\Delta(c) = \big[2c \log(2c) - (2c-1)\log(2c-1)\big]
- \big[c \log c - (c-1)\log(c-1)\big]$, with $(c-1)\log(c-1)$ read as $0$
at $c = 1$.
(ii) $\Delta$ is continuous on $[1, \infty)$, strictly decreasing on
$(1, \infty)$, with $\Delta(1) = 2\log 2 = 1.38629\ldots$ and
$\lim_{c\to\infty} \Delta(c) = \log 2 = 0.69314\ldots$
(iii) $\Delta(c) = 1$ has exactly one root $c^\ast$, and
$c^\ast \in (1.36, 1.37)$, $c^\ast = 1.36722\ldots$
(iv) $\Delta(3/2) = 0.95477\ldots$ and $\Delta(2) = 0.86305\ldots$

*Proof.* (i) Direct expansion: $2c\,h(1/(2c)) = \log(2c) - (2c-1)
\log\frac{2c-1}{2c} = 2c\log(2c) - (2c-1)\log(2c-1)$, and similarly
$c\,h(1/c) = c \log c - (c-1)\log(c-1)$.

(ii) Differentiate the closed form (i). With
$A(c) = 2c\log(2c) - (2c-1)\log(2c-1)$ and
$B(c) = c\log c - (c-1)\log(c-1)$:
$$A'(c) = 2\log(2c) + 2 - 2\log(2c-1) - 2 = 2\log\frac{2c}{2c-1},
\qquad
B'(c) = \log c + 1 - \log(c-1) - 1 = \log\frac{c}{c-1}.$$
Hence
$$\Delta'(c) = 2\log\frac{2c}{2c-1} - \log\frac{c}{c-1}
= \log\Big(\frac{4c^2}{(2c-1)^2}\cdot\frac{c-1}{c}\Big)
= \log\frac{4c(c-1)}{(2c-1)^2}.$$
Now
$(2c-1)^2 = 4c^2 - 4c + 1 = 4c(c-1) + 1 > 4c(c-1)$ for $c > 1$, so the
argument of the logarithm is $< 1$ and $\Delta'(c) < 0$ on $(1, \infty)$:
$\Delta$ is strictly decreasing there. This derivative identity is my own
route to the monotonicity; S1 asserts monotonicity by "a routine
derivative computation", and the computation, done explicitly, is the
identity above. $\Delta(1) = 2\log 2$ from (i). For the limit, rewrite
$A(c) = \log(2c) + (2c-1)\log\frac{2c}{2c-1} = \log 2 + \log c +
(2c-1)\log\big(1 + \frac{1}{2c-1}\big)$ and
$B(c) = \log c + (c-1)\log\big(1 + \frac{1}{c-1}\big)$; since
$m \log(1 + 1/m) \to 1$ as $m \to \infty$, $A(c) - B(c) \to \log 2$.

(iii) $\Delta$ continuous, strictly decreasing from $2\log 2 > 1$ to
$\log 2 < 1$ gives existence and uniqueness. Numerical evaluation of the
closed form (i) gives $\Delta(1.36) = 1.00295 > 1$ and
$\Delta(1.37) = 0.99888 < 1$, so $c^\ast \in (1.36, 1.37)$; bisection on
the same closed form gives $c^\ast = 1.3672188\ldots$, i.e. $1.3672$ to
four decimals, matching S1. Floating point is used only to identify this
constant, nowhere in any counting decision (see Theorem B2.D).

(iv) Substituting $c = 3/2$ and $c = 2$ in (i):
$\Delta(3/2) = [3\log 3 - 2\log 2] - [\frac32\log\frac32 -
\frac12\log\frac12] = 0.95477\ldots$ and
$\Delta(2) = [4\log 4 - 3\log 3] - 2\log 2 = 0.86305\ldots$ $\square$

---

## 2. Theorem A (T-A: the EEES-free finite reduction)

**Theorem B2.A.**
If $(n, i, j)$ is a counterexample, then
$$C(n,i) \le U^\sharp(n,i)\, C(j, j-i),
\qquad\text{i.e.}\qquad
n \in \mathrm{Bad}^\sharp(i,j) \subseteq [2j, N_K(i,j)].$$
Hence each pair $(i,j)$ admits only finitely many candidate $n$, with an
explicit bound $N_K(i,j)$, using no EEES78 input and no exception list.
A counterexample also satisfies the crude form
$F_i(n) \le C(j, j-i)$, i.e. $n \le N_K(i,j)$; combined with Phase 0, a
counterexample whose $(n,i)$ is not an EEES78 exception satisfies
$n \le \min(N_K(i,j), N(i,j))$, and $n \le N_K(i,j)$ unconditionally.

*Proof.* Lemma B2.1 gives $C(n,i) \le u\,C(j,j-i)$; Lemma B2.3(a) bounds
$u \le U^\sharp(n,i)$; that is the displayed inequality, i.e.
$G_i(n) \le C(j,j-i)$, i.e. $n \in \mathrm{Bad}^\sharp(i,j)$.
Lemma B2.5(a) gives the containment in $[2j, N_K(i,j)]$ and, via
$G_i \ge F_i$, the crude form. The $\min$ statement is the conjunction of
this bound with the Phase 0 bound $n \le N(i,j)$, which needs the EEES78
hypothesis; the Kummer bound $N_K$ alone does not. $\square$

**Remark B2.7 (fixed-$i$ strength).** For fixed $i$ and $j \to \infty$,
the condition $C(n,i) \le n^{\pi(i-1)} C(j, j-i)$ with
$C(m,i) \sim m^i / i!$ gives $N_K(i,j) = j^{e(i)}(1 + o(1))$ with
$e(i) = i/(i - \pi(i-1))$, against $N(i,j) \sim \kappa_i j^2$ for EEES.
By Lemma B2.3(d), $e(i) < 2$ iff $\pi(i-1) < i/2$, which holds for all
$i \ge 3$ except the equalities $i \in \{4, 6, 8\}$ (where $e(i) = 2$ and
constants decide). So far from the diagonal the Kummer interval is
eventually the shorter one; near the diagonal the comparison reverses
(Theorem B2.C). The operative combined bound is $\min(N_K, N)$.

---

## 3. Theorem B (T-B: all-$n$ closures by this route alone)

**Theorem B2.B.**
The following open-region pairs are closed for all $n$ by size alone, with
no EEES78 input and no sweep: (1) $i = 1$, every $j > 1$; (2) $i = 2$,
every $j > 2$; (3) $(i,j) = (3,5)$; (4) $(i,j) = (3,6)$, the last one
requiring the sharpened bound. All endpoint evaluations below are exact
integer arithmetic (cross-multiplied; no decimals in any decision).

*Proof.* In each case a counterexample would need $n \ge 2j$ and, by
Theorem B2.A, $G_i(n) \le C(j, j-i)$; I show $G_i(n) > C(j,j-i)$ for all
$n \ge 2j$.

(1) $i = 1$: there is no prime $< 1$, so $u = 1$ (empty product) and
$v = C(n,1) = n$. Lemma B2.1 would force $n = v \le C(j, 0) = 1$,
contradicting $n \ge 2j \ge 4$.

(2) $i = 2$: there is no prime $< 2$, so again $u = 1$ and
$v = C(n,2)$. Lemma B2.1 would force $C(n,2) \le C(j, j-2) = C(j,2)$.
But $C(\cdot, 2)$ is strictly increasing in its top argument, and
$n \ge 2j > j$, so $C(n,2) \ge C(2j,2) = j(2j-1) > \frac{j(j-1)}{2}
= C(j,2)$ (the last inequality cross-multiplies to $2(2j-1) > j - 1$,
true). Contradiction.

(3) $(3,5)$: target $C(5, 2) = 10$. Here $\pi(2) = 1$, so
$F_3(n) = C(n,3)/n$. At the endpoint $n = 2j = 10$:
$C(10,3) = 120$, and $120 > 10 \cdot 10 = 100$, i.e. $F_3(10) = 12 > 10$.
For all $n \ge 10$: $G_3(n) \ge F_3(n) \ge F_3(10) > 10$ by
Lemmas B2.5(a) and B2.4. So $\mathrm{Bad}^\sharp(3,5) = \varnothing$.
Note the crude bound already suffices here.

(4) $(3,6)$: target $C(6,3) = 20$. Split at $n = 16$.
On $[12, 15]$: the only prime $< 3$ is $2$, and $8 \le n < 16$ gives
$e_2(n) = 3$, so $U^\sharp(n,3) = 8$, constant; by Lemma B2.5(b) $G_3$
is increasing on this interval, so its minimum is at $n = 12$:
$C(12,3) = 220 > 20 \cdot 8 = 160$, i.e. $G_3(12) = 220/8 = 55/2 > 20$.
For $n \ge 16$: $G_3(n) \ge F_3(n) \ge F_3(16)$ by Lemmas B2.5(a) and
B2.4, and $C(16,3) = 560 > 20 \cdot 16 = 320$, i.e. $F_3(16) = 35 > 20$.
Hence $G_3(n) > 20$ for all $n \ge 12 = 2j$:
$\mathrm{Bad}^\sharp(3,6) = \varnothing$. The crude bound alone does
not close $(3,6)$ at the left endpoint ($F_3(12) = 220/12 < 20$), which
is why the sharpened bound is needed exactly on $[12,15]$. $\square$

**Remark B2.8 (the boundary case $(3,7)$, exact).**
$(3,7)$ is *not* closed by size, and the obstruction is a single exact
equality. Target $C(7,3) = 35$. Crude: $F_3(16) = 560/16 = 35 \le 35$ and
$F_3(17) = 680/17 = 40 > 35$, so $N_K(3,7) = 16$ by Lemma B2.4. Sharp
check of the only remaining candidates $n \in \{14, 15, 16\}$:
$U^\sharp(14,3) = U^\sharp(15,3) = 8$ and $C(14,3) = 364 > 35 \cdot 8
= 280$, $C(15,3) = 455 > 280$, so $14, 15 \notin \mathrm{Bad}^\sharp$;
$U^\sharp(16,3) = 2^4 = 16$ and $C(16,3) = 560 = 35 \cdot 16$ exactly,
so $16 \in \mathrm{Bad}^\sharp$. Hence
$\mathrm{Bad}^\sharp(3,7) = \{16\}$, proving Lemma B2.5(c). The
equality is the tight case of Lemma B2.2: at $(n,i) = (16,3)$ the true
small part is $u = 16 = U^\sharp = U$ (namely $C(16,3) = 560 = 16 \cdot
35$). The pair $(3,7)$ is of course closed by the direct check
$\gcd(v, C(16,7)) = \gcd(35, 11440) = 5 > 1$, already inside the
$n \le 10000$ sweep; the point here is only that *size alone* cannot
close it. I make no claim in this document about left-endpoint closure
for other pairs with $i \ge 3$ beyond Theorem B2.B; the exhaustive
$i \le 60$ scan asserted in S1 (its Proposition B$'$) was not part of my
brief and I have not reproduced it.

---

## 4. Theorem C (the diagonal barrier: a proved limitation of the route)

**Theorem B2.C.**
Fix $c \ge 1$ and let $j = \lfloor ci \rfloor$, $n = 2j$. Let
$R(i,j) = \log F_i(n) - \log C(j, j-i)$ and
$R^\sharp(i,j) = \log G_i(n) - \log C(j, j-i)$ be the crude and sharp
log-margins at the left endpoint. Then, as $i \to \infty$,
$$\frac{R(i,j)}{i} \longrightarrow \Delta(c) - 1,
\qquad
\frac{R^\sharp(i,j)}{i} \longrightarrow \Delta(c) - 1,$$
with $\Delta$ as in Lemma B2.6. Consequently, for every $c > c^\ast
= 1.36722\ldots$ there is $i_0(c)$ such that no pair
$(i, \lfloor ci \rfloor)$ with $i \ge i_0(c)$ is closed by this route,
for either bound: the endpoint $n = 2j$ itself is not excluded. Since
$c^\ast < 3/2$, this route cannot prove $j \le ci$ for any $c > 3/2$
uniformly in $i$, and cannot even re-derive the known $j \le 3i/2$
closure for large $i$: at $c = 3/2$ the margin per unit $i$ tends to
$\Delta(3/2) - 1 = -0.04523\ldots$

*Proof.* Three inputs.

*Entropy term.* By Stirling's formula in the form
$\log C(N,K) = N h(K/N) + O(\log N)$, valid uniformly for $K/N$ in a
compact subinterval of $(0,1)$ (the error term is
$-\frac12 \log\big(2\pi N \frac KN (1 - \frac KN)\big) + O(1/K +
1/(N-K))$): for fixed $c > 1$, apply it to $C(2j, i)$ (ratio
$i/(2j) \to 1/(2c)$) and to $C(j, j-i)$ (ratio $(j-i)/j \to 1 - 1/c$).
Since $j = ci + O(1)$ and $h$ is smooth near the limiting ratios,
$2j\, h(i/(2j)) = 2ci\, h(1/(2c)) + O(1)$ and
$j\, h((j-i)/j) = ci\, h(1 - 1/c) + O(1) = ci\, h(1/c) + O(1)$ by the
symmetry $h(p) = h(1-p)$ (equivalently $C(j, j-i) = C(j,i)$). Hence
$$\log C(2j, i) - \log C(j, j-i) = \Delta(c)\, i + O(\log i).$$
For $c = 1$ separately: $j = i$, $C(j, j-i) = 1$, and
$\log C(2i, i) = 2i\log 2 + O(\log i)$ by Stirling, matching
$\Delta(1) = 2\log 2$.

*Crude denominator.* $R$ subtracts $\pi(i-1)\log(2j)$ from the entropy
term. By the prime number theorem, $\pi(i-1) = (1 + o(1))\, i / \log i$
and $\log(2j) = (1 + o(1)) \log i$, so $\pi(i-1)\log(2j) = i + o(i)$.

*Sharp denominator.* $R^\sharp$ subtracts $\log U^\sharp(2j, i)$, and by
Lemma B2.3(a),(c),
$$\theta(i-1) \le \log U^\sharp(2j, i) \le \pi(i-1)\log(2j).$$
By the prime number theorem in the form $\theta(x) \sim x$, the left end
is $i + o(i)$; by the previous paragraph the right end is $i + o(i)$.
Squeeze: $\log U^\sharp(2j,i) = i + o(i)$. The sharpening therefore
changes $\log U$ by $o(i)$ only, and cannot change the exponential rate.

Dividing by $i$ gives both limits $\Delta(c) - 1$. If $c > c^\ast$ then
$\Delta(c) < 1$ (Lemma B2.6(ii),(iii)), so $R(i, \lfloor ci \rfloor) < 0$
and $R^\sharp(i, \lfloor ci \rfloor) < 0$ for all large $i$: at
$n = 2j$, $F_i(n) \le C(j, j-i)$ (resp. $G_i(n) \le C(j,j-i)$), so the
pair is not closed by the crude (resp. sharp) test. Taking
$c > 3/2 > c^\ast$ gives the stated barrier, and $c = 3/2$ itself has
negative limiting margin $-0.04523\ldots$ per unit $i$. $\square$

**Remark B2.9 (what the barrier means).** Closing $(i, ci)$ by size at
$n = 2j$ needs $\log U \le (\Delta(c) - \varepsilon)i$; at $c = 3/2$
that is $u \le C(n,i)^{0.4997}$-strength at $n = 3i$, essentially the
EEES78 threshold $u < C(n,i)^{1/2}$ itself. So the Kummer route, pushed
to its limit, re-derives the need for EEES-strength input rather than
replacing it. Its genuine deliverables are Theorem B2.A (an independent,
exception-free reduction), Theorem B2.B, and Theorem B2.D below. Note
also that convergence in Theorem B2.C is slow (the $o(i)$ terms involve
$\log\log i / \log i$), so finite diagonal margins are worse than the
limit; this is consistent with the interval comparisons in S1 §4(b),
which I have not reproduced and do not rely on.

---

## 5. Theorem D (T-D: independent exact recount of the payoff)

**Theorem B2.D (my recount).**
Let $1 \le i \le 1000$, $j > 3i/2$, $2j \le 10000$. Say a pair is
*newly cleared* if $N(i,j) > 10000$ (not fully cleared by the EEES
classification) but $N_K(i,j) \le 10000$. Then the number of newly
cleared pairs is exactly
$$\mathbf{328{,}079},$$
of which exactly $\mathbf{318{,}242}$ have $i \ge 3$ (the remaining
$9{,}837$ have $i \in \{1,2\}$ and are in any case closed for all $j$ by
Theorem B2.B). The spot values are $J_K(100) = \mathbf{1045}$ and
$J_K(1000) = \mathbf{2541}$, where $J_K(i)$ is the largest $j$ with
$2j \le 10000$ cleared by the Kummer criterion. These agree with S1's
claims in full; see the comparison and the discrepancy statement below.

*Proof (of the reduction to the count; the count itself is the exact
computation in Appendix A).*

*Threshold equivalences, all exact.* $N(i,j) > 10000$ iff
$C(10001, i) < C(2j, 2(j-i))$: indeed $N(i,j) = \max\{n : C(n,i) <
C(2j, 2(j-i))\}$ and $C(\cdot, i)$ is strictly increasing, so
$10001 \le N(i,j)$ iff $C(10001, i) < C(2j, 2(j-i))$.
$N_K(i,j) \le 10000$ iff $F_i(10001) > C(j, j-i)$ (Lemma B2.4: $F_i$
strictly increasing, so the set $\{n : F_i(n) \le C(j,j-i)\}$ is an
initial segment, and its maximum is $\le 10000$ iff $10001$ is outside
it, with strictness exactly as stated: equality $F_i(10001) =
C(j,j-i)$ would put $10001$ in the set). Cross-multiplying the positive
denominator, this is the exact integer inequality
$$C(j, j-i) \cdot 10001^{\pi(i-1)} < C(10001, i). \tag{$\dagger$}$$

*Prefix structure in $j$.* For fixed $i$, both sides' $j$-dependent
terms are strictly increasing in $j$: $C(j, j-i) = C(j,i)$ has ratio
$(j+1)/(j+1-i) > 1$ in $j$, and
$C(2j+2, 2(j+1-i))/C(2j, 2(j-i)) = \frac{(2j+2)(2j+1)}{(2(j-i)+2)(2(j-i)+1)}
> 1$ since $j > j - i$. Hence for each $i$ the EEES-cleared set and the
Kummer-cleared set are prefixes of the $j$-range, determined by their
maximal elements $J_E(i)$ and $J_K(i)$, and the newly cleared count for
this $i$ is $\max\big(0, \min(J_K(i), 5000) - \max(\lfloor 3i/2 \rfloor,
J_E(i))\big)$ (number of integers $j$ with $\lfloor 3i/2 \rfloor < j \le
J_K(i)$ and $j > J_E(i)$). Summing over $i$ gives the total. Appendix A
computes $J_E(i)$ and $J_K(i)$ for all $i \le 1000$ by exact integer
binary search on the two threshold inequalities (no floats anywhere in
the decision path: every comparison is $(\dagger)$ or its EEES analogue
between Python integers) and performs the sum. $\square$

**My results, and comparison with S1.**

| quantity | S1 claims | my recount | agreement |
|---|---|---|---|
| newly cleared pairs, $i \le 1000$ | 328,079 | **328,079** | exact |
| of which $i \ge 3$ | 318,242 | **318,242** | exact |
| $J_K(100)$ | 1045 | **1045** | exact |
| $J_K(1000)$ | 2541 | **2541** | exact |
| EEES cleared total (cross-check) | 768,741 | 768,741 | exact |
| combined cleared total | 1,096,820 | 1,096,820 | exact |
| total open pairs classified | 4,249,500 | 4,249,500 | exact |

Spot table from my run ($J_E$ = EEES threshold, $J_K$ = Kummer
threshold): $(i, J_E, J_K) = (3, 112, 465)$, $(5, 142, 253)$,
$(10, 199, 255)$, $(11, 209, 355)$, $(50, 454, 654)$, $(100, 656, 1045)$,
$(500, 1597, 1950)$, $(1000, 2391, 2541)$. Every one of these matches
the corresponding entry in S1's Theorem D table. As an additional
cross-check, my recomputed $J_E(i)$ equals the maximum cleared $j$ in
`pairpass.json`'s `cleared_js_by_i` for **all** $1000$ values of $i$
(zero mismatches), and my EEES cleared recount reproduces
`pairpass.json`'s `pairs_fully_cleared = 768741` exactly. My script's
runtime was $29.0$ s, inside the $\sim$2 minute budget.

**Discrepancy statement: none.** My independent count, both spot
values, the $i \ge 3$ subtotal, and all eight spot pairs I printed
agree with S1 exactly. Two presentational points, neither a numerical
discrepancy: (1) for $i \in \{1, 2\}$ the raw $J_K$ is $10000$ ($i = 2$)
or unbounded ($i = 1$, since $C(j,0) = 1 < C(10001,1)$ for every $j$);
the count above correctly treats $J_K$ inside the classified window
$2j \le 10000$, i.e. capped at $5000$, contributing $4930$ ($i = 1$) and
$4907$ ($i = 2$) newly cleared pairs. The spot values at $i = 100$ and
$i = 1000$ are far below the cap and are raw values. (2) The criterion
counted here is the *crude* one, $(\dagger)$; the sharp sawtooth test of
Lemma B2.5 could only clear more pairs, so 328,079 is a lower bound for
the sharp payoff, exactly as S1 states. I did not compute the sharp
count.

**Consequence.** For every newly cleared pair, Theorem B2.A excludes
counterexamples with $n > 10000$ with no EEES78 input, and the completed
sweep (`RESULTS.md`: zero counterexamples among all open-region triples
with $n \le 10000$) excludes the rest. So these $328{,}079$ pairs are
fully cleared, independently of EEES78, and the cleared total rises
from $768{,}741$ to $1{,}096{,}820$ of $4{,}249{,}500$ classified pairs.

---

## 6. Scope and gaps (stated plainly)

* Proved here, completely: Lemmas B2.1 to B2.6 (in particular (L-K) as
  Lemma B2.2, including the audit that $\pi(i-1) \le i/2$ holds for all
  $i$ and that the Bernoulli step in the monotonicity proof is valid as
  S1 states it, with the $\pi = 0$ and $\pi = 1$ cases genuinely
  separate), Theorem B2.A (T-A, crude and sharp forms), Theorem B2.B
  (T-B, all four closures, exact endpoint arithmetic), Theorem B2.C
  (the $c^\ast \approx 1.3672$ barrier, with the entropy computation
  done explicitly in Lemma B2.6), Theorem B2.D (T-D, my own exact
  recount).
* External inputs used, and only these: Legendre's formula (proved
  from in the sense that only its standard floor-sum form is quoted),
  Stirling's formula, and the prime number theorem (in both
  $\pi(x) \sim x/\log x$ and $\theta(x) \sim x$ forms) for Theorem
  B2.C only. Theorems B2.A, B2.B, B2.D are elementary apart from the
  quoted Legendre form and, for B2.D's consequence, the Phase 0 key
  lemma (reproved as B2.1) and the $n \le 10000$ sweep result.
* Not claimed here: S1's Proposition B$'$ (no left-endpoint closure
  for $4 \le i \le 60$ in range, and for $i = 3$, $j \ge 8$), the sharp
  version of the Theorem D count, the tightness/slack table of S1
  §4(d), and the crossover computations of S1 §4(b),(c). None of the
  theorems above depends on any of these.
* Floating point appears only in identifying the constant $c^\ast$ and
  the values $\Delta(3/2)$, $\Delta(2)$ in Lemma B2.6; every inequality
  that decides a closure or a count is exact integer arithmetic.

---

## Appendix A: the recount script (Python stdlib only, as run)

Runtime $29.0$ s on this machine. Every decision is an exact integer
comparison; `pairpass.json` is read only as a cross-check of $J_E$,
never as an input to the count.

```python
import math, time, json, os, bisect
from math import comb
t0 = time.time()
NSTAR, IMAX, JMAX = 10000, 1000, 5000

# sieve for pi
N = 1000
sieve = [True] * (N + 1); sieve[0] = sieve[1] = False
for p in range(2, int(N ** 0.5) + 1):
    if sieve[p]:
        sieve[p*p::p] = [False] * len(sieve[p*p::p])
primes = [p for p, v in enumerate(sieve) if v]
def pi(x): return bisect.bisect_right(primes, x)

def largest_true(pred, lo, hi):
    # pred monotone True...True False...False on [lo, hi]
    if not pred(lo): return lo - 1
    if pred(hi): return hi
    a, b = lo, hi                      # pred(a) True, pred(b) False
    while b - a > 1:
        m = (a + b) // 2
        if pred(m): a = m
        else: b = m
    return a

pp = json.load(open(os.path.expanduser(
    '~/workspace/math-hunt/erdos-699/pairpass.json')))
cleared = pp['cleared_js_by_i']

total = total_ge3 = 0
JK, JE, mismatch_E = {}, {}, []
for i in range(1, IMAX + 1):
    Ti = comb(NSTAR + 1, i)
    Pi = (NSTAR + 1) ** pi(i - 1)
    # EEES: N(i,j) <= 10000 iff C(2j, 2(j-i)) <= C(10001, i)
    jE = largest_true(lambda j, i=i, Ti=Ti:
                      comb(2*j, 2*(j-i)) <= Ti, i, JMAX)
    # Kummer crude: N_K(i,j) <= 10000 iff C(j, j-i) * 10001^pi(i-1) < C(10001, i)
    jK = largest_true(lambda j, i=i, Ti=Ti, Pi=Pi:
                      comb(j, j-i) * Pi < Ti, i, JMAX)
    JE[i], JK[i] = jE, jK
    lst = cleared[str(i)]
    if (max(lst) if lst else None) != jE:
        mismatch_E.append(i)
    lo = 3*i//2 + 1
    cnt = max(0, min(jK, JMAX) - max(lo, jE + 1) + 1)
    total += cnt
    if i >= 3: total_ge3 += cnt

print("TOTAL_NEW", total)              # 328079
print("TOTAL_NEW_i_ge3", total_ge3)    # 318242
print("JK100", JK[100], "JK1000", JK[1000])   # 1045 2541
print("mismatch_E_count", len(mismatch_E))    # 0
print("elapsed_s", round(time.time() - t0, 2))  # 29.04
```

## Appendix B: exact endpoint arithmetic used in Theorem B2.B and Remark B2.8

All values computed with `math.comb` (exact integers):
$C(10,3) = 120$, $C(5,2) = 10$, $120 > 100$;
$C(12,3) = 220$, $20 \cdot 8 = 160$, $220 > 160$;
$C(16,3) = 560$, $20 \cdot 16 = 320$, $560 > 320$;
$C(7,3) = 35$, $C(14,3) = 364 > 35 \cdot 8 = 280$,
$C(15,3) = 455 > 280$, $C(16,3) = 560 = 35 \cdot 16$;
$C(17,3) = 680$, $680/17 = 40 > 35$;
$\gcd(35, C(16,7)) = \gcd(35, 11440) = 5$.
Entropy values (float, identification only):
$\Delta(1) = 1.386294$, $\Delta(1.36) = 1.002947$,
$\Delta(1.3672) = 1.000008$, $\Delta(1.37) = 0.998881$,
$\Delta(3/2) = 0.954771$, $\Delta(1.6) = 0.928975$,
$\Delta(2) = 0.863046$; bisection root $c^\ast = 1.3672188\ldots$
