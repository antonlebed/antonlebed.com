r"""THE EARLY PRIMES -- are the two residuals the generator ceiling leaves
standing both counts of a field's SMALLEST primes? (sibling of
explore_ceiling_constant.py, whose populations, corrections and residual
statistic it imports whole and reads in WINDOWS of the norm rather than
at cumulative cuts.)

THE QUESTION. With the explicit formula's prime-power term put back, two
residuals stand (explore_ceiling_constant.py F2, F3), and both are fixed
COUNTS of primes rather than shares: the cubic partial fiber's
generator-cell excess is 3.0, 3.5, 4.3, 3.8 +- 0.3..0.7 primes per field
at the cuts 250, 400, 630, 1000 -- in place by cut 250 and flat after --
and over a 512-fold lever on D at a fixed narrow class number the real
quadratic trivial class's residual count rises with log D by 0.05 to
0.10 primes per unit at p <= 100 and by 0.14 to 0.35 at p < 1000, a
grading that LENGTHENS with the cut. Neither is derived. Both have the
shape of something accrued at the start of the norm order: a count that
is complete early and never repaid, and a count whose reach grows with
the field's size. This file asks WHERE in the norm order each count sits
-- which primes carry it -- by reading the same residual statistic over
disjoint windows of p, and over the RANK of a place in its field's own
norm order.

THE HAND-ATTACK (pre-engine, on paper).

  (1) THE WINDOW STATISTIC IS ADDITIVE. The residual of a class over
      [lo, hi) is its counted places in the window plus its prime-power
      weight there, minus the corrected total over h; every piece is a
      sum over the window, so the residuals over a partition of [0, x)
      sum exactly to the residual over [0, x). An increment read over a
      window is therefore the same statistic the cumulative reads were,
      and carries the same identity: a planted place moves its own
      class by 1 - 1/h and each sibling by -1/h, in its own window and
      in no other. (Controlled, C2 and C4.)

  (2) THE RANK STATISTIC. Sort a field's partial places by norm; at
      rank r the indicator "lies in a generating class" has expectation
      phi(h)/h under the uniform nominal, so the excess at rank r is the
      mean over fields of (indicator - phi(h)/h), a Bernoulli mean with
      standard error about sqrt(s(1-s)/N) -- 0.10 at N = 24, 0.045 at N
      = 120. The cumulative excess at cut x is the sum of the rank
      excesses over the ranks that sit below x, so a 3-prime excess held
      by the first six ranks reads +0.5 per rank, and one spread over
      forty reads +0.08 and is invisible rank by rank. The rank read
      answers the question the window read cannot: whether the count is
      the field's least norms, whatever p they sit at.

  (3) WHAT A GEOMETRY-OF-NUMBERS ORIGIN WOULD PREDICT. Every class holds
      an ideal of norm below the Minkowski bound, 0.283 sqrt|d| for a
      complex cubic field -- below 22 over the base population (|d| <=
      6000) -- and the primes below it generate the group. That
      conditioning forces AT LEAST one generator among the smallest
      primes and nothing about how many; it is a fraction of a prime per
      field, not three, so if the count sits below p = 20 something
      beyond generation is at work, and if it sits at p in the hundreds
      the bound is not the mechanism. The real quadratic early start,
      as explore_ceiling_constant.py F3 reads it, is the principal cycle's small leading
      coefficients -- norms below sqrt(D)/2 -- which at a fixed narrow
      group puts the trivial class's count on a window that ENDS at
      sqrt(D)/2 and moves with the field: read in units of sqrt(D) the
      increments would not depend on the band at all, and read in
      absolute p the band (2000, 4000), whose sqrt(D)/2 is 22 to 32,
      would accrue nothing above p = 100 while the band (512000,
      1024000), whose sqrt(D)/2 is 360 to 500, would accrue most of its
      count there. The conductor term of the explicit formula, by
      contrast, is (1/2) log D / log x primes at EVERY x -- complete at
      the first primes and a function of the cut only through log x --
      and puts no count in any window that moves with D.
      TRANSPLANT, marked: "the early start" is a reading of the degree-2
      real side, and it is carried to the cubic generator cell
      only as the question of WHERE the count sits, never as a
      prediction that the two sit at the same p.

  (4) WHAT MOVES THE DENOMINATORS. A window increment is a mean over
      fields of a per-field count with binomial spread sqrt(n_w /h) for
      n_w places in the window, so the narrow windows carry the smaller
      spreads and the read is most precise exactly where the count is
      claimed to sit. The scaled windows are truncated at the lever's cap
      of 1000, which empties [2 sqrt D, 1000) for the top band (sqrt D
      above 715) -- an empty window reads zero and is excluded from any
      pooled statistic, never counted as a zero increment. Every
      prediction is frozen on the window's own bar.

THE DESIGN. The cubic side on two populations: the BASE population of
explore_ceiling_constant.py P2 (|d| <= 6000, 24 admissible fields at h =
4 and 6, the reprint) and the WIDE population of explore_ceiling_topband.py
(the same box and its increment, read at h = 4, 6, 8, every group in it
cyclic) -- the partial fiber, one place per prime, the prime-power weights
of explore_ceiling_squares.py, the generator cell the classes of order h.
Windows [0, 20), [20, 50), [50, 100), [100, 250), [250, 500), [500, 1000);
ranks 1 to 10, and the pooled excess over ranks 1-3, 4-6 and 7-10. The
real side on the |D| LEVER of explore_ceiling_constant.py (the same seed,
stride and cells: five bands from (2000, 4000) to (512000, 1024000), up
to 200 fields per (band, h+) at h+ = 2, 4, 8, places below 1000), the
trivial class's residual read over the absolute windows [0, 100), [100,
250), [250, 500), [500, 1000) and the scaled windows [0, 1/4), [1/4,
1/2), [1/2, 1), [1, 2), [2, ...) in units of sqrt D, each truncated at
1000, per (band, h+) and regressed on log D per window.

THE SLATE -- PREDICTIONS FROZEN BEFORE THE ENGINE.

  P1  THE CUBIC COUNT SITS LOW. On the base population the generator-cell
      excess over [0, 50) is positive at 2 sigma or more and is at least
      0.6 of the cumulative excess at cut 250.
  P2  THE CUBIC COUNT IS THE LEAST NORMS. On the base population the
      generator share at ranks 1-3 pooled exceeds phi(h)/h by 0.15 or
      more, at 2 sigma or more.
  P3  THE WIDE REPLICATION. P1's and P2's brackets hold on the wide
      population at h = 4, 6, 8 pooled, with the same bars.
  P4  THE REAL COUNT ENDS AT sqrt(D)/2. Pooled over the lever at each of
      h+ = 4 and 8, the trivial class's increment over [sqrt(D)/2, 1000)
      lies within 2 sigma of zero, and its increment over [sqrt(D)/4,
      sqrt(D)/2) is positive at 3 sigma or more.
  P5  THE BANDS PART IN ABSOLUTE p. At h+ = 8 the trivial class's
      increment over [100, 1000) lies within 2 sigma of zero in the band
      (2000, 4000) and is positive at 3 sigma or more in the band
      (512000, 1024000).

THE CONTROLS, run before any prediction is read.

  C1  THE NULL. Every place re-sorted to a uniformly random class of its
      own group (one seeded draw), no correction: every cubic window
      increment, every rank excess and every pooled scaled increment
      must read within 3 sigma of zero.
  C2  ADDITIVITY. Over every field, the window increments sum to the
      cumulative residual at the cut to 1e-9 -- the absolute partition to
      [0, 1000) on both sides, the scaled partition to [0, 1000) on the
      real side.
  C3  THE REPRINT. The base population's generator excess at cut 250
      reprints +3.01 +- 0.33 inside 0.02, and the lever's h+ = 8 slope
      at p < 1000 reprints +0.351 inside 0.005.
  C4  THE PLANTED PLACE. One synthetic generator-class place at p = 7 in
      every base field moves the [0, 20) increment by exactly 1 - phi(h)/h
      times one field's share and every other window by exactly zero, to
      1e-9; one synthetic trivial place at p = 3 in every lever field
      does the same to the [0, 100) window with 1 - 1/h.
  C5  THE GENERATION-CONDITIONED NULL -- the confound priced rather than
      argued (added after the first run, before P2 was read as a finding;
      the slate untouched). The class group is GENERATED by the prime
      ideals of norm below the Minkowski bound M = (4/pi)(3!/3^3)
      sqrt|d| = 0.283 sqrt|d| -- 21.9 at the base population's cap and
      43.8 at the wide one -- so a field whose sub-bound places are few
      carries a generator among them BY CONSTRUCTION, and the rank-1
      excess of P2 is partly that conditioning whatever the arithmetic
      does. This null draws every PARTIAL place's class uniformly (the
      split fiber kept as it is, its triples being sum-constrained) and
      REJECTS the draw unless the sub-bound places generate the group --
      the sub-bound set being, per prime p with p <= M, a split prime's
      three classes, a partial prime's degree-1 class, and its degree-2
      class (the inverse, when p^2 <= M) -- then reads the same rank and
      window statistics over the accepted draws. The finding is what
      SURVIVES this null, and the null's own rank-1 excess is printed as
      the confound's measured size. THE NULL IS AN UPPER BOUND ON THE
      CONFOUND AND NOT AN ESTIMATE OF IT: the RAMIFIED places below the
      bound generate too, and the parent rig computes no class for them,
      so this condition demands generation from a SUBSET of the true
      generating set and leans on the drawn classes harder than the
      arithmetic does. The per-field acceptance rate is printed; a field
      whose sub-bound set cannot generate under ANY draw -- a field the
      omitted ramified places carry -- is excluded and counted there.

THE FINDINGS (the post-run record; every number is a print of the run).

  CONTROLS. C2: both real partitions sum to the cut-1000 residual (worst
  1.5e-14 over 2793 fields) and the cubic partition to the cut-1000
  excess (4.4e-15). C3: the h+ = 8 slope at p < 1000 reprints +0.3513 +-
  0.0378 and the cubic cut-250 excess +3.013 +- 0.328. C4: the planted
  place moves its own window by 1 - 1/h (real) and 1 - phi(h)/h (cubic)
  and every other window by zero, exactly (worst 1.3e-15 and 6.7e-16).
  C1: every pooled real scaled increment and every cubic window and rank
  within 3 sigma of zero (largest |z| 2.06). C5: acceptance 0.513 on the
  base population and 0.639 on the wide one, one field excluded from each
  (the ramified places the parent leaves unclassed); the conditioning's
  own rank-1 excess is +0.037 +- 0.007 on the base and +0.009 +- 0.006 on
  the wide, ranks 1-3 pooled +0.035 +- 0.004 and +0.007 +- 0.003 -- and
  it sits ENTIRELY in [0, 20) (+0.106 +- 0.013, every window above it
  within 1.3 sigma of zero), which is where the bound acts. THE NULL'S
  BARS ARE DRAW-TO-DRAW OVER A FIXED FIELD SET and not field-to-field:
  each field contributes 200 accepted draws (40 on the wide), so the
  means are equally weighted and unbiased while their standard errors,
  computed over draws, are understated by the within-field correlation.
  They are read here as a SIZE against an effect ten to thirty times
  larger, never as a test.


  F1  P1 FAILS AND TAKES P3's WINDOW HALF WITH IT: THE CUBIC COUNT IS
      SPREAD TO 250, NOT CONCENTRATED BELOW 50 (observation). The
      generator-cell excess per field by window, base population (24
      fields at h = 4, 6) then wide (185 at h = 4, 6, 8) --
        [0, 20)     +0.972 +- 0.175      +0.671 +- 0.051
        [20, 50)    +0.669 +- 0.238      +0.234 +- 0.071
        [50, 100)   +0.472 +- 0.192      +0.417 +- 0.074
        [100, 250)  +0.900 +- 0.287      +0.668 +- 0.131
        [250, 500)  +0.752 +- 0.411      +0.417 +- 0.153
        [500, 1000) +0.028 +- 0.579      -0.030 +- 0.190
      so [0, 50) holds +1.641 +- 0.261 against the frozen bar of 0.6 x
      the cut-250 excess = 1.81, and +0.895 +- 0.086 against 1.19 on the
      wide population: the count is low but not that low, and it CLOSES
      inside the range -- the wide population's top window reads -0.030
      +- 0.190, where the base population's +0.028 +- 0.579 has a bar too
      wide to say anything and is not read as a zero.

  F2  P2 PASSES AND REPLICATES: THE COUNT IS SEATED AT THE FIELD'S LEAST
      PLACES, READ BY RANK (observation; 185 wide fields, each stratum
      separately -- CYCLIC groups only, the wide population's five Klein
      and four Z/2 x Z/4 fields holding no class of order h and so no
      generator cell to read). The generator share minus phi(h)/h by rank of the
      partial place in its own field's norm order -- the fiber is built on
      ODD primes (the parents' convention: 2 carries no counted place and
      no allocated weight), so rank 1 is the least partial place above 2
      -- wide pooled: +0.283 +-
      0.032 at rank 1, then 0.180, 0.148, 0.083, 0.126, 0.115 through
      rank 6 and 0.088, 0.056, 0.094, 0.067 through rank 10; pooled
      +0.204 +- 0.017 over ranks 1-3, +0.108 +- 0.022 over 4-6, +0.076 +-
      0.018 over 7-10. By stratum, ranks 1-3: +0.190 +- 0.023 (h = 4, 101
      fields), +0.231 +- 0.025 (h = 6, 65), +0.184 +- 0.065 (h = 8, 19).
      The base population reads +0.375 +- 0.075 at rank 1 and +0.292 +-
      0.051 over ranks 1-3. Against C5's upper bound on the Minkowski
      conditioning (+0.037 and +0.009 at rank 1) the seat survives with a
      tenth to a thirtieth of it conceded, and the null's own excess lives
      below p = 20 where the measured excess runs to rank 10.
      A SECOND ARGUMENT FOR THE LEAST-NORMS SEAT SURVIVES AT ONE
      STRATUM ONLY. Pooled, the [0, 50) excess falls with the
      discriminant -- -0.439 +- 0.138 primes per unit of log|d| where the
      cut-250 excess is flat (-0.283 +- 0.225), which is what a count
      riding the least norms does as those norms grow with |d|. Per
      stratum that fall is ENTIRELY h = 4's: -0.721 +- 0.162 over 101
      fields, against +0.116 +- 0.286 at h = 6 (65 fields, a bar that
      would show -0.7 at 2.4 sigma, so the absence is read) and +0.553 +-
      0.597 at h = 8 (19 fields, unreadable). The h COMPOSITION is not
      the reason -- h and log|d| correlate at +0.128 over the 185 fields,
      measured rather than assumed -- so the pooled slope is one stratum
      showing through and not a population law. The RANK read, which
      holds at every stratum, is what carries the seat; why h = 4 alone
      should shed its low window is left open.

  F3  P5 PASSES: THE REAL COUNT'S WINDOW MOVES OUTWARD WITH |D|
      (observation, 2793 lever fields). At h+ = 8 the trivial class's
      residual count above p = 100 is -0.037 +- 0.209 in the band (2000,
      4000) and +1.276 +- 0.141 in the band (512000, 1024000) -- the top
      band 9.1 sigma from zero and the two bands 5.2 sigma apart --
      while the [0, 100) window rises only from +0.354 +- 0.090 to
      +1.056 +- 0.064. The conductor constant is complete at the
      first primes and graded only by log x, so the x-independent term is
      refuted on its LOCATION as well as on the size and shape
      explore_ceiling_constant.py F1 and F3 refuted it on.

  F4  P4 FAILS: THE COUNT DOES NOT END AT sqrt(D)/2, AND sqrt(D) IS NOT
      THE SCALE (observation). Above sqrt(D)/2 the increment is +0.479 +-
      0.081 at h+ = 4 and +0.541 +- 0.063 at h+ = 8 (the frozen
      prediction was zero within 2 sigma), and the [sqrt(D)/4, sqrt(D)/2)
      window is positive as predicted (+0.277 +- 0.031, +0.236 +- 0.030).
      In units of sqrt(D) every window's increment still RISES with
      log|D| -- 0.161, 0.180, 0.219 primes per unit over [0, sqrt(D)/4)
      at h+ = 2, 4, 8, against 0.02 to 0.09 over the three BOUNDED
      windows above it, the outermost being cut off by the lever's own
      cap -- so the principal cycle's small-coefficient range is where the
      count is densest and is not its boundary. What stands is a count
      whose REACH grows with the field, nowhere zero below 1000.

  F5  THE TWO RESIDUALS ARE NOT ONE COAT (the read the file was built for).
      The cubic count is CLOSED and seated in its field's own norm order:
      a fixed number of the least places, its excess decaying over their
      rank and complete by p = 500. The real count is OPEN in absolute p
      and in units of sqrt(D) alike: still accruing at the cut, its window
      moving outward with |D|, with no scale in the field that bounds it.
      Both are "early"; only one of them finishes. The shared-coat reading
      the parent left as a hunch is refuted, and each front stands
      separately -- what seats a generating class at the least norms, and
      what sets the real count's growing reach.

WHAT IS NOT CONTROLLED. The mechanism: a count found to sit at the least
norms is a location, and the derivation of its size is not attempted
here. The wide population's |d| reach (to 24000, explore_ceiling_topband.py)
doubles the Minkowski bound from the base population's cap, which is
printed beside the rank read and not predicted.

RUN RECORD. 2026-08-20, Windows 11, Python 3, `python
prime/code/memwatch.py --limit 512 prime/code/explore_ceiling_early.py`.
One process, CPython, no BLAS. 8 checks passed, 956.0 s wall, peak working
set 264.7 MB against the 512 MB ceiling. Rehearsed first at a tenth of the
lever with the wide population skipped (206 s), which caught a window the
verdict asked for and the tables never built. Five full runs of the same
day: the first scored the slate without C5; the second was C5's own first
attempt, halted by a hard assert on the one field whose sub-bound set
cannot generate without the ramified places (the assert became the
exclusion print, and the null's direction was read off the omission); the
third scored the record; the fourth added the per-stratum |d| slopes and
the h/log|d| correlation an audit round demanded of the pooled slope; the
fifth, this one, only renames a null table's rows from fields to accepted
draws. No number moved across the five runs -- the lever population and
both nulls are seeded and drawn in the same order, and all 585 signed
statistics of the fourth run reprint identically in the fifth.
"""

import os
os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")

import gc
import random
import sys
import time
from collections import defaultdict
from math import isqrt, log, sqrt

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import explore_ceiling_squares as SQ               # noqa: E402
import explore_ceiling_curve as CV                 # noqa: E402
import explore_ceiling_constant as EC              # noqa: E402
import explore_class_order as CO                   # noqa: E402
from explore_principal_share import primes_upto    # noqa: E402

CHECKS = 0
EDGES3 = (0, 20, 50, 100, 250, 500, 1000)
EDGES2 = (0, 100, 250, 500, 1000)
SCALED = ((0.0, 0.25), (0.25, 0.5), (0.5, 1.0), (1.0, 2.0), (2.0, None))
CAP2 = EC.LEVER_CAP                  # 1000
RANKS = 10
RANK_POOLS = ((1, 3), (4, 6), (7, 10))
WIDE_H = (4, 6, 8)
SEED = 20883
REPRINT_CUBIC = (3.01, 0.02)
REPRINT_SLOPE = (0.351, 0.005)
QUICK = os.environ.get("EARLY_QUICK") == "1"     # the rehearsal: no wide
if QUICK:                            # a tenth of the lever, no reprint
    EC.NSCAN, EC.NCELL = 150, 20


def ok(cond, msg):
    global CHECKS
    CHECKS += 1
    if not cond:
        print("  FAIL: " + msg)
        sys.exit(1)


def section(t):
    print("\n" + "=" * 72 + "\n" + t + "\n" + "=" * 72)


mean_se = CV.mean_se
fmt = EC.fmt


def windows_of(edges):
    return [(edges[i], edges[i + 1]) for i in range(len(edges) - 1)]


def gen_share(G):
    return sum(1 for k in G.keys if G.order[k] == G.h) / float(G.h)


# --------------------------------------------------------- cubic reads
def cubic_rows(recs, plist, keep, scramble=None, plant=None):
    """Per field: the generator-cell excess per absolute window and at
    cut 250, and the generator indicator by rank. plant = (p, 'gen')
    adds one synthetic generator-class place to every field."""
    rows = []
    for rec in recs:
        G = rec['G']
        if G.h not in keep:
            continue
        gens = [k for k in G.keys if G.order[k] == G.h]
        if not gens:
            continue
        places = list(rec['field'][2])
        if scramble is not None:
            places = [(p, scramble.choice(G.keys)) for (p, key) in places]
        if plant is not None:
            places.append((plant, gens[0]))
            places.sort()
        share = len(gens) / float(G.h)
        per = {}
        for (lo, hi) in windows_of(EDGES3) + [(0, 50), (0, 250), (0, 1000)]:
            if scramble is not None:
                w, blind = {}, 0.0
            else:
                w, blind, _ = SQ.corr_deg3(rec, lo, hi, plist, 'partial')
            res, tot = EC.residuals(places, G, lo, hi, w, blind)
            per[(lo, hi)] = (sum(res[k] for k in gens), tot)
        ranks = [(1.0 if key in gens else 0.0) - share
                 for (p, key) in sorted(places)[:RANKS]]
        rows.append(dict(h=G.h, d=rec['d'], per=per, ranks=ranks,
                         share=share))
    return rows


def cubic_table(rows, tag, unit="fields"):
    print("  %s: generator-cell excess per field by window (%d %s,"
          " h %s)" % (tag, len(rows), unit,
                      sorted(set(r['h'] for r in rows))))
    out = {}
    for wnd in windows_of(EDGES3) + [(0, 50), (0, 250), (0, 1000)]:
        vals = [r['per'][wnd][0] for r in rows if r['per'][wnd][1] > 0]
        if len(vals) < 2:
            out[wnd] = (None, None)
            continue
        mu, se = mean_se(vals)
        out[wnd] = (mu, se)
        print("    [%4d, %4d)  %s  z %+.1f  (%d %s)"
              % (wnd[0], wnd[1], fmt(mu, se), mu / se if se else 0.0,
                 len(vals), unit))
    return out


def rank_table(rows, tag, unit="fields"):
    print("  %s: generator share minus phi(h)/h by rank" % tag)
    out = {}
    for r in range(1, RANKS + 1):
        vals = [row['ranks'][r - 1] for row in rows
                if len(row['ranks']) >= r]
        if len(vals) < 2:
            continue
        mu, se = mean_se(vals)
        out[r] = (mu, se)
        print("    rank %2d  %s  z %+.1f  (%d %s)"
              % (r, fmt(mu, se), mu / se if se else 0.0, len(vals), unit))
    for (a, b) in RANK_POOLS:
        vals = []
        for row in rows:
            v = row['ranks'][a - 1:b]
            if len(v) == b - a + 1:
                vals.append(sum(v) / len(v))
        if len(vals) >= 2:
            mu, se = mean_se(vals)
            out[(a, b)] = (mu, se)
            print("    ranks %2d-%2d pooled  %s  z %+.1f  (%d %s)"
                  % (a, b, fmt(mu, se), mu / se if se else 0.0, len(vals),
                     unit))
    return out


def cubic_verdict(tab, rk, tag):
    lo_mu, lo_se = tab[(0, 50)]
    cum_mu, cum_se = tab[(0, 250)]
    p1 = (lo_mu is not None and lo_se > 0 and lo_mu / lo_se >= 2.0
          and cum_mu > 0 and lo_mu >= 0.6 * cum_mu)
    print("  %s P1: [0, 50) excess %s against 0.6 x cut-250 %s = %.2f:"
          " %s" % (tag, fmt(lo_mu, lo_se), fmt(cum_mu, cum_se),
                   0.6 * cum_mu, p1))
    mu, se = rk.get((1, 3), (None, None))
    p2 = mu is not None and mu >= 0.15 and mu / se >= 2.0
    print("  %s P2: ranks 1-3 pooled %s against 0.15 at 2 sigma: %s"
          % (tag, fmt(mu, se), p2))
    return p1, p2


def cubic_slope(rows, wnd):
    pts = [(log(abs(r['d'])), r['per'][wnd][0]) for r in rows
           if r['per'][wnd][1] > 0]
    if len(pts) < 8:
        return
    b, se, a = EC.slope_fit(pts)
    print("  excess over [%d, %d) on log|d|: slope %+.3f +- %.3f per unit"
          " (%d fields, |d| %d to %d)"
          % (wnd[0], wnd[1], b, se, len(pts),
             min(abs(r['d']) for r in rows), max(abs(r['d']) for r in rows)))


def minkowski(d):
    """The Minkowski bound of a complex cubic field of discriminant d."""
    return (4.0 / 3.141592653589793) * (6.0 / 27.0) * sqrt(abs(d))


def subbound_generators(rec, drawn):
    """The classes of the prime ideals of norm below the Minkowski bound,
    with the partial fiber's degree-1 classes taken from `drawn` (a dict
    p -> key) rather than from the field."""
    G = rec['G']
    M = minkowski(rec['d'])
    out = []
    for p, t in rec['types'].items():
        if p > M or t == 'dropped':
            continue
        if isinstance(t, tuple) and t[0] == 'split':
            out.extend(t[1])
        elif isinstance(t, tuple) and t[0] == 'partial':
            key = drawn.get(p, t[1])
            out.append(key)
            if p * p <= M:
                out.append(G.neg(key))
    return out


def generates(G, elems):
    """Does the multiset of classes generate the whole group?"""
    seen = {G.triv}
    frontier = [G.triv]
    while frontier:
        nxt = []
        for a in frontier:
            for e in elems:
                b = G.add(a, e)
                if b not in seen:
                    seen.add(b)
                    nxt.append(b)
        frontier = nxt
    return len(seen) == G.h


def conditioned_null(recs, plist, keep, rng, draws=200, tries=4000):
    """C5: uniform partial classes, REJECTED unless the sub-bound places
    still generate the group. Returns (rows, n_excluded, accept_rate)."""
    rows = []
    excluded = 0
    tried = accepted = 0
    for rec in recs:
        G = rec['G']
        if G.h not in keep:
            continue
        gens = [k for k in G.keys if G.order[k] == G.h]
        if not gens:
            continue
        share = len(gens) / float(G.h)
        places = list(rec['field'][2])
        got = 0
        local = 0
        while got < draws and local < tries:
            local += 1
            tried += 1
            drawn = {p: rng.choice(G.keys) for (p, key) in places}
            if not generates(G, subbound_generators(rec, drawn)):
                continue
            accepted += 1
            got += 1
            pl = sorted((p, drawn[p]) for (p, key) in places)
            per = {}
            for (lo, hi) in windows_of(EDGES3) + [(0, 50), (0, 250),
                                                  (0, 1000)]:
                res, tot = EC.residuals(pl, G, lo, hi, {}, 0.0)
                per[(lo, hi)] = (sum(res[k] for k in gens), tot)
            ranks = [(1.0 if key in gens else 0.0) - share
                     for (p, key) in pl[:RANKS]]
            rows.append(dict(h=G.h, d=rec['d'], per=per, ranks=ranks,
                             share=share))
        if got == 0:
            excluded += 1
    rate = accepted / float(tried) if tried else 0.0
    return rows, excluded, rate


# ---------------------------------------------------------- real reads
def lever_rows(recs, plist, scramble=None, plant=None):
    """Per lever field: the trivial class's residual per absolute window
    and per scaled window (units of sqrt D, truncated at the cap)."""
    rows = []
    for rec in recs:
        (field, D, G, qtype) = rec
        places = list(field[2])
        if scramble is not None:
            places = [(p, scramble.choice(G.keys)) for (p, key) in places]
        if plant is not None:
            places.append((plant, G.triv))
            places.sort()
        rt = sqrt(D)
        per = {}
        wins = [('abs', w) for w in windows_of(EDGES2)]
        wins.append(('abs', (0, CAP2)))
        for (a, b) in SCALED:
            lo = int(a * rt)
            hi = CAP2 if b is None else min(CAP2, int(b * rt))
            wins.append(('sc', (a, b), (lo, hi)))
        for item in wins:
            if item[0] == 'abs':
                lo, hi = item[1]
                key = item[1]
            else:
                lo, hi = item[2]
                key = item[1]
            if hi <= lo:
                per[key] = (0.0, 0)
                continue
            if scramble is not None:
                w, blind = {}, 0.0
            else:
                w, blind = SQ.corr_deg2(rec, lo, hi, plist)[:2]
            res, tot = EC.residuals(places, G, lo, hi, w, blind)
            per[key] = (res[G.triv], tot, hi - lo)
        rows.append(dict(h=G.h, D=D, per=per))
    return rows


def band_of(D):
    for (lo, hi) in EC.BANDS_D:
        if lo <= D < hi:
            return (lo, hi)
    return None


def lever_table(rows, keys, label, tag):
    """Mean +- se of the trivial increment per (h+, band) and pooled,
    and the slope on log D, per window key. Empty windows excluded."""
    print("  %s: trivial-class residual increment per field, %s windows"
          % (tag, label))
    out = {}
    for key in keys:
        name = ("[%d, %d)" % key if label == 'absolute' else
                "[%s, %s) sqrt D" % (key[0], "inf" if key[1] is None
                                      else key[1]))
        print("    window %s:" % name)
        for h in EC.HPLUS:
            cells = []
            pts = []
            for (lo, hi) in EC.BANDS_D:
                vals = [r['per'][key][0] for r in rows
                        if r['h'] == h and band_of(r['D']) == (lo, hi)
                        and r['per'][key][1] > 0]
                if len(vals) >= 2:
                    mu, se = mean_se(vals)
                    cells.append("%s" % fmt(mu, se))
                    out[(key, h, (lo, hi))] = (mu, se, len(vals))
                else:
                    cells.append("    --    ")
            for r in rows:
                if r['h'] == h and r['per'][key][1] > 0:
                    pts.append((log(r['D']), r['per'][key][0]))
            if len(pts) >= 30:
                mu, se = mean_se([y for x, y in pts])
                b, sb, a = EC.slope_fit(pts)
                out[(key, h, 'all')] = (mu, se, len(pts))
                out[(key, h, 'slope')] = (b, sb)
                print("      h+ = %d  bands %s | pooled %s (%d)  slope"
                      " %+.3f +- %.3f" % (h, "  ".join(cells), fmt(mu, se),
                                           len(pts), b, sb))
            else:
                print("      h+ = %d  bands %s | too few" % (h,
                                                            "  ".join(cells)))
    return out


# ------------------------------------------------------------------ main
def main():
    t0 = time.time()
    plist = primes_upto(CO.PCAP)
    rng = random.Random(SEED)

    section("THE |D| LEVER (real narrow, the sibling's population)")
    recs_l = EC.lever_population(plist)
    print("  %d fields" % len(recs_l))
    rows_l = lever_rows(recs_l, plist)
    abs_keys = windows_of(EDGES2)
    sc_keys = [(a, b) for (a, b) in SCALED]

    section("C2  ADDITIVITY (real side) AND C3  THE REPRINT (the slope)")
    worst = 0.0
    for r in rows_l:
        cum = r['per'][(0, CAP2)][0]
        worst = max(worst, abs(sum(r['per'][k][0] for k in abs_keys) - cum))
        worst = max(worst, abs(sum(r['per'][k][0] for k in sc_keys) - cum))
    ok(worst < 1e-9, "C2 real: partitions do not sum to the cut (%.3g)"
       % worst)
    print("  C2 real PASSES: both partitions sum to the cut-1000 residual"
          " (worst %.1e over %d fields)" % (worst, len(rows_l)))
    pts = [(log(r['D']), r['per'][(0, CAP2)][0]) for r in rows_l
           if r['h'] == 8 and r['per'][(0, CAP2)][1] > 0]
    b, sb, a = EC.slope_fit(pts)
    ok(QUICK or abs(b - REPRINT_SLOPE[0]) < REPRINT_SLOPE[1],
       "C3: h+ = 8 slope at p < 1000 reads %.4f" % b)
    print("  C3 real PASSES: h+ = 8 slope %+.4f +- %.4f reprints %.3f"
          % (b, sb, REPRINT_SLOPE[0]))

    section("C4  THE PLANTED PLACE (real side)")
    sub = recs_l[:150]
    base = lever_rows(sub, plist)
    moved = lever_rows(sub, plist, plant=3)
    worst = 0.0
    for r0, r1 in zip(base, moved):
        for k in abs_keys:
            want = (1.0 - 1.0 / r0['h']) if k == (0, 100) else 0.0
            worst = max(worst, abs((r1['per'][k][0] - r0['per'][k][0])
                                   - want))
    ok(worst < 1e-9, "C4 real: planted place off by %.3g" % worst)
    print("  C4 real PASSES: 1 - 1/h on [0, 100), zero elsewhere, exactly"
          " (worst %.1e over %d fields)" % (worst, len(sub)))
    del sub, base, moved

    section("C1  THE NULL (real side, one uniform re-sort, no correction)")
    null_l = lever_rows(recs_l, plist, scramble=rng)
    zs = []
    for key in sc_keys:
        for h in EC.HPLUS:
            vals = [r['per'][key][0] for r in null_l
                    if r['h'] == h and r['per'][key][1] > 0]
            if len(vals) < 30:
                continue
            mu, se = mean_se(vals)
            zs.append(mu / se)
            print("  null h+ = %d  [%s, %s) sqrt D  %s  z %+.2f  (%d)"
                  % (h, key[0], "inf" if key[1] is None else key[1],
                     fmt(mu, se), mu / se, len(vals)))
    ok(all(abs(z) < 3.0 for z in zs), "C1 real: a null increment is off"
       " zero")
    print("  C1 real PASSES: every pooled scaled increment within 3 sigma"
          " of zero")
    del null_l

    section("THE REAL TRIVIAL CLASS BY WINDOW")
    tab_abs = lever_table(rows_l, abs_keys, 'absolute', "lever")
    tab_sc = lever_table(rows_l, sc_keys, 'scaled', "lever")

    section("P4  THE REAL COUNT ENDS AT sqrt(D)/2")
    p4 = True
    for h in (4, 8):
        hi = tab_sc.get(((0.5, 1.0), h, 'all'))
        tail = tab_sc.get(((1.0, 2.0), h, 'all'))
        top = tab_sc.get(((2.0, None), h, 'all'))
        # the increment over [sqrt(D)/2, 1000) is the sum of the three
        # scaled windows above 1/2, read per field
        vals = [sum(r['per'][k][0] for k in sc_keys[2:])
                for r in rows_l if r['h'] == h
                and any(r['per'][k][1] > 0 for k in sc_keys[2:])]
        mu, se = mean_se(vals)
        lo = tab_sc.get(((0.25, 0.5), h, 'all'))
        print("  h+ = %d  [sqrt(D)/2, 1000) %s z %+.2f (%d fields);"
              " [sqrt(D)/4, sqrt(D)/2) %s z %+.2f"
              % (h, fmt(mu, se), mu / se, len(vals), fmt(lo[0], lo[1]),
                 lo[0] / lo[1]))
        p4 = p4 and abs(mu / se) < 2.0 and lo[0] / lo[1] >= 3.0
    print("  P4 PASSES iff the tail is within 2 sigma of zero and the"
          " [1/4, 1/2) window is positive at 3 sigma, at both h+: %s" % p4)

    section("P5  THE BANDS PART IN ABSOLUTE p (h+ = 8, [100, 1000))")
    cells = {}
    for band in (EC.BANDS_D[0], EC.BANDS_D[-1]):
        vals = [sum(r['per'][k][0] for k in abs_keys[1:]) for r in rows_l
                if r['h'] == 8 and band_of(r['D']) == band]
        mu, se = mean_se(vals)
        cells[band] = (mu, se)
        print("  band %d-%d  [100, 1000) %s  z %+.2f  (%d fields)"
              % (band[0], band[1], fmt(mu, se), mu / se, len(vals)))
    (m1, s1), (m5, s5) = cells[EC.BANDS_D[0]], cells[EC.BANDS_D[-1]]
    p5 = abs(m1 / s1) < 2.0 and m5 / s5 >= 3.0
    print("  P5 PASSES iff the bottom band reads zero within 2 sigma and"
          " the top band is positive at 3 sigma: %s" % p5)

    del recs_l, rows_l
    gc.collect()

    section("THE DEGREE-3 PARTIAL FIBER, BASE POPULATION")
    recs_3, nmapped = SQ.deg3_records(False)
    fields_3 = [r['field'] for r in recs_3]
    keep_3, _ = CV.frozen_strata(fields_3, CV.CUTS, CV.BANDS)
    print("  %d of %d fields admissible, strata %s" % (len(recs_3), nmapped,
                                                       keep_3))
    rows_3 = cubic_rows(recs_3, plist, keep_3)

    section("C2  ADDITIVITY, C3  THE REPRINT, C4  THE PLANTED PLACE"
            " (cubic side)")
    worst = 0.0
    for r in rows_3:
        worst = max(worst, abs(sum(r['per'][w][0] for w in windows_of(EDGES3))
                               - r['per'][(0, 1000)][0]))
    ok(worst < 1e-9, "C2 cubic: partition does not sum to the cut (%.3g)"
       % worst)
    print("  C2 cubic PASSES: the partition sums to the cut-1000 excess"
          " (worst %.1e over %d fields)" % (worst, len(rows_3)))
    mu, se = mean_se([r['per'][(0, 250)][0] for r in rows_3
                      if r['per'][(0, 250)][1] > 0])
    ok(abs(mu - REPRINT_CUBIC[0]) < REPRINT_CUBIC[1],
       "C3 cubic: cut-250 excess reads %.3f" % mu)
    print("  C3 cubic PASSES: cut-250 excess %s reprints %.2f"
          % (fmt(mu, se), REPRINT_CUBIC[0]))
    moved = cubic_rows(recs_3, plist, keep_3, plant=7)
    worst = 0.0
    for r0, r1 in zip(rows_3, moved):
        for w in windows_of(EDGES3):
            want = (1.0 - r0['share']) if w == (0, 20) else 0.0
            worst = max(worst, abs((r1['per'][w][0] - r0['per'][w][0])
                                   - want))
    ok(worst < 1e-9, "C4 cubic: planted place off by %.3g" % worst)
    print("  C4 cubic PASSES: 1 - phi(h)/h on [0, 20), zero elsewhere,"
          " exactly (worst %.1e)" % worst)
    del moved

    section("C1  THE NULL (cubic side, one uniform re-sort)")
    null_3 = cubic_rows(recs_3, plist, keep_3, scramble=rng)
    tab = cubic_table(null_3, "null")
    rk = rank_table(null_3, "null")
    zs = [mu / se for (mu, se) in list(tab.values()) + list(rk.values())
          if mu is not None and se]
    ok(all(abs(z) < 3.0 for z in zs), "C1 cubic: a null statistic is off"
       " zero")
    print("  C1 cubic PASSES: every null window and rank within 3 sigma")
    del null_3

    section("C5  THE GENERATION-CONDITIONED NULL (base population)")
    null_c, nexc, rate = conditioned_null(recs_3, plist, keep_3, rng)
    print("  Minkowski bound %.1f at the cap; acceptance rate %.3f, %d"
          " fields with no accepted draw" % (minkowski(6000), rate, nexc))
    print("  (an excluded field cannot generate without the ramified"
          " places the parent does not class; the null bounds the"
          " confound from above)")
    tab_c = cubic_table(null_c, "C5 null", unit="accepted draws")
    rk_c = rank_table(null_c, "C5 null", unit="accepted draws")
    print("  C5: the conditioning's OWN rank-1 excess is %s and its"
          " ranks 1-3 pooled %s -- the confound's measured size, to be"
          " subtracted from P2 by eye" % (fmt(*rk_c[1]), fmt(*rk_c[(1, 3)])))
    del null_c

    section("P1, P2  THE CUBIC COUNT BY WINDOW AND BY RANK (base)")
    tab = cubic_table(rows_3, "base")
    rk = rank_table(rows_3, "base")
    p1, p2 = cubic_verdict(tab, rk, "base")
    cubic_slope(rows_3, (0, 250))
    cubic_slope(rows_3, (0, 50))
    del recs_3, rows_3
    gc.collect()

    if QUICK:
        print("\n  (rehearsal: the wide population is skipped)")
    else:
        section("P3  THE WIDE REPLICATION (h = 4, 6, 8)")
        recs_w, nmapped = SQ.deg3_records(True)
        rows_w = cubic_rows(recs_w, plist, WIDE_H)
        print("  %d admissible wide fields, %d at h in %s"
              % (len(recs_w), len(rows_w), WIDE_H))
        tab = cubic_table(rows_w, "wide")
        rk = rank_table(rows_w, "wide")
        q1, q2 = cubic_verdict(tab, rk, "wide")
        print("  P3 PASSES iff both hold on the wide population: %s"
              % (q1 and q2))
        cubic_slope(rows_w, (0, 250))
        cubic_slope(rows_w, (0, 50))
        section("C5  THE GENERATION-CONDITIONED NULL (wide population)")
        null_w, nexc, rate = conditioned_null(recs_w, plist, WIDE_H, rng,
                                              draws=40)
        print("  Minkowski bound %.1f at the wide cap; acceptance rate"
              " %.3f, %d fields with no accepted draw"
              % (minkowski(24000), rate, nexc))
        rk_c = rank_table(null_w, "C5 null wide",
                          unit="accepted draws")
        print("  C5 wide: the conditioning's own rank-1 excess %s,"
              " ranks 1-3 pooled %s" % (fmt(*rk_c[1]), fmt(*rk_c[(1, 3)])))
        del null_w, recs_w
        for h in WIDE_H:
            sub = [r for r in rows_w if r['h'] == h]
            if len(sub) >= 5:
                print("  by stratum h = %d:" % h)
                cubic_table(sub, "wide h=%d" % h)
                rank_table(sub, "wide h=%d" % h)
                # the |d| slope PER STRATUM: the pooled slope's one
                # confound is the h composition, h and |d| not being
                # independent in this population
                cubic_slope(sub, (0, 50))
                cubic_slope(sub, (0, 250))
        hs = [r['h'] for r in rows_w]
        ds = [log(abs(r['d'])) for r in rows_w]
        mh = sum(hs) / len(hs)
        md = sum(ds) / len(ds)
        cov = sum((a - mh) * (b - md) for a, b in zip(hs, ds))
        vh = sum((a - mh) ** 2 for a in hs) ** 0.5
        vd = sum((b - md) ** 2 for b in ds) ** 0.5
        print("  h against log|d| over the %d fields: correlation %+.3f"
              " (the pooled slope's confound, measured)"
              % (len(rows_w), cov / (vh * vd)))

    print("\n%d checks passed, %.1f s wall" % (CHECKS, time.time() - t0))


if __name__ == "__main__":
    main()
