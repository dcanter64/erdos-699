# Process and Disclosure

This document follows the spirit of the AGMAI guidance on responsible release of AI generated mathematics: scour and cite the literature, disclose the model and the process, state the compute and time costs, state how the problem was chosen and how much was attempted, and support human understanding of the release. It is the disclosure companion to README.md.

Produced by Meta Muse, prompted by Dennis Canter.

## What this is, and who directed it

This repository contains partial progress on Erdős Problem #699. The problem remains open, and nothing in this repository is a proof of the conjecture or a proof claim.

Dennis Canter, the human principal, selected Erdős #699 and directed the campaign: he set its scope, retrieved source texts from erdosproblems.com that automated fetching could not reach, and decided what would be packaged and when. The mathematics, the computation, and these documents were produced by Meta Muse through orchestrated subagents working under that direction. The site's rules for a proof claim are not met by this package, because the human principal has not personally verified the mathematics in the sense those rules require and no Lean formalisation exists; the intended channel is therefore a comment on the problem thread and handoff to interested mathematicians.

## Method

The campaign ran three proof cycles and two sweeps, all recorded in files in this repository.

Proof cycles. For each proof cycle, work was divided into clusters. Each cluster had two independent provers who did not see each other's work, and one independent verifier who classified every numbered claim in the prover documents as PROVED, GAP, FALSE, or OPEN. Coordinator reports (CYCLE1.md, CYCLE2.md, CYCLE3.md) were written only from verifier certified files. Claims that a verifier marked GAP, FALSE, or OPEN are reported as such in the cycle reports and are not used as results.

Sweeps. The sweep code (sweep/sweep.py and its companions) underwent an adversarial review before the extension run (sweep/REVIEW.md). The review found no silent miss and contradicted no claim in substance; its must fix items were applied and regression tested before the cap 20,000 run. A prediction for the cap 20,000 classification, 1,302,183 fully cleared pairs in the sub-scope i ≤ 1000, j ≤ 5000, was computed by the threshold method and recorded in sweep/threshold_prediction_20000.txt before the cap 20,000 classification completed; the completed classification matched it exactly.

Computation throughout was exact Python integer arithmetic, Python standard library only.

## AI disclosure

Model: Meta Muse. Process: an agentic fan out in which a coordinator briefed independent prover agents, verifier agents checked their work claim by claim, and further agents ran and recounted the computations; the coordinator then wrote reports only from the verifier certified files.

No human mathematician has refereed these results, and no Lean formalisation exists. No part of the results has been formalised in Lean, and formalisation is not being pursued unless a mathematician working on the problem asks for it.

## Compute and token costs

The token figures come from the ledgers TOKENS.md, TOKENS2.md, and TOKENS3.md in this repository. Their honesty caveat applies in full: the figures are estimates, order of magnitude only. Exact per-agent counts were not visible to the coordinators; the ledgers were built from run counts, document sizes, transcript lengths, and tool call volume.

* Cycle 1: approximately 1.6M to 3.4M tokens (order 2M), across 24 child runs.
* Cycle 2: approximately 1.5M to 2.8M tokens (order 2M), across 16 child runs.
* Cycle 3: approximately 2.1M tokens (range 1.7M to 2.6M), across 12 child runs.

The sweeps and enumerations were CPU computation in exact Python integer arithmetic, not token spend. The sweep record (sweep/RESULTS.md) gives the cap 10,000 sweep a combined elapsed time of about 5,208 seconds across two runs separated by a machine restart, on a 2 core virtual machine, and the cap 20,000 sweep ran from 2026-10-28 to completion on 2026-10-29 on the same class of machine, with the completing run resumed from 173 validated checkpoints. The Cycle 3 enumerations were likewise run on a shared 2 core virtual machine, and the wall times in the certified files are machine dependent (TOKENS3.md).

## How the problem was chosen, and scope

One problem was attempted in this campaign: Erdős #699, chosen by Dennis Canter from a scouting shortlist. The campaign ran three proof cycles and two sweeps (to n ≤ 10,000 and to n ≤ 20,000). A companion problem, Erdős #488, was considered in the same scouting and was parked by Dennis Canter's decision; it is out of scope, and none of its material is in this repository.

Failed and abandoned directions are part of the record. In Cycle 1, ten strategies (strategies/S1.md to S10.md) were written; four clusters were pursued in the prover round (CYCLE1.md section 2), and the remaining strategies were not selected for that round, though two of them later became Cycle 2 clusters. Results that did not hold up are reported as such: in particular, the published table of MaxDKaos, reimplemented independently in Cycle 2 (verification/maxdkaos_reimplementation.py and its report), did not reproduce under any tested reconstruction of the stated method; only the entry (3, 5) is credited, under one candidate reconstruction only.

## Error log (summary)

The full logs are in the cycle reports. The main errors the process found and corrected were:

Cycle 1 (full record in CYCLE1.md sections 5 and 6, and REFEREE.md).
* Bloom's exposition of the literature proof for j ≤ 3i/2 never names or discharges the 12 EEES78 exception pairs, and at an exception pair the key inequality fails in the opposite direction. The gap was closed externally by direct computation of all exception triples, and Price's manuscript was later found to discharge the pairs in writing.
* Strategy S5's proviso, that only one EEES78 exception triple lies in the boundary family, was found FALSE: there are two, and both were discharged in the proofs.
* Two further strategy level errors were caught by the provers and verifiers: a false observation in the coordinator's own brief for the prime gap strategy, and the bare form of strategy S4's Lemma 4, which is false in both directions and was repaired in corrected form.

Cycle 2 (full log in CYCLE2.md section 7).
* A factor of 2 proof error in one prover's monotonicity argument: the statement was true, the verifier supplied the corrected proof, and the closure was in any case subsumed by the other prover's certified result.
* A bibliographic mislabel: a theta bound cited as Dusart 2010 is Dusart 1999. Bibliographic only, with no mathematical effect.
* A citation correction for Rosser and Schoenfeld: the theta bound used in secondary quotation comes from their 1962 paper, not the 1975 paper the campaign's attribution had conflated it with. Nothing in Cycle 2 depends on it.
* Two coordinator brief errors: the sharp Kummer criterion was specified in an all-n form under which a validation anchor fails, where the validated form was always sweep relative; and a suggested lever for i = 3 based on largeness of v2(C(n, 3)) was backwards, since the closing side is v2 ≤ 3.

Cycle 3 (full log in CYCLE3.md section 8).
* Two claims in prover document P-J2 were found FALSE: a universal sentence refuted at the (4, 2) row, and a list of rows described as still open that were already closed by a combination available inside that document's own inputs.
* Prover document P-L2 had three defects, none load bearing, including its check script hanging as filed at n in {1, 2}; the verifier recounted its numbers independently in verification/V-L.md.
* Prover P-K2 disclosed one wrong preliminary pair count, caught by its own independent recount before the final run and confirmed superseded by the verifier.
* Two T value slips in the earlier record's row table: row (3, 4) has T = 8, not 7, and row (5, 2) has T = 10, not 8.
* One coordinator brief error: a parenthetical suggesting that a solution of the higher digit system (LD3⁺) is not a counterexample was wrong for the full system; the verifier flagged it and the cycle report corrects it.

Campaign discipline note. Twice, in Cycle 2 and again in Cycle 3, figures in interim agent summaries did not survive verification: the correct figures existed in the deliverable files, and the summaries alone were wrong. The standing rule adopted from that experience is that only verifier certified files are the record. This package is built from files for that reason, and every number in README.md traces to a certified file in this repository.

## Literature conduct

External claims were graded in EXTERNAL_CLAIMS_2026-10-29.md, claim by claim, keeping a verified versus cited distinction: a claim is marked verified only where this campaign checked it by its own computation or read the primary text, and cited where it rests on a published source taken on trust. Price's Appendix A code was run by this campaign (price_appendixA.py): its 666 endpoint checks reproduced exactly. Primary source verification of the key analytic citations used in Cycle 2 is in verification/primary_sources_c2.md, which records which citations were verified in the primary text, which stand at secondary verification level, and which labels needed correction.
