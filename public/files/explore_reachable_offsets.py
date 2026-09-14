"""Is the kill round in base beta a covering-radius law of the reachable
offsets -- the first depth at which the offsets the confined tree
realizes are finer than the dead arc -- or is the round the image
width's?

THE QUESTION. At the confined tree's killed pairs, does the kill come
at the covering depth, before it by an arithmetic hit, or after it
because the killing nodes' own arcs are shorter than the widest? Below the margin law's L* at a contiguous digit set in
base beta the reader's move is forced at every box that can kill
(explore_delay_choice.py), so necessity there is the statement that
the forced remainder recursion reaches a dead arc, and the kill round
measures the adversary's search for that arc. Write the game in one
coordinate at the child's grain: at a node with parent q at output
depth t and image [lo, hi] at input depth n1 = t + 1 + c, let the unit
be the child cell's digit spacing beta^(o - t - 1), W = (hi - lo)/unit
the image's width, w = 2a/(beta - 1) the child cell's width and
v = (lo - floor of child -a's cell)/unit - a the image floor's
position on the child grid, so that digit d is legal iff
v - (w - W) <= d <= v. The image kills iff v lies in a DEAD ARC
(d + 1 - g, d + 1) for some digit d < a, its length g = W - (w - 1) the
node's own excess; write delta = ceil(v) - v for the distance below the
nearest grid point above v, so the node is dead iff 0 < delta < g. Two
quantities then face each other at every depth r: the set of deltas
the confined tree realizes at round r, whose largest gap on the circle
[0, 1) is G_r, and the arcs' lengths, whose largest over the depth's
nodes is g_r. If G_r < g_r then EVERY arc of length g_r holds a
realized delta, so a kill at round r is forced by counting alone
provided the node holding that delta has an arc as long as g_r; the
COVERING DEPTH r_cov is the first r with G_r < g_r, an upper bound on
the kill round only up to the per-node arc. Three readings of the
kill round r against r_cov, separated by the prints: r = r_cov, the
round is a covering-radius law of the shift set and the round's fitted
variable is the delta set's spread against the excess; r < r_cov, the
kill is an arithmetic hit before counting forces it and the round is
the offsets' but not their spread's; r > r_cov, the deltas cover the
arc's neighbourhood before the kill and the round is the image WIDTH's,
the nodes near the arc carrying arcs shorter than the widest. The
depth's node count against its predecessor's is the confined branching
b_r, so under the first reading r is about log(1/g)/log(b), a closed
form with no fitted constant.

THE SLATE, frozen before the engine. The instrument is the shipped
confined tree (explore_beta_delay.py BetaReader, explore_delay_sweep.py
x^2 + y and the five Pisot bases), run two ways at every one of the 30
beta pairs of the choice rig at L* - 1: the shipped certificate for the
kill round, and a breadth-first enumeration of the whole reachable
tree, every confined extension of every state and every legal child
kept, to the certificate's round, recording at every extension its v,
its W, its g and its legal-digit count. The round is recomputed from
the enumeration by minimax, death(node) = 1 + min over extensions of
max over legal children of death(child), an extension with no legal
child counting 0; the two rounds must agree. The float coordinate is
checked against the exact legality at every extension: the digits in
[v - (w - W), v] must be the engine's legal list.

P-A THE COORDINATE. The float legal list agrees with the exact one at
    every extension of every pair (a tie at the interval's end
    tolerated at 1e-9); the minimax round equals the certificate's at
    every killed pair.
P-B THE SPREAD. The realized deltas spread quasi-uniformly: the
    product G_r times the number of distinct deltas at depth r stays
    bounded (between 1 and about 5) as r grows at the deep pairs, and
    the distinct count grows geometrically at the confined branching.
P-C THE READING. TRANSPLANT from an earlier suspicion (the
    reachable remainders a digit-sum set over the shifts, an interval
    once the shifts' gap clears their span): the kill round equals the
    covering depth, within one, at most of the 25 killed pairs. The
    derivation's own reading: the round is at most the covering depth
    everywhere, and the deep kills (rounds 9 and 12) sit BELOW it,
    since a covering of a 0.027 share needs about 37 points on the
    circle and the confined branching near 1 supplies them slowly.
P-D THE ARC AT THE KILL. At the killing extension the node's own g is
    within a factor 2 of the depth's largest, the kill sitting where
    the adversary has drilled toward the map's corner; a kill at a
    node whose g is below half the depth's largest reads the width.

KILLS, frozen as what this rig PRINTS.

K1 THE CONTROL. The certificate's round differing from the record's at
   any of the golden x y at a = 1 (5), the Narayana divider at a = 1
   (5) and the plastic x y at a = 1 (12) -> nothing below is read.
K2 THE COORDINATE. Any extension whose float legal list differs from
   the exact one -> the coordinate is wrong.
K3 THE MINIMAX. The enumeration's minimax round differing from the
   certificate's at any killed pair whose enumeration reached the
   certificate's depth -> the enumeration is wrong.
K4 THE ORDER. A kill round above the covering depth at a pair where
   the killing node's g is the depth's largest -> the covering
   argument itself is wrong (a delta inside the arc at a node whose arc
   is the largest must be dead).
THE READING: the count of killed pairs with r = r_cov, r < r_cov and
r > r_cov, printed; and at each pair the ratio of the killing node's g
to the depth's largest.

POSITIVE CONTROL: K1, read before any other line.

FINDINGS (entered post-run; every number below sits in this file's
printed output).

F1 THE CONTROLS HOLD. Rounds 5, 5 and 12 at 626, 785 and 11,897
   confined nodes; K1 never fired.

F2 THE COORDINATE [property, checked]. The float legal list equals
   the exact one at all 2,375,984 extensions of the 30 pairs, and the
   enumeration's minimax round equals the certificate's at every one
   of the 21 killed pairs it reaches; K2 and K3 never fired. Four
   killed pairs are unread, their enumeration stopped by the 30 s
   wall or the 300,000-extension budget one to two depths short (the
   Narayana divider at a = 2, silver x^2 + y at a = 2, the plastic
   x^2 + y and divider at a = 1), and five pairs are unreached by the
   certificate as in the record.

F3 THE ARC OPENS LATE [observation at the 21 pairs]. The depth's
   largest arc g_max is 0 at every depth below an ARC-OPENING DEPTH:
   no confined node's image exceeds the zone until the adversary's
   boxes have shrunk toward the map's corner, where the box's average
   slope catches its sup. The plastic x y at a = 1 opens at depth 10
   (g_max 0.0027, then 0.0363 and 0.0616 at 11 and 12) and dies at
   12; the kill round is the opening depth at 7 pairs, one past it at
   10 and two past it at 4, never more (explore_arc_opening.py reads
   the opening with no tree, as a closed form, and the four pairs
   unread here, each at lag 1: 7, 14 and 4 of 25).

F4 THE READING [rule at the 21 pairs]. The kill round is never below
   the covering depth (0 of 21): it equals it at 13 pairs and is one
   past it at 8, and at all 8 the killing node's arc is below the
   depth's largest (g_kill/g_max 0.37 to 0.86), the width's and not
   the offsets'; K4 never fired. The transplant held at the letter
   (within one everywhere) and the derivation's own reading failed:
   no deep kill sits below the covering depth, because the covering
   is met within two depths of the opening (at the opening at 12
   pairs, one depth after at 8, two after at the golden x y at
   a = 1) -- the realized deltas' largest circle gap is under the
   widest arc almost as soon as an arc exists (0.0106 against 0.0363
   at the plastic x y's depth 11).

F5 THE SPREAD [observation]. The deltas are not uniform: G times the
   distinct count grows from about 1 at the first depths to 2 to 8 at
   the kill and 10.6 at the plastic x y's depth 9, the deltas
   clustering; the distinct count grows at 2.3 to 7.3 per round at
   the pairs killed at round 4 or later. The fitted-constant-free form
   log(1/g_max)/log(b) reads 0 to 3.4 against rounds 1 to 12 and is
   no fit.

VERDICT. In base beta the round is the WIDTH's: the dead arc does not
exist until the adversary's boxes are small enough for a node's own
image to exceed the zone, and once it exists the realized offsets
cover it within two rounds, the covering depth never after the kill
and the kill at most one round after the covering. The round's
variable is the arc-opening depth -- a property of the map's boxes
against the law's threshold and the base's grain, computable box by
box with no game -- plus a lag of 0 to 2 rounds, and not the offsets'
spread; the deep rounds of the plastic number are ten rounds of
drilling toward the corner and two of covering.

RUN RECORD: pure Python, the shipped engines imported; under memwatch,
peak commit 410 MB against the 512 MB default (the breadth-first tree
held whole for the minimax), wall 492 s at the budget 300,000
extensions and 30 s per certificate and per enumeration. Prints
reproduced by:
python prime/code/explore_reachable_offsets.py [NODE_BUDGET] [WALL_SECONDS]
"""
import math
import os
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import explore_beta_delay as bd                            # noqa: E402
import explore_delay_sweep as ds                           # noqa: E402

FAILS = []


def ok(cond, msg):
    if not cond:
        FAILS.append(msg)
        print("  KILL:", msg)


class Enumerator(bd.BetaReader):
    """The shipped reader, enumerated breadth-first with every legal
    child kept; records (v, W, g, nlegal) at every extension."""

    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)
        self.coord_fails = 0
        self.checked = 0

    def coordinate(self, us1, n1, q, t):
        B = self.B
        lo, hi = self.image(us1, n1)
        unit = B.fl ** (self.o - t - 1)
        d0 = self.digits[0]
        floor0 = B.ffloat(self.cell(self.child(q, d0), t + 1)[0])
        lof, hif = B.ffloat(lo), B.ffloat(hi)
        W = (hif - lof) / unit
        v = (lof - floor0) / unit + d0
        return v, W

    def enumerate(self, max_depth, budget, wall):
        """Levels of states (us, n, q, t); per level the extension
        records; returns (levels, ext_records, truncated_depth)."""
        t_end = time.time() + wall
        root = ((self.B.zero,) * self.d, 0, self.B.zero, 0)
        level = [root]
        # tree for minimax: ext_children[k] = list over level-k states of
        # list over extensions of list of child indices in level k+1
        tree = []
        recs = []
        w = self.wf
        for depth in range(1, max_depth + 1):
            nxt = []
            ext_lists = []
            rec = []
            for (us, n, q, t) in level:
                n1 = max(0, t + 1 + self.c)
                exts = []
                for us1 in self.extend(us, n, n1):
                    self.nodes += 1
                    if self.nodes > budget or time.time() > t_end:
                        return level, tree, recs, depth - 1
                    legal = [p for p in self.digits if self.legal(us1, n1, self.child(q, p), t + 1)]
                    v, W = self.coordinate(us1, n1, q, t)
                    room = w - W
                    flegal = [p for p in self.digits if v - room - 1e-9 <= p <= v + 1e-9]
                    self.checked += 1
                    if flegal != legal:
                        self.coord_fails += 1
                    g = W - (w - 1)
                    rec.append((v, W, g, len(legal)))
                    kids = []
                    for p in legal:
                        kids.append(len(nxt))
                        nxt.append((us1, n1, self.child(q, p), t + 1))
                    exts.append(kids)
                ext_lists.append(exts)
            tree.append(ext_lists)
            recs.append(rec)
            level = nxt
            if not level:
                break
        return level, tree, recs, max_depth


def minimax_round(tree):
    """death(node) = 1 + min over extensions of max over children of
    death(child); a frontier node is alive (inf)."""
    INF = float("inf")
    depth = len(tree)
    nxt_vals = None
    for k in range(depth - 1, -1, -1):
        vals = []
        for exts in tree[k]:
            best = INF
            for kids in exts:
                if not kids:
                    m = 0
                else:
                    m = max(nxt_vals[i] if nxt_vals is not None else INF for i in kids)
                best = min(best, m)
            vals.append(1 + best if best != INF else INF)
        nxt_vals = vals
    return nxt_vals[0] if nxt_vals else None


def depth_stats(rec, a):
    """At one depth: the circle gaps of the deltas over killable nodes,
    the arcs, the deaths."""
    deltas = []
    gmax = 0.0
    dead = []
    for v, W, g, nl in rec:
        gmax = max(gmax, g)
        top = math.ceil(v - 1e-12)
        if top > a:
            continue
        delta = top - v
        deltas.append(delta)
        if nl == 0:
            dead.append((delta, g))
    ds_ = sorted(set(round(x, 12) for x in deltas))
    if len(ds_) >= 2:
        G = max(max(b - a_ for a_, b in zip(ds_, ds_[1:])), ds_[0] + 1 - ds_[-1])
    elif len(ds_) == 1:
        G = 1.0
    else:
        G = None
    minpos = min((x for x in deltas if x > 1e-12), default=None)
    return dict(n=len(rec), killable=len(deltas), distinct=len(ds_), G=G, gmax=gmax,
                minpos=minpos, dead=dead)


def run_pair(B, fmap, a, budget, wall, max_rounds=14):
    L, _, _ = bd.law_L(B, fmap, a)
    o = bd.least_lead(B, fmap, a)
    rd = bd.BetaReader(B, fmap, L - 1 - o, o, a=a)
    t1 = time.time()
    r, depth = rd.certificate(budget, wall=wall, max_rounds=max_rounds, confined=True)
    cert_secs = time.time() - t1
    en = Enumerator(B, fmap, L - 1 - o, o, a=a)
    en.confined = True
    en.budget = budget
    target = r if r is not None else min(depth + 1, max_rounds)
    t2 = time.time()
    _, tree, recs, reached = en.enumerate(target, budget, wall)
    mm = minimax_round(tree) if tree else None
    return dict(L=L, o=o, r=r, depth=depth, cert_nodes=rd.nodes, cert_secs=cert_secs,
                enum_nodes=en.nodes, enum_secs=time.time() - t2, reached=reached, target=target,
                mm=mm, recs=recs, coord_fails=en.coord_fails, checked=en.checked, a=a)


def read_pair(label, res):
    a = res['a']
    stats = [depth_stats(rec, a) for rec in res['recs']]
    r_cov = None
    r_open = None
    lines = []
    prev = None
    for k, s in enumerate(stats, 1):
        cover = s['G'] is not None and s['G'] < s['gmax']
        if cover and r_cov is None:
            r_cov = k
        if s['gmax'] > 0 and r_open is None:
            r_open = k
        b = f"{s['n'] / prev:.2f}" if prev else "-"
        prev = s['n']
        Gs = f"{s['G']:.4f}" if s['G'] is not None else "-"
        GN = f"{s['G'] * s['distinct']:.2f}" if s['G'] is not None else "-"
        mp = f"{s['minpos']:.4f}" if s['minpos'] is not None else "-"
        ratio = f"{s['minpos'] / s['gmax']:.2f}" if s['minpos'] is not None and s['gmax'] > 0 else "-"
        dead = ""
        if s['dead']:
            dg = max(g for _, g in s['dead'])
            dead = f" DEAD x{len(s['dead'])} g_kill/g_max {dg / s['gmax']:.2f}"
        lines.append(f"    r={k:2d} ext {s['n']:6d} b {b:>5} killable {s['killable']:6d} distinct {s['distinct']:6d} "
                     f"G {Gs} G*N {GN} g_max {s['gmax']:.4f} min delta+ {mp} /g_max {ratio}"
                     f"{' COVER' if cover else ''}{dead}")
    return stats, r_cov, r_open, lines


def main():
    budget = int(sys.argv[1]) if len(sys.argv) > 1 else 300_000
    wall = float(sys.argv[2]) if len(sys.argv) > 2 else 30.0
    t0 = time.time()
    print(f"THE REACHABLE OFFSETS: budget {budget} nodes, wall {wall:.0f}s per pair and per enumeration")

    print("\n=== K1 THE CONTROLS (the record's rounds: golden x y a=1: 5, Narayana divider a=1: 5, "
          "plastic x y a=1: 12)")
    bases = {B.name.split()[0]: B for B in ds.beta_bases()}
    controls = {("golden", "x y", 1): 5, ("Narayana", "x/(M + 1 + y)", 1): 5, ("plastic", "x y", 1): 12}
    rows = []
    for B in ds.beta_bases():
        for a in (1, 2):
            for fmap in ds.beta_maps(B, a):
                key = (B.name.split()[0], fmap.name, a)
                if key in controls:
                    res = run_pair(B, fmap, a, budget, max(wall, 60.0))
                    print(f"  {key[0]} {fmap.name} a={a}: certificate {'dead r=' + str(res['r']) if res['r'] is not None else 'UNREACHED'} "
                          f"{res['cert_nodes']} nodes {res['cert_secs']:.1f}s")
                    ok(res['r'] == controls[key], f"K1 {key}: round {res['r']} against the record's {controls[key]}")
                    rows.append((key, B, fmap, res))
    if FAILS:
        print("\nCONTROL FAILED; nothing below is read.")
        return

    print("\n=== THE 30 BETA PAIRS at L* - 1: the certificate, the enumeration, the minimax round")
    for B in ds.beta_bases():
        for a in (1, 2):
            for fmap in ds.beta_maps(B, a):
                key = (B.name.split()[0], fmap.name, a)
                done = [r for r in rows if r[0] == key]
                if done:
                    res = done[0][3]
                else:
                    res = run_pair(B, fmap, a, budget, wall)
                    rows.append((key, B, fmap, res))
                label = f"{key[0]} {fmap.name} a={a}"
                cert = f"dead r={res['r']}" if res['r'] is not None else f"UNREACHED [{res['depth']}]"
                mm = res['mm']
                mms = f"{mm}" if mm not in (None, float('inf')) else "alive"
                print(f"  {label}: L*={res['L']} o={res['o']} certificate {cert} ({res['cert_nodes']} nodes) | "
                      f"enumeration to depth {res['reached']} of {res['target']}, {res['enum_nodes']} extensions "
                      f"{res['enum_secs']:.1f}s, minimax round {mms} | coordinate checks {res['checked']}, "
                      f"disagreements {res['coord_fails']}")
                ok(res['coord_fails'] == 0, f"K2 {label}: {res['coord_fails']} float legal lists differ from the exact")
                if res['r'] is not None and res['reached'] >= res['r']:
                    ok(mm == res['r'], f"K3 {label}: minimax round {mm} against the certificate's {res['r']}")

    print("\n=== THE OFFSETS BY DEPTH at every pair: extensions, branching b, killable nodes, distinct deltas,\n"
          "    largest circle gap G, G times the distinct count, the depth's largest arc g_max,\n"
          "    the least positive delta and its ratio to g_max; COVER marks G < g_max, DEAD a killed node")
    summary = []
    for key, B, fmap, res in rows:
        label = f"{key[0]} {fmap.name} a={key[2]}"
        stats, r_cov, r_open, lines = read_pair(label, res)
        print(f"  {label}: round {res['r']}, covering depth {r_cov}, arc-opening depth {r_open}")
        for ln in lines:
            print(ln)
        if res['r'] is not None and res['reached'] >= res['r']:
            s = stats[res['r'] - 1]
            gk = max((g for _, g in s['dead']), default=0.0)
            summary.append((label, res['r'], r_cov, gk / s['gmax'] if s['gmax'] > 0 else 0.0,
                            s['distinct'], s['gmax'], stats, r_open))

    print("\n=== THE READING: the kill round against the covering depth and the arc-opening depth\n"
          "    (the first depth at which any node's own excess is positive) over the killed pairs")
    eq = below = above = 0
    lag = {}
    for label, r, r_cov, gratio, distinct, gmax, stats, r_open in sorted(summary, key=lambda t: t[1]):
        lag[r - r_open] = lag.get(r - r_open, 0) + 1
        if r_cov is None:
            rel = "r < r_cov (never covered)"
            below += 1
        elif r == r_cov:
            rel = "r = r_cov"
            eq += 1
        elif r < r_cov:
            rel = "r < r_cov"
            below += 1
        else:
            rel = "r > r_cov"
            above += 1
            ok(gratio < 1 - 1e-9, f"K4 {label}: round {r} above the covering depth {r_cov} with the killing arc the largest")
        # the confined branching over the depths and the closed form log(1/g)/log(b)
        n1, nr = stats[0]['n'], stats[r - 1]['n']
        b = (nr / n1) ** (1 / (r - 1)) if r > 1 and n1 else float('nan')
        pred = math.log(1 / gmax) / math.log(b) if b > 1 and gmax > 0 else float('nan')
        gn = max(x['G'] * x['distinct'] for x in stats if x['G'] is not None)
        print(f"  round {r:2d} cover {str(r_cov):>4} open {r_open:2d} {rel:28s} g_kill/g_max {gratio:.2f} "
              f"distinct {distinct:6d} g_max {gmax:.4f} G*N max {gn:5.2f} b {b:.2f} "
              f"log(1/g)/log(b) {pred:5.1f}  {label}")
    print(f"  killed pairs read: {len(summary)}; r = r_cov at {eq}, r < r_cov at {below}, r > r_cov at {above}")
    print(f"  round minus arc-opening depth, pairs by lag: {sorted(lag.items())}")
    print(f"  coordinate checks over every pair: {sum(res['checked'] for _, _, _, res in rows)}, "
          f"disagreements {sum(res['coord_fails'] for _, _, _, res in rows)}")

    print(f"\nwall {time.time() - t0:.0f}s; {'ALL KILLS MISSED' if not FAILS else str(len(FAILS)) + ' KILL(S) FIRED'}")


if __name__ == "__main__":
    main()
