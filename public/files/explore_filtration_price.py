"""explore_filtration_price.py -- WHICH filtration is the schedule's price?
The additive index against the multiplicative one, swept through the laws
the corpus states over OPENINGS.

THE QUESTION. The walker's price at a move of width r on a place of norm N
is N^r -- the additive filtration's index [m^e : m^(e+r)] -- and at a SEATED
place that number is also the multiplicative congruence index
|U_(e+r)|/|U_e| exactly, so the two readings cannot part there. At an
UNSEATED place they part: the multiplicative index is N^(r-1)*(N-1), short
of the price by N/(N-1), because U_0/U_1 is the residue field's k^* of
order N - 1 and not N (explore_door_index.py F4). Over the number rings the
swap was measured: 4 of 9 trajectories move, every divergence a TIE the
norm ordering breaks, so the multiplicative price is LESS separating there
and undercuts nothing. What has never been asked is what the swap does to
the laws the schedule family states over openings -- the void-menu law
(explore_price_schedule.py F3), the two-curve stop law's cheapest-opening
half (explore_tick_pump.py F10), and the greedy image's opening-count and
tie-multiplicity factors (explore_greedy_image_nf.py) -- where every norm
is a power of one q, the function-field side of the same seam.

WHOSE VOCABULARY THE SUSPICION IS IN, asked at the freeze. The suspicion is
written in the LOCAL UNIT GROUP's terms -- two filtrations of one inverse
limit, an index for each -- and not in the schedule family's, whose price
column is the thing under test. The schedule enters only as the machine the
two indices are run through.

THE SETTING. The abstract walker of explore_price_schedule.py: items of
integer degree d with a supply n_d, a global clock T, a door of 1 at a
fresh degree and max(1, T + 1 - e) otherwise, and the corner price
f(d, r) = d * r -- which is log_q of the additive index q^(d*r), the norm
of a degree-d place of a curve over F_q being q^d. This rig prices RAW:

  additive          A(d, r)        = q^(d*r)          every move
  multiplicative    M(d, r)        = q^(d*r) - q^(d*(r-1))   at an OPENING
                                   = q^(d*r)                 at a climb

with every comparison exact -- prices are held as pairs (a, s) standing for
q^a - q^s and compared by a rule proved below, never floated and never
exponentiated, the exponents d*T growing far past what an integer should be
asked to hold.

THE HAND-ATTACK, on paper before any engine code.

 H1 THE LOG WALKER IS THE RAW-ADDITIVE WALKER. q^x is strictly increasing,
    so comparing A(d, r) = q^(d*r) is comparing d * r, ties included, at
    every q. The corner engine is therefore the raw-additive engine
    verbatim, which is the positive control: the new menu machinery must
    reproduce explore_price_schedule.py's menus move by move.
 H2 THE COMPARISON RULE, derived once and used everywhere. For prices
    p_i = q^(a_i) - t_i with t_i either 0 or q^(s_i), s_i < a_i:
      - a_1 = a_2: order by the subtracted term, larger t cheaper; equal
        iff t_1 = t_2.
      - a_1 < a_2: p_1 <= q^(a_1) <= q^(a_2 - 1) and
        p_2 >= q^(a_2) - q^(a_2 - 1) = q^(a_2 - 1) * (q - 1), so p_1 < p_2
        ALWAYS at q >= 3, and at q = 2 with one exception: equality exactly
        when t_1 = 0 and s_2 = a_2 - 1 = a_1. No strict comparison ever
        reverses, at any q.
 H3 WHAT THE SWAP DOES TO TIES, read off H2. An additive tie is a_1 = a_2
    with t_1 = t_2 = 0 in the additive reading. Multiplicatively an opening
    of degree d at width r subtracts t = q^(d*r - d): among tied openings
    the SMALLER degree subtracts more and strictly wins; an opening beats a
    climb of the same a outright. And q^a - q^s determines (a, s) -- the
    base-q digits of the difference sit exactly at s .. a-1 -- so two
    openings of distinct (d, r) NEVER tie multiplicatively, at any q. The
    one collision the multiplicative price has at all is H2's q = 2 case:
    a climb of log-price k - 1 against a DEGREE-1 opening at width k, the
    only way q^a - q^s is itself a power of q.
 H4 THE VOID TIE BREAKS DEEP-WARD, uniformly. The void-menu tie is
    f(d, 2) = f(2d, 1): additively q^(2d) both. Multiplicatively
    M(d, 2) = q^(2d) - q^d < q^(2d) - 1 = M(2d, 1) at every q and every d.
    So the two-branch census at the five rings whose least fresh degree is
    twice the least born-covered one, the attainment of the degree ceiling
    2 * d_min (explore_price_schedule.py PR9), and the b >= 3 strand -- an
    item the void tie seats and the clock then abandons -- all hang on a
    tie only the additive filtration has. If the walks confirm it, the
    celebrated "degree 1 or 2" attractor is a fact about WHICH index the
    price is, which is the sharpest possible answer to the question.
 H5 THE TWO-CURVE HALF IS INSENSITIVE. The stop law's cheapest-opening
    half needs the opening-cost curve to grow without bound against a
    recurrent price. The swap multiplies an opening by (1 - q^(-d)), a
    factor in [1/2, 1) -- less than one log-rung -- so unbounded growth,
    and with it the fate read off "does the walk still open degrees",
    survives the swap; only comparisons with a margin inside one rung can
    flip, and by H2 only at q = 2 into a tie broken toward the opening.
 H6 THE MULTIPLICITY FACTOR IS PRICE-BLIND. The tie multiplicity at an
    opening counts items of ONE degree sharing one menu key (d, r, kind);
    both prices are functions of that key, so the count per opening cannot
    move. What the swap reaches is the BRANCH count -- the shapes the
    image sums over -- via H4, never the per-opening factor.

TRANSPLANT FLAGS, fixed at the freeze.
 T1 From the number rings to the schedule family: NOTHING is carried. The
    measured "every divergence is a tie" is Z's fact, where distinct norms
    collide multiplicatively (2^1 * 1 = 3^0 * 2); over one q the derivation
    above predicts the OPPOSITE sign -- more separating, not less -- and it
    is derived fresh, not transplanted.
 T2 From the ideal world to the element world: nothing. Riders re-price
    nothing here; the element world's rider column is untouched.
 T3 The base q. All six supplies are place counts of curves over F_2, so
    q = 2 is the only ring-faithful base; the q = 3 and q = 5 rows are
    ABSTRACT, certified to be about the schedule family and no curve.

THE INDEX CONVENTION, re-derived from the engine before the freeze. The
walker's door at a seated exponent e is r = max(1, T + 1 - e) and its move
raises e by r; an opening is e = 0. The multiplicative index of that move
is |U_e / U_(e+r)| = q^(d*r) at e >= 1 and q^(d*r) - q^(d*(r-1)) at e = 0,
which is the (a, s) pair the comparison rule holds.

PREDICTIONS, fixed before the engine ran, each naming what the rig PRINTS.
  P1 The raw-additive walker's menu -- the tie dictionary over keys
     (degree, door, kind) -- equals explore_price_schedule.py's exact
     walker's at every state of a 120-move canonical walk over all six
     supplies at q = 2, advanced in lockstep by the exact walker's move.
     0 disagreements.
  P2 The pair comparator agrees with integer arithmetic at every pair of
     representable prices with exponents <= 24, at q = 2, 3, 5; over the
     enumerated opening/climb grid the swap reverses 0 strict comparisons,
     breaks EVERY cross-degree additive opening tie toward the smaller
     degree, and creates new ties only of H3's form (q = 2, a climb one
     rung under a degree-1 opening). 0 exceptions.
  P3 The branched census sweep (4 schedules x 6 supplies x both prices at
     q = 2, plus the multiplicative corner at q = 3 and q = 5): every row's
     census equals its OWN price's void-menu winners; the additive rows
     reproduce the recorded censuses ({1, 2} at F_2[x] and g2, {1} at h5,
     {2} at no-1, {3} at no-1-2, {2, 4} at no-1-3 under born-to-2); the
     multiplicative rows at the three former-tie supplies read the
     SINGLETON deep winner -- {1}, {1}, {2} -- with branch count 1, at
     every q run.
  P4 At b = 3 the additive branched walks reproduce the recorded strands
     (2 of 3 branches stranded at F_2[x], 3 of 4 at g2) and at b = 4
     likewise (1 of 2 at each); the multiplicative walks at those four
     rows read ONE branch and ZERO strands.
  P5 On 150-move corner walks over all six supplies, the count of fresh
     degrees opened in the second half is positive under BOTH prices at
     every row, and one item takes the last three clock moves under both.
  P6 For every degree opened by both prices' canonical walks of one
     supply, the tie multiplicity recorded at its first opening is equal
     across the two prices.

KILL-SHAPES, as observables.
  K1 one S1 menu disagreement: the raw machinery is not the engine, and
     nothing downstream is readable.
  K2 one comparator error against integers, or one order-lemma exception
     outside H3's form: the hand-derivation is wrong.
  K3 a row whose census is not its own price's void winners: the void-menu
     LAW itself dies under the swap -- a stronger finding than predicted,
     not a dead rig.
  K4 the multiplicative rows reproduce the additive censuses, branch
     counts and strands everywhere: the seam is notational and the
     question closes. (This is the sweep's own kill; H4 predicts it
     misses.)

THE SECTIONS.
  S1  positive control: the raw-additive walker against the exact engine.
  S2  the comparator against integers; the order lemma enumerated.
  S3  the branched census sweep under both prices; the void-winners law
      checked per row against its own price.
  S4  the b >= 3 strand under both prices.
  S5  the two-curve half: second-half openings and the deep coordinate.
  S6  the tie multiplicity at first openings, across prices.

FINDINGS (tiers below; run record at the bottom; every section asserts).

F1 THE ORDER LEMMA HOLDS AS DERIVED, AND THE INSTRUMENT STANDS ON IT
   (property for H2 and H3, which are the derivation; rule in range for
   the enumeration: 314928 comparator pairs against integer arithmetic at
   q = 2, 3, 5 with 0 errors, and 720 lockstep menu states over all six
   supplies with 0 disagreements). Over the opening/climb grid the swap
   reverses 0 strict comparisons at any q; all 237 cross-degree additive
   ties break, every opening/opening one toward the SMALLER degree; and
   the 11 new multiplicative ties are all of H3's one form -- q = 2, a
   climb one log-rung under a degree-1 opening -- the only way a
   difference of two q-powers is itself a q-power. So over one base q the
   multiplicative price is strictly MORE separating on openings, the
   exact opposite of the number-ring side, where distinct primes make
   N^(r-1)*(N-1) collide and every measured divergence is a tie CREATED
   (explore_door_index.py F4). One seam, two signs, and the sign is the
   norm image: many primes collide, powers of one q cannot.

F2 THE VOID TIE IS THE ADDITIVE FILTRATION'S, AND EVERYTHING RESTING ON
   IT GOES WITH IT (property for the tie-break -- H4's
   q^(2d) - q^d < q^(2d) - 1 at every q and d -- and a rule in range for
   what falls: 60 sweep rows, 4 schedules x 6 supplies x both prices with
   the multiplicative corner also at q = 3 and 5). Multiplicatively the
   void menu's tie breaks toward the deep branch at every q, so the
   two-branch census at the tie supplies reads the SINGLETON {1} (F_2[x],
   g2) and {2} (the attainment supply), one branch each. What that
   carries away, each measured: the celebrated "degree 1 or 2" attractor
   (the additive rows alone read {1, 2}); the ATTAINMENT of the degree
   ceiling 2 * d_min, whose census {2, 4} is additive-only, so under the
   multiplicative price the ceiling is admissible and never attained; and
   the b >= 3 STRAND -- additive rows reproduce the record (2 of 3
   branches stranded at F_2[x] and 3 of 4 at g2 at b = 3, 1 of 2 at each
   at b = 4) while every multiplicative row reads one branch, zero
   strands, a flat support with no abandoned item at any clock speed run.
   The strand is the fresh branch's fact, and the multiplicative price
   never takes the fresh branch.

F3 THE LAW IS PRICE-COVARIANT AND THE INVARIANT HALF IS EXACTLY THE HALF
   WITH NO TIE IN IT (rule in range; the same 60 rows, plus six 150-move
   corner walks per price). The void-menu LAW survives the swap: at all
   60 rows the census equals its OWN price's void winners, so what the
   swap moves is never the law but the tie clause, which empties -- no
   cross-degree opening tie exists multiplicatively (F1). And the laws
   the hand-attack called insensitive are: fresh degrees open in the
   second half of every walk under both prices (the two-curve stop law's
   cheapest-opening half, the discount being less than one log-rung), one
   item takes the last three clock moves under both (the deep coordinate),
   and the tie multiplicity at every shared first opening is equal across
   the prices at all six supplies (the greedy image's per-opening factor,
   price-blind by construction, H6). So the seam is NOT notational and it
   is also not everywhere: it lives precisely in the laws that consult a
   cross-degree tie, which are the census's branch structure and nothing
   else. Which filtration the corpus means is therefore a real choice
   with a known blast radius: the additive index is the price whose ties
   make the two-branch limits exist.

RUN RECORD. `python explore_filtration_price.py`, under memwatch.py. One
process, CPython, no BLAS. 326132 checks here plus the imported engine's
own per-move checks, 2.0 s wall, peak working set 16.7 MB against the 512
MB ceiling. The walker, its branch driver, the supplies and the strand
reader are imported from explore_price_schedule.py (with
explore_greedy_limit.py and explore_coarse_type.py beneath it), never
reimplemented; only the menu's price column is new. All six FROZEN
predictions hit; no kill-shape fired; K4 -- the sweep's own kill, the
seam notational -- missed at every row it could have fired on.
"""

import os

os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")

import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fractions import Fraction

import explore_coarse_type as CT
import explore_greedy_limit as GL
import explore_price_schedule as PS

CHECKS = 0

CONTROL_N = 120      # lockstep states of the S1 control
GRID_A = 24          # exponent cap of the S2 integer control
BRANCH_N = PS.BRANCH_N     # 10 -- the branched stretch, as recorded
BRANCH_CAP = PS.BRANCH_CAP # 16
SHORT_N = PS.SHORT_N       # 60 -- moves per branch
LONG_N = 150         # moves of the S5 canonical walks


def ok(cond, msg):
    global CHECKS
    assert cond, msg
    CHECKS += 1


def section(t):
    print("\n" + "=" * 72)
    print(t)
    print("=" * 72)


# ------------------------------------------------------- the price objects
class Price(object):
    """q^a - q^s, with s = -1 standing for nothing subtracted. Compared by
    H2's rule, exactly, without ever building the integer."""

    __slots__ = ("q", "a", "s")

    def __init__(self, q, a, s=-1):
        assert a >= 1 and (s == -1 or 0 <= s < a)
        self.q, self.a, self.s = q, a, s

    def value(self):
        """The integer, for the S2 control ONLY -- small exponents."""
        return self.q ** self.a - (0 if self.s == -1 else self.q ** self.s)

    def _cmp(self, o):
        assert self.q == o.q, "prices of two bases compared"
        if self.a == o.a:
            # larger subtracted term = cheaper; s = -1 subtracts least
            t1 = -1 if self.s == -1 else self.s
            t2 = -1 if o.s == -1 else o.s
            if t1 == t2:
                return 0
            # subtracting q^s with bigger s makes the price smaller;
            # s = -1 (nothing) is the biggest price of the a-class
            if t1 == -1:
                return 1
            if t2 == -1:
                return -1
            return -1 if t1 > t2 else 1
        lo, hi = (self, o) if self.a < o.a else (o, self)
        # lo <= q^lo.a <= q^(hi.a - 1) <= hi, equality iff q = 2,
        # lo subtracts nothing, and hi subtracts exactly its top rung
        eq = (self.q == 2 and lo.s == -1 and hi.s == hi.a - 1
              and lo.a == hi.a - 1)
        if eq:
            return 0
        return -1 if self.a < o.a else 1

    def __eq__(self, o):
        return self._cmp(o) == 0

    def __ne__(self, o):
        return self._cmp(o) != 0

    def __lt__(self, o):
        return self._cmp(o) < 0

    def __le__(self, o):
        return self._cmp(o) <= 0

    def __gt__(self, o):
        return self._cmp(o) > 0

    def __ge__(self, o):
        return self._cmp(o) >= 0

    def __repr__(self):
        if self.s == -1:
            return "q^%d" % self.a
        return "q^%d-q^%d" % (self.a, self.s)


class FSched(PS.Sched):
    """The corner schedule carrying a base q and a filtration mode. The
    inherited log price is untouched; the raw prices are new columns."""

    def __init__(self, tag, q, mode, b=2, m=1, born=(1,)):
        PS.Sched.__init__(self, tag, alpha=1, b=b, m=m, born=born)
        self.q = q
        self.mode = mode          # "add" | "mult"

    def rawprice(self, d, r, kind):
        if self.mode == "mult" and kind == "open":
            return Price(self.q, d * r, d * (r - 1) if r > 1 else 0)
        return Price(self.q, d * r)

    def rawlb(self, d):
        """A floor under every move at degree d, for the menu scan: the
        cheapest conceivable is an opening at width 1, q^d - 1."""
        if self.mode == "mult":
            return Price(self.q, d, 0)
        return Price(self.q, d)


class FWalk(PS.Walk):
    """The exact walker with the raw price column. Only the menu is
    overridden; doors, moves, the tick law and its per-move checks are
    inherited untouched."""

    def menu(self):
        best, ties = None, {}
        d = 0
        while True:
            d += 1
            if d > self.dcap:
                self.capped += 1
                break
            if best is not None and self.sch.rawlb(d) > best:
                break
            if self.npl[d] == 0:
                continue
            row = self.seat.get(d, ())
            cands = []
            if self.npl[d] > len(row):
                r = self.door(d, 0, "open")
                cands.append((self.sch.rawprice(d, r, "open"), r, "open",
                              self.npl[d] - len(row)))
            for e in row:
                r = self.door(d, e, "move")
                cands.append((self.sch.rawprice(d, r, "move"), r, "move", 1))
            for cost, r, kind, n in cands:
                if best is not None and cost > best:
                    continue
                if best is None or cost < best:
                    best, ties = cost, {}
                key = (d, r, kind)
                ties[key] = ties.get(key, 0) + n
        ok(best is not None, "%s: an empty menu" % self.tag)
        return best, ties


def void_winners_raw(sch, npl, dcap=200):
    """explore_price_schedule.py's void menu, priced raw: a born-covered
    degree bought at width 2 against the least fresh degree at width 1,
    each kind entering its least degree only (raw prices rise with the
    degree within a kind, checked here rather than assumed)."""
    cb = [d for d in range(1, dcap + 1) if npl[d] and d in sch.born]
    cf = [d for d in range(1, dcap + 1) if npl[d] and d not in sch.born]
    bids = []
    if cb:
        bids.append((sch.rawprice(cb[0], 2, "open"), cb[0]))
    if cf:
        bids.append((sch.rawprice(cf[0], 1, "open"), cf[0]))
    ok(bool(bids), "%s: a supply with no items" % sch.tag)
    for cand, r in ((cb, 2), (cf, 1)):
        for d in cand[1:40]:
            ok(sch.rawprice(d, r, "open") >= sch.rawprice(cand[0], r, "open"),
               "%s: degree %d underbids the least of its kind" % (sch.tag, d))
    best = min(p for p, _ in bids)
    return set(d for p, d in bids if p == best)


def branches_raw(npl, sch, tag, census):
    """explore_price_schedule.py's branched stretch, on the raw walker:
    every distinct state reachable by any tie choice, every edge's clock
    degree entering the census before deduplication."""
    root = FWalk(npl, sch, tag)
    live = {PS.key_of(root): root}
    for _ in range(BRANCH_N):
        nxt = {}
        for s in live.values():
            _, ties = s.menu()
            for key in sorted(ties):
                s2 = s.copy_raw()
                d, kind, Tb, Ta = s2.apply(key)
                if Ta > Tb:
                    census[d] = census.get(d, 0) + 1
                nxt.setdefault(PS.key_of(s2), s2)
        if len(nxt) > BRANCH_CAP:
            nxt = dict(sorted(nxt.items())[:BRANCH_CAP])
        live = nxt
    return [live[k] for k in sorted(live)]


def _copy_raw(self):
    s = FWalk(self.npl, self.sch, self.tag, self.dcap)
    s.seat = dict((d, list(v)) for d, v in self.seat.items())
    s.opens = dict(self.opens)
    s.opened = list(self.opened)
    s.T = self.T
    s.step = self.step
    s.clocks = list(self.clocks)
    s.capped = self.capped
    s.bad_l0 = self.bad_l0
    return s


FWalk.copy_raw = _copy_raw


def continue_raw(s, n, census):
    for _ in range(n):
        _, ties = s.menu()
        d, kind, Tb, Ta = s.apply(sorted(ties)[0])
        if Ta > Tb and census is not None:
            census[d] = census.get(d, 0) + 1
    return s


# ----------------------------------------------------------- the supplies
def supplies_build():
    supplies, ring_names = {}, []
    for L in CT.build_ladder():
        _, npl, _, _ = GL.universe(L)
        supplies[L.name] = npl
        ring_names.append(L.name)
    for cut, tag in ((1, "no-1"), (2, "no-1-2")):
        npl = list(supplies["F_2[x]"])
        for d in range(1, cut + 1):
            npl[d] = 0
        supplies[tag] = npl
    npl = list(supplies["F_2[x]"])
    npl[1] = npl[3] = 0
    supplies["no-1-3"] = npl
    return supplies, ring_names


SWEEP = ["F_2[x]", "h5", "g2", "no-1", "no-1-2", "no-1-3"]


# ------------------------------------------------- S1 the positive control
def s1_control(supplies):
    print("  the raw-additive walker advanced in lockstep by the exact")
    print("  engine's canonical move; menus compared as tie dictionaries")
    total = 0
    for name in SWEEP:
        npl = supplies[name]
        log_s = PS.Walk(npl, PS.Sched("corner"), "S1-log:" + name)
        raw_s = FWalk(npl, FSched("S1-raw:" + name, 2, "add"), "S1r:" + name)
        for _ in range(CONTROL_N):
            _, lt = log_s.menu()
            _, rt = raw_s.menu()
            ok(lt == rt, "%s: menus part at step %d: %s vs %s"
               % (name, log_s.step, sorted(lt), sorted(rt)))
            key = sorted(lt)[0]
            log_s.apply(key)
            raw_s.apply(key)
            total += 1
    print("  %d lockstep states compared over %d supplies, 0 disagreements"
          % (total, len(SWEEP)))
    ok(total == CONTROL_N * len(SWEEP), "control short")


# --------------------------------------- S2 the comparator, the order lemma
def s2_lemma():
    print("  the pair comparator against integer arithmetic, then the")
    print("  order lemma over the opening/climb grid")
    pairs = 0
    for q in (2, 3, 5):
        forms = [Price(q, a, s) for a in range(1, GRID_A + 1)
                 for s in [-1] + list(range(0, a))]
        for p1 in forms:
            for p2 in forms:
                got = p1._cmp(p2)
                v1, v2 = p1.value(), p2.value()
                want = -1 if v1 < v2 else (0 if v1 == v2 else 1)
                ok(got == want, "comparator wrong at q=%d: %r vs %r" %
                   (q, p1, p2))
                pairs += 1
    print("  %d comparator pairs, 0 errors" % pairs)

    # the grid: openings (d, r) with d*r <= 12, climbs of log-price <= 12
    rev = ties_kept = ties_broken = new_ties = bad_new = 0
    for q in (2, 3, 5):
        moves = []
        for d in range(1, 13):
            for r in range(1, 13):
                if d * r <= 12:
                    moves.append((d, r, "open"))
        for a in range(1, 13):
            moves.append((a, 1, "move"))     # a climb of log-price a
        sa = FSched("grid-add", q, "add")
        sm = FSched("grid-mult", q, "mult")
        for i, m1 in enumerate(moves):
            for m2 in moves[i + 1:]:
                d1, r1, k1 = m1
                d2, r2, k2 = m2
                a1 = sa.rawprice(d1, r1, k1)
                a2 = sa.rawprice(d2, r2, k2)
                u1 = sm.rawprice(d1, r1, k1)
                u2 = sm.rawprice(d2, r2, k2)
                ca, cm = a1._cmp(a2), u1._cmp(u2)
                if ca != 0 and cm != 0 and ca != cm:
                    rev += 1
                if ca == 0 and cm == 0:
                    ties_kept += 1
                    ok(k1 == k2 and (k1 == "move" or d1 == d2),
                       "a cross-degree opening tie survives at q=%d: %s %s"
                       % (q, m1, m2))
                if ca == 0 and cm != 0:
                    ties_broken += 1
                    if k1 == "open" and k2 == "open" and d1 != d2:
                        win = m1 if cm < 0 else m2
                        lose = m2 if cm < 0 else m1
                        ok(win[0] < lose[0],
                           "a tie broken AWAY from the smaller degree at "
                           "q=%d: %s beats %s" % (q, win, lose))
                if ca != 0 and cm == 0:
                    new_ties += 1
                    open_m = m1 if k1 == "open" else m2
                    climb_m = m2 if k1 == "open" else m1
                    good = (q == 2 and k1 != k2 and open_m[0] == 1
                            and climb_m[0] * climb_m[1]
                            == open_m[0] * open_m[1] - 1)
                    if not good:
                        bad_new += 1
    ok(rev == 0, "%d strict comparisons reversed" % rev)
    ok(bad_new == 0, "%d new ties outside H3's form" % bad_new)
    print("  reversals 0; additive ties broken %d, kept %d (same-key only);"
          % (ties_broken, ties_kept))
    print("  new multiplicative ties %d, all of H3's q=2 climb/degree-1 form"
          % new_ties)


# ------------------------------------------------- S3 the census sweep
def sweep_row(npl, sch, tag):
    census = {}
    br = branches_raw(npl, sch, tag, census)
    for s in br:
        continue_raw(s, SHORT_N - BRANCH_N, census)
    strands = sum(1 for s in br if PS.stranded(s))
    return set(census), len(br), strands, br


def s3_census(supplies):
    rows = []
    scheds = [("corner", dict(b=2, born=(1,))),
              ("b=3", dict(b=3, born=(1,))),
              ("b=4", dict(b=4, born=(1,))),
              ("born-to-2", dict(b=2, born=(1, 2)))]
    print("  schedule    supply    q  mode  census      void winners  br"
          "  strands")
    for stag, kw in scheds:
        for name in SWEEP:
            npl = supplies[name]
            for q, mode in ((2, "add"), (2, "mult"), (3, "mult"),
                            (5, "mult")):
                if (q, mode) != (2, "add") and (q, mode) != (2, "mult") \
                        and stag != "corner":
                    continue     # the q dial runs at the corner only
                sch = FSched("%s-%s-q%d" % (stag, mode, q), q, mode, **kw)
                cen, nbr, strands, br = sweep_row(npl, sch, sch.tag + name)
                win = void_winners_raw(sch, npl)
                ok(cen == win,
                   "%s %s q=%d %s: census %s is not the void winners %s"
                   % (stag, name, q, mode, sorted(cen), sorted(win)))
                rows.append((stag, name, q, mode, cen, nbr, strands))
                print("  %-10s  %-7s  %d  %-4s  %-10s  %-12s  %d   %d"
                      % (stag, name, q, mode, sorted(cen), sorted(win),
                         nbr, strands))
    return rows


def s3_asserts(rows):
    def row(stag, name, q, mode):
        for r in rows:
            if r[:4] == (stag, name, q, mode):
                return r
        raise AssertionError("row missing: %s" % [stag, name, q, mode])

    # P3: the additive corner reproduces the recorded censuses
    rec = {"F_2[x]": {1, 2}, "g2": {1, 2}, "h5": {1},
           "no-1": {2}, "no-1-2": {3}}
    for name, want in rec.items():
        cen = row("corner", name, 2, "add")[4]
        ok(cen == want, "additive census at %s reads %s, recorded %s"
           % (name, sorted(cen), sorted(want)))
    cen = row("born-to-2", "no-1-3", 2, "add")[4]
    ok(cen == {2, 4}, "additive attainment census reads %s" % sorted(cen))

    # P3: the multiplicative rows at the former ties read the singleton
    for name, want in (("F_2[x]", {1}), ("g2", {1})):
        for q in (2, 3, 5):
            _, _, _, _, cen, nbr, _ = row("corner", name, q, "mult")
            ok(cen == want, "mult census at %s q=%d reads %s"
               % (name, q, sorted(cen)))
            ok(nbr == 1, "mult branch count at %s q=%d is %d"
               % (name, q, nbr))
    _, _, _, _, cen, nbr, _ = row("born-to-2", "no-1-3", 2, "mult")
    ok(cen == {2}, "mult attainment census reads %s" % sorted(cen))
    ok(nbr == 1, "mult attainment branch count %d" % nbr)
    print("  additive rows reproduce the record; multiplicative former-tie")
    print("  rows are singleton, one branch, at every q run")


# --------------------------------------------------- S4 the b >= 3 strand
def s4_strand(rows):
    def row(stag, name, mode):
        for r in rows:
            if r[:4] == (stag, name, 2, mode):
                return r
        raise AssertionError("row missing")

    want_add = {("b=3", "F_2[x]"): (3, 2), ("b=3", "g2"): (4, 3),
                ("b=4", "F_2[x]"): (2, 1), ("b=4", "g2"): (2, 1)}
    for (stag, name), (wb, ws) in sorted(want_add.items()):
        _, _, _, _, _, nbr, strands = row(stag, name, "add")
        ok((nbr, strands) == (wb, ws),
           "additive %s %s reads %d branches %d stranded, recorded %d/%d"
           % (stag, name, nbr, strands, wb, ws))
        _, _, _, _, _, nbr2, strands2 = row(stag, name, "mult")
        ok((nbr2, strands2) == (1, 0),
           "mult %s %s reads %d branches %d stranded" %
           (stag, name, nbr2, strands2))
        print("  %-4s %-7s  additive %d branches / %d stranded -> "
              "multiplicative 1 / 0" % (stag, name, nbr, strands))


# ------------------------------------------- S5 the two-curve half, S6
def s5_s6(supplies):
    print("  150-move corner walks; second-half fresh openings, the deep")
    print("  coordinate, and the first-opening multiplicities")
    for name in SWEEP:
        npl = supplies[name]
        mults = {}
        for mode in ("add", "mult"):
            sch = FSched("long-" + mode, 2, mode)
            s = FWalk(npl, sch, "S5-%s-%s" % (mode, name))
            half_opens = 0
            firsts = {}
            for i in range(LONG_N):
                _, ties = s.menu()
                key = sorted(ties)[0]
                d, r, kind = key
                if kind == "open" and d not in firsts:
                    firsts[d] = ties[key]
                was_opened = len(s.opened)
                s.apply(key)
                if i >= LONG_N // 2 and len(s.opened) > was_opened:
                    half_opens += 1
            ok(half_opens > 0,
               "%s %s: no fresh degree opened in the second half"
               % (name, mode))
            ok(PS.late_clocks(s, 3) == 1,
               "%s %s: the last three clock moves are not one item's"
               % (name, mode))
            mults[mode] = firsts
        shared = sorted(set(mults["add"]) & set(mults["mult"]))
        for d in shared:
            ok(mults["add"][d] == mults["mult"][d],
               "%s: first-opening multiplicity at degree %d parts: %d vs %d"
               % (name, d, mults["add"][d], mults["mult"][d]))
        print("  %-7s  both prices open in the second half; one deep item;"
              % name)
        print("           %d shared opened degrees, multiplicities equal"
              % len(shared))


# ------------------------------------------------------ forced failures
def s0_forced(supplies):
    """Every load-bearing check made to fail once. A failed ok() raises
    before it counts, so the tally needs no repair here."""
    fails = 0
    # the comparator, handed a deliberately wrong expectation
    try:
        ok(Price(2, 3)._cmp(Price(2, 3, 2)) == 0, "forced")
    except AssertionError:
        fails += 1
    # the census law, handed the wrong winners
    npl = supplies["F_2[x]"]
    sch = FSched("forced", 2, "mult")
    try:
        ok(void_winners_raw(sch, npl) == {9}, "forced")
    except AssertionError:
        fails += 1
    assert fails == 2, "a forced failure did not fire"
    print("  2 forced failures fired")


def main():
    supplies, ring_names = supplies_build()

    section("S0  THE HARNESS FORCED TO FAIL")
    s0_forced(supplies)

    section("S1  POSITIVE CONTROL -- THE RAW-ADDITIVE WALKER IS THE ENGINE")
    s1_control(supplies)

    section("S2  THE COMPARATOR AND THE ORDER LEMMA")
    s2_lemma()

    section("S3  THE BRANCHED CENSUS SWEEP UNDER BOTH PRICES")
    rows = s3_census(supplies)
    s3_asserts(rows)

    section("S4  THE b >= 3 STRAND UNDER BOTH PRICES")
    s4_strand(rows)

    section("S5/S6  THE TWO-CURVE HALF AND THE MULTIPLICITY FACTOR")
    s5_s6(supplies)

    section("SUMMARY")
    print("  %d checks passed here (the imported engine's own per-move" %
          CHECKS)
    print("  checks ran besides, uncounted)")


if __name__ == "__main__":
    main()
