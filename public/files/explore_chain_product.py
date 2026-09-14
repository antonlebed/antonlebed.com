"""The chain's second pair: does the escape law compose past the
product-into-sum chain, at a product feeding a PRODUCT and at a pole
unit whose output leads its input feeding a product, or does a
nonlinear consumer or a producer's lead break the sum of floors?

THE QUESTION. explore_chain_delay.py prices the chain x y + z exactly:
a product reader feeding a sum reader pays the sum of the two units'
floors L1* + L2* whatever the multiplier does with its digit choice,
because the sum reader's death is a lattice clause the multiplier's
hull insets cannot empty within its slack budget, and the fused unit
reads below the chain at 15 of 20 cells. That was one pair, one linear
consumer. This rig runs the same escape law on two more pairs: a
NONLINEAR consumer, the product (x y) z, and a producer with a LEAD, the
reciprocal 1/(s + x) feeding a product, at the pairs where the
reciprocal emits before it reads.

CONVENTIONS, as in explore_chain_delay.py. Radix b, digit set
D = {-am..ap}, M-+ = a-+/(b-1), w = M- + M+, Mh = max(M-, M+), slack
rho = am + ap + 1 - b >= 1, w - 1 = rho/(b-1). A unit at lookahead c
and lead o emits its digit of weight b^(o-t) after reading its inputs
to position t + c; L = c + o is the lookahead in the output's own
scale and the margin law prices a unit at the least L with
b^L (w - 1) >= Lam w, Lam the sup over the window of the map's
gradient L1 norm (the many-stream theorem). A reader has no strategy:
it is dead at output level t iff the image of its input boxes
STRICTLY CONTAINS an overlap zone [q + 1 - M-, q + M+] of two
consecutive cells (in cell units), a condition on the streams alone.

LEG 1: THE PRODUCT CONSUMER, (x y) z. A product reader (unit 1,
lookahead L1, lead 0 where x y fits the root cell) emits the D-stream
P = x y; a product reader (unit 2) sees P and z and emits P z, whose
range [-M- Mh^2, M+ Mh^2] fits the root cell (Mh <= 1 on every
contiguous digit set), so unit 2's lead is 0 and L2 is its lookahead.
Unit 2 knows unit 1's rule, so of x y it reads the HULL of the fibre
of the P prefix it sees: an interval inside P's cell inset by
(alpha, beta) from the cell's ends, and inside the product's range
[-M- M+, Mh^2]. Its image at output level t, in cell units, is the
product of the hull and z's box, of width at most

    (|P| w + |z| (w - alpha - beta)) / b^L2  <=  (Mh^2 w + Mh (w - alpha - beta)) / b^L2,

the box width rate with one side narrowed, the sup at the corner
|P| = Mh^2, |z| = Mh, approached from below and dense in position (the
product's endpoints are dense at the emitted scale), so

    THE PRODUCT CONSUMER'S INSET CLAUSE: unit 2 is alive at L2 iff
    Mh^2 w + Mh (w - alpha - beta) <= b^L2 (w - 1),

and its ESCAPE COST is E2(L2) = max(0, w (1 + Mh) - b^L2 (w - 1)/Mh),
the least inset sum that makes it alive: a CONTINUOUS cost where the
sum consumer's was a lattice gap. The consumer's own floor L2* (zero
insets) is the margin law at Lam = Mh + Mh^2, the range-aware floor;
a generic product reader of two D-streams has Lam = 2 Mh, the same at
every cell of radices 2..5 but (4,2,2), where both floors are 2.

The producer's SLACK BUDGET is explore_chain_delay.py's,
S(L1) = w - 1 - 2 Mh w / b^L1: every image of an (x, y) prefix at
level n + L1 sits in some hull and consecutive hulls overlap by at
least the image width, so beta_n + alpha_(n+1) <= S on every
consecutive pair; the consumer's need is greatest at P's corner
|P| = Mh^2, which is exactly where the producer's images are widest,
so the two bind at the same place and the escape law reads

    THE ESCAPE LAW, second pair: the chain survives at (L1, L2)
    iff E2(L2) <= S(L1).

A run of hulls near the corner needs the inset (the need falls from
E2 at |P| = Mh^2 at rate w/Mh per unit of P), and summing the pair
constraint over a run of m hulls gives E2 <= S + O(1/m): a rule that
alternates its insets can beat the law at a finite level by at most
2 (w - 1)/m, which vanishes as the level grows. The fused unit x y z
has Lam = 3 Mh^2 and lead 0.

THE CLOSED-FORM PREDICTION, leg 1 (hand-derived before the engine;
the escape law's numbers, not a print), at the 13 cells of radices
2..5 with x y representable (am^2 <= ap (b - 1)): L1* = 2 at nine
cells and 1 at four ((4,3,3), (5,3,3), (5,3,4), (5,4,4)); L2* = L1* at
every cell; the fused floor 3 at (2,1,1) and 2 elsewhere. The
informed chain equals the naive chain L1* + L2* at 12 of 13 and reads
BELOW it at exactly one, (4,2,2), where at (L1, L2) = (2, 1) the
escape cost E2(1) = 2/9 EQUALS the budget S(2) = 2/9 — a knife edge
the law calls alive, since both bounds are approached from below —
so the chain reads at 3 against the naive 4 and the fused 2; the
fused unit sits below the informed chain at 9 cells (by one at
(2,1,1) and (4,2,2), by two at the seven others with L1* = 2) and
level with it at the four cells with L1* = 1. Every other pair below
the naive sum has E2 > S by at least 5/24 (the freeze wrote 4/27
here, S at L1 = 3 taken for S at L1 = 2; corrected post-run).

LEG 2: THE POLE'S LEAD, the reciprocal feeding a product. Unit 1 is
the reciprocal x -> 1/(s + x), s = M- + P, at pole distance P, lead
o1 the least integer with 1/P <= M+ b^o1 and floor L1* the least L
with b^L rho P^2 >= am + ap (explore_onestream_delay.py), lookahead
c1* = L1* - o1, NEGATIVE at 40 of the 120 sweep pairs: the reciprocal
emits its digit at level n after reading x to level n + c1* < n. Its
D-stream R' = R / b^o1 ranges over [Rmin, Rm], Rm = b^(-o1)/P in
(M+/b, M+]. Unit 2 reads R' and z and emits R' z (range inside the
root cell, lead 0). Two wirings:

  THE ALIGNED chain reads R' and z at the same level; unit 2's floor
  is the margin law at Lam = Rm + Mh, c2* the least c with
  (Rm + Mh) w <= b^c (w - 1); the chain's lookahead is c1* + c2* on x
  and c2* on z.

  THE EAGER chain reads R' as deep as it runs ahead: d = -c1* digits
  deeper than z, the R' box b^d times narrower, so unit 2's floor is
  c2' the least c with (Rm + Mh / b^d) w <= b^c (w - 1); the chain's
  lookahead is c2' on BOTH inputs (the R' digits at level t + c2' + d
  come from x read to level t + c2'), so the eager chain is a divider
  z/(s + x) assembled from two units, and its floor in the output's
  scale is L' = c2' + o1.

  The escape law on top of either: the reciprocal's budget at the pole
  side is S1(c1) = w - 1 - (Rm/P) w / b^c1 and the eager consumer's
  need is E2 = max(0, w + Rm w b^d/Mh - b^(c2 + d) (w - 1)/Mh) — the
  z box's own width times Rm is the term no inset touches.

  THE FUSED DIVIDER z/(s + x) has Lam = (P + Mh)/P^2 and lead of the
  least integer with 1/P <= b^of (explore_manystream_delay.py's
  Division), floor Lf* in its own scale; the chain's L' is at least
  Lf* at every pair, since b^L1* >= w/((w - 1) P^2) puts the chain's
  Mh term at or above the fused unit's Mh/P^2.

THE CLOSED-FORM PREDICTION, leg 2, at the 40 pairs with c1* < 0
(radices 2..5, P = j/(b - 1), j in {1, 2, 4, 8, 32, 128}): the eager
chain reads below the aligned chain, c2' < c2*, at 25 of 40 (by one
at 21, by two at 4: (3,2,1) P = 16, (4,3,1) P = 32/3 and 128/3,
(5,4,1) P = 32), never at radix 2 where Rm = 1 pins c2' = c2* = 2; the
escape law adds nothing at any of the 40 (the informed eager floor
equals c2'); the fused divider's Lf* is at or below L' at all 40.

THE SLATE, frozen before the engine.

P-A THE CONTROLS. (i) The scan engine on the product x y at zero
    insets, radices 2..4: a kill at L1* - 1 at some level within
    budget and none at L1*, at all 7 representable cells (the product
    census). (ii) The scan on the reciprocal at (o1, c1*) at the 40
    pairs: no kill at c1*; the kill at c1* - 1 counted (the region
    scan of explore_onestream_delay.py certified all 120 at input
    depths up to 10; a pair this scan's budget does not reach prints
    UNREACHED and is not a failure). (iii) The scan on the sum
    consumer with P's box inset and nested, at o = 1, radices 2..4,
    L2 in {1, 2}, six inset pairs: agrees with explore_chain_delay.py's
    inset clause at all 120 triples.
P-B THE RANGE-AWARE FLOOR. The product consumer P z with P confined to
    [-M- M+, Mh^2], zero insets: dead at L2* - 1 (a kill within
    budget) and alive at L2* (no kill to the budget) at the 13 cells
    of radices 2..5.
P-C THE INSET CLAUSE. The product consumer with P's box inset by
    (alpha, beta), nested and ranged, at L2 in {1, 2} and a grid of
    six inset pairs, radices 2..4: the scan kills within budget iff
    the clause says dead; a clause-dead triple the scan does not reach
    prints UNREACHED and is counted apart.
P-D THE PRICE TABLE, leg 1. Per cell: L1*, L2*, the fused floor, the
    naive chain, the informed chain by the escape law. At every pair
    (L1, L2) below the naive chain with L1 >= L1* that the law calls
    dead, radices 2..4, the covering search over ALL assignments of
    the level-(n + L1) product images to level-n hulls, each hull's
    tight extent SAFE against every z box at level n, finds no
    assignment at some n within the cap: a certificate against every
    multiplier rule. At the pair the law calls alive, (4,2,2) (2, 1):
    the consumer's scan at the escape insets (1/9, 1/9) finds no kill
    to the budget, the producer's narrowed scan at those insets kills
    at L1 - 1 and finds no kill at L1, and the covering search finds
    an assignment at every level it reaches.
P-E THE POLE'S LEAD, leg 2. At the 40 pairs: c1*, d, Rm, the aligned
    floor c2*, the eager floor c2', the fused divider's (of, Lf*) and
    the chain's L'. The eager consumer's death at c2' - 1 certified by
    the covering search over every reciprocal rule (x images at level
    n to R' hulls at level n + d, safe against every z box at level
    n), and its survival at c2' supported by the scan on the box model
    (R' boxes at level n + d cut to [Rmin, Rm], z at level n) to the
    budget; the aligned consumer the same at c2* - 1 and c2*.

KILLS, frozen as what this rig PRINTS.

K1 P-A prints a kill at a floor, a disagreement with the census, or
   a disagreement with the inset clause -> the scan engine is wrong;
   nothing below is read.
K2 P-B prints a kill at L2* -> the range-aware floor is misderived.
K3 P-C prints a scan kill at a triple the clause calls alive -> the
   product consumer's inset clause is wrong.
K4 THE COMPOSITION KILL. P-D prints a covering certificate (no
   assignment) at (4,2,2) (2, 1), or a consumer kill there at the
   escape insets -> the escape law calls alive a pair that is dead;
   or a pair the law calls dead at which the consumer's scan at
   S(L1)'s insets survives and the covering search finds assignments
   to the cap at every level, printed OPEN, is not a kill but leaves
   that pair's floor an upper bound.
K5 THE LEAD'S KILL. P-E prints c2' = c2* at all 40 pairs,
   or an eager consumer kill (a covering certificate) at c2' at a
   pair with c2' < c2* -> the lead buys the chain nothing the aligned
   sum did not count.
K6 P-E prints a pair where the eager consumer's death at c2' - 1 has
   no covering certificate within the cap -> the eager floor is an
   upper bound only there, printed OPEN.

POSITIVE CONTROL: P-A whole, read before any chain line.

TRANSPLANTS, marked: the escape law's form E <= S is carried from the
sum chain, where the budget bound at the corner and the consumer's
need were both uniform in position; here both are position-dependent
and the derivation above rests on their binding at the same corner.
The eager chain's one-lookahead gain is carried from the eager adder.

FINDINGS (entered post-run; every number below sits in this file's
printed output at radices 2..4 for the searches, 2..5 for the tables).

F1 THE CONTROLS HOLD. The product census: a kill at L1* - 1 at level
   1 to 3 and none at L1* to the budget, 7 of 7 cells. The reciprocal
   at (o1, c1*): no kill at c1* to level 8 at any of the 24 pairs of
   radices 2..4, a kill at c1* - 1 at level 0 to 3 at all 24. The sum
   consumer with P's box inset: 120 of 120 triples agree with the
   inset clause. P-A held; K1 never fired.

F2 THE RANGE-AWARE FLOOR HOLDS [rule at the 13 cells]. P z with P
   confined to the product's range: a kill at L2* - 1 at level 1 to 4
   and none at L2* to the budget at 13 of 13; L2* equals the generic
   product floor at every cell. K2 never fired.

F3 THE INSET CLAUSE HOLDS [rule at the scanned scope]. 36 of 36
   cell-lookahead-inset triples agree, none unreached, the clause
   read at the model's own P range (the inset root cut to the
   product's). K3 never fired.

F4 THE PRICE TABLE, leg 1 [the deaths a criterion where certified,
   the alive pair a rule]. 13 cells: the informed chain equals the
   naive chain at 12 and reads BELOW it at (4,2,2), the fused unit
   below the informed chain at 9 and level at 4, as predicted. Of the
   19 pairs below the naive sum at radices 2..4, the law calls 18 dead
   and the covering search certifies 16 of them, at n = 1 (11 pairs),
   2 (4) or 3 (1), and reaches the cap with assignments still found at
   two, (3,2,2) (2, 1) at n = 4 and (4,2,3) (2, 1) at n = 3, the two
   dead pairs with the smallest gaps E2 - S (4/9 and 5/24): their
   floors are upper bounds at the cap. The one pair the law calls
   alive, (4,2,2) (2, 1) at E2 = S = 2/9: the covering search finds
   an assignment at every level to the cap (n <= 2); the consumer at
   insets (1/9, 1/9) is clear to level 4; the narrowed producer at
   those insets kills at L1 - 1 = 1 at level 2 and is clear at L1 = 2
   to level 4. K4 never fired: the multiplier's choice IS a design
   axis for a product consumer, at the one cell where the continuous
   escape cost meets the budget, and the chain reads (x y) z at 3
   there, one above the fused 2 and one below the naive 4.

F5 THE POLE'S LEAD, leg 2 [the eager floor a criterion at the 19
   certified pairs, a rule at the 40]. The eager chain reads below the
   aligned chain at 25 of 40 (by two at 4), as predicted; the escape
   law adds nothing. At the 24 pairs of radices 2..4: the eager
   consumer is clear at c2' to level 3..7 at all 24; its death at
   c2' - 1 is certified against every reciprocal rule at 19, at n = 0
   to 5, and OPEN at 5 (K6): (2,1,1) P = 128, assignments found to
   n = 5 (the excess 1/32 of a cell at d = 6), and four capped at
   n = 3 or 4 at radix 4. All 15 searched pairs with c2' < c2* are
   certified. The aligned death at c2* - 1 is certified at 13 of 24
   and capped at 11. The fused divider's Lf* sits below the chain's
   L' at 7 pairs and equals it at 33, above at none: two units in
   series, the second reading the first's lead, match the fused
   divider's floor in the output's scale at 33 of 40.

VERDICT. The escape law composes: at a product consumer it is E2 <=
S with a continuous escape cost, dead at every pair below the naive
sum but one, and at that one the consumer's knowledge of the
multiplier's rule buys a lookahead the aligned adder never got — the
first ALIGNED chain in the corpus that reads below the sum of its
units' floors (the eager adder did so only by reading z early). A pole's lead propagates by DEPTH, not by digit choice: the
consumer reading the reciprocal's stream as far ahead as it runs
reads at the product floor of a narrower box, one or two lookaheads
under the aligned sum at 25 of 40 pairs, and saturates at the term
its other input's own width sets; the assembled divider matches the
fused divider's floor at 33 of 40. Both hypotheses survive their
kills and both are bounded by what they found.

RUN RECORD: pure Python, exact rationals, standard library; under
memwatch, peak commit 199.3 MB against the 512 MB default, wall 139 s
at the defaults (4, 5, 1000000, 400000). A run at IMG_CAP 2500000 was
killed by memwatch at 514 MB commit (the level-6 product images of
(3,2,2)) and was not repeated; the image cap stays at 1000000 and the
two pairs it leaves open are recorded as open. Prints reproduced by:
python prime/code/explore_chain_product.py [BMAX NMAX IMG_CAP COVER_CAP]
"""

import math
import os
import sys
import time
from fractions import Fraction as Fr

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from explore_chain_delay import (window, margin_L, slack_budget,   # noqa: E402
                                 narrowed_L, census, representable_xy,
                                 sum_law, death_interval)

FAILURES = []
SCAN_BUDGET = 400_000     # prefix pairs per scan level
IMG_CAP = 1_000_000       # (x, y) prefix pairs the covering search enumerates
COVER_CAP = 400_000       # hulls x z boxes a covering level may cost


def ok(cond, msg):
    if not cond:
        FAILURES.append(msg)
        print(f"  FAIL: {msg}")


# ---------------------------------------------------------- closed forms

def least_L(b, w, need):
    """Least L in Z with b^L (w - 1) >= need."""
    L = 0
    while Fr(b) ** L * (w - 1) < need:
        L += 1
    while Fr(b) ** (L - 1) * (w - 1) >= need:
        L -= 1
    return L


def escape_cost_product(b, am, ap, L2):
    Mm, Mp, w, Mh = window(b, am, ap)
    return max(Fr(0), w * (1 + Mh) - Fr(b) ** L2 * (w - 1) / Mh)


def chain_floor_product(b, am, ap, span=6):
    """(L1 + L2, L1, L2, E2, S) least by the escape law, leg 1."""
    Mm, Mp, w, Mh = window(b, am, ap)
    L1s = margin_L(b, am, ap, 2 * Mh)
    best = None
    for L1 in range(L1s, L1s + span):
        S = slack_budget(b, am, ap, L1)
        for L2 in range(0, span):
            E = escape_cost_product(b, am, ap, L2)
            if E <= S and (best is None or L1 + L2 < best[0]):
                best = (L1 + L2, L1, L2, E, S)
    return best


def recip_params(b, am, ap, P):
    """(o1, L1*, c1*, Rmin, Rm) of the reciprocal 1/(M- + P + x)."""
    Mm, Mp, w, Mh = window(b, am, ap)
    rho, wsum = am + ap + 1 - b, am + ap
    o = 0
    while 1 / P <= Mp * Fr(b) ** (o - 1):
        o -= 1
    while 1 / P > Mp * Fr(b) ** o:
        o += 1
    L = 0
    while Fr(b) ** L * rho * P * P < wsum:
        L += 1
    while Fr(b) ** (L - 1) * rho * P * P >= wsum:
        L -= 1
    return o, L, L - o, Fr(b) ** (-o) / (P + w), Fr(b) ** (-o) / P


def divider_params(b, am, ap, P):
    """(of, Lf*) of the fused divider z/(M- + P + x)."""
    Mm, Mp, w, Mh = window(b, am, ap)
    of = 0
    while 1 / P <= Fr(b) ** (of - 1):
        of -= 1
    while 1 / P > Fr(b) ** of:
        of += 1
    return of, least_L(b, w, (P + Mh) / (P * P) * w)


def pole_pairs(bmax):
    out = []
    for (b, am, ap) in census(bmax):
        for j in (1, 2, 4, 8, 32, 128):
            P = Fr(j, b - 1)
            o, L, c1, Rmin, Rm = recip_params(b, am, ap, P)
            if c1 < 0:
                out.append((b, am, ap, P))
    return out


# ------------------------------------------------------------ the scans

def zone_dead(lo, hi, Mm, Mp):
    """Does [lo, hi] (cell units) strictly contain a zone
    [q + 1 - Mm, q + Mp] for some integer q?  With Mm, Mp the cell's
    own half-widths; an inset cell passes Mm - alpha, Mp - beta."""
    q = math.floor(lo + Mm - 1) + 1          # least q with q + 1 - Mm > lo
    return q < hi - Mp


def prefix_range(b, am, ap, n):
    R = (b ** n - 1) // (b - 1)
    return -am * R, ap * R


def boxes_at(b, am, ap, n, inset=(Fr(0), Fr(0)), rng=None):
    """The nested inset boxes of every n-digit prefix, cut to rng:
    a list of (lo, hi) in absolute units; a prefix whose box empties
    is dropped."""
    Mm, Mp = Fr(am, b - 1), Fr(ap, b - 1)
    a, c = inset
    root = (-Mm + a, Mp - c)
    if rng is not None:
        root = (max(root[0], rng[0]), min(root[1], rng[1]))
    level = [(0, root)] if root[0] <= root[1] else []
    digits = range(-am, ap + 1)
    for m in range(1, n + 1):
        s = Fr(1, b ** m)
        nxt = []
        for (u0, (plo, phi)) in level:
            for x in digits:
                u = b * u0 + x
                lo, hi = max(plo, (u - Mm + a) * s), min(phi, (u + Mp - c) * s)
                if lo <= hi:
                    nxt.append((u, (lo, hi)))
        level = nxt
    return [bx for (u, bx) in level]


def plain_boxes(b, am, ap, n):
    Mm, Mp = Fr(am, b - 1), Fr(ap, b - 1)
    s = Fr(1, b ** n)
    lo_u, hi_u = prefix_range(b, am, ap, n)
    return [((u - Mm) * s, (u + Mp) * s) for u in range(lo_u, hi_u + 1)]


def prod_interval(A, B):
    cs = (A[0] * B[0], A[0] * B[1], A[1] * B[0], A[1] * B[1])
    return min(cs), max(cs)


def scan_two(b, am, ap, c, o, boxes1, boxes2, image, t, cell=(Fr(0), Fr(0))):
    """Is some pair of boxes' image (absolute) strictly containing a
    zone at output level t, lead o, cells inset by `cell`?  Returns
    the killing pair or None."""
    Mm, Mp = Fr(am, b - 1), Fr(ap, b - 1)
    e = Fr(b) ** (o - t)
    Mm2, Mp2 = Mm - cell[0], Mp - cell[1]
    for A in boxes1:
        for B in boxes2:
            lo, hi = image(A, B)
            if zone_dead(lo / e, hi / e, Mm2, Mp2):
                return A, B
    return None


def scan_levels(b, am, ap, c, o, mk_boxes1, mk_boxes2, image, nmin, nmax,
                budget=SCAN_BUDGET, cell=(Fr(0), Fr(0))):
    """Scan levels n = nmin..nmax (output level t = n - c >= 1), each
    within budget; returns ('kill', n) at the first kill, ('clear', n)
    with the last level fully scanned, or ('unreached', n) when the
    budget stops the scan before a kill."""
    last = None
    for n in range(nmin, nmax + 1):
        t = n - c
        if t < 1:
            continue
        B1, B2 = mk_boxes1(n), mk_boxes2(n)
        if len(B1) * len(B2) > budget:
            return ('unreached', n) if last is None else ('clear', last)
        if scan_two(b, am, ap, c, o, B1, B2, image, t, cell) is not None:
            return ('kill', n)
        last = n
    return ('clear', last) if last is not None else ('unreached', nmin)


# ------------------------------------------------ the covering search

def product_images(b, am, ap, m):
    """Every product image of an (x, y) prefix pair of length m."""
    boxes = plain_boxes(b, am, ap, m)
    out = set()
    for i, A in enumerate(boxes):
        for B in boxes[i:]:
            out.add(prod_interval(A, B))
    return sorted(out)


def recip_images(b, am, ap, P, o1, m):
    """Every image of an x prefix of length m under R' = b^-o1/(s + x)."""
    Mm = Fr(am, b - 1)
    s = Mm + P
    k = Fr(b) ** (-o1)
    return sorted((k / (s + x2), k / (s + x1)) for (x1, x2) in plain_boxes(b, am, ap, m))


def covering_exists(b, am, ap, imgs, n_hull, safe):
    """Is there an assignment of the images (sorted, absolute units)
    to hulls — the level-n_hull prefix boxes of the intermediate
    D-stream — with every hull's tight extent inside its box and
    safe(extent) true?  Each used hull starts at the leftmost
    uncovered image (an exchange argument makes this lossless) and
    reaches to the largest safe right end, so the search is exact."""
    Mm, Mp = Fr(am, b - 1), Fr(ap, b - 1)
    s = Fr(1, b ** n_hull)
    lo_u, hi_u = prefix_range(b, am, ap, n_hull)
    q_lo = max(lo_u, math.floor(imgs[0][0] / s - Mp) - 1)
    q_hi = min(hi_u, math.ceil(imgs[-1][1] / s + Mm) + 1)
    qs = list(range(q_lo, q_hi + 1))
    memo = {}

    def rec(idx, remaining):
        if not remaining:
            return True
        if idx == len(qs):
            return False
        key = (idx, len(remaining), remaining[0])
        if key in memo:
            return memo[key]
        q = qs[idx]
        bl, br = (q - Mm) * s, (q + Mp) * s
        l_min = remaining[0][0]
        res = False
        if l_min < bl:
            res = False
        else:
            # take: the largest safe right end
            if l_min <= br:
                rights = sorted({r for (l, r) in remaining if r <= br})
                lo_i, hi_i = 0, len(rights) - 1
                best = None
                while lo_i <= hi_i:
                    mid = (lo_i + hi_i) // 2
                    if safe((l_min, rights[mid])):
                        best, lo_i = rights[mid], mid + 1
                    else:
                        hi_i = mid - 1
                if best is not None:
                    rest = [I for I in remaining if I[1] > best]
                    if rec(idx + 1, rest):
                        res = True
            # skip: only if the leftmost image can still be taken later
            if not res and idx + 1 < len(qs) and l_min >= (q + 1 - Mm) * s:
                res = rec(idx + 1, remaining)
        memo[key] = res
        return res

    return rec(0, imgs)


def product_safe(b, am, ap, c, o, zboxes, t):
    """safe(extent): no z box at the given level makes extent x zbox
    strictly contain a zone at output level t."""
    Mm, Mp = Fr(am, b - 1), Fr(ap, b - 1)
    e = Fr(b) ** (o - t)

    def safe(ext):
        for Z in zboxes:
            lo, hi = prod_interval(ext, Z)
            if zone_dead(lo / e, hi / e, Mm, Mp):
                return False
        return True
    return safe


def certify_product_chain(b, am, ap, L1, L2, nmax):
    """Leg 1: no assignment of the level-(n + L1) product images to
    level-n hulls safe against the z boxes at level n, output level
    n - L2; returns ('dead', n), ('open', nmax) or ('capped', n)."""
    for n in range(max(1, L2 + 1), nmax + 1):
        lo_u, hi_u = prefix_range(b, am, ap, n + L1)
        zl, zh = prefix_range(b, am, ap, n)
        hl, hh = prefix_range(b, am, ap, n)
        if (hi_u - lo_u + 1) ** 2 > IMG_CAP or (zh - zl + 1) * (hh - hl + 1) > COVER_CAP:
            return ('capped', n)
        imgs = product_images(b, am, ap, n + L1)
        safe = product_safe(b, am, ap, L2, 0, plain_boxes(b, am, ap, n), n - L2)
        if not covering_exists(b, am, ap, imgs, n, safe):
            return ('dead', n)
    return ('open', nmax)


def certify_recip_chain(b, am, ap, P, o1, d, c2, nmax, eager=True):
    """Leg 2: x images at level n_x to R' hulls at level n_x + d, z at
    level n_z (= n_x eager, = n_x + d aligned), output level n_z - c2."""
    for n in range(0, nmax + 1):
        n_x = n
        n_h = n + d
        n_z = n_x if eager else n_h
        t = n_z - c2
        if t < 1:
            continue
        zl, zh = prefix_range(b, am, ap, n_z)
        hl, hh = prefix_range(b, am, ap, n_h)
        if (zh - zl + 1) * (hh - hl + 1) > COVER_CAP:
            return ('capped', n)
        imgs = recip_images(b, am, ap, P, o1, n_x)
        safe = product_safe(b, am, ap, c2, 0, plain_boxes(b, am, ap, n_z), t)
        if not covering_exists(b, am, ap, imgs, n_h, safe):
            return ('dead', n)
    return ('open', nmax)


# ------------------------------------------------------------------ main

def fmt(r):
    return f"{r[0]}@{r[1]}"


def main():
    global IMG_CAP, COVER_CAP
    bmax = int(sys.argv[1]) if len(sys.argv) > 1 else 4
    nmax = int(sys.argv[2]) if len(sys.argv) > 2 else 5
    if len(sys.argv) > 3:
        IMG_CAP = int(sys.argv[3])
    if len(sys.argv) > 4:
        COVER_CAP = int(sys.argv[4])
    t0 = time.time()
    prod = prod_interval

    print(f"=== P-A (i): the scan on the product x y, radices 2..{bmax}")
    for (b, am, ap) in census(bmax):
        if not representable_xy(b, am, ap):
            continue
        Mm, Mp, w, Mh = window(b, am, ap)
        L1s = margin_L(b, am, ap, 2 * Mh)
        mk = lambda n: plain_boxes(b, am, ap, n)
        kill = scan_levels(b, am, ap, L1s - 1, 0, mk, mk, prod, L1s, nmax + L1s)
        surv = scan_levels(b, am, ap, L1s, 0, mk, mk, prod, L1s + 1, nmax + L1s)
        ok(kill[0] == 'kill' and surv[0] != 'kill',
           f"K1 product census ({b},{am},{ap}) L1*={L1s}: {kill} / {surv}")
        print(f"  ({b},{am},{ap}) L1*={L1s} | at L1*-1: {fmt(kill)} | at L1*: {fmt(surv)}")

    print(f"\n=== P-A (ii): the scan on the reciprocal at (o1, c1*), the pairs with c1* < 0, radices 2..{bmax}")
    nk = nu = 0
    for (b, am, ap, P) in pole_pairs(bmax):
        o1, L1s, c1, Rmin, Rm = recip_params(b, am, ap, P)
        Mm = Fr(am, b - 1)
        s = Mm + P

        def rimg(A, B, s=s):
            return 1 / (s + A[1]), 1 / (s + A[0])
        mk = lambda n: plain_boxes(b, am, ap, n)
        one = lambda n: [(Fr(0), Fr(0))]
        kill = scan_levels(b, am, ap, c1 - 1, o1, mk, one, rimg, 0, nmax + 4)
        surv = scan_levels(b, am, ap, c1, o1, mk, one, rimg, 0, nmax + 4)
        ok(surv[0] != 'kill', f"K1 reciprocal ({b},{am},{ap}) P={P} kill at c1*={c1}: {surv}")
        nk += kill[0] == 'kill'
        nu += kill[0] != 'kill'
        print(f"  ({b},{am},{ap}) P={P} o1={o1} c1*={c1} | at c1*-1: {fmt(kill)} | at c1*: {fmt(surv)}")
    print(f"  {nk} pairs killed at c1*-1, {nu} unreached; no kill at c1* at any")

    print(f"\n=== P-A (iii): the scan on the sum consumer with P's box inset, against the inset clause, radices 2..{bmax}")
    grid = [(Fr(0), Fr(0)), (Fr(1, 2), Fr(0)), (Fr(0), Fr(1, 2)), (Fr(1, 3), Fr(1, 3)), (Fr(1), Fr(0)), (Fr(2, 3), Fr(1, 3))]
    agree = tot = 0
    for (b, am, ap) in census(bmax):
        for L2 in (1, 2):
            for alpha, beta in grid:
                lo, hi, q = death_interval(b, am, ap, L2)
                pred_dead = math.floor(lo + beta) + 1 < hi - alpha
                mk1 = lambda n, a=alpha, c=beta: boxes_at(b, am, ap, n, (a, c))
                mk2 = lambda n: plain_boxes(b, am, ap, n)
                r = scan_levels(b, am, ap, L2 - 1, 1, mk1, mk2,
                                lambda A, B: (A[0] + B[0], A[1] + B[1]), 1, nmax)
                tot += 1
                if (r[0] == 'kill') == pred_dead:
                    agree += 1
                else:
                    ok(False, f"K1 inset sum ({b},{am},{ap}) L2={L2} insets ({alpha},{beta}): clause {'dead' if pred_dead else 'alive'}, scan {r}")
    print(f"  {tot} triples, agree {agree}")
    if FAILURES:
        print("\nPOSITIVE CONTROL FAILED; nothing below is read")
        for f in FAILURES:
            print("  ", f)
        return

    print("\n=== P-B: the range-aware product consumer P z, zero insets, radices 2..5")
    for (b, am, ap) in census(5):
        if not representable_xy(b, am, ap):
            continue
        Mm, Mp, w, Mh = window(b, am, ap)
        L2s = least_L(b, w, (Mh + Mh * Mh) * w)
        rng = (-Mm * Mp, Mh * Mh)
        mk1 = lambda n: boxes_at(b, am, ap, n, rng=rng)
        mk2 = lambda n: plain_boxes(b, am, ap, n)
        kill = scan_levels(b, am, ap, L2s - 1, 0, mk1, mk2, prod, L2s, nmax + L2s)
        surv = scan_levels(b, am, ap, L2s, 0, mk1, mk2, prod, L2s + 1, nmax + L2s)
        ok(surv[0] != 'kill', f"K2 range-aware consumer ({b},{am},{ap}) kill at L2*={L2s}: {surv}")
        print(f"  ({b},{am},{ap}) L2*={L2s} (generic {margin_L(b, am, ap, 2 * Mh)}) | at L2*-1: {fmt(kill)} | at L2*: {fmt(surv)}")

    print(f"\n=== P-C: the product consumer's inset clause, radices 2..{bmax}")
    agree = tot = unreached = 0
    for (b, am, ap) in census(bmax):
        if not representable_xy(b, am, ap):
            continue
        Mm, Mp, w, Mh = window(b, am, ap)
        rng = (-Mm * Mp, Mh * Mh)
        for L2 in (1, 2):
            for alpha, beta in grid:
                if alpha + beta >= w - 1:
                    continue
                # the model's own P range: the inset root cut to the product's
                Pabs = max(min(Mh * Mh, Mp - beta), min(Mm * Mp, Mm - alpha))
                pred_dead = Pabs * w + Mh * (w - alpha - beta) > Fr(b) ** L2 * (w - 1)
                mk1 = lambda n, a=alpha, c=beta: boxes_at(b, am, ap, n, (a, c), rng)
                mk2 = lambda n: plain_boxes(b, am, ap, n)
                r = scan_levels(b, am, ap, L2, 0, mk1, mk2, prod, L2 + 1, nmax + L2)
                tot += 1
                if r[0] == 'kill' and not pred_dead:
                    ok(False, f"K3 inset product ({b},{am},{ap}) L2={L2} insets ({alpha},{beta}): clause alive, scan {r}")
                elif r[0] == 'kill' or not pred_dead:
                    agree += 1
                else:
                    unreached += 1
                    print(f"  UNREACHED ({b},{am},{ap}) L2={L2} insets ({alpha},{beta}): clause dead by "
                          f"{Pabs * w + Mh * (w - alpha - beta) - Fr(b) ** L2 * (w - 1)}, scan {fmt(r)}")
    print(f"  {tot} triples, agree {agree}, unreached {unreached}")

    print("\n=== P-D: the price table, leg 1, radices 2..5; the searches at radices 2..{}".format(bmax))
    print("  cell | L1* L2* | fused | naive | informed (L1,L2,E2,S) | fused-informed")
    nbelow = nequal = ninf = 0
    for (b, am, ap) in census(5):
        if not representable_xy(b, am, ap):
            continue
        Mm, Mp, w, Mh = window(b, am, ap)
        L1s, L2s = margin_L(b, am, ap, 2 * Mh), least_L(b, w, (Mh + Mh * Mh) * w)
        Lf = least_L(b, w, 3 * Mh * Mh * w)
        inf = chain_floor_product(b, am, ap)
        nbelow += Lf < inf[0]
        nequal += Lf == inf[0]
        ninf += inf[0] < L1s + L2s
        print(f"  ({b},{am},{ap}) | {L1s} {L2s} | {Lf} | {L1s + L2s} | {inf[0]} ({inf[1]},{inf[2]},{inf[3]},{inf[4]}) | {Lf - inf[0]}")
    print(f"  13 cells: fused below the informed chain at {nbelow}, equal at {nequal}; informed below naive at {ninf}")
    print("  -- the pairs below the naive chain")
    for (b, am, ap) in census(bmax):
        if not representable_xy(b, am, ap):
            continue
        Mm, Mp, w, Mh = window(b, am, ap)
        L1s, L2s = margin_L(b, am, ap, 2 * Mh), least_L(b, w, (Mh + Mh * Mh) * w)
        rng = (-Mm * Mp, Mh * Mh)
        for L1 in range(L1s, L1s + L2s):
            for L2 in range(0, L1s + L2s - L1):
                E, S = escape_cost_product(b, am, ap, L2), slack_budget(b, am, ap, L1)
                verdict = 'alive' if E <= S else 'dead'
                r = certify_product_chain(b, am, ap, L1, L2, nmax)
                line = f"  ({b},{am},{ap}) (L1,L2)=({L1},{L2}) E2={E} S={S} law {verdict} | covering {fmt(r)}"
                if verdict == 'dead':
                    if r[0] == 'dead':
                        line += " certified"
                    else:
                        line += " K4? OPEN: an upper bound only"
                else:
                    ok(r[0] != 'dead', f"K4 covering certificate at a law-alive pair ({b},{am},{ap}) ({L1},{L2}): {r}")
                    half = E / 2
                    mk1 = lambda n, h=half: boxes_at(b, am, ap, n, (h, h), rng)
                    mk2 = lambda n: plain_boxes(b, am, ap, n)
                    cs = scan_levels(b, am, ap, L2, 0, mk1, mk2, prod, L2 + 1, nmax + L2)
                    ok(cs[0] != 'kill', f"K4 consumer kill at the escape insets ({b},{am},{ap}) ({L1},{L2}): {cs}")
                    Ln = narrowed_L(b, am, ap, half, half)
                    mk = lambda n: plain_boxes(b, am, ap, n)
                    pk = scan_levels(b, am, ap, Ln - 1, 0, mk, mk, prod, Ln, nmax + Ln, cell=(half, half))
                    ps = scan_levels(b, am, ap, Ln, 0, mk, mk, prod, Ln + 1, nmax + Ln, cell=(half, half))
                    ok(ps[0] != 'kill', f"K4 producer kill at the narrowed law's L={Ln} ({b},{am},{ap}) insets ({half},{half}): {ps}")
                    line += (f" | consumer at insets ({half},{half}): {fmt(cs)} | producer narrowed L={Ln}: "
                             f"at L-1 {fmt(pk)}, at L {fmt(ps)}")
                print(line)

    print(f"\n=== P-E: the pole's lead, leg 2, the pairs with c1* < 0, radices 2..5; the searches at radices 2..{bmax}")
    print("  cell P | o1 c1* d | Rm | aligned c2* | eager c2' | chain L' | fused divider (of, Lf*) | aligned: kill/surv | eager: kill/surv")
    rows = []
    for (b, am, ap, P) in pole_pairs(5):
        Mm, Mp, w, Mh = window(b, am, ap)
        o1, L1s, c1, Rmin, Rm = recip_params(b, am, ap, P)
        d = -c1
        c2s = least_L(b, w, (Rm + Mh) * w)
        c2e = least_L(b, w, (Rm + Mh / Fr(b) ** d) * w)
        of, Lf = divider_params(b, am, ap, P)
        Lp = c2e + o1
        rows.append((b, am, ap, P, c2s, c2e, Lp, Lf))
        line = f"  ({b},{am},{ap}) P={P} | {o1} {c1} {d} | {Rm} | {c2s} | {c2e} | {Lp} | ({of}, {Lf})"
        if b <= bmax:
            rng = (Rmin, Rm)
            mkz = lambda n: plain_boxes(b, am, ap, n)
            # aligned: R' boxes and z at the same level
            mka = lambda n: boxes_at(b, am, ap, n, rng=rng)
            ak = certify_recip_chain(b, am, ap, P, o1, d, c2s - 1, nmax, eager=False)
            asv = scan_levels(b, am, ap, c2s, 0, mka, mkz, prod, c2s + 1, nmax + c2s + d)
            ok(asv[0] != 'kill', f"K1? aligned consumer kill at c2*={c2s} ({b},{am},{ap}) P={P}: {asv}")
            # eager: R' boxes d deeper than z
            mke = lambda n: boxes_at(b, am, ap, n + d, rng=rng)
            ek = certify_recip_chain(b, am, ap, P, o1, d, c2e - 1, nmax, eager=True)
            esv = scan_levels(b, am, ap, c2e, 0, mke, mkz, prod, c2e + 1, nmax + c2e)
            ok(esv[0] != 'kill', f"K5 eager consumer kill at c2'={c2e} ({b},{am},{ap}) P={P}: {esv}")
            line += f" | {fmt(ak)}/{fmt(asv)} | {fmt(ek)}/{fmt(esv)}"
            if ek[0] != 'dead':
                line += " K6 OPEN"
        print(line)
    ng = sum(1 for r in rows if r[5] < r[4])
    print(f"  {len(rows)} pairs: eager below aligned at {ng} (by two at {sum(1 for r in rows if r[4] - r[5] >= 2)}); "
          f"fused divider below the chain's L' at {sum(1 for r in rows if r[7] < r[6])}, equal at {sum(1 for r in rows if r[7] == r[6])}, "
          f"above at {sum(1 for r in rows if r[7] > r[6])}")
    ok(ng > 0, "K5: the eager chain equals the aligned chain at every pair")

    print(f"\nwall {time.time() - t0:.1f}s; failures: {len(FAILURES)}")
    for f in FAILURES:
        print("  ", f)


if __name__ == "__main__":
    main()
