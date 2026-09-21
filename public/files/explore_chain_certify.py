"""The streaming covering certifier: does the golden band's first
cell past radix 4, (9,4,5) at (2, 1), carry an assignment of the
product's images to the multiplier's hulls at every level reached, as
the escape law promises, or a covering certificate that no rule can
serve?

THE QUESTION. explore_chain_product.py prices the aligned chain
(x y) z by the escape law and certifies the law's deaths by a covering
search: at output level n the product images of every (x, y) prefix
pair of length n + L1 must be assigned to level-n hulls of the P
stream, each hull's tight extent inside its box and SAFE against every
z box at level n, safe meaning the extent times the z box strictly
contains no overlap zone at output level n - L2. That search
enumerates every prefix pair, 54 million at its first level at
(9,4,5) (2, 1), against a cap of one million, so the golden band
past radix 4 (explore_chain_cells.py F3) rests on the law's word. This
rig rebuilds the certifier so that the level is streamed and the
search never holds the pair set.

THE REDUCTION, derived before the engine, in three steps. First, an
image contained in another image is never a constraint: whatever hull
extent covers the container covers it, so the images that matter are
the MAXIMAL ones under inclusion, an antichain sorted by left end with
the right ends strictly rising. Second, the search's rule -- each used
hull starts at the leftmost uncovered image and reaches to the
largest safe right end within its box -- leaves as uncovered exactly
the images whose right end exceeds the reach, so after every take the
remaining set is "every image with right end above the reach" and the
state is the pair (hull, last reach); over the full image set the
same search visits the same states, since a non-maximal image's left
end is never the least among the remaining and a reach that ends at a
non-maximal right end leaves the same maximal images remaining as the
largest maximal right end below it. Third, the safe test is monotone
in the reach (a wider extent has the larger product), so the take is a
bisection of the reach over the integers of the box, and the images
enter only through TWO QUERIES: the largest right end at or below a
value, and the least left end among the images whose right end lies
above it. For a first prefix u >= 1 both ends of the image rise with
the second prefix v (the box ends are (b - 1) u -+ a, nonnegative from
u = 1 on), for u <= -1 both fall, so each query is one bisection over
v vectorised across the first prefixes -- bracketed by a float
estimate of the dominant corner, verified exactly and widened to the
whole range where the estimate fails -- and the row u = 0, whose box
straddles zero, is held explicitly; no image set is ever stored. All
of it runs in scaled integers: an image's ends are products of the
box ends over (b - 1)^2 b^(2m), and the safe test's corner products
over (b - 1)^3 b^(2m + n) fit a machine word through level 4 at radix
9 (an assertion guards the bound). The antichain of the first step is
kept as the control's form of the search, built by streaming the
prefix pairs in blocks and merging each block's maximal set into the
running one; it is 834 thousand entries at level 2 of (9,4,5) and
concentrates near zero, where images are narrow, so it is not the
certifier's form. A sign
symmetry of the image set does not hold at an asymmetric digit set
(negating a box of u is not the box of -u when a^- differs from a^+),
so the cut is the reduction's and not a symmetry's.

CONVENTIONS, as in explore_chain_product.py: digit set {-a^-..a^+},
M-+ = a-+/(b - 1), w = M- + M+, Mh = max(M-, M+); L1 the multiplier's
lookahead, L2 the consumer's; a covering level n has output level
n - L2 >= 1; the certifier returns ('dead', n) at the first level with
no assignment, ('open', nmax) when every level to nmax has one.

PREDICTIONS, fixed before the run.
 P1 (the control, the reduction): at every pair below the naive sum
    at the representable cells of radices 2..4 -- 19 pairs -- the
    streaming certifier at levels to 5 returns the old certifier's
    verdict at the 16 pairs it certified, ('dead', n) at the same n,
    and finds an assignment at every level the old one reached at the
    three it capped: (3,2,2) (2, 1) to level 3, (4,2,2) (2, 1) and
    (4,2,3) (2, 1) to level 2. Beside it the reduction read directly:
    at the levels the old search reaches, the old covering_exists over
    the full image set, the antichain search and the query search
    over the same hulls and the same safe test return the same
    boolean, and the two queries agree with the full image set at
    every maximal right end and at 400 values drawn across the range.
 P2 (the question): (9,4,5) (2, 1), the law's alive pair with E2 = 9/320
    against S = 31/288, finds an assignment at level 2 and at level 3.
    The law's finite-level slack is 2 (w - 1)/m over a run of m hulls,
    so a law-alive pair is expected open at every finite level.
 P3 (a transplant from radix 4, where every (L1, 0) pair died at
    level 1): the law-dead pairs of the same cell, (2, 0) and (3, 0),
    are certified dead at level 1 or 2; the mirror cell (9,5,4) at
    (2, 1) is open to level 3 as (9,4,5) is; the nearest slack-2 miss
    at radix 9, (9,2,8) at (2, 1), law-dead by 20/648 of a cell, is
    certified dead by level 3 or printed OPEN as an upper bound.

KILLS, as prints.
 K1: P1 prints a verdict off the old certifier's, or the two searches
     disagree at a level -> the reduction is wrong; nothing below is
     read.
 K2: (9,4,5) (2, 1) prints ('dead', n) -> the escape law calls alive a
     pair no multiplier rule can serve, the corner-binding derivation
     fails at this cell, and the classification line dies at its named
     kill.
 K3: a law-dead pair prints open to the deepest level -> not a kill;
     that pair's floor is an upper bound, printed OPEN.

POSITIVE CONTROL: P1, read before any radix-9 line.

FINDINGS (entered after the run; every number below is in this
file's print at NMAX = 4 with --deep).

F1 THE CONTROL HOLDS. All 19 pairs: the old certifier's ('dead', n)
   reproduced at the same n at its 16 certified pairs, assignments
   at every level the old one reached at its three capped pairs, and
   at 15 levels of eight pairs the old search over the full image set,
   the antichain search and the query search return the same boolean
   while the queries agree with the full image set at every maximal
   right end and at 400 drawn values. K1 never
   fired. The streaming certifier closes the two pairs the old one
   left open at its cap: (3,2,2) (2, 1) and (4,2,3) (2, 1) are
   certified dead at level 5, so every law-dead pair of radices 2..4
   is certified; (4,2,2) (2, 1) stays open to level 5.
F2 P2 HELD: THE WINDOW'S FIRST CELL PAST RADIX 4 IS SUPPORTED. (9,4,5)
   (2, 1) finds an assignment at levels 2, 3 and 4 (63, 519 and 4619
   hulls; 7381, 66430 and 597871 prefixes), and its mirror (9,5,4)
   at levels 2 and 3. K2 never fired.
F3 P3 HELD IN PART. The cell's law-dead pairs (2, 0) and (3, 0) are
   certified dead at level 1, as at radix 4. The nearest slack-2
   miss (9,2,8) (2, 1), law-dead by 5/162, finds assignments at
   levels 2 and 3 (K3: OPEN, its floor an upper bound), the first
   law-dead pair at any cell the certifier reaches three levels
   deep without a certificate; the gap 5/162 = 0.031 of a cell is
   the smallest among the pairs searched, under the 4/9 and 5/24 the
   old search left open; the law's finite-level slack 2 (w - 1)/m
   over a run of m hulls, with w - 1 = 1/4 at that cell, equals the
   gap at m = 16, and the region where the consumer's need exceeds
   the budget -- |P| within (E2 - S) Mh/w = 2/81 of the corner --
   spans about 14 hulls at level 3 (a hull is w/9^3 wide in P), so
   the depth reached cannot yet separate the law's death from the
   slack; at level 4 the region spans about 130.
F4 THE WINDOW'S NEXT CELL, (12,5,7) (2, 1), with E2 = 60/847 against
   S = 59/726, finds an assignment at level 2 (106 hulls, 22621
   prefixes).

VERDICT. The golden band is no longer the law's word only: at its
first cell past radix 4 the covering search finds an assignment at
every level to 4, the deepest the certifier has reached at any cell,
and at the next cell at level 2, while the same cell's law-dead pairs
die at level 1. The classification line survives its named kill. What
the certifier cannot yet say is a death at the nearest slack-2 miss,
where the law's gap is a thirtieth of a cell and the finite-level
slack outruns the depth reached.

RUN RECORD: pure Python and numpy, exact integers in machine words;
under memwatch, peak commit 80.0 MB, wall 96 s at NMAX = 3; at
NMAX = 4 with --deep, peak commit 179.4 MB, each level-4 search
between 800 and 1830 s across three runs (a query pair costs a
quarter second over the 597871 prefixes, times 4619 hulls), the whole
run about 55 minutes and run in two halves under memwatch's 3000 s
timeout. Level 4 stays opt-in.
Run: python prime/code/explore_chain_certify.py [NMAX] [--deep]
"""

import os
import sys
import time
os.environ["OPENBLAS_NUM_THREADS"] = "1"
import numpy as np   # noqa: E402

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from explore_chain_delay import (window, margin_L, slack_budget,   # noqa: E402
                                 census, representable_xy)
from explore_chain_product import (least_L, escape_cost_product,   # noqa: E402
                                   prefix_range, plain_boxes, product_images,
                                   product_safe, covering_exists)

FAILURES = []
BLOCK_PAIRS = 400_000  # prefix pairs per streamed block of the control's antichain
MERGE_AT = 1_000_000   # pending antichain entries before a merge


def ok(cond, msg):
    if not cond:
        FAILURES.append(msg)
        print(f"  FAIL: {msg}")


# --------------------------------------------------------- the antichain

def maximal(L, R):
    """The maximal intervals of (L, R) under inclusion, sorted by left
    end, right ends strictly rising."""
    order = np.lexsort((-R, L))
    L, R = L[order], R[order]
    if len(R) == 0:
        return L, R
    cm = np.maximum.accumulate(R)
    keep = np.ones(len(R), dtype=bool)
    keep[1:] = R[1:] > cm[:-1]
    return L[keep], R[keep]


def product_antichain(b, am, ap, m):
    """The maximal product images of all (x, y) prefix pairs of length
    m, ends in units of 1/((b - 1)^2 b^(2m)); streamed by blocks of
    the first prefix.  Returns (L, R, pairs seen)."""
    Rr = (b ** m - 1) // (b - 1)
    us = np.arange(-am * Rr, ap * Rr + 1, dtype=np.int64)
    lo = (b - 1) * us - am
    hi = (b - 1) * us + ap
    n = len(us)
    AL, AR = np.empty(0, np.int64), np.empty(0, np.int64)
    pend_L, pend_R, pending = [], [], 0
    total = 0
    idx = np.arange(n)
    block = max(1, BLOCK_PAIRS // n)
    for i0 in range(0, n, block):
        i1 = min(n, i0 + block)
        ii = np.repeat(np.arange(i0, i1), n)
        jj = np.tile(idx, i1 - i0)
        mask = jj >= ii
        ii, jj = ii[mask], jj[mask]
        li, hj, lj, hi_ = lo[ii], hi[jj], lo[jj], hi[ii]
        c1 = li * lj
        Lc = np.minimum(c1, li * hj)
        Rc = np.maximum(c1, li * hj)
        c1 = hi_ * lj
        Lc = np.minimum(Lc, c1)
        Rc = np.maximum(Rc, c1)
        c1 = hi_ * hj
        Lc = np.minimum(Lc, c1)
        Rc = np.maximum(Rc, c1)
        del ii, jj, li, hj, lj, hi_, c1
        total += len(Lc)
        Lc, Rc = maximal(Lc, Rc)
        pend_L.append(Lc)
        pend_R.append(Rc)
        pending += len(Lc)
        if pending >= MERGE_AT:
            AL, AR = maximal(np.concatenate([AL] + pend_L), np.concatenate([AR] + pend_R))
            pend_L, pend_R, pending = [], [], 0
    if pend_L:
        AL, AR = maximal(np.concatenate([AL] + pend_L), np.concatenate([AR] + pend_R))
    return AL, AR, total


# ---------------------------------------------------------- the search

def box_ends(b, am, ap, us):
    return (b - 1) * us - am, (b - 1) * us + ap


def make_safe(b, am, ap, m, n, L2):
    """safe(l, r) for an extent in the level's units: no z box at level
    n makes extent x zbox strictly contain a zone at output level
    n - L2; the corner products in units of 1/((b - 1)^3 b^(2m + n)),
    the zone test in the same units."""
    zl, zh = prefix_range(b, am, ap, n)
    zs = np.arange(zl, zh + 1, dtype=np.int64)
    Zlo, Zhi = box_ends(b, am, ap, zs)
    t = n - L2
    D1 = (b - 1) ** 2 * b ** (2 * m + n - t)          # one cell, in corner units
    D = D1 * (b - 1)
    lo_u, hi_u = prefix_range(b, am, ap, m)
    big = max(abs((b - 1) * lo_u - am), (b - 1) * hi_u + ap) ** 2 * max(abs(int(Zlo[0])), int(Zhi[-1]))
    assert big < 2 ** 62 and D * (b + am + ap) < 2 ** 62, "corner products overflow a machine word"
    shift = (am - (b - 1)) * D1

    def safe(l, r):
        c1, c2, c3, c4 = l * Zlo, l * Zhi, r * Zlo, r * Zhi
        LO = np.minimum(np.minimum(c1, c2), np.minimum(c3, c4))
        HI = np.maximum(np.maximum(c1, c2), np.maximum(c3, c4))
        q = np.floor_divide(LO + shift, D) + 1
        return not bool(np.any(q * D + ap * D1 < HI))
    return safe


class ImageQueries:
    """The two queries the covering search needs over the product
    images of every (x, y) prefix pair of length m, answered without
    the image set: for a first prefix u >= 1 both ends of the image
    rise with the second prefix v, for u <= -1 both fall, so the
    largest right end at or below Y and the least left end among the
    images beyond Y are one bisection over v, vectorised over u; the
    row u = 0, where the ends are not monotone, is held explicitly."""

    def __init__(self, b, am, ap, m):
        self.b, self.am, self.ap = b, am, ap
        lo_u, hi_u = prefix_range(b, am, ap, m)
        self.lo_u, self.hi_u = lo_u, hi_u
        us = np.arange(lo_u, hi_u + 1, dtype=np.int64)
        self.up = us[us >= 1]
        self.un = us[us <= -1]
        self.Lp, self.Hp = box_ends(b, am, ap, self.up)
        self.Ln, self.Hn = box_ends(b, am, ap, self.un)
        Lv, Hv = box_ends(b, am, ap, us)
        c = np.stack([-am * Lv, -am * Hv, ap * Lv, ap * Hv])
        L0, R0 = c.min(axis=0), c.max(axis=0)
        order = np.argsort(R0, kind='stable')
        self.R0 = R0[order]
        L0 = L0[order]
        self.L0suf = np.minimum.accumulate(L0[::-1])[::-1]     # min left over the suffix in right order
        L1, H1 = (b - 1) * lo_u - am, (b - 1) * hi_u + ap
        self.min_left = min(L1 * L1, L1 * H1, H1 * H1)
        self.max_right = max(L1 * L1, H1 * H1)

    def ends(self, Lu, Hu, v):
        Lv, Hv = box_ends(self.b, self.am, self.ap, v)
        c1, c2, c3, c4 = Lu * Lv, Lu * Hv, Hu * Lv, Hu * Hv
        return (np.minimum(np.minimum(c1, c2), np.minimum(c3, c4)),
                np.maximum(np.maximum(c1, c2), np.maximum(c3, c4)))

    def bracket(self, Lu, Hu, Y, increasing):
        """A bracket [lo, hi] around the split from float estimates of
        the dominant corner, verified exactly and widened to the whole
        range where the estimate fails, so the bisection stays exact."""
        lo_s, hi_s = self.lo_u - 1, self.hi_u + 1
        with np.errstate(divide='ignore', invalid='ignore'):
            if increasing:
                e1 = (Y / Hu - self.ap) / (self.b - 1)
                e2 = np.where(Lu != 0, (Y / np.where(Lu != 0, Lu, 1) - self.ap) / (self.b - 1), e1)
            else:
                e1 = (Y / Hu + self.am) / (self.b - 1)
                e2 = (Y / Lu + self.am) / (self.b - 1)
        fin = np.isfinite(e1) & np.isfinite(e2)
        e1 = np.where(fin, e1, 0.0)
        e2 = np.where(fin, e2, 0.0)
        lo = np.where(fin, np.clip(np.floor(np.minimum(e1, e2)) - 3, lo_s, hi_s), lo_s).astype(np.int64)
        hi = np.where(fin, np.clip(np.ceil(np.maximum(e1, e2)) + 3, lo_s, hi_s), hi_s).astype(np.int64)
        f_lo = self.ends(Lu, Hu, np.clip(lo, self.lo_u, self.hi_u))[1]
        f_hi = self.ends(Lu, Hu, np.clip(hi, self.lo_u, self.hi_u))[1]
        if increasing:
            good = ((lo == lo_s) | (f_lo <= Y)) & ((hi == hi_s) | (f_hi > Y))
        else:
            good = ((lo == lo_s) | (f_lo > Y)) & ((hi == hi_s) | (f_hi <= Y))
        # a bracket beyond the range on either side is pulled back to its
        # last in-range end, so the split is always read at a real prefix
        lo = np.minimum(lo, self.hi_u)
        hi = np.maximum(hi, self.lo_u)
        good &= lo < hi
        lo = np.where(good, lo, lo_s)
        hi = np.where(good, hi, hi_s)
        return lo, hi

    def split_pos(self, Y):
        """For u >= 1: the largest v with right(u, v) <= Y, lo_u - 1 if none."""
        lo, hi = self.bracket(self.Lp, self.Hp, Y, True)
        while True:
            act = hi - lo > 1
            if not act.any():
                return lo
            mid = (lo + hi) // 2
            r = self.ends(self.Lp, self.Hp, mid)[1]
            le = r <= Y
            lo = np.where(act & le, mid, lo)
            hi = np.where(act & ~le, mid, hi)
            assert lo.max() <= self.hi_u, "split_pos out of range"

    def split_neg(self, Y):
        """For u <= -1: the smallest v with right(u, v) <= Y, hi_u + 1 if none."""
        lo, hi = self.bracket(self.Ln, self.Hn, Y, False)
        while True:
            act = hi - lo > 1
            if not act.any():
                return hi
            mid = (lo + hi) // 2
            r = self.ends(self.Ln, self.Hn, mid)[1]
            le = r <= Y
            hi = np.where(act & le, mid, hi)
            lo = np.where(act & ~le, mid, lo)
            assert hi.min() >= self.lo_u, "split_neg out of range"

    def pred(self, Y):
        """The largest image right end <= Y, or None."""
        best = None
        vp = self.split_pos(Y)
        ok_ = vp >= self.lo_u
        if ok_.any():
            best = int(self.ends(self.Lp[ok_], self.Hp[ok_], vp[ok_])[1].max())
        vn = self.split_neg(Y)
        ok_ = vn <= self.hi_u
        if ok_.any():
            r = int(self.ends(self.Ln[ok_], self.Hn[ok_], vn[ok_])[1].max())
            best = r if best is None else max(best, r)
        i = int(np.searchsorted(self.R0, Y, side='right')) - 1
        if i >= 0:
            r = int(self.R0[i])
            best = r if best is None else max(best, r)
        return best

    def succ_left(self, Y):
        """The least left end among the images with right end > Y, or None."""
        best = None
        vp = self.split_pos(Y) + 1
        ok_ = vp <= self.hi_u
        if ok_.any():
            best = int(self.ends(self.Lp[ok_], self.Hp[ok_], vp[ok_])[0].min())
        vn = self.split_neg(Y) - 1
        ok_ = vn >= self.lo_u
        if ok_.any():
            l = int(self.ends(self.Ln[ok_], self.Hn[ok_], vn[ok_])[0].min())
            best = l if best is None else min(best, l)
        i = int(np.searchsorted(self.R0, Y, side='right'))
        if i < len(self.R0):
            l = int(self.L0suf[i])
            best = l if best is None else min(best, l)
        return best


def query_covering(b, am, ap, m, n, safe):
    """Is there an assignment of the level's images to level-n hulls,
    every extent inside its box and safe?  The state is (hull index,
    the last reach); the images are consulted through ImageQueries
    only.  Returns (found, hull count)."""
    Q = ImageQueries(b, am, ap, m)
    unit = (b - 1) * b ** (2 * m - n)
    ql, qh = prefix_range(b, am, ap, n)
    q_lo = max(ql, (Q.min_left // unit - ap) // (b - 1) - 2)
    q_hi = min(qh, (Q.max_right // unit + am) // (b - 1) + 2)
    qs = list(range(q_lo, q_hi + 1))
    memo = {}
    sys.setrecursionlimit(max(10000, len(qs) + 100))

    def bl(q):
        return ((b - 1) * q - am) * unit

    def br(q):
        return ((b - 1) * q + ap) * unit

    def rec(idx, tau):
        if tau >= Q.max_right:
            return True
        if idx == len(qs):
            return False
        key = (idx, tau)
        if key in memo:
            return memo[key]
        q = qs[idx]
        l_min = Q.succ_left(tau)
        res = False
        if l_min >= bl(q):
            if l_min <= br(q):
                # the largest reach r in [l_min, br] with safe(l_min, r); safe is monotone in r
                if safe(l_min, l_min):
                    a, c = l_min, br(q)
                    while a < c:
                        mid = (a + c + 1) // 2
                        if safe(l_min, mid):
                            a = mid
                        else:
                            c = mid - 1
                    best = Q.pred(a)
                    if best is not None and best > tau and rec(idx + 1, best):
                        res = True
            if not res and idx + 1 < len(qs) and l_min >= bl(q + 1):
                res = rec(idx + 1, tau)
        memo[key] = res
        return res

    return rec(0, Q.min_left - 1), len(qs)


def antichain_covering(b, am, ap, AL, AR, m, n, safe):
    """The same search over the maximal images (AL, AR) held whole,
    for the control: the state is (hull index, suffix start)."""
    N = len(AL)
    unit = (b - 1) * b ** (2 * m - n)
    lo_u, hi_u = prefix_range(b, am, ap, n)
    q_lo = max(lo_u, (int(AL[0]) // unit - ap) // (b - 1) - 2)
    q_hi = min(hi_u, (int(AR[-1]) // unit + am) // (b - 1) + 2)
    qs = list(range(q_lo, q_hi + 1))
    memo = {}
    sys.setrecursionlimit(max(10000, len(qs) + 100))

    def rec(idx, i0):
        if i0 == N:
            return True
        if idx == len(qs):
            return False
        key = (idx, i0)
        if key in memo:
            return memo[key]
        q = qs[idx]
        bl, br = ((b - 1) * q - am) * unit, ((b - 1) * q + ap) * unit
        l_min = int(AL[i0])
        res = False
        if l_min >= bl:
            if l_min <= br:
                hi_i = int(np.searchsorted(AR, br, side='right')) - 1
                best = None
                a, c = i0, hi_i
                while a <= c:
                    mid = (a + c) // 2
                    if safe(l_min, int(AR[mid])):
                        best, a = mid, mid + 1
                    else:
                        c = mid - 1
                if best is not None and rec(idx + 1, best + 1):
                    res = True
            if not res and idx + 1 < len(qs) and l_min >= ((b - 1) * (q + 1) - am) * unit:
                res = rec(idx + 1, i0)
        memo[key] = res
        return res

    return rec(0, 0)


def certify_streaming(b, am, ap, L1, L2, nmax, verbose=True):
    """('dead', n) at the first level with no assignment, else
    ('open', nmax); prints the hulls and wall per level."""
    for n in range(max(1, L2 + 1), nmax + 1):
        m = n + L1
        t0 = time.time()
        safe = make_safe(b, am, ap, m, n, L2)
        found, hulls = query_covering(b, am, ap, m, n, safe)
        if verbose:
            lo_u, hi_u = prefix_range(b, am, ap, m)
            print(f"    level {n}: {hi_u - lo_u + 1} prefixes, {hulls} hulls, "
                  f"{'assignment' if found else 'NO ASSIGNMENT'}, wall {time.time() - t0:.1f}s", flush=True)
        if not found:
            return ('dead', n)
    return ('open', nmax)


# ------------------------------------------------------------------ main

def fmt(r):
    return f"{r[0]}@{r[1]}"


OLD = {  # explore_chain_product.py's verdicts at nmax 5, its caps
    (2, 1, 1, 2, 0): ('dead', 2), (2, 1, 1, 2, 1): ('dead', 3), (2, 1, 1, 3, 0): ('dead', 2),
    (3, 1, 2, 2, 0): ('dead', 1), (3, 1, 2, 2, 1): ('dead', 2), (3, 1, 2, 3, 0): ('dead', 1),
    (3, 2, 2, 2, 0): ('dead', 1), (3, 2, 2, 2, 1): ('capped', 4), (3, 2, 2, 3, 0): ('dead', 1),
    (4, 1, 3, 2, 0): ('dead', 1), (4, 1, 3, 2, 1): ('dead', 2), (4, 1, 3, 3, 0): ('dead', 1),
    (4, 2, 2, 2, 0): ('dead', 1), (4, 2, 2, 2, 1): ('capped', 3), (4, 2, 2, 3, 0): ('dead', 1),
    (4, 2, 3, 2, 0): ('dead', 1), (4, 2, 3, 2, 1): ('capped', 3), (4, 2, 3, 3, 0): ('dead', 1),
    (4, 3, 3, 1, 0): ('dead', 1),
}


def main():
    nmax = int(sys.argv[1]) if len(sys.argv) > 1 and not sys.argv[1].startswith('-') else 3
    deep = '--deep' in sys.argv
    t0 = time.time()

    print("=== P1, the control: the streaming certifier against the old one, radices 2..4, levels to 5")
    for (b, am, ap) in census(4):
        if not representable_xy(b, am, ap):
            continue
        Mm, Mp, w, Mh = window(b, am, ap)
        L1s, L2s = margin_L(b, am, ap, 2 * Mh), least_L(b, w, (Mh + Mh * Mh) * w)
        for L1 in range(L1s, L1s + L2s):
            for L2 in range(0, L1s + L2s - L1):
                old = OLD[(b, am, ap, L1, L2)]
                E, S = escape_cost_product(b, am, ap, L2), slack_budget(b, am, ap, L1)
                r = certify_streaming(b, am, ap, L1, L2, 5, verbose=False)
                if old[0] == 'dead':
                    agree = r == old
                else:
                    agree = r[0] == 'open' or r[1] >= old[1]
                ok(agree, f"K1 ({b},{am},{ap}) ({L1},{L2}): old {old}, streaming {r}")
                print(f"  ({b},{am},{ap}) ({L1},{L2}) law {'alive' if E <= S else 'dead'} | old {fmt(old)} | streaming {fmt(r)}")

    print("\n=== P1, the reduction read directly: the old search over the full image set against the antichain search")
    same = tot = 0
    for (b, am, ap, L1, L2, nn) in [(2, 1, 1, 2, 1, 4), (3, 1, 2, 2, 1, 3), (3, 2, 2, 2, 1, 3),
                                    (4, 1, 3, 2, 1, 2), (4, 2, 2, 2, 1, 2), (4, 2, 3, 2, 1, 2),
                                    (4, 2, 2, 2, 0, 2), (4, 3, 3, 1, 0, 3)]:
        for n in range(max(1, L2 + 1), nn + 1):
            m = n + L1
            imgs = product_images(b, am, ap, m)
            old_safe = product_safe(b, am, ap, L2, 0, plain_boxes(b, am, ap, n), n - L2)
            a = covering_exists(b, am, ap, imgs, n, old_safe)
            AL, AR, total = product_antichain(b, am, ap, m)
            safe = make_safe(b, am, ap, m, n, L2)
            c = antichain_covering(b, am, ap, AL, AR, m, n, safe)
            d, hulls = query_covering(b, am, ap, m, n, safe)
            # the two queries against the full image set: at every maximal
            # right end, at 400 values drawn across the range, and at the ends
            Q = ImageQueries(b, am, ap, m)
            sc = (b - 1) ** 2 * b ** (2 * m)
            FL = np.array([int(l * sc) for (l, r) in imgs])
            FR = np.array([int(r * sc) for (l, r) in imgs])
            rng = np.random.default_rng(n)
            Ys = ([int(r) for r in AR] + [int(y) for y in rng.integers(Q.min_left, Q.max_right, 400)]
                  + [Q.min_left - 1, Q.max_right])
            qok = True
            for Y in Ys:
                below, above = FR <= Y, FR > Y
                tp = int(FR[below].max()) if below.any() else None
                ts = int(FL[above].min()) if above.any() else None
                qok &= Q.pred(Y) == tp and Q.succ_left(Y) == ts
            tot += 1
            same += (a == c == d) and qok
            ok(a == c == d, f"K1 the searches disagree at ({b},{am},{ap}) ({L1},{L2}) level {n}: full {a}, antichain {c}, queries {d}")
            ok(qok, f"K1 the queries differ from the image set at ({b},{am},{ap}) ({L1},{L2}) level {n}")
        print(f"  ({b},{am},{ap}) ({L1},{L2}) levels to {nn}: {len(imgs)} images, antichain {len(AL)}")
    print(f"  {tot} levels, the three searches agree and the queries match the image set at {same}")
    if FAILURES:
        print("POSITIVE CONTROL FAILED; nothing below is read")
        return

    print(f"\n=== P2, the question: (9,4,5) (2, 1), levels to {nmax}")
    b, am, ap = 9, 4, 5
    E, S = escape_cost_product(b, am, ap, 1), slack_budget(b, am, ap, 2)
    print(f"  law: E2 = {E}, S = {S}, {'alive' if E <= S else 'dead'}")
    r = certify_streaming(b, am, ap, 2, 1, nmax)
    print(f"  (9,4,5) (2,1): {fmt(r)}" + ("  K2: THE LAW'S ALIVE PAIR IS DEAD" if r[0] == 'dead' else "  assignments at every level reached"))

    print(f"\n=== P3, the neighbours: the law-dead pairs of (9,4,5), the mirror, the nearest slack-2 miss")
    for (b, am, ap, L1, L2, nn) in [(9, 4, 5, 2, 0, 3), (9, 4, 5, 3, 0, 2), (9, 5, 4, 2, 1, 3), (9, 2, 8, 2, 1, 3)]:
        E, S = escape_cost_product(b, am, ap, L2), slack_budget(b, am, ap, L1)
        verdict = 'alive' if E <= S else 'dead'
        print(f"  ({b},{am},{ap}) ({L1},{L2}) law {verdict}, E2 - S = {E - S}")
        r = certify_streaming(b, am, ap, L1, L2, nn)
        line = f"  ({b},{am},{ap}) ({L1},{L2}): {fmt(r)}"
        if verdict == 'dead' and r[0] != 'dead':
            line += "  K3: OPEN, an upper bound only"
        elif verdict == 'alive':
            ok(r[0] != 'dead', f"K2 covering certificate at a law-alive pair ({b},{am},{ap}) ({L1},{L2}): {r}")
        print(line)

    if deep:
        print("\n=== the window's next cell, (12,5,7) (2, 1), level 2")
        b, am, ap = 12, 5, 7
        E, S = escape_cost_product(b, am, ap, 1), slack_budget(b, am, ap, 2)
        print(f"  law: E2 = {E}, S = {S}, {'alive' if E <= S else 'dead'}")
        r = certify_streaming(b, am, ap, 2, 1, 2)
        ok(r[0] != 'dead', f"K2 covering certificate at (12,5,7) (2,1): {r}")
        print(f"  (12,5,7) (2,1): {fmt(r)}")

    print(f"\nwall {time.time() - t0:.1f}s; failures: {len(FAILURES)}")


if __name__ == "__main__":
    main()
