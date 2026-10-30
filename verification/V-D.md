# Verifier D (independent) — Strategy S4, proofs P-D1 and P-D2

I did not write either proof. I re-derived the master criterion myself,
audited every numbered step in both documents against the actual text,
and ran fresh computations (Python stdlib only, exact integer
arithmetic; total wall time of the main script 93.7 s, of which the
master-criterion sweep took 66.1 s). All verdicts are relative to the
background inputs both provers explicitly take as given (Kummer,
Legendre, EEES78 with its 12 exception pairs), which I did not reprove.

**Headline: no FALSE and no GAP in either document. All 10 numbered
items of P-D1 and all 11 numbered items of P-D2 are PROVED. The one
false statement in play is S4's original bare t=2 equivalence, which
both provers correctly identify as false and repair; it does not
propagate. The Rosser–Schoenfeld improvement to 82 is, in both
documents, correctly marked unproved and unused (status: OPEN, by
design, and not load-bearing).**

---

## 1. Classification tables

### P-D1

| Item | Claim | Verdict |
|---|---|---|
| D1.1 | L0: two-digit regime, $a \le \lfloor t/2\rfloor$ | PROVED |
| D1.2 | L2: master criterion $v_p\binom nk = \mathbf 1[s>r]$ | PROVED |
| D1.3 | L1: every prime $p>j$ is good, no digit hypothesis | PROVED |
| D1.4 | Cor 1.1: counterexample primes $\ge i$ lie in $[i,j]$ | PROVED |
| D1.5 | L3: $t=1$ all good | PROVED |
| D1.6 | L4: $t=2$ classification, incl. corrected equivalence | PROVED (corrected form); bare S4 form FALSE, see §3 |
| D1.7 | L5: general-$t$ bad iff $a_i<a_j$ and $s_i>r\ge s_j$ | PROVED |
| D1.8 | T-S4-A: counterexample anatomy | PROVED |
| D1.9 | Primorial $\prod_{p\le x}p \le 4^x$, elementary | PROVED |
| D1.10 | T-S4-C: wedge, no counterexample for $i>256$, $256i<n<i^2$, $3i/2<j<2i$ | PROVED |

Counts: 10 PROVED, 0 GAP, 0 FALSE, 0 OPEN (within the document's own claims).

### P-D2

| Item | Claim | Verdict |
|---|---|---|
| D2.1 | L0: two-digit regime, $a \le \lfloor t/2\rfloor < p$ | PROVED |
| D2.2 | L2: master criterion, exponent cap 1 | PROVED |
| D2.3 | L1: every prime $p>j$ is good, no digit hypothesis | PROVED |
| D2.4 | Cor: counterexample primes $\ge i$ lie in $[i,j]$ | PROVED |
| D2.5 | L3: $t=1$ all good | PROVED |
| D2.6 | L4: $t=2$ classification, incl. corrected equivalence (Remark D2.6.1) | PROVED (corrected form); bare S4 form FALSE, see §3 |
| D2.7 | L5: general-$t$ bad iff $a_i<a_j$ and $s_i>r\ge s_j$ | PROVED |
| D2.8 | T-S4-A: counterexample anatomy | PROVED |
| D2.9 | Primorial $\prod_{p\le x}p \le 4^x$ (integers), elementary | PROVED |
| D2.10 | Binomial lower bound $\binom ni \ge (n/i)^i$ | PROVED |
| D2.11 | T-S4-C: wedge with constant 256 | PROVED |

Counts: 11 PROVED, 0 GAP, 0 FALSE, 0 OPEN (within the document's own claims).

---

## 2. Mandatory check 1: master criterion and L1

### My own re-derivation of the master criterion

Let $p^2>n$, $n=tp+r$, $k=ap+s$, $k\le n/2$. Then $t<p$, and
$ap\le n/2 < p(t+1)/2$ gives $a\le\lfloor t/2\rfloor$ (splitting
$t=2m$, $t=2m+1$). Kummer in borrow form: the units borrow occurs iff
$s>r$; call it $b$. A tens borrow would need $a>t-b$. If $b=0$,
$a\le\lfloor t/2\rfloor\le t$. If $b=1$: for $t=1$, $a=0=t-1$; for
$t\ge2$, $a\le t/2\le t-1$; for $t=0$, necessarily $a=b=0$ (indeed
$s=k\le n/2<n=r$, so $s>r$ is vacuous). No tens borrow ever occurs,
there are no higher digits, so $v_p\binom nk = b = \mathbf 1[s>r]$.
This matches D1.2 (borrow form) and D2.2 (carry form via the explicit
expansion of $n-k$; the $t=0$ and $t=1$ edges are handled in both:
D1.2 explicitly, D2.2 by forcing $t\ge1$ in the case $s>r$ and by
$t-a-1=0$ at $t=1$). The Legendre cross-checks in both are also
correct: for $p^2>n$ only the $e=1$ Legendre term survives, and
$\lfloor (n-k)/p\rfloor$ is $t-a$ or $t-a-1$ according as $s\le r$
or $s>r$.

### Fresh computation (not the provers' ranges/scripts)

```
MASTER n<=1000, all primes p with p^2>n, all k<=n/2:
  checks=39,951,373  violations=0     (v_p by Legendre)
L1 random: 300 random triples, n<=2000, seed 69904:
  prime-divisor checks (p>j, p | C(n,i)) = 13,577  violations=0
Sharpness at p=j, (n,i,j,p)=(15,1,5,5):
  v_5 C(15,1) = 1,  v_5 C(15,5) = 0,  C(15,5) = 3003
```

So L1 is confirmed computationally, and its hypothesis $p>j$ is
sharp at $p=j$, exactly as D2.3's stress test claims (D1.3's proof
also checks out line by line: every Legendre summand is in $\{0,1\}$
by the floor identity, $\lfloor k/p^e\rfloor=0$ is exactly where
$k<p$ enters, and a multiple of $p^e$ in $(n-k,n]$ is a multiple of
$p$ there; the $p>n$ case is vacuous in both documents).

Spot checks of both documents' worked examples, recomputed exactly:
$(18,5,8,7)$: $v_7=1,0$; $(23,5,8,7)$ ($t=3$): $1,0$;
$(49,19,24,11)$ ($t=4$, a bad prime with $i>p$): $1,0$;
$(18,5,8,17)$: $1,1$ (good); outside the two-digit regime
$v_2\binom{12}{6}=2$, confirming D1.7's stated regime boundary.

---

## 3. Mandatory check 2: the t=2 bare-equivalence flaw

Direct computation:

```
(12,5,6,5):  t=2, r=2,  (n-i)/2 < p <= n-j  is  3.5 < 5 <= 6  TRUE,
             but v_5 C(12,5) = 0  (indeed v_5 C(12,6) = 0):
             p does not even divide C(n,i). Bare equivalence FALSE
             in the sufficiency direction (here i = p fails).
(30,9,10,11): t=2, r=8, inequalities 10.5 < 11 <= 20 TRUE,
             but p=11 > j=10 and v_11 C(30,9) = v_11 C(30,10) = 1:
             p is good (as L1 forces). Bare equivalence FALSE in
             this direction too (here p <= j fails).
(10,1,2,5) (D2's second witness): inequalities TRUE, v_5 = 1,1, good.
```

Corrected equivalence, exhaustive fresh check:

```
t=2, p^2>n, all n<=300, all i<j<=n/2:
  checks=8,608,152
  bad  <=>  [ (n-i)/2 < p <= n-j  AND  i < p <= j ] : violations=0
  bad  <=>  bare inequalities alone: mismatches=2,984,660
```

**Adjudication: S4's Lemma 4 bare equivalence is FALSE (both provers
are right); the corrected equivalence (inequalities AND $i<p\le j$)
is PROVED in D1.6 and in D2.6/D2.6.1 and is computationally exact.**

Propagation audit (reading the actual citing steps, not the summaries):

- D1: D1.8's proof cites only D1.3 (for $p\le j$) and D1.7 plus D1.2.
  D1.10 cites the Corollary to D1.8 and D1.9. The $t=2$ result D1.6
  is not used downstream at all except as classification; nothing
  uses sufficiency of the bare pair.
- D2: D2.8's proof cites D2.4 (contrapositive of D2.3) and D2.7;
  D2.11 cites D2.8. D2.7's linking inequalities are stated as exact
  rewrites with the band condition $a_i<a_j$ retained. Nothing uses
  sufficiency of $(\dagger)$.

**The flaw does not propagate to S4-A or to the wedge in either
document. Confirmed.**

---

## 4. Mandatory check 3: the wedge (T-S4-C)

### (a) Audit of the chain and of the $[i,\sqrt n]$ step

The chain is
$\binom ni \ge (n/i)^i > 256^i = 16^{2i} > 16^j \ge V_i(n)^2 >
\binom ni$.
Links: $(n/i)^i>256^i$ from $n>256i$; $256^i=16^{2i}$;
$16^{2i}>16^j$ from $j<2i$; $V_i(n)^2>\binom ni$ is EEES78, applicable
because all 12 exception pairs have $n\le56$ while the wedge has
$n>256\cdot257>65536$ (both documents state this; D1 Step 1,
D2.11 preamble). $\binom ni\ge (n/i)^i$ is proved in D1.10 Step 4 and
in D2.10 (the factor inequality $i(n-s)\ge n(i-s)$ is $s(n-i)\ge0$).

The load-bearing step is $V_i(n)\le 4^j$. It is valid **only under
the counterexample hypothesis**: by the Corollary (D1.4/D2.4) every
prime factor $\ge i$ of $\binom ni$ is $\le j$, and for $p>\sqrt n$
the master criterion caps the exponent at 1. Primes $p\in[i,j]$ with
$p\le\sqrt n$ would break squarefreeness, and both documents dispose
of them explicitly and correctly: in the wedge $n<i^2$, hence
$\sqrt n<i$, so the interval $[i,\sqrt n]$ is empty and the
$\le\sqrt n$ part of $V_i(n)$ is 1. D1 says this in Step 2 and in the
Corollary to D1.8 ($V^{>} $ is all of $V_i(n)$); D2.11 says it in
"Since $n<i^2$, $\sqrt n<i$, so every prime divisor $p\ge i$ ...
satisfies $p>\sqrt n$. By Theorem D2.8, $V_i(n)=V_i^{>}$...".
Then $V_i(n)\le\prod_{i\le p\le j}p\le\prod_{p\le j}p\le 4^j$ by the
primorial bound, and $V_i(n)^2\le 16^j$ (indeed $4^j$ squared is
$16^j$). **Step explicit and correct in both documents.**

### (b) Numerical verification on actual wedge triples

One clarification the task's phrasing requires: on an arbitrary
(non-counterexample) wedge triple the *full* $V_i(n)$ is **not**
$\le 4^j$, and it should not be: $V_i(n)$ also contains good primes
$p>j$ (which divide $\binom nj$ as well), and EEES78 forces
$V_i(n)^2>\binom ni > 16^j$ there. The wedge bound applies to $V_i$
under the counterexample hypothesis, where every prime factor of
$V_i$ is bad. I therefore verified, by direct Legendre computation
of all valuations, on six sample triples with
$i\in\{257,300,500\}$, $256i<n<i^2$, $3i/2<j<2i$:

```
(i,n,j)          full V_i <= 4^j?   V_i^2 > C(n,i)?   bad-only part <= 4^j?
(257,65793,400)  False (677 digits  True              True; 18 bad primes,
                 vs 241 for 4^j)                       all in [i,j], all exp 1
(257,66000,500)  False              True              True; 15 bad primes, ditto
(300,80000,500)  False              True              True; 16 bad primes, ditto
(300,88000,550)  False              True              True; 14 bad primes, ditto
(500,140000,800) False              True              True; 22 bad primes, ditto
(500,240000,900) False              True              True; 28 bad primes, ditto
```

In every sample: every locally bad prime $\ge i$ lies in $[i,j]$
with exponent exactly 1 (as S4-A predicts), the bad-only part (which
is what $V_i(n)$ would be for a counterexample) is $\le 4^j$, and
every arithmetic link of the chain ($n^i > 256^i i^i$ exactly,
$256^i=16^{2i}$, $16^{2i}>16^j$, $\binom ni\cdot i^i \ge n^i$)
holds. This is consistent with, and confirms the mechanism of, the
wedge; the "False" column is the expected behaviour off the
counterexample hypothesis, not a defect in either proof.

Exact corner checks (tightest corner $n=256i+1$, $j=2i-1$):
$n^i > 16^j i^i$ and $\binom ni > 16^j$ hold exactly for
$i\in\{257,258,300,512,1000\}$.

### (c) The constant 256 and the RS-82 status

$256 = 16^2$ is exactly the method's threshold: with $j$ allowed up
to $2i$, the chain needs $(n/i)^i \ge 16^{2i}$, i.e. $n/i \ge 256$,
with strictness on both sides compensating. 255 fails:
$255 < 16^2 = 256$ and $255^{257} < 16^{514} = 256^{257}$ (exact).
Both documents state this correctly (D1 "On the constant 256";
D2.11 boundary verification).

Rosser–Schoenfeld: both documents mark the improvement **UNPROVED
and UNUSED** (D1: "marked as not used... external explicit-estimate
input"; D2: "NOT proved here... NOT used anywhere above... gap,
explicitly marked, unused"). The conditional arithmetic is right:
$e^{4.4} = 81.4508686649\ldots < 82$ (I recomputed to 50-digit
Decimal precision: $81.45086866496811744\ldots$), so *if*
$\theta(j)<1.1j$ held, $V_i^2 < e^{2.2j} < e^{4.4i} < 82^i$ and
$n>82i$ would close the chain. **Status of RS-82: OPEN/unproved,
correctly labelled, load-bearing nowhere. Confirmed in both.**

---

## 5. Mandatory check 4: the primorial bound proof

The standard pitfall is the induction step through
$\binom{2m+1}{m}$: one must show every prime in $(m+1,2m+1]$ actually
divides that binomial, and must split the product at $m+1$ (not at
$m$) so the induction hypothesis applies to a strictly smaller index.

- D1.9: splits at $q+1$ for $m=2q+1$. Primes $p\in(q+1,2q+1]$ divide
  $\binom{2q+1}{q}$ because $p\mid(2q+1)!$ while $p\nmid q!(q+1)!$
  (the only multiple of $p$ up to $2q+1$ is $p$ itself, since
  $2p>2q+2>2q+1$). The bound $\binom{2q+1}{q}\le 4^q$ via
  $2\binom{2q+1}{q} = \binom{2q+1}{q}+\binom{2q+1}{q+1} \le 2^{2q+1}$
  is correct. The even case and the odd-composite case both reduce
  to $m-1$ legitimately (a composite or even $m$ contributes no new
  prime). The extension to real $x$ is valid. **No pitfall.**
- D2.9: same structure; it states $v_p\binom{2m+1}{m}=1$ via
  $p\le 2m+1 < 2p$, i.e. $p$ occurs exactly once in $(2m+1)!$ and
  not in $m!(m+1)!$, so the product of the distinct new primes
  divides the binomial. Same (correct) bound $\binom{2m+1}{m}\le4^m$.
  **No pitfall.** (D2.9 is stated for integers, which is all the
  wedge uses, $4^j$.)

Independent check: $\prod_{p\le x}p \le 4^x$ holds exactly for all
$x\le 2000$ (fresh computation).

Minor notes (no impact): D1.4's parenthetical "some prime divisor...
is already impossible" is loosely worded, but the stated corollary
(every prime divisor $\ge i$ lies in $[i,j]$) is what is proved and
used, and it is correct. D1.6's first-displayed-line typo from S4
("$i\le r<p\le j$") is correctly identified by D1 itself as a typo
against its own example $(18,5,8,7)$ with $r=4<i=5$ (recomputed:
$t=2$, $r=4$, $v_7=1,0$).

---

## 6. Final verdicts per claim at stake

| Claim | Verdict |
|---|---|
| L0/L2 two-digit master criterion $v_p\binom nk=\mathbf1[s>r]$, $p^2>n$ | PROVED (both), computationally exact on 39,951,373 fresh checks |
| L1 every prime $p>j$ good, no digit hypothesis | PROVED (both), 0 violations on 13,577 fresh random divisor checks; sharp at $p=j$ via $(15,1,5,5)$ |
| Cor: counterexample $\Rightarrow$ prime factors $\ge i$ of $\binom ni$ all in $[i,j]$ | PROVED (both) |
| L3 $t=1$ all good | PROVED (both) |
| L4 $t=2$ classification | PROVED (both) in the form bad $\iff r<i<p\le j$ |
| S4's bare L4 equivalence "bad $\iff (n-i)/2<p\le n-j$" | **FALSE** (counterexamples $(12,5,6,5)$ and $(30,9,10,11)$, both verified by direct computation); both provers correctly flag and repair it |
| L4 corrected equivalence (inequalities AND $i<p\le j$) | PROVED (both), 0 violations on 8,608,152 fresh checks, $n\le300$ |
| L5 general-$t$ bad-configuration classification | PROVED (both), in the two-digit regime $p^2>n$ only, as both state |
| T-S4-A counterexample anatomy | PROVED (both); uses only L1 / the forward direction, no propagation of the bare-L4 flaw |
| T-S4-C wedge ($i>256$, $256i<n<i^2$, $3i/2<j<2i$) | PROVED (both), conditional on EEES78 as a stated input; the $[i,\sqrt n]$ emptiness step is explicit and correct in both; constant 256 is the exact threshold of the method (255 fails, exact) |
| Primorial bound $\prod_{p\le x}p\le 4^x$, elementary | PROVED (both); central-binomial induction step audited, no pitfall |
| Rosser–Schoenfeld improvement to 82 | OPEN / unproved, correctly marked **unproved and unused** by both provers; conditional arithmetic $e^{4.4}\approx81.4509<82$ verified |

**Totals: P-D1: 10/10 PROVED. P-D2: 11/11 PROVED. FALSE: 1, and it
belongs to S4's original bare Lemma 4 phrasing, not to either proof
document. GAP: 0. OPEN: only the explicitly disclaimed RS-82
improvement, which neither proof uses.**
