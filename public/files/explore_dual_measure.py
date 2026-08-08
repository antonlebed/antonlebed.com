"""The pole's own measure: exact exception densities and Benford as
the dual rung's Haar measure.

THE QUESTION
------------
The dual pole reads the integers only through the size window
W_{b,t}(n) = (sign, exponent, t leading base-b digits); its graded
locality (explore_dual_pole.py) printed multiplication's exception
densities falling geometrically (ratios approximately b) under
COUNTING measure on mantissas at fixed depth, and the locality
classification (explore_dual_locality.py) settled which maps have
density zero. This experiment settles the measure theory: what are
the EXACT closed forms of the exception densities — derivation from
the periodic crossing geometry, never fitting — and in what sense is
log-uniform (Benford) the pole's OWN measure, the Haar measure of
the dual rung, and which laws sharpen when the corpus is re-read
under it? Every density below states its measure.

THE DESIGN
----------
The derivation preceded the engine; each prediction is marked with
its pre-run status. Setup for scalings: f(n) = a*n, a >= 2, base b,
output precision t, lookahead l >= 1 (operand precision t' = t + l),
operand depth j >= 1 (operand exponent e = t' + j - 1). alpha =
floor(log_b a). The output exponent is e + alpha + theta with theta
in {0, 1} (theta = 1 iff the mantissa product carries), so the
output grid spacing is b^J with J - j = l + alpha + theta. A fiber
[m b^j, (m+1) b^j) is exceptional iff a multiple of b^J lies in
(a*lo, a*(hi-1)], an interval of length L = a(b^j - 1); the residue
(-a m b^j) mod b^J = b^j((-a m) mod b^{J-j}) makes the exception
pattern periodic in m with period b^{J-j}, phase-free.

D1 [derived, rule] THE PERIOD LAW: over ANY b^{l+alpha+theta}
    consecutive class-interior fibers at depth j, the number of
    exceptional fibers is EXACTLY

        d * floor( a (b^j - 1) / (b^j d) ),
        d = gcd(a, b^{l+alpha+theta}),

    independent of phase; on deep fibers (b^j d > a) this is a - d.
    Its zero locus is d = a, i.e. rad(a) | rad(b) AND
    l + alpha + theta >= max_p ceil(v_p(a)/v_p(b)) — the radical /
    numerator criterion and the composite depth threshold
    (explore_dual_locality.py) are the vanishing locus of one
    density formula.
D2 [derived, rule] THE COUNTING COLLAPSE: mixing the two carry
    classes with their counting weights (low class
    (b^{alpha+1} - a)/(a(b-1)) of the mantissa range), alpha cancels:
    for a coprime to b the per-exponent exception density under
    counting measure is EXACTLY

        D_count = (1 - 1/a) / b^l

    — the prefactor forgets the base and the multiplier's size,
    keeping only the multiplier's reciprocal; the ratio per unit of
    lookahead is exactly b. The exact per-exponent total is
    (a-1)(b-1) b^{t'-1} / (a b^l) up to an edge term bounded by
    2a + 2 (two partial periods, two class-rounding units, one
    class-straddling fiber).
D3 [derived, rule] THE BENFORD RE-READ (scalings): under log-uniform
    the class weights become 1 - x and x with x = {log_b a} (the
    fractional part), so for a coprime to b, deep fibers:

        D_benford = (1 - 1/a) * R(x) / b^l,
        R(x) = b^{x-1} (1 + (b-1)(1-x)).

    R(0) = R(1) = 1 and R is humped between (max at
    x = 1 + 1/(b-1) - 1/ln b): Benford carries the multiplier's
    mantissa where counting is blind to it, and Benford sees MORE
    exceptions at every base. Reference values: (b=10, a=3, l=1):
    0.1141182 vs counting 1/15; (b=2, a=3, l=1): 0.3537594 vs 1/3;
    (b=2, a=5, l=1): 0.4195180 vs 2/5; (b=10, a=7, l=1): 0.1436471
    vs 3/35.
D4 [derived, rule] THE PAIR CRITERION: for two-operand
    multiplication on same-exponent fibers at precision tp = t + c,
    depth j (the object explore_dual_pole.py CHECK 5 measured), the
    pair (ma, mb) is exceptional iff a multiple of b^J lies in
    (P_min, P_max], P_min = ma mb b^{2j},
    P_max = ((ma+1)b^j - 1)((mb+1)b^j - 1); in residue form, for
    class-interior pairs,

        (-ma mb) mod b^{t+2c-1+theta}  in  [1, floor(L / b^{2j})],
        L = (b^j - 1)((ma + mb + 1) b^j - 1)

    — an exception is a near-miss of the product's low digits to
    the grid, within (ma+mb+1)(1 - b^{-j}) - O(1) of it. O(1)
    arithmetic per pair; must reproduce the sibling's measured
    counts exactly (13/16 = 0.8125 at c=1; 0.0598 at c=5; b=2,
    t=2, depth 4).
D5 [derived, rule-shape] THE PAIR DENSITY LIMITS: as t grows at
    fixed lookahead c and depth j, in the unsaturated regime
    (2 b^{1-c} <= 1):

        counting:  D_pair -> 2 (1 - b^{-j}) / b^c      (base-free)
        Benford:   D_pair -> 2 (1 - b^{-j}) K_b / b^c,
                   K_b = (b-1)^2 / (b ln^2 b)

    (K_2 = 1.040684, K_3 = 1.104714, K_10 = 1.527755). The Benford/
    counting ratio K_b EQUALS the mean of D3's hump R(x) over
    x uniform in [0,1] — two independent derivations of one
    constant. The ratio per unit of c is exactly b under BOTH
    measures; the sibling's printed ratio wobble (1.79-2.09 at
    b=2) is finite-t plus saturation (c=1 sits in the min(1,.)
    regime), not a deviation from the law.
D6 [property; the Haar statement is classical] BENFORD = THE DUAL
    HAAR. The mantissa space of the dual rung is the compact group
    R_{>0} / b^Z (the scale circle); log-uniform is its Haar
    measure, the unique scale-invariant law. THE MIRROR: finite
    pole — ambient Z (additive), rung Z/N, Haar = counting, and the
    reading partition (residue classes) consists of COSETS, every
    cell of equal Haar, which is why no finite-pole density ever
    needed a measure named. Dual pole — ambient R_{>0}
    (multiplicative), rung the scale circle, Haar = log-uniform,
    and the reading partition (digit windows) is NOT a coset
    partition: cell m carries Haar log_b((m+1)/m) — BENFORD'S LAW
    IS THE GRID/HAAR MISMATCH, and that mismatch is why every
    density at this pole is measure-carrying. Exact checks: the
    pushforward of Benford under x -> q x (rational q) returns
    every window's Haar — the preimage is a single arc of the
    circle (at most two chart pieces) whose endpoint ratios
    telescope to (m+1)/m exactly, verifiable in exact rational
    arithmetic with no logarithms; counting measure fails
    invariance exactly (the leading-digit shift under tripling);
    the additive mirror (one uniform summand makes a sum uniform
    on Z/N) holds exactly.
D7 [derived, rule] THE CARRY LINEARIZATION: under the pole's own
    measure the carry structure becomes flat where under counting
    it is base-entangled and log-transcendental:
      (i)  P(scaling carry under *a) = {log_b a} exactly
           (counting: b(a - b^alpha)/(a(b-1)), rational);
      (ii) P(pair mantissa carry) = 1/2 EXACTLY at every base —
           in log coordinates the class boundary uv = 1/b is the
           straight line x + y = -1 and x + y is symmetric-
           triangular about it (counting: 1 - (B ln b - B(1-B))/
           (1-B)^2 with B = 1/b: 0.613706 at b=2, 0.676041 at
           b=3, 0.826841 at b=10).
D8 [audit] THE CORPUS MEASURE AUDIT: every law of the dual corpus
    (explore_dual_pole.py, explore_dual_locality.py) except the
    graded-locality densities is a per-fiber or
    per-window statement (hiding bias, residue wall, equality wall,
    locality criteria, two-ends, depth threshold) — MEASURE-FREE;
    the only measure-carrying statements in the dual corpus are
    the exception densities, now closed-formed under both measures
    (the sibling's F5 gets a settling pointer naming its measure).

Kill criteria, named at the freeze: any class-interior period whose
exact count misses D1's formula (controls green) kills D1; the
sibling's anchor counts failing to reproduce kills D4; the pair
densities converging away from D5's constants — in particular the
Benford/counting ratio missing K_b — kills D5; the rational-arc
telescope failing kills D6's exactness; the pair-carry probability
converging off 1/2 kills D7. Positive controls: full-value sweeps
must equal endpoint verdicts (monotone maps, tiny scales); the
Benford meter must return log_b 2 on the leading-digit-1 mass; the
radical law's exact cases (doubling at base 10) must give count 0
and a rough case (tripling at base 2) count > 0; counting measure
must FAIL the invariance check.

Engine: pure python, exact integers for every count; Benford
weights are float sums of logs (machine-epsilon noise ~1e-12, far
below the b^{-t'} edge terms that drive convergence); exhaustive
enumeration throughout, no sampling. Single process, seconds-scale,
trivial memory.

THE FINDINGS
------------
Verdict: the dual pole's exception densities are a two-line
closed-form theory whose zero set IS the locality classification,
and the pole's own measure is literally the Haar measure of the
scale circle — the mirror is exact at the measure level: rung =
quotient group, Haar = the measure in which the pole's laws are
flattest, and the finite pole's "no measure ever named" is the
degenerate luxury of coset reading partitions. 14813 checks green,
~1 s.

F1 THE PERIOD LAW (rule; exhaustive over 219 scopes): over any
   b^{l+alpha+theta} consecutive class-interior fibers the exact
   exception count is d * floor(a(b^j-1)/(b^j d)),
   d = gcd(a, b^{l+alpha+theta}) — phase-free (3 phases per scope),
   bases 2, 6, 10, coprime/mixed/radical multipliers, lookaheads
   1-3, depths 1, 2, 4, both carry classes; deep (b^j d > a) it is
   a - d. All 48 zero-locus cells coincide with rad(a) | rad(b)
   AND l+alpha+theta >= max_p ceil(v_p(a)/v_p(b)): the numerator
   criterion and the composite depth threshold
   (explore_dual_locality.py) are the vanishing locus of one
   density formula.
F2 THE COUNTING COLLAPSE (rule; scope sharpened to DEEP fibers):
   on deep fibers the class-mixed counting density is EXACTLY
   (1 - 1/a)/b^l for a coprime to b — measured 6/90, 60/900,
   600/9000, 6000/90000 (b=10, a=3: the law with ZERO edge term at
   every scanned t'), 2/15 exactly at b=6, halving errors into
   1/3 at b=2 (85/256 at t'=9). The frozen D2 wording omitted the
   deep qualifier; the engine's own shallow specimen (b=2, a=3,
   j=1, where 2^1 < 3) sits at the correct SHALLOW mixed law 1/6
   (43/256 at t'=9), no collapse — the general per-period formula
   covers it, the collapse is a deep-fiber statement. Anchor: the
   six exceptional mantissas {13,16,23,26,33,66} at t'=2.
F3 THE BENFORD RE-READ (rule): the Benford density of the same
   exception sets converges to (1 - 1/a) R(x) / b^l,
   R(x) = b^{x-1}(1 + (b-1)(1-x)), x = {log_b a}: errors 4.1e-12
   (b=10 a=3), 4.3e-07 (b=10 a=7), 2.2e-05 (b=2, a=3 and a=5, at
   t'=15); carry-class weights converge to {log_b a} (8.7e-07 at
   b=10). Benford sees MORE exceptions than counting at every
   scanned case (R > 1 strictly between the lattice points
   x = 0, 1): counting is blind to the multiplier's mantissa,
   the pole's own measure reads it.
F4 THE PAIR CRITERION (rule; saturation clause added): the residue
   form needs its saturated regime stated — exceptional iff
   T >= b^{Lam} (the image interval covers a full grid period) OR
   (-ma mb) mod b^{Lam} in [1, T], T = floor(L/b^{2j}); with the
   clause it equals the endpoint verdict on every validated pair
   (~14k, plus exponent-straddling pairs exceptional by
   definition). The sibling's measured densities reproduce as
   exact integer counts: 13/16, 29/64, 59/256, 113/1024, 245/4096
   (0.8125 and 0.0598 anchors on the nose).
F5 THE PAIR DENSITY LIMITS (rule): counting -> 2(1 - b^{-j})/b^c
   (errors 1.3e-04 at b=2 t=8, 1.4e-04 at b=3 t=5, 8.5e-05 at
   b=10's single scanned t), Benford -> the same times
   K_b = (b-1)^2/(b ln^2 b) (1.041, 1.105, 1.528) — and K_b equals
   the mean of F3's hump R(x) over x uniform in [0,1], two
   independent derivations of one constant, both confirmed. The
   counting limit is base-free: each operand contributes b^{-c},
   an additive lookahead budget. The sibling's printed ratio
   wobble (1.79-2.09) is finite-t plus the saturated c=1 cell;
   the limit ratio is exactly b under both measures.
F6 BENFORD = THE DUAL HAAR (property): the rational-arc telescope
   is EXACT — the preimage of every scanned window cell under
   x -> qx on the scale circle is one arc (<= 2 chart pieces)
   whose endpoint ratios multiply to (m+1)/m as exact rationals,
   for q in {3, 7, 1/3, 21/5}, b in {2, 10}; counting measure
   fails the same invariance exactly (mass 10/27 != 1/9 for the
   digit-1 cell under tripling); the additive mirror (nu * uniform
   = uniform on Z/30) is exact. The mirror table stands: finite
   pole ambient Z, rung Z/N, Haar counting, reading cells = cosets
   (equal Haar); dual pole ambient R_{>0}, rung the scale circle
   R_{>0}/b^Z, Haar log-uniform, reading cells NOT cosets (cell m
   has Haar log_b((m+1)/m) — Benford's law is the grid/Haar
   mismatch, and that mismatch is why only this pole's densities
   carry a measure tag).
F7 THE CARRY LINEARIZATION (rule): the Benford pair-carry
   probability converges to 1/2 at every base (0.49949 at b=2,
   0.49998 at b=10) — in log coordinates the carry boundary is the
   straight line x+y = -1 and the pole's own measure is uniform
   there; under counting it is base-entangled and transcendental,
   0.613215 measured vs the hyperbola law 0.613706 at b=2,
   0.826830 vs 0.826841 at b=10. The scaling carry weight
   converges to {log_b a} (0.4771204 vs log10(3) = 0.4771213).
F8 THE CORPUS MEASURE AUDIT (audit, discharged): every other law
   of the dual corpus is per-fiber or per-window — measure-free;
   the graded-locality densities were the corpus's only
   measure-carrying statements and are now closed-formed under
   both measures, with the sibling's F5 carrying a settling
   pointer naming its measure (counting on mantissa pairs).

Run record: the pre-engine hand audit of the engine itself caught
three sweep bugs of one species — loops that grew the LOOKAHEAD
(changing the law under test) where they meant to grow the output
precision at fixed lookahead; fixed before any run. The first two
runs then caught, via the engine's own asserts, two scope
corrections to the pre-run design (the D2 deep qualifier — the
shallow specimen sits at its own mixed law; the D4 saturation
clause — the saturated c=1 anchor was the first failure) and one
meter bug (the pair validator reduced P_min instead of ma*mb mod
b^Lam; the criterion was right, the meter wrong, its own assert
the tripwire). Final run 14813 checks, ~1 s wall clock, trivial
memory.
"""

import math
from fractions import Fraction
from math import gcd

CHECKS = 0


def ok(cond, label):
    global CHECKS
    assert cond, "FAIL: " + label
    CHECKS += 1


def ndigits(a, b):
    """Number of base-b digits of a >= 1, minus 1 (the exponent)."""
    e = 0
    while a >= b:
        a //= b
        e += 1
    return e


def window(n, b, t):
    """The size window (sign, exponent, t leading digits) of n != 0."""
    s = 1 if n > 0 else -1
    a = abs(n)
    e = ndigits(a, b)
    j = max(0, e + 1 - t)
    return (s, e, a // b**j)


def ceil_div(x, y):
    return -((-x) // y)


def rad_divides(a, b):
    """rad(a) | rad(b): every prime factor of a divides b."""
    x = a
    for p in range(2, x + 1):
        while x % p == 0:
            if b % p != 0:
                return False
            x //= p
    return True


def depth_threshold(a, b):
    """max_p ceil(v_p(a)/v_p(b)) over p | a (requires rad(a)|rad(b))."""
    out, x, p = 0, a, 2
    while x > 1:
        if x % p == 0:
            va = 0
            while x % p == 0:
                x //= p
                va += 1
            vb = 0
            bb = b
            while bb % p == 0:
                bb //= p
                vb += 1
            out = max(out, ceil_div(va, vb))
        p += 1
    return out


# ------------------------------------------------ scaling machinery
def scaling_exceptional(a, b, t, m, j):
    """Endpoint (monotone-exact) exception verdict for fiber m."""
    bj = b**j
    lo, hi = a * m * bj, a * ((m + 1) * bj - 1)
    return window(lo, b, t) != window(hi, b, t)


def scaling_exc_mantissas(b, a, t, l, j):
    """Exceptional mantissas at one exponent (fast class-split form)."""
    tp = t + l
    e_in = tp + j - 1
    alpha = ndigits(a, b)
    bj = b**j
    cp = b ** (e_in + alpha + 1)
    p0 = b ** (e_in + alpha + 1 - t)
    p1 = p0 * b
    out = []
    for m in range(b ** (tp - 1), b**tp):
        lo = a * m * bj
        hi = lo + a * (bj - 1)
        if hi < cp:
            exc = (lo // p0) != (hi // p0)
        elif lo >= cp:
            exc = (lo // p1) != (hi // p1)
        else:
            exc = True
        if exc:
            out.append(m)
    return out


def class_interiors(b, a, l, t, j):
    """[mA, mB) of class-interior mantissas for theta = 0, 1."""
    tp = t + l
    e_in = tp + j - 1
    alpha = ndigits(a, b)
    bj = b**j
    cp = b ** (e_in + alpha + 1)
    m_lo, m_hi = b ** (tp - 1), b**tp
    top = ((cp - 1) // a + 1) // bj      # first m with fiber not wholly low
    bot = ceil_div(cp, a * bj)           # first m with fiber wholly high
    return (m_lo, min(m_hi, top)), (max(m_lo, bot), m_hi)


def run_count(b, a, t, j, tp, start, length, theta):
    """Exact exception count over a run of class-interior fibers."""
    e_in = tp + j - 1
    alpha = ndigits(a, b)
    bj = b**j
    pJ = b ** (e_in + alpha + 1 - t + theta)
    cnt = 0
    for m in range(start, start + length):
        lo = a * m * bj
        cnt += (lo // pJ) != ((lo + a * (bj - 1)) // pJ)
    return cnt


# ------------------------------------------------ CHECK 1: controls
def check_controls():
    print("CHECK 1 - positive controls")
    # monotone endpoint shortcut == full-value sweep (scaling, tiny)
    for b, a, t, l, j in ((2, 3, 2, 1, 2), (10, 7, 1, 1, 1)):
        tp = t + l
        for m in range(b ** (tp - 1), b**tp):
            bj = b**j
            full = len({window(a * n, b, t)
                        for n in range(m * bj, (m + 1) * bj)}) > 1
            ok(full == scaling_exceptional(a, b, t, m, j),
               "endpoint == full sweep at b=%d a=%d m=%d" % (b, a, m))
    print("  scaling endpoint verdicts == full-value sweeps (2 scopes)")
    # pair endpoint shortcut == full product sweep (tiny)
    b, t, c, j = 2, 2, 1, 2
    tp = t + c
    bj = b**j
    for ma in range(b ** (tp - 1), b**tp):
        for mb in range(b ** (tp - 1), b**tp):
            full = len({window(x * y, b, t)
                        for x in range(ma * bj, (ma + 1) * bj)
                        for y in range(mb * bj, (mb + 1) * bj)}) > 1
            pmin = ma * mb * bj * bj
            pmax = ((ma + 1) * bj - 1) * ((mb + 1) * bj - 1)
            ok(full == (window(pmin, b, t) != window(pmax, b, t)),
               "pair endpoint == full sweep at (%d,%d)" % (ma, mb))
    print("  pair endpoint verdicts == full product sweeps (1 scope)")
    # Benford meter control: leading-digit-1 mass = log_b 2
    for b, tprime in ((10, 5), (2, 10)):
        lo = b ** (tprime - 1)
        mass = sum(math.log(m + 1) - math.log(m)
                   for m in range(lo, 2 * lo)) / math.log(b)
        ok(abs(mass - math.log(2) / math.log(b)) < 1e-9,
           "Benford meter returns log_b 2 at b=%d" % b)
    print("  Benford meter control: leading-digit-1 mass = log_b(2) ok")
    # radical-law controls: doubling exact at base 10, tripling rough at 2
    ok(len(scaling_exc_mantissas(10, 2, 1, 1, 1)) == 0,
       "doubling at base 10 has zero exceptions at lookahead 1")
    ok(len(scaling_exc_mantissas(2, 3, 2, 1, 2)) > 0,
       "tripling at base 2 has exceptions")
    print("  radical-law controls: 2x@10 clean, 3x@2 graded")


# ------------------------------------------------ CHECK 2: period law
def check_period_law():
    print("CHECK 2 - the period law (D1): exact count per class-interior"
          " period")
    grid = {2: (3, 5, 7, 6, 4, 12), 10: (3, 7, 21, 6, 4, 40),
            6: (5, 9, 8, 15)}
    t = 2
    tested, zeros = 0, 0
    for b, alist in grid.items():
        for a in alist:
            alpha = ndigits(a, b)
            for l in ((1, 2, 3) if b == 2 else (1, 2)):
                for j in (1, 2, 4):
                    bj = b**j
                    for theta in (0, 1):
                        if theta == 1 and a == b**alpha:
                            continue        # carry class empty
                        P = b ** (l + alpha + theta)
                        d = gcd(a, P)
                        expect = d * ((a * (bj - 1)) // (bj * d))
                        # grow t (keeping the lookahead l fixed) until
                        # the class interior holds a full period
                        phases = (0, 1, P // 3) if P < 5000 else (0,)
                        need = P + max(phases) + 2
                        tt = t
                        while True:
                            lo_r, hi_r = class_interiors(b, a, l,
                                                         tt, j)[theta]
                            if hi_r - lo_r >= need:
                                break
                            tt += 1
                            assert tt <= 12, "no interior period found"
                        for ph in phases:
                            cnt = run_count(b, a, tt, j, tt + l,
                                            lo_r + ph, P, theta)
                            ok(cnt == expect,
                               "period count %d == %d at b=%d a=%d l=%d "
                               "j=%d th=%d ph=%d" %
                               (cnt, expect, b, a, l, j, theta, ph))
                        tested += 1
                        if bj * d > a:
                            ok(expect == a - d,
                               "deep count == a - d at b=%d a=%d" % (b, a))
                        zero = (rad_divides(a, b) and
                                l + alpha + theta >= depth_threshold(a, b))
                        ok((expect == 0) == zero,
                           "zero locus == radical+threshold at b=%d a=%d "
                           "l=%d th=%d" % (b, a, l, theta))
                        zeros += (expect == 0)
    print("  %d (b, a, l, j, theta) scopes, every period exact;"
          " %d zero-locus cells == radical law + depth threshold"
          % (tested, zeros))


# ------------------------------------------------ CHECK 3: collapse
def mixed_law(b, a, l, j):
    """The exact mixed-class density: per-period counts weighted by
    the counting class weights (deep OR shallow)."""
    alpha = ndigits(a, b)
    bj = b**j
    rho = []
    for theta in (0, 1):
        P = b ** (l + alpha + theta)
        d = gcd(a, P)
        rho.append(Fraction(d * ((a * (bj - 1)) // (bj * d)), P))
    w0 = Fraction(b ** (alpha + 1) - a, a * (b - 1))
    return w0 * rho[0] + (1 - w0) * rho[1]


def check_counting_collapse():
    print("CHECK 3 - the counting collapse (D2): totals and density")
    cases = ((10, 3, 1, 1), (10, 7, 1, 1), (2, 3, 2, 2), (6, 5, 1, 1),
             (2, 3, 2, 1))
    for b, a, t, j in cases:
        l = 1
        law = mixed_law(b, a, l, j)
        deep = b**j > a
        if deep:
            ok(law == Fraction(a - 1, a * b**l),
               "deep mixed law collapses to (a-1)/(a b^l)")
        print("  b=%d a=%d l=%d j=%d: law = %s (%s)"
              % (b, a, l, j, law,
                 "deep: collapses to (a-1)/(a b^l)" if deep
                 else "shallow: no collapse"))
        span = 7 if b == 2 else 4
        for tt in range(t, t + span):
            tprime = tt + l
            exc = scaling_exc_mantissas(b, a, tt, l, j)
            fibers = b**tprime - b ** (tprime - 1)
            ok(abs(Fraction(len(exc)) - law * fibers) <= 2 * a + 2,
               "edge bound at b=%d a=%d j=%d t'=%d" % (b, a, j, tprime))
            dens = Fraction(len(exc), fibers)
            err = abs(dens - law)
            print("    t'=%d: %d/%d = %.6f  (|density - law| = %.2e)"
                  % (tprime, len(exc), fibers, float(dens), float(err)))
            ok(err <= Fraction(2 * a + 2, fibers),
               "density within edge/fibers at t'=%d" % tprime)
    # the exact anchor: b=10 a=3 t=1 l=1 t'=2 -> exactly 6 of 90
    exc = scaling_exc_mantissas(10, 3, 1, 1, 1)
    ok(len(exc) == 6, "anchor: exactly 6 exceptional fibers")
    ok(exc == [13, 16, 23, 26, 33, 66], "anchor: the six mantissas")
    print("  anchor b=10 a=3 t'=2: exceptions {13,16,23,26,33,66},"
          " density exactly 1/15")


# ------------------------------------------------ CHECK 4: Benford scaling
def check_benford_scaling():
    print("CHECK 4 - the Benford re-read of scalings (D3)")
    cases = ((10, 3, 1, 1, (3, 4, 5, 6)), (10, 7, 1, 1, (3, 4, 5, 6)),
             (2, 3, 1, 2, (5, 9, 13, 15)), (2, 5, 1, 3, (5, 9, 13, 15)))
    for b, a, l, j, tprimes in cases:
        alpha = ndigits(a, b)
        x = math.log(a) / math.log(b) - alpha
        R = b ** (x - 1) * (1 + (b - 1) * (1 - x))
        law = (1 - 1 / a) * R / b**l
        lawc = (1 - 1 / a) / b**l
        print("  b=%d a=%d l=%d j=%d: Benford law %.7f (counting %.7f,"
              " hump R=%.6f)" % (b, a, l, j, law, lawc, R))
        errs, werrs = [], []
        lnb = math.log(b)
        for tprime in tprimes:
            tt = tprime - l
            exc = scaling_exc_mantissas(b, a, tt, l, j)
            dens = sum(math.log(m + 1) - math.log(m) for m in exc) / lnb
            # carry-class Benford weight -> {log_b a}
            _, (bot, m_hi) = class_interiors(b, a, l, tt, j)
            w1 = (math.log(m_hi) - math.log(bot)) / lnb
            errs.append(abs(dens - law))
            werrs.append(abs(w1 - x))
            print("    t'=%d: density %.7f (err %.2e), carry weight"
                  " %.7f (err %.2e)"
                  % (tprime, dens, errs[-1], w1, werrs[-1]))
        ok(errs[-1] < 0.06 * law,
           "Benford density within 6%% of law at b=%d a=%d" % (b, a))
        ok(errs[-1] < errs[0] / 4, "error shrank 4x at b=%d a=%d" % (b, a))
        ok(werrs[-1] < 1e-3, "carry weight -> frac(log_b a) at b=%d" % b)


# ------------------------------------------------ CHECK 5: pairs
def pair_scan(b, t, c, j):
    """Exact pair exception count + Benford-weighted density at one
    exponent; also validates the residue criterion on small scopes."""
    tp = t + c
    bj = b**j
    bj2 = bj * bj
    m_lo, m_hi = b ** (tp - 1), b**tp
    e = tp + j - 1
    cp = b ** (2 * e + 1)
    p0 = b ** (2 * e + 1 - t)
    p1 = p0 * b
    lam0 = b ** (t + 2 * c - 1)
    validate = (m_hi - m_lo) <= 70
    w = [math.log(m + 1) - math.log(m) for m in range(m_lo, m_hi)]
    lnb2 = math.log(b) ** 2
    exc_n, bw = 0, 0.0
    for ma in range(m_lo, m_hi):
        wa = w[ma - m_lo]
        for mb in range(m_lo, m_hi):
            pmin = ma * mb * bj2
            pmax = ((ma + 1) * bj - 1) * ((mb + 1) * bj - 1)
            if pmax < cp:
                exc = (pmin // p0) != (pmax // p0)
                theta = 0
            elif pmin >= cp:
                exc = (pmin // p1) != (pmax // p1)
                theta = 1
            else:
                exc = True
                theta = None
            if validate and theta is not None:
                lam = lam0 * (b if theta else 1)
                r = (-ma * mb) % lam
                T = (pmax - pmin) // bj2
                ok(exc == (T >= lam or 1 <= r <= T),
                   "residue criterion == endpoints at (%d,%d)" % (ma, mb))
            if exc:
                exc_n += 1
                bw += wa * w[mb - m_lo]
    total = (m_hi - m_lo) ** 2
    return exc_n, total, bw / lnb2


def check_pairs():
    print("CHECK 5 - the pair criterion + density limits (D4, D5)")
    # the sibling's anchors: b=2, t=2, depth 4, c = 1..5
    print("  sibling anchors (b=2 t=2 depth 4):")
    fracs = []
    for c in range(1, 6):
        exc, total, _ = pair_scan(2, 2, c, 4)
        fracs.append(exc / total)
        print("    c=%d: %d/%d = %.4f" % (c, exc, total, exc / total))
    ok(fracs[0] == Fraction(13, 16), "anchor 13/16 at c=1")
    ok(abs(fracs[4] - 0.0598) < 5e-5, "anchor 0.0598 at c=5")
    # the limit laws
    K = {b: (b - 1) ** 2 / (b * math.log(b) ** 2) for b in (2, 3, 10)}
    runs = ((2, 3, 6, range(1, 9)), (3, 2, 4, range(1, 6)),
            (10, 2, 2, range(1, 2)))
    for b, c, j, ts in runs:
        depth = 1 - b ** (-j)
        law_c = 2 * depth / b**c
        law_b = law_c * K[b]
        print("  b=%d c=%d j=%d: counting law %.6f, Benford law %.6f"
              " (K_b = %.6f)" % (b, c, j, law_c, law_b, K[b]))
        errs_c, errs_b = [], []
        for t in ts:
            exc, total, bdens = pair_scan(b, t, c, j)
            dc = exc / total
            errs_c.append(abs(dc - law_c))
            errs_b.append(abs(bdens - law_b))
            print("    t=%d: counting %.6f (err %.2e), Benford %.6f"
                  " (err %.2e)" % (t, dc, errs_c[-1], bdens, errs_b[-1]))
        if len(list(ts)) > 1:
            ok(errs_c[-1] < 0.03 * law_c,
               "counting pair density within 3%% at b=%d" % b)
            ok(errs_b[-1] < 0.03 * law_b,
               "Benford pair density within 3%% at b=%d" % b)
            ok(errs_c[-1] < errs_c[0] / 4 and errs_b[-1] < errs_b[0] / 4,
               "pair errors shrank 4x at b=%d" % b)
        else:
            ok(abs(dc / law_c - 1) < 0.25 and abs(bdens / law_b - 1) < 0.25,
               "single-t consistency at b=%d (25%%)" % b)


# ------------------------------------------------ CHECK 6: Haar
def circle_preimage_ratio(q, b, t, m):
    """Pieces of the preimage of window cell m under x -> q x on the
    scale circle, as exact rationals; returns (piece count, product
    of hi/lo ratios)."""
    cell_lo = Fraction(m, b ** (t - 1))
    cell_hi = Fraction(m + 1, b ** (t - 1))
    pieces = []
    for i in range(-8, 9):
        sc = Fraction(b) ** i / q
        lo, hi = cell_lo * sc, cell_hi * sc
        lo2, hi2 = max(lo, Fraction(1)), min(hi, Fraction(b))
        if lo2 < hi2:
            pieces.append((lo2, hi2))
    prod = Fraction(1)
    for lo, hi in pieces:
        prod *= hi / lo
    return len(pieces), prod


def check_haar():
    print("CHECK 6 - Benford as the dual Haar (D6) + the carry"
          " linearization (D7)")
    # exact scale invariance: rational-arc telescope
    for q in (Fraction(3), Fraction(7), Fraction(1, 3), Fraction(21, 5)):
        for b, t, ms in ((10, 2, (10, 37, 99)), (2, 3, (4, 5, 7))):
            for m in ms:
                n, prod = circle_preimage_ratio(q, b, t, m)
                ok(n <= 2, "preimage is one arc (<= 2 chart pieces)")
                ok(prod == Fraction(m + 1, m),
                   "telescope == (m+1)/m at q=%s b=%d m=%d" % (q, b, m))
    print("  scale invariance EXACT: preimage arc ratios telescope to"
          " (m+1)/m for q in {3, 7, 1/3, 21/5}, b in {2, 10}")
    # counting measure is NOT scale-invariant (exact counterexample)
    pre = Fraction(20, 3) - Fraction(10, 3)   # preimage of [1,2) under *3
    ok(pre / 9 != Fraction(1, 9),
       "counting fails invariance under tripling at b=10")
    print("  counting non-invariance: preimage of digit-1 cell under 3x"
          " has counting mass 10/27 != 1/9 (exact)")
    # the additive mirror on Z/N: one uniform summand -> uniform sum
    N = 30
    nu = [(i * i * 7 + 3 * i + 1) % 11 for i in range(N)]
    u = [1] * N
    s = sum(nu)
    conv = [sum(nu[a] * u[(k - a) % N] for a in range(N))
            for k in range(N)]
    ok(all(x == s for x in conv),
       "nu * uniform == uniform on Z/30 (exact)")
    print("  additive mirror: nu * uniform = uniform on Z/30, exact")
    # carry linearization: pair carry -> 1/2 under Benford, any base
    for b, tps in ((2, (6, 9, 12)), (10, (3, 4, 5))):
        lnb = math.log(b)
        vals = []
        for tp in tps:
            m_lo, m_hi = b ** (tp - 1), b**tp
            w = [math.log(m + 1) - math.log(m)
                 for m in range(m_lo, m_hi)]
            suf = [0.0] * (len(w) + 1)
            for i in range(len(w) - 1, -1, -1):
                suf[i] = suf[i + 1] + w[i]
            cp2 = b ** (2 * tp - 1)
            tot = 0.0
            for ma in range(m_lo, m_hi):
                thr = ceil_div(cp2, ma)
                idx = min(max(thr - m_lo, 0), len(w))
                tot += w[ma - m_lo] * suf[idx]
            vals.append(tot / lnb**2)
        print("  Benford pair-carry at b=%d: %s -> 1/2" %
              (b, ["%.5f" % v for v in vals]))
        ok(abs(vals[-1] - 0.5) < 0.02, "pair carry -> 1/2 at b=%d" % b)
        ok(abs(vals[-1] - 0.5) < abs(vals[0] - 0.5) + 1e-12,
           "pair-carry error non-growing at b=%d" % b)
    # counting pair carry: base-entangled transcendental value
    for b, tp, target in ((2, 12, 0.613706), (10, 5, 0.826841)):
        m_lo, m_hi = b ** (tp - 1), b**tp
        cp2 = b ** (2 * tp - 1)
        cnt = sum(m_hi - max(m_lo, ceil_div(cp2, ma))
                  for ma in range(m_lo, m_hi))
        dens = cnt / (m_hi - m_lo) ** 2
        print("  counting pair-carry at b=%d: %.6f (law %.6f)"
              % (b, dens, target))
        ok(abs(dens - target) < 0.01,
           "counting pair-carry matches hyperbola law at b=%d" % b)
    ok(abs(0.613706 - 0.826841) > 0.2,
       "counting carry is base-dependent where Benford pins 1/2")
    # scaling carry weight -> {log_b a} under Benford
    b, a, l, j = 10, 3, 1, 1
    x = math.log(a) / math.log(b)
    for tt in (3, 5):
        _, (bot, m_hi) = class_interiors(b, a, l, tt, j)
        w1 = (math.log(m_hi) - math.log(bot)) / math.log(b)
        print("  Benford scaling-carry weight at t'=%d: %.7f"
              " ({log_10 3} = %.7f)" % (tt + l, w1, x))
    ok(abs(w1 - x) < 1e-3, "scaling carry weight -> frac(log_b a)")


def main():
    print("=" * 70)
    print("THE POLE'S OWN MEASURE: exact densities + Benford as the"
          " dual Haar")
    print("=" * 70)
    check_controls()
    check_period_law()
    check_counting_collapse()
    check_benford_scaling()
    check_pairs()
    check_haar()
    print("=" * 70)
    print("ALL CHECKS PASSED: %d" % CHECKS)


if __name__ == "__main__":
    main()
