# Erdős Problem #699: Partial Progress

Partial progress on Erdős Problem #699, the statement that for 1 ≤ i < j ≤ n/2, the binomial coefficients C(n, i) and C(n, j) always share a prime factor ≥ i.

Produced by Meta Muse, prompted by Dennis Canter.

## Status

This repository records partial progress only. Erdős #699 remains open. This repository is not a proof of the conjecture and makes no proof claim, for the whole problem, for any region beyond the items listed below with their dependencies stated, or for the case i = 3. The intended channel for these results is a comment on the problem thread at erdosproblems.com and handoff to interested mathematicians, not a proof claim submission.

The results were produced by Meta Muse, an AI system run as orchestrated agents (independent provers and independent verifiers), at the direction of Dennis Canter, who selected the problem and directed the campaign. No human mathematician has refereed these results. No Lean formalisation exists. The full process record, including the error log and the cost ledgers, is in PROCESS_AND_DISCLOSURE.md. The campaign record files (CYCLE1.md to CYCLE3.md, and the proofs/, verification/, referee/, and strategies/ trees) are reproduced verbatim from the original record, including their original typography; the edited presentation layer is this README, the paper, REPRODUCE.md, and PROCESS_AND_DISCLOSURE.md, and those four documents are the ones held to the house style (including no em dashes).

## What is proved

Each item below carries its dependency label in brief. Full statements, proofs, and verifier classifications are in the cycle reports and in proofs/ and verification/.

* The region j ≤ 3i/2 is closed in the literature, as refereed by this campaign (dependency: modulo EEES78, with its 12 exception pairs discharged directly by computation). See REFEREE.md and EXTERNAL_CLAIMS_2026-10-29.md; Price's manuscript discharges the exception pairs in writing, and Price's Proposition 4.1 is used below.
* Regime R1 is closed: there is no counterexample with 3i/2 < j < 2i, for any i (dependency: modulo EEES78 and the cited explicit estimates, plus the completed sweep for the two pairs (4, 7) and (10, 19)). Combined with the previous item, the conjecture holds for all j < 2i. The line j = 2i is a separate case, treated in the next item.
* The line j = 2i is closed for i ≥ 1.2e8, via the strengthened EEES exponent θ_u ≤ 0.3262 (dependency: modulo EEES78 and the cited explicit estimates).
* The cases i = 1 and i = 2 are closed for all j and all n, and the boundary family j = ⌊3i/2⌋ + 1 is closed for all i and all n (dependency: unconditional).
* For i = 3, the subcase SPLIT-odd is closed: no i = 3 counterexample has n odd (dependency: two independent routes via Price's Proposition 4.1, with no EEES78 input).
* For i = 3, the whole band T ≤ 16 is closed, where T = R + 2(Q − 1) for n = Qj + R (dependency: the (LD3) reduction and the certified finite frontier; the stronger form proved is that (LD3) has no even solution in any of the 64 rows with T ≤ 16, for any j).
* For i = 3, the v2 condition is completely characterised: the set of n with v2(C(n, 3)) ≥ v is exactly five residue classes modulo 2^(v+1), for every v ≥ 2 (dependency: unconditional, proved in exact form in Cycle 3).
* For i = 3, every pair (3, j) with 5 ≤ j ≤ 50,000 is closed for all n (dependency: the standing finite reduction and the certified (LD3) enumeration described under computation below). The pairs with j ≤ 4 are covered by the j ≤ 3i/2 closure in the first item.

The consolidated paper is at paper/paper.tex (PDF: paper/paper.pdf). The cycle reports CYCLE1.md, CYCLE2.md, and CYCLE3.md are the audit record behind the paper.

## What is computation

All computation is exact integer arithmetic in Python, standard library only. REPRODUCE.md gives the commands.

* Sweep to n ≤ 10,000: 27,769,446,111 open region triples checked, 0 flagged. The closed form count of the same index set matches this total exactly.
* Sweep to n ≤ 20,000: 222,188,892,222 open region triples checked, 0 flagged. The closed form count matches exactly. An independent spot check of 300 seeded triples with n from 10,001 to 20,000 found all gcds greater than 1, 0 failures.
* Pair classification at cap 20,000: 33,330,000 pairs considered, 8,021,170 fully cleared. A prediction of 1,302,183 fully cleared pairs for the sub-scope i ≤ 1000, j ≤ 5000 was recorded in advance (sweep/threshold_prediction_20000.txt) and matched exactly.
* Audited clearance in the campaign scope (i ≤ 1000, ⌊3i/2⌋ < j ≤ 5000; 4,249,500 pairs): 3,919,306 pairs fully cleared by the audited chain of criteria, with 330,194 pairs remaining partial, all at rows 4 ≤ i ≤ 113.
* Cycle 3 enumerations for i = 3: the per-pair (LD3) frontier reached j ≤ 50,000, and (LD3) has zero survivors at even n ≤ 10^8, over 922,011,091 candidate pairs tested.

The large per-pair classification files pairpass.json (4.4 MB) and pairpass_20000.json (48 MB) are not in this repository; they are regenerable (see REPRODUCE.md) and their headline statistics are in sweep/RESULTS.md.

## What remains open

* The i = 3 residual: a counterexample, if one exists, must now have n even, n > 10^8, j ≥ 50,001, T ≥ 17, and satisfy the reconciled residual conditions (RES-3) stated in CYCLE3.md. The case i = 3 is not closed.
* The line j = 2i for i < 1.2e8, outside the sub-regions certified in Cycle 2.
* The region j > 2i beyond the certified sub-regions of Cycle 2.
* The general case. Erdős #699 remains open.

## Repository layout

* CYCLE1.md, CYCLE2.md, CYCLE3.md: the three proof cycle reports, written only from verifier certified files.
* REFEREE.md: the referee report on the literature closure of the region j ≤ 3i/2.
* EXTERNAL_CLAIMS_2026-10-29.md: the grading of external claims found on the problem thread, with the verified and cited distinction kept throughout.
* EXTERNAL_CLAIMS_ADDENDUM_2026-10-30.md: a graded addendum covering a later claim recorded in the erdosproblems.ai catalog (Plasma AI, 2026-10-19), graded as unverified, with its interaction with the results here spelled out.
* TOKENS.md, TOKENS2.md, TOKENS3.md: the run and token ledgers for the three cycles, with their honesty caveats.
* price_appendixA.py: Price's Appendix A code, run by this campaign (666 endpoint checks reproduced).
* paper/paper.tex (PDF: paper/paper.pdf): the consolidated paper style write-up of the partial results.
* proofs/: the prover documents P-A1 to P-L2 and their check scripts.
* verification/: the verifier reports V-A to V-L and V-U, their check scripts, counts_c2.py with counts_c2.md and counts_c2.json, maxdkaos_reimplementation.py with its report, and primary_sources_c2.md.
* referee/: the two referee reports and the coordinator checks behind REFEREE.md.
* strategies/: the ten strategy documents S1 to S10 from Cycle 1.
* texts/ACQUISITION.md: how the source texts were obtained, and what remained inaccessible.
* sweep/: the sweep record (RESULTS.md, REVIEW.md, PROVENANCE.md, PHASE0.md, stage2_design_notes.md), the sweep and classification code, the summary data files, the retained outputs, and the run logs sweep_10000.log and sweep_20000.log.

## How to cite

This work is free to use, with no conditions attached. If you do cite it, we would be grateful for credit in this form: Meta Muse, prompted by Dennis Canter. Title: Partial Progress on Erdős Problem #699. Repository documents CYCLE1.md to CYCLE3.md and sweep/RESULTS.md are the record of the results.

To cite the problem: T. F. Bloom, Erdős Problem #699, https://www.erdosproblems.com/699, accessed 2026-10-30.

## Reading further

REPRODUCE.md gives exact commands and expected outputs for every check that can be rerun, in increasing cost order, with honest notes on the expensive ones. PROCESS_AND_DISCLOSURE.md gives the method, the AI disclosure, the compute and token costs, and the error log.
