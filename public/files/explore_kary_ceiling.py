"""explore_kary_ceiling.py -- THE K-ARY CEILING: the ceiling proper for
the k-ary archimedean magnitude read Y = floor(kx/N) (the sign bit's
k-ary parent; sibling of explore_ceiling_anatomy.py, whose dial
vocabulary this file extends, and of explore_ruler_setvalued.py, whose
block machinery it inherits -- the index convention below is re-derived
from that file's hand derivation, not recalled).

THE QUESTION. The set-valued read opened the k-ary magnitude class as an
observable -- posterior closed form, Sturmian block law, k | c flat cell
-- but never priced it as an EVAL: what is the Bayes-optimal expected
0-1 score of guessing Y from the residue r = x mod M, its floor with the
evidence severed, the dial naming the dead cells, a tight achiever, and
what the geometric tilt theta^x does to all of it? The threshold family's
tilted law is one sliding fiber window at Q* = log_q((1+q^c)/2), dead
exactly at the resonant tilts where Q* is an integer. Does that law
generalize to k labels, and what replaces Q*?

SETUP (the corpus's standing frame). x uniform-or-tilted on {0..N-1},
N = cM, read modulus M (a proper CRT channel subset), unknown cofactor
c. Evidence: r = x mod M, fiber {r + jM : j = 0..c-1}, bijective in
(r, j). Label: Y = floor(kx/N), k >= 2. Prior P(x) proportional to
theta^x; q := theta^M; uniform is theta = 1. Write c = ak + b,
0 <= b < k.

HAND DERIVATION (frozen before the engine; every step below is a
prediction the engine confirms or kills).

1. BLOCKS. Y is nondecreasing in j at fixed r, so class y occupies a
   contiguous block [lo_y, lo_{y+1}) of fiber indices, lo_0 = 0,
   lo_k = c. With f := r/M, the block lengths are
       n_y = a + ceil((y+1)b/k - f) - ceil(yb/k - f),
   two values a and a+1 only, exactly b heavy (a+1) classes per atom,
   and the heavy set is {floor(k(m+f)/b) : m = 0..b-1} -- a Sturmian
   word of density b/k at phase f. The FIRST heavy class is
       y1(r) = floor(kf/b) = floor(kr/(bM)),
   class 0 being heavy iff y1 = 0.

2. MASSES ARE SUCCESSIVE DIFFERENCES. Since the blocks partition the
   fiber, the unnormalized class mass at tilt q is
       m_y = q^{lo_y} - q^{lo_{y+1}},
   successive differences of the convex function q^t at the block
   boundaries. That convexity is the whole tilted anatomy:
   - q < 1: among light classes, class 0's mass (1 - q^a, when light)
     beats every other light class; among heavy classes the FIRST heavy
     beats the rest. So the per-atom argmax is in {0, y1(r)} at every
     q < 1.
   - q > 1: the mirror x <-> N-1-x maps (r, q) to (M-1-r, 1/q) and
     reverses classes, so the argmax is in {last heavy, k-1}.
   - q = 1: all b heavy classes tie at (a+1)/c.
   At most FOUR classes are ever Bayes-optimal at an atom, across the
   entire tilt family.

3. THE UNIFORM CEILING AND ITS DIAL. At q = 1 the per-atom maximum is
   ceil(c/k)/c at EVERY atom (b >= 1 gives (a+1)/c; b = 0 gives a/c =
   1/k), so
       ceiling = ceil(c/k)/c,        floor = ceil(N/k)/N
   (the floor's x-space blocks have lengths floor(N/k)/ceil(N/k) with
   phase 0, so class 0 is heavy there and attains ceil(N/k)).
   Dead (ceiling = floor) iff M*ceil(c/k) = ceil(Mc/k), which unpacks
   to b = 0 OR M(k-b) < k. The second branch -- SATURATION -- is
   equivalent to k(M-1) < bM, i.e. y1(r) = 0 at every atom: the class
   partition is so fine against the read modulus that class 0 is heavy
   everywhere and the evidence never moves the guess. Saturation
   requires k > M; for k <= M the dial is divisibility alone, and at
   k = 2 it is exactly the parity dial (b = 0 iff c even; saturation
   impossible), so the sign bit's anatomy is the k = 2 row of this one.

4. THE ACHIEVER. Guess Y = floor(kr/(bM)) -- the first heavy class,
   one multiplication and one division on the reconstructed residue.
   Under the uniform prior it sits on a heavy block at every atom, so
   it attains ceil(c/k)/c exactly. (b = 0: any class attains 1/k.)

5. THE TILTED DIAL: A DEATH BAND REPLACES THE RESONANCE POINTS. For
   q < 1 the marginal (floor) guess is class 0 (heavy at phase 0). An
   atom with y1(r) >= 1 disagrees with it iff the first heavy's mass
   beats class 0's:
       g(q) := (1 - q^a) - q^L (1 - q^{a+1}) < 0,   L := a*y1(r).
   g(1) = 0, g'(1) = 1 > 0, and Descartes on
   q^{L+a+1} - q^L - q^a + 1 (sign pattern + - - +, two changes, one
   root spent at 1) leaves EXACTLY ONE root qhat(r) in (0, 1): the atom
   disagrees iff q > qhat(r). So the eval is dead iff q <= min_r
   qhat(r) =: qmin -- dead on the entire ray (0, qmin], alive on
   (qmin, 1), and by the mirror alive exactly on the OPEN BAND
       (qmin, 1/qmin),
   symmetric because the atom set is closed under r <-> M-1-r. The
   threshold family's isolated resonant tilts are replaced by a band
   with algebraic edges.

6. THE EDGE IS A RESONANCE ROOT. qhat grows with L, so qmin sits at the
   smallest positive y1, and whenever M > k an atom with y1 = 1 exists
   (the phase interval [b/k, 2b/k) has length >= 1/M), giving L = a and
       g = 0  <=>  q^{2a+1} - 2q^a + 1 = 0,
   which is the resonance polynomial q^c' - 2q^B + 1 at
   (B, c') = (a, 2a+1) -- the sign bit's odd-c death boundary
   2q^m = 1 + q^c IS this law's k = 2 member (a = m = (c-1)/2,
   2a+1 = c). So for every cell with a >= 1, b >= 1, M > k the band
   edge is the SAME algebraic number rho_a, depending on a = floor(c/k)
   alone -- not on k, b, M, or the atom structure -- and rho_1 is the
   reciprocal golden ratio (q^3 - 2q + 1 = (q-1)(q^2+q-1)).

7. THE TRICHOTOMY. Every cell (M, c, k) falls in exactly one class:
   - DEAD EVERYWHERE: b = 0 or saturation -- ceiling = floor at every
     tilt (b = 0: every block has length a at every atom, masses
     q^{ya}(1-q^a), ceiling telescopes to the floor exactly;
     saturation: every atom agrees with the marginal guess at every q).
   - THE BAND: a >= 1, b >= 1, not saturated -- alive exactly on
     (qmin, 1/qmin).
   - ALWAYS ALIVE: a = 0 (k > c), not saturated -- some atom's class 0
     block is EMPTY (mass zero), so that atom disagrees with the
     marginal guess at every tilt: no death band at all.

TRANSPLANT FLAGS (imported intuitions, marked as such). (i) "The sign bit dies at
every scanned tilt" is a scan record at tilts far from uniform; the
band law predicts the sign bit ALIVE at any q strictly inside
(rho_m, 1/rho_m) -- the derivation contradicts the scan's easy reading
and the engine must arbitrate. (ii) The band-edge-is-a-resonance-root
step imports the resonance polynomial from the threshold family one
storey up; it is confirmed only if the y1 = 1 reduction holds exactly.

PREDICTIONS, fixed before the engine.
  P1 Per-atom block lengths are {a, a+1} with exactly b heavies at
     every atom of every cell; the closed-form n_y and the heavy-set
     formula match direct counts; uniform per-atom max = ceil(c/k)/c.
  P2 Uniform dead cells are exactly M*ceil(c/k) = ceil(Mc/k), and that
     condition is equivalent to (b = 0 or M(k-b) < k).
  P3 The achiever floor(kr/(bM)) lands on a heavy class at every atom
     of every b >= 1 cell.
  P4 b = 0 cells: ceiling = floor EXACTLY at every tilt on the grid.
  P5 At every scanned tilt, every atom's argmax set is within
     {0, y1(r)} for q < 1 and {last heavy, k-1} for q > 1.
  P6 Per atom with y1 >= 1, g has exactly one sign change in (0, 1);
     cells with a >= 1, b >= 1, unsaturated are EXACTLY dead at a
     rational tilt below every crossing and alive at one inside the
     band (exact Fractions, both sides).
  P7 M > k forces min positive y1 = 1, so the edge polynomial is
     q^{2a+1} - 2q^a + 1; at a = 1 the numeric edge is the reciprocal
     golden ratio.
  P8 Saturated and a = 0 unsaturated cells behave per the trichotomy
     at every scanned tilt (dead everywhere / alive everywhere).

KILL-SHAPES (observables, not inferences): any atom printing a block
multiset off {a, a+1} or a heavy count off b; a uniform per-atom max
off ceil(c/k)/c; the dead-cell equivalence failing at any grid cell;
an argmax outside the four-class set at any scanned tilt; a g sign
count other than one at a y1 >= 1 atom; an exact ceiling/floor verdict
disagreeing with the band prediction on either side; min positive y1
> 1 at any M > k cell.

CONTROLS (asserted before any result is read).
  K0 POSITIVE CONTROL, known values reproduced: the sign-bit cell
     (M=15, c=7, k=2) must print uniform ceiling 4/7 = (c+1)/2c, the
     anatomy's proved parity-dial value; the hand-checked saturation
     cell (M=2, c=3, k=5) must print ceiling = floor = 1/3 (worked by
     hand in the slate: fibers {0,2,4} -> Y {0,1,3} and {1,3,5} ->
     Y {0,2,4}, every class mass 1/3).
  K1 TRUTH CONTROL: closed-form n_y == direct fiber count at every
     atom, and per-atom masses sum to the fiber mass (exact Fractions).
  K2 MIRROR CONTROL: blocks at (M-1-r) are the class-reversed blocks
     at r; exact ceiling and floor are invariant under theta <-> 1/theta.

DESIGN. Uniform grid: M in {2, 3, 6, 15, 35}, c in 2..12, k in 2..9
(k <= N), exact integers. Tilt grid: M in {2, 3, 6, 15}, c in 2..10,
k in 2..6, theta in {1/5, 1/2, 4/5, 9/10, 199/200, 201/200, 10/9, 2, 5},
exact Fractions. Band test: every a >= 1, b >= 1 unsaturated tilt-grid
cell -- per-atom crossings bracketed in float, then one rational tilt
below the band and one inside verified in exact arithmetic, with the
placement itself certified exactly by g's sign at every atom before the
verdict is read.

RESOURCE ENVELOPE. Pure Python ints and Fractions, no numpy, no BLAS.
Peak state is one cell's Fraction table; estimated wall well under two
minutes, far under the 512MB default.

RUN RECORD (post-run edit; printed output copied, the slate above
frozen -- where the engine killed a slate step, the correction is HERE
and the frozen text stands as written).

Run: ALL CHECKS PASS, 44,191 checks, wall 1.0 s (the placement
certificates below entered after a first green run of 43,855 checks). K0 controls first
(sign-bit cell 4/7 and floor 53/105; hand-worked saturation cell
ceiling = floor = 1/3). Uniform grid 428 cells, 144 dead of which 44
are the saturation cells beyond k | c. Tilt grid 1,602 exact
(cell, theta) evaluations. Dead-set law verified exactly at 109 live
cells and 17 saturation cells, each side's sample tilt carrying an
exact placement certificate (g's sign at every disagreeing atom in
Fractions) before its ceiling/floor verdict is read. Band edges
printed: rho_1 = 0.618034
(reciprocal golden), rho_2 = 0.848375, rho_3 = 0.920568,
rho_4 = 0.951425, rho_5 = 0.967305, rho_6 = 0.976518. Sign-bit
arbitration: (M=15, c=3) exactly ALIVE at theta = 199/200
(q ~ 0.928, inside the band) and exactly DEAD at theta = 24/25
(q ~ 0.542, below it) -- transplant flag (i) resolved AGAINST the
scan's easy reading: the sign bit's every-scanned-tilt death was the
outside of a narrow live band around uniform.

TWO SLATE STEPS KILLED BY THE ENGINE, both traced to one root cause:
Y = floor(kx/N) is a FLOOR partition and is NOT mirror-symmetric --
x <-> N-1-x maps it to the ceiling-based partition, not to itself
(counterexample from the failed control: M=2, c=2, k=3 has atom words
[1,1,0] and [1,0,1], not reversals). So control K2 was refuted AS
STATED and was replaced by a direct analysis of the q > 1 side, and
step 7's saturation clause ("dead at every tilt") is FALSE: worked
counterexample M=2, c=3, k=5 at theta = 2 has ceiling 48/63 > floor
32/63. What survives is stronger and asymmetric -- THE DEAD-SET LAW,
now engine-verified exactly at every b >= 1 cell of the tilt grid:

    dead set = (0, q_lo] u [q_up, infinity),
    q_lo = min lower crossing over atoms with y1 >= 1
           (1 if none, i.e. saturation; 0 if a = 0, class 0 empty),
    q_up = max upper crossing 1/root(g at L' = a(k-1-y_last))
           over atoms with light top class -- the atom r = 0 always
           has a light top class, mirror of class 0 heavy at phase 0
           -- and infinite iff a = 0 (a top-EMPTY atom exists and
           disagrees at every q > 1).

  Read as one law: every b >= 1 cell is alive exactly on the ONE OPEN
  ARC (q_lo, q_up) and dead on the two rays outside it, and b = 0
  cells have q_lo = q_up = 1 (empty arc, dead everywhere). Saturation
  cells have q_lo = 1: uniform-dead but revived by ANY sufficiently
  small upward tilt (they lean on the floor asymmetry: class 0 heavy
  everywhere kills the downward side, the light top class keeps the
  upward side alive) -- and at a >= 1 they die AGAIN from q_up on;
  only a = 0 saturation is dead exactly on (0, 1], its q_up being
  infinite. a = 0 unsaturated cells are alive at every tilt (q_lo = 0,
  q_up infinite). At M > k the arc is the SYMMETRIC band
  (rho_a, 1/rho_a) -- both P7 asserts held: min positive y1 = 1 on
  the lower side AND min positive y1' = 1 on the upper side, so the
  lower edge is the (a, 2a+1) resonance root and the upper its
  reciprocal, which by the locus's own reflection is the (a+1, 2a+1)
  member. The five cells with min positive y1 > 1 all have M < k, as
  predicted: (2,5,4), (2,6,5), (2,7,6), (2,9,4), (3,7,6).

WHAT REPLACES Q*, in one sentence: the threshold family's sliding
window with isolated resonant deaths is replaced by a LIVE ARC of
tilts with algebraic endpoints -- the per-atom argmax staircase
0 -> first heavy -> (all heavies tie at uniform) -> last heavy -> k-1
crosses at single roots of the resonance-shaped polynomial
q^{L+a+1} - q^L - q^a + 1 (the upper handovers at reciprocals of such
roots), and the arc's endpoints at M > k depend on a = floor(c/k)
ALONE, reciprocal-golden at a = 1. One scope the slate's step 2
overstates: "at most FOUR classes ... across the entire tilt family"
holds OFF UNIFORM; at the uniform point itself every heavy class ties,
so an atom with b >= 3 heavies has more than four optimal classes
once q = 1 is counted in.

THE STURMIAN WATCH, answered: the dial is Sturmian (two block lengths,
density b/k, phase r/M) but no Ostrowski/three-distance vocabulary is
needed anywhere -- the first-heavy-class closed form floor(kr/(bM))
resolves every question the ceiling asks at this level. The suspected
stitch to the quadratic storeys did not materialize.
"""

import math
import sys
import time
from fractions import Fraction


def blocks_direct(M, c, k, r):
    """Class of each fiber index by definition; returns lo[0..k]."""
    N = c * M
    counts = [0] * k
    for j in range(c):
        counts[(k * (r + j * M)) // N] += 1
    lo = [0] * (k + 1)
    for y in range(k):
        lo[y + 1] = lo[y] + counts[y]
    # contiguity: Y nondecreasing in j
    ys = [(k * (r + j * M)) // N for j in range(c)]
    assert ys == sorted(ys)
    return lo


def blocks_closed(M, c, k, r):
    """Closed-form block lengths from the Sturmian formula."""
    a, b = divmod(c, k)
    f = Fraction(r, M)
    n = [a + math.ceil((y + 1) * Fraction(b, k) - f)
         - math.ceil(y * Fraction(b, k) - f) for y in range(k)]
    lo = [0] * (k + 1)
    for y in range(k):
        lo[y + 1] = lo[y] + n[y]
    return lo


def heavy_set_closed(M, c, k, r):
    a, b = divmod(c, k)
    f = Fraction(r, M)
    return {math.floor(k * (m + f) / Fraction(b)) for m in range(b)}


def marginal_blocks(N, k):
    """x-space class boundaries Lo[0..k]."""
    return [math.ceil(Fraction(y * N, k)) for y in range(k + 1)]


def cell_values(M, c, k, theta):
    """Exact (ceiling, floor, per-atom argmax sets) at tilt theta.
    Values share the normalizer Z = sum theta^x, left off both."""
    N = c * M
    q = theta ** M
    S_ceil = Fraction(0)
    marg = [Fraction(0)] * k
    argmax_sets = []
    for r in range(M):
        lo = blocks_direct(M, c, k, r)
        w = theta ** r
        if q == 1:
            masses = [Fraction(lo[y + 1] - lo[y]) for y in range(k)]
        else:
            masses = [w * (q ** lo[y] - q ** lo[y + 1]) / (1 - q)
                      for y in range(k)]
        mx = max(masses)
        S_ceil += mx
        for y in range(k):
            marg[y] += masses[y]
        argmax_sets.append({y for y in range(k) if masses[y] == mx})
    S_floor = max(marg)
    marg_arg = {y for y in range(k) if marg[y] == S_floor}
    return S_ceil, S_floor, argmax_sets, marg_arg


def g_poly(a, L, q):
    """Class-0 minus first-heavy unnormalized mass at tilt q (class 0
    light, length a; first heavy at lo = L, length a+1)."""
    return (1 - q ** a) - q ** L * (1 - q ** (a + 1))


CHECKS = 0


def ok(cond, msg):
    global CHECKS
    assert cond, msg
    CHECKS += 1


def main():
    t0 = time.time()
    UM = [2, 3, 6, 15, 35]
    TM = [2, 3, 6, 15]
    THETAS = [Fraction(1, 5), Fraction(1, 2), Fraction(4, 5),
              Fraction(9, 10), Fraction(199, 200), Fraction(201, 200),
              Fraction(10, 9), Fraction(2), Fraction(5)]

    # ---- K0 positive controls ----
    Sc, Sf, _, _ = cell_values(15, 7, 2, Fraction(1))
    Z = Fraction(7 * 15)
    ok(Sc / Z == Fraction(4, 7), "K0 sign-bit ceiling")
    ok(Sf / Z == Fraction(53, 105), "K0 sign-bit floor ceil(105/2)/105")
    Sc, Sf, _, _ = cell_values(2, 3, 5, Fraction(1))
    ok(Sc / 6 == Fraction(1, 3) and Sf / 6 == Fraction(1, 3),
       "K0 saturation cell by hand")
    print("K0 positive controls pass: sign-bit 4/7, saturation 1/3")

    # ---- uniform grid: P1 P2 P3, K1 ----
    n_cells = n_dead = n_sat = 0
    for M in UM:
        for c in range(2, 13):
            N = c * M
            for k in range(2, 10):
                if k > N:
                    continue
                a, b = divmod(c, k)
                n_cells += 1
                per_atom_max = None
                for r in range(M):
                    lo_d = blocks_direct(M, c, k, r)
                    ok(lo_d == blocks_closed(M, c, k, r), "K1 n_y closed form")
                    n = [lo_d[y + 1] - lo_d[y] for y in range(k)]
                    ok(set(n) <= {a, a + 1}, "P1 lengths")
                    heav = {y for y in range(k) if n[y] == a + 1}
                    ok(len(heav) == b, "P1 heavy count")
                    if b >= 1:
                        ok(heav == heavy_set_closed(M, c, k, r), "P1 heavy set")
                        y1 = (k * r) // (b * M)
                        ok(y1 in heav and min(heav) == y1, "P3 achiever first-heavy")
                    m = max(n)
                    ok(Fraction(m, c) == Fraction(math.ceil(Fraction(c, k)), c),
                       "P1 per-atom max")
                    per_atom_max = m
                ceil_u = Fraction(per_atom_max, c)
                Lo = marginal_blocks(N, k)
                ok(Lo == [math.ceil(Fraction(y * N, k)) for y in range(k + 1)]
                   and Lo[-1] == N, "marginal blocks")
                floor_u = Fraction(max(Lo[y + 1] - Lo[y] for y in range(k)), N)
                ok(floor_u == Fraction(math.ceil(Fraction(N, k)), N), "floor form")
                dead = (ceil_u == floor_u)
                cond = (M * math.ceil(Fraction(c, k))
                        == math.ceil(Fraction(M * c, k)))
                branch = (b == 0 or M * (k - b) < k)
                ok(dead == cond == branch, "P2 dial equivalence")
                if dead:
                    n_dead += 1
                if b >= 1 and M * (k - b) < k:
                    n_sat += 1
                    ok(all((k * r) // (b * M) == 0 for r in range(M)),
                       "saturation = y1 zero everywhere")
    print("uniform grid: %d cells, %d dead (%d saturation, beyond k|c)"
          % (n_cells, n_dead, n_sat))

    # ---- tilt grid: P4 P5 P8, K1 K2 ----
    n_tilt = 0
    for M in TM:
        for c in range(2, 11):
            N = c * M
            for k in range(2, 7):
                if k > N:
                    continue
                a, b = divmod(c, k)
                sat = (b >= 1 and M * (k - b) < k)
                for theta in THETAS:
                    q = theta ** M
                    Sc, Sf, arg, _ = cell_values(M, c, k, theta)
                    n_tilt += 1
                    # K1 masses sum to fiber mass (exact)
                    tot = sum(theta ** x for x in range(N))
                    ok(sum((theta ** r) * (q ** 0 - q ** c) / (1 - q)
                           for r in range(M)) == tot, "K1 fiber mass")
                    ok(Sc >= Sf, "ceiling >= floor")
                    if b == 0:
                        ok(Sc == Sf, "P4 divisibility dead at tilt")
                    if b >= 1:
                        for r in range(M):
                            y1 = (k * r) // (b * M)
                            lo = blocks_direct(M, c, k, r)
                            heav = {y for y in range(k)
                                    if lo[y + 1] - lo[y] == a + 1}
                            if q < 1:
                                ok(arg[r] <= {0, y1}, "P5 argmax q<1")
                            elif q > 1:
                                ok(arg[r] <= {max(heav), k - 1}, "P5 argmax q>1")
                    if sat and q < 1:
                        ok(Sc == Sf, "saturation dead below uniform")
                    if a == 0 and not sat:
                        ok(Sc > Sf, "P8 a=0 unsaturated alive at tilt")
    print("tilt grid: %d (cell, theta) evaluations pass" % n_tilt)

    # ---- the dead set: P6 P7, both sides ----
    # For every b >= 1 cell the dead set is (0, q_lo] u [q_up, inf):
    #   q_lo = min lower crossing over atoms with y1 >= 1 (1 if none --
    #          saturation; 0 if a = 0 and such an atom exists, its class
    #          0 being EMPTY);
    #   q_up = max upper crossing over atoms whose top class is light
    #          (the atom r = 0 always qualifies), the upper crossing
    #          being 1/root of g at L' = a*(k-1-y_last); infinite iff
    #          a = 0 (a top-EMPTY atom disagrees at every q > 1).
    def one_root(a, L):
        """The single root of g in (0,1), float bisection; asserts the
        sign-change count on a fine grid first."""
        changes = 0
        prev = 1.0  # g(0+) = 1
        for i in range(1, 4000):
            qf = i / 4000.0
            val = (1 - qf ** a) - qf ** L * (1 - qf ** (a + 1))
            if val == 0.0:
                continue
            if (prev > 0) != (val > 0):
                changes += 1
            prev = val
        ok(changes == 1, "P6 one crossing per disagreeing atom")
        loq, hiq = 0.0, 1.0 - 1e-12
        for _ in range(60):
            mid = (loq + hiq) / 2
            if (1 - mid ** a) - mid ** L * (1 - mid ** (a + 1)) > 0:
                loq = mid
            else:
                hiq = mid
        return (loq + hiq) / 2

    def rat_theta(q_target, M, direction):
        """Rational theta with theta^M near q_target, stepped in the
        safe direction (-1 below, +1 above)."""
        th = q_target ** (1.0 / M)
        return Fraction(int(th * 10 ** 6) + direction * 2, 10 ** 6)

    n_band = n_sat_band = 0
    y1min_gt1 = []
    for M in TM:
        for c in range(2, 11):
            for k in range(2, 7):
                if k > c * M:
                    continue
                a, b = divmod(c, k)
                if b == 0:
                    continue
                sat = (M * (k - b) < k)
                y1s = sorted({(k * r) // (b * M) for r in range(M)} - {0})
                # upper-side data: per atom, last heavy and top lightness
                ups = []
                top_empty = False
                for r in range(M):
                    lo = blocks_direct(M, c, k, r)
                    n = [lo[y + 1] - lo[y] for y in range(k)]
                    heav = [y for y in range(k) if n[y] == a + 1]
                    y_last = max(heav)
                    if n[k - 1] == a:  # top class light
                        if a == 0:
                            top_empty = True
                        else:
                            ups.append(k - 1 - y_last)
                ok((blocks_direct(M, c, k, 0)[k]
                    - blocks_direct(M, c, k, 0)[k - 1]) == a,
                   "atom 0 top class light")
                if sat:
                    ok(y1s == [], "saturation = no disagreeing atom below")
                else:
                    ok(len(y1s) >= 1, "unsaturated has a disagreeing atom")
                if M > k:
                    ok(y1s[0] == 1, "P7 min positive y1 = 1 at M > k")
                    ok(min(ups) == 1 if a >= 1 else top_empty,
                       "P7 min positive y1' = 1 at M > k")
                elif not sat and y1s and y1s[0] > 1:
                    y1min_gt1.append((M, c, k, y1s[0]))
                # lower side (only a >= 1 unsaturated has an edge in (0,1))
                if a >= 1 and not sat:
                    q_lo = min(one_root(a, a * y1) for y1 in y1s)
                    th = rat_theta(q_lo * 0.97, M, -1)
                    ok(all(g_poly(a, a * y1, th ** M) > 0 for y1 in y1s),
                       "placement certificate: below every lower crossing")
                    Sc, Sf, _, _ = cell_values(M, c, k, th)
                    ok(Sc == Sf, "P6 dead below q_lo")
                    th = rat_theta((q_lo + 1) / 2, M, 0)
                    ok(th < 1 and any(g_poly(a, a * y1, th ** M) < 0
                                      for y1 in y1s),
                       "placement certificate: above some lower crossing")
                    Sc, Sf, _, _ = cell_values(M, c, k, th)
                    ok(Sc > Sf, "P6 alive inside (q_lo, 1)")
                    if M > k:
                        rho = one_root(a, a)
                        ok(abs(q_lo - rho) < 1e-9,
                           "P7 edge is the (a, 2a+1) resonance root")
                if a == 0 and not sat:
                    th = rat_theta(0.02, M, 0)
                    Sc, Sf, _, _ = cell_values(M, c, k, th)
                    ok(Sc > Sf, "a=0 unsaturated alive at tiny q")
                # upper side
                if a >= 1:
                    q_up = max(1.0 / one_root(a, a * u) for u in ups)
                    th = rat_theta(q_up * 1.03, M, 1)
                    ok(all(g_poly(a, a * u, 1 / (th ** M)) > 0 for u in ups),
                       "placement certificate: above every upper crossing")
                    Sc, Sf, _, _ = cell_values(M, c, k, th)
                    ok(Sc == Sf, "P6 dead above q_up")
                    th = rat_theta((1 + q_up) / 2, M, 0)
                    ok(th ** M > 1 and any(g_poly(a, a * u, 1 / (th ** M)) < 0
                                           for u in ups),
                       "placement certificate: below some upper crossing")
                    Sc, Sf, _, _ = cell_values(M, c, k, th)
                    ok(Sc > Sf, "P6 alive inside (1, q_up)")
                    if M > k:
                        rho = one_root(a, a)
                        ok(abs(q_up - 1.0 / rho) < 1e-6 * q_up,
                           "P7 upper edge is 1/rho_a at M > k")
                else:
                    ok(top_empty, "a=0: a top-empty atom exists")
                    th = rat_theta(50.0, M, 0)
                    Sc, Sf, _, _ = cell_values(M, c, k, th)
                    ok(Sc > Sf, "a=0 alive at large q (q_up infinite)")
                if sat:
                    n_sat_band += 1
                else:
                    n_band += 1
    print("dead-set law verified exactly at %d live cells and %d"
          % (n_band, n_sat_band))
    print("  saturation cells (dead (0,1], revived above uniform)")
    print("min positive y1 > 1 cells (all have M < k): %r" % y1min_gt1)

    # ---- the edge family: P7 golden, and the resonance identity ----
    # rho_a = root in (0,1) of q^(2a+1) - 2 q^a + 1
    edges = []
    for a in range(1, 7):
        loq, hiq = 0.0, 1.0 - 1e-9
        for _ in range(80):
            mid = (loq + hiq) / 2
            val = mid ** (2 * a + 1) - 2 * mid ** a + 1
            if val > 0:
                loq = mid
            else:
                hiq = mid
        edges.append((a, (loq + hiq) / 2))
    golden = (5 ** 0.5 - 1) / 2
    ok(abs(edges[0][1] - golden) < 1e-9, "P7 golden edge at a = 1")
    # coefficient identity with the resonance polynomial at (B, c') =
    # (a, 2a+1): q^{L+a+1} - q^L - q^a + 1 at L = a IS q^{2a+1} - 2q^a + 1
    for a in range(1, 7):
        lhs = {2 * a + 1: 1, a: -2, 0: 1}
        rhs = {(a) + a + 1: 1}
        rhs[a] = rhs.get(a, 0) - 1
        rhs[a] = rhs.get(a, 0) - 1
        rhs[0] = rhs.get(0, 0) + 1
        ok(lhs == rhs, "P7 resonance-member identity")
    print("band edges rho_a (root of q^(2a+1) - 2q^a + 1):")
    for a, rho in edges:
        print("  a = %d   rho = %.6f   band (%.4f, %.4f)"
              % (a, rho, rho, 1 / rho))

    # ---- the sign bit inside its band: the transplant arbitrated ----
    # (M=15, c=3, k=2): a = 1, edge = 1/phi ~ 0.618, in q. theta with
    # q inside: theta = 199/200 -> q ~ 0.928 > 0.618: ALIVE.
    th = Fraction(199, 200)
    Sc, Sf, _, _ = cell_values(15, 3, 2, th)
    ok(Sc > Sf, "sign bit alive strictly inside its band")
    # theta with q below: theta = 24/25 -> q = (24/25)^15 ~ 0.542: DEAD.
    th = Fraction(24, 25)
    Sc, Sf, _, _ = cell_values(15, 3, 2, th)
    ok(Sc == Sf, "sign bit dead below the boundary (the scanned regime)")
    print("sign bit (M=15, c=3): alive at q~0.928, dead at q~0.542 -- the")
    print("  scan's every-tilt death was the outside of a narrow live band")

    print("ALL CHECKS PASS: %d checks, wall %.1f s" % (CHECKS, time.time() - t0))


if __name__ == "__main__":
    sys.exit(main())
