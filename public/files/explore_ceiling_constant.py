r"""THE CONSTANT TERM -- is the second object the square term leaves the
explicit formula's x-INDEPENDENT term? (sibling of
explore_ceiling_squares.py, whose populations, class groups and
prime-power corrections it imports whole and reads in a different unit:
COUNTS of primes per field, never levels.)

THE QUESTION. Putting the explicit formula's prime-power terms back
flattens the generator ceiling at both degrees and both quadratic signs
(explore_ceiling_squares.py F1-F5), and leaves three things standing:
on the imaginary side the order-2 cells read LONG after the correction
at p < 1000 (1.02-1.09) and on the real narrow side SHORT (0.944, 0.920,
0.875, 0.822 at h = 4, 6, 8, 10), both gone by 10000; the cubic partial
fiber carries no prime-square term at all, yet its generator cell runs a
ladder 1.25, 1.20, 1.16, 1.10 over the cuts 250, 400, 630, 1000 and reads
1 in the band [630, 1000); and at a fixed narrow class number the
trivial class's level at p <= 100 SHALLOWS with |D| across a 512-fold
lever (0.342 -> 0.627 at h+ = 8), which a prime-power weight blind to
|D| at a fixed group cannot produce. Read as COUNTS the three share a
shape. The cubic generator surplus is 0.25 x 13, 0.20 x 19.5, 0.16 x
28.5, 0.10 x 42 = about 3.3, 3.9, 4.6, 4.2 primes per field across the
four cuts -- a fixed number of primes, not a decaying share. The
shallowing is 0.06 to 0.08 primes per unit of log|D| at every one of
h+ = 2, 4, 8 -- a common slope, the tell of an additive count. This file
asks whether all of it is one more term of the same explicit formula: the
one that does not depend on x.

THE HAND-DERIVATION (pre-engine, on paper).

  (1) THE TERM. For a primitive character chi the explicit formula reads
        psi(x, chi) = -sum_rho x^rho/rho - (1 - a) log x - b(chi) + ...
      (Davenport, ch. 19), with a the parity and b(chi) the constant of
      the Hadamard product, Re b(chi) = -sum_rho Re(1/rho) (ch. 12). The
      product evaluated at s = 1 gives sum_rho Re(1/rho) = (1/2) log(q/pi)
      + Re L'/L(1, chi) + (1/2) Re Gamma'/Gamma((1 + a)/2), so the
      x-independent part of psi(x, chi) is
        (1/2) log q + Re L'/L(1, chi) - (#trivial zeros at s = 0) log x
        + O(1),
      of size log q and of either sign: the "(1 - a) log x" is the trivial
      zero of Gamma_R(s) at s = 0, and an L-function with Gamma_R(s)^2 at
      infinity pays it twice. For the class-group characters of a
      quadratic field K read over Q, Ind(chi) has conductor |D| for every
      nontrivial chi (unramified at the finite places), and its type at
      infinity is Gamma_C(s) = Gamma_R(s) Gamma_R(s + 1) -- one trivial
      zero at 0 -- when complex conjugation acts as a reflection (every
      nontrivial character of an imaginary field; every NARROW character
      of a real field that is nontrivial on the kernel of Cl+ -> Cl), and
      Gamma_R(s)^2 -- two trivial zeros at 0 -- when it acts trivially
      (the narrow characters that factor through the wide group, all of
      them when N(eps) = -1). Divided by log x to reach a PRIME count,
      the term is c_chi = ((1/2) log|D| - t_chi log x + Re L'/L(1, chi) +
      O(1)) / log x primes per character, t_chi in {1, 2}: about -0.4 for
      Gamma_C and -1.4 for Gamma_R^2 at |D| = 3000, x = 1000.

  (2) HOW IT LANDS ON THE CLASSES. pi_C(x) = (1/h) sum_chi conj(chi)(C)
      pi(x, chi), and the corpus's nominal is the realised total over h,
      which is the trivial character's share, so every class C carries
        (1/h) sum_{chi != 1} conj(chi)(C) c_chi
      beyond its nominal. Where every nontrivial chi has the same type
      (the imaginary side) this is ((h - 1)/h) c on the trivial class and
      -c/h on every other: a trivial-against-the-rest structure and
      nothing finer. On the real narrow side with N(eps) = +1 the h/2 wide
      characters carry t = 2 and the h/2 others t = 1, and the character
      sums over the two cosets put the difference on ONE class: the
      nontrivial element k0 of the kernel of Cl+ -> Cl, the narrow class
      of a principal ideal with a generator of negative norm, of order 2.
      Worked through: a generic nontrivial class reads 2/h - L/h, the k0
      class 2/h - 1/2 - L/h, the trivial class (h - 1)L/h - 3/2 + 2/h,
      with L = (1/2) log|D| / log x; so k0 sits HALF A PRIME per field
      below its nontrivial siblings, whatever h. When N(eps) = -1 there is
      no k0 and every character pays t = 2.

  (3) THE GRADING BY |D|. At a fixed group the only |D| in the term is the
      conductor: the trivial class gains ((h - 1)/h) x (1/2) / log x
      primes per unit of log|D| -- 0.109 (h - 1)/h per unit at x = 100
      and 0.072 (h - 1)/h at x = 1000 -- in the direction that SHALLOWS
      its deficit. The corpus's shallowing read in counts is 0.06 to
      0.08 per unit at h+ = 2, 4, 8 at p <= 100.

  (4) THE SHAPE IN x. A count, so a level that decays as 1/pi(x): the
      count at cut 10000 against cut 1000 moves only through the
      -t log x piece, a ratio of about 1.1 to 1.4, where a leftover of the
      prime-power term's kind would read pi(100)/pi(31) = 25/11 = 2.27
      and a 1/sqrt(x) level 2.4.

  (5) THE CLASS-DEPENDENT PIECE AND WHY IT IS NOT DECIDABLE HERE. The
      Re L'/L(1, chi) piece in the class basis is -(1/h) x h x S(C) with
      S(C) the sum of log NP / NP^k over the prime powers of class C: a
      class rich in small-prime mass is, ABOVE those primes, short by
      about S(C)/log x. For the one class holding the prime 3 against its
      siblings that is log 3 / 3 / log 1000 = 0.05 primes per field in
      the window [100, 1000), against a per-class window count of about
      60 primes: a regression over the corpus resolves 0.5 per unit of S
      where the signal is 0.14. It is computed and printed for the record
      and frozen as NO prediction -- the late start PRINCIPAL names is
      this piece, and this population cannot read it.

  (6) THE STATISTIC'S ALGEBRA. Per field and window the corrected count
      of a class is its counted places plus its prime-power weight, the
      corrected total is the counted total plus the summed weights, and
      the residual count of the class is its corrected count minus the
      corrected total over h. The residuals of a field's classes sum to
      zero exactly, so a class's residual is read against its siblings'
      and never alone, and a constant the same on every class is
      invisible -- which is the trivial character's and should be. The
      per-field residual has the binomial spread of its cell, about
      sqrt(84/h) primes at cut 1000; every pooled figure is a mean over
      fields with its standard error, and a ratio of two counts is read
      only where the denominator stands 3 sigma from zero.

THE DESIGN. The parents' imaginary sweep to |D| <= 4000 and real narrow
sweep to D <= 16000, admissible fields and frozen strata as the parents
froze them, with the corrections of explore_ceiling_squares.py at the
windows [0, 400), [0, 630), [0, 1000), [0, 2500), [0, 10000) and the
scale cell [0, 101). The cubic base population to |d| <= 6000, partial
fiber, cuts 250 to 1000. A NEW real narrow population for the |D| lever:
the five bands (2000, 4000), (8000, 16000), (32000, 64000), (128000,
256000), (512000, 1024000) sampled by a uniform stride, up to 200 fields
per (band, h+) cell at h+ = 2, 4, 8, each with its full narrow class
group, composition, orders and places below 1000 -- the imaginary side
is not usable for this read, every field of every band having |D|/4
above 100 and so no principal prime at all below it (the hard zero).
Every field's classes are sorted into trivial, k0 (real only), order 2
holding a ramified ideal, order 2 holding none, and higher, and the
per-class residual is pooled by that sort.

THE SLATE -- PREDICTIONS FROZEN BEFORE THE ENGINE.

  P1  FLAT IN x AT DEGREE 2. For every (sign, cell) among {imaginary,
      real} x {order-2 classes pooled, trivial class} whose residual
      count per field at cut 1000 stands 3 sigma from zero, the ratio of
      the cut-10000 count to the cut-1000 count has its central value
      in [0.5, 2.0]; the distance of 2.27 from the measured ratio is
      printed beside it.
  P2  FLAT IN x AT DEGREE 3. The cubic partial fiber's generator-cell
      excess count per field at cut 1000 over the same at cut 250 lies
      in [0.6, 1.6] (the level's own ratio is 0.10/0.25 = 0.4).
  P3  THE |D| SLOPE. On the lever population at p <= 100 the trivial
      class's residual count regressed on log|D| has a positive slope at
      2 sigma or more at each of h+ = 2, 4, 8, and the slopes divided by
      (h - 1)/h pool to a value within a factor 2.5 of 1/(2 log 100) =
      0.109, i.e. in [0.044, 0.27].
  P4  THE REAL NARROW SEAT. Over the real sweep's admissible fields with
      N(eps) = +1 and h+ >= 4, at cut 1000, the k0 class's residual count
      per field minus the mean residual of its nontrivial siblings lies
      in [-1.0, -0.2] and is negative at 2 sigma or more.

THE CONTROLS, run before any prediction is read.

  C1  THE NULL. Every place of every field re-sorted to a uniformly
      random class of its own group (one seeded draw) and read with no
      correction, uniform classes carrying no term; the P1 counts at
      cut 1000 and the P4 difference must all read within 3 sigma of
      zero.
  C2  THE PLANTED PRIME. One synthetic trivial-class place added to every
      field moves that field's trivial residual by exactly 1 - 1/h and
      its siblings' by exactly -1/h (the identity of (6)), at every
      field, to 1e-9.
  C3  THE REPRINT. The parents' corrected imaginary generator levels at
      cuts 1000 and 10000 (1.0011, 1.0000) reprint through the imported
      reader inside 0.0015, and every field's residuals sum to zero.
  C4  THE KERNEL CLASS. At every real field k0 has order at most 2, and
      k0 is the trivial class exactly when the fundamental unit has norm
      -1 (class_data_real's reading), at zero disagreements.

WHAT IS NOT CONTROLLED. The term's absolute SIZE: -b(chi)'s O(1) and the
low zeros' fluctuation in sum Re(1/rho) are the family's one-level density
at the kernel 1/(1/4 + gamma^2), not computed here; this file reads the
shape in x, the grading by log|D|, the seat on the real side, and nothing
about the number. At x below the discriminant the oscillatory remainder
carries the geometry (the hard zero), which is why the lever read is real
narrow only and the imaginary trivial class is read at cuts past |D|.

THE FINDINGS (the post-run record; every number is a print of the run).

  CONTROLS. C3: the parents' corrected generator levels reprint (1.0011
  at cut 1000, 1.0000 at 10000) and every field's residuals sum to zero
  (worst 3.5e-13). C2: the planted prime moves the trivial residual by
  1 - 1/h and each sibling's by -1/h exactly (worst 2.4e-15). C4: k0 has
  order at most 2 at every real field and is trivial iff N(eps) = -1, 0
  disagreements; 1518 of the 2086 admissible real fields carry a k0.
  C1: the null reads +0.03 +- 0.19 (imaginary order 2), -0.20 +- 0.19
  (imaginary trivial), +0.10 +- 0.15 and +0.08 +- 0.16 (real), -0.05 +-
  0.23 (k0 difference) -- every |z| below 1.1. THE FIRST RUN FAILED C1 BY
  THE INSTRUMENT'S OWN CONSTRUCTION: the null re-sorted the places but
  kept the real population's prime-power weights, which land on the
  trivial class by construction, and read +2.8 primes there at 14
  sigma; the null now carries no correction, uniform classes carrying no
  term. The slate was untouched by the fix.

  F1  P1 FAILS: THE COUNTS ARE FLAT TO 1000 AND THEN SHRINK, AND THE
      IMAGINARY LADDER READS THE HARD ZERO'S REPAYMENT (observation).
      Residual counts per field over the cuts 400, 630, 1000, 2500,
      10000 --
        imaginary order 2  +0.29  +0.51  +0.51  +0.17  +0.00 (+- 0.08..0.23)
        imaginary trivial  -0.70  -0.83  -0.05  -0.35  -0.50 (+- 0.06..0.20)
        real order 2       -1.12  -1.19  -1.31  -0.90  -0.88 (+- 0.07..0.24)
        real trivial       +0.38  +0.37  +0.45  +0.22  +0.08 (+- 0.07..0.24)
      The decidable ratios 10000/1000 are 0.01 +- 0.45, 0.67 +- 0.19 and
      0.18 +- 0.53, so the central values fall below the [0.5, 2.0] band
      in two of three cells; the prime-power shape 2.27 sits 5.0, 8.5 and
      4.0 sigma away. On the real side, which carries no hard zero, the
      counts are constant from 400 to 1000 and fall to about two thirds
      by 10000 -- neither a constant nor a decaying share. The imaginary
      trivial class jumps from -0.83 +- 0.09 at cut 630 to -0.05 +- 0.09
      at cut 1000, which reads as REPAYMENT: a field's trivial class is
      empty below |D|/4 while the main term is unchanged, so the deficit
      must be repaid above |D|/4, and the fields with |D| in (2520, 4000]
      have their |D|/4 inside that band -- a reading of the pooled jump,
      not a per-field measurement; the uncontrolled item (7)(a) of the
      parent rig, now seen.

  F2  P2 PASSES: THE CUBIC PARTIAL EXCESS IS A FIXED COUNT (observation,
      24 fields at h = 4 and 6). The generator-cell excess reads +3.01
      +- 0.33, +3.53 +- 0.45, +4.29 +- 0.59, +3.79 +- 0.67 primes per
      field at cuts 250, 400, 630, 1000; the ratio 1000/250 is 1.26 +-
      0.26, where a count of prime squares would move by pi(31)/pi(15)
      = 11/6 = 1.83 over those cuts, 2.2 spreads off (the 2.27 of (4) is
      that shape over 1000 -> 10000 and was once printed here). The
      parents' ladder 1.246 -> 1.096 is this
      count over a growing denominator, and the top band's 1 is the same
      count over a window that holds none of it.

  F3  P3 PASSES, AND THE p <= 100 SLOPE IS THE CONDUCTOR CONSTANT TO ONE
      PER CENT WHILE THE p < 1000 SLOPE IS SIX TIMES IT (observation, 2793
      fields). The trivial class's residual count regressed on log|D| --
        p <= 100   h+ = 2  +0.052 +- 0.021 (z 2.5)   /((h-1)/h) 0.105
                   h+ = 4  +0.074 +- 0.018 (z 4.2)              0.099
                   h+ = 8  +0.098 +- 0.016 (z 6.1)              0.112
                   pooled normalised slope 0.107 +- 0.014, the term's 0.109
        p < 1000   h+ = 2  +0.143 +- 0.045 (z 3.2)              0.286
                   h+ = 4  +0.353 +- 0.041 (z 8.6)              0.471
                   h+ = 8  +0.351 +- 0.038 (z 9.3)              0.402
                   pooled normalised slope 0.410 +- 0.032, the term's 0.072.
      Band means at p < 1000, h+ = 8: +0.32, +0.97, +1.49, +2.03, +2.33
      primes per field from the 2000-4000 band to the 512000-1024000
      one. The grading grows with the cut where the conductor term
      shrinks with it, so the agreement at p <= 100 is not the term's
      doing; a grading that lengthens with the cut has the shape of the
      trivial class's EARLY START, its small norms accruing over p <
      sqrt(D)/2 -- read, not derived.

  F4  P4 FAILS ON SIZE AND HOLDS ON THE SEAT (observation). k0 minus the
      mean of its nontrivial siblings reads -1.81 +- 0.09 at cut 400,
      -2.10 +- 0.14 at cut 1000 (z -14.8) and -1.54 +- 0.34 at 10000, on
      385 fields with h+ >= 4 and N(eps) = +1; by stratum at cut 1000,
      -2.39 +- 0.24, -1.59 +- 0.24, -2.51 +- 0.34, -2.18 +- 0.24 at h+ =
      4, 6, 8, 10. The frozen bracket was [-1.0, -0.2]. The per-class
      table at cut 1000 over the real strata: trivial +0.45 +- 0.10, k0
      -1.85 +- 0.12, the other order-2 classes +0.18 +- 0.16, the higher
      orders +0.28 +- 0.03 each: the order-2 residual of the parents is
      this one class. On the imaginary side at cut 1000 every order-2
      class holds a ramified ideal and the cell reads +0.51 +- 0.10, the
      trivial -0.05 +- 0.09, the higher orders -0.07 +- 0.02; at 10000
      +0.00 +- 0.23, -0.50 +- 0.20, +0.08 +- 0.04. AND THE DERIVATION'S
      ARCHIMEDEAN TYPE WAS WRONG FOR THE CHARACTERS ODD ON k0 (noted
      after the scoring, the slate left as frozen): complex conjugation
      is trivial on a real field, so in Gal(H+/Q) it is an ELEMENT of
      Cl+ -- the class k0 itself, the Artin image of the infinite places
      -- and Ind(chi) has Gamma_R(s)^2 when chi(k0) = +1 and Gamma_R(s +
      1)^2, with no trivial zero at 0, when chi(k0) = -1; never Gamma_C.
      Corrected, the trivial zeros alone put k0 ONE prime below its
      siblings, not half; measured two at cut 1000, one and a half at
      10000.

  R1  THE SEAT IS THE ODD-CHARACTER RACE (post-run read; identity a
      property, the rest observation). At h+ = 2 with k0 != triv, D =
      D1.D2 with both prime discriminants negative, and over 1133 such
      fields triv - k0 over the split primes equals sum chi_D1(p) at
      every one, at both cuts. The k0 residual there is -1.07 +- 0.07 at
      cut 1000 and -0.84 +- 0.18 at 10000, which is -(1/4) of the pair
      mean of S(d) = sum_{p < x} chi_d(p) + pi(sqrt x)/2. Over every
      fundamental d < 0 to 16000 that square-corrected race reads, by
      |d| band, +2.8 +- 1.2, +3.9 +- 0.6, +8.4 +- 0.3, +6.6 +- 0.2 at x =
      1000 (|d| below 100, to 1000, to 4000, to 16000) and -0.4 +- 2.1,
      +2.5 +- 1.3, +5.9 +- 0.9, +9.8 +- 0.5 at x = 10000. Read against
      the +pi(sqrt x)/2 it carries (5.5 and 12.5): at x = 1000 the raw
      race averages +1.2 over the 4863 discriminants, near zero against
      the term's -5.5, as the average of chi_d(p) over a family wider
      than p gives; at x = 10000, where the family is not wider than x,
      it averages -3.9 against -12.5. The square-term bias is developed
      only where |d| << x (|d| < 100 at x = 10000: -12.9 against -12.5),
      a fifth of its size at |d| ~ x, and reversed to a residue lead at
      |d| in (x, 4x). So the
      k0 deficit is Chebyshev's bias for two odd characters BEFORE it has
      developed -- x comparable to |d| -- and its shrinking by 10000 is
      the bias catching up. The x-independent term this file asked about
      is not what the corpus's residual is; the residual is the
      approach to the square term, seen through the one class whose
      characters are odd.

RUN RECORD. 2026-08-20, Windows 11, Python 3, `python
prime/code/memwatch.py --limit 512 prime/code/explore_ceiling_constant.py`.
One process, CPython, no BLAS. 1140 checks passed, 250.4 s wall, peak
working set 442 MB against the 512 MB ceiling. Three earlier runs of the
same day: the first failed C1 as recorded above; the second and third
were killed by memwatch at 515 MB at the lever stage with the degree-2
populations still resident, cured by freeing them and by running the
lever before the cubic stage; the fourth scored the slate, and R1 was
added and run after it. No number changed between the scoring run and
this one. Re-run 2026-08-24 after the prime-square shape beside each
ratio was made a function of its two cuts: 1140 checks, 250.7 s wall, peak
442.7 MB; every figure above reprinted unchanged.
"""

import os
os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")

import gc
import random
import sys
import time
from collections import defaultdict
from math import isqrt, log

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import explore_ceiling_squares as SQ               # noqa: E402
import explore_ceiling_curve as CV                 # noqa: E402
import explore_class_order as CO                   # noqa: E402
from explore_class_share import classes_real       # noqa: E402
from explore_principal_share import (              # noqa: E402
    primes_upto, kronecker, form_at, reduce_form, class_data_real,
    fundamental_discriminants)

CHECKS = 0
CUTS = (400, 630, 1000, 2500, 10000)
SCALE_HI = 101                       # the window [0, 101) = p <= 100
CUBIC_CUTS = CV.CUTS                 # 250, 400, 630, 1000
BANDS_D = ((2000, 4000), (8000, 16000), (32000, 64000),
           (128000, 256000), (512000, 1024000))
HPLUS = (2, 4, 8)
NSCAN = 1500                         # discriminants scanned per band
NCELL = 200                          # fields kept per (band, h+) cell
LEVER_CAP = 1000
SEED = 20881


def prime_square_shape(ca, cb):
    """pi(sqrt(cb)) / pi(sqrt(ca)): what a count of prime squares below the
    cut would do between the two cuts -- 25/11 = 2.27 for 1000 -> 10000
    and 11/6 = 1.83 for 250 -> 1000."""
    def pi(n):
        return sum(1 for k in range(2, n + 1)
                   if all(k % q for q in range(2, isqrt(k) + 1)))
    return pi(isqrt(cb)) / pi(isqrt(ca))


IMAG_GEN = {1000: 1.0011, 10000: 1.0000}
REPRINT_TOL = 0.0015


def ok(cond, msg):
    global CHECKS
    CHECKS += 1
    if not cond:
        print("  FAIL: " + msg)
        sys.exit(1)


def section(t):
    print("\n" + "=" * 72 + "\n" + t + "\n" + "=" * 72)


def mean_se(vals):
    return CV.mean_se(vals)


def fmt(mu, se):
    if mu is None:
        return "    --    "
    return "%+.3f +- %.3f" % (mu, se)


# ------------------------------------------------------------ residuals
def residuals(places, G, lo, hi, w, blind):
    """Per-class residual count over [lo, hi): corrected count minus the
    corrected total over h. Returns (res, tot)."""
    h = G.h
    cnt = defaultdict(float)
    tot = 0
    for (p, key) in places:
        if lo <= p < hi:
            tot += 1
            cnt[key] += 1.0
    tot_c = float(tot)
    for key, wt in w.items():
        cnt[key] += wt
        tot_c += wt
    res = {key: cnt.get(key, 0.0) - tot_c / h for key in G.keys}
    return res, tot


def sort_classes(G, triv, k0, ram_keys):
    """key -> 'triv' | 'k0' | 'ram2' | 'oth2' | 'high'."""
    cat = {}
    for key in G.keys:
        if key == triv:
            cat[key] = 'triv'
        elif k0 is not None and key == k0:
            cat[key] = 'k0'
        elif G.order[key] == 2:
            cat[key] = 'ram2' if key in ram_keys else 'oth2'
        else:
            cat[key] = 'high'
    return cat


def deg2_extras(rec, sign, plist, hi):
    """(k0 or None, ramified class keys below hi, neps) for one field."""
    (field, D, G, qtype) = rec
    ram = set()
    for q in plist:
        if q >= hi:
            break
        if D % q == 0:
            t, key = qtype(q)
            if t == 0 and key is not None:
                ram.add(key)
    k0 = None
    neps = 0
    if sign > 0:
        recs_r, member, triv, rt = classes_real(D)
        b0 = D % 2
        c0 = (b0 * b0 - D) // 4
        k0 = member[reduce_form((-1, b0, -c0), D, rt)]
        _, _, neps = class_data_real(D, rt)
    return k0, ram, neps


def field_rows(recs, sign, plist, windows, places_of, corr_of, G_of,
               triv_of, scramble=None):
    """Per field: dict window -> (res, tot), plus the sort and h.
    scramble: an rng; every place re-sorted to a uniform class (C1)."""
    rows = []
    for rec in recs:
        G = G_of(rec)
        triv = triv_of(rec)
        places = places_of(rec)
        if scramble is not None:
            places = [(p, scramble.choice(G.keys)) for (p, key) in places]
        k0, ram, neps = deg2_extras(rec, sign, plist, 1000)
        cat = sort_classes(G, triv, k0 if k0 != triv else None, ram)
        per = {}
        for (lo, hi) in windows:
            if scramble is not None:
                w, blind = {}, 0.0      # uniform classes carry no term
            else:
                w, blind = corr_of(rec, lo, hi)[:2]
            per[(lo, hi)] = residuals(places, G, lo, hi, w, blind)
        rows.append(dict(h=G.h, cat=cat, per=per, k0=k0, neps=neps,
                         D=rec[1], keys=G.keys, triv=triv))
    return rows


def pooled(rows, window, which, keep=None):
    """Mean +- se over fields of a per-field residual statistic:
    which = 'ord2' (sum over order-2 classes), 'triv', 'k0diff' (k0 minus the mean of its nontrivial
    siblings, fields with a k0 only)."""
    vals = []
    for r in rows:
        if keep is not None and r['h'] not in keep:
            continue
        res, tot = r['per'][window]
        if tot == 0:
            continue
        cat = r['cat']
        if which == 'triv':
            vals.append(res[r['triv']])
        elif which == 'ord2':
            s = [res[k] for k in r['keys'] if cat[k] in ('k0', 'ram2',
                                                          'oth2')]
            if not s:
                continue
            vals.append(sum(s))
        elif which == 'k0diff':
            if r['k0'] is None or r['k0'] == r['triv'] or r['h'] < 4:
                continue
            sib = [res[k] for k in r['keys']
                   if k != r['triv'] and k != r['k0']]
            vals.append(res[r['k0']] - sum(sib) / len(sib))
    if len(vals) < 2:
        return None, None, len(vals)
    mu, se = mean_se(vals)
    return mu, se, len(vals)


def ratio_line(label, a, b, ca=1000, cb=10000):
    """b/a with propagated bars; a = (mu, se) at cut ca, b at cut cb."""
    (ma, sa), (mb, sb) = a, b
    if ma is None or mb is None or abs(ma) < 3 * sa:
        print("  %-34s cut %5d %s   cut %5d %s   ratio undecidable"
              " (denominator under 3 sigma)" % (label, ca, fmt(ma, sa), cb,
                                                 fmt(mb, sb)))
        return None
    rt = mb / ma
    srt = abs(rt) * ((sa / ma) ** 2 + (sb / mb) ** 2) ** 0.5
    alt = prime_square_shape(ca, cb)
    z_alt = (alt - rt) / srt
    print("  %-34s cut %5d %s   cut %5d %s   ratio %.2f +- %.2f"
          "  (prime-square shape %.2f at z %+.1f)"
          % (label, ca, fmt(ma, sa), cb, fmt(mb, sb), rt, srt, alt, z_alt))
    return rt


def per_class_table(rows, window, keep, tag):
    """Mean per-class residual by category, pooled over fields."""
    acc = defaultdict(list)
    for r in rows:
        if r['h'] not in keep:
            continue
        res, tot = r['per'][window]
        if tot == 0:
            continue
        by = defaultdict(list)
        for k in r['keys']:
            by[r['cat'][k]].append(res[k])
        for c, v in by.items():
            acc[c].append(sum(v) / len(v))
    print("  %s per-class residual count per field at [%d, %d):"
          % (tag, window[0], window[1]))
    for c in ('triv', 'k0', 'ram2', 'oth2', 'high'):
        if len(acc[c]) >= 2:
            mu, se = mean_se(acc[c])
            print("    %-5s %s  (%d fields)" % (c, fmt(mu, se), len(acc[c])))


def slope_fit(pts):
    """Least squares y = a + b x with the slope's standard error."""
    n = len(pts)
    mx = sum(x for x, y in pts) / n
    my = sum(y for x, y in pts) / n
    sxx = sum((x - mx) ** 2 for x, y in pts)
    sxy = sum((x - mx) * (y - my) for x, y in pts)
    b = sxy / sxx
    a = my - b * mx
    ss = sum((y - a - b * x) ** 2 for x, y in pts)
    se = (ss / (n - 2) / sxx) ** 0.5
    return b, se, a


# ------------------------------------------------------- the lever sweep
def lever_population(plist):
    """Real narrow fields across BANDS_D at h+ in HPLUS, each with its
    group, orders, places below LEVER_CAP and a qtype closure, in the
    parents' record shape (field, D, G, qtype)."""
    out = []
    small = [p for p in plist if p < LEVER_CAP]
    for (lo, hi) in BANDS_D:
        ds = fundamental_discriminants(lo, hi, +1)
        if len(ds) > NSCAN:
            step = len(ds) / float(NSCAN)
            ds = [ds[int(i * step)] for i in range(NSCAN)]
        got = defaultdict(int)
        t0 = time.time()
        for D in ds:
            rt = isqrt(D)
            if rt * rt == D:
                continue
            recs, member, triv, rt = classes_real(D)
            hplus = len(recs)
            if hplus not in HPLUS or got[hplus] >= NCELL:
                continue
            bad = [0, 0, 0, 0]
            comp = CO.make_composer(D, +1, recs, member, rt, bad)
            orders = CO.class_orders(recs, triv, comp, hplus, bad)
            if orders is None or bad[0] or bad[1]:
                continue
            places = []
            for p in small:
                if p == 2 or D % p == 0 or kronecker(D, p) != 1:
                    continue
                b = form_at(D, p)
                key = member[reduce_form((p, b, (b * b - D) // (4 * p)),
                                         D, rt)]
                places.append((p, key))
            if len(places) < CO.MIN_SPLIT:
                continue
            classes = [(key, orders[key]) for key in sorted(recs)]
            G = SQ.group_deg2(D, +1, recs, orders, triv, member, rt)
            cache = {}

            def qtype(q, D=D, member=member, rt=rt, cache=cache):
                if q in cache:
                    return cache[q]
                t = SQ.type_deg2(D, q)
                key = None
                if t == 1:
                    key = SQ.split_class_deg2(D, +1, q, member, rt)
                elif t == 0:
                    key = SQ.ramified_class_deg2(D, +1, q, member, rt)
                cache[q] = (t, key)
                return cache[q]
            out.append(((hplus, classes, places), D, G, qtype))
            got[hplus] += 1
        print("  band %7d-%8d: scanned %d, kept %s, %.1f s"
              % (lo, hi, len(ds), dict(got), time.time() - t0))
    return out


# ------------------------------------------------------------------ main
def main():
    t0 = time.time()
    plist = primes_upto(CO.PCAP)
    rng = random.Random(SEED)

    def places2(rec):
        return rec[0][2]

    def G2(rec):
        return rec[2]

    def triv2(rec):
        return rec[2].triv

    def corr2(rec, lo, hi):
        return SQ.corr_deg2(rec, lo, hi, plist)

    windows2 = [(0, c) for c in CUTS] + [(0, SCALE_HI)]

    section("THE DEGREE-2 IMAGINARY POPULATION (the parents' sweep)")
    recs_i = SQ.deg2_records(-1, 4000, plist)
    fields_i = [r[0] for r in recs_i]
    keep_i, _ = CV.frozen_strata(fields_i, CV.CUTS, CV.BANDS)
    keep_i = [h for h in keep_i if CV.is_composite(h)]
    print("  %d admissible fields, strata %s" % (len(recs_i), keep_i))
    rows_i = field_rows(recs_i, -1, plist, windows2, places2, corr2, G2,
                        triv2)

    section("C3  THE REPRINT (the parents' corrected generator levels)")
    for c in (1000, 10000):
        out = SQ.read_both(recs_i, keep_i, [(0, c)], "imag", places2,
                           corr2, G2)
        mu = out[(0, c)][1][0]
        ok(abs(mu - IMAG_GEN[c]) < REPRINT_TOL,
           "C3: corrected generator level at cut %d reprints %.4f" % (c, mu))
    worst = 0.0
    for r in rows_i:
        for wnd, (res, tot) in r['per'].items():
            worst = max(worst, abs(sum(res.values())))
    ok(worst < 1e-9, "C3: residuals do not sum to zero (%.3g)" % worst)
    print("  C3 PASSES: levels reprint, residuals sum to zero (worst %.1e)"
          % worst)

    section("C2  THE PLANTED PRIME (the identity of the statistic)")
    worst = 0.0
    for rec in recs_i[:200]:
        G = rec[2]
        w, blind = corr2(rec, 0, 1000)
        res0, _ = residuals(places2(rec), G, 0, 1000, w, blind)
        res1, _ = residuals(list(places2(rec)) + [(3, G.triv)], G, 0, 1000,
                            w, blind)
        for k in G.keys:
            want = (1.0 - 1.0 / G.h) if k == G.triv else (-1.0 / G.h)
            worst = max(worst, abs((res1[k] - res0[k]) - want))
    ok(worst < 1e-9, "C2: planted prime recovered off by %.3g" % worst)
    print("  C2 PASSES: 1 - 1/h on the trivial class, -1/h on each sibling,"
          " exactly (worst %.1e over 200 fields)" % worst)

    section("THE DEGREE-2 REAL NARROW POPULATION (the sibling's sweep)")
    recs_r = SQ.deg2_records(+1, SQ.DBOUND_REAL, plist)
    fields_r = [r[0] for r in recs_r]
    keep_r, _ = CV.frozen_strata(fields_r, CV.CUTS, CV.BANDS)
    keep_r = [h for h in keep_r if CV.is_composite(h)]
    print("  %d admissible fields, strata %s" % (len(recs_r), keep_r))
    rows_r = field_rows(recs_r, +1, plist, windows2, places2, corr2, G2,
                        triv2)

    section("C4  THE KERNEL CLASS")
    bad = 0
    nk0 = 0
    for r, rec in zip(rows_r, recs_r):
        G = rec[2]
        if G.order[r['k0']] > 2:
            bad += 1
        if (r['k0'] == r['triv']) != (r['neps'] == -1):
            bad += 1
        if r['k0'] != r['triv']:
            nk0 += 1
    ok(bad == 0, "C4: %d disagreements" % bad)
    print("  C4 PASSES: k0 has order <= 2 and is trivial iff N(eps) = -1;"
          " %d of %d fields carry a k0" % (nk0, len(rows_r)))

    section("C1  THE NULL (every place re-sorted uniformly, one draw)")
    null_i = field_rows(recs_i, -1, plist, [(0, 1000)], places2, corr2, G2,
                        triv2, scramble=rng)
    null_r = field_rows(recs_r, +1, plist, [(0, 1000)], places2, corr2, G2,
                        triv2, scramble=rng)
    zs = []
    for (tag, rows, keep) in (("imag", null_i, keep_i), ("real", null_r,
                                                          keep_r)):
        for which in ('ord2', 'triv'):
            mu, se, n = pooled(rows, (0, 1000), which, keep)
            if mu is None:
                continue
            zs.append(mu / se)
            print("  null %s %-5s %s  z %+.2f  (%d fields)"
                  % (tag, which, fmt(mu, se), mu / se, n))
    mu, se, n = pooled(null_r, (0, 1000), 'k0diff')
    zs.append(mu / se)
    print("  null real k0diff %s  z %+.2f  (%d fields)" % (fmt(mu, se),
                                                         mu / se, n))
    ok(all(abs(z) < 3.0 for z in zs), "C1: a null statistic is off zero")
    print("  C1 PASSES: every null statistic within 3 sigma of zero")

    section("P1  FLAT IN x AT DEGREE 2 (residual COUNTS per field)")
    ratios = []
    for (tag, rows, keep) in (("imag", rows_i, keep_i), ("real", rows_r,
                                                          keep_r)):
        for which in ('ord2', 'triv'):
            line = []
            for c in CUTS:
                mu, se, n = pooled(rows, (0, c), which, keep)
                line.append((mu, se))
            print("  %s %-5s " % (tag, which) + "  ".join(
                "cut %5d %s" % (c, fmt(mu, se))
                for c, (mu, se) in zip(CUTS, line)))
            a = line[CUTS.index(1000)]
            b = line[CUTS.index(10000)]
            rt = ratio_line("%s %s ratio" % (tag, which), a, b)
            if rt is not None:
                ratios.append(rt)
    print("  P1: decidable ratios %s; PASSES iff every one lies in"
          " [0.5, 2.0]: %s" % (["%.2f" % r for r in ratios],
                               all(0.5 <= r <= 2.0 for r in ratios)))
    for (tag, rows, keep) in (("imag", rows_i, keep_i), ("real", rows_r,
                                                          keep_r)):
        per_class_table(rows, (0, 1000), keep, tag)
        per_class_table(rows, (0, 10000), keep, tag)

    section("P4  THE REAL NARROW SEAT (k0 against its nontrivial siblings)")
    for c in (400, 1000, 10000):
        mu, se, n = pooled(rows_r, (0, c), 'k0diff')
        print("  cut %5d  k0 - siblings %s  z %+.2f  (%d fields, h+ >= 4,"
              " N(eps) = +1)" % (c, fmt(mu, se), mu / se, n))
    mu, se, n = pooled(rows_r, (0, 1000), 'k0diff')
    print("  P4 PASSES iff the cut-1000 value lies in [-1.0, -0.2] at"
          " z <= -2: %s" % (-1.0 <= mu <= -0.2 and mu / se <= -2.0))
    by_h = defaultdict(list)
    for r in rows_r:
        if r['k0'] is None or r['k0'] == r['triv'] or r['h'] < 4:
            continue
        res, tot = r['per'][(0, 1000)]
        sib = [res[k] for k in r['keys'] if k not in (r['triv'], r['k0'])]
        by_h[r['h']].append(res[r['k0']] - sum(sib) / len(sib))
    for h in sorted(by_h):
        if len(by_h[h]) >= 10:
            mu, se = mean_se(by_h[h])
            print("    h+ = %2d  %s  (%d fields)" % (h, fmt(mu, se),
                                                    len(by_h[h])))
    section("R1  POST-RUN READ: THE k0 SEAT AS THE ODD-CHARACTER RACE"
            " (added after the slate was scored; nothing frozen for it)")
    # At h+ = 2 with k0 != triv, D = D1.D2 with both prime discriminants
    # negative, and a split prime's place lies in k0 iff chi_D1(p) = -1:
    # the identity is checked per field, then the classical race sum
    # S(d) = sum_{p <= x} chi_d(p) is averaged over every odd d.
    mism = 0
    nid = 0
    k0res = {1000: [], 10000: []}
    for r, rec in zip(rows_r, recs_r):
        if r['h'] != 2 or r['k0'] == r['triv']:
            continue
        D = r['D']
        pd = []
        for q in plist:
            if q > D:
                break
            if q > 2 and D % q == 0:
                pd.append(q if q % 4 == 1 else -q)
        odd = 1
        for v in pd:
            odd *= v
        two = D // odd
        if two != 1:
            pd.append(two)
        neg = [v for v in pd if v < 0]
        ok(len(pd) == 2 and len(neg) == 2,
           "R1: h+ = 2 field with k0 has D = %d = %s" % (D, pd))
        D1 = neg[0]
        nid += 1
        for c in (1000, 10000):
            diff = 0
            race = 0
            for (q, key) in places2(rec):
                if q < c:
                    diff += 1 if key == r['triv'] else -1
                    race += kronecker(D1, q)
            if diff != race:
                mism += 1
            res, tot = r['per'][(0, c)]
            k0res[c].append(res[r['k0']])
    ok(mism == 0, "R1: %d identity mismatches" % mism)
    print("  identity triv - k0 = sum chi_D1(p) over split p: %d fields,"
          " 0 mismatches at both cuts" % nid)
    for c in (1000, 10000):
        mu, se = mean_se(k0res[c])
        print("  h+ = 2, k0 != triv: k0 residual per field at cut %5d"
              " %s  (%d fields)" % (c, fmt(mu, se), len(k0res[c])))
    # the bare odd race, square-corrected, over every fundamental d < 0,
    # read in bands of |d| against the cut: triv - k0 over split primes is
    # (1/2)(S(D1) + S(D2)), so the k0 residual is -(1/4) of the pair mean
    for c in (1000, 10000):
        sq = 0.5 * sum(1 for q in plist if q * q < c)
        bands = defaultdict(list)
        for d in fundamental_discriminants(1, SQ.DBOUND_REAL, -1):
            s_ = 0
            for q in plist:
                if q >= c:
                    break
                if d % q:
                    s_ += kronecker(d, q)
            for (lo, hi) in ((0, 100), (100, 1000), (1000, 4000),
                             (4000, 16000)):
                if lo <= -d < hi:
                    bands[(lo, hi)].append(s_ + sq)
        print("  bare odd race at cut %5d, mean of sum chi_d(p) + pi(sqrt)/2"
              " over fundamental d < 0 by |d| band (k0 residual = -1/4 of"
              " the pair mean):" % c)
        for (lo, hi), v in sorted(bands.items()):
            mu, se = mean_se(v)
            print("    |d| in [%5d, %5d)  %s  (%d discriminants)"
                  % (lo, hi, fmt(mu, se), len(v)))
        allv = [x for v in bands.values() for x in v]
        mu, se = mean_se(allv)
        print("    all %d discriminants   %s, i.e. the raw race %+.3f"
              " against the term's %+.1f" % (len(allv), fmt(mu, se), mu - sq,
                                             -sq))

    del rows_i, rows_r, null_i, null_r, recs_i, recs_r, fields_i, fields_r
    gc.collect()

    section("THE |D| LEVER (real narrow, five bands, h+ = 2, 4, 8)")
    recs_l = lever_population(plist)
    print("  %d fields" % len(recs_l))
    windows_l = [(0, SCALE_HI), (0, 1000)]
    rows_l = field_rows(recs_l, +1, plist, windows_l, places2, corr2, G2,
                        triv2)

    section("P3  THE |D| SLOPE OF THE TRIVIAL CLASS'S RESIDUAL COUNT")
    verdict = True
    for wnd in windows_l:
        print("  window [%d, %d):" % wnd)
        num = den = 0.0
        for h in HPLUS:
            pts = []
            for r in rows_l:
                if r['h'] != h:
                    continue
                res, tot = r['per'][wnd]
                if tot == 0:
                    continue
                pts.append((log(r['D']), res[r['triv']]))
            if len(pts) < 30:
                print("    h+ = %d: %d fields, too few" % (h, len(pts)))
                continue
            b, se, a = slope_fit(pts)
            norm = (h - 1.0) / h
            print("    h+ = %d  slope %+.4f +- %.4f primes per unit log|D|"
                  "  z %+.2f   /((h-1)/h) = %+.4f   (%d fields)"
                  % (h, b, se, b / se, b / norm, len(pts)))
            num += (b / norm) / (se / norm) ** 2
            den += 1.0 / (se / norm) ** 2
            if wnd == (0, SCALE_HI) and b / se < 2.0:
                verdict = False
            # the band means, for the eye
            bands = defaultdict(list)
            for (x, y) in pts:
                for (lo, hi) in BANDS_D:
                    if log(lo) <= x < log(hi):
                        bands[(lo, hi)].append(y)
            print("      band means: " + "  ".join(
                "%d-%d %s" % (lo, hi, fmt(*mean_se(bands[(lo, hi)])))
                for (lo, hi) in BANDS_D if len(bands[(lo, hi)]) >= 2))
        if den > 0:
            pooled_slope = num / den
            pse = (1.0 / den) ** 0.5
            target = 0.5 / log(wnd[1] - 1)
            print("    pooled normalised slope %+.4f +- %.4f against the"
                  " term's 1/(2 log x) = %.4f" % (pooled_slope, pse, target))
            if wnd == (0, SCALE_HI):
                verdict = verdict and (0.044 <= pooled_slope <= 0.27)
    print("  P3 PASSES iff every h+ slope at p <= 100 is positive at 2"
          " sigma and the pooled normalised slope lies in [0.044, 0.27]:"
          " %s" % verdict)

    section("THE DEGREE-3 PARTIAL FIBER (the parents' base population)")
    recs_3, nmapped = SQ.deg3_records(False)
    fields_3 = [r['field'] for r in recs_3]
    keep_3, _ = CV.frozen_strata(fields_3, CV.CUTS, CV.BANDS)
    print("  %d of %d fields admissible, strata %s" % (len(recs_3), nmapped,
                                                       keep_3))

    section("P2  FLAT IN x AT DEGREE 3 (generator-cell excess count)")
    line = []
    for c in CUBIC_CUTS:
        vals = []
        for rec in recs_3:
            G = rec['G']
            if G.h not in keep_3:
                continue
            w, blind, unalloc = SQ.corr_deg3(rec, 0, c, plist, 'partial')
            res, tot = residuals(rec['field'][2], G, 0, c, w, blind)
            if tot == 0:
                continue
            vals.append(sum(res[k] for k in G.keys if G.order[k] == G.h))
        mu, se = mean_se(vals)
        line.append((mu, se))
        print("  cut %5d  generator excess %s  (%d fields)" % (c, fmt(mu, se),
                                                               len(vals)))
    rt = ratio_line("cubic generator ratio 1000/250", line[0], line[-1],
                    CUBIC_CUTS[0], CUBIC_CUTS[-1])
    print("  P2 PASSES iff the ratio lies in [0.6, 1.6]: %s"
          % (rt is not None and 0.6 <= rt <= 1.6))
    del recs_3

    print("\n%d checks passed, %.1f s wall" % (CHECKS, time.time() - t0))


if __name__ == "__main__":
    main()
