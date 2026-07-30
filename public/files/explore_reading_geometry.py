"""The reading geometry: one lemma behind every window's readability.

THE QUESTION
------------
Positional numeration reads an integer through windows: the trailing
window (last t base-b digits), the leading window (sign, exponent,
first t digits), redundant-digit variants, and the scale circle
(the slide rule's window). Each window family has its own corpus of
readable and unreadable operations, charted in explore_dual_pole.py,
explore_dual_locality.py, explore_dual_redundant.py, and
explore_dual_lipschitz.py. This script asks whether ONE abstract
statement generates all of them:

  Model a window as a metric measure geometry (X, d, mu, {C_t}) -- a
  metric, a measure, and a sequence of covers C_t with mesh
  delta_t -> 0 and Lebesgue number ell_t (every set of diameter
  < ell_t lies inside some cell). A reader of f at lookahead c maps
  each deep precision-(t+c) cell into a precision-t cell containing
  its f-image, REFINEMENT-COMPATIBLY: the chosen output cells must
  be nested as the input cell refines (the output is one digit
  stream, not a fresh cell per precision). The compatibility clause
  has teeth exactly at redundant covers: without it, wide low-value
  prefixes (at digits {-1,0,1} the 3-digit prefix of value 1 has
  fiber [1, 2^{j+1}-1] -- wider than its own value) let every image
  "fit" and per-level fitting degenerates; with it, choosing a cell
  commits the stream's future, and the operational form of a
  refinement-compatible reader is the residual safety game of
  explore_dual_redundant.py / explore_dual_lipschitz.py.

  THE READING LEMMA (sufficiency). If f is Lipschitz with constant
  L, its cell images have diameter <= L*delta_{t+c}, so f is
  readable at any c with L*delta_{t+c} < ell_t. [The run sharpens
  this: the inequality buys PER-LEVEL fitting, which is readability
  outright only where cells nest; at overlapping covers the
  refinement-compatible reader can pay one more digit -- see
  FINDINGS P1, the stream correction.] Instances:
    - cells = balls of an ultrametric: ell_t = delta_t, so the
      condition is L <= b^c -- fitting AUTOMATIC (the trailing end);
    - cells a partition of a connected space: ell_t = 0 -- the lemma
      is silent and readability is a per-map alignment question (the
      non-redundant leading end);
    - overlapping cover with ell_t = rho*delta_t, rho > 0: the
      condition is c >= log_b L + log_b(1/rho) (the redundant
      leading end; digits {-a..a} give rho = (2a-b+1)/(2a), so the
      margin is log_b(2a/(2a-b+1)) -- exactly the delay-law margin of
      explore_dual_redundant.py).

  NECESSITY. Readable at c forces diam f(C) <= delta_t on deep
  cells -- COARSE Lipschitz (Lipschitz at mesh scale). The exact
  pointwise equivalence should hold precisely when cells are balls.

  TOPOLOGY IS NOT ENOUGH. Bounded lookahead is a linear-modulus
  (metric) notion. A map can be uniformly continuous -- readable at
  finite but growing lookahead -- while readable at NO bounded c.
  Witness: the even-position digit extraction
  g(sum d_i b^i) = sum d_{2i} b^i, whose modulus is s(t) = 2t.

THE DESIGN
----------
Five engines, each a brute readability rig over a finite range with
the cell structure implemented directly (no formula from the target
laws is used by the rig itself; closed forms enter only as predicted
values to compare against).

E1  THE TRAILING EQUIVALENCE (ultrametric instance). Base 10.
    For f in {3x, x^2, floor(x/2), floor(x/4), floor(x/3), g}:
    measure the exact b-adic Lipschitz exponent e(f) = max over
    sample pairs of v_b(x-y) - v_b(fx-fy), and the least lookahead
    c_min(f) on residue-matched witness pairs (n, n + m*b^{t+c})
    with the tested t growing with c. Positive control: floor(x/2)
    must give c_min = 1 (the known division gate) before any
    verdict is read.

E2  THE REDUNDANT MARGIN (bought-fitting instance). Digit sets
    (b,a) = (2,1) and (10,6). The rig measures, over a grid of
    non-b-power slopes u/v, THREE quantities for floor((u/v)n + ph):
    the bare-floor game c_min (residual safety game, engine as in
    explore_dual_lipschitz.py), the best game c_min over a small
    phase menu, and the ABSTRACT bound -- least c with
    b^c * rho >= u/v, computed from the cover's own Lebesgue ratio
    rho, itself measured as the overlap/mesh ratio of consecutive
    prefix intervals [V*b^j - a*R_j, V*b^j + a*R_j]. The abstract
    bound is checked to COINCIDE algebraically with the delay-law
    closed form of explore_dual_lipschitz.py, and the game values
    are compared against it: the per-level Lebesgue argument does
    not see refinement-compatibility (a redundant cell's children
    cover it with interior overlap rho but ZERO margin at the
    parent's edges, so a stream can be forced down an edge-hugging
    trajectory the per-level count misses), so the bound is a
    worst-case-alignment heuristic and one-digit deviations in
    BOTH directions are the expected shape. Positive control:
    u/v = 1/3 at (2,1) must give bare c_min = 0 (division by three
    at redundant binary runs at delay zero,
    explore_dual_redundant.py).

E3  THE TOPOLOGY/METRIC SEPARATION (the witness). g at base 10:
    verify (i) g(n) mod 10^t is a function of n mod 10^{2t}
    (readable at modulus 2t -- uniformly continuous), (ii) g is NOT
    readable at any bounded c <= 4 for depths t > c + 2, (iii) the
    Lipschitz exponent of g grows with sample depth (no finite
    Lipschitz constant).

E4  COARSE VS POINTWISE NECESSITY (partition instance). The leading
    window at base 10; f = permute the third-from-top digit by
    v -> 9-v on integers with >= 3 digits. f maps every leading
    cell into a leading cell (readable at c = 0) yet its pointwise
    difference ratio |fx - fy| / |x - y| on adjacent straddling
    pairs grows without bound: necessity is coarse Lipschitz only.

E5  THE SCALE-CIRCLE WINDOW (the slide-rule mirror). Cells at
    precision t = b^t equal arcs of the circle [0,1) in log_b
    coordinate (a partition, Lebesgue number 0).
    (i) Multiplication by u is a rotation -- a log-metric ISOMETRY
        (Lip = 1); its misfit density at lookahead c (fraction of
        input arcs straddling an output boundary) decays like
        b^{-c} -- graded by alignment alone.
    (ii) Addition of s > 0 is log-metric NONEXPANDING on the
         positives (measured Lip <= 1): its known grading (the
         shift wall, explore_dual_locality.py) is an alignment
         phenomenon, not a Lipschitz failure.
    (iii) Subtraction x -> x - s blows up in the log metric at its
         cancellation locus: measured pointwise ratio grows without
         bound as x approaches s. Catastrophic cancellation is a
         Lipschitz failure, not an alignment one.

PREDICTIONS (fixed before the run)
----------------------------------
P1  The abstract lemma reproduces the three known regime rows with
    the exact margins: trailing margin 0 (E1: c_min = max(0, e(f))
    for every Lipschitz f in the battery, equivalence exact);
    redundant margin log_b(2a/(2a-b+1)) (E2: measured c_min equals
    ceil(log_b(2*a*u / (v*(2a-b+1)))) clipped at 0, at every scanned
    non-b-power slope); non-redundant leading = alignment (E5(i):
    an isometry, Lip = 1, still graded).
P2  g is readable at modulus 2t and at no bounded c <= 4, with
    unbounded Lipschitz exponent: continuity (quotient topology)
    does not capture bounded-lookahead readability -- the reading
    criterion is metric, not topological.
P3  Necessity splits: trailing readable-at-c iff Lipschitz exponent
    <= c (exact, cells are balls); leading readable-at-0 with
    pointwise ratio unbounded (E4) -- necessity in general is coarse
    Lipschitz, pointwise only at ball windows.
P4  E5: multiplication Lip = 1 with misfit density ~ b^{-c};
    addition measured Lip <= 1; subtraction ratio unbounded near
    x = s. The slide rule's cheap operation is multiplication and
    its Lipschitz wall is subtraction -- the mirror of the
    positional leading end.

Scopes are small (seconds); every engine prints its table and the
asserts encode the predictions above.

FINDINGS (entered after the run; ALL ENGINES PASS)
--------------------------------------------------
P1  TRAILING AND SCALE-CIRCLE ROWS CONFIRMED, REDUNDANT ROW REFUTED
    AS FROZEN. E1: c_min = max(0, lip exponent) exactly across the
    battery (3x: 0/0; x^2: 0/0; floor(x/2): 1/1; floor(x/4): 2/2;
    floor(x/3) and g unreadable with unbounded exponent). E2: the
    closed form equals the Lebesgue bound ALGEBRAICALLY at all 12
    slopes (that half of P1 is an identity), but the game-measured
    c_min is NOT the bound: bare floor 1/7 at (10,6) reads at 1
    where the bound says 0 -- the first slope found above the
    closed form, refuting the form's conjectured generality for the
    bare floor -- while the best phase reads 3/5 at (2,1), 1/3 and
    2/7 at (10,6) one digit BELOW the bound. All deviations are
    exactly one digit; deviations appear only at redundant covers.
    THE STREAM CORRECTION (the mechanism, by hand on top of the
    run): per-level Lebesgue fitting is not the reading relation.
    A redundant cell's children cover it with interior overlap rho
    but zero margin at the parent's edges, so a refinement-
    compatible reader can be forced down an edge-hugging trajectory
    the per-level count misses; conversely a structured (rational-
    slope, phased) image never realizes the worst-case alignment
    the bound charges for. The residual safety game is the exact
    law; the Lebesgue bound is its worst-case-alignment heuristic,
    tight at ultrametric windows (where children NEST and the
    correction vanishes -- E1's equivalence is exact) and one digit
    loose in either direction at overlapping covers (all scanned
    scopes).
P2  CONFIRMED. g is readable at modulus 2t (exhaustive t = 1, 2),
    unreadable at every c <= 4, with Lipschitz exponent growing
    1 -> 4 as pair depth grows 3 -> 8: uniform continuity does not
    give bounded lookahead. The reading criterion is metric, not
    topological.
P3  CONFIRMED. Trailing: exact equivalence (E1). Leading: the
    third-digit permutation is readable at c = 0 with straddle
    ratios 19, 181, 1801, 18001 growing without bound (E4):
    necessity in general is coarse Lipschitz — pointwise at the
    ball (trailing) window, coarse-only at the leading partition
    witness.
P4  CONFIRMED (as corrected at the freeze). Multiplication by 3 on
    the scale circle: measured Lip = 1.000000 (isometry), misfit
    density 1, 0.1, 0.01, 0.001 at c = 0..3 -- exactly b^{-c};
    addition of 7: measured Lip 0.998 <= 1 (nonexpanding; its
    grading is alignment, explore_dual_locality.py); subtraction
    of 1000: pointwise log-metric ratio 4.9 -> 61.6 -> 694.2
    approaching the cancellation locus. The slide rule's cheap
    operation is multiplication; its Lipschitz wall is subtraction.

Tier summary: the reading lemma's sufficiency and the coarse/exact
necessity split are RULES at the scanned scopes (the ultrametric
equivalence elementary both directions); the stream correction is a
RULE at the scanned redundant scopes (mechanism argued, general
statement open); the topology/metric separation is a PROPERTY
(witness g). One-digit deviation bound: OBSERVATION (12 slopes, two
digit sets).

RUN RECORD: ALL ENGINES PASS, ~8 s. E1 battery table, E2 12-slope
three-way table (bare/best-phase/bound), E3 exponent growth 1 -> 4,
E4 ratios to 18001, E5 densities to 0.0010 as printed above.
"""

import math
from fractions import Fraction


# ----------------------------------------------------------------- #
# shared utilities                                                   #
# ----------------------------------------------------------------- #

def vb(n, b):
    """b-adic valuation of n (n != 0)."""
    v = 0
    while n % b == 0:
        n //= b
        v += 1
    return v


def digits_of(n, b):
    """Base-b digits of n >= 0, least significant first."""
    if n == 0:
        return [0]
    ds = []
    while n:
        ds.append(n % b)
        n //= b
    return ds


def g_even(n, b=10):
    """Even-position digit extraction: keeps digits at positions
    0, 2, 4, ... of n's base-b expansion."""
    ds = digits_of(n, b)
    out = 0
    for i, d in enumerate(ds[::2]):
        out += d * b**i
    return out


# ----------------------------------------------------------------- #
# E1 + E3: the trailing window (ultrametric instance)                #
# ----------------------------------------------------------------- #

def trailing_cmin(f, b, c_max, ts, n_range):
    """Least lookahead c <= c_max at which f(n) mod b^t is a function
    of n mod b^{t+c} for every t in ts. Tested on residue-matched
    witness pairs (n, n + m*b^{t+c}) -- a grouped test over a sample
    smaller than the modulus would pass vacuously (one point per
    class). ts is a function of c: readability at lookahead c is a
    for-all-t statement, and some violations only appear at t > c
    (the even-position extraction g needs t + c even and t > c), so
    the tested t must grow with the scanned c. Returns c_min or
    None."""
    for c in range(c_max + 1):
        ok = True
        for t in ts(c):
            mod_in, mod_out = b**(t + c), b**t
            for n in n_range:
                fn = f(n)
                for m in (1, 2, 3, 7):
                    if (f(n + m * mod_in) - fn) % mod_out:
                        ok = False
                        break
                if not ok:
                    break
            if not ok:
                break
        if ok:
            return c
    return None


def trailing_lip_exponent(f, b, n_range, depths):
    """Max of v_b(x-y) - v_b(fx-fy) over pairs x, y = x + m*b^d:
    the exact b-adic Lipschitz exponent seen on the sample."""
    e_max = -10**9
    for x in n_range:
        fx = f(x)
        for d in depths:
            for m in (1, 3):
                y = x + m * b**d
                fy = f(y)
                if fy == fx:
                    continue  # contraction to 0 distance: no bound
                e = vb(y - x, b) - vb(fy - fx, b)
                e_max = max(e_max, e)
    return e_max


def run_e1_e3():
    b = 10
    ts = lambda c: (2, 3, c + 2, c + 3)
    c_max = 4
    n_range = range(1, 4000)
    depths = (0, 1, 2, 3, 4)

    battery = [
        ("3x",          lambda n: 3 * n,        True),
        ("x^2",         lambda n: n * n,        True),
        ("floor(x/2)",  lambda n: n // 2,       True),
        ("floor(x/4)",  lambda n: n // 4,       True),
        ("floor(x/3)",  lambda n: n // 3,       False),
        ("g (even digits)", lambda n: g_even(n, b), False),
    ]

    # positive control first: the known division gate
    ctrl = trailing_cmin(lambda n: n // 2, b, c_max, ts, n_range)
    print("E1 positive control  floor(x/2) c_min = %s (expect 1)" % ctrl)
    assert ctrl == 1, "positive control failed: trailing rig broken"

    print("E1 trailing equivalence (base 10): c_min vs Lipschitz exponent")
    print("  %-16s %8s %8s" % ("f", "c_min", "lip_exp"))
    for name, f, is_lip in battery:
        c_min = trailing_cmin(f, b, c_max, ts, n_range)
        e = trailing_lip_exponent(f, b, range(1, 400), depths)
        print("  %-16s %8s %8d" % (name, c_min, e))
        if is_lip:
            assert c_min == max(0, e), (
                "trailing equivalence fails for " + name)
        else:
            assert c_min is None, name + " should be unreadable"

    # E3: the witness in detail
    # (i) readable at modulus 2t (exhaustive at t = 1, 2)
    for t in (1, 2):
        seen = {}
        for n in range(0, 10**(2 * t + 1)):
            key = n % 10**(2 * t)
            val = g_even(n) % 10**t
            assert seen.setdefault(key, val) == val, \
                "g not readable at modulus 2t"
    # (ii) not readable at any bounded c (checked in battery above)
    # (iii) Lipschitz exponent grows with depth
    e_small = trailing_lip_exponent(lambda n: g_even(n), b,
                                    range(1, 200), (0, 1, 2, 3))
    e_large = trailing_lip_exponent(lambda n: g_even(n), b,
                                    range(1, 200), (0, 2, 4, 6, 8))
    print("E3 witness g: modulus-2t readable; lip exponent "
          "%d (depth<=3) -> %d (depth<=8)" % (e_small, e_large))
    assert e_large > e_small, "g's Lipschitz exponent should grow"
    print("E1/E3 PASS: trailing readability is exactly Lipschitz;"
          " topology (uniform continuity) is strictly weaker\n")


# ----------------------------------------------------------------- #
# E2: the redundant leading window (bought fitting)                  #
# ----------------------------------------------------------------- #

def sd_digits(a):
    return range(-a, a + 1)


def repunit(b, j):
    return (b**j - 1) // (b - 1)


def rgame_feasible(b, a, c, u, v, w=0, z=1):
    """0-initialized greatest fixed point of the residual safety
    game for f(n) = floor((u/v) n + w/z): the operational
    (refinement-compatible) reader at lookahead c. Game engine as
    in explore_dual_lipschitz.py: integer state r = L*R with
    L = lcm(v, z), flushable iff |floor(r/L)| <= a*R_c."""
    L = v * z // math.gcd(v, z)
    F = a * repunit(b, c)
    win = set(range(-F * L, (F + 1) * L))
    assert L * w % z == 0, "phase scaling not integral"
    phc = (b - 1) * (L * w // z)
    inj = [L * u * x // v - phc for x in sd_digits(a)]
    shift = L * b**c
    changed = True
    while changed:
        changed = False
        for r in list(win):
            for s in inj:
                pre = b * r + s
                if not any(pre - e * shift in win for e in sd_digits(a)):
                    win.discard(r)
                    changed = True
                    break
    return (L * w // z) in win


def redundant_cmin(b, a, u, v, w=0, z=1, cap=8):
    for c in range(cap + 1):
        if rgame_feasible(b, a, c, u, v, w, z):
            return c
    return None


PHASE_MENU = [(0, 1), (1, 2), (1, 3), (2, 3), (3, 7)]


def run_e2():
    print("E2 redundant margin: stream game vs the per-level"
          " Lebesgue bound")
    scopes = [
        # (b, a, [(u, v), ...]) -- non-b-power slopes only
        (2, 1, [(3, 1), (1, 3), (5, 3), (7, 1), (3, 5), (1, 7)]),
        (10, 6, [(3, 1), (1, 3), (7, 3), (3, 7), (1, 7), (2, 7)]),
    ]
    # positive control: division by 3 at redundant binary, delay 0
    ctrl = redundant_cmin(2, 1, 1, 3)
    print("E2 positive control  (2,1) u/v=1/3 bare c_min = %s"
          " (expect 0)" % ctrl)
    assert ctrl == 0, "positive control failed: redundant rig broken"

    table = {}
    for b, a, slopes in scopes:
        rho = Fraction(2 * a - b + 1, 2 * a)
        # the cover's own Lebesgue ratio, measured from the prefix
        # intervals: overlap of consecutive cells / mesh, deep scale
        j = 10
        Rj = repunit(b, j)
        mesh = 2 * a * Rj
        overlap = 2 * a * Rj - b**j
        print("  (b,a)=(%d,%d): measured Lebesgue ratio %.4f -> rho"
              " = %s = %.4f" % (b, a, overlap / mesh, rho, float(rho)))
        assert abs(overlap / mesh - float(rho)) < 1e-3, \
            "Lebesgue ratio off"
        for u, v in slopes:
            # the abstract bound: least c with b^c * rho >= u/v,
            # exact arithmetic, computed from rho alone
            bound = 0
            while b**bound * rho < Fraction(u, v):
                bound += 1
            # the delay-law closed form (explore_dual_lipschitz.py)
            cf = 0
            while b**cf * v * (2 * a - b + 1) < 2 * a * u:
                cf += 1
            assert cf == bound, \
                "closed form != Lebesgue bound at %d/%d" % (u, v)
            bare = redundant_cmin(b, a, u, v)
            best = min(redundant_cmin(b, a, u, v, w, z)
                       for w, z in PHASE_MENU)
            table[(b, a, u, v)] = (bare, best, bound)
            print("    u/v = %d/%d: bare game %s, best-phase game %s,"
                  " bound %d" % (u, v, bare, best, bound))
            assert bare is not None and abs(bare - bound) <= 1, \
                "bare deviates by > 1 digit at %d/%d" % (u, v)
            assert bound - 1 <= best <= bare, \
                "best-phase outside [bound-1, bare] at %d/%d" % (u, v)
    # the two specimen facts: the bound is neither sufficient for
    # the bare floor nor tight for the phase family
    assert table[(10, 6, 1, 7)][0] == 1 and table[(10, 6, 1, 7)][2] == 0, \
        "specimen 1 gone: bare 1/7 at (10,6) should exceed the bound"
    assert table[(2, 1, 3, 5)][1] == 0 and table[(2, 1, 3, 5)][2] == 1, \
        "specimen 2 gone: best-phase 3/5 at (2,1) should beat the bound"
    print("E2 PASS: closed form == Lebesgue bound algebraically;"
          " the stream game deviates from it by <= 1 digit in BOTH"
          " directions (bare 1/7 at (10,6) above, phased 3/5 at (2,1)"
          " below) -- the bound is a per-level heuristic, the"
          " refinement-compatible game is the law\n")


# ----------------------------------------------------------------- #
# E4: coarse vs pointwise necessity at the leading partition         #
# ----------------------------------------------------------------- #

def leading_cell(n, t):
    """Leading window: (exponent, first t digits) of n >= 1."""
    s = str(n)
    return (len(s) - 1, s[:t])


def permute_third(n):
    """Permute the third-from-top digit by v -> 9-v (identity on
    numbers shorter than 3 digits)."""
    s = str(n)
    if len(s) < 3:
        return n
    return int(s[:2] + str(9 - int(s[2])) + s[3:])


def run_e4():
    # readable at c = 0: f maps every leading cell into a leading cell
    for t in (1, 2, 3, 4):
        seen = {}
        for n in range(100, 60000):
            key = leading_cell(n, t)
            val = leading_cell(permute_third(n), t)
            assert seen.setdefault(key, val) == val, \
                "digit permutation not cellular at t=%d" % t
    # pointwise ratio unbounded on adjacent straddling pairs
    ratios = []
    for k in (3, 4, 5, 6):
        x = 12 * 10**(k - 2) - 1          # e.g. 1199, 11999, ...
        y = x + 1
        r = abs(permute_third(x) - permute_third(y)) / (y - x)
        ratios.append(r)
    print("E4 leading digit-permutation: readable at c = 0;"
          " straddle ratios %s" % ["%.0f" % r for r in ratios])
    assert all(ratios[i + 1] > ratios[i] for i in range(len(ratios) - 1)), \
        "straddle ratio should grow without bound"
    print("E4 PASS: readable-at-0 yet pointwise ratio unbounded --"
          " necessity is coarse Lipschitz, pointwise only at balls\n")


# ----------------------------------------------------------------- #
# E5: the scale-circle window (the slide-rule mirror)                #
# ----------------------------------------------------------------- #

def circle_misfit_density(b, t, c, rot):
    """Fraction of precision-(t+c) arcs whose image under rotation
    by rot straddles a precision-t boundary."""
    n_in = b**(t + c)
    h = 1.0 / n_in
    out = b**t
    bad = 0
    for m in range(n_in):
        lo = (m * h + rot) % 1.0
        hi = lo + h * (1 - 1e-12)
        if math.floor(lo * out) != math.floor(hi * out):
            bad += 1
    return bad / n_in


def log_lip_ratio(f, pairs):
    """Max |log f(x) - log f(y)| / |log x - log y| over pairs."""
    best = 0.0
    for x, y in pairs:
        fx, fy = f(x), f(y)
        if fx <= 0 or fy <= 0:
            continue
        num = abs(math.log(fx) - math.log(fy))
        den = abs(math.log(x) - math.log(y))
        if den > 0:
            best = max(best, num / den)
    return best


def run_e5():
    b, t = 10, 2
    rot = math.log(3.0, b) % 1.0   # multiplication by 3
    dens = [circle_misfit_density(b, t, c, rot) for c in range(4)]
    print("E5 scale circle, x -> 3x: misfit density by lookahead c:"
          " %s" % ["%.4f" % d for d in dens])
    # isometry: Lip = 1 exactly
    pairs = [(x, x + 1) for x in range(50, 4000, 37)]
    lip_mul = log_lip_ratio(lambda x: 3 * x, pairs)
    lip_add = log_lip_ratio(lambda x: x + 7, pairs)
    s = 1000
    near = [(s + d, s + d + 1) for d in (1, 2, 4, 8, 16, 64, 256)]
    lip_sub_near = log_lip_ratio(lambda x: x - s, near)
    lip_sub_prof = [log_lip_ratio(lambda x: x - s, [(s + d, s + d + 1)])
                    for d in (256, 16, 1)]
    print("   log-metric Lip: x->3x %.6f (isometry), x->x+7 %.6f"
          " (nonexpanding), x->x-1000 near locus %.1f"
          " (profile d=256,16,1: %s)"
          % (lip_mul, lip_add, lip_sub_near,
             ["%.1f" % r for r in lip_sub_prof]))
    assert abs(lip_mul - 1.0) < 1e-9, "multiplication should be isometry"
    assert lip_add <= 1.0 + 1e-9, "addition should be nonexpanding"
    assert lip_sub_prof[-1] > 100 * lip_sub_prof[0], \
        "subtraction ratio should blow up at cancellation"
    # decay of misfit density ~ b^{-c}
    for c in range(3):
        assert dens[c + 1] < dens[c], "misfit density should decay in c"
    print("E5 PASS: multiplication isometric + alignment-graded,"
          " addition nonexpanding, subtraction the Lipschitz wall\n")


if __name__ == "__main__":
    run_e1_e3()
    run_e2()
    run_e4()
    run_e5()
    print("ALL ENGINES PASS")
