"""WHAT EXCHANGE RESCUES THE CLEAN VECTORS THE SWAP LEMMA MISSES?
The mass-conserving exchange: a partner-dominated optimum serving the light atom.

(The menus, the grid and the integer scorer are IMPORTED from
explore_ruler_excess.py, and the swap lemma's own reader `swaps_for` from
explore_ruler_swap.py, so every cell, every optimum and every one-pair swap
here is the record's. New here is ONE exchange -- the set-valued swap -- read
off the optimum list the scorer already enumerates.)

THE QUESTION
------------
explore_ruler_swap.py proved the swap lemma: an optimum R abandoning an atom
r that holds, on ONE partner r' with s w_r <= w_r', a lowest taken label y
with w_r' p(y|r') <= w_r top_s(r) + D_R trades that pair for r's top s labels
at no extra cost, so some optimum serves r. The lemma rescues every
abandoning optimum at the nine coarse three-atom vectors and the five coarse
four-atom ones, and 162 of the 183 clean vectors at 3/4 and 105 of 105 at
7/10 at three atoms; at four atoms 23 of 29 and 5 of 11, the (8, 8, 12, 12)
permutations -- clean at both targets -- rescued by exchanges the lemma does
not name. This file asks what those exchanges are, and whether the lemma's
one-pair shape was ever the whole rescue.

THE DERIVATION, worked on paper before any engine code
------------------------------------------------------
Symbols as in explore_ruler_excess.py: M atoms with masses w_r (numerators
over 40) summing to 1, posterior rows over k = 3 labels, a rule taking the
top s_r labels at each atom at cost sum w_r s_r and coverage
sum w_r top_s(r); the target T; an optimum a cheapest rule covering T;
D_R = cov(R) - T its overshoot.

  THE MASS CONDITION IS AN EQUALITY (property). A swap the lemma fires
  yields a rule of cost opt - w_r' + s w_r <= opt that covers T. The
  optimum is the least cost of a covering rule, so the new cost is opt and

      w_r' = s w_r  EXACTLY  at every swap that fires at an optimum.

  The record's reader asserts `cost == opt` at every rescue and states the
  condition as an inequality; the inequality is the lemma's hypothesis and
  the equality is what its conclusion forces. So the swap is a
  DIVISIBILITY statement -- the partner's mass is an exact multiple of the
  light atom's -- which is why the gcd returned at one edge.

  THE SET-VALUED SWAP. Let R abandon r and let R' be R with a prefix of
  depth d_i dropped from each partner i in a set S and r's top s labels
  added. R' costs opt - sum_S w_i d_i + s w_r and covers
  cov(R) - sum_S (dropped coverage) + w_r top_s(r). It is an optimum iff

      sum_S w_i d_i = s w_r   and   sum_S (dropped coverage) <= w_r top_s(r) + D_R,

  the first by the same optimality argument (an inequality there would be
  a cheaper covering rule). At (8, 8, 12, 12) the two 12/40 partners
  together drop 24/40 = 3 x 8/40: the light atom takes ALL THREE of its
  labels, never two -- a first paper reading had it at 2 x 8/40, and the
  equality forbids it.

  WHAT THE SET-VALUED SWAP IS. Dropping prefixes on partners and adding a
  prefix on r produces a rule R' with R'_r = s > 0 and R'_i <= R_i at every
  partner; conversely any such R' is one such exchange. So

      the set-valued swap rescues R  <=>  some optimum serving r is
      DOMINATED by R on the partners (R'_i <= R_i for every i != r).

  The scorer enumerates every optimum, so the reading is a scan of that
  list and needs no new search. The lemma's own swap is the case of ONE
  partner dropping ONE label. Three shapes partition the dominated
  rescues: SINGLE (one partner, depth 1: the lemma's), DEEP (one partner,
  depth 2 or 3), MULTI (two or more partners). What the set-valued swap
  cannot reach is a serving optimum that GAINS a label on some partner
  while dropping on another -- call an abandoning optimum whose every
  serving optimum gains a GAIN case. At a vector clean above, every
  abandoning optimum has a serving optimum; the question is whether one is
  always dominated.

WHOSE VOCABULARY
----------------
explore_ruler_excess.py's and explore_ruler_swap.py's throughout -- ATOM,
LEVEL, OPTIMUM, OVERSHOOT, ABOVE half, FORCED, ABANDONING, RESCUED,
SWAP-CLEAN (every abandoning optimum at every cell rescued by the lemma),
ABOVE-CLEAN (no above-level atom forced-abandoned), LIGHTEST MASS w_min.
New here: MULTI-CLEAN -- every above-level abandoning optimum at every cell
rescued by a dominated serving optimum; the three SHAPES; the GAIN case.

THE ARMS
----------------------------------
  3A  menus A-E, three atoms, 3/4     3B  menus A-E, three atoms, 7/10
  4A  menus A-E, four atoms (gcd >= 4), 3/4     4B  the same at 7/10

THE PREDICTIONS, frozen before the engine
-----------------------------------------
P1  MASS CONSERVATION: at every dominated serving optimum of every
    abandoning optimum, the partners' dropped mass equals s w_r
    (asserted; a derivation).
P2  THE SET-VALUED SWAP IS THE WHOLE RESCUE AT THE CLEAN VECTORS:
    multi-clean equals above-clean on all four arms -- 183 / 105 / 29 / 11
    -- so the 21 + 6 + 6 clean vectors the lemma misses are rescued by DEEP
    or MULTI exchanges.
P3  At the (8, 8, 12, 12) permutations some rescue the lemma misses is a
    MULTI exchange on the two 12/40 partners at s = 3 (observable: the
    vector's MULTI count is positive at both targets, and every MULTI
    rescue there prints s = 3).
P4  THE STRONG FORM, over the whole grid: no GAIN case anywhere -- every
    abandoning optimum at an above-level atom that is not forced has a
    dominated serving optimum, at failing vectors as at clean ones.

KILLS, as observables
---------------------
K-A  The mass-conservation assertion trips.
K-B  An above-clean vector prints a GAIN case at 3A, 3B, 4A or 4B: an
     abandoning optimum whose every serving optimum takes MORE of some
     partner. Then the exchange behind the clean vectors is not a
     prefix-preserving swap of any size, and the set-valued swap files as a
     rule at the count it reaches.
K-C  A GAIN case at a failing vector (P4 dies, P2 may survive).
K-D  The reproduction prints anything but 183 / 105 forced clean and
     162 / 105 / 23 / 5 swap-clean with the lemma's rescue totals
     4,800 / 6,390 / 53,248 / 87,288.

THE CONTROLS, read before any verdict
-------------------------------------
C1  REPRODUCTION: the record's forced-clean, swap-clean and lemma-rescue
    counts on all four arms, exactly (K-D).
C2  THE LEMMA IS THE SINGLE SHAPE: at every abandoning optimum, `swaps_for`
    fires iff a dominated serving optimum of shape SINGLE exists
    (asserted; the equivalence derived above).
C3  CONTAINMENT: multi-clean inside above-clean and swap-clean inside
    multi-clean, per vector, on every arm (asserted).
C4  THE HAND CELL of the swap rig -- masses (8, 16, 16), rows (7, 7, 6),
    (11, 7, 2), (8, 6, 6), coverage 3/4 -- prints the optimum (0, 2, 3)
    rescued by the dominated optimum (2, 2, 2), shape SINGLE, mass 16
    dropped for s = 2.
C5  DENOMINATORS: every count prints over its abandoning-optimum
    population; a stratum with none prints as such.

THE SECOND LEG -- a reading, not a prediction
---------------------------------------------
The slack sigma = 1 - w_min - T (in fortieths, 10 - w_min at 3/4 and
12 - w_min at 7/10). The arm prints, per lightest mass, the clean counts
under the lemma and under the set-valued swap and the shape totals, so the
grading by sigma can be read with the exchange named -- whether the clean
vectors the lemma misses sit at one slack and whether a threshold in sigma
separates the strata the equality alone would predict.

RESOURCES
---------
Integers throughout, no numpy; the scorer is the excess rig's, the lemma's
reader the swap rig's. Two arity-3 arms of 463,125 cells and two arity-4
arms of 371,875; the new reading is a scan over the optimum list at cells
with abandonment. Estimated 90 s wall-clock and a few tens of MB, under
the memory watch. Rehearsed first (--rehearse) on the swap rig's handful of
vectors plus the (8, 8, 12, 12) permutations and one menu per arm,
exercising every arm, every assertion and every print.

WHAT RAN
--------
Rehearsed (1.1 s, every assertion live), then one full run at 70.0 s wall
under the memory watch, peak 15.3 MB; two readings were added after that
run and it was re-run at 70.4 s, peak 15.5 MB, every count of the first
run reproduced: an exhibit of the first GAIN case per arm (added after
the rehearsal), and THE FULL-PARTNER EXCHANGE below, derived reading the
zero-slack row of the first run and asserted at every cell of the second.
Integers throughout.

EVERY CONTROL PASSES. C1: swap-clean 162 / 105 / 23 / 5 and lemma rescues
4,800 / 6,390 / 53,248 / 87,288, EXACT on all four arms. C2: the lemma
fires iff a SINGLE-shape dominated optimum exists, asserted at 104,241 +
115,467 + 60,496 + 100,656 abandoning optima, never tripped. C3:
swap-clean inside multi-clean inside above-clean on every arm. C4: the
hand cell prints optima (0, 2, 3), (2, 1, 3), (2, 2, 2), the abandoning
(0, 2, 3) dominated by both others at shape SINGLE, s = 2, one 16/40
label dropped. C5: every count below is over its population.

WHAT IT FOUND
-------------
THE SET-VALUED SWAP IS THE WHOLE RESCUE AT EVERY CLEAN VECTOR (P2 holds,
K-B silent): multi-clean equals above-clean at 183 / 105 / 29 / 11 on the
four arms -- every optimum abandoning an above-level atom at a clean
vector has a serving optimum it dominates on the partners, so the
exchange behind the clean set is a prefix-preserving swap of some size at
every one of them (rule at the count; the exchange proved). The 21 clean
vectors at 3/4 the lemma misses ALL sit at lightest mass 10/40 -- ZERO
SLACK -- 18 of them rescued by MULTI (each partner drops one label:
12 + 18 = 30 = 3 x 10) and the three (10, 15, 15) permutations by DEEP
(one 15/40 partner drops two), every rescue at s = 3. At four atoms the
(8, 8, 12, 12) permutations: at 3/4 all 8 abandoning optima per vector
rescued DEEP at s = 3 (one 12/40 partner drops two labels, 24 = 3 x 8);
at 7/10, 52 per vector, 32 single at s = 1 (the twin), 16 deep and 4
multi at s = 3.

P3 HALF-REFUTED: the exchange P3 named -- the two 12/40 partners
dropping one each -- exists at 7/10 (4 per vector) and NOT at 3/4, where
every rescue the lemma misses is the deep one; and it takes s = 3, never
2, the mass equality forcing it.

THE STRONG FORM DIES AT THE FAILING VECTORS (P4 refuted; K-C): GAIN cases
2,604 / 2,142 / 4,536 / 6,120 -- but every one at a vector that FAILS
above, at lightest mass 6/40 and under at three atoms (3/4 and 7/10
alike) and 5/40 and under at four, none at any clean vector. The
exhibit: masses (1, 18, 21), rows (6, 2, 2), (6, 2, 2), (4, 3, 3) at 3/4,
tau 3, optima (0, 1, 3) and (3, 2, 2) -- the serving optimum GAINS the
middle atom's second label while dropping the heavy atom's third (21
dropped for 3 + 18 added), a three-atom rearrangement no drop-set
reaches. So below the clean band the rescue can need a partner to grow,
and the dominated exchange is the clean band's shape, not the grid's
(observation on the designed sweep).

THE FULL-PARTNER EXCHANGE (property; derived after the first run, asserted
in the second at every cell of every arm). Dropping the lowest d labels
of a partner that R serves FULLY loses coverage at most a d / k: the
lowest d of k posteriors average at most 1/k. So for any drop-set S over
fully served partners with sum_S a_i d_i = k w_r, the exchange at s = k
loses at most w_r of coverage and gains w_r top_k(r) = w_r, and its cost
is opt: it is an optimum serving r, with NO coverage condition -- mass
conservation is the only hypothesis, a subset-sum on the full partners.
Asserted at 912 / 450 / 12,076 / 17,268 firings, never tripped. At zero
slack (w_min = 1 - T) the rest's untaken coverage is zero, so with every
posterior POSITIVE -- as on every menu here; a zero label can sit untaken
at no coverage -- every partner of an abandoning optimum is full, and
at 3/4 with three atoms the partners' masses sum to 30/40 = 3 w_min, so
"one label off each" conserves mass at every such vector: THE ZERO-SLACK
ROW IS A THEOREM -- every abandoning optimum at every vector of lightest
mass 10/40 at 3/4 is rescued, 180 of 180 by this exchange, 30 of 30
vectors clean, the lemma reaching 9 of them. The general zero-slack
statement is the subset-sum sum_S a_i d_i = k w_min with d_i in 0..k over
the partners; at 7/10 zero slack is 12/40, where no optimum abandons.

WHAT THIS LEAVES OPEN: the grading in the slack above zero -- at sigma > 0
a partner may be partial and its dropped label sits above the row's
mean, so the coverage condition returns; whether it can be bounded by
the slack (dropped coverage <= w_r top_s(r) + D_R with D_R <= sigma) into
a threshold is the closed form still owed. And the GAIN cases' own
lemma, if one exists: the exhibit's exchange trades one heavy label for a
light row plus a middle label, and its shape is unread. (Settled later
by explore_ruler_gain.py: every serving optimum is this exchange with
SIGNED mass conservation, and below the clean band the dominated one is
absent mostly because no drop-set has the mass -- the arithmetic
obstruction; the slack threshold stays owed.)
"""

import itertools
import os
import sys
import time
from fractions import Fraction

os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from explore_ruler_excess import (  # noqa: E402
    K, MENUS_OLD, WD, compositions, int_menu, score_cell, vec_gcd)
from explore_ruler_swap import swaps_for  # noqa: E402

F = Fraction
REHEARSE = "--rehearse" in sys.argv
SHAPES = ("single", "deep", "multi")


# ------------------------------------------------- the set-valued swap

def dominated_rescues(weights, opt_r, arg, r):
    """Every optimum serving r that opt_r dominates on the partners, with
    its shape and s. Asserts mass conservation (P1 / K-A)."""
    m = len(weights)
    out = []
    for o in arg:
        if o[r] == 0:
            continue
        if any(o[i] > opt_r[i] for i in range(m) if i != r):
            continue
        drops = [(i, opt_r[i] - o[i]) for i in range(m)
                 if i != r and opt_r[i] > o[i]]
        dropped = sum(weights[i] * d for i, d in drops)
        assert dropped == o[r] * weights[r], "K-A: mass not conserved"
        if len(drops) >= 2:
            shape = "multi"
        elif drops[0][1] == 1:
            shape = "single"
        else:
            shape = "deep"
        out.append((shape, o[r], drops, o))
    return out


def full_partner_drops(weights, tops, tt, opt, R, r):
    """THE FULL-PARTNER EXCHANGE, checked: every drop-set over the partners
    R serves FULLY (depths 0..K each) whose dropped mass is K w_r is
    asserted to yield a covering rule at the optimum cost, so it is an
    optimum serving r fully. Returns the number of such drop-sets."""
    m = len(weights)
    full = [i for i in range(m) if i != r and R[i] == K]
    n = 0
    for ds in itertools.product(range(K + 1), repeat=len(full)):
        if sum(weights[i] * d for i, d in zip(full, ds)) != K * weights[r]:
            continue
        if not any(ds):
            continue
        new = list(R)
        for i, d in zip(full, ds):
            new[i] -= d
        new[r] = K
        cov = sum(weights[i] * tops[i][new[i]] for i in range(m))
        cost = sum(weights[i] * new[i] for i in range(m))
        assert cost == opt and cov >= tt, "full-partner exchange misfires"
        n += 1
    return n


def read_cell(weights, rows, pd, tt):
    """Score a cell; at every above-level atom with an abandoning optimum,
    read each such optimum through the lemma and through the set-valued
    swap. Returns the scorer's result and per-optimum records
    (r, lemma_fired, best_shape or 'gain' or 'forced', s)."""
    res = score_cell(weights, rows, pd, tt)
    tau, opt, arg, tops = res["tau"], res["opt"], res["arg"], res["tops"]
    m = len(weights)
    records = []
    for r in range(m):
        if max(rows[r]) <= tau:
            continue
        aband = [s for s in arg if s[r] == 0]
        if not aband:
            continue
        serving = [s for s in arg if s[r] > 0]
        for R in aband:
            cov = sum(weights[i] * tops[i][R[i]] for i in range(m))
            fired, _ = swaps_for(weights, rows, tops, tt, opt, R, r, cov - tt)
            dom = dominated_rescues(weights, R, arg, r)
            nfull = full_partner_drops(weights, tops, tt, opt, R, r)
            # the full-partner exchange is a dominated rescue at s = K.
            assert nfull == 0 or any(d[1] == K for d in dom), "full-partner"
            # C2: the lemma is exactly the SINGLE shape.
            single = [d for d in dom if d[0] == "single"]
            assert bool(fired) == bool(single), "C2: lemma != single shape"
            if not serving:
                verdict, s = "forced", 0
            elif not dom:
                verdict, s = "gain", 0
            else:
                best = min(dom, key=lambda d: SHAPES.index(d[0]))
                verdict, s = best[0], best[1]
            records.append((r, bool(fired), verdict, s, dom, nfull))
    return res, records


# -------------------------------------------------------------- an arm

def run_arm(name, vectors, menus, target, m, record):
    t0 = time.time()
    keys = ("aband", "lemma", "single", "deep", "multi", "gain", "forced",
            "cells", "above_forced", "full")
    tally = {v: {k: 0 for k in keys} for v in vectors}
    s_by_shape = {v: {} for v in vectors}
    exhibit = None
    for tag, menu in menus:
        pd, mrows = int_menu(menu)
        tt = WD * pd * target
        assert tt.denominator == 1
        tt = int(tt)
        choices = list(itertools.product(range(len(mrows)), repeat=m))
        for v in vectors:
            t = tally[v]
            for ch in choices:
                rows = [mrows[i] for i in ch]
                res, recs = read_cell(v, rows, pd, tt)
                t["cells"] += 1
                t["above_forced"] += res["above_forced"]
                for r, fired, verdict, s, dom, nfull in recs:
                    t["aband"] += 1
                    t["full"] += nfull > 0
                    t["lemma"] += fired
                    t[verdict] += 1
                    if verdict == "gain" and exhibit is None:
                        exhibit = (tag, v, rows, res["tau"], res["arg"], r)
                    if verdict in SHAPES:
                        sb = s_by_shape[v].setdefault(verdict, {})
                        sb[s] = sb.get(s, 0) + 1
    above_clean = {v for v, t in tally.items() if t["above_forced"] == 0}
    swap_clean = {v for v, t in tally.items() if t["lemma"] == t["aband"]}
    multi_clean = {v for v, t in tally.items()
                   if t["single"] + t["deep"] + t["multi"] == t["aband"]}
    assert swap_clean <= multi_clean <= above_clean, "C3: containment"
    tot = {k: sum(t[k] for t in tally.values()) for k in keys}
    print("\n%s  [%d vectors, %d cells, %.1f s]"
          % (name, len(vectors), tot["cells"], time.time() - t0))
    print("  above-clean %d   swap-clean %d   multi-clean %d"
          % (len(above_clean), len(swap_clean), len(multi_clean)))
    print("  abandoning optima at above-level atoms %d: lemma-rescued %d;"
          " dominated rescue by shape single %d / deep %d / multi %d;"
          " GAIN %d; forced %d"
          % (tot["aband"], tot["lemma"], tot["single"], tot["deep"],
             tot["multi"], tot["gain"], tot["forced"]))
    print("  the full-partner exchange fires at %d abandoning optima (every"
          " firing asserted an optimum)" % tot["full"])
    if record is not None:
        sc, lr = record
        print("  C1 reproduction: swap-clean %d against the record's %d,"
              " lemma rescues %d against %d -- %s"
              % (len(swap_clean), sc, tot["lemma"], lr,
                 "EXACT" if (len(swap_clean), tot["lemma"]) == (sc, lr)
                 else "MISS"))
        assert (len(swap_clean), tot["lemma"]) == (sc, lr), "K-D"
    gain_clean = [v for v in above_clean if tally[v]["gain"]]
    print("  P2: multi-clean %s above-clean%s"
          % ("==" if multi_clean == above_clean else "!=",
             "" if not gain_clean else
             "  -- K-B: GAIN cases at %d above-clean vectors" % len(gain_clean)))
    print("  P4: GAIN cases over the whole grid %d%s"
          % (tot["gain"], "" if tot["gain"] == 0 else "  -- K-C"))
    if exhibit is not None:
        tag, v, rows, tau, arg, r = exhibit
        print("  first GAIN case: menu %s, masses %s, rows %s, tau %d,"
              " atom %d; optima %s"
              % (tag, fmt(v), rows, tau, r, arg))
    return tally, s_by_shape, above_clean, swap_clean, multi_clean


def by_key(label, vectors, tally, sets, keyf):
    above_clean, swap_clean, multi_clean = sets
    print("  %s" % label)
    print("      key    n   above-clean   swap-clean   multi-clean"
          "   abandoning   single    deep   multi    gain   forced"
          "   full")
    by = {}
    for v in vectors:
        by.setdefault(keyf(v), []).append(v)
    for k in sorted(by):
        vs = by[k]
        s = {q: sum(tally[v][q] for v in vs)
             for q in ("aband", "single", "deep", "multi", "gain", "forced",
                       "full")}
        print("    %5s %4d   %11d   %10d   %11d   %10d   %6d   %5d   %5d"
              "   %5d   %6d   %5d"
              % (k, len(vs), sum(v in above_clean for v in vs),
                 sum(v in swap_clean for v in vs),
                 sum(v in multi_clean for v in vs), s["aband"],
                 s["single"], s["deep"], s["multi"], s["gain"], s["forced"],
                 s["full"]))


def fmt(v):
    return "(" + ", ".join("%d/%d" % (a, WD) for a in v) + ")"


def s_line(sb):
    return "; ".join("%s: %s" % (sh, ", ".join("s=%d x%d" % (s, n)
                                                for s, n in sorted(
                                                    sb[sh].items())))
                     for sh in SHAPES if sh in sb) or "none"


# ---------------------------------------------------------- the controls

def hand_cell():
    """C4: the swap rig's hand cell read through the set-valued swap."""
    weights = (8, 16, 16)
    rows = [(7, 7, 6), (11, 7, 2), (8, 6, 6)]
    pd, tt = 20, 600
    res, recs = read_cell(weights, rows, pd, tt)
    print("C4 hand cell: tau %d  OPT %s  optima %s"
          % (res["tau"], F(res["opt"], WD), res["arg"]))
    assert res["tau"] == 6 and F(res["opt"], WD) == 2
    hit = [rec for rec in recs if rec[0] == 0]
    assert len(hit) == 1 and hit[0][1] and hit[0][2] == "single" \
        and hit[0][3] == 2, hit
    doms = hit[0][4]
    print("  optimum (0, 2, 3): dominated serving optima %s"
          % [(sh, s, dr, o) for sh, s, dr, o in doms])
    assert any(o == (2, 2, 2) and sh == "single" and dr == [(2, 1)]
               for sh, s, dr, o in doms)
    print("  -- the hand cell reproduces: (2, 2, 2) dominates, shape"
          " SINGLE, 16/40 dropped for s = 2.")


def main():
    t0 = time.time()
    print("explore_ruler_multiswap.py -- the set-valued swap%s"
          % (" (REHEARSAL)" if REHEARSE else ""))
    hand_cell()

    grid3 = list(compositions(WD, 3))
    assert len(grid3) == 741
    grid4 = [v for v in compositions(WD, 4) if vec_gcd(v) >= 4]
    tenths = sorted(set(itertools.permutations((8, 8, 12, 12))))
    if REHEARSE:
        reps = [(8, 8, 24), (8, 16, 16), (10, 10, 20), (7, 16, 17),
                (5, 5, 30), (8, 15, 17), (13, 13, 14), (2, 3, 35)]
        grid3 = sorted({p for r in reps for p in itertools.permutations(r)})
        grid4 = sorted({v for v in grid4 if vec_gcd(v) >= 8} | set(tenths))
        menus = MENUS_OLD[:1]
        records = {}
    else:
        menus = MENUS_OLD
        records = {"3A": (162, 4800), "3B": (105, 6390),
                   "4A": (23, 53248), "4B": (5, 87288)}

    for name, grid, target, m in (("3A", grid3, F(3, 4), 3),
                                  ("3B", grid3, F(7, 10), 3),
                                  ("4A", grid4, F(3, 4), 4),
                                  ("4B", grid4, F(7, 10), 4)):
        tally, sbs, above, swap, multi = run_arm(
            "ARM %s -- menus %s, %d atoms, coverage %s"
            % (name, "".join(t for t, _ in menus), m, target),
            grid, menus, target, m, records.get(name))
        sets = (above, swap, multi)
        print("  sigma = 1 - w_min - T = %d/40 - w_min" % (WD - int(WD * target)))
        by_key("by lightest mass w_min", grid, tally, sets, min)
        if m == 3:
            by_key("by gcd stratum", grid, tally, sets, vec_gcd)
        missed = sorted(v for v in above if v not in swap)
        print("  above-clean vectors the lemma misses: %d" % len(missed))
        for v in missed:
            t = tally[v]
            print("    %s  w_min %d  abandoning %d  lemma %d  shapes %s%s"
                  % (fmt(v), min(v), t["aband"], t["lemma"], s_line(sbs[v]),
                     "  GAIN %d" % t["gain"] if t["gain"] else ""))
        if m == 4:
            print("  P3 -- the (8, 8, 12, 12) permutations:")
            for v in tenths:
                t = tally[v]
                print("    %s  abandoning %d  lemma %d  %s  -- %s"
                      % (fmt(v), t["aband"], t["lemma"], s_line(sbs[v]),
                         "multi-clean" if v in multi else "NOT multi-clean"))
    print("\ntotal wall %.1f s" % (time.time() - t0))


if __name__ == "__main__":
    main()
