"""The reciprocal-feeding-product chain recertified by the streaming
walk: does the two-query covering walk reproduce every recorded
verdict of the pole's-lead consumer at the 24 pairs of radices 2..4,
and close the sixteen certificates the old certifier capped or left
open?

THE QUESTION. explore_chain_product.py leg 2 wires the reciprocal
x -> 1/(s + x), s = M- + P, into a product consumer, eager (the
consumer reading the reciprocal's stream d = -c1* digits deeper than
z) or aligned, and certifies the consumer's death one below its floor
by a covering search: the reciprocal's images of every x prefix at
level n must be assigned to hulls of the R' stream at level n + d,
each hull's tight extent inside its box and SAFE against every z box
(at level n eager, n + d aligned), safe meaning the extent times the z
box strictly contains no overlap zone at the output level. That
certifier caps a level whose hulls times z boxes exceed 400,000, so
the eager death is certified at 19 of the 24 pairs and the aligned
death at 13, the rest capped at levels 2 to 4 or, at one pair, open
at level 5. explore_chain_certify.py's reduction -- the search's state
is (hull, last reach), the safe test is monotone in the reach, and the
images enter only through two queries -- is rewritten here for the
one-argument producer: one image per x prefix, both ends strictly
falling in the prefix, so the image set is its own antichain, the
largest right end at or below a value is the image at the least prefix
whose right end lies there, and the least left end beyond it is the
next image's; the cost that capped the old search was never the image
set but the safe test, one Python pass over the z boxes in exact
rationals per probe. Here the safe test runs vectorised over the z
boxes in scaled integers (the extent's ends are image ends, rationals
with one denominator each, so every corner product and every zone
edge is an integer over the extent's denominator times the z box's;
the magnitude is bounded in Python integers before each level and the
arrays fall back to Python-object dtype past a machine word), behind
a width prefilter: a z box can kill only if its product with the
extent is wider than a zone, and that width rises with |z| on each
side of zero, so the boxes tested are those above a threshold, the
boxes straddling zero tested whole. The walk itself is the old
search's exchange argument -- each used hull starts at the leftmost
uncovered image and reaches to the largest safe right end -- run as
a forward pass over the hulls with the set of reachable "first
uncovered image" indices, no recursion, each state met once.

CONVENTIONS, as in explore_chain_product.py: digit set {-a^-..a^+},
M-+ = a-+/(b - 1), w = M- + M+, Mh = max(M-, M+); the reciprocal at
pole distance P = j/(b - 1), lead o1, lookahead c1* = L1* - o1 < 0,
d = -c1*, its D-stream R' = b^-o1/(s + x) in [Rmin, Rm]; the aligned
floor c2* the least c with (Rm + Mh) w <= b^c (w - 1), the eager
floor c2' the least c with (Rm + Mh/b^d) w <= b^c (w - 1); a
certificate at c2 - 1 runs levels n = 0, 1, ... with x at level n,
hulls at n + d, z at n (eager) or n + d (aligned), output level t =
n_z - c2 + 1 >= 1 else the level is skipped; ('dead', n) at the first
level with no assignment, ('open', n) with an assignment at every
level to n. THE GAP of a pair, as the record prices it: the floor
condition's excess at the certified lookahead, ((Rm + Mh/b^d) w -
b^(c2' - 1) (w - 1))/Mh eager and ((Rm + Mh) w - b^(c2* - 1)
(w - 1))/Mh aligned, the excess of a cell that the record's "1/32 of a
cell at d = 6" names at (2,1,1) P = 128. The finite-level slack at a
level is 2 (w - 1)/m, m the hull count the walk visits.

PREDICTIONS, fixed before the run.
 P1 (the control): at the 19 eager deaths and the 13 aligned deaths
    the record certifies, the walk prints ('dead', n) at the recorded
    n; and the vectorised safe test agrees with the old product_safe
    at 200 extents drawn from the image ends at every pair, at the
    least of the recorded level and 3.
 P2 (the gain, eager): the four eager pairs capped at level 4 --
    (4,2,3) and (4,3,2) at P = 128/3, (4,3,1) at P = 8/3, (4,3,3) at
    P = 32/3 -- die within two levels past the cap (a TRANSPLANT from
    leg 1, whose law-dead pairs at radices 2..4 all died by level 5);
    (2,1,1) at P = 128, open at level 5 with a gap of 1/32 and d = 6,
    dies at the first level where 2 (w - 1)/m falls under 1/32, at
    w = 2 the first level with m >= 64 hulls.
 P3 (the gain, aligned): the eleven capped aligned deaths close within
    two levels past their caps.
 P4 (the priced-certificate line, its second read, a TRANSPLANT from
    the product chain where the slack 2 (w - 1)/m matched the gap at
    the level reached): every death level printed here, old or new,
    lies within one of the least level whose slack is at or under the
    pair's gap; the table prints both beside each verdict.

KILLS, as prints.
 K1: a walk verdict off the recorded one at a certified pair, or the
     two safe tests disagreeing at any extent -> the walk (or the
     record) is wrong; nothing below is read.
 K2: an open pair still open at the run's element budget -> not a
     kill; OPEN printed with the level reached, an upper bound.
 K3 (P4): the printed death level off the slack's level by more than
     one at three or more pairs -> the priced line's slack is not this
     chain's, or its m is not the visited hull count.

POSITIVE CONTROL: P1's 32 verdicts and the safe-test agreement, read
before any open pair's line.

FINDINGS (entered after the run; every number below is in this
file's print at NMAX = 10).

F1 THE CONTROL HOLDS. All 32 recorded deaths -- the 19 eager and the
   13 aligned -- reproduced at the recorded level, and the vectorised
   safe test agrees with product_safe at every one of the 200 extents
   drawn at every pair. K1 never fired.
F2 THE EAGER CERTIFICATE IS COMPLETE. All five open eager deaths
   close: (4,2,3) and (4,3,2) at P = 128/3 and (4,3,1) at P = 8/3 die
   at level 4, the level the old certifier capped, (4,3,3) at P = 32/3
   at level 5 (2047 images, 248 hulls), and (2,1,1) at P = 128 at
   level 7 (255 images, 129 hulls, 255 z boxes), one past the first
   level with 64 hulls. P2 held; the eager consumer's death one below
   its floor is certified against every reciprocal rule at all 24
   pairs.
F3 THE ALIGNED CERTIFICATE CLOSES AT FIVE OF ELEVEN AND STAYS OPEN AT
   SIX. (3,1,2) at P = 64, (3,2,1) at P = 16 and 64 and (4,1,3) at
   P = 128/3 die at level 3, their cap, and (3,2,1) at P = 4 at level
   6 (154 hulls, 3280 z boxes); the six with a gap of an eighth or a
   twelfth of a cell -- (3,2,2) at P = 16, (4,2,2) at P = 32/3 and
   128/3, (4,3,1) at P = 8/3, 32/3 and 128/3 -- find an assignment at
   every level reached, to level 9 at (3,2,2) (11078 hulls, 354293 z
   boxes, half a second) and to level 7 or 8 at the radix-4 five (up
   to 1.4 million z boxes at level 7), and stop at the element budget
   (K2: OPEN, upper bounds). P3 held at five and failed at six; open
   is exactly gap <= 1/8 among the eleven.
F4 THE SLACK DOES NOT PRICE THIS CHAIN. K3 fired at 16 of the 42
   deaths: the aligned deaths at ten pairs, where the slack level is
   0 or 1 while the deaths come at levels 2 to 6 (the gaps from 9/32
   to 2), and the eager deaths at six; the six open aligned pairs
   sit at levels 7 to 9 against slack levels 1 to 3. P4 died.
F5 THE PRICED LINE AT ITS OWN KILL: SURVIVES BY LETTER, EMPTY IN
   SUBSTANCE. Over the product chain's 18 deaths the slack level is
   within one of the death level at 16 and off by three at 2, (3,2,2)
   and (4,2,3) at (2, 1), both dying at level 5 against a slack level
   of 2 (gaps 4/9 and 5/24). K4 did not fire (three were needed), but
   the 16 agreements are the pairs dying at level 1 to 3 under a gap
   above 1, where every pricing agrees; at the only two deaths the
   pricing could inform, it misses by three.

VERDICT. The walk is the certifier the record wanted: every verdict
the old search reached is reproduced, the eager death is now certified
at all 24 pairs, and the aligned at 18; the cost is the hull count
times a bisection, the z boxes entering only above the width
threshold, so a level runs in under a second where the old engine
capped. What the walk cannot yet say is a death at the six aligned
pairs whose excess is at most an eighth of a cell: assignments exist
to levels 7 to 9, thousands of hulls deep, and no closed form of the
slack predicts where, or whether, they end. The finite-level slack
2 (w - 1)/m prices neither this chain nor the product chain's two
deep deaths.

RUN RECORD: pure Python and numpy, exact rationals for the ends and
scaled integers for the safe test; under memwatch, peak commit
179.2 MB, wall 11.4 s at NMAX = 10.
Run: python prime/code/explore_chain_recip.py [NMAX] [BUDGET]
  NMAX the deepest level tried (default 9); BUDGET the element
  operations a level may cost, visited hulls x z boxes x probes
  (default 1e11), a level past it printed capped.
"""

import bisect
import math
import os
import random
import sys
import time
from fractions import Fraction as Fr
os.environ["OPENBLAS_NUM_THREADS"] = "1"
import numpy as np   # noqa: E402

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from explore_chain_delay import window   # noqa: E402
from explore_chain_product import (least_L, recip_params, pole_pairs,   # noqa: E402
                                   prefix_range, plain_boxes, product_safe)

FAILURES = []


def ok(cond, msg):
    if not cond:
        FAILURES.append(msg)
        print(f"  FAIL: {msg}")


# explore_chain_product.py's leg 2 print at radices 2..4, nmax 5, its
# caps: (b, a-, a+, P as printed) -> (aligned verdict, eager verdict)
RECORDED = {
    (2, 1, 1, '4'): (('dead', 3), ('dead', 4)),
    (2, 1, 1, '8'): (('dead', 2), ('dead', 4)),
    (2, 1, 1, '32'): (('dead', 1), ('dead', 5)),
    (2, 1, 1, '128'): (('dead', 1), ('open', 5)),
    (3, 1, 2, '16'): (('dead', 2), ('dead', 1)),
    (3, 1, 2, '64'): (('capped', 3), ('dead', 2)),
    (3, 2, 1, '4'): (('capped', 5), ('dead', 2)),
    (3, 2, 1, '16'): (('capped', 3), ('dead', 1)),
    (3, 2, 1, '64'): (('capped', 3), ('dead', 2)),
    (3, 2, 2, '16'): (('capped', 4), ('dead', 2)),
    (3, 2, 2, '64'): (('dead', 0), ('dead', 0)),
    (4, 1, 3, '32/3'): (('dead', 3), ('dead', 1)),
    (4, 1, 3, '128/3'): (('capped', 3), ('dead', 1)),
    (4, 2, 2, '32/3'): (('capped', 4), ('dead', 2)),
    (4, 2, 2, '128/3'): (('capped', 3), ('dead', 2)),
    (4, 2, 3, '32/3'): (('dead', 1), ('dead', 2)),
    (4, 2, 3, '128/3'): (('dead', 1), ('capped', 4)),
    (4, 3, 1, '8/3'): (('capped', 4), ('capped', 4)),
    (4, 3, 1, '32/3'): (('capped', 3), ('dead', 1)),
    (4, 3, 1, '128/3'): (('capped', 2), ('dead', 1)),
    (4, 3, 2, '32/3'): (('dead', 1), ('dead', 2)),
    (4, 3, 2, '128/3'): (('dead', 1), ('capped', 4)),
    (4, 3, 3, '32/3'): (('dead', 2), ('capped', 4)),
    (4, 3, 3, '128/3'): (('dead', 1), ('dead', 0)),
}


# ------------------------------------------------------------- the images

def recip_ends(b, am, ap, P, o1, m):
    """The image ends of every x prefix at level m under R' =
    b^-o1/(s + x), as Fractions, sorted by left end rising (the
    prefix falling); both lists rise, no image contains another."""
    Mm, Mp = Fr(am, b - 1), Fr(ap, b - 1)
    s = Mm + P
    k = Fr(b) ** (-o1)
    sc = Fr(1, b ** m)
    lo_u, hi_u = prefix_range(b, am, ap, m)
    L = [k / (s + (u + Mp) * sc) for u in range(hi_u, lo_u - 1, -1)]
    R = [k / (s + (u - Mm) * sc) for u in range(hi_u, lo_u - 1, -1)]
    return L, R


# ---------------------------------------------------------- the safe test

class ZoneSafe:
    """safe(l, r) for a positive extent [l, r] given as Fractions: no
    z box at level n_z makes [l, r] x zbox strictly contain a zone at
    output level t.  Vectorised over the z boxes in scaled integers,
    behind the width prefilter."""

    def __init__(self, b, am, ap, n_z, t, max_num, max_den):
        self.b, self.am, self.ap, self.t = b, am, ap, t
        zl, zh = prefix_range(b, am, ap, n_z)
        zq = np.arange(zl, zh + 1, dtype=np.int64)
        ZL = (b - 1) * zq - am
        ZH = (b - 1) * zq + ap
        self.zq0 = zl
        self.Dz = (b - 1) * b ** n_z
        self.bt = b ** t
        self.wm1 = Fr(am + ap, b - 1) - 1
        self.pos0 = int(np.searchsorted(ZL, 0))            # first index with ZL >= 0
        self.neg1 = int(np.searchsorted(ZH, 0, side='right'))   # one past the last with ZH <= 0
        # the magnitude bound: every product below, in Python integers
        Zmax = int(max(abs(int(ZL[0])), int(ZH[-1])))
        n_side = max_num * Zmax * self.bt * (b - 1)
        d_side = (b + max_den * self.Dz) * (Zmax * self.bt * max_num + 2 * max_den * self.Dz) * b
        self.big = max(n_side, d_side) >= 2 ** 62
        if self.big:
            ZL = ZL.astype(object)
            ZH = ZH.astype(object)
        self.ZL, self.ZH = ZL, ZH

    def _dead(self, nl, dl, nh, dh, ZL, ZH):
        """Any zone strictly inside [nl ZL/(dl Dz), nh ZH/(dh Dz)] at
        output level t?  nl, dl, nh, dh Python integers."""
        b, am, ap, bt = self.b, self.am, self.ap, self.bt
        D_lo = dl * self.Dz
        D_hi = dh * self.Dz
        q = (ZL * (nl * bt * (b - 1)) + (am - (b - 1)) * D_lo) // ((b - 1) * D_lo) + 1
        return bool(np.any((q * (b - 1) + ap) * D_hi < ZH * (nh * bt * (b - 1))))

    def __call__(self, l, r):
        b, am, ap = self.b, self.am, self.ap
        pl, ql, pr, qr = l.numerator, l.denominator, r.numerator, r.denominator
        Mm, Mp = Fr(am, b - 1), Fr(ap, b - 1)
        zone = self.wm1 * self.Dz / self.bt      # a zone's width in Dz units
        # the straddling boxes (ZL < 0 < ZH): lo = r ZL, hi = r ZH
        if self.neg1 < self.pos0:
            if self._dead(pr, qr, pr, qr, self.ZL[self.neg1:self.pos0], self.ZH[self.neg1:self.pos0]):
                return False
        # the positive side: width ((r - l)(b - 1) zq + r a+ + l a-)/Dz, rising in zq
        if self.pos0 < len(self.ZL):
            c0 = r * ap + l * am
            if r == l:
                i0 = self.pos0 if c0 > zone else len(self.ZL)
            else:
                thr = (zone - c0) / ((r - l) * (b - 1))
                zmin = math.floor(thr) + 1
                i0 = max(self.pos0, zmin - self.zq0)
            if i0 < len(self.ZL):
                if self._dead(pl, ql, pr, qr, self.ZL[i0:], self.ZH[i0:]):
                    return False
        # the negative side: width ((r - l)(b - 1)(-zq) + l a+ + r a-)/Dz, rising in -zq
        if self.neg1 > 0:
            c0 = l * ap + r * am
            if r == l:
                i1 = self.neg1 if c0 > zone else 0
            else:
                thr = (zone - c0) / ((r - l) * (b - 1))
                zmax = -(math.floor(thr) + 1)
                i1 = min(self.neg1, zmax - self.zq0 + 1)
            if i1 > 0:
                if self._dead(pr, qr, pl, ql, self.ZL[:i1], self.ZH[:i1]):
                    return False
        return True


# --------------------------------------------------------------- the walk

def walk(b, am, ap, L, R, n_h, safe):
    """Is there an assignment of the images (L, R) to level-n_h hulls,
    every extent inside its box and safe?  A forward pass over the
    hulls carrying the set of reachable first-uncovered indices; each
    used hull starts at the leftmost uncovered image and reaches to the
    largest safe right end (the exchange argument).  Returns (found,
    hull count, probes)."""
    Mm, Mp = Fr(am, b - 1), Fr(ap, b - 1)
    s = Fr(1, b ** n_h)
    lo_u, hi_u = prefix_range(b, am, ap, n_h)
    q_lo = max(lo_u, math.floor(L[0] / s - Mp) - 1)
    q_hi = min(hi_u, math.ceil(R[-1] / s + Mm) + 1)
    N = len(L)
    probes = 0
    reach = {0}
    for q in range(q_lo, q_hi + 1):
        bl, br = (q - Mm) * s, (q + Mp) * s
        nxt = set()
        for i0 in reach:
            l_min = L[i0]
            if l_min < bl:
                continue                    # never coverable again
            if l_min <= br:
                hi_i = bisect.bisect_right(R, br) - 1
                a, c, best = i0, hi_i, None
                while a <= c:
                    mid = (a + c) // 2
                    probes += 1
                    if safe(l_min, R[mid]):
                        best, a = mid, mid + 1
                    else:
                        c = mid - 1
                if best is not None:
                    if best + 1 == N:
                        return True, q_hi - q_lo + 1, probes
                    nxt.add(best + 1)
            if l_min >= bl + s:             # the skip: still coverable later
                nxt.add(i0)
        reach = nxt
        if not reach:
            break
    return False, q_hi - q_lo + 1, probes


def certify_walk(b, am, ap, P, o1, d, c2, nmax, eager, budget, verbose=True):
    """The pole's-lead consumer at lookahead c2, eager or aligned:
    ('dead', n), ('open', n) or ('capped', n), plus the per-level
    table [(n, hulls, wall)]."""
    Mm, Mp, w, Mh = window(b, am, ap)
    table = []
    for n in range(0, nmax + 1):
        n_h, n_z = n + d, (n if eager else n + d)
        t = n_z - c2
        if t < 1:
            continue
        L, R = recip_ends(b, am, ap, P, o1, n)
        zl, zh = prefix_range(b, am, ap, n_z)
        hl, hh = prefix_range(b, am, ap, n_h)
        sc = Fr(1, b ** n_h)
        q_lo = max(hl, math.floor(L[0] / sc - Mp) - 1)
        q_hi = min(hh, math.ceil(R[-1] / sc + Mm) + 1)
        est = (q_hi - q_lo + 1) * (zh - zl + 1) * (len(L).bit_length() + 1)
        if est > budget:
            return ('capped', n), table
        t0 = time.time()
        max_num = max(max(x.numerator for x in L), max(x.numerator for x in R))
        max_den = max(max(x.denominator for x in L), max(x.denominator for x in R))
        safe = ZoneSafe(b, am, ap, n_z, t, max_num, max_den)
        found, hulls, probes = walk(b, am, ap, L, R, n_h, safe)
        table.append((n, hulls, time.time() - t0))
        if verbose:
            print(f"      level {n}: {len(L)} images, {hulls} hulls, {zh - zl + 1} z boxes, "
                  f"{probes} probes{' (object ints)' if safe.big else ''}, "
                  f"{'assignment' if found else 'NO ASSIGNMENT'}, wall {time.time() - t0:.1f}s", flush=True)
        if not found:
            return ('dead', n), table
    return ('open', nmax), table


def gap_of(b, am, ap, Rm, d, c2, eager):
    Mm, Mp, w, Mh = window(b, am, ap)
    lam = Rm + (Mh / Fr(b) ** d if eager else Mh)
    return (lam * w - Fr(b) ** c2 * (w - 1)) / Mh


def slack_level(table, gap, w):
    """The least level in the table whose slack 2 (w - 1)/m is at or
    under the gap, or None."""
    for (n, m, _) in table:
        if 2 * (w - 1) / m <= gap:
            return n
    return None


def fmt(r):
    return f"{r[0]}@{r[1]}"


# ------------------------------------------------------------------ main

def main():
    nmax = int(sys.argv[1]) if len(sys.argv) > 1 else 9
    budget = float(sys.argv[2]) if len(sys.argv) > 2 else 1e11
    t0 = time.time()
    rng = random.Random(1248)

    print("=== P1, the control: the walk against the record at the 24 pairs of radices 2..4, "
          "and the safe tests against each other")
    results = {}
    for (b, am, ap, P) in pole_pairs(4):
        Mm, Mp, w, Mh = window(b, am, ap)
        o1, L1s, c1, Rmin, Rm = recip_params(b, am, ap, P)
        d = -c1
        rec_a, rec_e = RECORDED[(b, am, ap, str(P))]
        c2s = least_L(b, w, (Rm + Mh) * w)
        c2e = least_L(b, w, (Rm + Mh / Fr(b) ** d) * w)
        for (name, c2, eager, rec) in (('eager', c2e - 1, True, rec_e), ('aligned', c2s - 1, False, rec_a)):
            # the safe tests against each other
            n_chk = min(rec[1], 3)
            if rec[0] == 'capped':
                n_chk = min(rec[1] - 1, 3)
            n_z = n_chk if eager else n_chk + d
            t = n_z - c2
            if t >= 1:
                L, R = recip_ends(b, am, ap, P, o1, n_chk)
                max_num = max(max(x.numerator for x in L), max(x.numerator for x in R))
                max_den = max(max(x.denominator for x in L), max(x.denominator for x in R))
                new = ZoneSafe(b, am, ap, n_z, t, max_num, max_den)
                old = product_safe(b, am, ap, c2, 0, plain_boxes(b, am, ap, n_z), t)
                dis = 0
                for _ in range(200):
                    i = rng.randrange(len(L))
                    k = rng.randrange(i, len(L))
                    if new(L[i], R[k]) != old((L[i], R[k])):
                        dis += 1
                ok(dis == 0, f"K1 safe tests disagree at ({b},{am},{ap}) P={P} {name} level {n_chk}: {dis} of 200")
            gap = gap_of(b, am, ap, Rm, d, c2, eager)
            print(f"  ({b},{am},{ap}) P={P} {name} c2={c2} d={d} gap {gap} = {float(gap):.4f}, recorded {fmt(rec)}")
            r, table = certify_walk(b, am, ap, P, o1, d, c2, nmax, eager, budget)
            sl = slack_level(table, gap, w)
            results[(b, am, ap, P, name)] = (rec, r, table, gap, sl)
            if rec[0] == 'dead' and nmax >= rec[1]:
                ok(r == rec, f"K1 ({b},{am},{ap}) P={P} {name}: recorded {rec}, walk {r}")
            print(f"    -> walk {fmt(r)} | recorded {fmt(rec)} | slack level {sl}"
                  f"{'' if rec[0] == 'dead' else '   (' + ('GAIN' if r[0] == 'dead' else 'K2 OPEN') + ')'}", flush=True)

    print("\n=== THE TABLE: pair | eager: recorded, walk, slack level | aligned: recorded, walk, slack level")
    n_cert = n_new = n_open = 0
    off = []
    for (b, am, ap, P) in pole_pairs(4):
        cells = []
        for name in ('eager', 'aligned'):
            rec, r, table, gap, sl = results[(b, am, ap, P, name)]
            cells.append(f"{fmt(rec)} {fmt(r)} sl={sl}")
            if rec[0] == 'dead':
                n_cert += 1
            elif r[0] == 'dead':
                n_new += 1
            else:
                n_open += 1
            if r[0] == 'dead':
                if sl is None or abs(sl - r[1]) > 1:
                    off.append((b, am, ap, P, name, r[1], sl))
        print(f"  ({b},{am},{ap}) P={P} | {cells[0]} | {cells[1]}")
    print(f"  {n_cert} recorded deaths reproduced, {n_new} newly certified, {n_open} still open")
    print(f"  P4: death level off the slack level by more than one at {len(off)} pairs: {off}")
    ok(len(off) < 3, f"K3: the slack level misses the death level by more than one at {len(off)} pairs")

    print("\n=== P5, the priced-certificate line at its own kill: the product chain's 18 certified deaths "
          "(explore_chain_certify.py F1), death level against the least level with 2 (w - 1)/m <= E2 - S")
    from explore_chain_certify import OLD, ImageQueries
    from explore_chain_delay import slack_budget
    from explore_chain_product import escape_cost_product
    deaths = {k: v[1] for k, v in OLD.items() if v[0] == 'dead'}
    deaths[(3, 2, 2, 2, 1)] = 5
    deaths[(4, 2, 3, 2, 1)] = 5
    off5 = []
    for (b, am, ap, L1, L2), nd in sorted(deaths.items()):
        Mm, Mp, w, Mh = window(b, am, ap)
        gap = escape_cost_product(b, am, ap, L2) - slack_budget(b, am, ap, L1)
        row, sl = [], None
        for n in range(max(1, L2 + 1), nd + 3):
            m_ = n + L1
            Q = ImageQueries(b, am, ap, m_)
            unit = (b - 1) * b ** (2 * m_ - n)
            ql, qh = prefix_range(b, am, ap, n)
            q_lo = max(ql, (Q.min_left // unit - ap) // (b - 1) - 2)
            q_hi = min(qh, (Q.max_right // unit + am) // (b - 1) + 2)
            m = q_hi - q_lo + 1
            row.append((n, m))
            if sl is None and 2 * (w - 1) / m <= gap:
                sl = n
        if sl is None or abs(sl - nd) > 1:
            off5.append((b, am, ap, L1, L2, nd, sl))
        print(f"  ({b},{am},{ap}) ({L1},{L2}) gap E2 - S = {gap} = {float(gap):.4f} | death {nd} | slack level {sl} | hulls {row}")
    print(f"  off by more than one at {len(off5)} of {len(deaths)}: {off5}")
    ok(len(off5) < 3, f"K4: the priced line's slack level misses the death level by more than one at {len(off5)} of 18")

    print(f"\nwall {time.time() - t0:.1f}s; failures: {len(FAILURES)}")
    for f in FAILURES:
        print("  ", f)


if __name__ == "__main__":
    main()
