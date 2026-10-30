# Verifier B (independent): verification of P-B1 and P-B2, Strategy S1, Erdős #699

Verifier: B (independent; did not write either proof). Documents checked:
`proofs/P-B1.md` (Lemmas B1.1 to B1.12, including B1.12a) and
`proofs/P-B2.md` (Lemmas B2.1 to B2.6, Theorems B2.A to B2.D).
All computations below are my own, run for this verification in Python
standard library only, exact integer or rational arithmetic wherever a
decision is made. Code: [V-B_checks.py](sandbox://workspace/math-hunt/erdos-699-proof/verification/V-B_checks.py)
(stages `quick` 3.1 s, `recount` 8.7 s, `spot500` 2.7 s).

**Headline result.** 23 numbered items classified: 22 PROVED, 1 GAP,
0 FALSE, 0 OPEN. The single GAP is localized and repairable: the proof of
Theorem B2.B, case (1), in P-B2 contains a false intermediate target
(it repeats the S1 slip that P-B1 correctly flags). The statement of
B2.B is true, and the one line repair is given below. Every headline
number in T-D reproduces exactly in my third recount.

---

## 1. Mandatory check 1: re-derivation of the proof skeleton

**(L-K), Legendre summands.** For $x=i/p^e$, $y=(n-i)/p^e$, $x+y=n/p^e$ and
$\lfloor x+y\rfloor-\lfloor x\rfloor-\lfloor y\rfloor
= \lfloor\{x\}+\{y\}\rfloor \in \{0,1\}$ since $0\le\{x\}+\{y\}<2$.
Vanishing for $p^e>n$: then $n<p^e$ and $0\le i,\ n-i\le n<p^e$, so all
three floors are $0$. This is valid for general $1\le i\le n$, in
particular for $i>n/2$ (outside our range $i\le n/2$, but the lemma as
stated covers it, including $i=n-1$ and $i=n$, which I tested explicitly).
Hence $v_p(C(n,i))$ is a sum of at most $\#\{e\ge1:p^e\le n\}$
terms each at most $1$, giving $p^{v_p(C(n,i))}\le q_p(n)\le n$.
My test: 3,000 random $(n,i,p)$ with $i$ uniform in $1..n$ (so $i>n/2$
included): summand set, vanishing, $\sum = v_p$ computed by direct
division of $C(n,i)$, and $p^{v_p}\le q_p(n)\le n$; 0 violations.
Multiplying over $p<i$ gives $u\le U^\sharp(n,i)\le n^{\pi(i-1)}$,
since each $q_p(n)\le n$ and there are $\pi(i-1)$ factors. Both
B1.2/B1.3 and B2.2/B2.3 are correct.

**$\pi(i-1)\le i/2$, equality exactly at $\{4,6,8\}$.** I tested all
$i\le 10000$ computationally: no violations, and equality holds exactly
at $i\in\{4,6,8\}$. Audit of B1.4: for $i\le2$, $\pi(i-1)=0$. For
$i\ge3$ the odd integers in $[3,i-1]$ are $2k+1$, $1\le k\le (i-2)/2$,
count $\lfloor(i-2)/2\rfloor$, which handles the small cases correctly
($i=3$: empty set, count $0$; $i=4$: $\{3\}$, count $1$), giving
$\pi(i-1)\le 1+\lfloor(i-2)/2\rfloor\le i/2$. Equality: odd $i\ge3$ is
excluded since $\pi(i-1)\le (i-1)/2<i/2$; even $i\ge10$ is excluded
since $9\in[3,i-1]$ is an odd composite, costing one from the count.
B2.3(d)'s variant, $\pi(i-1)\le 1+(\lfloor i/2\rfloor-1)=\lfloor i/2\rfloor$,
is also watertight (odd integers in $[1,i-1]$ number $\lfloor i/2\rfloor$,
exclude $1$); B2's lemma does not itself claim the global equality
classification, which is fine because no B2 theorem needs it.
The case splits used later check out: $\pi(i-1)=0$ iff $i\in\{1,2\}$,
$\pi(i-1)=1$ iff $i=3$ (verified computationally).

**Monotonicity of $F_i$, the Bernoulli step.** The ratio is
$F_i(n+1)/F_i(n)=\frac{n+1}{n+1-i}\,(n/(n+1))^{\pi}$, and $>1$ is
equivalent to $n^{\pi}/(n+1)^{\pi-1} > n+1-i$ $(\ast)$.
Case $\pi=0$: $(\ast)$ is $n+1>n+1-i$. Case $\pi=1$ ($i=3$): $(\ast)$
is $n>n+1-i$. Case $\pi\ge2$: writing the left side as
$n(1-\frac1{n+1})^{\pi-1}$, Bernoulli with $r=\pi-1\ge1$,
$y=-1/(n+1)\ge-1$ gives $\ge n-\frac{n(\pi-1)}{n+1} > n-(\pi-1)\ge n+1-i$,
the strict step using $n/(n+1)<1$ and $\pi-1>0$, the last step using
$\pi\le i$. Valid as written in both documents (B2.4's phrase "dividing
by $n+1$" compresses a second division by $(n+1)^{\pi-1}$; the asserted
equivalence $(\ast)$ is correct). Crucially the argument is for
**every** $n\ge i$, not only $n\ge 2j$: the ratio step is proved for all
$n\ge i$, so $F_i$ is strictly increasing on all of $[i,\infty)$, and
the growth bound $F_i(n)\ge n^{i-\pi}/i^i\to\infty$ (using
$(n-t)/(i-t)\ge n/i$) is correct. I also verified strict increase in
exact `Fraction` arithmetic for all $i\le40$, $i\le n<300$: 0 failures.

**The T-D criterion chain and the prefix property in $j$.**
$N_K(i,j)\le 10000$ iff $F_i(10001)>C(j,j-i)$: since $F_i$ is strictly
increasing and tends to infinity, $\{n:F_i(n)\le C(j,j-i)\}$ is an
initial segment; its maximum is $\le10000$ iff $10001$ is outside it,
and the inequality is strict exactly as stated (equality at $10001$
would put $10001$ in the set). Cross-multiplying by the positive
$10001^{\pi(i-1)}$ gives the exact integer predicate
$C(j,j-i)\cdot10001^{\pi(i-1)} < C(10001,i)$, and $C(j,j-i)=C(j,i)$.
Application form: if the predicate holds at $(i,j)$ then
$F_i(n)>C(j,j-i)$ for **all** $n>10000$ (monotonicity from $n=10001$
upward), so any counterexample for that pair has $n\le10000$.
Prefix property: for fixed $i$, $j\mapsto C(j,i)$ is strictly increasing
(ratio $(j+1)/(j+1-i)>1$), so $\{j : \text{predicate holds}\}$ is a
prefix of the $j$ range, and intersecting with the open range
$j>\lfloor 3i/2\rfloor$ and with the EEES prefix gives exactly the
count formulas both provers use,
$\max(0,\ \min(J_K,5000)-\max(J_E,\lfloor 3i/2\rfloor))$ (B1) and the
equivalent $+1$ form (B2). B1.12a's second monotonicity,
$j\mapsto C(2j,2(j-i))=C(2j,2i)$ with ratio
$(2j+2)(2j+1)/((2j+2-2i)(2j+1-2i))>1$, and B2.D's EEES ratio, are both
correct. Note the distinction both documents keep straight: the prefix
property is in $j$ for the clearance criterion; $\mathrm{Bad}^\sharp$
as a set of $n$ is **not** an interval (see (3,7) below).

## 2. Mandatory check 2: third independent recount of T-D

Method, different from both provers: $J_K(i)$ was found by **direct
binary search on the exact predicate**
$C(j,j-i)\cdot10001^{\pi(i-1)} < C(10001,i)$ in the form written here
(no floor formula $K_i=\lfloor(T_i-1)/U_i\rfloor$ anywhere), and the
EEES frontier $J_E(i)$ was taken **from `pairpass.json`**
(`cleared_js_by_i`; I first verified each list is exactly the prefix
$[\lfloor3i/2\rfloor+1,\ J_E(i)]$: 0 structural mismatches, file total
768,741). Runtime 8.7 s.

My exact results, agreeing with S1, P-B1 and P-B2 on every entry:

| quantity | claimed | Verifier B recount |
|---|---|---|
| open pairs ($i\le1000$, $j>3i/2$, $2j\le10000$) | 4,249,500 | 4,249,500 |
| EEES cleared | 768,741 | 768,741 |
| Kummer cleared within open range | 1,096,586 | 1,096,586 |
| **newly cleared** | **328,079** | **328,079** |
| newly cleared with $i\ge3$ | 318,242 | 318,242 |
| newly cleared with $i\in\{1,2\}$ | 9,837 | 9,837 (4,930 + 4,907) |
| **union cleared total** | **1,096,820** | **1,096,820** |
| $J_K(100)$ / $J_E(100)$ | 1045 / 656 | 1045 / 656 |
| $J_K(1000)$ / $J_E(1000)$ | 2541 / 2391 | 2541 / 2391 |

All eight shared spot pairs agree: $(i,J_E,J_K) = (3,112,465)$,
$(5,142,253)$, $(10,199,255)$, $(11,209,355)$, $(50,454,654)$,
$(100,656,1045)$, $(500,1597,1950)$, $(1000,2391,2541)$. The indices
$i\le30$ with $J_K(i)\le J_E(i)$ are exactly $\{4,6,8,9,14,20\}$.

Predicate equivalence spot verification: 500 seeded random pairs
($i$ uniform in $1..1000$, $j$ uniform in the open range, seed
20261028). For each pair I computed $N_K(i,j)$ **directly from the
definition of $F_i$**: a float-guided bracket, then exact boundary
verification exhibiting $n_0$ with $F_i(n_0)\le C(j,j-i)$ and
$F_i(n_0+1)>C(j,j-i)$ in exact integer arithmetic
($C(n,i)\le C(j,j-i)\cdot n^{\pi(i-1)}$), at most 1 exact adjustment
step per pair. Comparison $(N_K\le10000) \Leftrightarrow$ predicate:
**0 mismatches in 500**.

## 3. Mandatory check 3: (3,7) singleton and T-B endpoints

Direct computation for $(3,7)$, target $C(7,4)=35$,
$U^\sharp(n,3)=2^{\lfloor\log_2 n\rfloor}$:
$G_3(14)=364/8=91/2$, $G_3(15)=455/8$, $G_3(16)=560/16=35\le35$, and
$F_3(17)=680/17=40>35$ with $F_3$ increasing and $G_3\ge F_3$ excludes
all $n\ge17$; my scan of $14\le n\le2000$ also returns exactly $\{16\}$.
So $\mathrm{Bad}^\sharp(3,7)=\{16\}$ exactly. The equality case is real:
Legendre terms for $v_2(C(16,3))$ are $(8-1-6)+(4-0-3)+(2-0-1)+(1-0-0)
=1+1+1+1=4$, so $u=2^4=16=U^\sharp(16,3)=U(16,3)$, and
$C(16,3)=560=16\cdot35=U^\sharp\cdot C(7,4)$ with equality; the pair is
only closed by the direct check $\gcd(35,C(16,7))=\gcd(35,11440)=5>1$.

T-B endpoints, all exact: $i=1$: $u=1$, $v=n$, correct target is
$C(j,j-1)=j$, and $n\ge2j>j$ (see the B2.B note below). $i=2$: $u=1$ and
$C(2j,2)=j(2j-1)>j(j-1)/2=C(j,2)$ for all $j$ (tested $3\le j<500$,
and the algebra is immediate). $(3,5)$: $F_3(10)=120/10=12>10=C(5,2)$,
crude bound suffices. $(3,6)$: crude fails, $F_3(12)=55/3\le20$;
$U^\sharp(n,3)=8$ on $[12,15]$, $G_3(12)=220/8=55/2>20=C(6,3)$, and
$F_3(16)=560/16=35>20$ covers $n\ge16$. All confirmed.

**Discrepancy found (in P-B2 only).** Theorem B2.B, case (1), states a
counterexample for $i=1$ would force "$n=v\le C(j,0)=1$". That target
is wrong: the key lemma gives $C(j,j-i)=C(j,j-1)=j$ (equivalently
$C(j,i)=C(j,1)=j$), not $C(j,0)$. This is precisely the S1 slip that
B1.8 flags and repairs. The closure still follows, since
$n=v\le j$ contradicts $n\ge2j$ for $j\ge1$, so the **statement** of
B2.B is true; the **proof as written** has a false step in case (1).
I therefore classify B2.B as GAP (localized, one line repair:
replace $C(j,0)=1$ by $C(j,j-1)=j$ and $n\ge2j>j$), not FALSE.
Cases (2), (3), (4) of B2.B are proved exactly as written.
No other document contains this error: P-B1's B1.8(1) is correct.

## 4. Mandatory check 4: Theorem C, the diagonal barrier

Closed form, re-derived: from
$\Delta(c)=2c\log(2c)-(2c-1)\log(2c-1)-c\log c+(c-1)\log(c-1)$,
term-by-term differentiation gives
$\Delta'(c)=\log\frac{4c(c-1)}{(2c-1)^2}$, confirmed two ways: B1's
direct differentiation, B2.6's split $A'(c)=2\log\frac{2c}{2c-1}$,
$B'(c)=\log\frac{c}{c-1}$, whose difference is the same expression
($\frac{4c^2}{(2c-1)^2}\cdot\frac{c-1}{c}=\frac{4c(c-1)}{(2c-1)^2}$);
and my numeric central differences agree with the closed form to
$10^{-9}$ at $c=1.1,\ 1.3672,\ 1.5,\ 2,\ 5$. Since
$(2c-1)^2=4c(c-1)+1>4c(c-1)$, $\Delta'(c)<0$ on $(1,\infty)$: strictly
decreasing. High precision values (Decimal, 60 digits, mine):
$\Delta(1)=1.386294361120$, $\Delta(3/2)=0.954771252442$ (claimed
0.954771, correct), $\Delta(2)=0.863046217355$,
$\Delta(1.3672)=1.000007582390>1$, $\Delta(1.3673)=0.999967176884<1$,
so the root bracket $c^\ast\in(1.3672,1.3673)$ holds, and bisection
gives $c^\ast=1.367218763568$, i.e. $1.3672$ to four decimals
(B2's $1.3672188$ and $1.36722$ are both consistent roundings).
Limit $\Delta(c)\to\log2$ via $m\log(1+1/m)\to1$ is correct.
The barrier argument itself (entropy term $\Delta(c)\,i+o(i)$ from
Stirling; $\pi(i-1)\log(2j)=i+o(i)$ and the squeeze
$\theta(i-1)\le\log U^\sharp(2j,i)\le\pi(i-1)\log(2j)$, both ends
$i+o(i)$, from the prime number theorem) is sound in both documents.
Theorem C is a limitation statement whose proof legitimately uses
Stirling plus PNT, as both provers state; nothing elementary is claimed
for it. Classification: PROVED (as a limitation statement).

Extra check, P-B1 only: Proposition B1.10(b) was re-run by me in exact
integer arithmetic: for $4\le i\le60$ and every open pair $j\le2000$
(111,278 pairs, the claimed count) $R^\sharp(i,j)<0$ holds in every
case, closest approach $(i,j)=(7,11)$ at $-0.3316$ (float margin,
sign decided exactly); and $R^\sharp(3,j)<0$ for all $8\le j\le2000$.

---

## 5. Classification tables

### P-B1 (13 items: 13 PROVED, 0 GAP, 0 FALSE, 0 OPEN)

| Item | Content | Verdict |
|---|---|---|
| B1.1 | key lemma, $d\mid C(j,j-i)$ | PROVED |
| B1.2 | (L-K) $p^{v_p(C(n,i))}\le q_p(n)\le n$ | PROVED |
| B1.3 | $u\le U^\sharp\le n^{\pi(i-1)}$, monotonicity, $\theta$ lower bound | PROVED |
| B1.4 | $\pi(i-1)\le i/2$ all $i$, equality exactly $\{4,6,8\}$ | PROVED |
| B1.5 | $F_i$ strictly increasing for all $n\ge i$, growth to $\infty$ | PROVED |
| B1.6 | sharp test: containment, sawtooth, $\mathrm{Bad}^\sharp(3,7)=\{16\}$ | PROVED |
| B1.7 | (T-A) EEES-free reduction $n\in\mathrm{Bad}^\sharp\subseteq[2j,N_K]$ | PROVED |
| B1.8 | (T-B) closures $i=1$, $i=2$, $(3,5)$, $(3,6)$ | PROVED |
| B1.9 | entropy estimates, $\Delta$ analysis, $c^\ast\in(1.3672,1.3673)$ | PROVED |
| B1.10 | Proposition B': $i=3$ margins to $-\infty$; exact scan $i\le60$ | PROVED |
| B1.11 | Theorem C barrier, both margins per unit $i\to\Delta(c)-1$ | PROVED |
| B1.12a | prefix monotonicity in $j$ (both criteria) | PROVED |
| B1.12 | (T-D) recount 328,079 / 318,242 / total 1,096,820 | PROVED |

### P-B2 (10 items: 9 PROVED, 1 GAP, 0 FALSE, 0 OPEN)

| Item | Content | Verdict |
|---|---|---|
| B2.1 | key lemma | PROVED |
| B2.2 | (L-K), sharp form with $e_p(n)$ | PROVED |
| B2.3 | small-part bounds; $\pi(i-1)\le i/2$ audit | PROVED |
| B2.4 | $F_i$ strictly increasing, Bernoulli audit, growth | PROVED |
| B2.5 | sharp test finiteness and sawtooth; $N_K$ well defined | PROVED |
| B2.6 | $\Delta$ closed form, derivative, root $c^\ast=1.36722\ldots$ | PROVED |
| B2.A | (T-A) EEES-free finite reduction | PROVED |
| B2.B | (T-B) closures | **GAP** (proof only: case (1) uses the false target $C(j,0)=1$; correct target $C(j,j-1)=j$ repairs it, statement true; cases (2) to (4) proved) |
| B2.C | Theorem C barrier, $c^\ast\approx1.36722$ | PROVED |
| B2.D | (T-D) recount 328,079 / 318,242, spots 1045 and 2541 | PROVED |

Minor notes, not affecting any classification: B2.4's derivation of
$(\ast)$ compresses one division step (the equivalence stated is
correct); Remark B2.7's global equality set $\{4,6,8\}$ is proved in
B1.4 and verified by me to $i\le10000$, though B2.3 alone only audits
it to $i\le100$ (the remark is not load-bearing for B2.A to B2.D);
the two documents define $N_K$ cosmetically differently (B1 by a
$2j-1$ empty convention, B2 as a maximum over $n\ge i$, nonempty since
$F_i(i)\le1$), with identical consequences for every use.

## 6. Final verdicts per claim at stake

- **(L-K)** $p^{v_p(C(n,i))}\le n$: **PROVED**, twice independently
  (B1.2, B2.2), and re-derived and randomly tested by me.
- **(T-A)** EEES-free reduction $n\le N_K(i,j)$ (sharp form
  $n\in\mathrm{Bad}^\sharp(i,j)$): **PROVED** (B1.7, B2.A).
- **(T-B)** all-$n$ closures $i=1$, $i=2$ (all $j$), $(3,5)$, $(3,6)$:
  **PROVED** as statements, with a complete proof in B1.8. In P-B2 the
  proof of B2.B has one localized GAP in case (1) (false target
  $C(j,0)=1$, repair $C(j,j-1)=j$ supplied above); the theorem itself
  is not false.
- **(T-D)** payoff count: **PROVED**. My third recount, by a different
  method (direct predicate binary search, EEES frontier from
  `pairpass.json`), gives exactly **328,079** newly cleared pairs,
  **318,242** with $i\ge3$, total cleared **1,096,820**, with
  $J_K(100)=1045$ and $J_K(1000)=2541$; the predicate/$N_K$ equivalence
  was spot-verified on 500 random pairs with 0 mismatches.
- **(Theorem C)** diagonal barrier $c^\ast\approx1.3672$:
  **PROVED** as a limitation statement (Stirling plus PNT, explicitly
  flagged as such by both provers); $\Delta$ and $\Delta'$ re-derived,
  $\Delta(3/2)=0.954771$, root $c^\ast=1.3672187636\in(1.3672,1.3673)$
  confirmed in 60-digit arithmetic.

No FALSE statements and no OPEN items were found in either document.
The only defect anywhere is the B2.B case (1) proof step described
above, inherited from S1's text, which P-B1 had already caught.
