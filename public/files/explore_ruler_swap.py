"""WHY DOES NO OPTIMUM ABANDON AN ABOVE-LEVEL ATOM AT A COARSE WEIGHT VECTOR?
The feasibility bound, the swap lemma, and the lightest mass as the variable.

(The menus are IMPORTED from explore_ruler_abandon.py, explore_ruler_family.py
and explore_ruler_box.py and the integer scorer from explore_ruler_excess.py,
so every cell and every optimum here is the record's. New here is one
exchange -- the SWAP -- and the reading of the whole grid by its lightest
mass rather than by its gcd.)

THE QUESTION
------------
On the first menu family at coverage 3/4 and 7/10, the nine fortieth weight
vectors whose numerators share a divisor of 8 or 10 (fifths and quarters)
take no forced failure: no optimum abandons an atom whose best posterior sits
above the operative level. The below half of that law is vacuous by a mass
bound (an atom wholly under the level weighs at most 1 - T/s_max, and no
fifths or quarters atom is that light). The above half is open: certificate
optimality is dead as its mechanism (the coarse certificates fail at 34 to
108 of 625 cells), tie multiplicity is dead, both certificate criteria clear
nothing. This file asks whether the above half is ALSO a mass bound, and
whether the gcd was ever the variable.

THE DERIVATION, worked on paper before any engine code
------------------------------------------------------
Symbols as in explore_ruler_excess.py: a cell has M atoms r with masses w_r
summing to 1 and posterior rows p(y|r) over k = 3 labels; a rule takes the
top s_r labels at each atom, costing w_r s_r and covering w_r top_s(r), top_s
the sum of the s largest posteriors; the target is T; an optimum is a
cheapest rule covering at least T, and D_R = cov(R) - T is a rule's
overshoot. An atom is ABANDONED by a rule taking none of its labels, and
FORCED-abandoned when every optimum abandons it.

  THE FEASIBILITY BOUND (property). A rule abandoning r covers T from the
  other atoms alone, whose whole coverage is 1 - w_r. So

      an atom abandoned by ANY feasible rule has  w_r <= 1 - T.

  This is the mirror of the below half's bound 1 - T/s_max and is weaker
  than it (s_max <= 1). It does NOT decide the coarse vectors -- 8/40 and
  10/40 sit under 10/40 at 3/4 and 12/40 at 7/10 -- but it confines
  abandonment there to the LIGHTEST atom, since 16/40 and 20/40 sit above,
  and at 3/5 it admits the 16/40 atoms, where the fifths go 0 of 6 (the
  admission and the failure turn out not to sit on the same atom; P6).

  THE SLACK. With r abandoned, the rest's untaken coverage U satisfies
  U = (1 - w_r) - cov(R) <= 1 - w_r - T =: sigma, and D_R = sigma - U. In
  coverage units of 1/800: sigma is 40 at fifths and 0 at quarters at 3/4,
  80 and 40 at 7/10. So the rest holds every label whose coverage exceeds
  sigma; at quarters and 3/4 it holds every label it has.

  THE SWAP LEMMA (property). Let R be an optimum abandoning r, and let R
  hold a pair (r', y) -- its lowest taken label on r' is the one that
  matters, the rules being prefixes -- with, for some s in 1..k,

      s w_r <= w_r'    and    w_r' p(y|r') <= w_r top_s(r) + D_R.

  Then R minus (r', y) plus r's top s labels costs at most cost(R) and
  covers at least T, so it is an optimum, and it serves r. Hence r is not
  forced-abandoned. Contrapositive: a forced-abandoned atom has, in EVERY
  optimum, every pair on an atom at least as heavy too lumpy to trade for
  r's prefix plus the overshoot.

  WHAT THE LEMMA CLOSES ON PAPER. Quarters at 3/4: r = the 10/40 atom, the
  twin 10/40 atom holds its third label (sigma = 0), whose posterior is at
  most 6/20 on the first family while every row's top is at least 7/20 --
  so the s = 1 swap fires at every cell, and (10, 10, 20) and its
  permutations are clean above at 3/4 by derivation. Fifths, and 7/10,
  have sigma > 0, and a hand cell shows the s = 1 swap can fail where s = 2
  rescues: masses (8, 16, 16), rows (7, 7, 6), (11, 7, 2), (8, 6, 6) at
  3/4 -- tau = 6, optimum 80/40, the optimum (0, 2, 3) abandons r with
  D_R = 8; dropping the (8, 6, 6) atom's third label (96) for r's top label
  (56) misses, for r's top two (112) it lands on (2, 2, 2) at cost 80. So
  whether the lemma covers every cell is a COUNT, and this rig owns it.

  THE VARIABLE. Feasibility says nothing about the gcd: a vector whose
  lightest mass exceeds 1 - T has no abandonable atom at all and is clean
  above trivially -- 36 vectors at 3/4 (every part at least 11/40), 3 at
  7/10 -- almost all of gcd 1. Within the window the swap's two conditions
  read the lightest mass (the mass condition) and the slack 1 - w_min - T
  (the coverage condition), never a divisor. So the grid is read here by
  w_min crossed with gcd, and the coarse nine are compared with the gcd-1
  vectors sharing their lightest mass.

WHOSE VOCABULARY
----------------
explore_ruler_excess.py's throughout -- ATOM, LEVEL, OPTIMUM, OVERSHOOT,
ABOVE/BELOW half, FORCED and LOOSE failures (a loose failure: SOME optimum
breaks the split; forced: every one). New here: a SWAP is the exchange of
the lemma; an abandoning optimum is RESCUED when some swap fires; a vector
is SWAP-CLEAN at an arm when every abandoning optimum at every cell is
rescued -- by the lemma a swap-clean vector is forced-clean above. The
LIGHTEST MASS w_min of a vector is its least part.

THE ARMS
--------
  ARITY 3 (741 vectors x 125 row choices x 5 menus per arm):
    3A  menus A-E, 3/4      3B  menus A-E, 7/10     3C  menus A-E, 3/5
    3D  menus A-E, 1/2      3F  menus F-J, 7/10
  ARITY 4 (menus A-E, the strata of gcd >= 4: 119 vectors x 625 x 5):
    4A  3/4                 4B  7/10

THE PREDICTIONS, frozen before the engine
-----------------------------------------
P1  The feasibility bound holds at every abandoned atom of every optimum on
    every arm (asserted; a derivation).
P2  The nine coarse vectors are SWAP-CLEAN at 3A and 3B, and the five
    coarse arity-4 vectors at 4A and 4B: every abandoning optimum at every
    cell is rescued by one swap.
P3  Swap-clean is contained in forced-clean-above (asserted; a derivation)
    and covers at least three quarters of it at 3A and 3B.
P4  THE GCD WAS NEVER THE VARIABLE: at 3A, among the gcd-1 vectors whose
    lightest mass is 8 or 10, more than half are forced-clean above, and
    the share exceeds the gcd-1 bulk's.
P5  On 3F the three fifths vectors that fail do so on the swap's COVERAGE
    condition -- an atom at least as heavy holds a pair, and every such
    pair is too lumpy -- and never on the mass condition.
P6  At 3C the fifths' forced failures include an above-half failure at a
    16/40 atom, the atom the feasibility bound admits exactly there.

KILLS, as observables
---------------------
K-A  The feasibility-bound assertion trips.
K-B  A coarse vector prints an unrescued abandoning optimum at 3A or 3B.
K-C  The swap-clean set's share of the forced-clean-above set prints under
     one half at 3A.
K-D  The reproduction prints anything but 183 / 105 / 18 / 0 / 54 forced
     clean, or a non-zero above-forced count at a coarse vector at 3A/3B.

THE CONTROLS, read before any verdict
-------------------------------------
C1  REPRODUCTION: the record's five forced clean counts, exactly, and the
    coarse nine at zero forced failures at 3A and 3B.
C2  EVERY SWAP RE-SCORED: the rule a swap produces is asserted feasible and
    at the optimum cost, at every rescue.
C3  CONTAINMENT: swap-clean subset of forced-clean-above, per vector,
    asserted on every arm.
C4  THE HAND CELL: masses (8, 16, 16), rows (7, 7, 6), (11, 7, 2),
    (8, 6, 6), coverage 3/4 prints tau 6, optimum 80/40, the optimum
    (0, 2, 3) abandoning atom 0 with D_R = 8, rescued at s = 2 and not at
    s = 1.
C5  QUARTERS AT 3/4: every abandoning optimum at (10, 10, 20) and its
    permutations has D_R = 0 and the rest fully served (the slack is zero),
    and is rescued at s = 1 -- the paper derivation, asserted.
C6  DENOMINATORS: every rescue rate is printed over its abandoning-optimum
    population; a stratum with no abandonment prints as such.

RESOURCES
---------
Integers throughout, no numpy; the scorer is the excess rig's. Arity 3:
5 arms x 463,125 cells; arity 4: 2 arms x 371,875 cells. Estimated 2 to 3
minutes wall-clock and a few tens of MB. Rehearsed first (--rehearse) on a
permutation-closed handful of vectors and one menu per family, exercising
every arm, every assertion and every print.

WHAT RAN
--------
Rehearsed (0.8 s, every assertion live), then one full run at 106.9 s
wall under the memory watch, peak 16.1 MB: five arity-3 arms of 463,125
cells at 10 s each, two arity-4 arms of 371,875 cells at 28 s each. Two
readings were added after the rehearsal and before the full run: the
forced failures at a vector printed by the failing atom's mass, and C5
asserting that the twin's s = 1 swap is among the rescues. Integers
throughout.

EVERY CONTROL PASSES. C1: 183 / 105 / 18 / 0 / 54 forced clean, EXACT, and
the coarse nine at zero forced failures at 3A and 3B. C2: every rescue's
rule re-scored feasible at the optimum cost, at 4,800 + 6,390 + 8,073 +
7,608 + 9,246 + 53,248 + 87,288 rescues, never tripped. C3: swap-clean
inside above-clean on every arm. C4: the hand cell prints tau 6, optimum
2, optima (0, 2, 3), (2, 1, 3), (2, 2, 2), D_R 8 at (0, 2, 3), rescued at
s = 2 on either 16/40 atom and not at s = 1. C5: at the quarters at 3/4
every abandoning optimum has zero overshoot, the rest fully served, and
the twin's s = 1 swap fires. C6: every rate below is over its population.

WHAT IT FOUND
-------------
THE SWAP IS THE MECHANISM AT THE COARSE VECTORS (P2 holds, K-B silent).
At 3/4 and 7/10 on the first family, every optimum that abandons an
above-level atom at any of the nine coarse vectors is rescued by one swap
-- 48 / 0 / 26 abandoning optima per vector at 3/4 ((8, 16, 16) and its
permutations never abandon there), 80 / 44 / 38 at 7/10, all rescued --
and the same at the five coarse arity-4 vectors: 168 / 100 at 3/4, 717 /
444 at 7/10. The rescue never needs the mass condition relaxed: mass-fail
is 0 at every coarse vector on every arm but 1/2. So no optimum abandons
an above-level atom at a coarse vector BECAUSE the rest is within a slack
of full coverage and holds a pair a prefix of the light atom trades for
at no extra cost; a rule, the lemma proved and the count exhaustive.

THE FEASIBILITY BOUND HOLDS EVERYWHERE (P1; K-A silent) and it is NOT what
decides the coarse vectors, which sit inside it. What it decides is the
top of the grid: at 3/4 every vector with lightest mass 9/40 or more is
clean above (39 of 39 at 9, 30 of 30 at 10, and every vector at 11 to 13
-- the last 36 being the window's own, with no abandonable atom), at 7/10
every vector at 10/40 or more (30 of 30, then 21, 12, 3).

SWAP-CLEAN COVERS MOST OF ABOVE-CLEAN AT THREE ATOMS AND NOT AT FOUR (P3
holds where it was frozen; K-C silent): 162 of 183 at 3/4 (88.5%), 105 of
105 at 7/10, 18 of 18 at 3/5, 42 of 54 on the second family -- and 23 of
29 at four atoms and 3/4, 5 of 11 at 7/10, where the six clean tenths
vectors (gcd 4, lightest mass 8: (8, 8, 12, 12) and its permutations,
clean at both targets) are rescued by exchanges the lemma does not name. Over all
abandoning optima the swap rescues 4.6% at 3/4 and 5.5% at 7/10 at three
atoms, the unrescued sitting almost all at failing vectors, and 88% and
87% at four.

THE VARIABLE IS THE LIGHTEST MASS, AND THE GCD RETURNS AT ONE EDGE AS
DIVISIBILITY (P4 holds at 3/4 and fails at 7/10). Above-clean by lightest
mass at 3/4: 0 of 111, 102, 93, 84, 75 at masses 1 to 5, then 6 of 66,
36 of 57, 36 of 48, 39 of 39, 30 of 30, all above; the gcd-1 vectors with
lightest mass 8 go 18 of 24 and with 10 go 12 of 12 against the gcd-1
bulk's 135 of 552. At 7/10: 0 through mass 6, then 6 of 57, 6 of 48, 27
of 39, 30 of 30, all above -- and the 6 clean at lightest mass 8 are
EXACTLY the six fifths, the gcd-1 vectors there going 0 of 24. The
lemma's mass condition s w_r <= w_r' reads this: at (8, 16, 16) and
(8, 8, 24) every partner mass is a multiple of the lightest, so two
labels of the light atom trade evenly for one pair of a 16/40 atom (the
hand cell's rescue), while at (8, 15, 17) or (8, 12, 20) a 15/40 or 12/40
partner admits only s = 1. The grading by lightest mass is an observation
on the designed sweep; the divisibility reading at the edge is an
observation at one edge (three atoms, 7/10, lightest mass 8), and at four
atoms the edge is not there -- lightest mass 8 goes 10 of 10 at both
targets with only the four fifths swap-clean.

THE SECOND FAMILY'S FAILING FIFTHS FAIL ON COVERAGE (P5 holds): at 7/10
the three permutations of (8, 8, 24) take 4 forced failures each, all at
an 8/40 atom, with mass-fail 0 -- a partner at least as heavy holds a
pair at every such cell and every such pair is too lumpy.

AT 3/5 THE FIFTHS FAIL AT THE LIGHT ATOM, NOT AT THE ATOM THE WINDOW
ADMITS (P6 refuted). (8, 8, 24) takes 14 forced failures and (8, 16, 16)
6, every one at an 8/40 atom; no 16/40 atom is ever forced-abandoned. What
changed from 7/10 is the light atom's slack, 160 coverage units against
80, so the rest need not hold its low labels. The quarters stay swap-clean
at 3/5 and fail only at 1/2, at the 10/40 atoms (4 forced per vector);
the 20/40 atom enters the window there too and, with no partner as heavy,
is the coarse vectors' one mass-fail (6 abandoning optima per vector,
none of them forced).

WHAT THIS LEAVES OPEN: whether the grading by lightest mass has a closed
form -- a threshold in the slack 1 - w_min - T at which the rest must hold
a tradable pair -- and what exchange rescues the clean vectors the swap
does not, the (8, 8, 12, 12) permutations at four atoms first.
"""

import itertools
import os
import sys
import time
from fractions import Fraction

os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from explore_ruler_excess import (  # noqa: E402
    K, MENUS_NEW, MENUS_OLD, WD, compositions, int_menu, score_cell, vec_gcd)

F = Fraction
REHEARSE = "--rehearse" in sys.argv


# ------------------------------------------------------------- the swap

def swaps_for(weights, rows, tops, tt, opt, sizes, r, dr):
    """Every swap the lemma offers an optimum `sizes` abandoning atom r:
    drop atom r's lowest taken label on some other atom r', add r's top s
    labels. Returns the list of (r', s) that fire; each is re-scored (C2).
    Also returns whether any atom at least as heavy as r holds a pair at
    all (the mass condition met somewhere)."""
    m = len(weights)
    w = weights[r]
    fired = []
    mass_ok = False
    for rp in range(m):
        if rp == r or sizes[rp] == 0:
            continue
        a = weights[rp]
        if a < w:
            continue
        mass_ok = True
        srt = sorted(rows[rp], reverse=True)
        v = srt[sizes[rp] - 1]
        for s in range(1, K + 1):
            if s * w > a:
                break
            if a * v <= w * tops[r][s] + dr:
                new = list(sizes)
                new[rp] -= 1
                new[r] = s
                cov = sum(weights[i] * tops[i][new[i]] for i in range(m))
                cost = sum(weights[i] * new[i] for i in range(m))
                assert cov >= tt and cost <= opt, "swap misfires"
                assert cost == opt, "swap beats the optimum"
                fired.append((rp, s))
                break
    return fired, mass_ok


def read_cell(weights, rows, pd, tt):
    """Score a cell and read every abandoning optimum through the lemma.
    Returns the scorer's result plus per-atom abandonment records:
    (r, above_level, forced, n_optima_abandoning, n_rescued, mass_fail)."""
    res = score_cell(weights, rows, pd, tt)
    tau, opt, arg, tops = res["tau"], res["opt"], res["arg"], res["tops"]
    m = len(weights)
    records = []
    for r in range(m):
        top = max(rows[r])
        aband = [s for s in arg if s[r] == 0]
        if not aband:
            continue
        # P1 / K-A: the feasibility bound at every abandoned atom.
        assert (WD - weights[r]) * pd >= tt, "feasibility bound"
        rescued = 0
        mass_fail = 0
        for s in aband:
            cov = sum(weights[i] * tops[i][s[i]] for i in range(m))
            dr = cov - tt
            fired, mass_ok = swaps_for(weights, rows, tops, tt, opt, s, r,
                                       dr)
            if fired:
                rescued += 1
            elif not mass_ok:
                mass_fail += 1
        records.append((r, top > tau, top > tau and len(aband) == len(arg),
                        len(aband), rescued, mass_fail, dr if len(aband) == 1
                        else None))
    return res, records


# -------------------------------------------------------------- an arm

def run_arm(name, vectors, menus, target, m, record=None, quarters=None):
    t0 = time.time()
    tally = {v: dict(above_forced=0, below_forced=0, aband_opt=0,
                     rescued=0, mass_fail=0, cov_fail=0, cells=0,
                     forced_mass={})
             for v in vectors}
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
                t["below_forced"] += res["below_forced"]
                for r, above, forced, n, resc, mfail, dr in recs:
                    if not above:
                        continue
                    if forced:
                        assert resc == 0, "a forced atom was rescued"
                        fm = t["forced_mass"]
                        fm[v[r]] = fm.get(v[r], 0) + 1
                    t["aband_opt"] += n
                    t["rescued"] += resc
                    t["mass_fail"] += mfail
                    t["cov_fail"] += n - resc - mfail
                    if quarters is not None and v in quarters:
                        # C5: the slack is zero, every abandoning optimum
                        # has the rest fully served and is rescued at s=1.
                        assert resc == n, "quarters: an optimum unrescued"
                        for s in res["arg"]:
                            if s[r] == 0:
                                cov = sum(v[i] * res["tops"][i][s[i]]
                                          for i in range(m))
                                assert cov == tt, "quarters: overshoot"
                                assert all(s[i] == K for i in range(m)
                                           if i != r), "quarters: rest"
                                fired, _ = swaps_for(v, rows, res["tops"],
                                                     tt, res["opt"], s, r, 0)
                                assert any(v[rp] == v[r] and sw == 1
                                           for rp, sw in fired),                                     "quarters: the twin's s = 1 swap"
    forced_clean = {v for v, t in tally.items()
                    if t["above_forced"] == 0 and t["below_forced"] == 0}
    above_clean = {v for v, t in tally.items() if t["above_forced"] == 0}
    swap_clean = {v for v, t in tally.items() if t["rescued"] == t["aband_opt"]}
    assert swap_clean <= above_clean, "C3: swap-clean not in above-clean"
    print("\n%s  [%d vectors, %d cells, %.1f s]"
          % (name, len(vectors), sum(t["cells"] for t in tally.values()),
             time.time() - t0))
    print("  forced clean %d   above-clean %d   swap-clean %d"
          " (%.1f%% of above-clean)"
          % (len(forced_clean), len(above_clean), len(swap_clean),
             100.0 * len(swap_clean) / max(1, len(above_clean))))
    if record is not None:
        print("  C1 reproduction: forced clean %d against the record's %d"
              " -- %s" % (len(forced_clean), record,
                          "EXACT" if len(forced_clean) == record else "MISS"))
        assert len(forced_clean) == record, "K-D"
    tot = {k: sum(t[k] for t in tally.values())
           for k in ("aband_opt", "rescued", "mass_fail", "cov_fail")}
    print("  abandoning optima at above-level atoms %d: rescued %d, unrescued"
          " by mass %d, by coverage %d"
          % (tot["aband_opt"], tot["rescued"], tot["mass_fail"],
             tot["cov_fail"]))
    return tally, forced_clean, above_clean, swap_clean


def by_key(label, vectors, tally, above_clean, swap_clean, keyf):
    print("  %s" % label)
    print("      key    n   above-clean   swap-clean   abandoning optima"
          "   rescued   mass-fail   cov-fail   above-forced atoms")
    by = {}
    for v in vectors:
        by.setdefault(keyf(v), []).append(v)
    for k in sorted(by):
        vs = by[k]
        s = {q: sum(tally[v][q] for v in vs)
             for q in ("aband_opt", "rescued", "mass_fail", "cov_fail",
                       "above_forced")}
        print("    %5s %4d   %11d   %10d   %17d   %7d   %9d   %8d   %d"
              % (k, len(vs), sum(v in above_clean for v in vs),
                 sum(v in swap_clean for v in vs), s["aband_opt"],
                 s["rescued"], s["mass_fail"], s["cov_fail"],
                 s["above_forced"]))


def fmt(v):
    return "(" + ", ".join("%d/%d" % (a, WD) for a in v) + ")"


# ---------------------------------------------------------- the controls

def hand_cell():
    """C4: the paper cell where s = 1 misses and s = 2 rescues."""
    weights = (8, 16, 16)
    rows = [(7, 7, 6), (11, 7, 2), (8, 6, 6)]
    pd, tt = 20, 600
    res, recs = read_cell(weights, rows, pd, tt)
    print("C4 hand cell: tau %d  OPT %s  optima %s"
          % (res["tau"], F(res["opt"], WD), res["arg"]))
    assert res["tau"] == 6 and F(res["opt"], WD) == 2
    assert (0, 2, 3) in res["arg"]
    tops = res["tops"]
    dr = sum(weights[i] * tops[i][s] for i, s in enumerate((0, 2, 3))) - tt
    fired, mass_ok = swaps_for(weights, rows, tops, tt, res["opt"],
                               (0, 2, 3), 0, dr)
    print("  optimum (0, 2, 3): D_R %d, swaps that fire (atom, s): %s"
          % (dr, fired))
    assert dr == 8 and fired and all(s == 2 for _, s in fired)
    assert not any(16 * 6 <= 8 * tops[0][1] + dr for _ in [0]), "s=1 fires"
    print("  -- the hand cell reproduces: rescued at s = 2, not at s = 1.")


def main():
    t0 = time.time()
    print("explore_ruler_swap.py -- the feasibility bound, the swap lemma"
          " and the lightest mass%s" % (" (REHEARSAL)" if REHEARSE else ""))
    hand_cell()

    grid3 = list(compositions(WD, 3))
    assert len(grid3) == 741
    if REHEARSE:
        reps = [(8, 8, 24), (8, 16, 16), (10, 10, 20), (7, 16, 17),
                (5, 5, 30), (8, 15, 17), (13, 13, 14), (2, 3, 35)]
        grid3 = sorted({p for r in reps for p in itertools.permutations(r)})
        menus_old, menus_new = MENUS_OLD[:1], MENUS_NEW[:1]
        records = {}
    else:
        menus_old, menus_new = MENUS_OLD, MENUS_NEW
        records = {"3A": 183, "3B": 105, "3C": 18, "3D": 0, "3F": 54}
    coarse = [v for v in grid3 if vec_gcd(v) >= 8]
    quarters = {v for v in coarse if vec_gcd(v) == 10}
    fifths = [v for v in coarse if vec_gcd(v) == 8]

    for name, menus, target in (("3A", menus_old, F(3, 4)),
                                ("3B", menus_old, F(7, 10)),
                                ("3C", menus_old, F(3, 5)),
                                ("3D", menus_old, F(1, 2)),
                                ("3F", menus_new, F(7, 10))):
        tally, forced, above, swap = run_arm(
            "ARM %s -- menus %s, coverage %s"
            % (name, "".join(t for t, _ in menus), target),
            grid3, menus, target, 3, record=records.get(name),
            quarters=quarters if name == "3A" else None)
        print("  feasibility window: an abandoned atom weighs at most %d/40"
              " here" % (WD - -(-WD * 20 * target // 20)))
        by_key("by gcd stratum", grid3, tally, above, swap, vec_gcd)
        by_key("by lightest mass w_min", grid3, tally, above, swap, min)
        if name in ("3A", "3B"):
            print("  P4 -- the gcd-1 vectors sharing the coarse nine's"
                  " lightest mass:")
            for wmin in (8, 10):
                vs = [v for v in grid3 if min(v) == wmin and vec_gcd(v) == 1]
                bulk = [v for v in grid3 if vec_gcd(v) == 1]
                print("    w_min %d, gcd 1: %d of %d above-clean, %d"
                      " swap-clean; the gcd-1 bulk %d of %d above-clean"
                      % (wmin, sum(v in above for v in vs), len(vs),
                         sum(v in swap for v in vs),
                         sum(v in above for v in bulk), len(bulk)))
        print("  the coarse nine at this arm:")
        for v in coarse:
            t = tally[v]
            print("    %s  above-forced %d%s  below-forced %d  abandoning"
                  " optima %d  rescued %d  mass-fail %d  cov-fail %d  -- %s"
                  % (fmt(v), t["above_forced"],
                     " (at masses %s)" % ", ".join(
                         "%d/40 x%d" % (a, n)
                         for a, n in sorted(t["forced_mass"].items()))
                     if t["forced_mass"] else "",
                     t["below_forced"], t["aband_opt"], t["rescued"],
                     t["mass_fail"], t["cov_fail"],
                     "swap-clean" if v in swap else
                     ("above-clean" if v in above else "FAILS above")))
        if name in ("3A", "3B"):
            for v in coarse:
                assert tally[v]["above_forced"] == 0, "K-D"
                assert v in swap, "K-B: a coarse vector is not swap-clean"

    # ---------------------------------------------------------- arity 4
    grid4 = list(compositions(WD, 4))
    vectors4 = [v for v in grid4 if vec_gcd(v) >= 4]
    if REHEARSE:
        vectors4 = [v for v in vectors4 if vec_gcd(v) >= 8]
    coarse4 = [v for v in vectors4 if vec_gcd(v) >= 8]
    print("\nARITY 4 grid: %d vectors of gcd >= 4 (%s)"
          % (len(vectors4), ", ".join("gcd %d: %d" % (g, sum(vec_gcd(v) == g
                                                         for v in vectors4))
                                      for g in (10, 8, 5, 4))))
    for name, target in (("4A", F(3, 4)), ("4B", F(7, 10))):
        tally, forced, above, swap = run_arm(
            "ARM %s -- menus %s, coverage %s, FOUR atoms"
            % (name, "".join(t for t, _ in menus_old), target),
            vectors4, menus_old, target, 4)
        by_key("by gcd stratum", vectors4, tally, above, swap, vec_gcd)
        by_key("by lightest mass w_min", vectors4, tally, above, swap, min)
        for v in coarse4:
            t = tally[v]
            print("    %s  above-forced %d  abandoning optima %d  rescued"
                  " %d  -- %s" % (fmt(v), t["above_forced"], t["aband_opt"],
                                  t["rescued"], "swap-clean" if v in swap
                                  else "NOT swap-clean"))
            assert t["above_forced"] == 0 and v in swap, "K-B at arity 4"
    print("\ntotal wall %.1f s" % (time.time() - t0))


if __name__ == "__main__":
    main()
