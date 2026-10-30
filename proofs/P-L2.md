# Prover L2 (independent): Cluster L — the higher-digit Kummer refinement (LD3⁺) at $i=3$, Cycle 3

Prover: L2, working independently in Cycle 3. The second prover on this
cluster (L1) exists, but `proofs/P-L1.md` was **not** read, looked for, or
consulted at any point; methodological independence is preserved. Sources
read: `CYCLE2.md` §2; `proofs/P-A1.md` §§4–5 (Lemma A1.15, the (LD3)
Definition, Proposition A1.16, Statement (H3), Theorem A1.17);
`proofs/P-A2.md` §4 (Lemma A2.21, Definition A2.22, Corollary A2.23,
Statements A2.27/A2.28); `proofs/P-F1.md` (especially Claim F1.6(c), the
recorded GAP this cluster addresses, and Claims F1.9–F1.11);
`proofs/P-F2.md` §§1–3 (Lemma F2.2, Theorem F2.3, Corollary F2.4,
Theorem F2.9, Proposition F2.13, Claim F2.14); `verification/V-A.md` and
`verification/V-F.md` for what is certified. Every computation below is in
`proofs/P-L2_checks.py` (Python standard library only, exact integer
arithmetic, no randomness; section letters below refer to that script).
Every numbered claim is labelled PROVED / GAP / FALSE / OPEN / COMPUTATION.

**Headline.** The full digitwise refinement (LD3⁺) is formulated exactly
(§1). The precision question in the brief has a clean answer: on the low
digits $0,\dots,a-1$, digitwise is **exactly** $j \bmod q \le \rho$,
neither stronger nor weaker — the apparently extra content (forcing $j$'s
digits $1,\dots,a-1$ to vanish) is already encoded in (LD3), because the
bound $\rho \le 2$ is smaller than the prime $p$ itself (Lemma L2.2). The
genuinely new content of (LD3⁺) is therefore precisely the **tail**:
digits $\ge a_p$ for each prime $p \mid C(n,3)$, and for primes dividing a
top to the first power ($a_p = 1$) that tail is everything above digit
$0$. One correction to the brief's framing is proved in §1
(Theorem L2.4): the *completed* system (LD3⁺) is not merely necessary —
it is **equivalent** to $\gcd(V_3(n), C(n,j)) = 1$, so a solution of
(LD3⁺) in range *is* a counterexample, and (H3⁺) is logically equivalent
to closing $i=3$ (while (H3) is strictly stronger). At $p=3$ (§2), the
classical near-miss family $n = 3^a+1$, $j = n/2$ is excluded by (LD3⁺)
at exactly the low ternary digits and its tail passes, so (LD3⁺) gives
**no** stronger exclusion there; the calibration six are reproduced
digit-for-digit. The tail is nevertheless strictly stronger *per prime*
(§3: a proved infinite family at $p=5$, and $303{,}253$ of $529{,}054$
low-passing prime instances at $n \le 2000$ fail only in the tail). But
on every residual population enumerated in §4 — in particular all
$h=0$ rows with $Q \in \{2,\dots,8\}$, $T \le 20$, enumerated **globally**
via a finiteness lemma (Lemma L2.11), and the $(4,2)$ row — (LD3) already
has **zero** survivors, so (LD3⁺) has nothing to act on. Verdict (§5):
option **(b)** — (LD3⁺) is strictly stronger as a condition and
computationally decisive at the single-prime level, but **no general
shrinkage of the residual class is proved**, and the exact point where
the proof attempt stops is identified. **$i=3$ is not closed, (H3) and
(H3⁺) are not proved, and #699 is not claimed solved.**

## 0. Standing inputs and notation

A **counterexample** is a triple $(n,3,j)$, $3 < j \le n/2$, with
$\gcd(V_3(n), C(n,j)) = 1$, where $V_3(n)$ is the odd part of $C(n,3)$
(the part on primes $\ge 3$). The top numbers are $n, n-1, n-2$; every
prime $p \ge 3$ divides at most one of them. $R(m)$ is the product of the
relevant prime powers $q = p^a \Vert m$ ($p \ge 5$, any $a \ge 1$;
$p = 3$ with $a \ge 2$). Certified inputs used: (LD3) and its necessity
(A1.15/A1.16(i), A2.21/A2.23); (N1), (N2) ($V_3(n) \mid C(j,3)$);
Proposition 4.1 at $i=3$ in the forms F1.9/F2.9 (genuine split parts
$\le T := R + 2(Q-1)$, $n = Qj + R$) and F2.13 ($h = 0$ rows:
$V_3(n) \mid \Lambda_3(T)$); SPLIT-odd closed (no counterexample has $n$
odd); rows $(Q,R) \in \{(2,0),(2,2),(3,0),(3,2),(4,0)\}$ closed;
$v_2(C(n,3)) \ge 4$ necessary; (LD3) has no solution with $n \le 10^6$;
every pair $(3,j)$ with $j \le 5000$ is closed for all $n$. The residual
is the even class of F1.11/F2.14.

**Digit notation.** For a prime $p$ and $x \ge 0$, $x_e(p)$ is the digit
of $x$ at position $e$ in base $p$ ($x = \sum_e x_e p^e$,
$0 \le x_e < p$). For a prime $p$ dividing some top number, let
$\rho(p) \in \{0,1,2\}$ be the unique index with $p \mid n - \rho(p)$,
$a_p = v_p(n - \rho(p)) \ge 1$, $q_p = p^{a_p}$, and
$K_p = (n - \rho(p))/q_p$. Since $n = q_p K_p + \rho(p)$ with
$0 \le \rho(p) \le 2 < q_p$, we have $\lfloor n / q_p \rfloor = K_p$, and
the digits of $n$ split at position $a_p$: digits $0,\dots,a_p-1$ encode
$\rho(p)$ (see Lemma L2.2) and digits $a_p, a_p+1, \dots$ are the digits
of $K_p$.

**The prime set.** Let $\mathcal{P}(n) = \{p \ge 5 : p \text{ divides
some top}\} \cup (\{3\}$ if the $3$-divisible top has $v_3 \ge 2)$.

**Lemma L2.0 (PROVED — $\mathcal{P}(n)$ is the prime support of
$V_3(n)$).** $p \in \mathcal{P}(n)$ iff $p \ge 3$ and $p \mid C(n,3)$,
iff $p \mid V_3(n)$.

*Proof.* For $p \ge 5$, $p \nmid 6$, so
$v_p(C(n,3)) = v_p(n(n-1)(n-2))$, which is $\ge 1$ iff $p$ divides a top
(uniquely). For $p = 3$, exactly one top is divisible by $3$, say with
valuation $a$; then $v_3(C(n,3)) = a - v_3(6) = a - 1$, which is $\ge 1$
iff $a \ge 2$. $V_3(n)$ is by definition the part of $C(n,3)$ on primes
$\ge 3$. $\square$

Note the bijection used throughout: relevant prime powers $q$ (in
(LD3)'s sense) are in one-to-one correspondence with $p \in
\mathcal{P}(n)$, via $q = q_p$.

## 1. Task L.1: the system (LD3⁺), and the exact gap to (LD3)

**Definition L2.1 ((LD3⁺)).** A pair $(n,j)$, $3 < j \le n/2$,
**satisfies (LD3⁺)** if for every $p \in \mathcal{P}(n)$ and every
$e \ge 0$,
$$j_e(p) \;\le\; n_e(p).$$
For $p \in \mathcal{P}(n)$, call the conditions at positions
$e < a_p$ the **low part** at $p$ and those at $e \ge a_p$ the **tail**
at $p$.

**Lemma L2.2 (PROVED — the low part is exactly (LD3); the precision
point of the brief).** Let $p \ge 3$ divide a top number, with
$\rho = \rho(p)$, $a = a_p$, $q = q_p$. Then
$$\big(j_e(p) \le n_e(p) \text{ for all } e < a\big)
\;\Longleftrightarrow\; j \bmod q \le \rho.$$

*Proof.* Since $q \mid n - \rho$ and $0 \le \rho \le 2 < p$, we have
$n \bmod q = \rho$, whose base-$p$ expansion padded to $a$ digits is
$n_0 = \rho$, $n_1 = \dots = n_{a-1} = 0$.

($\Rightarrow$) $j \bmod q = \sum_{e<a} j_e p^e$. Digitwise gives
$j_0 \le \rho$ and $j_e \le n_e = 0$, i.e. $j_e = 0$, for $1 \le e < a$.
Hence $j \bmod q = j_0 \le \rho$.

($\Leftarrow$) Suppose $s := j \bmod q \le \rho$. Then
$s \le \rho \le 2 < p$, so $s < p$. The base-$p$ expansion of $s$ is
therefore a single digit: digit $0$ equal to $s$, digits
$1,\dots,a-1$ equal to $0$. But the digits of $s = j \bmod q$ at
positions $0,\dots,a-1$ are exactly $j_0, \dots, j_{a-1}$. Hence
$j_0 = s \le \rho = n_0$ and $j_e = 0 = n_e$ for $1 \le e < a$. $\square$

**Precision remarks (the point the brief insisted on).** (i) The
digitwise condition on digits $1,\dots,a-1$ *does* force those digits of
$j$ to be $0$ — i.e. it constrains $j \bmod q$ to lie in
$\{0, 1, \dots, \rho\}$ rather than merely to be $\le$ some large bound —
but (LD3) as stated already says exactly this, because the bound in
(LD3) is $\rho \le 2$, which is **smaller than $p$**, hence smaller than
any two-digit base-$p$ number. The equivalence is *not* a general fact
about inequalities mod $q$: it uses $\rho < p$ load-bearingly. (For
contrast, with a hypothetical bound $\beta \ge p$ it would fail: at
$p = 5$, $a = 2$, $j \bmod 25 = 6 \le \beta := 6$ has digits $(1,1)$,
violating digit $1 \le 0$.) This covers every sub-case uniformly:
$a = 1$ (no intermediate digits, both sides say $j \bmod p \le \rho$)
and $a \ge 2$ (the intermediate digits are forced to $0$ by both sides).
So A1.15's derivation is confirmed exactly as it suggests: digitwise on
digits $0,\dots,a-1$ ⟺ $j \bmod q \le \rho$, and (LD3) is *precisely*
the low truncation of (LD3⁺), with no hidden strengthening and no gap.
(ii) Verified computationally (script §B): for all $n \le 1000$,
all $j \le n/2$, all relevant $(\rho, p, a, q)$, the two sides agree in
$1{,}101{,}758$ instances, $0$ mismatches.

**Theorem L2.3 (PROVED — necessity, and the exact gap).**
(i) If $(n,3,j)$ is a counterexample, then $(n,j)$ satisfies (LD3⁺).
(ii) (LD3⁺) $\Rightarrow$ (LD3). (iii) The gap between them is exactly
the tails: writing $K_p$ as in §0,
$$\text{(LD3⁺)} \iff \text{(LD3)} \;\wedge\; \bigwedge_{p \in
\mathcal{P}(n)} \mathrm{Tail}(p), \qquad
\mathrm{Tail}(p):\ \forall k \ge 0,\ 
\big(\lfloor j/q_p \rfloor\big)_k(p) \le (K_p)_k(p),$$
i.e. $\lfloor j/q_p \rfloor$ is digitwise $\le K_p$ in base $p$. In
particular the digit at position $a_p$ is constrained by
$j_{a_p}(p) \le K_p \bmod p$, the digit at $a_p + 1$ by
$j_{a_p+1}(p) \le \lfloor K_p/p \rfloor \bmod p$, and so on.

*Proof.* (i) A counterexample has $p \nmid C(n,j)$ for every
$p \in \mathcal{P}(n)$ (such $p$ divides $V_3(n)$ by Lemma L2.0, and
$\gcd(V_3(n), C(n,j)) = 1$). By Kummer's theorem, $v_p(C(n,j)) = 0$ iff
$j$ is digitwise $\le n$ in base $p$ (no carry when adding $j$ and
$n-j$). That is (LD3⁺). (ii) For each relevant $q = q_p$, Lemma L2.2
turns the low part at $p$ into the (LD3) clause $j \bmod q \le \rho$.
(iii) The digits of any $x$ at positions $\ge a_p$ are the digits of
$\lfloor x / q_p \rfloor$ shifted by $a_p$; applied to $x = n$,
$\lfloor n/q_p \rfloor = K_p$ (§0), and to $x = j$. So the conditions
at positions $\ge a_p$ are exactly $\mathrm{Tail}(p)$, and (LD3⁺)
splits as low (⟺ (LD3), Lemma L2.2) ∧ tails. $\square$

**What is new, prime by prime.** For a prime dividing a top to the
**first power only** ($a_p = 1$: the typical case, and the only case
(LD3) sees through a single digit), (LD3) constrains only
$j \bmod p \le \rho$, while (LD3⁺) additionally constrains **every**
digit of $\lfloor j/p \rfloor$ against the digits of
$K_p = (n - \rho)/p$: entirely new content. For $a_p \ge 2$, the tail
begins at position $a_p$ and is likewise new. Primes $p \ge 5$ dividing
**no** top number have $v_p(C(n,3)) = 0$ (Lemma L2.0), are not in
$\mathcal{P}(n)$, and impose no condition: a counterexample is not
required to have $p \nmid C(n,j)$ for them, and indeed typically
$p \mid C(n,j)$ is harmless there.

**Theorem L2.4 (PROVED — the completed system is a reformulation, not
a weakening; a correction to the brief's parenthetical).** For
$3 < j \le n/2$,
$$(n,j) \text{ satisfies (LD3⁺)} \;\Longleftrightarrow\;
\gcd(V_3(n), C(n,j)) = 1 \;\Longleftrightarrow\;
(n,3,j) \text{ is a counterexample.}$$

*Proof.* $\gcd(V_3(n), C(n,j)) > 1$ iff some prime $p \ge 3$ divides
both $V_3(n)$ and $C(n,j)$. By Lemma L2.0, $p \mid V_3(n)$ iff
$p \in \mathcal{P}(n)$. By Kummer, $p \mid C(n,j)$ iff some digit
position $e$ has $j_e(p) > n_e(p)$. So $\gcd > 1$ iff (LD3⁺) fails at
some $(p, e)$, and $\gcd = 1$ iff (LD3⁺) holds. The second equivalence
is the definition of a counterexample. $\square$

*Consequences, stated plainly.* The brief for this cluster describes
(LD3⁺) as "still only a necessary-condition system — a solution of
(LD3⁺) is not a counterexample". For the **truncated** system (LD3)
that description is correct (A1.16), and for any proper truncation of
(LD3⁺) it remains correct. But for the **completed** system it is
false, by Theorem L2.4: completing the digit conditions at every
$p \in \mathcal{P}(n)$ exactly closes the sufficiency gap, because the
gcd condition is, prime by prime, *nothing but* the digit conditions.
This has two honest implications, both used in §5. First,
unsatisfiability of (LD3⁺) would close $i = 3$ — indeed it is
*equivalent* to closing $i = 3$, so (H3⁺) is not a shortcut around the
problem; it is the problem restated digitwise. Second, (N1) and (N2),
which are independent extra filters relative to (LD3), are **redundant
given (LD3⁺)**: any (LD3⁺) solution is a counterexample
(Theorem L2.4), hence satisfies (N1) and (N2) by the A1.16 arguments.
Computational confirmation (script §A): for all $n \le 400$ and all
$3 < j \le n/2$ ($38{,}809$ pairs), (LD3⁺) satisfaction agrees with
$\gcd(V_3(n), C(n,j)) = 1$ in every pair, $0$ mismatches (and, as
expected, there are no solutions in that range).

## 2. Task L.2: the prime $p = 3$

**Proposition L2.5 (PROVED — the $p=3$ digits, all cases).** Let $\tau$
be the unique index in $\{0,1,2\}$ with $3 \mid n - \tau$, and
$a_\tau = v_3(n - \tau) \ge 1$.

(i) **Case $a_\tau = 1$:** $v_3(C(n,3)) = a_\tau - 1 = 0$, so
$3 \notin \mathcal{P}(n)$ and (LD3⁺) imposes **no** condition at
$p = 3$. This confirms that (LD3)'s omission of the $v_3 = 1$ case is
not a gap: when the unique $3$-divisible top has valuation $1$, the
factor $3$ in the numerator $n(n-1)(n-2)$ is exactly cancelled by the
$3$ in the denominator $6$, $3 \nmid V_3(n)$, and a counterexample is
free to have $3 \mid C(n,j)$ or not.

(ii) **Case $a_\tau \ge 2$:** $3 \in \mathcal{P}(n)$, and a
counterexample needs $3 \nmid C(n,j)$, i.e. full ternary digitwise
$j_e(3) \le n_e(3)$ for all $e \ge 0$. By Lemma L2.2 with
$p = 3$, $\rho = \tau < 3$, the low part ($e < a_\tau$) is exactly the
(LD3) clause $j \bmod 3^{a_\tau} \le \tau$; more explicitly, since
$j \bmod 3^{a_\tau} \le \tau < 3$ forces $j \bmod 3^{a_\tau}$ to be a
single ternary digit, the low part says:
- $\tau = 0$ ($v_3(n) \ge 2$): $j \bmod 3^{a_\tau} = 0$, i.e.
  $3^{a_\tau} \mid j$;
- $\tau = 1$ ($v_3(n-1) \ge 2$): $j \bmod 3^{a_\tau} \in \{0, 1\}$;
- $\tau = 2$ ($v_3(n-2) \ge 2$): $j \bmod 3^{a_\tau} \in \{0, 1, 2\}$.
The tail ($e \ge a_\tau$) is new: $\lfloor j / 3^{a_\tau} \rfloor$
digitwise $\le K_3 = (n - \tau)/3^{a_\tau}$ in base $3$, i.e.
$j_{a_\tau}(3) \le K_3 \bmod 3$, $j_{a_\tau+1}(3) \le
\lfloor K_3/3 \rfloor \bmod 3$, etc.

(iii) **Intersection with the residual class.** The residual class has
$n$ even; parity does not distinguish the $\tau$ cases — all three
occur with $n$ even (e.g. $v_3(n) \ge 2$ at $n = 18$; $v_3(n-1) \ge 2$
at $n = 10$; $v_3(n-2) \ge 2$ at $n = 20$) — and the other certified
residual conditions ($v_2(C(n,3)) \ge 4$, the Prop. 4.1 bounds) are
orthogonal to the ternary digits. So all three sub-cases of (ii), and
the vacuous case (i), survive into the residual as live possibilities
that any $p=3$ argument must respect.

*Proof.* (i) and the membership $3 \in \mathcal{P}(n) \iff a_\tau \ge 2$
are Lemma L2.0 at $p = 3$. (ii) is Theorem L2.3(i),(iii) at $p = 3$,
with Lemma L2.2 for the low part; the displayed forms of the low part
are $j \bmod 3^{a_\tau} \le \tau$ rewritten using $j \bmod 3^{a_\tau}
< 3$ (forced, as in Lemma L2.2). (iii) is by the displayed examples and
the absence of any parity content in the hypotheses. $\square$

**Proposition L2.6 (PROVED — the family $n = 3^a + 1$, $j = n/2$:
(LD3⁺) at $p=3$ gives no stronger exclusion than (LD3)).** Let
$a \ge 2$, $n = 3^a + 1$, $j = (3^a+1)/2$. Then $v_3(n-1) = a \ge 2$
(case $\tau = 1$ of Proposition L2.5), and the ternary expansions are:
$$n:\quad n_0 = 1,\ n_1 = \dots = n_{a-1} = 0,\ n_a = 1,\ n_e = 0
\ (e > a); \qquad
j:\quad j_0 = 2,\ j_1 = \dots = j_{a-1} = 1,\ j_a = 0,\ j_e = 0
\ (e > a).$$
Consequently $j$ violates digitwise $\le n$ at $p = 3$ at **exactly**
the low positions $0, 1, \dots, a-1$ (position $0$: $2 > 1$; positions
$1,\dots,a-1$: $1 > 0$), and the $p=3$ tail **passes**
($j_a = 0 \le 1 = n_a$; above $a$ both are $0$). Hence the exclusion of
this family by (LD3⁺) at $p = 3$ is the exclusion already effected by
the $3$-clause of (LD3) ($j \bmod 3^a = (3^a+1)/2 > 1$): it is neither
independent of nor stronger than the low-digit exclusion. (This family
satisfies the $\ge 5$ part of (LD3) — standing input from A1/A2 — so
$p = 3$ is the operative prime, and at the operative prime the tail is
silent.)

*Proof.* $n = 3^a + 1$ has the displayed expansion by definition of
base $3$. For $j$: $(3^a - 1)/2 = \sum_{k=0}^{a-1} 3^k$ (geometric
series), so $j = 1 + \sum_{k=0}^{a-1} 3^k = 2 + \sum_{k=1}^{a-1} 3^k$,
which is the displayed expansion (digits $2, 1, \dots, 1$, and $j < 3^a$
gives $j_a = 0$). The comparisons are then read off digit by digit.
Verified for $a = 2, \dots, 12$ in script §C3. $\square$

**Computation L2.7 (COMPUTATION — calibration on the six $\ge5$
solutions; script §C1–C2).** Brute force over all $n \le 2000$,
$3 < j \le n/2$ reproduces exactly the six solutions of the
$\ge 5$-only (LD3) system from P-A1:
$(10,5), (28,14), (82,41), (162,70), (244,122), (730,365)$. For each,
the digit machinery's exclusion is:

| $(n,j)$ | $a_\tau$ / $\tau$ | full-(LD3) witness | (LD3⁺) failing digits at $p=3$ | $\gcd(V_3(n), C(n,j))$ |
|---|---|---|---|---|
| $(10,5)$ | $2$ / $1$ | $j \bmod 9 = 5 > 1$ | $\{0,1\}$ | $3$ |
| $(28,14)$ | $3$ / $1$ | $j \bmod 27 = 14 > 1$ | $\{0,1,2\}$ | $9$ |
| $(82,41)$ | $4$ / $1$ | $j \bmod 81 = 41 > 1$ | $\{0,1,2,3\}$ | $135$ |
| $(244,122)$ | $5$ / $1$ | $j \bmod 243 = 122 > 1$ | $\{0,\dots,4\}$ | $81$ |
| $(730,365)$ | $6$ / $1$ | $j \bmod 729 = 365 > 1$ | $\{0,\dots,5\}$ | $1215$ |
| $(162,70)$ | $4$ / $0$ | $j \bmod 81 = 70 > 0$ | $\{0,1,2,3\}$ | $945$ |

In every case the failing ternary digits are **exactly the low
positions** $0,\dots,a_\tau - 1$ — the digit machinery reproduces the
(LD3) exclusion precisely, as Proposition L2.6 predicts for the five
$3^a+1$ members. (Some members also show redundant tail failures at
auxiliary primes — e.g. $(82,41)$ and $(730,365)$ fail at $p=5$,
position $1$; $(162,70)$ at $p=5$, positions $\{1,2\}$, and $p=7$,
position $1$ — but the pair is already excluded by the low $p=3$
digits, so these are not operative.)

**Computation L2.8 (COMPUTATION — the other named shapes; script
§C4–C5).** (a) $n = 3^a - 1$, $j = n/2$, $a = 2,\dots,8$: the $3$-adic
valuations of the tops are $(0, 0, 1)$ in every case, so by
Proposition L2.5(i) $3 \notin \mathcal{P}(n)$ — the $p=3$ digits are
irrelevant here, confirming the case analysis. Every member is killed
by the $\ge5$ part of (LD3) already (first witnesses: $q = 7$ at
$r = 1$ for $a = 2$; $q = 25$ at $r = 1$ for $a = 3$; $q = 79$, $241$,
$727$ at $r = 1$ for $a = 4, 5, 6$; $q = 5$ at $r = 1$ for $a = 7$;
$q = 7$ at $r = 1$ for $a = 8$). (LD3⁺) also fails for each, and at
$a = 4, 5$ there is a genuine tail failure at $p = 5$, position $1$
(while the $p=5$ low clause passes) — but it is redundant, the large
prime at $r = 1$ having already excluded the pair at digit $0$.
(b) $n = 2\cdot 3^a + 1$, $a = 2,\dots,6$, with
$j \in \{\lfloor n/3 \rfloor, \lfloor n/2 \rfloor\}$ (the shape does not
pin a canonical $j$; both natural choices were tested): every tested
pair is killed by (LD3) at $r = 0$ at digit $0$ (e.g. $q = 19 \mid n$
at $a = 2$; $q = 5 \mid n$ at $a = 3$, $j \bmod 5 \in \{2, 3\} > 0$).
**Conclusion of L.2's search:** in all tested families, no pair is
excluded by (LD3⁺) that (LD3) does not already exclude; where tail
failures occur they are redundant. This is evidence, not a theorem
about all families.

## 3. The tail is strictly stronger per prime (local strictness)

**Proposition L2.9 (PROVED — an infinite family where a single prime's
tail is decisive against its own low clause).** For every $w \ge 0$,
let $n = 50w + 30$ and $j = 25w + 15 = n/2$ (admissible range for
$w \ge 1$). At $p = 5$: $5 \Vert n$ (so $\rho = 0$, $a_5 = 1$,
$q_5 = 5$), the (LD3) clause at $p = 5$ **passes** ($j \bmod 5 = 0 \le
0$), but $\mathrm{Tail}(5)$ **fails at digit position $1$**:
$\lfloor n/5 \rfloor \bmod 5 = (10w + 6) \bmod 5 = 1$ while
$\lfloor j/5 \rfloor \bmod 5 = (5w + 3) \bmod 5 = 3 > 1$.

*Proof.* $n = 5(10w + 6)$ with $10w + 6 \equiv 1 \pmod 5$, so
$v_5(n) = 1$. $j = 5(5w + 3)$, so $5 \mid j$ and the low clause passes.
The digit-$1$ comparison is the displayed congruence computation.
Verified for $w = 0,\dots,200$ in script §D1. $\square$

Proposition L2.9 is a statement about one prime's condition in
isolation: the pairs $(50w+30, 25w+15)$ are **not** claimed to satisfy
the other primes' (LD3) clauses (e.g. $w = 0$ gives $(80, 40)$, killed
by $q = 79$ at $r = 1$). Its content is exactly that the (LD3⁺)
condition at a single prime is *strictly* stronger than the (LD3)
clause at that prime — the tail is not vacuous, and not implied by the
low clause.

**Computation L2.10 (COMPUTATION — how often the tail is the decisive
part; script §D2).** Over all instances $(n, j, p)$ with $n \le 2000$,
$3 < j \le n/2$, $p \in \mathcal{P}(n)$ — $4{,}711{,}997$ instances in
total — the low part at $p$ and the tail at $p$ were tested separately
(low via the proved equivalent form $j \bmod q_p \le \rho(p)$, tail
digit-by-digit on $\lfloor j/q_p \rfloor$ against $K_p$):
$$\text{low fails: } 4{,}182{,}943; \qquad
\text{low passes, tail passes: } 225{,}801; \qquad
\text{low passes, tail fails: } 303{,}253.$$
So among the $529{,}054$ instances where the (LD3) clause at $p$
passes, the tail fails in $303{,}253$ cases ($57.3\%$): at the
single-prime level the tail is decisive in the majority of
low-passing instances. (LD3⁺) is a genuinely stronger condition than
(LD3), instance by instance. The question of §4 is whether that
strength is ever *operative on the residual class as a whole* — i.e.
whether any configuration can pass all the low clauses and all
certified Cycle 1–2 filters simultaneously, so that a tail could be
the thing that kills it.

## 4. Task L.3: does (LD3⁺) bite inside the residual class?

The residual configurations left open by F1.11/F2.14 split into
$h = 1$ rows ($R \in \{0,1,2\}$) and $h = 0$ rows ($R \ge 3$). In the
$h = 0$ rows every relevant prime power is $\le T$
(F1.9(a)/F2.13), so $V_3(n) \mid \Lambda_3(T)$ is a *fixed* finite
bound per row. The following lemma — implicit in F2.13 but not stated
there — makes those rows globally finite, which is what makes the
enumerations below complete rather than bounded searches.

**Lemma L2.11 (PROVED — every $h=0$ row is globally finite).** Fix
$(Q, R)$ with $R \ge 3$, put $T = R + 2(Q-1)$ and
$\Lambda = \Lambda_3(T)$. If $(n, 3, j)$ is a counterexample in this
row with $n$ even, then
$$n - 1 \;\in\; \mathcal{F}(\Lambda) := \{\,3^b u : u \mid \Lambda,\
\gcd(u, 3) = 1,\ 0 \le b \le v_3(\Lambda) + 1\,\},$$
hence $n \le 3^{v_3(\Lambda)+1} \cdot \big(\Lambda /
3^{v_3(\Lambda)}\big) + 1$: the row contains only finitely many
potential counterexamples, explicitly enumerable.

*Proof.* In an $h = 0$ row, Proposition 4.1 (F2.3/F1.9(a)) gives
$V_3(n) \mid \Lambda_3(T) = \Lambda$ for a counterexample. The odd top
$m = n - 1$ factors as $m = 3^\beta U_1$ with $U_1$ its $\ge 5$ part
($\gcd(U_1, 3) = 1$). Now $U_1 \mid V_3(n)$: indeed
$V_3(n) = U_0 U_1 U_2 \cdot 3^{e-1}$ with pairwise coprime factors
(the $U_r$ are coprime across tops, a prime $\ge 5$ dividing at most
 one top). Hence $U_1 \mid \Lambda$ and $\gcd(U_1, 3) = 1$. If
$\beta \ge 1$ then $m$ is the unique $3$-divisible top, so $e = \beta$
and $3^{\beta - 1} \mid V_3(n) \mid \Lambda$, giving
$\beta \le v_3(\Lambda) + 1$; if $\beta = 0$ the same bound holds
trivially. Therefore $m \in \mathcal{F}(\Lambda)$, and the bound on
$n$ is the maximum element of $\mathcal{F}(\Lambda)$ plus $1$.
$\square$

Validated directly (script §E): for every even $n \le 200{,}000$ and
every $\Lambda \in \{15, 105, 315, 3465, 45045, 765765, 14549535\}$
(the values at $T \le 20$), $V_3(n) \mid \Lambda$ implies
$n - 1 \in \mathcal{F}(\Lambda)$; $0$ violations.

**Computation L2.12 (COMPUTATION — the $(2,4)$ class, enumerated two
ways to $n \le 10^8$; script §F1).** Row $(Q,R) = (2,4)$: $T = 6$,
$\Lambda_3(6) = 15$, $V_3(n) \mid 15$ for a counterexample (F2.13).

*Method A (the brief's parametrisation: the $2$-power varies, the odd
part ranges over a finite set).* $V_3(n) \mid 15$ forces the odd part
of the even number $n$ to be $3^b u$ with $b \le 2$, $u \in \{1, 5\}$,
i.e. in $\{1, 3, 9, 5, 15, 45\}$. The values $n = 2^\alpha \cdot o \le
10^8$ with $o$ in that set number exactly $146$; among them,
$V_3(n) \mid 15$ holds only for $n = 6$ and $n = 10$ — neither of which
lies in the row with $j > 3$ ($j = (n-4)/2$ gives $j = 1$ and $j = 3$).

*Method B (Lemma L2.11).* $\mathcal{F}(15) = \{1, 3, 5, 9, 15, 45\}$,
so a counterexample in the row has $n \in \{2, 4, 6, 10, 16, 46\}$
(global bound $n \le 46$, so the $10^8$ range is globally exhaustive,
not a truncation). The in-row candidates with $j > 3$ are exactly
$(16, 6)$ and $(46, 21)$: **stage 1 count $2$**. Both fail the
$V_3(n) \mid 15$ filter itself ($V_3(16) = 35$; $23 \mid V_3(46)$):
**stage 2 count $0$**. Consequently (LD3) is tested on $0$ candidates
and (LD3⁺) on $0$ candidates — both survivor counts are $0$, vacuously.
The row contains no counterexample for any $n$ (via Proposition 4.1 +
Lemma L2.11); both candidate pairs were in any case already closed by
the certified per-pair frontier ($j = 6, 21 \le 5000$).

Since (LD3) — indeed the $V$-filter before it — already empties the
$(2,4)$ class, per the brief the next thinnest classes were enumerated.

**Computation L2.13 (COMPUTATION — $(2,6)$, $(3,4)$, and the $(4,2)$
cross-check; script §F2–F3).** Rows $(2,6)$ and $(3,4)$ are the
$h = 0$ rows with $T = 8$, $\Lambda_3(8) = 105$; Lemma L2.11 gives the
global bound $n \le 316$ ($\mathcal{F}(105)$ has maximum $315$).

- $(2,6)$: stage 1 (in-row, $n - 1 \in \mathcal{F}(105)$, $j > 3$):
  $7$ candidates $(16,5), (22,8), (36,15), (46,20), (64,29), (106,50),
  (316,155)$. Stage 2 ($V_3(n) \mid 105$): exactly $1$, namely
  $(16, 5)$. (LD3) kills it (witness $q = 7 \Vert (n - 2)$, $r = 2$:
  $5 \bmod 7 = 5 > 2$; $\gcd(V_3(16), C(16,5)) = 7$). (LD3⁺) fails for
  it at $p = 7$, digit $0$ — the low digit, not the tail. (LD3)
  survivors: $0$. (LD3⁺) survivors: $0$.
- $(3,4)$: stage 1: $6$ candidates $(16,4), (22,6), (46,14), (64,20),
  (106,34), (316,104)$. Stage 2: exactly $1$, namely $(16, 4)$ —
  with $j = 4$ in the already-closed region $j \le 3i/2$. (LD3) kills
  it (witnesses $q = 5$ at $r = 1$: $4 \bmod 5 = 4 > 1$; $q = 7$ at
  $r = 2$: $4 \bmod 7 = 4 > 2$). (LD3⁺) fails at digit $0$ of $p = 5$
  and $p = 7$. (LD3) survivors: $0$. (LD3⁺) survivors: $0$.
- $(4,2)$ ($h = 1$, $T = 8$, $\Lambda_3 = 105$; the brief's suggested
  comparison class): the F1.9(b)/V-F §5 finite analysis leaves
  exactly the three candidates $(22,5), (46,11), (106,26)$ (from
  $n - 1 = 3^b 5^a 7^c$, $b \le 2$, $a, c \le 1$, $n - 1 \equiv 1
  \pmod 4$), reproduced by the script. Each is killed by (LD3) —
  witnesses $q = 11 \Vert n$ ($5 \bmod 11 = 5 > 0$), $q = 23 \Vert n$
  (and $q = 9$ at $r = 1$) resp. $q = 53 \Vert n$ — with
  $\gcd = 77, 69, 371$, and each (LD3⁺) failure includes digit $0$
  (the low digit) at the witnessing prime. (LD3⁺) survivors: $0$.

**Computation L2.14 (COMPUTATION — aggregate $h=0$ sweep, globally
complete per row; script §F4).** The pipeline of Lemma L2.11 +
$V$-filter + (LD3) + (LD3⁺) was run for **every** $h = 0$ row with
$Q \in \{2, \dots, 8\}$ and $T \le 20$ — $70$ rows. Totals: stage 1
candidates $1{,}942$; stage 2 ($V_3(n) \mid \Lambda_3(T)$) pairs $79$,
with largest $n = 210$ and largest $j = 96$ among them; **every one
of the $79$ is killed by (LD3) with an explicit witness** (asserted in
the script, and each has $\gcd > 1$); (LD3) survivors $0$; (LD3⁺)
survivors $0$, vacuously. The stage-1 enumeration is globally complete
for each row by Lemma L2.11 (not a search to a bound), and was
additionally cross-checked by brute force over all $n$ in each row up
to $200{,}000$ (script §F, `row_pipeline`): agreement in every row.
Honesty note: every stage-2 pair has $j \le 96 \le 5000$, so all were
already closed by the certified per-pair frontier; the content of
L2.12–L2.14 is not new pair closures. It is that the Prop. 4.1 +
odd-top finiteness route *independently and globally* empties these
rows, and that **at no point in any of these residual populations is
(LD3⁺) the operative filter** — the $V$-filter or a low digit always
fires first.

**Summary of L.3's evidence.** Inside the residual class, the
populations that can currently be delimited at all (fixed $h = 0$
rows; the $(4,2)$ row; the certified range $n \le 10^6$ for (LD3)
itself) contain **no (LD3) survivor at all**, hence no configuration
on which a tail condition could be the operative exclusion. Combined
with §3, the picture is: tails are strong locally (per prime) and
vacuous marginally (on every delimited residual population), because
the low digits — or the Prop. 4.1 $V$-bound before them — already
exclude everything there.

## 5. Task L.4: verdict on (H3)

**Statement (H3⁺).** (LD3⁺) has no solutions $(n, j)$ with
$3 < j \le n/2$.

**Theorem L2.15 (PROVED — the exact logical relations).**
(i) $\mathrm{Sol}(\mathrm{LD3}^+) \subseteq \mathrm{Sol}(\mathrm{LD3})$
(Theorem L2.3(ii)); hence **(H3) $\Rightarrow$ (H3⁺)**: if (LD3) has
no solutions, neither does its strengthening.
(ii) **(H3⁺) $\iff$ $i = 3$ is closed** (no counterexample exists):
a solution of (LD3⁺) in range *is* a counterexample
(Theorem L2.4), and a counterexample satisfies (LD3⁺)
(Theorem L2.3(i)). In particular unsatisfiability of (LD3⁺) **would**
close $i = 3$ — the A1.16-style necessity argument goes through
verbatim, with (LD3⁺) in place of (LD3) — but by the same token
proving (H3⁺) is *exactly* as strong as closing $i = 3$; it is a
reformulation, not a reduction of difficulty.
(iii) **(H3⁺) does not imply (H3).** (H3) is the strictly stronger
statement. If an (LD3) solution exists, then by (ii) it is not a
counterexample, hence by Theorem L2.4 it fails (LD3⁺); since its low
parts all pass (it satisfies (LD3)), it must fail some
$\mathrm{Tail}(p)$: *every* (LD3) solution is killed by a tail
condition or is a counterexample, with no third possibility. So
(H3) could fail while (H3⁺) holds, the difference being measured
exactly by tail-killed (LD3) solutions — of which none are currently
known at any size ((LD3) has no solution with $n \le 10^6$, certified,
and none in any population delimited in §4).
(iv) **(N1)/(N2) independence, settled.** Relative to (LD3), (N1)
and (N2) are independent additional necessary conditions (they are
not digit conditions and do not follow from (LD3)). Relative to
(LD3⁺) they are **redundant**: an (LD3⁺) solution is a
counterexample (Theorem L2.4) and therefore satisfies (N1) and (N2)
by the standing A1.16 arguments. The $p = 3$ case is fully included
in these relations: $\mathcal{P}(n)$ contains $3$ exactly when
$3 \mid V_3(n)$ (Lemma L2.0, Proposition L2.5(i)).

**Claim L2.16 (the verdict: option (b)).** **(LD3⁺) is strictly
stronger than (LD3) as a condition — proved per prime
(Proposition L2.9) and quantified computationally
(Computation L2.10: the tail is decisive in $303{,}253$ of
$529{,}054$ low-passing prime instances at $n \le 2000$) — but no
general shrinkage of the residual class by (LD3⁺) is proved, and on
every residual population that can currently be delimited, its
marginal effect is exactly zero (Computations L2.12–L2.14:
(LD3) survivors $0$ everywhere, so there is no survivor for a tail
to kill).**

*The exact point where the proof attempt stops.* A general shrinkage
proof would require a certified input that constrains the tail
variables — the digits of $\lfloor j / q_p \rfloor$ against $K_p$.
Every certified input constrains something else: (LD3) and the
splitting conditions constrain $j \bmod q_p$ (the low digits);
Proposition 4.1 constrains the prime powers themselves ($q_p \le T$,
or $q_p \mid j$, per F1.9/F2.9) and, in its proof (F2.2), records
residues $j \bmod p^a$ and $c \bmod p^a$ — again low digits, the same
truncation; (N2) and the size bounds constrain $|j|$ relative to
$n$. Nothing in the certified record says anything about
$\lfloor j/q_p \rfloor \bmod p$. And no incompatibility can be
expected from counting alone: for fixed $n$ and $p$, digitwise $\le$
is a box condition — the number of $j \in [0, p^L)$ satisfying the
full digitwise condition at $p$ is $\prod_{e < L} (n_e(p) + 1) \ge 1$,
positive and typically large — and conditions at distinct primes
live in different bases, where no CRT-type incompatibility is
available. A shrinkage proof therefore needs a genuinely new input
linking the quotient $\lfloor j/q_p \rfloor$ to the splitting data;
none is presently known, and this is exactly where the attempt
stops. Options (a) and (c) are both rejected on the evidence: (a)
fails because no sub-configuration of the residual class is excluded
by a tail argument for all $n$ (the $h = 0$ row closures of §4 are
effected by the $V$-filter and low digits, not by tails); (c) fails
because the tail is demonstrably non-vacuous per prime
(Proposition L2.9, Computation L2.10) — it adds content beyond
(LD3) + the certified filters, just not content that has yet been
operative on a delimited residual population.

## 6. Closing statement for Cluster L

*Proved in this file:*
1. The exact formulation of (LD3⁺) (Definition L2.1), its necessity
   for a counterexample, and the splitting (LD3⁺) = (LD3) ∧ tails
   with the tail at $p$ stated as digitwise comparison of
   $\lfloor j/q_p \rfloor$ against $K_p = (n - \rho(p))/q_p$
   (Theorem L2.3).
2. The low-digit precision point: digitwise on digits $0..a-1$ is
   **exactly** $j \bmod q \le \rho$, in all sub-cases, the load-bearing
   fact being $\rho \le 2 < p$ (Lemma L2.2, with $1{,}101{,}758$
   computational instances in agreement).
3. The completed system is equivalent to the counterexample condition
   itself (Theorem L2.4), correcting the "only necessary" framing:
   (H3⁺) ⟺ ($i = 3$ closed), (H3) ⇒ (H3⁺), (H3⁺) ⇏ (H3), and
   (N1)/(N2) are redundant given (LD3⁺) though independent of (LD3)
   (Theorem L2.15).
4. The $p = 3$ analysis: $v_3(\text{top}) = 1$ correctly imposes no
   condition; for $v_3 \ge 2$ the three cases $\tau = 0, 1, 2$ with
   explicit low parts and tails (Proposition L2.5). The family
   $n = 3^a + 1$, $j = n/2$ is excluded at exactly the low ternary
   digits, its $p=3$ tail passing: (LD3⁺) gives no stronger exclusion
   of it (Proposition L2.6).
5. Per-prime strictness of the tail: the infinite family
   $n = 50w + 30$, $j = n/2$ at $p = 5$ (Proposition L2.9).
6. Global finiteness of every fixed $h = 0$ row, via the odd top:
   $n - 1 \in \mathcal{F}(\Lambda_3(T))$ (Lemma L2.11).

*Reduced / computed:*
7. Calibration: the six $\ge 5$ (LD3) solutions reproduced, each
   excluded by (LD3⁺) at exactly the low ternary digits
   (Computation L2.7); the shapes $3^a - 1$ and $2\cdot 3^a + 1$
   tested, all excluded by (LD3) already, tail failures where present
   being redundant (Computation L2.8). Instance counts quantifying
   the tail's local decisiveness (Computation L2.10).
8. Residual populations: row $(2,4)$ enumerated to $10^8$ by two
   parametrisations (globally exhaustive; stage counts $2 \to 0$);
   rows $(2,6)$, $(3,4)$ (stage counts $7 \to 1 \to 0$ and
   $6 \to 1 \to 0$ through the $V$-filter and (LD3)); the $(4,2)$
   candidates disposed by (LD3); the aggregate $h = 0$ sweep
   ($70$ rows, $T \le 20$: $1{,}942$ stage-1 candidates, $79$
   stage-2 pairs, all (LD3)-killed, (LD3⁺) survivors $0$ vacuously)
   (Computations L2.12–L2.14).

*Still OPEN, explicitly:* (H3) and (H3⁺) in general — by
Theorem L2.15(ii), (H3⁺) is exactly the $i = 3$ problem in digit
form; the residual even class of F1.11/F2.14 outside the delimited
rows of §4 (in particular all $h = 1$ rows beyond the closed ones,
and $h = 0$ rows with $T > 20$ as a uniform statement, though each
fixed such row is finite by Lemma L2.11); and the missing input
identified in Claim L2.16 (any certified constraint on
$\lfloor j/q_p \rfloor$). **$i = 3$ is not closed, and #699 is not
claimed solved.**

## 7. Verification log

All numbers above are outputs of `proofs/P-L2_checks.py`
(Python stdlib only, exact arithmetic; the script asserts every
headline value; measured total runtime $942.9$ s on this machine,
dominated by §D's instance census and §F's per-row brute-force
cross-checks):
- §A: (LD3⁺) ⟺ $\gcd(V_3(n), C(n,j)) = 1$, exhaustive $n \le 400$:
  $38{,}809$ pairs, $0$ mismatches, $0$ solutions.
- §B: low-digit equivalence (Lemma L2.2), exhaustive $n \le 1000$:
  $1{,}101{,}758$ instances, $0$ mismatches.
- §C: $\ge 5$-only (LD3) solutions $n \le 2000$ are exactly the six
  of P-A1; the $p=3$ failing-digit table of Computation L2.7; the
  ternary digit patterns of Proposition L2.6 asserted for
  $a = 2,\dots,12$; the $3^a - 1$ valuation pattern $(0,0,1)$ and
  (LD3) witnesses for $a = 2,\dots,8$; the $2\cdot 3^a + 1$
  witnesses at $r = 0$ for $a = 2,\dots,6$.
- §D: the $p=5$ strictness family asserted for $w = 0,\dots,200$;
  the instance counts of Computation L2.10 ($4{,}711{,}997$
  instances: low fails $4{,}182{,}943$; low passes/tail passes
  $225{,}801$; low passes/tail fails $303{,}253$).
- §E: Lemma L2.11 validated for all even $n \le 200{,}000$ at the
  seven values $\Lambda \in \{15, 105, 315, 3465, 45045, 765765,
  14549535\}$: $0$ violations.
- §F: row $(2,4)$ by both parametrisations ($146$ candidates in
  Method A, members $\{6, 10\}$; stage counts $2 \to 0$ in
  Method B); rows $(2,6)$, $(3,4)$ stage counts and witnesses;
  the $(4,2)$ candidate set $\{(22,5), (46,11), (106,26)\}$ with
  gcds $77, 69, 371$; the aggregate $h=0$ sweep ($70$ rows,
  stage 1 total $1{,}942$, stage 2 total $79$, largest stage-2
  $n = 210$, $j = 96$, (LD3) survivors $0$, (LD3⁺) survivors $0$),
  with a brute-force cross-check of the stage-1/stage-2 pipeline
  in every row up to $n \le 200{,}000$.
