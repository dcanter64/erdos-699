# Prover I2 (independent): Cycle 3, Cluster I, the even residual class at $i=3$, attacked row by row

Prover: I2, working independently in Cycle 3. I did **not** read
`proofs/P-I1.md` (the other Cluster I prover's file); independence is
methodologically essential and was preserved. Sources read, as assigned:
`CYCLE2.md` §2 and §§8–9; `proofs/P-F1.md` in full; `proofs/P-F2.md`
§§1–3 and §7; `verification/V-F.md`; `proofs/P-A1.md` (Lemma A1.15,
Proposition A1.16, Statement (H3), Theorem A1.17); `strategies/S8.md`
§3; `EXTERNAL_CLAIMS_2026-10-29.md` (the Van Doorn–Rocca diagnosis).
Every computation below is in `proofs/P-I2_checks.py` (Python standard
library only, exact integer arithmetic; total runtime about 0.1 s on
this machine), and every number quoted from it is asserted inside the
script. Every numbered claim is labelled PROVED, GAP, FALSE, OPEN, or
COMPUTATION.

**Headline.** $i=3$ is **not** closed and (H3) is **not** proved. What
this file adds: (I.1) F1.11 and F2.14 are reconciled into one exact
residual statement, RES-3 (Claim I2.1), with the discrepancies between
the two formulations itemised. (I.2) For every fixed row $(Q,R)$ with
$h\le 1$, the squared half of Price's Proposition 4.1 gives an explicit
finite bound $j<B^{*}(Q,R)$ for counterexamples in that row; $B^{*}$ is
computed exactly for all 64 rows with $T\le 16$; exactly 54 of them
(42 with $h=0$ and 12 with $h=1$) have $B^{*}\le 5000$, and 50 of
those 54 lie in the residual class of §1 (the other 4 are rows
already closed before this cycle), so those 50 are already entirely
closed once the certified per-pair frontier $j\ge 5001$ is imposed. The finiteness statement as stated for **all**
rows is FALSE: the unique $h=2$ row $(2,0)$ is a counterexample to it
(Claim I2.4); that row is closed by Price's central case, not by size.
(I.3) A label argument that neither F prover used in this form, the
elimination lemma (Claim I2.7), shows that (LD3) **alone** (no EEES78,
no Proposition 4.1) reduces every fixed row to an explicit finite
list; carrying the disposal out for all rows with $T\le 16$ closes
every one of them for the even class, including the 9 rows with
$B^{*}>5000$ that (I.2) cannot reach. The (4,2) analysis of F1.11 is
reproduced exactly as a validation step before the method is trusted
(Claim I2.10). (I.4) The even half of (H3) is restated with the
$T\le 16$ rows removed: a putative even (LD3) solution, and a putative
even counterexample, must now lie in a row with $T\ge 17$ (Claim
I2.15). That remaining class is OPEN.

**Corrections to the brief (flagged prominently, per standing
campaign practice).** No certified input from the files was found to
be wrong; every F1/F2 statement used below was checked against V-F or
recomputed. But two annotations in my assignment brief are arithmetic
slips: the brief annotates the row $(3,4)$ with "$T=7$" and groups
$(5,2)$ under "$T=8$". Direct computation from $T=R+2(Q-1)$ gives
$T=8$ for $(3,4)$ and $T=10$ for $(5,2)$ (the $T=8$ value is correct
for $(5,0)$). I use the correct values throughout; no conclusion
depends on the brief's annotations. The brief's starting point for
$(2,4)$, namely F2.13's $V_3(n)\mid 15$ there, is correct
($T=6$, $\Lambda_3(6)=15$).

## 0. Standing inputs and notation

$i=3$ throughout. A **counterexample** is a triple $(n,3,j)$,
$3<j\le n/2$, with $\gcd(V_3(n),C(n,j))=1$, where $V_3(n)$ is the part
of $C(n,3)$ on primes $\ge 3$. Write $n=Qj+R$ with
$Q=\lfloor n/j\rfloor\ge 2$ and $0\le R<j$; a pair $(Q,R)$ is a
**row**. Put $T=R+2(Q-1)$ and
$h=\max(0,\lceil(3-R)/Q\rceil)$; $h=2$ only for $(Q,R)=(2,0)$,
$h=1$ for $R\in\{0,1,2\}$ otherwise, $h=0$ for $R\ge 3$.
$\Lambda_3(T)=\prod_{q\ge 3}q^{\lfloor\log_q T\rfloor}$
($\Lambda_3(T)=1$ for $T\le 2$). For $m\in\{n,n-1,n-2\}$, $R(m)$ is the
product of the relevant prime powers $q=p^a\parallel m$ ($p\ge 5$, any
$a\ge 1$; or $p=3$, $a\ge 2$), and $U_r$ is the part of $n-r$ on primes
$\ge 5$.

Certified inputs used (V-F certified unless noted): (LD3) and its
splitting form; (N1); (N2); Price Proposition 4.1 at $i=3$ in both
halves, namely $V_3(n)\mid\Lambda_3(T)\binom{j}{h}$ (divisibility half,
no EEES78) and $C(n,3)<(\Lambda_3(T)\binom{j}{h})^2$ (squared half,
via EEES78); the per-part dichotomy F1.1/F2.4; F1.9 and F2.9 (genuine
split parts at $p\ge 5$ are $\le T$ for $(Q,R)\ne(2,0)$); F1.7 (no
relevant $q\parallel(n-1)$ with $q>(n-1)/3$ for even $n$); F1.8
($n\le 3j(j-1)+1$ for even $n$); F1.10 (rows $(2,2),(3,0),(3,2),(4,0)$
closed); Price's central case (row $(2,0)$ closed); SPLIT-odd closed
(no counterexample has $n$ odd); F1.13/F2.15 ($v_2(C(n,3))\le 3$ is
not a counterexample, so $v_2(C(n,3))\ge 4$ is necessary); the
computations that (LD3) has no solution with $n\le 10^6$ and no
solution with $2j\le n\le N(3,j)$ for any $5\le j\le 5000$, so every
pair $(3,j)$ with $j\le 5000$ is closed for all $n$, and a
counterexample must have $n$ even, $j\ge 5001$, $n>10^6$.

## 1. Task I.1: one exact residual statement (RES-3)

**Claim I2.1 (PROVED, as a reconciliation of F1.11 and F2.14).**
Intersecting F1.11, F2.14, and the certified frontier conditions of
§0, a counterexample at $i=3$ must satisfy **all** of the following
simultaneously. This conjunction is the single residual statement
**(RES-3)** used in the rest of this file.

* (a) $n$ even, $j\ge 5001$, $n>10^6$, $v_2(C(n,3))\ge 4$,
  $3<j\le n/2$.
* (b) $(Q,R)\notin\{(2,0),(2,2),(3,0),(3,2),(4,0)\}$.
* (c) (LD3) in full, in splitting form: $R(n)\mid j$;
  $R(n-1)=X_0X_1$, $X_0\mid j$, $X_1\mid j-1$;
  $R(n-2)=Y_0Y_1Y_2$, $Y_s\mid j-s$.
* (d) (N1) and (N2): $V_3(n)\mid C(j,3)$.
* (e) $V_3(n)\mid\Lambda_3(T)\binom{j}{h}$ (Proposition 4.1,
  divisibility half).
* (f) Per-part dichotomy, in its at-least-one form (the "exactly one"
  wording of F2.4 is literally false, as V-F records; only the
  at-least-one form is used anywhere): every full prime-power part
  $p^a$ of $V_3(n)$ satisfies $p^a\le T$ or $p^a\mid j-r$ for some
  $0\le r<h$. For $p\ge 5$ the part is the relevant prime power of the
  unique top $n-r_0$ divisible by $p$; for $p=3$ the part is
  $3^{e-1}$, one factor of $3$ below the (LD3) prime power $3^e$ when
  $e\ge 2$. In particular every genuine split part (a prime power at
  $p\ge 5$ that (LD3) assigns to $j-1$ or $j-2$ but not to $j$) is
  $\le T$, for $(Q,R)\ne(2,0)$ (F2.9).
* (g) The label consequences of F1.9: if $R\ge 3$ ($h=0$), every
  prime-power part of $V_3(n)$ is $\le T$, every $\ge 5$ prime power
  of every top is $\le T$, the $3$-part of $V_3(n)$ is $\le T$ (the
  exact $3$-power of a top may be $3T$), and
  $V_3(n)\mid\gcd(C(j,3),\Lambda_3(T))$ (F2.13). If
  $R\in\{0,1,2\}$ ($h=1$), every top $n-r$ with $r\ne R$ has no prime
  factor $>T$ in its $\ge 5$ part (this is a statement about primes,
  not prime powers: a prime power $p^a$ with $p\le T<p^a$ is
  constrained only through (f)), and every $\ge 5$ prime power
  $P\parallel(n-R)$ with prime $>T$ divides $j$.
* (h) No relevant prime power $q\parallel(n-1)$ exceeds $(n-1)/3$
  (F1.7), and $n\le 3j(j-1)+1$ (F1.8).

In the terminology of F2.14: condition (g), first case, is (E-res 2)
with the $3$-part included; condition (f) plus (g), second case, is
(E-res 1) with the per-part statement kept separate from the prime
statement. **(RES-3) is OPEN**: no argument in the Cycle 2 record, and
none in §§2–3 below outside the rows disposed there, excludes it in
general.

*Discrepancies between F1.11 and F2.14, and how each is resolved in
(RES-3).* (D1) **Closed rows.** F1.11 is stated after F1.10, so it
excludes $(2,2),(3,0),(3,2),(4,0)$ (and Price's $(2,0)$). F2.14 is
stated after F2's weaker even cut, so its (E-res 1) still contains
$(2,2)$ and $(3,0)$, subject only to Proposition F2.12's
$U_0U_1U_2\mid j$ conclusion, and contains the row $(2,1)$, which is
parity-impossible for even $n$ ($n=2j+1$ is odd). (RES-3) adopts
F1.11's sharper list (condition (b)) and drops $(2,1)$ by parity.
(D2) **The $j$ threshold inside F2.14.** F2.14 as written carries
"$j\ge 159$" (§4 of that file at the point of statement), superseded
within the same file by F2.19's $j\ge 5001$. (RES-3) uses $j\ge 5001$
(condition (a)); the $159$ figure is not a contradiction, it is an
unsharpened intermediate. (D3) **The $3$-part in $h=0$ rows.** F1.11
(iii) bounds every prime-power part of $V_3(n)$, including its
$3$-part, by $T$; F2.14's (E-res 2) states the bound only at
$p\ge 5$ and adds $V_3(n)\mid\gcd(C(j,3),\Lambda_3(T))$. Both follow
from $V_3(n)\mid\Lambda_3(T)$; (RES-3)(g) states the conjunction.
(D4) **Primes versus prime powers in $h=1$ rows.** F1.11(iv) says
tops $n-r$, $r\ne R$, have all their $\ge 5$ prime **factors** $\le
T$. Read as a prime-power statement this would be stronger than
F1.9's proof supports; F2.4's dichotomy is the correct prime-power
statement. (RES-3) keeps the two apart ((f) for prime powers, (g)
for primes). (D5) **Extra F1 conditions.** F1.11 includes F1.7 and
F1.8 explicitly; F2.14 does not list them. They are certified
necessary conditions, so (RES-3) includes them as (h). No discrepancy
of substance was found beyond (D1)–(D5): in particular the two
formulations agree on (LD3), (N1), (N2), and the Proposition 4.1
divisibility. $\square$

## 2. Task I.2: per-row finiteness from the squared half

For a fixed row, $C(Qj,3)\le C(n,3)$ (since $n=Qj+R\ge Qj$ and
$C(\cdot,3)$ is increasing), so a counterexample in the row satisfies
$$C(Qj,3)\;<\;\bigl(\Lambda_3(T)\binom{j}{h}\bigr)^2. \tag{$\ast$}$$
Write $B^{*}(Q,R)=J_{\max}+1$, where $J_{\max}$ is the largest
$j\ge 1$ satisfying $(\ast)$ when that set is finite; a counterexample
in the row then has $j<B^{*}(Q,R)$.

**Claim I2.2 ($h=0$: PROVED).** Let $R\ge 3$ and $\Lambda=\Lambda_3(T)$.
If $(\ast)$ holds then
$(Qj-2)^3<6\Lambda^2$, i.e.
$j<\bigl((6\Lambda^2)^{1/3}+2\bigr)/Q$. Hence the set of $j$
satisfying $(\ast)$ is finite, $B^{*}(Q,R)$ is well defined, and it
is an initial segment: $C(Qj,3)$ is nondecreasing in $j$ and strictly
increasing once $Qj\ge 3$.

*Proof.* $C(Qj,3)=(Qj)(Qj-1)(Qj-2)/6\ge (Qj-2)^3/6$ for $Qj\ge 3$
(each factor is $\ge Qj-2$), and $(\ast)$ with $\binom{j}{0}=1$ gives
$C(Qj,3)<\Lambda^2$. Combine. $\square$

**Claim I2.3 ($h=1$: PROVED).** Let $h=1$ and $\Lambda=\Lambda_3(T)$.
For $j>0$, $(\ast)$ is equivalent to
$\varphi(j):=\frac{Q}{6}\bigl(Q^2j-3Q+2/j\bigr)<\Lambda^2$, and
$\varphi$ is strictly increasing; hence the satisfying set is an
initial segment, $B^{*}(Q,R)$ is well defined, and every satisfying
$j$ obeys the explicit closed-form bound
$$j\;<\;\frac{6\Lambda^2}{Q^3}+\frac{3}{Q}.$$

*Proof.* Dividing $(\ast)$ by $j^2$:
$C(Qj,3)/j^2=\frac{Q(Qj-1)(Qj-2)}{6j}
=\frac{Q}{6}\bigl(Q^2j-3Q+2/j\bigr)=\varphi(j)$.
$\varphi(j+1)-\varphi(j)=\frac{Q}{6}\bigl(Q^2-\frac{2}{j(j+1)}\bigr)>0$
for $Q\ge 2$, $j\ge 1$. Since $2/j>0$,
$\varphi(j)>\frac{Q}{6}(Q^2j-3Q)$, and $\varphi(j)<\Lambda^2$ then
gives $Q^2j-3Q<6\Lambda^2/Q$, the displayed bound. $\square$

**Claim I2.4 (the universal finiteness statement is FALSE at $h=2$).**
For the unique $h=2$ row $(Q,R)=(2,0)$, $(\ast)$ imposes **no**
finite bound on $j$: exactly,
$\dfrac{C(2j,3)}{\binom{j}{2}^2}=\dfrac{8(2j-1)}{3j(j-1)}\longrightarrow 0$
as $j\to\infty$, so $(\ast)$ holds for all sufficiently large $j$.
Per-row finiteness from the squared half is therefore a theorem for
$h\le 1$ rows only. The $(2,0)$ row is closed by Price's central case
($n=2j$), independently of size. $\square$

**Claim I2.5 (COMPUTATION: the exact thresholds for $T\le 16$).**
Script §A computes $\Lambda_3(T)$ for $T\le 16$:
$1,1,1,3,3,15,15,105,105,315,315,3465,3465,45045,45045,45045,45045$
($T=0,\dots,16$), then for each of the 64 rows with $T\le 16$ finds
$J_{\max}$ by binary search on the monotone inequalities of Claims
I2.2 and I2.3, asserting the endpoint conditions
$(\ast)$ holds at $J_{\max}$ and fails at $J_{\max}+1$ for every row.
$J_{\max}$ depends only on $Q$ and $\Lambda_3(T)$ (and the $h$ class);
grouping consecutive $R$ with equal $B^{*}$, the full table is:

| $Q$ | rows ($R$ ranges) and $B^{*}$ |
|---|---|
| 2 | $R{=}0$: $h{=}2$, none. $R{=}1,2$: $9$. $R{=}3,4$: $7$. $R{=}5,6$: $21$. $R{=}7,8$: $43$. $R{=}9,10$: $209$. $R{=}11$ to $14$: $1151$. |
| 3 | $R{=}0$: $3$. $R{=}1,2$: $51$. $R{=}3,4$: $14$. $R{=}5,6$: $29$. $R{=}7,8$: $140$. $R{=}9$ to $12$: $768$. |
| 4 | $R{=}0$: $22$. $R{=}1,2$: $1035$. $R{=}3,4$: $22$. $R{=}5,6$: $105$. $R{=}7$ to $10$: $576$. |
| 5 | $R{=}0$: $530$. $R{=}1,2$: $4764$. $R{=}3,4$: $84$. $R{=}5$ to $8$: $461$. |
| 6 | $R{=}0$: $2757$. $R{=}1,2$: $333507$. $R{=}3$ to $6$: $384$. |
| 7 | $R{=}0$: $210022$. $R{=}1,2$: $35493622$. $R{=}3,4$: $329$. |
| 8 | $R{=}0,1,2$: $23777954$. |
| 9 | $R{=}0$: $16700017$. |

Counts: 64 rows; 42 with $h=0$, 21 with $h=1$, 1 with $h=2$.
**Every $h=0$ row has $B^{*}\le 1151\le 5000$.** The $h=1$ rows with
$B^{*}\le 5000$ are exactly
$(2,1),(2,2),(3,0),(3,1),(3,2),(4,0),(4,1),(4,2),(5,0),(5,1),(5,2),
(6,0)$ (12 rows, $B^{*}$ values
$9,9,3,51,51,22,1035,1035,530,4764,4764,2757$).
The $h=1$ rows with $B^{*}>5000$ are exactly
$(6,1),(6,2),(7,0),(7,1),(7,2),(8,0),(8,1),(8,2),(9,0)$ (9 rows,
$B^{*}$ values $333507,333507,210022,35493622,35493622,23777954,
23777954,23777954,16700017$). $\square$

**Claim I2.6 (what I.2 does and does not prove: PROVED, as a scope
statement).** (i) By itself, Claim I2.2/I2.3 proves only this: a
counterexample in a fixed $h\le 1$ row has $j<B^{*}(Q,R)$. It uses
the squared half, hence EEES78; it says nothing about (LD3)
solutions that are not counterexamples. (ii) Combined with the
certified frontier (a counterexample has $j\ge 5001$, §0), every row
with $B^{*}\le 5000$ contains no counterexample at all. Among the
rows present in (RES-3) (condition (b) already removes
$(2,0),(2,2),(3,0),(3,2),(4,0)$), that is **50 rows removed by I.2**:
all 42 $h=0$ rows, and the 8 $h=1$ rows
$(2,1),(3,1),(4,1),(4,2),(5,0),(5,1),(5,2),(6,0)$. (iii) For the 9
$h=1$ rows with $B^{*}>5000$, I.2 gives a finite bound and nothing
more; those rows are **not** closed by I.2. They are closed in §3
below by a different argument (for (LD3) solutions, not only
counterexamples). $\square$

## 3. Task I.3: the elimination lemma and row-by-row closure for $T\le 16$

The method generalises the $(n-1)$ step of F1.10. F1.10 applied an
elimination only to prime powers that Proposition 4.1 had first
forced into $j$. (LD3) itself assigns **every** relevant prime power
of **every** top to a specific $j-s$, and eliminating $j$ between the
top and its assigned target bounds the whole group of prime powers
assigned to that target, with no reference to $T$, to Proposition
4.1, or to EEES78.

**Claim I2.7 (the elimination lemma: PROVED).** Let $(n,j)$ satisfy
(LD3), $n=Qj+R$. For a top index $t\in\{0,1,2\}$ and
$s\in\{0,\dots,t\}$, let $G_{t,s}$ be the product of the relevant
prime powers $q\parallel(n-t)$ with $j\bmod q=s$ (equivalently
$q\mid j-s$), with $G_{t,s}=1$ if there are none. Then:

* (i) The assignment is a partition: each relevant $q$ occurs for
  exactly one $s$ (if $q\mid j-s_1$ and $q\mid j-s_2$ then
  $q\mid|s_1-s_2|\le 2<3\le q$), and
  $R(n-t)=\prod_{s=0}^{t}G_{t,s}$.
* (ii) If $D_{t,s}:=Qs+R-t\ne 0$, then $G_{t,s}\mid D_{t,s}$.
* (iii) $D_{t,s}=0$ only in the aligned cases: $s=0$ and $R=t$, or
  $(Q,R,t,s)=(2,0,2,1)$ (where $n-2=2(j-1)$ identically).

*Proof.* (i) is (LD3) plus the uniqueness just shown. (ii) Each $q$
in the group divides both $n-t$ and $j-s$, hence divides
$(n-t)-Q(j-s)=Qj+R-t-Qj+Qs=D_{t,s}$; the $q$ are pairwise coprime,
so their product divides $D_{t,s}$. (iii) $Qs+R=t\le 2$ with $Q\ge 2$:
if $s=0$ then $R=t$; if $s\ge 1$ then $Qs\ge 2$ forces
$Q=2$, $s=1$, $R=0$, $t=2$. $\square$

**Claim I2.8 (rows $R\ne 1$: an explicit (LD3) bound: PROVED).** Let
$(n,j)$ satisfy (LD3) with $n$ even, in a row with $R\ne 1$. Then
$$R(n-1)\ \Big|\ (R-1)(Q+R-1),
\qquad\text{hence}\qquad
n\ \le\ 3\,\bigl|(R-1)(Q+R-1)\bigr|+1.$$

*Proof.* Apply Claim I2.7 at $t=1$: $D_{1,0}=R-1\ne 0$ (since
$R\ne 1$) and $D_{1,1}=Q+R-1\ge 1$, so
$R(n-1)=G_{1,0}G_{1,1}$ divides $(R-1)(Q+R-1)$. Since $n$ is even,
$n-1$ is odd; an odd number $m$ equals $R(m)$ unless $v_3(m)=1$, in
which case it equals $3R(m)$ (in the second case $3\nmid R(m)$).
Hence $n-1\le 3\,|R(n-1)|$ and the bound follows. Note the proof uses
only (LD3) and parity: it bounds (LD3) solutions, not merely
counterexamples. $\square$

**Claim I2.9 (rows $R=1$: an explicit finite reduction: PROVED).**
Let $(n,j)$ satisfy (LD3) with $n$ even, in a row with $R=1$ ($Q$
fixed). Then $R(n)=1$, so $n=2^a3^b$ with $a\ge 1$ and $b\le 1$; and
$R(n-2)\mid(Q-1)(2Q-1)$, so the odd part $M$ of $n-2$ obeys
$M\le 3(Q-1)(2Q-1)=:B_M(Q)$. Consequently $a$ is explicitly bounded:
$a\le 1$ gives $n\le 6$ (no $j>3$); for $a\ge 2$, $M=2^{a-1}-1$ if
$b=0$ and $M=3\cdot 2^{a-1}-1$ if $b=1$, giving
$a\le 1+\lfloor\log_2(B_M(Q)+1)\rfloor$ resp.
$a\le 1+\lfloor\log_2((B_M(Q)+1)/3)\rfloor$. Each $R=1$ row therefore
contains only finitely many possible even (LD3) solutions, with an
explicit enumeration.

*Proof.* At $t=0$ the only group is $s=0$ and $D_{0,0}=R=1\ne 0$, so
Claim I2.7 gives $R(n)\mid 1$. At $t=2$ the values
$D_{2,0}=-1$, $D_{2,1}=Q-1$, $D_{2,2}=2Q-1$ are all nonzero, so
$R(n-2)=G_{2,1}G_{2,2}$ divides $(Q-1)(2Q-1)$. The odd part $M$ of
$n-2$ has the same odd prime powers as $n-2$, so as in Claim I2.8,
$M=R(n-2)$ or $M=3R(n-2)$. For $a\ge 2$, $n-2=2\cdot(\text{odd})$
with odd part $2^{a-1}-1$ ($b=0$) or $3\cdot2^{a-1}-1$ ($b=1$).
$\square$

*Remark.* Claims I2.8 and I2.9 together say that (LD3) alone gives
per-row finiteness for **every** fixed row, a statement orthogonal
to §2 (which bounds counterexamples via EEES78). Finiteness per row
is not a proof of (H3): there are infinitely many rows, the bounds
grow with $(Q,R)$, and each row still needs its finite list
disposed. §3.2–§3.4 dispose all rows with $T\le 16$.

### 3.1 Validation: the $(4,2)$ analysis, reproduced exactly

**Claim I2.10 (COMPUTATION, validation of the method).** Before the
elimination method is trusted on new rows, the $(4,2)$ illustration
of F1.11 is reproduced exactly, by its original argument (script
§B). For $(Q,R)=(4,2)$: $T=8$, $\Lambda_3(8)=105$,
$V_3(n)\mid 105j$, $m=n-1=4j+1$ with $\gcd(j,m)=1$. F1.9(b) excludes
prime factors $>8$ of $m$; the $3$-, $5$-, $7$-parts of $m$ are
bounded by $V_3(n)\mid 105j$ with $3,5,7\nmid j$, leaving
$m=3^b5^a7^c$ with $b\le 2$, $a,c\le 1$ and $m\equiv 1\pmod 4$.
Enumerating those $m$ with $j=(m-1)/4\ge 5$ leaves **precisely**
$(n,j)=(22,5)$ ($m=21$), $(46,11)$ ($m=45$), $(106,26)$ ($m=105$),
and each is then killed by (LD3), already at $r=0$:
$\gcd(V_3(n),C(n,j))=77, 69, 371$ respectively, with (LD3) witnesses
$q=11\parallel 22$, $q=23\parallel 46$, $q=53\parallel 106$ (in each
case $j\bmod q=j>0$). This matches F1.11 and V-F §5 digit for digit.
The disposal is per-instance, as F1 states; what §3.2 adds is that
the elimination lemma turns the same style of argument into a
complete row closure, because it is applied to (LD3) assignments
directly rather than to the Proposition 4.1 survivors. $\square$

### 3.2 Hand closures of the specified rows

For a row with $R\ne 1$, write $P(D)$ for the set of possible group
products $G_{1,s}$ at $D_{1,s}=D$: products of distinct relevant
prime powers each dividing $D$ (so $P(D)$ consists of divisors of
$D$ whose prime-power factors are all relevant; e.g. $P(3)=\{1\}$
since $3^1$ is not relevant, $P(6)=\{1\}$, $P(9)=\{1,9\}$). By Claim
I2.7, $\rho:=R(n-1)\in\{g_0g_1:g_0\in P(R-1),\,g_1\in P(Q+R-1)\}$
(the two groups are coprime), and $n-1\in\{\rho\}\cup\{3\rho:3\nmid
\rho\}$ (the second case is $v_3(n-1)=1$, where $3\nmid\rho$ by
definition of $R(n-1)$). Solving $Qj+R-1$ against that finite set,
with $j>3$ and $n$ even, gives each row's candidate list; a listed
candidate is disposed by the (LD3) witness shown (a relevant
$q\parallel(n-r)$ with $j\bmod q>r$, which by Lemma A1.15 gives a
common prime $\ge 3$, so the pair is not a counterexample and not an
(LD3) solution). Each list below is confirmed by script §E.

**Claim I2.11 (PROVED: the specified $R\ne 1$ rows).** In increasing
$T$:

* (a) $(2,4)$, $T=6$, $h=0$: $P(3)=\{1\}$, $P(5)=\{1,5\}$, so
  $\rho\in\{1,5\}$ and $n-1\in\{1,5,3,15\}$. With $n-1=2j+3$ the only
  value with $j>3$ is $15$: candidate $(16,6)$, killed by
  $q=7\parallel(n-2)=14$, $6\bmod 7=6>2$. **CLOSED** (finite list of
  one, disposed).
* (b) $(3,4)$, $T=8$ (not $7$; see the corrections note), $h=0$:
  $P(3)=\{1\}$, $P(6)=\{1\}$, so $\rho=1$ and $n-1\in\{1,3\}$, but
  $n-1=3j+3\ge 18$ for $j\ge 5$. No candidates. **CLOSED** outright.
* (c) $(2,6)$, $T=8$, $h=0$: $P(5)=\{1,5\}$, $P(7)=\{1,7\}$, so
  $\rho\in\{1,5,7,35\}$ and
  $n-1\in\{1,5,7,35,3,15,21,105\}$. With $n-1=2j+5$: candidates
  $(16,5)$ ($m=15$, witness $q=7\parallel 14$, $5\bmod 7=5>2$),
  $(22,8)$ ($m=21$, witness $q=11\parallel 22$, $8\bmod 11=8>0$),
  $(36,15)$ ($m=35$, witness $q=9\parallel 36$, $15\bmod 9=6>0$),
  $(106,50)$ ($m=105$, witness $q=53\parallel 106$,
  $50\bmod 53=50>0$). **CLOSED** (finite list of four, all disposed).
* (d) $(4,4)$, $T=10$, $h=0$: $P(3)=\{1\}$, $P(7)=\{1,7\}$, so
  $\rho\in\{1,7\}$ and $n-1\in\{1,7,3,21\}$. With $n-1=4j+3$: $7$
  gives $j=1$ (inadmissible), $21$ gives no integer $j$, the rest
  none. No admissible candidates. **CLOSED** outright.
* (e) $(5,0)$, $T=8$, $h=1$: $P(-1)=\{1\}$, $P(4)=\{1\}$, so
  $\rho=1$ and $n-1\in\{1,3\}$, but $n-1=5j-1\ge 29$ for admissible
  even $n$ ($j$ even). No candidates. **CLOSED** outright.
* (f) $(5,2)$, $T=10$ (not $8$), $h=1$: $P(1)=\{1\}$, $P(6)=\{1\}$,
  so $\rho=1$ and $n-1\in\{1,3\}$, but $n-1=5j+1$. No candidates.
  **CLOSED** outright.
* (g) $(2,8)$, $T=10$, $h=0$: $P(7)=\{1,7\}$, $P(9)=\{1,9\}$, so
  $\rho\in\{1,7,9,63\}$ and, applying the rule
  $n-1\in\{\rho\}\cup\{3\rho:3\nmid\rho\}$ (so $27=3\cdot 9$ and
  $189=3\cdot 63$ do **not** occur, since $3\mid\rho$ there and
  $v_3(n-1)=1$ would force $3\nmid\rho$), $n-1\in\{1,7,9,63,3,21\}$.
  With $n-1=2j+7$: candidates $(22,7)$ ($m=21$, witness
  $q=11\parallel 22$, $7\bmod 11=7>0$) and $(64,28)$ ($m=63$,
  witness $q=31\parallel(n-2)=62$, $28\bmod 31=28>2$).
  **CLOSED** (finite list of two, both disposed).
* (h) $(6,0)$, $T=10$, $h=1$: $P(-1)=\{1\}$, $P(5)=\{1,5\}$, so
  $\rho\in\{1,5\}$ and $n-1\in\{1,5,3,15\}$. With $n-1=6j-1$: $5$
  gives $j=1$, the rest no integer $j$. No admissible candidates.
  **CLOSED** outright.

Together with Claim I2.10, this reproduces and extends the
$(4,2)$-style analysis: the method's candidate lists on the
validation row and on rows (a), (c), (g) are finite and explicitly
disposed; on rows (b), (d), (e), (f), (h) the group products collapse
to $\rho=1$ or a two-element set and the row equation already
excludes every admissible $j$. $\square$

**Claim I2.12 (PROVED: the $R=1$ rows with $T\le 16$).** $R=1$ gives
$T=2Q-1\le 16$, so $Q\le 8$. If $Q$ is even, $n=Qj+1$ is odd for
every $j$: the row contains no even $n$ at all and is vacuous for
the even residual (and odd counterexamples are closed globally).
Let $Q$ be odd; then $n$ even forces $j$ odd. By Claim I2.9,
$n=2^a3^b$ with $b\le 1$, and at $t=2$ the group products are
$G_{2,1}\in P(Q-1)$, $G_{2,2}\in P(2Q-1)$.

* $(3,1)$, $T=5$, $h=1$ ($\Lambda_3(5)=15$, $V_3(n)\mid 15j$):
  $n=3j+1\equiv 1\pmod 3$ excludes $b=1$, so $n=2^a$.
  $P(2)=\{1\}$, $P(5)=\{1,5\}$, so $R(n-2)\in\{1,5\}$ and the odd
  part $M$ of $n-2$ lies in $\{1,5,3,15\}$. $a=1$ gives $n=2$;
  $a\ge 2$ gives $M=2^{a-1}-1\in\{1,3,15\}$ from the set
  ($M=5$ has no solution), i.e. $(a,n)=(2,4),(3,8),(5,32)$, with
  $j=(n-1)/3=1$, $7/3$, $31/3$: none admissible. No candidates.
  **CLOSED** outright.
* $(5,1)$, $T=9$, $h=1$: $P(4)=\{1\}$, $P(9)=\{1,9\}$, so
  $R(n-2)\in\{1,9\}$ and $M\in\{1,9,3\}$ (the value $27=3\cdot 9$ is
  excluded by the same $3\nmid\rho$ rule as in Claim I2.11(g)).
  $a=1$: $n\in\{2,6\}$, $j=(n-1)/5\le 1$. $a\ge 2$, $b=0$:
  $M=2^{a-1}-1\in\{1,3,9\}$ gives $a=2$ ($n=4$) or $a=3$ ($n=8$),
  neither with integer $j>3$. $a\ge 2$, $b=1$:
  $M=3\cdot2^{a-1}-1\in\{1,3,9\}$ needs
  $3\cdot2^{a-1}\in\{2,4,10\}$: none. No candidates. **CLOSED**
  outright.
* $(7,1)$, $T=13$, $h=1$: $P(6)=\{1\}$, $P(13)=\{1,13\}$, so
  $R(n-2)\in\{1,13\}$ and $M\in\{1,13,3,39\}$. $a=1$:
  $n\in\{2,6\}$, no admissible $j$. $a\ge 2$, $b=0$:
  $M=2^{a-1}-1\in\{1,3,13,39\}$ gives $a=2$ ($n=4$, $j=3/7$) or
  $a=3$ ($n=8$, $j=1$); $M=13,39$ need $2^{a-1}=14,40$: none.
  $a\ge 2$, $b=1$: $3\cdot2^{a-1}\in\{2,4,14,40\}$: none. No
  candidates. **CLOSED** outright.

Script §D confirms each row's group-product sets and $M$ sets and
cross-checks by direct clause tests (5, 4, and 3 integer-$j$ forms
tested for $Q=3,5,7$ respectively over a superset range of $a$; none
passes the $r=0$ and $r=2$ clauses simultaneously). $\square$

### 3.3 All remaining $R\ne 1$ rows with $T\le 16$

**Claim I2.13 (PROVED, computation: every $R\ne 1$ row with
$T\le 16$ is closed for even (LD3) solutions).** There are 57 such
rows. For each, Claim I2.8 bounds any even (LD3) solution by
$n\le 3|(R-1)(Q+R-1)|+1$ (the maximum bound is $586$, at $(2,14)$).
Script §C scans every even pair $(n,j)$ in each row with $j>3$ up to
its bound (1390 pairs in total), collects those passing the $r=1$
clause of (LD3) (a necessary condition, so the list is complete),
and disposes of each by a full (LD3) witness. The complete
$r=1$-candidate list across all 57 rows has exactly **20** pairs:
in row $(2,4)$: $(16,6)$; $(2,6)$: $(16,5),(22,8),(36,15),(106,50)$;
$(2,8)$: $(22,7),(64,28)$; $(2,10)$: $(34,12),(100,45)$; $(2,12)$:
$(34,11),(40,14),(144,66),(430,209)$; $(2,14)$:
$(40,13),(66,26),(196,91)$; $(3,12)$: $(78,22)$; $(4,6)$: $(46,10)$;
$(4,8)$: $(232,56)$; $(4,10)$: $(118,27)$. Every one fails (LD3) at
an explicit witness printed by the script (for example
$(430,209)$ fails at $q=5\parallel 430$, $r=0$; $(196,91)$ at
$q=49\parallel 196$, $r=0$; $(100,45)$ at $q=25\parallel 100$,
$r=0$). The other 47 rows have no $r=1$ candidate at all. Hence no
even (LD3) solution exists in any of these rows, for any $j$.
The hand closures of Claim I2.11 are the human-readable instances
of this computation on the specified rows, and their candidate
lists agree with the scan (script §E). $\square$

**Claim I2.14 (PROVED: all rows with $T\le 16$ are closed for the
even class).** Combining Claims I2.12 and I2.13 (57 rows with
$R\ne 1$, 7 rows with $R=1$, of which 4 are parity-vacuous and 3 are
closed analytically), plus the previously closed rows (which are
among these and are consistent): **there is no pair $(n,j)$ with
$n$ even and $3<j\le n/2$ satisfying (LD3) in any row with
$T\le 16$, and in particular no counterexample in any such row.**
This is a statement about (LD3) solutions themselves (stronger, in
this direction, than a counterexample statement: it needs no
EEES78 and no Proposition 4.1). $\square$

## 4. Task I.4: the even half of (H3) after this work

**Claim I2.15 (OPEN, exact statement).** Let
$(H3)_{\mathrm{even}}$ be the statement that (LD3) has no solution
$(n,j)$ with $n$ even and $3<j\le n/2$. After Claims I2.13 and
I2.14, $(H3)_{\mathrm{even}}$ is equivalent to its restriction to
rows with $T\ge 17$, and it remains **OPEN** there. In row
coordinates the surviving region is exactly: $Q=2$, $R\ge 15$;
$Q=3$, $R\ge 13$; $Q=4$, $R\ge 11$; $Q=5$, $R\ge 9$; $Q=6$, $R\ge 7$;
$Q=7$, $R\ge 5$; $Q=8$, $R\ge 3$; $Q=9$, $R\ge 1$; $Q\ge 10$, any
$R\ge 0$ (always with $R<j$, $n$ even, and, for counterexamples, the
full (RES-3) conditions of Claim I2.1 and $j\ge 5001$, $n>10^6$,
$v_2(C(n,3))\ge 4$). No argument in this file excludes that region.

*How (RES-3) shrank, itemised.* (RES-3) as reconciled in Claim I2.1
contains 59 rows with $T\le 16$ (the 64 rows of Claim I2.5 minus the
5 rows already closed before this cycle, listed in condition (b)).
(1) By I.2 (Claim I2.6), for **counterexamples**, 50 of those 59
rows are removed: the 42 $h=0$ rows and the 8 $h=1$ rows with
$B^{*}\le 5000$ other than the already closed ones. This removal
uses EEES78 through the squared half and the certified $j\ge 5001$
frontier, and applies only to counterexamples, not to bare (LD3)
solutions. (2) By I.3 (Claims I2.11–I2.14), for **(LD3) solutions
and counterexamples alike**, all 59 rows are removed; the 9 rows
whose removal is genuinely new at this step are exactly the $h=1$
rows with $B^{*}>5000$: $(6,1)$ and $(8,1)$ (parity-vacuous for even
$n$), $(7,1)$ (Claim I2.12), and $(6,2),(7,0),(7,2),(8,0),(8,2),
(9,0)$ (Claims I2.8 and I2.13, with no $r=1$ candidates in any of
them). (3) Additionally, though it removes no row by itself, §2
establishes that every $h\le 1$ row whatsoever contains only
finitely many counterexample candidates ($j<B^{*}$), and §3
establishes the same finiteness for (LD3) solutions in every fixed
row (Claims I2.8, I2.9). The obstruction is now precisely the
infinitude of rows with $T\ge 17$, in each of which the finite lists
grow with $(Q,R)$ and have not been disposed uniformly. $\square$

**Claim I2.16 (what is not proved: OPEN).** (H3) in full remains
open: its even half is Claim I2.15, and its odd half, as a statement
about (LD3) alone, is also not proved in general (odd
**counterexamples** are excluded by Proposition 4.1 via SPLIT-odd,
but that argument assumes the counterexample condition
$\gcd(V_3(n),C(n,j))=1$, which is stronger than (LD3); the pinned
odd (LD3) family is excluded computationally to $n\le 10^6$ and by
nothing in this file beyond that). $i=3$ in general is not closed,
and #699 is not claimed solved. $\square$

## 5. Closing statement

*Proved in this file, beyond the Cycle 2 record:*
1. (RES-3), the single reconciled residual statement for even
   $i=3$ counterexamples, with the five F1.11/F2.14 discrepancies
   (D1)–(D5) resolved explicitly (Claim I2.1).
2. Per-row finiteness for counterexamples in every $h\le 1$ row,
   with explicit closed-form bounds and exact thresholds
   $B^{*}(Q,R)$ for all 64 rows with $T\le 16$; the $h=2$ row is a
   proved exception to the finiteness statement (Claims
   I2.2–I2.5).
3. The elimination lemma (Claim I2.7) and its corollaries: (LD3)
   alone bounds every fixed row explicitly (Claims I2.8, I2.9).
4. Every row with $T\le 16$ is closed for even (LD3) solutions and
   hence for even counterexamples (Claims I2.10–I2.14), with
   hand proofs for the validation row $(4,2)$ and for rows
   $(2,4)$, $(3,4)$, $(2,6)$, $(4,4)$, $(5,0)$, $(5,2)$, $(2,8)$,
   $(6,0)$, $(3,1)$, $(5,1)$, $(7,1)$.

*Reduced:* a counterexample at $i=3$ must now lie in (RES-3) with
$T\ge 17$ (Claim I2.15); $(H3)_{\mathrm{even}}$ is reduced to the
same region.

*Still OPEN, explicitly:* $(H3)_{\mathrm{even}}$ for $T\ge 17$;
(H3) in full; $i=3$ in general; #699. An honest EXACT RESIDUAL is
the outcome for the $T\ge 17$ region: it is the precise
sub-configuration of (RES-3) stated in Claim I2.15, not excluded by
any argument here.

## 6. Verification log

All numbers above are outputs of `proofs/P-I2_checks.py` (about
0.1 s, stdlib only, exact arithmetic), whose sections assert their
own headline values:

* §A: $\Lambda_3(T)$ for $T\le 16$; the 64 rows with $T\le 16$;
  $J_{\max}$ and $B^{*}=J_{\max}+1$ for the 63 rows with $h\le 1$,
  with endpoint assertions for every row; the counts 42/21/1 for
  $h=0/1/2$; every $h=0$ row has $B^{*}\le 5000$; the $h=1$
  $B^{*}\le 5000$ list (12 rows) and $B^{*}>5000$ list (9 rows)
  exactly as in Claim I2.5.
* §B: the $(4,2)$ validation: candidates exactly
  $(22,5),(46,11),(106,26)$; gcds exactly $77,69,371$; (LD3)
  witnesses $(r,q)=(0,11),(0,23),(0,53)$.
* §C: the 57 rows with $R\ne 1$, $T\le 16$: 1390 even pairs tested
  up to the per-row Claim I2.8 bounds (maximum bound $586$ at
  $(2,14)$); exactly 20 $r=1$-clause candidates, each printed with
  its full (LD3) witness; 0 survivors.
* §E: the hand-analysed rows of Claim I2.11: candidate lists
  $(2,4)$: $[(16,6)]$; $(2,6)$: $[(16,5),(22,8),(36,15),(106,50)]$;
  $(3,4),(4,4),(5,0),(5,2),(6,0)$: $[]$; $(2,8)$: $[(22,7),(64,28)]$,
  matching the text.
* §D: the $R=1$ rows $Q=3,5,7$: group-product sets
  $P(Q-1)=\{1\}$ in all three cases; $P(2Q-1)=\{1,5\},\{1,9\},
  \{1,13\}$; $R(n-2)$ sets $\{1,5\},\{1,9\},\{1,13\}$; odd-part sets
  $\{1,3,5,15\},\{1,3,9\},\{1,3,13,39\}$; analytic candidates none;
  clause cross-checks tested 5, 4, 3 integer-$j$ forms with 0
  passing the $r=0$ and $r=2$ clauses.
