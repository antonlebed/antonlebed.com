"""
explore_supply_tameness.py -- WHICH SUPPLIES ARE TAME: the classification
between the solved sqrt pole and the planted-bit pole. (Sibling of
explore_wrap_word.py, whose closed form and offset recurrence are the
sqrt-supply instance of the machinery generalized here; and of
explore_pending_fires.py, whose supply oracle is the untame pole.)

THE SETTING. The honest decidability law for the growing-window machine
on a sublinear modulus supply reads DECIDABILITY = RATE + SUPPLY
TAMENESS: the rate caps the machine's own arithmetic and forces every
pending fire to land, and the one remaining input channel is the
supply's fine arithmetic. Its two poles are on record -- the canonical
supply m(g) = ceil sqrt g is fully solved (closed-form landings, the
offset recurrence, reachable residues decided for every modulus L up to
60), while a supply with a planted tail switch makes halting
undecidable with every capacity cap intact. Between them sits the
classification this script works: for which computable sublinear
supplies is the extracted supply-arithmetic question -- "is some landing
time congruent to a mod L?" -- decidable?

THE OBJECT (conventions re-derived from explore_wrap_word.py's engine).
  THE RIDER      v := (v + 1) mod max(2, m(g)), one pass per tick, the
                 frontier g = t + 2 (pregrow 2).
  A LANDING      a pass t at which v returns to 0. The gap from a
                 landing at t is d = min{j >= 2 : j >= m(t + j + 2)},
                 non-decreasing in t for monotone m -- so one
                 non-decreasing pointer generates the word for ANY
                 monotone supply, no simulation.
  THE INVERSE SUPPLY   M(d) = max{g : m(g) <= d}. This -- not the
                 rate -- turns out to be the classification variable.
  WINDOW TOP     top(d) = M(d) - 2. A landing t has gap d iff
                 top(d-1) < t <= top(d); inside a window landings walk
                 in steps of d.
  TOP OFFSET     o(d) = top(d) - t_last(d), t_last(d) the last landing
                 <= top(d). When window d is nonempty,
                 o(d) = (o(d-1) + top(d) - top(d-1)) mod d; an empty
                 window carries the offset without the mod.
  MULTIPLICITY   mu(d) = number of landings in window d,
                 ~ (top(d) - top(d-1)) / d.
  A MARK         a value d where the offset wraps upward
                 (o(d) > o(d-1)) -- the generalization of the sqrt
                 supply's reset points at 3 * 2^n.
  TRANSPLANT FLAG: the offset recurrence was derived at the sqrt supply;
  its restatement over an arbitrary monotone inverse M is this record's
  claim, and every section bisimulates the closed generator against the
  concrete tick rider on its own supply before reading anything else.

THE HAND ATTACK (derived on paper before any engine code; the run
adjudicates).

(1) THE PARITY DICHOTOMY (power supplies m = ceil g^(1/c)). Here
M(d) = d^c and the window-top decrement is
d^c - (d-1)^c == (-1)^(c+1) mod d. Two regimes:
  c EVEN: decrement == -1 mod d -- the offset counts down by one per
  value, resets to about d at zero, and the resets DOUBLE: geometric
  marks with ratio 2, the sqrt shape at every even power.
  c ODD (>= 3): decrement == +1 mod d -- the offset GROWS by one per
  value while its bound d also grows by one, so it never wraps again:
  o(d) = d - a for a constant a. The landing set is then EVENTUALLY
  EXACTLY POLYNOMIAL -- no geometric correction at all. Hand-simulated
  at c = 3 to d = 7: o(d) = d - 2 from d = 2 on, t_last(d) = d^3 - d,
  first landing of window d is (d-1)^3 + 1, mu(d) = 3(d-1). The odd
  tower is TAMER than sqrt: where the sqrt supply's non-polynomial
  content is a doubling sequence, the cube supply has none.

(2) THE SCALED CRITICAL LINE (m = ceil sqrt(2g)). M(d) = floor(d^2/2);
the decrement alternates exactly: top(d) - top(d-1) = d for even d,
d - 1 for odd d -- mod d that is {0, -1} alternating, a countdown by
one per TWO values. A reset therefore recurs at ratio 3, not 2: from a
reset at d0 with offset about d0, the offset reaches zero after about
2*d0 further values. Same mechanism, different geometric ratio -- the
marks' ratio is a fingerprint of the supply's inverse, not a universal
constant. Multiplicity sits at about 1, so some gap values are SKIPPED
(empty windows), which the offset carries across without wrapping.

(3) THE COVERAGE LEMMA (the slow side, proved). If any gap value d
with gcd(d, L) = 1 is attained with multiplicity >= L, that window's
landings walk d steps across all of Z/L: EVERY class mod L is hit, by
the end of that one window. So for a supply with mu(d) -> infinity
(any m growing slower than every g^(1/2 - eps) has this along its
attained values), reachability mod L is decidable from a finite prefix
and the answer is uniformly YES -- provided coprime values are
attained. Contrapositive, THE STARVATION LEMMA: a supply that keeps
any class mod L empty must starve coprime high-multiplicity values --
every window with mu >= L has gcd(d, L) > 1. The supply oracle's
planted track (every modulus value divisible by L) is exactly maximal
starvation: all gaps are 0 mod L, the landings never leave one class,
and the only structure a landing can report is the supply's own value
arithmetic. The oracle's design was FORCED, not merely clever.

(4) THE SUPER-CRITICAL BAND (m = ceil g^(2/3): faster than sqrt, still
sublinear). M(d) = isqrt(d^3), multiplicity ~ (3/2) d^(-1/2) -> 0:
most values are skipped, and the offset signal stops compressing (its
increments read the digits of floor(d^(3/2)) -- no eventual
periodicity). The equidistribution heuristic says every class is hit,
but proving it is Piatetski-Shapiro territory -- fractional-power
sequences mod L -- outside every mechanism above. This is the
classification's honest OPEN CELL, and the classification variable
says why: M is no longer quasi-polynomial, and multiplicity gives no
coverage.

THE CLASSIFICATION (what the sections test): tameness is a property of
the INVERSE SUPPLY M(d), not of the rate. Quasi-polynomial M -- the
critical band, both parities and any rational scaling -- is tame by
offset compression: the landing set is polynomial-per-window plus a
geometric mark sequence, and residue questions reduce to eventually
periodic data. Slow supplies attaining coprime values are tame by
coverage. Value-starved supplies are the oracle channel, untame at any
rate. Fast-but-sublinear supplies with irrational-power M -- the name is
the classification's, and what it means is M = floor(d^c) at NON-INTEGER
c, the rational non-integers included -- are the open band.

SECTIONS.

S0  THE CONTROL. The general machinery (pointer generator over top(d),
    offset tracker, mark detector) re-run on the sqrt supply must
    reproduce the frozen record exactly: closed generator == concrete
    tick rider landing for landing over the sibling's horizon, and the
    marks exactly {3 * 2^n}. Everything downstream is read only if
    this passes.

S1  THE PARITY DICHOTOMY. c = 3: assert o(d) = d - 2, t_last = d^3 - d,
    mu(d) = 3(d-1), no skipped values, over the full horizon. c = 5:
    the offset freezes at o(d) = d - a from some d* on (a and d*
    printed; freezing is the prediction, the constant is read from the
    run). c = 4: the decrement is -1 mod d at every value, and the
    mark ratios approach 2. Each supply bisimulated against its tick
    rider on a prefix first.

S2  THE SCALED CRITICAL LINE. m = ceil sqrt(2g): the alternating
    decrement law checked exactly over the horizon; skipped values
    appear (mu ~ 1); the mark ratios approach 3.

S3  COVERAGE. On c = 3 (all L = 2..60) and the log2 supply
    (L in {6, 60}): every class mod L is hit, and the LAST first-hit
    time is <= top(d0(L)), d0(L) the smallest attained value coprime
    to L whose window multiplicity is >= L -- the lemma's bound,
    checked as an inequality against the run.

S4  THE STARVED SUPPLY (the untame shape, with a FIXED computable
    switch -- a control, not a new claim). Values 6 * ceil(sqrt(g)/6)
    (all divisible by 6) until g = 10^5, then +1 (all 1 mod 6).
    Pre-switch: every landing in ONE class mod 6. Post-switch: the
    first wrap is legible and the phase then advances by one per
    landing, hitting all six classes. One bit per landing, read off
    the values -- the starvation lemma exhibited.

S5  THE OPEN BAND. m = ceil g^(2/3) out to t ~ 10^12 (about 3 * 10^4
    landings, gap solved directly rather than by unit pointer): the
    attained-value fraction decays like d^(-1/2); censuses mod 6 and
    mod 60 with first-hit indices -- every class hit is the
    equidistribution OBSERVATION, explicitly not a proof.

PREDICTIONS (fixed before the run; each adjudicated SEPARATELY -- the
sibling's lesson: no AND-welded kill criteria).
  PR1  S0 reproduces the record: closed == rider on the sibling's
       horizon; marks exactly {3, 6, 12, 24, ...} in range.
  PR2  c = 3: o(d) = d - 2 for every d from 2 to the horizon's d_max,
       zero skipped values, t_last(d) = d^3 - d, mu(d) = 3(d-1).
       Falsifier: any single violation (first one printed).
  PR3  c = 5: the offset freezes -- o(d) - d constant from some d* to
       d_max. Falsifier: a wrap after d*.
  PR4  c = 4: decrement == -1 mod d at every d; the last three mark
       ratios land in [1.85, 2.15].
  PR5  scaled a = 2: decrement alternation exact; the last three mark
       ratios land in [2.8, 3.2].
  PR6  coverage holds: all classes hit on both supplies at every L
       tested, and every last-first-hit <= the lemma bound.
  PR7  starved supply: exactly one class mod 6 pre-switch; all six
       post-switch, phase advancing by one per landing.
  PR8  open band (observation tier): all 60 classes mod 60 hit by
       k = 3 * 10^4; attained fraction below 0.01 by d ~ 10^6.

SECOND FREEZE (written after the first run printed the scaled-critical
marks and before the verifying re-run). The printed marks 10, 28, 82,
244, 730, 2188 read as an exact law: m_(n+1) = 3 m_n - 2, closed form
3^n + 1 -- the analogue at inverse d^2/2 of the sqrt pole's 3 * 2^n.
Hand account: a reset puts the offset at d - 1 and the one-per-two
countdown spends it over 2(d - 1) further values, so the next mark sits
at 3d - 2. Prediction: the equality marks == [3^n + 1] holds exactly
over the horizon. Adjudicated by the added S2 check on the re-run.

ESTIMATES. Wall clock: under ~90 s (the heavy legs: the log2 supply's
~8 * 10^5 landings, the c = 5 closed generation ~3 * 10^6, the sqrt
control's tick rider at 1.5 * 10^6). Memory: well under 100 MB against
the 512 MB analysis ceiling (streams and per-window scalars; the one
retained list is the log2 landing prefix).

FINDINGS (entered after the runs; every number below is a printed
output).

1. THE PARITY DICHOTOMY IS EXACT (rule at the checked families). c = 3:
   o(d) = d - 2 at every complete window 2..215 (windows to t = 10^7),
   t_last(d) = d^3 - d, mu(d) = 3(d - 1), zero skipped values, 14,850
   landings bisimulated against the tick rider to t = 10^6. c = 5: the
   offset freezes at o(d) = d - 2 from d* = 2, no wrap through d = 39
   (t = 10^8), the same constant as c = 3 at this initialization. The
   FREEZE IS STRUCTURAL AND THE CONSTANT IS NOT: re-run at pregrows 5
   and 9 the c = 3 offset still freezes, at d - 1 and d - 3 -- the
   wrap-word split again, the structure the supply's, the seed the
   start's (the audit added this control after a first findings draft
   read the shared 2 as the pregrow itself). c = 4: decrement == -1
   mod d at every d to 100, marks exactly [3, 6, 12, 24, 48, 96] --
   the sqrt pole's own 3 * 2^n sequence, seed included, not merely its
   ratio; c = 6 and c = 8 print the same 3 * 2^n marks. So the odd
   tower carries NO geometric content at all (its landing set is
   exactly polynomial from the start), and the even towers CHECKED
   (c = 2, 4, 6, 8) all carry the same doubling marks at the canonical
   start -- the countdown itself is proved at every even c; the shared
   seed 3 is a statement about the checked powers at this start, the
   seed being start-data.

2. THE MARK SEQUENCE IS A FINGERPRINT OF THE INVERSE, AND AT THE
   SCALED LINE IT IS EXACT (rule at a = 2; the second freeze). The
   marks of m = ceil sqrt(2g) are 10, 28, 82, 244, 730, 2188 =
   3^n + 1 exactly, recurrence m' = 3m - 2 -- reset to d - 1, spent at
   one-per-two over 2(d - 1) values. The decrement alternation
   (d even -> d, d odd -> d-1) holds exactly to d = 4472; 8 of 4471
   values are skipped (multiplicity ~ 1), and the offset carries over
   every skip without wrapping. Same mechanism as the sqrt pole, a
   different geometric ratio: the ratio is data about M, not a
   universal constant.

3. THE COVERAGE LEMMA HOLDS WITH ROOM (lemma, proved; checked at 61
   supply-modulus pairs). On c = 3 every class mod L is hit for every
   L = 2..60 and on log2 for L = 6, 60, with the last first-hit under
   the bound top(d0) in every case (log2 L = 60: all classes by
   t = 1658 against bound 2046 at d0 = 11; c = 3 L = 60: by t = 4573
   against 12,165).

4. THE STARVED SUPPLY IS LEGIBLE ONE BIT PER LANDING (control,
   rule by construction). All 603 pre-switch landings sit in one class
   mod 6; the first post-switch wrap lands at t = 100,297 and the
   phase then advances by exactly one class per landing, hitting all
   six. The supply oracle's planted track is this shape at its
   extreme -- the starvation lemma exhibited.

5. THE OPEN BAND LOOKS EQUIDISTRIBUTED AND COMPRESSES NOWHERE
   (observation). m = ceil g^(2/3), 30,000 landings out to
   t ~ 1.001 * 10^12 (d_max = 100,089,290): the attained-value
   fraction tracks the 1.5/sqrt(d) heuristic at every decade (0.0012
   measured vs 0.0015 at d ~ 10^6), all 60 classes mod 60 are hit by
   landing 410, and the mod-6 census is near-uniform (4863..5170 over
   30,000). No proof mechanism reaches it: multiplicity gives no
   coverage and the offset signal has no eventual periodicity.

6. THE CLASSIFICATION (the synthesis the sections assemble). Tameness
   is a property of the inverse supply M(d), not of the rate.
   (i) Quasi-polynomial M -- the critical band, both parities, any
   rational scaling -- is tame by OFFSET COMPRESSION: landings are
   polynomial-per-window plus a geometric mark sequence, so residue
   questions reduce to eventually periodic data (rule at the checked
   families; conjectured at every quasi-polynomial M). (ii) Slow
   supplies attaining coprime values are tame by COVERAGE (proved).
   (iii) Value-starved supplies are the oracle channel, untame at any
   rate (proved by the starvation contrapositive; the planted-bit
   construction was forced to live here). (iv) Irrational-power M in
   the super-critical band is the OPEN CELL: equidistribution
   observed, no elementary mechanism proves it.

RUN RECORD. ALL 155 CHECKS PASS, 43.3 s wall clock; 85.9 MB peak
working set against the 512 MB ceiling (memwatch, at the 147-check
stage — the controls added since retain no new data). First run: 146
checks, all eight predictions PR1-PR8 confirmed as frozen. Second run
added the second-freeze mark-law check. The audit then added the
pregrow sweep and the direct-solver control (a findings draft had
misread the constant 2 shared by c = 3 and c = 5 as the pregrow
itself), and the c = 6, 8 mark checks (a draft had extended the shared
seed 3 to EVERY even power from two instances — the same species one
level up); a later audit added the c = 6, 8 tick-rider bisimulations,
which those mark checks had run without while the design sentence
promised one per supply. No other slips found between the freezes and
the runs.
"""

import math

CHECKS = 0


def ok(cond, msg):
    global CHECKS
    assert cond, msg
    CHECKS += 1
    print(f"  [ok] {msg}")


# ---------------------------------------------------------------- #
# supplies: m(g) and the inverse M(d), one pair per family          #
# ---------------------------------------------------------------- #

def iroot(n, c):
    """Floor integer c-th root."""
    if n <= 0:
        return 0
    r = int(round(n ** (1.0 / c)))
    while r > 0 and r ** c > n:
        r -= 1
    while (r + 1) ** c <= n:
        r += 1
    return r


def ceil_root(n, c):
    r = iroot(n, c)
    return r if r ** c == n else r + 1


def make_power(c):
    m = lambda g: max(2, ceil_root(g, c))
    M = lambda d: d ** c
    return m, M


def sqrt2_m(g):
    return max(2, ceil_root(2 * g, 2))


def sqrt2_M(d):
    return (d * d) // 2


def log2_m(g):
    return max(2, (g - 1).bit_length() if g >= 2 else 1)


def log2_M(d):
    return 2 ** d


def p23_m(g):
    """m = ceil(g^(2/3)) = least d with d^3 >= g^2."""
    return max(2, ceil_root(g * g, 3))


def p23_M(d):
    return math.isqrt(d ** 3)


# ---------------------------------------------------------------- #
# the two generators: concrete tick rider, and the pointer form     #
# ---------------------------------------------------------------- #

def rider_landings(m_func, horizon, pregrow=2):
    """THE CONTROL. Tick by tick: per pass the frontier grows by one
    and v := (v + 1) mod max(2, m(g)). Returns landing pass indices."""
    g = pregrow
    v = 0
    out = []
    for t in range(1, horizon + 1):
        g += 1
        v = (v + 1) % max(2, m_func(max(1, g)))
        if v == 0:
            out.append(t)
    return out


def closed_landings(M_func, t_max, pregrow=2, d_start=2):
    """The pointer generator, any monotone supply: from a landing at t
    the next gap is the least d with top(d) - d >= t, top(d) =
    M(d) - pregrow; the pointer never moves back. Yields (t, d)."""
    t = 0
    d = d_start
    while True:
        while M_func(d) - pregrow - d < t:
            d += 1
        t += d
        if t > t_max:
            return
        yield t, d


def window_stats(M_func, t_max, pregrow=2):
    """Walk the closed generator and fold per-window: returns dict
    d -> (t_first, t_last, mu) for every ATTAINED gap value, plus the
    ordered attained-value list."""
    stats = {}
    order = []
    for t, d in closed_landings(M_func, t_max, pregrow):
        if d not in stats:
            stats[d] = [t, t, 1]
            order.append(d)
        else:
            stats[d][1] = t
            stats[d][2] += 1
    return stats, order


def offsets_and_marks(M_func, stats, order, pregrow=2):
    """o(d) = top(d) - t_last(d) over attained values, and the MARKS:
    attained values whose offset exceeds the previous attained one.
    The LAST attained value is excluded: its window is cut by the
    horizon, so its offset is not final and would mark spuriously."""
    offs = []
    marks = []
    prev_o = None
    for d in order[:-1]:
        o = (M_func(d) - pregrow) - stats[d][1]
        offs.append((d, o))
        if prev_o is not None and o > prev_o:
            marks.append(d)
        prev_o = o
    return offs, marks


# ================================================================ #
# S0 -- the control: the sqrt pole reproduced by the general rig    #
# ================================================================ #

SQRT_HORIZON = 1500000


def s0_control():
    print("== S0  the general machinery against the sqrt record ==")
    m, M = make_power(2)
    concrete = rider_landings(m, SQRT_HORIZON)
    derived = [t for t, _ in closed_landings(M, SQRT_HORIZON)]
    ok(derived == concrete,
       f"pointer generator == tick rider on all {len(concrete)} sqrt "
       f"landings out to t = {SQRT_HORIZON}")
    stats, order = window_stats(M, SQRT_HORIZON)
    offs, marks = offsets_and_marks(M, stats, order)
    d_top = order[-2]
    expected = []
    v = 3
    while v <= d_top:
        expected.append(v)
        v *= 2
    ok(marks == expected,
       f"marks are exactly the doubling sequence {expected} "
       f"(the recorded 3*2^n resets) up to d = {d_top}")


# ================================================================ #
# S1 -- the parity dichotomy: c = 3, 5 frozen; c = 4 doubling       #
# ================================================================ #

def bisimulate(name, m_func, M_func, horizon):
    concrete = rider_landings(m_func, horizon)
    derived = [t for t, _ in closed_landings(M_func, horizon)]
    ok(derived == concrete,
       f"{name}: pointer generator == tick rider on {len(concrete)} "
       f"landings to t = {horizon}")


def s1_parity():
    print("== S1  the parity dichotomy on power supplies ==")

    # -- c = 3: the frozen offset, checked exactly ----------------- #
    m3, M3 = make_power(3)
    bisimulate("c=3", m3, M3, 1000000)
    T3 = 10 ** 7
    stats, order = window_stats(M3, T3)
    d_max = order[-1]
    ok(order == list(range(2, d_max + 1)),
       f"c=3: no skipped values (every gap value 2..{d_max} attained)")
    bad = [(d, (M3(d) - 2) - stats[d][1]) for d in order
           if (M3(d) - 2) - stats[d][1] != d - 2 and d < d_max]
    ok(not bad,
       f"c=3: o(d) = d - 2 at every complete window 2..{d_max - 1} "
       f"(first violation would print here: {bad[:3]})")
    bad_last = [d for d in order[:-1] if stats[d][1] != d ** 3 - d]
    ok(not bad_last,
       f"c=3: t_last(d) = d^3 - d at every complete window")
    bad_mu = [d for d in order[1:-1] if stats[d][2] != 3 * (d - 1)]
    ok(not bad_mu,
       f"c=3: mu(d) = 3(d-1) at every complete window 3..{d_max - 1}")
    for pg, a_seen in [(2, 2), (5, 1), (9, 3)]:
        statsp, orderp = window_stats(M3, 10 ** 6, pregrow=pg)
        offsp = [(d, (M3(d) - pg) - statsp[d][1]) for d in orderp[:-1]]
        ok(all(o == d - a_seen for d, o in offsp[-8:]),
           f"c=3 pregrow {pg}: the offset still freezes, at d - {a_seen} "
           f"-- the freeze is structural, the constant is the start's")

    # -- c = 5: does the offset freeze, and at what constant? ------ #
    m5, M5 = make_power(5)
    bisimulate("c=5", m5, M5, 1000000)
    T5 = 10 ** 8
    stats5, order5 = window_stats(M5, T5)
    offs5, marks5 = offsets_and_marks(M5, stats5, order5)
    complete = [(d, o) for d, o in offs5 if d < order5[-1]]
    diffs = [d - o for d, o in complete]
    tail_const = diffs[-1]
    d_star = None
    for (d, o), dd in zip(complete, diffs):
        if dd == tail_const and d_star is None:
            d_star = d
        elif dd != tail_const:
            d_star = None
    print(f"  c=5: o(d) = d - {tail_const} from d* = {d_star} to "
          f"{complete[-1][0]}; marks before the freeze: {marks5}")
    ok(d_star is not None and d_star <= complete[-1][0],
       f"c=5: the offset FREEZES -- o(d) = d - {tail_const} from "
       f"d* = {d_star} on, no wrap after")

    # -- c = 4: countdown by one, marks double --------------------- #
    m4, M4 = make_power(4)
    bisimulate("c=4", m4, M4, 1000000)
    T4 = 10 ** 8
    stats4, order4 = window_stats(M4, T4)
    d_max4 = order4[-1]
    bad_dec = [d for d in range(3, d_max4 + 1)
               if (M4(d) - M4(d - 1)) % d != d - 1]
    ok(not bad_dec,
       f"c=4: window-top decrement == -1 mod d at every d 3..{d_max4}")
    offs4, marks4 = offsets_and_marks(M4, stats4, order4)
    ratios4 = [marks4[i + 1] / marks4[i] for i in range(len(marks4) - 1)]
    print(f"  c=4: marks {marks4}, successive ratios "
          f"{[f'{r:.3f}' for r in ratios4]}")
    ok(len(ratios4) >= 3 and all(1.85 <= r <= 2.15 for r in ratios4[-3:]),
       f"c=4: the last three mark ratios sit in [1.85, 2.15] "
       f"(doubling, the even-parity shape)")
    for cc in [6, 8]:
        mm, MM = make_power(cc)
        bisimulate(f"c={cc}", mm, MM, 1000000)
        sts, orr = window_stats(MM, 10 ** 9)
        _, mks = offsets_and_marks(MM, sts, orr)
        ok(len(mks) >= 3 and all(mks[i] == 3 * 2 ** i
                                 for i in range(len(mks))),
           f"c={cc}: marks {mks} are 3*2^n seed included at the "
           f"canonical start")


# ================================================================ #
# S2 -- the scaled critical line: ratio 3                           #
# ================================================================ #

def s2_scaled():
    print("== S2  the scaled critical line m = ceil sqrt(2g) ==")
    bisimulate("a=2", sqrt2_m, sqrt2_M, 1000000)
    T = 10 ** 7
    stats, order = window_stats(sqrt2_M, T)
    d_max = order[-1]
    bad = [d for d in range(3, d_max + 1)
           if sqrt2_M(d) - sqrt2_M(d - 1) != (d if d % 2 == 0 else d - 1)]
    ok(not bad,
       f"a=2: decrement alternation exact (d even -> d, d odd -> d-1) "
       f"over 3..{d_max}")
    skipped = d_max - 1 - len(order)
    print(f"  a=2: {len(order)} attained values, {skipped} skipped, "
          f"d_max = {d_max}")
    ok(skipped > 0, "a=2: skipped values exist (multiplicity ~ 1)")
    offs, marks = offsets_and_marks(sqrt2_M, stats, order)
    ratios = [marks[i + 1] / marks[i] for i in range(len(marks) - 1)]
    print(f"  a=2: marks {marks[:14]}{' ...' if len(marks) > 14 else ''}, "
          f"last ratios {[f'{r:.3f}' for r in ratios[-4:]]}")
    ok(len(ratios) >= 3 and all(2.8 <= r <= 3.2 for r in ratios[-3:]),
       f"a=2: the last three mark ratios sit in [2.8, 3.2] "
       f"(the ratio-3 fingerprint)")
    exact = [3 ** n + 1 for n in range(2, 2 + len(marks))]
    ok(marks == exact,
       f"a=2 SECOND FREEZE: the marks are exactly 3^n + 1 = {exact} -- "
       f"the recurrence m' = 3m - 2 from a reset to d - 1 and the "
       f"one-per-two countdown")


# ================================================================ #
# S3 -- coverage on the slow side, against the lemma bound          #
# ================================================================ #

def coverage_check(name, M_func, t_max, mods):
    stats, order = window_stats(M_func, t_max)
    landings = [(t, d) for t, d in closed_landings(M_func, t_max)]
    for L in mods:
        first_hit = {}
        for t, _ in landings:
            r = t % L
            if r not in first_hit:
                first_hit[r] = t
                if len(first_hit) == L:
                    break
        ok(len(first_hit) == L,
           f"{name} L={L}: all {L} classes hit "
           f"(last first-hit at t = {max(first_hit.values())})")
        d0 = None
        for d in order:
            if math.gcd(d, L) == 1 and stats[d][2] >= L:
                d0 = d
                break
        bound = M_func(d0) - 2
        ok(max(first_hit.values()) <= bound,
           f"{name} L={L}: last first-hit <= the lemma bound "
           f"top(d0={d0}) = {bound}")


def s3_coverage():
    print("== S3  the coverage lemma on the slow side ==")
    m3, M3 = make_power(3)
    coverage_check("c=3", M3, 10 ** 6, list(range(2, 61)))
    bisimulate("log2", log2_m, log2_M, 1000000)
    coverage_check("log2", log2_M, 2 ** 24, [6, 60])


# ================================================================ #
# S4 -- the starved supply: the untame shape exhibited              #
# ================================================================ #

SWITCH_G = 100000


def starved_m(g):
    base = 6 * ((ceil_root(g, 2) + 5) // 6)
    return base if g < SWITCH_G else base + 1


def s4_starved():
    print("== S4  the starved supply (fixed switch at g = 10^5) ==")
    horizon = 400000
    landings = rider_landings(starved_m, horizon)
    switch_t = SWITCH_G - 2
    pre = [t for t in landings if t <= switch_t]
    post = [t for t in landings if t > switch_t]
    pre_classes = sorted(set(t % 6 for t in pre))
    ok(len(pre_classes) == 1,
       f"pre-switch: every one of {len(pre)} landings sits in the single "
       f"class {pre_classes[0]} mod 6 (all gap values divisible by 6)")
    post_classes = sorted(set(t % 6 for t in post))
    ok(post_classes == [0, 1, 2, 3, 4, 5],
       f"post-switch: all six classes hit (first post-switch wrap at "
       f"t = {post[0]}, phase walks one class per landing)")
    steps = set((post[i + 1] - post[i]) % 6 for i in range(min(20, len(post) - 1)))
    ok(steps == {1},
       f"post-switch phase advances by exactly one per landing over the "
       f"first 20 gaps -- one legible bit per landing, as the starvation "
       f"lemma says")


# ================================================================ #
# S5 -- the open band: m = ceil g^(2/3), observation tier           #
# ================================================================ #

def s5_open_band():
    print("== S5  the open band m = ceil g^(2/3) (observation tier) ==")
    bisimulate("g^(2/3)", p23_m, p23_M, 1000000)

    # direct gap solve (the unit pointer would scan ~10^8 values)
    def landings_direct(k_max, pregrow=2):
        t = 0
        d = 2
        for _ in range(k_max):
            lo = max(d, iroot(int(t ** 2), 3) - 2)
            while p23_M(lo) - pregrow - lo < t:
                lo += 1
            d = lo
            t += d
            yield t, d

    ptr = [t for t, _ in closed_landings(p23_M, 10 ** 6)]
    direct_prefix = [t for t, _ in landings_direct(len(ptr))]
    ok(direct_prefix == ptr,
       f"direct gap solver == unit pointer on all {len(ptr)} landings to "
       f"t = 10^6 (the second implementation controlled)")

    K = 30000
    seq = list(landings_direct(K))
    t_end, d_end = seq[-1]
    print(f"  {K} landings out to t = {t_end} (d_max = {d_end})")
    attained = set(d for _, d in seq)
    for dec in [10 ** 3, 10 ** 4, 10 ** 5, 10 ** 6]:
        window = [d for d in attained if dec <= d < 2 * dec]
        frac = len(window) / dec
        print(f"  attained fraction in [{dec}, {2 * dec}): {frac:.4f} "
              f"(heuristic 1.5/sqrt(d) = {1.5 / math.sqrt(dec):.4f})")
    frac6 = len([d for d in attained if 10 ** 6 <= d < 2 * 10 ** 6]) / 10 ** 6
    ok(frac6 < 0.01,
       f"attained-value fraction at d ~ 10^6 is {frac6:.5f} < 0.01 "
       f"(the offset signal does not compress)")
    for L in [6, 60]:
        first_hit = {}
        for i, (t, _) in enumerate(seq):
            r = t % L
            if r not in first_hit:
                first_hit[r] = i + 1
        ok(len(first_hit) == L,
           f"mod {L}: all classes hit, last first-hit at landing "
           f"k = {max(first_hit.values())} -- equidistribution "
           f"OBSERVED, not proved")
        census = {}
        for t, _ in seq:
            census[t % L] = census.get(t % L, 0) + 1
        if L == 6:
            print(f"  mod 6 census over {K} landings: "
                  f"{dict(sorted(census.items()))}")


# ================================================================ #

def main():
    import time
    t0 = time.time()
    s0_control()
    s1_parity()
    s2_scaled()
    s3_coverage()
    s4_starved()
    s5_open_band()
    print(f"\nALL {CHECKS} CHECKS PASS  ({time.time() - t0:.1f} s)")


if __name__ == "__main__":
    main()
