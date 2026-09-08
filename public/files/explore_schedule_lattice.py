"""explore_schedule_lattice.py -- the schedule family's images as ONE merge
lattice: the clock factor b as a dial, the b >= 3 strand as a third row, and
the exhausted and stopped images as the lattice's terminal cells.

THE QUESTION. The greedy image of the corner schedule at a move budget N is
the N-th antidiagonal of a two-row merge lattice -- the deep item's clock
ladder against the fresh openings in degree order -- with no walk run
(explore_image_lattice.py). Three other counts of the same family were each
derived on their own: the exhausted image n_h * prod n_d over a supply with a
top degree (explore_ladder_stop.py), the stopped image prod (n_h + 1) - 1
under a covering rule that outruns the ladder (explore_stopped_untie.py), and
the b >= 3 strand, an item the clock hands off and leaves above exponent 1,
multiplying the image as a free coordinate (explore_price_schedule.py F4,
explore_schedule_image.py F3). This rig asks whether all four are one
lattice read at different places: b changing the two ladders and nothing in
the merge rule, the strand a THIRD row that is a prefix, the exhausted and
stopped images the cells from which only the deep item ever moves again.

THE LATTICE, restated so that nothing below leans on a walker. Integer b;
the tick after m clock moves is b^m. An item last clocked when the tick was
T_0 sits at T_0 + 1 forever, so its door at tick T is T - T_0. Price is
d^alpha times the door. Three priced rows:
  BORN   the born-covered least degree D_b: opening at door T + 1 (a clock
         move), then door T - b^(m-1) at every later move, m the clock count.
  STRAND the void menu's fresh winner D_f, in the fresh world only: opened
         at door 1 with no clock, first raise at door T (1 at tick 1), then,
         after s moves (the opening counted), exponent b^(s-2) + 1 and door
         T - b^(s-2).
  FRESH  the least present degree not born-covered, not D_f, not yet opened
         and, under the covering rule "d is covered while d <= c T", above
         c T: door 1, no clock. A degree covered before it is opened is lost
         to this row for good, T never falling.
A cell is (world, s, j, opened degrees), and its shape and orbit are read
off the cell: the born item at b^(m-1) + 1 when j >= 1, the strand at 1 or
b^(s-2) + 1, one flat item per opened degree, the orbit the product of the
widths. A move takes every minimal row. The b = 2 corner is this lattice
with the strand row never handing off; the born world has no strand row.

THE HAND-ATTACK, on paper before any engine code.

 L1 THE HANDOFF. In the fresh world the born item's opening costs
    D_b (b^(s-1) + 1) at strand-phase cell s against the strand's next raise,
    D_f at s = 1 and D_f b^(s-2) (b - 1) at s >= 2. With D_f = 2 D_b, the
    void tie: a tie at s = 1 at every b (the born world's own flat opening of
    D_f, so an exponent-1 strand is no strand); at s >= 2 the born item wins
    iff b^(s-2) (b - 2) > 1 and ties iff it equals 1, which is b = 3 at s = 2
    exactly. So at b = 2 the fresh item is never handed off and IS the deep
    item; at b = 3 the strand row has length 3 (handoff at s = 2 by a tie or
    at s = 3 outright, strand exponents 2 and 4); at b = 4 length 2 (strand
    exponent 2 only).
 L2 THE STRAND ROW IS DEAD AFTER THE HANDOFF. With m = (s - 1) + j clock
    moves the strand prices D_f (b^m - b^(s-2)) against the born item's
    D_b b^(m-1) (b - 1), and D_f b^m - D_b b^(m-1)(b-1) >= D_f b^(m-1)
    >= D_f b^(s-1) > D_f b^(s-2) for D_f >= D_b and m >= s. So the third row
    is a PREFIX: s moves, then never. The born row is dead forever in the
    strand phase iff D_f (b - 1) <= D_b b (b = 2 at the void tie; the floor
    family's D_f = 3, D_b = 2 at b = 2), and otherwise fires at the first s
    with b^(s-2) (D_f (b-1) - D_b b) >= D_b.
 L3 TERMINAL CELLS. A cell from which only the deep item ever moves again
    has its fresh row dead forever: no eligible degree left above c T (a
    finite supply exhausted, or every remaining degree lost to the rule), or
    c >= D_deep (b - 1) / b, since the next uncovered degree is at least
    floor(c b^m) + 1 > c b^m >= D_deep b^(m-1) (b - 1) with no m in the
    verdict -- explore_stopped_untie.py F2's integrality step read as a cell
    criterion, D_deep the born item after the handoff and the strand's own
    degree where no born row can fire. The limit reading forgets the deep
    exponent, so a terminal cell's whole column in j is ONE reading, and the
    image at the limit is the sum over terminal cells, by reading, of the
    orbit, once every frontier cell is terminal.
 L4 THE EXHAUSTED IMAGE. With a top degree the fresh row is finite and
    every column but the last is finite in j (the deep price grows as b^m
    against a fixed g_(i+1)), so the terminal cells are the last column of
    each world: at b = 2, n_1 prod_(d>=2) n_d + n_2 prod_(d>=3) n_d, which at
    uniform width n over degrees 1..D is n^(D-1) (n + 1), the filed form. At
    b >= 3 the fresh world's last column is one reading per strand exponent:
    3 n^D at b = 3 and 2 n^D at b = 4 over the toys, the s = 1 handoff being
    the born reading.
 L5 THE STOPPED IMAGE. At b = 2 the fresh row is dead from the first clock
    at c >= D_deep / 2, so every opening happens at tick 1, in the row
    j = 0: the born world's cells (j, 0) and (j, 1) -- degree D_f opened at
    the void tie -- and the fresh world's column 0, reading n_b + n_b n_f +
    n_f = (n_b + 1)(n_f + 1) - 1, the filed form, tail widths never entering.
    At b = 3 the born row fires at THREE ticks (1, 3, 9) and the fresh row is
    truncated at each: at T = 3 degree 3 is lost and degree 4 ties three ways
    with the strand and the born opening; at T = 9 degree 10 ties with the
    born opening. So the stopped image at b = 3, c = 1 over a uniform width n
    is n + n^2 + n^2 (1 + n) + n^2 (1 + n)^2 -- a sum over strand exponents of
    products over the degrees tied at the handoff ticks, of which the filed
    product over the homes is the s <= 1 case.

TRANSPLANT FLAGS, fixed at the freeze.
 1. From explore_image_lattice.py: the merge rule and the cell-to-shape
    reading. The ladders are RE-DERIVED from the door rule with b in them and
    the b = 2 rows are recalled as a regression, never as evidence.
 2. From the b = 2 stop threshold c >= d_deep / 2 to b >= 3: nothing. L3 is
    derived with b symbolic and the b = 3 stop is a new prediction (L5).
 3. Integer b only. At a non-integer b the tick is ceil(bT) and the
    criterion of L3 carries a ceiling's slack; that dial is out of scope.
 4. One fresh discount per degree and one born-covered degree throughout,
    as in every family recalled; a second born-covered degree above D_b is
    excluded from the fresh row and never minimal at door T + 1.

THE PREDICTIONS, fixed before any engine code, each naming what the rig
PRINTS.

PR1 THE CONTROL. What the rig PRINTS: per (supply, b), the first budget at
    which the lattice on a born ladder shifted one clock move parts from the
    identified enumeration. KILL: NEVER on any row.
PR2 THE SHAPES AT EVERY BUDGET, b A DIAL. What the rig PRINTS: per supply
    and b in {2, 3, 4}, per budget N to 8, the shape count derived and
    enumerated, the symmetric difference, and |Im(N)| both ways; the six
    ring supplies at b = 2 with explore_image_lattice.py's budget-8 figures
    recalled (396, 672, 7920, 4864, 16000, 4608). KILL: a nonzero symmetric
    difference or one |Im(N)| off, at any (supply, b, N).
PR3 THE STRAND ROW. What the rig PRINTS: per (toy, b), the strand-phase
    cells s at which the born row fires (the handoffs), the strand exponents
    the handed-off cells carry, whether the strand row ever fires after a
    handoff, and the (strand, deep) pair count against the walker's at
    budget 8, with explore_schedule_image.py F3's 4 and 9 recalled. KILL:
    handoff cells off L1's {1}, {1, 2, 3}, {1, 2} at b = 2, 3, 4; a strand
    exponent off b^(s-2) + 1; a strand row firing after a handoff; a pair
    count off.
PR4 THE EXHAUSTED IMAGE AT b = 2. What the rig PRINTS: per (width, top)
    row of explore_ladder_stop.py's grid, the lattice's terminal-cell count
    against the filed 2, 96, 384, 324, 972, 1280, 5120; and at three rows
    the walker's reading set matched shape by shape. KILL: one row off.
PR5 THE EXHAUSTED IMAGE AT b >= 3. What the rig PRINTS: per toy and b in
    {3, 4}, the lattice's terminal-cell count against L4's 768, 2187, 512,
    1458, and the walker's reading set at two budgets past exhaustion --
    equal as sets -- matched shape by shape. KILL: one off; a frontier cell
    that is not terminal; a reading set that moves.
PR6 THE STOPPED IMAGE AT b = 2. What the rig PRINTS: per family of
    explore_stopped_untie.py (three tied widths, gapped, steep, floor at two
    widths, the mixed homes and its tail row), the lattice's terminal-cell
    count against the filed 3, 8, 15 / 2, 3 / 2, 3 / 2, 3 / 11, 11 and the
    walker's reading set shape by shape. KILL: one off.
PR7 THE STOPPED IMAGE AT b = 3. What the rig PRINTS: at c = 1 over uniform
    widths 1 and 2, the lattice's count against L5's 8 and 54, the terminal
    readings listed by (deep, strand exponent, optional degrees), and the
    walker's reading set shape by shape. KILL: one off.

THE CONTROL, run before any result is read: PR1's shifted ladder, and a
doctored reading table -- one shape's multiplicity moved by one -- that the
shape-by-shape checker must reject.

FINDINGS (tiers below; run record at the bottom; every section asserts).
The shifted ladder parted from the enumeration at budget 4 at b = 2, 3 at
b = 3 and 2 at b = 4 on every row -- earlier as b grows, the ladders
parting where a price first meets a degree -- and the doctored table was
rejected.

F1 THE FAMILY IS ONE LATTICE AND b IS A DIAL ON ITS LADDERS (proved for
   integer b, L1 to L3; rule in range: the six ring supplies at b = 2 and
   the two toys at b = 2, 3, 4, every budget to 8, 0 shapes in either set
   and not the other at any (supply, b, N), every |Im(N)| matched and every
   shape's orbit equal to its configuration count; the budget-8 figures
   396, 672, 7920, 4864, 16000, 4608 recalled and matched). The merge rule
   of explore_image_lattice.py is untouched; what b moves is the two
   ladders, c_(j+1) = D_b b^(m-1) (b - 1) and D_f b^(s-2) (b - 1), and
   what b >= 3 adds is a row.

F2 THE STRAND IS A THIRD ROW, A PREFIX, AND ITS HANDOFF CELLS ARE L1's
   (rule in range at the toys; the cells derived first). The born row
   fires in the fresh world at the strand-phase cells {1} at b = 2, {1, 2,
   3} at b = 3 and {1, 2} at b = 4, the handed-off cells carrying strand
   exponents {2, 4} and {2}, and the strand row fired 0 times after a
   handoff at every row. The (strand, deep) pairs read 4 and 9 at both b,
   the walker's own and explore_schedule_image.py F3's. A third row is a
   third direction: at b = 3 a toy reaches 5 shapes on one antidiagonal
   (224 configurations at N = 7, toy2), which the corner's width of 1 or 2
   per world cannot.

F3 THE EXHAUSTED IMAGE IS THE LAST COLUMN, AT EVERY b (proved, L4; rule in
   range). At b = 2 the lattice's terminal cells read 2, 96, 384, 324, 972,
   1280, 5120 at the seven filed rows, two readings' shapes each -- the two
   homes -- and at three rows the walker's reading set matched shape by
   shape at budgets 14 and 16. At b >= 3 the fresh world's last column is
   one reading per strand exponent: 768 and 2187 at b = 3, 512 and 1458 at
   b = 4, the walker's reading sets equal as sets at budgets 12 and 14
   (10 and 12) and matched shape by shape, no state without a deep item.
   So "the b >= 3 image carries a factor the b = 2 image does not" is a
   count of handoff cells past s = 1: 2 at b = 3, 1 at b = 4.

F4 THE STOPPED IMAGE IS THE ROW j = 0 AT b = 2 AND THE HANDOFF ROWS AT
   b >= 3, AND THE FILED PRODUCT OVER THE HOMES IS THE ONE-HANDOFF CASE
   (proved, L3 and L5; rule in range over eleven families at b = 2, 0 off
   the filed 3, 8, 15 / 2, 3 / 2, 3 / 2, 3 / 11, 11 and 0 off the walker's
   reading set shape by shape; two widths at b = 3). At b = 3, c = 1 the
   lattice reads 8 at width 1 and 54 at width 2, L5's prediction, and the
   walker reads the same; the eight readings are the deep item alone or
   beside degree 2 flat (the born world), beside the strand at exponent 2
   with degree 4 optional (the tie at T = 3, degree 3 lost to the rule),
   and beside the strand at 4 with degrees 4 and 10 optional (the tie at
   T = 9). The stopped image at b >= 3 is therefore a SUM over strand
   exponents of a product over the degrees tied at the handoff ticks of
   (n_d + 1), each term carrying n_b n_f, and the widths at every other
   degree are still irrelevant; the product over the homes is what this
   reads when the only handoff is the void tie's.

F5 WHAT IS LEFT OPEN. Non-integer b, where the tick is a ceiling and L3's
   criterion carries its slack. m >= 2 discounts, where a degree can hold
   two items. And the handoff ticks' tied degrees as a closed form in
   (b, c): here they are read off the lattice, and derived by hand at
   b = 3, c = 1 only.

THE SLATE, read against the run. PR1, PR2, PR4, PR5, PR6 and PR7 hit as
frozen. PR3 hit after its observable was restated: the slate's "strand
row length" is unbounded at b = 2, where the fresh item IS the deep item
and its row runs forever, so the observable is the set of cells the born
row fires at, which is what L1 derives. Two slips in the engine were found
by the enumeration and not by the hand-attack, and the first is a
derivation error: the strand's first raise is at door 1 ONLY AT TICK 1 --
the fresh world's exponent-1 cell after a born clock is the born world's
flat opening, whose raise costs D_f T -- and the lattice as first written
raised it at door 1 at every tick, reaching a shape (born at 5, strand at
2) the walker never does, at budget 4 at F_2[x]. The second was
bookkeeping: the void tie at the fresh world's root recorded as a handoff.

RUN RECORD. One process, CPython, no BLAS. Wall 8.3 s, peak working set
43.9 MB against the 512 MB ceiling. 5477 checks here; the enumerations are
the identified walker's own reach and the covering walker's, run at every
budget rather than one.
"""

import os

os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")

import sys
from fractions import Fraction

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import explore_greedy_limit as GL
import explore_coarse_type as CT
import explore_price_schedule as PS
import explore_schedule_image as SI
import explore_ladder_stop as LS
import explore_stopped_untie as SU

CHECKS = 0

RING_BUDGET = 8
TOY_BUDGET = 8
LAT_BUDGET = 40      # the lattice is cells, so its horizon is cheap


def ok(cond, msg):
    global CHECKS
    assert cond, msg
    CHECKS += 1


def section(t):
    print("\n" + "=" * 72)
    print(t)
    print("=" * 72)


# ------------------------------------------------------------- the lattice
class Lattice(object):
    """The three-row merge lattice over one supply at one schedule. `c` is
    the covering rule's dial, None for the imported rule alone. `shift`
    moves the born ladder one clock early: the control's wrong lattice."""

    def __init__(self, npl, b=2, alpha=1, born=(1,), c=None, shift=0):
        ok(int(b) == b and b >= 2, "integer b >= 2 only")
        self.npl = npl
        self.b = int(b)
        self.alpha = alpha
        self.born = frozenset(born)
        self.c = None if c is None else Fraction(c)
        self.shift = shift
        self.present = [d for d in range(1, len(npl)) if npl[d]]
        self.sch = PS.Sched("lat b=%d" % self.b, alpha=alpha, b=self.b,
                            born=born)
        bornd = [d for d in self.present if d in self.born]
        self.D_b = bornd[0] if bornd else None
        self.strand_after_handoff = 0
        self.handoffs = set()      # the strand-phase cells s the born row fires at

    def price(self, d, door):
        return d ** self.alpha * door

    def worlds(self):
        """(kind, D) per world the void menu seats."""
        vw = PS.void_winners(self.sch, self.npl, len(self.npl) - 2)
        return sorted(("born" if d in self.born else "fresh", d)
                      for d in vw)

    def tick(self, m):
        return self.b ** m

    def node0(self, kind, D):
        return (kind, D, 0, 0, ())

    def rows(self, node):
        """The candidate rows at a cell: (price, name, successor)."""
        kind, D, s, j, opened = node
        m = max(s - 1, 0) + j
        T = self.tick(m)
        out = []
        D_f = D if kind == "fresh" else None
        if kind == "fresh":
            if s == 0:
                out.append((self.price(D, 1), "strand", (kind, D, 1, j, opened)))
            elif s == 1:
                out.append((self.price(D, T), "strand", (kind, D, 2, j, opened)))
            else:
                door = T - self.tick(s - 2)
                out.append((self.price(D, door), "strand",
                            (kind, D, s + 1, j, opened)))
        if self.D_b is not None:
            if j == 0:
                door = T + 1
            else:
                door = T - self.tick(m - 1 + self.shift) if m - 1 + self.shift >= 0 else T
            out.append((self.price(self.D_b, door), "born",
                        (kind, D, s, j + 1, opened)))
        d = self.next_fresh(node)
        if d is not None:
            out.append((self.price(d, 1), "fresh",
                        (kind, D, s, j, opened + (d,))))
        return out

    def eligible(self, node):
        kind, D, s, j, opened = node
        return [d for d in self.present if d not in self.born
                and not (kind == "fresh" and d == D) and d not in opened]

    def next_fresh(self, node):
        kind, D, s, j, opened = node
        m = max(s - 1, 0) + j
        T = self.tick(m)
        for d in self.eligible(node):
            if self.c is None or d > self.c * T:
                return d
        return None

    def step(self, node):
        rows = self.rows(node)
        best = min(p for p, _, _ in rows)
        out = []
        for p, name, nxt in rows:
            if p == best:
                if name == "strand" and node[2] >= 1 and node[3] >= 1:
                    self.strand_after_handoff += 1
                if name == "born" and node[0] == "fresh" and node[2] >= 1                         and node[3] == 0:
                    self.handoffs.add(node[2])
                out.append(nxt)
        return out

    def shape(self, node):
        kind, D, s, j, opened = node
        m = max(s - 1, 0) + j
        shp = {}
        if j >= 1:
            shp[self.D_b] = (self.tick(m - 1) + 1,)
        if kind == "fresh" and s >= 1:
            shp[D] = (1,) if s == 1 else (self.tick(s - 2) + 1,)
        for d in opened:
            shp[d] = (1,)
        return tuple(sorted(shp.items()))

    def orbit(self, node):
        kind, D, s, j, opened = node
        out = 1
        if j >= 1:
            out *= self.npl[self.D_b]
        if kind == "fresh" and s >= 1:
            out *= self.npl[D]
        for d in opened:
            out *= self.npl[d]
        return out

    def deep(self, node):
        """The item that runs away from this cell, or None: the born item
        once it has moved; the strand where no born row can ever fire."""
        kind, D, s, j, opened = node
        if j >= 1:
            return self.D_b
        if kind == "fresh" and s >= 2:
            if self.D_b is None or D * (self.b - 1) <= self.D_b * self.b:
                return D
        return None

    def terminal(self, node):
        """L3: only the deep item ever moves again."""
        dp = self.deep(node)
        if dp is None:
            return False
        if self.next_fresh(node) is None:
            return True
        return self.c is not None and self.c >= Fraction(dp * (self.b - 1),
                                                          self.b)

    def reading(self, node):
        kind, D, s, j, opened = node
        dp = self.deep(node)
        shp = dict(self.shape(node))
        others = tuple(sorted((d, e) for d, es in shp.items() if d != dp
                              for e in es))
        return (dp, others)

    def strand_exponent(self, node):
        kind, D, s, j, opened = node
        if kind == "fresh" and s >= 2 and j >= 1:
            return self.tick(s - 2) + 1
        return None

    def run(self, nmax):
        """{N: {shape: orbit}} over all worlds, the shared cells counted
        once; the per-N node sets; the terminal readings {reading: orbit}."""
        per_n = {0: set(self.node0(k, D) for k, D in self.worlds())}
        for N in range(nmax):
            nxt = set()
            for node in per_n[N]:
                nxt.update(self.step(node))
            per_n[N + 1] = nxt
        by_shape = {}
        readings = {}
        for N, nodes in per_n.items():
            by_shape[N] = {}
            for node in nodes:
                shp = self.shape(node)
                orb = self.orbit(node)
                if shp in by_shape[N]:
                    ok(by_shape[N][shp] == orb,
                       "a shared cell with two orbit sizes at N = %d" % N)
                by_shape[N][shp] = orb
                if self.terminal(node):
                    rd = self.reading(node)
                    if rd in readings:
                        ok(readings[rd] == orb,
                           "one reading with two orbit sizes: %s" % (rd,))
                    readings[rd] = orb
        return by_shape, per_n, readings


# ------------------------------------------------------- the enumeration
def enumerated(npl, sch, tag, nmax, stop=None, dcap=SI.DCAP):
    """{N: {shape: configurations}} and the states, from the identified
    walker -- the imported reach, or the covering walker under a rule."""
    out, states = {}, {}
    for N in range(nmax + 1):
        if stop is None:
            st = SI.reach(npl, sch, tag, N, dcap=dcap)
        else:
            st = LS.creach(npl, sch, tag, N, dcap)
        states[N] = st
        out[N] = dict((shp, len(c)) for shp, c in SI.by_shape(st).items())
    return out, states


def walker_readings(states):
    """{shape: distinct readings} at one budget, the shape as
    explore_stopped_untie.py reads it; states with no deep item counted."""
    out, nodeep = {}, 0
    for s in states:
        shp = SU.shape_of(s)
        if shp is None:
            nodeep += 1
            continue
        out.setdefault(shp, set()).add(s.reading())
    return dict((k, len(v)) for k, v in out.items()), nodeep


def match_readings(lat_readings, walk_readings, tag):
    """Shape by shape: every lattice reading is a walker shape with the
    same multiplicity and nothing is left over either way."""
    a = dict(lat_readings)
    b = dict(walk_readings)
    only_a = sorted(set(a) - set(b))
    only_b = sorted(set(b) - set(a))
    ok(not only_a and not only_b,
       "%s: readings only in the lattice %s, only in the walker %s"
       % (tag, only_a[:3], only_b[:3]))
    for k in a:
        ok(a[k] == b[k], "%s: reading %s has orbit %d against %d walker "
           "readings" % (tag, k, a[k], b[k]))
    return sum(a.values()), sum(b.values())


# --------------------------------------------------------------- sections
def s0_control(rows):
    print("  the lattice on a born ladder one clock move early, against the")
    print("  enumeration: it must part somewhere on every row")
    print("  supply     b   first budget where the wrong lattice parts")
    for name, npl, b, budget in rows:
        lat = Lattice(npl, b=b, shift=1)
        der, _, _ = lat.run(budget)
        enu, _ = enumerated(npl, PS.Sched("b=%d" % b, b=b), name, budget)
        first = next((N for N in range(budget + 1)
                      if set(der[N]) != set(enu[N])), None)
        print("  %-10s %-3d %s" % (name, b, first if first is not None
                                   else "NEVER"))
        ok(first is not None, "%s/b=%d: the wrong ladder agrees everywhere"
           % (name, b))
    # the doctored reading table
    tab = {(1, ((2, 1),)): 4, (2, ()): 2}
    bad = dict(tab)
    bad[(1, ((2, 1),))] = 5
    fired = False
    try:
        match_readings(tab, bad, "doctored")
    except AssertionError:
        fired = True
    print("  a reading table with one multiplicity moved: %s"
          % ("rejected" if fired else "ACCEPTED"))
    ok(fired, "the shape-by-shape checker accepted a doctored table")


def s1_shapes(rows, recalled):
    print("  per (supply, b), per budget: shapes derived / enumerated, the")
    print("  symmetric difference, and |Im(N)| derived / enumerated")
    print("  supply     b   N   shapes d/e  off   |Im| d      |Im| e    "
          "  recalled")
    for name, npl, b, budget in rows:
        lat = Lattice(npl, b=b)
        der, _, _ = lat.run(budget)
        enu, _ = enumerated(npl, PS.Sched("b=%d" % b, b=b), name, budget)
        for N in range(budget + 1):
            a, bb = set(der[N]), set(enu[N])
            off = len(a ^ bb)
            sd = sum(der[N].values())
            se = sum(enu[N].values())
            r = recalled.get((name, b, N))
            print("  %-10s %-3d %-3d %d/%-9d %-5d %-11d %-11d %s"
                  % (name, b, N, len(a), len(bb), off, sd, se,
                     r if r is not None else ""))
            ok(off == 0, "%s/b=%d: %d shapes off at N = %d: lattice-only "
               "%s, walker-only %s" % (name, b, off, N, sorted(a - bb)[:2],
                                       sorted(bb - a)[:2]))
            ok(sd == se, "%s/b=%d: |Im(%d)| %d against %d"
               % (name, b, N, sd, se))
            for shp in a:
                ok(der[N][shp] == enu[N][shp],
                   "%s/b=%d: shape %s orbit %d against %d at N = %d"
                   % (name, b, shp, der[N][shp], enu[N][shp], N))
            if r is not None:
                ok(sd == r, "%s/b=%d: |Im(%d)| %d against the recalled %d"
                   % (name, b, N, sd, r))


def s2_strand(rows, want_hand, recalled_pairs):
    print("  supply     b   handoff cells  strand exps  fired after"
          "  pairs L1/walk   supply product")
    for name, npl, b, budget in rows:
        lat = Lattice(npl, b=b)
        _, per_n, _ = lat.run(LAT_BUDGET)
        exps = set()
        for N, nodes in per_n.items():
            for node in nodes:
                e = lat.strand_exponent(node)
                if e is not None:
                    exps.add(e)
        hand = sorted(lat.handoffs)
        # the walker's pairs at the budget
        states = SI.reach(npl, PS.Sched("b=%d" % b, b=b), name, budget)
        pairs = set()
        for st in states:
            for x in st.strands():
                pairs.add((x, st.deep()))
        prod = 0 if b == 2 else npl[2] * npl[1]
        latp = 0 if b == 2 else npl[2] * npl[1]
        print("  %-10s %-3d %-14s %-12s %-12d %-3d/%-11d %d"
              % (name, b, hand, sorted(exps) or "-",
                 lat.strand_after_handoff, latp, len(pairs), prod))
        ok(hand == want_hand[b], "%s/b=%d: handoff cells %s against L1's "
           "%s" % (name, b, hand, want_hand[b]))
        ok(sorted(exps) == [lat.tick(x - 2) + 1 for x in hand if x >= 2],
           "%s/b=%d: strand exponents %s off the handoff cells %s"
           % (name, b, sorted(exps), hand))
        ok(lat.strand_after_handoff == 0,
           "%s/b=%d: the strand row fired %d times after a handoff"
           % (name, b, lat.strand_after_handoff))
        ok(len(pairs) == prod, "%s/b=%d: %d pairs against %d"
           % (name, b, len(pairs), prod))
        r = recalled_pairs.get((name, b))
        if r is not None:
            ok(len(pairs) == r, "%s/b=%d: %d pairs against the recalled %d"
               % (name, b, len(pairs), r))


def limit_count(lat, budget, tag):
    by_shape, per_n, readings = lat.run(budget)
    front = per_n[budget]
    bad = [n for n in front if not lat.terminal(n)]
    ok(not bad, "%s: %d of %d frontier cells at budget %d are not terminal, "
       "e.g. %s" % (tag, len(bad), len(front), budget, bad[:2]))
    return readings


def s3_exhausted_b2(grid, walk_rows):
    print("  width  top  lattice readings  filed   walker readings  shapes"
          "  walker no-deep")
    for n, hi, filed in grid:
        npl = LS.flat_supply(n, hi)
        lat = Lattice(npl, b=2)
        rd = limit_count(lat, LAT_BUDGET, "n=%d,D=%d" % (n, hi))
        got = sum(rd.values())
        wr = "-"
        if (n, hi) in walk_rows:
            bud = walk_rows[(n, hi)]
            states = SI.reach(npl, PS.Sched("corner"), "n=%d,D=%d" % (n, hi),
                              bud)
            wrd, nodeep = walker_readings(states)
            a, w = match_readings(rd, wrd, "n=%d,D=%d" % (n, hi))
            ok(nodeep == 0, "n=%d,D=%d: %d walker states with no deep item"
               % (n, hi, nodeep))
            wr = "%d at budget %d" % (w, bud)
        print("  %-6d %-4d %-17d %-7d %-16s %-7d %s"
              % (n, hi, got, filed, wr, len(rd), "-" if wr == "-" else 0))
        ok(got == filed, "n=%d,D=%d: %d against the filed %d"
           % (n, hi, got, filed))


def s4_exhausted_b3(rows):
    print("  supply     b   lattice readings  predicted  walker at two "
          "budgets  same set  no-deep")
    for name, npl, b, want, buds in rows:
        lat = Lattice(npl, b=b)
        rd = limit_count(lat, LAT_BUDGET, "%s/b=%d" % (name, b))
        got = sum(rd.values())
        sets, counts, nodeeps = [], [], []
        for bud in buds:
            states = SI.reach(npl, PS.Sched("b=%d" % b, b=b), name, bud)
            sets.append(set(s.reading() for s in states))
            wrd, nodeep = walker_readings(states)
            counts.append(sum(wrd.values()))
            nodeeps.append(nodeep)
            match_readings(rd, wrd, "%s/b=%d at %d" % (name, b, bud))
        same = sets[0] == sets[1]
        print("  %-10s %-3d %-17d %-10d %-22s %-9s %s"
              % (name, b, got, want, "%d, %d" % tuple(counts),
                 "yes" if same else "NO", max(nodeeps)))
        ok(got == want, "%s/b=%d: %d against the predicted %d"
           % (name, b, got, want))
        ok(same, "%s/b=%d: the reading set moved between budgets %s"
           % (name, b, buds))
        ok(max(nodeeps) == 0, "%s/b=%d: walker states with no deep item"
           % (name, b))


def stop_row(name, npl, b, alpha, born, c, filed, bud, want=None):
    lat = Lattice(npl, b=b, alpha=alpha, born=born, c=c)
    rd = limit_count(lat, LAT_BUDGET, name)
    got = sum(rd.values())
    sch = LS.CSched(name, rule="tick", c=c, b=b, alpha=alpha, born=born)
    states = LS.creach(npl, sch, name, bud, SU.CAP)
    wrd, nodeep = walker_readings(states)
    match_readings(rd, wrd, name)
    ok(nodeep == 0, "%s: %d walker states with no deep item" % (name, nodeep))
    return got, rd, sum(wrd.values())


def s5_stopped_b2(fams):
    print("  family              lattice readings  filed  walker  shapes")
    for name, npl, alpha, born, c, filed in fams:
        got, rd, w = stop_row(name, npl, 2, alpha, born, c, filed,
                              SU.BUDGETS[-1])
        print("  %-19s %-17d %-6d %-7d %d" % (name, got, filed, w, len(rd)))
        ok(got == filed, "%s: %d against the filed %d" % (name, got, filed))


def s6_stopped_b3(rows):
    print("  the born row fires at three ticks and the fresh row is")
    print("  truncated at each; every terminal reading listed")
    for name, npl, want, bud in rows:
        got, rd, w = stop_row(name, npl, 3, 1, (1,), 1, None, bud)
        print("  %-14s lattice %-5d predicted %-5d walker %d" % (name, got,
                                                                 want, w))
        for (dp, others), orb in sorted(rd.items()):
            print("      deep %d  others %-28s orbit %d" % (dp, others, orb))
        ok(got == want, "%s: %d against the predicted %d" % (name, got, want))


# ------------------------------------------------------------------- main
def main():
    supplies, ring_names = {}, []
    for L in CT.build_ladder():
        _, npl, _, _ = GL.universe(L)
        supplies[L.name] = npl
        ring_names.append(L.name)
    for tag, n, hi in (("toy2", 2, 8), ("toy3", 3, 6)):
        supplies[tag] = LS.flat_supply(n, hi)
    toy_names = ["toy2", "toy3"]

    ring_rows = [(n, supplies[n], 2, RING_BUDGET) for n in ring_names]
    toy_rows = [(n, supplies[n], b, TOY_BUDGET) for n in toy_names
                for b in (2, 3, 4)]
    recalled = {("F_2[x]", 2, 8): 396, ("h2", 2, 8): 672, ("h3", 2, 8): 7920,
                ("h4", 2, 8): 4864, ("h5", 2, 8): 16000, ("g2", 2, 8): 4608}

    section("S0  THE CONTROLS, BEFORE ANY RESULT IS READ")
    s0_control(toy_rows + ring_rows[:2])

    section("S1  THE SHAPES AT EVERY BUDGET, b A DIAL")
    s1_shapes(ring_rows + toy_rows, recalled)

    section("S2  THE THIRD ROW")
    s2_strand(toy_rows, {2: [1], 3: [1, 2, 3], 4: [1, 2]},
              {("toy2", 3): 4, ("toy3", 3): 9, ("toy2", 4): 4,
               ("toy3", 4): 9})

    section("S3  THE EXHAUSTED IMAGE AT b = 2 IS THE LAST COLUMN")
    s3_exhausted_b2([(1, 6, 2), (2, 6, 96), (2, 8, 384), (3, 5, 324),
                     (3, 6, 972), (4, 5, 1280), (4, 6, 5120)],
                    {(1, 6): 16, (2, 6): 16, (3, 5): 14})

    section("S4  THE EXHAUSTED IMAGE AT b >= 3: ONE COLUMN PER STRAND "
            "EXPONENT")
    s4_exhausted_b3([("toy2", supplies["toy2"], 3, 768, (12, 14)),
                     ("toy3", supplies["toy3"], 3, 2187, (10, 12)),
                     ("toy2", supplies["toy2"], 4, 512, (12, 14)),
                     ("toy3", supplies["toy3"], 4, 1458, (10, 12))])

    section("S5  THE STOPPED IMAGE AT b = 2 IS THE ROW j = 0")
    fams = [("tied n=1", SU.supply(1), 1, (1,), 1, 3),
            ("tied n=2", SU.supply(2), 1, (1,), 1, 8),
            ("tied n=3", SU.supply(3), 1, (1,), 1, 15),
            ("gapped n=2", SU.supply(2, absent=(2,)), 1, (1,), 1, 2),
            ("gapped n=3", SU.supply(3, absent=(2,)), 1, (1,), 1, 3),
            ("steep n=2", SU.supply(2), 2, (1,), 1, 2),
            ("steep n=3", SU.supply(3), 2, (1,), 1, 3),
            ("floor n=2", SU.supply(2, absent=(1,)), 1, (2,),
             Fraction(3, 2), 2),
            ("floor n=3", SU.supply(3, absent=(1,)), 1, (2,),
             Fraction(3, 2), 3),
            ("mixed homes", SU.supply(1, over={1: 2, 2: 3}), 1, (1,), 1, 11),
            ("mixed tail 5", SU.supply(5, over={1: 2, 2: 3}), 1, (1,), 1,
             11)]
    s5_stopped_b2(fams)

    section("S6  THE STOPPED IMAGE AT b = 3: THE FRESH ROW TRUNCATED AT "
            "EVERY HANDOFF")
    s6_stopped_b3([("b=3 c=1 n=1", SU.supply(1), 8, 9),
                   ("b=3 c=1 n=2", SU.supply(2), 54, 9)])

    section("SUMMARY")
    print("  %d checks here, %d in the identified walker, %d in the"
          % (CHECKS, SI.CHECKS, PS.CHECKS))
    print("  identity-free one, %d in the stopped-ladder rig." % LS.CHECKS)


if __name__ == "__main__":
    main()
