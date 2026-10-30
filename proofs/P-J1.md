# Prover J1 (independent): Cluster J, the $v_2$ condition and refined comparisons at $i=3$, Cycle 3

Prover: J1, working independently in Cycle 3. `proofs/P-J2.md` was
**not** read or looked for; independence from the second prover of this
cluster is methodological and was preserved. Sources read (ground
truth, in the order given by the assignment): `CYCLE2.md` Section 2;
`proofs/P-F1.md` (especially Claims F1.12 to F1.14); `proofs/P-F2.md`
Sections 1 and 4.1 (Theorem F2.15, Corollary F2.16);
`verification/V-F.md`; `proofs/P-A1.md` (Lemma A1.15, Proposition
A1.16, Statement (H3)). Every computation below is in
`proofs/P-J1_checks.py` (Python standard library only, exact integer
arithmetic; total runtime under 1 second on this machine). Every numbered
claim is labelled PROVED, GAP, FALSE, OPEN, or COMPUTATION.

**Headline.** $i=3$ is **not** closed in general, and (H3) is **not**
proved. What is new in this file: (a) a complete, self-contained
$v_2$ theory (Section 1): for every $v \ge 2$ the set
$\{n : v_2(C(n,3)) \ge v\}$ is exactly five residue classes modulo
$2^{v+1}$, namely $\{0, 1, 2, 2^v, 2^v+2\}$, of density
$5/2^{v+1}$; (b) an exact $Q$-stratification (Section 2): a
counterexample in row $Q$ must satisfy
$v_2(C(n,3)) \ge v_{\min}(Q) = \lfloor 3\log_2 Q \rfloor + 1$, so the
brief's expected values $v_{\min}(2)=4$, $v_{\min}(3)=5$,
$v_{\min}(4)=7$ are all **correct**, and the formula is proved for
every $Q \ge 2$ and is best possible from the comparison that produces
it; (c) row closures (Section 3): intersecting the squared half of
Price Proposition 4.1 with the two certified frontiers ($j \le 5000$
per pair, and no (LD3) solution with $n \le 10^6$) closes, for the
first time in the campaign record, **every** $(Q,R)$ row with
$Q=2$ and even $R \le 22$, **every** row with $Q=3$ and $R \le 20$,
and **every** row with $Q=4$ and even $R \le 18$, together with all
$h=1$ rows at $Q \in \{2,3,4\}$ (several already closed in Cycle 2);
the first rows not closed by this combination are
$(2,24)$, $(3,21)$, $(4,20)$, each left with an explicit finite
$j$-window; (d) the GAP in Claim F1.14 is settled, and its final
sentence is **FALSE** (Section 4): the $V_3$-refined comparison closes
the full pair $(3,j)$ on the finite-reduction interval exactly for
$j \in \{5, 6, 10\}$ among $5 \le j \le 18$, and for **no** $j \ge 19$,
the obstruction for large $j$ being an explicit power-of-two witness
$n = 2^{\lceil \log_2 2j \rceil}$ with $V_3(n) \le C(j,3)$; a second
comparison of my own design (the $2^{v_2} \le n$ tail bound) shows in
addition that the closures at $j=6$ and $j=10$ hold for **all**
$n \ge 2j$ unconditionally, with no EEES78 or finite-reduction input.

## 0. Standing inputs and notation

$C(n,k) = \binom nk$; $V_3(n) = C(n,3)/2^{v_2(C(n,3))}$, the part of
$C(n,3)$ on primes $\ge 3$; a **counterexample** is a triple
$(n,3,j)$, $3 < j \le n/2$, with $\gcd(V_3(n), C(n,j)) = 1$.
$s_2(m)$ is the binary digit sum. Used as certified ground truth
(Cycle 2, verified by V-F): the key lemma and its consequence
**(N2)** $V_3(n) \mid C(j,3)$; **(N1)**; the system **(LD3)**;
Price Proposition 4.1 at $i=3$ (F1.2 / F2.3): with $n = Qj + R$,
$Q = \lfloor n/j \rfloor \ge 2$, $0 \le R < j$, $T = R + 2(Q-1)$,
$h = \max(0, \lceil (3-R)/Q \rceil)$,
$$V_3(n) \mid \Lambda_3(T) \binom{j}{h},
\qquad
C(n,3) < \Bigl(\Lambda_3(T) \binom{j}{h}\Bigr)^2
\ \text{(EEES form)},$$
where $\Lambda_3(T) = \prod_{q \ge 3} q^{\lfloor \log_q T \rfloor}$
is the $\ge 3$ part of $\mathrm{lcm}(1,\dots,T)$; the label bounds
F1.9 / F2.4 / F2.9; the closed rows
$(Q,R) \in \{(2,0), (2,2), (3,0), (3,2), (4,0)\}$ (F1.10); no
counterexample with $n$ odd (F1.5 / F2.7); the finite reduction
$n \le N(3,j) := \max\{n : C(n,3) < C(2j,6)\}$, the only EEES78
exception pair at $i=3$ being $(8,3)$, which admits no $j \ge 5$;
every pair $(3,j)$ with $j \le 5000$ closed for all $n$ (F2.19);
(LD3) has no solution with $n \le 10^6$ (F1.17 / F2.21). Net certified
necessary conditions for a counterexample, used throughout: $n$ even,
$j \ge 5001$, $n > 10^6$, $v_2(C(n,3)) \ge 4$. No certified input read
for this cluster was found to be wrong; the one statement found to be
wrong is F1.14's final sentence, which V-F already flagged as a GAP
rather than as certified (see Claim J4.2).

## 1. J.1: exact $v_2$ theory

**Claim J1.1 (PROVED, the three faces of $v_2(C(n,3))$).** For
$n \ge 3$,
$$v_2(C(n,3)) \;=\; s_2(n-3) + s_2(3) - s_2(n)
\;=\; s_2(n-3) + 2 - s_2(n),$$
and $v_2(C(n,3))$ equals the number of borrows when subtracting $3$
from $n$ in binary (equivalently, the number of carries when adding
$3$ and $n-3$ in binary).

*Proof.* Legendre's formula gives
$v_2(m!) = \sum_{k \ge 1} \lfloor m/2^k \rfloor$. If
$m = \sum_i b_i 2^i$ is the binary expansion, then
$\lfloor m/2^k \rfloor = \sum_{i \ge k} b_i 2^{i-k}$, and summing over
$k \ge 1$ gives $\sum_i b_i (2^i - 1) = m - s_2(m)$. Hence
$v_2(C(n,3)) = v_2(n!) - v_2(3!) - v_2((n-3)!)$
$= (n - s_2(n)) - (3 - s_2(3)) - ((n-3) - s_2(n-3))$
$= s_2(n-3) + s_2(3) - s_2(n)$, and $s_2(3) = 2$. The borrow statement
is Kummer's theorem at $p=2$ applied to $C(n,3) = C(n, n-3)$: the
valuation is the number of carries when adding $3$ and $n-3$, which
is the number of borrows in the subtraction $n - 3$. The two
expressions agree because both equal $v_2(C(n,3))$. (Script Section A
verifies both identities, against the factorisation definition, for
all $3 \le n \le 5000$.) $\square$

**Claim J1.2 (PROVED, the threshold $4$ in parity form; the brief's
forms are correct).**
$$v_2(C(n,3)) \ge 4 \iff v_2\bigl(n(n-1)(n-2)\bigr) \ge 5.$$
For $n$ even this is equivalent to $16 \mid n$ or $16 \mid (n-2)$;
for $n$ odd it is equivalent to $32 \mid (n-1)$.

*Proof.* $C(n,3) = n(n-1)(n-2)/6$ and $v_2(6) = 1$, proving the first
equivalence. Write $P = v_2(n(n-1)(n-2)) =
v_2(n) + v_2(n-1) + v_2(n-2)$; exactly one of the three consecutive
factors is odd-indexed in the middle, and the parity cases are:

* $n$ odd: $v_2(n) = v_2(n-2) = 0$, so $P = v_2(n-1)$, and
  $P \ge 5 \iff 32 \mid (n-1)$.
* $n \equiv 0 \pmod 4$: $v_2(n-2) = 1$, so $P = v_2(n) + 1$, and
  $P \ge 5 \iff v_2(n) \ge 4 \iff 16 \mid n$ (which indeed implies
  $n \equiv 0 \pmod 4$).
* $n \equiv 2 \pmod 4$: $v_2(n) = 1$, so $P = 1 + v_2(n-2)$, and
  $P \ge 5 \iff v_2(n-2) \ge 4 \iff 16 \mid (n-2)$.

The two even subcases are disjoint and cover all even $n$.
(Script Section A verifies the equivalence for all $n \le 20000$.)
$\square$

**Claim J1.3 (PROVED, the general classification).** For every
$v \ge 0$, the set $\{n : v_2(C(n,3)) \ge v\}$ is a union of residue
classes modulo $2^{v+1}$. Exactly:

* $v = 0$: all $n$ (2 classes mod 2), density $1$;
* $v = 1$: the classes $\{0, 1, 2\}$ mod 4 (3 classes), density $3/4$;
* $v \ge 2$: exactly **five** classes modulo $2^{v+1}$,
  $$\{0,\ 1,\ 2,\ 2^v,\ 2^v + 2\} \pmod{2^{v+1}},$$
  of density $5/2^{v+1}$. In particular
  $v=4$: $\{0,1,2,16,18\}$ mod 32, density $5/32$;
  $v=5$: $\{0,1,2,32,34\}$ mod 64, density $5/64$;
  $v=6$: $\{0,1,2,64,66\}$ mod 128, density $5/128$.

*Proof.* Since $v_2(C(n,3)) = P - 1$ with $P$ as in Claim J1.2, the
condition is $P \ge v+1$. A valuation $v_2(m) \ge v+1$ holds iff
$m \equiv 0 \pmod{2^{v+1}}$, and $v_2(m) = t \le v$ is determined by
$m \bmod 2^{v+1}$; so $P \ge v+1$, a condition on the three valuations
each capped at $v+1$, depends only on $n \bmod 2^{v+1}$.

Let $v \ge 2$. Case $n$ odd: $P = v_2(n-1)$, so the condition is
$v_2(n-1) \ge v+1$, i.e. $n \equiv 1 \pmod{2^{v+1}}$: one class.
Case $n \equiv 0 \pmod 4$: $P = v_2(n) + 1$, so the condition is
$v_2(n) \ge v$, i.e. $n \equiv 0 \pmod{2^v}$; the residues mod
$2^{v+1}$ divisible by $2^v$ are $0$ and $2^v$, and both are
$0 \pmod 4$ because $v \ge 2$: two classes. Case $n \equiv 2 \pmod 4$:
$P = 1 + v_2(n-2)$, so the condition is $v_2(n-2) \ge v$, i.e.
$n \equiv 2 \pmod{2^v}$; the residues mod $2^{v+1}$ congruent to $2$
mod $2^v$ are $2$ and $2^v + 2$, and both are $2 \pmod 4$ because
$v \ge 2$: two classes. The five classes are pairwise distinct (they
are distinct mod $2^{v+1}$: $0 < 1 < 2 < 2^v < 2^v + 2 < 2^{v+1}$ for
$v \ge 2$), and every $n$ falls in exactly one of the three cases, so
the list is complete.

For $v = 1$, argue directly mod 4: $n \equiv 0 \pmod 4$ gives
$v_2(C(n,3)) = v_2(n) \ge 2$; $n \equiv 2 \pmod 4$ gives
$v_2(C(n,3)) = v_2(n-2) \ge 2$; $n \equiv 1 \pmod 4$ gives
$v_2(n-1) \ge 2$, hence $v_2(C(n,3)) \ge 1$; $n \equiv 3 \pmod 4$
gives $v_2(n-1) = 1$, hence $v_2(C(n,3)) = 0$. So the set is
$\{0,1,2\}$ mod 4. (The $v \ge 2$ counting degenerates at $v=1$
because $2^v = 2$ is not $0 \pmod 4$ and the two even subcase lists
coincide.) $v = 0$ is vacuous. Script Section A confirms the lists
for $0 \le v \le 7$. $\square$

**Corollary J1.4 (PROVED).** (i) The certified F2.16 density is
recovered: $v_2(C(n,3)) \le 3$ iff $v_2(C(n,3)) \not\ge 4$, a set of
$32 - 5 = 27$ classes mod 32, density $27/32$. (ii) Inside the
residual class ($n$ even), $v_2(C(n,3)) \ge v$ (for $v \ge 2$) confines
$n$ to the four even classes $\{0, 2, 2^v, 2^v + 2\}$ mod $2^{v+1}$,
of absolute density $4/2^{v+1}$, i.e. a proportion $2^{1-v}$ of all
even $n$. (iii) The exact $v_2$ thresholds of F1.13 are consistent
with this theory and are spot re-verified in script Section F:
$n_0(j,4) = 14, 17, 19, 24, 49$ and $n_0(j,5) = 17, 20, 24, 30, 62$
for $j = 6, 7, 8, 10, 20$ (COMPUTATION).

## 2. J.2: $Q$-stratification

Fix $Q \ge 2$ and $j > 2$, and put
$\rho(Q,j) = C(Qj,3)/C(j,3) = Q(Qj-1)(Qj-2)/((j-1)(j-2))$.

**Claim J2.1 (PROVED, behaviour of $\rho$).** For fixed $Q$, $\rho(Q,
\cdot)$ is strictly decreasing in $j$ (as a function of a real
variable $j > 2$, hence on integers), satisfies $\rho(Q,j) > Q^3$ for
every finite $j$, and $\lim_{j \to \infty} \rho(Q,j) = Q^3$. Hence
$\inf_j \rho(Q,j) = Q^3$, and the infimum is not attained.

*Proof.* $\rho(Q,j) = Q \cdot \frac{Qj-1}{j-1} \cdot \frac{Qj-2}{j-2}$,
and for $a \in \{1,2\}$,
$\frac{Qj-a}{j-a} = Q + \frac{a(Q-1)}{j-a}$, which is strictly
decreasing in $j > a$ and strictly greater than $Q$, with limit $Q$.
A product of two strictly decreasing positive functions is strictly
decreasing; the product is $> Q \cdot Q = Q^2$, so $\rho > Q^3$, and
both factors tend to $Q$, so $\rho \to Q^3$. (Script Section B
verifies strict decrease and $\rho > Q^3$ in exact rational arithmetic
for $2 \le Q \le 8$, $j < 400$.) $\square$

**Claim J2.2 (PROVED, the exact uniform $v_{\min}(Q)$).** Let
$(n,3,j)$ be a counterexample with $n \ge Qj$ (in particular in row
$Q$, where $n = Qj + R$). Then
$$2^{v_2(C(n,3))} \;\ge\; \frac{C(n,3)}{C(j,3)} \;\ge\; \rho(Q,j)
\;>\; Q^3,
\qquad\text{hence}\qquad
v_2(C(n,3)) \;\ge\; v_{\min}(Q) \;:=\; \lfloor 3 \log_2 Q \rfloor + 1,$$
the least integer $v$ with $2^v > Q^3$. Values (script Section B):

| $Q$ | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| $v_{\min}(Q)$ | 4 | 5 | 7 | 7 | 8 | 9 | 10 | 10 | 10 | 11 | 11 | 12 | 12 | 12 | 13 |
| density $5/2^{v_{\min}+1}$ | 5/32 | 5/64 | 5/256 | 5/256 | 5/512 | 5/1024 | 5/2048 | 5/2048 | 5/2048 | 5/4096 | 5/4096 | 5/8192 | 5/8192 | 5/8192 | 5/16384 |

The brief's expected values $v_{\min}(2) = 4$, $v_{\min}(3) = 5$,
$v_{\min}(4) = 7$ are **correct**. The bound is best possible from
this comparison alone, uniformly in $j$: since $2^{v_{\min}(Q)-1}
\le Q^3 < 2^{v_{\min}(Q)}$ and $\rho(Q,j) \downarrow Q^3$, for every
$Q$ there are arbitrarily large $j$ with $\rho(Q,j) < 2^{v_{\min}(Q)}$,
so the inequality $2^{v} \ge \rho$ cannot force
$v \ge v_{\min}(Q) + 1$ for all $j$. (This is sharpness of the
derivation, not the existence of counterexamples.) For a *fixed*
$j$ the sharper necessary condition is $v_2 \ge \lceil \log_2
\rho(Q,j) \rceil$, which is $> v_{\min}(Q)$ for small $j$
(e.g. $\rho(4,5) = 114$ already forces $v_2 \ge 7$ at $j=5$, and
$\rho(2,j) = 8 + 12/(j-2)$ forces $v_2 \ge 4$ at every $j$).

*Proof.* A counterexample satisfies $V_3(n) \le C(j,3)$ by (N2), i.e.
$C(n,3) = 2^{v} V_3(n) \le 2^{v} C(j,3)$ with $v = v_2(C(n,3))$; hence
$2^v \ge C(n,3)/C(j,3)$. Since $C(\cdot, 3)$ is increasing and
$n \ge Qj$, $C(n,3)/C(j,3) \ge C(Qj,3)/C(j,3) = \rho(Q,j) > Q^3$ by
Claim J2.1 (strictness is essential at powers of two: for $Q = 2$,
$2^v > 8$ gives $v \ge 4$, not $v \ge 3$; for $Q = 4$, $2^v > 64$
gives $v \ge 7$). An integer $v$ satisfies $2^v > Q^3$ iff
$v > 3 \log_2 Q$ iff $v \ge \lfloor 3 \log_2 Q \rfloor + 1$. $\square$

**Corollary J2.3 (PROVED, the stratification of the residual class).**
A counterexample in row $Q$ has $n$ confined to the five classes
$\{0, 1, 2, 2^{v}, 2^{v}+2\}$ mod $2^{v+1}$ with $v = v_{\min}(Q)$
(Claim J1.3), and, $n$ being even in the residual class, to the four
even classes $\{0, 2, 2^v, 2^v+2\}$, of absolute density
$4/2^{v+1}$: $1/8$ of all integers at $Q=2$; $1/16$ at $Q=3$;
$1/64$ at $Q = 4$ and $Q = 5$; $1/128$ at $Q=6$; and so on by the
table of Claim J2.2. This is the exact $v_2$ shadow of (N2) per row;
it does not by itself close any row, because the classes are
nonempty for every $Q$ and contain arbitrarily large even $n$.


## 3. J.3: intersection with the residual class

Throughout, $n = Qj + R$, $0 \le R < j$, $T = R + 2(Q-1)$, and the
hypothetical counterexample has $n$ even, $j \ge 5001$, $n > 10^6$.

**Claim J3.1 (PROVED, the $v_2$ conditions as congruences on $j$).**
Let $v = v_{\min}(Q)$ and $S = \{0, 2, 2^v, 2^v+2\}$ (the even classes
of Claim J1.3 mod $2^{v+1}$). The condition $v_2(C(n,3)) \ge v$ is
$Qj + R \bmod 2^{v+1} \in S$. For the small rows:

* $Q = 2$ ($v = 4$): $2j + R \bmod 32 \in \{0, 2, 16, 18\}$. Since the
  residual has $R$ even, this is exactly four classes for $j$ mod 16:
  $j \equiv \frac{s - R}{2} \pmod{16}$ for $s \in \{0,2,16,18\}$
  (the numerators are even). A proportion $1/4$ of $j$ classes.
* $Q = 3$ ($v = 5$): $3j + R \bmod 64 \in \{0, 2, 32, 34\}$. Since
  $3^{-1} \equiv 43 \pmod{64}$, this is exactly four classes
  $j \equiv 43(s - R) \pmod{64}$, $s \in \{0,2,32,34\}$: a proportion
  $1/16$ of $j$ classes.
* $Q = 4$ ($v = 7$): $4j + R \bmod 256 \in \{0, 2, 128, 130\}$.
  Solvability forces $s \equiv R \pmod 4$; in the residual $R$ is
  even, so exactly two values of $s$ are compatible ($s \in \{0,128\}$
  if $R \equiv 0 \pmod 4$; $s \in \{2,130\}$ if $R \equiv 2 \pmod 4$),
  giving exactly two classes $j \equiv \frac{s-R}{4} \pmod{64}$: a
  proportion $1/32$ of $j$ classes.

No contradiction arises from these congruences alone in any row:
each row's system has solutions with $j$ arbitrarily large. Their
force is purely restrictive (density), and the closure results below
come from the label and size conditions, not from $v_2$.

*Proof.* Substitute $n = Qj + R$ in Claim J1.3 and Corollary J1.4(ii);
the counts are: for $Q=2$, $j \mapsto 2j \bmod 32$ is a bijection from
$j \bmod 16$ onto the even residues mod 32; for $Q=3$, $3$ is a unit
mod 64; for $Q=4$, $4j \bmod 256$ takes each multiple of $4$ exactly
once as $j$ ranges mod 64. $\square$

**Lemma J3.2 (PROVED, a strengthening of F1.9(b) from F2.4).** Let
$h = 1$ (i.e. $R \in \{0,1,2\}$, $(Q,R) \ne (2,0)$). For every
$r \ne R$ and every prime power $q = p^a \Vert (n - r)$ with
$p \ge 5$, one has $q \le T$.

*Proof.* By Corollary F2.4 (at-least-one form), $q \le T$ or
$q \mid j$ (the only index below $h = 1$ is $0$). If $q \mid j$ then
$q \mid (n - r) - Qj = R - r$, but $0 < |R - r| \le 2 < 5 \le q$,
impossible. Hence $q \le T$. (F1.9(b) as filed states this only for
the prime $p > T$; the dichotomy gives the prime-power form.) $\square$

**Claim J3.3 (PROVED, label finiteness per fixed row).** (a) If
$h = 0$ ($R \ge 3$) and $(Q, R)$ is **fixed**, then only finitely many
$n$ satisfy the label bound F1.9(a) at all; in particular the row
contains only finitely many triples satisfying F1.9(a) and (LD3).
(b) If $h = 1$ and $R \ne 1$, the same holds with $(Q, R)$ fixed, by
Lemma J3.2 applied to the odd top $n - 1$ (here $r = 1 \ne R$).
(c) Consequently, for each **fixed** $Q$, the union of the rows
$R \in \{0, 2\}$ is finite by the label bounds alone (no EEES78
input; $T \le 2Q$ there), and every $h = 0$ row is finite once $R$ is
fixed; but for fixed $Q$ and $R \ge 3$ varying, $T = R + 2Q - 2$ is
unbounded and no finiteness follows. The remaining $h = 1$ case
$R = 1$ is finite per fixed $Q$ by the squared bound of Claim J3.4
($T = 2Q - 1$ is fixed there), not by the label bounds.

*Proof.* In both cases it suffices that the odd top $m = n - 1$ can
take only finitely many values. Every prime power $p^a \Vert m$ with
$p \ge 5$ is $\le T$: in case (a) by F1.9(a) directly; in case (b) by
Lemma J3.2. Hence every prime divisor of $m$ is $\le T$ or equal to
$3$. The $3$-exponent $e = v_3(m)$ (if $3 \mid m$, then $m$ is the
unique top divisible by $3$) is also bounded: the $3$-part of
$V_3(n)$ is $3^{e-1}$, and by F1.9(a) in case (a), resp. by
Corollary F2.4 in case (b), either $3^{e-1} \le T$, giving
$e \le 1 + \log_3 T$, or (case (b) only) $3^{e-1} \mid j$; but then
$3^{e-1} \mid \gcd(j, m) = \gcd(j, Qj + R - 1) = \gcd(j, R - 1) = 1$
since $R \in \{0, 2\}$, forcing $e = 1$. So $m$ has finitely many
possible prime divisors, each with bounded exponent: finitely many
$m$, hence finitely many $n$. $\square$

**Claim J3.4 (PROVED, monotonicity for the squared bound).** (a) In
an $h = 0$ row, $C(Qj + R, 3)$ is strictly increasing in $j$ while
$\Lambda_3(T)^2$ is constant, so if the squared inequality
$C(Qj+R,3) < \Lambda_3(T)^2$ fails at some $j_0$ it fails for all
$j \ge j_0$. Write $N_{\max}(T) = \max\{n : C(n,3) <
\Lambda_3(T)^2\}$ (script Section C certifies each value by
$C(N_{\max},3) < \Lambda_3(T)^2 \le C(N_{\max}+1,3)$); a
counterexample in the row has $n \le N_{\max}(T)$ and
$j \le j_{\mathrm{sq}} := \lfloor (N_{\max}(T) - R)/Q \rfloor$.
(b) In an $h = 1$ row, the ratio
$A(j) = (\Lambda_3(T) j)^2 / C(Qj + R, 3)$ is strictly decreasing in
$j$ for $j > R$; hence if the squared inequality fails at $j_0 > R$
it fails for all $j \ge j_0$, and the exact maximum
$j_{\mathrm{sq}} = \max\{j : C(Qj+R,3) < (\Lambda_3(T) j)^2\}$ is
certified by the two values at $j_{\mathrm{sq}}$ and
$j_{\mathrm{sq}} + 1$ (script Section C). A crude proved bound is
$j_{\mathrm{sq}} < 24 \Lambda_3(T)^2 / Q^3$ (from
$C(Qj,3) \ge (Qj)^3/24$ for $Qj \ge 4$).

*Proof of (b).* $A(j+1)/A(j) = ((j+1)/j)^2 \cdot C(n,3)/C(n+Q,3)$
with $n = Qj + R$. Now
$C(n+Q,3)/C(n,3) = \prod_{t=0}^{2} \frac{n + Q - t}{n - t}
\ge (1 + Q/n)^3$, since each factor is $1 + Q/(n-t) \ge 1 + Q/n$.
As $R < j$ (Euclidean division), $n < (Q+1)j$, so $Q/n >
\frac{Q}{(Q+1)j} \ge \frac{2}{3j}$ (as $Q \ge 2$). And
$(1 + \frac{1}{j})^{2/3} < 1 + \frac{2}{3j}$, because for $x > 0$,
$(1 + \frac{2x}{3})^3 - (1+x)^2 = \frac{x^2}{3} + \frac{8x^3}{27} > 0$
(expansion in the script's Section C sample range and in general by
the displayed identity), applied at $x = 1/j$. Chaining,
$(1 + Q/n)^3 > (1 + 1/j)^2$, so $A(j+1) < A(j)$. (Script Section C
also samples this on 20,000 fixed-seed draws, $0$ failures.) $\square$

**Claim J3.5 (COMPUTATION, with the closure deduction PROVED modulo
the standing inputs of Section 0).** For a fixed row $(Q,R)$, a
counterexample must satisfy the squared inequality (EEES form; the
sole exception $n = 8$ is incompatible with $j \ge 5001$). Hence the
row is **closed** (no counterexample in it, for any $j$) as soon as
either **(A)** $j_{\mathrm{sq}} \le 5000$ (contradicting the certified
per-pair frontier $j \ge 5001$), or **(B)** the row is $h = 0$ and
$N_{\max}(T) \le 10^6$ (contradicting the certified fact that (LD3)
has no solution with $n \le 10^6$). Exact values (script Section C;
$\Lambda_3$ and $N_{\max}$ values include $\Lambda_3(6) = 15$,
$N_{\max} = 12$; $\Lambda_3(8) = 105$, $41$; $\Lambda_3(10) = 315$,
$85$; $\Lambda_3(12) = 3465$, $417$; $T = 17$: $765765$, $15210$;
$T = 24$: $334639305$, $875861$; $T = 25$: $1673196525$, $2561033$):

*$h = 1$ rows* (criterion A; $j_{\mathrm{sq}}$): $(2,1)$: $6$ (row
void in the residual anyway, $n$ odd); $(2,2)$: $5$ (already closed);
$(3,0)$: $2$ (already closed); $(3,1)$: $50$; $(3,2)$: $48$ (already
closed); $(4,0)$: $21$ (already closed); $(4,1)$: $1033$ (row void
in the residual, $n$ odd); $(4,2)$: $1032$ (also disposed directly by
(LD3) on its three label candidates, F1.11 / V-F Section 5). **Every
$h = 1$ row at $Q \in \{2, 3, 4\}$ is closed.** Bonus, same test
(COMPUTATION): $(5,0), (5,1), (5,2)$ have $j_{\mathrm{sq}} = 529,
4762, 4762$ and $(6,0)$ has $2756$, all closed by (A); but
$(6,1), (6,2)$ and every $h = 1$ row at $Q \in \{7, 8\}$ have the
squared inequality **holding** at $j = 5001$, so criterion A does
not close them.

*$h = 0$ rows at $Q = 2$* (even $R$; odd $R$ gives $n$ odd, already
closed globally): $R = 4, 6, 8, 10, 12, 14$ closed by (A), with
$j_{\mathrm{sq}} = 4, 17, 38, 203, 1144, 1143$; $R = 16, 18, 20, 22$
closed by (B), with $N_{\max} = 15210, 108298, 108298, 875861$
(while $j_{\mathrm{sq}} = 7597, 54140, 54139, 437919$ exceeds
5000, so (A) alone would **not** close them). **First row not
closed: $(2, 24)$** ($T = 26$, $N_{\max} = 2561033$,
$j_{\mathrm{sq}} = 1280504$), where a counterexample would need
$j \in [499989, 1280504]$ (the lower end from $n = 2j + 24 > 10^6$).

*$h = 0$ rows at $Q = 3$*: $R = 3, \dots, 12$ closed by (A), with
$j_{\mathrm{sq}} = 12, 12, 26, 26, 136, 136, 764, 763, 763, 763$;
$R = 13, \dots, 20$ closed by (B), with $N_{\max} = 15210, 15210$,
$108298$ (four rows), $875861$ (two rows) (while $j_{\mathrm{sq}}$
reaches $5065$ already at $R = 13, 14$, so (A) alone would leave the
window $j \in [5001, 5065]$ there; (B) removes it, since
$n \le 15210 \le 10^6$). **First row not closed: $(3, 21)$**
($T = 25$, $N_{\max} = 2561033$, $j_{\mathrm{sq}} = 853670$), window
$j \in [333327, 853670]$.

*$h = 0$ rows at $Q = 4$* (even $R$; odd $R$ gives $n$ odd):
$R = 4, 6, 8, 10, 12$ closed by (A), with $j_{\mathrm{sq}} = 20, 102,
573, 572, 3799$; $R = 14, 16, 18$ closed by (B), with
$N_{\max} = 108298, 108298, 875861$. **First row not closed:
$(4, 20)$** ($T = 26$, $N_{\max} = 2561033$,
$j_{\mathrm{sq}} = 640253$), window $j \in [249996, 640253]$.

Remark (same criteria at general $Q$): criterion (B) as stated
closes every $h = 0$ row, at any $Q$, with $T = R + 2Q - 2 \le 24$
(equivalently $R \le 26 - 2Q$), because $N_{\max}(T) \le 10^6$ iff
$T \le 24$ ($\Lambda_3$ and $N_{\max}$ are nondecreasing in $T$,
with $N_{\max}(24) = 875861$ and $N_{\max}(25) = 2561033$); the
tables above are the $Q \in \{2, 3, 4\}$ instances the task asked
for, and Corollary J3.6's $Q \ge 7$ clause should be read with this
sharpening applied.

In every not-closed fixed row the residual is still **finite**
(Claim J3.3 plus the squared bound), confined to the displayed kind
of window $[\max(5001, \lfloor (10^6 - R)/Q \rfloor + 1),\
j_{\mathrm{sq}}]$ and to the $v_2$ classes of Claim J3.1 (at $Q = 3$,
additionally to $j \equiv R \pmod 2$, since $n = 3j + R$ must be
even). No row with $R$ unbounded is closed by these arguments: as
$R \to j$ also $T \to \infty$ and both criteria fail eventually.

**Corollary J3.6 (PROVED modulo Section 0, the combined picture per
small row).** After Claims J2.2, J3.1 and J3.5, a counterexample at
$i = 3$ must lie in one of: row $Q = 2$ with even $R \ge 24$; row
$Q = 3$ with $R \ge 21$; row $Q = 4$ with even $R \ge 20$; row
$Q = 5$ with $R \ge 3$ (its $h = 1$ rows are closed by Claim J3.5's
bonus); row $Q = 6$ with $R \ge 1$ except $R = 0$ closed, i.e.
$R \ge 1$; or any row $Q \ge 7$ (with the $v_2$ stratification of
Claim J2.2, the label conditions of F1.9 / F2.14, (LD3), (N1), (N2),
$j \ge 5001$, $n > 10^6$ throughout). In particular the Cycle 2
residual class (F1.11 / F2.14) is now empty in **all** rows
$(Q, R)$ with $Q \le 4$ and $R$ below the displayed thresholds, a
region that Cycle 2 left open outside the five rows
$\{(2,0), (2,2), (3,0), (3,2), (4,0)\}$. This is a reduction of the
residual class, **not** a closure of $i = 3$: $R$ and $Q$ remain
unbounded in general.


## 4. J.4: Del Pin-spirit comparisons

### 4(a). Settling the GAP in F1.14

The $V_3$-refined comparison closes the triple $(n,3,j)$ iff
$V_3(n) > C(j,3)$ (a counterexample requires $V_3(n) \mid C(j,3)$ by
(N2), hence $V_3(n) \le C(j,3)$). Relative to the finite reduction,
the pair $(3,j)$ is closed **by this comparison** iff every
$n \in [2j, N(3,j)]$ has $V_3(n) > C(j,3)$.

**Claim J4.1 (PROVED, the general behaviour for $j \ge 19$).** For
every $j \ge 19$ there exists $n \in [2j, N(3,j)]$ with
$V_3(n) \le C(j,3)$; explicitly, $n = 2^a$ with
$a = \lceil \log_2 2j \rceil$ works. Hence the refined comparison
closes no pair $(3, j)$ with $j \ge 19$.

*Proof.* Let $a$ be as stated, so $2j \le n = 2^a < 4j$ and $a \ge 6$.
Since $v_2(n) = a$, $v_2(n-1) = 0$, $v_2(n-2) = 1$, Claim J1.2's
bookkeeping gives $v_2(C(n,3)) = a$, and therefore
$$V_3(n) = \frac{C(2^a, 3)}{2^a}
= \frac{(2^a - 1)(2^a - 2)}{6} = \frac{(2^a-1)(2^{a-1}-1)}{3}
< \frac{(4j)(2j)}{3} = \frac{8}{3} j^2.$$
For $j \ge 19$, $(j-1)(j-2) - 16j = j^2 - 19j + 2 \ge 2 > 0$, i.e.
$\frac{8}{3} j^2 \le \frac{j(j-1)(j-2)}{6} = C(j,3)$; hence
$V_3(n) < C(j,3)$, in particular $V_3(n) \le C(j,3)$. It remains
that $n \le N(3,j)$, i.e. $C(n,3) < C(2j,6)$. Since $n < 4j$ it
suffices that $C(4j,3) \le C(2j,6)$, which holds for $j \ge 10$ by
crude bounds: $C(2j,6) > (2j-5)^6/720$ (six factors, each
$\ge 2j - 5$, one equal and the rest larger) and
$C(4j,3) < (4j)^3/6$; and $(2j-5)^2 \ge 20j$ for $j \ge 10$
(equivalently $4j^2 - 40j + 25 \ge 25 > 0$), so
$(2j-5)^6 \ge 8000 j^3$ and
$C(2j,6) > \frac{8000}{720} j^3 = \frac{100}{9} j^3 >
\frac{96}{9} j^3 = \frac{(4j)^3}{6} > C(4j,3)$.
(Script Section D verifies the witness, including
$C(n,3) < C(2j,6)$ and the closed form of $V_3(2^a)$, for all
$19 \le j \le 2000$.) $\square$

**Claim J4.2 (COMPUTATION for $5 \le j \le 18$; the F1.14 sentence
is FALSE).** Exact enumeration over $[2j, N(3,j)]$ (script Section D)
gives, with $m(j) := \min_{2j \le n \le N(3,j)} V_3(n)$:

| $j$ | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| $C(j,3)$ | 10 | 20 | 35 | 56 | 84 | 120 | 165 | 220 | 286 | 364 | 455 | 560 | 680 | 816 |
| $N(3,j)$ | 11 | 18 | 27 | 37 | 49 | 62 | 77 | 94 | 112 | 132 | 153 | 176 | 201 | 227 |
| $m(j)$ | 15 | 35 | 35 | 35 | 51 | 155 | 155 | 155 | 155 | 155 | 155 | 155 | 187 | 651 |
| attained at $n$ | 10 | 16 | 16 | 16 | 18 | 32 | 32 | 32 | 32 | 32 | 32 | 32 | 34 | 64 |
| comparison closes pair? | yes | **yes** | no | no | no | **yes** | no | no | no | no | no | no | no | no |

Hence, among $j \ge 5$, the refined comparison closes the full pair
on the finite-reduction interval exactly for $j \in \{5, 6, 10\}$
in the computed range, and (by Claim J4.1) for no $j \ge 19$; so
exactly for $j \in \{5, 6, 10\}$ overall (with $j = 5$ also being
Del Pin's unrefined case, F1.12). The failing witnesses are visible
in the table: $(16, 7)$ with $V_3(16) = 35 = C(7,3)$ (the F1.14
sharpness example) already blocks $j = 7$, and likewise $j = 8$;
$n = 32$ with $V_3(32) = 155$ blocks $11 \le j \le 16$; $n = 34$
blocks $j = 17$; $n = 64$ blocks $j = 18$; and the power-of-two
family of Claim J4.1 blocks every $j \ge 19$. **Consequently the
final sentence of Claim F1.14 as filed ("the refined comparison
does not by itself close any full pair $(3,j)$ with $j > 5$") is
FALSE**: $j = 6$ and $j = 10$ are counterexamples to the sentence.
This does not disturb any downstream Cycle 2 claim (V-F already
noted that no claim depends on the sentence, and both pairs are
closed by (LD3) per pair in any case); what is new is the *method*:
these two pairs are closed by a pure size comparison, and Claim
J4.4 below strengthens that to all $n \ge 2j$ with no EEES78 input.
(The pair $(3,4)$ is outside this discussion: its interval
$[8, N(3,4)] = [8, 6]$ is empty.)

### 4(b). A further comparison of my own design: the $2^{v_2} \le n$ tail bound

**Claim J4.3 (PROVED, the tail comparison).** For every $n \ge 3$,
$2^{v_2(C(n,3))} \le n$; hence
$$V_3(n) \;\ge\; \frac{C(n,3)}{n} \;=\; \frac{(n-1)(n-2)}{6},$$
and the triple $(n,3,j)$ is not a counterexample whenever
$(n-1)(n-2)/6 > C(j,3)$. Let $t(j)$ be the least $n$ with
$(n-1)(n-2) > 6 C(j,3)$; the comparison therefore closes, for each
$j$, the whole tail $n \ge t(j)$ with **no EEES78 input and no
finite reduction**. Values (script Section E): $t(6) = 13$,
$t(7) = 17$, $t(8) = 20$, $t(10) = 29$, $t(20) = 85$,
$t(100) = 987$; asymptotically $t(j) \sim j^{3/2}$, well below
$N(3,j) \sim 0.81 j^2$.

*Proof.* By Legendre's formula as in Lemma A1.13's source (P-A1),
$v_2(C(n,3)) = \sum_{k \ge 1} (\lfloor n/2^k \rfloor -
\lfloor 3/2^k \rfloor - \lfloor (n-3)/2^k \rfloor)$; each summand is
$\lfloor x + y \rfloor - \lfloor x \rfloor - \lfloor y \rfloor \in
\{0, 1\}$ for $x = 3/2^k$, $y = (n-3)/2^k$, and summands with
$2^k > n$ vanish, so $v_2 \le \#\{k : 2^k \le n\} =
\lfloor \log_2 n \rfloor$, i.e. $2^{v_2} \le n$. The rest is
substitution. $\square$

**Claim J4.4 (PROVED, what the tail comparison does and does not
close).** (a) Used uniformly at the left endpoint $n = 2j$, the tail
comparison closes the pair $(3,j)$ for all $n \ge 2j$ iff $j \le 5$:
the condition is $2(2j - 1) > j(j - 2)$ (after cancelling
$j - 1 > 0$), i.e. $j^2 - 6j + 2 < 0$, i.e. $j \le 5$; so as a
uniform comparison it **does not** improve on Del Pin's unrefined
range, an honest negative. (b) Used as a tail bound combined with
an exact-$v_2$ check on the finite head $[2j, t(j))$ (the *hybrid
comparison*), it closes the pairs $j = 6$ and $j = 10$ for **all**
$n \ge 2j$, unconditionally: for $j = 6$ the head is the single
value $n = 12$ with $V_3(12) = 55 > 20 = C(6,3)$, and every
$n \ge 13 = t(6)$ is closed by Claim J4.3; for $j = 10$ the head is
$n = 20, \dots, 28$ with $V_3$ values $285, 665, 385, 1771, 253,
575, 325, 2925, 819$, all $> 120 = C(10,3)$ (script Section E), and
every $n \ge 29 = t(10)$ is closed by Claim J4.3. (c) The hybrid
closes no other pair. By construction the hybrid closes the pair
$(3,j)$ iff every $n$ in the head $[2j, t(j))$ has $V_3(n) > C(j,3)$
(the tail $n \ge t(j)$ being automatic). For $7 \le j \le 18$,
$j \ne 10$, the minimum $m(j) \le C(j,3)$ of Claim J4.2's table is
attained at an $n$ with $n < t(j)$ (attained at $n = 16, 16, 18$ for
$j = 7, 8, 9$, against $t(j) = 17, 20, 24$; at $n = 32$ for
$11 \le j \le 16$, against $t(j) \ge t(11) = 33$; at $n = 34, 64$
for $j = 17, 18$, against $t(j) = 66, 72$; all asserted in script
Section E), so that $n$ lies in the head and blocks the hybrid.
For $j \ge 19$, the Claim J4.1 witness $n = 2^a$ satisfies
$n < 4j$, and $4j < t(j)$ for all $j \ge 19$: indeed
$t(j) > 4j$ iff the defining inequality fails at $n = 4j$, i.e. iff
$D(j) := 6 C(j,3) - (4j-1)(4j-2) =
j(j-1)(j-2) - (16j^2 - 12j + 2) = j^3 - 19j^2 + 14j - 2$ is
positive; and $D(19) = 264 > 0$ with
$D'(j) = 3j^2 - 38j + 14$ positive at $j = 19$ ($375$) and
increasing thereafter ($D''(j) = 6j - 38 > 0$), so $D(j) > 0$ for
all $j \ge 19$. Hence the witness lies in the head $[2j, t(j))$
and, having $V_3(n) \le C(j,3)$, blocks the hybrid there too.
(Script Section E asserts $D(j) > 0$ for $19 \le j \le 2000$ and
$t(j) > 4j$ for $19 \le j < 200$.)

**Claim J4.5 (PROVED, a second tested comparison, negative).** The
single-top bound $V_3(n) \ge R(n-1)/3$ (where $R(m)$ is the relevant
part of $m$; proof: $V_3(n) = U_0 U_1 U_2 3^{e-1} \ge U_1 3^{e-1}$,
and $R(n-1)$ is $U_1$ times $3^{v_3(n-1)}$ if $v_3(n-1) \ge 2$, in
which case $e = v_3(n-1)$ and $3^{e-1} = 3^{v_3(n-1)}/3$, and is
$U_1$ otherwise) pushed through (N2) gives only
$R(n-1) \le 3 C(j,3)$, i.e. with $R(n-1) \ge (n-1)/3$ the bound
$n \le \frac{3}{2} j (j-1)(j-2) + 1$, of order $j^3$: strictly
weaker than F1.8's splitting bound $n \le 3j(j-1) + 1$ for $j > 3$,
and it closes no pair and no row. It is recorded as a tested
comparison that does **not** help, in the spirit of the campaign's
honest-negative convention.

## 5. Closing statement for Cluster J

**Claim J5.1 (summary; labels as in the claims).**

*Proved in this file, beyond Cycle 2 (all modulo the standing
inputs of Section 0 where stated):*
1. Exact $v_2$ theory (J1.1 to J1.3): borrow and digit-sum formulas;
   $v_2 \ge 4$ iff $16 \mid n$ or $16 \mid (n-2)$ ($n$ even), iff
   $32 \mid (n-1)$ ($n$ odd); for $v \ge 2$ exactly five classes
   $\{0, 1, 2, 2^v, 2^v + 2\}$ mod $2^{v+1}$, density $5/2^{v+1}$;
   the exceptional counts $2$ ($v = 0$) and $3$ ($v = 1$).
2. $Q$-stratification (J2.1, J2.2): $\rho(Q, \cdot)$ strictly
   decreasing to the unattained infimum $Q^3$;
   $v_{\min}(Q) = \lfloor 3 \log_2 Q \rfloor + 1$ for every
   $Q \ge 2$, confirming $4, 5, 7$ at $Q = 2, 3, 4$, best possible
   from (N2) uniformly in $j$; residual densities per row (J2.3).
3. $v_2$ congruences on $j$ per small row (J3.1); the prime-power
   strengthening of F1.9(b) (J3.2); label finiteness per fixed row
   (J3.3); monotonicity of the squared bound (J3.4).
4. Row closures (J3.5, J3.6): all $h = 1$ rows at $Q \in \{2,3,4\}$;
   $h = 0$ rows at $Q = 2$ (even $R \le 22$), $Q = 3$ ($R \le 20$),
   $Q = 4$ (even $R \le 18$), by the squared bound intersected with
   the certified frontiers $j \le 5000$ and $n \le 10^6$; bonus
   closures at $Q = 5$ ($R \in \{0,1,2\}$) and $(6, 0)$. First open
   rows $(2, 24)$, $(3, 21)$, $(4, 20)$ with explicit finite
   windows.
5. F1.14's GAP settled (J4.1, J4.2): the refined comparison closes
   the full pair exactly at $j \in \{5, 6, 10\}$; its final sentence
   is FALSE, with $j = 6, 10$ as counterexamples; for every
   $j \ge 19$ an explicit power-of-two $n$ blocks the comparison.
6. A new comparison (J4.3, J4.4): $V_3(n) \ge (n-1)(n-2)/6$; the
   hybrid with exact $v_2$ on the head closes $(3,6)$ and $(3,10)$
   for all $n$ with no EEES78 input; uniformly at $n = 2j$ it
   closes nothing beyond $j \le 5$ (honest negative), and the
   single-top comparison of J4.5 closes nothing (honest negative).

*Reduced:* the $i = 3$ residual class of F1.11 / F2.14 is reduced
to the rows listed in Corollary J3.6 (in particular, no residual
triple has $Q \le 4$ with $R$ below the J3.5 thresholds), with
per-row $v_2$ densities as in J2.3 and finite windows in every
fixed row.

*Still OPEN, explicitly:* the residual class in rows with
$R$ or $Q$ above the J3.5 thresholds (first instances
$(2,24)$, $(3,21)$, $(4,20)$, and all sufficiently large rows);
(H3) in general; $i = 3$ in general. **$i = 3$ is not closed,
(H3) is not proved, and $\#699$ is not claimed solved.** No
comparison in this file closes any class beyond what is stated:
the $v_2$ stratification is a density restriction, the refined
comparison closes exactly three pairs, and the row closures of
Section 3 rest on the certified (LD3) frontiers, not on $v_2$
alone.

## 6. Verification log

All numbers above are outputs of `proofs/P-J1_checks.py`
(under 1 s, stdlib only, exact arithmetic), whose sections assert their
own headline values:

* Section A: $v_2(C(n,3))$ against the digit-sum formula and a
  direct binary borrow counter, $3 \le n \le 5000$; the class lists
  for $0 \le v \le 7$ (exactly the lists of Claim J1.3); the
  $v_2 \ge 4$ parity forms for $n \le 20000$.
* Section B: $\rho(Q,j)$ strictly decreasing and $> Q^3$ in exact
  `Fraction` arithmetic ($2 \le Q \le 8$, $j < 400$), the closed
  form of $\rho$, and the $v_{\min}$ table $Q = 2..16$ with
  $2^{v_{\min}} > Q^3 \ge 2^{v_{\min} - 1}$ asserted.
* Section C: $\Lambda_3$ spot values; $N_{\max}(T)$ certificates
  $C(N_{\max},3) < \Lambda_3(T)^2 \le C(N_{\max}+1,3)$ for
  $3 \le T \le 30$; the full $j_{\mathrm{sq}}$ / $N_{\max}$ tables
  for $Q = 2, 3, 4$ with the closure thresholds asserted
  ($Q=2$: $N_{\max} \le 10^6$ exactly for even $R \le 22$;
  $Q=3$: exactly for $R \le 20$; $Q=4$: exactly for even
  $R \le 18$); $h = 1$ exact $j_{\mathrm{sq}}$ values certified by
  `ok(jmax)` and `not ok(jmax+1)`; `ok(5001) = True` asserted for
  $(6,1), (6,2)$ and $Q \in \{7,8\}$; the Claim J3.4 monotonicity
  sample (20,000 fixed-seed draws, $0$ failures); the first-open-row
  windows.
* Section D: the $(16,7)$ sharpness witness; the full
  classification table of Claim J4.2 for $5 \le j \le 18$
  (asserting the closing set is exactly $\{5, 6, 10\}$, with minima
  $(51, 18)$ at $j = 9$ and $(187, 34)$ at $j = 17$); the
  power-of-two witness verified for all $19 \le j \le 2000$.
* Section E: $t(j)$ values; the uniform-at-$2j$ equivalence with
  $j \le 5$ for $j < 60$; the head-placement assertions of Claim
  J4.4(c) (minimisers $< t(j)$ for $7 \le j \le 18$, $j \ne 10$;
  $D(j) > 0$ for $19 \le j \le 2000$; $t(j) > 4j$ for
  $19 \le j < 200$); the hybrid head values for $j = 6$
  ($n = 12$: $V_3 = 55$) and $j = 10$ ($n = 20..28$, values as in
  Claim J4.4(b), all $> 120$).
* Section F: F1.13's thresholds $n_0(j,4)$ and $n_0(j,5)$
  re-verified exactly.

Adversarial self-check note: the sign of the polynomial
$D(j) = j^3 - 19j^2 + 14j - 2$ in Claim J4.4(c) (where a sign error
would reverse the conclusion $t(j) > 4j$) was checked three ways:
by the expansion $6C(j,3) - (4j-1)(4j-2)$, by exact values
($D(17) = -342$, $D(18) = -74$, $D(19) = 264$, so the threshold is
exactly $j = 19$), and by the script's direct assertion
$t(j) > 4j$ for $19 \le j < 200$.
