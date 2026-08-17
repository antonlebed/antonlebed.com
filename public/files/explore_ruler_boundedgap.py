"""explore_ruler_boundedgap.py -- CAN THE EXACTNESS THRESHOLD BE RAISED
OFF THE WEIGHT LATTICE? The anchored gap: the same criterion with the
lattice's g replaced by the minimum over the coefficient box the
certificate's own sizes pin.

(The cells, the certificate, the exhaustive optimum, the exact solver
and the surplus identity are all IMPORTED from explore_ruler_barecell.py,
explore_ruler_exchange.py, explore_ruler_setvalued.py,
explore_ruler_optimum.py and explore_ruler_surplus.py. What is new here
is one substitution in the criterion's last step, the witness machinery
that makes it computable, and the census that says what it buys.)

THE QUESTION. The surplus criterion proves cert = OPT whenever D/t* < g,
g being the smallest positive gap of the lattice the atom weights
generate. That test decides 7,643 of the 13,678 exact designed
unequal-weight cells and dies outright on the geometric family, where
fifteen atoms drive g to 1e-21 and the walk's one live rung (W-10,
certificate exact, D/t* = 7.008e-4 against g = 1.259e-15) is missed by
eleven orders. But g prices cert - OPT as an ARBITRARY lattice element,
and it is not one: cert - OPT = sum_r (s_r - s'_r) w_r over the
certificate's sizes s_r and some optimal rule's sizes s'_r. Can the
threshold be raised to the minimum over THAT set, and does the raise
reach W-10?

WHOSE VOCABULARY. The surplus rig's own: ATOM, LEVEL, TIED BLOCK,
SURPLUS D, ROOM D/t*, COST LATTICE and its gap g keep
explore_ruler_surplus.py's senses. New here: the COEFFICIENT BOX at a
size vector s is the set of integer vectors c with c_r in
[s_r - k, s_r] per atom -- k + 1 consecutive values, since a rule's size
at an atom lies in [0, k] (the range exhaustive_optimum itself searches;
re-derived from the engine, where a first pricing had used the
SYMMETRIC box [-k, k] of (2k+1)^M vectors -- the anchoring at the
certificate's sizes is what shrinks 7^15 to 4^15). The ANCHORED GAP
g_A(s) is the smallest positive value of sum_r c_r w_r over the box.

THE HAND ATTACK, worked on paper before any engine code.

FIRST, THE RAISED CRITERION. Any optimal rule has per-atom sizes s'_r in
[0, k] (its cost depends on sizes alone), so cert - OPT lies in the
box's value set, and cert >= OPT always. If cert != OPT then
0 < cert - OPT, so cert - OPT >= g_A(s); with the cap
cert - OPT <= D/t* that gives

    D / t*  <  g_A(s)   =>   cert = OPT.

The proof is the parent's with one substitution, and the box's value
set is a subset of the lattice difference group, so g_A(s) >= g always:
every cell the lattice criterion decides, this one decides. The raise
is monotone and can only extend the reach.

SECOND, THE ALGEBRA OF THE STATISTIC. g_A(s) is a minimum over a finite
set; it is well-defined iff the box contains a positive value, and it
does at every cell with cert > 0: c = s itself (s' = 0) gives
sum s_r w_r = cert. The rig asserts cert > 0 rather than assuming it.
Both sides of the comparison are exact Fractions in the cell's
integerized scale (integerize's den), so nothing here can blow up or
round; the box minimum is a minimum of integers.

THIRD, THE BOX DEPENDS ON THE WITNESS. The tied fill's value is unique
but the subset achieving it need not be, and different witnesses give
different s and different boxes. Each box yields a VALID criterion for
the same cert (cost depends only on the fill value), so the rig scores
the one witness fill_witness returns and claims nothing about others.

FOURTH, WHAT THE RAISE CAN REACH AT W-10, bounded by hand. A
second-difference vector (1, -2, 1) at atoms r, r+1, r+2 has value
theta^r (1-theta)^2 x (an atom-0 weight), about 1.26e-3 x 0.9^r of
total mass at theta = 9/10 -- under the 7.008e-4 threshold from r >= 6
on -- while a first difference (1, -1) is 1.26e-2 x 0.9^r and never
gets under it within fifteen atoms. Whether those vectors sit IN the
box depends on the certificate's sizes ((1,-2,1) needs s_{r+1} <= 1
with its neighbours >= 1, at k = 3), so the verdict is genuinely the
computation's. Two heuristics disagree: counting (4^15 sums spread
over a span three times the total mass puts the typical spacing near
1e-9 of it) says the minimum sits far below the threshold; the digit
obstruction (hitting a SMALL value forces one residue mod 9 per digit
and the box offers 4 of 9) says small values may be unreachable. The
slate freezes the counting side and lets the rig decide.

FIFTH, WHERE THE EXACT MINIMUM IS OUT OF REACH, A WITNESS STILL
DECIDES THE NEGATIVE. At TILT-4-WIDE the box is 5^105 and no
meet-in-the-middle touches it. But a NO-FIRE verdict needs only ONE box
vector with 0 < value < D/t*, since g_A is a minimum: a windowed search
over box vectors supported on w consecutive atoms (5^w per window) can
prove the criterion dead there without the minimum. A FIRE verdict has
no such shortcut and stays REFUSED at that size.

THE SLATE, frozen before any engine code.

PREDICTIONS.
  P1. g_A >= g at every cell scored, and the anchored criterion fires
      at every cell the lattice one fires at. (Derivation; a single
      violation refutes the box argument or the arithmetic.)
  P2. The anchored criterion fires at ZERO cells where cert > OPT.
      (Derivation.)
  P3. On the /20 sweep the raise buys FEW cells: fewer than 500 of the
      6,035 exact unequal-weight cells the lattice criterion misses.
      (The /20 grid's minimal positive combinations need only small
      coefficients, which the boxes mostly admit -- so g_A = g at most
      cells. A guess at the size; the census is the number.)
  P4. At W-10 the anchored minimum stays BELOW its D/t* of 7.008e-4:
      no fire, and the criterion's death at geometric weights is
      structural rather than a loose constant. (The counting heuristic
      of FOURTH; the digit obstruction points the other way.)
  P5. W-25 (= TILT-3) does NOT fire. Its certificate OVERSTATES, so a
      firing there is not a miss but a refutation (K-A).
  P6. At TILT-4-WIDE the windowed search finds a witness under its
      D/t* of 4.349e-6, so the anchored criterion provably cannot fire
      there either -- the exactness it misses stays missed, now with a
      certificate of the miss rather than a lattice too fine to read.

KILLS, as observables rather than inferences -- what the rig prints,
with what it would mean weighed only after the run.
  K-A. Any nonzero count of cells where the anchored criterion fires
       and cert > OPT.
  K-B. Any nonzero count of cells with g_A < g, or firing the lattice
       criterion but not the anchored one.
  K-C. Any parity failure: brute-force box minimum != meet-in-the-middle
       box minimum at an M = 3 cell, or a rebuilt certificate cost
       differing from the parent's exact-fill certificate.
  K-D. Any ring or walk cell where the solver returns CAPPED or the
       tied block is unusable. A refusal with its size named, not a
       result.

CONTROLS, run and read BEFORE any kill or survive result, each printing
HOW MANY cases it exercised.
  C1 (POSITIVE, ON THE AXIS THE ARM VARIES). The anchored criterion
     must fire at unequal-weight cells the lattice one misses -- counted
     against the lattice baseline recomputed in the same pass, so the
     gain is read against a number produced by this run and not quoted
     from the parent.
  C2 (WITNESS). At every ring and walk cell the certificate is rebuilt
     from the tied witness: its cost must equal the solver's cert, its
     coverage must reach the target, and every size must lie in [0, k].
     The box argument is ABOUT these sizes, so the criterion is only as
     real as this rebuild.
  C3 (TRUTH). check_truth / ring_truth at every generated cell, in
     Fraction.
  C4 (PARITY, TWO ROUTES). At every M = 3 cell, g_A by 64-vector brute
     force and by meet-in-the-middle, compared exactly. At every M = 15
     cell, the windowed-witness minimum must be >= the exact
     meet-in-the-middle minimum.

THE ARMS.
  1. The seven bare cells: g against g_A, identity of reach (P1, C4).
  2. The 19,125-cell designed sweep plus the 125 equal-weight cells:
     the anchored census against the exhaustive optimum and the lattice
     baseline (P1, P2, P3, C1, C3, C4).
  3. The four ring cells, the solver supplying OPT: g_A exact at the
     three M = 15 cells, the windowed witness at TILT-4-WIDE (P1, P6,
     C2, K-D).
  4. The theta walk, nine rungs at TILT-3's ring shape: g_A exact by
     meet-in-the-middle, the live question at W-10 (P4, P5, C2, C4).

RESOURCE NOTE. Exact integer arithmetic throughout, no numpy. The sweep
re-runs the parent's 19,250 cells with an added witness rebuild and two
64-vector box scans per cell; the ring and walk arms re-run solve(),
whose peak is TILT-4-WIDE's truth at about 184 MB in the parent, plus
meet-in-the-middle at 4^8 + 4^7 sums per M = 15 cell and a 5^6-per-window
scan at TILT-4-WIDE. Estimated three to six minutes wall (the sweep's
Fraction work dominates), under the 512 MB default, run under memwatch;
the run record below carries what it cost.

RUN RECORD (wall 16.3s, peak working set 41.1 MB against the 512 MB
default under memwatch). The FIRST launch was KILLED by memwatch at 523
MB commit: _box_sums kept duplicate values, and DEAD-7's fifteen equal
weights at k = 7 make an 8^8 half of duplicate bigints. The fix
deduplicates at every accumulation step -- a minimum needs values, not
multiplicity -- and every verdict below is read off the green rerun,
whose peak is 41.1 MB. 19,270 scorings over 19,269 distinct cells: 7
bare, 19,125 designed unequal-weight, 125 equal-weight, 4 ring, 9 walk
(TILT-3 appears again as the walk's n = 25 rung and reproduces its ring
row, figure for figure).

CONTROLS, before any verdict. C3 truth failures 0. K-C parity failures
0 -- brute force and meet-in-the-middle agree at all 19,250 sweep cells.
C2 holds at every ring and walk cell: sizes all in [0, k], rebuilt cost
equal to the solver's certificate. C4 holds at every M = 15 cell: the
window witness is >= the exact minimum everywhere.

P1 HOLDS. Zero monotonicity violations: g_A >= g at every cell scored,
and every lattice firing is an anchored firing. At all seven bare cells
and all 125 equal-weight cells g_A = g exactly -- the anchoring buys
nothing where the lattice was already coarse.
P2 HOLDS. The anchored criterion fires at ZERO of the 5,447 overstating
sweep cells and zero of the walk's eight.
P3 HOLDS, at 492 gained. The anchored criterion decides 8,135 of the
13,678 exact unequal-weight cells against the lattice's 7,643 -- 59.5%
against 55.9% -- with g_A > g at 1,371 cells, so just over a third of
the raised thresholds cross their own cell's room.
P5 HOLDS. W-25 (= TILT-3, certificate overstating) does not fire.
P6 HOLDS. TILT-4-WIDE: exact box REFUSED at 5^105; the width-6 window
finds a box vector worth 1.832e-07 against a D/t* of 4.349e-06, so the
anchored criterion PROVABLY cannot fire there -- the miss now carries a
witness instead of a lattice too fine to read.

P4 HOLDS, AND THE DEATH AT GEOMETRIC WEIGHTS IS STRUCTURAL. The walk,
with the exact anchored gap per rung:

  cell     theta      D/t*         g       g_A  cert exact  fires A
  W-3        2/3  5.314e-03 6.985e-08 6.985e-08  False       False
  W-5        4/5  5.920e-03 3.396e-11 4.789e-09  False       False
  W-10      9/10  7.008e-04 1.259e-15 1.852e-09  True        False
  W-25     24/25  2.794e-02 2.345e-21 1.784e-09  False       False
  W-50     49/50  5.380e-02 1.253e-25 9.120e-10  False       False
  W-100   99/100  2.518e-02 7.146e-30 2.049e-10  False       False
  W-200  199/200  3.537e-02 4.213e-34 7.555e-10  False       False
  W-400  399/400  4.259e-02 2.527e-38 4.717e-11  False       False
  W-1000 999/1000 7.202e-03 6.713e-44 1.203e-12  False       False

At the one live rung, W-10, the anchoring raises the threshold SIX
orders -- 1.259e-15 to 1.852e-09 -- and the room is 7.008e-04, so the
criterion still misses by more than five orders. The raise is real and
it is not enough, and the two failures are now different in kind: the
lattice gap collapses without bound as theta rises (1e-08 to 1e-44
across the ladder), while the anchored gap DECOUPLES from it,
declining five orders (7e-08 to 1e-12, one inversion at n = 200) and
sitting at least 4.8 orders under every rung's room. The box always
contains a cheap positive combination: the width-6 window witness
ALONE already lands under every rung's room -- 5.421e-04 against
W-10's 7.008e-04 at the tightest -- so small-support
difference-shaped vectors (the (1,-2,1) family of FOURTH, whose value
scales as (1-theta)^2 theta^r) suffice to kill the criterion at every
rung, whatever the certificate's sizes turn out to be. The counting
heuristic won and the digit obstruction lost: at geometric weights no
threshold read off the certificate's own coefficient box reaches the
surplus, and the criterion's boundary is a WEIGHT-FAMILY property, not
a loose constant of the lattice argument.

WHAT THIS LEAVES OPEN. The anchored gap's slow decline on the walk
(7e-08 at n = 3 down to 1e-12 at n = 1000) is measured, not derived;
the window evidence points at a closed form over difference vectors
weighted (1-theta)^j theta^r, and nothing here derives it. And the 492
gained cells are 8.2% of what the lattice missed: which grid geometries
the anchoring helps is read off one /20 grid only.
"""

import os
import sys
import time
from bisect import bisect_right
from fractions import Fraction

os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from explore_ruler_setvalued import CELLS, Cell  # noqa: E402
from explore_ruler_barecell import (  # noqa: E402
    BARE, exhaustive_optimum, operative_level,
)
from explore_ruler_exchange import (  # noqa: E402
    ALPHA, EQUAL, ROWS, WEIGHTS, check_truth, make_cell,
)
from explore_ruler_optimum import (  # noqa: E402
    TiedBlock, integerize, solve,
)
from explore_ruler_surplus import LADDER, lattice_gap, ring_truth  # noqa: E402

F = Fraction


# ------------------------------------------------ the certificate's sizes

def cert_sizes(cell, alpha):
    """The exact-fill certificate as a SIZE VECTOR, plus its scale.

    Rebuilds what control_C6 rebuilds -- the strictly-above pairs plus
    the tied items the subset sum picked -- but keeps the per-atom
    counts, which is what the box argument is about. Returns
    (sizes, cert_int, room, den, level) with cert_int the certificate's
    cost in integerize's scale and room = D/t* as a Fraction, or None
    where the tied block is past its sum cap (K-D).
    """
    cost, cover, target, den = integerize(cell, alpha)
    level, _m, _c, _s = operative_level(cell, alpha)
    sizes = [0] * cell.M
    above_cost = above_cov = 0
    tied = []
    for r in range(cell.M):
        for j in range(cell.k):
            ratio = F(cover[r][j], cost[r])
            if ratio > level:
                sizes[r] += 1
                above_cost += cost[r]
                above_cov += cover[r][j]
            elif ratio == level:
                tied.append((r, cost[r]))
    blk = TiedBlock([ct for _r, ct in tied])
    if not blk.usable:
        return None
    got = blk.fill_witness(F(target - above_cov) / level)
    if got is None:
        return None
    fill, idx = got
    for i in idx:
        sizes[tied[i][0]] += 1
    cert_int = above_cost + fill
    assert cert_int > 0, (cell.name, "a zero-cost certificate")
    room = (F(above_cov - target) + level * fill) / (level * den)
    return sizes, cert_int, room, den, level


# ------------------------------------------------------ the anchored gap

def _box_sums(cost, sizes, k, lo, hi):
    """Every DISTINCT value of sum c_r cost[r] over c_r in
    [sizes_r - k, sizes_r], atoms lo..hi-1. Deduplicated at every step:
    a minimum needs the values and not their multiplicity, and repeated
    weights (DEAD-7 carries fifteen equal ones at k = 7, an 8^8 half)
    otherwise commit gigabytes of duplicate bigints."""
    sums = {0}
    for r in range(lo, hi):
        opts = [c * cost[r] for c in range(sizes[r] - k, sizes[r] + 1)]
        sums = {s + o for s in sums for o in opts}
    return list(sums)

def anchored_gap_mim(cost, sizes, k, M):
    """min positive box value by meet-in-the-middle, exact in integers."""
    half = M // 2
    a = _box_sums(cost, sizes, k, 0, half)
    b = sorted(_box_sums(cost, sizes, k, half, M))
    best = None
    for x in a:
        i = bisect_right(b, -x)
        if i < len(b):
            v = x + b[i]
            if best is None or v < best:
                best = v
    return best

def anchored_gap_brute(cost, sizes, k, M):
    """The same minimum by one flat scan -- the parity route at M = 3."""
    best = None
    for v in _box_sums(cost, sizes, k, 0, M):
        if v > 0 and (best is None or v < best):
            best = v
    return best

def window_witness(cost, sizes, k, M, width):
    """min positive box value over vectors supported on `width`
    consecutive atoms -- an UPPER bound on the anchored gap, which is
    all a no-fire verdict needs where the full box is out of reach."""
    best = None
    for lo in range(M - width + 1):
        for v in _box_sums(cost, sizes, k, lo, lo + width):
            if v > 0 and (best is None or v < best):
                best = v
    return best


# --------------------------------------------------------------- the arms

def score(cell):
    """One cell: lattice gap, anchored gap (both routes at M = 3), the
    two criteria's verdicts. Exact throughout."""
    got = cert_sizes(cell, ALPHA)
    if got is None:
        return None
    sizes, cert_int, room, den, level = got
    cost, _cover, _target, den2 = integerize(cell, ALPHA)
    assert den == den2
    g = lattice_gap(cell)
    mim = anchored_gap_mim(cost, sizes, cell.k, cell.M)
    gA = None if mim is None else F(mim, den)
    return dict(sizes=sizes, cert=F(cert_int, den), room=room, g=g,
                gA=gA, cost=cost, den=den,
                fires_g=room < g,
                fires_A=gA is not None and room < gA)


def arm_sweep(weights, tag):
    out = dict(seen=0, bad_truth=0, bad_parity=0, bad_mono=0,
               exact=0, inexact=0,
               fires_g=0, fires_A=0, fires_g_at_exact=0,
               fires_A_at_exact=0, fires_A_at_inexact=0,
               gained=0, raised=0)
    for rows in ROWS:
        for wts in weights:
            cell = make_cell(tag, rows, wts)
            if not check_truth(cell):
                out["bad_truth"] += 1
                continue
            m = score(cell)
            out["seen"] += 1
            brute = anchored_gap_brute(m["cost"], m["sizes"], cell.k,
                                       cell.M)
            if brute is None or F(brute, m["den"]) != m["gA"]:
                out["bad_parity"] += 1
            if m["gA"] < m["g"] or (m["fires_g"] and not m["fires_A"]):
                out["bad_mono"] += 1
            if m["gA"] > m["g"]:
                out["raised"] += 1
            opt = exhaustive_optimum(cell, ALPHA)
            if opt is None:
                continue
            is_exact = opt == m["cert"]
            out["exact" if is_exact else "inexact"] += 1
            if m["fires_g"]:
                out["fires_g"] += 1
                if is_exact:
                    out["fires_g_at_exact"] += 1
            if m["fires_A"]:
                out["fires_A"] += 1
                if is_exact:
                    out["fires_A_at_exact"] += 1
                else:
                    out["fires_A_at_inexact"] += 1
                if not m["fires_g"]:
                    out["gained"] += 1
    return out


def report_solved(cell, m, s, mim_witness_max_M=15):
    """One ring or walk cell: both gaps, both verdicts, C2's rebuild."""
    opt = s.opt
    opts = "CAPPED" if opt is None else "%.7f" % float(opt)
    gA = "--" if m["gA"] is None else "%9.3e" % float(m["gA"])
    print("  %-12s %4d %3d %10s %9.3e %9.3e %9s  fires g %-5s A %-5s"
          % (cell.name, cell.M, cell.k, opts, float(m["room"]),
             float(m["g"]), gA, m["fires_g"], m["fires_A"]))
    sizes_ok = all(0 <= v <= cell.k for v in m["sizes"])
    cert_ok = s.cert is None or m["cert"] == s.cert
    print("      C2 sizes in [0,%d]: %s  cert matches solver: %s  "
          "sizes %s" % (cell.k, sizes_ok, cert_ok,
                        "".join(str(v) for v in m["sizes"])
                        if cell.M <= 20 else "(%d atoms)" % cell.M))
    if opt is not None:
        print("      cert exact %s   nodes %d" % (opt == m["cert"],
                                                  s.nodes))
    if cell.M <= mim_witness_max_M:
        ww = window_witness(m["cost"], m["sizes"], cell.k, cell.M, 6)
        wf = None if ww is None else F(ww, m["den"])
        print("      C4 window witness %s >= exact %s: %s"
              % ("--" if wf is None else "%.3e" % float(wf),
                 "--" if m["gA"] is None else "%.3e" % float(m["gA"]),
                 wf is None or (m["gA"] is not None and wf >= m["gA"])))


def main():
    print("THE ANCHORED GAP -- the exactness threshold raised off the")
    print("weight lattice to the certificate's own coefficient box.")
    print("alpha = %s, nominal coverage %s" % (ALPHA, 1 - ALPHA))
    print()

    print("ARM 1 -- the seven bare cells")
    for cell in BARE:
        m = score(cell)
        print("  %-12s g %9.3e  g_A %9.3e  raised %-5s  "
              "fires g %-5s A %-5s"
              % (cell.name, float(m["g"]), float(m["gA"]),
                 m["gA"] > m["g"], m["fires_g"], m["fires_A"]))
    print()

    for weights, tag, label in ((WEIGHTS, "SW", "UNEQUAL-weight sweep"),
                                ([EQUAL], "EQ", "EQUAL-weight arm")):
        t0 = time.time()
        r = arm_sweep(weights, tag)
        print("ARM 2 %s: %d cells, %.1fs" % (label, r["seen"],
                                             time.time() - t0))
        print("  C3 truth failures: %d   K-C parity failures: %d   "
              "K-B monotonicity violations: %d"
              % (r["bad_truth"], r["bad_parity"], r["bad_mono"]))
        print("  certificate exact: %d   overstating: %d"
              % (r["exact"], r["inexact"]))
        print("  K-A anchored fires where it overstates: %d"
              % r["fires_A_at_inexact"])
        print("  lattice baseline: fires %d (%d at exact)"
              % (r["fires_g"], r["fires_g_at_exact"]))
        print("  anchored:         fires %d (%d at exact)   "
              "gained over lattice: %d   cells with g_A > g: %d"
              % (r["fires_A"], r["fires_A_at_exact"], r["gained"],
                 r["raised"]))
        if r["exact"]:
            print("  reach: lattice %d/%d = %.1f%%   anchored "
                  "%d/%d = %.1f%%"
                  % (r["fires_g_at_exact"], r["exact"],
                     100.0 * r["fires_g_at_exact"] / r["exact"],
                     r["fires_A_at_exact"], r["exact"],
                     100.0 * r["fires_A_at_exact"] / r["exact"]))
        print()

    print("ARM 3 -- the four ring cells")
    print("  %-12s %4s %3s %10s %9s %9s %9s"
          % ("cell", "M", "k", "optimum", "D/t*", "g", "g_A"))
    for cell in CELLS:
        t0 = time.time()
        if not ring_truth(cell):
            print("  %-12s TRUTH FAILURE" % cell.name)
            continue
        if cell.M > 20:
            # TILT-4-WIDE: the exact box is (k+1)^M and REFUSED; the
            # windowed witness alone decides the negative (FIFTH).
            got = cert_sizes(cell, ALPHA)
            if got is None:
                print("  %-12s K-D: tied block unusable" % cell.name)
                continue
            sizes, cert_int, room, den, _lv = got
            cost, _cv, _tg, _dn = integerize(cell, ALPHA)
            g = lattice_gap(cell)
            print("  %-12s %4d %3d %10s %9.3e %9.3e   REFUSED "
                  "(box %d^%d)"
                  % (cell.name, cell.M, cell.k, "(solver)", float(room),
                     float(g), cell.k + 1, cell.M))
            ww = window_witness(cost, sizes, cell.k, cell.M, 6)
            wf = None if ww is None else F(ww, den)
            if wf is None:
                print("      window witness: NONE in width 6 -- "
                      "no verdict")
            else:
                print("      window witness %.3e %s D/t* %.3e -> "
                      "anchored fire %s  (%.1fs)"
                      % (float(wf), "<" if wf < room else ">=",
                         float(room),
                         "IMPOSSIBLE" if wf < room else "UNDECIDED",
                         time.time() - t0))
            continue
        m = score(cell)
        s = solve(cell, ALPHA)
        report_solved(cell, m, s)
        print("      (%.1fs)" % (time.time() - t0))
    print()

    print("ARM 4 -- the theta walk, TILT-3's ring shape")
    print("  %-12s %4s %3s %10s %9s %9s %9s"
          % ("cell", "M", "k", "optimum", "D/t*", "g", "g_A"))
    for n in LADDER:
        cell = Cell("W-%d" % n, (3, 5, 7), (3, 5), 3, F(n - 1, n))
        t0 = time.time()
        if not ring_truth(cell):
            print("  W-%-10d TRUTH FAILURE" % n)
            continue
        m = score(cell)
        s = solve(cell, ALPHA)
        report_solved(cell, m, s)
        print("      (%.1fs)" % (time.time() - t0))


if __name__ == "__main__":
    main()
