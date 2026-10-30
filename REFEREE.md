# Referee Report — the claimed proof of Erdős #699 for j ≤ 3i/2

Erdős #699 Referee-and-Proof Campaign, Cycle 1, Workstream A.
Date: 2026-10-28. Synthesis of two independent referee reports
(referee/referee1.md, reconstruction, ~8,900 words;
referee/referee2.md, adversarial) and the coordinator's independent
bounded computations (referee/coordinator_checks.md). The referees
worked independently of each other and of Phase 0; where they agree,
this report says so; no substantive disagreement arose.

## 0. Texts: obtained versus inaccessible

OBTAINED (fullest available):
- **Bloom's exposition** of the proof, complete verbatim text
  (erdosproblems.com/699, last edited 27 Aug 2026; fetched and saved
  as texts/bloom_exposition_699.md). It is a short, self-contained
  argument ending in the contradiction. This is the text refereed.
- **The main problem page** (statement verbatim; metadata: Comments
  (9), Proof claims (2), Proof expositions (1); page last edited
  19 July 2026), including its assertion that GPT 5.6 (prompted by
  Price) proved the statement "if j ≤ 3i/2 OR n = 2j".
- **EEES78** (Ecklund–Eggleton–Erdős–Selfridge, J. Austral. Math.
  Soc. A 26(3), 1978): abstract verbatim; the 12 exception pairs
  recovered from the paper and confirmed by three independent
  computations (Phase 0 to n ≤ 240 and n ≤ 400; Referee 2 to
  n ≤ 600; coordinator to n ≤ 400 — all return exactly the 12).

INACCESSIBLE (a finding in itself):
- **The raw GPT 5.6 Sol proof-claim text** (both proof claims): the
  site's forum returns HTTP 403 to automated fetching (confirmed
  again this cycle); the bodies are not search-indexed; a Wayback
  route also failed through the available fetcher; the GitHub
  metadata repo carries status only. No mirror or PDF exists for
  #699 (the ulam.ai PDF belongs to #488). Consequently the fidelity
  of Bloom's exposition to the raw claim is UNVERIFIABLE, and any
  argument present only in the raw claim (in particular any n = 2j
  argument) is unrefereed by anyone in this campaign.
- **The 9 comment bodies**: same barrier.

The refereeing below is therefore of the argument AS EXPOSITED by
Bloom, which Bloom presents as his own mini-exposition of the claim.
The exposited argument is self-contained, so this limitation does
not weaken the section-by-section verdicts; it limits only what can
be said about the raw claim and about the n = 2j assertion.

## 1. Reconstruction (condensed from Referee 1)

Claim (Theorem R). Let 1 ≤ i < j ≤ n/2 with j ≤ 3i/2, and suppose
(n, i) is not one of the 12 EEES78 exception pairs. Then
gcd(V_i(n), C(n,j)) > 1, where V_i(n) is the part of C(n,i) on
primes ≥ i.

Steps. (S0) Reformulation: a common prime ≥ i exists iff
gcd(V_i(n), C(n,j)) > 1 (prime divisors of V_i(n) are exactly the
primes ≥ i dividing C(n,i); holds also when V_i(n) = 1, both sides
then failing together). (S1) EEES78 input: writing C(n,i) = u·v with
u on primes < i and v = V_i(n), u < v (non-exception pairs), hence
v² > u·v = C(n,i). EEES78's hypothesis n ≥ 2k is met at (n, i) since
the problem's range gives n ≥ 2j ≥ 2i + 2. (S2) Identity
C(n,i)·C(n−i, j−i) = C(n,j)·C(j,i). (S3) Key lemma: d | C(n,i) with
gcd(d, C(n,j)) = 1 implies d | C(j,i) (Euclid). (S4) Under the
contrary assumption, v | C(j, j−i), so v² ≤ C(j, j−i)². (S5)
Vandermonde: C(j, j−i)² < Σ_k C(j,k)C(j, 2(j−i)−k) = C(2j, 2(j−i)),
strict because the sum has at least three positive terms (2(j−i)+1
terms when 2(j−i) ≤ j, else 2i+1 terms; the central term is one of
them). (S6) Combination: C(n,i) < C(2j, 2(j−i)). (S7) Closure: for
j ≤ 3i/2, 2(j−i) ≤ i ≤ j, and C(2j, ·) is nondecreasing on [0, j], so
C(2j, 2(j−i)) ≤ C(2j, i); and C(·, i) is increasing, with 2j ≤ n, so
C(2j, i) ≤ C(n, i): contradiction with (S6). Boundaries j = 3i/2
and n = 2j are safe because the only strict inequality needed sits
in (S6). (S8) Finiteness remark: for fixed (i, j), (S6) bounds the
possible bad n (per-pair finiteness only).

Dependency graph (text form). S0: definitions only. S3 ← S2 +
Euclid. S4 ← S3. S6 ← S1, S4, S5. S7 ← S6 + two elementary
monotonicities. Theorem R ← S0, S6, S7, plus the exception-pair
discharge (external, §3 below), which is a hypothesis of S1. EEES78
enters exactly once, at S1. Sylvester–Schur is nowhere used.

## 2. Section-by-section verdicts

| Step | Verdict | Notes |
|---|---|---|
| S0 reformulation | PROVED (gap in text, filled) | Exposition asserts equivalence without comment; both referees prove it, incl. the v = 1 case. Correct ONLY under the ≥ convention (see §4). |
| S1 EEES78 → v² > C(n,i) | PROVED as a derivation; **GAP (material) as invoked** | Derivation u < v ⟹ v² > C(n,i) exact; all 12 exceptions have u > v strictly, so "not an exception" ⟺ "u < v". But the exposition names and discharges NO exceptions while every later step is conditioned on non-exceptionality. See §3. |
| S2 identity | PROVED | Standard double count; also under the 1,113,775-triple numerical umbrella (Referee 2) and Phase 0's 568,820-triple check. |
| S3 key lemma | PROVED | Euclid via the identity; strong form verified computationally (Referee 2: all n ≤ 300; Phase 0: n ≤ 240). |
| S4 v ≤ C(j, j−i) | PROVED | Divisibility of positive integers + binomial symmetry. |
| S5 Vandermonde strictness | GAP (presentational, filled) | Asserted without comment in the exposition. Filled by the ≥ 3 positive terms argument; numerically min ratio 1.5 at (j, j−i) = (2,1) over j ≤ 1000 (Referee 2); coordinator: 0 failures to j ≤ 500. This strictness is genuinely load-bearing: at j = 3i/2 the proof's margin is exactly one integer (Referee 2: N(300, 450) = 899 = 2j − 1). |
| S6 combination | PROVED (conditional on S1's hypothesis) | Pure inequality chaining. |
| S7 closure chain | GAP (presentational, filled) | Neither monotonicity is mentioned in the exposition; both filled by one-line ratio arguments (Referee 2 §4, steps 9b/9c; Referee 1 §4(d)). Equalities at j = 3i/2 and n = 2j are harmless. |
| S8 finiteness | PROVED (per-pair) | Phase 0's scope correction stands: finiteness is per fixed pair (i, j); the region j > 3i/2 is infinite pair by pair. |
| EEES78 itself | EXTERNAL INPUT (accepted) | A published 1978 theorem; its statement, convention, and 12-pair exception list were verified against the paper and by independent computation (see §4). Its proof was not re-refereed (standard practice for a cited theorem; recorded explicitly). |
| Raw GPT claim | UNVERIFIABLE | Text inaccessible (403). Attribution only. |
| Page's "OR n = 2j" | **NOT PROVED by any available text** | See §5. |

**Errors found in the exposited deduction: NONE** (both referees,
independently). Every step is either proved in the text, proved by
the referees, or is the single material gap of §3.

## 3. The one material gap: EEES78 exceptions

At an exception pair (n0, i0), u > v, hence v² < C(n0, i0): the
input (S1) fails in the opposite direction, and the exposition —
which never lists the exceptions — proves nothing for any triple
with (n, i) an exception pair, in either region. The complete list
of affected j values: 41 triples (27 inside j ≤ 3i/2, 14 outside;
(9,4) and (10,5) vacuous, i0 = ⌊n0/2⌋). Referee 1's failing-case
exhibit: at (8,3,4), v = 7, v² = 49 < 56 = C(8,3), and the
unqualified claim "C(n,i) < C(2j, 2(j−i))" would read 56 < 28 —
false (the triple is not a counterexample to #699: gcd = 7).

The gap is closed EXTERNALLY, by direct computation, four times
over independently: Phase 0's checker (41 triples, all gcd > 1),
Referee 1 (Appendix B recomputation), Referee 2 (§2.7), and the
coordinator (41 triples, 0 with gcd = 1). With the discharge, the
region j ≤ 3i/2 is fully proved. Without it, the exposition proves
Theorem R only for non-exception (n, i). "Conditional on EEES78"
must therefore be read literally: EEES78-with-its-exceptions-
discharged is part of the proof, and the discharge is computational.

## 4. Convention audit (Referee 2, confirmed by Referee 1)

The proof needs, and Bloom consistently uses, v = part on primes
≥ i and u on primes < i, with exactly 12 exceptions. The ≥ vs >
distinction is load-bearing at exactly two points:
(i) The reformulation S0: under the > convention it becomes the
strengthened variant of #699, which is FALSE — witness (28,5,14):
gcd(V_{≥5}(28), C(28,14)) = 5 (the prime i itself) but
gcd(V_{>5}(28), C(28,14)) = 1, computed exactly.
(ii) The EEES78 input S1: under the > convention, EEES78's second
theorem proves only finiteness of the u > v cases (19 known, not
proved complete), so the exceptions could not be discharged at
all; and the sets genuinely differ — 7 pairs with n ≤ 200, smallest
(9,3), have u_≤ > v_> while u_< < v_≥, i.e. the >-convention
inequality fails exactly where the ≥ version holds.
All later steps (identity, Euclid, Vandermonde, monotonicities) are
convention-blind. The primes < k versus ≤ k question flagged in
Phase 0 is thus resolved: the operative input is primes < k vs ≥ k,
Bloom uses it correctly, and substituting the other convention
breaks the proof at S0 and S1.

## 5. The n = 2j assertion

The page asserts the proof covers "j ≤ 3i/2 OR n = 2j". Findings:
- The exposition does not state, mention, or address the n = 2j
  case. For j ≤ 3i/2 it is already inside Theorem R; the new content
  would be n = 2j with j > 3i/2.
- The exposited method PROVABLY cannot cover it (Referee 1 §6.2,
  obstruction Proposition): for every i < j with j > 3i/2,
  C(2j, 2(j−i)) > C(2j, i) (strict monotonicity on [0, j] when
  2(j−i) ≤ j; symmetry C(2j, 2(j−i)) = C(2j, 2i) with i < 2i < j
  when 2(j−i) > j). Hence at n = 2j the necessary condition
  C(n,i) < C(2j, 2(j−i)) holds automatically and the closure chain
  fails at its first inequality, exactly, for every such pair.
  Smallest witness (both referees, and the coordinator):
  (i, j) = (1, 2): C(4,1) = 4 < 6 = C(4,2).
- The n = 2j STATEMENT itself is not in doubt computationally:
  Referee 2 verified gcd(V_i(2j), C(2j,j)) > 1 for all 79,800 pairs
  i < j ≤ 400 (0 failures). And in our own Stage 2, n = 2j is the
  left endpoint of every swept interval and is checked directly.
- Classification: as a claim about what is proved, the page's
  "OR n = 2j" is UNVERIFIABLE from available texts (any separate
  argument lives in the inaccessible raw claim) and is an ERROR of
  coverage if attributed to the exposited chain. It is immaterial
  to our RESULTS.md, which never relies on it.

## 6. Overall verdict

**Sound modulo one named gap, which is externally closed.** The
Bloom exposition is a sound and, after the standard exception
discharge, complete proof of Problem #699 for the region
j ≤ 3i/2, conditional on the published theorem EEES78. No error
was found in the deduction by either referee. The gaps are: one
material gap (EEES78 exceptions neither named nor discharged in
the exposition; closed by direct computation of 41 triples,
verified four times independently) and three presentational gaps
(reformulation, Vandermonde strictness, the two monotonicities),
all filled by the referees. Phase 0's verdict — SOUND conditional
on EEES78 — is confirmed and sharpened: the conditionality
includes the discharge, which is computational, not textual.

## 7. What RESULTS.md is entitled to claim about j ≤ 3i/2

Entitled (and this matches RESULTS.md's current wording):
"For every pair (i, j) with j ≤ 3i/2, the conjecture holds for all
n. This rests on (a) the argument exposited by Bloom for the GPT
5.6 Sol / Price proof claim, independently refereed line by line
(Cycle 1, two referees plus coordinator checks) and found sound
with no errors, conditional on EEES78; and (b) the direct
computational discharge of EEES78's 12 exception pairs (41
triples, all gcd > 1), which the exposition itself does not
contain."

NOT entitled:
- "The GPT 5.6 Sol proof was refereed." (Only Bloom's exposition
  of it was; the raw claim is inaccessible.)
- "n = 2j is proved" as a universal case for j > 3i/2. (Asserted
  on the page; not proved in any available text; the exposited
  method provably cannot prove it. Per-pair, n = 2j triples are
  covered by our sweep wherever the pair's interval was swept.)
- Any weakening of "conditional on EEES78": EEES78 is a cited
  published theorem whose proof was not re-refereed; its
  statement, convention, and exception list were verified.

## Addendum 2026-10-29: Price's original manuscript obtained; both open items resolved

Dennis retrieved the original manuscript from the erdosproblems forum
("Common Prime Divisors of Binomial Coefficients", GPT 5.6 Sol Pro;
~/workspace/user/files/Liam_699_partial.pdf) and Muse read it in full.
This addendum supplements, and does not alter, the referee verdict above,
which concerned Bloom's exposition as its stated object.

1. The exception-pair gap was exposition-only. Price's text contains
   Lemma 1.3, discharging every EEES78 exceptional pair explicitly:
   (9,4) and (10,5) admit no admissible j, and the remaining ten pairs are
   handled by terminal primes q > n/2 with n - q < i, giving
   v_q(C(n,r)) = 1 for all i <= r <= n/2. The prime table is IDENTICAL,
   entry for entry, to the one in the Van Doorn-Rocca write-up and to the
   discharge our own Phase 0 verification produced independently. The
   exposition omitted this lemma; the underlying proof did not. The
   j <= 3i/2 closure is therefore sound as written in the original, not
   merely modulo our external patch.

2. The n = 2j side finding is retired. The original proves the central
   case (Proposition 3.3) in full: a central compression lemma
   (V_i(2m) divides C(m, ceil(i/2))), the even case by Vandermonde, odd
   composite i by reduction to i-1, and odd prime i = 2k+1 by an analytic
   argument for k >= 2500 plus an exact finite computation for k < 2500.
   Appendix A includes the complete Python code for the finite part.
   Muse transcribed and ran it (price_appendixA.py in this workspace):
   it reproduces the manuscript's certificate exactly, 666 endpoint
   checks, minimum ratio C(108,19) / C(54,10)^2 =
   659645433004618405800 / 572679032824811448900 > 1 at
   (k,p,e,A_k,M_k) = (9,19,3,91,54). The analytic branch (k >= 2500) was
   read and is coherent in structure; its individual explicit estimates
   were not each re-derived in this pass.

3. Proposition 4.1 of the manuscript adds a Euclidean-division necessary
   condition for any counterexample outside the two proved ranges
   (V_i(n) controlled by a Lambda_i(T) term and a short falling factorial
   in j). Noted for the proof campaign's criteria file; its exact
   statement should be taken from the manuscript, not from this summary.

Updated overall status: with Price's ranges (j <= 3i/2, and n = 2j) proved
in the original and accepted by the site, and Van Doorn-Rocca's ranges
(i in {1,2} closed, i >= 1476 closed, 4..1475 finite but ineffective),
a bad triple must have i = 3 with j >= 5 and n != 2j, or lie in the
ineffective finite band with j > 3i/2 and n != 2j. Problem #699 remains
open; i = 3 is the clean remaining infinite case.
