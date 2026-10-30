# MaxDKaos cut-off: independent reimplementation (HK-A, Cycle 2)

**Claim under test** (MaxDKaos, forum comment 25 Jul 2026, disclosed as
Claude/Opus-written, filed in `EXTERNAL_CLAIMS_2026-10-29.md`): using the
Kummer bound $U_i(n) \le n^{\pi(i-1)}$ (S1), a prime-free-interval
condition (S3), and first-occurrence prime-gap data $G(i)$, via a "sharp
form of the cut-off" that was not printed, the settled $j$-ranges for all
$n$ are $j \le 5, 12, 30, 138, 25063, 713421, 360654145$ for
$i = 3, 5, 10, 20, 100, 200, 394$, plus an asymptotic $j \le C\,i\log^2 i$
via Dusart.

**Headline verdict.** Only **one** of the seven tabulated values
reproduces exactly under any of the candidate cut-offs tested, namely
$i=3 \to 5$, and only under the *crude* candidate A. Every other entry is
**not reproduced** under any tested candidate: the sharp candidates
settle strictly fewer pairs than claimed (candidate B prefix values
$6, 9, 25, 116, 22587, 658087, 331301695$ against claimed
$5, 12, 30, 138, 25063, 713421, 360654145$; note $i=3$ under B settles
*more*, 6, so 5 is not the B-maximum either). No count beyond the single
$i=3$ entry under A is credited.

Code: `verification/maxdkaos_reimplementation.py` (Python stdlib only,
single thread, exact integer arithmetic via `math.comb` for every
binomial comparison; no log-space comparisons anywhere; total runtime
129.5 s, dominated by a sieve to $5\cdot10^7$ and a full brute-force
validation at $i=100$).

---

## 1. Definitions (exact)

Pairs are $(i,j)$ with $i < j$; $n \ge 2j$; a counterexample at $(n,i,j)$
must satisfy the S1 size condition $C(n,i) \le u \cdot C(j, j-i)$ with
$u$ the $({<}i)$-part of $C(n,i)$, and the S3 condition that $(n-i, n]$
is prime-free.

**$G(i)$.** $G(i) := $ the largest $M$ such that every interval
$(n-i, n]$ with $n \le M$ contains a prime. If $(p, p+g)$ is the first
prime gap with $g > i$, the first prime-free $n$ is $p+i$ (for
$n = p+i$: $(p, p+i]$ contains no prime, since the next prime is
$p+g > p+i$), so
$$G(i) = p + i - 1.$$

**Candidate A (crude Kummer + first-gap cut-off).**
$N_K(i,j) := \max\{n \ge 2j : C(n,i) \le n^{\pi(i-1)} C(j, j-i)\}$,
with the convention $N_K = 2j-1$ if the inequality already fails at
$n = 2j$ (the bad set is the interval $[2j, N_K]$, by strict
monotonicity of $F_i(n) = C(n,i)/n^{\pi(i-1)}$, S1 Lemma 4).
Settled$_A(i,j)$ iff $N_K(i,j) \le G(i)$.

**Candidate B (sharp Kummer + first-gap cut-off).** With
$U^\sharp(n,i) := \prod_{p<i} q_p(n)$, $q_p(n) = p^{\lfloor\log_p n\rfloor}$
(S1 Lemma 3), let
$\mathrm{Bad}^\sharp(i,j) := \{n \ge 2j : C(n,i) \le U^\sharp(n,i)\,C(j, j-i)\}$
(a subset of $[2j, N_K(i,j)]$ by S1 Lemma 5(a); it need not be an
interval, S1 Lemma 5(c)). Settled$_B(i,j)$ iff **no**
$n \in \mathrm{Bad}^\sharp(i,j)$ has $n > G(i)$, i.e. iff
$\max \mathrm{Bad}^\sharp(i,j) \le G(i)$ (or the set is empty).

**Candidate C (sharp Kummer + exact prime-free windows).**
Settled$_C(i,j)$ iff no $n \in \mathrm{Bad}^\sharp(i,j)$ is prime-free
in the S3 sense. Prime-free $n$ are exactly the integers in the windows
$[p+i,\ p+g-1]$ over prime gaps $(p, p+g)$ with $g > i$. Candidate C is
the mathematically exact combination of the two ingredients (B throws
away a bad $n > G(i)$ even when $(n-i,n]$ in fact contains a prime;
only a bad **and** prime-free $n$ can be a counterexample), so
C settles at least as much as B, pointwise.

**Settled-$j(i)$** reported below is the *prefix* value: the largest
$J$ such that every $i < j \le J$ is settled. Where the settled set is
not a prefix, the actual set structure is reported (§4).

**How B and C are evaluated exactly (segment minima).** $U^\sharp(\cdot, i)$
is constant between consecutive prime powers $p^e$ ($p < i$), and
$C(n,i)$ is strictly increasing, so on each such segment
$C(n,i)/U^\sharp(n,i)$ is strictly increasing and its minimum on any
sub-domain is attained at the first point of that sub-domain. Hence
settled$_B$ is decided by evaluating the exact inequality at
$n = \max(2j, G(i)+1)$ and at each prime power in $( \max(2j,G(i)+1), N_K ]$;
$\max \mathrm{Bad}^\sharp$ is computed segment-by-segment by exact
binary search; settled$_C$ is decided window-by-window by evaluating
at the window start (clipped to $n \ge 2j$) and at prime powers inside
the window. These fast tests were **validated against brute force**
(§5), not merely asserted.

**Monotonicity in $j$ (verified, not assumed).**
- *A:* $C(j, j-i)$ is strictly increasing in $j$ and $F_i$ is strictly
  increasing in $n$, so $N_K(i,j)$ is nondecreasing in $j$; settled$_A$
  is a genuine prefix, globally. The enumerations and searches below
  confirm $N_K$ nondecreasing at every evaluated step.
- *B:* if $(i, j_2)$ is settled$_B$ and $i < j_1 < j_2$ with
  $2 j_2 \le G(i)$, then $(i, j_1)$ is settled$_B$: a bad $n \ge 2j_2$
  for $j_1$ is also bad for $j_2$ (the right side grows with $j$), and
  a bad $n \in [2j_1, 2j_2)$ satisfies $n < 2j_2 \le G(i)$, so it does
  not violate settled$_B$. Hence settled$_B$ is a prefix on
  $j \le G(i)/2$, which covers every binary-searched threshold below
  except $i=3$; for $i=3$ the settled set was enumerated completely to
  $j = 2000$ and then closed off by proof (§4). Threshold
  neighbourhoods were additionally evaluated $j$ by $j$.
- *C:* **not** a prefix in general (see $i=3$ in §4). For
  $j \le G(i)/2$ the same boundary argument applies (an $n \in
  [2j_1, 2j_2) \le G(i)$ cannot be prime-free, by definition of $G$),
  and all searches below stay inside such ranges except where complete
  enumeration was done instead.

---

## 2. The values $G(i)$

Computed from raw prime gaps by my own sieve (exhaustive scan in
increasing prime order), except $i=394$, for which see below.

| $i$ | first gap $> i$ | at prime $p$ | $G(i) = p+i-1$ | source |
|---|---|---|---|---|
| 3 | 4 | 7 | **9** | own sieve |
| 5 | 6 | 23 | **27** | own sieve |
| 10 | 14 | 113 | **122** | own sieve |
| 20 | 22 | 1129 | **1148** | own sieve |
| 100 | 112 | 370261 | **370360** | own sieve (limit $5\cdot10^5$) |
| 200 | 210 | 20831323 | **20831522** | own sieve (limit $5\cdot10^7$) |
| 394 | 456 | 25056082087 | **25056082480** | published maximal-gap records (below) |

**Anchors.** The definition above reproduces both coordinator anchors
exactly: $G(3) = 9$ and $G(5) = 27$. ✓

**A trap definition (noted as requested).** The slightly different
$G_{\mathrm{alt}}(i) := p_{\text{next}} - 2 = p + g - 2$ also reproduces
both anchors (because the first gaps there are $g = i+1$ exactly), but
it is *wrong* in general: it gives $125, 1149, 370371$ for
$i = 10, 20, 100$ against the true $122, 1148, 370360$; e.g. for
$i=10$, $n = 124$ already has $(114, 124]$ prime-free (the primes
around are 113 and 127), so $G(10) = 122$, not 125. All computations
below use the interval definition, $G(i) = p+i-1$.

**$i=200$ is attainable, contrary to the expectation in my brief.** The
brief suggested the first gap $> 200$ might first occur at a prime
around $10^9$ and be untestable. That is not what the data show: my own
sieve to $5\cdot10^7$ finds, exhaustively and in order, that the first
gap exceeding 200 is the gap of **210 at $p = 20831323$**
($\approx 2.1\cdot10^7$), giving $G(200) = 20831522$. This matches the
published maximal-gap table (gap 210 at 20831323, in e.g.
Granville–Lumley, *Primes in short intervals*, arXiv:2009.05000,
Fig. 4, and the maximal-gap table on Wikipedia, "Prime gap", crawled
2026-10-27). So candidates A, B and C are all fully testable at
$i = 200$ (prime-free windows for $i=200$ up to $5\cdot10^7$ from the
same sieve: $[20831523, 20831532]$ and $[47326893, 47326912]$ only).

**$i=394$ via published maximal gaps.** A sieve past $2.5\cdot10^{10}$
is outside the resource bounds, so $G(394)$ is taken from the published
maximal (record) prime-gap table (OEIS A005250 / A002386, Nicely's
tables; as tabulated on Wikipedia, "Prime gap", crawled 2026-10-27):
the records near the relevant range are gap 382 at 10726904659, gap
**394** at 22367084959, gap **456** at 25056082087, gap 464 at
42652618343. A gap $> 394$ starting before 25056082087 would exceed
every earlier gap (the maximum up to that point is the record 394
itself), so it would itself be a record with value in $(394, 456]$;
the published record list contains no such record. Hence the first
gap $> 394$ is the 456 gap at $p = 25056082087$, and
$G(394) = 25056082087 + 393 = 25056082480$. Cross-checks of the record
pair: Granville–Lumley, arXiv:2009.05000, Fig. 4 lists 25056082087
with gap 456; Kourbatov, arXiv:1309.4053, lists the pair
$25056082087 \to 25056082543$ (difference 456, matching the script's
assertion). Candidates A and B need only $G(394)$ and are fully
testable; candidate C at $i=394$ is treated in §4/§6.

---

## 3. Results: prefix settled-$j(i)$ per candidate

| $i$ | claimed | A (crude) | B (sharp) | C (sharp + windows) | $G(i)$ |
|---|---|---|---|---|---|
| 3 | **5** | **5** ✓ | 6 | 6 | 9 |
| 5 | 12 | 8 | 9 | 9 | 27 |
| 10 | 30 | 22 | 25 | 26 | 122 |
| 20 | 138 | 77 | 116 | 116 | 1148 |
| 100 | 25063 | 15060 | 22587 | 23305 | 370360 |
| 200 | 713421 | 432029 | 658087 | 658087 | 20831522 |
| 394 | 360654145 | 232615486 | 331301695 | 331301695 (prefix; §6) | 25056082480 |

Diagnostic values at his claimed $j$ (exact): $N_K$ = crude top,
$M^\sharp = \max \mathrm{Bad}^\sharp$.

| $i$ | $N_K(i, j_{\text{claim}})$ | $M^\sharp(i, j_{\text{claim}})$ | $G(i)$ | $M^\sharp / G(i)$ |
|---|---|---|---|---|
| 3 | 9 | — (empty) | 9 | — |
| 5 | 48 | 40 | 27 | 1.481 |
| 10 | 226 | 157 | 122 | 1.287 |
| 20 | 3282 | 1548 | 1148 | 1.348 |
| 100 | 731596 | 433530 | 370360 | 1.171 |
| 200 | 39964155 | 22583327 | 20831522 | 1.084 |
| 394 | 43214243868 | 27682720715 | 25056082480 | 1.105 |

Reading of the diagnostic: his claimed $j$ would be settled under
candidate B **iff** $G(i)$ were at least $M^\sharp(i, j_{\text{claim}})$,
i.e. iff the first gap $> i$ occurred later than it actually does, by
the factors in the last column (1.08–1.48, at every $i \ge 5$). The
Kummer side of the computation is not where the discrepancy sits: the
same $N_K$ and $M^\sharp$ functions that fail his table at the true
$G(i)$ would reproduce it at a uniformly inflated $G(i)$.

## 4. Set structure (where the settled set is not just a prefix)

- **A, all $i$:** settled set is exactly the prefix in §3, globally
  (monotonicity of $N_K$ in $j$, §1). E.g. at $i=3$: $\{4, 5\}$,
  confirmed by enumeration to $j = 2000$ and by the monotonicity proof.
- **B, $i=3$:** settled set is exactly $\{4, 5, 6\}$. Enumerated to
  $j = 2000$; closed off for all $j \ge 7$ as follows: at $j=7$,
  $\mathrm{Bad}^\sharp(3,7) = \{16\}$ with $16 > G(3) = 9$; for every
  $j \ge 8$, $2j \in \mathrm{Bad}^\sharp(3,j)$ (verified exactly in the
  script for $8 \le j \le 5000$, and in closed form:
  $C(2j,3)/C(j,3) = 4(2j-1)/(j-2) \le 10$ for $j \ge 8$ and decreasing,
  while $U^\sharp(2j,3) = $ largest power of 2 $\le 2j$ is $\ge 16$),
  and $2j > 9$. So no $(3, j)$ with $j \ge 7$ is B-settled.
- **B, $i \in \{5, 10, 20\}$:** complete enumerations (to
  $j = 200, 200, 300$ respectively) give exactly the prefixes
  $\{6..9\}$, $\{11..25\}$, $\{21..116\}$ with no sporadic returns
  inside the enumerated ranges. For $i \in \{100, 200, 394\}$ the §1
  prefix argument rules out any sporadic B-return for all
  $j \le G(i)/2$ ($185180$, $10415761$, $12528041240$), far beyond the
  claimed values.
- **C, $i=3$:** the settled set is **not** a prefix. Complete
  enumeration to $j = 200$ gives exactly $\{4, 5, 6, 9\}$: $j = 7, 8$
  fail (witness $n = 16$, which is sharp-bad and prime-free), while
  $j = 9$ is settled again once $2j = 18 > 16$ removes that witness
  from the domain. The C prefix value is therefore 6, with an isolated
  extra settled point at $j=9$ in the enumerated range.
- **C, $i \in \{5, 10, 20\}$:** complete enumerations (same ranges as
  B) give exactly the prefixes $\{6..9\}$, $\{11..26\}$, $\{21..116\}$;
  no sporadic returns in range. Note $i=10$ is the one case where C
  beats B (26 vs 25): B's first failure is at a non-prime-free jump
  point, C's at the window point $n = 370361$-analogue $[123,126]$.
- **C, $i=100$:** windows up to $10^6$ are $[370361, 370372]$ and
  $[492213, 492226]$ (from my sieve); prefix 23305, first failure
  witnessed at $n = 370361$ itself.
- **C, $i=200$:** prefix 658087, equal to B: B's first failure at
  $j = 658088$ is already witnessed at the prime-free window start
  $n = G(200)+1 = 20831523$ (script-verified exactly), and that same
  $n$ stays sharp-bad for all larger $j$ up to $n/2$ (the right side
  $C(j, j-i)$ grows with $j$), so C also fails at the claimed
  $j = 713421$ itself, not merely as a prefix.
- **C, $i=394$:** prefix 331301695, by the same witness argument
  (§6); individual C status for $j$ beyond the first failure is not
  asserted. The claimed $j = 360654145$ itself is **not** C-settled:
  the witness $n_0 = G(394)+1 = 25056082481$ is sharp-bad already at
  $j = 331301696$ (script-verified exactly), lies in the first window
  $[25056082481, 25056082542]$, stays sharp-bad as $j$ grows (right
  side increasing) and stays in the domain since
  $360654145 < n_0/2$.

## 5. Validation performed

- Anchors $G(3) = 9$, $G(5) = 27$ reproduced from raw gaps by my own
  sieve (asserted in the script).
- The segment-minima tests for B (`settled_B`, `maxbad_sharp`) agree
  with **brute force** (independent `math.comb` evaluation at every
  single $n$) for: $i \in \{3,5,10,20\}$, all $j \in (i, i+40]$;
  $i = 100$, $j \in \{200, 500, 1000\}$; and at the $i=100$ B-threshold
  itself, where brute force gives $\max \mathrm{Bad}^\sharp(100, 22587)
  = 358921 \le 370360$ (settled) and
  $\max \mathrm{Bad}^\sharp(100, 22588) = 390639 > 370360$ (not settled).
- The window/minima test for C agrees with brute-force C (direct
  prime-free check at every bad $n$) for $i \in \{3,5,10,20\}$, all
  $j \in (i, i+40]$.
- $i=3$ B-closure for all $j \ge 8$ (the $2j \in \mathrm{Bad}^\sharp$
  statement) verified exactly for $8 \le j \le 5000$ in the script,
  plus the closed-form ratio bound in §4.
- All binary searches were run only inside ranges where the relevant
  settled set is *proved* to be a prefix (§1), the endpoints were
  asserted (settled at the bottom, not settled at the claimed value),
  and every threshold neighbourhood was re-evaluated $j$ by $j$
  (e.g. $i=100$: flags True,True,True,False,False across
  $j = \text{threshold}-2 \dots \text{threshold}+2$ for each of A, B, C).

## 6. What is NOT testable, and why (exact obstructions)

- **Candidate C at $i=394$, beyond the prefix.** Deciding C for an
  *individual* $j$ beyond the first failure requires all prime-free
  windows up to $N_K(394, j)$; at the claimed $j$,
  $N_K = 43214243868 \approx 4.3\cdot10^{10}$. Published maximal-gap
  records give only *record* gaps in that range, not all gaps in
  $(394, 456]$, and a sieve to $4.3\cdot10^{10}$ is outside the stated
  bounds (stdlib-only, $\sim$25 min per computation, $<$ 2 GB). So:
  the C **prefix** at $i=394$ is exact (331301695, via the §4 witness
  argument, which needs only $G(394)$ and one exact inequality), and
  the claimed value itself is exactly refuted for C by the same
  witness; but a complete C settled-*set* at $i=394$ is **NOT
  TESTABLE** with these resources, and none is claimed.
- Nothing else is untestable: $G(i)$ was obtained for **all seven**
  values of $i$ (six by my own sieve, $i=394$ from the cited published
  maximal-gap records), and candidates A and B were evaluated exactly
  for all seven.

## 7. Verdicts, entry by entry

| $i$ | claimed | verdict |
|---|---|---|
| 3 | 5 | **REPRODUCED under candidate A** (exactly: $N_K(3,5) = 9 = G(3)$ and $N_K(3,6) = 12 > 9$). Under B and C the maximum is 6, so 5 does not reproduce as the sharp-criterion maximum; the pair $(3,5)$ itself is of course settled under all three. |
| 5 | 12 | **NOT REPRODUCED** under any tested candidate (A 8, B 9, C 9; at $j=12$ itself, $M^\sharp = 40 > G(5) = 27$, and 12 is settled under none of A/B/C). |
| 10 | 30 | **NOT REPRODUCED** under any tested candidate (A 22, B 25, C 26; $M^\sharp(10,30) = 157 > 122$). |
| 20 | 138 | **NOT REPRODUCED** under any tested candidate (A 77, B 116, C 116; $M^\sharp(20,138) = 1548 > 1148$). |
| 100 | 25063 | **NOT REPRODUCED** under any tested candidate (A 15060, B 22587, C 23305; $M^\sharp(100,25063) = 433530 > 370360$). |
| 200 | 713421 | **NOT REPRODUCED** under any tested candidate (A 432029, B 658087, C 658087; $M^\sharp(200,713421) = 22583327 > 20831522$). |
| 394 | 360654145 | **NOT REPRODUCED** under any tested candidate (A 232615486, B 331301695, C prefix 331301695 and C fails at the claimed $j$ itself by the §4 witness; $M^\sharp(394, 360654145) = 27682720715 > 25056082480$). Complete C set at $i=394$: NOT TESTABLE (§6). |

## 8. The asymptotic claim $j \le C\,i \log^2 i$

Ratios $j / (i (\ln i)^2)$ (natural log), for his claimed values and
for the candidate-B prefix values actually obtained:

| $i$ | $i(\ln i)^2$ | claimed $j$ | ratio (claimed) | B prefix $j$ | ratio (B) |
|---|---|---|---|---|---|
| 3 | 3.6 | 5 | 1.381 | 6 | 1.657 |
| 5 | 13.0 | 12 | 0.927 | 9 | 0.695 |
| 10 | 53.0 | 30 | 0.566 | 25 | 0.472 |
| 20 | 179.5 | 138 | 0.769 | 116 | 0.646 |
| 100 | 2120.8 | 25063 | 11.818 | 22587 | 10.650 |
| 200 | 5614.4 | 713421 | 127.069 | 658087 | 117.213 |
| 394 | 14072.4 | 360654145 | 25628.461 | 331301695 | 23542.645 |

**Consistency assessment (no over-claim).** Over the tested range the
ratio does **not** settle toward a constant: it is $\lesssim 1.7$ for
$i \le 20$, then grows to $\approx 11$–$12$ at $i = 100$,
$\approx 117$–$127$ at $i = 200$, and $\approx 2.4$–$2.6\cdot10^4$ at
$i = 394$, for *both* his table and the independently computed B
values. A single constant $C$ fitting all seven points would have to
be at least $25628$ (from his own $i=394$ entry), and the ratio is
still increasing steeply at the largest $i$ tested, so the table (his
or ours) provides no evidence of a bound $j \le C\,i\log^2 i$ with a
stable, informative constant over this range. Strictly, seven finite
points cannot refute an asymptotic statement with unspecified $C$ and
unspecified onset; what is established is only the ratios above and
that they are strongly increasing, not stabilising, throughout the
entire range his table covers.

## 9. Bottom line

Of MaxDKaos's seven tabulated values, exactly one — $i=3 \to 5$ —
reproduces, and it reproduces under the **crude** candidate A
($N_K \le G$), not under either sharp candidate (both of which give 6
at $i=3$). The remaining six values exceed what the strongest exact
combination of his stated ingredients (candidate C) delivers, by
factors in $j$ of $12/9$, $30/26$, $138/116$, $25063/23305$,
$713421/658087$, $360654145/331301695$ (claimed over C). Equivalently,
on the $n$-side his values would require the first prime gap $> i$ to
sit at $M^\sharp(i, j_{\text{claim}})$ instead of the true $G(i)$ —
systematically 8–48% further out. **No count beyond $(i, j) = (3, 5)$
under candidate A is credited.**
