"""Is the optimal reader at a state-dependent gap set memoryless: does
the legal digit keeping the image farthest from its child's zones buy
every round the free reader buys at the 42 radix-3 gap-set pairs, or
die before it somewhere?

THE QUESTION. At a gap set the reader's choice among legal digits is
real at killing boxes and buys rounds (explore_gap_choice.py): a
reader whose legal list is cut to one fixed digit, its lowest or its
highest, dies at round 2 at 9 of the 11 pairs killed at round 3 or 4,
where the free reader searches every legal child to the tree's depth.
The hypothesis under test is that the search is not needed -- that the
free reader's extra rounds are bought by ONE choice a one-line rule
makes, the rule reading nothing but the present image and the
candidate child's zones. If it holds, delay at any digit set is
certified by the forced recursion under that rule, the game tree
retired; if it fails, the reader at a state-dependent set is a game
and no memoryless rule stands in for it.

THE RULE, two readings of "farthest from the nearest zone", both run.
The reader at output state q, depth t, holds the image [lo, hi] of the
extended input box; a legal digit p names the child q' = bq + p, whose
zones are the gaps between its own children's cells at depth t + 2,
(top_d, bot_{d'}) for consecutive digits d < d'. The child dies at the
next node when the extended image strictly contains one of its zones.
  CENTER: the score of p is the least distance from the image's
    midpoint to a zone of q' (0 when the midpoint lies in a zone); the
    puppet takes the largest score, ties to the lowest digit.
  MARGIN: the score of p is the least, over the zones of q', of the
    amount by which the image fails to strictly contain the zone,
    max(lo - top, bot - hi); the puppet takes the largest score, ties
    to the lowest digit.
Both are exact in integers: the images share one denominator S at a
node and the cells one denominator T at a depth, so scores are
compared as cross-multiplied integers.

THE SLATE, frozen before the engine. The instrument is the shipped
counting reader (explore_gap_choice.py CountingGap) with the pick
rule handed the node's state. Pairs: the 14 radix-3 sets of positive
least zone at x y, x^2 + y and the divider x/(s + y) at P = 1/2, each
at L* - 1 of the generalized law, 42 pairs; the free reader and the
two fixed puppets rerun beside the two centering puppets. Controls:
the record's three deep kills at round 4, and the fixed puppets'
record (a puppet earlier at 9 of the 30 state-dependent pairs, at 0
of the 12 image-only).

P-A THE IMAGE-ONLY SETS [property, carried]. Every puppet dies at the
    free reader's round at all 12 pairs of the 4 image-only sets:
    survival there is the image's by induction, whatever the rule.
P-B THE HYPOTHESIS. A centering puppet dies at the free round at all
    30 state-dependent pairs. The reading against it:
    the fixed puppets' losses are all round-2 deaths at deep kills, a
    trap set at depth two, and a one-step score reads depth one; so a
    centering puppet dies before the free reader at between 1 and 8 of
    the 9 pairs where a fixed puppet loses, and at none of the 21
    where both fixed puppets already match the free round.
P-C THE ORDER AMONG PUPPETS. At every pair a centering puppet's round
    is at least the better fixed puppet's: the rule never loses to a
    constant. Reads as a count of pairs where it does.

KILLS, frozen as what this rig PRINTS.

K1 THE CONTROLS. The free reader's round at any of the three record
   pairs differing from 4 -> nothing below is read.
K2 THE FIXED-PUPPET RECORD. The fixed puppets' earlier count at the
   state-dependent pairs differing from 9, or nonzero at the
   image-only pairs -> the rig is not the record's and nothing below
   is read.
K3 THE IMAGE-ONLY PROPERTY. Any puppet's round differing from the free
   reader's at an image-only pair -> the engine or the criterion is
   wrong.
K4 THE ORDER. Any puppet's round above the free reader's at any pair
   -> the engine is wrong.
K5 THE STATE LEMMA (the shipped reader's own, carried).
THE READING, the hypothesis's kill: a centering puppet's round
below the free reader's at any of the 42 pairs kills the hypothesis for
that rule, printed as the count of such pairs per rule and the pairs
named; 0 at both rules at all 42 is the hypothesis surviving; 0 at one rule
is the hypothesis amended to that rule.

POSITIVE CONTROL: K1 and K2, read before any other line.

FINDINGS (entered post-run; every number below sits in this file's
printed output).

F1 THE CONTROLS HOLD. Rounds 4, 4 and 4 at the record's three pairs
   (36,539, 36,708 and 286,169 confined nodes); a fixed puppet earlier
   at 9 of the 30 state-dependent pairs and 0 of the 12 image-only,
   the record's; K5 never fired at any node of any tree; no pair
   unreached.

F2 THE IMAGE-ONLY SETS [property, checked]. All four puppets die at
   the free reader's round at all 12 image-only pairs, at the free
   reader's node count; K3 never fired.

F3 THE HYPOTHESIS IS KILLED AT BOTH RULES [rule at the 30 pairs]. CENTER
   dies before the free reader at 3 of the 30 state-dependent pairs
   and MARGIN at 8, every loss at one of the 9 pairs where a fixed
   puppet loses and none at the 21 where both fixed puppets match the
   free round. CENTER's three are the three deepest kills, the pairs
   the free reader kills at round 4: the divider over
   {-3, -2, -1, 0, 2} (CENTER 2, the highest digit 4), x y over
   {-3, -1, 0, 1, 2} (CENTER 3, the lowest digit 4) and the divider
   over {-2, 0, 1, 2, 3} (CENTER 3, the lowest digit 4); at the other
   6 of the 9 CENTER reaches the free round, at the free reader's node
   count or under it. MARGIN dies at round 2 at 8 of the 9, the
   fixed puppets' round, and reaches the free round only at the
   divider over {-2, 0, 2, 3}. The counter-reading held at both
   rules (1 to 8 of the 9, none elsewhere). K4 never fired.

F4 THE ORDER AMONG PUPPETS. CENTER dies before the better fixed
   puppet at 3 of the 42 pairs, its three losses, by two rounds once
   and one round twice; MARGIN at 7 of the 42, by two rounds at the
   three round-4 kills and one round at the other 4. P-C failed at
   both rules: a one-step score picks worse
   than a constant, and neither rule is the best puppet at every pair.

F5 THE ROUNDS. The free rounds reproduce the record: x y 1 at 6 sets,
   2 at 6, 3 at 1, 4 at 1; x^2 + y 1 at 11, 2 at 2, 3 at 1; the
   divider 1 at 3, 2 at 3, 3 at 6, 4 at 2.

VERDICT. The optimal reader at a state-dependent gap set is not
memoryless: both readings of the centering rule die before the free
reader, the midpoint rule at 3 of the 30 state-dependent pairs and
the margin rule at 8, every loss at a deep kill and the midpoint
rule's exactly the three round-4 kills, so the rounds the free reader
buys there are bought by a search that sees past the next node and by
no one-step score of the present image against the child's zones. A
one-step score is not even the best constant, losing to a fixed digit
at 3 and 7 pairs. The reader at a state-dependent set is a game; the
midpoint rule is its best one-line approximation, exact at 27 of 30
and one or two rounds short at the deepest three.

RUN RECORD: pure Python, the shipped engines imported; under memwatch,
peak commit 43 MB against the 512 MB default, wall 9 s at the budget
3 million nodes and 60 s per free run, the puppets at 30 s. Prints
reproduced by:
python prime/code/explore_gap_centering.py [NODE_BUDGET] [WALL_SECONDS]
"""

import os
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import explore_manystream_delay as ms                      # noqa: E402
import explore_gap_lattice as gl                           # noqa: E402
import explore_beta_delay as bd                            # noqa: E402
import explore_gap_choice as gc                            # noqa: E402

FAILS = []
B = gc.B


def ok(cond, msg):
    if not cond:
        FAILS.append(msg)
        print("  KILL:", msg)


class Centering(gc.CountingGap):
    """The counting reader whose pick rule reads the node: the legal
    digit whose child keeps the image farthest from its zones."""
    rule = "center"

    def child_zones(self, q1, t):
        """The zones of child q1, a state at depth t + 1, as
        (top, bot, T): the gaps between its own children's cells at
        depth t + 2, the depth dead_by_zone reads them at."""
        out = []
        for d, d1 in self.pairs:
            _, top, T = self.cell(self.b * q1 + d, t + 2)
            bot = self.cell(self.b * q1 + d1, t + 2)[0]
            out.append((top, bot, T))
        return out

    def score(self, p, us1, n1, q, t):
        lo, hi, S = self.f.image(us1, n1)
        best = None
        for top, bot, T in self.child_zones(self.b * q + p, t):
            if self.rule == "center":
                mid = (lo + hi) * T                      # 2 S T x midpoint
                s = max(top * 2 * S - mid, mid - bot * 2 * S, 0)
            else:
                s = max(lo * T - top * S, bot * S - hi * T)
            best = s if best is None else min(best, s)
        return best

    def choose(self, legal, us1, n1, q, t):
        if len(legal) <= 1:
            return legal
        scored = [(self.score(p, us1, n1, q, t), -p, p) for p in legal]
        scored.sort(reverse=True)
        return [scored[0][2]]

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
                       for p in self.choose(legal, us1, n1, q, t)):
                return False
        return True


class CenterPuppet(Centering):
    rule = "center"


class MarginPuppet(Centering):
    rule = "margin"


PUPPETS = (("lowest", gc.PuppetLow), ("highest", gc.PuppetHigh),
           ("CENTER", CenterPuppet), ("MARGIN", MarginPuppet))


def rnd(res):
    return res['r']


def main():
    budget = int(sys.argv[1]) if len(sys.argv) > 1 else 3_000_000
    wall = float(sys.argv[2]) if len(sys.argv) > 2 else 60.0
    t0 = time.time()
    print(f"THE CENTERING PUPPET AT A GAP SET: radix {B}, budget {budget} nodes, wall {wall:.0f}s per free run")

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

    print("\n=== THE 42 PAIRS at L* - 1, confined: the free reader, the two fixed puppets, the two centering puppets")
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
            pup = {name: gc.run_pair(D, fmap, Lg - 1, budget, wall / 2, cls=cls) for name, cls in PUPPETS}
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

    def earlier(sub, names):
        return [r for r in sub if r[4]['r'] is not None and
                any(r[5][nm]['r'] is not None and r[5][nm]['r'] < r[4]['r'] for nm in names)]

    print("\n=== K2 THE FIXED-PUPPET RECORD (a puppet earlier at 9 of 30 state-dependent, 0 of 12 image-only)")
    sd = [r for r in rows if not r[1]]
    io_rows = [r for r in rows if r[1]]
    e_sd, e_io = earlier(sd, ("lowest", "highest")), earlier(io_rows, ("lowest", "highest"))
    print(f"  state-dependent: {len(sd)} pairs, a fixed puppet earlier at {len(e_sd)}; "
          f"image-only: {len(io_rows)} pairs, earlier at {len(e_io)}")
    ok(len(sd) == 30 and len(e_sd) == 9 and len(io_rows) == 12 and len(e_io) == 0,
       f"K2 fixed puppets earlier at {len(e_sd)} of {len(sd)} state-dependent, {len(e_io)} of {len(io_rows)} image-only")
    if FAILS:
        print("\nCONTROL FAILED; nothing below is read.")
        return

    print("\n=== THE READING: the centering puppets against the free reader")
    fixed_loss = {r[0] for r in e_sd}
    for name in ("CENTER", "MARGIN"):
        e = earlier(sd, (name,))
        at_fixed = [r for r in e if r[0] in fixed_loss]
        print(f"  {name}: earlier than the free reader at {len(e)} of {len(sd)} state-dependent pairs "
              f"({len(at_fixed)} of them at the 9 fixed-puppet losses, {len(e) - len(at_fixed)} elsewhere); "
              f"image-only earlier at {len(earlier(io_rows, (name,)))} of {len(io_rows)}")
        for r in e:
            print(f"    EARLIER: {r[0]}: free {r[4]['r']}, {name} {r[5][name]['r']}, "
                  f"lowest {r[5]['lowest']['r']}, highest {r[5]['highest']['r']}")
        print(f"  {name}: {'THE HYPOTHESIS IS KILLED at this rule' if e else 'the hypothesis survives at this rule'}")

    print("\n=== P-C THE ORDER AMONG PUPPETS: a centering puppet against the better fixed puppet")
    for name in ("CENTER", "MARGIN"):
        worse = []
        for r in rows:
            fx = [r[5][nm]['r'] for nm in ("lowest", "highest") if r[5][nm]['r'] is not None]
            c = r[5][name]['r']
            if fx and c is not None and c < max(fx):
                worse.append((r[0], c, max(fx)))
        print(f"  {name} below the better fixed puppet at {len(worse)} of {len(rows)} pairs: "
              + "; ".join(f"{lb} ({c} against {m})" for lb, c, m in worse))

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

    print(f"\nwall {time.time() - t0:.0f}s; {'ALL KILLS MISSED' if not FAILS else str(len(FAILS)) + ' KILL(S) FIRED'}")
    for f in FAILS:
        print("  ", f)


if __name__ == "__main__":
    main()
