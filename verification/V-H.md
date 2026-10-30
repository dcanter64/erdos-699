# V-H — Independent Verification of Cluster H (S10 R1 Counting Bound), Cycle 2

**Verifier:** V-H (independent; P-H1 and P-H2 read in full, S10 §3–§7,
EXTERNAL_CLAIMS_2026-10-29 Del Pin entry, Phase 0 / REFEREE ground truth).
**Scripts:** `verification/V-H_checks.py` (all small checks, exact),
`verification/V-H_scan.py` (exact primorial scan),
`verification/V-H_scan_fast.py` (incremental exact scan used for the
$i \le 2000$ extension; binomials updated by gcd-reduced small-factor
steps and asserted against `math.comb` every 997th pair and at the end
of every $i$-row). Python stdlib only,
exact integer arithmetic throughout; every number below was recomputed
by the verifier unless explicitly described as a cited estimate.
**Date:** 2026-10-29.

---

## 0. Bottom line (adjudicated)

**R1 IS CERTIFIED CLOSED** — in exactly the sense of option (a) of the
verification brief:

> There is no counterexample to #699 with $3i/2 < j < 2i$, for any $i$,
> modulo: EEES78 (with its 12 exception pairs discharged — for R1 this
> discharge is exactly the 9 triples listed in §1.3, all verified
> directly below), S10's R1 characterisation, the key lemma, the two
> cited explicit $\theta$ estimates (D1), (D2) of §3, and — for the two
> pairs $(4,7)$ and $(10,19)$ only — the finite reduction plus the
> completed sweep to $n \le 20{,}000$.

**The seam is explicit and gapless:** the exact integer scan covers
$i \le 1000$ (249,500 R1 pairs, failures exactly $(4,7)$, $(10,19)$);
H1's analytic argument (its Claim 9) covers every $i > 1000$ with a
proved margin of $0.03726$ in $\log$ per unit $i$, using estimates
whose validity ranges ($x \ge 2$ for (D1), $x > 0$ for (D2)) start far
below the seam. There is **no unscanned band** and **no ineffective
constant** in the combined argument.

**On the dispute:** H1's headline (its Claim 11, "R1 is closed") is
**upheld**. H2's refusal to claim closure rests on its own Claim 9,
which is genuinely ineffective (PNT $o(i)$ with no rate) — H2 labels
that GAP itself, correctly. H2's GAP is real *as a property of H2's
argument*; it is **repaired by H1's Claim 9**, which supplies exactly
the effective $\theta(j)-\theta(i)$ estimate H2's Claim 15 says is
needed. The two files are otherwise in complete agreement on every
number the verifier recomputed.

---

## 1. The core lever (brief item 1)

### 1.1 The lever is sound

Re-derived from S10's verified results, independently of both provers:

- Counterexample in R1 $\Rightarrow S(n,i) \subseteq [i,j]$ (S10,
  Theorem S10 item 1: every $p > j$ in $S(n,i)$ is good by Lemma 2, so a
  counterexample, in which every member of $S(n,i)$ is bad, has none).
- $e_p = 1$ for every $p \in S(n,i)$ (S10 §5 R1 characterisation; upper
  band only, since the lower band $[i, j/2]$ is empty in R1).
- $p = i$ is never bad (S10 Theorem 3(b): $B_i = 0$, $\Delta_i \le 0 <
  e_i$), and $i \notin S(n,i)$ for composite $i$ trivially; hence every
  prime factor of $V_i(n)$ lies in the **open** interval $(i, j]$.
- Hence $V_i(n) = \prod_{p \in S(n,i)} p$ is squarefree, and since its
  distinct prime factors all lie in $(i,j]$,
  $V_i(n) \mid P(i,j) := \prod_{i<p\le j} p$. (Both files also route
  through the key lemma, $V_i(n) \mid C(j,i)$; the divisibility by
  $P(i,j)$ needs only squarefreeness plus support, and is additionally
  consistent with $v_p(C(j,i)) = 1$ for all $i<p\le j$ — verified as a
  proof in §5 under Claim 2/Claim 14.)
- EEES78, for $(n,i)$ not an exception pair: $V_i(n) > C(n,i)^{1/2} \ge
  C(2j,i)^{1/2}$ ($n \ge 2j$, $C(\cdot,i)$ increasing). So
  $P(i,j)^2 \le C(2j,i)$ excludes a counterexample at $(i,j)$. The
  endpoint logic is correct in both files: the EEES inequality is
  strict, so $\le$ in the criterion suffices.

No step in either file's lever chain was found to be wrong, reversed,
or silently strengthened.

### 1.2 $N(4,7)$ and $N(10,19)$, and the sweep

Recomputed exactly from the reduction's definition
($N(i,j) = \max\{n : C(n,i) < C(2j, 2(j-i))\}$):

- $N(4,7) = 17$, $N(10,19) = 55$ — both as claimed. (Also
  $N(39,59) = 119$, $N(39,61) = 130$, $N(59,113) = 337$, all matching.)
- `pairpass_20000.json` (in `~/workspace/math-hunt/erdos-699/`) lists
  $j=7$ in `cleared_js_by_i['4']` and $j=19$ in
  `cleared_js_by_i['10']`: both pairs are **fully cleared** (their
  whole intervals $[2j, N(i,j)]$ lie below the sweep cap). The cap-20000
  sweep log records completion: 222,188,892,222 triples checked in the
  open region, 0 flagged, no confirmed counterexamples. So both
  exceptional pairs fall to the finite reduction plus the sweep,
  exactly as H1 Claim 10 states. H1 Claim 10's exception sub-argument
  is also correct: the only EEES exception with $i=4$ is $(9,4)$, with
  $n = 9 < 14 = 2j$, so for every admissible $n \ge 14$ the pair
  $(n,4)$ is a non-exception and the reduction applies; there is no
  EEES exception with $i=10$ at all.

### 1.3 EEES78 exception handling — the one place care was needed

The lever uses $V_i(n) > C(n,i)^{1/2}$, which **fails** at the 12
exception pairs $(n,i)$: $(8,3)$, $(9,4)$, $(10,5)$, $(12,5)$, $(21,7)$,
$(21,8)$, $(30,7)$, $(33,13)$, $(33,14)$, $(36,13)$, $(36,17)$,
$(56,13)$ (Phase 0 Item 4, list verified there three ways). A file
that assumed EEES78 at an exception pair *inside R1* would have a real
gap. The verifier therefore enumerated exactly which exception pairs
can occur in R1 at all: an exception pair $(n_0,i_0)$ admits an R1 $j$
($3i_0/2 < j < 2i_0$, $j \le n_0/2$) only for

- $(30,7)$ with $j \in \{11, 12, 13\}$, and
- $(56,13)$ with $j \in \{20, 21, 22, 23, 24, 25\}$

— **9 triples**, and no others (the other ten exception pairs admit
no R1 $j$). For each of the 9 the verifier computed
$\gcd(V_{i_0}(n_0), C(n_0,j))$ directly by Legendre exponents:
$377, 377, 29$ for $(30,7)$ at $j = 11,12,13$, and
$57293, 57293, 57293, 42347, 42347, 42347$ for $(56,13)$ at
$j = 20,\dots,25$ — all $> 1$, so none is a counterexample. (For
completeness: all 41 exception-pair triples over all $j$ were likewise
recomputed; every gcd $> 1$, matching the Phase 0 discharge.)

**Disposition.** Neither file is *silently* assuming EEES78 at an
exception pair: both state the non-exception hypothesis in every lever
claim, and both invoke the established discharge for the exceptions
(H1 Claim 11 parenthetically; H2 in Claim 15's "Not claimed"). The
discharge they invoke is real — it is precisely the 9 triples above,
inside the $n \le 240$ Phase 0 brute force and the $n \le 20{,}000$
sweep. This is a *presentational* thinness in H1 (it does not
enumerate the 9 triples), not a logical gap: the repair the brief
asks for, had it been needed, is exactly "discharge the 9 listed
triples directly," and that discharge is on record and re-verified
here. No claim is marked GAP on this ground.

---

## 2. Independent recount of the exact scan (brief item 2)

Verifier's own code (`V-H_scan.py`: sieve primes to $2i_{\max}$;
$P(i,j)$ built as an exact integer product, incremented prime by
prime in $j$; exact integer comparison $P(i,j)^2$ vs $C(2j,i)$ via
`math.comb`).

- **All R1 pairs with $i \le 1000$: total = 249,500** (confirming both
  files' count), **failures exactly $\{(4,7), (10,19)\}$**, with
  $P(4,7) = 35$, $35^2 = 1225 > 1001 = C(14,4)$, and
  $P(10,19) = 46189$, $46189^2 = 2{,}133{,}423{,}721 >
  472{,}733{,}756 = C(38,10)$ — every digit as claimed.
- Smallest positive margin on $i \le 1000$: $0.2794$ nats at
  $(57,113)$ (ratio $P^2/C = 0.5719$), confirming H1's "next-worst
  ratio $0.572$ at $(57,113)$" and H2's float-scan margin $+0.279$
  there. The failures' margins are $-0.1010$ nats at $(4,7)$ and
  $-0.7535$ nats at $(10,19)$, matching H2's $-0.101$ / $-0.753$; the
  next positive margin after $(57,113)$ is $+0.7142$ at $(12,23)$,
  matching H2's $+0.714$.
- **Spot-extension to $i \le 2000$:** for **every** $i \in [1001,2000]$,
  the 3 smallest and 3 largest R1 values of $j$ (i.e. $j$ within 3 of
  $\lfloor 3i/2\rfloor$ from above and within 3 of $2i$ from below),
  plus a seeded random sample of 3,000 further pairs (seed 20261029):
  9,000 pairs tested exactly, **0 failures** (smallest positive margin
  in the spot set: $130.21$ nats at $(1006,2011)$).
- **Full extension to $i \le 2000$:** a second, independent exact
  scan over $i \in [1001, 2000]$ (`V-H_scan_fast.py`, with the
  periodic `math.comb` assertions described in the header) found
  **749,500 pairs, 0 failures**. Combined with the $i \le 1000$ run:
  **999,000 R1 pairs with $i \le 2000$, failures exactly
  $\{(4,7), (10,19)\}$, criterion holding at 998,998** — H2 Claim 8's
  totals to the pair. The same runs count the pairs where Del Pin's
  unsharpened condition fails but the sharpened criterion closes:
  247,623 for $i \le 1000$ plus 747,000 for $1001 \le i \le 2000$,
  total **994,623** — exactly H2 Claim 8's figure.

The failure set on the covered range is exactly $\{(4,7),(10,19)\}$,
confirming H1 Claim 8 and H2 Claim 8 in full.

---

## 3. The asymptotic step — adjudication of H1 Claim 9 (brief item 3)

### 3.1 The chain, reproduced step by step

H1 Claim 9 must show, for all $i > 1000$ and $3i/2 < j < 2i$:
$\log P(i,j) < \tfrac12 \log C(2j,i)$, where
$\log P(i,j) = \theta(j) - \theta(i)$. Write $c = j/i \in (3/2, 2)$.

1. **Upper side.** (D1) at $x = i > 1000$:
   $\theta(i) > i\big(1 - 3.965/\log^2 i\big) \ge i(1 - 0.0831)$,
   since $3.965/\log^2 1000 = 0.083094$ (verifier-recomputed) and
   $\log^2 i$ increases. (D2) at $x = j$: $\theta(j) < 1.000081\,j$.
   Hence $\log P(i,j) < \big(1.000081\,c - 0.9169\big) i$. The rounding
   $0.91691 \to 0.9169$ is in the safe direction. ✔
2. **Lower side (entropy bound, elementary).**
   $\log C(2j,i) \ge 2j\,h(t) - \log(2j+1)$ with $t = i/(2j)$,
   $h(t) = -t\log t - (1-t)\log(1-t)$: the binomial term
   $C(2j,i) t^i (1-t)^{2j-i}$ is the mode of
   $\mathrm{Bin}(2j, t)$ (mode $= \lfloor (2j+1)t \rfloor =
   \lfloor i + t \rfloor = i$), is therefore $\ge 1/(2j+1)$ since
   $2j+1$ terms sum to 1, and equals $C(2j,i)\,2^{-2j H_2(t)}$ with
   $2j\,h(t)$ the natural-log form. Hence
   $\tfrac12 \log C(2j,i) \ge c\,h(1/(2c))\,i - \tfrac12\log(2j+1)$. ✔
3. **Worst corner.** $\Psi(c) := c\,h(1/(2c)) - 1.000081\,c + 0.9169$.
   $\frac{d}{dc}\big[c\,h(1/(2c))\big] = -\log(1-u)$, $u = 1/(2c)$
   (verifier re-differentiated: with $h'(u) = \log\frac{1-u}{u}$ and
   $du/dc = -u/c$, $h(u) - u h'(u) = -\log(1-u)$). On $c \in [3/2,2]$,
   $-\log(1-u) \le -\log(2/3) = 0.405465$, so
   $\Psi'(c) \le 0.4055 - 1.000081 < 0$: $\Psi$ is decreasing, worst
   corner $c = 2$ (i.e. $j \to 2i$, as both files' numerics suggested).
   $\Psi(2) = 2h(1/4) - 2.000162 + 0.9169 = 1.124670 - 2.000162 +
   0.9169 = 0.041408$ (verifier: $h(1/4) = 0.5623351446$,
   $\Psi(2) = 0.0414083$; H1 prints $0.04141$). ✔
4. **Error term.** $\tfrac12\log(2j+1)/i \le \tfrac12\log(4005)/1001 =
   0.004144$ for $i > 1000$ (H1 prints $< 0.00415$). H1 does not spell
   out why the $i = 1001$ value bounds all larger $i$; the verifier
   fills it in one line: $j < 2i$ gives $2j+1 \le 4i-1$, and
   $\phi(i) = \frac{\log(4i+1)}{2i}$ is decreasing for $i \ge 1000$
   because $\phi'(i) < 0 \iff \frac{4i}{4i+1} < \log(4i+1)$, and the
   right side is $\ge \log 4001 = 8.294$ while the left side is $< 1$.
   A filled presentational step, not a gap. ✔
5. **Net margin:** $0.041408 - 0.004144 = 0.037265$ per unit $i$
   (H1 prints $0.03726$). Hence $\log P(i,j) < \frac12 \log C(2j,i)$
   strictly, i.e. $(\ast\ast)$ holds, for **every** R1 pair with
   $i > 1000$, with all error terms explicit. ✔

### 3.2 The cited $\theta$ estimates — constants, ranges, directions

- **(D1)** $|\theta(x) - x| < 3.965\,x/\log^2 x$. This is the
  $k = 2$, $M_k = 3.965$ entry of Dusart's explicit-estimates theorem
  (Dusart, *Explicit estimates of some functions over primes*,
  Ramanujan J. 45 (2018), Theorem 4.2), tabulated with starting point
  $X_0 = 2$ in Broadbent–Kadiri–Lumley–Ng–Wilk, *Sharper bounds for
  the Chebyshev function $\theta(x)$* (arXiv:2002.11068), Corollary
  11.2 — whose authors explicitly supply valid proofs of that theorem
  of Dusart. Constant ✔, validity $x \ge 2$ ✔ (H1's "for all $x > 1$"
  is a harmless overstatement of the range; the bound is *used* only
  at $x = i > 1000$, and for $1 < x < 2$ it also holds trivially since
  $\theta(x) = 0$ and $3.965/\log^2 x > 1$ there). Direction of use ✔:
  only the **lower** bound on $\theta(i)$ is used, which is the side
  (D1) provides.
- **(D2)** $\theta(x) < 1.000081\,x$ for all $x > 0$. This is
  Schoenfeld's bound, quoted verbatim with exactly this constant and
  range in the secondary literature (e.g. Bennett et al.: "From
  Schoenfeld [19], we have $\theta(x) = \sum_{p\le x}\log p <
  1.000081x\ (x > 0)$"). Constant ✔, range ✔, direction ✔ (upper
  bound on $\theta(j)$).
- **Robustness note.** The margin does not hinge on the last digits
  of (D2): replacing (D2) by the weaker classical Rosser–Schoenfeld
  bound $\theta(x) \le 1.001102\,x$ still gives
  $\Psi(2) = 1.124670 - 2.002204 + 0.9169 = 0.039366$, net margin
  $0.03522 > 0$. The chain has an order of magnitude of slack in the
  cited constants.

### 3.3 Independent numerical sanity check at large $i$

Exact $\theta$ differences (sum of $\log p$ over $i < p \le j$ by
sieve to $2\times10^5$, accumulated with `math.fsum`) against
$\log C(2j,i)$ computed as the exact log-sum
$\sum_{k=1}^{i} \log\frac{2j-i+k}{k}$ (also `fsum`), cross-checked
against `lgamma` (agreement $\le 6.4\times10^{-10}$ absolute on values
of size $\sim 10^5$; `fsum` rounding error is $\lesssim i \cdot
2^{-53} \cdot \log(\cdot) \ll 10^{-9}$ per unit-$i$ after division —
five orders of magnitude below the margins):

| $i$ | $\gamma = j/i$ | $\big(\tfrac12\log C(2j,i) - \log P(i,j)\big)/i$ |
|---|---|---|
| 10,000 | 1.51 | 0.45501 |
| 10,000 | 1.75 | 0.29977 |
| 10,000 | 1.99 | 0.14247 |
| 100,000 | 1.51 | 0.44947 |
| 100,000 | 1.75 | 0.29967 |
| 100,000 | 1.99 | 0.13281 |

All comfortably positive, decreasing toward the $c \to 2$ limiting
value $f(2) = 2h(1/4) - 1 = 0.124670$ of H2's Claim 9 analysis as
$\gamma \to 2$ — exactly the behaviour both files predict. The
inequality is not close at any tested point.

### 3.4 Decision

Case **(a)** of the brief applies. The chain is sound, every error
term is explicit, the effective threshold is $i_0 = 1000$, and the
cited estimates are valid far below it. **H1 Claim 9 is PROVED
(modulo (D1), (D2) as cited published estimates), and H1 Claim 11's
headline is CERTIFIED** in the form stated in §0. H2 Claim 9 is
PROVED as an ineffective existence statement with its effectivity
GAP correctly self-labelled; that GAP does not propagate to the
combined record, because H1 Claim 9 closes it.

---

## 4. Combined-cap recount (brief item 4)

Verifier's independent replication (Legendre exponents throughout;
R1 pairs $i < 40$; $n \in [2j, N(i,j)]$; a triple counted when
$|S(n,i) \cap [i,j]| \ge 3$ and every such prime is window-bad,
$\Delta_p \ge e_p$):

- Pairs: 361 R1 pairs with $i < 40$; scanned triples: **10,317**.
- Window-badness alone: **377 triples**, distribution by simultaneous
  bad count $\{3: 195,\ 4: 166,\ 5: 16\}$, maximum **5**, over 116
  distinct $(i,j)$ pairs. First examples $(60,11,21)$, $(61,11,21)$,
  $(61,12,22)$ — all matching both files and S10.
- With the key-lemma cap $e_p \le v_p(C(j, j-i))$ imposed additionally:
  **377 triples, maximum 5, killed = 0.** Both files' numbers are
  confirmed exactly.

**H1 Claim 14 (and identically H2 Claim 14) as a proof: PROVED.**
For $p > i$ in R1: $v_p(C(j,d)) = B_p - v_p(d!)$ with $B_p = 1$
(S10 Theorem 3(a)) and $v_p(d!) = 0$ (since $p > i > d$), so the cap
is $e_p \le 1$; window-badness forces $e_p = 1$ (S10 Theorem 3(b)),
so the cap holds with equality — it cannot bite. For $p = i$ prime,
window-badness is already impossible ($\Delta_i \le 0 < e_i$). Hence
the combined condition is *identical* to window-badness throughout
R1, for structural reasons; the empirical 0-killed is a theorem.
(Note the cap genuinely can bite outside R1, as both files say; that
is outside this cluster.)

---

## 5. H1's numerics and the remaining counts (brief item 5)

All recomputed exactly; all match.

- $\prod_{p\ \mathrm{bad}} p$ at $(119,39,59)$: $41\cdot43\cdot47
  \cdot53\cdot59 = 259{,}106{,}347$ ✔. $C(59,39) =
  2{,}794{,}563{,}003{,}870{,}330$ ✔, divisible by that product with
  quotient exactly $10{,}785{,}390$ ✔.
- $J_1(39) = 59$ ✔ (exact: $(\ast)$ holds at $j=59$, fails at every
  $j = 60,\dots,77$). Also re-verified exactly: $J_1(3) = 5$,
  $J_1(5) = 8$, $J_1(640) = 962$, $J_1(5000) = 7503$, matching the
  Del Pin values recorded in EXTERNAL_CLAIMS.
- Claim 6 crude counts: over the 361 R1 pairs with $i < 40$, the
  crude cardinality bounds are incompatible for exactly **14** pairs,
  and the verifier's list is identical to H1's:
  $(5,8), (6,10), (7,11), (9,15), (10,16), (11,17), (14,22),
  (15,23), (19,29), (24,37), (25,38), (29,44), (34,52), (35,53)$.
  At $(39,59)$: $8.8685 < b \le 9.7082$ (H1: $8.868 < b \le 9.708$);
  at $(39,60)$: $8.9285 < b \le 9.9947$ (H1: $8.929 < b \le 9.995$) —
  both force $b = 9$, as claimed. The sharpened condition closes
  **359 of 361** at $i < 40$ ✔, and the unsharpened $(\ast)$ closes
  **34 of 361** ✔ (H1 Claim 8's comparison figure).
- Further exact spot values, all confirmed: $C(60,39) =
  7{,}984{,}465{,}725{,}343{,}800$; $C(120,39) =
  56{,}571{,}283{,}083{,}933{,}415{,}181{,}782{,}620{,}687{,}640$;
  $C(120,39)/C(60,39)^2 = 0.8873691112\ldots$;
  $C(60,39) - \lfloor C(120,39)^{1/2}\rfloor =
  463{,}077{,}350{,}586{,}557$; $C(118,39)$, $C(119,39)$, $C(238,39)$
  and their integer square roots as printed in H1 Claim 5;
  $V_{39}(119) = 2{,}545{,}453{,}702{,}497{,}494{,}433{,}235{,}781$
  with $V^2 > C(119,39)$; $Q(39,61) = 15{,}805{,}487{,}167$ and its
  square vs $C(122,39)$ (H2 Claim 6); the bad-prime set
  $\{43,47,53,59,61\}$ at $(122,39,61)$; CRT counts
  $\prod(p-20) = 16{,}783{,}767$ and density $0.0647755919\ldots$
  (H1 Claim 12 / H2 Claim 12); both $n = 118$ and $n = 119$ satisfy
  all five badness conditions at $(39,59)$ with $e_p = 1$.
- H2 Claim 10's counting-sandwich table: all five rows recomputed —
  lower bounds $8.8685$, $8.9868$, $13.4274$, $1.7752$, $3.3918$;
  $\pi(j)-\pi(i)$ values $5, 6, 13, 2, 4$; $\log Q/\log i$ values
  $5.2880$, $6.4101$, $14.2394$, $2.5646$, $4.6645$ — every entry
  matches to the printed precision, and the verdicts (in particular
  $B=2$, $V=35$ forced at $(4,7)$ and $B=4$, $V=46189$ forced at
  $(10,19)$) follow.
- H2 Claim 11's barrier integers: $35 \mid C(7,4) = 35$ (quotient 1);
  $46189 \mid C(19,10) = 92378$ (quotient 2); both squares exceed
  $C(2j,i)$ as claimed. The barrier is genuinely sharp for
  size/divisibility data alone. ✔
- One rounding nit (H2 Claim 5(b) only): the exact ratio
  $C(118,39)/P^2 = 382{,}372{,}565{,}116{,}467.98\ldots$; H2 prints
  $382{,}372{,}565{,}116{,}468$, i.e. the nearest integer, in a line
  that also carries "$\approx 3.8\times10^{14}$". Immaterial; no
  claim depends on it. H1's corresponding approximations
  ($1.955\times10^7$, $2.385\times10^7$, $1.146\times10^{14}$ for the
  square-root ratios) are all correct to the precision printed
  (exact floor ratios: $19{,}554{,}349$, $23{,}849{,}092$,
  $1.1460\times10^{14}$).

---

## 6. Claim-by-claim tables

### P-H1 (17 claims)

| # | Verdict | Basis |
|---|---|---|
| 1 | **PROVED** | Chain re-derived in §1.1; endpoint ($\ge$ in $(\ast)$) logic correct. Hypothesises non-exception $(n,i)$, as stated. |
| 2 | **PROVED** | Legendre computation rechecked: $v_p(C(j,i)) = 1$ for $i<p\le j$ ($p > j/2$ kills $k\ge2$ terms; floors $1-0-0$), $v_i = 0$; $p=i$ weakening shown vacuous via S10 Thm 3(b). |
| 3 | **PROVED** | Pairwise iff for the Claim-1 size data is correct ($V_0 = C(j,i)$ is a model when $(\ast)$ fails); initial-segment structure from Del Pin's verified monotonicity; $J_1$ values incl. $J_1(39)=59$ recomputed exactly (§5). |
| 4 | **PROVED** | All integers at $(39,60)$ recomputed exactly (§5); barrier conclusion for the unsharpened lever follows. |
| 5 | **PROVED** | Every printed integer, quotient, isqrt and difference recomputed (§5); slack discussion is a correct reading of those numbers. |
| 6 | **PROVED** | Independent recount: 14 of 361, list identical; $b=9$ forced at $(39,59)$ and $(39,60)$ (§5). |
| 7 | **PROVED** | §1.1: squarefree $+$ support in $(i,j]$ gives $V \mid P(i,j)$; criterion $(\ast\ast)$ follows from Claim 1. |
| 8 | **PROVED** | Verifier's full exact recount, $i \le 1000$: 249,500 pairs, failures exactly $(4,7)$, $(10,19)$ (§2). |
| 9 | **PROVED** (modulo cited (D1), (D2)) | Full chain audited line by line (§3.1); cited constants/ranges verified against the literature (§3.2); one presentational step (monotonicity of the error-term bound) filled by the verifier. Effective threshold $i_0 = 1000$. |
| 10 | **PROVED** | $N(4,7)=17$, $N(10,19)=55$ recomputed; both pairs fully cleared in `pairpass_20000.json`; sweep complete, 0 flagged; exception sub-argument correct (§1.2). |
| 11 | **PROVED modulo the named inputs — CERTIFIED** | Claims 7–10 combine with no seam ($i\le1000$ exact, $i>1000$ analytic); EEES exceptions in R1 are exactly the 9 triples of §1.3, discharged on record and re-verified. Headline upheld (§0). |
| 12 | **PROVED** | CRT count and density exact (§5); limitation conclusion is rigorous: density arguments cannot return "0 solutions" for $[118,119]$, which in fact contains 2 solutions (both recomputed). |
| 13 | **PROVED** | Independent recount identical: 377 / max 5 / 0 killed, distribution $\{3{:}195, 4{:}166, 5{:}16\}$, 10,317 scanned (§4). |
| 14 | **PROVED** | Proof checked (§4): cap $= B_p - v_p(d!) = 1 - 0 = 1$ for $p>i$, met with equality by window-badness; $p=i$ case vacuous. |
| 15 | **PROVED** | Summary chain assembled from Claims 1, 2, 7, each proved; $P(i,j) \mid C(j,i)$ follows from Claim 2 (distinct primes, each to the first power). |
| 16 | **PROVED** | Boundary statements are Claims 4, 6, 8, 9 restated; margin $0.037$ per unit $i$ is §3.1's figure ("grows with $i$" is correct for the total log-margin $0.037\,i$; the proved per-unit margin at the frozen constants is the constant $0.03726$). |
| 17 | **OPEN** | Correctly self-labelled: R2, R3 lower band, and any EEES-free version are untouched by anything in the file; the verifier found no hidden closure of them. |

No claim in P-H1 is FALSE, and none is left as a GAP: the two
candidate weak points (the $\theta$ citations in Claim 9; the
exception-pair disposal behind Claim 11) were both checked to the
primary/secondary literature and to direct computation respectively,
and both hold.

### P-H2 (15 claims)

| # | Verdict | Basis |
|---|---|---|
| 1 | **PROVED** | Same lever facts as §1.1; $i \notin S(n,i)$ handled for prime and composite $i$; key-lemma application correct. |
| 2 | **PROVED** | $B_p = 1$, $v_p(d!) = 0$, hence $v_p(C(j,i)) = 1$ on $(i,j]$; endpoint check $v_i = 0$ consistent. The two caps coincide — correct. |
| 3 | **PROVED** | Squarefree $+$ support $\Rightarrow V \mid Q(i,j)$; wasted factor identified correctly. |
| 4 | **PROVED** | Iff for the unsharpened chain correct in both directions; $J_1$ values match verifier's exact computations. |
| 5 | **PROVED** | All integers recomputed (§5), including the correction that $(39,59)$ lies *inside* Del Pin's range ($J_1(39) = 59$; holding set $40..59$ confirmed, failure at 60 plus verified monotonicity of $F$ covers $j > 60$). One immaterial rounding nit (§5, last bullet). |
| 6 | **PROVED** | $(39,60)$ barrier ratio recomputed; $Q(39,60)$, $Q(39,61)$ and both squared comparisons recomputed; $(122,39,61)$ bad set and $N(39,61)=130$ re-verified. |
| 7 | **PROVED** | Criterion chain $C(2j,i) \le C(n,i) < V^2 \le Q^2 \le C(2j,i)$ correct under the stated non-exception hypothesis. |
| 8 | **PROVED** | Verifier's exact recount in full: $i \le 1000$ by direct `math.comb` scan and $i \le 2000$ by the asserted incremental scan (§2) — 999,000 pairs, failures exactly $(4,7)$, $(10,19)$, 998,998 holding, and the Del Pin-fails/sharpened-closes count 994,623 reproduced exactly; float-margin values ($-0.753$, $-0.101$, $+0.279$, $+0.714$) all match (§2, §5). |
| 9 | **PROVED as stated (ineffective); GAP: effectivity** | The PNT $+$ Stirling argument is sound: uniformity in $t \in [3/2,2]$ is legitimate ($\theta(j)-\theta(i) = (j-i) + o(i)$ uniformly since $j \le 2i$; entropy limit uniform since $1/(2t)$ stays in $[1/4,1/3]$); $f'(t) = \log\frac{2t}{2t-1} - 1 < 0$ re-differentiated; $f(2) = 0.124670$ recomputed. The $o(i)$ carries no rate, so $I_0$ is ineffective — exactly the GAP the file itself declares. Repaired in the combined record by H1 Claim 9 (§3.4). |
| 10 | **PROVED** | Sandwich proof correct ($V \le j^B$; $B \le \pi(j)-\pi(i)$; $B \le \log Q/\log i$); all five table rows recomputed exactly (§5). |
| 11 | **PROVED** | Both barrier integers verified exactly (§5): they satisfy squarefreeness, support, $V \mid C(j,i)$, $V = Q(i,j)$ and $V^2 > C(2j,i)$ simultaneously, so no size-only argument can exclude those two pairs. |
| 12 | **PROVED** | Density $0.0647755919\ldots$ and period $259{,}106{,}347$ exact; the can/cannot statements are correct — in particular $n=119$ *is* a hit (recomputed), so no density argument can exclude the interval $[118,119]$. |
| 13 | **PROVED** | Independent recount identical: window 377 (max 5), combined 377 (max 5), killed 0; 361 pairs, 10,317 triples; first examples match (§4). |
| 14 | **PROVED** | Same structural argument as H1 Claim 14, checked in §4; the $p=i$ sub-case (cap $0$, window-badness impossible, $e_i \ge 1$ violates both) is handled correctly. |
| 15 | **PROVED as a statement of what P-H2 itself establishes; its declared GAP is real for P-H2 alone and is closed in the combined record** | The strongest bound and the $J_1$ / $Q^2 = C(2j,i)$ boundaries are Claims 4, 7, 11 (proved). The "GAP between $i \le 2000$ and $I_0$" is an accurate self-assessment of H2's ineffective Claim 9 — and is precisely what H1 Claim 9 repairs (§3). "$(4,7)$ and $(10,19)$ OPEN within this method" is correct qua size-method statement (Claim 11); with the reduction $+$ sweep those pairs are closed (H1 Claim 10), as H2's own Claim 11 parenthetical notes. H2's refusal to claim R1 closed is therefore *conservative, not correct as a verdict on the combined record*. |

No claim in P-H2 is FALSE. The only GAP in either file is the
effectivity GAP H2 declares in its own Claim 9 / Claim 15, and it
does not survive combination with P-H1.

---

## 7. Adjudicated bottom line

1. **The sharpened lever is real and correctly proved in both files:**
   an R1 counterexample forces $V_i(n) \mid P(i,j)$, hence is excluded
   whenever $P(i,j)^2 \le C(2j,i)$ (non-exception $(n,i)$).
2. **The exact failure set of that criterion is $\{(4,7), (10,19)\}$**
   on every range the verifier covered exhaustively: $i \le 1000$
   (249,500 pairs) by the direct scan, and $i \le 2000$ in full
   (999,000 pairs) by the asserted incremental scan, with a
   boundary-plus-random spot check (9,000 pairs, 0 failures) in
   agreement. Both
   exceptional pairs are closed by the finite reduction
   ($N = 17$, $55$) plus the completed sweep, confirmed in
   `pairpass_20000.json`.
3. **The asymptotic step is effective, not merely asymptotic.**
   H1 Claim 9's chain is sound step by step; its worst corner is
   $j \to 2i$; its proved margin is $0.03726$ in $\log$ per unit $i$;
   its cited estimates (Dusart's $3.965/\log^2 x$ bound, valid for
   $x \ge 2$; Schoenfeld's $\theta(x) < 1.000081x$, valid for
   $x > 0$) are correctly quoted and used in the correct directions,
   and the conclusion survives even the weaker classical
   $1.001102$ upper bound. Effective seam: **scan to $i = 1000$,
   analysis from $i = 1001$ — no gap.**
4. **EEES78 exceptions do not disturb the closure:** in R1 they
   amount to exactly 9 triples, all discharged by direct gcd
   computation (re-verified), as the established ground truth records.
5. **The combined cap adds nothing in R1** (377 triples, max 5,
   0 killed — a theorem, per Claims 14 of both files, not an
   accident of the range).

**Therefore: R1 is certified closed, modulo EEES78 with its
exception pairs discharged, S10's R1 characterisation, the key
lemma, the cited estimates (D1) and (D2), and the finite
reduction plus sweep for $(4,7)$ and $(10,19)$.** This certifies
Cluster H's contribution only: it does not close R2, R3, or #699
as a whole, and nothing in either file claims otherwise (H1
Claim 17 / H2 Claim 15 are correct on that scope).

*End of V-H.*
