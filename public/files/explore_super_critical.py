"""
explore_super_critical.py -- THE SUPER-CRITICAL CELL: is the last
unclassified band of sublinear supplies untame, or was its question only
ever asked in the wrong currency? (Sibling of
explore_supply_tameness.py, whose four-cell classification leaves this
one cell open; and of explore_wrap_word.py, whose closed form and offset
recurrence solve the sqrt pole below it.)

THE SETTING. For the growing-window machine on a sublinear modulus
supply the honest law reads DECIDABILITY = RATE + SUPPLY TAMENESS: the
rate caps the machine's own arithmetic and forces every pending fire to
land, and the one remaining input channel is the supply's fine
arithmetic, extracted as the question "is some landing time congruent to
a mod L?". The classification of supplies runs on the INVERSE supply
M(d) = max{g : m(g) <= d} rather than on the rate, and it has four cells:
quasi-polynomial M is tame by offset compression, slow supplies are tame
by the coverage lemma, value-starved supplies are the undecidable
channel at any rate, and the IRRATIONAL-POWER band between the sqrt pole
and the linear rate is open -- filed as fractional-power
equidistribution and outside every mechanism there.

THE TAKE, and it is a change of currency rather than a harder attack.
Equidistribution is not what the extracted question needs. Deciding "is
some landing congruent to a mod L" needs COVERAGE of Z/L -- every class
hit at all -- and coverage is an arithmetic statement about the landing
word, not an analytic one about its density. The old coverage lemma
proves coverage from MULTIPLICITY (one attained gap value coprime to L
walking its own window across all of Z/L), and multiplicity is exactly
what this band does not have: mu(d) ~ (3/2) d^(-1/2) sits BELOW ONE
across the whole cell, so almost every window is empty and the lemma has
no purchase here by construction. So the question this script asks is
whether a DIFFERENT sufficient condition covers -- one built from the
gap sequence's own shape rather than from any window's repetition.

THE OBJECT (conventions re-derived from explore_supply_tameness.py's
engine, not from the docs, which do not carry them).
  THE RIDER      v := (v + 1) mod max(2, m(g)), one pass per tick, the
                 frontier g = t + 2 (pregrow 2).
  A LANDING      a pass t at which v returns to 0.
  WINDOW TOP     top(d) = M(d) - pregrow.
  THE STEP       from a landing at t the next gap is the least d with
                 top(d) - d >= t, and the next landing is t + d. The
                 pointer never moves back, M being monotone.
  MULTIPLICITY   mu(d) = the number of landings with gap d.
  THE CELL       m(g) = ceil(g^(2/3)), M(d) = isqrt(d^3): the specimen
                 the classification names. Read as M(d) = floor(d^c) at
                 c = 3/2, which generalizes to any rational c > 1 whose
                 denominator exceeds 1 -- the irrational-power band is
                 c non-integer, and c integer is the solved critical
                 band.

THE HAND ATTACK (derived on paper before any engine code; the run
adjudicates, and every derived quantity below is re-derived rather than
carried over from the sibling).

(1) THE GAP LAW. Write d_n for the n-th landing's gap. A landing sits
just under its own window top, so t_n ~ top(d_n) ~ d_n^c, while the step
from one landing to the next is t_{n+1} - t_n = d_n. Differentiating the
first against n and substituting the second: c d_n^(c-1) d' = d_n, so
d' = d_n^(2-c)/c. The clean form is in u = d^(c-1), where
u' = (c-1) d^(c-2) d' = (c-1)/c -- a CONSTANT. So d_n^(c-1) ~ ((c-1)/c) n
at every c, and at c = 3/2 that is sqrt(d_n) ~ n/3, giving d_n ~ n^2/9
and t_n ~ n^3/27. The same line fixes the horizon's arithmetic size at
the other powers swept: d_n ~ ((c-1)n/c)^(1/(c-1)), largest at c = 5/3
(about 8 * 10^6 at n = 10^5) and smallest at c = 5/2. PREDICTION SHAPE:
the gap sequence is quadratic in the landing index and its first
difference grows like sqrt(d) -- both measured, neither assumed.

(2) WHY MULTIPLICITY CANNOT BE THE MECHANISM. mu(d) ~ 1/d' = c d^(c-2),
which at c = 3/2 is (3/2) d^(-1/2): below 1 from d = 3 on. Almost every
gap value is SKIPPED, and no window is walked twice. The coverage
lemma's hypothesis (some coprime d attained with mu >= L) is not merely
unverified here, it is false for every L >= 2 beyond a computable point.
This is the sentence that makes a second mechanism necessary rather than
merely nice.

(3) THE BLOCK, and the mechanism it offers. The first difference
delta_n = d_{n+1} - d_n grows like sqrt(d) but grows SLOWLY: it holds a
fixed integer value across a run of landings, because delta changes by
one only when d has moved far enough to shift (2/3) sqrt(d) by one, and
that takes about 3 sqrt(d) / ((2/3) sqrt(d)) = 4.5 landings at c = 3/2.
Call a maximal run of landings with constant delta a BLOCK. THE INDEX
CONVENTION IS RE-DERIVED FROM THE ENGINE AND NOT CARRIED OVER: the
generator appends (t, d) after t += d, so a pair carries the landing and
the gap that PRODUCED it, never the gap that leaves it. Reading it the
other way puts the block's quadratic one index out of phase. With the
engine's convention, inside a block with first landing t_0, first gap
d_0 and difference delta, the landings are exactly
       t_j = t_0 + j d_0 + delta * j (j + 1) / 2,
a QUADRATIC in the within-block index -- so a block's residues mod L are
the values of a fixed quadratic polynomial over an interval of j, and a
block long enough to run j over all of Z/L would hit about half the
classes at odd prime L and could never hit all of them. The blocks here
are far shorter than L at the moduli swept, which is what makes the
mechanism a UNION statement: consecutive blocks carry different
(t_0, d_0, delta) and the linear coefficient d_0 walks, so covering Z/L
is a question about a RUN of consecutive landings and not about any one
block. The quantity that answers it is the COVERAGE WINDOW -- how many
consecutive landings suffice -- measured both at its best position in
the horizon and at its worst over sampled starts. A window bounded by a
constant times L is a coverage lemma with a computable certificate; a
window growing like L log L is a waiting time and no lemma at all.

(4) THE OTHER FACE, AND IT IS THE ONE WITH A REAL KILL IN IT. The
classification records "every class mod 60 is hit by landing 410 and the
censuses sit near-uniform" as an OBSERVATION at ONE supply and TWO
moduli. The sqrt pole's own history says that is exactly where an
exclusion hides: there the landings never take the value 4 mod 6, a real
congruence obstruction (2 s(v) vanishing mod 6) that no equidistribution
heuristic predicts, and it was found by census and not by argument. So
the hunt runs the full rectangle -- four irrational powers by every
modulus L <= 60 by every class -- and a single never-hit class refutes
the heuristic the cell was filed under, which is a larger find than
closing it.

(5) THE POSITIVE CONTROL THE HUNT NEEDS. A rectangle sweep that reports
"no exclusions anywhere" is worthless unless the same code reports an
exclusion where one is known to exist. The starved supply (all gap
values divisible by 6) keeps five of six classes mod 6 empty forever by
the starvation lemma, and the sqrt pole excludes 4 mod 6 by the wrap
word's closed form. Both are run through the identical census path
BEFORE any open-cell result is read.

TRANSPLANT FLAGS (every intuition available here was grown at INTEGER
powers, and each import is marked).
  T1  The offset recurrence o(d) = (o(d-1) + top(d) - top(d-1)) mod d
      was derived at the sqrt pole and restated over monotone M by the
      sibling. It is NOT used as a lemma here: this script works the
      landing word directly and the offset appears only as a printed
      diagnostic.
  T2  The PARITY DICHOTOMY (decrement -1 mod d at even integer c, +1 at
      odd) has no statement at c = 3/2, top(d) - top(d-1) not being a
      polynomial in d there. No prediction below inherits it.
  T3  The geometric MARK ratios (2 at the sqrt pole, 3 at the scaled
      line) are fingerprints of a quasi-polynomial M. Marks are printed
      here for the record and no ratio is predicted.

PREDICTIONS (fixed before the run; each adjudicated SEPARATELY -- the
sibling's lesson, no AND-welded kill criteria; each names what the rig
PRINTS and not what it would mean).
  PR1  CONTROL. The direct-inverse generator agrees landing for landing
       with the sibling's unit-pointer generator on the sqrt pole and on
       M = isqrt(d^3) over a shared prefix, and with the concrete tick
       rider on a shorter one. Falsifier: any disagreement.
  PR2  THE GAP LAW. On M = isqrt(d^3), d_n / n^2 lies in [1/9 - 0.02,
       1/9 + 0.02] at n = 10^4 and 10^5, and delta_n = d_{n+1} - d_n
       takes at most two distinct values in any 50 consecutive landings
       beyond n = 10^3. Falsifier: either band missed, or a 50-landing
       stretch carrying three delta values.
  PR3  THE QUADRATIC IDENTITY. Inside every block, t_j = t_0 + j d_0 +
       delta j (j+1) / 2 exactly, over the whole horizon. Falsifier: one
       violation. (This is an identity, not a measurement; it is checked
       because the block definition is the mechanism's carrier and a
       block boundary read one landing wrong would leave every count
       below reading as structure.)
  PR4  BLOCK LENGTHS. A block is counted in LANDINGS, which is one more
       than the run of deltas that defines it, and consecutive blocks
       therefore share their boundary landing. The hand figure is 4.5
       deltas, so 5.5 landings: the mean lies in [4.0, 6.5] and the
       maximum stays below 60 -- so no block ever runs its index across
       a full residue system at the moduli swept, and single-block
       coverage is impossible at L = 60 for a reason the print states.
  PR5  THE COVERAGE WINDOW, and it is the mechanism's whole content. For
       each L let N(L) be the least w such that SOME w consecutive
       landings in the horizon cover Z/L, and W(L) the largest w needed
       to cover from any of 20 starts sampled across the horizon. Both
       are at least L. PREDICTION: N(L) <= 3L and W(L) <= 6L for every
       L = 2..60. W is the one that matters: a uniform bound of the form
       "any c*L consecutive landings cover Z/L" IS an arithmetic
       coverage lemma with a computable certificate, and it is what the
       old multiplicity lemma delivered by a route this band forbids.
       Falsifier: either bound exceeded at any L. The two readings the
       print must separate: a ratio flat in L reads arithmetic, a ratio
       climbing like log L reads as a coupon-collector waiting time and
       leaves the cell exactly where the classification put it -- so the
       ratio is printed per L and not only its extreme.
  PR6  THE OBSTRUCTION HUNT. Over the four supplies M = floor(d^c) for
       c in {3/2, 5/3, 5/2, 7/3} and every L = 2..60, every class is hit
       within 10^5 landings. Falsifier: any never-hit class -- which
       refutes the equidistribution filing rather than confirming it,
       and is reported as the finding it is.
  PR7  THE POSITIVE CONTROL. The same census path reports exactly five
       never-hit classes mod 6 on the starved supply, and reports 4 mod
       6 never hit on the sqrt pole. Falsifier: either miss -- and PR6
       is not read at all until PR7 has passed.

RESOURCE ENVELOPE (named before the run). 10^5 landings per supply by
binary search on the inverse, four supplies plus two controls; integers
reach about d^c with d ~ 10^9 at c = 5/2, so ~10^22, well inside Python
ints. No arrays beyond the per-supply landing list (10^5 ints). Estimate
under 512 MB and under 5 minutes; peak reported under memwatch.

FINDINGS (entered after the run, from printed output).

THE TAKE IS REFUTED, and the refutation is this record's main purchase.
Coverage of Z/L by the landing word on the super-critical band is a
WAITING TIME and not an arithmetic certificate -- on the window from an
arbitrary start, and, which is the half that decides the matter, on the
first-hit index from the start of the run that the decider actually
reads. The frozen bound
W(L) <= 6L fails at L <= 60 already (worst 12.58 L at L = 60), and the
extended grid says why it was never going to hold: W(L)/L RISES with L,
end to end across the grid by +4.93 from L = 30 to L = 2000. THE
ONE-VARIABLE CONTROL RISES WITH IT: the real gap sequence shuffled --
identical multiset, identical residues mod every L, only the order gone
-- rises +4.50 over the same span, and the random-gap reference that
calibrates the path rises +5.01. So the shape is not carried by the
arithmetic: destroying the order alone leaves it. Read to the grid's
INTERIOR the real word rises +3.46 against the reference's +5.03, which
is where its constant-factor advantage sits and is not the shape
question; the rise is quoted end to end for that reason. So the change of currency does NOT close the cell: what
the extracted question needs is a UNIFORM coverage bound, and there is
no evidence of one where a waiting time is not also present. The
classification's filing of this cell as analytic stands, and it now
stands on a measurement against a control rather than on an
equidistribution heuristic (rule in range for the falsification, the
surrogate comparison an observation at seven moduli).

WHY THE L <= 60 RANGE COULD NOT HAVE DECIDED IT, which is the process
finding under the result. Across 2..60 the coupon-collector mean H_L
moves by about 2 while the worst-of-twenty tail contributes a constant
near 3, so the two readings the prediction was placed to separate differ
by less than the sampling spread -- and the printed table over that
range is flat-looking for exactly that reason. A verdict read off it
would have confirmed the take. The grid to L = 2000 plus the surrogate
is what separates them, and the surrogate is asserted to separate
(its W/L rises by at least 2.5) BEFORE the real word's number is read.

WHAT SURVIVES, AND IT IS A SPLIT THE CELL DID NOT HAVE.
  (1) THE DECIDER'S OWN QUANTITY PAYS THE SAME WAITING TIME, and this
      is the one the verdict has to be read on. W(L) above is the window
      needed from an ARBITRARY start, and the decider never starts
      anywhere but the beginning of the run -- so W's growth is a
      strictly stronger statement that says nothing about decidability,
      and it was measured first because it was the easier neighbour of
      the real question. The real question is the FIRST-HIT index F(L)
      from the start: a computable bound on F is exactly what would let
      the decider answer NO. Measured, F(L) sits at 0.63 to 1.46 times
      L H_L across the same grid -- the coupon-collector law, and the
      same law the shuffled and random references pay. No arithmetic
      advantage on the quantity that decides anything.
      The best-position window is short by contrast -- N(L) <= 3L over
      every L = 2..60, worst ratio 2.21 at L = 57, attaining its floor L
      at 12 moduli, all of them at most 15 -- so a YES has a short
      certificate SOMEWHERE; that is a fact about the word and not about
      the decider, which cannot start where the certificate is.
      SO THE SHARPER OPEN QUESTION IS A COMPUTABLE FIRST-HIT BOUND: is
      there computable B with every class mod L hit by landing B(L)?
      L H_L fits in range and nothing proves it, which is where
      "fractional-power equidistribution" was pointing all along -- the
      cell is not restated cheaper, it is restated in the decider's own
      terms and it stays exactly as hard.
  (2) THE GAP LAW, derived and confirmed: d_n^(c-1) ~ ((c-1)/c) n at
      every c, so d_n ~ n^2/9 at c = 3/2. Measured d_n/n^2 = 0.11138 at
      n = 10^4 and 0.11114 at n = 10^5 against 1/9 = 0.11111.
  (3) THE BLOCK IDENTITY: inside a maximal run of landings with constant
      gap difference, t_j = t_0 + j d_0 + delta j (j+1) / 2 exactly, at
      every landing of all 51,150 blocks in the horizon. The sqrt pole's
      global closed form has no analogue on this band; this local one
      does, and it is what makes the residues a quadratic walk.
  (4) NO CONGRUENCE OBSTRUCTION ANYWHERE. Four irrational powers
      (c = 3/2, 5/3, 5/2, 7/3) by every L = 2..60 by every class: every
      class hit, the last one at landing 410, 365, 379 and 480
      respectively. This upgrades the classification's ONE-supply,
      TWO-moduli observation to four supplies and 59 moduli, and it
      independently reproduces that record's own figure -- landing 410
      at c = 3/2, mod 60. The census path is positive-controlled first:
      the same code reports five never-hit classes mod 6 on the starved
      supply and exactly {4} mod 6 on the sqrt pole, which are the two
      exclusions the corpus already owns.

TWO FREEZE ERRORS, both caught by the run and both worth their space.
  PR2's second clause ("at most two distinct delta values in any 50
  consecutive landings") contradicted the hand attack it was written
  from: the same paragraph gives delta a change every 4.5 landings, so a
  50-landing window holds about 11 values. Measured 13. The clause was a
  consequence stated in the wrong direction, not a claim about the
  object, and the corrected consequence is what the rig now checks.
  PR3's identity was written as delta j (j-1) / 2 -- one index out of
  phase, because the generator appends (t, d) AFTER t += d, so a pair
  carries the gap that PRODUCED its landing and not the gap that leaves
  it. The convention was carried over from the sibling instead of being
  re-derived from the engine, which is exactly what the conventions
  block above exists to prevent. PR3 was placed as a carrier check on
  definition and it did its job: with the wrong phase, every block count
  downstream would have read as structure.

AND ONE PREDICTION FALSIFIED BY THE OBJECT, not by the freeze. PR4's
mean: blocks run 2.955 landings, not the hand figure's 5.5, with max 6
and min 2. The trend rate is right and the picture behind it is wrong --
delta does not climb a monotone staircase, it JITTERS, descending at
15.1% of steps with the largest single change 2. Maximal constant runs
are therefore short while the trend still moves at 2/9 per landing. PR4's
max clause -- the load-bearing half, that no block runs its index across
a full residue system -- stands at max 6.

RUN RECORD. ALL 25 CHECKS PASS, 13.6 s wall clock; 129.0 MB peak working
set against the 512 MB ceiling (memwatch). Predictions as frozen: PR1
confirmed, PR2 first clause confirmed and second clause falsified by its
own hand figure, PR3 confirmed after the index convention was re-derived
from the engine, PR4 max clause confirmed and mean clause falsified by
the object, PR5 FALSIFIED at both bounds and the shape adjudicated
against a surrogate control, PR6 confirmed, PR7 confirmed and run before
PR6 was read.
"""

import math

CHECKS = 0


def ok(cond, msg):
    global CHECKS
    assert cond, msg
    CHECKS += 1
    print(f"  [ok] {msg}")


def note(msg):
    print(f"  ... {msg}")


# ---------------------------------------------------------------- #
# supplies: the inverse M(d), and the concrete m(g) where needed    #
# ---------------------------------------------------------------- #

PREGROW = 2


def M_power(num, den):
    """M(d) = floor(d^(num/den)), exact by integer root of d^num."""
    def M(d):
        return iroot(d ** num, den)
    return M


def iroot(n, c):
    """Floor integer c-th root, exact, by integer Newton -- never via a
    float estimate. At c = 5/3 the argument reaches d^5 ~ 10^34 and a
    float seed's absolute error would put the correction loop past any
    horizon; the sibling's float-seeded root is sound only at the sizes
    it runs."""
    if n <= 0:
        return 0
    if c == 1:
        return n
    if c == 2:
        return math.isqrt(n)
    x = 1 << (-(-n.bit_length() // c))
    while True:
        y = ((c - 1) * x + n // x ** (c - 1)) // c
        if y >= x:
            return x
        x = y


def ceil_root(n, c):
    r = iroot(n, c)
    return r if r ** c == n else r + 1


def m_p23(g):
    """m = ceil(g^(2/3)) = least d with d^3 >= g^2 -- the cell's own
    forward supply, kept so the tick rider can be run against it."""
    return max(2, ceil_root(g * g, 3))


def M_sqrt(d):
    return d * d


def m_sqrt(g):
    return max(2, ceil_root(g, 2))


def M_starved(d):
    """The starvation control: every attained gap value divisible by 6.
    M is the inverse of m(g) = 6 * ceil(sqrt(g) / 6), so the pointer can
    only ever stop at multiples of 6."""
    return (d // 6) * 6 * ((d // 6) * 6) if d >= 6 else 0


# ---------------------------------------------------------------- #
# the generators                                                    #
# ---------------------------------------------------------------- #

def landings_pointer(M, t_max, d_start=2):
    """The sibling's unit-pointer form: from a landing at t the next gap
    is the least d with top(d) - d >= t, found by walking d upward."""
    t = 0
    d = d_start
    while True:
        while M(d) - PREGROW - d < t:
            d += 1
        t += d
        if t > t_max:
            return
        yield t, d


def landings_direct(M, count, d_hi_seed=8):
    """The same word by BINARY SEARCH on the inverse rather than by a
    unit pointer -- the only form that reaches 10^5 landings on a
    super-critical supply, where the gap value passes 10^9."""
    t = 0
    d_lo = 2
    out = []
    while len(out) < count:
        # least d >= d_lo with M(d) - PREGROW - d >= t
        hi = max(d_lo, d_hi_seed)
        while M(hi) - PREGROW - hi < t:
            hi *= 2
        lo = d_lo
        while lo < hi:
            mid = (lo + hi) // 2
            if M(mid) - PREGROW - mid >= t:
                hi = mid
            else:
                lo = mid + 1
        d = lo
        d_lo = d
        t += d
        out.append((t, d))
    return out


def rider_landings(m_func, horizon):
    """THE CONTROL. Tick by tick, the concrete rider."""
    g = PREGROW
    v = 0
    out = []
    for t in range(1, horizon + 1):
        g += 1
        v = (v + 1) % max(2, m_func(max(1, g)))
        if v == 0:
            out.append(t)
    return out


# ---------------------------------------------------------------- #
# blocks: maximal runs of landings with constant first difference   #
# ---------------------------------------------------------------- #

def blocks(word):
    """word = [(t, d), ...]. A BLOCK is a maximal run of landings whose
    gap first difference delta = d_{n+1} - d_n is constant. Returns
    [(start_index, length, t_0, d_0, delta)], the last partial run
    dropped: its delta is cut by the horizon and is not final."""
    if len(word) < 3:
        return []
    deltas = [word[i + 1][1] - word[i][1] for i in range(len(word) - 1)]
    out = []
    i = 0
    while i < len(deltas):
        j = i
        while j + 1 < len(deltas) and deltas[j + 1] == deltas[i]:
            j += 1
        # landings i .. j+1 share the difference deltas[i]
        out.append((i, j - i + 2, word[i][0], word[i][1], deltas[i]))
        i = j + 1
    return out[:-1]


# ================================================================ #
# S0 -- THE CONTROL, run before anything downstream is read        #
# ================================================================ #

def s0_control():
    print("\nS0  CONTROL -- the direct solver against the pointer form"
          " and the tick rider")

    M23 = M_power(3, 2)

    # direct vs pointer, sqrt pole
    ptr = [x for x in landings_pointer(M_sqrt, 20000)]
    dir_ = landings_direct(M_sqrt, len(ptr))
    ok(ptr == dir_,
       f"sqrt pole: direct == pointer over {len(ptr)} landings")

    # direct vs pointer, the cell
    ptr23 = [x for x in landings_pointer(M23, 200000)]
    dir23 = landings_direct(M23, len(ptr23))
    ok(ptr23 == dir23,
       f"cell M = floor(d^1.5): direct == pointer over {len(ptr23)}"
       " landings")

    # both against the concrete tick rider
    rid = rider_landings(m_sqrt, 20000)
    ok([t for t, _ in ptr] == rid,
       f"sqrt pole: pointer == concrete tick rider over {len(rid)}"
       " landings")
    rid23 = rider_landings(m_p23, 60000)
    ok([t for t, _ in ptr23 if t <= 60000] == rid23,
       f"cell: pointer == concrete tick rider over {len(rid23)}"
       " landings")

    ok(M23(4) == 8 and M23(9) == 27,
       "M = floor(d^1.5) exact at the integer cases 4 -> 8, 9 -> 27")


# ================================================================ #
# S1 -- THE GAP LAW (PR2)                                          #
# ================================================================ #

HORIZON = 100000


def s1_gap_law():
    print("\nS1  THE GAP LAW -- d_n ~ n^2/9 and its first difference")
    M23 = M_power(3, 2)
    word = landings_direct(M23, HORIZON)

    for n in (10000, HORIZON):
        d = word[n - 1][1]
        r = d / (n * n)
        note(f"n = {n}: d_n = {d}, t_n = {word[n-1][0]}, d_n/n^2 ="
             f" {r:.5f}  (hand: 1/9 = {1/9:.5f})")
        ok(abs(r - 1 / 9) <= 0.02,
           f"d_n/n^2 within 0.02 of 1/9 at n = {n}")

    deltas = [word[i + 1][1] - word[i][1] for i in range(len(word) - 1)]
    worst = 0
    worst_at = None
    for s in range(1000, len(deltas) - 50, 137):
        k = len(set(deltas[s:s + 50]))
        if k > worst:
            worst, worst_at = k, s
    note(f"max distinct delta values in a 50-landing window (sampled"
         f" from n = 1000): {worst} at n = {worst_at}")
    # The hand attack's own figure: delta ~ (2/3) sqrt(d) and d ~ n^2/9,
    # so d(delta)/dn = 2/9 and delta holds a value for 4.5 landings. A
    # 50-landing window therefore holds about 50 / 4.5 = 11 values. The
    # frozen clause said TWO, which contradicts the hand figure it was
    # written from; the corrected consequence is checked here and the
    # freeze error is carried in the run record.
    ok(8 <= worst <= 16,
       "distinct delta values in a 50-landing window sit at the hand"
       f" figure 50 / 4.5 = 11 (measured {worst})")


# ================================================================ #
# S2 -- THE QUADRATIC IDENTITY AND BLOCK LENGTHS (PR3, PR4)        #
# ================================================================ #

def s2_blocks():
    print("\nS2  BLOCKS -- the quadratic identity and the block lengths")
    M23 = M_power(3, 2)
    word = landings_direct(M23, HORIZON)
    blks = blocks(word)

    bad = None
    for (i, ln, t0, d0, dl) in blks:
        for j in range(ln):
            pred = t0 + j * d0 + dl * j * (j + 1) // 2
            if word[i + j][0] != pred:
                bad = (i, j, word[i + j][0], pred)
                break
        if bad:
            break
    ok(bad is None,
       f"the quadratic identity holds at every landing of all"
       f" {len(blks)} blocks")

    lens = [b[1] for b in blks]
    mean = sum(lens) / len(lens)
    note(f"blocks: {len(blks)}, mean length {mean:.3f}, max"
         f" {max(lens)}, min {min(lens)}  (hand figure 5.5 landings)")

    # PR4's mean clause is falsified by the print above, and this is the
    # diagnostic that says why: the hand attack read delta as a MONOTONE
    # staircase rising by one every 4.5 landings, which would make a
    # block 4.5 deltas long. Measured here instead: how often delta
    # descends at all, and how many distinct values it takes across the
    # span of a nominal staircase step. A jittering delta gives short
    # maximal runs at the SAME trend rate, which is what leaves PR4's
    # max clause -- the load-bearing one -- standing while its mean
    # clause falls. Printed, not asserted: this measurement was not
    # frozen and enters the record as an observation.
    deltas = [word[i + 1][1] - word[i][1] for i in range(len(word) - 1)]
    desc = sum(1 for i in range(1, len(deltas)) if deltas[i] < deltas[i - 1])
    jump = max(abs(deltas[i] - deltas[i - 1]) for i in range(1, len(deltas)))
    note(f"delta descends at {desc} of {len(deltas)-1} steps"
         f" ({100*desc/(len(deltas)-1):.1f}%); largest single change"
         f" |delta_n+1 - delta_n| = {jump}")

    ok(max(lens) < 60, "max block length below 60 -- no block runs its"
       " index across a full residue system at any modulus swept")


# ================================================================ #
# S3 -- BLOCK COVERAGE, the mechanism (PR5)                        #
# ================================================================ #

def cover_window_from(word, start, L, cap):
    """Least w <= cap such that word[start : start + w] covers Z/L, or
    None if the cap is reached first."""
    seen = set()
    n = len(word)
    for w in range(1, cap + 1):
        if start + w > n:
            return None
        seen.add(word[start + w - 1][0] % L)
        if len(seen) == L:
            return w
    return None


def s3_coverage_window():
    print("\nS3  THE COVERAGE WINDOW -- how many consecutive landings"
          " cover Z/L")
    M23 = M_power(3, 2)
    word = landings_direct(M23, HORIZON)
    n = len(word)

    worst_N = (0.0, None)
    worst_W = (0.0, None)
    rows = []
    for L in range(2, 61):
        cap = 40 * L
        # N(L): the best position anywhere in the horizon, scanned on a
        # stride so the sweep stays linear in the horizon rather than
        # quadratic; the stride is 1 up to 3000 landings and 29 after,
        # 29 being coprime to nothing in range that would alias it.
        best = None
        for start in list(range(0, 3000)) + list(range(3000, n - cap, 29)):
            w = cover_window_from(word, start, L, cap if best is None
                                  else best - 1)
            if w is not None and (best is None or w < best):
                best = w
                if best == L:
                    break
        # W(L): the worst over 20 starts spread across the horizon
        worst = 0
        for f in range(20):
            start = (n - cap - 1) * f // 20
            w = cover_window_from(word, start, L, cap)
            if w is None:
                worst = None
                break
            worst = max(worst, w)
        rows.append((L, best, worst))
        if best is not None and best / L > worst_N[0]:
            worst_N = (best / L, L)
        if worst is not None and worst / L > worst_W[0]:
            worst_W = (worst / L, L)

    for L, best, worst in rows:
        if L in (2, 6, 12, 30, 47, 59, 60):
            note(f"L = {L}: N(L) = {best} ({(best or 0)/L:.2f} L),"
                 f" W(L) = {worst} ({(worst or 0)/L:.2f} L)")
    note(f"worst ratio N(L)/L = {worst_N[0]:.2f} at L = {worst_N[1]};"
         f" worst W(L)/L = {worst_W[0]:.2f} at L = {worst_W[1]}")
    perfect = [L for L, b, _ in rows if b == L]
    note(f"moduli attaining the floor N(L) = L: {len(perfect)} of 59"
         f" -- {perfect[:12]}{' ...' if len(perfect) > 12 else ''}")

    ok(all(b is not None for _, b, _ in rows) and worst_N[0] <= 3.0,
       "N(L) <= 3L for every L = 2..60")
    note("PR5's W bound is FALSIFIED at this range. s3b reads the"
         " SHAPE of this same statistic; s3c reads the one the decider"
         " consumes, and that is where the verdict is taken")


# The extended sweep, added after the L <= 60 print and before any
# verdict was written: over 2..60 the coupon-collector constant swamps
# the logarithm (H_L moves by only 2 across the whole range), so that
# range cannot separate "bounded certificate" from "waiting time" and
# reading a verdict off it would be reading noise. Two things fix it --
# a grid reaching L = 2000, and a MATCHED SURROGATE: the same number of
# landings with the same gap magnitudes and the arithmetic destroyed,
# run through the identical measurement path. The surrogate is the
# discriminator's own control: if it does not separate, nothing read
# off the real word separates either.

GRID = (30, 60, 125, 250, 500, 1000, 2000)
LONG_HORIZON = 300000


def surrogate_uniform(word, seed=7):
    """THE RANDOM-GAP REFERENCE, and it is not a one-variable control:
    gap n drawn uniformly from [2, 2 d_n) matches the landing density
    and its growth in the MEAN, but it changes the gap variance as well
    as the arithmetic. It is here to establish what a pure waiting time
    looks like through this measurement path, and it is named for that
    rather than for matching."""
    import random
    rng = random.Random(seed)
    out = []
    t = 0
    for _, d in word:
        t += rng.randrange(2, max(3, 2 * d))
        out.append((t, 0))
    return out


def surrogate_permuted(word, seed=11):
    """THE ONE-VARIABLE CONTROL: the real gap sequence shuffled. The
    multiset of gaps is IDENTICAL -- every magnitude and every residue
    mod every L is the one the object supplies -- and the only thing
    destroyed is the ORDER, which is where any arithmetic in the landing
    word has to live. This is the control the verdict rests on; the
    uniform reference above only calibrates the path."""
    import random
    rng = random.Random(seed)
    gaps = [d for _, d in word]
    rng.shuffle(gaps)
    out = []
    t = 0
    for d in gaps:
        t += d
        out.append((t, 0))
    return out


def worst_window(word, L, cap, starts=20):
    worst = 0
    for f in range(starts):
        st = (len(word) - cap - 1) * f // starts
        v = cover_window_from(word, st, L, cap)
        if v is None:
            return None
        worst = max(worst, v)
    return worst


def s3b_shape():
    print("\nS3b THE SHAPE -- the coverage window against a matched"
          " surrogate, out to L = 2000")
    M23 = M_power(3, 2)
    word = landings_direct(M23, LONG_HORIZON)
    perm = surrogate_permuted(word)
    unif = surrogate_uniform(word)

    real, ctrl, fake = {}, {}, {}
    for L in GRID:
        cap = 40 * L
        real[L] = worst_window(word, L, cap)
        ctrl[L] = worst_window(perm, L, cap)
        fake[L] = worst_window(unif, L, cap)
        # A None here means the cap was hit rather than that coverage
        # failed, and dividing it below would raise a TypeError three
        # lines from the cause. Named where it happens.
        ok(None not in (real[L], ctrl[L], fake[L]),
           f"all three words cover Z/{L} inside the 40L cap")
        note(f"L = {L:5d}:  real W/L = {real[L]/L:6.2f}   permuted"
             f" {ctrl[L]/L:6.2f}   uniform {fake[L]/L:6.2f}")

    lo, hi = GRID[0], GRID[-1]
    rise_f = fake[hi] / hi - fake[lo] / lo
    rise_r = real[hi] / hi - real[lo] / lo
    # The rise is read END TO END across the grid and not to an interior
    # point: over 30..1000 the two rises are +3.46 and +5.03, which a
    # reader cannot reconcile with "same shape", and the sub-range is
    # chosen by nothing but which L the printed table happens to name.
    rise_c = ctrl[hi] / hi - ctrl[lo] / lo
    note(f"W/L rise from L = {lo} to L = {hi}: real {rise_r:+.2f},"
         f" permuted {rise_c:+.2f}, uniform {rise_f:+.2f}")
    ok(rise_f >= 2.5,
       "CALIBRATION: the random-gap reference's W/L rises by at least"
       " 2.5 end to end across the grid, so the measurement path can"
       " see a waiting time when there is one")
    ok(rise_c >= 2.5,
       "THE ONE-VARIABLE CONTROL RISES TOO: shuffling the real gap"
       " sequence, which changes nothing but the order, leaves the"
       " same shape -- so the shape is not carried by the arithmetic")
    ok(max(real[L] / L for L in GRID) > 6.0,
       "PR5 FALSIFIED and pinned: the real word's W(L) passes 6L on the"
       " grid")


# ================================================================ #
# S4 -- THE POSITIVE CONTROL for the census path (PR7)             #
# ================================================================ #

def never_hit(word, L):
    seen = set(t % L for t, _ in word)
    return sorted(set(range(L)) - seen)


def first_hit(word, L):
    """F(L): the index of the landing at which the LAST class mod L is
    first hit, counting from the START of the run. This is the decider's
    own quantity -- it enumerates landings from the beginning and never
    from anywhere else -- so a computable bound on F is what would let
    it answer NO. W(L) above, the window needed from an ARBITRARY start,
    is a strictly stronger statement whose failure says nothing about
    the decider; it was measured first and it was the easier neighbour
    of this question."""
    seen = set()
    for i, (t, _) in enumerate(word):
        seen.add(t % L)
        if len(seen) == L:
            return i + 1
    return None


def s3c_first_hit():
    print("\nS3c THE DECIDER'S OWN QUANTITY -- first hit from the start"
          " of the run, against the coupon-collector law")
    M23 = M_power(3, 2)
    word = landings_direct(M23, LONG_HORIZON)
    perm = surrogate_permuted(word)
    unif = surrogate_uniform(word)

    ratios = []
    for L in GRID:
        H = sum(1.0 / k for k in range(1, L + 1))
        a, b, c = (first_hit(word, L), first_hit(perm, L),
                   first_hit(unif, L))
        ratios.append((L, a / L / H))
        note(f"L = {L:5d}:  real F/L = {a/L:6.2f}   permuted"
             f" {b/L:6.2f}   uniform {c/L:6.2f}   H_L = {H:5.2f}")
    lo = min(r for _, r in ratios)
    hi = max(r for _, r in ratios)
    note(f"real F(L) / (L H_L) over the grid: {lo:.2f} to {hi:.2f}"
         f" (1.00 is the coupon-collector law exactly)")
    ok(0.5 <= lo and hi <= 2.0,
       "the real word's first-hit index sits within a factor of two of"
       " L H_L at every grid point -- the waiting time the shuffled and"
       " random references also pay, on the quantity the decider"
       " actually reads")


def s4_census_control():
    print("\nS4  POSITIVE CONTROL -- the census path on two supplies"
          " with KNOWN exclusions")

    starved = landings_direct(M_starved, 20000, d_hi_seed=12)
    miss6 = never_hit(starved, 6)
    note(f"starved supply, gaps mod 6: "
         f"{sorted(set(d % 6 for _, d in starved))}; classes mod 6"
         f" never hit: {miss6}")
    ok(len(miss6) == 5,
       "starved supply: exactly five classes mod 6 never hit")

    sq = landings_direct(M_sqrt, 100000)
    miss = never_hit(sq, 6)
    note(f"sqrt pole, classes mod 6 never hit: {miss}")
    ok(miss == [4],
       "sqrt pole: 4 mod 6 never hit, and it is the only exclusion")


# ================================================================ #
# S5 -- THE OBSTRUCTION HUNT (PR6), read only after S4             #
# ================================================================ #

SUPPLIES = [("3/2", 3, 2), ("5/3", 5, 3), ("5/2", 5, 2), ("7/3", 7, 3)]


def s5_hunt():
    print("\nS5  THE OBSTRUCTION HUNT -- four irrational powers by"
          " every L <= 60")
    total_missing = []
    for name, num, den in SUPPLIES:
        M = M_power(num, den)
        word = landings_direct(M, HORIZON)
        miss_here = []
        worst_first = (0, None)
        for L in range(2, 61):
            first = {}
            for idx, (t, _) in enumerate(word):
                r = t % L
                if r not in first:
                    first[r] = idx + 1
                    if len(first) == L:
                        break
            if len(first) < L:
                miss_here.append((L, sorted(set(range(L)) - set(first))))
            else:
                mx = max(first.values())
                if mx > worst_first[0]:
                    worst_first = (mx, L)
        note(f"c = {name}: last class covered at landing"
             f" {worst_first[0]} (worst L = {worst_first[1]});"
             f" moduli with a never-hit class: {len(miss_here)}")
        if miss_here:
            for L, cls in miss_here[:5]:
                note(f"    c = {name}, L = {L}: never hit {cls}")
        total_missing.extend((name, L, cls) for L, cls in miss_here)
    ok(not total_missing,
       "every class mod every L = 2..60 is hit on all four"
       f" irrational-power supplies within {HORIZON} landings")


def main():
    import time
    t0 = time.time()
    s0_control()
    s1_gap_law()
    s2_blocks()
    s3_coverage_window()
    s3b_shape()
    s3c_first_hit()
    s4_census_control()
    s5_hunt()
    print(f"\nALL {CHECKS} CHECKS PASS  ({time.time() - t0:.1f} s)")


if __name__ == "__main__":
    main()
