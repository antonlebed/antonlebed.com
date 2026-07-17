"""The flow layer of the continued-fraction window: readers run on
flow time, and rate forcing is a theorem.

THE QUESTION
------------
explore_cf_window.py found the metric pair (digit clock vs scale
clock, exchange rate = the Gauss-map entropy); explore_cf_conductor.py
found the conductor law (the scale rate of a quadratic stream is
r = 2 i R_K / ell, reading delay an instrument for unit indices) and
proved the unit gate's necessity up to two named lean points — RATE
FORCING (rate mismatch implies linear digit delay, both signs) and
the sign-crossing unimodular legs of the Smith transport;
explore_cf_nonlinear.py found the conductor law MAP-BLIND at x^2.
This script asks whether one classical object organizes all of it:
are the window's two clocks the return clock and the flow clock of a
suspension — the continued-fraction cross-section of the modular
geodesic flow — with the rate law an instance of Abramov's formula
read per orbit, and rate forcing a provable piece of return-time
bookkeeping?

Classical background imported, not re-proved (each marked where
used): the suspension/cross-section presentation, roof functions,
return times, and Abramov's entropy formula; Rokhlin's formula
h(T) = INT ln|T'| dmu for these interval maps; Shannon-McMillan-
Breiman; the continued-fraction cross-section of the geodesic flow
on the modular surface (Artin; Series; Adler-Flatto); closed
geodesics <-> quadratic irrationals, the surface geodesic closing
at the NORM +1 automorph (length 2 ln eta at even tail periods,
4 ln eta when N(eta) = -1); divergent
geodesic rays <-> rational endpoints; badly approximable <-> bounded
partial quotients. The corpus's mint is the READING layer on top:
the reader, its emission e(n), the digit/scale delays, and the new
coinage below.

THE CRUX, resolved on paper before the engines
----------------------------------------------
THE SUSPENSION PRESENTATION. Each window's digit process is the
shift of an expanding interval map T with an absolutely continuous
invariant own measure, and its per-digit scale is ln|T'| (base b:
constant ln b; the Gauss map: 2 ln(1/x)). Taking ln|T'| as the ROOF,
Rokhlin's formula says digit entropy = mean roof, so by Abramov the
suspension flow has entropy exactly 1: every such window runs its
scale flow at entropy 1 — entropy per digit equals scale per digit,
and the exchange-rate law of explore_cf_window.py is this identity
read per-stream. A positional window is the CONSTANT-ROOF case (the
zero-variance degeneration; its suspension circle is the scale
circle of the leading window's own measure — Benford is the roof
coordinate's marginal). Only the CF window's suspension is a named
classical flow — the modular geodesic flow — and there a quadratic
tail rides a closed geodesic: the suspension orbit's flow period
per tail period is 2 ln eta = 2 i R_K (the surface geodesic itself
closes at the norm +1 automorph — one or two tail periods by the
sign of N(eta)), so the conductor rate r = 2 i R_K / ell is flow
period per return: the per-orbit Abramov mean. The exact anchor,
testable in exact arithmetic:

  THE ROOF IDENTITY. Over one tail period, the product of the
  complete quotients w_j (equivalently, of 1/x_j along the Gauss
  orbit) equals the period matrix's dominant eigenvalue eta — the
  roof's Birkhoff period-sum is the closed orbit's flow period
  2 ln eta, exactly, not just in the mean.

THE COMMITMENT DEFICIT (new coinage). For a reader of f at input y,
with I_n the depth-n input cylinder and J_n = f(I_n) the image
interval, the deficit is

    D(n) = scale(J_n) - scale(committed cell),

scale = ln(1/length). Emission is e(n) = max{e : J_n inside C_e(z)},
z = f(y): the common prefix of an interval is the deepest cell of z
containing it, because cells nest.

THE COMMITMENT BOUND (proved). Let f be monotone and C^1 with
f'(y) != 0, and let z = f(y) be irrational, badly approximable with
partial quotients bounded by A, and not a cell vertex. Then

    0 <= D(n) <= 3 ln(A + 2) + O(1).

Proof. Lower: the committed cell contains J_n, so its scale is at
most scale(J_n). Upper: both endpoints of C_e(z) are rationals of
denominator at most 2 q_e, badly approximable gives
|z - p/q| >= 1/((A+2) q^2) for EVERY rational p/q (non-convergents
by the best-approximation theorem, convergents by the quotient
bound), and |C_e| >= 1/(2 q_e^2); so dist(z, boundary C_e) >=
c_A |C_e| with c_A ~ 1/(8(A+2)). The committed cell C_e(n) fails to
refine only while J_n still crosses the boundary of the NEXT cell,
so |J_n| >= dist(z, boundary C_{e(n)+1}) >= c_A |C_{e(n)+1}|, and
one refinement step costs at most the cell ratio
|C_e|/|C_{e+1}| <= (A+1)(A+2) (from q_{e+1} <= (A+1) q_e); hence
D(n) <= ln(1/c_A) + 2 ln(A+2) + O(1) = 3 ln(A+2) + O(1). (The
measured peaks sit at ~2 ln A, the full excursion cost — below the
proof's constant.) Since scale(J_n) = scale(I_n) + O(1) (|f'|
bounded above and below near y), the reader is SCALE-SYNCED at every
badly approximable non-vertex output, regardless of the map: the
scale clock always syncs; only the digit clock forks. A wall is the
bound's infinite endpoint — z ON a vertex (z rational: the output
ray divergent, the cusp-bound geodesic).

RATE FORCING (proved — the first lean point closes). Add that y has
an eventually periodic tail and z = f(y) is quadratic. Then
ln q_n(y) = n ln(eta_in)/ell_in + O(1) (linear recurrence, dominant
eigenvalue), so scale(I_n) = n r_in + O(1), scale(C_e(z)) =
e r_out + O(1), and the commitment bound gives

    e(n) = (r_in / r_out) n + O(1),   r_in/r_out =
    (i_in ell_out)/(i_out ell_in), a RATIONAL (R_K cancels).

Corollaries. (a) The digit delay n - e(n) = n (1 - r_in/r_out) +
O(1) is bounded iff the rates match, else linear with the mismatch
sign — rate forcing, an iff, both signs. (b) MAP-BLINDNESS: f
enters only through |f'| (an O(1)) and through which output orbit
it selects — any monotone C^1 map with nonzero derivative is
conductor-priced at quadratic orbits; the map-blind law of
explore_cf_nonlinear.py is proved at this scope. (c) The SECOND
lean point also closes at the scope the necessity proof needs: the
Smith transport only ever needs unimodular maps read boundedly at
QUADRATIC streams, and a unimodular image is GL(2,Z)-equivalent
(Serret) — same tail, same (i, ell), ratio 1, bounded by (a). The
interval-reader proof is transducer-free; no negation rewrites.
(The word factorization still carries the positive direction at
general non-quadratic streams — that lean narrows to its honest
scope but does not vanish.)

THE CUSP READING. A hug is a finite cusp excursion of the output
ray: the excursion's height is ~ ln N (N the pending giant
quotient) and committing N costs 2 ln N — up AND down the cusp —
so the deficit peaks at ~ 2 ln N just before the quotient commits
(the reader has paid the whole excursion while the committed cell
still sits at the excursion's base). A permanent wall is the
excursion that never
returns. NOT annexed: whether f sends y onto a vertex is a property
of the pair (map, point) — the flow layer prices rates and delays
from orbit invariants; which ray the output is remains diophantine
data (under x^2, phi's output is a closed geodesic and sqrt2's is a
cusp ray).

Hand-derived rows fixed before any engine ran (sight-unseen where
marked):
  (x^2, 1+sqrt3): output 4+2sqrt3 = [7;(2,6)], eta = 7+4sqrt3 =
    eps^2, i 1->2, ell 2->2, rho := r_in/r_out = 1/2.
  (sqrt x, 7+4sqrt3): input tail (1,12), eta = (2+sqrt3)^2, i = 2,
    ell = 2; output 2+sqrt3 = [3;(1,2)], i = 1, ell = 2; rho = 2 —
    the inverse map RUNS AHEAD linearly (fresh row, sight-unseen).
  (x/2, 2phi): input 2phi (i = 3, ell = 1), output phi, rho = 3 —
    run-ahead (sight-unseen).
  (7x, phi): output 7phi = [11;(3,15)], i = 8, ell = 2, rho = 1/4;
    output quotient bound A = 15 vs A = 4 for (2x, phi) — the
    big-quotient deficit witness.

THE DESIGN
----------
Exact machinery reused: interval reader, cylinders, surd CF, exact
eigenvalues, unit indices (explore_cf_window.py,
explore_cf_conductor.py, explore_cf_nonlinear.py). No closed form
from the target laws enters any rig.

E0  POSITIVE CONTROLS (read before any verdict): 1/x at phi reads
    at bounded delay; 2x at phi stalls at slope ~ 1/3. (The check()
    harness's failure path has fired live in this rig family —
    explore_cf_nonlinear.py's run record.)

E1  THE ROOF IDENTITY, exact: for 25 tails — phi, sqrt2, sqrt3,
    1+sqrt3, sqrt13, sqrt19, the family (a + sqrt(a^2+4))/2 for
    a = 1..10, and the output tails 2phi, 3phi, 7phi, phi^2,
    4+2sqrt3, 7+4sqrt3, 2+sqrt3, sqrt50, sqrt27 — the product of
    the complete quotients over one period, computed in exact
    Q(sqrt d0) arithmetic, equals the period matrix's eigenvalue
    eta EXACTLY (and eta = eps^i exactly where the row's index is
    quoted).

E2  RATE FORCING AT O(1): ten pairs — (2x, phi) rho 1/3, (3x, phi)
    1/2, (x/2, phi) 1/3, (2x, sqrt2) 1 (the Pell control),
    (5x, sqrt2) 1/3, (3x, sqrt3) 1/3, (x^2, phi) 1,
    (x^2, 1+sqrt3) 1/2, (sqrt x, 7+4sqrt3) 2, (x/2, 2phi) 3.
    Per pair: the algebraic rho from lattice data must equal the
    hand value; sup over the second half of depths of
    |e(n) - rho n| at most the first half's sup + 2 (the O(1)
    flatness); terminal delay sign = sign(1 - rho) at mismatched
    rows. Depth 240 (the sqrt reader uses outer bounds sharp to
    10^-400, far below every cell at this depth).

E3  THE DEFICIT: D(n) >= 0 and flat (same two-half criterion,
    tolerance 0.75) at (2x, phi) — mismatched yet scale-synced —
    (2x, sqrt2), (x^2, phi), (7x, phi); the ordering
    D_max(7x, phi) > D_max(2x, phi) (excursion height grows with
    the quotient; magnitudes printed, read against ~2 ln A by
    hand); at the WALL (x^2, sqrt2), D(n) grows linearly with
    least-squares slope on the second half = r(sqrt2) =
    2 ln(1+sqrt2) = 1.7627 within 5%. [Sharpened after the first
    run: D(n) is defined only from the FIRST NONEMPTY emission —
    before any output digit there is no committed cell (the
    committed set is the whole ray), and the first draft's
    "committed scale 0" convention manufactured D < 0 wherever the
    image interval was still longer than 1 (the n = 1..2 startup at
    (x^2, phi) and (7x, phi): D_min -0.56 and -1.25, both at empty
    emission; every nonempty-emission depth satisfies D >= 0
    exactly). The wall series keeps the all-n convention, where
    empty emission is the phenomenon itself.]

PREDICTIONS, fixed before any engine ran:
  P-A: E1 exact equality at every row.
  P-B: E2 passes at all ten rows, including the two sight-unseen
       run-ahead rows (rho = 2, 3) — the run-ahead side of rate
       forcing has never been scanned at designed witnesses.
  P-C: E3 deficits nonnegative and flat at all four bounded rows;
       the wall slope lands at 1.7627 +- 5%; the ordering holds.
       (The 5% band is the one soft margin: the kill is the slope
       VALUE, derived; if it misses, read the prints against the
       hand law before touching the band.)

FINDINGS (entered after the run; the printed tables are the record)
-------------------------------------------------------------------
All three predictions landed.

E1 THE ROOF IDENTITY: exact equality prod == eta at all 25 tails —
periods up to 6, fields d0 = 2, 3, 5, 10, 13, 17, 26, 29, 53, 85 —
two independent exact computations (quotient product vs the
eigenvalue linear form) agreeing in Q(sqrt d0). The conductor rate
2 i R_K / ell is the roof's Birkhoff period-average: Abramov read
per orbit.

E2 RATE FORCING AT O(1): at every one of the ten rows the algebraic
rho equals the hand value and |e(n) - rho n| is FLAT — residual sup
at most 2.00 over 240 depths, second half never above the first.
Terminal delays vs the predicted n(1 - rho): 160/160, 120/120,
158/160, 0/0, 160/160, 160/160, 1/0, 120/120, -242/-240 (the
sight-unseen sqrt run-ahead), -482/-480 (the sight-unseen rho = 3
run-ahead). Both run-ahead rows land: rate forcing holds with BOTH
signs at designed witnesses, through a nonlinear map (sqrt x) as
through Mobius ones.

E3 THE COMMITMENT DEFICIT: D(n) >= 0 exactly and flat at all four
bounded rows — D_max 2.015 (2x @ phi: digit delay linear, scale
SYNCED), 2.199 (2x @ sqrt2), 0.831 (x^2 @ phi), 5.032 (7x @ phi);
the ordering 5.032 > 2.015 confirms the excursion reading, and the
magnitudes sit at the predicted ~2 ln A order (2 ln 15 = 5.42 at
A = 15; 2 ln 4 = 2.77 at A = 4). At the wall the deficit's
second-half slope is 1.7627 vs 2 ln(1+sqrt2) = 1.7627 — exact to
four decimals — with D(240) = 422.05 ~ 240 r_in: the wall is the
deficit's linear-growth regime, the excursion that never returns.

Tier summary. THE COMMITMENT BOUND and RATE FORCING are proved
algebraically at their stated scopes (the proofs above: monotone
C^1 maps with nonzero derivative at badly approximable non-vertex
outputs; the rate form at eventually periodic tails with quadratic
outputs) and verified dynamically at the ten scanned pairs — rules
at proved scope. Their corollaries inherit: map-blindness of the
conductor pricing is proved at that scope (upgrading the six-pair
rule of explore_cf_nonlinear.py); the unit gate's necessity at
quadratic streams (explore_cf_conductor.py) now rests on proved
pieces alone — both former lean points (rate forcing; the
sign-crossing unimodular legs of the Smith transport) close, the
second because the transport only needs unimodular maps at
quadratic streams, where GL(2,Z)-equivalence gives ratio 1. The
roof identity is classical in substance (recurrence telescoping)
and verified exactly at 25 tails; the entropy-1 statement is a
composition of classical facts (Rokhlin + Abramov) — the corpus's
content in both is the reading: scale is flow time, windows are
cross-sections, the digit clock is the return clock. The cusp
reading of hugs and walls is a dictionary translation (divergent
rays are classical); the wall itself remains a property of the
(map, point) pair — the flow layer prices rates and delays, never
which ray the output is.

RUN RECORD: ALL ENGINES PASS, ~1.1 s, exit 0 bare. The check()
failure path fired live during the mint: the first run printed two
D >= 0 FAILs, traced to the empty-emission startup convention (the
sharpening note in E3's design), not to the bound — every
nonempty-emission depth satisfies D >= 0 exactly.
"""

import os

os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")

from fractions import Fraction
from math import isqrt, log

from explore_cf_window import (cylinder, interval_cf, image_interval,
                               emitted, WITNESSES)
from explore_cf_conductor import (surd_cf, period_eigenvalue,
                                  squarefree_kernel, fmul, mobius_surd,
                                  lattice_data, unit_index, power_equals,
                                  eps_of)
from explore_cf_nonlinear import surd_digits, scale


# ------------------------------------------------------------------ #
# harness                                                              #
# ------------------------------------------------------------------ #

FAILS = []


def check(label, ok):
    print(("  PASS  " if ok else "  FAIL  ") + label)
    if not ok:
        FAILS.append(label)


# ------------------------------------------------------------------ #
# readers (image-interval form; sqrt uses deep outer bounds)           #
# ------------------------------------------------------------------ #

SQRT_K = 10 ** 400


def sqrt_outer_deep(fr):
    """Outer rational bounds for sqrt(fr), slack < 2/SQRT_K."""
    n = isqrt(fr.numerator * SQRT_K * SQRT_K // fr.denominator)
    return Fraction(n, SQRT_K), Fraction(n + 1, SQRT_K)


def img_mobius(mat):
    def img(quots, n):
        return image_interval(mat, *cylinder(quots, n))
    return img


def img_square(quots, n):
    lo, hi = cylinder(quots, n)
    return lo * lo, hi * hi


def img_sqrt(quots, n):
    lo, hi = cylinder(quots, n)
    slo, _ = sqrt_outer_deep(lo)
    _, shi = sqrt_outer_deep(hi)
    return slo, shi


def emission_series(img, quots, N):
    """e(n) for n = 1..N from the image interval's common prefix."""
    return [len(interval_cf(*img(quots, n))) for n in range(1, N + 1)]


def deficit_series(img, quots, N):
    """D(n) = scale(J_n) - scale(committed cell), for the n = 1..N
    with NONEMPTY emission: before the first output digit there is no
    committed cell (the committed set is the whole ray) and the
    deficit is undefined — a bounded startup prefix."""
    out = []
    for n in range(1, N + 1):
        lo, hi = img(quots, n)
        digs = interval_cf(lo, hi)
        if not digs:
            continue
        clo, chi = cylinder(digs, len(digs) - 1)
        out.append(scale(hi - lo) - scale(chi - clo))
    return out


def deficit_full(img, quots, N):
    """scale(J_n) - committed scale for ALL n (empty emission scored
    scale 0) — the wall series, where emission stays empty forever."""
    out = []
    for n in range(1, N + 1):
        lo, hi = img(quots, n)
        digs = interval_cf(lo, hi)
        if digs:
            clo, chi = cylinder(digs, len(digs) - 1)
            out.append(scale(hi - lo) - scale(chi - clo))
        else:
            out.append(scale(hi - lo))
    return out


def two_half_flat(series, tol):
    """sup over the second half at most the first half's sup + tol."""
    mid = len(series) // 2
    lo = max(abs(v) for v in series[:mid])
    hi = max(abs(v) for v in series[mid:])
    return hi <= lo + tol, lo, hi


# ------------------------------------------------------------------ #
# exact surd helpers                                                   #
# ------------------------------------------------------------------ #

def sq_surd(P, D, Q):
    """The surd of y^2 for y = (P + sqrt(D))/Q."""
    return P * P + D, 4 * P * P * D, Q * Q


def roof_product(P, D, Q):
    """Exact product of the complete quotients over one tail period,
    as (A, B) in Q(sqrt d0); returns (product, eta, ell, d0)."""
    pre, per, state, D2 = surd_cf(P, D, Q)
    d0, t = squarefree_kernel(D2)
    Pj, Qj = state
    prod = (Fraction(1), Fraction(0))
    for a in per:
        prod = fmul(prod, (Fraction(Pj, Qj), Fraction(t, Qj)), d0)
        Pj = a * Qj - Pj
        Qj = (D2 - Pj * Pj) // Qj
    A, B, k = period_eigenvalue(per, state, D2)
    assert k == d0
    return prod, (A, B), len(per), d0


def rho_algebraic(P, D, Q, P2, D2, Q2):
    """r_in/r_out = (i_in ell_out)/(i_out ell_in), from exact lattice
    data of input and output surds (eta = eps^i asserted both sides)."""
    f_in, ell_in, eta_in, d0 = lattice_data(P, D, Q)
    f_out, ell_out, eta_out, d0b = lattice_data(P2, D2, Q2)
    assert d0 == d0b
    eps = eps_of(d0)
    i_in = unit_index(f_in, d0, eps)
    i_out = unit_index(f_out, d0, eps)
    assert power_equals(eps, i_in, eta_in, d0)
    assert power_equals(eps, i_out, eta_out, d0)
    return Fraction(i_in * ell_out, i_out * ell_in)


# ------------------------------------------------------------------ #
# E0: positive controls                                                #
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


# ------------------------------------------------------------------ #
# E1: the roof identity                                                #
# ------------------------------------------------------------------ #

E1_ROWS = [
    ("phi", (1, 5, 2)), ("sqrt2", (0, 2, 1)), ("sqrt3", (0, 3, 1)),
    ("1+sqrt3", (1, 3, 1)), ("sqrt13", (0, 13, 1)), ("sqrt19", (0, 19, 1)),
    ("2phi", mobius_surd((2, 0, 0, 1), 1, 5, 2)),
    ("3phi", mobius_surd((3, 0, 0, 1), 1, 5, 2)),
    ("7phi", mobius_surd((7, 0, 0, 1), 1, 5, 2)),
    ("phi^2", sq_surd(1, 5, 2)),
    ("4+2sqrt3", sq_surd(1, 3, 1)),
    ("7+4sqrt3", (7, 48, 1)), ("2+sqrt3", (2, 3, 1)),
    ("sqrt50", (0, 50, 1)), ("sqrt27", (0, 27, 1)),
] + [(f"[( {a} )]", (a, a * a + 4, 2)) for a in range(1, 11)]


def e1():
    print("\nE1 THE ROOF IDENTITY: prod of complete quotients over one "
          "period == eta, exactly")
    all_ok = True
    for name, (P, D, Q) in E1_ROWS:
        prod, eta, ell, d0 = roof_product(P, D, Q)
        ok = prod == eta
        all_ok = all_ok and ok
        print(f"    {name:12s} ell {ell:2d}  d0 {d0:3d}  "
              f"prod == eta: {ok}")
    check("E1: roof identity exact at every row", all_ok)


# ------------------------------------------------------------------ #
# E2: rate forcing at O(1)                                             #
# ------------------------------------------------------------------ #

DEPTH = 240

E2_ROWS = [
    # label, img, input surd, output surd, hand rho
    ("2x @ phi", img_mobius((2, 0, 0, 1)), (1, 5, 2),
     mobius_surd((2, 0, 0, 1), 1, 5, 2), Fraction(1, 3)),
    ("3x @ phi", img_mobius((3, 0, 0, 1)), (1, 5, 2),
     mobius_surd((3, 0, 0, 1), 1, 5, 2), Fraction(1, 2)),
    ("x/2 @ phi", img_mobius((1, 0, 0, 2)), (1, 5, 2),
     mobius_surd((1, 0, 0, 2), 1, 5, 2), Fraction(1, 3)),
    ("2x @ sqrt2", img_mobius((2, 0, 0, 1)), (0, 2, 1),
     mobius_surd((2, 0, 0, 1), 0, 2, 1), Fraction(1)),
    ("5x @ sqrt2", img_mobius((5, 0, 0, 1)), (0, 2, 1),
     mobius_surd((5, 0, 0, 1), 0, 2, 1), Fraction(1, 3)),
    ("3x @ sqrt3", img_mobius((3, 0, 0, 1)), (0, 3, 1),
     mobius_surd((3, 0, 0, 1), 0, 3, 1), Fraction(1, 3)),
    ("x^2 @ phi", img_square, (1, 5, 2), sq_surd(1, 5, 2), Fraction(1)),
    ("x^2 @ 1+sqrt3", img_square, (1, 3, 1), sq_surd(1, 3, 1),
     Fraction(1, 2)),
    ("sqrt(x) @ 7+4sqrt3", img_sqrt, (7, 48, 1), (2, 3, 1), Fraction(2)),
    ("x/2 @ 2phi", img_mobius((1, 0, 0, 2)),
     mobius_surd((2, 0, 0, 1), 1, 5, 2), (1, 5, 2), Fraction(3)),
]


def e2():
    print("\nE2 RATE FORCING: e(n) = rho n + O(1), rho the conductor "
          "ratio (depth {})".format(DEPTH))
    check("E2 pre: sqrt row's output squares back to its input",
          sq_surd(2, 3, 1) == (7, 48, 1))
    for label, img, s_in, s_out, rho_hand in E2_ROWS:
        rho = rho_algebraic(*s_in, *s_out)
        digs = surd_digits(*s_in, DEPTH + 1)
        es = emission_series(img, digs, DEPTH)
        resid = [es[n - 1] - float(rho) * n for n in range(1, DEPTH + 1)]
        flat, lo, hi = two_half_flat(resid, 2.0)
        term = DEPTH - es[-1]
        sign_ok = True
        if rho != 1:
            sign_ok = (term > 0) == (rho < 1)
        print(f"    {label:20s} rho {str(rho):5s} "
              f"resid sup {lo:5.2f} -> {hi:5.2f}  delay(240) {term:5d}")
        check(f"E2 {label}: algebraic rho == hand rho", rho == rho_hand)
        check(f"E2 {label}: |e(n) - rho n| flat", flat)
        if rho != 1:
            check(f"E2 {label}: delay sign matches mismatch sign", sign_ok)


# ------------------------------------------------------------------ #
# E3: the commitment deficit                                           #
# ------------------------------------------------------------------ #

E3_BOUNDED = [
    ("2x @ phi", img_mobius((2, 0, 0, 1)), (1, 5, 2)),
    ("2x @ sqrt2", img_mobius((2, 0, 0, 1)), (0, 2, 1)),
    ("x^2 @ phi", img_square, (1, 5, 2)),
    ("7x @ phi", img_mobius((7, 0, 0, 1)), (1, 5, 2)),
]


def e3():
    print("\nE3 THE COMMITMENT DEFICIT (depth {})".format(DEPTH))
    dmax = {}
    for label, img, s_in in E3_BOUNDED:
        digs = surd_digits(*s_in, DEPTH + 1)
        ds = deficit_series(img, digs, DEPTH)
        flat, lo, hi = two_half_flat(ds, 0.75)
        dmax[label] = max(ds)
        print(f"    {label:12s} D_max {max(ds):6.3f}  "
              f"sup halves {lo:6.3f} -> {hi:6.3f}  D_min {min(ds):9.2e}")
        check(f"E3 {label}: D(n) >= 0", min(ds) > -1e-9)
        check(f"E3 {label}: D(n) flat (scale-synced)", flat)
    check("E3 ordering: D_max(7x @ phi) > D_max(2x @ phi)",
          dmax["7x @ phi"] > dmax["2x @ phi"])

    digs = surd_digits(0, 2, 1, DEPTH + 1)
    ds = deficit_full(img_square, digs, DEPTH)
    n0 = DEPTH // 2
    xs = list(range(n0 + 1, DEPTH + 1))
    ys = ds[n0:]
    mx = sum(xs) / len(xs)
    my = sum(ys) / len(ys)
    slope = (sum((x - mx) * (y - my) for x, y in zip(xs, ys))
             / sum((x - mx) ** 2 for x in xs))
    target = 2 * log(1 + 2 ** 0.5)
    print(f"    WALL x^2 @ sqrt2: D(240) = {ds[-1]:7.2f}, "
          f"second-half slope {slope:.4f} vs 2 ln(1+sqrt2) = {target:.4f}")
    check("E3 wall: deficit slope = 2 ln(1+sqrt2) within 5%",
          abs(slope - target) <= 0.05 * target)


# ------------------------------------------------------------------ #

if __name__ == "__main__":
    e0()
    e1()
    e2()
    e3()
    print()
    if FAILS:
        print("FAILURES:")
        for f in FAILS:
            print("  " + f)
        raise SystemExit(1)
    print("ALL ENGINES PASS")
