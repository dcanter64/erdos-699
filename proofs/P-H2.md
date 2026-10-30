# P-H2 — Cycle 2, Prover H2: A Counting Bound on Simultaneous Badness in R1

**Campaign:** Erdős #699. **Agent:** H2 (independent; S10 and
EXTERNAL_CLAIMS_2026-10-29 read in full; P-H1 not read).
**Target:** the T1 size lever of S10 §8 in regime
**R1: `3i/2 < j < 2i`**, `d = j − i`, and a counting bound on
simultaneous bad configurations there.
**Headline result:** the T1 chain as stated in S10 closes exactly
Del Pin's J1 range (Claim 4), but the chain wastes a large factor:
in R1 every bad prime satisfies `v_p(C(j,i)) = 1`, so the key lemma
gives not merely `V ≤ C(j,i)` but `V | Q(i,j) := ∏_{i<p≤j} p`
(Claim 3). The sharpened criterion `Q(i,j)^2 ≤ C(2j,i)` closes
every R1 pair with `i ≤ 2000` except `(4,7)` and `(10,19)` (exact
computation, Claim 8), and closes all sufficiently large `i`
(ineffective threshold, via PNT + Stirling, Claim 9). At `(4,7)`
and `(10,19)` the barrier is sharp and exhibited by a single
integer each: `V0 = 35` and `V0 = 46189` satisfy *every* size and
divisibility constraint either lever uses (Claim 11). **R1 is not
claimed closed**: the two named pairs, and the ineffectivity of
the large-`i` threshold, remain (Claims 9, 15).

**Standing hypotheses throughout:** `(n,i,j)` a counterexample
means `1 ≤ i < j ≤ n/2`, every `p ∈ S(n,i)` bad, `(n,i)` not one
of the 12 EEES78 exception pairs, so `V := V_i(n)` satisfies
`V^2 > C(n,i)` (EEES78). In R1, S10 §5 gives the exact
characterisation used below: a counterexample has
`S(n,i) ⊆ [i,j]`, `e_p = 1` for every `p ∈ S(n,i)`, and
`(n−i) mod p ∈ [d, p−1]` for every `p ∈ S(n,i)`; and Theorem 3(b)
of S10 gives `e_i = 0` if `i` is prime.

---

## Task 1 — The T1 size lever, exactly

### Claim 1 (PROVED): the shape of `V` in an R1 counterexample

In R1, a counterexample has `V = ∏_{p ∈ S(n,i)} p`, a squarefree
product of distinct primes, each lying in `(i, j]` (note: `i`
itself is excluded), and `V | C(j, j−i) = C(j,i)` by the key lemma.

*Proof.* `e_p = 1` for all `p ∈ S(n,i)` (S10 §5), so
`V = ∏ p^{e_p} = ∏ p`. If `i` is prime, `e_i = 0` (S10 Thm 3(b)),
so `i ∉ S(n,i)`; if `i` is composite, `i ∉ S(n,i)` trivially.
Hence every prime factor of `V` lies in `(i, j]`. The key lemma
applied to `d = V` (which divides `C(n,i)` and is coprime to
`C(n,j)`) gives `V | C(j, j−i)`, and `C(j, j−i) = C(j,i)`. ∎

### Claim 2 (PROVED): `v_p(C(j,i)) = 1` on the whole support; the two exponent caps coincide

For every prime `p ∈ (i, j]` in R1, `v_p(C(j,i)) = 1`. Consequently
the key-lemma cap of S10 §7(a), `e_p ≤ v_p(C(j, j−i))`, is the
number `1` for every prime that can divide `V` — *identical* to the
window cap forced by Theorem 3(b) of S10. There is no slack and no
gain in the exponent caps themselves.

*Proof.* In R1, `p > i > j/2`, so `p ∈ (j/2, j]`. Then
`v_p(j!) = 1` (only the multiple `p` itself, since `2p > j`),
`v_p(i!) = 0` (as `i < p`), so `B_p = v_p(j!) − v_p(i!) = 1`.
Also `p > i > d`, so `v_p(d!) = 0`. Hence
`v_p(C(j,i)) = v_p(j!) − v_p(i!) − v_p(d!) = B_p − v_p(d!) = 1`.
(Consistency check at the excluded endpoint: if `i` is prime,
`v_i(C(j,i)) = 1 − 1 − 0 = 0`, matching `e_i = 0`.) ∎

### Claim 3 (PROVED): the real slack — `V | Q(i,j)`, not just `V ≤ C(j,i)`

Let `Q(i,j) := ∏_{i < p ≤ j, p prime} p`. In an R1 counterexample,
`V | Q(i,j)`, hence `V ≤ Q(i,j)`.

*Proof.* By Claim 1, `V` is squarefree, supported on primes in
`(i, j]`, and `V | C(j,i)`. By Claim 2 each such prime occurs in
`C(j,i)` to exactly the first power. A squarefree integer all of
whose prime factors lie in a set `T` divides `∏_{p ∈ T} p`; apply
with `T = {primes in (i, j]}`. ∎

The T1 chain in S10 §8 uses only `V ≤ C(j,i)`. The wasted factor
is `C(j,i)/Q(i,j)`, which is large: at `(i,j) = (39,59)` it is
exactly `10,785,390` (Claim 5). This divisibility sharpening —
not the exponent cap — is where the lever had slack.

### Claim 4 (PROVED): the unsharpened T1 chain closes exactly Del Pin's J1 range

The chain `C(2j,i) ≤ C(n,i) < V^2 ≤ C(j,i)^2` yields a
contradiction **if and only if** `C(2j,i) ≥ C(j,i)^2`. Hence it
closes precisely the pairs `(i,j)` with `j ≤ J1(i)`, where
`J1(i)` is the largest `j` with `C(2j,i) ≥ C(j,i)^2` (Del Pin's
range; `F(j) = C(2j,i)/C(j,i)^2` is strictly decreasing in `j`,
verified in EXTERNAL_CLAIMS_2026-10-29).

*Proof.* If `C(2j,i) ≥ C(j,i)^2`, the chain gives
`C(j,i)^2 ≤ C(2j,i) ≤ C(n,i) < V^2 ≤ C(j,i)^2`, impossible.
Conversely, if `C(2j,i) < C(j,i)^2`, the integer `V0 = C(j,i)`
satisfies every inequality the chain uses:
`V0^2 = C(j,i)^2 > C(2j,i)` and `V0 ≤ C(j,i)`. So the chain, as a
system of pure size inequalities, has a model and cannot by itself
exclude any pair beyond J1. (That the boundary is genuinely
crossed inside R1: `J1(3) = 5`, `J1(5) = 8`, `J1(39) = 59`,
`J1(640) = 962`, `J1(5000) = 7503`, per EXTERNAL_CLAIMS and
Claim 5.) ∎

### Claim 5 (PROVED, exact integer computation): the `(39,59)` numerics — and a correction

For `(i,j) = (39,59)`, `d = 20`, at `n = 119 = N(39,59)` the five
bad primes of S10 Example A are `41, 43, 47, 53, 59`, and:

- `P := ∏_{p bad} p = 41·43·47·53·59 = 259,106,347`;
  `P^2 = 67,136,099,055,684,409`.
- `C(59,39) = 2,794,563,003,870,330`, and `P | C(59,39)` with
  quotient exactly `10,785,390` (this is the Claim 3 divisibility,
  with `Q(39,59) = P`).
- `C(118,39) = 25,671,002,407,835,331,258,960,180,816,240`, and
  `C(118,39) / C(59,39)^2 = 3.2871158981… > 1`.
- `C(119,39) = 38,185,616,081,655,055,247,703,268,964,157`.
- The full `V_39(119) = 2,545,453,702,497,494,433,235,781`
  (13 primes, each to the first power), the extra 8 primes
  `83, 89, 97, 101, 103, 107, 109, 113` being `> j`, as in S10.

Consequences. (a) Since `C(2j,i) ≥ C(j,i)^2` holds at `(39,59)`,
this pair lies **inside** Del Pin's range: direct check gives
`C(2j,39) ≥ C(j,39)^2` at `j = 59` and failure at `j = 60`
(ratio `0.8873691112…`), and a brute-force check over
`40 ≤ j ≤ 500` confirms the holding set is exactly `40..59`;
with `F` strictly decreasing, `J1(39) = 59`. So `(39,59)` does
**not** exhibit a barrier for the T1 lever — the task's premise
on this point is corrected: the lever *does* close `(39,59)`.
(b) What the numerics do show is *why* the simultaneously bad
configuration at `n = 119` is not a counterexample, in size
terms: its in-range product `P` undershoots the EEES78 threshold
by a factor `C(118,39)/P^2 = 382,372,565,116,468 ≈ 3.8 × 10^14`
in squares (`⌊√C(118,39)⌋ / P ≈ 19,554,349`). The in-range primes
alone come nowhere near `V^2 > C(n,i)`; the rescue primes `> j`
supply the missing factor, exactly as S10 §6 describes.
(c) On the task's requested `C(238,39)`: `238 = 2n`, not `2j`;
no step of the chain involves it (the pair-level threshold is
`C(2j,i) = C(118,39)`, the `n`-level threshold is `C(119,39)`).
For the record, `C(238,39) =
881,689,851,124,977,590,640,300,656,276,855,178,603,818,200`,
with `⌊√C(238,39)⌋ = 29,693,262,722,795,849,580,394`; `P` is
below this too, but the comparison has no role in the lever.

### Claim 6 (PROVED): barrier for the unsharpened chain, one step past J1(39)

At `(i,j) = (39,60)`: `C(120,39)/C(60,39)^2 = 0.8873691112… < 1`,
so by Claim 4 the unsharpened chain cannot close `(39,60)`. The
sharpened Claim 3 bound still closes it, and `(39,61)` too:
`Q(39,60) = 259,106,347`, `Q^2 ≈ 6.7 × 10^16 < C(120,39) =
56,571,283,083,933,415,181,782,620,687,640`;
`Q(39,61) = 15,805,487,167`, `Q(39,61)^2 =
249,813,424,586,201,685,889 < C(122,39) =
122,701,334,246,991,636,043,707,764,706,280`.
(S10's `(122,39,61)`, with bad primes `43, 47, 53, 59, 61`
re-verified here by Legendre exponents, lies in its reduction
interval: `N(39,61) = 130 ≥ 122`. Simultaneous badness at a pair
the size lever closes is possible because badness of
`S(n,i) ∩ [i,j]` is not the counterexample condition — see
Claim 10.)

---

## Task 2 — Second lever: the counting bound (option (b)), with the CRT comparison (option (a)) on `(39,59)`

### Claim 7 (PROVED): the sharpened size criterion

If `Q(i,j)^2 ≤ C(2j,i)`, then `(i,j)` admits no counterexample
with `n ≥ 2j` and `(n,i)` not an EEES78 exception pair.

*Proof.* A counterexample would give, by Claims 1–3 and EEES78
and monotonicity of `C(n,i)` in `n` (`n ≥ 2j` since `j ≤ n/2`):
`C(2j,i) ≤ C(n,i) < V^2 ≤ Q(i,j)^2 ≤ C(2j,i)`, impossible. ∎

### Claim 8 (PROVED, exact computation): scope of the sharpened criterion, `i ≤ 2000`

Exact integer comparison of `Q(i,j)^2` against `C(2j,i)` over all
`999,000` R1 pairs with `3 ≤ i ≤ 2000` (Python stdlib
`math.comb`, `Q` built incrementally prime by prime; runtime
≈ 1093 s, single-threaded): the criterion **fails at exactly two
pairs**,
`(4,7)` (`Q = 35`, `Q^2 = 1225 > 1001 = C(14,4)`) and
`(10,19)` (`Q = 46189`, `Q^2 = 2,133,423,721 > 472,733,756 =
C(38,10)`), and holds at the other `998,998`. Among these
pairs, Del Pin's unsharpened condition fails but the sharpened
criterion closes the pair in `994,623` cases. An independent
floating-point margin scan (`lgamma` for `log C(2j,i)`, prefix
sums for `θ`) over the same range agrees: exactly two
non-positive margins, at `(10,19)` (`−0.753` nats) and `(4,7)`
(`−0.101` nats); the smallest positive margins are at `(57,113)`
(`+0.279`) and `(12,23)` (`+0.714`).

### Claim 9 (PROVED for large `i`, ineffective threshold; GAP: effectivity)

There exists `I0` such that for all `i ≥ I0`, every R1 pair
`(i,j)` satisfies `Q(i,j)^2 < C(2j,i)`, hence is closed by
Claim 7. The threshold `I0` supplied by this argument is
ineffective; making it effective is a GAP.

*Proof.* Write `j = ti`, `t ∈ [3/2, 2]`. Then
`log Q(i,j) = θ(j) − θ(i) = (j − i) + o(i)` uniformly in `t`, by
the Prime Number Theorem (`θ(x) = x + o(x)`). By Stirling's
formula, uniformly for `t` in the compact interval `[3/2, 2]`
(the ratio `i/(2j) = 1/(2t) ∈ [1/4, 1/3]` stays away from `0,1`),
`(1/i) log C(2j,i) → 2t·h(1/(2t))`, where
`h(u) = −u ln u − (1−u) ln(1−u)`. Hence
`(1/i)[ (1/2) log C(2j,i) − log Q(i,j) ] → f(t) :=
t·h(1/(2t)) − (t−1)` uniformly. Now
`f'(t) = ln(2t/(2t−1)) − 1 < 0` on `[3/2, 2]` (since
`2t/(2t−1) ≤ 3/2 < e`): indeed, with `g(t) = t·h(1/(2t))`,
`g'(t) = −ln(1 − 1/(2t))`. So `f` is decreasing and
`f(t) ≥ f(2) = 2h(1/4) − 1 = 0.1246702892… > 0.12`. For large
`i` the bracket is therefore `≥ 0.12 i − o(i) > 0`. The `o(i)`
comes from PNT and carries no explicit rate in this argument,
so `I0` is not computed: **GAP** (effectivity). ∎

### Claim 10 (PROVED): the counting sandwich on `B = |S(n,i)|`

In an R1 counterexample, with `B := |S(n,i)|` (every member bad),

```
ln C(2j,i) / (2 ln j)   <   B   ≤   min( π(j) − π(i),  ln Q(i,j) / ln i ).
```

*Proof.* Lower: `V ≤ j^B` (each of the `B` primes is `≤ j`), and
`V^2 > C(n,i) ≥ C(2j,i)`, so `2B ln j > ln C(2j,i)`. Upper:
`B ≤ π(j) − π(i)` since `S(n,i)` consists of distinct primes in
`(i, j]` (Claim 1); and `V = ∏_{p∈S} p ≥ ` (product of `B`
distinct primes each `> i`) gives `V > i^B` — in fact
`ln V ≥ B ln i` suffices — while `V ≤ Q(i,j)` (Claim 3), so
`B ≤ ln Q / ln i`. ∎

Numerical content (all bounds evaluated exactly from the
integers above; decimals rounded):

| pair | lower bound: `B >` | upper: `π(j)−π(i)` | upper: `ln Q/ln i` | verdict |
|---|---|---|---|---|
| (39,59) | 8.8685 → `B ≥ 9` | 5 | 5.2880 → `B ≤ 5` | impossible: closed |
| (39,61) | 8.9868 → `B ≥ 9` | 6 | 6.4101 → `B ≤ 6` | impossible: closed |
| (59,113) | 13.4274 → `B ≥ 14` | 13 | 14.2394 → `B ≤ 14` | impossible via count: closed |
| (4,7) | 1.7752 → `B ≥ 2` | 2 | 2.5646 → `B ≤ 2` | `B = 2`, `V = 35` forced, not excluded |
| (10,19) | 3.3918 → `B ≥ 4` | 4 | 4.6645 → `B ≤ 4` | `B = 4`, `V = 46189` forced, not excluded |

Comparison with the unsharpened count: using only `V ≤ C(j,i)`
gives `B ≤ ln C(j,i)/ln i`; at `(39,59)` that is `9.71`, i.e.
`B ≤ 9`, which against `B ≥ 9` leaves `B = 9` open — the
unsharpened counting bound does **not** close `(39,59)`, the
sharpened one does. Comparison with measurement: S10 found, and
Claim 13 re-finds, a maximum of **5** simultaneously bad primes
inside reduction intervals (`i < 40`). There is no tension with
the lower bounds in the table: those bounds constrain a
counterexample's *full* `S(n,i)` under the hypothesis
`S(n,i) ⊆ [i,j]`; the measured configurations have `S(n,i)`
extending above `j` (e.g. 13 primes at `(119,39,59)`, 5 of them
in range), which is precisely how they evade the count.

### Claim 11 (PROVED): the barrier is sharp — two integers satisfy every size constraint

At `(4,7)`, `V0 = 35`: squarefree, supported on primes in
`(4,7]`, `V0 | C(7,4) = 35` (quotient 1), `V0 = Q(4,7)`, and
`V0^2 = 1225 > 1001 = C(14,4)`. At `(10,19)`, `V0 = 46189`:
squarefree, supported on primes in `(10,19]`,
`V0 | C(19,10) = 92378` (quotient 2), `V0 = Q(10,19)`, and
`V0^2 = 2,133,423,721 > 472,733,756 = C(38,10)`. Hence **no
argument using only** squarefreeness, support in `(i,j]`,
`V | C(j,i)`, `V ≤ Q(i,j)`, and `V^2 > C(2j,i)` can exclude a
counterexample at these two pairs: the hypothetical `V` values
above satisfy all of them simultaneously. Any closure of
`(4,7)` or `(10,19)` for all `n` must use information about `n`
(residues, prime gaps, or label data), not sizes. (Both pairs are
of course inside the verified sweep range for the `n` that can
occur: `N(4,7) = 17`, `N(10,19) = 55`.)

### Claim 12 (PROVED as a limitation statement): what CRT/density can and cannot do at `(39,59)`

For fixed `(i,j) = (39,59)`, badness at `p` is the condition
`(n−i) mod p ∈ [20, p−1]`, of density `(p−20)/p` in `n`. For the
five primes of Claim 5 the combined density is
`∏ (p−20)/p = (21/41)(23/43)(27/47)(33/53)(39/59) =
0.0647755919…`, and the CRT period is the modulus
`M = 41·43·47·53·59 = 259,106,347`. The reduction interval is
`[2j, N] = [118, 119]`, of length 2. Precisely:

- **Cannot:** a density or CRT-period argument cannot exclude a
  solution in `[118, 119]`: the expected number of hits in the
  interval is `≈ 2 × 0.0648 ≈ 0.13 < 1`, yet `n = 119` *is* a
  hit, so the heuristic is consistent with both existence and
  non-existence; and CRT spacing `M ≈ 2.6 × 10^8` dwarfs the
  interval length 2, so no covering/pigeonhole contradiction is
  available. Density arguments bound *frequencies over long
  ranges of `n`*; the reduction interval for fixed `(i,j)` is
  short and `S(n,i)` itself varies with `n`, so no density
  statement about fixed prime sets applies directly to the
  existence question in `[2j, N(i,j)]`.
- **Can:** CRT explains the *abundance* S10 measured: for each
  fixed set of in-range primes, the simultaneous-badness
  conditions are a positive-density periodic system in `n`, so
  simultaneous badness recurs indefinitely often as `n` grows
  (cf. Example B of S10 at `n = 4871`, outside its interval).
  This is a proof that in-range badness alone can never yield a
  contradiction for large `n` — the obstruction must come from
  the primes above `j`, i.e. from `S(n,i) ⊆ [i,j]` failing.

---

## Task 3 — Combined-cap recount (exact computation)

### Claim 13 (PROVED as computation): the combined cap kills none of the 377

Reproduction of S10's search, in S10's appendix style (Legendre
exponents `v_p` via factorial valuations; `math.comb` for
`N(i,j)`; Python stdlib only; 361 R1 pairs with `i < 40`,
10,317 triples `n ∈ [2j, N(i,j)]` examined; runtime < 1 s):

- Window-badness alone (`Δ_p ≥ e_p` for every
  `p ∈ S(n,i) ∩ [i,j]`, with `|S(n,i) ∩ [i,j]| ≥ 3`): **377
  triples**, maximum simultaneous bad count **5** — exactly
  S10's numbers, independently reproduced.
- Combined condition (window-badness **and** the key-lemma cap
  `e_p ≤ v_p(C(j, j−i))` for every such `p`): **377 triples**,
  maximum simultaneous bad count **5**.
- **Triples killed by adding the cap: 0.**

### Claim 14 (PROVED): the recount outcome is forced — in R1 the combined condition is identical to the window condition

For every R1 triple (counted or not), every
`p ∈ S(n,i) ∩ [i,j]` satisfies the key-lemma cap iff the
window analysis permits it to be bad at all; precisely: for
`p > i`, `v_p(C(j, j−i)) = 1` (Claim 2), and window-badness
forces `e_p = 1` (S10 Thm 3(b)), so every window-bad prime
automatically meets the cap with equality; for `p = i` prime,
the cap is `e_i ≤ v_i(C(j, j−i)) = 0`, and window-badness is
already impossible (`Δ_i ≤ 0`), with `e_i ≥ 1` violating both
conditions simultaneously. Hence the two counted sets coincide
for structural reasons, not by numerical accident: in R1 the
combined cap `e_p ≤ min(Δ_p, B_p − v_p(d!))` of S10 §7(a)
collapses to the window condition, because `B_p − v_p(d!) = 1`
throughout the support. (Outside R1 this collapse fails — in
R3's lower band the two caps are genuinely incomparable, as
S10 §7(a) notes — but that is beyond this task's scope.)

---

## Task 4 — Final statement

### Claim 15 (the strongest counting bound proved here; boundary; what is missing)

**Strongest bound (PROVED).** In R1, a counterexample (with
`(n,i)` not an EEES78 exception) must satisfy all of:
`V = ∏_{p∈S} p` squarefree with `S ⊆ (i, j]`;
`V | Q(i,j)`; `V^2 > C(2j,i)`; and the counting sandwich of
Claim 10. Consequently every R1 pair with
`Q(i,j)^2 ≤ C(2j,i)` is closed for all `n ≥ 2j` — verified
exactly for all `i ≤ 2000`, where the only exceptions are
`(4,7)` and `(10,19)` — and every R1 pair with `i ≥ I0` is
closed for an ineffective constant `I0` (PNT + Stirling,
margin `f(t) ≥ 0.12467`).

**Exact boundary of size arguments (PROVED).** The unsharpened
T1 chain caps out exactly at Del Pin's `J1(i)` (Claim 4). The
sharpened size/divisibility levers of this file cap out exactly
where `Q(i,j)^2 > C(2j,i)`; the smallest such pairs are
`(4,7)` and `(10,19)`, and there the cap-out is not a failure
of technique but a theorem: the integers `35` and `46189`
satisfy every size constraint in play (Claim 11). Between the
computed range (`i ≤ 2000`) and the ineffective threshold `I0`
lies a **GAP**: closing it needs either an effective
`θ(j) − θ(i)` estimate strong enough to beat the entropy margin
uniformly, or a larger exact computation. **OPEN** within this
method: `(4,7)` and `(10,19)` for all `n`.

**What a completion needs (non-size input).** At the boundary
pairs the counting forces a *unique* candidate `V` (`35`,
`46189`) with a forced prime set (`B = 2`, `B = 4`
respectively). Excluding them requires using `n`: e.g. the
residue system `(n−i) mod p ∈ [d, p−1]` for the forced primes
*together with* the requirement `S(n,i) ⊆ [i,j]` and the
prime-free interval condition of S10 Thm S10 item 5, or the
label-retaining data (which of the window elements supplies
each prime) whose necessity Van Doorn–Rocca diagnose for
`i = 3` in EXTERNAL_CLAIMS. Size alone, in any of the forms
above, provably does not suffice.

**Not claimed.** #699 is not proved; R1 is not proved in full.
Nothing here touches R2 or R3, the EEES78 exception pairs
(handled by the established discharge), or `n < 2j` (excluded by
`j ≤ n/2`).

---

## Appendix — computational record (Python stdlib only, exact arithmetic)

All computations in this file use only `math.comb`, `math.prod`,
`math.isqrt`, and Legendre factorial valuations
`v_p(m!) = Σ_{k≥1} ⌊m/p^k⌋`, in the style of S10's appendix.

1. **Recount (Claim 13).** For each R1 pair `i < 40`
(`3i/2 < j < 2i`; 361 pairs), `N(i,j)` = largest `n` with
   `C(n,i) < C(2j, 2(j−i))`; for each `n ∈ [2j, N(i,j)]`
   (10,317 triples), each prime `p ∈ [i,j]` with
   `e_p = v_p(C(n,i)) ≥ 1`: bad iff
   `B_p − A_p ≥ e_p` with `A_p = v_p((n−i)!) − v_p((n−j)!)`,
   `B_p = v_p(j!) − v_p(i!)`; cap value `v_p(C(j, j−i))` by the
   same valuations. Counts: window 377 (max 5), combined 377
   (max 5), killed 0. First window examples:
   `(60,11,21)`, `(61,11,21)`, `(61,12,22)` (bad primes
   `13, 17, 19`).
2. **Q-scan (Claim 8).** For `3 ≤ i ≤ 2000`, `j` increasing over
   R1, `Q` updated by multiplying by `j` when `j` is prime and
   `> i`; exact test `Q^2 ≤ C(2j,i)` via `math.comb`.
   999,000 pairs (runtime ≈ 1093 s), failures exactly `(4,7)`,
   `(10,19)`; 994,623 pairs with Del Pin failing and Q
   closing. Independent float margin scan over the same range
   (prefix-`θ` + `lgamma`): exactly two non-positive margins,
   in agreement.
3. **Pair numerics (Claims 5, 6, 10, 11).** All binomial values,
   products, quotients, and square comparisons computed as exact
   integers (`P^2` vs `C(118,39)` compared as integers, not via
   floating square roots; `⌊√·⌋` via `math.isqrt`).
   `J1(39) = 59` additionally brute-forced for `j ≤ 500`
   (holding set exactly `40..59`), consistent with the verified
   strict decrease of `F(j)`.
4. **Re-verifications.** `(122,39,61)`: `S ∩ [39,61] =
   {43, 47, 53, 59, 61}`, all bad, `N(39,61) = 130`.
   `N(4,7) = 17`, `N(10,19) = 55`, `N(39,59) = 119`.

*End of P-H2.*
