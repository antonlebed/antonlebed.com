"""
The ring CA chart (building on an earlier shader-CA seed):
what replaces Conway's threshold ring-natively?

Setting: cells hold values in a tower ring R = Z/N (squarefree, k
channels); a CA rule is F: R^n -> R over a neighborhood of size n.
Conway's Life rule is a THRESHOLD ON A COUNT of alive neighbors -- a
comparison, i.e. a wall op. The n-variable locality criterion
(channel-local = compatible = polynomial on squarefree
rings, verbatim for n variables) settles what pure ring ops can do,
and the charts below measure the rest.

PREDICTIONS (stated before the run; adjudication
recorded per item after the run -- PR1-PR5 landed, PR6's parity law
landed exact while its rate model missed low, and the run surfaced
one unpredicted finding, THE FREEZE, below):
 PR1 (rule, proved by citation + verified): THE DECOUPLING LAW.
     Any rule built from ring ops (+, x, constants -- hence all power
     maps: the pair (diamond/box), every gate_m, the meadow inverse
     x^(lam-1)) is a polynomial, = channel-local, so the CA it
     generates is the DIRECT PRODUCT of k independent mod-p CAs:
     channel p's trajectory is a function of channel p's initial
     plane alone. Even the wall-breaker (the meadow inverse)
     is a power map: it breaks measurement walls INSIDE a
     channel, never the locality wall between channels. (Local =>
     product decomposition holds for any product ring; the
     "= polynomial" leg is squarefree-only, thin boundary Z/4.)
     Verified: exhaustive channel-locality at Z/6, n = 3, all 216
     inputs, over a 3-rule battery (polynomial / diamond-of-sum /
     gate-composite); trajectory channel-invariance at Z/30 on a
     16x16 torus, T = 64, a composite rule using meadow inverse +
     diamond: mod-5 planes of two soups equal mod 5 stay equal at
     every step. LANDED (S1a, S1b).
 PR2 (rule, proved + verified exact): COMPLETENESS. Conversely,
     EVERY k-tuple of arbitrary per-channel rules g_p: F_p^n -> F_p
     is ONE polynomial rule: n-variable Lagrange interpolation per
     channel, coefficients CRT-glued degreewise. So pure-ring CAs on
     Z/N are EXACTLY the products of arbitrary mod-p CAs --
     per-channel thresholds (Conway inside one channel) are FREE;
     only JOINT thresholds cost. Verified: a random per-channel rule
     triple on Z/30, n = 2, reconstructed as one polynomial, exact on
     all 900 inputs. LANDED (S2).
 PR3 (rule, witnesses): THE THRESHOLD IS A CHANNEL QUANTIFIER.
     Ring-valued Conway needs ALIVE(x) as one bit for the whole cell:
     [x != 0] (there-exists flavor) or the graded [supp-count >= t].
     Neither is channel-local: [x=0] differs at 15 = 0 mod 3;
     ALIVE_{g>=2} at Z/30 differs at 25 vs 15 (equal mod 2, outputs
     1 vs 0). No ring polynomial computes either (the locality
     criterion; provenance: any composite modulus -- at one field
     [a=0] is Fermat's 1 - a^(p-1)). LANDED (S3).
 PR4 (observation -> witness): GRADED LIFE COUPLES. Two soups equal
     on the channel-5 plane, differing elsewhere, diverge on the
     channel-5 plane. LANDED at t = 1 (S4): one grade-read is enough.
 PR5 (observation, the risky one): at t = 50 from one soup, the
     decoupled baseline's support planes carry pairwise MI at
     finite-sample floor (< 0.01 bits), graded Life's carry > 5x
     that. LANDED with margin (S5): baseline max pair 0.0015 bits,
     graded-A 0.1627 bits at t=50 (~108x; 0.1784 at t=20) -- two
     decades above the floor. CONFOUND CAUGHT AND CLOSED (S5e): the
     shared-zero soup starts correlated (max pair 0.244 bits at
     t=0, measured -- cells zero in ALL channels at once), so the
     coupled figure alone confounds creation with preservation; from a
     channel-INDEPENDENT soup (initial MI 0.0006, ALIVE density
     matched at 0.22) the coupled rules BUILD correlation where the
     decoupled rule stays at the floor: t=20 MI 0.0264 (A) and
     0.1092 (B) vs 0.0010 decoupled -- creation, and the decoupled
     run doubles as proof that the washout of inherited soup
     correlation is the decoupled norm.
 PR6 (rule + observation): BIRTH INTERFERENCE. Born content = sum of
     the 3 parents, so channel 2's born bit is the PARITY of parents
     carrying channel 2 (deterministic -- the classical channel,
     F_2 = {0,1}); odd channels still a birth when the residues
     interfere. The parity law holds on all 17,528 births (S6a -- an
     arithmetic identity; the check is an implementation-consistency
     check, not an empirical adjudication). The naive uniform-parent
     rate ~ 1/p MISSED LOW: measured stillbirth rates 0.796 / 0.772 /
     0.398 vs 1/p = 0.5 / 0.333 / 0.2 (S6c, inside the stated loose
     bracket). Mechanism hunted to ground (S6d): NOT value-cloning
     (all-3-equal births 1.6%; all-distinct-parent births stillbirth
     at the same rates) and NOT skewed marginals (parent carrier
     fractions 0.56 / 0.85 / 0.94; iid-from-marginal predicts only
     ~1/p: 0.499 / 0.322 / 0.196) -- the elevation is INTER-PARENT
     RESIDUE CORRELATION, >= 1.5x the iid null in every channel, and
     its shape differs by channel: mod-3 consensus excess (0.451 of
     parent triples share a residue class vs 0.162 iid; consensus
     stills mod 3 identically, 3r = 0) vs mod-5 sum-patterned
     correlation (consensus excess NONE, 0.055 vs 0.053 iid, yet 2x
     the iid stillbirth). Lineage makes neighborhoods
     residue-correlated: the CA breeds its own interference.
     Intermediate grades are the BULK regime, not an edge case:
     73.3% of nonzero cells sit at partial support 0 < g < 3 at
     t = 50 (S7).

THE FREEZE (found by the run, mechanism confirmed by hand): rule A's
fade (keep channel p iff >= 2 neighbors carry p) never kills a
well-supported channel, so OVERCROWDING DOES NOT KILL -- in a dense
fully-supported region fade = identity, births don't apply, survive
keeps: dense blobs are fixed points. Graded Life A condenses to a
FROZEN DENSE PHASE: static from t = 36, 70.3% nonzero / 56.0% ALIVE
at t = 300, MI locked at its freeze value (unlike Conway, whose
overcrowd death drives sparse activity). One knob restores the
Conway regime -- variant B fades channel p unless the carrier count
is in {2,3} (under- AND over-support kill, per-channel
Conway-flavored): sparse ash (13.1% nonzero, 4.2% ALIVE -- Conway
soup decays to ~3%), freezes only at t = 188, MI 0.063 bits at
t = 300 (~40x floor). The B-prediction "no global freeze by 300"
MISSED at the record seed -- B froze at 188 -- though B's freeze is
the one seed-dependent trait (S8 sweep: 70 / never / 85); the
decoupled baseline
never goes static through t = 300 (measured: still moving at 300
and NOT period-2 -- the per-channel inheritance variant keeps
churning where pure Conway soup settles into ash). Ring CA rules
have a density dial where Conway has a point. SEED-ROBUST (S8,
three fresh soups): A always freezes early and dense (t = 22-43,
54-56% alive), B always runs sparse (5-7% alive), the decoupled
run never goes static, coupled MI stays an order above the floor.

THE CHART (the deletion read as dynamics):
 - THE COUPLING TOLL (taxonomy -- a design menu, not a normal-form
   theorem): a cross-channel CA rule is BUILT as free per-channel
   pre-reads (the quantifier ladder: support bits, or richer gate_m
   bits) + ONE cross-channel bit-op (the toll) + free post-mask
   (idempotent masking is in-ring). Priced by bits
   crossing the channel boundary per cell-read: there-exists/for-all
   aliveness (1 bit) < the support grade (log2(k+1) bits) < full
   size/compare (log2 N bits). Content NEVER crosses; only
   quantifier bits do.
 - GRADED LIFE (the demo rule, S4-S7): R = Z/30, Moore-8, 48x48
   torus. g(x) = |supp(x)|, ALIVE = [g >= 2], S = alive-neighbor
   count. Survive: ALIVE and S in {2,3} -> unchanged. Birth: not
   ALIVE and S = 3 -> sum of the 3 alive neighbors (inheritance;
   interference can still it). Else FADE: keep channel p iff the
   carrier count passes (A: >= 2; B: in {2,3}) -- channel-local,
   hence FREE: graded death down the support lattice, light and
   shadow. The toll is isolated: exactly one grade-read per cell
   per step.

Run: python prime/code/explore_ring_ca.py   (~30 s, pure Python,
memory trivial). Checks: 17.
"""

import random
import sys

# ---------------------------------------------------------------- helpers

CHECKS = []


def check(name, cond):
    status = "PASS" if cond else "FAIL"
    print("  [%s] %s" % (status, name))
    CHECKS.append((name, bool(cond)))


def crt3(r2, r3, r5):
    return (15 * r2 + 10 * r3 + 6 * r5) % 30


PRIMES = [2, 3, 5]
N = 30
LAM = 4  # lambda(30) = lcm(1, 2, 4)


def bits(x):
    return tuple(int(x % p != 0) for p in PRIMES)


def grade(x):
    return sum(bits(x))


# ------------------------------------------------- S1a: decoupling at Z/6


def s1a():
    # Rule battery at Z/6 (lambda(6) = 2), n = 3: polynomial /
    # diamond-of-sum / gate-composite (box(a^2) = 1 - (1 - a^2)^2).
    def f_poly(v):
        return (v[0] * v[0] + v[1] * v[2] + 3) % 6

    def f_diamond(v):
        return pow((v[0] + v[1] + v[2]) % 6, 2, 6)

    def f_gate(v):
        g = (1 - pow((1 - pow(v[0], 2, 6)) % 6, 2, 6)) % 6
        return (g * v[1] + v[2]) % 6

    battery = [("poly", f_poly), ("diamond", f_diamond), ("gate", f_gate)]
    all_local = True
    for name, f in battery:
        for p in (2, 3):
            table = {}
            for a in range(6):
                for b in range(6):
                    for c in range(6):
                        key = (a % p, b % p, c % p)
                        val = f((a, b, c)) % p
                        if table.setdefault(key, val) != val:
                            all_local = False
    check("S1a decoupling: 3-rule battery channel-local, exhaustive Z/6 n=3 (216 inputs)", all_local)


# ------------------------------- S1b: trajectory invariance at Z/30


def ringop_rule(cell, nbrs):
    # A composite pure-ring rule: meadow inverse (x^(lam-1)) + diamond
    # (x^lam) + polynomial mixing. Channel-local by the criterion.
    s = sum(nbrs) % 30
    m = (nbrs[0] * nbrs[1]) % 30
    inv = pow((cell + 1) % 30, LAM - 1, 30)
    dia = pow(s, LAM, 30)
    return (cell * cell * dia + pow(s, 3, 30) + inv * m) % 30


def run_ca(grid, steps, step_fn):
    H, W = len(grid), len(grid[0])
    for _ in range(steps):
        new = [[0] * W for _ in range(H)]
        for y in range(H):
            for x in range(W):
                nbrs = [grid[(y + dy) % H][(x + dx) % W]
                        for dy in (-1, 0, 1) for dx in (-1, 0, 1)
                        if (dy, dx) != (0, 0)]
                new[y][x] = step_fn(grid[y][x], nbrs)
        grid = new
        yield grid


def s1b():
    rng = random.Random(951)
    H = W = 16
    a = [[rng.randrange(30) for _ in range(W)] for _ in range(H)]
    # b: same mod-5 plane, channels 2 and 3 re-randomized
    b = [[crt3(rng.randrange(2), rng.randrange(3), a[y][x] % 5)
          for x in range(W)] for y in range(H)]
    ok = all(a[y][x] % 5 == b[y][x] % 5 for y in range(H) for x in range(W))
    it_a = run_ca(a, 64, ringop_rule)
    it_b = run_ca(b, 64, ringop_rule)
    for ga, gb in zip(it_a, it_b):
        if any(ga[y][x] % 5 != gb[y][x] % 5 for y in range(H) for x in range(W)):
            ok = False
            break
    check("S1b decoupling: mod-5 planes equal stay equal, ring-op rule, 16x16 T=64", ok)


# ------------------------------------------------- S2: completeness


def lagrange_2var(table, p):
    # Coefficient matrix c[i][j] of the interpolating polynomial over F_p.
    def basis_1var(a):
        # L_a(X) = prod_{b != a} (X - b) / (a - b) as coefficient list
        coeffs = [1]
        denom = 1
        for b in range(p):
            if b == a:
                continue
            denom = (denom * (a - b)) % p
            new = [0] * (len(coeffs) + 1)
            for i, c in enumerate(coeffs):
                new[i + 1] = (new[i + 1] + c) % p
                new[i] = (new[i] - c * b) % p
            coeffs = new
        dinv = pow(denom, p - 2, p) if p > 2 else denom % p
        return [(c * dinv) % p for c in coeffs]

    Lx = [basis_1var(a) for a in range(p)]
    c = [[0] * p for _ in range(p)]
    for (a, b), val in table.items():
        for i in range(p):
            for j in range(p):
                c[i][j] = (c[i][j] + val * Lx[a][i] * Lx[b][j]) % p
    return c


def s2():
    rng = random.Random(952)
    tables = {p: {(a, b): rng.randrange(p) for a in range(p) for b in range(p)}
              for p in PRIMES}
    # CRT-glue coefficients degreewise into one polynomial over Z/30
    per = {p: lagrange_2var(tables[p], p) for p in PRIMES}
    C = [[0] * 5 for _ in range(5)]
    for i in range(5):
        for j in range(5):
            r = [per[p][i][j] if (i < p and j < p) else 0 for p in PRIMES]
            C[i][j] = crt3(r[0] % 2, r[1] % 3, r[2] % 5)
    ok = True
    for x in range(30):
        for y in range(30):
            v = sum(C[i][j] * pow(x, i, 30) * pow(y, j, 30)
                    for i in range(5) for j in range(5)) % 30
            for p in PRIMES:
                if v % p != tables[p][(x % p, y % p)]:
                    ok = False
    check("S2 completeness: random per-channel rule triple = one polynomial, exact on all 900 inputs", ok)


# --------------------------------------------- S3: quantifier witnesses


def s3():
    # [x = 0] as a function to {0,1} in Z/30: incompatible at (15, 0) mod 3
    f = lambda x: 1 if x == 0 else 0
    w1 = (15 % 3 == 0 % 3) and (f(15) % 3 != f(0) % 3)
    check("S3a [x=0] not channel-local: witness (15, 0) mod 3", w1)
    alive = lambda x: 1 if grade(x) >= 2 else 0
    w2 = (25 % 2 == 15 % 2) and (alive(25) % 2 != alive(15) % 2)
    check("S3b ALIVE (g>=2) not channel-local: witness (25, 15) mod 2", w2)


# ------------------------------------------------- graded Life engine


def fade_a(cnt):
    return cnt >= 2


def fade_b(cnt):
    return cnt in (2, 3)


def step_graded(grid, births=None, fade_keep=fade_a):
    H, W = len(grid), len(grid[0])
    new = [[0] * W for _ in range(H)]
    for y in range(H):
        for x in range(W):
            nbrs = [grid[(y + dy) % H][(x + dx) % W]
                    for dy in (-1, 0, 1) for dx in (-1, 0, 1)
                    if (dy, dx) != (0, 0)]
            cell = grid[y][x]
            alive = grade(cell) >= 2
            live_nbrs = [nb for nb in nbrs if grade(nb) >= 2]
            S = len(live_nbrs)
            if alive and S in (2, 3):
                new[y][x] = cell
            elif (not alive) and S == 3:
                b = sum(live_nbrs) % 30
                new[y][x] = b
                if births is not None:
                    births.append((live_nbrs, b))
            else:
                # FADE (channel-local, free): keep channel p iff the
                # neighborhood carrier count passes fade_keep
                r = []
                for p in PRIMES:
                    cnt = sum(1 for nb in nbrs if nb % p != 0)
                    r.append(cell % p if fade_keep(cnt) else 0)
                new[y][x] = crt3(r[0], r[1], r[2])
    return new


def step_perchannel(grid):
    # The decoupled baseline: per-channel Life with per-channel
    # inheritance -- a rule TUPLE, hence (by S2) one ring polynomial.
    H, W = len(grid), len(grid[0])
    new = [[0] * W for _ in range(H)]
    for y in range(H):
        for x in range(W):
            nbrs = [grid[(y + dy) % H][(x + dx) % W]
                    for dy in (-1, 0, 1) for dx in (-1, 0, 1)
                    if (dy, dx) != (0, 0)]
            cell = grid[y][x]
            r = []
            for p in PRIMES:
                bit = cell % p != 0
                carriers = [nb % p for nb in nbrs if nb % p != 0]
                S = len(carriers)
                if bit and S in (2, 3):
                    r.append(cell % p)
                elif (not bit) and S == 3:
                    r.append(sum(carriers) % p)
                else:
                    r.append(0)
            new[y][x] = crt3(r[0], r[1], r[2])
    return new


def soup(rng, H, W, p_zero=0.7):
    return [[0 if rng.random() < p_zero else rng.randrange(30)
             for _ in range(W)] for _ in range(H)]


def indep_soup(rng, H, W, c=0.31):
    # Channel-INDEPENDENT soup: each channel carries w.p. c with a
    # uniform nonzero residue -- initial support planes uncorrelated
    # (the shared-zero soup above starts at 0.244 bits max-pair MI;
    # this one at the sampling floor). c = 0.31 matches the ALIVE
    # density ~0.22.
    grid = []
    for y in range(H):
        row = []
        for x in range(W):
            r = [rng.randrange(1, p) if rng.random() < c else 0
                 for p in PRIMES]
            row.append(crt3(r[0], r[1], r[2]))
        grid.append(row)
    return grid


def mi_planes(grid, pa, pb):
    from math import log
    H, W = len(grid), len(grid[0])
    n = H * W
    joint = {}
    ma = {0: 0, 1: 0}
    mb = {0: 0, 1: 0}
    for y in range(H):
        for x in range(W):
            a = int(grid[y][x] % pa != 0)
            b = int(grid[y][x] % pb != 0)
            joint[(a, b)] = joint.get((a, b), 0) + 1
            ma[a] += 1
            mb[b] += 1
    mi = 0.0
    for (a, b), c in joint.items():
        if c and ma[a] and mb[b]:
            mi += (c / n) * log(c * n / (ma[a] * mb[b]), 2)
    return mi


def s4():
    rng = random.Random(954)
    H = W = 32
    a = soup(rng, H, W)
    b = [[crt3(rng.randrange(2), rng.randrange(3), a[y][x] % 5)
          for x in range(W)] for y in range(H)]
    t_div = None
    ga, gb = a, b
    for t in range(1, 51):
        ga = step_graded(ga)
        gb = step_graded(gb)
        if any(ga[y][x] % 5 != gb[y][x] % 5 for y in range(H) for x in range(W)):
            t_div = t
            break
    check("S4 coupling witness: equal mod-5 planes diverge under graded Life (t <= 50)", t_div is not None)
    print("        first mod-5 divergence at t = %s" % t_div)


def s5_s6_s7():
    rng = random.Random(955)
    H = W = 48
    g0 = soup(rng, H, W)
    times = (20, 50, 100, 200, 300)
    rec = times + (298, 299)  # 298/299 recorded for the period test only

    def run(step_fn, record_births=False):
        grid = [row[:] for row in g0]
        births = [] if record_births else None
        snaps = {}
        freeze_t = None
        for t in range(1, 301):
            new = step_fn(grid, births) if record_births else step_fn(grid, None)
            if freeze_t is None and new == grid:
                freeze_t = t
            grid = new
            if t in rec:
                snaps[t] = grid
        return snaps, births, freeze_t

    snaps_a, births, freeze_a_t = run(lambda g, b: step_graded(g, b, fade_a), True)
    snaps_b, _, freeze_b_t = run(lambda g, b: step_graded(g, b, fade_b))
    snaps_d, _, freeze_d_t = run(lambda g, b: step_perchannel(g))

    pairs = [(2, 3), (2, 5), (3, 5)]

    def max_mi(grid):
        return max(mi_planes(grid, pa, pb) for pa, pb in pairs)

    def frac_nonzero(grid):
        return sum(1 for row in grid for v in row if v) / (H * W)

    def frac_alive(grid):
        return sum(1 for row in grid for v in row if grade(v) >= 2) / (H * W)

    print("        support-plane MI (max over channel pairs), bits:")
    print("        t=0 (the shared-zero soup, all three runs): %.4f" % max_mi(g0))
    print("        t      decoupled   graded-A    graded-B")
    for t in times:
        print("        %-6d %-11.4f %-11.4f %.4f"
              % (t, max_mi(snaps_d[t]), max_mi(snaps_a[t]), max_mi(snaps_b[t])))
    print("        freeze step (grid static from t): decoupled %s  A %s  B %s"
          % (freeze_d_t, freeze_a_t, freeze_b_t))
    d_moving = snaps_d[300] != snaps_d[299]
    d_period2 = snaps_d[300] == snaps_d[298]
    print("        decoupled at t=300: moving %s, period-2 %s" % (d_moving, d_period2))
    mi_d50, mi_a50 = max_mi(snaps_d[50]), max_mi(snaps_a[50])
    check("S5a decoupled baseline MI at floor (< 0.01 bits, t=50)", mi_d50 < 0.01)
    check("S5b graded Life (A) MI > 5x baseline at t=50", mi_a50 > 5 * mi_d50)

    for name, snaps in (("A", snaps_a), ("B", snaps_b)):
        fg, fa = frac_nonzero(snaps[300]), frac_alive(snaps[300])
        print("        graded-%s t=300: nonzero %.3f  alive %.3f" % (name, fg, fa))
    check("S5c populations live at T=300 (graded-A nonzero > 2%)",
          frac_nonzero(snaps_a[300]) > 0.02)
    check("S5d the freeze: graded-A reaches a fixed point by t=300",
          freeze_a_t is not None)

    # S5e: creation, not inheritance. The shared-zero soup starts
    # correlated (~0.14 bits by construction), so sustained MI there
    # confounds creation with preservation. From a channel-INDEPENDENT
    # soup the coupled rules must BUILD the correlation.
    rng2 = random.Random(957)
    gi = indep_soup(rng2, H, W)
    mi0 = max_mi(gi)
    mi20 = {}
    for name, fn in (("decoupled", lambda g: step_perchannel(g)),
                     ("A", lambda g: step_graded(g, None, fade_a)),
                     ("B", lambda g: step_graded(g, None, fade_b))):
        grid = [row[:] for row in gi]
        for _ in range(20):
            grid = fn(grid)
        mi20[name] = max_mi(grid)
    print("        independent soup: MI t=0 %.4f | t=20 decoupled %.4f  A %.4f  B %.4f"
          % (mi0, mi20["decoupled"], mi20["A"], mi20["B"]))
    check("S5e MI is CREATED from an independent soup (t=20: graded A and B > 10x decoupled; t=0 at floor)",
          mi0 < 0.01 and mi20["decoupled"] < 0.01
          and mi20["A"] > 10 * mi20["decoupled"]
          and mi20["B"] > 10 * mi20["decoupled"])

    # S6: birth parity (channel 2, deterministic) + stillbirth rates
    parity_ok = all((b % 2) == (sum(1 for pa in parents if pa % 2) % 2)
                    for parents, b in births)
    check("S6a channel-2 birth parity law exact on all %d births" % len(births), parity_ok)
    check("S6b enough births to rate (>= 200)", len(births) >= 200)
    print("        stillbirth rate per channel (expected ~ 1/p):")
    rates = []
    for p in PRIMES:
        r = sum(1 for _, b in births if b % p == 0) / len(births)
        rates.append(r)
        print("        p=%d: %.3f (1/p = %.3f)" % (p, r, 1.0 / p))
    ok_rates = all(1 / (3 * p) < r < 3 / p for p, r in zip(PRIMES, rates))
    check("S6c stillbirth rates within (1/3p, 3/p) each channel", ok_rates)
    # Mechanism instrumentation. Two candidates REFUTED by the run:
    # (i) inter-parent VALUE correlation (clones) -- all-3-equal births
    # are 1.6%, and all-distinct-parent births stillbirth at the same
    # rates; (ii) skewed per-channel parent MARGINALS -- carrier
    # fractions are healthy and the iid-from-marginal model predicts
    # only ~1/p. What remains, measured directly: inter-parent RESIDUE
    # correlation -- parent triples reach mod-p consensus far above
    # iid, and consensus interferes (3r = 0 mod 3 identically; parity
    # of equal bits reads the shared bit; 3r = 0 mod 5 iff r = 0).
    all_eq = [ps for ps, _ in births if ps[0] == ps[1] == ps[2]]
    dist = [(ps, b) for ps, b in births if len(set(ps)) == 3]
    print("        parent correlation: all-3-equal %.3f  all-distinct %.3f of births"
          % (len(all_eq) / len(births), len(dist) / len(births)))
    if dist:
        for p in PRIMES:
            r = sum(1 for _, b in dist if b % p == 0) / len(dist)
            print("        p=%d stillbirth among all-distinct-parent births: %.3f" % (p, r))
    print("        iid-from-marginal model vs measured, per channel:")
    gap_ok = True
    for p, measured in zip(PRIMES, rates):
        marg = [0] * p
        for ps, _ in births:
            for pa in ps:
                marg[pa % p] += 1
        tot = sum(marg)
        marg = [m / tot for m in marg]
        pred = sum(marg[r1] * marg[r2] * marg[r3]
                   for r1 in range(p) for r2 in range(p) for r3 in range(p)
                   if (r1 + r2 + r3) % p == 0)
        cons = sum(1 for ps, _ in births
                   if ps[0] % p == ps[1] % p == ps[2] % p) / len(births)
        cons_iid = sum(m ** 3 for m in marg)
        carrier = 1 - marg[0]
        print("        p=%d: carrier %.3f, iid-pred %.3f, measured %.3f | consensus %.3f (iid %.3f)"
              % (p, carrier, pred, measured, cons, cons_iid))
        if measured < 1.5 * pred:
            gap_ok = False
    check("S6d stillbirth elevation is inter-parent correlation: measured >= 1.5x iid-from-marginal, each channel", gap_ok)

    # S7: the graded region is occupied
    nz = [v for row in snaps_a[50] for v in row if v]
    partial = sum(1 for v in nz if 0 < grade(v) < 3) / len(nz)
    print("        t=50: fraction of nonzero cells at partial support: %.3f" % partial)
    check("S7 intermediate grades occupied (> 1% of nonzero cells, t=50)", partial > 0.01)


def s8():
    # Seed robustness of the regime split (three fresh soups): A
    # freezes early and dense, B runs sparse (freeze seed-dependent:
    # 70 / never / 85 across these seeds), decoupled never static,
    # coupled MI an order above the floor.
    def one(g0, fn, T=300):
        grid = [row[:] for row in g0]
        freeze = None
        mi50 = None
        for t in range(1, T + 1):
            new = fn(grid)
            if freeze is None and new == grid:
                freeze = t
            grid = new
            if t == 50:
                mi50 = max(mi_planes(grid, a, b)
                           for a, b in [(2, 3), (2, 5), (3, 5)])
        alive = sum(1 for row in grid for v in row if grade(v) >= 2) / (48 * 48)
        return freeze, mi50, alive

    ok = True
    for seed in (1001, 1002, 1003):
        rng = random.Random(seed)
        g0 = soup(rng, 48, 48)
        fa, mia, aa = one(g0, lambda g: step_graded(g, None, fade_a))
        fb, mib, ab = one(g0, lambda g: step_graded(g, None, fade_b))
        fd, mid, ad = one(g0, lambda g: step_perchannel(g))
        print("        seed %d: A freeze %-4s alive %.3f | B freeze %-4s alive %.3f | d freeze %s | mi50 A %.4f B %.4f d %.4f"
              % (seed, fa, aa, fb, ab, fd, mia, mib, mid))
        if not (fa is not None and fa <= 100 and aa > 0.3
                and ab < 0.15 and fd is None and mia > 10 * mid):
            ok = False
    check("S8 regime split seed-robust (3 soups): A freezes <= 100 dense > 30%, B sparse < 15%, decoupled unfrozen, MI-A > 10x floor", ok)


# ---------------------------------------------------------------- main

if __name__ == "__main__":
    print("=== The ring CA chart: what replaces Conway's threshold? ===")
    print("-- S1: the decoupling law")
    s1a()
    s1b()
    print("-- S2: completeness (per-channel rules = one polynomial)")
    s2()
    print("-- S3: the threshold is a channel quantifier")
    s3()
    print("-- S4: graded Life couples")
    s4()
    print("-- S5-S7: dynamics (48x48, T=300, one soup, three rules)")
    s5_s6_s7()
    print("-- S8: seed robustness")
    s8()
    failed = [n for n, ok in CHECKS if not ok]
    print("=== %d/%d checks pass ===" % (len(CHECKS) - len(failed), len(CHECKS)))
    if failed:
        for n in failed:
            print("FAILED: " + n)
        sys.exit(1)
