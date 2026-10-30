# V-I: Independent verification of Cluster I (the even residual class at $i=3$, row by row), Cycle 3

Verifier: V-I (independent). Files verified: `proofs/P-I1.md` (with
`proofs/P-I1_checks.py`) and `proofs/P-I2.md` (with `proofs/P-I2_checks.py`),
against the certified inputs both provers build on: `CYCLE2.md` §2,
`proofs/P-F1.md` (F1.7–F1.11), `proofs/P-F2.md` §§1–3 (F2.4, F2.9, F2.13,
F2.14), `verification/V-F.md`, and `proofs/P-A1.md` (A1.15, A1.16, (H3)) —
all read in full before any checking began. The two provers did not see
each other's files; this verifier treated their agreement as evidence to
be tested, never as proof.

Verifier's own computations (Python stdlib only, exact arithmetic;
implementations independent of both provers' scripts — SPF-sieve
factorisation where the provers used trial division, brute-force filtering
where P-I1 used product construction, an $n$-outer loop where P-I2 used a
$j$-outer loop): `verification/V-I_checks.py` (§§A–G; all assertions
passed; runtime 18.4 s). Running the provers' own scripts to confirm
their outputs is reported separately in §1 and is **not** counted as
independent verification anywhere below.

**Headline verdict. Both provers' central claims are CERTIFIED, and the
one substantive difference between them is adjudicated in P-I2's favour.**
(1) There is **no counterexample at $i=3$ with $T = R + 2(Q-1) \le 16$**:
a counterexample must satisfy (RES-3) **and** $T \ge 17$ (both provers,
by independent routes — P-I1 via per-row finiteness plus the certified
$j \le 5000$ frontier plus finite lists; P-I2 via the same finiteness
table plus its elimination lemma). (2) Stronger, and this is the
adjudication the brief asked for: **P-I2's claim that all 64 rows with
$T \le 16$ are closed for even (LD3) solutions themselves — not merely
for counterexamples — is PROVED** (Claims I2.7–I2.14, audited line by
line in §4 and stress-tested on $1{,}282{,}474$ candidate pairs with
zero failures). P-I1's explicit refusal to claim (LD3)-solution closure
(its Claim I4.1 precision note) is a correct statement about *its own*
Proposition 4.1 method, not a counter-argument to P-I2's (LD3)-only
method; the two files do not contradict each other, and the certified
record now contains the stronger statement. (3) Every candidate disposal
in both files was independently recomputed: P-I1's 68 candidates and
P-I2's 20 candidates are **all genuinely disposed** — no survivor, no
surviving gap (§6). (4) The (4,2) validation is confirmed exactly by both
routes (§3). **What remains OPEN, correctly labelled by both provers:
the residual class with $T \ge 17$, $(H3)_{\mathrm{even}}$ restricted to
$T \ge 17$, $i=3$ in general, and #699.** Findings against the provers
are minor only: one completeness GAP in P-I2's (RES-3) as a
*reconciliation* (its conditions are all true, but (N1) is labelled
without being stated, parity feasibility is not formalised, and the
squared half is not listed — §8), one immaterial numerical looseness in
P-I2 Claim I2.11(e), one presentational numbering gap in P-I1 (no
Claims I3.3/I3.4 exist), and an apparent — but merely definitional —
difference between the two $J_{\max}$ tables (§5.1). No claim in either
file was found FALSE as a mathematical statement, except the two
universal statements the provers themselves label FALSE and refute
(the squared-half finiteness derivation at $(2,0)$).

---

## 1. The provers' own scripts, re-run (not independent verification)

* `proofs/P-I1_checks.py`: re-run by this verifier; **all assertions
  passed** (0.7 s). Output matches the text of P-I1.md in every
  particular checked: the $\Lambda_3$ table; the $J_{\max}$ table for
  all 63 rows with $h \le 1$; the exception list
  $[(6,1),(6,2),(7,0),(7,1),(7,2),(8,0),(8,1),(8,2),(9,0)]$; the §D
  candidate lists (66 candidates over 15 rows) with gcds and (LD3)
  witnesses; the §E $R=1$ lists ($(3,1)$: none, $(5,1)$: $[(56,11)]$,
  $(7,1)$: $[(288,41)]$); the (4,2) gcds $[77, 69, 371]$.
* `proofs/P-I2_checks.py`: re-run; **all assertions passed** (0.1 s).
  Output matches the text of P-I2.md: the $B^{*}$ table for all 64 rows;
  the counts 42/21/1 for $h=0/1/2$; §B (4,2) reproduction; §C's 57 rows,
  1390 tested pairs, maximum bound 586 at $(2,14)$, exactly 20 $r=1$
  candidates each printed with its (LD3) witness; §E's hand-row lists;
  §D's $R=1$ sets and cross-check counts 5/4/3.

Everything those scripts assert was then re-derived by the verifier's
own code (§§3–7 below); the re-runs above establish only that the files'
printed numbers are the scripts' actual outputs.

## 2. Claim-by-claim tables

### 2.1 P-I1

| Claim | Status | Verifier's note |
|---|---|---|
| I1.1 (RES-3) | **PROVED** as a necessary-condition assembly; class **OPEN** as labelled | Every condition re-derived from F1.7–F1.10/F2.4/F2.9/F2.13/F2.19 and A1.16 (see §8). This is the correct complete reconciliation of F1.11/F2.14. |
| D1–D9 (discrepancies) | **PROVED** (accurate) | Each checked against the F files (§8). D3 (removing $(4,2)$ at reconciliation) is a judgement call, justified: the disposal is V-F-certified (§5 of V-F) and independently reproduced by both provers (§3 below). |
| I2.1 (analytic bounds $B_0$, $B_1$) | **PROVED** | Proof audited: (a) $C(n,3) > (n-2)^3/6$ step sound; (b) the $0.72$ factor at $x = Qj \ge 10$ sound. Bounds additionally verified in exact integer arithmetic for all 63 rows (script §B: integer cube root for $B_0$; exact `Fraction` ceilings for $B_1$; first integer at/above each bound infeasible, $J_{\max}+1$ at/below it). Spot value confirmed: $B_1(5,1) = 6615$ vs exact $J_{\max} = 4762$. |
| I2.2 (threshold monotonicity) | **PROVED** | Proof of (b) audited line by line: the factor bound $(1+Q/n)^3$, the estimates $\ln(1+x) > x/(1+x)$, $\ln(1+y) < y$, and the reduction to $Q(j-2) > 2R$ (which holds since $R \le 2$, $Q \ge 2$, $j \ge 5$ give $Q(j-2) \ge 6 > 4 \ge 2R$) are all correct. Independent exact check of $f(j+1) > f(j)$ for **every** $j$ in range for the 15 $h=1$ rows with $J_{\max} \le 400{,}000$ (including $(6,1), (6,2), (7,0)$), and sampled ($j < 5000$, stride 9973, $J_{\max}$ window) for the remaining six — zero failures. |
| I2.3 (universal finiteness **FALSE** at $(2,0)$) | Refutation **PROVED**; the universal statement is **FALSE**, as self-labelled | Ratio identity $\binom j2^2/C(2j,3) = 3j(j-1)/(8(2j-1))$ and the equivalence with $3j^2 - 19j + 8 > 0$ verified exactly for $5 \le j \le 500$ (script §C): the squared inequality at $(2,0)$ holds iff $j \ge 6$, hence yields no bound. $(2,0)$ stays closed by Price's central case (standing input), not by size. |
| I2.4 ($J_{\max}$ table, $T \le 16$) | **PROVED** (computation, fully recounted) | All 63 values reproduced **exactly** by the verifier's own binary search under P-I1's definition (exact $n = Qj+R$, $j \ge 5$, sentinel $J_{\max} = 4$): script §B. Exactly 54 of 63 have $J_{\max} \le 5000$; the nine exceptions are exactly $(6,1),(6,2),(7,0),(7,1),(7,2),(8,0),(8,1),(8,2),(9,0)$; $(6,1)$ and $(8,1)$ are parity-vacuous. Required-row detail in §5.2. |
| Cor. I2.5 (54 rows contain no counterexample) | **PROVED**, modulo the certified frontier F2.19 (standing input, V-F-certified) | Deduction sound. The three rows with $J_{\max} = 4$ — exactly $(2,3), (2,4), (3,0)$ in the recount — need no frontier input (no $j \ge 5$ is even feasible). The claim's own scope warning (the nine exceptions are only bounded, not closed, by §2) is accurate. |
| Lemma I3.1 (non-special-top prime powers $\le T$) | **PROVED** — the sharpening is **valid as stated** | Full audit in §5.3. |
| Lemma I3.2 (finite form set $M(T)$) | **PROVED** | Proof audited (cases (a)/(b)/(c); the $v_2 = 1$ top argument in (c) and the bound $n \le 6\Lambda_3(T) + 2$ are correct). Sizes independently brute-verified: $\lvert M(6)\rvert = 6$, $\lvert M(8)\rvert = 12$, $\lvert M(10)\rvert = 16$, $\lvert M(12)\rvert = 32$, $\lvert M(14)\rvert = \lvert M(16)\rvert = 64$, by filtering all odd $m \le 3\Lambda_3(T)$ through the defining conditions (a different construction from the prover's product build); $m \le 3\Lambda_3(T)$ confirmed for every member. |
| I3.5 ((4,2) validation, FINITE LIST) | **PROVED** | §3 below: two independent enumerations, gcds $77, 69, 371$, witnesses at $r = 0$. Matches F1.11 and V-F §5 in every particular. |
| I3.6 (2,4), I3.7 (2,6), I3.8 (3,4), I3.10 (4,4), I3.13 (2,8), I3.14 (6,0) (FINITE LISTs) | **PROVED** | Candidate lists regenerated from the verifier's brute-built $M(T)$ sets; every gcd recomputed and equal to the printed value; every candidate independently shown to fail (LD3) by an explicit witness (§6). Counts 2, 6, 5, 5, 9, 1. I3.8 is correctly proved at the corrected $T = 8$ (the brief's $T = 7$ annotation is indeed wrong, and $\Lambda_3(7) = \Lambda_3(8)$ makes it immaterial there). |
| I3.9 ((3,1) CLOSED) | **PROVED** | Hand argument audited: $j$ odd is forced, neither non-special top is divisible by 3, so each odd part lies in $\{1, 5\}$ (the only $\ge 5$ prime power $\le T = 5$ is $5^1$), the $v_2 = 1$ top is $\le 10$, $n \le 12 < 16 \le n$ — contradiction. The generic case-(c) filter to $n \le 92$ independently returns zero candidates (verifier's §D recount). |
| I3.11 ((5,0) CLOSED), I3.12 ((5,2) CLOSED) | **PROVED** | Empty candidate lists reproduced. Hand checks verified against the brute $M$ sets: in $M(8)$ only $m = 9$ is $\equiv 4 \pmod 5$ (giving $j = 2$); in $M(10)$ only $m = 1, 21$ are $\equiv 1 \pmod 5$ (giving $j = 0, 4$). I3.12 is correctly proved at the corrected $T = 10$ (brief's $T = 8$ annotation wrong; the prover's correction is right and material to the form set, as stated). |
| I3.15 ((5,1)), I3.16 ((6,2)), I3.17 ((7,0)), I3.18 ((7,1)), I3.19 ((7,2)), I3.20 ((8,0)), I3.21 ((8,2)), I3.22 ((9,0)) (FINITE LISTs) | **PROVED** | All lists regenerated and all candidates independently disposed (§6). Counts 1, 2, 1, 1, 4, 14, 13, 1. I3.20's note is confirmed: its largest candidate $(135136, 16892)$ has $j = 16892 > 5000$ (beyond the per-pair frontier) and $n = 135136 \le 10^6$, and fails (LD3) at $q = 27 \Vert (n-1)$, $16892 \bmod 27 = 17 > 1$ (verifier's witness agrees with the text). |
| I3.23 (assembly: no counterexample with $T \le 16$) | **PROVED** | Row-by-row coverage audit in §7: the case split (Price row / parity / Corollary I2.5 / Claims I3.16–I3.22) is exhaustive over the 64 rows. |
| I4.1 ((H3)-even **OPEN**; precision note) | **OPEN**, correctly labelled; the precision note is **correct** | P-I1's §§2–3 do rest on Proposition 4.1 (a counterexample hypothesis), so they do not by themselves prove (LD3)-solution closure for any row; the note's caveat about (LD3) solutions outside its candidate sets is exactly right. Superseded as a statement about the *combined* record by P-I2's §3 (see §4.4) — P-I1 does not claim otherwise. |
| I4.2 ((RES-3) after Cluster I) | **PROVED** (assembly) | Shrinkage items 1–5 all verified: (4,2) removed; 54 rows removed by §2, of which exactly 5 were already excluded from (RES-3) and 14 of the remaining 49 are also parity-vacuous; the seven non-vacuous exceptions removed by §3 with candidate counts 2, 1, 1, 4, 14, 13, 1; per-row finiteness general for $h \le 1$. |
| §5 closing / §6 verification log | **PROVED** as a summary | Matches the audited claims. "68 candidates in total" confirmed: 66 in the odd-top rows (§D) + 2 in the $R = 1$ rows (§E). Numbering note: there are no Claims I3.3/I3.4 — §3's numbering jumps from Lemma I3.2 to Claim I3.5. Presentational only; nothing is missing (the §3.1/§3.2 structure accounts for the jump). |

### 2.2 P-I2

| Claim | Status | Verifier's note |
|---|---|---|
| I2.1 (RES-3) | **PROVED** as a necessary-condition statement; **GAP (minor, completeness only)** as a reconciliation | Every condition stated is true and necessary (checked against F1.11/F2.14/F2.19/A1.16). But as the *single reconciled* statement it is less complete than P-I1's I1.1 in four items: (i) item (d) is labelled "(N1) and (N2)" yet states only (N2)'s content $V_3(n) \mid C(j,3)$ — (N1) itself never appears; (ii) parity feasibility is not formalised (only the $(2,1)$ remark inside discrepancy D1); (iii) the squared half of Proposition 4.1 is not listed as a residual condition (it is used in §2 instead); (iv) $(4,2)$ is retained in the residual (closed later, in I2.10/§3, so the file's final position agrees with P-I1's). None of these makes any stated condition false; see §8 for the itemised adjudication. |
| I2.2 ($h = 0$ finiteness) | **PROVED** | $(Qj-2)^3 < 6\Lambda^2$ step audited; bound verified in exact integer arithmetic for all 42 $h = 0$ rows (script §B). |
| I2.3 ($h = 1$ finiteness, $\varphi$ form) | **PROVED** | Algebra audited: $C(Qj,3)/j^2 = \frac{Q}{6}(Q^2j - 3Q + 2/j)$, $\varphi(j+1) - \varphi(j) = \frac{Q}{6}(Q^2 - \frac{2}{j(j+1)}) > 0$ for $Q \ge 2$; closed-form bound $j < 6\Lambda^2/Q^3 + 3/Q$ verified exactly for all 21 $h = 1$ rows. |
| I2.4 (universal finiteness **FALSE** at $h = 2$) | Refutation **PROVED**; universal statement **FALSE**, as self-labelled | $C(2j,3)/\binom j2^2 = 8(2j-1)/(3j(j-1)) \to 0$ (the reciprocal of P-I1's ratio; identity verified exactly, §C of the verifier's script), so $(\ast)$ holds for all large $j$ at $(2,0)$. |
| I2.5 ($B^{*}$ table, $T \le 16$) | **PROVED** (computation, fully recounted) | All 63 $B^{*}$ values reproduced **exactly** by the verifier's own binary search under P-I2's definition (the majorant $(\ast)$ with $C(Qj,3)$, $j \ge 1$). Counts confirmed: 42 $h = 0$ rows all with $B^{*} \le 1151$; the 12 $h = 1$ rows with $B^{*} \le 5000$ and the 9 with $B^{*} > 5000$ are exactly the lists printed. See §5.1 on why this table differs entry-by-entry from P-I1's without either being wrong. |
| I2.6 (scope of §2) | **PROVED** | Counts verified: 54 rows with $B^{*} \le 5000$, minus the 4 already-closed rows among them $((2,2),(3,0),(3,2),(4,0))$ = **50 rows of (RES-3) removed for counterexamples** (all 42 $h = 0$ rows + the 8 listed $h = 1$ rows). The (i)/(iii) scope warnings (EEES78 dependence; nothing about bare (LD3) solutions; the 9 large rows not closed by §2) are accurate. |
| I2.7 (elimination lemma) | **PROVED** | Line-by-line audit and a 200,000-limit computational stress test in §4: 1,492,091 assignment-group instances, **0 divisibility failures**; aligned cases exactly as classified. |
| I2.8 ($R \ne 1$ corollary: $R(n-1) \mid (R-1)(Q+R-1)$) | **PROVED** | Proof audited (both $D_{1,0} = R-1 \ne 0$ and $D_{1,1} = Q+R-1 \ge 1$ are nonzero; $n - 1 \in \{R(n-1), 3R(n-1)\}$ for odd $n-1$ is correct). Stress test: on all 55 candidate pairs with $n \le 200{,}000$ passing the $r = 0$ and $r = 1$ clauses with $R \ne 1$, the divisibility holds — 0 failures (§4.3). |
| I2.9 ($R = 1$ finite reduction) | **PROVED** | Proof audited: $D_{0,0} = 1$ forces $R(n) = 1$, hence $n = 2^a 3^b$, $a \ge 1$, $b \le 1$; at $t = 2$ all three $D_{2,s} \in \{-1, Q-1, 2Q-1\}$ are nonzero, giving $R(n-2) \mid (Q-1)(2Q-1)$ (the $s = 0$ group divides $-1$, hence is 1 — the text's suppression of $G_{2,0}$ is justified); the odd-part formulas $2^{a-1} - 1$ / $3 \cdot 2^{a-1} - 1$ for $a \ge 2$ are correct. Stress test: all 83 $R = 1$-row candidate pairs with $n \le 200{,}000$ have $R(n) = 1$ (0 exceptions). One honesty note: **no** $R = 1$-row pair in that range passes the full $r = 2$ clause, so the $R(n-2)$ product divisibility had 0 corollary-level test instances — it is computationally vacuous there and rests on the (audited) proof plus the group-level instances of §4.2, not on direct instances. |
| I2.10 ((4,2) validation) | **PROVED** | §3 below. Reproduced by the *original* F1.11 argument, exactly as claimed. |
| I2.11 (hand closures, $R \ne 1$ rows) | **PROVED** | All eight rows re-derived by the verifier from the $P(D)$ group-product sets (a route independent of P-I2's scan): candidate lists $(2,4)$: $[(16,6)]$; $(3,4)$: $[]$; $(2,6)$: $[(16,5),(22,8),(36,15),(106,50)]$; $(4,4)$: $[]$; $(5,0)$: $[]$; $(5,2)$: $[]$; $(2,8)$: $[(22,7),(64,28)]$; $(6,0)$: $[]$ — all match the text, including the $3 \nmid \rho$ rule that excludes $27 = 3 \cdot 9$ and $189 = 3 \cdot 63$ at $(2,8)$. Every listed candidate independently has a full (LD3) witness. One immaterial slip: at (e) ($(5,0)$) the text says $n - 1 \ge 29$ "for admissible even $n$ ($j$ even)"; with the section's stated $j > 3$ alone the bound is $n - 1 \ge 19$ ($j = 4$ gives $n = 20$); $\ge 29$ needs $j \ge 5$. The conclusion is unaffected (the $\rho$-set forces $n - 1 \in \{1, 3\}$ either way). |
| I2.12 ($R = 1$ rows, $T \le 16$) | **PROVED** | The four even-$Q$ rows are parity-vacuous as stated. For $Q = 3, 5, 7$ the verifier recomputed $P(Q-1) = \{1\}$ in all three cases, $P(2Q-1) = \{1,5\}, \{1,9\}, \{1,13\}$, the $R(n-2)$ sets and the odd-part sets $\{1,3,5,15\}, \{1,3,9\}, \{1,3,13,39\}$ — all match; the case analyses on $a, b$ were audited (including the exclusion of $27 = 3 \cdot 9$ at $Q = 5$); clause cross-check counts 5/4/3 reproduced with 0 forms passing the $r = 0$ and $r = 2$ clauses simultaneously. |
| I2.13 (all 57 $R \ne 1$ rows closed for (LD3)) | **PROVED** (computation, fully recounted) | Verifier's independent scan ($n$-outer loop, SPF clause tests): 57 rows, **1390** even pairs tested to the per-row I2.8 bounds, maximum bound **586** at $(2,14)$ — all three figures match. Exactly **20** $r = 1$-clause candidates, the identical list to the text (§6.2); each independently disposed by a full (LD3) witness; **0 survivors**. |
| I2.14 (all $T \le 16$ rows closed for the even class) | **PROVED** | Assembly is exhaustive: $57$ rows ($R \ne 1$, I2.13) $+$ $7$ rows ($R = 1$: 4 parity-vacuous, 3 closed in I2.12) $= 64$. The claim is about **(LD3) solutions themselves** and needs no EEES78 and no Proposition 4.1 — verified as such. This is the cluster's strongest certified statement; see the adjudication in §4.4. |
| I2.15 ($(H3)_{\mathrm{even}}$ reduced to $T \ge 17$, **OPEN**) | **OPEN**, correctly labelled; reduction **PROVED** | Surviving-region arithmetic verified: $T \ge 17 \iff$ $Q = 2, R \ge 15$; $Q = 3, R \ge 13$; $Q = 4, R \ge 11$; $Q = 5, R \ge 9$; $Q = 6, R \ge 7$; $Q = 7, R \ge 5$; $Q = 8, R \ge 3$; $Q = 9, R \ge 1$; $Q \ge 10$, any $R \ge 0$. The itemised shrinkage (50 rows by §2 for counterexamples; all 59 (RES-3) rows by §3; the 9 genuinely-new-at-§3 rows, with no $r = 1$ candidates in the six $R \ne 1$ ones — confirmed against the recount) is accurate. |
| I2.16 (what is not proved) | **PROVED** as a scope statement | Accurate: (H3) in full, its odd half as a pure (LD3) statement, $i = 3$ in general, and #699 all remain open; the distinction drawn between odd *counterexamples* (closed, via Proposition 4.1) and odd *(LD3) solutions* (not excluded in general) is correct. |
| §5 closing / §6 verification log | **PROVED** as a summary | Matches the audited claims and the re-run script output (the script's internal section order is A, B, C, E, D; the log describes the same content). |

## 3. Task 2 — the (4,2) validation, independently confirmed

For $(Q, R) = (4, 2)$: $T = 8$, $\Lambda_3(8) = 105$, $V_3(n) \mid 105j$,
$n - 1 = 4j + 1$. The verifier enumerated the candidates by **two**
routes independent of each other and of both provers' code
(script §G):

* (i) the original F1.11 form enumeration: $m = 3^b 5^a 7^c$ with
  $b \le 2$, $a, c \le 1$, $m \equiv 1 \pmod 4$, $j = (m-1)/4 \ge 5$;
* (ii) P-I1's $M(T)$ route, with $M(8)$ built by the verifier's
  brute-force filter (12 values).

Both leave **precisely** $(n, j) = (22, 5), (46, 11), (106, 26)$
($m = 21, 45, 105$) — no others. For each, the verifier recomputed
$$\gcd(V_3(n), C(n, j)) = 77,\ 69,\ 371 \quad\text{respectively},$$
and each carries an explicit (LD3) violation already at the top $n$
itself ($r = 0$): $q = 11 \Vert 22$ with $5 \bmod 11 = 5 > 0$;
$q = 23 \Vert 46$ with $11 \bmod 23 = 11 > 0$; $q = 53 \Vert 106$ with
$26 \bmod 53 = 26 > 0$. This confirms, digit for digit, F1.11's
illustration, V-F §5, P-I1 Claim I3.5, and P-I2 Claim I2.10. **Both
provers' methods pass the mandatory validation exactly.** (For the
record: P-I2's *elimination* scan is a different instrument and finds
no $r = 1$ candidate in row $(4,2)$ at all — its I2.8 bound there is
$n \le 16$ — which is consistent, since the three pairs above are
counterexample-candidates of the Proposition 4.1 argument, not (LD3)
near-solutions; they fail (LD3) at $r = 0$ already.)

## 4. Task 3 — P-I2's elimination lemma: the crux, audited and stress-tested

### 4.1 Line-by-line audit of Claim I2.7

Setup: $(n, j)$ satisfies (LD3), $n = Qj + R$; $G_{t,s}$ is the product
of the relevant prime powers $q \Vert (n - t)$ with $j \bmod q = s$.

* **The equivalence "$j \bmod q = s \iff q \mid j - s$":** correct.
  Relevant $q$ satisfy $q \ge 5$ (either $p \ge 5$, or $p = 3$ with
  $a \ge 2$ giving $q \ge 9$), and $0 \le s \le t \le 2 < q$, so
  $j \equiv s \pmod q$ is the same as $j \bmod q = s$. (The text's
  "$\le 2 < 3 \le q$" in part (i) is weaker than the truth $q \ge 5$
  but sufficient.)
* **(i) Partition:** correct. (LD3) assigns every relevant $q$ of the
  top $n - t$ some $s \in \{0, \dots, t\}$; uniqueness follows from
  $q \mid |s_1 - s_2| \le 2 < q$ for two putative assignments; the
  $q$'s are pairwise coprime (distinct primes), so
  $R(n - t) = \prod_s G_{t,s}$.
* **(ii) Divisibility:** correct. Each $q$ in the group divides both
  $n - t$ and $j - s$, hence divides the integer combination
  $(n - t) - Q(j - s) = Qj + R - t - Qj + Qs = Qs + R - t = D_{t,s}$
  (algebra rechecked). Pairwise coprimality upgrades the individual
  divisibilities to $G_{t,s} \mid D_{t,s}$ whenever $D_{t,s} \ne 0$.
  Negative $D_{t,s}$ (e.g. $D_{2,0} = -1$ at $R = 1$) is handled
  correctly — divisibility is in $\mathbb{Z}$.
* **(iii) Aligned cases:** correct and exhaustive. $D_{t,s} = Qs + R - t
  = 0$ with $Qs + R = t \le 2$, $Q \ge 2$: either $s = 0$ and $R = t$,
  or $s \ge 1$ forces $Qs \le 2$, i.e. $(Q, R, t, s) = (2, 0, 2, 1)$.
  No other case exists.
* **Downstream hygiene:** the aligned cases are never silently used.
  Claim I2.8 works at $t = 1$ under the hypothesis $R \ne 1$, which is
  exactly what makes $D_{1,0} = R - 1 \ne 0$ (and $D_{1,1} = Q + R - 1
  \ge 1$ always). Claim I2.9 works at $t = 0$ (where $D_{0,0} = R = 1
  \ne 0$) and $t = 2$ at $R = 1$ (where no $D_{2,s}$ vanishes). The
  exceptional aligned case $(2, 0, 2, 1)$ sits in a row with $R = 0$,
  where only the $t = 1$ corollary is ever applied. **The proof is
  sound; the lemma is PROVED.**

### 4.2 Stress test of the *statement* (independent implementation)

Design (script §F): SPF sieve to $200{,}000$; for every even $n \le
200{,}000$, (LD3) candidate pairs $(n, j)$ enumerated via multiples of
$R(n)$ ($j > 3$, $j \le n/2$ — the $r = 0$ clause is then automatic, as
(LD3) requires); for each pair, with $(Q, R)$ from $n = Qj + R$, every
relevant prime power of every top $n - t$ with an (LD3)-consistent
assignment ($s = j \bmod q \le t$) was grouped into $G_{t,s}$, and the
conclusion $G_{t,s} \mid D_{t,s}$ ($D_{t,s} \ne 0$) and the aligned-case
classification ($D_{t,s} = 0$) were checked. Results:

| Quantity | Count |
|---|---|
| Candidate pairs tested | **1,282,474** |
| Assignment-group instances $G_{t,s}$ checked | **1,492,091** |
| — of which $D_{t,s} \ne 0$: divisibility **failures** | **0** (of 1,125,632) |
| — of which aligned ($D_{t,s} = 0$) | 366,459 |
| — aligned instances outside the classified cases $\{(s = 0, R = t)\} \cup \{(2,0,2,1)\}$ | **0** |
| Full (LD3) solutions found | **0** (as certified: none exist with $n \le 10^6$) |

The statement survived every instance. (The group-level test is the
right granularity: the divisibility $q \mid D_{t,s}$ is pure arithmetic
given $q \mid (n - t)$ and $q \mid (j - s)$; (LD3) is what guarantees
the assignment exists for *every* relevant $q$, which is the form in
which I2.8/I2.9 consume it.)

### 4.3 The corollaries on the same range

* **I2.8 corollary** $R(n-1) \mid (R-1)(Q + R - 1)$ for $R \ne 1$:
  verified on **all 55** candidate pairs with $n \le 200{,}000$ that
  pass the $r = 0$ and $r = 1$ clauses and land in an $R \ne 1$ row
  (the exact hypothesis the corollary needs at $t = 1$) — **0
  failures**. (62 pairs pass the $r = 1$ clause in total; 7 of them
  are in $R = 1$ rows, where the corollary does not apply.)
* **I2.9, $R = 1$ reduction:** all **83** candidate pairs landing in
  $R = 1$ rows have $R(n) = 1$ — **0 exceptions** — confirming the
  first conclusion ($n = 2^a 3^b$, $b \le 1$) on every available
  instance. The second conclusion ($R(n-2) \mid (Q-1)(2Q-1)$) had **0
  corollary-level instances** in range, because no $R = 1$-row pair
  passes the full $r = 2$ clause; its support is the audited proof
  plus the $t = 2$ group-level instances of §4.2. Recorded here so the
  computational support is not overstated.

### 4.4 Adjudication of the P-I1 / P-I2 difference

P-I1 (Claim I4.1) states, correctly, that *its* closures rest on
Proposition 4.1 and therefore speak about counterexamples, not about
bare (LD3) solutions; it claims no (LD3)-solution closure for any row.
P-I2 (Claims I2.7–I2.14) claims (LD3)-solution closure for **all**
$T \le 16$ rows, by an argument that uses (LD3) alone. These are
compatible statements about *different methods*, and the question for
the record is whether P-I2's stronger claim holds. **It does**: the
elimination lemma's proof is sound (§4.1), its corollaries are sound
(I2.8, I2.9), the finite disposals are fully recounted (I2.11, I2.12,
I2.13 — §6.2), and the lemma's statement survived 1.49 million
independent group instances without a failure (§4.2). The certified
record therefore adopts P-I2's stronger conclusion; P-I1's caution is
preserved as a correct description of P-I1's own route, and nothing in
P-I1 asserts the contrary.

## 5. Task 4 — P-I1's finiteness, the $(2,0)$ refutation, and Lemma I3.1

### 5.1 Why the two $J_{\max}$ tables differ (definitional, not an error)

P-I1's $J_{\max}(Q, R)$ is the largest $j \ge 5$ satisfying the squared
inequality with the **exact** $n = Qj + R$ (sentinel $4$ if none),
while P-I2's $J_{\max}$ (with $B^{*} = J_{\max} + 1$) is the largest
$j \ge 1$ satisfying the **majorant** $(\ast)$ with $C(Qj, 3)$ in place
of $C(n, 3)$. P-I2's is a valid but weaker bound ($C(Qj, 3) \le C(n,
3)$); P-I1's is sharper. The verifier recomputed **both full tables**
under each prover's own definition: **all 63 + 63 values match the two
texts exactly**. The exception sets coincide exactly (the same nine
rows exceed 5000 under both definitions), as do the counts at/below
5000 (54 under both). No discrepancy of substance exists here; the
tables must not be compared entry-by-entry across files without the
definitions.

### 5.2 Required rows, recomputed exactly

| Row | P-I1 $J_{\max}$ (exact $n$) | P-I2 $J_{\max}$ for $(\ast)$ ($B^{*}$) |
|---|---|---|
| (5,1) | 4762 ✓ | 4763 (4764) ✓ |
| (6,1) | 333506 ✓ | 333506 (333507) ✓ |
| (6,2) | 333505 ✓ | 333506 (333507) ✓ |
| (7,0) | 210021 ✓ | 210021 (210022) ✓ |
| (7,1) | 35493621 ✓ | 35493621 (35493622) ✓ |
| (7,2) | 35493620 ✓ | 35493621 (35493622) ✓ |
| (8,0) | 23777953 ✓ | 23777953 (23777954) ✓ |
| (8,1) | 23777953 ✓ | 23777953 (23777954) ✓ |
| (8,2) | 23777953 ✓ | 23777953 (23777954) ✓ |
| (9,0) | 16700016 ✓ | 16700016 (16700017) ✓ |
| (2,14) | 1143 ✓ | 1150 (1151) ✓ |
| (3,12) | 763 ✓ | 767 (768) ✓ |

(✓ = reproduced by the verifier's own binary search, with endpoint
assertions feasible($J_{\max}$) / infeasible($J_{\max} + 1$).) The
claim that **exactly nine** $h \le 1$ rows at $T \le 16$ have threshold
$> 5000$ — $(6,1), (6,2), (7,0), (7,1), (7,2), (8,0), (8,1), (8,2),
(9,0)$ — is **confirmed under both definitions**, as is the
parity-vacuity of $(6,1)$ and $(8,1)$ ($Q$ even, $R$ odd: no even $n$).
Bounds $B_0, B_1$ and the monotonicity lemma: §2.1 table, Claims
I2.1/I2.2 rows.

### 5.3 The $(2,0)$ refutation and Lemma I3.1 vs F1.9/F2.4

* **$(2,0)$, $h = 2$:** both provers are right and agree in substance.
  The squared inequality there is $C(2j, 3) < \binom j2^2$ with
  $\Lambda_3(2) = 1$; the verifier confirmed the exact ratio identities
  in both orientations and that the inequality **holds for all
  $j \ge 6$** (P-I1's form: iff $3j^2 - 19j + 8 > 0$). It therefore
  entails no bound — the universal per-row finiteness *derivation from
  the squared half* is indeed FALSE at this single row, as both files
  state. The row is closed by Price's central case, a standing input.
* **Lemma I3.1 (the sharpening): VALID as stated.** F1.9(b), as filed,
  bounds prime *factors* $p > T$ of non-special tops, and F2.4 gives
  the per-part dichotomy ($P \le T$ or $P \mid j - r$, $r < h$) for the
  $V_3$-parts. P-I1's step — for $p \ge 5$ the $V_3$-part *is* the
  exact prime power $P = p^a \Vert t$ of the top (V-F-certified), so
  the dichotomy applies to $P$ itself; the alternative $P \mid j$ is
  impossible for a non-special top because $P \mid t = Qj + (R - r_0)$
  as well, forcing $P \mid R - r_0$ with $0 < |R - r_0| \le 2 < 5 \le
  P$ — is correct, and it genuinely sharpens F1.9(b) from primes to
  prime powers (it disposes of the case $p \le T < p^a$ that F1.9(b)
  leaves open). Part (b) (the 3-part) is also correct: the $V_3$
  3-part is $3^{e-1}$, exactly the quantity F2.4's dichotomy governs
  (one factor of 3 below the (LD3) power, as V-F recorded), and
  $\gcd(j, t) \mid |R - r_0| \le 2$ excludes $3 \mid j$, killing the
  divisibility alternative when $e \ge 2$ (for $e \le 1$ the claim
  $3^{e-1} \le T$ is trivial). No gap found.

## 6. Task 5 — candidate disposals, all independently recomputed

### 6.1 P-I1's 68 candidates

The verifier regenerated every candidate list from its own brute-built
$M(T)$ sets (rows via $n - 1 \in M(T)$) and its own $R = 1$ enumeration
(odd-part filters to $n \le 6\Lambda_3(T) + 2$), then recomputed every
$\gcd(V_3(n), C(n, j))$ and every (LD3) witness with its own SPF-based
code (script §D). **All 18 row lists match P-I1's text exactly**
(including the three empty lists $(3,1), (5,0), (5,2)$); **all 68
gcds match the printed values**; **every one of the 68 candidates
independently fails (LD3)** by an explicit witness. Per-row counts:
$(4,2)$: 3; $(2,4)$: 2; $(2,6)$: 6; $(3,4)$: 5; $(4,4)$: 5; $(2,8)$: 9;
$(6,0)$: 1; $(5,1)$: 1; $(6,2)$: 2; $(7,0)$: 1; $(7,1)$: 1; $(7,2)$: 4;
$(8,0)$: 14; $(8,2)$: 13; $(9,0)$: 1 — total **68, all disposed, no
survivor**.

### 6.2 P-I2's 20 candidates

The verifier's independent scan of the 57 rows with $R \ne 1$
($n$-outer loop; per-row bound $n \le 3|(R-1)(Q + R - 1)| + 1$ from
Claim I2.8) tested **1390** even pairs and found exactly the same
**20** $r = 1$-clause candidates as P-I2 Claim I2.13:

$(2,4)$: $(16,6)$; $(2,6)$: $(16,5), (22,8), (36,15), (106,50)$;
$(2,8)$: $(22,7), (64,28)$; $(2,10)$: $(34,12), (100,45)$;
$(2,12)$: $(34,11), (40,14), (144,66), (430,209)$;
$(2,14)$: $(40,13), (66,26), (196,91)$; $(3,12)$: $(78,22)$;
$(4,6)$: $(46,10)$; $(4,8)$: $(232,56)$; $(4,10)$: $(118,27)$.

Each of the 20 was independently disposed by a full (LD3) witness
(e.g. $(430, 209)$ fails at $q = 5 \Vert 430$, $r = 0$; $(196, 91)$ at
$q = 49 \Vert 196$, $r = 0$; $(100, 45)$ at $q = 25 \Vert 100$,
$r = 0$ — agreeing with the witnesses P-I2 names). The other 47 rows
have no $r = 1$ candidate. **All 20 disposed, 0 survivors.** P-I2's
hand-derived lists (Claim I2.11) and its scan agree with each other
and with the recount on every shared row.

**Conclusion for Task 5: no candidate in either file survives. There
is no surviving gap to name.**

## 7. Task 6 — row coverage audit and the final certified residual

The verifier enumerated all $(Q, R)$ with $Q \ge 2$, $R \ge 0$,
$T = R + 2(Q - 1) \le 16$: **exactly 64 rows** — $Q = 2$: 15,
$Q = 3$: 13, $Q = 4$: 11, $Q = 5$: 9, $Q = 6$: 7, $Q = 7$: 5,
$Q = 8$: 3, $Q = 9$: 1 — matching the brief's expected counts. Of
these, **16 are parity-vacuous** for even $n$ ($Q$ even, $R$ odd), and
5 were already closed before this cycle ($(2,0)$ by Price; $(2,2),
(3,0), (3,2), (4,0)$ by F1.10). Row by row, the **union** of the two
provers' certified closures covers **all 64 rows**, in fact with
redundancy:

* **(LD3)-solution closure (P-I2, EEES-free): all 64 rows.** 57 rows
  with $R \ne 1$ by the I2.8 bound + the recounted scan (20 candidates,
  all disposed); 7 rows with $R = 1$ by parity vacuity ($Q$ even: 4
  rows) and Claim I2.12 ($Q = 3, 5, 7$). This subsumes every
  counterexample closure below.
* **Counterexample closure (P-I1, independent route): all 64 rows.**
  $(2,0)$ by Price; the 54 rows with $J_{\max} \le 5000$ by the squared
  half + the certified $j \le 5000$ frontier (Corollary I2.5) — this
  includes the four F1.10 rows and $(4,2)$; the 9 exceptions split as
  2 parity-vacuous ($(6,1), (8,1)$) + 7 closed by the finite lists of
  Claims I3.16–I3.22. P-I1 additionally gives frontier-free structural
  disposals of 10 further rows (§3 of P-I1) that overlap the
  frontier route.

**Final certified residual, stated exactly.**

* *For counterexamples at $i = 3$:* a counterexample $(n, 3, j)$ must
  satisfy **(RES-3)** in the reconciled form of P-I1 Claim I1.1 (§8)
  **and** $$T = R + 2(Q - 1) \ge 17.$$ In row coordinates (P-I2 Claim
  I2.15, verified): $Q = 2, R \ge 15$; $Q = 3, R \ge 13$; $Q = 4,
  R \ge 11$; $Q = 5, R \ge 9$; $Q = 6, R \ge 7$; $Q = 7, R \ge 5$;
  $Q = 8, R \ge 3$; $Q = 9, R \ge 1$; $Q \ge 10$, any $R \ge 0$
  (always with $R < j$, $n$ even, $j \ge 5001$, $n > 10^6$,
  $v_2(C(n, 3)) \ge 4$). This class is **OPEN**.
* *For (LD3) solutions (a separate, stronger statement):* it is now
  certified that **(LD3) has no solution $(n, j)$ with $n$ even and
  $3 < j \le n/2$ in any row with $T \le 16$, for any $j$** (P-I2
  Claim I2.14). Together with the Cycle 2 computations (no (LD3)
  solution with $n \le 10^6$ at all; none with $5 \le j \le 5000$ in
  the finite-reduction range), an even (LD3) solution, if one exists,
  must lie in a $T \ge 17$ row with $n > 10^6$. $(H3)_{\mathrm{even}}$
  is thereby reduced to the $T \ge 17$ region and remains **OPEN**
  there.

## 8. Task 7 — RES-3 reconciliation

Both provers reconciled F1.11 and F2.14; their agreements and
differences, with the verifier's ruling on each:

**Agreed by both (and verified correct):** the frontier is
$j \ge 5001$ (F2.14's internal $j \ge 159$ is superseded by F2.19 —
P-I1's D1, P-I2's D2); the pre-closed rows are F1.11's sharper list
$\{(2,0), (2,2), (3,0), (3,2), (4,0)\}$ (P-I1's D2, P-I2's D1); F1.7
and F1.8 are included (P-I1's D5, P-I2's D5); in $h = 0$ rows the
3-part bound and the gcd form $V_3(n) \mid \gcd(C(j, 3),
\Lambda_3(T))$ are both stated (P-I1's D6, P-I2's D3); (LD3), (N2),
and the Proposition 4.1 divisibility are common ground. Both also
correctly record the brief's two $T$ slips ($(3,4)$ is $T = 8$, not
7; $(5,2)$ is $T = 10$, not 8).

**Conditions one includes and the other omits (or states more
weakly):**

1. **$(4,2)$ exclusion.** P-I1 excludes $(4,2)$ already in (RES-3)
   (its D3); P-I2 retains it in (RES-3) and closes it in §3. *Ruling:*
   P-I1's form is the sharper correct one — the row's complete
   candidate set is disposed and the disposal is V-F-certified and
   doubly reproduced (§3) — but P-I2's is not false (a residual class
   may conservatively retain a disposed row), and the two files'
   *final* residuals agree. No mathematical error on either side.
2. **Parity feasibility.** P-I1 states it generally (if $Q$ even then
   $R$ even; if $Q$ odd then $j \equiv R \pmod 2$ — derivation from
   $n = Qj + R$ even rechecked; 16 of the 64 rows are vacuous under
   it). P-I2 has no such formal item, mentioning only $(2,1)$ inside
   its D1. *Ruling:* P-I1 is correct and more complete; P-I2's
   statement remains true (the condition is implied by its "$n$
   even"), just less explicit.
3. **The squared half as a listed condition.** P-I1 lists
   $C(n, 3) < (\Lambda_3(T)\binom jh)^2$ inside (RES-3) (item 6);
   P-I2 lists only the divisibility half (item (e)) and deploys the
   squared half separately in §2. *Ruling:* P-I1 more complete; the
   condition is a certified necessary condition for counterexamples.
4. **(N1).** P-I1 states it explicitly,
   $\gcd(C(n, 2), C(n, j)) = 2^a 3^b$ (item 5). P-I2's item (d) is
   *labelled* "(N1) and (N2)" but its text states only (N2). *Ruling:*
   P-I1 correct; P-I2's (d) is a labelling overclaim — the one genuine
   (if minor) defect in P-I2's reconciliation, recorded as the GAP in
   §2.2. The conjunction P-I2 states is still a true necessary
   condition.
5. **$h = 1$ non-special tops: primes vs prime powers.** P-I2 (item
   (g)) deliberately states F1.9(b)'s prime-factor form and warns
   that prime powers are constrained only through the dichotomy —
   which is an accurate account of the Cycle 2 record *as filed*.
   P-I1 states the same two Cycle 2 forms in its (RES-3)(8) and then
   *proves the sharpening* (Lemma I3.1: every $\ge 5$ prime power of
   a non-special top is $\le T$). *Ruling:* the sharpening is valid
   (§5.3), so the correct current statement is P-I1's stronger one;
   P-I2's caution was warranted relative to F1.9/F2.4 alone and its
   (RES-3) is true but no longer sharpest on this point.
6. **Itemisation granularity.** P-I1 lists nine discrepancies
   (D1–D9), P-I2 five (D1–D5) with a different partitioning; P-I1
   additionally itemises $v_2 \ge 4$ (D8) and $n > 10^6$ (D9) as
   conditions present in neither F1.11 nor F2.14 — verified accurate
   (both conditions appear in the provers' summaries and CYCLE2 §2,
   not in the two residual statements). No contradiction between the
   two lists.

**Net ruling:** P-I1 Claim I1.1 is the correct complete (RES-3) and
is the form adopted in §7's final residual; P-I2 Claim I2.1 is a true
but strictly weaker necessary-condition statement, with the minor
completeness GAP itemised above. This does not touch P-I2's §3, which
is where its contribution lies and which is fully certified.

## 9. Discrepancy register (everything found, however small)

1. **$J_{\max}$ tables differ between the provers** (e.g. $(2,14)$:
   1143 vs $B^{*} = 1151$; $(3,0)$: sentinel 4 vs $B^{*} = 3$).
   **Not an error** — different, clearly-defined quantities (§5.1);
   both tables reproduced exactly under their own definitions, with
   identical exception sets and identical $\le 5000$ counts.
2. **P-I2 Claim I2.1(d):** "(N1)" is named but not stated (GAP,
   completeness only; §8 item 4).
3. **P-I2 Claim I2.11(e):** "$n - 1 \ge 29$" should be $\ge 19$ under
   the section's stated $j > 3$ (the printed figure assumes
   $j \ge 5$). Immaterial: the row's $\rho$-set already forces
   $n - 1 \in \{1, 3\}$.
4. **P-I1 numbering:** Claims I3.3 and I3.4 do not exist (numbering
   jumps I3.2 → I3.5). Presentational; no content missing.
5. **P-I1 D1 wording:** "F1.16 gives $j > 2000$ in F1's summary" —
   F1.18 item 5 states the closure as "$5 \le j \le 2000$ closed",
   which is the same content from the other side. Immaterial.
6. **Conventions for $(H3)$:** P-A1's (H3) uses $3 < j \le n/2$; F2 §0
   restates it with $7 \le j$. Both Cluster I provers use the
   $3 < j$ form (P-A1's). Since every closure here is row-wise over
   all $j > 3$, the variance has no effect on any claim in this
   cluster; recorded for citation hygiene only.
7. No other discrepancy was found: in particular, every number
   printed in either file that the verifier recomputed — $\Lambda_3$
   values, both threshold tables, all $M(T)$ sizes, all 88 candidate
   lists/gcds across both files, the scan totals 1390/20/586, the
   cross-check counts 5/4/3, and both brief-correction $T$ values —
   matched exactly.

## 10. Bottom line for Cluster I

**Certified after this verification:**

1. **No counterexample at $i = 3$ has $T \le 16$** (two independent
   prover routes; P-I1: squared-half finiteness + certified frontier
   + finite lists; P-I2: elimination lemma). A counterexample must
   satisfy (RES-3) (P-I1's Claim I1.1 form) **and** $T \ge 17$.
2. **No even (LD3) solution exists in any row with $T \le 16$**
   (P-I2 Claims I2.7–I2.14; EEES-free, Proposition-4.1-free). The
   adjudicated difference between the provers is resolved: P-I2's
   stronger claim stands; P-I1's non-claim was method-relative
   caution, explicitly flagged as such in its own Claim I4.1.
3. The elimination lemma (I2.7) and its corollaries (I2.8, I2.9) are
   proved and computationally stress-tested (1,282,474 pairs;
   1,492,091 group instances; 0 failures; aligned cases exactly as
   classified).
4. P-I1's per-row finiteness for $h \le 1$ (I2.1–I2.5), its
   $M(T)$ machinery (I3.1, I3.2 — with Lemma I3.1's prime-power
   sharpening of F1.9(b) certified valid), and all of its finite
   lists are correct; the squared-half derivation's failure at
   $(2,0)$ is correctly identified by both provers.
5. The (4,2) validation is exact under both provers' methods:
   candidates $(22,5), (46,11), (106,26)$; gcds $77, 69, 371$; (LD3)
   violated at $r = 0$ by $11, 23, 53$ respectively.
6. All 68 + 20 candidate disposals are genuine. **No surviving
   candidate, no surviving gap in any $T \le 16$ row.**

**What remains OPEN (correctly labelled by both provers):** the
(RES-3) class with $T \ge 17$; $(H3)_{\mathrm{even}}$ restricted to
$T \ge 17$ rows (with $n > 10^6$); (H3) in full; $i = 3$ in general;
#699. Per-row finiteness now holds in *every* fixed row by two
independent mechanisms (squared half for counterexamples at
$h \le 1$; (LD3) alone for solutions in all rows), so the obstruction
is exactly the infinitude of rows with $T \ge 17$, in each of which
the finite lists grow with $(Q, R)$ and no uniform disposal is known.

— V-I
