"""The Lipschitz criterion: one metric statement behind both poles'
reading laws — what a digit window computes is what is Lipschitz in
the window's own metric, and the boundary-alignment clause is exactly
the price of a non-ultrametric window read through a partition.
[Sharpened since by explore_reading_geometry.py: Lipschitz AT CELL
SCALE — the readable class includes fiber-cellular maps whose
pointwise ratios are unbounded — and the per-level bound carries a
one-digit stream correction at redundant covers; see also F4.]

THE QUESTION
------------
The corpus so far charts four reading regimes, each with its own laws:
the trailing end (residues mod b^t) has multiplication free and
division gated by rad(v) | rad(b) with a depth threshold
(explore_dual_locality.py, the two-ends exchange and depth threshold);
the non-redundant leading end has division free and multiplication
gated by rad(u) | rad(b) (the numerator criterion, same record); the
redundant leading end dissolves the arithmetic gates entirely and
prices by size (the delay law, explore_dual_redundant.py). This
experiment asks whether ONE criterion carves all of them: a window
reads f at bounded lookahead iff f is Lipschitz in the window's own
metric, PLUS a boundary-alignment clause exactly where the window's
cell family is a partition of a NON-ultrametric space — and whether
the criterion's constants (the Lipschitz constant's logarithm)
reproduce the measured lookaheads exactly.

THE FOUR REGIMES AND THEIR METRICS (fixed before anything else)
---------------------------------------------------------------
R1 TRAILING NON-REDUNDANT: window = n mod b^t. The metric is the
   b-ultrametric d_b(n, n') = b^{-k}, k = max{j : b^j | n - n'};
   fibers are the cosets V + b^t Z = the d_b-balls. Readability at
   lookahead c ("f(n) mod b^t is a function of n mod b^{t+c}") IS,
   verbatim, the Lipschitz statement d_b(f n, f n') <= b^c d_b(n, n').
   In an ultrametric space every set of diameter <= b^{-t} lies inside
   ONE ball (the strong triangle), so the ball partition's Lebesgue
   number equals the ball size — no alignment clause can arise.
R2 TRAILING REDUNDANT: digits {-a..a} read LSB-first. The completions
   of a t-prefix of value V form (a sub-progression of) the coset
   V + b^t Z, and as a set the fiber depends on V only through
   V mod b^t; two cells are cosets of one subgroup — EQUAL OR
   DISJOINT. A coset cover cannot partially overlap, so redundancy
   cannot buy the trailing end a positive Lebesgue overlap: the R1
   criterion should hold verbatim and the division gate survive.
R3 LEADING NON-REDUNDANT: window = (sign, exponent, t leading
   digits). The metric is the scale-circle log metric
   d_log(x, y) = |log_b x - log_b y| (sign a clopen component); a
   depth-t cell has d_log-diameter ~ b^{-t}/ln b, the cells partition,
   and the Lebesgue number is 0 (adjacent integers can straddle any
   boundary). Every scaling x -> (u/v)x is a d_log-ISOMETRY, yet the
   numerator criterion gates it by rad(u) | rad(b): here Lipschitz is
   necessary but NOT sufficient, and the whole gate is the ALIGNMENT
   clause (image cell boundaries grid-aligned), stated on the
   partition — any non-redundant digit set (standard asymmetric,
   balanced symmetric) induces its interval partition and falls under
   the one clause.
R4 LEADING REDUNDANT: same log metric; the cells fatten to intervals
   V b^j +- a R_j covering with positive Lebesgue count
   (explore_dual_redundant.py, the prefix-interval law). A positive
   Lebesgue number deletes the alignment clause: Lipschitz alone
   should suffice, priced by size.

THE ENGINES
-----------
(i) Trailing determinacy checks (exhaustive over residue classes at
stated scopes) with collision witnesses below the threshold.
(ii) THE RATIONAL-SLOPE SAFETY GAME, the digitwise-linear engine of
explore_dual_redundant.py generalized to f(n) = floor((u/v)n + w/z):
invariant R_k = (u/v)X_k + w/z - E_k b^c, integer state r = L R with
L = lcm(v, z), step r' = b r + (Lu/v) x - L e b^c; at input end
floor((u/v)X + w/z) = E b^c + floor(R), so the flush needs
|floor(R)| <= a R_c (the floor LOOSENS the pure-stream flush). R is a
sufficient statistic (the map is affine; frac(R) carries the eventual
floor correction). Locality at lookahead c iff the initial state lies
in the greatest fixed point of "some e keeps r flushable-and-winning
for every x" — computed exhaustively, never by sampled play.
(iii) THE PREFIX-TREE GAME for maps that are not digitwise-linear
(|x|, piecewise-affine): backward induction over (read prefix value,
emitted prefix value) at fixed input length, emission legal iff the
f-image hull of the input fiber fits the emitted prefix's reachable
interval; the leaf condition is re-checked from the definition.

PREDICTIONS, fixed before the engine ran
----------------------------------------
P-A [criterion, elementary] R1: bounded-lookahead trailing
    readability = d_b-Lipschitz, with c_min = max(0,
    ceil(log_b Lip_b(f))). For the affine-floor class: Lip_b(x -> mx)
    <= 1 (free, every m); Lip_b(floor(x/v)) = b^{d_v} with
    d_v = min{d : v | b^d} = max_p ceil(v_p(v)/v_p(b)) — finite iff
    rad(v) | rad(b), otherwise Lipschitz fails and growing collision
    witnesses exist at every depth. The depth threshold and the
    trailing gate of the two-ends exchange are b-adic Lipschitz facts.
    Phases floor((n+s)/v) ride free (shifts are d_b-isometries).
P-B [criterion, two-line proof] R2 = R1 verbatim: a shared deep
    LSB-prefix realizes any two values agreeing mod b^{t+c}, so
    redundant-LSB readability forces the same congruence determinacy;
    the division gate SURVIVES redundancy (collision witnesses with
    redundant strings); redundancy is a leading-end-only door.
P-C [derived, rule] R3: the alignment clause carries the whole gate —
    scalings are log-isometries (Lipschitz constant 1) at every u/v,
    readable iff image boundaries align with the output partition:
    smooth-u scalings aligned at every scanned cell, rough-u scalings
    given straddle witnesses; balanced ternary's centered partition
    passes x3 (containment at every scanned cell) and fails x2 —
    standard and balanced digit sets under ONE clause.
P-D [derived bound + expected tightness; the pure-power waiver at
    negative exponents is a TRANSPLANT from the integer case] R4,
    THE RATIONAL-SLOPE DELAY LAW: floor((u/v)n + w/z) is exactly
    local at bounded lookahead for EVERY rational slope u/v > 0 —
    BOTH radical gates dissolve (numerator and denominator) — with
    the sufficient bound b^c (2a - b + 1) >= 2a(u/v) (the integer
    delay law with m -> u/v = the Lipschitz constant) and expected
    minimal lookahead
        c_min = max(0, ceil(log_b(2a u / (v (2a - b + 1)))))
    for slopes that are not pure b-powers, pure b-power slopes b^s
    at c_min = max(0, s) (aligned maps waive the margin — the
    alignment clause's ghost inside the pricing). The phase w/z is
    FREE (same c_min), where the non-redundant leading end's phase
    law kills every nonzero phase. Hand-played spots to confirm:
    (2,1) slope 1/3 at c = 0 (division by 3, redundant binary, delay
    ZERO), slope 3/5 at 1, slope 5/3 at 2; (10,6) slope 1/3 at 0
    [freeze-time arithmetic slip: the frozen formula itself gives 1,
    since 10^0 * 3 * 3 = 9 < 12 = 2au — the formula is the
    prediction; see the run record], slope 7/3 at 1, slope 3/5 at 1,
    slope 21/5 at 2.
P-E [derived from the flush, hand-played] the margin-zero control
    (3,1) balanced ternary through the SAME game: non-power slopes
    infeasible at every scanned c (the bound divides by zero = no
    Lebesgue slack); x3 at c = 1, x9 at 2 (the schedule shift);
    slope 1/3 at c = 1, NOT 0 — the balanced floor correction
    (floor(d/3) = -1 on digit -1) needs one flush digit, so the
    integer waiver does NOT transplant to negative powers at margin
    zero; at (2,1) it does (slope 1/2 at c = 0, hand-played).
P-F [derived, rule] THE HEDGE: |x| is exactly local at the redundant
    leading end at small lookahead (expected c = 1 at (2,1) and
    (10,6), bracket <= 2) even though SIGN is non-local at every
    lookahead — a sign-symmetric map computed without ever reading
    the sign; the all-zero output prefix is the hedge, and the same
    near-zero prefixes that wall division pay for it. At the trailing
    end |x| is DEAD (|x| mod b^t needs the sign of x, an archimedean
    read): collision witnesses at every scanned lookahead.
P-G [derived, rule] SCALE CONFINEMENT: a genuinely two-slope monotone
    piecewise-affine map is trailing-DEAD at every base (trailing
    fibers are unbounded APs, so one fiber straddles the breakpoint
    and mixes slopes: d_b-Lipschitz fails; collision witnesses) and
    redundant-leading-ALIVE (deep leading cells eventually see one
    affine piece; prefix-tree game feasible at the tail slope's
    delay, bracket c <= 3 at (2,1) for slopes {1, 2}).
P-H [derived witnesses both ways] THE EXPONENTIAL SPLIT: f(n) = 2^n
    is leading-DEAD at every redundancy (two integers sharing every
    deep leading fiber map to different exponent windows: the
    log-Lipschitz constant diverges) but TRAILING-READABLE at b = 10
    with c_min = 1 (ord(2 mod 5^t) = 4 * 5^{t-1} divides 10^{t+1};
    collision at c = 0 via 2^10 != 1 mod 5) and trailing-dead at
    b = 3 (the order 2 * 3^{t-1} carries the factor 2 that rad(3)
    lacks; collision at every c). The exponential is d_b-Lipschitz
    by lifting-the-exponent exactly where its order tower is
    b-smooth: the ultrametric pole is the exponential's home.
P-I [identity + measured] THE PRICING ARITHMETIC: the trailing price
    of /v is d_v = MAX_p ceil(v_p(v)/v_p(b)); the redundant leading
    price of *u is ceil(log_b u + margin) with log_b u =
    SUM_p v_p(u) log_b p — the product formula. The ultrametric
    window prices by MAX over places, the archimedean window by SUM:
    each pole prices in its own metric's arithmetic.
P-J [synthesis; engine = the sections above] THE TWO-POLE READING
    CRITERION: a window reads f at bounded lookahead iff f is
    Lipschitz in the window's own metric AND the image of each deep
    input cell fits one output cell; the fitting follows from
    Lipschitz alone wherever the cell family has positive Lebesgue
    number relative to cell size (ultrametric balls: automatic;
    redundant covers: bought), and degenerates to the boundary-
    alignment clause exactly at the non-redundant archimedean
    window — where it is the radical and phase gates. The wall
    corpus reads as the criterion's negative space: residue reads
    (leading) and order reads are d_log-discontinuous, catastrophic
    cancellation is the log-metric blowup of subtraction at its zero
    locus, and the division certificate |D| >= Dmin is a Lipschitz-
    domain restriction.

KILL CRITERIA, fixed at the freeze: K1 any rational slope infeasible
at the P-D sufficient bound kills the rational game (or the bound);
K2 a smooth-denominator floor violating d_b-Lipschitz at the stated
constant, or a rough-denominator floor passing determinacy, kills
P-A; K3 |x| infeasible through c = 2 kills the hedge; K4 sign or
trailing-|x| passing a locality test at any scanned lookahead kills
its wall. POSITIVE CONTROLS: PC1 the rational game at v = z = 1 must
reproduce the integer delay table of explore_dual_redundant.py
(spot: (2,1) x3 = 3, x4 = 2; (10,6) x2 = 1, x10 = 1); PC2 the
prefix-tree game must reproduce a rational-game verdict where both
run (identity slope and x2 at (2,1)); PC3 balanced ternary must
reproduce the numerator gate through the rational game (x2, 2/5
infeasible; x3 = 1). The flush margin inside P-D is asserted
separately at every scope, never folded into the verdict.

Engine: pure python, exact integers (the game state is the integer
L*R), no sampling in any verdict; seconds.

FINDINGS (from the run: 601 checks, exit 0, ~6 s)
--------------------------------------------------
F1 R1 (criterion, elementary, verified at stated scopes): trailing
   readability at lookahead c IS d_b-Lipschitz with constant b^c, and
   c_min = ceil(log_b Lip_b) exactly: floor(/v) at c_min = d_v for
   v = 4, 8 | 8, 50 | 9, 12 at bases 2, 10, 6 with collisions below
   the threshold; multiplication nonexpanding (c_min = 0 at every
   scanned m); rough denominators d_b-non-Lipschitz with witnesses at
   input depths 2..6 and collisions at every scanned lookahead;
   phases ride free (d_b-isometries). The two-ends-exchange trailing
   gate and the depth threshold are b-adic Lipschitz facts.
F2 R2 THE COSET RIGIDITY (criterion, two-line proof + the
   completeness lemma verified): a depth-t redundant-LSB prefix's
   completions realize the FULL coset window V + b^t k within the
   tail budget (every element, both scanned systems, all residue
   classes) — so in the length limit the fiber IS the coset
   V + b^t Z, a shared deep prefix realizes any two values agreeing
   mod b^{t+c}, the R1 criterion holds verbatim, and the division
   gate SURVIVES redundancy (floor(/3) collisions from shared
   redundant prefixes at every scanned lookahead). Cosets of one
   subgroup cannot partially overlap: redundancy is a
   leading-end-only door.
F3 R3 (rule): the scalings are d_log-isometries and the gate is
   carried entirely by alignment — x{2,4,5} image cells grid-aligned
   over the scanned range, x{3,7} straddle witnesses; balanced
   ternary's centered partition passes x3 by cell containment and
   fails x2 by escape witness: the standard and balanced partitions
   sit under ONE alignment clause.
F4 THE RATIONAL-SLOPE DELAY LAW (rule at 17 scanned slope scopes
   across (2,1), (4,2), (10,6); the closed form conjectured
   general): floor((u/v)n) is exactly local at bounded lookahead for
   EVERY rational slope — BOTH radical gates dissolve — with minimal
   lookahead exactly the frozen closed form
   c_min = max(0, ceil(log_b(2au/(v(2a-b+1))))) at every scanned
   non-power slope and max(0, s) at the pure b-power slopes; the
   sufficient bound b^c(2a-b+1) >= 2a(u/v) held everywhere, flush
   margins asserted separately. Division by 3 at redundant binary
   runs at delay ZERO. The floor's termination correction is
   absorbed by the flush (|floor(R)| <= a R_c), never priced.
   [Settled since, the other way: explore_reading_geometry.py finds
   the unscanned slope 1/7 at (10,6) reading at 1 where the closed
   form says 0 — the form is the per-level Lebesgue bound of the
   reading lemma, and the exact (game) delay deviates from it by
   one digit in either direction. The generality conjecture is
   dead; the 17-scope exactness above stands. The b-power half is
   dead as a general claim too: explore_slope_proof.py derives the
   delay as a closed form and finds (4,2) slope 1/4 at 1, not
   max(0, s) = 0 — NEGATIVE b-powers read 0 iff a >= b - 1 and 1
   otherwise, at every depth. The scoped cells here all satisfy
   a >= b - 1, which is why the scan never saw it.]
F5 THE PHASE-SHAPE LAW (rule at scanned scopes; NEW — it corrects
   two frozen spots, see the run record): each non-redundant
   window's unique free rounding phase is its own CELL SHAPE.
   At the centered (balanced) partitions, round-to-nearest is
   exactly local at c = 0 with the denominator FREE for every
   scanned odd v (v = 3, 5, 9, 15 at (3,1); 3, 7, 9 at (5,2)) while
   every OTHER phase class is walled at every scanned lookahead —
   uniqueness swept over ALL tip-classes at v = 3 (both systems)
   and v = 5 (all five classes at (3,1)) — the exact mirror of the
   standard-digit phase law (floor free, round/ceil walled,
   explore_dual_locality.py), which is hereby the floor-shaped case
   of one law. Even denominators are tie-walled
   at balanced sets in every scanned phase (the ties of n/2 sit on
   the cell boundaries); the numerator gate is phase-invariant
   (round(2n/3) walled). At the REDUNDANT windows no phase walls or
   raises the delay (24 cells scanned) and the window-shaped phase
   saves one digit exactly where the bare floor misaligns ((2,1)
   slope 3/5 and (10,6) slope 1/3: 1 -> 0): the alignment clause
   survives inside redundancy as a one-digit PRICE, not a wall.
F6 THE HEDGE (rule): |x| is exactly local at lookahead 0 at both
   scanned redundant systems (below the predicted 1) while sign
   stays open on the all-zero prefix at every depth — the window
   computes the sign-symmetric map without ever reading the sign,
   hedging with the near-zero output prefixes that wall division.
   At the trailing end |x| is dead (collisions mod 4 at every
   scanned lookahead; depth-1 parity is the one sign-blind residue).
F7 THE PRICING ARITHMETIC (identity + measured): the trailing price
   of /v is MAX_p ceil(v_p(v)/v_p(b)); the redundant leading price
   of *u is ceil(log_b u + margin) with log_b u = SUM_p v_p(u)
   log_b p, the product formula — the ultrametric window prices by
   the max over places, the archimedean window by the sum: each
   pole prices in its own metric's arithmetic.
F8 THE SPECIMENS (rule): 2^n is leading-dead at any redundancy (a
   depth-4 fiber spans 4 output exponents, exact) yet
   trailing-READABLE at base 10 with c_min = 1 ON THE SATURATED
   RANGE n >= t (ord(2 mod 5^t) = 4*5^{t-1} | 10^{t+1}; collision
   at c = 0; below saturation the 2-column still ramps — 2^1 and
   2^{1+10^{t+1}} differ mod 2^t — a genuine exception family, the
   residue wall's shallow leak in mirror) and trailing-dead at
   base 3 at every n (the order tower carries the factor 2 that
   rad(3) lacks): the exponential lives at the ultrametric pole,
   gated by its own order tower. A
   two-slope monotone piecewise map is trailing-dead at every
   scanned lookahead (unbounded AP fibers straddle the breakpoint)
   and redundant-leading local at the tail slope's delay: piecewise
   structure is free at the scale-confined end, fatal at the
   all-scales end.
F9 THE TWO-POLE READING CRITERION (synthesis, the experiment's
   verdict):
   all four regimes verified under the one statement — readable at
   bounded lookahead iff Lipschitz in the window's own metric plus
   cell-fitting, where fitting is automatic at ultrametric windows
   (F1, F2), bought by any positive Lebesgue cover (F4, F6), and at
   non-redundant archimedean windows degenerates to the alignment
   clause = the radical gates plus the phase-shape law (F3, F5).
   The constants unify: lookahead = log_b(Lipschitz constant) +
   window margin, with the margin 0 at ultrametric windows,
   log_b(2a/(2a-b+1)) at redundant covers, and infinite (a wall)
   at misaligned non-redundant reads.

RUN RECORD: the margin-zero control caught a real engine bug — the
first game encoded the constant phase as initial state only, so the
step recursion scaled it by b each digit (the first "phases free"
pass was vacuous); fixed by re-injecting -(b-1)(w/z) per step, all
phase results re-run after the fix. Two frozen spots refuted by the
fixed game: P-D's phase-freedom (phases can LOWER the delay at
symmetric windows, never raise it — F5's redundant half) and P-E's
balanced floor(n/3) = 1 (floor is walled at every scanned lookahead;
the hand flush argument missed that the half-cell skew of floor
against a centered partition recurs at every scale — F5's law is the
correction). One freeze-time arithmetic slip in P-D's hand-spot list
((10,6) slope 1/3: the frozen formula itself gives 1, mis-evaluated
as 0; the game matches the formula). The |x| trailing witness moved
from depth 1 to depth 2 (parity is sign-blind). |x| landed at c = 0,
one below its predicted bracket. All other predictions landed as
frozen; no kill criterion fired; positive controls green. Final
run: 601 checks, wall 7.0 s, peak working set 80.0 MB (memwatch,
512 MB limit).
"""

import itertools
from fractions import Fraction
from math import gcd

CHECKS = [0]


def ok(cond, msg):
    CHECKS[0] += 1
    if not cond:
        raise AssertionError(msg)


def repunit(b, j):
    return (b**j - 1) // (b - 1)


def digits(a):
    return range(-a, a + 1)


def v_b(x, b):
    """Largest j with b^j | x (x != 0)."""
    j = 0
    while x % b == 0:
        x //= b
        j += 1
    return j


def factorize(n):
    f = {}
    d = 2
    while d * d <= n:
        while n % d == 0:
            f[d] = f.get(d, 0) + 1
            n //= d
        d += 1
    if n > 1:
        f[n] = f.get(n, 0) + 1
    return f


def depth_in_base(v, b):
    """d_v = min{d : v | b^d}, or None if rad(v) does not divide
    rad(b); equals max_p ceil(v_p(v)/v_p(b))."""
    fv, fb = factorize(v), factorize(b)
    if any(p not in fb for p in fv):
        return None
    return max(-(-fv[p] // fb[p]) for p in fv) if fv else 0


# ----------------------------------------------------------------- S1
# The metric table: measured Lipschitz data in each window metric.

def lip_exponent_pairs(f, b, k_max, n_range):
    """max over scanned pairs (n, n + s b^k) of v_b(dn) - v_b(df)
    (the b-Lipschitz exponent: Lip_b = b^exponent); None-safe."""
    best = None
    for k in range(k_max + 1):
        for n in n_range:
            for s in (1, 2, 3):
                d_n = s * b**k
                df = f(n + d_n) - f(n)
                if df == 0:
                    continue
                e = v_b(d_n, b) - v_b(df, b)
                if best is None or e > best:
                    best = e
    return best


def s1_metric_table():
    print("== S1 THE METRIC TABLE ==")
    # trailing metric: multiplication is nonexpanding, division by a
    # smooth v has Lip_b exactly b^{d_v}, rough v is non-Lipschitz.
    for (b, ms) in [(2, [3, 5, 6]), (10, [2, 3, 7, 20])]:
        for m in ms:
            e = lip_exponent_pairs(lambda n, m=m: m * n, b, 6,
                                   range(1, 200))
            ok(e is not None and e <= 0,
               f"x{m} expands d_{b} (exponent {e})")
        print(f"  base {b}: x{ms} all d_b-nonexpanding (exponent <= 0)"
              " -- multiplication free at the trailing end")
    for (b, v) in [(2, 4), (2, 8), (10, 8), (10, 50), (6, 9), (6, 12)]:
        dv = depth_in_base(v, b)
        e = lip_exponent_pairs(lambda n, v=v: n // v, b, dv + 4,
                               range(1, 4 * v * b))
        ok(e == dv, f"Lip_b(floor(/{v})) exponent {e} != d_v {dv} "
                    f"at base {b}")
        print(f"  base {b}: Lip_b(floor(/{v})) = {b}^{dv} "
              f"(d_v = {dv})")
    for (b, v) in [(2, 3), (2, 5), (10, 3), (10, 7), (6, 5)]:
        ok(depth_in_base(v, b) is None, f"{v} smooth at {b}?")
        for k in range(2, 7):
            found = any(((n + b**k) // v - n // v) % b != 0
                        for n in range(0, 6 * v))
            ok(found, f"no depth-{k} Lipschitz-violating pair for "
                      f"/{v} base {b}")
        print(f"  base {b}: floor(/{v}) has unit-valuation output "
              f"jumps at input depth 2..6 -- d_b-Lipschitz FAILS")
    # leading metric: scalings are log-isometries (identity
    # |log(u/v x) - log(u/v y)| = |log x - log y|, a property); the
    # exponential's log-Lipschitz ratio diverges.
    prev = 0.0
    import math
    for n in (10, 60, 300):
        ratio = (math.log(2)) / math.log(1 + 1 / n)  # pair (n, n+1)
        ok(ratio > prev, "2^n log-Lipschitz ratio not growing")
        prev = ratio
    print("  leading: scalings are d_log-isometries (identity); "
          "2^n pair-ratio grows ~ n ln 2 (10: %.0f, 60: %.0f, "
          "300: %.0f) -- log-Lipschitz fails" % (
              math.log(2) / math.log(1.1),
              math.log(2) / math.log(1 + 1 / 60),
              math.log(2) / math.log(1 + 1 / 300)))


# ----------------------------------------------------------------- S2
# R1: trailing readability = d_b-Lipschitz, c_min = ceil(log_b Lip_b).

def trailing_determined(f, b, t, c, reps=4, span=3):
    """Exhaustive over residues mod b^{t+c}: f mod b^t constant on
    scanned representatives; returns a collision witness or None."""
    M = b**(t + c)
    for r in range(M):
        base = f(r) % b**t
        for i in range(1, reps):
            for s in (1, span):
                if f(r + i * s * M) % b**t != base:
                    return (r, r + i * s * M)
    return None


def cmin_trailing(f, b, cap, ts=(1, 2)):
    for c in range(cap + 1):
        if all(trailing_determined(f, b, t, c) is None for t in ts):
            return c
    return None


MEASURED_TRAILING = {}


def s2_trailing_criterion():
    print("== S2 R1: THE TRAILING CRITERION ==")
    for (b, v) in [(2, 4), (2, 8), (10, 8), (10, 50), (6, 9), (6, 12)]:
        dv = depth_in_base(v, b)
        cm = cmin_trailing(lambda n, v=v: n // v, b, dv + 2)
        MEASURED_TRAILING[(b, v)] = cm
        ok(cm == dv, f"trailing c_min(floor(/{v})) = {cm} != d_v "
                     f"= {dv} at base {b}")
        w = trailing_determined(lambda n, v=v: n // v, b, 1, dv - 1) \
            if dv >= 1 else None
        ok(dv == 0 or w is not None,
           f"no collision below d_v for /{v} base {b}")
        # phases ride free: same c_min at every shift
        for s in (1, v - 1):
            cs = cmin_trailing(lambda n, v=v, s=s: (n + s) // v, b,
                               dv + 2)
            ok(cs == dv, f"phase {s}/{v} shifts trailing c_min at "
                         f"base {b}: {cs} != {dv}")
        print(f"  base {b}: c_min(floor(/{v})) = {dv} = d_v, phases "
              f"free, collision below threshold")
    for (b, m) in [(2, 3), (2, 7), (10, 3), (10, 21)]:
        cm = cmin_trailing(lambda n, m=m: m * n, b, 2)
        ok(cm == 0, f"x{m} not free at trailing base {b}")
    print("  multiplication x{3,7,21}: c_min = 0 at bases 2, 10 "
          "(nonexpanding = free)")
    for (b, v) in [(2, 3), (10, 7)]:
        for c in range(4):
            w = trailing_determined(lambda n, v=v: n // v, b, 1, c)
            ok(w is not None, f"floor(/{v}) determined at c={c} "
                              f"base {b} (gate breached)")
        print(f"  base {b}: floor(/{v}) collision at every c <= 3 "
              f"-- the rough-denominator gate = non-Lipschitz")


# ----------------------------------------------------------------- S3
# R2: the coset rigidity — redundancy buys the trailing end nothing.

def s3_coset_rigidity():
    print("== S3 R2: THE COSET RIGIDITY ==")
    # (i) COMPLETENESS, the load-bearing lemma: the completions of a
    # depth-t LSB prefix realize EVERY element of the coset
    # V + b^t Z within the tail budget (tails are a full integer
    # interval), so in the length limit the fiber IS the coset and a
    # shared prefix realizes any two values agreeing mod b^t.
    for (b, a, t, T) in [(2, 1, 2, 7), (10, 6, 1, 3)]:
        fibers = {}
        for s in itertools.product(digits(a), repeat=T):
            V = sum(d * b**i for i, d in enumerate(s[:t]))
            tail = sum(d * b**i for i, d in enumerate(s[t:]))
            fibers.setdefault(V, set()).add(V + b**t * tail)
        Rt = a * repunit(b, T - t)
        for V, vals in fibers.items():
            want = set(V + b**t * k for k in range(-Rt, Rt + 1))
            ok(vals == want,
               f"prefix V={V} fiber not the full coset window "
               f"({b},{a})")
        ok(len(set(V % b**t for V in fibers)) == b**t,
           f"missing residue class ({b},{a})")
        print(f"  ({b},{a}): every depth-{t} LSB prefix's length-{T} "
              f"completions = the FULL coset window V + {b**t}k, "
              f"|k| <= {Rt} (completeness; all {b**t} classes "
              f"realized)")
    # (ii) the division gate survives redundancy: two redundant LSB
    # strings sharing a deep prefix whose values collide mod b^{t+c}
    # but floor(/3) separates mod 2 (base 2).
    b, a = 2, 1
    for c in range(4):
        t = 1
        M = b**(t + c)
        found = None
        for n in range(0, 60):
            if (n // 3) % 2 != ((n + M) // 3) % 2:
                found = n
                break
        ok(found is not None, f"no redundant trailing collision "
                              f"for /3 at c={c}")
    print("  (2,1): floor(/3) collision mod 2 from a shared LSB "
          "prefix at every c <= 3 -- the gate SURVIVES redundancy: "
          "redundancy is a leading-end-only door")


# ----------------------------------------------------------------- S4
# R3: the alignment clause carries the gate (log-isometries gated).

def s4_alignment():
    print("== S4 R3: ALIGNMENT CARRIES THE GATE ==")
    b = 10
    for (u, aligned) in [(2, True), (5, True), (4, True),
                         (3, False), (7, False)]:
        # image of cell [M b^j, (M+1) b^j) under x -> u x fits one
        # output cell at scale b^{j + ceil(log_b u) + c}?
        c = 2
        j = 0
        bad = None
        out_scale = 10**(c + 1)
        for M in range(10, 4000):
            lo, hi = u * M, u * (M + 1) - 1
            if lo // out_scale != hi // out_scale:
                bad = M
                break
        if aligned:
            ok(bad is None, f"x{u} straddles at lookahead {c} (M={bad})")
        else:
            ok(bad is not None, f"x{u} never straddles (gate breached)")
    print("  base 10, lookahead 2: x{2,4,5} image cells aligned over "
          "M <= 4000; x{3,7} straddle witnesses found -- the "
          "log-isometries are gated by alignment alone")
    # balanced ternary: centered partition, one clause. x3 aligned:
    # the image of every centered cell sits inside the parent cell.
    R = repunit(3, 2)
    for V in range(-8, 9):
        lo, hi = 3 * (V * 9 - R), 3 * (V * 9 + R)
        ok(lo >= V * 27 - repunit(3, 3) and hi <= V * 27 + repunit(3, 3),
           f"balanced x3 image escapes parent cell at V={V}")
    # x2 straddles: some centered cell's doubled image fits no cell.
    R3 = repunit(3, 3)
    def fits_some_cell(lo, hi, scale, R):
        for K in range(lo // scale - 2, hi // scale + 3):
            if K * scale - R <= lo and hi <= K * scale + R:
                return True
        return False
    bad = None
    for V in range(1, 40):
        lo, hi = 2 * (V * 9 - R), 2 * (V * 9 + R)
        if not fits_some_cell(lo, hi, 27, R3):
            bad = V
            break
    ok(bad is not None, "balanced x2 always fits (gate breached)")
    print("  balanced ternary: x3 cell-contained everywhere scanned; "
          "x2 escape witness at V=%d -- standard and balanced "
          "partitions under ONE alignment clause" % bad)


# ----------------------------------------------------------------- S5
# R4: the rational-slope delay law (the generalized safety game).

def rgame_feasible(b, a, c, u, v, w=0, z=1):
    """0-initialized greatest fixed point of the residual game for
    f(n) = floor((u/v) n + w/z): integer state r = L R, L = lcm(v,z),
    flushable iff |floor(r/L)| <= a R_c."""
    L = v * z // gcd(v, z)
    F = a * repunit(b, c)
    win = set(range(-F * L, (F + 1) * L))
    ok(L * w % z == 0, "phase scaling not integral")
    # R' = bR + (u/v)x - (b-1)(w/z) - e b^c keeps the CONSTANT phase
    # constant (multiplying the whole invariant by b would scale it).
    phc = (b - 1) * (L * w // z)
    inj = [L * u * x // v - phc for x in digits(a)]
    shift = L * b**c
    changed = True
    while changed:
        changed = False
        for r in list(win):
            for s in inj:
                pre = b * r + s
                if not any(pre - e * shift in win for e in digits(a)):
                    win.discard(r)
                    changed = True
                    break
    return (L * w // z) in win


def cmin_rational(b, a, u, v, w=0, z=1, cap=8):
    for c in range(cap + 1):
        if rgame_feasible(b, a, c, u, v, w, z):
            return c
    return None


def pred_cmin(b, a, u, v):
    """The frozen closed form: pure b-power slopes at max(0, s);
    otherwise max(0, ceil(log_b(2au/(v(2a-b+1))))); None when the
    margin is nonpositive (non-redundant) and the slope unaligned."""
    s, uu, vv = 0, u, v
    while uu % b == 0:
        uu //= b
        s += 1
    while vv % b == 0:
        vv //= b
        s -= 1
    if uu == 1 and vv == 1:
        return max(0, s)
    marg = 2 * a - b + 1
    if marg <= 0:
        return None
    c = 0
    while b**c * v * marg < 2 * a * u:
        c += 1
    return max(0, c)


def s5_rational_delay():
    print("== S5 R4: THE RATIONAL-SLOPE DELAY LAW ==")
    # positive control PC1: the integer table reproduces.
    for (b, a, m, want) in [(2, 1, 3, 3), (2, 1, 4, 2),
                            (10, 6, 2, 1), (10, 6, 10, 1)]:
        ok(cmin_rational(b, a, m, 1) == want,
           f"PC1: x{m} at ({b},{a}) != {want}")
    print("  PC1: integer delays reproduce ((2,1) x3=3 x4=2; "
          "(10,6) x2=1 x10=1)")
    scan = [(2, 1, [(1, 3), (2, 3), (3, 5), (5, 3), (1, 7), (7, 5),
                    (1, 2), (1, 4)]),
            (4, 2, [(1, 3), (3, 5), (5, 2)]),
            (10, 6, [(1, 3), (7, 3), (3, 5), (3, 7), (21, 5), (1, 2)])]
    for (b, a, uvs) in scan:
        marg = 2 * a - b + 1
        for (u, v) in uvs:
            cu = 0
            while b**cu * v * marg < 2 * a * u:
                cu += 1
            ok(rgame_feasible(b, a, cu, u, v),
               f"K1: {u}/{v} infeasible at sufficient c={cu} ({b},{a})")
            ok(2 * a * repunit(b, cu) >= b**cu or cu == 0,
               f"flush margin fails at ({b},{a},{cu})")
            cm = cmin_rational(b, a, u, v)
            pd = pred_cmin(b, a, u, v)
            tag = "=" if cm == pd else "  != predicted"
            print(f"  ({b},{a}) slope {u}/{v}: c_min = {cm} "
                  f"(predicted {pd}) {tag}")
            ok(cm is not None and cm <= cu,
               f"c_min exceeds sufficient bound at ({b},{a}) {u}/{v}")
    # the hand-played spots, asserted exactly
    for (b, a, u, v, want) in [(2, 1, 1, 3, 0), (2, 1, 3, 5, 1),
                               (2, 1, 5, 3, 2), (10, 6, 1, 3, 1),
                               (10, 6, 7, 3, 1), (10, 6, 3, 5, 1),
                               (10, 6, 21, 5, 2), (2, 1, 1, 2, 0)]:
        ok(cmin_rational(b, a, u, v) == want,
           f"hand spot {u}/{v} at ({b},{a}) != {want}")
    print("  hand spots exact: division by 3 at redundant binary has "
          "delay ZERO; both radical gates dissolved, size-only price")
    # the phase never RAISES the delay at a redundant window, and
    # the window-shaped phase (round, for symmetric digit sets) can
    # save one digit: the alignment clause's ghost prices the phase.
    for (b, a, u, v) in [(2, 1, 1, 3), (2, 1, 3, 5), (2, 1, 5, 3),
                         (10, 6, 1, 3), (10, 6, 7, 3), (10, 6, 21, 5)]:
        bare = cmin_rational(b, a, u, v)
        for (w, z) in [(1, 2), (1, 3), (2, 3), (1, 7)]:
            cp = cmin_rational(b, a, u, v, w, z)
            ok(cp is not None and cp <= bare,
               f"phase {w}/{z} raises c_min at ({b},{a}) {u}/{v}")
    for (b, a, u, v, saved) in [(2, 1, 3, 5, 0), (10, 6, 1, 3, 0),
                                (10, 6, 7, 3, 1), (2, 1, 5, 3, 2)]:
        ok(cmin_rational(b, a, u, v, 1, 2) == saved,
           f"round phase at ({b},{a}) {u}/{v} != {saved}")
    print("  phases never raise the delay at the redundant windows "
          "(24 cells); the round phase saves one digit where the "
          "bare floor misaligns ((2,1) 3/5: 1 -> 0; (10,6) 1/3: "
          "1 -> 0) and never costs -- the phase is priced by cell "
          "shape, not walled")
    # PC3 + P-E: the margin-zero (balanced, non-redundant) controls.
    # The frozen P-E spot 'slope 1/3 at c = 1' is REFUTED: floor is
    # walled at every scanned lookahead, and THE PHASE-SHAPE LAW
    # replaces it — the window's free rounding phase is its own cell
    # shape: round-to-nearest at the centered partitions (denominator
    # free for every scanned ODD v), floor at the standard partition
    # (explore_dual_locality.py), even v tie-walled at balanced sets.
    for (b, a) in [(3, 1), (5, 2)]:
        for v in (3, 9, 5 if b == 3 else 7):
            ok(cmin_rational(b, a, 1, v, 1, 2, cap=6) == 0,
               f"round(n/{v}) not free at ({b},{a})")
            ok(cmin_rational(b, a, 1, v, cap=6) is None,
               f"floor(n/{v}) local at ({b},{a})")
        ok(cmin_rational(b, a, 1, 2, 1, 2, cap=6) is None,
           f"round(n/2) local at ({b},{a}) (tie wall breached)")
        ok(cmin_rational(b, a, 2, 3, 1, 2, cap=6) is None,
           f"round(2n/3) local at ({b},{a}) (numerator gate "
           f"breached under round)")
    ok(cmin_rational(3, 1, 1, 15, 1, 2, cap=6) == 0,
       "round(n/15) not free at (3,1)")
    ok(cmin_rational(3, 1, 1, 3, 2, 3, cap=6) is None,
       "ceil(n/3) local at (3,1)")
    # uniqueness swept across ALL phase tip-classes (a phase class =
    # the set of w/z tipping the same fractional parts of n/v): v = 3
    # has classes [0,1/3) floor, [1/3,2/3) round, [2/3,1) ceil — all
    # three tested above at both systems; v = 5 at (3,1) has five,
    # and only the round class [2/5,3/5) is free.
    for (w, z) in [(1, 5), (7, 10), (9, 10)]:
        ok(cmin_rational(3, 1, 1, 5, w, z, cap=6) is None,
           f"off-round phase class {w}/{z} of n/5 local at (3,1)")
    ok(cmin_rational(5, 2, 1, 3, 5, 6, cap=6) is None,
       "ceil-class phase 5/6 of n/3 local at (5,2)")
    for (u, v, want) in [(3, 1, 1), (9, 1, 2)]:
        ok(cmin_rational(3, 1, u, v, cap=6) == want,
           f"PC3: x{u} at (3,1) != {want}")
    ok(cmin_rational(5, 2, 5, 1, cap=6) == 1 and
       cmin_rational(5, 2, 25, 1, cap=6) == 2,
       "PC3: b-power schedule shift off at (5,2)")
    for (b, a, u) in [(3, 1, 2), (5, 2, 2), (5, 2, 3)]:
        ok(cmin_rational(b, a, u, 1, cap=6) is None,
           f"PC3: x{u} feasible at ({b},{a})")
    ok(cmin_rational(3, 1, 2, 5, cap=6) is None,
       "PC3: 2/5 feasible at (3,1)")
    print("  margin-zero controls (3,1) and (5,2): THE PHASE-SHAPE "
          "LAW -- round(n/v) exactly local at c = 0 for every "
          "scanned odd v (3, 5, 9, 15 | 3, 7, 9), floor and ceil "
          "walled at every scanned lookahead, even v walled in "
          "every scanned phase (the ties sit on cell boundaries), "
          "round(2n/3) walled (the numerator gate persists under "
          "the aligned phase); x3=1 x9=2 x5=1 x25=2 (the schedule "
          "shift), x2/x3/2-per-5 infeasible: the numerator gate "
          "reproduced at both balanced systems")


# ----------------------------------------------------------------- S6
# The hedge: |x| local at the redundant leading end; sign walled.

def prefix_game_feasible(b, a, c, f, T, To):
    """Backward induction: read T digits MSB-first (adversary), emit
    To digits with delay c (emitted count at k read digits =
    max(0, min(To, k + To - T - c))); emission legal iff every
    completion's f-value stays reachable from the emitted prefix.
    Leaf re-checks reachability from the definition."""
    from functools import lru_cache
    emitted_at = [max(0, min(To, k + To - T - c)) for k in range(T + 1)]

    @lru_cache(maxsize=None)
    def feas(k, V, W):
        if k == T:
            j = To - emitted_at[k]
            return abs(f(V) - W * b**j) <= a * repunit(b, j)
        for x in digits(a):
            V2 = b * V + x
            need = emitted_at[k + 1] - emitted_at[k]
            cands = [W] if need == 0 else \
                [b * W + e for e in digits(a)]
            if not any(feas(k + 1, V2, W2) for W2 in cands):
                return False
        return True

    # digits owed before the first read are a free (blind) choice,
    # not forced to zero
    starts = [0]
    for _ in range(emitted_at[0]):
        starts = [b * W + e for W in starts for e in digits(a)]
    return any(feas(0, 0, W0) for W0 in starts)


def s6_hedge():
    print("== S6 THE HEDGE (|x|) ==")
    # PC2: the prefix-tree game agrees with the rational game where
    # both run (identity and x2 at (2,1)).
    ok(prefix_game_feasible(2, 1, 0, lambda n: n, 6, 6),
       "PC2: identity infeasible at c=0")
    ok(prefix_game_feasible(2, 1, 1, lambda n: 2 * n, 6, 7),
       "PC2: x2 infeasible at c=1")
    ok(not prefix_game_feasible(2, 1, 0, lambda n: 2 * n, 6, 7),
       "PC2: x2 feasible at c=0")
    print("  PC2: prefix-tree game reproduces the rational game "
          "(identity c=0; x2 c=1 not 0)")
    got = None
    for c in range(3):
        if prefix_game_feasible(2, 1, c, abs, 8, 8):
            got = c
            break
    ok(got is not None, "K3: |x| infeasible through c=2 at (2,1)")
    got10 = None
    for c in range(3):
        if prefix_game_feasible(10, 6, c, abs, 4, 4):
            got10 = c
            break
    ok(got10 is not None, "K3: |x| infeasible through c=2 at (10,6)")
    print(f"  |x| exactly local: c_min = {got} at (2,1) [T=8], "
          f"{got10} at (10,6) [T=4]")
    # the order-wall witness, re-verified from the definition: +1 and
    # -1 both complete the all-zero depth-j prefix (they lie in its
    # fiber) and their outputs differ in the SIGN component of every
    # window — one input window, two output windows.
    for j in (3, 6):
        in_fiber = lambda n, j=j: abs(n) <= 1 * repunit(2, j)
        ok(in_fiber(1) and in_fiber(-1) and (1 > 0) != (-1 > 0),
           "order-wall witness fails at the all-zero prefix")
    print("  sign: the all-zero prefix admits both signs at every "
          "depth (the order wall stands, explore_dual_redundant.py) "
          "-- a sign-symmetric map computed without reading the sign")
    # |x| trailing-dead: |x| mod b^t collides on a shared LSB prefix
    # (depth 2 — the depth-1 base-2 residue is the one sign-blind
    # exception, |-x| == x mod 2).
    for c in range(4):
        M = 2**(2 + c)
        found = any(abs(n) % 4 != abs(n - k * M) % 4
                    for n in range(1, M) for k in (1, 2, 3))
        ok(found, f"|x| trailing-determined at c={c}")
    ok(all(abs(n) % 2 == abs(n - 2) % 2 for n in range(-8, 9)),
       "parity not sign-blind")
    print("  |x| at the trailing end: collision mod 4 at every "
          "c <= 3 (the sign is an archimedean read; parity alone is "
          "sign-blind) -- the hedge is leading-only")


# ----------------------------------------------------------------- S7
# The pricing arithmetic: MAX over places vs SUM over places.

def s7_pricing():
    print("== S7 THE PRICING ARITHMETIC ==")
    import math
    for (b, v) in [(2, 8), (10, 50), (6, 12), (10, 8)]:
        fv, fb = factorize(v), factorize(b)
        mx = max(-(-fv[p] // fb[p]) for p in fv)
        ok(MEASURED_TRAILING[(b, v)] == mx,
           f"MEASURED trailing price != MAX-formula at {v},{b}")
    print("  trailing: MEASURED price(/v) = MAX_p ceil(v_p(v)/v_p(b))"
          " (v=8 base 2; v=50,8 base 10; v=12 base 6; the "
          "ultrametric prices by max)")
    for (b, a, u) in [(2, 1, 6), (2, 1, 12), (10, 6, 21)]:
        fu = factorize(u)
        lg = sum(e * math.log(p, b) for p, e in fu.items())
        ok(abs(lg - math.log(u, b)) < 1e-9, "product formula off")
        pd = pred_cmin(b, a, u, 1)
        marg = 2 * a - b + 1
        ok(b**(pd - 1) * marg < 2 * a * u <= b**pd * marg or pd == 0,
           f"leading price bracket off at x{u} ({b},{a})")
        print(f"  leading ({b},{a}): price(x{u}) = {pd} = "
              f"ceil(SUM_p v_p log_b p + margin) "
              f"(log_{b} {u} = {lg:.3f})")
    print("  the archimedean window prices by SUM over places (the "
          "product formula), the ultrametric window by MAX -- each "
          "pole in its own metric's arithmetic")


# ----------------------------------------------------------------- S8
# The kill specimens: the exponential split + scale confinement.

def s8_specimens():
    print("== S8 THE SPECIMENS ==")
    # 2^n leading-dead at any redundancy: a deep input fiber whose
    # image spans several exponents fits no output cell.
    lo, hi = 10240, 10249  # the depth-4 base-10 fiber [1024*10, +10)
    span = (len(str(2**hi)) - 1) - (len(str(2**lo)) - 1)
    ok(span >= 2, "2^n image exponent span too small")
    print("  2^n leading: fiber [10240,10249] spans %d output "
          "exponents (exact; no window at any lookahead) -- dead at "
          "every redundancy" % (span + 1))
    # trailing at b=10: on the SATURATED range n >= t, readable at
    # c=1 (period 4*5^{t-1} | 10^{t+1}); collision at c=0; and the
    # sub-threshold n < t are a genuine exception family (the 2-column
    # shallow ramp), so the readability claim carries that scope.
    b = 10
    for t in (1, 2, 3):
        M = 10**(t + 1)
        for n in range(t + 1, t + 40, 7):
            ok(pow(2, n, 10**t) == pow(2, n + M, 10**t) ==
               pow(2, n + 3 * M, 10**t),
               f"2^n not determined mod 10^{t} by n mod 10^{t+1}")
    ok(pow(2, 3, 10) != pow(2, 13, 10),
       "2^n determined at c=0 (collision missing)")
    for t in (2, 3):
        ok(pow(2, 1, 2**t) != pow(2, 1 + 10**(t + 1), 2**t),
           f"no shallow 2-column collision at t={t}")
    print("  2^n trailing, base 10: readable at c_min = 1 ON THE "
          "SATURATED RANGE n >= t (ord(2 mod 5^t) = 4*5^{t-1} | "
          "10^{t+1}; c=0 collision 2^3=8 vs 2^13=..2); below "
          "saturation the 2-column still ramps (2^1 vs 2^{1+10^{t+1}}"
          " differ mod 2^t) -- the shallow-ramp exception is the "
          "residue wall's shallow leak in mirror")
    for c in range(4):
        ok(pow(2, 1, 3) != pow(2, 1 + 3**(1 + c), 3),
           f"2^n mod 3 determined at c={c}")
    print("  2^n trailing, base 3: collision at every c <= 3 (the "
          "order carries the factor 2 that rad(3) lacks) -- the "
          "exponential's trailing home is gated by its order tower")
    # scale confinement: two-slope piecewise map.
    TH = 5
    pw = lambda n: n if n < TH else 2 * n - TH
    for c in range(4):
        M = 2**(1 + c)
        found = any((pw(n + M) - pw(n)) % 2 != 0
                    for n in range(0, TH))
        ok(found, f"piecewise trailing-determined at c={c}")
    got = None
    for c in range(4):
        if prefix_game_feasible(2, 1, c, pw, 7, 8):
            got = c
            break
    ok(got is not None, "piecewise infeasible through c=3 at (2,1)")
    print(f"  two-slope piecewise (slopes 1,2 at threshold {TH}): "
          f"trailing collision at every c <= 3 (unbounded AP fibers "
          f"mix the pieces), redundant-leading local at c = {got} "
          f"-- piecewise structure is free at the scale-confined "
          f"end, fatal at the all-scales end")


def main():
    s1_metric_table()
    s2_trailing_criterion()
    s3_coset_rigidity()
    s4_alignment()
    s5_rational_delay()
    s6_hedge()
    s7_pricing()
    s8_specimens()
    print(f"ALL CHECKS PASS ({CHECKS[0]} checks)")


if __name__ == "__main__":
    main()
