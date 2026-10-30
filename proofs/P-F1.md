# Prover F1 (independent): the case $i=3$ in Cycle 2

Prover: F1, working independently in Cycle 2. Sources read: `strategies/S8.md`
§3 and §3.5, `proofs/P-A1.md` (the (LD3) system, Proposition A1.16, Statement
H3), `EXTERNAL_CLAIMS_2026-10-29.md` (the Del Pin entry and the Van
Doorn–Rocca $i=3$ diagnosis), `REFEREE.md` (for the description of Price
Proposition 4.1), and Price's manuscript
`~/workspace/user/files/Liam_699_partial.pdf` itself (extracted with
`pdftotext`). `proofs/P-F2.md` was **not** read. Every computation below is
in `proofs/P-F1_checks.py` (Python standard library only, exact integer
arithmetic, no randomness; total runtime 53 seconds on this machine), and
the headline computations were each run through two independent code paths
(§7). Every numbered claim is labelled PROVED, GAP, FALSE, or OPEN.

**Headline.** $i=3$ is **not** closed in general, and (H3) is **not** proved.
What is new in this file: (a) there is **no counterexample with $n$ odd**
(Claim F1.5, via Price Proposition 4.1 applied to the pinned SPLIT-odd case);
(b) four even $(Q,R)$ subfamilies are closed (Claim F1.10); (c) the pairs
$(3,j)$ are closed **for all $n$ for every $5 \le j \le 2000$**, by the pure
(LD3) method inside the finite reduction (Claim F1.16); (d) (LD3) has **no
solution at all with $n \le 10^6$** (Claim F1.17), extending the Cycle 1
bound of $5000$ by a factor of $200$.

## 0. Standing inputs and notation

$C(n,k)=\binom nk$; $V_3(n)$ is the part of $C(n,3)$ on primes $\ge 3$, i.e.
the odd part of $C(n,3)$; a **counterexample** is a triple $(n,3,j)$,
$3<j\le n/2$, with $\gcd(V_3(n),C(n,j))=1$. Used as established ground truth
(per the assignment and Cycle 1): EEES78 and the key lemma
($d\mid C(n,i)$, $\gcd(d,C(n,j))=1 \Rightarrow d\mid C(j,i)$); the finite
reduction $n\le N(i,j)$, where
$N(i,j)=\max\{n : C(n,i)<C(2j,\,2(j-i))\}$; the closures $j\le 3i/2$ (Price)
and $n=2j$ (Price); $i\in\{1,2\}$ closed; $(3,5)$ and $(3,6)$ closed; the
system (LD3), conditions (N1), (N2), and the SPLIT-odd / SPLIT-even
reductions of S8 §3.5 and Proposition A1.16(iv); and the sweep statement
"no counterexample with $n\le 20{,}000$". For $m\in\{n,n-1,n-2\}$,
$R(m)$ is the product of the **relevant** prime powers $q=p^a\Vert m$
($p\ge5$, any $a\ge1$; or $p=3$, $a\ge2$), and $U_r$ is the part of $n-r$ on
primes $\ge5$, so that (S8 §3.3, (N2))
$$V_3(n)=U_0U_1U_2\cdot 3^{\,v_3(n(n-1)(n-2))-1}.$$

## 1. Task 1: Price Proposition 4.1, extracted exactly

**Claim F1.1 (PROVED, as an extraction).** Proposition 4.1 of Price's
manuscript (Section 4, "A Euclidean-division bound", page 5) states:

> **Proposition 4.1.** Suppose $1\le i<j\le n/2$ and no prime $q\ge i$
> divides both $\binom ni$ and $\binom nj$. Write $n=Qj+R$, where
> $Q=\lfloor n/j\rfloor\ge2$ and $0\le R<j$, and put
> $$T=R+(Q-1)(i-1),\qquad
> h=\max\Bigl(0,\ \Bigl\lceil\frac{i-R}{Q}\Bigr\rceil\Bigr).$$
> Then $V_i(n)\mid\Lambda_i(T)\binom{j}{h}$, and consequently
> $$\binom ni\;<\;\Bigl(\Lambda_i(T)\binom{j}{h}\Bigr)^{2},$$
> where, for $T\ge1$,
> $\Lambda_i(T)=\prod_{q\ge i,\ q\text{ prime}}q^{\lfloor\log_q T\rfloor}$
> and $\Lambda_i(0)=1$; the manuscript notes $\Lambda_i(T)$ is "the part of
> $\mathrm{lcm}(1,\dots,T)$ supported on primes at least $i$".

Its proof (also extracted, and used in §2 below) puts $c=n-j=(Q-1)j+R$ and
applies the manuscript's Lemma 2.1 to each full $q$-part $q^a$ of $V_i(n)$,
giving $r,s\ge0$ with $r+s<i$, $q^a\mid j-r$ and $q^a\mid c-s$; hence
$q^a\mid E:=R+(Q-1)r-s$. If $E\ne0$ then
$|E|\le\max\{R+(Q-1)(i-1),\,i-1-R\}\le T$, so $q^a\mid\Lambda_i(T)$. If
$E=0$ then $s=R+(Q-1)r$ and $R+Qr<i$, whence $0\le r<h$ and $q^a\mid j-r$;
the product of all such $q^a$ divides $j(j-1)\cdots(j-h+1)$, and since every
prime involved exceeds $h$ it divides $\binom{j}{h}$. The displayed
inequality then follows from Theorem 1.2 of the manuscript (EEES78):
a counterexample has $(n,i)\notin E$ by its Lemma 1.3, so
$\binom ni<V_i(n)^2$.

*Extraction fidelity, stated exactly.* The proposition's text, hypotheses,
the definitions of $T$, $h$ and $\Lambda_i$, and the whole proof were
legible in plain `pdftotext -layout` output. The **only** garbling was
typographic: binomial coefficients print as stacked glyphs (the plain text
shows "`hj`" for $\binom{j}{h}$), and in the consequence the exponent $2$
initially looked as if it attached only to $\binom{j}{h}$. Coordinate
extraction (`pdftotext -bbox`) resolves this unambiguously: in the first
assertion the glyphs are $j$ above $h$ inside one pair of parentheses, and
in the consequence the superscript $2$ (x $\approx 344$) sits after a
closing parenthesis (x $\approx 328$) that encloses **both**
$\Lambda_i(T)$ and $\binom{j}{h}$, i.e. the right side is
$\bigl(\Lambda_i(T)\binom{j}{h}\bigr)^2$. Nothing in the proposition could
not be read. Note for later use: **the divisibility assertion does not use
EEES78**; only the squared inequality does. $\square$

**Claim F1.2 (PROVED, specialisation to $i=3$).** Let $(n,3,j)$ be a
counterexample, $n=Qj+R$ as above. Then, with
$T=R+2(Q-1)$ and $h=\max(0,\lceil(3-R)/Q\rceil)$,
$$V_3(n)\ \Big|\ \Lambda_3(T)\binom{j}{h},
\qquad\text{and}\qquad
C(n,3)<\Bigl(\Lambda_3(T)\binom{j}{h}\Bigr)^2\ \text{(EEES form)},$$
where the case table is:

| case | $T$ | $h$ | $\Lambda_3(T)\binom{j}{h}$ |
|---|---|---|---|
| $R=0$, $Q=2$ | $2$ | $2$ | $1\cdot\binom{j}{2}$ (and $n=2j$ is closed separately) |
| $R=0$, $Q\ge3$ | $2Q-2$ | $1$ | $\Lambda_3(2Q-2)\cdot j$ |
| $R=1$ | $2Q-1$ | $1$ | $\Lambda_3(2Q-1)\cdot j$ |
| $R=2$ | $2Q$ | $1$ | $\Lambda_3(2Q)\cdot j$ |
| $R\ge3$ | $R+2Q-2$ | $0$ | $\Lambda_3(R+2Q-2)$ |

with $\Lambda_3(3)=3$, $\Lambda_3(4)=3$, $\Lambda_3(6)=15$,
$\Lambda_3(7)=\Lambda_3(8)=105$ (script §A). In particular the three
parameter values that drive §§2–3 are: $(Q,R)=(3,0)$ gives
$V_3(n)\mid 3j$; $(Q,R)=(2,2)$ gives $V_3(n)\mid 3j$; $(Q,R)=(3,2)$ and
$(4,0)$ give $V_3(n)\mid 15j$.

*Proof.* Substitute $i=3$ in Claim F1.1: $T=R+(Q-1)\cdot2$;
$h=\lceil(3-R)/Q\rceil$ for $R\le2$ (equal to $2$ only for $(Q,R)=(2,0)$,
else $1$ since $Q\ge2$), and $h=0$ for $R\ge3$. $\Lambda_3$ values are
direct products over primes $3\le q\le T$ of the largest power of $q$ not
exceeding $T$ (e.g. $\Lambda_3(6)=3\cdot5=15$). $\square$

*Answer to "does it cut into the SPLIT configurations?"* Yes. For
SPLIT-odd it is decisive (Claim F1.4: $(Q,R)=(3,0)$ is forced there). For
SPLIT-even it closes four $(Q,R)$ subfamilies and gives a label-retaining
bound on all the others (Claims F1.9, F1.10, F1.11). It is exactly the kind
of input the Van Doorn–Rocca diagnosis calls for: the parameters $Q,R$
record *where $j$ sits inside $n$*, and the proof of Proposition 4.1
records, for each prime power, whether it is charged to $\Lambda_3(T)$ or
to a specific factor $j-r$.

## 2. Task 2: the SPLIT-odd attack — closed

**Claim F1.3 (PROVED, the full remaining condition set in the pinned
case).** Let $(n,3,j)$ be a counterexample with $n$ odd. By Proposition
A1.16(iv) (Cycle 1, reproved in S8 §3.5), $v_3(n)=1$ and $j=n/3$ exactly;
hence $j$ is odd, $3\nmid j$, $n=3j$, and the full condition set is:

* ($r=0$) automatic: $R(n)=n/3=j\mid j$.
* ($r=1$) for each relevant $q\Vert(n-1)$: $j\bmod q\le1$, i.e.
  $R(n-1)=X_0X_1$ with $X_0\mid j$, $X_1\mid j-1$.
* ($r=2$) for each relevant $q\Vert(n-2)$: $j\bmod q\le2$, i.e.
  $R(n-2)=Y_0Y_1Y_2$ with $Y_s\mid j-s$.
* (N1), specialised: $\gcd(C(n,2),C(n,j))=2^a3^b$; since for $p\ge5$,
  $p\mid C(n,2)\iff p\mid j$ or $p\mid n-1$ (as $C(n,2)=3j(3j-1)/2$), this
  says no prime $\ge5$ dividing $j$ or $n-1$ divides $C(3j,j)$.
* (N2), specialised: exactly one of $n,n-1,n-2$ is divisible by $3$
  (namely $n$, to the first power), so the $3$-factor in $V_3(n)$ is
  $3^{1-1}=1$ and, with $U_0=n/3=j$,
  $$V_3(n)=j\,U_1U_2,\qquad\text{hence}\qquad
  U_1U_2\ \Big|\ \frac{(j-1)(j-2)}{6}$$
  (the right side is an integer: one of $j-1,j-2$ is divisible by $3$
  since $3\nmid j$, and $j-1,j-2$ are consecutive, one even; the
  divisibility is $V_3(n)\mid C(j,3)$ with the factor $j$ cancelled).

*Proof.* The pinning is A1.16(iv); the rest is substitution of $n=3j$ into
(LD3), (N1), (N2) as displayed. $\square$

**Claim F1.4 (PROVED — SPLIT-odd counterexamples do not exist).** There
is no counterexample $(n,3,j)$ with $n=3j$ (in particular none in the
pinned shape of Claim F1.3, for any $j$).

*Proof.* Suppose $(n,3,j)$ is a counterexample with $n=3j$. Then
$Q=\lfloor n/j\rfloor=3$ and $R=0$, so by Claim F1.2
$V_3(n)\mid\Lambda_3(4)\binom{j}{1}=3j$.
By Claim F1.3, $V_3(n)=j\,U_1U_2$ with $U_1U_2$ coprime to $3$ (its prime
factors are $\ge5$). Hence $j\mid V_3(n)\mid 3j$, so $U_1U_2\mid3$, and
coprimality to $3$ forces $U_1U_2=1$, i.e. $U_1=U_2=1$. But $U_2=1$ says
$n-2$ has no prime factor $\ge5$; $n-2$ is odd ($n$ odd) and
$n-2\equiv-2\equiv1\pmod3$ ($3\mid n$), so $n-2$ has no prime factor at
all, i.e. $n-2=1$, $n=3$, contradicting $j=n/3\ge5$ (indeed any $j>1$).
Only the divisibility half of Proposition 4.1 is used; no EEES78 input,
no exception-pair caveat (the sole $i=3$ exception pair is $(8,3)$,
with $n$ even). $\square$

**Claim F1.5 (PROVED, corollary).** **There is no counterexample to
$\#699$ at $i=3$ with $n$ odd, for any $j$.** Consequently $i=3$ is
reduced, as a counterexample problem, to $n$ even.

*Proof.* A counterexample with $n$ odd satisfies (LD3) (A1.16(i)), hence
is pinned by A1.16(iv) to the shape of Claim F1.3, which Claim F1.4
excludes. (The pinning needs $n>9$ in A1.16(iv)'s statement; for
$n\le9$ there is no admissible $j$ with $3<j\le n/2$ and $j\ge5$, and
$n\le20{,}000$ is swept in any case.) $\square$

**Claim F1.6 (the other levers, and exactly where they stop).**
(a) (PROVED, computation; script §D) (N2) **alone** does not close the
pinned case: among the $111{,}110$ pinned triples with $n\le10^6$
($n$ odd, $v_3(n)=1$, $j=n/3$), exactly $3{,}472$ satisfy the (N2)
inequality $U_1U_2\le(j-1)(j-2)/6$, the smallest being $(n,j)=(129,43)$
with $(U_1,U_2)=(1,127)$: there $V_3(n)=43\cdot127\le C(43,3)$, so size
through (N2) is genuinely insufficient, and it is (LD3) (the clause
$43\bmod127=43>2$ at $r=2$) and Proposition 4.1, not (N2), that exclude
such shapes. (b) (N1) in the form of Claim F1.3 was not needed and gives
no contradiction by itself in the pinned case: it constrains primes
dividing $j$ or $n-1$, while the fatal prime power in examples like
$(129,43)$ comes from $n-2$, which (N1) does not see. (c) **GAP
(superseded, not filled):** the higher-digit Kummer conditions beyond
the lowest $a$ digits (for $q=p^a\Vert(n-r)$, $p\nmid C(n,j)$ requires
$j$ digitwise $\le n$ in base $p$ at *every* digit, of which (LD3) uses
only digits $0,\dots,a-1$) were **not** developed in the odd case,
because Proposition 4.1 — whose proof localises against $c=n-j$ rather
than against the top three numbers — closes it without them. Whether
the higher-digit conditions alone (without Proposition 4.1) close the
pinned case is **OPEN** and is not claimed here.

## 3. Task 3: the SPLIT-even attack — partial closure, exact residual

Throughout this section $n$ is even, so $n-1$ is the odd top number,
$R(n-1)\in\{n-1,(n-1)/3\}$, and (LD3) requires $R(n-1)=X_0X_1$,
$X_0\mid j$, $X_1\mid j-1$.

**Claim F1.7 (PROVED — a prime-power factor of $n-1$ above $(n-1)/3$
excludes the splitting).** If $n$ is even and some relevant prime power
$q\Vert(n-1)$ satisfies $q>(n-1)/3$ (a fortiori if $q>n/3$), then
$(n,3,j)$ is not a counterexample, for any $j$.

*Proof.* The cofactor $s=(n-1)/q$ is a positive integer $<3$, and $n-1$
is odd, so $s=1$ and $q=n-1$. The splitting requires $q\mid j$ or
$q\mid j-1$, but $0<j-1<j\le n/2<n-1=q$ for $n>2$, impossible. This
sharpens the Cycle 1 observation (which needed a prime power exceeding
$n/2$, or $R(n-1)$ itself a single prime power) to the threshold
$(n-1)/3$ for an individual factor. $\square$

**Claim F1.8 (PROVED — the combined size bound from the splitting, and
where it stops).** A counterexample with $n$ even satisfies
$$n\ \le\ 3j(j-1)+1.$$
Hence the splitting is excluded whenever $j$ is small enough that
$3j(j-1)+1<n$. But this never excludes the region $Q=2$: there
$n\le3j-1<3j(j-1)+1$ for all $j\ge2$ (at $j=2$ the difference is $2$,
and it grows), so for $j$ comparable to $n/2$ the bound is vacuous.
The companion bound from (N2), $V_3(n)\ge(n-1)/9$ (the $n-1$ contribution
to $V_3(n)$ is $R(n-1)$ or $R(n-1)/3$, and $R(n-1)\ge(n-1)/3$) combined
with $V_3(n)\le C(j,3)$ gives only $n<\tfrac32j^3+1$, strictly weaker
than $3j(j-1)+1$ for $j>2$. **This is exactly where the pure size
arguments stop in the even case.**

*Proof.* $R(n-1)=X_0X_1\le j(j-1)$ since $X_0\mid j$ gives $X_0\le j$
and $X_1\mid j-1$ gives $X_1\le j-1$ (for $j\ge2$, including the cases
$X_0=1$, $X_1=1$); and $R(n-1)\ge(n-1)/3$ since $R(n-1)\in\{n-1,(n-1)/3\}$.
Combine. $\square$

**Claim F1.9 (PROVED — the label-retaining consequence of Proposition
4.1 in the even case).** Let $(n,3,j)$ be a counterexample, $n=Qj+R$,
$T=R+2(Q-1)$ as in Claim F1.2.
(a) If $R\ge3$ ($h=0$): **every** prime-power part $q^a\Vert V_3(n)$
satisfies $q^a\le T$. In particular every relevant prime power
$p^a\Vert(n-r)$ with $p\ge5$ is $\le T$, and the $3$-part of $V_3(n)$
is $\le T$.
(b) If $R\in\{0,1,2\}$ ($h=1$, apart from the central $(Q,R)=(2,0)$):
for each $r\in\{0,1,2\}$ with $r\ne R$, the top number $n-r$ has **no
prime factor $>T$** in its $\ge5$ part; and any prime power
$P=p^a\Vert(n-R)$ ($p\ge5$) with $p>T$ satisfies $P\mid j$.

*Proof.* (a) $V_3(n)\mid\Lambda_3(T)$ by Claim F1.2, so
$q^a\mid\Lambda_3(T)$ forces $a\le\lfloor\log_qT\rfloor$, i.e. $q^a\le T$.
For $p\ge5$, the $p$-part of $V_3(n)$ is exactly $p^a$ ($p$ divides a
unique top number and $p\nmid6$). (b) Let $P=p^a\Vert(n-r)$, $p\ge5$,
$p>T$. Then $P\mid V_3(n)\mid\Lambda_3(T)\cdot j$ (Claim F1.2, $h=1$),
and $p\nmid\Lambda_3(T)$ since $\lfloor\log_pT\rfloor=0$; hence
$P\mid j$. Also $P\mid n-r=Qj+(R-r)$. If $r\ne R$ then
$P\mid R-r$ with $0<|R-r|\le2$, impossible for $P\ge5$; so no such $P$
exists for $r\ne R$. For $r=R$ the conclusion $P\mid j$ is the
statement. This is the label information (which top number, and which
of $j-r$ vs $\Lambda_3(T)$) that aggregate size arguments discard.
$\square$

**Claim F1.10 (PROVED — four even $(Q,R)$ subfamilies are closed).**
There is no counterexample with $n$ even and
$(Q,R)\in\{(2,2),(3,0),(3,2),(4,0)\}$ (for $(2,2)$, none with $j\ge5$;
$j=4$ is in the closed region $j\le3i/2$).

*Proof.* In each case $m=n-1$ is odd and $\gcd(j,m)$ is $1$ or is
controlled by $m-Qj=R-1\in\{-1,1\}$; we use that every $\ge5$ prime
power $P\Vert m$ divides $V_3(n)$ (unique top, $p\nmid6$).

$(Q,R)=(3,0)$: $V_3(n)\mid3j$ (Claim F1.2). Each $P\Vert m$ ($p\ge5$)
has $P\mid3j$ and $\gcd(P,3)=1$, so $P\mid j$; the $P$ are pairwise
coprime, so $U_{n-1}\mid j$. Also $U_{n-1}\mid m$ and $m-3j=-1$, so
$U_{n-1}=1$. Then $m$ has no prime factor $\ge5$ and $m=3j-1\equiv-1
\pmod3$ excludes the prime $3$; $m$ odd excludes $2$; so $m=1$,
contradicting $m=3j-1\ge14$.

$(Q,R)=(2,2)$: $V_3(n)\mid3j$, $m=2j+1$. As above $U_{n-1}\mid j$ and
$U_{n-1}\mid m$ with $m-2j=1$, so $U_{n-1}=1$ and $m=3^b$ for some
$b\ge0$. If $b\ge2$, $m$ is the unique top divisible by $3$, so
$3^{b-1}\Vert V_3(n)$ in the $3$-part, and $3^{b-1}\mid3j$; but
$j=(3^b-1)/2$ is not divisible by $3$ (else $3\mid3^b-1$), so
$b-1\le1$, $b\le2$. The cases $b=0,1,2$ give $j=0,1,4$ respectively
($m=1,3,9$): no $j\ge5$.

$(Q,R)=(3,2)$: $V_3(n)\mid15j$, $m=3j+1$, so $3\nmid m$. For $P\Vert m$
with $p\ge7$: $p\nmid\Lambda_3(6)=15$, so $P\mid j$ by Claim F1.9(b)'s
argument; these $P$ are coprime and divide $m$ too, and $m-3j=1$, so
their product is $1$: $m$ has no prime factor $\ge7$. Write $m=5^a$.
If $a=0$, $m=1$, impossible. If $a\ge1$, the $5$-part of $V_3(n)$ is
$5^a\mid15j$, so $5^{a-1}\mid j$; but $j=(5^a-1)/3$ is not divisible by
$5$ ($5^a-1\equiv-1\pmod5$), forcing $a=1$, and then $3j+1=5$ has no
integer solution (it also fails the congruence $5^a\equiv1\pmod3$,
which needs $a$ even). All $a$ are excluded.

$(Q,R)=(4,0)$: $V_3(n)\mid15j$, $m=4j-1$, $\gcd(j,m)=1$. By Claim
F1.9(b) with $T=6$, $r=1\ne R=0$: $m$ has no prime factor $>6$, so its
prime factors lie in $\{3,5\}$. The $5$-part: if $5^a\Vert m$, $a\ge1$,
then $5\nmid j$ (coprimality), so $5^a\mid15j$ forces $a\le1$. The
$3$-part: if $3^b\Vert m$ with $b\ge2$, then $m$ is the unique top
divisible by $3$, $3^{b-1}\mid15j$, $3\nmid j$, so $b-1\le1$, $b\le2$
($b\le1$ is unconstrained and allowed). Hence
$m\in\{3^b5^a:b\le2,a\le1\}=\{1,3,9,5,15,45\}$, and $4j-1=m$ gives
integer $j$ only for $m=3$ ($j=1$) and $m=15$ ($j=4$): no $j\ge5$.
$\square$

**Claim F1.11 (OPEN — the exact residual class in the even case).**
After Claims F1.7–F1.10, Price's central case, and Claim F1.5, a
counterexample at $i=3$ must have $n$ **even**, $(Q,R)\notin
\{(2,0),(2,2),(3,0),(3,2),(4,0)\}$, and simultaneously:
(i) (LD3) in full, with the $n-1$ splitting having no prime-power
factor $>(n-1)/3$ (Claim F1.7);
(ii) $n\le3j(j-1)+1$ (Claim F1.8);
(iii) if $R\ge3$: every prime-power part of $V_3(n)$ is $\le
T=R+2Q-2$ (Claim F1.9(a)); in particular every $\ge5$ prime power
of every top number is $\le T$, and the $3$-part of $V_3(n)$ is
$\le T$ (the exact $3$-power of a top number may be $3T$);
(iv) if $R\in\{0,1,2\}$: every top number $n-r$ with $r\ne R$ has all
its $\ge5$ prime factors $\le T=R+2Q-2$, and every $\ge5$ prime power
of $n-R$ whose prime exceeds $T$ divides $j$ (Claim F1.9(b));
(v) (N1) and (N2).
No argument in this file excludes this residual class in general, and
it is **not** claimed to be empty. It is genuinely nonempty as a
*formal* class for the Proposition 4.1 + $(n-1)$ argument alone:
(PROVED, computation; script §F) for $(Q,R)=(4,2)$, $T=8$, that
argument leaves exactly the three candidates $(n,j)=(22,5),(46,11),
(106,26)$ (from $n-1=3^b5^a7^c$, $b\le2$, $a,c\le1$, $n-1\equiv1
\pmod4$); each is then killed by (LD3) directly, with
$\gcd(V_3(n),C(n,j))=77,69,371$ respectively — but that disposal is
per-instance, not a general argument. Closing the residual class in
general is equivalent, for the routes in this file, to the even half
of (H3) and remains **OPEN**.

## 4. Task 4: Del Pin, refined; the pairpass frontier; (LD3) per pair

**Claim F1.12 (PROVED — Del Pin's condition at $i=3$ is exactly
$j\le5$).** For $i=3$, $C(2j,3)\ge C(j,3)^2$ holds iff $j\le5$
($j=4$: $56\ge16$; $j=5$: $120\ge100$), recovering $J_1(3)=5$ and the
closure of $(3,5)$ for all $n$ (outside EEES exceptions, of which the
only one at $i=3$ is $(8,3)$, with $8<2j$).

*Proof.* For $j\ge6$:
$\dfrac{C(2j,3)}{C(j,3)^2}=\dfrac{\rho_j}{C(j,3)}$ with
$\rho_j=\dfrac{C(2j,3)}{C(j,3)}=\dfrac{4(2j-1)}{j-2}
=8+\dfrac{12}{j-2}\le11$ (decreasing in $j$), while $C(j,3)\ge C(6,3)
=20$; hence the ratio is $\le11/20<1$. (Values in script §A.) $\square$

**Claim F1.13 (PROVED — the $V_3$-refined Del Pin comparison).** Let
$v=v_2(C(n,3))$, so $V_3(n)=C(n,3)/2^{v}$ exactly. A triple $(n,3,j)$
is **not** a counterexample whenever
$$2^{v}\;<\;\frac{C(n,3)}{C(j,3)}.$$
In particular, since $C(n,3)/C(j,3)$ is increasing in $n$ and its
minimum on $n\ge2j$ is $\rho_j=8+\frac{12}{j-2}>8$:
$$\textbf{for every } j>3,\ \textbf{every } n\ge2j\
\textbf{with } v_2(C(n,3))\le3\ \textbf{is closed,}$$
for all $j>5$ as well, with no EEES78 input. More generally, for each
$v$ and $j$, every $n\ge n_0(j,v)$ with $v_2(C(n,3))\le v$ is closed,
where $n_0(j,v)$ is the least $n\ge2j$ with $C(n,3)>2^vC(j,3)$;
exactly (script §A): $n_0(j,4)=14,17,19,24,49$ and
$n_0(j,5)=17,20,24,30,62$ for $j=6,7,8,10,20$.

*Proof.* A counterexample satisfies $V_3(n)\mid C(j,3)$ (key lemma
with $d=V_3(n)$, using $C(j,3)=C(j,j-3)$), hence $V_3(n)\le C(j,3)$,
i.e. $C(n,3)\le2^{v}C(j,3)$: the displayed condition is its negation.
The uniform case is $2^3=8<\rho_j\le C(n,3)/C(j,3)$. $\square$

**Claim F1.14 (FALSE — the direction of the $v_2$ condition).** The
suggestion that in this comparison it is *largeness* of $v_2(C(n,3))$
that closes triples is false: the closing condition in Claim F1.13 is
an **upper** bound on $v_2$. Largeness of $v_2$ shrinks $V_3(n)$ and
helps a counterexample hide. Sharpness witness: at $(n,j)=(16,7)$,
$v_2(C(16,3))=v_2(560)=4$ and $V_3(16)=35=C(7,3)$ exactly, so the
comparison gives equality and cannot exclude that triple (it is
excluded by other means: $\gcd(V_3(16),C(16,7))=5$, and $(3,7)$ is
closed per pair by Claim F1.16); hence $v_2\le3$ in Claim F1.13 cannot
be raised to $4$ uniformly in $n$. The refined comparison does **not**
by itself close any full pair $(3,j)$ with $j>5$ for *all* $n$: it
closes, for each such $j$, the subclass $\{n\ge2j:v_2(C(n,3))\le3\}$
(and the larger subclasses of the threshold form above). $\square$

**Claim F1.15 (PROVED, computation — what the cap-$20{,}000$ sweep's
pairpass file already clears at $i=3$).** In
`~/workspace/math-hunt/erdos-699/pairpass_20000.json`, the row
`cleared_js_by_i['3']` consists of exactly the $154$ values
$$j=5,6,\dots,158,$$
contiguous, with no gaps (read directly from the file; not recomputed).
($j=4$ is absent from the row: it lies in the closed region
$j\le3i/2$.) For scale, $N(3,158)=19{,}926\le20{,}000$ (script §A
method), which is why the cap bites exactly there.

**Claim F1.16 (PROVED, computation — (LD3) alone closes every pair
$(3,j)$ with $5\le j\le2000$).** For every $j$ with $5\le j\le2000$,
the system (LD3) has **no** solution $(n,j)$ with $2j\le n\le N(3,j)$.
Consequently, by the finite reduction (and since the only EEES78
exception pair at $i=3$ is $(8,3)$, with $8<2j$ for $j\ge5$, so no
exception triple lies in the interval), **the pair $(3,j)$ admits no
counterexample for any $n$, for every $5\le j\le2000$** — extending
the previously recorded per-pair frontier ($j\le158$ by the sweep,
$j\le465$ by S1's Kummer reduction as reported in P-A1) to $j\le2000$
by the pure low-digit method.

*Method (script §B; exact).* $N(3,j)=\max\{n:C(n,3)<C(2j,6)\}$ is
computed by exact binary search ($N(3,2000)=3{,}239{,}787$). A pair
satisfying (LD3) must have $R(n)\mid j$, hence $R(n)\le2000$. Every
$n$ with $R(n)\le2000$ is enumerated **exactly once** as $n=d\cdot t$
where $d=R(n)$ is odd with $v_3(d)\in\{0\}\cup[2,\infty)$ and
$t=2^a$ (if $v_3(n)\ne1$) or $t=3\cdot2^a$ (if $v_3(n)=1$, in which
case $v_3(d)=0$): there are $18{,}178$ such $n\le N(3,2000)$. For each,
$j$ runs over the multiples of $R(n)$ in $[4,2000]$ with $2j\le n$
($148{,}591$ candidate pairs; the $r=0$ clause is then automatic since
the relevant prime powers are pairwise coprime and their product
$R(n)$ divides $j$), and the $r=1,2$ clauses are tested directly from
the exact prime-power factorisations of $n-1,n-2$. Survivors: **none**,
for any $j$. The enumeration's completeness is the displayed
$d\cdot t$ decomposition, which is a restatement of the definition of
$R(n)$. $\square$

## 5. Task 5: bounded searches

**Claim F1.17 (PROVED, computation — (LD3) to $n\le10^6$, both
families).** (Script §§D–E; two independent implementations, §7.)
(a) **SPLIT-odd family:** of the $111{,}110$ values $n\le10^6$ with
$n$ odd, $v_3(n)=1$, $j=n/3$ (tested by trial-division factorisation
of $n-1,n-2$), **zero** satisfy the $r=1,2$ clauses of (LD3).
(b) **Full (LD3), in particular SPLIT-even:** (LD3) has **no solution
$(n,j)$ with $n\le10^6$ and $3<j\le n/2$ at all.** The search
(SPF-sieve implementation) tested $7{,}085{,}360$ candidate pairs
(the multiples of $R(n)$, as in Claim F1.16, over the $611{,}107$
values of $n\le10^6$ with $R(n)\le n/2$): **zero survivors.** This
extends the Cycle 1 computation "no (LD3) solution with $n\le5000$"
to $n\le10^6$. There are no survivors to double-verify; the double
verification is instead at the level of implementations (§7): the
trial-division odd-family search (a) and the SPF search (b) agree on
the odd family, and both agree with the brute-force checks of §7 on
their common range. These are finite computations about (LD3), not a
proof of (H3).

## 6. Task 6: closing statement for $i=3$

**Claim F1.18 (PROVED — summary of what this file adds; and what
remains OPEN).**

*Proved in this file, beyond Cycle 1:*
1. Price Proposition 4.1 extracted exactly and specialised to $i=3$
   (F1.1, F1.2).
2. **No $i=3$ counterexample has $n$ odd** (F1.4, F1.5). $i=3$ is
   reduced to $n$ even.
3. In the even case: a prime-power factor of $n-1$ above $(n-1)/3$
   is impossible (F1.7); $n\le3j(j-1)+1$ (F1.8); the label-retaining
   Proposition 4.1 bounds (F1.9); and the subfamilies
   $(Q,R)\in\{(2,2),(3,0),(3,2),(4,0)\}$ are closed (F1.10).
4. The $V_3$-refined Del Pin comparison: every $(3,j)$, $j>3$, is
   closed for all $n\ge2j$ with $v_2(C(n,3))\le3$, with exact
   thresholds for larger $v_2$ (F1.13); the unrefined Del Pin
   condition at $i=3$ is exactly $j\le5$ (F1.12).
5. Per pair: $(3,j)$ is closed for all $n$ for every $5\le j\le2000$,
   by (LD3) inside the finite reduction (F1.16); the cap-$20{,}000$
   pairpass row alone gives $5\le j\le158$ (F1.15).
6. Computations: (LD3) has no solution with $n\le10^6$ in general
   (F1.17(b)) and none in the SPLIT-odd family to $10^6$ (F1.17(a)).

*Reduced:* the whole of $i=3$ is reduced to the residual even class
of Claim F1.11 (even $n$; $(Q,R)$ outside the closed list; the
$T$-boundedness / label conditions (iii)–(iv); (LD3), (N1), (N2)).

*Still OPEN, explicitly:* (H3) in general — (LD3) solutions with
$n>10^6$ are not excluded by computation, and no proof in this file
excludes the residual class of F1.11 for all even $n$; per-pair
(LD3) closure for $j>2000$ was not computed (the method's cost grows
like the candidate count at $N(3,j)\approx(2j)^2/120^{1/3}$); the
higher-digit Kummer route of Claim F1.6(c). **$i=3$ is not closed,
(H3) is not proved, and $\#699$ is not claimed solved.**

## 7. Verification log

All numbers above are outputs of `proofs/P-F1_checks.py` (53 s,
stdlib only, exact arithmetic), whose sections assert their own
headline values:
- §A: $\Lambda_3$ values, $N(3,j)$ values (including
  $N(3,465)=174{,}408$, matching P-A1's frontier scale, and
  $N(3,2000)=3{,}239{,}787$), Del Pin ratios and thresholds.
- §B: Claim F1.16's candidate search: $18{,}178$ candidates,
  $148{,}591$ pairs, zero survivors.
- §C (independent code path: plain SPF sieve, brute force over **all**
  $j$, no $R(n)$-candidate generation): the $\ge5$-only (LD3) system
  for $n\le2000$ returns **exactly** the known six pairs
  $(10,5),(28,14),(82,41),(162,70),(244,122),(730,365)$ — validating
  the factorisation and clause tests against Cycle 1 — the full (LD3)
  system for $n\le2000$ returns zero, and per-pair brute force on
  $[2j,N(3,j)]$ for $j\le150$ returns zero, agreeing with §B.
- §D: Claim F1.17(a) and Claim F1.6(a) ($111{,}110$ tested; $3{,}472$
  pass (N2) alone; zero (LD3) survivors).
- §E: Claim F1.17(b) ($611{,}107$ values of $n$ with candidates;
  $7{,}085{,}360$ pairs; zero survivors), using a third factorisation
  implementation (SPF by descending slice assignment).
- §F: Claim F1.11's three $(4,2)$ candidates, their (LD3) failure,
  and their gcds $77, 69, 371$ for $(22,5),(46,11),(106,26)$.
