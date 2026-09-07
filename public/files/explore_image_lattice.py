"""explore_image_lattice.py -- the reachable SHAPES of the corner schedule
with no walk run, and so the greedy image as a closed formula.

THE QUESTION. The image of the corner schedule at a move budget N is a sum,
over the shapes the identity-free walker can reach in N moves, of a
multinomial read off the supply (explore_schedule_image.py L3, F1). The
multinomial needs no dynamics; the shapes were the one thing the dynamics was
still run for -- one or two per supply at the budgets read, sixteen over
eight supplies. This rig asks whether the shape set follows from the price
alone: the void menu, the tick ladder and the degree ceiling, with no menu
ever scanned. If it does, |Im(N)| is a closed formula in the supply vector
and the count owes the walk nothing.

THE CORNER, restated so that nothing below leans on the walker. Items carry
a degree d, n_d of them at degree d. A state seats items at exponents and
carries a tick T, starting at 1. Degree 1 is born covered; any other degree
is covered once opened. An opening at an uncovered degree pays door 1 and
lands at exponent 1 with no tick change (FRESH). Every other move -- an
opening at a covered degree, or a raise of a seated item at exponent e --
pays door T + 1 - e (e = 0 for an opening) and lands at T + 1, which
doubles the tick (CLOCK). The price is d times the door; a move is a
minimal-price one; ties are every minimal move.

THE HAND-ATTACK, on paper before any engine code.

 L1 THE FIRST CLOCK MOVER IS THE ONLY DEEP ITEM. At T = 1 the menu holds
    the born-covered least degree b0 at door 2, price 2*b0, and the least
    uncovered degree f0 fresh at price f0; every other move is dearer, since
    the price rises with the degree at a fixed door. So before the first
    clock at most one fresh opening happens, f0's, and the first clock is
    either b0's opening (landing at 2) or f0's raise (door 1, price f0, also
    landing at 2). Either way the mover sits at T + 1 = 2 with door 1 next.
    After j clock moves on it the tick is 2^j (born world) or 2^(j-1)
    (fresh world) and the item sits at T/2 + 1, so its door is T/2 and its
    price D*T/2 where D is its degree. Every OTHER seated item sits at
    exponent 1 with door T, price d*T; every covered opening prices
    d*(T + 1). With D <= 2*d_min -- the ceiling, and here the void rule
    gives D = b0 or D = f0 <= 2*b0 -- the deep move is strictly cheaper than
    all of these at every T >= 2, so no second item is ever raised and no
    covered degree is ever reopened. That is the ideal limit theorem of
    explore_greedy_limit.py read at the corner; it is restated here because
    the lattice below is nothing but its consequence.
 L2 THE WALK IS A MERGE OF TWO SEQUENCES. By L1 the only moves ever taken
    are the deep item's clock moves and fresh openings, and a fresh opening
    is taken at the least uncovered present degree, since the price is the
    degree. So a trajectory in a world is an interleaving of two fixed
    sequences: the deep item's prices c_1, c_2, ... (born world: 2D, D, 2D,
    4D, ...; fresh world: D, D, D, 2D, 4D, ...) and the present degrees
    other than D in increasing order, g_1 < g_2 < ... (degree 1 excluded in
    the fresh world, since a covered opening is never minimal). A state is
    a cell (j, i): j moves of the deep item taken (its opening the first
    of them in the fresh world), i degrees opened. The step from
    (j, i) may go to (j + 1, i) iff c_(j+1) <= g_(i+1) and to (j, i + 1)
    iff g_(i+1) <= c_(j+1); both at a tie. The state at (j, i) is the deep
    item at exponent E(j) -- born: 2^(j-1) + 1; fresh: 1 at j = 1, else
    2^(j-2) + 1 -- beside the first i degrees at exponent 1.
 L3 THE SHAPES AT N ARE THE LATTICE'S N-TH ANTIDIAGONAL. Since every step
    adds one to j + i, the shapes reachable in exactly N moves are the
    reachable cells with j + i = N, and a shape's orbit is n_D times the
    product of n_g over the i opened degrees (each block holds one item at
    one exponent; L3 of explore_schedule_image.py). Two worlds share
    exactly one cell -- the born world's (0, 1) and the fresh world's
    (1, 0) are both "f0 seated at 1, nothing else, T = 1" -- and no other,
    since a born-world cell with j >= 1 seats b0 and a fresh-world cell
    never does. So

      |Im(N)| = sum over worlds, over cells (j, i) on antidiagonal N, of
                n_D * prod_(k <= i) n_(g_k),  the shared cell counted once.

 L4 THE WIDTH. From a tie at (j, i) the two successors are (j+1, i) and
    (j, i+1). From the first the deep price c_(j+2) is at least 2*c_(j+1)
    once j + 1 >= 2 in the born world (j + 1 >= 3 in the fresh one), above
    g_(i+1) = c_(j+1), so the fresh opening is forced; from the second the
    next degree g_(i+2) > g_(i+1) = c_(j+1) forces the clock. Both land at
    (j+1, i+1): a tie is a window of width 2 at one budget and closes at
    the next. The exception is the void tie of the born world, 2*b0 = f0,
    where c_2 = D < c_1 lets the deep item run twice before f0's window
    closes: cells (1,0),(0,1) then (2,0),(1,1) then (3,0),(2,1), width 2
    at N = 1, 2, 3. So a world's antidiagonal is 1 or 2 cells wide, never
    3, and the shape count at N is 1, 2, 3 or 4.
 L5 WHAT MERGES. A limit reading forgets the deep exponent, so two cells
    (j, i) and (j', i) in one world, both past the first clock move, are
    one reading. Over a pooled window of
    budgets the merged-reading count is the sum, over worlds and over i
    with two or more j reachable in the window, of n_D * prod n_g -- the
    number explore_schedule_image.py F4 measured.

TRANSPLANT FLAGS, fixed at the freeze.
 1. From the walker's code to the lattice: NOTHING. The lattice is built
    from the supply vector and the three constants of the corner (born set
    {1}, doubling clock, price d*door); it never constructs a menu. The
    walker is run only as the control, and its states are read through
    explore_schedule_image.py's own reach and by_shape, never re-derived.
 2. From the corner to any other dial: nothing. At b = 3 the clock hands
    off and strands, at m = 2 a degree opens twice, at the additive price
    the ceiling is gone; L1 is a corner fact and the lattice is a corner
    object.
 3. The toy supplies are abstract, as in the companion rigs; one is added
    with NO degree-1 item, where the born world is empty and the void rule
    must return the fresh world alone.

THE PREDICTIONS, fixed before any engine code, each naming what the rig
PRINTS.

PR1 THE VOID RULE. What the rig PRINTS: per supply, the worlds the void
    menu seats -- born at degree b0 if 2*b0 <= f0, fresh at f0 if f0 <=
    2*b0 -- against explore_price_schedule.py's void_winners.
    KILL: a disagreement.
PR2 THE SHAPE SET AT EVERY BUDGET. What the rig PRINTS: per supply and per
    budget N from 0 to the enumeration's budget, the lattice's shape count
    and the enumeration's, and the number of shapes in either set and not
    the other. KILL: a nonzero symmetric difference at any N, in either
    direction.
PR3 THE COUNT. What the rig PRINTS: per supply and per N, |Im(N)| from L3
    and the enumeration's configuration count. KILL: one N off.
PR4 THE MERGE COUNT. What the rig PRINTS: over the window of budgets 3 to
    8, per supply, L5's merged-reading count and the enumeration's, with
    F4's four figures recalled beside them. KILL: one off.
PR5 THE WIDTH. What the rig PRINTS: per supply, the widest antidiagonal
    of each world and the budgets at which it is 2. KILL: a width of 3;
    a born world with a void tie whose width-2 budgets are not {1, 2, 3}
    plus the later tie budgets.
PR6 THE ONE-WORLD SUPPLY. What the rig PRINTS: h5's worlds and its shape
    count at 8. KILL: anything but one world and one shape.

THE CONTROL, run before any result is read: the same comparison with the
lattice built on a WRONG ladder (the deep price sequence shifted by one
clock move) must disagree with the enumeration at some budget on every
supply, or the comparison has no teeth.

FINDINGS (tiers below; run record at the bottom). The control parted at
budget 3 on all nine supplies -- later than 1, because a shifted ladder
changes prices before it changes states: the deep item's first moves are
forced under either ladder, and the lattices part at the first budget
where a price meets a degree -- and the void rule agreed with
void_winners at all nine.

F1 THE SHAPES NEED NO WALK (proved for the corner schedule, L1 to L4, and
   a rule in range: nine supplies -- the six ring supplies at budgets 0 to
   8, two toys and a toy with no degree-1 item at 0 to 10 -- 87 (supply,
   budget) rows, 176 shapes, 0 in either set and not the other, every
   shape's orbit equal to its configuration count). The reachable shapes
   at N are the cells of a two-sequence merge lattice on its N-th
   antidiagonal, one lattice per world the void menu seats. The counts the
   companion rig read at its budgets -- 2, 2, 2, 2, 1, 2 at the rings, 3
   and 2 at the toys -- are those antidiagonals, and every budget between
   is matched as well. The hypothesis carried in, that lockstep makes each
   world ONE shape at every budget, is false at the tie budgets and true
   between them: the two orders of a clock/fresh tie meet one move later,
   but at the tie budget itself they are two shapes.

F2 THE IMAGE IS A CLOSED FORMULA (the same evidence; |Im(N)| matched at all
   87 rows, 396 at F_2[x], 672 at h2, 7920 at h3, 4864 at h4, 16000 at h5,
   4608 at g2 at budget 8; and the merged-reading count over budgets 3 to
   8 matched the companion rig's 26, 75, 40 and 153 at F_2[x], h2 and the
   two toys, and over every budget from the void at all nine supplies: 29,
   79, 29, 27, 24, 34, 44, 159, 14). |Im(N)| is the sum over worlds, over
   the cells (j, i) of
   antidiagonal N, of n_D times the product of n_g over the first i
   degrees, the one shared cell counted once; what merges under the limit
   reading is every i two cells share, and its count is L5's sum.

F3 THE WIDTH IS ONE OR TWO, AND EVERY TWO IS A TIE (rule in range; 16
   worlds over the nine supplies, widest antidiagonal 2 at 15 of them and
   1 at h3's fresh world, which meets no tie by budget 8). A born world
   with a void tie is 2 wide at budgets 1, 2, 3 -- the deep item's second
   move at price D under its first at 2D -- and afterwards exactly at the
   budgets where the deep price meets the next degree: 6 at F_2[x] and h2
   (price 4 against degree 4), 5 at h4 and g2 (degree 4 with no degree 3),
   4 at h5 (degree 4 with no 2 or 3); the fresh world at 5 (price 4 against
   degree 4) or 4. Each width-2 pair is (j+1, i) beside (j, i+1) with
   c_(j+1) = g_(i+1), asserted at every one. So a supply reaches 1, 2 or 3
   shapes at a budget over this range, never 4, though L4 allows it.

F4 ONE WORLD, ONE SHAPE (rule in range). h5 seats the born world alone,
   its first fresh degree 4 pricing above the born opening's 2, and reads
   one shape at every budget but 4, its first tie; the toy with no
   degree-1 item seats the fresh world alone and reads one shape at every
   budget but 5.

RUN RECORD. One process, CPython, no BLAS. Wall 2.3 s, peak working set
66 MB against the 512 MB ceiling. 460 checks here; the enumeration is the
companion rig's own reach, run at every budget rather than one.
"""

import os

os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")

import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import explore_greedy_limit as GL
import explore_coarse_type as CT
import explore_price_schedule as PS
import explore_schedule_image as SI

CHECKS = 0

RING_BUDGET = 8      # the enumeration's budget at the ring supplies
TOY_BUDGET = 10      # and at the toys
WINDOW = (3, 8)      # F4's pooled window


def ok(cond, msg):
    global CHECKS
    assert cond, msg
    CHECKS += 1


def section(t):
    print("\n" + "=" * 72)
    print(t)
    print("=" * 72)


# ------------------------------------------------------------- the lattice
def present(npl):
    return [d for d in range(1, len(npl)) if npl[d]]


def worlds(npl):
    """PR1: the void rule. (kind, D) per world, kind 'born' or 'fresh'."""
    degs = present(npl)
    born = [d for d in degs if d == 1]
    fresh = [d for d in degs if d != 1]
    bids = []
    if born:
        bids.append((2 * born[0], "born", born[0]))
    if fresh:
        bids.append((fresh[0], "fresh", fresh[0]))
    best = min(p for p, _, _ in bids)
    return [(k, D) for p, k, D in bids if p == best]


def deep_price(kind, D, j, shift=0):
    """c_j: the price of the deep item's j-th move. `shift` is the control's
    wrong ladder, one clock move early."""
    j += shift
    if kind == "born":
        return 2 * D if j == 1 else D * 2 ** (j - 2)
    return D if j <= 3 else D * 2 ** (j - 3)


def deep_exp(kind, j):
    """E(j): the deep item's exponent after j moves."""
    if j == 0:
        return 0
    if kind == "born":
        return 2 ** (j - 1) + 1
    return 1 if j == 1 else 2 ** (j - 2) + 1


def lattice(npl, kind, D, nmax, shift=0):
    """The reachable cells (j, i) of one world up to antidiagonal nmax, as
    {N: sorted cells}."""
    g = [d for d in present(npl) if d != D and not (kind == "fresh" and d == 1)]
    cells = {0: [(0, 0)]}
    for N in range(nmax):
        nxt = set()
        for j, i in cells[N]:
            c = deep_price(kind, D, j + 1, shift)
            gi = g[i] if i < len(g) else None
            if gi is None or c <= gi:
                nxt.add((j + 1, i))
            if gi is not None and gi <= c:
                nxt.add((j, i + 1))
        cells[N + 1] = sorted(nxt)
    return g, cells


def cell_shape(npl, kind, D, g, j, i):
    """The shape at a cell in explore_schedule_image.py's own key."""
    shp = {}
    if j:
        shp[D] = (deep_exp(kind, j),)
    for d in g[:i]:
        shp[d] = (1,)
    return tuple(sorted(shp.items()))


def cell_orbit(npl, g, j, i, D):
    out = npl[D] if j else 1
    for d in g[:i]:
        out *= npl[d]
    return out


def derived(npl, nmax, shift=0):
    """{N: {shape: orbit}} over all worlds, the shared cell counted once,
    plus the per-world lattices for the width and merge readings."""
    out = {N: {} for N in range(nmax + 1)}
    per = []
    for kind, D in worlds(npl):
        g, cells = lattice(npl, kind, D, nmax, shift)
        per.append((kind, D, g, cells))
        for N, cs in cells.items():
            for j, i in cs:
                shp = cell_shape(npl, kind, D, g, j, i)
                orb = cell_orbit(npl, g, j, i, D)
                if shp in out[N]:
                    ok(out[N][shp] == orb,
                       "a shared cell with two orbit sizes at N = %d" % N)
                out[N][shp] = orb
    return out, per


def merged_count(npl, per, lo, hi):
    """L5 over the window [lo, hi]. A cell with no clock move yet -- j = 0
    in the born world, j <= 1 in the fresh one, where the first move is the
    opening -- has no deep item to forget and is its own reading."""
    tot = 0
    for kind, D, g, cells in per:
        byi = {}
        for N in range(lo, hi + 1):
            for j, i in cells[N]:
                if j >= (1 if kind == "born" else 2):
                    byi.setdefault(i, set()).add(j)
        for i, js in byi.items():
            if len(js) >= 2:
                tot += cell_orbit(npl, g, 1, i, D)
    return tot


# ------------------------------------------------------- the enumeration
def enumerated(npl, name, nmax):
    """{N: {shape: configurations}} from the walker, and the states."""
    out, states = {}, {}
    for N in range(nmax + 1):
        st = SI.reach(npl, PS.Sched("corner"), name, N)
        states[N] = st
        out[N] = dict((shp, len(c)) for shp, c in SI.by_shape(st).items())
    return out, states


def enumerated_merged(states, lo, hi):
    rd = {}
    for N in range(lo, hi + 1):
        for s in states[N]:
            rd.setdefault(s.reading(), set()).add(s.config())
    return sum(1 for v in rd.values() if len(v) > 1)


# --------------------------------------------------------------- sections
def s0_control(supplies, names, budgets):
    print("  the lattice on a ladder one clock move early, against the")
    print("  enumeration: it must part somewhere on every supply")
    print("  supply     first budget where the wrong lattice parts")
    for name in names:
        npl = supplies[name]
        der, _ = derived(npl, budgets[name], shift=1)
        enu, _ = enumerated(npl, name, budgets[name])
        first = next((N for N in range(budgets[name] + 1)
                      if set(der[N]) != set(enu[N])), None)
        print("  %-10s %s" % (name, first if first is not None else "NEVER"))
        ok(first is not None, "%s: the wrong ladder agrees everywhere, so "
           "the comparison has no teeth" % name)


def s1_void(supplies, names):
    print("  supply     worlds                 void_winners")
    for name in names:
        npl = supplies[name]
        ws = worlds(npl)
        vw = PS.void_winners(PS.Sched("corner"), npl)
        print("  %-10s %-22s %s"
              % (name, " ".join("%s@%d" % w for w in ws), sorted(vw)))
        ok(set(D for _, D in ws) == vw,
           "%s: the void rule seats %s, void_winners %s" % (name, ws, vw))
    return None


def s2_shapes(supplies, names, budgets):
    print("  per supply, per budget: shapes derived / enumerated, the")
    print("  symmetric difference, and |Im(N)| derived / enumerated")
    results = {}
    for name in names:
        npl = supplies[name]
        nmax = budgets[name]
        der, per = derived(npl, nmax)
        enu, states = enumerated(npl, name, nmax)
        results[name] = (der, per, enu, states)
        print("  %s" % name)
        print("    N   shapes d/e  off   |Im| derived   |Im| enumerated")
        for N in range(nmax + 1):
            a, b = set(der[N]), set(enu[N])
            off = len(a ^ b)
            sd = sum(der[N].values())
            se = sum(enu[N].values())
            print("    %-3d %d/%-9d %-5d %-14d %d" % (N, len(a), len(b),
                                                     off, sd, se))
            ok(off == 0, "%s: %d shapes off at N = %d: derived-only %s, "
               "enumerated-only %s" % (name, off, N, sorted(a - b),
                                       sorted(b - a)))
            ok(sd == se, "%s: |Im(%d)| derived %d against %d" % (name, N,
                                                                 sd, se))
            for shp in a:
                ok(der[N][shp] == enu[N][shp],
                   "%s: shape %s orbit %d against %d configurations at N = "
                   "%d" % (name, shp, der[N][shp], enu[N][shp], N))
    return results


def s3_merge(results, names, lo, hi, recalled):
    print("  supply     merged derived  merged enumerated  F4 recalled")
    for name in names:
        npl_per = results[name]
        der, per, enu, states = npl_per
        npl = states[0][0].npl
        a = merged_count(npl, per, lo, hi)
        b = enumerated_merged(states, lo, hi)
        r = recalled.get(name)
        print("  %-10s %-15d %-18d %s" % (name, a, b, r if r is not None
                                          else "-"))
        ok(a == b, "%s: merged %d derived against %d" % (name, a, b))
        if r is not None:
            ok(a == r, "%s: merged %d against F4's %d" % (name, a, r))


def s4_width(results, names):
    print("  supply     world     widest  budgets of width 2")
    for name in names:
        der, per, enu, states = results[name]
        npl = states[0][0].npl
        for kind, D, g, cells in per:
            widths = dict((N, len(cs)) for N, cs in cells.items())
            two = [N for N, w in widths.items() if w == 2]
            print("  %-10s %-9s %-7d %s" % (name, "%s@%d" % (kind, D),
                                            max(widths.values()), two))
            ok(max(widths.values()) <= 2, "%s: a width of %d" % (name,
                                                               max(widths.values())))
            if kind == "born" and len(per) == 2:
                ok(set([1, 2, 3]) <= set(two),
                   "%s: the void window is not 1, 2, 3 wide: %s" % (name, two))
            # every width-2 budget past the void window is a tie budget:
            # the two cells are (j+1, i) and (j, i+1) with c_(j+1) = g_(i+1)
            for N in two:
                if kind == "born" and N <= 3 and len(per) == 2:
                    continue
                (j1, i1), (j2, i2) = sorted(cells[N])
                ok((j1 + 1, i1 - 1) == (j2, i2),
                   "%s: width 2 at N = %d is not a tie's window: %s"
                   % (name, N, cells[N]))
                ok(deep_price(kind, D, j2) == g[i1 - 1],
                   "%s: width 2 at N = %d with no tie behind it" % (name, N))


def main():
    supplies, ring_names, budgets = {}, [], {}
    for L in CT.build_ladder():
        _, npl, _, _ = GL.universe(L)
        supplies[L.name] = npl
        ring_names.append(L.name)
        budgets[L.name] = RING_BUDGET
    for tag, n, lo, hi in (("toy2", 2, 1, 8), ("toy3", 3, 1, 6),
                           ("toy-no1", 2, 2, 7)):
        npl = [0] * (PS.DEG_CAP + 2)
        for d in range(lo, hi + 1):
            npl[d] = n
        supplies[tag] = npl
        budgets[tag] = TOY_BUDGET
    toy_names = ["toy2", "toy3", "toy-no1"]
    names = ring_names + toy_names

    section("S0  THE CONTROL -- A WRONG LADDER MUST PART")
    s0_control(supplies, names, budgets)

    section("S1  THE VOID RULE")
    s1_void(supplies, names)

    section("S2  THE SHAPES AT EVERY BUDGET, DERIVED AGAINST ENUMERATED")
    results = s2_shapes(supplies, names, budgets)

    section("S3  THE MERGED READINGS OVER BUDGETS %d TO %d" % WINDOW)
    s3_merge(results, ring_names[:2] + toy_names[:2], WINDOW[0], WINDOW[1],
             {"F_2[x]": 26, "h2": 75, "toy2": 40, "toy3": 153})
    print("  and over every budget from the void, where the cells before the")
    print("  first clock move carry no deep item to forget:")
    s3_merge(results, names, 0, RING_BUDGET, {})

    section("S4  THE WIDTH")
    s4_width(results, names)

    section("S5  THE ONE-WORLD SUPPLY")
    der, per, enu, states = results["h5"]
    print("  h5: %d world(s), %d shape(s) at N = %d"
          % (len(per), len(der[RING_BUDGET]), RING_BUDGET))
    ok(len(per) == 1 and len(der[RING_BUDGET]) == 1,
       "h5 is not one world with one shape")

    section("SUMMARY")
    print("  %d checks passed here, %d in the imported image rig, %d in the "
          "imported walker." % (CHECKS, SI.CHECKS, PS.CHECKS))


if __name__ == "__main__":
    main()
