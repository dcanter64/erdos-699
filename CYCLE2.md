# Erdős #699 Proof Campaign — Cycle 2 Report

**Date:** 2026-10-29/30. **Workspace:** `~/workspace/math-hunt/erdos-699-proof/`.
**Problem:** for $1 \le i < j \le n/2$, $C(n,i)$ and $C(n,j)$ always share a
prime factor $\ge i$.

Cycle 2 executed the ranked crux list of `CYCLE1.md` §8, updated by the
external results Dennis retrieved on 2026-10-29 (`EXTERNAL_CLAIMS_2026-10-29.md`:
Price's manuscript, Van Doorn–Rocca, Del Pin, MaxDKaos, Cong). Method as in
Cycle 1: four clusters, two independent provers per cluster who did not see
each other's work, one independent verifier per cluster classifying every
numbered claim PROVED / GAP / FALSE / OPEN; plus three housekeeping items
(MaxDKaos reimplementation, the exact clearance recount, primary-source
verification) with an independent audit verifier (V-U) over the two
computational ones. All computation Python stdlib only, exact arithmetic.

**Headline.** Two regions fell completely. **Regime R1 is closed**: there is
no counterexample with $3i/2 < j < 2i$, for any $i$ (Cluster H, certified by
V-H; dependencies in §4). Combined with Price's $j \le 3i/2$ closure, the
conjecture now holds for all $j < 2i$ except the boundary line $j = 2i$
itself, which is closed for $i \ge 1.2\times10^8$ (Cluster E) and in the
Cluster G sub-regions. And **Lemma S7(2.0) is proved** with parameters
stronger than targeted ($\theta_u \le 0.3262$, $i_0 = 1.2\times10^8$),
independently by both provers and certified by V-E. For $i = 3$,
SPLIT-odd is closed by two independent routes via Price's Proposition 4.1 —
no $i = 3$ counterexample has $n$ odd — and the per-pair (LD3) frontier is
certified to $j \le 5000$; the even residual class remains open, exactly
isolated. In the campaign scope ($i \le 1000$, $\lfloor 3i/2 \rfloor < j \le
5000$; 4,249,500 pairs), the certified fully-cleared count rises from
Cycle 1's 3,700,736 to **3,919,306**, leaving **330,194** partial pairs, all
at rows $4 \le i \le 113$ (audit-certified, §6). MaxDKaos's tabulated
clearances do **not** reproduce under any tested reconstruction of his
method; only his $(3,5)$ entry is credited. **#699 is not solved**; §8
states exactly what remains open.

---

## 1. Cluster E — S7's strengthened EEES exponent (crux 1)

**Target (CYCLE1 §8.1):** Lemma S7(2.0): $\theta_u \le 0.36$ on
$\alpha = n/i \in [4, 6.4]$, $i \ge i_0$, which closes $j \le 2i$ for
$i \ge i_0$.

**Result: PROVED, with stronger parameters than targeted (V-E certified).**
The certified statement is E2's: $i_0 = 120{,}000{,}000$ and
$\theta_u \le 0.3262$ on $4i \le n \le N(i, 2i)$ (i.e. $\delta = 0.0338$
against the 0.36 budget), via the R1/R2/R3 assembled bound with S7's
Lemma B; the R3 interval-length bound and the assembly were recomputed by
V-E to the provers' pre-rounding values (0.326106 / 0.355205 / 0.413644).
**Closure (E2.15, certified):** the pair $(i, 2i)$ is closed for
$i \ge 1.2\times10^8$ (margin 0.0574), and every $j \le 2i$ is closed for
$i \ge 1.7\times10^8$ (margins 0.0277, 0.0062), modulo EEES78 and the cited
estimates. E1 independently proved the same lemma at weaker parameters
($i_0 = 2\times10^8$, $\delta = 0.004$; its Theorem E1.8 is certified).

Dependencies, honestly labelled: both proofs are modulo published explicit
estimates cited at secondary level this session (V-E checked each is
correctly stated): Dusart's $\pi(x)$ and $\theta(x)$ bounds and Robbins's
Stirling bounds for E1; for E2, Dusart 2010's $\pi(x) < x/(\log x - 1.1)$
($x \ge 60184$, secondary only) and a $\theta$ bound
$|\theta(x) - x| \le 0.006788\,x/\log x$ ($x \ge 10{,}544{,}111$) whose
statement and provenance V-E verified — it is **Dusart 1999**, not
"Dusart 2010" as E2 cited it (defect F-E2, §7; bibliographic only, no
mathematical effect).

**Empirics (independently recomputed by V-E, exact integer tests):** over
the full window for $i \le 500$ (299,743 points), $\sup_{i \ge 50}
\theta_u = 0.339629$ at $(378, 61)$ and $\sup_{i \ge 30} \theta_u =
0.357355$ at $(145, 32)$, both provers' values confirmed digit-for-digit.
Exactly **40 window pairs violate 0.36, all at $i \le 23$** (the two largest
are EEES78 exception pairs), so the lemma is FALSE for any $i_0 \le 23$ and
the empirical threshold is $\le 30$; the gap to the proved
$i_0 = 1.2\times10^8$ is the measured cost of the explicit estimates. V-E
also records the barrier both provers' files support: with the cruder
Rosser–Schoenfeld $\pi$ bound (coefficient 1.25506) the binding band ratio
becomes $0.4039 > 0.36$ — the sharp Dusart-form estimates are load-bearing.

**Residue, stated exactly:** S7(2.0)'s own residue was "pairs with
$i < i_0$, $j \le 2i$ not otherwise cleared," unsized by the provers. After
this cycle's Cluster H result (§4), every $3i/2 < j < 2i$ is closed for all
$i$ by a different argument, so the part of the S7 residue with
$j \le 2i$ not closed by any certified result is exactly the line
$j = 2i$ for $i < 1.2\times10^8$, minus the pairs/triples closed by
Cluster G's regions and by the in-scope finite criteria (§6).

## 2. Cluster F — $i = 3$ via (H3)/(LD3) (crux 2)

**Price Proposition 4.1, extracted and verified (V-F, item 1).** Both
provers quote it faithfully in every material particular, checked against
the manuscript by independent extraction: for a counterexample with
$n = Qj + R$ (Euclidean division of $n$ by $j$),
$V_i(n) \mid \Lambda_i(T)\binom{j}{h}$ with $T = R + (Q-1)(i-1)$,
$h = \max(0, \lceil (i-R)/Q \rceil)$, and $\Lambda_i(T)$ the $\ge i$ part of
$\mathrm{lcm}(1, \dots, T)$; and $C(n,i) < (\Lambda_i(T)\binom{j}{h})^2$.

**SPLIT-odd is CLOSED — certified by two independent routes (V-F, item 2).**
In the pinned case ($n$ odd $\Rightarrow v_3(n) = 1$, $j = n/3$, so
$n = 3j$, $(Q, R) = (3, 0)$, $T = 4$), Proposition 4.1 gives
$V_3(n) \mid 3j$, while the pinned bookkeeping gives
$V_3(n) = j\,U_1U_2$ with $\gcd(U_1U_2, 3) = 1$ (the 3-factor is
$3^{1-1} = 1$), forcing $U_1 = U_2 = 1$; F1's endgame (then $n - 2 = 1$,
contradiction) and F2's independent endgame (via $n - 1 = 2^a$,
$n - 2 = 3^d$, $2^a - 3^d = 1$, with its own Kummer proof of Prop. 4.1 at
$i = 3$) are both sound, edge cases ($j = 5$, $n \le 9$) included.
**Corollary: no $i = 3$ counterexample has $n$ odd, for any $j$.** No
EEES78 input is used. This is the first infinite family of the $i = 3$
problem closed since the (LD3) reduction, and it is exactly the
label-retaining argument Van Doorn–Rocca's diagnosis (§2 of the claims
file) said a completion would need.

**The even side: partial closure, exact residual (both provers, verified).**
F1 closes the four even subfamilies $(Q, R) \in \{(2,2), (3,0), (3,2),
(4,0)\}$ (F1.10, PROVED) and proves the exclusion of any relevant
prime-power factor of $n - 1$ above $(n-1)/3$ (F1.7); F1.9 records the
label-retaining Prop. 4.1 bounds for general $(Q, R)$. What remains is the
**residual even class** (F1.11 / F2.14, OPEN, correctly self-labelled):
$n$ even satisfying the (LD3) splitting conditions outside the closed
subfamilies. V-F verified F1.11's $(4,2)$ illustration exactly: Prop. 4.1
plus the $(n-1)$ argument leaves precisely $(22,5)$, $(46,11)$,
$(106,26)$, each killed per-instance by (LD3) with
$\gcd(V_3(n), C(n,j)) = 77, 69, 371$ respectively (recomputed).

**Computation (all fully recounted by V-F with independent code):**
the sweep's row $i = 3$ clears exactly $j = 5..158$; **(LD3) alone has no
solution with $2j \le n \le N(3,j)$ for every $5 \le j \le 5000$** (F2.18;
verifier's recount: 50,489 candidates, 341,633 N-filtered pairs, zero
survivors; F1.16's $j \le 2000$ recount matches F1's own counts exactly) —
so every pair $(3, j)$ with $j \le 5000$ is closed for all $n$ via the
finite reduction; and full (LD3) has **zero survivors with $n \le 10^6$**
(7,085,360 pairs; F1's and F2's counts both reproduced, including F2's
corrected 6,974,117 even pairs — see §7, item E-6).
**Net necessary conditions for an $i = 3$ counterexample, certified:**
$n$ even, $j \ge 5001$, $n > 10^6$, $v_2(C(n,3)) \ge 4$.

**Del Pin direction at $i = 3$:** F1.12 (PROVED): Del Pin's condition
$C(2j,3) \ge C(j,3)^2$ holds iff $j \le 5$ — no extension there. The
$V_3$-refined comparison (F1.13, PROVED) closes $(3, j)$ for all
$n \ge 2j$ with $v_2(C(n,3)) \le 3$ (the ratio $C(2j,3)/C(j,3) =
8 + 12/(j-2) > 8$ does the work); the brief's suggested direction
(largeness of $v_2$) is **FALSE** (F1.14): $(16, 7)$ has $v_2 = 4$ and
$V_3(16) = 35 = C(7,3)$, showing $v_2 \le 3$ is sharp uniformly. F1.14's
own final sentence (no full pair $j > 5$ closed by this comparison) is a
GAP as filed (unproved; a search found no $n \le 200{,}000$ with
$V_3(n) \le C(j,3)$ at all for $j = 6$ or $j = 10$).
Minor: F2.4's "exactly one" is literally false (only the at-least-one
form is proved, and only it is used); F2.5's sample counts were
unrecounted (no script/seed), substance verified on the verifier's own
sample (834 instances, 0 failures).

## 3. Cluster G — S4 flanks (crux 3)

**The θ input is settled at primary-source level.** Both provers
independently fetched and read Broadbent–Kadiri–Lumley–Ng–Wilk,
*Sharper bounds for the Chebyshev function θ(x)* (arXiv:2002.11068),
Corollary 2.1: $\theta(x) \le (1 + 1.93378\times10^{-8})\,x$ for **all**
$x \ge 0$; V-G re-fetched and confirmed the statement verbatim, and
Dusart's Prop. 5.1 ($\theta(x) < (1 + 1/36260)x$, all $x > 0$) as an
independent alternative. V-G records that the Broadbent bound rests on
cited RH-verification computations (Büthe, Platt–Trudgian), used as a
cited published theorem like EEES78. With $c = 1 + 1.93378\times10^{-8}$,
$K = \lceil e^{4c} \rceil = 55$ (rigorous Fraction bounds:
$e^{4c} < 54.598155$; the Dusart constant gives $< 54.604174$, same $K$),
no validity-range adjustment needed. Since PNT forces $c \ge 1$,
55 is this method's integer optimum. Rosser–Schoenfeld 1975 was not read
by either prover and is not used (see §6(c) for its corrected status).

**Certified regions (V-G §7, verbatim in substance; all additionally rest
on EEES78, the key lemma, and the S4/S10 anatomy):**
1. **Wedge, $K = 55$:** no counterexample with $55i < n < i^2$,
   $3i/2 < j < 2i$ (Cycle 1's 256 improved to 55).
2. **Support-bound closure, $i \ge 379$:** no counterexample with
   $3i/2 < j < 2i$, $2j \le n < i^2$ — all $\alpha$; subsumes region 1 and
   flank (c) ($n \le 256i$) for $i \ge 379$. G2.2 was re-derived from
   scratch by V-G; the seam is sharp: $\Psi(2, 378) = -0.0000626 < 0$,
   $\Psi(2, 379) = +0.0001945 > 0$, $\gamma^*(378) = 1.999956$.
3. **Flank (c) sliver, all $i > 256$:** pairs with $C(2j,i) \ge C(j,i)^2$
   (the Del Pin segment $j \le j^*(i)$) closed for all $2j \le n < i^2$ —
   with the corrected excess range of item E-3 (§7):
   $j^*(i) - 3i/2 \in \{3/2,\ 2,\ 5/2,\ 3\}$ in the classified range.
4. **Flank (b), large $n$:** $2i \le j \le \Gamma i$ with $n > K_\Gamma i$,
   $K_\Gamma = \lceil e^{2c\Gamma} \rceil$: $K_2 = 55$, $K_3 = 404$,
   $K_4 = 2981$.
5. **Flank (b), explicit-θ strip:** $i \ge 379$, $2i \le j \le
   \gamma^*(i)\,i$, $2j \le n < i^2$, with $\gamma^*(1000) = 2.0509$,
   $\gamma^*(10^4) = 2.1072$, $\gamma^*(10^5) = 2.1310$,
   $\gamma^*(i) \uparrow \gamma^*_\infty = 2.17178$.
6. **Flank (b), huge-$i$ strip:** $2i < j \le (12/5)i$, $i > e^{20} + 1$,
   $2j \le n < i^2$ (G1 Claim 8; its S10 support exclusion audited sound —
   the interval $(d, j/2]$ is empty since $d > j/2$ when $j > 2i$;
   coefficient 0.500155653 vs $H(5/24) = 0.51174$, margin 0.0115844).
   Regions 5 and 6 are incomparable; the support method's absolute
   ceiling is $\gamma^{**} = 2.50363$ at $n = 2j$ (exact barrier,
   G3.3(b): the failing inequality is off by $+148.9$ nats at
   $i = 1000$, $\gamma = 3$).
7. **Flank (a) shells:** the exact region $R_a = \{n \ge i^2$,
   $3i/2 < j < 2i$, $2M(n,i)\log n + 2cj \le i\log(n/i)\}$ (with
   $M = \pi(\sqrt n) - \pi(i-1)$ the candidate $V^\le$ exponent), which
   includes the band $i \ge 70$, $i^2 \le n < (i+1)^2$; and the
   candidate-bound shell $i^2 \le n \le u_{\max}(i)^2 i^2$ with
   $u_{\max} = 2.70, 3.35, 4.00$ at $i = 10^4, 10^5, 10^6$ (worst case
   $j = 2i$). The specification (G4.1/G1 Claim 10): extending the wedge
   to $n \ge i^2$ needs exactly $V^\le \le C(n,i)^\beta$ with
   $\beta < 1/2 - cj/\log C(n,i)$; the candidate bound is valid (G4.2)
   but its region is only this shell (G4.3, COMPUTED, reproduced).

**Barriers (recounted exactly by V-G):** flank (c)'s in-range anatomy
cannot close beyond the sliver — 666,006 triples (G1's search,
$40 \le i \le 170$) and 2,493 triples (G2's, $40 \le i \le 160$) where
every prime of $S(n,i) \cap [i,j]$ is simultaneously bad; showcases
verified prime by prime: $(512, 170, 256)$ with 15 bad primes *inside*
its reduction interval ($N(170,256) = 515$), and $(482, 157, 241)$ with
16 bad primes at $n = 2j$, rescued only by 26 primes $> j$; the maximum
found is 18 bad primes at $(20350, 149, 251)$. Coordinator's note: for
$j < 2i$ these triple-level regions are now also covered by Cluster H's
pair-level closure (§4); the Cluster G flank (b)/(a) regions, the
$\gamma^{**}$ ceiling, and this barrier cartography are the parts not
subsumed by §4.

## 4. Cluster H — S10's R1 counting bound (crux 4)

**Result: R1 is CLOSED (V-H adjudicated, option (a) of its brief).**
Precisely (V-H §0): *there is no counterexample with $3i/2 < j < 2i$,
for any $i$, modulo EEES78 (with its exception pairs discharged — for R1
exactly the 9 triples of V-H §1.3), S10's R1 characterisation, the key
lemma, the two cited explicit $\theta$ estimates (D1), (D2) below, and —
for the pairs $(4,7)$ and $(10,19)$ only — the finite reduction plus the
completed sweep to $n \le 20{,}000$.*

**The lever (found independently by both provers; PROVED in both files).**
In R1 a counterexample forces $V_i(n)$ squarefree with all prime factors
in $(i, j]$ (S10: every $p \in S(n,i)$ is bad, $e_p = 1$, and $p = i$ is
never bad), hence $V_i(n) \mid P(i,j) := \prod_{i < p \le j} p$, and
EEES78 gives $P(i,j) \ge V_i(n) > C(n,i)^{1/2} \ge C(2j,i)^{1/2}$. So any
pair with $P(i,j)^2 \le C(2j,i)$ is closed — a strict sharpening of the
$C(j,i)$ cap (Claim 2: $v_p(C(j,i)) = 1$ exactly for $i < p \le j$ in R1,
so there is no multiplicity slack; the gain is pure support). This
subsumes the T1/Del Pin lever: the $C(j,i)$ form closes exactly the
$C(2j,i) \ge C(j,i)^2$ pairs (Claim 3; $J_1(39) = 59$ recomputed), while
the primorial form closes the barrier pair $(39, 60)$ by a factor
$\approx 8.4\times10^{14}$ in the squared comparison (Claim 7).

**Exact scan (independently recounted by V-H, and again by HK-B §6):**
over all 249,500 R1 pairs with $i \le 1000$, $P(i,j)^2 \le C(2j,i)$ fails
at **exactly two pairs**: $(4,7)$ ($35^2 = 1225 > C(14,4) = 1001$) and
$(10,19)$ ($46189^2 = 2{,}133{,}423{,}721 > C(38,10) = 472{,}733{,}756$).
V-H extended the recount to all 999,000 R1 pairs with $i \le 2000$:
998,998 hold, same two failures; the Del Pin-fails/sharpened-closes
count 994,623 was reproduced exactly. $N(4,7) = 17$, $N(10,19) = 55$
recomputed; both pairs are fully cleared in `pairpass_20000.json`.

**Asymptotic step (H1 Claim 9: PROVED modulo (D1), (D2); this was the
provers' one disagreement — H2 labelled its version ineffective with the
effectivity a GAP and declined to claim closure).** V-H reproduced H1's
chain step by step: worst corner $j \to 2i$, $\Psi(2) = 0.041408$, net
margin $0.03726$ in log per unit $i$; (D1) is Dusart's
$|\theta(x) - x| < 3.965\,x/\log^2 x$, valid for $x \ge 2$ (tabulated in
Broadbent et al. Cor. 11.2, which supplies valid proofs of that Dusart
theorem); (D2) is Schoenfeld's $\theta(x) < 1.000081\,x$ for $x > 0$,
quoted verbatim in the secondary literature; both used in the correct
directions, and the conclusion survives even the weaker $1.001102$ bound
(net margin $0.03522$). One presentational step (monotonicity of the
error-term bound) was filled by the verifier. Large-$i$ sanity checks
($i = 10^4, 10^5$; $\gamma = 1.51, 1.75, 1.99$) give margins per unit $i$
from 0.45501 down to 0.13281, all positive. **The seam is gapless:**
exact scan to $i = 1000$, analysis from $i = 1001$. Verdict: H1's Claim
11 (R1 closed) is CERTIFIED; H2's Claim 9 GAP is repaired by H1's
Claim 9 in the combined record and does not propagate; H2's caution is
recorded as conservative, not correct as a verdict on the combined
record.

**EEES78 exceptions inside R1 (V-H §1.3):** exactly 9 triples —
$(n, i) = (30, 7)$ with $j = 11, 12, 13$ and $(56, 13)$ with
$j = 20, \dots, 25$ — all discharged by direct gcd computation
($\gcd$ values 377, 377, 29; and $57293\times3$, $42347\times3$
patterns), re-verified by V-H. Neither prover silently assumes EEES78 at
an exception pair.

**The other Cycle 2 targets in this cluster:** the combined-cap recount
is confirmed exactly (V-H §4): over R1 pairs $i < 40$,
$n \in [2j, N(i,j)]$ (10,317 triples scanned), window-badness alone
gives **377 triples** with $\ge 3$ simultaneous bad primes, distribution
$\{3{:}195,\ 4{:}166,\ 5{:}16\}$, maximum **5**; adding the key-lemma cap
$e_p \le v_p(C(j, j-i))$ kills **0** — and Claim 14 (both files) proves
this is forced in R1 (the cap equals $B_p - v_p(d!) = 1$ for $p > i$,
met with equality; $p = i$ vacuous), so the combined cap can only bite
outside R1. The CRT/density analysis (H1 Claim 12, PROVED): on
$(39, 59)$ the badness system has exactly 16,783,767 favourable classes
mod 259,106,347 (density 0.064776), but the reduction interval
$[118, 119]$ has length 2 and *both* its points satisfy all five badness
conditions — density proves abundance in long ranges and nothing in the
reduction interval; it also cannot see $e_p = 1$ (a mod-$p^2$ condition)
or $S(n,i) \subseteq [i,j]$. Numerics spot-verified throughout
($\prod_{p\ \mathrm{bad}} p = 259{,}106{,}347$ at $(119, 39, 59)$;
$C(59, 39) = 2{,}794{,}563{,}003{,}870{,}330$, quotient 10,785,390;
crude cardinality bounds close 14 of 361 R1 pairs at $i < 40$,
sharpened 359/361). One immaterial rounding nit in H2 Claim 5(b).

## 5. Cluster E/F/G/H cross-checks

The two headline closures are consistent where they overlap: Cluster H
closes $3i/2 < j < 2i$ for all $i$ (modulo EEES78 + (D1),(D2) + sweep for
two pairs); Cluster E closes $j \le 2i$ for $i \ge 1.7\times10^8$ by the
$\theta_u$ route (modulo EEES78 + its cited estimates), which is
independent of (D1),(D2) in its $j < 2i$ range except through EEES78, and
is the only certified closure of the $j = 2i$ line at large $i$. Cluster
G's $j < 2i$ regions are third, disjoint-method corroborations of part
of the same strip. No verifier found any contradiction between clusters.

## 6. Housekeeping

### (a) MaxDKaos's criterion — independently reimplemented (HK-A; audited by V-U)

Definitions fixed exactly: $G(i)$ = (first prime gap $> i$, at prime $p$)
mapped to $p + i - 1$; anchors $G(3) = 9$, $G(5) = 27$ reproduced from
raw gaps. Computed: $G(10) = 122$, $G(20) = 1148$, $G(100) = 370360$,
$G(200) = 20831522$ (own sieve to $5\times10^7$; the first gap $> 200$
is the gap of 210 at 20,831,323 — not $\sim 10^9$ as the coordinator's
brief guessed), $G(394) = 25056082480$ (from published maximal-gap
records: the first gap $> 394$ is the record gap 456 at 25,056,082,087).
Three precisely-stated candidate cut-offs were tested: A (crude Kummer
$N_K(i,j) \le G(i)$), B (sharp $U^\sharp$: no Bad$^\sharp$ point
$> G(i)$), C (sharp plus exact prime-free windows). V-U re-ran the
script end-to-end (all tables reproduced exactly), independently
confirmed $G(100)$ by its own sieve, and confirmed the $i = 3$
candidate-C settled set $\{4, 5, 6, 9\}$ by direct enumeration (note:
**not a prefix** — the isolated 9 appears when the witness $n = 16$
exits the domain).

**Verdicts:** of MaxDKaos's seven tabulated values, **only $i = 3 \to 5$
reproduces, under candidate A only** ($N_K(3,5) = 9 = G(3)$,
$N_K(3,6) = 12 > 9$); it is credited there and nowhere else (under B and
C the $i = 3$ maximum is 6). Every other entry is **NOT REPRODUCED**
under any of A, B, C: $i = 5$: claimed 12, computed A 8, B 9, C 9;
$i = 10$: 30 vs 22/25/26; $i = 20$: 138 vs 77/116/116; $i = 100$:
25063 vs 15060/22587/23305; $i = 200$: 713421 vs 432029/658087/658087;
$i = 394$: 360654145 vs 232615486/331301695/331301695 (and refuted under
C by the explicit prime-free witness $n_0 = G(394) + 1$). Diagnostic:
his claimed $j$ would be settled iff the first gap $> i$ sat
$1.084$–$1.481\times$ further out than it does (every $i \ge 5$). At
$i = 394$ the candidate-C *full settled set* is NOT TESTABLE with the
stated resources (it would need all prime-free windows up to
$N_K \approx 4.3\times10^{10}$); the claimed value is nevertheless
refuted under all three candidates. His asymptotic $j \le C\,i\log^2 i$
is not consistent with a stable informative constant over the covered
range (the ratio $j/(i\ln^2 i)$ grows by four orders of magnitude
across the table, for his values and for the computed ones); seven
finite points cannot strictly refute an asymptotic with unspecified
$C$ and onset, and the report says exactly that. **Bottom line: no
count beyond $(i, j) = (3, 5)$ under candidate A is credited.** This
supersedes the "promising but unproven" filing in
`EXTERNAL_CLAIMS_2026-10-29.md`: under every natural reconstruction of
his stated ingredients, the table is not merely unproved but too large.

### (b) The exact clearance picture in scope (HK-B; audited by V-U)

Scope: $i \le 1000$, $\lfloor 3i/2 \rfloor < j \le 5000$ (4,249,500
pairs). Baseline is now the cap-20,000 sweep classification
(`pairpass_20000.json`): 1,302,183 cleared in scope, every row a clean
prefix. The audited certified chain (V-U headline; step order as
computed, marginals are order-dependent, the union is not):

| Step | Marginal | Running cleared |
|---|---:|---:|
| (1) cap-20,000 sweep baseline | 1,302,183 | 1,302,183 |
| (2) S3 uniform, $i \ge 132$ | +2,383,028 | 3,685,211 |
| (3) S1 crude (10001 predicate) | +17,085 | 3,702,296 |
| (4) S1 sharp, sweep-relative S20 form | +123,949 | 3,826,245 |
| (5) S3 per-pair, $i \le 131$ (after S20) | +88,849 | 3,915,094 |
| (6) Primorial R1 | +0 | 3,915,094 |
| (7) $i = 3$ (LD3) to $F_3 = 5000$ (V-F-certified) | +4,212 | **3,919,306** |

**Certified: 3,919,306 of 4,249,500 pairs fully cleared; 330,194
partial pairs remain** (V-U verified the arithmetic and re-ran
`counts_c2.py` end-to-end: regenerated JSON identical, no mismatches;
the S20 sharp form's theorem and implementation — candidate set
$\{20001\} \cup \{$jump points $q = p^e\}$, left edge load-bearing —
verified, with 32/32 seeded brute-force pairs agreeing; step (5)
recomputed per-pair with no threshold inversion: rows 100–131 exact at
every row, rows 114–131 confirmed fully cleared, 49/49 sample pairs
below 100). The step-(7) adjustment is exactly $5000 - 788 = 4{,}212$:
the S20 chain's row-3 frontier before (LD3) is 788.

Notes on the steps: step (2)'s marginal fell from Cycle 1's 2,891,106
because the deeper sweep already owned 508,078 of those pairs; step
(5)'s per-pair S3 clearances (+88,849 after S20; +168,359 in the
literal chain) were far larger than the brief expected and finish rows
114–131 entirely. Step (6) is +0 in scope — independently recounted:
the primorial criterion fails in scope only at $(4,7)$, $(10,19)$,
both baseline-cleared; indeed every in-scope R1 pair has
$N(i,j) \lesssim 6.4i \le 6{,}400 < 20{,}000$ and was already
sweep-cleared. The lever's value is as a proof (§4), not a count.

**Residual map (certified):** after steps (1)–(6) the partial rows are
exactly $3 \le i \le 113$; step (7) closes row 3, leaving **110 partial
rows, $4 \le i \le 113$**, each with surviving tail $j \in [F_i + 1,
5000]$ at the S20 frontier $F_i$ (full table in `counts_c2.md`;
samples: $F_4 = 180$, $F_5 = 399$, $F_{10} = 410$, $F_{50} = 1616$,
$F_{100} = 3746$, $F_{113} = 4586$). Every residual pair has
$j > F_i \ge 2i$ by a wide margin, consistent with §4: no residual pair
lies in R1's range. Against Cycle 1's 3,700,736 cleared / 548,764
partial, Cycle 2's union is a superset (the Cycle 2 chain includes the
old sweep's range, the same S3-uniform and S1-crude criteria, and adds
S20-sharp, S3 per-pair, and the (LD3) row): **+218,570 pairs newly
cleared in scope.**

### (c) Primary-source verification (HK-C; file `verification/primary_sources_c2.md`)

- **Dusart 2018, Corollary 5.5: PRIMARY VERIFIED.** Read in the journal
  text (*Ramanujan Journal* 45 (2018), 227–251): "For all
  $x \ge 468\,991\,632$, there exists a prime $p$ such that
  $x < p \le x(1 + 1/(5000\ln^2 x))$" — number, threshold, constant,
  form all match S3/P-C1/P-C2 exactly. P-C1's Flag F2 is closed.
- **Axler 2017, Theorem 4.1: PRIMARY VERIFIED, label settled.**
  arXiv:1703.08032v2, Theorem 4.1: for every $x \ge 6\,034\,256$ there
  is a prime $p$ with $x < p \le x(1 + 0.087/\log^3 x)$ (plus the
  $198.2/\log^4 x$ clause S3 uses). "Thm 4.1" is correct (also
  announced as Thm 1.4 in the introduction); citations should specify
  **v2** (v1's Theorem 4.1 is a different interval). P-C2's
  unverified-label flag is closed.
- **Rosser–Schoenfeld $\theta(x) < 1.1x$: PARTIALLY VERIFIED
  (secondary only), with a bibliographic correction.** The primary text
  was not sighted. The openly readable secondary quote (Garcia–Lee)
  gives "Rosser–Schoenfeld [Thm. 9]: $\theta(x) < 1.01624x < 1.1x$ for
  $x > 0$" from the **1962** *Illinois J. Math.* paper "Approximate
  formulas for some functions of prime numbers" — the campaign's
  "1975" attribution conflates it with "Sharper Bounds for the
  Chebyshev Functions" (*Math. Comp.* 29, 1975). Nothing in Cycle 2
  depends on it: Cluster G superseded it with primary-verified bounds
  (§3).

## 7. Errors found (including the coordinator's and the briefs')

- **E-1 (coordinator's HK-B brief, step (4) definition):** the sharp
  criterion was specified in all-$n$ form ("Bad$^\sharp(i,j) = \emptyset$
  over all $n \ge 2j$"), under which the frontier anchor
  $J_K^\sharp \ge J_K$ fails at 998 of 1000 rows, because $2j \in
  \mathrm{Bad}^\sharp(i,j)$ at every $i \ge 4$ (S1's own diagonal
  barrier, stated in `strategies/S1.md`). The validated form of the
  Kummer clearance was always sweep-relative; HK-B computed the literal
  form (adds 0) and the sweep-relative S10/S20 forms, and V-U certified
  S20 as the headline. The brief's minima prescription was also wrong
  (test at jump points $q$, not $q - 1$; the anchor
  $\mathrm{Bad}^\sharp(3,7) = \{16\}$ turns on it). Both errors were
  caught by the computation agent, not by the coordinator.
- **E-2 (coordinator's Cluster F brief, lever suggestion):** "large
  $v_2(C(n,3))$ closes pairs" is backwards (F1.14, FALSE, with the
  $(16,7)$ sharpness example); the closing side is $v_2 \le 3$.
- **E-3 (both Cluster G provers, summary gloss):** the claim
  $j^*(i) - 3i/2 \in \{1.5, 2\}$ for $i \le 2000$ is **FALSE**: exact
  classification (V-G) gives excess values $\{3/2, 2, 5/2, 3\}$, the
  excess-3 case occurring at 521 odd $i \in [959, 1999]$ (smallest
  $i = 959$, $j \in \{1439, 1440, 1441\}$); the correct uniform bound
  is $\gamma \le 3/2 + 3/i$. (This also matches the campaign's own
  Del Pin offset data: offset 3 at $i = 5000$.) No downstream proof
  uses the gloss; G2's "1859 two-point cases" is the size-$\ge 2$ count
  mislabelled.
- **E-4 (P-E1, Lemma E1.10):** the monotonicity proof has a
  factor-of-2 error (positivity of $\Phi'$ needs $f(\alpha) >
  \alpha f'(\alpha)$, not $\frac{\alpha}{2} f'(\alpha)$ as printed);
  the statement is true and V-E supplies the corrected proof, but as
  filed E1's closure Theorem E1.9 is a GAP in Case B only (Case A
  sound; the coupling and both margins correct). Subsumed by E2's
  certified closure.
- **E-5 (P-E2, Input E2.3):** the $\theta$ bound cited as "Dusart
  2010" is Dusart **1999** (V-E). Bibliographic only.
- **E-6 (phantom summary figures, self-caught pre-verification):**
  P-F2's first summary reported 19,971,940 pairs for its even-(LD3)
  search; the authoritative session output, now in the file, is
  6,974,117 pairs / 0 survivors (V-F recount reproduced it exactly).
  P-H2's interim summary reported scan totals of 1,996,000 pairs /
  1,992,343 / 1,995,998; the definitive scan in the file is 999,000
  pairs / 994,623 / 998,998 (V-H reproduced all three). In both cases
  the false figures appeared only in agent chat summaries, never in
  the deliverable files as verified — the campaign's standing lesson
  (only verifier-certified files are the record) is what caught them.
- **E-7 (minor):** H2 Claim 5(b) rounding nit (exact ratio
  $382{,}372{,}565{,}116{,}467.98\ldots$, printed $\ldots 468$); F2.4's
  "exactly one" (see §2); two immaterial one-count endpoint
  conventions in Cluster F (V-F).
- **E-8 (coordinator's HK-A brief):** the guess that the first gap
  $> 200$ occurs around $10^9$ is wrong; it occurs at
  $20{,}831{,}323$ (gap 210), which is what made $i = 200$ fully
  testable by sieve.

## 8. What is NOT proved (claim discipline)

- **#699 is not solved.** No claim in this cycle is a proof of the
  general case.
- The remaining open territory, exactly: **(i) Regime R3 ($j > 2i$) in
  general**, outside the certified sub-regions of §3 items 4–6
  (Cluster G: $j \le \gamma^*(i)\,i$ for $i \ge 379$ with $n < i^2$;
  wedge ranges $n > K_\Gamma i$ for $\Gamma \le 4$; $j \le (12/5)i$
  for $i > e^{20}+1$ with $n < i^2$) and outside the in-scope finite
  criteria. The in-scope residue is 330,194 pairs at rows
  $4 \le i \le 113$, all with $j > F_i \ge 2i$. **(ii) The line
  $j = 2i$ (R2)** for $i < 1.2\times10^8$ in general, outside §3 item
  5/7's ranges and the finite criteria; for $i \ge 1.2\times10^8$ it is
  closed by Cluster E, and for $j < 2i$ there is nothing left at any
  $i$ (Price + §4). **(iii) $i = 3$'s residual even class** (§2):
  a counterexample there must have $n$ even, $j \ge 5001$,
  $n > 10^6$, $v_2(C(n,3)) \ge 4$, and satisfy the (LD3) splitting
  conditions outside the four closed $(Q,R)$ subfamilies; (H3) remains
  open. **(iv) Flank (a)** beyond the §3 item 7 shells, and flank (c)
  at $257 \le i \le 378$ as a triple-region statement beyond the
  sliver (its pairs are closed by §4; the wedge/support methods alone
  do not reach it).
- Cluster E's and Cluster H's analytic steps are modulo the cited
  published explicit estimates listed in §1/§4 (several at
  secondary-verification level, all checked correctly stated by the
  verifiers); Cluster G's wedge/support bounds are modulo
  Broadbent et al. Cor. 2.1, which itself rests on cited
  RH-verification computations. EEES78 is a cited published theorem
  throughout, as in Cycle 1.
- The clearance counts of §6(b) are theorems about the finite scope
  relative to the Phase 0 reduction and the completed sweep; they are
  not a proof of the conjecture in that scope by pure thought.
- MaxDKaos's asymptotic claim is not strictly refuted (§6(a)); his
  finite table is not reproduced under any tested candidate, and no
  count from it is credited beyond $(3,5)$ under candidate A.

## 9. Cycle 3 crux list (ranked)

1. **R3's lower band ($j > 2i$, $p \in [i, j/2]$).** Now the binding
   frontier of the whole problem. Available inputs not yet exploited:
   the nesting in S10's (†) (residues mod $p^{k+1}$ determine residues
   mod $p^k$ — S10 task T3); the combined cap
   $e_p \le \min(\Delta_p,\ B_p - v_p(d!))$, proved *unable* to bite
   inside R1 (H Claim 14) and therefore an R3-specific tool; and the
   support method's hard ceiling $\gamma^{**} = 2.50363$ at $n = 2j$,
   which says size/support arguments cannot finish R3 — a non-size
   input is required beyond $\gamma^{**}$.
2. **$i = 3$'s residual even class.** Push F1.9's label-retaining
   Prop. 4.1 bounds and the higher-digit Kummer conditions against the
   F1.11/F2.14 conditions; generalise the $(4,2)$-style finite
   analysis across $(Q, R)$. (Extending the per-pair (LD3) frontier
   past $j = 5000$ is computation, not proof, and is ranked with
   item 5.)
3. **The $j = 2i$ line for $i < 1.2\times10^8$** (R2), especially
   $i < 379$ at $n \ge i^2$: S10's R2 analysis (the prime $i$ itself
   under Theorem 5's cap $\lfloor \log_i 2i \rfloor = 1$) plus the
   Cluster G shells are the current partial coverage.
4. **Sharpen Cluster E.** Close the gap between the proved
   $i_0 = 1.2\times10^8$ and the empirical threshold ($\le 30$) for
   S7(2.0) by feeding Broadbent-grade $\theta$ inputs (primary-verified
   in §3) into the R2/R3 assembly in place of the Dusart 1999/2010
   forms, and attempt S7(2.25) (budget 0.3516; empirical sup at
   $i \ge 100$ is 0.2918) with the same machinery.
5. **Flank (a) beyond the shells:** a real bound on $V^\le$ in the
   multi-digit regime $p \le \sqrt n$ (the specification is now exact:
   $V^\le \le C(n,i)^\beta$, $\beta < 1/2 - cj/\log C(n,i)$).
6. **In-scope residuals as computation (labelled as such):** the
   330,194 partial pairs at rows $4 \le i \le 113$ — a deeper sweep or
   per-pair criteria with better gap data; this extends the verified
   region but proves nothing new in kind.
7. **Citation completion:** sight Cluster E's Dusart inputs and
   Schoenfeld's (D2) in primary text (all currently secondary-only,
   correctly stated); the campaign's other load-bearing citations
   (Dusart 2018 Cor. 5.5, Axler Thm 4.1, Broadbent Cor. 2.1, Dusart
   Prop. 5.1) are now primary-verified.

## 10. File index

- `CYCLE2.md` — this report. `TOKENS2.md` — run/token ledger.
- `proofs/` — Cycle 2 prover documents: `P-E1.md`, `P-E2.md`
  (+ `P-E1_empirical.py`), `P-F1.md` (+ `P-F1_checks.py`), `P-F2.md`,
  `P-G1.md`, `P-G2.md`, `P-H1.md`, `P-H2.md`.
- `verification/` — `V-E.md`, `V-F.md` (+ `V-F_checks.py`,
  `V-F_chunkD.py`, `V-F_chunkEG.py`, `V-F_chunkF.py`), `V-G.md`,
  `V-H.md` (+ `V-H_checks.py`, `V-H_scan.py`, `V-H_scan_fast.py`),
  `V-U.md`, `counts_c2.py` / `counts_c2.md` / `counts_c2.json`,
  `maxdkaos_reimplementation.py` / `maxdkaos_reimplementation.md`,
  `primary_sources_c2.md`.
- Prior record: `CYCLE1.md`, `REFEREE.md` (+ 2026-10-29 addendum),
  `EXTERNAL_CLAIMS_2026-10-29.md`; sweep data in
  `~/workspace/math-hunt/erdos-699/` (`RESULTS.md`,
  `pairpass_20000.json`, `sweep_summary_20000.json`).
