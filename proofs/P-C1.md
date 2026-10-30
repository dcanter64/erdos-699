# Prover C1 (independent): Strategy S3 formalized

**Subject.** Erdős Problem #699: for $1 \le i < j \le n/2$, the binomial
coefficients $\binom{n}{i}$ and $\binom{n}{j}$ share a prime factor $\ge i$.

**Role and independence.** This is the independent Prover C1 document for
Strategy S3 (large prime factors and prime gaps), written from
`strategies/S3.md` alone. The other prover's work was not read.

**Established inputs (taken as given, not reproved here).**

1. *Phase 0 reduction.* Outside the 12 EEES78 exception pairs
   $(n_0,i_0) \in \{(8,3),(9,4),(10,5),(12,5),(21,7),(21,8),(30,7),
   (33,13),(33,14),(36,13),(36,17),(56,13)\}$, a counterexample
   $(n,i,j)$ satisfies $\binom{n}{i} < \binom{2j}{2(j-i)}$, hence
   $2j \le n \le N(i,j)$, where
   $$N(i,j) := \max\{n : \tbinom{n}{i} < \tbinom{2j}{2(j-i)}\}.$$
   The 12 exception pairs are discharged directly in
   `erdos-699/RESULTS.md` (41 admissible triples, all with gcd $> 1$;
   two pairs vacuous).
2. *Closed region.* Every pair with $j \le 3i/2$ is settled for all $n$
   (Phase 0). The open region is $j > 3i/2$.
3. *Sweep.* No counterexample exists with $n \le 10000$ in the open
   region. Of the $4{,}249{,}500$ pairs with $1 \le i \le 1000$,
   $j > 3i/2$, $2j \le 10000$: $768{,}741$ are fully cleared
   ($N(i,j) \le 10000$) and $3{,}480{,}759$ are partially covered
   ($N(i,j) > 10000$). For each $i$, the fully cleared $j$ form the
   prefix $\lfloor 3i/2 \rfloor < j \le J_i$ (`pairpass.json`).

**Standing notation.** Throughout, $1 \le i < j \le n/2$, $p$ is prime,
$\log$ is natural, and Legendre's formula
$v_p\binom{n}{k} = \sum_{e \ge 1}\big(\lfloor n/p^e \rfloor -
\lfloor k/p^e \rfloor - \lfloor (n-k)/p^e \rfloor\big)$
is the only valuation tool used. A *counterexample* is a triple
$(n,i,j)$ in range whose two binomial coefficients have **no** common
prime divisor $\ge i$.

---

## 1. The single-hit lemmas

**Lemma C1.1 (task L1).** *If $n - j < p \le n$, then
$v_p\binom{n}{j} = 1$; in particular $p \mid \binom{n}{j}$.*

*Proof.* Since $j \le n/2$, $p > n - j \ge n/2$, so $\lfloor n/p \rfloor
= 1$ and $p^2 > n$, hence every $e \ge 2$ Legendre term is $0$.
Also $\lfloor j/p \rfloor = 0$ (as $j \le n/2 < p$) and
$\lfloor (n-j)/p \rfloor = 0$ (as $n - j < p$). Therefore
$v_p\binom{n}{j} = 1 - 0 - 0 = 1$. $\square$

**Lemma C1.2 (task L2).** *If $n - i < p \le n$, then
$v_p\binom{n}{i} = 1$; in particular $p \mid \binom{n}{i}$.*

*Proof.* Identical to Lemma C1.1 with $i$ in place of $j$:
$p > n - i \ge n/2$ gives $\lfloor n/p \rfloor = 1$,
$\lfloor i/p \rfloor = 0$, $\lfloor (n-i)/p \rfloor = 0$. $\square$

**Lemma C1.3 (task L3, corrected form).** *Let $n/2 < p \le n$ and
$1 \le k \le n/2$. Then*
$$v_p\tbinom{n}{k} = \begin{cases} 1, & k > n - p, \\ 0, & k \le n - p,
\end{cases}
\qquad\text{i.e.}\qquad p \mid \tbinom{n}{k} \iff k > n - p.$$
*Consequently:*

*(i) (the useful interval) if $p \in (n-i, n]$, then $p$ divides both
$\binom{n}{i}$ and $\binom{n}{j}$, and $p > i$;*

*(ii) (wasted primes) if $p \in (n-j, n-i]$, then
$p \mid \binom{n}{j}$ but $p \nmid \binom{n}{i}$;*

*(iii) if $n/2 < p \le n - j$, then $p$ divides neither coefficient.*

*Proof.* Since $p > n/2$: $\lfloor n/p \rfloor = 1$, $p^2 > n$ kills
all $e \ge 2$ terms, and $\lfloor k/p \rfloor = 0$ since
$k \le n/2 < p$. Moreover $n/2 \le n - k < n < 2p$, so
$\lfloor (n-k)/p \rfloor$ is $0$ if $n - k < p$ and $1$ if
$n - k \ge p$; i.e. it is $0$ iff $k > n - p$ and $1$ iff
$k \le n - p$. Hence $v_p\binom{n}{k} = 1 - 0 - \lfloor (n-k)/p
\rfloor \in \{0,1\}$ with the stated dichotomy.

(i) $p > n - i$ means $i > n - p$, and $j > i > n - p$, so the
dichotomy gives $v_p = 1$ for both $k = i$ and $k = j$. Also
$p > n/2 \ge j > i$.

(ii) $p \in (n-j, n-i]$ means $j > n - p \ge i$, so the dichotomy
gives $v_p\binom{n}{j} = 1$ and $v_p\binom{n}{i} = 0$.

(iii) $p \le n - j < n - i$ gives $j \le n - p$ and $i \le n - p$,
so both valuations are $0$. $\square$

**Remark (the naive claim is false, and why).** The claim "every
prime in $(n-j, n]$ divides both coefficients" is false: the
inclusion goes the wrong way, since $j > i$ implies
$(n-i, n] \subsetneq (n-j, n]$, and the annulus $(n-j, n-i]$ is
exactly the wasted case (ii). Counterexample, verified by direct
computation: $(n,i,j,p) = (20,3,9,13)$. Here $13 \in (n-j, n] =
(11, 20]$ and indeed $13 \in (n-j, n-i] = (11, 17]$, case (ii):
$\binom{20}{9} = 167960 = 13 \cdot 12920$, but
$\binom{20}{3} = 1140 = 13 \cdot 87 + 9$, so $13 \nmid \binom{20}{3}$.
Among primes $> n/2$, Lemma C1.3 says the common divisors of the two
coefficients are *exactly* the primes in $(n-i, n]$; nothing in
$(n/2, n-i]$ can serve. Every closure below is therefore governed by
$i$, not by $j$. (Independent numerical check by this prover: the
dichotomy of Lemma C1.3 held for every prime $p \in (n/2, n]$ in
3000 random triples $(n,i,j)$ with $n \le 600$, no violations;
script in §6.)

**Corollary C1.4 (task GAP: gap forcing).** *If $(n,i,j)$ is a
counterexample, then the interval $(n-i, n]$ contains no prime.
Equivalently, writing $p_-(n)$ for the largest prime $\le n$ and
$p_+(n)$ for the next prime after $p_-(n)$, one has
$p_-(n) \le n - i$ and the prime gap straddling $n$ satisfies*
$$p_+(n) - p_-(n) \ge i + 1.$$

*Proof.* If a prime $p$ lay in $(n-i, n]$, Lemma C1.3(i) would make
$p$ a common divisor of $\binom{n}{i}$ and $\binom{n}{j}$ with
$p > i$, contradicting the definition of a counterexample. Hence no
prime lies in $(n-i, n]$. The largest prime $p_-(n) \le n$ therefore
satisfies $p_-(n) \le n - i$ (note $p_-(n)$ exists: $n \ge 2j \ge 4$).
Since $p_+(n) > n$ and both are integers, $p_+(n) \ge n + 1$, so
$p_+(n) - p_-(n) \ge (n+1) - (n-i) = i + 1$. $\square$

The $+1$ is exact and load-bearing: a counterexample needs a gap of
length at least $i+1$ (not $i$) straddling $n$, with lower end
$p_-(n) \le n - i$.

---

## 2. A uniform bound on $N(i,j)$

**Lemma C1.5 (task L4).** *For all $1 \le i < j$,*
$$N(i,j) \;<\; \frac{e^{2} j^{2}}{i} \;\le\; e^{2} j^{2}.$$

*Proof.* Two elementary binomial bounds.

(a) $\binom{N}{K} \le (eN/K)^K$ for $1 \le K \le N$: indeed
$\binom{N}{K} \le N^K / K!$, and $e^K = \sum_{t \ge 0} K^t/t! \ge
K^K/K!$ gives $K! \ge (K/e)^K$, so $\binom{N}{K} \le (eN/K)^K$.

(b) $\binom{n}{i} \ge (n/i)^i$ for $i \le n$: indeed
$\binom{n}{i} = \prod_{t=0}^{i-1} \frac{n-t}{i-t}$, and each factor
satisfies $\frac{n-t}{i-t} \ge \frac{n}{i}$, because
$i(n-t) - n(i-t) = t(n-i) \ge 0$.

By symmetry $\binom{2j}{2(j-i)} = \binom{2j}{2i}$, and (a) with
$N = 2j$, $K = 2i$ gives
$\binom{2j}{2(j-i)} \le \big(\frac{e \cdot 2j}{2i}\big)^{2i}
= (ej/i)^{2i}$.
Now let $n$ be an integer with $n \ge e^2 j^2 / i$. By (b),
$\binom{n}{i} \ge (n/i)^i \ge \big(e^2 j^2/i^2\big)^i = (ej/i)^{2i}
\ge \binom{2j}{2(j-i)}$.
So $\binom{n}{i} \ge \binom{2j}{2(j-i)}$: this $n$ is not in the set
whose maximum is $N(i,j)$, and since $\binom{n}{i}$ is strictly
increasing in $n$, no larger integer is in the set either. Hence
$N(i,j) \le n - 1$ for every integer $n \ge e^2j^2/i$. Taking
$n = \lceil e^2j^2/i \rceil$ gives
$N(i,j) \le \lceil e^2j^2/i \rceil - 1 < e^2j^2/i$ (the last
inequality holds both when $e^2j^2/i$ is an integer, giving
$N(i,j) \le e^2j^2/i - 1$, and when it is not, giving
$N(i,j) \le \lfloor e^2j^2/i \rfloor < e^2j^2/i$).
Finally $i \ge 1$ gives $e^2j^2/i \le e^2 j^2$. $\square$

*Sharpness remark.* The bound is within a factor $e$ of the truth:
for $i = 1$ exactly, $\binom{n}{1} = n < \binom{2j}{2} = j(2j-1)$
gives $N(1,j) = j(2j-1) - 1 \approx 2j^2$, against the bound
$e^2 j^2 \approx 7.39 j^2$; Stirling gives $N(i,j) \approx ej^2/i$
for $i \ll j$. (Verified numerically: $N(1,j) = j(2j-1)-1$ at
$j = 5, 71, 200, 1000$; $N(i,j) < e^2j^2/i$ on all spot-checked
pairs including $(132, 5000)$, $(1000, 5000)$, $(17,71)$ with
$N(17,71) = 621$; §6.)

---

## 3. The table criterion

**Definition (S3's $G$).** $G(X) := \max\{p_{k+1} - p_k : p_k < X\}$,
the maximal prime gap whose *lower* end is $< X$. $G$ is
nondecreasing, and it changes only at first-occurrence (record) gaps:
if the record gaps with lower ends $< X$ are known, $G(X)$ is the
largest of them.

**Theorem C1.6 (task T-A: table criterion).** *Let $(i,j)$ be any
pair (in particular any open pair, $j > 3i/2$) such that*
$$i \;\ge\; G(N(i,j)).$$
*Then there is no counterexample $(n,i,j)$ for any $n$; the pair
$(i,j)$ is fully cleared.*

*Proof, with all off-by-ones made explicit.* Suppose, for a
contradiction, that $(n,i,j)$ is a counterexample. By the Phase 0
reduction (input 1), apart from the EEES78 exception pairs, which
are discharged directly in RESULTS.md and are not counterexamples,
$2j \le n \le N(i,j)$; recall also $j \le n/2$ by the range of the
problem, so $n \ge 2j$ is the full range to exclude.

Fix this $n \le N(i,j)$. By Corollary C1.4, $(n-i, n]$ is prime-free,
$p_-(n) \le n - i$, and the straddling gap satisfies
$p_+(n) - p_-(n) \ge i + 1$. Now the counting step: this gap is one
of the gaps maximised over in $G(N(i,j))$, because its lower end
satisfies
$$p_-(n) \;\le\; n - i \;\le\; N(i,j) - i \;<\; N(i,j),$$
using $n \le N(i,j)$ and $i \ge 1$. The inequality $p_-(n) < N(i,j)$
is *strict*, matching the strict condition $p_k < X$ in the
definition of $G$ with $X = N(i,j)$; no endpoint convention is
strained. Hence
$$G(N(i,j)) \;\ge\; p_+(n) - p_-(n) \;\ge\; i + 1 \;>\; i,$$
contradicting the hypothesis $i \ge G(N(i,j))$. (Note the criterion
is $i \ge G$, not $i > G$: the contradiction needs exactly the
$i+1$ produced by Corollary C1.4. A hypothesis $i \ge G - 1$ would
not suffice.)

Therefore no $n \in [2j, N(i,j)]$ admits a counterexample, and
$n > N(i,j)$ is excluded by Phase 0. Equivalently, positively: for
every $2j \le n \le N(i,j)$, $(n-i, n]$ contains a prime, which by
Lemma C1.3(i) divides both $\binom{n}{i}$ and $\binom{n}{j}$ and
exceeds $i$. $\square$

**Why the criterion is checkable.** $N(i,j)$ is a specific integer
(exactly computable by binary search on
$\binom{n}{i} < \binom{2j}{2(j-i)}$, or bounded above by Lemma C1.5,
which suffices since $G$ is nondecreasing: $i \ge G(B)$ for any
proved upper bound $B \ge N(i,j)$ also gives $i \ge G(N(i,j))$).
$G$ at that argument is read off the first-occurrence prime gap
table. This is the entire mechanism of §5 below.

---

## 4. Theorem B: the explicit-theorem region

**Cited explicit prime-gap theorems.** Each has the form: for
$x \ge x_0$ there is a prime in $(x,\ x(1 + C/\log^m x)]$. All
$\log$ natural.

| # | Source | $x_0$ | $C$ | $m$ | This prover's verification |
|---|---|---|---|---|---|
| D10 | Dusart 2010, arXiv:1002.0442, Prop. 6.8 | $396738$ | $1/25$ | $2$ | Verified verbatim in the original text: "for $x \ge 396\,738$, $x < p \le x(1 + 1/(25\ln^2 x))$" |
| T14 | Trudgian 2014, arXiv:1401.2689, Cor. 2 | $2898329$ (see flag) | $1/111$ | $2$ | Read in the original; see Flag F1 below |
| D18a | Dusart 2018, *Ramanujan J.* 45, Cor. 5.5 | $468991632$ | $1/5000$ | $2$ | Constants match the independent survey table in Caffarelli, *Mathematics* 2018, 6, 289 (arXiv:1804.02500), Thm. 6; not read in Dusart's own text in this pass, see Flag F2 |
| D18b | Dusart 2018, *Ramanujan J.* 45, Prop. 5.4 | $89693$ | $1$ | $3$ | Same as D18a |
| A17 | Axler 2017, arXiv:1703.08032, Thm. 4.1 (= Thm. 1.4) | $6034256$ | $0.087$ | $3$ | Verified verbatim in the original text: "for every $x \ge 6\,034\,256$, $x < p \le x(1 + 0.087/\log^3 x)$" |

**Conversion.** Apply a cited theorem at $x = n - i \ge x_0$. It
produces a prime $p$ with $n - i < p \le (n-i)\big(1 +
C/\log^m(n-i)\big)$. This $p$ lies in $(n-i, n]$, as
Lemma C1.3(i) requires, exactly when
$(n-i)\, C/\log^m(n-i) \le i$. Hence the sufficient condition
$$i \;\ge\; \frac{C\,(n-i)}{\log^m (n-i)}, \qquad n - i \ge x_0,$$
rules out a counterexample at this $n$, by Corollary C1.4. (The
cleaner sufficient condition $i \ge Cn/\log^m n$ also works: the
function $x \mapsto x/\log^m x$ has derivative
$\log^{m-1} x\,(\log x - m)/\log^{2m} x > 0$ for $x > e^m$, and
$n - i < n$.)

**Theorem C1.7 (task T-B: Theorem B, S3's corrected $i$-based
form).** *There is no counterexample $(n,i,j)$, for any $j$, in any
of the following regions:*

* *(B1, Dusart 2010)* $n - i \ge 396738$ and
  $i \ge \dfrac{n-i}{25\log^2(n-i)}$. In particular the clean region
  $\{\,i > n/\big(25(\log n)^2\big),\ n - i \ge 396738\,\}$ is
  counterexample-free.
* *(B2, Dusart 2018)* $n - i \ge 468991632$ and
  $i \ge \dfrac{n-i}{5000\log^2(n-i)}$.
* *(B3, Axler 2017)* $n - i \ge 6034256$ and
  $i \ge \dfrac{0.087\,(n-i)}{\log^3(n-i)}$, the strongest of the
  three whenever $\log n < 435$.

*Proof.* Corollary C1.4 plus the conversion, applied with (D10),
(D18a), (A17) respectively. For the clean form of (B1):
$x \mapsto x/\log^2 x$ is increasing for $x > e^2$, and
$n - i \ge 396738 > e^2$, so
$(n-i)/\big(25\log^2(n-i)\big) \le n/\big(25\log^2 n\big) < i$,
which is the (B1) condition. $\square$

**Remark (the two remaining table rows).** The same conversion
applied to (T14) and (D18b) gives the further regions
$n - i \ge 2898329$, $i \ge (n-i)/\big(111 \log^2(n-i)\big)$, and
$n - i \ge 89693$, $i \ge (n-i)/\log^3(n-i)$. S3's Theorem B states
only (B1) to (B3); (B3) dominates (D18b) and (B1)/(B2) dominate
(T14) in their ranges, so nothing is lost.

**Flag F1 (Trudgian threshold).** In arXiv:1401.2689v2, Corollary 2
as printed states the threshold $x \ge 2898239$ and a *closed*
interval $[x, x(1 + 1/(111\log^2 x))]$. The survey table (and S3)
give $2898329$, a digit transposition, with the open interval form.
Since $2898329 > 2898239$, every use of the larger threshold is a
fortiori valid for the closed-interval statement; and Trudgian's
row is not used in Theorem C1.7 at all (see the remark above), so
this discrepancy touches nothing downstream. It is recorded here
because a referee should not have to discover it.

**Flag F2 (Dusart 2018).** The (D18a)/(D18b) constants and
thresholds were verified against an independent published survey
table, not against Dusart's *Ramanujan J.* 45 text itself, in this
pass. (B2) is the only part of Theorem C1.7 resting on (D18a). If a
referee requires original-text verification of Cor. 5.5, that is the
one citation still to be sighted; (B1) and (B3) are sighted
verbatim above, and neither Theorem C1.6 nor C1.8 depends on any of
§4.

---

## 5. Theorem C: table closures and the count

**Table input.** Oliveira e Silva, Herzog and Pardi, *Math. Comp.*
83 (2014), 2033–2060: all prime gaps below $4 \cdot 10^{18}$
computed; the maximal gap with lower end below $4\cdot 10^{18}$ is
$1476$, first occurring after the prime $1425172824437699411$.
Hence $G(X) \le 1476$ for all $X \le 4\cdot 10^{18}$. First-occurrence
records used below (same tables; OEIS A002386/A005250): gap $36$
after $9551$; $72$ after $31397$; $86$ after $155921$; $96$ after
$360653$; $112$ after $370261$; $114$ after $492113$; $118$ after
$1349533$; $132$ after $1357201$; $148$ after $2010733$; $154$ after
$4652353$; $180$ after $17051707$; $222$ after $122164747$. This
prover independently recomputed all records with lower end
$< 2.1 \cdot 10^6$ by a direct sieve (records: $36$ after $9551$,
$44$ after $15683$, $52$ after $19609$, $72$ after $31397$, $86$
after $155921$, $96$ after $360653$, $112$ after $370261$, $114$
after $492113$, $118$ after $1349533$, $132$ after $1357201$, $148$
after $2010733$), confirming every record S3 uses in this range,
and $G(10127) = 36$, matching S3 §6's frontier observation.

**Theorem C1.8 (task T-C: Theorem C).**

*(C1) Every open pair $(i,j)$ with $i \ge 1476$ and
$j \le 7.35 \cdot 10^{8}$ is fully cleared.*

*Proof.* By Lemma C1.5, $N(i,j) < e^2 j^2/i \le e^2 j^2 \le
e^2 (7.35\cdot 10^8)^2 = 3.9918 \cdot 10^{18} < 4 \cdot 10^{18}$
(the exact threshold would be $j < 2\cdot 10^9/e = 735758882$;
$7.35\cdot 10^8$ is safely inside). Hence
$G(N(i,j)) \le 1476 \le i$, and Theorem C1.6 applies. $\square$

*(C2) Every open pair with $132 \le i \le 1000$ and $j \le 5000$ is
fully cleared. In particular, all $2{,}891{,}106$ partially covered
pairs in this range are newly fully cleared.*

*Proof of the closure.* By Lemma C1.5, for $i \ge 132$ and
$j \le 5000$,
$$N(i,j) \;<\; \frac{e^2 j^2}{i} \;\le\;
\frac{e^2 \cdot 5000^2}{132} \;=\; 1399442.44\ldots \;<\; 1.40\cdot 10^6
\;<\; 2010733,$$
so $N(i,j) \le 1399442$. Every prime gap with lower end
$< N(i,j) \le 1399442 < 2010733$ has length at most $132$: the
record table has gap $132$ first occurring after $1357201$ and the
next record, $148$, not occurring until after $2010733$; and this
prover's sieve gives directly $G(1400000) = 132$. Hence
$G(N(i,j)) \le 132 \le i$, and Theorem C1.6 applies to every such
pair, uniformly, with no per-pair computation. $\square$

*The count, reproduced independently.* The partially covered pairs
with given $i$ are exactly $J_i < j \le 5000$, where $J_i$ is the
sweep's maximal fully cleared $j$; their number is $5000 - J_i$.
Reading $J_i$ from `erdos-699/pairpass.json` (equivalently the
RESULTS.md appendix) and summing,
$$\sum_{i=132}^{1000} \big(5000 - J_i\big) \;=\; 2{,}891{,}106,$$
**exactly S3's claimed count.** Cross-checks from the same run: the
total census is $4{,}249{,}500$ pairs, of which $768{,}741$ fully
cleared and $3{,}480{,}759$ partially covered, matching RESULTS.md;
the complementary partially covered count for $1 \le i \le 131$ is
$589{,}653$, and $2{,}891{,}106 + 589{,}653 = 3{,}480{,}759$. The
remaining open pairs in the range (those with $j \le J_i$) were
already fully cleared by the sweep, so (C2) leaves no pair with
$132 \le i \le 1000$, $j \le 5000$ unsettled. $\square$

*(C3) Per-pair criterion (decidable).* Any specific pair with
$N(i,j) \le 4\cdot 10^{18}$ and $i \ge G(N(i,j))$, with $N(i,j)$
computed exactly by binary search and $G$ read off the record
table (or a sieve, for $N(i,j)$ within sieving range), is fully
cleared by Theorem C1.6. Example, recomputed by this prover: every
$(i, 71)$ with $18 \le i \le 47$ satisfies the criterion (e.g.
$N(18,71) = 578$, $G = 18 \le 18$; $N(47,71) = 143$, $G = 14$),
while for $i \le 17$, $N(i,71) \le 10010$, and except for $(1,71)$
($N = 10010$) those pairs already satisfy $N \le 10000$, i.e. were
cleared by the sweep anyway. $\square$

---

## 6. Verification performed by this prover

All computations are Python standard library only; total wall time
under 3 seconds.

1. Counterexample of Lemma C1.3: $\binom{20}{9} = 167960$,
   $13 \mid \binom{20}{9}$; $\binom{20}{3} = 1140$,
   $13 \nmid \binom{20}{3}$.
2. Lemma C1.3 dichotomy: 3000 random triples $(n,i,j)$, $n \le 600$,
   every prime $p \in (n/2, n]$ checked against Legendre valuations:
   $v_p\binom{n}{k} = 1 \iff k > n - p$ for $k \in \{i,j\}$, and
   $v_p \in \{0,1\}$ throughout. Zero violations.
3. Count (C2): from `pairpass.json`, census $4{,}249{,}500$,
   cleared $768{,}741$, partial $3{,}480{,}759$, partial with
   $132 \le i \le 1000$: $\mathbf{2{,}891{,}106}$.
4. Prime gaps: sieve to $2.1\cdot 10^6$ reproducing every
   first-occurrence record S3 uses below that point;
   $G(1400000) = 132$, $G(10127) = 36$, $G(2010733) = 132$,
   $G(2010734) = 148$ (the last two display the strict lower-end
   convention of $G$ at work).
5. Lemma C1.5: exact $N(i,j)$ by binary search on spot pairs,
   including $N(1,j) = j(2j-1)-1$ ($j = 5, 71, 200, 1000$),
   $N(17,71) = 621$, $N(100,2000) = 103058$, $N(500,4000) = 76545$,
   $N(132,5000) = 500097$, $N(1000,5000) = 55305$, all strictly
   below $e^2j^2/i$, and the last three agreeing with S3 §6's table
   where they overlap.
6. (C3) example: exact $N(i,71)$ and sieve $G$ for $1 \le i \le 47$,
   confirming S3's claim in full.

## 7. Honest limits and discrepancies

1. **Sufficiency, not necessity.** The route sees only common
   primes $> n/2$. Where $(n-i, n]$ is prime-free for some
   $n \le N(i,j)$ the route is silent even though the triple is
   fine (e.g. $i = 17$, $j = 71$, $n = 540 \le N(17,71) = 621$:
   $(523, 540]$ is prime-free, the common prime is $\le n/2$).
   Theorem C1.6's criterion failing for a pair proves nothing
   against the pair.
2. **Small fixed $i$ is out of reach.** For fixed $i$,
   $N(i,j) \approx ej^2/i \to \infty$ while $G$ grows; $i = 1$ is
   extremal: the route fires only when $n$ is prime. The uncovered
   regime beyond the tables is $N(i,j) > 4\cdot 10^{18}$ with
   $i \lesssim 10^{12}$ (S3 §5, item 2), and no known explicit gap
   theorem reaches $i \ll N(i,j)^{0.525}$ (Baker–Harman–Pintz is
   non-explicit). None of this is hidden by the statements above:
   (C1) and (C2) are exactly as strong as claimed and no stronger.
3. **Discrepancies found.** (a) Flag F1: Trudgian's threshold as
   printed in arXiv:1401.2689v2 is $2898239$ with a closed interval;
   S3 (following the survey table) prints $2898329$ with an open
   interval. Conservative direction, unused downstream. (b) Flag
   F2: Dusart 2018 Cor. 5.5 / Prop. 5.4 verified via an independent
   survey table, not the original text, in this pass. (c) No
   discrepancy in any *proved* statement: Lemmas C1.1 to C1.5,
   Theorem C1.6, and Theorem C1.8 (including the count
   $2{,}891{,}106$) all check out exactly as S3 states them.

**Bottom line.** Strategy S3 is sound in its corrected form. The
naive observation (c) is false and S3's correction is necessary and
exact (Lemma C1.3, with the wasted-prime annulus $(n-j, n-i]$).
Gap forcing (Corollary C1.4) plus the table criterion
(Theorem C1.6, off-by-ones verified) yields Theorem C: the infinite
family $i \ge 1476$, $j \le 7.35\cdot 10^8$, and the complete
discharge of all $2{,}891{,}106$ partially covered pairs with
$132 \le i \le 1000$, $j \le 5000$. Theorem B (C1.7) is the correct
$i$-based explicit-theorem region, with (B1) and (B3) verified
against the original papers and (B2) flagged as survey-verified.
