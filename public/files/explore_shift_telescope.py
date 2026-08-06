"""THE SHIFT TELESCOPE: the domination law's exists-neighbor built
by shifting the class's own trace.

THE QUESTION
------------
The domination census (explore_stall_domination.py) left one open
step: derive the domination law itself — SOME cure neighbor of every
off-bottom class commits nested-or-equal cells at every counted step
— whose routing-step case analysis was the named gap (its L4). This
rig attacks the law from the other end: a DELAY argument that avoids
the routing case analysis entirely by re-indexing, and a census of
which cure-move types actually supply the nested neighbor, the
anatomy the remaining distance-1 derivation needs.

THE NAMED CLASS (imported verbatim)
-----------------------------------
Cover, streams, policies, losses, moves, quotient, the stall object
and the landscape evaluator are the parents'
(explore_scale_clock.py, explore_stall_tie.py,
explore_stall_unresourced.py, explore_stall_assembly.py,
explore_stall_maprate.py). UNRESOURCED throughout: delta inert, 100
policies, N0 = 8 counted start, quotient by counted trace, cure
neighbors, lexicographic deficit.

HAND-ATTACK (fixed before the engine; the design follows it)
------------------------------------------------------------
LEMMA T (THE SHIFT TELESCOPE — any map, any stream, any style
bits). Let pi = (st, ss, pt, pc) have both patiences finite and
>= 1, and let pi_down = (st, ss, pt-1, pc-1). Then
   C_{pi_down}(n) = C_pi(n+1) for every step n.
PROOF. The references are functions of the age alone: pi_down's
references at step n are J[n-(pt-1)] = J[(n+1)-pt] and likewise on
the chain side, defined exactly when pi's step-(n+1) references
are — identical inputs, both coordinates. The commit loop is a
deterministic function of (cell, ref_t, ref_c, st, ss). Base: at
step 0 pi has both references missing (pt, pc >= 1), so
C_pi(0) = ROOT, which is pi_down's start; induct on n. QED. The
routing-step case analysis is not resolved here — it is AVOIDED:
the two runs are the same run read one step apart.

ONE-SIDED VARIANT T'. If pt is infinite (the tree reference never
exists) the run is a function of the chain-reference sequence
alone, so the SINGLE cure move pc -> pc-1 (pc >= 1) is a pure
delay with the same conclusion — a distance-ONE nested neighbor.
Mirror for pc infinite, pt >= 1.

COROLLARIES (unresourced, lexicographic deficit, finite-loss
off-bottom class x; every commit strictly shrinks the interval):
CT1 (pointwise nesting, free). pi_down's counted cell at step n is
    C_pi(n+1), a subset of C_pi(n), for n <= H-2; at the last
    counted step C_{pi_down}(H-1) sits inside C_{pi_down}(H-2) =
    C_pi(H-1). So pi_down nests pointwise at EVERY counted step.
CT2 (the loss telescopes to the window's ends).
    L(pi_down)/L(pi) = |C_pi(H)| / |C_pi(8)|, every interior
    counted step cancelling — the same telescoping the one-cell
    wall met at the frontier, now for every policy at once.
CT3 (the dichotomy is exact). Equal lengths of nested cells force
    the same cell, and the trace entry is a function of the cell:
    EITHER pi's counted window is FROZEN (C(8) = C(H)), pi_down
    lands in the SAME class, and one more shift probes one more
    step — OR pi_down is a DISTINCT class, nested pointwise, with
    STRICTLY smaller loss.
CT4 (distance <= 2 in the cure graph). (pt-1, pc) is one single
    move from a member of x, (pt-1, pc-1) one more: every
    off-bottom finite-loss class holding a SHIFTABLE member (both
    patiences in {1,2,3}) with an unfrozen window has a strictly
    improving pointwise-nested class within cure-graph distance 2
    — for EVERY map, sq included. The measured escape radius of
    exactly 2 at every stall specimen is this shift.
CT5 (the wall at distance 2). The distance-2 margin is capped by
    ln|C(H)| - ln|C(8)|, one refinement's price when the window
    pins to a single mediant step — the 1/D walk as a corollary.
What Lemma T does NOT give: the distance-ONE law under id (the
measured fact). Its unreachable cases: classes whose members all
have a zero patience coordinate (PINNED), frozen windows at the
axis floor, and mixed-consultation single moves. The census below
names them.

PREDICTIONS, fixed before the engine ran
----------------------------------------
T1 [gate] Lemma T verifies mechanically: over the three anchor
   worlds (the near-miss dbl world, the sq flagship, the designed
   three-burst stream) x maps id/dbl/sq x all four style pairs x
   pt, pc in {1,2,3}: trace_{pi_down}(n) == trace_pi(n+1) for all
   n <= H-2, one hundred percent. A single miss kills the rig (K1).
T2 [the id move anatomy] Per off-bottom finite-loss id class, the
   cure-move TYPES whose neighbor nests pointwise and strictly
   improves (types: st-flip, ss-flip, pt-down/up, pc-down/up,
   sigma-diagonal). GUESS, marked as such: patience-DOWN types
   dominate the histogram, and every id class has at least one
   nesting type (the domination census re-seen through moves).
T3 [telescope coverage] Per off-bottom finite-loss class (id and
   dbl): SHIFTABLE member present? window FROZEN (every shiftable
   member's shift lands in-class)? THEOREM CHECK, hard (K2): every
   shiftable member's shift either lands in-class or is nested
   pointwise with strictly smaller loss. GUESS on the shape: over
   90 percent of classes shiftable, under 5 percent frozen.
T4 [the dbl dent at distance 2] Among the dbl classes with NO
   nesting cure move (the frozen record's 632), count those without
   a shiftable member — the genuine residue Lemma T cannot reach.
   GUESS: zero or near zero. Control: the no-nesting count itself
   reproduces 632 (and id's reproduces 0) against the frozen
   domination record.
T5 [the sq stalls at distance 2] Each of the three sq stall classes
   holds a shiftable member whose shift strictly improves — the
   measured radius-2 escape identified as the telescope. GUESS:
   all three. The hard control is only that each specimen
   reproduces as a stall and keeps SOME improving class at
   cure-graph distance two (the parents' measured escape radius);
   whether that escape is the telescope is what E3 reports.

E4 FOLLOW-UP SLATE (frozen after E2's histogram printed, before E4
ran; E2's histogram showed nesting is a patience-down monopoly with
pt-down covering every id class, so the pairwise question became
the sharp one)
----------------------------------------------------------------
E4a pt-down with finite pt in {1,2,3} nests pointwise on counted
    steps UNIVERSALLY under id at the census scope. GUESS: zero
    failing pairs — the class-level law would reduce to member
    choice plus class exit.
E4b pt-down from the infinite tree patience (the INF -> 3 axis
    move) under id: GUESS, weaker: universal as well.
E4c pc-down under id fails pairwise nesting somewhere (the routing
    crossing is real on the chain side): measure the rate, print
    the first anatomies. Counted-step nesting and all-steps
    nesting tallied separately.
E2w (added in the same follow-up, frozen before its run) the
    WITNESS TALLY: per id class, the patience values of the
    members whose pt-down move witnesses the nesting — how many
    classes have a finite-pt witness, how many only the INF -> 3
    witness. GUESS: both kinds occur; the split names the
    derivation target.

KILL CRITERIA (observables, meaning weighed after the run)
----------------------------------------------------------
K1 Any T1 trace pair misses: the lemma misreads the engine — the
   rig is dead, no verdicts.
K2 A shiftable member's shift lands out-of-class and fails nesting
   or strict improvement: Lemma T is false as coded — the witness
   prints (world, map, horizon, member).
K3 T1 and the theorem check hold: the exists-form law is PROVED at
   distance <= 2 for every shiftable unfrozen class on every map,
   and the census's pinned/frozen counts plus the T2 histogram
   name exactly what a distance-1 id derivation still owes.

ENGINE
------
E1 the lemma battery (T1).
E2 the census (T2, T3, T4): the domination rig's scope verbatim —
   MR.census_pool at horizons 9/10/12/16, maps id and dbl; per
   off-bottom finite-loss class, typed nesting moves from every
   member, shiftable/frozen status, and the per-member theorem
   check; cells cached per class.
E3 the sq specimens (T5): the three stall classes' shiftable
   members, their shifts, and the distance-2 escape-route anatomy
   (typed two-move paths to every improving class).
E4 the pairwise patience-down scan (E4a-c): id only, census scope,
   every policy against its own single patience-down moves.
Exact big-integer arithmetic for every verdict; ln only in printed
logs. Sequential; estimated run twelve to eighteen minutes (the E2
census and the E4 scan are the drivers); memory trivial (no BLAS
import); exit nonzero on any check failure.

FINDINGS (entered after the run; ALL CHECKS PASS, exit 0, ~15 min,
memory trivial)
----------------------------------------------------------------
F1 THE LEMMA VERIFIES. All 324 battery trace pairs equal under the
   shift, and the per-member theorem check runs clean over every
   census class: ZERO violations — every shiftable member's shift
   either stays in-class or lands nested-pointwise strictly
   better. Lemma T holds as coded.
F2 THE TELESCOPE'S REACH AT SCOPE. Identity: 9,401 off-bottom
   finite-loss classes, 2,800 PINNED (no member with both
   patiences in {1,2,3}), zero frozen — the telescope reaches
   6,601. Doubling: 11,935 classes, 4,215 pinned, 2 frozen —
   reaches 7,718. So the exists-form law is PROVED at cure-graph
   distance two wherever a shiftable member exists with an
   unfrozen window, on every map at once.
F3 THE MOVE MONOPOLY. Nesting cure moves are PATIENCE-DOWN only,
   both maps: id pt-down covers all 9,401 classes (pc-down 3,287);
   dbl pt-down 10,481, pc-down 5,880; the five other move types
   witness nesting in ZERO classes across 21,336. The dbl dent is
   exactly its no-patience-down set (632 = 632). Witness kinds:
   id 9,147 classes have only finite-pt witnesses, 254 only the
   INF -> 3 witness, never both; dbl 10,481 only-finite, 1,454
   with no pt-down witness at all.
F4 THE PAIRWISE BREAK AND THE FROM-INF UNIVERSALITY. E4a's guess
   FALSIFIED: finite pt-down breaks pairwise counted nesting in
   3,225 of 44,040 id pairs (pc-down in 8,274), so the class-level
   law is EXISTS-OVER-MEMBERS with the member choice load-bearing.
   Both from-INF moves are universal at scope: zero counted
   failures in 14,680 pairs each (pt's 508 all-steps failures sit
   entirely before the counted window; pc's has none anywhere) —
   granting a reference where none existed always nests; only
   freshening an existing one can break.
F5 THE SQ STALLS SIT IN THE PINNED RESIDUE. T5's guess FALSIFIED:
   all three stall classes are SINGLETONS at patiences (3,0),
   (3,0), (2,0) — a zero chain patience, so no shiftable member
   and the telescope cannot reach them. Each keeps 3-5 improving
   classes at distance two (hard control) and every printed escape
   route contains a patience move; their measured radius-2 escape
   is NOT the diagonal shift.

THE VERDICT. The exists-form domination question SPLITS BY
DISTANCE. At distance two it is a THEOREM (Lemma T, this cover and
move set, unresourced, any map, any stream): the diagonal patience
shift is an exact one-step delay, nests pointwise for free, its
loss telescopes to the window's endpoints, and it strictly improves
whenever it leaves the class — verified with zero exceptions across
21,336 classes, covering every class with a shiftable member and an
unfrozen window. Two-move lookahead is therefore a PROVED cure at
that shape, and the L4 routing-step case analysis is not resolved
but AVOIDED — the two runs are the same run read one step apart.
At distance one the domination law stays MEASURED, its anatomy now
sharp: nesting is a patience-down monopoly, the exists-choice of
member is load-bearing (F4), the from-INF legs are universal, and
what a derivation still owes is exactly why SOME member's
tree-patience-down always dodges the routing divergence (id, 9,401
of 9,401). The sq stalls sit outside the theorem's reach in the
pinned residue (F5) — consistent with their stallhood.

Run record. THREE runs. The first gated at E3: T5's GUESS was
wired as hard checks (the parent domination rig's own recorded
trap, repeated); the checks were re-scoped to the stated guess
semantics with the stall reproduction and distance-2 escape
existence kept hard, and E3 gained the escape-route anatomy. E4
was added after the first run's E2 histogram printed, with its own
slate frozen before E4 ran; the second run exited 0. The E2w
witness tally was added after the second run, frozen before the
third; no E1/E2 prediction or band was touched at any point. Final
run ALL CHECKS PASS, exit 0, ~15 min.
"""

import sys
from fractions import Fraction

import explore_scale_clock as SC
import explore_stall_tie as ST
import explore_stall_assembly as SA
import explore_stall_maprate as MR

FAILURES = []

def check(name, ok):
    tag = "PASS" if ok else "FAIL"
    print("  [%s] %s" % (tag, name))
    if not ok:
        FAILURES.append(name)

NEARMISS = (1, 2, 64, 1, 2, 1, 64, 1, 1, 2)
FLAGSHIP = (3, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2)
DESIGNED = (3, 1, 1, 6, 1, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 6)

SHIFT_AXIS = (1, 2, 3)

def shiftable(p):
    return p[2] in SHIFT_AXIS and p[3] in SHIFT_AXIS

def down5(p):
    return (p[0], p[1], p[2] - 1, p[3] - 1, p[4])

def counted_cells(J, policy, horizon):
    """Committed cells at counted steps: (lo, hi, length Fraction
    or None)."""
    tr = SC.run_reader(J, policy[:4], horizon)[3]
    out = []
    for n in range(SC.N0, horizon):
        lo, hi = tr[n][2]
        if lo[1] == 0 or hi[1] == 0:
            out.append((lo, hi, None))
        else:
            out.append((lo, hi,
                        Fraction(hi[0], hi[1]) - Fraction(lo[0], lo[1])))
    return out

def frac_le(a, b):
    return a[0] * b[1] <= b[0] * a[1]

def nested_or_equal(cy, cx):
    return frac_le(cx[0], cy[0]) and frac_le(cy[1], cx[1])

def nests_pointwise(cy, cx):
    return all(nested_or_equal(c1[:2], c2[:2])
               for c1, c2 in zip(cy, cx))

# ----------------------------------------------------------------- #
# E1: the lemma battery
# ----------------------------------------------------------------- #

ANCHORS = (("near-miss", NEARMISS, 10),
           ("flagship", FLAGSHIP, 12),
           ("designed", DESIGNED, 16))

def e1_lemma():
    print("\nE1  THE LEMMA BATTERY (trace equality under the shift)")
    pairs = misses = 0
    for wname, digs, horizon in ANCHORS:
        cyls = SC.cylinders(list(digs))
        for mp in ("id", "dbl", "sq"):
            J = SC.images(cyls, mp)[:horizon]
            for st in (0, 1):
                for ss in (0, 1):
                    for pt in SHIFT_AXIS:
                        for pc in SHIFT_AXIS:
                            tr = SC.run_reader(J, (st, ss, pt, pc),
                                               horizon)[3]
                            trd = SC.run_reader(
                                J, (st, ss, pt - 1, pc - 1),
                                horizon)[3]
                            pairs += 1
                            if any(trd[n] != tr[n + 1]
                                   for n in range(horizon - 1)):
                                misses += 1
                                print("  MISS %s %s (%d,%d,%d,%d)"
                                      % (wname, mp, st, ss, pt, pc))
    check("lemma holds on all %d battery pairs" % pairs,
          misses == 0)

# ----------------------------------------------------------------- #
# E2: the census
# ----------------------------------------------------------------- #

MOVE_TYPES = ("st-flip", "ss-flip", "pt-down", "pt-up",
              "pc-down", "pc-up", "sig-diag")

def typed_moves(p):
    """The cure moves of one member, tagged by type."""
    st, ss, pt, pc, d = p
    axis = SC.AX_BASE
    out = [("st-flip", (1 - st, ss, pt, pc, d)),
           ("ss-flip", (st, 1 - ss, pt, pc, d)),
           ("sig-diag", (1 - st, 1 - ss, pt, pc, d))]
    it, ic = axis.index(pt), axis.index(pc)
    if it > 0:
        out.append(("pt-down", (st, ss, axis[it - 1], pc, d)))
    if it < len(axis) - 1:
        out.append(("pt-up", (st, ss, axis[it + 1], pc, d)))
    if ic > 0:
        out.append(("pc-down", (st, ss, pt, axis[ic - 1], d)))
    if ic < len(axis) - 1:
        out.append(("pc-up", (st, ss, pt, axis[ic + 1], d)))
    return out

CENSUS_HORIZONS = (9, 10, 12, 16)
CENSUS_MAPS = ("id", "dbl")

def class_stats(ev, horizon, s, cellcache, sig_of):
    """One off-bottom finite-loss class: typed nesting moves,
    shiftable/frozen status, per-member theorem check. Returns
    (nest_types, has_shiftable, frozen, telescope_improves,
    violations)."""
    J, mem, qloss = ev["J"], ev["mem"], ev["qloss"]
    def cells(sig):
        if sig not in cellcache:
            rep = sorted(mem[sig], key=SC.pol_key)[0]
            cellcache[sig] = counted_cells(J, rep, horizon)
        return cellcache[sig]
    cx = cells(s)
    Lx = Fraction(qloss[s][1][0], qloss[s][1][1])
    nest_types = set()
    pt_witnesses = set()
    for p in mem[s]:
        for mtype, q in typed_moves(p):
            t = sig_of[q]
            if t == s or qloss[t][1][2]:
                continue
            Lt = Fraction(qloss[t][1][0], qloss[t][1][1])
            if Lt < Lx and nests_pointwise(cells(t), cx):
                nest_types.add(mtype)
                if mtype == "pt-down":
                    pt_witnesses.add("INF" if p[2] is None
                                     else "finite")
    has_shiftable = frozen = False
    improves = False
    violations = []
    shift_members = [p for p in mem[s] if shiftable(p)]
    if shift_members:
        has_shiftable = True
        frozen = True
        for p in shift_members:
            t = sig_of[down5(p)]
            if t == s:
                continue
            frozen = False
            Lt = Fraction(qloss[t][1][0], qloss[t][1][1]) \
                if not qloss[t][1][2] else None
            ok = (Lt is not None and Lt < Lx
                  and nests_pointwise(cells(t), cx))
            if ok:
                improves = True
            else:
                violations.append(p)
    return (nest_types, has_shiftable, frozen, improves,
            violations, pt_witnesses)

def e2_census():
    print("\nE2  THE CENSUS (typed nesting moves + telescope "
          "coverage, id/dbl, horizons %s)"
          % ",".join(str(h) for h in CENSUS_HORIZONS))
    hist = {mp: {t: 0 for t in MOVE_TYPES} for mp in CENSUS_MAPS}
    tot = {mp: 0 for mp in CENSUS_MAPS}
    no_nest = {mp: 0 for mp in CENSUS_MAPS}
    pinned = {mp: 0 for mp in CENSUS_MAPS}
    frozen_ct = {mp: 0 for mp in CENSUS_MAPS}
    pinned_no_nest = {mp: 0 for mp in CENSUS_MAPS}
    no_pat_down = {mp: 0 for mp in CENSUS_MAPS}
    wit = {mp: {"finite": 0, "onlyINF": 0, "onlyfinite": 0,
                "both": 0, "none": 0} for mp in CENSUS_MAPS}
    all_violations = []
    for horizon in CENSUS_HORIZONS:
        pool = MR.census_pool(horizon)
        for mp in CENSUS_MAPS:
            for wname, digs in pool:
                ev = SA.evaluate(digs, mp, horizon)
                sig_of = {p: s for s, ps in ev["mem"].items()
                          for p in ps}
                cellcache = {}
                for s in ev["marg"]:
                    nt, sh, fz, imp, viol, ptw = class_stats(
                        ev, horizon, s, cellcache, sig_of)
                    tot[mp] += 1
                    if not ptw:
                        wit[mp]["none"] += 1
                    elif ptw == {"INF"}:
                        wit[mp]["onlyINF"] += 1
                    elif ptw == {"finite"}:
                        wit[mp]["onlyfinite"] += 1
                    else:
                        wit[mp]["both"] += 1
                    if "finite" in ptw:
                        wit[mp]["finite"] += 1
                    for t in nt:
                        hist[mp][t] += 1
                    if not nt:
                        no_nest[mp] += 1
                    if not sh:
                        pinned[mp] += 1
                        if not nt:
                            pinned_no_nest[mp] += 1
                    elif fz:
                        frozen_ct[mp] += 1
                    if not (nt & {"pt-down", "pc-down"}):
                        no_pat_down[mp] += 1
                    for p in viol:
                        all_violations.append(
                            (wname, mp, horizon, s, p))
            print("  h=%-2d %-3s done (classes so far %d)"
                  % (horizon, mp, tot[mp]))
    for mp in CENSUS_MAPS:
        print("  %-3s: %d classes | nesting-move histogram %s"
              % (mp, tot[mp],
                 {t: hist[mp][t] for t in MOVE_TYPES}))
        print("       no-nesting %d | pinned %d (of them "
              "no-nesting %d) | frozen %d | no-patience-down %d"
              % (no_nest[mp], pinned[mp], pinned_no_nest[mp],
                 frozen_ct[mp], no_pat_down[mp]))
        print("       pt-down witness kinds: only-INF %d | "
              "only-finite %d | both %d | none %d"
              % (wit[mp]["onlyINF"], wit[mp]["onlyfinite"],
                 wit[mp]["both"], wit[mp]["none"]))
    for w, mp, h, s, p in all_violations[:12]:
        print("  VIOLATION %s %s h=%d member %s"
              % (w, mp, h, SC.fmt_pol5(p)))
    check("theorem check: zero telescope violations",
          not all_violations)
    check("id no-nesting count reproduces 0 (%d)"
          % no_nest["id"], no_nest["id"] == 0)
    check("dbl no-nesting count reproduces 632 (%d)"
          % no_nest["dbl"], no_nest["dbl"] == 632)
    return hist, tot, no_nest, pinned, frozen_ct, pinned_no_nest

# ----------------------------------------------------------------- #
# E3: the sq specimens
# ----------------------------------------------------------------- #

SQ_SPECIMENS = (
    ("census-2313..", (2, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3), 12),
    ("census-3212..", FLAGSHIP, 12),
    ("designed-16", DESIGNED, 16),
)

def e3_sq():
    print("\nE3  THE SQ STALLS AT DISTANCE 2")
    for tag, digs, horizon in SQ_SPECIMENS:
        ev = SA.evaluate(list(digs), "sq", horizon)
        if not ev["stalls"]:
            check("%s reproduces as a stall" % tag, False)
            continue
        sig_of = {p: s for s, ps in ev["mem"].items() for p in ps}
        qloss = ev["qloss"]
        for s in ev["stalls"]:
            cellcache = {}
            _nt, sh, fz, imp, viol, _ptw = class_stats(
                ev, horizon, s, cellcache, sig_of)
            Lx = Fraction(qloss[s][1][0], qloss[s][1][1])
            print("  %s stall %s (members: %s): shiftable %s, "
                  "telescope improves %s"
                  % (tag, SC.summarize_class(ev["mem"][s]),
                     " ".join(SC.fmt_pol5(p)
                              for p in ev["mem"][s]),
                     sh, imp))
            routes = set()
            esc_classes = set()
            for p in ev["mem"][s]:
                for t1, q in typed_moves(p):
                    z = sig_of[q]
                    if z == s:
                        continue
                    for r in ev["mem"][z]:
                        for t2, q2 in typed_moves(r):
                            w = sig_of[q2]
                            if w in (s, z) or qloss[w][1][2]:
                                continue
                            Lw = Fraction(qloss[w][1][0],
                                          qloss[w][1][1])
                            if Lw < Lx:
                                routes.add((t1, t2))
                                esc_classes.add(w)
            print("    distance-2 escapes: %d improving classes "
                  "via routes %s"
                  % (len(esc_classes), sorted(routes)))
            check("%s: some distance-2 improving class exists"
                  % tag, bool(esc_classes))

# ----------------------------------------------------------------- #
# E4: the pairwise patience-down scan (id)
# ----------------------------------------------------------------- #

def e4_pairwise():
    print("\nE4  THE PAIRWISE PATIENCE-DOWN SCAN (id)")
    axis = SC.AX_BASE
    space = SC.policy_space4(axis)
    tallies = {}   # (move, from_inf) -> [pairs, counted_fail,
                   #                      all_fail]
    for key in (("pt", False), ("pt", True),
                ("pc", False), ("pc", True)):
        tallies[key] = [0, 0, 0]
    anatomies = []
    for horizon in CENSUS_HORIZONS:
        pool = MR.census_pool(horizon)
        for wname, digs in pool:
            J = SC.images(SC.cylinders(list(digs)), "id")[:horizon]
            traces = {p: SC.run_reader(J, p, horizon)[3]
                      for p in space}
            for p in space:
                st, ss, pt, pc = p
                moves = []
                if pt is not None and pt in (1, 2, 3):
                    moves.append((("pt", False),
                                  (st, ss, pt - 1, pc)))
                if pt is None:
                    moves.append((("pt", True), (st, ss, 3, pc)))
                if pc is not None and pc in (1, 2, 3):
                    moves.append((("pc", False),
                                  (st, ss, pt, pc - 1)))
                if pc is None:
                    moves.append((("pc", True), (st, ss, pt, 3)))
                for key, q in moves:
                    tra, trb = traces[p], traces[q]
                    cfail = afail = False
                    first = None
                    for n in range(horizon):
                        lo_a, hi_a = tra[n][2]
                        lo_b, hi_b = trb[n][2]
                        ok = (frac_le(lo_a, lo_b)
                              and frac_le(hi_b, hi_a))
                        if not ok:
                            afail = True
                            if n >= SC.N0:
                                cfail = True
                                if first is None:
                                    first = n
                    t = tallies[key]
                    t[0] += 1
                    t[1] += cfail
                    t[2] += afail
                    if cfail and len(anatomies) < 8:
                        anatomies.append((wname, horizon, p, q,
                                          first))
    for key in sorted(tallies):
        pairs, cf, af = tallies[key]
        print("  %s-down%s: %d pairs, counted-nesting fails %d, "
              "all-steps fails %d"
              % (key[0], " (from INF)" if key[1] else "",
                 pairs, cf, af))
    for wname, horizon, p, q, first in anatomies:
        print("  FAIL %s h=%d %s -> %s first counted non-nest at "
              "step %d" % (wname, horizon, p, q, first))
    print("  E4a verdict line: finite pt-down counted-nesting "
          "failures = %d (the guess said zero; any failure is a "
          "finding, not a gate)" % tallies[("pt", False)][1])
    return tallies

# ----------------------------------------------------------------- #

def main():
    print("THE SHIFT TELESCOPE (unresourced, exact arithmetic)")
    e1_lemma()
    if FAILURES:
        print("\nRIG DEAD AT E1 (K1): %s" % FAILURES)
        return 1
    e2_census()
    e3_sq()
    e4_pairwise()
    print("\n%s" % ("ALL CHECKS PASS" if not FAILURES
                    else "FAILURES: %s" % FAILURES))
    return 1 if FAILURES else 0

if __name__ == "__main__":
    sys.exit(main())
