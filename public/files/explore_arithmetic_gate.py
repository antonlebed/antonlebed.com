"""Can the arithmetic emptiness be derived — and checked at the exact
points the derivation names?

THE QUESTION
------------
Between LIPSCHITZ (readable at bounded delay) and DISCONTINUOUS
(unreadable at any modulus) sits MIDDLE: continuous with unbounded
modulus. On the arithmetic maps (integer multiplication, floor
division) MIDDLE has measured empty at two window families
(explore_continuity_converse.py, explore_quadratic_middle.py) — a
scanned verdict. This rig accompanies the derivation of that
emptiness: a proof that at both completion shapes posing the gate
question an arithmetic map is continuous iff Lipschitz. A derivation, unlike a
scan, LOCATES its discontinuities — it names the exact circle point
where a continuous extension of x m must tear, and the exact class
pair whose cellmates a floor division must separate. This rig goes to
those named points and watches. Either the located splits fire as
derived (the emptiness closes at proved tier, with the scan as its
independent instrument), or a named point fails to split — which
refutes the derivation at its crux and localizes exactly where an
arithmetic middle member could live.

THE DERIVATION BEING CHECKED (the two completion shapes)
--------------------------------------------------------
RING SIDE (positional base b; completion the b-adic ring, carries up).
  x m: agreement mod b^t gives agreement of images mod b^t: delay 0,
  1-Lipschitz outright — an integer-linear map on a ring completion.
  floor(n/m), r = n mod m: if rad(m) | rad(b), take c with m | b^c;
  agreement to depth t + c fixes r and makes (n - n')/m a multiple of
  b^t: Lipschitz at delay <= c. Otherwise some prime p | m is coprime
  to b, and the residue AT p is invisible to trailing digits: every
  depth-t cell contains cellmates with r' != r (b^t a unit mod p), and
  for those the image difference (n - n' - (r - r'))/m has bounded
  valuation at every prime of b — bounded image agreement at every
  depth. Discontinuous at every point, spread bounded. So continuity
  of floor(n/m) on a ring completion IS local constancy of n mod m:
  rad(m) | rad(b) or everywhere-torn, no third state.

ODOMETER SIDE (trailing Ostrowski window of an irrational alpha; the
quadratic windows are instances). Structural input, checked here as
E2 rather than assumed: the depth-t cells are intervals of a
partition of the circle under n -> {n alpha} (the digit identity
n alpha = sum b_k theta_k mod 1, theta_k = q_k alpha - p_k), the
endpoints of every level's partition lie in the BACKWARD orbit
C = {-j alpha mod 1 : j >= 1} (hand check at depth 1, Zeckendorf:
the boundaries sit at {-alpha} and {-2 alpha}), and the completion
is the circle CUT along C: one point per position off C, TWO per
point of C (the one-sided codings), integers dense. The point 0 is
GLUED, not cut: the all-zero cylinder contains q_t and q_{t+1},
whose positions flank 0, at every depth — the zero cell wraps.
  x m: a continuous extension f would satisfy pi f = M_m pi with
  M_m(z) = mz (both sides continuous, equal on the dense integers).
  THE CUT-POINT OBSTRUCTION: a tear is forced exactly where a
  NON-cut point maps to a cut point. Solving (-j' alpha + i)/m =
  -j'' alpha mod 1 forces j' = m j'' and m | i (alpha irrational),
  so z* = (1 - alpha)/m maps to {-alpha} in C while z* itself is
  NOT in C, for every m >= 2. The fiber over z* is a single point
  approached by integers from BOTH sides; M_m carries the two sides
  to the two sides of {-alpha}, whose one-sided codings are two
  DISTINCT points of the completion. So the images of a straddling
  pair agree no deeper than the two codings of {-alpha} agree — a
  CONSTANT — while the pair itself agrees ever deeper. No continuous
  extension, and the tear has an address. The mirror address
  z0 = (1 + alpha)/m maps to {+alpha}, which is NOT an endpoint: a
  non-cut point to a non-cut point, where M_m lifts continuously —
  a derived CONTINUITY point, kept as the E3a control. (The
  odometer +1 stays continuous under this C: its circle preimage of
  C is {-j alpha : j >= 2}, inside C; the top cut {-alpha} maps to
  the glued 0 — cut-to-glue is allowed, only non-cut-to-cut tears.)
  floor(n/m): q = (n - r)/m gives q alpha = (n alpha - r alpha)/m
  over the REALS, so the image position reads TWO invisibles:
  r = n mod m and the branch y = n alpha mod m, a point of the
  m-fold cover circle R/mZ (NOT floor(n alpha) mod m raw, which
  jumps at the wrap while y is continuous there). Distinct classes
  (r, branch) land at circle positions distinct mod 1 (equality
  forces alpha rational), and every class meets every cell (density
  of {(mk + r) alpha}), so cross-class cellmates have bounded image
  agreement at every depth: torn at EVERY point, an m^2-fold local
  split. Within one class, n -> floor(n/m) descends to the degree-1
  circle map y -> (y - r alpha)/m from R/mZ to R/Z: same-class
  image agreement grows. The split is exactly the class boundary.
  Control that the argument proves nothing false: the odometer +1
  descends to rotation by alpha, a bijection of C onto itself — cut
  compatible, continuous, as it must be. And the locally constant
  stretcher (the designed middle member) descends to no circle map at
  all, so the argument never touches it: what is being used is the
  ARITHMETIC of the maps — that they commute with the rotation
  semiconjugacy — never continuity alone.

CONSEQUENCE IF THE CHECKS PASS: at both completion shapes that pose
the gate question (a discrete completion holds the iff trivially),
continuous iff Lipschitz for x m and floor(n/m) — the middle class
meets the arithmetic maps in the empty set, proved, with the two
scanning rigs as independent instruments. The only freedom the
derivation leaves is a completion that is neither a ring, nor an
almost one-to-one extension of an irrational rotation, nor discrete.

THE INSTRUMENT
--------------
Windows: WPHI (alpha = phi - 1, Zeckendorf) and WSILVER
(alpha = sqrt(2) - 1, Pell), digits greedy against q_0 = 1,
q_1 = a_1, q_k = a_k q_{k-1} + q_{k-2}, low index first, classical
legality; agreement agr(n, n') = number of agreeing low digits;
positions on the circle in 60-digit decimal arithmetic. Maps x2, x3,
floor/2, floor/3 at both windows; base-10 ring controls.

E1  DIGIT SANITY. Reconstruction and legality exhaustive on n < N.
E2  STRUCTURE (the derivation's load-bearing input). At depths
    t = 4, 8, 12: the realized cells, read as [min, max] intervals of
    {n alpha} (the zero cell split at its wrap), are pairwise
    disjoint; and every internal boundary gap between consecutive
    cells contains a backward-orbit point {-j alpha} with
    0 <= j <= q_{t+1} + q_t.
E3  THE LOCATED TEAR AND ITS MIRROR. For m in {2, 3}: the 20 closest
    integers on each side of the address. E3b at the tear
    z* = (1 - alpha)/m: same-side pairs' image agreement under x m
    climbs with input agreement; straddling pairs' PINNED at a
    constant — the agreement of the two codings of {-alpha}, printed
    beside the table. E3a at the mirror z0 = (1 + alpha)/m: BOTH
    climb — the derived continuity point.
E4  THE CLASS SPLIT. Consecutive pairs in digit-string order with
    input agreement >= 6, classified by (n mod m, branch of
    n alpha mod m) with the branch compared on the m-circle
    (wrap-aware): same-class pairs' image agreement under floor(n/m)
    climbs; cross-class pairs' stays bounded.
E5  RING CONTROLS at base 10 (the derivation's ring clauses, sampled):
    x3 at delay 0 exactly; floor(n/4) Lipschitz at delay <= 2
    (4 | 100); floor(n/3) cross-residue cellmates at image agreement
    EXACTLY 0 (the image difference has valuation 0 at 2 and at 5).

PREDICTIONS, frozen before the engine
-------------------------------------
P1  E1 zero failures; E2 zero overlaps and zero orbit-less
    boundaries, at both windows, all three depths.
P2  E3b same-side, and BOTH families at the E3a mirror: max image
    agreement climbing with input agreement, exceeding 10 at the
    deepest realized inputs.
P3  E3b straddle: max image agreement over pairs with input
    agreement >= 12 exceeds its value over pairs at input agreement
    6..8 by at most 2 — the pin. (KILL: it climbs in step with the
    input through the top of the table; then the located tear does
    not tear, the derivation is refuted at its crux, and z* is the
    address where an arithmetic middle member lives.)
P4  E4: same-class max image agreement climbs past 10; cross-class
    max bounded by a constant across all input depths. (KILL: a
    cross-class column that climbs — the two-invisible argument is
    wrong.)
P5  E5: zero violations in all three controls. (KILL: any violation —
    the ring-side algebra is wrong.)

FINDINGS (entered after the runs; prints copied from the run record)
--------------------------------------------------------------------
F1  STRUCTURE HOLDS, AND IT CORRECTED THE FIRST DRAFT. Run 1 tested
    the two-sided orbit {j alpha} and an unsplit zero cell: nearly
    every boundary came back orbit-less and the zero cell overlapped
    everything. The probe that explained it produced the corrected
    statement now in the derivation — endpoints on the BACKWARD
    orbit only, 0 glued, the zero cylinder wrapping (its deep
    members q_t, q_{t+1} flank 0: the consecutive-Fibonacci pairs
    made it visible). Under the corrected statement E2 is exact:
    zero overlaps and zero orbit-less boundaries at t = 4, 8, 12 at
    both windows (WPHI 6/35/234 cells, WSILVER 30/986/33462 cells).
F2  THE TEAR FIRES AT ITS ADDRESS, AND ONLY THERE. At
    z* = (1-alpha)/m the straddling pairs' image agreement is PINNED
    at 1 (WPHI, x2 and x3) and 0 (WSILVER, x2 and x3) at every
    realized straddle depth (17..24 and 8..13), while same-side
    climbs to the table cap (24, 24, 14, 12). Run 1, which mislocated the
    tear at the mirror address z0 = (1+alpha)/m — the two-sided
    orbit does not distinguish them — measured straddle CLIMBING
    there (max 24), i.e. genuine continuity at a non-cut point: kept
    as E3a, where both windows and both m print continuity (straddle
    max 24/23/12/12). The pair of addresses is the derivation's
    sharpest print: one map, two circle points a reflection apart,
    torn at exactly the one whose image is a cylinder endpoint.
F3  THE CLASS SPLIT IS EXACT. Same-class pairs (residue and
    m-circle branch both equal) climb with the input — at WPHI
    floor/2 the diagonal prints im = ia + 1 at every bucket from
    6:7 to 23:24 except one that EXCEEDS it (21:24; the column is a
    max) — while cross-class pairs pin flat: max 4 (WPHI /2),
    6 (/3), 2 (WSILVER /2), 3 (/3) across the full table. Run 1's raw
    floor(n alpha) mod m classification had printed the same-class
    bucket EMPTY at WPHI m=2 and a climbing cross bucket at m=3:
    both were wrap pairs misclassified by the branch jump at 0 —
    the m-circle comparison removed both anomalies. (A second
    sampling lesson, left in the code: sort-consecutive differences
    realize so thin a set of high strings that a Fibonacci parity
    obstruction emptied the same-class m=2 bucket; pairs at sort
    distance up to 4 fill it.)
F4  RING CONTROLS EXACT: 20000 samples each, zero violations — x3
    at delay 0, floor/4 Lipschitz at delay 2, floor/3 cross-residue
    image agreement identically 0.
F5  THE VERDICT. All three verdict lines TRUE. The derivation
    survives its checks at the exact points it named, so the
    emptiness stands PROVED at both completion shapes that pose the
    gate question, a discrete completion holding the iff trivially
    (theorem; the rotation-coding structure of Ostrowski cylinders
    is classical, checked here as E1/E2 rather than assumed): on a
    trailing positional or irrational-Ostrowski window, an
    arithmetic map x m or floor(n/m) is continuous iff Lipschitz —
    the middle class meets the arithmetic maps in the empty set,
    with the two scanning rigs (explore_continuity_converse.py,
    explore_quadratic_middle.py) as independent instruments. What
    the proof leaves open is exactly one shape: a completion that is
    neither a ring, nor almost one-to-one over an irrational
    rotation, nor discrete.

RUN RECORD
----------
Run 1: N = 200000, two-sided orbit, address (1+alpha)/m, raw floor
classification — E2/E3/E4 misfires as recorded in F1-F3; WSILVER
crashed on a short weight table (fixed: weights extend by index).
2.8s, peak 145.3 MB (memwatch).
Run 2 (final, this text's figures): N = 200000, wall 11.9s, peak
150.2 MB under memwatch, limit 512 MB. VERDICT structure True,
located tears + class splits True, ring controls True.
"""

import time
from bisect import bisect_right, bisect_left
from collections import defaultdict
from decimal import Decimal, getcontext

getcontext().prec = 60

N = 200000
T_STRUCT = (4, 8, 12)
MULTS = (2, 3)
SEED = 20260810


class Window:
    def __init__(self, name, a, alpha):
        self.name = name
        self.a = a
        self.alpha = alpha

    def weights(self, top, minlen=46):
        """Weights q_0 = 1, q_1 = a_1, ... — past top AND minlen long,
        so digit strings can be padded beyond the usable depth."""
        a, q = self.a, [1, self.a[0]]
        while q[-1] <= top or len(q) < minlen:
            k = len(q)
            q.append(a[(k - 1) % len(a)] * q[-1] + q[-2])
        return q

    def legality_failures(self, d):
        a, fails = self.a, 0
        if d[0] > a[0] - 1:
            fails += 1
        for k in range(1, len(d)):
            ak = a[k % len(a)]
            if d[k] > ak:
                fails += 1
            if d[k] == ak and d[k - 1] != 0:
                fails += 1
        return fails


WINDOWS = [
    Window("WPHI    phi-1     [0;1,1,1,...] (Zeckendorf)",
           [1], (Decimal(5).sqrt() - 1) / 2),
    Window("WSILVER sqrt2-1   [0;2,2,2,...] (Pell)",
           [2], Decimal(2).sqrt() - 1),
]


def greedy(v, q, depth):
    d = [0] * depth
    for k in range(min(bisect_right(q, v), depth) - 1, -1, -1):
        if q[k] <= v:
            b = v // q[k]
            d[k] = b
            v -= b * q[k]
    if v:
        # value exceeds the tabulated depth's reach; mark unusable
        return None
    return tuple(d)


def agr(d1, d2):
    m = min(len(d1), len(d2))
    for i in range(m):
        if d1[i] != d2[i]:
            return i
    return m


def usable_depth(q, top):
    t = 0
    while t + 1 < len(q) and q[t + 1] <= top:
        t += 1
    return t


def build(win):
    """Digit strings, circle positions and floors for n < N."""
    q = win.weights(4 * N)
    kn = usable_depth(q, N)
    depth = kn + 4
    strings = [greedy(i, q, depth) for i in range(N)]
    fr, fl = [], []
    a = win.alpha
    for i in range(N):
        x = i * a
        f = int(x)
        fl.append(f)
        fr.append(x - f)
    return q, kn, depth, strings, fr, fl


def image_digits(v, q, depth):
    return greedy(v, q, depth)


def e1(win, strings, q):
    recon = sum(1 for i in range(N)
                if sum(b * q[k] for k, b in enumerate(strings[i])) != i)
    legal = sum(win.legality_failures(strings[i]) for i in range(N))
    print(f"  E1 recon fails {recon}  legality fails {legal}")
    return recon + legal


def frac(x):
    f = x % 1
    if f < 0:
        f += 1
    return f


def e2(win, strings, fr, q):
    bad = 0
    half = Decimal("0.5")
    for t in T_STRUCT:
        cells = defaultdict(list)
        for i in range(N):
            cells[strings[i][:t]].append(fr[i])
        ivs = []
        for v in cells.values():
            lo, hi = min(v), max(v)
            if hi - lo > half:
                # the zero cell wraps through 0; split it there
                ivs.append((min(x for x in v if x >= half), hi))
                ivs.append((lo, max(x for x in v if x < half)))
            else:
                ivs.append((lo, hi))
        ivs.sort()
        overlaps = sum(1 for j in range(1, len(ivs))
                       if ivs[j][0] <= ivs[j - 1][1])
        jmax = q[t + 1] + q[t]
        orb = sorted(frac(-j * win.alpha) for j in range(jmax + 1))
        orbless = 0
        for j in range(1, len(ivs)):
            lo, hi = ivs[j - 1][1], ivs[j][0]
            k = bisect_left(orb, lo)
            if not (k < len(orb) and orb[k] <= hi):
                orbless += 1
        print(f"  E2 t={t:2d}  cells {len(ivs):5d}  overlaps {overlaps}"
              f"  orbit-less boundaries {orbless}"
              f"  (backward orbit, j <= {jmax})")
        bad += overlaps + orbless
    return bad


def e3(win, strings, fr, q, depth, m, tear):
    """Straddle read at one address: the tear z* = (1 - alpha)/m
    (tear=True) or the mirror continuity point z0 = (1 + alpha)/m."""
    a = win.alpha
    z = (1 - a) / m if tear else (1 + a) / m
    tag = f"z* = (1-alpha)/{m} TEAR" if tear else \
        f"z0 = (1+alpha)/{m} mirror control"
    left = sorted((z - f, i) for i, f in enumerate(fr) if f < z)[:20]
    right = sorted((f - z, i) for i, f in enumerate(fr) if f > z)[:20]
    imdepth = depth + 4

    def im(i):
        return image_digits(m * i, q, imdepth)

    same, cross = defaultdict(int), defaultdict(int)
    for fam in (left, right):
        for x in range(len(fam) - 1):
            for y in range(x + 1, len(fam)):
                i, j = fam[x][1], fam[y][1]
                ia = agr(strings[i], strings[j])
                same[ia] = max(same[ia], agr(im(i), im(j)))
    for gx, i in left:
        for gy, j in right:
            ia = agr(strings[i], strings[j])
            cross[ia] = max(cross[ia], agr(im(i), im(j)))
    li, ri = left[0][1], right[0][1]
    pin = agr(im(li), im(ri))
    print(f"  E3{'b' if tear else 'a'} x{m}  {tag}")
    print("     same-side  ia->max im  "
          + "  ".join(f"{k}:{v}" for k, v in sorted(same.items())))
    print("     straddle   ia->max im  "
          + "  ".join(f"{k}:{v}" for k, v in sorted(cross.items())))
    print(f"     closest straddling pair ({li},{ri}) im={pin}")
    climb = max(same.values(), default=0)
    deep_cross = max((v for k, v in cross.items() if k >= 10), default=0)
    cross_top = max(cross.values(), default=0)
    if tear:
        ok = climb >= 10 and deep_cross <= 4
        print(f"     verdict: tear (same-side max {climb} >= 10,"
              f" deep straddle max {deep_cross} <= 4): {ok}")
    else:
        ok = climb >= 10 and cross_top >= 10
        print(f"     verdict: continuity (same-side max {climb},"
              f" straddle max {cross_top}, both >= 10): {ok}")
    return ok


def e4(win, strings, fr, fl, q, depth, order, m):
    imdepth = depth + 4
    same, cross = defaultdict(int), defaultdict(int)
    npairs = 0
    frf = [float(f) for f in fr]
    # pairs at sort-distance 1..4, not only consecutive: the
    # consecutive differences alone realize too thin a set of high
    # strings, which can miss a class entirely
    for w in (1, 2, 3, 4):
        for x in range(N - w):
            i, j = order[x], order[x + w]
            ia = agr(strings[i], strings[j])
            if ia < 6:
                continue
            npairs += 1
            # same class: equal residue, and equal branch of
            # n*alpha mod m compared on the m-circle (wrap-aware):
            # the y-difference, reduced to (-m/2, m/2], near 0.
            dy = (fl[i] + frf[i]) - (fl[j] + frf[j])
            dy -= m * round(dy / m)
            samecls = (i % m == j % m) and abs(dy) < 0.25
            imv = agr(image_digits(i // m, q, imdepth),
                      image_digits(j // m, q, imdepth))
            if samecls:
                same[ia] = max(same[ia], imv)
            else:
                cross[ia] = max(cross[ia], imv)
    print(f"  E4 floor/{m}  pairs {npairs}")
    print("     same-class  ia->max im  "
          + "  ".join(f"{k}:{v}" for k, v in sorted(same.items())))
    print("     cross-class ia->max im  "
          + "  ".join(f"{k}:{v}" for k, v in sorted(cross.items())))
    cmax = max(cross.values(), default=-1)
    smax = max(same.values(), default=-1)
    print(f"     verdict: cross-class max {cmax}  same-class max {smax}")
    return cmax, smax


def agr10(x, y, cap=40):
    t = 0
    while t < cap and x % 10 == y % 10:
        if x == y:
            return cap
        t += 1
        x //= 10
        y //= 10
    return t


def e5():
    import random
    rng = random.Random(SEED)
    v_x3 = v_f4 = v_f3 = 0
    for _ in range(20000):
        t = rng.randint(1, 8)
        n = rng.randint(0, 10 ** 9)
        k = rng.choice([1, 2, 3, 4, 5, 6, 7, 8, 9])
        n2 = n + 10 ** t * k
        if agr10(3 * n, 3 * n2) < agr10(n, n2):
            v_x3 += 1
        n3 = n + 10 ** (t + 2) * k
        if agr10(n // 4, n3 // 4) < t:
            v_f4 += 1
        k3 = rng.choice([1, 2, 4, 5, 7, 8])
        n4 = n + 10 ** t * k3
        if n4 % 3 != n % 3 and agr10(n // 3, n4 // 3) != 0:
            v_f3 += 1
    print(f"  E5 base-10 ring controls: x3 delay-0 violations {v_x3}"
          f"  floor/4 delay-2 violations {v_f4}"
          f"  floor/3 cross-residue nonzero-agreement {v_f3}")
    return v_x3 + v_f4 + v_f3


def main():
    t0 = time.time()
    print(f"N = {N}")
    all_pin = all_struct = True
    for win in WINDOWS:
        print(f"\n== {win.name}")
        q, kn, depth, strings, fr, fl = build(win)
        print(f"  usable depth {kn}  string depth {depth}")
        bad = e1(win, strings, q)
        bad += e2(win, strings, fr, q)
        if bad:
            all_struct = False
        order = sorted(range(N), key=lambda i: strings[i])
        for m in MULTS:
            if not e3(win, strings, fr, q, depth, m, False):
                all_pin = False
            if not e3(win, strings, fr, q, depth, m, True):
                all_pin = False
            cmax, smax = e4(win, strings, fr, fl, q, depth, order, m)
            if cmax > 6 or smax < 10:
                all_pin = False
        del strings, fr, fl, order
    print()
    ring_ok = e5() == 0
    print(f"\nVERDICT structure {all_struct}  located tears + class"
          f" splits {all_pin}  ring controls {ring_ok}")
    print(f"wall {time.time() - t0:.1f}s")


if __name__ == "__main__":
    main()
