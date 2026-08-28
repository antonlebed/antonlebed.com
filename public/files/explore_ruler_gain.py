"""WHAT IS THE GAIN EXCHANGE -- THE RESCUE THAT TAKES MORE OF A PARTNER?
The signed mass-conserving exchange, and the arithmetic that forces it.

(The menus, the grid and the integer scorer are IMPORTED from
explore_ruler_excess.py and the dominated reader from
explore_ruler_multiswap.py, so every cell, every optimum and every
dominated rescue here is the record's. New here is the reading of the
serving optima the dominated exchange does NOT reach -- the GAIN cases --
as exchanges of their own, and the predicate that decides when no
dominated exchange could have existed.)

THE QUESTION
------------
explore_ruler_multiswap.py proved the set-valued swap: an optimum R
abandoning an atom r is rescued by a serving optimum it DOMINATES on the
partners iff a drop-set over the partners conserves mass (sum w_i d_i =
s w_r) and loses coverage at most w_r top_s(r) + D_R. That is the whole
rescue at every clean vector, and below the clean band it fails: 2,604 /
2,142 / 4,536 / 6,120 abandoning optima on the four arms have a serving
optimum but none dominated -- every serving optimum GAINS a label on some
partner. The exhibit: masses (1, 18, 21), rows (6, 2, 2), (6, 2, 2),
(4, 3, 3), target 3/4, tau 3, optima (0, 1, 3) and (3, 2, 2). This file
asks what exchange those serving optima are, and WHY the dominated one is
absent there: because the coverage condition fails, or because no drop-set
has the mass at all.

THE DERIVATION, worked on paper before any engine code
------------------------------------------------------
Symbols as in explore_ruler_excess.py: M atoms with masses w_r (numerators
over 40) summing to 1, posterior rows over k = 3 labels, a rule taking the
top s_r labels at each atom at cost sum w_r s_r and coverage
sum w_r top_s(r); the target T; an optimum a cheapest rule covering T;
D_R = cov(R) - T its overshoot. R abandons r (R_r = 0).

  THE GAIN EXCHANGE (property). Any rule R' with R'_r = s > 0 is R with a
  prefix of depth d_i = R_i - R'_i dropped on the partners S where R' is
  lower, a prefix of depth g_j = R'_j - R_j ADDED on the partners G where
  it is higher, and r's top s labels added. Its cost is
  opt - sum_S w_i d_i + sum_G w_j g_j + s w_r, so R' is an optimum iff

      sum_S w_i d_i - sum_G w_j g_j = s w_r    (SIGNED mass conservation)

  and  sum_S (dropped coverage) <= w_r top_s(r) + sum_G (gained coverage) + D_R.

  The equality is the set-valued swap's by the same optimality argument
  (a cheaper covering rule cannot exist; a dearer one is not an optimum),
  with the gained mass on the other side. So EVERY serving optimum is one
  such exchange, the dominated ones being the case G empty, and the swap
  lemma the case of one partner, depth 1, G empty. The exhibit:
  21 x 1 - 18 x 1 = 3 x 1, and 21 x 3 = 63 <= 1 x 10 + 18 x 2 + 18 = 64.

  THE ARITHMETIC OBSTRUCTION (property). A dominated rescue drops
  d_i <= R_i labels on partners with sum w_i d_i = s w_r for some s in
  1..k. Call R NO-DROP when no such depth-capped drop-set exists for any
  s. Then no dominated rescue exists, so every rescue of a NO-DROP
  abandoning optimum is a gain case -- forced by the masses alone, before
  any coverage is read. The exhibit is NO-DROP: 18 d_1 + 21 d_2 in
  {1, 2, 3} has no solution. The other kind of gain case -- some drop-set
  conserves mass and every one loses too much coverage -- is COVERAGE-
  driven; the two kinds partition the gain cases, and which kind fills
  the band below the clean vectors is the count this file owns.

  THREE ATOMS (property). With r abandoned there are two partners. Both
  dropping is a dominated exchange; both gaining cannot pay for s w_r > 0;
  so every gain exchange at three atoms is ONE dropper (mass A, depth d)
  and ONE gainer (mass B, depth g) with A d = s w_r + B g -- the smallest
  gain lemma's whole shape, and at depths (1, 1) the dropper is strictly
  heavier than the gainer, A = s w_r + B > B.

  WHAT A GAIN BUYS. A drop on a FULLY served partner loses at most
  w_i d_i / k of coverage (the lowest d of k posteriors average at most
  1/k), which is what made the full-partner exchange coverage-free. A
  gained label is the largest posterior the partner's row has left, at
  or above the row's remaining mean and bounded by 1/k in neither
  direction, so no rate comparison between a gain and a full drop holds
  in general; no coverage-free corollary of the gain exchange is derived
  here, and none is predicted.

WHOSE VOCABULARY
----------------
explore_ruler_excess.py's, explore_ruler_swap.py's and
explore_ruler_multiswap.py's throughout -- ATOM, LEVEL, OPTIMUM, OVERSHOOT,
ABOVE half, FORCED, ABANDONING, RESCUED, DOMINATED rescue and its three
SHAPES, GAIN case, LIGHTEST MASS w_min. New here: NO-DROP (no depth-capped
drop-set over the served partners reaches s w_r for any s); a gain case's
KIND -- ARITHMETIC (NO-DROP) or COVERAGE (a drop-set conserves mass and
every one fails coverage); the DEPTH PROFILE (d, g, s) of a gain exchange.

THE ARMS
--------
  3A  menus A-E, three atoms, 3/4     3B  menus A-E, three atoms, 7/10
  4A  menus A-E, four atoms (gcd >= 4), 3/4     4B  the same at 7/10

THE PREDICTIONS, frozen before the engine
-----------------------------------------
P1  SIGNED CONSERVATION: at every serving optimum of every abandoning
    optimum, dropped mass minus gained mass equals s w_r (asserted; a
    derivation).
P2  THE OBSTRUCTION: at every NO-DROP abandoning optimum the dominated
    reader returns nothing (asserted; a derivation).
P3  THREE ATOMS: every gain exchange on 3A and 3B has exactly one dropper
    and one gainer, and at depths (1, 1) the dropper is the heavier
    (asserted; derivations).
P4  THE KIND SPLIT: on the three-atom arms the ARITHMETIC kind is the
    majority of gain cases (over half on each of 3A and 3B), the gcd-1
    light atoms sitting under every partner's mass; on the four-atom arms
    (masses multiples of 4, so some partner of mass 4, 8 or 12 nearly
    always drops to s w_r exactly) it is a small minority, under a tenth
    on each of 4A and 4B.

KILLS, as observables
---------------------
K-A  The signed-conservation assertion trips.
K-B  A NO-DROP abandoning optimum prints a dominated rescue.
K-C  A three-atom gain exchange prints two droppers, two gainers, or a
     lighter dropper at depths (1, 1).
K-D  The reproduction prints anything but GAIN 2,604 / 2,142 / 4,536 /
     6,120 and multi-clean 183 / 105 / 29 / 11.
K-E  An arithmetic share at or under one half on a three-atom arm, or at
     or over one tenth on a four-atom arm.

THE CONTROLS, read before any verdict
-------------------------------------
C1  REPRODUCTION: the record's GAIN and multi-clean counts on all four
    arms, exactly (K-D).
C2  THE EXHIBIT as a hand cell -- masses (1, 18, 21), rows (6, 2, 2),
    (6, 2, 2), (4, 3, 3), coverage 3/4 -- prints tau 3, optima (0, 1, 3)
    and (3, 2, 2), the abandoning optimum NO-DROP, kind ARITHMETIC, its
    one exchange dropping one label of the 21/40 atom and gaining one on
    the 18/40 atom at s = 3.
C3  DOMINATED IMPLIES A DROP-SET: wherever the dominated reader fires, the
    NO-DROP predicate is false (asserted; the contrapositive of P2, read
    at every dominated rescue rather than only at the gain cases).
C4  DENOMINATORS: every share prints over its gain-case population; a
    stratum with none prints as such.

THE READINGS -- read, not predicted
-----------------------------------
Per arm: the gain cases by kind and by lightest mass; the depth profile
(d, g, s) of every gain exchange and how many gain cases the exhibit's
own shape -- depths (1, 1), s = 3 -- rescues; the s taken by the light
atom.

RESOURCES
---------
Integers throughout, no numpy; the scorer is the excess rig's, the
dominated reader the multiswap rig's. Two arity-3 arms of 463,125 cells
and two arity-4 arms of 371,875; the new reading is a scan over the
serving optima at cells with abandonment plus a depth-capped subset-sum
over at most three partners. Estimated 100 s wall-clock and a few tens of
MB, under the memory watch. Rehearsed first (--rehearse) on the exhibit's
vector, the swap rig's handful and one menu per arm, exercising every
arm, every assertion and every print.

WHAT RAN
--------
Rehearsed (0.9 s, every assertion live, the exhibit reproduced), then
one full run at 70.1 s wall under the memory watch, peak 14.8 MB.
Integers throughout.

EVERY CONTROL PASSES. C1: GAIN 2,604 / 2,142 / 4,536 / 6,120 and
multi-clean 183 / 105 / 29 / 11, EXACT on all four arms. C2: the exhibit
prints tau 3, opt 81/40, optima (0, 1, 3) and (3, 2, 2), the abandoning
optimum NO-DROP and ARITHMETIC, its one exchange dropping one label of
21/40 and gaining one of 18/40 at s = 3. C3 and P2 together: NO-DROP and
a dominated rescue never met, asserted at 104,241 + 115,467 + 60,496 +
100,656 abandoning optima. C4: every share below is over its population.

WHAT IT FOUND
-------------
THE GAIN EXCHANGE IS THE WHOLE RESCUE (P1 holds, K-A silent): every
serving optimum of every abandoning optimum on every arm decomposes as
drops, gains and r's top s labels with dropped mass minus gained mass
equal to s w_r exactly, and the coverage condition holds at each -- the
property asserted at every serving optimum of the sweep. At three atoms
every gain exchange is one dropper and one gainer, the dropper heavier
at depths (1, 1) (P3 holds, K-C silent).

THE KIND SPLIT (P4 holds, K-E silent). Three atoms: ARITHMETIC 2,226 of
2,604 (85.5%) at 3/4 and 1,914 of 2,142 (89.4%) at 7/10 -- the dominated
exchange is absent below the clean band because NO drop-set over the
served partners has the mass s w_r, not because one loses too much
coverage. The COVERAGE kind sits at lightest mass 4/40 and 5/40 ONLY, on
both targets (186 + 192 at 3/4, 108 + 120 at 7/10) -- there a partner of
mass 8 or 12, or 10 or 15, carries the light atom's multiple and every
such drop-set fails on coverage; at 1, 2, 3 and 6 every gain case is
arithmetic and at 7 and above there are none, which is the sweep's
reading and not a derivation (a partner of mass 2 carries 1's multiple
and one of 18 carries 6's, and the sweep holds no coverage case at
either). Four atoms (gcd >= 4): ARITHMETIC 0 of 4,536 at 3/4 and 144 of
6,120 (2.4%) at 7/10 -- three partners of the shared divisor summing to
36 or 35 cannot all sit above 12 or 15, so a partner of mass 4, 8 or 12
(5, 10 or 15 at lightest mass 5) always exists, and the 144 are the one
way it fails to drop: that partner is abandoned by R too, so it holds
nothing to drop.

THE DEPTH PROFILES (a reading). Every drop is one label but a few
hundred exchanges per arm: depth 2 at 84 / 90 / 384 / 24, and two
droppers only at four atoms, 48 and 24. The exhibit's own shape -- one
dropped, one gained, s = 3 -- holds at 804 of 2,604 and 402 of 2,142 gain
cases at three atoms and 2,340 of 4,536 and 2,232 of 6,120 at four: the
commonest single shape at four atoms (3,408 and 2,544 exchanges) and
second at three to the one-label exchange at s = 1 (900 and 1,098
exchanges against 804 and 402). The light atom takes every s: at three
atoms s = 1 alone at 954 and 1,236 gain cases, s = 3 alone at 1,152 and
474.

WHAT THIS LEAVES OPEN: the coverage kind's own threshold -- at lightest
mass 4 and 5 a drop-set conserves mass and every one fails coverage, and
whether the slack bounds that failure into a closed condition is the
same question the dominated exchange left at sigma > 0; and the
collapse, which takes every stratum at once.

THE DESIGN
----------
read_cell scores a cell, and at every above-level atom with an abandoning
optimum reads each such optimum: the dominated rescues (the multiswap
reader, which asserts its own conservation), every serving optimum
decomposed as a gain exchange with signed conservation asserted, the
NO-DROP predicate, and the verdict -- forced / dominated / gain, a gain
case carrying its kind and its exchanges' depth profiles. run_arm tallies
per vector; the arm prints the reproduction, the kind split, the
lightest-mass table and the depth profiles.
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
from explore_ruler_multiswap import dominated_rescues  # noqa: E402

F = Fraction
REHEARSE = "--rehearse" in sys.argv


# ----------------------------------------------------- the gain exchange

def exchange_of(weights, tops, tt, opt, R, o, r):
    """The serving optimum o read as an exchange from R: the drop-set, the
    gain-set and s. Asserts signed mass conservation (P1 / K-A) and the
    coverage condition."""
    m = len(weights)
    s = o[r]
    drops = [(i, R[i] - o[i]) for i in range(m) if i != r and o[i] < R[i]]
    gains = [(j, o[j] - R[j]) for j in range(m) if j != r and o[j] > R[j]]
    dropped = sum(weights[i] * d for i, d in drops)
    gained = sum(weights[j] * g for j, g in gains)
    assert dropped - gained == s * weights[r], "K-A: signed conservation"
    cov_r = sum(weights[i] * tops[i][R[i]] for i in range(m))
    lost = sum(weights[i] * (tops[i][R[i]] - tops[i][R[i] - d])
               for i, d in drops)
    won = sum(weights[j] * (tops[j][R[j] + g] - tops[j][R[j]])
              for j, g in gains)
    assert lost <= weights[r] * tops[r][s] + won + (cov_r - tt), "coverage"
    return drops, gains, s


def no_drop(weights, R, r):
    """NO-DROP: no depth-capped drop-set over the partners R serves reaches
    s w_r for any s in 1..K."""
    m = len(weights)
    partners = [i for i in range(m) if i != r and R[i] > 0]
    reach = {0}
    for i in partners:
        reach |= {x + weights[i] * d for x in reach for d in range(R[i] + 1)}
    return not any(s * weights[r] in reach for s in range(1, K + 1))


def read_cell(weights, rows, pd, tt):
    """Score a cell; at every above-level atom with an abandoning optimum,
    read each such optimum. Returns the scorer's result and per-optimum
    records (r, verdict, kind, exchanges) with verdict in forced /
    dominated / gain, kind in arithmetic / coverage / None, and exchanges
    the list of (drops, gains, s) over the serving optima."""
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
            dom = dominated_rescues(weights, R, arg, r)
            nd = no_drop(weights, R, r)
            # P2 / K-B and C3: NO-DROP and a dominated rescue exclude.
            assert not (nd and dom), "K-B: NO-DROP with a dominated rescue"
            exch = [exchange_of(weights, tops, tt, opt, R, o, r)
                    for o in serving]
            if not serving:
                verdict, kind = "forced", None
            elif dom:
                verdict, kind = "dominated", None
            else:
                verdict = "gain"
                kind = "arithmetic" if nd else "coverage"
                if m == 3:
                    for drops, gains, s in exch:
                        # P3 / K-C: one dropper, one gainer.
                        assert len(drops) == 1 and len(gains) == 1, \
                            "K-C: shape at three atoms"
                        (i, d), (j, g) = drops[0], gains[0]
                        if d == 1 and g == 1:
                            assert weights[i] > weights[j], "K-C: heavier"
            records.append((r, verdict, kind, exch))
    return res, records


# -------------------------------------------------------------- an arm

def profile(drops, gains, s):
    return (tuple(sorted(d for _, d in drops)),
            tuple(sorted(g for _, g in gains)), s)


def run_arm(name, vectors, menus, target, m, record):
    t0 = time.time()
    keys = ("aband", "dominated", "gain", "forced", "arithmetic",
            "coverage", "cells", "above_forced")
    tally = {v: {k: 0 for k in keys} for v in vectors}
    profiles = {}          # (d-profile, g-profile, s) -> exchanges
    s_taken = {}           # s -> gain cases whose every exchange takes s
    exhibit_shape = 0      # gain cases some exchange of which is (1),(1),3
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
                for r, verdict, kind, exch in recs:
                    t["aband"] += 1
                    t[verdict] += 1
                    if verdict != "gain":
                        continue
                    t[kind] += 1
                    ss = set()
                    shape = False
                    for drops, gains, s in exch:
                        p = profile(drops, gains, s)
                        profiles[p] = profiles.get(p, 0) + 1
                        ss.add(s)
                        shape |= p == ((1,), (1,), K)
                    exhibit_shape += shape
                    key = tuple(sorted(ss))
                    s_taken[key] = s_taken.get(key, 0) + 1
    above_clean = {v for v, t in tally.items() if t["above_forced"] == 0}
    multi_clean = {v for v, t in tally.items()
                   if t["dominated"] == t["aband"]}
    tot = {k: sum(t[k] for t in tally.values()) for k in keys}
    print("\n%s  [%d vectors, %d cells, %.1f s]"
          % (name, len(vectors), tot["cells"], time.time() - t0))
    print("  above-clean %d   multi-clean %d" % (len(above_clean),
                                                 len(multi_clean)))
    print("  abandoning optima at above-level atoms %d: dominated %d;"
          " GAIN %d; forced %d"
          % (tot["aband"], tot["dominated"], tot["gain"], tot["forced"]))
    if record is not None:
        gc, mc = record
        ok = (tot["gain"], len(multi_clean)) == (gc, mc)
        print("  C1 reproduction: GAIN %d against the record's %d,"
              " multi-clean %d against %d -- %s"
              % (tot["gain"], gc, len(multi_clean), mc,
                 "EXACT" if ok else "MISS"))
        assert ok, "K-D"
    g = tot["gain"]
    if g:
        share = F(tot["arithmetic"], g)
        print("  P4 kind split: ARITHMETIC %d (%.1f%%) / COVERAGE %d of %d"
              " gain cases%s"
              % (tot["arithmetic"], 100 * float(share), tot["coverage"], g,
                 "" if (share > F(1, 2) if m == 3 else share < F(1, 10))
                 else "  -- K-E"))
    else:
        print("  P4: no gain cases on this arm")
    print("  by lightest mass w_min: gain cases, arithmetic / coverage,"
          " over abandoning optima")
    by = {}
    for v in vectors:
        by.setdefault(min(v), []).append(v)
    for k in sorted(by):
        vs = by[k]
        s = {q: sum(tally[v][q] for v in vs)
             for q in ("aband", "gain", "arithmetic", "coverage", "forced")}
        if s["gain"] == 0 and s["forced"] == 0:
            continue
        print("    %2d/40  %4d vectors  abandoning %6d  gain %5d ="
              " %5d + %5d   forced %6d"
              % (k, len(vs), s["aband"], s["gain"], s["arithmetic"],
                 s["coverage"], s["forced"]))
    print("  the light atom's s over gain cases (every exchange's s):")
    for key in sorted(s_taken):
        print("    s in %s: %d" % (key, s_taken[key]))
    print("  depth profiles (drops, gains, s) over gain exchanges:")
    for p in sorted(profiles, key=lambda q: (-profiles[q], q)):
        print("    drops %s gains %s s=%d: %d" % (p[0], p[1], p[2],
                                                    profiles[p]))
    print("  gain cases holding the exhibit's shape (one label dropped, one"
          " gained, s = %d): %d of %d" % (K, exhibit_shape, g))
    return tally


def fmt(v):
    return "(" + ", ".join("%d/%d" % (a, WD) for a in v) + ")"


# ---------------------------------------------------------- the controls

def hand_cell():
    """C2: the multiswap rig's exhibit read as a gain exchange."""
    weights = (1, 18, 21)
    rows = [(6, 2, 2), (6, 2, 2), (4, 3, 3)]
    pd, tt = 10, 300
    res, recs = read_cell(weights, rows, pd, tt)
    print("C2 exhibit: tau %d  OPT %s  optima %s"
          % (res["tau"], F(res["opt"], WD), res["arg"]))
    assert res["tau"] == 3 and res["opt"] == 81
    assert sorted(res["arg"]) == [(0, 1, 3), (3, 2, 2)]
    hit = [rec for rec in recs if rec[0] == 0]
    assert len(hit) == 1, hit
    r, verdict, kind, exch = hit[0]
    print("  optimum (0, 1, 3): verdict %s, kind %s, exchanges %s"
          % (verdict, kind, exch))
    assert verdict == "gain" and kind == "arithmetic"
    assert no_drop(weights, (0, 1, 3), 0)
    assert exch == [([(2, 1)], [(1, 1)], 3)], exch
    print("  -- the exhibit reproduces: NO-DROP, one label of 21/40 dropped,"
          " one of 18/40 gained, s = 3.")


def main():
    t0 = time.time()
    print("explore_ruler_gain.py -- the gain exchange%s"
          % (" (REHEARSAL)" if REHEARSE else ""))
    hand_cell()

    grid3 = list(compositions(WD, 3))
    assert len(grid3) == 741
    grid4 = [v for v in compositions(WD, 4) if vec_gcd(v) >= 4]
    if REHEARSE:
        reps = [(1, 18, 21), (8, 8, 24), (8, 16, 16), (10, 10, 20),
                (7, 16, 17), (5, 5, 30), (6, 17, 17), (2, 3, 35)]
        grid3 = sorted({p for r in reps for p in itertools.permutations(r)})
        grid4 = sorted({v for v in grid4 if vec_gcd(v) >= 8}
                       | {(4, 4, 16, 16), (4, 8, 12, 16), (4, 12, 12, 12)})
        menus = MENUS_OLD[:1]
        records = None
    else:
        menus = MENUS_OLD
        records = {"3A": (2604, 183), "3B": (2142, 105),
                   "4A": (4536, 29), "4B": (6120, 11)}

    for name, grid, target, m in (("3A", grid3, F(3, 4), 3),
                                  ("3B", grid3, F(7, 10), 3),
                                  ("4A", grid4, F(3, 4), 4),
                                  ("4B", grid4, F(7, 10), 4)):
        tally = run_arm(
            "ARM %s -- menus %s, %d atoms, coverage %s"
            % (name, "".join(t for t, _ in menus), m, target),
            grid, menus, target, m, records[name] if records else None)
        del tally
    print("\ntotal wall %.1f s" % (time.time() - t0))


if __name__ == "__main__":
    main()
