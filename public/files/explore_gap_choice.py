"""Does the reader's choice at a gap set buy a round: at the radix-3
digit sets with a gap and a positive least zone, does a reader with its
choice removed die earlier than the free reader below the margin law's
L*, or at the same round?

THE QUESTION. Below the margin law's L* at a contiguous digit set, in
base beta as at an integer radix, the reader's move is forced at every
box that can kill (explore_delay_choice.py): the legal digits are those
within the room l' = w - W' below the image's offset, and a box whose
image W' is wider than the zone w - 1 has room under one digit. At a
digit set D with a GAP the same coordinate says something else. Let
the gaps between consecutive digits be g_i with largest g_max and least
zone z_min = w - g_max. The legal digits are D within [v - l', v]; two
of them fit iff the room reaches the small gap, l' >= 1 at every set
here; and the image exceeds the least zone iff l' < g_max. So a box
whose image still exceeds the least zone -- a box the adversary can
still kill at, by driving the window across the g_max gap -- holds two
legal digits whenever its room lies in [1, g_max), a nonempty interval
at every set with two gap sizes. The choice at a gap set is REAL at
killing boxes, inside the gap-1 runs, and the record's reading of the
kill round as the reader's strategy, refuted in base beta, has its one
remaining home here. Whether that choice buys rounds is the third arm
again: the same confined tree with the reader's legal list cut to one
digit, its lowest and then its highest.

TWO CONSEQUENCES DERIVED BEFORE THE RUN, both kills. A puppet never
outlives the free reader: a puppet surviving r rounds at a node means
every extension's picked digit survives r - 1 as a puppet, which by
induction survives r - 1 free, so the free reader survives r; hence
every puppet round is at most the free round. At an IMAGE-ONLY set
(explore_gap_lattice.py's criterion: every zone of one legal parent
inside the overlap contains a zone of the other, so death is a
property of the image alone) survival is image-only by the same
induction -- at round 1 it is not-dead, and at round r every legal
child at one image has the same round-(r - 1) verdict -- so the choice
among legal digits changes nothing and both puppets die at the free
reader's round exactly. Of the 14 radix-3 sets of positive least zone,
4 are image-only ({-3, -1, 0, 2}, {-2, 0, 1, 3}, {-3, -2, 0, 1, 3},
{-3, -1, 0, 2, 3}) and 10 state-dependent.

THE SLATE, frozen before the engine. The instrument is the shipped
confined gap reader (explore_beta_delay.py ConfinedGap) with two
counters at every node it visits: the number of legal reader digits
and whether the image is wider than the least zone (exact in integers,
a tie counted apart). Pairs: the 14 radix-3 sets of positive least
zone (explore_gap_lattice.py candidate_sets and tail_verdict) at the
three maps x y, x^2 + y and the divider x/(s + y) at P = 1/2, each at
L* - 1 of the generalized law, 42 pairs. The puppets: the same tree
with the legal list cut to its lowest digit, and again to its highest.
Controls: the record's three deep kills, x y over {-3, -1, 0, 1, 2} at
L = 2 (round 4) and the divider over {-3, -2, -1, 0, 2} and
{-2, 0, 1, 2, 3} at L = 3 (round 4 at both, explore_beta_delay.py F6),
and the contiguous cell (3, 2, 2) at the three maps, where the reader
has no strategy.

P-A THE ROOM. Nodes with two or more legal digits at an image wider
    than the least zone exist: a positive count at some of the 42
    pairs, by the room derivation; 0 at the contiguous control, where
    the room at a wide image is under one digit (a tie admits two at
    an integer radix, counted apart).
P-B THE PUPPET AT AN IMAGE-ONLY SET [property]. Both puppets die at the
    free reader's round at all 12 pairs of the 4 image-only sets.
P-C THE PUPPET AT A STATE-DEPENDENT SET. TRANSPLANT from base beta:
    the same round at every one of the 30 pairs, the choice
    re-offsetting the drift without delaying the arc. The derivation's
    own reading: at some state-dependent pair a puppet dies at least
    one round before the free reader, since the choice here sits at
    boxes that can kill, and the record's strategy reading holds at a
    gap set and fails in base beta -- the necessity front's proof
    SPLITS by digit set.
P-D THE ROUNDS. The free rounds reproduce the records: x y and the
    divider at 1 to 4 (explore_gap_lattice.py F4, explore_beta_delay.py
    F6), x^2 + y at 1 to 3 (explore_delay_sweep.py F2).

KILLS, frozen as what this rig PRINTS.

K1 THE CONTROLS. The counting reader's round at any of the three
   record pairs differing from 4 -> nothing below is read.
K2 THE CONTIGUOUS CONTROL. Any node with two or more legal digits at
   an image strictly wider than the zone at (3, 2, 2) -> the counters
   are wrong.
K3 THE IMAGE-ONLY PROPERTY. A puppet's round differing from the free
   reader's at any pair of an image-only set -> the engine or the
   criterion is wrong.
K4 THE ORDER. A puppet's round above the free reader's at any pair ->
   the engine is wrong.
K5 THE STATE LEMMA (the shipped reader's own, carried): "no legal
   child" disagreeing with "the image strictly contains a zone".
THE READING: a puppet round below the free reader's at a
state-dependent pair is P-C's second reading, printed as the count of
such pairs; the same round at all 30 is the transplant.

POSITIVE CONTROL: K1, read before any other line.

FINDINGS (entered post-run; every number below sits in this file's
printed output).

F1 THE CONTROLS HOLD. Rounds 4, 4 and 4 at 36,539, 36,708 and 286,169
   confined nodes, the record's rounds; K1 never fired, and K5 never
   fired at any node of any tree.

F2 THE ROOM [the contiguous count a property's print; the gap-set
   census an observation]. At (3, 2, 2) no node with two legal digits
   at a wide image over the three maps (93, 3 and 93 nodes; 16 and 15
   at narrow images at x y and the divider). At the gap sets,
   two-digit nodes at images wider than the least zone at 25 of the 42
   pairs and 276,511 of the 388,829 confined nodes over all 42 -- from
   1.8 percent of a tree ({-2, 0, 1, 3} divider) to 77.7 percent
   ({-2, 0, 1, 2, 3} divider, 222,350 of 286,169) -- up to three legal
   digits; a tie with the least zone only at the two z_min = 1 sets at
   x^2 + y (8 and 9 nodes).

F3 THE PUPPET AT AN IMAGE-ONLY SET [property, checked]. Both puppets
   die at the free reader's round at all 12 pairs of the 4 image-only
   sets, at the same node count; K3 never fired, although two-digit
   nodes at wide images exist there too (25 of 104 at {-3, -1, 0, 2}
   x y).

F4 THE PUPPET AT A STATE-DEPENDENT SET [rule at the 30 pairs]. Both
   puppets die at the free round at 21 of 30 and a puppet dies earlier
   at 9 -- the divider at 6 sets, x y at 2, x^2 + y at 1 -- by one
   round at 6 pairs and by two at 3 (the divider over {-3, -2, -1, 0,
   2} and over {-2, 0, 1, 2, 3}, and x y over {-3, -1, 0, 1, 2}, free
   round 4 against a puppet's 2). The nine are exactly the deep kills
   but two: at every pair killed at round 1 or 2 (31 pairs) both
   puppets die at the free round, and at 9 of the 11 pairs killed at
   round 3 or 4 a puppet dies at ROUND 2, the exceptions the divider
   over {-3, -1, 0, 1, 2} and over {-2, -1, 0, 1, 3} (round 3, both
   puppets 3). Which puppet buys the rounds is the pair's: both at 2
   pairs, the lowest alone at 2, the highest alone at 5. K4 never
   fired: no puppet outlived the free reader. The transplant failed
   and the derivation's own reading held.

F5 THE ROUNDS. x y 1 at 6 sets, 2 at 6, 3 at 1, 4 at 1; x^2 + y 1 at
   11, 2 at 2, 3 at 1; the divider 1 at 3, 2 at 3, 3 at 6, 4 at 2:
   the records' ranges.

VERDICT. At a gap set the reader's choice is real at killing boxes and
it buys rounds: never an L (every pair dead at L* - 1) but a round or
two exactly at the deep kills, nine of the eleven pairs killed at
round 3 or 4 dying at round 2 with the choice removed, and none at an
image-only set, where survival is the image's. The record's "strategy"
reading is right at the state-dependent gap sets and wrong in base
beta, so necessity off the contiguous sets SPLITS BY DIGIT SET: at the
image-only sets and in base beta it is the forced remainder recursion
reaching an arc; at the state-dependent sets it is a game the reader
plays for a round or two and never for a digit.

RUN RECORD: pure Python, the shipped engines imported; under memwatch,
peak commit 41 MB against the 512 MB default, wall 8 s at the budget
3 million nodes and 60 s per free run, the puppets at 30 s. Prints
reproduced by:
python prime/code/explore_gap_choice.py [NODE_BUDGET] [WALL_SECONDS]
"""

import os
import sys
import time
from fractions import Fraction as Fr

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import explore_manystream_delay as ms                      # noqa: E402
import explore_gap_lattice as gl                           # noqa: E402
import explore_beta_delay as bd                            # noqa: E402

FAILS = []
B = 3


def ok(cond, msg):
    if not cond:
        FAILS.append(msg)
        print("  KILL:", msg)


class CountingGap(bd.ConfinedGap):
    """The confined gap reader with two counters at every visited node:
    the legal-digit count and the image's width against the least
    zone, exact in integers."""
    pick = staticmethod(lambda legal: legal)

    def __init__(self, b, D, c, fmap, o):
        super().__init__(b, D, c, fmap, o)
        D = sorted(D)
        gaps = [(D[i + 1] - D[i], D[i], D[i + 1]) for i in range(len(D) - 1)]
        _, d, d1 = max(gaps)
        self.gpair = (d, d1)
        self.hist = {}
        self.max_legal = 0

    def kind(self, us1, n1, q, t):
        lo, hi, S = self.f.image(us1, n1)
        d, d1 = self.gpair
        bot = self.cell(self.b * q + d1, t + 1)[0]
        _, top, T = self.cell(self.b * q + d, t + 1)
        lhs, rhs = (hi - lo) * T, (top - bot) * S
        return "wide" if lhs > rhs else ("tie" if lhs == rhs else "narrow")

    def survives(self, us, n, q, t, rounds, confined=False):
        if rounds == 0:
            return True
        n1 = max(0, t + 1 + self.c)
        for us1 in self.extend(us, n, n1):
            self.nodes += 1
            if self.nodes > self.budget or time.time() > self.t_end:
                raise bd.Budget()
            legal = [p for p in self.digits if self.legal(us1, n1, self.b * q + p, t + 1)]
            if self.lemma_checked < 100_000:
                self.lemma_checked += 1
                ok((not legal) == self.dead_by_zone(us1, n1, q, t),
                   f"K5 state lemma at ({self.b},{self.digits}) {self.f.name} c={self.c}")
            key = (len(legal), self.kind(us1, n1, q, t))
            self.hist[key] = self.hist.get(key, 0) + 1
            self.max_legal = max(self.max_legal, len(legal))
            if not any(self.survives(us1, n1, self.b * q + p, t + 1, rounds - 1)
                       for p in self.pick(legal)):
                return False
        return True


class PuppetLow(CountingGap):
    pick = staticmethod(lambda legal: legal[:1])


class PuppetHigh(CountingGap):
    pick = staticmethod(lambda legal: legal[-1:])


def maps(D):
    am, ap = -min(D), max(D)
    return [ms.Product(B, am, ap), ms.SquarePlus(B, am, ap), ms.Division(B, am, ap, Fr(1, B - 1))]


def run_pair(D, fmap, L, budget, wall, cls=CountingGap, max_rounds=14):
    am, ap = -min(D), max(D)
    o = ms.least_lead(B, am, ap, fmap)
    rd = cls(B, D, L - o, fmap, o)
    t1 = time.time()
    r, depth = rd.certificate(budget, wall=wall, max_rounds=max_rounds)
    h = rd.hist
    return dict(L=L, o=o, r=r, depth=depth, nodes=rd.nodes, secs=time.time() - t1,
                two_wide=sum(v for (k, kd), v in h.items() if k >= 2 and kd == "wide"),
                two_tie=sum(v for (k, kd), v in h.items() if k >= 2 and kd == "tie"),
                two_narrow=sum(v for (k, kd), v in h.items() if k >= 2 and kd == "narrow"),
                wide=sum(v for (k, kd), v in h.items() if kd == "wide"),
                max_legal=rd.max_legal, hist=h)


def verdict(res):
    return f"dead r={res['r']}" if res['r'] is not None else f"UNREACHED [{res['depth']}]"


def fmt(res):
    return (f"L={res['L']} o={res['o']}: {verdict(res)} {res['nodes']} nodes {res['secs']:.1f}s | "
            f"2+ legal at wide {res['two_wide']}, at tie {res['two_tie']}, at narrow {res['two_narrow']} | "
            f"wide nodes {res['wide']} | max legal {res['max_legal']}")


def main():
    budget = int(sys.argv[1]) if len(sys.argv) > 1 else 3_000_000
    wall = float(sys.argv[2]) if len(sys.argv) > 2 else 60.0
    t0 = time.time()
    print(f"THE READER'S CHOICE AT A GAP SET: radix {B}, budget {budget} nodes, wall {wall:.0f}s per free run")

    print("\n=== K1 THE CONTROLS (the record's rounds, all 4)")
    controls = [((-3, -1, 0, 1, 2), 0, 2), ((-3, -2, -1, 0, 2), 2, 3), ((-2, 0, 1, 2, 3), 2, 3)]
    for D, mi, L in controls:
        fmap = maps(D)[mi]
        res = run_pair(D, fmap, L, budget, max(wall, 120.0))
        print(f"  {list(D)} {fmap.name}: {fmt(res)}")
        ok(res['r'] == 4, f"K1 {list(D)} {fmap.name} L={L}: round {res['r']} against the record's 4")
    if FAILS:
        print("\nCONTROL FAILED; nothing below is read.")
        return

    print("\n=== K2 THE CONTIGUOUS CONTROL (3, 2, 2): the reader has no strategy")
    D = (-2, -1, 0, 1, 2)
    for fmap in maps(D):
        Le = ms.law_L(B, 2, 2, fmap)
        res = run_pair(D, fmap, Le - 1, budget, wall)
        print(f"  {list(D)} {fmap.name} L*={Le}: {fmt(res)}")
        ok(res['two_wide'] == 0, f"K2 {fmap.name}: {res['two_wide']} nodes with 2+ legal digits at a wide image")

    print("\n=== THE 42 PAIRS at L* - 1, confined, the free reader then the two puppets")
    sets = [D for D in gl.candidate_sets(B)
            if gl.tail_verdict(B, D)[0] and gl.tail_verdict(B, D)[3] > 0]
    print(f"  sets of positive least zone: {len(sets)}; image-only: "
          f"{[list(D) for D in sets if gl.image_only(B, D)]}")
    rows = []
    for D in sets:
        io = gl.image_only(B, D)
        _, w, gmax, zmin = gl.tail_verdict(B, D)
        for fmap in maps(D):
            Lg = gl.law_gen(B, D, fmap)
            free = run_pair(D, fmap, Lg - 1, budget, wall)
            label = f"{list(D)} {fmap.name}"
            print(f"  {label} [{'image-only' if io else 'state-dependent'}, z_min={zmin}, g_max={gmax}] "
                  f"L*={Lg} {fmt(free)}")
            lo = run_pair(D, fmap, Lg - 1, budget, wall / 2, cls=PuppetLow)
            hi = run_pair(D, fmap, Lg - 1, budget, wall / 2, cls=PuppetHigh)
            print(f"      free round {verdict(free)} ({free['nodes']}) | lowest-digit puppet {verdict(lo)} "
                  f"({lo['nodes']}) | highest-digit puppet {verdict(hi)} ({hi['nodes']})")
            for name, res in (("lowest", lo), ("highest", hi)):
                if res['r'] is not None and free['r'] is not None:
                    ok(res['r'] <= free['r'],
                       f"K4 {label}: the {name}-digit puppet dies at round {res['r']} above the free reader's {free['r']}")
                    if io:
                        ok(res['r'] == free['r'],
                           f"K3 {label}: image-only, the {name}-digit puppet at round {res['r']} against the free {free['r']}")
            rows.append((label, io, D, fmap.name, free, lo, hi))

    print("\n=== P-A THE ROOM: two-digit nodes at images wider than the least zone")
    for label, io, D, nm, free, lo, hi in rows:
        if free['two_wide'] or free['two_tie']:
            print(f"  {label}: {free['two_wide']} of {free['nodes']} nodes at a wide image "
                  f"({100 * free['two_wide'] / free['nodes']:.1f}%), {free['two_tie']} at a tie, "
                  f"{free['two_narrow']} at a narrow one; histogram {sorted(free['hist'].items())}")
    nw = sum(1 for r in rows if r[4]['two_wide'])
    print(f"  pairs with a two-digit node at a wide image: {nw} of {len(rows)}; "
          f"such nodes over every pair: {sum(r[4]['two_wide'] for r in rows)} of "
          f"{sum(r[4]['nodes'] for r in rows)} confined nodes")

    print("\n=== P-B, P-C THE PUPPET: rounds by set class")
    for cls_name, want_io in (("image-only", True), ("state-dependent", False)):
        sub = [r for r in rows if r[1] == want_io]
        same = [r for r in sub if r[4]['r'] is not None and r[5]['r'] == r[4]['r'] and r[6]['r'] == r[4]['r']]
        earlier = [r for r in sub if r[4]['r'] is not None and
                   ((r[5]['r'] is not None and r[5]['r'] < r[4]['r']) or
                    (r[6]['r'] is not None and r[6]['r'] < r[4]['r']))]
        unreached = [r for r in sub if r[4]['r'] is None or r[5]['r'] is None or r[6]['r'] is None]
        print(f"  {cls_name}: {len(sub)} pairs; both puppets at the free round at {len(same)}; "
              f"a puppet earlier at {len(earlier)}; unreached at {len(unreached)}")
        for label, io, D, nm, free, lo, hi in earlier:
            print(f"    EARLIER: {label}: free {free['r']}, lowest {lo['r']}, highest {hi['r']}")
        for label, io, D, nm, free, lo, hi in unreached:
            print(f"    unreached: {label}: free {verdict(free)}, lowest {verdict(lo)}, highest {verdict(hi)}")

    print("\n=== P-D THE ROUNDS by map (free reader)")
    for nm in ("x y", "x^2 + y", None):
        sub = [r for r in rows if (r[3] == nm if nm else r[3].startswith("x/("))]
        cnt = {}
        for r in sub:
            k = r[4]['r'] if r[4]['r'] is not None else "unreached"
            cnt[k] = cnt.get(k, 0) + 1
        print(f"  {nm or 'the divider'}: {dict(sorted(cnt.items(), key=lambda kv: str(kv[0])))}")

    print(f"\nwall {time.time() - t0:.0f}s; {'ALL KILLS MISSED' if not FAILS else str(len(FAILS)) + ' KILL(S) FIRED'}")
    for f in FAILS:
        print("  ", f)


if __name__ == "__main__":
    main()
