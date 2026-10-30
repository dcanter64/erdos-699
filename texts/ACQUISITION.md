# Workstream A — text acquisition record (2026-10-28, campaign coordinator)

## Obtained

1. **Bloom's exposition of the proof (FULL verbatim text).**
   https://www.erdosproblems.com/699, fetched 2026-10-28 via text fetch
   (page crawl dated 2026-10-28 13:52 UTC). Saved verbatim as
   texts/bloom_exposition_699.md. Written by Thomas Bloom, last edited
   27 Aug 2026. It states it is "an exposition of a proof of the
   conjecture when j ≤ 3i/2, provided by GPT 5.6 Sol (prompted by
   Liam Price) in a proof claim." The text is short and self-contained:
   equivalence reformulation, EEES78 input, key divisibility lemma,
   Vandermonde step, finiteness remark, and the j ≤ 3i/2 contradiction.
   It ends with the contradiction (appears complete as an exposition).

2. **Main problem page (statement and discussion).** Via the site's own
   rendered entry (Phase 0 Item 1, 2026-10-28) and today's search-index
   copy of the same page. Statement verbatim (TeX): "Is it true that
   for every 1 ≤ i < j ≤ n/2 there exists some prime p ≥ i such that
   p | gcd(C(n,i), C(n,j))?" Page metadata confirmed today: Comments
   (9), Proof claims (2), Proof expositions (1); page last edited
   19 July 2026; exposition last edited 27 Aug 2026. The page's main
   text asserts GPT 5.6 (prompted by Price) proved the statement "if
   j ≤ 3i/2 OR n = 2j". The page also records counterexamples to the
   STRENGTHENED variant (p > i in place of p ≥ i), e.g. gcd(C(28,5),
   C(28,14)) = 2^3·3^3·5; those are not counterexamples to #699.

3. **EEES78 source material.** Ecklund–Eggleton–Erdős–Selfridge,
   J. Austral. Math. Soc. A 26(3) (1978) 257–269. Abstract verbatim
   (Phase 0 Item 4): "For positive integers n and k, with n ≥ 2k, let
   C(n,k) = uv, where each prime factor of u is less than k, and each
   prime factor of v is at least equal to k. It is shown that u < v
   holds with just 12 exceptions, which are determined." The 12
   exception pairs (n,k): (8,3), (9,4), (10,5), (12,5), (21,7),
   (21,8), (30,7), (33,13), (33,14), (36,13), (36,17), (56,13) —
   recovered from the paper scan (pp. 258–259), corroborated by
   Erdős's 1979 restatement and by two independent computations
   (Phase 0 Item 2 test D to n ≤ 240; a second enumeration to
   n ≤ 400). The same paper's OTHER convention (u on primes ≤ k,
   v on primes > k) has 19 cases and only finiteness proved; it is
   NOT the input to #699.

## Inaccessible (a finding in itself)

4. **The raw GPT 5.6 Sol proof-claim text (both proof claims).**
   The claims live in the site's forum (thread route). Fetching
   https://www.erdosproblems.com/forum/thread/699 returns HTTP 403 to
   automated access (confirmed again today, 2026-10-28; same result
   as Phase 0). The claim bodies are not search-indexed. A Wayback
   Machine route for the problem page also returned 403 through the
   available fetcher. No mirror, PDF, or alternate full text of the
   raw claim was located anywhere (web searches, including the
   teorth/erdosproblems GitHub metadata repo, which carries status
   only: state "falsifiable", formalised "yes"). In particular, NO
   ulam.ai PDF is linked for #699 (that was a #488 artifact).

5. **The 9 comment bodies.** Same 403 barrier; contents uninspected.
   One of the two proof claims presumably underlies the j ≤ 3i/2
   exposition; the other plausibly underlies the page's asserted
   n = 2j case, which the exposition does NOT prove. How the two
   claims divide coverage cannot be confirmed from readable material.

## Consequence for the refereeing

The fullest refereeable text of the claimed proof is Bloom's
exposition (item 1). It is Bloom's own mini-exposition of the GPT
claim. The referees therefore referee the argument AS EXPOSITED,
line by line, and separately classify the status of (a) the raw
claim (UNVERIFIABLE — text inaccessible), and (b) the page's n = 2j
assertion (asserted on the page, not proved in the exposition).
