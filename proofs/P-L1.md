# Prover L1 (independent): Cluster L, the higher-digit Kummer refinement (LD3+) at $i=3$, Cycle 3

Prover: L1, working independently in Cycle 3. Sources read: `CYCLE2.md`
§2; `proofs/P-A1.md` §§4–5 in full (Lemma A1.15, the (LD3) Definition,
Proposition A1.16, Statement (H3), Theorem A1.17) and the corresponding
material of `proofs/P-A2.md` (§§4.2–4.3, Lemma A2.21, Definition A2.22,
Corollary A2.23, Statement A2.27); `proofs/P-F1.md` (especially Claim
F1.6(c), the recorded gap this cluster addresses, and Claims F1.9–F1.11);
`proofs/P-F2.md` §§1–3 (Theorem F2.3, Corollary F2.4, Theorem F2.9,
Proposition F2.13, Claim F2.14); `verification/V-A.md` and
`verification/V-F.md` for what is certified. `proofs/P-L2.md` was **not**
read or looked for: the two Cluster L provers work independently.
Every computation below is in `proofs/P-L1_checks.py` (Python standard
library only, exact integer arithmetic, no randomness; total runtime
30.5 seconds on this machine, of which §D is about 29 seconds). Every
numbered claim is labelled PROVED, GAP, FALSE, OPEN, or COMPUTATION.

**Headline.** The full digitwise refinement (LD3+) is formulated exactly
(§1). Its new content is located precisely: on digits $0,\dots,a-1$ the
digitwise condition at a relevant prime power $q=p^a$ is **exactly**
(LD3)'s clause $j \bmod q \le r$, neither weaker nor stronger (Lemma
L1.2, proved, and checked on 1,101,758 instances); everything new in
(LD3+) sits at digits $\ge a$, in the single quotient condition
$\lfloor j/q \rfloor$ digitwise $\le (n-r)/q$ in base $p$ (Definition
L1.3). At $p=3$ the higher-digit conditions are derived in all three
cases (Theorem L2.1), but on every concrete family tested they add
nothing: for the near-miss family $n=3^a+1$, $j=n/2$ the $p=3$
higher-digit subcondition **passes** for all $a$ (Claim L2.3, proved),
so that family's exclusion remains the low $3$-clause alone, exactly as
in Cycle 1. Computationally (LD3+) is genuinely stronger than the low
system on subsystems: of the exactly 12 solutions of the $\ge5$-only
(LD3) system with $n \le 10^6$ (Computation L2.5, a new enumeration),
8 are excluded by $\ge5$ higher digits alone, without the $3$-clause.
But inside the residual class no shrinkage is proved and none is
exhibited: in every $h=0$ row class enumerated to $n \le 10^8$ (and, by
the bound of Lemma L3.1, exhaustively for all $n$ in those rows), the
Proposition 4.1 filter $V_3(n) \mid \Lambda_3(T)$ leaves only 23
candidates in total and (LD3) already kills all 23, so the (LD3+) stage
is never reached (Computation L3.2). §4 gives the exact logical
relation between (H3), (H3+), and closing $i=3$, including one
correction to the brief's framing (Claim L4.1(c): under the full
definition, a solution of (LD3+) **is** a counterexample, so (H3+) is
equivalent to $i=3$ being closed, and it is (H3), not (H3+), that is
the potentially stronger auxiliary statement). **Verdict: option (b)**
of the brief: (LD3+) is computationally stronger but no general
shrinkage of the residual class is proved; §4.2 states the exact point
where the proof attempt stops. $i=3$ is **not** closed, (H3) and (H3+)
are **not** proved, and #699 is **not** claimed solved.

## 0. Standing inputs and notation

$C(n,k)=\binom nk$; $V_3(n)$ is the odd part of $C(n,3)$; a
**counterexample** is a triple $(n,3,j)$, $3<j\le n/2$, with
$\gcd(V_3(n),C(n,j))=1$. Used as certified ground truth (per CYCLE2.md
and V-F): (LD3) and its necessity (A1.15/A1.16(i)); (N1), (N2)
($V_3(n)\mid C(j,3)$); Price Proposition 4.1 at $i=3$ with the per-part
dichotomy (F1.9/F2.9: a genuine split part at $p\ge5$ is $\le
T:=R+2(Q-1)$, where $n=Qj+R$); SPLIT-odd closed ($n$ odd impossible);
rows $(Q,R)\in\{(2,0),(2,2),(3,0),(3,2),(4,0)\}$ closed;
$v_2(C(n,3))\ge4$ necessary; (LD3) has no solution with $n\le10^6$;
every pair $(3,j)$ with $j\le5000$ is closed for all $n$. The residual
class is F1.11/F2.14 intersected with these: $n$ even, $j\ge5001$,
$n>10^6$, $(Q,R)$ outside the closed list, satisfying (LD3), (N1),
(N2), and the $T$-boundedness/label conditions. For a prime $p$ and
$x\ge0$, $\mathrm{dig}_k(x,p)$ is the $k$-th base-$p$ digit of $x$
(digits beyond the length are $0$), and $x \preceq_p y$ means
$\mathrm{dig}_k(x,p)\le\mathrm{dig}_k(y,p)$ for all $k\ge0$. Kummer's
theorem: $p\nmid C(n,j)$ iff $j\preceq_p n$.

For the rest of the file, fix a counterexample candidate $(n,3,j)$ and
a prime $p\ge3$ dividing a top number. Since two of $n,n-1,n-2$ differ
by at most $2<p$ unless $p=3$ (and for $p=3$ exactly one of them is
divisible by $3$), there is a unique $r=r(p)\in\{0,1,2\}$ with
$p\mid n-r$. Write $a=a(p)=v_p(n-r)\ge1$, $q=q(p)=p^a$, and
$U=U(p)=(n-r)/q$, so $p\nmid U$.

## 1. Task L.1: the system (LD3+), stated exactly

**Lemma L1.1 (support characterisation; PROVED).** For a prime
$p\ge3$, $p\mid C(n,3)$ if and only if $p$ divides a top number and
($p\ge5$, any $a\ge1$) or ($p=3$ and $a\ge2$). In that case
$v_p(C(n,3))=a$ for $p\ge5$, and $v_3(C(n,3))=a-1$ for $p=3$.

*Proof.* $6C(n,3)=n(n-1)(n-2)$. For $p\ge5$, $p\nmid6$ and $p$ divides
exactly one top factor, so $v_p(C(n,3))=v_p$ of the product $=a$. For
$p=3$, exactly one top factor is divisible by $3$; $v_3$ of the product
is its valuation $a\ge1$, and $v_3(C(n,3))=a-v_3(6)=a-1$, which is
$\ge1$ iff $a\ge2$. If $p\ge3$ divides no top number then $p$ does not
divide the product; for $p\ge5$, $p\mid C(n,3)$ would give $p\mid
6C(n,3)$, the product, a contradiction; for $p=3$ some top number is
always divisible by $3$, so the case is empty. $\square$

*Remark.* Lemma L1.1 confirms the brief's parenthetical in L.2: the
case $v_3(\text{top})=1$ is correctly ignored by (LD3) at the digit
level, because then $3\nmid C(n,3)$, i.e. $3$ is not a prime of
$V_3(n)$ and a counterexample imposes no condition at $3$ at all. It
also confirms L.1(iii): a prime $p\ge3$ dividing **no** top number
never divides $C(n,3)$, so it is irrelevant to $\gcd(V_3(n),C(n,j))$,
and (LD3+) imposes no condition at such $p$.

**Lemma L1.2 (the low digits are exactly (LD3); PROVED).** Let
$q=p^a\Vert(n-r)$ with $p\ge5$ (any $a\ge1$) or $p=3$, $a\ge2$. Then:

(i) $n\bmod q=r$, and the base-$p$ digits of $n$ at positions
$0,\dots,a-1$ are $(r,0,\dots,0)$.

(ii) The digitwise condition on digits $0,\dots,a-1$,
$\mathrm{dig}_k(j,p)\le\mathrm{dig}_k(n,p)$ for $0\le k<a$, holds if
and only if $j\bmod q\le r$. In particular (LD3)'s clause at $q$
already encodes the vanishing of $j$'s digits $1,\dots,a-1$: the
digitwise condition on the lowest $a$ digits is **neither stronger nor
weaker** than $j\bmod q\le r$.

*Proof.* (i) $q\mid n-r$ and $0\le r\le2<q$ (since $q\ge3$ and $r\le2$,
with $r<3\le q$), so $n\bmod q=r$. Since $r<p$, the base-$p$ expansion
of the residue $r$, padded to $a$ digits, is digit $0$ equal to $r$ and
digits $1,\dots,a-1$ equal to $0$; these are $n$'s lowest $a$ digits
because $n\equiv r\pmod{p^a}$.

(ii) The lowest $a$ digits of $j$ are the base-$p$ digits of
$t:=j\bmod q$. If the digitwise condition holds, then by (i)
$\mathrm{dig}_0(j,p)\le r$ and $\mathrm{dig}_k(j,p)=0$ for
$1\le k<a$, so $t=\mathrm{dig}_0(j,p)\le r$. Conversely, if $t\le r$
then $t<p$ (as $r<p$), so the base-$p$ expansion of $t$ is the single
digit $t$ followed by zeros; hence $\mathrm{dig}_0(j,p)=t\le r$ and
$\mathrm{dig}_k(j,p)=0=\mathrm{dig}_k(n,p)$ for $1\le k<a$. The two
conditions are equivalent. (Checked computationally in script §A2:
1,101,758 instances $(n,j,q)$ with $n\le1000$, zero failures; the
assertion $n\bmod q=r$ was also asserted for every relevant $q$ in
that range.) $\square$

*Consequence for L.1(ii) of the brief.* The suspicion that digitwise on
digits $0,\dots,a-1$ might be strictly stronger than $j\bmod q\le r$
(in forcing $j$'s digits $1,\dots,a-1$ to vanish separately) is
resolved in the negative: the single congruence already forces the
vanishing, because its bound $r$ is smaller than $p$. **All** of
(LD3+)'s content beyond (LD3) is at digits $\ge a$.

**Definition L1.3 ((LD3+); the full digitwise refinement).** The pair
$(n,j)$, $3<j\le n/2$, **satisfies (LD3+)** if for every prime
$p\ge3$ dividing $C(n,3)$ (equivalently: every $p$ of Lemma L1.1),
$$j\ \preceq_p\ n\qquad\text{in base }p,$$
i.e. $p\nmid C(n,j)$. Split at the position $a=a(p)$, with $r,q,U$ as
in §0, this is the conjunction of:

($\alpha$) the **low condition** $j\bmod q\le r$, which by Lemma L1.2
is exactly the (LD3) clause at $q$ (for $p\ge5$ every $a\ge1$; for
$p=3$ exactly when $a\ge2$); and

($\beta$) the **high condition**
$\lfloor j/q\rfloor\ \preceq_p\ U$, i.e. for every $t\ge0$,
$\mathrm{dig}_t(\lfloor j/q\rfloor,p)\le\mathrm{dig}_t(U,p)$.

The equivalence of the split with the full condition is the following
digit bookkeeping. Since $n=qU+r$ with $0\le r<q=p^a$,
$\lfloor n/q\rfloor=U$, so $\mathrm{dig}_{a+t}(n,p)=
\mathrm{dig}_t(U,p)$ for all $t\ge0$, and likewise
$\mathrm{dig}_{a+t}(j,p)=\mathrm{dig}_t(\lfloor j/q\rfloor,p)$. Hence
digits $\ge a$ of the comparison $j\preceq_p n$ are exactly ($\beta$),
and digits $<a$ are exactly ($\alpha$) by Lemma L1.2. Two features of
($\beta$) deserve emphasis:

* **Digit $a$ itself.** $\mathrm{dig}_a(n,p)=U\bmod p$, and this is
  **nonzero**: $p\nmid U$ by the definition of $a$ as the exact
  valuation. The condition at digit $a$ is
  $\lfloor j/q\rfloor\bmod p\ \le\ U\bmod p\in\{1,\dots,p-1\}$.
* **First-power primes are the extreme case.** If $a=1$ (in
  particular every prime $p\ge5$ dividing a top number to the first
  power only, which is the typical situation in the $h=0$ rows of §3),
  then (LD3) sees only digit $0$, and ($\beta$) with $q=p$,
  $U=(n-r)/p$ is **entirely** new content: it constrains
  $\lfloor j/p\rfloor\bmod p\le\lfloor n/p\rfloor\bmod p$, then
  $\lfloor j/p^2\rfloor\bmod p\le\lfloor n/p^2\rfloor\bmod p$, and so
  on through all higher digits.

**Theorem L1.4 (necessity, and (LD3+) $\Rightarrow$ (LD3); PROVED).**
(a) If $(n,3,j)$ is a counterexample, then $(n,j)$ satisfies (LD3+).
(b) If $(n,j)$ satisfies (LD3+), then $(n,j)$ satisfies (LD3).

*Proof.* (a) A counterexample has $\gcd(V_3(n),C(n,j))=1$; by Lemma
L1.1 the primes of $V_3(n)$ are exactly the primes in Definition
L1.3, so for each of them $p\nmid C(n,j)$, and Kummer's theorem gives
$j\preceq_p n$. (b) For each relevant $q$ of (LD3), its prime $p$
divides $C(n,3)$ (Lemma L1.1: for $p\ge5$ relevant means $p$ divides a
top; for $p=3$ relevant means $a\ge2$), so ($\alpha$) of Definition
L1.3 applies and gives $j\bmod q\le r$, which is the (LD3) clause.
$\square$

**Claim L1.5 (strictness: local PROVED, global OPEN).** (a) As a
per-prime predicate, ($\beta$) is strictly stronger than ($\alpha$)
(COMPUTATION, script §F): at $(n,j,p)=(30,15,5)$, the prime power is
$q=5\Vert n$ ($a=1$, $r=0$); the low condition holds,
$15\bmod5=0\le0$, but the full digitwise condition fails at digit 1:
$30=(0,1,1)_5$ and $15=(0,3,0)_5$, with
$\lfloor15/5\rfloor\bmod5=3>1=\lfloor30/5\rfloor\bmod5$. (The pair
$(30,15)$ is not an (LD3) solution: other primes' clauses fail. The
example is a statement about the predicate at one prime.) The high
condition is also not determined by the low data: at the same
$(n,p)=(30,5)$, $j=5$ satisfies both ($\alpha$) and ($\beta$)
($5=(0,1)_5\preceq_5 30$) while $j=15$ satisfies ($\alpha$) and fails
($\beta$). (b) Whether the two **systems** differ extensionally, i.e.
whether $\mathrm{Sol}(\mathrm{LD3})\setminus
\mathrm{Sol}(\mathrm{LD3+})$ is nonempty, is **OPEN**: it is exactly
the question whether (LD3) has a solution that is not a
counterexample (see Claim L4.1), and no (LD3) solution is known at any
$n$ (certified: none with $n\le10^6$).

## 2. Task L.2: the $p=3$ digits

Let $r_3\in\{0,1,2\}$ be the unique offset with $3\mid n-r_3$ and
$a_3=v_3(n-r_3)\ge1$ (exactly one of three consecutive integers is
divisible by $3$).

**Theorem L2.1 (the $p=3$ conditions, explicit; PROVED).**
$3\mid C(n,3)$ iff $a_3\ge2$ (Lemma L1.1). In that case a
counterexample requires $3\nmid C(n,j)$, i.e. $j\preceq_3 n$, which
splits (Definition L1.3 at $p=3$) into the low clause
$j\bmod 3^{a_3}\le r_3$ (the $3$-clause of (LD3)) and the high
condition $\lfloor j/3^{a_3}\rfloor\preceq_3 U_3$ with
$U_3=(n-r_3)/3^{a_3}$, $3\nmid U_3$. By the value of $r_3$:

* **$v_3(n)\ge2$** ($r_3=0$): low clause is $j\bmod 3^{a_3}=0$, i.e.
  $3^{a_3}\mid j$; high condition
  $\lfloor j/3^{a_3}\rfloor\preceq_3 n/3^{a_3}$.
* **$v_3(n-1)\ge2$** ($r_3=1$): low clause is
  $j\bmod 3^{a_3}\in\{0,1\}$; high condition
  $\lfloor j/3^{a_3}\rfloor\preceq_3 (n-1)/3^{a_3}$.
* **$v_3(n-2)\ge2$** ($r_3=2$): low clause is
  $j\bmod 3^{a_3}\in\{0,1,2\}$; high condition
  $\lfloor j/3^{a_3}\rfloor\preceq_3 (n-2)/3^{a_3}$.

In each case the digit at position $a_3$ of $n$ is $U_3\bmod3\in
\{1,2\}$. If $a_3=1$ there is **no** condition at $3$ in (LD3) or in
(LD3+), correctly, since then $3\nmid C(n,3)$.

*Proof.* This is Definition L1.3 and Lemma L1.2 specialised to $p=3$,
with the three cases being $r_3=0,1,2$. $\square$

*Intersection with the residual class (remark).* The residual class
has $n$ even, which excludes none of the three cases ($9\mid n$,
$9\mid n-1$, $9\mid n-2$ are each compatible with $n$ even), and it
has $j\ge5001$, so $\lfloor j/3^{a_3}\rfloor$ is typically $\ge1$: the
high condition at $3$ is **not vacuous** in the residual class. It is
simply not controlled by any certified input (see Claim L4.2).

**Claim L2.2 ($v_3(\mathrm{top})=1$: no digit content; PROVED).** If
$a_3=1$ then $v_3(C(n,3))=0$, and whether $3\mid C(n,j)$ or not is
irrelevant to $\gcd(V_3(n),C(n,j))$. (LD3)'s omission of this case is
correct, and (LD3+) adds nothing there. $\square$ (Lemma L1.1.)

**Claim L2.3 (the family $n=3^a+1$, $j=n/2$: the $p=3$ high condition
gives no independent exclusion; PROVED for the high condition, and
COMPUTATION for the $\ge5$ part).** Let $a\ge2$, $n=3^a+1$, $j=n/2$.
The $3$-divisible top is $n-1=3^a$, so $r_3=1$, $a_3=a$, $U_3=1$.

(i) The low $3$-clause fails: $j\bmod 3^a=j=(3^a+1)/2>1$. This is the
Cycle 1 exclusion of the family.

(ii) The high $3$-condition **passes**, for every $a\ge2$:
$\lfloor j/3^a\rfloor=0$ (since $j=(3^a+1)/2<3^a$), and
$0\preceq_3 1=U_3$ trivially; digit $a$ of $j$ is $0\le1=$ digit $a$
of $n$, and all higher digits of both are $0$.

Hence (LD3+) at $p=3$ excludes this family **only through the same low
clause as (LD3)**; the higher digits contribute nothing here, neither
independently nor as a strengthening. (COMPUTATION, script §§C, D:
the $\ge5$ part of (LD3) holds for this family for all $2\le a\le12$
($n\le531{,}442$), so within that range the family's status is exactly
as in P-A1's calibration list, extended from $a\le6$ to $a\le12$.)
$\square$

**Claim L2.4 (the shapes $n=3^a-1$ and $n=2\cdot3^a+1$ at $p=3$;
PROVED, with COMPUTATION for the excluding witness).**
(a) $n=3^a-1$ ($a\ge2$), $j=n/2$: the $3$-divisible top is
$n-2=3^a-3=3(3^{a-1}-1)$, and $v_3(n-2)=1$ for all $a\ge2$, because
$3^{a-1}-1\equiv-1\pmod3$ (for $a=2$ it is $2$). Hence $a_3=1$,
$3\nmid C(n,3)$, and **there is no $p=3$ condition in (LD3) or
(LD3+) at all for this shape**; its exclusions, where they occur,
must come from $p\ge5$. (COMPUTATION, script §C: for $2\le a\le8$ the
full (LD3) fails at a $\ge5$ witness, e.g. $q=25\Vert n-1$ at $a=3$,
$q=79\Vert n-1$ at $a=4$.)
(b) $n=2\cdot3^a+1$ ($a\ge2$) with $j=3^a=(n-1)/2$: the $3$-divisible
top is $n-1=2\cdot3^a$, so $r_3=1$, $a_3=a$, $U_3=2$. The low
$3$-clause **passes** ($j\bmod 3^a=0\le1$) and the high $3$-condition
also **passes** for all $a$: $\lfloor j/3^a\rfloor=1\preceq_3 2=U_3$
(digit $a$: $1\le2$; above: $0\le0$). So (LD3+) at $p=3$ does not
exclude this shape either. (Its (LD3) exclusion, in the computed
range $2\le a\le8$, is at the $r=0$ clause from a $\ge5$ prime power
of $n$ itself, script §C; and as a counterexample shape it is in any
case impossible for a different reason: $n$ is odd, and an odd-$n$
counterexample is pinned to $j=n/3\ne(n-1)/2$ by A1.16(iv), besides
being closed outright by F1.5/F2.7.) $\square$

**Computation L2.5 (the $\ge5$-only system to $10^6$; the calibration
of the digit machinery; COMPUTATION, script §§B, D).** The
$\ge5$-only (LD3) system (the (LD3) clauses at $p\ge5$ only) has
**exactly 12 solutions with $n\le10^6$** (26,035,963 candidate pairs
tested by the $R_5(n)$-multiple enumeration over an SPF sieve):
$$(10,5),(28,14),(82,41),(162,70),(244,122),(730,365),(2188,1094),
(6562,3281),(19684,9842),(59050,29525),(177148,88574),(531442,265721),$$
i.e. the family $n=3^a+1$, $j=n/2$ for $2\le a\le12$, plus the single
sporadic $(162,70)$. The first six are exactly P-A1's list for
$n\le2000$, so the machinery reproduces the certified calibration.
Classification of the 12 by the digit machinery:

* all 12 **fail the $p=3$ low clause** (as they must: a $\ge5$
  solution passing it would be a full (LD3) solution, and none exists
  with $n\le10^6$);
* all 12 **pass the $p=3$ high subcondition** (for the family and for
  $(162,70)$ alike, $\lfloor j/3^{a_3}\rfloor=0$);
* **8 of the 12 are excluded by $\ge5$ higher digits alone**, i.e.
  some $p\ge5$ in the support of $C(n,3)$ fails the full digitwise
  condition although all its low clauses pass: $(82,41)$ at $p=5$;
  $(162,70)$ at $p=5,7$; $(730,365)$ at $p=5$; $(6562,3281)$ at
  $p=17,41$; $(19684,9842)$ at $p=7$; $(59050,29525)$ at $p=5,61$;
  $(177148,88574)$ at $p=67$; $(531442,265721)$ at $p=5,7,13,41,73$.
  For the remaining 4, $(10,5)$, $(28,14)$, $(244,122)$, $(2188,1094)$,
  (LD3+)'s exclusion rests solely on the $p=3$ **low** clause, the
  same clause (LD3) already has.

So (LD3+) is a strictly stronger filter than (LD3) on the $\ge5$
subsystem within this range, in the concrete sense that it kills 8 of
that subsystem's 12 solutions without using the $3$-clause at all.
But every one of the 12 was already killed by (LD3) in full (via the
$3$-clause), so this is a second, independent exclusion channel for
pairs that were not (LD3) solutions in the first place. It is **not**
an instance of (LD3+) excluding an (LD3) solution. $\square$

## 3. Task L.3: does (LD3+) bite in the residual class? The thin $h=0$ rows

Throughout this section $(Q,R)$ is a row with $R\ge3$, so $h=0$ and
Proposition 4.1 (F2.3/F2.13) gives, for any counterexample in the row,
$$V_3(n)\ \Big|\ \Lambda_3(T),\qquad T=R+2(Q-1).$$
The **class** of the row is the set of pairs $(n,j)$ with $n=Qj+R$,
$j>3$, satisfying $V_3(n)\mid\Lambda_3(T)$: a necessary condition for a
counterexample in the row, before (LD3) is consulted.

**Lemma L3.1 (the odd-top bound in $h=0$ rows; PROVED).** Let
$(n,3,j)$ be a counterexample in an $h=0$ row, with $n$ **even**.
Then $n-1\mid 3\Lambda_3(T)$, in particular $n\le 3\Lambda_3(T)+1$.

*Proof.* $n-1$ is odd. For each prime $p\ge5$ with $p^a\Vert n-1$,
$p^a$ is exactly the $p$-part of $V_3(n)$ (unique top, $p\nmid6$), so
$p^a\mid V_3(n)\mid\Lambda_3(T)$. For $p=3$: if $3\nmid n-1$ there is
nothing; if $3^b\Vert n-1$ with $b\ge1$, then $n-1$ is the unique
$3$-divisible top, the $3$-part of $V_3(n)$ is $3^{b-1}$, so
$3^{b-1}\mid\Lambda_3(T)$ and $3^b\mid3\Lambda_3(T)$. The prime-power
factors of $n-1$ are pairwise coprime and each divides the
corresponding part of $3\Lambda_3(T)$, so $n-1\mid3\Lambda_3(T)$.
$\square$

*Remarks.* (i) The same argument applied to $n$ itself shows that the
odd part of $n$ divides $3\Lambda_3(T)$ (for $p\ge5$ its $p$-part
divides $\Lambda_3(T)$'s; for $3$ it is $3^b$ with
$3^{b-1}\mid\Lambda_3(T)$ or $b=0$). This is what makes the
enumeration below a parametrisation rather than a scan: every class
member has $n=o\cdot2^s$ with $o$ an odd divisor of $3\Lambda_3(T)$,
a finite set of size $6$ for $T=6$, $12$ for $T\in\{7,8\}$, $128$ for
$T=18$, $256$ for $T\in\{19,20\}$. (ii) For $n$ odd members of a row
there is no such bound from $n-1$ (which is then even), but all
odd-$n$ triples are closed globally by F1.5/F2.7. (iii) Lemma L3.1
makes the enumerations of the rows below **exhaustive for all $n$**,
not only for $n\le10^8$: in each row tested, $3\Lambda_3(T)+1\le
43{,}648{,}606<10^8$, so every even class member lies below the
enumeration cap, and every odd class member is closed by the standing
SPLIT-odd result. The lemma is a Proposition 4.1 consequence, not an
(LD3+) consequence, and (as noted in Claim L3.3) the disposals it
enables here are in fact already subsumed by the certified per-pair
frontier.

**Computation L3.2 (the row classes; COMPUTATION, script §E).** For
each row, the class was enumerated to $n\le10^8$ by the odd-part
parametrisation of Lemma L3.1(i) (never by scanning all $n$), then
filtered by $V_3(n)\mid\Lambda_3(T)$, then by (LD3), then by (LD3+).
The main row of the brief is the first line: $(Q,R)=(2,4)$, $T=6$,
$\Lambda_3(6)=15$ (F2.13's class: each top is $2^a3^b u$ with the
total $\ge5$ part dividing $15$).

| row $(Q,R)$ | $T$ | $\Lambda_3(T)$ | odd parts | candidate $n$ | in-row | pass $V\mid\Lambda$ | pass (LD3) | pass (LD3+) |
|---|---|---|---|---|---|---|---|---|
| $(2,4)$ | 6 | 15 | 6 | 146 | 135 | **0** | 0 | 0 |
| $(2,3)$ | 5 | 15 | 6 | 146 | 2 | 0 | 0 | 0 |
| $(2,5)$ | 7 | 105 | 12 | 275 | 7 | 0 | 0 | 0 |
| $(3,3)$ | 7 | 105 | 12 | 275 | 173 | 0 | 0 | 0 |
| $(2,6)$ | 8 | 105 | 12 | 275 | 257 | 1: $(16,5)$ | 0 | 0 |
| $(3,4)$ | 8 | 105 | 12 | 275 | 45 | 1: $(16,4)$ | 0 | 0 |
| $(2,16)$ | 18 | 765765 | 128 | 2113 | 1974 | 5 | 0 | 0 |
| $(2,17)$ | 19 | 14549535 | 256 | 3683 | 245 | 3 | 0 | 0 |
| $(2,18)$ | 20 | 14549535 | 256 | 3683 | 3415 | 9 | 0 | 0 |
| $(3,16)$ | 20 | 14549535 | 256 | 3683 | 529 | 4 | 0 | 0 |

Details: the $(2,16)$ passers are $(28,6),(34,9),(36,10),(56,20),
(66,25)$; the $(2,17)$ passers are $(35,9),(57,20),(65,24)$ (all with
$n$ odd, hence also closed by SPLIT-odd); the $(2,18)$ passers are
$(28,5),(34,8),(36,9),(40,11),(56,19),(66,24),(78,30),(154,68),
(210,96)$; the $(3,16)$ passers are $(28,4),(34,6),(40,8),(154,46)$.
**In the main row $(2,4)$ the Proposition 4.1 filter already leaves
zero candidates with $j>3$, before (LD3) is consulted** (the row's
only $V_3(n)\mid15$ members at any $n$ are $(6,1)$ and $(10,3)$, both
with $j\le3$, outside the counterexample domain; the bound of Lemma
L3.1 is $n\le46$, so this is exhaustive, not a range effect). In every row, **all 23
$V$-passers in total are killed by (LD3)** (e.g. $(16,5)$ fails at
$q=7\Vert n-2$, $5\bmod7=5>2$), so the (LD3+) stage has **zero**
candidates to act on in every row tested. Per the brief's instruction
the next thinnest classes were therefore also run: the remaining
$h=0$ rows with $T\le8$ (the table's first six lines), the
$(4,2)$-style $h=1$ row (Claim L3.3), and, to reach classes whose
bound $3\Lambda_3(T)+1$ exceeds the certified $n\le10^6$ frontier,
the rows with $T\in\{18,19,20\}$ (last four lines). The answer is the
same in all of them. $\square$

**Claim L3.3 (the $(4,2)$ row, and the status of these disposals;
PROVED as a summary of certified inputs and Computation L3.2).** For
the $h=1$ row $(Q,R)=(4,2)$ ($T=8$, $\Lambda_3(8)=105$), the F1.9(b) /
F1.11 finite analysis leaves exactly $(22,5),(46,11),(106,26)$, and
(script §E2, reproducing V-F §5) all three fail (LD3), with
$\gcd(V_3(n),C(n,j))=77,69,371$. No (LD3+) input is needed or used.
More broadly, none of the row disposals in this section is new
against the full certified record: every $V$-passer found in any row
has $j\le96$, so all of them lie inside F2.18's per-pair frontier
($j\le5000$ closed for all $n$), and the odd ones are also inside
SPLIT-odd. The rows' value here is diagnostic, not closural: the
thinnest classes the label bounds leave open are classes where the
higher-digit conditions are **never reached**, because the low-digit
system, and usually the Proposition 4.1 size filter before it, is
already empty there. $\square$

## 4. Task L.4: verdict on (H3)

**Definition (H3+).** $(\mathrm{H3}^+)$ is the statement that (LD3+)
has no solution $(n,j)$ with $3<j\le n/2$.

**Claim L4.1 (the exact logical relations; PROVED, with one correction
to the brief).**
(a) $\mathrm{Sol}(\mathrm{LD3+})$ is **exactly** the set of
counterexamples $(n,3,j)$ in the domain $3<j\le n/2$.
(b) Consequently $(\mathrm{H3}^+)$ holds if and only if $i=3$ has no
counterexample: **(H3+) $\iff$ ($i=3$ closed)**.
(c) The brief's parenthetical that a solution of (LD3+) "is not a
counterexample" is **FALSE** for the full system of Definition L1.3
(it is true for (LD3), and for any truncation of (LD3+), but not for
(LD3+) itself). The correct relation between the two statements is:
$(\mathrm{H3})\Rightarrow(\mathrm{H3}^+)$, since
$\mathrm{Sol}(\mathrm{LD3+})\subseteq\mathrm{Sol}(\mathrm{LD3})$ by
Theorem L1.4(b); and $(\mathrm{H3}^+)\Rightarrow(\mathrm{H3})$ is
**OPEN** (it would follow from, and in the relevant sense is
equivalent to, (LD3) having no solution that fails a higher digit;
compare Claim L1.5(b)). So (H3) is a **sufficient but potentially
strictly stronger** route to closing $i=3$: (H3) could fail while
$i=3$ still holds.
(d) Neither (N1) nor (N2) is used anywhere in (a)–(c) or in the
necessity Theorem L1.4(a): the digit route needs only Kummer's
theorem and the support characterisation (Lemma L1.1). (N1) and (N2)
are independent necessary conditions (the key lemma and the level-2
gcd), neither implied by the low-digit system (LD3) nor needed for
the implication "(H3+) unsatisfiable $\Rightarrow$ $i=3$ closed";
that implication is, by (b), an equivalence of statements, and its
proof content would have to come from the digit conditions
themselves.

*Proof.* (a) If $(n,j)$ satisfies (LD3+), then by Definition L1.3
every prime $p\ge3$ dividing $C(n,3)$ fails to divide $C(n,j)$; the
primes $\ge3$ dividing $C(n,3)$ are exactly the prime divisors of
$V_3(n)$, so $\gcd(V_3(n),C(n,j))=1$, which with $3<j\le n/2$ is the
definition of a counterexample. The converse is Theorem L1.4(a). (b)
is (a) restated. (c) The inclusion is Theorem L1.4(b), and emptiness
of the larger set implies emptiness of the smaller; the failure of
the converse direction is exactly Claim L1.5(b). The brief's
parenthetical appears to import into (LD3+) a caveat that A1.16 /
A2.27 state, correctly, for (LD3) alone ("a solution of (LD3) could
still be saved by higher digits"): once the higher digits are all
imposed, there is nothing left to be saved by. (d) By inspection of
the proofs of Lemma L1.1, Lemma L1.2, and Theorem L1.4. $\square$

**Claim L4.2 (verdict: option (b); PROVED as a statement of what this
file does and does not establish).** Exactly one of the brief's three
outcomes holds for this cluster's work:

**(b) (LD3+) is computationally stronger than (LD3) plus the certified
filters on the subsystems and classes where both can be tested, but
no general shrinkage of the residual class is proved, and no residual
configuration is exhibited that (LD3+) excludes and (LD3) does not.**

The evidence: (i) per-prime, ($\beta$) is a genuine extra condition,
with both outcomes occurring under identical low data (Claim L1.5(a));
(ii) on the $\ge5$ subsystem, (LD3+) kills 8 of the 12 solutions with
$n\le10^6$ through higher digits at $p\ge5$ alone, a channel (LD3)
does not have (Computation L2.5); (iii) against this, in **every**
class drawn from the residual's own description that was tested (the
$h=0$ rows of Computation L3.2, exhaustively for all $n$ in those
rows by Lemma L3.1, and the $(4,2)$ row), the candidate set reaching
the (LD3+) stage is **empty**: the Proposition 4.1 filter and (LD3)
dispose of everything first. And on the full system the two solution
sets agree on the whole certified range (both empty for $n\le10^6$).

The exact point where the proof attempt stops is this. A general
shrinkage proof would have to produce, from the residual data alone
(the row parameters $(Q,R)$, the bound $T$, the F1.9/F2.9 label
information: relevant prime powers are $\le T$ or divide $j$), a prime
$p$ in the support and a digit position $k\ge a(p)$ at which
$\mathrm{dig}_k(j,p)>\mathrm{dig}_k(n,p)$ is forced. The residual data
constrain only prime powers and low residues: they say nothing about
the quotient digits $\lfloor j/q\rfloor\bmod p$ versus
$U\bmod p$ when both quotients are large, and Claim L1.5(a) shows
that with $n$, $p$, and the low clause all fixed, the high condition
can pass ($j=5$) or fail ($j=15$) independently. In the residual
class $j\ge5001$ and $n>10^6$, so the quotients are large and there
are many digit positions; the high conditions there are genuine
additional congruences on $j$ modulo $p^{a+t}$ for all $t$, which
heuristically thin candidates digit by digit (at each new position
the digit of $j$ must land in a set of size
$\mathrm{dig}(n,p)+1$ out of $p$), but a thinning heuristic is not an
emptiness proof, and the Chinese remainder theorem poses no
obstruction to simultaneous digit alignments across positions and
primes, for exactly the reason F1.11/F2.14 identify for the low
system: the choices are a priori independent. No argument in this
file bridges that gap, and outcome (a) is therefore not claimed.
Outcome (c) is also not claimed: it would require proving that
(LD3+) adds nothing on the **whole** residual class, which the
evidence of (ii) makes implausible as a statement about the
conditions themselves, and which no computation here (all of it at
$n\le10^8$ in thin rows, or $n\le10^6$ for the full system) can
establish. $\square$

## 5. Closing statement for Cluster L

**Claim L5.1 (summary; PROVED as a summary of the claims above).**

*Proved in this file:*
1. (LD3+) formulated exactly (Definition L1.3), with the digit split
   at $a=a(p)$ into the low condition ($\alpha$), which is **exactly**
   (LD3)'s clause (Lemma L1.2, the brief's L.1(ii) question, answered:
   the congruence $j\bmod q\le r$ already encodes the vanishing of
   $j$'s digits $1,\dots,a-1$), and the high condition ($\beta$),
   $\lfloor j/q\rfloor\preceq_p (n-r)/q$, which is all of (LD3+)'s new
   content, including the digit-$a$ condition with its nonzero
   right-hand side $U\bmod p$ and the entirely-new conditions at
   first-power primes ($a=1$).
2. Necessity of (LD3+) for a counterexample, and
   (LD3+) $\Rightarrow$ (LD3) (Theorem L1.4). Support characterisation
   (Lemma L1.1): primes dividing no top number are irrelevant, and
   $3\mid C(n,3)$ iff the $3$-top has valuation $\ge2$.
3. The $p=3$ conditions in all three cases $v_3(n)$, $v_3(n-1)$,
   $v_3(n-2)$ $\ge2$ (Theorem L2.1); the $a_3=1$ case correctly has no
   content (Claim L2.2). For the family $n=3^a+1$, $j=n/2$ the $p=3$
   high condition passes for all $a$, so (LD3+) gives **no**
   independent or stronger exclusion of that family (Claim L2.3); for
   $n=3^a-1$ there is no $p=3$ condition at all, and for
   $n=2\cdot3^a+1$, $j=3^a$ both $p=3$ subconditions pass (Claim L2.4).
4. The $h=0$ odd-top bound $n-1\mid3\Lambda_3(T)$ for even $n$
   (Lemma L3.1), making the row enumerations of §3 exhaustive for
   all $n$ in those rows.
5. The logical relations (H3) $\Rightarrow$ (H3+) $\iff$ ($i=3$
   closed), with the correction of Claim L4.1(c), and the
   independence of this route from (N1) and (N2) (Claim L4.1(d)).

*Computed in this file (COMPUTATION):*
6. The digit machinery validated against Kummer's theorem
   exhaustively for $n\le300$ (84,526 instances) and the low-digit
   equivalence exhaustively for $n\le1000$ (1,101,758 instances).
7. The $\ge5$-only (LD3) system has exactly 12 solutions with
   $n\le10^6$ (the family $n=3^a+1$, $2\le a\le12$, plus $(162,70)$),
   reproducing P-A1's six for $n\le2000$; 8 of the 12 are excluded by
   $\ge5$ higher digits alone; all 12 pass the $p=3$ high
   subcondition and fail the $p=3$ low clause (Computation L2.5).
8. Ten $h=0$ row classes enumerated to $n\le10^8$ by the finite
   odd-part parametrisation: the $(2,4)$ class is empty in the domain
   already at the Proposition 4.1 filter; 23 $V$-passers across all
   rows, all killed by (LD3), zero reaching (LD3+) (Computation
   L3.2); the $(4,2)$ candidates disposed of as in Cycle 2
   (Claim L3.3).

*Still OPEN, explicitly:* whether
$\mathrm{Sol}(\mathrm{LD3})\setminus\mathrm{Sol}(\mathrm{LD3+})$ is
nonempty (Claim L1.5(b)); whether (LD3+) excludes **any**
configuration in the residual class that (LD3) and the certified
Cycle 1–2 filters do not (no instance found, no proof either way,
Claim L4.2); (H3); (H3+), which by Claim L4.1 is equivalent to
closing $i=3$ and is therefore exactly as hard as the problem it was
meant to assist. **$i=3$ is not closed and #699 is not claimed
solved.**

## 6. Verification log

All numbers above are outputs of `proofs/P-L1_checks.py` (30.5 s,
stdlib only, exact arithmetic), whose sections assert their own
headline values:

- §A: Kummer equivalence $\mathrm{dig}$-wise $\iff p\nmid C(n,j)$:
  84,526 instances $(n,j,p)$, $n\le300$, 0 failures (note this count
  coincides with V-A's independent spot-check count for A1.15 at the
  same bound, by the same exhaustive design); low-digit equivalence
  and $n\bmod q=r$: 1,101,758 instances, $n\le1000$, 0 failures;
  the support of $C(n,3)$ computed from the tops asserted equal to
  the support computed from $C(n,3)$ directly, for all $n\le300$.
- §B: the six calibration pairs of P-A1: $\ge5$ (LD3) holds, full
  (LD3) fails at the displayed $3$-clause, (LD3+) failing primes as
  listed in Computation L2.5's discussion, $p=3$ high subcondition
  passes for all six.
- §C: the three families of §2: $n=3^a+1$ for $2\le a\le12$ ($\ge5$
  (LD3) holds, low $3$-clause fails at $(3,a,1,3^a)$, high passes);
  $n=3^a-1$ for $2\le a\le8$ ($a_3=1$ asserted, (LD3) fails at the
  displayed $\ge5$ witness); $n=2\cdot3^a+1$, $j=3^a$ for
  $2\le a\le8$ (both $p=3$ subconditions pass, (LD3) fails at an
  $r=0$ witness).
- §D: the $\ge5$-only search to $10^6$: 26,035,963 candidate pairs,
  exactly the 12 solutions asserted, with the per-solution
  classification of Computation L2.5 asserted line by line (8 with a
  $\ge5$ higher failure, all 12 passing the $p=3$ high subcondition,
  all 12 failing the $p=3$ low clause at the displayed witness).
- §E: the ten $h=0$ rows of Computation L3.2 (odd-part divisors of
  $3\Lambda_3(T)$ generated from its prime factorisation, candidates
  $n=o\cdot2^s\le10^8$, row filter, $V_3(n)\mid\Lambda_3(T)$ filter
  with the assertion $V_3(n)\le\Lambda_3(T)$ for every passer, then
  (LD3), then (LD3+)); §E2: the $(4,2)$ finite set, exactly
  $(22,5),(46,11),(106,26)$, all failing (LD3), gcds $77,69,371$.
- §F: the local strictness example $(30,15,5)$: low condition holds,
  full digitwise condition fails at digit 1 ($3>1$), asserted.
