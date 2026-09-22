"""The segmented unit and the breakpoint slide: does a
table-and-interpolate map of one signed-digit stream ever read below
the margin law's L*, and when a two-piece map's breakpoint slides with
its slopes fixed, what decides whether its delay moves?

THE QUESTION. The piecewise theorem (explore_piecewise_delay.py) reads
a continuous piecewise-affine map with rational data at the least L at
which every piece clause and every kink clause is empty, below the
margin's L* exactly when every clause at L* - 1 is empty. Two design
questions ride on it. A table-and-interpolate function unit — the
field's standard shape for reciprocals, logarithms and exponentials,
a curve sampled at breakpoints and joined by chords — is such a map:
does it read below the margin, and does the answer depend on how many
segments it has or where its breakpoints sit? And for a fixed pair of
slopes, does sliding the breakpoint move the delay, and if so through
which clause?

THE DERIVATION, before the engine. Conventions as in
explore_piecewise_delay.py: radix b, digits {-am..ap}, slack
rho = am + ap + 1 - b >= 1, M+- = a+-/(b-1), w = M- + M+. A box inside
an affine piece of slope s = p/q kills at lookahead L iff its lower
end's phase lies in the piece's dead arc (1 - g, 1), g = |s| w/b^L -
(w - 1), and over the prefixes the phases form a lattice of step
delta = gcd(p, q b^L)/(q b^L) with an offset eventually periodic in n. At
L = L* - 1 the steepest piece has g > 0 by the definition of L*.
  THE SEGMENT LEMMA. An open arc of length g contains a point of every
  lattice of step delta < g, whatever the offset; so a piece with
  delta < g at L* - 1 is dead there for every offset, and a map reads
  below the margin only if its steepest piece has delta >= g, which
  needs the slope's denominator times b^L to be at most about 1/g.
  A chord of a curve has a slope whose denominator is the product of
  the breakpoints' denominators, so a segmented curve's steepest chord
  has a fine lattice and is dead at L* - 1 for every breakpoint
  placement: THE SEGMENT COUNT AND THE ALIGNMENT ARE BOTH FREE, AND
  BOTH ARE WORTHLESS — the unit reads at the margin regardless.
  THE SLIDE. For the specimen [x/2 | x] at a kink kappa with the left
  offset 0, the right piece's offset is kappa/2 and its lattice at
  L = 0 has step 1 and excess g = 1, the arc (0, 1): its phases are
  u + kappa b^n / 2 + M- - M- mod 1, alive iff kappa b^n / 2 is an
  integer at every depth of the cycle, i.e. iff kappa lies in
  2 Z[1/b] — all of Z[1/b] at even b, where 2 divides b^n, and the
  even-numerator half at odd b. The slope-1/2 piece's clause does not
  see kappa (its
  offset is 0). So with the slopes fixed the delay moves with the
  breakpoint exactly through the offset phase of the coarse-lattice
  piece: on the b-adic lattice 2 Z[1/b] the specimen reads at 0
  wherever it did at kappa = 0, and off it the slope-1 piece kills and
  the floor is 1 at every cell. Alignment is everything only for a
  piece whose slope has a coarse lattice; the reciprocal's chords have
  none.

THE SLATE, frozen before the engine.

P-A THE CONTROL. The specimen at kappa = 0 over the 20 census cells of
    radices 2..5 reproduces explore_piecewise_delay.py F2: floor 1 at
    exactly (4,2,2), (5,2,3), (5,3,2), (5,3,3) and 0 at the other 16,
    the table equal to the engine at every cell.
P-B THE SLIDE ON THE SPECIMEN. Slopes 1/2 and 1 with kappa over a
    fixed menu of breakpoints per cell, half in 2 Z[1/b] and half off
    it: at the 16 alive cells the floor is 0 exactly at the kappa in
    2 Z[1/b] and 1 at the others, the kill off the lattice inside the
    slope-1 piece; at the four dead cells the floor is 1 at every
    kappa; the table equals the engine at every run.
P-C THE SLIDE ON A SAME-SIGN PAIR. Slopes 1/2 and 2 over the same
    menu: a reading — whether the floor moves with kappa at a cell,
    and, where it does, that the moving verdict is the slope-2 piece's
    clause and never the slope-1/2 piece's.
P-D THE SEGMENTED RECIPROCAL. 1/(s + x), s = 1 + M-, sampled at N = 4
    and N = 8 uniform breakpoints over [-M-, M+] and, at N = 8, at
    the nearest box lower ends of a depth with at least 4N prefixes
    (the aligned design), over the 20 cells: the steepest chord has
    delta < g at L* - 1 at every design, the engine's floor is L* at
    every design, and the kill at L* - 1 sits inside the steepest
    chord's piece.

KILLS, frozen as what this rig PRINTS.

K1 P-A prints a floor other than F2's at any cell, or a table-engine
   disagreement -> the control failed; nothing below is read.
K2 The table and the engine disagree at any slide run.
K3 A kill at the law's L* anywhere -> the Lipschitz sufficiency is
   wrong.
K4 At an alive cell a kappa in 2 Z[1/b] with floor 1, or a kappa off
   it with floor 0 -> the slide derivation is wrong.
K5 A segmented design with a floor below L*, or with delta >= g at
   its steepest chord -> the segment lemma is wrong or the design
   is coarser than derived; the print names which.

POSITIVE CONTROL: P-A whole, read before any other line.

THE REHEARSAL (radices 2..3, 64 slide runs and 12 designs, the table
equal to the engine at every run) FIRED K4 AND K5, so the derivation
above is re-done by hand here, before the full run, and two marked
predictions are added; the original slate and its kills stand above
as written.
  THE SLIDE, corrected. The slope-1 piece's clause is as derived —
  empty iff kappa b^n / 2 is an integer along the cycle, i.e. kappa
  in 2 Z[1/b] — but the KINK CLAUSE also moves with kappa, and at
  shallow depth a same-sign kink fires alone (explore_piecewise_smooth.py
  F5), the containment lemma reaching only the depths where the right
  box is a prefix; the rehearsal's on-lattice kills are straddlers at
  the root or depth 1, and 5 of 16 on-lattice breakpoints read 0
  against 0 of 16 off it. So the lattice is NECESSARY and not
  sufficient: off 2 Z[1/b] the slope-1 piece fires; on it the floor is
  0 iff the kink clause (and the slope-1/2 piece's) is empty, a shallow
  finite check with no lattice law behind it.
  THE SEGMENT LEMMA, corrected. The open arc (1 - g, 1) is missed by a
  lattice of step delta iff delta >= g and the offset phi satisfies
  phi mod delta in [0, delta - g], a closed window of length delta - g
  — at delta = g exactly, the lattice must contain the point 1. A
  chord's slope can be arithmetically simple while the curve's is
  not: the uniform 4-segment reciprocal at (2,1,1) and (3,2,2) has
  steepest chord -2/3 with delta = g = 1/3 and offset 1/3, on the
  window's one point, and reads at 0 against L* = 1 — a segmented
  unit BELOW the margin, and its 8-segment refinement (chord -4/5,
  delta 1/5 < g 3/5) back at the margin: a finer table is a steeper,
  finer-latticed first chord, so the segment count is a delay axis
  with the coarse side winning.
P-B' Off 2 Z[1/b] the slope-1 piece's clause fires at every run; on
    it the clause is empty at every run and the floor is 0 exactly
    when the kink clause and the slope-1/2 piece's are empty.
P-D' A design reads below L* only with delta >= g at its steepest
    chord; the print counts how many of those sit at delta = g exactly
    and how many designs with delta >= g still read at L*. (A first
    full run walked each design's clause table too and was killed at
    1500 s inside the aligned 8-chord design at (3,2,2), whose offset
    cycle is too long to walk; the engine's survival certifies the
    clause, so the table is not consulted here and P-D runs alone
    under --seg.)
K4' P-B' fails at a run.  K5' P-D' fails at a design.

THE FULL RUN'S P-B FIRED K4' TOO, at on-lattice breakpoints: the
slope-1 piece's clause holds along the CYCLE and also at every
shallower depth where a box already lies inside the piece, and there
kappa b^n / 2 need not be an integer yet — at (2,1,1) and kappa = -1/2
the depth-1 box [-1/2, 1/2] sits inside the right piece with phase
1/2. So the exact law is finer than the lattice: with n1 the first
depth at which the piece holds a box, the clause is empty iff
kappa b^n1 / 2 is an integer (deeper depths then follow). P-B'' is
that law checked by the table alone over the same runs
(python explore_segmented_delay.py [BMAX] --law), added after the
engine run and read against its prints.

FINDINGS (entered post-run; every number below sits in this file's
printed output at radices 2..5).

F1 THE CONTROL HOLDS. The specimen at kappa = 0 reads F2's floors at
   20 of 20 cells, the table equal to the engine at every one. P-A
   held; K1 never fired.

F2 THE SLIDE IS NOT A LATTICE LAW. 160 runs (20 cells, 8 breakpoints),
   the table equal to the engine at 160 of 160; the floor moves with
   kappa at 16 of 20 cells. Off 2 Z[1/b] the floor is L* at 80 of 80
   runs and the slope-1 piece's clause fires at 80 of 80; on it the
   floor is 0 at 19 of 80 and L* at 61, the slope-1 piece firing at 41
   of the 80 on-lattice runs. K4 fired 91 times and K4' 41: the
   derivation's lattice condition is necessary and not sufficient.
   The exact law (P-B'', the table alone over the same 160 runs): the
   slope-1 piece's clause is empty iff kappa b^n1 / 2 is an integer
   at 160 of 160, n1 the first depth at which the piece holds a box
   (39 breakpoints satisfy it), and the floor is L* - 1 iff that holds
   with the kink clause and the slope-1/2 piece's empty, 160 of 160.
   So a breakpoint's alignment reads at ONE depth, the first the
   piece holds a box, and the shallow kink clause sits on top of it.

F3 THE SAME-SIGN PAIR MOVES THROUGH THE STEEP PIECE. Slopes 1/2 and 2,
   160 runs, the table equal to the engine at 160 of 160: the floor
   moves with kappa at 6 of 20 cells ((2,1,1), (3,2,2), (4,1,3),
   (4,3,1), (5,2,4), (5,3,3)), at every one of them the slope-2
   piece's verdict moving and the slope-1/2 piece's constant (empty at
   every run of the leg); at 3 of the other 14 cells ((4,2,3), (4,3,2),
   (5,4,2)) every clause is empty at every breakpoint and the pair
   reads at L* - 1 wherever the kink sits, and at the other 11 the
   slope-2 piece is dead at L* - 1 at every breakpoint. P-C read.

F4 THE SEGMENTED RECIPROCAL READS BELOW THE MARGIN AT THE BOUNDARY.
   60 designs: the steepest chord has delta < g at 56 and those 56
   read at L*, the kill at L* - 1 inside the steepest chord at 24 and
   at a straddler at 32; the other 4 — the uniform 4-chord design at
   the four symmetric top cells (2,1,1), (3,2,2), (4,3,3), (5,4,4),
   where w = 2 and the steepest chord is -2/3 with delta = g = 1/3 —
   read at 0 against L* = 1, alive at L* - 1 by the engine; 0 designs
   with delta >= g read at L*. K5 fired 8 times (the four designs, on
   both prints); K5' never fired: every design below L* sits at
   delta = g exactly. The 8-chord refinement at those cells (chord
   -4/5, delta 1/5 < g 3/5) and the aligned 8-chord design read at
   L*: the alignment moved nothing at any of the 20 cells, the
   segment count moved four.

VERDICT. A table-and-interpolate unit reads below the margin exactly
through the segment lemma: its steepest chord must have a lattice at
least as coarse as its excess, which a uniform 4-chord reciprocal
meets at the boundary at the four symmetric top cells and no finer
table meets anywhere; where the breakpoints sit is worthless for the
chords and decides a coarse-lattice piece at one depth, the first
its piece holds a box, with the kink clause on top. Alignment is not
the design axis; the chords' arithmetic is.

RUN RECORD: pure Python, exact fractions for every verdict, standard
library; under memwatch. The control and the two slide legs: 246 s
at radices 2..5 (the control 36 s, P-B 89 s, P-C 121 s), one process
whose P-D leg walked each design's clause table and was killed at the
1500 s timeout inside the aligned design at (3,2,2), peak commit
285 MB, its P-A..P-C prints complete and read; P-D alone (--seg)
42 s, peak commit 81 MB; the slide law (--law) under a minute, the
table alone. Prints reproduced by:
python prime/code/explore_segmented_delay.py [BMAX]
python prime/code/explore_segmented_delay.py [BMAX] --seg
python prime/code/explore_segmented_delay.py [BMAX] --law
"""

import math
import sys
import time
from fractions import Fraction as Fr

import explore_onestream_delay as one
import explore_piecewise_delay as pw

FAILURES = []


def ok(cond, msg):
    if not cond:
        FAILURES.append(msg)
        print(f"  FAIL: {msg}")


# ------------------------------------------------------------ the maps

def interpolant(points, name):
    """The chords through consecutive (x, f(x)) points, exact."""
    slopes, offsets, kinks = [], [], []
    for (x1, y1), (x2, y2) in zip(points, points[1:]):
        s = (y2 - y1) / (x2 - x1)
        slopes.append(s)
        offsets.append(y1 - s * x1)
    kinks = [x for x, _ in points[1:-1]]
    return pw.Piecewise(slopes, offsets, kinks, name)


def recip_points(b, am, ap, xs):
    s = 1 + Fr(am, b - 1)
    return [(x, 1 / (s + x)) for x in xs]


def uniform_xs(b, am, ap, N):
    Mm, Mp = Fr(am, b - 1), Fr(ap, b - 1)
    w = Mm + Mp
    return [-Mm + j * w / N for j in range(N + 1)]


def aligned_xs(b, am, ap, N):
    """The uniform breakpoints moved to the nearest box lower end of the
    least depth m with at least 4N prefixes; the ends stay."""
    Mm, Mp = Fr(am, b - 1), Fr(ap, b - 1)
    m = 0
    while (am + ap) * (b ** m - 1) // (b - 1) + 1 < 4 * N:
        m += 1
    D = (b - 1) * b ** m
    xs = uniform_xs(b, am, ap, N)
    out = [xs[0]]
    for x in xs[1:-1]:
        u = round(x * D + am) // (b - 1)
        cand = Fr((b - 1) * u - am, D)
        out.append(cand)
    out.append(xs[-1])
    return out, m


def in_2Zb(kappa, b):
    """Is kappa in 2 Z[1/b]: some b^n kappa an even integer?"""
    x = Fr(kappa)
    for _ in range(40):
        if x.denominator == 1 and x.numerator % 2 == 0:
            return True
        if x.denominator > 1 and math.gcd(x.denominator, b) == 1:
            return False
        x *= b
    return False


def kappa_menu(b, am, ap):
    """Eight breakpoints inside (-M-, M+): four in 2 Z[1/b], four off it."""
    Mm, Mp = Fr(am, b - 1), Fr(ap, b - 1)
    on = [Fr(2, b), Fr(-2, b), Fr(2, b * b), Fr(-2, b * b), Fr(4, b * b), Fr(-4, b * b), Fr(2, b ** 3), Fr(-2, b ** 3)]
    off = [Fr(1, b), Fr(-1, b), Fr(1, 3), Fr(-1, 3), Fr(1, b * b), Fr(-1, b * b), Fr(1, 6), Fr(-1, 6), Fr(1, 7), Fr(3, b * b), Fr(-3, b * b), Fr(1, 2), Fr(-1, 2)]
    if b == 2:
        off = [k for k in off if not in_2Zb(k, b)]
    on = list(dict.fromkeys(k for k in on if -Mm < k < Mp and in_2Zb(k, b)))[:4]
    off = list(dict.fromkeys(k for k in off if -Mm < k < Mp and not in_2Zb(k, b)))[:4]
    assert len(on) == 4 and len(off) == 4, (b, am, ap, on, off)
    return on + off


# ------------------------------------------------------------------ runs

F2_DEAD = {(4, 2, 2), (5, 2, 3), (5, 3, 2), (5, 3, 3)}


def control(bmax):
    print(f"\n=== P-A the control: [x/2 | x] at 0, radices 2..{bmax}")
    f = pw.specimen()
    good = 0
    for (b, am, ap) in pw.cells(bmax):
        r = pw.run_map(b, am, ap, f)
        want = 1 if (b, am, ap) in F2_DEAD else 0
        ok(r["efloor"] == want and r["tfloor"] == want, f"K1 ({b},{am},{ap}): floor engine {r['efloor']} table {r['tfloor']}, F2 says {want}")
        good += r["efloor"] == want and r["tfloor"] == want
    print(f"  F2 reproduced at {good} of {len(pw.cells(bmax))}")


def slide(bmax, sl, sr, title, check_law):
    print(f"\n=== {title}: slopes {sl} | {sr}, eight breakpoints per cell, radices 2..{bmax}")
    n_runs = agree = 0
    on_ok = off_ok = off_piece = on_kink_decides = 0
    moving = 0
    for (b, am, ap) in pw.cells(bmax):
        floors, moved_clause = {}, set()
        for kap in kappa_menu(b, am, ap):
            f = pw.two_piece(sl, sr, kap, 0)
            r = pw.run_map(b, am, ap, f)
            n_runs += 1
            agree += r["efloor"] == r["tfloor"]
            ok(r["efloor"] == r["tfloor"], f"K2 ({b},{am},{ap}) kappa={kap}: engine {r['efloor']} table {r['tfloor']}")
            floors[kap] = r["efloor"]
            if check_law:
                alive_cell = (b, am, ap) not in F2_DEAD
                lat = in_2Zb(kap, b)
                if alive_cell:
                    want = 0 if lat else 1
                    ok(r["efloor"] == want, f"K4 ({b},{am},{ap}) kappa={kap} {'on' if lat else 'off'} 2Z[1/b]: floor {r['efloor']}")
                    if lat:
                        on_ok += r["efloor"] == 0
                    else:
                        off_ok += r["efloor"] == 1
                        where = kill_where(f, b, am, ap, r["kill"])
                        ok(where == 1, f"K4 ({b},{am},{ap}) kappa={kap}: the off-lattice kill not inside the slope-1 piece: {r['kill']} at {where}")
                else:
                    ok(r["efloor"] == 1, f"K4 ({b},{am},{ap}) kappa={kap} dead cell: floor {r['efloor']}")
            # the clause table at L* - 1 at every run: what fires
            tab = pw.Table(b, am, ap, f)
            pieces, kinks, _ = tab.verdict(r["Ls"] - 1)
            floors[kap] = (r["efloor"], pieces[0], pieces[1], kinks[0], kill_where(f, b, am, ap, r["kill"]))
            if check_law:
                # P-B' (post-rehearsal): off the lattice the slope-1 piece fires; on it, floor 0 iff the kink is empty
                lat = in_2Zb(kap, b)
                if not lat:
                    ok(pieces[1], f"K4' ({b},{am},{ap}) kappa={kap} off 2Z[1/b]: the slope-1 piece's clause empty")
                    off_piece += pieces[1]
                else:
                    ok(not pieces[1], f"K4' ({b},{am},{ap}) kappa={kap} on 2Z[1/b]: the slope-1 piece's clause fires")
                    on_kink_decides += (r["efloor"] == 0) == (not kinks[0] and not pieces[0])
        vals = set(v[0] for v in floors.values())
        if len(vals) > 1:
            moving += 1
        tag = lambda k: "on " if in_2Zb(k, b) else "off"
        print(f"  ({b},{am},{ap}) L*={r['Ls']}: " + "; ".join(
            f"k={k} {tag(k)} floor {v[0]} [p0 {'D' if v[1] else '-'} p1 {'D' if v[2] else '-'} kink {'D' if v[3] else '-'}] kill {v[4]}"
            for k, v in floors.items()))
        if not check_law and len(vals) > 1:
            ok(len(set(v[1] for v in floors.values())) == 1, f"P-C ({b},{am},{ap}): the slope-{sl} piece's verdict moves with kappa")
    print(f"  {n_runs} runs, table = engine at {agree}; the floor moves with kappa at {moving} of {len(pw.cells(bmax))} cells")
    if check_law:
        print(f"  alive cells: floor 0 on 2Z[1/b] at {on_ok}, floor 1 off it at {off_ok} (of 64 + 64 at radices 2..5); "
              f"P-B': off the lattice the slope-1 piece fires at {off_piece} of the off runs, on it the floor is 0 exactly when "
              f"the kink and the slope-1/2 piece are empty at {on_kink_decides} of the on runs")


def steepest(f):
    j = max(range(len(f.s)), key=lambda i: abs(f.s[i]))
    return j


def piece_of_box(f, b, am, ap, u, n):
    """The piece holding the box's midpoint (a box end can sit on a kink)."""
    D = (b - 1) * b ** n
    mid = Fr(2 * (b - 1) * u - am + ap, 2 * D)
    return f.piece(mid)


def kill_where(f, b, am, ap, kill):
    """'STRADDLER', a piece index, 'tree', or None for an alive verdict."""
    if kill is None or kill[0] != "dead":
        return None
    if kill[4]:
        return "STRADDLER"
    if kill[3] is None:
        return "tree"
    return piece_of_box(f, b, am, ap, kill[3], kill[2])


def segmented(bmax):
    print(f"\n=== P-D the segmented reciprocal 1/(s + x), s = 1 + M-, radices 2..{bmax}")
    n = at_law = fine = inside = below = boundary = coarse_dead = 0
    for (b, am, ap) in pw.cells(bmax):
        designs = [("uniform N=4", uniform_xs(b, am, ap, 4)), ("uniform N=8", uniform_xs(b, am, ap, 8))]
        axs, m = aligned_xs(b, am, ap, 8)
        designs.append((f"aligned N=8 depth {m}", axs))
        for label, xs in designs:
            f = interpolant(recip_points(b, am, ap, xs), f"recip {label}")
            o = one.least_lead(b, am, ap, f)
            Ls = pw.law_L(b, am, ap, f)
            j = steepest(f)
            L = Ls - 1
            tab = pw.Table(b, am, ap, f)
            period = tab.lattice_period(j, L)
            delta = Fr(1, period)
            g = abs(f.s[j]) * tab.w / Fr(b) ** L - (tab.w - 1)
            efloor, verdicts = pw.engine_floor(b, am, ap, f, o, Ls)
            kill = verdicts.get(L)
            n += 1
            fine += delta < g
            at_law += efloor == Ls
            where = kill_where(f, b, am, ap, kill)
            inside += where == j
            ok(delta < g, f"K5 ({b},{am},{ap}) {label}: delta {delta} >= g {g} at the steepest chord")
            ok(efloor == Ls, f"K5 ({b},{am},{ap}) {label}: floor {efloor} below L*={Ls}")
            # P-D' (post-rehearsal): a floor below L* only at delta >= g (the clause table is not walked: an
            # 8-chord interpolant's offset cycle is too long, and the engine's survival certifies the clause)
            if efloor < Ls:
                below += 1
                ok(delta >= g, f"K5' ({b},{am},{ap}) {label}: floor {efloor} < L* with delta {delta} < g {g}")
                boundary += delta == g
            elif delta >= g:
                coarse_dead += 1
            desc = (f"alive at L*-1 (floor {efloor})" if kill and kill[0] == "alive"
                    else f"kill at L*-1: t={kill[1]} n={kill[2]} in {where}" if kill else "no verdict")
            print(f"  ({b},{am},{ap}) {label}: o={o} L*={Ls}; steepest chord piece {j} slope {f.s[j]} delta={delta} g={g}; {desc}")
    print(f"  {n} designs: delta < g at {fine}, floor = L* at {at_law}, the kill inside the steepest chord at {inside}; "
          f"P-D': {below} designs read below L*, {boundary} of them at delta = g exactly; {coarse_dead} designs with delta >= g still at L*")


def first_box_depth(b, am, ap, f, j):
    """The least depth at which some box lies inside piece j."""
    Mm, Mp = Fr(am, b - 1), Fr(ap, b - 1)
    cuts = [-Mm] + f.k + [Mp]
    n = 0
    while True:
        bn = Fr(b) ** n
        umin, umax = -am * (b ** n - 1) // (b - 1), ap * (b ** n - 1) // (b - 1)
        lo = math.ceil(cuts[j] * bn + Mm)
        hi = math.floor(cuts[j + 1] * bn - Mp)
        if max(lo, umin) <= min(hi, umax):
            return n
        n += 1


def slide_law(bmax):
    """P-B'' (post-run, the table alone): the specimen's slope-1 piece at
    L* - 1 is empty iff kappa b^n1 / 2 is an integer, n1 the first depth
    at which the piece holds a box; and the floor is 0 iff that holds
    and the kink clause and the slope-1/2 piece's are empty."""
    print(f"\n=== P-B'' the slide law, the table alone: slopes 1/2 | 1, radices 2..{bmax}")
    runs = law_ok = floor_ok = on_lat = 0
    for (b, am, ap) in pw.cells(bmax):
        for kap in kappa_menu(b, am, ap):
            f = pw.two_piece(Fr(1, 2), Fr(1), kap, 0)
            Ls = pw.law_L(b, am, ap, f)
            tab = pw.Table(b, am, ap, f)
            pieces, kinks, _ = tab.verdict(Ls - 1)
            n1 = first_box_depth(b, am, ap, f, 1)
            pred = (kap * Fr(b) ** n1 / 2).denominator == 1
            runs += 1
            law_ok += pred == (not pieces[1])
            on_lat += pred
            ok(pred == (not pieces[1]), f"P-B'' ({b},{am},{ap}) kappa={kap}: n1={n1}, predicted {'empty' if pred else 'fires'}, table {'empty' if not pieces[1] else 'fires'}")
            floor_ok += (not tab.dead(Ls - 1)) == (pred and not kinks[0] and not pieces[0])
    print(f"  {runs} runs: the slope-1 piece's clause is empty iff kappa b^n1 / 2 is an integer at {law_ok}; "
          f"{on_lat} breakpoints satisfy it; the table's floor is L* - 1 iff it holds with the kink and the slope-1/2 piece empty at {floor_ok}")


def main():
    bmax = int(sys.argv[1]) if len(sys.argv) > 1 else 5
    if "--law" in sys.argv:
        slide_law(bmax)
        print(f"failures: {len(FAILURES)}")
        return
    if "--seg" in sys.argv:
        t0 = time.time()
        segmented(bmax)
        print(f"\nwall {time.time() - t0:.1f}s; failures: {len(FAILURES)}")
        return
    t0 = time.time()
    control(bmax)
    if FAILURES:
        print("\nPOSITIVE CONTROL FAILED; nothing below is read")
        for f in FAILURES:
            print("  ", f)
        return
    print(f"  control: {time.time() - t0:.1f}s")
    slide(bmax, Fr(1, 2), Fr(1), "P-B the slide on the specimen", True)
    print(f"  elapsed: {time.time() - t0:.1f}s")
    slide_law(bmax)
    slide(bmax, Fr(1, 2), Fr(2), "P-C the slide on a same-sign pair", False)
    print(f"  elapsed: {time.time() - t0:.1f}s")
    segmented(bmax)
    print(f"\nwall {time.time() - t0:.1f}s; failures: {len(FAILURES)}")
    for f in FAILURES:
        print("  ", f)


if __name__ == "__main__":
    main()
