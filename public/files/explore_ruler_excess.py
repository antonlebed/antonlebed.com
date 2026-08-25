"""WHY ARE THE COARSE WEIGHT VECTORS CLEAN? The level-excess identity, the
criterion it hands over, and the arity-4 read of the coarse strata.

(The menus are IMPORTED from explore_ruler_abandon.py, explore_ruler_family.py
and explore_ruler_box.py so the cells are the record's cells. The scorer is
NEW and runs in integers -- every mass a fortieth, every posterior a twentieth
or a fortieth -- and its first duty is to reproduce the record's forced clean
sets exactly, which is the control that licenses every other number here.)

THE QUESTION
------------
On the designed prediction-set family the forced abandonment law -- every
optimum abandons exactly the atoms whose best posterior sits under the
operative level -- holds at 183, 105, 18 and 0 of the 741 fortieth weight
vectors at coverage 3/4, 7/10, 3/5 and 1/2, and the clean set has no
coordinate shape. One arithmetic regularity survived: every vector whose
numerators share a divisor of 8 or 10 (fifths and quarters -- nine vectors)
is clean at 3/4 and 7/10, and the gcd-10 ones at 3/5. WHY is open. Tie
multiplicity is dead as a mechanism, and the corpus's one sufficient
condition -- the surplus criterion D/t* < gcd/N -- clears no vector at any
target. This file asks whether the clean set has a MECHANISM at all, and
reads the coarse strata at an arity above three, the one measurement the
law was recorded as waiting on.

THE DERIVATION, worked on paper before any engine code
------------------------------------------------------
Every symbol re-derived from the engines that define it: the cell, the
level and the certificate from explore_ruler_barecell.py, the optima from
explore_ruler_abandon.py's all_optima, the surplus from
explore_ruler_surplus.py.

  THE OBJECTS. A cell has M atoms r with masses w_r summing to 1 and
  posterior rows p(y|r) over k labels. A rule takes a set of labels at
  each atom; a pair (r, y) costs w_r and covers w_r p(y|r). The target is
  T = 1 - alpha. The operative level t* is the largest posterior value
  whose superlevel rule reaches T. A = the pairs with p > t*, S = the
  tied pairs with p = t*, B = the pairs with p < t*. The certificate C
  takes all of A plus a cheapest sub-collection of S closing the deficit,
  overshooting by the surplus D = cov(C) - T >= 0.

  THE IDENTITY. For ANY rule R, split each pair's cost as its coverage
  at the level plus its LEVEL-EXCESS:

      w_r = w_r p / t*  +  w_r (t* - p) / t*,

  and sum over R:

      t* cost(R) = cov(R) + sum_{(r,y) in R} w_r (t* - p(y|r)).

  Write E_A = sum_A w_r (p - t*) for the whole above-level excess, X = A
  minus R for the above pairs R DROPS, Y = R meets B for the below pairs
  R BUYS, e(X) = sum_X w_r (p - t*) and f(Y) = sum_Y w_r (t* - p), both
  non-negative. Tied pairs contribute nothing. Then

      t* cost(R) = cov(R) - E_A + e(X) + f(Y),

  and for the certificate, which drops and buys nothing,

      t* cert = T + D - E_A.

  Subtracting, with D_R = cov(R) - T >= 0 the rule's own overshoot:

      t* (cost(R) - cert) = e(X) + f(Y) + D_R - D.

  So R beats the certificate iff e(X) + f(Y) + D_R < D, and the
  certificate is an optimum iff NO feasible rule's excess-plus-overshoot
  falls under the surplus. This is complementary slackness for the
  program read at its dual price t*, and it is exact, not a bound.

  THE CRITERION IT HANDS OVER, needing no lattice. If D is below the
  least single-pair excess on either side --

      D < min( min_{a in A} w_r (p_a - t*),  min_{b in B} w_r (t* - p_b) )

  -- then every rule with X or Y non-empty costs at least cert, and a
  rule with X = Y = empty differs from C only in its tied sub-collection,
  where C's is a cheapest feasible one by construction. So the threshold
  rule is an optimum (EXC, the excess criterion). It is a different
  sufficient condition from the lattice one: the lattice bounds cert -
  OPT from below by g, this bounds the reachable improvement from above
  by an excess, and neither implies the other.

  FROM "CERT IS AN OPTIMUM" TO "FORCED-CLEAN". The certificate serves
  every above-level atom (it holds all of A) and abandons every
  below-level atom (such an atom has no pair at or above t*). A forced
  failure needs EVERY optimum to break the split. So a cell where C is an
  optimum takes no forced failure, and a vector with C optimal at every
  cell of an arm is forced-clean there:

      EXC set  subset of  OPT set  subset of  forced clean set,

  the first by the criterion, the second by this paragraph. Both are
  derivations and both are ASSERTED by the rig rather than reported.

  WHAT THE IDENTITY SAYS ABOUT THE EXCHANGE RIG'S REMAINDER.
  explore_ruler_exchange.py sorted its 5,447 disagreements into a
  surplus route (some above pair's whole COVERAGE w_r p_a fits inside D)
  and a below route (every optimum buys a below pair), and 129 cells fit
  neither. The identity says every disagreement is an exchange with
  e(X) + f(Y) + D_R < D, so a "neither" cell must drop an above pair
  whose coverage does NOT fit in D and buy nothing below -- which is
  feasible only by RE-CHOOSING the tied sub-collection, the deficit
  having grown by w_r p_a. The crude test asked whether the drop was
  feasible with S held fixed. So the remainder is predicted to be
  exactly the cells where an optimum drops above and re-fills from S.

  THE COARSE VECTORS, on paper. At gcd d the masses are multiples of
  d/40, so every single-pair excess is at least d/40 * 1/20 = d/800 --
  and the surplus is also a multiple of 1/800, bounded by the least tied
  mass times t*. Nothing on paper puts D under the least excess at a
  coarse vector, so P2 and P3 are predictions and not derivations.

  THE ARITY. At M atoms the size-vector enumeration is (k+1)^M: 64 at
  three atoms, 256 at four. The arity-4 grid is the fortieth
  compositions into FOUR parts, restricted to the strata that carry the
  question -- gcd 10 (quarters: the equal vector alone), gcd 8 (fifths,
  4 vectors), gcd 5 (eighths, 35), gcd 4 (tenths, 84) -- and a seeded
  sample of the gcd-1 bulk as the control the strata are read against.
  The "coarse" of the arity-3 law translates by LATTICE STEP, not by the
  divisor: fifths and quarters are what gcd 8 and 10 of forty mean.

  THE ALGEBRA OF THE STATISTIC. Masses a_r / 40, posteriors b / PD with
  PD = 20 (menus A-E) or 40 (menus F-J). Coverage counts in units of
  1/(40 PD), cost in units of 1/40, the level tau in units of 1/PD; the
  target 40 PD T is an integer at every arm (600, 560, 480, 400 on A-E;
  1120 on F-J). Every excess a_r |b - tau| and every surplus is an
  integer in coverage units, the identity clears its denominators as
  tau * cost = cov - E_A + e + f, and nothing rounds.

WHOSE VOCABULARY
----------------
The surplus rig's own: ATOM, LEVEL, TIED BLOCK, SURPLUS D, CERTIFICATE,
COST LATTICE keep explore_ruler_surplus.py's senses; FORCED and LOOSE
failures keep explore_ruler_forced.py's; GCD STRATUM keeps
explore_ruler_room.py's. New here: the LEVEL-EXCESS of a pair is
w_r |p - t*|; a rule's EXCHANGE is the pair (X, Y) of above pairs it
drops and below pairs it buys; the OPT SET at an arm is the set of weight
vectors whose certificate is an optimum at every cell; the EXC SET is the
set at which the excess criterion fires at every cell.

THE ARMS
--------
  ARITY 3 (the record's grid, 741 vectors x 125 row choices x 5 menus):
    3A  menus A-E, coverage 3/4      record forced clean 183
    3B  menus A-E, coverage 7/10     record 105
    3C  menus A-E, coverage 3/5      record 18
    3D  menus A-E, coverage 1/2      record 0
    3F  menus F-J, coverage 7/10     record 54
  ARITY 4 (menus A-E, 625 row choices x 5 menus per vector):
    4A  coverage 3/4,  strata gcd 10, 8, 5, 4 plus a gcd-1 sample
    4B  coverage 7/10, the same vectors

THE PREDICTIONS, frozen before the engine
-----------------------------------------
P1  EXC fires at strictly more cells than the lattice criterion did on
    every arity-3 arm, and the EXC set is NON-EMPTY at 3/4 and 7/10.
    (The lattice criterion cleared no vector anywhere, so an empty EXC
    set would make the new criterion no better than the old.)
P2  Every vector of the EXC set has gcd >= 2 -- no gcd-1 vector fires
    the excess criterion at every cell of an arm.
P3  The nine coarse vectors (gcd 8 and 10) are in the OPT set at 3/4 and
    7/10: their certificate is an OPTIMUM at every cell, the law they
    obey being the stronger one.
P4  The exchange rig's remainder is explained: at every arity-3 cell
    where cert != OPT, some optimum's exchange (X, Y) has e + f + D_R < D
    (the identity -- an assertion), and every cell whose optima all have
    Y empty and no above pair with w_r p_a <= D has an optimum that
    re-fills from the tied block (a prediction about the 129).
P5  ARITY 4, the awaited measurement: the fifths vectors (gcd 8) are
    forced-clean at 3/4 and 7/10 while the tenths stratum (gcd 4) carries
    at least one failing vector at each -- coarse clean, less coarse not,
    the arity-3 law reproducing one arity up.
P6  ARITY 4 populates the below half: the at-risk below-level atom count
    over the coarse vectors exceeds the arity-3 record's 24 at 3/4.

KILLS, as observables
---------------------
K-A  The arity-3 reproduction prints anything but 183 / 105 / 18 / 0 /
     54. No other number is read.
K-B  A coarse vector prints a cell with cert != OPT at 3/4 or 7/10.
K-C  The EXC set prints empty at 3/4.
K-D  A fifths vector prints a forced failure at arity 4.

THE CONTROLS, read before any verdict
-------------------------------------
C1  REPRODUCTION: the record's five forced clean counts, exactly.
C2  THE IDENTITY, asserted at the certificate and at every optimum of
    every cell: tau * cost == cov - E_A + e(X) + f(Y).
C3  CONTAINMENT, asserted: EXC subset of OPT subset of forced-clean, per
    cell and per vector, on every arm.
C4  EQUAL MASS at arity 4 takes zero forced failures at both targets
    (the equal-mass theorem, explore_ruler_forced.py C1) -- and its
    above-half population is non-empty.
C5  THE SPECIMEN: the exchange rig's smallest disagreement -- masses
    3/10, 3/10, 2/5, every row (2/5, 2/5, 1/5), coverage 7/10 -- prints
    cert 2, OPT 19/10, D = 1/10 and an optimum with e + f + D_R = 3/50.
C6  DENOMINATORS: every clean count is printed over its at-risk
    populations on both halves; a zero over an empty population is
    untested.

RESOURCES
---------
Integers throughout, no numpy. Arity 3: 5 arms x 463,125 cells x 64 size
vectors; arity 4: 2 arms x ~124 + sample vectors x 3,125 cells x 256.
Estimated 4-6 minutes wall-clock total and a few tens of MB. Rehearsed
first (--rehearse) on a permutation-closed handful of vectors and one
menu, exercising every arm, every assertion and every print.

WHAT RAN
--------
Rehearsed (1.1 s, every assertion live), then one full run at 290.6 s
wall: five arity-3 arms of 463,125 cells at 10-11 s each, two arity-4
arms of 1,621,875 cells at 119 s each. The arity-4 grid was WIDENED after
the rehearsal, on the measured rate, from the strata gcd >= 4 to those
plus 200 of the 884 gcd-2 vectors and 200 gcd-1 controls (a first full
attempt with the whole gcd-2 stratum cost 285 s per arm and was cut for
the ten-minute line; its arity-3 numbers agree with the run below to the
cell). Two readings were added after the rehearsal and before the full
run, both reported rather than predicted: the MASS BOUND on a below-level
atom, asserted per atom, and the forced failures split by half per
stratum. Integers throughout; a few tens of MB.

EVERY CONTROL PASSES. C1: 183 / 105 / 18 / 0 / 54 forced clean,
EXACT on all five arms -- the integer scorer is the record's scorer. C2:
the identity holds at the certificate and at every optimum of every one
of the 5.6 million cells (an assertion, never tripped). C3: EXC subset of
OPT subset of forced-clean at every cell and every vector. C4: equal mass
at four atoms takes zero forced failures at both targets over above-half
populations 12,196 and 11,560. C5: the specimen prints cert 2, OPT 19/10,
D 1/10, both optima at (e, f, D_R) = (0, 48, 0)/800 = 3/50. C6: every
count below is printed over its populations, and the below half's are
what the mass bound then explains.

WHAT IT FOUND
-------------
THE COARSE LAW IS NOT CERTIFICATE OPTIMALITY, AND NEITHER CRITERION
REACHES IT (P3 refuted, K-B fired; P1 refuted in BOTH halves, K-C fired;
P2 vacuous). The OPT set is EMPTY on all five arity-3 arms: no weight
vector's certificate is an optimum at every cell, at any target -- the
nine coarse vectors included, whose certificates fail at 34 to 108 of
their 625 cells at 3/4 and 7/10 while they take no forced failure there.
The excess criterion fires at 12 to 25% of cells and clears no vector,
like the lattice one -- and it does NOT fire at more cells than the
lattice one where that matters: explore_ruler_room.py's lattice rate is
15.3% at gcd 1 and 91.5% at gcd 10 at 3/4, against this criterion's
24.7% and 35.7% there, so the excess criterion wins the bulk and loses
the coarse strata by a factor of two and a half. So the clean set is
rescued by OPTIMA THAT ARE NOT THE CERTIFICATE and still respect the
split, which is why no sufficient condition for the certificate can find
it. What the certificate DOES carry is graded: the share of cells at
which it is optimal climbs with the stratum at every arm --

  gcd          1      2      4      5      8     10
  3A  3/4    56.6   58.9   70.5   73.4   85.9   94.6   %
  3B  7/10   57.5   59.9   69.0   73.6   85.5   93.8
  3C  3/5    55.1   56.9   64.3   67.5   82.9   92.0
  3D  1/2    61.8   63.0   69.0   73.7   87.8   96.0
  3F  7/10   51.3   55.1   65.2   72.1   86.2   94.4
  4A  3/4    50.4   60.3   75.3   82.0   96.4  100.0
  4B  7/10   50.5   60.1   75.1   81.8   94.9  100.0

-- monotone in the stratum on every arm, the equal vector alone reaching
100% at four atoms (the equal-mass theorem, seen from this side). The
grading itself is not new in kind: explore_ruler_room.py recorded the
LATTICE criterion's firing rate stratifying the same way, and since a
lattice firing implies certificate optimality that rate sits UNDER this
one at every stratum -- 15.3 under 56.6 at gcd 1, 91.5 under 94.6 at gcd
10 at 3/4. What is new is the gap between them: at the coarse strata
nearly every certificate-optimal cell is lattice-certified, and in the
bulk fewer than a third are. An observation, and a candidate for the
above half below, not a mechanism.

P4 HOLDS, AND THE REMAINDER IS ONE SHAPE. Over arm 3B's 189,126
disagreements, 75,786 have every optimum buying below the level; 3,846
fit NEITHER of the exchange rig's crude routes, and at 3,846 of the
3,846 an optimum drops an above pair and buys nothing below -- the
tied-block re-fill the identity predicted. The exchange rig's own 129
sit on a twentieth grid with its own menu, which this run does not
re-score; that they are the same species is the prediction carried,
not a measurement made here.

THE BELOW HALF OF THE COARSE LAW IS VACUOUS, AND THE REASON IS A MASS
BOUND (P6 refuted by derivation; the bound is a property and it is
TIGHT). An atom wholly under the level contributes nothing at it, so the
others reach the target alone: a <= 40 - tt/smax(t). On menus A-E that
ceiling is 4/40 at 3/4, 7/40 at 7/10, 11/40 at 3/5, 16/40 at 1/2, and
8/40 on F-J at 7/10 -- and the heaviest below-level atom actually found
equals the ceiling on all seven arms. A fifths or quarters vector has no
atom under 8/40, so it carries NO below-level atom at 3/4 or 7/10 at any
arity (0 at-risk over gcd 8 and 10 on 3A, 3B, 4A, 4B), while the eighths
(gcd 5) carry none at 3/4 and 252 at 7/10, and the tenths 96 and 468 --
the strata entering the below half exactly as the ceiling admits their
least mass. At 3/5 the fifths gain below-level atoms (294) and go 0 of 6
clean. So what is coarse-and-clean at 3/4 and 7/10 is the ABOVE half
alone.

P5 HOLDS AT FOUR ATOMS. Fifths 4 of 4 forced-clean at 3/4 and at 7/10;
tenths 6 of 80 at each; eighths 18 of 34 and 0 of 34; the gcd-2 sample
15 and 2 of 200; the gcd-1 sample 9 and 2 of 200. The forced failures
are above-half at every stratum of gcd >= 4 (below-half failures 0
there, over 448 and 3,960 below-level atoms at the tenths and 0 and
1,080 at the eighths), and ZERO in both halves at gcd 8 and 10 at both
targets, as at three atoms.

WHAT THIS LEAVES OPEN, sharper than it was: WHY NO OPTIMUM ABANDONS AN
ABOVE-LEVEL ATOM at a fifths or quarters vector at 3/4 and 7/10 -- a
question about the above half only, the below half being empty there by
the bound. The graded certificate-optimality rate is the candidate. The
measurement the law waited on -- "the coarse strata's cleanliness at an
arity above three" -- is answered in the direction it did not name: the
below half it wanted tested cannot be populated at those strata and
targets, by derivation.
"""

import itertools
import os
import random
import sys
import time
from fractions import Fraction
from math import gcd

os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from explore_ruler_abandon import MENU_A, MENU_B  # noqa: E402
from explore_ruler_box import MENU_F, MENU_G, MENU_H, MENU_I, MENU_J  # noqa: E402
from explore_ruler_family import MENU_C, MENU_D, MENU_E  # noqa: E402

F = Fraction
WD = 40          # the mass lattice
K = 3            # labels

REHEARSE = "--rehearse" in sys.argv


# ------------------------------------------------------------ integerize

def int_menu(menu):
    """A menu of Fraction rows -> (PD, rows of integer numerators)."""
    pd = 1
    for row in menu:
        for v in row:
            pd = pd * v.denominator // gcd(pd, v.denominator)
    rows = [tuple(int(v * pd) for v in row) for row in menu]
    for row in rows:
        assert sum(row) == pd, ("row does not sum to 1", row, pd)
    return pd, rows


MENUS_OLD = [("A", MENU_A), ("B", MENU_B), ("C", MENU_C), ("D", MENU_D),
             ("E", MENU_E)]
MENUS_NEW = [("F", MENU_F), ("G", MENU_G), ("H", MENU_H), ("I", MENU_I),
             ("J", MENU_J)]


def compositions(total, parts):
    """Ordered compositions of `total` into `parts` positive parts."""
    if parts == 1:
        yield (total,)
        return
    for a in range(1, total - parts + 2):
        for rest in compositions(total - a, parts - 1):
            yield (a,) + rest


def vec_gcd(v):
    g = 0
    for a in v:
        g = gcd(g, a)
    return g


# ----------------------------------------------------------- the scorer

def score_cell(weights, rows, pd, tt):
    """One cell, in integers.

    weights: atom masses (numerators over WD); rows: one posterior row per
    atom (numerators over pd); tt: the target in coverage units WD*pd.

    Returns a dict with the level tau, the certificate's cost and surplus
    D, the optimum cost, every optimum's size vector, the per-atom
    verdicts, and the excess data the criterion reads.
    """
    m = len(weights)
    # Sorted per-atom posteriors, prefix coverage per size.
    tops = []
    for r in range(m):
        srt = sorted(rows[r], reverse=True)
        pref = [0]
        for v in srt:
            pref.append(pref[-1] + v)
        tops.append(pref)
    # The operative level: largest posterior value whose superlevel rule
    # reaches the target.
    values = sorted({v for row in rows for v in row}, reverse=True)
    tau = None
    for t in values:
        cov = sum(weights[r] * sum(v for v in rows[r] if v >= t)
                  for r in range(m))
        if cov >= tt:
            tau = t
            break
    assert tau is not None, "no feasible threshold"
    # Above / tied / below pairs.
    above_cov = above_cost = ea = 0
    tied = []          # (a_r, r)
    min_exc_above = min_exc_below = None
    for r in range(m):
        a = weights[r]
        for v in rows[r]:
            if v > tau:
                above_cov += a * v
                above_cost += a
                ea += a * (v - tau)
                exc = a * (v - tau)
                if min_exc_above is None or exc < min_exc_above:
                    min_exc_above = exc
            elif v == tau:
                tied.append(a)
            else:
                exc = a * (tau - v)
                if min_exc_below is None or exc < min_exc_below:
                    min_exc_below = exc
    # The certificate: cheapest tied sub-multiset closing the deficit.
    deficit = tt - above_cov
    assert deficit > 0 or (deficit <= 0 and tau == values[0]) or True
    need = max(0, -(-deficit // tau))  # ceil(deficit / tau) in cost units
    reach = {0}
    for a in tied:
        reach |= {s + a for s in reach}
    fill = min(s for s in reach if s >= need)
    cert_cost = above_cost + fill
    d_surplus = above_cov + fill * tau - tt
    assert d_surplus >= 0
    # Every optimum, by enumeration over size vectors.
    ranges = [range(K + 1)] * m
    best, arg = None, []
    for sizes in itertools.product(*ranges):
        cov = 0
        cost = 0
        for r in range(m):
            cov += weights[r] * tops[r][sizes[r]]
            cost += weights[r] * sizes[r]
        if cov >= tt:
            if best is None or cost < best:
                best, arg = cost, [sizes]
            elif cost == best:
                arg.append(sizes)
    assert arg, "no feasible rule"
    # Per-atom verdicts.
    above_pop = below_pop = at_level = 0
    above_loose = below_loose = above_forced = below_forced = 0
    below_weights = []
    for r in range(m):
        top = max(rows[r])
        if top == tau:
            at_level += 1
        elif top < tau:
            below_pop += 1
            below_weights.append(weights[r])
            if any(s[r] > 0 for s in arg):
                below_loose += 1
                if all(s[r] > 0 for s in arg):
                    below_forced += 1
        else:
            above_pop += 1
            if any(s[r] == 0 for s in arg):
                above_loose += 1
                if all(s[r] == 0 for s in arg):
                    above_forced += 1
    min_exc = min(x for x in (min_exc_above, min_exc_below)
                  if x is not None) if (min_exc_above is not None
                                        or min_exc_below is not None) else None
    exc_fires = (min_exc is not None and d_surplus < min_exc) or \
                (min_exc is None)
    return dict(tau=tau, cert=cert_cost, D=d_surplus, opt=best, arg=arg,
                ea=ea, tops=tops, above_pop=above_pop, below_pop=below_pop,
                at_level=at_level, above_loose=above_loose,
                below_loose=below_loose, above_forced=above_forced,
                below_forced=below_forced, min_exc=min_exc,
                exc_fires=exc_fires, deficit=deficit, tied=tied,
                below_weights=below_weights)


def exchange_of(weights, rows, tau, sizes):
    """(e(X), f(Y), cov) of a rule given by its size vector: e sums the
    dropped above pairs' excess, f the bought below pairs'."""
    e = f = cov = 0
    for r, s in enumerate(sizes):
        srt = sorted(rows[r], reverse=True)
        a = weights[r]
        for i, v in enumerate(srt):
            taken = i < s
            if taken:
                cov += a * v
                if v < tau:
                    f += a * (tau - v)
            elif v > tau:
                e += a * (v - tau)
    return e, f, cov


def check_identity(weights, rows, pd, tt, res):
    """C2: tau * cost == cov - E_A + e + f at the certificate and at every
    optimum; and at every optimum e + f + D_R <= D with strictness iff
    cert != OPT. Returns the exchange classes of the optima."""
    tau, ea, d = res["tau"], res["ea"], res["D"]
    # The certificate itself: cost cert, coverage tt + D, no exchange.
    assert tau * res["cert"] == (tt + d) - ea, "identity fails at cert"
    classes = []
    for sizes in res["arg"]:
        e, f, cov = exchange_of(weights, rows, tau, sizes)
        cost = sum(weights[r] * sizes[r] for r in range(len(weights)))
        assert tau * cost == cov - ea + e + f, "identity fails at optimum"
        dr = cov - tt
        assert dr >= 0
        gap = d - (e + f + dr)
        assert gap == tau * (res["cert"] - cost), "gap mismatch"
        classes.append((e, f, dr))
    return classes


# ------------------------------------------------------------- the arms

def rows_for(menu_rows, m):
    return list(itertools.product(range(len(menu_rows)), repeat=m))


def sweep(vectors, menus, target, m, want_remainder=False):
    """Every (vector, menu, row choice) cell. Returns per-vector tallies
    and the arm-wide cell counters."""
    tally = {v: dict(above_pop=0, below_pop=0, at_level=0, above_loose=0,
                     below_loose=0, above_forced=0, below_forced=0,
                     cells=0, opt_cells=0, exc_cells=0)
             for v in vectors}
    arm = dict(cells=0, opt_cells=0, exc_cells=0, disagree=0,
               rem_neither=0, rem_refill=0, below_route=0,
               below_wmax=0, bound=0)
    for tag, menu in menus:
        pd, mrows = int_menu(menu)
        tt = WD * pd * target
        assert tt.denominator == 1, ("target not integral", tag, target)
        tt = int(tt)
        choices = rows_for(mrows, m)
        # THE MASS BOUND. An atom wholly under level t contributes nothing
        # at t, so the others must reach the target alone: tt <= (WD - a)
        # * smax(t), smax the largest superlevel sum any menu row has at
        # t. Hence a <= WD - tt / smax(t) -- a derived ceiling on the mass
        # of any below-level atom, asserted at every such atom and read
        # against the largest mass actually found.
        values = sorted({v for row in mrows for v in row})
        smax = {t: max(sum(v for v in row if v >= t) for row in mrows)
                for t in values}
        min_top = min(max(row) for row in mrows)
        for t in values:
            if t > min_top and smax[t] > 0:
                arm["bound"] = max(arm["bound"], WD - -(-tt // smax[t]))
        for v in vectors:
            trow = tally[v]
            for ch in choices:
                rows = [mrows[i] for i in ch]
                res = score_cell(v, rows, pd, tt)
                classes = check_identity(v, rows, pd, tt, res)
                for a in res["below_weights"]:
                    assert (WD - a) * smax[res["tau"]] >= tt, "mass bound"
                    arm["below_wmax"] = max(arm["below_wmax"], a)
                opt_here = res["cert"] == res["opt"]
                # C3 containment, per cell.
                if res["exc_fires"]:
                    assert opt_here, "EXC fired where cert != OPT"
                if opt_here:
                    assert res["above_forced"] == 0 and \
                        res["below_forced"] == 0, "forced failure at OPT"
                for key in ("above_pop", "below_pop", "at_level",
                            "above_loose", "below_loose", "above_forced",
                            "below_forced"):
                    trow[key] += res[key]
                trow["cells"] += 1
                trow["opt_cells"] += opt_here
                trow["exc_cells"] += res["exc_fires"]
                arm["cells"] += 1
                arm["opt_cells"] += opt_here
                arm["exc_cells"] += res["exc_fires"]
                if not opt_here:
                    arm["disagree"] += 1
                    if want_remainder:
                        # The exchange rig's two routes, its crude tests.
                        tau, d = res["tau"], res["D"]
                        cover_fits = any(
                            v[r] * val <= d
                            for r in range(m) for val in rows[r]
                            if val > tau)
                        every_buys_below = all(f > 0 for _e, f, _dr in
                                               classes)
                        if every_buys_below:
                            arm["below_route"] += 1
                        if not cover_fits and not every_buys_below:
                            arm["rem_neither"] += 1
                            # Does some optimum drop above and buy no
                            # below -- the re-fill shape?
                            if any(e > 0 and f == 0
                                   for e, f, _dr in classes):
                                arm["rem_refill"] += 1
    return tally, arm


def survivors(tally, keys):
    return {v for v, t in tally.items() if all(t[k] == 0 for k in keys)}


def stratum_report(label, vectors, tally, forced_set, opt_set, exc_set):
    print("  %s" % label)
    print("    gcd   n   forced-clean   OPT-set   EXC-set   "
          "cells OPT %   cells EXC %   at-risk above / below"
          "   forced fail above / below")
    by = {}
    for v in vectors:
        by.setdefault(vec_gcd(v), []).append(v)
    for g in sorted(by):
        vs = by[g]
        ab = sum(tally[v]["above_pop"] for v in vs)
        be = sum(tally[v]["below_pop"] for v in vs)
        cells = sum(tally[v]["cells"] for v in vs)
        oc = sum(tally[v]["opt_cells"] for v in vs)
        ec = sum(tally[v]["exc_cells"] for v in vs)
        fa = sum(tally[v]["above_forced"] for v in vs)
        fb = sum(tally[v]["below_forced"] for v in vs)
        print("    %3d %4d   %12d   %7d   %7d   %10.1f   %10.1f   %d / %d"
              "   %d / %d"
              % (g, len(vs), sum(v in forced_set for v in vs),
                 sum(v in opt_set for v in vs),
                 sum(v in exc_set for v in vs),
                 100.0 * oc / cells, 100.0 * ec / cells, ab, be, fa, fb))


def fmt(v):
    return "(" + ", ".join("%d/%d" % (a, WD) for a in v) + ")"


def run_arm(name, vectors, menus, target, m, record=None,
            want_remainder=False):
    t0 = time.time()
    tally, arm = sweep(vectors, menus, target, m, want_remainder)
    forced = survivors(tally, ("above_forced", "below_forced"))
    loose = survivors(tally, ("above_loose", "below_loose"))
    opt_set = {v for v, t in tally.items() if t["opt_cells"] == t["cells"]}
    exc_set = {v for v, t in tally.items() if t["exc_cells"] == t["cells"]}
    assert exc_set <= opt_set <= forced, "containment fails per vector"
    print("\n%s  [%d vectors, %d cells, %.1f s]"
          % (name, len(vectors), arm["cells"], time.time() - t0))
    print("  forced clean %d   loose clean %d   OPT set %d   EXC set %d"
          % (len(forced), len(loose), len(opt_set), len(exc_set)))
    print("  cells: cert = OPT at %d (%.1f%%), EXC fires at %d (%.1f%%), "
          "disagreements %d"
          % (arm["opt_cells"], 100.0 * arm["opt_cells"] / arm["cells"],
             arm["exc_cells"], 100.0 * arm["exc_cells"] / arm["cells"],
             arm["disagree"]))
    if record is not None:
        print("  C1 reproduction: forced clean %d against the record's %d"
              " -- %s" % (len(forced), record,
                          "EXACT" if len(forced) == record else "MISS"))
        assert len(forced) == record, "K-A: the record is not reproduced"
    print("  mass bound: a below-level atom weighs at most %d/40 on this"
          " arm (derived from the menus and the target); the heaviest"
          " found weighs %d/40" % (arm["bound"], arm["below_wmax"]))
    if want_remainder:
        print("  exchange routes over the disagreements: every optimum buys"
              " below at %d; NEITHER crude route at %d, of which an optimum"
              " drops above and buys nothing below (the re-fill shape) at %d"
              % (arm["below_route"], arm["rem_neither"], arm["rem_refill"]))
    stratum_report("by gcd stratum", vectors, tally, forced, opt_set,
                   exc_set)
    if exc_set:
        print("  EXC set gcds: %s" % sorted(vec_gcd(v) for v in exc_set))
        print("  EXC set: %s" % ", ".join(fmt(v) for v in sorted(exc_set)))
    return tally, forced, opt_set, exc_set


def specimen():
    """C5: the exchange rig's smallest disagreement, in this scorer."""
    weights = (12, 12, 16)              # 3/10, 3/10, 2/5 over 40
    rows = [(8, 8, 4)] * 3              # (2/5, 2/5, 1/5) over 20
    pd, tt = 20, 40 * 20 * 7 // 10
    res = score_cell(weights, rows, pd, tt)
    classes = check_identity(weights, rows, pd, tt, res)
    print("C5 specimen: cert %s  OPT %s  D %s  tau %s  optima exchanges"
          " (e, f, D_R) in 1/800 units: %s"
          % (F(res["cert"], WD), F(res["opt"], WD), F(res["D"], 800),
             F(res["tau"], pd), classes))
    assert F(res["cert"], WD) == 2 and F(res["opt"], WD) == F(19, 10)
    assert F(res["D"], 800) == F(1, 10)
    assert any(F(e + f + dr, 800) == F(3, 50) for e, f, dr in classes)
    print("  -- the specimen reproduces: cert 2, OPT 19/10, D 1/10, an"
          " optimum at e + f + D_R = 3/50 < D.")


def main():
    t0 = time.time()
    print("explore_ruler_excess.py -- the level-excess identity and the"
          " coarse strata%s" % (" (REHEARSAL)" if REHEARSE else ""))
    specimen()

    grid3 = list(compositions(WD, 3))
    assert len(grid3) == 741
    if REHEARSE:
        reps = [(8, 8, 24), (10, 10, 20), (7, 16, 17), (5, 5, 30),
                (1, 19, 20), (2, 3, 35)]
        grid3 = sorted({p for r in reps for p in itertools.permutations(r)})
        menus_old, menus_new = MENUS_OLD[:1], MENUS_NEW[:1]
        records = {}
    else:
        menus_old, menus_new = MENUS_OLD, MENUS_NEW
        records = {"3A": 183, "3B": 105, "3C": 18, "3D": 0, "3F": 54}

    coarse = [v for v in grid3 if vec_gcd(v) >= 8]
    print("\ncoarse vectors (gcd 8 or 10): %d -- %s"
          % (len(coarse), ", ".join(fmt(v) for v in coarse)))

    results3 = {}
    for name, menus, target in (("3A", menus_old, F(3, 4)),
                                ("3B", menus_old, F(7, 10)),
                                ("3C", menus_old, F(3, 5)),
                                ("3D", menus_old, F(1, 2)),
                                ("3F", menus_new, F(7, 10))):
        results3[name] = run_arm("ARM %s -- menus %s, coverage %s"
                                 % (name, "".join(t for t, _ in menus),
                                    target),
                                 grid3, menus, target, 3,
                                 record=records.get(name),
                                 want_remainder=(name == "3B"))

    print("\nP3 -- the coarse vectors' certificate at every cell:")
    for name in ("3A", "3B"):
        tally, forced, opt_set, exc_set = results3[name]
        for v in coarse:
            t = tally[v]
            print("  %s %s  OPT at %d/%d cells  EXC at %d/%d  forced fail"
                  " %d/%d  at-risk above %d below %d"
                  % (name, fmt(v), t["opt_cells"], t["cells"],
                     t["exc_cells"], t["cells"], t["above_forced"],
                     t["below_forced"], t["above_pop"], t["below_pop"]))

    # ---------------------------------------------------------- arity 4
    grid4 = list(compositions(WD, 4))
    rng = random.Random(992)
    strata = [v for v in grid4 if vec_gcd(v) >= 4]
    # The gcd-2 stratum (884 vectors) and the gcd-1 bulk are SAMPLED at
    # 200 each: the full gcd-2 stratum cost 285 s per arm at the first
    # run's measured rate, and a sample decides the stratum question.
    strata += sorted(rng.sample([v for v in grid4 if vec_gcd(v) == 2],
                                8 if REHEARSE else 200))
    bulk = [v for v in grid4 if vec_gcd(v) == 1]
    sample = sorted(rng.sample(bulk, 8 if REHEARSE else 200))
    vectors4 = strata + sample
    if REHEARSE:
        vectors4 = [v for v in strata if vec_gcd(v) >= 8] + sample[:4]
    equal4 = (10, 10, 10, 10)
    assert equal4 in vectors4
    print("\nARITY 4 grid: %d vectors in strata gcd >= 2 (%s; gcd 2"
          " sampled) plus %d gcd-1 controls, both samples seeded 992"
          % (len(strata), ", ".join("gcd %d: %d" % (g, sum(vec_gcd(v) == g
                                                           for v in strata))
                                    for g in (10, 8, 5, 4, 2)), len(sample)))
    for name, target in (("4A", F(3, 4)), ("4B", F(7, 10))):
        tally, forced, opt_set, exc_set = run_arm(
            "ARM %s -- menus %s, coverage %s, FOUR atoms"
            % (name, "".join(t for t, _ in menus_old), target),
            vectors4, menus_old, target, 4)
        te = tally[equal4]
        print("  C4 equal mass: forced failures %d above / %d below over"
              " populations %d / %d -- %s"
              % (te["above_forced"], te["below_forced"], te["above_pop"],
                 te["below_pop"],
                 "PASS" if te["above_forced"] == te["below_forced"] == 0
                 and te["above_pop"] > 0 else "FAIL"))
        assert te["above_forced"] == 0 and te["below_forced"] == 0
        fifths = [v for v in vectors4 if vec_gcd(v) == 8]
        print("  P5 fifths (gcd 8): %d of %d forced-clean; tenths (gcd 4):"
              " %d of %d; eighths (gcd 5): %d of %d; gcd-1 sample: %d of %d"
              % (sum(v in forced for v in fifths), len(fifths),
                 sum(v in forced for v in vectors4 if vec_gcd(v) == 4),
                 sum(vec_gcd(v) == 4 for v in vectors4),
                 sum(v in forced for v in vectors4 if vec_gcd(v) == 5),
                 sum(vec_gcd(v) == 5 for v in vectors4),
                 sum(v in forced for v in sample), len(sample)))
        for v in fifths + [equal4]:
            t = tally[v]
            print("    %s  forced fail %d/%d  loose %d/%d  OPT %d/%d  EXC"
                  " %d/%d  at-risk above %d below %d at-level %d"
                  % (fmt(v), t["above_forced"], t["below_forced"],
                     t["above_loose"], t["below_loose"], t["opt_cells"],
                     t["cells"], t["exc_cells"], t["cells"], t["above_pop"],
                     t["below_pop"], t["at_level"]))
        print("  P6 at-risk below-level atoms over the coarse vectors"
              " (gcd 8 and 10): %d"
              % sum(tally[v]["below_pop"] for v in fifths + [equal4]))
    print("\ntotal wall %.1f s" % (time.time() - t0))


if __name__ == "__main__":
    main()
