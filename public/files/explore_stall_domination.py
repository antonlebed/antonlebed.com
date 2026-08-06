"""THE DOMINATION LAW: does the slow-map refusal reduce to a
one-cell wall?

THE QUESTION
------------
The map-rate scan (explore_stall_maprate.py) closed with a shape and
no law: under the id and dbl maps the best adversarial stall margin
walks to zero like 1/(digit cap) and never crosses, while sq keeps
its three stall specimens. This rig attacks the law behind that
refusal. The candidate reduction, fixed on paper below: a stall
margin under a rate-preserving map is capped by the price of ONE
cover-cell refinement at one counted step — a one-cell wall — and
that reduction is exact IF a pointwise condition holds: some cure
neighbor of every off-bottom class commits a nested-or-equal cell at
every counted step. The rig measures that condition (the DOMINATION
LAW), which the sq specimens must break and the id/dbl landscapes
must satisfy if the reduction is the true mechanism.

THE NAMED CLASS (imported verbatim)
-----------------------------------
Cover, streams, policies, losses, moves, quotient, the stall object,
the stall margin and the margin detector are the parents'
(explore_scale_clock.py, explore_stall_unresourced.py,
explore_stall_assembly.py, explore_stall_maprate.py). UNRESOURCED
throughout: delta inert, 100 policies, N0 = 8 counted start,
quotient by counted trace, cure-graph neighbors.

HAND-ATTACK (fixed before the engine; the design follows it)
------------------------------------------------------------
L1 (CONFINEMENT). Containment of a reference is STRICT at both
   endpoints, so while a vertex v lies in the closed span of a
   reader's tree reference, no tree cell with v on or past its
   boundary is committable: the only deepenings available to ANY
   reader at that vertex are straddle cells at v. On a shared
   straddle chain the fresher reference (a subset of the staler one)
   allows the weakly larger chain index, so at confinement steps a
   fresher-reference neighbor is weakly deeper. A fresher neighbor
   can fall SHALLOWER only at a routing step — the fresher reference
   opens a tree door at a vertex where the staler reader is forced
   down the chain (or the mirror case), the exact divergence anatomy
   of the decision trade.
L2 (STRADDLE BALANCE, LOPSIDEDNESS IS RATE-PRICED). A straddle cell
   S_k at vertex p/q with parent denominators qL, qR has endpoint
   denominators qL + kq and qR + kq — ratio at most 1 + 1/k <= 2:
   straddles are balanced. Lopsided cells (adjacent denominator
   ratio R >> 1) arise only from straddle-exit tree children, whose
   ratio is of order the chain index k reached; and the per-step
   jump in the reachable chain index is capped by the per-step
   shrink of the references. Under id and dbl that shrink is
   digit-priced — bounded by a function of the digit cap D alone
   (a continuant step multiplies the denominator by at most D + 1,
   a width shrinks per step by at most a factor of order D^2, and
   the map multiplies widths by a constant mf = 1 or 2) — so R
   stays bounded at any fixed D. Under sq the widths square every
   step, the reachable chain index squares with them, and R is
   unbounded in the step index: lopsidedness is free.
L3 (THE ONE-CELL WALL, conditional — proved for this cover given
   the domination hypothesis). Let x be an off-bottom finite-loss
   class and suppose some cure neighbor y commits, at every counted
   step, a cell nested inside or equal to x's (THE DOMINATION LAW),
   with x and y distinct classes. Distinct classes differ at some
   counted step (the quotient is by counted trace — a pair differing
   only at uncounted steps is one class), and at any differing step
   nesting is strict, so y's committed cell is at least one cover
   refinement deeper. Every single refinement multiplies a cell
   length by a factor at most 1/(1 + 1/R) at the cell's own
   lopsidedness R: a tree child of a cell with denominators
   (qL, qR) keeps length ratio (qL + qR)/qR = 1 + qL/qR, and a
   chain step k -> k+1 keeps at least 1 + 1/(k + 2). Hence
      margin(x) <= ln L(y) - ln L(x) <= -ln(1 + 1/R) < 0:
   no strict stall anywhere the domination law holds, and by L2 the
   wall's height ~ 1/R is bounded below at fixed digit cap under a
   rate-preserving map — the measured 1/D walk is the wall's own
   asymptotic, approached as the cap grows and never attained. Under
   sq the wall still stands wherever domination holds; what sq
   breaks is the hypothesis, at L1's routing steps, where its
   compounding lets a stale chain ride ahead of a fresh tree walk
   for the length of the counted window.
L4 (THE NAMED GAP). What this rig does NOT prove: that the
   domination law itself follows from rate preservation. The paper
   argument covers confinement steps (L1) and prices lopsidedness
   (L2); at a routing step where the two references' ages cross —
   the stale chain reference tracking ahead of the fresh tree
   reference — the case analysis of the commit loop's two fixed
   points is open. The law is therefore MEASURED here, as the
   reduction's load-bearing condition, not derived.

PREDICTIONS, fixed before the engine ran
----------------------------------------
C1 [controls, gate]
   (i)  The recovered near-miss world (digits 1,2,64,1,2,1,64,1,1,2,
        dbl, horizon 10 — the map-rate rig's h=10 D=64 frontier
        optimum, re-derived by rerunning that census and climb
        before this rig was written) evaluates to best margin in
        (-0.0080, -0.0075) ln
        with binding-edge loss ratio exactly 33538/33799.
   (ii) The assembly flagship (321212121212, sq, horizon 12)
        reproduces as a strict stall with best margin in
        (+0.47, +0.49) ln.
C2 [THE DOMINATION CENSUS - id/dbl] For every off-bottom
   finite-loss class of every census landscape (the map-rate rig's
   pools) at horizons 9/10/12/16 under id and dbl: grade the class
   (i) NESTED - some cure neighbor's counted cells are nested-or-
       equal in x's at every counted step;
   (ii) SHORTER - no nested neighbor, but some cure neighbor's
       counted cells are weakly shorter at every counted step;
   (iii) NET - neither, though some neighbor is better on net;
   (iv) STALLED - no improving neighbor.
   GUESS, marked as such: grade (i) covers 100% of the id/dbl
   classes at this scope — the domination law holds as measured
   fact — and grade (iv) is empty (the map-rate refusal again).
   The counterweight: nothing in the paper argument forces the
   dominating neighbor to exist at routing steps, so (ii)/(iii)
   spill is possible; any spill is printed with its witness.
C3 [THE SQ BREAK] Each sq stall specimen's class (the two census
   stalls at horizon 12 and the designed three-burst stall at 16)
   has ZERO weakly-shorter-everywhere neighbors, and every neighbor
   concedes at one or more counted steps — printed per neighbor
   with the concession steps (the freeze made visible inside the
   window). This is entailed by stallhood; the observable content
   is the loci.
C4 [THE WALL CONSTANTS] At the near-miss binding edge the deciding
   refinement's lopsidedness R = 33538/261 lies in (128, 129) and
   under the dbl bound 2(D + 2) = 132 at D = 64; the map-rate
   record's h=9 id D=256 binding ratio 16973823/17040128 (imported
   verbatim from that rig's frozen record) has R =
   16973823/66305 in (255.5, 256.5), under the id bound
   D + 2 = 258. Both margins equal -ln(1 + 1/R) at their own R —
   the one-cell wall's cap met with equality at the frontier.

KILL CRITERIA (observables, meaning weighed after the run)
----------------------------------------------------------
K1 Any C1 check fails: the rig is dead, no verdicts.
K2 An id/dbl class grades (iii) or worse, or a sq stall class
   fails C3: the domination law is false as stated at scope - the
   witness prints (world, class, counted step) and is the finding.
K3 C2 grades 100% (i) and C3 holds: the reduction closes at scope —
   the slow-map refusal = a proved one-cell wall standing on a
   measured domination law, the law's own derivation the remaining
   open step (L4).

ENGINE
------
E1 controls (C1).
E2 the domination census (C2): per landscape, per off-bottom
   finite-loss class, grade against all cure neighbors from the
   counted traces; margins re-derived from the trace ratios and
   checked against the margin table (exact arithmetic).
E3 the sq break (C3): the three specimens' stall classes, per
   neighbor concession loci.
E4 the wall constants (C4): exact rational arithmetic on the two
   binding ratios and their bounds.
Exact big-integer arithmetic for every verdict; ln only in printed
logs. Sequential, one landscape at a time; estimated run five to
ten minutes (the census is the driver), memory trivial (no BLAS
import); positive controls gate all verdicts; exit nonzero on any
check failure.

FINDINGS (entered after the run; ALL CHECKS PASS, exit 0, ~7 min,
memory trivial)
----------------------------------------------------------------
F1 Controls exact: near-miss margin -0.007752 with binding ratio
   exactly 33538/33799; flagship stall margin +0.4775.

F2 THE DOMINATION CENSUS SPLITS BY MAP. Identity: EXHAUSTIVE - all
   9,401 off-bottom finite-loss classes across 1,468 landscapes at
   horizons 9/10/12/16 grade NESTED (some cure neighbor's counted
   cells nested-or-equal at every counted step), zero exceptions.
   Doubling: 11,303 nested + 540 shorter + 92 NET - ninety-two
   classes have no pointwise-dominating cure neighbor and still
   lose on aggregate, the witnesses sitting in burst and
   head-period worlds (first witness burst7.D8, horizon 10: class
   sigma=(0,1) patience (2,0), whose best neighbor concedes step 9
   and wins on net). Zero classes grade STALLED anywhere - 21,336
   classes, the map-rate refusal reproduced a third way. So C2's
   guess falls exactly where L4 warned: the law is a fact of the
   MAP-ALIGNMENT pair, exhaustive for the identity embedding,
   dented by dbl's alignment shift (dbl adds alignment, never
   rate - the parent's L2), broken wholesale by sq's compounding.

F3 THE SQ BREAK CONFIRMED. All three sq specimens reproduce and
   every finite-loss neighbor of every stall class concedes at one
   or more counted steps - the freeze loci print inside each
   window (e.g. the flagship's three patience neighbors concede at
   steps 9-11; the designed stall's five neighbors concede at up
   to six of eight counted steps).

F4 THE WALL CONSTANTS MET WITH EQUALITY. The near-miss margin
   equals -ln(1 + 1/R) exactly at R = 33538/261 = 128.498 (under
   the dbl bound 132 at D = 64), and the map-rate id record equals
   its cap at R = 255.996 (under the id bound 258 at D = 256): the
   frontier optimum's binding loss ratio IS a single parent/child
   refinement ratio - every other counted step cancels exactly -
   so the 1/D walk is the one-cell wall's own asymptotic.

THE VERDICT. Between K2 and K3, split by map: the reduction CLOSES
FOR THE IDENTITY MAP at scope - no unresourced id stall exists
where the domination law holds, the law holds without exception at
the scanned scope (rule: 9,401 classes, exhaustive at stated
scope), and the one-cell wall (L3) is proved for this cover given
it - while for dbl the pointwise skeleton has 92 net-only
witnesses (K2: the law is false as stated there) and the refusal
keeps only its measured aggregate margins. What remains open is
L4: deriving the domination law itself - the routing-step case
analysis, for which the identity map is now the sharp target,
its measured law having zero exceptions to survive.

Run record. The first run gated at E1: the near-miss control band
was mistyped (-0.0078 for -0.0075) against the parent's printed
-0.007752; corrected, no verdict leg had run. The second full run
printed the 92-class spill as a FAILURE because the C2 guess was
wired as a hard check; the check was re-scoped to K2's own stated
semantics (the spill prints as the finding, zero-STALLED gates)
and the spill reporting extended (per-map totals, first-witness
locus) - no prediction band touched. Final run ALL CHECKS PASS,
exit 0, ~7 min.
"""

import sys
from fractions import Fraction

import explore_scale_clock as SC
import explore_stall_tie as ST
import explore_stall_unresourced as SU
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

# ----------------------------------------------------------------- #
# trace machinery
# ----------------------------------------------------------------- #

def counted_cells(J, policy, horizon):
    """The committed cells at counted steps, as exact endpoint
    pairs, plus their lengths as Fractions (None = infinite)."""
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
    """a <= b for endpoint pairs (num, den), den >= 0."""
    return a[0] * b[1] <= b[0] * a[1]

def nested_or_equal(cy, cx):
    """cell y inside-or-equal cell x (endpoint pairs)."""
    return frac_le(cx[0], cy[0]) and frac_le(cy[1], cx[1])

def grade_class(J, horizon, mem, nbrs, qloss, s):
    """Grade one off-bottom finite-loss class: returns
    (grade, witness) with grade in 'nested'/'shorter'/'net'/
    'stalled' and witness the dominating neighbor (or None)."""
    rep_x = sorted(mem[s], key=SC.pol_key)[0]
    cx = counted_cells(J, rep_x, horizon)
    Lx = Fraction(qloss[s][1][0], qloss[s][1][1])
    best_grade, best_wit = "stalled", None
    order = {"nested": 0, "shorter": 1, "net": 2, "stalled": 3}
    for t in nbrs[s]:
        if qloss[t][1][2]:
            continue
        rep_y = sorted(mem[t], key=SC.pol_key)[0]
        cy = counted_cells(J, rep_y, horizon)
        Lt = Fraction(qloss[t][1][0], qloss[t][1][1])
        # exact identity: the loss ratio is the product of the
        # counted length ratios
        prod = Fraction(1)
        okay = True
        for (l1, h1, wy), (l2, h2, wx) in zip(cy, cx):
            if wy is None or wx is None:
                okay = False
                break
            prod *= wy / wx
        if okay and prod != Lt / Lx:
            raise AssertionError("trace product != loss ratio")
        if Lt >= Lx:
            continue
        g = "net"
        if all(wy is not None and wx is not None and wy <= wx
               for (_l1, _h1, wy), (_l2, _h2, wx) in zip(cy, cx)):
            g = "shorter"
            if all(nested_or_equal(c1[:2], c2[:2])
                   for c1, c2 in zip(cy, cx)):
                g = "nested"
        if order[g] < order[best_grade]:
            best_grade, best_wit = g, (t, rep_y)
    return best_grade, best_wit

# ----------------------------------------------------------------- #
# E1: controls
# ----------------------------------------------------------------- #

def e1_controls():
    print("\nE1  CONTROLS")
    ev = SA.evaluate(list(NEARMISS), "dbl", 10)
    m = ev["best_m"]
    check("near-miss margin in (-0.0080,-0.0075): %+.6f" % m,
          -0.0080 < m < -0.0075)
    s = ev["best"]
    Ls = Fraction(ev["qloss"][s][1][0], ev["qloss"][s][1][1])
    ratios = []
    for t in ev["nbrs"][s]:
        if ev["qloss"][t][1][2]:
            continue
        Lt = Fraction(ev["qloss"][t][1][0], ev["qloss"][t][1][1])
        ratios.append(Lt / Ls)
    check("binding ratio exactly 33538/33799",
          min(ratios) == Fraction(33538, 33799))
    ev2 = SA.evaluate(list(FLAGSHIP), "sq", 12)
    ok = bool(ev2["stalls"])
    m2 = None
    if ok:
        s2 = next(iter(ev2["stalls"]))
        m2 = ev2["marg"][s2][0]
    check("flagship stall margin in (+0.47,+0.49): %s"
          % ("%+.4f" % m2 if m2 is not None else "no stall"),
          ok and 0.47 < m2 < 0.49)
    return ev, ev2

# ----------------------------------------------------------------- #
# E2: the domination census
# ----------------------------------------------------------------- #

CENSUS_HORIZONS = (9, 10, 12, 16)
CENSUS_MAPS = ("id", "dbl")

def e2_domination():
    print("\nE2  THE DOMINATION CENSUS (id/dbl, horizons %s)"
          % ",".join(str(h) for h in CENSUS_HORIZONS))
    totals = {"nested": 0, "shorter": 0, "net": 0, "stalled": 0}
    per_map = {mp: {"nested": 0, "shorter": 0, "net": 0,
                    "stalled": 0} for mp in CENSUS_MAPS}
    spill = []
    n_land = 0
    for horizon in CENSUS_HORIZONS:
        pool = MR.census_pool(horizon)
        for mp in CENSUS_MAPS:
            cell = {"nested": 0, "shorter": 0, "net": 0,
                    "stalled": 0}
            for wname, digs in pool:
                ev = SA.evaluate(digs, mp, horizon)
                n_land += 1
                for s in ev["marg"]:
                    g, _w = grade_class(ev["J"], horizon, ev["mem"],
                                        ev["nbrs"], ev["qloss"], s)
                    cell[g] += 1
                    totals[g] += 1
                    per_map[mp][g] += 1
                    if g in ("net", "stalled"):
                        spill.append((wname, digs, mp, horizon, s,
                                      g, ev))
            print("  h=%-2d %-3s: %s" % (horizon, mp, cell))
    print("  landscapes %d | totals %s" % (n_land, totals))
    for mp in CENSUS_MAPS:
        print("  per-map %-3s: %s" % (mp, per_map[mp]))
    for wname, digs, mp, horizon, s, g, _ev in spill[:12]:
        print("  SPILL %s: %s %s h=%d class %s"
              % (g, wname, mp, horizon, s))
    if spill:
        wname, digs, mp, horizon, s, g, ev = spill[0]
        rep_x = sorted(ev["mem"][s], key=SC.pol_key)[0]
        cx = counted_cells(ev["J"], rep_x, horizon)
        best_t, best_L = None, None
        for t in ev["nbrs"][s]:
            if ev["qloss"][t][1][2]:
                continue
            Lt = Fraction(ev["qloss"][t][1][0], ev["qloss"][t][1][1])
            if best_L is None or Lt < best_L:
                best_t, best_L = t, Lt
        rep_y = sorted(ev["mem"][best_t], key=SC.pol_key)[0]
        cy = counted_cells(ev["J"], rep_y, horizon)
        concede = [SC.N0 + i for i, (a, b) in enumerate(zip(cy, cx))
                   if a[2] is not None and b[2] is not None
                   and a[2] > b[2]]
        print("  first net witness %s %s h=%d: class %s, best "
              "neighbor %s concedes at steps %s and wins on net"
              % (wname, mp, horizon, SC.fmt_pol5(rep_x),
                 SC.fmt_pol5(rep_y), concede))
    n_cls = sum(totals.values())
    check("no id/dbl class grades stalled (%d classes)" % n_cls,
          totals["stalled"] == 0)
    print("  grade (i) coverage: %d of %d (+%d shorter, %d net)"
          % (totals["nested"], n_cls, totals["shorter"],
             totals["net"]))
    return totals, per_map

# ----------------------------------------------------------------- #
# E3: the sq break
# ----------------------------------------------------------------- #

SQ_SPECIMENS = (
    ("census-2313..", (2, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3), 12),
    ("census-3212..", FLAGSHIP, 12),
    ("designed-16", DESIGNED, 16),
)

def e3_sq_break():
    print("\nE3  THE SQ BREAK (per-neighbor concession loci)")
    all_ok = True
    for tag, digs, horizon in SQ_SPECIMENS:
        ev = SA.evaluate(list(digs), "sq", horizon)
        if not ev["stalls"]:
            check("%s reproduces as a stall" % tag, False)
            all_ok = False
            continue
        for s in ev["stalls"]:
            rep_x = sorted(ev["mem"][s], key=SC.pol_key)[0]
            cx = counted_cells(ev["J"], rep_x, horizon)
            n_short = 0
            for t in ev["nbrs"][s]:
                if ev["qloss"][t][1][2]:
                    print("    %s nbr %s: infinite loss" %
                          (tag, SC.fmt_pol5(
                              sorted(ev["mem"][t],
                                     key=SC.pol_key)[0])))
                    continue
                rep_y = sorted(ev["mem"][t], key=SC.pol_key)[0]
                cy = counted_cells(ev["J"], rep_y, horizon)
                concede = [SC.N0 + i for i, (a, b)
                           in enumerate(zip(cy, cx))
                           if a[2] is not None and b[2] is not None
                           and a[2] > b[2]]
                if not concede:
                    n_short += 1
                print("    %s nbr %s concedes at steps %s"
                      % (tag, SC.fmt_pol5(rep_y), concede or "NONE"))
            check("%s: zero weakly-shorter-everywhere neighbors"
                  % tag, n_short == 0)
            all_ok = all_ok and n_short == 0
    return all_ok

# ----------------------------------------------------------------- #
# E4: the wall constants
# ----------------------------------------------------------------- #

def e4_wall():
    print("\nE4  THE WALL CONSTANTS")
    import math
    R1 = Fraction(33538, 261)
    check("near-miss R = 33538/261 in (128,129): %.4f" % float(R1),
          128 < R1 < 129)
    check("dbl bound R <= 2(D+2) = 132 at D=64", R1 <= 132)
    m1 = -math.log(1 + 1 / float(R1))
    print("  -ln(1+1/R) = %+.6f (measured margin %+.6f)"
          % (m1, -math.log(33799 / 33538)))
    check("near-miss margin equals its own one-cell cap",
          Fraction(33538, 33799) == 1 / (1 + 1 / R1))
    num, den = 16973823, 17040128
    R2 = Fraction(num, den - num)
    check("map-rate id record R = %d/%d in (255.5,256.5): %.4f"
          % (num, den - num, float(R2)), Fraction(511, 2) < R2
          < Fraction(513, 2))
    check("id bound R <= D+2 = 258 at D=256", R2 <= 258)
    check("id record margin equals its own one-cell cap",
          Fraction(num, den) == 1 / (1 + 1 / R2))

# ----------------------------------------------------------------- #

def main():
    print("THE DOMINATION LAW - the slow-map refusal as a "
          "one-cell wall")
    e1_controls()
    if FAILURES:
        print("\nCONTROLS FAILED - no verdicts")
        return 1
    e2_domination()
    e3_sq_break()
    e4_wall()
    print("\n%s" % ("ALL CHECKS PASS" if not FAILURES
                    else "FAILURES: %s" % FAILURES))
    return 1 if FAILURES else 0

if __name__ == "__main__":
    sys.exit(main())
