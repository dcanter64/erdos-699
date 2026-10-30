# P-H1 — Cycle 2, Prover H1: Counting Bounds on Simultaneous Bad Configurations in R1

**Problem.** Erdős #699: for $1 \le i < j \le n/2$, $C(n,i)$ and $C(n,j)$
always share a prime factor $\ge i$. Notation, regime R1
($3i/2 < j < 2i$, $d = j-i$), $S(n,i)$, $e_p$, $A_p$, $B_p$, $\Delta_p$,
bad/good primes: as in `strategies/S10.md`, which is taken as established,
together with the campaign ground truth: EEES78
($V_i(n) > C(n,i)^{1/2}$ for $(n,i)$ not one of the 12 exception pairs),
the key lemma ($d \mid C(n,i)$, $\gcd(d, C(n,j)) = 1 \Rightarrow
d \mid C(j,i)$), the finite reduction $n \le N(i,j)$, the closures of
$j \le 3i/2$, $n = 2j$, $i \in \{1,2\}$, and the clean sweep to
$n \le 20{,}000$. Del Pin's lemma and the values of $J_1$ are taken from
`EXTERNAL_CLAIMS_2026-10-29.md` (verified there).

**Headline.** The T1 size lever as posed in S10 §8 closes exactly the
Del Pin range (Claim 3), and it has a genuine barrier at the first pair
beyond it (Claim 4). But the chain contains real slack: in R1 every bad
prime satisfies $v_p(C(j,i)) = 1$ *exactly* (Claim 2), so $V_i(n)$ is
not merely $\le C(j,i)$ — it divides the primorial ratio
$P(i,j) = \prod_{i < p \le j} p$, which is typically *enormously*
smaller. The sharpened lever (Claim 7) closes every R1 pair with
$i \le 1000$ except $(4,7)$ and $(10,19)$ by exact computation
(Claim 8), every pair with $i > 1000$ analytically modulo two cited
explicit $\theta$ estimates (Claim 9), and the two exceptional pairs
fall to the finite reduction plus the sweep (Claim 10). Net: **R1 is
closed modulo the named established/cited inputs** (Claim 11). The
combined-cap recount of Task 3 is exact: **377 triples, the combined
cap kills 0 of them, maximum simultaneous bad count 5** (Claim 13),
and this is forced by theory, not accident (Claim 14).

---

## 1. Task 1 — the T1 size lever, exactly

### Claim 1 (PROVED): the T1 chain

Let $(n,i,j)$ be a counterexample in R1 with $(n,i)$ not an EEES78
exception pair. Then, writing $\mathcal{B}$ for the set of bad primes,

$$ \prod_{p \in \mathcal{B}} p \;=\; V_i(n) \;>\; C(n,i)^{1/2} \;\ge\; C(2j,i)^{1/2},
\qquad\text{and}\qquad V_i(n) \mid C(j,i),\ \text{so } V_i(n) \le C(j,i). $$

*Proof.* In R1 a counterexample has $S(n,i) \subseteq [i,j]$ and
$e_p = 1$ for every $p \in S(n,i)$ (S10, Theorem S10/R1), and every
$p \in S(n,i)$ is bad by definition of counterexample, so
$V_i(n) = \prod_{p \in S(n,i)} p^{e_p} = \prod_{p \in \mathcal{B}} p$,
squarefree. Since every $p \in S(n,i)$ is bad,
$\gcd(V_i(n), C(n,j)) = 1$, and $V_i(n) \mid C(n,i)$, so the key lemma
gives $V_i(n) \mid C(j,i)$, hence $V_i(n) \le C(j,i)$. EEES78 gives
$V_i(n) > C(n,i)^{1/2}$, and $C(n,i) \ge C(2j,i)$ because $n \ge 2j$
(the hypothesis $j \le n/2$) and $C(n,i)$ is increasing in $n$ for
fixed $i$. $\square$

Consequently the lever yields a contradiction for the pair $(i,j)$
whenever $C(j,i) \le C(2j,i)^{1/2}$, i.e. whenever

$$ C(2j,i) \;\ge\; C(j,i)^2. \tag{$\ast$} $$

(If $(\ast)$ holds, Claim 1 gives $C(j,i) \ge V_i(n) > C(2j,i)^{1/2}
\ge C(j,i)$, impossible. The endpoint case is included: the first
inequality in Claim 1 is strict, so $\ge$ in $(\ast)$ suffices.)

### Claim 2 (PROVED): the $v_p(C(j,i))$ check — automatic, exactly 1, with one exception that never occurs

For every prime $p$ with $i < p \le j$ in R1,
$v_p(C(j,i)) = 1$ exactly. For $p = i$ (possible only if $i$ is prime),
$v_i(C(j,i)) = 0$.

*Proof.* $v_p(C(j,i)) = \lfloor j/p \rfloor - \lfloor i/p \rfloor -
\lfloor d/p \rfloor$ in the $k=1$ Legendre term, and all $k \ge 2$
terms vanish because $p > j/2$ (as $p \ge i > j/2$ in R1) gives
$p^2 > j$. If $i < p \le j$: $\lfloor j/p \rfloor = 1$ (since
$p \le j < 2p$), $\lfloor i/p \rfloor = 0$, $\lfloor d/p \rfloor = 0$
(since $d < i < p$), so $v_p = 1$. If $p = i$ prime:
$\lfloor j/i \rfloor = 1$ (since $j < 2i$), $\lfloor i/i \rfloor = 1$,
$\lfloor d/i \rfloor = 0$, so $v_i = 0$. $\square$

*Consequences, stated precisely.* (i) No sharpening of Claim 1 comes
from multiplicities: each bad prime can contribute *at most* one
factor $p$ to $C(j,i)$, and it does contribute one — there is no
$v_p \ge 2$ headroom on either side. (ii) The one weakening in the
chain is $p = i$: a prime $i \in S(n,i)$ would contribute a factor to
$V_i(n)$ that does *not* divide $C(j,i)$. But in R1 such a prime can
never be bad (S10, Theorem 3(b): $B_i = 0$, $\Delta_i \le 0 < e_i$),
so a counterexample has $i \notin S(n,i)$ anyway, and the weakening
is vacuous under the counterexample hypothesis. (iii) The real slack
is not in the exponents but in the *support*: Claim 1 uses only
$V_i(n) \le C(j,i)$, whereas $V_i(n)$ is a squarefree product of
*distinct primes in the short interval $(i, j]$*, each occurring in
$C(j,i)$ to exactly the first power. Hence in fact
$V_i(n) \mid P(i,j) := \prod_{i<p\le j} p$ and $P(i,j) \mid C(j,i)$,
usually with a huge quotient. This is the sharpening exploited in §2
(Claim 7).

### Claim 3 (PROVED, pairwise): the $C(j,i)$ lever closes precisely the pairs satisfying $(\ast)$ — Del Pin's $J_1$ range

For a single pair $(i,j)$, the two inequalities of Claim 1 are
incompatible iff $(\ast)$ holds: if $(\ast)$ fails, i.e.
$C(2j,i) < C(j,i)^2$, then $V_0 = C(j,i)$ itself satisfies
$V_0 \mid C(j,i)$ and $V_0 > C(2j,i)^{1/2}$, so no contradiction can
be extracted from the size data of Claim 1 alone. By Del Pin's lemma
(recorded and verified in `EXTERNAL_CLAIMS_2026-10-29.md`: the ratio
$F(j) = C(2j,i)/C(j,i)^2$ is strictly decreasing in $j$), for fixed
$i$ the set of $j$ satisfying $(\ast)$ is an initial segment
$j \le J_1(i)$, with $J_1(3) = 5$, $J_1(5) = 8$, $J_1(640) = 962$,
$J_1(5000) = 7503$. So the unsharpened lever closes exactly the R1
pairs $3i/2 < j \le J_1(i)$ — a slice only $O(\log i)$ wide beyond
$3i/2$ — and nothing beyond. For $i = 39$ I compute exactly:
$J_1(39) = 59$, i.e. $(\ast)$ holds at $j = 59$ and fails for every
$j = 60, \dots, 77$ in R1 (exact integer comparisons, Appendix A).

### Claim 4 (PROVED): the barrier beyond $J_1$, exhibited at $(39,60)$

The pair $(i,j) = (39,60)$ is in R1 ($58.5 < 60 < 78$) and is the
first pair beyond $J_1(39) = 59$. Exact values:

$$ C(60,39) = 7{,}984{,}465{,}725{,}343{,}800, \qquad
C(120,39) = 56{,}571{,}283{,}083{,}933{,}415{,}181{,}782{,}620{,}687{,}640, $$
$$ \frac{C(120,39)}{C(60,39)^2} = 0.8873691112\ldots < 1, \qquad
C(60,39) - \lfloor C(120,39)^{1/2} \rfloor = 463{,}077{,}350{,}586{,}557 > 0. $$

So the interval $\big(C(2j,i)^{1/2},\, C(j,i)\big]$ is nonempty and
$V_0 = C(60,39)$ is an abstract integer satisfying *both* size
constraints of Claim 1 simultaneously. The $C(j,i)$ lever alone
therefore cannot exclude a counterexample at $(39,60)$: **the
barrier for the unsharpened lever is exactly the curve
$C(2j,i) = C(j,i)^2$, and $(39,60)$ sits strictly beyond it.**
(This is a barrier for the lever, not for the pair: Claim 7 closes
$(39,60)$ by the sharpened bound, with a margin of about $10^{15}$.)

### Claim 5 (PROVED, by exact computation): the $(119, 39, 59)$ numerics and the slack in the in-range part

At $(n,i,j) = (119, 39, 59)$ the five bad primes are
$41, 43, 47, 53, 59$ (S10, Example A), and

$$ \prod_{p\ \mathrm{bad}} p = 41 \cdot 43 \cdot 47 \cdot 53 \cdot 59 = 259{,}106{,}347 =: P. $$

$$ C(59,39) = 2{,}794{,}563{,}003{,}870{,}330, \qquad P \mid C(59,39),
\quad \frac{C(59,39)}{P} = 10{,}785{,}390 \ \text{(exact)}. $$

Square comparisons (integer arithmetic, via $\mathrm{isqrt}$):

$$ C(118,39) = 25{,}671{,}002{,}407{,}835{,}331{,}258{,}960{,}180{,}816{,}240,
\quad \lfloor C(118,39)^{1/2} \rfloor = 5{,}066{,}655{,}939{,}358{,}358, $$
$$ C(118,39) - C(59,39)^2 = 17{,}861{,}420{,}025{,}234{,}569{,}212{,}400{,}726{,}507{,}340 > 0
\quad (F = 3.2871\ldots), $$
$$ C(119,39) = 38{,}185{,}616{,}081{,}655{,}055{,}247{,}703{,}268{,}964{,}157,
\quad \lfloor C(119,39)^{1/2} \rfloor = 6{,}179{,}451{,}114{,}917{,}493. $$

As requested, also $C(238,39)$ (note $238 = 2n$, not $2j$; the T1
threshold is $C(2j,i) = C(118,39)$, and I record the requested number
alongside it):

$$ C(238,39) = 881{,}689{,}851{,}124{,}977{,}590{,}640{,}300{,}656{,}276{,}855{,}178{,}603{,}818{,}200,
\quad \lfloor C(238,39)^{1/2} \rfloor = 29{,}693{,}262{,}722{,}795{,}849{,}580{,}394. $$

**The slack.** The in-range product $P$ falls short of every size
threshold in sight, by large exact factors:

$$ \frac{C(118,39)^{1/2}}{P} \approx 1.955 \times 10^{7}, \qquad
\frac{C(119,39)^{1/2}}{P} \approx 2.385 \times 10^{7}, \qquad
\frac{C(238,39)^{1/2}}{P} \approx 1.146 \times 10^{14}, \qquad
\frac{C(59,39)}{P} = 10{,}785{,}390. $$

So the lever, applied to the in-range part *alone*, excludes nothing
at this triple: $P$ satisfies $P \mid C(59,39)$ with quotient
$\approx 1.08 \times 10^7$ to spare, and $P$ is seven orders of
magnitude below the EEES threshold that a genuine counterexample
would need its *full* $V_i(n)$ to exceed. The contradiction the lever
produces for the pair $(39,59)$ (which lies exactly on the $J_1$
boundary, $F = 3.287 > 1$) uses essentially the hypothesis
$S(n,i) \subseteq [i,j]$, i.e. the identification $V_i(n) = P$ for a
*hypothetical* counterexample — not any largeness of the realised
in-range product. For the realised triple, $S(119,39)$ has the eight
further primes $83, 89, 97, 101, 103, 107, 109, 113$, each with
$e_p = 1$, contributing $Q = 9{,}823{,}972{,}789{,}433{,}423$, and the
true value is

$$ V_{39}(119) = P \cdot Q = 2{,}545{,}453{,}702{,}497{,}494{,}433{,}235{,}781,
\qquad V_{39}(119)^2 > C(119,39), $$

exactly as EEES78 requires. The size lever has essentially nothing
to say against the in-range configuration itself; all of its force
comes from the support hypothesis $S(n,i) \subseteq [i,j]$. That is
the precise sense in which size arguments cap out here, and it is
what the sharpening in §2 repairs — by making the support hypothesis
itself carry a much smaller upper bound.

---

## 2. Task 2 — second lever: counting (option (b)), crude form, then sharpened

Let $b = |S(n,i)|$ for a hypothetical R1 counterexample. Since
$e_p = 1$ on $S(n,i)$ and $i \le p \le j$ there, $V_i(n) = \prod p$
gives the two crude cardinality bounds

$$ j^{\,b} \;\ge\; V_i(n) \;>\; C(2j,i)^{1/2}
\qquad\text{and}\qquad
i^{\,b} \;\le\; V_i(n) \;\le\; C(j,i), $$
i.e. $\;b > \dfrac{\tfrac12 \log C(2j,i)}{\log j}$ and
$\;b \le \dfrac{\log C(j,i)}{\log i}$.

### Claim 6 (PROVED; computation exact): the crude counting bound is weak — it closes 14 of the 361 R1 pairs with $i < 40$, and at $(39,59)$ and $(39,60)$ it only forces $b = 9$

Exact integer test (largest $b$ with $i^b \le C(j,i)$, then check
$j^{2b} \le C(2j,i)$; Appendix A): over the 361 R1 pairs with
$i < 40$, the crude bounds are incompatible for exactly **14 pairs**:
$(5,8), (6,10), (7,11), (9,15), (10,16), (11,17), (14,22), (15,23),
(19,29), (24,37), (25,38), (29,44), (34,52), (35,53)$.
At $(39,59)$: the bounds give $8.868 < b \le 9.708$, forcing $b = 9$;
at $(39,60)$: $8.929 < b \le 9.995$, again forcing $b = 9$. So crude
counting reduces a hypothetical counterexample at $(39,59)$ to the
single possibility $|S| = 9$ — already absurd there, because
$[39,59]$ contains only five primes at all (this is the sharp form
below). Against the measured data of §3 the tension is the same:
the counting lower bound demands $\ge 9$ simultaneous bad primes at
$(39,59)$, while the exhaustive in-interval search (§3) never sees
more than **5** simultaneous in-range bad primes for any R1 pair
$i < 40$. Crude counting, however, wastes too much (it pretends the
bad primes could be as small as $i$ and as large as $j$
simultaneously) to close pairs in general: 347 of 361 pairs at
$i < 40$ survive it.

### Claim 7 (PROVED): the sharpened counting bound — $V_i(n) \mid P(i,j)$

For a hypothetical R1 counterexample,
$$ V_i(n) \;\Big|\; P(i,j) \;:=\; \prod_{i < p \le j} p,
\qquad\text{hence}\qquad V_i(n) \le P(i,j), $$
and a contradiction follows whenever
$$ P(i,j)^2 \;\le\; C(2j,i). \tag{$\ast\ast$} $$

*Proof.* By Claim 2, every bad prime $p$ satisfies $i < p \le j$
($p = i$ is impossible, as shown there) and the bad primes are
distinct, so $V_i(n) = \prod_{p\ \mathrm{bad}} p$ divides the product
of *all* primes in $(i, j]$. Combine with $V_i(n) > C(2j,i)^{1/2}$
from Claim 1: if $(\ast\ast)$ holds then
$C(2j,i)^{1/2} < V_i(n) \le P(i,j) \le C(2j,i)^{1/2}$, impossible.
$\square$

Note $b \le \pi(j) - \pi(i)$ is an immediate corollary (there are
only that many candidate primes), and $(\ast\ast)$ is far stronger
than the $C(j,i)$ condition $(\ast)$ whenever it holds, because
$P(i,j) \mid C(j,i)$ with typically enormous quotient (at $(39,59)$
the quotient is $10{,}785{,}390$, Claim 5). Example: $(39,60)$,
barrier pair for the unsharpened lever (Claim 4), satisfies
$P(39,60)^2 = 67{,}136{,}099{,}055{,}684{,}409 \le C(120,39)
= 5.657\ldots \times 10^{31}$ — closed by a factor of $\approx
8.4 \times 10^{14}$ in the squared comparison.

### Claim 8 (PROVED, by exact computation): $(\ast\ast)$ holds for every R1 pair with $i \le 1000$ except $(4,7)$ and $(10,19)$

Exact integer scan (Python stdlib, `math.comb`, primorial built
incrementally; Appendix A): of the **249,500** R1 pairs with
$1 \le i \le 1000$, the refined condition $(\ast\ast)$ fails for
exactly two pairs:

* $(4,7)$: $P = 5 \cdot 7 = 35$, $P^2 = 1225 > C(14,4) = 1001$
  (fails by a factor $1.224$);
* $(10,19)$: $P = 11\cdot13\cdot17\cdot19 = 46{,}189$,
  $P^2 = 2{,}133{,}423{,}721 > C(38,10) = 472{,}733{,}756$
  (fails by a factor $4.513$).

For $i < 40$ this says: $(\ast\ast)$ closes **359 of 361** R1 pairs,
versus 34 closed by the $J_1$ condition $(\ast)$ and 14 by crude
cardinality (Claim 6). The next-worst ratio after the two failures
is $0.572$ at $(57,113)$, so the two failures are isolated small-$i$
fluctuations, not a trend.

### Claim 9 (PROVED, modulo two cited published estimates): $(\ast\ast)$ holds for every R1 pair with $i > 1000$

*Cited inputs (published explicit estimates, taken as given, in the
same spirit as citing EEES78).* (D1) $|\theta(x) - x| < 3.965\,
x/\log^2 x$ for all $x > 1$ (Dusart). (D2) $\theta(x) < 1.000081\,x$
for all $x > 0$ (Rosser–Schoenfeld/Schoenfeld). Here
$\log P(i,j) = \theta(j) - \theta(i)$.

*Proof.* Write $c = j/i \in (3/2, 2)$ and $t = i/(2j) = 1/(2c) \in
(1/4, 1/3)$.

*Upper side.* By (D1) at $x = i > 1000$,
$\theta(i) > i\big(1 - 3.965/\log^2 i\big) \ge i(1 - 0.0831)$, and by
(D2), $\theta(j) < 1.000081\,j$. Hence
$$ \log P(i,j) \;<\; \big(1.000081\,c - 0.9169\big)\, i. $$

*Lower side.* $\log C(2j,i) \ge 2j\, h(t) - \log(2j+1)$, where
$h(t) = -t\log t - (1-t)\log(1-t)$: indeed, in the binomial
distribution on $2j$ trials with success probability $t = i/(2j)$,
the term at $k = i$ is the mode (since $(2j+1)t = i + t \in (i, i+1)$),
it is $\ge 1/(2j+1)$ because $2j+1$ terms sum to 1, and it equals
$C(2j,i)\, 2^{-2j H_2(t)}$. Thus
$\tfrac12 \log C(2j,i) \ge \big(c\, h(1/(2c))\big) i -
\tfrac12 \log(2j+1)$.

*Comparison.* Let $\Psi(c) = c\,h(1/(2c)) - 1.000081\,c + 0.9169$.
With $u = 1/(2c)$, $\frac{d}{dc}\big[c\,h(1/(2c))\big] = -\log(1-u)
\le -\log(2/3) = 0.4055$ on $c \in [3/2, 2]$ (direct differentiation:
$\frac{d}{du}[h(u)/(2u)] = \log(1-u)/(2u^2)$ and $du/dc = -2u^2$), so
$\Psi'(c) \le 0.4055 - 1.000081 < 0$: $\Psi$ is decreasing, and
$$ \Psi(c) \;\ge\; \Psi(2) \;=\; 2h(1/4) - 2.000162 + 0.9169
\;=\; 1.124670 - 2.000162 + 0.9169 \;=\; 0.04141. $$
Finally $\tfrac12\log(2j+1)/i \le \tfrac12 \log(4005)/1001 < 0.00415$
for $i > 1000$. Net margin: $0.04141 - 0.00415 = 0.03726 > 0$ per
unit $i$, i.e. $\log P(i,j) < \tfrac12 \log C(2j,i)$ strictly, which
is $(\ast\ast)$. $\square$

### Claim 10 (PROVED, from established inputs): the two exceptional pairs $(4,7)$ and $(10,19)$ are not counterexamples either

For these pairs the finite reduction gives $N(4,7) = 17$ and
$N(10,19) = 55$ (exact, Appendix A), so any counterexample would
have $14 \le n \le 17$ resp. $38 \le n \le 55$ — inside the
established clean sweep to $n \le 20{,}000$. The EEES78 exception
list contains no pair $(n, 4)$ with $n \ge 14$ and no pair with
$i = 10$, so the reduction applies. Hence no counterexample exists
at these two pairs. $\square$

### Claim 11 (PROVED modulo the named inputs): R1 is closed

Combining Claims 7–10: there is no counterexample to #699 with
$3i/2 < j < 2i$, for any $i$, provided $(n,i)$ is not an EEES78
exception pair (those are discharged in the established ground
truth). The inputs are exactly: S10's R1 characterisation
($S(n,i) \subseteq [i,j]$, $e_p = 1$), EEES78, the key lemma, the
finite reduction and sweep (only for two small pairs), and the two
cited explicit $\theta$ estimates (D1), (D2) (only for $i > 1000$).
No part of this claim is asserted beyond those inputs; in
particular this does **not** close R2, R3, or #699 as a whole.

### Claim 12 (PROVED for the density statement; the rest is a proved limitation): the CRT/density lever (option (a)) on $(39,59)$ — what it can and cannot do

For the five primes $41, 43, 47, 53, 59$ with $d = 20$, badness
requires $A_p = 0$, i.e. $(n-39) \bmod p \in [20, p-1]$: exactly
$p - d$ residue classes mod $p$ per prime. By CRT the combined
system has exactly
$$ \prod (p - d) = 21 \cdot 23 \cdot 27 \cdot 33 \cdot 39 = 16{,}783{,}767
\quad\text{favourable classes mod}\quad
M = \prod p = 259{,}106{,}347, $$
a density of $16{,}783{,}767 / 259{,}106{,}347 = 0.064776\ldots$
*What this proves:* the residue system is exactly periodic with
period $M$ and the stated density — simultaneous $A_p = 0$ is a
positive-density, CRT-realised event, never an incompatibility.
*What it cannot prove:* anything about the actual reduction
interval $[2j, N(39,59)] = [118, 119]$, which has length 2 against a
period of $259{,}106{,}347$ (a factor $1.3 \times 10^8$ smaller).
The density heuristic "expects" $2 \times 0.0648 = 0.130$ hits in
the interval, yet **both** $n = 118$ and $n = 119$ satisfy all five
conditions with $e_p = 1$ (verified exactly, Appendix A) — a
heuristic expectation below 1 is not an upper bound, and no
sieve/CRT counting argument can return "$0$ solutions" for an
interval that in fact contains 2. Nor does the residue system see
the conditions that actually kill these triples: $e_p = 1$ needs a
mod-$p^2$ lift (the crossed multiple of $p$ must not be a multiple
of $p^2$), and $S(n,i) \subseteq [i,j]$ / the prime-free interval
condition (S10, Theorem S10 item 5) are invisible to congruences
mod $M$ — at $n = 119$ the interval $(80, 119]$ contains 8 primes,
the exact opposite of prime-free. Density is a statement about
long intervals; the reduction interval here has length 2. **A
density argument can prove abundance of simultaneous-bad $n$ in
long ranges; it cannot exclude them in the reduction interval.**

---

## 3. Task 3 — combined-cap recount (exact computation)

### Claim 13 (PROVED, by exact computation): combined count $= 377$, maximum $5$, cap kills $0$

Replicating S10's search (R1 pairs $i < 40$; $n \in [2j, N(i,j)]$;
triples where $S(n,i) \cap [i,j]$ has $\ge 3$ primes, all
window-bad, $\Delta_p \ge e_p$; Legendre exponents throughout;
Appendix A): **377 triples**, distribution by simultaneous bad
count $\{3 : 195,\ 4 : 166,\ 5 : 16\}$, maximum **5**, over 116
distinct $(i,j)$ pairs and 10,317 scanned triples. Imposing
additionally the key-lemma cap $e_p \le v_p(C(j, j-i))$ on every
$p \in S(n,i) \cap [i,j]$: **exactly 377 triples again, maximum 5,
and the cap kills 0 of the 377.** $(119,39,59)$ (and $(118,39,59)$)
satisfy the combined condition. The combined necessary condition of
S10 §7(a), $e_p \le \min(\Delta_p,\ B_p - v_p(d!))$, is therefore
**exactly equivalent** to window-badness alone on this entire R1
range — it removes nothing.

### Claim 14 (PROVED): the recount outcome is forced — in R1 the key-lemma cap is automatic given window-badness

Let $p \in S(n,i) \cap [i,j]$ be window-bad in R1. The key-lemma cap
is $v_p(C(j,d)) = B_p - v_p(d!)$ (S10 §7(a)). If $p > i$: $B_p = 1$
(S10, Theorem 3(a)) and $v_p(d!) = 0$ (since $p > d$ in R1), so the
cap is $e_p \le 1$; window-badness forces $e_p = 1$ (S10, Theorem
3(b)), so the cap holds with equality. If $p = i$ (prime):
window-badness is impossible (S10, Theorem 3(b)), so no counted
triple contains it. Hence in R1 *every* window-bad prime
automatically satisfies the cap, for every $(i,j)$ — the empirical
"0 killed" of Claim 13 is a theorem, and the combined cap can only
ever bite outside R1 (lower band / R3), where $B_p - v_p(d!)$ and
$\Delta_p$ are genuinely incomparable. $\square$

---

## 4. Task 4 — final statement

### Claim 15 (PROVED, summary): the strongest counting bound

For a hypothetical counterexample in R1 ($3i/2 < j < 2i$,
$(n,i)$ not an EEES78 exception pair):

$$ C(2j,i)^{1/2} \;<\; V_i(n) \;=\; \prod_{p\ \mathrm{bad}} p
\;\Big|\; P(i,j) \;=\; \prod_{i<p\le j} p \;\Big|\; C(j,i),
\qquad b = |S(n,i)| \le \pi(j) - \pi(i), $$

with every inequality in the chain proved above (Claims 1, 2, 7).
The strongest *usable* form is the middle one, $V_i(n) \mid P(i,j)$:
it converts the support information ($e_p = 1$, primes confined to
$(i, j]$, each with $v_p(C(j,i)) = 1$) into a primorial upper bound
that is typically $10^{7}$–$10^{15}$ times smaller than the
$C(j,i)$ bound the plain T1 lever uses.

### Claim 16 (PROVED): the exact boundary where each size argument caps out

* The $C(j,i)$ lever caps out exactly at the curve
  $C(2j,i) = C(j,i)^2$ (Del Pin's $J_1$): it closes precisely
  $j \le J_1(i)$, and at the first pair beyond, e.g. $(39,60)$, its
  two constraints are simultaneously satisfiable (Claim 4).
* Crude cardinality counting caps out much earlier: it closes only
  14 of 361 R1 pairs at $i < 40$ and merely pins $b = 9$ at
  $(39,59)$ and $(39,60)$ (Claim 6).
* The primorial lever caps out at the curve $P(i,j)^2 = C(2j,i)$,
  which on the computed range $i \le 1000$ is crossed only at
  $(4,7)$ and $(10,19)$, and is provably (modulo (D1), (D2)) never
  crossed for $i > 1000$; the analytic margin at the worst corner
  $j \to 2i$ is $\approx 0.037$ in $\log$ per unit $i$ and grows
  with $i$ (Claims 8, 9). Together with the finite reduction this
  closes R1 (Claim 11). The in-range configurations themselves
  (e.g. $P = 259{,}106{,}347$ at $(119,39,59)$, seven orders of
  magnitude below the EEES threshold) are *not* excluded by any of
  these levers individually — they are excluded as counterexamples
  only because a counterexample would force $V_i(n)$ to equal an
  in-range product (Claim 5).

### Claim 17 (OPEN): what a completion beyond R1 still needs

R1 yielded because in R1 the support of $V_i(n)$ collapses to
squarefree primes in a short interval, turning a size estimate into
a counting estimate. Outside R1 this collapse fails, and no purely
size/counting input in this file touches: (i) **R2** ($j = 2i$),
where the prime $i$ itself enters with the multi-scale condition of
S10, Theorem 5; (ii) **R3's lower band** $p \in [i, j/2]$, where
$e_p$ can be as large as $\lfloor \log_p j \rfloor$, $V_i(n)$ is not
squarefree, the primorial bound is unavailable, and the combined
cap $e_p \le \min(\Delta_p, B_p - v_p(d!))$ is the strongest
statement proved here (Claim 14 shows it is exactly in R3-type
territory that this cap can bite); (iii) an **EEES-free** version
of any of this — every closure in §2 uses $V_i(n) > C(n,i)^{1/2}$,
and replacing it needs a strengthened smooth-part estimate, not a
counting trick. A completion needs a genuinely non-size input:
control of the primes $> j$ in $S(n,i)$ (prime-gap / forced-prime
arguments in the interval $(\max(j, n-i), n]$, S10 task T2), or a
multi-scale incompatibility in the lower band exploiting that
residues mod $p^{k+1}$ determine residues mod $p^k$ (S10 task T3),
or, for the $i = 3$ case left open by the external claims, an
argument retaining *which* of $n, n-1, n-2$ supplies each prime
power rather than aggregate exponents. Counting has done what
counting can do: in R1, it turned out to be enough.

---

## Appendix A — computations (Python stdlib only, exact arithmetic)

All numbers above were produced by the following code (run
2026-10-29; total runtime dominated by the $i \le 1000$ scan,
$\approx$ 130 s; everything else seconds).

```python
import math

def vp_fact(N, p):
    t = 0
    while N:
        N //= p; t += N
    return t

def vp_binom(n, k, p):
    return vp_fact(n, p) - vp_fact(k, p) - vp_fact(n - k, p)

def primes_upto(b):
    s = bytearray(b'\x01') * (b + 1); s[0:2] = b'\x00\x00'
    for q in range(2, int(b**0.5) + 1):
        if s[q]:
            s[q*q::q] = b'\x00' * (((b - q*q)//q) + 1)
    return [x for x in range(b + 1) if s[x]]

def N_of(i, j):
    target = math.comb(2*j, 2*(j - i)); n = 2*j
    while math.comb(n, i) < target: n += 1
    return n - 1

# --- Claim 5 numerics ---
P = 41*43*47*53*59                      # 259106347
assert math.comb(59, 39) % P == 0 and math.comb(59, 39)//P == 10785390
for N in (118, 119, 238):
    v = math.comb(N, 39); r = math.isqrt(v)
    assert r*r <= v < (r+1)*(r+1)
assert math.comb(118, 39) > math.comb(59, 39)**2      # (39,59): (*) holds
assert math.comb(120, 39) < math.comb(60, 39)**2      # (39,60): (*) fails
# J1(39) = 59 within R1:
assert all(math.comb(2*j, 39) < math.comb(j, 39)**2 for j in range(60, 78))
# realised V_39(119) = P * Q, V^2 > C(119,39):
S119 = [p for p in primes_upto(119) if p >= 39 and vp_binom(119, 39, p) > 0]
V = 1
for p in S119: V *= p ** vp_binom(119, 39, p)
assert V**2 > math.comb(119, 39)

# --- Claim 12: both n = 118, 119 satisfy all five badness conditions ---
for n in (118, 119):
    for p in (41, 43, 47, 53, 59):
        e = vp_binom(n, 39, p)
        D = (vp_fact(59, p) - vp_fact(39, p)) - (vp_fact(n-39, p) - vp_fact(n-59, p))
        assert e == 1 and D >= e

# --- Claims 6-8: refined / crude / J1 conditions over R1 pairs ---
def primorial(i, j, primes):
    v = 1
    for p in primes:
        if i < p <= j: v *= p
    return v

# exact scan, i <= 1000: refined failures are exactly (4,7), (10,19)
Pset = set(primes_upto(2000)); fails = []; total = 0
for i in range(1, 1001):
    prod = 1
    for j in range(i + 1, 2*i):
        if j in Pset: prod *= j
        if 2*j <= 3*i: continue
        total += 1                       # total == 249500
        if prod*prod > math.comb(2*j, i): fails.append((i, j))
assert fails == [(4, 7), (10, 19)]
assert N_of(4, 7) == 17 and N_of(10, 19) == 55

# --- Claim 13: combined-cap recount, R1 pairs i < 40 ---
window = []; combined = []
for i in range(1, 40):
    for j in range(i + 1, 2*i):
        if 2*j <= 3*i: continue
        d = j - i; N = N_of(i, j)
        if N < 2*j: continue
        primes = [p for p in primes_upto(j) if p >= i]
        kl = {p: vp_binom(j, d, p) for p in primes}
        for n in range(2*j, N + 1):
            S = []; data = {}
            for p in primes:
                e = vp_binom(n, i, p)
                if e > 0:
                    S.append(p)
                    data[p] = (e, (vp_fact(j, p) - vp_fact(i, p))
                               - (vp_fact(n - i, p) - vp_fact(n - j, p)))
            if len(S) >= 3 and all(data[p][1] >= data[p][0] for p in S):
                window.append((n, i, j, tuple(S)))
                if all(data[p][0] <= kl[p] for p in S):
                    combined.append((n, i, j, tuple(S)))
assert len(window) == 377 and len(combined) == 377
assert max(len(x[3]) for x in window) == 5
print("all P-H1 checks passed")
```

*End of P-H1.*
