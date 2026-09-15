"""Is the covering of the dead arc by the realized offsets in base beta
a property of the shift set alone -- generated past the arc's opening
by the forced recursion from the sub-boxes' floor shifts, no game tree
-- and does the covering set the lag from the opening to the kill?

THE QUESTION. Below the margin law's L* at a contiguous digit set in
base beta the reader's move is forced at every killing box
(explore_delay_choice.py), the dead arc is empty below an ARC-OPENING
DEPTH that is a closed form (explore_arc_opening.py), and the kill
comes 0 to 2 rounds after the opening, never before the depth at which
the realized offsets' largest circle gap G_r drops under the depth's
widest arc and at most one round after it (explore_reachable_offsets.py
F4). That rig read G_r off the whole enumerated game tree. The
conjecture under test says the tree is not needed: past the opening the
offsets are the digit-sum set a forced recursion generates from the
shifts the map's sub-boxes admit, so G_r -- and with it the covering
lag j, the least j at which G at round r_open + j is under the corner
arc g at that round's depth -- is computable from the shift set, and the kill
round is the opening's closed form plus j plus 0 or 1.

THE PAPER DERIVATION, done before the engine. In the coordinate of
explore_reachable_offsets.py a node with parent q at output depth t and
image [lo, hi] at input depth n1 = t + 1 + c has v = lo beta^(t + 1 - o)
- beta q + M, digit d legal iff v - (w - W) <= d <= v. Let eta = v - d
be the image floor's offset above the chosen cell's floor, in [0, w -
W]. The next round's parent is beta q + d and its coordinate is
  v' = lo' beta^(t + 2 - o) - beta (beta q + d) + M
     = beta (v - d) + (lo' - lo) beta^(t + 2 - o) + M - beta M
     = beta eta + s - a,
s = (lo' - lo)/unit' the sub-box's floor shift in the new round's cell
units: THE FORCED RECURSION, exact, with the reader's digit subtracted
before the multiplication (frac(beta frac(x)) is not frac(beta x), so
the offsets are the orbit of a beta-transformation with shifts and not
a plain digit sum). The delta at a node is ceil(v) - v, a function of
the box and the PARENT alone; the reader's digit changes the next
round's offsets, by beta per digit step. Two consequences fix the
predictions. (i) The shift s of a sub-box with digits e of a box near
the corner is grad f(corner) . (e + a) beta^(1 - L*) plus a term of
relative order theta (the box's deficit from the corner, which the
confined region admits up to theta w) plus beta^(-n): for x y at the
corner (M, M), s = M beta^(1 - L*) (e_x + e_y + 2a) to first order,
the exact shift carrying (e_x + a) y_lo + (e_y + a) x_lo with y_lo, x_lo
off M by the deficit. The shift SET -- the corner's (2a + 1)^d linear
values -- is therefore an approximation of relative size theta to the
shifts the sub-boxes admit, and at the plastic x y (theta w = 0.16) it
moves the offsets by about a tenth of a shift quantum per round,
against circle gaps near 0.01. (ii) The free reader's narrow-box
choices (two legal digits where the image is narrower than the zone,
at 28 of 30 pairs) realize offsets the forced recursion does not, each
alternative digit shifting every descendant's offset by beta; the
enumeration's set is the union over the reader's policies and the
forced set is a subset, so G_forced >= G_enum with equality only where
no choice ever exists. The conjecture's letter -- G from the shift set
equal to the enumeration's -- is therefore expected to die twice, on
the reader's choice and on the map's curvature; what survives that is
a weaker statement the same walk decides: whether the kill round is a
LEVEL WALK with one float per box. Under the forced reader the
adversary's search is an existence over boxes, so the forced reader's
death round is the first round at which any confined box's offset is
dead, computable level by level with no minimax; the record says the
highest-digit puppet dies at the free reader's round at 23 of 24
decided pairs and one round earlier at the plastic x^2 + y at a = 1
(explore_delay_choice.py F4). And the covering lag of the forced set
against the closed-form arc, j_B, bounds the forced reader's own lag.

THE SLATE, frozen before the engine. At every one of the 30 beta pairs
of explore_delay_choice.py at L* - 1 the admitted boxes are walked
level by level (explore_beta_delay.py BetaReader.extend confined, the
same set explore_arc_opening.py scans), each box carrying its forced
parent q (the largest legal digit at every round, the exact legality
of the shipped engine), its exact offset eta, and a second offset
eta_A that starts equal to eta at the opening round and evolves by the
recursion with the LINEAR shift set s_lin(sigma, e), the limit of the
corner box's sub-box shifts at depth 40 for the box's corner sigma.
Per round the rig prints the box count, the killable count, the
distinct deltas and their largest circle gap under the exact walk
(G_B) and under the linear shifts (G_A), the dead boxes, the round's
widest arc and the closed form's g(n), beside the enumeration's
extensions, killable count, distinct deltas, G and g_max read from the
print of explore_reachable_offsets.py handed in as a file. The
recursion is checked at every box past the root: v recomputed from the
coordinate against beta eta_prev + s - a with s from the exact image
floors, agreement to 1e-6. THE READING per killed pair: r_open (the
walk's first round with a positive arc, against the closed form), r_kill
(the record's certificate), r_B (the forced reader's death round from
the walk), the lags r_kill - r_open and r_B - r_open, and three covering
lags -- j_enum from the enumeration's G against its own g_max, j_B and
j_A from the walk's G against the closed form's g at the round's own
depth (the opening round is clamped at 1 where the first box is already
past n_open, so the depth is the round's, never n_open + j).

P-A THE CODES. The recursion agrees with the coordinate to 1e-6 at
    every box of every pair; the walk's opening round equals the closed
    form's at every pair it opens; the plastic x y at a = 1 opens at
    10 with g_max 0.0027, 0.0363, 0.0616 and the forced reader dies at
    12.
P-B THE ROUND (TRANSPLANT from explore_delay_choice.py F4). The forced
    reader's death round r_B equals the record's r_kill at every
    decided pair but the plastic x^2 + y at a = 1, where it is 4 against
    5; the walk reaches it at a fraction of the certificate's nodes.
P-C THE SET. G_B exceeds G_enum at some round of every pair with a
    narrow choice (the enumeration's extensions outnumbering the walk's
    boxes there), and equals it at the two pairs without one (silver
    x y and the silver divider at a = 1): the realized set is the
    reader's, not the recursion's.
P-D THE SHIFTS. G_A differs from G_B past the opening at most pairs by
    more than 1e-6: the corner's linear shift set is not the shifts the
    sub-boxes admit.
P-E THE LAG. The forced reader's lag r_B - r_open is j_B or j_B + 1 at
    every killed pair the walk decides, and the free lag is the same
    but at the plastic x^2 + y at a = 1, one more; j_B is at most 2
    everywhere. j_A predicts the lag at fewer pairs than j_B.

KILLS, frozen as what this rig PRINTS.

K1 THE CONTROL. The plastic x y at a = 1 opening at a round other than
   10, its g_max at rounds 10, 11, 12 off 0.0027, 0.0363, 0.0616 by
   more than 0.0005, or the forced reader's death at a round other
   than 12; or the recursion check exceeding 1e-6 at any box of any
   pair -> nothing below is read.
K2 THE ROUND. r_B differing from the record's r_kill at any decided
   pair but the plastic x^2 + y at a = 1, or equal to 5 there -> the
   forced walk is not the highest-digit puppet.
K3 THE SET. |G_B - G_enum| > 5e-5 (the print's four decimals) at any
   round of any pair the enumeration read -> the realized offsets are
   not the forced recursion's (the conjecture's first clause, at the
   letter).
K4 THE SHIFTS. |G_A - G_B| > 1e-6 at any round past the opening ->
   the shift set carries the map's curvature.
K5 THE LAG. A killed pair whose free lag r_kill - r_open is not j_B or
   j_B + 1 -> the covering by the forced set does not set the lag (the
   conjecture's second clause).
THE READING: the per-round table at every pair; the per-pair line
(r_open formula / walk, r_kill, r_B, lag, lag_B, j_enum, j_B, j_A, the
walk's boxes against the certificate's nodes); the counts of pairs at
each (lag, j_B) and at each (lag, j_A).

POSITIVE CONTROL: K1, read before any other line.

FINDINGS (entered post-run; every number below sits in this file's
printed output, the enumeration column read from the print of
explore_reachable_offsets.py rerun the same sitting).

F1 THE CONTROLS HOLD. The plastic x y at a = 1 opens at 10 with g_max
   0.0027, 0.0363, 0.0616 and the forced reader dies at 12 (8 dead
   boxes of 22,680); the recursion matches the coordinate to 2.1e-14
   there and to 2.9e-14 at worst over the 30 pairs; the walk's opening
   equals the closed form's at every pair it opens; K1 never fired.

F2 THE ROUND IS A LEVEL WALK [rule at the 23 decided pairs]. The
   forced reader's death round equals the record's certificate round
   at 22 of 23 decided pairs and is 4 against 5 at the plastic x^2 + y
   at a = 1, the record's puppet round; K2 never fired. Two pairs are
   undecided at the 60 s wall (the Narayana divider at a = 2 walked to
   round 5 of 6, silver x^2 + y at a = 2 to 4 of 5) and the five the
   record's certificate never reached stay unreached. The walk is NOT
   cheaper than the certificate: it visits every confined box to the
   kill depth where the depth-first search stops at the first dead
   subtree, 2.2 to 15 times the certificate's nodes (1,976 boxes
   against 626 at the golden x y, 30,668 against 11,897 at the plastic
   x y, 400 against 27 at tribonacci x y at a = 2); P-B's "fraction"
   was wrong.

F3 THE SET IS THE READER'S AT HALF THE PAIRS [rule at the 30 pairs].
   The walk's boxes equal the enumeration's extensions at every round
   only at the three silver a = 1 pairs, the narrow choice multiplying
   extensions over boxes by up to 23.6 (the plastic x y at a = 2); yet
   G_B equals the enumeration's G at every read round, to the print's
   four decimals, at 14 of the 30 pairs, 11 of them with a choice, and
   exceeds it -- never falls below it -- at some round of the other
   14 (28 rounds, by up to 4.0 times; K3 fired): the choice's offsets
   close a gap at the plastic x y (0.0132 against 0.0106 at round 11,
   0.0048 against 0.0036 at 12), at 10 of the 15 a = 2 pairs and at 4
   of the 15 at a = 1.

F4 THE SHIFT SET CARRIES THE MAP [rule at the 16 pairs read past the
   opening]. The corner's linear shift set misreads G past the opening
   at 14 of the 16 pairs with a round past it (K4 fired at 18 rounds),
   above G_B at 15 rounds and below at 3, by up to 2.9 times (0.1716
   against 0.0589 at silver x y at a = 2, round 2; 0.0342 against
   0.0132 at the plastic x y, round 11); G_A = G_B at the Narayana x y
   and silver x y at a = 1 alone.

F5 THE LAG IS THE FORCED SET'S COVERING PLUS 0 OR 1 [rule at the 23
   decided pairs]. The free lag r_kill - r_open is j_B or j_B + 1 at
   all 23 (K5 never fired): (lag, j_B) = (0, 0) at 7, (1, 0) at 7,
   (1, 1) at 5, (2, 1) at 3, (2, 2) at 1; j_enum equals j_B at every
   pair the enumeration decided, and the walk's own g_max in place of
   the closed form's arc changes no j. The forced reader's own lag is
   j_B or j_B + 1 at all 23 too, one less than the free lag at the
   plastic x^2 + y alone. The linear set's j_A predicts the lag at 16
   of 23: unread at the 7 lag-0 pairs by construction (the linear
   offsets start at the opening) and one round late at 7 of the 12
   lag-1 pairs, exactly those with j_B = 0.

VERDICT. The covering is not the digit set's and not the recursion's
alone: past the opening the offsets a reader realizes are the forced
recursion's plus what its narrow-box choices add, and that addition
moves the largest gap at half the pairs; the shifts are the sub-boxes'
own, carrying the map's curvature, and the corner's linear set
misreads the gap at 14 of 16. The conjecture dies at both clauses'
letter. What stands is the walk: below L* in base beta the kill round
is a LEVEL WALK over the confined boxes carrying one float per box --
the forced offset -- with no game tree and no minimax, equal to the
certificate's round at 22 of 23 decided pairs and one round early at
one, and the lag past the arc's opening is the least j at which that
walk's offsets cover the closed-form arc at the round's own depth,
plus 0 or 1, at every decided pair. The walk costs more nodes than the
certificate and buys a certifier whose every round is an existence
over boxes.

RUN RECORD: pure Python, the shipped engines imported; boxes walked
level by level to the record's kill round, a level capped at
LEVEL_CAP boxes and a pair at WALL seconds; under memwatch, peak
commit 307 MB against the 512 MB default, wall 397 s (a first run
with a 600,000-box cap and the walk three rounds past the opening was
killed by memwatch at 513 MB after 1,166 s). Prints reproduced by:
python prime/code/explore_covering_lag.py [OFFSETS_PRINT_FILE] [LEVEL_CAP] [WALL_SECONDS]
"""

import math
import os
import re
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import explore_beta_delay as bd                            # noqa: E402
import explore_delay_sweep as ds                           # noqa: E402
import explore_arc_opening as ao                           # noqa: E402

FAILS = []
LEVEL_CAP = 300_000
WALL = 60.0
REF_DEPTH = 40
MAX_ROUNDS = 14


def ok(cond, msg):
    if not cond:
        FAILS.append(msg)
        print("  KILL:", msg)


def circle_gap(deltas):
    ds_ = sorted(set(round(x, 12) for x in deltas))
    if len(ds_) >= 2:
        return max(max(b - a_ for a_, b in zip(ds_, ds_[1:])), ds_[0] + 1 - ds_[-1]), len(ds_)
    if len(ds_) == 1:
        return 1.0, 1
    return None, 0


class Walk(bd.BetaReader):
    """The confined boxes walked level by level, each carrying its
    forced parent and its offsets; no minimax, no choice."""

    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)
        self.confined = True
        self.rec_err = 0.0
        self.lin = {}

    def lo_float(self, us, n):
        lo, _ = self.image(us, n)
        return self.B.ffloat(lo)

    def coordinate(self, us1, n1, q, t):
        B = self.B
        lo, hi = self.image(us1, n1)
        unit = B.fl ** (self.o - t - 1)
        d0 = self.digits[0]
        floor0 = B.ffloat(self.cell(self.child(q, d0), t + 1)[0])
        lof, hif = B.ffloat(lo), B.ffloat(hi)
        return (lof - floor0) / unit + d0, (hif - lof) / unit, lof

    def corner_box(self, sigma, n):
        B = self.B
        u = B.zero
        for _ in range(n):
            u = B.add(B.mul(B.beta, u), self.aone)
        return tuple(u if s > 0 else B.neg(u) for s in sigma)

    def linear_shift(self, sigma, e):
        """The limit of the corner box's sub-box shift in the round's
        cell units: (lo(sub-box) - lo(box)) beta^(N + 2 - L*) at N deep."""
        key = (sigma, e)
        if key not in self.lin:
            B = self.B
            N = REF_DEPTH
            u = self.corner_box(sigma, N)
            u1 = tuple(B.add(B.mul(B.beta, x), self.delem[d]) for x, d in zip(u, e))
            lo0, _ = self.image(u, N)
            lo1, _ = self.image(u1, N + 1)
            num = B.sub(B.mul(lo1[0], lo0[1]), B.mul(lo0[0], lo1[1]))
            den = B.mul(lo0[1], lo1[1])
            self.lin[key] = B.ffloat((num, den)) * B.fl ** (N + 2 - (self.c + self.o + 1))
        return self.lin[key]

    def sigma_of(self, us, n):
        return tuple(1 if self.B.tofloat(u) >= 0 else -1 for u in us)

    def step_digits(self, us, us1):
        B = self.B
        return tuple(B.sub(u1, B.mul(B.beta, u))[0] for u, u1 in zip(us, us1))

    def walk(self, r_stop, cap, wall, stop_dead=False):
        """Rounds 1..r_stop (or until the level cap or the wall, or, with
        stop_dead, the first round with a dead box); per round a dict of
        prints. States: (us, n, q, t, eta, eta_A, lo_f)."""
        t_end = time.time() + wall
        B, w, a = self.B, self.wf, self.a
        level = [((B.zero,) * self.d, 0, B.zero, 0, None, None, None)]
        rounds = []
        r_open = None
        total = 0
        for r in range(1, r_stop + 1):
            nxt = []
            deltas_B, deltas_A = [], []
            gmax, dead, killable = 0.0, 0, 0
            nboxes = 0
            for (us, n, q, t, eta, eta_A, lo_prev) in level:
                n1 = max(0, t + 1 + self.c)
                for us1 in self.extend(us, n, n1):
                    nboxes += 1
                    total += 1
                    if nboxes > cap or time.time() > t_end:
                        return rounds, r_open, r - 1, total
                    v, W, lof = self.coordinate(us1, n1, q, t)
                    g = W - (w - 1)
                    gmax = max(gmax, g)
                    if eta is not None:
                        s = (lof - lo_prev) * B.fl ** (t + 1 - self.o)
                        self.rec_err = max(self.rec_err, abs(v - (B.fl * eta + s - a)))
                    legal = [p for p in self.digits if self.legal(us1, n1, self.child(q, p), t + 1)]
                    top = math.ceil(v - 1e-12)
                    if top <= a:
                        killable += 1
                        deltas_B.append(top - v)
                    if not legal:
                        dead += 1
                    # the linear model rides the same boxes
                    v_A = None
                    if r_open is not None and eta_A is not None:
                        if n1 == n:
                            s_lin = 0.0
                        else:
                            s_lin = self.linear_shift(self.sigma_of(us, n), self.step_digits(us, us1))
                        v_A = B.fl * eta_A + s_lin - a
                        top_A = math.ceil(v_A - 1e-12)
                        if top_A <= a:
                            deltas_A.append(top_A - v_A)
                    if legal:
                        d = max(legal)
                        if v_A is not None:
                            d_A = min(max(math.floor(v_A + 1e-12), -a), a)
                            eta_A1 = v_A - d_A
                        else:
                            eta_A1 = v - d
                        nxt.append((us1, n1, self.child(q, d), t + 1, v - d, eta_A1, lof))
            if gmax > 0 and r_open is None:
                r_open = r
            GB, NB = circle_gap(deltas_B)
            GA, NA = circle_gap(deltas_A) if r_open is not None and r > r_open else (None, 0)
            rounds.append(dict(r=r, n=max(0, r + self.c), boxes=nboxes, killable=killable, NB=NB, GB=GB,
                               NA=NA, GA=GA, gmax=gmax, dead=dead))
            if stop_dead and dead:
                return rounds, r_open, r, total
            level = nxt
            if not level:
                break
        return rounds, r_open, r_stop, total


def read_offsets(path):
    """The enumeration's print: per pair the header (round, covering
    depth, arc-opening depth, certificate nodes) and the depth rows."""
    out = {}
    if not path or not os.path.exists(path):
        return out
    head = re.compile(r"^\s*(\S+) (.+?) a=(\d): round (\S+), covering depth (\S+), arc-opening depth (\S+)")
    cert = re.compile(r"^\s*(\S+) (.+?) a=(\d): L\*=\S+ o=\S+ certificate (?:dead r=(\d+)|UNREACHED \[\d+\]) \((\d+) nodes\)")
    row = re.compile(r"^\s*r=\s*(\d+) ext\s+(\d+) b\s+\S+ killable\s+(\d+) distinct\s+(\d+) G (\S+) G\*N \S+ g_max (\S+)")
    cur = None
    with open(path, encoding="utf-8", errors="replace") as f:
        for line in f:
            m = cert.match(line)
            if m:
                key = (m.group(1), m.group(2), int(m.group(3)))
                out.setdefault(key, {})["cert_nodes"] = int(m.group(5))
                continue
            m = head.match(line)
            if m:
                key = (m.group(1), m.group(2), int(m.group(3)))
                cur = out.setdefault(key, {})
                cur["r_kill"] = None if m.group(4) == "None" else int(m.group(4))
                cur["r_cov"] = None if m.group(5) == "None" else int(m.group(5))
                cur["r_open"] = None if m.group(6) == "None" else int(m.group(6))
                cur["rows"] = {}
                continue
            m = row.match(line)
            if m and cur is not None:
                k = int(m.group(1))
                G = None if m.group(5) == "-" else float(m.group(5))
                cur["rows"][k] = dict(ext=int(m.group(2)), killable=int(m.group(3)), distinct=int(m.group(4)),
                                      G=G, gmax=float(m.group(6)))
    return out


def covering_lag(rounds, key, r_open, gfun, use_scan_g=False):
    """The least j >= 0 with G at round r_open + j under the closed form's
    corner arc g at that round's own depth n(r) (or the round's own
    g_max); None if never within the walk."""
    if r_open is None:
        return None
    for j in range(0, 20):
        r = r_open + j
        row = next((x for x in rounds if x['r'] == r), None)
        if row is None:
            return None
        G = row[key]
        g = row['gmax'] if use_scan_g else gfun(row['n'])
        if G is not None and G < g:
            return j
    return None


def main():
    path = sys.argv[1] if len(sys.argv) > 1 else None
    cap = int(sys.argv[2]) if len(sys.argv) > 2 else LEVEL_CAP
    wall = float(sys.argv[3]) if len(sys.argv) > 3 else WALL
    t0 = time.time()
    enum = read_offsets(path)
    print(f"THE COVERING LAG WITHOUT THE TREE: level cap {cap} boxes, wall {wall:.0f}s per pair; "
          f"enumeration from {path if enum else 'NONE (not handed in)'}: {len(enum)} pairs")

    print("\n=== K1 THE CONTROL: the plastic x y at a = 1 (the record: opens at 10, g_max 0.0027, 0.0363, 0.0616, dies at 12)")
    Bp = [B for B in ds.beta_bases() if B.name.startswith("plastic")][0]
    fm = bd.BProduct(Bp)
    cf = ao.closed_form(Bp, fm, 1)
    wk = Walk(Bp, fm, cf['c'], cf['o'], a=1)
    rounds, r_open, reached, total = wk.walk(12, cap, max(wall, 120.0))
    for x in rounds[-3:]:
        print(f"  round {x['r']:2d} depth {x['n']:2d} boxes {x['boxes']:6d} g_max {x['gmax']:+.4f} dead {x['dead']}")
    ok(r_open == 10, f"K1: the plastic x y opens at round {r_open}, the record's 10")
    got = {x['r']: x['gmax'] for x in rounds}
    for r, want in ((10, 0.0027), (11, 0.0363), (12, 0.0616)):
        ok(r in got and abs(got[r] - want) <= 0.0005, f"K1: g_max at round {r} is {got.get(r)}, the record's {want}")
    r_B = next((x['r'] for x in rounds if x['dead'] > 0), None)
    ok(r_B == 12, f"K1: the forced reader dies at round {r_B}, the record's 12")
    ok(wk.rec_err <= 1e-6, f"K1: the recursion misses the coordinate by {wk.rec_err:.2e}")
    print(f"  recursion check: max |v - (beta eta + s - a)| = {wk.rec_err:.2e} over {total} boxes")
    if FAILS:
        print("\nCONTROL FAILED; nothing below is read.")
        return

    print("\n=== THE 30 BETA PAIRS at L* - 1: the forced walk, the linear shift set, the enumeration\n"
          "    per round: boxes, killable, distinct/G under the exact walk (B) and the linear shifts (A),\n"
          "    dead boxes, the round's widest arc and the closed form's g(n); then the enumeration's\n"
          "    extensions, killable, distinct, G, g_max. COVER marks G under the closed form's arc.")
    table = []
    for B in ds.beta_bases():
        for a in (1, 2):
            for fmap in ds.beta_maps(B, a):
                key = (B.name.split()[0], fmap.name, a)
                label = f"{key[0]} {fmap.name} a={a}"
                cf = ao.closed_form(B, fmap, a)
                en = enum.get(key, {})
                r_kill = en.get("r_kill")
                r_stop = MAX_ROUNDS if r_kill is None else r_kill
                wk = Walk(B, fmap, cf['c'], cf['o'], a=a)
                t1 = time.time()
                rounds, r_open, reached, total = wk.walk(r_stop, cap, wall)
                secs = time.time() - t1
                r_B = next((x['r'] for x in rounds if x['dead'] > 0), None)
                print(f"  {label}: L*={cf['L']} o={cf['o']} c={cf['c']} n_open {cf['n_open']} r_open formula {cf['r_open']} "
                      f"walk {r_open} enum {en.get('r_open')} | r_kill {r_kill} ({en.get('cert_nodes')} certificate nodes) "
                      f"r_B {r_B} | walk {total} boxes to round {reached} {secs:.1f}s, recursion err {wk.rec_err:.1e}")
                ok(wk.rec_err <= 1e-6, f"K1 {label}: the recursion misses the coordinate by {wk.rec_err:.2e}")
                if r_open is not None:
                    ok(r_open == cf['r_open'], f"K1 {label}: walk opening {r_open} against the closed form's {cf['r_open']}")
                rows_e = en.get("rows", {})
                for x in rounds:
                    e = rows_e.get(x['r'])
                    gf = cf['g'](x['n']) if x['n'] >= 1 else float('nan')
                    GB = f"{x['GB']:.4f}" if x['GB'] is not None else "-"
                    GA = f"{x['GA']:.4f}" if x['GA'] is not None else "-"
                    cov = " COVER" if x['GB'] is not None and x['GB'] < gf else ""
                    es = (f" | enum ext {e['ext']:6d} killable {e['killable']:6d} distinct {e['distinct']:6d} "
                          f"G {e['G'] if e['G'] is None else round(e['G'], 4)} g_max {e['gmax']:.4f}") if e else ""
                    print(f"    r={x['r']:2d} n={x['n']:2d} boxes {x['boxes']:6d} killable {x['killable']:6d} "
                          f"B distinct {x['NB']:6d} G {GB} | A distinct {x['NA']:6d} G {GA} | dead {x['dead']:4d} "
                          f"g_max {x['gmax']:+.4f} g(n) {gf:+.4f}{cov}{es}")
                    if e and e['G'] is not None and x['GB'] is not None:
                        ok(abs(x['GB'] - e['G']) <= 5e-5,
                           f"K3 {label} r={x['r']}: G_B {x['GB']:.4f} against the enumeration's {e['G']:.4f}")
                    if x['GA'] is not None and x['GB'] is not None:
                        ok(abs(x['GA'] - x['GB']) <= 1e-6, f"K4 {label} r={x['r']}: G_A {x['GA']:.4f} against G_B {x['GB']:.4f}")
                decided = r_kill is not None and reached >= r_kill
                if decided:
                    if key == ("plastic", "x^2 + y", 1):
                        ok(r_B == 4, f"K2 {label}: forced death at {r_B}, the record's puppet at 4")
                    else:
                        ok(r_B == r_kill, f"K2 {label}: forced death at {r_B} against the record's {r_kill}")
                j_B = covering_lag(rounds, 'GB', r_open, cf['g'])
                j_A = covering_lag(rounds, 'GA', r_open, cf['g'])
                j_Bs = covering_lag(rounds, 'GB', r_open, cf['g'], use_scan_g=True)
                j_e = (en['r_cov'] - en['r_open']) if en.get('r_cov') is not None and en.get('r_open') is not None else None
                lag = r_kill - r_open if (r_kill is not None and r_open is not None) else None
                lag_B = r_B - r_open if (r_B is not None and r_open is not None) else None
                if lag is not None and decided:
                    ok(j_B is not None and lag in (j_B, j_B + 1), f"K5 {label}: lag {lag} against the forced covering lag {j_B}")
                table.append((label, cf, r_open, r_kill, r_B, lag, lag_B, j_e, j_B, j_Bs, j_A, total, en.get('cert_nodes'), decided))

    print("\n=== THE READING per killed pair: the opening, the record's kill, the forced walk's kill, the lags,\n"
          "    the covering lags (j_enum: the enumeration's G under its own g_max; j_B: the walk's G under the\n"
          "    closed form's arc; j_Bs: the walk's G under the walk's g_max; j_A: the linear shifts' G), the cost")
    pairs_lag_jB, pairs_lag_jA = {}, {}
    for (label, cf, r_open, r_kill, r_B, lag, lag_B, j_e, j_B, j_Bs, j_A, total, cn, decided) in sorted(
            table, key=lambda t: (t[5] is None, t[5] or 0, t[1]['phi'])):
        if r_kill is None:
            continue
        print(f"  open {r_open} kill {r_kill} forced {r_B} lag {lag} lag_B {lag_B} | j_enum {j_e} j_B {j_B} j_Bs {j_Bs} j_A {j_A} "
              f"| phi {cf['phi']:.2f} | walk {total} boxes vs {cn} certificate nodes{'' if decided else ' (UNDECIDED)'}  {label}")
        if decided:
            pairs_lag_jB[(lag, j_B)] = pairs_lag_jB.get((lag, j_B), 0) + 1
            pairs_lag_jA[(lag, j_A)] = pairs_lag_jA.get((lag, j_A), 0) + 1
    print(f"  decided pairs by (lag, j_B): {sorted(pairs_lag_jB.items(), key=str)}")
    print(f"  decided pairs by (lag, j_A): {sorted(pairs_lag_jA.items(), key=str)}")
    dec = [t for t in table if t[13]]
    print(f"  forced death = record's kill at {sum(1 for t in dec if t[4] == t[3])} of {len(dec)} decided pairs; "
          f"lag in {{j_B, j_B + 1}} at {sum(1 for t in dec if t[8] is not None and t[5] in (t[8], t[8] + 1))}, "
          f"in {{j_A, j_A + 1}} at {sum(1 for t in dec if t[10] is not None and t[5] in (t[10], t[10] + 1))}, "
          f"in {{j_enum, j_enum + 1}} at {sum(1 for t in dec if t[7] is not None and t[5] in (t[7], t[7] + 1))}")
    print(f"\nwall {time.time() - t0:.0f}s; {'ALL KILLS MISSED' if not FAILS else str(len(FAILS)) + ' KILL(S) FIRED'}")


if __name__ == "__main__":
    main()
