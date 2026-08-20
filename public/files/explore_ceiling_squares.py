r"""THE SQUARE TERM -- is the generator ceiling the prime-power term of the
explicit formula, and is the place law the square map on the Galois
group? (sibling of explore_ceiling_curve.py, explore_ceiling_topband.py,
explore_ceiling_realquad.py and explore_ceiling_fourthcell.py, whose
populations and frozen rules it imports whole and re-reads with one
classical correction added.)

THE QUESTION. Across the ceiling corpus the class of a split prime's
place is graded by its ORDER: the trivial class short, the generators
long, a ceiling of about 1.09 over p < 1000 at both degrees, decaying
with the prime cut as 1/sqrt(x) looks (a factor 8 from cut 250 to
10000, which excludes a constant and a 1/log law), and a TOP-BAND
SURPLUS that both quadratic populations keep (1.043 and 1.061 in
[630, 1000)) while both cubic populations lose it (0.978 and 1.017).
The corpus names the carrier as "the quadratic place" and the
mechanism as underived. This file asks whether the whole of it is one
known term of the Chebotarev explicit formula -- the prime POWERS --
which the corpus's counts exclude and the formula's main term includes.

THE HAND-DERIVATION (pre-engine, on paper).

  (1) WHAT THE EXPLICIT FORMULA PREDICTS FOR A COUNT OF PRIMES. For a
      Galois extension with group G and a conjugacy class C, the
      prime-power count Pi_C(x) = sum over p^k <= x with Frob_p^k in C
      of 1/k has main term (|C|/|G|) Li(x) and an oscillatory remainder
      with no drift. The PRIME count is therefore
        pi_C(x) = (|C|/|G|) Li(x) - (1/2) #{q <= sqrt x : Frob_q^2 in C}
                  - (1/3) #{q <= x^(1/3) : Frob_q^3 in C} - ... + osc.
      So every cell whose population is a Frobenius class is SHORT, at
      the mean, by the weight of the prime powers that land in it --
      the classical Chebyshev bias, which favours the classes that are
      not squares. Over ONE field the oscillation is as large as the
      shift; over a POPULATION of fields the oscillations are
      independent and the shift is what survives the average. The
      corpus averages over populations, so the shift is the prediction.

  (2) THE QUADRATIC FIELD, READ IN THE HILBERT CLASS FIELD H OVER Q.
      Gal(H/Q) is Cl x| {1, s} with s acting by inversion (a place's
      conjugate has the inverse class). A split prime with place class
      b has Frobenius (b, 1), with k-th power (kb, 1). An INERT prime
      has Frobenius (b, s), whose square is (b - b, 1) = the identity:
      every inert prime below sqrt x lands its square on the PRINCIPAL
      class, and on nothing else. So in the corpus's units (one place
      per split prime, cell = the class pair {c, -c}) the correction
      for the cell of c over a norm window [lo, hi) is
        split q, k >= 2, q^k in window : 1/k   at the class k.b
        inert q, k even, q^k in window : 1/k   at the trivial class
        ramified q, k >= 1, q^k in window : 1/(2k) at the class k.r,
      the last because the ramified place r (r^2 principal, so r is
      ambiguous) is a prime ideal of K unramified in H/K, counted by
      the formula and excluded by the corpus -- one ideal where a
      split prime has two, hence the half. The prime 2, which the
      corpus excludes from its count, enters at k = 1 when split.
      Sizes, cumulative to 1000 (pi(31.6) = 11, pi(1000) = 168), with
      the count renormalised by the realised total as the corpus does:
        trivial class        short by (h + |Cl[2]|)/2 * 11/168
        non-trivial square   short by  |Cl[2]|/2      * 11/168
        non-square class     short by  nothing
      so the NON-SQUARES lead equally and the renormalised non-square
      level is 1/(1 - 11/168) = 1.070 against the corpus's 1.093 +-
      0.017; at cut 10000 it is 1/(1 - 25/1229) = 1.021 against the
      measured 1.0240 +- 0.0012 (imaginary) and 1.0246 +- 0.0010
      (real); and in the top band [630, 1000), where only q = 29 and 31
      have squares inside, the two primes' weight against ~54 window
      primes gives 1.038 against the measured 1.043 +- 0.010
      (imaginary) and 1.061 +- 0.007 (real). The trivial
      deficit grows LINEARLY IN h: (h + 2)/2 * 0.0655 predicts 0.87,
      0.80, 0.74 at h = 2, 4, 6 where the corpus's real bottom bin
      reads 0.938, 0.815, 0.764.

  (3) THE VOCABULARY: SQUARES, NOT ORDERS. In a cyclic group of even
      order h = 2^b n the non-squares are exactly the classes whose
      order carries the full 2-part 2^b. At h = 4, 8, 16 those are the
      generators alone, so the order ladder and the square ladder
      coincide and the corpus could not tell them apart. They part at
      h = 6 (order 2 is a non-square, order 3 a square), h = 10 (order
      2 non-square, order 5 square), h = 12 (order 4 non-square, orders
      3 and 6 squares), h = 20 (order 4 non-square, orders 5 and 10
      squares) -- and the corpus's recorded inversions of its order
      ladder are order 3 below order 2 at h = 6 and 12, order 5 below
      order 2 at h = 10 and below order 4 at h = 20: every one of them
      is the square grading showing through the order grading. At odd
      h every class is a square with one root and the prediction is NO
      grading at all beyond the inert term on the trivial class.

  (4) THE CUBIC FIELD, READ IN THE GALOIS CLOSURE OF ITS HILBERT CLASS
      FIELD OVER Q. Let L be the S_3 closure of the non-Galois cubic K
      and M the closure of H over Q. A prime is totally split (three
      degree-1 places, Frobenius the identity in S_3), partial (one
      degree-1 place and one of degree 2, Frobenius a transposition)
      or inert (a 3-cycle). Squares in S_3 are the identity and the
      3-cycles: A TRANSPOSITION IS NEVER A SQUARE. So the PARTIAL fiber
      -- which is the population every cubic ceiling in the corpus
      reads (explore_ceiling_curve.py's build_pop3 keeps the partial
      primes' degree-1 place and nothing else) -- carries NO
      prime-square term: its only prime-power term is the cube of a
      partial prime's own Frobenius, at weight 1/3 on the class 3a for
      q <= x^(1/3), and at cut 1000 that is q <= 10. The TOTALLY SPLIT
      fiber carries them all: a totally split q below sqrt x lands its
      square on the triple 2.(b1, b2, b3); a partial q below sqrt x
      lands its square on the triple (2a, -a, -a) -- derived from the
      three primes of L above q, one lying over the degree-1 place
      with residue degree 2 (Artin class 2a) and two over the degree-2
      place with residue degree 1 (Artin class -a each); and an inert
      q below x^(1/3) lands its cube on (0, 0, 0). The triple form of
      the correction is checked inside the engine: every target triple
      sums to zero, as every totally split triple must.

  (5) WHAT THIS SAYS THE PLACE LAW IS. Not "a quadratic place keeps the
      surplus and a formless place loses it": a population whose
      Frobenius class is a SQUARE IN ITS GALOIS GROUP carries the
      prime-power term, and one whose class is not carries none. The
      quadratic split primes are squares (the inert Frobenius squares
      to the identity, the split one to the doubled class); the cubic
      partial primes are transpositions. The unit rank, the form, the
      signature are all invisible to this, which is what the fourth
      cell measured. And it makes a NEW prediction the corpus never
      read: the cubic's TOTALLY SPLIT places must keep the surplus, and
      keep MORE of it -- the weight (1/6 + 1/2) of all primes below
      sqrt x lands on a fiber of size 1/6, a relative deficit four
      times a quadratic field's 1/2 on 1/2 per prime but spread over
      three places and two triples, which the band arithmetic below
      puts at about 1.08 in the top band against the quadratic 1.04.

  (6) THE STATISTIC'S ALGEBRA. The corrected count of a cell is the
      counted places plus the cell's correction weight; the corrected
      total is the counted total plus the summed weights; the level is
      corrected count over (corrected total x nominal share). The
      correction is at most 13 % of the total at cut 250 and 2 % at
      10000, so the denominator never nears zero and the level's
      variance is the parent's to within the same factor. A correction
      can be fractional; a cell's count can fall below its correction
      only by being empty, which the cell floors already exclude. Every
      other rule -- the admissibility floor, the cyclic profile, the
      stratum floors, the dispersion scale, the inverse-variance mean
      -- is imported from explore_ceiling_curve.py unchanged, and the
      RAW column of every table must reprint the parents' figures.

  (7) WHAT IS NOT CONTROLLED. (a) At x well below the discriminant the
      oscillatory remainder carries the geometry -- no split prime
      below |D|/4 is principal in an imaginary field -- and a population
      average does not remove a term that has one sign in every field;
      the corrected trivial class is therefore read, never predicted,
      and the reads that decide are the tail and the top band, where x
      has passed the discriminants. (b) The cubic fibers omit the prime
      2 (the class maps walk odd primes) and the ramified primes: their
      weight is computed and printed as an UNALLOCATED bound per window,
      zero in every band above 300. (c) The correction's size in the
      top band rests on two primes, 29 and 31, per field -- a coarse
      instrument the population count makes fine.

THE DESIGN (`--wide` swaps the cubic population for the top-band
sibling's 1274-field one to |d| <= 24000, the read that decides P5 at
the base population's four times the cell). Degree 2: the parents'
imaginary sweep to |D| <= 4000 and the real sweep to D <= 16000 (narrow
classes), the parents' admissible fields and frozen strata; each field's
class group re-equipped with doubling, negation and k-th powers through
the parents' own composer;
the correction of (2) accumulated per field per window over every
prime q < hi. Degree 3: the parents' base population to |d| <= 6000
with its class maps; the partial fiber re-read with the cube term, the
totally split fiber read for the first time, both with the correction
of (4). Every table prints RAW beside CORRECTED, by order cell and by
square cell.

THE SLATE -- PREDICTIONS FROZEN BEFORE THE ENGINE.

  P1  THE TAIL IS THE SQUARE TERM. The corrected imaginary generator
      level at cuts 2500 and 10000 lies within +-0.010 of 1 (raw
      1.0240 +- 0.0012 at 10000), and the prime-power terms account
      for at least 70 % of the raw surplus at every cut from 630 up.
  P2  THE TOP BAND IS THE SQUARE TERM AT BOTH QUADRATIC SIGNS. The
      corrected top-band generator level is within 2 sigma of 1 on the
      imaginary side (raw 1.0426 +- 0.0101) and on the real narrow
      side (raw 1.0613 +- 0.0069).
  P3  SQUARES GRADE, ORDERS DO NOT. On the raw imaginary (h, order)
      table at p < 1000 with order 1 excluded, grouping the cells by
      squareness scores a lower within-group SS per degree of freedom
      than grouping by order; and the non-square, non-generator cells
      (order 2 at h = 6 and 10, order 4 at h = 12 and 20) sit within
      2 sigma of their stratum's generator level where they are
      readable.
  P4  THE PARTIAL FIBER HAS NO SQUARE TERM. The cubic partial
      population's correction moves no cut or band level by more than
      0.005; its raw figures reprint the parents' (1.246, 1.201, 1.163,
      1.096 cumulative) to 0.0015.
  P5  THE TOTALLY SPLIT PLACES KEEP THE SURPLUS. The raw non-square
      level of the cubic's totally split places in the top band
      [630, 1000) reads above 1 by at least 3 sigma and at least 1.05,
      and its corrected level lies within 2 sigma of 1.

THE CONTROLS, run before any prediction is read.

  C1  THE ARITHMETIC-PROGRESSION RACE, the classical instance. Primes
      to 10^7 in the residue classes of every odd prime modulus below
      400: the non-residue classes' pooled level over the residue
      classes' has predicted mean 1 + pi(sqrt x)/pi(x) (every residue
      class short by a weight of two half-squares); the measured mean
      over the moduli must lie within a factor 2 of the prediction and
      more than 2 sigma from 0; and the same counts corrected by the
      same prime-power rule must read within 2 sigma of 1.
  C2  THE WEIGHT IDENTITY. Per field and window, the summed
      correction over cells equals the summed prime-power weight
      computed with no class data at all, exactly.
  C3  THE REPRINT. Every raw figure the parents froze reprints:
      degree-2 imaginary cuts and top band, real narrow top band,
      degree-3 cumulative ladder.
  C4  THE TRIPLES SUM TO ZERO. Every totally split triple and every
      correction triple of (4) sums to the trivial class.

THE FINDINGS (the post-run record; every number is a print of the run).

  CONTROLS. C1: over 77 odd prime moduli below 400 at x = 10^7 the raw
  non-residue lead reads 0.00077 +- 0.00010, 1.15 times the predicted
  pi(sqrt x)/pi(x) = 0.00067 and 8.0 sigma from 0; the corrected lead
  reads 0.00009 +- 0.00010 (0.9 sigma). C2: exact at every field and
  window. C3: the imaginary cuts 1000 and 10000 and top band, the real
  top band and the degree-3 cumulative ladder all reprint inside
  0.0015. C4: 0 triples off zero.

  F1  THE IMAGINARY GENERATOR CEILING IS THE PRIME-POWER TERM, WHOLE
      (rule in range; P1 and P2 PASS). Raw against corrected, the
      parents' generator cell over the strata h = 6, 8, 10, 12, 14:
        cut   250   1.1926 +- 0.0073  ->  1.0275 +- 0.0058   (86 %)
        cut   400   1.1551 +- 0.0055  ->  1.0140 +- 0.0047   (91 %)
        cut   630   1.1095 +- 0.0046  ->  1.0016 +- 0.0041   (99 %)
        cut  1000   1.0875 +- 0.0035  ->  1.0011 +- 0.0033   (99 %)
        cut  2500   1.0569 +- 0.0022  ->  1.0046 +- 0.0021   (92 %)
        cut 10000   1.0240 +- 0.0012  ->  1.0000 +- 0.0011  (100 %)
        band 630-1000  1.0426 +- 0.0101  ->  1.0001 +- 0.0097 (z +0.01).
      The decay the corpus measured as "a factor 8 against the 1.7 a
      1/log law allows" is the term's own, pi(sqrt x)/pi(x) at leading
      order. And the WHOLE TABLE
      flattens, not the generator cell alone: at p < 10000 every
      (h, order) cell of the five strata reads within 0.03 of 1
      corrected, the trivial class from 0.84-0.93 raw to 0.97-1.00,
      the generators from 1.021-1.029 to 0.998-1.004; at p < 1000
      the trivial class moves from 0.52-0.79 raw (the deficit that
      deepens with h) to 0.96-1.02, the generators from 1.08-1.10 to
      0.996-1.008, the order-2 cells from 0.94-1.04 to 1.02-1.09 and
      the odd-order square cells from 0.99-1.01 to 0.97-0.99. The
      h-grading of the principal deficit is the inert primes' squares
      (weight 1/2 each, all on the principal class) and the ramified
      ideals (1/2 each on an ambiguous class), which is why it scales
      with h and with the 2-rank and why the corpus could read it as a
      |D| grading: |D| sets h.

  F2  THE REAL NARROW SIDE IS THE SAME TERM TO THREE QUARTERS OR MORE,
      WITH A RESIDUAL THAT DIES BY 10000 (observation; P2 fails its
      2-sigma letter there). Generator cell: cut 1000 1.1041 +- 0.0028
      -> 1.0190 +- 0.0025 (82 %), cut 10000 1.0246 +- 0.0010 -> 1.0008
      +- 0.0009 (97 %), top band 1.0613 +- 0.0069 -> 1.0151 +- 0.0066
      (75 %, z +2.3). Per cell at p < 1000 the residual has a shape:
      the order-2 cells stay short after correction (0.944, 0.920,
      0.875, 0.822 at h = 4, 6, 8, 10 against raw 0.917, 0.940, 0.814,
      0.816) and the generators a little long (1.017, 1.014, 1.036,
      1.013); at p < 10000 every cell sits within 0.024 of 1.

  F3  SQUARES GRADE WHERE ORDERS INVERT, AND THE RAMIFIED TERM IS WHY
      THE ORDER-2 NON-SQUARE IS NOT A GENERATOR (P3: the ranking half
      passes, the cell half fails on two of four cells). On the raw
      imaginary table at p < 1000 (11 cells, order 1 excluded) the
      within-group SS per degree of freedom reads 0.0745 grouped by
      squareness against 0.0955 grouped by order. The non-square
      non-generator cells against their stratum's generator: h = 12
      order 4 at 1.092 +- 0.017 against 1.087 (z +0.2) and h = 10
      order 2 at 1.038 +- 0.030 against 1.088 (z -1.6) sit at the
      ceiling; h = 6 order 2 at 1.019 +- 0.012 against 1.101 (z -5.4)
      and h = 14 order 2 at 0.970 +- 0.038 against 1.091 (z -3.1) do
      not -- and those are the cells the ramified ideals land on: at
      2-rank 1 the one ambiguous non-trivial class IS the order-2
      class, and each ramified prime in the window puts 1/2 there.
      Corrected, both read flat (1.018 and 1.055). So the grading is
      not "the order" and not "squareness" alone: it is the prime-power
      weight each class receives -- squares of split primes on 2Cl,
      squares of inert primes on the identity, ramified ideals on
      Cl[2].

  F4  THE CUBIC PARTIAL FIBER CARRIES NO SQUARE TERM, AND ITS LOW-CUT
      SURPLUS IS THEREFORE NOT THIS (P4 PASSES, to 0.0064 at one cut).
      The partial population's levels move under the cube term by at
      most 0.0064 (cut 250), by 0.0032 at cut 1000 and by 0.0000 in
      the top band, with 0.79 % of the cut-1000 weight unallocated
      (the prime 2) and none in any band. Its raw ladder 1.246, 1.201,
      1.163, 1.096 and top band 0.963 +- 0.040 stand as printed. So the
      cubic surplus the parents measured at low cuts is a different
      object from the quadratic one: it is not a prime-power term, it
      is larger at cut 250 than the quadratic's, and it is gone by the
      top band, where the quadratic term is still 4 % and still
      exactly the square term.

  F5  THE TOTALLY SPLIT PLACES (P5). On the base population (227
      fields, strata h = 4 and 6) the split places' generator cell
      reads 1.073 +- 0.051 raw and 1.065 +- 0.045 corrected in the top
      band (z +1.4 both), with NO ladder at the low cuts (1.024, 0.978,
      1.018, 1.036 at cuts 250 to 1000). And derivation (5) mis-sized
      this fiber's correction: the exact weights put 2.25 place-weights
      per field in the band against 26.4 counted places, but two
      thirds of a partial prime's (2a, -a, -a) lands on classes of a's
      own squareness, so the generator cell receives about half the
      weight and its corrected level moves by 0.008, not 0.05; the
      square term predicts a split-place generator surplus near 1.01,
      not 1.08. ON THE WIDE POPULATION (`--wide`: 1274 admissible fields
      over strata h = 4, 6, 8, 9, 10, 12) the split places' generator
      cell reads 1.0188 +- 0.0138 raw in the top band (z +1.4) and
      0.9913 +- 0.0128 corrected (z -0.7); the non-square cell 1.0061
      +- 0.0144 raw, 0.9732 +- 0.0134 corrected. So P5 FAILS as frozen
      -- the 1.05 bar was derivation (5)'s error -- and the fiber reads
      exactly as the square term says it should: its CUMULATIVE ladder
      1.1154, 1.0858, 1.0626, 1.0479 (cuts 250 to 1000) corrects to
      1.0448, 1.0220, 1.0100, 1.0041 +- 0.0053, 61 % to 92 % of it the
      prime-power term, while the partial fiber's ladder on the same
      fields, 1.1431, 1.1100, 1.0795, 1.0468, does not move (largest
      move 0.0017, top band 0.9780 +- 0.0123 reprinted). THE PLACE LAW,
      RESTATED: a population carries the term's leading piece, the
      prime SQUARES, iff its Frobenius class is a SQUARE in its Galois
      group -- the quadratic
      split primes (identity squared, inert squared) and the cubic
      totally split primes (identity and transposition squared) do,
      and the term is removed exactly on both; the cubic partial primes
      (transpositions) carry none. The form, the signature and the
      unit rank are invisible to it. What the partial primes DO carry
      -- a ladder of 1.14 to 1.05 over cuts 250 to 1000 on the wide
      population, 1.25 to 1.10 on the base one, gone by the top band --
      is a second object no prime-power term produces, and it is the
      open front this file leaves.

WIDE-RUN RECORD. Same date and command with `--wide`: 4770 checks
passed, 763.0 s wall, peak working set 398.9 MB; 3 fields excluded
unresolved by the sibling's own policy (-7699, -7771, -23928).

RUN RECORD. 2026-08-20, Windows 11, Python 3, `python
prime/code/memwatch.py --limit 512 prime/code/explore_ceiling_squares.py`.
One process, CPython, no BLAS. 2679 checks passed, 224.5 s wall, peak
working set 398.7 MB against the 512 MB ceiling. An earlier run of the
same engine printed the corrected and the raw non-square columns under
each other's labels (a tuple unpacked in the wrong order); the
arithmetic was unchanged and the run above is the corrected print.
"""

import os
os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")

import sys
import time
from collections import Counter, defaultdict
from math import isqrt

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import explore_ceiling_curve as CV                 # noqa: E402
import explore_cubic_transposition as XT           # noqa: E402
import explore_cubic_split_triple as ST            # noqa: E402
import explore_cubic_field_shop as CFS             # noqa: E402
import explore_class_order as CO                   # noqa: E402
from explore_class_share import classes_real       # noqa: E402
from explore_principal_share import (              # noqa: E402
    primes_upto, kronecker, form_at, reduce_definite, reduce_form)

CHECKS = 0
CUTS = CV.CUTS
EXT_CUTS = CV.EXT_CUTS
BANDS = CV.BANDS
TOP = BANDS[-1]
DBOUND_REAL = 16000
MIN_CELL = CV.MIN_CELL

# the parents' frozen prints (C3)
IMAG_CUT1000 = 1.0875
IMAG_CUT10K = 1.0240
IMAG_TOP = (1.0426, 0.0101)
REAL_TOP = (1.0613, 0.0069)
DEG3_CUM = (1.246, 1.201, 1.163, 1.096)
DEG3_TOP = (0.9780, 0.0123)       # the wide population's top band
REPRINT_TOL = 0.0015

AP_X = 10 ** 7
P3_MINCELL = 20           # fields an (h, order) cell needs; strata hold 40-50
AP_MODULI_CAP = 400


def ok(cond, msg):
    global CHECKS
    CHECKS += 1
    if not cond:
        print("  FAIL: " + msg)
        sys.exit(1)


def section(t):
    print("\n" + "=" * 72 + "\n" + t + "\n" + "=" * 72)


def phi(n):
    return CV.phi(n)


def mean_se(vals):
    return CV.mean_se(vals)


# ----------------------------------------------------------- the groups
class Group:
    """A finite abelian class group with its cells: order, squareness."""

    def __init__(self, keys, order, triv, add):
        self.keys = list(keys)
        self.order = dict(order)
        self.triv = triv
        self.add = add
        self.h = len(self.keys)
        self.dbl = {k: add(k, k) for k in self.keys}
        self.squares = set(self.dbl.values())
        self.nroots = defaultdict(int)
        for k in self.keys:
            self.nroots[self.dbl[k]] += 1
        self._pow = {}

    def mul(self, k, n):
        """n.k by repeated addition, memoised."""
        if (k, n) in self._pow:
            return self._pow[(k, n)]
        acc = self.triv
        for _ in range(n):
            acc = self.add(acc, k)
        self._pow[(k, n)] = acc
        return acc

    def neg(self, k):
        return self.mul(k, self.h - 1)

    def sq_cell(self, k):
        if k == self.triv:
            return 'triv'
        return 'sq' if k in self.squares else 'nsq'

    def sq_share(self):
        n = defaultdict(int)
        for k in self.keys:
            n[self.sq_cell(k)] += 1
        return {c: n[c] / float(self.h) for c in n}


def group_deg2(D, sign, recs, orders, triv, member, rt):
    bad = [0, 0, 0, 0]
    comp = CO.make_composer(D, sign, recs, member, rt, bad)

    def add(u, v):
        w = comp(u, v)
        if w is None:
            raise RuntimeError("composition failed at D=%d" % D)
        return w
    return Group(recs, orders, triv, add)


def group_deg3(piv, k, H):
    grid = [[0] * k]
    for (cc, row) in piv:
        n = abs(row[cc])
        grid = [q[:cc] + [t] + q[cc + 1:] for q in grid for t in range(n)]
    keys = [XT.reduce_vec(r, piv) for r in grid]
    ok(len(set(keys)) == H, "degree-3 grid is not the group")
    order = {key: XT.class_order(list(key), piv, H) for key in keys}
    triv = XT.reduce_vec([0] * k, piv)

    def add(u, v):
        return XT.reduce_vec([x + y for x, y in zip(u, v)], piv)
    return Group(keys, order, triv, add)


# ---------------------------------------------- degree-2 field records
def split_class_deg2(D, sign, q, member, rt):
    """The key of one place above the split prime q (q = 2 allowed)."""
    if q == 2:
        b = 1
    else:
        b = form_at(D, q)
    num = b * b - D
    f = (q, b, num // (4 * q))
    if sign < 0:
        return reduce_definite(f, D)
    return member[reduce_form(f, D, rt)]


def ramified_class_deg2(D, sign, q, member, rt):
    """The key of the ramified place above q | D."""
    for b in (0, q):
        if (b * b - D) % (4 * q) == 0:
            f = (q, b, (b * b - D) // (4 * q))
            if sign < 0:
                return reduce_definite(f, D)
            return member[reduce_form(f, D, rt)]
    raise RuntimeError("no ramified form at D=%d q=%d" % (D, q))


def type_deg2(D, q):
    if q == 2:
        if D % 2 == 0:
            return 0
        return 1 if D % 8 == 1 else -1
    return kronecker(D, q)


def deg2_records(sign, bound, plist):
    """[(field, D, G, qtype)] over the parents' sweep, the admissible
    fields only. field = (h, classes, places) as the parents build it;
    qtype(q) -> (type, key) with the class for split and ramified q."""
    old = CO.DBOUND
    CO.DBOUND = bound
    try:
        rows, bad, id_bad, c2_bad, c4_bad, law_bad = CO.sweep(sign, plist)
    finally:
        CO.DBOUND = old
    print("  sweep: %d fields, composition failures %s, identity %d,"
          " order-vs-ambiguous %d, minimum %d, law %s"
          % (len(rows), bad, id_bad, c2_bad, c4_bad, law_bad))
    ok(bad[2] == 0 and bad[3] == 0, "the order walk failed")
    out = []
    for r in rows:
        (D, hplus, recs, orders, n0, tot0, qfirst, hits) = r
        fs = CV.build_pop2([r])
        if not fs or not CV.admissible(fs, CUTS[0], CO.MIN_SPLIT):
            continue
        field = fs[0]
        if sign < 0:
            member, rt = None, None
            triv = [k for k in recs if recs[k][0]][0]
        else:
            recs_r, member, triv, rt = classes_real(D)
            ok(set(recs_r) == set(recs), "real class records differ")
        G = group_deg2(D, sign, recs, orders, triv, member, rt)
        cache = {}

        def qtype(q, D=D, sign=sign, member=member, rt=rt, cache=cache):
            if q in cache:
                return cache[q]
            t = type_deg2(D, q)
            key = None
            if t == 1:
                key = split_class_deg2(D, sign, q, member, rt)
            elif t == 0:
                key = ramified_class_deg2(D, sign, q, member, rt)
            cache[q] = (t, key)
            return cache[q]
        out.append((field, D, G, qtype))
    del rows
    cnt = defaultdict(int)
    for (f, D, G, qt) in out:
        cnt[f[0]] += 1
    out = [rec for rec in out if cnt[rec[0][0]] >= CV.MINSTRAT]
    return out


def corr_deg2(rec, lo, hi, plist):
    """Correction weights per class key over the norm window [lo, hi),
    in the corpus's units (one place per split prime); and the
    class-free total (C2)."""
    (field, D, G, qtype) = rec
    w = defaultdict(float)
    blind = 0.0
    for q in plist:
        if q >= hi:
            break
        t, key = qtype(q)
        n, k = q, 1
        while n < hi:
            if n >= lo:
                if t == 1:
                    if k >= 2:
                        w[G.mul(key, k)] += 1.0 / k
                        blind += 1.0 / k
                    elif q == 2:
                        w[key] += 1.0
                        blind += 1.0
                elif t == -1:
                    if k % 2 == 0:
                        w[G.triv] += 1.0 / k
                        blind += 1.0 / k
                else:
                    w[G.mul(key, k)] += 0.5 / k
                    blind += 0.5 / k
            n *= q
            k += 1
    return w, blind


# ---------------------------------------------- degree-3 field records
def type2_deg3(a, b, c, d):
    """The splitting type of 2 when 2 does not divide the index: 2 is
    never totally split; 'partial' iff f has a root mod 2."""
    if d % 2 == 0:
        return 'ramified'
    pdisc = CFS.poly_disc3(a, b, c)
    idx = isqrt(abs(pdisc) // abs(d))
    if idx * idx * abs(d) != abs(pdisc) or idx % 2 == 0:
        return 'unknown'
    roots = [x for x in (0, 1) if (x ** 3 + a * x * x + b * x + c) % 2 == 0]
    return 'partial' if roots else 'inert'


def deg3_records(wide=False):
    if wide:
        import explore_ceiling_topband as TB
        recs = TB.wide_class_reading()
    else:
        recs = XT.s1_population()
        XT.s2_pin(recs)
    mapped = XT.s3_profiles(recs)
    del recs
    pop3 = CV.build_pop3(mapped)
    ok(len(pop3) == len(mapped), "build_pop3 dropped a field")
    out = []
    for (m, f) in zip(mapped, pop3):
        if not CV.admissible([f], CUTS[0], CV.MIN_TOT):
            continue
        (d, cx, a, b, c, O, H, piv, k, per_prime, prof) = m
        G = group_deg3(piv, k, H)
        ok(set(G.keys) == set(key for (key, o) in f[1]),
           "degree-3 group keys differ from the parent's")
        types = {}
        ts = []
        dropped = 0
        for (p, kd, vecs) in per_prime:
            if any(v is None for v in vecs):
                dropped += 1
                types[p] = 'dropped'
                continue
            if kd == 'split':
                tri = tuple(XT.reduce_vec(v, piv) for v in vecs)
                types[p] = ('split', tri)
                ts.append((p, tri))
            else:
                types[p] = ('partial', XT.reduce_vec(vecs[0], piv))
        t2 = type2_deg3(a, b, c, d)
        out.append(dict(field=f, d=d, G=G, types=types, ts=sorted(ts),
                        t2=t2, dropped=dropped))
    return out, len(mapped)


def qtype_deg3(rec, q):
    if q == 2:
        return rec['t2'], None
    t = rec['types'].get(q)
    if t is None:
        return ('ramified', None) if rec['d'] % q == 0 else ('inert', None)
    if t == 'dropped':
        return 'unknown', None
    return t


def corr_deg3(rec, lo, hi, plist, fiber):
    """Correction weights per class key for the PARTIAL fiber (one place
    per prime) or the TOTALLY SPLIT fiber (three places per prime), and
    the unallocated weight from primes of unknown class."""
    G = rec['G']
    w = defaultdict(float)
    blind = 0.0
    unalloc = 0.0
    for q in plist:
        if q >= hi:
            break
        t, data = qtype_deg3(rec, q)
        n, k = q, 1
        while n < hi:
            if n >= lo:
                if fiber == 'partial':
                    if k % 2 == 1 and k >= 3 and t in ('partial', 'unknown'):
                        if t == 'partial' and data is not None:
                            w[G.mul(data, k)] += 1.0 / k
                            blind += 1.0 / k
                        else:
                            unalloc += 1.0 / k
                    elif k == 1 and q == 2 and t in ('partial', 'unknown'):
                        unalloc += 1.0          # 2 is excluded from the count
                else:
                    if t == 'split' and k >= 2:
                        for b in data:
                            w[G.mul(b, k)] += 1.0 / k
                        blind += 3.0 / k
                    elif t == 'partial' and k % 2 == 0:
                        a = data
                        if a is None:
                            unalloc += 3.0 / k
                        else:
                            w[G.mul(a, k)] += 1.0 / k
                            w[G.neg(G.mul(a, k // 2))] += 2.0 / k
                            blind += 3.0 / k
                    elif t == 'inert' and k % 3 == 0:
                        w[G.triv] += 3.0 / k
                        blind += 3.0 / k
                    elif t == 'unknown' and k >= 2:
                        unalloc += 3.0 / k
            n *= q
            k += 1
    return w, blind, unalloc


# ------------------------------------------------------------ the cells
def strata_table(recs, lo, hi, places_of, corr_of, G_of, corrected):
    """The parents' stratum_cells with an optional correction; also the
    square cells. Returns (strata, sqcells) with strata in the parents'
    shape so within_scale/curve_point read it unchanged."""
    strata = {}
    sq = {}
    for rec in recs:
        G = G_of(rec)
        h = G.h
        tot = 0
        cnt = defaultdict(float)
        cnt_sq = defaultdict(float)
        for (p, key) in places_of(rec):
            if lo <= p < hi:
                tot += 1
                cnt[G.order[key]] += 1
                cnt_sq[G.sq_cell(key)] += 1
        if tot == 0:
            continue
        tot_c = float(tot)
        if corrected:
            w, blind = corr_of(rec, lo, hi)[:2]
            for key, wt in w.items():
                cnt[G.order[key]] += wt
                cnt_sq[G.sq_cell(key)] += wt
                tot_c += wt
        s = strata.setdefault(h, dict(obs=defaultdict(float),
                                      exp=defaultdict(float),
                                      gpf=[], epf=[], res=[]))
        for d in range(1, h + 1):
            if h % d == 0:
                s['obs'][d] += cnt.get(d, 0.0)
                s['exp'][d] += tot_c * phi(d) / float(h)
        q = phi(h) / float(h)
        g = cnt.get(h, 0.0)
        s['gpf'].append(g * h / (tot_c * float(phi(h))))
        l1 = cnt.get(1, 0.0) * h / tot_c
        s['epf'].append(g * h / (tot_c * float(phi(h)))
                        - (h - l1) / float(h - 1))
        e = tot_c * q
        if e >= CV.MIN_SCALE_EXP and q < 1.0:
            s['res'].append((g - e) / (e * (1 - q)) ** 0.5)
        share = G.sq_share()
        t = sq.setdefault(h, dict(obs=defaultdict(float),
                                  exp=defaultdict(float), share=share))
        for c in ('triv', 'sq', 'nsq'):
            if c in share:
                t['obs'][c] += cnt_sq.get(c, 0.0)
                t['exp'][c] += tot_c * share[c]
    return strata, sq


def read_point(strata, keep):
    scale, nsc = CV.within_scale(strata, keep)
    mu, se, pts = CV.curve_point(strata, keep, scale)
    return mu, se, pts, scale


def nsq_point(sq, strata, keep, scale):
    """Pooled non-square level over the readable strata, with the same
    scaled binomial bars as the generator cell."""
    pts = []
    for h in keep:
        t = sq.get(h)
        if t is None or 'nsq' not in t['share'] or t['exp']['nsq'] < MIN_CELL:
            continue
        q = t['share']['nsq']
        sd = scale * ((1 - q) / t['exp']['nsq']) ** 0.5
        pts.append((h, t['obs']['nsq'] / t['exp']['nsq'], sd))
    if not pts:
        return None, None, []
    w = [1.0 / (sd * sd) for (h, l, sd) in pts]
    mu = sum(wi * l for wi, (h, l, sd) in zip(w, pts)) / sum(w)
    return mu, (1.0 / sum(w)) ** 0.5, pts


def fmt(mu, se):
    if mu is None:
        return "   --   "
    return "%.4f +- %.4f" % (mu, se)


def read_both(recs, keep, windows, tag, places_of, corr_of, G_of):
    """RAW beside CORRECTED, generator cell and non-square cell, over a
    list of windows. Returns {window: (raw, corr, raw_nsq, corr_nsq)}
    with each entry (mu, se)."""
    out = {}
    for (lo, hi) in windows:
        label = ("cut %5d" % hi) if lo == 0 else ("band %4d-%4d" % (lo, hi))
        row = []
        for corrected in (False, True):
            strata, sq = strata_table(recs, lo, hi, places_of, corr_of,
                                      G_of, corrected)
            mu, se, pts, scale = read_point(strata, keep)
            mn, sn, _ = nsq_point(sq, strata, keep, scale)
            row.append((mu, se))
            row.append((mn, sn))
        (r, rn, c, cn) = row      # raw gen, raw nsq, corr gen, corr nsq
        out[(lo, hi)] = (r, c, rn, cn)
        expl = None
        if r[0] is not None and c[0] is not None and r[0] != 1.0:
            expl = (r[0] - c[0]) / (r[0] - 1.0)
        print("  %s %-14s gen raw %s  corr %s   nsq raw %s  corr %s%s"
              % (tag, label, fmt(*r), fmt(*c), fmt(*rn), fmt(*cn),
                 ("   explained %.2f" % expl) if expl is not None else ""))
    return out


def order_cells(recs, lo, hi, places_of, G_of):
    """Per-field order ratios by (h, order), raw, the parents' table."""
    cells = defaultdict(list)
    sqcell = {}
    nfield = defaultdict(int)
    for rec in recs:
        G = G_of(rec)
        h = G.h
        tot = 0
        cnt = defaultdict(int)
        for (p, key) in places_of(rec):
            if lo <= p < hi:
                tot += 1
                cnt[G.order[key]] += 1
        if tot == 0:
            continue
        nfield[h] += 1
        for key in G.keys:
            sqcell[(h, G.order[key])] = G.sq_cell(key)
        prof = defaultdict(int)
        for key in G.keys:
            prof[G.order[key]] += 1
        for o, m in prof.items():
            cells[(h, o)].append(cnt.get(o, 0) * h / float(tot * m))
    return cells, sqcell, nfield


# ------------------------------------------------------- the AP control
def ap_control():
    section("C1  THE ARITHMETIC-PROGRESSION RACE (the classical instance)")
    t0 = time.time()
    plist = primes_upto(AP_X)
    pi_x = len(plist)
    pi_sqrt = sum(1 for p in plist if p * p <= AP_X)
    pred = pi_sqrt / float(pi_x)
    print("  pi(10^7) = %d, pi(sqrt) = %d, predicted non-residue lead"
          " %.5f" % (pi_x, pi_sqrt, pred))
    moduli = [m for m in primes_upto(AP_MODULI_CAP) if m >= 3]
    leads, cleads = [], []
    for m in moduli:
        res = set((x * x) % m for x in range(1, m))
        cnt = Counter(p % m for p in plist if p != m)
        corr = defaultdict(float)
        for q in plist:
            if q == m:
                continue
            n, k = q * q, 2
            while n <= AP_X:
                corr[n % m] += 1.0 / k
                n *= q
                k += 1
        nr = sum(cnt[c] for c in range(1, m) if c not in res)
        rs = sum(cnt[c] for c in res)
        nrc = nr + sum(corr[c] for c in range(1, m) if c not in res)
        rsc = rs + sum(corr[c] for c in res)
        leads.append(nr / float(rs) - 1.0)
        cleads.append(nrc / rsc - 1.0)
    m1, s1 = mean_se(leads)
    m2, s2 = mean_se(cleads)
    print("  %d odd prime moduli < %d, %.1f s" % (len(moduli), AP_MODULI_CAP,
                                                  time.time() - t0))
    print("  raw  non-residue lead  %.5f +- %.5f   (%.2f x predicted,"
          " z %+.2f from 0)" % (m1, s1, m1 / pred, m1 / s1))
    print("  corrected lead         %.5f +- %.5f   (z %+.2f from 0)"
          % (m2, s2, m2 / s2))
    ok(0.5 * pred < m1 < 2.0 * pred and m1 / s1 > 2.0,
       "C1: the raw lead is not the predicted size")
    ok(abs(m2 / s2) < 2.0, "C1: the corrected lead is not flat")
    print("  C1 PASSES")


# ------------------------------------------------------------------ main
def main():
    t0 = time.time()
    ap_control()
    plist = primes_upto(CO.PCAP)

    section("THE DEGREE-2 IMAGINARY POPULATION (the parents' sweep)")
    recs_i = deg2_records(-1, 4000, plist)
    fields_i = [r[0] for r in recs_i]
    keep_i, keep_ib = CV.frozen_strata(fields_i, CUTS, BANDS)
    keep_i = [h for h in keep_i if CV.is_composite(h)]
    keep_ib = [h for h in keep_ib if CV.is_composite(h)]
    print("  %d admissible fields, cumulative strata %s, band strata %s"
          % (len(recs_i), keep_i, keep_ib))

    def places2(rec):
        return rec[0][2]

    def G2(rec):
        return rec[2]

    def corr2(rec, lo, hi):
        return corr_deg2(rec, lo, hi, plist)

    section("C2  THE WEIGHT IDENTITY (degree 2, every field, two windows)")
    for (lo, hi) in ((0, 1000), TOP, (0, 10000)):
        worst = 0.0
        for rec in recs_i:
            w, blind = corr2(rec, lo, hi)
            worst = max(worst, abs(sum(w.values()) - blind))
        ok(worst < 1e-9, "C2: identity off by %.3g" % worst)
    print("  C2 PASSES: the allocated and the class-free weights agree"
          " exactly")

    section("THE IMAGINARY LADDER AND BANDS: RAW BESIDE CORRECTED (P1,"
            " P2, C3)")
    wins = [(0, c) for c in CUTS + EXT_CUTS] + list(BANDS)
    keepmap = {}
    for wnd in wins:
        keepmap[wnd] = keep_i if wnd[0] == 0 else keep_ib
    res_i = {}
    for wnd in wins:
        res_i.update(read_both(recs_i, keepmap[wnd], [wnd], "imag",
                               places2, corr2, G2))
    ok(abs(res_i[(0, 1000)][0][0] - IMAG_CUT1000) < REPRINT_TOL,
       "C3: imaginary cut 1000 reprint off")
    ok(abs(res_i[(0, 10000)][0][0] - IMAG_CUT10K) < REPRINT_TOL,
       "C3: imaginary cut 10000 reprint off")
    ok(abs(res_i[TOP][0][0] - IMAG_TOP[0]) < REPRINT_TOL,
       "C3: imaginary top band reprint off")
    print("  C3: the imaginary parents' figures reprint")
    for c in (2500, 10000):
        mu, se = res_i[(0, c)][1]
        print("  P1 cut %d corrected %.4f +- %.4f  (|corr - 1| %s 0.010)"
              % (c, mu, se, "<" if abs(mu - 1) < 0.010 else ">="))
    for c in (630, 1000, 2500, 10000):
        r, cc = res_i[(0, c)][0], res_i[(0, c)][1]
        print("  P1 cut %d explained fraction %.2f"
              % (c, (r[0] - cc[0]) / (r[0] - 1.0)))
    mu, se = res_i[TOP][1]
    print("  P2 imaginary top band corrected %.4f +- %.4f  z %+.2f"
          % (mu, se, (mu - 1) / se))

    section("P3  SQUARES AGAINST ORDERS (the raw imaginary table, p < 1000)")
    cells, sqcell, nfield = order_cells(recs_i, 0, 1000, places2, G2)
    cm = {}
    for (h, o), vals in cells.items():
        if nfield[h] < CV.MINSTRAT or len(vals) < P3_MINCELL or o == 1:
            continue
        cm[(h, o)] = (sum(vals) / len(vals), len(vals))
    groupings = (("by order", lambda h, o: o),
                 ("by squareness", lambda h, o: sqcell[(h, o)]),
                 ("by squareness x h", lambda h, o: (h, sqcell[(h, o)])))
    keep = dict(cm)
    while True:
        before = len(keep)
        for name, fn in groupings[:2]:
            sizes = defaultdict(int)
            for (h, o) in list(keep):
                sizes[fn(h, o)] += 1
            keep = {k: v for k, v in keep.items() if sizes[fn(*k)] > 1}
        if len(keep) == before:
            break
    print("  %d cells survive the no-singleton rule" % len(keep))
    ssd = {}
    for name, fn in groupings:
        grp = defaultdict(list)
        for (h, o), (m, n) in keep.items():
            grp[fn(h, o)].append((m, n))
        ss = 0.0
        for members in grp.values():
            w = sum(n for _, n in members)
            mu = sum(m * n for m, n in members) / w
            ss += sum(n * (m - mu) ** 2 for m, n in members)
        df = len(keep) - len(grp)
        ssd[name] = ss / df if df > 0 else float('nan')
        print("    %-20s SS %8.4f over %2d groups, df %2d, SS/df %.5f"
              % (name, ss, len(grp), df, ssd[name]))
    print("  the non-square non-generator cells against their generator:")
    for (h, o) in sorted(keep):
        if sqcell[(h, o)] == 'nsq' and o != h and (h, h) in cm:
            (m, n), (mg, ng) = cm[(h, o)], cm[(h, h)]
            sd = ((sum((v - m) ** 2 for v in cells[(h, o)]) / (n - 1)) / n
                  ) ** 0.5
            sdg = ((sum((v - mg) ** 2 for v in cells[(h, h)]) / (ng - 1)) / ng
                   ) ** 0.5
            z = (m - mg) / (sd * sd + sdg * sdg) ** 0.5
            print("    h=%2d order %2d  %.4f +- %.4f  generator %.4f +- %.4f"
                  "  z %+.2f" % (h, o, m, sd, mg, sdg, z))
    print("  the square non-trivial cells, for the eye:")
    for (h, o) in sorted(keep):
        if sqcell[(h, o)] == 'sq':
            (m, n) = cm[(h, o)]
            print("    h=%2d order %2d  %.4f  (n %d)" % (h, o, m, n))
    del recs_i

    section("THE REAL NARROW POPULATION (the sibling's sweep to %d)"
            % DBOUND_REAL)
    recs_r = deg2_records(+1, DBOUND_REAL, plist)
    fields_r = [r[0] for r in recs_r]
    keep_r, keep_rb = CV.frozen_strata(fields_r, CUTS, BANDS)
    keep_r = [h for h in keep_r if CV.is_composite(h)]
    keep_rb = [h for h in keep_rb if CV.is_composite(h)]
    print("  %d admissible fields, cumulative strata %s, band strata %s"
          % (len(recs_r), keep_r, keep_rb))
    res_r = {}
    for wnd in [(0, 1000), (0, 10000)] + list(BANDS):
        kp = keep_r if wnd[0] == 0 else keep_rb
        res_r.update(read_both(recs_r, kp, [wnd], "real", places2, corr2, G2))
    ok(abs(res_r[TOP][0][0] - REAL_TOP[0]) < REPRINT_TOL,
       "C3: real top band reprint off")
    print("  C3: the real sibling's top band reprints")
    mu, se = res_r[TOP][1]
    print("  P2 real top band corrected %.4f +- %.4f  z %+.2f"
          % (mu, se, (mu - 1) / se))
    del recs_r

    wide = "--wide" in sys.argv[1:]
    section("THE DEGREE-3 POPULATION (%s)"
            % ("the top-band sibling's wide population to |d| <= 24000"
               if wide else "the parents' base population to |d| <= 6000"))
    recs_3, nmapped = deg3_records(wide)
    fields_3 = [r['field'] for r in recs_3]
    keep_3, keep_3b = CV.frozen_strata(fields_3, CUTS, BANDS)
    print("  %d of %d fields admissible, cumulative strata %s, band"
          " strata %s" % (len(recs_3), nmapped, keep_3, keep_3b))
    t2 = defaultdict(int)
    for r in recs_3:
        t2[r['t2']] += 1
    print("  the prime 2: %s" % dict(t2))
    print("  places dropped by the map: %d" % sum(r['dropped']
                                                 for r in recs_3))

    section("C4  THE TRIPLES SUM TO ZERO")
    bad = 0
    for r in recs_3:
        G = r['G']
        for (p, tri) in r['ts']:
            s = G.add(G.add(tri[0], tri[1]), tri[2])
            if s != G.triv:
                bad += 1
        for (lo, hi) in ((0, 1000),):
            for q in plist:
                if q * q >= hi:
                    break
                t, data = qtype_deg3(r, q)
                if t == 'partial' and data is not None:
                    tri = (G.mul(data, 2), G.neg(data), G.neg(data))
                    s = G.add(G.add(tri[0], tri[1]), tri[2])
                    if s != G.triv:
                        bad += 1
    ok(bad == 0, "C4: %d triples do not sum to zero" % bad)
    print("  C4 PASSES: every split triple and every correction triple"
          " sums to the trivial class")

    def places3p(rec):
        return rec['field'][2]

    def places3s(rec):
        return [(p, key) for (p, tri) in rec['ts'] for key in tri]

    def G3(rec):
        return rec['G']

    def corr3p(rec, lo, hi):
        return corr_deg3(rec, lo, hi, plist, 'partial')

    def corr3s(rec, lo, hi):
        return corr_deg3(rec, lo, hi, plist, 'split')

    section("THE PARTIAL FIBER: RAW BESIDE CORRECTED (P4, C3)")
    wins3 = [(0, c) for c in CUTS] + list(BANDS)
    res_p = {}
    for wnd in wins3:
        kp = keep_3 if wnd[0] == 0 else keep_3b
        res_p.update(read_both(recs_3, kp, [wnd], "deg3 partial", places3p,
                               corr3p, G3))
    if wide:
        ok(abs(res_p[TOP][0][0] - DEG3_TOP[0]) < REPRINT_TOL,
           "C3: degree-3 wide top band reprint off")
        print("  C3: the degree-3 wide top band reprints")
    else:
        for (c, frozen) in zip(CUTS, DEG3_CUM):
            ok(abs(res_p[(0, c)][0][0] - frozen) < REPRINT_TOL,
               "C3: degree-3 cut %d reprint off" % c)
        print("  C3: the degree-3 cumulative ladder reprints")
    worst = 0.0
    for wnd in wins3:
        r, c = res_p[wnd][0], res_p[wnd][1]
        if r[0] is not None and c[0] is not None:
            worst = max(worst, abs(r[0] - c[0]))
    print("  P4 largest move of a partial-fiber level under correction:"
          " %.4f" % worst)
    for wnd in ((0, 1000), TOP):
        un = sum(corr3p(r, *wnd)[2] for r in recs_3)
        tot = sum(1 for r in recs_3 for (p, k) in places3p(r)
                  if wnd[0] <= p < wnd[1])
        print("  unallocated partial-fiber weight over %s: %.1f against"
              " %d counted primes (%.2f %%)"
              % (wnd, un, tot, 100.0 * un / tot))

    section("THE TOTALLY SPLIT PLACES: RAW BESIDE CORRECTED (P5)")
    strata_s, _ = strata_table(recs_3, TOP[0], TOP[1], places3s, corr3s,
                               G3, False)
    keep_s = [h for h in keep_3 if h in strata_s
              and strata_s[h]['exp'][h] >= MIN_CELL]
    keep_sb = [h for h in keep_3b if h in strata_s
               and strata_s[h]['exp'][h] >= MIN_CELL]
    print("  strata readable on the split places: cumulative %s, band %s"
          % (keep_s, keep_sb))
    res_s = {}
    for wnd in wins3:
        kp = keep_s if wnd[0] == 0 else keep_sb
        res_s.update(read_both(recs_3, kp, [wnd], "deg3 split  ", places3s,
                               corr3s, G3))
    for wnd in ((0, 1000), TOP):
        un = sum(corr3s(r, *wnd)[2] for r in recs_3)
        tot = sum(1 for r in recs_3 for (p, k) in places3s(r)
                  if wnd[0] <= p < wnd[1])
        print("  unallocated split-fiber weight over %s: %.1f against"
              " %d counted places (%.2f %%)"
              % (wnd, un, tot, 100.0 * un / tot))
    (r, c, rn, cn) = res_s[TOP]
    if rn[0] is not None:
        print("  P5 split places top band: nsq raw %.4f +- %.4f (z %+.2f"
              " from 1)  corrected %.4f +- %.4f (z %+.2f)"
              % (rn[0], rn[1], (rn[0] - 1) / rn[1], cn[0], cn[1],
                 (cn[0] - 1) / cn[1]))
    if r[0] is not None:
        print("  P5 split places top band: generator raw %.4f +- %.4f"
              " (z %+.2f from 1)  corrected %.4f +- %.4f (z %+.2f)"
              % (r[0], r[1], (r[0] - 1) / r[1], c[0], c[1],
                 (c[0] - 1) / c[1]))
    print("  the split places' order cells in the top band, pooled over"
          " the band strata, raw then corrected:")
    for corrected in (False, True):
        strata_s, sq_s = strata_table(recs_3, TOP[0], TOP[1], places3s,
                                      corr3s, G3, corrected)
        for h in keep_sb:
            s = strata_s[h]
            print("    %s h=%d  " % ("corr" if corrected else "raw ", h)
                  + "  ".join("ord %d %.3f (obs %.1f exp %.1f)"
                              % (d, s['obs'][d] / s['exp'][d], s['obs'][d],
                                 s['exp'][d])
                              for d in sorted(s['obs']) if s['exp'][d] > 0))

    print("\n%d checks passed, %.1f s wall" % (CHECKS, time.time() - t0))


if __name__ == "__main__":
    main()
