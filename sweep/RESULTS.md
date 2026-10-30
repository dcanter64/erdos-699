# Erdős Problem #699, Stage 2 Results

Date: 2026-10-28. Gate: Phase 0 verdict PASS (see PHASE0.md). Stage 2 ran
only after the gate was written.

## Bottom line

No counterexample exists among all 27,769,446,111 open-region triples
(n, i, j) with n ≤ 10000, 1 ≤ i < j ≤ n/2, and j > 3i/2: the sweep found
zero triples with gcd(V_i(n), C(n, j)) = 1. Combined with the finite
reduction of Phase 0, this settles the conjecture for all n for 768,741
explicitly enumerated (i, j) pairs in the open region (list in
pairpass.json, summarized in the appendix). The problem as a whole is
NOT solved: the open region is infinite pair by pair, and pairs beyond
the scope below remain partially covered or untouched. Exact scope
follows; nothing outside it is claimed.

## Method in brief

- Reduction (Phase 0, derived and numerically verified there): if
  (n, i) is not one of the 12 EEES78 exception pairs and
  gcd(V_i(n), C(n, j)) = 1, then n ≤ N(i, j), where N(i, j) is the
  largest n with C(n, i) < C(2j, 2(j-i)). So a pair (i, j) is settled
  for all n once every n in [2j, N(i, j)] is checked directly, plus the
  EEES78 exception values of n for that i are checked directly.
- Sweep (sweep.py): for each n, prime-support bitmasks of C(n, k) for
  k ≤ n/2 built incrementally via an spf sieve; a triple fails iff
  (support of C(n, i) restricted to primes ≥ i) AND support of C(n, j)
  is empty. Any flagged triple would have been re-verified by direct
  gcd before being recorded; none was flagged.
- Pre-production validation (validate.py): the bitmask verdicts were
  compared against direct gcd (Legendre exponents) on all 568,820
  triples with n ≤ 240 in both regions: 0 mismatches.

## Coverage, stated in the two exact currencies

Scope parameters: NSTAR = 10000 (n cap), IMAX = 1000 (i cap for pair
classification).

(a) N-coverage. Every open-region triple with n ≤ 10000 was checked:
27,769,446,111 triples, 0 failures. This total was independently
reproduced by a closed-form count of the same index set (sum over n of
the number of admissible (i, j)); the two counts agree exactly.

(b) Fully cleared pairs. Of the 4,249,500 pairs (i, j) with
1 ≤ i ≤ 1000, j > 3i/2, and 2j ≤ 10000:

- 768,741 pairs are FULLY CLEARED: N(i, j) ≤ 10000, so the sweep checked
  their entire interval [2j, N(i, j)], and the reduction excludes every
  larger n (EEES78 exception values of n for these i were discharged
  directly, see below). For these pairs the conjecture holds for ALL n.
- 3,480,759 pairs are PARTIALLY covered: N(i, j) > 10000; all their
  triples with n ≤ 10000 were checked (no failure), but their intervals
  extend beyond the sweep cap, so they are not settled.
- Pairs with j > 5000 or i > 1000 were not classified and (except for
  their triples with n ≤ 10000, which the sweep did check whenever
  i < j ≤ n/2) are untouched. There are infinitely many such pairs.

Pair classification method (pairpass_fast.py): N(i, j) ≤ 10000 iff
C(10001, i) ≥ C(2j, 2(j-i)), since C(n, i) is strictly increasing in n;
and C(2j, 2(j-i)) is strictly increasing in j for fixed i, so each i's
cleared set is a prefix of its j-range, located by exact binary search
on the single threshold C(10001, i). The boundary was verified in exact
arithmetic for every i (C(2J, 2(J-i)) ≤ C(10001, i) < C(2J+2, 2(J+1-i))
at each i's maximal cleared J), and the classification was
cross-checked against the direct N(i, j) computation on 150 seeded
random pairs: 0 mismatches. Per-i maximal cleared j values are listed
in the appendix; the full cleared sets are in pairpass.json.

## EEES78 exception pairs discharged directly

The 12 exception pairs (n0, i0) where V_i(n) > C(n, i)^{1/2} can fail,
from PHASE0.md item 4: (8,3), (9,4), (10,5), (12,5), (21,7), (21,8),
(30,7), (33,13), (33,14), (36,13), (36,17), (56,13). The independent
checker computed gcd(V_{i0}(n0), C(n0, j)) directly for every
i0 < j ≤ n0/2 (both regions): 41 triples, all gcd > 1. Two pairs,
(9,4) and (10,5), have no admissible j at all (i0 = floor(n0/2)) and
are vacuously discharged. This discharge is also what the j ≤ 3i/2
closure needs at exception values of (n, i): with it, the closed
region j ≤ 3i/2 is settled for all n (proof refereed SOUND in
PHASE0.md item 3, conditional on EEES78, whose exception pairs are
exactly these).

## Independent checker outcomes (checker.py, checker_results.json)

The checker shares no machinery with the sweep: no bitmasks, no
Legendre formula; it uses math.comb and extracts V_i(n) by physically
dividing out all prime factors < i. Seed 20261028 throughout.

- Task 1, EEES78 exceptions: 41 triples, all gcd > 1.
- Task 2, cleared-pair re-verification: 18 fully cleared pairs sampled
  (seeded shuffle of all 768,741; pairs admitted while their full
  intervals fit a 40,000-triple budget, at most 300 pairs examined),
  each re-verified by brute force over its complete interval
  [2j, N(i, j)] with N(i, j) recomputed by exact binary search inside
  the checker: 39,982 triples, all gcd > 1.
- Task 3, random open-region triples with n ≤ 10000: 1,996 triples,
  all gcd > 1.
- Task 4, random closed-region triples (empirical spot check only):
  498 triples, all gcd > 1.
- Task (a) of the brief, re-verifying claimed coprime triples, was
  vacuous: the sweep claimed none.
- Problems found: none. Checker runtime 64 s.

Disclosure: the checker's first run was killed after about 17 minutes
because its original sample-selection loop, once the triple budget was
exceeded, kept computing exact N(i, j) for every remaining pair in the
768,741-pair list (an effective hang in sample selection, not in
verification). Only that selection loop was changed (budget-fitting
admission, 300-pair examination cap); the verification code is
unchanged, and the results above are from the fixed run.

## Runtimes

- Validation (n ≤ 240, both regions): 1.9 s.
- Sweep: 100 blocks of 100 consecutive n. First run completed blocks
  1 to 62 (n ≤ 6201) in 1,197 s of its own elapsed time and was
  interrupted by a VM restart; the resumed run completed blocks 63 to
  100 from the on-disk checkpoints (no block recomputed) in 4,011 s.
  Combined wall time about 5,208 s (about 87 minutes) on 2 workers.
- Pair classification: 97 s wall.
- Independent checker: 64 s.

## What this does and does not establish

Established: no counterexample with n ≤ 10000 anywhere in the open
region; the conjecture holds for all n for the 768,741 enumerated
open-region pairs and (via the Phase 0 refereed proof plus the direct
exception discharge) for every pair with j ≤ 3i/2.

Not established: the conjecture in general. Partially covered pairs
(3,480,759 of them within i ≤ 1000, j ≤ 5000 alone) have intervals
extending beyond n = 10000, and pairs with larger i or j were not
classified. Any future extension is a matter of raising NSTAR (the
sweep is checkpointed and resumable, and pair classification is a
threshold recomputation), but the pair-by-pair intervals grow without
bound, so no finite sweep of this form closes the whole problem.

## Files

- PHASE0.md: gate record (statement, reduction, referee verdict,
  EEES78 exceptions, incumbent check).
- sweep.py, checkpoints/ (100 block files), sweep_summary_10000.json:
  {"nstar": 10000, "triples": 27769446111, "flagged": [], "confirmed": []}.
- validate.py, phase0_item2_test.py: pre-production validations.
- pairpass_fast.py, pairpass.json: pair classification (pairpass.py is
  the slower direct-N(i, j) reference implementation used for
  cross-checks).
- checker.py, checker_results.json: independent checker and outcomes.
- sweep_10000.log, pairpass_fast.log, checker.log: run logs.

## Appendix: maximal fully cleared j for each i

For each i (1 to 1000, in order), the cleared pairs are exactly
floor(3i/2) + 1 ≤ j ≤ J_i, with J_i below. (Every i in range has at
least one cleared pair.)

70, 93, 112, 128, 142, 155, 167, 178, 189, 199, 209, 218, 227, 236,
244, 252, 260, 268, 275, 283, 290, 297, 304, 310, 317, 323, 330, 336,
342, 348, 354, 360, 366, 372, 377, 383, 388, 394, 399, 404, 410, 415,
420, 425, 430, 435, 440, 445, 450, 454, 459, 464, 468, 473, 478, 482,
487, 491, 496, 500, 504, 509, 513, 517, 522, 526, 530, 534, 538, 543,
547, 551, 555, 559, 563, 567, 571, 575, 578, 582, 586, 590, 594, 598,
601, 605, 609, 613, 616, 620, 624, 627, 631, 635, 638, 642, 645, 649,
653, 656, 660, 663, 667, 670, 673, 677, 680, 684, 687, 690, 694, 697,
701, 704, 707, 710, 714, 717, 720, 724, 727, 730, 733, 736, 740, 743,
746, 749, 752, 756, 759, 762, 765, 768, 771, 774, 777, 780, 783, 786,
790, 793, 796, 799, 802, 805, 808, 811, 814, 816, 819, 822, 825, 828,
831, 834, 837, 840, 843, 846, 849, 851, 854, 857, 860, 863, 866, 868,
871, 874, 877, 880, 882, 885, 888, 891, 894, 896, 899, 902, 905, 907,
910, 913, 915, 918, 921, 924, 926, 929, 932, 934, 937, 940, 942, 945,
948, 950, 953, 955, 958, 961, 963, 966, 969, 971, 974, 976, 979, 981,
984, 987, 989, 992, 994, 997, 999, 1002, 1004, 1007, 1009, 1012, 1014,
1017, 1020, 1022, 1024, 1027, 1029, 1032, 1034, 1037, 1039, 1042, 1044,
1047, 1049, 1052, 1054, 1057, 1059, 1061, 1064, 1066, 1069, 1071, 1073,
1076, 1078, 1081, 1083, 1085, 1088, 1090, 1093, 1095, 1097, 1100, 1102,
1104, 1107, 1109, 1112, 1114, 1116, 1119, 1121, 1123, 1126, 1128, 1130,
1133, 1135, 1137, 1139, 1142, 1144, 1146, 1149, 1151, 1153, 1156, 1158,
1160, 1162, 1165, 1167, 1169, 1171, 1174, 1176, 1178, 1180, 1183, 1185,
1187, 1189, 1192, 1194, 1196, 1198, 1201, 1203, 1205, 1207, 1209, 1212,
1214, 1216, 1218, 1220, 1223, 1225, 1227, 1229, 1231, 1234, 1236, 1238,
1240, 1242, 1244, 1247, 1249, 1251, 1253, 1255, 1257, 1260, 1262, 1264,
1266, 1268, 1270, 1272, 1275, 1277, 1279, 1281, 1283, 1285, 1287, 1289,
1292, 1294, 1296, 1298, 1300, 1302, 1304, 1306, 1308, 1310, 1313, 1315,
1317, 1319, 1321, 1323, 1325, 1327, 1329, 1331, 1333, 1335, 1337, 1339,
1342, 1344, 1346, 1348, 1350, 1352, 1354, 1356, 1358, 1360, 1362, 1364,
1366, 1368, 1370, 1372, 1374, 1376, 1378, 1380, 1382, 1384, 1386, 1388,
1390, 1392, 1394, 1396, 1398, 1400, 1402, 1404, 1406, 1408, 1410, 1412,
1414, 1416, 1418, 1420, 1422, 1424, 1426, 1428, 1430, 1432, 1434, 1436,
1438, 1440, 1442, 1444, 1446, 1448, 1450, 1452, 1453, 1455, 1457, 1459,
1461, 1463, 1465, 1467, 1469, 1471, 1473, 1475, 1477, 1479, 1481, 1482,
1484, 1486, 1488, 1490, 1492, 1494, 1496, 1498, 1500, 1502, 1504, 1505,
1507, 1509, 1511, 1513, 1515, 1517, 1519, 1521, 1522, 1524, 1526, 1528,
1530, 1532, 1534, 1536, 1537, 1539, 1541, 1543, 1545, 1547, 1549, 1551,
1552, 1554, 1556, 1558, 1560, 1562, 1564, 1565, 1567, 1569, 1571, 1573,
1575, 1577, 1578, 1580, 1582, 1584, 1586, 1588, 1589, 1591, 1593, 1595,
1597, 1599, 1600, 1602, 1604, 1606, 1608, 1609, 1611, 1613, 1615, 1617,
1619, 1620, 1622, 1624, 1626, 1628, 1629, 1631, 1633, 1635, 1637, 1638,
1640, 1642, 1644, 1646, 1647, 1649, 1651, 1653, 1655, 1656, 1658, 1660,
1662, 1663, 1665, 1667, 1669, 1671, 1672, 1674, 1676, 1678, 1679, 1681,
1683, 1685, 1686, 1688, 1690, 1692, 1693, 1695, 1697, 1699, 1701, 1702,
1704, 1706, 1708, 1709, 1711, 1713, 1715, 1716, 1718, 1720, 1721, 1723,
1725, 1727, 1728, 1730, 1732, 1734, 1735, 1737, 1739, 1741, 1742, 1744,
1746, 1747, 1749, 1751, 1753, 1754, 1756, 1758, 1759, 1761, 1763, 1765,
1766, 1768, 1770, 1771, 1773, 1775, 1777, 1778, 1780, 1782, 1783, 1785,
1787, 1788, 1790, 1792, 1794, 1795, 1797, 1799, 1800, 1802, 1804, 1805,
1807, 1809, 1810, 1812, 1814, 1816, 1817, 1819, 1821, 1822, 1824, 1826,
1827, 1829, 1831, 1832, 1834, 1836, 1837, 1839, 1841, 1842, 1844, 1846,
1847, 1849, 1851, 1852, 1854, 1856, 1857, 1859, 1861, 1862, 1864, 1866,
1867, 1869, 1870, 1872, 1874, 1875, 1877, 1879, 1880, 1882, 1884, 1885,
1887, 1889, 1890, 1892, 1893, 1895, 1897, 1898, 1900, 1902, 1903, 1905,
1907, 1908, 1910, 1911, 1913, 1915, 1916, 1918, 1920, 1921, 1923, 1924,
1926, 1928, 1929, 1931, 1933, 1934, 1936, 1937, 1939, 1941, 1942, 1944,
1945, 1947, 1949, 1950, 1952, 1953, 1955, 1957, 1958, 1960, 1961, 1963,
1965, 1966, 1968, 1969, 1971, 1973, 1974, 1976, 1977, 1979, 1981, 1982,
1984, 1985, 1987, 1989, 1990, 1992, 1993, 1995, 1996, 1998, 2000, 2001,
2003, 2004, 2006, 2008, 2009, 2011, 2012, 2014, 2015, 2017, 2019, 2020,
2022, 2023, 2025, 2026, 2028, 2030, 2031, 2033, 2034, 2036, 2037, 2039,
2041, 2042, 2044, 2045, 2047, 2048, 2050, 2051, 2053, 2055, 2056, 2058,
2059, 2061, 2062, 2064, 2065, 2067, 2069, 2070, 2072, 2073, 2075, 2076,
2078, 2079, 2081, 2082, 2084, 2086, 2087, 2089, 2090, 2092, 2093, 2095,
2096, 2098, 2099, 2101, 2102, 2104, 2105, 2107, 2109, 2110, 2112, 2113,
2115, 2116, 2118, 2119, 2121, 2122, 2124, 2125, 2127, 2128, 2130, 2131,
2133, 2134, 2136, 2138, 2139, 2141, 2142, 2144, 2145, 2147, 2148, 2150,
2151, 2153, 2154, 2156, 2157, 2159, 2160, 2162, 2163, 2165, 2166, 2168,
2169, 2171, 2172, 2174, 2175, 2177, 2178, 2180, 2181, 2183, 2184, 2186,
2187, 2189, 2190, 2192, 2193, 2195, 2196, 2198, 2199, 2201, 2202, 2204,
2205, 2207, 2208, 2210, 2211, 2213, 2214, 2216, 2217, 2219, 2220, 2222,
2223, 2224, 2226, 2227, 2229, 2230, 2232, 2233, 2235, 2236, 2238, 2239,
2241, 2242, 2244, 2245, 2247, 2248, 2250, 2251, 2253, 2254, 2255, 2257,
2258, 2260, 2261, 2263, 2264, 2266, 2267, 2269, 2270, 2272, 2273, 2274,
2276, 2277, 2279, 2280, 2282, 2283, 2285, 2286, 2288, 2289, 2291, 2292,
2293, 2295, 2296, 2298, 2299, 2301, 2302, 2304, 2305, 2307, 2308, 2309,
2311, 2312, 2314, 2315, 2317, 2318, 2320, 2321, 2322, 2324, 2325, 2327,
2328, 2330, 2331, 2333, 2334, 2335, 2337, 2338, 2340, 2341, 2343, 2344,
2345, 2347, 2348, 2350, 2351, 2353, 2354, 2355, 2357, 2358, 2360, 2361,
2363, 2364, 2365, 2367, 2368, 2370, 2371, 2373, 2374, 2375, 2377, 2378,
2380, 2381, 2383, 2384, 2385, 2387, 2388, 2390, 2391

## Addendum (2026-10-28): post-review disclosures and Stage 1 fixes

Appended after the adversarial review (REVIEW.md); the original text
above is unchanged. The review found no silent miss and contradicted
no claim in substance; the items below are the disclosures and
evidence deposits it required.

Disclosures (review findings L1, L2, L3, L4):

- Task 2 sampling bias (L1). The 18 re-verified cleared pairs are NOT
  a uniform sample of the 768,741: they are the first budget-fitting
  pairs among 300 seeded-shuffle-examined pairs (40,000-triple budget,
  first pair admitted unconditionally). This biases the sample toward
  shorter intervals (selected median interval length 1734, vs 2238
  among the 300 examined). Task 2 is a spot re-verification, not an
  estimator, so the bias does not affect any conclusion; it is
  recorded here because the original text did not note it.
- Pre-fix checker version (L2). The disclosure in "Independent
  checker outcomes" that the killed first run's fix touched only the
  sample-selection loop rests on author statement plus an in-code
  comment: no pre-fix version of checker.py was preserved anywhere,
  so the claim cannot be diff-verified. It is structurally consistent
  (the budget/cap variables are referenced only inside the selection
  block), and a fresh rerun of the fixed checker.py reproduced
  checker_results.json in every field except runtime.
- Pair classification runtime (L3). Two numbers are recorded for the
  same run: pairpass.json's runtime_s = 89.30 s and the 97 s in
  pairpass_fast.log (and in "Runtimes" above). Both are correct as
  measured: the JSON field is stamped before the 4.2 MB JSON dump is
  written, the log line after it; the difference is that
  serialization plus final output.
- Sweep log structure (L4). sweep_10000.log is two concatenated runs
  with no separator: lines 1-63 are run 1 (header "already done 0"
  plus 62 block lines, ending at its elapsed 1197 s), and the second
  header at line 64 ("already done 62") begins run 2 (38 block lines,
  ending at its elapsed 4011 s). The "combined wall time about
  5,208 s" in "Runtimes" above is the SUM of the two runs' internal
  elapsed times (1197 + 4011), excluding the VM-restart interval
  between them.

Stage 1 fixes applied 2026-10-28 (review must-fix list; details and
production history in PROVENANCE.md):

- Closed-form counting evidence deposited: counting.py and
  count_closed_form.py; count_closed_form_10000.txt records exactly
  27,769,446,111 open-region triples for n <= 10000, confirming the
  cross-check sentence in "Coverage" above (H2).
- Retained outputs deposited: validate_rerun.txt (568,820 triples,
  0 mismatches) and phase0_test_rerun.txt (Phase 0 tests (A)-(G) all
  as recorded in PHASE0.md) (M2).
- Production commands and environment recorded in PROVENANCE.md;
  sweep.py's docstring no longer advertises the nonexistent
  --validate-direct flag (M3).
- pairpass.py (reference implementation) now writes
  pairpass_reference.json and cannot overwrite the production
  pairpass.json (M4).
- sweep.py's checkpoint loader now validates every checkpoint it
  loads (internal lo/hi vs filename, per-block count vs the closed
  form, flagged-list shape and region membership) and aborts loudly
  on any mismatch; test_checkpoint_loader.py plants the review's
  forged-checkpoint probe and variants and confirms rejection (H1).
- checker.py's N_exact is now exact on the full domain (downward
  pinning ported; verified against pairpass.N_of on all 3,160 pairs
  with i < j <= 80 and 300 random open pairs, 0 mismatches) (M1).
- Regression gate after all changes: validate.py, phase0 tests, and
  checker.py rerun end-to-end with every verdict and count identical
  to the originals, and the sweep machinery rerun over n <= 500
  reproduced the original per-block counts and total exactly,
  including a validated resume. No Stage 1 change altered any
  previously reported number.

## Completion addendum (2026-10-29): cap-20,000 extension sweep

Appended 2026-10-29 after hourly check 8 verified completion. The
original text above is unchanged.

The cap-20,000 extension sweep is COMPLETE. All 200 blocks finished;
the final block (19902-20000) was written at 21:37 UTC / 17:37 ET on
2026-10-29, completing the run resumed manually from the main chat at
about 15:12 ET that day from 173 validated checkpoints.

- Sweep total: sweep_summary_20000.json records 222,188,892,222
  open-region triples checked for n <= 20000. This equals the
  closed-form figure in count_closed_form_20000.txt
  (222,188,892,222) exactly.
- Flagged candidates: none. The summary's flagged and confirmed
  lists are both empty, and every checkpoint's bad list was empty
  throughout the run. No counterexample was found in scope. This
  does not solve Erdos #699 overall; it clears the open region for
  n <= 20000 only.
- Classification (pairpass_fast20000.py, run 2026-10-29 after the
  sweep completed; output pairpass_20000.json): 33,330,000 pairs
  considered, 8,021,170 pairs fully cleared, 25,308,830 pairs
  partial. The built-in cross-check against the direct N_of
  computation covered 150 seeded random pairs with 0 mismatches,
  and the boundary was verified exactly for every i.
- Sub-scope comparison: the i <= 1000, j <= 5000 sub-scope fully
  cleared count computed from pairpass_20000.json is 1,302,183,
  matching the prediction on record in
  threshold_prediction_20000.txt (1,302,183) exactly.
- Independent spot check (spotcheck_20000.py, output
  spotcheck_20000.json): a seeded random sample (seed 20261029) of
  300 open-region triples with n in (10000, 20000] was verified by
  direct gcd computation, gcd(V_i(n), C(n, j)) with V_i computed by
  Legendre exponents in exact bigint arithmetic. All 300 triples
  had gcd > 1; 0 coprime triples found, consistent with the sweep.
