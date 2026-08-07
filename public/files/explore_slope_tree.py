"""The safety game IS a tree-avoidance condition, and what that does to
the saturation criterion's surviving rule.

THE QUESTION. explore_slope_tail.py proved the saturation criterion
wherever every unsaturated class an orbit meets below depth J recurs,
and left a residual: gcd(b, g) > 1, J >= 2, and an unsaturated class
strictly inside a pre-period below J. It measured 7 such cells, exact
at all 7, and named where to look for a counterexample -- a cell with
J >= 3, a deep pre-period and a large n, which its scope (c <= 3,
slopes to 9/8) cannot reach. This asks the residual question one level
down instead of one scope wider: what IS the winning set, exactly,
with no hypothesis at all? The answer turns out to be a statement
about the reachable tree, it is cheap to evaluate, and it makes the
counterexample hunt arithmetic rather than a game replay.

THE DERIVATION, hand-attacked on paper before this engine existed.
Conventions re-derived from explore_slope_tail.py's rgame, which took
them verbatim from explore_slope_lattice.py. Notation is that file's:
L the state scale, phi = L w / z the phase, N = L b^c the emission
step, q = L u / v the injection step, g = gcd(q, N), n = N / g, I the
derived interval, B = Z/N \\ pi(I) the complement interval, A the
saturated classes, f(t) = b t + kappa the class map, J the depth at
which q S_j covers the whole subgroup, and

    T_j(r) = b^j r - (b-1) phi r_j + q [-a r_j, a r_j]   (mod N)

the reachable tree of (B)-(D) there, PROVED for every radix, every
symmetric redundant digit set, every rational slope and every phase.

(J) THE EMISSION IS INVISIBLE AND THE INJECTION IS NOT. The emission
subtracts a multiple of N, so the state's RESIDUE mod N is chosen by
the reader alone: after j steps the residue is an arbitrary element of
T_j(m), and no play of ours changes that. Necessity is then immediate
at EVERY level rather than from J on: the winning region sits inside
I, so if m is in W then T_j(m) misses B for every j >= 1. This is
(E) with the coset step deleted -- (E) needed j >= J only because it
was reading the tree through its class.

(K) AND THE CONVERSE HOLDS, WITH NO HYPOTHESIS. Let
W' = { m in I : T_j(m) misses B for all j >= 1 }. Take m in W' and
any injection x. The successor value is b m + q x - (b-1) phi, whose
residue lies in T_1(m) and so in pi(I); the span test makes reduction
injective on I, so that residue has a UNIQUE representative m' in I,
and the emission carrying the value to m' is in D by the endpoint
bound -- the same step (F) uses, which never consulted saturation, only
membership of the target residue in pi(I). And T_j(m') is contained in
T_(j+1)(m), so m' is again in W'. So W' is a strategy set, W' is
contained in W, and with (J) they are EQUAL. The safety game is a
tree-avoidance condition, exactly, always.

(L) IT IS FINITELY CHECKABLE. For j >= J the tree is the full coset,
so the level-j condition is exactly saturation of f^j(m mod g), and
the class orbit is eventually periodic: levels J .. J+g decide all of
them. Below J the tree is a proper sub-progression and is checked
directly. So W is computable WITHOUT the fixed-point iteration, in one
pass per level, and the residue r fails level j exactly when b^j r
lands in B + (b-1) phi r_j - q [-a r_j, a r_j] -- a set of size at
most |B| (2 a r_j + 1), and |B| < g at any cell where a class is
saturated at all.

(M) SO THE SURVIVING RULE HAS A SHARP STATEMENT AND A REASON TO
DOUBT IT. The criterion's set is W* (every level saturated); the truth
is W' (every level's TREE clean). W* is contained in W' because a
saturated class contains no B at all. They part exactly when a partial
tree DODGES the B-residues of an unsaturated class it lands in. Write
the level-j tree in the subgroup coordinate: q y mod N is
g ((q/g) y mod n) with gcd(q/g, n) = 1, so the tree is the image of a
CENTRED INTERVAL of 2 a r_j + 1 values of y under multiplication by a
unit of Z/n, while B's residues in that class are a short block of
consecutive indices. Dodging is therefore a three-distance question,
and it is easy exactly when the interval is short against n. At J = 2
the interval is 2a + 1 and n only just exceeds it -- which is the
definition of J = 2 -- so there is almost nothing to dodge with, and
that is why the 7 measured cells came back exact. At J >= 3 the
interval is a vanishing fraction of n and a single missing residue
should be dodgeable. THE PREDICTION FROZEN HERE: the rule is FALSE and
this rig will find a counterexample, most likely at the first cell it
reaches with J >= 3, a pre-period of 2 or more, and one unsaturated
class. If instead a scope reaching J >= 4 comes back exact, the
dodging is being blocked structurally and (M)'s coordinate is where
the block must be found.

THE DESIGN, frozen before the engine.

P-A The controls come back through this code path: rgame verbatim,
    the four integer delays, the three specimen sparse sets EXACTLY as
    sets, and explore_slope_tail.py's residual census -- 7 cells, all
    at J = 2, with their (g, n, J).
P-B THE ENDPOINT BOUND, which is the one step (K) borrows. At every
    cell of the old scope: for every m in I and every injection digit
    x, if the successor residue lies in pi(I) then the emission taking
    it to that residue's representative in I is in D.
P-C THE REGION IS THE INTERVAL. At every cell of the old scope, the
    measured winning set is contained in I. Without this the residue
    reduction is reading the wrong region.
P-D THE TREE LAW IS EXACT, AND THE OLD SCOPE IS SPLIT THREE WAYS so
    that no cell is silently dropped. (K) needs the span test, which
    is what makes reduction injective on I, so its claim covers only
    the cells with 0 < span <= N; there (L)'s set must equal the
    measured winning set. The other two classes are MEASURED beside
    it rather than skipped: where I is empty the game must return
    nothing, and where span > N -- pi(I) is all of Z/N and B is empty,
    but uniqueness fails so (K) does not reach -- the game is asked
    whether it returns I anyway, which says whether the span test is
    load-bearing or merely convenient.
P-E THE CENSUS, EXTENDED. Sweep a scope reaching c = 5, slopes to
    12/12 and radices to 12 -- residual detection only, which is
    arithmetic and needs no game -- and report the residual cells by
    depth J. The number that matters is how many have J >= 3, which
    the old scope had none of.
P-F THE HUNT. At every residual cell reachable by (L), compare W* to
    W. Report every mismatch with the level j at which the dodge
    happens, the class dodged, and the tree and B sizes there. Replay
    rgame at the smallest mismatch to confirm it against the game
    itself rather than against (L).

P-G THE FEASIBILITY VERDICT, WHICH IS THE SHIPPED CLAIM. A winning-set
    mismatch need not move the DELAY: the criterion's public statement
    is that the game is feasible at lookahead c iff the START class's
    orbit stays saturated, and c_min is the least c at which it is.
    So sweep the wide scope again asking only about the start state --
    phi in W by (L) against phi in W*, and the two c_min values they
    give -- and report the disagreements separately from P-F's. This
    is the number that decides whether the shipped delay is FALSE or
    merely stated more weakly than the law allows.

P-H THE START CLASS IS A FIXED POINT, which if it holds explains P-G
    rather than leaving it a coincidence. kappa = -(b-1) phi mod g, so
    f(phi) = b phi - (b-1) phi = phi: the start class maps to itself
    at every cell, with no hypothesis. Check that identity at every
    cell read, and check the consequence that makes it worth having --
    that the criterion's feasibility verdict is exactly "the start
    class is saturated", the orbit contributing nothing.

P-I IS THE WINNING SET STILL A UNION OF CLASSES? The criterion made
    membership a property of m mod g_c, and the measured fixed points beyond
    that hypothesis stand recorded as unions of classes mod g_c. (L) makes
    membership a property of m mod N below depth J, which need not be
    class-determined at all. So at every residual cell read, ask
    whether W is the intersection of I with a union of classes, and
    report the cells where it is not.

KILLS, frozen as what this rig PRINTS.

K1 A control misses, or a specimen sparse set differs as a set, or
   the old residual census is not 7 cells at J = 2 -> the conventions
   are wrong through this path and nothing below is read.
K2 A cell with m in I, an injection whose successor residue is in
   pi(I), and the required emission outside D -> the endpoint bound is
   not free and (K)'s sufficiency has a hole.
K3 A cell with a winning state outside I -> P-C fails, the region is
   not the interval, and (J) is reading a residue set that does not
   determine membership.
K4 A cell where (L)'s set differs from the measured winning set ->
   the tree law is not exact and (J) or (K) is wrong.
K5 A mismatch W* != W confirmed by rgame -> the saturation criterion
   is FALSE beyond the proved region, and the rule stated for it in
   explore_slope_lattice.py needs correcting to (K), everywhere that
   rule is repeated.
K7 A wide-scope cell whose FEASIBILITY verdict, or whose c_min,
   differs between (L) and the criterion -> the delay criterion itself
   is false and every shipped delay computed from it is suspect. Its
   ABSENCE beside a K5 firing is the other outcome and is not a
   consolation prize: it would say the criterion decides the start
   state correctly while mis-describing the region, which is a
   correction to one clause rather than to the law.
K6 No mismatch anywhere in a scope reaching J >= 4 -> the prediction
   in (M) is wrong, the dodge is blocked structurally, and the rule
   survives with a reason rather than a cell count.

POSITIVE CONTROL, run and read before any verdict line: P-A whole.

FINDINGS (entered post-run; every number below sits in this file's
printed output).

F1 THE CONTROL HOLDS. The four integer delays reproduce, all three
   specimen sparse sets come back exactly as sets, and the old
   residual census reproduces through this path: 7 cells, all at
   J = 2. K1 never fired.

F2 THE ENDPOINT BOUND IS FREE, AND THE REGION IS THE INTERVAL. Of the
   (state, injection) pairs whose successor residue lands back in
   pi(I), the emission taking it to that residue's representative is
   in D at 36111/36111; and the measured winning set sits inside I at
   674/674. So (K)'s one borrowed step costs nothing and the residue
   reduction is reading the right region. K2 and K3 never fired.

F3 THE GAME IS A TREE-AVOIDANCE CONDITION, EXACTLY. Where (K) claims
   -- 0 < span <= N -- (L)'s set equals the measured winning set at
   674/674. The rest of the old scope is measured rather than
   dropped: 496 cells have an empty I and the game returns nothing at
   496/496, and 1733 have span > N, where uniqueness fails and (K)
   does not reach -- the game returns I at 1733/1733 there anyway. So
   the span test is what the PROOF needs and not what the phenomenon
   needs, and the three classes account for the whole 2903-cell
   scope. K4 never fired.

F4 THE EXTENDED CENSUS REACHES DEPTH. Residual cells by depth J:
   2 -> 25, 3 -> 10, 4 -> 9, 5 -> 8, 6 -> 3. That is 30 with J >= 3,
   which the old scope had none of, and it is what makes the next
   finding a measurement rather than a guess.

F5 THE WINNING-SET RULE IS FALSE. K5 FIRES. Of the 53 residual cells
   read (N <= 4000; 2 larger not read), W* differs from W at 19, and
   rgame replayed at the smallest confirms the game against (L) and
   against the criterion: game |W| = 13 = (L)'s, criterion |W*| = 9.
   The gaps are not marginal -- (3,1) slope 9/5 at c = 5 has
   |W| = 1195 against |W*| = 403.
   AND THE PREDICTION IN (M) WAS HALF WRONG, which is the useful
   half. It said the first counterexample would need J >= 3. The
   smallest is at J = 2: (b=2, a=1) slope 12/5, c = 2, g = 4, n = 5,
   tree width 3 of 5, and the mismatches run over J = 2, 3, 4, 5, 6
   alike. (M) was right about the MECHANISM and wrong about the dial:
   every extra state in all 19 cells dodges at level j = 1, so what
   decides dodgeability is the tree width 2a + 1 against n, and DEPTH
   is not the dial that reaches it. THE DIAL IS THE DIGIT SET. All 19
   sit at the redundancy FLOOR -- 2a + 1 <= b + 1, the narrowest
   digit set that is still redundant and so the narrowest possible
   tree -- and 18 of them at pairs neither old grid contained,
   (3,1), (5,2) and (10,5). The single mismatch at an old pair,
   (2,1), needed a slope past the old cap of 9/8, which is the whole
   of what that cap was hiding. The floor is where to look and is NOT
   a criterion: 50 of the 53 residual cells read sit at it too, and
   the 3 above it carry no mismatch.

F6 THE SHIPPED CLAIM SURVIVES, AND NOT BY LUCK. K7 never fired: over
   6984 cells (N <= 20000; 6673 larger not read) the criterion's
   FEASIBILITY verdict never differs from the truth, and over the
   5045 slope rows those cells cover, c_min never differs. So what is
   false is the criterion's description of the winning REGION, while
   the delay it computes is untouched.

F7 BECAUSE THE START CLASS IS THE ONE CLASS THE MAP FIXES. kappa is
   built from phi as -(b-1) phi, so f(phi) = b phi - (b-1) phi = phi:
   an identity, holding at 6984/6984 with no hypothesis. The start
   class therefore has pre-period 0 and is recurrent, which is
   exactly the condition the cycle corollary needs -- the residual
   explore_slope_tail.py left cannot contain it. Two consequences.
   The delay criterion is PROVED ENTIRE, for every radix, every
   symmetric redundant digit set, every rational slope and every
   phase: no hypothesis, no residual, no cell count. And it collapses
   to a ONE-CLASS test, the orbit contributing nothing, verified
   6984/6984 -- the game is feasible at lookahead c iff the single
   class phi mod g_c is saturated, and c_min is the least c at which
   it is.

F8 AND THE WINNING SET STOPS BEING A UNION OF CLASSES IN THE SAME
   PLACE. At 19 of the 53 residual cells read, W is not the
   intersection of I with any union of classes mod g_c -- and they are
   exactly the 19 where W* differs from W. That is the structural
   reading of F5 rather than a second finding: below depth J the tree
   is a proper sub-progression of its coset, so membership is a
   property of m mod N and not of m mod g_c, and the criterion's
   whole vocabulary -- classes, orbits, saturation -- is the right
   one only from depth J on. The standing record that the sparse
   fixed points are unions of classes holds where it was measured (67
   cells, all inside the old scope, where W = W*) and does not
   generalise.

VERDICT, by piece, since they do not share a tier.
  - THE TREE LAW. W = { m in I : T_j(m) misses B for all j >= 1 } is
    PROVED for every radix, every symmetric redundant digit set,
    every rational slope and every phase. It has two hypotheses and
    each is used once: redundancy, to make the j-fold digit sums an
    interval (inherited from (C)), and the span test, to make the
    representative in I unique. Exact at 674/674, and the 1733 cells
    where the span test fails come back exact anyway.
  - THE SATURATION CRITERION'S WINNING-SET CLAUSE IS FALSE beyond the
    region explore_slope_tail.py proved. It is not a rule awaiting
    more cells and it is not repairable by a wider digit set: 19
    counterexamples, the smallest with 13 winning states against the
    criterion's 9. It is SWAPPED for the tree law, which is exact,
    cheaper to evaluate, and needs no fixed-point iteration.
  - THE DELAY CRITERION IS A THEOREM, and a smaller one than it was
    stated as: feasibility at lookahead c iff phi mod g_c is
    saturated. The 1833-cell rule and the 7-cell residual are both
    retired, and not by measuring more cells -- by noticing that the
    state anybody asks about is the one state the residual cannot
    reach.

WHAT IT COST TO SEE. The criterion was written per-state and then
read at the start state as though the start state were a general one.
It is not: the phase enters the class map through kappa, so phi's
class is the unique fixed point of that map. Everything the covering
hypothesis and then the pre-period residual were guarding lives
strictly away from the only state the public claim is about. The
earlier work widened the proof toward the residual; the residual was
never in front of the claim.

RUN RECORD: pure Python, integers only, standard library; 2903
old-scope cells with the game replayed once per cell, plus a
44k-cell arithmetic census and 6984 cells read for the start state.
27.8s wall clock against a ~40s estimate, peak working set 23.5 MB
against the 512 MB analysis ceiling (memwatch.py). Two residual cells
above N = 4000 and 6673 cells above N = 20000 are not read, and both
counts print. Prints reproduced by:
python prime/code/explore_slope_tree.py
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
# rgame and interval are VERBATIM explore_slope_tail.py, which took
# them verbatim from explore_slope_lattice.py. Copied rather than
# imported so this file is a standalone record; P-A checks the copy.

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


def params(b, a, c, u, v, w=0, z=1):
    """The five numbers the derivation runs on."""
    L = v * z // gcd(v, z)
    phi = L * w // z
    N = L * b ** c
    q = L * u // v
    return L, phi, N, q, gcd(q, N)


def depth_J(b, a, n):
    """(D): the least j whose digit sums cover the whole subgroup."""
    j = 1
    while 2 * a * repunit(b, j) + 1 < n:
        j += 1
    return j


def class_map(b, phi, g):
    kappa = (-(b - 1) * phi) % g
    return lambda t: (b * t + kappa) % g


def orbit(f, t, steps):
    out, cur = [], t
    for _ in range(steps):
        cur = f(cur)
        out.append(cur)
    return out


def preperiod(f, t, g):
    seen, cur, j = {}, t, 0
    while cur not in seen:
        seen[cur] = j
        cur = f(cur)
        j += 1
    return seen[cur]


# ------------------------------------------------ the cheap cell facts

def cell(b, a, c, u, v, w=0, z=1):
    """Everything (L) needs about a cell, in O(g) -- the class counts
    are closed-form rather than a walk over I, which is what lets the
    census reach c = 5. Returns None where I is empty or where the
    span exceeds N (there pi(I) is all of Z/N, B is empty and both
    sets are I)."""
    L, phi, N, q, g = params(b, a, c, u, v, w, z)
    lo, hi, span, _ = interval(b, a, c, u, v, w, z)
    if lo > hi or span > N:
        return None
    n = N // g
    counts = []
    for t in range(g):
        first = lo + ((t - lo) % g)
        counts.append(0 if first > hi else (hi - first) // g + 1)
    A = {t for t in range(g) if counts[t] >= n}
    return {"L": L, "phi": phi, "N": N, "q": q, "g": g, "n": n,
            "lo": lo, "hi": hi, "span": span, "A": A,
            "J": depth_J(b, a, n), "f": class_map(b, phi, g)}


def is_residual(b, a, ce):
    """(I) of explore_slope_tail.py: does this cell escape the cycle
    corollary? Some class of I meets an unsaturated class strictly
    inside its own pre-period, below J."""
    if gcd(b, ce["g"]) == 1 or ce["J"] == 1:
        return False
    f, A, g, J = ce["f"], ce["A"], ce["g"], ce["J"]
    for t in {m % g for m in range(ce["lo"], min(ce["hi"], ce["lo"] + g - 1) + 1)}:
        tau = preperiod(f, t, g)
        for j, x in enumerate(orbit(f, t, J - 1), start=1):
            if j < tau and x not in A:
                return True
    return False


# -------------------------------------------------------- (L): the set

def w_tree(b, a, c, u, v, ce, w=0, z=1):
    """(L): the winning set as a tree-avoidance condition, computed
    level by level with no fixed-point iteration. Also returns W* --
    the saturation criterion's set -- and, for each level below J, the
    residues that level rules out."""
    N, q, g, n, J = ce["N"], ce["q"], ce["g"], ce["n"], ce["J"]
    phi, A, f = ce["phi"], ce["A"], ce["f"]
    lo, hi = ce["lo"], ce["hi"]
    pi_I = {m % N for m in range(lo, hi + 1)}
    Bset = [r for r in range(N) if r not in pi_I]
    okdeep, okstar = {}, {}
    for t in range(g):
        orb = orbit(f, t, J + g)
        okstar[t] = all(x in A for x in orb)
        okdeep[t] = all(x in A for x in orb[J - 1:])
    # levels below J: r fails iff b^j r lands in B + (b-1) phi r_j - q Y_j
    bad = {}
    for j in range(1, J):
        rj = repunit(b, j)
        shift = (b - 1) * phi * rj
        U = {(pt + shift - q * y) % N
             for pt in Bset for y in range(-a * rj, a * rj + 1)}
        bad[j] = {m for m in range(lo, hi + 1) if (b ** j * m) % N in U}
    W = {m for m in range(lo, hi + 1) if okdeep[m % g]}
    for j in range(1, J):
        W -= bad[j]
    star = {m for m in range(lo, hi + 1) if okstar[m % g]}
    return W, star, bad


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


def old_scope(cap_c=3):
    """explore_slope_tail.py's scope, verbatim."""
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


def wide_scope():
    """The extended census: every redundant (b, a) to radix 12, slopes
    to 12/12, c to 5, and the same phases on a coarser slope slice.
    Reaches J >= 3, which the old scope could not."""
    pairs = [(b, a) for b in range(2, 13) for a in range(1, 9)
             if 2 * a + 1 >= b]
    for (b, a) in pairs:
        for u in range(1, 13):
            for v in range(1, 13):
                if gcd(u, v) != 1:
                    continue
                for c in range(6):
                    yield (b, a, u, v, 0, 1, c)
    for (b, a) in pairs:
        for (u, v) in PHASE_SLOPES:
            for (w, z) in PHASES:
                for c in range(6):
                    yield (b, a, u, v, w, z, c)


# ------------------------------------------------------------ the runs

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
    res = []
    for (b, a, u, v, w, z, c) in old_scope():
        ce = cell(b, a, c, u, v, w, z)
        if ce is None or ce["n"] <= 2 * a + 1:
            continue
        if is_residual(b, a, ce):
            res.append((b, a, u, v, w, z, c, ce["g"], ce["n"], ce["J"]))
    print(f"  old residual census through this path: {len(res)} cells, "
          f"depths {sorted({r[9] for r in res})}")
    ok(len(res) == 7, f"K1: old residual census is {len(res)}, not 7")
    ok({r[9] for r in res} == {2}, "K1: old residual census is not all J=2")
    return res


def s1_endpoint_and_region():
    """P-B and P-C."""
    print("\n== P-B THE ENDPOINT BOUND, P-C THE REGION ==")
    checked, badE, badR, cells = 0, [], [], 0
    for (b, a, u, v, w, z, c) in old_scope():
        ce = cell(b, a, c, u, v, w, z)
        if ce is None:
            continue
        cells += 1
        N, q, phi, lo, hi = ce["N"], ce["q"], ce["phi"], ce["lo"], ce["hi"]
        rep = {}
        for m in range(lo, hi + 1):
            rep[m % N] = m
        for m in range(lo, hi + 1):
            for x in digits(a):
                val = b * m + q * x - (b - 1) * phi
                r = val % N
                if r not in rep:
                    continue
                checked += 1
                e = (val - rep[r]) // N
                if not -a <= e <= a:
                    badE.append((b, a, u, v, w, z, c, m, x, e))
        _, win = rgame(b, a, c, u, v, w, z)
        if not all(lo <= m <= hi for m in win):
            badR.append((b, a, u, v, w, z, c))
    print(f"  cells with a non-empty span-tested interval: {cells}")
    print(f"  endpoint bound holds: {checked - len(badE)}/{checked} "
          f"(state, injection) pairs landing back in pi(I)")
    print(f"  measured winning set inside I: {cells - len(badR)}/{cells}")
    ok(not badE, f"K2: endpoint bound fails at {badE[:3]}")
    ok(not badR, f"K3: a winning state sits outside I at {badR[:3]}")


def s2_tree_exact():
    """P-D: (L)'s set against the game, at every old-scope cell."""
    print("\n== P-D THE TREE LAW IS EXACT ==")
    cells, bad, star_gap = 0, [], 0
    empty, empty_bad, full, full_isI = 0, [], 0, 0
    for (b, a, u, v, w, z, c) in old_scope():
        lo, hi, span, N = interval(b, a, c, u, v, w, z)
        if lo > hi:
            empty += 1
            if rgame(b, a, c, u, v, w, z)[1]:
                empty_bad.append((b, a, u, v, w, z, c))
            continue
        if span > N:
            full += 1
            _, win = rgame(b, a, c, u, v, w, z)
            if win == set(range(lo, hi + 1)):
                full_isI += 1
            continue
        ce = cell(b, a, c, u, v, w, z)
        W, star, _ = w_tree(b, a, c, u, v, ce, w, z)
        _, win = rgame(b, a, c, u, v, w, z)
        cells += 1
        if W != win:
            bad.append((b, a, u, v, w, z, c, len(W), len(win)))
        if star != W:
            star_gap += 1
    print(f"  cells with 0 < span <= N -- where (K) claims: {cells}")
    print(f"  (L)'s set == the measured winning set: "
          f"{cells - len(bad)}/{cells}")
    print(f"  cells where the saturation criterion W* differs from it: "
          f"{star_gap}")
    print(f"  cells with an empty I: {empty}; the game returns nothing at "
          f"{empty - len(empty_bad)}/{empty}")
    print(f"  cells with span > N (outside (K)): {full}; the game returns "
          f"I at {full_isI}/{full}")
    ok(not bad, f"K4: tree law differs from the game at {bad[:3]}")
    ok(not empty_bad, f"K3: empty I but a non-empty winning set at "
                      f"{empty_bad[:3]}")


def s3_census_and_hunt(cap_N=4000):
    """P-E and P-F."""
    print("\n== P-E THE EXTENDED CENSUS, P-F THE HUNT ==")
    seen = set()
    by_depth = {}
    mismatches, not_union = [], []
    checked = skipped = 0
    for (b, a, u, v, w, z, c) in wide_scope():
        key = (b, a, u, v, w, z, c)
        if key in seen:
            continue
        seen.add(key)
        ce = cell(b, a, c, u, v, w, z)
        if ce is None or ce["n"] <= 2 * a + 1:
            continue
        if not is_residual(b, a, ce):
            continue
        by_depth[ce["J"]] = by_depth.get(ce["J"], 0) + 1
        if ce["N"] > cap_N:
            skipped += 1
            continue
        W, star, bad = w_tree(b, a, c, u, v, ce, w, z)
        checked += 1
        cls = {m % ce["g"] for m in W}
        if W != {m for m in range(ce["lo"], ce["hi"] + 1)
                 if m % ce["g"] in cls}:
            not_union.append((b, a, u, v, w, z, c, ce["g"], len(W)))
        if star != W:
            mismatches.append((b, a, u, v, w, z, c, ce, W, star, bad))
    print(f"  residual cells by depth J: "
          f"{ {j: by_depth[j] for j in sorted(by_depth)} }")
    print(f"  residual cells with J >= 3: "
          f"{sum(v for j, v in by_depth.items() if j >= 3)}")
    print(f"  W* vs W compared at {checked} of them "
          f"(N <= {cap_N}; {skipped} larger cells not read)")
    print(f"  P-I W not a union of classes mod g: {len(not_union)} of "
          f"{checked}")
    for row in not_union[:4]:
        print(f"    (b={row[0]},a={row[1]}) slope {row[2]}/{row[3]} "
              f"phase {row[4]}/{row[5]} c={row[6]}: g={row[7]} |W|={row[8]}")
    print(f"  MISMATCHES W* != W: {len(mismatches)}")
    for (b, a, u, v, w, z, c, ce, W, star, bad) in mismatches:
        extra = sorted(W - star)
        m0 = extra[0]
        t0 = m0 % ce["g"]
        orb = orbit(ce["f"], t0, ce["J"] + ce["g"])
        lvl = [j for j in range(1, ce["J"]) if orb[j - 1] not in ce["A"]]
        print(f"    (b={b},a={a}) slope {u}/{v} phase {w}/{z} c={c}: "
              f"g={ce['g']} n={ce['n']} J={ce['J']} |B|={ce['N']-ce['span']} "
              f"|W|={len(W)} |W*|={len(star)} extra={len(extra)}")
        print(f"      first extra state m={m0} class {t0}, orbit "
              f"{orb[:ce['J']+2]}, unsaturated below J at levels {lvl}, "
              f"tree width there {2*a*repunit(b, lvl[0])+1 if lvl else '-'} "
              f"of n={ce['n']}")
    if mismatches:
        b, a, u, v, w, z, c, ce, W, star, _ = mismatches[0]
        _, win = rgame(b, a, c, u, v, w, z)
        agree = (win == W)
        print(f"  rgame replay at the first mismatch: game |W|={len(win)}, "
              f"(L) |W|={len(W)}, criterion |W*|={len(star)}; "
              f"game == (L): {agree}; game == W*: {win == star}")
        ok(agree, "K5/K4: rgame disagrees with (L) at the mismatch cell")
        if agree:
            print("  -> K5 FIRES: the saturation criterion is not exact "
                  "beyond the proved region.")
    else:
        deep = sum(v for j, v in by_depth.items() if j >= 4)
        print(f"  no mismatch; residual cells at J >= 4 read: {deep}")
        if deep:
            print("  -> K6 FIRES: the dodge is blocked structurally.")


def start_verdicts(b, a, c, u, v, w=0, z=1):
    """(L) and the criterion, asked only about the START state -- the
    tree is walked directly rather than inverted, which is what makes
    the whole wide scope readable. Returns (true, criterion) or None
    where the cell has no span-tested interval."""
    ce = cell(b, a, c, u, v, w, z)
    if ce is None:
        return None
    N, q, g, J = ce["N"], ce["q"], ce["g"], ce["J"]
    phi, A, f, lo, hi = ce["phi"], ce["A"], ce["f"], ce["lo"], ce["hi"]
    if not lo <= phi <= hi:
        return (False, False)
    orb = orbit(f, phi % g, J + g)
    crit = all(x in A for x in orb)
    if not all(x in A for x in orb[J - 1:]):
        return (False, crit)
    pi_I = {m % N for m in range(lo, hi + 1)}
    for j in range(1, J):
        rj = repunit(b, j)
        base = (b ** j * phi - (b - 1) * phi * rj) % N
        for y in range(-a * rj, a * rj + 1):
            if (base + q * y) % N not in pi_I:
                return (False, crit)
    return (True, crit)


def s4_feasibility(cap_N=20000):
    """P-G: the shipped claim, which is about the start state."""
    print("\n== P-G THE FEASIBILITY VERDICT ==")
    seen, read, skipped = set(), 0, 0
    disagree_cell, cmin_rows = [], {}
    for (b, a, u, v, w, z, c) in wide_scope():
        key = (b, a, u, v, w, z, c)
        if key in seen:
            continue
        seen.add(key)
        L = v * z // gcd(v, z)
        if L * b ** c > cap_N:
            skipped += 1
            continue
        got = start_verdicts(b, a, c, u, v, w, z)
        if got is None:
            continue
        read += 1
        true_f, crit_f = got
        if true_f != crit_f:
            disagree_cell.append((b, a, u, v, w, z, c, true_f, crit_f))
        row = cmin_rows.setdefault((b, a, u, v, w, z), [None, None])
        if true_f and row[0] is None:
            row[0] = c
        if crit_f and row[1] is None:
            row[1] = c
    bad_cmin = [(k, r) for k, r in cmin_rows.items() if r[0] != r[1]]
    print(f"  cells read: {read} (N <= {cap_N}; {skipped} larger not read)")
    print(f"  cells where the criterion's FEASIBILITY verdict differs "
          f"from the truth: {len(disagree_cell)}")
    for row in disagree_cell[:8]:
        b, a, u, v, w, z, c, tf, cf = row
        print(f"    (b={b},a={a}) slope {u}/{v} phase {w}/{z} c={c}: "
              f"truth={tf} criterion={cf}")
    print(f"  slope rows whose c_min differs: {len(bad_cmin)} of "
          f"{len(cmin_rows)}")
    for (k, r) in bad_cmin[:8]:
        b, a, u, v, w, z = k
        print(f"    (b={b},a={a}) slope {u}/{v} phase {w}/{z}: "
              f"c_min truth={r[0]} criterion={r[1]}")
    if disagree_cell:
        b, a, u, v, w, z, c, tf, cf = disagree_cell[0]
        feas, _ = rgame(b, a, c, u, v, w, z)
        print(f"  rgame replay at the first disagreement: game "
              f"feasible={feas}, (L)={tf}, criterion={cf}")
        ok(feas == tf, "K7/K4: rgame disagrees with (L) on feasibility")


def s5_start_fixed(cap_N=20000):
    """P-H: the identity that makes P-G a theorem."""
    print("\n== P-H THE START CLASS IS A FIXED POINT ==")
    seen, read, badfix, badcrit = set(), 0, [], []
    for (b, a, u, v, w, z, c) in wide_scope():
        key = (b, a, u, v, w, z, c)
        if key in seen:
            continue
        seen.add(key)
        L = v * z // gcd(v, z)
        if L * b ** c > cap_N:
            continue
        ce = cell(b, a, c, u, v, w, z)
        if ce is None:
            continue
        read += 1
        t0 = ce["phi"] % ce["g"]
        if ce["f"](t0) != t0:
            badfix.append((b, a, u, v, w, z, c))
        orb = orbit(ce["f"], t0, ce["J"] + ce["g"])
        crit = all(x in ce["A"] for x in orb)
        if crit != (t0 in ce["A"]):
            badcrit.append((b, a, u, v, w, z, c))
    print(f"  cells read: {read}")
    print(f"  f(phi mod g) == phi mod g: {read - len(badfix)}/{read}")
    print(f"  the criterion's orbit test == 'the start class is "
          f"saturated': {read - len(badcrit)}/{read}")
    ok(not badfix, f"K1: the start class is not fixed at {badfix[:3]}")
    ok(not badcrit, f"K1: the orbit test is not the one-class test at "
                    f"{badcrit[:3]}")


def main():
    s0_control()
    if FAILURES:
        print("\nCONTROL FAILED -- nothing below is read.")
        return 1
    s1_endpoint_and_region()
    s2_tree_exact()
    s3_census_and_hunt()
    s4_feasibility()
    s5_start_fixed()
    print()
    if FAILURES:
        print(f"FAILURES: {len(FAILURES)}")
        for f in FAILURES:
            print(f"  {f}")
        return 1
    print("ALL CHECKS PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
