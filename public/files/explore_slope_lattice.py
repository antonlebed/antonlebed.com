"""The winning set where the two steps share a factor — the length
test replaced by a per-class saturation test, and the sparse fixed
points read off it.

THE QUESTION. The rational-slope delay criterion is proved entire in
explore_slope_proof.py: with L = lcm(v, z) the state scale, q = L u / v
the injection step, N = L b^c the emission step and
g_c = gcd(q, N), the span test Htop - Lbot + 1 >= N SUFFICES
everywhere and is an IFF at g_c = 1, while at g_c > 1 it can withhold
inside a band of width g_c - 1. Inside that band the game grants and
the fixed point goes SPARSE rather than interval — three measured
specimens, and nothing said what the sparse set IS. This asks that,
and asks it as a question about the lattice the state lives on.

THE SLATE, and it is arithmetic before it is engine. The naive
expectation from step (5) of the proof is a progression of step g_c:
the winning set meets N / g_c classes mod N, pairwise congruent mod
g_c. The corpus's own specimens refuse it flatly. At (2,1) slope 1/3
under phase 1/7, c = 0, the measured fixed point is {3, 10, 17} —
step 7, and g_c = 7, so the naive reading is right. At (2,1) slope 2,
c = 1, it is the singleton {0} with g_c = 2, which discriminates
nothing since the interval is one point wide. At (2,1) slope 8/3,
c = 2, it is {-4, -2, 0, 2, 4} — step 2 where g_c = gcd(8, 12) = 4,
five points where the bound demands three. Right twice and wrong
once, and what 8/3 has that the others do not is the question.

THE DERIVATION, hand-attacked on paper and then on the three
specimens before this engine was written. Conventions re-derived from
explore_slope_proof.py's rgame rather than from memory: the state
recurrence in the engine's own coordinate is

    m' = b m + (q x - (b - 1) phi) - e N,   x in D, e in D,

with D = {-a..a}, phi = L w / z the phase, and the start state m = phi
inside the flush window. The winning set W is the greatest subset of
that window closed under the rule: for EVERY x some e in D lands the
successor back in W.

(1) THE WINNING SET IS A SET OF RESIDUES MOD N. The emission term is a
multiple of N, so what a successor needs from W is not a value but a
REPRESENTATIVE of the class b m + q x - (b-1) phi mod N. Steps (1) and
(2) of the proof put W inside I = [Lbot + phi, Htop + phi], whose
span is at most N wherever the span test withholds — so on I the
reduction mod N is INJECTIVE, and W is exactly the lift of

    C = the greatest subset of R = pi(I) < Z/N with
        b C + pi(qD - (b-1) phi) contained in C.

The span test is this at full span: span >= N makes R the whole of
Z/N, every condition is met by construction, and C = R. So the
criterion's own sufficiency step (4) is the degenerate case of a
COVERING condition, which is what the g_c > 1 band was always about.

What this reformulation DROPS is the emission's membership in D, and
that is the step the whole tier rests on, so it is spelled out rather
than waved at. E = a(N - q)/(b - 1) exactly, which is what the
(b-1) division in the endpoint bound is FOR: for any state m <= Htop
<= E and any injection x <= a, the value V = b m + q x satisfies

    V - Htop <= (b - 1) E + q a = a N,

so the emission e = (V - target)/N carrying V to a target at or below
Htop is at most a, and the mirror at Lbot >= -E gives e >= -a. The
bound is the same in both regimes, so a forced emission -- and where
span < N it IS forced, the class having one representative in I --
never leaves D. Measured, never assumed: K3 is what would print.

(2) THE INJECTED CLASSES ARE A COSET OF <q>, AND WHEN D IS BIG ENOUGH
THEY ARE ALL OF IT. x |-> q x mod N is a bijection from Z/(N/g_c)
onto the subgroup <q> = g_c Z/N, so the 2a + 1 injections cover that
whole subgroup exactly when

    n := N / g_c <= 2a + 1.

Where they do, the successor requirement collapses: m needs the ENTIRE
class of b m - (b-1) phi mod g_c to sit inside C.

(3) THE SATURATION CRITERION. Call a class t in Z/g_c SATURATED when
every one of its n residues mod N has a representative in I — a
per-class length test, since the members of I congruent to t mod g_c
are distinct mod N and there are at most n of them:

    A = { t in Z/g_c : #{ m in I : m = t mod g_c } >= n }.

Let f(t) = b t + kappa mod g_c with kappa = -(b-1) phi mod g_c — the
class map, well defined because q vanishes mod g_c. Then by induction
on the closure, m survives iff its class's whole FORWARD ORBIT is
saturated:

    W = { m in I : f^j(m mod g_c) in A for all j >= 1 },

and the game is feasible at c iff the start class of phi survives.
Z/g_c is finite so the orbit is rho-shaped and j <= g_c decides it.
At g_c = 1 there is one class, it is saturated iff span >= N, and the
whole statement is the length test — so this GENERALIZES the proved
criterion rather than competing with it.

(4) WHAT IT SAYS ABOUT THE THREE SPECIMENS. At 1/3 under phase 1/7:
N = 21, g_c = 7, n = 3, I = [0, 17], the saturated classes are
{0,1,2,3} and f(t) = 2t + 4 has 3 as its only survivor, giving
{3, 10, 17} — one class, step 7, the naive reading by coincidence.
At 8/3: N = 12, g_c = 4, n = 3, I = [-4, 4], only class 0 is
saturated, f(t) = 2t survives from t = 0 AND t = 2, giving TWO
classes mod 4 — the even integers of I, step 2. The naive lattice
misses because it reads the SUBGROUP where the law reads a UNION OF
CLASSES selected by a dynamical condition, and a union of two classes
mod 4 reads as one progression of step 2. At slope 2: g_c = 2, n = 1,
I = {0}, and the singleton survives. All three by hand, before this
file existed.

THE DESIGN, frozen before the engine.

P-A The controls come back through this code path: rgame verbatim from
    explore_slope_proof.py (the engine every shipped table was
    measured with), the four integer delays, and the three specimen
    sparse sets EXACTLY as sets, not as spans.
P-B THE QUOTIENT LAW. At every cell of both grids, phased and
    unphased, at every scanned lookahead: the measured winning set is
    contained in I, and equals the lift of the greatest invariant
    subset C of pi(I) < Z/N. Feasible or not — an empty game must
    give an empty C. The lift is checked as a SET.
P-C THE SATURATION CRITERION. At every cell with n <= 2a + 1, the
    orbit test of (3) reproduces the measured winning set as a set,
    and its feasibility verdict matches the game's.
P-D THE REDUCTION. At every g_c = 1 cell the saturation criterion and
    the proved length test agree — one class, saturated iff
    span >= N. Anything else means the generalization is not one.
P-E THE 54 CELLS. Every cell where the length test withholds while
    the game grants is a cell the saturation criterion GRANTS. That
    band is the whole of what the proved criterion left open, so this
    is the number that says whether it closes.
P-F THE SHAPE. Census of the surviving class count |C mod g_c| over
    the sparse cells: how often one class (naive lattice right), how
    often several, and whether the union is ever NOT a single
    arithmetic progression — which is the case that would refuse a
    lattice reading altogether, and the most interesting outcome.
P-G OFF THE COSET HYPOTHESIS. The cells with n > 2a + 1 are reported
    separately: (2) does not reach them, so whether the class law
    still holds there is the finding either way, and P-B covers them
    regardless since (1) needs no hypothesis.

KILLS, frozen as what this rig PRINTS.

K1 A control misses, or a specimen sparse set differs as a set ->
   the conventions were re-derived wrong and nothing below is read.
K2 A cell whose measured winning set is not contained in I -> steps
   (1) and (2) of the proof were misread and the injectivity that
   (1) rests on is not available.
K3 A cell where the measured winning set differs from the lift of C
   -> the quotient law is wrong; the emission's membership in D is
   the suspect, since the quotient formulation drops it.
K4 A cell with n <= 2a + 1 where the saturation criterion's set or
   verdict differs from the game's -> (2) or (3) is wrong.
K5 A g_c = 1 cell where the saturation criterion and the length test
   disagree -> this is not a generalization of the proved criterion.
K6 A withholding cell the saturation criterion also withholds -> the
   band does not close and the sparse region keeps a gap.

POSITIVE CONTROL, run and read before any verdict line: P-A whole.

FINDINGS (entered post-run; every number below sits in this file's
printed output).

F1 THE CONTROL HOLDS. The four integer delays reproduce through this
   code path, and all three specimen sparse sets come back EXACTLY as
   sets rather than as spans. K1 never fired.

F2 THE WINNING SET IS A RESIDUE FIXED POINT, AND THAT NEEDS NO
   HYPOTHESIS. At 2903/2903 cells over both grids plus the phased
   slice the measured winning set sits inside I, and at 2903/2903 it
   equals the lift of C exactly -- 2030 of them at g_c = 1 and 873 at
   g_c > 1. The emission's membership in D is what the quotient
   formulation drops, and it never bites: the endpoint bound that
   grants it in the proof grants it here. K2 and K3 never fired.

F3 THE SATURATION CRITERION IS THE GAME. Inside the coset hypothesis
   -- 1070 cells -- the orbit test reproduces the winning set at
   1070/1070 and the feasibility verdict at 1070/1070. At every
   g_c = 1 cell it IS the length test: one class, saturated iff
   span >= N. So it CONTAINS the proved criterion rather than
   competing with it. K4 and K5 never fired.

F4 THE COSET HYPOTHESIS IS NOT LOAD-BEARING. Forced past its own
   precondition at the 1833 cells with n > 2a + 1, the class law is
   exact at 1833/1833 -- never too small, never otherwise wrong; 586
   of those carry g_c > 1, which is the count that means anything,
   the other 1247 being cells the proved length test already settles --
   and the winning set is a union of g_c-classes at every one of
   them. So (2) is a convenience of THIS derivation route, not a
   condition on the law. The mechanism the numbers suggest, stated as
   the suspicion it is: one step of injection covers only part of the
   subgroup there, but several steps generate all of it, which is the
   same multi-step covering the proof's own necessity argument
   already runs -- so the collapse to a class condition should
   survive without the one-step hypothesis, and deriving it is what
   would raise F4's tier.

F5 THE BAND CLOSES. In this rig's scope 67 cells have the length test
   withholding while the game grants (the corpus's earlier count of
   54 is a different phase slice, not a disagreement). The saturation
   criterion grants at all 49 inside the hypothesis, and forced past
   it at the other 18: 67 of 67. The band of width g_c - 1 that the
   proved criterion left open is not a gap in the law but a gap in
   the TEST, and the per-class test closes it. K6 never fired.

F6 THE SPARSE SETS ARE UNIONS OF CLASSES, AND NOT ALWAYS LATTICES.
   21 feasible cells carry a winning set short of the full interval.
   Their surviving class counts: ONE class at 9 cells, TWO at 11,
   THREE at 1. The naive step-g_c reading is right exactly at the 9
   one-class cells and nowhere else, which is why the corpus's own
   three specimens read two ways. And at (3,2) slope 1/3 under phase
   1/8, c = 0, g_c = 8, the surviving classes are {0, 2, 3} mod 8 and
   the winning set {0,2,3,8,10,11,16,18,19} is NOT a single
   arithmetic progression. So the sparse region is not lattice-shaped
   in general: the lattice question was the wrong question, and the
   right object is the class set an affine map on Z/g_c leaves
   surviving.

VERDICT, by piece, since they do not share a tier.
  - THE QUOTIENT LAW (1) is PROVED for every radix b >= 2, every
    symmetric redundant digit set, every rational slope and every
    phase: the proved endpoint and window bounds put W inside I, the
    span is at most N wherever the test withholds so reduction mod N
    is injective on I, and the reformulation is then definitional
    with the emission staying in D by those same bounds. The 2903
    cells are the CHECK on it, not the evidence for it.
  - THE SATURATION CRITERION at n <= 2a + 1 is PROVED at that same
    scope, and it contains the proved length test as its g_c = 1
    case: feasible at lookahead c iff the forward orbit of the start
    class under t |-> b t + kappa stays saturated.
  - BEYOND n <= 2a + 1 the same criterion is a RULE, verified at 1833
    cells across two grids sharing no window and a phased slice, with
    no counterexample and no near miss. The load-bearing 586 of those
    are the g_c > 1 ones: at g_c = 1 the criterion is the length test
    and the length test is already proved, so those 1247 cells check
    the machinery without extending the claim.
  - THE SPARSE WINNING SET is exactly the states whose class survives
    that orbit -- a union of classes mod g_c, PROVED inside the
    hypothesis and a RULE outside it.
  - THE NAIVE STEP-g_c LATTICE is REFUTED and swaps in place.

WHAT IT COST TO SEE. The band read as a gap in the LAW for as long as
the test being generalized was a LENGTH test, which has one number to
give and so can only be loosened or tightened. Reading the same
sufficiency argument as a COVERING condition -- the emission lattice
already tiles the line, so what a state needs is a representative and
not a value -- turns one number into one number per class, and the
band is what the coarse test could not resolve. The step that was
never available at g_c = 1 is the step that made the general case
easy: there is only one class there, so the whole structure the law
runs on is invisible in the case that was already proved.

RUN RECORD: pure Python, integers only, standard library; 2903 cells
with the safety game replayed once per cell, which is what the single
sweep buys -- four sections reading the same game would have cost four
times it. 28.4s wall clock against a ~25s estimate, far under the
analysis memory ceiling. Prints reproduced by:
python prime/code/explore_slope_lattice.py
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


# --------------------------------------------------------------- game
# rgame and interval are VERBATIM explore_slope_proof.py, which is
# itself verbatim the engine explore_dual_lipschitz.py S5 measured the
# scanned scopes with. Copied rather than imported so this file is a
# standalone record; the controls of P-A are what check the copy.

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


def interval(b, a, c, u, v, w=0, z=1):
    """The derived winning interval [Lbot + phi, Htop + phi] and the
    span the proved criterion tests against L b^c."""
    L = v * z // gcd(v, z)
    phi = L * w // z
    E = (a * L * (v * b ** c - u)) // (v * (b - 1))
    if v * b ** c < u:
        E = -1
    wtop = (a * repunit(b, c) + 1) * L - 1
    wbot = -a * repunit(b, c) * L
    htop = min(E, wtop - phi)
    lbot = max(-E, wbot - phi)
    return lbot + phi, htop + phi, htop - lbot + 1, L * b ** c


def cmin_measured(b, a, u, v, w=0, z=1, cap=4):
    for c in range(cap + 1):
        if rgame(b, a, c, u, v, w, z)[0]:
            return c
    return None


# ------------------------------------------------------- the quotient

def params(b, a, c, u, v, w=0, z=1):
    """The five numbers the derivation runs on."""
    L = v * z // gcd(v, z)
    phi = L * w // z
    N = L * b ** c
    q = L * u // v
    return L, phi, N, q, gcd(q, N)


def quotient_set(b, a, c, u, v, w=0, z=1):
    """Step (1): the greatest invariant subset C of pi(I) < Z/N, and
    its lift back into I. No hypothesis on the digit set."""
    _, phi, N, q, _ = params(b, a, c, u, v, w, z)
    lo, hi, _, _ = interval(b, a, c, u, v, w, z)
    if lo > hi:
        return set(), set()
    offs = {(q * x - (b - 1) * phi) % N for x in digits(a)}
    C = {m % N for m in range(lo, hi + 1)}
    changed = True
    while changed:
        changed = False
        for r in list(C):
            if any((b * r + o) % N not in C for o in offs):
                C.discard(r)
                changed = True
    return C, {m for m in range(lo, hi + 1) if m % N in C}


def saturation_set(b, a, c, u, v, w=0, z=1, force=False):
    """Step (3): the classes mod g_c whose forward orbit under
    f(t) = b t + kappa stays saturated, and the states they lift to.
    Valid where n <= 2a + 1; returns None where it is not, unless
    forced -- forcing is how the rig measures whether that hypothesis
    is load-bearing rather than assuming it."""
    _, phi, N, _, g = params(b, a, c, u, v, w, z)
    n = N // g
    if n > 2 * a + 1 and not force:
        return None
    lo, hi, _, _ = interval(b, a, c, u, v, w, z)
    if lo > hi:
        return set(), set()
    counts = [0] * g
    for m in range(lo, hi + 1):
        counts[m % g] += 1
    A = {t for t in range(g) if counts[t] >= n}
    kappa = (-(b - 1) * phi) % g

    def survives(t):
        s = t
        for _ in range(g + 1):
            s = (b * s + kappa) % g
            if s not in A:
                return False
        return True

    T = {t for t in range(g) if survives(t)}
    return T, {m for m in range(lo, hi + 1) if m % g in T}


def is_single_progression(S):
    """Does the set read as one arithmetic progression?"""
    xs = sorted(S)
    if len(xs) < 3:
        return True
    d = xs[1] - xs[0]
    return all(y - x == d for x, y in zip(xs, xs[1:]))


# ---------------------------------------------------------- the grids

WINDOWS = [(2, 1), (3, 2), (4, 2), (10, 6)]

SLOPES = [(u, v) for u in range(1, 9) for v in range(1, 9)
          if gcd(u, v) == 1]

DISJOINT = [(5, 3), (5, 4), (6, 3), (6, 5), (7, 4), (8, 5), (9, 5),
            (9, 8), (7, 6), (3, 3), (2, 2)]

PHASE_SLOPES = [(1, 3), (3, 5), (5, 3), (2, 5), (8, 3)]
PHASES = [(1, 2), (2, 3), (3, 5), (1, 7), (1, 8)]

SPECIMENS = [(2, 1, 1, 3, 1, 7, 0, {3, 10, 17}),
             (2, 1, 8, 3, 0, 1, 2, {-4, -2, 0, 2, 4}),
             (2, 1, 2, 1, 0, 1, 1, {0})]


def scope(cap_c=3):
    """Every cell this rig reads, once: both grids plus the phased
    slice. Yields (b, a, u, v, w, z, c)."""
    for (b, a) in WINDOWS:
        for (u, v) in SLOPES:
            for c in range(cap_c + 1):
                yield (b, a, u, v, 0, 1, c)
    for (b, a) in DISJOINT:
        if 2 * a + 1 <= b:
            continue
        for u in range(1, 10):
            for v in range(1, 10):
                if gcd(u, v) != 1:
                    continue
                for c in range(3):
                    yield (b, a, u, v, 0, 1, c)
    for (b, a) in WINDOWS:
        for (u, v) in PHASE_SLOPES:
            for (w, z) in PHASES:
                for c in range(cap_c + 1):
                    yield (b, a, u, v, w, z, c)


# ----------------------------------------------------------- the runs

def s0_control():
    print("== POSITIVE CONTROL (P-A) ==")
    for (b, a, m, want) in [(2, 1, 3, 3), (2, 1, 4, 2),
                            (10, 6, 2, 1), (10, 6, 10, 1)]:
        got = cmin_measured(b, a, m, 1)
        ok(got == want, f"K1: integer x{m} at ({b},{a}) = {got} != {want}")
    print("  integer delays reproduce: (2,1) x3=3 x4=2; (10,6) x2=1 x10=1")
    bad = []
    for (b, a, u, v, w, z, c, want) in SPECIMENS:
        feas, win = rgame(b, a, c, u, v, w, z)
        if not feas or win != want:
            bad.append((b, a, u, v, w, z, c, sorted(win)))
    print(f"  the three specimen sparse sets reproduce as SETS: "
          f"{len(SPECIMENS) - len(bad)}/{len(SPECIMENS)}")
    ok(not bad, f"K1: specimen set differs at {bad[:3]}")


def sweep(cap_c=3):
    """ONE pass over every cell, every check. The game is the
    expensive object and it is played once per cell."""
    st = {"n": {1: 0, 2: 0}, "lift": {1: 0, 2: 0}, "outside": [],
          "qbad": [], "inreach": 0, "outreach": 0, "setbad": [],
          "verdbad": [], "redbad": [], "offbad": [], "band": [],
          "bandreach": 0, "missed": [], "sparse": 0, "hist": {},
          "nonap": [], "band_forced": 0, "forced_ok": 0, "forced_under": 0,
          "forced_other": 0}
    for (b, a, u, v, w, z, c) in scope(cap_c):
        _, phi, _, _, g = params(b, a, c, u, v, w, z)
        key = 1 if g == 1 else 2
        feas, win = rgame(b, a, c, u, v, w, z)
        lo, hi, span, need = interval(b, a, c, u, v, w, z)

        # P-B, K2/K3
        st["n"][key] += 1
        if win and (min(win) < lo or max(win) > hi):
            st["outside"].append((b, a, u, v, w, z, c,
                                  (min(win), max(win)), (lo, hi)))
        _, lift = quotient_set(b, a, c, u, v, w, z)
        if win == lift:
            st["lift"][key] += 1
        else:
            st["qbad"].append((b, a, u, v, w, z, c))

        # P-C, P-D, P-G, K4/K5
        res = saturation_set(b, a, c, u, v, w, z)
        if res is None:
            st["outreach"] += 1
            # a UNION OF CLASSES mod g_c: every member of I sharing a
            # class with the winning set is itself in it. (Testing
            # "one class" instead would be a different claim, and a
            # vacuous one wherever the set is the full interval.)
            cls = {m % g for m in lift}
            if any(m % g in cls and m not in lift
                   for m in range(lo, hi + 1)):
                st["offbad"].append((b, a, u, v, w, z, c))
            # is the hypothesis load-bearing? force the class law
            # past its own precondition and read which way it fails.
            _, forced = saturation_set(b, a, c, u, v, w, z, force=True)
            if forced == win:
                st["forced_ok"] += 1
            elif forced < win:
                st["forced_under"] += 1
            else:
                st["forced_other"] += 1
        else:
            st["inreach"] += 1
            T, pred = res
            if pred != win:
                st["setbad"].append((b, a, u, v, w, z, c))
            if (phi in pred) != feas:
                st["verdbad"].append((b, a, u, v, w, z, c))
            if g == 1 and bool(T) != (span >= need and span > 0):
                st["redbad"].append((b, a, u, v, w, z, c, span, need))

        if not feas:
            continue

        # P-E, K6
        if span < need:
            st["band"].append((b, a, u, v, w, z, c, span, need, g))
            if res is not None:
                st["bandreach"] += 1
                if phi not in res[1]:
                    st["missed"].append((b, a, u, v, w, z, c))
            else:
                _, forced = saturation_set(b, a, c, u, v, w, z,
                                           force=True)
                if phi in forced:
                    st["band_forced"] += 1
                else:
                    st["missed"].append((b, a, u, v, w, z, c))

        # P-F
        if len(win) != span:
            st["sparse"] += 1
            k = len({m % g for m in win})
            st["hist"][k] = st["hist"].get(k, 0) + 1
            if not is_single_progression(win):
                st["nonap"].append((b, a, u, v, w, z, c,
                                    sorted(win)[:9], g))
    return st


def report(st):
    tot = st["n"][1] + st["n"][2]
    print("\n== THE QUOTIENT LAW (P-B) ==")
    print(f"  {tot} cells over both grids plus phases; winning set "
          f"inside [Lbot+phi, Htop+phi]: {tot - len(st['outside'])}/{tot}")
    for k, tag in ((1, "g_c = 1"), (2, "g_c > 1")):
        print(f"  {tag}: winning set equals the lift of C at "
              f"{st['lift'][k]}/{st['n'][k]} cells")
    ok(not st["outside"], f"K2: winning set escapes the interval at "
                          f"{st['outside'][:3]}")
    ok(not st["qbad"], f"K3: quotient law fails at {st['qbad'][:4]}")

    print("\n== THE SATURATION CRITERION (P-C, P-D, P-G) ==")
    ir = st["inreach"]
    print(f"  cells inside the coset hypothesis n <= 2a+1: {ir}; "
          f"outside it: {st['outreach']}")
    print(f"  winning set reproduced by the orbit test: "
          f"{ir - len(st['setbad'])}/{ir}")
    print(f"  feasibility verdict reproduced: "
          f"{ir - len(st['verdbad'])}/{ir}")
    red = "yes" if not st["redbad"] else "NO " + str(st["redbad"][:3])
    print(f"  at g_c = 1 the criterion IS the length test: {red}")
    off = ("yes" if not st["offbad"]
           else f"no, at {len(st['offbad'])} of them")
    print(f"  outside the hypothesis, the winning set still a union of "
          f"g_c-classes: {off}")
    print(f"  the class law FORCED past its own precondition, on those "
          f"{st['outreach']} cells: exact at {st['forced_ok']}, too "
          f"SMALL at {st['forced_under']}, otherwise wrong at "
          f"{st['forced_other']}")
    ok(not st["setbad"], f"K4: saturation set differs at {st['setbad'][:4]}")
    ok(not st["verdbad"], f"K4: saturation verdict differs at "
                          f"{st['verdbad'][:4]}")
    ok(not st["redbad"], f"K5: no reduction to the length test at "
                         f"{st['redbad'][:3]}")

    print("\n== THE BAND THE PROVED CRITERION LEFT OPEN (P-E) ==")
    print(f"  cells where the length test withholds and the game "
          f"grants: {len(st['band'])}")
    print(f"  of those, inside the coset hypothesis: {st['bandreach']}; "
          f"the saturation criterion grants at "
          f"{st['bandreach'] - len(st['missed'])}; forced past the "
          f"precondition it grants at the other {st['band_forced']}")
    if st["band"]:
        print(f"    sample (b,a,u,v,w,z,c,span,need,g_c): {st['band'][:3]}")
    ok(not st["missed"], f"K6: the band does not close at "
                         f"{st['missed'][:4]}")

    print("\n== THE SHAPE OF THE SPARSE SETS (P-F) ==")
    print(f"  feasible cells whose winning set is NOT the full "
          f"interval: {st['sparse']}")
    print(f"  surviving classes mod g_c, count -> cells: "
          f"{dict(sorted(st['hist'].items()))}")
    print(f"  winning sets that are NOT a single arithmetic "
          f"progression: {len(st['nonap'])}")
    for row in st["nonap"][:3]:
        print(f"    {row}")
    for (b, a, u, v, w, z, c, want) in SPECIMENS:
        _, _, _, _, g = params(b, a, c, u, v, w, z)
        res = saturation_set(b, a, c, u, v, w, z)
        T = sorted(res[0]) if res else None
        print(f"    ({b},{a}) {u}/{v} phase {w}/{z} c={c}: g_c = {g}, "
              f"surviving classes {T} -> {sorted(want)}")


def main():
    s0_control()
    if FAILURES:
        print("\nCONTROL FAILED — nothing below is read.")
        return 1
    report(sweep())
    print(f"\n{'ALL CHECKS PASS' if not FAILURES else 'FAILURES:'}")
    for f in FAILURES:
        print(f"  {f}")
    return 1 if FAILURES else 0


if __name__ == "__main__":
    sys.exit(main())
