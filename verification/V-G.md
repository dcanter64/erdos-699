# Verification V-G — Cluster G (S4 flanks), Cycle 2

**Scope.** Independent verification of `proofs/P-G1.md` (Claims 0–13) and
`proofs/P-G2.md` (Claims G1.1–G1.4, G2.1–G2.4, G3.1–G3.3 (+ table entry
G3.4), G4.1–G4.4), against `strategies/S4.md` §5, `strategies/S10.md`
§4–§5, and `verification/primary_sources_c2.md`.

**Method.** Primary sources fetched and read via `browser.open`
(arXiv PDFs, full text). All computations redone from scratch with
Python stdlib only, exact integer arithmetic (`math.comb`,
`fractions.Fraction`) wherever a claim is finite, `lgamma`/float only
where the file itself is log-domain (with boundary margins recorded).
Bulk barrier counts were re-run in full, not sampled. Verdicts:
**PROVED** / **COMPUTED (verified)** / **GAP** / **FALSE** / **OPEN**.

---

## 1. The θ input (Task 1) — primary verification

**Broadbent–Kadiri–Lumley–Ng–Wilk, arXiv:2002.11068v2 (27 Jan 2021),
Corollary 2.1 — CONFIRMED verbatim** (PDF p. 4):

> θ(x) ≤ (1 + 1.93378·10⁻⁸)·x for all x ≥ 0.

Its printed proof combines Büthe's θ(x) < x for 0 < x ≤ 10¹⁹
([4, Thm 2, (1.7)]) with M₀ = ε(19 log 10) = 1.93378·10⁻⁸ from
Table 8. **Dependence recorded:** the bound rests on cited
RH-verification computations (Büthe; Platt–Trudgian — the paper's
Theorem 2 is explicitly headed "Büthe, Platt-Trudgian"). Per campaign
practice this is a citable published theorem (same status as EEES78),
not re-verified here; both prover files state this dependence
correctly (G2 explicitly, G1 by describing the proof).

**Table 14 row used by G1 Claim 8 — CONFIRMED verbatim** (PDF
Appendix B.5.1): Table 14 states (1 − m₀)x < θ(x) < (1 + M₀)x for all
x > X₀ = X₁, and the row log X₀ = log X₁ = 20 gives
**M₀ = 4.2676·10⁻⁵, m₀ = 9.1639·10⁻⁵**, exactly as G1 quotes.

**Dusart, arXiv:1002.0442 — CONFIRMED verbatim** (PDF p. 4):
Proposition 5.1: ϑ(x) − x < x/36260 for all x > 0. Theorem 5.2 table
contains (k, η_k, x_k) = (2, 3.965, 2) and (2, 0.2, 3 594 641),
exactly the rows G2 uses; the π(x) bounds G2 quotes
(π(x) ≤ (x/log x)(1 + 1.2762/log x), x > 1; π(x) ≥ (x/log x)(1 + 1/log x),
x ≥ 599) also appear verbatim (p. 2).

**The constant K = 55 — re-derived with rigorous rational bounds**
(G2 Appendix A method, reproduced): with
e < e_ub = Σ_{k≤12} 1/k! + 1/(12·12!) = 2.7182818284601415…,
e_ub⁴ = 54.5981500332…, and e^y ≤ 1/(1−y):

- e^{4c_B} < e_ub⁴/(1 − 4·1.93378·10⁻⁸) < **54.598155** < 55 (float value 54.5981542564);
- Dusart alternative: e^{4c_D} < e_ub⁴/(1 − 4/36260) < **54.604174** < 55 (float 54.6041733).

Hence K = ⌈e^{4c}⌉ = **55 from either bound**. **No x₀ adjustment is
needed**: Corollary 2.1 holds for all x ≥ 0 and Dusart Prop. 5.1 for
all x > 0, so the wedge restatement carries no validity threshold;
the only i-threshold is nonemptiness of the region (i > 55).
Rosser–Schoenfeld 1975 is not used by either file and remains not
primary-verified (consistent with `primary_sources_c2.md` Item 3).

---

## 2. P-G1 — claim-by-claim

| Claim | Verdict | Verification |
|---|---|---|
| 0 (entropy bounds) | **PROVED** | Standard binomial-term argument; ratio T_{k+1}/T_k and mode argument correct. |
| 1 (θ citation) | **PROVED** (citation) | Cor. 2.1 and Table 14 row confirmed at primary source (§1 above). |
| 2 (wedge K = 55) | **PROVED** | Chain rechecked: V squarefree on [i,j] for n < i²; V² ≤ e^{2cj} < e^{4ci}; e^{4c} = 54.598154… < 55 < (n/i) ≤ C(n,i)^{1/i}; EEES78 exception disposal valid (region forces i ≥ 56, n > 3080). Remark (i) (no K ≤ 54 from any all-x bound θ ≤ cx, since PNT forces c ≥ 1 and e⁴ = 54.598…) is sound. |
| 3 (flank (c) plain chain region) | **PROVED** | Condition C(2j,i) ≥ C(j,i)² is α-independent (worst case n = 2j, monotonicity of C(n,i) in n); closes exactly {(α,γ): 2γ ≤ α ≤ 256, γ ≤ j*(i)/i}, indeed all n ≥ 2j with n < i². |
| 4 (R decreasing) | **PROVED** | Step-ratio identity verified on 300 random exact cases; the < 3/4 bound's inequalities all check. Sanity value 0.45833… = 11/24 at (i,j) = (3,5) reproduced — note it is the boundary step j = 5 → 6 = 2i, just outside the strict region; immaterial to the bound. |
| 5 (sliver boundary) | **PROVED + COMPUTED (body); summary gloss FALSE** | Table exact-verified: for i ∈ {256, 257, 300, 500, 1000, 2000}, R ≥ 1 exactly at j = ⌊3i/2⌋+1, ⌊3i/2⌋+2 and fails at +3, giving j* − 3i/2 ∈ {1.5, 2} at those i. The claim "R(i,⌊3i/2⌋+1) ≥ 1 for 257 ≤ i ≤ 600" exact-verified over all 3 ≤ i ≤ 600 (failures exactly i ∈ {4,6,8}). Log-domain j*(10000) = 15003 confirmed (log R = +0.471 at 15003, −0.915 at 15004). Asymptotics (b): bracket H(1/(2γ)) − H(1/γ) < 0 proof correct, so no fixed γ > 3/2 is closed by plain size. **However** the §5 summary row's gloss "j*(i) − 3i/2 ∈ {1.5, 2} (i ≤ 2000, exact)" is **false if read for all i ≤ 2000**: excess 5/2 occurs, e.g. i = 959, j* = 1441 (exact, log R = +0.000102 at the third point). The body of Claim 5 asserts the values only at the tabulated i and is not affected. See §4 for the full corrected distribution. |
| 6 (flank (c) barrier, 666,006 triples) | **COMPUTED (verified in full)** | Full independent recount reproduces **666,006** exactly (40 ≤ i ≤ 60: **64,475**; 61 ≤ i ≤ 170: **601,531**). Showcases re-verified by general Legendre: (512,170,256): the 15 bad primes are exactly as listed, they are all of S∩[i,j], 29 primes of S above j, and **N(170,256) = 515** (Phase-0 N = max{n : C(n,i) < C(2j,2(j−i))}, exact) ≥ n, so inside the reduction interval. (5958,100,180): 10 bad primes exact, **unique** in range (recount = 1), N(100,180) = 486, 60 primes above j. (20350,149,251): 18 bad primes exact, N(149,251) = 609, 92 primes above j. Barrier interpretation is correctly caveated in the file (bulk evidence at i ≤ 170, not a proof for every large i). |
| 7 (plain test fails, flank (b)) | **PROVED + COMPUTED** | g′(a) < 0 ⟺ 8a² − 8a + 1 < 0 algebra verified; bracket minimum H(1/2) − H(1/4) = 0.1308120359…; 0.130812j − log(j+1) > 0 at j = 25 (margin +0.012) and beyond. Instance (100,300,600): log₁₀ ratio = +23.60, exact match. |
| 8 (flank (b) strip via (†) + Table 14) | **PROVED** | See §5 below for the support-exclusion audit. Coefficient recomputed: ½ + (3/2)M₀ + m₀ = **0.500155653**, constant 1 − m₀ = 0.999908361; H(5/24) = **0.5117400734**, margin **0.0115844**; tail (1 + ½log(2j+1))/j < 1.18·10⁻⁸ at j = 10⁹ (file: < 1.2·10⁻⁸ ✓) ≪ margin. All four θ arguments strictly exceed e²⁰ under i > e²⁰ + 1, j > 2i, so the Table 14 row applies. Region certified exactly as stated: 2i < j ≤ (12/5)i, i > e²⁰ + 1, 2j ≤ n < i². |
| 9 (W-refinement fails) | **COMPUTED (verified)** | All five rows reproduced exactly (log₁₀ W − ½log₁₀ C(2j,i)): (100,300): +1.21; (100,400): +15.01; (200,600): +5.26; contrast rows (40,100): −1.16; (60,132): −4.35. Plain-test column also matches (+23.60, +31.58, +47.75). |
| 10 (β-specification) | **PROVED** | Algebra correct and sharp for the method (≤ form is the sharp one; see G4.1 note). β = 0.36 threshold: exp(2c/0.14) = **1,600,320.63**, so i ≥ 1,600,321, exact match. |
| 11 (candidate bound) | **PROVED** | Legendre: each summand ∈ {0,1}, at most ⌊log_p n⌋ of them, so p^{v_p} ≤ n; product over the M(n,i) primes in [i,√n]. |
| 12 (region R_a + band) | **PROVED** | Closing condition 2M log n + 2cj ≤ i log(n/i) correct. Band: √n < i+1 forces M ≤ 1 (only possible prime is i itself); sufficient inequality 4log(i+1) + 4ci < i log i first holds at **i = 70** (fails at 69, both checked); persistence increment lower bound log 70 − 4c − 4/71 = **0.19216** > 0 verified (actual increments ≈ 1.20, so the file's bound is loose but valid). |
| 13 (candidate fails at (100,10⁶)) | **COMPUTED (verified); flank (a) general OPEN** | π(1000) − π(99) = 168 − 25 = **143**; 2M log n = **3951.24** vs i log(n/i) = **921.03**; log C(10⁶,100) = 1017.81 (lgamma); β_cand = **1.941**; admissible β = 0.304–0.353 over 150 < j < 200; overshoot factor 5.5–6.4. All digits match. |

## 3. P-G2 — claim-by-claim

| Claim | Verdict | Verification |
|---|---|---|
| G1.1 (Broadbent Cor. 2.1) | **PROVED** (citation) | Confirmed at primary source (§1); RH-computation dependence stated in the file and confirmed (paper Thm 2, "Büthe, Platt-Trudgian"). |
| G1.2 (Dusart Prop. 5.1, Thm 5.2, π bounds) | **PROVED** (citation) | All confirmed at primary source (§1). |
| G1.3 (Rosser–Schoenfeld status) | **Correct as stated** | Not primary-verified, not used; consistent with primary_sources_c2.md Item 3. |
| G1.4 (wedge K = 55) | **PROVED** | Fraction certification reproduced (§1): e^{4c_B} < 54.598155, e^{4c_D} < 54.604174, both < 55. No x₀ for either bound. Restated wedge equivalent to G1 Claim 2. |
| G2.1(a) (entropy boundary F) | **COMPUTED (verified)** | F(3/2) = 0; F values reproduced to all printed digits: F(1.51) = −0.013764, F(1.55) = −0.066933, F(1.6) = −0.129526, F(1.75) = −0.296235, F(1.9) = −0.438624, F(2) = −0.523248. F′(3/2) = −2 log 2: numeric derivative −1.38629436 vs −2 log 2 = −1.38629436. |
| G2.1(b) (exact classification, i ≤ 2000) | **FALSE** (in detail; qualitative content survives) | See §4. Exact classification: the (*) set is empty for i ∈ {4,6,8} ✓, but has **three** points for 521 values of i (all odd, 959 ≤ i ≤ 1999), not at most two. The file's "two-point case occurs for 1859 of 1998" is the count of size **≥ 2** (1338 + 521 = 1859), mislabeled. Consequently "(*) closes precisely the strip γ ≤ 3/2 + 2/i" is **false**; the correct uniform strip from the data is γ ≤ 3/2 + 3/i. No downstream claim depends on the exact 2/i: G2.2 and G2.4 do not use it, and the conclusions actually drawn (strip width → 0; asymptotically empty in the open strip (3/2,2); agreement with the boundary-family closure j = ⌊3i/2⌋+1) remain true. |
| G2.1(c) (threshold curve α_c) | **COMPUTED (verified, entropy-order)** | α_c values reproduced: 3.054 (1.51), 3.278 (1.55), 3.569 (1.6), 4.526 (1.75), 5.605 (1.9), 6.393 (2); also α_c(2.5) = 11.149, α_c(3) = 17.264, α_c(4) = 33.573 as used in G3.3. The file labels these "at entropy order"; they are not finite-i theorems and are not used as such. |
| G2.2 (flank (c) closed, i ≥ 379) | **PROVED** | Full re-derivation in §6 below. Certified region stated precisely there. One exposition slip: Step 1 writes V = ∏_{i≤p≤j} p where V is in general a sub-product; the inequality actually used, log V ≤ θ(j) − θ(i−1), is correct. |
| G2.3 (barrier, 2,493 triples) | **COMPUTED (verified in full)** | Independent recount reproduces **2,493**; subrange distribution 40 ≤ i ≤ 80 exactly {4:16, 5:79, 6:140, 7:58, 8:68, 9:23} (sum 384); over the full range the bad-count distribution is {4:16, 5:79, 6:140, 7:80, 8:133, 9:268, 10:463, 11:633, 12:324, 13:206, 14:87, 15:56, 16:8}, so the minimum is indeed 4, as claimed. Showcase (482,157,241) re-verified by general Legendre: S∩[157,241] is exactly the 16 listed primes, all bad; rescued only by the **26** primes above j (list 331, 337, …, 479 reproduced exactly); n = 482 = 2j; C(483,157) < C(241,84)² exactly, so n is strictly inside the square-reduction interval. |
| G2.4 (band 257 ≤ i ≤ 378) | **GAP** (correctly self-labeled) | Not closed by either file (G1 closes only its Claim-3 sliver there). The finiteness remark via α_c(2) ≈ 6.4 is entropy-order; per-pair finiteness via the exact square reduction is unaffected. |
| G3.1 (K_Γ wedge extensions) | **PROVED** | K_Γ = ⌈e^{2c_B Γ}⌉; Fraction-certified e^{6c_B} < 403.42884 → K₃ = **404**, e^{8c_B} < 2980.95845 → K₄ = **2981**, reproduced. Chain valid; K_Γ ≥ 2Γ in all cases, so j ≤ n/2 is automatic as claimed. |
| G3.2 (support bound, γ*(i)) | **PROVED** | γ*(i) reproduced by bisection on Ψ: γ*(1000) = **2.0509**, γ*(10⁴) = **2.1072**, γ*(10⁵) = **2.1310**, γ*(10⁷) = **2.1511**; limit root of 2γh(1/(2γ)) − 2c_Bγ + 2 = 0 is γ*_∞ = **2.17178**. Endpoint γ = γ*(i) is included via the strict Dusart lower bound on θ(i−1); immaterial for integer j. Certified region: i ≥ 379, 2i ≤ j ≤ γ*(i)·i, 2j ≤ n < i². |
| G3.3(a) (key-lemma barrier at γ = 2) | **PROVED** (barrier, as stated) | log C(2000,1000) − ½log C(4000,1000) = **+259.7** reproduced (259.712); asymptotic excess  γh(1/γ) − γh(1/(2γ)) = 0.26162 per unit i at γ = 2 consistent. |
| G3.3(b) (support+autogood barrier at γ = 3) | **PROVED** (barrier, as stated) | Exact-θ computation reproduced: log B_allowed = θ(1500) − θ(999) + θ(3000) − θ(2000) = **1498.4** vs threshold ½log C(6000,1000) = **1349.5**; fails by **148.9** nats. At γ = 4, i = 1000 the margin is **+457.5**, also reproduced. |
| G3.3(c) (= summary table's "G3.4") | **COMPUTED (verified)** | At (i,j) = (1000,2500), n = 2j, exact θ: log B_allowed − ½log C(2j,i) = **−24.7** (closes that point), reproduced. Borderline γ** = root of h(1/(2γ)) = 1/2: p = 0.199710, γ** = **2.50363** ≈ 2.504 ✓. (Cosmetic: the summary table numbers this G3.4, the body folds it into G3.3(c).) |
| G4.1 (β-specification) | **PROVED** | Algebra correct. Fine point: the sharp condition is β ≤ 1/2 − c_B j/log C(n,i) (G1 Claim 10 form, using strictness of EEES78); G2's boxed strict < is a valid sufficient form, non-sharp only at exact equality. The sufficient forms via C(n,i) ≥ (n/i)^i are in the correct direction. |
| G4.2 (candidate bound) | **PROVED** | Same Legendre argument as G1 Claim 11; correct. |
| G4.3 (shell u_max) | **COMPUTED (verified at all three i)** | Recomputed with an independent exact sieve (grid step 0.05, j = 2i worst case, as in the file's Appendix D): i = 10⁴: certifies to u = **2.70**, cannot from **3.05**; i = 10⁵: **3.35** / **3.70**; i = 10⁶: **4.00** / **4.35**. Sample values at i = 10⁵, u = 2 reproduced: P = **8392**, 2P log n + 2c_B j = 8.097×10⁵ < i log(n/i) = 1.290×10⁶; at u = 5: 2.077×10⁶ > n·h(i/n) = 1.573×10⁶. Caveat: the "cannot certify" column is evaluated at the worst case j = 2i; the "certifies" column, being at j = 2i, is valid for all j < 2i. Shell is nonempty; u_max(i) = (log i)/4 + O(1) asymptotics consistent with the data. |
| G4.4 (flank (a) beyond shell) | **OPEN** (correctly stated) | The failure exhibited is of the candidate bound n^{π(√n)−π(i−1)}, not of the conjecture. |

---

## 4. The one false claim in detail: G2.1(b) (and the G1 summary gloss)

Exact classification of {(i,j) : 3 ≤ i ≤ 2000, 3i/2 < j < 2i,
C(2j,i) ≥ C(j,i)²}, obtained by logΓ scan with **every** boundary
case re-checked in exact integer arithmetic (the smallest |log R| at
any boundary is 1.02·10⁻⁴, at (959,1441), far above float error, and
all 521 three-point boundaries were exact-verified individually):

| size of (*) set | count | which i |
|---|---|---|
| 0 | 3 | i ∈ {4, 6, 8} |
| 1 | 136 | |
| 2 | 1338 | |
| 3 | **521** | all odd, 959 ≤ i ≤ 1999 |

Total 1998. By G1 Claim 4 (independently proved) the set is always an
initial segment {⌊3i/2⌋+1, …, j*(i)}, so size 3 means
j*(i) = ⌊3i/2⌋+3, i.e. excess j*(i) − 3i/2 = 5/2 for those odd i.
Smallest counterexample to G2.1(b): **i = 959, j ∈ {1439, 1440, 1441}**,
with log R(959,1441) = +0.000102 > 0 (exact). Hence:

- G2.1(b)'s "either empty or an initial segment of size 1 or 2" is FALSE;
- its "two-point case occurs for 1859 of 1998" is FALSE as labeled
  (1859 = 1338 + 521 is the size ≥ 2 count; the two-point count is 1338);
- its "(*) closes precisely the strip γ ≤ 3/2 + 2/i" is FALSE; the
  correct uniform bound over the classified range is γ ≤ 3/2 + 3/i
  (size-3 odd i give γ up to 3/2 + 5/(2i));
- G1's §5 summary gloss "j*(i) − 3i/2 ∈ {1.5, 2} (i ≤ 2000, exact)"
  is likewise FALSE as a statement about all i ≤ 2000 (excess 5/2
  occurs); G1 Claim 5's body, which tabulates only six values of i
  (all with excess ∈ {1.5, 2}, all exact-verified here) and separately
  notes excess 3 at i = 10000, is not affected. G1's own part (b)
  already allows excess ∈ {1.5, 2, 3} "in the computed range", which
  the corrected distribution confirms (adding 5/2).

**Propagation:** none into any proof. G2.2, G2.4, G3.x, G4.x never
invoke the 2/i strip or the size ≤ 2 classification; G1 Claims 3–4
(the proved initial-segment structure) are the load-bearing statements
and they are correct. The only repairs needed are the two summary
sentences identified above.

## 5. G1 Claim 8 audit: the support exclusion (†)

The task brief asked specifically whether supp V ⊆ [i, j/2] ∪ (d, j]
is sound against S10 §4–§5, and what happens on (d, j/2].

- S10 Theorem S10, item 3, states: if j > 2i and p ∈ S(n,i) ∩ (j/2, d],
  then A_p ≥ 1 (a window of length d ≥ p meets a multiple of p) while
  B_p ≤ 1 (Theorem 3 applies since p ∈ (j/2, j]), so
  v_p(C(n,j)) ≥ e_p ≥ 1: p is automatically good. In a counterexample
  every p ∈ S(n,i) is bad, hence S(n,i) ∩ (j/2, d] = ∅. This is
  exactly the exclusion G1 imports, and it is sound.
- The interval (d, j/2] raised in the brief is **empty in this regime**:
  d > j/2 ⟺ j − i > j/2 ⟺ j > 2i, which is the standing hypothesis.
  There is no missing case.
- Primes in [i, j/2] are **not** excluded, and G1 does not exclude
  them: they are charged to the bound through θ(j/2) − θ(i−1). S10
  Theorem 5 shows such primes *can* be bad only under its multi-scale
  condition (†) with e_p ≤ ⌊log_p j⌋; in the present regime
  (n < i², so p ≥ i > √n) S4 gives e_p = 1 automatically, and Claim 8
  needs no more than the support bound plus squarefreeness — the
  multi-scale condition is not load-bearing here, and G1's text says
  so correctly.
- The mechanism is as the file's remark states: the two surviving
  intervals have total length (j/2 − i) + (j − d) = j/2, so log V ≲ j/2
  (coefficient 0.500155653 with Table 14 errors) against the entropy
  term j·H(1/(2γ)) ≥ j·H(5/24) = 0.51174j. The method's ceiling is
  γ** = 2.50363… (root of H(1/(2γ)) = 1/2, independently computed),
  matching both files' remarks; 12/5 = 2.4 is a clean value inside it.

**Claim 8 is PROVED as stated.**

## 6. G2.2 re-derivation and seam probe

Re-derived from scratch. Let (n,i,j) be a counterexample with
i ≥ 379, 3i/2 < j < 2i, 2j ≤ n < i²; (n,i) is not an EEES78 exception
(n ≥ 2j > 3i ≥ 1137 > 56).

1. **Support bound.** n < i² gives p ≥ i > √n for every prime factor
   of V, so V is a squarefree sub-product of ∏_{i≤p≤j} p (support in
   [i,j] by S4 Lemma 1), hence log V ≤ θ(j) − θ(i−1) ≤ c_B·j −
   (i−1)(1 − ε(i)), using Cor. 2.1 above and Dusart Thm 5.2 with
   (k, η_k, x_k) = (2, 3.965, 2) below: θ(i−1) ≥ (i−1)(1 − ε(i)),
   ε(i) = 3.965/log²(i−1), valid for i−1 ≥ 2.
2. **Binomial lower bound.** C(n,i) ≥ e^{n·h(i/n)}/(n+1): the term
   C(n,i)(i/n)^i(1−i/n)^{n−i} is the largest of the n+1 binomial
   terms (mode of Bin(n, i/n) is i since (n+1)i/n ∈ [i, i+1)), hence
   ≥ 1/(n+1). Sound.
3. **Reduction.** n·h(i/n) − log(n+1) is increasing in n for n ≥ 2j
   (derivative −log(1 − i/n) − 1/(n+1) > 0, as −log(1−i/n) ≥ i/n >
   1/(n+1) for i ≥ 2), so the minimum is at n = 2j. Dividing by i,
   the needed inequality 2[θ(j) − θ(i−1)] < log C(n,i) is implied by
   Ψ(γ,i) > 0 with
   Ψ(γ,i) = 2γh(1/(2γ)) − 2c_Bγ + 2(1−ε(i))(1 − 1/i) − log(2γi+1)/i,
   exactly as defined in the file.
4. **Monotonicities.** ∂/∂γ[γh(1/(2γ))] = −log(1 − 1/(2γ)) ≤ log(3/2)
   (identity h(u) − uh′(u) = −log(1−u) at u = 1/(2γ)), so
   Ψ_γ ≤ 2 log(3/2) − 2c_B − 2/(2γi+1) < 0 on [3/2, 3]; independently,
   the maximum numeric derivative of Ψ in γ over [3/2,3] ×
   {379, 1000, 10⁵} is −1.189 < 0. Ψ(2, i) is increasing in i
   (ε decreasing, (1 − 1/i) increasing, log(4i+1)/i decreasing);
   numerically no decrease on 4 ≤ i ≤ 1999.
5. **Threshold values (recomputed):** Ψ(2,378) = **−0.0000626**,
   Ψ(2,379) = **+0.0001945**, Ψ(2,1000) = 0.07298, Ψ(2,10⁴) = 0.15461,
   Ψ(3/2,1000) = 0.73347 — all matching the file. Hence Ψ(γ,i) ≥
   Ψ(2,i) ≥ Ψ(2,379) > 0 for 3/2 < γ < 2, i ≥ 379, and Step 4 of the
   file (C(n,i) > V² contradicts EEES78) follows.

**Seam probe (own computation).** At i = 378 the root of Ψ(·,378) = 0
is γ*(378) = **1.999956**: the support bound at i = 378 still closes
every γ ≤ 1.999956 but not γ ∈ (1.999956, 2) (e.g. Ψ(1.999,379) =
+0.00162 > 0 while Ψ(2,378) < 0). So i₀ = 379 is exactly the first
integer at which the *whole* strip γ ∈ (3/2, 2) is closed; the
threshold is sharp for this method, not an artifact of rounding.

**Certified region of G2.2, precisely:**
{i ≥ 379, 3i/2 < j < 2i, 2j ≤ n < i²} — **all** α = n/i (necessarily
3 < 2γ ≤ α < i). In particular it strictly contains flank (c)
(n ≤ 256i) for i ≥ 379, and it also contains the K = 55 wedge region
for i ≥ 379 (overlap, no conflict: both are no-counterexample
statements). The argument uses no bad-configuration input, as the
file's remark states.

---

## 7. Certified bottom line

No counterexample exists in any of the following regions (constants
as verified above; all regions also assume the standing campaign
inputs EEES78, the key lemma, and the S4/S10 anatomy, which were
taken as given per the task):

1. **Wedge, K = 55** (G1 Claim 2 = G2 G1.4): 55i < n < i²,
   3i/2 < j < 2i (region forces i ≥ 56). θ input: Broadbent et al.
   Cor. 2.1, c_B = 1 + 1.93378·10⁻⁸, all x ≥ 0, no x₀ adjustment;
   Dusart Prop. 5.1 (c_D = 1 + 1/36260) independently gives the same K.
2. **Flank (c) and all-α extension, i ≥ 379** (G2.2):
   3i/2 < j < 2i, 2j ≤ n < i². Subsumes region 1 for i ≥ 379 and
   flank (c) (n ≤ 256i) for i ≥ 379.
3. **Flank (c) sliver, all i > 256** (G1 Claims 3–5, corrected per §4):
   pairs (i,j) with C(2j,i) ≥ C(j,i)² — an initial segment
   j ≤ j*(i) with j*(i) − 3i/2 ∈ {3/2, 2, 5/2, 3} in the classified
   range — closed for all 2j ≤ n < i².
4. **Flank (b), large n** (G2 G3.1): 2i ≤ j ≤ Γi, n > K_Γ·i, with
   K₂ = 55, K₃ = 404, K₄ = 2981 (K_Γ = ⌈e^{2c_B Γ}⌉ in general).
5. **Flank (b), all n, explicit-θ strip** (G2 G3.2): i ≥ 379,
   2i ≤ j ≤ γ*(i)·i, 2j ≤ n < i², with γ*(1000) = 2.0509,
   γ*(10⁴) = 2.1072, γ*(10⁵) = 2.1310, γ*(i) ↑ γ*_∞ = 2.17178.
6. **Flank (b), huge-i strip via Table 14** (G1 Claim 8):
   2i < j ≤ (12/5)i, i > e²⁰ + 1, 2j ≤ n < i². (Regions 5 and 6 are
   incomparable: 5 has threshold i ≥ 379 but γ-reach ≤ 2.17178;
   6 reaches γ = 2.4 only for i > e²⁰. The support method's absolute
   ceiling is γ** = 2.50363…, and exact-θ pointwise computations go
   beyond γ*(i), e.g. (1000, 2500) at n = 2j closes by 24.7 nats.)
7. **Flank (a) shells** (G1 Claim 12; G2 G4.3): the exact region
   R_a = {n ≥ i², 3i/2 < j < 2i, 2M(n,i) log n + 2cj ≤ i log(n/i)},
   including the band i ≥ 70, i² ≤ n < (i+1)²; and the candidate-bound
   shell i² ≤ n ≤ u_max(i)²·i² with u_max = 2.70, 3.35, 4.00 at
   i = 10⁴, 10⁵, 10⁶ (certified at worst case j = 2i).

**Still open (both files agree, verified as not closed):**
flank (c) for 257 ≤ i ≤ 378 beyond the Claim-3 sliver (G2.4, GAP);
flank (b) for γ > γ*(i) at uniform-explicit level, and for
γ > γ** ≈ 2.504 at n = 2j the size/support/autogood methods are
barred by the exact barrier of G3.3(b) (margin +148.9 nats at
γ = 3, i = 1000, growing); flank (b) for 2 < γ ≤ 12/5 at
i ≤ e²⁰ is closed only where region 5 applies (γ ≤ γ*(i));
flank (a) for n ≥ i² outside R_a / the G4.3 shell (the needed input
is exactly a bound V^≤ ≤ C(n,i)^β with β ≤ 1/2 − cj/log C(n,i);
the candidate n^{M(n,i)} provably does not supply it in general).

**Errors found (complete list):**
1. **G2.1(b) is FALSE** in its exact classification (three-point
   cases exist: 521 of them, smallest i = 959) and in its derived
   strip γ ≤ 3/2 + 2/i; its "1859 two-point" count is the size ≥ 2
   count mislabeled. No downstream proof is affected (§4).
2. **G1 §5 summary gloss** on Claim 5 ("excess ∈ {1.5, 2}, i ≤ 2000")
   overstates Claim 5's body in the same way (excess 5/2 occurs).
   Claim 5's body is proved/computed as written.
3. Non-fatal slips: G2.2 Step 1 writes V as an equality where a
   sub-product (≤) is meant (the used inequality is correct);
   G2's summary table numbers G3.3(c) as "G3.4"; G4.1's boxed
   condition uses < where ≤ is the sharp form (G1 Claim 10);
   G1 Claim 4's sanity maximum is attained at a boundary step
   (j = 5 → 6 = 2i at i = 3).

Everything else in both files — every numbered claim, every printed
constant, both bulk barrier counts (666,006 and 2,493) with their
showcases and N-values, the Ψ threshold i₀ = 379, the γ*(i) table,
the γ = 3 barrier numerics (1498.4 vs 1349.5), the W-table, and the
flank-(a) shell table — was independently reproduced and stands as
labeled by the provers, with the single exception of G2.1(b) above.

*Verification performed 2026-10-29 (America/New_York). Primary sources:
arXiv:2002.11068v2 PDF (Cor. 2.1, Table 8 reference, Table 14) and
arXiv:1002.0442 PDF (Prop. 5.1, Thm 5.2) fetched via browser.open in
this session. All other computations are the verifier's own
(Python stdlib, exact arithmetic as described).*
