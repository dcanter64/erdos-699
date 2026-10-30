# P-A2: Small-$i$ closures of Erdős #699: $i=1$, $i=2$, the boundary family $j=\lfloor 3i/2\rfloor+1$, and the exact status of $i=3$

**Prover A2 (independent).** This document was written independently of the
other prover's document. The inputs are the strategy papers S8 (§§2–3),
S6 (§2), S5 (boundary family and square reduction), S1 (Theorem B), and the
Phase 0 record (`erdos-699/PHASE0.md`) for the statement of EEES78 and its
exception list. Every computational claim used below was recomputed by this
prover in Python standard library exact arithmetic; the recomputations are
listed in §6. One source claim **fails** and is corrected in §4.3:
S5's assertion that $(56,13,20)$ is the only in-family EEES78 exception
triple is false; $(30,7,11)$ is a second one. Both are discharged by direct
computation here, so the final theorem is unaffected, but any verifier
checking S5's proviso as stated will find it incomplete.

## 0. Setting, notation, and the two external inputs

For integers $1\le i<j\le n/2$ write $C(a,b)=\binom ab$, $d=j-i$, and

$$C(n,i)=u\,v,\qquad
v=V_i(n)=\prod_{p\ge i}p^{v_p(C(n,i))},\qquad
u=\prod_{p<i}p^{v_p(C(n,i))}.$$

Problem #699 for the triple $(n,i,j)$ is the assertion
$\gcd(V_i(n),C(n,j))>1$, equivalently: some prime $p\ge i$ divides both
$C(n,i)$ and $C(n,j)$. A **counterexample** is a triple with
$\gcd(v,C(n,j))=1$.

**External input 1 (EEES78).** If $(n,i)$ is not one of the 12 pairs

$$(8,3),(9,4),(10,5),(12,5),(21,7),(21,8),(30,7),(33,13),(33,14),
(36,13),(36,17),(56,13),$$

then $u<v$, i.e. $v^2>C(n,i)$. (Ecklund–Eggleton–Erdős–Selfridge 1978, as
recorded and independently cross-checked in Phase 0, Item 4.) Every use of
EEES78 below is flagged, and every exception pair that can occur in the
relevant range is discharged by an explicit computation.

**External input 2 (Kummer's criterion, used only in §5).** For a prime
$p$, $v_p(C(n,j))=0$ if and only if $j$ is digitwise $\le n$ in base $p$
(no carry when adding $j$ and $n-j$ in base $p$).

Everything else is proved here.

**Lemma A2.1 (identity and key lemma).**
For $1\le i<j\le n$,
$$C(n,i)\,C(n-i,j-i)=C(n,j)\,C(j,i).$$
Hence, if $d\mid C(n,i)$ and $\gcd(d,C(n,j))=1$, then $d\mid C(j,i)=C(j,d)$.

*Proof.* Both sides of the identity count the ways to choose an $i$-subset
of an $n$-set and then a disjoint $(j-i)$-subset: the left side directly;
the right side by first choosing the union, a $j$-subset, and then the
$i$-subset inside it. For the consequence: $d\mid C(n,i)$ gives
$d\mid C(n,i)C(n-i,j-i)=C(n,j)C(j,i)$, and Euclid's lemma with
$\gcd(d,C(n,j))=1$ gives $d\mid C(j,i)$. $\square$

**Lemma A2.2 (the two Phase 0 reductions).**
Let $(n,i,j)$ be a counterexample with $(n,i)$ EEES78-non-exceptional.
Then

(a) (square reduction) $C(n,i)<C(j,d)^2$;

(b) (Phase 0 reduction) $C(n,i)<C(2j,2d)$.

*Proof.* Apply Lemma A2.1 with $d_0=v$: $v\mid C(n,i)$ by definition and
$\gcd(v,C(n,j))=1$ by the counterexample assumption, so $v\mid C(j,d)$ and
$v\le C(j,d)$ (both sides positive). EEES78 gives $v^2>C(n,i)$, proving (a).
For (b), Vandermonde's identity gives
$C(2j,2d)=\sum_k C(j,k)C(j,2d-k)$, whose $k=d$ term is $C(j,d)^2$; the sum
has at least three positive terms (the indices $k$ with
$0\le k\le j$ and $0\le 2d-k\le j$ number $2d+1\ge3$ if $2d\le j$, and
$2i+1\ge3$ if $2d>j$), so $C(j,d)^2<C(2j,2d)$, and (a) gives (b). $\square$

**Lemma A2.3 (monotonicity).**
For fixed $i\ge1$, $C(n,i)$ is strictly increasing in $n$ for $n\ge i$.
For fixed $j$, $C(2j,i)\le C(n,i)$ whenever $2j\le n$.

*Proof.* $C(n+1,i)/C(n,i)=(n+1)/(n+1-i)>1$ for $n\ge i$. $\square$

## 1. (T1) The case $i=1$: complete

**Lemma A2.4 ($V_1$ and $V_2$ are the whole binomial).**
$V_1(n)=C(n,1)=n$ and $V_2(n)=C(n,2)$.

*Proof.* Every prime is $\ge1$, and every prime is $\ge2$, so the product
defining $V_i(n)$ runs over all prime divisors of $C(n,i)$ for $i=1,2$.
$\square$

**Theorem A2.5 (T1).**
For every $n$ and every $1<j\le n/2$, $\gcd(n,C(n,j))>1$. In fact the
stronger divisibility $n/\gcd(n,j)\mid C(n,j)$ holds, and
$n/\gcd(n,j)\ge2$.

*Proof 1 (via the key lemma, the S8 §2.1 route).* Suppose, for
contradiction, that $\gcd(n,C(n,j))=1$. Apply Lemma A2.1 with
$d=C(n,1)=n$: the hypothesis $d\mid C(n,1)$ is equality, and the hypothesis
$\gcd(d,C(n,j))=1$ is exactly the supposition. The conclusion is
$n\mid C(j,1)=j$. But $0<j\le n/2<n$, and a positive integer strictly
smaller than $n$ is not divisible by $n$: contradiction. Hence
$\gcd(n,C(n,j))>1$. By Lemma A2.4 any prime divisor of this gcd is a prime
$\ge1$ dividing $V_1(n)$ and $C(n,j)$, which is #699 at $i=1$. $\square$

*Proof 2 (the stronger divisor, S6 §2.2, independent check).* Write
$g=\gcd(n,j)$, $n=gn'$, $j=gj'$ with $\gcd(n',j')=1$. From
$C(n,j)=\frac{n}{j}C(n-1,j-1)$ we get $j'\,C(n,j)=n'\,C(n-1,j-1)$. Since
$\gcd(j',n')=1$, Euclid's lemma gives $j'\mid C(n-1,j-1)$, say
$C(n-1,j-1)=j't$; then $C(n,j)=n't$. Hence $n'\mid C(n,j)$ and $n'\mid n$,
so $n'\mid\gcd(n,C(n,j))$. Finally $g\le j\le n/2$, so $n'=n/g\ge2$, and
any prime divisor of $n'$ divides the gcd. $\square$

**Remark A2.6 (reconciling the Kummer discussion in S8's assignment).**
The assignment underlying S8 §2 suggested a digitwise (Kummer) analysis
of when $\gcd(n,C(n,j))=1$ can happen, heading toward a conclusion of the
shape $\operatorname{rad}(n)\mid j$. That analysis is not wrong, but it is
strictly weaker than what the key lemma gives, and no part of it is
needed. The point is exactly the one flagged in the task: the statement
to prove is that *some* prime divides both $n$ and $C(n,j)$, and
$\gcd(n,C(n,j))=1$ is precisely its negation, so the key lemma may be
applied to the *whole* integer $d=n$ at once, not prime by prime. The
conclusion is correspondingly stronger: failure would force $n\mid j$
(the whole of $n$, with all prime powers), not merely
$\operatorname{rad}(n)\mid j$. There is no hidden sub-case: the feared
configuration "$n$ a product of small prime powers, $j$ a multiple of
$\operatorname{rad}(n)$" cannot satisfy the failure hypothesis, because
that hypothesis demands $n\mid j$ and $j<n$. The verification of each
implication is: (i) $d\mid C(n,1)$ is equality; (ii) the coprimality
hypothesis of Lemma A2.1 is the negated conclusion, so Proof 1 is a
legitimate proof by contradiction; (iii) $C(j,1)=j$ by definition;
(iv) $n\nmid j$ because $0<j<n$. It really is that simple, and the
simplicity is explained by Lemma A2.4: at $i=1$ the "large part" $V_1(n)$
is not a proper part at all.

## 2. (T2) The case $i=2$: complete

**Theorem A2.7 (T2).**
For every $n$ and every $2<j\le n/2$, $\gcd(C(n,2),C(n,j))>1$. Hence #699
holds at $i=2$ for all $j$ and all $n$ (any common prime is $\ge2$).

*Proof.* By Lemma A2.4, $V_2(n)=C(n,2)$. Suppose
$\gcd(C(n,2),C(n,j))=1$. Apply Lemma A2.1 with $d=C(n,2)$: then
$C(n,2)\mid C(j,2)$, so $C(n,2)\le C(j,2)$ (both positive). But
$C(x,2)=x(x-1)/2$ is strictly increasing for $x\ge2$ (its ratio at
$x+1$ versus $x$ is $(x+1)/(x-1)>1$), and $2<j<n$ (since $j\le n/2<n$ as
$n\ge2j\ge6$), so $C(j,2)<C(n,2)$: contradiction. $\square$

**Remark A2.8 (why the argument stops at $i=2$).**
For $i\ge3$ the threshold $p\ge i$ discards the prime $2$, $V_i(n)$ is a
proper divisor of $C(n,i)$, and Lemma A2.1 applied to $v$ yields only
$v\mid C(j,i)$, i.e. $v\le C(j,i)$, which size alone cannot contradict:
e.g. for $i=3$ and $n=2^a$, $v_2(C(n,3))=a$, so
$V_3(n)=C(n,3)/n\approx n^2/6$ while $C(j,3)$ at $j\approx n/2$ is
$\approx n^3/48$. This is the exact point where EEES78-type input (a lower
bound on $v$ relative to $C(n,i)$) becomes necessary, and it is what §3
uses.


## 3. (T3) The boundary family $j=\lfloor 3i/2\rfloor+1$

Throughout §3, $j$ is tied to $i$ by $j=\lfloor 3i/2\rfloor+1$, so
$d=j-i=\lfloor i/2\rfloor+1$, and $n\ge2j$. Note $j>3i/2$, so this family
lies strictly outside the established closed region $j\le 3i/2$; and
Phase 0's reduction does **not** close it (Lemma A2.9). The square
reduction (Lemma A2.2(a)) does, once the numerical inequality
$C(2j,i)\ge C(j,d)^2$ is proved on the family (Lemmas A2.11, A2.12) and
the small cases and EEES78 exceptions are disposed of (Lemmas A2.10,
A2.13).

**Lemma A2.9 (Phase 0 non-closure on the family).**
For every $i\ge2$ on the family, $C(2j,i)<C(2j,2d)$; hence the
conclusion $C(n,i)<C(2j,2d)$ of Lemma A2.2(b) is compatible with
$n=2j$ and Phase 0's stated reduction closes no pair of the family.

*Proof.* Odd case $i=2m+1$ ($m\ge1$): $j=3m+2$, $2d=2m+2=i+1$, and
$C(2j,2d)/C(2j,i)=C(6m+4,2m+2)/C(6m+4,2m+1)=(4m+3)/(2m+2)>1$ by the
one-step ratio $C(N,k+1)/C(N,k)=(N-k)/(k+1)$ at $N=6m+4$, $k=2m+1$.
Even case $i=2m$: $j=3m+1$, $2d=2m+2=i+2$, and the two-step ratio is
$\frac{4m+2}{2m+1}\cdot\frac{4m+1}{2m+2}>1$. $\square$

**Lemma A2.10 (pair-closure criterion).**
Fix $(i,j)$ on the family. If $C(2j,i)\ge C(j,d)^2$, then no triple
$(n,i,j)$ with $n\ge2j$ and $(n,i)$ EEES78-non-exceptional is a
counterexample.

*Proof.* A counterexample would satisfy $C(n,i)<C(j,d)^2$ by Lemma
A2.2(a), but $C(n,i)\ge C(2j,i)\ge C(j,d)^2$ by Lemma A2.3:
contradiction. $\square$

**Lemma A2.11 (step ratios, odd case).**
Let $i=2m+1$ with $m\ge1$, so $j=3m+2$ and $d=m+1$, and set
$R_m=C(6m+4,\,2m+1)\,/\,C(3m+2,\,m+1)^2$. Then $R_1=6/5$ and

$$\frac{R_{m+1}}{R_m}=
\frac{2(m+2)^2(2m+3)(6m+5)(6m+7)}
{(m+1)(3m+4)(3m+5)(4m+5)(4m+7)},\qquad
\frac{R_{m+1}}{R_m}-1=
\frac{72m^4+369m^3+678m^2+523m+140}
{(m+1)(3m+4)(3m+5)(4m+5)(4m+7)}>0
\quad(m\ge1).$$

Hence $R_m>1$ for all $m\ge1$, i.e. $C(2j,i)>C(j,d)^2$ for all odd
$i\ge3$ on the family.

*Proof.* $R_1=C(10,3)/C(5,2)^2=120/100=6/5$. The two displayed identities
are identities of rational functions of $m$: writing each of the three
binomial coefficients in $R_{m+1}/R_m$ as a ratio of consecutive-term
products and cancelling gives the first; subtracting $1$ and putting
over the common denominator gives the second, whose numerator and
denominator are the displayed polynomials. (Verifiability: clearing
denominators reduces each identity to a polynomial identity in $m$;
this prover checked the second identity symbolically and the first in
exact rational arithmetic at $m=1,\dots,10,37,100,251$; see §6.)
The numerator of $R_{m+1}/R_m-1$ has all coefficients positive and the
denominator is positive for $m\ge1$, so $R_{m+1}>R_m$ for all $m\ge1$,
and induction from $R_1=6/5$ gives $R_m\ge6/5>1$. $\square$

**Lemma A2.12 (step ratios, even case).**
Let $i=2m$ with $m\ge1$, so $j=3m+1$ and $d=m+1$, and set
$R_m=C(6m+2,\,2m)\,/\,C(3m+1,\,m+1)^2$. Then

$$\frac{R_{m+1}}{R_m}=
\frac{2(m+2)^2(2m+1)^2(6m+5)(6m+7)}
{(m+1)(2m+3)(3m+2)(3m+4)(4m+3)(4m+5)},\qquad
\frac{R_{m+1}}{R_m}-1=
\frac{144m^5+546m^4+617m^3+91m^2-202m-80}
{(m+1)(2m+3)(3m+2)(3m+4)(4m+3)(4m+5)},$$

the numerator of the second fraction is positive for all $m\ge1$, and
$R_5=64512240/64128064=310155/308308>1$. Hence $R_m>1$ for all $m\ge5$,
i.e. $C(2j,i)>C(j,d)^2$ for all even $i\ge10$ on the family. (For
$m=1,2,3,4$ one has $R_m<1$: $R_1=7/9$, $R_2=143/175$, $R_3=646/735$,
$R_4=10925/11583$; these are the pairs $(2,4)$, $(4,7)$, $(6,10)$,
$(8,13)$, disposed of in Lemma A2.14.)

*Proof.* The identities are rational-function identities of the same
kind as in Lemma A2.11 (same verification status; see §6). Positivity
of the numerator for $m\ge1$: every term except $-202m-80$ is positive,
and $546m^4\ge546m\ge202m+80$ for $m\ge1$ (since $344m\ge344>80$), so
the numerator is $\ge144m^5+617m^3+91m^2+(546m-202m-80)>0$. Hence
$R_{m+1}>R_m$ for all $m\ge1$; since the sequence is increasing and
$R_5>1$ (exact values: $C(32,10)=64512240$ and $C(16,6)^2=8008^2=
64128064$), $R_m>1$ for all $m\ge5$. $\square$

### 3.1 The EEES78 exceptions inside the family: a source claim fails

**Lemma A2.13 (in-family exception triples: exactly two, both closed
directly).**
Let $(n_0,i_0)$ be one of the 12 EEES78 exception pairs and let
$j_0=\lfloor3i_0/2\rfloor+1$. The condition $n_0\ge2j_0$ (equivalently
$j_0\le n_0/2$, so that the triple $(n_0,i_0,j_0)$ exists at all) holds
for exactly two exception pairs: $(n_0,i_0)=(30,7)$, giving the triple
$(30,7,11)$, and $(n_0,i_0)=(56,13)$, giving the triple $(56,13,20)$.
Both triples satisfy the conjecture, by direct computation:

* $(30,7,11)$: $C(30,7)=2^3\cdot3^3\cdot5^2\cdot13\cdot29$, so
  $V_7(30)=13\cdot29=377$, and
  $\gcd(V_7(30),C(30,11))=\gcd(377,54627300)=377>1$.
* $(56,13,20)$: $C(56,13)=2^4\cdot3^2\cdot5^2\cdot7^2\cdot11\cdot17
  \cdot23\cdot47\cdot53$, so
  $V_{13}(56)=17\cdot23\cdot47\cdot53=973981$, and
  $\gcd(V_{13}(56),C(56,20))=\gcd(973981,785613562163430)
  =57293=23\cdot47\cdot53>1$.

*Proof.* The enumeration is a finite check on the 12 listed pairs:
$j_0$ and $2j_0$ for $i_0=3,4,5,5,7,8,7,13,14,13,17,13$ are
$5,7,8,8,11,13,11,20,22,20,26,20$, and $n_0\ge2j_0$ holds only for
$(30,7)$ ($30\ge22$) and $(56,13)$ ($56\ge40$). The two gcd computations
are exact integer computations (recomputed by this prover; §6); the
factorisations displayed are those of $C(30,7)$ and $C(56,13)$, and
$V$ is by definition the product of the prime powers with $p\ge i$.
$\square$

> **Failure report (loud).** S5, §4 ("EEES78 proviso") and §8, states
> that "the only EEES78 exception pair falling inside this family with
> $n\ge2j$ is $(n,i,j)=(56,13,20)$". **This is false.** The pair
> $(30,7)$ also falls inside the family: $i=7$ gives
> $j=\lfloor21/2\rfloor+1=11$ and $30\ge22=2j$. S5's Theorem 5, taken
> literally with its stated proviso, therefore leaves the triple
> $(30,7,11)$ unclosed. The gap is presentational rather than fatal:
> $(30,7,11)$ is closed by the direct computation above (indeed the
> whole of $V_7(30)=377$ divides $C(30,11)$), and with Lemma A2.13 in
> place of S5's proviso the boundary-family theorem below is complete.
> Verifiers should not cite S5's proviso without this correction.

### 3.2 The small even cases $i=4,6,8$

**Lemma A2.14 (finite closure of $(4,7)$, $(6,10)$, $(8,13)$).**
The three boundary pairs where Lemma A2.12's inequality fails are
closed for all $n$, as follows. For a fixed pair $(i,j)$, Lemma
A2.2(b) shows that a counterexample with $(n,i)$ non-exceptional
satisfies $n\le N(i,j):=\max\{n:C(n,i)<C(2j,2d)\}$. Direct evaluation
gives $N(4,7)=17$, $N(6,10)=23$, $N(8,13)=29$. The only EEES78
exception pairs with $i\in\{4,6,8\}$ are $(9,4)$ and $(21,8)$, and
$9<14=2j$, $21<26=2j$, so no exception triple exists for these pairs.
It remains to check $2j\le n\le N(i,j)$ directly, and the exact gcds
$\gcd(V_i(n),C(n,j))$ are:

* $(4,7)$, $n=14,15,16,17$: $143,\ 65,\ 65,\ 17$.
* $(6,10)$, $n=20,21,22,23$: $323,\ 2261,\ 24871,\ 33649$
  (in each case the gcd equals $V_6(n)$ itself).
* $(8,13)$, $n=26,27,28,29$: $437,\ 23,\ 23,\ 667$.

All are $>1$, so no triple with these pairs is a counterexample, for
any $n$ whatsoever.

*Proof.* The bounds $N(i,j)$ are exact: e.g. for $(4,7)$,
$C(17,4)=2380<C(14,6)=3003\le C(18,4)=3060$, and similarly
$C(23,6)<C(20,8)\le C(24,6)$, $C(29,8)<C(26,10)\le C(30,8)$ by direct
evaluation; monotonicity (Lemma A2.3) then gives $n\le N(i,j)$ for any
non-exceptional counterexample, and $n>N(i,j)$ is impossible by Lemma
A2.2(b) contraposed. The gcd table is exact integer arithmetic
(recomputed by this prover; §6). For $n$ in the table the conclusion
holds whether or not $(n,i)$ is exceptional, and the two exceptional
$n$ values lie below $2j$ anyway. $\square$

**Theorem A2.15 (T3, boundary family: complete for all $i$).**
Let $i\ge1$ and $j=\lfloor3i/2\rfloor+1$. Then for every $n\ge2j$,
$\gcd(V_i(n),C(n,j))>1$.

*Proof.* If $i=1$, this is Theorem A2.5 ($j=2$). If $i=2$, this is
Theorem A2.7 ($j=4$). Let $i\ge3$ and suppose $(n,i,j)$ were a
counterexample. If $(n,i)$ is EEES78-non-exceptional and $i$ is odd
$\ge3$ or even $\ge10$, Lemmas A2.11/A2.12 give $C(2j,i)>C(j,d)^2$,
contradicting Lemma A2.10. If $i\in\{4,6,8\}$, Lemma A2.14 excludes
every $n$. If $(n,i)$ is an EEES78 exception pair, Lemma A2.13 shows
the only possible triples are $(30,7,11)$ and $(56,13,20)$, and both
have gcd $>1$, contradicting the counterexample assumption. All cases
are covered. $\square$

**Remark A2.16.** The task's formulation of T3 allowed an explicit
finite small set of excluded $i$. No exclusion is needed in the end:
the square method itself covers odd $i\ge3$ and even $i\ge10$; the
three remaining pairs are closed by the finite Phase 0 interval plus
twelve explicit gcd values (Lemma A2.14); and $i=1,2$ are Theorems
A2.5 and A2.7. Note the division of labour is sharp: for
$(4,7),(6,10),(8,13)$ the square inequality genuinely fails
($R_m<1$ in Lemma A2.12), so *some* non-square argument is necessary
there; the finite reduction is the one used.


## 4. (T4) The case $i=3$: exactly what is proved, and the precise obstruction

Throughout §4, $i=3$ and $3<j\le n/2$, so $V_3(n)$ is the odd part of
$C(n,3)$: the only prime discarded by the threshold is $2$.

### 4.1 The closed part

**Lemma A2.17 ($j=4$, all $n$).**
For every $n\ge8$, $\gcd(V_3(n),C(n,4))>1$.

*Proof.* $j=4\le 3i/2=4.5$. If $(n,3)$ is EEES78-non-exceptional and
$(n,3,4)$ were a counterexample, Lemma A2.2(b) would give
$C(n,3)<C(8,2)=28$; but $2(j-i)=2\le i=3\le j$ gives
$C(2j,2(j-i))=C(8,2)=28\le C(8,3)=56\le C(n,3)$ (binomial coefficients
$C(8,\cdot)$ increase up to the middle, and Lemma A2.3), a
contradiction. The only EEES78 exception pair with $i=3$ is $(8,3)$,
and at $n=8$: $C(8,3)=56=2^3\cdot7$, $V_3(8)=7$, $C(8,4)=70$,
$\gcd(7,70)=7>1$. $\square$

**Lemma A2.18 ($(3,5)$, two independent closures).**
For every $n\ge10$, $\gcd(V_3(n),C(n,5))>1$.

*Proof.* First proof: $(3,5)$ is the boundary pair of §3
($\lfloor 9/2\rfloor+1=5$), so Theorem A2.15 applies; the relevant
exception pair $(8,3)$ has $8<10=2j$ and does not occur. Second proof
(EEES-free, S1 Theorem B(3)): for $i=3$ the small part $u$ is a power
of $2$, and by the Legendre bound of Lemma A2.20 below (with $p=2$),
$u\le 2^{\lfloor\log_2 n\rfloor}\le n$. A counterexample satisfies
$v\mid C(5,2)=10$ by Lemma A2.1, hence $C(n,3)=uv\le 10n$, i.e.
$F_3(n):=C(n,3)/n\le10$. But $F_3(n+1)/F_3(n)=n/(n-2)>1$, so $F_3$ is
strictly increasing, and $F_3(10)=120/10=12>10$; hence no $n\ge10$ is
a counterexample. $\square$

**Lemma A2.19 ($(3,6)$ via the sharpened bound, S1 Theorem B(4)).**
For every $n\ge12$, $\gcd(V_3(n),C(n,6))>1$.

*Proof.* Let $U^\sharp(n)=2^{\lfloor\log_2 n\rfloor}$, the largest power
of $2$ that is $\le n$. By Lemma A2.20 with $p=2$, the $2$-part $u$ of
$C(n,3)$ satisfies $u\le U^\sharp(n)$. A counterexample satisfies
$v\mid C(6,3)=20$ by Lemma A2.1, hence $C(n,3)\le U^\sharp(n)\cdot20$,
i.e. $G_3(n):=C(n,3)/U^\sharp(n)\le20$. On $12\le n\le15$,
$U^\sharp(n)=8$ is constant while $C(n,3)$ is strictly increasing, so
$G_3$ is increasing there and $G_3(n)\ge G_3(12)=220/8=27.5>20$. For
$n\ge16$, $G_3(n)\ge F_3(n)\ge F_3(16)=560/16=35>20$, using
$U^\sharp(n)\le n$ and the monotonicity of $F_3$ from Lemma A2.18.
Hence no $n\ge12$ is a counterexample. No EEES78 input is used.
$\square$

**Lemma A2.20 (prime-power bound; S5 Lemma 6 / S1 Lemma 2).**
For every prime $p$ and $1\le k\le n$,
$p^{v_p(C(n,k))}\le p^{\lfloor\log_p n\rfloor}\le n$.

*Proof.* Legendre's formula expresses $v_p(C(n,k))$ as a sum over
$e\ge1$ of
$\lfloor n/p^e\rfloor-\lfloor k/p^e\rfloor-\lfloor(n-k)/p^e\rfloor$;
each summand is $0$ or $1$ (it is
$\lfloor x+y\rfloor-\lfloor x\rfloor-\lfloor y\rfloor$ for
$x=k/p^e$, $y=(n-k)/p^e$), and summands with $p^e>n$ vanish, leaving at
most $\lfloor\log_p n\rfloor$ nonzero terms. $\square$

So for $i=3$ the pairs $j=4,5,6$ are closed for all $n$. The rest of §4
concerns $j\ge7$.

### 4.2 The low-digit reduction (S8 §3)

**Lemma A2.21 (low digits; S8 Lemma 3).**
Let $q=p^a$ exactly divide $m=n-r$ for some $r\in\{0,1,2\}$, where
either (a) $p\ge5$, or (b) $p=3$ and $a\ge2$. Then $p\mid C(n,3)$, and

$$p\nmid C(n,j)\ \Longrightarrow\ j\bmod q\le r.$$

Equivalently, if $j\bmod q>r$ then $p$ is a common prime $\ge3$ of
$C(n,3)$ and $C(n,j)$ and the triple is closed.

*Proof.* First $p\mid C(n,3)$. Case (a): $p\mid n(n-1)(n-2)$ (it
divides $m$), $p$ divides only one of the three factors (two of them
differ by at most $2<p$), and $p\nmid6$, so
$v_p(C(n,3))=v_p(n(n-1)(n-2))\ge a\ge1$. Case (b): exactly one of three
consecutive integers is divisible by $3$, namely $m$, and
$v_3(C(n,3))=a-v_3(6)=a-1\ge1$. Second, the digits: $n\equiv r\pmod q$
with $0\le r<p$, so the lowest $a$ base-$p$ digits of $n$ are $r$
followed by zeros. If $p\nmid C(n,j)$ then by Kummer (External input
2) $j$ is digitwise $\le n$ in base $p$, forcing $j$'s lowest digit to
be $\le r$ and its next $a-1$ digits to be $0$, i.e. $j\bmod q\le r$.
$\square$

**Definition A2.22 ((LD3)).**
For $m\in\{n,n-1,n-2\}$ let $R(m)$ be the product of the prime powers
$q=p^a\Vert m$ (exact powers) with $p\ge5$ (any $a\ge1$) or $p=3$,
$a\ge2$. The pair $(n,j)$ **satisfies (LD3)** if for every such $q\mid
R(m)$, with $r=n-m$: $j\bmod q\in\{0,1,\dots,r\}$. Equivalently:
$R(n)\mid j$; $R(n-1)=X_0X_1$ with $X_0\mid j$, $X_1\mid j-1$;
$R(n-2)=Y_0Y_1Y_2$ with $Y_s\mid j-s$ for $s=0,1,2$ (the factorisation
form holds because the prime powers in question are pairwise coprime,
also across the three numbers $n,n-1,n-2$, a prime $p\ge3$ dividing at
most one of them; and for each such $q$ one has $q\ge5>2\ge r$, so
$j\bmod q\le r$ is exactly the statement that $q$ divides one of
$j,j-1,\dots,j-r$, the choices for different $q$ being independent).

**Corollary A2.23 (necessity).**
If $(n,3,j)$ is a counterexample, then $(n,j)$ satisfies (LD3).

*Proof.* For each relevant $q$, Lemma A2.21's $p$ divides $C(n,3)$ and
$p\ge3$, so $p$ is a prime divisor of $V_3(n)$; the counterexample
assumption gives $p\nmid C(n,j)$, and Lemma A2.21 gives
$j\bmod q\le r$. $\square$

**Lemma A2.24 (two further necessary conditions).**
If $(n,3,j)$ is a counterexample, then

(N1) $\gcd(C(n,2),C(n,j))=2^a3^b$ for some $a,b\ge0$ (the level-2 gcd
is $6$-smooth);

(N2) $V_3(n)\mid C(j,3)$, in particular $V_3(n)\le C(j,3)$.

*Proof.* (N1) If a prime $p\ge5$ divided both $C(n,2)$ and $C(n,j)$,
then $p\mid n(n-1)$ ($p$ odd), hence $p\mid C(n,3)$ by the argument of
Lemma A2.21(a), so $p$ would divide $V_3(n)$ and $C(n,j)$,
contradicting the counterexample assumption. (N2) is Lemma A2.1 with
$d=V_3(n)$. $\square$

**Lemma A2.25 (odd-top reduction; S8 §3.5).**
Let $m$ be odd. Then $R(m)=m$ if $3\nmid m$ or $9\mid m$, and
$R(m)=m/3$ if $v_3(m)=1$. Consequently, under (LD3):

(i) if $n$ is odd and $R(n)=n$, then $n\mid j$, impossible; hence
(LD3) with $n$ odd forces $v_3(n)=1$, $R(n)=n/3\mid j$, and since
$j\le n/2$ this pins $j=n/3$ exactly (in particular $3\mid n$);

(ii) if $n$ is even, the odd top number is $n-1$ ($r=1$):
$R(n-1)\in\{n-1,(n-1)/3\}$ must split as $X_0X_1$ with $X_0\mid j$ and
$X_1\mid j-1$; in particular if $R(n-1)$ is a single prime power
exceeding $n/2$ (e.g. $R(n-1)=n-1$ with $n-1$ prime) it divides
neither $j$ nor $j-1$ and the triple is closed.

*Proof.* For odd $m$, the prime $2$ does not occur in $m$, so every
exact prime power $p^a\Vert m$ is relevant except possibly $3^1$,
which is excluded exactly when $v_3(m)=1$; this gives the formula for
$R(m)$. Parts (i) and (ii) are then Definition A2.22 read off for
$r=0$ and $r=1$ respectively, using $X_0,X_1\le j\le n/2$. $\square$

**Proposition A2.26 (the $\ge5$ subsystem and its six small solutions;
the $3^a+1$ family).**
Drop the $p=3$ clauses from (LD3). The resulting $\ge5$ system has, by
direct computation, exactly six solutions with $n\le2000$:
$(10,5)$, $(28,14)$, $(82,41)$, $(162,70)$, $(244,122)$, $(730,365)$.
Each is killed by the $3$-clause of Lemma A2.21: for
$n=3^a+1$, $j=n/2$ ($a\ge2$, covering five of the six, with
$a=2,3,4,5,6$), $q=3^a\mid n-1$ with $r=1$ and
$j\bmod 3^a=j=(3^a+1)/2>1$, so $3\mid C(n,j)$ and $3\mid C(n,3)$; for
$(162,70)$, $q=81\mid162$ with $r=0$ and $70\bmod81=70>0$, so again
$3$ is the witness. Moreover the argument for $n=3^a+1$, $j=n/2$,
$a\ge2$ is a proof for **all** $a$, not only $n\le2000$: that infinite
family is closed at $i=3$.

*Proof.* The enumeration is exact computation (recomputed by this
prover; §6). The killing computations are the displayed congruences
together with Lemma A2.21(b): in the family case
$v_3(C(n,3))=a-1\ge1$ since $3^a\Vert n-1$; in the $(162,70)$ case
$81\Vert162$, $v_3(C(162,3))=4-1=3\ge1$. $\square$

**Computational status (evidence, not proof).**
This prover independently recomputed S8's headline claim: the
criterion of Lemma A2.21 fires for **every one of the $6{,}235{,}009$
triples** with $6\le n\le5000$, $4\le j\le n/2$; equivalently (LD3) has
**no solution with $n\le5000$**. This agrees exactly with S8 §3.4
(same triple count). It is strong evidence for the unsatisfiability
of (LD3) and proves nothing for $n>5000$.

### 4.3 The precise remaining obstruction

**Statement A2.27 (the obstruction $H_3$, formal).**
What is missing for a complete proof at $i=3$ is a proof of:

> $(H_3)$ There do not exist integers $n,j$ with $7\le j\le n/2$
> satisfying (LD3) of Definition A2.22,

or, failing that, a characterisation of the solutions of (LD3) in
that range together with, for each solution family, an additional
argument (higher-digit Kummer conditions beyond the lowest $a$
digits, or (N2), or a direct witness) closing it.

By Corollary A2.23 and Lemmas A2.17–A2.19, a proof of $(H_3)$ would
complete $i=3$ for all $j$ and all $n$: $j=4,5,6$ are closed, and any
counterexample with $j\ge7$ would satisfy (LD3). Conversely, (LD3) is
a **necessary, not sufficient**, condition for a counterexample: it
records only the lowest $a$ base-$p$ digits. A solution of (LD3), if
one exists for some $n>5000$, would not be a counterexample to #699;
it would merely be a triple the low-digit method cannot close. So
$(H_3)$ is exactly the obstruction *for this route*, stated as S8
§3.2 states it, and no claim stronger than that is made here.

**Statement A2.28 (the splitting sub-case, where $(H_3)$ actually
lives).**
By Lemma A2.25, any proof of $(H_3)$ must dispose of exactly the
following residual configurations, in which all single-prime-power
size arguments have already been exhausted:

(SPLIT-odd) $n$ odd, $v_3(n)=1$, $j=n/3$ pinned, **and** the
$r=1$ condition on $n-1$ and the $r=2$ condition on $n-2$ both hold
by genuine distribution of their relevant prime powers among
$j,j-1$ and $j,j-1,j-2$ respectively.

(SPLIT-even) $n$ even, $R(n)\mid j$, **and** $R(n-1)$ has at least two
distinct relevant prime-power factors, distributed between divisors
of $j$ and of $j-1$ (a single prime power $>n/2$ is excluded by
Lemma A2.25(ii); a single prime power $\le j$ is not excluded by any
size consideration, since it may simply divide $j$ or $j-1$),
**and** the analogous three-way distribution for $R(n-2)$ among
$j,j-1,j-2$ holds.

In both configurations every individual prime power $q$ is $\le j$
(or divides a number $\le j$), so no inequality of the form
$q>j$ or $R(m)>j$ applies; the conditions are a simultaneous
congruence/distribution system (each $q$ must divide one of two or
three consecutive integers, the choices for different $q$ being
independent a priori), and the Chinese remainder theorem poses no
obstruction to such distributions in general. This is the exact
place the $i=3$ proof stops. This prover attempted to push the
(LD3) analysis further along S8 §3.5's lines, in particular the
pinned case (SPLIT-odd), and found only additional necessary
conditions, not a contradiction; one is recorded in Remark A2.29
as an illustration of the gap's nature.

**Remark A2.29 (a sharpening in the pinned case, still not a
closure).**
In case (SPLIT-odd), (N2) forces $v_2(C(n,3))\ge5$: indeed
$v_3(C(n,3))=0$ there (as $v_3(n)=1$), so the small part of $C(n,3)$
is $u=2^{v_2(C(n,3))}$, while with $n=3j$,
$C(n,3)/C(j,3)=\frac{3j}{j}\cdot\frac{3j-1}{j-1}\cdot\frac{3j-2}{j-2}
>27$ (the first factor equals $3$ and the other two exceed $3$), so $V_3(n)\le C(j,3)$ requires
$u>27$, i.e. $u\ge32$. This restricts pinned-case counterexamples to
$n$ with an unusually large $2$-adic valuation of $C(n,3)$, but such
$n$ exist in abundance (e.g. $n$ near a power of $2$ in the carry
count), and no contradiction results. The same pattern, conditions
that thin the candidate set without emptying it, was the outcome of
every strengthening of (LD3) this prover tried within the
low-digit framework.

**Conclusion for $i=3$.** Proved: $j\le6$, all $n$ (Lemmas
A2.17–A2.19); every specific triple satisfying any of the checkable
conditions of Lemma A2.21 (in particular all triples with $n\le5000$,
and the infinite families: some of $n,n-1,n-2$ prime; $n=3^a+1$ with
$j=n/2$). **Not proved: $i=3$ in general.** The deliverable for the
open part is Statements A2.27 and A2.28: a counterexample with
$j\ge7$ must satisfy the explicit finite-type congruence system
(LD3), and a proof at $i=3$ via this route is equivalent to
resolving the splitting configurations (SPLIT-odd) and (SPLIT-even).

## 5. Summary of what is proved

* **T1 ($i=1$): complete, unconditional, all $j$, all $n$**
  (Theorem A2.5, two proofs).
* **T2 ($i=2$): complete, unconditional, all $j$, all $n$**
  (Theorem A2.7).
* **T3 (boundary family $j=\lfloor3i/2\rfloor+1$): complete for
  every $i\ge1$ and all $n$** (Theorem A2.15), via the square
  reduction and the exact step-ratio identities, with the small
  even pairs closed by a finite Phase 0 interval and the EEES78
  exceptions corrected and discharged (Lemma A2.13; S5's proviso as
  stated is **false**, see §3.1).
* **T4 ($i=3$): not closed in general.** Closed: $j=4,5,6$ for all
  $n$; all triples with $n\le5000$ (computation); the families listed
  in §4.3. The precise remaining obstruction is $(H_3)$,
  equivalently the splitting configurations (SPLIT-odd) and
  (SPLIT-even) of Statement A2.28.

## 6. Computations performed by this prover (Python stdlib, exact)

1. $\gcd(V_{13}(56),C(56,20))=57293$ and
   $\gcd(V_7(30),C(30,11))=377$, with the factorisations displayed in
   Lemma A2.13.
2. Boundary ratios $R_m$ in exact rational arithmetic for odd and
   even $m$ (values in Lemmas A2.11, A2.12, including $R_m<1$ exactly
   for even $m=1,2,3,4$); the step-ratio formula of Lemma A2.11 and
   of Lemma A2.12 verified in exact rational arithmetic at
   $m=1,\dots,10,37,100,251$, and the "$-1$" numerator identities
   verified symbolically as polynomial identities.
3. $N(4,7)=17$, $N(6,10)=23$, $N(8,13)=29$ and the twelve gcd values
   of Lemma A2.14.
4. (LD3): no solution with $n\le5000$ (all $6{,}235{,}009$ triples);
   the $\ge5$-only system has exactly the six solutions of
   Proposition A2.26 with $n\le2000$.
5. Spot values: $\gcd(V_3(8),C(8,4))=7$,
   $\gcd(V_3(12),C(12,6))=11$.
