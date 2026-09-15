"""Is the reader's game at a state-dependent digit set finite-state: does
the image's offset above its cell, in the cell's own grain, take
finitely many values over the confined tree's states as the depth
grows, or does the count rise at every depth, at radix 3 as in base
beta?

THE QUESTION. Below the margin law's L* the reader at a state-dependent
gap set plays a game: its choice among legal digits buys a round or
two at the deep kills (explore_gap_choice.py) and no one-step score of
the present image stands in for the search (explore_gap_centering.py).
The hypothesis under test is that the game is nonetheless FINITE: that
the image's position against its cell -- the coordinate the level walk
rides (explore_covering_lag.py, the floor offset eta, the next round's
coordinate b eta + s - a) -- takes finitely many classes over the
prefixes, so the game is played on a finite graph and a numeration's
delay table is computed, never certified. Addition is the shape the
hypothesis has in mind: an on-line adder carries a bounded carry, its
state a finite set. The count is the print.

THE COORDINATE, derived before the engine. A state at output depth t
is an input prefix pair (u_1, u_2) at depth n = t + c and an output
prefix q whose cell b^(o - t) (q + [-M_-, M_+]) contains the image;
its grain is b^(o - t). The offset is

    eta = (image floor) b^(t - o) - (q - M_-),     omega = (width) b^(t - o),

with 0 <= eta and eta + omega <= w by legality. The product's image
floor is X_1 Y_1 / ((b - 1)^2 b^(2n)) at a positive corner, X_1 =
(b - 1) u_1 - a_-, so eta = X_1 Y_1 / ((b - 1)^2 b^(n + L)) - (q - M_-),
2n - t + o = n + L: the offset carries the low n + L digits of a
product of two n-digit prefixes, its reduced denominator dividing
(b - 1)^2 b^(n + L) and refining with the depth. The sum x + y has
floor (X_1 + Y_1) / ((b - 1) b^n) and eta = (X_1 + Y_1) / ((b - 1) b^L)
- (q - M_-): a denominator FIXED at (b - 1) b^L, so the sum's offsets
number at most (b - 1) b^L w + 1 at every depth -- the adder's finite
state, in this coordinate. The product's count is unbounded along
the corner row, by hand: the fractional part of eta + M_- is
(X_1 Y_1 mod G) / G with G = (b - 1)^2 b^(n + L), whatever q the state
sits in; fix u_2 at a corner prefix whose Y_1 is prime to b (one of
every b consecutive u_2 near the corner) and let u_1 run over the
prefixes whose box meets the excess region, x within
Lambda - Lambda_law of the corner, a constant times b^n consecutive
integers; X_1 Y_1 steps by (b - 1) Y_1, which repeats modulo G only
every b^(n + L) steps, so those prefixes carry as many residues, and
as many offsets, as there are of them. What the argument does not
say is which of them the confined tree REACHES through legal
ancestors; the rig counts the reached states, and the count is the
print. In base beta the same coordinate is an element of Q(beta),
the product of two prefixes in Z[beta] over (beta - 1)^2 beta^(n + L),
compared exactly in the power basis.

THE SLATE, frozen before the engine. Pairs: the 10 state-dependent
radix-3 sets of positive least zone (explore_gap_lattice.py
candidate_sets, tail_verdict, image_only) at x y, x^2 + y and the
divider x/(s + y) at P = 1/2, each at L* - 1 of the generalized law,
30 pairs; and in base beta over {-1, 0, 1} at the golden mean and the
Narayana root, x y and the divider at P = 1, each at L* - 1, 4 pairs
(explore_beta_delay.py's engine, confined). The instrument: the
confined tree enumerated breadth-first by output depth as a SET of
states (u, q), a state reached by several paths counted once, the
adversary's extensions pruned to the excess region as the shipped
readers prune them; at every state eta and omega exact (Fractions at
the radix, rational vectors in the power basis in base beta, the
denominator divided out by a linear solve). Per depth: the states,
the distinct eta, the distinct (eta, omega), the eta absent at the
previous depth, the largest reduced denominator. The control: the sum
x + y at three of the state-dependent sets, the same enumeration.

P-A THE SUM SATURATES [property]. At each control set the count of
    distinct eta never exceeds (b - 1) b^L w + 1 and is equal at the
    last two depths reached, with no new value at the last.
P-B THE PRODUCT'S GRAIN [property]. At x y every reduced denominator
    divides (b - 1)^2 b^(n + L), and the largest denominator rises at
    every depth.
P-C THE COUNT GROWS. At all 30 radix-3 pairs and all 4 base-beta
    pairs the distinct-eta count rises at every depth past the first,
    with new values at every depth. The hypothesis's own reading, the
    alternative: some pair whose count is equal at two consecutive
    depths past the second with no new value.
P-D THE RATIO. Distinct eta over states stays above 1/4 at every depth
    of every product pair (collisions X_1 Y_1 = X_1' Y_1' at one q are
    rare among near-corner integers).

KILLS, frozen as what this rig PRINTS.

K1 THE CONTROLS. The shipped counting reader's round at any of the
   three record pairs differing from 4 -> nothing below is read.
K2 THE STATE LEMMA (the shipped reader's, carried). At any enumerated
   extension, "no legal child" disagreeing with "the image strictly
   contains a zone of the parent".
K3 THE COORDINATE. At any state eta < 0 or eta + omega > w: the grain
   arithmetic disagrees with the engine's legality.
K4 THE FINITE CONTROL. The sum's distinct-eta count above
   (b - 1) b^L w + 1 at any depth -> the coordinate is wrong; the
   sum's count still rising at the last depth reached -> the control
   is UNREACHED and nothing below is read.
K5 THE GRAIN. A product eta whose reduced denominator does not divide
   (b - 1)^2 b^(n + L).
THE READING: per pair, GROWS (the count up at every depth past the
first, new values at every depth) or SATURATES (from some depth on,
the count constant and no new value at every later depth); the number
of pairs of each shape at the radix and in base beta. Every pair GROWS
kills the hypothesis as filed; a SATURATES pair is its card.

POSITIVE CONTROL: K1, then K4's saturation, read before any other line.

FINDINGS (entered post-run; every number below sits in this file's
printed output).

F1 THE CONTROLS HOLD. Rounds 4, 4 and 4 at 36,539, 36,708 and 286,169
   confined nodes; K1 never fired. K2 never fired over the first 5,000
   extensions of every pair, K3 never at any state at the radix or in
   the field, K5 never at any product depth.

F2 THE SUM SATURATES [property, checked]. At all three control sets
   the distinct offsets number 18 at every depth reached (depths 1 to
   3, 235 to 73,924 states), no new value past the first depth, the
   grain's lcm 18 or 9 and the bound 46; K4 never fired. The adder's
   finite state, in this coordinate, at the first depth.

F3 THE COUNT GROWS [rule at the 34 pairs; unbounded along the corner
   row by the derivation above, the reached share its print]. All 30
   radix-3 pairs and all 4 base-beta pairs print
   GROWS: the count up and new values at every depth reached (four
   depths at the radix, seven to nine in base beta). The grain rules
   the count. At x y the lcm of the offsets' denominators is
   (b - 1)^2 b^(n + L) exactly at every depth, 324 to 8748 across
   n = 2..5, and the count fills a rising share of it, 0.04..0.10 at
   n = 2 to 0.38..0.44 at n = 5 (8,403 to 9,532 offsets of 21,871 at
   the eight z_min = 1/2 product pairs; 902 and 938 of 2,917 at n = 4
   at the two z_min = 1 pairs, L = 1). At x^2 + y the count triples
   with the grain from the second depth on, the fill settling at
   0.11..0.15 at the z_min = 1/2 sets (about 123, 350, 1009 offsets at
   n = 2, 3, 4) and at 0.04 at the z_min = 1 sets. At the divider the
   offsets' denominators are no
   grain (the lcm past 10^9 by the second depth) and the count runs
   near the state count, 24,837 of 29,010 states to 40,703 of 47,746
   at n = 6. In base beta: the golden product 4, 9, 24, 52, 130, 325,
   784, 1696, 3495 offsets at depths 1..9 (12 to 49,256 states), the
   Narayana divider 17 to 57,923 at depth 9.

F4 THE RATIO PREDICTION FAILED [observation]. Distinct offsets over
   states at the product pairs run 0.02 to 0.11, below 1/4 at all 10:
   the count is capped by the grain's capacity (b - 1)^2 b^(n + L) w,
   and the states outrun the grain because a redundant digit set
   reaches one integer prefix by many paths and one offset from many
   prefixes; P-D read the wrong denominator, and the fill against the
   grain is the reading.

VERDICT. The reader's game at a state-dependent digit set is not
finite-state in the coordinate the level walk rides: the image's
offset above its cell takes a number of distinct values that rises at
every depth at all 30 radix-3 pairs and all 4 base-beta pairs, on a
grain (b - 1)^2 b^(n + L) that refines with the depth and is filled
to a rising share, where the sum's offsets number 18 at every depth.
The unboundedness is the derivation's, the product of two prefixes
carrying its low digits into the offset, and the count is its print;
an automaton for the game would have to carry the partial product, as
an on-line multiplier does and an adder does not. What is not
excluded is a quotient coarser than the offset that still decides the
game -- the outcome function's classes rather than the offset's --
and that question is a different rig, the round verdict per state.

RUN RECORD: pure Python, Fractions at the radix and rational vectors
in the power basis in base beta; under memwatch, peak commit 184 MB
against the 512 MB default, wall 122 s at the budget 60,000 states
per pair and 12 s per pair. Prints reproduced by:
python prime/code/explore_gap_finite.py [STATE_BUDGET] [WALL_SECONDS]
"""

import os
import sys
import time
from fractions import Fraction as Fr

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import explore_manystream_delay as ms                      # noqa: E402
import explore_gap_lattice as gl                           # noqa: E402
import explore_beta_delay as bd                            # noqa: E402
import explore_gap_choice as gc                            # noqa: E402

FAILS = []
B = 3
LEMMA_CAP = 5_000


def ok(cond, msg):
    if not cond:
        FAILS.append(msg)
        print("  KILL:", msg)


class Sum:
    """x + y: the affine control, its offsets on a fixed grain."""
    name, d, e = "x + y", 2, (0, 0)

    def __init__(self, b, am, ap):
        self.b, self.am, self.ap = b, am, ap
        self.Mm, self.Mp = Fr(am, b - 1), Fr(ap, b - 1)
        self.Mh = max(self.Mm, self.Mp)

    def image(self, us, n):
        b, am, ap = self.b, self.am, self.ap
        N = (b - 1) * b ** n
        X1, X2 = (b - 1) * us[0] - am, (b - 1) * us[0] + ap
        Y1, Y2 = (b - 1) * us[1] - am, (b - 1) * us[1] + ap
        return X1 + Y1, X2 + Y2, N

    def window_range(self, Mm, Mp):
        return -2 * Mm, 2 * Mp

    def law_ok(self, b, rho, wsum, L):
        return Fr(b) ** L * rho * (b - 1) >= 2 * wsum

    def lam(self):
        return 2.0

    def grad_iv(self, box):
        return [(1.0, 1.0), (1.0, 1.0)]


# ------------------------------------------------------- the radix walk

def levels_radix(D, fmap, L, budget, wall, lemma=None):
    """The confined tree at radix B as a set of states per output depth,
    with the offset census at each depth."""
    am, ap = -min(D), max(D)
    o = ms.least_lead(B, am, ap, fmap)
    rd = bd.ConfinedGap(B, D, L - o, fmap, o)
    _, w, _, _ = gl.tail_verdict(B, D)
    b, c = B, L - o
    frontier = {((0,) * rd.d, 0)}
    t, n, total = 0, 0, 1
    rows, prev = [], set()
    t_end = time.time() + wall
    while total < budget and time.time() < t_end:
        t1, n1 = t + 1, max(0, t + 1 + c)
        nxt = set()
        for us, q in frontier:
            for us1 in rd.extend(us, n, n1):
                legal = [p for p in rd.digits if rd.legal(us1, n1, b * q + p, t1)]
                if lemma is not None and lemma[0] < LEMMA_CAP:
                    lemma[0] += 1
                    ok((not legal) == rd.dead_by_zone(us1, n1, q, t),
                       f"K2 state lemma at radix {b} {list(D)} {fmap.name} L={L}: us={us1} n={n1} q={q} t={t}")
                for p in legal:
                    nxt.add((us1, b * q + p))
        if not nxt:
            break
        g = Fr(b) ** (t1 - o)
        etas, pairs, dmax, lcm = set(), set(), 1, 1
        for us1, q1 in nxt:
            lo, hi, S = rd.f.image(us1, n1)
            C1, _, T = rd.cell(q1, t1)
            eta = (Fr(lo, S) - Fr(C1, T)) * g
            om = Fr(hi - lo, S) * g
            if eta < 0 or eta + om > w:
                ok(False, f"K3 coordinate at radix {b} {list(D)} {fmap.name} L={L}: eta={eta} omega={om} w={w}")
            etas.add(eta)
            pairs.add((eta, om))
            dmax = max(dmax, eta.denominator)
            lcm = lcm * eta.denominator // _gcd(lcm, eta.denominator)
        # the grain's capacity: offsets in [0, w) on the lcm's lattice, where the lcm is a grain
        cap = int(lcm * w) + 1 if lcm < 10 ** 9 else None
        rows.append(dict(t=t1, n=n1, states=len(nxt), etas=len(etas), pairs=len(pairs),
                         new=len(etas - prev), dmax=dmax, lcm=lcm if lcm < 10 ** 9 else "large", cap=cap))
        total += len(nxt)
        frontier, prev, t, n = nxt, etas, t1, n1
        if len(rows) >= 2 and rows[-1]['states'] ** 2 > 3 * budget * max(1, rows[-2]['states']):
            break                     # the next depth, projected at this growth, is past the budget
    return dict(o=o, L=L, w=w, rows=rows, total=total)


# -------------------------------------------------------- the beta walk

def solve_field(Bs, den, num):
    """x in Q(beta) with den x = num, as a tuple of Fractions in the
    power basis: Gaussian elimination over the multiplication matrix."""
    D = Bs.D
    cols = [Bs.mul(den, tuple(1 if j == i else 0 for j in range(D))) for i in range(D)]
    A = [[Fr(cols[j][i]) for j in range(D)] + [Fr(num[i])] for i in range(D)]
    for col in range(D):
        piv = next(r for r in range(col, D) if A[r][col] != 0)
        A[col], A[piv] = A[piv], A[col]
        pv = A[col][col]
        A[col] = [x / pv for x in A[col]]
        for r in range(D):
            if r != col and A[r][col] != 0:
                f = A[r][col]
                A[r] = [x - f * y for x, y in zip(A[r], A[col])]
    return tuple(A[i][D] for i in range(D))


def levels_beta(Bs, fmap, L, budget, wall, lemma=None):
    o = bd.least_lead(Bs, fmap)
    rd = bd.BetaReader(Bs, fmap, L - o, o)
    rd.confined = True
    M = (rd.aone, Bs.bm1)
    w = (Bs.scale(2, M[0]), M[1])
    c = L - o
    frontier = {((Bs.zero,) * rd.d, Bs.zero)}
    t, n, total = 0, 0, 1
    rows, prev = [], set()
    t_end = time.time() + wall
    while total < budget and time.time() < t_end:
        t1, n1 = t + 1, max(0, t + 1 + c)
        nxt = set()
        for us, q in frontier:
            for us1 in rd.extend(us, n, n1):
                legal = [p for p in rd.digits if rd.legal(us1, n1, rd.child(q, p), t1)]
                if lemma is not None and lemma[0] < LEMMA_CAP:
                    lemma[0] += 1
                    ok((not legal) == rd.dead_by_zone(us1, n1, q, t),
                       f"K2 state lemma at {Bs.name} {fmap.name} L={L}: n={n1} t={t}")
                for p in legal:
                    nxt.add((us1, rd.child(q, p)))
        if not nxt:
            break
        k = t1 - o
        etas, pairs = set(), set()
        for us1, q1 in nxt:
            (lo, dl), (hi, dh) = rd.image(us1, n1)
            (C1, dc), _ = rd.cell(q1, t1)
            num = Bs.sub(Bs.mul(lo, dc), Bs.mul(C1, dl))
            den = Bs.mul(dl, dc)
            wn = Bs.sub(Bs.mul(hi, dl), Bs.mul(lo, dh))
            wd = Bs.mul(dh, dl)
            if k >= 0:
                num, wn = Bs.mul(num, Bs.power(k)), Bs.mul(wn, Bs.power(k))
            else:
                den, wd = Bs.mul(den, Bs.power(-k)), Bs.mul(wd, Bs.power(-k))
            eta = solve_field(Bs, den, num)
            om = solve_field(Bs, wd, wn)
            # K3 in the field: eta >= 0 and eta + omega <= w, signs decided exactly
            lcm_e = 1
            for x in eta + om:
                lcm_e = lcm_e * x.denominator // _gcd(lcm_e, x.denominator)
            ei = tuple(int(x * lcm_e) for x in eta)
            si = tuple(int((x + y) * lcm_e) for x, y in zip(eta, om))
            wi = Bs.mul(w[0], Bs.scale(lcm_e, Bs.one))
            if Bs.sign(ei) < 0 or Bs.sign(Bs.sub(Bs.mul(si, w[1]), wi)) > 0:
                ok(False, f"K3 coordinate at {Bs.name} {fmap.name} L={L}: eta={eta} omega={om}")
            etas.add(eta)
            pairs.add((eta, om))
        rows.append(dict(t=t1, n=n1, states=len(nxt), etas=len(etas), pairs=len(pairs),
                         new=len(etas - prev), dmax=None))
        total += len(nxt)
        frontier, prev, t, n = nxt, etas, t1, n1
        if len(rows) >= 2 and rows[-1]['states'] ** 2 > 3 * budget * max(1, rows[-2]['states']):
            break
    return dict(o=o, L=L, rows=rows, total=total)


def _gcd(a, b):
    while b:
        a, b = b, a % b
    return a


# -------------------------------------------------------------- reading

def shape(rows):
    """GROWS (the count up and new values at every depth past the
    first), SATURATES (from some depth on, the count constant and no
    new value at every later depth), SHORT (fewer than three depths
    reached), else NEITHER."""
    if len(rows) < 3:
        return "SHORT"
    up = [rows[i]['etas'] > rows[i - 1]['etas'] and rows[i]['new'] > 0 for i in range(1, len(rows))]
    flat = [rows[i]['etas'] == rows[i - 1]['etas'] and rows[i]['new'] == 0 for i in range(1, len(rows))]
    if all(up):
        return "GROWS"
    if flat[-1] and all(flat[flat.index(True):]):
        return "SATURATES"
    return "NEITHER"


def show(label, res):
    print(f"  {label} L={res['L']} o={res['o']}: {res['total']} states over {len(res['rows'])} depths -> {shape(res['rows'])}")
    for r in res['rows']:
        dm = ""
        if r['dmax'] is not None:
            dm = f" grain lcm {r['lcm']}" + (f", fill {r['etas'] / r['cap']:.2f} of {r['cap']}" if r['cap'] else "")
        print(f"      t={r['t']} n={r['n']}: states {r['states']}, distinct eta {r['etas']}, "
              f"distinct (eta, omega) {r['pairs']}, new eta {r['new']}{dm}")


def main():
    budget = int(sys.argv[1]) if len(sys.argv) > 1 else 60_000
    wall = float(sys.argv[2]) if len(sys.argv) > 2 else 12.0
    t0 = time.time()
    print(f"THE FINITE-STATE COUNT: radix {B} and base beta, budget {budget} states per pair, wall {wall:.0f}s")

    print("\n=== K1 THE CONTROLS (the record's rounds, all 4)")
    controls = [((-3, -1, 0, 1, 2), 0, 2), ((-3, -2, -1, 0, 2), 2, 3), ((-2, 0, 1, 2, 3), 2, 3)]
    for D, mi, L in controls:
        fmap = gc.maps(D)[mi]
        res = gc.run_pair(D, fmap, L, 3_000_000, 120.0)
        print(f"  {list(D)} {fmap.name}: {gc.fmt(res)}")
        ok(res['r'] == 4, f"K1 {list(D)} {fmap.name} L={L}: round {res['r']} against the record's 4")
    if FAILS:
        print("\nCONTROL FAILED; nothing below is read.")
        return

    sets = [D for D in gl.candidate_sets(B)
            if gl.tail_verdict(B, D)[0] and gl.tail_verdict(B, D)[3] > 0 and not gl.image_only(B, D)]
    print(f"\n  state-dependent sets of positive least zone: {len(sets)}")
    checks = 0

    print("\n=== K4 THE FINITE CONTROL: x + y at three state-dependent sets, the bound (b - 1) b^L w + 1")
    reached = True
    for D in sets[:3]:
        am, ap = -min(D), max(D)
        fmap = Sum(B, am, ap)
        Lg = gl.law_gen(B, D, fmap)
        lemma = [0]
        res = levels_radix(D, fmap, Lg - 1, budget, wall, lemma)
        checks += lemma[0]
        bound = (B - 1) * B ** (Lg - 1) * res['w'] + 1
        show(f"{list(D)} {fmap.name} (L*={Lg}, bound {bound})", res)
        rows = res['rows']
        ok(all(r['etas'] <= bound for r in rows),
           f"K4 {list(D)} x + y: a distinct-eta count above the bound {bound}")
        if len(rows) < 2 or rows[-1]['etas'] != rows[-2]['etas'] or rows[-1]['new'] != 0:
            print(f"      UNREACHED: the sum's count still rising at the last depth")
            reached = False
    if FAILS or not reached:
        print("\nCONTROL FAILED OR UNREACHED; nothing below is read.")
        return

    print("\n=== THE 30 PAIRS at L* - 1, confined: the offset census by depth")
    results = []
    for D in sets:
        _, w, gmax, zmin = gl.tail_verdict(B, D)
        for fmap in gc.maps(D):
            Lg = gl.law_gen(B, D, fmap)
            lemma = [0]
            res = levels_radix(D, fmap, Lg - 1, budget, wall, lemma)
            checks += lemma[0]
            label = f"{list(D)} {fmap.name} [z_min={zmin}, g_max={gmax}] L*={Lg}"
            show(label, res)
            if fmap.name == "x y":
                for r in res['rows']:
                    grain = (B - 1) ** 2 * B ** (r['n'] + Lg - 1)
                    ok(grain % r['dmax'] == 0,
                       f"K5 {list(D)} x y t={r['t']}: denominator {r['dmax']} outside (b-1)^2 b^(n+L) = {grain}")
            results.append((label, fmap.name, res))

    print("\n=== BASE BETA at L* - 1, confined: the offset census by depth")
    beta_results = []
    for Bs in bd.bases():
        for fmap in (bd.BProduct(Bs), bd.BDivision(Bs, 1, 1)):
            Lg, _, _ = bd.law_L(Bs, fmap)
            lemma = [0]
            res = levels_beta(Bs, fmap, Lg - 1, budget, wall, lemma)
            checks += lemma[0]
            label = f"{Bs.name} {fmap.name} L*={Lg}"
            show(label, res)
            beta_results.append((label, res))
    ok(not bd.FAILURES, f"the beta engine's own kills fired {len(bd.FAILURES)} time(s)")

    print("\n=== THE READING")
    for name, group in (("radix 3", results), ("base beta", beta_results)):
        shapes = {}
        for row in group:
            s = shape(row[-1]['rows'])
            shapes[s] = shapes.get(s, 0) + 1
        print(f"  {name}: {len(group)} pairs; shapes {dict(sorted(shapes.items()))}")
        for row in group:
            s = shape(row[-1]['rows'])
            if s != "GROWS":
                rows = row[-1]['rows']
                print(f"    {s}: {row[0]}: counts {[r['etas'] for r in rows]}, new {[r['new'] for r in rows]}")
    ratios = [(lb, min(r['etas'] / r['states'] for r in res['rows']))
              for lb, nm, res in results if nm == "x y" and res['rows']]
    low = [(lb, f"{v:.2f}") for lb, v in ratios if v < 0.25]
    print(f"  P-D the least eta/states ratio over the product pairs: {min(v for _, v in ratios):.2f}; "
          f"below 1/4 at {len(low)} of {len(ratios)}: {low}")
    print(f"  K2 lemma checks: {checks} over {3 + len(results) + len(beta_results)} pairs, at most {LEMMA_CAP} each")

    print(f"\nwall {time.time() - t0:.0f}s; {'ALL KILLS MISSED' if not FAILS else str(len(FAILS)) + ' KILL(S) FIRED'}")
    for f in FAILS:
        print("  ", f)


if __name__ == "__main__":
    main()
