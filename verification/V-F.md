# V-F: Independent verification of Cluster F ($i=3$), Cycle 2

Verifier: V-F (independent). Files verified: `proofs/P-F1.md` (with
`proofs/P-F1_checks.py`), `proofs/P-F2.md` (no script file in the
workspace), against `strategies/S8.md` §3, `EXTERNAL_CLAIMS_2026-10-29.md`,
Proposition A1.16 of `proofs/P-A1.md` (Cycle 1, taken as standing input
per the assignment), and Price's manuscript
`~/workspace/user/files/Liam_699_partial.pdf` (extracted independently
with `pdftotext -layout` and `pdftotext -bbox`).

Verifier's own computations (Python stdlib only, exact arithmetic,
single thread): `verification/V-F_checks.py` (§A small checks),
`verification/V-F_chunkD.py` (per-pair recount),
`verification/V-F_chunkF.py` ($n\le10^6$ recount),
`verification/V-F_chunkEG.py` (brute-force cross-check, random
Lemma F2.2 check, §C reproduction). Implementations differ from the
provers': global $R(n)=d$ candidate generation with trial-division
factorisation for the per-pair recount; a prime-power sieve for $R(m)$
plus SPF factorisation of candidate tops for the $n\le10^6$ recount;
Legendre valuations for the random check.

**Headline verdict. SPLIT-odd is certified CLOSED by two independent
routes (F1.4/F1.5 and F2.7/F2.8). The per-pair (LD3) frontier is
certified to $j\le 5000$ (F2.18, fully recounted; F1.16's $j\le2000$
is subsumed and its exact counts were reproduced). (LD3) has zero
survivors with $n\le10^6$, with both provers' pair counts reproduced
exactly. The even residual class remains OPEN, correctly labelled by
both provers. $i=3$ in general and (H3) are NOT closed. Three minor
flaws were found, none load-bearing: F2.4's "exactly one" wording,
the last sentence of F1.14 (a GAP), and F2.5's missing script/seed.**

---

## 1. Proposition 4.1 extraction (task item 1)

Independent extraction from the manuscript, §4 "A Euclidean-division
bound", p. 5, confirms **both** provers' quotations in every material
particular:

* Hypothesis: $1\le i<j\le n/2$ and no prime $q\ge i$ divides both
  $\binom ni$ and $\binom nj$. ✓ (F1.1 and F2.1 agree with the PDF.)
* $n=Qj+R$ with $Q=\lfloor n/j\rfloor\ge2$, $0\le R<j$ — Euclidean
  division of $n$ by $j$, as the assignment conjectured. ✓
* $T=R+(Q-1)(i-1)$; $h=\max\{0,\lceil (i-R)/Q\rceil\}$ (the ceiling
  glyph is legible in `-bbox`; F2.1's remark that the manuscript's
  "$h\le\lceil i/2\rceil$" line confirms the ceiling is also correct). ✓
* $\Lambda_i(T)=\prod_{q\ge i,\,q\text{ prime}}q^{\lfloor\log_q T\rfloor}$
  for $T\ge1$, $\Lambda_i(0)=1$, described in the manuscript as the part
  of $\mathrm{lcm}(1,\dots,T)$ supported on primes at least $i$. ✓
* Divisibility $V_i(n)\mid\Lambda_i(T)\binom jh$. In `-layout` text this
  prints garbled ("$V_i(n)\mid\Lambda_i(T)\ h j$"); `-bbox` word
  positions show $j$ directly above $h$ inside one binomial bracket
  after $\Lambda_i(T)$. Both provers' garbling notes are accurate. ✓
* Squared consequence $\binom ni<\bigl(\Lambda_i(T)\binom jh\bigr)^2$:
  in `-bbox`, the superscript $2$ follows a closing parenthesis
  enclosing both factors; this is also the only reading consistent
  with the manuscript's closing sentence ($\binom ni<V_i(n)^2$ via
  Theorem 1.2/Lemma 1.3). Both provers read it correctly. ✓
* The manuscript's proof mechanism ($c=n-j$, Lemma 2.1 residues
  $r,s$, $E=R+(Q-1)r-s$, the $E\ne0$/$E=0$ split, "every prime
  involved is greater than $h$") is quoted accurately by both. ✓

**No misquotation that matters exists in either file.** The
divisibility half (the only half either prover uses for SPLIT-odd)
does not depend on EEES78; only the squared consequence does, as
both provers state.

## 2. SPLIT-odd closure (task item 2)

The pinned case was checked bookkeeping-first, as instructed:

* $(Q,R)$ for $n=3j$: $Q=\lfloor 3j/j\rfloor=3$, $R=0$. Proposition 4.1's
  hypotheses hold for a counterexample: $3<j\le n/2$ and
  $\gcd(V_3(n),\binom nj)=1$ is the counterexample definition.
  $(3,0)$ row: $T=0+2\cdot2=4$, $h=\lceil 3/3\rceil=1$,
  $\Lambda_3(4)=3$, so $V_3(n)\mid 3j$. ✓ (recomputed: row table in §A
  of the verifier script).
* $U_0=n/3=j$ **exactly**: $n=3j$ with $v_3(n)=1$ gives $3\nmid j$, and
  $n$ odd gives $2\nmid j$; hence every prime factor of $j$ is $\ge5$,
  so the $\ge5$-part of $n$ is $j$ itself. ✓
* 3-part bookkeeping: $V_3(n)=U_0U_1U_2\cdot
  3^{v_3(n(n-1)(n-2))-1}$; in the pinned case $v_3(n)=1$ and
  $3\nmid(n-1)(n-2)$, so the exponent is $1-1=0$ and the 3-factor is
  $3^0=1$. Hence $V_3(n)=j\,U_1U_2$ with $\gcd(U_1U_2,3)=1$. ✓
* From $j\,U_1U_2\mid 3j$: cancelling $j>0$ gives $U_1U_2\mid3$, and
  coprimality to 3 forces $U_1=U_2=1$. This step is identical in both
  files and is sound. Edge cases: $j=5$ ($n=15$) is inside both
  arguments (no step needs $j\ge7$); the pinning input A1.16(iv)
  requires $n>9$, and for $n\le9$ the only admissible pair is
  $(9,4)$, closed by the standing $j\le 3i/2$ range / the sweep, as
  F1.5 notes. The $U_1U_2=1$ subcases are handled separately by each
  prover (next bullet). ✓

Endgames — genuinely different, both sound:

* **F1 (Claim F1.4):** $U_2=1$ alone suffices. $n-2$ is odd ($n$ odd)
  and $n-2\equiv1\pmod3$ ($3\mid n$), so $n-2$ has no prime factor
  $2$, $3$, or $\ge5$; hence $n-2=1$, $n=3$, contradicting $j=n/3>1$.
  Sound, including the subcase $n-2=3^d$ (excluded mod 3) and
  $n-2=2^a$ (excluded by parity). ✓
* **F2 (Theorem F2.7):** uses both $U_1=U_2=1$: $n-1=2^a3^b$ ($a\ge1$),
  $n-2=3^d$; $d=0$ gives $n=3$; $d\ge1$ forces $b=0$ (since
  $n-1=3^d+1\equiv1\pmod3$), so $2^a-3^d=1$, and Lemma F2.6 (elementary,
  audited: $d=0\Rightarrow(a,d)=(1,0)$; $d\ge1\Rightarrow a$ even,
  $(2^k-1)(2^k+1)=3^d$, $3^t-3^s=2$ forces $s=0$, giving $(2,1)$)
  forces $n=5$, which has $v_3(n)=0\ne1$. Sound. ✓

F2's route additionally rests on its **self-contained** proof of
Proposition 4.1 at $i=3$ (Lemma F2.2 + Theorem F2.3), audited line by
line in the F2 table below and found sound; F1's route rests on the
extracted manuscript proposition, whose proof the manuscript itself
supplies via its Lemma 2.1. The two routes share the
$V_3(n)=jU_1U_2$ decomposition and the $U_1U_2\mid3$ step, and both
depend on the Cycle 1 pinning (A1.16(iv), verified above against
P-A1.md: $n>9$, $v_3(n)=1$, $j=n/3$).

**Verdict: SPLIT-odd is certified closed by two independent routes.
Either route alone suffices.**

## 3. Claim-by-claim table: P-F1

| Claim | Status | Verifier's note |
|---|---|---|
| F1.1 (Prop. 4.1 extraction) | **PROVED** | Matches independent PDF extraction (§1 above) in full, including the `-bbox` resolution of $\binom jh$ and of the squared consequence. |
| F1.2 ($i=3$ specialisation) | **PROVED** | Case table recomputed: $(2,0){:}\ T{=}2,h{=}2,\Lambda{=}1$; $(3,0),(2,2){:}\ \Lambda_3(4)\binom j1=3j$; $(3,2),(4,0){:}\ 15j$. $\Lambda_3$ values $3,3,15,105,105$ at $T=3,4,6,7,8$ recomputed exactly. |
| F1.3 (pinned condition set) | **PROVED** | All items re-derived (§2): $R(n)=j$, (N1) specialisation ($p\ge5\mid\binom n2\iff p\mid j$ or $p\mid n-1$), (N2) $V_3(n)=jU_1U_2\mid\binom j3$, $U_1U_2\mid(j-1)(j-2)/6$ (RHS integral, as argued). |
| F1.4 (no $n=3j$ counterexample) | **PROVED** | See §2. Uses only the divisibility half of Prop. 4.1; the $(8,3)$ exception note is correct (divisibility needs no EEES input; $n=3j$ odd case has $n\ne8$ anyway). |
| F1.5 (no odd-$n$ counterexample) | **PROVED** | Follows from A1.16(iv) pinning + F1.4; the $n\le9$ residue is covered as stated. |
| F1.6 (other levers) | (a) **PROVED** (computation); (b) **PROVED**; (c) **OPEN** as self-labelled | (a) Recounted exactly: $111{,}110$ pinned triples to $10^6$ ($j\ge5$), $3{,}472$ pass (N2) alone, smallest $(129,43)$ with $(U_1,U_2)=(1,127)$, and $43\bmod127=43>2$ kills it under (LD3). (b) Correct scope argument: a prime $\ge5$ of $n-2$ divides neither $j$ nor $n-1$ (any common divisor of $j$ and $n-2=3j-2$ divides 2), so (N1) does not see it. (c) Honestly labelled GAP/OPEN; not used downstream. |
| F1.7 (prime power $>(n-1)/3$) | **PROVED** | Cofactor $s=(n-1)/q<3$; $s=2$ would make $n-1$ even, so $s=1$, $q=n-1>j>j-1$, cannot divide $j$ or $j-1$. |
| F1.8 (size bound $n\le3j(j-1)+1$) | **PROVED** | $R(n-1)\in\{n-1,(n-1)/3\}$, $X_0X_1\le j(j-1)$ for $j>1$; companion (N2) bound $n<\frac32j^3+1$ and its strict weakness for $j>2$ also check; $Q=2$ vacuity arithmetic correct. |
| F1.9 (label-retaining Prop. 4.1, even) | **PROVED** | (a) $h=0$: $q^a\mid\Lambda_3(T)\Rightarrow q^a\le T$; $p\ge5$ parts of $V_3$ are the exact prime powers. (b) $p>T\Rightarrow p\nmid\Lambda_3(T)\Rightarrow P\mid j$, and $P\mid n-r=Qj+(R-r)$ then forces $r=R$ since $0<|R-r|\le2<P$. |
| F1.10 (four even $(Q,R)$ subfamilies) | **PROVED** | Each case re-audited: $(3,0)$: $U_{n-1}\mid\gcd(j,3j-1)=1$ then $m=1$ contradiction; $(2,2)$: $m=3^b$, $b\le2$ via $3^{b-1}\mid3j$, $3\nmid j$, giving $j\in\{0,1,4\}$; $(3,2)$: $p\ge7$ parts divide $\gcd(j,3j+1)=1$, $m=5^a$, $a=1$ forced and $3j+1=5$ unsolvable; $(4,0)$: $m\in\{1,3,9,5,15,45\}$, integral $j$ only $1,4$. |
| F1.11 (even residual class) | **OPEN** (as labelled); embedded computation **PROVED** | The necessary conditions (i)–(v) are accurate restatements of F1.7–F1.10. The $(4,2)$ illustration was recomputed from scratch (§5 below): exactly $(22,5),(46,11),(106,26)$, each failing (LD3), gcds $77,69,371$ confirmed. Note: the sharpest combined residual also intersects F1.16/F1.17, i.e. $j>2000$ and $n>10^6$; F1.11's class as stated (after §§2–3 only) is a valid, slightly larger necessary class. |
| F1.12 (Del Pin at $i=3$ iff $j\le5$) | **PROVED** | Ratio $\rho_j=4(2j-1)/(j-2)=8+12/(j-2)\le11$ for $j\ge6$ while $\binom j3\ge20$; $j=4,5$ checked directly ($56\ge16$, $120\ge100$). |
| F1.13 ($V_3$-refined comparison) | **PROVED** | $V_3(n)=\binom n3/2^{v}$ exactly; counterexample $\Rightarrow V_3(n)\le\binom j3$; $\rho_j>8$ gives the uniform $v_2\le3$ closure. Threshold table recomputed exactly: $n_0(j,4)=14,17,19,24,49$ and $n_0(j,5)=17,20,24,30,62$ for $j=6,7,8,10,20$. |
| F1.14 (direction of $v_2$ condition) | **PROVED** in its labelled content; **GAP** in its final sentence | The labelled claim — largeness of $v_2$ does *not* close; the closing condition is the upper bound — is correct, and the sharpness witness verifies exactly: $v_2(\binom{16}3)=v_2(560)=4$, $V_3(16)=35=\binom73$, $\gcd(V_3(16),\binom{16}7)=5$. But the final sentence ("the comparison does not by itself close **any** full pair $(3,j)$, $j>5$") is asserted without proof: it needs, for every $j>5$, an $n\ge2j$ with $V_3(n)\le\binom j3$, and the verifier's search found **no such $n\le200{,}000$ at all for $j=6$ or $j=10$**, so the sentence is unproved and may fail there. No downstream claim depends on it (pairs $(3,6)$, $(3,10)$ are closed by F1.16/F2.18 regardless). |
| F1.15 (sweep row $i=3$) | **PROVED** (file read, as labelled) | Independently read from `pairpass_20000.json`: `cleared_js_by_i['3']` is exactly $[5,\dots,158]$, 154 values, contiguous. $N(3,158)=19{,}926$ recomputed. |
| F1.16 ((LD3) per pair, $j\le2000$) | **PROVED** (computation, fully recounted) | Independent recount reproduces F1's own §B counts **exactly**: $18{,}178$ candidate $n$, $148{,}591$ candidate pairs, **zero survivors**. With the $n\le N(3,j)$ filter applied up front the verifier tested $107{,}220$ pairs, also zero. Completeness of the $n=d\cdot t$ enumeration is a restatement of the definition of $R(n)$, as stated. Hence $(3,j)$ closed for all $n$, $5\le j\le2000$, modulo the standing finite reduction. |
| F1.17 ((LD3) to $n\le10^6$) | **PROVED** (computation, fully recounted) | (a) Odd pinned family: $111{,}110$ tested, zero (LD3) survivors (recounted). (b) Full search: verifier's pair total **$7{,}085{,}360$, exactly F1's count**, zero survivors. One immaterial convention difference: F1's "$611{,}107$ values of $n$ with candidates" counts $n$ having at least one $j$-candidate; the verifier's $R(n)\le n/2$ count is $611{,}108$, the extra value being $n=6$ ($R(6)=1$ but no $j\ge4$ with $j\le3$). The §C cross-checks in F1's log were also reproduced: $\ge5$-only survivors for $n\le2000$ are exactly the six pairs $(10,5),(28,14),(82,41),(162,70),(244,122),(730,365)$; full (LD3) survivors: none. |
| F1.18 (summary) | **PROVED** as a summary; open items correctly **OPEN** | Items 1–6 match the audited claims above. Same sharpening note as F1.11: the residual class in the "Reduced" bullet should be read intersected with items 5–6 ($j>2000$, $n>10^6$). (H3) and the higher-digit route are correctly left open; no overclaim. |

## 4. Claim-by-claim table: P-F2

| Claim | Status | Verifier's note |
|---|---|---|
| F2.1 (Prop. 4.1 extraction) | **PROVED** | Matches independent PDF extraction (§1). The garbling note is exact: only the placement of $\binom jh$ and of the exponent $2$ needs `-bbox`; the ceiling reading is confirmed by the $E=0$ analysis as well as by position data. |
| Lemma F2.2 (localisation at $i=3$) | **PROVED** | Audited: uniqueness of $t$ ($p\ge5$: $a=v_p$ of the product, one factor; $p=3$: the divisible factor has valuation $a+1$, so $3^a$ divides it); $n\bmod p^a=t$ since $0\le t\le2<p^a$; Kummer digitwise argument gives $r+s=n\bmod p^a=t<3$ for the least residues of $j$ and $c=n-j$. Also verified computationally (see F2.5 row). |
| Theorem F2.3 (Prop. 4.1 at $i=3$, self-contained) | **PROVED** | Audited: $E\ne0$ bound $|E|\le\max\{T,|R-2|\}=T$ ($T\ge R+2$ for $Q\ge2$); $p^a\le T\iff p^a\mid\Lambda_3(T)$; $E=0$ gives $r<h$ in both the integral and non-integral cases for $(3-R)/Q$, and is impossible for $R\ge3$ ($h=0$ ✓); assembly via pairwise coprimality, grouping parts by target factor $j-r$, and $\gcd(P_0,h!)=1$ (primes $\ge3>h$, $h\le2$). Specialisation table recomputed in full (all 12 rows). The $(2,0)$ sharpening note $\binom j2<\binom j3$ for $j>5$ is correct. |
| Corollary F2.4 (per-part dichotomy) | **PROVED** in substance; wording flaw (minor **FALSE**) | The dichotomy "at least one of (i) $p^a\le T$, (ii) $p^a\mid j-r$, $r<h$" is proved. The words "**exactly one**" are literally false as a property statement: a part can satisfy both (e.g. $p^a\mid j$ and $p^a\le T$); what the proof gives is a partition by the sign of $E$ for the canonical residues. Only the at-least-one form is used downstream (notably F2.9), so nothing is affected. The $h\le1$ consequence and the $p=3$ caveat ($3^{e-1}$, one factor below the (LD3) power $3^e$) are correct. |
| Computation F2.5 (random check of F2.2/F2.4) | **GAP** (documentation only) | No script and no seed exists in the workspace for F2, so the exact counts (4000 pairs, 840 instances) are **UNRECOUNTED as stated**. The substance was verified independently: the verifier's own seeded run (seed 20261029, same ranges) produced 834 qualifying prime-power instances with **0 failures** of Lemma F2.2 and of the dichotomy. The lemma is in any case proved (F2.2 row), so this computation is corroboration only. |
| §2.1 (pinned condition set) | **PROVED** | Same content as F1.3, re-derived in §2 above. The (N1) line is stated as an "in particular" (primes dividing $3j-1$); it is correct as far as it goes. The remark that even (N2)'s divisibility form does not close the case is consistent with F1.6(a)'s count of (N2)-only passes. |
| Lemma F2.6 ($2^a-3^d=1$) | **PROVED** | Elementary argument audited; solutions exactly $(1,0),(2,1)$. |
| Theorem F2.7 (SPLIT-odd empty) | **PROVED** | See §2. Valid for any $j>3$ in the pinned shape; no use of (LD3), (N1), (N2), or EEES78, as F2.8 states. |
| Claim F2.8 (status of Task 2) | **PROVED** | Accurate summary of F2.7 and its inputs (Kummer only, via F2.2/F2.3). The §5 consistency check is indeed weaker and independent. |
| Theorem F2.9 (genuine split parts $\le T$) | **PROVED** | For $(Q,R)\ne(2,0)$, $h\le1$ (checked all cases), so F2.4 gives $q\mid j$ or $q\le T$; a genuine split part divides some $j-s$, $s\in\{1,2\}$, and cannot also divide $j$ (else $q\mid s\le2<5\le q$). |
| Corollary F2.10 ($Q=2$, $>n/3$ factor) | **PROVED** | $T=n-2j+2<n/3\iff j>n/3+1$ (algebra checked). Part (b): a second relevant factor of $R(n-1)$ is $\ge5$ (a $3$-power factor would be $\ge9$), giving $R(n-1)\ge5q> n-1$, contradiction; hence $R(n-1)=q\in\{n-1,(n-1)/3\}$; $q=n-1$ contradicts $q\mid j\le n/2$; the remaining sub-configuration is exactly as stated. |
| Corollary F2.11 (single prime power $R(n-1)$) | **PROVED** | Direct from F2.9 plus $q\in\{n-1,(n-1)/3\}$ in the §3 even-$n$ setting; $j<(n-1)/3\Rightarrow q>j$. |
| Proposition F2.12 ($V\mid3j$ rows, even) | **PROVED** | $U_r\mid V_3(n)\mid3j$ and $\gcd(U_r,3)=1$ give $U_r\mid j$; pairwise coprimality gives $U_0U_1U_2\mid j$; the $3^{e-1}$ statement follows by dividing $V_3(n)\mid3j$ through by $U_0U_1U_2$. (Row $(2,1)$ is parity-impossible for even $n$, correctly not listed.) |
| Proposition F2.13 ($h=0$ combined bound) | **PROVED** | $V_3(n)\mid\gcd(\binom j3,\Lambda_3(T))$ from F2.3 + (N2). Example $(2,4)$: $T=6$, $\Lambda_3(6)=15$, $U_0U_1U_2\mid15$, $e\le2$ — all recomputed. "Not excluded in general" is honest. |
| Claim F2.14 (SPLIT-even residual) | **OPEN** (as labelled) | The (E-res 1)/(E-res 2) description accurately collects F2.3/F2.4/F2.9/F2.12/F2.13. Two non-fatal notes: the "$j\ge159$" bound inside this claim is superseded within the same file by F2.19 ($j\ge5001$), which the §7 summary uses — the claim as written is true but not sharpest; and the growth remark $\Lambda_3(T)=e^{(1+o(1))T}$ is a PNT-level assertion not proved in the file, used only as heuristic explanation of where the proof stops, not as a step. |
| Theorem F2.15 ($v_2\le3$ closes) | **PROVED** | Same argument as F1.13, audited: $\binom{2j}3/\binom j3=4(2j-1)/(j-2)>8\iff2j-1>2j-4$; valid for $j\ge3$; no EEES input (key lemma only). |
| Corollary F2.16 | **PROVED** | (i) $v_2(\binom n3)\ge4\iff v_2(n(n-1)(n-2))\ge5$ (subtracting $v_2(6)=1$). (iii) Density: dependence on $n\bmod32$ argued correctly (a factor $\equiv0\pmod{32}$ already gives valuation $\ge5$; otherwise each valuation $<5$ is read off mod 32); verifier's recount: exactly **27 of 32** residue classes have $v_2(\binom n3)\le3$. |
| Claim F2.17 (sweep row) | **PROVED** (file read, as labelled) | Same independent read as F1.15: $[5,\dots,158]$, 154 values. Consistency values recomputed: $N(3,158)=19{,}926\le20{,}000<20{,}181=N(3,159)$. |
| Computation F2.18 ((LD3) per pair, $j\le5000$) | **PROVED** (computation, fully recounted) | Verifier's independent recount (different enumeration and factorisation): $50{,}489$ candidate $n$ with $R(n)\le5000$ up to $N(3,5000)=20{,}263{,}871$; $341{,}633$ pairs tested with the $n\le N(3,j)$ filter ($107{,}220$ of them at $j\le2000$); **zero solutions for every $5\le j\le5000$**. Cross-validation by a second, brute-force implementation over **all** $n\in[2j,N(3,j)]$ for $5\le j\le60$ (no candidate shortcut): zero, agreeing with F2.18's stated cross-check. $N(3,2000)$ and $N(3,5000)$ recomputed exactly and match. |
| Corollary F2.19 (pairs $(3,j)$, $j\le5000$, closed) | **PROVED** modulo F2.18 and the standing finite reduction | The deduction is correct: a counterexample would have $n\le N(3,j)$ (sole $i=3$ EEES exception $(8,3)$ admits no $j\ge5$) and would satisfy (LD3). "Frontier within the range computed" is stated with the correct caveat; $j>5000$ is left **OPEN**, correctly. |
| Computation F2.20 (pinned family to $10^6$) | **PROVED** (computation, recounted) | Verifier's recount: $111{,}109$ candidates with $j=n/3\ge7$, **zero (LD3) survivors** — exactly F2's count. The one-count difference against F1.17(a)'s $111{,}110$ is fully explained: F1 counts $j\ge5$, F2 counts $j\ge7$, and $(15,5)$ is the unique pinned triple between the two conventions. |
| Computation F2.21 (even (LD3) to $10^6$) | **PROVED** (computation, recounted exactly) | Verifier's recount reproduces both counts **exactly**: $604{,}976$ pairs tested at $n\le10^5$ and $6{,}974{,}117$ at $n\le10^6$ (even $n$, $j\ge7$), **zero survivors** in both ranges. (F2's file is the record here, as the assignment instructed: the corrected figures in the file are the ones that reproduce. The verifier's combined all-parity total at $j\ge4$ is $7{,}085{,}360$, matching F1.17(b), so the two provers' searches are mutually consistent.) |
| §6 computation log | **PROVED** with two immaterial exceptions | Item 4: all eight $N(3,j)$ values recomputed exactly ($27$; $7{,}908$; $19{,}926$; $20{,}181$; $201{,}728$; $808{,}934$; $3{,}239{,}787$; $20{,}263{,}871$). Items 5–7: recounted (F2.18/F2.20/F2.21 rows; runtimes not verifiable and immaterial). Item 2: see F2.5 (substance verified, exact counts unrecounted). Item 3: the verifier's count of $n\in[3,10^5)$ with $v_2(\binom n3)\le3$ is $84{,}375$, i.e. fraction $0.84375$ ($=27/32$), against F2's reported $0.84376$ — a one-count endpoint-convention difference, immaterial to Corollary F2.16, whose density statement is exact. Item 1: §1 above. |
| §7 closing statement | **PROVED** as a summary; open items correctly **OPEN** | The "newly proved" list matches the audited claims; the residual-class and $(H_3)$ items are correctly left open, with the sharpest in-file frontier ($j\ge5001$, $n>10^6$ in the searched families, $v_2(\binom n3)\ge4$, $n\ne2j$) used here. No overclaim: $i=3$ and #699 are explicitly not claimed proved. |

## 5. The (4,2) residual illustration (task item 4) — full recomputation

For $(Q,R)=(4,2)$: $T=8$, $\Lambda_3(8)=105$, $V_3(n)\mid105j$,
$m=n-1=4j+1$, $\gcd(j,m)=1$. The Proposition 4.1 + $(n-1)$ argument
(F1.9(b) for the prime factors $>T$; the $3$-, $5$-, $7$-part bounds
from $V_3(n)\mid105j$ with $3,5,7\nmid j$) leaves $m=3^b5^a7^c$ with
$b\le2$, $a,c\le1$, $m\equiv1\pmod4$. The verifier enumerated all such
$m$: the candidates with $j=(m-1)/4\ge5$ are **exactly**
$(n,j)=(22,5)$ ($m=21=3\cdot7$), $(46,11)$ ($m=45=3^2\cdot5$),
$(106,26)$ ($m=105=3\cdot5\cdot7$) — no others. Each fails (LD3)
with explicit witnesses ($(22,5)$: $q=11\mid n$, $5\bmod11=5>0$;
$(46,11)$: $q=23\mid n$; $(106,26)$: $q=53\mid n$), and the direct
gcds recompute **exactly** as claimed:
$\gcd(V_3(22),\binom{22}5)=77$,
$\gcd(V_3(46),\binom{46}{11})=69$,
$\gcd(V_3(106),\binom{106}{26})=371$. F1.11's per-instance disposal
is confirmed; it is, as F1 states, per-instance only.

## 6. Bottom line for Cluster F (task item 6)

**Certified for $i=3$:**

1. **SPLIT-odd is closed** — no counterexample with $n$ odd, for any
   $j$. Certified by two independent routes: F1 (manuscript
   extraction + $U_2=1\Rightarrow n-2=1$) and F2 (self-contained
   Kummer proof of Prop. 4.1 at $i=3$ + the $2^a-3^d=1$ endgame).
   Both rest on the Cycle 1 pinning (A1.16(iv)) as standing input
   and on the divisibility $V_3(n)\mid3j$ at $(Q,R)=(3,0)$, whose
   extraction from Price's manuscript is verified faithful.
2. **Price Proposition 4.1 is extracted faithfully by both provers**
   (divisibility, $\Lambda_i$, $T$, $h$, hypotheses, squared
   consequence); F2's $i=3$ case is moreover proved in-file.
3. **Per-pair frontier: $j\le5000$.** (LD3) has no solution with
   $2j\le n\le N(3,j)$ for any $5\le j\le5000$ (F2.18, fully
   recounted; F1.16's $j\le2000$ subsumed, its counts reproduced
   exactly). Hence the pair $(3,j)$ admits no counterexample for any
   $n$, for every $5\le j\le5000$. The sweep row alone ($j\le158$)
   is also confirmed.
4. **Bounded search: (LD3) has zero solutions with $n\le10^6$**, all
   parities and both SPLIT families, with F1's total
   ($7{,}085{,}360$ pairs) and F2's even-family counts
   ($604{,}976$ / $6{,}974{,}117$ pairs) reproduced exactly.
5. **Even-case partial results as stated**: F1.7's $>(n-1)/3$
   prime-power exclusion, F1.8's $n\le3j(j-1)+1$, F1.9's
   label-retaining bounds, F1.10's closure of
   $(Q,R)\in\{(2,2),(3,0),(3,2),(4,0)\}$; F2.9–F2.13's split-part
   bound $q\le T$, the $Q=2$ corollaries, $U_0U_1U_2\mid j$ in the
   $V\mid3j$ rows, and the $h=0$ gcd bound.
6. **$v_2$ refinement (both provers)**: $v_2(\binom n3)\le3$ closes
   $(n,3,j)$ for every $j$ and $n\ge2j$; every $i=3$ counterexample
   has $v_2(\binom n3)\ge4$; the closed set of $n$ has density
   $27/32$. Del Pin's unrefined criterion at $i=3$ is exactly
   $j\le5$.

**What remains OPEN (correctly labelled by both provers):**

* The even residual class (F1.11 / F2.14 (E-res 1)/(E-res 2)) in
  general. Intersecting everything certified, a counterexample at
  $i=3$ must now have: $n$ even, $j\ge5001$, $n>10^6$,
  $v_2(\binom n3)\ge4$, $n\ne2j$, $(Q,R)\notin\{(2,0),(2,2),(3,0),
  (3,2),(4,0)\}$, and must satisfy (LD3), (N1), (N2), the
  $T$-boundedness/label conditions of F1.9/F2.4, and
  $V_3(n)\mid\Lambda_3(T)\binom jh$.
* (H3) in general, per-pair (LD3) closure for $j>5000$, and the
  higher-digit Kummer route (F1.6(c)).
* Minor items: F1.14's final sentence (GAP, §3 table); F2.4's
  "exactly one" wording (false literally, harmless); F2.5's exact
  sample counts (unrecounted for lack of a script/seed; substance
  verified on an independent sample).

**$i=3$ is not closed in general, (H3) is not proved, and #699 is
not claimed solved — both provers state exactly this, and the
verifier concurs.**

— V-F
