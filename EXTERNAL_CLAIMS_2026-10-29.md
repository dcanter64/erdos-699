# External claims on #699 found by Dennis on erdosproblems.com (2026-10-29)

Dennis retrieved these from the site himself (our automated fetches were
403-blocked). Files as uploaded: ~/workspace/user/files/488_paper_github.pdf
is #488; for #699: Wooter_Erdos_Problem_699.pdf (strict-variant paper),
Wooter_erdos_699.pdf (Partial Progress), Wooter_Erdos_699_audited_revision.pdf.

## Claim A: Van Doorn & Rocca, strict variant (p > i), submitted 2026-07-25
Title: "Binomial coefficients sharing a large prime divisor". Proof found by
ChatGPT 5.6 Sol per its AI declaration, human-rewritten by the authors.
Result: for i >= 4, only finitely many triples have largest prime factor of
gcd(C(n,i),C(n,j)) <= i; large-i theorem gives a common prime >= min(q, c i
log i). i = 3 explicitly untouched ("cannot even exclude G a power of two
infinitely often"). Finiteness for fixed i >= 5 is ineffective (BEG S-parts);
effective remark: no exceptions for i >= 1000 (details omitted).
Muse's spot checks (2026-10-29): pi(i) < i/4 verified on [121, 5000];
Bergman Lemma 2.1 bound held on 4,000 random triples plus edge cases
(tightest slack ~96,881x at (16,4,8)); no i=3 power-of-two gcd for n <= 2000;
smallest exhibits of largest-prime-factor exactly i: (10,3,5) G=12,
(16,2,6) G=8, (28,3,14) G=36.

## Claim B: Van Doorn & Rocca, "Partial Progress on Erdos Problem #699"
The >= i statement itself ("bad" = no prime q >= i dividing both). States it
follows Price [Pri26] throughout. Global structure:
- B_{1,2} = empty (elementary; agrees with our Cycle 1 unconditional closures).
- B_{>=1476} = empty: orbit polynomial + Jacobi discriminant bound
  G > (4n/27)^{i/4} K_i^{-1/(2i-2)}, confinement via pi(x) estimates
  (n < 4e18 for 1476 <= i < e^16; n < 6000i beyond), terminal prime from
  Oliveira e Silva gap tables (max gap 1476 below 4e18) and Axler's interval
  theorem for i >= e^16.
- B_{4..1475} finite but INEFFECTIVE (fat-point divisors: line arrangement
  for i >= 5 with rho_i < i-1; explicit line-conic Phi_4 of degree 17,
  multiplicity 6 for i = 4; then BEG S-part theorem).
- i = 3 OPEN. Their diagnosis: exponent-only arguments would need d/m < 2;
  a completion must retain the labels recording which of n, n-1, n-2 supplies
  each prime power (the r+s=t data), not just aggregate size. This matches
  our Cycle 1 crux (i = 3 via (LD3) splitting configurations).
- Prop. 2.4 is Price's j <= 3i/2 closure, and here the EEES78 exception
  pairs ARE discharged in writing: (9,4), (10,5) admit no admissible j; the
  other ten get a terminal-prime table ((8,3):7, (12,5):11, (21,7):19,
  (21,8):19, (30,7):29, (33,13):31, (33,14):31, (36,13):31, (36,17):31,
  (56,13):53). This fills, in this write-up, the exact gap REFEREE.md
  flagged in Bloom's exposition. Our referee verdict on the exposition
  itself stands as written.

## Audited revision (solo author: Stefano Rocca)
Same title/abstract/theorem and, on a full read, the same proofs, constants,
and tables as Claim B. Differences spotted: (1) sole authorship by Rocca;
(2) the Conclusion drops the clause "and an effective version of the
fixed-index finiteness statement" (Claim B: "Only the cubic boundary and an
effective version ... remain outside the proved statement for now";
revision: "Only the cubic boundary remains outside the proved statement").
The section 4.3 Effectivity paragraph is retained in both, so the document
as a whole still discloses ineffectivity; only the conclusion sentence is
trimmed. No theorem, constant, or proof step differs, so verification
results apply to both versions unchanged.

## Notes
- The forum summary Dennis pasted with Claim A (1475, Kummer localization,
  orbit polynomial) in fact describes Claim B; the forum listing appears to
  have paired that summary with Claim A's PDF.
- Combined status if both claims hold: #699 is reduced to i = 3 plus a
  finite, ineffective band at 4 <= i <= 1475. Still NOT solved. Our sweep
  (n <= 20,000, all i) and the 3,700,736 for-all-n cleared pairs remain the
  only explicit exclusions in the band.
- Muse's verification batch on Claim B's core (Phi_4 expansion, arrangement
  identity for all 5..1475, Kummer localization sampling, terminal-prime
  table, confinement arithmetic) was launched 2026-10-29 ~08:07 ET; results
  to be appended here when it lands.

## Muse's verification of Claim B's checkable core (2026-10-29, all exact)
- Phi_4 certificate: expanded symbolically; degree exactly 17; minimum
  vanishing order over all ten points of Delta_4 is exactly 6 (as claimed);
  conic Q passes through the six claimed points; 0 < Q(j,c) < n^2 held on
  2,000 random admissible spot checks.
- Line arrangement: for EVERY i in 5..1475, the minimum of
  (k-r)_+ + (k-s)_+ + (r+s-ell)_+ over Delta_i equals mu_i exactly, and
  rho_i = d_i/mu_i < i-1 strictly. Exhaustive, not sampled.
- Kummer localization lemma: 6,339 random instances, zero failures.
- Terminal-prime table: all ten (n,i,p) entries valid; (9,4) and (10,5)
  confirmed to admit no admissible j.
- Tail confinement arithmetic: pi(1475) = 233 exactly; RS bound 253.7 gives
  denominator 0.312 at i=1476 (claimed > 0.31); numerator caps 9.22 (at
  1476) and 11.91 (at e^10), both < 12; log n < 38.7 < log(4e18) = 42.83;
  linear regime: LHS 6.790 > 6.78 against RHS 6.631 < 6.64. Constants are
  tight but correct.
NOT covered by these checks: the Jacobi discriminant identity (5.1) itself
(its consequences' arithmetic was verified, not the identity), the BEG
S-part theorem and the Oliveira e Silva gap tables (both taken on citation
as published results), and Price's underlying argument beyond the exception
discharge (see REFEREE.md).

## Claim C: Price, "Common Prime Divisors of Binomial Coefficients" (GPT 5.6 Sol Pro)
The second forum claim; the site has ACCEPTED it as correct (per Dennis).
Proves the conjecture for j <= 3i/2 and for the central case n = 2j.
Contains Lemma 1.3 discharging the EEES78 exceptions with the same
terminal-prime table as Claim B, and an Appendix A with complete Python
code for the finite part of the central case. Muse ran that code:
666 checks pass, certificate reproduced exactly (see the REFEREE.md
addendum of 2026-10-29 for full detail). This manuscript is the source
Claims A and B both build on: Claim B's Prop. 2.4 is its j <= 3i/2
proposition, and its Lemma 2.2/Kummer machinery originates here.

## Comment thread (supplied by Dennis 2026-10-29; graded by Muse's checks)
Dennis's caveat stands: comments are not authoritative by default. Results
of Muse's verification of every checkable assertion:

- Marco Del Pin (24 Jul 2026): a Vandermonde-free variant of Price's
  argument. If C(2j,i) >= C(j,i)^2 then (n,i) outside EEES exceptions is
  good for all n >= 2j. VERIFIED: the ratio formula for
  F(j) = C(2j,i)/C(j,i)^2 is exact (300 random (i,j)); F is strictly
  decreasing; J1(3)=5, J1(5)=8, J1(640)=962, J1(5000)=7503, all exactly as
  stated (offsets 1,1,2,3 over floor(3i/2)); the 12 exception pairs admit
  exactly 29 triples satisfying the hypothesis and all 29 are good by
  direct gcd computation. Consequence: the pair (3,5) is settled for all
  n, and Price's range is extended by a growing margin (~log2(i)/4) at
  every i. His cap remark (size arguments through v^2 cap at 3/2) is a
  heuristic entropy statement, consistent with MaxDKaos's construction.
- MaxDKaos (25 Jul 2026; disclosed as written by Claude/Opus 5, machine-
  verified by a second implementation): the elementary bound
  U_i(n) <= n^{pi(i-1)} (same Kummer carry bound as Claim B's Lemma 5.4),
  giving exponent 1 - pi(i-1)/i -> 1, crossing EEES's 1/2 at i = 9
  (pi(8) = 4, 1 - 4/9 = 5/9; VERIFIED). Combined with a prime-free-interval
  condition and first-occurrence prime-gap data G(i), he tabulates settled
  j-ranges for all n: 5 (i=3), 12 (i=5), 30 (i=10), 138 (i=20), 25063
  (i=100), 713421 (i=200), 360654145 (i=394), plus an asymptotic
  j <= C i log^2 i via Dusart. CALIBRATION: Muse verified the lemma and
  the crossing, and computed G(3) = 9, G(5) = 27 from raw gaps; the CRUDE
  cut-off then settles only j <= 4 (i=3) and j <= 7 (i=5). The headline
  values use a "sharp form of the cut-off" not printed in the comment, so
  they are NOT independently reproduced here, except i=3's j <= 5, which
  Del Pin's verified lemma settles outright. If the sharp values hold,
  this criterion clears pairs far beyond our campaign's j <= 5000 scope
  (e.g. all j <= 25063 at i=100). Filed as a Cycle 2 input: reimplement
  independently (own sieve, own gap table, derive the sharp cut-off)
  before crediting the counts.
- Cong (06 Jan 2026): independent Rust verification to n = 10^7, no
  counterexamples, plus targeted n = 2^k (k <= 27) and n = 3^m + 1
  (m <= 17); repo github.com/conglu1997/erdos_699_rust. His complete list
  of strict-variant (p > i) failures in range: (10,(3,5)) gcd 12,
  (16,(2,6)) 8, (28,(3,14)) 36, (28,(5,14)) 1080, (244,(3,122)) 324,
  (512,(2,147)) 256, (2048,(2,713)) 1024, (2188,(3,1094)) 2916,
  (1594324,(3,797162)) 2125764 = 2^2 * 3^12. Muse verified ALL NINE gcd
  values exactly (factor C(n,i), Legendre valuations for C(n,j)). His
  sweep independently corroborates ours far beyond our range.
- Thread history: an earlier proof claim (Apr 2026, post deleted) was
  reviewed by Bloom and declared invalid on 11 May 2026 ("the Lean code
  is not formalising anything like the statement here"). The site's
  acceptance process has rejected claims before; Price's acceptance is
  not a rubber stamp.

## Site activity snapshot for #699 (supplied by Dennis 2026-10-29; these lists change)
- Likes: conglu, Dogmachine.
- Open to collaboration: conglu.
- Currently working on: conglu, Woett, ster.
- Looks difficult: Dogmachine. Looks tractable: none. Could be formalisable: none.
- Working on formalising: Woett.
Identity mapping (context-supported; the Woett one is an inference):
conglu = Cong, author of the independent Rust sweep to n = 10^7;
ster = Stefano Rocca, submitter of the Van Doorn-Rocca claims;
Woett is in all likelihood Wouter van Doorn (the "Wooter" spelling in the
uploaded filenames was Dennis's typo, corrected by him 2026-10-29). Note
the consistency: Woett "working on formalising" matches
the Van Doorn-Rocca note promising a Lean verification conditional on
results like [OeSHP14]. Conglu is the only participant flagged open to
collaboration.

## Literature statement supplied by Dennis 2026-10-29 (formal statement page)
Substance already in our file, with one new provenance anchor: the strict
variant's unique known counterexample at i >= 4, gcd(C(28,5), C(28,14)) =
2^3 * 3^3 * 5 = 1080, originates with Erdos and Szekeres themselves and is
catalogued as problem B31 in Guy's Unsolved Problems in Number Theory
(2004). Muse verified that gcd exactly on 2026-10-29 (from Cong's table),
and Cong's sweep to 10^7 found no other i >= 4 strict counterexample,
so the 1978 example remains the only one known across all three sources.
The same page records the Sylvester-Schur theorem as background and the
finitely-many-n-per-fixed-pair reduction.

## Submission mechanics (confirmed 2026-10-29)
Dennis recalled a submission form with a proof-link field; Muse confirmed
its shape from the site's other proof-claims forum threads. Each problem
has a forum "proof-claims" thread carrying a "Submit your own proof claim"
form (account required). Claims render with: claimant and AI used,
Summary, Notes, an "External link to proof", an optional "External link
to formalisation", and a submitted-by timestamp. Expositions are a
separate channel: message a moderator or email
erdosproblemsonline@gmail.com. So a future Canter submission needs a
public proof host (his GitHub) plus summary/notes text, all subject to
his explicit approval of the actual draft before anything is submitted.
Dennis confirmed 2026-10-29: he has a GitHub account and will create the
repo himself if and when the project produces something significant; the
repo creation is his step, at his trigger. Muse's part, when asked, is
the contents: exposition, code, and verification records ready to drop in.

## Submission route verified by live browser, 2026-10-29
Path: erdosproblems.com/699 -> "Proof claims (2)" ->
/forum/thread/699/proof-claims -> "Submit your own proof claim" ->
/forum/thread/699/submit-proof, which REQUIRES SIGN-IN: signed out, it
redirects to /forum/login (Dennis's browser showed it as a 404). The
login page itself warns there is currently NO password-reset ability, so
credentials for a site account must be kept carefully. Form fields past
the login gate were not inspected (no login performed). Forum rules
(fetched 2026-10-29): AI assistance must be disclosed; the human poster
must understand and have verified the mathematics themselves, or hold a
sorry-free Lean formalisation; long proofs belong in external links.
Comments are the low-gate contribution channel (Del Pin, MaxDKaos were
credited there), and problem pages carry "Additional thanks to" lines
naming contributors.
