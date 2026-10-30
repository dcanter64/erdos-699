# Erdős Problem #699: Referee 1 Report (Reconstruction Referee)

**Scope.** This report referees the argument exactly as exposited by
Thomas Bloom (last edited 27 Aug 2026) on the Erdős Problems #699 page,
together with its cited external input, Ecklund, Eggleton, Erdős, and
Selfridge, *On the prime factorization of binomial coefficients*,
J. Austral. Math. Soc. A 26(3) (1978), 257-269, cited below as EEES78.

**Materials and limits.** Bloom's exposition is the fullest refereeable
text. The raw GPT 5.6 Sol proof claim (prompted by Liam Price) is
inaccessible (forum route returns HTTP 403; the text is not indexed).
No conclusion in this report about the *exposited* argument depends on the
raw claim. Where the problem page makes an assertion that the exposition
does not contain (the case n = 2j, Section 6), that assertion is refereed
separately and classified UNVERIFIABLE as presented. I did not refetch
the inaccessible claim text.

**Classification vocabulary.**

* **PROVED**: the step is correct and a complete justification is either
  in the exposition or supplied in this report from elementary facts.
* **GAP (filled)**: the exposition omits a justification that is needed
  for a formal proof, but the omitted justification is correct and is
  supplied in this report.
* **GAP (external)**: the exposition omits a case or input that is not
  supplied inside the exposition at all, but that can be, and in the
  campaign record (Phase 0) and in my own recomputation (Appendix B) has
  been, supplied from outside the exposition.
* **ERROR**: the step is false as stated, with a failing case given.
* **UNVERIFIABLE**: the step depends on text or material not available to
  the referees.
* **EXTERNAL**: a published result used as a black box, in the normal
  way. Its statement, hypotheses, and exception list are checked here;
  its internal proof is not re-refereed in this pass.

**Headline finding.** The exposited argument for the region
j ≤ 3i/2 is mathematically sound in every one of its mathematical steps.
I found no ERROR in the core argument. It has exactly one material
incompleteness as a standalone text: it invokes EEES78 "with finitely
many explicit exceptions" but never lists the exceptions and never
discharges the cases they block. That is a GAP (external), not an error
in the deduction: once the standard non-exception hypothesis is made
explicit, every subsequent step goes through, including at all boundary
cases, and the exception cases are a finite explicit set that is
discharged by direct computation (Section 5, Appendix B). The problem
page's additional assertion about n = 2j is a different matter: it is
not proved, or even stated as a goal, in the exposition, and the
exposited method provably cannot be extended to prove it when
j > 3i/2 (Section 6).

---

## 1. Reconstruction as a formal proof

### 1.1 Notation, ranges, and standing hypotheses

Throughout, all variables are integers.

* **(H1) Range.** 1 ≤ i < j ≤ n/2, where n/2 is the real number.
  Equivalently: 1 ≤ i < j and 2j ≤ n. Two consequences are used
  repeatedly and are recorded here once:
  * 2i < 2j ≤ n, hence **n ≥ 2i + 1**, in particular n ≥ 2i.
  * Writing **r := j - i**, we have **1 ≤ r ≤ j - 1** (r ≥ 1 from i < j;
    r ≤ j - 1 from i ≥ 1), and **1 ≤ r < j ≤ n - j < n**.
* **(H2) Positivity.** Every binomial coefficient C(a, b) with
  0 ≤ b ≤ a that appears is a positive integer. In particular
  C(n, i) > 1 in range (H1): indeed C(n, i) ≥ n for
  1 ≤ i ≤ n - 1 (for fixed n the values C(n, i) over
  1 ≤ i ≤ n - 1 are minimised at the ends i = 1 and i = n - 1, where
  they equal n), and n ≥ 2j ≥ 4 by (H1). The fact C(n, i) > 1 is
  needed only in the discussion of v = 1 in Section 4(a).
* **(H3) The split of C(n, i).** Write the prime factorisation
  C(n, i) = ∏_p p^(a_p) (a_p ≥ 0, a_p = 0 for almost all p). Define
  * u := ∏_{p < i} p^(a_p) (the part of C(n, i) supported on primes < i),
  * v := V_i(n) := ∏_{p ≥ i} p^(a_p) (the part supported on primes ≥ i),
  with the empty product equal to 1. Then
  **C(n, i) = u v, gcd(u, v) = 1, u ≥ 1, v ≥ 1,**
  because the two products range over disjoint sets of primes. The prime
  divisors of v are exactly the primes p ≥ i with p | C(n, i).
* **(H4) Supposed counterexample.** A triple (n, i, j) satisfying (H1)
  is a *counterexample* if gcd(v, C(n, j)) = 1. By Lemma 1 below this
  is exactly a counterexample to Problem #699.
* **(H5) The EEES78 exception set.** Let E be the set of pairs
  E = {(8,3), (9,4), (10,5), (12,5), (21,7), (21,8), (30,7), (33,13),
  (33,14), (36,13), (36,17), (56,13)}.
  Section 4(b) and Appendix A verify what EEES78 says about E.

### 1.2 Lemmas

**Lemma 1 (Equivalence reformulation).**
For (n, i, j) satisfying (H1), the following are equivalent:
(i) there exists a prime p ≥ i with p | C(n, i) and p | C(n, j);
(ii) gcd(v, C(n, j)) > 1.
Hence Problem #699 (statement (i) for all (H1) triples) is equivalent to:
no (H1) triple is a counterexample in the sense of (H4).

*Proof.* The prime divisors of gcd(v, C(n, j)) are exactly the primes
dividing both v and C(n, j). By (H3), p | v iff (p ≥ i and p | C(n, i)).
So a prime divides the gcd iff p satisfies the conditions in (i), and a
positive integer is > 1 iff it has a prime divisor. Both directions are
this single observation. The case v = 1 is included without exception:
if v = 1 then v has no prime divisors, so (i) fails, and
gcd(1, C(n, j)) = 1, so (ii) fails; the equivalence of the two failures
is exactly the statement that such a triple would be a counterexample in
both formulations. ∎

**Lemma 2 (EEES78, in the exact form used).**
Let (n, i) satisfy n ≥ 2i, i ≥ 1, and define u, v as in (H3) with
k := i. If (n, i) ∉ E, then u < v, and consequently
**v² > C(n, i), i.e. v > C(n, i)^(1/2).**

*Proof of the consequence, and status of the input.*
EEES78 (EXTERNAL) states: for positive integers n, k with **n ≥ 2k**,
writing C(n, k) = u v with every prime factor of u less than k and every
prime factor of v at least k, one has u < v with just 12 exceptions,
which are determined; the exceptions are the pairs E of (H5), and for
each of them u > v (Appendix A). Granting that statement, suppose
(n, i) ∉ E. Then u < v. Since v > 0, multiplying u < v by v gives
u v < v². By (H3), u v = C(n, i). Hence C(n, i) < v², and taking square
roots of positive reals gives C(n, i)^(1/2) < v. ∎

*Range check.* The proof applies Lemma 2 at the pair (n, k) = (n, i)
only (never at (n, j)). The hypothesis n ≥ 2k of EEES78 becomes
n ≥ 2i, which (H1) supplies with room to spare: n ≥ 2i + 1
(Section 1.1). The hypothesis "positive integers" is satisfied. Note
also Bloom's convention is the operative one: u on primes **< k**, v on
primes **≥ k**. The same paper's other convention (u on primes ≤ k,
v on primes > k, 19 cases, only finiteness proved) is a different
theorem and is not used anywhere in the argument.

**Lemma 3 (The identity).**
For (n, i, j) satisfying (H1),
C(n, i) · C(n - i, j - i) = C(n, j) · C(j, i).

*Proof.* All factorial arguments below are nonnegative integers, since
0 ≤ i < j ≤ n. By the factorial formula, the left side is
[n! / (i! (n-i)!)] · [(n-i)! / ((j-i)! (n-j)!)]
= n! / (i! (j-i)! (n-j)!),
and the right side is
[n! / (j! (n-j)!)] · [j! / (i! (j-i)!)]
= n! / (i! (j-i)! (n-j)!).
The two are equal. (Equivalently, both sides count the choices of an
i-subset and a disjoint (j-i)-subset of an n-set.) ∎

**Lemma 4 (Key divisibility lemma).**
Let d be a positive integer with d | C(n, i) and gcd(d, C(n, j)) = 1.
Then d | C(j, i).

*Proof.* Since d | C(n, i), d divides C(n, i) · C(n - i, j - i), which
by Lemma 3 equals C(n, j) · C(j, i). So d | C(n, j) · C(j, i) with
gcd(d, C(n, j)) = 1. The general form of Euclid's lemma now applies:
if gcd(d, m) = 1 and d | m t then d | t (proof: Bézout gives
x d + y m = 1 for integers x, y; multiplying by t, t = x d t + y (m t),
and d divides both terms on the right). With m = C(n, j) and
t = C(j, i), d | C(j, i). ∎

**Lemma 5 (Vandermonde bound, with strictness).**
For (n, i, j) satisfying (H1), with r = j - i,
C(j, r)² < C(2j, 2r).

*Proof.* Vandermonde's identity (convolution of two copies of
(1 + x)^j, coefficient of x^(2r)) gives
C(2j, 2r) = Σ_k C(j, k) · C(j, 2r - k),
the sum over all integers k, with the standard convention that
C(j, s) = 0 unless 0 ≤ s ≤ j. Every term is a nonnegative integer. The
term at k = r is C(j, r) · C(j, r) = C(j, r)², and r is in range
(0 ≤ r ≤ j, indeed 1 ≤ r ≤ j - 1, by (H1)). It remains to exhibit at
least one other index k ≠ r with a positive term; in fact there are
always at least three positive terms, in two cases:

*Case A, 2r ≤ j.* The positive terms are exactly those with
0 ≤ k ≤ 2r, a total of 2r + 1 ≥ 3 terms (r ≥ 1). In particular k = 0
(which differs from r, since r ≥ 1) contributes
C(j, 0) · C(j, 2r) = C(j, 2r) > 0.

*Case B, 2r > j.* The positive terms are exactly those with
2r - j ≤ k ≤ j, a total of j - (2r - j) + 1 = 2j - 2r + 1 = 2i + 1 ≥ 3
terms (i ≥ 1). In particular k = j (which differs from r, since
r ≤ j - 1) contributes C(j, j) · C(j, 2r - j) = C(j, 2r - j) > 0;
here 0 < 2r - j ≤ j - 2 because 1 ≤ r ≤ j - 1, so the binomial
coefficient is positive.

In both cases the sum contains the k = r term plus at least one (in
fact at least two) further strictly positive terms, so the inequality
is strict. ∎

*Small cases, checked explicitly (they are covered by the proof above,
and are recorded because they are the cases a reader is most likely to
worry about).*
- r = 1 (j = i + 1, so j ≥ 2): Case A applies (2 ≤ j). Terms k = 0, 1, 2:
  C(2j, 2) = C(j, 2) + j² + C(j, 2) > j² = C(j, 1)². Smallest instance
  (i, j) = (1, 2): C(4, 2) = 6 > 4 = C(2, 1)², extra terms 1 + 1.
- i = 1, j = 2: the same instance; C(2j, 2r) = C(4, 2) = 6 > C(2, 1)² = 4.
- i = 1, j ≥ 3: then r = j - 1 and 2r = 2j - 2 > j, Case B, with exactly
  2i + 1 = 3 positive terms (k = j - 2, j - 1, j). Instance (i, j) = (1, 3):
  C(6, 4) = 15 = 3 + 9 + 3 > 9 = C(3, 2)².
- Boundary 2r = j (j even, r = j/2): Case A, 2r + 1 = j + 1 ≥ 3 terms.
- No case is left out: 2r ≤ j and 2r > j exhaust all possibilities, and
  the inputs used are exactly r ≥ 1 (for Case A) and i ≥ 1 (for Case B).
  Both come from (H1). I also verified the inequality computationally
  for all 1 ≤ i < j ≤ 600 (exact integer arithmetic, no failures), in
  agreement with Phase 0, Item 2, test C.

**Lemma 6 (The size bound, and finiteness per pair).**
Suppose (n, i, j) satisfies (H1), (n, i) ∉ E, and (n, i, j) is a
counterexample in the sense of (H4). Then
**C(n, i) < C(2j, 2(j - i)).**

*Proof.* Apply Lemma 4 with d = v: v | C(n, i) by (H3), and
gcd(v, C(n, j)) = 1 by (H4). Hence v | C(j, i). Now
C(j, i) = C(j, j - i) = C(j, r) by symmetry of binomial coefficients
(i + r = j). Since v ≥ 1 and C(j, r) ≥ 1, divisibility gives
v ≤ C(j, r), hence v² ≤ C(j, r)². By Lemma 5,
v² ≤ C(j, r)² < C(2j, 2r). By Lemma 2 (this is the only place the
hypothesis (n, i) ∉ E is used), v² > C(n, i). Chaining:
C(n, i) < v² and v² ≤ C(j, r)² < C(2j, 2r), so
C(n, i) < C(2j, 2r). ∎

**Corollary 6.1 (Finiteness, stated precisely).**
Fix a pair (i, j) with 1 ≤ i < j. Then there are only finitely many
integers n for which (n, i, j) can be a counterexample.

*Proof.* Any such n satisfies 2j ≤ n (from (H1)). If (n, i) ∉ E,
Lemma 6 gives C(n, i) < B, where B := C(2j, 2(j-i)) depends only on the
fixed pair (i, j). For fixed i ≥ 1, the function n ↦ C(n, i) is
strictly increasing for n ≥ i (Lemma 7(ii) below) and takes positive
integer values, so it tends to infinity; hence the set
{n : C(n, i) < B} is finite (it is contained in {n : n < some explicit
bound}, for instance n ≤ B suffices since C(n, i) ≥ n for
1 ≤ i ≤ n - 1). If instead (n, i) ∈ E, then n belongs to the finite set
of first coordinates of E (n ∈ {8, 9, 10, 12, 21, 30, 33, 36, 56}).
The union of the two finite sets is finite. ∎

**Lemma 7 (Monotonicity of binomial coefficients).**
(i) *In the lower index.* For fixed N, the function k ↦ C(N, k) is
strictly increasing on 0 ≤ k ≤ N/2: for 0 ≤ k < N/2,
C(N, k + 1) / C(N, k) = (N - k) / (k + 1) > 1, because
N - k > N/2 ≥ k + 1 when k + 1 ≤ N/2, and in fact for the case used
below (N = 2j, k ≤ j - 1) the ratio is at least (j + 1)/j > 1.
Consequently, for 0 ≤ a ≤ b ≤ N/2, C(N, a) ≤ C(N, b), with equality
iff a = b.
(ii) *In the upper index.* For fixed i ≥ 1, the function n ↦ C(n, i)
is strictly increasing for n ≥ i: for n ≥ i,
C(n + 1, i) / C(n, i) = (n + 1) / (n + 1 - i) > 1, because i ≥ 1.
Consequently, for i ≤ a ≤ b, C(a, i) ≤ C(b, i), with equality iff
a = b.

*Proof.* Both ratios are the standard one-step ratios from the
factorial formula; all quantities are positive, so the comparisons are
legitimate, and iterating one-step comparisons gives the claims. ∎

### 1.3 The reconstructed theorem

**Theorem R (the exposited result, with all hypotheses explicit).**
Let (n, i, j) satisfy (H1) and **j ≤ 3i/2**. If (n, i) ∉ E, then
(n, i, j) is not a counterexample: gcd(V_i(n), C(n, j)) > 1, i.e.
there is a prime p ≥ i dividing both C(n, i) and C(n, j).

*Proof.* Suppose for contradiction that (n, i, j) is a counterexample.
By Lemma 6 (applicable since (n, i) ∉ E),
C(n, i) < C(2j, 2(j - i)). (⋆)
Now j ≤ 3i/2 is equivalent, on multiplying by 2 and rearranging, to
2(j - i) ≤ i. Combined with (H1):
0 ≤ 2(j - i) ≤ i ≤ j (i ≤ j because i < j), and 2j ≤ n with 2j ≥ i
(so C(2j, i) is defined in the usual range). Lemma 7(i) with N = 2j
applies to the pair 2(j-i) ≤ i, both in [0, j] = [0, N/2]:
C(2j, 2(j - i)) ≤ C(2j, i).
Lemma 7(ii) applies to 2j ≤ n:
C(2j, i) ≤ C(n, i).
Chaining: C(n, i) < C(2j, 2(j-i)) ≤ C(2j, i) ≤ C(n, i), i.e.
C(n, i) < C(n, i), a contradiction. ∎

**Corollary R.1 (the region, once the exceptions are discharged).**
Problem #699 holds for every (n, i, j) satisfying (H1) with
j ≤ 3i/2, *provided* each exception pair (n0, i0) ∈ E is discharged by
direct verification that gcd(V_{i0}(n0), C(n0, j)) > 1 for all
i0 < j ≤ n0/2. That discharge is finite (41 values of j in total), is
recorded in Phase 0, and I recomputed it independently: all 41 values
are > 1 (Appendix B). With that discharge in place, Theorem R covers
the non-exception pairs and the direct check covers the exception
pairs, and together they cover all (H1) triples with j ≤ 3i/2.

### 1.4 Where each hypothesis is used (audit trail)

* **n ≥ 2j (from j ≤ n/2):** used in Lemma 7(ii) step
  C(2j, i) ≤ C(n, i); used to obtain n ≥ 2i for Lemma 2; used as the
  lower end of the range of n in Corollary 6.1. It is *not* needed for
  Lemmas 1, 3, 4, 5, which need only i < j ≤ n.
* **i < j:** gives r ≥ 1 (Lemma 5, Case A count; Lemma 3 range), and
  i ≤ j for Lemma 7(i).
* **i ≥ 1:** gives r ≤ j - 1 (so k = j ≠ r in Lemma 5, Case B), the
  count 2i + 1 ≥ 3 in Lemma 5 Case B, strictness in Lemma 7(ii), and
  the growth needed in Corollary 6.1. If i = 0 the whole argument
  collapses (v would be C(n, 0) = 1), which is one way to see why the
  hypothesis 1 ≤ i in the problem statement is load-bearing.
* **Positivity:** used in Lemma 2 (multiplying u < v by v > 0; taking
  square roots), Lemma 6 (v | C(j, r) implies v ≤ C(j, r) for positive
  integers; squaring preserves ≤), Lemma 5 (extra terms are *positive*,
  not merely nonzero), and Lemma 7 (ratios of positive integers).
* **j ≤ 3i/2:** used in exactly one place, the inequality
  2(j - i) ≤ i in the proof of Theorem R.

---

## 2. Dependency graph

Nodes are inputs (rectangles, in words) and lemmas. An arrow X to Y
means Y's proof uses X.

```
                         [Factorial formula / combinatorics]
                            |            |              |
                            v            v              v
   [Definition of u, v]  Lemma 3    Lemma 7        Vandermonde
        |         |      (identity) (monotonicity)  identity
        |         |          |            |              |
        v         v          v            |              v
   Lemma 1        +--> Lemma 4            |         Lemma 5
  (equivalence)        (Euclid's lemma    |      (strict Vandermonde
        |               + Bezout)          |       bound; uses H1:
        |                  |              |       r >= 1, i >= 1)
        |                  v              |              |
   [EEES78 theorem]        +--------------+--------------+
   [Exact list E:          |              |              |
    12 pairs, u > v]       v              v              v
        |               Lemma 6 (size bound C(n,i) < C(2j, 2(j-i));
        v                uses Lemma 2 + Lemma 4 + Lemma 5;
   Lemma 2               hypothesis (n,i) not in E used here only)
  (v^2 > C(n,i);              |
   uses uv = C,               +-----------> Corollary 6.1
   u < v, v > 0,              |             (finiteness per pair;
   and range n >= 2i          |              uses Lemma 7(ii) growth
   from H1)                   |              and finiteness of E)
                              v
                         Theorem R (region j <= 3i/2;
                         uses Lemma 6 + Lemma 7(i) + Lemma 7(ii)
                         + the arithmetic 2(j-i) <= i
                         from j <= 3i/2)
                              |
                              v
                    Corollary R.1 (full region)
                         uses additionally:
                         [Direct computation discharging
                          all (n0, i0) in E, all i0 < j <= n0/2]
```

Adjacency list (each result, and exactly what it depends on):

| Result | Depends on |
|---|---|
| Lemma 1 (equivalence) | Definition (H3) only. No external input. |
| Lemma 2 (v² > C(n,i)) | EEES78 (EXTERNAL); exact list E; algebra uv = C(n,i); positivity; range check n ≥ 2i from (H1). |
| Lemma 3 (identity) | Factorial formula (or double counting); ranges from (H1). |
| Lemma 4 (divisibility) | Lemma 3; Euclid's lemma in gcd form (via Bézout). |
| Lemma 5 (strict Vandermonde) | Vandermonde's identity; nonnegativity/positivity of binomial coefficients; (H1) in the form r ≥ 1 and i ≥ 1. |
| Lemma 6 (size bound) | Lemma 2, Lemma 4, Lemma 5; symmetry C(j, i) = C(j, j-i); positivity. The hypothesis (n, i) ∉ E enters only through Lemma 2. |
| Corollary 6.1 (finiteness) | Lemma 6; Lemma 7(ii) (strict growth in n); finiteness of E. |
| Lemma 7 (monotonicity) | Factorial one-step ratios; positivity; for (ii), i ≥ 1. |
| Theorem R | Lemma 6; Lemma 7(i); Lemma 7(ii); the equivalence 2(j-i) ≤ i iff j ≤ 3i/2; (H1). |
| Corollary R.1 | Theorem R; the direct exception discharge (external computation, Appendix B). |
| Section 6 obstruction (n = 2j) | Lemma 7(i) (strict form); symmetry C(2j, k) = C(2j, 2j - k). Deliberately does not use EEES78. |

No step depends on Sylvester-Schur, on any property of C(n, j) beyond
its gcd with v, or on the second EEES78 convention. The argument has a
single external mathematical input (EEES78) and a single computational
input (the exception discharge).

---

## 3. Line-by-line verification of the exposition

I take the exposition sentence by sentence. "Bloom line" paraphrases are
kept short; the verbatim text is in the campaign file
texts/bloom_exposition_699.md.

| # | Bloom line | Classification | Referee comment |
|---|---|---|---|
| L0 | "Exposition of a proof of the conjecture when j ≤ 3i/2." | PROVED, conditional on the GAP at L8 being discharged externally | True once Corollary R.1's discharge is included. As a statement about the exposition text alone, it is incomplete by exactly the exception cases (Section 5). |
| L1 | Definition of v; "this problem is then equivalent to asking whether v can be coprime to C(n, j)." | GAP (filled) | No proof is given in the exposition, but the equivalence is a one-line prime-support observation. Filled: Lemma 1, including the case v = 1 (Section 4(a)). |
| L2 | "Main input [EEES78]: (with finitely many explicit exceptions) v > C(n,i)^(1/2)." | EXTERNAL, correctly stated | Derivation from u < v: Lemma 2 and Section 4(b). The parenthetical exceptions are the crux of Section 5. EEES78's exact quantifier (n ≥ 2k) matches, with room (Section 4(b)). |
| L3 | The identity C(n,i)·C(n-i,j-i) = C(n,j)·C(j,i). | PROVED | Lemma 3. Ranges are fine: all factorial arguments are nonnegative under (H1). |
| L4 | "If d | C(n,i) is coprime to C(n,j) then d | C(j,i)." | PROVED | Lemma 4. This is Euclid's lemma in the form gcd(d, m) = 1 and d | m t implies d | t; the exposition compresses it into "the key observation", which is standard and correct. |
| L5 | "If v is coprime to C(n,j) then v | C(j,i) = C(j, j-i)." | PROVED | Lemma 4 at d = v (v | C(n,i) by definition), plus binomial symmetry i + (j - i) = j. |
| L6 | "v² ≤ C(j, j-i)²." | PROVED | Divisibility of positive integers gives v ≤ C(j, j-i); squaring preserves the inequality for nonnegative integers. Positivity is essential and holds (H2). |
| L7 | "C(j, j-i)² < Σ_k C(j,k)·C(j, 2(j-i)-k) = C(2j, 2(j-i))." | GAP (filled) | The equality is Vandermonde; the strictness is asserted without comment in the exposition. It is true in all cases, with at least three positive summands. Filled: Lemma 5, with the case split and small cases in Section 4(c). This is the presentational omission Phase 0 noted; on the deeper pass I confirm it is an omission only, never a near-miss: there is no borderline case (Section 4(c)). |
| L8 | "By [EEES78], in any supposed counterexample C(n,i) < C(2j, 2(j-i))." | GAP (external), material | Correct for counterexamples with (n, i) ∉ E: Lemma 6. As written, the words "in any supposed counterexample" drop the non-exception hypothesis that L2's parenthetical introduced. For an exception pair in the region j ≤ 3i/2 the intermediate claim is not merely unjustified, its antecedent inequality v² > C(n,i) is false, and the displayed conclusion C(n,i) < C(2j, 2(j-i)) is false as well (failing case: (n, i, j) = (8, 3, 4): v = 7, v² = 49 < 56 = C(8, 3), and C(8, 2) = 28 < 56). Note carefully: (8, 3, 4) is a failing case for the *unqualified EEES invocation*, not a counterexample to Problem #699, since gcd(7, C(8, 4)) = gcd(7, 70) = 7 > 1. The repair is a case split plus the discharge in Section 5. I classify this as a GAP rather than an ERROR in the argument, because the qualification exists in L2 and the missing case is finite, explicit, and checkable; but it is the one place where the exposition, read literally and standalone, does not prove what it claims. |
| L9 | "This immediately implies only finitely many possible bad n for fixed i < j." | GAP (filled), with a reading caveat | Correct when "fixed i < j" means a fixed pair (i, j): Corollary 6.1. The word "immediately" glosses two facts, both supplied there: strict growth of C(n, i) in n for i ≥ 1, and the finiteness of E to absorb the n for which L8 is unavailable. Reading caveat: the bound B = C(2j, 2(j-i)) depends on both i and j. For fixed i alone, with j free, there is no uniform finite bound and the remark would be false; nothing in the exposition needs that stronger reading. See Section 4(e). |
| L10 | "If j ≤ 3i/2, we have 2(j-i) ≤ i < j ≤ n/2." | PROVED | Pure arithmetic from (H1): 2(j - i) ≤ i iff 2j ≤ 3i iff j ≤ 3i/2. Each displayed inequality is used: 2(j-i) ≤ i starts the chain, i ≤ j puts i in the monotone range [0, j] for upper index 2j, j ≤ n/2 gives 2j ≤ n. |
| L11 | "C(2j, 2(j-i)) ≤ C(2j, i) ≤ C(n, i), a contradiction." | GAP (filled) | Both monotonicities are correct and are proved in Lemma 7: the first is monotonicity in the lower index on [0, j] for upper index 2j; the second is monotonicity in the upper index for fixed lower index i ≥ 1. The contradiction is genuine because (⋆) in Theorem R is strict while both chain steps are allowed to be equalities. Boundary cases are verified in Section 4(d). |

Net line-by-line result: no line is an ERROR in its mathematical
content under the intended (EEES78-with-exceptions) reading; L7 and L11
are presentational gaps, filled above; L8/L9 contain the one material
gap, the undischarged exceptions, treated in Section 5. The raw GPT
claim's fidelity to this exposition is UNVERIFIABLE (text inaccessible),
and is immaterial to the verdict on the exposited argument, which is
self-contained.

---

## 4. The six points requiring special attention

### (a) The equivalence reformulation, including v = 1

The problem's statement asks for a prime p ≥ i dividing both C(n, i)
and C(n, j). Bloom reformulates via v = V_i(n). The equivalence is
exact, and the proof is Lemma 1: the prime divisors of v are by
construction exactly the candidate primes p, so a common prime exists
iff gcd(v, C(n, j)) has a prime divisor iff the gcd exceeds 1.

Two edge points deserve explicit statement, since the exposition gives
none:

1. **v = 1.** This means C(n, i) has no prime factor ≥ i at all. In
   that case gcd(v, C(n, j)) = 1 automatically, for every j, so the
   triple is a counterexample in the gcd formulation; and statement (i)
   fails because there is no prime ≥ i dividing C(n, i) in the first
   place. The two formulations agree, as failures, so the equivalence
   survives v = 1. The subsequent proof also handles v = 1 correctly
   without a separate case: if v = 1 and (n, i) ∉ E, Lemma 2 gives
   1 = v² > C(n, i) > 1, a contradiction, so a non-exception pair
   cannot have v = 1; if (n, i) ∈ E, Appendix A shows v > 1 for all
   twelve pairs anyway (smallest value v = 7). In fact, EEES78 plus its
   list therefore implies v > 1 for every (n, i) with n ≥ 2i, but the
   argument never needs this as a separate step.
2. **Primes equal to i.** The split in (H3) puts p = i (when i is prime)
   on the v side (p ≥ i), matching both the problem's condition p ≥ i
   and EEES78's convention "at least equal to k". The strengthened
   variant of the problem with p > i, for which the page records
   counterexamples, is a different statement; nothing in this report
   bears on it, and its counterexamples are not counterexamples here.

Classification: GAP (filled). The reformulation is correct.

### (b) From EEES78's u < v to v > C(n,i)^(1/2); the quantifier range

The derivation is pure algebra, but it is worth writing out because the
exposition jumps directly from the citation to the square-root form.
Given: C(n, i) = u v (disjoint prime supports, (H3)); u, v ≥ 1;
hypothesis u < v. Then C(n, i) = u v < v · v = v², where the inequality
is multiplication of u < v by the positive number v. Taking square
roots (an order-preserving operation on positive reals) gives
C(n, i)^(1/2) < v. Conversely, at an exception pair, EEES78's
determination gives u > v, and the same multiplication gives
v² < C(n, i): the inequality the proof needs fails in the *opposite*
direction at exceptions, a fact Section 5 uses.

One refinement a careful referee should record: the abstract of EEES78
says only that u < v "holds with just 12 exceptions, which are
determined", which by itself leaves open the logical possibility of an
exception with u = v (which would also block the strict conclusion
v² > C(n, i)). The possibility does not occur: for each of the twelve
determined pairs, u > v strictly (Appendix A, verified by exact
computation). So "not an exception" and "u < v" coincide, and Lemma 2's
hypothesis (n, i) ∉ E is exactly right.

**Quantifier range.** EEES78 requires n ≥ 2k, with k the lower index of
the binomial coefficient being split. The proof splits C(n, i), so
k = i, and the required hypothesis is n ≥ 2i. The problem's range gives
more: i < j ≤ n/2 implies 2i < 2j ≤ n, hence n ≥ 2i + 1 in integers.
So the EEES78 invocation at (n, i) is in range for every triple the
problem quantifies over, with one unit to spare. There is no hidden
boundary case at n = 2i: such a pair cannot arise under (H1) at all
(it would force i = j). All twelve exception pairs also satisfy
n ≥ 2i (the tightest are (10, 5) with equality and (9, 4)), so the
list E is stated over the same domain.

Classification: PROVED, given EEES78 as EXTERNAL input with its list.

### (c) The strict Vandermonde inequality

The claim is C(j, r)² < C(2j, 2r) for r = j - i, 1 ≤ i < j. The full
proof is Lemma 5. The logical structure a referee should check is:

1. Vandermonde writes C(2j, 2r) as a sum of products C(j, k)·C(j, 2r-k),
   all terms nonnegative integers (zero outside the support range).
2. The term k = r is present and equals the claimed square. Present
   means: r in [0, j] and 2r - r = r in [0, j]; true since 1 ≤ r ≤ j - 1.
3. Strictness is equivalent to: at least one other term is positive.
   This is where a careless version of the argument could fail, e.g.
   if the support of the sum were a single point. It never is: the
   number of positive terms is 2r + 1 ≥ 3 when 2r ≤ j, and
   2i + 1 ≥ 3 when 2r > j. The two expressions are worth noting: the
   count is controlled by r in the first regime and by i in the
   second, and the hypotheses r ≥ 1 and i ≥ 1 are exactly what keeps
   both counts at least 3. The boundary between regimes, 2r = j,
   belongs to the first regime and gives j + 1 ≥ 3 terms.
4. Small cases: (i, j) = (1, 2) (the smallest triple overall, with
   n = 4): 6 > 4, margin 2. (i, j) = (1, 3): 15 > 9. j - i = 1 in
   general: the extra terms are 2·C(j, 2), positive for j ≥ 2. No case
   has margin 1 or relies on a large-n effect.

So the strictness is robust, with at least two extra positive terms in
every case. The exposition's silence on strictness is a presentational
gap only. Classification: GAP (filled); the inequality is PROVED.

### (d) The final chain, its two monotonicities, and the boundaries

The chain is C(2j, 2(j-i)) ≤ C(2j, i) ≤ C(n, i), to be contradicted
against the strict (⋆): C(n, i) < C(2j, 2(j-i)).

*First inequality.* Upper index fixed at N = 2j; lower indices
a = 2(j - i) and b = i satisfy 0 ≤ a ≤ b ≤ j = N/2 (a ≤ b is
j ≤ 3i/2; b ≤ j is i < j; a ≥ 0 is i ≤ j). On [0, N/2], C(N, ·) is
nondecreasing, indeed strictly increasing: the one-step ratio
C(N, k+1)/C(N, k) = (N - k)/(k + 1) exceeds 1 for k ≤ j - 1
(Lemma 7(i)). Hypotheses used: nothing about n.

*Second inequality.* Lower index fixed at i ≥ 1; upper indices
2j ≤ n (from j ≤ n/2), with 2j ≥ i so C(2j, i) is in range. The
function m ↦ C(m, i) is nondecreasing, indeed strictly increasing,
in m ≥ i: one-step ratio (m + 1)/(m + 1 - i) > 1 since i ≥ 1
(Lemma 7(ii)). Hypotheses used: n ≥ 2j and i ≥ 1. Note that i ≥ 1 is
essential: for i = 0, C(m, 0) = 1 is constant and also the rest of the
argument has already collapsed (Section 1.4).

*Boundary j = 3i/2.* This forces i even, i = 2t, j = 3t (t ≥ 1), and
2(j - i) = 2t = i exactly. The first chain inequality is then an
equality. The contradiction is unaffected, because (⋆) is strict:
C(n, i) < C(2j, i) ≤ C(n, i) is already impossible. So the boundary
is not a near-miss; the strictness budget of the whole proof sits in
(⋆), which is funded by two independent strictnesses (u < v in
Lemma 2, and the extra Vandermonde terms in Lemma 5), either of which
alone would suffice for the final contradiction.

*Boundary n = 2j.* The second chain inequality is then an equality.
Same conclusion: C(n, i) < C(2j, 2(j-i)) ≤ C(2j, i) = C(n, i) is
impossible. Both boundaries simultaneously (n = 2j and j = 3i/2,
e.g. (n, i, j) = (12, 4, 6)) give equalities in both chain steps and
the strict (⋆) still yields the contradiction. There is no boundary
case in which the proof degenerates.

Classification: GAP (filled) for the unstated monotonicity
justifications; the chain is PROVED, boundaries included.

### (e) The finiteness remark

Bloom: the bound C(n, i) < C(2j, 2(j-i)) "immediately implies that
there are only finitely many possible bad n for fixed i < j".

Verdict: **correct, for a fixed pair (i, j)**, and the precise content
is Corollary 6.1. The reasoning the word "immediately" compresses:

1. The right side B = C(2j, 2(j-i)) is a constant once (i, j) is fixed.
2. For fixed i ≥ 1, C(n, i) is a strictly increasing, unbounded
   function of n (Lemma 7(ii) plus positive integer values; a crude
   explicit bound is C(n, i) ≥ n for 1 ≤ i ≤ n - 1). Hence
   {n : C(n, i) < B} is finite.
3. The derivation of the bound assumed (n, i) ∉ E. The n with
   (n, i) ∈ E form a finite set globally (twelve pairs), so adjoining
   them keeps the set of possibly bad n finite.

Two clarifications the exposition does not make, and which matter for
how the remark may be quoted downstream:

* Finiteness is **per pair (i, j)**, not uniform over any region. For
  fixed i and growing j, B grows and the finite interval of candidate
  n grows with it (Phase 0 computed, e.g., for (i, j) = (10, 1000) the
  interval reaches n = 260,190). The remark does not reduce the region
  j > 3i/2 to a finite check overall; it reduces each pair separately.
* The remark as printed inherits the L8 caveat: strictly, the displayed
  bound is derived only for non-exception n. Point 3 above is the
  repair, and it is cheap because E is finite and explicit.

Classification: GAP (filled). Correct as a per-pair statement.

### (f) The exception-pair logic

This is the one material incompleteness in the exposition, and I state
its exact extent.

**What EEES78 gives at an exception pair.** For (n0, i0) ∈ E, the
theorem's conclusion u < v is false; in fact u > v (Appendix A), so
v² < C(n0, i0). Lemma 2 is unavailable, in the worst possible
direction: the proof needs a lower bound on v, and at exceptions the
available information is an upper-type bound v² < C(n0, i0).

**What the rest of the argument gives at an exception pair, without
Lemma 2.** Lemmas 1, 3, 4, 5 do not use EEES78. So for any j with
i0 < j ≤ n0/2, the exposition's machinery does establish the
conditional statement: *if* gcd(v, C(n0, j)) = 1, *then*
v² ≤ C(j, j - i0)² < C(2j, 2(j - i0)). This is an upper bound on v.
There is nothing to contradict it with: at an exception pair we know
v² < C(n0, i0), and an upper bound on v² is perfectly compatible with
that. Formally, the proof of Theorem R at an exception pair would need
C(2j, 2(j-i0)) ≤ C(n0, i0) (true in the region, by Lemma 7) to clash
with C(n0, i0) < C(2j, 2(j-i0)) (Lemma 6), but Lemma 6's proof breaks
at its Lemma 2 step, so the clash never materialises.

**Conclusion for exception pairs.** The exposition alone establishes
**nothing** about Problem #699 at any triple (n0, i0, j) with
(n0, i0) ∈ E, in **either** region:

* In the region j ≤ 3i0/2: not proved by the exposition. (This is the
  consequential half of the gap, since the region is the exposition's
  stated subject.)
* In the region j > 3i0/2: also not proved by the exposition, which is
  unsurprising there (the exposition claims nothing about that region
  beyond the per-pair finiteness of Corollary 6.1, whose proof also
  routes the non-exception bound and the finiteness of E; for a fixed
  exception pair, "finitely many bad n" is vacuous anyway, since n is
  already fixed).

**The exact finite residue.** The pairs and their j ranges
(i0 < j ≤ n0/2) are:

| (n0, i0) | j values | in region j ≤ 3i0/2 | outside region | includes j = n0/2 |
|---|---|---|---|---|
| (8, 3) | 4 | 4 | (none) | yes |
| (9, 4) | (none) | (none) | (none) | no |
| (10, 5) | (none) | (none) | (none) | no |
| (12, 5) | 6 | 6 | (none) | yes |
| (21, 7) | 8, 9, 10 | 8, 9, 10 | (none) | no |
| (21, 8) | 9, 10 | 9, 10 | (none) | no |
| (30, 7) | 8 to 15 | 8, 9, 10 | 11 to 15 | yes (j = 15) |
| (33, 13) | 14, 15, 16 | 14, 15, 16 | (none) | no |
| (33, 14) | 15, 16 | 15, 16 | (none) | no |
| (36, 13) | 14 to 18 | 14 to 18 | (none) | yes (j = 18) |
| (36, 17) | 18 | 18 | (none) | yes |
| (56, 13) | 14 to 28 | 14 to 19 | 20 to 28 | yes (j = 28) |

Totals: 41 values of j across all exception pairs; 27 in the region,
14 outside it. Two pairs, (9, 4) and (10, 5), have no admissible j at
all and are discharged vacuously. Every other pair requires the direct
check gcd(V_{i0}(n0), C(n0, j)) > 1 for each listed j.

**Status of the discharge.** The exposition does not perform it (it
does not even list E). Externally, the discharge is complete and easy:
Phase 0 (Item 2 brute force to n ≤ 240, and Item 4's list) covers all
of it, and I independently recomputed all 41 gcd values by exact
integer arithmetic for this report: every one is > 1 (Appendix B).
So the gap is closed by material outside the exposition; within the
exposition it is a genuine, if small and fully understood, gap.

Classification: GAP (external), material for the standalone
exposition, closed for the campaign-level claim
"exposition + EEES78 + discharged exception list".

---

## 5. The role of the exception discharge in the complete claim

Section 4(f) contains the full exception-pair analysis, and
Appendices A and B contain the computations. The logical position,
stated once here for use in Sections 6 and 7, is the following.
Theorem R (Section 1.3) proves the region j ≤ 3i/2 for every triple
with (n, i) not in E. The direct computation in Appendix B verifies
the statement for every triple with (n, i) in E and i < j ≤ n/2
(41 values of j, all with gcd > 1; two pairs vacuous). The two pieces
are disjoint in their hypotheses and together exhaust the region.
That combination, and only that combination, is what the verdict in
Section 7 calls "fully proved". The exposition by itself supplies
the first piece only.

---

## 6. The n = 2j assertion

### 6.1 What the available texts say

The main problem page asserts that GPT 5.6 Sol (prompted by Price)
proved the statement "if j ≤ 3i/2 OR n = 2j". Bloom's exposition, the
only refereeable text, proves (modulo Section 4(f)) the first disjunct
only. It does not state the n = 2j case as a goal, does not mention it,
and contains no step that addresses it. The raw proof claim(s), which
might contain a separate n = 2j argument, are inaccessible
(HTTP 403, not indexed), and how the page's two proof claims divide
the two disjuncts cannot be confirmed from readable material.

**Classification of the n = 2j assertion as presented: UNVERIFIABLE.**
It is asserted on the page and not proved in any text available to the
referees. This is not a claim that the n = 2j statement is false; it
is a claim about the state of the presented evidence. Note also the
logical anatomy of the "OR": the genuinely new content of the second
disjunct, beyond Theorem R, is the set of triples with n = 2j **and**
j > 3i/2, since triples with n = 2j and j ≤ 3i/2 are already covered
by Theorem R (the boundary discussion in Section 4(d) includes
n = 2j). So the question is precisely whether the case
n = 2j, j > 3i/2 is proved. In the exposition, it is not.

### 6.2 The exposited method does not extend to n = 2j

I now show the failure is structural, not a matter of insufficient
cleverness with the final chain: at n = 2j with j > 3i/2, the size
inequality the method derives is *always true*, so it cannot yield a
contradiction.

The method's output, for a supposed counterexample with (n, i) ∉ E,
is Lemma 6: C(n, i) < C(2j, 2(j - i)). At n = 2j this reads
C(2j, i) < C(2j, 2(j - i)). (⋆⋆)
The final chain of Theorem R would need C(2j, 2(j-i)) ≤ C(2j, i) ≤
C(2j, i); the second inequality is an equality at n = 2j, so
everything rests on the first, which requires 2(j - i) ≤ i, i.e.
j ≤ 3i/2. When j > 3i/2 the first inequality does not merely lack a
proof; its reverse holds:

**Proposition (obstruction).** For all 1 ≤ i < j with j > 3i/2,
C(2j, 2(j - i)) > C(2j, i).

*Proof.* Let r = j - i and a = 2r. Note a > i iff j > 3i/2.
Case 1, a ≤ j: then i < a ≤ j, and strict monotonicity of C(2j, ·) on
[0, j] (Lemma 7(i)) gives C(2j, i) < C(2j, a).
Case 2, a > j: by symmetry C(2j, a) = C(2j, 2j - a) = C(2j, 2i).
Now a > j iff 2j - 2i > j iff j > 2i, so i < 2i < j, and strict
monotonicity on [0, j] gives C(2j, i) < C(2j, 2i) = C(2j, a).
(The boundary a = j falls in Case 1 and gives strict inequality since
i < a.) ∎

Hence (⋆⋆) holds automatically for every (i, j) with j > 3i/2, with
no reference to counterexamples, to EEES78, or to gcds. Concretely:

| (i, j) | n = 2j | C(n, i) | C(2j, 2(j-i)) | (⋆⋆) holds | Chain step C(2j, 2(j-i)) ≤ C(2j, i) |
|---|---|---|---|---|---|
| (1, 3) | 6 | 6 | C(6, 4) = 15 | yes | false |
| (2, 5) | 10 | 45 | C(10, 6) = 210 | yes | false |
| (5, 8) | 16 | 4368 | C(16, 6) = 8008 | yes | false |

These triples are not counterexamples to Problem #699 (direct
computation gives gcd(v, C(n, j)) equal to 2, 9, and 13 respectively,
all > 1). They are counterexamples to the *chain step* the method
would need, and the Proposition shows every (i, j) with j > 3i/2 is
such a counterexample. **The exact point of failure is the first
inequality of the final chain, C(2j, 2(j-i)) ≤ C(2j, i), whose
hypothesis 2(j-i) ≤ i is equivalent to j ≤ 3i/2.**

Therefore any proof of the n = 2j, j > 3i/2 case must use input beyond
the exposited method: the combination of (i) the divisibility
v | C(j, i), (ii) the EEES78 lower bound on v, and (iii) binomial size
comparisons is provably insufficient, because the sizes are in the
wrong order throughout that range. A proof would need, for example,
prime-by-prime information about v or about C(2j, j) that the
exposition never develops. Whether the inaccessible raw claim contains
such an argument is UNVERIFIABLE from available texts.

Two further remarks. First, the exception issue compounds here rather
than disappearing: six exception pairs have an admissible j equal to
n0/2 (namely (8, 3) with j = 4, (12, 5) with j = 6, (30, 7) with
j = 15, (36, 13) and (36, 17) with j = 18, and (56, 13) with j = 28),
so an n = 2j proof routed through Lemma 6 would additionally need the
exception discharge at those pairs; Appendix B supplies it, but that
repairs only the EEES78 step, not the size obstruction above. Second,
for any *fixed* pair (i, j), the single value n = 2j is of course
checkable directly, and computational campaigns check it as the left
endpoint of the interval [2j, N(i, j)]; that is a per-pair verification,
not a proof of the universal n = 2j assertion.

---

## 7. Verdict input

**Fully proved by the exposition + EEES78 (statement and list verified)
+ the discharged exception list:**

1. The equivalence of Problem #699 with the gcd formulation
   gcd(V_i(n), C(n, j)) > 1 (Lemma 1, including v = 1).
2. The reduction: for any (H1) triple with (n, i) ∉ E, a counterexample
   would satisfy C(n, i) < C(2j, 2(j - i)) (Lemma 6), with every step
   (identity, Euclid divisibility, strict Vandermonde, EEES78
   square-root bound) verified line by line.
3. Finiteness of the set of bad n for each fixed pair (i, j)
   (Corollary 6.1).
4. **The region j ≤ 3i/2, in full**: all integers 1 ≤ i < j ≤ n/2 with
   j ≤ 3i/2, all n, boundaries j = 3i/2 and n = 2j included
   (Theorem R for non-exception pairs; direct computation for the 41
   exception-pair j values, 27 of which lie in the region; two
   exception pairs vacuous). No case in this region is left open by
   the combination above.

**Proved by the exposition alone, without the external discharge:**
items 1 to 3 above, and Theorem R restricted to (n, i) ∉ E. The
exposition alone proves nothing at exception pairs, in either region
(Section 4(f)).

**Not proved by any available text:**

5. The region j > 3i/2 in general. What is available is only the
   per-pair finite reduction (item 3); clearing the region requires
   checking, for each pair separately, the finite interval of n, and
   the region contains infinitely many pairs.
6. The n = 2j assertion for j > 3i/2, as a universal statement. Status:
   asserted on the problem page; **UNVERIFIABLE** as presented (raw
   claim inaccessible; exposition silent); and the exposited method
   **provably cannot** supply it (Section 6.2, obstruction
   Proposition). (For j ≤ 3i/2, n = 2j is already inside item 4.)
7. The fidelity of Bloom's exposition to the raw GPT 5.6 Sol claim:
   UNVERIFIABLE (text inaccessible). This does not weaken items 1 to 4,
   which referee the exposition as a self-contained argument.

**Errors found:** none in the mathematical content of the exposition.
**Gaps found:** one material gap (undischarged EEES78 exceptions,
externally closed), and three presentational gaps (equivalence,
Vandermonde strictness, monotonicities), all filled in this report.

**Overall classification (Referee 1):** The Bloom exposition is a
**sound and, after the standard exception discharge, complete proof
of Problem #699 for the region j ≤ 3i/2, conditional on the published
theorem EEES78**. The page's additional "or n = 2j" claim is
**not established by the available texts**.

---

## Appendix A. The twelve EEES78 exception pairs, recomputed

For each (n, k) in E, exact computation (prime exponents in C(n, k) by
Legendre's formula, split at p < k versus p ≥ k) gives u and v with
u · v = C(n, k) and u > v in every case, confirming that the exceptions
are exactly the pairs where Lemma 2's conclusion fails, and fails in
the direction v² < C(n, k):

| (n, k) | u | v | C(n, k) |
|---|---|---|---|
| (8, 3) | 8 | 7 | 56 |
| (9, 4) | 18 | 7 | 126 |
| (10, 5) | 36 | 7 | 252 |
| (12, 5) | 72 | 11 | 792 |
| (21, 7) | 360 | 323 | 116,280 |
| (21, 8) | 630 | 323 | 203,490 |
| (30, 7) | 5,400 | 377 | 2,035,800 |
| (33, 13) | 27,720 | 20,677 | 573,166,440 |
| (33, 14) | 39,600 | 20,677 | 818,809,200 |
| (36, 13) | 151,200 | 15,283 | 2,310,789,600 |
| (36, 17) | 415,800 | 20,677 | 8,597,496,600 |
| (56, 13) | 1,940,400 | 973,981 | 1,889,912,732,400 |

This agrees with Phase 0, Item 4 (list recovered from the paper,
pp. 258-259, corroborated by Erdős's 1979 restatement and by two
independent enumerations) and Phase 0, Item 2, test D (the same twelve
pairs, and no others, fail v² > C(n, i) for n ≤ 240).

## Appendix B. Direct discharge of the exception pairs (referee's recomputation)

For each (n0, i0) ∈ E and each admissible j, I computed
g = gcd(V_{i0}(n0), C(n0, j)) by exact integer arithmetic. All 41
values exceed 1, so no exception pair yields a counterexample, in
either region. Summary (j ranges as in Section 4(f)):

* (8, 3): j = 4: g = 7.
* (9, 4): no admissible j (vacuous).
* (10, 5): no admissible j (vacuous).
* (12, 5): j = 6: g = 11.
* (21, 7): j = 8, 9, 10: g = 323 each.
* (21, 8): j = 9, 10: g = 323 each.
* (30, 7): j = 8 to 12: g = 377 each; j = 13, 14, 15: g = 29 each.
* (33, 13): j = 14, 15, 16: g = 20,677 each.
* (33, 14): j = 15, 16: g = 20,677 each.
* (36, 13): j = 14, 15, 16: g = 15,283 each; j = 17, 18: g = 899 each.
* (36, 17): j = 18: g = 20,677.
* (56, 13): j = 14, 15, 16: g = 973,981 each; j = 17 to 22:
  g = 57,293 each; j = 23 to 28: g = 42,347 each.

## Appendix C. Referee's independent spot computations

Performed by exact integer arithmetic during this review, in addition
to the targeted checks embedded in the text above:

* Vandermonde strict inequality C(j, j-i)² < C(2j, 2(j-i)) verified
  for all 1 ≤ i < j ≤ 600, no failures.
* The obstruction Proposition of Section 6.2 verified numerically for
  all 1 ≤ i < j ≤ 300 with j > 3i/2: C(2j, 2(j-i)) > C(2j, i) in every
  case, no exceptions.
* Exception tables of Appendix A and gcd table of Appendix B computed
  in full (not sampled).

*End of Referee 1 report.*
