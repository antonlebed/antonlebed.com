"""
The prediction door: score an exact reader on anticipating its
stream rather than on the tightness of its commitments -- does the
optimal reader finally depend on its data?

THE QUESTION
------------
The reader-descent corpus (explore_ratchet_learner.py,
explore_bootstrap_cures.py, explore_throttled_reader.py,
explore_banking_reader.py, explore_scale_clock.py) established
destination universality within its loss family: under the deficit
loss and the scale-clock loss -- both read off the committed-cell
trace's geometry -- a universal policy sits in every row's argmin
class, so no training stream picks the destination; the optimum
depends only on the resource environment. The one axis not yet
relaxed is what the loss READS. This experiment relaxes exactly
that axis, holding the reader family fixed: the loss below scores
each step's committed state on a decision about the stream's next
move -- data the trace geometry does not determine.

  Q1  EXISTENCE: under the next-side prediction loss, on the same
      policy space and rows, does a universal policy still sit in
      every row's argmin class -- or does the optimum finally
      depend on the stream?
  Q2  MECHANISM: where dependence appears, which policy axis
      carries it (route preference vs patience), and does the
      greedy reader stay optimal anywhere?
  Q3  PRICE: read the answer with the amnesia instruments -- group
      rows by their optimum sets (the readability partition: each
      refinement of the one-block partition is a bit of the data
      readable from the adapted optimum), and measure the exchange
      rate between per-row advantage and pooled loss.

TWO LEMMAS, PROVED BY HAND BEFORE THE ENGINE
--------------------------------------------
THE COLLAPSE LEMMA. The density reading of prediction is already
inside the old loss family. Score state C_n by the log-loss of the
true next image under the uniform conditional on C_n:

    -ln( |J_{n+1}| / |C_n| )  =  ln|C_n| - ln|J_{n+1}|,

and the counted sum is  sum ln|C_n| - sum ln|J_{n+1}|,  whose
second term is policy-free: the deficit loss plus a row constant,
per-row argmin classes verbatim. Any LOCAL proper score against
the flat conditional belief collapses the same way, for a stronger
reason: a flat density is constant on its cell, so the realized
score is a function of the cell length alone, the truth entering
at most through policy-free granularity. A prediction loss that
can leave the family must therefore score a DISCRETE DECISION
extracted from the state.

THE COARSENING LEMMA. The ratchet state is always coarser than the
public past: C_n contains J_n (the containment invariant), and
every policy sees the same J_0..J_n. Prediction from the full past
is policy-independent -- zero discrimination -- and any extractor
that conditions on the public J_n collapses to the same guess for
every policy (the belief is uniform on C_n intersect J_n = J_n).
The honest question is state-only: the evaluator asks the
committed cell ALONE to localize the stream's next move, through
one fixed policy-blind extractor.

THE NEXT-SIDE LOSS (fixed before the engine)
--------------------------------------------
Target -- policy-independent, future-determined. At counted step
n let the cut m_n be the mediant of J_n's endpoints. The cut is
interior to J_n, and the stream's image point x is interior to
every image interval, so the side of x relative to m_n is decided
by digits not yet seen at step n: a genuine prediction target.
For the identity map the cut is exactly the boundary between the
next-digit-1 child and the next-digit>=2 children of the cylinder,
so the target is the window's own next-digit question in cover
coordinates. The truth is read by deepening: the first later image
interval that excludes the cut pins the side (asserted to exist
within the deepened horizon; a rational cut can touch only
finitely many cylinder endpoints).

Guess -- state-only, one fixed extractor. The cut is interior to
C_n (which contains J_n). The uniform belief on the cell puts more
mass on the wider side of the cut, so the extractor guesses the
WIDER SIDE, by exact cross-multiplied comparison; an infinite
right side wins outright; an exact tie guesses left, and tie
counts are reported so the convention is visible, never silent.

THE LOSS = the number of misses over counted steps n in
[8, 119]. Primary comparator: the pure miss count. Secondary,
reported alongside: the composite order (misses, then the
lexicographic deficit), so the integer ties are visible and
refined, never hidden. The loss leaves the trace-geometry family
by construction: it reads the stream's side data -- two streams
with identical demand geometry but different digit directions
score the same committed trace differently.

THE DOMINANCE BREAK (why the question is live)
----------------------------------------------
Under trace-geometry losses tighter cells never hurt, and that
pointwise dominance is what made the greedy reader universal.
Under the next-side loss a tighter cell can flip the guess to the
WRONG side: with x just left of the cut, a coarse cell left-heavy
at the cut guesses left and hits, while a tight cell hugging the
image that is right-heavy at the cut guesses right and misses. No
pointwise dominance -- the universality proof route is dead at
this loss, and neither outcome of Q1 is foregone: dependence is
not trivially forced (on constant-direction rows many policies can
hit every counted step, and integer ties are fat), and survival is
not trivially forced (truth sequences genuinely differ per row).
Watches fixed with the design: argmin class sizes and the per-row
loss spread print beside any verdict -- a survive verdict carried
by argmin classes covering most of the space is a TIE-DRIVEN
survive, not a universality finding; a loss spread of zero names
the loss toothless at this scope.

PREDICTIONS (fixed before the run)
----------------------------------
P1  The controls pass (E1); a failed control stops the read.
P2  The dominance break realizes at scope: the witness scan finds
    a (row, step, cell pair) where the strictly tighter cell
    misses while the coarser one hits. If none prints, the break
    needs resources or wider spaces, and the verdict must say the
    dominance route survived here.
P3  Q1 is genuinely open; no outcome is predicted. The two
    toothless shapes above are the only pre-named readings.

EXPERIMENTS
-----------
E1  CONTROLS, run and read before any verdict.
    C1  Truth-sequence cross-check: for the four identity-map rows
        the engine's deepening truth must equal the truth computed
        independently from the digit sequence via the convergent
        tracker (next digit 1 = the side toward the far endpoint).
    C2  The rig reproduces the known result at the old loss: under
        the deficit, a universal class sits in every row's argmin
        and all transfer gaps are zero, with the greedy-patience
        policies inside it.
    C3  Extractor unit checks on hand-built cells (wider side,
        infinite side, exact tie).
    C4  The dominance-break witness scan (P2's observable).
E2  THE ARGMIN CENSUS: per row, the argmin classes of the
    next-side loss on the behavioral quotient, pure and composite;
    class sizes, loss spread, tie counts; the universal
    intersection (empty or not) -- Q1's observable; the transfer
    gap matrix; greedy's standing per row (Q2).
E3  THE PRICE: the readability partition (rows grouped by argmin
    sets, pure and composite); per-state readability (how many of
    a row's argmin classes are row-EXCLUSIVE -- optimal for that
    row alone); the pooled order (total misses across rows) and
    its winners; per-row regret of the pooled winners vs the row
    specialists' pooled excess -- the exchange rate between
    adaptation and the pooled loss (Q3).

DESIGN
------
Policy space: the unresourced commitment policies (s_t, s_s, pt,
pc) -- route preference at tree cells and at straddles, tree and
chain patience over the axis {0, 1, 2, 3, INF} -- 100 policies,
quotiented by counted-window behavior (the tuple over rows of
counted committed-cell traces); the loss is class-constant per row
(guess and truth are trace- and row-determined), asserted, and
computed once per class. Rows: the nine of
explore_scale_clock.py -- eight quadratic (maps id, sq, dbl over
phi, sqrt2, sqrt3, theta8) plus the aperiodic dbl/fib row (the
Fibonacci-word stream). Horizon 120, losses counted from step 8.
Index conventions re-derived from the engine: J_list[i] is the
image of the cylinder of digits a_0..a_i; step n commits after
seeing J_list[n]; the truth for step n reads strictly later images
(digits computed to depth 300 -- the sq/phi cut is a double-depth
convergent, mediant of consecutive squared Fibonacci-ratio
endpoints = F_{2n+3}/F_{2n+1} by the identity F_{n+1}^2 + F_{n+2}^2
= F_{2n+3}, so exclusion needs image depth about 2n; exclusion
asserted). Engine core --
cover cells, commit loop, containment invariant -- verbatim from
explore_scale_clock.py. Exact arithmetic throughout; no floats
anywhere in a comparison.

FINDINGS (from the run; all controls green first)
-------------------------------------------------
E1  All controls pass. C1: the engine's deepening truth equals the
    convergent-tracker truth on all four identity rows. The printed
    truth strings expose an orientation composition: cylinder
    orientation flips each step, so CONSTANT digits give an
    ALTERNATING side sequence (id/phi RLRL..., id/sqrt2 LRLR...)
    and sqrt3's alternating digits compose to a CONSTANT side
    (all R); the fib row's string is aperiodic. C2: in this same
    rig the deficit still has exactly one universal argmin class
    with the greedy class inside it -- the old-family result
    reproduced as the contrast control. C4: the dominance break
    REALIZES -- 1661 witness sites (first: id/phi step 9), a
    strictly tighter cell missing where a coarser cell hits.

E2  DESTINATION UNIVERSALITY FAILS AT THE NEXT-SIDE LOSS
    (exhaustive at scope; 38 behavior classes from 100 policies).
    The universal intersection is EMPTY under both the pure and the
    composite order. Per-row argmin classes are small where it
    matters (dbl/phi 2/38, dbl/sqrt2 4/38, dbl/fib 2/38, sq/phi
    7/38) and the loss spread is the full window (0 to 112 misses),
    so the failure is neither tie-driven nor toothless. Transfer
    gaps reach 112 = every counted step (dbl/sqrt2's optimum
    transported to sq/phi); every source row's argmin set fails on
    some other row except sq/sqrt2's, whose 32-of-38-class argmin
    is fat enough to cover every row at gap zero without any single
    class being universal. The greedy reader
    falls OUT of the argmin on six of nine rows. Eight of nine rows
    are PERFECTLY predictable inside the family (best = 0 misses)
    -- but by different policies per row: the argmin intersection
    over just those eight rows is ALREADY EMPTY, so the failure is
    not carried by the aperiodic row alone. The fib row is the
    exception: best = 47 of 112, no commitment policy tracks the
    Fibonacci word's side sequence.

E3  THE PRICE. The readability partition under the pure order is
    FULLY DISCRETE -- nine blocks, one per row: the set of optimal
    behaviors determines the row identity outright (the composite
    order merges exactly one pair, id/sqrt2 with id/sqrt3 -- eight
    blocks). In the amnesia vocabulary the readability SPLITS BY
    LEVEL: under the trace-geometry losses the adapted optimum was
    robustly data-free (the factoring witness); under the next-side
    loss the row is a function of the argmin SET -- set-level
    readability (the baseline is since measured: even the deficit's
    argmin SETS split the rows into three blocks, one split
    stream-driven, so this loss COMPLETES set-level readability
    rather than creating it -- explore_bandwidth_dial.py) -- while
    a SINGLE adapted state almost never pins
    its row: seven of nine rows have ZERO row-exclusive argmin
    classes (only sq/sqrt2 6/32 and sq/phi 1/7 have any), so at the
    state level most optima remain possibilistic about their
    stream -- and possibilistic is where the grade stops: the
    posterior on such a fiber tilts with the co-optimum counts
    rather than staying uniform (explore_door_grades.py).
    The ensemble of optima reads the data; an individual
    optimum can still deny it. The exchange rate prints: the
    pooled winner (one class, 171 total misses) is row-optimal on
    six rows and pays specialist advantage 56 / 56 / 12 on sq/phi,
    dbl/sqrt2, dbl/fib, whose specialists pay pooled excess
    222 / 287 / 175. That the excess is nonzero is definitional
    (a free specialist would itself be a pooled winner); the
    finding is the measured RATE -- roughly 4:1, 5:1, and 15:1
    pooled misses per miss of row advantage.

READING. The data door of this family is the LOSS'S TEMPORAL
REACH: both trace-geometry losses tried leave the optimum
stream-free (and the collapse lemma shows density-scored
prediction is such a loss in disguise), while at the one
stream-reading specimen tried -- one future side bit per counted
step -- the optimum SET becomes stream-readable, pointwise
dominance dies, and perfect prediction fragments into per-stream
specialists. Whether every stream-reading loss opens the door,
and how little coupling suffices, are the next questions. (The
coupling question is since answered: explore_bandwidth_dial.py --
one future bit at any counted position already empties the
universal intersection, and zero bits restore it; no threshold.
The criterion question is since answered too:
explore_score_criterion.py -- "reads the stream" is not the law;
emptiness is generic (row-uniform functions of the deficit value
alone also break it) and value-only future reads keep it, so the
door's surviving signature is class-level: only a beyond-geometry
loss can score a geometry-colliding class differently across two
rows.)
Tier: the collapse and coarsening lemmas are proved; everything
else is exact and exhaustive at the stated scope only.

Run record: run 1 exit 1 -- truth unresolved at depth 200, the
sq/phi double-depth-convergent effect, fixed by depth 300; run 2
exit 0, all controls green, 0.6s.
"""

import math
import time

LN2 = math.log(2)
INF_P = None          # patience sentinel: refuse the class
N0 = 8                # loss counted from this step
HORIZON = 120
DEEP = 300            # digit depth for truth resolution (the sq/phi
                      # cut is a double-depth convergent: depth ~2n)
AX_BASE = [0, 1, 2, 3, INF_P]

# ----------------------------------------------------------------- #
# exact interval / cover machinery (verbatim engine core)
# ----------------------------------------------------------------- #

def lt(a, b):
    return a[0] * b[1] < b[0] * a[1]

def frac_eq(a, b):
    return a[0] * b[1] == b[0] * a[1]

def mediant(a, b):
    return (a[0] + b[0], a[1] + b[1])

def ln_int(x):
    """ln of a positive big integer without overflow."""
    b = x.bit_length()
    if b <= 900:
        return math.log(x)
    return math.log(x >> (b - 64)) + (b - 64) * LN2

def cf_digits(head, period, count):
    digs = list(head)
    while len(digs) < count:
        digs.extend(period)
    return digs[:count]

STREAMS = {
    "phi":   ([1], [1]),
    "sqrt2": ([1], [2]),
    "sqrt3": ([1], [1, 2]),
    "theta8": ([0], [8]),
}

def fib_word(count):
    """CF digits from the Fibonacci word over {1, 2}: the fixed
    point of the morphism 1 -> 12, 2 -> 1 (prefix-stable)."""
    w = "1"
    while len(w) < count:
        w = "".join("12" if ch == "1" else "1" for ch in w)
    return [int(ch) for ch in w[:count]]

def stream_digits(name, count):
    if name == "fib":
        return fib_word(count)
    return cf_digits(*STREAMS[name], count=count)

def cylinders(digs):
    """Exact cylinder intervals: after digits a_0..a_n the interval
    spans p_n/q_n to (p_n+p_{n-1})/(q_n+q_{n-1})."""
    p2, q2, p1, q1 = 0, 1, 1, 0
    out = []
    for a in digs:
        p, q = a * p1 + p2, a * q1 + q2
        e1, e2 = (p, q), (p + p1, q + q1)
        out.append((e1, e2) if lt(e1, e2) else (e2, e1))
        p2, q2, p1, q1 = p1, q1, p, q
    return out

MAPS = {
    "id":  lambda e: e,
    "sq":  lambda e: (e[0] * e[0], e[1] * e[1]),
    "dbl": lambda e: (2 * e[0], e[1]),
}

def images(rows_digits, map_name):
    f = MAPS[map_name]
    out = []
    for lo, hi in rows_digits:
        a, b = f(lo), f(hi)
        out.append((a, b) if lt(a, b) else (b, a))
    return out

ROOT = ("T", (0, 1), (1, 0), 0)

def interval(cell):
    if cell[0] == "T":
        return cell[1], cell[2]
    _, v, l, r, _, k = cell
    mL = (l[0] + k * v[0], l[1] + k * v[1])
    mR = (r[0] + k * v[0], r[1] + k * v[1])
    return mL, mR

def rank(cell):
    return cell[3] if cell[0] == "T" else cell[4] + cell[5]

def contains(cell, J):
    lo, hi = interval(cell)
    return lt(lo, J[0]) and lt(J[1], hi)

def length_pair(cell):
    """(num, den) of the interval length, or None for infinite."""
    lo, hi = interval(cell)
    if hi[1] == 0:
        return None
    return hi[0] * lo[1] - lo[0] * hi[1], hi[1] * lo[1]

def max_k(A, B):
    """Largest k >= 1 with k*A < B; 0 if none; None if all k."""
    if A <= 0:
        return None if A < B else 0
    if B <= A:
        return 0
    return (B - 1) // A

def chain_kmax(v, l, r, J):
    """Largest k >= 1 with S_k(v) containing J; 0 if none."""
    (a, b), (c, d) = J
    kL = max_k(b * v[0] - a * v[1], a * l[1] - b * l[0])
    kR = max_k(c * v[1] - d * v[0], d * r[0] - c * r[1])
    if kL == 0 or kR == 0:
        return 0
    if kL is None and kR is None:
        raise AssertionError("straddle contains J at every index")
    if kL is None:
        return kR
    if kR is None:
        return kL
    return min(kL, kR)

def run_reader(J_list, policy, horizon):
    """Run one policy over one image stream, unthrottled. Returns
    (loss_num, loss_den, inf_flag, trace) with trace entries
    (rank, chain_index, (lo, hi))."""
    s_t, s_s, pt, pc = policy
    C = ROOT
    num, den, inf = 1, 1, False
    trace = []
    for n in range(horizon):
        J = J_list[n]
        ref_t = J_list[n - pt] if pt is not None and n - pt >= 0 else None
        ref_c = J_list[n - pc] if pc is not None and n - pc >= 0 else None
        guard = 0
        while True:
            guard += 1
            if guard > 10 ** 6:
                raise AssertionError("commit loop runaway")
            cand_tree = cand_chain = None
            if C[0] == "T":
                _, l, r, d = C
                v = mediant(l, r)
                if ref_t is not None:
                    for ch in (("T", l, v, d + 1), ("T", v, r, d + 1)):
                        if contains(ch, ref_t):
                            cand_tree = ch
                            break
                if ref_c is not None:
                    k = chain_kmax(v, l, r, ref_c)
                    if k >= 1:
                        cand_chain = ("S", v, l, r, d, k)
                prefer_chain = (s_t == 1)
            else:
                _, v, l, r, d, k = C
                if ref_c is not None:
                    k2 = chain_kmax(v, l, r, ref_c)
                    if k2 > k:
                        cand_chain = ("S", v, l, r, d, k2)
                if ref_t is not None:
                    mL, mR = interval(C)
                    for ch in (("T", mL, v, d + k + 1),
                               ("T", v, mR, d + k + 1)):
                        if contains(ch, ref_t):
                            cand_tree = ch
                            break
                prefer_chain = (s_s == 0)
            if cand_tree is None and cand_chain is None:
                break
            if cand_chain is not None and (cand_tree is None or prefer_chain):
                C = cand_chain
            else:
                C = cand_tree
        clo, chi = interval(C)
        if lt(J[0], clo) or lt(chi, J[1]):
            raise AssertionError("commitment lost the image")
        if n >= N0:
            lp = length_pair(C)
            if lp is None:
                inf = True
            else:
                num *= lp[0]
                den *= lp[1]
        trace.append((rank(C), C[5] if C[0] == "S" else 0, (clo, chi)))
    return num, den, inf, trace

# ----------------------------------------------------------------- #
# rows and spaces
# ----------------------------------------------------------------- #

ROWS8 = [
    ("id",  "phi"), ("id", "sqrt2"), ("id", "sqrt3"), ("id", "theta8"),
    ("sq",  "sqrt2"),
    ("sq",  "phi"), ("dbl", "phi"), ("dbl", "sqrt2"),
]
FIB_ROW = ("dbl", "fib")
ROWS = ROWS8 + [FIB_ROW]
ID_ROWS = [r for r in ROWS if r[0] == "id"]

def build_images(depth):
    names = set(s for (m, s) in ROWS)
    cyl = {s: cylinders(stream_digits(s, depth)) for s in names}
    return {(m, s): images(cyl[s], m) for (m, s) in ROWS}

def policy_space4(axis):
    return [(st, ss, pt, pc)
            for st in (0, 1) for ss in (0, 1)
            for pt in axis for pc in axis]

def fmt_pol(p):
    return "(%d,%d,%s,%s)" % (
        p[0], p[1],
        "INF" if p[2] is None else str(p[2]),
        "INF" if p[3] is None else str(p[3]))

def fmt_row(row):
    return "%s/%s" % row

def cmp_lex(a, b):
    """Lexicographic deficit comparison: finite beats infinite; two
    infinites compare their finite parts (the shortfall)."""
    if a[2] != b[2]:
        return 1 if a[2] else -1
    left = a[0] * b[1]
    right = b[0] * a[1]
    return -1 if left < right else (1 if left > right else 0)

# ----------------------------------------------------------------- #
# the next-side loss
# ----------------------------------------------------------------- #

def truth_targets(J_deep):
    """Per counted step n in [N0, HORIZON): the cut (mediant of
    J_n's endpoints) and the truth side of the image point, read by
    deepening. Asserts the cut interior to J_n and the exclusion
    found."""
    cuts = []
    sides = []
    for n in range(N0, HORIZON):
        lo, hi = J_deep[n]
        assert hi[1] != 0, "infinite image interval"
        cut = mediant(lo, hi)
        assert lt(lo, cut) and lt(cut, hi), "cut not interior"
        side = None
        for m in range(n + 1, len(J_deep)):
            mlo, mhi = J_deep[m]
            if not lt(cut, mhi):       # J_m entirely at or left of cut
                side = "L"
                break
            if not lt(mlo, cut):       # J_m entirely at or right of cut
                side = "R"
                break
        assert side is not None, "truth unresolved at depth %d" % len(J_deep)
        cuts.append(cut)
        sides.append(side)
    return cuts, sides

def guess_side(clo, chi, cut):
    """The state-only extractor: guess the wider side of the cut
    inside the cell [clo, chi]. Returns (side, tie_flag). An
    infinite right side wins; an exact tie guesses left."""
    if chi[1] == 0:
        return "R", False
    left_n = cut[0] * clo[1] - clo[0] * cut[1]
    left_d = cut[1] * clo[1]
    right_n = chi[0] * cut[1] - cut[0] * chi[1]
    right_d = chi[1] * cut[1]
    a = left_n * right_d
    b = right_n * left_d
    if a > b:
        return "L", False
    if b > a:
        return "R", False
    return "L", True

def score_trace(trace, cuts, sides):
    """(misses, ties, hits_vector) of a counted trace against a
    row's cuts and truth sides."""
    misses = 0
    ties = 0
    hits = []
    for i, n in enumerate(range(N0, HORIZON)):
        clo, chi = trace[n][2]
        g, tie = guess_side(clo, chi, cuts[i])
        if tie:
            ties += 1
        ok = (g == sides[i])
        if not ok:
            misses += 1
        hits.append(ok)
    return misses, ties, hits

# ----------------------------------------------------------------- #
# the behavioral quotient
# ----------------------------------------------------------------- #

def build_classes(imgs, targets):
    """Run every policy on every row; quotient by the tuple of
    counted committed-cell traces. Returns a list of class dicts:
    members, per-row counted cells, misses/ties/hits, deficit
    triple. Loss equality within a class is asserted."""
    space = policy_space4(AX_BASE)
    per_policy = {}
    for pol in space:
        row_data = {}
        for row in ROWS:
            num, den, inf, trace = run_reader(imgs[row], pol, HORIZON)
            counted = tuple(trace[n][2] for n in range(N0, HORIZON))
            cuts, sides = targets[row]
            m, t, hits = score_trace(trace, cuts, sides)
            row_data[row] = {"cells": counted, "miss": m, "tie": t,
                             "hits": hits, "deficit": (num, den, inf)}
        sig = tuple(row_data[row]["cells"] for row in ROWS)
        per_policy[pol] = (sig, row_data)
    classes = {}
    for pol, (sig, row_data) in per_policy.items():
        if sig not in classes:
            classes[sig] = {"members": [], "rows": row_data}
        else:
            for row in ROWS:
                assert classes[sig]["rows"][row]["miss"] == \
                    row_data[row]["miss"], "loss not class-constant"
        classes[sig]["members"].append(pol)
    out = list(classes.values())
    out.sort(key=lambda c: sorted(c["members"])[0].__repr__())
    return out

def check(name, ok, detail=""):
    tag = "PASS" if ok else "FAIL"
    print("  [%s] %s%s" % (tag, name, (" -- " + detail) if detail else ""))
    return ok

# ----------------------------------------------------------------- #
# E1: controls
# ----------------------------------------------------------------- #

def id_truth_expected(digs, n_first, n_last):
    """The independent truth route for identity-map rows: track
    convergents; next digit 1 puts the point on the side of the cut
    toward the far endpoint (p_n+p_{n-1})/(q_n+q_{n-1})."""
    p2, q2, p1, q1 = 0, 1, 1, 0
    ends = []
    for a in digs:
        p, q = a * p1 + p2, a * q1 + q2
        ends.append(((p, q), (p + p1, q + q1)))
        p2, q2, p1, q1 = p1, q1, p, q
    out = []
    for n in range(n_first, n_last + 1):
        e1, e2 = ends[n]
        cut = mediant(e1, e2)
        toward_far = "L" if lt(e2, cut) else "R"
        if digs[n + 1] == 1:
            out.append(toward_far)
        else:
            out.append("R" if toward_far == "L" else "L")
    return out

def e1_controls(imgs, targets):
    print("E1 CONTROLS")
    all_ok = True

    # C1: engine truth vs the convergent-tracker truth, id rows
    for row in ID_ROWS:
        digs = stream_digits(row[1], DEEP)
        exp = id_truth_expected(digs, N0, HORIZON - 1)
        got = targets[row][1]
        all_ok &= check("C1 truth cross-check %s" % fmt_row(row),
                        got == exp)
    for row in ROWS:
        s = "".join(targets[row][1])
        print("    truth %-10s %s" % (fmt_row(row), s))

    # C3: extractor unit checks
    g1 = guess_side((0, 1), (1, 1), (1, 3))
    g2 = guess_side((0, 1), (1, 0), (5, 1))
    g3 = guess_side((0, 1), (2, 1), (1, 1))
    all_ok &= check("C3 wider side", g1 == ("R", False))
    all_ok &= check("C3 infinite side", g2 == ("R", False))
    all_ok &= check("C3 exact tie", g3 == ("L", True))
    return all_ok

def e1_deficit_control(classes):
    """C2: reproduce the known result under the deficit on the same
    quotient: a universal argmin class with zero transfer gaps and
    the greedy-patience policies inside it."""
    print("  C2 deficit reproduction")
    ok = True
    argmin = {}
    for ri, row in enumerate(ROWS):
        best = None
        ids = []
        for ci, c in enumerate(classes):
            d = c["rows"][row]["deficit"]
            if best is None or cmp_lex(d, best) < 0:
                best = d
                ids = [ci]
            elif cmp_lex(d, best) == 0:
                ids.append(ci)
        argmin[row] = set(ids)
    universal = set.intersection(*(argmin[row] for row in ROWS))
    ok &= check("universal deficit class exists", len(universal) > 0,
                "%d class(es)" % len(universal))
    greedy_cls = set()
    for ci, c in enumerate(classes):
        for pol in c["members"]:
            if pol[2] == 0 and pol[3] == 0:
                greedy_cls.add(ci)
    ok &= check("greedy classes inside the universal set",
                greedy_cls <= universal,
                "greedy classes: %d" % len(greedy_cls))
    return ok

def e1_witness_scan(classes):
    """C4: the dominance-break witness -- a (row, step, cell pair)
    where the strictly tighter cell misses and the coarser hits."""
    print("  C4 dominance-break witness scan")
    total = 0
    first = None
    for row in ROWS:
        for i in range(HORIZON - N0):
            seen = []
            for c in classes:
                cell = c["rows"][row]["cells"][i]
                hit = c["rows"][row]["hits"][i]
                seen.append((cell, hit))
            uniq = []
            have = set()
            for cell, hit in seen:
                key = (cell, hit)
                if key not in have:
                    have.add(key)
                    uniq.append((cell, hit))
            for (ca, ha) in uniq:
                for (cb, hb) in uniq:
                    if ca == cb:
                        continue
                    alo, ahi = ca
                    blo, bhi = cb
                    inside = (not lt(blo, alo)) and (not lt(bhi, ahi))
                    equal = frac_eq(alo, blo) and (
                        ahi[1] == 0 and bhi[1] == 0 or
                        (ahi[1] != 0 and bhi[1] != 0 and
                         frac_eq(ahi, bhi)))
                    if inside and not equal and ha and not hb:
                        total += 1
                        if first is None:
                            first = (row, N0 + i, ca, cb)
    found = total > 0
    check("dominance-break witness found", found,
          "%d witness site(s)" % total)
    if first is not None:
        row, n, ca, cb = first
        print("    first: %s step %d coarse hits, tight misses"
              % (fmt_row(row), n))
    return found

# ----------------------------------------------------------------- #
# E2: the argmin census
# ----------------------------------------------------------------- #

def census(classes):
    print("E2 THE ARGMIN CENSUS (%d behavior classes, %d policies)"
          % (len(classes), sum(len(c["members"]) for c in classes)))
    argmin_pure = {}
    argmin_comp = {}
    for row in ROWS:
        losses = [(c["rows"][row]["miss"], ci)
                  for ci, c in enumerate(classes)]
        best = min(m for m, _ in losses)
        worst = max(m for m, _ in losses)
        vals = sorted(m for m, _ in losses)
        med = vals[len(vals) // 2]
        pure = [ci for m, ci in losses if m == best]
        bestd = None
        comp = []
        for ci in pure:
            d = classes[ci]["rows"][row]["deficit"]
            if bestd is None or cmp_lex(d, bestd) < 0:
                bestd = d
                comp = [ci]
            elif cmp_lex(d, bestd) == 0:
                comp.append(ci)
        argmin_pure[row] = set(pure)
        argmin_comp[row] = set(comp)
        ties = max(classes[ci]["rows"][row]["tie"] for ci in pure)
        greedy_in = any(pol[2] == 0 and pol[3] == 0
                        for ci in pure for pol in classes[ci]["members"])
        print("  %-10s best %3d worst %3d median %3d | argmin %d/%d"
              " (comp %d) | ties@win %d | greedy in argmin: %s"
              % (fmt_row(row), best, worst, med, len(pure),
                 len(classes), len(comp), ties,
                 "yes" if greedy_in else "NO"))
    uni_pure = set.intersection(*(argmin_pure[row] for row in ROWS))
    uni_comp = set.intersection(*(argmin_comp[row] for row in ROWS))
    print("  UNIVERSAL INTERSECTION pure: %d class(es); composite: %d"
          % (len(uni_pure), len(uni_comp)))
    uni8 = set.intersection(*(argmin_pure[row] for row in ROWS
                              if row != FIB_ROW))
    print("  argmin intersection over the eight non-fib rows: %d"
          % len(uni8))
    print("  transfer gap matrix (rows: source argmin; cols: target;"
          " entry = min extra misses):")
    hdr = "            " + " ".join("%6s" % fmt_row(r)[:6] for r in ROWS)
    print("  " + hdr)
    for r in ROWS:
        cells = []
        for s in ROWS:
            best_s = min(c["rows"][s]["miss"] for c in classes)
            gap = min(classes[ci]["rows"][s]["miss"]
                      for ci in argmin_pure[r]) - best_s
            cells.append("%6d" % gap)
        print("    %-10s %s" % (fmt_row(r), " ".join(cells)))
    return argmin_pure, argmin_comp, uni_pure, uni_comp

# ----------------------------------------------------------------- #
# E3: the price
# ----------------------------------------------------------------- #

def price(classes, argmin_pure, argmin_comp):
    print("E3 THE PRICE")
    for label, argmin in (("pure", argmin_pure), ("composite",
                                                  argmin_comp)):
        blocks = {}
        for row in ROWS:
            key = frozenset(argmin[row])
            blocks.setdefault(key, []).append(row)
        print("  readability partition (%s): %d block(s)"
              % (label, len(blocks)))
        for key, rows in sorted(blocks.items(),
                                key=lambda kv: fmt_row(kv[1][0])):
            print("    {%s} argmin set size %d"
                  % (", ".join(fmt_row(r) for r in rows), len(key)))
    print("  per-state readability (pure argmin members):")
    for row in ROWS:
        excl = 0
        for ci in argmin_pure[row]:
            rows_of = [r for r in ROWS if ci in argmin_pure[r]]
            if rows_of == [row]:
                excl += 1
        print("    %-10s %d/%d argmin classes row-exclusive"
              % (fmt_row(row), excl, len(argmin_pure[row])))
    pooled = [(sum(c["rows"][row]["miss"] for row in ROWS), ci)
              for ci, c in enumerate(classes)]
    pbest = min(p for p, _ in pooled)
    winners = [ci for p, ci in pooled if p == pbest]
    print("  pooled loss: best %d, winners %d class(es)"
          % (pbest, len(winners)))
    for row in ROWS:
        best_r = min(c["rows"][row]["miss"] for c in classes)
        pooled_r = min(classes[ci]["rows"][row]["miss"]
                       for ci in winners)
        regret = pooled_r - best_r
        if regret > 0:
            spec = [ci for ci, c in enumerate(classes)
                    if c["rows"][row]["miss"] == best_r]
            excess = min(sum(classes[ci]["rows"][r]["miss"]
                             for r in ROWS) for ci in spec) - pbest
            print("    %-10s specialist advantage %d, pooled excess %d"
                  % (fmt_row(row), regret, excess))
        else:
            print("    %-10s pooled winner is row-optimal" % fmt_row(row))

# ----------------------------------------------------------------- #

def main():
    t0 = time.time()
    print("THE PREDICTION DOOR -- the next-side loss on the reader"
          " family")
    print("rows: %s" % ", ".join(fmt_row(r) for r in ROWS))
    print("policies: %d, horizon %d, counted from %d, truth depth %d"
          % (len(policy_space4(AX_BASE)), HORIZON, N0, DEEP))
    print()
    imgs = build_images(DEEP)
    targets = {row: truth_targets(imgs[row]) for row in ROWS}
    ok = e1_controls(imgs, targets)
    classes = build_classes(imgs, targets)
    ok &= e1_deficit_control(classes)
    e1_witness_scan(classes)
    if not ok:
        print("CONTROL FAILURE -- stop; no verdict may be read.")
        raise SystemExit(1)
    print()
    argmin_pure, argmin_comp, uni_pure, uni_comp = census(classes)
    print()
    price(classes, argmin_pure, argmin_comp)
    print()
    print("done in %.1fs" % (time.time() - t0))

if __name__ == "__main__":
    main()
