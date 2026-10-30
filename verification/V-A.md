# Verifier A (independent): verification of P-A1 and P-A2 for Erdős #699

Verifier: A (independent; did not write either proof). Scope: every numbered
item in `proofs/P-A1.md` (A1.1–A1.17) and `proofs/P-A2.md` (A2.1–A2.29),
the four theorems T1–T4, the S5 proviso dispute, and the mandated bounded
computations. All computations below are my own, Python standard library,
exact integer / exact rational arithmetic (plus one SymPy symbolic check),
total runtime under ~15 seconds. Classifications: **PROVED** / **GAP** /
**FALSE** / **OPEN**. No item in either proof document is GAP or FALSE.
The one FALSE claim found anywhere is in the *source* paper S5, not in
either proof document; both provers caught and corrected it, and I confirm
the correction independently.

## 1. Classification table: P-A1

| Item | Content | Verdict | Notes |
|---|---|---|---|
| A1.1 | Identity + key lemma | PROVED | Double-counting correct; Euclid step correct. |
| A1.2 | $V_i(n)=C(n,i)$ for $i\le2$ | PROVED | Definitional; every prime is $\ge1$, $\ge2$. This is what licenses $d=C(n,i)$ in T1/T2. |
| A1.3 | $n/\gcd(n,j) \mid C(n,j)$ | PROVED | Absorption + Euclid argument re-derived; my brute check: divisibility holds for all $n\le300$, all $j<n$, 0 failures. |
| A1.4 (T1) | $i=1$ closed, all $j,n$ | PROVED | $\gcd(n,j)\le j\le n/2$ gives $n'\ge2$. No EEES78, no finiteness. |
| A1.5 (T2) | $i=2$ closed, all $j,n$ | PROVED | Negation logic airtight (see §3.1). $C(j,2)<C(n,2)$ for $j<n$ correct. |
| A1.6 | Square reduction | PROVED | Exception conditioning present and correct: hypothesis is "$(n,i)$ not an EEES78 exception"; EEES78 used only there. |
| A1.7 | Pair-closure criterion $(\ast)$ | PROVED | Monotonicity of $C(n,i)$ in $n$ correct. |
| A1.8 | Odd step ratio, $(\ast)$ for odd $i\ge3$ | PROVED | $R_1=6/5$ recomputed; step identity and "minus 1" numerator $72m^4+369m^3+678m^2+523m+140$ verified by me symbolically (SymPy, difference exactly 0) and in exact rationals at $m=1,\dots,6,10,37$. |
| A1.9 | Even step ratio, $(\ast)$ for even $i\ge10$ | PROVED | Step identity verified in exact rationals at $m=1,\dots,6,10,37$ against the binomial ratios; "minus 1" numerator $144m^5+\cdots-202m-80$ verified symbolically from the claimed step formula; positivity argument ($546m^4$ dominates) correct. $R_5$ recomputed (see §3.3). |
| A1.10 | Exactly two in-family exception triples | PROVED | Independently re-enumerated (§3.2); both gcds recomputed: 377 and 57293. Contains the correction to S5. |
| A1.11 | Small $i\in\{4,6,8\}$ via Phase 0 + finite check | PROVED | $N=17,23,29$ and all twelve gcds recomputed exactly, all match (§3.4). $(\ast)$-failures $1001<1225$, $38760<44100$, $1562275<1656369$ recomputed. No exception triple at these pairs: correct. |
| A1.12 (T3) | Boundary family closed, all $i,n$ | PROVED | Case split is exhaustive (odd $\ge3$; even $\ge10$; $\{1,2,4,6,8\}$); exception values handled by A1.10 in every branch. |
| A1.13 | $U_3(n)\le 2^{\lfloor\log_2 n\rfloor}\le n$ | PROVED | Legendre summands are 0/1; count correct. |
| A1.14 | $(3,5)$, $(3,6)$ closed, EEES-free | PROVED | $F(10)=12>10$; $G(12)=27.5>20$, $F(16)=35>20$ recomputed. Remark $\mathrm{Bad}^\sharp(3,7)=\{16\}$ on $[14,200)$ independently reproduced; $\gcd(V_3(16),C(16,7))=5$ recomputed. |
| A1.15 | Low-digit lemma (S8 Lemma 3) | PROVED | $p\mid C(n,3)$ in both cases correct ($v_3=a-1\ge1$ in case (b)); Kummer digit argument correct. Computationally spot-checked exhaustively for $n\le300$ (§3.5): 0 failures in 84,526 instances. |
| A1.16 | Necessary conditions (LD3), (N1), (N2), odd-top rigidity | PROVED | (i) is the contrapositive of A1.15 applied per relevant $q$ (one parenthetical phrase is loosely worded but the derivation is the correct one); (ii)–(iv) re-derived and correct; $j=n/3$ pinning for odd $n>9$ correct. (LD3) explicitly stated necessary-not-sufficient: correct. |
| A1.17 (T4) | Exact $i=3$ status | PROVED (as stated) | Claims (a), (c), (d) verified; (b) ($j\le465$) rests on the cited Stage 2 sweep + S1 Theorem D, which are standing inputs, not re-proved in either document, and are labelled as such. The document does **not** claim $i=3$ closed. |

**P-A1 totals: 17 items — 17 PROVED, 0 GAP, 0 FALSE, 0 OPEN-as-claims**
(H3 inside A1.16/A1.17 is presented as an open statement, correctly).

## 2. Classification table: P-A2

| Item | Content | Verdict | Notes |
|---|---|---|---|
| A2.1 | Identity + key lemma | PROVED | Same argument as A1.1, independently correct. |
| A2.2 | Square + Phase 0 reductions | PROVED | Vandermonde step correct: the $k=d$ term is $C(j,d)^2$ and there are $\ge3$ positive terms, so the inequality is strict. Exception conditioning explicit. |
| A2.3 | Monotonicity | PROVED | |
| A2.4 | $V_1,V_2$ are the whole binomial | PROVED | Same as A1.2. |
| A2.5 (T1) | $i=1$ closed (two proofs) | PROVED | Proof 1 is the key-lemma route; hypothesis check (i)–(iv) in A2.6 is accurate. Proof 2 matches A1.3. |
| A2.6 | Remark reconciling Kummer discussion | PROVED (remark correct) | The "whole $n$, not $\mathrm{rad}(n)$" point is correct. |
| A2.7 (T2) | $i=2$ closed | PROVED | Same airtight negation logic as A1.5. |
| A2.8 | Remark: why the argument stops at $i=2$ | PROVED (remark correct) | The $n=2^a$ size comparison is correct as an illustration. |
| A2.9 | Phase 0 does not close the family | PROVED | One-step/two-step ratios recomputed: odd $(4m+3)/(2m+2)>1$; even $\frac{4m+2}{2m+1}\cdot\frac{4m+1}{2m+2}>1$. |
| A2.10 | Pair-closure criterion | PROVED | Same as A1.7. |
| A2.11 | Odd step ratios | PROVED | Identities verified by me exactly as for A1.8 (symbolic + rational spot values). $R_1=6/5$. |
| A2.12 | Even step ratios; $R_5$ | PROVED | $R_m<1$ exactly at $m=1,2,3,4$ recomputed: $7/9,\ 143/175,\ 646/735,\ 10925/11583$ — all match. $R_5$ see §3.3. Positivity argument correct. |
| A2.13 | In-family exceptions: exactly two, both closed | PROVED | Enumeration and both gcds independently recomputed (§3.2). Factorisations of $C(30,7)$, $C(56,13)$ and the values $V_7(30)=377$, $V_{13}(56)=973981$ all check. |
| A2.14 | $(4,7),(6,10),(8,13)$ finite closure | PROVED | $N$ values and twelve gcds recomputed, all match (§3.4); the claim that for $(6,10)$ the gcd equals $V_6(n)$ itself also verified ($V_6(n)=323,2261,24871,33649$). |
| A2.15 (T3) | Boundary family complete, all $i$ | PROVED | Exhaustive case split; no excluded finite set remains, as claimed. |
| A2.16 | Remark on division of labour | PROVED (remark correct) | Square inequality genuinely fails at $m=1,\dots,4$ (recomputed). |
| A2.17 | $(3,4)$ closed, all $n$ | PROVED | Self-contained Phase-0-style argument correct ($C(8,2)=28\le C(8,3)=56$); exception $(8,3)$ discharged directly: $\gcd(V_3(8),C(8,4))=\gcd(7,70)=7$, recomputed. |
| A2.18 | $(3,5)$ closed, two proofs | PROVED | Boundary route and EEES-free size route both correct; $F_3(10)=12>10$. |
| A2.19 | $(3,6)$ closed via sharpened bound | PROVED | Same computation as A1.14; $G_3(12)=27.5$, $F_3(16)=35$ recomputed. |
| A2.20 | Prime-power bound $p^{v_p(C(n,k))}\le n$ | PROVED | Legendre argument correct. |
| A2.21 | Low-digit lemma | PROVED | Identical in substance to A1.15; covered by my $n\le300$ exhaustive spot check (§3.5). |
| A2.22 | Definition (LD3) + splitting form | PROVED (definition correct) | Splitting equivalence correct: relevant prime powers are pairwise coprime (also across $n,n-1,n-2$) and each $q\ge5>r$, so $j\bmod q\le r$ iff $q\mid j-s$ for some $s\le r$. |
| A2.23 | (LD3) is necessary for a counterexample | PROVED | Direct from A2.21. |
| A2.24 | (N1), (N2) necessary | PROVED | (N1) argument correct; (N2) is the key lemma at $d=V_3(n)$. |
| A2.25 | Odd-top reduction | PROVED | $R(m)$ formula for odd $m$ correct; (i) pinning $j=n/3$ and (ii) splitting statement correct. |
| A2.26 | $\ge5$-only system: six solutions $n\le2000$; $3^a+1$ family killed | PROVED | My independent enumeration for $n\le1000$ finds **exactly the same six** pairs and no others (§3.5); all six lie below 1000, so the only part of the $n\le2000$ claim outside my rerun is the absence of further solutions in $1000<n\le2000$, which both provers' independent computations agree on. The $3^a+1$, $j=n/2$ discharge is a valid all-$a$ proof, as claimed. |
| A2.27 | Statement $(H_3)$ as the obstruction | OPEN (correctly) | This is a *statement of what is missing*, not a claimed proof. The necessity-not-sufficiency caveat is correct and prominent. |
| A2.28 | Splitting sub-cases (SPLIT-odd/even) | PROVED (as analysis) | Correctly identifies the residual configurations; the claim that no $q>j$-type size argument applies there is accurate. Not a closure, and not presented as one. |
| A2.29 | Remark: pinned case forces $v_2(C(n,3))\ge5$ | PROVED (remark correct) | Re-derived: $v_3(C(n,3))=0$ when $v_3(n)=1$; $C(n,3)/C(j,3)>27$ at $n=3j$ (factors $3$, $>3$, $>3$), so (N2) forces $u>27$, i.e. $u\ge32$. Correctly presented as non-closing. |

**P-A2 totals: 29 items — 28 PROVED (including remarks/definitions/statements
verified correct), 1 OPEN (A2.27, the obstruction statement $H_3$, which the
document itself flags as unproved), 0 GAP, 0 FALSE.**

## 3. Mandated adjudications

### 3.1 Key-lemma logic in T1/T2 — airtight

For $i\le2$, $V_i(n)=C(n,i)$ is genuinely established (A1.2/A2.4: the
defining product for $U_i(n)$ is empty). Hence the claim
$\gcd(V_i(n),C(n,j))>1$ has as its exact negation
$\gcd(C(n,i),C(n,j))=1$, which is *verbatim* the gcd hypothesis of the key
lemma at $d=C(n,i)$ (the divisibility hypothesis is equality). There is no
circularity: proof by contradiction legitimately assumes the negation.
Conclusions: T1 via key lemma forces $n\mid j$, contradicting $0<j<n$; the
retained A1 proof via A1.3 is even stronger. T2 forces
$C(n,2)\mid C(j,2)$, contradicting strict monotonicity. For $i\ge3$ both
documents correctly note the argument stops ($V_i$ a proper divisor). No gap.

### 3.2 The S5 error — CONFIRMED FALSE (in S5); correction in both proofs CONFIRMED

- $(30,7)$ is a genuine EEES78 exception: $V_7(30)=377$,
  $377^2=142{,}129 \le 2{,}035{,}800=C(30,7)$ (recomputed).
- Boundary $j$ at $i=7$: $\lfloor 3\cdot7/2\rfloor+1 = 11$; $30 \ge 22 = 2j$. ✔ in-family.
- $\gcd(V_7(30), C(30,11)) = \gcd(377, 54{,}627{,}300) = 377 > 1$ (recomputed;
  in fact $377 \mid C(30,11)$ with quotient $144{,}900$).
- $\gcd(V_{13}(56), C(56,20)) = \gcd(973981, 785613562163430) = 57293
  = 23\cdot47\cdot53 > 1$ (recomputed), with $V_{13}(56)=973981=17\cdot23\cdot47\cdot53$.
- **Complete census** (my computation, all 12 exception pairs; $j_b=\lfloor3i_0/2\rfloor+1$):

  | $(n_0,i_0)$ | $j_b$ | $2j_b$ | $n_0\ge 2j_b$? |
  |---|---|---|---|
  | (8,3) | 5 | 10 | no |
  | (9,4) | 7 | 14 | no |
  | (10,5) | 8 | 16 | no |
  | (12,5) | 8 | 16 | no |
  | (21,7) | 11 | 22 | no ($21<22$) |
  | (21,8) | 13 | 26 | no |
  | **(30,7)** | **11** | **22** | **YES** |
  | (33,13) | 20 | 40 | no |
  | (33,14) | 22 | 44 | no |
  | (36,13) | 20 | 40 | no |
  | (36,17) | 26 | 52 | no |
  | **(56,13)** | **20** | **40** | **YES** |

  I also verified $V_{i_0}(n_0)^2 \le C(n_0,i_0)$ for all 12 pairs, i.e. each
  listed pair really is an exception. **Exactly two in-family exception
  triples exist: $(30,7,11)$ and $(56,13,20)$.** S5's proviso ("only
  $(56,13,20)$") is FALSE; A1.10/A2.13 state the corrected version, and
  with it T3 is complete. Downstream effect: none beyond the correction —
  the missed triple has gcd 377 and was also inside the Stage 2 blanket
  discharge.

- Square-reduction exception conditioning: checked at every use. A1.6/A2.2
  carry the non-exception hypothesis explicitly; A1.7/A2.10 inherit it;
  every branch of A1.12/A2.15 routes exception pairs to A1.10/A2.13 or
  A1.11/A2.14; A2.17 discharges $(8,3)$ separately. No unconditioned use found.

### 3.3 Step ratios and $R_5$

- Odd identity: verified **symbolically** (SymPy: the product-form step
  ratio minus the claimed closed form simplifies to exactly 0; the
  "minus 1" numerator/denominator match the stated polynomials exactly).
- Even identity: step formula verified in exact rational arithmetic against
  the binomial ratios $R_{m+1}/R_m$ at $m=1,2,3,4,5,6,10,37$ (all equal);
  "minus 1" numerator and denominator verified symbolically from the
  claimed step formula. This matches or exceeds the verification status
  each prover claimed for themselves.
- $R_5$: $C(32,10)/C(16,6)^2 = 64512240/64128064$ (A1's form) reduces to
  $310155/308308$ (A2's form); $64512240/64128064 = 310155/308308$ exactly
  (common factor 208, as the task anticipated). **Confirmed: the two
  provers' $R_5$ values are the same rational, $>1$.**

### 3.4 Small-$i$ dispositions — all recomputed exactly

$N(4,7)=17$ ($C(17,4)=2380 < 3003=C(14,6) \le 3060=C(18,4)$),
$N(6,10)=23$, $N(8,13)=29$: **all confirmed**. Twelve gcds, all matching
both documents exactly:

- $(4,7)$, $n=14,15,16,17$: $143,\ 65,\ 65,\ 17$.
- $(6,10)$, $n=20,21,22,23$: $323,\ 2261,\ 24871,\ 33649$.
- $(8,13)$, $n=26,27,28,29$: $437,\ 23,\ 23,\ 667$.

All $>1$. The claim in A2.14 that the $(6,10)$ gcds equal $V_6(n)$ itself
also verified.

### 3.5 $i=3$

- $(3,4)$, $(3,5)$, $(3,6)$ closures: proofs verified (A1.14, A2.17–A2.19);
  additionally my direct computation finds no counterexample for
  $(3,j)$, $j\in\{4,5,6,7\}$, for any $n\le2000$.
- Lemma 3 prime-power criterion spot check, $n\le300$, exhaustive over all
  relevant $q=p^a\Vert(n-r)$ and all $4\le j\le n/2$ (84,526 instances):
  $p\mid C(n,3)$ held in every case, and whenever $j\bmod q>r$ the prime
  $p$ divided $C(n,j)$ in every case. **0 violations.**
- (LD3) enumeration, my own code, $n\le1000$: **no (LD3) solutions** —
  reproducing the documents' claim (theirs: $n\le2000$ for A1, $n\le5000$
  for A2) on the mandated bounded range. The $\ge5$-only system on
  $n\le1000$ has exactly the six solutions
  $(10,5),(28,14),(82,41),(162,70),(244,122),(730,365)$, matching both
  documents; each is killed by the 3-clause as described.
- Neither document claims $i=3$ closed; both state $(H_3)$ as
  necessary-not-sufficient and as the exact remaining obstruction for the
  low-digit route. **Confirmed: no overclaim.**

### 3.6 Bounded direct verification of T1/T2/T3 conclusions

- T1: $\gcd(C(n,1),C(n,j))>1$ for all $n\le300$, all $j$: 22,201 triples, **0 failures**.
- T2: $\gcd(C(n,2),C(n,j))>1$ for all $n\le300$, all $j$: 21,904 triples, **0 failures**.
- T3: direct (not proof-mediated) check $\gcd(V_i(n),C(n,\lfloor3i/2\rfloor+1))>1$
  for **all** $i\le60$ and all $2j\le n\le400$: **0 failures** — this covers
  every exception triple in range directly, as mandated.

## 4. Final verdicts

| Theorem | Verdict |
|---|---|
| T1 ($i=1$ closed, all $j,n$) | **PROVED** |
| T2 ($i=2$ closed, all $j,n$) | **PROVED** |
| T3 (boundary family closed, all $i,n$) | **PROVED WITH CORRECTIONS** — the correction is to source S5's proviso (two in-family exception triples, not one); both proof documents already contain the corrected statement and the extra discharge, so as written in P-A1/P-A2 the theorem is fully proved. |
| T4 ($i=3$ partial results + (LD3)/(H3) obstruction) | **PROVED as stated** — $(3,4),(3,5),(3,6)$ closed for all $n$, necessity of (LD3)/(N1)/(N2) and the odd-top rigidity proved, $(H_3)$ correctly identified as the open obstruction. The general closure of $i=3$ is **NOT ESTABLISHED**, and neither document claims it. |

**Overall counts: 46 numbered items classified — 45 PROVED, 1 OPEN (A2.27 /
the H3 statement, openly flagged as unproved in both documents), 0 GAP,
0 FALSE within P-A1 and P-A2. The single FALSE claim in the material is
S5's EEES78 proviso, independently confirmed false with counterexample
$(30,7,11)$, and repaired in both proofs.**
