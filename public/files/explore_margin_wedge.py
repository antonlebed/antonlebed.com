"""The Lebesgue margin's wedge, derived from the lookahead criterion —
never-underpredicting and the one-digit locus rise from rule at grid
scope to proved.

THE QUESTION. The margin story for redundant addition — the Lebesgue
heuristic b^c * rho >= 2W never underpredicts the lookahead, and
overpredicts by exactly one digit precisely on the wedge
rho*(b-2) < 2*(b-1) intersected with the law's c = 1 region — was a
rule at grid scope (explore_margin_locus.py's 214 contiguous cells,
with the symmetric sweeps' margin rows behind them,
explore_redundant_lookback.py) while the lookahead law above it is
proved (explore_lookahead_proof.py: c = 1 iff
rho >= sigma := ceil(am/(b-1)) + ceil(ap/(b-1)), every radix, every
contiguous set with rho >= 1). This run supplies the missing chain:
the margin's grant region reduces to the criterion's by the same
unpacking cases the proof already carries, so the wedge is a
consequence of the criterion and not a separate observation.

THE DERIVATION, hand-derived before this engine was written.
Conventions as in explore_lookahead_proof.py: contiguous digit set
D = {-am..ap}, spread W = am + ap, slack rho = W + 1 - b >= 1,
sigma = ceil(am/(b-1)) + ceil(ap/(b-1)), and the margin's verdict at
lookahead c the inequality b^c * rho >= 2W.

(1) THE MARGIN'S GRANT IS A (b, rho) CONDITION. Substituting
W = rho + b - 1 into b*rho >= 2W gives b*rho >= 2*rho + 2*(b-1),
i.e. rho*(b-2) >= 2*(b-1): the margin's c = 1 grant never sees the
set's shape, only its radix and slack — which is why its miss locus
can be written as the wedge rho*(b-2) < 2*(b-1) at all.

(2) NEVER UNDERPREDICTS AT c = 1. rho*(b-2) >= 2*(b-1) forces b >= 3
(the left side vanishes at b = 2 and the right side is positive) and
rho >= 2 + 2/(b-2): rho >= 4 at b = 3, rho >= 3 at b >= 4. The
proof's unpacking cases (explore_lookahead_proof.py step (6)) give
sigma <= 3 at every rho = 3 shape and sigma <= rho at every
rho >= 4 shape once b >= 3 — so rho >= sigma holds everywhere the
margin grants c = 1, and the criterion grants with it.

(3) THE OTHER TWO LOOKAHEADS ARE TRIVIALLY SAFE. At c = 0 the margin
requires rho >= 2W, impossible (rho = W + 1 - b <= W - 1 < 2W), so
it never grants a lookahead the game never wins. At c = 2 it always
grants: b^2 * rho >= 2W reduces by (1)'s substitution to
rho*(b^2 - 2) >= 2*(b-1), and rho >= 1 with b^2 - 2 >= 2*(b-1)
(i.e. (b-1)^2 >= 1) closes it — matching the proved "c = 2 always
suffices". So the margin never underpredicts at ANY lookahead.

(4) THE WEDGE IS EXACTLY THE OVERPREDICTION SET, AND ITS SHAPE
FOLLOWS. The margin misses (reads c = 2 where the true lookahead is
1) exactly on {rho >= sigma} intersected with
{rho*(b-2) < 2*(b-1)}. Unpacking with the criterion's clause form
(rho >= 2, b >= 3, not (rho = 2 with min(am, ap) = 1)): the wedge
inequality caps rho at 3 for b = 3, at 2 for b = 4 (2*rho < 6), and
at 2 for b >= 5 (rho < 2 + 2/(b-2) < 3). So the wedge is

    (b >= 3, rho = 2, min(am, ap) != 1)  union  (b = 3, rho = 3),

the doc's "at b >= 4 the wedge is rho = 2 alone; at b = 3 it
includes rho = 3" — and every rho = 3 shape at b = 3 is granted
(sigma <= 3), so no endpoint clause thins the rho = 3 slice. On the
wedge the margin's verdict is c = 2 by (3) against a true c = 1:
exactly one digit, every time.

THE DESIGN, frozen before the engine. The rig checks every object
the derivation constructs, against pure arithmetic on a wide grid
and against the residual safety game's fixed points on the census
grid (the game engine is explore_lookahead_proof.py's, carried
verbatim).

P-A The controls come back: (2,1) at c_min = 2 and (10,6) at
    c_min = 1 through this code path, and the census grid
    (2 <= b <= 10, 1 <= rho <= 5, am <= ap, spread <= 14) counts
    214 cells.
P-B The substitution identity of (1) holds at every (b, am, ap)
    with b <= 40, am, ap <= 30, rho >= 1: b*rho >= 2W iff
    rho*(b-2) >= 2*(b-1).
P-C Never-underpredicting holds twice over: arithmetically,
    rho*(b-2) >= 2*(b-1) implies rho >= sigma at every wide-grid
    cell; and on the game, c_margin >= c_min at every census cell,
    where c_margin is the least c in {0, 1, 2} with b^c * rho >= 2W
    and c_min the least c with 0 in the game's winning set.
P-D The wedge identity holds twice over: arithmetically,
    {rho >= sigma and rho*(b-2) < 2*(b-1)} equals the closed form
    of (4) at every wide-grid cell; and on the game, the measured
    miss cells {c_margin = 2, c_min = 1} are exactly the wedge
    cells of the census grid.
P-E The margin never grants c = 0 (rho < 2W) and always grants
    c = 2 (b^2 * rho >= 2W) at every wide-grid cell.

KILLS, frozen as what this rig PRINTS.

K1 A census cell prints c_margin < c_min -> the margin DOES
   underpredict and (2)/(3) are wrong; the story stays a rule at
   grid scope and the tier does not move.
K2 The wide grid prints a cell where {rho >= sigma and
   rho*(b-2) < 2*(b-1)} and the closed form of (4) disagree -> the
   wedge's derived shape is wrong at that cell; the shape claim
   demotes to the game's scope.
K3 A census cell prints a measured miss off the predicted wedge, or
   a predicted wedge cell that is not a measured miss -> the
   reduction chain breaks at the game; the cell is the report.
K4 The census recount differs from 214 or an anchor misses -> wrong
   grid, nothing downstream is read.

POSITIVE CONTROL, run and read before any verdict line: P-A whole.

FINDINGS (entered post-run; every number below sits in this file's
printed output).

F1 THE CONTROL HOLDS. Both anchors return their recorded values
   through this code path — (2,1) at c_min = 2, (10,6) at
   c_min = 1 — and the census recounts 214 cells. P-A held.

F2 THE SUBSTITUTION IDENTITY IS EXACT. b*rho >= 2W iff
   rho*(b-2) >= 2*(b-1) at 26330/26330 wide-grid cells (b <= 40,
   am, ap <= 30, rho >= 1). P-B held: the margin's c = 1 grant is
   a (b, rho) condition and never sees the set's shape.

F3 THE MARGIN NEVER UNDERPREDICTS, DERIVED AND MEASURED. The
   implication rho*(b-2) >= 2*(b-1) -> rho >= sigma holds at
   26330/26330 wide-grid cells, and c_margin >= c_min at 214/214
   census cells. K1 never fired.

F4 THE WEDGE IDENTITY IS EXACT, DERIVED AND MEASURED. The
   overprediction set {rho >= sigma, rho*(b-2) < 2*(b-1)} equals
   the closed form (b >= 3, rho = 2, min != 1) union (b = 3,
   rho = 3) at 26330/26330 wide-grid cells; on the census the
   measured misses {c_margin = 2, c_min = 1} are exactly the
   predicted wedge cells, 31/31 — the same 31 one-digit losses
   explore_margin_locus.py counted, now derived. K2, K3 never
   fired.

F5 THE OUTER LOOKAHEADS ARE SAFE AS DERIVED. rho < 2W and
   b^2 * rho >= 2W at 26330/26330 wide-grid cells each: the margin
   never grants the c = 0 the game never wins, and always grants
   the c = 2 that always suffices. P-E held.

VERDICT. With the derivation in the docstring and no kill fired,
the margin story is PROVED at the criterion's own scope — every
radix b >= 2, every contiguous digit set with rho >= 1: the
Lebesgue margin never underpredicts at any lookahead, and
overpredicts by exactly one digit precisely on the wedge
(b >= 3, rho = 2, min endpoint != 1) union (b = 3, rho = 3),
equivalently {rho >= sigma} intersected with
{rho*(b-2) < 2*(b-1)}. The census's 214 game cells, re-measured
here, are now the check on the chain rather than the evidence for
a rule. What
stays scanned: the slope bound's one-digit loss on the same wedge
is the scaling rigs' rule, not touched here.

RUN RECORD: pure Python, integers only, standard library; largest
winning set a few hundred residues, far under the analysis memory
ceiling; ~0.16 s wall clock. Prints reproduced by:
python prime/code/explore_margin_wedge.py
"""

FAILURES = []


def ok(cond, msg):
    if not cond:
        FAILURES.append(msg)
        print(f"  FAIL: {msg}")


def ceil_div(x, y):
    return -(-x // y)


def repunit(b, c):
    return sum(b ** i for i in range(c))


def win_set(b, am, ap, c):
    """Greatest fixed point of the residual safety game (the engine of
    explore_lookahead_proof.py, carried verbatim)."""
    S = list(range(-2 * am, 2 * ap + 1))
    lo, hi = -am * repunit(b, c), ap * repunit(b, c)
    win = set(range(lo, hi + 1))
    changed = True
    while changed:
        changed = False
        for R in list(win):
            for s in S:
                if not any(b * R + s - e * b ** c in win
                           for e in range(-am, ap + 1)):
                    win.discard(R)
                    changed = True
                    break
    return win


def c_min(b, am, ap):
    for c in (0, 1, 2):
        if 0 in win_set(b, am, ap, c):
            return c
    return None


def c_margin(b, am, ap):
    W = am + ap
    rho = W + 1 - b
    for c in (0, 1, 2):
        if b ** c * rho >= 2 * W:
            return c
    return None


def sigma(b, am, ap):
    return ceil_div(am, b - 1) + ceil_div(ap, b - 1)


def census_cells():
    cells = []
    for b in range(2, 11):
        for am in range(0, 15):
            for ap in range(am, 15):
                W = am + ap
                rho = W + 1 - b
                if 1 <= rho <= 5 and W <= 14:
                    cells.append((b, am, ap))
    return cells


def wide_cells():
    cells = []
    for b in range(2, 41):
        for am in range(0, 31):
            for ap in range(0, 31):
                if am + ap + 1 - b >= 1:
                    cells.append((b, am, ap))
    return cells


def wedge_closed_form(b, am, ap):
    rho = am + ap + 1 - b
    return ((b >= 3 and rho == 2 and min(am, ap) != 1)
            or (b == 3 and rho == 3))


def main():
    print("=== P-A: controls and census recount ===")
    a1 = c_min(2, 1, 1)
    a2 = c_min(10, 6, 6)
    print(f"  (2,1) c_min = {a1}   (10,6) c_min = {a2}")
    ok(a1 == 2, "anchor (2,1) expected c_min = 2")
    ok(a2 == 1, "anchor (10,6) expected c_min = 1")
    census = census_cells()
    print(f"  census recount: {len(census)} cells")
    ok(len(census) == 214, "census recount expected 214")
    if FAILURES:
        print("POSITIVE CONTROL FAILED — nothing downstream is read.")
        return

    wide = wide_cells()
    print(f"=== wide arithmetic grid: {len(wide)} cells "
          "(b <= 40, am, ap <= 30, rho >= 1) ===")

    print("=== P-B: substitution identity b*rho >= 2W iff "
          "rho*(b-2) >= 2*(b-1) ===")
    n_ok = 0
    for (b, am, ap) in wide:
        W = am + ap
        rho = W + 1 - b
        if (b * rho >= 2 * W) == (rho * (b - 2) >= 2 * (b - 1)):
            n_ok += 1
        else:
            ok(False, f"substitution identity fails at {(b, am, ap)}")
    print(f"  identity holds: {n_ok}/{len(wide)}")

    print("=== P-C (arithmetic): margin grant implies criterion "
          "grant ===")
    n_ok = 0
    for (b, am, ap) in wide:
        rho = am + ap + 1 - b
        if rho * (b - 2) >= 2 * (b - 1):
            if rho >= sigma(b, am, ap):
                n_ok += 1
            else:
                ok(False, f"margin underpredicts arithmetically "
                          f"at {(b, am, ap)}")
        else:
            n_ok += 1
    print(f"  implication holds: {n_ok}/{len(wide)}")

    print("=== P-D (arithmetic): wedge set equals closed form ===")
    n_ok = 0
    for (b, am, ap) in wide:
        rho = am + ap + 1 - b
        in_wedge = (rho >= sigma(b, am, ap)
                    and rho * (b - 2) < 2 * (b - 1))
        if in_wedge == wedge_closed_form(b, am, ap):
            n_ok += 1
        else:
            ok(False, f"wedge closed form disagrees at {(b, am, ap)}")
    print(f"  wedge identity holds: {n_ok}/{len(wide)}")

    print("=== P-E: margin never grants c = 0, always grants "
          "c = 2 ===")
    n0 = n2 = 0
    for (b, am, ap) in wide:
        W = am + ap
        rho = W + 1 - b
        if rho < 2 * W:
            n0 += 1
        else:
            ok(False, f"margin grants c = 0 at {(b, am, ap)}")
        if b * b * rho >= 2 * W:
            n2 += 1
        else:
            ok(False, f"margin refuses c = 2 at {(b, am, ap)}")
    print(f"  c = 0 never granted: {n0}/{len(wide)}   "
          f"c = 2 always granted: {n2}/{len(wide)}")

    print("=== P-C / P-D (game): the census grid, measured ===")
    n_safe = 0
    misses = []
    for (b, am, ap) in census:
        cm = c_min(b, am, ap)
        cg = c_margin(b, am, ap)
        if cg >= cm:
            n_safe += 1
        else:
            ok(False, f"MARGIN UNDERPREDICTS at {(b, am, ap)}: "
                      f"margin {cg} < game {cm}")
        if cg == 2 and cm == 1:
            misses.append((b, am, ap))
    print(f"  c_margin >= c_min: {n_safe}/{len(census)}")
    predicted = [cell for cell in census if wedge_closed_form(*cell)]
    print(f"  measured misses: {len(misses)}   "
          f"predicted wedge cells: {len(predicted)}")
    ok(sorted(misses) == sorted(predicted),
       "measured misses differ from predicted wedge cells")
    if sorted(misses) == sorted(predicted):
        print(f"  miss set = wedge set: {len(misses)}/{len(misses)}")

    print()
    if FAILURES:
        print(f"KILLED: {len(FAILURES)} failure(s).")
    else:
        print("ALL CHECKS PASS -- the margin story is proved at the "
              "criterion's scope.")


if __name__ == "__main__":
    main()
