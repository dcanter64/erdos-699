# Verifier C (independent): Strategy S3 proof campaign, Erdős #699

**Scope.** I did not write either proof. I classified every numbered
lemma/theorem in `proofs/P-C1.md` (C1.1–C1.8) and `proofs/P-C2.md`
(C2.1–C2.11), re-derived the core mechanism myself, ran my own
bounded Python checks (sieve to $2.3\cdot10^6$, exhaustive small-case
trichotomy, exact-$N$ boundary pairs with full-interval scans,
literal gcd brute force on the small example pairs, total wall time
under 35 s), performed a third recount of the C2 count directly from
`erdos-699/pairpass.json`, and audited the external citations by web
search. All theorem verdicts are conditional on the campaign's
established inputs (Phase 0 reduction, EEES78 discharge, $n\le 10000$
sweep), which both provers take as given and which are outside S3.

---

## 1. My re-derivation of the trichotomy and the GAP corollary

For prime $p$ with $n/2 < p \le n$ and $1 \le k \le n/2$, Legendre's
formula collapses: $\lfloor n/p\rfloor = 1$, $p^2 > n$ kills all
$e\ge2$ terms, $\lfloor k/p\rfloor = 0$, and
$\lfloor (n-k)/p\rfloor \in \{0,1\}$ according as $n-k < p$ or
$n-k \ge p$. Hence $v_p\binom{n}{k} = 1$ iff $k > n-p$, else $0$.
Specialising to $k=i,j$ gives the trichotomy: primes in $(n-i,n]$
divide **both** coefficients (to the first power, and $p>i$);
primes in the annulus $(n-j,\,n-i]$ divide $\binom{n}{j}$ only
("wasted"); primes in $(n/2,\,n-j]$ divide neither. The naive claim
that every prime in $(n-j,n]$ divides both is false, because
$j>i$ gives $(n-i,n] \subsetneq (n-j,n]$.

**GAP corollary.** If $(n,i,j)$ were a counterexample, $(n-i,n]$
must be prime-free, so $p_-(n) \le n-i$ and, since $p_+(n)\ge n+1$
(integers), the straddling gap satisfies $p_+(n)-p_-(n) \ge i+1$.
The $+1$ is exact and is what makes the table criterion
$i \ge G(N(i,j))$ (not $i \ge G-1$) the right hypothesis. Both
provers' derivations agree with mine line for line.

**My computational confirmation.** Exhaustive check for all
$n \le 200$, every prime $p\in(n/2,n]$, every $k\le n/2$:
135,569 prime–$k$ checks, **0 violations** of
$p\mid\binom{n}{k} \iff k > n-p$. Naive-claim counterexample
recomputed: $\binom{20}{9}=167960\equiv0\pmod{13}$,
$\binom{20}{3}=1140\equiv9\pmod{13}$, with $13\in(11,17]$ the wasted
annulus for $(n,i,j)=(20,3,9)$.

## 2. Mandatory check 1: T-A off-by-one, boundary pairs, gcd brute force

My sieve reproduces the record table exactly in range: gap 132 first
after prime $1357201$, next record gap 148 after $2010733$; hence
$G(1400000)=132$ (the claimed $G(1{,}400{,}000)=132$ is **correct**),
and the strict-lower-end convention behaves as both provers state:
$G(1357201)=118$, $G(1357202)=132$, $G(2010733)=132$,
$G(2010734)=148$.

Exact $N(i,j)$ (binary search, each value verified by exact integer
neighbour checks $\binom{N}{i}<T\le\binom{N+1}{i}$), $i=132$, with a
full scan of $[2j,\,N(i,j)]$ counting $n$ with $(n-132,n]$
prime-free (by §1 such an $n$ is exactly where this route can fail;
a prime in the interval divides both coefficients):

| $j$ | $N(132,j)$ | $G(N)$ | criterion $132\ge G(N)$ | prime-free $n$ in $[2j,N]$ |
|---|---|---|---|---|
| 8194 | 1,357,021 | 118 | holds | 0 |
| 8195 | 1,357,355 | 132 | holds **by equality** | 0 |
| 9959 | 2,010,328 | 132 | holds | 0 |
| 9960 | 2,010,734 | 148 | **fails** | 0 |
| 9961 | 2,011,141 | 148 | fails | **16** ($n=2010865\ldots2010880$) |

Reading of the boundary behaviour, all consistent with T-A as
proved (sufficiency, not necessity): crossing $1357201$ raises
$G$ to exactly $132=i$, and the criterion still fires — a gap of
length exactly $i$ can never straddle an $n$ with $(n-i,n]$
prime-free, because that needs gap $\ge i+1$. At $j=9960$ the
criterion fails but no prime-free $n$ exists yet: the new gap's
lower end $2010733$ exceeds $N-i$, so it cannot straddle any
$n\le N$; $G$ is conservative by up to $i$ at its right edge. At
$j=9961$ the gap becomes usable and exactly $148-132=16$ prime-free
$n$ appear, as predicted. This is a sharp, quantitative confirmation
of both off-by-ones (the $+1$ in GAP and the strict $p_k<X$ in $G$).

**Small C3 example, literal gcd brute force.** $N(17,71)=621$,
$G=18>17$: criterion **fails** for $i=17$, as claimed.
$N(18,71)=578$, $G=18\le18$: criterion **holds** for $i=18$, as
claimed. Literal check: $\gcd(\binom{n}{17},\binom{n}{71})>1$ for
**every** $n\in[142,621]$, and
$\gcd(\binom{n}{18},\binom{n}{71})>1$ for **every** $n\in[142,578]$ —
so the $i=17$ pair is in fact cleared (by small primes $\le n/2$;
e.g. at $n=540$, $(523,540]$ is prime-free, 523 and 541 consecutive,
yet the gcd exceeds 1), illustrating sufficiency-not-necessity
exactly as both provers state.

## 3. Mandatory check 2: third recount of C2 and uniform clearance

**Recount from `pairpass.json` alone** (my code read $J_i$ as the
maximum of `cleared_js_by_i[i]`; I also verified every cleared list
is the contiguous prefix $\lfloor 3i/2\rfloor < j \le J_i$):

- Census: $\sum_{1\le i\le1000}\big(5000-\lfloor 3i/2\rfloor\big)
  = 4{,}249{,}500$; fully cleared $768{,}741$; partial $3{,}480{,}759$.
  All three match the file's own header fields and RESULTS.md.
- $\sum_{132\le i\le1000}(5000-J_i) = \mathbf{2{,}891{,}106}$ —
  **exactly the claimed count** (third independent computation:
  C1 from the file, C2 from thresholds, mine from the file again by
  a differently structured summation). Complementary sum for
  $1\le i\le131$ is $589{,}653$, and
  $2{,}891{,}106+589{,}653=3{,}480{,}759$. Spot values:
  $J_1=70$, $J_{132}=762$, $J_{500}=1597$, $J_{1000}=2391$;
  in-range: considered $3{,}607{,}436$, already cleared $716{,}330$,
  partial $2{,}891{,}106$.

**Uniform clearance logic.** By L4 (§6 below), for $i\ge132$,
$j\le5000$: $N(i,j) < e^2\cdot5000^2/132 = 1{,}399{,}442.44\ldots
< 1{,}399{,}443$. The exact statement I verified by my own sieve is:

> *The maximal prime gap with lower end $< 1{,}399{,}443$ is $132$.*
> Precisely: sieving to $1{,}500{,}000$, there is **no** prime gap
> $\ge 133$ with lower end $<1{,}500{,}000$ (maximal such gap: 132),
> which a fortiori covers all lower ends $<1{,}399{,}443$; sieving
> further to $2{,}300{,}000$ confirms the first gap $>132$ anywhere
> in range is the gap 148 with lower end $2{,}010{,}733$.

Hence $G(N(i,j))\le132\le i$ uniformly, T-A fires for every pair
with $132\le i\le1000$, $j\le5000$, no per-pair computation needed.
**Logic and count both PROVED.**

**C1-family arithmetic.** $e^2(7.35\cdot10^8)^2
= 3.9918\cdot10^{18} < 4\cdot10^{18}$ (ratio $0.99794$);
$\sqrt{4\cdot10^{18}/e^2} = 2\cdot10^9/e = 735{,}758{,}882$, so
$7.35\cdot10^8$ is inside with margin. **Correct.**

**Oliveira e Silva–Herzog–Pardi bound.** Bibliographic check:
*Empirical verification of the even Goldbach conjecture and
computation of prime gaps up to $4\cdot10^{18}$*, Math. Comp. 83
(2014), 2033–2060 — confirmed in multiple independent reference
lists; the OEIS first-occurrence compilation attributes gap 1476,
after prime $1425172824437699411$, to Oliveira e Silva (2009), and
secondary literature states the maximal gap below $4\cdot10^{18}$
is 1476 on the basis of that computation. **Honest dependence
classification: this is a published computational theorem taken on
trust.** Neither prover recomputed it (it is not recomputable at
campaign scale), and neither do I. Theorem C's part (C1) is
therefore PROVED *conditional on that published computation*;
part (C2) does not depend on it (its range is sieve-verified here
three times over).

## 4. Mandatory check 3: the B3 "strongest" disagreement — C2 is right

$$\frac{0.087}{\log^3 x} \le \frac{1}{5000\log^2 x}
\iff 0.087\cdot 5000 \le \log x \iff \log x \ge 435,$$
since $0.087\cdot5000 = 435$ exactly. So B3's coefficient is smaller
than B2's **only for $\log x > 435$** ($x > e^{435}\approx10^{189}$);
below that B2 is stronger. Numeric spot check at $\log x = 15$:
B1 $1.78\cdot10^{-4}$, B3 $2.58\cdot10^{-5}$, B2 $8.9\cdot10^{-7}$
(B2 smallest), matching C2's figures; at $\log x=436$ B3 first dips
below B2. B3 does beat B1 throughout its validity range
($0.087/\log^3x \le 1/(25\log^2x) \iff \log x \ge 2.175$, and
$\log 6034256 \approx 15.61$), which may be the source of the slip.

**Adjudication: C2 is correct; the remark in S3 and in P-C1
("strongest of the three whenever $\log n < 435$") is FALSE**
(algebraically reversed). It is not load-bearing: B1, B2, B3 are
each proved as independent regions in both documents, and no
numbered theorem depends on any comparison among them.

## 5. Mandatory check 4: citation audit

| Citation | Content used | My classification |
|---|---|---|
| Dusart 2010, arXiv:1002.0442, Prop. 6.8: $x\ge396738$, $C=1/25$, $m=2$ | B1 threshold/constant | **VERIFIED SECONDARY.** Threshold, constant and exponent appear identically in the Caffarelli survey table (*Mathematics* 2018, 6, 289, Thm. 6; arXiv:1804.02500) and in the Bertrand's-postulate survey statement of Dusart's 2010 result; the arXiv primary paper (title/author) is confirmed. I did not sight the "Prop. 6.8" label in the primary text in this audit; C1 claims verbatim primary verification of the statement — the load-bearing numbers are corroborated regardless. |
| Dusart 2018, *Ramanujan J.* 45, Cor. 5.5: $x\ge468991632$, $C=1/5000$, $m=2$ (and Prop. 5.4: $x\ge89693$, $C=1$, $m=3$) | B2 | **VERIFIED SECONDARY** (with internal numbering). The Bertrand's-postulate survey explicitly attributes Prop. 5.4 and Cor. 5.5 to Dusart with exactly these thresholds/constants/intervals, and the Caffarelli table matches. Journal, volume, pages and DOI (10.1007/s11139-016-9839-4) confirmed via independent reference lists. This matches C2's account and upgrades C1's Flag F2 concern: the numbering, not just the numbers, is secondarily attested. Primary text not sighted by me. |
| Axler 2017, arXiv:1703.08032, "Thm. 4.1": $x\ge6034256$, $C=0.087$, $m=3$ | B3 numbers; theorem-number label | Numbers **VERIFIED SECONDARY** (Caffarelli table row: 6034256 / 3 / 0.087 / Axler 2017 / 1703.08032). Paper confirmed on arXiv: Christian Axler, *New estimates for some functions defined over primes* (submitted 23 Mar 2017; abstract: "two new results concerning the existence of prime numbers in short intervals"). The **"Thm. 4.1" label is UNVERIFIABLE** in my audit: I could not confirm the internal numbering from the primary text. On this point C2's caution is vindicated and C1's "verified verbatim … (= Thm. 1.4)" could not be reproduced. Bibliographic gap only: the statement B3 uses is corroborated. |
| Trudgian 2014, arXiv:1401.2689 — C1 Flag F1 | not used | **Confirmed unused and conservative, as flagged.** Grep of both proofs: Trudgian appears only in C1's citation table, its §4 unnumbered remark, and Flag F1, and in C2's register note ("not used in Theorem C2.9"). Neither C1.7 nor C2.9 (the Theorem B statements) uses it. The survey value $2898329$ is what the Caffarelli table indeed prints; the threshold discrepancy $2898329 > 2898239$ is in the conservative direction for the only form in which it could ever be applied (a result assumed only for larger $x$). One nuance C1 understates: a closed-interval $[x,\cdot]$ guarantee, if it *were* used at $x=n-i$, would not by itself give a prime $>n-i$; since it is used nowhere in any theorem, this touches nothing downstream. |
| Oliveira e Silva, Herzog, Pardi 2014 | $G(X)\le1476$ for $X\le4\cdot10^{18}$ | **VERIFIED SECONDARY** bibliographically (see §3); the computation itself is a published computational theorem **taken on trust**, honestly labelled as such by both provers and here. |

## 6. Mandatory check 5: L4 algebra audit

Claim: $N(i,j) < e^2j^2/i$. The chain, audited step by step:

1. $\binom{2j}{2(j-i)} = \binom{2j}{2i}$ (symmetry, $2j-2(j-i)=2i$). ✓
2. Standard bound $\binom{N}{K}\le(eN/K)^K$ (from
   $\binom{N}{K}\le N^K/K!$ and $K!\ge(K/e)^K$) with $N=2j$, $K=2i$:
   $\binom{2j}{2i} \le \big(\tfrac{e\cdot2j}{2i}\big)^{2i}
   = (ej/i)^{2i}$. ✓ (Spot-checked numerically:
   e.g. $(i,j)=(17,71)$: $\binom{142}{34}\approx6.9\cdot10^{32}
   \le (ej/i)^{2i}\approx7.5\cdot10^{35}$.)
3. $\binom{n}{i}\ge(n/i)^i$ (term-wise
   $\frac{n-t}{i-t}\ge\frac{n}{i}\iff t(n-i)\ge0$). ✓
4. Contrapositive step: if $n \ge e^2j^2/i$ then
   $\binom{n}{i}\ge(n/i)^i \ge \big(e^2j^2/i^2\big)^i
   = e^{2i}(j/i)^{2i} = (ej/i)^{2i} \ge \binom{2j}{2(j-i)}$,
   so $n$ fails the strict defining inequality of $N(i,j)$; by
   monotonicity in $n$, every larger integer fails too. Hence
   $N(i,j) < e^2j^2/i$. ✓

C1's ceiling formulation
($N\le\lceil e^2j^2/i\rceil-1 < e^2j^2/i$) and C2's "no element of
the defining set reaches the bound" formulation are both valid
renderings of step 4. **The derivation closes; L4 is PROVED.**
Spot values from my runs: $N(132,5000)=500097$,
$N(1000,5000)=55305$, $N(17,71)=621$, all far below $e^2j^2/i$.

## 7. Classification tables

### P-C1 (8 numbered items)

| Item | Content | Verdict |
|---|---|---|
| C1.1 (L1) | $n-j<p\le n \Rightarrow v_p\binom{n}{j}=1$ | **PROVED** |
| C1.2 (L2) | $n-i<p\le n \Rightarrow v_p\binom{n}{i}=1$ | **PROVED** |
| C1.3 (L3 corrected) | trichotomy for $p\in(n/2,n]$; (i)/(ii)/(iii) | **PROVED** (my §1; exhaustive n≤200) |
| C1.4 (GAP) | counterexample $\Rightarrow$ $(n-i,n]$ prime-free, gap $\ge i+1$ | **PROVED** |
| C1.5 (L4) | $N(i,j) < e^2j^2/i$ | **PROVED** (§6) |
| C1.6 (T-A) | $i\ge G(N(i,j)) \Rightarrow$ pair fully cleared | **PROVED** (§2 boundary tests incl. equality case) |
| C1.7 (T-B) | regions B1/B2/B3 | **PROVED** as regions, conditional on the cited explicit theorems (numbers secondarily verified, §5). **One FALSE non-load-bearing clause**: "B3 … the strongest of the three whenever $\log n < 435$" (§4). Citation caveats: B2 secondary-only (its own Flag F2), Axler "Thm. 4.1" label unverifiable (§5). |
| C1.8 (T-C) | (C1) $i\ge1476$, $j\le7.35\cdot10^8$ cleared; (C2) $2{,}891{,}106$ pairs; (C3) per-pair criterion + $(i,71)$ example | **PROVED** — (C1) conditional on Oliveira e Silva et al. taken on trust; (C2) fully verified (§3); (C3) example recomputed (§2: criterion holds exactly for $i\ge18$ at $j=71$) |

Counts for P-C1: **8 PROVED, 0 GAP, 0 OPEN; 1 FALSE sub-clause**
(the comparative remark inside C1.7, also present in S3) and
**1 bibliographic GAP** (Axler theorem-number label), neither
load-bearing.

### P-C2 (11 numbered items)

| Item | Content | Verdict |
|---|---|---|
| C2.1 (L1) | as C1.1 | **PROVED** |
| C2.2 (L2) | as C1.2 | **PROVED** |
| C2.3 (L3 corrected) | $p\mid\binom{n}{k}\iff k>n-p$; (i)/(ii)/(iii); brief's claim (c) refuted with $(20,3,9,13)$ | **PROVED** (the refuted naive claim is correctly identified as false) |
| C2.4 (GAP) | gap forcing, $p_+-p_-\ge i+1$ | **PROVED** |
| C2.5 (auxiliary) | $\binom{N}{K}\le(eN/K)^K$; $\binom{n}{i}\ge(n/i)^i$ | **PROVED** |
| C2.6 (L4) | $N(i,j) < e^2j^2/i$ | **PROVED** (§6) |
| C2.7 (conversion) | explicit interval theorem $+$ $i\ge (n-i)C/\log^m(n-i)$ $\Rightarrow$ prime in $(n-i,n]$ | **PROVED** (strict lower end correctly identified as load-bearing) |
| C2.8 (T-A) | table criterion with strict $p_k<X$ convention; $G$ boundary values $G(2010733)=132$, $G(2010734)=148$ | **PROVED** (boundaries reproduced by my sieve) |
| C2.9 (T-B) | regions B1/B2/B3 restated | **PROVED** as regions, same citation caveats as C1.7 (§5). Its appended *correction* of the "strongest" remark is **PROVED correct** (§4). |
| C2.10 (T-C1) | $i\ge1476$, $j\le7.35\cdot10^8$ family | **PROVED**, conditional on Oliveira e Silva et al. taken on trust; arithmetic verified (§3) |
| C2.11 (T-C2) | $132\le i\le1000$, $j\le5000$ cleared; count $2{,}891{,}106$ | **PROVED** (third recount exact, §3; uniform argument sieve-verified) |

Counts for P-C2: **11 PROVED, 0 GAP, 0 FALSE, 0 OPEN** (the Axler
label caution in its §7 register matches my independent audit).

## 8. Final verdict per claim at stake (Strategy S3)

| Claim | Verdict |
|---|---|
| L1 / L2 / L3-corrected trichotomy for $p\in(n/2,n]$ | **PROVED** |
| Naive claim "every prime in $(n-j,n]$ divides both" | **FALSE** (correctly rejected by both provers; counterexample verified) |
| GAP: counterexample $\Rightarrow$ $(n-i,n]$ prime-free (gap $\ge i+1$) | **PROVED** |
| L4: $N(i,j) < e^2j^2/i$ | **PROVED** |
| T-A: $i \ge G(N(i,j)) \Rightarrow$ pair fully cleared | **PROVED** (off-by-ones computationally stress-tested, §2) |
| T-B: explicit region from B1 (Dusart 2010), B2 (Dusart 2018), B3 (Axler 2017) | **PROVED** as regions, on secondarily verified citations; Axler internal label **UNVERIFIABLE** (bibliographic only) |
| "B3 strongest for $\log n < 435$" (S3, repeated in P-C1) | **FALSE** — reversed; correct crossover is $\log(n-i)\ge435$ (C2's correction is right); not load-bearing |
| T-C (C1): $i\ge1476$, $j\le7.35\cdot10^8$ family | **PROVED**, conditional on Oliveira e Silva–Herzog–Pardi's published computation up to $4\cdot10^{18}$ (taken on trust, bibliographically verified) |
| T-C (C2): $2{,}891{,}106$ newly cleared pairs, $132\le i\le1000$ | **PROVED** — third recount from `pairpass.json` reproduces $2{,}891{,}106$ exactly; census $4{,}249{,}500$ / $768{,}741$ / $3{,}480{,}759$ all reproduced; uniform-clearance bound and $G\le132$ sieve-verified by me |

**Overall.** No numbered lemma or theorem in either document is
GAP, FALSE, or OPEN in its load-bearing content: 19 of 19 numbered
items are PROVED (two of them, the T-B regions and the T-C (C1)
family, conditional on published external results in the standard
way, with the dependencies honestly labelled above). The only
FALSE statement found anywhere is the non-load-bearing comparative
remark about B3 in S3/P-C1, which P-C2 already corrects; the only
GAP is bibliographic (Axler's "Thm. 4.1" label), which P-C2 already
flags. The two provers agree on every substantive claim, and my
independent computations agree with both.
