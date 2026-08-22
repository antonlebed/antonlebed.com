"""THE PINNED TELESCOPE: what cures a class whose reference is
pinned to the present.

THE QUESTION
------------
The shift telescope (explore_shift_telescope.py) proved that
lowering both patiences by one is an exact one-step delay, which
nests pointwise for free and so exits every class it leaves with a
strictly smaller loss — two-move lookahead as a proved cure. Its
hypothesis is a SHIFTABLE member: both patiences finite and at
least one. What it cannot reach is the PINNED residue, and the
residue is large — 2,800 of 9,401 classes under the identity map,
4,215 of 11,935 under doubling — and it holds every stall the
squaring map produces, all three of them singleton classes at
patiences (3,0), (3,0) and (2,0). A zero patience is not a missing
reference: it is a reference pinned to the CURRENT image, the
tightest one available. So the delay argument does not merely fail
there, it is the wrong argument — a delay needs both references to
move, and one of these cannot move at all.

This rig asks whether the pinned side has a cure of its own, in
its own terms: not a delay but a REFINEMENT. With one reference
pinned to the present, the only move left on the patience axis is
to FRESHEN the other one, and a fresher reference is a SUBSET of
the one it replaces.

THE NAMED CLASS (imported verbatim)
-----------------------------------
Cover, streams, policies, losses, moves, quotient, the stall
object and the landscape evaluator are the parents'
(explore_scale_clock.py, explore_stall_tie.py,
explore_stall_unresourced.py, explore_stall_assembly.py,
explore_stall_maprate.py, explore_shift_telescope.py).
UNRESOURCED throughout: drawdown inert, 100 policies, counted
window starting at step 8, quotient by counted trace, cure
neighbours, lexicographic deficit. The patience axis is
0, 1, 2, 3, INF, where 0 reads the current image and INF refuses
the reference entirely.

WHOSE VOCABULARY THIS IS WRITTEN IN
-----------------------------------
The suspicion is NOT written in the shift telescope's vocabulary,
and the difference is the whole point. "Shiftable", "the diagonal",
"the delay" all belong to the interior of the patience square,
where both coordinates can step. The pinned cell's own vocabulary
is the ORDER on references: the stream's images are strictly
nested, so patience orders the references by inclusion and the
only question is what a strictly smaller reference does to a
commitment. TRANSPLANT, flagged: the expectation that the
freshened run stays inside the coarser one is imported from the
delay lemma's conclusion (pointwise nesting) while its mechanism
is discarded. The parent measured that transplant failing in
general — freshening a finite tree patience broke pairwise
counted nesting in 3,225 of 44,040 identity-map pairs — so the
question here is precisely whether the pinned coordinate is what
tames it.

HAND-ATTACK (fixed before the engine; the design follows it)
------------------------------------------------------------
Write pi = (st, ss, pt, pc) and let the images be J[0] ⊃ J[1] ⊃ …
(strictly nested; the maps are monotone, so the images inherit the
cylinders' nesting). At step n the tree reference is J[n − pt] and
the chain reference J[n − pc], each absent when the index is
negative.

WHAT IS FREE. On the tree side alone, freshening cannot change
BRANCH. A tree candidate is the child strictly containing the
reference; if the coarser reference already sits inside a child,
the fresher one — a subset of it — sits inside the same child. So
a fresher tree reference can only ever refine FURTHER along the
same path: it never crosses to a sibling. That much is a property
of the containment test and holds at every patience.

WHAT IS NOT FREE, and is the whole question. The commit loop is a
RACE. Tree and chain candidates are both offered and a preference
bit picks; whichever is taken changes the base the next candidate
is computed from. A run that refines deeper on the tree at step n
reaches the chain test from a different straddle, with a different
apex and different flanks, and its chain index is not comparable
term by term with the coarser run's. Nesting of the FINAL cells is
therefore not implied by nesting of the references, and the
parent's 3,225 identity-map failures are that gap being real.

LEMMA P (candidate; what the rig decides). Let pc = 0 and
pt ∈ {1, 2, 3}, and let pi' be pi with pt lowered by one. Then the
committed cell of pi' is contained in that of pi at every step.
The reason it might hold where the general freshening fails: with
the chain reference pinned to the current image, the chain side is
not a stale competitor at all. It refines toward the very interval
the commitment is required to contain — the run asserts it at
every step — so the chain test is applied against the tightest
reference in play, at the deepest index it admits, from whatever
base the tree race leaves. The suspicion is that the pinned chain
absorbs the difference the tree race opens, and that is exactly
what a race with a stale chain reference cannot do. Its mirror
swaps the coordinates: pt = 0 and pc freshened.

THE DICHOTOMY, and it needs nesting ALONE. Counted loss is the
product of the counted cells' lengths. If pi' nests pointwise then
every factor is at most pi's, so EITHER every counted cell is
equal — the freshened run lands in the same class — OR the loss is
strictly smaller. So one nesting lemma buys a strictly improving
nested class the moment the walk leaves its class, with no
separate improvement argument anywhere. Two steps of that are
checked against the parents' code rather than assumed, because
either would break it silently. The class signature is the TUPLE
OF COUNTED INTERVALS and nothing else — not the rank, not the
chain index (explore_stall_tie.py, the run over a policy) — so
equal cells really do mean the same class; and nested intervals of
equal length ARE the same interval, which is the step the equal
case rests on. It needs every counted cell finite, and it has
that wherever both classes are finite-loss, since one infinite
counted cell is what sets that flag.

THE WALK, and what it can prove. From a present-pinned member the
freshening move is available until the moving coordinate reaches
0, so the walk has length at most 3 on this axis. At a STALL no
single move improves, so the first step must land in the same
class, and the exit — if there is one — is at distance two or
three. The reach a proved Lemma P would buy is therefore: every
present-pinned class either exits to a strictly improving
pointwise-nested class within three cure moves, or is FROZEN all
the way down the freshened axis. Distance two is not implied and
is a measurement; the three squaring-map stalls are measured at
exactly two by the parents, which is what makes them the sharpest
place to read the walk.

PREDICTIONS, fixed before the engine ran
----------------------------------------
C0 [positive control, run first] The three squaring-map stall
   specimens reproduce as stalls, each a singleton class, at
   patiences (3,0), (3,0), (2,0), and each keeps at least three
   strictly improving classes at cure distance two. Reproduced
   here from this rig's own code path. A miss means the population
   is not the parents' and no verdict below is read (K3).
P1 [the lemma battery, hard] Over the three anchor worlds x maps
   identity/doubling/squaring x all four style pairs x
   pt ∈ {1,2,3} at pc = 0: the freshened run's cell is contained
   in the coarser run's at EVERY step, not only the counted ones.
   GUESS: universal, zero failing pairs. A miss is K1 and prints
   its witness.
P1' [the mirror, hard] The same at pt = 0 with pc freshened.
   GUESS, marked as a guess and weaker: universal as well. The
   chain side is where the parent's pairwise failures were denser
   (8,274 against 3,225), so this is the leg more likely to fall.
P2 [the residue's anatomy] Over the parents' census scope
   (horizons 9, 10, 12, 16; maps identity and doubling), split the
   PINNED off-bottom finite-loss classes by kind: present-pinned
   (some member with a zero patience), INF-only pinned (covered
   already by the parent's one-sided variant), and neither.
   Controls: the pinned totals reproduce 2,800 and 4,215 and the
   no-nesting totals 0 and 632. GUESS: present-pinned is the
   majority of the residue under both maps.
P3 [the reach] For every present-pinned class, walk the freshening
   move down the pinned axis and report the exit distance (1, 2 or
   3) or FROZEN. HARD CHECK (K2): every step of every walk nests
   pointwise against the start class, and every step landing in a
   distinct class strictly improves. GUESS: exits at distance 1
   dominate off the stalls, no walk reaches 3, and FROZEN is rare.
P4 [the stalls] The three squaring-map stalls' measured radius-two
   escape IS this walk: from (3,0), (3,0), (2,0) the freshening
   step stays in class once and exits improving at the second, and
   the exit class is one the parents already count among the
   distance-two improving classes. GUESS: all three.

FOLLOW-UP SLATE (frozen after the battery's first print and
before the amended run; no prediction above was touched)
----------------------------------------------------------------
The battery as frozen asked for containment at EVERY step and P1
FELL there, while P1' — the leg the slate marked weaker — held.
The first witness sits at step 4, and the counted window starts at
step 8, so the frozen question and the LOAD-BEARING one have come
apart: the dichotomy is a statement about counted cells alone, and
a pre-window failure costs it nothing. The parents met the same
split from the other side (the one-sided delay's 508 all-steps
failures all sitting before the window). So the battery is
amended to tally the two scopes separately and to report where the
first failure of each sits.
P1a [the counted scope, hard] At pc = 0 with pt freshened, the
    freshened cell is contained in the coarser one at every
    COUNTED step. GUESS: universal — the pre-window race settles
    before the window opens. A counted miss keeps K1 and kills
    the tree-side lemma outright.
P1b [the anatomy of the all-steps failures] Every all-steps
    failure sits strictly before the counted window start. GUESS:
    yes; a failure at or after it is the same event as P1a's.

KILL CRITERIA (observables; the meaning is weighed after the run)
----------------------------------------------------------------
K1 Any battery pair with a step whose freshened cell is not
   contained in the coarser cell. Lemma P is FALSE as stated; the
   rig prints the first witness (world, map, styles, patience,
   step) and the census legs report on the failing map only as
   anatomy, never as a law.
K2 Any census walk step that nests pointwise, lands in a distinct
   class, and does not strictly improve. The dichotomy is
   miscoded; the witness prints and no reach verdict is read.
K3 The control counts miss (the stalls, the pinned totals, the
   no-nesting totals). The population is not the parents' and
   nothing below is a verdict.

ENGINE
------
E0 the control (C0).
E1 the lemma battery, both directions (P1, P1').
E2 the pinned census over the parents' scope (P2, P3), with the
   reproduction controls.
E3 the three squaring-map stalls walked step by step (P4).
Exact big-integer arithmetic for every verdict; floating point
only in printed logs. Sequential; estimated run three to eight
minutes, the E2 census the driver; memory trivial (no BLAS
import); exit nonzero on any check failure.

FINDINGS (entered after the run; ALL CHECKS PASS, exit 0, 5.5 s,
15.3 MB peak under the memory watch)
----------------------------------------------------------------
F1 THE PINNED SIDE IS NOT SYMMETRIC, AND THE SURVIVING LEMMA IS
   THE ONE THE SLATE CALLED WEAKER. Chain freshening at a pinned
   tree (pt = 0, pc lowered by one) holds containment at EVERY
   step in all 108 battery pairs -- three anchor worlds, three
   maps, four style pairs, three patiences -- with zero misses at
   any scope. Tree freshening at a pinned chain FALLS: 38 of 108
   pairs break containment somewhere and 31 break it inside the
   counted window, the first at the near-miss world under the
   identity map at styles (0,0), patience 2, step 8. K1 fires on
   that side and the follow-up's P1a falls with it -- the failures
   do not sit before the window, they reach step 15. So P1 is
   FALSIFIED and P1' survives, exactly inverting the slate's
   ranking of the two legs. AND THE NEGATIVE IS SIGNAL RATHER
   THAN INSTRUMENT, by a split the corpus itself supplies: the
   failing side's 38 misses sorted by style pair leave the
   chain-preferring corner -- preference for the chain at both
   cell kinds -- carrying 6, every one of them under doubling or
   squaring and ZERO under the identity map, which is exactly the
   scope at which the chain-preferring nesting theorem
   (explore_ladder_entry.py) says there can be none. A rig
   breaking containment for its own reasons would not know to
   stop at that corner under that map, and the off-map misses
   match the drift that record already carries.
F2 THE RESIDUE IS ALMOST ALL PRESENT-PINNED. Identity: 2,800
   pinned classes = 2,546 present-pinned + 254 INF-only + 0
   neither. Doubling: 4,215 = 3,552 + 663 + 0. Both reproduction
   controls hold (pinned 2,800 and 4,215; no-nesting 0 and 632).
   So the delay lemma's residue is not a scattering of odd cells:
   five in six of it has a reference pinned to the present, and
   the one-sided variant already covered the rest.
F3 EXISTS-OVER-MEMBERS, THE FRESHENING REACHES MOST OF THE
   RESIDUE AT DISTANCE ONE -- AND THE GAP IS ON THE SIDE F1
   NAMES. From SOME member, a pointwise-nested strictly improving
   class sits at cure distance ONE for identity 2,546 of 2,546
   tree-side classes, doubling 597 of 597 chain-side and 2,535 of
   2,955 tree-side; the 420 that reach nothing are all doubling
   tree-side, which is the pinned CHAIN, the side whose
   containment F1 refutes. Zero classes are frozen anywhere. The
   dichotomy is clean across the whole census -- no walk step
   nests into a distinct class without strictly improving. P3's
   guess that distance-one exits dominate holds, but NOT in the
   form the distance histogram appears to give: the walk stops at
   the first change of class, so the two and three slots read
   zero because at EVERY present-pinned class the first
   freshening already leaves the class, never because a longer
   walk was measured and refused. What this leg does not observe
   is whether the 420 reach anything at distance two -- E4 asks
   exactly that question at the three stalls and nowhere else.
   The member choice is load-bearing exactly as the parent found
   it, which is why F1's per-pair failures and this leg's
   coverage are the same fact seen from two sides.
F4 AT THE STALLS THE FIRST STEP DOES NOT NEST, AND EXACTLY ONE
   ESCAPE DOES. Walked from each stall's own member, the single
   freshening move LEAVES the class and is neither nested nor
   improving at all three specimens -- P4 is falsified, and the
   measured radius-two escape is not this walk read stepwise. Yet
   of the strictly improving classes at cure distance two --
   five, four and three at the three specimens -- EXACTLY ONE at
   each nests pointwise against the stall, and at all three it is
   reached by tree freshening twice. E4 reports the move TYPES
   over every member of the intermediate class and never which
   member pays; what it therefore does NOT establish is that the
   second freshening needs a different member than the first one
   landed on. That further clause is measured and REFUTED by
   explore_pinned_composite.py: the two freshenings run from the
   stall's own member at one style pair throughout, and the free
   re-selection is never spent.

THE VERDICT. The pinned residue has no telescope of its own on
the side that matters. Freshening a reference is a cure at cure
distance one across essentially the whole residue (F3), and at a
pinned TREE it nests by what looks like a law (F2, F1) -- but at a
pinned CHAIN, which is where every stall the parents located in
this residue sits (the three squaring-map ones; what the corpus's
other finite-loss stalls do on this axis is not read here) --
containment is false with witnesses inside the counted window
(F1), so no stepwise nesting argument can reach those stalls. What
the three stalls' measured escape radius of two actually is, read
here for the first time: a nested improving class DOES sit at
distance two, exactly one of the several improving ones, and the
route to it is two tree freshenings. So the derivation the reader
corpus's open edge still owes is not a stepwise lemma at all -- it
is a two-move statement whose intermediate step is deliberately
non-nesting. Which member the second move departs from is not read
here and is read by explore_pinned_composite.py, which finds it is
the stall's own descendant: the object is a single member and its
cells, not the intermediate class. That is a sharper
statement of the owe than the corpus carried before, and it names
the one place a proof can start.

Run record. ONE engine, three runs. The first run's battery asked
for containment at every step, and its failure at step 4 --
before the counted window opens -- separated the frozen question
from the load-bearing one; the follow-up slate above was frozen
before the amended battery ran, and the amendment tallies the two
scopes separately rather than replacing either. The second run
repaired the census, which had lumped "does not nest" together
with "nests but does not improve": the first is the lemma failing
and the second is the dichotomy failing, and only the second is a
kill, so the two are now counted apart and per side. E4 was added
after E2 and E3 printed, with its own slate frozen before it ran;
naming which class the nesting escape is, and the route, is
anatomy of that same observable and was printed with it. A FOURTH
run was added by the audit, under one question frozen before it:
a negative verdict owes a split between instrument and signal,
and the corpus holds a theorem -- chain-preferring nesting under
the identity map -- that pins a corner where a signal-measuring
rig must find zero misses. The battery now sorts its misses by
style pair and map and checks that corner. No prediction, no
control and no finding above it was touched. Final run ALL CHECKS
PASS, exit 0, 5.5 s.
"""

import sys
from fractions import Fraction

import explore_scale_clock as SC
import explore_stall_assembly as SA
import explore_stall_maprate as MR
import explore_shift_telescope as TS

FAILURES = []

def check(name, ok):
    print("  [%s] %s" % ("PASS" if ok else "FAIL", name))
    if not ok:
        FAILURES.append(name)

FRESH_AXIS = (1, 2, 3)
VERDICT = {}
NESTING_ESCAPES = {}

def is_present_pinned(p):
    """A member with a reference pinned to the current image and a
    freshening move still available on the other coordinate."""
    return ((p[3] == 0 and p[2] in FRESH_AXIS)
            or (p[2] == 0 and p[3] in FRESH_AXIS))

def freshen(p):
    """Lower the non-pinned patience by one; the pinned coordinate
    stays where it is."""
    if p[3] == 0:
        return (p[0], p[1], p[2] - 1, p[3], p[4])
    return (p[0], p[1], p[2], p[3] - 1, p[4])

def all_cells(J, policy, horizon):
    """Committed intervals at EVERY step (the battery's scope)."""
    tr = SC.run_reader(J, policy[:4], horizon)[3]
    return [tr[n][2] for n in range(horizon)]

def inside(a, b):
    """Interval a contained in interval b (endpoints allowed)."""
    return TS.frac_le(b[0], a[0]) and TS.frac_le(a[1], b[1])

# ----------------------------------------------------------------- #
# E0: the control
# ----------------------------------------------------------------- #

EXPECT_PATIENCE = {"census-2313..": (3, 0),
                   "census-3212..": (3, 0),
                   "designed-16": (2, 0)}

def e0_control():
    print("\nE0  THE CONTROL (the parents' stall population)")
    seen = {}
    for tag, digs, horizon in TS.SQ_SPECIMENS:
        ev = SA.evaluate(list(digs), "sq", horizon)
        if not ev["stalls"]:
            check("%s reproduces as a stall" % tag, False)
            continue
        sig_of = {p: s for s, ps in ev["mem"].items() for p in ps}
        qloss = ev["qloss"]
        for s in ev["stalls"]:
            mem = ev["mem"][s]
            Lx = Fraction(qloss[s][1][0], qloss[s][1][1])
            pats = sorted({(p[2], p[3]) for p in mem})
            esc = set()
            for p in mem:
                for _t1, q in TS.typed_moves(p):
                    z = sig_of[q]
                    if z == s:
                        continue
                    for r in ev["mem"][z]:
                        for _t2, q2 in TS.typed_moves(r):
                            w = sig_of[q2]
                            if w in (s, z) or qloss[w][1][2]:
                                continue
                            if Fraction(qloss[w][1][0],
                                        qloss[w][1][1]) < Lx:
                                esc.add(w)
            print("    %s: %d member(s), patiences %s, "
                  "distance-2 improving classes %d"
                  % (tag, len(mem), pats, len(esc)))
            check("%s singleton at patience %s"
                  % (tag, (EXPECT_PATIENCE[tag],)),
                  len(mem) == 1 and pats == [EXPECT_PATIENCE[tag]])
            check("%s keeps >= 3 distance-2 improving classes" % tag,
                  len(esc) >= 3)
            seen[tag] = (ev, s, esc)
    return seen

# ----------------------------------------------------------------- #
# E1: the lemma battery
# ----------------------------------------------------------------- #

ANCHORS = TS.ANCHORS
BATTERY_MAPS = ("id", "dbl", "sq")

def e1_battery():
    print("\nE1  THE LEMMA BATTERY (containment under freshening)")
    for side, label in ((0, "tree freshened at pinned chain"),
                        (1, "chain freshened at pinned tree")):
        pairs = miss_all = miss_ct = 0
        first_all = first_ct = None
        latest_all = -1
        by_style = {}
        for wname, digs, horizon in ANCHORS:
            cyls = SC.cylinders(list(digs))
            for mp in BATTERY_MAPS:
                J = SC.images(cyls, mp)[:horizon]
                for st in (0, 1):
                    for ss in (0, 1):
                        for pfree in FRESH_AXIS:
                            if side == 0:
                                pol = (st, ss, pfree, 0, SC.INF_D)
                            else:
                                pol = (st, ss, 0, pfree, SC.INF_D)
                            polf = freshen(pol)
                            ca = all_cells(J, pol, horizon)
                            cb = all_cells(J, polf, horizon)
                            pairs += 1
                            bad = [n for n in range(horizon)
                                   if not inside(cb[n], ca[n])]
                            if not bad:
                                continue
                            miss_all += 1
                            by_style[((st, ss), mp)] =                                 by_style.get(((st, ss), mp), 0) + 1
                            latest_all = max(latest_all, max(bad))
                            if first_all is None:
                                first_all = (wname, mp, st, ss,
                                             pfree, bad[0])
                            ctbad = [n for n in bad if n >= SC.N0]
                            if ctbad:
                                miss_ct += 1
                                if first_ct is None:
                                    first_ct = (wname, mp, st, ss,
                                                pfree, ctbad[0])
        if first_all is not None:
            print("    first all-steps miss %s %s styles=(%d,%d) "
                  "patience=%d step=%d" % first_all)
            print("    latest failing step %d (counted window "
                  "starts at %d)" % (latest_all, SC.N0))
        if first_ct is not None:
            print("    first COUNTED miss %s %s styles=(%d,%d) "
                  "patience=%d step=%d" % first_ct)
        print("    %s: %d pairs | all-steps misses %d | "
              "counted-step misses %d" % (label, pairs, miss_all,
                                          miss_ct))
        if side == 0:
            print("    misses by style pair and map: %s"
                  % dict(sorted(by_style.items())))
            corner = sum(v for k, v in by_style.items()
                         if k[0] == (1, 0))
            corner_id = sum(v for k, v in by_style.items()
                            if k[0] == (1, 0) and k[1] == "id")
            print("    chain-preferring corner (styles (1,0)): %d "
                  "misses, of them %d under the identity map"
                  % (corner, corner_id))
            check("the negative is signal, not instrument: zero "
                  "identity-map misses in the chain-preferring "
                  "corner", corner_id == 0)
        print("    VERDICT %s: %s" % (
            label,
            "the lemma HOLDS at this scope" if miss_ct == 0
            else "K1 FIRES -- the lemma is FALSE, and the failures "
                 "reach the counted window"))
        VERDICT[label] = (miss_ct == 0, miss_all, miss_ct, pairs)

# ----------------------------------------------------------------- #
# E2: the pinned census
# ----------------------------------------------------------------- #

CENSUS_HORIZONS = TS.CENSUS_HORIZONS
CENSUS_MAPS = TS.CENSUS_MAPS
EXPECT_PINNED = {"id": 2800, "dbl": 4215}
EXPECT_NO_NEST = {"id": 0, "dbl": 632}

def side_of(p):
    """Which coordinate the freshening walk moves: 'tree' at a
    pinned chain, 'chain' at a pinned tree."""
    return "tree" if p[3] == 0 else "chain"

def walk_class(ev, horizon, s, cellcache, sig_of):
    """Walk the freshening move from every present-pinned member of
    class s, keeping the two sides apart. Returns a dict per side
    with the best exit distance, the frozen and non-nesting walk
    counts, and the dichotomy violations."""
    mem, qloss = ev["mem"], ev["qloss"]
    def cells(sig):
        if sig not in cellcache:
            rep = sorted(mem[sig], key=SC.pol_key)[0]
            cellcache[sig] = TS.counted_cells(ev["J"], rep, horizon)
        return cellcache[sig]
    out = {"tree": None, "chain": None}
    starts = [p for p in mem[s] if is_present_pinned(p)]
    if not starts:
        return out
    cx = cells(s)
    Lx = Fraction(qloss[s][1][0], qloss[s][1][1])
    for side in ("tree", "chain"):
        mine = [p for p in starts if side_of(p) == side]
        if not mine:
            continue
        rec = {"best": None, "frozen": 0, "nonest": 0,
               "viol": []}
        for p in mine:
            cur = p
            d = 0
            while is_present_pinned(cur):
                cur = freshen(cur)
                d += 1
                t = sig_of[cur]
                if t == s:
                    continue
                nested = TS.nests_pointwise(cells(t), cx)
                improves = (not qloss[t][1][2]
                            and Fraction(qloss[t][1][0],
                                         qloss[t][1][1]) < Lx)
                if not nested:
                    rec["nonest"] += 1
                elif not improves:
                    rec["viol"].append((s, p, cur))
                else:
                    rec["best"] = d if rec["best"] is None \
                        else min(rec["best"], d)
                break
            else:
                rec["frozen"] += 1
        out[side] = rec
    return out

def e2_census():
    print("\nE2  THE PINNED CENSUS (identity and doubling, "
          "horizons %s)" % ",".join(str(h) for h in CENSUS_HORIZONS))
    tot = {mp: 0 for mp in CENSUS_MAPS}
    pinned = {mp: 0 for mp in CENSUS_MAPS}
    no_nest = {mp: 0 for mp in CENSUS_MAPS}
    present = {mp: 0 for mp in CENSUS_MAPS}
    infonly = {mp: 0 for mp in CENSUS_MAPS}
    neither = {mp: 0 for mp in CENSUS_MAPS}
    dist = {mp: {sd: {1: 0, 2: 0, 3: 0, "frozen": 0,
                      "no-nesting": 0, "classes": 0}
                 for sd in ("tree", "chain")}
            for mp in CENSUS_MAPS}
    all_viol = []
    for horizon in CENSUS_HORIZONS:
        for mp in CENSUS_MAPS:
            for wname, digs in MR.census_pool(horizon):
                ev = SA.evaluate(digs, mp, horizon)
                sig_of = {p: s for s, ps in ev["mem"].items()
                          for p in ps}
                cellcache = {}
                for s in ev["marg"]:
                    tot[mp] += 1
                    nt, sh, _fz, _imp, _v, _ptw = TS.class_stats(
                        ev, horizon, s, cellcache, sig_of)
                    if not nt:
                        no_nest[mp] += 1
                    if sh:
                        continue
                    pinned[mp] += 1
                    walks = walk_class(ev, horizon, s, cellcache,
                                       sig_of)
                    if any(walks[sd] for sd in walks):
                        present[mp] += 1
                        for sd in ("tree", "chain"):
                            rec = walks[sd]
                            if rec is None:
                                continue
                            cell = dist[mp][sd]
                            cell["classes"] += 1
                            for v in rec["viol"]:
                                all_viol.append(
                                    (wname, mp, horizon) + v)
                            if rec["best"] is not None:
                                cell[rec["best"]] += 1
                            elif rec["frozen"]:
                                cell["frozen"] += 1
                            else:
                                cell["no-nesting"] += 1
                    elif any(p[2] is None or p[3] is None
                             for p in ev["mem"][s]):
                        infonly[mp] += 1
                    else:
                        neither[mp] += 1
            print("  h=%-2d %-3s done (classes so far %d)"
                  % (horizon, mp, tot[mp]))
    for mp in CENSUS_MAPS:
        print("  %-3s: %d classes | pinned %d = present %d + "
              "INF-only %d + neither %d"
              % (mp, tot[mp], pinned[mp], present[mp],
                 infonly[mp], neither[mp]))
        for sd in ("tree", "chain"):
            print("       %-5s freshening: %s" % (sd, dist[mp][sd]))
        check("%s pinned total reproduces %d (%d)"
              % (mp, EXPECT_PINNED[mp], pinned[mp]),
              pinned[mp] == EXPECT_PINNED[mp])
        check("%s no-nesting total reproduces %d (%d)"
              % (mp, EXPECT_NO_NEST[mp], no_nest[mp]),
              no_nest[mp] == EXPECT_NO_NEST[mp])
    for v in all_viol[:12]:
        print("  VIOLATION %s %s h=%d class %s member %s -> %s"
              % (v[0], v[1], v[2], v[3], SC.fmt_pol5(v[4]),
                 SC.fmt_pol5(v[5])))
    check("dichotomy holds: zero walk violations (%d)"
          % len(all_viol), not all_viol)
    return dist

# ----------------------------------------------------------------- #
# E3: the stalls walked
# ----------------------------------------------------------------- #

def e3_stalls(seen):
    print("\nE3  THE SQUARING-MAP STALLS WALKED")
    for tag, digs, horizon in TS.SQ_SPECIMENS:
        if tag not in seen:
            continue
        ev, s, esc = seen[tag]
        sig_of = {p: s2 for s2, ps in ev["mem"].items() for p in ps}
        qloss = ev["qloss"]
        Lx = Fraction(qloss[s][1][0], qloss[s][1][1])
        p = sorted(ev["mem"][s], key=SC.pol_key)[0]
        cx = TS.counted_cells(ev["J"], p, horizon)
        print("    %s: start %s, walk on the %s side"
              % (tag, SC.fmt_pol5(p), side_of(p)))
        cur, d = p, 0
        while is_present_pinned(cur):
            cur = freshen(cur)
            d += 1
            t = sig_of[cur]
            if t == s:
                print("      step %d -> %s: same class"
                      % (d, SC.fmt_pol5(cur)))
                continue
            rep = sorted(ev["mem"][t], key=SC.pol_key)[0]
            ct = TS.counted_cells(ev["J"], rep, horizon)
            nested = TS.nests_pointwise(ct, cx)
            better = (not qloss[t][1][2]
                      and Fraction(qloss[t][1][0],
                                   qloss[t][1][1]) < Lx)
            print("      step %d -> %s: new class, nested %s, "
                  "improves %s, among the parents' escapes %s"
                  % (d, SC.fmt_pol5(cur), nested, better,
                     t in esc))
            check("%s: the walk's dichotomy holds at step %d"
                  % (tag, d), (not nested) or better)
            break
        else:
            print("      the walk reaches the axis floor in class")

def e4_escape_nesting(seen):
    """E4 (added after E2 and E3 printed; slate frozen before the
    run). At each squaring-map stall, does ANY of the strictly
    improving classes at cure distance two nest pointwise against
    the stall? GUESS: at least one does at each stall, which would
    make nesting non-monotone along the walk; none nesting anywhere
    is the stronger reading -- the pinned stalls' measured escape
    would then sit wholly outside the nesting frame, and that is
    what a derivation of radius two there still owes.
    """
    print("\nE4  DO THE DISTANCE-2 ESCAPES NEST?")
    for tag, digs, horizon in TS.SQ_SPECIMENS:
        if tag not in seen:
            continue
        ev, s, esc = seen[tag]
        p0 = sorted(ev["mem"][s], key=SC.pol_key)[0]
        cx = TS.counted_cells(ev["J"], p0, horizon)
        nest_ct = 0
        for t in sorted(esc, key=lambda z: ev["qranks"][z]):
            rep = sorted(ev["mem"][t], key=SC.pol_key)[0]
            ct = TS.counted_cells(ev["J"], rep, horizon)
            if TS.nests_pointwise(ct, cx):
                nest_ct += 1
                sig_of = {q: z for z, qs in ev["mem"].items()
                          for q in qs}
                routes = set()
                for t1, q in TS.typed_moves(p0):
                    z = sig_of[q]
                    if z == s:
                        continue
                    for r in ev["mem"][z]:
                        for t2, q2 in TS.typed_moves(r):
                            if sig_of[q2] == t:
                                routes.add((t1, t2))
                print("      the nesting escape is %s, reached by "
                      "%s" % (SC.fmt_pol5(rep),
                              " ".join("%s+%s" % rt
                                       for rt in sorted(routes))))
        print("    %s: %d of %d distance-2 improving classes nest "
              "pointwise against the stall" % (tag, nest_ct,
                                               len(esc)))
        NESTING_ESCAPES[tag] = (nest_ct, len(esc))

def main():
    print("THE PINNED TELESCOPE (unresourced, exact arithmetic)")
    seen = e0_control()
    if FAILURES:
        print("\nRIG DEAD AT E0 (K3): %s" % FAILURES)
        return 1
    e1_battery()
    e2_census()
    e3_stalls(seen)
    e4_escape_nesting(seen)
    print("\n%s" % ("ALL CHECKS PASS" if not FAILURES
                    else "FAILURES: %s" % FAILURES))
    return 1 if FAILURES else 0

if __name__ == "__main__":
    sys.exit(main())
