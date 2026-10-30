# Prover J2 (independent): Cluster J — the $v_2$ condition and refined comparisons at $i=3$, Cycle 3

Prover: J2, working independently in Cycle 3. The second prover on this
cluster (J1) was **not** read; no file of J1's was opened. Sources read:
`CYCLE2.md` §2; `proofs/P-F1.md` (especially Claims F1.12–F1.14);
`proofs/P-F2.md` §§1, 4.1 (Theorem F2.15, Corollary F2.16);
`verification/V-F.md`; `proofs/P-A1.md` (Lemma A1.15, Proposition A1.16,
Statement (H3)). Every computation below is in `proofs/P-J2_checks.py`
(Python standard library only, exact integer and `Fraction` arithmetic, no
randomness; total runtime under 10 seconds on this machine, all assertions
passing). Every numbered claim is labelled PROVED, GAP, FALSE, OPEN, or
COMPUTATION.

**Headline.** $i=3$ is **not** closed here, and (H3) is **not** proved.
What is new in this file: (a) a complete, self-contained $v_2$ theory for
$C(n,3)$ (§1): the set $\{n : v_2(C(n,3)) \ge v\}$ is a union of exactly
$5$ residue classes modulo $2^{v+1}$ for every $v \ge 2$ (and $3$ classes
modulo $4$ for $v=1$), with the brief's characterisations at $v=4$
**verified correct**; (b) the $Q$-stratification (§2): a counterexample in
row $Q$ forces $v_2(C(n,3)) \ge v_{\min}(Q) = \lfloor 3\log_2 Q\rfloor + 1$,
confirming the hypothesised values $v_{\min}(2)=4$, $v_{\min}(3)=5$,
$v_{\min}(4)=7$, with densities $5/2^{v_{\min}(Q)+1}$; (c) the intersection
with the residual class (§3): exact congruence translations per row, an
exact per-$(Q,R)$ finiteness table from Proposition 4.1's squared half,
and the combined picture per row; (d) the F1.14 GAP is **settled, and the
sentence is FALSE** (§4): the $V_3$-refined comparison closes the pair
$(3,j)$ for all $n$ **if and only if** $j \in \{6, 10\}$ among $j > 5$ —
for every other $j > 5$ an explicit witness $n \in [2j, N(3,j)]$ with
$V_3(n) \le C(j,3)$ exists (for $j \ge 19$, the least power of $2$ that is
$\ge 2j$); (e) a new hybrid comparison (§4, Claim J2.12) combining the
maximal-valuation bound $2^{v_2(C(n,3))} \le n$ with Proposition 4.1's
divisibility cap, which is sharper than the squared half in every row
computed and, combined with the certified $j \le 5000$ closure, **closes
the rows** $(2, R)$ for even $4 \le R \le 20$, $(3, R)$ for
$1 \le R \le 18$, and $(4, R)$ for even $2 \le R \le 16$, for all $j$.

## 0. Standing inputs and notation

$C(n,k) = \binom nk$; $V_3(n) = C(n,3)/2^{v_2(C(n,3))}$ is the odd part of
$C(n,3)$ (at $i=3$ the only prime $< 3$ is $2$, so this agrees with the
campaign's $V_3$); a **counterexample** is a triple $(n,3,j)$,
$3 < j \le n/2$, with $\gcd(V_3(n), C(n,j)) = 1$. Used as certified ground
truth (per the assignment, CYCLE2 §2, and V-F): the key lemma and its
consequence **(N2)** $V_3(n) \mid C(j,3)$; **(N1)**; the system **(LD3)**
(Lemma A1.15 / Proposition A1.16(i)); the finite reduction
$n \le N(3,j) := \max\{n : C(n,3) < C(2j,6)\}$; Price Proposition 4.1 at
$i=3$ (Claims F1.1/F1.2, Theorem F2.3): with $n = Qj + R$,
$Q = \lfloor n/j \rfloor \ge 2$, $0 \le R < j$, $T = R + 2(Q-1)$,
$h = \max(0, \lceil (3-R)/Q \rceil)$,
$$V_3(n) \mid \Lambda_3(T)\binom{j}{h},
\qquad C(n,3) < \Bigl(\Lambda_3(T)\binom{j}{h}\Bigr)^2,$$
where $\Lambda_3(T) = \prod_{q \ge 3} q^{\lfloor \log_q T \rfloor}$;
the label bounds of Claim F1.9 / Corollary F2.4 (in $h=0$ rows every
prime-power part of $V_3(n)$ is $\le T$; a genuine split part at a prime
$\ge 5$ is $\le T$); the closures of rows
$(Q,R) \in \{(2,0), (2,2), (3,0), (3,2), (4,0)\}$ (Claim F1.10, and
$(2,0)$ also by Price's $n=2j$ closure); SPLIT-odd closed (Claims
F1.5/F2.7), so a counterexample has $n$ **even**; (LD3) has no solution
with $n \le 10^6$, and every pair $(3,j)$ with $j \le 5000$ is closed for
all $n$ (Claims F1.16/F1.17, Computation F2.18, all V-F certified).
**Net residual class (certified):** a counterexample has $n$ even,
$j \ge 5001$, $n > 10^6$, and $v_2(C(n,3)) \ge 4$ (Theorem F2.15 /
Claim F1.13). $s_2(m)$ is the binary digit sum; $v_p$ is the $p$-adic
valuation. "Row $(Q,R)$" always means the set of triples with
$\lfloor n/j \rfloor = Q$ and $n - Qj = R$; in a row, $n$ is determined
by $j$.

No certified input read for this cluster was found to be wrong. The one
item flagged in the brief as suspect-by-omission — the final sentence of
Claim F1.14 — is indeed false; see Claim J2.11, where the two
counterexample pairs are exhibited and proved.

## 1. J.1: Exact $v_2$ theory

**Claim J2.1 (PROVED — Legendre/Kummer forms of $v_2(C(n,3))$).**
For $n \ge 3$, the following are equal:
(i) $v_2(C(n,3))$;
(ii) $s_2(3) + s_2(n-3) - s_2(n) = 2 + s_2(n-3) - s_2(n)$;
(iii) the number of carries, counted with multiplicity (one per bit
position whose carry-out is $1$), when adding $(n-3) + 3$ in binary;
(iv) the number of bit positions whose borrow-out is $1$ when subtracting
$3$ from $n$ in binary;
(v) $\sum_{k \ge 1} e_k$, where
$e_k = \lfloor n/2^k \rfloor - \lfloor 3/2^k \rfloor -
\lfloor (n-3)/2^k \rfloor \in \{0,1\}$, and $e_k = 1$ iff
$n \bmod 2^k < 3 \bmod 2^k$.

*Proof.* Legendre's formula at $p=2$ gives
$v_2(C(n,3)) = \sum_{k\ge1} e_k$ directly, and $e_k \in \{0,1\}$ since
$e_k = \lfloor x+y \rfloor - \lfloor x \rfloor - \lfloor y \rfloor$ for
$x = (n-3)/2^k$, $y = 3/2^k$. Now $e_k = 1$ iff the lowest $k$ bits of
$(n-3)$ and $3$ sum to at least $2^k$, i.e. iff adding them produces a
carry across the $2^k$ boundary; since
$n \bmod 2^k = \bigl((n-3)\bmod 2^k + 3 \bmod 2^k\bigr) \bmod 2^k$, this
overflow happens iff $n \bmod 2^k < 3 \bmod 2^k$. Summing over $k$ counts
each carry position once, giving (iii); and a borrow crosses the $2^k$
boundary in the subtraction $n - 3$ under exactly the same condition
$n \bmod 2^k < 3 \bmod 2^k$ (borrow out of bit position $k-1$ iff the
low $k$ bits of $n$ are smaller than those of $3$), giving (iv). For
(ii), the binary form of Legendre's identity,
$v_2(m!) = \sum_k \lfloor m/2^k \rfloor = m - s_2(m)$ (because writing
$m = \sum_i b_i 2^i$ gives $\sum_k \lfloor m/2^k \rfloor =
\sum_i b_i (2^i - 1)$), applied to $m = n, 3, n-3$ gives
$v_2(C(n,3)) = [n - s_2(n)] - [3 - s_2(3)] - [(n-3) - s_2(n-3)]
= s_2(3) + s_2(n-3) - s_2(n)$. (Script §A1 verifies all four forms agree
for $3 \le n \le 20{,}000$.) $\square$

**Claim J2.2 (PROVED — characterisations; the brief's forms are
correct).** Since $v_2(6) = 1$,
$v_2(C(n,3)) = v_2(n(n-1)(n-2)) - 1$, so
$v_2(C(n,3)) \ge v \iff v_2(n(n-1)(n-2)) \ge v+1$ for every $v$.
Moreover, for every $v \ge 1$:
- **$n$ even:** $v_2(C(n,3)) \ge v \iff 2^v \mid n$ or $2^v \mid (n-2)$.
- **$n$ odd:** $v_2(C(n,3)) \ge v \iff 2^{v+1} \mid (n-1)$.

In particular at $v=4$: $v_2(C(n,3)) \ge 4 \iff
v_2(n(n-1)(n-2)) \ge 5$; for $n$ even $\iff 16 \mid n$ or $16 \mid (n-2)$;
for $n$ odd $\iff 32 \mid (n-1)$. **The brief's three forms are verified,
not corrected.**

*Proof.* If $n$ is odd, only $n-1$ among the three factors is even, so
$v_2(n(n-1)(n-2)) = v_2(n-1)$, and the claim is the definition of
valuation. If $n$ is even, $n-1$ is odd and
$v_2(n(n-1)(n-2)) = v_2(n) + v_2(n-2)$; exactly one of $n, n-2$ is
$\equiv 2 \pmod 4$, so $\min(v_2(n), v_2(n-2)) = 1$ and
$v_2(n) + v_2(n-2) \ge v+1 \iff \max(v_2(n), v_2(n-2)) \ge v
\iff 2^v \mid n$ or $2^v \mid (n-2)$. (Script §A3 verifies both parity
forms for $n \le 100{,}000$ and $v \in \{1,2,3,5,6,7\}$.) $\square$

**Claim J2.3 (PROVED — periodicity, exact class counts, densities).**
For each $v \ge 0$, $\{n : v_2(C(n,3)) \ge v\}$ is a union of residue
classes modulo $2^{v+1}$. The number of classes, and the natural density,
are:
- $v = 0$: all $n$ ($2$ classes mod $2$), density $1$;
- $v = 1$: $3$ classes mod $4$, namely $\{0, 1, 2\}$, density $3/4$;
- $v \ge 2$: exactly $5$ classes mod $2^{v+1}$, namely
  $$\{\,0,\ 1,\ 2,\ 2^v,\ 2^v + 2\,\} \pmod{2^{v+1}},$$
  density $5/2^{v+1}$.

Explicitly: $v=4$: $\{0, 1, 2, 16, 18\} \pmod{32}$ (density $5/32$);
$v=5$: $\{0, 1, 2, 32, 34\} \pmod{64}$ (density $5/64$);
$v=6$: $\{0, 1, 2, 64, 66\} \pmod{128}$ (density $5/128$).

*Proof.* Whether $v_2(m) \ge v+1$ holds, and the value of $v_2(m)$ when
it is $\le v$, are both determined by $m \bmod 2^{v+1}$; hence whether
$v_2(n) + v_2(n-1) + v_2(n-2) \ge v+1$ holds is determined by
$n \bmod 2^{v+1}$, proving periodicity. For the count, use Claim J2.2.
Odd $n$: the condition is $n \equiv 1 \pmod{2^{v+1}}$ — exactly one
class, for every $v \ge 1$. Even $n$: the condition is
$2^v \mid n$ or $2^v \mid (n-2)$, i.e.
$n \bmod 2^{v+1} \in \{0, 2^v\} \cup \{2, 2^v+2\}$. The two conditions are
disjoint for $v \ge 2$ (both would force $2^v \mid 2$), and the four
classes are distinct modulo $2^{v+1}$ for $v \ge 2$
($2^v \not\equiv 0, 2$ and $2^v + 2 \not\equiv 0, 2 \pmod{2^{v+1}}$ since
$0 < 2^v + 2 < 2^{v+1}$), giving $4 + 1 = 5$ classes. For $v = 1$ the two
conditions coincide (every even $n$ satisfies both), giving
$\{0, 2\} \cup \{1\} = 3$ classes mod $4$. The case $v=0$ is vacuous.
Density is class count divided by modulus, by periodicity. (Script §A2
verifies periodicity and the class lists for $0 \le v \le 8$.) $\square$

*Corollary (recovery of F2.16).* $\{n : v_2(C(n,3)) \le 3\}$ has density
$1 - 5/32 = 27/32$, and $v_2(C(n,3)) \ge 4$ is the certified necessary
condition of Theorem F2.15 / Claim F1.13. Within the residual class
($n$ even) only the four classes $\{0, 2, 16, 18\} \pmod{32}$ survive:
density $1/8$ over all $n$, i.e. $1/4$ of even $n$.

## 2. J.2: $Q$-stratification

**Claim J2.4 (PROVED — behaviour of $\rho(Q, \cdot)$).** For $Q \ge 2$,
$$\rho(Q, j) := \frac{C(Qj, 3)}{C(j, 3)}
= \prod_{t=0}^{2} \frac{Qj - t}{j - t}
= Q \cdot \Bigl(Q + \frac{Q-1}{j-1}\Bigr)
\cdot \Bigl(Q + \frac{2(Q-1)}{j-2}\Bigr).$$
Hence $\rho(Q, \cdot)$ is **strictly decreasing** in $j$ (for $j \ge 3$),
$\rho(Q, j) > Q^3$ for every finite $j$, and
$\inf_j \rho(Q, j) = \lim_{j \to \infty} \rho(Q, j) = Q^3$, the infimum
never attained.

*Proof.* $C(Qj,3)/C(j,3) = \prod_{t=0}^2 (Qj-t)/(j-t)$ by cancelling the
factors $1/6$. And $(Qj - t) = Q(j - t) + t(Q-1)$, so
$(Qj-t)/(j-t) = Q + t(Q-1)/(j-t)$: constant $Q$ at $t=0$, strictly
decreasing in $j$ at $t = 1, 2$ (as $Q > 1$). A product of positive
strictly decreasing functions is strictly decreasing; each factor tends
to $Q$ and exceeds the next factor's value, and the $t \ge 1$ factors
strictly exceed $Q$, so $\rho > Q^3$ with limit $Q^3$. (Script §C1
verifies strict decrease and $\rho > Q^3$ exactly, in `Fraction`s, for
$2 \le Q \le 10$, $4 \le j \le 500$.) $\square$

**Claim J2.5 (PROVED — the uniform $v_{\min}(Q)$; the brief's hypothesis
is confirmed).** Let $(n, 3, j)$ be a counterexample in row $Q$
($n \ge Qj$). Then
$$v_2(C(n,3)) \;\ge\; v_{\min}(Q) \;:=\; \lfloor 3 \log_2 Q \rfloor + 1
\;=\; \min\{v : 2^v > Q^3\}.$$
In particular $v_{\min}(2) = 4$, $v_{\min}(3) = 5$, $v_{\min}(4) = 7$ —
**the hypothesised values are verified, not corrected.** The bound is
the best uniform bound this argument yields: $v = v_{\min}(Q)$ is not
excluded, since $\rho(Q, j) \to Q^3 < 2^{v_{\min}(Q)}$.

*Proof.* By (N2), $V_3(n) \le C(j,3)$, so
$2^{v_2(C(n,3))} = C(n,3)/V_3(n) \ge C(n,3)/C(j,3) \ge C(Qj,3)/C(j,3)
= \rho(Q, j) > Q^3$ (Claim J2.4; $C(\cdot, 3)$ is increasing and
$n \ge Qj$). An integer strictly exceeding $3 \log_2 Q$ is at least
$\lfloor 3 \log_2 Q \rfloor + 1$. The boundary care the brief asked for
is exactly the strictness $\rho > Q^3$: at $Q = 4$, $2^6 = 64 = Q^3$
would **not** suffice, because $2^{v_2} \ge \rho(Q,j) > 64$ forces
$v_2 \ge 7$; likewise at $Q = 2$ ($2^3 = 8 < \rho$) and $Q = 8, 16$.
(Script §C2 computes $v_{\min}$ by exact integer comparison
$2^v > Q^3$ and checks $\rho(Q, 10^6) < 2^{v_{\min}(Q)}$.) $\square$

*Stratification table* (density $=$ density of
$\{n : v_2(C(n,3)) \ge v_{\min}(Q)\}$ from Claim J2.3; a counterexample
in row $Q$ has its $n$ confined to those classes, and, $n$ being even,
to the four even classes among them):

| $Q$ | $Q^3$ | $v_{\min}(Q)$ | density |
|---|---|---|---|
| 2 | 8 | 4 | $5/32 \approx 0.1563$ |
| 3 | 27 | 5 | $5/64 \approx 0.0781$ |
| 4 | 64 | 7 | $5/256 \approx 0.0195$ |
| 5 | 125 | 7 | $5/256$ |
| 6 | 216 | 8 | $5/512 \approx 0.0098$ |
| 7 | 343 | 9 | $5/1024 \approx 0.0049$ |
| 8 | 512 | 10 | $5/2048 \approx 0.0024$ |
| 9 | 729 | 10 | $5/2048$ |
| 10 | 1000 | 10 | $5/2048$ |
| 11 | 1331 | 11 | $5/4096$ |
| 12 | 1728 | 11 | $5/4096$ |
| 13 | 2197 | 12 | $5/8192$ |
| 14 | 2744 | 12 | $5/8192$ |
| 15 | 3375 | 12 | $5/8192$ |
| 16 | 4096 | 13 | $5/16384 \approx 0.0003$ |

*Remark (the $j$-dependent form).* For fixed $j$ the same argument gives
$v_2 \ge \lceil \log_2 \rho(Q, j) \rceil$, which is stronger for small
$j$ (e.g. $\rho(2, 6) = 11$, $\rho(4, 6) = 506/5$) but tends to the
uniform $v_{\min}(Q)$ as $j$ grows; at the residual scale $j \ge 5001$,
$\rho(Q, j)$ is within $0.1\%$ of $Q^3$ for $Q \le 10$ (script §C2), so
no improvement over $v_{\min}(Q)$ is available there from this lever.

## 3. J.3: Intersection with the residual class

**Claim J2.6 (PROVED — congruence translations in the small rows).**
In the residual class $n$ is even, so by Claim J2.2 the condition
$v_2(C(n,3)) \ge v_{\min}(Q)$ is exactly
$2^{v_{\min}(Q)} \mid n$ or $2^{v_{\min}(Q)} \mid (n-2)$. With
$n = Qj + R$:
- **$Q = 2$** ($v_{\min} = 4$; $n$ even forces $R$ even):
  $16 \mid 2j + R$ or $16 \mid 2j + R - 2$, equivalently
  $$j \equiv -R/2 \ \text{or}\ 1 - R/2 \pmod 8.$$
  E.g. $R = 4$: $j \equiv 6, 7 \pmod 8$; $R = 6$: $j \equiv 5, 6$;
  $R = 8$: $j \equiv 4, 5$; $R = 16$: $j \equiv 0, 1 \pmod 8$.
  So for each fixed $R \bmod 16$, exactly $2$ of the $8$ residue classes
  of $j \bmod 8$ survive.
- **$Q = 3$** ($v_{\min} = 5$): $32 \mid 3j + R$ or $32 \mid 3j + R - 2$,
  equivalently (using $3^{-1} \equiv 11 \pmod{32}$)
  $$j \equiv -11R \ \text{or}\ 11(2 - R) \pmod{32},$$
  exactly $2$ classes of $j \bmod 32$ for each $R$.
- **$Q = 4$** ($v_{\min} = 7$): $128 \mid 4j + R$ or $128 \mid 4j + R - 2$.
  The first alternative requires $4 \mid R$ and $j \equiv -R/4 \pmod{32}$;
  the second requires $R \equiv 2 \pmod 4$ and $j \equiv (2-R)/4
  \pmod{32}$. (For $R$ odd the row has $n$ odd and is already closed by
  SPLIT-odd; for $R \equiv 0, 2 \pmod 4$ exactly one of the two
  alternatives is available, giving one class of $j \bmod 32$.)

*Proof.* Claim J2.2 (even case) with $v = v_{\min}(Q)$, then elementary
modular solving: for $Q=2$ divide by $2$; for $Q=3$ multiply by
$3^{-1} \bmod 32$; for $Q=4$ divide by $4$ after the necessary
congruence on $R$. (Script §G1 verifies all three translations
exhaustively over the stated ranges.) $\square$

**Claim J2.7 (PROVED observation — $v_2$ plus label bounds alone never
contradict; and a computation).** The $v_2$ conditions of §1–§2 constrain
only the $2$-adic valuations of $n$ and $n-2$ — i.e. the part of
$C(n,3)$ that $V_3(n)$ discards. The label bounds of Claim F1.9 /
Corollary F2.4 constrain only prime powers at primes $\ge 3$ (the
$\ge 5$ prime powers of the tops, the genuine split parts, and in $h=0$
rows the $3$-part of $V_3(n)$). The two families of conditions act on
disjoint sets of prime valuations, so **no $(Q,R)$ row is contradictory
from $v_2$ + labels alone**; every closure in this section uses, in
addition, a size input ((N2), the squared half, or (LD3)). That the $v_2$
condition nevertheless has independent bite is shown by F1.11's $(4,2)$
illustration (COMPUTATION, script §G2): the three formal candidates
$(n, j) = (22, 5), (46, 11), (106, 26)$ left open by the Proposition 4.1
+ $(n-1)$ argument have $v_2(C(n,3)) = 2, 2, 3$ respectively — all
$< 4 \le v_{\min}(4)$ — so the $v_2$ condition kills all three
independently of the (LD3) disposal recorded in F1.11/V-F.

**Claim J2.8 (COMPUTATION, with rigorous caps — per-row finiteness from
the squared half).** For a **fixed** row $(Q, R)$, Proposition 4.1's
squared half $C(Qj + R, 3) < (\Lambda_3(T) \binom{j}{h})^2$ bounds $j$:
define $j_{\mathrm{sq}}(Q, R)$ as the largest $j \ge 5$ satisfying it
($\bot$ if no $j \ge 5$ does). A counterexample in the row has
$j \le j_{\mathrm{sq}}(Q, R)$. The values below are exact: for $h = 0$
the inequality is $C(n, 3) < \Lambda_3(T)^2$ with $n = Qj + R$, monotone
in $n$, evaluated by binary search; for $h = 1$ by exact scan up to the
rigorous cap $j < 48\,\Lambda_3(T)^2/Q^3$ (from
$C(Qj+R, 3) \ge (Qj-2)^3/6 \ge (Qj/2)^3/6$). $\Lambda_3$ values used:
$\Lambda_3(6) = 15$, $\Lambda_3(8) = 105$, $\Lambda_3(10) = 315$,
$\Lambda_3(12) = 3465$, $\Lambda_3(16) = 45045$,
$\Lambda_3(18) = 765765$, $\Lambda_3(22) = 14549535$,
$\Lambda_3(24) = 334639305$ (script §D0, §D).

Selected values (full table for $0 \le R \le 24$ in script §D):

| row | $j_{\mathrm{sq}}$ | row | $j_{\mathrm{sq}}$ | row | $j_{\mathrm{sq}}$ |
|---|---|---|---|---|---|
| (2,4) | $\bot$ | (3,1) | 50 | (4,2) | 1032 |
| (2,6) | 17 | (3,3) | 12 | (4,4) | 20 |
| (2,8) | 38 | (3,5) | 26 | (4,6) | 102 |
| (2,10) | 203 | (3,7) | 136 | (4,8) | 573 |
| (2,12) | 1144 | (3,9) | 764 | (4,10) | 572 |
| (2,14) | 1143 | (3,11) | 763 | (4,12) | 3799 |
| (2,16) | 7597 | (3,13) | 5065 | (4,14) | 27071 |
| (2,18) | 54140 | (3,15) | 36094 | (4,16) | 27070 |
| (2,20) | 54139 | (3,17) | 36093 | (4,18) | 218960 |
| (2,22) | 437919 | (3,19) | 291947 | (4,20) | 640253 |

(Row $(2,0)$ is omitted: $h=2$ there and the row is closed separately.
Rows $(3,0)$, $(2,3)$, $(2,4)$ have $j_{\mathrm{sq}} = \bot$: the squared
inequality already fails at $j=5$, so the squared half alone excludes
every $j \ge 5$ in them — consistent with, but weaker than, their
certified closures.)

**Combined picture per row (squared half + residual conditions).**
Intersecting with $j \ge 5001$ (certified residual): the squared half
alone eliminates the residual part of rows $(2, R)$ for even
$R \le 14$; $(3, R)$ for $R \le 12$ and for $R = 1$; $(4, R)$ for even
$R \le 12$ and $R = 2$. It leaves three narrow **windows**:
$(3, 13)$ and $(3, 14)$ with $5001 \le j \le 5065$, and $(2, 16)$ with
$5001 \le j \le 7597$. Those windows are closed by direct computation
(COMPUTATION, script §F3): in a fixed row $n$ is determined by $j$, and
(LD3) — a certified necessary condition — was tested on every triple in
each window with $n$ even: $33$ triples in $(3,13)$, $32$ in $(3,14)$,
$2597$ in $(2,16)$; **zero (LD3) survivors** in each. (The (LD3) test was
validated in the same script: the $\ge 5$-only system at $n \le 2000$
returns exactly the six known pairs of P-A1, and the full system returns
zero survivors at $n \le 2000$, script §F1–F2.) Rows with
$j_{\mathrm{sq}} \ge 54139$ — $(2, R)$, $R \ge 18$; $(3, R)$, $R \ge 15$;
$(4, R)$, $R \ge 14$ — are **not** eliminated by the squared half at the
residual scale; §4's hybrid comparison (Claim J2.12) shrinks this list
further, and the final combined list is in §5.

## 4. J.4: Del Pin-spirit comparisons

**Claim J2.9 (PROVED — the maximal-valuation bound).**
$2^{v_2(C(n,3))} \le n$ for all $n \ge 3$, with equality iff $n$ is a
power of $2$. Consequently
$$V_3(n) \;\ge\; \frac{C(n,3)}{n} \;=\; \frac{(n-1)(n-2)}{6}
\qquad\text{for all } n.$$

*Proof.* By Claim J2.2's proof: if $n$ is odd,
$v_2(C(n,3)) = v_2(n-1) - 1 \le \log_2(n-1) - 1 < \log_2 n$. If $n$ is
even, $v_2(C(n,3)) = \max(v_2(n), v_2(n-2))$ (the other of the two
valuations being $1$, by the $\min = 1$ observation), and
$\max(v_2(n), v_2(n-2)) \le \log_2 n$ with equality iff $n$ itself is a
power of $2$ (the alternative $n - 2 = 2^{v}$ with $2^v \le n - 2 < n$
gives strict inequality $2^{v_2} = n - 2 < n$). (Script §B verifies the
bound and the $V_3$ consequence for $n \le 200{,}000$.) $\square$

**Claim J2.10 (PROVED — the comparison's failure window is
$[2j, M(j)]$).** Define
$M(j) := \max\{n : (n-1)(n-2) \le j(j-1)(j-2)\}$ (so
$M(j) \sim j^{3/2}$). If $n > M(j)$ then $V_3(n) > C(j,3)$: the
$V_3$-refined comparison closes the triple $(n, 3, j)$ using the
**specific** $v_2$ of $n$ (through Claim J2.9), not a uniform bound.
Hence the refined comparison can fail at $(3, j)$ only for
$2j \le n \le \min(N(3,j), M(j))$; in the computed range $j \le 60$,
$M(j) < N(3,j)$ throughout (script §E0), so the window genuinely shrinks
from $\sim 0.81\,j^2$ to $\sim j^{3/2}$.

*Proof.* $n > M(j)$ gives $(n-1)(n-2) > j(j-1)(j-2)$, i.e.
$(n-1)(n-2)/6 > C(j,3)$, and Claim J2.9 gives $V_3(n) \ge
(n-1)(n-2)/6$. $\square$

**Claim J2.11 (PROVED + COMPUTATION — F1.14's GAP sentence is FALSE;
the exact reach of the refined comparison).** The final sentence of
Claim F1.14 asserts that the $V_3$-refined comparison "does not by
itself close any full pair $(3, j)$ with $j > 5$ for all $n$". This is
**FALSE**. The exact truth is:

> Among $j > 5$, the refined comparison closes the pair $(3, j)$ for
> all $n \ge 2j$ **iff $j \in \{6, 10\}$**. For every other $j > 5$
> there exists $n \in [2j, N(3,j)]$ with $V_3(n) \le C(j, 3)$, so the
> comparison does not close that pair.

*Proof.* By Claim J2.10 it suffices to examine $n \in [2j, M(j)]$
(failure outside is impossible; and any witness $n \le M(j)$ with
$n \le N(3,j)$ shows non-closure in the sense of the brief's interval
criterion).

*The two closed pairs.* $j = 6$: $M(6) = 12$, and the only candidate is
$n = 12$ with $V_3(12) = 55 > 20 = C(6,3)$. $j = 10$: $M(10) = 28$, and
$(n, V_3(n))$ for $n = 20, \dots, 28$ is
$(285, 665, 385, 1771, 253, 575, 325, 2925, 819)$ — all
$> 120 = C(10,3)$ (script §E3). Hence for $j \in \{6, 10\}$ **every**
$n \ge 2j$ has $V_3(n) > C(j,3)$: the comparison closes these pairs for
all $n$ outright (a stronger statement than the interval criterion).
Both pairs were already closed by other means (Claim F1.16 /
Computation F2.18); the new content is that this comparison alone
suffices, refuting F1.14's sentence. (V-F had flagged the sentence as a
GAP and recorded that a search found no $n \le 200{,}000$ with
$V_3(n) \le C(j,3)$ for $j = 6$ or $j = 10$; the present claim explains
that observation: there is no such $n$ at all.)

*All other $j > 5$ have witnesses.* For $7 \le j \le 18$, $j \ne 10$,
explicit first witnesses (script §E2; each satisfies $n \le N(3,j)$,
verified there): $j = 7$: $(16, 35)$ with $V_3 = 35 = C(7,3)$ (equality —
the comparison needs strict $>$, so this is F1.14's sharpness example);
$j = 8$: $(16, 35) \le 56$; $j = 9$: $(18, 51) \le 84$;
$j = 11, \dots, 16$: $(32, 155)$ against $C(j,3) = 165, 220, 286, 364,
455, 560$; $j = 17$: $(34, 187) \le 680$; $j = 18$: $(64, 651) \le 816$.

For $j \ge 19$, let $n_0$ be the least power of $2$ with $n_0 \ge 2j$;
then $n_0 < 4j$. By Claim J2.9's equality case,
$V_3(n_0) = (n_0 - 1)(n_0 - 2)/6$, and
$(n_0-1)(n_0-2) < n_0^2 < 16j^2 \le j(j-1)(j-2)$, the last inequality
being $(j-1)(j-2) \ge 16j \iff j^2 - 19j + 2 \ge 0$, true for $j \ge 19$
(value $2$ at $j = 19$, increasing thereafter). Hence
$V_3(n_0) \le C(j, 3)$. It remains that $n_0 \le N(3, j)$: since
$n_0 < 4j$ it suffices that $C(4j, 3) < C(2j, 6)$ for $j \ge 19$, which
follows from $C(2j, 6) \ge (2j-5)^6/720$ and $C(4j, 3) \le (4j)^3/6$:
the required inequality $(2j-5)^6 > 7680\,j^3$ expands to
$64j^6 - 960j^5 + 6000j^4 - 27680j^3 + 37500j^2 - 37500j + 15625 > 0$,
whose terms group as $64j^5(j - 15) + j^3(6000j - 27680) +
37500j(j-1) + 15625$, each strictly positive for $j \ge 19$. Hence
$N(3, j) \ge 4j > n_0$.

*Corroboration (COMPUTATION, script §E1):* for every $6 \le j \le 2000$,
a witness $n \in [2j, M(j)]$ was found except at $j = 6$ and $j = 10$
exactly. $\square$

**Claim J2.12 (PROVED + COMPUTATION — the hybrid comparison, J.4(b)).**
Let $(n, 3, j)$ be a counterexample in row $(Q, R)$, with $T, h$ as in
Proposition 4.1. Then
$$\frac{(n-1)(n-2)}{6} \;\le\; V_3(n) \;\le\; \Lambda_3(T)\binom{j}{h},$$
the left inequality by Claim J2.9, the right by Proposition 4.1's
divisibility. Hence the triple is closed whenever
$(n-1)(n-2) > 6\,\Lambda_3(T)\binom{j}{h}$. Define
$j_{\mathrm{hyb}}(Q, R)$ as the largest $j \ge 5$ **not** closed by this
test ($\bot$ if none). Exact values (script §D; $h=0$ rows scanned to
the cap from $(Qj + R - 2)^2 \le 6\Lambda_3(T)$, $h=1$ rows to the cap
$j \le 24\,\Lambda_3(T)/Q^2$ from $(Qj-2)^2 \le 6\Lambda_3(T) j$):

| row | $j_{\mathrm{hyb}}$ | row | $j_{\mathrm{hyb}}$ | row | $j_{\mathrm{hyb}}$ |
|---|---|---|---|---|---|
| (2,4) | $\bot$ | (3,1) | 10 | (4,2) | 39 |
| (2,6) | 10 | (3,3) | 7 | (4,4) | 10 |
| (2,8) | 18 | (3,5) | 13 | (4,6) | 34 |
| (2,10) | 67 | (3,7) | 46 | (4,8) | 128 |
| (2,12) | 254 | (3,9) | 170 | (4,10) | 127 |
| (2,14) | 253 | (3,11) | 170 | (4,12) | 533 |
| (2,16) | 1064 | (3,13) | 710 | (4,14) | 2332 |
| (2,18) | 4663 | (3,15) | 3109 | (4,16) | 2332 |
| (2,20) | 4662 | (3,17) | 3109 | (4,18) | 11198 |
| (2,22) | 22394 | (3,19) | 14930 | (4,20) | 25044 |

In **every** row computed ($Q \in \{2,3,4\}$, $0 \le R \le 24$,
$(Q, R) \ne (2, 0)$ — the $h=2$ row, closed separately),
$j_{\mathrm{hyb}}(Q, R) \le j_{\mathrm{sq}}(Q, R)$: the hybrid is
uniformly sharper than Proposition 4.1's own squared half. The reason is
visible in the crude caps: for $h = 0$ the hybrid bounds
$n \lesssim \sqrt{6\Lambda_3(T)}$ against the squared half's
$n \lesssim (6\Lambda_3(T)^2)^{1/3}$, and $\sqrt{6\Lambda} <
(6\Lambda^2)^{1/3}$ iff $\Lambda > 6$. Intersecting with the residual
condition $j \ge 5001$: the hybrid eliminates the residual part of rows
$(2, R)$ for even $R \le 20$ (squared: $R \le 14$, plus the §3 windows);
$(3, R)$ for $R \le 18$ (squared: $R \le 12$, plus windows); $(4, R)$ for
even $R \le 16$ (squared: even $R \le 12$). It does not eliminate
$(2, 22)$ ($j_{\mathrm{hyb}} = 22394$), $(3, 19)$ ($14930$),
$(4, 18)$ ($11198$), or any row beyond those.

**Claim J2.13 (COMPUTATION — a second test comparison, honestly
negative).** The single-top bound suggested in the brief,
$V_3(n) \ge R(n-1)/3$ pushed through (N2), was tested: since the
$n-1$ contribution to $V_3(n)$ is $R(n-1)$ or $R(n-1)/3$ and
$R(n-1) \ge (n-1)/3$ in the even case, it gives $V_3(n) \ge (n-1)/9$,
which through (N2) yields only $n < \tfrac32 j^3 + 1$ — strictly weaker
than Claim F1.8's $n \le 3j(j-1) + 1$ and far weaker than Claim J2.9's
quadratic lower bound $(n-1)(n-2)/6$, which dominates it for all
$n \ge 4$. **It closes nothing** beyond what was already certified, and
is recorded here as a tested, dominated comparison rather than used.

## 5. Closing statement for Cluster J

**Claim J2.14 (summary — PROVED / reduced / OPEN, stated exactly).**

*Proved in this file, beyond the certified Cycle 2 record:*
1. The complete $v_2$ theory at $i=3$ (Claims J2.1–J2.3): borrow/carry
   and digit-sum forms; the parity characterisations for all $v$ (the
   brief's $v=4$ forms verified); $\{v_2(C(n,3)) \ge v\}$ has exactly
   $5$ classes mod $2^{v+1}$ for $v \ge 2$ ($3$ for $v=1$), density
   $5/2^{v+1}$, with explicit lists at $v = 4, 5, 6$.
2. The $Q$-stratification (Claims J2.4–J2.5):
   $v_2(C(n,3)) \ge v_{\min}(Q) = \lfloor 3\log_2 Q\rfloor + 1$ in row
   $Q$, via the strictly decreasing $\rho(Q, \cdot) \downarrow Q^3$;
   $v_{\min}(2) = 4$, $v_{\min}(3) = 5$, $v_{\min}(4) = 7$ as
   hypothesised; the strictness at $Q \in \{2, 4, 8, 16\}$ (where
   $Q^3$ is a power of $2$) is exactly what the hypothesis needed.
3. Congruence translations of the $v_{\min}$ condition in rows
   $Q = 2, 3, 4$ (Claim J2.6), and the disjointness observation that
   $v_2$ + label bounds alone close no row (Claim J2.7), with the
   $(4,2)$ candidates shown to fail $v_2$ independently.
4. **F1.14's GAP sentence is settled and is FALSE** (Claim J2.11): the
   $V_3$-refined comparison closes a pair $(3, j)$, $j > 5$, for all
   $n$ iff $j \in \{6, 10\}$; every other $j > 5$ has a witness
   $n \in [2j, N(3,j)]$ with $V_3(n) \le C(j,3)$ (power-of-two witnesses
   for $j \ge 19$; exact computation corroborates to $j \le 2000$).
   The maximal-valuation bound $2^{v_2} \le n$ and the resulting
   failure window $[2j, M(j)]$, $M(j) \sim j^{3/2}$ (Claims J2.9–J2.10).
5. The hybrid comparison (Claim J2.12), sharper than the squared half
   in every row computed, which — combined with the certified closure
   of all pairs $j \le 5000$ — **closes for all $j$** the rows
   $(2, R)$ for even $4 \le R \le 20$, $(3, R)$ for $1 \le R \le 18$
   (with $R \in \{0, 2\}$ previously closed), and $(4, R)$ for even
   $2 \le R \le 16$ (with $R = 0$ previously closed). The three
   squared-bound windows $(3,13)$, $(3,14)$, $(2,16)$ are independently
   closed by an (LD3) computation (Claim J2.8).

*Reduced:* the $i=3$ residual class is now stratified by row: in row
$Q$ a counterexample needs $v_2(C(n,3)) \ge v_{\min}(Q)$ (density
$5/2^{v_{\min}(Q)+1}$, four even classes), the congruences of
Claim J2.6, and $j > j_{\mathrm{hyb}}(Q, R)$ in its $(Q, R)$ row.

*Still OPEN, explicitly:* the residual class itself. Rows not closed by
anything in this file or the certified record include $(2, R)$ for even
$R \ge 22$, $(3, R)$ for $R \ge 19$, $(4, R)$ for even $R \ge 18$, and
all rows with $Q \ge 5$ beyond the $v_{\min}$ stratification (per-fixed-
$(Q,R)$ finiteness from the squared half and the hybrid holds for every
$Q$, but the maxima grow with $\Lambda_3(T)$ and no uniform-in-$R$
closure is proved or claimed). (H3) remains open; **$i = 3$ is not
closed, and Erdős #699 is not claimed solved.** No comparison in this
file closes any subclass larger than what is stated row by row above.

## 6. Verification log

All numbers above are outputs of `proofs/P-J2_checks.py` (Python stdlib
only, exact arithmetic; all assertions pass; runtime under 10 s):
- §A1: digit-sum, carry-count, and borrow-count forms of $v_2(C(n,3))$
  agree for $3 \le n \le 20{,}000$ (0 mismatches).
- §A2: periodicity mod $2^{v+1}$ and the class lists for
  $0 \le v \le 8$: counts $2, 3, 5, 5, 5, 5, 5, 5, 5$, lists matching
  $\{0, 1, 2, 2^v, 2^v+2\}$ for $v \ge 2$.
- §A3: the parity characterisations, including the general-$v$ forms,
  for $n \le 100{,}000$ (0 mismatches).
- §B: $2^{v_2(C(n,3))} \le n$ and $V_3(n) \ge (n-1)(n-2)/6$ for
  $n \le 200{,}000$ (0 mismatches).
- §C1: $\rho(Q, j)$ strictly decreasing and $> Q^3$ in exact `Fraction`s
  ($2 \le Q \le 10$, $4 \le j \le 500$). §C2: $v_{\min}(Q)$ table for
  $2 \le Q \le 16$ by exact integer comparison $2^v > Q^3$, with
  $\rho(Q, 10^6) < 2^{v_{\min}(Q)}$.
- §D0: $\Lambda_3(T)$ for $T \le 24$. §D: $j_{\mathrm{sq}}$ and
  $j_{\mathrm{hyb}}$ for $Q \in \{2, 3, 4\}$, $0 \le R \le 24$ (row
  $(2,0)$ skipped: $h=2$, closed separately), by the exact methods of
  Claims J2.8/J2.12.
- §E0: $M(j)$ and $N(3, j)$ for $4 \le j \le 60$ ($M(j) < N(3,j)$
  throughout). §E1: witness search on $[2j, M(j)]$ for
  $6 \le j \le 2000$: no-witness set exactly $\{6, 10\}$. §E2: the
  table witnesses for $7 \le j \le 18$, each checked $\le N(3, j)$.
  §E3: the full $(n, V_3(n))$ lists on $[2j, M(j)]$ for $j = 6, 10$.
- §F1–F2: (LD3) implementation validation ($\ge 5$-only system: exactly
  the six P-A1 pairs at $n \le 2000$; full system: zero survivors).
  §F3: the window checks for $(3,13)$ ($33$ triples), $(3,14)$ ($32$),
  $(2,16)$ ($2597$): zero (LD3) survivors.
- §G1: the congruence translations of Claim J2.6 (0 mismatches).
  §G2: $v_2(C(n,3)) = 2, 2, 3$ at the $(4,2)$ candidates
  $(22,5), (46,11), (106,26)$.
