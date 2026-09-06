r"""THE FAMILY TERM -- is the raw split share's deficit at a fixed prime,
climbing toward 1/6 with the discriminant box, the SECONDARY TERM of
the count of cubic fields by discriminant, read at that prime's local
density? (No per-field explicit formula carries such a share; child of
explore_triple_ramified_term.py, whose F3 measured the climb with no
class map and named the count's secondary term as the suspect, unread.)

THE QUESTION. Over the cubic fields to |d| <= 24000 the share of
fields in a discriminant box where a fixed unramified prime p is
totally split sits below Chebotarev's 1/6 and rises with the box (p =
3: 0.080 +- 0.014 over |d| <= 3000, 0.120 +- 0.008 over 12000 < |d| <=
24000). A per-field term predicts nothing about a share across fields
at a fixed prime. The count of cubic fields by discriminant has a
second main term of order X^(5/6) whose local densities per splitting
type are published. Does that term, read per prime, predict the
measured share in every box, at every prime p <= 31?

THE SOURCES, read full-text. Taniguchi and Thorne, Secondary terms in
counting functions for cubic fields, Duke Math. J. 162 (2013), Theorem
1.1, Theorem 1.3 and the density table of Section 6.2 (arXiv
1102.2914); Bhargava, Shankar and Tsimerman, On the Davenport-Heilbronn
theorems and second order terms, Invent. Math. 193 (2013), Theorems 3
and 7 (arXiv 1005.0672), the same two terms with the local factor
written as a p-adic integral.

THE HAND-DERIVATION (pre-engine, on paper).

  (1) THE TWO TERMS. With N^(+-)(X) the number of cubic fields with
      0 < +-Disc < X,
          N^(+-)(X) = C^(+-) A X + K^(+-) B X^(5/6) + O(X^(7/9 + eps)),
          A = 1/(12 zeta(3)),  B = 4 zeta(1/3) / (5 Gamma(2/3)^3 zeta(5/3)),
          C^+ = 1, C^- = 3, K^+ = 1, K^- = sqrt 3.
      zeta(1/3) < 0, so B < 0: the second term is a DEFICIT that decays
      as X^(-1/6) relative to the first. Numerically A = 0.069326, B =
      -0.147685 (the constants recomputed at C1, the paper's worked
      example reproduced at C2).

  (2) THE LOCAL DENSITIES (Taniguchi-Thorne Section 6.2, the table).
      Write x = p^(-1/3). Unnormalised, per splitting type at p:

          type                  at s = 1        at s = 5/6
          totally split (111)   1/6             (1 + x)^3 / 6
          partially split (12)  1/2             (1 + x)(1 + x^2) / 2
          inert (3)             1/3             (1 + x^3) / 3
          partially ramified    1/p             (1 + x)^2 / p
          totally ramified      1/p^2           (1 + x) / p^2

      normalised by their sums C_p = 1 + 1/p + 1/p^2 and K_p =
      (1 - p^(-5/3))(1 + 1/p)/(1 - x); the identities are checked by
      hand (sympy) and at every prime the engine reads (C1). At p = 2
      and 3 the extra ramified rings split each ramified row by
      multipliers that are the same at both s, so the row TOTALS above
      hold at every prime. With the local condition "type t at p" the
      count is C^(+-) c_p(t) A X + K^(+-) k_p(t) B X^(5/6), c and k
      the normalised densities: the second term carries its own
      density, and it is NOT proportional to the first (k_p(111)/c_p(111)
      = 1.92 at p = 3), which is the whole of the effect.

  (3) THE PREDICTED SHARE. In a box (X1, X2] the predicted count of
      fields of type t is the difference of the two-term formula at the
      edges; the split share among fields unramified at p is
          [C c(111) A D1 + K k(111) B D56] /
          [C c(unr) A D1 + K k(unr) B D56],
      D1 = X2 - X1, D56 = X2^(5/6) - X1^(5/6), c(unr) and k(unr) the
      sums over the three unramified types. At the main term alone the
      share is exactly 1/6 (c(unr) = 1/C_p). The second term lowers it
      because the split type's 5/6-density is the LARGEST relative to
      its 1-density among the unramified types: (1 + x)^3 against
      (1 + x)(1 + x^2) and (1 + x^3). Hand values, COMPLEX fields, the
      split share among unramified fields per box:

          p     (0,3000] (3000,6000] (6000,12000] (12000,24000] (24000,48000] (48000,96000]
          3     0.0928   0.1143      0.1217       0.1278        0.1330        0.1373
          5     0.0992   0.1188      0.1255       0.1311        0.1358        0.1398
          7     0.1030   0.1215      0.1278       0.1331        0.1375        0.1413
          13    0.1103   0.1267      0.1323       0.1370        0.1409        0.1443
          31    0.1209   0.1343      0.1388       0.1426        0.1458        0.1485
          997   0.1508   0.1555      0.1570       0.1584        0.1595        0.1604

      and both signs pooled 0.0710, 0.1007, 0.1105, 0.1185 at p = 3
      over the parent's four boxes, against the parent's measured
      0.080 +- 0.014, 0.088 +- 0.014, 0.119 +- 0.011, 0.120 +- 0.008:
      z = +0.6, -0.9, +0.8, +0.2 on paper, before the rig runs. The
      deficit 1/6 - share falls by the factor 2.52 from the first box
      to the sixth at p = 3 (complex), the X^(-1/6) of the term
      through the boxes' own D56/D1.

  (4) THE REAL SIGN ALONE IS UNREADABLE IN THE FIRST BOX: with C^+ = 1
      the two terms give 91.3 fields at X = 3000 against 96 found, and
      the split-at-3 count goes NEGATIVE (-0.029 as a share) -- the
      asymptotic read below its range. So the primary read is the
      COMPLEX fields, where the second term is sqrt 3 / 3 of the first
      in relative size and the count control (C0) holds to a handful
      of fields at every edge; both signs pooled is printed beside it
      because the parent's F3 was pooled.

  (5) THE RAMIFIED TYPES move the other way: the partially ramified
      5/6-density (1 + x)^2/p is 2.9 times its 1-density at p = 3 and
      the totally ramified one (1 + x)/p^2 only 1.7 times, so with B
      < 0 the partially ramified share of ALL fields sits BELOW its
      main-term density and the totally ramified share ABOVE it: at
      p = 3 in the first box 0.2159 against 0.2308 and 0.0891 against
      0.0769 (complex).

  (6) THE RANGE IN p. Theorem 1.3's error term is O(X^(7/9 + eps)
      p^(8/9)) for an unramified condition at p, which at these X
      exceeds the count itself at EVERY p -- a worst-case bound, not
      the truth; the count control shows the two terms hold with no
      local condition. What the bound does say is that nothing is
      claimed uniformly in p, and the parent measured the band [300,
      1000) at 1/6 over |d| <= 3000 where the table predicts about
      0.145: a prime above the discriminant reads Chebotarev's share,
      the family term being a small-p statement. Read as a print (P6),
      never as a kill.

  (7) THE STATISTIC. The measured share is s = m/n over the n fields
      of the box unramified at p, m of them split; its bar is
      binomial, sqrt(s(1 - s)/n) printed, and every z is computed on
      the PREDICTED share's variance, z = (m - n s_pred)/sqrt(n s_pred
      (1 - s_pred)). The pooled z per prime over the boxes is the sum
      of the excesses over the root of the summed variances. The
      prediction has no sampling error of its own; the theorem's
      remainder is the unpriced part, (6).

  (8) THE DEGREE-2 ARM, the third arm of the transfer. The count of
      quadratic fields by discriminant has NO X^(5/6) term (the number
      of fundamental discriminants in a class mod p is its density
      times X plus O(sqrt X)), so the split share among the quadratic
      fields unramified at p sits at 1/2 in every box up to a relative
      O(X^(-1/2)), 0.018 at X = 3000 against a binomial bar of the same
      size. A deficit of the cubic shape there would say the effect is
      not the count's.

  (9) WHAT IS NOT CONTROLLED. (a) The remainder term of the two-term
      formula, (6): a disagreement at the size of the count control's
      residuals (a few fields per box) is inside it. (b) The prime 2,
      where the parent's type reader is not run; the odd primes 3 to
      31 are the read. (c) The parent's population had 4865 fields
      after its class reading excluded three; this rig reads the
      enumeration itself, 4868 to 24000, so the reproduction of F3 is
      to the third decimal, not the digit.

TRANSPLANT FLAGS, fixed at the freeze.

 T1 FROM explore_triple_ramified_term.py S6: the boxes to 24000, the
    primes 3, 5, 7, 13, 997 and the band [300, 1000) are REPRINTED as
    the reproduction (C4); the boxes to 96000 are this file's.
 T2 FROM explore_cubic_principal.py: the enumeration and the type
    reader are IMPORTED; the maximal-order sieve is widened here for
    the cap (the parent's asserts |disc| < 10^6, which the Hunter box
    at 96000 exceeds), the enumerator otherwise the parent's.
 T3 FROM explore_ceiling_squares.py: the expectation that the
    quadratic family shows NO deficit is a transplant from its
    flattened degree-2 table, re-derived in (8) from the count.

THE SLATE -- PREDICTIONS FROZEN BEFORE THE ENGINE.

  P1  THE FRONT'S KILL-SHAPE, printed: over the ten odd primes p <= 31,
      complex fields, the pooled z per prime between the measured
      split share and the two-term prediction across the six boxes.
      |z| > 2 at MORE THAN FIVE of the ten kills: the residual is a
      third thing. Hand-read on the parent's pooled figures, (3):
      survives.
  P2  THE BAR TO BEAT: against the null 1/6 (no family term) the same
      pooled z is below -2 at every one of the ten primes.
  P3  THE SCALING: the measured deficit ratio between the first box
      and the sixth at p = 3 sits within 2 sigma of the predicted 2.52.
  P4  THE RAMIFIED TYPES: pooled over the six boxes, the partially and
      totally ramified shares of all complex fields at p = 3, 5, 7 sit
      within 2 sigma of the two-term prediction, the partially
      ramified share BELOW its main-term density in the first box at
      each of the three.
  P5  THE DEGREE-2 ARM: the quadratic split share among unramified
      fields, pooled z against 1/2 per prime over the six boxes,
      |z| <= 2 at eight or more of the ten primes; no prime reads
      below -2 in the first box.
  P6  THE LARGE PRIMES, printed, no assert: at p = 101, 307, 997 and
      the band [300, 1000) the measured share in the first box exceeds
      the two-term prediction.

THE CONTROLS, run before any prediction is read.

  C0  THE COUNT. The enumerated complex fields to X = 3000, 6000,
      12000, 24000, 48000, 96000 against the two-term formula: within
      +-40 at every edge, and the main term alone off by more than 20 %
      at every edge. (The scratch rehearsal read -2.9, +0.2, -6.2,
      +0.6, +28.8, -23.7.)
  C1  THE TABLES: the five densities sum to C_p and K_p at every prime
      read, to 1e-12; the constants A and B recomputed by mpmath agree
      with the frozen values to 1e-9.
  C2  THE PAPER'S EXAMPLE: X = 2 x 10^6, positive discriminant, inert
      at 7 and partially ramified at 5: C(S) = 0.046217, K(S) =
      0.030884, the terms 6408.0 and -812.7 (Taniguchi-Thorne (6.20)-
      (6.22)), to the printed digits.
  C3  THE TYPE VECTOR: at every prime and box the five type counts sum
      to the field count, and off the polynomial discriminant the type
      agrees with the enumerator's own fingerprint at every field.
  C4  REPRODUCTION: the parent's F3 pooled shares over both signs to
      24000 at p = 3, 5, 7, 13, 997 and its band figures, within 0.003
      of the parent's print.

THE DESIGN. The parent's Hunter enumeration to |d| <= 96000 with the
sieve widened; per field one defining polynomial and its maximal
order; per odd prime p in 3..31, 101, 307, 997 and per field the type
read as the parent reads it (roots mod p off the polynomial
discriminant, the algebra O/pO on it, the ramification indices sorting
the two ramified types); the counts by sign, box and type; the
prediction by (3); the degree-2 arm by a sieve of fundamental
discriminants to 96000 and the Kronecker symbol. Estimate: 250 s for
the enumeration (rehearsed, peak 349 MB under memwatch), under a
minute for the types; one run, no class map anywhere.

FINDINGS. One population, both signs, 20908 fields to |d| <= 96000
(16313 complex, 4595 real; the parent's 4868 to 24000 inside it); the
odd primes 3 to 31 read at every field, 101, 307, 997 and the band
[300, 1000) beside. C0 held: the complex count sits within +-29 of the
two terms at all six edges (-2.9, +0.2, -6.2, +0.6, +28.8, -23.7)
while the main term alone overshoots by 49 % to 22 %; the real count
runs +5 to +35 above the two terms at every edge. C1 held to 4.4e-16,
C2 reproduced the paper's example to its printed digits, C3 held at
every one of 156 cells and 203821 fingerprint reads, C4 reproduced the
parent's F3 within 0.0017 at every cell.

  F1. THE DEFICIT IS THE COUNT'S SECONDARY TERM, READ AT THE PRIME'S
      LOCAL DENSITY (observation, ten primes, six boxes, complex
      fields; P1 SURVIVES, P2 holds). The split share among unramified
      complex fields against the two-term prediction, pooled z per
      prime over the six boxes:

        p     3     5     7    11    13    17    19    23    29    31
        z  -0.17 -0.39 -0.04 -1.12 -1.23 +0.16 +0.51 +0.29 +0.42 -0.68
        vs 1/6  -10.0 -10.1 -9.5 -9.9 -9.8 -8.1 -7.6 -7.4 -6.9 -7.8

      No prime is beyond 2 sigma of the prediction; every prime is 7 to
      10 sigma below 1/6. Of the 60 cells, one sits beyond 2 sigma
      (p = 31 in (3000, 6000], +2.3) and one at -2.1 (p = 7 in (12000,
      24000]), the expected two of sixty. Both signs pooled reads the
      same: pooled z between -1.03 and +0.97 at every prime, 10 to 14
      sigma below 1/6. At p = 3 the complex share climbs 0.092, 0.093,
      0.128, 0.125, 0.129, 0.139 over the boxes against the table's
      0.093, 0.114, 0.122, 0.128, 0.133, 0.137.

  F2. THE DEFICIT DECAYS AS THE TERM'S X^(-1/6) (observation; P3
      holds). The ratio of the deficit 1/6 - share between the box
      (0, 3000] and (48000, 96000] reads 2.72 +- 0.76, 2.87 +- 0.76,
      3.12 +- 0.75, 2.68 +- 0.68 at p = 3, 5, 7, 13 against the
      predicted 2.52, 2.51, 2.51, 2.51; the sixth-box deficits 0.0274
      +- 0.0045, 0.0261, 0.0260, 0.0268 against 0.0293, 0.0269, 0.0254,
      0.0224.

  F3. THE RAMIFIED TYPES CARRY THE TERM WITH ITS SIGN (observation; P4
      holds). Pooled over the six boxes the partially and totally
      ramified shares of all complex fields sit within 0.8 sigma of the
      two terms at p = 3, 5, 7 (z +0.24, -0.20, +0.44, +0.18, +0.54,
      +0.77), the partially ramified share below its main-term density
      in the first box at all three (0.2124 against 0.2308 at p = 3,
      0.1575 against 0.1613, 0.1074 against 0.1228) and the totally
      ramified share above it (0.0883 against 0.0769 at p = 3).

  F4. THE DEGREE-2 FAMILY HAS NO SUCH TERM (observation; P5 holds).
      Over 58356 fundamental discriminants to 96000 the quadratic split
      share among unramified fields sits at 1/2 in every one of the 60
      cells, the largest |z| 0.2 and the pooled z per prime within
      +-0.09 at all ten primes: the degree-2 table's flattening under
      per-field terms alone (explore_ceiling_squares.py) is the count's
      own shape, and the cubic residual is a cubic-count fact.

  F5. ABOVE THE THEOREM'S RANGE IN p THE BAND LEAVES THE TWO TERMS
      BOTH WAYS (observation, a print; P6 as read). At p = 997 the
      first box reads 0.175 +- 0.019 against 0.151 and the band [300,
      1000) 0.1623 +- 0.0018 against a predicted mean of 0.1480 where
      the window is above the discriminant; in the four middle boxes
      the band sits BELOW the two terms, 0.1516 +- 0.0011 against
      0.1553, 0.1541 +- 0.0008 against 0.1568, 0.1549 +- 0.0005 against
      0.1582, 0.1584 +- 0.0004 against 0.1593, and below 1/6 in every
      box (z -2.5 to -20.8). The two terms are a small-p statement;
      what the share does at p comparable to the discriminant is a
      third shape, uniform in neither p nor X, left open here.

RUN RECORD. 2026-09-06, Windows 11, Python 3, `python
prime/code/memwatch.py python prime/code/explore_family_term.py`. One
process, CPython, no BLAS. 18 checks, 371.9 s wall, peak working set
349.9 MB against memwatch's 512 MB ceiling: the enumeration 247 s and
the whole of the peak, the types 18 s, the degree-2 arm and the band
the rest. Rehearsed first at cap 6000 (14 s, 35 MB, every stage
exercised, P1-P5 holding on two boxes); the scratch count control that
fixed C0's band and the memory envelope ran before the file was
written.
"""

import os

os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")

import math
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import explore_cubic_field_shop as CFS
import explore_cubic_principal as ECP
import explore_cubic_ring as CR

CHECKS = 0
CAP = int(sys.argv[1]) if len(sys.argv) > 1 else 96000   # a rehearsal cap
BOXES = tuple(b for b in ((0, 3000), (3000, 6000), (6000, 12000),
                          (12000, 24000), (24000, 48000), (48000, 96000))
              if b[1] <= CAP)
READ_PRIMES = (3, 5, 7, 11, 13, 17, 19, 23, 29, 31)
LARGE_PRIMES = (101, 307, 997)
BAND = (300, 1000)
TYPES = ('split', 'partial', 'inert', 'pram', 'tram')
SIGNS = ((True, 3.0, math.sqrt(3.0)), (False, 1.0, 1.0))  # cx, C, K

# (1): the constants, frozen from mpmath at 17 digits (C1 recomputes)
ZETA3 = 1.2020569031595943
ZETA13 = -0.97336024835078272
ZETA53 = 2.1235229688575835
GAMMA23 = 1.3541179394264004
A_CONST = 1.0 / (12.0 * ZETA3)
B_CONST = 4.0 * ZETA13 / (5.0 * GAMMA23 ** 3 * ZETA53)


def ok(cond, msg):
    global CHECKS
    CHECKS += 1
    if not cond:
        print("  FAIL: " + msg)
        sys.exit(1)


def section(t):
    print()
    print("=" * 78)
    print(t)
    print("=" * 78)


# ------------------------------------------------------------ the densities
def densities(p):
    """(2): the normalised local densities at s = 1 and s = 5/6 per
    type, and the two normalisers."""
    x = p ** (-1.0 / 3.0)
    c = {'split': 1.0 / 6, 'partial': 0.5, 'inert': 1.0 / 3,
         'pram': 1.0 / p, 'tram': 1.0 / p ** 2}
    k = {'split': (1 + x) ** 3 / 6, 'partial': (1 + x) * (1 + x * x) / 2,
         'inert': (1 + x ** 3) / 3, 'pram': (1 + x) ** 2 / p,
         'tram': (1 + x) / p ** 2}
    Cp = 1 + 1.0 / p + 1.0 / p ** 2
    Kp = (1 - p ** (-5.0 / 3)) * (1 + 1.0 / p) / (1 - x)
    return ({t: c[t] / Cp for t in TYPES}, {t: k[t] / Kp for t in TYPES},
            Cp, Kp, sum(c.values()), sum(k.values()))


def predicted(p, t, lo, hi, signs, second=True):
    """(3): the two-term count of fields of type t at p with lo < |d| <=
    hi over the signs given ((cx, C, K) triples)."""
    c, k = densities(p)[:2]
    d1 = float(hi - lo)
    d56 = hi ** (5.0 / 6) - lo ** (5.0 / 6)
    out = 0.0
    for (_cx, Cs, Ks) in signs:
        out += Cs * c[t] * A_CONST * d1
        if second:
            out += Ks * k[t] * B_CONST * d56
    return out


def pred_share(p, lo, hi, signs, second=True):
    s = predicted(p, 'split', lo, hi, signs, second)
    u = s + sum(predicted(p, t, lo, hi, signs, second)
                for t in ('partial', 'inert'))
    return s / u


def zscore(m, n, s):
    return (m - n * s) / math.sqrt(n * s * (1 - s)) if n else 0.0


def bar(m, n):
    s = m / float(n) if n else 0.0
    return s, (math.sqrt(s * (1 - s) / n) if n else 0.0)


# ----------------------------------------------------------- the controls
def s_constants():
    section("S1  THE CONSTANTS AND THE TABLES -- C1, C2")
    print("  A = 1/(12 zeta(3)) = %.6f   B = 4 zeta(1/3)/(5 Gamma(2/3)^3 "
          "zeta(5/3)) = %.6f" % (A_CONST, B_CONST))
    try:
        import mpmath as mp
        mp.mp.dps = 20
        a = 1 / (12 * mp.zeta(3))
        b = (4 * mp.zeta(mp.mpf(1) / 3)
             / (5 * mp.gamma(mp.mpf(2) / 3) ** 3 * mp.zeta(mp.mpf(5) / 3)))
        print("  [C1] mpmath: A = %s, B = %s" % (mp.nstr(a, 12),
                                                 mp.nstr(b, 12)))
        ok(abs(float(a) - A_CONST) < 1e-9 and abs(float(b) - B_CONST) < 1e-9,
           "the frozen constants disagree with mpmath")
    except ImportError:
        print("  [C1] mpmath absent; the frozen constants stand unchecked")
    worst = 0.0
    for p in READ_PRIMES + LARGE_PRIMES:
        c, k, Cp, Kp, sc, sk = densities(p)
        worst = max(worst, abs(sc - Cp), abs(sk - Kp),
                    abs(sum(c.values()) - 1), abs(sum(k.values()) - 1))
    print("  [C1] the five densities sum to C_p and K_p at every prime "
          "read: worst defect %.1e" % worst)
    ok(worst < 1e-12, "a density table does not sum to its normaliser")
    c7, k7 = densities(7)[:2]
    c5, k5 = densities(5)[:2]
    CS = c7['inert'] * c5['pram']
    KS = k7['inert'] * k5['pram']
    X = 2.0e6
    main, sec = CS * A_CONST * X, KS * B_CONST * X ** (5.0 / 6)
    print("  [C2] the paper's example: C(S) = %.6f (.046217), K(S) = %.6f "
          "(.030884); terms %.1f (6408.0) and %.1f (-812.7)"
          % (CS, KS, main, sec))
    ok(abs(CS - 0.046217) < 1e-6 and abs(KS - 0.030884) < 1e-6
       and abs(main - 6408.0) < 0.15 and abs(sec + 812.7) < 0.05,
       "the paper's example does not reproduce")
    print("  the split share among unramified fields the table predicts, "
          "complex, by box:")
    for p in (3, 5, 7, 13, 31, 997):
        print("  p = %3d  %s" % (p, "  ".join(
            "%.4f" % pred_share(p, lo, hi, SIGNS[:1]) for (lo, hi) in BOXES)))


WIDE_SIEVE = CR._sieve(20000)


def maximal_order3_wide(a, b, c):
    """The parent's maximal_order3 with the index sieve widened to the
    primes below 20000 (p^2 | disc needs p <= sqrt |disc|), for the
    polynomial discriminants the Hunter box carries at this cap."""
    R = (-c, -b, -a)
    trvec = (3, -a, a * a - 2 * b)
    O = CFS.Order(R, trvec, [(1, 0, 0), (0, 1, 0), (0, 0, 1)])
    d0 = O.trace_form_disc()
    assert abs(d0) < 4 * 10 ** 8, "polynomial discriminant out of sieve range"
    for p in WIDE_SIEVE:
        if p * p > abs(d0):
            break
        if d0 % (p * p) == 0:
            O = CFS.p_maximalize(O, p)
    return O, O.trace_form_disc()


def s_enumerate():
    section("S2  THE POPULATION -- Hunter's box to |d| <= %d, and the "
            "count control C0" % CAP)
    t0 = time.time()
    ECP.maximal_order3 = maximal_order3_wide
    fields, b = ECP.enumerate_fields(CAP)
    print("  %d polynomials -> %d fields, %.1f s" % (b[0], len(fields),
                                                     time.time() - t0))
    print("  %-8s %-3s %6s %9s %9s %7s %8s" % ("X", "", "count", "main",
                                               "two terms", "diff",
                                               "main/n"))
    edges = [hi for (_lo, hi) in BOXES]
    for X in edges:
        for (cx, Cs, Ks) in SIGNS:
            n = sum(1 for f in fields if f[2] == cx and f[0] <= X)
            main = Cs * A_CONST * X
            two = main + Ks * B_CONST * X ** (5.0 / 6)
            print("  %-8d %-3s %6d %9.1f %9.1f %+7.1f %8.3f"
                  % (X, "cx" if cx else "re", n, main, two, n - two,
                     main / n))
            if cx:
                ok(abs(n - two) <= 40, "complex count off the two terms "
                   "by %.1f at X = %d" % (n - two, X))
                ok(main / n > 1.2, "the main term alone is within 20 %% "
                   "at X = %d" % X)
    return fields


# --------------------------------------------------------------- the types
def field_type(O, a, b, c, pdisc, p):
    if pdisc % p:
        _pl, kd = ECP.deg1_places(O, a, b, c, pdisc, p)
        return kd
    pl = CFS.maximal_places(O, p)
    es = sorted(e for (_P, e, _f) in pl)
    if es == [3]:
        return 'tram'
    if 2 in es:
        return 'pram'
    return ('split' if len(pl) == 3 else 'partial' if len(pl) == 2
            else 'inert')


def s_types(fields):
    section("S3  THE TYPES -- every field at every prime read, C3")
    t0 = time.time()
    counts = {}           # (p, cx, box) -> {type: n}
    fp_agree = fp_read = 0
    fp_names = {((1, 1), (1, 1), (1, 1)): 'split', ((1, 1), (1, 2)): 'partial',
                ((1, 3),): 'inert'}
    for (ad, d, cx, polys) in fields:
        bi = next(i for i, (lo, hi) in enumerate(BOXES) if lo < ad <= hi)
        a, b, c, O = polys[0]
        pdisc = CFS.poly_disc3(a, b, c)
        for p in READ_PRIMES + LARGE_PRIMES:
            t = field_type(O, a, b, c, pdisc, p)
            cell = counts.setdefault((p, cx, bi), dict((u, 0) for u in TYPES))
            cell[t] += 1
            if pdisc % p and p in CFS.SMALL_PRIMES:
                fp_read += 1
                fp_agree += (fp_names[CFS.shape_at(a, b, c, p)] == t)
    tot = 0
    for (p, cx, bi), cell in counts.items():
        n = sum(1 for f in fields if f[2] == cx
                and BOXES[bi][0] < f[0] <= BOXES[bi][1])
        tot += (sum(cell.values()) == n)
    print("  [C3] cells whose five types sum to the field count: %d of %d; "
          "fingerprint agreement off the discriminant: %d of %d; %.1f s"
          % (tot, len(counts), fp_agree, fp_read, time.time() - t0))
    ok(tot == len(counts), "a type vector does not sum to the field count")
    ok(fp_agree == fp_read, "a type disagrees with the fingerprint")
    return counts


def cell(counts, p, bi, signs):
    out = dict((t, 0) for t in TYPES)
    for (cx, _C, _K) in signs:
        for t, n in counts[(p, cx, bi)].items():
            out[t] += n
    return out


# --------------------------------------------------------------- the reads
def s_reproduce(counts):
    section("S4  REPRODUCTION -- the parent's F3, both signs to 24000, C4")
    parent = {3: (0.080, 0.088, 0.119, 0.120), 5: (0.086, 0.106, 0.103, 0.129),
              7: (0.082, 0.120, 0.119, 0.113), 13: (0.089, 0.114, 0.124, 0.136),
              997: (0.173, 0.169, 0.149, 0.148)}
    worst = 0.0
    for p in (3, 5, 7, 13, 997):
        line = "  p = %3d" % p
        for bi in range(min(4, len(BOXES))):
            cl = cell(counts, p, bi, SIGNS)
            n = cl['split'] + cl['partial'] + cl['inert']
            s, e = bar(cl['split'], n)
            worst = max(worst, abs(s - parent[p][bi]))
            line += "  %.4f +- %.4f (%.3f)" % (s, e, parent[p][bi])
        print(line)
    print("  worst departure from the parent's print: %.4f" % worst)
    ok(worst <= 0.003, "the parent's F3 does not reproduce")


def s_family(counts, signs, label, assert_p1=False):
    section("S5  THE FAMILY READ -- the split share among unramified fields "
            "by box, %s" % label)
    print("  per box: measured +- bar, then z against the two terms; "
          "pooled z per prime against the two terms and against 1/6")
    kills = null_fail = 0
    for p in READ_PRIMES:
        line = "  p = %2d" % p
        ex = var = ex0 = var0 = 0.0
        for bi, (lo, hi) in enumerate(BOXES):
            cl = cell(counts, p, bi, signs)
            n = cl['split'] + cl['partial'] + cl['inert']
            sp = pred_share(p, lo, hi, signs)
            s, e = bar(cl['split'], n)
            line += "  %.4f+-%.4f %+5.1f" % (s, e, zscore(cl['split'], n, sp))
            ex += cl['split'] - n * sp
            var += n * sp * (1 - sp)
            ex0 += cl['split'] - n / 6.0
            var0 += n * (1 / 6.0) * (5 / 6.0)
        zp, z0 = ex / math.sqrt(var), ex0 / math.sqrt(var0)
        kills += abs(zp) > 2
        null_fail += z0 < -2
        print(line + "   pooled z %+5.2f   vs 1/6 %+6.2f" % (zp, z0))
    print("  primes with |pooled z| > 2 against the two terms: %d of %d; "
          "primes with pooled z < -2 against 1/6: %d of %d"
          % (kills, len(READ_PRIMES), null_fail, len(READ_PRIMES)))
    if assert_p1:
        print("  [P1] %s" % ("KILLED: the residual is a third thing"
                             if kills > 5 else "SURVIVES"))
        print("  [P2] %s" % ("holds" if null_fail == len(READ_PRIMES)
                             else "FAILS"))
    return kills, null_fail


def s_scaling(counts):
    section("S6  THE SCALING -- the deficit ratio first box / sixth, "
            "complex, P3")
    for p in (3, 5, 7, 13):
        c1 = cell(counts, p, 0, SIGNS[:1])
        c6 = cell(counts, p, len(BOXES) - 1, SIGNS[:1])
        n1 = c1['split'] + c1['partial'] + c1['inert']
        n6 = c6['split'] + c6['partial'] + c6['inert']
        s1, e1 = bar(c1['split'], n1)
        s6, e6 = bar(c6['split'], n6)
        d1, d6 = 1 / 6.0 - s1, 1 / 6.0 - s6
        ratio = d1 / d6 if d6 > 0 else float('inf')
        err = (ratio * math.sqrt((e1 / d1) ** 2 + (e6 / d6) ** 2)
               if d1 > 0 and d6 > 0 else float('inf'))
        p1 = 1 / 6.0 - pred_share(p, BOXES[0][0], BOXES[0][1], SIGNS[:1])
        p6 = 1 / 6.0 - pred_share(p, BOXES[-1][0], BOXES[-1][1], SIGNS[:1])
        print("  p = %2d  deficits %.4f +- %.4f and %.4f +- %.4f; ratio "
              "%.2f +- %.2f  predicted %.2f (%.4f, %.4f)"
              % (p, d1, e1, d6, e6, ratio, err, p1 / p6, p1, p6))
        if p == 3:
            print("  [P3] %s" % ("holds" if abs(ratio - p1 / p6) <= 2 * err
                                 else "FAILS"))


def s_ramified(counts):
    section("S7  THE RAMIFIED TYPES -- shares of all complex fields by "
            "box, P4")
    holds = below = 0
    for p in (3, 5, 7):
        for t in ('pram', 'tram'):
            line = "  p = %d %-5s" % (p, t)
            ex = var = 0.0
            for bi, (lo, hi) in enumerate(BOXES):
                cl = cell(counts, p, bi, SIGNS[:1])
                n = sum(cl.values())
                tot = sum(predicted(p, u, lo, hi, SIGNS[:1]) for u in TYPES)
                sp = predicted(p, t, lo, hi, SIGNS[:1]) / tot
                s, e = bar(cl[t], n)
                line += "  %.4f (%.4f)" % (s, sp)
                ex += cl[t] - n * sp
                var += n * sp * (1 - sp)
                if bi == 0 and t == 'pram':
                    below += s < densities(p)[0]['pram']
            z = ex / math.sqrt(var)
            holds += abs(z) <= 2
            print(line + "  pooled z %+5.2f  main-term density %.4f"
                  % (z, densities(p)[0][t]))
    print("  [P4] %s: %d of 6 pooled reads within 2 sigma, the partially "
          "ramified share below its main-term density in the first box "
          "at %d of 3 primes" % ("holds" if holds == 6 and below == 3
                                 else "FAILS", holds, below))


def fundamental_discs(cap):
    """Every fundamental discriminant with |D| <= cap, both signs."""
    sqf = [True] * (cap + 1)
    for q in range(2, int(math.sqrt(cap)) + 1):
        for m in range(q * q, cap + 1, q * q):
            sqf[m] = False
    out = []
    for m in range(2, cap + 1):
        if not sqf[m]:
            continue
        for D in (m, -m):
            if D % 4 == 1:
                out.append(D)
        if m % 4 in (2, 3) and 4 * m <= cap:
            out.append(4 * m)
        if (-m) % 4 in (2, 3) and 4 * m <= cap:
            out.append(-4 * m)
    return out


def kron(D, p):
    r = pow(D % p, (p - 1) // 2, p)
    return 0 if r == 0 else (1 if r == 1 else -1)


def s_degree2():
    section("S8  THE DEGREE-2 ARM -- the quadratic split share among "
            "unramified fields by box, P5")
    Ds = fundamental_discs(CAP)
    print("  %d fundamental discriminants to |D| <= %d, both signs; the "
          "count has no X^(5/6) term" % (len(Ds), CAP))
    within = first_bad = 0
    for p in READ_PRIMES:
        line = "  p = %2d" % p
        ex = var = 0.0
        for bi, (lo, hi) in enumerate(BOXES):
            n = m = 0
            for D in Ds:
                if lo < abs(D) <= hi and D % p:
                    n += 1
                    m += kron(D, p) == 1
            s, e = bar(m, n)
            z = zscore(m, n, 0.5)
            line += "  %.4f %+5.1f" % (s, z)
            ex += m - n * 0.5
            var += n * 0.25
            if bi == 0 and z < -2:
                first_bad += 1
        zp = ex / math.sqrt(var)
        within += abs(zp) <= 2
        print(line + "   pooled z %+5.2f" % zp)
    print("  [P5] %s: %d of %d primes with |pooled z| <= 2, %d below -2 in "
          "the first box" % ("holds" if within >= 8 and first_bad == 0
                             else "FAILS", within, len(READ_PRIMES),
                             first_bad))


def s_large(fields, counts):
    section("S9  THE LARGE PRIMES AND THE BAND -- printed, P6")
    for p in LARGE_PRIMES:
        line = "  p = %3d" % p
        for bi, (lo, hi) in enumerate(BOXES):
            cl = cell(counts, p, bi, SIGNS[:1])
            n = cl['split'] + cl['partial'] + cl['inert']
            s, e = bar(cl['split'], n)
            line += "  %.4f+-%.4f (%.4f)" % (s, e, pred_share(p, lo, hi,
                                                                SIGNS[:1]))
        print(line)
    primes = [q for q in CR._sieve(BAND[1]) if BAND[0] <= q < BAND[1]]
    print("  the band [%d, %d), %d primes, complex fields: measured share "
          "and the table's mean prediction over the band's primes"
          % (BAND[0], BAND[1], len(primes)))
    for (lo, hi) in BOXES:
        n = m = 0
        for (ad, d, cx, polys) in fields:
            if not cx or not (lo < ad <= hi):
                continue
            a, b, c, O = polys[0]
            pdisc = CFS.poly_disc3(a, b, c)
            for q in primes:
                if d % q == 0:
                    continue
                n += 1
                m += ECP.deg1_places(O, a, b, c, pdisc, q)[1] == 'split'
        s, e = bar(m, n)
        mean = sum(pred_share(q, lo, hi, SIGNS[:1]) for q in primes) / len(primes)
        print("  (%5d, %5d]  %.4f +- %.4f   predicted %.4f   z vs 1/6 %+5.1f"
              % (lo, hi, s, e, mean, zscore(m, n, 1 / 6.0)))
    print("  [P6] a print: the theorem's error term is O(X^(7/9+eps) "
          "p^(8/9)), nothing uniform in p")


def main():
    t0 = time.time()
    s_constants()
    fields = s_enumerate()
    counts = s_types(fields)
    s_reproduce(counts)
    s_family(counts, SIGNS[:1], "COMPLEX fields (the primary read)",
             assert_p1=True)
    s_family(counts, SIGNS, "both signs pooled (the parent's read)")
    s_scaling(counts)
    s_ramified(counts)
    s_degree2()
    s_large(fields, counts)
    section("SUMMARY")
    print("  %d checks passed, %.1f s wall" % (CHECKS, time.time() - t0))


if __name__ == "__main__":
    main()
