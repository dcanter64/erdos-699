# V-L: Independent verification of Cluster L (higher-digit Kummer refinement (LD3⁺) at $i=3$), Cycle 3

Verifier: V-L (independent). Files verified: `proofs/P-L1.md` (with
`proofs/P-L1_checks.py`) and `proofs/P-L2.md` (with
`proofs/P-L2_checks.py`), against `proofs/P-A1.md` (Lemma A1.15, the
(LD3) Definition, Proposition A1.16, Statement (H3)),
`proofs/P-F1.md` (F1.6(c), F1.9, F1.11), `proofs/P-F2.md` (F2.13,
F2.14), `verification/V-A.md`, `verification/V-F.md`, `CYCLE2.md` §2,
and — as a certified sibling result, cited but not re-verified —
`verification/V-I.md` (Cluster I).

Verifier's own computations (Python stdlib only, exact arithmetic;
implementations independent of both provers': own SPF sieve, own
digit code, own row enumerations in both parametrisations):
`verification/V-L_checks.py` (all sections completed, exit 0;
runtime 30.2 s uncontended). Running the provers' own scripts is
reported in §1 and is
**not** counted as independent verification anywhere below.

**Headline verdict. Verdict (b) is the correct label for BOTH files,
and the cluster's central claims are CERTIFIED.** Both provers'
formulation of (LD3⁺) quantifies over exactly the primes
$p \ge 3$ dividing $C(n,3)$ (checked in the files' own definitions,
not their summaries), and with that quantifier the following are
proved and independently confirmed: (i) on digits $0,\dots,a-1$ the
digitwise condition is **exactly** $j \bmod q \le r$ — neither
stronger nor weaker (the load-bearing fact is $r \le 2 < p$; the
verifier's test suite separates the two forms precisely outside that
hypothesis, at $p=2$, $r=2$); all new content of (LD3⁺) is the tail
condition $\lfloor j/q \rfloor \preceq_p (n-r)/q$ on digits $\ge a$;
(ii) $\mathrm{Sol}(\mathrm{LD3}^+)$ is **exactly** the set of
counterexamples, so (H3⁺) $\iff$ ($i=3$ closed), (H3) $\Rightarrow$
(H3⁺), and (H3⁺) $\Rightarrow$ (H3) is **OPEN**; (iii) no general
shrinkage of the residual class is proved by either file, and no
residual configuration is exhibited that (LD3⁺) excludes and (LD3)
does not. Every headline computation in both files was reproduced
exactly by the verifier's independent code (§§4–6): the 12
$\ge5$-only solutions to $10^6$ with the 8-of-12 $\ge5$-higher-digit
exclusions, the 4,711,997-instance census with all four sub-counts,
and both row parametrisations with their aggregate counts. Three
defects were found in P-L2, none load-bearing: the illustrative
parenthetical after Proposition L2.9 mislabels $w=0$ (it gives
$(30,15)$, not $(80,40)$ — that pair is $w=1$); Theorem
L2.15(iii)'s unqualified "(H3⁺) does not imply (H3) / strictly
stronger" overstates what is proved — the conditional dichotomy
inside it is proved, but strictness is exactly the OPEN statement
P-L1 records correctly in Claim L4.1(c); and P-L2's check script
as filed **hangs in §F1** (its `V3` loops forever at $n\in\{1,2\}$,
where $C(n,3)=0$), so its §F outputs are not reproducible from
the filed script in a single run — with two minimal small-$n$
guards the script completes and matches the file everywhere
except Method A's member list, which the file understates as
$\{6,10\}$ against the true $\{3,4,5,6,10\}$ (§1, §2.2). Every
§F number is in any case independently recounted in §6.2.
**$i=3$ is not closed, (H3)
and (H3⁺) are not proved, and #699 is not claimed solved — both
provers state exactly this, and the verifier concurs.**

---

## 1. The provers' own scripts, re-run (not independent verification)

* `proofs/P-L1_checks.py`: re-run by this verifier; **all assertions
  passed** ("ALL P-L1 CHECKS PASSED", 73.1 s on this machine; the
  file's stated 30.5 s is a machine-dependent runtime and immaterial).
  Output matches the text of P-L1.md in every particular checked:
  §A counts 84,526 (Kummer, $n\le300$) and 1,101,758 (low-digit
  equivalence, $n\le1000$), 0 failures; §B the six calibration pairs
  with the displayed witnesses; §C the three $p=3$ families,
  including the $\ge5$ witnesses for $3^a-1$ ($q=7,25,79,241,727,5,7$
  at $r=1$ for $a=2,\dots,8$ — agreeing digit-for-digit with
  P-L2's independently computed list in Computation L2.8(a));
  §D 26,035,963 pairs and exactly the 12 solutions with the
  per-solution classification; §E all ten row lines as printed in
  Computation L3.2; §E2 the (4,2) gcds 77, 69, 371; §F the
  $(30,15,5)$ example.
* `proofs/P-L2_checks.py`: re-run by this verifier. Sections A–E,
  re-run as filed, **all pass and match the text exactly**: §A
  38,809 pairs, 0 mismatches, no (LD3⁺) solutions; §B 1,101,758
  instances, 0 mismatches; §C the six calibration pairs with the
  gcd table (3, 9, 135, 81, 1215, 945) and the failing-digit lists
  of Computation L2.7, the $3^a+1$ tail-pass assertions, the
  $3^a-1$ witnesses, and the $2\cdot3^a+1$ $r=0$ witnesses; §D the
  $w=0,\dots,200$ family assertion and the instance counts
  4,711,997 / 4,182,943 / 225,801 / 303,253; §E Lemma L2.11
  validation, 0 violations. **Section F as filed does not
  terminate** — a genuine defect, found by this verifier: §F1's
  `memA` evaluates the script's `V3(n)` at every candidate
  $n = o\cdot2^s \le 10^8$ with $o \in \{1,3,9,5,15,45\}$, including
  $n = 1$ and $n = 2$, where $C(n,3) = 0$ and the filed
  `while c % 2 == 0: c //= 2` loop spins on $c = 0$ forever
  (demonstrated directly: `V3(2)` under the filed definitions does
  not return within a 5 s timeout; the verbatim §F1 snippet does
  not return within 8 s; behind the hang, `15 % V3(n)` would in
  any case divide by zero at those $n$). So the §7 log's claim
  that the script as filed asserts every headline value in
  942.9 s is **not reproducible as filed** — the prover's §F
  numbers must have come from a working variant with a small-$n$
  guard. With exactly two minimal guards added in a temporary
  copy (the filed script untouched; return 0 at $C(n,3)=0$, and
  restrict `memA` to $n \ge 3$), the script runs to "ALL CHECKS
  PASSED" in 6.4 s and its §F outputs match the file in every
  particular **except one**: Method A's $V_3(n) \mid 15$ member
  list, which the script prints as $[3, 4, 5, 6, 10]$ against the
  file's $\{6, 10\}$ (see the L2.12 row of §2.2). Independently of
  any re-run, **every** §F number in the file was reproduced by
  the verifier's own code (§6.2), so no §F claim in this report
  rests on the script's provenance.
* **P-L2's corrected census (task item 1, second half).** The task
  brief states that P-L2's script was correct while its prose census
  was wrong and was corrected in-file. The verifier grepped every
  occurrence of every census figure in the current `P-L2.md`: the
  total 4,711,997, low fails 4,182,943, low-pass/tail-pass 225,801,
  low-pass/tail-fail 303,253, low-passing total 529,054, and 57.3%
  appear identically in the headline, Computation L2.10, Claim
  L2.16, the §6 closing statement, and the §7 verification log; the
  aggregate row figures 1,942 / 79 likewise appear identically in
  Computation L2.14, §6, and §7. No stale pre-correction figure
  survives anywhere in the file. The verifier's independent recount
  (§5) confirms these current numbers are the correct ones.

## 2. Claim-by-claim tables

### 2.1 P-L1

| Claim | Status | Verifier's note |
|---|---|---|
| Lemma L1.1 (support characterisation) | **PROVED** | Proof audited ($6C(n,3)=n(n-1)(n-2)$; $p\ge5$: $v_p=a$; $p=3$: $v_3=a-1$). Independently recomputed for all $n\le2000$ (§3 of the verifier's script): exponent of every $p\ge5$ in $C(n,3)$ equals its exponent in the unique top; $3\mid C(n,3)$ iff $v_3(\text{top})\ge2$. |
| Lemma L1.2 (low digits = (LD3)) | **PROVED** | Proof audited line by line; the equivalence rests on $r<p$, used in both directions. Computational stress in §3 below: 0 separations in-domain; separations occur exactly out-of-domain. |
| Definition L1.3 ((LD3⁺)) | **PROVED** (definition correct) | Quantifier checked in the file itself: "for every prime $p\ge3$ dividing $C(n,3)$" — the full prime set, no truncation. The ($\alpha$)/($\beta$) split is correct digit bookkeeping ($n=qU+r$, $\lfloor n/q\rfloor=U$, $p\nmid U$ so digit $a$ has nonzero right-hand side). |
| Theorem L1.4 (necessity; (LD3⁺)⇒(LD3)) | **PROVED** | (a) is Kummer applied at exactly the primes of Lemma L1.1; (b) is ($\alpha$) at each relevant $q$. |
| Claim L1.5 (strictness) | (a) **PROVED** (per-prime, by example); (b) **OPEN**, correctly labelled | (a) Recomputed: $30=(0,1,1)_5$, $15=(0,3,0)_5$; low passes ($15\bmod5=0$), digit 1 fails ($3>1$); $j=5$ passes both at the same $(n,p)$. This is per-prime predicate strictness only, as the file states. (b) $\mathrm{Sol}(\mathrm{LD3})\setminus\mathrm{Sol}(\mathrm{LD3}^+)\ne\emptyset$ is open; no (LD3) solution is known at any $n$. |
| Theorem L2.1 ($p=3$ conditions, all cases) | **PROVED** | Specialisation of Definition L1.3/Lemma L1.2 at $p=3$; the three cases $r_3=0,1,2$ and the $a_3=1$ vacuity are all correct. |
| Claim L2.2 ($v_3=1$: no content) | **PROVED** | Immediate from Lemma L1.1; independently confirmed in the §3 support check. |
| Claim L2.3 (family $3^a+1$: $p=3$ high passes) | **PROVED** | $\lfloor j/3^a\rfloor=0\preceq_3 1=U_3$ for all $a\ge2$; the low clause fails ($j=(3^a+1)/2>1$). Script §C confirms $a=2,\dots,12$. (LD3⁺) excludes this family only through the (LD3) $3$-clause it already had. |
| Claim L2.4 (shapes $3^a-1$, $2\cdot3^a+1$) | **PROVED**, computation confirmed | (a) $v_3(n-2)=1$ for $n=3^a-1$ (since $3^{a-1}-1\equiv-1\pmod3$): no $p=3$ condition at all; script §C witnesses at $\ge5$ primes agree with P-L2's list. (b) At $n=2\cdot3^a+1$, $j=3^a$: low passes ($0\le1$), high passes ($1\preceq_3 2$); exclusion at an $r=0$, $\ge5$ witness (script §C: $q=19,5,163,487,1459$'s prime powers, …). The odd-$n$ remark is correct. |
| Computation L2.5 ($\ge5$-only census to $10^6$) | **PROVED** (computation, fully recounted) | §4 below: verifier's independent recount reproduces 26,035,963 pairs, exactly the 12 solutions, the 8-of-12 $\ge5$-higher exclusions with the identical excluding-prime lists, and all-12 $p=3$ high-pass / low-fail. |
| Lemma L3.1 ($n-1\mid 3\Lambda_3(T)$, $h=0$, $n$ even) | **PROVED** | Full audit in §6.1. The $p\ge5$ parts of $n-1$ are exactly the $p$-parts of $V_3(n)$; the $3$-part costs exactly one factor 3 ($3^{b-1}\mid\Lambda_3(T)$, so $3^b\mid3\Lambda_3(T)$, including the $b=1$ case where the $V_3$ 3-part is 1). Numeric form stress-tested: 0 violations for even $n\le5000$ at seven $T$ values. |
| Computation L3.2 (ten $h=0$ rows) | **PROVED** (computation, fully recounted) | §6.2: every row line reproduced exactly by the verifier's independent implementation (candidate counts, in-row counts, all 23 $V$-passer lists, (LD3) and (LD3⁺) survivor counts 0). Exhaustiveness for all $n$ follows from Lemma L3.1 ($3\Lambda_3(T)+1\le43{,}648{,}606<10^8$ in these rows), as stated. |
| Claim L3.3 ((4,2) row; status of the disposals) | **PROVED** as a summary | (4,2) candidates exactly $(22,5),(46,11),(106,26)$, all (LD3)-failing, gcds 77/69/371 recomputed (agreeing with V-F §5). Every $V$-passer in §3 has $j\le96\le5000$, hence lies in the certified per-pair frontier — the "diagnostic, not closural" characterisation is accurate. |
| Claim L4.1 (logical relations) | **PROVED**, including the correction | (a) Sol(LD3⁺) = counterexamples: both directions audited (§3 below); the quantifier in Definition L1.3 is over **all** $p\mid C(n,3)$, $p\ge3$, so no downgrade is needed. (b) (H3⁺) $\iff$ ($i=3$ closed) follows. (c) The brief's parenthetical is indeed FALSE for the full system; (H3) $\Rightarrow$ (H3⁺) by Theorem L1.4(b), and the converse is correctly labelled **OPEN**. (d) (N1)/(N2) are used nowhere in the digit route — verified by inspection of the proofs. |
| Claim L4.2 (verdict (b)) | **PROVED** as a statement of what the file establishes | The evidence (i)–(iii) is as audited above; the stopping point is stated exactly (see §8). |
| Claim L5.1 (summary) | **PROVED** as a summary | Matches the audited claims; open items correctly **OPEN**. |

### 2.2 P-L2

| Claim | Status | Verifier's note |
|---|---|---|
| Lemma L2.0 ($\mathcal{P}(n)$ = support of $V_3(n)$) | **PROVED** | Same computation as P-L1's Lemma L1.1, independently recomputed ($n\le2000$, 0 failures). |
| Definition L2.1 ((LD3⁺)) | **PROVED** (definition correct) | Quantifier checked in the file itself: every $p\in\mathcal{P}(n)$, every $e\ge0$ — by Lemma L2.0 this is exactly "every prime $p\ge3$ dividing $C(n,3)$". No smaller prime set is used anywhere downstream. |
| Lemma L2.2 (low part = (LD3)) | **PROVED** | Proof audited; the contrast example in the precision remarks is correct ($p=5$, $a=2$, $j\bmod25=6$ has digits $(1,1)$), and matches the verifier's out-of-domain separations (§3). Script §B count 1,101,758 instances, 0 mismatches — the same exhaustive design and count as P-L1's §A2, independently arrived at. |
| Theorem L2.3 (necessity; (LD3⁺) = (LD3) ∧ tails) | **PROVED** | (i) Kummer at $p\in\mathcal{P}(n)$; (ii) via Lemma L2.2; (iii) the digit-shift bookkeeping $\lfloor n/q_p\rfloor=K_p$ is correct, including digit $a_p$: $j_{a_p}(p)\le K_p\bmod p$. |
| Theorem L2.4 ((LD3⁺) ⟺ counterexample) | **PROVED** | Both directions are the prime-by-prime reading of $\gcd(V_3(n),C(n,j))=1$ via Lemma L2.0 and Kummer. Script §A confirms on 38,809 pairs, $n\le400$, 0 mismatches (re-run, §1; the statement is proved, the computation is corroboration). |
| Proposition L2.5 ($p=3$ digits, all cases) | **PROVED** | (i) $a_\tau=1$: no condition — correct, and load-bearing for Computation L2.8(a). (ii) The three low forms are $j\bmod 3^{a_\tau}\le\tau$ rewritten. (iii) The parity examples verify: $n=18$ ($v_3(n)=2$), $n=10$ ($v_3(n-1)=2$), $n=20$ ($v_3(n-2)=2$), all even. |
| Proposition L2.6 (family $3^a+1$ at $p=3$) | **PROVED** | Ternary expansions verified symbolically and in the re-run script §C3 ($a=2,\dots,12$): $j$ fails at exactly the low positions $0,\dots,a-1$ and the tail passes. Same conclusion as P-L1 Claim L2.3, by a digit-explicit route. |
| Computation L2.7 (calibration six) | **PROVED** (computation, spot-recounted) | The six pairs reproduced by both provers' scripts and by the verifier's §4 recount (they are the first six of the 12). The gcd column recomputed exactly by the verifier: 3, 9, 135, 81, 1215, 945 — all match. The failing ternary digits are exactly the low positions in each case. |
| Computation L2.8 (other shapes) | **PROVED** (computation, confirmed) | (a) $3^a-1$: valuations $(0,0,1)$ and the first (LD3) witnesses ($7,25,79,241,727,5,7$ at $r=1$) agree with P-L1's independent script §C output exactly. The redundant $p=5$ tail failures at $a=4,5$ are confirmed in the re-run script §C4 failure lists ($a=4$: $\{5:[1],\,79:[0]\}$; $a=5$: $\{5:[1],\,241:[0]\}$ — position 1 at $p=5$ with the $p=5$ low clause passing, the pair already killed at the large prime). (b) $2\cdot3^a+1$ with $j\in\{\lfloor n/3\rfloor,\lfloor n/2\rfloor\}$: killed at $r=0$ — consistent with P-L1 Claim L2.4(b) for the shared choice $j=3^a=\lfloor n/2\rfloor$. |
| Proposition L2.9 ($p=5$ strictness family) | **PROVED** as a per-prime statement; one **FALSE** illustrative parenthetical (immaterial) | Proof audited and re-verified for $w=0,\dots,200$ plus spot $w=500,1000,5000$ (§5.2): $v_5(n)=1$, low passes, digit 1 is $3>1$. **Defect:** the text after the proof says "$w=0$ gives $(80,40)$, killed by $q=79$ at $r=1$" — $w=0$ gives $(30,15)$; $(80,40)$ is $w=1$ (and for $w=1$ the $q=79$ remark is correct). An index slip in an example explicitly not claimed to satisfy the other primes' clauses; the proposition and its proof are unaffected. Adjudication vs P-L1 in §5.2. |
| Computation L2.10 (instance census) | **PROVED** (computation, fully recounted) | §5.1: verifier's independent implementation reproduces all four numbers exactly (total 4,711,997; low fails 4,182,943; low-pass/tail-pass 225,801; low-pass/tail-fail 303,253; 57.3%). Instance definition taken from the file's script §D2: $(n,j,p)$, $7\le n\le2000$, $3<j\le n/2$, $p\in\mathcal{P}(n)$ via the relevant prime powers; low via $j\bmod q_p\le\rho$; tail digitwise on $\lfloor j/q_p\rfloor$ vs $K_p$. |
| Lemma L2.11 ($h=0$ row finiteness) | **PROVED** | Full audit in §7. |
| Computation L2.12 ((2,4) two ways) | **PROVED** (computation, fully recounted) with one minor **FALSE** sub-statement | §6.2: Method A: 146 candidates — but the $V_3(n)\mid15$ members among them are exactly $\{3,4,5,6,10\}$ ($V_3$ values $1,1,5,5,15$; verifier-recomputed, and the guarded re-run of the prover's own §F1 prints the same list), **not** $\{6,10\}$ as the file states. The file's conclusion is unaffected: no member lies in the row with $j>3$ ($6\mapsto j=1$, $10\mapsto j=3$; $3,4,5$ are not in the row at all), so Method A's disposal stands. Method B: $\mathcal{F}(15)=\{1,3,5,9,15,45\}$, stage 1 exactly $(16,6),(46,21)$, stage 2 count 0 (both fail the $V$-filter itself: $V_3(16)=35$, $23\mid V_3(46)$). Global bound $n\le46$ makes the $10^8$ range exhaustive, as stated. The §F script defect behind this item is recorded in §1. |
| Computation L2.13 ((2,6), (3,4), (4,2)) | **PROVED** (computation, fully recounted) | §6.2: stage counts $7\to1\to0$ and $6\to1\to0$ reproduced with the identical candidate lists; the single stage-2 pairs $(16,5)$, $(16,4)$ are (LD3)-killed at low digits, as stated. (4,2): the three candidates, (LD3) witnesses, and gcds 77/69/371 all recomputed. |
| Computation L2.14 (aggregate $h=0$ sweep) | **PROVED** (computation, fully recounted) | §6.2: 70 rows ($Q\in\{2,\dots,8\}$, $T\le20$), stage 1 total 1,942, stage 2 total 79, largest stage-2 $n=210$, $j=96$, (LD3) survivors 0, (LD3⁺) survivors 0 — all reproduced exactly. The honesty note (all stage-2 pairs have $j\le96$, already frontier-closed) is correct. |
| Theorem L2.15 (logical relations) | (i), (ii), (iv) **PROVED**; (iii) **GAP** (overlabelled) | (i) (H3) $\Rightarrow$ (H3⁺): inclusion. (ii) (H3⁺) $\iff$ ($i=3$ closed): Theorem L2.4. (iv) (N1)/(N2) redundant given (LD3⁺), independent of (LD3): correct. **(iii)** The proved content is the dichotomy: *any* (LD3) solution is a counterexample or is killed by some $\mathrm{Tail}(p)$ — that is proved. But the heading's unqualified "(H3⁺) does **not** imply (H3)" and "(H3) is **strictly** stronger" assert a proved non-implication, which would require an (LD3) solution that is not a counterexample; none is known, and by L2.15's own dichotomy producing one is equivalent to separating the systems. The correct status, as P-L1 Claim L4.1(c) states it, is: (H3⁺) $\Rightarrow$ (H3) is **OPEN**. Same overstatement in the headline's "(while (H3) is strictly stronger)" and §6 item 3's "(H3⁺) $\nRightarrow$ (H3)". Minor: nothing downstream uses strictness — Claim L2.16's verdict needs only the dichotomy and the census evidence. |
| Claim L2.16 (verdict (b)) | **PROVED** as a statement of what the file establishes, with the L2.15(iii) caveat | The per-prime strictness and the zero marginal effect on delimited populations are as audited; the stopping point (§8) is stated exactly. Options (a) and (c) are correctly rejected. |

## 3. The low-digit equivalence and the support/Kummer boundaries (task items 2–3)

**Proof audit (Lemma L1.2 / Lemma L2.2).** Both files give the same
proof, and it is sound. Since $q=p^a\Vert(n-r)$ and $0\le r\le2<q$,
$n\bmod q=r$; since $r<p$, the lowest $a$ base-$p$ digits of $n$ are
$(r,0,\dots,0)$. Forward: digitwise-$\le$ on those digits forces
$j$'s digit 0 to be $\le r$ and digits $1,\dots,a-1$ to be 0, so
$j\bmod q\le r$. Backward: $j\bmod q\le r<p$ means $j\bmod q$ is a
single base-$p$ digit, so $j$'s digits $1,\dots,a-1$ vanish and
digit 0 is $\le r$. The hypothesis $r<p$ is used in the backward
direction essentially, and both files say so (P-L2 with an explicit
contrast example).

**Computational stress (verifier's script §2, independent code).**
* Abstract form, exhaustive: for every prime $3\le p\le50$, every
  $a\le4$ with $q=p^a\le2500$, every $r\in\{0,1,2\}$, and **every**
  $t<q$ (53,754 cases): digitwise-on-$a$-digits $\iff t\le r$,
  **0 failures**. For $q>2500$ up to $50^4$: strided sampling plus
  all boundary values $t\in\{r,r+1,p-1,p,p+1,q-1\}$ (61,908 cases),
  **0 failures**.
* Out-of-domain boundary: at $p=2$, $r=2$ (where $r<p$ fails), $t=2$
  satisfies $t\le r$ but violates digitwise at digit 1, for every
  $a\in\{2,3,4\}$ — the two formulations **do** separate exactly
  where the hypothesis is dropped, confirming the subtle point is
  real and the proofs' use of it is necessary, not decorative.
* In situ: for all $n\le3000$, all $3<j\le n/2$, all relevant $q$
  (10,961,518 instances, with $n\bmod q=r$ holding throughout):
  digitwise on digits $0,\dots,a-1$ $\iff j\bmod q\le r$,
  **0 failures**. (Both provers' exhaustive $n\le1000$ count,
  1,101,758 instances, 0 mismatches, was reproduced by their re-run
  scripts; the verifier's larger sample is independent code.)

**Equivalence Sol(LD3⁺) = counterexamples (task item 3).** Audited
in both files with the boundaries checked individually:
(a) For $p\ge5$: $p\mid C(n,3)$ iff $p$ divides a top number, and
$v_p(C(n,3))=v_p(\text{top})$ since $p\nmid6$ and $p$ divides
exactly one top — recomputed for all $n\le2000$, 0 failures.
(b) For $p=3$: $v_3(C(n,3))=a_3-1$ for the unique 3-divisible top,
so $3\mid C(n,3)$ iff $a_3\ge2$ — recomputed for all $n\le2000$,
0 failures. (LD3⁺) as formulated in **both** files imposes no
condition at $p=3$ when $a_3=1$ (Definition L1.3 quantifies over
primes dividing $C(n,3)$; P-L2's $\mathcal{P}(n)$ excludes 3 exactly
then, Proposition L2.5(i)) and the full digitwise condition when
$a_3\ge2$ (Theorem L2.1 / Proposition L2.5(ii)) — the correct
behaviour in both cases.
(c) Kummer's direction: $p\nmid C(n,j)$ iff $j\preceq_p n$ —
spot-checked exhaustively for $n\le250$ over all top primes
(66,814 instances, 0 failures), in addition to both provers'
$n\le300$/$n\le400$ exhaustions.
(d) The quantifiers: read in the files themselves (Definition L1.3;
Definition L2.1 with Lemma L2.0), both quantify over **all**
$p\ge3$ with $p\mid C(n,3)$. Hence the equivalence claim stands at
full strength in both files: Sol(LD3⁺) = counterexamples,
(H3⁺) $\iff$ ($i=3$ closed), (H3) $\Rightarrow$ (H3⁺), converse
OPEN (P-L2's L2.15(iii) wording notwithstanding, §2.2).

## 4. P-L1's $\ge5$-only census to $10^6$ (task item 4)

Verifier's independent recount (script §4: own SPF sieve,
$R_5(n)$-candidate method — $j$ ranges over multiples of
$R_5(n)=\prod_{p\ge5}p^{v_p(n)}$ in $[4,n/2]$, the $r=1,2$ clauses
tested per prime power, the 3-clause dropped, exactly the file's
system): **26,035,963 candidate pairs tested — P-L1's count
reproduced exactly** — and **exactly 12 solutions**:
$(10,5),(28,14),(82,41),(162,70),(244,122),(730,365),(2188,1094),
(6562,3281),(19684,9842),(59050,29525),(177148,88574),
(531442,265721)$, i.e. $n=3^a+1$, $j=n/2$ for $a=2,\dots,12$, plus
$(162,70)$. No count difference to reconcile.

Classification, recomputed per solution: **all 12 fail the $p=3$
low clause** (at $r_3=1$ for the eleven family members; at
$r_3=0$, $q=81$ for $(162,70)$) and **all 12 pass the $p=3$ high
subcondition** ($\lfloor j/3^{a_3}\rfloor=0$ in every case).
**Exactly 8 are excluded by $\ge5$ higher digits alone**, with the
excluding primes identified independently by the verifier and
matching P-L1's list prime-for-prime: $(82,41)$ at $p=5$;
$(162,70)$ at $p=5,7$; $(730,365)$ at $p=5$; $(6562,3281)$ at
$p=17,41$; $(19684,9842)$ at $p=7$; $(59050,29525)$ at $p=5,61$;
$(177148,88574)$ at $p=67$; $(531442,265721)$ at $p=5,7,13,41,73$.
The remaining four — $(10,5),(28,14),(244,122),(2188,1094)$ — have
no $\ge5$ full-digitwise failure, so their (LD3⁺) exclusion rests
solely on the $p=3$ low clause. Since all $\ge5$ low clauses pass
for these pairs by construction, every $\ge5$ full failure is
necessarily a tail (digits $\ge a$) failure: the "higher digits
alone" wording is exact. Computation L2.5 is certified, including
its own caveat that this is strictness on the $\ge5$ **subsystem**,
not an (LD3) solution killed by a tail.

## 5. P-L2's census and $p=5$ family (task items 5–6)

### 5.1 Instance census, $n\le2000$ (Computation L2.10)

Instance definition taken from P-L2's file/script §D2 (not assumed):
an instance is $(n,j,p)$ with $7\le n\le2000$, $3<j\le n/2$,
$p\in\mathcal{P}(n)$ (one instance per relevant prime power of the
tops); "low" is $j\bmod q_p\le\rho(p)$; "tail" is digitwise
$\lfloor j/q_p\rfloor\preceq_p K_p$, $K_p=(n-\rho)/q_p$, tested
digit by digit. The verifier's independent implementation
reproduces **every** figure exactly:

| | P-L2 (current file) | Verifier |
|---|---:|---:|
| total instances | 4,711,997 | 4,711,997 |
| low fails | 4,182,943 | 4,182,943 |
| low passes, tail passes | 225,801 | 225,801 |
| low passes, tail fails | 303,253 | 303,253 |
| low-passing total | 529,054 | 529,054 |
| tail decisive among low-passing | 57.3% | 57.32% |

The file's current (corrected) numbers are the script's numbers at
every occurrence (§1). Computation L2.10 is certified.

### 5.2 Proposition L2.9 and the strictness adjudication

The family $n=50w+30$, $j=25w+15=n/2$ at $p=5$: $n=5(10w+6)$ with
$10w+6\equiv1\pmod5$, so $v_5(n)=1$, $\rho=0$, low clause passes
($5\mid j$); digit 1 compares $\lfloor j/5\rfloor\bmod5=3$ against
$\lfloor n/5\rfloor\bmod5=1$ — tail fails. Re-verified by the
verifier for $w=0,\dots,200$ (the file's stated range) plus spot
$w=500,1000,5000$: holds throughout. (The $w=0$ parenthetical
defect is recorded in §2.2.)

**What kind of strictness this is:** per-instance / per-prime. It
shows the (LD3⁺) condition **at a single prime** is strictly
stronger than the (LD3) clause at that prime, with both outcomes
realised under identical low data (P-L1's Claim L1.5(a) example
makes the same point at $(30,5)$). It does **not** exhibit a pair
satisfying (LD3) as a whole system that (LD3⁺) excludes: the family
members are not claimed to pass the other primes' low clauses, and
Computation L2.10's 303,253 tail-decisive instances are likewise
single-prime instances inside pairs whose other clauses may fail.
**There is therefore no conflict with P-L1's Claim L1.5(b)**:
system-level extensional strictness,
$\mathrm{Sol}(\mathrm{LD3})\setminus\mathrm{Sol}(\mathrm{LD3}^+)
\ne\emptyset$, remains **OPEN** — the two files are talking about
two different levels, both label their level correctly (P-L2's
Claim L2.16 says "strictly stronger *as a condition* — proved per
prime"), and the only place the distinction blurs is P-L2's
L2.15(iii) "strictly stronger" phrasing for (H3) vs (H3⁺), flagged
in §2.2. P-L1's Computation L2.5 adds the intermediate level:
strictness is exhibited on the $\ge5$ subsystem (8 of its 12
solutions tail-killed), still not on the full system.

## 6. Row enumerations (task item 7)

### 6.1 Lemma L3.1 audit

Statement: in an $h=0$ row ($R\ge3$, so Proposition 4.1 gives
$V_3(n)\mid\Lambda_3(T)$), a counterexample with $n$ even satisfies
$n-1\mid3\Lambda_3(T)$. Proof audit: $n-1$ is odd. For $p\ge5$ with
$p^a\Vert n-1$, $p^a$ is exactly the $p$-part of $V_3(n)$ (unique
top, $p\nmid6$), hence divides $\Lambda_3(T)$. For $p=3$ with
$3^b\Vert n-1$: if $b=0$ there is nothing; if $b\ge1$ then $n-1$ is
the unique 3-divisible top, the 3-part of $V_3(n)$ is $3^{b-1}$
(with $3^0=1$ when $b=1$), so $3^{b-1}\mid\Lambda_3(T)$ and
$3^b\mid3\Lambda_3(T)$. Pairwise coprimality assembles the parts.
Sound, including the $b=1$ edge. The remark that the odd part of
$n$ likewise divides $3\Lambda_3(T)$ is also correct and is what
P-L1's parametrisation uses. This is a Proposition 4.1 consequence,
not an (LD3⁺) consequence, as the file itself notes.

### 6.2 Both parametrisations, recounted

The parametrisations differ by design: P-L1 enumerates **$n$** by
its odd part (odd divisors of $3\Lambda_3(T)$, times powers of 2,
to $10^8$) and then filters by the row, by $V_3(n)\mid\Lambda_3(T)$,
by (LD3), by (LD3⁺). P-L2 enumerates **$n-1$** by Lemma L2.11's
finite set $\mathcal{F}(\Lambda_3(T))$ (stage 1: in-row, $j>3$),
then the same $V$-filter (stage 2), then (LD3)/(LD3⁺). Stage-1 /
in-row counts therefore measure different candidate sets and are
**not** expected to agree; the $V$-passing sets and survivor counts
must, and do.

**The (2,4) row in both parametrisations (verifier's independent
implementations of each):**
* P-L1 form: 6 odd parts, 146 candidate $n\le10^8$, 135 in-row,
  **0** with $V_3(n)\mid15$ — the row is empty already at the
  Proposition 4.1 filter. (Over the 146 candidates at any $j$, the
  $V_3(n)\mid15$ members are $n=3,4,5,6,10$; none is in-row with
  $j>3$ — $6\mapsto j=1$, $10\mapsto j=3$. This corrects P-L2's
  Method A member list $\{6,10\}$; see §2.2.)
* P-L2 form: $\mathcal{F}(15)=\{1,3,5,9,15,45\}$, stage 1 exactly
  $(16,6),(46,21)$ — count **2**; stage 2 **0** (both fail the
  $V$-filter itself). Global bound $n\le46$.
* Reconciliation: P-L1's 135 in-row candidates include all $n$ with
  admissible odd part, most of which the $n-1$ condition of Lemma
  L3.1/L2.11 excludes a priori; P-L2's stage 1 applies that
  condition first, leaving 2. Both then find the same thing: no
  $V$-passer in the domain, (LD3) tested on 0 candidates, (LD3⁺)
  survivors 0. Headline counts differ because the funnels differ;
  the shared conclusion is identical and confirmed.

**P-L1's ten rows (Computation L3.2), all reproduced exactly:**

| row | cand. $n$ | in-row | $V$-pass | (LD3) | (LD3⁺) |
|---|---:|---:|---:|---:|---:|
| (2,4) | 146 | 135 | 0 | 0 | 0 |
| (2,3) | 146 | 2 | 0 | 0 | 0 |
| (2,5) | 275 | 7 | 0 | 0 | 0 |
| (3,3) | 275 | 173 | 0 | 0 | 0 |
| (2,6) | 275 | 257 | 1: $(16,5)$ | 0 | 0 |
| (3,4) | 275 | 45 | 1: $(16,4)$ | 0 | 0 |
| (2,16) | 2113 | 1974 | 5 | 0 | 0 |
| (2,17) | 3683 | 245 | 3 | 0 | 0 |
| (2,18) | 3683 | 3415 | 9 | 0 | 0 |
| (3,16) | 3683 | 529 | 4 | 0 | 0 |

$V$-passer lists match P-L1's printed lists pair-for-pair
(including $(2,18)$'s $(210,96)$, the largest, $j=96$). **Total
$V$-passers: 23, all killed by (LD3), zero reaching (LD3⁺)** —
confirmed.

**P-L2's rows (Computations L2.12–L2.14), all reproduced exactly:**
(2,6): stage 1 = the 7 listed candidates, stage 2 = $(16,5)$,
(LD3)-killed at $q=7\Vert(n-2)$ (low digit). (3,4): stage 1 = the
6 listed, stage 2 = $(16,4)$, (LD3)-killed at $q=5,7$ (low digits).
Aggregate over all 70 $h=0$ rows with $Q\in\{2,\dots,8\}$, $T\le20$:
**stage 1 total 1,942; stage 2 total 79; largest stage-2 $n=210$,
$j=96$; (LD3) survivors 0; (LD3⁺) survivors 0** — the verifier's
totals match, and the stage-2 maximum $(210,96)$ is the same pair
P-L1's (2,18) row lists, a cross-file consistency check the two
independent parametrisations pass. The difference between P-L1's
23 and P-L2's 79 $V$-passers is scope, not disagreement: P-L2's
sweep covers 70 rows (all $Q\le8$, $T\le20$), P-L1's table 10 named
rows; on every shared row the $V$-passer sets are identical.

**Shared conclusion, confirmed in both parametrisations:** in
every class tested, the Proposition 4.1 $V$-filter and (LD3)
dispose of everything; the (LD3⁺) stage has zero candidates to act
on; and no exhibited residual configuration is excluded by (LD3⁺)
that (LD3) does not already exclude.

## 7. Lemma L2.11 (task item 8)

**Exact statement (from P-L2.md):** fix $(Q,R)$ with $R\ge3$,
$T=R+2(Q-1)$, $\Lambda=\Lambda_3(T)$. If $(n,3,j)$ is a
counterexample in this row with $n$ even, then
$n-1\in\mathcal{F}(\Lambda)=\{3^b u : u\mid\Lambda,\
\gcd(u,3)=1,\ 0\le b\le v_3(\Lambda)+1\}$, hence
$n\le 3^{v_3(\Lambda)+1}\cdot(\Lambda/3^{v_3(\Lambda)})+1$
(= $3\Lambda+1$): the row contains only finitely many potential
counterexamples, explicitly enumerable.

**Audit.** In an $h=0$ row Proposition 4.1 (F2.13) gives
$V_3(n)\mid\Lambda$. Write the odd top $n-1=3^\beta U_1$ with $U_1$
its $\ge5$ part. $U_1\mid V_3(n)$: the decomposition
$V_3(n)=U_0U_1U_2\cdot3^{e-1}$ with pairwise coprime $U_r$ is the
standard top-by-top bookkeeping (a prime $\ge5$ divides exactly one
top, with the same exponent in $C(n,3)$), so $U_1\mid\Lambda$ and
$\gcd(U_1,3)=1$. If $\beta\ge1$, $n-1$ is the unique 3-divisible
top, $e=\beta$, and $3^{\beta-1}\mid V_3(n)\mid\Lambda$ gives
$\beta\le v_3(\Lambda)+1$; if $\beta=0$ the bound is trivial. Hence
$n-1\in\mathcal{F}(\Lambda)$, and the displayed bound is its
maximum plus 1. **Sound in every step**, including the $\beta=1$
edge (3-part of $V_3$ is $3^0$). The script §E validation (all even
$n\le200{,}000$, seven $\Lambda$ values, 0 violations) was not
re-run by the verifier; the proof is self-contained and the
verifier's §6.2 enumerations, which are built on
$\mathcal{F}(\Lambda)$, reproduce P-L2's stage counts exactly,
which exercises the lemma's conclusion on every row with $T\le20$.

**Relation to Cluster I (citing V-I, not re-verifying it).**
Lemma L2.11 is the $h=0$, counterexample-level finiteness statement
via the odd top $n-1$. V-I certifies the complementary Cluster I
results: per-row finiteness for $h\le1$ rows via the squared half
of Proposition 4.1 (P-I1 Claims I2.1–I2.5), the finite form set
$M(T)$ for $n-1$ built on the same odd-top idea (P-I1 Lemma I3.2,
with $|M(6)|=6$, $|M(8)|=12$ brute-verified by V-I), P-I2's
$h=0$ finiteness (Claim I2.2), and, strongest, the (LD3)-solution
closure of all $T\le16$ rows. Lemma L2.11 is consistent with all of
these, is neither contradicted nor subsumed in form (it covers
every fixed $h=0$ row at any $T$, with an explicit set, but only
for counterexamples, where Cluster I's P-I2 route covers
(LD3) solutions at $T\le16$), and V-I §10's summary — per-row
finiteness in every fixed row by two independent mechanisms, with
the obstruction being the infinitude of rows — applies verbatim to
the picture Lemma L2.11 completes on the $h=0$ side. No tension
between the clusters was found.

## 8. Final verdict (task item 9)

**Per prover.** P-L1: verdict **(b) is the correct label**; every
numbered claim is PROVED / COMPUTATION-confirmed / correctly
OPEN, with no defect found, and its script re-runs clean with all
outputs matching. P-L2: verdict **(b) is the correct label**;
every numbered claim is likewise sustained except the minor
defects of §2.2 and §1 (the $w=0$/$w=1$ example slip after
Proposition L2.9; the overlabelled strictness in Theorem
L2.15(iii) and its echoes; the understated Method A member list
in Computation L2.12; and the filed script's §F1 non-termination,
a provenance/documentation defect on the §F computations, all of
whose numbers the verifier independently reproduced). None of
these touches the verdict or any downstream claim.

**For the cluster: (b), certified.** Exactly what (LD3⁺) adds,
certified:
* **The new exclusion channel is the tail at digits $\ge a(p)$**,
  for each $p\mid C(n,3)$: $\lfloor j/q_p\rfloor\preceq_p
  (n-r)/q_p$, including digit $a$ itself (right-hand side
  $U\bmod p\in\{1,\dots,p-1\}$, nonzero) and, at first-power primes
  ($a=1$), every digit above 0. On digits $<a$ (LD3⁺) adds
  **nothing** — the equivalence with $j\bmod q\le r$ is exact
  (§3). At $p=3$ the channel is present exactly when
  $v_3(\text{top})\ge2$, and on the classical near-miss family
  $n=3^a+1$ it is **silent** (the tail passes for all $a$; the
  exclusion remains the low 3-clause alone).
* **Its exact scope, as exhibited:** per prime, the tail is
  decisive in 303,253 of 529,054 low-passing instances at
  $n\le2000$ (57.3%), and on the $\ge5$ subsystem it kills 8 of the
  12 solutions with $n\le10^6$ through $\ge5$ higher digits alone.
  On the full system and on every delimited residual population
  (the $h=0$ rows of §6 in both parametrisations, the (4,2) row,
  the certified range $n\le10^6$), its marginal effect is
  **exactly zero**: (LD3) — usually the Proposition 4.1 filter
  before it — already has no survivors there.
* **The exact stopping point for a general shrinkage proof**
  (both files identify the same point, and the verifier confirms
  no certified input crosses it): every certified input constrains
  the low data — $j\bmod q_p$, the prime powers themselves
  ($q_p\le T$ or $q_p\mid j$), or sizes — and nothing constrains
  the quotient digits $\lfloor j/q_p\rfloor\bmod p$ against
  $K_p\bmod p$ when both quotients are large, as they are
  throughout the residual class ($j\ge5001$, $n>10^6$). With
  $(n,p)$ and the low clause fixed, the tail can pass or fail
  independently (the $(30,5)$ example, §2.1); digitwise-$\le$ at
  each prime is a box condition with
  $\prod_e(n_e(p)+1)\ge1$ admissible digit vectors, and conditions
  at distinct primes live in distinct bases with no CRT-type
  incompatibility. A shrinkage proof needs a genuinely new input
  linking $\lfloor j/q_p\rfloor$ to the splitting data; none is
  presently known.

**Bottom line.** (LD3⁺) is the complete digitwise reformulation of
the counterexample condition at $i=3$: Sol(LD3⁺) = counterexamples,
(H3⁺) $\iff$ ($i=3$ closed), (H3) $\Rightarrow$ (H3⁺) with the
converse OPEN. It is computationally stronger than (LD3) per prime
and on the $\ge5$ subsystem, and marginally vacuous on every
residual population that can currently be delimited. **No general
shrinkage of the residual class is proved. (H3), (H3⁺), $i=3$ in
general, and #699 remain OPEN, correctly labelled by both
provers.**

— V-L
