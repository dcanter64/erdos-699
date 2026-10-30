# P-F2: Erdős #699 at $i=3$: Price's Proposition 4.1 specialised, the SPLIT-odd case **closed**, SPLIT-even cut down, a $V_3$-refined Del Pin comparison, and the exact reach of (LD3) per pair

**Prover F2 (independent, Cycle 2).** This document was written
independently of prover F1's document (`proofs/P-F1.md` was not read).
Inputs used: the established ground truth listed in §0; the Cycle 1
record in `strategies/S8.md` §3, §3.5 and `proofs/P-A2.md` §4 (the
system (LD3), conditions (N1), (N2), and the SPLIT-odd / SPLIT-even
configurations of Statement A2.28); the Del Pin entry of
`EXTERNAL_CLAIMS_2026-10-29.md`; Price's manuscript
(`~/workspace/user/files/Liam_699_partial.pdf`) for Task 1; and the
cap-20,000 sweep file `erdos-699/pairpass_20000.json` for Task 4.
Every computation reported was run by this prover in Python standard
library exact arithmetic; the computations are described in §6 in
enough detail to reproduce them.

**Headline.** One Cycle 1 open case is closed here: **(SPLIT-odd)
is impossible** (Theorem F2.7, PROVED), via the $i=3$ case of Price's
Proposition 4.1, which is proved self-containedly in §1 (only
Kummer's criterion is used; no EEES78 input). The same proposition
cuts (SPLIT-even) down to an explicit residual class (§3, OPEN in
general). Independently, a computation in §4 shows that (LD3)
*alone* has no solution in the finite-reduction range of **every**
pair $(3,j)$ with $5 \le j \le 5000$; combined with the finite
reduction this closes every such pair for all $n$. **$i=3$ in
general, and hence #699, is NOT proved here:** pairs $(3,j)$ with
$j \ge 5001$ remain open outside the ranges of §5, and $(H_3)$ is
not proved.

## 0. Setting and standing inputs

For $1 \le i < j \le n/2$, $V_i(n)$ is the part of $\binom ni$
supported on primes $\ge i$; a **counterexample** at $(n,i,j)$ has
$\gcd(V_i(n), \binom nj) = 1$. Throughout, $i = 3$, so $V_3(n)$ is
the odd part of $\binom n3$: writing
$C(n,3) = U_0U_1U_2 \cdot 3^{e} / 6$ is avoided in favour of the exact
decomposition used in P-A2 §4.3,

$$V_3(n) = U_0U_1U_2 \cdot 3^{\,e-1}, \qquad
e = v_3\!\big(n(n-1)(n-2)\big),$$

where $U_r$ is the part of $n-r$ supported on primes $\ge 5$
($r \in \{0,1,2\}$); the $U_r$ are pairwise coprime, and for a prime
$p \ge 5$ the full $p$-part of $V_3(n)$ is exactly the prime power
$p^{v_p(n-r)} \Vert (n-r)$ for the unique $r$ with $p \mid n-r$.
Standing inputs, all Cycle 1 verified:

* **Key lemma.** $d \mid \binom ni$ and $\gcd(d, \binom nj) = 1$
  imply $d \mid \binom ji$; in particular a counterexample at
  $(n,3,j)$ satisfies **(N2)** $V_3(n) \mid \binom j3$.
* **(N1).** A counterexample satisfies
  $\gcd(\binom n2, \binom nj) = 2^a 3^b$.
* **(LD3).** For $m \in \{n, n-1, n-2\}$, let $R(m)$ be the product
  of the exact prime powers $q = p^a \Vert m$ with $p \ge 5$ (any
  $a \ge 1$) or $p = 3$, $a \ge 2$. A counterexample satisfies
  (LD3): for each such $q \mid R(n-r)$, $j \bmod q \le r$;
  equivalently $R(n) \mid j$, $R(n-1) = X_0X_1$ with $X_0 \mid j$,
  $X_1 \mid j-1$, and $R(n-2) = Y_0Y_1Y_2$ with $Y_s \mid j-s$.
* **Finite reduction.** A counterexample with $(n,3)$
  EEES78-non-exceptional satisfies
  $\binom n3 < \binom{2j}{2(j-3)} = \binom{2j}{6}$, i.e.
  $n \le N(3,j) := \max\{n : \binom n3 < \binom{2j}{6}\}$
  (P-A2, Lemma A2.2(b)). The only EEES78 exception pair with
  $i = 3$ is $(8,3)$, which admits no $j \ge 5$.
* **Closed already:** $j \le 6$ for all $n$ (P-A2, Lemmas
  A2.17–A2.19; $j = 4$ also by Price's $j \le 3i/2$ range, $(3,5)$
  also by the boundary family); $n = 2j$ for all $j$ (Price,
  Proposition 3.3); the sweep's statement that no counterexample
  has $n \le 20{,}000$.
* **(H3)** is the statement that (LD3) has no solution with
  $7 \le j \le n/2$; **(SPLIT-odd)** is the configuration
  $n$ odd, $v_3(n) = 1$, $j = n/3$, with the $r = 1, 2$ clauses of
  (LD3) holding by distribution; **(SPLIT-even)** is the
  configuration $n$ even, $R(n) \mid j$, with $R(n-1)$ and
  $R(n-2)$ splitting by genuine distribution among
  $j, j-1$ resp. $j, j-1, j-2$ (P-A2, Statement A2.28).

## 1. Task 1: Price's Proposition 4.1, extracted and specialised to $i=3$

### 1.1 Extraction

**Claim F2.1 (extraction from the manuscript) — PROVED as a
transcription (see the garbling note).** Section 4 of Price's
manuscript ("A Euclidean-division bound") states, verbatim in
substance:

> For $T \ge 1$, define
> $\Lambda_i(T) = \prod_{q \ge i,\ q \text{ prime}}
> q^{\lfloor \log_q T \rfloor}$, $\Lambda_i(0) = 1$.
> Thus $\Lambda_i(T)$ is the part of $\mathrm{lcm}(1, \dots, T)$
> supported on primes at least $i$.
>
> **Proposition 4.1.** Suppose $1 \le i < j \le n/2$ and no prime
> $q \ge i$ divides both $\binom ni$ and $\binom nj$. Write
> $n = Qj + R$, where $Q = \lfloor n/j \rfloor \ge 2$ and
> $0 \le R < j$, and put
> $$T = R + (Q-1)(i-1), \qquad
> h = \max\Big\{0, \Big\lceil \tfrac{i-R}{Q} \Big\rceil\Big\}.$$
> Then $V_i(n) \mid \Lambda_i(T)\, \binom{j}{h}$, and consequently
> $\binom ni < \big(\Lambda_i(T)\, \binom{j}{h}\big)^2$.

The proof in the manuscript: with $c = n - j = (Q-1)j + R$, Lemma
2.1 of the manuscript supplies, for each full $q$-part $q^a$ of
$V_i(n)$, nonnegative $r, s$ with $r + s < i$ and $q^a \mid j - r$,
$q^a \mid c - s$; hence $q^a \mid E := R + (Q-1)r - s$. If
$E \ne 0$ then $|E| \le \max\{R + (Q-1)(i-1),\ i-1-R\} \le T$, so
$q^a \mid \Lambda_i(T)$. If $E = 0$ then $s = R + (Q-1)r$ and
$R + Qr < i$, whence $0 \le r < h$ and $q^a \mid j - r$; the product
of all such parts divides $j(j-1)\cdots(j-h+1)$, and since every
prime involved exceeds $h$ it divides $\binom{j}{h}$. The
consequence follows from $V_i(n)^2 > \binom ni$ (EEES78,
non-exceptional case; exceptions are discharged by the
manuscript's Lemma 1.3).

*Garbling note (exact).* `pdftotext` (both `-layout` and `-raw`)
renders the binomial coefficients as stacked glyphs and drops the
large brackets: the divisibility prints as
"$V_i(n) \mid \Lambda_i(T)\ h j$" and the consequence with the
exponent $2$ displaced onto the following line. The reading above
was recovered from the word-position (`-bbox`) data: in the
divisibility, $j$ sits directly above $h$ inside a binomial
bracket after $\Lambda_i(T)$; in the consequence, a matched pair
of large parentheses encloses $\Lambda_i(T)\binom{j}{h}$ and
carries the superscript $2$ — this is also the only reading under
which the manuscript's final sentence ("Theorem 1.2 therefore
gives $\binom ni < V_i(n)^2$, and the stated inequality follows")
is arithmetically correct, since $V_i(n) \le \Lambda_i(T)
\binom{j}{h}$ yields $\binom ni < (\Lambda_i(T)\binom{j}{h})^2$
and not $\Lambda_i(T)\binom{j}{h}^2$. The symbol in $h$'s
definition is the ceiling (the proof's remark "$h \le \lceil
i/2 \rceil$ for $i \ge 2$" confirms the ceiling, and the
$E = 0$ analysis in §1.2 below independently forces
$h = \max\{0, \lceil (i-R)/Q \rceil\}$). Everything else in the
statement — the definition of $\Lambda_i$, $T$, $Q$, $R$, and all
hypotheses — extracted cleanly. What could **not** be read from
`pdftotext` alone, without the position data, is exactly the
placement of $\binom{j}{h}$ and of the exponent $2$; no other part
of §4 of the manuscript was garbled.

### 1.2 The $i=3$ case, proved self-containedly

For the applications below only $i = 3$ is needed, and for $i = 3$
the proposition is proved here from Kummer's criterion alone, so
that no part of §§2–3 rests on an unexamined external proof. The
single ingredient is the $i = 3$ case of the manuscript's Lemma
2.1(b).

**Lemma F2.2 (localisation at $i=3$) — PROVED.** Let
$3 < j \le n/2$, let $p \ge 3$ be prime with
$a := v_p(\binom n3) \ge 1$, and suppose $p \nmid \binom nj$.
Put $c = n - j$. Then there exist $r, s \ge 0$ with $r + s < 3$
such that $p^a \mid j - r$ and $p^a \mid c - s$; indeed one may
take $r = j \bmod p^a$ and $s = c \bmod p^a$ (least residues).

*Proof.* There is a unique $t \in \{0,1,2\}$ with $p^a \mid n - t$:
for $p \ge 5$, $a = v_p(n(n-1)(n-2))$ (as $p \nmid 6$), $p$ divides
exactly one of the three consecutive factors (two differ by
$\le 2 < p$), and that factor has $p$-valuation exactly $a$; for
$p = 3$, exactly one factor is divisible by $3$, it has valuation
$a + 1 = v_3(n(n-1)(n-2))$, and $3^a$ divides it. Since
$0 \le t \le 2 < 3 \le p \le p^a$, the least residue of $n$
modulo $p^a$ is $t$. By Kummer, $v_p(\binom nj) = 0$ iff $j$ is
digitwise $\le n$ in base $p$, i.e. iff at every digit position
the digits of $j$ and $c$ sum to the digit of $n$ with no carry.
Summing the lowest $a$ digit positions gives
$r + s = \sum_{e<a} n_e p^e = n \bmod p^a = t < 3$, where $r, s$
are the least residues of $j, c$ modulo $p^a$. By definition
$p^a \mid j - r$ and $p^a \mid c - s$. $\square$

**Theorem F2.3 (Proposition 4.1 at $i=3$) — PROVED.** Suppose
$(n, 3, j)$ is a counterexample, $3 < j \le n/2$. Write
$n = Qj + R$ with $Q = \lfloor n/j \rfloor \ge 2$, $0 \le R < j$,
and put
$$T = R + 2(Q-1), \qquad h = \max\{0, \lceil (3-R)/Q \rceil\}
\in \{0, 1, 2\}.$$
Then $V_3(n) \mid \Lambda_3(T)\, \binom{j}{h}$, where
$\Lambda_3(T) = \prod_{q \ge 3} q^{\lfloor \log_q T \rfloor}$
($\Lambda_3(0) = \Lambda_3(1) = \Lambda_3(2) = 1$,
$\Lambda_3(3) = \Lambda_3(4) = 3$, $\Lambda_3(5) =
\Lambda_3(6) = 15$).

*Proof.* Let $p^a$ be a full prime-power part of $V_3(n)$
($p \ge 3$, $a \ge 1$). Since the triple is a counterexample,
$p \nmid \binom nj$, so Lemma F2.2 gives $r, s \ge 0$,
$r + s \le 2$, with $p^a \mid j - r$ and $p^a \mid c - s$, where
$c = n - j = (Q-1)j + R$. Hence
$p^a \mid (c - s) - (Q-1)(j - r) = E$, where
$E := R + (Q-1)r - s$.

*Case $E \ne 0$.* From $r + s \le 2$: the maximum of $E$ is
$R + 2(Q-1) = T$ (at $r = 2$, $s = 0$) and the minimum is
$R - 2$ (at $r = 0$, $s = 2$), so
$|E| \le \max\{T, |R - 2|\} = T$, since
$T = R + 2Q - 2 \ge R + 2 > |R - 2|$ for $Q \ge 2$. Since
$T \ge 2(Q-1) \ge 2$ and
$p^a \mid E \ne 0$, $p^a \le |E| \le T$, which is exactly
$p^a \mid \Lambda_3(T)$ (the $p$-part of $\Lambda_3(T)$ is
$p^{\lfloor \log_p T \rfloor} \ge p^a$ iff $p^a \le T$).

*Case $E = 0$.* Then $s = R + (Q-1)r$ and $r + s = R + Qr \le 2$,
so $Qr < 3 - R$. If $R \ge 3$ this is impossible, and indeed
$h = 0$ then. If $R \le 2$ it gives $r \le h - 1$, i.e.
$0 \le r < h$: for if $(3-R)/Q$ is an integer $m$, then
$Qr < 3 - R = Qm$ gives $r < m = h$; otherwise
$r < (3-R)/Q$ gives $r \le \lfloor (3-R)/Q \rfloor = h - 1$.
And $p^a \mid j - r$.

Now assemble. The full parts $p^a$ are pairwise coprime. Let
$P_\Lambda$ be the product of the parts in Case $E \ne 0$ and
$P_0$ the product of those in Case $E = 0$, so
$V_3(n) = P_\Lambda P_0$. Each part of $P_\Lambda$ divides
$\Lambda_3(T)$, so $P_\Lambda \mid \Lambda_3(T)$. Each part of
$P_0$ divides one of $j, j-1, \dots, j-h+1$ ($h \le 2$ factors;
$j - r \ge j - 1 \ge 1$ as $j \ge 7$ in the open range, and in
any case $j - r > 0$ since $r \le 2 < j$), so
$P_0 \mid j(j-1)\cdots(j-h+1) = h!\binom{j}{h}$; every prime
dividing $P_0$ is $\ge 3 > h$ (as $h \le 2$), so
$\gcd(P_0, h!) = 1$ and $P_0 \mid \binom{j}{h}$. Since
$\gcd(P_\Lambda, P_0) = 1$, $V_3(n) \mid \Lambda_3(T)
\binom{j}{h}$. $\square$

**Corollary F2.4 (per-part dichotomy) — PROVED.** Under the
hypotheses of Theorem F2.3, every full prime-power part $p^a$ of
$V_3(n)$ satisfies exactly one of: **(i)** $p^a \le T$ (in fact
$p^a \mid \Lambda_3(T)$); or **(ii)** $p^a \mid j - r$ for some
$0 \le r < h$. In particular, if $h \le 1$ — which holds for
every $(Q, R)$ except $(2, 0)$ — every part satisfies
$p^a \mid j$ or $p^a \le T$. For $p \ge 5$ the part $p^a$ is the
relevant prime power of the unique $n - r_0$ divisible by $p$,
so the dichotomy applies verbatim to the prime powers in (LD3);
for $p = 3$ it applies to $3^{e-1}$, one factor of $3$ below the
(LD3) prime power $3^e$ when $e \ge 2$.

*Specialisation table* ($i = 3$; $V = V_3(n)$):

| $(Q, R)$ | $T$ | $h$ | conclusion |
|---|---|---|---|
| $(2, 0)$ ($n = 2j$) | $2$ | $2$ | $V \mid \binom j2$ |
| $(2, 1)$ | $3$ | $1$ | $V \mid 3j$ |
| $(2, 2)$ | $4$ | $1$ | $V \mid 3j$ |
| $(2, R)$, $R \ge 3$ | $R + 2$ | $0$ | $V \mid \Lambda_3(R+2)$ |
| $(3, 0)$ ($n = 3j$) | $4$ | $1$ | $V \mid 3j$ |
| $(3, 1)$ | $5$ | $1$ | $V \mid 15j$ |
| $(3, 2)$ | $6$ | $1$ | $V \mid 15j$ |
| $(3, R)$, $R \ge 3$ | $R + 4$ | $0$ | $V \mid \Lambda_3(R+4)$ |
| $(Q \ge 4, 0)$ | $2Q - 2$ | $1$ | $V \mid \Lambda_3(2Q-2)\, j$ |
| $(Q \ge 4, 1)$ | $2Q - 1$ | $1$ | $V \mid \Lambda_3(2Q-1)\, j$ |
| $(Q \ge 4, 2)$ | $2Q$ | $1$ | $V \mid \Lambda_3(2Q)\, j$ |
| $(Q \ge 4, R \ge 3)$ | $R + 2Q - 2$ | $0$ | $V \mid \Lambda_3(R + 2Q - 2)$ |

Note the $(2,0)$ row sharpens (N2) at $n = 2j$
($\binom j2 < \binom j3$ for $j > 5$); that case is already
closed by Price's Proposition 3.3, so the sharpening is a
consistency check, not a new closure. The decisive rows are
$(3,0)$, used in §2, and the $h \le 1$ dichotomy, used in §3.
This is the labelled strengthening the Van Doorn–Rocca diagnosis
calls for: Proposition 4.1 retains, for each prime power, the
pair $(r, s)$ recording which of $j$ and $c = n - j$ it divides,
where (LD3) retains only the lowest-digit shadow in $n$.

**Computation F2.5 (verification of Lemma F2.2 and Corollary
F2.4) — COMPUTATION.** On $4000$ seeded random pairs
($20 \le n \le 3000$, $7 \le j \le n/2$), for every prime
$3 \le p \le 59$ with $v_p(\binom n3) \ge 1$ and
$v_p(\binom nj) = 0$ ($840$ instances), the $r, s$ of Lemma F2.2
exist with $r + s < 3$, and the dichotomy of Corollary F2.4
(with $E = R + (Q-1)r - s$ computed from the residues) held in
every instance: $0$ failures of either statement.

## 2. Task 2: the SPLIT-odd case is closed

### 2.1 The full remaining condition set in the pinned case

Let $(n, 3, j)$ be a counterexample in (SPLIT-odd): $n$ odd,
$v_3(n) = 1$, $j = n/3$ (so $n = 3j$, $Q = 3$, $R = 0$), $j \ge 7$.
The conditions it must satisfy, in full:

* **(LD3), $r = 0$:** automatic: $R(n) = n/3 = j \mid j$, since
  $n$ is odd with $v_3(n) = 1$.
* **(LD3), $r = 1$:** every relevant prime power
  $q \Vert (n-1)$ satisfies $j \bmod q \in \{0, 1\}$, i.e.
  $R(n-1) = X_0 X_1$ with $X_0 \mid j$, $X_1 \mid j - 1$.
* **(LD3), $r = 2$:** every relevant prime power
  $q \Vert (n-2)$ satisfies $j \bmod q \in \{0, 1, 2\}$, i.e.
  $R(n-2) = Y_0Y_1Y_2$ with $Y_s \mid j - s$.
* **(N1):** $\gcd(\binom n2, \binom nj) = 2^a 3^b$; here
  $\binom n2 = 3j(3j-1)/2$, so in particular no prime
  $p \ge 5$ dividing $3j - 1$ may divide $\binom nj$.
* **(N2), unwound:** since $e = v_3(n(n-1)(n-2)) = 1$ (only $n$
  is divisible by $3$, exactly once) and $U_0 = n/3 = j$ exactly,
  $$V_3(n) = j \cdot U_1 U_2, \qquad\text{hence (N2) gives}\qquad
  j\, U_1 U_2 \mid \tbinom j3,\ \ U_1U_2 \le \frac{(j-1)(j-2)}{6}.$$
  (The size shadow of this is Remark A2.29's $v_2(\binom n3)
  \ge 5$; the divisibility form above is sharper, but even it
  does not close the case: $U_1U_2$ may a priori be a nontrivial
  divisor of $\binom j3 / j$ distributed as (LD3) allows.)

None of these conditions is needed for the contradiction in
§2.2; they are recorded because the task asks for the full set,
and to make clear that the closure below does not secretly use
any of them.

### 2.2 Contradiction via Theorem F2.3

**Lemma F2.6 (the exponential Diophantine step) — PROVED.**
The equation $2^a - 3^d = 1$ in integers $a \ge 1$, $d \ge 0$
has exactly the solutions $(a, d) = (1, 0)$ and $(2, 1)$.

*Proof.* If $d = 0$ then $2^a = 2$, $a = 1$. If $d \ge 1$ then
$2^a \equiv 1 \pmod 3$, so $a$ is even, $a = 2k$, and
$(2^k - 1)(2^k + 1) = 3^d$. Both factors are powers of $3$,
say $2^k - 1 = 3^s$, $2^k + 1 = 3^t$ with $s + t = d$,
$t > s \ge 0$; subtracting, $3^t - 3^s = 2$. If $s \ge 1$ then
$3 \mid 2$, impossible; so $s = 0$, $3^t = 3$, $t = 1$,
$k = 1$, giving $(a, d) = (2, 1)$. $\square$

**Theorem F2.7 (SPLIT-odd is empty) — PROVED.** There is no
counterexample $(n, 3, j)$ with $n$ odd, $v_3(n) = 1$ and
$j = n/3$ (for any $j > 3$; the configuration has $j \ge 7$ in
the open range, and no pinned triple with $j \le 3$ exists
except $n = 3$, $j = 1$).

*Proof.* Suppose $(n, 3, j)$ is a counterexample in the pinned
case. Then $n = 3j$, so $Q = 3$, $R = 0$, and the $(3,0)$ row of
Theorem F2.3's table gives
$$V_3(n) \mid \Lambda_3(4)\, \binom j1 = 3j.$$
By §2.1, $V_3(n) = j \cdot U_1 U_2$ (using $U_0 = j$ and
$e = 1$). Hence $U_1 U_2 \mid 3$. But $U_1, U_2$ are supported on
primes $\ge 5$, so $\gcd(U_1U_2, 3) = 1$ and $U_1 U_2 = 1$,
i.e. $U_1 = U_2 = 1$. Thus $n - 1$ and $n - 2$ have no prime
factor $\ge 5$: $n - 1 = 2^a 3^b$ ($a \ge 1$, as $n - 1$ is even)
and $n - 2 = 3^d$ ($n - 2$ is odd, so its $2$-part is trivial).
If $d = 0$ then $n = 3$ and $j = 1$, excluded. If $d \ge 1$
then $n - 1 = 3^d + 1 \equiv 1 \pmod 3$, so $b = 0$ and
$n - 1 = 2^a$. Therefore $2^a - 3^d = (n-1) - (n-2) = 1$, and
Lemma F2.6 gives $(a, d) \in \{(1,0), (2,1)\}$; with $d \ge 1$
this forces $n = 3^1 + 2 = 5$, which has $v_3(n) = 0 \ne 1$
(and $3 \nmid n$, so $j = n/3$ is not an integer) —
contradiction. $\square$

**Claim F2.8 (status of Task 2) — PROVED.** The SPLIT-odd
configuration of P-A2 Statement A2.28 is closed, unconditionally
on the inputs of §0 (in fact only Kummer's criterion, via Lemma
F2.2, is used; not (LD3), (N1), (N2), or EEES78). The argument
does not stop anywhere: the levers named in the task
(higher-digit Kummer conditions, (N1) modulo constraints) are
not needed, because Proposition 4.1's conclusion
$V_3(n) \mid 3j$ is already incompatible with
$V_3(n) = j U_1 U_2$ unless $U_1 = U_2 = 1$, and the resulting
two-term exponential equation is elementary. As a consistency
check, the computation of §5 finds $0$ (LD3) survivors in this
family up to $n \le 10^6$ — weaker than Theorem F2.7, which
covers all $n$, but independent of it.

## 3. Task 3: SPLIT-even — what Proposition 4.1 cuts, and the exact residual class

Throughout §3, $(n, 3, j)$ is a counterexample with $n$ even,
$j \ge 7$ (so $j \ge 159$ once §4's pair closures are applied),
$n = Qj + R$ as in Theorem F2.3. The odd top number is $n - 1$,
with $R(n-1) \in \{n - 1, (n-1)/3\}$.

**Theorem F2.9 (genuine split prime powers are small) —
PROVED.** Let $q = p^a$ ($p \ge 5$) be a relevant prime power of
one of $n, n-1, n-2$ — equivalently a full prime-power part of
$V_3(n)$ at $p$ — and suppose $(Q, R) \ne (2, 0)$. If
$q \nmid j$ then $q \le T = R + 2(Q-1)$. Consequently, any prime
power that (LD3) assigns to $j - 1$ or $j - 2$ but not to $j$
(a *genuine split part*) satisfies $q \le T$.

*Proof.* Corollary F2.4 with $h \le 1$: $q \mid j$ or
$q \le T$. A genuine split part has $q \mid j - s$ for some
$s \in \{1, 2\}$ and $q \nmid j$ (it cannot divide both, as
$q > \gcd(j, j-s) \ge 1$ would force $q \mid s \le 2 < 5 \le q$),
so $q \le T$. $\square$

**Corollary F2.10 (the $> n/3$ prime-power factor, $Q = 2$
regime) — PROVED.** Suppose $Q = 2$ (i.e. $2j \le n < 3j$),
$R \ge 3$, and $j > n/3 + 1$. Then $T = n - 2j + 2 < n/3$.
Hence: (a) every genuine split part of $R(n-1)$ and of
$R(n-2)$ is $< n/3$ (Theorem F2.9). (b) If $R(n-1)$ has a
prime-power factor $q > n/3$ at a prime $p \ge 5$, then
$R(n-1) = q$: indeed $q \mid R(n-1) \le n - 1 < 3q$, and any
second prime-power factor of $R(n-1)$ is $\ge 5$, which would
give $R(n-1) \ge 5q > 5n/3 > n - 1$, impossible. So
$q \in \{n - 1, (n-1)/3\}$. By (LD3), $q \mid j$ or
$q \mid j - 1$; the latter with $q \nmid j$ would make $q$ a
genuine split part, contradicting (a) via Theorem F2.9, so
$q \mid j$. If $q = n - 1$ this contradicts $q \le j \le n/2$.
The only sub-configuration not excluded is therefore
$R(n-1) = (n-1)/3$ with $\big((n-1)/3\big) \mid j$.

**Corollary F2.11 (single prime power $R(n-1)$, clean form) —
PROVED.** Suppose $R(n-1) = q$ is a single relevant prime power
with $p \ge 5$, $(Q, R) \ne (2,0)$, and $T < q$. Then (LD3)
forces $q \mid j$ (the alternative $q \mid j - 1$ contradicts
Theorem F2.9). Hence if also $q > j$ the triple is closed.
Since $q \in \{n - 1, (n-1)/3\}$ here, $q > j$ holds whenever
$j < (n-1)/3$; so a single-prime-power $R(n-1)$ with
$T < q$ and $j < (n-1)/3$ is excluded outright.

**Proposition F2.12 (the $V \mid 3j$ rows in even parity) —
PROVED.** In the rows $(Q, R) = (2, 2)$ and $(3, 0)$ of the
table in §1.2 (i.e. $n = 2j + 2$, resp. $n = 3j$ with $n$ even,
so $j$ even), Theorem F2.3 gives $V_3(n) \mid 3j$. Each $U_r$
divides $V_3(n)$, is coprime to $3$, and the $U_r$ are pairwise
coprime; hence
$$U_0 U_1 U_2 \mid j, \qquad
3^{\,e-1} \mid 3j \,/\, (U_0U_1U_2).$$
In particular every $\ge 5$ prime power of every top number
divides $j$ itself in these rows — no genuine splitting of the
$\ge 5$ parts is possible at all — and (LD3) is reduced to the
splitting of the $3$-parts alone.

*Proof.* $U_r \mid 3j$ and $\gcd(U_r, 3) = 1$ give
$U_r \mid j$; pairwise coprimality gives the product statement;
the $3$-part statement is what remains of $V_3(n) \mid 3j$.
$\square$

**Proposition F2.13 (combined size in the $h = 0$ rows) —
PROVED.** If $R \ge 3$ (so $h = 0$), then
$V_3(n) \mid \gcd\big(\binom j3, \Lambda_3(T)\big)$ by
Theorem F2.3 and (N2). E.g. at $(Q, R) = (2, 4)$
($n = 2j + 4$): $T = 6$, $\Lambda_3(6) = 15$, so
$V_3(n) \mid 15$: $U_0U_1U_2 \mid 15$ and $e \le 2$. Thus in
this row each of $n, n-1, n-2$ is of the form
$2^a 3^b \cdot u$ with $u \mid 15$ composed of primes $\ge 5$
and total $\ge 5$-part dividing $15$ — an explicit thin class,
not excluded in general by the arguments here.

**Claim F2.14 (the exact residual class for SPLIT-even) —
OPEN.** After Cycle 1 and §§1–3, a counterexample with $n$ even
must satisfy *simultaneously*: (LD3); (N1); (N2); the
divisibility $V_3(n) \mid \Lambda_3(T)\binom jh$ of
Theorem F2.3; the per-part dichotomy of Corollary F2.4 (every
genuine split prime power at $p \ge 5$ is $\le T$; the $3$-part
$3^{e-1}$ either is $\le T$ in the $\Lambda_3$ sense or divides
some $j - r$, $r < h$); Proposition F2.12's conclusion in the
rows $(2,2)$ and $(3,0)$; and $j \ge 159$ (§4) — resp.
$n > 10^6$ in the searched range (§5). No contradiction from
this system is proved here. The configurations **not** excluded
are exactly: **(E-res 1)** $h = 1$ rows with every genuine split
part $\le T$ and $\Lambda_3(T) \ge$ the relevant split parts
(includes all $(Q, R)$ with $R \in \{0, 1, 2\}$, $Q \ge 3$, and
$Q = 2$, $R \in \{1, 2\}$ beyond Proposition F2.12's
$U$-product condition); **(E-res 2)** $h = 0$ rows
($R \ge 3$) in which every relevant prime power of
$n, n-1, n-2$ at $p \ge 5$ is $\le T$ and
$V_3(n) \mid \gcd(\binom j3, \Lambda_3(T))$. The obstruction
to finishing is the same in both: $\Lambda_3(T)$ grows like
$e^{(1 + o(1))T}$ (logarithm of $\mathrm{lcm}(1, \dots, T)$),
so for $T$ moderately large the size content of
Theorem F2.3 is weak, and the remaining content is a
distribution condition on prime powers $\le T$ among
$j, j-1, j-2$ that neither (LD3) nor Proposition 4.1
contradicts in general. This is stated as the exact place the
SPLIT-even proof stops.

## 4. Task 4: Del Pin refined by $V_3$; the sweep row $i=3$; the per-pair reach of (LD3)

### 4.1 The $V_3$-refined Del Pin comparison

Del Pin's verified lemma (EXTERNAL_CLAIMS, Claim thread):
if $\binom{2j}{i} \ge \binom ji^2$ then $(i, j)$ is good for all
$n \ge 2j$ outside the EEES78 exceptions. For $i = 3$,
$F(j) := \binom{2j}{3} / \binom j3^2$ satisfies
$F(4) = 56/16 > 1$, $F(5) = 120/100 > 1$,
$F(6) = 220/400 < 1$, and $F$ is strictly decreasing, so
Del Pin's criterion closes exactly $j \le 5$ at $i = 3$
($J_1(3) = 5$). The refinement uses (N2) directly: a
counterexample needs $V_3(n) \mid \binom j3$, hence
$V_3(n) \le \binom j3$, and $V_3(n) = \binom n3 / 2^{v_2(\binom
n3)}$ exactly (the part of $\binom n3$ on primes $< 3$ is a pure
power of $2$).

**Theorem F2.15 ($v_2 \le 3$ closes every $j$) — PROVED.**
Let $n \ge 2j$, $j \ge 3$. If $v_2(\binom n3) \le 3$ then
$\gcd(V_3(n), \binom nj) > 1$: the triple $(n, 3, j)$ is not a
counterexample. No EEES78 input is used.

*Proof.* Suppose it were a counterexample. By (N2),
$V_3(n) \le \binom j3$. But
$V_3(n) = \binom n3 / 2^{v_2(\binom n3)} \ge
\binom{2j}{3} / 2^{v_2(\binom n3)} \ge \binom{2j}{3}/8$
(monotonicity of $\binom{\cdot}{3}$ and $v_2 \le 3$), and
$$\frac{\binom{2j}{3}}{\binom j3}
= \frac{2j(2j-1)(2j-2)}{j(j-1)(j-2)}
= \frac{4(2j-1)}{j-2} > 8
\qquad\Longleftrightarrow\qquad 2j - 1 > 2j - 4,$$
which is true. Hence $V_3(n) > \binom j3$, contradiction.
$\square$

**Corollary F2.16 — PROVED.** (i) Every counterexample at
$i = 3$ (any $j$, any $n \ge 2j$) has $v_2(\binom n3) \ge 4$,
i.e. $v_2(n(n-1)(n-2)) \ge 5$. (ii) For **every** $j > 5$ —
exactly where Del Pin's unrefined comparison fails — the
refined comparison closes all triples $(n, 3, j)$ with
$v_2(\binom n3) \le 3$, uniformly in $j$. More generally a
triple is closed whenever
$2^{v_2(\binom n3)} \binom j3 < \binom n3$ (this is
$V_3(n) > \binom j3$ restated; the content of Theorem F2.15 is
the uniform threshold $v_2 \le 3$ obtained by inserting
$n \ge 2j$). (iii) The set of $n$ with $v_2(\binom n3) \le 3$
has natural density $27/32$: $v_2(\binom n3) \le 3$ iff
$v_2(n(n-1)(n-2)) \le 4$, this depends only on $n \bmod 32$
(if some factor is $\equiv 0 \pmod{32}$ its valuation is
$\ge 5$; otherwise each factor's valuation is read off from
$n \bmod 32$), and exactly $27$ of the $32$ residue classes
satisfy it (finite check, §6). So the refined comparison
closes, for each $j$, a set of $n$ of density $27/32$; the
necessary condition $v_2 \ge 4$ confines counterexamples to
the complementary density $5/32$. (This sharpens, for general
$j$, the $v_2 \ge 5$ bound that Remark A2.29 obtained in the
pinned case from the weaker ratio $> 27$; in the pinned case
the sharper truth is Theorem F2.7.)

### 4.2 Exactly which $j$ the cap-20,000 sweep clears at $i=3$

**Claim F2.17 (sweep row, read off the file) — COMPUTATION
(file read, not recomputed).** In
`erdos-699/pairpass_20000.json` ($n^\star = 20{,}000$), the row
`cleared_js_by_i["3"]` is exactly
$$[\,5, 6, 7, \dots, 158\,],$$
$154$ values, contiguous, no gaps: the pairs $(3, j)$ with
$5 \le j \le 158$ are fully cleared by the sweep for all $n$,
and no $j \ge 159$ is in the row. ($j = 4$ is not in the row;
it is closed for all $n$ by Price's $j \le 3i/2$ range and by
P-A2 Lemma A2.17.) Consistency check with §0's finite
reduction: $N(3, 158) = 19{,}926 \le 20{,}000 <
20{,}181 = N(3, 159)$ (computed in §6), which is exactly why a
cap of $20{,}000$ clears $j = 158$ and not $j = 159$.

### 4.3 The reach of the pure digit method per pair

**Computation F2.18 ((LD3) alone, per pair, $j \le 5000$) —
COMPUTATION (exact; cross-validated).** For every $j$ with
$5 \le j \le 5000$, the system (LD3) has **no** solution with
$2j \le n \le N(3, j)$. Method (complete enumeration, not
sampling): any (LD3) solution has $R(n) \mid j$ (the $r = 0$
clause); writing $n = R(n) \cdot s$, the cofactor $s$ is
supported on primes $\{2, 3\}$ with $v_3(s) \le 1$ (any prime
$\ge 5$ in $s$, and any $3^2$ in $s$, would lie in $R(n)$), and
$R(n)$ is an odd divisor of $j$ with $v_3(R(n)) \ne 1$. The
computation enumerated all such pairs $(R, s = 2^a 3^e)$,
$e \in \{0, 1\}$, with $2j \le Rs \le N(3, j)$ — $N(3, 2000) =
3{,}239{,}787$ and $N(3, 5000) = 20{,}263{,}871$ are the largest
bounds — verified $R(n) = R$ for each candidate by exact
factorisation, and tested the full (LD3) clauses on
$n, n-1, n-2$. **Result: zero solutions for every $j$ in
$5 \le j \le 5000$** (the range $5 \le j \le 2000$ required by
the task, and the extension to $5000$, agree). Cross-validation:
an independent brute-force implementation (trial division, no
enumeration shortcut) over all $n \in [2j, N(3,j)]$ for
$5 \le j \le 60$ also found zero solutions; the two factorisation
implementations (smallest-prime-factor sieve; trial division by
sieved primes) agree on their overlap.

**Corollary F2.19 (pairs $(3, j)$, $5 \le j \le 5000$, closed
for all $n$) — PROVED modulo Computation F2.18 and the §0
finite reduction.** For each such $j$, a counterexample would
satisfy $n \le N(3, j)$ (finite reduction; the sole $i = 3$
EEES78 exception $(8, 3)$ admits no $j \ge 5$) and would
satisfy (LD3) (P-A2, Corollary A2.23), contradicting
Computation F2.18. Hence **the exact frontier of the pure digit
method per pair, within the range computed, is: every
$j \le 5000$** — the method does not break down anywhere in
$5 \le j \le 5000$. Whether (LD3) alone continues to exclude
every $j > 5000$ is **OPEN** (Computation F2.18 does not reach
it, and no proof is given here); note the enumeration cost per
$j$ grows like $\tau(j) \log N(3, j)$ with
$N(3, j) \sim (2j)^2 / 120^{1/3}$, so the computation extends
readily, but any finite extension leaves the same open tail.

## 5. Task 5: bounded searches (labelled computation)

**Computation F2.20 (SPLIT-odd family, (LD3) to $10^6$) —
COMPUTATION.** All $n \le 10^6$ with $n$ odd, $v_3(n) = 1$,
$j = n/3 \ge 7$ were tested against the $r = 1$ and $r = 2$
clauses of (LD3) (the $r = 0$ clause is automatic in this
family), by exact prime-power factorisation of $n - 1$ and
$n - 2$ (smallest-prime-factor sieve to $10^6$). Candidates
tested: $111{,}109$. **Survivors: $0$.** This is consistent
with, and strictly weaker than, Theorem F2.7 (which closes the
family for all $n$ using Proposition 4.1, not (LD3)).

**Computation F2.21 (full (LD3), $n$ even) — COMPUTATION.**
All pairs $(n, j)$ with $n$ even, $7 \le j \le n/2$, were
tested against the full system (LD3), enumerating for each $n$
only the multiples $j$ of $R(n)$ (the $r = 0$ clause) and
testing the $r = 1, 2$ clauses by exact factorisation.
Ranges and counts: $n \le 10^5$: $604{,}976$ pairs tested,
**$0$ survivors**. $n \le 10^6$: $6{,}974{,}117$ pairs tested,
**$0$ survivors** ($32$ s).
No survivor was found in any range, so there is nothing to
double-verify; had a survivor appeared it would have been
reported prominently here (it would *not* have been a
counterexample to #699, (LD3) being necessary, not sufficient).

These computations extend S8 §3.4 / P-A2 §4.2 ((LD3) has no
solution with $n \le 5000$, all parities) to $n \le 10^6$ in
the two SPLIT families, and are consistent with the sweep's
stronger statement (no counterexample with $n \le 20{,}000$,
all $i$).

## 6. Computations performed by this prover (Python stdlib, exact)

1. Extraction of Price §4 via `pdftotext -layout`, `-raw`, and
   `-bbox` word positions (§1.1).
2. Lemma F2.2 / Corollary F2.4 sampling check: $4000$ seeded
   random pairs, $840$ prime-power instances, $0$ failures (§1).
   $\Lambda_3$ values: $\Lambda_3(2) = 1$, $\Lambda_3(3) =
   \Lambda_3(4) = 3$, $\Lambda_3(5) = \Lambda_3(6) = 15$.
3. Del Pin values $F(4), F(5), F(6)$ and the ratio
   $\binom{2j}{3}/\binom j3 = 4(2j-1)/(j-2)$ at
   $j = 4, \dots, 9$ (§4.1); $v_2(\binom n3)$ distribution for
   $n < 10^5$ (fraction with $v_2 \le 3$ is $0.84376 \approx
   27/32$) and the residue count $27$ of $32$ modulo $32$ (§4.1).
4. $N(3, j)$ exactly at $j = 7, 100, 158, 159, 500, 1000,
   2000, 5000$: $27$; $7{,}908$; $19{,}926$; $20{,}181$;
   $201{,}728$; $808{,}934$; $3{,}239{,}787$; $20{,}263{,}871$
   (binary search on $\binom n3 < \binom{2j}{6}$, exact).
5. Computation F2.18: (LD3) per pair for $5 \le j \le 2000$
   (SPF sieve to $3{,}239{,}787$; $3.2$ s) and $2001 \le j \le
   5000$ (trial division; $17.6$ s); brute-force cross-check for
   $5 \le j \le 60$. Zero solutions throughout.
6. Computations F2.20, F2.21: SPF sieve to $10^6$; SPLIT-odd
   candidates $111{,}109$, $0$ survivors; even $n \le 10^5$:
   $604{,}976$ pairs, $0$ survivors; even $n \le 10^6$:
   $6{,}974{,}117$ pairs, $0$ survivors.
7. Reading (not recomputation) of the sweep row
   `cleared_js_by_i["3"]` in `pairpass_20000.json` (§4.2).

## 7. Task 6: closing statement — exactly what is proved for $i=3$ beyond Cycle 1

**Newly proved here (beyond Cycle 1):**

* **(SPLIT-odd) is closed for all $n$** (Theorem F2.7):
  PROVED, using only Kummer's criterion via the self-contained
  $i = 3$ case of Price's Proposition 4.1 (Theorem F2.3). One
  of the two residual configurations of P-A2 Statement A2.28
  is eliminated.
* **Price's Proposition 4.1 at $i = 3$** (Theorem F2.3, with
  the per-part dichotomy, Corollary F2.4): PROVED
  self-containedly; its exact statement at general $i$ is
  extracted in Claim F2.1.
* **SPLIT-even cut:** every genuine split prime power
  ($p \ge 5$) in a counterexample is $\le T = R + 2(Q-1)$
  (Theorem F2.9), with the $Q = 2$, $j > n/3 + 1$ corollary
  excluding split parts $> n/3$ (Corollary F2.10), the clean
  single-prime-power criterion (Corollary F2.11), the
  $U_0U_1U_2 \mid j$ conclusion in the rows $n = 2j + 2$ and
  $n = 3j$ (Proposition F2.12), and the combined
  $V_3(n) \mid \gcd(\binom j3, \Lambda_3(T))$ bound in the
  $h = 0$ rows (Proposition F2.13): all PROVED.
* **$v_2$ refinement of Del Pin:** $v_2(\binom n3) \le 3$
  closes $(n, 3, j)$ for every $j$ and every $n \ge 2j$
  (Theorem F2.15); every $i = 3$ counterexample has
  $v_2(\binom n3) \ge 4$; the closed set of $n$ has density
  $27/32$ (Corollary F2.16): PROVED.
* **Pairs $(3, j)$ for $5 \le j \le 5000$ are closed for all
  $n$** (Corollary F2.19): PROVED modulo the exact computation
  F2.18 and the Cycle 1 finite reduction. This extends the
  sweep's fully-cleared range at $i = 3$ from $j \le 158$ to
  $j \le 5000$ (by a different, per-pair digit method).

**Reduced but not closed:**

* (SPLIT-even) is reduced to the explicit residual class
  (E-res 1) / (E-res 2) of Claim F2.14, together with
  $j \ge 5001$ (after §4) and $n > 10^6$ in the searched
  families (§5). **OPEN.**

**Still open, untouched by this document:**

* $(H_3)$ in general: (LD3) is not proved unsatisfiable for
  $j \ge 5001$; Computation F2.18 shows the digit method's
  per-pair reach is at least $j \le 5000$ and does not locate
  any breakdown, but a general proof that (LD3) has no
  solutions — or a closure of the residual class (E-res 1) /
  (E-res 2) by higher-digit Kummer conditions or another idea —
  remains the missing step for $i = 3$ via this route.
* $i = 3$ in general, and Erdős #699, are **not** proved here.
  A counterexample at $i = 3$, if one exists, now must have:
  $n$ even, $j \ge 5001$, $v_2(\binom n3) \ge 4$, $n \ne 2j$,
  and must lie in the residual class of Claim F2.14 while
  satisfying (LD3), (N1), (N2), and Theorem F2.3.
