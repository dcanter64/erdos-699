# Primary-source verification — Cycle 2

**Scope.** Three citations the campaign held only at secondary level:
Dusart 2018 Cor. 5.5 (used in S3 Theorem B, region B2), Axler 2017
"Thm 4.1" (used in S3 Theorem B, region B3), and the Rosser–Schoenfeld
bound $\theta(x) < 1.1x$ (remarked, not used, in S4 / P-D1 / P-D2).
**Method.** `browser.search` / `browser.open` only. Below, "sighted"
means the quoted words appeared in the text returned by `browser.open`
for the URL given. PDF text extraction interleaves fraction numerators
and denominators; where that happens the extraction order is noted and
the formula is transcribed in its standard printed arrangement, which
is confirmed in each case by a second, independently sighted statement
of the same result in the same document (introduction summary or a
restatement). No statement is reconstructed from memory: anything not
read is marked NOT VERIFIED.

Campaign usage reconstructed first (from `strategies/S3.md` §3–§4,
`proofs/P-C1.md` §4, `proofs/P-C2.md` §4): S3 converts a forward
statement "for $x \ge x_0$ there is a prime in
$(x, x(1 + C/\log^m x)]$", applied at $x = n-i$, into the backward
sufficient condition $i \ge C(n-i)/\log^m(n-i)$, $n-i \ge x_0$.
Theorem B is: (B2) $n-i \ge 468991632$ and
$i \ge (n-i)/(5000\log^2(n-i))$ (Dusart 2018); (B3) $n-i \ge 6034256$
and $i \ge 0.087\,(n-i)/\log^3(n-i)$ (Axler 2017). P-C1 Flag F2 left
Dusart 2018 survey-verified only; P-C2 §7 item 4 left the Axler
theorem number unverified. Both flags are resolved below.

---

## Item 1 — Dusart 2018, Corollary 5.5

**Source located (primary, read in full).**
Pierre Dusart, "Explicit estimates of some functions over primes",
*Ramanujan Journal* 45 (2018), 227–251. Journal header sighted on
p. 1 of the PDF: "Ramanujan J (2018) 45:227–251
https://doi.org/10.1007/s11139-016-9839-4", with "Received: 18 March
2016 / Accepted: 10 August 2016 / Published online: 27 October 2016"
— i.e. the "2018" citation is the journal-issue year, 2016 the
online-first year (this explains the split year in some
bibliographies; it is not a discrepancy).
URL read:
https://piyanit.nl/wp-content/uploads/2020/10/art_10.1007_s11139-016-9839-4.pdf?utm_source=chatgpt.com
(a complete publisher-formatted PDF of the journal article).

**Exact statement sighted — Corollary 5.5 (§5.2, p. 242).**

> "Corollary 5.5  For all x ≥ 468 991 632, there exists a prime p
> such that x < p ≤ x(1 + 1/(5000 ln²x))."

In the extraction the "1/5000" appears on the line above
"x < p ≤ x(1 + … ln²x)", i.e. as the numerator over $\ln^2 x$; the
arrangement above is the printed one and is confirmed by the
article's own introduction summary, sighted on p. 229:

> "We use the above results to prove (Corollary 5.5) that, for
> x ≥ 468 991 632, the interval [x, x + x/(5000 ln²x)] contains at
> least one prime."

**Corroboration inside a second primary source.** Axler's paper
(Item 2) restates it, sighted in §4 of that paper:

> "Recently, Dusart [13, Corollary 5.5] improved Trudgian's result
> by showing that for every x ≥ 468 991 632 there exists a prime
> number p such that x < p ≤ x(1 + 1/(5000 log²x))."

**Companion statement also sighted (campaign's D18b row).**
Immediately preceding, on the same page:

> "Proposition 5.4  For all x ≥ 89 693, there exists a prime p such
> that x < p ≤ x(1 + 1/ln³x)."

This matches S3's table row "Dusart 2018, Prop. 5.4, $x \ge 89693$,
$C = 1$, $m = 3$" exactly.

**Comparison with the campaign citation.**

| Element | Campaign (S3 / P-C1 / P-C2) | Primary text |
|---|---|---|
| Number | Cor. 5.5 | Corollary 5.5 — same |
| Threshold | $x \ge 468991632$ | $x \ge 468\,991\,632$ — same |
| Constant / exponent | $C = 1/5000$, $m = 2$ | $1/(5000\ln^2 x)$ — same |
| Form | prime in $(x, x(1 + C/\log^m x)]$ | $x < p \le x(1 + 1/(5000\ln^2 x))$ — same |
| Side conditions | none stated | none beyond $x \ge 468991632$ |

No discrepancy. Note only the direction convention the campaign
already handles correctly: Dusart states a *forward* interval
$(x, x(1+\delta)]$; the backward form
$(x - x/(5000\log^2 x), x]$ in the task brief is not Dusart's
wording — S3's B2 is obtained by applying the forward statement at
$x = n-i$, as S3 §3 / P-C1 §4 / P-C2 Lemma C2.7 set out.

**Verdict: PRIMARY VERIFIED.** Corollary number, threshold,
constant $1/5000$, exponent $2$, interval form and absence of extra
side conditions were all read in Dusart's own journal text. P-C1's
Flag F2 can be closed.

---

## Item 2 — Axler 2017, theorem numbering for the 0.087 / log³ statement

**Source located (primary, read in full).**
Christian Axler, "New estimates for some functions defined over
primes", arXiv:1703.08032v2 [math.NT], 17 May 2017. The arXiv
abstract page (https://arxiv.org/abs/1703.08032) was sighted with:
"Comments: 14 pages, v2: minor changes (for instance, a smaller
interval in Theorem 4.1 is obtained)"; v1 (23 Mar 2017) carried the
shorter title "New estimates for some prime functions", v2 the
title above. The full text read was the v2 PDF:
https://storage.googleapis.com/arxiv-dataset/arxiv/arxiv/pdf/1703/1703.08032v2.pdf
(also at https://arxiv.org/pdf/1703.08032). All quotations below are
from **v2**; the v2 comment just quoted shows the Theorem 4.1
interval changed between v1 and v2, so the version matters.

**Exact statement sighted — Theorem 4.1 (§4, p. 10 of the preprint).**

> "Theorem 4.1. For every x ≥ 6 034 256 there is a prime number p,
> such that x < p ≤ x(1 + 0.087/log³x), and for every x > 1 there
> is a prime number p, such that x < p ≤ x(1 + 198.2/log⁴x)."

(Extraction order as in Item 1: "0.087" appears on the line above
"x < p ≤ x(1 + … log³x)".) The same statement is announced in the
introduction, sighted on p. 2, under a dual number:

> "Theorem 1.4 (See Theorem 4.1). For every x ≥ 6 034 256 there is
> a prime number p, such that x < p ≤ x(1 + 0.087/log³x), and for
> every x > 1 there is a prime number p, such that
> x < p ≤ x(1 + 198.2/log⁴x)."

**Comparison with the campaign citation.**

| Element | Campaign (S3 / P-C2) | Primary text (v2) |
|---|---|---|
| Label | "Axler 2017, Thm 4.1" | Theorem 4.1 — **correct**; also Theorem 1.4 in the introduction |
| Threshold | $x \ge 6034256$ | $x \ge 6\,034\,256$ — same |
| Constant / exponent | $C = 0.087$, $m = 3$ | $0.087/\log^3 x$ — same |
| Form | prime in $(x, x(1 + C/\log^m x)]$ | $x < p \le x(1 + 0.087/\log^3 x)$ — same |
| Extra content | not used by the campaign | Theorem 4.1 has a second clause, for every $x > 1$: prime in $(x, x(1 + 198.2/\log^4 x)]$ — the S3 table's extra Axler row ($x_0 = 1$, $C = 198.2$, $m = 4$) is this clause |

No discrepancy in the part the campaign uses. Two precisions worth
recording: (i) P-C1's parenthetical "(= Thm. 1.4)" is also correct —
1.4 is the introduction's announcement of 4.1, not a different
theorem; (ii) §4 of Axler's paper introduces Theorem 4.1 explicitly
as an improvement of Dusart's Proposition 5.4 (Item 1), which is
the logical position S3's B3 occupies relative to B2/D18b.

**Verdict: PRIMARY VERIFIED.** The statement and the "Thm 4.1"
label were both read in Axler's own text (v2). P-C2 §7 item 4's
"theorem number unverified" flag can be closed, and B3 may be cited
simply as "Axler 2017, arXiv:1703.08032v2, Thm. 4.1" without the
"as tabulated in …" hedge.

---

## Item 3 — Rosser–Schoenfeld bound θ(x) < 1.1·x (secondary item)

Campaign usage: S4 §5 Remark (i) states the bound as
"the explicit Rosser–Schoenfeld bound $\theta(j) < 1.1\,j$
(to be referee-checked before use)"; P-D1 and P-D2 both record it
as **not used** in any proved statement, with P-D1 attributing it to
"Rosser–Schoenfeld (1975)". The task brief attributes it to
Rosser & Schoenfeld 1975, "Approximate formulas for some functions
of prime numbers".

**Bibliographic problem sighted.** Those two halves do not belong
to the same paper:

- "Approximate formulas for some functions of prime numbers" is
  J. B. Rosser and L. Schoenfeld, *Illinois Journal of
  Mathematics* 6 (**1962**), 64–94. Sighted as reference [24] in
  Garcia–Lee (below): "24. J. B. Rosser and L. Schoenfeld,
  Approximate formulas for some functions of prime numbers,
  Illinois J. Math. 6 (1962), 64–94. MR 0137689".
- The 1975 Rosser–Schoenfeld paper is a different work, "Sharper
  Bounds for the Chebyshev Functions $\theta(x)$ and $\psi(x)$",
  *Mathematics of Computation* 29 (1975), 243–269
  (DOI 10.1090/S0025-5718-1975-0457373-7) — journal header, authors
  and abstract sighted in search-result text for the AMS PDF.

**What was sighted about the bound itself (secondary, open).**
Stephan Ramon Garcia and Ethan Simpson Lee, "Unconditional explicit
Mertens' theorems for number fields and Dedekind zeta residue
bounds" (accepted manuscript, openly readable at
https://uwe-repository.worktribe.com/previewfile/15804297/GarciaLee-EMT4NFs_accepted.pdf),
§2.2, sighted verbatim:

> "We need the following result of Rosser–Schoenfeld [24, Thm. 9]:
> $\theta(x) = \sum_{p \le x} \log p < 1.01624x < 1.1x$, for
> $x > 0$. (6)"

with [24] identified in their bibliography as the **1962**
"Approximate formulas" paper, as above. So, on this openly readable
attribution, the $1.1$ bound is a deliberate weakening of a sharper
primary statement — $\theta(x) < 1.01624x$ for $x > 0$, Theorem 9
of the 1962 paper — and the campaign's "$< 1.1x$" is true but loose,
with no range restriction needed. Garcia–Lee's Remark 14 (also
sighted) notes (6) "has been improved over the years. The current
record appears to be due to Broadbent, Kadiri, Lumley, Ng, and
Wilk, who proved that $\theta(x) < (1 + 1.93378 \times 10^{-8})x$,
for $x \ge 0$" — quoted here as their attribution, not independently
verified in this pass.

**Best openly readable primary $\theta$ bounds sighted in this pass**
(for use instead of the loose $1.1$, if the campaign ever wants the
remark promoted):

- Dusart 2018 (Item 1 source), Theorem 4.2, sighted on p. 237:
  "We have $|\vartheta(x) - x| < \eta_k x / \ln^k x$ for
  $x \ge x_k$", with a table of $(\eta_k, x_k)$ pairs (extraction
  pairs them in column order; e.g. $\eta_3 = 0.5$ at
  $x_k = 767\,135\,587$ appears in Axler's restatement of Dusart's
  table, Lemma 2.3 there). Hence in particular
  $\theta(x) < x + \eta_k x/\ln^k x$ in the stated ranges.
- Axler 2017 (Item 2 source), Theorem 2.4 (= Theorem 1.1),
  sighted: "for every $x > 1$, we have
  $\vartheta(x) < x + 0.15x/\log^3 x$", and "for every
  $x \ge 19\,035\,709\,163$, $\vartheta(x) > x - 0.15x/\log^3 x$".
- Dusart 2018, proof of Proposition 4.4, sighted: "For $x > 0$, we
  have $\vartheta(x) < 1.000081x$ by [38, p. 360]" — Dusart's in-text
  citation of Schoenfeld 1976; quoted here as Dusart's text, not as
  Schoenfeld sighted directly.

**What could not be verified, and why.** The Rosser–Schoenfeld
primary text itself (either the 1962 *Illinois J. Math.* paper or
the 1975 *Math. Comp.* paper) was **not** read in this pass: no
open full text of the 1962 paper was returned by search, and the
one attempt to fetch the AMS PDF of the 1975 paper via
`browser.open` failed at the fetch stage (no source text returned);
it was not retried. Theorem 9 / the constant $1.01624$ / the range
$x > 0$ therefore rest, in this file, on Garcia–Lee's explicit
attribution quoted above, not on the primary page.

**Verdict: PARTIALLY VERIFIED.** (a) The bound $\theta(x) < 1.1x$
as the campaign states it is corroborated by an openly readable
secondary source that attributes the sharper
$\theta(x) < 1.01624x$ ($x > 0$) to Rosser–Schoenfeld, Theorem 9 —
but of the **1962** "Approximate formulas" paper, so the campaign's
"1975" attribution (P-D1) and the brief's "1975 + that title"
combination conflate two different Rosser–Schoenfeld papers and
should be corrected to 1962, Thm. 9, if the remark is ever used.
(b) The primary Rosser–Schoenfeld text was not sighted, for the
reason given above, so the theorem number $9$ and constant
$1.01624$ are NOT VERIFIED at primary level in this pass.
Nothing proved in the campaign depends on this item (S4, P-D1 and
P-D2 all leave it unused).

---

## Summary

| Item | Verdict | Effect on the campaign |
|---|---|---|
| 1. Dusart 2018, Cor. 5.5: $x \ge 468991632$, prime in $(x, x(1 + 1/(5000\ln^2 x))]$ | **PRIMARY VERIFIED** | B2 stands as cited; P-C1 Flag F2 closed. No discrepancy. |
| 2. Axler 2017, $x \ge 6034256$, prime in $(x, x(1 + 0.087/\log^3 x)]$ | **PRIMARY VERIFIED**, label **Thm. 4.1** (v2; = Thm. 1.4 in the introduction) | B3 stands as cited; P-C2's unverified-label flag closed. Note the v1/v2 version sensitivity. |
| 3. Rosser–Schoenfeld $\theta(x) < 1.1x$ | **PARTIALLY VERIFIED** (secondary only; primary not sighted) | Unused by any proof. If used: cite Rosser–Schoenfeld 1962, Thm. 9, $\theta(x) < 1.01624x$ for $x > 0$ (per Garcia–Lee), not "1975"; or use the Dusart 2018 Thm. 4.2 / Axler 2017 Thm. 2.4 primary bounds sighted above. |

*Verification performed 2026-10-29 (America/New_York) with
`browser.search` / `browser.open`. Quotations are transcribed from
the page text those tools returned for the URLs listed under each
item; fraction glyph order in the PDF extractions is noted where it
affects the transcription.*
