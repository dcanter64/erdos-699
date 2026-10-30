# V-J: Independent verification of Cluster J (the $v_2$ condition and refined comparisons at $i=3$), Cycle 3

Verifier: V-J (independent). Files verified: `proofs/P-J1.md` (with
`proofs/P-J1_checks.py`) and `proofs/P-J2.md` (with
`proofs/P-J2_checks.py`), against `CYCLE2.md` §2, `proofs/P-F1.md`
(Claims F1.12–F1.14), `proofs/P-F2.md` §4.1 (Theorem F2.15, Corollary
F2.16), `verification/V-F.md`, and `proofs/P-A1.md` (Proposition
A1.16). Both prover scripts were run as filed: **P-J1_checks.py passes
in full (~1.2 s); P-J2_checks.py passes in full (~4.9 s)**.

Verifier's own computations (Python stdlib only, exact arithmetic):
`verification/V-J_checks.py` (~9.5 s, all assertions pass).
Implementations differ from both provers': $v_2$ by trailing-zero
string scan and by direct division of $C(n,3)$; $\Lambda_3$ by trial
division; $N(3,j)$ and $N_{\max}$ by exact binary search; hybrid maxima
by binary search ($h=0$, monotone) and direct scan to analytic caps
($h=1$); (LD3) via a verifier-written SPF factorisation applied by
brute force over **all** $j$ (validation) and over the three window
rows (disposals).

**Headline verdict. The two provers agree on every headline statement,
and every headline statement is CERTIFIED.** (1) The $v_2$ theory is
correct: $v_2(C(n,3)) = s_2(n-3) + 2 - s_2(n)$; for $v \ge 2$,
$\{n : v_2(C(n,3)) \ge v\}$ is exactly the five classes
$\{0, 1, 2, 2^v, 2^v+2\} \bmod 2^{v+1}$ (three classes for $v=1$),
brute-force verified for $v \le 8$ over $n \le 10^5$; the $v=4$ forms
($16 \mid n$ or $16 \mid (n-2)$ for $n$ even; $32 \mid (n-1)$ for $n$
odd) are correct. (2) $\rho(Q,j)$ is strictly decreasing with unattained
infimum $Q^3$, and $v_{\min}(Q) = \lfloor 3\log_2 Q \rfloor + 1$ is
correct for all $Q \le 16$ recomputed (in particular $4, 5, 7$ at
$Q = 2, 3, 4$), strictness at $Q \in \{2,4,8,16\}$ included. (3) The
F1.14 GAP is settled and its final sentence is **FALSE**, as both
provers claim: the $V_3$-refined comparison closes the full pair
$(3,j)$, $j > 5$, exactly for $j \in \{6, 10\}$ (full closing set
$\{5, 6, 10\}$ among $j \ge 5$), verified by independent enumeration
over $[2j, N(3,j)]$ for $5 \le j \le 18$ and by the power-of-two witness
for $j \ge 19$. (4) P-J1's criterion (A)/(B) row closures are all
arithmetically correct. (5) P-J2's hybrid comparison is correct,
uniformly sharper than the squared half in all 74 rows recomputed, and
its (LD3) window disposals reproduce exactly (33 + 32 + 2597 triples,
zero survivors). **Four defects were found, none touching the headline
closures:** P-J1 Corollary J1.4(ii)'s conditional density is off by a
factor of 2 (minor FALSE gloss); P-J1 Claim J3.3(c)'s proof omits the
$(2,0)$ subcase (GAP as filed; the statement is true and a
verifier-supplied repair is given in §4.3); P-J2 Claim J2.7's universal
"$v_2$ + labels close no row" sentence is **FALSE** (refuted by the
$(4,2)$ row, on the provers' own candidate enumeration); and P-J2
Claim J2.14's "still open" list is **FALSE** at the four boundary rows
$(2,22)$, $(3,19)$, $(3,20)$, $(4,18)$ (and overstated at $Q \ge 5$),
which P-J1's criterion (B) closes. The reconciled union table is in
§6. **$i = 3$ is not closed, (H3) is not proved, and #699 is not
claimed solved — both provers state exactly this, and the verifier
concurs.**

---

## 1. J.1: the $v_2$ theory (task item 1)

Both provers' proofs of the digit-sum identity were audited line by
line: Legendre's formula $v_2(m!) = m - s_2(m)$ (via
$\sum_k \lfloor m/2^k \rfloor = \sum_i b_i(2^i - 1)$) gives
$v_2(C(n,3)) = s_2(n-3) + s_2(3) - s_2(n)$ with $s_2(3) = 2$, and
Kummer's theorem identifies this with the carry count when adding
$(n-3) + 3$, equivalently the borrow count when subtracting $3$ from
$n$. The verifier confirmed all forms independently: direct division
of $C(n,3)$ by 2 (a third implementation) agrees with the $s_2$
formula for $n \le 3000$, and a verifier-coded carry/borrow counter
agrees for $n \le 20{,}000$ (0 mismatches).

The classification proof (both files) is sound: with
$P = v_2(n(n-1)(n-2)) = v_2(C(n,3)) + 1$, the parity cases give, for
$n$ odd, $P = v_2(n-1)$; for $n \equiv 0 \pmod 4$, $P = v_2(n) + 1$;
for $n \equiv 2 \pmod 4$, $P = 1 + v_2(n-2)$; P-J2's equivalent
$\min(v_2(n), v_2(n-2)) = 1$ formulation for even $n$ is also correct.
The five classes for $v \ge 2$ are distinct mod $2^{v+1}$ and complete;
the $v = 1$ degeneration (the two even subcase lists coincide, since
$2^1 = 2$ is not $0 \bmod 4$) is correctly handled by both. Verifier's
brute force over $n \le 10^5$ reproduces the lists for every
$0 \le v \le 8$: counts $2, 3, 5, 5, 5, 5, 5, 5, 5$, lists
$\{0,1,2,2^v,2^v+2\}$ for $v \ge 2$, explicitly
$v=4$: $\{0,1,2,16,18\}$ mod 32; $v=5$: $\{0,1,2,32,34\}$ mod 64;
$v=6$: $\{0,1,2,64,66\}$ mod 128. The parity forms at $v = 4$ and the
general-$v$ parity forms of P-J2 Claim J2.2 were brute-force verified
over the same range. F2.16's density $27/32$ for $v_2 \le 3$ is
recovered as $1 - 5/32$.

**One flaw (P-J1 only).** Corollary J1.4(ii) states the four even
classes have "absolute density $4/2^{v+1}$, i.e. a proportion
$2^{1-v}$ of all even $n$." The absolute density is right, but the
proportion **among even $n$** is $2^{2-v}$ (divide by $1/2$), not
$2^{1-v}$: at $v = 4$ the proportion is $1/4$, exactly as P-J2's
corollary to Claim J2.3 correctly states. Minor FALSE gloss; the
class lists, the absolute densities, and every downstream use
(P-J1 Corollary J2.3 uses absolute densities) are unaffected.

## 2. J.2: $Q$-stratification (task item 2)

$\rho(Q,j) = Q \cdot \frac{Qj-1}{j-1} \cdot \frac{Qj-2}{j-2}$, with
$\frac{Qj-a}{j-a} = Q + \frac{a(Q-1)}{j-a}$ strictly decreasing and
$> Q$ for $a \in \{1,2\}$; hence $\rho$ is strictly decreasing,
$\rho(Q,j) > Q^3$ for all finite $j$, and $\inf_j \rho = Q^3$,
unattained. (P-J2's proof contains one immaterial wording slip —
"each factor … exceeds the next factor's value" is not true of the
constant factor $Q$ — but its actual argument, constant factor times
two strictly decreasing factors $> Q$, is complete.) The derivation
of $v_{\min}$ is correct and the strictness is exactly where both
provers put it: a counterexample satisfies
$2^{v_2} = C(n,3)/V_3(n) \ge C(n,3)/C(j,3) \ge \rho(Q,j) > Q^3$ by
(N2), so $v_2 > 3\log_2 Q$, i.e.
$v_2 \ge \lfloor 3\log_2 Q\rfloor + 1$. At $Q \in \{2, 4, 8, 16\}$,
$Q^3 = 2^{v_{\min}-1}$ exactly (verifier-checked), so the non-strict
inequality would give one less — the strict $\rho > Q^3$ is
load-bearing and is used correctly in both files. Verifier's exact
recomputation by integer comparison $2^v > Q^3$ for $Q \le 16$:
$v_{\min} = 4, 5, 7, 7, 8, 9, 10, 10, 10, 11, 11, 12, 12, 12, 13$ —
both tables match in full. Strict decrease and $\rho > Q^3$ were
re-verified in exact `Fraction` arithmetic for $Q \le 16$,
$j < 300$, and $\rho(Q, 10^7) < 2^{v_{\min}(Q)}$ confirms the claimed
sharpness of the uniform bound. P-J2's remark that
$\rho(Q,j)$ is within $0.1\%$ of $Q^3$ at $j \ge 5001$, $Q \le 10$,
checks out from its factor form (each factor contributes
$< 1 + 2/(j-2)$-type terms; total $< 0.07\%$).

The congruence translations of the $v_{\min}$ condition (P-J1 Claim
J3.1, P-J2 Claim J2.6) are **both correct and mutually consistent —
no conflict**: P-J1 works mod $2^{v+1}$ (four even $n$-classes,
giving e.g. four classes of $j$ mod 64 at $Q = 3$, proportion
$1/16$), P-J2 works mod $2^{v}$ via the equivalent divisibility form
$2^{v_{\min}} \mid n$ or $2^{v_{\min}} \mid (n-2)$ (two classes of $j$
mod 32 at $Q = 3$, same proportion $1/16$; one class mod 32 at
$Q = 4$, proportion $1/32$, matching P-J1's two classes mod 64). The
verifier re-derived P-J2's translations exhaustively (its §G1 run
plus the parity forms of §1 above) and spot-checked P-J1's:
$3^{-1} \equiv 43 \pmod{64}$ and the $Q = 4$ solvability condition
$s \equiv R \pmod 4$ are correct.

## 3. Settlement of the F1.14 GAP (task item 3)

**Independent enumeration** over $[2j, N(3,j)]$ (verifier's own
$N(3,j)$ by binary search; $V_3$ by the verifier's $v_2$) reproduces
both provers' tables **exactly**:

| $j$ | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| $C(j,3)$ | 10 | 20 | 35 | 56 | 84 | 120 | 165 | 220 | 286 | 364 | 455 | 560 | 680 | 816 |
| $N(3,j)$ | 11 | 18 | 27 | 37 | 49 | 62 | 77 | 94 | 112 | 132 | 153 | 176 | 201 | 227 |
| $\min V_3$ | 15 | 35 | 35 | 35 | 51 | 155 | 155 | 155 | 155 | 155 | 155 | 155 | 187 | 651 |
| at $n$ | 10 | 16 | 16 | 16 | 18 | 32 | 32 | 32 | 32 | 32 | 32 | 32 | 34 | 64 |
| closes? | yes | **yes** | no | no | no | **yes** | no | no | no | no | no | no | no | no |

Every named witness was checked individually to lie in
$[2j, N(3,j)]$ with $V_3(n) \le C(j,3)$: $(16,7)$ with equality
$V_3(16) = 35 = C(7,3)$ and $v_2(C(16,3)) = 4$; $n = 32$
($V_3 = 155$) for $j = 11..16$; $n = 34$ ($V_3 = 187$) for $j = 17$;
$n = 64$ ($V_3 = 651$) for $j = 18$.

**The $j \ge 19$ argument is sound in both files.** With
$a = \lceil \log_2 2j \rceil$ and $n = 2^a$: $2j \le n < 4j$;
$v_2(C(n,3)) = a$ (P-J1's bookkeeping) resp. the equality case of
$2^{v_2} \le n$ (P-J2), giving
$V_3(2^a) = (2^a-1)(2^{a-1}-1)/3 = (n-1)(n-2)/6$ — direction checked:
this is an **upper** bound target, $V_3(n)$ must be shown $\le
C(j,3)$, and both derivations upper-bound $V_3$ correctly
(P-J1: $V_3 < (4j)(2j)/3 = \frac83 j^2 \le C(j,3)$ via
$(j-1)(j-2) - 16j = j^2 - 19j + 2 \ge 2$ at $j \ge 19$, increasing;
P-J2: $(n-1)(n-2) < n^2 < 16j^2 \le j(j-1)(j-2)$, same polynomial).
The in-range lemma $C(4j,3) < C(2j,6)$ (which gives
$n < 4j \Rightarrow n \le N(3,j)$) was verified two ways: brute force
for $10 \le j \le 2000$ (0 failures), and audit of both crude-bound
proofs — P-J1's via $(2j-5)^2 \ge 20j$ for $j \ge 10$
($4j^2 - 40j + 25 \ge 25 > 0$), giving
$C(2j,6) > \frac{100}{9}j^3 > \frac{96}{9}j^3 > C(4j,3)$; P-J2's
grouping of $(2j-5)^6 - 7680j^3$ as
$64j^5(j-15) + j^3(6000j - 27680) + 37500j(j-1) + 15625$ expands
correctly and is termwise positive for $j \ge 19$.

**Exact validity range of the bare inequality** (verifier
computation, $j \le 5000$): $V_3(2^a) \le C(j,3)$ for the $a$-witness
holds exactly at $j \in \{7, 8\} \cup \{j : j \ge 11\}$ in that range
(fails at $j = 5, 6, 9, 10$). The provers' claimed range $j \ge 19$
is therefore correct and strictly inside the inequality's true
range; for $11 \le j \le 18$ the analytic chains as filed do not
cover the inequality (the $j^2 - 19j + 2 \ge 0$ step fails there),
but those $j$ are disposed by the verified table witnesses anyway,
so no claim is affected.

**Verdict: the final sentence of Claim F1.14 is FALSE, as both
provers assert; the refined comparison closes the full pair exactly
at $j \in \{5, 6, 10\}$** (P-J1's formulation on the
finite-reduction interval), equivalently exactly at $j \in \{6, 10\}$
among $j > 5$ for all $n \ge 2j$ (P-J2's formulation, via its
$M(j)$ window; P-J1 Claim J4.4(b) independently gives the all-$n$
closure at $6$ and $10$). The two formulations are consistent, and
the strengthening is genuine: the head values for $j = 10$,
$V_3(20..28) = 285, 665, 385, 1771, 253, 575, 325, 2925, 819$, all
$> 120$, were recomputed exactly.

## 4. P-J1's squared-bound criteria (task item 4)

### 4.1 The criteria's logic

Criterion (A): a counterexample in a fixed row has $j \ge 5001$
(certified per-pair frontier, F2.19) and must satisfy the squared
inequality (EEES form of Prop. 4.1; the sole $i=3$ exception pair
$(8,3)$ is incompatible with $j \ge 5001$). If the exact maximum
$j_{\mathrm{sq}}$ of the inequality is $\le 5000$, contradiction.
Criterion (B): in an $h = 0$ row the squared inequality is
$C(n,3) < \Lambda_3(T)^2$, i.e. $n \le N_{\max}(T)$; if
$N_{\max}(T) \le 10^6$, a counterexample would satisfy (LD3) with
$n \le 10^6$, contradicting the certified zero-survivor search
(F1.17/F2.21, V-F §4). **Both inputs are applied only within their
certified ranges** — (A) uses $j \ge 5001$ exactly where the frontier
is certified, (B) uses $n \le 10^6$ exactly where (LD3) is certified
— and the restriction of (B) to $h = 0$ is necessary and correctly
observed (for $h = 1$ the right side grows with $j$, so no constant
$N_{\max}(T)$ exists). The monotonicity inputs are proved, not just
sampled: Claim J3.4(a) ($h = 0$: left side increasing, right side
constant) is immediate, and J3.4(b)'s proof that
$A(j) = (\Lambda_3(T) j)^2 / C(Qj+R,3)$ is strictly decreasing was
audited step by step — the factor bound
$C(n+Q,3)/C(n,3) \ge (1 + Q/n)^3$, the estimate $Q/n > 2/(3j)$ from
$R < j$ and $Q \ge 2$, and the polynomial identity
$(1 + \frac{2x}{3})^3 - (1+x)^2 = \frac{x^2}{3} + \frac{8x^3}{27} > 0$
all check. The crude cap $j_{\mathrm{sq}} < 24\Lambda_3(T)^2/Q^3$
(from $C(Qj,3) \ge (Qj)^3/24$) is also correct.

### 4.2 Boundary arithmetic, recomputed independently

Verifier's $\Lambda_3$ (trial division) and $N_{\max}$ (binary search
with the two-sided certificate $C(N_{\max},3) < \Lambda_3(T)^2 \le
C(N_{\max}+1,3)$) reproduce the provers' values, including
$\Lambda_3(24) = 334639305$, $N_{\max}(24) = 875861$,
$\Lambda_3(25) = \Lambda_3(26) = 1673196525$,
$N_{\max}(25) = N_{\max}(26) = 2561033$, and the threshold fact
$N_{\max}(T) \le 10^6 \iff T \le 24$ (checked for $3 \le T \le 30$,
monotonicity included). For every row named in the brief:

| row | $T$ | $N_{\max}$ / $j_{\mathrm{sq}}$ | verdict |
|---|---|---|---|
| (2,22) | 24 | $N_{\max} = 875861$, $j_{\mathrm{sq}} = 437919$ | closed by (B), **not** (A) — as claimed |
| (2,24) | 26 | $N_{\max} = 2561033$, $j_{\mathrm{sq}} = 1280504$ | **open**, window $j \in [499989, 1280504]$ — as claimed |
| (3,20) | 24 | $N_{\max} = 875861$, $j_{\mathrm{sq}} = 291947$ | closed by (B) — as claimed |
| (3,21) | 25 | $N_{\max} = 2561033$, $j_{\mathrm{sq}} = 853670$ | **open**, window $[333327, 853670]$ — as claimed |
| (4,18) | 24 | $N_{\max} = 875861$, $j_{\mathrm{sq}} = 218960$ | closed by (B) — as claimed |
| (4,20) | 26 | $N_{\max} = 2561033$, $j_{\mathrm{sq}} = 640253$ | **open**, window $[249996, 640253]$ — as claimed |
| (5,0) | 8 | $j_{\mathrm{sq}} = 529$ ($h=1$) | closed by (A) — as claimed |
| (5,1) | 9 | $j_{\mathrm{sq}} = 4762$ | closed by (A) — as claimed |
| (5,2) | 10 | $j_{\mathrm{sq}} = 4762$ | closed by (A) — as claimed |
| (6,0) | 10 | $j_{\mathrm{sq}} = 2756$ | closed by (A) — as claimed |
| (6,1) | 11 | squared holds at $j = 5001$; verifier's exact $j_{\mathrm{sq}} = 333506$ | not closed by (A) — as claimed |
| (6,2) | 12 | squared holds at $j = 5001$; verifier's exact $j_{\mathrm{sq}} = 333505$ | not closed by (A) — as claimed |

All remaining table values in Claim J3.5 were also recomputed and
match exactly: the $h = 1$ values $(2,1){:}\ 6$, $(2,2){:}\ 5$,
$(3,0){:}\ 2$, $(3,1){:}\ 50$, $(3,2){:}\ 48$, $(4,0){:}\ 21$,
$(4,1){:}\ 1033$, $(4,2){:}\ 1032$; the $h = 0$ (A)-closures at
$Q = 2$ ($j_{\mathrm{sq}} = 4, 17, 38, 203, 1144, 1143$ for
$R = 4..14$), $Q = 3$ ($12, 12, 26, 26, 136, 136, 764, 763, 763, 763$
for $R = 3..12$, and $5065$ at $R = 13, 14$), $Q = 4$ ($20, 102, 573,
572, 3799$ for $R = 4..12$), and the (B)-closures' $N_{\max}$ lists.
The first-open windows' lower ends, $\lfloor (10^6 - R)/Q \rfloor + 1$
from $n > 10^6$, are correct in all three cases.

### 4.3 Supporting claims J3.1–J3.3

Claim J3.1 (congruences on $j$): PROVED, see §2. Lemma J3.2 (the
prime-power strengthening of F1.9(b) at $h = 1$): PROVED — the
F2.4 dichotomy gives $q \le T$ or $q \mid j$, and $q \mid j$ with
$q \Vert (n-r)$, $r \ne R$, forces $q \mid R - r$ with
$0 < |R - r| \le 2 < 5 \le q$, impossible. Claim J3.3 (label
finiteness per fixed row): parts (a) and (b) are **PROVED** (the
$3$-exponent bookkeeping via $3^{e-1}$ and, at $R \in \{0,2\}$,
$\gcd(j, R-1) = 1$ forcing $e = 1$, all check, within §3's standing
hypothesis that $n$ is even). Part (c)'s deduction has a **GAP as
filed**: the union over $R \in \{0, 2\}$ includes the row $(2,0)$,
which is neither case (a) ($R < 3$) nor case (b) (there $h = 2$, and
Lemma J3.2 explicitly excludes $(2,0)$), and no filed argument covers
it. The **statement is nevertheless true**; verifier-supplied repair:
at $(2,0)$, $T = 2$ and F2.4 with $h = 2$ gives, for every $\ge 5$
prime power $P \Vert (n-1)$, either $P \le 2$ (impossible) or
$P \mid j$ or $P \mid j-1$ — both impossible since
$\gcd(j, n-1) = \gcd(j, 2j-1) = 1$ and
$\gcd(j-1, n-1) = \gcd(j-1, 2j-1) = 1$; and for the $3$-part
$3^{e-1}$ of $n-1$, either $3^{e-1} \le 2$, or it divides $j$ or
$j-1$, again forcing $3^{e-1} = 1$. Hence $n - 1 \in \{1, 3\}$:
finitely many $n$, by label bounds alone, as claimed. The gap is in
the filed proof only, touches no closure (the row $(2,0)$ is closed
separately by Price), and does not propagate.

## 5. P-J2's hybrid comparison and (LD3) windows (task item 5)

**The maximal-valuation bound is correct.** Claim J2.9's proof: for
$n$ odd, $v_2(C(n,3)) = v_2(n-1) - 1 < \log_2 n$; for $n$ even,
$v_2(C(n,3)) = \max(v_2(n), v_2(n-2))$ (since the minimum of the two
valuations is exactly 1), which is $\le \log_2 n$ with equality iff
$n$ is a power of 2 (the $n - 2$ alternative gives
$2^{v_2} = n - 2 < n$). Hence $2^{v_2(C(n,3))} \le n$ and
$V_3(n) \ge (n-1)(n-2)/6$. The verifier confirmed the bound **and**
the equality characterisation by brute force for $n \le 50{,}000$
(P-J1 Claim J4.3 proves the same bound by the Legendre-summand
argument of A1.13; that proof is also sound — each summand is in
$\{0,1\}$ and summands with $2^k > n$ vanish).

**The hybrid test's logic is correct**: a counterexample satisfies
$(n-1)(n-2)/6 \le V_3(n) \le \Lambda_3(T)\binom{j}{h}$ (left by
J2.9, right by Prop. 4.1 divisibility), so
$(n-1)(n-2) > 6\Lambda_3(T)\binom{j}{h}$ closes the triple; combined
with the certified $j \le 5000$ closure, a row with
$j_{\mathrm{hyb}} \le 5000$ is closed for all $j$. The analytic caps
used for the exact scans check: for $h = 0$,
$(Qj+R-2)^2 \le (n-1)(n-2) \le 6\Lambda_3(T)$; for $h = 1$,
$(Qj-2)^2 \le 6\Lambda_3(T) j$ with $Qj - 2 \ge Qj/2$ gives
$j \le 24\Lambda_3(T)/Q^2$. Boundary rows, recomputed independently
($h = 0$ by binary search on the monotone predicate):

| row | $j_{\mathrm{hyb}}$ (verifier) | $j_{\mathrm{hyb}}$ (P-J2) | closes residual? |
|---|---|---|---|
| (2,20) | 4662 | 4662 | yes |
| (2,22) | 22394 | 22394 | **no** |
| (3,18) | 3108 | (not printed; $\le 5000$ implied) | yes |
| (3,19) | 14930 | 14930 | **no** |
| (4,16) | 2332 | 2332 | yes |
| (4,18) | 11198 | 11198 | **no** |

Every $j_{\mathrm{hyb}}$ and $j_{\mathrm{sq}}$ value printed in
Claims J2.8 and J2.12 was recomputed and **matches exactly** (all 25
hybrid and 31 squared values in the printed tables, including
$(4,14){:}\ 27071$, $(3,13){:}\ j_{\mathrm{sq}} = 5065$,
$(2,18){:}\ j_{\mathrm{hyb}} = 4663$). The "sharper than squared"
claim was verified in the strong form: for **all 74 rows**
$Q \in \{2,3,4\}$, $0 \le R \le 24$, $(Q,R) \ne (2,0)$, the verifier
recomputed both maxima and found $j_{\mathrm{hyb}} \le
j_{\mathrm{sq}}$ in every row, no exceptions. The closure claims
follow: hybrid + $j \le 5000$ frontier closes $(2, R)$ for even
$4 \le R \le 20$, $(3, R)$ for $1 \le R \le 18$, $(4, R)$ for even
$2 \le R \le 16$ — **confirmed**.

**The (LD3) window disposals reproduce with independent code.** The
verifier's (LD3) implementation (relevant prime powers
$q = p^a \Vert (n-r)$ with $p \ge 5$, or $p = 3$ with $a \ge 2$;
condition $j \bmod q \le r$) was validated by brute force over **all**
$j \le n/2$ (not the multiples-of-$R(n)$ shortcut the provers use):
the $\ge 5$-only system at $n \le 2000$ returns **exactly** P-A1's
six pairs $(10,5), (28,14), (82,41), (162,70), (244,122), (730,365)$,
and the full system returns zero survivors — both as P-J2 reports.
The windows: $(3,13)$: 33 triples ($j$ odd in $[5001, 5065]$),
$(3,14)$: 32 triples ($j$ even), $(2,16)$: 2597 triples
($j \in [5001, 7597]$, $n$ always even) — **counts match exactly,
zero (LD3) survivors in each**, confirming Claim J2.8's disposals.
(Note these windows are also subsumed by P-J1's criterion (B), since
their $N_{\max} = 15210 \le 10^6$; the two disposals are consistent,
and P-J2's is an independent direct computation.)

**The one FALSE claim in P-J2's §3.** Claim J2.7 asserts that
$v_2$ + label bounds alone close **no** $(Q,R)$ row, arguing that the
two condition families "act on disjoint sets of prime valuations."
The inference is invalid (both families constrain the same $(n,j)$
through $n = Qj + R$ and the gcd conditions internal to the label
argument itself), and the universal statement is refuted on the
provers' own record: at $(4,2)$ the F1.9/F2.4 label dichotomy plus
$\gcd(j, n-1) = 1$ leaves exactly the three candidates
$(22,5), (46,11), (106,26)$ (enumeration re-derived by the verifier:
$n - 1 = 3^b 5^a 7^c$, $b \le 2$, $a, c \le 1$, $n \equiv 1 \pmod 4$),
and their valuations $v_2(C(n,3)) = 2, 2, 3$ (verifier-recomputed)
are all $< 4$, so $v_2$ + labels **do** close that row — which is
precisely the "independent bite" the claim's own second half
exhibits. The computation in J2.7 is PROVED; the observation as
stated is FALSE. Nothing downstream uses it: P-J2's closures all go
through the squared half, the hybrid, or (LD3), and $(4,2)$ is
closed independently by criteria (A) and hybrid.

## 6. Reconciliation: one union table (task item 6)

Strongest certified status per row, combining Cycle 2, P-J1, and
P-J2. "Closed" means no counterexample in the row for any $j$.
Rows with $R$ odd at $Q \in \{2, 4\}$ have $n$ odd throughout and are
closed globally by SPLIT-odd; they are listed once.

**$Q = 2$** ($v_{\min} = 4$)

| rows | status | supplied by |
|---|---|---|
| $R$ odd (any) | CLOSED | SPLIT-odd (Cycle 2) |
| $(2,0)$ | CLOSED | Price ($n = 2j$), Cycle 2 |
| $(2,2)$ | CLOSED | F1.10; also J1-(A) ($j_{\mathrm{sq}} = 5$) |
| even $4 \le R \le 14$ | CLOSED | J1-(A); also J2 squared, J2 hybrid |
| even $R \in \{16, 18, 20\}$ | CLOSED | J1-(B); also J2 hybrid ($(2,16)$ also J2 (LD3) window) |
| even $R = 22$ | CLOSED | **J1-(B) only** (J2 hybrid fails: 22394) |
| even $R \ge 24$ | **OPEN** | first $(2,24)$, window $j \in [499989, 1280504]$ |

**$Q = 3$** ($v_{\min} = 5$)

| rows | status | supplied by |
|---|---|---|
| $(3,0), (3,2)$ | CLOSED | F1.10 (Cycle 2) |
| $R = 1$ | CLOSED | J1-(A) (50); also J2 hybrid (10) |
| $3 \le R \le 12$ | CLOSED | J1-(A); also J2 squared |
| $R \in \{13, 14\}$ | CLOSED | J1-(B); also J2 (LD3) windows (33 / 32 triples) |
| $15 \le R \le 18$ | CLOSED | J1-(B); also J2 hybrid (3109, 3109, 3109, 3108) |
| $R \in \{19, 20\}$ | CLOSED | **J1-(B) only** (J2 hybrid fails: 14930 at $R = 19$, 14930 at $R = 20$) |
| $R \ge 21$ | **OPEN** | first $(3,21)$, window $j \in [333327, 853670]$ |

**$Q = 4$** ($v_{\min} = 7$)

| rows | status | supplied by |
|---|---|---|
| $R$ odd (any) | CLOSED | SPLIT-odd (Cycle 2) |
| $(4,0)$ | CLOSED | F1.10 (Cycle 2) |
| even $R = 2$ | CLOSED | J1-(A) (1032); also J2 hybrid (39) |
| even $4 \le R \le 12$ | CLOSED | J1-(A); also J2 squared / hybrid |
| even $R \in \{14, 16\}$ | CLOSED | J1-(B); also J2 hybrid (2332) |
| even $R = 18$ | CLOSED | **J1-(B) only** (J2 hybrid fails: 11198) |
| even $R \ge 20$ | **OPEN** | first $(4,20)$, window $j \in [249996, 640253]$ |

**$Q = 5$** ($v_{\min} = 7$) — P-J2 makes no row claims here.

| rows | status | supplied by |
|---|---|---|
| $R \in \{0, 1, 2\}$ ($h = 1$) | CLOSED | J1-(A) (529, 4762, 4762) |
| $3 \le R \le 16$ ($h = 0$) | CLOSED | J1-(B) via its remark ($T = R + 8 \le 24$) |
| $R \ge 17$ | **OPEN** (by cluster criteria) | first $h = 0$ row $(5,17)$ |

**$Q = 6$** ($v_{\min} = 8$) — P-J2 makes no row claims here.

| rows | status | supplied by |
|---|---|---|
| $R = 0$ ($h = 1$) | CLOSED | J1-(A) (2756) |
| $R \in \{1, 2\}$ ($h = 1$) | **OPEN** | squared holds at $j = 5001$ (J1); finite windows to $j_{\mathrm{sq}} = 333506, 333505$ (verifier) |
| $3 \le R \le 14$ ($h = 0$) | CLOSED | J1-(B) via its remark ($T = R + 10 \le 24$) |
| $R \ge 15$ | **OPEN** (by cluster criteria) | |

Notes. (i) P-J1's Corollary J3.6 lists the $Q \ge 5$ locus as
"$Q = 5$ with $R \ge 3$; $Q = 6$ with $R \ge 1$; or any row
$Q \ge 7$" — a valid (non-minimal) necessary-condition list, and
P-J1's own remark to Claim J3.5 states the sharpening used above:
criterion (B) closes every $h = 0$ row at **any** $Q$ with
$T = R + 2Q - 2 \le 24$ (equivalently $R \le 26 - 2Q$; this also
closes some $h = 0$ rows at $7 \le Q \le 11$, beyond this table's
brief). (ii) **Conflicts between the two files, resolved:** P-J2
Claim J2.14 lists $(2, R)$ even $R \ge 22$, $(3, R)$ $R \ge 19$,
$(4, R)$ even $R \ge 18$, and all $Q \ge 5$ rows as not closed.
At $(2,22)$, $(3,19)$, $(3,20)$, $(4,18)$ — and, via (B), at the
$Q = 5, 6$ rows above — that list is **FALSE in the combined
record**: the arithmetic of §4.2 shows criterion (B) closes them,
and the combination (P-J2's own $j_{\mathrm{sq}}$ table plus its own
standing input that (LD3) has no solution with $n \le 10^6$) was
already available inside P-J2's inputs; P-J2 simply did not draw
it. P-J1 is correct at every contested row. No other row conflicts
exist: wherever both provers close the same row, they agree, and
their $v_2$ translations (§2) and F1.14 settlements (§3) coincide.

## 7. Claim-by-claim tables

### 7.1 P-J1

| Claim | Status | Verifier's note |
|---|---|---|
| J1.1 (three faces of $v_2$) | **PROVED** | Legendre/Kummer proof audited; verifier's direct-division and carry/borrow implementations agree ($n \le 3000$ / $20{,}000$). |
| J1.2 ($v_2 \ge 4$ parity forms) | **PROVED** | Case argument correct; brute-verified $n \le 20{,}000$ by prover, $n \le 10^5$ by verifier (§1). |
| J1.3 (general classification) | **PROVED** | Five classes for $v \ge 2$, three for $v = 1$; brute-verified $v \le 8$, $n \le 10^5$. |
| Cor. J1.4 | (i), (iii) **PROVED** (iii as COMPUTATION, re-verified); (ii) **PROVED** except its last clause **FALSE** (minor) | (ii) conditional proportion among even $n$ is $2^{2-v}$, not $2^{1-v}$ (§1). (iii) $n_0(j,4) = 14,17,19,24,49$, $n_0(j,5) = 17,20,24,30,62$ reproduced. |
| J2.1 ($\rho$ behaviour) | **PROVED** | Factorisation and monotonicity audited; re-verified in Fractions. |
| J2.2 ($v_{\min}(Q)$) | **PROVED** | Strictness at powers of 2 handled correctly; table to $Q = 16$ recomputed exactly (§2). |
| Cor. J2.3 (stratification) | **PROVED** | Absolute densities $4/2^{v+1}$ per row correct ($1/8, 1/16, 1/64, \dots$). |
| J3.1 (congruences on $j$) | **PROVED** | Counts/proportions correct; consistent with P-J2's alternative modulus (§2). |
| Lemma J3.2 (F1.9(b) prime-power form) | **PROVED** | See §4.3. |
| J3.3 (label finiteness per fixed row) | (a), (b) **PROVED**; (c) **GAP** as filed, statement **true** with verifier repair | (c) omits $(2,0)$ ($h = 2$); repair in §4.3. No downstream effect. |
| J3.4 (squared-bound monotonicity) | **PROVED** | Proof audited in full (§4.1), incl. the polynomial identity and the $24\Lambda_3(T)^2/Q^3$ cap. |
| J3.5 (row closures) | **COMPUTATION** fully re-verified; deduction **PROVED** | Every printed $j_{\mathrm{sq}}$, $N_{\max}$, threshold, and window recomputed (§4.2); criteria applied within certified ranges (§4.1). |
| Cor. J3.6 (combined picture) | **PROVED** as a necessary-condition list | Valid but non-minimal at $Q \ge 5$; P-J1's own remark supplies the sharpening used in §6. |
| J4.1 ($j \ge 19$ witness) | **PROVED** | Inequality direction, closed form, and $C(4j,3) < C(2j,6)$ all verified (§3). |
| J4.2 (table $5 \le j \le 18$; F1.14 sentence FALSE) | **COMPUTATION** re-verified; the **FALSE** verdict on F1.14's sentence is **correct** | Table reproduced entry-for-entry (§3). |
| J4.3 ($2^{v_2} \le n$ tail bound) | **PROVED** | Legendre-summand proof sound (same bound as A1.13); $t(j)$ values $13, 17, 20, 29, 85, 987$ reproduced. |
| J4.4 (hybrid at pair level) | **PROVED** | (a) algebra ($j^2 - 6j + 2 < 0$) correct; (b) head values for $j = 6, 10$ recomputed; (c) head-placement and $D(j) = j^3 - 19j^2 + 14j - 2 > 0$ for $j \ge 19$ ($D(19) = 264$, $D' > 0$) verified. |
| J4.5 (single-top comparison, negative) | **PROVED** in substance; one wording point minor **FALSE** | The bound $V_3(n) \ge R(n-1)/3$ holds (case split on $v_3(n-1)$ filled by verifier). "Strictly weaker than F1.8 for $j > 3$" fails at $j = 4$, where both bounds equal 37; strict for $j \ge 5$, which covers the relevant range. Closes nothing, as claimed. |
| J5.1 (summary) | **PROVED** as a summary, with the J1.4(ii) and J3.3(c) notes inherited | Items 2, 4, 5, 6 match the audited claims; open items correctly **OPEN**. |

### 7.2 P-J2

| Claim | Status | Verifier's note |
|---|---|---|
| J2.1 (Legendre/Kummer forms) | **PROVED** | All five forms audited; carry/borrow counts re-verified by verifier code ($n \le 20{,}000$). |
| J2.2 (parity characterisations, all $v$) | **PROVED** | $\min = 1$ argument correct; brute-verified $n \le 10^5$ (verifier, §1). Brief's $v = 4$ forms confirmed, not corrected. |
| J2.3 (periodicity, class counts) | **PROVED** | Proof via J2.2 sound, $v = 1$ coincidence handled; lists brute-verified $v \le 8$. Its corollary's $1/4$-of-even-$n$ figure is the correct one (cf. P-J1 J1.4(ii)). |
| J2.4 ($\rho$ behaviour) | **PROVED** | Factorisation checked against $C(Qj,3)/C(j,3)$ exactly; one immaterial wording slip (§2). |
| J2.5 ($v_{\min}(Q)$) | **PROVED** | Strictness at $Q \in \{2,4,8,16\}$ explicit and correct; table recomputed; $j$-dependent remark verified ($\rho(2,6) = 11$, $\rho(4,6) = 506/5$). |
| J2.6 (congruence translations) | **PROVED** | $3^{-1} \equiv 11 \pmod{32}$; $Q = 4$ alternative analysis correct; exhaustive re-verification (prover §G1, verifier §1–§2). |
| J2.7 ($v_2$ + labels observation) | observation **FALSE**; embedded computation **PROVED** | Universal sentence refuted at $(4,2)$ (§5); disjointness inference invalid. Not used downstream. |
| J2.8 ($j_{\mathrm{sq}}$ table + windows) | **COMPUTATION** fully re-verified | All printed values match (§5); caps rigorous ($48\Lambda_3(T)^2/Q^3$ argument correct); window counts 33 / 32 / 2597 and zero survivors reproduced with independent (LD3) code (§5). |
| J2.9 ($2^{v_2} \le n$) | **PROVED** | Proof incl. equality case audited; brute-verified with equality characterisation $n \le 50{,}000$. |
| J2.10 (failure window $[2j, M(j)]$) | **PROVED** | $M(j) \sim j^{3/2} < N(3,j)$ in the computed range; the deduction from J2.9 is immediate. |
| J2.11 (F1.14 sentence FALSE; exact reach $\{6, 10\}$) | **PROVED** + **COMPUTATION** corroborated | $j = 6, 10$ all-$n$ closure via $M(6) = 12$, $M(10) = 28$ and the exact head lists; witnesses for all other $j > 5$ verified (§3); polynomial grouping for $C(4j,3) < C(2j,6)$ expands correctly. |
| J2.12 (hybrid comparison) | **PROVED** + **COMPUTATION** fully re-verified | Boundary rows and every printed value match; $j_{\mathrm{hyb}} \le j_{\mathrm{sq}}$ in all 74 rows recomputed (§5); closure ranges confirmed. |
| J2.13 (single-top comparison, negative) | **PROVED** | Derivation $V_3(n) \ge (n-1)/9 \Rightarrow n < \frac32 j^3 + 1$ checks; dominated by J2.9's bound; closes nothing, as claimed. |
| J2.14 (summary) | **PROVED** except: item 3 inherits J2.7 (**FALSE**); the "still open" list is **FALSE** at $(2,22)$, $(3,19)$, $(3,20)$, $(4,18)$ and overstated at $Q \ge 5$ | See §6 note (ii). Proved/reduced items otherwise match the audited claims; (H3) and $i = 3$ correctly left **OPEN**. |

## 8. Discrepancies found (complete list)

1. **P-J1, Corollary J1.4(ii)** — conditional density among even $n$
   printed as $2^{1-v}$; correct value $2^{2-v}$ (at $v = 4$: $1/4$,
   as P-J2 states). Minor, propagates nowhere.
2. **P-J1, Claim J3.3(c)** — proof GAP at the $(2,0)$ subcase ($h = 2$
   is in neither case (a) nor case (b), and Lemma J3.2 excludes it).
   Statement true; verifier repair in §4.3. Propagates nowhere
   ($(2,0)$ is closed by Price independently).
3. **P-J1, Claim J4.5** — "strictly weaker … for $j > 3$" fails at
   the single point $j = 4$ (bounds equal, 37). Immaterial.
4. **P-J2, Claim J2.7** — the universal "$v_2$ + labels alone close
   no row" is FALSE, refuted by $(4,2)$ on the campaign's own
   enumeration (§5); its disjointness argument is in any case a GAP
   (disjoint prime sets do not imply joint satisfiability). The
   claim's computation ($v_2 = 2, 2, 3$ at the three candidates) is
   correct. Propagates only to P-J2 Claim J2.14 item 3.
5. **P-J2, Claim J2.14 "still open" list** — FALSE at $(2,22)$,
   $(3,19)$, $(3,20)$, $(4,18)$ and overstated at $Q \ge 5$: those
   rows are closed by P-J1's criterion (B) (§6). This is the only
   conflict between the two files' row claims, and P-J1 is correct
   at every contested row.
6. Immaterial wording slips, no mathematical content: P-J2 Claim
   J2.4's "exceeds the next factor's value"; P-J1's script comment
   citing "Claim J3.3" for the monotonicity proved as Claim J3.4.

No discrepancy was found in any number either prover prints: every
table entry, threshold, window end, density, and count named in the
brief was recomputed and matches, including both provers' full
$v_{\min}$ tables, P-J1's $j_{\mathrm{sq}}$/$N_{\max}$ tables and
first-open windows, P-J2's $j_{\mathrm{sq}}$ and $j_{\mathrm{hyb}}$
tables, the $5 \le j \le 18$ minima table, and the three (LD3)
window counts.

## 9. Bottom line for Cluster J

**Certified for $i = 3$, beyond the Cycle 2 record:**

1. **Complete $v_2$ theory**: the digit-sum/borrow formulas; the
   parity characterisations for all $v$; exactly five classes
   $\{0, 1, 2, 2^v, 2^v+2\} \bmod 2^{v+1}$ for $v \ge 2$ (three for
   $v = 1$), density $5/2^{v+1}$.
2. **$Q$-stratification**: $v_2(C(n,3)) \ge v_{\min}(Q) =
   \lfloor 3\log_2 Q \rfloor + 1$ in row $Q$, via
   $\rho(Q,\cdot) \downarrow Q^3$ (unattained); $v_{\min}(2,3,4) =
   4, 5, 7$; per-row congruence translations in both provers'
   (equivalent) forms.
3. **F1.14's GAP is settled; its final sentence is FALSE.** The
   $V_3$-refined comparison closes the full pair $(3,j)$ exactly at
   $j \in \{5, 6, 10\}$; for $j \ge 19$ the power-of-two witness
   $n = 2^{\lceil \log_2 2j \rceil}$ blocks it, and the maximal bound
   $2^{v_2} \le n$ (proved by both provers) upgrades the closures at
   $j = 6, 10$ to all $n \ge 2j$ with no EEES78 input.
4. **Row closures (union, §6)**: all rows at $Q = 2$ with even
   $R \le 22$ (odd $R$ closed globally); all rows at $Q = 3$ with
   $R \le 20$; all rows at $Q = 4$ with even $R \le 18$ (odd $R$
   closed globally); at $Q = 5$, $R \le 16$; at $Q = 6$, $R = 0$ and
   $3 \le R \le 14$ — by P-J1's squared-bound criteria (A)/(B),
   independently corroborated in their overlap range by P-J2's
   hybrid comparison (uniformly sharper than the squared half) and
   its direct (LD3) window computations. First open rows:
   $(2,24)$, $(3,21)$, $(4,20)$, each with an explicit finite window.

**What remains OPEN (correctly labelled by both provers):** the
residual class in rows above the §6 thresholds (including $(6,1)$,
$(6,2)$ and all sufficiently large $R$ or $Q$); (H3) in general;
$i = 3$ in general. **$i = 3$ is not closed, (H3) is not proved, and
#699 is not claimed solved — both provers state exactly this, and
the verifier concurs.**

— V-J
