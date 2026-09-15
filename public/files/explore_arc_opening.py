"""Is the arc-opening depth in base beta a closed form -- the least
depth at which the corner box's average slope clears the margin law's
threshold -- computed box by box with no game tree?

THE QUESTION. Below the margin law's L* at a contiguous digit set in
base beta the confined tree's dead arc is empty at every round below
an ARC-OPENING DEPTH, and the kill comes 0 to 2 rounds after it
(explore_reachable_offsets.py). That rig read the opening off the
whole enumerated tree. The opening is a property of the boxes alone:
at round r the reader is at output depth t = r - 1, the adversary's
box at input depth n = max(0, r + c), the child cell's digit spacing
beta^(o - r), and a box's arc has positive length iff its exact image
width exceeds (w - 1) beta^(o - r), w = 2M the cell's width,
M = a/(beta - 1). The confined boxes at depth n are the prefixes the
rate bound admits, the same set whatever parent the reader holds; so
the opening depth is the least round at which any admitted box at
depth n(r) has an image wider than (w - 1) beta^(o - r), a scan over
the admitted boxes level by level with no reader, no parent and no
minimax. THE PROPERTY that ties the scan to the tree: the enumeration
of explore_reachable_offsets.py records every confined extension of
every live state, and a state is dead only at a positive arc, so
below the first positive arc every admitted box is present in the
enumeration and the two openings coincide by construction; the print
checks the two codes against each other, not the property.

THE PAPER DERIVATION, done before the engine. Let the box at depth n
have half-width h = M beta^(-n); the widest prefix box sits at the
window's corner, every digit a, its top at M and its bottom at
M - 2h. With c + o = L* - 1 the round's unit is beta^(L* - 1 - n) and
the law's threshold at L* - 1 is Lam_law = (w - 1) beta^(L* - 1) / w,
so the arc condition width > (w - 1) beta^(L* - 1 - n) reads
width > Lam_law w beta^(-n) = Lam_law (2h). The corner box's image:
  x y      : M^2 - (M - 2h)^2 = 2h (2M - 2h) = 2h (Lam - 2h),
             Lam = 2M = w;
  x^2 + y  : (M^2 - (M - 2h)^2) + 2h = 2h (2M + 1 - 2h) = 2h (Lam - 2h),
             Lam = 2M + 1 (the excess region is a strip in x, but the
             widest box in it is still the one with |x| at M);
  x/(s + y): s = M + 1, the corner at (M, -M) where s + y runs over
             [1, 1 + 2h]: M/1 - (M - 2h)/(1 + 2h) = 2h (M + 1)/(1 + 2h)
             = 2h Lam/(1 + 2h), Lam = 1 + M; the width
             2h (x1 + D1 + 2h)/(D1 (D1 + 2h)) increases in x1 and
             decreases in D1, so the corner is the widest box.
Dividing by 2h, the average slope over the corner box against the
threshold: the box opens an arc iff
  Lam - 2h > Lam_law            (x y, x^2 + y)      i.e. 2h < Lam - Lam_law,
  Lam/(1 + 2h) > Lam_law        (the divider)        i.e. 2h < (Lam - Lam_law)/Lam_law,
and with 2h = w beta^(-n) THE CLOSED FORM: the opening depth is the
least n with beta^(-n) < theta, theta = (Lam - Lam_law)/(w kappa),
kappa = 1 for the polynomial maps and kappa = Lam_law for the divider
(the pole's average slope drops by a share of itself, the polynomial's
by an absolute amount); n_open = floor(log_beta(1/theta)) + 1, and
the round is r_open = max(1, n_open - c). At L* the excess
Lam - Lam_law is at most 0 and no box ever opens: the law's
sufficiency in one line. Past the opening the corner arc grows to a
limit: for the polynomial maps g(n) = w beta^(1 - L*) (Lam - Lam_law
- w beta^(-n)) = g_inf (1 - beta^(-n)/theta), g_inf = w (Lam -
Lam_law)/beta^(L* - 1) the excess in child-cell units; for the
divider g(n) = w beta^(1 - L*) (Lam/(1 + w beta^(-n)) - Lam_law). The
arc at the opening is g_inf (1 - beta^(-phi)) with phi = n_open -
log_beta(1/theta) in (0, 1], THE OVERSHOOT: an opening at small phi
is barely open, its arc a small share of the excess.
  Hand check at the plastic x y, a = 1: M = beta^4 exactly (beta^5 -
beta^4 = 1), o = 4, L* = 8, c = 3, Lam = w = 6.15916, Lam_law =
5.99676, theta = 0.02637, log_beta(1/theta) = 12.94, n_open = 13,
r_open = 10; g(13) = 0.0027, g(14) = 0.037, g(15) = 0.062 -- the
record's opening at round 10 with g_max 0.0027, 0.0363, 0.0616 at
rounds 10, 11, 12 (explore_reachable_offsets.py F3).

THE SLATE, frozen before the engine. At every one of the 30 beta pairs
of explore_delay_choice.py at L* - 1 (the five Pisot bases, the three
maps, a = 1 and 2), the admitted boxes are walked level by level from
the root (explore_beta_delay.py BetaReader.in_region at every depth,
BetaReader.image for the exact width), the round's largest arc g_max
printed at every round to three past the opening or the budget, the
box attaining it located by its prefix (every digit a, or not), and
the scan's opening read against three columns: the closed form, the
enumeration's arc-opening column
(explore_reachable_offsets.py, its print handed in as a file), and the certificate's kill round from the same print.

P-A THE TWO CODES. The scan's opening round equals the enumeration's
    at all 21 pairs the enumeration read (the property above; a
    difference is a bug in one code).
P-B THE CLOSED FORM. r_open = max(1, n_open - c) at every pair the
    scan opens, n_open = floor(log_beta(1/theta)) + 1 with the two
    kappas, and the box attaining g_max at the opening is a corner box
    (every digit of every stream at +-a, the divider's y stream at
    -a). The printed g_max at the opening and the next two rounds
    matches g(n) to three figures.
P-C THE STRIP. x^2 + y, whose excess region is a strip and not a
    corner, obeys the same closed form (kappa = 1): the widest
    admitted box has |x| at M whatever y.
P-D THE FOUR UNREAD PAIRS. The scan reaches the opening at the four
    killed pairs the enumeration could not (the Narayana divider at
    a = 2, silver x^2 + y at a = 2, the plastic x^2 + y and divider
    at a = 1), and the certificate's round is 0 to 2 past it at each:
    the lag rule at 25 pairs.
P-E THE OVERSHOOT (TRANSPLANT from the enumeration's covering picture: the
    lag is the offsets' covering of an arc the grain sizes). The lag
    r_kill - r_open is larger where the overshoot phi is small: over
    the killed pairs the lag-2 pairs have phi below the lag-0 pairs'
    median. A lag independent of phi says the covering is not the
    arc's size but the offsets' arithmetic.

KILLS, frozen as what this rig PRINTS.

K1 THE CONTROL. The plastic x y at a = 1 opening at a round other
   than 10, or its g_max at rounds 10, 11, 12 outside 0.0027, 0.0363,
   0.0616 by more than 0.0005 -> nothing below is read.
K2 THE TWO CODES. The scan's opening differing from the enumeration's
   at any read pair -> one code is wrong; both re-read before any
   line below.
K3 THE CLOSED FORM. The scan's opening differing from
   max(1, n_open - c) at any pair the scan opens, with the attaining
   box a corner box -> the derivation is wrong; with the attaining
   box NOT a corner box -> the widest-box claim is wrong and the form
   needs that box's own average slope.
K4 THE LAG. The certificate's round more than 2 past the scan's
   opening at any of the four unread pairs -> the conjectured
   "plus at most two" dies.
THE READING: the table of (pair, L*, o, c, Lam, Lam_law, theta,
n_open, r_open formula, r_open scan, r_open enumeration, r_kill, lag,
phi, corner?) over the 30 pairs; the count of pairs at each lag; the
lag against phi.

POSITIVE CONTROL: K1, read before any other line.

FINDINGS (entered post-run; every number below sits in this file's
printed output, the enumeration column read from the print of
explore_reachable_offsets.py rerun the same sitting).

F1 THE CONTROL HOLDS. The plastic x y at a = 1 opens at round 10 with
   g_max 0.0027, 0.0363, 0.0616 at rounds 10, 11, 12, the formula's
   g(n) equal to each; K1 never fired.

F2 THE TWO CODES AGREE [property, checked]. The scan opens 26 of the
   30 pairs (the four unopened stop at the level cap or the wall short
   of the formula's round: Narayana x^2 + y at both a, plastic x^2 + y
   and the divider at a = 2) and its opening round equals the
   enumeration's at all 24 pairs the enumeration printed one at; K2
   never fired. The scan reads pairs the tree could not: the Narayana
   divider at a = 2 (opens at 5, 564,348 boxes at depth 10) and the
   plastic x y at a = 2 (opens at 8, the certificate unreached).

F3 THE CLOSED FORM [rule at the 26 opened pairs]. r_open = max(1,
   n_open - c) with n_open = floor(log_beta(1/theta)) + 1, theta =
   (Lam - Lam_law)/(w kappa), at all 26; K3 never fired. At the three
   silver pairs at a = 1 the clamp acts: n_open = 1 = c, the first
   round's box already at depth 2, so the printed phi and arc at the
   opening are the formula's at n_open and not the realized round's
   (which overshoots by a further depth); F5's ranges are read with
   that in mind and its verdict survives either reading. The box
   attaining the arc is the corner box at every one of the 20 product
   and divider pairs; at x^2 + y it has |x| at M and y off the corner
   at 6 of the 7 pairs (the seventh a corner by coincidence), as P-C
   said. The scan's g_max equals g(n) to four figures at every printed
   round past the opening but one: tribonacci x^2 + y at a = 1 opens
   at depth 1, where 2h = 1.09 M and the corner box straddles zero,
   its image's floor 0 rather than (M - 2h)^2, and reads 0.0933
   against the formula's 0.0874 -- the derivation's scope is
   beta^n >= 2, below which the formula is a lower bound on the arc;
   the opening round matched there and at every pair, none opening
   at a straddling depth without also opening by the formula.

F4 THE FOUR UNREAD PAIRS [rule at 25 killed pairs]. The Narayana
   divider at a = 2 opens at 5 and dies at 6, silver x^2 + y at a = 2
   at 4 and 5, the plastic x^2 + y at a = 1 at 4 and 5, the plastic
   divider at a = 1 at 8 and 9: lag 1 at each, K4 never fired. Over
   the 25 killed pairs with an opening the lag is 0 at 7, 1 at 14 and
   2 at 4, never more.

F5 THE OVERSHOOT [observation]. The four lag-2 pairs open barely: phi
   0.04, 0.07, 0.12, 0.15 (arcs at the opening 0.0037 to 0.0258),
   below every lag-0 pair (phi 0.17 to 1.00, median 0.59), so the
   transplant's letter held; but lag 0 and lag 1 overlap across the
   whole range (lag 1 phi 0.07 to 0.89, median 0.22), so the lag is
   not a function of the overshoot. What separates 0 from 1 is the
   offsets' arithmetic at the opening depth and not the arc's size.

VERDICT. The arc-opening depth is a closed form in the base, the digit
bound and the map's Lam with one curvature number kappa -- an absolute
slope drop for the polynomial maps, a relative one for the pole -- and
no tree: n_open = floor(log_beta(w kappa/(Lam - Lam_law))) + 1, the
round n_open - c. At L* the excess is at most 0 and no box opens, the
margin law's sufficiency in one line; below it the tree kills 0 to 2
rounds past the opening at every one of 25 pairs, so the certificate
depth is the formula plus two. Open: the lag's proof, and its
mechanism, which the overshoot bounds on one side only (read since as
the forced level walk's covering plus 0 or 1, explore_covering_lag.py
F5; the closed form and the lag rule stand as printed here).

RUN RECORD: pure Python, the shipped engines imported; boxes walked
level by level, a level capped at LEVEL_CAP boxes and a pair at WALL
seconds; under memwatch, peak commit 484 MB against the 512 MB
default (the depth-10 level of the Narayana divider at a = 2 held
whole), wall 168 s. Prints reproduced by:
python prime/code/explore_arc_opening.py [OFFSETS_PRINT_FILE] [LEVEL_CAP] [WALL_SECONDS]
"""
import math
import os
import re
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import explore_beta_delay as bd                            # noqa: E402
import explore_delay_sweep as ds                           # noqa: E402

FAILS = []
LEVEL_CAP = 600_000
WALL = 60.0
PAST_OPENING = 2


def ok(cond, msg):
    if not cond:
        FAILS.append(msg)
        print("  KILL:", msg)


class Scan(bd.BetaReader):
    """The shipped reader's boxes, walked level by level: no parent,
    no legality, no game."""

    def levels_to(self, n, cap, t_end):
        """The admitted boxes at every depth up to n; a level past the
        cap or the wall stops the walk (returns the depth reached)."""
        if not hasattr(self, "_levels"):
            self._levels = [[(self.B.zero,) * self.d]]
        while len(self._levels) - 1 < n:
            depth = len(self._levels)
            prev = self._levels[-1]
            B = self.B
            nxt = []
            for us in prev:
                for mv in self.moves:
                    us1 = tuple(B.add(B.mul(B.beta, u), self.delem[x]) for u, x in zip(us, mv))
                    if self.in_region(us1, depth):
                        nxt.append(us1)
                if len(nxt) > cap or time.time() > t_end:
                    return depth - 1
            self._levels.append(nxt)
        return n

    def arc_max(self, n, r):
        """The largest arc over the admitted boxes at depth n read at
        round r, and the box attaining it (its centre in units of M)."""
        B = self.B
        unit = B.fl ** (self.o - r)
        s = B.fl ** n
        best, arg = -math.inf, None
        for us in self._levels[n]:
            lo, hi = self.image(us, n)
            W = (B.ffloat(hi) - B.ffloat(lo)) / unit
            g = W - (self.wf - 1)
            if g > best:
                best, arg = g, tuple(B.tofloat(u) / s / self.Mf for u in us)
        return best, arg, len(self._levels[n])


def closed_form(B, fmap, a):
    """(L*, o, c, Lam, Lam_law, theta, kappa, n_open, r_open, phi, g(n))."""
    L, _, _ = bd.law_L(B, fmap, a)
    o = bd.least_lead(B, fmap, a)
    c = L - 1 - o
    M = B.ffloat((B.scale(a, B.one), B.bm1))
    w = 2 * M
    lam = B.ffloat(fmap.lam((B.scale(a, B.one), B.bm1)))
    lam_law = (w - 1) * B.fl ** (L - 1) / w
    divider = isinstance(fmap, bd.BDivision)
    kappa = lam_law if divider else 1.0
    theta = (lam - lam_law) / (w * kappa)
    x = math.log(1 / theta) / math.log(B.fl)
    n_open = math.floor(x) + 1
    phi = n_open - x
    g_inf = w * (lam - lam_law) / B.fl ** (L - 1)

    def g(n):
        two_h = w * B.fl ** (-n)
        if divider:
            return w * B.fl ** (1 - L) * (lam / (1 + two_h) - lam_law)
        return w * B.fl ** (1 - L) * (lam - lam_law - two_h)
    return dict(L=L, o=o, c=c, lam=lam, lam_law=lam_law, theta=theta, kappa=kappa,
                n_open=n_open, r_open=max(1, n_open - c), phi=phi, g=g, g_inf=g_inf, w=w)


def scan_pair(B, fmap, a, cf, cap, wall):
    sc = Scan(B, fmap, cf['c'], cf['o'], a=a)
    t_end = time.time() + wall
    rows = []
    r_open = None
    r = 0
    while True:
        r += 1
        n = max(0, r + cf['c'])
        reached = sc.levels_to(n, cap, t_end)
        if reached < n:
            return r_open, rows, reached
        g, arg, count = sc.arc_max(n, r)
        rows.append((r, n, count, g, arg))
        if g > 0 and r_open is None:
            r_open = r
        if r_open is not None and r >= r_open + PAST_OPENING:
            return r_open, rows, n
        if r > 40:
            return r_open, rows, n


def is_corner(arg, n, B, a, divider):
    """Every stream's centre at +-M (1 - beta^-n): the digits all +-a;
    the divider's y stream at -M."""
    edge = 1 - B.fl ** (-n)
    if not all(abs(abs(x) - edge) < 1e-9 for x in arg):
        return False
    return (arg[1] < 0) if divider else True


def read_offsets(path):
    """The enumeration's print: per pair 'round R, covering depth C, arc-opening depth O'."""
    out = {}
    if not path or not os.path.exists(path):
        return out
    pat = re.compile(r"^\s*(\S+) (.+?) a=(\d): round (\S+), covering depth (\S+), arc-opening depth (\S+)")
    with open(path, encoding="utf-8", errors="replace") as f:
        for line in f:
            m = pat.match(line)
            if m:
                base, name, a, r, _, ro = m.groups()
                out[(base, name, int(a))] = (None if r == "None" else int(r), None if ro == "None" else int(ro))
    return out


def main():
    path = sys.argv[1] if len(sys.argv) > 1 else None
    cap = int(sys.argv[2]) if len(sys.argv) > 2 else LEVEL_CAP
    wall = float(sys.argv[3]) if len(sys.argv) > 3 else WALL
    t0 = time.time()
    enum = read_offsets(path)
    print(f"THE ARC OPENING WITHOUT A TREE: level cap {cap} boxes, wall {wall:.0f}s per pair; "
          f"enumeration column from {path if enum else 'NONE (not handed in)'}: {len(enum)} pairs")

    print("\n=== K1 THE CONTROL: the plastic x y at a = 1 (the record: opens at round 10, g_max 0.0027, 0.0363, 0.0616)")
    Bp = [B for B in ds.beta_bases() if B.name.startswith("plastic")][0]
    fm = bd.BProduct(Bp)
    cf = closed_form(Bp, fm, 1)
    r_open, rows, reached = scan_pair(Bp, fm, 1, cf, cap, wall)
    for r, n, count, g, arg in rows[-4:]:
        print(f"  round {r:2d} depth {n:2d} boxes {count:7d} g_max {g:+.4f} formula g(n) {cf['g'](n):+.4f}")
    ok(r_open == 10, f"K1: the plastic x y opens at round {r_open}, the record's 10")
    got = {r: g for r, n, count, g, arg in rows}
    for r, want in ((10, 0.0027), (11, 0.0363), (12, 0.0616)):
        ok(r in got and abs(got[r] - want) <= 0.0005, f"K1: g_max at round {r} is {got.get(r)}, the record's {want}")
    if FAILS:
        print("\nCONTROL FAILED; nothing below is read.")
        return

    print("\n=== THE 30 BETA PAIRS at L* - 1: the closed form, the scan, the enumeration, the kill\n"
          "    (theta the opening share, n_open its depth, phi the overshoot in (0, 1]; "
          "r_open by formula / scan / enumeration; r_kill the certificate's; corner? the box attaining the arc)")
    table = []
    for B in ds.beta_bases():
        for a in (1, 2):
            for fmap in ds.beta_maps(B, a):
                key = (B.name.split()[0], fmap.name, a)
                label = f"{key[0]} {fmap.name} a={a}"
                cf = closed_form(B, fmap, a)
                t1 = time.time()
                r_open, rows, reached = scan_pair(B, fmap, a, cf, cap, wall)
                secs = time.time() - t1
                divider = isinstance(fmap, bd.BDivision)
                corner = None
                gcheck = ""
                if r_open is not None:
                    row = [x for x in rows if x[0] == r_open][0]
                    corner = is_corner(row[4], row[1], B, a, divider)
                    gs = [(x[3], cf['g'](x[1])) for x in rows if x[0] >= r_open]
                    gcheck = " ".join(f"{g:.4f}/{gf:.4f}" for g, gf in gs)
                r_kill, r_enum = enum.get(key, (None, None))
                lag = r_kill - r_open if (r_kill is not None and r_open is not None) else None
                boxes = rows[-1][2] if rows else 0
                print(f"  {label}: L*={cf['L']} o={cf['o']} c={cf['c']} Lam {cf['lam']:.4f} Lam_law {cf['lam_law']:.4f} "
                      f"theta {cf['theta']:.5f} n_open {cf['n_open']} phi {cf['phi']:.2f} | r_open formula {cf['r_open']} "
                      f"scan {r_open} enum {r_enum} | r_kill {r_kill} lag {lag} | corner {corner} | "
                      f"g scan/formula {gcheck} | boxes at last level {boxes}, reached depth {reached}, {secs:.1f}s")
                if r_open is None:
                    print(f"    UNREACHED: the scan stopped at depth {reached} before the opening (formula round {cf['r_open']})")
                else:
                    if r_enum is not None:
                        ok(r_open == r_enum, f"K2 {label}: scan opening {r_open} against the enumeration's {r_enum}")
                    ok(r_open == cf['r_open'], f"K3 {label}: scan opening {r_open} against the closed form's {cf['r_open']}"
                                               f" ({'corner box' if corner else 'NOT a corner box'})")
                    if lag is not None and r_enum is None:
                        ok(lag <= 2, f"K4 {label}: the certificate's round {r_kill} is {lag} past the opening")
                table.append((label, cf, r_open, r_enum, r_kill, lag, corner))

    print("\n=== THE READING: the lag r_kill - r_open over the killed pairs, and the lag against the overshoot phi")
    lags = {}
    for label, cf, r_open, r_enum, r_kill, lag, corner in sorted(table, key=lambda t: (t[5] is None, t[5] or 0, t[1]['phi'])):
        if lag is None:
            continue
        lags[lag] = lags.get(lag, 0) + 1
        print(f"  lag {lag} phi {cf['phi']:.2f} theta {cf['theta']:.5f} g_inf {cf['g_inf']:.4f} "
              f"g at opening {cf['g'](cf['n_open']):.4f} r_open {r_open} r_kill {r_kill}"
              f"{'' if r_enum is not None else ' (unread by the enumeration)'}  {label}")
    print(f"  killed pairs with an opening: {sum(lags.values())}; pairs by lag: {sorted(lags.items())}")
    by_lag = {}
    for label, cf, r_open, r_enum, r_kill, lag, corner in table:
        if lag is not None:
            by_lag.setdefault(lag, []).append(cf['phi'])
    for lag in sorted(by_lag):
        v = sorted(by_lag[lag])
        print(f"  lag {lag}: {len(v)} pairs, phi median {v[len(v) // 2]:.2f}, range {v[0]:.2f}..{v[-1]:.2f}")
    print(f"  formula = scan at {sum(1 for t in table if t[2] is not None and t[2] == t[1]['r_open'])} of "
          f"{sum(1 for t in table if t[2] is not None)} pairs the scan opened; corner box at "
          f"{sum(1 for t in table if t[6])} of them; scan = enumeration at "
          f"{sum(1 for t in table if t[2] is not None and t[3] is not None and t[2] == t[3])} of "
          f"{sum(1 for t in table if t[2] is not None and t[3] is not None)} read pairs")

    print(f"\nwall {time.time() - t0:.0f}s; {'ALL KILLS MISSED' if not FAILS else str(len(FAILS)) + ' KILL(S) FIRED'}")


if __name__ == "__main__":
    main()
