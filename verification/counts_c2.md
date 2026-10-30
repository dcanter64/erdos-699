# Cycle 2 Housekeeping Counts (HK-B) — Erdős #699 Proof Campaign

**Computation:** `verification/counts_c2.py` (Python stdlib only, exact
integer / `Fraction` arithmetic, single thread, runtime 66 s, peak memory
≈ 62 MB for the prime sieve). Machine-readable output:
`verification/counts_c2.json`. **Scope:** pairs $(i,j)$,
$1 \le i \le 1000$, $\lfloor 3i/2 \rfloor < j \le 5000$ — **4,249,500 pairs**.
**Baseline:** cap-20,000 sweep classification
(`erdos-699/pairpass_20000.json`), every row a clean prefix with frontier
$J_i^{20000}$; in-scope cleared count **1,302,183** (reproduced, not just
taken on trust).

---

## ⚠ Validation anchor failure in step (4) as written — read first

One of the task's validation anchors **fails**, and it fails for a
mathematical reason, not a coding one:

* The anchor $\mathrm{Bad}^{\sharp}(3,7) = \{16\}$ **holds** (verified two
  independent ways, §4).
* The anchor $J_K^{\sharp}(i) \ge J_K(i)$ for all $i$ **fails under the
  step-(4) definition as literally written** (pair sharp-cleared iff
  $\mathrm{Bad}^{\sharp}(i,j) = \varnothing$ over all $n \ge 2j$). It fails
  at **998 of the 1000 rows**. Counterexample, exact: at $i = 100$,
  $J_K(100) = 1045$, but $2j \in \mathrm{Bad}^{\sharp}(100, j)$ for **every**
  scope $j$ (already at the first scope point $j = 151$), so the literal
  sharp frontier is $J_K^{\sharp,\mathrm{lit}}(100) = 150 < 1045$. At
  $i = 3$: literal frontier $6 < 465 = J_K(3)$.

  The reason is structural, and it is exactly S1's Theorem C / Proposition
  B′: the crude $J_K$ of step (3) is a **sweep-relative** frontier (the
  predicate says $N_K(i,j) \le 10000$, i.e. every crude-bad $n$ lies inside
  the old sweep), whereas $\mathrm{Bad}^{\sharp}(i,j) = \varnothing$ is an
  **absolute, all-$n$** size closure, which S1 proved holds for essentially
  no scope pairs with $i \ge 4$ (the diagonal shortfall
  $\Delta(3/2) - 1 < 0$). Comparing the two frontiers mixes the two notions.

* Resolution used in this report: step (4) is reported in **three forms**.
  **L** is the task's literal definition, carried through the headline
  table in the task's stated order. **S10** and **S20** are the
  sweep-relative sharp criteria at caps 10,000 and 20,000 (pair cleared iff
  no sharp-bad $n$ exceeds the cap; S10 is the sharp analogue of S1's
  Theorem D, its follow-up V2). For both sweep-relative forms the anchor
  $J_K^{\sharp}(i) \ge J_K(i)$ **holds at every row (0 violations)**, and
  their full marginal chains (steps (5)–(7) recomputed after them) are
  given in §8. The coordinator can adopt either reading; the numbers for
  all three are exact.

* A second slip in the task text, corrected here: the sharp test's test
  points are $n = 2j$ and the **jump points $q$ themselves** (S1 Lemma 5),
  not $n = q-1$. At $(3,7)$ the unique bad point is $n = 16$, where
  $U^{\sharp}$ jumps $8 \to 16$; testing at $q - 1 = 15$ gives
  $G_3(15) = 455/8 > 35 = C(7,4)$ and would wrongly clear $(3,7)$,
  contradicting the $\{16\}$ anchor.

* A third expectation in the task text is not borne out: step (5) was
  expected to clear "few or zero" pairs. It clears **168,359** pairs in the
  headline chain (the exact count; the per-pair S3 criterion reaches
  $j = 5000$ for all $i \ge 114$). See §5.

---

## Conventions (as verified in Cycle 1)

* $C(a,b) = \binom{a}{b}$ (`math.comb`); note $C(j, j-i) = C(j, i)$ and
  $C(2j, 2(j-i)) = C(2j, 2i)$.
* $N(i,j) := \max\{n : C(n,i) < C(2j, 2(j-i))\}$ (Phase 0 / P-C convention),
  computed exactly by binary search on `math.comb`.
* $G(X) := \max\{p_{k+1} - p_k : p_k < X\}$ — maximal prime gap with
  **strict** lower end $p_k < X$ (P-C1 §3, P-C2 §3). S3 table criterion:
  pair cleared iff $i \ge G(N(i,j))$.
* S1 crude predicate (`union_check.py`): $(i,j)$ cleared iff
  $C(j,i) \cdot 10001^{\pi(i-1)} < C(10001, i)$; a prefix in $j$, frontier
  $J_K(i)$.
* $U^{\sharp}(n,i) = \prod_{p<i} q_p(n)$, $q_p(n)$ the largest power of $p$
  that is $\le n$; $G_i(n) = C(n,i)/U^{\sharp}(n,i)$;
  $F_i(n) = C(n,i)/n^{\pi(i-1)}$ (strictly increasing, S1 Lemma 4);
  $N_K(i,j) = \max\{n : F_i(n) \le C(j, j-i)\}$;
  $\mathrm{Bad}^{\sharp}(i,j) = \{n \ge 2j : C(n,i) \le U^{\sharp}(n,i)\,
  C(j, j-i)\}$. By S1 Lemma 5, $G_i$ is strictly increasing on intervals
  where $U^{\sharp}$ is constant and $U^{\sharp}$ jumps exactly at prime
  powers $p^e$ ($p < i$), so every local minimum of $G_i$ on $[2j,\infty)$
  is at $n = 2j$ or at a jump point $q$; and
  $\mathrm{Bad}^{\sharp}(i,j) \subseteq [2j, N_K(i,j)]$.

## Headline marginal table (task order, step (4) in its literal form L)

| Step | Criterion | Newly cleared | Running union | Remaining |
|---|---|---:|---:|---:|
| (1) | Baseline: sweep-20,000 frontiers $J_i^{20000}$ | 1,302,183 | 1,302,183 | 2,947,317 |
| (2) | S3 uniform: all scope pairs with $i \ge 132$ | 2,383,028 | 3,685,211 | 564,289 |
| (3) | S1 crude: $C(j,i)\,10001^{\pi(i-1)} < C(10001,i)$ | 17,085 | 3,702,296 | 547,204 |
| (4L) | S1 sharp, literal: $\mathrm{Bad}^{\sharp}(i,j) = \varnothing$ | 0 | 3,702,296 | 547,204 |
| (5) | S3 per-pair at $i \le 131$: $i \ge G(N(i,j))$ | 168,359 | 3,870,655 | 378,845 |
| (6) | Primorial R1 on $\lfloor 3i/2\rfloor < j < 2i$ | 0 | 3,870,655 | 378,845 |

**Full union (steps (1)–(6)): 3,870,655 of 4,249,500 cleared; 378,845
partial pairs remain in scope**, all at $3 \le i \le 113$ (§7). Step (7) is
parametric and is tabulated in §6.

Notes on the individual steps:

**(2)** Scope pairs with $i \ge 132$ number 3,607,436; the baseline had
already cleared 1,224,408 of them, so the uniform S3 theorem (Cycle 1,
verified) newly clears 2,383,028 and closes every row $i \ge 132$. All
later steps therefore only act at $i \le 131$.

**(3)** Against the new baseline the crude pay-off collapses from its
old-baseline value: the sweep-20,000 frontiers already exceed $J_K(i)$ on
most rows (e.g. $i = 4$: $J^{20000} = 180$ vs $J_K = 101$). The validation
targets on the **old** baseline reproduce exactly (see §3).

**(4L)** The literal sharp-cleared scope pairs are exactly: all of rows
$i = 1, 2$ (already cleared by step (3)) and $(3,5)$, $(3,6)$ (already
baseline-cleared). Marginal **0**. Proof of completeness is computational
and exact: the start ratio $R_i(j) = G_i(2j)/C(j,i)$ is strictly
decreasing in $j$ for $i \ge 2$ (its comb factor has
$D - N = i(i-1)(j+1) > 0$, an identity verified symbolically in the code
comments and on a grid in the script, and $U^{\sharp}(2j,i)$ is
nondecreasing), and $2j \in \mathrm{Bad}^{\sharp}(i, \lfloor 3i/2\rfloor+1)$
was verified exactly for **all 997 rows $4 \le i \le 1000$**; hence every
scope pair with $i \ge 4$ has a bad point at $n = 2j$ itself. Row $i = 3$
was scanned pair by pair (minima method): cleared exactly at $j = 5, 6$.

**(5)** See §5 — the second-largest marginal in the whole computation.

**(6)** Independent recount over all **249,500** R1-window pairs in scope
(exact incremental arithmetic): the criterion $P(i,j)^2 \le C(2j,i)$ fails
at exactly **$(4,7)$ and $(10,19)$**, confirming the two provers. Both are
already baseline-cleared (frontiers $J_4^{20000} = 180$,
$J_{10}^{20000} = 280$). Marginal **0** — in fact stronger: for every
$i \le 131$ the baseline frontier already satisfies
$J_i^{20000} \ge \min(2i-1, 5000)$, so every R1-window pair in scope was
cleared at step (1), before any other criterion ran.

## Validation results

* **Crude (step (3)) on the old baseline: PASS, exactly.**
  Newly cleared vs `pairpass.json` = **328,079** (target 328,079);
  $J_K(100) = 1045$ (target 1045); $J_K(1000) = 2541$ (target 2541).
* **Baseline: PASS.** In-scope count recomputed as **1,302,183**; every
  row verified to be a clean prefix $\lfloor 3i/2\rfloor < j \le
  J_i^{20000}$ in scope.
* **$\mathrm{Bad}^{\sharp}(3,7) = \{16\}$: PASS, twice.** By the Lemma-5
  minima method and by a direct brute-force scan of every
  $n \in [14, N_K(3,7)] = [14, 16]$ with exact $U^{\sharp}$; both give
  exactly $[16]$. Hence $(3,7)$ is **not** literal-sharp-cleared (it is
  baseline-cleared, $J_3^{20000} = 158$).
* **Sharp predicate vs brute force: PASS.** On 20 seeded pairs (fixed
  sample including $(3,5), (3,6), (3,20), (4,12), (5,8), (5,15), (10,30),
  $(10,100)$ plus seeded random pairs with $i \le 40$ and
  $N_K(i,j) \le 6000$), the minima method and a direct scan of all
  $n \in [2j, N_K(i,j)]$ agree on emptiness of $\mathrm{Bad}^{\sharp}$, and
  every bad point reported by the minima method is confirmed bad by the
  scan.
* **Prefix property of sharp-clearedness: PASS in every form.** Literal:
  the cleared set per row is a prefix by the decreasing-$R_i$ argument
  above plus the row-by-row checks (rows $i \ge 4$: empty; $i = 3$:
  $\{5,6\}$; $i = 1,2$: full). Sweep-relative (S10/S20): the predicate is
  $C(j,i) < M_i(T^*)$ with $M_i(T^*) = \min_{n \ge T^*+1} G_i(n)$ a
  constant in $j$ and $C(j,i)$ strictly increasing in $j$ — a prefix by
  construction; frontiers were additionally spot-verified by a direct
  per-pair test at $j = $ frontier and $j = $ frontier${}+1$ for
  $i \in \{3, 10, 50, 100, 131, 500, 1000\}$ in both forms: PASS.
* **$J_K^{\sharp} \ge J_K$ anchor: FAILS for the literal form** (998 of
  1000 rows; see the warning box), **PASSES for both sweep-relative
  forms** (0 violations each). Sweep-relative frontiers (samples):
  S10: $J^{\sharp}(3) = 497$, $J^{\sharp}(100) = 1381$,
  $J^{\sharp}(131) = 1764$, $J^{\sharp}(1000) = 3758$.
  S20: $J^{\sharp}(3) = 788$, $J^{\sharp}(100) = 2444$,
  $J^{\sharp}(131) = 2634$, $J^{\sharp}(1000) = 5000$.
  (Method for $M_i(T^*)$: minima candidates are $n = T^*{+}1$ and the
  prime powers in $(T^*, \mathrm{cap}]$, where cap is a float-estimated
  bound on $N_K(i, 5000)$ verified exactly by $F_i(\mathrm{cap}) >
  C(5000, i)$; beyond cap, $G_i \ge F_i > C(5000,i) \ge C(j,i)$, so no
  minimizer is missed.)
* **Gap function: PASS.** $G(10127) = 36$, $G(1\,400\,000) = 132$,
  $G(2\,010\,733) = 132$, $G(2\,010\,734) = 148$ — the strict-lower-end
  convention behaving exactly as P-C1/P-C2 record.

## Step (5) in detail: S3 per-pair at $i \le 131$

**Bounding before sieving.** At this step (headline chain) the uncleared
pairs have $3 \le i \le 131$ (rows 1–2 are fully cleared by step (3)) and
$j \le 5000$. By S3 Lemma 4, $N(i,j) < e^2 j^2 / i$, increasing in $j$ and
decreasing in $i$, so every remaining pair has
$N(i,j) < e^2 \cdot 5000^2 / 3 \approx 61\,575\,467.5$. The sieve limit
was set to **61,575,468** $< 2 \times 10^8$, so a **plain (non-segmented)
bytearray sieve** was used (61.6 MB). It found **3,649,967 primes** and
the record-gap table (gap, lower prime):
$(36, 9551)$, $(44, 15683)$, $(52, 19609)$, $(72, 31397)$, $(86, 155921)$,
$(96, 360653)$, $(112, 370261)$, $(114, 492113)$, $(118, 1349533)$,
$(132, 1357201)$, $(148, 2010733)$, $(154, 4652353)$, $(180, 17051707)$,
$(210, 20831323)$, $(220, 47326693)$ — agreeing with the published
first-occurrence table at every value S3/P-C use. For scale: the exact
$N(3, 5000) = 20\,263\,871$ (the extremal pair), with
$G(N(3,5000)) = 180 > 3$, so $(3,5000)$ is not S3-cleared.

**Exact evaluation without per-pair binary searches.** Let $B_i$ be the
smallest prime whose following gap exceeds $i$ (read off the record
table; the first gap exceeding $i$ is necessarily a record gap). Then
$i \ge G(N)$ ⟺ $N \le B_i$ ⟺ $C(2j, 2i) \le C(B_i + 1, i)$, a threshold
condition in $j$; $J^{S3pp}(i)$, the largest scope $j$ it clears, was
computed by exact binary search per row. This inversion was **validated
against exact $N(i,j)$** (binary search on `math.comb`, pairpass method)
at **both sides of all 129 frontiers** $3 \le i \le 131$ and on 40 seeded
random pairs: PASS everywhere. Samples: $J^{S3pp}(50) = 627$,
$J^{S3pp}(100) = 3746$, $J^{S3pp}(120) = J^{S3pp}(131) = 5000$; in fact
$J^{S3pp}(i) = 5000$ for all $114 \le i \le 131$, which is what closes
those rows completely.

**Marginal: 168,359 newly cleared** in the headline chain (not "few or
zero"). The mechanism is honest: for $i$ near 131, $N(i,j)$ stays below
$\approx 5.5 \times 10^5$ even at $j = 5000$ (exact:
$N(131, 5000) = 504\,006$), where the maximal gap is only $114 \le 131$;
the uniform Cycle 1 argument stopped at $i \ge 132$ only because it used
one bound for all rows.

## Step (7): parametric $i = 3$ (LD3) frontier

Row 3's frontier after steps (1)–(6) in the headline chain is
$J = 465$ (from step (3)'s crude $J_K(3)$; baseline 158, literal sharp
adds nothing, $J^{S3pp}(3) = \lfloor 9/2 \rfloor$, R1 window $j = 5$
already cleared). Clearing $(3, j)$ for all $j \le F_3$ on top of the
full union gives:

| $F_3$ | Meaning | Extra pairs | Union total | **Partial pairs remaining** |
|---:|---|---:|---:|---:|
| 158 | sweep only (no LD3 gain beyond baseline) | 0 | 3,870,655 | **378,845** |
| 2000 | P-F1's computed frontier | 1,535 | 3,872,190 | **377,310** |
| 5000 | P-F2's claimed frontier (whole row) | 4,535 | 3,875,190 | **374,310** |

(Kept parametric exactly as instructed; no verification of P-F1/P-F2 is
claimed here.)

## Residual map (headline chain): rows $i \le 131$ still partial after steps (1)–(6)

Rows **fully cleared** at $i \le 131$: $i = 1, 2$ and $114 \le i \le 131$
(20 rows). **111 rows remain partial: exactly $3 \le i \le 113$**, each
with surviving range a clean tail $j \in [F_i + 1, 5000]$, where $F_i$ is
the row's final union frontier (all six criteria are row prefixes, and
step (6) adds nothing, so the residual is a single interval per row).
The S20-variant frontier and count are shown alongside for comparison
(its residual rows are the same 111 rows).

| $i$ | Frontier $F_i$ (headline) | Surviving $j$ (headline) | Count (headline) | Frontier (S20) | Count (S20) |
|---:|---:|---|---:|---:|---:|
| 3 | 465 | 466–5000 | 4535 | 788 | 4212 |
| 4 | 180 | 181–5000 | 4820 | 180 | 4820 |
| 5 | 253 | 254–5000 | 4747 | 399 | 4601 |
| 6 | 218 | 219–5000 | 4782 | 218 | 4782 |
| 7 | 235 | 236–5000 | 4765 | 309 | 4691 |
| 8 | 251 | 252–5000 | 4749 | 251 | 4749 |
| 9 | 266 | 267–5000 | 4734 | 267 | 4733 |
| 10 | 280 | 281–5000 | 4720 | 410 | 4590 |
| 11 | 355 | 356–5000 | 4645 | 583 | 4417 |
| 12 | 307 | 308–5000 | 4693 | 354 | 4646 |
| 13 | 319 | 320–5000 | 4681 | 482 | 4518 |
| 14 | 331 | 332–5000 | 4669 | 365 | 4635 |
| 15 | 343 | 344–5000 | 4657 | 476 | 4524 |
| 16 | 354 | 355–5000 | 4646 | 601 | 4399 |
| 17 | 395 | 396–5000 | 4605 | 738 | 4262 |
| 18 | 376 | 377–5000 | 4624 | 555 | 4445 |
| 19 | 386 | 387–5000 | 4614 | 670 | 4330 |
| 20 | 396 | 397–5000 | 4604 | 513 | 4487 |
| 21 | 406 | 407–5000 | 4594 | 610 | 4390 |
| 22 | 416 | 417–5000 | 4584 | 715 | 4285 |
| 23 | 425 | 426–5000 | 4575 | 825 | 4175 |
| 24 | 434 | 435–5000 | 4566 | 640 | 4360 |
| 25 | 444 | 445–5000 | 4556 | 734 | 4266 |
| 26 | 452 | 453–5000 | 4548 | 833 | 4167 |
| 27 | 476 | 477–5000 | 4524 | 937 | 4063 |
| 28 | 530 | 531–5000 | 4470 | 1044 | 3956 |
| 29 | 586 | 587–5000 | 4414 | 1156 | 3844 |
| 30 | 487 | 488–5000 | 4513 | 1018 | 3982 |
| 31 | 526 | 527–5000 | 4474 | 1120 | 3880 |
| 32 | 503 | 504–5000 | 4497 | 991 | 4009 |
| 33 | 511 | 512–5000 | 4489 | 1085 | 3915 |
| 34 | 523 | 524–5000 | 4477 | 1182 | 3818 |
| 35 | 569 | 570–5000 | 4431 | 1281 | 3719 |
| 36 | 616 | 617–5000 | 4384 | 1382 | 3618 |
| 37 | 663 | 664–5000 | 4337 | 1486 | 3514 |
| 38 | 563 | 564–5000 | 4437 | 1318 | 3682 |
| 39 | 605 | 606–5000 | 4395 | 1413 | 3587 |
| 40 | 649 | 650–5000 | 4351 | 1510 | 3490 |
| 41 | 693 | 694–5000 | 4307 | 1607 | 3393 |
| 42 | 597 | 598–5000 | 4403 | 1433 | 3567 |
| 43 | 637 | 638–5000 | 4363 | 1523 | 3477 |
| 44 | 592 | 593–5000 | 4408 | 1364 | 3636 |
| 45 | 599 | 600–5000 | 4401 | 1448 | 3552 |
| 46 | 627 | 628–5000 | 4373 | 1533 | 3467 |
| 47 | 665 | 666–5000 | 4335 | 1618 | 3382 |
| 48 | 619 | 620–5000 | 4381 | 1456 | 3544 |
| 49 | 626 | 627–5000 | 4374 | 1536 | 3464 |
| 50 | 654 | 655–5000 | 4346 | 1616 | 3384 |
| 51 | 689 | 690–5000 | 4311 | 1697 | 3303 |
| 52 | 803 | 804–5000 | 4197 | 1780 | 3220 |
| 53 | 811 | 812–5000 | 4189 | 1863 | 3137 |
| 54 | 818 | 819–5000 | 4182 | 1683 | 3317 |
| 55 | 826 | 827–5000 | 4174 | 1761 | 3239 |
| 56 | 834 | 835–5000 | 4166 | 1838 | 3162 |
| 57 | 841 | 842–5000 | 4159 | 1917 | 3083 |
| 58 | 849 | 850–5000 | 4151 | 1996 | 3004 |
| 59 | 856 | 857–5000 | 4144 | 2075 | 2925 |
| 60 | 864 | 865–5000 | 4136 | 1884 | 3116 |
| 61 | 871 | 872–5000 | 4129 | 1959 | 3041 |
| 62 | 879 | 880–5000 | 4121 | 1784 | 3216 |
| 63 | 886 | 887–5000 | 4114 | 1854 | 3146 |
| 64 | 893 | 894–5000 | 4107 | 1924 | 3076 |
| 65 | 900 | 901–5000 | 4100 | 1994 | 3006 |
| 66 | 907 | 908–5000 | 4093 | 2065 | 2935 |
| 67 | 914 | 915–5000 | 4086 | 2136 | 2864 |
| 68 | 922 | 923–5000 | 4078 | 1954 | 3046 |
| 69 | 928 | 929–5000 | 4072 | 2021 | 2979 |
| 70 | 935 | 936–5000 | 4065 | 2088 | 2912 |
| 71 | 942 | 943–5000 | 4058 | 2155 | 2845 |
| 72 | 2072 | 2073–5000 | 2928 | 2072 | 2928 |
| 73 | 2087 | 2088–5000 | 2913 | 2087 | 2913 |
| 74 | 2101 | 2102–5000 | 2899 | 2101 | 2899 |
| 75 | 2116 | 2117–5000 | 2884 | 2116 | 2884 |
| 76 | 2130 | 2131–5000 | 2870 | 2130 | 2870 |
| 77 | 2144 | 2145–5000 | 2856 | 2144 | 2856 |
| 78 | 2158 | 2159–5000 | 2842 | 2158 | 2842 |
| 79 | 2172 | 2173–5000 | 2828 | 2181 | 2819 |
| 80 | 2186 | 2187–5000 | 2814 | 2186 | 2814 |
| 81 | 2200 | 2201–5000 | 2800 | 2200 | 2800 |
| 82 | 2213 | 2214–5000 | 2787 | 2213 | 2787 |
| 83 | 2227 | 2228–5000 | 2773 | 2227 | 2773 |
| 84 | 2241 | 2242–5000 | 2759 | 2241 | 2759 |
| 85 | 2254 | 2255–5000 | 2746 | 2254 | 2746 |
| 86 | 3427 | 3428–5000 | 1573 | 3427 | 1573 |
| 87 | 3447 | 3448–5000 | 1553 | 3447 | 1553 |
| 88 | 3467 | 3468–5000 | 1533 | 3467 | 1533 |
| 89 | 3487 | 3488–5000 | 1513 | 3487 | 1513 |
| 90 | 3506 | 3507–5000 | 1494 | 3506 | 1494 |
| 91 | 3526 | 3527–5000 | 1474 | 3526 | 1474 |
| 92 | 3545 | 3546–5000 | 1455 | 3545 | 1455 |
| 93 | 3565 | 3566–5000 | 1435 | 3565 | 1435 |
| 94 | 3584 | 3585–5000 | 1416 | 3584 | 1416 |
| 95 | 3603 | 3604–5000 | 1397 | 3603 | 1397 |
| 96 | 3670 | 3671–5000 | 1330 | 3670 | 1330 |
| 97 | 3689 | 3690–5000 | 1311 | 3689 | 1311 |
| 98 | 3708 | 3709–5000 | 1292 | 3708 | 1292 |
| 99 | 3727 | 3728–5000 | 1273 | 3727 | 1273 |
| 100 | 3746 | 3747–5000 | 1254 | 3746 | 1254 |
| 101 | 3765 | 3766–5000 | 1235 | 3765 | 1235 |
| 102 | 3784 | 3785–5000 | 1216 | 3784 | 1216 |
| 103 | 3803 | 3804–5000 | 1197 | 3803 | 1197 |
| 104 | 3821 | 3822–5000 | 1179 | 3821 | 1179 |
| 105 | 3840 | 3841–5000 | 1160 | 3840 | 1160 |
| 106 | 3858 | 3859–5000 | 1142 | 3858 | 1142 |
| 107 | 3876 | 3877–5000 | 1124 | 3876 | 1124 |
| 108 | 3895 | 3896–5000 | 1105 | 3895 | 1105 |
| 109 | 3913 | 3914–5000 | 1087 | 3913 | 1087 |
| 110 | 3931 | 3932–5000 | 1069 | 3931 | 1069 |
| 111 | 3949 | 3950–5000 | 1051 | 3949 | 1051 |
| 112 | 4565 | 4566–5000 | 435 | 4565 | 435 |
| 113 | 4586 | 4587–5000 | 414 | 4586 | 414 |

Total residual (headline): **378,845** pairs. Total residual under the
S20 variant of step (4): **334,406** pairs (same rows, higher frontiers).

## Supplementary: full chains under the sweep-relative readings of step (4)

If step (4) is read sweep-relatively, steps (5)–(7) recomputed after it
give (steps (1)–(3) and (6) as in the headline table; (6) is 0 in all
chains):

| Step (4) form | (4) newly | Running after (4) | (5) newly | **Union (1)–(6)** | **Remaining** | Row-3 frontier | Remaining at $F_3 = 2000$ / $5000$ |
|---|---:|---:|---:|---:|---:|---:|---:|
| S10 (cap 10,000) | 41,374 | 3,743,670 | 142,194 | 3,885,864 | **363,636** | 497 | 362,133 / 359,133 |
| S20 (cap 20,000) | 123,949 | 3,826,245 | 88,849 | 3,915,094 | **334,406** | 788 | 333,194 / 330,194 |

Corresponding union totals at $F_3 = 158$ equal the "Union (1)–(6)"
column (row 3 is already past 158 in both chains). All frontiers for all
three chains, the $B_i$ table, $J^{S3pp}$, the record-gap table, and the
per-row residuals are in `verification/counts_c2.json`.
