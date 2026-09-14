"""The wide sweep off the contiguous sets: does any pair of a digit set
with interval tails and a non-affine map read below the margin law's
L*, once the confined tree can reach round 6 at every pair?

THE QUESTION. Off the contiguous digit sets the margin law's delay
holds as a rule without its proof: at the radix-3 gap sets x y and the
divider die at L* - 1 at all 28 pairs (explore_gap_lattice.py,
explore_beta_delay.py) and in base beta over {-1, 0, 1} at the golden
mean and the Narayana root the four pairs die at rounds 4 and 5. The
reader has a strategy at every one of these, and the only kill shape
left to the law is a pair where that strategy buys a whole digit -- the
tree alive at L* - 1 past the rounds every kill so far has needed. The
confined tree (the adversary restricted to the excess region, sound
both ways) reaches round 5 in under 800 nodes where the full tree spent
millions, so a sweep an order of magnitude wider than the record's
costs minutes: more maps at the gap sets, more bases and a wider digit
set in beta.

THE DERIVATION, written before the engine. At an integer radix within
[-3, 3], a set with two gap sizes and a least zone above 0 exists only
at radix 3 (radix 4's four interval sets all touch, and at radix 5 a
positive least zone needs a hull width above 2, a span above 8, beyond
the box), so the integer arm is radix 3's fourteen sets at the map the
record has not read there, x^2 + y (Lam = 2 max|x| + 1, its box image
[min x^2 + y_lo, max x^2 + y_hi] with the minimum 0 across a box
holding 0). In base beta over {-a, ..., a}, M = a/(beta - 1), the
tails are an interval iff beta - 1 <= 2a, the zone is w - 1 = 2M - 1,
and the law reads beta^L (2M - 1) >= Lam 2M; a = 2 is legal at every
base here and doubles the moves per step to 25. THE BASES beyond the
record's two: the silver mean x^2 = 2x + 1 (2.414, above 2, so at a = 1
the hull is narrow, M = 0.707, and the zone 0.414), the tribonacci
root x^3 = x^2 + x + 1 (1.839) and the plastic number x^3 = x + 1
(1.3247, the least Pisot number, M = 3.08 at a = 1). Every base is a
unit (constant term +-1), so nothing here depends on that: the engine
carries fractions of elements. The kill rounds at the record's pairs
were 4 and 5 where the contiguous sets' were read as 1 to 4 (a
transplant from the gap sets' range; the contiguous arm, F6, prints
1 to 3); a state-dependent
set delays the kill because the reader steers between misaligned
parents, and the delay should grow with the number of legal parents an
image typically has, which grows with a (more redundancy) and shrinks
with beta - 1 (a wider hull at a fixed a).

THE SLATE, frozen before the engine. Integer arm: the fourteen radix-3
sets of positive least zone, x^2 + y at L* - 1 (the generalized law
with Lam = 2 max(a-, a+)/(b - 1) + 1). Beta arm: the five bases, a in
{1, 2}, the maps x y, x^2 + y and the divider at P = 1, at L* - 1.
Every pair under the confined tree with a node budget and a wall cap
per pair, iterative deepening to round 6; a pair the budget stops is
UNREACHED, never alive.

P-A THE CONTROLS. The confined tree reproduces the record's rounds:
    x y at the golden mean, a = 1, L = 3, round 5; the divider at the
    Narayana root, a = 1, L = 3, round 5; x y at radix 3 over
    {-3, -1, 0, 1, 2}, L = 2, round 4.
P-B THE INTEGER ARM. TRANSPLANT from x y and the divider: x^2 + y dead
    at L* - 1 at all fourteen sets, rounds 1 to 5.
P-C THE BETA ARM. TRANSPLANT: dead at L* - 1 at all 30 pairs, the
    rounds 1 to 6. The derivation's own reading: the round grows with
    a and falls with beta - 1, the deepest kills at the plastic number
    at a = 2, and if any pair is alive to round 6 it is there.
P-D THE ROUNDS. The distribution of kill rounds over the sweep against
    the contiguous 1..4: some mass at 5 and, if P-C's reading holds, a
    round-6 kill; a pair unreached at the budget is printed as such.

KILLS, frozen as what this rig PRINTS.

K1 THE CONTROLS. Any of P-A's three rounds differing from the record's
   -> nothing below is read.
K2 THE STATE LEMMA. At any node, "no legal child" disagreeing with
   "the image strictly contains a zone".
K3 THE TAILS. A base-and-a pair whose tails are not an interval run
   anyway (the engine's zone would be wrong).
THE LINE'S KILL: a pair alive at L* - 1 through round 6 (the confined
tree completing round 6 with the reader surviving), printed as ALIVE;
an UNREACHED pair is the budget's and decides nothing.

POSITIVE CONTROL: K1, read before any other line.

FINDINGS (entered post-run; every number below sits in this file's
printed output).

F1 THE CONTROLS HOLD: rounds 5, 5 and 4 as recorded; x^2 + y's range
   top and the divider's pole offset at a = 2 equal M^2 + M and M + 1.
   K2 never fired.

F2 THE INTEGER ARM [rule at the 14 sets]. x^2 + y dead at L* - 1 at
   every radix-3 set of positive least zone, rounds 1 (11 sets), 2
   (2) and 3 (1), the kills at 4 to 512 nodes.

F3 THE BETA ARM [rule at 27 of the 30 pairs; three unreached]. Dead at
   L* - 1 at every pair the tree reached: rounds 1 to 6 at the golden
   mean, the Narayana root, the silver mean and the tribonacci root
   (the Narayana divider at a = 2 at round 6, 108,761 nodes); at the
   plastic number x y at a = 1 at ROUND 12 (11,897 confined nodes,
   where the tree to round 6 held 176 and the full tree survived two
   rounds at 369,185) and the divider at a = 1 at round 9 (44,497),
   x^2 + y at a = 1 at round 5. THE LINE'S KILL FIRED ON ITS LETTER at
   five pairs -- alive through round 6 -- and the deep certificate
   killed two of them: the frozen bar of six rounds was a transplant
   from bases where the kills sit at 1 to 6, and at the plastic number
   the reader's strategy delays the kill to 9 and 12 rounds without
   escaping it. Alive at the 60 s cap, unreached: x^2 + y at the
   Narayana root, a = 1 (round 7 completed, 670,785 nodes), and at the
   plastic number a = 2 both x y (round 8, 342,237) and the divider
   (round 7, 428,992); x^2 + y at a = 2 unreached at the Narayana root
   (round 4) and the plastic number (round 3). Every unreached pair
   survived the full tree to its budget, so the confinement was never
   falsified (K-check at each alive pair). The descent: one L below,
   every alive pair dies -- the plastic x y at a = 1 at round 4 at
   L = 6, at a = 2 at round 4 at L = 8, the divider at a = 1 at round
   6 at L = 4, at a = 2 at round 4 at L = 4 (L = 5 and 6 unreached) --
   so the strategy buys nothing where the tree reached, at most one L
   at every unreached pair but the plastic divider at a = 2, and at
   most three there.

F4 THE ROUNDS. Over the 44 pairs read: 1 at 13, 2 at 10, 3 at 2, 4 at
   4, 5 at 7, 6 at 1, 9 at 1, 12 at 1, against the contiguous 1 to 3
   (F6);
   the round grows with the redundancy -- with a at a fixed base
   (silver x^2 + y from 1 to 5) and as beta - 1 falls (the plastic
   number's 9 and 12) -- as the derivation's own reading said, and the
   deepest kills sit at the plastic number, though at a = 1 and not
   at a = 2, where the tree is unreached.

F5 THE UNREACHED PASS (--deepen, 300 s per pair). x^2 + y at the
   Narayana root, a = 1, dies at round 9 (1,053,162 nodes, 90 s); x y
   at the plastic number, a = 2, at round 10 (1,311,863 nodes, 203 s);
   the divider at the plastic number, a = 2, is alive to round 8 at
   the wall (2,397,044 nodes) and stays UNREACHED, with x^2 + y at
   a = 2 at the Narayana root and the plastic number, so the sweep's
   verdict is 41 of its 44 pairs dead below L* and three unreached,
   none alive.

F6 THE CONTIGUOUS ARM (--contiguous). The same confined tree at every
   contiguous cell of radices 2..5 with slack at least 1, x y, x^2 + y
   and the divider at P = 1/(b - 1), at L* - 1: dead at all 60 pairs,
   rounds 1 at 35, 2 at 23 and 3 at 2 (x y at (5,4,2) and (3,2,2)),
   the deepest kill at 206 nodes, wall 0.3 s -- the contiguous range
   the sweep's rounds are read against is 1 to 3, not the 1 to 4 the
   derivation carried from the gap sets.

VERDICT. Off the contiguous sets the margin law's L* is the delay at
every one of the 41 pairs the tree reached, over three integer gap-set
maps, five Pisot bases and two digit radii; the reader's strategy
delays the kill -- to round 12 at the plastic number, four times the
contiguous arm's deepest -- and never escapes it where the tree
reaches, buying nothing where the tree reaches and at most one L at
every unreached pair but one. The
frozen kill bar of six rounds was a transplant and is retired: the
kill round is unbounded across bases as far as the sweep can see, and
the instrument that decides a pair is the confined tree with a wall,
never a round count.

RUN RECORD: pure Python, the beta reader and the confined gap reader
imported from explore_beta_delay.py; under memwatch, peak commit 43 MB
against the 512 MB default, wall 538 s at the pair budget 1.5 million
nodes with 30 s per pair and 60 s per deep certificate -- over the
five-minute line by the per-pair caps, named here; the unreached pass
593 s more. Prints reproduced by:
python prime/code/explore_delay_sweep.py [NODE_BUDGET]
python prime/code/explore_delay_sweep.py --deepen Narayana:1:1,plastic:2:0,plastic:2:2 300
python prime/code/explore_delay_sweep.py --contiguous
"""

import os
import sys
import time
from collections import Counter
from fractions import Fraction as Fr

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import explore_manystream_delay as ms                      # noqa: E402
import explore_gap_lattice as gl                           # noqa: E402
import explore_beta_delay as bd                            # noqa: E402

FAILURES = []
PAIR_BUDGET = 1_500_000
PAIR_WALL = 30.0
MAX_ROUNDS = 6
DEEP_WALL = 60.0
DEEP_ROUNDS = 20


def ok(cond, msg):
    if not cond:
        FAILURES.append(msg)
        print("  KILL:", msg)


class BSquarePlus:
    """x^2 + y in base beta."""
    name, d = "x^2 + y", 2

    def __init__(self, B):
        self.B = B

    def image(self, xs, ys, den, betan):
        B = self.B
        X1, X2 = xs
        s1, s2 = B.mul(X1, X1), B.mul(X2, X2)
        if B.sign(X1) <= 0 <= B.sign(X2):
            sq_lo = B.zero
        else:
            sq_lo = s1 if B.sign(B.sub(s1, s2)) < 0 else s2
        sq_hi = s1 if B.sign(B.sub(s1, s2)) > 0 else s2
        d2 = B.mul(den, den)
        return (B.add(sq_lo, B.mul(ys[0], den)), d2), (B.add(sq_hi, B.mul(ys[1], den)), d2)

    def window_range(self, M):
        B = self.B
        M2 = B.fmul(M, M)
        hi = (B.add(M2[0], B.mul(M[0], M[1])), M2[1])          # (a^2 + a (beta - 1)) / (beta - 1)^2
        return (B.neg(M[0]), M[1]), hi

    def lam(self, M):
        B = self.B
        return B.add(B.scale(2, M[0]), M[1]), M[1]

    def grad_sup(self, box):
        return 2 * max(abs(box[0][0]), abs(box[0][1])) + 1


def beta_bases():
    return [bd.Base("golden (x^2 = x + 1)", (1, 1)),
            bd.Base("Narayana (x^3 = x^2 + 1)", (1, 0, 1)),
            bd.Base("silver (x^2 = 2x + 1)", (1, 2)),
            bd.Base("tribonacci (x^3 = x^2 + x + 1)", (1, 1, 1)),
            bd.Base("plastic (x^3 = x + 1)", (1, 1, 0))]


def beta_maps(B, a):
    return [bd.BProduct(B), BSquarePlus(B), bd.BDivision(B, 1, 1, a)]


def run_beta(B, fmap, a, L, budget, label):
    o = bd.least_lead(B, fmap, a)
    rd = bd.BetaReader(B, fmap, L - o, o, a)
    t1 = time.time()
    r, depth = rd.certificate(budget, wall=PAIR_WALL, max_rounds=MAX_ROUNDS, confined=True)
    verdict = ("dead r=%d" % r if r is not None else
               ("ALIVE to round %d" % depth if depth >= MAX_ROUNDS else "UNREACHED at round %d" % depth))
    print(f"  {label} o={o} L={L}: {verdict} [{rd.nodes} nodes {time.time() - t1:.1f}s]")
    return r, depth, o


def alive_checks(B, fmap, a, L, o, budget):
    """At a pair alive through round 6 under confinement: the FULL tree
    at the same pair to its budget (a kill there falsifies the
    confinement), then the descent in L until the confined tree kills
    (how many digits the strategy buys)."""
    rd = bd.BetaReader(B, fmap, L - 1 - o, o, a)
    t1 = time.time()
    r, depth = rd.certificate(budget, wall=PAIR_WALL, max_rounds=MAX_ROUNDS, confined=False)
    print(f"      FULL tree at L={L - 1}: {'dead r=' + str(r) if r is not None else 'alive'} "
          f"[{depth}] {rd.nodes} nodes {time.time() - t1:.1f}s")
    ok(r is None, f"CONFINEMENT FALSIFIED at {B.name} {fmap.name} a={a} L={L - 1}: full tree dead at round {r}")
    rd = bd.BetaReader(B, fmap, L - 1 - o, o, a)
    t1 = time.time()
    r, depth = rd.certificate(budget, wall=DEEP_WALL, max_rounds=DEEP_ROUNDS, confined=True)
    print(f"      DEEP confined certificate at L={L - 1}: "
          f"{'dead r=' + str(r) if r is not None else 'alive to round ' + str(depth)} "
          f"{rd.nodes} nodes {time.time() - t1:.1f}s")
    for LL in range(L - 2, L - 5, -1):
        r, depth, _ = run_beta(B, fmap, a, LL, budget, "      descent")
        if r is not None:
            break


def run_gap(D, fmap, L, budget, label):
    b = 3
    o = ms.least_lead(b, -min(D), max(D), fmap)
    rd = bd.ConfinedGap(b, D, L - o, fmap, o)
    t1 = time.time()
    r, depth = rd.certificate(budget, wall=PAIR_WALL, max_rounds=MAX_ROUNDS)
    verdict = ("dead r=%d" % r if r is not None else
               ("ALIVE to round %d" % depth if depth >= MAX_ROUNDS else "UNREACHED at round %d" % depth))
    print(f"  {label} o={o} L={L}: {verdict} [{rd.nodes} nodes {time.time() - t1:.1f}s]")
    return r, depth, o


def controls(budget):
    print("\n=== K1 THE CONTROLS against the record's rounds")
    G, N = beta_bases()[0], beta_bases()[1]
    r, _, _ = run_beta(G, bd.BProduct(G), 1, 3, budget, "golden x y a=1")
    ok(r == 5, f"K1 golden x y L=3: round {r} against the record's 5")
    r, _, _ = run_beta(N, bd.BDivision(N, 1, 1), 1, 3, budget, "Narayana divider a=1")
    ok(r == 5, f"K1 Narayana divider L=3: round {r} against the record's 5")
    D = (-3, -1, 0, 1, 2)
    r, _, _ = run_gap(D, ms.Product(3, 3, 2), 2, budget, "radix 3 {-3,-1,0,1,2} x y")
    ok(r == 4, f"K1 radix 3 x y L=2: round {r} against the record's 4")
    # the lead's arithmetic at a = 2: the divider's pole offset and x^2 + y's range top
    M2 = G.ffloat((G.scale(2, G.one), G.bm1))
    top = G.ffloat(BSquarePlus(G).window_range((G.scale(2, G.one), G.bm1))[1])
    print(f"  x^2 + y at the golden mean, a=2: range top {top:.4f} against M^2 + M = {M2 * M2 + M2:.4f}")
    ok(abs(top - (M2 * M2 + M2)) < 1e-9, "K1 x^2 + y's range top")
    div = bd.BDivision(G, 1, 1, 2)
    print(f"  the divider at the golden mean, a=2: s = {div.sf:.4f} against M + 1 = {M2 + 1:.4f}")
    ok(abs(div.sf - (M2 + 1)) < 1e-9, "K1 the divider's pole offset at a=2")


def integer_arm(budget):
    print("\n=== P-B THE INTEGER ARM: radix 3, every set of positive least zone, x^2 + y at L* - 1")
    rounds = Counter()
    b = 3
    for D in gl.candidate_sets(b):
        interval, w, gmax, zmin = gl.tail_verdict(b, D)
        if not interval or zmin == 0:
            continue
        am, ap = -min(D), max(D)
        fmap = ms.SquarePlus(b, am, ap)
        Lg = gl.law_gen(b, D, fmap)
        r, depth, o = run_gap(D, fmap, Lg - 1, budget, f"radix 3 {list(D)} z_min={zmin} x^2 + y L*={Lg}")
        rounds[r if r is not None else ("alive" if depth >= MAX_ROUNDS else "unreached")] += 1
    print(f"  rounds: {dict(rounds)}")
    return rounds


def beta_arm(budget):
    print("\n=== P-C THE BETA ARM: five bases, a in {1, 2}, x y, x^2 + y and the divider at L* - 1")
    rounds = Counter()
    table = []
    for B in beta_bases():
        for a in (1, 2):
            interval = B.fl - 1 <= 2 * a
            M = B.ffloat((B.scale(a, B.one), B.bm1))
            print(f"  {B.name} a={a}: beta={B.fl:.4f}, M={M:.4f}, w-1={2 * M - 1:.4f}, "
                  f"tails {'interval' if interval else 'CANTOR'}")
            ok(interval, f"K3 {B.name} a={a}: Cantor tails")
            if not interval:
                continue
            for fmap in beta_maps(B, a):
                L, _, _ = bd.law_L(B, fmap, a)
                r, depth, o = run_beta(B, fmap, a, L - 1, budget, f"    {fmap.name} L*={L}")
                key = r if r is not None else ("alive" if depth >= MAX_ROUNDS else "unreached")
                rounds[key] += 1
                table.append((B.name, a, fmap.name, L, o, key))
                if key == "alive":
                    alive_checks(B, fmap, a, L, o, budget)
    print(f"  rounds: {dict(rounds)}")
    print("\n=== P-C BY BASE AND a: the kill round per map (x y, x^2 + y, the divider)")
    for B in beta_bases():
        for a in (1, 2):
            row = [str(k) for (nm, aa, mp, L, o, k) in table if nm == B.name and aa == a]
            if row:
                print(f"  {B.name} a={a}: {' / '.join(row)}")
    return rounds, table


def contiguous_arm(budget):
    """--contiguous: the same tree at every contiguous cell of radices
    2..5 with slack at least 1, x y, x^2 + y and the divider at
    P = 1/(b - 1), at L* - 1 -- the contiguous kill rounds the sweep's
    are read against, printed by the instrument that read the sweep."""
    print("\n=== THE CONTIGUOUS ARM: radices 2..5, x y, x^2 + y and the divider at P = 1/(b - 1), L* - 1")
    rounds = Counter()
    n = 0
    for b in (2, 3, 4, 5):
        for am in range(1, b):
            for ap in range(1, b):
                if am + ap + 1 - b < 1:
                    continue
                D = tuple(range(-am, ap + 1))
                for fmap in (ms.Product(b, am, ap), ms.SquarePlus(b, am, ap),
                             ms.Division(b, am, ap, Fr(1, b - 1))):
                    Le = ms.law_L(b, am, ap, fmap)
                    o = ms.least_lead(b, am, ap, fmap)
                    rd = bd.ConfinedGap(b, D, Le - 1 - o, fmap, o)
                    t1 = time.time()
                    r, depth = rd.certificate(budget, wall=PAIR_WALL, max_rounds=MAX_ROUNDS)
                    verdict = ("dead r=%d" % r if r is not None else
                               ("ALIVE to round %d" % depth if depth >= MAX_ROUNDS
                                else "UNREACHED at round %d" % depth))
                    print(f"  ({b},{am},{ap}) {fmap.name} L*={Le} o={o}: {verdict} "
                          f"[{rd.nodes} nodes {time.time() - t1:.1f}s]")
                    rounds[r if r is not None else ("alive" if depth >= MAX_ROUNDS else "unreached")] += 1
                    n += 1
    print(f"  rounds over {n} pairs: {dict(sorted(rounds.items(), key=lambda kv: str(kv[0])))}")
    return rounds


def deepen(specs, wall):
    """--deepen base:a:map[,...]: the confined tree at L* - 1 to round
    DEEP_ROUNDS under a longer wall at the named pairs (base by name
    prefix, map by index 0..2), the pass for pairs the sweep's deep
    certificate left alive."""
    print(f"\n=== THE UNREACHED PASS: wall {wall:.0f}s per pair, rounds to {DEEP_ROUNDS}")
    for spec in specs.split(","):
        name, a, mi = spec.split(":")
        a, mi = int(a), int(mi)
        B = [b for b in beta_bases() if b.name.startswith(name)][0]
        fmap = beta_maps(B, a)[mi]
        L, _, _ = bd.law_L(B, fmap, a)
        o = bd.least_lead(B, fmap, a)
        rd = bd.BetaReader(B, fmap, L - 1 - o, o, a)
        t1 = time.time()
        r, depth = rd.certificate(10 ** 9, wall=wall, max_rounds=DEEP_ROUNDS, confined=True)
        print(f"  {B.name} a={a} {fmap.name} L*={L} o={o} L={L - 1}: "
              f"{'dead r=' + str(r) if r is not None else 'alive to round ' + str(depth)} "
              f"{rd.nodes} nodes {time.time() - t1:.1f}s")


def main():
    if len(sys.argv) > 2 and sys.argv[1] == "--deepen":
        deepen(sys.argv[2], float(sys.argv[3]) if len(sys.argv) > 3 else 300.0)
        return
    if len(sys.argv) > 1 and sys.argv[1] == "--contiguous":
        contiguous_arm(int(sys.argv[2]) if len(sys.argv) > 2 else PAIR_BUDGET)
        return
    budget = int(sys.argv[1]) if len(sys.argv) > 1 else PAIR_BUDGET
    t0 = time.time()
    controls(budget)
    ri = integer_arm(budget)
    rb, table = beta_arm(budget)
    allr = ri + rb
    print("\n=== P-D THE ROUNDS over the sweep (the contiguous arm: --contiguous)")
    print(f"  {dict(sorted(allr.items(), key=lambda kv: str(kv[0])))}")
    alive = [t for t in table if t[5] == "alive"]
    unreached = [t for t in table if t[5] == "unreached"]
    print(f"  alive through round {MAX_ROUNDS}: {len(alive)}; unreached: {len(unreached)}")
    for t in alive:
        print(f"    ALIVE: {t}")
    for t in unreached:
        print(f"    unreached: {t}")
    print(f"\nwall {time.time() - t0:.1f}s; failures: {len(FAILURES)}")
    for f in FAILURES:
        print("  ", f)


if __name__ == "__main__":
    main()
