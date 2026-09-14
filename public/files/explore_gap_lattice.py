"""The delay at a digit set with a gap: is the on-line delay of a
non-affine map still the margin law's L* when the digit set is not an
interval of integers, or does the reader gain a strategy there?

THE QUESTION. The many-stream theorem (explore_manystream_delay.py) is
written for a CONTIGUOUS digit set {-a-, ..., a+}: the tails from a
prefix fill an interval, the output cells at a depth are the intervals
[q - M-, q + M+] over the integers q, consecutive cells overlap in a
zone of length W - 1, and the reader is dead iff the image of its input
box strictly contains a zone -- a condition on the streams alone, so
the reader has no strategy and the delay is the least L with
b^L rho >= Lam (a- + a+). Take instead a digit set D with a GAP, such
as {-2, 0, 1, 2} at radix 3 or {-3, -1, 0, 1, 3} at radix 4, the same
set on the input and the output streams. What is its tail set, what
does the cell lemma become, and does the delay follow a margin law?

THE DERIVATION, written before the engine. Let dmin, dmax be D's ends,
m = dmin/(b - 1), M = dmax/(b - 1) the hull [m, M] of the tail set T,
and w = M - m its width. T satisfies T = (D + T)/b, so T is the whole
hull iff the digit images d + [m, M] cover b [m, M], iff every gap
between consecutive digits is at most w; otherwise T is a Cantor set.
THE INTERVAL CASE. Every prefix box is then p + b^-n [m, M]^d, the
image of a box is an interval, and a parent cell's children, in the
child's units, are [bq + d + m, bq + d + M] over d in D, their union
the parent exactly. The image lies inside the parent and fits no child
iff it strictly contains the ZONE between some consecutive pair of
children: the overlap [bq + d' + m, bq + d + M] of length w - g where
g = d' - d is the gap, a single point where g = w. THE LEMMA IS NO
LONGER A PROPERTY OF THE IMAGE: a parent's zones sit at bq plus fixed
offsets, and at a contiguous set the zones inside the parent are
exactly the integer-indexed ones [k + 1 + m, k + M], the same for every
parent holding the image, while at a gap set a zone of parent q shifted
by b need not be a zone of parent q + 1. At radix 3 over {-2, 0, 1, 2}
the image [1.9, 2.1] in depth-2 units fits parent 0's child with digit
2, [1, 3], and strictly contains parent 1's touching point 2: dead
under one parent, alive under the other, so THE READER HAS A STRATEGY
and the delay is the value of a two-player game, the adversary
choosing input digits and the reader its output digit, each seeing the
other's moves. THE MARGIN LAW'S TWO HALVES. Sufficiency survives with
the least zone in the zone's place: at output depth t + 1 the reader
has read t + 1 + c input digits, the image is at most Lam w b^-(t+1+c)
wide and a zone at least z_min b^(o-t-1) with z_min = w - g_max, so

    b^L z_min >= Lam w,   L = c + o,

suffices (at a contiguous set z_min = rho/(b - 1) and w = (a- + a+)/
(b - 1), the theorem's law). Necessity does not survive as written: its
first step, any legal digit as good as any other, is the image-only
lemma. Where g_max = w the generalized law never holds and predicts no
finite delay for any non-affine map; where 0 < z_min the law's L* may
sit one above the contiguous cell's of the same radix and slack
(|D| - b), since w is larger while z_min is not.

THE SLATE, frozen before the engine. Sets: every D within [-3, 3] at
radices 3 and 4 holding 0 and both signs, of at most five digits, with
at least two distinct gaps (a set whose gaps are all equal is an
affine image of a contiguous set, its tails an interval rescaled) and
with the interval tail condition; the two candidate sets named above
among them.
Maps: the product x y and the divider x/(s + y) at P = 1/(b - 1), the
pole specimen with two streams. The instrument is the exhaustive game
tree at lookahead c and lead o (the engine's survives, the reader
choosing among legal digits, the adversary among all input digit
pairs), a death at round r exact and a survival to the tree's depth a
bounded certificate.

P-A THE TAIL CENSUS. Over the sets enumerated: the count with interval
    tails against Cantor tails; {-2, 0, 1, 2} at radix 3 and
    {-3, -1, 0, 1, 3} at radix 4 both interval with z_min = 0 (a
    touching pair); {-3, -1, 0, 1, 3} at radix 3 interval with
    z_min = 1 against the contiguous {-2..2}'s zone 1.
P-B THE STRATEGY WITNESS. Over the representable input prefixes at
    depth 3 and the representable parents whose cell holds the image:
    the count of images with two legal parents of different verdicts is
    positive at every interval gap set for x y (the lemma is not
    image-only), and zero at the contiguous control (3, 2, 2).
P-C THE STATE LEMMA. At every node the tree visits, "no legal child"
    agrees with "the image strictly contains a zone of the parent".
P-D THE GAME AT z_min > 0. TRANSPLANT from the contiguous theorem: the
    tree kills at every L below the generalized L* and survives at L*.
    The derivation's own reading: at some set and map the tree survives
    to its depth one below the generalized L*, the strategy buying a
    digit.
P-E THE GAME AT z_min = 0. TRANSPLANT: dead at every L tested (the
    generalized law never holds). The derivation's own reading: alive
    to the tree's depth at some finite L at some cell, the reader
    steering between the two parents whose touching points are b apart.

KILLS, frozen as what this rig PRINTS.

K1 The contiguous control (3, 2, 2) and (4, 2, 2), x y and the divider:
   the generalized law's L* differing from the engine's law_L, or the
   tree's verdicts (dead at L* - 1, alive at L*) differing from
   explore_manystream_delay.py's record -> nothing below is read.
K2 P-C failing at any node -> the state lemma is wrong.
K3 The tree killing at or above the generalized L* where it is finite
   -> the sufficiency half is wrong.
THE WIDER KILLS: a non-affine map alive to
the tree's depth below the generalized L* (P-D's second reading), or
alive at a finite L where the law's L* is infinite (P-E's second
reading); either prints "the delay is not one margin law across
lattices".

POSITIVE CONTROL: K1's control pairs, read before any other line.

FINDINGS (entered post-run; every number below sits in this file's
printed output at radices 3 and 4).

F1 THE CONTROL HOLDS. At (3, 2, 2) and (4, 2, 2) the generalized law's
   L* equals the engine's law_L, 2 for x y and 3 for the divider; the
   tree kills at L* - 1 (rounds 2 and 3 at radix 3, 2 and 1 at radix 4)
   and survives at L* to its depth; the contiguous witness reads 0
   disagreeing images of 176 and 24. K1 never fired.

F2 THE TAIL CENSUS. Radix 3: 34 sets, 26 with interval tails, 12 of
   them touching (z_min = 0), 8 Cantor; radix 4: 28 sets, 4 interval,
   all touching, 24 Cantor. {-2, 0, 1, 2} at radix 3 is touching and
   state-dependent, {-3, -1, 0, 1, 3} at radix 4 touching and
   image-only, {-3, -1, 0, 1, 3} at radix 3 has z_min = 1 (w = 3,
   slack 2) against the contiguous {-2..2}'s zone 1 at w = 2.

F3 THE READER HAS A STRATEGY [the criterion a property; its census a
   rule at the 30 sets]. Death is image-only at 7 of the 30 interval
   sets ({-3, -2, 0, 1}, {-3, -1, 0, 2}, {-2, 0, 1, 3}, {-1, 0, 2, 3},
   {-3, -2, 0, 1, 3}, {-3, -1, 0, 2, 3} at radix 3 and {-3, -1, 0, 1, 3}
   at radix 4) and state-dependent at 23; a disagreeing image at depth 3
   at 17 of the 23 and at none of the 7 (K4 never fired). The
   criterion quantifies over every parent offset below w, and every
   such offset is realized by two prefixes of one depth at all 30 sets
   (checked at depths 1 to 7 at the audit), so it is the reader's own.
   P-B's "every set" failed: the witness needs a zone of one legal
   parent that contains no zone of the other, and 7 sets have none.

F4 THE GAME AT z_min > 0 [rule at 26 of the 28 pairs; the law's L* alive
   at all 28]. Fourteen sets, x y at L* = 3 (z_min = 1/2) or 2 (z_min =
   1), the divider at 4 or 3. Dead below L* at every pair once deepened:
   26 of 28, the kills at rounds 1 to 4 (x y at {-3, -1, 0, 1, 2}, L = 2,
   dies at round 4 after surviving 3); alive to the tree's depth at
   L* - 1 at two divider pairs, {-3, -2, -1, 0, 2} and {-2, 0, 1, 2, 3},
   3 rounds at 10.6 million nodes each, unreached. Alive at L* at 28 of
   28; K3 never fired. The transplant held wherever the tree reached;
   the derivation's own reading, a digit bought by the strategy, found
   no instance.

F5 THE GAME AT z_min = 0 [observation at L <= 3]. All 32 pairs of the
   16 touching sets dead at every L in 0..3: at round 1 at 29, later at
   three x y pairs ({-3, -2, 0, 1} at round 2, {-3, -1, 0, 1} at rounds
   2, 2, 3, 3, {-1, 0, 1, 3} at 1, 2, 2, 2), the three where the root's
   touching point lies outside the map's range; inside it at the other
   29, where the first digit kills. Past L = 3 the tree's depth falls
   below the kill rounds seen and decides nothing.

VERDICT. At a digit set with a gap and interval tails the delay of x y
and the divider is the margin law's L* with the least zone in the
zone's place, at every pair the tree reaches (26 of 28), although the
reader has a strategy at 23 of the 30 sets and the theorem's necessity
proof -- death a property of the image, the phases along a lattice
line -- does not transfer; at a touching set no specimen reads at any
lookahead tested. The margin law survives the gap sets as a law and
loses its proof there: necessity at a gap set is open.

RUN RECORD: pure Python, integers for every verdict, the many-stream
engine imported for the maps and the tree; under memwatch, peak commit
43.8 MB against the 512 MB default, wall 177 s at radices 3 and 4.
Prints reproduced by:
python prime/code/explore_gap_lattice.py [BMAX]
"""

import itertools
import math
import os
import sys
import time
from fractions import Fraction as Fr

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import explore_manystream_delay as ms                      # noqa: E402

FAILURES = []
TREE_BUDGET = 400_000
DEEP_BUDGET = 10_000_000
WITNESS_DEPTH = 3


def ok(cond, msg):
    if not cond:
        FAILURES.append(msg)
        print("  KILL:", msg)


# --------------------------------------------------------- the digit sets

def tail_verdict(b, D):
    """(interval?, w, g_max, z_min) for the digit set D at radix b."""
    D = sorted(D)
    w = Fr(D[-1] - D[0], b - 1)
    gaps = [D[i + 1] - D[i] for i in range(len(D) - 1)]
    gmax = max(gaps)
    return gmax <= w, w, gmax, w - gmax


def candidate_sets(b, span=3, maxlen=5):
    out = []
    digits = range(-span, span + 1)
    for k in range(b, maxlen + 1):
        for D in itertools.combinations(digits, k):
            if 0 not in D or D[0] >= 0 or D[-1] <= 0:
                continue
            gaps = {D[i + 1] - D[i] for i in range(len(D) - 1)}
            if len(gaps) < 2:
                continue                        # contiguous or its affine image
            out.append(D)
    return out


def law_gen(b, D, fmap):
    """The generalized margin law's L*: least L with b^L z_min >= Lam w,
    exact in the map's own law where z_min > 0 (Lam w is the law's
    right side over (b - 1)); None where z_min = 0."""
    interval, w, gmax, zmin = tail_verdict(b, D)
    if zmin == 0:
        return None
    lam = Fr(fmap.lam()).limit_denominator(10 ** 9)
    L = 0
    while Fr(b) ** L * zmin < lam * w:
        L += 1
    while L > -60 and Fr(b) ** (L - 1) * zmin >= lam * w:
        L -= 1
    return L


def image_only(b, D):
    """Is death a property of the image alone? For parents q and q + k
    whose cells overlap, every zone of one lying inside the overlap must
    contain a zone of the other (an image strictly containing a zone
    strictly contains every zone inside it), in child units."""
    D = sorted(D)
    m, M = Fr(D[0], b - 1), Fr(D[-1], b - 1)
    zones = [(d1 + m, d + M) for d, d1 in zip(D, D[1:])]
    w = M - m
    k = 1
    while k < w:
        lo, hi = b * k + b * m, b * M              # the overlap of cell 0 and cell k
        z0 = [z for z in zones if lo < z[0] and z[1] < hi]
        zk = [(z[0] + b * k, z[1] + b * k) for z in zones]
        zk = [z for z in zk if lo < z[0] and z[1] < hi]
        for fam, other in ((z0, zk), (zk, z0)):
            for z in fam:
                if not any(z[0] <= y[0] and y[1] <= z[1] for y in other):
                    return False
        k += 1
    return True


def root_touch_inside(b, D, fmap, o):
    """Does a touching point of the root cell's children lie strictly
    inside the map's range? Absolute units."""
    D = sorted(D)
    m, M = Fr(D[0], b - 1), Fr(D[-1], b - 1)
    lo, hi = fmap.window_range(Fr(-D[0], b - 1), Fr(D[-1], b - 1))
    for d, d1 in zip(D, D[1:]):
        if d1 - d == M - m:
            pt = (d + M) * Fr(b) ** (o - 1)
            if lo < pt < hi:
                return True
    return False


# --------------------------------------------------------------- the game

class GapReader(ms.ReaderD):
    """The reading game over a digit set D with a gap: the engine's
    tree with D as the digit list on both streams and the state lemma
    checked at every node."""

    def __init__(self, b, D, c, fmap, o):
        D = sorted(D)
        super().__init__(b, -D[0], D[-1], c, fmap, o, None)
        self.digits = list(D)
        self.moves = list(itertools.product(self.digits, repeat=self.d))
        self.pairs = [(D[i], D[i + 1]) for i in range(len(D) - 1)]
        self.nodes = 0
        self.lemma_checked = 0

    def dead_by_zone(self, us, n, q, t):
        """The state lemma: the image strictly contains a zone between
        two consecutive children of q."""
        lo, hi, S = self.f.image(us, n)
        for d, d1 in self.pairs:
            bot = self.cell(self.b * q + d1, t + 1)[0]
            _, top, T = self.cell(self.b * q + d, t + 1)
            if hi * T > top * S and lo * T < bot * S:
                return True
        return False

    def survives(self, us, n, q, t, rounds, confined=False):
        if rounds == 0:
            return True
        n1 = max(0, t + 1 + self.c)
        for mvs in itertools.product(self.moves, repeat=n1 - n):
            us1 = us
            for mv in mvs:
                us1 = tuple(self.b * u + x for u, x in zip(us1, mv))
            self.nodes += 1
            legal = [p for p in self.digits if self.legal(us1, n1, self.b * q + p, t + 1)]
            if self.lemma_checked < 200_000:
                self.lemma_checked += 1
                ok((not legal) == self.dead_by_zone(us1, n1, q, t),
                   f"K2 state lemma at ({self.b},{self.digits}) {self.f.name} c={self.c}: "
                   f"us={us1} n={n1} q={q} t={t}")
            alive = False
            for p in legal:
                if self.survives(us1, n1, self.b * q + p, t + 1, rounds - 1):
                    alive = True
                    break
            if not alive:
                return False
        return True

    def certificate(self, budget, max_rounds=8):
        m = len(self.moves)
        if m ** max(0, 1 + self.c) > budget:
            return None, 0
        depth = max(1, min(max_rounds, int(math.log(budget) / math.log(m)) - self.c))
        root = (0,) * self.d
        for r in range(0, depth + 1):
            if not (self.legal(root, 0, 0, 0) and self.survives(root, 0, 0, 0, r)):
                return r, depth
        return None, depth

    def representable(self, n):
        """The prefix integers at depth n, one coordinate."""
        cur = {0}
        for _ in range(n):
            cur = {self.b * u + d for u in cur for d in self.digits}
        return sorted(cur)

    def witness_count(self, n, t):
        """P-B: images at input depth n with two legal parents at output
        depth t of different verdicts; returns (images, disagreeing)."""
        reps = self.representable(n)
        parents = self.representable(t)
        images = disagree = 0
        for us in itertools.product(reps, repeat=self.d):
            legal_q = [q for q in parents if self.legal(us, n, q, t)]
            if len(legal_q) < 2:
                continue
            images += 1
            verdicts = {self.dead_by_zone(us, n, q, t) for q in legal_q}
            if len(verdicts) == 2:
                disagree += 1
        return images, disagree


def game_delay(b, D, fmap, Ls, label):
    """The tree at each L in Ls; prints one line per L and returns the
    dict L -> (death round or None, depth)."""
    o = ms.least_lead(b, -min(D), max(D), fmap)
    out = {}
    for L in Ls:
        rd = GapReader(b, D, L - o, fmap, o)
        r, depth = rd.certificate(TREE_BUDGET)
        out[L] = (r, depth)
    words = ", ".join(f"L={L}: {'dead r=' + str(r) if r is not None else 'alive'} [{d}]"
                      for L, (r, d) in out.items())
    print(f"  {label} o={o}: {words}")
    return o, out


# ------------------------------------------------------------------ runs

def control():
    print("\n=== K1 THE CONTROL: contiguous cells against the engine's own law and record")
    for b, am, ap in ((3, 2, 2), (4, 2, 2)):
        D = tuple(range(-am, ap + 1))
        for fmap in (ms.Product(b, am, ap), ms.Division(b, am, ap, Fr(1, b - 1))):
            Lg = law_gen(b, D, fmap)
            Le = ms.law_L(b, am, ap, fmap)
            ok(Lg == Le, f"K1 ({b},{am},{ap}) {fmap.name}: generalized L*={Lg} against law_L={Le}")
            o, res = game_delay(b, D, fmap, (Le - 1, Le), f"({b},{am},{ap}) {fmap.name} L*={Le}")
            ok(res[Le - 1][0] is not None, f"K1 ({b},{am},{ap}) {fmap.name}: tree alive at L*-1")
            ok(res[Le][0] is None, f"K1 ({b},{am},{ap}) {fmap.name}: tree dead at L*")
        rd = GapReader(b, D, 0, ms.Product(b, am, ap), 0)
        images, dis = rd.witness_count(WITNESS_DEPTH, WITNESS_DEPTH)
        ok(dis == 0, f"K1 ({b},{am},{ap}) x y: {dis} disagreeing images at a contiguous set")
        print(f"  ({b},{am},{ap}) x y witness: {images} images with two legal parents, {dis} disagreeing")


def census(bmax):
    print("\n=== P-A THE TAIL CENSUS: digit sets within [-3, 3], 0 and both signs, at most five digits, two gap sizes")
    rows = []
    for b in range(3, bmax + 1):
        sets = candidate_sets(b)
        inter = [D for D in sets if tail_verdict(b, D)[0]]
        touch = [D for D in inter if tail_verdict(b, D)[3] == 0]
        print(f"  radix {b}: {len(sets)} sets, {len(inter)} with interval tails ({len(touch)} touching, "
              f"z_min = 0), {len(sets) - len(inter)} Cantor")
        for D in inter:
            _, w, gmax, zmin = tail_verdict(b, D)
            rows.append((b, D, w, gmax, zmin))
    for b, D, w, gmax, zmin in rows:
        print(f"    radix {b} {list(D)}: w={w} g_max={gmax} z_min={zmin} slack={len(D) - b}; "
              f"death {'image-only' if image_only(b, D) else 'state-dependent'}")
    return rows


def games(rows):
    print("\n=== P-B..P-E THE GAME at every interval gap set: x y and x/(s + y) at P = 1/(b - 1)")
    summary, witness_rows = [], []
    for b, D, w, gmax, zmin in rows:
        am, ap = -min(D), max(D)
        for fmap in (ms.Product(b, am, ap), ms.Division(b, am, ap, Fr(1, b - 1))):
            Lg = law_gen(b, D, fmap)
            if Lg is None:
                Ls = tuple(range(0, 4))
                tag = f"radix {b} {list(D)} {fmap.name} z_min=0 (law: no L)"
            else:
                Ls = tuple(range(Lg - 2, Lg + 1))
                tag = f"radix {b} {list(D)} {fmap.name} z_min={zmin} law L*={Lg}"
            o, res = game_delay(b, D, fmap, Ls, tag)
            if Lg is not None:
                ok(res[Lg][0] is None, f"K3 {tag}: tree dead at the generalized L* (round {res[Lg][0]})")
            alive_below = [L for L, (r, d) in res.items() if r is None and (Lg is None or L < Lg)]
            summary.append((b, D, fmap.name, zmin, Lg, o, res, alive_below))
        rd = GapReader(b, D, 0, ms.Product(b, am, ap), 0)
        images, dis = rd.witness_count(WITNESS_DEPTH, WITNESS_DEPTH)
        io = image_only(b, D)
        print(f"    witness x y at depth {WITNESS_DEPTH}: {images} images with two legal parents, {dis} disagreeing; "
              f"criterion: {'image-only' if io else 'state-dependent'}")
        ok(not (io and dis > 0), f"K4 radix {b} {list(D)}: a disagreeing image at an image-only set")
        witness_rows.append((b, D, io, dis))
        if zmin == 0:
            for fmap in (ms.Product(b, am, ap), ms.Division(b, am, ap, Fr(1, b - 1))):
                o = ms.least_lead(b, am, ap, fmap)
                print(f"    root touching point inside the range of {fmap.name} at o={o}: "
                      f"{root_touch_inside(b, D, fmap, o)}")
    print("\n=== P-B THE WITNESS AGAINST THE CRITERION")
    sd = [r for r in witness_rows if not r[2]]
    io = [r for r in witness_rows if r[2]]
    print(f"  state-dependent sets {len(sd)}, with a witness at depth {WITNESS_DEPTH}: {sum(1 for r in sd if r[3] > 0)}; "
          f"image-only sets {len(io)}, with a witness: {sum(1 for r in io if r[3] > 0)}")
    print("  image-only: " + "; ".join(f"radix {b} {list(D)}" for b, D, _, _ in io))
    print("\n=== THE DEEPENING PASS: every pair alive below the law's L*, the tree at a larger budget")
    for i, (b, D, nm, z, Lg, o, res, ab) in enumerate(summary):
        if Lg is None or not ab:
            continue
        am, ap = -min(D), max(D)
        fmap = ms.Product(b, am, ap) if nm == "x y" else ms.Division(b, am, ap, Fr(1, b - 1))
        for L in ab:
            rd = GapReader(b, D, L - o, fmap, o)
            t1 = time.time()
            r, depth = rd.certificate(DEEP_BUDGET)
            print(f"  radix {b} {list(D)} {nm} L={L} (law L*={Lg}): "
                  f"{'dead r=' + str(r) if r is not None else 'alive'} [{depth}] {time.time() - t1:.1f}s, "
                  f"{rd.nodes} nodes")
            if r is not None:
                summary[i] = (b, D, nm, z, Lg, o, res, [x for x in ab if x != L])
    print("\n=== SUMMARY")
    pos = [s for s in summary if s[4] is not None]
    zer = [s for s in summary if s[4] is None]
    below = [s for s in pos if s[7]]
    print(f"  z_min > 0: {len(pos)} (set, map) pairs; alive to the tree's depth below the law's L* at {len(below)}: "
          + "; ".join(f"radix {b} {list(D)} {nm} L*={Lg} alive at {ab}" for b, D, nm, z, Lg, o, res, ab in below))
    fin = [s for s in zer if s[7]]
    print(f"  z_min = 0: {len(zer)} (set, map) pairs; alive to the tree's depth at some finite L at {len(fin)}: "
          + "; ".join(f"radix {b} {list(D)} {nm} alive at {ab}" for b, D, nm, z, Lg, o, res, ab in fin))
    dead_all = [s for s in zer if not s[7]]
    print(f"  z_min = 0 dead at every L tested at {len(dead_all)}: "
          + "; ".join(f"radix {b} {list(D)} {nm} rounds {[r for r, d in res.values()]}"
                      for b, D, nm, z, Lg, o, res, ab in dead_all))


def main():
    bmax = int(sys.argv[1]) if len(sys.argv) > 1 else 4
    t0 = time.time()
    control()
    rows = census(bmax)
    games(rows)
    print(f"\nwall {time.time() - t0:.1f}s; failures: {len(FAILURES)}")
    for f in FAILURES:
        print("  ", f)


if __name__ == "__main__":
    main()
