r"""THE UNCOMPENSATED FRACTION AT DEGREE 2 -- is the fixed fraction of the
forcing the raw primes leave unpaid at degree 3 the explicit formula's
or the cubic seat's? (child of explore_ceiling_squares.py, whose
degree-2 populations, groups and prime-power correction it imports
whole and re-reads with every term kept by source, prime and power;
sibling of explore_triple_image_level.py, whose statistic it ports
from the cubic all-principal event to the quadratic principal class.)

THE QUESTION. At degree 3 the all-principal level, corrected by the
prime powers each counted at the uniform share 1/h^2, exceeds 1 by a
fixed fraction f of the FORCING F -- the excess the powers the algebra
sends to the identity put on the level -- with f = 0.21 +- 0.03 at
h = 2 and 0.33 to 0.45 at h = 4 to 11 prime to 3 while F runs 0.3 to
3.1; the naive explicit formula says f = 0, the image share f = 1 and
the Chebyshev bias 0.66 to 0.71, and none is met. At degree 2 the
generator ceiling's corrected top band reads 1.0001 +- 0.0097 under the
uniform share (explore_ceiling_squares.py F1), and the corrected
trivial class at p < 1000 reads 0.96 to 1.02 across the strata, which
would be f near 0 if the forcing there is not small. This file reads f
at degree 2 by the same statistic, per stratum and window, on both
quadratic signs: if f is 0 there the naive formula is exact at degree 2
and 40 % short at degree 3, and the shortfall is the cubic seat's; if f
sits in the cubic band the fraction is the formula's own and the seat
is not the cause.

THE HAND-DERIVATION (pre-engine, on paper).

  (1) THE GROUP AND THE SOURCES. Gal(H/Q) = Cl x| {1, s}, s inverting.
      A split prime's place b has Frobenius (b, 1) with k-th power
      (k.b, 1); an inert prime's (b, s) squares to the identity; a
      ramified prime q | D has one place r of K, unramified in H, with
      class in Cl[2], counted by the formula at the half weight of a
      split prime's two places (the parent's (2)). The prime 2, which
      the corpus's counts exclude, is a raw place when split, at
      weight 1. So per field and window [lo, hi) the terms are
        split  q, k >= 2, q^k in window : weight 1/k    on k.b
        two    q = 2 split, k = 1        : weight 1      on b
        inert  q, k even, q^k in window : weight 1/k    on 0
        ram    q | D, k >= 1, q^k in win : weight 1/(2k) on k.r,
      and the parent's corr_deg2 is the sum of these, checked (C1).

  (2) THE IMAGE SHARES, the probability a term lands on the identity
      under a uniform Frobenius in its coset:
        split k.b = 0   iff b in Cl[k]      : |Cl[k]| / h  (= gcd(k, h)/h,
                                              every field here cyclic)
        two   b = 0                         : 1 / h        (a raw place)
        inert k even                        : 1            (forced)
        ram   k even, k.r = 0 always        : 1            (forced)
              k odd, r = 0 iff r principal  : 1 / |Cl[2]|  (r taken
                                              uniform on Cl[2], a MODEL
                                              as the cubic P^3 term's
                                              1/|Cl[3]| was; the actual
                                              landing is printed).
      The uniform read is 1/h for every term.

  (3) THE FORCING AND ITS SIZE. Write W_t for a term's weight summed
      over a stratum's fields, n_s the raw split places, N = n_s +
      sum W_t, exp_u = N/h; the forcing F = sum_t W_t (p_t - 1/h) /
      exp_u; the uniform level L_u = (n_triv + landed)/exp_u; f =
      (L_u - 1)/F. Over p < 1000 the forced weight per field is the
      inert primes' squares below 31.6 (about 5.5 x 1/2), their fourth
      powers below 5.6 (about 1.5 x 1/4), 3^6 and 2^6 (1/6 each when
      inert) and the ramified even powers (about 1/4), near 3.5, plus
      the split squares' surplus (|Cl[2]|/h - 1/h per 1/2 on about 5.5
      split primes below 31.6, 1/h at even h); against N near 89 that is
      F near 0.04 (h - 1): 0.2 at h = 6, 0.5 at h = 14. Over
      [1000, 10000) the squares of the 14 primes in (31.6, 100) and
      7^4, 3^8, 2^10, 2^12 give near 3.8 forced against N near 545, F
      near 0.007 (h - 1). The forcing is a tenth of the cubic one and
      the read leans on the low window, as the cubic read did.

  (4) THE GEOMETRY, which the cubic read did not face as a zero. An
      imaginary field has NO principal split prime below |D|/4 -- the
      norm form's least value off the identity -- so over p < 1000 with
      |D| <= 4000 the raw principal count is short by the whole of the
      expectation below |D|/4, the corpus's raw trivial level 0.52 to
      0.79 at p < 1000. The naive formula says the raw primes ABOVE the
      zero pay it back with the forcing; a per-field statement it is
      not (the oscillatory term carries the geometry), a population one
      it can be. So the read is taken on FOUR windows: p < 1000 (the
      cubic read's twin, the geometry inside), the top band [630, 1000)
      (past the zero for |D| < 2520), [1000, 10000) (past every zero
      on the imaginary sweep; the real sweep to 16000 has no zero, an
      indefinite form) and p < 10000. The zero is wider than the raw
      primes: a principal ideal of norm n < |D|/4 is a rational
      integer's, so every term below |D|/4 lands on the identity
      exactly when it is forced (an inert or ramified even power is
      the ideal (q^(k/2))) and never when it is free. The HARD-ZERO
      MASS, the identity's expectation from the raw places and the
      free terms below |D|/4 in the window over exp_u, is printed
      beside F per stratum: where it exceeds F the raw primes above
      the zero must sit ABOVE 1/h for the naive formula to hold, and
      the raw level by bin says whether they do.

  (5) THE STATISTIC AND ITS SPREAD. The summands are a raw place at
      1/h (var (1/h)(1 - 1/h)), a power of weight w at p_t (var
      w^2 p_t (1 - p_t), a forced term adding none). The uniform level
      keeps a binomial bar sqrt(exp_u (1 - 1/h))/exp_u; the parents
      found the principal count UNDER-dispersed (index 0.5 at p < 1000),
      so the bar that decides is the FIELD bar, the per-field residuals'
      empirical sd summed over the stratum's independent fields, both
      printed. f's bar is the uniform level's over F; the pooled f is
      the inverse-variance mean over the readable strata (exp_u >= the
      corpus's cell floor). The Chebyshev null's c_RS is the parent's
      (3) with the split primes' mean log p taken over the stratum's own
      counted places.

  (6) THE PRICE. Two sweeps the parent ran in 224 s beside a degree-3
      population; the term walk per field is primes to 10000 over ten
      windows. Estimate 3 minutes, peak under the parent's 400 MB.

  (7) WHAT 1 - f IS MADE OF, and its floor (written after the first
      run printed, before the finding was read at degree 3). Split the
      terms into the FORCED (p = 1, weight A, landing whole) and the
      FREE (weight B, image expectation b, landed l); with R = n_s/h
      the raw expectation, L_u - 1 = [(n_triv - R) + (l - b) + forcing]
      / exp_u, so
          1 - f = (R - n_triv)/forcing + (b - l)/forcing,
      the RAW DEFICIT and the FREE DEFICIT as shares of the forcing,
      each printed. Neither count can fall below zero, so f has a
      FLOOR, f_min = 1 - (R + b)/forcing, the value when nothing
      non-forced lands: negative wherever the raw expectation exceeds
      the forcing, positive where the forced landings alone exceed the
      uniform expectation, in which case f = 0 is unreachable and the
      naive formula's main term is smaller than its prime-power term.
      The same split is read on the cubic sibling's kept walks by bin.

TRANSPLANT FLAGS, fixed at the freeze.

 T1 FROM explore_ceiling_squares.py: the imaginary sweep to |D| <= 4000
    and the real narrow sweep to D <= 16000, the admissible fields
    (cyclic profile, MIN_SPLIT places below 250), the strata at 30
    fields, the Group with its composer, corr_deg2 as the C1 witness.
 T2 FROM explore_triple_image_level.py: the forcing, f, the three
    nulls and the summand bar, ported from Frobenius uniform on
    M x| S_3 to Frobenius uniform on Cl x| {1, s}. The cubic band for f,
    [0.33, 0.45], is the kill's bar; that f is a constant of the formula
    across degrees is the wild line being killed, not assumed.
 T3 THE RAMIFIED ODD POWER's share 1/|Cl[2]| is a model of r's class,
    as (2) says; its weight is a few tenths per stratum.

THE SLATE -- PREDICTIONS FROZEN BEFORE THE ENGINE.

  P1  THE KILL-SHAPE, printed: f pooled over the readable strata at
      h >= 4 of BOTH signs over p < 1000 lies within 2 sigma (field
      bar) of the band [0.33, 0.45] -- f - 2 sigma <= 0.45 and f + 2
      sigma >= 0.33. If it does, f is the formula's and the cubic seat
      is not the cause.
  P2  f WITHIN 2 SIGMA OF 0 at every readable stratum over p < 1000 on
      both signs, and pooled within 2 sigma of 0 on every one of the
      four windows.
  P3  THE CHEBYSHEV NULL 1 - c_RS lies above the pooled p < 1000 f by
      more than 2 sigma on both signs.
  P4  THE RAW PRINCIPAL LEVEL BY BIN rises across the bins on the
      imaginary side from below 0.30 in [3, 30) to within 0.10 of 1 in
      [1000, 3000), and the real side's [3, 30) bin sits above the
      imaginary's by more than 3 sigma.
  P5  REPRINT: the corrected trivial-class cells the parent's F1 quotes
      -- 0.96 to 1.02 at p < 1000 and 0.97 to 1.00 at p < 10000 over
      the imaginary strata h = 6 to 14 -- reprint as this file's L_u
      within 0.01; the parent's generator top band 1.0001 +- 0.0097
      reprints through its own reader to 0.0015.

THE CONTROLS, run before any prediction is read.

  C0  THE SHARES AGAINST THE GROUP: on one field per stratum, the
      closed forms of (2) equal the brute count over the Group's keys
      of k.b = 0 at every k <= 13; every inert even power and ramified
      even power lands on the identity in the walk.
  C1  THE WEIGHT IDENTITY: per field and window the by-source weights
      sum to corr_deg2's class-free total, and the landed weight per
      class equals corr_deg2's per-class weight, to 1e-9.
  C2  THE SUMMAND BAR: 2000 Bernoulli replicates of one stratum's
      image count at its measured weights and shares give a spread
      within 15 % of the summand sd of (5).
  C3  THE POSITIVE CONTROL: with the raw principal count REPLACED by a
      uniform draw at 1/h per split place and every free term drawn at
      its share, f reads 1 within 2 sigma (binomial bar), and with the raw count set to (n_s + W)/h minus
      the identity's landed weight it reads 0 exactly; the statistic tells its
      two nulls apart at this population's size.
  C4  THE REPRINT of P5's generator top band through the parent's
      read_both.

THE FINDINGS (the post-run record; every number is a print of the run).

  THE POPULATIONS. Imaginary: 224 admissible fields, strata h = 6, 8,
  10, 12, 14 of 45, 49, 51, 37, 42 fields. Real narrow: 2086, strata
  h = 2, 3, 4, 5, 6, 8, 10 of 1445, 85, 237, 32, 163, 62, 62. Readable
  at h >= 4 over p < 1000: the five imaginary strata; 4, 5, 6, 8, 10
  real.

  CONTROLS. C0: |Cl[k]| = gcd(k, h) on every stratum to k = 13, every
  forced term landed. C1: 3.6e-15 on both signs. C2: replicate spread
  22.9 against summand sd 23.1 (Poisson 29.6) at h = 6 imaginary, 62.3
  against 61.3 (79.0) at h = 4 real. C3: the image null's draw reads
  f = 0.949 +- 0.045 and 0.956 +- 0.042, the naive null's 0.000
  exactly, on the two signs. C4: 1.0001 +- 0.0097 reprints. P5: L_u
  over the composite strata h = 6 to 14 runs 0.959 to 1.016 at
  p < 1000 and 0.974 to 1.002 at p < 10000, the parent's cells.

  F1  THE KILL DOES NOT FIRE: THE FRACTION IS ZERO AT DEGREE 2 OVER THE
      CUBIC READ'S WINDOW (observation; P1 not met, P3 holds). Pooled
      over both signs at h >= 4 over p < 1000, f = 0.021 +- 0.016
      (field bar), z +1.3 from 0 and -23.5 from the cubic band's
      centre 0.39: imaginary -0.022 +- 0.020 (0.055, 0.019, -0.092,
      -0.055, 0.011 at h = 6 to 14, bars 0.04 to 0.05) and real
      +0.092 +- 0.026 (0.127, -0.549, 0.142, 0.021, 0.127 at h = 4,
      5, 6, 8, 10; the odd stratum h = 5, 32 fields, is the outlier).
      The Chebyshev null 1 - c_RS reads 0.61 to 0.64 at every
      stratum, 32 and 20 sigma above the pooled f.

  F2  f MOVES WITH THE WINDOW BY A FEW TENTHS AT DEGREE 2, WITH THE
      GEOMETRY DOMINANT WHERE IT SITS (observation; P2's letter fails:
      five of ten strata past 2 sigma from 0 at p < 1000, three of
      eight pooled window reads past it). The top band [630, 1000)
      reads 1.20 +- 0.18 on the imaginary sweep whole -- the fields
      with |D|/4 inside the band carry the burst of principal primes
      just past their zero, raw levels 1.06 to 1.14 -- and 0.36 +-
      0.17 on the 172 fields with |D| < 2520, past it; the real top
      band 0.19 +- 0.12. The far window [1000, 10000) reads -0.12 +-
      0.06 and -0.09 +- 0.06; p < 10000 reads -0.07 +- 0.02 and 0.00
      +- 0.03. The real narrow stratum h = 2 (1445 fields) reads
      0.217 +- 0.020 over p < 1000, the cubic h = 2's 0.21 +- 0.03,
      and -0.19 +- 0.08, -0.03 +- 0.05, 0.084 +- 0.023 on the other
      three windows.

  F3  BY BIN, THE DEGREE-2 FRACTION IS THE SMALLEST BIN'S ALONE, AND
      THERE IT SITS NEAR THE CUBIC BAND (observation; P4's letter fails on
      one clause, the imaginary bins dipping 0.913 to 0.905 across
      1000). Real, h >= 4: f = 0.400 +- 0.028 in [3, 30) and -0.04
      +- 0.07, -0.01 +- 0.07, 0.01 +- 0.08, -0.05 +- 0.09, -0.11 +-
      0.10 in the five bins above, the raw principal level 0.58,
      0.70, 0.80, 0.89, 0.94, 0.97; h = 2 real 0.42 +- 0.03, 0.36 +-
      0.07, 0.07 +- 0.06, 0.19 +- 0.06, -0.15 +- 0.06, 0.04 +- 0.07.
      Imaginary: 0.35 +- 0.03 in [3, 30) over h = 6, 8, 10 with the
      raw level 0.000 and nothing free landing -- that bin's f IS its
      floor, 0.30, 0.35, 0.375 by stratum, arithmetic of the weights
      -- then -0.65, -0.68 inside the hard zone ([30, 100) and
      [100, 300), raw 0.03 and 0.34, the zero mass 1.1 and 0.8 of
      the expectation), +0.30 +- 0.08 in [300, 1000) and -0.17, -0.08
      above 1000. The real side's [3, 30) sits above the imaginary's
      by 5.6 sigma in the raw level.

  F4  WHAT THE TWO DEGREES' FRACTIONS ARE MADE OF (observation; the
      split of (7), the cubic rows from explore_triple_image_level.py's
      kept walks). Over p < 1000 at h >= 4 the raw deficit takes 0.65
      to 0.83 of the forcing at degree 2 (h = 5 real 1.36) and the free
      terms 0.19 to 0.28, summing to 1; at degree 3 over [3, 1000) the
      raw deficit takes 0.13 to 0.33 and the free terms 0.33 to 0.48,
      summing to 0.55 to 0.67. The floor f_min = 1 - (R + b)/forcing
      is -0.8 to -5.0 at degree 2 and -0.63, -0.54, -0.09, +0.01,
      +0.12, +0.18 at h = 4, 5, 7, 8, 10, 11 at degree 3: from h = 8
      the forced landings alone exceed the uniform expectation and
      f = 0 is unreachable. The cubic f by bin: 0.48, 0.48 in [3, 30)
      at h = 4, 5; 0.37, 0.41 in [30, 100); 0.22 to 0.61 in
      [100, 300); 0.23, 0.31, 0.45, 0.26, 0.39 in [300, 1000) at h = 4,
      5, 7, 8, 10 (bars 0.08 to 0.17): in no bin does it fall to 0.
      At h = 2 the cubic's 0.21 splits 0.56 raw and 0.23 free, the
      real quadratic's 0.22 splits 0.69 and 0.09.

  F5  THE FREE TERMS LAND SHORT OF THEIR SHARES AT BOTH SIGNS
      (observation). Imaginary over p < 1000, h >= 4: the split
      squares land 10.0 on a weight of 508.5 (0.020 against the share
      0.217) and the ramified places at k = 1 land 17.5 on 220 (0.08
      against 0.50) -- both the hard zero, a square below |D|/4 never
      principal; real: 303 on 1432 (0.212 against 0.368) and 148.5 on
      419 (0.354 against 0.501), short with no zero to blame.

RUN RECORD. 2026-09-07, Windows 11, Python 3, `python
prime/code/memwatch.py --limit 512 prime/code/explore_ceiling_forcing.py`.
One process, CPython, no BLAS. 382 checks passed, 43.3 s wall, peak
working set 444 MB (the real sweep, the parent's). Five launches: the
first failed C3 as frozen -- the image null's draw replaced the raw
primes and kept the free terms' measured landings, which fall short of
their shares, f 0.685 -- and the control was made to draw the free
terms too, the zero mass widened to the free powers below |D|/4 in
the same edit; the second and third printed the slate's reads, the
third adding f per bin; the fourth added (7)'s columns and the cubic
stage and was killed at 565 MB commit loading the sibling's readings
beside the degree-2 populations; the fifth loads the walks alone after
freeing the populations and is the record above. The cubic rows need
the sibling's checkpoints under the system temp; absent, the stage
prints a notice.
"""

import os
os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")

import gc
import math
import random
import sys
import time
from collections import defaultdict
from math import gcd

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import explore_ceiling_curve as CV                 # noqa: E402
import explore_ceiling_squares as SQ               # noqa: E402
import explore_class_order as CO                   # noqa: E402
from explore_principal_share import primes_upto    # noqa: E402

CHECKS = 0
KMAX = 13                     # 2^13 = 8192 is the deepest power below 10^4
WINDOWS = ((0, 1000), (630, 1000), (1000, 10000), (0, 10000))
BINS = ((3, 30), (30, 100), (100, 300), (300, 1000), (1000, 3000),
        (3000, 10000))
MIN_CELL = CV.MIN_CELL
CUBIC_BAND = (0.33, 0.45)     # T2: the degree-3 f, the kill's bar
TRIV_1000 = (0.96, 1.02)      # P5, the parent's F1 at p < 1000
TRIV_10K = (0.97, 1.00)       # P5, the parent's F1 at p < 10000
GEN_TOP = (1.0001, 0.0097)    # P5, the parent's F1 top band
REPRINT_TOL = 0.0015
SEED = 20260907


def ok(cond, msg):
    global CHECKS
    CHECKS += 1
    if not cond:
        print("  FAIL: " + msg)
        sys.exit(1)


def section(t):
    print("\n" + "=" * 72 + "\n" + t + "\n" + "=" * 72)
    sys.stdout.flush()


def fmt(x, d=3):
    return "--" if x is None else ("%%.%df" % d) % x


# ------------------------------------------------------------ the terms
def torsion(G):
    """|Cl[k]| for k <= KMAX, counted over the group's keys."""
    return {k: sum(1 for key in G.keys if G.mul(key, k) == G.triv)
            for k in range(1, KMAX + 1)}


def terms_deg2(rec, lo, hi, plist, tor):
    """Every prime-power term of (1) in the window: a list of
    (tag, w, landed, p) with landed the weight on the identity and p
    the identity's image share of (2)."""
    (field, D, G, qtype) = rec
    h = G.h
    out = []
    for q in plist:
        if q >= hi:
            break
        t, key = qtype(q)
        n, k = q, 1
        while n < hi:
            if n >= lo:
                if t == 1:
                    if k >= 2:
                        w = 1.0 / k
                        out.append(("split:%d:%d" % (q, k), w,
                                    w if G.mul(key, k) == G.triv else 0.0,
                                    tor[k] / float(h)))
                    elif q == 2:
                        out.append(("two:2:1", 1.0,
                                    1.0 if key == G.triv else 0.0,
                                    1.0 / h))
                elif t == -1:
                    if k % 2 == 0:
                        w = 1.0 / k
                        out.append(("inert:%d:%d" % (q, k), w, w, 1.0))
                else:
                    w = 0.5 / k
                    land = w if G.mul(key, k) == G.triv else 0.0
                    p = 1.0 if k % 2 == 0 else 1.0 / tor[2]
                    out.append(("ram:%d:%d" % (q, k), w, land, p))
            n *= q
            k += 1
    return out


def new_cell():
    return dict(ns=0, ntriv=0, W=0.0, landed=0.0, exp_t=0.0, var_t=0.0,
                forcing=0.0, dlog=0.0, sumlog=0.0, zero=0.0, nfield=0,
                forced=0.0, res=[], terms={})


def add_field(cell, rec, lo, hi, plist, tor):
    """One field's raw places and terms in the window folded into a
    stratum cell; returns (count, exp_u) for the field."""
    (field, D, G, qtype) = rec
    h = G.h
    ns = ntriv = 0
    sumlog = 0.0
    zero = 0
    for (p, key) in field[2]:
        if lo <= p < hi:
            ns += 1
            sumlog += math.log(p)
            if key == G.triv:
                ntriv += 1
            if D < 0 and 4 * p < -D:
                zero += 1
    W = landed = exp_t = var_t = forcing = dlog = forced = 0.0
    for (tag, w, land, p) in terms_deg2(rec, lo, hi, plist, tor):
        kind, q, k = tag.split(":")
        if D < 0 and p < 1.0 and 4 * int(q) ** int(k) < -D:
            zero += w * p * h
        if p >= 1.0:
            forced += w
        W += w
        landed += land
        exp_t += w * p
        var_t += w * w * p * (1 - p)
        forcing += w * (p - 1.0 / h)
        dlog += w * (p - 1.0 / h) * math.log(int(tag.split(":")[1]))
        t = cell['terms'].setdefault(tag, [0.0, 0.0, 0.0])
        t[0] += w
        t[1] += land
        t[2] += w * p
    if ns == 0 and W == 0.0:
        return None
    cell['ns'] += ns
    cell['ntriv'] += ntriv
    cell['sumlog'] += sumlog
    cell['zero'] += zero / float(h)
    cell['W'] += W
    cell['landed'] += landed
    cell['exp_t'] += exp_t
    cell['var_t'] += var_t
    cell['forcing'] += forcing
    cell['dlog'] += dlog
    cell['forced'] += forced
    cell['nfield'] += 1
    count = ntriv + landed
    exp_u = (ns + W) / float(h)
    cell['res'].append(count - exp_u)
    return count, exp_u


def strata_cells(recs, lo, hi, plist, tors):
    cells = {}
    for rec in recs:
        h = rec[2].h
        add_field(cells.setdefault(h, new_cell()), rec, lo, hi, plist,
                  tors[rec[1]])
    return cells


# ------------------------------------------------------------ the reads
def levels(cell, h):
    """The uniform and image levels with their bars, F, f, the nulls
    and the raw level of one stratum cell."""
    N = cell['ns'] + cell['W']
    count = cell['ntriv'] + cell['landed']
    exp_u = N / float(h)
    if exp_u <= 0:
        return None
    lu = count / exp_u
    sd_bin = math.sqrt(exp_u * (1 - 1.0 / h)) / exp_u
    r = cell['res']
    n = len(r)
    if n >= 2:
        mu = sum(r) / n
        sd_fld = math.sqrt(sum((x - mu) ** 2 for x in r) * n / (n - 1)
                           ) / exp_u
    else:
        sd_fld = sd_bin
    exp_i = cell['ns'] / float(h) + cell['exp_t']
    var_i = cell['ns'] * (1.0 / h) * (1 - 1.0 / h) + cell['var_t']
    li = count / exp_i
    zi = (count - exp_i) / math.sqrt(var_i) if var_i > 0 else 0.0
    F = cell['forcing'] / exp_u
    f = (lu - 1) / F if F > 0 else None
    sf = sd_fld / F if F > 0 else None
    sfb = sd_bin / F if F > 0 else None
    mean_log = cell['sumlog'] / cell['ns'] if cell['ns'] else None
    c_rs = ((cell['dlog'] / cell['forcing']) / mean_log
            if cell['forcing'] > 0 and mean_log else None)
    exp_raw = cell['ns'] / float(h)
    lr = cell['ntriv'] / exp_raw if exp_raw > 0 else None
    zr = ((cell['ntriv'] - exp_raw) / math.sqrt(exp_raw * (1 - 1.0 / h))
          if exp_raw > 0 else None)
    # the decomposition (7): 1 - f = (raw deficit + free deficit)/forcing
    A = cell['forced']
    b = cell['exp_t'] - A
    lfree = cell['landed'] - A
    frc = cell['forcing']
    rawdef = (exp_raw - cell['ntriv']) / frc if frc > 0 else None
    freedef = (b - lfree) / frc if frc > 0 else None
    floor = 1 - (exp_raw + b) / frc if frc > 0 else None
    return dict(lu=lu, sd_bin=sd_bin, sd_fld=sd_fld, li=li, zi=zi,
                exp_u=exp_u, exp_i=exp_i, F=F, f=f, sf=sf, sfb=sfb,
                c_rs=c_rs, lr=lr, zr=zr, zero=cell['zero'] / exp_u,
                count=count, N=N, nfield=cell['nfield'], rawdef=rawdef,
                freedef=freedef, floor=floor, A=A, b=b, R=exp_raw)


def pool_f(rows):
    """Inverse-variance mean of f over readable strata: (f, sigma)."""
    pts = [(L['f'], L['sf']) for L in rows
           if L is not None and L['f'] is not None and L['sf'] > 0]
    if not pts:
        return None, None
    w = [1.0 / (s * s) for (_, s) in pts]
    return (sum(wi * x for wi, (x, _) in zip(w, pts)) / sum(w),
            math.sqrt(1.0 / sum(w)))


def readable(cells, hmin=4):
    return sorted(h for h, c in cells.items()
                  if h >= hmin and (c['ns'] + c['W']) / float(h) >= MIN_CELL)


def print_table(tag, cells, keep):
    print("  %s  h   n  exp_u    L_u (fld;bin)      L_img  z_i     F"
          "   zero     f  +-fld (bin)  1-cRS   raw  | rawdef freedef"
          "  floor" % tag)
    rows = []
    for h in keep:
        L = levels(cells[h], h)
        rows.append(L)
        print("  %s %3d %3d %6.0f  %.3f (%.3f;%.3f)  %.3f %+5.1f  %.3f"
              "  %.3f  %s +-%s (%s)  %s  %.3f  | %s  %s  %s"
              % (tag, h, L['nfield'], L['exp_u'], L['lu'], L['sd_fld'],
                 L['sd_bin'], L['li'], L['zi'], L['F'], L['zero'],
                 fmt(L['f']), fmt(L['sf']), fmt(L['sfb']),
                 fmt(1 - L['c_rs'] if L['c_rs'] is not None else None, 2),
                 L['lr'], fmt(L['rawdef'], 2), fmt(L['freedef'], 2),
                 fmt(L['floor'], 2)))
    return rows


def source_table(cells, keep):
    """The by-source table pooled over the readable strata, per kind."""
    agg = defaultdict(lambda: [0.0, 0.0, 0.0])
    for h in keep:
        for tag, t in cells[h]['terms'].items():
            kind, q, k = tag.split(":")
            key = (kind, int(k))
            for i in range(3):
                agg[key][i] += t[i]
    print("    kind  k   weight   landed   expected(img)   landed/w  exp/w")
    for (kind, k) in sorted(agg):
        w, land, e = agg[(kind, k)]
        print("    %-5s %2d  %8.2f  %8.2f  %8.2f   %.3f  %.3f"
              % (kind, k, w, land, e, land / w if w else 0.0,
                 e / w if w else 0.0))


# ---------------------------------------------------------- the controls
def c0_shares(recs, plist, tors):
    section("C0  THE SHARES AGAINST THE GROUP")
    seen = set()
    worst_k = 0
    for rec in recs:
        (field, D, G, qtype) = rec
        if G.h in seen:
            continue
        seen.add(G.h)
        tor = tors[D]
        for k in range(1, KMAX + 1):
            ok(tor[k] == gcd(k, G.h),
               "C0: |Cl[%d]| = %d at h = %d, D = %d" % (k, tor[k], G.h, D))
            worst_k = max(worst_k, k)
        for (tag, w, land, p) in terms_deg2(rec, 0, 10000, plist, tor):
            kind, q, k = tag.split(":")
            if kind == "inert" or (kind == "ram" and int(k) % 2 == 0):
                ok(land == w and p == 1.0, "C0: a forced term not landed")
    print("  C0 PASSES: |Cl[k]| = gcd(k, h) on %d strata to k = %d; every"
          " forced term lands" % (len(seen), worst_k))


def c1_identity(recs, plist, tors):
    section("C1  THE WEIGHT IDENTITY against corr_deg2")
    worst = 0.0
    for (lo, hi) in WINDOWS:
        for rec in recs:
            G = rec[2]
            w, blind = SQ.corr_deg2(rec, lo, hi, plist)
            terms = terms_deg2(rec, lo, hi, plist, tors[rec[1]])
            worst = max(worst, abs(sum(t[1] for t in terms) - blind))
            worst = max(worst, abs(sum(t[2] for t in terms)
                                   - w.get(G.triv, 0.0)))
    ok(worst < 1e-9, "C1: identity off by %.3g" % worst)
    print("  C1 PASSES: by-source weights and the identity's landed weight"
          " agree with the parent to %.1e" % worst)


def c2_summand(recs, plist, tors, h):
    section("C2  THE SUMMAND BAR (2000 replicates at h = %d, p < 1000)" % h)
    rng = random.Random(SEED)
    fields = [rec for rec in recs if rec[2].h == h]
    draws = []
    for _ in range(2000):
        tot = 0.0
        for rec in fields:
            ns = sum(1 for (p, key) in rec[0][2] if p < 1000)
            for _ in range(ns):
                if rng.random() < 1.0 / h:
                    tot += 1
            for (tag, w, land, p) in terms_deg2(rec, 0, 1000, plist,
                                                tors[rec[1]]):
                if p >= 1.0 or rng.random() < p:
                    tot += w
        draws.append(tot)
    cell = new_cell()
    for rec in fields:
        add_field(cell, rec, 0, 1000, plist, tors[rec[1]])
    L = levels(cell, h)
    mu = sum(draws) / len(draws)
    sd = math.sqrt(sum((x - mu) ** 2 for x in draws) / (len(draws) - 1))
    var_i = cell['ns'] * (1.0 / h) * (1 - 1.0 / h) + cell['var_t']
    print("  replicate mean %.2f against exp_img %.2f; spread %.3f against"
          " summand sd %.3f (Poisson %.3f)"
          % (mu, L['exp_i'], sd, math.sqrt(var_i), math.sqrt(L['exp_i'])))
    ok(abs(sd - math.sqrt(var_i)) < 0.15 * math.sqrt(var_i),
       "C2: replicate spread off the summand sd")
    print("  C2 PASSES")


def c3_positive(recs, plist, tors, keep):
    section("C3  THE POSITIVE CONTROL: f at its two nulls")
    rng = random.Random(SEED + 1)
    cells1, cells0 = {}, {}
    for rec in recs:
        h = rec[2].h
        if h not in keep:
            continue
        tor = tors[rec[1]]
        for which, cells in ((1, cells1), (0, cells0)):
            cell = cells.setdefault(h, new_cell())
            ns = sum(1 for (p, key) in rec[0][2] if p < 1000)
            terms = terms_deg2(rec, 0, 1000, plist, tor)
            W = sum(t[1] for t in terms)
            landed = sum(t[2] for t in terms)
            forcing = sum(t[1] * (t[3] - 1.0 / h) for t in terms)
            if which == 1:
                ntriv = sum(1 for _ in range(ns) if rng.random() < 1.0 / h)
                landed = sum(t[1] for t in terms
                             if t[3] >= 1.0 or rng.random() < t[3])
            else:
                ntriv = (ns + W) / float(h) - landed
            cell['ns'] += ns
            cell['ntriv'] += ntriv
            cell['W'] += W
            cell['landed'] += landed
            cell['forcing'] += forcing
            cell['nfield'] += 1
            cell['res'].append(ntriv + landed - (ns + W) / float(h))
    for which, cells, target in ((1, cells1, 1.0), (0, cells0, 0.0)):
        rows = [levels(cells[h], h) for h in keep]
        f, sf = pool_f(rows)
        fb = pool_f([dict(f=L['f'], sf=L['sfb']) for L in rows])[1]
        print("  null %d: pooled f %.3f +- %.3f (field) +- %.3f (binomial)"
              % (which, f, sf, fb))
        if which == 1:
            ok(abs(f - target) < 2 * fb, "C3: the uniform draw's f off 1")
        else:
            ok(abs(f - target) < 1e-9, "C3: the exact deficit's f off 0")
    print("  C3 PASSES: the statistic separates its nulls here")


# --------------------------------------------------------------- main
def read_sign(sign, bound, plist, tag):
    section("THE %s POPULATION (the parent's sweep to %d)"
            % ("IMAGINARY" if sign < 0 else "REAL NARROW", bound))
    recs = SQ.deg2_records(sign, bound, plist)
    tors = {rec[1]: torsion(rec[2]) for rec in recs}
    cnt = defaultdict(int)
    for rec in recs:
        cnt[rec[2].h] += 1
    print("  %d admissible fields; strata %s"
          % (len(recs), dict(sorted(cnt.items()))))
    c0_shares(recs, plist, tors)
    c1_identity(recs, plist, tors)
    base = strata_cells(recs, 0, 1000, plist, tors)
    keep = readable(base)
    print("  readable strata at h >= 4 over p < 1000: %s" % keep)
    c2_summand(recs, plist, tors, keep[0])
    c3_positive(recs, plist, tors, keep)

    out = {}
    for (lo, hi) in WINDOWS:
        section("%s  WINDOW [%d, %d): the principal class by stratum"
                % (tag, lo, hi))
        cells = strata_cells(recs, lo, hi, plist, tors)
        kp = readable(cells)
        rows = print_table(tag, cells, kp)
        f, sf = pool_f(rows)
        fb = pool_f([dict(f=L['f'], sf=L['sfb']) for L in rows])[1]
        Fm = sum(L['F'] for L in rows) / len(rows) if rows else None
        crs = [1 - L['c_rs'] for L in rows if L['c_rs'] is not None]
        print("  -> pooled f over h >= 4: %s +- %s (field; binomial %s),"
              " mean F %s, 1 - c_RS %s to %s"
              % (fmt(f), fmt(sf), fmt(fb), fmt(Fm),
                 fmt(min(crs), 2) if crs else "--",
                 fmt(max(crs), 2) if crs else "--"))
        if 2 in cells and (cells[2]['ns'] + cells[2]['W']) / 2.0 >= MIN_CELL:
            print_table(tag + " h=2", cells, [2])
        if (lo, hi) == (0, 1000):
            print("  the by-source table pooled over the readable strata:")
            source_table(cells, kp)
        out[(lo, hi)] = dict(rows=rows, keep=kp, f=f, sf=sf, fb=fb,
                             crs=crs)
        if sign < 0 and lo >= 630 and lo < 1000:
            sub = [rec for rec in recs if -rec[1] < 4 * lo]
            cs = strata_cells(sub, lo, hi, plist, tors)
            ks = readable(cs)
            print("  the %d fields with |D| < %d, past the hard zero:"
                  % (len(sub), 4 * lo))
            rs = print_table(tag + " nz", cs, ks)
            fz, sz = pool_f(rs)
            print("  -> pooled f %s +- %s" % (fmt(fz), fmt(sz)))

    section("%s  THE RAW PRINCIPAL LEVEL BY BIN (no powers), pooled over"
            " the readable strata" % tag)
    bins = []
    for (lo, hi) in BINS:
        cells = strata_cells(recs, lo, hi, plist, tors)
        ntriv = sum(cells[h]['ntriv'] for h in keep if h in cells)
        exp = sum(cells[h]['ns'] / float(h) for h in keep if h in cells)
        var = sum(cells[h]['ns'] * (1.0 / h) * (1 - 1.0 / h)
                  for h in keep if h in cells)
        zero = sum(cells[h]['zero'] for h in keep if h in cells)
        lr = ntriv / exp if exp else None
        sd = math.sqrt(var) / exp if exp else None
        forced = sum(cells[h]['landed'] for h in keep if h in cells)
        kb = readable(cells)
        rows = [levels(cells[h], h) for h in kb]
        fb, sfb = pool_f(rows)
        Fm = sum(L['F'] for L in rows) / len(rows) if rows else None
        rd = sum(L['rawdef'] for L in rows) / len(rows) if rows else None
        fd = sum(L['freedef'] for L in rows) / len(rows) if rows else None
        r2 = levels(cells[2], 2) if 2 in cells else None
        print("  [%5d, %5d)  raw %s +- %s   hard-zero mass %.3f of exp"
              "   landed weight %.1f   strata %s: F %s  f %s +- %s"
              " (rawdef %s freedef %s)   h=2: F %s f %s +- %s"
              % (lo, hi, fmt(lr), fmt(sd), zero / exp if exp else 0.0,
                 forced, kb, fmt(Fm), fmt(fb), fmt(sfb), fmt(rd, 2),
                 fmt(fd, 2),
                 fmt(r2['F']) if r2 else "--", fmt(r2['f']) if r2 else "--",
                 fmt(r2['sf']) if r2 else "--"))
        bins.append((lr, sd))
    out['bins'] = bins
    out['recs'] = recs
    out['tors'] = tors
    return out


def cubic_table():
    """The same decomposition on the cubic sibling's kept walks, by bin
    and over [3, 1000), the readable strata prime to 3 off the
    degenerate regime; skipped with a notice when the checkpoints are
    gone (a fresh walk is the sibling's two hours, not this file's)."""
    section("THE CUBIC POPULATION, the same decomposition from"
            " explore_triple_image_level.py's kept walks")
    import tempfile
    ck = os.path.join(tempfile.gettempdir(), "image_level_96000")
    if not all(os.path.exists(os.path.join(ck, "walk%d.json" % i))
               for i in range(6)):
        print("  no checkpoints under %s: the cubic table is the frozen"
              " record's" % ck)
        return
    argv = sys.argv
    sys.argv = [argv[0]]
    import explore_triple_image_level as IL
    import explore_triple_cube_term as CT
    sys.argv = argv
    import json
    sel = [json.load(open(os.path.join(ck, "walk%d.json" % i)))
           for i in IL.NEW]          # the walks alone; the readings stay
    keys = set()
    for data in sel:
        keys.update(IL.key_of(k) for k in data['nfields'])
    for bins, name in (((0,), "[3, 30)"), ((1,), "[30, 100)"),
                       ((2,), "[100, 300)"), ((3,), "[300, 1000)"),
                       (None, "[3, 1000)")):
        print("  cubic %-12s  h    R    n3      A       B      b  landed_free"
              "  forcing    F     f +-sf   rawdef freedef  floor" % name)
        for key in sorted(keys):
            if key[1] == 'D' or key[0] % 3 == 0:
                continue
            L = IL.levels(sel, key, bins)
            if L is None or L['exp_u'] < IL.MIN_READ:
                continue
            g = L['g']
            A = sum(t[1] for t in g['terms'].values()
                    if abs(t[2] - t[0]) < 1e-9)
            B = sum(t[0] for t in g['terms'].values()) - A
            b = g['exp'] - A
            lf = (L['count'] - L['n3']) - A
            R = L['ns'] * CT.share_of(*key)
            frc = g['forcing']
            print("  cubic %-12s %2d %6.1f %6.1f %7.1f %7.1f %6.1f %8.1f"
                  "  %8.1f  %5.2f  %+.2f+-%.2f   %.2f   %.2f   %+.2f"
                  % (name, key[0], R, L['n3'], A, B, b, lf, frc, L['F'],
                     L['f'], L['sf'], (R - L['n3']) / frc, (b - lf) / frc,
                     1 - (R + b) / frc))


def main():
    t0 = time.time()
    plist = primes_upto(CO.PCAP)
    res = {}
    res[-1] = read_sign(-1, 4000, plist, "imag")
    res[+1] = read_sign(+1, SQ.DBOUND_REAL, plist, "real")

    section("C4 / P5  THE REPRINT through the parent's reader")
    recs_i = res[-1]['recs']
    fields_i = [r[0] for r in recs_i]
    keep_i, keep_ib = CV.frozen_strata(fields_i, CV.CUTS, CV.BANDS)
    keep_ib = [h for h in keep_ib if CV.is_composite(h)]

    def places2(rec):
        return rec[0][2]

    def G2(rec):
        return rec[2]

    def corr2(rec, lo, hi):
        return SQ.corr_deg2(rec, lo, hi, plist)
    r = SQ.read_both(recs_i, keep_ib, [SQ.TOP], "imag", places2, corr2, G2)
    mu, se = r[SQ.TOP][1]
    ok(abs(mu - GEN_TOP[0]) < REPRINT_TOL and abs(se - GEN_TOP[1]) < 0.001,
       "C4: the generator top band does not reprint")
    print("  C4 PASSES: the generator top band reprints %.4f +- %.4f"
          % (mu, se))
    for (win, band) in (((0, 1000), TRIV_1000), ((0, 10000), TRIV_10K)):
        rows = res[-1][win]['rows']
        keep = res[-1][win]['keep']
        vals = [(h, L['lu']) for h, L in zip(keep, rows)
                if 6 <= h <= 14 and CV.is_composite(h)]
        lo_, hi_ = min(v for _, v in vals), max(v for _, v in vals)
        print("  P5 window %s: L_u over h = 6..14 composite runs %.3f to"
              " %.3f against the parent's %.2f to %.2f"
              % (win, lo_, hi_, band[0], band[1]))
        print("      %s" % ("PASS" if lo_ > band[0] - 0.01
                            and hi_ < band[1] + 0.01 else "FAIL"))

    section("THE SLATE READ")
    # P1: both signs pooled at p < 1000
    both = []
    for s in (-1, +1):
        both.extend(res[s][(0, 1000)]['rows'])
    f, sf = pool_f(both)
    inband = (f - 2 * sf <= CUBIC_BAND[1]) and (f + 2 * sf >= CUBIC_BAND[0])
    print("  P1 f pooled over both signs, h >= 4, p < 1000: %.3f +- %.3f;"
          " the cubic band [%.2f, %.2f] is %s 2 sigma"
          % (f, sf, CUBIC_BAND[0], CUBIC_BAND[1],
             "WITHIN" if inband else "OUTSIDE"))
    print("     -> %s" % ("KILL: f is the formula's, the seat is not the"
                         " cause" if inband else
                         "the kill does not fire"))
    z0 = f / sf
    print("     f against 0: z %+.2f; against the band's centre 0.39:"
          " z %+.2f" % (z0, (f - 0.39) / sf))
    # P2
    worst = 0.0
    off = []
    for s in (-1, +1):
        for h, L in zip(res[s][(0, 1000)]['keep'], res[s][(0, 1000)]['rows']):
            z = L['f'] / L['sf']
            worst = max(worst, abs(z))
            if abs(z) > 2:
                off.append((s, h, round(L['f'], 3), round(L['sf'], 3)))
    print("  P2 per-stratum f at p < 1000: largest |z| from 0 is %.2f;"
          " strata past 2 sigma: %s" % (worst, off or "none"))
    for s in (-1, +1):
        for win in WINDOWS:
            f_, sf_ = res[s][win]['f'], res[s][win]['sf']
            print("     %s %-14s pooled f %s +- %s  z %s"
                  % ("imag" if s < 0 else "real", str(win), fmt(f_),
                     fmt(sf_), fmt(f_ / sf_ if f_ is not None else None, 2)))
    # P3
    for s in (-1, +1):
        r_ = res[s][(0, 1000)]
        cmin = min(r_['crs']) if r_['crs'] else None
        d = (cmin - r_['f']) / r_['sf'] if cmin is not None else None
        print("  P3 %s: the least 1 - c_RS %s sits %s sigma above the pooled"
              " f" % ("imag" if s < 0 else "real", fmt(cmin, 2), fmt(d, 1)))
    # P4
    bi, br = res[-1]['bins'], res[+1]['bins']
    rising = all(bi[i][0] < bi[i + 1][0] for i in range(len(bi) - 1))
    d = ((br[0][0] - bi[0][0]) / math.sqrt(br[0][1] ** 2 + bi[0][1] ** 2)
         if bi[0][0] is not None and br[0][0] is not None else None)
    print("  P4 imaginary raw by bin %s; [3, 30) %s (< 0.30: %s);"
          " [1000, 3000) %s (within 0.10 of 1: %s); real above imaginary"
          " in [3, 30) by %s sigma"
          % ("rises monotonically" if rising else "does NOT rise"
             " monotonically", fmt(bi[0][0]), bi[0][0] < 0.30,
             fmt(bi[4][0]), abs(bi[4][0] - 1) < 0.10, fmt(d, 1)))

    del recs_i, fields_i
    res[-1]['recs'] = res[+1]['recs'] = None
    gc.collect()
    cubic_table()

    print("\n%d checks passed, %.1f s wall" % (CHECKS, time.time() - t0))


if __name__ == "__main__":
    main()
