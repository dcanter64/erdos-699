# Prover A1 (independent): small-i closures of Erdos Problem #699

Prover: A1, working independently. This document was produced from the
strategy papers S6 (Section 2), S8 (Sections 2 and 3), S5 (boundary family
and surplus/square material), and S1 (Theorem B), together with the Phase 0
record (PHASE0.md) and the Stage 2 record (RESULTS.md). No other prover's
proof document was read. Every computational claim below was recomputed
independently by this prover in Python (standard library only, exact integer
arithmetic; symbolic ratio identities additionally verified with SymPy exact
rational simplification). Section 7 is an audit log: it records one material
error found in a source claim (S5's EEES78 proviso), with the counterexample,
and confirms that the affected theorem survives after correction.

## 0. Setting, notation, and standing inputs

Problem #699: for $1 \le i < j \le n/2$, show that there is a prime
$p \ge i$ dividing both $\binom ni$ and $\binom nj$. Write $C(n,k) = \binom nk$.
For a prime $p$, $v_p(m)$ is the $p$-adic valuation. Define

$$V_i(n) = \prod_{p \ge i} p^{v_p(C(n,i))}, \qquad
U_i(n) = \prod_{p < i} p^{v_p(C(n,i))},$$

so $C(n,i) = U_i(n) V_i(n)$ with $\gcd(U_i(n), V_i(n)) = 1$. The problem is
equivalent to $\gcd(V_i(n), C(n,j)) > 1$ for all $1 \le i < j \le n/2$:
the prime divisors of $V_i(n)$ are exactly the primes $\ge i$ dividing
$C(n,i)$. A triple $(n,i,j)$ with $\gcd(V_i(n), C(n,j)) = 1$ is called a
**counterexample**.

Standing inputs, each flagged where used:

- (EEES78) Ecklund, Eggleton, Erdos, Selfridge (1978): $U_i(n) < V_i(n)$,
  equivalently $V_i(n)^2 > C(n,i)$, for all $(n,i)$ with $i \le n/2$ except
  exactly 12 exception pairs:
  $(8,3)$, $(9,4)$, $(10,5)$, $(12,5)$, $(21,7)$, $(21,8)$, $(30,7)$,
  $(33,13)$, $(33,14)$, $(36,13)$, $(36,17)$, $(56,13)$.
  (List as recorded in PHASE0.md, Item 4, and independently confirmed there
  by two computations.)
- (Closed region) For $j \le 3i/2$ there is no counterexample with
  $(n,i)$ a non-exception pair (Phase 0, Item 3, refereed sound there,
  conditional on EEES78), and all 12 exception pairs have been discharged
  by direct computation for every admissible $j$ (RESULTS.md: 41 triples,
  all gcds $> 1$). Hence the region $j \le 3i/2$ is settled for all $n$.
  This input is used only in Section 6 (the $i = 3$ status), never in
  Sections 2 to 5.
- (Sweep) The Stage 2 sweep verified $\gcd(V_i(n), C(n,j)) > 1$ for every
  triple with $n \le 10000$ (RESULTS.md). The proofs below do not depend on
  the sweep except where explicitly noted as an alternative disposal.

**Lemma A1.1 (identity and key lemma).** For $1 \le i < j \le n$,
$$C(n,i)\,C(n-i, j-i) = C(n,j)\,C(j,i).$$
Consequently, if $d \mid C(n,i)$ and $\gcd(d, C(n,j)) = 1$, then
$d \mid C(j,i) = C(j, j-i)$.

*Proof.* Both sides of the identity count the pairs $(A, B)$ with
$A \subseteq B \subseteq [n]$, $|A| = i$, $|B| = j$: choosing $B$ then $A$
gives $C(n,j) C(j,i)$; choosing $A$ then the remaining $j - i$ elements of
$B$ from the $n - i$ elements outside $A$ gives $C(n,i) C(n-i, j-i)$.
For the consequence: $d \mid C(n,i)$ implies
$d \mid C(n,i) C(n-i, j-i) = C(n,j) C(j,i)$, and since
$\gcd(d, C(n,j)) = 1$, Euclid's lemma gives $d \mid C(j,i)$. Finally
$C(j,i) = C(j, j-i)$ by symmetry of the binomial coefficient. $\square$

**Lemma A1.2 (the cases $i \le 2$ have no small part).** For $i = 1$ and
$i = 2$, $U_i(n) = 1$ and $V_i(n) = C(n,i)$ for every $n$.

*Proof.* Every prime is $\ge 1$, and every prime is $\ge 2$. Hence the
product defining $U_i(n)$ is empty for $i \le 2$, and $V_i(n)$ is the full
factorisation of $C(n,i)$. $\square$

## 1. (T1) The case $i = 1$

**Lemma A1.3 (explicit divisor).** For every $n$ and every $1 \le j < n$,
$$\frac{n}{\gcd(n,j)} \;\Big|\; C(n,j).$$

*Proof.* Write $d = \gcd(n,j)$, $n = d n'$, $j = d j'$ with
$\gcd(n', j') = 1$. From $C(n,j) = \frac{n}{j} C(n-1, j-1)$ (the standard
absorption identity: $j \cdot C(n,j) = n \cdot C(n-1,j-1)$, both sides
counting pairs consisting of a $j$-subset of $[n]$ and a distinguished
element of it), clearing denominators with $n/j = n'/j'$ gives
$$j' \cdot C(n,j) = n' \cdot C(n-1, j-1).$$
Hence $j' \mid n' \cdot C(n-1,j-1)$, and since $\gcd(j', n') = 1$,
Euclid's lemma gives $j' \mid C(n-1, j-1)$, say $C(n-1,j-1) = j' t$.
Substituting back gives $C(n,j) = n' t$, so $n' = n/d$ divides $C(n,j)$.
$\square$

**Theorem A1.4 (T1: $i = 1$ is closed).** For all $n$ and all
$1 < j \le n/2$,
$$\gcd\!\big(C(n,1),\, C(n,j)\big) \;\ge\; \frac{n}{\gcd(n,j)} \;\ge\; 2
\;>\; 1.$$
In particular $\gcd(V_1(n), C(n,j)) > 1$: the $i = 1$ case of #699 holds
for all $j$ and all $n$, unconditionally, with no exceptions.

*Proof.* By Lemma A1.2, $V_1(n) = C(n,1) = n$, so the claim is
$\gcd(n, C(n,j)) > 1$. By Lemma A1.3, $n' := n/\gcd(n,j)$ divides both
$n$ and $C(n,j)$, hence divides their gcd. Since
$\gcd(n,j) \le j \le n/2$, we have $n' \ge 2$. Any prime divisor of $n'$
is a prime (hence $\ge 1$) dividing both $C(n,1)$ and $C(n,j)$.
No EEES78 input, no key lemma hypothesis, and no finiteness reduction is
used. $\square$

*Remark.* Lemma A1.3 is stronger than the bare claim: it holds for every
$1 \le j < n$ (not only $j \le n/2$), it names a divisor of the gcd rather
than only a prime, and it shows the configuration $\gcd(n, C(n,j)) = 1$
never occurs in range. The alternative route of S8 (key lemma with
$d = n$, forcing $n \mid j$, contradicting $0 < j < n$) is the same
conclusion in weaker form; the proof above, following S6 Section 2.2, is
the one retained. Independent check by this prover: $n/\gcd(n,j) \mid
C(n,j)$ for all $n < 200$, all $j \le n/2$, zero failures.

## 2. (T2) The case $i = 2$

**Theorem A1.5 (T2: $i = 2$ is closed).** For all $n$ and all
$2 < j \le n/2$,
$$\gcd\!\big(C(n,2),\, C(n,j)\big) > 1.$$
Since every prime is $\ge 2$, this is exactly
$\gcd(V_2(n), C(n,j)) > 1$: the $i = 2$ case of #699 holds for all $j$
and all $n$, unconditionally, with no exceptions.

*Proof, with the negation made exact.* By Lemma A1.2, $V_2(n) = C(n,2)$,
because the set of primes $\ge 2$ is the set of all primes. The $i = 2$
case of #699 is therefore the statement $\gcd(C(n,2), C(n,j)) > 1$, and
its negation is precisely $\gcd(C(n,2), C(n,j)) = 1$; there is no residual
distinction between "a common prime" and "a common prime $\ge i$", since
any prime divisor of the gcd is automatically $\ge 2 = i$. Suppose, for
contradiction, that $\gcd(C(n,2), C(n,j)) = 1$. Apply Lemma A1.1 with
$d = C(n,2)$: we have $d \mid C(n,2)$ trivially and
$\gcd(d, C(n,j)) = 1$ by assumption, so $d \mid C(j,2)$, that is
$C(n,2) \mid C(j,2)$. But $j \ge 3$ gives $C(j,2) = j(j-1)/2 > 0$, and
$j < n$ (since $j \le n/2 < n$) gives $C(j,2) < C(n,2)$, because
$x \mapsto x(x-1)/2$ is strictly increasing for $x \ge 2$. A positive
integer cannot divide a strictly smaller positive integer, contradiction.
Hence $\gcd(C(n,2), C(n,j)) > 1$. No EEES78 input is used. $\square$

*Remark (why the argument stops at $i = 2$).* For $i \ge 3$ the prime $2$
leaves $V_i(n)$, so $V_i(n)$ is a proper divisor of $C(n,i)$, Lemma A1.1
applied to $d = V_i(n)$ yields only $V_i(n) \le C(j, j-i)$, and size alone
no longer contradicts $n > j$. This is the exact point where EEES78-type
input becomes necessary. Independent check by this prover:
$\gcd(C(n,2), C(n,j)) > 1$ for all $n < 200$, $3 \le j \le n/2$, zero
failures.

## 3. (T3) The boundary family $j = \lfloor 3i/2 \rfloor + 1$

Throughout this section $d = j - i$ and the pair $(i,j)$ is the first open
diagonal $j = \lfloor 3i/2 \rfloor + 1$ (so $j > 3i/2$: this diagonal lies
strictly outside the closed region).

**Lemma A1.6 (square reduction).** Let $(n,i,j)$ be a counterexample with
$(n,i)$ not an EEES78 exception pair. Then
$$C(n,i) \;<\; V_i(n)^2 \;\le\; C(j, d)^2,
\qquad\text{i.e.}\qquad C(n,i) < C(j, j-i)^2.$$

*Proof.* Since $(n,i,j)$ is a counterexample,
$\gcd(V_i(n), C(n,j)) = 1$, and $V_i(n) \mid C(n,i)$ by definition, so
Lemma A1.1 with $d = V_i(n)$ gives $V_i(n) \mid C(j,i) = C(j,d)$, hence
$V_i(n) \le C(j,d)$ (both sides positive). EEES78 at the non-exception
pair $(n,i)$ gives $V_i(n)^2 > C(n,i)$. Chaining:
$C(n,i) < V_i(n)^2 \le C(j,d)^2$. $\square$

Note this is strictly stronger than the Phase 0 reduction
$C(n,i) < C(2j, 2d)$: Phase 0 inserts the Vandermonde inequality
$C(j,d)^2 < C(2j, 2d)$ after exactly this step, weakening the bound.
Lemma A1.6 keeps the square.

**Lemma A1.7 (pair closure criterion).** Fix $(i,j)$ with $i < j$. If
$$C(2j, i) \;\ge\; C(j, d)^2, \tag{$\ast$}$$
then there is no counterexample $(n,i,j)$ with $n \ge 2j$ and $(n,i)$
a non-exception pair.

*Proof.* For fixed $i$, $C(n,i)$ is strictly increasing in $n \ge i$,
since $C(n+1,i)/C(n,i) = (n+1)/(n+1-i) > 1$. So any counterexample with
$n \ge 2j$ and $(n,i)$ non-exception would satisfy, by Lemma A1.6,
$C(j,d)^2 > C(n,i) \ge C(2j,i) \ge C(j,d)^2$ by $(\ast)$, a contradiction.
$\square$

So the whole task for the boundary family is: verify $(\ast)$ on the
family, then dispose of (a) the finitely many $i$ where the ratio argument
for $(\ast)$ does not apply, and (b) the EEES78 exception triples inside
the family (values of $n$ where Lemma A1.6 is unavailable). Both are done
below; item (b) is where a source claim needed correction (Lemma A1.10).

Parametrisation of the family. If $i = 2m+1$ is odd ($m \ge 1$, i.e.
$i \ge 3$), then $j = \lfloor 3(2m+1)/2 \rfloor + 1 = (3m+1) + 1 = 3m+2$,
$d = m+1$, $2j = 6m+4$. If $i = 2m$ is even ($m \ge 1$), then
$j = 3m + 1$, $d = m+1$, $2j = 6m+2$.

**Lemma A1.8 (odd case: $(\ast)$ holds for all odd $i \ge 3$).** For
$m \ge 1$ let
$$R_m = \frac{C(6m+4,\, 2m+1)}{C(3m+2,\, m+1)^2}.$$
Then $R_1 = 6/5$ and $R_{m+1}/R_m > 1$ for all $m \ge 1$; hence
$R_m > 1$ for all $m \ge 1$, which is $(\ast)$ for $(i,j) = (2m+1, 3m+2)$.

*Proof.* $R_1 = C(10,3)/C(5,2)^2 = 120/100 = 6/5$. For the step, write
each binomial ratio as a product of linear factors in $m$:
$$\frac{C(6m+10, 2m+3)}{C(6m+4, 2m+1)}
= \frac{\prod_{k=5}^{10}(6m+k)}{(2m+2)(2m+3)(4m+4)(4m+5)(4m+6)(4m+7)},$$
$$\frac{C(3m+5, m+2)}{C(3m+2, m+1)}
= \frac{(3m+3)(3m+4)(3m+5)}{(m+2)(2m+2)(2m+3)},$$
(the first from $C(N+6, K+2)/C(N,K)$ with $N = 6m+4$, $K = 2m+1$,
$N - K = 4m+3$; the second from $C(N+3, K+1)/C(N,K)$ with $N = 3m+2$,
$K = m+1$, $N - K = 2m+1$). Since
$R_{m+1}/R_m$ is the first ratio divided by the square of the second,
cancelling common factors gives the closed form
$$\frac{R_{m+1}}{R_m} =
\frac{2(m+2)^2(2m+3)(6m+5)(6m+7)}
     {(m+1)(3m+4)(3m+5)(4m+5)(4m+7)},$$
and subtracting 1 and combining over the common denominator gives the
polynomial identity
$$\frac{R_{m+1}}{R_m} - 1 =
\frac{72m^4 + 369m^3 + 678m^2 + 523m + 140}
     {(m+1)(3m+4)(3m+5)(4m+5)(4m+7)}.$$
Both identities are identities of rational functions in $m$; this prover
verified them by exact symbolic simplification (SymPy `cancel`/`together`
on the product expressions above: the difference from the stated closed
forms is exactly $0$, and the numerator of $R_{m+1}/R_m - 1$ is exactly
the displayed polynomial, with no hidden common factor). The numerator
has all coefficients positive and the denominator is positive for
$m \ge 1$ (indeed for $m \ge 0$), so $R_{m+1}/R_m > 1$ for all $m \ge 1$.
Induction from $R_1 = 6/5 > 1$ gives $R_m > 1$ for all $m \ge 1$.
$\square$

**Lemma A1.9 (even case: $(\ast)$ holds for all even $i \ge 10$).** For
$m \ge 1$ let
$$R_m = \frac{C(6m+2,\, 2m)}{C(3m+1,\, m+1)^2}.$$
Then $R_{m+1}/R_m > 1$ for all $m \ge 1$, and
$R_5 = 64512240/64128064 > 1$; hence $R_m > 1$ for all $m \ge 5$, which
is $(\ast)$ for $(i,j) = (2m, 3m+1)$ with $i = 2m \ge 10$.

*Proof.* As in Lemma A1.8, with $C(N+6,K+2)/C(N,K)$ at
$N = 6m+2$, $K = 2m$, $N - K = 4m+2$, and $C(N+3,K+1)/C(N,K)$ at
$N = 3m+1$, $K = m+1$, $N - K = 2m$:
$$\frac{R_{m+1}}{R_m} =
\frac{2(m+2)^2(2m+1)^2(6m+5)(6m+7)}
     {(m+1)(2m+3)(3m+2)(3m+4)(4m+3)(4m+5)},$$
$$\frac{R_{m+1}}{R_m} - 1 =
\frac{144m^5 + 546m^4 + 617m^3 + 91m^2 - 202m - 80}
     {(m+1)(2m+3)(3m+2)(3m+4)(4m+3)(4m+5)},$$
again verified by this prover as exact rational identities (symbolic
simplification of the product expressions; difference exactly $0$).
The denominator is positive for $m \ge 1$. The numerator is positive for
$m \ge 1$: the terms $144m^5 + 617m^3 + 91m^2$ are positive, and
$546m^4 \ge 546m \ge 202m + 80$ for $m \ge 1$ (since $344m \ge 80$),
so $546m^4 - 202m - 80 \ge 0$, with the remaining terms strictly
positive. Hence $R_m$ is strictly increasing in $m$. Finally
$R_5 = C(32,10)/C(16,6)^2 = 64512240/8008^2 = 64512240/64128064 > 1$
(exact integers, recomputed). Therefore $R_m > 1$ for all $m \ge 5$.
$\square$

*Remark (these pairs are genuinely new).* On the same family, Phase 0's
reduction does not close any pair: in the odd case
$C(2j, 2d)/C(2j,i) = (4m+3)/(2m+2) > 1$ (one step of the ratio
$C(N,K+1)/C(N,K) = (N-K)/(K+1)$ at $N = 6m+4$, $K = 2m+1$), and in the
even case $C(2j,2d)/C(2j,i) = \frac{(4m+2)(4m+1)}{(2m+1)(2m+2)} > 1$
(two such steps). So $C(2j,i) < C(2j,2d)$ throughout the family, the
Phase 0 interval $[2j, N(i,j)]$ is nonempty, and the closure above comes
entirely from keeping the square in Lemma A1.6.

**Lemma A1.10 (EEES78 exceptions inside the family: there are exactly
two, not one).** Let $(i, j)$ be a boundary-family pair,
$j = \lfloor 3i/2 \rfloor + 1$. The values $n \ge 2j$ at which $(n,i)$ is
an EEES78 exception pair are: none, except $n = 30$ for $(i,j) = (7,11)$
and $n = 56$ for $(i,j) = (13,20)$. Both exceptional triples are not
counterexamples, by direct computation:
$$\gcd\big(V_7(30),\, C(30,11)\big) = 377 > 1,
\qquad
\gcd\big(V_{13}(56),\, C(56,20)\big) = 57293 > 1.$$

*Proof.* Group the 12 exception pairs by $i$ and compare each $n_0$ with
$2j$ for the boundary $j$ at that $i$ (all values recomputed exactly):

| $i$ | boundary $j$ | $2j$ | exception $n_0$ with this $i$ | $n_0 \ge 2j$? |
|---|---|---|---|---|
| 3 | 5 | 10 | 8 | no |
| 4 | 7 | 14 | 9 | no |
| 5 | 8 | 16 | 10, 12 | no |
| 7 | 11 | 22 | 21, **30** | **30 only** |
| 8 | 13 | 26 | 21 | no (and $13 > 21/2$: no triple) |
| 13 | 20 | 40 | 33, 36, **56** | **56 only** |
| 14 | 22 | 44 | 33 | no |
| 17 | 26 | 52 | 36 | no |

All other $i$ have no exception pairs. (Sanity: each listed pair is a
genuine exception, $V_i(n_0)^2 \le C(n_0,i)$; e.g. $V_7(30) = 377$,
$377^2 = 142129 \le 2035800 = C(30,7)$; $V_{13}(56) = 973981$,
$973981^2 = 948638988361 \le 1889912732400 = C(56,13)$.) It remains to
check the two surviving triples directly. Exact computation (Python
standard library, $V_i(n)$ obtained from $C(n,i)$ by dividing out all
prime factors $< i$):

- $(n,i,j) = (30,7,11)$: $V_7(30) = 377 = 13 \cdot 29$,
  $C(30,11) = 54627300$, and $377 \mid C(30,11)$ (quotient $144900$), so
  $\gcd = 377 > 1$. In fact the whole of $V_7(30)$ divides $C(30,11)$.
- $(n,i,j) = (56,13,20)$: $V_{13}(56) = 973981 = 17 \cdot 23 \cdot 47
  \cdot 53$, $C(56,20) = 785613562163430$, and
  $\gcd = 57293 = 23 \cdot 47 \cdot 53 > 1$.

Both triples satisfy the conjecture. $\square$

**Correction to S5 (flagged loudly).** S5 (Section 4 proviso, repeated in
its Section 8) asserts that $(56,13,20)$ is "the only EEES78 exception
pair falling inside this family with $n \ge 2j$". **That assertion is
false.** The pair $(30,7)$ is an EEES78 exception, $i = 7$ has boundary
$j = \lfloor 21/2 \rfloor + 1 = 11$, and $30 \ge 22 = 2j$, so the triple
$(30,7,11)$ falls inside the family exactly as $(56,13,20)$ does; S5
overlooked it (the near miss $(21,7)$, with $21 < 22$, may have masked
it). The error does not sink S5's Theorem 5: the missed triple is
discharged by the direct computation above (and was in fact already
covered by the Stage 2 checker's blanket discharge of all 41 exception
triples, RESULTS.md), so the family closure stands with **two**
exceptional triples discharged directly instead of one. But any citation
of S5's proviso must be corrected to Lemma A1.10's statement.

**Lemma A1.11 (the small $i$ the ratio argument does not cover).** The
ratio arguments of Lemmas A1.8 and A1.9 cover odd $i \ge 3$ and even
$i \ge 10$. The remaining boundary-family pairs are exactly:
$(i,j) = (1,2)$, $(2,4)$, $(4,7)$, $(6,10)$, $(8,13)$. The first two are
closed by Theorems A1.4 and A1.5 (all $j$, all $n$). For the last three,
$(\ast)$ **fails** at $n = 2j$:
$$C(14,4) = 1001 < 1225 = C(7,3)^2,\quad
C(20,6) = 38760 < 44100 = C(10,4)^2,\quad
C(26,8) = 1562275 < 1656369 = C(13,5)^2,$$
so the square reduction cannot close them. They are closed instead by
the Phase 0 reduction plus a finite direct check. The Phase 0 bounds
$N(i,j) = \max\{n : C(n,i) < C(2j, 2(j-i))\}$ are
$$N(4,7) = 17, \qquad N(6,10) = 23, \qquad N(8,13) = 29$$
(exact computation), so by Phase 0 any counterexample at these pairs has
$2j \le n \le N(i,j)$ with $(n,i)$ non-exception. Direct exact
computation of $\gcd(V_i(n), C(n,j))$ on those intervals gives:

| $(i,j)$ | $n$ | gcd |
|---|---|---|
| $(4,7)$ | 14, 15, 16, 17 | 143, 65, 65, 17 |
| $(6,10)$ | 20, 21, 22, 23 | 323, 2261, 24871, 33649 |
| $(8,13)$ | 26, 27, 28, 29 | 437, 23, 23, 667 |

all $> 1$. Finally, no EEES78 exception triple exists at these pairs:
for $i = 4$ the only exception is $(9,4)$ and $7 > 9/2$; for $i = 6$
there is no exception pair; for $i = 8$ the only exception is $(21,8)$
and $13 > 21/2$. Hence no counterexample exists at $(4,7)$, $(6,10)$,
$(8,13)$ for any $n$. (Consistency note: all three bounds satisfy
$N(i,j) \le 10000$, so these pairs are also among the Stage 2 sweep's
fully cleared pairs; the direct check above makes the disposal
independent of the sweep.) $\square$

**Theorem A1.12 (T3: the boundary family is closed).** For every
$i \ge 1$, the pair $(i, j)$ with $j = \lfloor 3i/2 \rfloor + 1$ admits
no counterexample for any $n$: for all $n \ge 2j$,
$\gcd(V_i(n), C(n,j)) > 1$.

*Proof.* Split by $i$. Odd $i \ge 3$: $(\ast)$ holds by Lemma A1.8, so
Lemma A1.7 excludes counterexamples at every non-exception $n \ge 2j$;
by Lemma A1.10 the only possible exception value is $n = 30$ at
$i = 7$ and $n = 56$ at $i = 13$, both checked directly there, and all
other odd $i$ have no exception value $\ge 2j$ at all. Even $i \ge 10$:
identical, using Lemma A1.9 for $(\ast)$ and Lemma A1.10 (no exception
value $\ge 2j$ occurs at any even $i \ge 10$ in the family: the table's
even rows are $i = 4, 8, 14$, with $n_0 < 2j$). Remaining
$i \in \{1, 2, 4, 6, 8\}$: Lemma A1.11. $\square$

## 4. (T4) The exact status of $i = 3$

This section states precisely what is proved for $i = 3$, proves the two
unconditional closures $(3,5)$ and $(3,6)$ in full, and isolates the exact
remaining obstruction as a formal statement. **$i = 3$ is not closed in
general, and nothing below should be read as claiming otherwise.**

What is already settled for $i = 3$:

1. $j = 4$: this is the closed region, since $j \le 3i/2$ means
   $j \le 9/2$, i.e. $j \le 4$ for integer $j$; with $j > i = 3$ the only
   pair is $(3,4)$, settled for all $n$ by the closed-region input of
   Section 0.
2. $(3,5)$: $j = 5 = \lfloor 9/2 \rfloor + 1$ is the boundary family at
   $i = 3$, closed for all $n$ by Theorem A1.12 (the $m = 1$ case of
   Lemma A1.8: $C(10,3) = 120 \ge 100 = C(5,2)^2$; no exception value,
   since the only $i = 3$ exception is $(8,3)$ with $8 < 10$).
3. $(3,6)$: closed for all $n$ by Theorem A1.14 below (S1, Theorem B).
   Note $(\ast)$ fails for $(3,6)$: $C(12,3) = 220 < 400 = C(6,3)^2$, so
   the square reduction does **not** close $(3,6)$; the Kummer bound
   does.
4. Fixed pairs beyond: the Stage 2 sweep plus the Phase 0 reduction fully
   clear $(3,j)$ for all $j \le 112$, and S1's Kummer reduction raises
   this to $j \le 465$ (S1, Theorem D). These are per-pair closures for
   fixed $j$, not a closure of $i = 3$ for all $j$.
5. Every triple with $n \le 10000$ is verified (sweep). The open content
   of $i = 3$ is: pairs $(3,j)$ with $j$ large and triples with
   $n > 10000$.

**Lemma A1.13 (prime-power bound, $i = 3$ form).** Let
$u = U_3(n) = 2^{v_2(C(n,3))}$ be the small part of $C(n,3)$. Then
$$u \;\le\; U^\sharp(n) := 2^{\lfloor \log_2 n \rfloor} \;\le\; n.$$

*Proof.* Legendre's formula gives
$v_2(C(n,3)) = \sum_{k \ge 1}
\big(\lfloor n/2^k \rfloor - \lfloor 3/2^k \rfloor -
\lfloor (n-3)/2^k \rfloor\big)$.
Each summand is $0$ or $1$ (it equals
$\lfloor x + y \rfloor - \lfloor x \rfloor - \lfloor y \rfloor$ for
$x = 3/2^k$, $y = (n-3)/2^k$), and summands with $2^k > n$ vanish, so
$v_2(C(n,3)) \le \#\{k : 2^k \le n\} = \lfloor \log_2 n \rfloor$.
$\square$

**Theorem A1.14 ($(3,5)$ and $(3,6)$ closed unconditionally; S1 Theorem B
for $i = 3$).** There is no counterexample $(n, 3, 5)$ or $(n, 3, 6)$ for
any $n$. The proof uses no EEES78 input.

*Proof.* Let $(n,3,j)$ be a counterexample, $j \in \{5,6\}$, $n \ge 2j$.
By Lemma A1.1 with $d = V_3(n)$,
$V_3(n) \mid C(j, j-3)$, so
$C(n,3) = u \cdot V_3(n) \le u \cdot C(j, j-3) \le U^\sharp(n) \cdot
C(j, j-3)$ by Lemma A1.13. Set $G(n) = C(n,3)/U^\sharp(n)$ and
$F(n) = C(n,3)/n = (n-1)(n-2)/6$. Since $U^\sharp(n) \le n$,
$G(n) \ge F(n)$; and $F$ is strictly increasing for $n \ge 3$ (it is a
quadratic with positive leading coefficient and vertex below $3$; directly,
$F(n+1) - F(n) = (2n-2)/6 > 0$). A counterexample therefore requires
$G(n) \le C(j, j-3)$.

Case $j = 5$: $C(5,2) = 10$. For all $n \ge 10 = 2j$,
$G(n) \ge F(n) \ge F(10) = 12 > 10$. Contradiction.

Case $j = 6$: $C(6,3) = 20$. On $12 \le n \le 15$, $U^\sharp(n) = 8$ is
constant while $C(n,3)$ is strictly increasing in $n$, so
$G(n) \ge G(12) = 220/8 = 27.5 > 20$. For $n \ge 16$,
$G(n) \ge F(n) \ge F(16) = 560/16 = 35 > 20$. Contradiction in both
ranges. $\square$

*Remark.* The next pair shows the size method's exact edge:
$\mathrm{Bad}^\sharp(3,7) := \{n \ge 14 : C(n,3) \le U^\sharp(n) C(7,4)\}
= \{16\}$, a singleton, with equality $C(16,3) = 560 = 16 \cdot 35$ at
$n = 16$ (recomputed by this prover; the set is empty on $[14, 200)$
except for $16$). The triple itself is fine:
$\gcd(V_3(16), C(16,7)) = \gcd(35, 11440) = 5 > 1$, and the pair $(3,7)$
is fully cleared by item 4 above. But no pure size argument of this shape
closes $(3,7)$, let alone all $(3,j)$.

**Lemma A1.15 (low-digit lemma for $i = 3$; S8, Lemma 3, reproved).**
Let $q = p^a$ exactly divide $m = n - r$ for some $r \in \{0,1,2\}$,
where either (a) $p \ge 5$, or (b) $p = 3$ and $a \ge 2$. Then
$p \mid C(n,3)$, and
$$p \nmid C(n,j) \;\Longrightarrow\; j \bmod q \;\le\; r.$$
Equivalently, if $j \bmod q > r$ then $p$ is a common prime $\ge 3$ of
$C(n,3)$ and $C(n,j)$, and $(n,3,j)$ is not a counterexample.

*Proof.* First, $p \mid C(n,3)$. In case (a), $p \nmid 6$ and $p$ divides
the product $n(n-1)(n-2)$ (it divides $m$); $p$ divides only one of the
three factors, since two of them differ by at most $2 < p$; hence
$v_p(C(n,3)) = v_p(n(n-1)(n-2)) \ge a \ge 1$. In case (b), exactly one of
three consecutive integers is divisible by $3$, namely $m$, and
$v_3(C(n,3)) = a - v_3(6) = a - 1 \ge 1$. Second, the digit claim. Since
$q \mid n - r$ and $0 \le r \le 2 < p$, we have $n \bmod q = r$, whose
base-$p$ expansion padded to $a$ digits is: digit $0$ equal to $r$,
digits $1, \dots, a-1$ equal to $0$. If $p \nmid C(n,j)$ then by Kummer's
theorem $j$ is digitwise $\le n$ in base $p$ (no carry when adding $j$
and $n - j$), so digit $0$ of $j$ is $\le r$ and digits $1, \dots, a-1$
of $j$ are $0$, which says exactly $j \bmod q \le r$. $\square$

**Definition (the system (LD3)).** Call a prime power $q = p^a \Vert m$
(for $m \in \{n, n-1, n-2\}$) **relevant** if $p \ge 5$ (any $a \ge 1$)
or $p = 3$ with $a \ge 2$. Let $R(m)$ be the product of the relevant prime
powers dividing $m$ (the factors are pairwise coprime, also across the
three values of $m$, since a prime $p \ge 3$ divides at most one of
$n, n-1, n-2$). The pair $(n,j)$ **satisfies (LD3)** if for every
$m = n - r$ and every relevant $q \mid R(m)$,
$$j \bmod q \;\in\; \{0, 1, \dots, r\},$$
equivalently the factorisation conditions: $R(n) \mid j$;
$R(n-1) = X_0 X_1$ with $X_0 \mid j$, $X_1 \mid j - 1$;
$R(n-2) = Y_0 Y_1 Y_2$ with $Y_s \mid j - s$ for $s = 0, 1, 2$
(the splitting form follows because the relevant prime powers of $m$
are pairwise coprime, so each must divide entirely one of the allowed
$j - s$).

**Proposition A1.16 (proved necessary conditions for an $i = 3$
counterexample).** If $(n,3,j)$ is a counterexample ($3 < j \le n/2$),
then all of the following hold.

(i) **(LD3) holds for $(n,j)$.** (Immediate from Lemma A1.15: failure
means no prime $\ge 3$ of $C(n,3)$ divides $C(n,j)$; in particular for
each relevant $q$ the prime $p$ of Lemma A1.15 does not divide $C(n,j)$,
forcing $j \bmod q \le r$.)

(ii) **(N1)** $\gcd(C(n,2), C(n,j)) = 2^a 3^b$ for some $a, b \ge 0$.
(Indeed, if a prime $p \ge 5$ divided both $C(n,2)$ and $C(n,j)$, then
$p \mid n(n-1)$ since $p$ is odd and $C(n,2) = n(n-1)/2$; as in Lemma
A1.15(a), $p \mid C(n,3)$; so $p$ would be a common prime $\ge 3$ of
$C(n,3)$ and $C(n,j)$, contradicting failure.)

(iii) **(N2)** $V_3(n) \mid C(j,3)$, in particular $V_3(n) \le C(j,3)$.
(Lemma A1.1 with $d = V_3(n)$.)

(iv) **Odd-top rigidity.** If $n$ is odd and $n > 9$, then
$v_3(n) = 1$ and $j = n/3$ exactly. If $n$ is even, then with
$m = n - 1$ odd, $R(n-1) \in \{n-1, (n-1)/3\}$ must split as in the
Definition with each factor $\le j \le n/2$; in particular if
$R(n-1) = n - 1$ (e.g. $n - 1$ prime) the triple is closed.
(For odd $m$, every prime power of $m$ is relevant except a single
factor $3$ when $v_3(m) = 1$, so $R(m) = m$ if $3 \nmid m$ or $9 \mid m$,
and $R(m) = m/3$ if $v_3(m) = 1$. For $n$ odd, (LD3) at $r = 0$ gives
$R(n) \mid j$; $R(n) = n$ would force $n \mid j$, impossible for
$0 < j \le n/2 < n$; hence $v_3(n) = 1$ and $n/3 \mid j$, and the only
multiple of $n/3$ in $(3, n/2]$ (for $n > 9$) is $n/3$ itself, since
$2n/3 > n/2$. The even case is the $r = 1$ clause of the Definition
applied to the odd number $n - 1$.)

Furthermore (LD3) is a **necessary, not sufficient**, condition: it uses
only the lowest $a$ base-$p$ digits in Lemma A1.15, and a pair satisfying
(LD3) could still be saved by higher digits.

**Statement H3 (the exact remaining obstruction for $i = 3$).**

> **(H3)** There is no pair $(n, j)$ with $3 < j \le n/2$ satisfying
> (LD3): that is, for every such $(n,j)$ there exist $r \in \{0,1,2\}$
> and a relevant prime power $q = p^a \Vert (n - r)$ ($p \ge 5$, or
> $p = 3$ with $a \ge 2$) such that $j \bmod q > r$.

By Proposition A1.16(i), a proof of (H3) would close $i = 3$ completely
(for all $j$ and all $n$). Conversely, (H3) is exactly the obstruction
*for the low-digit method*: it is the single statement whose proof is
missing. This prover does **not** prove (H3), and therefore does **not**
claim $i = 3$ is closed. Where the difficulty sits, precisely: by
Proposition A1.16(iv), an (LD3) solution with $n$ odd is pinned to
$v_3(n) = 1$, $j = n/3$, subject to the $r = 1, 2$ clauses; an (LD3)
solution with $n$ even requires $R(n-1)$ (and the relevant part of
$n - 2$) to **split** across $j, j-1$ (resp. $j, j-1, j-2$), each prime
power factor individually $\le j$. When $R(m)$ has two or more prime
power factors, the factors can be distributed among the allowed targets
in several ways, and no size bound known to this prover (or recorded in
S8, Section 3.5, where the same point is identified as the stopping
place) excludes all distributions simultaneously. A proof of (H3) must
either rule out these splitting configurations in general, or close any
(LD3) solutions that do exist using the higher-digit Kummer conditions
beyond Lemma A1.15.

**Computational status of (H3), stated exactly.** S8 reports that the
criterion of Lemma A1.15 fires for every one of the $6{,}235{,}009$
triples with $6 \le n \le 5000$, $4 \le j \le n/2$ (their computation),
i.e. (LD3) has no solution with $n \le 5000$. This prover independently
recomputed the (LD3) survivor set with a separate implementation
(smallest-prime-factor sieve, exact prime-power factorisation of
$n, n-1, n-2$, direct test of $j \bmod q \le r$ for all relevant $q$)
and confirms: **(LD3) has no solution with $n \le 2000$**, and dropping
the $p = 3$ clause, the $\ge 5$ system has exactly six solutions with
$n \le 2000$, namely
$$(10,5),\ (28,14),\ (82,41),\ (244,122),\ (730,365),\ (162,70),$$
agreeing exactly with S8's list. The first five are $n = 3^a + 1$,
$j = n/2$ ($a = 2, \dots, 6$), each killed by the $3$-clause:
$q = 3^a \mid n - 1$ ($r = 1$) and $j \bmod 3^a = (3^a+1)/2 > 1$, so
$3 \mid C(n,j)$ and $3 \mid C(n,3)$ (this in fact proves the whole family
$n = 3^a + 1$, $j = n/2$, $a \ge 2$, at $i = 3$). The sixth is killed by
$q = 81 \mid 162$ ($r = 0$) with $70 \bmod 81 = 70 > 0$. These are finite
computations about (LD3), not a proof of (H3): for $n > 5000$ the system
is untested by either computation, and for all $n$ it is unproved.

**Theorem A1.17 (T4: exact $i = 3$ status).** For $i = 3$ the following
is proved, and no more is claimed:

(a) For every $n$: the pairs $(3,4)$ (closed region), $(3,5)$
(Theorem A1.12), and $(3,6)$ (Theorem A1.14) admit no counterexample.

(b) For each fixed $j \le 465$, the pair $(3,j)$ admits no counterexample
for any $n$ (Stage 2 sweep plus reductions; items 4 and 5 above).

(c) For any specific triple $(n,3,j)$, the conjecture is proved as soon
as any checkable sufficient condition holds, in particular if some
relevant prime power has $j \bmod q > r$ (Lemma A1.15), if
$\gcd(C(n,2), C(n,j))$ has a prime factor $\ge 5$ (Proposition
A1.16(ii), contrapositive), or if $3 \mid C(n,3)$ and $3 \mid C(n,j)$.

(d) A counterexample with $j \ge 7$ and $n > 10000$ is not excluded by
anything proved here. Its existence is equivalent, for the low-digit
route, to the failure of (H3) in a strong form: any counterexample must
satisfy (LD3) together with (N1) and (N2) (Proposition A1.16), must have
$n$ odd only in the pinned shape $v_3(n) = 1$, $j = n/3$, and must have
$n$ even only with the splitting behaviour of Proposition A1.16(iv).
Closing $i = 3$ in general is exactly the task of proving (H3) (or
finding another argument that excludes (LD3) solutions, or solutions
refined by higher digits). $\square$

## 5. Verification log (all computations by this prover, exact)

- Lemma A1.3 divisibility and Theorem A1.5: brute force, all $n < 200$,
  zero failures.
- Lemma A1.8 and A1.9 ratio identities: exact symbolic verification
  (SymPy rational simplification of the product forms): both step ratios
  equal S5's closed forms exactly; both "minus 1" numerators equal S5's
  polynomials exactly ($72m^4 + 369m^3 + 678m^2 + 523m + 140$ and
  $144m^5 + 546m^4 + 617m^3 + 91m^2 - 202m - 80$), denominators as stated.
  Base values $R_1 = 6/5$, $R_5 = 64512240/64128064$ recomputed in exact
  integers. Spot values: $R_m > 1$ also at even $m = 6$
  ($C(38,12) = 2707475148 > 2538950544 = C(19,7)^2$).
- Lemma A1.10: all 12 exception pairs re-derived as exceptions
  ($V_i(n)^2 \le C(n,i)$ verified for each), boundary comparison table
  computed entry by entry; the two gcds computed exactly:
  $\gcd(V_7(30), C(30,11)) = 377$ with $V_7(30) = 377 = 13 \cdot 29$ and
  $C(30,11) = 54627300 = 377 \cdot 144900$;
  $\gcd(V_{13}(56), C(56,20)) = 57293 = 23 \cdot 47 \cdot 53$ with
  $V_{13}(56) = 973981 = 17 \cdot 23 \cdot 47 \cdot 53$ and
  $C(56,20) = 785613562163430$.
- Lemma A1.11: $N(4,7) = 17$, $N(6,10) = 23$, $N(8,13) = 29$ recomputed
  by exact search; the 12 interval gcds computed exactly (table in
  Lemma A1.11); the three failures of $(\ast)$ computed exactly.
- Theorem A1.14 and the $(3,7)$ remark: $F(10) = 12$, $G(12) = 27.5$,
  $F(16) = 35$ recomputed; $\mathrm{Bad}^\sharp(3,7) = \{16\}$ verified
  on $[14, 200)$; $\gcd(V_3(16), C(16,7)) = \gcd(35, 11440) = 5$.
- (LD3): independent enumeration, $n \le 2000$: full system, zero
  survivors; $\ge 5$-only system, exactly the six pairs listed.
- S8 spot checks used above: $\gcd(C(16,2), C(16,5)) = 24$,
  $\gcd(C(16,3), C(16,5)) = 112$, $\gcd(C(16,2), C(16,6)) = 8$,
  $\gcd(C(16,3), C(16,6)) = 56$ (the persistence discussion), and the
  $n = 50$, $q = 49$ example ($7 \mid C(50,3)$ and $7 \mid C(50,j)$ for
  all $4 \le j \le 25$): all recomputed and correct.

## 6. Audit of source claims

- S6, Section 2 ($i = 1, 2$ theorems, explicit divisor
  $n/\gcd(n,j)$): correct; adopted (Theorems A1.4, A1.5).
- S8, Section 2 ($i = 1, 2$): correct; the $i = 1$ proof there is the
  weaker key-lemma form, superseded here by Lemma A1.3.
- S8, Section 3 (Lemma 3, (LD3), (N1), (N2), the six $\ge 5$-only pairs,
  the odd-top reduction, and the honest statement that (H3) is unproved):
  correct in every particular recomputed, including the exact six-pair
  list and the $n = 3^a + 1$ and $(162,70)$ discharges. S8's computation
  to $n \le 5000$ was not rerun in full; this prover's independent
  computation covers $n \le 2000$ and agrees.
- S1, Theorem B ($(3,5)$, $(3,6)$; $(3,7)$ not closed by size,
  $\mathrm{Bad}^\sharp(3,7) = \{16\}$): correct; adopted and reproved
  (Theorem A1.14).
- S5, Theorem 5 (the ratio identities, $R_1 = 6/5$, $R_5 > 1$, the family
  closure): the mathematics is correct; both identities verified
  symbolically to the letter.
- **S5, EEES78 proviso (Section 4 and Section 8): INCORRECT as stated.**
  It claims $(56,13,20)$ is the sole in-family exception triple; the
  triple $(30,7,11)$ is a second one (Lemma A1.10). The family theorem
  survives because the missed triple is discharged directly
  ($\gcd = 377 > 1$), as recorded in the correction after Lemma A1.10.
  No other S5 claim used here was found to fail.

## 7. Summary of what this document proves

- (T1) $i = 1$: closed for all $j$, all $n$ (Theorem A1.4), with the
  explicit bound $\gcd \ge n/\gcd(n,j) \ge 2$.
- (T2) $i = 2$: closed for all $j$, all $n$ (Theorem A1.5).
- (T3) Boundary family $j = \lfloor 3i/2 \rfloor + 1$: closed for all
  $i$, all $n$ (Theorem A1.12), via the square reduction (Lemma A1.6),
  exact step ratios (Lemmas A1.8, A1.9), direct disposal of
  $i \in \{4,6,8\}$ (Lemma A1.11; $i \in \{1,2\}$ by T1, T2), and direct
  discharge of the **two** in-family EEES78 exception triples
  $(30,7,11)$ and $(56,13,20)$ (Lemma A1.10).
- (T4) $i = 3$: **not closed in general.** Proved: $(3,4)$, $(3,5)$,
  $(3,6)$ for all $n$; per-pair closures to $j \le 465$; the reduction of
  any counterexample to the system (LD3) with the additional conditions
  (N1), (N2) and the odd-top rigidity (Proposition A1.16). The exact
  remaining obstruction is Statement **(H3)**: prove that (LD3) has no
  solution $(n,j)$ with $3 < j \le n/2$; the unresolved core is the
  splitting of $R(n-1)$ (and the relevant part of $n-2$) across
  $j, j-1, j-2$ when $R$ has several prime power factors.
