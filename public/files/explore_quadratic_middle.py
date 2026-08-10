"""Is the middle class empty on the arithmetic maps at the quadratic
trailing windows — the cap-gap read at the window family the claim
has not been measured on.

THE QUESTION
------------
The reading gate's whole content is a claim about maps, not topology:
between LIPSCHITZ (readable at bounded delay) and DISCONTINUOUS
(unreadable at any modulus) sits MIDDLE — continuous with unbounded
modulus, readable only at a lookahead growing with depth — and on the
ARITHMETIC maps (integer multiplication, floor division, the
odometer) that class has measured EMPTY at five windows: the b-adic
row and four continued-fraction windows (explore_continuity_converse.py).
A class-emptiness claim should not rest on one rig and one window
family. This rig reads the same observable at the family that claim
has never been measured on: the trailing Zeckendorf window and the
quadratic Ostrowski windows — non-positional covers, odometer
completions, the windows where every rational integer m >= 2 is a
non-unit. Two outcomes, both findings: every arithmetic map lands
cap-shaped (the empty middle confirmed by a second instrument at a
second family), or some map's column settles under a moving cap while
its row grows — the first arithmetic member of MIDDLE, and a
counterexample to the emptiness the gate rests on.

THE OBJECTS, fixed
------------------
A WINDOW here is a nested partition of the nonnegative integers by
greedy digits against the convergent denominators q_k of a quadratic
irrational (q_0 = 1, q_1 = a_1, q_k = a_k q_{k-1} + q_{k-2}) — the
trailing Ostrowski window, with the classical legality checked, never
assumed. Four are read, all eventually periodic (quadratic):

  WPHI     alpha = phi - 1        [0; 1, 1, 1, ...]   (Zeckendorf)
  WSILVER  alpha = sqrt(2) - 1    [0; 2, 2, 2, ...]   (Pell)
  WBRONZE  (3 + sqrt(13))/2 conj  [0; 3, 3, 3, ...]
  WALT     alpha = sqrt(3) - 1    [0; 1, 2, 1, 2, ...] (period 2)

plus positional base 2 as an instrument calibration frame only.
The depth-t cell of n is agreement on the t low-order digits; the
metric is the agreement ultrametric d(x, y) = 2^{-agr(x, y)}.
c_min(f, t) is the least c with agr(n, n') >= t + c forcing
agr(f n, f n') >= t. The completion at every quadratic window is an
odometer and not a ring (the Zeckendorf case proved,
explore_zeckendorf_discontinuity.py), and no rational integer
m >= 2 is a unit of the window's order (norm m^2).

THE INSTRUMENT (carried whole from explore_continuity_converse.py,
recalibrated here before any verdict). Three readings of one table:
  ROW    (t across, N fixed): c_min constant iff f is Lipschitz.
  COLUMN (t fixed, range growing): c_min settles iff f is continuous
         — c_min(f, t) is the lookahead the modulus assigns to t.
  CAP GAP: the discriminator. Ranges are indexed by DEPTH —
         N = q_{K+1} - 1 at three successive K, so the deepest
         realized agreement CAP moves by one per step by
         construction. CAP - c_min at fixed t is bounded and small
         for a discontinuous map (the deepest-agreeing pairs still
         break at depth t) and grows with the cap for a continuous
         one. Column verdicts are read at t = 1 and t = 2 ONLY: at
         depths near the top of the table a stalled column can be
         the table's own ceiling (pairs agreeing deeper have images
         agreeing past the tabulated depth), and t = 1, 2 are where
         that censoring cannot reach.

WHAT IS KNOWN AT THIS FAMILY BEFORE THIS RUN — the poles the KILL
check reads. Continuous pole: the odometer n+1 reads at delay 1
(explore_zeckendorf_window.py, explore_ostrowski_window.py).
Discontinuous pole: x2 at Zeckendorf has a proved discontinuity (the
step-3 comb family, explore_zeckendorf_discontinuity.py), and xa at a
constant-a window inherits the same down-carry mechanism from
a q_k = q_{k+1} - q_{k-1}. Everything else — 3n, 4n, n//2, n//3 at
Zeckendorf; the off-a multiplications and every floor division at the
other three — carries only a DIAGONAL verdict ("unreadable at
bounded delay"), which by construction cannot tell MIDDLE from
DISCONTINUOUS. Those maps are the hunt.

HAND-ATTACK, before any engine
------------------------------
H1. The transplant that must be flagged rather than trusted: at
    positional b = 2 the decimation D(n) = sum_t d_{2t}(n) 2^t is
    the proved MIDDLE witness (c_min = t - 1 exactly), and its
    mechanism is that positional carries go only UP, so packing
    digits down leaves low image digits determined by a
    bounded-multiple depth. At Zeckendorf that intuition FAILS in
    the down direction: re-legalizing a packed string sums Fibonacci
    numbers whose duplicates resolve by 2 F_m = F_{m+1} + F_{m-2},
    a carry that rewrites a LOWER position — the exact mechanism
    that kills x2 there. So the Zeckendorf decimation
    D_phi(n) = sum_j b_{2j+1}(n) q_{1+j} (extract the odd-position
    digits, pack them down; position 0 is vacuous at a_1 = 1) is
    EXPLORATORY: the positional transplant predicts MIDDLE, the
    down-carry says it may be cap-shaped, and neither print kills
    anything — either way it is the first compression map read at a
    non-positional window.
H2. Masking is not compression: keeping the odd-position digits IN
    PLACE (image a subword) deletes digits and cannot create an
    illegal adjacency, so it is carry-free and 1-Lipschitz — no
    middle witness lives there. The unbounded-modulus shape needs
    packing DOWN, which is exactly where the carry algebra bites.
    So this family has no cheap derivable middle control, and the
    KILL check rests on the two poles above.
H3. Why the hunt is not idle at the division maps: x2 discontinuity
    at Zeckendorf is proved by a comb whose DOUBLES converge to two
    points. Halving is not its inverse on integers (floor), and no
    comb family for n//2 is on record at any quadratic window — a
    map can be discontinuous in one direction and continuous in the
    other (base 10: n//3 discontinuous, 3n Lipschitz).

PREDICTIONS, frozen before the engine
-------------------------------------
P1  CONTROL. c_min(id, t) = 0 at every window, depth, range. The
    odometer n+1 is row-constant with value <= 2 at every window
    and its CAP GAP GROWS across the three depth-indexed ranges.
    Either half failing means the instrument is wrong and no
    verdict below is readable.
P2  CALIBRATION. At positional b = 2 the decimation D prints
    c_min(D, t) = t - 1 on the prefix the range admits
    (N > 2^{2t-1}), reproducing the sibling rig's row on this
    rig's code path, and its column settles: the fixed-t value
    does not move once its witness exists.
P3  THE DISCONTINUOUS POLE. x2 at WPHI, x2 at WSILVER, x3 at
    WBRONZE: cap gap bounded by 3 at t = 1, 2 across the three
    ranges. KILL (instrument): a growing gap at any of these three,
    which would mean the discriminator does not separate the
    classes at this family and no hunt verdict is readable.
P4  THE HUNT. Every remaining integer map — 3n, 4n, n//2, n//3 at
    WPHI; 3n, n//2 at WSILVER; 2n, n//2 at WBRONZE; 2n, 3n, n//2
    at WALT — is cap-shaped: gap at t = 1, 2 bounded across the
    moving cap, the middle class EMPTY at this family too.
    KILL (the larger find): any of them settles at t = 1 and 2
    across the moving cap while its row still grows — an
    arithmetic map continuous at an unbounded modulus, the first
    member of MIDDLE and a counterexample to the emptiness claim.
P5  EXPLORATORY (transplant marked, H1). D_phi at WPHI: the
    positional transplant predicts settling column + growing row
    (MIDDLE); the down-carry predicts cap-shaped. Weighed after the
    run; no kill either way.

THE DESIGN
----------
Exhaustive per range, no sampling. Digits by greedy descent only.
c_min exactly, by the sorted-consecutive-pairs identity: sorting the
integers by low-first digit string makes every depth-p cell a
contiguous block, so some CONSECUTIVE pair realizes the deepest
agreement among pairs whose images differ before t. Digit strings
are read to the frame's full usable depth plus margin so no realized
agreement is truncated (the sibling rig's Fibonacci frames saturated
their fixed string cut; here the cut tracks the window).

E1  DIGIT SANITY + CONTROLS. Reconstruction and legality exhaustive
    per frame; c_min(id) and the odometer row print before any
    verdict.
E2  CALIBRATION. Base-2 decimation against the closed form t - 1.
E3  THE TABLES. Per window, the three depth-indexed frames
    N = q_{K+1} - 1: c_min(f, t) rows for every map above, CAP per
    frame, and the per-map verdict line — gap at t = 1, 2 across
    the three caps, flagged SETTLING (gap grows) vs CAP-SHAPED
    (gap bounded).

RESOURCE. One greedy descent per (frame, map, input); the top frame
per window is the largest N whose usable depth is that window's
deepest K, which can overshoot the nominal 3 * 10^5 by up to the
window's growth ratio (the bronze top frame is N = 467279); three
frames per window, dropped between windows. Estimate 2-6 minutes
wall, peak under the sibling rig's 250 MB; run under memwatch at
the 512 MB default.

RUN RECORD
----------
One run under memwatch: wall 36.3 s, peak working set 182.7 MB
against the 512 MB ceiling (the 2-6 minute estimate overshot the
same way the sibling rig's did, and for the recorded reason: the
greedy descent costs the digit count, not the weight-list length).
E1 green at every frame before any verdict: zero reconstruction
failures, zero legality failures, c_min(id) = 0 everywhere. Frames:
WPHI K = 24, 25, 26 (N = 121392, 196417, 317810), WSILVER
K = 12, 13, 14 (N = 80781, 195024, 470831), WBRONZE K = 8, 9, 10
(N = 42836, 141480, 467279), WALT K = 17, 18, 19
(N = 110770, 151315, 413402); CAP = K at every frame.
ONE INSTRUMENT CAVEAT, read from the prints and applied to every
verdict below: at the two windows with a_1 = 1 (WPHI, WALT) the
digit b_0 is identically zero, so the t = 1 column is vacuous —
every map prints c_min(., 1) = 0 and the t = 1 gap reads as the
whole cap for every map, odometer and doubling alike. At those two
windows the readable column is t = 2; at WSILVER and WBRONZE
(a_1 >= 2) both columns are real and agree.

FINDINGS (each at its own tier)
-------------------------------
F1  THE PORTED INSTRUMENT SEES MIDDLE WHERE IT EXISTS (calibration).
    Base-2 decimation printed c_min(D, t) = t - 1 on the full
    in-scope prefix at all three ranges (t <= 7 at N = 30000,
    t <= 8 at 100000 and 300000), the proved closed form to the
    digit. P2 lands.
F2  THE POLES SEPARATE AT THIS FAMILY (control). The odometer is
    row-constant at 1 with a gap growing step for step with the cap
    at every window (WPHI 23-24-25 at t = 2, WSILVER 11-12-13,
    WBRONZE 7-8-9, WALT 16-17-18). The proved-discontinuous maps
    pin to the cap: x2 at WPHI gap 1, 1, 1 at t = 2; x2 at WSILVER
    gap 0, 0, 0 at t = 1; x3 at WBRONZE gap 0, 0, 0 at t = 1. P1
    and P3 land; the instrument kill misses.
F3  THE MIDDLE CLASS IS EMPTY ON THE ARITHMETIC MAPS AT THE
    QUADRATIC FAMILY (rule at scanned scope — the finding this rig
    was built for). Every integer map beyond the odometer — 2n, 3n,
    4n, n//2, n//3 — is cap-shaped at every window: c_min at the
    readable column tracks the moving cap exactly, gap pinned at
    0 or 1 across all three depth-indexed ranges, at all four
    windows. No map settles; nothing sits between the odometer's
    settled column and the cap-pinned rest. The emptiness claim the
    reading gate rests on is now measured by two instruments at two
    window families — the b-adic row and four continued-fraction
    windows (explore_continuity_converse.py), and here four
    quadratic Ostrowski windows including the one whose x2 kill is
    a theorem. P4 lands; the counterexample hunt comes home empty.
F4  THE POSITIONAL MIDDLE WITNESS DOES NOT TRANSPLANT (observation,
    the exploratory P5 weighed). D_phi — the same
    extract-and-pack-down map that is the proved middle member at
    base 2 — is CAP-SHAPED at Zeckendorf: gap 2, 3, 2 at t = 2,
    bounded, not growing. The down-carry named in H1 wins: packing
    digits down forces Fibonacci re-legalization, whose duplicate
    resolution 2 F_m = F_{m+1} + F_{m-2} rewrites lower positions,
    and the compression map falls to the same mechanism that kills
    doubling. So at the quadratic windows MIDDLE has no known
    member of ANY kind — not only do the arithmetic maps avoid it,
    the one engineered witness class collapses into DISCONTINUOUS
    when carried there. What dies at the odometer windows is the
    COMPRESSION mechanism, not the class: a locally constant
    stretcher — constant on each "lowest nonzero digit at position
    k" cell, sent to an integer whose lowest nonzero digit sits at
    position k/2 rounded up — is continuous with modulus about 2t
    and Lipschitz at no constant, an integer map, so MIDDLE is
    inhabited there by design (a derivation, not a print of this
    rig). The sharpening is therefore about mechanisms: pack-down
    compression inhabits MIDDLE at positional windows and falls to
    the down-carry at odometer ones, while the designed stretcher
    inhabits it everywhere.

THE READING. The hunt was for an arithmetic map continuous at an
unbounded modulus, and the family where it was likeliest — the
non-positional windows where nothing rational is a unit — refuses
it: every tested arithmetic map pins to the cap, the odometer
settles, and nothing lands between. The emptiness the reading gate
rests on now stands measured at two instruments and two families.
What the rig found instead of a counterexample is a mechanism
split: the pack-down compression that inhabits MIDDLE at
positional windows dies at the odometer ones, killed by the same
down-carry as doubling, while the class itself stays inhabited
there by the designed stretcher of F4 — so MIDDLE is everywhere a
class of DESIGNED maps, entered by compression only where carries
go up, and entered by arithmetic nowhere yet measured.
"""

from bisect import bisect_right

T_MAX = 8
N_TOP = 300_000


# ---------------------------------------------------------------- windows

class Window:
    """A trailing window: greedy digits against CF-convergent weights
    (kind "cf") or powers of a base (kind "pos")."""

    def __init__(self, name, kind, a=None, base=None):
        self.name = name
        self.kind = kind
        self.a = a
        self.base = base

    def weights(self, npos):
        if self.kind == "pos":
            return [self.base ** k for k in range(npos + 1)]
        q = [1, self.a[0]]
        while len(q) <= npos and len(q) <= len(self.a):
            q.append(self.a[len(q) - 1] * q[-1] + q[-2])
        return q

    def legality_failures(self, d):
        if self.kind == "pos":
            return sum(1 for x in d if x > self.base - 1)
        a = self.a
        fails = 0
        if d[0] > a[0] - 1:
            fails += 1
        for k in range(1, len(d)):
            if k >= len(a):
                break
            if d[k] > a[k]:
                fails += 1
            if d[k] == a[k] and d[k - 1] != 0:
                fails += 1
        return fails


WANT = 80
WINDOWS = [
    Window("WPHI    phi-1       [0;1,1,1,...]  Zeckendorf", "cf",
           a=[1] * WANT),
    Window("WSILVER sqrt(2)-1   [0;2,2,2,...]  Pell", "cf",
           a=[2] * WANT),
    Window("WBRONZE bronze      [0;3,3,3,...]", "cf",
           a=[3] * WANT),
    Window("WALT    sqrt(3)-1   [0;1,2,1,2,...] period 2", "cf",
           a=[1, 2] * (WANT // 2)),
]
B2 = Window("B2 base 2 POSITIONAL (calibration)", "pos", base=2)


# ------------------------------------------------------------- instrument

def greedy(v, q):
    """Greedy digits of v >= 0 against weights q, low index first."""
    d = [0] * len(q)
    for k in range(bisect_right(q, v) - 1, -1, -1):
        if q[k] <= v:
            b = v // q[k]
            d[k] = b
            v -= b * q[k]
    return d


def usable_depth(q, top):
    t = 0
    while t + 1 < len(q) and q[t + 1] <= top:
        t += 1
    return t


class Frame:
    """One (window, range) frame: sorted digit strings, agreement
    depths of consecutive pairs, and exact c_min rows."""

    def __init__(self, win, n):
        self.win, self.n = win, n
        self.kn = usable_depth(win.weights(200), n)
        self.tmax = min(T_MAX, self.kn - 1)
        self.depth = self.kn + 4
        self.q = win.weights(self.kn + 8)
        strings = [tuple(greedy(i, self.q)[:self.depth]) for i in range(n)]
        self.order = sorted(range(n), key=lambda i: strings[i])
        self.agr = []
        for j in range(n - 1):
            s1, s2 = strings[self.order[j]], strings[self.order[j + 1]]
            p = 0
            while p < self.depth and s1[p] == s2[p]:
                p += 1
            self.agr.append(p)
        self.cap = max(self.agr) if self.agr else 0
        self.strings = strings

    def sanity(self):
        recon = legal = 0
        for i in range(self.n):
            d = greedy(i, self.q)
            if sum(x * w for x, w in zip(d, self.q)) != i:
                recon += 1
            legal += self.win.legality_failures(d)
        return recon, legal

    def row(self, f):
        imgs = [tuple(greedy(f(i), self.q)[:self.tmax])
                for i in range(self.n)]
        best = [-1] * (self.tmax + 1)
        for j in range(self.n - 1):
            u1, u2 = imgs[self.order[j]], imgs[self.order[j + 1]]
            dpos = 0
            while dpos < self.tmax and u1[dpos] == u2[dpos]:
                dpos += 1
            if dpos < self.tmax:
                p = self.agr[j]
                for t in range(dpos + 1, self.tmax + 1):
                    if p > best[t]:
                        best[t] = p
        return [max(0, best[t] - t + 1) for t in range(1, self.tmax + 1)]


def fmt(row):
    return " ".join(f"{c:>2d}" for c in row)


def depth_indexed_frames(win):
    """Three successive depths K ending at the deepest whose weight
    stays under N_TOP; each frame takes N = q_{K+1} - 1, the largest
    range at usable depth exactly K (the top frame therefore
    overshoots N_TOP itself), so the cap moves by one per step by
    construction."""
    q = win.weights(120)
    ktop = usable_depth(q, N_TOP)
    return [(k, q[k + 1] - 1) for k in (ktop - 2, ktop - 1, ktop)]


def zeck_decimate(q):
    """D_phi: extract the digits at odd positions (position 0 is vacuous
    at a_1 = 1) and pack them down one full position scale."""
    def f(i):
        d = greedy(i, q)
        return sum(d[1 + 2 * j] * q[1 + j]
                   for j in range((len(d) - 1) // 2)
                   if 1 + j < len(q))
    return f


def pos_decimate(base):
    def f(i):
        v, w, k = 0, 1, 0
        while i:
            if k % 2 == 0:
                v += (i % base) * w
                w *= base
            i //= base
            k += 1
        return v
    return f


# ------------------------------------------------------------ experiments

def verdict(name, caps, g1, g2):
    """The cap-gap verdict line for one map: gap = CAP - c_min at
    t = 1, 2 across the three frames."""
    gaps1 = [c - v for c, v in zip(caps, g1)]
    gaps2 = [c - v for c, v in zip(caps, g2)]
    shape1 = "SETTLING" if gaps1[-1] > gaps1[0] + 1 else "CAP-SHAPED"
    shape2 = "SETTLING" if gaps2[-1] > gaps2[0] + 1 else "CAP-SHAPED"
    print(f"    verdict {name:8s} gap(t=1) {gaps1} {shape1:10s} "
          f"gap(t=2) {gaps2} {shape2}")


def run_window(win, maps):
    print("=" * 74)
    frames_spec = depth_indexed_frames(win)
    print(f"{win.name}   depths K = {[k for k, _ in frames_spec]}")
    rows = {name: [] for name, _ in maps}
    caps = []
    for k, n in frames_spec:
        fr = Frame(win, n)
        recon, legal = fr.sanity()
        idrow = fr.row(lambda i: i)
        print(f"  K = {k:2d}  N = {n:6d}  usable {fr.kn:2d}  CAP {fr.cap:2d}"
              f"  recon fails {recon}  legality fails {legal}"
              f"  c_min(id) {fmt(idrow)}")
        assert recon == 0 and legal == 0 and not any(idrow)
        caps.append(fr.cap)
        for name, f in maps:
            if name == "D_phi":
                f = zeck_decimate(fr.q)
            rows[name].append((k, n, fr.tmax, fr.row(f)))
        del fr
    for name, _ in maps:
        print(f"  {name}")
        for k, n, tmax, row in rows[name]:
            print(f"    K = {k:2d}  N = {n:6d}  t = 1..{tmax:<2d}  "
                  + fmt(row))
        g1 = [row[0] for _, _, _, row in rows[name]]
        g2 = [row[1] for _, _, _, row in rows[name]]
        verdict(name, caps, g1, g2)
    print()


def e2_calibration():
    print("=" * 74)
    print("E2 CALIBRATION: base-2 decimation against the closed form "
          "c_min(D, t) = t - 1")
    D = pos_decimate(2)
    for n in (30_000, 100_000, 300_000):
        fr = Frame(B2, n)
        row = fr.row(D)
        pred = [t - 1 for t in range(1, fr.tmax + 1)]
        scope = max((t for t in range(1, fr.tmax + 1)
                     if 2 ** (2 * t - 1) < n), default=0)
        ok = row[:scope] == pred[:scope]
        print(f"  N = {n:6d}  CAP {fr.cap:2d}  t = 1..{fr.tmax:<2d}  "
              f"measured {fmt(row)}  in-scope t <= {scope}: match {ok}")
        del fr
    print()


ARITH = [("n+1", lambda i: i + 1), ("2n", lambda i: 2 * i),
         ("3n", lambda i: 3 * i), ("4n", lambda i: 4 * i),
         ("n//2", lambda i: i // 2), ("n//3", lambda i: i // 3)]


def main():
    e2_calibration()
    run_window(WINDOWS[0], ARITH + [("D_phi", None)])
    for win in WINDOWS[1:]:
        run_window(win, ARITH)


if __name__ == "__main__":
    main()
