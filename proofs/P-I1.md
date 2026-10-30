# Prover I1 (independent): the even residual class at $i=3$, row by row — Cycle 3, Cluster I

Prover: I1, working independently in Cycle 3. The second prover on this
cluster (I2) was **not** consulted and `proofs/P-I2.md` was **not** read;
independence is methodologically essential and was preserved. Sources read:
`CYCLE2.md` §2 and §§8–9; `proofs/P-F1.md` in full; `proofs/P-F2.md`
§§1–3 and §7; `verification/V-F.md`; `proofs/P-A1.md` (Lemma A1.15,
Proposition A1.16, Statement (H3), Theorem A1.17); `strategies/S8.md` §3;
`EXTERNAL_CLAIMS_2026-10-29.md` (the Van Doorn–Rocca diagnosis: a completion
at $i=3$ must retain the labels recording which of $n, n-1, n-2$ supplies
each prime power — the row analysis of §3 below is exactly a label-retaining
argument, with the row $(Q,R)$ as the label). Every computation is in
`proofs/P-I1_checks.py` (Python standard library only, exact arithmetic;
total runtime under 1 second). Every numbered claim is labelled PROVED /
GAP / FALSE / OPEN / COMPUTATION.

**Headline.** $i=3$ is **not** closed and (H3) is **not** proved. What is
new here: (§1) F1.11 and F2.14 are reconciled into one residual statement
(RES-3), with nine discrepancies/sharpenings itemised (D1–D9); (§2) the
per-row finiteness statement suggested by the squared half of Proposition
4.1 is **proved for $h \in \{0,1\}$ and refuted at the single row
$(Q,R)=(2,0)$** (where $h=2$), with explicit bounds $B(Q,R)$ computed
exactly for all 64 rows with $T \le 16$: 54 of the 63 rows with $h \le 1$
have $B(Q,R) \le 5001$ and are therefore already entirely closed by the
certified per-pair frontier $j \le 5000$; (§3) the $(4,2)$ analysis of
F1.11 is reproduced **exactly** (validation: precisely the candidates
$(22,5), (46,11), (106,26)$, gcds $77, 69, 371$), and the odd-top method
behind it is generalised into a lemma that disposes — as CLOSED rows or
explicit FINITE LISTs — every row the brief named and, beyond them, every
non-vacuous row with $T \le 16$ that §2 could not close. **Net effect
(§4): a counterexample at $i=3$ must now satisfy $T = R + 2(Q-1) \ge 17$,
on top of all of (RES-3).** The residual class with $T \ge 17$ remains
OPEN.

**Corrections to the brief (flagged per standing campaign practice).**
Two $T$-values in the assignment's candidate list are arithmetically
wrong against the certified formula $T = R + 2(Q-1)$: (i) $(3,4)$ is
listed with $T=7$; in fact $T = 4 + 2\cdot2 = 8$. The slip is immaterial
to that row ($\Lambda_3(7) = \Lambda_3(8) = 105$ and the finite set
$M(7) = M(8)$ of §3 coincide), but the record here uses $T=8$. (ii)
$(5,2)$ is listed with $T=8$; in fact $T = 2 + 2\cdot4 = 10$. This one
*is* material to the form set ($M(10)$ admits the factor $3^3$ where
$M(8)$ does not); the row's conclusion (no candidates at all) survives
the correction and is proved at the correct $T=10$ in Claim I3.12.

## 0. Standing inputs and notation

As in the brief and the Cycle 2 record (all verifier-certified there):
a counterexample is $(n,3,j)$, $3 < j \le n/2$, with
$\gcd(V_3(n), C(n,j)) = 1$, where $V_3(n)$ is the part of $C(n,3)$ on
primes $\ge 3$. Write $n = Qj + R$ ($Q = \lfloor n/j \rfloor \ge 2$,
$0 \le R < j$), $T = R + 2(Q-1)$,
$h = \max(0, \lceil (3-R)/Q \rceil)$, and
$\Lambda_3(T) = \prod_{q \ge 3} q^{\lfloor \log_q T \rfloor}$.
Proposition 4.1 at $i=3$ (F1.1/F1.2, F2.3) gives, for a counterexample,
$V_3(n) \mid \Lambda_3(T)\binom{j}{h}$ (divisibility half; no EEES78) and
$C(n,3) < (\Lambda_3(T)\binom{j}{h})^2$ (squared half; EEES78). The
per-part dichotomy (F2.4, in the at-least-one form V-F certified): every
full prime-power part $p^a$ of $V_3(n)$ satisfies $p^a \le T$ or
$p^a \mid j - r$ for some $0 \le r < h$; for $p \ge 5$ the part $p^a$ is
the exact prime power $p^a \Vert (n - r_0)$ of the unique top number it
divides. Relevant prime powers, $R(m)$, (LD3) in splitting form, (N1),
(N2) are as in A1.15/A1.16 and the brief. Certified necessary conditions
used throughout: $n$ even (F1.5/F2.7: SPLIT-odd closed); $j \ge 5001$
(F2.18/F2.19: (LD3) has no solution with $2j \le n \le N(3,j)$ for any
$5 \le j \le 5000$, so every pair $(3,j)$, $j \le 5000$, is closed for
all $n$); $n > 10^6$ (F1.17/F2.21: no (LD3) solution with $n \le 10^6$);
$v_2(C(n,3)) \ge 4$ (F1.13/F2.15); rows
$(Q,R) \in \{(2,0), (2,2), (3,0), (3,2), (4,0)\}$ closed ((2,0) is
Price's central case; the other four are F1.10). In the open range we
take $j \ge 5$ (the pair $j = 4$ lies in the closed region
$j \le 3i/2$). The three top numbers are $n - r_0$, $r_0 \in \{0,1,2\}$;
following F1.9/F2.9, in an $h = 1$ row the top $n - R$ is called
**special** and the other two tops **non-special**.

## 1. Task I.1 — (RES-3): F1.11 and F2.14 reconciled

**Claim I1.1 (RES-3 — the reconciled residual class; assembly of
certified inputs, PROVED as a necessary-condition statement).**
If $(n,3,j)$ is a counterexample, then, with $(Q,R,T,h)$ as above, ALL
of the following hold simultaneously:

1. $n$ is even, $j \ge 5001$, $n > 10^6$, $v_2(C(n,3)) \ge 4$.
2. $(Q,R) \notin \{(2,0), (2,2), (3,0), (3,2), (4,0), (4,2)\}$, and the
   row is parity-feasible for even $n$: if $Q$ is even then $R$ is
   even; if $Q$ is odd then $j \equiv R \pmod 2$.
3. (LD3) in full splitting form: $R(n) \mid j$;
   $R(n-1) = X_0X_1$, $X_0 \mid j$, $X_1 \mid j-1$;
   $R(n-2) = Y_0Y_1Y_2$, $Y_s \mid j-s$; and no relevant prime power
   $q \Vert (n-1)$ exceeds $(n-1)/3$ (F1.7).
4. $n \le 3j(j-1) + 1$ (F1.8).
5. (N1) $\gcd(C(n,2), C(n,j)) = 2^a3^b$; (N2) $V_3(n) \mid C(j,3)$.
6. $V_3(n) \mid \Lambda_3(T)\binom{j}{h}$ and
   $C(n,3) < (\Lambda_3(T)\binom{j}{h})^2$ (Proposition 4.1).
7. If $h = 0$ ($R \ge 3$): every prime-power part of $V_3(n)$ is
   $\le T$; every $\ge 5$ prime power of every top number is $\le T$;
   the $3$-part of $V_3(n)$ is $\le T$ (the exact $3$-power of a top
   number may be as large as $3T$); and
   $V_3(n) \mid \gcd(C(j,3), \Lambda_3(T))$ (F1.9(a), F2.13).
8. If $h = 1$ ($R \in \{0,1,2\}$, $(Q,R) \ne (2,0)$): every top
   $n - r_0$ with $r_0 \ne R$ has no prime factor $> T$ in its $\ge 5$
   part; any prime power $P = p^a \Vert (n-R)$ ($p \ge 5$) with
   $p > T$ satisfies $P \mid j$ (F1.9(b)); and any prime power at
   $p \ge 5$ that (LD3) assigns to $j-1$ or $j-2$ but not to $j$ (a
   genuine split part) is $\le T$ (F2.9). The $3$-part $3^{e-1}$ of
   $V_3(n)$ satisfies the dichotomy of F2.4: it is $\le T$ in the
   $\Lambda_3$ sense or divides some $j - r$, $r < h$.

No argument in the Cycle 2 files, and none in §§2–3 below for rows with
$T \ge 17$, excludes this class in general; as a class for
counterexamples it is **OPEN** (its shrinkage in this cycle is §4).

**Discrepancies between F1.11 and F2.14, and how (RES-3) resolves
them.**
- **D1 (frontier).** F2.14 states $j \ge 159$; that figure is
  superseded *inside the same file* by F2.19 ($j \ge 5001$). F1.11
  states no $j$-bound (F1.16 gives $j > 2000$ in F1's summary).
  (RES-3) uses the sharpest certified value, $j \ge 5001$.
- **D2 (closed rows).** F1.11 excludes the four F1.10 rows; F2.14 does
  not exclude $(2,2)$ and $(3,0)$ — it only records F2.12's condition
  $U_0U_1U_2 \mid j$ there (F2 alone does not close those rows).
  (RES-3) takes the intersection: the rows are out (via certified
  F1.10).
- **D3 (the $(4,2)$ row).** F1.11 lists $(4,2)$ as *inside* the
  residual class, yet its own embedded computation — recomputed from
  scratch by V-F (§5 of V-F) — shows that the Proposition 4.1 +
  $(n-1)$ argument leaves exactly three candidates
  $(22,5), (46,11), (106,26)$ for that row, each failing (LD3). A row
  whose complete candidate set is disposed is not residual in any
  operative sense; F1.11's accounting is conservative because the
  disposal is per-instance computation rather than a general argument.
  (RES-3) removes $(4,2)$, on the strength of that certified embedded
  computation, independently reproduced in this file as the mandatory
  validation step (Claim I3.5).
- **D4 (strength of the $h=1$ bound).** F1.11(iv) bounds prime
  *factors* ($> T$) of non-special tops and treats special-top prime
  powers separately; F2.9 bounds genuine split prime *powers* by $T$.
  These are compatible, not contradictory; (RES-3)(8) keeps both
  forms. §3 (Lemma I3.1) proves the common sharpening — *every*
  $\ge 5$ prime power of a non-special top is $\le T$ — from F2.4 plus
  the difference argument in F1.9(b)'s own proof.
- **D5.** F1.11 includes F1.7 and F1.8; F2.14 omits them (F2.10/F2.11
  are partial analogues in the $Q=2$ / single-prime-power regimes).
  (RES-3) includes them; they are certified necessary conditions.
- **D6.** F2.14 makes $V_3(n) \mid \Lambda_3(T)\binom{j}{h}$ and (in
  $h=0$ rows) the gcd form $V_3(n) \mid \gcd(C(j,3), \Lambda_3(T))$
  explicit; F1.11 records only their consequences (iii)–(iv).
  (RES-3) includes both (items 6–7).
- **D7 (parity).** Neither residual statement mentions parity
  feasibility, although $n$ even forces it immediately from
  $n = Qj + R$. (RES-3)(2) makes it explicit: 16 of the 64 rows with
  $T \le 16$ ($Q$ even, $R$ odd) can never carry an even $n$ at all.
  This is an addition of an immediate consequence, not a correction.
- **D8 ($v_2$).** The necessary condition $v_2(C(n,3)) \ge 4$
  (F1.13/F2.15) appears in neither residual statement, only in the
  provers' summaries and CYCLE2 §2. (RES-3)(1) includes it.
- **D9 ($n > 10^6$).** F1.11 as stated does not intersect the
  $n \le 10^6$ computation (V-F notes this explicitly); F2.14 mentions
  it only as a searched-range remark. (RES-3)(1) includes it, from
  certified F1.17/F2.21.

## 2. Task I.2 — per-row finiteness from the squared half: proved for $h \le 1$, refuted at $(2,0)$

The squared half of Proposition 4.1 says
$C(n,3) < (\Lambda_3(T)\binom{j}{h})^2$ with $n = Qj + R$. Since
$n \ge Qj$ and $\binom{\cdot}{3}$ is increasing,
$C(Qj,3) \le C(n,3)$. The left side has degree $3$ in $j$; the right
side has degree $2h$. So a bound on $j$ can be extracted **iff
$h \le 1$** — and $h = 2$ occurs for exactly one row.

**Claim I2.1 (PROVED — analytic per-row bounds for $h \le 1$).**
Let $(n,3,j)$ be a counterexample in a row with $h \le 1$,
$\Lambda = \Lambda_3(T)$.
(a) If $h = 0$: $\displaystyle j \;<\; B_0(Q,R) :=
\frac{2 + (6\Lambda^2)^{1/3}}{Q}$.
(b) If $h = 1$: $\displaystyle j \;<\; B_1(Q,R) :=
\frac{25}{3}\cdot\frac{\Lambda^2}{Q^3}$.

*Proof.* (a) $C(n,3) = n(n-1)(n-2)/6 > (n-2)^3/6 \ge (Qj-2)^3/6$
($n \ge Qj \ge 10$). A counterexample satisfies $C(n,3) < \Lambda^2$,
so $(Qj-2)^3 < 6\Lambda^2$ and $Qj - 2 < (6\Lambda^2)^{1/3}$.
(b) $C(n,3) \ge C(Qj,3) = (Qj)(Qj-1)(Qj-2)/6$. For $x = Qj \ge 10$,
$(1 - 1/x)(1 - 2/x) \ge (0.9)(0.8) = 0.72$ (each factor increases in
$x$), so $C(Qj,3) \ge 0.72\,(Qj)^3/6 = 0.12\,Q^3j^3$. A counterexample
satisfies $C(n,3) < \Lambda^2 j^2$, hence
$0.12\,Q^3j^3 < \Lambda^2j^2$ and $j < \Lambda^2/(0.12\,Q^3)
= \frac{25}{3}\Lambda^2/Q^3$. $\square$

**Claim I2.2 (PROVED — the feasibility predicate is a threshold).**
For fixed $(Q,R)$ define *feasible* $j \ge 5$ by
$C(Qj+R,3) < (\Lambda_3(T)\binom{j}{h})^2$ (the squared inequality with
the exact $n = Qj+R$). (a) If $h = 0$, feasibility in $j$ is an initial
segment $\{5, \dots, J_{\max}\}$ (possibly empty): the left side is
strictly increasing in $j$ and the right side is constant. (b) If
$h = 1$, the same holds: $f(j) := C(Qj+R,3)/j^2$ is strictly
increasing for $j \ge 5$.

*Proof of (b).* With $n = Qj + R$,
$f(j+1)/f(j) = \prod_{k=0}^{2}\frac{n+Q-k}{\,n-k\,}\cdot
\big(\frac{j}{j+1}\big)^2$.
Each factor $\frac{n+Q-k}{n-k} = 1 + \frac{Q}{n-k} \ge 1 + \frac{Q}{n}$,
so the product is $\ge (1 + Q/n)^3$. It suffices that
$3\ln(1 + Q/n) > 2\ln(1 + 1/j)$. Using
$\ln(1+x) > x/(1+x)$ and $\ln(1+y) < y$ ($x, y > 0$), the left side
exceeds $3\cdot\frac{Q/n}{1+Q/n} = \frac{3Q}{n+Q}$ and the right side
is $< 2/j$; and $\frac{3Q}{n+Q} > \frac{2}{j}$ iff
$3Qj > 2n + 2Q = 2Qj + 2R + 2Q$ iff $Q(j-2) > 2R$. In an $h=1$ row
$R \le 2$, and $Q \ge 2$, $j \ge 5$ give $Q(j-2) \ge 6 > 4 \ge 2R$.
$\square$

Consequently $J_{\max}(Q,R) := \max\{j \ge 5 : j \text{ feasible}\}$
(with $J_{\max} = 4$ if no $j \ge 5$ is feasible) is well-defined and
computable by binary search between $5$ and the analytic bound of
Claim I2.1, and **every counterexample in the row satisfies
$j \le J_{\max}(Q,R)$, i.e. $j < B(Q,R) := J_{\max}(Q,R) + 1$.**

**Claim I2.3 (FALSE — the universal per-row finiteness statement, as
a derivation from the squared half).** The statement "for every fixed
$(Q,R)$ the squared half yields a bound $j < B(Q,R)$" is **false** at
the unique row with $h = 2$, namely $(Q,R) = (2,0)$ (indeed
$h = \lceil(3-R)/Q\rceil = 2$ with $R \le 2$ forces $Q < 3 - R \le 3$,
i.e. $(2,0)$). There $\Lambda_3(2) = 1$ and the squared inequality is
$C(2j,3) < \binom{j}{2}^2$, whose ratio is exactly
$$\frac{\binom{j}{2}^2}{C(2j,3)} = \frac{3j(j-1)}{8(2j-1)},$$
which exceeds $1$ iff $3j^2 - 19j + 8 > 0$ — true at $j = 6$
($2 > 0$) and for all larger $j$ (the increments are $6j - 16 > 0$).
So the inequality *holds* for every $j \ge 6$ and entails no bound
whatsoever. (Script §B verifies the ratio identity and the inequality
exactly for $6 \le j < 2000$.) The row $(2,0)$ is of course closed —
by Price's central case, a standing input — but **not** by this
argument. The per-row finiteness statement is therefore: PROVED for
every row except $(2,0)$; the derivation is FALSE at $(2,0)$.

**Claim I2.4 (COMPUTATION — exact thresholds for all rows with
$T \le 16$, and the classification).** $\Lambda_3(T)$ for
$T = 0..16$ is $1,1,1,3,3,15,15,105,105,315,315,3465,3465,45045,
45045,45045,45045$ (script §A). There are exactly $64$ rows with
$T \le 16$ ($Q = 2..9$). For the $63$ rows with $h \le 1$, exact
$J_{\max}$ (binary search per Claim I2.2; endpoint assertions
feasible($J_{\max}$), infeasible($J_{\max}+1$), and
infeasible at the Claim I2.1 analytic cap all asserted in script §C;
monotonicity of $f$ additionally spot-verified exactly for $j = 5..300$
and around $J_{\max}$ in §C3):

| $Q$ | $J_{\max}$ by $R$ |
|---|---|
| 2 | $R{=}1{:}\ 6;\ R{=}2{:}\ 5;\ R{=}3{:}\ 4;\ R{=}4{:}\ 4;\ R{=}5{:}\ 18;\ R{=}6{:}\ 17;\ R{=}7{:}\ 39;\ R{=}8{:}\ 38;\ R{=}9{:}\ 204;\ R{=}10{:}\ 203;\ R{=}11{:}\ 1145;\ R{=}12{:}\ 1144;\ R{=}13{:}\ 1144;\ R{=}14{:}\ 1143$ (and $R{=}0$: $h=2$, Claim I2.3) |
| 3 | $R{=}0{:}\ 4;\ R{=}1{:}\ 50;\ R{=}2{:}\ 48;\ R{=}3{:}\ 12;\ R{=}4{:}\ 12;\ R{=}5{:}\ 26;\ R{=}6{:}\ 26;\ R{=}7{:}\ 136;\ R{=}8{:}\ 136;\ R{=}9{:}\ 764;\ R{=}10{:}\ 763;\ R{=}11{:}\ 763;\ R{=}12{:}\ 763$ |
| 4 | $R{=}0{:}\ 21;\ R{=}1{:}\ 1033;\ R{=}2{:}\ 1032;\ R{=}3{:}\ 20;\ R{=}4{:}\ 20;\ R{=}5{:}\ 103;\ R{=}6{:}\ 102;\ R{=}7{:}\ 573;\ R{=}8{:}\ 573;\ R{=}9{:}\ 573;\ R{=}10{:}\ 572$ |
| 5 | $R{=}0{:}\ 529;\ R{=}1{:}\ 4762;\ R{=}2{:}\ 4762;\ R{=}3{:}\ 82;\ R{=}4{:}\ 82;\ R{=}5{:}\ 459;\ R{=}6{:}\ 459;\ R{=}7{:}\ 458;\ R{=}8{:}\ 458$ |
| 6 | $R{=}0{:}\ 2756;\ R{=}1{:}\ 333506;\ R{=}2{:}\ 333505;\ R{=}3{:}\ 383;\ R{=}4{:}\ 382;\ R{=}5{:}\ 382;\ R{=}6{:}\ 382$ |
| 7 | $R{=}0{:}\ 210021;\ R{=}1{:}\ 35493621;\ R{=}2{:}\ 35493620;\ R{=}3{:}\ 328;\ R{=}4{:}\ 328$ |
| 8 | $R{=}0{:}\ 23777953;\ R{=}1{:}\ 23777953;\ R{=}2{:}\ 23777953$ |
| 9 | $R{=}0{:}\ 16700016$ |

Exactly **54 of the 63** rows with $h \le 1$ have
$J_{\max} \le 5000$. The nine exceptions are
$(6,1), (6,2), (7,0), (7,1), (7,2), (8,0), (8,1), (8,2), (9,0)$.
Two of them, $(6,1)$ and $(8,1)$, are parity-vacuous ($Q$ even, $R$
odd: no even $n$ exists in the row, by (RES-3)(2)).

**Corollary I2.5 (PROVED, modulo the certified frontier F2.19 — what
Claim I2.4 does and does not prove).** Every row with $T \le 16$,
$h \le 1$ and $J_{\max} \le 5000$ contains **no counterexample at
all**: a counterexample in such a row would need $j \le J_{\max}
\le 5000$ (Claim I2.2), but every pair $(3,j)$ with $j \le 5000$ is
closed for all $n$ (F2.19). Three rows are closed by the squared
inequality *alone*, with no frontier input: those with
$J_{\max} = 4$ — $(2,3), (2,4), (3,0)$ — where no $j \ge 5$ is even
feasible. **What this does not prove:** for the nine exception rows
the argument gives only the finite bound $j < B(Q,R)$ (e.g.
$B(7,1) = 35{,}493{,}622$); it does not close them. §3 closes the
seven non-vacuous exceptions by a different, structural argument.
For rows with $T \ge 17$ (any $Q$), Claims I2.1–I2.2 still give a
finite $B(Q,R)$ per row — per-row finiteness is general — but
$B(Q,R) > 5000$ there in general and no row closure follows from §2
alone. (Spot illustration of the exact-vs-analytic gap: at $(5,1)$,
$B_1 = 6615$ analytically but $J_{\max} = 4762$ exactly; the
monotonicity of Claim I2.2 is what makes the exact value, and hence
the closure of that row by the frontier, available.)

## 3. Task I.3 — row-by-row label analysis

**Label convention for this section.** Each row concludes with exactly
one label: **CLOSED** (the argument leaves no candidate; a finite
enumeration of a bounded *form set* is part of the argument, but no
per-triple check is needed), **FINITE LIST** (the argument leaves an
explicit finite candidate set, every member disposed by the direct
computation $\gcd(V_3(n), C(n,j)) > 1$ and by an explicit (LD3)
witness, both scripted), or **EXACT RESIDUAL** (a precise
sub-configuration not excluded). No row treated below ends in EXACT
RESIDUAL; the residual after this section is stated in §4.

### 3.1 The method: two lemmas

**Lemma I3.1 (PROVED — prime powers of non-special tops are $\le T$;
the sharpening announced in D4).** Let $(n,3,j)$ be a counterexample
in an $h = 1$ row, and let $t = n - r_0$ with $r_0 \ne R$ be a
non-special top.
(a) Every prime power $P = p^a \Vert t$ with $p \ge 5$ satisfies
$P \le T$.
(b) If $3 \mid t$ and $e = v_3(t)$, then $3^{e-1} \le T$, i.e.
$e \le 1 + \lfloor \log_3 T \rfloor$ (and the factor of $3$ in $t$ is
at most $3^{1 + \lfloor\log_3 T\rfloor}$; if $e = 1$ this is just $3$).

*Proof.* (a) By the dichotomy (F2.4) applied to the $V_3$-part $P$
(for $p \ge 5$ the $p$-part of $V_3(n)$ is exactly $P$): $P \le T$ or
$P \mid j - r$ for some $r < h = 1$, i.e. $P \mid j$. In the second
case $P \mid t = Qj + (R - r_0)$ as well, so
$P \mid R - r_0$ with $0 < |R - r_0| \le 2 < 5 \le P$: impossible.
(b) Exactly one of three consecutive integers is divisible by $3$;
if $3 \mid t$ it is $t$, and the $3$-part of $V_3(n)$ is $3^{e-1}$.
If $e \ge 2$, apply F2.4 to $3^{e-1}$: it is $\le T$ or divides $j$.
But $\gcd(j, t) = \gcd(j, R - r_0)$ divides $|R - r_0| \le 2$, so
$3 \nmid j$ while $3 \mid 3^{e-1}$; the divisibility alternative is
impossible, hence $3^{e-1} \le T$. $\square$

**Lemma I3.2 (PROVED — the finite form set $M(T)$).** For $T \ge 2$
let $M(T)$ be the set of odd $m \ge 1$ such that
$v_3(m) \le 1 + \lfloor\log_3 T\rfloor$ and, for every $p \ge 5$,
$p^{v_p(m)} \le T$. Then $M(T)$ is finite,
$m \le 3\,\Lambda_3(T)$ for $m \in M(T)$ (each prime power in $m$ is
at most the corresponding factor of $\Lambda_3(T)$, with one extra
factor $3$ available), and:
(a) in an $h = 0$ row, $n - 1 \in M(T)$;
(b) in an $h = 1$ row with $R \in \{0,2\}$, $n - 1 \in M(T)$;
(c) in an $h = 1$ row with $R = 1$, the odd parts of $n$ and of
$n - 2$ both lie in $M(T)$, and $n \le 6\,\Lambda_3(T) + 2$.

*Proof.* (a) $n-1$ is odd. Its $\ge 5$ prime powers are $\le T$ by
F1.9(a); if $3 \mid n-1$ then $n-1$ is the unique $3$-divisible top
and $3^{v_3(n-1)-1}$, the $3$-part of $V_3(n)$, is $\le T$ by
F1.9(a), giving the $v_3$ bound. (b) $n-1$ is the non-special top
with $r_0 = 1 \ne R$; apply Lemma I3.1(a),(b) (for (b), note
$\gcd(j, n-1) = \gcd(j, R-1) = 1$ since $R \in \{0,2\}$, so the proof
of Lemma I3.1(b) applies verbatim). (c) The tops $n$ and $n-2$ are
non-special ($r_0 = 0, 2 \ne 1$); by Lemma I3.1 their odd parts
satisfy the $M(T)$ conditions (for the $3$-part: $\gcd(j, n)$ and
$\gcd(j, n-2)$ divide $|R - r_0| = 1$, so certainly $3 \nmid j$ if
$3$ divides the top). Both tops are even and differ by $2$, so
exactly one of them is $\equiv 2 \pmod 4$, i.e. has $v_2 = 1$; that
top equals $2 \times (\text{its odd part}) \le 2 \cdot 3\Lambda_3(T)$,
and $n$ is at most $2$ more than that top. $\square$

Sizes (script §D): $|M(6)| = 6$, $|M(8)| = 12$, $|M(10)| = 16$,
$|M(12)| = 32$, $|M(14)| = |M(16)| = 64$. In cases (a) and (b) a row
is disposed by listing $m \in M(T)$, setting $n = m + 1$, imposing
$n = Qj + R$ with $n$ even, $j \ge 5$, $R < j$, and disposing the
survivors. In case (c) the row is disposed by enumerating the row up
to $6\Lambda_3(T) + 2$ under the two odd-part filters. Note what this
method does **not** use: neither the $j \le 5000$ frontier nor the
$n \le 10^6$ computation. Its candidate lists are typically far
smaller than §2's thresholds (e.g. at $(5,2)$: no candidates at all,
vs $J_{\max} = 4762$).

### 3.2 Validation (mandatory): row $(4,2)$

**Claim I3.5 (FINITE LIST — validation, reproducing F1.11/V-F
exactly).** Row $(4,2)$: $T = 8$, $h = 1$, $\Lambda_3(8) = 105$,
$V_3(n) \mid 105j$, $n - 1 = 4j + 1$ (non-special top, case (b)).
$M(8) = \{3^b u : b \le 2,\ u \in \{1,5,7,35\}\}$ (12 values). The
values $m \in M(8)$ with $m = 4j + 1$, $j \ge 5$ are exactly
$m = 21, 45, 105$, giving precisely the candidates
$$(n,j) = (22,5),\ (46,11),\ (106,26),$$
and each is disposed: $\gcd(V_3(n), C(n,j)) = 77, 69, 371$
respectively, and each has an (LD3) witness at the top $n$ itself:
$q = 11 \Vert 22$ with $5 \bmod 11 = 5 > 0$; $q = 23 \Vert 46$ with
$11 \bmod 23 = 11 > 0$; $q = 53 \Vert 106$ with $26 \bmod 53 = 26 > 0$.
This matches F1.11's illustration and V-F §5 **in every particular**
(candidate set, gcds, witnesses). The method of §3.1 is therefore
validated against the certified record before use on new rows.
$\square$

### 3.3 The brief's rows

**Claim I3.6 (FINITE LIST — row $(2,4)$).** $T = 6$, $h = 0$,
$\Lambda_3(6) = 15$, so $V_3(n) \mid 15$ (F2.13's starting point).
Case (a): $M(6) = \{1,3,5,9,15,45\}$; $n - 1 = 2j + 3$ with $j \ge 5$
forces $m \ge 15$, leaving $m = 15, 45$: candidates
$(16,6)$ (gcd $7$; (LD3) witness $q = 7 \Vert (n-2)$, $6 \bmod 7
= 6 > 2$) and $(46,21)$ (gcd $759$; witness $q = 23 \Vert n$,
$21 \bmod 23 = 21 > 0$). Both disposed. $\square$

**Claim I3.7 (FINITE LIST — row $(2,6)$).** $T = 8$, $h = 0$, case
(a): $M(8)$ has 12 values; $n - 1 = 2j + 5$, $j \ge 5$ and $R = 6 < j$
leave six candidates, all disposed (gcd; (LD3) witness in script
§D): $(22,8)$: $55$; $(36,15)$: $255$; $(46,20)$: $759$;
$(64,29)$: $651$; $(106,50)$: $689$; $(316,155)$: $37209$.
$\square$

**Claim I3.8 (FINITE LIST — row $(3,4)$, at the corrected $T = 8$).**
$h = 0$, case (a), $M(8)$; $n - 1 = 3j + 3$ must be divisible by $3$,
leaving five candidates, all disposed: $(22,6)$: $77$;
$(46,14)$: $3795$; $(64,20)$: $651$; $(106,34)$: $24115$;
$(316,104)$: $1302315$. $\square$

**Claim I3.9 (CLOSED — row $(3,1)$).** $T = 5$, $h = 1$; $n$ even
forces $j$ odd (RES-3(2)), so $j \ge 5$ and $n = 3j + 1 \ge 16$.
The non-special tops are $n$ and $n - 2$; since $n \equiv 1 \pmod 3$
and $n - 2 \equiv 2 \pmod 3$, neither is divisible by $3$, so each
odd part equals its $\ge 5$ part. By Lemma I3.1(a) every $\ge 5$
prime power of these tops is $\le T = 5$; the only such prime is $5$
itself, to the first power, so **each odd part is in $\{1, 5\}$**.
Exactly one of $n, n-2$ has $v_2 = 1$; that top is
$2 \times (\text{odd part}) \le 10$, hence $n \le 12$ — contradicting
$n \ge 16$. No candidate exists; the row is closed by the argument
alone. (Corroboration: the generic case-(c) filter of Lemma I3.2,
run to the bound $n \le 6\Lambda_3(5) + 2 = 92$, also returns zero
candidates; script §E.) $\square$

**Claim I3.10 (FINITE LIST — row $(4,4)$).** $T = 10$, $h = 0$, case
(a), $|M(10)| = 16$; $n - 1 = 4j + 3 \equiv 3 \pmod 4$ leaves five
candidates, all disposed: $(28,6)$: $819$; $(36,8)$: $255$;
$(64,15)$: $93$; $(136,33)$: $51255$; $(316,78)$: $1302315$.
$\square$

**Claim I3.11 (CLOSED — row $(5,0)$).** $T = 8$, $h = 1$, case (b),
$M(8)$ (12 values). Here $n - 1 = 5j - 1 \equiv 4 \pmod 5$; among the
12 values of $M(8)$ only $m = 9$ is $\equiv 4 \pmod 5$, and it gives
$j = 2 < 5$. The candidate set is **empty** (verifiable by hand from
$M(8) = \{3^b u : b \le 2, u \in \{1,5,7,35\}\}$); the row is closed
with no per-triple check. $\square$

**Claim I3.12 (CLOSED — row $(5,2)$, at the corrected $T = 10$).**
$h = 1$, case (b), $|M(10)| = 16$: $M(10) = \{3^b u : b \le 3,\
u \in \{1,5,7,35\}\}$. Here $n - 1 = 5j + 1 \equiv 1 \pmod 5$; among
the 16 values only $m = 1$ and $m = 21$ are $\equiv 1 \pmod 5$,
giving $j = 0$ and $j = 4$ — neither $\ge 5$ (and $j = 4$ is the
closed-region pair in any case). The candidate set is **empty**;
the row is closed. (At the brief's incorrect $T = 8$ the form set
would be smaller and the conclusion the same; the correction is
recorded because $M(10)$, not $M(8)$, is the honest form set.)
$\square$

**Claim I3.13 (FINITE LIST — row $(2,8)$).** $T = 10$, $h = 0$, case
(a), $|M(10)| = 16$; nine candidates, all disposed:
$(28,10)$: $273$; $(36,14)$: $255$; $(46,19)$: $1265$;
$(64,28)$: $217$; $(106,49)$: $3445$; $(136,64)$: $51255$;
$(190,91)$: $13395$; $(316,154)$: $186045$; $(946,469)$: $8790705$.
$\square$

**Claim I3.14 (FINITE LIST — row $(6,0)$).** $T = 10$, $h = 1$, case
(b), $|M(10)| = 16$; the single candidate is $(36,6)$, disposed
(gcd $357$; witness $q = 9 \Vert n$, $6 \bmod 9 = 6 > 0$).
$\square$

### 3.4 The rows §2 could not close (and one $R=1$ companion)

**Claim I3.15 (FINITE LIST — row $(5,1)$).** $T = 9$, $h = 1$,
$R = 1$: case (c) with bound $n \le 6\Lambda_3(9) + 2 = 1892$. The
odd-part filters on $n$ and $n-2$ leave exactly one candidate,
$(56,11)$, disposed (gcd $105$; witness $q = 7 \Vert n$,
$11 \bmod 7 = 4 > 0$). (This row was already closed by §2,
$J_{\max} = 4762$; the structural list is an independent disposal.)
$\square$

**Claim I3.16 (FINITE LIST — row $(6,2)$).** $T = 12$, $h = 1$, case
(b), $|M(12)| = 32$; two candidates, both disposed: $(56,9)$: $1155$;
$(386,64)$: $74305$. This is one of §2's nine exceptions
($J_{\max} = 333505$). $\square$

**Claim I3.17 (FINITE LIST — row $(7,0)$).** $T = 12$, $h = 1$, case
(b), $|M(12)| = 32$; the single candidate is $(56,8)$, disposed
(gcd $3465$). A §2 exception ($J_{\max} = 210021$). $\square$

**Claim I3.18 (FINITE LIST — row $(7,1)$).** $T = 13$, $h = 1$,
$R = 1$: case (c) with bound $n \le 6\Lambda_3(13) + 2 = 270272$.
The odd-part filters leave exactly one candidate, $(288,41)$,
disposed (gcd $231$; witness $q = 9 \Vert n$, $41 \bmod 9 = 5 > 0$).
A §2 exception ($J_{\max} = 35493621$). $\square$

**Claim I3.19 (FINITE LIST — row $(7,2)$).** $T = 14$, $h = 1$, case
(b), $|M(14)| = 64$; four candidates, all disposed:
$(100,14)$: $5775$; $(352,50)$: $9009$; $(716,102)$: $895895$;
$(1486,212)$: $2574495$. A §2 exception ($J_{\max} = 35493620$).
$\square$

**Claim I3.20 (FINITE LIST — row $(8,0)$).** $T = 14$, $h = 1$, case
(b), $|M(14)| = 64$; fourteen candidates, all disposed:
$(40,5)$: $247$; $(56,7)$: $495$; $(64,8)$: $93$; $(136,17)$: $3015$;
$(144,18)$: $30459$; $(232,29)$: $1265$; $(352,44)$: $20475$;
$(456,57)$: $14755$; $(496,62)$: $40755$; $(1288,161)$: $275847$;
$(2080,260)$: $46801755$; $(4096,512)$: $399165$;
$(15016,1877)$: $37572535$; $(135136,16892)$: $434793645$.
A §2 exception ($J_{\max} = 23777953$). Note the last candidate has
$j = 16892 > 5000$: it lies **beyond** the certified per-pair
frontier, and the structural argument disposes it directly (it is
also within the $n \le 10^6$ (LD3) computation's range, and indeed
has the (LD3) witness $q = 27 \Vert (n-1)$, $16892 \bmod 27
= 17 > 1$). $\square$

**Claim I3.21 (FINITE LIST — row $(8,2)$).** $T = 16$, $h = 1$, case
(b), $|M(16)| = 64$; thirteen candidates, all disposed:
$(66,8)$: $715$; $(106,13)$: $1855$; $(274,34)$: $12467$;
$(298,37)$: $4917$; $(386,48)$: $74305$; $(586,73)$: $57135$;
$(946,118)$: $49665$; $(1002,125)$: $167167$; $(2146,268)$: $767195$;
$(2458,307)$: $1006551$; $(3466,433)$: $2001615$;
$(9010,1126)$: $13528515$; $(19306,2413)$: $1180224045$.
A §2 exception ($J_{\max} = 23777953$). $\square$

**Claim I3.22 (FINITE LIST — row $(9,0)$).** $T = 16$, $h = 1$, case
(b), $|M(16)| = 64$; the single candidate is $(144,16)$, disposed
(gcd $30459$). A §2 exception ($J_{\max} = 16700016$). $\square$

**Claim I3.23 (PROVED, assembly — every row with $T \le 16$ is
accounted for).** Let $(n,3,j)$ be a counterexample with
$T = R + 2(Q-1) \le 16$. Then: if $(Q,R) = (2,0)$, the triple is
excluded by Price's central case; if $Q$ is even and $R$ is odd, no
even $n$ lies in the row (RES-3(2)) — this covers $(6,1)$ and
$(8,1)$ among §2's exceptions, and 14 further rows; if
$J_{\max}(Q,R) \le 5000$, the triple is excluded by Corollary I2.5;
and the remaining seven rows $(6,2), (7,0), (7,1), (7,2), (8,0),
(8,2), (9,0)$ are exactly Claims I3.16–I3.19 and I3.20–I3.22, where
the candidate lists are complete by Lemma I3.2 and every candidate
is disposed. **Hence no counterexample at $i=3$ has $T \le 16$.**
$\square$

## 4. Task I.4 — the even half of (H3) after this work; how (RES-3) shrank

**Claim I4.1 (OPEN — (H3)-even, stated exactly, with a precision
note).** The even half of (H3) is the statement: *the system (LD3)
has no solution $(n,j)$ with $n$ even and $3 < j \le n/2$.* It
remains **OPEN**. Precision note, stated plainly so the accounting
below is not misread: §§2–3 of this file close rows as
**counterexample** rows — Proposition 4.1, the tool behind
$J_{\max}$ and behind the form set $M(T)$, is a statement about
counterexamples (it assumes $\gcd(V_3(n), C(n,j)) = 1$), not about
arbitrary (LD3) solutions. So this file does **not** prove
(H3)-even for any row in its literal (LD3)-only form. What is
certified about (LD3) solutions themselves is the pre-existing
computation: none with $n \le 10^6$ (F1.17/F2.21) and none with
$5 \le j \le 5000$ in the finite-reduction range (F2.18). It is
consistent with everything proved here that (LD3) has even
solutions with $T \ge 17$ which are not counterexamples; the
obstruction to $i=3$ via the low-digit route is unchanged in kind.
In the weaker, operative sense used by F1.11 ("closing the residual
class is equivalent, for the routes in this file, to the even half
of (H3)"), the residual class itself shrank as itemised in Claim
I4.2. (Within the §3 candidate sets, incidentally, every one of the
68 disposed candidates *also* fails (LD3) by an explicit witness —
the script asserts this — so no (LD3) solution hides among the
candidates the counterexample argument produces; the caveat above
concerns (LD3) solutions outside those candidate sets, which the
$ M(T)$ enumeration does not purport to reach.)

**Claim I4.2 (PROVED, assembly — (RES-3) after Cycle 3 Cluster I,
this prover).** A counterexample at $i=3$ must satisfy (RES-3)
(Claim I1.1) **and** $T = R + 2(Q-1) \ge 17$, **and**, in $h=1$
rows, the sharpened bound of Lemma I3.1 (every $\ge 5$ prime power
of a non-special top is $\le T$, replacing the weaker
prime-factor wording of F1.11(iv)). Itemised shrinkage relative to
F1.11/F2.14:
1. **$(4,2)$ removed at reconciliation** (D3, Claim I1.1; validated
   as Claim I3.5): F1.11/F2.14 left it in the residual class; its
   complete candidate set $\{(22,5), (46,11), (106,26)\}$ is
   disposed.
2. **54 rows with $T \le 16$, $h \le 1$, $J_{\max} \le 5000$
   removed by §2** (Claims I2.4–I2.5): any counterexample there
   would need $j \le J_{\max} \le 5000$, contradicting the certified
   frontier. Five of the 54 were already excluded from (RES-3)
   (the F1.10 rows and $(4,2)$); the other 49 are new removals, 14
   of them also parity-vacuous. Three rows — $(2,3), (2,4), (3,0)$ —
   need no frontier input at all ($J_{\max} = 4$).
3. **The seven non-vacuous §2 exceptions removed by §3**:
   $(6,2), (7,0), (7,1), (7,2), (8,0), (8,2), (9,0)$ (Claims
   I3.16–I3.22), by complete finite candidate lists (2, 1, 1, 4,
   14, 13, 1 candidates respectively), each candidate disposed by
   direct gcd computation and an (LD3) witness. The two remaining
   exceptions, $(6,1)$ and $(8,1)$, are parity-vacuous (item D7).
4. **Structural disposals beyond the brief's list** (same claims):
   rows $(2,4), (2,6), (3,4), (3,1), (4,4), (5,0), (5,2), (2,8),
   $(6,0), (5,1)$ are disposed by the $M(T)$ method independently of
   §2 — in particular $(3,1), (5,0), (5,2)$ are CLOSED with empty
   candidate sets, and $(5,2)$ is proved at the corrected $T = 10$.
   These overlap item 2 (all ten also have $J_{\max} \le 5000$); the
   value added is a frontier-free proof for those rows, with
   candidate maxima far below $J_{\max}$ (e.g. $(5,2)$: no
   candidates, vs $J_{\max} = 4762$; $(8,0)$ in item 3: largest
   candidate $j = 16892$, vs $J_{\max} = 23777953$).
5. **Per-row finiteness is now general** (Claims I2.1–I2.2): every
   row with $h \le 1$ — including all rows with $T \ge 17$ — carries
   an explicit finite bound $j < B(Q,R)$; the residual is a union of
   individually finite rows with $T \ge 17$, not a single
   undifferentiated class. The one row where the squared-half
   derivation fails, $(2,0)$, is closed by Price (Claim I2.3).
Nothing else in (RES-3) changed: conditions 1, 3, 4, 5 of Claim
I1.1 stand as reconciled, and rows with $T \ge 17$ are untouched by
§§2–3 beyond item 5 and the Lemma I3.1 sharpening.

## 5. Closing statement

*Proved in this file, beyond Cycle 2:*
1. (RES-3): one reconciled residual statement for $i=3$, with the
   nine discrepancies D1–D9 between F1.11 and F2.14 resolved
   explicitly (Claim I1.1).
2. Per-row finiteness from the squared half of Proposition 4.1:
   explicit analytic bounds for $h = 0$ and $h = 1$ (Claim I2.1),
   threshold monotonicity (Claim I2.2), exact $J_{\max}$ for all 64
   rows with $T \le 16$ (Claim I2.4), and the resulting closure of
   the 54 rows with $J_{\max} \le 5000$ via the certified frontier
   (Corollary I2.5).
3. A refutation, at $(2,0)$, of the universal form of that
   finiteness derivation (Claim I2.3): the squared inequality there
   holds for all $j \ge 6$.
4. The non-special-top prime-power bound (Lemma I3.1), the finite
   form set $M(T)$ with $m \le 3\Lambda_3(T)$ and the $R = 1$ bound
   $n \le 6\Lambda_3(T) + 2$ (Lemma I3.2), the exact reproduction of
   the $(4,2)$ validation (Claim I3.5), CLOSED rows $(3,1), (5,0),
   (5,2)$, and FINITE LIST disposals for 15 rows in all (including
   the $(4,2)$ validation) — 68 candidates in total, every one
   disposed by a direct gcd $> 1$ and
   an explicit (LD3) witness (Claims I3.6–I3.22).
5. The assembled consequence: **no counterexample at $i=3$ has
   $T \le 16$** (Claim I3.23); the residual class is (RES-3) with
   $T \ge 17$ (Claim I4.2).

*Reduced:* the even residual class of F1.11/F2.14 is reduced to its
$T \ge 17$ part, with the $h=1$ prime-power condition sharpened
(Lemma I3.1) and an explicit per-row finite bound $B(Q,R)$ on $j$
in every $h \le 1$ row.

*Still OPEN, explicitly:* the residual class with $T \ge 17$ in
general (rows are infinite in number — $Q$ and $R$ are unbounded —
and $M(T)$ grows with $\Lambda_3(T)$, so the §3 method, while it
disposes any *fixed* row in principle, gives no uniform argument);
(H3) in general, and its even half in the literal (LD3)-only form
(Claim I4.1); per-pair (LD3) closure for $j > 5000$ by computation
(that is Cluster K's territory, not this file's). **$i=3$ is not
closed, (H3) is not proved, and #699 is not claimed solved.**

## 6. Verification log

All numbers above are outputs of `proofs/P-I1_checks.py`
(Python stdlib only, exact integer and rational arithmetic; all
assertions passed; runtime 0.4 s of computation, under 1 s wall):
- §A: $\Lambda_3(T)$ for $T = 0..16$ asserted against the table in
  Claim I2.4.
- §B: the $(2,0)$ ratio identity
  $\binom{j}{2}^2/C(2j,3) = 3j(j-1)/(8(2j-1))$ and its being $> 1$
  verified exactly (Fractions) for $6 \le j < 2000$; the $j = 5$
  value $100/120 < 1$ also asserted.
- §C: $J_{\max}$ for all 63 rows with $T \le 16$, $h \le 1$, by
  binary search; for every row the script asserts feasibility at
  $J_{\max}$ (when $\ge 5$), infeasibility at $J_{\max} + 1$, and
  infeasibility at the Claim I2.1 analytic cap; the exception list
  is asserted to be exactly the nine rows named in Claim I2.4.
- §C3: monotonicity of $C(Qj+R,3)/j^2$ spot-verified exactly
  ($j = 5..300$ and around $J_{\max}$) for every $h = 1$ row — a
  check on, not a substitute for, the proof of Claim I2.2.
- §D: $M(T)$ candidate lists for the 15 odd-top rows of §3 asserted
  equal to the lists printed in Claims I3.5–I3.22 (66 candidates);
  for every candidate the script asserts $\gcd(V_3(n), C(n,j)) > 1$
  (values as printed per claim) **and** the existence of an explicit
  (LD3) witness $(r, p, a, q, j \bmod q)$ with $j \bmod q > r$
  (printed in the script output); the $(4,2)$ gcds are asserted to
  be $[77, 69, 371]$ in order.
- §E: the $R = 1$ enumerations: $(3,1)$ returns zero candidates up
  to $n \le 92$; $(5,1)$ returns exactly $[(56,11)]$ up to
  $n \le 1892$; $(7,1)$ returns exactly $[(288,41)]$ up to
  $n \le 270272$; gcd and (LD3)-witness assertions as in §D.
