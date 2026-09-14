"""Does the reader ever have a choice at a killing box in base beta: is
the kill round below the margin law's L* delayed by the reader's
strategy, or by the adversary's search for a small excess?

THE QUESTION. Off the contiguous digit sets the margin law's delay is a
rule without its necessity proof, and the record reads the growing kill
round -- 1 to 3 at the contiguous integer cells, 4 to 12 in base beta
over {-a, ..., a} -- as the reader's strategy delaying the kill: two
legal parents of one image can disagree about death, so the reader
steers. But a parent is only worth steering toward if the reader can
CHOOSE it. Write the game in one coordinate: in the cell units of output
depth t let W be the image's width, w the cell's, l = w - W the room and
xi in [0, l] the image's offset above its cell's floor. A round: the
adversary picks the sub-image's offset s in [0, beta W - W'] inside the
scaled image, v = -a + beta xi + s; the reader picks a digit d with
v - l' <= d <= v (the image then fits the child beta q + d), and the new
offset is xi' = v - d. Death iff no digit lies in [v - l', v]. The
reader's options are the digits within l' below v, at most
floor(l'/g_min) + 1 of them, and at a contiguous digit set g_min = 1: a
box whose image is wider than the zone has l' < 1 and admits AT MOST ONE
legal digit. So at every box that can kill, in base beta as at an
integer radix, the reader's move is forced; a choice exists only at
boxes whose image is no wider than the zone, which cannot kill (a kill
is strict containment) and whose descendants inherit the choice's
one-digit offset multiplied by beta. Whether those choices buy rounds
is the third arm: the same tree with the choice removed.
The kill round then measures the adversary's search, not the reader's
play: the confined adversary keeps only the sub-boxes whose width rate
clears the law's threshold (the corner digits at x y, one or two a
step), a near-deterministic drift that must land the image's offset in
a dead arc whose length is the EXCESS g = W - (w - 1), and at L* - 1
the ceiling puts g anywhere in (0, (beta - 1)(w - 1)]: the excess's
share of the zone is at most beta - 1 -- 0.32 at the plastic number,
0.62 at the golden mean, 1.41 at the silver mean -- so the plastic
number's arcs are small by the grain of its base, before any strategy.

THE SLATE, frozen before the engine. The instrument is the shipped
confined tree (explore_beta_delay.py's reader, explore_delay_sweep.py's
x^2 + y), run at L* - 1 at every pair of the five Pisot bases, the two
digit radii a in {1, 2} and the three maps x y, x^2 + y and the divider
at P = 1, with two counters at every node the tree visits: the number of
legal reader digits, and whether the image is wider than the zone
(floats, a tie counted apart). The third arm is the PUPPET: the same
tree with the reader's list of legal digits cut to its lowest member,
and again to its highest, so every choice is gone and the kill round is
the adversary's search alone. Two integer controls, radix 2 over
{-1, 0, 1} and radix 3 over {-2, 0, 1, 2}'s contiguous cousin {-2..2},
where the theorem itself says the reader has no strategy.

P-A THE FORCED MOVE. At every node whose image is wider than the zone,
    the legal-digit count is 1 (or 0 at the kill): a property by the
    derivation above, printed as the count of nodes with two or more
    legal digits at a wide image, 0 at every pair; at an integer radix
    the tie (image exactly the zone) is exact in floats and admits two.
P-B THE NARROW CHOICE. Nodes with two legal digits exist, all at images
    no wider than the zone; the derivation's own reading: at some pairs
    they are a visible share of the tree, since the excess region is a
    rate bound and the actual image can sit below it.
P-D THE PUPPET. TRANSPLANT from the record's reading: the puppet dies
    earlier than the free reader at the deep pairs, the choice at the
    narrow boxes being what delays the kill. The derivation's own
    reading: the same round at every killed pair -- a choice at a box
    that cannot kill only re-offsets the drift, and the adversary's
    search finds the arc at the same depth either way.
P-C THE EXCESS AND THE ROUND. Over the killed pairs the kill round falls
    as the relative excess g/(w - 1) at L* - 1 grows: the rank
    correlation between the two is negative, and the deepest kills sit
    at the smallest excesses. TRANSPLANT from the record: the plastic
    x y at a = 1 is the deepest kill; the derivation's own reading puts
    it among the three smallest excesses.

KILLS, frozen as what this rig PRINTS.

K1 THE CONTROL. The instrumented tree's kill round differing from the
   record's at any of the golden x y at a = 1 (round 5), the Narayana
   divider at a = 1 (round 5) and the plastic x y at a = 1 (round 12)
   -> nothing below is read.
K2 THE FORCED MOVE. Any node with two or more legal digits at an image
   at least as wide as the zone -> the one-coordinate derivation is
   wrong and the record's strategy reading stands.
K3 THE RANK. The rank correlation between the relative excess and the
   kill round printing at or above 0 over the killed pairs -> the
   excess is not what the round counts.
K4 THE PUPPET. Either puppet's kill round below the free reader's at
   any killed pair -> the choice at the narrow boxes delays the kill,
   and the record's reading stands, scoped to those boxes.

POSITIVE CONTROL: K1, read before any other line.

FINDINGS (entered post-run; every number below sits in this file's
printed output).

F1 THE CONTROLS HOLD. Rounds 5, 5 and 12 at 626, 785 and 11,897
   confined nodes, the record's rounds; K1 never fired.

F2 THE FORCED MOVE [property, checked over 1.4 million nodes]. At every
   node of every pair whose image is wider than the zone the legal-digit
   count is 1, or 0 at the kill: 0 nodes with two at a wide image over
   the 30 beta pairs and the four integer controls. The tie is exact at
   an integer radix and admits two: 16 nodes at radix 2 x y, 4 at its
   divider, none in base beta.

F3 THE NARROW CHOICE [observation]. Two or more legal digits at 28 of
   the 30 beta pairs, every one at an image no wider than the zone,
   from 1 percent of a tree (silver x^2 + y at a = 2, 300 of 30,986
   nodes) to 92 percent (Narayana x y at a = 2, 2,434 of 2,639), up to
   four digits at a = 2; none at silver x y and the silver divider at
   a = 1, where every node's image is wide.

F4 THE PUPPET [rule at the 24 decided pairs]. Both puppets die at the
   free reader's round at 23 of 24, at the same node count or within a
   third of it, and one round earlier at one, the plastic x^2 + y at
   a = 1 (round 4 against 5, 6,277 and 7,282 nodes against 25,591);
   the Narayana divider at a = 2 is unreached by both puppets at the
   halved wall. K4 fired at that one pair and nowhere else: the choice
   at the narrow boxes buys a round there and nothing at the rest.

F5 THE EXCESS AND THE ROUND. The rank correlation between the excess's
   share of the zone at L* - 1 and the kill round is -0.732 over the 25
   killed pairs; the deepest kills are the plastic x y at a = 1
   (share 0.027, round 12), the plastic divider at a = 1 (0.194, round
   9) and the Narayana divider at a = 2 (0.299, round 6); the smallest
   shares are silver x^2 + y at a = 2 (0.016, round 5), the plastic
   x y at a = 1 and golden x y at a = 1 (0.106, round 5). The
   transplant held; K3 never fired. The excess sorts the rounds and is
   not a function of them: a share of 0.194 kills at rounds 5 and 9,
   and the smallest share of all kills at round 5.

VERDICT. Below the margin law's L*, at a contiguous digit set in base
beta as at an integer radix, the reader's move is forced at every box
that can kill and free only at boxes it cannot die at; removing that
freedom leaves the kill round unchanged at 23 of 24 decided pairs and
costs one round at one. The kill round is the adversary's search for a
dead arc whose length is the excess -- falling as the excess's share of
the zone grows, a share the base's grain caps at beta - 1 -- and not the
reader's play; the "strategy" the record read into the growing round is
the small arc of a fine base. Necessity in base beta is the statement
that the forced remainder recursion reaches an arc for every non-affine
map, with the reader's narrow-box choices a perturbation worth at most
one round where it is worth anything.

RUN RECORD: pure Python, the shipped engines imported; under memwatch,
peak commit 41 MB against the 512 MB default, wall 168 s at the pair
budget 300,000 nodes and 20 s per pair, the puppets at 10 s. Prints
reproduced by:
python prime/code/explore_delay_choice.py [NODE_BUDGET] [WALL_SECONDS]
"""

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


class CountingReader(bd.BetaReader):
    """The shipped reader with two counters at every visited node: the
    legal-digit count and whether the image is at least the zone."""

    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)
        self.hist = {}          # (nlegal, wide) -> nodes; wide in {"wide", "narrow", "tie"}
        self.max_legal = 0

    def zone_and_width(self, us1, n1, q, t):
        B = self.B
        lo, hi = self.image(us1, n1)
        width = B.ffloat(hi) - B.ffloat(lo)
        d = self.digits[0]
        bot = self.cell(self.child(q, d + 1), t + 1)[0]
        top = self.cell(self.child(q, d), t + 1)[1]
        zone = B.ffloat(top) - B.ffloat(bot)
        return width, zone

    def survives(self, us, n, q, t, rounds):
        if rounds == 0:
            return True
        n1 = max(0, t + 1 + self.c)
        for us1 in self.extend(us, n, n1):
            self.nodes += 1
            if self.nodes > self.budget or time.time() > self.t_end:
                raise bd.Budget()
            legal = [p for p in self.digits if self.legal(us1, n1, self.child(q, p), t + 1)]
            width, zone = self.zone_and_width(us1, n1, q, t)
            rel = (width - zone) / zone
            kind = "tie" if abs(rel) < 1e-9 else ("wide" if rel > 0 else "narrow")
            key = (len(legal), kind)
            self.hist[key] = self.hist.get(key, 0) + 1
            self.max_legal = max(self.max_legal, len(legal))
            alive = False
            for p in legal:
                if self.survives(us1, n1, self.child(q, p), t + 1, rounds - 1):
                    alive = True
                    break
            if not alive:
                return False
        return True


class PuppetLow(CountingReader):
    """The reader with its choice removed: the lowest legal digit."""
    pick = staticmethod(lambda legal: legal[:1])

    def survives(self, us, n, q, t, rounds):
        if rounds == 0:
            return True
        n1 = max(0, t + 1 + self.c)
        for us1 in self.extend(us, n, n1):
            self.nodes += 1
            if self.nodes > self.budget or time.time() > self.t_end:
                raise bd.Budget()
            legal = self.pick([p for p in self.digits if self.legal(us1, n1, self.child(q, p), t + 1)])
            if not any(self.survives(us1, n1, self.child(q, p), t + 1, rounds - 1) for p in legal):
                return False
        return True


class PuppetHigh(PuppetLow):
    """The reader with its choice removed: the highest legal digit."""
    pick = staticmethod(lambda legal: legal[-1:])


def run_pair(B, fmap, a, budget, wall, max_rounds=14, cls=None):
    L, _, _ = bd.law_L(B, fmap, a)
    o = bd.least_lead(B, fmap, a)
    rd = (cls or CountingReader)(B, fmap, L - 1 - o, o, a=a)
    M = rd.Mf
    w = rd.wf
    lam = B.ffloat(fmap.lam((rd.aone, B.bm1)))
    excess = lam * w / (B.fl ** (L - 1) * (w - 1)) - 1
    t1 = time.time()
    r, depth = rd.certificate(budget, wall=wall, max_rounds=max_rounds, confined=True)
    secs = time.time() - t1
    two_wide = sum(v for (k, kind), v in rd.hist.items() if k >= 2 and kind == "wide")
    two_tie = sum(v for (k, kind), v in rd.hist.items() if k >= 2 and kind == "tie")
    two_narrow = sum(v for (k, kind), v in rd.hist.items() if k >= 2 and kind == "narrow")
    wide = sum(v for (k, kind), v in rd.hist.items() if kind == "wide")
    return dict(L=L, o=o, r=r, depth=depth, nodes=rd.nodes, secs=secs, excess=excess,
                two_wide=two_wide, two_tie=two_tie, two_narrow=two_narrow, wide=wide,
                max_legal=rd.max_legal, hist=rd.hist)


def fmt(res):
    verdict = f"dead r={res['r']}" if res['r'] is not None else f"UNREACHED [{res['depth']}]"
    return (f"L*={res['L']} o={res['o']} at L*-1: {verdict} {res['nodes']} nodes {res['secs']:.1f}s | "
            f"excess/zone {res['excess']:.3f} | 2+ legal at wide {res['two_wide']}, at tie "
            f"{res['two_tie']}, at narrow {res['two_narrow']} | wide nodes {res['wide']} | "
            f"max legal {res['max_legal']}")


def spearman(xs, ys):
    def ranks(v):
        order = sorted(range(len(v)), key=lambda i: v[i])
        rk = [0.0] * len(v)
        i = 0
        while i < len(order):
            j = i
            while j + 1 < len(order) and v[order[j + 1]] == v[order[i]]:
                j += 1
            for k in range(i, j + 1):
                rk[order[k]] = (i + j) / 2 + 1
            i = j + 1
        return rk
    rx, ry = ranks(xs), ranks(ys)
    n = len(xs)
    mx, my = sum(rx) / n, sum(ry) / n
    num = sum((a - mx) * (b - my) for a, b in zip(rx, ry))
    den = (sum((a - mx) ** 2 for a in rx) * sum((b - my) ** 2 for b in ry)) ** 0.5
    return num / den if den else 0.0


def main():
    budget = int(sys.argv[1]) if len(sys.argv) > 1 else 300_000
    wall = float(sys.argv[2]) if len(sys.argv) > 2 else 20.0
    t0 = time.time()
    print(f"THE READER'S CHOICE AT A KILLING BOX: budget {budget} nodes, wall {wall:.0f}s per pair")

    print("\n=== K1 THE CONTROLS (the record's rounds: golden x y a=1: 5, Narayana divider a=1: 5, "
          "plastic x y a=1: 12)")
    bases = {B.name.split()[0]: B for B in ds.beta_bases()}
    controls = [("golden", lambda B: bd.BProduct(B), 1, 5),
                ("Narayana", lambda B: bd.BDivision(B, 1, 1, 1), 1, 5),
                ("plastic", lambda B: bd.BProduct(B), 1, 12)]
    for bname, mk, a, want in controls:
        B = bases[bname]
        res = run_pair(B, mk(B), a, budget, max(wall, 60.0))
        print(f"  {bname} {mk(B).name} a={a}: {fmt(res)}")
        ok(res['r'] == want, f"K1 {bname} {mk(B).name} a={a}: round {res['r']} against the record's {want}")
    if FAILS:
        print("\nCONTROL FAILED; nothing below is read.")
        return

    print("\n=== THE INTEGER CONTROLS: contiguous cells where the theorem says the reader has no strategy")
    for coeffs, name, a in (((2,), "radix 2", 1), ((3,), "radix 3", 2)):
        B = bd.Base(name, coeffs)
        for fmap in (bd.BProduct(B), bd.BDivision(B, 1, 1, a)):
            res = run_pair(B, fmap, a, budget, wall)
            print(f"  {name} {fmap.name} a={a}: {fmt(res)}")
            ok(res['two_wide'] == 0, f"K2 {name} {fmap.name} a={a}: {res['two_wide']} nodes with 2+ legal digits at a wide image")

    print("\n=== THE BETA PAIRS at L* - 1, confined")
    rows = []
    for B in ds.beta_bases():
        for a in (1, 2):
            for fmap in ds.beta_maps(B, a):
                res = run_pair(B, fmap, a, budget, wall)
                label = f"{B.name.split()[0]} {fmap.name} a={a}"
                print(f"  {label}: {fmt(res)}")
                ok(res['two_wide'] == 0, f"K2 {label}: {res['two_wide']} nodes with 2+ legal digits at a wide image")
                rows.append((label, res))

    print("\n=== P-B THE NARROW CHOICE: pairs with any two-digit node, and its share of the tree")
    for label, res in rows:
        if res['two_narrow']:
            print(f"  {label}: {res['two_narrow']} of {res['nodes']} nodes ({100 * res['two_narrow'] / res['nodes']:.1f}%), "
                  f"histogram {sorted(res['hist'].items())}")
    print(f"  pairs with a two-digit node: {sum(1 for _, r in rows if r['two_narrow'])} of {len(rows)}; "
          f"nodes with 2+ legal digits at a wide or tied image over every pair: {sum(r['two_wide'] for _, r in rows)}")

    print("\n=== P-D THE PUPPET: the free reader's round against the readers with the choice removed")
    for B in ds.beta_bases():
        for a in (1, 2):
            for fmap in ds.beta_maps(B, a):
                label = f"{B.name.split()[0]} {fmap.name} a={a}"
                free = dict(rows)[label]
                if free['r'] is None:
                    continue
                lo = run_pair(B, fmap, a, budget, wall / 2, cls=PuppetLow)
                hi = run_pair(B, fmap, a, budget, wall / 2, cls=PuppetHigh)

                def verdict(r):
                    return f"dead r={r['r']}" if r['r'] is not None else f"UNREACHED [{r['depth']}]"
                print(f"  {label}: free round {free['r']} ({free['nodes']} nodes) | lowest-digit puppet {verdict(lo)} "
                      f"({lo['nodes']}) | highest-digit puppet {verdict(hi)} ({hi['nodes']})")
                for name, res in (("lowest", lo), ("highest", hi)):
                    ok(res['r'] is None or res['r'] >= free['r'],
                       f"K4 {label}: the {name}-digit puppet dies at round {res['r']} below the free reader's {free['r']}")

    print("\n=== P-C THE EXCESS AND THE ROUND, killed pairs sorted by the excess's share of the zone")
    killed = [(label, res) for label, res in rows if res['r'] is not None]
    for label, res in sorted(killed, key=lambda t: t[1]['excess']):
        print(f"  {res['excess']:.3f}  round {res['r']:2d}  {res['nodes']:8d} nodes  {label}")
    for label, res in rows:
        if res['r'] is None:
            print(f"  {res['excess']:.3f}  UNREACHED [{res['depth']}]  {res['nodes']:8d} nodes  {label}")
    xs = [res['excess'] for _, res in killed]
    ys = [res['r'] for _, res in killed]
    rho = spearman(xs, ys)
    print(f"  rank correlation (excess, round) over {len(killed)} killed pairs: {rho:+.3f}")
    ok(rho < 0, f"K3 rank correlation {rho:+.3f} at or above 0")
    deepest = sorted(killed, key=lambda t: -t[1]['r'])[:3]
    smallest = sorted(killed, key=lambda t: t[1]['excess'])[:3]
    print(f"  deepest kills: {[l for l, _ in deepest]}")
    print(f"  smallest excesses: {[l for l, _ in smallest]}")

    print(f"\nwall {time.time() - t0:.0f}s; {'ALL KILLS MISSED' if not FAILS else str(len(FAILS)) + ' KILL(S) FIRED'}")


if __name__ == "__main__":
    main()
