"""The nonlinear window walls: x -> x^2 at the continued-fraction window.

THE QUESTION
------------
The continued-fraction window's Mobius corpus (explore_cf_window.py,
explore_cf_conductor.py) found no permanent boundary walls: output
cell boundaries are rationals, an integer Mobius map's preimage of a
rational is rational, hence finite CF — every boundary hug resolves.
This script opens the corpus's first NON-Mobius map, x -> x^2, and
asks whether it owns PERMANENT walls, whether the conductor law's
orbit reading survives a nonlinear map, and what near-wall behavior
looks like.

THE CRUX, resolved on paper before the engines. Fix the vocabulary in
the window's own terms (x^2 has no determinant, no transducer, no
unit): the window's VERTEX SET is the set of cell-boundary points —
for the CF window that is ALL of Q (every rational is a Stern-Brocot
vertex and stays a cell endpoint at every deeper depth); for the
leading base-b window it is Z[1/b], the finite expansions. A map's
RATIONALIZING SET is f^{-1}(vertices) minus the vertices: the
irrational inputs sent exactly onto a vertex. The hand analysis:

  THE WALL CRITERION. For f continuous and strictly monotone near an
  irrational input y, the reader's emission e(n) (output quotients
  common to every point of f(I_n), I_n the depth-n input cylinder)
  tends to infinity iff f(y) is irrational. If f(y) = r rational,
  then r is INTERIOR to f(I_n) at every depth (y interior, f open),
  and the two sides of a rational agree only up to r's own
  Stern-Brocot position — so e(n) freezes at e*(r), the common
  prefix length of r's two one-sided expansions, FOREVER. The
  permanent wall set of x^2 is therefore exactly the square roots of
  the rationals: the first permanent walls in the CF corpus, and the
  Mobius boundary collapse is the special case of an EMPTY
  rationalizing set (integer Mobius maps preserve Q). At a wall the
  delay slope is 1 — emission DIES; a rate stall only slows it
  (slope 1 - sigma < 1). The wall is the rate account's sigma -> 0
  endpoint: near-wall outputs start [prefix; N, ...] with N giant.

  THE MAP-BLIND CONDUCTOR LAW. Off the wall (y quadratic, y^2
  irrational), y^2 lies in the same field, both streams share the
  regulator, and the predicted digit ratio is pure orbit data:
  ratio = (i_out/i_in) * (ell_in/ell_out) — the conductor law of
  explore_cf_conductor.py with the map entering ONLY through which
  output orbit it selects. [Transplant, marked: the law is imported
  from the Mobius corpus; map-blindness is exactly the claim under
  test. The rate account's one local ingredient — |f(I_n)| scales by
  the bounded nonzero derivative 2y — replaces the Mobius derivative
  argument.]

  THE HUG DECOUPLING. A Mobius hug at output vertex v lasts as long
  as the CF of v's rational preimage — a function of v's own depth
  (that IS the boundary collapse). An x^2 hug at the FIXED vertex 2
  lasts m for EVERY m: input = sqrt2's first m quotients then an
  all-1s tail. Hug depth decouples from boundary depth, at bounded
  input digits (no giant input quotient — the Mobius mechanism
  requires one at the departure point). Both delay rulers freeze
  during the hug (commitment freezes outright — the rate-mismatch
  stall only slows digits while scale flows); the hugged scale is
  repaid in ONE giant output quotient at resolution:
  ln N_m ~ 2m ln(1+sqrt2). Permanence is the m -> infinity limit.

  THE CROSS-WINDOW LAW. The same criterion at the leading base-10
  window (vertex set Z[1/10]): x^2 at sqrt2 freezes there too, but
  x^2 at sqrt(1/3) freezes ONLY at CF (1/3 is a Stern-Brocot vertex,
  not a decimal one). Z[1/b] is a subset of Q, so every base-b wall
  of x^2 is a CF wall and not conversely: among rational-vertex
  grids the CF vertex set is the maximum possible — maximal wall
  exposure (property, by construction; a designed partition could
  place vertices at irrationals, outside this comparison).
  And redundancy is the cure by the reading lemma itself: at an
  overlapping cover the Lebesgue number is positive, a small-enough
  image interval fits inside SOME cell, and the stream correction
  prices the committed stream within one digit — no map with a
  modulus of continuity walls permanently at a redundant window.
  Walls are a partition phenomenon: the reading lemma was silent at
  partitions (Lebesgue number 0), and this script fills that regime
  for the CF window — permanent misalignment exactly on the
  rationalizing set.

  THE INVERSE ASYMMETRY. sqrt(x) has EMPTY rationalizing set (a
  rational square root forces a rational input), so the inverse map
  is wall-free while the forward map walls at every sqrt(r):
  readability is direction-asymmetric for nonlinear algebraic maps
  (one-line property; x^k walls at k-th roots — power-general, only
  x^2 scanned here).

THE DESIGN
----------
Exact interval semantics throughout (Fraction endpoints; squaring an
input cylinder squares its endpoints), reusing the CF machinery of
explore_cf_window.py and the exact quadratic arithmetic (surd CF,
lattice data, unit indices) of explore_cf_conductor.py. No closed
form from the target laws enters any rig.

E0  POSITIVE CONTROLS (read before any verdict). (i) 1/x at phi
    reads at bounded delay (the rig sees bounded reads). (ii) 2x at
    phi shows emission slope near 1/3 (the rig sees rate stalls).
    (iii) a Mobius hug that ENDS: 2x at input = CF(55/178) then an
    all-1s tail — the staircase resolves (the rig sees finite hugs,
    so an unresolved freeze is a finding, not an artifact).

E1  THE WALL. x^2 at sqrt(r) for r in {2, 3, 6, 3/2, 7/3, 17/12},
    input quotients exact (surd CF), scanned to depth 200: e(n)
    frozen at e*(r) — computed independently as the reader's output
    on a straddling interval (r - eps, r + eps), stable across two
    eps scales — and the delay slope tends to 1.

E2  THE MAP-BLIND CONDUCTOR LAW. Witnesses phi, 1+sqrt2, 1+sqrt3,
    3+sqrt2, 2+sqrt3, 3phi (all quadratic, squares irrational). For
    each: the algebraic side computes (i_in, ell_in, i_out, ell_out)
    exactly (unit indices of the multiplier orders of Z+Zy and
    Z+Zy^2, tail periods, eta = eps^i asserted exactly on both
    sides); the dynamic side measures emission slope and the two
    streams' denominator rates. Verdicts: sigma * r_out/r_in = 1
    within 6%; measured rate ratio = the algebraic ratio within 6%;
    delay bounded iff ratio 1 (max delay over the second half of
    depths at most the first half's max plus one).

E3  THE HUG DECOUPLING. m = 10, 20, 40: input = sqrt2's first m
    quotients + all-1s tail. Verdicts: e(n) = 0 while the input
    still agrees with sqrt2 (scanned at n = 3, m/2, m-1); first
    depth with e >= 2 lands within 4 of m; the giant output
    quotient satisfies (ln N_40 - ln N_10)/30 = 2 ln(1+sqrt2)
    within 5%; the committed-to-consumed scale ratio is 0 mid-hug
    and recovers at the full-commitment depth; the hug ENDS
    (contrast E1). [Sharpened after the first run: the original
    scan horizon m + 30 assumed the giant quotient commits once the
    input repays the hugged scale ln(1/delta) — a freeze-time
    arithmetic slip: the quotient N ~ 1/delta sits in a cell of
    size ~ 1/N^2 (the Stern-Brocot length formula the rig itself
    uses), so committing it costs 2 ln N, and the full-commitment
    depth is n* = m(1 + r_sqrt2/r_phi) = 2.832 m (per-digit scale
    rates r_sqrt2 = 2 ln(1+sqrt2), r_phi = 2 ln phi: consumed scale
    m r_sqrt2 + (n - m) r_phi reaches 2 m r_sqrt2 there). The
    first run's prints at
    m = 20, 40 showed e frozen at the 2-digit prefix [1, 1] through
    m + 30, exactly the waiting regime the corrected account
    demands; the scale account itself holds unchanged. The engine
    now scans to n* + 10 and verifies the waiting regime and the
    commitment depth as positive checks.]

E4  THE CROSS-WINDOW LAW. Base-10 interval reader (decimal digits
    common to the squared decimal input interval; the input interval
    from exact isqrt floors, verified exact): x^2 at sqrt2 freezes
    at 0 committed places, at sqrt(3/2) freezes at 1 (the integer
    part), at sqrt(1/3) GROWS (n - 2 places by depth n). The CF
    reader at sqrt(1/3) freezes at e* = 1: one input, one map, one
    window reads on while the other walls.

E5  THE INVERSE ASYMMETRY. sqrt(x) via outer rational bounds
    (isqrt at denominator 10^80, slack far below every scanned
    interval): e grows at sqrt2, phi, 3+sqrt2 (outputs 2^{1/4},
    sqrt(phi), sqrt(3+sqrt2), all irrational).

PREDICTIONS (fixed before the run)
----------------------------------
P1  THE WALL: e frozen at e* = {sqrt2: 0, sqrt3: 0, sqrt6: 0,
    sqrt(3/2): 1, sqrt(7/3): 1, sqrt(17/12): 3} at every scanned
    depth beyond onset; delay slope >= 0.95 at depth 200.
P2  THE MAP-BLIND LAW: algebraic ratios {phi: 1, 1+sqrt2: 1,
    1+sqrt3: 2, 3+sqrt2: 2, 2+sqrt3: 2} (hand-derived: phi^2 keeps
    phi's own tail; 1+sqrt2 compensates, index 1->2 against period
    1->2; the other three hit conductor-2/4/6 lattices at doubled
    index); (x^2, 3phi) is the sight-unseen row — the formula side
    (i(9phi+9) = 12 expected from the Fibonacci coefficient, ell
    unknown) must equal the measured emission with no hand input.
    sigma * r_out/r_in = 1 within 6% at every row; ratio-1 rows
    read at bounded delay — a NON-Mobius map reading a quadratic
    stream at bounded delay.
P3  THE HUG: flat at 0 through depth m - 1, resolution within 4 of
    m, giant-quotient slope 2 ln(1+sqrt2) = 1.7627 within 5%
    (difference across m kills the O(1)), scale repaid at the
    cliff, the hug ends. [As first frozen this predicted repayment
    by depth m + 30; the corrected commitment depth is 2.832 m —
    see the E3 bracket. The flat/resolution/slope/repayment claims
    stand at the corrected horizon; the m + 30 horizon itself was
    the slip.]
P4  THE CROSS-WINDOW: base-10 freezes {sqrt2: 0, sqrt(3/2): 1},
    grows at sqrt(1/3); CF freezes at sqrt(1/3) at e* = 1.
P5  THE INVERSE: e grows at all three witnesses (e(60) > e(30) >
    e(15), e(60) >= 15); no freeze.

KILL-SHAPES: (x^2, phi) stalling linearly kills map-blindness (the
map itself would tax the read); sqrt2's reader emitting unboundedly
kills the wall criterion. The 6% and 5% tolerances are the margins
to distrust — read the prints, not only the verdicts.

Scopes are small (seconds); every engine prints its table, the
checks encode the predictions above, and the exit status is nonzero
on any failure.

FINDINGS (entered after the run; ALL ENGINES PASS)
--------------------------------------------------
P1  THE WALL CONFIRMED. x^2 at sqrt(r) freezes at exactly e*(r) —
    {sqrt2, sqrt3, sqrt6: 0; sqrt(3/2), sqrt(7/3): 1;
    sqrt(17/12): 3}, every value equal to the straddling-interval
    ceiling (stable across eps scales) and constant at depths
    50/100/200; delay slope 1.000/0.995/0.985 at depth 200. The
    first permanent walls in the CF corpus: emission DIES (slope 1)
    where the Mobius rate stall only slowed it (slope 1 - sigma).
P2  THE MAP-BLIND CONDUCTOR LAW CONFIRMED. All six rows: eta =
    eps^i exact on both lattices; sigma * rate ratio in
    [0.9917, 0.9976]; measured ratio = the algebraic
    (i_out/i_in)(ell_in/ell_out) within 1% everywhere — phi 1.0000
    (i 1->1, ell 1->1: phi^2 = phi + 1 keeps the tail), 1+sqrt2
    0.9967 (i 1->2 against ell 1->2 — compensation), 1+sqrt3 1.9951,
    3+sqrt2 1.9913 (i 1->4, the conductor-6 lattice), 2+sqrt3
    1.9862 (all i-doubling rows), and the sight-unseen 3phi row:
    i 4->12, ell 2->6, ratio 1, measured 0.9917 — the formula
    landed with no hand input. Ratio-1 rows read at BOUNDED delay:
    a non-Mobius map reading quadratic streams at bounded delay
    (phi, 1+sqrt2, 3phi). The conductor law never sees the map —
    only the orbit pair.
P3  THE HUG DECOUPLING CONFIRMED, WITH ONE FREEZE-TIME SLIP. Flat
    at e = 0 through every hug (m = 10, 20, 40 — bounded input
    digits, no giant input quotient); resolution at exactly m;
    the giant output quotient commits at 29/60/113 vs the corrected
    n* = 2.832 m = 28/57/113; ln N = 16.49/34.11/69.37, slope
    1.7627 = 2 ln(1+sqrt2) EXACT to four figures; scale repay
    0.909/0.942/0.980 at commitment; emission resumes past the
    giant (e = 19/21/22 at n* + 40). The slip: the frozen horizon
    m + 30 forgot the giant quotient's own cell scale 2 ln N (cells
    at quotient N have size ~ 1/N^2), so full commitment costs the
    hugged scale TWICE — the m = 20, 40 waiting regime (prefix
    [1, 1] only through m + 30) is the corrected account's positive
    print; the scale account itself held unchanged.
P4  THE CROSS-WINDOW LAW CONFIRMED. Base-10 freezes at sqrt2 (0
    places) and sqrt(3/2) (1 place, the integer part) at depths
    20/60/120; base-10 READS ON at sqrt(1/3) (n places at depth n)
    while CF freezes there at e* = 1 — one input, one map: walled
    at the grid whose vertex set contains 1/3, read at the grid
    whose vertex set does not. Every base-b wall is a CF wall
    (Z[1/b] inside Q); the CF grid is the maximal-exposure grid
    among rational-vertex grids.
P5  THE INVERSE ASYMMETRY CONFIRMED. sqrt(x) emission grows at all
    three witnesses (10/27/54, 6/12/25, 8/18/40 at depths
    15/30/60): the inverse map is wall-free while the forward map
    walls at every sqrt(r).

Tier summary: the wall criterion (e(n) -> infinity iff the image
is irrational; frozen at e*(r) at a rational image) is a RULE at
the scanned witnesses with the two-line interior/vertex argument
above (the argument is elementary and general for continuous
strictly monotone maps; only x^2 and sqrt(x) are scanned). The
wall SET of x^2 = the square roots of the rationals is the
criterion's immediate consequence (same tier). The map-blind
conductor law is a RULE at the six scanned pairs (eta = eps^i
exact; one row sight-unseen) (settled since: PROVED at scope by
explore_cf_flow.py's rate forcing — any monotone map with
continuous nonzero derivative is conductor-priced at quadratic
orbits). The hug decoupling and the
double-payment commitment depth 2.832 m are RULES at the scanned
family. The cross-window statement is a rule at the scanned
witnesses; vertex-set inclusion Z[1/b] in Q is a property. The
inverse asymmetry's emptiness argument (rational sqrt forces
rational input) is a property; the growth prints are observations
at three witnesses. The redundancy cure (no permanent walls at
positive-Lebesgue covers) is INHERITED from the reading lemma and
stream correction (explore_reading_geometry.py), not re-verified
here.

RUN RECORD: ALL ENGINES PASS, < 1 s, exit 0 bare (failure path
fired twice while this rig was built: the m + 30 horizon FAILs above). E0
three controls (bounded read, rate stall, finite Mobius hug); E1
six-witness wall table; E2 six-row conductor table as quoted; E3
three-hug table with the giant-commitment depths; E4 two frozen +
one growing base-10 witness + the CF sqrt(1/3) freeze; E5 three
growing sqrt(x) witnesses.
"""

from fractions import Fraction
from math import isqrt, log

from explore_cf_window import (cylinder, interval_cf, emitted, q_rate,
                               rational_cf, WITNESSES)
from explore_cf_conductor import (surd_cf, lattice_data, unit_index,
                                  power_equals, eps_of)


# ------------------------------------------------------------------ #
# harness                                                              #
# ------------------------------------------------------------------ #

FAILS = []


def check(label, ok):
    print(("  PASS  " if ok else "  FAIL  ") + label)
    if not ok:
        FAILS.append(label)


# ------------------------------------------------------------------ #
# readers                                                              #
# ------------------------------------------------------------------ #

def surd_digits(P, D, Q, count):
    """First `count` CF quotients of (P + sqrt(D))/Q, exactly."""
    pre, per, _state, _D2 = surd_cf(P, D, Q)
    digs = list(pre)
    while len(digs) < count:
        digs += per
    return digs[:count]


def emitted_sq(quots, n):
    """Output quotients determined by squaring the depth-n cylinder."""
    lo, hi = cylinder(quots, n)
    return interval_cf(lo * lo, hi * hi)


def e_star(r, exp=9):
    """The reader's ceiling at rational r: quotients common to a
    straddling interval (r - eps, r + eps)."""
    eps = Fraction(1, 10 ** exp)
    return len(interval_cf(r - eps, r + eps))


def sqrt_outer(fr, K=10 ** 80):
    """Outer rational bounds for sqrt(fr): (lo, hi) with
    lo <= sqrt(fr) <= hi and slack < 2/K."""
    n = isqrt(fr.numerator * K * K // fr.denominator)
    return Fraction(n, K), Fraction(n + 1, K)


def emitted_sqrt(quots, n):
    """Output quotients determined by the sqrt of the depth-n
    cylinder, via conservative outer bounds."""
    lo, hi = cylinder(quots, n)
    slo, _ = sqrt_outer(lo)
    _, shi = sqrt_outer(hi)
    return interval_cf(slo, shi)


def scale(x):
    """ln(1/x) for a positive Fraction, exactly enough."""
    return log(x.denominator) - log(x.numerator)


# ------------------------------------------------------------------ #
# E0: positive controls                                               #
# ------------------------------------------------------------------ #

def e0():
    print("\nE0 POSITIVE CONTROLS")
    phi = WITNESSES["phi"]

    d30 = 30 - len(emitted((0, 1, 1, 0), phi, 30))
    d60 = 60 - len(emitted((0, 1, 1, 0), phi, 60))
    print(f"    1/x at phi: delay {d30} at 30, {d60} at 60")
    check("control: 1/x at phi bounded (|delay| <= 2)",
          abs(d30) <= 2 and abs(d60) <= 2)

    s150 = len(emitted((2, 0, 0, 1), phi, 150)) / 150
    print(f"    2x at phi: emission slope {s150:.3f}")
    check("control: 2x at phi stalls (slope in [0.30, 0.37])",
          0.30 <= s150 <= 0.37)

    pre = rational_cf(Fraction(55, 178))          # preimage of 55/89 under 2x
    hug_in = pre + [1] * 120
    k = len(pre)
    e_at, e_past = (len(emitted((2, 0, 0, 1), hug_in, n))
                    for n in (k, k + 40))
    print(f"    Mobius hug (2x, preimage len {k}): e({k}) = {e_at}, "
          f"e({k + 40}) = {e_past}")
    check("control: the Mobius hug ENDS (e grows past the preimage)",
          e_past >= e_at + 10)


# ------------------------------------------------------------------ #
# E1: the wall                                                        #
# ------------------------------------------------------------------ #

WALLS = {"sqrt2": Fraction(2), "sqrt3": Fraction(3), "sqrt6": Fraction(6),
         "sqrt(3/2)": Fraction(3, 2), "sqrt(7/3)": Fraction(7, 3),
         "sqrt(17/12)": Fraction(17, 12)}
ESTAR_PRED = {"sqrt2": 0, "sqrt3": 0, "sqrt6": 0,
              "sqrt(3/2)": 1, "sqrt(7/3)": 1, "sqrt(17/12)": 3}


def e1():
    print("\nE1 THE WALL: x^2 at sqrt(r), r rational")
    print("    witness        e*  e(50) e(100) e(200)  delay/n(200)")
    for name, r in WALLS.items():
        digs = surd_digits(0, r.numerator * r.denominator,
                           r.denominator, 220)
        es = e_star(r)
        es2 = e_star(r, exp=15)
        evals = {n: len(emitted_sq(digs, n)) for n in (50, 100, 200)}
        slope = (200 - evals[200]) / 200
        print(f"    {name:12s}  {es:2d}  {evals[50]:4d}  {evals[100]:5d} "
              f" {evals[200]:5d}   {slope:.3f}")
        check(f"{name}: e* stable across eps scales", es == es2)
        check(f"{name}: e* = {ESTAR_PRED[name]} as predicted",
              es == ESTAR_PRED[name])
        check(f"{name}: e frozen at e* at depths 50/100/200",
              evals[50] == evals[100] == evals[200] == es)
        check(f"{name}: delay slope >= 0.95", slope >= 0.95)


# ------------------------------------------------------------------ #
# E2: the map-blind conductor law                                     #
# ------------------------------------------------------------------ #

E2_ROWS = {"phi": (1, 5, 2), "1+sqrt2": (1, 2, 1), "1+sqrt3": (1, 3, 1),
           "3+sqrt2": (3, 2, 1), "2+sqrt3": (2, 3, 1), "3phi": (3, 45, 2)}
RATIO_PRED = {"phi": 1, "1+sqrt2": 1, "1+sqrt3": 2,
              "3+sqrt2": 2, "2+sqrt3": 2}          # 3phi: sight-unseen


def e2():
    print("\nE2 THE MAP-BLIND CONDUCTOR LAW: x^2 at quadratic streams")
    print("    witness   i_in ell_in i_out ell_out  pred   "
          "measured  sigma*ratio")
    for name, (P, D, Q) in E2_ROWS.items():
        f_in, ell_in, eta_in, d0 = lattice_data(P, D, Q)
        P2, D2, Q2 = P * P + D, 4 * P * P * D, Q * Q
        f_out, ell_out, eta_out, d0b = lattice_data(P2, D2, Q2)
        assert d0 == d0b
        eps = eps_of(d0)
        i_in = unit_index(f_in, d0, eps)
        i_out = unit_index(f_out, d0, eps)
        check(f"{name}: eta = eps^i exact on both lattices",
              power_equals(eps, i_in, eta_in, d0)
              and power_equals(eps, i_out, eta_out, d0))
        pred = Fraction(i_out * ell_in, i_in * ell_out)

        digs = surd_digits(P, D, Q, 300)
        N = 240
        out = emitted_sq(digs, N)
        sigma = len(out) / N
        ratio = q_rate(out) / q_rate(digs[:N + 1])
        print(f"    {name:8s}  {i_in:3d}  {ell_in:4d}  {i_out:4d} "
              f" {ell_out:5d}   {str(pred):5s}  {ratio:7.4f}   "
              f"{sigma * ratio:.4f}")
        check(f"{name}: sigma * rate ratio = 1 within 6%",
              abs(sigma * ratio - 1) <= 0.06)
        check(f"{name}: measured ratio = algebraic ratio within 6%",
              abs(ratio / float(pred) - 1) <= 0.06)
        if name in RATIO_PRED:
            check(f"{name}: algebraic ratio = {RATIO_PRED[name]} "
                  "as hand-derived", pred == RATIO_PRED[name])
        if pred == 1:
            delays = [n - len(emitted_sq(digs, n))
                      for n in range(10, 241, 10)]
            half = len(delays) // 2
            check(f"{name}: ratio 1 => bounded delay (non-growing)",
                  max(delays[half:]) <= max(delays[:half]) + 1)


# ------------------------------------------------------------------ #
# E3: the hug decoupling                                              #
# ------------------------------------------------------------------ #

def e3():
    print("\nE3 THE HUG DECOUPLING: sqrt2-prefix inputs, all-1s tails")
    sqrt2 = surd_digits(0, 2, 1, 60)
    lnN = {}
    for m in (10, 20, 40):                       # even m: y_m < sqrt2
        digs = sqrt2[:m] + [1] * 260
        n_star = round(2.832 * m)
        n_full = n_star + 10
        flat = all(len(emitted_sq(digs, n)) == 0
                   for n in (3, m // 2, m - 1))
        n_res = next(n for n in range(m - 4, m + 30)
                     if len(emitted_sq(digs, n)) >= 2)
        n_giant = next(n for n in range(n_res, n_full + 40)
                       if len(emitted_sq(digs, n)) >= 3)
        out = emitted_sq(digs, n_full)
        e_later = len(emitted_sq(digs, n_full + 30))
        giant = max(out[:4])
        lnN[m] = log(giant)
        lo, hi = cylinder(digs, n_full)
        clo, chi = cylinder(out, len(out) - 1)
        repay = scale(chi - clo) / scale(hi - lo)
        print(f"    m = {m:2d}: flat {flat}, resolves at {n_res}, "
              f"giant commits at {n_giant} (n* = {n_star}), "
              f"ln N = {lnN[m]:.2f}, scale repay {repay:.3f}, "
              f"e(n*+10) = {len(out)}, e(n*+40) = {e_later}")
        check(f"m={m}: e = 0 through the hug", flat)
        check(f"m={m}: resolution within 4 of m", abs(n_res - m) <= 4)
        if m >= 20:
            check(f"m={m}: waiting regime — prefix only at m + 30",
                  len(emitted_sq(digs, m + 30)) == 2)
        check(f"m={m}: giant commits at n* within 8% + 4",
              abs(n_giant - n_star) <= 0.08 * n_star + 4)
        check(f"m={m}: the hug ENDS (emission resumes past the giant)",
              len(out) >= 4 and e_later >= len(out) + 3)
        check(f"m={m}: scale repaid at commitment (ratio in "
              f"[0.8, 1.05])", 0.8 <= repay <= 1.05)
    slope = (lnN[40] - lnN[10]) / 30
    target = 2 * log(1 + 2 ** 0.5)
    print(f"    giant-quotient slope {slope:.4f} vs 2 ln(1+sqrt2) = "
          f"{target:.4f}")
    check("giant-quotient slope = 2 ln(1+sqrt2) within 5%",
          abs(slope / target - 1) <= 0.05)


# ------------------------------------------------------------------ #
# E4: the cross-window law                                            #
# ------------------------------------------------------------------ #

def dec_input(r, n):
    """The base-10 depth-n input interval for sqrt(r), exact."""
    d = isqrt(r.numerator * 10 ** (2 * n) // r.denominator)
    assert d * d * r.denominator <= r.numerator * 10 ** (2 * n) \
        < (d + 1) * (d + 1) * r.denominator
    return Fraction(d, 10 ** n), Fraction(d + 1, 10 ** n)


def dec_common(lo, hi, tmax=400):
    """Committed decimal places (integer part = the first) for an
    interval: the number of scales at which the floors agree."""
    e = 0
    while e <= tmax:
        s = 10 ** e
        if (lo * s).numerator // (lo * s).denominator \
                != (hi * s).numerator // (hi * s).denominator:
            return e
        e += 1
    return e


def e4():
    print("\nE4 THE CROSS-WINDOW LAW: one map, two grids")
    for name, r, frozen in (("sqrt2", Fraction(2), 0),
                            ("sqrt(3/2)", Fraction(3, 2), 1)):
        vals = {}
        for n in (20, 60, 120):
            lo, hi = dec_input(r, n)
            vals[n] = dec_common(lo * lo, hi * hi)
        print(f"    base-10, x^2 at {name}: committed places "
              f"{vals[20]}/{vals[60]}/{vals[120]} at depths 20/60/120")
        check(f"base-10 freezes at {name} at {frozen}",
              all(v == frozen for v in vals.values()))
    third = Fraction(1, 3)
    vals = {}
    for n in (20, 60, 120):
        lo, hi = dec_input(third, n)
        vals[n] = dec_common(lo * lo, hi * hi)
    print(f"    base-10, x^2 at sqrt(1/3): committed places "
          f"{vals[20]}/{vals[60]}/{vals[120]} — no wall (1/3 not a "
          f"decimal vertex)")
    check("base-10 READS ON at sqrt(1/3) (>= n - 2 places)",
          all(vals[n] >= n - 2 for n in (20, 60, 120)))

    digs = surd_digits(0, 3, 3, 220)               # sqrt(1/3) = sqrt3/3
    es = e_star(third)
    evals = {n: len(emitted_sq(digs, n)) for n in (50, 200)}
    print(f"    CF, x^2 at sqrt(1/3): e* = {es}, e(50) = {evals[50]}, "
          f"e(200) = {evals[200]} — walled (1/3 IS a CF vertex)")
    check("CF freezes at sqrt(1/3) at e* = 1",
          es == 1 and evals[50] == evals[200] == 1)


# ------------------------------------------------------------------ #
# E5: the inverse asymmetry                                           #
# ------------------------------------------------------------------ #

def e5():
    print("\nE5 THE INVERSE ASYMMETRY: sqrt(x) is wall-free")
    for name, (P, D, Q) in (("sqrt2", (0, 2, 1)), ("phi", (1, 5, 2)),
                            ("3+sqrt2", (3, 2, 1))):
        digs = surd_digits(P, D, Q, 80)
        e15, e30, e60 = (len(emitted_sqrt(digs, n)) for n in (15, 30, 60))
        print(f"    sqrt(x) at {name}: e = {e15}/{e30}/{e60} "
              f"at depths 15/30/60")
        check(f"sqrt(x) at {name}: e grows, no freeze",
              e15 < e30 < e60 and e60 >= 15)


if __name__ == "__main__":
    e0()
    e1()
    e2()
    e3()
    e4()
    e5()
    print("\n" + ("ALL ENGINES PASS" if not FAILS
                  else f"{len(FAILS)} FAILURES: {FAILS}"))
    raise SystemExit(1 if FAILS else 0)
