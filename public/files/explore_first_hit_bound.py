"""
explore_first_hit_bound.py -- A COMPUTABLE FIRST-HIT BOUND FOR THE
SUPER-CRITICAL CELL: derive one, or name the step that blocks it.
(Sibling of explore_super_critical.py, whose landing word, gap law and
block identity this script reuses, and of explore_supply_tameness.py,
whose coverage lemma turns out to reach half of what the sibling swept.)

THE SETTING. For the growing-window machine on a sublinear modulus
supply, DECIDABILITY = RATE + SUPPLY TAMENESS, and the classification
of supplies runs on the inverse supply M(d) = max{g : m(g) <= d}. Four
cells: quasi-polynomial M is tame by offset compression; SLOW supplies
-- any m growing slower than every g^(1/2 - eps), which is M(d) growing
faster than every d^(2 + eps) -- are tame by THE COVERAGE LEMMA (one
attained gap value d coprime to L with multiplicity mu(d) >= L walks its
window across all of Z/L); value-starved supplies are the oracle
channel; and the SUPER-CRITICAL band, m faster than sqrt and still
sublinear, M = floor(d^c) at NON-INTEGER c, is the open cell. The
sibling restated what is open there in the decider's own terms: is
there a COMPUTABLE bound B(L) with every class mod L hit by landing
B(L)? It measured the first-hit index F(L) at 0.63 to 1.46 times L H_L
and proved nothing about it.

THE OBJECT (the sibling's conventions, re-derived from its engine).
  THE RIDER      v := (v + 1) mod max(2, m(g)), one pass per tick, the
                 frontier g = t + 2 (pregrow 2).
  A LANDING      a pass t at which v returns to 0.
  WINDOW TOP     top(d) = M(d) - 2;  e(d) = top(d) - d.
  THE STEP       from a landing at t the next gap is D(t) = the least d
                 with e(d) >= t, and the next landing is t + D(t). So
                 landing n+1 sits in window d_n: top(d_n - 1) + 1 <
                 t_{n+1} <= top(d_n), and every landing with gap d lies
                 in (e(d-1), e(d)].
  WINDOW LENGTH  w(d) = top(d) - top(d-1) = M(d) - M(d-1).
  MULTIPLICITY   mu(d) = the number of landings with gap d.
  THE OFFSET     o_n = e(d_n) - t_n, so that t_{n+1} = top(d_n) - o_n
                 with 0 <= o_n <= w(d_n) - 2.
  THE SUPPLIES   M(d) = floor(d^c) at c = p/q, exact by integer root.

THE HAND ATTACK (on paper before any engine code).

(1) WHERE THE BAND'S MULTIPLICITY SITS, EXACTLY. The landings with gap
d are the orbit's points in (e(d-1), e(d)], an interval of w(d) - 1
integers walked in steps of d. So mu(d) <= ceil((w(d) - 1) / d), and
     w(d) = floor(d^c) - floor((d-1)^c) <= d^c - (d-1)^c + 1
          <= c d^(c-1) + 1.
For c < 2 that is below d from an explicit d_1 on, so mu(d) <= 1 at
every d >= d_1: no window is walked twice and the coverage lemma has no
hypothesis at any L >= 2 beyond d_1. For c > 2 the SAME computation
runs the other way: w(d) >= d^c - (d-1)^c - 1 >= c (d-1)^(c-1) - 1,
which exceeds d from an explicit d_0 on, and then
  (a) window d is ATTAINED: from a landing t <= e(d-1) the step D(t) is
      at most d - 1, and an interval of w(d) - 1 >= d - 1 integers
      cannot be jumped;
  (b) mu(d) >= floor((w(d) - 1) / d), since a progression of step d
      that meets an interval of that many integers has at least that
      many points in it;
so mu(d) -> infinity along EVERY d >= d_0, and for any L the least
d* >= d_0 coprime to L with floor((w(d*) - 1) / d*) >= L has its window
alone cover Z/L. THE COMPUTABLE BOUND, at every c > 2: every class mod
L is hit by the last landing with gap d*(L), a landing the supply
locates without enumerating anything (it is at most top(d*)), and
B(L) = its index. The sibling swept four powers and called all four the
cell; two of them, c = 5/2 and 7/3, sit ABOVE 2, so the coverage lemma
already decides them and "mu below 1 across the whole band" was written
at c = 3/2 and carried to powers where it is false. The open cell is
c in (1, 2) and nothing else -- the classification's own words ("faster
than sqrt, still sublinear") always said so.

(2) WHAT A DERIVATION INSIDE (1, 2) HAS TO WORK WITH, and why each
input fails alone. Three inputs are available.
  MULTIPLICITY is dead by (1): mu <= 1 beyond d_1.
  THE BLOCK STRUCTURE -- inside a maximal run of constant gap
  difference delta the landings are t_j = t_0 + j d_0 + delta j(j+1)/2,
  blocks are short and delta jitters by at most 2 per step -- cannot
  force coverage by counting, because the class of words it defines
  CONTAINS members that miss classes: a block continued with its jitter
  frozen at zero is a quadratic in j, and a quadratic with leading
  coefficient nonzero mod an odd prime p takes exactly (p + 1) / 2
  values mod p. So any statement of the form "the walk of (d_0, delta)
  mod L across consecutive blocks sweeps every class within N blocks"
  is FALSE over the class the block structure defines, and coverage --
  if it holds -- is carried by the jitter, that is by WHICH of the two
  candidate increments the offset selects at each block boundary.
  THE OFFSET is the live input, and it is exactly where the arithmetic
  is. t_{n+1} = top(d_n) - o_n, so the residue mod L is the residue of
  the offset (shifted by floor(d_n^c) - 2), and the offset is the
  orbit's position inside its window measured from the top, on a scale
  w(d_n) that grows without bound. Its recurrence is exact and
  elementary --
     o_{n+1} = o_n - d_n + sum_{d_n < d <= d_{n+1}} (w(d) - 1),
  with d_{n+1} the least value making the right side nonnegative -- a
  countdown by the gap and a refill by window lengths, the wrap-word
  offset recurrence of the sqrt pole with the refill no longer
  polynomial. At the sqrt pole the refill is 2d - 2 against a countdown
  of d and the offset COMPRESSES to a closed form; here the refill is
  the run of floor(d^c) differences across the skipped windows, and
  o_n mod L reads the fractional structure of d^c at the selected d
  at resolution 1/w(d_n). The step no elementary argument supplies:
  that the offset's residue mod L, along the orbit's self-selected
  sparse set of windows, takes every value -- a joint distribution
  statement about {d^c} and the orbit's position, which is
  equidistribution input and not a counting statement. The sibling's
  "L H_L fits in range" was the shadow of this: the residue behaves as
  a fresh draw because the offset is a fresh digit at each landing.

(3) THE SHARPENING, which the doc will carry. A computable B with every
class hit by B(L) is the SAME statement as universal coverage: if every
class is hit at every L then F(L) is computable by enumeration (the
search terminates) and B = F serves; conversely such a B is universal
coverage. So the cell's open question is a coverage THEOREM on
c in (1, 2), and its quantitative flavour -- whether F sits at L H_L
or at L^3 -- is not what is asked. A proof needs the offset's
equidistribution (2); any effective form of it gives a bound and the
bare existence form already gives the decider (answer YES).

TRANSPLANT FLAGS. T1: the coverage lemma and the sqrt pole's offset
recurrence were derived in the siblings at their own supplies; here
the lemma is applied at c > 2 exactly as stated and the recurrence is
re-derived from the step rule above. T2: the jitter bound (|change in
delta| <= 2) is the sibling's measurement at c = 3/2 and is not a
hypothesis of anything below.

PREDICTIONS (fixed before the run; each adjudicated separately; each
names what the rig PRINTS).
  PR1  CONTROL -- THE BOUND MUST NOT EXIST AT THE SQRT POLE. On
       M = d^2 every attained value has mu(d) <= 2 over 10^5 landings,
       so for every L in 3..60 no attained d coprime to L has
       mu(d) >= L, and class 4 mod 6 is never hit. On the starved supply
       no attained value is coprime to 6. Falsifier: either miss.
  PR2  THE SEAM -- c > 2 IS THE SLOW SIDE. At c = 5/2, 7/3, 9/4, with
       d_0 the least d at which c (d-1)^(c-1) - 1 >= d (checked in exact
       rational arithmetic and monotone from there), every d >= d_0 up
       to the horizon's last complete window is attained, and
       mu(d) >= floor((w(d) - 1) / d) at each. Falsifier: a skipped
       value or a window under its floor.
  PR3  THE BOUND, PRINTED BESIDE THE FIRST HIT. At the same three
       powers and every L = 2..60: the landings with gap d*(L) cover
       Z/L by themselves, and F(L) <= B(L) with B(L) the index of the
       last landing with gap d*(L). Falsifier: any L at either clause.
       Printed: d*(L), B(L), B(L)/F(L) at every tenth L and at 60 --
       the bound is expected to grow like L^((c-1)/(c-2)) against F's
       L log L, so the ratio should climb; no band is placed on it.
  PR4  THE BAND -- mu <= 1. At c = 4/3, 3/2, 5/3, 7/4, with d_1 the
       least d at which c d^(c-1) + 1 <= d (exact rational check),
       mu(d) <= 1 at every attained d >= d_1 over 2 x 10^4 landings,
       and for every L = 2..60 no attained d coprime to L has
       mu(d) >= L. Falsifier: a window walked twice beyond d_1, or a
       qualifying window at some L -- the latter would be a computable
       bound at that L and is reported as one.
  PR5  THE BLOCK STRUCTURE DOES NOT FORCE COVERAGE. For the first
       1,000 blocks of the c = 3/2 word, each block continued with its
       jitter frozen (the quadratic t_0 + j d_0 + delta j(j+1)/2 over
       j = 0..L^2) misses exactly (p - 1) / 2 classes mod p at every
       odd prime p <= 60 not dividing delta. Falsifier: any block-prime
       pair off that count. (A property; it is checked because the
       aimed derivation was written over exactly this class.)
  PR6  THE RESIDUE READS THE OFFSET. At c = 3/2 over 10^5 landings:
       t_{n+1} = top(d_n) - o_n with 0 <= o_n <= w(d_n) - 2 at every n
       (identity), and the offset recurrence of (2) reproduces o_{n+1}
       and d_{n+1} from (o_n, d_n) at every n (identity). Measured, not
       predicted beyond a band: the census of o_n mod L over the
       horizon at L = 6 and L = 60 has every class within 10% of
       uniform, and theta_n = o_n / (w(d_n) - 1) has Kolmogorov
       distance from uniform on [0, 1) below 0.02. Falsifier for the
       identities: one landing. The census bands are observation-tier
       and their failure is reported, not read as a kill.
  PR7  THE HUNT WIDENED INTO THE BAND'S INTERIOR. At c = 4/3 and 7/4,
       every class mod every L = 2..60 is hit within 2 x 10^4
       landings; the last first-hit landing is printed. Falsifier: a
       never-hit class -- an obstruction, the larger find.

RESOURCE ENVELOPE. 10^5 landings at c = 3/2 and the two controls; 10^5
at c = 5/2, 7/3, 9/4 (gap values to ~10^4 there, since mu grows);
2 x 10^4 at the four powers inside the band, where d reaches ~10^13 at
c = 4/3 and the integer roots run on ~170-bit ints. Estimate under
60 s and under 200 MB; peak reported under memwatch.

FINDINGS (entered after the run, from printed output).

THE CELL WAS HALF THE WIDTH IT WAS FILED AT, and the half that leaves
is decided by the lemma the classification already owned. Above c = 2
every window is attained and multiplicity is unbounded -- at c = 5/2,
7/3 and 9/4 no value in [d_0, horizon) is skipped, d_0 = 3 at all
three, and mu(d) >= floor((w(d) - 1) / d) at every window (mu = 69 at
d = 767 for c = 5/2; 28 at d = 1849 for 7/3; 17 against a floor of 16 at
d = 3125 for 9/4). So the coverage lemma's bound EXISTS and is computed
from M alone: T(L) = top(d*(L)), d*(L) the first value coprime to L at
or above the exact-rational threshold c (d-1)^(c-1) - 2 >= L d, and the
last first-hit landing t_F(L) sits under T(L) at every L = 2..60 at all
three powers; wherever the horizon reaches d*(L) -- 59, 35 and 19 of
the 59 moduli -- that window's own landings cover Z/L by themselves
and F(L) <= B(L), the index of its last landing. The bound is
enormous beside the first hit -- at c = 5/2, L = 60: d* = 581, T =
8.14 x 10^6 against t_F = 5,463, B = 23,278 against F = 277 -- and it
grows at the hand exponent, T ~ L^(c/(c-2)): log2(T(60)/T(30)) = 4.91,
6.99, 9.00 against 5, 7, 9. Which is the point: a computable bound
is a coverage THEOREM and nothing about its size is asked. The
sibling's "mu below 1 across the whole band" was written at c = 3/2
and is false at 5/2 and 7/3, so its four-power obstruction hunt was two
powers inside the cell and two on the slow side. The open cell is
c in (1, 2), which is what "faster than sqrt, still sublinear" said.

INSIDE (1, 2) THE THREE INPUTS FAIL AS DERIVED, and the failing step is
named. mu(d) <= 1 at every attained d beyond d_1 (d_1 = 3, 4, 8, 13 at
c = 4/3, 3/2, 5/3, 7/4; the attained values below d_1 number 0, 1, 4,
10 and none is walked twice), and no attained value coprime to any
L = 2..60 has mu >= L at any of the four powers: the coverage lemma has
no hypothesis anywhere in the band. The block structure cannot carry
coverage by counting: over the first 1,000 blocks of the c = 3/2 word
(mean 2.94 landings, max 6) every jitter-free continuation misses
exactly (p - 1)/2 classes mod p at every odd prime p <= 60 not dividing
its delta, 14,809 block-prime pairs and none off -- the class of words
the block structure defines contains members that miss classes, so a
statement over block parameters alone is false and coverage, where it
holds, is carried by the jitter, which is the offset's choice. And the
offset is the whole of the arithmetic: t_{n+1} = top(d_n) - o_n with
0 <= o_n <= w(d_n) - 2 at all 99,998 landings, and the countdown-and-
refill recurrence -- o_{n+1} = o_n - d_n + top(d) - top(d_n) - (d -
d_n) at the least d making it nonnegative -- reproduces (d_{n+1},
o_{n+1}) at every one. What a proof needs is that o_n mod L takes
every value along the orbit's own sparse set of windows. It does, as
far as measured: the census of o_n mod 6 is 16,881 / 16,554 / 16,669 /
16,642 / 16,652 / 16,600 (every class within 1.3% of uniform), mod 60
within 5.4%, and the normalized offset theta_n = o_n / (w(d_n) - 1) is
uniform on [0, 1) to Kolmogorov distance 0.0030 with mean 0.4989. That
is the step: the offset is a fresh digit of the orbit's position at
resolution 1/w(d_n) at every landing, its residue is the landing's
residue, and no elementary argument makes a digit at a growing
resolution take every value -- it is equidistribution input, on the
selected windows and not on all of them. The census the decider's
first-hit reading rode on is this digit's; the coupon-collector law
was its shadow.

THE HUNT WIDENED INTO THE BAND'S INTERIOR finds nothing: at c = 4/3
and 7/4 every class mod every L = 2..60 is hit within 2 x 10^4
landings, the last first-hit at landing 363 and 450, which with the
sibling's 410 and 365 at 3/2 and 5/3 puts the census at four powers
INSIDE the cell and no obstruction at any.

THE CONTROL held first: on the sqrt pole the maximum multiplicity over
50,007 complete windows is 2, no attained coprime value has mu >= L at
any L in 3..60, and 4 mod 6 is never hit -- the lemma finds nothing
beside the known obstruction, as it must; on the starved supply all
1,671 attained values are multiples of 6.

THREE ENGINE ERRORS, all caught by the run. PR3 was frozen on the
INDEX bound B(L), which needs the landings enumerated out to d*(L) --
at c = 9/4, L = 60 that is 10^7 landings; the lemma's bound is the
TIME top(d*), computable from M alone, which is how the tameness rig
states it, and the index form is checked where the horizon reaches it.
The scan for d*(L) walked one value at a time and ran past its
estimate by more than 2x at c = 9/4 (killed; a binary search on the
rigorous threshold replaced it, so d*(L) is the first coprime value at
or above that threshold and not the least qualifying value, which the
bound never needed). And S4 read the offset one landing out of phase:
the word's tuple (t, d) carries the gap that PRODUCED t, the sibling's
own convention block says so, and the first run failed the identity at
every landing -- the offset of t is read against the landing before it.

RUN RECORD. 32/32 CHECKS PASS, 7.5 s wall clock; 38.1 MB peak working
set against the 512 MB ceiling (memwatch). Predictions as frozen: PR1
confirmed; PR2 confirmed at all three powers; PR3 confirmed on the
time bound at every L and on the index bound where reached, after the
freeze error above; PR4 confirmed at all four powers; PR5 confirmed;
PR6 identities confirmed after the phase error, census and Kolmogorov
bands met; PR7 confirmed.
"""

import math
import os
import sys
from fractions import Fraction

os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from explore_super_critical import (  # noqa: E402
    M_power, M_sqrt, M_starved, landings_direct, blocks, iroot)

PREGROW = 2
CHECKS = [0, 0]


def ok(cond, msg):
    CHECKS[0] += 1
    if not cond:
        CHECKS[1] += 1
    print(("  PASS  " if cond else "  FAIL  ") + msg)


def note(msg):
    print("        " + msg)


# ---------------------------------------------------------------- #
# window statistics from a landing word                             #
# ---------------------------------------------------------------- #

def window_table(word):
    """mu(d) and the index of the last landing with gap d, over the
    word's attained values. The last attained value's window may be
    incomplete at the horizon; callers stop one short of it."""
    mu = {}
    last_index = {}
    for i, (t, d) in enumerate(word):
        mu[d] = mu.get(d, 0) + 1
        last_index[d] = i + 1
    return mu, last_index


def w_len(M, d):
    return M(d) - M(d - 1)


def first_hit_index(word, L):
    seen = set()
    for i, (t, _) in enumerate(word):
        seen.add(t % L)
        if len(seen) == L:
            return i + 1
    return None


def never_hit(word, L):
    seen = set(t % L for t, _ in word)
    return sorted(set(range(L)) - seen)


# ---------------------------------------------------------------- #
# the two thresholds, in exact rational arithmetic                  #
# ---------------------------------------------------------------- #

def d0_slow(p, q):
    """least d >= 2 with c (d-1)^(c-1) - 1 >= d at c = p/q > 2, i.e.
    p^q (d-1)^(p-q) >= q^q (d+1)^q; monotone from there since the left
    side's growth exponent p - q exceeds the right side's q."""
    d = 2
    while p ** q * (d - 1) ** (p - q) < q ** q * (d + 1) ** q:
        d += 1
    return d


def d1_band(p, q):
    """least d >= 2 with c d^(c-1) + 1 <= d at c = p/q in (1, 2), i.e.
    p^q d^(p-q) <= q^q (d-1)^q; monotone from there since p - q < q."""
    d = 2
    while p ** q * d ** (p - q) > q ** q * (d - 1) ** q:
        d += 1
    return d


def d_star_of(p, q, d0, L):
    """The lemma's value at c = p/q > 2: floor((w(d) - 1) / d) >= L
    holds wherever c (d-1)^(c-1) - 2 >= L d, i.e. p^q (d-1)^(p-q) >=
    q^q (L d + 2)^q, a condition monotone in d from d0 on (the left
    side's exponent p - q exceeds the right side's q); its threshold
    is found by binary search, and the first value at or above it
    coprime to L -- at most L steps up -- is d*(L). Nothing here
    enumerates a landing."""
    def holds(d):
        return p ** q * (d - 1) ** (p - q) >= q ** q * (L * d + 2) ** q
    hi = max(d0, 2)
    while not holds(hi):
        hi *= 2
    lo = d0
    while lo < hi:
        mid = (lo + hi) // 2
        if holds(mid):
            hi = mid
        else:
            lo = mid + 1
    d = lo
    while math.gcd(d, L) != 1:
        d += 1
    return d


# ---------------------------------------------------------------- #
# S0 -- the control: no bound at the sqrt pole, none when starved    #
# ---------------------------------------------------------------- #

def s0_control():
    print("S0  CONTROL -- the coverage lemma must find nothing at the sqrt"
          " pole and nothing on the starved supply")
    word = landings_direct(M_sqrt, 100000)
    mu, _ = window_table(word)
    attained = sorted(mu)
    complete = attained[:-1]
    mmax = max(mu[d] for d in complete)
    ok(mmax <= 2, f"sqrt pole: max multiplicity over {len(complete)}"
       f" complete windows is {mmax} <= 2")
    bad = [L for L in range(3, 61)
           if any(math.gcd(d, L) == 1 and mu[d] >= L for d in complete)]
    ok(not bad, "sqrt pole: no attained coprime value with mu >= L at any"
       f" L in 3..60 (the lemma has no hypothesis; offending L: {bad})")
    nh = never_hit(word, 6)
    ok(nh == [4], f"sqrt pole: never-hit classes mod 6 = {nh}"
       " (the known obstruction, and no bound can exist beside it)")
    sw = landings_direct(M_starved, 20000)
    mus, _ = window_table(sw)
    cop = [d for d in mus if math.gcd(d, 6) == 1]
    ok(not cop, f"starved supply: attained values coprime to 6: {cop}"
       f" (every attained value is a multiple of 6; {len(mus)} values)")


# ---------------------------------------------------------------- #
# S1 -- the seam: c > 2 is the slow side, the bound computed          #
# ---------------------------------------------------------------- #

SLOW = [(5, 2), (7, 3), (9, 4)]
HORIZON_SLOW = 100000


def s1_seam_and_bound():
    print("\nS1  THE SEAM -- above c = 2 every window is attained, mu is"
          " unbounded, and the coverage lemma prints a bound beside F")
    for p, q in SLOW:
        c = Fraction(p, q)
        M = M_power(p, q)
        word = landings_direct(M, HORIZON_SLOW)
        mu, last_index = window_table(word)
        attained = sorted(mu)
        d_end = attained[-1]          # possibly incomplete window
        d0 = d0_slow(p, q)
        skipped = [d for d in range(d0, d_end) if d not in mu]
        under = [d for d in range(d0, d_end)
                 if d in mu and mu[d] < (w_len(M, d) - 1) // d]
        note(f"c = {p}/{q}: d_0 = {d0}, horizon d = {d_end},"
             f" landings {len(word)}, t_max = {word[-1][0]}")
        ok(not skipped, f"c = {p}/{q}: every d in [{d0}, {d_end}) attained"
           f" (skipped: {skipped[:5]})")
        ok(not under, f"c = {p}/{q}: mu(d) >= floor((w(d)-1)/d) at every"
           f" window in [{d0}, {d_end}) (violations: {under[:5]})")
        sample = [d for d in (d0, 2 * d0, 10 * d0, d_end // 2) if d in mu]
        note("mu at d = " + ", ".join(f"{d}: {mu[d]} (floor {(w_len(M, d) - 1) // d})"
                                      for d in sample))
        # the bound: d*(L) and T(L) = top(d*) from M alone, no
        # enumeration; the index form B(L) wherever the horizon reaches
        time_ok = True
        cover_ok = True
        reached = 0
        rows = []
        for L in range(2, 61):
            F = first_hit_index(word, L)
            tF = word[F - 1][0]
            d_star = d_star_of(p, q, d0, L)
            assert (w_len(M, d_star) - 1) // d_star >= L
            T = M(d_star) - PREGROW
            if tF > T:
                time_ok = False
            B = None
            if d_star < d_end:
                reached += 1
                res = set(t % L for t, d in word if d == d_star)
                if len(res) != L or F > last_index[d_star]:
                    cover_ok = False
                B = last_index[d_star]
            rows.append((L, d_star, T, B, F, tF))
        ok(time_ok, f"c = {p}/{q}: the last first-hit landing t_F(L) <= T(L)"
           " = top(d*(L)) at every L = 2..60, T computed from M alone")
        ok(cover_ok, f"c = {p}/{q}: where the horizon reaches d*(L) -- {reached}"
           " of 59 moduli -- that window alone covers Z/L and F(L) <= B(L),"
           " the index of its last landing")
        for L, d_star, T, B, F, tF in rows:
            if L % 10 == 0 or L == 2:
                note(f"L = {L:2d}: d* = {d_star:7d}  T = {T:.3e}  t_F ="
                     f" {tF:.3e}  F = {F:4d}  B = {B}")
        ex = Fraction(p, p - 2 * q)
        T30 = [T for L, _, T, _, _, _ in rows if L == 30][0]
        T60 = [T for L, _, T, _, _, _ in rows if L == 60][0]
        note(f"log2(T(60)/T(30)) = {math.log2(T60 / T30):.2f} against the"
             f" hand exponent c/(c-2) = {float(ex):.2f}")


# ---------------------------------------------------------------- #
# S2 -- the band: mu <= 1, the lemma has no hypothesis                #
# ---------------------------------------------------------------- #

BAND = [(4, 3), (3, 2), (5, 3), (7, 4)]
HORIZON_BAND = 20000


def s2_band():
    print("\nS2  THE BAND c in (1, 2) -- no window is walked twice beyond"
          " d_1, so the coverage lemma reaches nothing")
    for p, q in BAND:
        M = M_power(p, q)
        word = landings_direct(M, HORIZON_BAND)
        mu, _ = window_table(word)
        d1 = d1_band(p, q)
        twice = [d for d in mu if d >= d1 and mu[d] >= 2]
        ok(not twice, f"c = {p}/{q}: d_1 = {d1}; mu(d) <= 1 at every"
           f" attained d >= d_1 (d reaches {max(mu)}; violations"
           f" {twice[:5]})")
        hyp = {}
        for L in range(2, 61):
            q_d = [d for d in mu if math.gcd(d, L) == 1 and mu[d] >= L]
            if q_d:
                hyp[L] = min(q_d)
        ok(not hyp, f"c = {p}/{q}: no attained coprime value with mu >= L"
           f" at any L = 2..60 (qualifying: {hyp})")
        below = sorted(d for d in mu if d < d1)
        note(f"c = {p}/{q}: attained values below d_1: {len(below)},"
             f" max multiplicity there {max((mu[d] for d in below), default=0)}")


# ---------------------------------------------------------------- #
# S3 -- the block structure does not force coverage                  #
# ---------------------------------------------------------------- #

def s3_block_control(word32):
    print("\nS3  THE BLOCK STRUCTURE -- a block continued jitter-free is a"
          " quadratic and misses (p-1)/2 classes at every odd prime p")
    bl = blocks(word32)[:1000]
    primes = [p for p in range(3, 61) if all(p % r for r in range(2, p))]
    bad = 0
    pairs = 0
    for b in bl:
        t0, d0, delta = b[2], b[3], b[4]
        for p in primes:
            if delta % p == 0:
                continue
            pairs += 1
            vals = set((t0 + j * d0 + delta * j * (j + 1) // 2) % p
                       for j in range(p * p))
            if len(vals) != (p + 1) // 2:
                bad += 1
    ok(bad == 0, f"{pairs} block-prime pairs over the first {len(bl)}"
       f" blocks: every frozen continuation misses exactly (p-1)/2"
       f" classes mod p ({bad} off)")
    lens = [b[1] for b in bl]
    note(f"block lengths over these: mean {sum(lens) / len(lens):.2f},"
         f" max {max(lens)} -- against p up to 59")


# ---------------------------------------------------------------- #
# S4 -- the residue reads the offset                                 #
# ---------------------------------------------------------------- #

def s4_offset(word32):
    print("\nS4  THE OFFSET -- t_{n+1} = top(d_n) - o_n, the recurrence"
          " that moves it, and how its residue is distributed")
    M = M_power(3, 2)
    n = len(word32)
    ident = 0
    rec = 0
    offs = []
    thetas = []
    # THE ENGINE'S TUPLE CONVENTION: word[i] = (t, d) carries the gap
    # that PRODUCED t, so the offset of the landing t is read against
    # the landing before it -- o = e(d) - t_prev -- and the identity
    # is t = top(d) - o. (The docstring writes the same thing with the
    # gap indexed as LEAVING its landing.)
    for i in range(1, n - 1):
        t_prev = word32[i - 1][0]
        t, d = word32[i]
        t1, d1 = word32[i + 1]
        o = (M(d) - PREGROW - d) - t_prev
        w = w_len(M, d)
        if not (t == M(d) - PREGROW - o and 0 <= o <= w - 2):
            ident += 1
        # the recurrence: countdown by d, refill by window lengths --
        # the refill over (d, dd] telescopes to M(dd) - M(d) - (dd - d),
        # so the least dd making o - d + refill >= 0 is found by binary
        # search rather than by walking the skipped windows (which at
        # 10^5 landings is 10^9 root extractions)
        def refill(dd):
            return o - d + M(dd) - M(d) - (dd - d)
        hi = d + 1
        while refill(hi) < 0:
            hi *= 2
        lo = d + 1
        while lo < hi:
            mid = (lo + hi) // 2
            if refill(mid) >= 0:
                hi = mid
            else:
                lo = mid + 1
        o1 = (M(d1) - PREGROW - d1) - t
        if not (lo == d1 and refill(lo) == o1):
            rec += 1
        offs.append(o)
        thetas.append(o / (w - 1) if w > 1 else 0.0)
    ok(ident == 0, f"identity t_{{n+1}} = top(d_n) - o_n with"
       f" 0 <= o_n <= w(d_n) - 2 at all {n - 2} landings ({ident} off)")
    ok(rec == 0, "the offset recurrence (countdown by d_n, refill by"
       f" w(d) - 1 to nonnegative) reproduces (d_{{n+1}}, o_{{n+1}}) at"
       f" all {n - 2} landings ({rec} off)")
    for L in (6, 60):
        census = [0] * L
        for o in offs:
            census[o % L] += 1
        mean = len(offs) / L
        dev = max(abs(x - mean) / mean for x in census)
        ok(dev < 0.10, f"o_n mod {L} census over {len(offs)} landings:"
           f" every class within {100 * dev:.1f}% of uniform (band 10%)")
        if L == 6:
            note(f"mod 6 census: {census}")
    thetas.sort()
    m = len(thetas)
    ks = max(max(abs((i + 1) / m - x), abs(i / m - x))
             for i, x in enumerate(thetas))
    ok(ks < 0.02, f"theta_n = o_n / (w - 1): Kolmogorov distance from"
       f" uniform on [0, 1) is {ks:.4f} (band 0.02)")
    note(f"theta mean {sum(thetas) / m:.4f} (uniform: 0.5)")


# ---------------------------------------------------------------- #
# S5 -- the hunt widened into the band's interior                    #
# ---------------------------------------------------------------- #

def s5_hunt():
    print("\nS5  THE HUNT -- two more powers inside (1, 2), every L <= 60,"
          " every class")
    for p, q in [(4, 3), (7, 4)]:
        M = M_power(p, q)
        word = landings_direct(M, HORIZON_BAND)
        missing = {}
        last = 0
        for L in range(2, 61):
            nh = never_hit(word, L)
            if nh:
                missing[L] = nh
            else:
                last = max(last, first_hit_index(word, L))
        ok(not missing, f"c = {p}/{q}: every class mod every L = 2..60 hit"
           f" within {len(word)} landings (missing: {missing});"
           f" last first-hit at landing {last}")


def main():
    import time
    t0 = time.time()
    s0_control()
    s1_seam_and_bound()
    s2_band()
    word32 = landings_direct(M_power(3, 2), 100000)
    s3_block_control(word32)
    s4_offset(word32)
    s5_hunt()
    print(f"\n{CHECKS[0] - CHECKS[1]}/{CHECKS[0]} checks pass,"
          f" {time.time() - t0:.1f} s")
    return CHECKS[1] == 0


if __name__ == "__main__":
    sys.exit(0 if main() else 1)
