"""The exact lookahead law for scaling by a rational slope, derived —
the winning set in closed form, and the delay as a criterion rather
than a bracket around the Lebesgue bound.

THE QUESTION. Addition's delay law was a rule by exhaustion until
explore_lookahead_proof.py derived it for every radix and every
contiguous digit set, turning its 354-cell census into the check. Its
sibling in the same corpus is still a rule at three scanned windows:
floor((u/v) n + w/z) is window-local at bounded lookahead for EVERY
rational slope, at a delay within one digit of the Lebesgue bound
max(0, ceil(log_b(2 a u / (v (2a - b + 1))))), the exact delay being
the residual safety game's value — scanned at (2,1), (4,2), (10,6)
by explore_dual_lipschitz.py S5 and nowhere derived. Does
addition's machinery travel to it?

THE TRANSPLANT, named as one. Addition's proof
runs on the injected set S = D + D with the emission scaled by b^c.
Scaling by u/v changes BOTH halves of that pair, and the second
change is the one that carries the delay:

    addition:  R' = b R + s - e b^c,        s in D + D
    scaling:   m' = b m + (Lu/v) x - e L b^c,   x in D, m = L R

with L = lcm(v, z) the state scale of the recorded rig. So the
injected set is u D -- an arithmetic progression of step u, NOT
contiguous, which is exactly where addition's residue-count step is
at risk -- and the emission lattice coarsens from b^c to L b^c. The
transplant's own reading: addition IS the slope game at u/v = 2/1,
its contiguous S = D + D being the closure of the doubling map's
injected set 2D, which shares D + D's endpoints.

THE DERIVATION, hand-attacked on paper before this engine was
written. Conventions re-derived from explore_dual_lipschitz.py's
rgame_feasible rather than from memory: symmetric digits
D = {-a..a} with 2a + 1 > b, slack rho = 2a + 1 - b >= 1, state
m = L R integral, phase offset phi = L w / z, and the flush window
floor(m/L) in [-a r_c, a r_c] with r_c the c-digit repunit -- an
interval ASYMMETRIC to the right by L - 1, since a residual in
[0, 1) is what the floor itself absorbs. Write

    E(c)    = floor( a L (v b^c - u) / (v (b - 1)) )
    Wtop(c) = (a r_c + 1) L - 1,     Wbot(c) = -a r_c L.

(1) THE ENDPOINT BOUND. If the winning set is nonempty with maximum
H, the opponent injects x = a: every successor is at least
b H + (L/v) u a - a L b^c, and one must stay <= H, forcing
H (b - 1) <= a L (v b^c - u) / v, i.e. H <= E. Mirrored at the
minimum with x = -a: L_min >= -E. Addition's (1) is this at
u = 2, v = 1, where E = floor(a (b^c - 2) / (b - 1)) is its own H1
verbatim -- the (b-1) division is the shared object, and E is
SHAPE-AWARE where the Lebesgue count is not.

(2) THE WINDOW. The winning set lies inside the flush window, so
H <= Wtop - phi and L_min >= Wbot - phi in phase-shifted
coordinates. E minus the window's HALF-WIDTH a r_c L is exactly
a L (v - u) / (v (b - 1)), so E is at least the half-width iff
u <= v -- and since the half-width is an integer the floor never
disturbs it. But the window is NOT symmetric: its top carries a
further L - 1, the overhang the floor's own truncation buys. So
the two bounds bind SIDE BY SIDE and often on opposite sides --
the endpoint bound on the right while the window binds on the
left -- which is the asymmetry step (3)'s phase re-centres, and
the reason no single "which bound wins" reading is available.
Both bounds together:

    Htop = min(E, Wtop - phi),   Lbot = max(-E, Wbot - phi).

(3) THE PHASE IS A WINDOW SHIFT, NOTHING ELSE. Substituting
m = m' + phi in the phased recurrence cancels the phase term
exactly -- b(m' + phi) - (b-1) phi = b m' + phi -- so the phased
game IS the unphased game with the flush window translated by -phi
and the query still at 0. The usable length is then
len(phi) = min(E, Wtop - phi) + min(E, phi - Wbot) + 1. This is NOT
monotone in phi -- it falls once E exceeds both terms -- so the
lemma is the COMPARISON AGAINST phi = 0, not a monotonicity: for
every phi in [0, L), len(phi) >= len(0). Case on E against
Wtop and against a r_c L + phi; each of the four gives a
difference of phi, Wtop - E, E - a r_c L or L - 1 - phi, all
non-negative, and the two remaining combinations are empty
because phi <= L - 1 while Wtop = a r_c L + L - 1. So a phase can
only LOWER the delay, and it lowers it exactly when the endpoint
bound binds on the right while the window binds on the left.

(4) SUFFICIENCY -- THE INVARIANT INTERVAL. For [Lbot, Htop] to trap
the game, each (m, x) needs an emission e in D with
Lbot <= b m + (L/v) u x - e L b^c <= Htop. The emission intervals
[e L b^c + Lbot, e L b^c + Htop] are spaced L b^c apart, so they
cover every achievable value once Htop - Lbot + 1 >= L b^c; and the
needed e stays inside D precisely by (1)'s two inequalities, which
Htop <= E and Lbot >= -E grant by construction. Hence

    Htop - Lbot + 1 >= L b^c   ==>   the game is feasible at c.

(5) NECESSITY -- THE t-STEP INJECTION. Over t steps from the maximum
H the opponent plays x_1..x_t and the state becomes
b^t H + (L/v) u X - L b^c E, where X and E both range over the
CONTIGUOUS run sum(b^(t-i) x_i) of length 2a(b^t - 1)/(b - 1) + 1 --
contiguous because D is, which is where the non-contiguity of the
one-step injected set u D is repaired. Choose t with that run at
least L b^c long. When gcd(u, b) = 1, u is invertible modulo L b^c,
so u X covers EVERY residue class mod L b^c; each class must find a
representative in [Lbot, Htop], forcing Htop - Lbot + 1 >= L b^c.
The E it needs is in range: the bound of (1) makes the required
|b^t H + (L/v) u X| / (L b^c) at most a b^t / (b - 1) exactly.

(6) THE CRITERION AND THE IDENTITY. With (4) and (5), for
gcd(u, b) = 1 the game is feasible at lookahead c IFF
Htop - Lbot + 1 >= L b^c; and where it is feasible, (1) and (2)
bound the fixed point inside [Lbot, Htop] while (4) makes that
interval invariant, so THE WINNING SET IS EXACTLY [Lbot, Htop].
c_min is the least c meeting the inequality.

(7) WHERE gcd(u, b) > 1. Step (5) weakens: u X covers only the
multiples of g_c = gcd(u, b^c) mod L b^c, so necessity loosens to
Htop - Lbot >= L b^c - g_c while (4) is untouched. The extreme case
is exact by hand: at u = b^s, v = 1, c = s the endpoint bound gives
E = 0, so the winning set is {0}, which IS invariant (emit e = x),
while at c = s - 1 the bound is negative and the set is empty --
pure b-power slopes read at max(0, s) exactly, with the b-power
case sitting in precisely the gap step (5) leaves open.

(8) THE LEBESGUE BOUND IS THE CRITERION WITH THE FLOORS DROPPED.
The scanned bound's condition v b^c (2a - b + 1) >= 2 a u is
2a(v b^c - u) >= (b - 1) v b^c; the criterion at v = z = 1 with the
endpoint bound binding is 2 E + 1 >= b^c, i.e.
2 floor(a(b^c - u)/(b - 1)) >= b^c - 1. The two differ only by the
floor and the b - 1 against v b^c, which is at most one digit --
the scanned "within one digit" is the rounding gap, and both named
exceptions are on the side the floors predict.

THE DESIGN, frozen before the engine.

P-A The controls come back through this code path: the integer
    delays (2,1) x3 = 3, x4 = 2 and (10,6) x2 = 1, x10 = 1; the
    eight hand-played spots of explore_dual_lipschitz.py S5; and
    (10,6) slope 1/7 at c_min = 1, the cell that killed the closed
    form's conjectured generality.
P-B THE INTERVAL IDENTITY: at every grid cell feasible at c, the
    measured greatest fixed point equals [Lbot + phi, Htop + phi]
    exactly -- not merely contains it.
P-C THE CRITERION: measured feasibility equals
    Htop - Lbot + 1 >= L b^c at every grid cell with gcd(u, b) = 1,
    at every scanned lookahead, phase 0 and phased.
P-D PURE b-POWERS read at max(0, s) exactly, and the criterion
    returns that value at every b-power slope in the grid.
P-E THE gcd CELLS: at gcd(u, b) > 1 the criterion is reported
    separately -- sufficiency must hold at every such cell, and
    whether necessity survives there is the finding either way.
P-F PHASES NEVER RAISE THE DELAY, and the window-shaped phase 1/2
    lowers it exactly where the endpoint bound binds right while
    the window binds left ((2,1) 3/5 and (10,6) 1/3, both 1 -> 0).
P-G THE SIDE CHECK: E at u = 2, v = 1, z = 1, c = 1 equals
    a - ceil(a/(b-1)), addition's H1, at every radix and reach in
    the sweep -- the shape-aware margin is one object across the
    two operations. Reported beside the Lebesgue bound's own
    prediction, cell for cell.

KILLS, frozen as what this rig PRINTS.

K1 A control misses -> the game convention was re-derived wrong and
   nothing downstream is read.
K2 A feasible cell prints a fixed point differing from
   [Lbot + phi, Htop + phi] -> the identity is wrong; the closed
   form does not hold and the law stays a rule at scanned scopes.
K3 A cell with gcd(u, b) = 1 where measured feasibility and the
   criterion disagree -> the criterion is wrong. Which side it
   fails on says which of (4) and (5) broke.
K4 A pure b-power slope reading off max(0, s) -> the exactness
   corollary is wrong.
K5 A phase raising c_min above its phase-0 value -> the shift
   lemma of (3) is wrong.
K6 A cell where the criterion's c_min and the Lebesgue bound differ
   by 2 or more -> (8) is wrong and the "within one digit" scanned
   statement was never the rounding gap.

POSITIVE CONTROL, run and read before any verdict line: P-A whole.

FINDINGS (entered post-run; every number below sits in this file's
printed output).

F1 THE CONTROL HOLDS. The integer delays and all nine hand spots
   reproduce through this code path, (10,6) slope 1/7 at c_min = 1
   included. K1 never fired.

F2 THE FROZEN SCOPE WAS WRONG, AND THE OBJECT THAT REPAIRS IT WAS
   ALREADY INSIDE THE DERIVATION. P-B and P-C as frozen sorted the
   grid by gcd(u, b), and the first run refuted them: the fixed
   point at (2,1) slope 1/3 under phase 1/7 is {3, 10, 17}, at
   (2,1) slope 8/3 is {-4,-2,0,2,4}, at (2,1) slope 2 is {0} --
   SPARSE SETS, not intervals. All three are one phenomenon, the
   injection step L u / v and the emission step L b^c sharing a
   factor. Step (5) names that factor but computes it as
   gcd(u, b^c), missing the phase's L: the invariant that separates
   the two regimes is g_c = gcd(L u / v, L b^c). It SEPARATES rather
   than characterises -- g_c = 1 is where the criterion is exact,
   while plenty of g_c > 1 cells agree with it anyway (168 of 183).
   The frozen cells are re-sorted by it below -- a re-sort of the
   frozen grid, not a new selection.

F3 THE CRITERION IS EXACT WHERE ITS OWN NECESSITY STEP IS
   AVAILABLE. At g_c = 1 the criterion and the game agree at
   505/505 UNPHASED cells across every scanned lookahead -- and
   separately at the 48 phased g_c = 1 cells of F5, which are not
   in that count -- and the measured fixed point equals
   [Lbot, Htop] at
   303/303 feasible cells -- the closed form, not a bracket. A
   SECOND grid sharing no window with the first, eleven more
   windows at radices up to 9 and slopes to 9/9, agrees at
   1469/1469 further g_c = 1 cells. Sufficiency holds in every
   region of both grids with no counterexample, as (4) proves it
   must. At g_c > 1 the criterion withholds where
   the game grants (15 of 183 cells) and the fixed point goes
   sparse (1 of 164), both necessity-side: exactly the gap (7)
   predicted, now located by the sharper invariant.

F4 A SHIPPED CLAUSE IS FALSE, AND THE CRITERION CORRECTS IT. "Pure
   b-power slopes b^s read at max(0, s) exactly" fails at (4,2)
   slope 1/4, which reads at 1. The corrected law: s >= 0 reads s
   exactly (the hand argument of (7)), and s < 0 reads 0 iff
   a >= b - 1 and 1 otherwise, with the DEPTH t = |s| never
   entering -- 33/33 cells across 11 windows and t = 1, 2, 3,
   including (10,6) slope 1/10 at 1, predicted before it ran. The
   condition is the criterion's own at c = 0, where the span test
   E >= v - 1 unpacks to a >= b - 1, i.e. slack rho >= b - 1 --
   strictly stronger than redundancy. DIVIDING BY THE RADIX IS A
   FREE SHIFT ONLY WHEN THE DIGIT SET IS AT LEAST {-(b-1)..(b-1)};
   below that it costs one digit, at every depth alike.

F5 THE PHASE IS A WINDOW SHIFT AND NOTHING ELSE. At 336 phased
   cells no phase raises the delay, and both the criterion and the
   interval identity stay exact under phase at every g_c = 1 cell.
   The round phase saves a digit at (2,1) slope 3/5 and (10,6)
   slope 1/3, both 1 -> 0 -- which (3) places exactly where the
   endpoint bound binds on the right while the flush window binds
   on the left, the window's own right overhang being what the
   phase re-centres. K5 never fired.

F6 THE SIDE CHECK PAYS: ONE MARGIN, TWO OPERATIONS. E at u = 2,
   v = 1, c = 1 equals a - ceil(a/(b-1)) -- addition's H1 verbatim
   -- at 760/760 cells over radices 3..40, E read off interval()
   rather than recomputed, so the control cannot pass by
   reimplementing what it checks. So the
   shape-aware margin is ONE object across addition and scaling,
   and the Lebesgue count is that same object with the floors
   dropped. Against the game's own delay the Lebesgue form agrees
   at 137/169 cells and is one digit off at 32, never two (K6
   never fired), and the misses run BOTH ways -- 18 above, 14
   below. The wedge is a rounding gap in a size-only heuristic,
   not a loss belonging to either operation.

VERDICT, by piece, since they do not share a tier.
  - The endpoint bound (1), the window bound (2), the phase shift
    lemma (3), and the SUFFICIENCY of the span criterion (4) are
    PROVED for every radix b >= 2, every symmetric redundant digit
    set, every rational slope and every phase, with no computation
    at specific values load-bearing.
  - The winning set equals [Lbot, Htop] wherever the criterion
    grants: PROVED -- (4) gives the containment one way and (1)
    with (2) the other.
  - NECESSITY, hence the criterion as an IFF and c_min as the
    least granting c: a RULE, verified at 1974/1974 g_c = 1 cells
    across TWO GRIDS SHARING NO WINDOW -- 505 over the four scanned
    windows at 43 slopes and four lookaheads, and 1469 over eleven
    further windows including radices 7, 8 and 9 the corpus had
    never scanned, at slopes to 9/9 -- plus 48 phased cells. The
    second grid exists because the first could not tell a law from
    an artifact of its own four windows. The t-step argument of (5)
    closes it whenever
    the emission it needs is in range, and THAT RANGE CHECK DOES
    NOT CLOSE IN GENERAL: the required emission can exceed the
    attainable run by a/(b-1). That is the one open step, and
    closing it would promote the whole criterion.
  - The negative-power law of F4 is the criterion at c = 0
    unpacked, so it is a RULE at the same scope and inherits the
    same open step.
  - The shipped max(0, s) clause is REFUTED and swaps in place.

WHERE THE MACHINERY STOPPED TRAVELING. Addition's residue-count
step survives the transplant only as the t-step argument of (5),
and only at g_c = 1: addition has S = D + D contiguous and its own
emission lattice coprime to nothing in particular, so the question
never arose there. Scaling injects u D, an arithmetic progression,
and the shared factor between that progression's step and the
emission lattice is the whole of what does not travel.

RUN RECORD: pure Python, integers only, standard library; largest
winning set ~10,700 residues at (10,6) slope 7/8 lookahead 3, far
under the analysis memory ceiling; 8.4s wall clock against a ~60s
estimate. Prints reproduced by:
python prime/code/explore_slope_proof.py
"""

import sys
from math import gcd

FAILURES = []


def ok(cond, msg):
    if not cond:
        FAILURES.append(msg)
        print(f"  FAIL: {msg}")


def repunit(b, j):
    return sum(b ** i for i in range(j))


def digits(a):
    return list(range(-a, a + 1))


def ceil_div(x, y):
    return -(-x // y)


# --------------------------------------------------------------- game
# Verbatim the engine explore_dual_lipschitz.py S5 measured the
# scanned scopes with, so the controls of P-A mean something.

def rgame(b, a, c, u, v, w=0, z=1):
    """Greatest fixed point of the residual safety game, and whether
    the initial state is in it."""
    L = v * z // gcd(v, z)
    F = a * repunit(b, c)
    win = set(range(-F * L, (F + 1) * L))
    phc = (b - 1) * (L * w // z)
    inj = [L * u * x // v - phc for x in digits(a)]
    shift = L * b ** c
    changed = True
    while changed:
        changed = False
        for r in list(win):
            for s in inj:
                pre = b * r + s
                if not any(pre - e * shift in win for e in digits(a)):
                    win.discard(r)
                    changed = True
                    break
    return (L * w // z) in win, win


def cmin_measured(b, a, u, v, w=0, z=1, cap=4):
    for c in range(cap + 1):
        if rgame(b, a, c, u, v, w, z)[0]:
            return c
    return None


# ----------------------------------------------------- the derivation

def interval(b, a, c, u, v, w=0, z=1):
    """The derived winning set [Lbot + phi, Htop + phi] in the game's
    own state units, plus the span the criterion tests."""
    L = v * z // gcd(v, z)
    phi = L * w // z
    E = (a * L * (v * b ** c - u)) // (v * (b - 1))
    if v * b ** c < u:
        E = -1                      # bound negative: no state survives
    wtop = (a * repunit(b, c) + 1) * L - 1
    wbot = -a * repunit(b, c) * L
    htop = min(E, wtop - phi)
    lbot = max(-E, wbot - phi)
    return lbot + phi, htop + phi, htop - lbot + 1, L * b ** c


def lattice_gcd(b, c, u, v, w=0, z=1):
    """g_c = gcd(injection step, emission step) in the game's own
    state units. The derivation's step (5) needs g_c = 1."""
    L = v * z // gcd(v, z)
    return gcd(L * u // v, L * b ** c)


def criterion(b, a, c, u, v, w=0, z=1):
    lo, hi, span, need = interval(b, a, c, u, v, w, z)
    return lo <= hi and span >= need


def cmin_derived(b, a, u, v, w=0, z=1, cap=4):
    for c in range(cap + 1):
        if criterion(b, a, c, u, v, w, z):
            return c
    return None


def cmin_lebesgue(b, a, u, v):
    """The scanned closed form: pure b-power slopes at max(0, s),
    else the per-level Lebesgue bound."""
    s, uu, vv = 0, u, v
    while uu % b == 0:
        uu //= b
        s += 1
    while vv % b == 0:
        vv //= b
        s -= 1
    if uu == 1 and vv == 1:
        return max(0, s)
    marg = 2 * a - b + 1
    if marg <= 0:
        return None
    c = 0
    while b ** c * v * marg < 2 * a * u:
        c += 1
    return max(0, c)


def bpower_exponent(b, u, v):
    """s if u/v == b^s exactly, else None."""
    s, uu, vv = 0, u, v
    while uu % b == 0:
        uu //= b
        s += 1
    while vv % b == 0:
        vv //= b
        s -= 1
    return s if (uu == 1 and vv == 1) else None


# ---------------------------------------------------------- the grids

WINDOWS = [(2, 1), (3, 2), (4, 2), (10, 6)]

SLOPES = [(u, v) for u in range(1, 9) for v in range(1, 9)
          if gcd(u, v) == 1]

PHASES = [(1, 2), (1, 3), (2, 3), (1, 4), (3, 4), (1, 5), (2, 5),
          (3, 5), (4, 5), (1, 7), (5, 7), (6, 7), (1, 8), (7, 8)]


def cells(cap_c):
    for (b, a) in WINDOWS:
        for (u, v) in SLOPES:
            yield (b, a, u, v, cap_c)


# ----------------------------------------------------------- the runs

def s0_control():
    print("== POSITIVE CONTROL (P-A) ==")
    for (b, a, m, want) in [(2, 1, 3, 3), (2, 1, 4, 2),
                            (10, 6, 2, 1), (10, 6, 10, 1)]:
        got = cmin_measured(b, a, m, 1)
        ok(got == want, f"K1: integer x{m} at ({b},{a}) = {got} != {want}")
    print("  integer delays reproduce: (2,1) x3=3 x4=2; (10,6) x2=1 x10=1")
    spots = [(2, 1, 1, 3, 0), (2, 1, 3, 5, 1), (2, 1, 5, 3, 2),
             (10, 6, 1, 3, 1), (10, 6, 7, 3, 1), (10, 6, 3, 5, 1),
             (10, 6, 21, 5, 2), (2, 1, 1, 2, 0), (10, 6, 1, 7, 1)]
    bad = [(b, a, u, v) for (b, a, u, v, want) in spots
           if cmin_measured(b, a, u, v) != want]
    print(f"  hand spots: {len(spots) - len(bad)}/{len(spots)} reproduce "
          f"(including (10,6) 1/7 at 1)")
    ok(not bad, f"K1: hand spot missed at {bad[:4]}")


def s1_identity_and_criterion(cap_c=3):
    print("\n== THE INTERVAL IDENTITY AND THE CRITERION (P-B, P-C, P-E) ==")
    stats = {1: [0, 0], 2: [0, 0]}
    ident = {1: [0, 0], 2: [0, 0]}
    critbad, suffbad, idbad = [], [], []
    for (b, a, u, v, _) in cells(cap_c):
        for c in range(cap_c + 1):
            key = 1 if lattice_gcd(b, c, u, v) == 1 else 2
            feas, win = rgame(b, a, c, u, v)
            pred = criterion(b, a, c, u, v)
            stats[key][0] += 1
            if feas == pred:
                stats[key][1] += 1
            elif key == 1:
                critbad.append((b, a, u, v, c, feas, pred))
            if pred and not feas:
                suffbad.append((b, a, u, v, c))
            if feas:
                lo, hi, _, _ = interval(b, a, c, u, v)
                ident[key][0] += 1
                if win == set(range(lo, hi + 1)):
                    ident[key][1] += 1
                elif key == 1:
                    idbad.append((b, a, u, v, c,
                                  (min(win), max(win)), (lo, hi)))
    for key, tag in ((1, "g_c = 1"), (2, "g_c > 1")):
        n, good = stats[key]
        ni, gi = ident[key]
        print(f"  {tag}: criterion vs game {good}/{n} agree; "
              f"fixed point equals [Lbot, Htop] at {gi}/{ni} feasible")
    print(f"  sufficiency (criterion grants => game feasible), both "
          f"regions: {'holds' if not suffbad else f'FAILS {suffbad[:4]}'}")
    if stats[2][0] != stats[2][1]:
        print(f"  -> every g_c > 1 disagreement is necessity-side: the "
              f"game is feasible where the criterion withholds")
    ok(not idbad, f"K2: identity fails at g_c = 1: {idbad[:3]}")
    ok(not critbad, f"K3: criterion disagrees at g_c = 1: {critbad[:3]}")
    ok(not suffbad, f"K3: sufficiency fails at {suffbad[:3]}")
    return stats


def s2_bpowers(cap_c=3):
    print("\n== PURE b-POWER SLOPES (P-D) ==")
    shipped, pos, neg, gap, n = [], [], [], [], 0
    for (b, a, u, v, _) in cells(cap_c):
        s = bpower_exponent(b, u, v)
        if s is None or max(0, s) > cap_c:
            continue
        n += 1
        got = cmin_measured(b, a, u, v, cap=cap_c)
        if got != max(0, s):
            shipped.append((b, a, u, v, s, got))
        if s >= 0:
            if got != s:
                pos.append((b, a, u, v, s, got))
            if cmin_derived(b, a, u, v, cap=cap_c) != s:
                gap.append((b, a, u, v, s))
        elif got != (0 if a >= b - 1 else 1):
            neg.append((b, a, u, v, s, got))
    print(f"  the shipped max(0, s) form holds at {n - len(shipped)}/{n} "
          f"b-power cells; it FAILS at {shipped}")
    print(f"  s >= 0 reads s exactly: {len(pos) == 0} "
          f"(the criterion misses {len(gap)} of these, all g_c > 1: "
          f"{all(lattice_gcd(b, s, u, v) > 1 for (b, a, u, v, s) in gap)})")
    print(f"  s < 0 reads 0 iff a >= b-1, else 1: {len(neg) == 0} "
          f"in the grid")

    # the corrected negative-power law, swept off-grid and at depth:
    # the delay does not depend on t, only on a against b - 1.
    off, m = [], 0
    for (b, a) in [(2, 1), (3, 2), (4, 2), (4, 3), (5, 3), (5, 4),
                   (6, 3), (6, 5), (10, 5), (10, 6), (10, 9)]:
        if 2 * a + 1 <= b:
            continue
        for t in (1, 2, 3):
            m += 1
            got = cmin_measured(b, a, 1, b ** t, cap=2)
            if got != (0 if a >= b - 1 else 1):
                off.append((b, a, t, got))
    print(f"  swept at t = 1,2,3 over 11 windows: {m - len(off)}/{m} "
          f"cells read the corrected law, t never entering")
    ok(not pos, f"K4: s >= 0 b-power off s at {pos[:4]}")
    ok(not neg, f"K4: s < 0 b-power off the a >= b-1 law at {neg[:4]}")
    ok(not off, f"K4: negative-power sweep off the law at {off[:4]}")


def s3_phases(cap_c=3):
    print("\n== THE PHASE AS A WINDOW SHIFT (P-F) ==")
    raised, idbad, critbad, n, ngc = [], [], [], 0, [0]
    for (b, a) in WINDOWS:
        for (u, v) in [(1, 3), (3, 5), (5, 3), (7, 3), (1, 2), (2, 5)]:
            bare = cmin_measured(b, a, u, v, cap=cap_c)
            for (w, z) in PHASES:
                cp = cmin_measured(b, a, u, v, w, z, cap=cap_c)
                cd = cmin_derived(b, a, u, v, w, z, cap=cap_c)
                n += 1
                if bare is not None and (cp is None or cp > bare):
                    raised.append((b, a, u, v, w, z, bare, cp))
                if cp is not None and lattice_gcd(b, cp, u, v, w, z) == 1:
                    ngc[0] += 1
                    if cp != cd:
                        critbad.append((b, a, u, v, w, z, cp, cd))
                    feas, win = rgame(b, a, cp, u, v, w, z)
                    lo, hi, _, _ = interval(b, a, cp, u, v, w, z)
                    if win != set(range(lo, hi + 1)):
                        idbad.append((b, a, u, v, w, z))
    print(f"  {n} phased cells: no phase raises the delay = "
          f"{not raised}")
    print(f"  criterion under phase at the {ngc[0]} g_c = 1 phased "
          f"cells: {'exact' if not critbad else f'FAILS {critbad[:3]}'}")
    print(f"  phased interval identity: "
          f"{'exact' if not idbad else f'FAILS {idbad[:3]}'}")
    for (b, a, u, v) in [(2, 1, 3, 5), (10, 6, 1, 3)]:
        bare = cmin_measured(b, a, u, v, cap=cap_c)
        half = cmin_measured(b, a, u, v, 1, 2, cap=cap_c)
        print(f"  ({b},{a}) slope {u}/{v}: bare {bare} -> "
              f"round phase {half}")
        ok(half == bare - 1, f"K5: window phase does not save a digit "
                             f"at ({b},{a}) {u}/{v}")
    ok(not raised, f"K5: a phase raises c_min at {raised[:3]}")
    ok(not critbad, f"K3: phased criterion off at {critbad[:3]}")
    ok(not idbad, f"K2: phased identity off at {idbad[:3]}")


def s3b_disjoint_grid():
    """The criterion against the game on a grid sharing no window
    with the one above: if 505/505 were an artifact of the four
    scanned windows, this is where it shows."""
    print("\n== THE CRITERION ON A DISJOINT GRID ==")
    other = [(5, 3), (5, 4), (6, 3), (6, 5), (7, 4), (8, 5), (9, 5),
             (9, 8), (7, 6), (3, 3), (2, 2)]
    assert not (set(other) & set(WINDOWS)), "grids must not overlap"
    bad, suff, n1, n2 = [], [], 0, 0
    for (b, a) in other:
        if 2 * a + 1 <= b:
            continue
        for u in range(1, 10):
            for v in range(1, 10):
                if gcd(u, v) != 1:
                    continue
                for c in range(3):
                    feas, _ = rgame(b, a, c, u, v)
                    pred = criterion(b, a, c, u, v)
                    if lattice_gcd(b, c, u, v) == 1:
                        n1 += 1
                        if feas != pred:
                            bad.append((b, a, u, v, c, feas, pred))
                    else:
                        n2 += 1
                    if pred and not feas:
                        suff.append((b, a, u, v, c))
    print(f"  11 further windows (radices 7, 8, 9 never scanned "
          f"above), slopes to 9/9: {n1 - len(bad)}/{n1} g_c = 1 cells "
          f"agree, {n2} g_c > 1 cells beside them")
    print(f"  sufficiency violations across the whole disjoint grid: "
          f"{len(suff)}")
    ok(not bad, f"K3: criterion fails off the first grid at {bad[:3]}")
    ok(not suff, f"K3: sufficiency fails off the first grid {suff[:3]}")


def s4_side_check(cap_c=3):
    print("\n== THE SIDE CHECK: ADDITION'S MARGIN IS THIS ONE (P-G) ==")
    # E is read off interval() itself, never recomputed here: a
    # control that reimplements the object it checks can pass for
    # the wrong reason.
    bad, n = [], 0
    for b in range(3, 41):
        for a in range((b + 1) // 2, 31):
            if 2 * a + 1 <= b:
                continue
            n += 1
            lo, hi, _, _ = interval(b, a, 1, 2, 1)
            if hi != a - ceil_div(a, b - 1):
                bad.append((b, a, hi, a - ceil_div(a, b - 1)))
    print(f"  E(u=2,v=1,c=1) = a - ceil(a/(b-1)) (addition's H1) at "
          f"{n - len(bad)}/{n} cells, E read off interval() itself")
    ok(not bad, f"K2: the margins are not one object at {bad[:4]}")

    print("  the GAME's delay against the Lebesgue closed form, cell "
          "for cell:")
    agree, off1, off2, tot = 0, [], [], 0
    for (b, a, u, v, _) in cells(cap_c):
        got = cmin_measured(b, a, u, v, cap=cap_c)
        leb = cmin_lebesgue(b, a, u, v)
        if got is None or leb is None or leb > cap_c:
            continue
        tot += 1
        if got == leb:
            agree += 1
        elif abs(got - leb) == 1:
            off1.append((b, a, u, v, got, leb))
        else:
            off2.append((b, a, u, v, got, leb))
    print(f"    {agree}/{tot} cells agree; {len(off1)} differ by one "
          f"digit; {len(off2)} differ by two or more")
    if off1:
        hi = [x for x in off1 if x[4] > x[5]]
        lo = [x for x in off1 if x[4] < x[5]]
        print(f"    of the one-digit cells, {len(hi)} read ABOVE the "
              f"Lebesgue bound and {len(lo)} below")
        print(f"    sample above: {hi[:4]}")
    ok(not off2, f"K6: two-digit gap from the Lebesgue bound at "
                 f"{off2[:4]}")


def main():
    cap_c = 3
    s0_control()
    if FAILURES:
        print("\nCONTROL FAILED -- nothing downstream is read.")
        return 1
    s1_identity_and_criterion(cap_c)
    s2_bpowers(cap_c)
    s3_phases(cap_c)
    s3b_disjoint_grid()
    s4_side_check(cap_c)
    print()
    if FAILURES:
        print(f"{len(FAILURES)} FAILURES")
    else:
        print("ALL CHECKS PASS")
    return 1 if FAILURES else 0


if __name__ == "__main__":
    sys.exit(main())
