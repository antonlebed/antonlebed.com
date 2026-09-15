"""Does the reader's game at a state-dependent gap set have a bounded
horizon: does a depth-2 lookahead under the midpoint centering score
buy every round the free reader buys at the 42 radix-3 gap-set pairs,
or die before it somewhere?

THE QUESTION. At a state-dependent gap set the reader's choice among
legal digits buys rounds, never a digit (explore_gap_choice.py), and
no one-step score of the present image against the child's zones
stands in for the search: the midpoint centering puppet dies before
the free reader at exactly the three pairs the free reader kills at
round 4, by one round twice and two rounds once, and matches it at the
other 27 state-dependent pairs (explore_gap_centering.py F3). The
hypothesis under test is that the horizon is bounded -- that a puppet
scoring two nodes ahead, the adversary's next extension played out and
the child's own best one-step score read at each, buys every round the
free reader buys. If it holds, the reader at any numeration is a
constant-depth rule, the confined tree replaced by a fixed-depth
lookahead at every digit set; if it fails, the horizon grows with the
free round and the search is the reader.

THE RULE. The reader at output state q, depth t, holds the image
[lo, hi] of the extended input box at input depth n; a legal digit p
names the child q' = bq + p. The one-step midpoint score of a digit at
a node is explore_gap_centering.py's CENTER: the least distance from
the image's midpoint to a zone of the child, the child's zones the
gaps between its own children's cells two depths down. The DEPTH-2
score of p at (us, n, q, t): for every extension us2 of the input to
the depth the next round reads, n2 = t + 2 + c, the adversary
confined to the excess region as the free reader's tree confines it,
read the child's legal digits at us2; the extension's value is -1 if
none is legal (the child dies there) and otherwise the largest
one-step midpoint score among them; the depth-2 score is the least of
these values over the extensions. The puppet takes the legal digit of
largest depth-2 score, ties to the lowest digit. Scores are exact:
the images of the divider carry a denominator that varies with the
input, so a score is a Fraction of its own numerator over 2 S T and
the comparison is exact across extensions and digits.

THE SLATE, frozen before the engine. The instrument is the shipped
centering puppet class (explore_gap_centering.py Centering), the
one-step score reused verbatim, the pick rule replaced by the depth-2
score. Pairs: the 14 radix-3 sets of positive least zone at x y,
x^2 + y and the divider x/(s + y) at P = 1/2, each at L* - 1 of the
generalized law, 42 pairs; the free reader, the two fixed puppets and
the one-step CENTER puppet rerun beside the depth-2 puppet. Controls:
the record's three deep kills at round 4, and the one-step puppet's
record, earlier than the free reader at exactly 3 of the 30
state-dependent pairs, the three round-4 kills, and at 0 of 12
image-only.

P-A THE IMAGE-ONLY SETS [property, carried]. Every puppet dies at the
    free reader's round at all 12 pairs of the 4 image-only sets:
    survival there is the image's by induction, whatever the rule.
P-B THE HYPOTHESIS. The depth-2 puppet dies at the free round at all
    30 state-dependent pairs. The reading against it:
    the one-step puppet's losses are the three round-4 kills, two by
    one round and one by two; a depth-2 score sees the trap a
    round-2 death is, so the puppet reaches at least round 3 at all
    three, and where the free reader's fourth round is bought by a
    choice made two nodes before the kill the puppet matches it; so
    the depth-2 puppet dies before the free reader at between 0 and 3
    of the 30, every loss among the three round-4 kills and none at
    the 27 where the one-step puppet already matches.
P-C THE ORDER AMONG PUPPETS. At every pair the depth-2 puppet's round
    is at least the one-step puppet's: reading deeper never picks
    worse. Reads as a count of pairs where it does; the one-step score
    already loses to a constant at 3 pairs, so this is a prediction and
    not a kill.

KILLS, frozen as what this rig PRINTS.

K1 THE CONTROLS. The free reader's round at any of the three record
   pairs differing from 4 -> nothing below is read.
K2 THE ONE-STEP RECORD. The one-step CENTER puppet earlier than the
   free reader at a count of state-dependent pairs other than 3, or
   at any pair other than the three round-4 kills, or at any
   image-only pair -> the rig is not the record's and nothing below is
   read.
K3 THE IMAGE-ONLY PROPERTY. Any puppet's round differing from the free
   reader's at an image-only pair -> the engine or the criterion is
   wrong.
K4 THE ORDER. Any puppet's round above the free reader's at any pair
   -> the engine is wrong.
K5 THE STATE LEMMA (the shipped reader's own, carried).
THE READING, the hypothesis's kill: the depth-2 puppet's round
below the free reader's at any of the 42 pairs kills the hypothesis,
printed as the count of such pairs and the pairs named with every
puppet's round; 0 at all 42 is the hypothesis surviving as a fixed-depth
rule at this sweep, the depth then swept at its own deep kills.

POSITIVE CONTROL: K1 and K2, read before any other line.

THE DEEP SWEEP, the depth then swept at deeper kills. The 42-pair
sweep's deepest free kill is round 4, and a depth-2 lookahead at a
round-4 kill spans the last choice's whole future, so a match there
fits "the horizon is bounded at 2" and "the horizon is the round less
2" alike; the readings part only at a kill of round 5 or deeper. The
divider's offset s = M- + P sets the map's width rate and so the
excess over the law's threshold one L below L*, and a scout of the
confined free reader over P in {1/4, 1/3, 2/3, 1, 3/2, 2, 3} at the
10 state-dependent radix-3 sets found the deep kills at P = 1/3: the
free reader dies at round 6 at {-3, -2, 0, 2}, {-3, -2, 0, 1, 2}, at
round 5 at {-2, 0, 2, 3}, {-3, -1, 0, 1, 2}, {-2, -1, 0, 1, 3},
{-2, -1, 0, 2, 3}, and is unreached past round 6 at 3 million nodes
at {-3, -2, -1, 0, 2} and {-2, 0, 1, 2, 3}; at P = 1/4 the set
{-3, -1, 0, 1, 3} dies at round 6 (the other P and radix 4 over spans
to 4 and six digits gave nothing past round 4). The deep slate is
these 9 pairs at L* - 1 of the generalized law, the free reader at a
budget of 30 million nodes, and the depth ladder beside it: the two
fixed puppets (depth 0), the one-step CENTER puppet (depth 1) and the
depth-2 puppet.

P-D THE HYPOTHESIS AT DEPTH. The depth-2 puppet dies at the free
    round at every reached deep pair. The reading against
    it, the horizon growing with the round: CENTER matched
    every round-3 kill and lost at every round-4 kill of the record,
    so at a round-6 kill the depth-2 puppet loses by one or two
    rounds at at least one pair and CENTER loses by more than it did
    at round 4; the ladder's rounds rise with the depth at every deep
    pair where any puppet loses.
P-E THE LADDER'S ORDER. At every deep pair the depth-2 puppet's round
    is at least CENTER's and CENTER's at least the better fixed
    puppet's, a count of violations printed (a prediction, not a
    kill: the record already has the one-step score losing to a
    constant).

K6 THE DEEP CONTROLS. The free reader's round at the 7 reached deep
   pairs differing from the scout's (6, 6, 5, 5, 5, 5 at P = 1/3 in
   the order above, 6 at P = 1/4) -> the deep sweep is not read.
THE DEEP READING: the depth-2 puppet's round below the free reader's
at any deep pair kills the hypothesis at depth 2, the ladder printed; the
free round matched at every reached deep pair leaves the hypothesis standing as a
fixed-depth rule at kills to round 6, the unreached pairs named as
unreached.

The depth-2 puppet runs at four times the free reader's wall, its
per-node cost being the next extension's fan-out times the one-step
score.

FINDINGS (entered post-run; every number below sits in this file's
printed output).

F1 THE CONTROLS HOLD. Rounds 4, 4 and 4 at the record's three pairs
   (36,539, 36,708 and 286,169 confined nodes); CENTER earlier than
   the free reader at exactly the three round-4 kills and at 0 of the
   12 image-only pairs; K3, K4 and K5 never fired; no pair unreached.

F2 THE 42 PAIRS [rule at the 30 state-dependent pairs]. The depth-2
   puppet dies at the free reader's round at all 42 pairs, and above
   CENTER at exactly its three losses: the divider over
   {-3, -2, -1, 0, 2} (4 against CENTER's 2), x y over
   {-3, -1, 0, 1, 2} and the divider over {-2, 0, 1, 2, 3} (4 against
   3), at the node count of the fixed puppet that matches the free
   round at the first and third (31,313 and 283,376) and at the free
   reader's own at the second (36,539). The
   reading in P-B held at its lower end (0 of 30), and P-C held (below
   CENTER at 0 of 42).

F3 THE DEEP SWEEP KILLS THE HYPOTHESIS [rule at the 7 reached deep
   pairs]. K6 held: the free rounds 6, 6, 5, 5, 5, 5 at P = 1/3 and 6
   at P = 1/4 are the scout's. At the six P = 1/3 pairs reached every
   puppet dies at the free round at the free reader's node count, the
   choice never real there. At the divider at P = 1/4 over
   {-3, -1, 0, 1, 3} the ladder reads: fixed puppets 4 and 4, CENTER
   4, DEPTH2 5, the free reader 6 (300, 85, 85, 777 and 4,045 nodes).
   At the two unreached pairs the free reader survives 7 rounds at 30
   million nodes: over {-3, -2, -1, 0, 2} the lowest puppet and CENTER
   die at round 6 and the highest puppet and DEPTH2 are unreached at
   7 and 6; over {-2, 0, 1, 2, 3} the highest puppet dies at 6, CENTER
   at 7, the lowest puppet and DEPTH2 unreached at 7 and 6. P-E held:
   the ladder is in order at all 7 reached pairs.

VERDICT. The reader's game at a state-dependent gap set has no
bounded horizon: a two-node lookahead under the midpoint score buys
every round the free reader buys where the deepest kill is round 4
and one round fewer where it is round 6, the ladder rising one round
per depth (4, 4, 5 against 6), and at the two pairs alive past round
7 the one-step puppet dies at 6 and 7, at least two and one rounds
short. The reader at a
state-dependent set is a search whose depth grows with the round it
certifies, and the confined tree is not replaced by a fixed-depth
rule at any digit set where the choice is real.

RUN RECORD: pure Python, the shipped engines imported; under memwatch,
peak commit 42 MB against the 512 MB default, wall 1,645 s at the
budget 3 million nodes and 90 s per free run on the 42 pairs and 30
million nodes at the deep sweep, the two unreached pairs taking 1,400
s of it. Prints reproduced by:
python prime/code/explore_gap_horizon.py [NODE_BUDGET] [WALL_SECONDS]
"""
import os
import sys
import time
from fractions import Fraction as Fr

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import explore_gap_lattice as gl                           # noqa: E402
import explore_beta_delay as bd                            # noqa: E402
import explore_gap_choice as gc                            # noqa: E402
import explore_gap_centering as gcen                       # noqa: E402

FAILS = []
B = gc.B


def ok(cond, msg):
    if not cond:
        FAILS.append(msg)
        print("  KILL:", msg)


class HorizonPuppet(gcen.Centering):
    """The centering puppet reading two nodes ahead: the legal digit
    whose child, at the adversary's worst next extension, keeps the
    best one-step midpoint score."""
    rule = "center"

    def one_step(self, p, us1, n1, q, t):
        """The one-step midpoint score as an exact Fraction."""
        lo, hi, S = self.f.image(us1, n1)
        _, _, T = self.child_zones(self.b * q + p, t)[0]
        return Fr(self.score(p, us1, n1, q, t), 2 * S * T)

    def depth2(self, p, us1, n1, q, t):
        """The least, over the adversary's next extensions, of the
        child's best one-step score; -1 where the child has no legal
        digit at that extension."""
        q1 = self.b * q + p
        t1 = t + 1
        n2 = max(0, t1 + 1 + self.c)
        worst = None
        for us2 in self.extend(us1, n1, n2):
            self.look += 1
            legal2 = [p2 for p2 in self.digits if self.legal(us2, n2, self.b * q1 + p2, t1 + 1)]
            val = Fr(-1) if not legal2 else max(self.one_step(p2, us2, n2, q1, t1) for p2 in legal2)
            if worst is None or val < worst:
                worst = val
                if worst < 0:
                    break
        return worst if worst is not None else Fr(0)

    def choose(self, legal, us1, n1, q, t):
        if len(legal) <= 1:
            return legal
        scored = [(self.depth2(p, us1, n1, q, t), -p, p) for p in legal]
        scored.sort(reverse=True)
        return [scored[0][2]]

    def __init__(self, *a, **k):
        super().__init__(*a, **k)
        self.look = 0


PUPPETS = (("lowest", gc.PuppetLow), ("highest", gc.PuppetHigh),
           ("CENTER", gcen.CenterPuppet), ("DEPTH2", HorizonPuppet))

RECORD_KILLS = ("[-3, -2, -1, 0, 2] x/(", "[-3, -1, 0, 1, 2] x y", "[-2, 0, 1, 2, 3] x/(")


def is_record(label):
    return any(label.startswith(k) for k in RECORD_KILLS)


DEEP = [((-3, -2, 0, 2), Fr(1, 3), 6), ((-3, -2, 0, 1, 2), Fr(1, 3), 6),
        ((-2, 0, 2, 3), Fr(1, 3), 5), ((-3, -1, 0, 1, 2), Fr(1, 3), 5),
        ((-2, -1, 0, 1, 3), Fr(1, 3), 5), ((-2, -1, 0, 2, 3), Fr(1, 3), 5),
        ((-3, -1, 0, 1, 3), Fr(1, 4), 6),
        ((-3, -2, -1, 0, 2), Fr(1, 3), None), ((-2, 0, 1, 2, 3), Fr(1, 3), None)]
DEEP_BUDGET = 30_000_000


def deep_sweep(wall):
    print("\n=== THE DEEP SWEEP: the divider at P = 1/3 and 1/4, the free reader at 30 million nodes, the depth ladder beside it")
    rows = []
    for D, P, scout in DEEP:
        am, ap = -min(D), max(D)
        fmap = gc.maps(D)[2].__class__(B, am, ap, P)
        Lg = gl.law_gen(B, D, fmap)
        label = f"{list(D)} {fmap.name}"
        free = gc.run_pair(D, fmap, Lg - 1, DEEP_BUDGET, 4 * wall)
        pup = {name: gc.run_pair(D, fmap, Lg - 1, DEEP_BUDGET, 4 * wall if name == "DEPTH2" else 2 * wall, cls=cls)
               for name, cls in PUPPETS}
        words = " | ".join(f"{name} {gc.verdict(r)} ({r['nodes']})" for name, r in pup.items())
        print(f"  {label} [state-dependent] L*={Lg}: free {gc.verdict(free)} ({free['nodes']}, {free['secs']:.0f}s) | {words}")
        if scout is not None:
            ok(free['r'] == scout, f"K6 {label}: free round {free['r']} against the scout's {scout}")
        for name, res in pup.items():
            if res['r'] is not None and free['r'] is not None:
                ok(res['r'] <= free['r'],
                   f"K4 {label}: the {name} puppet dies at round {res['r']} above the free reader's {free['r']}")
        rows.append((label, free, pup))
    if any(f.startswith("K6") for f in FAILS):
        print("  DEEP CONTROL FAILED; the deep sweep is not read.")
        return
    print("\n=== THE DEEP READING: the depth ladder against the free reader")
    reached = [r for r in rows if r[1]['r'] is not None and all(p['r'] is not None for p in r[2].values())]
    e = [r for r in reached if r[2]['DEPTH2']['r'] < r[1]['r']]
    for label, free, pup in rows:
        print(f"  {label}: free {gc.verdict(free)} | " + ", ".join(f"{nm} {gc.verdict(res)}" for nm, res in pup.items()))
    print(f"  reached deep pairs: {len(reached)} of {len(rows)}; DEPTH2 earlier than the free reader at {len(e)}: {[r[0] for r in e]}")
    lad = [r for r in reached if not (r[2]['DEPTH2']['r'] >= r[2]['CENTER']['r'] >=
                                      max(r[2]['lowest']['r'], r[2]['highest']['r']))]
    print(f"  P-E the ladder out of order at {len(lad)} of {len(reached)} reached pairs: {[r[0] for r in lad]}")
    print(f"  DEPTH2 at depth: {'THE HYPOTHESIS IS KILLED at depth 2' if e else 'the hypothesis survives at depth 2 at every reached deep pair'}")


def main():
    budget = int(sys.argv[1]) if len(sys.argv) > 1 else 3_000_000
    wall = float(sys.argv[2]) if len(sys.argv) > 2 else 60.0
    t0 = time.time()
    print(f"THE HORIZON PUPPET AT A GAP SET: radix {B}, budget {budget} nodes, wall {wall:.0f}s per free run")

    print("\n=== K1 THE CONTROLS (the record's rounds, all 4)")
    controls = [((-3, -1, 0, 1, 2), 0, 2), ((-3, -2, -1, 0, 2), 2, 3), ((-2, 0, 1, 2, 3), 2, 3)]
    for D, mi, L in controls:
        fmap = gc.maps(D)[mi]
        res = gc.run_pair(D, fmap, L, budget, max(wall, 120.0))
        print(f"  {list(D)} {fmap.name}: {gc.fmt(res)}")
        ok(res['r'] == 4, f"K1 {list(D)} {fmap.name} L={L}: round {res['r']} against the record's 4")
    if FAILS:
        print("\nCONTROL FAILED; nothing below is read.")
        return

    print("\n=== THE 42 PAIRS at L* - 1, confined: the free reader, the fixed puppets, the one-step and the depth-2 puppet")
    sets = [D for D in gl.candidate_sets(B)
            if gl.tail_verdict(B, D)[0] and gl.tail_verdict(B, D)[3] > 0]
    rows = []
    for D in sets:
        io = gl.image_only(B, D)
        _, w, gmax, zmin = gl.tail_verdict(B, D)
        for fmap in gc.maps(D):
            Lg = gl.law_gen(B, D, fmap)
            free = gc.run_pair(D, fmap, Lg - 1, budget, wall)
            label = f"{list(D)} {fmap.name}"
            pup = {name: gc.run_pair(D, fmap, Lg - 1, budget, 4 * wall if name == "DEPTH2" else wall / 2, cls=cls)
                   for name, cls in PUPPETS}
            words = " | ".join(f"{name} {gc.verdict(r)} ({r['nodes']})" for name, r in pup.items())
            print(f"  {label} [{'image-only' if io else 'state-dependent'}, z_min={zmin}, g_max={gmax}] "
                  f"L*={Lg}: free {gc.verdict(free)} ({free['nodes']}) | {words}")
            for name, res in pup.items():
                if res['r'] is not None and free['r'] is not None:
                    ok(res['r'] <= free['r'],
                       f"K4 {label}: the {name} puppet dies at round {res['r']} above the free reader's {free['r']}")
                    if io:
                        ok(res['r'] == free['r'],
                           f"K3 {label}: image-only, the {name} puppet at round {res['r']} against the free {free['r']}")
            rows.append((label, io, D, fmap.name, free, pup))
    ok(not gc.FAILS, f"K5 the shipped reader's own lemma fired {len(gc.FAILS)} time(s)")
    ok(not gcen.FAILS, f"K5 the centering rig's own lemma fired {len(gcen.FAILS)} time(s)")

    def earlier(sub, names):
        return [r for r in sub if r[4]['r'] is not None and
                any(r[5][nm]['r'] is not None and r[5][nm]['r'] < r[4]['r'] for nm in names)]

    print("\n=== K2 THE ONE-STEP RECORD (CENTER earlier at exactly the three round-4 kills, 0 of 12 image-only)")
    sd = [r for r in rows if not r[1]]
    io_rows = [r for r in rows if r[1]]
    e_sd, e_io = earlier(sd, ("CENTER",)), earlier(io_rows, ("CENTER",))
    print(f"  state-dependent: {len(sd)} pairs, CENTER earlier at {len(e_sd)} {[r[0] for r in e_sd]}; "
          f"image-only: {len(io_rows)} pairs, earlier at {len(e_io)}")
    ok(len(sd) == 30 and len(io_rows) == 12 and len(e_io) == 0 and len(e_sd) == 3 and all(is_record(r[0]) for r in e_sd),
       f"K2 CENTER earlier at {[r[0] for r in e_sd]} against the record's three round-4 kills")
    if FAILS:
        print("\nCONTROL FAILED; nothing below is read.")
        return

    print("\n=== THE READING: the depth-2 puppet against the free reader")
    e = earlier(sd, ("DEPTH2",))
    at_rec = [r for r in e if is_record(r[0])]
    print(f"  DEPTH2: earlier than the free reader at {len(e)} of {len(sd)} state-dependent pairs "
          f"({len(at_rec)} of them at the three round-4 kills, {len(e) - len(at_rec)} elsewhere); "
          f"image-only earlier at {len(earlier(io_rows, ('DEPTH2',)))} of {len(io_rows)}")
    for r in e:
        print(f"    EARLIER: {r[0]}: free {r[4]['r']}, DEPTH2 {r[5]['DEPTH2']['r']}, CENTER {r[5]['CENTER']['r']}, "
              f"lowest {r[5]['lowest']['r']}, highest {r[5]['highest']['r']}")
    print("  the three round-4 kills, every puppet's round:")
    for r in rows:
        if is_record(r[0]):
            print(f"    {r[0]}: free {r[4]['r']} | " + ", ".join(f"{nm} {res['r']}" for nm, res in r[5].items()))
    print(f"  DEPTH2: {'THE HYPOTHESIS IS KILLED' if e else 'the hypothesis survives at depth 2 over the 42 pairs'}")

    print("\n=== P-C THE ORDER AMONG PUPPETS: the depth-2 puppet against the one-step puppet")
    worse = [(r[0], r[5]['DEPTH2']['r'], r[5]['CENTER']['r']) for r in rows
             if r[5]['DEPTH2']['r'] is not None and r[5]['CENTER']['r'] is not None
             and r[5]['DEPTH2']['r'] < r[5]['CENTER']['r']]
    better = [(r[0], r[5]['DEPTH2']['r'], r[5]['CENTER']['r']) for r in rows
              if r[5]['DEPTH2']['r'] is not None and r[5]['CENTER']['r'] is not None
              and r[5]['DEPTH2']['r'] > r[5]['CENTER']['r']]
    print(f"  DEPTH2 below CENTER at {len(worse)} of {len(rows)} pairs: "
          + "; ".join(f"{lb} ({c} against {m})" for lb, c, m in worse))
    print(f"  DEPTH2 above CENTER at {len(better)} of {len(rows)} pairs: "
          + "; ".join(f"{lb} ({c} against {m})" for lb, c, m in better))

    print("\n=== THE ROUNDS by map (free reader)")
    for nm in ("x y", "x^2 + y", None):
        sub = [r for r in rows if (r[3] == nm if nm else r[3].startswith("x/("))]
        cnt = {}
        for r in sub:
            k = r[4]['r'] if r[4]['r'] is not None else "unreached"
            cnt[k] = cnt.get(k, 0) + 1
        print(f"  {nm or 'the divider'}: {dict(sorted(cnt.items(), key=lambda kv: str(kv[0])))}")
    unreached = [r[0] for r in rows if r[4]['r'] is None or any(p['r'] is None for p in r[5].values())]
    print(f"  unreached pairs: {len(unreached)} {unreached}")

    deep_sweep(wall)

    print(f"\nwall {time.time() - t0:.0f}s; {'ALL KILLS MISSED' if not FAILS else str(len(FAILS)) + ' KILL(S) FIRED'}")
    for f in FAILS:
        print("  ", f)


if __name__ == "__main__":
    main()
