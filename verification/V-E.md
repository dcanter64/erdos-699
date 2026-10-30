# Verification V-E — Cluster E (S7 strengthened EEES exponent), Cycle 2

**Scope.** Independent verification of `proofs/P-E1.md` and `proofs/P-E2.md`
(both claiming Lemma S7(2.0) of `strategies/S7.md` §§3–5), including:
line-by-line re-derivation of both assembled bounds; adjudication of the
competing parameters; primary-source checking of every cited explicit
estimate (web, `browser.search`/`browser.open`); an independent recomputation
of the empirical frontier test (own code, Legendre exponents, exact integer
threshold checks); and a check of both closure steps. All computations are
Python stdlib only, exact (`Fraction` / integer) arithmetic where claimed.
Runtimes: empirical recomputation 50 s, characterisation brute-force 30 s,
exact-rational register checks < 1 s.

**Headline result.** Both main $\theta_u$ bounds are sound modulo
correctly-stated published explicit estimates. E2's parameters are the
stronger ones on every axis and are **certified** (with one provenance
defect in E2's citation of its $\vartheta$ bound, §2, which does not affect
validity). E1's main theorem is also sound at its weaker parameters; E1's
*closure* proof has exactly one defective step (Lemma E1.10's monotonicity
argument, a factor-of-2 error), localised to Case B of Theorem E1.9 — the
statement is true and a corrected proof is supplied in §3, but as filed it
is a **GAP**, and it is not softened below.

---

## 1. Method for the analytic re-derivation

Every displayed bound in both files was re-derived from its stated inputs,
not merely re-evaluated. The two R3-type characterisations were additionally
brute-force validated against direct Legendre exponents:

- **E1.5 characterisation:** 157,584 triples $(n,i,p)$, $27 \le i < 120$,
  $4i \le n \le 13i/2$, $i/2 < p < i$: **0 mismatches** ($e_p \in \{0,1\}$
  always; $e_p = 1 \iff p \in (A_q, B_q]$, $q = \lfloor n/p \rfloor$).
- **E2.7 characterisation:** 3,092,968 triples $(n,i,p)$, $164 \le i < 260$,
  $2i \le n \le 13i/2$, $i/5 < p < i$: **0 mismatches** ($e_p \le 1$ always;
  $e_p = 1 \iff p \in J_{m,q}$, $m = \lfloor i/p \rfloor$, $q = \lfloor n/p
  \rfloor$).

All numerical registers in both files were recomputed independently;
every value matched at the printed precision except the two immaterial
rounding differences noted in §3 (E1 §8) and §4 (E2 §6.1).

---

## 2. Citation verification (task item 3)

`verification/primary_sources_c2.md` covers **none** of the four Dusart
bounds used by Cluster E (its items are Dusart 2018 Cor. 5.5, Axler 2017
Thm. 4.1, and the Rosser–Schoenfeld $\theta(x) < 1.1x$ remark), so it
neither verifies nor contradicts any citation here. P-G2's prover did
primary-read Dusart arXiv:1002.0442 and recorded Prop. 5.1 and Thm. 5.2's
form $|\theta(x) - x| < \eta_k x/\log^k x$ with rows
$(k,\eta_k,x_k) = (2, 3.965, 2)$, $(2, 0.2, 3594641)$, plus $\pi$ bounds
$\pi(x) \le \frac{x}{\log x}(1 + \frac{1.2762}{\log x})$ ($x > 1$) and
$\pi(x) \ge \frac{x}{\log x}(1 + \frac{1}{\log x})$ ($x \ge 599$). Those
rows are consistent with, but do not by themselves sight, the exact rows
E1/E2 cite. This session's own checks:

| Citation | As cited | Finding | Status |
|---|---|---|---|
| E1 D-$\pi$ | $\pi(x) \le \frac{x}{\log x}(1 + \frac1{\log x} + \frac{2.51}{\log^2 x})$, $x \ge 355991$ (Dusart, via survey Thm. 2.1) | Exact statement, constants $(1, 1, 2.51)$ and threshold $355991$ sighted in multiple independent secondary sources quoting Dusart (Wikipedia "Prime number theorem" §Non-asymptotic bounds; a Twente thesis quoting Dusart; Glasby–Praeger–Unger citing "Dusart [3, p. 55]"). Dusart's own page not opened this session. | **SECONDARY ONLY — correctly stated** |
| E1 D-$\theta$ | $\lvert\theta(x) - x\rvert < x/\log^3 x$, $x \ge 89967803$ (Dusart 2010, Thm. 5.2) | Exact statement with threshold and the label "[2, Theorem 5.2]" sighted in Kourbatov's paper on geometric means of primes (secondary). Independently, Broadbent–Kadiri–Lumley–Ng–Wilk Cor. 11.2 restates Dusart's $\theta$ table with the row $(k, M_k, X_0) = (3, 1, 89\,967\,803)$ exactly; P-G2's primary read of arXiv:1002.0442 confirms Thm. 5.2 is precisely this $\eta_k$ table. The $k=3$ row itself was not sighted in Dusart's own text this session. | **SECONDARY ONLY — correctly stated** (theorem-number attribution corroborated) |
| E1 Input R / E2 (Robbins) | $m! = \sqrt{2\pi m}(m/e)^m e^{r_m}$, $\frac{1}{12m+1} < r_m < \frac{1}{12m}$ (Robbins 1955) | The standard explicit Stirling form, identical to the one used in P-C2 Lemma 2.6. Not web-checked this session; no discrepancy found anywhere. | **SECONDARY ONLY — correctly stated** (standard) |
| E2 Input E2.2 | $\pi(x) < \frac{x}{\log x - 1.1}$, $x \ge 60184$ (Dusart 2010) | Exact statement sighted with the attribution "Later in 2010, Dusart proved … $\pi(x) < x/(\log x - 1.1)$ for $x \ge 60184$" (Wikipedia PNT, ref. to arXiv:1002.0442), and restated as a theorem of Dusart in Paz's paper (Thm. 1.2 there) and in Axler's 2014 $\pi$-bounds paper ("In 2010, he proved…"). | **SECONDARY ONLY — correctly stated** |
| E2 Input E2.3 | $\lvert\vartheta(x) - x\rvert \le 0.006788\,x/\log x$, $x \ge 10544111$ ("Dusart 2010, same paper") | The **statement** (constant $0.006788$, threshold $10\,544\,111$) is exact and sighted in several secondaries: the Ramanujan-primes paper's Lemma 2.1(b) ("due to Dusart [1, p. 54]") and Trudgian's $\sigma^*$ paper. But the **source is Dusart 1999**, "Inégalités explicites pour $\psi(X), \theta(X), \pi(X)$ et les nombres premiers", *C. R. Math. Acad. Sci. Soc. R. Can.* 21(2):53–59 (Trudgian's ref. [4], confirmed from his bibliography as sighted this session; the citing lemma's "p. 54" is that paper's second page). Dusart 2010's Thm. 5.2 table contains **no** $(k{=}1,\ 0.006788,\ 10544111)$ row (its $k=1$ rows, per P-G2 and Broadbent et al. Cor. 11.2, are $1.2323$ at $x_0 = 2$ and $0.001$ at $x_0 = 908\,994\,923$). | **MISQUOTED attribution** (1999, not 2010); **statement SECONDARY ONLY — correctly stated** |

**Survival on secondary-only citations.** Campaign standard: a proof
modulo a correctly-stated published theorem is acceptable; a misquoted
constant or range is a GAP. Four of the five citations are correctly
stated (constant and range exact) and survive as "PROVED modulo cited
published estimates". E2.3's constant and range are also exact, and the
bound is a genuine published theorem — only its provenance pointer
("Dusart 2010") is wrong. E2.3 **as a citation claim** is therefore a GAP
(and its self-label "PROVED as a citation" is not sustained), but the
defect is bibliographic, not mathematical: downstream, only the
inequality is used, so E2's theorems remain PROVED modulo the bound
under its correct attribution (Dusart 1999). Anyone citing E2 must fix
the attribution; nobody needs to redo the mathematics.

---

## 3. P-E1: claim-by-claim

| Claim | Verdict | Reason (re-derivation summary) |
|---|---|---|
| Input D-$\pi$ | SECONDARY ONLY, correctly stated | §2. |
| Input D-$\theta$ | SECONDARY ONLY, correctly stated | §2. |
| Input R (Robbins) | SECONDARY ONLY, correctly stated | §2. |
| Lemma E1.1 (Erdős) | **PROVED** | Legendre summands in $\{0,1\}$, vanishing for $p^e > n$; $e_p \le \log n/\log p$. Re-derived. |
| Lemma E1.2 (binomial lower bound) | **PROVED** (mod R) | Stirling subtraction re-derived: main term $i f(\alpha)$, sqrt term $\ge -\frac12\log(2\pi i)$, remainder $> -1/(12i) - 1/(12(n-i)) \ge -1/6$. |
| Lemma E1.3 (cap $N(i,2i) < 13i/2$) | **PROVED** (mod R) | $\binom{4i}{2i} \le 2^{4i}$; $f(13/2) = 2.790600$, $4\log 2 = 2.772589$, margin $0.018011$ per unit $i$ (recomputed: $0.0180109$); correction/i₀ $= 5.3\times10^{-8}$ (recomputed $5.32\times10^{-8}$), and the correction function is decreasing (derivative $< 0$ for all $i \ge 1$). |
| Lemma E1.4 (R1+R2, $p \le i/2$) | **PROVED** (mod D-$\pi$) | $\sum e_p \log p \le \pi(i/2)\log n$; $B_2$ formula re-derived ($\log n \le L + \log 2\alpha_{\max}$); $B_2$ decreasing in $L$ factor-by-factor. Values recomputed exactly as printed: $B_2(4) = 0.590767$, $B_2(5) = 0.597197$, $B_2(13/2) = 0.604758$. The merge of R1 into R2 (no separate $\pi(\sqrt i)$ term) is valid: E1.1 applies to all $p \le i/2$. $p = i$ correctly excluded ($p=i$ belongs to $v$). |
| Lemma E1.5 (R3 characterisation) | **PROVED** | $v_p(i!) = 1$; $t_e = 0$ for $e \ge 2$ because $p^2 > i^2/4 > 13i/2 \ge n$ iff $i > 26$ — this discharges both the $p^2$-multiple subcase and $e_p \ge 2$ (the latter would need $t_1 \ge 2$, i.e. $M_p \ge 3$, impossible since 3 multiples span $\ge 2p > i > i-1$). The interval equivalence is sound: $p > (n-i)/(q-1)$ forces $\lfloor (n-i)/p \rfloor \le q-2$, and the a priori bound $M_p \le 2$ upgrades this to $M_p = 2$ without needing an explicit upper bound from $\lfloor (n-i)/p \rfloor \ge q-2$. $q = \lfloor n/p \rfloor \in \{4,\dots,12\}$ from $n/p \in (\alpha, 2\alpha) \subset (4,13)$. Brute-force: 0/157,584 mismatches (§1). |
| Lemma E1.6 (total length $\le 1/5$) | **PROVED** | Kink analysis verified: the three lower terms $\alpha/(q+1)$, $(\alpha-1)/(q-1)$, $1/2$ pairwise agree **only** at $\alpha = (q+1)/2$; the upper terms agree only at $\alpha = q$; $0$/positive switches occur only at $\alpha \in \{q/2, q, q+1, (q+1)/2\}$ — all on the half-integer grid, so $L$ is linear on each $[m/2, (m+1)/2]$. All eight endpoint values recomputed in exact `Fraction` arithmetic and match E1's list verbatim ($11/60$, $1/5$, $79/420$, $331/1680$, $479/2520$, $493/2520$, $5297/27720$, $2701/13860$); max $= 1/5$ at $\alpha = 7/2$. Exact midpoint test confirms linearity on all seven half-intervals. (Expositional note, not a defect in the applied range: the sum is over the $q$ occurring in E1.5, $q \ge 3$ in the extended range; a $q = 1$ term would be undefined but never occurs.) |
| Lemma E1.7 (R3 bound) | **PROVED** (mod D-$\theta$) | $\theta(B_q) - \theta(A_q) \le (B_q - A_q) + 2i/L^3$ per $q$: each endpoint error $x/\log^3 x \le i/L^3$ since $x \le i$ and $\log x \ge L$; endpoints satisfy $i/2 \le A_q < B_q \le i$, and $i/2 \ge 10^8 \ge 89\,967\,803$, so D-$\theta$ applies at both ends. Error count: "at most nine $q$" is the union over $\alpha \in [4, 13/2]$; for fixed $\alpha$ at most 7 occur — using 9 is conservative and valid, including for empty intervals (the $\theta$-difference inequality holds regardless of interval order). $18/L^3 = 0.002880$ recomputed; total $0.20288\,i$ ✓; decreasing in $i$ ✓. |
| Lemma E1.7b (R3 on $[3,4]$) | **PROVED** (mod D-$\theta$) | Same characterisation (only $i > 26$, $n \le 13i/2$ used); $q \in \{3,\dots,7\}$, five values, error $10/L^3 = 0.001600$; total $0.20160\,i$ ✓. |
| **Theorem E1.8 (S7(2.0), $i_0 = 2\times10^8$, $\delta = 0.004$)** | **PROVED** (mod D-$\pi$, D-$\theta$, R) | Both bands re-derived. $[4,5]$: numerator $0.597197 + 0.202880 = 0.800077$, ratio $0.800077/2.249341 = 0.355694$ (recomputed) $\le 0.356$ ✓. $[5, 13/2]$: $0.807638/2.502012 = 0.322795$ ✓. Monotonicity in $i$: numerator bounds decreasing (E1.4, E1.7), denominator correction per unit $i$ decreasing — the $i = i_0$ evaluation bounds all $i \ge i_0$ ✓. $\delta = 0.36 - 0.356 = 0.004$ ✓. |
| Lemma E1.10 ($\varphi_{\mathrm{req}}$ bound) | **GAP** (statement true; proof defective as written) | The direct bound at fixed $c$ is sound: numerator $\le ci\log 2$, denominator $\ge i f(2c) - \frac12\log(2\pi i) - \frac16$ via E1.2, giving $\varphi_{\mathrm{req}} \le \Phi(c) + 10^{-6}$ (the $10^{-6}$ absorbs the true relative correction $\le 2.8\times10^{-8}$); $\Phi(7/4) = 0.579293$, $\Phi(2) = 0.616311$ recomputed ✓. **But the monotonicity proof contains a factor-of-2 error:** $\frac{d}{dc}\log\Phi(c) = \frac1c - \frac{2f'(2c)}{f(2c)}$, so positivity is equivalent to $f(\alpha) > \alpha f'(\alpha)$ ($\alpha = 2c$), **not** to the file's $f(\alpha) > \frac{\alpha}{2} f'(\alpha) =: h(\alpha)$. The proved comparison $f > h$ is therefore insufficient, and the "iff" as printed is false. **Correction (verified here):** with $H(\alpha) := \alpha\log\frac{\alpha}{\alpha-1} = \alpha f'(\alpha)$, $H'(\alpha) = \log(1 + \frac{1}{\alpha-1}) - \frac{1}{\alpha-1} < 0$, so $H$ is decreasing, $H(\alpha) \le H(3) = 3\log\frac32 = 1.216395 < 1.909543 = f(3) \le f(\alpha)$ on $[3,4]$; numerically $\min_{[3,4]} (f - \alpha f') = 0.6931 > 0$ (at $\alpha = 3$). Hence $\Phi$ **is** increasing and the lemma's statement holds — but E1's file does not prove it. The $c = 2$ endpoint bound (used in E1.9 Case A) does not use monotonicity and is unaffected. |
| Lemma E1.11 ($\theta_u$ on $[3,4]$) | **PROVED** (mod D-$\pi$, D-$\theta$, R) | Numerator $0.590767 + 0.201600 = 0.792367$; ratios recomputed: $0.792367/1.909542 = 0.414951 \le 0.4150$ ✓, $0.792367/2.093944 = 0.378409 \le 0.3785$ ✓. Stirling correction ($\sim 10^{-8}$ in the ratio) is far inside both margins. |
| **Theorem E1.9 (closure, $j \le 2i$, $i \ge i_0$)** | **GAP** as written (Case A PROVED; Case B inherits the E1.10 gap) | Preliminaries verified: $N(i,j) \le N(i,2i)$ since $\binom{2j}{2(j-i)} = \binom{2j}{2i}$ is increasing in $j$ (successive ratio $> 1$ ✓); $n \ge 2j > 3i$; $\binom{j}{j-i} \le \binom{2i}{i}$ via fixed-lower-index then central maximality ✓. **Case A** ($n \ge 4i$, incl. $j = 2i$): sound and self-contained — E1.8 gives $v \ge \binom{4i}{i}^{0.644}$, the direct $c=2$ bound gives $\binom{2i}{i} \le \binom{4i}{i}^{0.61632}$, margin $0.0277$ ✓. **Case B** ($3i < n < 4i$): the coupling $c = j/i \le n/(2i) = \alpha/2$ (from $j \le n/2$) is **sound**, the band pairing is correct ($\alpha \in (3, 7/2] \Rightarrow c \le 7/4$, $\theta_u \le 0.4150$, exponent $0.5850$ vs $\varphi_{\mathrm{req}} \le 0.57930$, margin $0.0057$; $\alpha \in (7/2, 4) \Rightarrow \theta_u \le 0.3785$, exponent $0.6215$ vs $0.61632$, margin $0.0052$ — arithmetic all recomputed ✓), and $v = \binom{n}{i}^{1-\theta_u} \ge \binom{2j}{i}^{1-\theta_u}$ from $n \ge 2j$ is valid. **But** both subcases bound $\varphi_{\mathrm{req}}(i,j)$ for $c < 2$ via $\Phi$'s monotonicity, whose proof is the defective step of E1.10. With the correction in the E1.10 row substituted, Case B closes; as filed, it does not. Consequently E1's headline sentence "this closes $j \le 2i$ for all $i \ge i_0$" is **not** sustained by the file as written (it is sustained after the one-step repair). |
| §7 computation | **PROVED** (as a computation) | Independently recomputed — see §5. All headline values confirmed, several to all printed digits. |
| §8 barrier claims | **PROVED** (in substance) | Rosser–Schoenfeld substitution recomputed: numerator $0.9089$, ratio $0.4041 > 0.36$ (E1 prints $0.9086$ / $0.4039$; the $3\times10^{-4}$ intermediate difference is rounding, the failure-by-$\approx 0.044$ conclusion is exact in substance). Weak-$\theta$ variant: error $18 \cdot 3.965/L^2 = 0.2103$ recomputed ✓ (the $3.965$ form is the $(k{=}2)$ row of Dusart Thm. 5.2, primary-read in P-G2). |

No claim in P-E1 is FALSE as a mathematical statement. The file's one
false sub-assertion is E1.10's printed "iff" (the $\frac{\alpha}{2}$
condition), which is why E1.10/E1.9 are GAP and not PROVED.

---

## 4. P-E2: claim-by-claim

| Claim | Verdict | Reason (re-derivation summary) |
|---|---|---|
| Lemma E2.1 (entropy, error $\le \log N$) | **PROVED** (mod Robbins) | Error decomposition re-derived: $\frac{N}{K(N-K)} = \frac1K + \frac1{N-K} \in [4/N, 2]$, log term in $[-\frac12\log N - 0.226, -0.572] \subset [-\frac12\log N - 0.226, 0]$; $\rho$-difference in $(-1/6, 1/12)$; hence $|E| \le \frac12\log N + 0.393 \le \log N$ for $N \ge 10$ ✓. |
| Input E2.2 (Dusart $\pi$) | SECONDARY ONLY, correctly stated | §2. Its self-label "PROVED as a citation" overstates the epistemic status (it is a citation, verified at secondary level this session), but the content is exact. |
| Input E2.3 (Dusart $\vartheta$) | **GAP** as cited (MISQUOTED attribution); statement correctly stated | §2: bound is Dusart **1999**, not "Dusart 2010, same paper". Non-fatal downstream — see the E2.9 row. |
| Lemma E2.4 (cap $\alpha < 13/2$) | **PROVED** | Via E2.1: $\log\binom{n_0}{i} - \log\binom{4i}{2i} \ge 0.0180109\,i - \log n_0 - \log 4i > 0$ at $i \ge 1.2\times10^8$ ($2\,161\,308 - 40.5$, recomputed) and increasing in $i$ (increment of the linear term $0.018$ dominates the logarithmic increments $< 10^{-7}$). General $j \le 2i$: $\binom{2j}{2(j-i)} = \binom{2j}{2i}$ strictly increasing in $j$ ✓, so $N(i,j) \le N(i,2i)$. |
| Lemma E2.5 (denominator) | **PROVED** | Entropy main term is exactly $i f(\alpha)$; error $\ge -\log n \ge -\log(6.5 i)$; $\log(6.5 i)/i = 6.5 \cdot \frac{\log(6.5 i)}{6.5 i}$ decreasing in $i$ ✓. |
| Lemma E2.6 (Erdős) | **PROVED** | Same argument as E1.1. |
| Lemma E2.7 (generalised carry lemma) | **PROVED** | (a) $p^2 > i^2/25 > 13i/2 \ge n$ iff $i > 325/2$ ✓; Legendre terms $e \ge 2$ vanish; $v_p(i!) = \lfloor i/p \rfloor = m$; $e_p \le 1$ by the span argument ($m+2$ multiples span $(m+1)p > (m+1)\frac{i}{m+1} = i$, but block points span $< i$). This discharges the $p^2$ subcase and **all** $e_p \ge 2$ behaviour in $u_>$ — there is no missing subcase. (b) $J_{m,q}$ characterisation re-derived: $e_p = 1$ ⇒ the $m+1$ block multiples are $(q-m)p, \dots, qp$, giving $(q-m)p > n-i$, $qp \le n$; nonemptiness ⟺ $q > m\alpha$; $q < (m+1)\alpha$ from $p > i/(m+1)$ ✓. (c) $m = 1$ recovers S7 Lemma B with the $p^2$ alternative vacuous for $i > 26$ ✓. (d) $p = i$ excluded by definition, and every $J_{m,q}$ has $n/q < i$ (since $q > m\alpha \ge \alpha$), so the overcounting sums never charge it ✓. Brute-force: 0/3,092,968 mismatches (§1). |
| Lemma E2.8 ($\sup L$) | **PROVED** (exact computation, independently reproduced) | On a cell with constant active set each summand is affine with slope $-m/(q(q-m)) < 0$, so $L$ is strictly decreasing there; the right-limit formula at a critical $\alpha_0$ (enlarged active set $\{m\alpha_0 \le q \le (m+1)\alpha_0\}$; $q = m\alpha_0$ terms contribute $0$, $q = (m+1)\alpha_0$ terms contribute their full $\alpha_0$ value) is correct, and $L(\alpha_0) \le L(\alpha_0^+)$. Independent exact `Fraction` enumeration reproduces all three suprema **exactly**: $\frac{11797349}{25865840} = 0.4560977$ at $\alpha_0 = 4$; $\frac{11394421}{24504480} = 0.4649934$ at $\alpha_0 = 7/2$; $\frac{182701}{360360} = 0.5069958$ at $\alpha_0 = 3$; second-largest $0.428433$ at $\alpha_0 = 9/2$ ✓ as printed. Count note (immaterial): E2's "26/31/36 critical points" counts the closed range including $\alpha_0 = 13/2$; on the half-open ranges the counts are 25/30/35. The suprema are unaffected. |
| Lemma E2.9 ($\log u_>$ bound) | **PROVED** (mod the E2.3 inequality, under its correct attribution) | Overcounting direction valid (each $e_p = 1$ prime lies in its own $J_{m,q}$; all terms $\ge 0$); $\sum_{p \in J} \log p = \vartheta(n/q) - \vartheta((n-i)/(q-m))$ exact. Endpoint applicability: both endpoints $\ge (n-i)/(q-m) \ge (\alpha_{\min}-1)i/31$ ($q - m \le 31$ since $q < (m+1)\alpha < 32.5$), which is the lemma's stated sufficient condition. Per-interval error $\le (b-a) + 0.006788 \cdot 2b/\log a$ (using $b/\log b \le b/\log a$, $a/\log a \le b/\log a$) ✓. Error sum: for fixed $m$, admissible $q$ lie in an interval of length $\alpha < 6.5$, hence at most 7 integers, each $1/q < 1/(m\alpha_{\min})$; $S(\alpha_{\min}) = \frac{7}{\alpha_{\min}} \cdot \frac{25}{12}$ ✓. $\sum |J_{m,q}| = i L(\alpha)$ by the §4 identity $\frac{n}{q} - \frac{n-i}{q-m} = i\frac{q - m\alpha}{q(q-m)}$ (re-derived) ✓. |
| Lemma E2.9b ($\log u_\le$ bound) | **PROVED** (mod E2.2) | $\log u_\le \le \pi(i/5)\log n$; the displayed ratio is decreasing in $i$ (derivative $-(a+b)/(L-b)^2 < 0$) ✓. |
| **Theorem E2.10 (S7(2.0), $i_0 = 1.2\times10^8$, $\delta = 0.0338$)** | **PROVED** (mod E2.2, E2.3-inequality, Robbins) | Assembly recomputed from the stated formulas: tail $0.257649$; endpoint condition $3i_0/31 = 11\,612\,903 \ge 10\,544\,111$ ✓; $S(4) = 3.645833$; error $0.019777$; total $\log u/i \le 0.733524$ (E2's pre-rounding value, reproduced exactly); denominator $\ge 2.249340$; ratio $0.326106 \le 0.3262$ ✓. $\delta = 0.36 - 0.3262 = 0.0338$ ✓. Monotonicity in $i$ of all three pieces verified (tail decreasing, error decreasing, denominator correction decreasing) ✓. |
| Corollary E2.11 ($\alpha \ge 7/2$, $i \ge 1.7\times10^8$) | **PROVED** (same inputs) | Recomputed: tail $0.256413$, error $0.022374$, total $0.743780$, ratio $0.743780/2.093943 = 0.355205 \le 0.3553$ ✓. Endpoint $(5/2)i_1/31 = 13\,709\,677 \ge 10\,544\,111$ ✓. |
| Corollary E2.12 ($\alpha \ge 3$, $i \ge 1.7\times10^8$) | **PROVED** (same inputs) | Recomputed: error $0.026462$, total $0.789871$, ratio $0.789871/1.909542 = 0.413644 \le 0.4138$ ✓. Endpoint $2i_1/31 = 10\,967\,742 \ge 10\,544\,111$ ✓. |
| §6.1 (barrier for unsharpened S7 §5) | **PROVED** (in substance; not load-bearing) | R2 term at $i = 10^8$ recomputed as $0.610$ (E2 prints $0.609$ — rounding only); the $m$-group interval lengths at $\alpha_0 = 4$ recomputed exactly: $m = 1,2,3,4$ give $0.259524$, $0.104509$, $0.056577$, $0.035488$ (E2: $0.2595$, $0.1045$, $0.0566$, $0.0355$) ✓. |
| Lemma E2.13 ($\varphi_{\mathrm{req}}(i,2i) \le 0.6164$) | **PROVED** (mod Robbins) | Ratio bound $\frac{2\log 2 + (\log 2i)/i}{f(4) - (\log 4i)/i}$ re-derived from E2.1 and decreasing in $i$ ✓; at $i_0$ it equals $0.616312 \le 0.6164$ (recomputed); `lgamma` value $\varphi_{\mathrm{req}}(i_0, 2i_0) = 0.61631144$ reproduced ✓. |
| Lemma E2.14 ($\varphi_{\mathrm{req}}(i,j)$ bounds) | **PROVED** (mod Robbins) | Entropy forms re-derived: $F_1(c) = c\log c - (c-1)\log(c-1)$, $F_2(c) = f(2c)$ (the $\log i$ coefficients cancel in both) ✓. $D_\kappa'(c) \le 0$ proof verified: $2\log\frac{2c}{2c-1} \le \log\frac{c}{c-1}$ ⟺ $4c(c-1) \le (2c-1)^2 = 4c(c-1) + 1$ ✓. Constants recomputed: $D_{0.617}(2) = 0.0015488$, $D_{0.580}(7/4) = 0.0193981$, $F_1(7/4) = 1.195089$ ✓; error requirements at $i_1$ hold with margins $255\,000$ vs $32.3$ and $3\,281\,000$ vs $32$ ✓. |
| **Theorem E2.15 (closure)** | **PROVED** (mod (G1)–(G4) and E2.10–E2.14) | (a) $j = 2i$, $i \ge i_0$: margin $1 - 0.3262 - 0.6164 = 0.0574$ ✓. (b) $i \ge i_1 = 1.7\times10^8$: case $j \ge 7i/4$ uses $\alpha \ge 2j/i \ge 7/2$ — the coupling here is $\alpha \ge 2j/i$ directly (not E1's $c \le \alpha/2$), and is sound; margin $1 - 0.3553 - 0.617 = 0.0277$ ✓. Case $3i/2 < j < 7i/4$ uses $\alpha > 3$ (from $n \ge 2j$), margin $1 - 0.4138 - 0.580 = 0.0062$ ✓. Together with (G4) this closes every $j \le 2i$ for $i \ge i_1$ ✓. Exception pairs irrelevant ($i \ge i_0 > 56 \ge$ every exception pair's $i$; in fact max exception $i$ is 17). |
| Computation E2.16 | **PROVED** (as a computation) | Independently recomputed — see §5. All values confirmed, including the exact $\theta_u(378,61)$ to all printed digits. |
| "S7(2.0) FALSE for every $i_0 \le 23$" | **PROVED** (by E2.16 / §5) | The window point $(136, 23)$ has $\theta_u = 0.387523 > 0.36$ (exact integer check $u^{100} > \binom{n}{i}^{36}$ passed in my recomputation), and $23 \ge i_0$ for any $i_0 \le 23$. |

No claim in P-E2 is FALSE as a mathematical statement. The file's one
false claim is bibliographic: Input E2.3's attribution of the
$0.006788$ bound to Dusart 2010 (it is Dusart 1999), with the
consequent overlabel "PROVED as a citation".

---

## 5. Independent empirical recomputation (task item 4)

**My method (independent of both provers' scripts).** For each
$1 \le i \le 500$: $N(i,2i)$ by exact binary search on
$\binom{n}{i} < \binom{4i}{2i}$ (`math.comb`, defining property asserted
at each $i$). For every $n \in [4i, N(i,2i)]$: $\log u$ from **direct
Legendre exponents** $e_p = \sum_e (\lfloor n/p^e \rfloor - \lfloor
i/p^e \rfloor - \lfloor (n-i)/p^e \rfloor)$ over primes $p < i$ (no
incremental sweep); $\log\binom{n}{i}$ by `lgamma`. Every candidate with
float $\theta_u > 0.35$ (47 points) was adjudicated by the **exact
integer test** $\theta_u > 0.36 \iff u^{100} > \binom{n}{i}^{36}$ with
$u$ built from the Legendre exponents. Runtime 50 s.

**Confirmed, matching both provers on every point:**

- Total window points: **299,743** ✓ (both files).
- $\max_i N(i,2i)/i = 6.392034$ at $i = 477$ (E2 ✓); $\max N = 3196$ at
  $i = 500$ (E1 ✓); consistent with the proved cap $6.5$.
- Suprema: $i \ge 1$: $0.591623$ at $(30,7)$; $i \ge 10$: $0.512192$ at
  $(56,13)$; $i \ge 20$: $0.387523$ at $(136,23)$; $i \ge 30$:
  **$0.357355$ at $(145,32)$** (E1's $0.35735$ ✓, E2's $0.357355$ ✓);
  $i \ge 50$: **$0.339629$ at $(378,61)$**; $i \ge 100$: $0.291824$ at
  $(536,114)$; $i \ge 200$: $0.260510$ at $(1170,283)$; $i \ge 300$:
  $0.248309$ at $(1705,383)$ (E1's $0.24831$ ✓).
- Exact values (40-digit `Decimal` from exact integers):
  $\theta_u(378,61) = 0.339629234164629\ldots$ — identical to E2's
  printed exact value; $\theta_u(145,32) = 0.3573547149\ldots$;
  $\theta_u(30,7) = 0.5916231534\ldots$ ✓.
- **Violations of $0.36$: exactly 40, all with $i \le 23$** ✓ (both
  files). The complete list, $(n,i)$ with $\theta_u$:
  $(30,7)\ .591623$, $(56,13)\ .512192$, $(56,9)\ .482758$,
  $(28,5)\ .467595$, $(36,7)\ .456308$, $(18,4)\ .446479$,
  $(16,3)\ .438151$, $(57,14)\ .436039$, $(81,19)\ .429698$,
  $(28,7)\ .420904$, $(32,8)\ .420716$, $(66,13)\ .414853$,
  $(18,3)\ .413547$, $(57,13)\ .413400$, $(60,13)\ .412680$,
  $(30,6)\ .407402$, $(50,11)\ .405989$, $(28,6)\ .404458$,
  $(56,14)\ .402840$, $(20,5)\ .401208$, $(58,11)\ .400404$,
  $(57,10)\ .399283$, $(33,7)\ .397471$, $(29,6)\ .397285$,
  $(56,12)\ .395375$, $(50,9)\ .392621$, $(55,12)\ .389935$,
  $(136,23)\ .387523$, $(25,6)\ .381082$, $(57,11)\ .376930$,
  $(32,7)\ .376797$, $(55,13)\ .373278$, $(54,13)\ .367184$,
  $(31,7)\ .366390$, $(81,20)\ .364833$, $(56,11)\ .364311$,
  $(29,7)\ .364145$, $(52,13)\ .363665$, $(82,20)\ .362476$,
  $(32,6)\ .362310$. Largest violating $i$: $23$ at $(136,23)$ ✓.
  Largest non-exception violation: $(56,9)$, $0.482758$ ✓ (E2).
  No corrections to either prover's empirical claims.

---

## 6. Closure coverage — what is and is not closed (task item 5)

The $\theta_u$ bounds themselves (E1.8, E2.10) are statements about the
window $4i \le n \le N(i,2i)$ only. " $j \le 2i$ closed for $i \ge i_0$"
follows only through the $\varphi_{\mathrm{req}}$ comparison, and the two
files do it differently:

- **E2 (certified):** $\varphi_{\mathrm{req}}$ is bounded directly for
  all $3i/2 \le j \le 2i$ (E2.14, proof sound), and the strip
  $3i/2 < j < 2i$ is covered by the $\alpha \ge 7/2$ and $\alpha \ge 3$
  assemblies (E2.11/E2.12) using $\alpha \ge 2j/i$. The conclusion
  "every $j \le 2i$ closed" is valid for $i \ge i_1 = 170\,000\,000$;
  the single pair $(i, 2i)$ is already closed for $i \ge i_0 =
  120\,000\,000$. Margins: $0.0574$, $0.0277$, $0.0062$.
- **E1 (gap as filed):** Case A ($n \ge 4i$) is sound. Case B
  ($3i < n < 4i$) couples $c = j/i \le \alpha/2$ — that step is correct
  (it is exactly $j \le n/2$ rewritten) and the band pairing/margins
  ($0.0057$, $0.0052$) are correct — but it quotes $\varphi_{\mathrm{req}}$
  bounds for $c < 2$ from E1.10's monotonicity, whose proof is
  defective (§3). After substituting the corrected monotonicity proof
  given in §3, E1's closure also goes through, at $i \ge 2\times10^8$.

**What neither closure covers** (both files state this correctly):
the **finite residue $i < i_0$** (E2: $i < 1.7\times10^8$ for the full
strip, $i < 1.2\times10^8$ for the pair $(i,2i)$), $3i/2 < j \le 2i$.
It is *not* discharged by the $n \le 20\,000$ sweep ($N(i,2i) \approx
6.39\,i$ exceeds $20\,000$ already for $i \gtrsim 3130$) nor by Cycle
1's in-scope counts ($i \le 1000$). It requires a targeted finite check
or an $i_0$-lowering refinement; neither file performs or sizes it
(per the brief). Also untouched: all $j > 2i$, and Erdős #699 in
general. The EEES78 exception pairs play no role at these thresholds
(all have $i \le 17$).

---

## 7. Adjudication of parameters (task item 2)

| | $i_0$ for S7(2.0) | proved $\theta_u$ | $\delta$ | full $j \le 2i$ closure at | status |
|---|---|---|---|---|---|
| E1 | $2\times10^8$ | $0.356$ | $0.004$ | $2\times10^8$ | main theorem PROVED; closure GAP as filed (E1.10 monotonicity), repairable by §3 correction |
| E2 | $1.2\times10^8$ | $0.3262$ | $0.0338$ | $1.7\times10^8$ | PROVED throughout, modulo the E2.3 attribution defect (bibliographic only) |

E2 is stronger on **every** parameter (smaller $i_0$, larger $\delta$,
smaller closure threshold, larger closure margins $0.0574/0.0277/0.0062$
vs E1's $0.0277/0.0057/0.0052$), and its derivation is fully sound modulo
correctly-stated published estimates. Per the brief, the certified
statement is therefore E2's. E1 stands as an independent corroboration
of S7(2.0) at weaker parameters, with its main theorem (E1.8) proved
outright and its closure one repaired step short.

Neither proof "fails" in the sense of §2's alternative: there is no
barrier left for S7(2.0) itself. The exact defects found are: (i) E1.10's
factor-of-2 derivative condition (proof gap, statement true, correction
supplied); (ii) E2.3's misattributed source (Dusart 1999, not 2010;
statement exact, no downstream effect).

---

## 8. Certified bottom line for Cluster E

1. **Lemma S7(2.0) is PROVED** with the certified constants
   $$i_0 = 120\,000\,000, \qquad \delta = 0.0338,$$
   i.e. $\theta_u(n,i) \le 0.3262$ for all $i \ge i_0$ and
   $4i \le n \le N(i,2i)$ (Theorem E2.10), **modulo** the published
   explicit estimates: Dusart's $\pi(x) < x/(\log x - 1.1)$ for
   $x \ge 60184$ (Dusart 2010; SECONDARY ONLY this session, correctly
   stated); Dusart's $|\vartheta(x) - x| \le 0.006788\,x/\log x$ for
   $x \ge 10\,544\,111$ (correctly stated; published source is
   **Dusart 1999**, C. R. Math. Acad. Sci. Soc. R. Can. 21(2):53–59 —
   E2's "Dusart 2010" attribution is misquoted and must be corrected
   in any citation of E2); and Robbins' 1955 Stirling bounds
   (correctly stated).
2. **Closure certified (E2.15):** the pair $(i, 2i)$ is closed for all
   $i \ge 120\,000\,000$ (margin $0.0574$), and **every pair $j \le 2i$
   is closed for all $i \ge 170\,000\,000$** (margins $0.0277$ and
   $0.0062$), modulo the established ground truth (G1)–(G4).
3. **Independent corroboration (E1):** Lemma S7(2.0) is also PROVED at
   $i_0 = 200\,000\,000$, $\delta = 0.004$ (Theorem E1.8) modulo
   Dusart's $\pi$ bound with constant $2.51$ at $x \ge 355991$ and
   Dusart's $|\theta(x) - x| < x/\log^3 x$ at $x \ge 89\,967\,803$
   (both SECONDARY ONLY this session, both correctly stated) and
   Robbins. E1's closure Theorem E1.9 is **GAP as filed** (Case B uses
   Lemma E1.10's defective monotonicity step); with the corrected
   monotonicity proof recorded in §3 it closes $j \le 2i$ for
   $i \ge 2\times10^8$.
4. **Empirics certified:** 299,743 window points for $i \le 500$;
   $\sup_{i \ge 50} \theta_u = 0.339629$ at $(378,61)$;
   $\sup_{i \ge 30} \theta_u = 0.357355$ at $(145,32)$; exactly **40**
   violations of $0.36$, all at $i \le 23$ (full list in §5); hence
   S7(2.0) is FALSE for every $i_0 \le 23$.
5. **Not covered / still open:** the finite residue $i < 1.7\times10^8$,
   $3i/2 < j \le 2i$ (not discharged by the $n \le 20\,000$ sweep or
   Cycle 1 counts; unsized, per the brief); all $j > 2i$; Erdős #699
   in general.

*Verification performed with independent Python (stdlib) computations
saved in this session's scratch (`ve_checks.py`, `ve_empirical.py`,
`ve_char.py` in /tmp) and web checks via `browser.search`/`browser.open`
as detailed in §2.*
