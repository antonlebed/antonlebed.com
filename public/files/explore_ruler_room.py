"""IS THE CERTIFICATE'S OWN ROOM WHAT EMPTIES THE CLEAN SET?

THE QUESTION
------------
Over one menu family the clean set collapses with the nominal coverage:
183, 105, 18 and 0 weight vectors of 741 obey the abandonment law across
five menus at coverage 3/4, 7/10, 3/5 and 1/2. Nothing explains the
collapse. The box, the spread bound and the ratio bound all fail on
every non-empty clean set, so the region has no coordinate shape, and
the level alone is refuted: the operative level is non-decreasing as
coverage falls at every cell and is IDENTICAL at 3/5 and 1/2 at 55.9% of
them, where the clean set reads 18 and 0.

The corpus carries exactly one sufficient condition for the threshold
rule being optimal, and it has never been read at more than one target.
This file reads it at four, and it reads it as a PREDICTOR of the clean
set rather than as a bound.

THE DERIVATION, worked on paper before any engine code
------------------------------------------------------
Every symbol is re-derived from the engines that define it -- the
certificate and its surplus from explore_ruler_optimum.py, the level
from explore_ruler_barecell.py -- and never inherited from a summary.

  THE OBJECTS. A cell carries atoms r with masses w_r summing to 1 and
  posterior rows p(y|r) summing to 1. The target is T = 1 - alpha. The
  operative level t* is the largest posterior value whose superlevel
  rule still covers T. Write A for the pairs with p > t* and S for the
  pairs with p = t*; a pair (r, y) costs w_r and covers w_r p(y|r), so
  every tied pair covers exactly w_r t*. The certificate takes all of A
  and then the cheapest subset of S that closes the gap:

      deficit = T - above_cov,     q = deficit / t*,
      fill    = min { sum of tied costs over U subset of S : sum >= q },
      D       = above_cov + t* fill - T = t* (fill - q),
      ROOM    = D / t* = fill - q.

  The surplus criterion is 0 <= cert - OPT <= D/t*, and cert - OPT lies
  in the lattice the atom weights generate, so

      ROOM < g   =>   cert = OPT,   g = the lattice's smallest positive
                                        element.

  cert = OPT says the threshold rule IS an optimum, which is exactly
  what the FORCED criterion asks of a cell: an atom fails only when
  every optimum breaks the rule, and none can when the rule is one. So
  a vector firing the criterion at every cell is forced-CLEAN there.
  The criterion set is a SUBSET of the clean set by construction, and
  that containment is the derivation this run is built on.

  FIRST -- THE ROOM IS A SUBSET-SUM OVERSHOOT AND t* DOES NOT SCALE IT.
  ROOM = sigma(q) - q, sigma(q) being the least achievable tied subset
  sum at or above q. The level enters ONLY through q. It does not
  multiply the overshoot, so the room's t*-dependence is a POSITION in
  the tied sum set and never a magnitude.

  SECOND -- THE RANGE OF q. Maximality of t* gives above_cov < T, so
  q > 0. Feasibility gives above_cov + t* W >= T for W the total tied
  cost, so q <= W. Hence q lies in (0, W].

  THIRD -- THE t*-DEPENDENCE IS A SAWTOOTH AND NOT A MONOTONE. Hold the
  cell and lower T. While the level is unchanged, above_cov is fixed and
  q falls linearly with T. When T drops under above_cov the level jumps
  UP to the next posterior value, above_cov falls to the smaller above
  set's coverage and q resets upward. So across four targets q sweeps
  down and resets, and the room, a function of q's position, resets with
  it. THE ROOM CANNOT RUN THE WRONG WAY IN t* BECAUSE IT DOES NOT RUN
  MONOTONICALLY AT ALL -- which is the opposite of what the lattice
  variable did, where the N-dependence was monotone and pointed against
  the observation. The bound survives its second reading.

  FOURTH -- INSIDE ONE REGIME THE TWO ENDS DIFFER, AND THAT IS A
  TENDENCY AND NOT A DERIVATION. At q just above 0 the least tied sum
  at or above it is the smallest tied cost, so ROOM is nearly that
  cost; at q = W the fill is everything and ROOM is 0. The two ENDS of
  a regime therefore differ in the direction the observation runs. That
  is all this says, and two things stop it short of a derivation. ROOM
  is sigma(q) - q throughout, so it sawtooths WITHIN a regime as well,
  climbing as q falls between two achievable sums and dropping to 0 the
  moment q crosses one. And the smallest tied cost is not the room's
  maximum: tied costs {1, 10} give achievable sums {0, 1, 10, 11} and a
  room approaching 9 just above q = 1, nine times the smallest cost. So
  this is an endpoint comparison offered as a guess, P6 is what tests
  it, and THIRD is the part that is derived.

  FIFTH -- THE LATTICE THRESHOLD WAS READ AT ITS WORST CASE, AND THE
  CORRECTION IS A SHAPE. The paper route recorded the condition as
  ROOM < 1/N for weights on a 1/N lattice. But g is the smallest
  POSITIVE element of the lattice the weights generate, and for masses
  a_r/N that lattice is (d/N)Z with d = gcd(a_1, ..., a_M). The true
  threshold is d/N and it is larger by exactly the FACTOR d. The
  criterion
  therefore fires more easily at weight vectors of high gcd -- an
  ARITHMETIC function of the vector, permutation-invariant as the clean
  sets are, and invisible to every description the clean set has been
  tested against, all three of which are coordinate-geometric and
  continuous. A set stratified by gcd is a set on which each of them
  must fail. That is a candidate account of the shapelessness itself.

  On this grid N = 40 and M = 3, so d divides 40 with 40/d >= 3 and
  d lies in {1, 2, 4, 5, 8, 10}. The strata have sizes 552, 132, 30,
  18, 6 and 3 by Moebius over the compositions, since the vectors with
  d dividing e number C(40/e - 1, 2). They sum to 741.

  SIXTH -- THE ALGEBRA OF THE STATISTIC. Nothing here can round or blow
  up: with masses a_r/WD and posteriors b/PD, the level is t = tau/PD,
  the feasibility test is sum_r a_r B_r(tau) >= WD*PD*T for
  B_r(tau) the sum of that atom's entries at or above tau, and writing
  U = sum_r a_r (B_r - c_r tau) for c_r the count of entries EQUAL to
  tau, the whole criterion clears its denominators:

      Nq = WD*PD*T - U,     fill = S/WD over integer combinations
      S = sum_r i_r a_r with 0 <= i_r <= c_r,
      ROOM = (S*tau - Nq) / (WD*tau),   FIRES <=> S*tau - Nq < d*tau.

  Every quantity is an integer; WD*PD*T is an integer at all four
  targets on both grids (1600T and 120T). The scorer runs in integers
  and the Fractions are gone, which is also why it is cheap.

WHOSE VOCABULARY
----------------
The surplus rig's own: ATOM, LEVEL, TIED BLOCK, SURPLUS D, ROOM D/t*,
COST LATTICE and its gap g keep explore_ruler_surplus.py's senses.
GCD STRATUM is new here and means the set of weight vectors whose
integer numerators share a given greatest common divisor. FIRES means
the criterion's inequality holds at a cell; the CRITERION SET at a
target is the set of weight vectors that fire at every cell of the arm.

THE ARMS
--------
The four controlled targets on menus A-E, twentieth posteriors, 741
fortieth weight vectors by 125 row choices = 625 cells apiece, plus the
fortieth menus F-J at 7/10 as a second lattice:

  coverage 3/4, 7/10, 3/5, 1/2 on A-E, recorded forced clean sets 183,
  105, 18 and 0; coverage 7/10 on F-J, recorded forced clean set 54.

THE PREDICTIONS, frozen before the engine
-----------------------------------------
P1  CONTAINMENT. The criterion set is at most the recorded forced clean
    set at every arm: at most 183, 105, 18, 0 and 54. This is a
    DERIVATION and not a guess -- firing implies clean -- so a violation
    refutes the room, the level or the record, and nothing else in this
    file may be read until it holds.

P2  The criterion set is non-increasing in size as the coverage falls
    3/4, 7/10, 3/5, 1/2, and is EMPTY at 1/2.

P3  ENRICHMENT. The share of the criterion set carrying gcd >= 2 exceeds
    the grid's own 189/741 = 25.5%, at every non-empty arm.

P4  The criterion set at coverage 3/5 is EXACTLY the gcd = 5 stratum,
    all 18 of it. A guess off a coincidence of counts and the cheapest
    thing here to kill; a miss costs the guess and nothing else.

P5  The room explains a non-trivial share of the clean set: the
    criterion set at coverage 3/4 has at least 20 members, about a
    ninth of the 183. Fewer than 20 says the certificate's error is not
    the mechanism at this arity, and the thread closes on it.

P6  The grid-wide MEAN room grows as the coverage falls 3/4 to 1/2 --
    FOURTH's within-regime direction beating THIRD's resets. This is
    the direct answer to whether the room moves with the collapse.

P7  Every criterion set is closed under permutation of the weight
    vector. A violation is a BUG in the scoring, never a finding.

THE CONTROLS
------------
C1  THE POSITIVE CONTROL, and it runs before any criterion set is read.
    At equal mass the tied costs are all w0 and the deficit is under one
    tied pair's coverage, so D < w0 t* and ROOM < w0 = g: the criterion
    fires at EVERY equal-mass cell. Derived; asserted here at all five
    arms, both because the derivation says so and because the equal-mass
    vector is not on the fortieth lattice and so cannot be reached by
    the grid.

C2  PARITY AGAINST THE OPTIMUM. At every cell where the criterion
    fires, the certificate's cost must equal the exhaustive optimum.
    Checked at every cell of every criterion-set member -- the whole
    point of the derivation, measured rather than assumed. A single
    failure is a bug in the room or the level.

C3  REPRODUCTION OF THE LEVEL. This file recomputes the operative level
    by an integer route that shares no code with the record's. The
    grid-wide above-level, below-level and at-level atom populations it
    prints must reproduce the record exactly -- 1307295/5898/76182 at
    3/4, 1204311/17796/167268 at 7/10, 951717/68124/369534 at 3/5 and
    665862/157623/565890 at 1/2. A miss means the levels are not the
    record's and no criterion number may be read.

C4  NON-VACUITY. The criterion set at 3/4 is asserted to be neither the
    whole grid nor empty, so that P3's enrichment reading has something
    to read.

C5  THE DENOMINATORS. Every criterion set is printed against the
    recorded clean count it sits inside, and the per-arm cell counts are
    printed, so a small set is never reported as a shape.

C7  ROOM PARITY, added at audit and not frozen. C1 and C2 both validate
    cells where the criterion FIRES, and neither can see a room computed
    too LARGE -- which is exactly the failure that would manufacture
    this file's headline. So the integer room is checked against an
    independent Fraction route built from the cell object alone, on both
    halves of the decision.

RESOURCES
---------
Five arms of 741 weight vectors by 625 cells, integer-only in the hot
loop: a few minutes and a few tens of megabytes, under memwatch against
the 512 MB ceiling. C2's optimum parity runs only over criterion-set
members, which the containment prediction bounds by a few hundred
vectors. The pipeline is rehearsed first on a permutation-closed sample
(--rehearse), which exercises every arm, every control and every set
reading in seconds, so a kill costs seconds rather than the run.

WHAT RAN
--------
One run, rehearsed first. Five arms, 741 weight vectors by 625 cells
apiece, 4.0 s, peak working set 16.7 MB under memwatch against a 512 MB
ceiling. The integer scorer is what makes a question that looked like a
sweep cost four seconds -- and RESOURCES above, frozen before the run,
said "a few minutes". It was wrong by a factor of about sixty, in the
safe direction, because it was estimated from the predecessor sweep's
per-cell cost without accounting for the fact that clearing the
denominators removes the optima from the loop entirely. Worth recording
because the estimate is what decides whether a question gets asked at
all: a run priced in minutes has to be argued for against the
wall-clock rule, one priced in seconds does not, and the margin here
paid for the second stage below.

The rehearsal fired P7 on its first execution and the fault was the
REHEARSAL SAMPLE, not the scoring: a cell pairs atom r with menu row
rows[r], so permuting the weights alone is a symmetry only when the ROW
set is permutation-closed too, and a prefix of ROWS is not. The
rehearsal now takes the closed row set {0,1}^3. That is the second time
in this thread a permutation assert has caught its own sample rather
than the engine, and both times the sample was drawn by a condition
that is not permutation-invariant.

C4 WAS FROZEN AS AN ASSERT AND IT SHOULD NOT HAVE BEEN. It demanded a
non-vacuous criterion set at 3/4 so that P3 would have something to
read -- but an empty criterion set is the run's actual answer, not a
bug, and an assert there turns a legitimate negative into a crash. It
is a printed observable now. A kill criterion names what the rig
PRINTS, never what it would mean.

C7 WAS ADDED AT AUDIT AND IT CLOSES A REAL HOLE. Every control frozen
before the run validates cells where the criterion FIRES, and this
file's headline is that nothing fires -- a claim resting entirely on
the cells where it does NOT. A room computed too large would
manufacture that headline and no frozen control could see it. The
integer room now runs against an independent Fraction route built from
the cell object alone: 1,890 sampled cells per arm, 0 mismatches on
both the room and the fire decision, with 1,424 to 1,626 of them
NON-firing at each arm. The wall goes 4.0 s to 4.8 s.

EVERY CONTROL PASSES. C1: the criterion fires at all 625 equal-mass
cells at all five arms, which is the derivation holding exactly and the
proof that the scorer CAN fire. C2: no criterion-set member exists to
check on the full grid, so it is reported UNTESTED and not as a pass;
the rehearsal did check 120 firing cells against the exhaustive optimum
with zero mismatches, which is where the certificate-equals-optimum
claim is actually measured. C3 REPRODUCTION is the control that
matters most and it is EXACT at all four A-E targets -- 1307295/5898/
76182, 1204311/17796/167268, 951717/68124/369534 and 665862/157623/
565890 -- by an integer code path sharing nothing with the record's
Fraction one, so the levels here are the record's levels. C5's
denominators are printed per arm and they are the reason an empty set
is reported as a distance rather than as a nothing. P7 holds at every
arm.

WHAT IT FOUND
-------------
THE CERTIFICATE'S ERROR IS NOT THE MECHANISM, AND THE MARGIN IS NOT
CLOSE. The criterion set is EMPTY at all five arms: not one of the 741
weight vectors fires the sufficient condition at all 625 cells, at any
target, on either posterior lattice. So the only derivation this thread
carried explains ZERO of the 183 clean vectors at 3/4, zero of the 105
at 7/10, zero of the 18 at 3/5 and zero of the 54 on the fortieth
menus. P5 asked for 20 of the 183 and got none. P1's containment holds
trivially and buys nothing, P4's coincidence dies with the set that
would have carried it.

THE DISTANCE IS THE POINT AND IT IS PRINTED. Per CELL the criterion
fires 20.7%, 22.6%, 17.1% and 16.9% of the time as coverage falls 3/4
to 1/2, and 17.6% on the fortieth menus. The closest ORBIT at every
single arm is (1/4, 1/4, 1/2)'s -- all three of its members tie, the
miss count being permutation-invariant -- and it still misses 53, 56,
70, 41 and 52 cells of 625. A condition that misses forty cells at its
best orbit is not a condition that was one refinement away from the
clean set.

AND THE CELL RATE DOES NOT TRACK THE COLLAPSE EITHER. It rises 20.7 to
22.6 and then falls to 17.1 and 16.9, while the clean set falls
monotonically 183, 105, 18, 0. So the room is refuted twice over: too
weak to produce a clean vector, and not even moving in the right
direction when read as a tendency.

P6 IS REFUTED AND THE DERIVATION PREDICTED IT. The grid-wide mean room
reads 0.166226, 0.156966, 0.177517 and 0.169890 as coverage falls 3/4,
7/10, 3/5, 1/2 -- down, up, down, with no monotone direction at all.
That is THIRD measured: the room is a SAWTOOTH in the target because
t* enters only through q's position in the tied subset-sum set, and
FOURTH's within-regime growth does not survive the resets. The room
does not run the wrong way in t*, which is what the lattice variable
did; it does not run at all. Both variables of the only sufficient
condition are now read, and neither governs the clean set.

WHAT SURVIVES, AND IT IS FIFTH'S CORRECTION. The paper route recorded
the threshold as 1/N; it is d/N with d the gcd of the weight
numerators, larger by exactly d. That correction is REAL and it is
large. The per-cell firing rate stratifies monotonically by gcd at
every arm, and the spread is a factor of six:

  gcd            1      2      4      5      8     10
  vectors      552    132     30     18      6      3
  fires 3/4  15.3%  27.2%  48.9%  57.9%  78.6%  91.5%
  fires 7/10 17.4%  29.1%  50.7%  59.5%  78.3%  91.0%
  fires 3/5  11.8%  23.2%  44.4%  55.1%  76.0%  88.8%
  fires 1/2  11.7%  22.8%  44.4%  54.8%  80.1%  93.4%
  fires F-J  12.2%  23.7%  46.8%  57.4%  80.4%  91.7%

So what governs the CRITERION is arithmetic -- a divisibility property
of the weight numerators -- and not geometry. That matters because the
three descriptions the clean set has been tested against, the
coordinate box and the spread and ratio bounds, are all continuous
functions of the vector, and every one of them must fail on a set
stratified this way. Whether the CLEAN set carries the same
stratification is not answered here: the criterion set is empty, so it
carries no information about the clean set beyond containment. That is
stage two.

STAGE TWO, frozen after stage one printed and before its own engine
-------------------------------------------------------------------
THE QUESTION. Stage one leaves exactly one live thing: the criterion is
governed by an ARITHMETIC property of the weight vector, and the three
descriptions the clean set was tested against are all continuous. Is
the CLEAN set stratified by gcd as the criterion set is? The criterion
being empty says nothing either way -- containment over an empty set is
free -- so this has to be measured on the clean set itself.

THE ENGINE. The forced clean set, recomputed from every optimum at
every cell, with one change that makes it cheap: a vector EARLY-EXITS
the moment a cell charges it a forced failure, since cleanliness is a
conjunction. The recorded run scored every cell because it wanted the
counts; this one wants the boolean.

  P8   ENRICHMENT. The share of the clean set carrying gcd >= 2 exceeds
       the grid's 189/741 = 25.5%, at every non-empty arm. This is the
       whole stage: a yes makes gcd the first description that survives
       contact with the clean set, a no kills the arithmetic angle with
       the geometric ones and closes the thread.

  P9   THE SHARP FORM. The clean set at 3/4 is exactly the union of the
       gcd strata 2, 4, 5 and 10 (132 + 30 + 18 + 3 = 183) and the
       clean set at 3/5 is exactly the gcd = 5 stratum (18). Both are
       guesses off a coincidence of counts, and both are cheap to kill.
       At 7/10 no such reading is even possible: 105 is not a sum of
       the strata sizes {552, 132, 30, 18, 6, 3}, which is derived on
       paper and is why a union CANNOT be the general answer.

  C6   REPRODUCTION, and it gates everything above. The clean counts
       must come back 183, 105, 18, 0 and 54 exactly. A miss means the
       early exit changed the set and no profile may be read.

WHAT STAGE TWO RAN
------------------
One run, 129 s, peak working set 14.5 MB under memwatch against a
512 MB ceiling. C6 is EXACT at all five arms -- 183, 105, 18, 0 and 54
-- so the early exit is the record's set and not a near neighbour of
it, and the reproduction covers three targets and both posterior
lattices.

WHAT STAGE TWO FOUND
--------------------
P9 DIES AT BOTH FORMS. The clean set is not a union of gcd strata at
either target: at 3/4 it holds 135 of the 552 gcd = 1 vectors, and at
3/5 it holds 12 of them. The count coincidences were coincidences.

P8 HOLDS AND THE AGGREGATE IS THE WRONG STATISTIC TO READ IT WITH. The
share carrying gcd >= 2 does exceed the grid's 25.5% at every non-empty
arm -- 26.2%, 28.6%, 33.3% and 44.4% -- but at 3/4 that is a margin of
0.72 of a percentage point over the grid, which is nothing. What
the per-stratum RATE shows instead is not a gradient at all:

  gcd            1      2      4      5      8     10
  vectors      552    132     30     18      6      3
  clean 3/4  24.5%  20.5%  30.0%  16.7%   100%   100%
  clean 7/10 13.6%  11.4%  10.0%  16.7%   100%   100%
  clean 3/5   2.2%   2.3%   0.0%   0.0%   0.0%   100%
  clean 1/2   0.0%   0.0%   0.0%   0.0%   0.0%   0.0%
  clean F-J   5.4%   9.1%  10.0%  16.7%  50.0%   100%

THE TWO TOP STRATA BEHAVE UNLIKE EVERYTHING BELOW THEM, AND THE MIDDLE
IS FLAT. Every gcd 8
and gcd 10 vector is clean at 3/4 and at 7/10, and every gcd 10 vector
is clean at 3/5 where the strata at 4, 5 and 8 read ZERO outright and
the two below them read 2.2% and 2.3%. Meanwhile strata 2, 4 and 5
track the gcd = 1 bulk, above it at one target and below it at another.
So gcd does not GRADE cleanliness; it separates a top of nine vectors
-- and only partly, the gcd 8 stratum reading 50% on the fortieth menus
where gcd 10 reads 100% -- and says nothing about the 552-vector
bulk, which is 74% of the grid and 74% of the clean set at 3/4.

AND IT DOES NOT EXPLAIN THE COLLAPSE. Every stratum collapses, the
coarse ones simply last longer: the gcd = 1 rate runs 24.5, 13.6, 2.2,
0 while the gcd = 10 rate runs 100, 100, 100, 0. What empties the set
acts on all six strata at once, and gcd orders the SURVIVAL rather than
causing the death. The 1/2 column is the sharpest form of it -- even
the vector that is clean everywhere else fails there.

WHAT THIS LEAVES. The first EXACT sub-description of the clean set the
thread has found, and it is a subset rather than a superset: every
weight vector of gcd 8 or 10 is clean at 3/4 and at 7/10, and the gcd
10 vectors are clean at 3/5 as well. It is NOT "gcd 8 or more is clean
at three targets" -- the gcd 8 stratum reads zero at 3/5, so the two
top strata part company exactly where everything else has already
died. It is an observation and it has no proof, and stage
one is why it cannot borrow one: the corpus's only sufficient condition
fails on the (1/4, 1/4, 1/2) orbit at 41 to 70 cells of 625 at every
arm. So the sharp open question is no longer "what shape is
the clean set": it is why the COARSE vectors are clean when the one
condition that could certify them demonstrably is not what does it.
"""

import os
import sys
import time
from fractions import Fraction
from functools import reduce
from math import gcd, lcm

os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from explore_ruler_barecell import (  # noqa: E402
    exhaustive_optimum,
    operative_level,
)
from explore_ruler_family import KEYS, score  # noqa: E402
from explore_ruler_abandon import (  # noqa: E402
    ALPHA,
    all_optima,
    EQUAL,
    ROWS,
    check_truth,
    make_cell,
)
from explore_ruler_box import ALPHA2, DEN, GRID, NEW, OLD, fmt  # noqa: E402

F = Fraction

PD = 40                   # the posterior denominator both menu sets share
LCM = reduce(lcm, range(1, PD + 1))   # clears every room's denominator

# The recorded forced clean counts these criterion sets must sit inside.
RECORD = {"3/4": 183, "7/10": 105, "3/5": 18, "1/2": 0, "7/10 F-J": 54}

# The record's grid-wide atom populations, for C3.
POPS = {"3/4": (1307295, 5898, 76182),
        "7/10": (1204311, 17796, 167268),
        "3/5": (951717, 68124, 369534),
        "1/2": (665862, 157623, 565890)}

ARMS = (("3/4", OLD, F(1, 4)),
        ("7/10", OLD, ALPHA),
        ("3/5", OLD, ALPHA2),
        ("1/2", OLD, F(1, 2)),
        ("7/10 F-J", NEW, ALPHA))


# ------------------------------------------------- the menus, in integers

def integerize_menu(menu):
    """A menu's rows as integer numerators over PD, checked exact."""
    out = []
    for row in menu:
        vals = []
        for p in row:
            v = p * PD
            assert v.denominator == 1, ("posterior is not a %dth" % PD, p)
            vals.append(int(v))
        assert sum(vals) == PD, ("row does not sum to 1", row)
        out.append(vals)
    return out


def cell_tables(menu_int, rows):
    """Everything one row choice needs, level by level, as integers.

    Returns a list over candidate levels tau (descending) of
    (tau, B, C, above_pop, below_pop, at_level) where B[r] sums that
    atom's entries at or above tau and C[r] counts those equal to it,
    and the three populations count ATOMS by where their best entry
    sits -- the record's own convention.
    """
    post = [menu_int[i] for i in rows]
    tops = [max(row) for row in post]
    taus = sorted({v for row in post for v in row}, reverse=True)
    out = []
    for tau in taus:
        B = [sum(v for v in row if v >= tau) for row in post]
        C = [sum(1 for v in row if v == tau) for row in post]
        ab = sum(1 for t in tops if t > tau)
        be = sum(1 for t in tops if t < tau)
        out.append((tau, B, C, ab, be, len(tops) - ab - be))
    return out


def min_fill(a, C, Nq, tau):
    """The least tied subset sum S with S*tau >= Nq, or None.

    S ranges over sum_r i_r a_r with i_r at most the tied multiplicity
    C[r]. Three atoms, so at most 64 combinations and no recursion.
    """
    best = None
    for i in range(C[0] + 1):
        s0 = i * a[0]
        for j in range(C[1] + 1):
            s1 = s0 + j * a[1]
            for m in range(C[2] + 1):
                s = s1 + m * a[2]
                if s * tau >= Nq and (best is None or s < best):
                    best = s
    return best


def score_cell(a, d, WD, table, scaledT):
    """One cell: does the criterion fire, and how much room is there?

    `scaledT` is WD*PD*T. Returns (fires, room_num, room_den, tau,
    above_pop, below_pop, at_level) with the room as an exact pair of
    integers. Raises where no level is feasible, which is a bug.
    """
    for tau, B, C, ab, be, at in table:
        if sum(a[r] * B[r] for r in range(3)) >= scaledT:
            U = sum(a[r] * (B[r] - C[r] * tau) for r in range(3))
            Nq = scaledT - U
            assert Nq > 0, ("the level is not maximal", a, tau)
            S = min_fill(a, C, Nq, tau)
            assert S is not None, ("the tied block cannot close the"
                                   " deficit", a, tau)
            num = S * tau - Nq
            return num < d * tau, num, WD * tau, tau, ab, be, at
    raise AssertionError(("no feasible level", a, scaledT))


# --------------------------------------------------------------- the arms

def numerators(w, den):
    out = []
    for x in w:
        v = x * den
        assert v.denominator == 1, ("weight is not a %dth" % den, x)
        out.append(int(v))
    assert sum(out) == den, ("weights do not sum to 1", w)
    return tuple(out)


def run_arm(name, menus, alpha, grid, tables):
    """One target: the criterion set, the populations, the mean room."""
    T = 1 - alpha
    print()
    print("=" * 70)
    print("ARM %s -- nominal coverage %s, %d weight vectors, %d cells each"
          % (name, T, len(grid), len(tables)))

    # C1 first, before any grid number is read.
    eq = numerators(EQUAL, 3)
    sT_eq = 3 * PD * T
    assert sT_eq.denominator == 1, ("equal-mass target does not clear",
                                    T)
    sT_eq = int(sT_eq)
    eq_fire = eq_cells = 0
    for table in tables:
        fires, _n, _dn, _t, _a, _b, _l = score_cell(eq, gcd(*eq), 3,
                                                    table, sT_eq)
        eq_cells += 1
        eq_fire += fires
    print("   C1 EQUAL MASS: criterion fires at %d of %d cells"
          % (eq_fire, eq_cells))
    assert eq_fire == eq_cells, (
        "C1 BROKEN: the criterion misses an equal-mass cell, which the"
        " derivation forbids -- a bug and not a finding", name,
        eq_cells - eq_fire)

    scaledT = DEN * PD * T
    assert scaledT.denominator == 1, ("grid target does not clear", T)
    scaledT = int(scaledT)

    # The mean room is summed EXACTLY over a fixed common denominator
    # rather than as a running Fraction: every room is num/(DEN*tau)
    # with tau at most PD, so DEN*lcm(1..PD) clears them all at once and
    # the accumulator stays a single integer. A running Fraction over
    # 463,125 terms grows its denominator instead, which is the one way
    # this statistic could have gone wrong.
    common = DEN * LCM
    members, above, below, at_lv = [], 0, 0, 0
    room_acc, room_cnt = 0, 0
    fired, by_gcd, closest = 0, {}, None
    t0 = time.time()
    for w in grid:
        a = numerators(w, DEN)
        d = gcd(*a)
        clean, misses = True, 0
        for table in tables:
            fires, num, dn, _t, ab, be, lv = score_cell(a, d, DEN, table,
                                                        scaledT)
            above += ab
            below += be
            at_lv += lv
            assert common % dn == 0, ("the common denominator does not"
                                      " clear a room", dn)
            room_acc += num * (common // dn)
            room_cnt += 1
            if fires:
                fired += 1
            else:
                clean = False
                misses += 1
        st = by_gcd.setdefault(d, [0, 0])
        st[0] += len(tables) - misses
        st[1] += len(tables)
        if closest is None or misses < closest[0]:
            closest = (misses, w)
        if clean:
            members.append(w)
    dt = time.time() - t0

    mean_room = F(room_acc, common * room_cnt)
    print("   populations over %d cells: ABOVE %d  BELOW %d  AT LEVEL %d"
          % (room_cnt, above, below, at_lv))
    if name in POPS:
        got, want = (above, below, at_lv), POPS[name]
        print("   C3 REPRODUCTION of the record's populations: %s"
              % ("exact" if got == want else "MISS want %s" % (want,)))
        assert got == want, ("C3: the levels are not the record's", name,
                             got, want)
    print("   MEAN ROOM over the grid: %s = %.6f   (%.0f s)"
          % (mean_room, float(mean_room), dt))
    print("   C5 THE DENOMINATOR: the criterion fires at %d of %d cells"
          " = %.2f%%; the closest orbit %s misses %d of %d"
          % (fired, room_cnt, 100.0 * fired / room_cnt,
             fmt(closest[1]), closest[0], len(tables)))
    print("   firing rate by gcd stratum: %s"
          % {d: "%.1f%%" % (100.0 * v[0] / v[1])
             for d, v in sorted(by_gcd.items())})
    print("   CRITERION SET: %d of %d vectors; recorded forced clean %s"
          % (len(members), len(grid), RECORD.get(name, "n/a")))
    return members, mean_room


# ------------------------------------------------------- reading a set

def gcd_profile(members):
    prof = {}
    for w in members:
        d = gcd(*numerators(w, DEN))
        prof[d] = prof.get(d, 0) + 1
    return prof


def perm_closed(members):
    ms = set(members)
    for w in ms:
        for p in ((0, 2, 1), (1, 0, 2), (1, 2, 0), (2, 0, 1), (2, 1, 0)):
            if tuple(w[i] for i in p) not in ms:
                return False, (fmt(w), p)
    return True, None


def report_set(name, members, grid):
    print("      gcd profile of the set: %s  (grid: %s)"
          % (dict(sorted(gcd_profile(members).items())),
             dict(sorted(gcd_profile(grid).items()))))
    ok, bad = perm_closed(members)
    print("      P7 permutation closure: %s"
          % ("holds" if ok else "BROKEN at %s / %s -- a bug" % bad))
    assert ok, ("P7: criterion set is not permutation closed", name, bad)
    if not members:
        return
    hi = sum(1 for w in members if gcd(*numerators(w, DEN)) >= 2)
    print("      P3 share with gcd >= 2: %d/%d = %.1f%%  (grid %.1f%%)"
          % (hi, len(members), 100.0 * hi / len(members),
             100.0 * sum(1 for w in grid
                         if gcd(*numerators(w, DEN)) >= 2) / len(grid)))


def parity_check(name, members, menus, alpha, rows_list):
    """C2: at every cell of every member, certificate cost = optimum."""
    if not members:
        print("      C2 PARITY: no members -- UNTESTED, not a pass.")
        return
    T = 1 - alpha
    scaledT = int(DEN * PD * T)
    ints = {tag: integerize_menu(menu) for menu, tag in menus}
    checked = bad = 0
    for w in members:
        a = numerators(w, DEN)
        d = gcd(*a)
        for menu, tag in menus:
            mi = ints[tag]
            for rows in rows_list:
                table = cell_tables(mi, rows)
                fires, _n, _dn, tau, _ab, _be, _lv = score_cell(
                    a, d, DEN, table, scaledT)
                if not fires:
                    continue
                cell = make_cell(menu, "%s-%s" % (tag, rows), rows, w)
                assert check_truth(cell), ("C2: cell is not a model", tag)
                # the certificate's cost, rebuilt from the same level
                post = [mi[i] for i in rows]
                cert = F(0)
                B = [sum(v for v in row if v >= tau) for row in post]
                C = [sum(1 for v in row if v == tau) for row in post]
                U = sum(a[r] * (B[r] - C[r] * tau) for r in range(3))
                Nq = scaledT - U
                S = min_fill(a, C, Nq, tau)
                above_cost = sum(a[r] * sum(1 for v in post[r] if v > tau)
                                 for r in range(3))
                cert = F(above_cost + S, DEN)
                opt = exhaustive_optimum(cell, alpha)
                checked += 1
                if cert != opt:
                    bad += 1
                    if bad == 1:
                        print("      C2 FIRST MISMATCH: %s %s-%s cert %s"
                              " optimum %s" % (fmt(w), tag, rows, cert,
                                               opt))
    print("      C2 PARITY: %d firing cells checked, %d mismatches"
          % (checked, bad))
    assert bad == 0, ("C2 BROKEN: the criterion fires where the"
                      " certificate is not optimal", name, bad)


def room_parity(menus, alpha, stride_w=37, stride_r=7):
    """C7: the integer room against an independent Fraction route.

    ADDED AT AUDIT, not a frozen control -- see the run record. Every
    other control here validates cells where the criterion FIRES: C1
    asserts firing at equal mass, C2 checks the certificate against the
    optimum at firing cells. None of them can see a room computed too
    LARGE, which would produce false non-fires -- and the headline of
    this file is that nothing fires, a claim resting entirely on the
    non-firing cells.

    So this recomputes the room from the cell OBJECT alone, in
    Fractions, through operative_level and a brute subset sum over the
    tied costs, and compares both the room and the fire decision. It
    samples on a stride because the point is the code path, not
    coverage.
    """
    T = 1 - alpha
    scaledT = int(DEN * PD * T)
    ints = {tag: integerize_menu(menu) for menu, tag in menus}
    bad = seen = fired = 0
    for w in GRID[::stride_w]:
        a = numerators(w, DEN)
        d = gcd(*a)
        for menu, tag in menus:
            for rows in ROWS[::stride_r]:
                cell = make_cell(menu, "%s-%s" % (tag, rows), rows, w)
                assert check_truth(cell), ("C7: not a model", tag)
                lvl, _m, _c, _s = operative_level(cell, alpha)
                above = sum(cell.atom_prob(r) * p
                            for r in range(cell.M)
                            for p in cell.posterior(r) if p > lvl)
                tied = [cell.atom_prob(r) for r in range(cell.M)
                        for p in cell.posterior(r) if p == lvl]
                q = (T - above) / lvl
                best = None
                for mask in range(1 << len(tied)):
                    tot = sum(tied[i] for i in range(len(tied))
                              if mask >> i & 1)
                    if tot >= q and (best is None or tot < best):
                        best = tot
                assert best is not None, ("C7: no fill", tag, rows)
                want = best - q
                fires, num, den, _t, _a, _b, _l = score_cell(
                    a, d, DEN, cell_tables(ints[tag], rows), scaledT)
                seen += 1
                fired += fires
                if F(num, den) != want or (want < F(d, DEN)) != fires:
                    bad += 1
    print("   C7 ROOM PARITY against a Fraction route: %d cells"
          " (%d firing, %d NOT), %d mismatches"
          % (seen, fired, seen - fired, bad))
    assert bad == 0, ("C7 BROKEN: the integer room disagrees with the"
                      " Fraction route", bad)


def main():
    rehearse = "--rehearse" in sys.argv
    if rehearse:
        # A permutation-CLOSED sample, because P7 is asserted and an
        # unclosed sample would fire it as an artifact of the sample.
        reps = ((12, 12, 16), (13, 13, 14), (10, 10, 20), (2, 3, 35),
                (8, 8, 24), (9, 10, 21))
        grid = sorted({tuple(F(x, DEN) for x in p)
                       for r in reps
                       for p in ((r[0], r[1], r[2]), (r[0], r[2], r[1]),
                                 (r[1], r[0], r[2]), (r[1], r[2], r[0]),
                                 (r[2], r[0], r[1]), (r[2], r[1], r[0]))})
        # The row choices must be permutation-closed too: a cell pairs
        # atom r with menu row rows[r], so permuting the weights alone
        # is a symmetry only when the row set is closed. A prefix of
        # ROWS is not, and asserting P7 on one tests the sample.
        rows_list = [(a, b, c) for a in range(2) for b in range(2)
                     for c in range(2)]
        print("REHEARSAL on %d weight vectors (permutation closed) and %d"
              " row choices -- every arm, every control, every set"
              " reading; the record's counts are NOT reproduced and C3"
              " is skipped." % (len(grid), len(rows_list)))
    else:
        grid = GRID
        rows_list = ROWS

    print("IS THE CERTIFICATE'S ROOM WHAT EMPTIES THE CLEAN SET?")
    print("weight lattice %dths: %d ordered compositions; scoring %d"
          % (DEN, len(GRID), len(grid)))

    sets, rooms = {}, {}
    for name, menus, alpha in ARMS:
        ints = {tag: integerize_menu(menu) for menu, tag in menus}
        tables = [cell_tables(ints[tag], rows)
                  for _menu, tag in menus for rows in rows_list]
        if rehearse:
            members, mean_room = run_arm_rehearsed(name, menus, alpha,
                                                   grid, tables)
        else:
            members, mean_room = run_arm(name, menus, alpha, grid, tables)
        sets[name], rooms[name] = members, mean_room
        if not rehearse:
            room_parity(menus, alpha)
        report_set(name, members, grid)
        parity_check(name, members, menus, alpha, rows_list)

    print()
    print("=" * 70)
    print("THE READING")
    for name, _m, _a in ARMS:
        print("   %-9s criterion %4d   recorded clean %4s   mean room %.6f"
              % (name, len(sets[name]), RECORD.get(name, "n/a"),
                 float(rooms[name])))

    if not rehearse:
        for name, _m, _a in ARMS:
            print("   P1 CONTAINMENT at %-9s: %d <= %d: %s"
                  % (name, len(sets[name]), RECORD[name],
                     len(sets[name]) <= RECORD[name]))
            assert len(sets[name]) <= RECORD[name], (
                "P1 BROKEN: the criterion set is larger than the recorded"
                " clean set, which the derivation forbids", name)
        order = ["3/4", "7/10", "3/5", "1/2"]
        sizes = [len(sets[n]) for n in order]
        print("   P2 sizes as coverage falls %s: %s; non-increasing: %s;"
              " empty at 1/2: %s"
              % (order, sizes,
                 all(sizes[i] >= sizes[i + 1] for i in range(3)),
                 sizes[3] == 0))
        print("   C4 NON-VACUITY at 3/4: the criterion set is neither"
              " empty nor the whole grid: %s"
              % (len(sets["3/4"]) not in (0, len(grid))))
        print("   P4 criterion set at 3/5 IS the gcd = 5 stratum: %s"
              % (set(sets["3/5"]) == {w for w in grid
                                      if gcd(*numerators(w, DEN)) == 5}))
        print("   P5 criterion set at 3/4 has at least 20 members: %s (%d)"
              % (len(sets["3/4"]) >= 20, len(sets["3/4"])))
        mr = [rooms[n] for n in order]
        print("   P6 mean room as coverage falls: %s; growing: %s"
              % ([round(float(x), 6) for x in mr],
                 all(mr[i] < mr[i + 1] for i in range(3))))


def run_arm_rehearsed(name, menus, alpha, grid, tables):
    """The same arm with C3 skipped -- the sample is not the record's."""
    saved = POPS.pop(name, None)
    try:
        return run_arm(name, menus, alpha, grid, tables)
    finally:
        if saved is not None:
            POPS[name] = saved


# ------------------------------------------------------------ stage two

def forced_clean(w, menus, alpha, rows_list):
    """Is this weight vector forced-clean across the arm?

    Every optimum at every cell, exiting the moment one cell charges a
    forced failure -- cleanliness is a conjunction, so the first miss
    settles the vector.
    """
    for menu, tag in menus:
        for rows in rows_list:
            cell = make_cell(menu, "%s-%s" % (tag, rows), rows, w)
            if not check_truth(cell):
                raise AssertionError(("cell is not a model", tag, rows))
            level, _m, _c, _s = operative_level(cell, alpha)
            got = dict(zip(KEYS, score(cell, level, alpha)))
            if got["above_forced"] or got["below_forced"]:
                return False
    return True


def stage_two():
    print("STAGE TWO -- IS THE CLEAN SET STRATIFIED BY GCD?")
    grid = GRID
    strata = {}
    for w in grid:
        strata.setdefault(gcd(*numerators(w, DEN)), []).append(w)
    print("   grid strata: %s"
          % {d: len(v) for d, v in sorted(strata.items())})
    hi_grid = sum(len(v) for d, v in strata.items() if d >= 2)
    print("   grid share with gcd >= 2: %d/%d = %.1f%%"
          % (hi_grid, len(grid), 100.0 * hi_grid / len(grid)))

    sets = {}
    for name, menus, alpha in ARMS:
        t0 = time.time()
        members = [w for w in grid if forced_clean(w, menus, alpha, ROWS)]
        sets[name] = members
        prof = gcd_profile(members)
        hi = sum(n for d, n in prof.items() if d >= 2)
        print()
        print("   ARM %-9s clean %4d (record %4s)  (%.0f s)"
              % (name, len(members), RECORD[name], time.time() - t0))
        print("      C6 REPRODUCTION: %s"
              % ("exact" if len(members) == RECORD[name] else "MISS"))
        assert len(members) == RECORD[name], (
            "C6: the early exit changed the clean set", name,
            len(members), RECORD[name])
        if not members:
            print("      EMPTY -- no profile to read, and not a pass.")
            continue
        print("      gcd profile: %s" % dict(sorted(prof.items())))
        print("      clean RATE within each stratum: %s"
              % {d: "%.1f%%" % (100.0 * prof.get(d, 0) / len(v))
                 for d, v in sorted(strata.items())})
        print("      P8 share with gcd >= 2: %d/%d = %.1f%%  (grid %.1f%%);"
              " ENRICHED: %s"
              % (hi, len(members), 100.0 * hi / len(members),
                 100.0 * hi_grid / len(grid),
                 hi / len(members) > hi_grid / len(grid)))

    print()
    print("   P9 clean set at 3/4 IS the union of strata 2,4,5,10: %s"
          % (set(sets["3/4"]) == {w for d in (2, 4, 5, 10)
                                  for w in strata.get(d, [])}))
    print("   P9 clean set at 3/5 IS the gcd = 5 stratum: %s"
          % (set(sets["3/5"]) == set(strata.get(5, []))))


# ---------------------------------------------------------- stage three

TIE_PROBE = ((10, 10, 20), (8, 8, 24), (5, 5, 30), (11, 11, 18),
             (13, 13, 14), (7, 16, 17), (2, 3, 35))


def tie_count(w, menus, alpha):
    """Cells of the arm carrying more than one optimal size vector."""
    return sum(1 for menu, tag in menus for rows in ROWS
               if len(all_optima(make_cell(menu, "%s-%s" % (tag, rows),
                                           rows, w), alpha)[1]) > 1)


def stage_three():
    """Does TIE MULTIPLICITY explain which vectors are clean?

    THE QUESTION, frozen before this engine. Stage two found the two
    coarsest gcd strata wholly clean at the loosest targets. The
    natural mechanism is ties: the forced criterion fails an atom only
    when EVERY optimum breaks the threshold rule, so a cell with many
    optima is hard to fail, and coarse weights collide costs -- sum
    s_r w_r takes fewer distinct values when the weights share a large
    divisor -- so coarse SHOULD mean tie-rich and tie-rich should mean
    clean.

    T1. The coarse vectors are tie-rich. (Nearly a derivation: cost
         collisions follow from the shared divisor.)
    T2. Tie count PREDICTS cleanliness -- clean vectors carry more
         ties than failing ones. This is the mechanism claim and the
         only one worth testing; a clean vector at ZERO ties refutes
         it outright, one exhibit sufficing to kill a universal.

    WHAT IT FOUND. T1 HOLDS: the coarse vectors are tie-rich, 394 and
    367 tied cells of 625 at coverage 3/4, against a gcd = 1 range
    running 0 to 307.

    T2 IS REFUTED IN BOTH DIRECTIONS AT ONCE, WHICH IS AS DEAD AS A
    MECHANISM GETS. Ties are not NECESSARY: (7, 16, 17) is forced-clean
    at ZERO tied cells, at both targets. And they are not SUFFICIENT:
    (5, 5, 30) carries 350 tied cells -- more than either clean
    near-diagonal vector -- and FAILS. Cleanliness is not a function of
    tie multiplicity, so what the coarse strata buy is not the
    protection of many optima, and the open question keeps its whole
    content.

    The hypothesis is attractive because the two near-diagonal clean
    vectors (11, 11, 18) and (13, 13, 14) carry 289 and 307 tied cells
    and look like the pattern. It took the two off-pattern exhibits to
    kill it, which is why this probe is EXHIBITS and not a sample: read
    first off a stride sample of 40 gcd = 1 vectors, the same question
    returned clean vectors carrying FEWER ties than failing ones, 4.2
    against 35.9 on average -- an artifact of a stride that missed
    every near-diagonal clean vector. A mean over a sample answered the
    question backwards; two exhibits answered it.
    """
    print("STAGE THREE -- DOES TIE MULTIPLICITY EXPLAIN CLEANLINESS?")
    for alpha, lbl in ((F(1, 4), "3/4"), (ALPHA, "7/10")):
        print("   coverage %s:" % lbl)
        for a in TIE_PROBE:
            w = tuple(F(x, DEN) for x in a)
            print("      %-12s gcd %2d   tied cells %3d/625   forced-clean"
                  " %s" % (str(a), gcd(*a), tie_count(w, OLD, alpha),
                           forced_clean(w, OLD, alpha, ROWS)))


if __name__ == "__main__":
    if "--stage3" in sys.argv:
        stage_three()
    elif "--stage2" in sys.argv:
        stage_two()
    else:
        main()
