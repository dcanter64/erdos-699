# V-U: Audit verification of the Cycle 2 housekeeping computations (HK-A, HK-B)

**Verifier:** V-U (independent). **Audited:** `verification/counts_c2.md` /
`counts_c2.py` / `counts_c2.json` (HK-B) and
`verification/maxdkaos_reimplementation.md` / `.py` (HK-A), against
`strategies/S1.md`, `verification/V-F.md` (per-pair (LD3) frontier
$F_3 = 5000$ certified there), and `verification/V-H.md` (primorial-R1
lever certified there). **Method:** both scripts re-run end-to-end by
the verifier; the load-bearing parts of each recomputed with the
verifier's own independent code (Python stdlib only, exact integer /
`Fraction` arithmetic throughout). Verifier's scripts and logs:
`~/workspace/vu_scratch/vu_audit.py` (Items 2, 5) and
`~/workspace/vu_scratch/vu_item3.py` (Item 3). (A `/tmp` wipe mid-audit
destroyed the first Item 3 run after rows 100–109 had already matched;
the full run was repeated from durable storage and is the one reported.)

---

## Certified headline counts

**The certified chain is the S20 chain** (Item 2: the sweep-relative
sharp form is sound; the literal form L is not the headline). In scope
($1 \le i \le 1000$, $\lfloor 3i/2 \rfloor < j \le 5000$; 4,249,500
pairs):

| Step | Marginal | Running cleared |
|---|---:|---:|
| (1) cap-20,000 sweep baseline | 1,302,183 | 1,302,183 |
| (2) S3 uniform, $i \ge 132$ | +2,383,028 | 3,685,211 |
| (3) S1 crude | +17,085 | 3,702,296 |
| (4) S1 sharp, **S20 form** | +123,949 | 3,826,245 |
| (5) S3 per-pair, $i \le 131$ (after S20) | +88,849 | 3,915,094 |
| (6) Primorial R1 | +0 | 3,915,094 |
| (7) $i=3$ (LD3) to $F_3 = 5000$ (V-F-certified) | +4,212 | **3,919,306** |

**Certified final numbers: 3,919,306 of 4,249,500 pairs cleared;
330,194 partial pairs remain.** Arithmetic verified:
$3{,}919{,}306 + 330{,}194 = 4{,}249{,}500$. Steps (1)–(6) alone give
3,915,094 cleared / 334,406 remaining (the $F_3 = 158$ line). The
step-(7) adjustment is exactly $5000 - 788 = 4{,}212$: the S20 chain's
row-3 frontier before step (7) is 788, every criterion in the chain is
a row prefix, so the pairs $(3, j)$ with $j \in (788, 5000]$ are
precisely those not cleared earlier in the chain, and step (7) clears
all of them. (In the literal chain the same adjustment would be
$5000 - 465 = 4{,}535$, matching HK-B's L table.)

**Residual map (certified chain).** After steps (1)–(6) the partial
rows are exactly $3 \le i \le 113$ (111 rows), each with surviving tail
$j \in [F_i + 1, 5000]$ at the S20 frontier $F_i$; step (7) closes
row 3, leaving **110 partial rows, $4 \le i \le 113$**. Frontiers
(steps (1)–(6), S20) for the requested rows, read from the audited
computation and re-verified against `counts_c2.json` (the S20 residual
counts sum to exactly 334,406):

| $i$ | $F_i$ (S20) | Surviving count |
|---:|---:|---:|
| 3 | 788 | 4,212 (all cleared by step (7)) |
| 4 | 180 | 4,820 |
| 5 | 399 | 4,601 |
| 10 | 410 | 4,590 |
| 50 | 1,616 | 3,384 |
| 100 | 3,746 | 1,254 |
| 113 | 4,586 | 414 |

---

## Part 1 — HK-B (counts)

### Item 1 — Re-run of `counts_c2.py`: **CONFIRMED**

The script re-ran end-to-end with exit 0, and the regenerated
`counts_c2.json` is **identical** (full dictionary equality) to the
file as delivered. Every number in `counts_c2.md` was compared against
the printed output and the JSON; **no mismatch was found**, including:
baseline 1,302,183; marginals +2,383,028 (step 2), +17,085 (step 3),
literal +0 (step 4L), +168,359 (step 5, literal chain), +0 (step 6);
literal union 3,870,655 with remaining 378,845 at $F_3 = 158$,
377,310 at $F_3 = 2000$, 374,310 at $F_3 = 5000$; S10 chain (step 4
+41,374, step 5 +142,194) union 3,885,864; S20 chain (step 4 +123,949,
step 5 +88,849) union 3,915,094 with remaining 334,406 at $F_3 = 158$.
The internal validation anchors also reproduced: crude-vs-old-baseline
328,079, $J_K(100) = 1045$, $J_K(1000) = 2541$,
$\mathrm{Bad}^{\sharp}(3,7) = \{16\}$ by both methods, the four $G$
anchor values, the exact scan of R1 failing only at $(4,7)$ and
$(10,19)$, and 111 residual rows $3 \le i \le 113$ in every chain. The
only difference from the .md is the wall-clock runtime (15.5 s here vs
66 s recorded), which is machine variance and carries no number.

### Item 2 — The sharp-sawtooth headline form (S20): **CONFIRMED — S20 is sound; the certified headline is the S20 chain**

*Theorem check (from S1).* S1 Theorem A: a counterexample at
$(n, i, j)$ satisfies $C(n,i) \le U^{\sharp}(n,i)\, C(j, j-i)$, i.e.
$G_i(n) := C(n,i)/U^{\sharp}(n,i) \le C(j,i)$. By S1 Lemma 5(a),
$\mathrm{Bad}^{\sharp}(i,j) \subseteq [2j, N_K(i,j)]$. Hence if
$\mathrm{Bad}^{\sharp}(i,j) \cap (20000, N_K(i,j)] = \varnothing$ and
the completed cap-20,000 sweep excludes every $n \le 20000$, no
counterexample exists at $(i,j)$: the pair is cleared. That is exactly
the S20 predicate. The literal form L (emptiness over **all**
$n \ge 2j$) is a stronger, different claim; HK-B's finding that it
adds 0 and that its frontier anchor fails at 998 rows is a property
of the definition, not an error, and L is not used in the headline.

*Implementation check.* HK-B computes
$M_i = \min_{n \ge 20001} G_i(n)$ over the candidates
$\{20001\} \cup \{q = p^e \le \mathrm{cap}\}$ and clears $(i,j)$ iff
$C(j,i) < M_i$. This is the right candidate set: by S1 Lemma 5(b),
$G_i$ is strictly increasing on each interval where $U^{\sharp}$ is
constant, and $U^{\sharp}$ jumps exactly at prime powers $p^e$
($p < i$), so on $(20000, \mathrm{cap}]$ every local minimum is at the
left edge $n = 20001$ or at a jump point. The code tests exactly
those points, **including the left edge 20001 itself** (not 20000:
the sweep already covers $n \le 20000$). Two fine points verified:
(i) the code's prime-power generator uses $e \ge 2$ only, which is
vacuously complete on $(20000, \mathrm{cap}]$ because the $e = 1$
jumps are primes $p < i \le 1000$, none in range — the verifier's
generator included $e = 1$ and obtained identical verdicts;
(ii) the cap is sound: the code verifies exactly that
$F_i(\mathrm{cap}) > C(5000, i)$, and since $G_i \ge F_i$ with $F_i$
increasing (S1 Lemmas 4–5), no $n > \mathrm{cap}$ can be sharp-bad
for any $j \le 5000$; the verifier independently recomputed such a
cap and confirmed $F_i(\mathrm{cap}) > C(5000,i)$ for
$i \in \{3, 10, 100\}$ (caps 512639, 1730159, 101261).

*Brute-force check.* 32 seeded pairs (frontier-adjacent at
$i \in \{3, 5, 10, 20, 50, 100\}$ from the JSON S20 frontiers, plus 14
seeded random pairs, seed 20261030): **0 mismatches** between the
code's verdict and direct computation. Of these, 12 pairs had
$N_K \le 26000$ and were checked by a full direct scan of **every**
$n \in (20000, N_K]$; 19 were checked by an exhaustive scan of
$(20000, 23000]$ plus every jump point in $(20000, N_K]$; 1 had
$N_K < 20000$ (trivially cleared). The left edge is load-bearing in
practice: most non-cleared verdicts in the sample are witnessed at
$n = 20001$ itself, and the code tests it.

**Conclusion:** no implementation hole found. The S20 form is sound
and is the certified headline (headline table above). The S10 form
(union 3,885,864) is likewise sound but strictly weaker and is not
used.

### Item 3 — Independent recomputation of step (5): **CONFIRMED**

Verifier's own code, no threshold inversion anywhere: own sieve to
21,000,000; **$G$ convention stated:** $G(X) = \max\{p_{k+1} - p_k :
p_k < X\}$ (strict lower end), which the verifier confirmed matches
S3/P-C and HK-B by reproducing the anchor values
$G(10127) = 36$, $G(1{,}400{,}000) = 132$, $G(2{,}010{,}733) = 132$,
$G(2{,}010{,}734) = 148$. For each pair, $N(i,j)$ was computed exactly
by binary search on `math.comb` ($N(i,j) = \max\{n : C(n,i) <
C(2j, 2i)\}$) and the criterion $i \ge G(N(i,j))$ applied directly.

* **Rows $i \in [100, 131]$ in full** (every pair not cleared by
  steps (1)–(3) of the literal chain, i.e. $j$ above
  $\max(J_i^{20000}, J_K(i))$): the per-row newly-cleared counts agree
  with `counts_c2.json` at **all 32 rows exactly**, and in each row
  the first failing $j$ is exactly $J^{S3pp}(i) + 1$, confirming the
  cleared set is the prefix the $B_i$ shortcut claims. This validates
  HK-B's threshold-inversion shortcut on the rows where it matters
  most, including the claimed literal-chain total contribution of
  these rows toward the +168,359.
* **Rows 114–131 end fully cleared: CONFIRMED.** For every
  $114 \le i \le 131$ the per-pair recomputation clears every
  remaining $j$ up to 5000 (no first failure), $J^{S3pp}(i) = 5000$,
  and directly $N(i, 5000)$ ranges from 580,923 ($i = 114$) down to
  504,006 ($i = 131$, matching HK-B's printed value) with
  $G(N(i,5000)) = 114 \le i$ in every case.
* **Seeded sample below 100:** 49 pairs (seed 699699; rows
  3, 5, 10, 17, 25, 33, 50, 64, 75, 88, 99, plus $(3, 5000)$ and the
  frontier-adjacent pairs $(50, 627), (50, 628), (99, 3727),
  $(99, 3728)$): **0 mismatches** against the JSON frontiers.

### Item 4 — Certified final numbers and arithmetic: **CONFIRMED**

As stated in the headline section: cleared + remaining
$= 3{,}919{,}306 + 330{,}194 = 4{,}249{,}500$ (and
$3{,}915{,}094 + 334{,}406 = 4{,}249{,}500$ before step (7)); the S20
per-row residual counts in `counts_c2.json` sum to exactly 334,406;
the step-(7) adjustment at $F_3 = 5000$ is exactly the 4,212 pairs
$(3, j)$, $788 < j \le 5000$, none cleared earlier in the S20 chain
(the chain frontier is a prefix at 788). The intermediate $F_3$
values in the certified chain are: $F_3 = 158$: total 3,915,094,
remaining 334,406; $F_3 = 2000$: total 3,916,306, remaining 333,194;
$F_3 = 5000$: total 3,919,306, remaining 330,194.

---

## Part 2 — HK-A (MaxDKaos)

### Item 5 — Re-run of `maxdkaos_reimplementation.py` and spot checks: **CONFIRMED**

The script re-ran end-to-end with exit 0 and reproduced its own .md
tables **exactly**: $G$ values 9, 27, 122, 1148, 370360, 20831522 (and
25056082480 at $i = 394$ from the published maximal-gap records);
candidate prefixes A/B/C — $i{=}3$: 5/6/6; $i{=}5$: 8/9/9;
$i{=}10$: 22/25/26; $i{=}20$: 77/116/116; $i{=}100$:
15060/22587/23305; $i{=}200$: 432029/658087/658087; $i{=}394$:
232615486/331301695/331301695 — and the diagnostics at the claimed
$j$ ($M^{\sharp}$ = 40, 157, 1548, 433530, 22583327, 27682720715
against $G$ = 27, 122, 1148, 370360, 20831522, 25056082480). The
script's internal brute-force validations (segment minima vs full
scans, including at the $i = 100$ B-threshold 22587/22588) all passed
during the re-run. (Runtime 32.2 s vs 129.5 s recorded: machine
variance only.)

Independent spot checks by the verifier:

* **$G(100) = 370360$: CONFIRMED by the verifier's own sieve.** An
  exhaustive in-order scan of all prime gaps up to 400,000 (the
  verifier's own sieve, not the script's) finds the first gap
  $> 100$ at $p = 370261$ with gap 112 (next prime 370373, confirmed
  consecutive in the verifier's prime list), so no gap $> 100$ occurs
  below it and $G(100) = 370261 + 100 - 1 = 370360$. This is the
  script's full-sieve logic spot-verified independently, not merely
  trusted.
* **$i = 3$ candidate-C settled set $\{4, 5, 6, 9\}$: CONFIRMED by
  direct enumeration.** The verifier computed
  $\mathrm{Bad}^{\sharp}(3, j)$ by brute scan for $j = 4, \dots, 10$
  and tested each bad $n$ for prime-freeness of $(n-3, n]$ directly:
  $j = 4, 5, 6$ have empty bad sets (settled); $j = 7$ has
  $\mathrm{Bad}^{\sharp} = \{16\}$ with 16 prime-free (not settled);
  $j = 8$ has bad set $\{16, 17, 18\}$ with the same prime-free
  witness 16 (not settled); $j = 9$ has bad set $\{18, 19, 20, 21\}$
  with no prime-free member (settled); $j = 10$ fails via $n = 22$.
  So within the enumerated range the C-settled set is exactly
  $\{4, 5, 6, 9\}$, as the .md states.

### Item 6 — HK-A's bottom line: **CONFIRMED**

The .md's conclusions follow from the (reproduced) tables. Of
MaxDKaos's seven tabulated values, only $i = 3 \to 5$ reproduces,
and only under candidate A (crude Kummer: $N_K(3,5) = 9 = G(3)$,
$N_K(3,6) = 12 > 9$); it is credited there and nowhere else. Every
other claimed entry (12, 30, 138, 25063, 713421, 360654145) is
**NOT REPRODUCED under any of candidates A, B, or C**: at each
claimed $j$ the exact $M^{\sharp}(i, j_{\text{claim}})$ exceeds the
true $G(i)$, by factors 1.08–1.48 on the $n$-side. At $i = 394$ the
candidate-C **full settled set is NOT TESTABLE** with the stated
resources, for exactly the obstruction the .md gives (deciding
individual $j$ beyond the first failure needs all prime-free windows
up to $N_K(394, j_{\text{claim}}) = 43{,}214{,}243{,}868$, beyond any
feasible sieve and not supplied by maximal-gap records) — while the
claimed value itself **is refuted under all three candidates**: under
A and B by the exact prefixes 232,615,486 and 331,301,695, and under
C by the witness $n_0 = G(394) + 1 = 25{,}056{,}082{,}481$, which is
prime-free (first window) and was verified sharp-bad at
$j = 331{,}301{,}696$ in the re-run, hence remains sharp-bad at the
claimed $j = 360{,}654{,}145 < n_0/2$. The verifier concurs with the
credit line: **no count beyond $(i, j) = (3, 5)$ under candidate A is
credited.**

---

## Summary of verdicts

| Item | Verdict |
|---|---|
| 1. HK-B re-run vs .md / JSON | CONFIRMED (no mismatch; JSON identical after re-run) |
| 2. S20 sharp form sound; headline = S20 chain | CONFIRMED (theorem verified from S1; candidate set and left edge verified; 32/32 brute-force pairs agree) |
| 3. Step (5) per-pair recomputation | CONFIRMED (rows 100–131 exact at every row; rows 114–131 fully cleared; 49/49 sample pairs below 100) |
| 4. Certified final numbers | CONFIRMED (3,919,306 cleared / 330,194 remaining at $F_3 = 5000$; sums and step-(7) adjustment exact) |
| 5. HK-A re-run and spot checks | CONFIRMED (all tables reproduced; $G(100)$ and $i{=}3$ C-set verified independently) |
| 6. HK-A bottom line | CONFIRMED (only (3,5) under A credited; $i{=}394$ C full set NOT TESTABLE, claimed value refuted under A, B, C) |

No item required a CORRECTED number, and no load-bearing claim was
NOT CONFIRMED.

— V-U
