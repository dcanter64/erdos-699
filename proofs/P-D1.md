# Prover D1 (independent) — Strategy S4: Kummer Digit Classification

**Problem (Erdős #699).** For $1 \le i < j \le n/2$, show
$\gcd(V_i(n), \binom{n}{j}) > 1$, where $V_i(n)$ is the part of
$\binom{n}{i}$ supported on primes $\ge i$. A triple $(n,i,j)$ with
$1 \le i < j \le n/2$ and $\gcd(V_i(n), \binom{n}{j}) = 1$ is called a
**counterexample**; a prime $p \ge i$ with $p \mid \binom{n}{i}$ and
$p \nmid \binom{n}{j}$ is called **locally bad** (for the triple), and
**good** otherwise.

**Inputs taken as given (not reproved here).** Kummer's theorem
($v_p\binom{n}{k}$ = number of carries when adding $k$ and $n-k$ in
base $p$, equivalently the number of borrows when subtracting $k$
from $n$); Legendre's formula; EEES78: outside the 12 exception pairs
$(8,3),(9,4),(10,5),(12,5),(21,7),(21,8),(30,7),(33,13),(33,14),
(36,13),(36,17),(56,13)$, the part $u$ of $\binom{n}{i}$ on primes
$< i$ satisfies $u < V_i(n)$, hence $V_i(n)^2 > \binom{n}{i}$; the
Phase 0 reduction and the computational sweep to $n \le 10000$.

**Notation.** $p$ is prime, $1 \le k \le n/2$,
$t = \lfloor n/p \rfloor$, $r = n - tp$ ($0 \le r < p$), and
$k = ap + s$ with $a = \lfloor k/p \rfloor$, $s = k \bmod p$
($0 \le s < p$). For $k \in \{i, j\}$ we write $a_k, s_k$.

**Lemma numbering.** D1.1 = S4 Lemma 0; D1.2 = S4 Lemma 2 (master
criterion); D1.3 = S4 Lemma 1 (universal good range); D1.4 = S4
Corollary 1.1; D1.5 = S4 Lemma 3; D1.6 = S4 Lemma 4; D1.7 = S4
Lemma 5; D1.8 = Theorem S4-A; D1.9 = primorial bound (Chebyshev,
proved); D1.10 = Theorem S4-C (closed wedge).

**Audit findings up front.** (1) S4's Lemma 1 proof **survives**: it
is correct as stated for all $p > j$; three expository steps are
patched below (D1.3, Audit note). (2) One genuine flaw found, in
S4's Lemma 4: the displayed equivalence "bad $\iff$
$(n-i)/2 < p \le n-j$" is **false as a standalone equivalence**; only
the forward implication holds without extra hypotheses. The correct
equivalence, proved in D1.6 and verified computationally, is
"bad $\iff$ [$(n-i)/2 < p \le n-j$ **and** $i < p \le j$]". This does
not propagate: every downstream use (S4-A, the wedge) needs only the
forward direction. (3) S4 Lemma 4's first displayed line
"$i \le r < p \le j$" contradicts its own "more precisely" clause and
its own example ($(18,5,8,7)$ has $r = 4 < 5 = i$); treated as a
typographical error and resolved in favour of the precise clause.

---

## Lemma D1.1 (L0: the two-digit regime and the band bound)

If $p^2 > n$ then $n$ has at most two base-$p$ digits: $n = tp + r$
with $t < p$, $0 \le r < p$ (exactly two digits if $p \le n$; one
digit, $t = 0$, if $p > n$). Moreover, for every $k \le n/2$,
$a = \lfloor k/p \rfloor \le \lfloor t/2 \rfloor$.

*Proof.* $t < p \iff \lfloor n/p \rfloor \le p-1 \iff n \le p^2 - 1
\iff n < p^2$, so $n = tp + r$ is the base-$p$ expansion (leading
digit $t$, units digit $r$). For the band bound:
$ap \le k \le n/2 = (tp + r)/2 < p(t+1)/2$ (using $r < p$), so
$2a < t + 1$. If $t = 2m$ is even, $a < m + \tfrac12$ gives
$a \le m = \lfloor t/2 \rfloor$; if $t = 2m+1$ is odd, $a < m+1$
gives $a \le m = \lfloor t/2 \rfloor$. ∎

## Lemma D1.2 (L2: master two-digit criterion)

Assume $p^2 > n$. Then for every $k \le n/2$,
$$v_p\tbinom{n}{k} = \mathbf 1[\,s > r\,] \in \{0,1\},$$
i.e. $p \mid \binom{n}{k} \iff (k \bmod p) > (n \bmod p)$, and the
exponent is at most $1$.

*Proof (Kummer, via borrows, digit by digit).* By D1.1,
$n = (t, r)_p$ and $k = (a, s)_p$ with $a \le \lfloor t/2 \rfloor$
(write $n = (0, n)_p$ if $p > n$; the argument below covers $t = 0$
with $a = 0$). By Kummer's theorem in subtraction form,
$v_p\binom{n}{k}$ is the number of borrows when subtracting $k$
from $n$ in base $p$; there are only two digit positions.

*Units position.* A borrow out of the units position occurs iff
$s > r$; call the borrow $b \in \{0,1\}$ ($b = 1 \iff s > r$).

*Tens position.* After the possible borrow, the tens digit of the
minuend is $t - b$, and we subtract $a$. A second borrow would
occur iff $a > t - b$. This never happens: if $b = 0$ then
$a \le \lfloor t/2 \rfloor \le t$; if $b = 1$ then
$a \le \lfloor t/2 \rfloor \le t - 1$ for every $t \ge 1$
(for $t = 1$: $\lfloor t/2 \rfloor = 0 = t-1$; for $t \ge 2$:
$\lfloor t/2 \rfloor \le t/2 \le t-1$), and for $t = 0$ we have
$a = b = 0$. There are no higher positions.

Hence the total number of borrows is exactly $b$:
$v_p\binom{n}{k} = 1$ if $s > r$, and $0$ if $s \le r$. ∎

*Cross-check (Legendre).* Since $p^2 > n$, Legendre's sum for
$v_p\binom{n}{k}$ has only the term $p^1$:
$v_p = t - a - \lfloor (n-k)/p \rfloor$, and
$n - k = (t-a)p + (r-s)$ with $r - s \in [0, p)$ if $s \le r$,
$n - k = (t-a-1)p + (r-s+p)$ with $r-s+p \in (0, p)$ if $s > r$;
so $\lfloor (n-k)/p \rfloor = t - a$, resp. $t - a - 1$, giving the
same conclusion. (The case $s > r$ needs $t - a - 1 \ge 0$, which
is the tens-position check above.) ∎

## Lemma D1.3 (L1: universal good range — every $p > j$ is good)

Let $p$ be a prime with $p > j$. Then, with **no digit hypothesis**
($p$ arbitrary relative to $\sqrt n$),
$p \mid \binom{n}{i} \Rightarrow p \mid \binom{n}{j}$.

*Proof.* If $p > n$ then $v_p\binom{n}{k} = 0$ for all $k$ and the
implication is vacuous; assume $p \le n$. We use the following
characterisation. For any $k$ with $1 \le k < p$:
$$v_p\tbinom{n}{k} \ge 1 \iff (n-k,\, n] \text{ contains a multiple of } p.
\tag{$\ast$}$$
Indeed, by Legendre's formula,
$v_p\binom{n}{k} = \sum_{e \ge 1} \big(\lfloor n/p^e \rfloor -
\lfloor k/p^e \rfloor - \lfloor (n-k)/p^e \rfloor\big)$.
Each summand is $0$ or $1$: writing $n = k + (n-k)$, the summand is
$\lfloor x + y \rfloor - \lfloor x \rfloor - \lfloor y \rfloor$ for
$x = k/p^e$, $y = (n-k)/p^e$, which lies in $\{0, 1\}$. Since
$p^e \ge p > k$, $\lfloor k/p^e \rfloor = 0$, so the $e$-th summand
equals $\lfloor n/p^e \rfloor - \lfloor (n-k)/p^e \rfloor$, which is
exactly the number of multiples of $p^e$ in $(n-k, n]$; in
particular it is $\ge 0$, and it is $\le 1$ also because the
interval has length $k < p \le p^e$, so it contains at most one
multiple of $p^e$.

($\Leftarrow$ in $(\ast)$) If $(n-k, n]$ contains a multiple of
$p$, the $e = 1$ summand is $\ge 1$, hence $= 1$, so
$v_p\binom{n}{k} \ge 1$.

($\Rightarrow$ in $(\ast)$) If $v_p\binom{n}{k} \ge 1$, some summand
is $1$ (all summands are in $\{0,1\}$), say the $e$-th; then
$(n-k, n]$ contains a multiple of $p^e$, and a multiple of $p^e$ is
a multiple of $p$.

Now apply $(\ast)$ with $k = i$ and $k = j$; both satisfy $k < p$
because $i < j < p$. If $p \mid \binom{n}{i}$, then $(n-i, n]$
contains a multiple of $p$; since $i < j$,
$(n-i, n] \subseteq (n-j, n]$, so $(n-j, n]$ contains a multiple
of $p$, and $(\ast)$ gives $p \mid \binom{n}{j}$. ∎

**Audit note (does S4's proof of Lemma 1 survive?).** Yes. S4's
argument is exactly the one above. Three steps that S4 compresses
are made explicit here, and each checks out: (i) the claim "every
summand is $0$ or $1$" is the floor identity
$\lfloor x+y\rfloor - \lfloor x\rfloor - \lfloor y\rfloor
\in \{0,1\}$; (ii) the identification of the $e$-th summand with
the count of multiples of $p^e$ in $(n-k, n]$ uses
$\lfloor k/p^e \rfloor = 0$, which is exactly where the hypothesis
$k < p$ enters — the characterisation $(\ast)$ is **not** claimed
for $k \ge p$, and it would fail there; (iii) the forward direction
of $(\ast)$ uses that a multiple of $p^e$ lying in the interval is
in particular a multiple of $p$ in the interval. Note the proof
covers both regimes the brief asked about uniformly: $p > n/2$
(where $v_p\binom{n}{k} \in \{0,1\}$ and the multiple, if any, is
$n$'s top multiple) and $j < p \le n/2$ (where higher powers $p^e$
can contribute, and the argument through $(\ast)$ is essential —
a naive "the multiple of $p$ in $(n-i,n]$" phrasing without the
$p^e$ bookkeeping would have a hole; S4's version does the
bookkeeping correctly). No repair was needed, only expansion.

## Corollary D1.4 (Corollary 1.1)

In a counterexample, every prime divisor $p \ge i$ of
$\binom{n}{i}$ satisfies $i \le p \le j$. This holds for all $p$,
including $p \le \sqrt n$.

*Proof.* If $p \mid \binom{n}{i}$ and $p > j$, D1.3 gives
$p \mid \binom{n}{j}$, contradicting that $(n,i,j)$ is a
counterexample (which requires every $p \ge i$ dividing
$\binom{n}{i}$ to fail to divide $\binom{n}{j}$ — in fact it
requires $\gcd(V_i(n), \binom{n}{j}) = 1$, so *some* prime divisor
$\ge i$ of $\binom{n}{i}$ failing to divide $\binom{n}{j}$ is
already impossible for $p > j$; a fortiori every prime divisor
$p \ge i$ of $\binom{n}{i}$ in a counterexample has $p \le j$). ∎

## Lemma D1.5 (L3: $t = 1$, primes in $(n/2, n]$ are all good)

Let $p \in (n/2, n]$, so $t = 1$, $n = p + r$ with
$r = n - p < n/2 < p$. Then no prime in this range is locally bad.

*Proof.* For $k \le n/2 < p$: $a = 0$ and $s = k$. By D1.2
(applicable since $p > n/2 \ge \sqrt n$ for $n \ge 4$; for $n < 4$
there is no triple $i < j \le n/2$),
$p \mid \binom{n}{k} \iff k > r$. Hence
$p \mid \binom{n}{i} \Rightarrow i > r$, and $j > i > r$ gives
$p \mid \binom{n}{j}$. ∎

(Remark: this is subsumed by D1.3, since $p > n/2 \ge j$. The
Kummer proof is given because it is the template for $t \ge 2$.)

## Lemma D1.6 (L4: $t = 2$, primes in $(n/3, n/2]$)

Let $p \in (n/3, n/2]$ and assume $p^2 > n$ (automatic if $n > 9$,
since $p > n/3$ gives $p^2 > n^2/9 > n$; the finitely many smaller
cases lie in the swept region). So $t = 2$, $n = 2p + r$,
$0 \le r < p$, and by D1.1 every $k \le n/2$ has $a \in \{0, 1\}$.

(a) *Sub-band $k < p$* ($a = 0$): $p \mid \binom{n}{k} \iff k > r$.

(b) *Sub-band $k \ge p$* ($a = 1$): $v_p\binom{n}{k} = 0$ for every
such $k \le n/2$.

(c) *Bad configuration.* $p$ is locally bad iff
$$r < i < p \le j \qquad\text{(whence automatically }
j \le p + \lfloor r/2 \rfloor\text{)}.$$

*Proof.* (a) is D1.2 with $s = k$. For (b): write $k = p + k'$.
Since $k \le n/2 = p + r/2$, we get $k' \le r/2$ (this is the bound
in the brief; it is correct, and since $k'$ is an integer,
$k' \le \lfloor r/2 \rfloor$). Here $s = k' \le r/2 \le r$, so
D1.2 gives $v_p\binom{n}{k} = 0$. Digitwise confirmation:
$k = (1, k')_p$, $n - k = (1, r - k')_p$ (valid since
$0 \le k' \le r$), digit sums $k' + (r - k') = r < p$ and
$1 + 1 = 2 < p$: no carry.

For (c): Suppose $p$ is locally bad. Then $v_p\binom{n}{i} = 1$, so
by (b) $a_i = 0$, and by (a) $i = s_i > r$; in particular $i < p$.
Also $v_p\binom{n}{j} = 0$; if $a_j$ were $0$, then
$s_j = j > i > r$ would give $v_p\binom{n}{j} = 1$ by (a),
contradiction; hence $a_j = 1$, i.e. $p \le j$ (and $j < 2p$ since
$a_j \le 1$). Conversely, if $r < i < p \le j$: $a_i = 0$ and
$s_i = i > r$ give $v_p\binom{n}{i} = 1$ by (a); $a_j = 1$ (as
$p \le j \le n/2$ and $a_j \le 1$) gives $v_p\binom{n}{j} = 0$ by
(b). Finally, $j \le p + \lfloor r/2 \rfloor$ is the bound $k' \le
\lfloor r/2 \rfloor$ from (b) applied to $k = j$. ∎

**The linking inequalities, with a correction to S4.** From
$r < i$ and (given $a_j = 1$) $s_j = j - p \le r$:
$$r < i \iff n - 2p < i \iff \tfrac{n-i}{2} < p,
\qquad
j - p \le r \iff j - p \le n - 2p \iff p \le n - j.$$
So local badness **implies**
$\frac{n-i}{2} < p \le n - j$. However, S4's wording that the bad
configuration is "*equivalently* $\frac{n-i}{2} < p \le n-j$" is
**not correct as a standalone equivalence**:

- The inequality pair alone does not imply $i < p$: e.g.
  $(n,i,j,p) = (12,5,6,5)$ has $t = 2$, $r = 2$,
  $\frac{12-5}{2} = 3.5 < 5 \le 6 = n - j$, and $p \le j$, but
  $i = p$, $v_5\binom{12}{5} = 0$: $p$ does not even divide
  $\binom{n}{i}$.
- Nor does it imply $p \le j$: e.g. $(n,i,j,p) = (30,9,10,11)$
  has $t = 2$, $r = 8$, $\frac{30-9}{2} = 10.5 < 11 \le 20 =
  n - j$, but $p = 11 > 10 = j$ and
  $v_{11}\binom{30}{9} = v_{11}\binom{30}{10} = 1$: $p$ is good
  (consistently with D1.3).

The **correct equivalence** is:
$$p \text{ locally bad} \iff
\Big[\tfrac{n-i}{2} < p \le n - j\Big] \ \text{and}\ [\,i < p \le j\,],$$
in the $t = 2$ regime. *Proof of the corrected equivalence.* The
two bracketed conditions unpack to $r < i$, $j - p \le r$ (by the
algebra above, using $r = n - 2p$), $i < p$, and $p \le j$.
($\Rightarrow$) Local badness gives $r < i < p \le j$ by (c), and
$j - p = s_j \le r$ because $v_p\binom{n}{j} = 0$ with $a_j = 1$
means $s_j \le r$ by D1.2. ($\Leftarrow$) From $i < p$: $a_i = 0$,
$s_i = i > r$, so $v_p\binom{n}{i} = 1$. From $p \le j$ and
$a_j \le 1$: $a_j = 1$, $s_j = j - p \le r$, so
$v_p\binom{n}{j} = 0$. ∎ This corrected equivalence, and the
failure of the naive one, were verified exhaustively for all
$t = 2$ triples with $n < 200$ (1,805,080 triple/prime checks,
0 violations of the corrected form; the naive form's failure is
witnessed already at $n = 10$, $(i,j,p) = (1,2,5)$). Since all
downstream arguments use only the forward implication
(bad $\Rightarrow$ inequalities), this flaw does **not** propagate
to D1.8 or D1.10.

*Verified example.* $(n, i, j, p) = (18, 5, 8, 7)$: $t = 2$,
$r = 4$, $r < i = 5 < 7 = p \le j = 8 \le 7 + 2$; exactly,
$v_7\binom{18}{5} = 1$, $v_7\binom{18}{8} = 0$ (recomputed with
exact Legendre arithmetic in the audit, §A).

## Lemma D1.7 (L5: general $t$ in the two-digit regime)

**Regime boundary (read carefully).** This lemma, like S4's
Lemma 5, lives **entirely in the two-digit regime $p^2 > n$**,
equivalently $t = \lfloor n/p \rfloor < p$. "General $t$" means
$t \ge 1$ arbitrary subject to $t < p$ — *not* $p^2 \le n$. For
$p^2 \le n$ the conclusions are false: $n$ has $\ge 3$ base-$p$
digits, the exponent cap fails ($v_2\binom{12}{6} = 2$, since
$\binom{12}{6} = 924 = 4 \cdot 231$), and divisibility can be
witnessed at a higher digit position, unrelated to $s$ versus $r$.

Assume $p^2 > n$, $t \ge 1$ arbitrary, and write
$i = a_i p + s_i$, $j = a_j p + s_j$. Then
$$p \text{ is locally bad} \iff a_i < a_j \ \text{and}\
s_i > r \ge s_j,$$
i.e. $\lfloor i/p \rfloor < \lfloor j/p \rfloor$ and
$(i \bmod p) > r \ge (j \bmod p)$.

*Proof.* First, $a_i \le a_j$: if $a_i \ge a_j + 1$ then
$i \ge a_i p \ge (a_j + 1)p > a_j p + s_j = j$ (as $s_j < p$),
contradicting $i < j$. Also $a_i, a_j \le \lfloor t/2 \rfloor$ by
D1.1. By D1.2, $p \mid \binom{n}{i} \iff s_i > r$ and
$p \nmid \binom{n}{j} \iff s_j \le r$. If $a_i = a_j$, then
$i < j$ forces $s_i < s_j$, so $s_i > r$ implies $s_j > r$: $p$
cannot be locally bad. If $a_i < a_j$, the two D1.2 conditions
$s_i > r \ge s_j$ are exactly local badness, and they are clearly
sufficient as well as necessary. ∎

**Consequences.**

1. **$p \le j$.** $a_i < a_j$ gives $a_j \ge 1$, so $j \ge p$.
   (Weaker than D1.4, but obtained purely digitwise.)
2. **A multiple of $p$ in $(i, j]$.** $a_i < a_j$ iff the multiple
   $(a_i + 1)p$ lies in $(i, j]$.
3. **Linking inequalities.** Using $r = n - tp$ and
   $s_i = i - a_i p$: $s_i > r \iff i - a_i p > n - tp
   \iff n < i + (t - a_i)p$; similarly $s_j \le r \iff
   n \ge j + (t - a_j)p$. Since
   $a_j \le \lfloor t/2 \rfloor < t$ and $a_i \le a_j$, both
   $t - a_i, t - a_j \ge 1$, and dividing:
   $$j + (t - a_j)p \;\le\; n \;<\; i + (t - a_i)p,
   \qquad\text{i.e.}\qquad
   \frac{n - i}{\,t - a_i\,} < p \le \frac{n - j}{\,t - a_j\,}.$$
   Equivalently the residue window is
   $r \in [s_j, s_i) = [\,j - a_j p,\; i - a_i p\,)$, an interval
   of length $s_i - s_j = (a_j - a_i)p - (j - i) \in (0, p)$
   (positive since $s_i \ge r + 1 > r \ge s_j$; and $< p$ since
   $s_i, s_j \in [0, p)$).
4. **$i < p$ is forced only for $t \le 3$.** For $t \in \{2, 3\}$,
   $\lfloor t/2 \rfloor = 1$, so $(a_i, a_j) = (0,1)$ is the only
   bad band pair, giving $i < p \le j$. For $t = 3$ the shape is
   identical to D1.6: bad iff $r < i < p \le j$ with
   $j - p \le r$, equivalently (with the same caveat as D1.6: the
   band conditions $i < p \le j$ must be included)
   $\frac{n-i}{3} < p \le \frac{n-j}{2}$. Bad $t = 3$ configurations
   exist: $(n,i,j,p) = (23,5,8,7)$, $t = 3$, $r = 2$,
   $v_7\binom{23}{5} = 1$, $v_7\binom{23}{8} = 0$ (audit §A). For
   $t \ge 4$, band pairs with $a_i \ge 1$ occur, so a bad prime can
   have $i > p$: $(n,i,j,p) = (49,19,24,11)$, $t = 4$, $r = 5$,
   $s_i = 8 > 5 \ge 2 = s_j$, $v_{11}\binom{49}{19} = 1$,
   $v_{11}\binom{49}{24} = 0$ (audit §A).

## Theorem D1.8 (T-S4-A: synthesis)

For all $1 \le i < j \le n/2$ and every prime $p \ge i$: if
$p \mid \binom{n}{i}$ and $p \nmid \binom{n}{j}$, then $p \le j$;
and if moreover $p^2 > n$, then, with $t = \lfloor n/p \rfloor$,
$r = n - tp$, $a_i = \lfloor i/p \rfloor$, $a_j = \lfloor j/p
\rfloor$: $a_i < a_j$, $(i \bmod p) > r \ge (j \bmod p)$,
$v_p\binom{n}{i} = 1$, and $j + (t - a_j)p \le n < i + (t - a_i)p$.

*Proof.* The first claim is D1.3. The rest is D1.7 (classification
and Consequence 3) plus D1.2 (the exponent is exactly $1$, since
$p \mid \binom{n}{i}$ and D1.2 caps the exponent at $1$). ∎

**Corollary (necessary anatomy of a counterexample).** If
$(n, i, j)$ is a counterexample, then every prime divisor $p \ge i$
of $\binom{n}{i}$ lies in $[i, j]$ (D1.4); every such prime with
$p > \sqrt n$ has exponent exactly $1$ in $\binom{n}{i}$ and lies
in a bad configuration of D1.7 form. Writing $V_i(n) =
V^{\le} \cdot V^{>}$ for the parts on primes $\le \sqrt n$ and
$> \sqrt n$: $V^{>}$ is **squarefree**, composed only of
bad-configuration primes in $[i, j]$, and $V^{\le} = 1$ whenever
$i > \sqrt n$ (the range $[i, \sqrt n]$ is then empty). ∎

## Lemma D1.9 (primorial bound, Chebyshev)

For every real $x \ge 1$, $\prod_{p \le x} p \le 4^x$.

*Proof (Erdős's elementary induction).* It suffices to prove
$\prod_{p \le m} p \le 4^m$ for integers $m \ge 1$, by strong
induction; the real case follows since the product is constant
between integers and $4^x$ is increasing. The cases $m \le 2$ are
clear ($1$ and $2 \le 16$). Let $m \ge 3$ and assume the bound for
all smaller integers. If $m$ is even,
$\prod_{p \le m} p = \prod_{p \le m-1} p \le 4^{m-1} < 4^m$. If
$m = 2q + 1$ is odd and composite, the same reduction applies. If
$m = 2q + 1$ is prime, split the product at $q + 1$:
$\prod_{p \le q+1} p \le 4^{q+1}$ by induction, and every prime
$p$ with $q + 1 < p \le 2q + 1$ divides $\binom{2q+1}{q}$: indeed
$p$ divides $(2q+1)!$, while $p \nmid q!$ and $p \nmid (q+1)!$
(since $p > q + 1$ and the only multiple of $p$ up to $2q+1$ is
$p$ itself, as $2p > 2q + 2 > 2q + 1$), so $p \mid
\frac{(2q+1)!}{q!(q+1)!} = \binom{2q+1}{q}$. Hence
$\prod_{q+1 < p \le 2q+1} p \le \binom{2q+1}{q} \le 4^q$, the last
step because $\binom{2q+1}{q} = \binom{2q+1}{q+1}$ and their sum
is $\le \sum_k \binom{2q+1}{k} = 2^{2q+1}$, so
$2\binom{2q+1}{q} \le 2^{2q+1}$. Multiplying:
$\prod_{p \le 2q+1} p \le 4^{q+1} \cdot 4^q = 4^{2q+1}$. ∎

(We use the bound in the form $\prod_{p \le j} p \le 4^j$. The
strict form $< 4^j$ also holds but is not needed.)

## Theorem D1.10 (T-S4-C: the closed wedge)

There is no counterexample with
$$i > 256, \qquad 256\,i < n < i^2, \qquad 3i/2 < j < 2i.$$

*Proof.* Suppose $(n, i, j)$ in this region were a counterexample.

*Step 1 (exceptions excluded).* The 12 EEES78 exception pairs have
$n \le 56$, while here $n > 256i > 256 \cdot 256 = 65536$. So
EEES78 applies to $(n, i)$: $V_i(n)^2 > \binom{n}{i}$.

*Step 2 (the small-prime part is empty).* Since $n < i^2$ and
$i > 0$, $\sqrt n < i$. Every prime divisor $p \ge i$ of
$\binom{n}{i}$ therefore satisfies $p > \sqrt n$, i.e.
$p^2 > n$: the two-digit regime. (This is ingredient (b) of the
brief: the part of $V_i(n)$ on primes in $[i, \sqrt n]$ is an
empty product, equal to $1$ — there is nothing to bound.)

*Step 3 (squarefree product bound).* By the Corollary to D1.8,
$V_i(n) = V^{>}$ is a product of **distinct** primes in $[i, j]$,
each to the first power. Hence by D1.9,
$$V_i(n) \;\le\; \prod_{i \le p \le j} p \;\le\;
\prod_{p \le j} p \;\le\; 4^j, \qquad V_i(n)^2 \le 16^j.$$

*Step 4 (binomial lower bound).* $\binom{n}{i} \ge (n/i)^i$:
indeed $\binom{n}{i} = \prod_{s=0}^{i-1} \frac{n-s}{i-s}$ and each
factor satisfies $\frac{n-s}{i-s} \ge \frac{n}{i}$, because
$i(n - s) - n(i - s) = s(n - i) \ge 0$ for $0 \le s < i$ and
$n > i$.

*Step 5 (assembly).* Using $n > 256 i$ and $j < 2i$ (and that
$x \mapsto 16^x$ is increasing):
$$\binom{n}{i} \;\ge\; (n/i)^i \;>\; 256^i \;=\; 16^{2i}
\;>\; 16^j \;\ge\; V_i(n)^2 \;>\; \binom{n}{i},$$
so $\binom{n}{i} > \binom{n}{i}$, a contradiction. The strict
inequalities are: $(n/i)^i > 256^i$ from $n/i > 256$ and $i \ge 1$;
$16^{2i} > 16^j$ from $j < 2i$; $V_i(n)^2 > \binom{n}{i}$ is
EEES78 (Step 1). Hence no counterexample exists in the region.
(The hypothesis $j > 3i/2$ is not needed for the contradiction
itself; it places the wedge inside the open region $j > 3i/2$
left by the Phase 0 closure of $j \le 3i/2$.) ∎

**On the constant 256.** It is the exact threshold of this
method: the chain needs $(n/i)^i > 16^j$ uniformly for $j < 2i$,
and as $j \to 2i$ this forces $n/i \ge 16^2 = 256$ (with
$n > 256i$ strict, compensating $j < 2i$ strict). Any constant
$c < 256$ fails the method: $c^i < 256^i = 16^{2i}$ for all $i$
(audit §C). The condition $i > 256$ itself is used only through
Step 1 ($n > 65536 \gg 56$); the inequality chain would work for
any $i$ with $(n, i)$ not an EEES78 exception.

**On the Rosser–Schoenfeld remark (NOT used).** S4 remarks that
$\theta(j) < 1.1\,j$ would lower the threshold to $n > 82\,i$,
$i > 82$. The arithmetic checks out: the product bound would
become $\prod_{p \le j} p < e^{1.1 j}$, so
$V_i(n)^2 < e^{2.2 j} < e^{4.4 i}$, and $e^{4.4} = 81.4508\ldots
< 82$ (verified to 50-digit precision in audit §C), so
$n > 82\,i$ gives $(n/i)^i > 82^i > e^{4.4 i} > V_i(n)^2 >
\binom{n}{i}$. But this improvement is **marked as not used**:
the bound $\theta(x) < 1.1x$ is an external explicit-estimate
input whose valid range and exact constant would need
referee-checking against Rosser–Schoenfeld (1975) before use,
and D1.10 as proved rests only on the elementary D1.9.

## Appendix: numeric audit (Python stdlib, exact integer arithmetic)

All checks were run on this VM with Python's standard library
only (Legendre valuations; `math.comb`; big-integer `pow`
comparisons — no floating point in any inequality that the proof
depends on). Total wall time $\approx 18$ s over three scripts.

**§A. Worked examples (exact Legendre $v_p$).**
$(18,5,8,7)$: $v_7\binom{18}{5} = 1$, $v_7\binom{18}{8} = 0$,
$t = 2$, $r = 4$. $(23,5,8,7)$: $1, 0$; $t = 3$, $r = 2$.
$(49,19,24,11)$: $1, 0$; $t = 4$, $r = 5$.
$(15,1,5,5)$: $1, 0$; $t = 3$, $r = 0$. All as claimed.

**§B. Lemma D1.6 equivalence.** Exhaustive over all $t = 2$
prime/triple combinations with $n < 200$ (1,805,080 checks of
triples $(i, j)$ per prime): bad $\Rightarrow$
($(n-i)/2 < p \le n-j$) with **0 violations**; the corrected
equivalence (inequalities **and** $i < p \le j$) with
**0 violations**; the naive equivalence fails, first at
$(n,i,j,p) = (10,1,2,5)$, and concretely at $(12,5,6,5)$
(inequalities hold, $p \le j$, but $i = p$ and
$v_5\binom{12}{5} = 0$) and $(30,9,10,11)$ (inequalities hold,
$p > j$, $v_{11}\binom{30}{9} = v_{11}\binom{30}{10} = 1$).

**§C. Wedge corners, exactly.** The chain of Step 5 is tightest
at the corner $n = 256i + 1$ (smallest admissible), $j = 2i - 1$
(largest admissible integer). The key inequality
$(n/i)^i > 16^j$ was tested in the exact integer form
$n^i > 16^j \cdot i^i$:

| $i$ | $n_{\min}$ | $j_{\max}$ | $n^i > 16^{j} i^i$ | $\binom{n}{i} > 16^j$ | $\binom{n}{i} i^i \ge n^i$ |
|---|---|---|---|---|---|
| 257 | 65793 | 513 | ✓ | ✓ (exact `math.comb`) | ✓ |
| 258 | 66049 | 515 | ✓ | ✓ | ✓ |
| 300 | 76801 | 599 | ✓ | ✓ | ✓ |
| 512 | 131073 | 1023 | ✓ | ✓ | ✓ |
| 1000 | 256001 | 1999 | ✓ | ✓ | ✓ |

Additionally the tight-corner inequality was checked for
**every** $i$ with $257 \le i < 2000$: no failures. (The
$\log_{10}$ margin is $\approx 1.206$ throughout, i.e.
$\log_{10} 16$: it comes from the integrality $j \le 2i - 1$;
the proof itself needs only the strict real inequalities
$j < 2i$ and $n > 256i$, as written.) Sharpness of the method:
$255^{257} < 16^{514} = 256^{257}$, exactly. Rosser–Schoenfeld
arithmetic: $e^{4.4} = 81.4508686649\ldots < 82$ (50-digit
`Decimal` evaluation; used only in the remark, not the proof).

## Status summary (D1)

- **Proved:** D1.1 (L0), D1.2 (L2, master criterion, via borrows
  with the tens-digit borrow exclusion $\lfloor t/2 \rfloor \le
  t - 1$ made explicit), D1.3 (L1), D1.4 (Cor. 1.1), D1.5 (L3),
  D1.6 (L4, including the bound $k' \le r/2$), D1.7 (L5, in the
  two-digit regime only — the regime boundary $t < p \iff
  p^2 > n$ is stated explicitly, with $v_2\binom{12}{6} = 2$ as
  the standing counterexample outside it), D1.8 (T-S4-A and the
  counterexample-anatomy corollary), D1.9 (primorial bound,
  proved elementarily), D1.10 (T-S4-C, the closed wedge).
- **L1 verdict:** S4's proof **survived** scrutiny; it is correct
  for all $p > j$ with no digit hypothesis. Only expository
  expansion was needed (floor-summand $\in \{0,1\}$; the role of
  $k < p$ in killing $\lfloor k/p^e \rfloor$; the $p > n$ vacuous
  case).
- **Wedge verdict:** T-S4-C **proved** with constant $256$,
  which is the exact threshold of the method; all inequalities
  audited with exact integer arithmetic at the corners and for
  all $257 \le i < 2000$ (§C). The Rosser–Schoenfeld improvement
  to $82$ is arithmetically correct ($e^{4.4} < 82$) but
  **marked not used** (external input, unrefereed here).
- **Gaps found in S4:** (1) Lemma 4's "equivalently
  $(n-i)/2 < p \le n-j$" is false as a standalone equivalence —
  counterexamples $(12,5,6,5)$ and $(30,9,10,11)$; the corrected
  equivalence adds $i < p \le j$ and is proved in D1.6 and
  verified exhaustively for $n < 200$. Impact: none on S4-A or
  the wedge, which use only the forward implication. (2) Lemma
  4's first displayed line "$i \le r < p \le j$" contradicts its
  own precise clause and example; treated as a typo. (3) Minor:
  S4 Lemma 2's cross-check and Lemma 5's "$a_i \le a_j$" are
  asserted without the one-line justifications supplied here
  (D1.2 cross-check, D1.7).
- **Not proved (by design, matching S4 §4):** Theorem S4-B in
  general. The open flank is $V^{\le}$ ($p \le \sqrt n$,
  multi-digit, exponents $> 1$), and the product bound $4^j$ is
  too weak when $n = O(j)$ or $j \ge 2i$. Bad configurations
  exist at every $t \ge 2$; the classification is a rigidity
  statement, not a local exclusion.
