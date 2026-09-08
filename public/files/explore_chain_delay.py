"""The chained delay: does a multiplier feeding an adder read x y + z at
the fused unit's delay once the multiplier chooses its digits with
the adder in view, or does the chain pay the sum of the two units'
delays whatever the multiplier does?

THE QUESTION. explore_polynomial_delay.py prices the fused reader of
x y + z (one unit seeing x, y and z) at the Lebesgue margin in the
map's L1-Lipschitz constant, L* = 3 at (2,1,1) and 2 at every other
census cell of radices 2..5, while a product reader alone reads at
L1* = 2 or 1 and a sum reader alone at L2* = 2 or 1, so a chain that
pays L1* + L2* sits one or two lookaheads above the fused floor at
fifteen of the twenty cells. The field composes on-line units by
adding their delays: "for a series of online operations, the overall
latency is the sum of online delays of the corresponding operation"
(Usman, Ercegovac and Lee, Low-Latency Online Multiplier with Reduced
Activities and Minimized Interconnect for Inner Product Arrays, 2023,
section 4.2.2). The sum-of-delays price treats the intermediate
stream as an arbitrary D-stream. But the multiplier's digit choice is
free wherever two digits are legal, and a consumer that KNOWS the
multiplier's rule can read more from the emitted prefix than its
cell. This rig prices the chain exactly, over every multiplier rule.

THE CHAIN. Radix b, digit set D = {-am..ap}, M-+ = a-+/(b-1),
w = M- + M+, Mh = max(M-, M+), slack rho = am + ap + 1 - b >= 1, so
w - 1 = rho/(b-1). A product reader sees x and y and emits a
D-stream P with P = x y (the digit of weight b^-m emitted after the
inputs to position m + L1); a sum reader sees P and z and emits the
output (the digit of weight b^-t after P and z to position t + L2).
The chain's lookahead is L1 + L2 in the inputs, whatever the offsets.
The product reader's rule sigma is any function of the (x, y) prefix;
the sum reader knows sigma but sees neither x nor y.

WHAT THE SUM READER CAN USE. Its output cell must contain x y + z for
every (x, y, z) consistent with what it has seen; what it knows about
x y is the fibre V(P_n) = the union of the product images of every
(x, y) prefix sigma sends to the prefix P_n, and a cell (an interval)
contains V + zbox iff it contains hull(V) + zbox. So the sum reader
reads exactly the HULL of the fibre, an interval inside P_n's own
box [P_n - M-, P_n + M+] (in level-n units), which we write with its
INSETS alpha, beta >= 0 from the box's two ends. The sum reader's
death is a property of the hull and the z prefix alone (explore_
product_necessity.py's death criterion: the image strictly contains
an overlap zone of two consecutive output cells), and z is the
adversary's, its prefix sum s = P_n + z_n running over every residue
once n is large, so in the units of explore_polynomial_delay.py

    THE INSET CLAUSE: the sum reader at lookahead L2 is dead iff an
    integer lies in ((b^L2 - 2) M+ + beta,  b^L2 - (b^L2 - 2) M- - alpha),

the k-sum's clause at k = 2 with the death interval shortened by
beta at its lower end and alpha at its upper. Its ESCAPE COST
E(L2) is the least alpha + beta making the interval integer-free:
0 where the plain clause is already alive, and otherwise, for the
integers j_1 < ... < j_r inside, the least over splits i of
(j_i - lo) + (hi - j_{i+1}), the integers at or below j_i pushed out
below and the rest above.

WHAT THE PRODUCT READER CAN AFFORD. Every (x, y) prefix at level
n + L1 has an image of width at most Lip w / b^L1 in level-n units,
Lip = 2 Mh, approached from below at the window's corner and dense
in position (the split line of explore_product_necessity.py), and
sigma must send each image into a hull that contains it; the hulls
sit at unit spacing, so consecutive hulls must overlap by at least
the image width, which reads beta_n + alpha_{n+1} <= w - 1 - Lip
w / b^L1 on every consecutive pair. Constant insets are then optimal
up to the two boundary hulls of a level's range (a period's pair
sums add to its inset sums, so some option's sum is under the bound
wherever the pairs' are), so the product reader's SLACK BUDGET is

    S(L1) = w - 1 - 2 Mh w / b^L1,

nonnegative exactly from the product's own floor on, and the chain
survives at (L1, L2) iff E(L2) <= S(L1): THE ESCAPE LAW. The chain's
floor is the least L1 + L2 over the pairs the law admits; the
covering search below decides the deaths exactly, boundary hulls
included. A product reader
that realises the budget is the reader into NARROWED CELLS
[q - M- + alpha, q + M+ - beta], whose children still cover their
parent (the parent's insets scale by b) and overlap by w - 1 - alpha
- beta, so it reads at the margin with the narrowed slack
rho' = rho - (b-1)(alpha + beta):

    THE NARROWED LAW:  b^L1 (b-1) (rho - (b-1)(alpha + beta)) >= 2 ah (am + ap),

the product's law (explore_product_delay.py) with the narrowed slack.

THE EAGER CHAIN. The field's adder takes z delayed to align with P;
an adder wired to read z as it arrives sees z to position t + L1 + L2
and its z box is b^L1 times narrower. The same derivation with
s = b^L1 P_n + z gives the eager clause: dead iff an integer lies in
(B M+ - (q+1) M+ + q beta, B (1 - M-) + (q+1) M- - q alpha) with
q = b^L1, B = b^(L1 + L2); the insets count q-fold. This variant is
a partly fused adder, priced beside the chain, never as it.

THE CLOSED-FORM PREDICTION (hand-derived before the engine; the
numbers below are the escape law's, not a print). Fused floor L_f:
least L with w - 1 >= (2 Mh + 1) w / b^L; product floor L1*; sum
floor L2* (E = 0); the naive chain L1* + L2*; the informed chain by
the escape law; the eager chain by the eager law with the same
budget. At the 20 representable cells of radices 2..5 (o = 1 for
the fused unit): the informed chain EQUALS the naive chain at every
cell (the multiplier's choice buys the aligned adder nothing: where
the plain clause holds an integer, its escape cost exceeds every
budget); the fused unit reads BELOW the chain by one at the eleven
cells with L1* = 2 and L2* = 1 or with (b,am,ap) = (2,1,1), by two
at the four cells with L1* = L2* = 2 at radix >= 3, and EQUALS it at
the five cells with L1* = 1; the eager chain closes exactly one
lookahead at the L2* = 2 cells of radix >= 3 and none elsewhere, so
it sits one above the fused floor at every cell but the five.

THE SLATE, frozen before the engine.

P-A THE CONTROLS. (i) The inset clause at alpha = beta = 0 is the
    k = 2 clause: it reproduces sum_law at 20/20 cells of radices
    2..5. (ii) The narrowed-cell product game at alpha = beta = 0
    reproduces the product census (explore_monomial_delay.py: c* by
    the margin law, certified at c* - 1, surviving at c*) at every
    representable cell of radices 2..4. (iii) The sum game with P's
    INPUT boxes inset by (alpha, beta), run through the engine at a
    grid of insets, agrees with the inset clause at every cell and
    lookahead tried.
P-B THE NARROWED LAW. The product reader into cells inset by
    (alpha, beta) on a grid of insets, radices 2..4: certified at
    the narrowed law's L - 1 and surviving at its L, cell by cell.
P-C THE ESCAPE LAW'S LOWER BOUND. At every pair (L1, L2) the law
    calls dead with L1 >= L1* (radices 2..4, L1 + L2 below the
    naive chain), the level-n covering search over ALL assignments
    of the level-(n + L1) product images to inset hulls finds no
    assignment at some n <= the search depth: a certificate against
    every multiplier rule.
P-D THE PRICE TABLE. The chain's floor (informed), the eager floor,
    the naive chain and the fused floor print at every cell; the
    prediction is the closed-form table above.

KILLS, frozen as what this rig PRINTS.

K1 P-A prints a disagreement -> the engine or the clause is wrong;
   nothing below is read.
K2 P-B prints a certificate at the narrowed law's L, or a survival
   to the budget at L - 1 -> the narrowed law is not the floor and
   the budget S(L1) is misderived.
K3 P-C finds an assignment at every searched level for some pair
   the law calls dead -> the lower bound is not a certificate at
   that depth; the pair is printed OPEN and the floor at that cell
   is an upper bound only.
K4 THE HEADLINE KILL. The informed chain's floor equals the fused
   floor at every cell -> no fusion edge, and the chain is the fused
   unit's equal.
K5 The informed chain reads BELOW the naive chain at some cell ->
   the multiplier's choice is a design axis for the aligned adder.

POSITIVE CONTROL: P-A whole, read before any chain line.

THE ENGINE'S FIRST FORM, corrected before the first full run and
recorded here: the input-inset boxes were first unnested, so an inset
child box poked out of its parent's and the adversary won at (2,1,1),
L2 = 1, insets (1, 0), a configuration no fibre hull produces (K1 as
first coded); the narrowed law was first written without the (b-1)
factor the product's law carries, invisible at radix 2; the
narrowed root's offset was first fixed at 1, and an inset of three
quarters of the slack needs 2.

FINDINGS (entered post-run; every number below sits in this file's
printed output).

F1 THE CONTROLS HOLD. The inset clause at zero insets reproduces
   sum_law at 20/20 cells. The narrowed-cell product game at zero
   insets reproduces the product census at 7/7 representable cells
   of radices 2..4 (c* = 2 at six, 1 at (4,3,3); certified at c* - 1
   in 1 or 2 rounds, surviving at c*). The sum game with P's box
   inset and nested agrees with the inset clause at 120 of 120
   cell-lookahead-inset triples (radices 2..4, L2 in {1, 2}, six
   inset pairs). P-A held; K1 never fired on the corrected engine.

F2 THE NARROWED LAW HOLDS [rule at the scanned scope]. The product
   reader into cells inset by a half, a quarter each side, or three
   quarters of the slack: 28 cell-inset pairs at radices 2..4,
   certified at the law's L - 1 in 1 to 3 rounds and surviving the
   search at L at 28/28, the root offset 0, 1 or 2 as the inset
   demands. P-B held; K2 never fired.

F3 THE ESCAPE LAW'S DEATHS ARE CERTIFIED. Every pair (L1, L2) below
   the naive chain that the law calls dead, radices 2..4: 22 aligned
   pairs, all with no assignment at n = 1; 17 eager pairs, 16 at
   n = 1 and (2,1,1) (2,1) at n = 3, the z prefix reaching every
   residue at the certifying level in each case. P-C held; K3 never
   fired, no pair capped.

F4 THE PRICE TABLE [the aligned chain's floor a criterion at the 20
   cells: deaths certified by F3, survivals at zero insets by the
   product census and the k-sum clause; the eager chain's informed
   floor a rule, its survivals resting on the narrowed law read at
   insets F2's grid did not run]. Radices 2..5, 20 cells: the informed
   chain equals the naive chain L1* + L2* at 20/20 (informed below
   naive at 0: the multiplier's choice buys the aligned adder
   nothing; K5 never fired); the fused floor sits below the chain at
   15 and equal at 5 (the cells with L1* = 1), by one at (2,1,1) and
   at the five cells with L1* = 2, L2* = 1, by two at the nine cells
   with L1* = L2* = 2 at radix >= 3. K4 never fired. The eager adder,
   reading z as it arrives, closes one lookahead at exactly the
   L2* = 2 cells of radix >= 3 (9 of 20), and only when the
   multiplier's choice is used: the informed eager floor is below
   the naive eager at those 9 and the insets that buy it are small
   (1/18 at (3,1,2), 1/100 at (5,1,4)); the eager chain reaches the
   fused floor at the same 5 cells and nowhere else. The prediction
   held cell for cell, but for its two counts: six and nine, not
   eleven and four (the freeze miscounted the L1* = L2* = 2 cells of
   radix >= 3; the table is the record).

VERDICT. A chain of on-line units pays the sum of its units' floors
whatever the first unit does with its digit choice, and the fused
unit reads below it wherever the product's margin absorbs the
addition outright (the fused floor equal to the product's, L1* = 2
at radix >= 3) or the adder alone needs two lookaheads ((2,1,1));
the two are level only where the product's floor is 1 and both pay
one for z. The consumer's knowledge of the producer's
rule is worth exactly one digit-grain of hull, which pays only where
the adder's death interval has an integer within the producer's
slack of an endpoint, and an aligned adder never has one there. The
composed-margin conjecture dies by this print: a network of on-line
units does not read at the composed margin unless it is fused.

RUN RECORD: pure Python, exact rationals, standard library; under
memwatch, peak commit 50.7 MB against the 512 MB default; wall 220 s
at the defaults (4, 3), the exact-rational games most of it. Prints
reproduced by:
python prime/code/explore_chain_delay.py [BMAX_game NMAX_cover]
"""

import itertools
import math
import sys
import time
from fractions import Fraction as Fr

FAILURES = []
IMG_CAP = 4_000_000   # prefix pairs the covering search will enumerate


def ok(cond, msg):
    if not cond:
        FAILURES.append(msg)
        print(f"  FAIL: {msg}")


# ---------------------------------------------------------- closed forms

def window(b, am, ap):
    Mm, Mp = Fr(am, b - 1), Fr(ap, b - 1)
    return Mm, Mp, Mm + Mp, max(Mm, Mp)


def margin_L(b, am, ap, lip):
    """Least L with w - 1 >= lip * w / b^L, lip in window units."""
    Mm, Mp, w, Mh = window(b, am, ap)
    L = 0
    while w - 1 < lip * w / b ** L:
        L += 1
    return L


def death_interval(b, am, ap, L2, L1=0):
    """(lo, hi, q): the sum reader of P + z is dead at L2 iff an integer
    lies in (lo + q beta, hi - q alpha); q = 1 for the aligned chain,
    b^L1 for the eager one."""
    Mm, Mp, w, Mh = window(b, am, ap)
    q, B = b ** L1, b ** (L1 + L2)
    return B * Mp - (q + 1) * Mp, B * (1 - Mm) + (q + 1) * Mm, q


def escape_options(b, am, ap, L2, L1=0):
    """The minimal (alpha, beta) pairs making the death interval
    integer-free; [(0, 0)] when it already is."""
    lo, hi, q = death_interval(b, am, ap, L2, L1)
    ints = [j for j in range(math.floor(lo) + 1, math.ceil(hi) + 1) if lo < j < hi]
    if not ints:
        return [(Fr(0), Fr(0))]
    opts = []
    for i in range(len(ints) + 1):
        beta = (ints[i - 1] - lo) / q if i > 0 else Fr(0)
        alpha = (hi - ints[i]) / q if i < len(ints) else Fr(0)
        opts.append((alpha, beta))
    return opts


def escape_cost(b, am, ap, L2, L1=0):
    return min(a + c for a, c in escape_options(b, am, ap, L2, L1))


def slack_budget(b, am, ap, L1):
    Mm, Mp, w, Mh = window(b, am, ap)
    return w - 1 - 2 * Mh * w / b ** L1


def narrowed_L(b, am, ap, alpha, beta):
    """Least L with b^L (b-1) (rho - (b-1)(alpha+beta)) >= 2 ah (am+ap)."""
    rho, ah, W = am + ap + 1 - b, max(am, ap), am + ap
    rho2 = rho - (b - 1) * (alpha + beta)
    if rho2 <= 0:
        return None
    L = 0
    while b ** L * (b - 1) * rho2 < 2 * ah * W:
        L += 1
    return L


def chain_floor(b, am, ap, eager=False, span=6):
    """(L1 + L2, L1, L2, alpha, beta) least by the escape law."""
    L1s = margin_L(b, am, ap, 2 * window(b, am, ap)[3])
    best = None
    for L1 in range(L1s, L1s + span):
        S = slack_budget(b, am, ap, L1)
        for L2 in range(0, span):
            for alpha, beta in escape_options(b, am, ap, L2, L1 if eager else 0):
                if alpha + beta <= S and (best is None or L1 + L2 < best[0]):
                    best = (L1 + L2, L1, L2, alpha, beta)
    return best


def sum_law(b, am, ap):
    rho = am + ap + 1 - b
    sig = -(-am // (b - 1)) - (-ap // (b - 1))
    return 1 if rho >= sig else 2


def census(bmax):
    return [(b, am, ap) for b in range(2, bmax + 1)
            for am in range(0, b) for ap in range(0, b)
            if am + ap + 1 - b >= 1]


def representable_ma(b, am, ap):
    """x y + z fits the root cell at o = 1 (explore_polynomial_delay.py)."""
    Mm, Mp, w, Mh = window(b, am, ap)
    return max(Mm * Mm, Mp * Mp) + Mp <= Mp * b and -Mm * Mp - Mm >= -Mm * b


def representable_xy(b, am, ap):
    return am * am <= ap * (b - 1)


# --------------------------------------------------------------- engine

class InsetGame:
    """The reading game at lookahead c for a map that is a product of
    the streams in `prod` plus the streams in `lin` (each with integer
    coefficient 1), with the INPUT boxes of the streams in in_inset
    inset by (alpha_i, beta_i) and NESTED (a prefix's box is its own
    inset box cut to its parent's, as a fibre hull is), and the OUTPUT
    cells inset by (alpha, beta) = out_inset, all in cell units;
    offset o. Exact rationals throughout."""

    def __init__(self, b, am, ap, c, prod=(), lin=(), o=0,
                 in_inset=None, out_inset=(Fr(0), Fr(0))):
        self.b, self.am, self.ap, self.c, self.o = b, am, ap, c, o
        self.prod, self.lin = tuple(prod), tuple(lin)
        self.k = 1 + max(self.prod + self.lin)
        self.Mm, self.Mp = Fr(am, b - 1), Fr(ap, b - 1)
        self.in_inset = dict(in_inset or {})
        self.oa, self.ob = out_inset
        self.digits = list(range(-am, ap + 1))
        self.moves = list(itertools.product(self.digits, repeat=self.k))

    def own_box(self, i, u, n):
        a, c = self.in_inset.get(i, (Fr(0), Fr(0)))
        s = Fr(1, self.b ** n)
        return (u - self.Mm + a) * s, (u + self.Mp - c) * s

    def extend(self, boxes, us1, n):
        """The nested boxes of the extended prefixes."""
        out = []
        for i in range(self.k):
            lo, hi = self.own_box(i, us1[i], n)
            if boxes is not None:
                lo, hi = max(lo, boxes[i][0]), min(hi, boxes[i][1])
            out.append((lo, hi))
        return tuple(out)

    def image(self, boxes):
        lo, hi = Fr(1), Fr(1)
        first = True
        for i in self.prod:
            p1, p2 = boxes[i]
            if first:
                lo, hi, first = p1, p2, False
            else:
                cs = (lo * p1, lo * p2, hi * p1, hi * p2)
                lo, hi = min(cs), max(cs)
        if first:
            lo, hi = Fr(0), Fr(0)
        for i in self.lin:
            p1, p2 = boxes[i]
            lo, hi = lo + p1, hi + p2
        return lo, hi

    def legal(self, boxes, q, t):
        lo, hi = self.image(boxes)
        s = Fr(self.b ** self.o, self.b ** t)
        return lo >= (q - self.Mm + self.oa) * s and hi <= (q + self.Mp - self.ob) * s

    def survives(self, us, boxes, q, t, rounds):
        if rounds == 0:
            return True
        n = t + self.c
        for mv in self.moves:
            us1 = tuple(self.b * u + x for u, x in zip(us, mv))
            boxes1 = self.extend(boxes, us1, n + 1)
            alive = False
            for p in self.digits:
                if self.legal(boxes1, self.b * q + p, t + 1) and                         self.survives(us1, boxes1, self.b * q + p, t + 1, rounds - 1):
                    alive = True
                    break
            if not alive:
                return False
        return True

    def reader_survives(self, rounds):
        states = [(tuple([0] * self.k), self.extend(None, tuple([0] * self.k), 0))]
        for lev in range(1, self.c + 1):
            states = [(us1, self.extend(bx, us1, lev))
                      for us, bx in states for mv in self.moves
                      for us1 in [tuple(self.b * u + x for u, x in zip(us, mv))]]
        return all(self.legal(bx, 0, 0) and self.survives(us, bx, 0, 0, rounds)
                   for us, bx in states)

    def certificate_depth(self, max_rounds, budget=300_000):
        m = len(self.moves)
        depth = max(1, min(max_rounds, int(math.log(budget) / math.log(m)) - self.c))
        for r in range(0, depth + 1):
            if not self.reader_survives(r):
                return r, depth
        return None, depth


# ------------------------------------------------ the covering search

def product_images(b, am, ap, m):
    """Every product image of an (x, y) prefix pair of length m, as
    (lo, hi) in absolute units; duplicates removed."""
    Mm, Mp = Fr(am, b - 1), Fr(ap, b - 1)
    lo_u = -sum(am * b ** i for i in range(m))
    hi_u = sum(ap * b ** i for i in range(m))
    s = Fr(1, b ** m)
    boxes = [((u - Mm) * s, (u + Mp) * s) for u in range(lo_u, hi_u + 1)]
    out = set()
    for (x1, x2) in boxes:
        for (y1, y2) in boxes:
            cs = (x1 * y1, x1 * y2, x2 * y1, x2 * y2)
            out.add((min(cs), max(cs)))
    return sorted(out)


def covering_exists(b, am, ap, L1, L2, n, eager=False):
    """Is there an assignment of the level-(n + L1) product images to
    level-n hulls, each hull an escape option's inset of its box, with
    every image inside its hull? Depth-first over the hulls in order,
    an image lost once the hulls have passed it."""
    Mm, Mp = Fr(am, b - 1), Fr(ap, b - 1)
    if (am + ap + 1) ** (2 * (n + L1)) > IMG_CAP:
        return None
    imgs = product_images(b, am, ap, n + L1)
    opts = escape_options(b, am, ap, L2, L1 if eager else 0)
    opts = sorted(set(opts))
    s = Fr(1, b ** n)
    lo_q = math.floor(imgs[0][0] / s - Mp) - 1
    hi_q = math.ceil(imgs[-1][1] / s + Mm) + 1
    qs = list(range(lo_q, hi_q + 1))
    imgs_sorted = imgs

    def rec(idx, remaining):
        if not remaining:
            return True
        if idx == len(qs):
            return False
        q = qs[idx]
        # an image whose left end is below this hull's least left end
        # and which is still unassigned can never be covered later
        least_left = (q - Mm) * s
        if any(l < least_left for (l, r) in remaining):
            return False
        for alpha, beta in opts:
            hl, hr = (q - Mm + alpha) * s, (q + Mp - beta) * s
            rest = [(l, r) for (l, r) in remaining if not (hl <= l and r <= hr)]
            if len(rest) < len(remaining) and rec(idx + 1, rest):
                return True
        return rec(idx + 1, remaining)

    return rec(0, imgs_sorted)


# ------------------------------------------------------------------ main

def main():
    T = 12
    bmax_game = int(sys.argv[1]) if len(sys.argv) > 1 else 4
    nmax = int(sys.argv[2]) if len(sys.argv) > 2 else 3
    t0 = time.time()

    print("=== P-A (i): the inset clause at zero insets against sum_law, radices 2..5")
    agree = tot = 0
    for (b, am, ap) in census(5):
        tot += 1
        Lc = min(L for L in range(0, 6) if escape_cost(b, am, ap, L) == 0)
        if Lc == sum_law(b, am, ap):
            agree += 1
        else:
            ok(False, f"K1 inset clause at zero insets ({b},{am},{ap}): {Lc} vs sum_law {sum_law(b, am, ap)}")
    print(f"  {tot} cells, agree {agree}")

    print(f"\n=== P-A (ii): the narrowed-cell product game at zero insets, radices 2..{bmax_game}")
    for (b, am, ap) in census(bmax_game):
        if not representable_xy(b, am, ap):
            continue
        L = narrowed_L(b, am, ap, Fr(0), Fr(0))
        cert, d1 = InsetGame(b, am, ap, L - 1, prod=(0, 1)).certificate_depth(T)
        surv, d2 = InsetGame(b, am, ap, L, prod=(0, 1)).certificate_depth(T, budget=100_000)
        ok(cert is not None and surv is None,
           f"K1 product control ({b},{am},{ap}): L*={L}, cert {cert} [{d1}], survival {surv} [{d2}]")
        print(f"  ({b},{am},{ap}) c*={L} | cert at c*-1: {cert} [{d1}] | survives at c*: {'yes' if surv is None else 'NO'} [{d2}]")

    print(f"\n=== P-A (iii): the sum game with P's input box inset, against the inset clause, radices 2..{bmax_game}")
    grid = [(Fr(0), Fr(0)), (Fr(1, 2), Fr(0)), (Fr(0), Fr(1, 2)), (Fr(1, 3), Fr(1, 3)), (Fr(1), Fr(0)), (Fr(2, 3), Fr(1, 3))]
    agree = tot = 0
    for (b, am, ap) in census(bmax_game):
        for L2 in (1, 2):
            for alpha, beta in grid:
                lo, hi, q = death_interval(b, am, ap, L2)
                pred_dead = math.floor(lo + beta) + 1 < hi - alpha
                g = InsetGame(b, am, ap, L2 - 1, lin=(0, 1), o=1, in_inset={0: (alpha, beta)})
                cert, d = g.certificate_depth(T, budget=100_000)
                tot += 1
                if (cert is not None) == pred_dead:
                    agree += 1
                else:
                    ok(False, f"K1 inset sum ({b},{am},{ap}) L2={L2} insets ({alpha},{beta}): "
                              f"clause {'dead' if pred_dead else 'alive'}, engine {cert} [{d}]")
    print(f"  {tot} cell-lookahead-inset triples, agree {agree}")
    if FAILURES:
        print("\nPOSITIVE CONTROL FAILED; nothing below is read")
        for f in FAILURES:
            print("  ", f)
        return

    print(f"\n=== P-B: the narrowed law, the product into inset cells, radices 2..{bmax_game}")
    for (b, am, ap) in census(bmax_game):
        if not representable_xy(b, am, ap):
            continue
        w1 = window(b, am, ap)[2] - 1
        for fa, fb in ((Fr(1, 2), Fr(0)), (Fr(0), Fr(1, 2)), (Fr(1, 4), Fr(1, 4)), (Fr(3, 4), Fr(0))):
            alpha, beta = fa * w1, fb * w1
            L = narrowed_L(b, am, ap, alpha, beta)
            if L is None or L > 4:
                print(f"  ({b},{am},{ap}) insets ({alpha},{beta}): slack exhausted, no L")
                continue
            Mm, Mp = Fr(am, b - 1), Fr(ap, b - 1)
            o = 0   # the least offset whose inset root holds the product's range
            while not (-Mm * Mp >= (-Mm + alpha) * b ** o and max(Mm, Mp) ** 2 <= (Mp - beta) * b ** o):
                o += 1
            cert, d1 = InsetGame(b, am, ap, L - 1 - o, prod=(0, 1), o=o, out_inset=(alpha, beta)).certificate_depth(T)
            surv, d2 = InsetGame(b, am, ap, L - o, prod=(0, 1), o=o, out_inset=(alpha, beta)).certificate_depth(T, budget=100_000)
            ok(surv is None, f"K2 narrowed product ({b},{am},{ap}) insets ({alpha},{beta}) certified at the law's L={L} after {surv}")
            if cert is None:
                print(f"  K2? ({b},{am},{ap}) insets ({alpha},{beta}) L={L}: survives to depth {d1} at L-1")
            print(f"  ({b},{am},{ap}) insets ({alpha},{beta}) L={L} o={o} | cert at L-1: {cert} [{d1}] | survives at L: {'yes' if surv is None else 'NO'} [{d2}]")

    print(f"\n=== P-C: the escape law's lower bound by the covering search, radices 2..{bmax_game}, n <= {nmax}")
    for eager in (False, True):
        print(f"  -- {'eager' if eager else 'aligned'} chain")
        for (b, am, ap) in census(bmax_game):
            if not representable_ma(b, am, ap):
                continue
            L1s = margin_L(b, am, ap, 2 * window(b, am, ap)[3])
            naive = L1s + sum_law(b, am, ap)
            for L1 in range(L1s, naive):
                for L2 in range(0, naive - L1):
                    dead = escape_cost(b, am, ap, L2, L1 if eager else 0) > slack_budget(b, am, ap, L1)
                    if not dead:
                        continue
                    found, capped = None, None
                    for n in range(1, nmax + 1):
                        # the adversary's z prefix at the level the adder
                        # reads must reach every residue the death
                        # interval can ask for
                        nz = n + (L1 if eager else 0)
                        if (am + ap) * (b ** nz - 1) // (b - 1) + 1 < b ** (L2 + (L1 if eager else 0)):
                            continue
                        r = covering_exists(b, am, ap, L1, L2, n, eager)
                        if r is None:
                            capped = n
                            break
                        if not r:
                            found = n
                            break
                    if found is not None:
                        print(f"  ({b},{am},{ap}) (L1,L2)=({L1},{L2}) dead by the law: no assignment at n={found}")
                    elif capped is not None:
                        print(f"  K3 UNSEARCHED ({b},{am},{ap}) (L1,L2)=({L1},{L2}): assignments exist at n < {capped}, the search capped there")
                    else:
                        print(f"  K3 OPEN ({b},{am},{ap}) (L1,L2)=({L1},{L2}): an assignment exists at every n <= {nmax}")

    print("\n=== P-D: the price table, radices 2..5")
    print("  cell | L1* L2* | fused | naive | informed (L1,L2,alpha,beta) | eager (L1,L2,alpha,beta) | naive eager")
    nfused_below = nequal = ninf_below_naive = 0
    rows = []
    for (b, am, ap) in census(5):
        if not representable_ma(b, am, ap):
            continue
        Mm, Mp, w, Mh = window(b, am, ap)
        L1s, L2s = margin_L(b, am, ap, 2 * Mh), sum_law(b, am, ap)
        Lf = margin_L(b, am, ap, 2 * Mh + 1)
        inf, eag = chain_floor(b, am, ap), chain_floor(b, am, ap, eager=True)
        eag0 = min(L1 + L2 for L1 in range(L1s, L1s + 6) for L2 in range(0, 6)
                   if escape_cost(b, am, ap, L2, L1) == 0)
        nfused_below += Lf < inf[0]
        nequal += Lf == inf[0]
        ninf_below_naive += inf[0] < L1s + L2s
        rows.append((b, am, ap, L1s, L2s, Lf, L1s + L2s, inf, eag, eag0))
        print(f"  ({b},{am},{ap}) | {L1s} {L2s} | {Lf} | {L1s + L2s} | {inf[0]} ({inf[1]},{inf[2]},{inf[3]},{inf[4]}) | {eag[0]} ({eag[1]},{eag[2]},{eag[3]},{eag[4]}) | {eag0}")
    print(f"  {len(rows)} cells: fused below the informed chain at {nfused_below}, equal at {nequal}; "
          f"informed below naive at {ninf_below_naive}; eager below informed at "
          f"{sum(1 for r in rows if r[8][0] < r[7][0])}, eager at the fused floor at {sum(1 for r in rows if r[8][0] == r[5])}, "
          f"informed eager below naive eager at {sum(1 for r in rows if r[8][0] < r[9])}")
    ok(nfused_below > 0, "K4: the informed chain reads at the fused floor at every cell")
    if ninf_below_naive:
        print("  K5: the multiplier's choice buys the aligned adder a lookahead somewhere")

    print(f"\nwall {time.time() - t0:.1f}s; failures: {len(FAILURES)}")
    for f in FAILURES:
        print("  ", f)


if __name__ == "__main__":
    main()
