"""Which half of the readability gate carries the content.

THE QUESTION
------------
The reading geometry states one gate across every numeration window it
has: a map is READABLE AT BOUNDED DELAY iff it acts CONTINUOUSLY on
the window's completion. Every unreadability result behind that
statement is argued the same way — exhibit two input sequences
converging to one point whose images converge to two, so no continuous
extension exists. That is DISCONTINUOUS => UNREADABLE, i.e. the
contrapositive of READABLE => CONTINUOUS, and none of it touches the
other half. This asks which half carries the content, and what the
gate says once that is settled.

THE OBJECTS, fixed
------------------
A WINDOW is a nested partition of the nonnegative integers: the
depth-t cell of n is its first t digits in the window's numeration.
Two windows shapes are used. A CF WINDOW has weights
q_k = a_k q_{k-1} + q_{k-2} from a partial-quotient sequence, digits
greedy, legality b_0 <= a_1 - 1, b_k <= a_{k+1}, and b_k = a_{k+1}
forcing b_{k-1} = 0. A POSITIONAL WINDOW has weights q_k = b^k and
digits 0..b-1.

X is the inverse limit of the depth-t partitions: compatible sequences
of cells. It is compact (an inverse limit of finite sets), the
integers sit densely in it, and the natural metric is the ultrametric
d(x, y) = 2^{-agr(x, y)} with agr the agreement depth.

For a map f on the integers, c_min(f, t) is the least c with
    agr(n, n') >= t + c  =>  agr(f n, f n') >= t,
the quantity every window rig in the corpus already prints. READABLE
AT BOUNDED DELAY means one c serves every t.

THE HAND-ATTACK, before any engine
----------------------------------
H1. The delay statement is metric, not merely topological. Delay c
    says exactly d(f x, f y) <= 2^c d(x, y): f is LIPSCHITZ with
    constant 2^c. A Lipschitz map on a dense subset of a complete
    space extends uniquely, with the same constant. So READABLE AT
    BOUNDED DELAY => CONTINUOUS is one line, and every unreadability
    theorem in the corpus is that one line's contrapositive.

H2. The converse cannot be that line read backwards. X is compact, so
    continuous = uniformly continuous, which buys a MODULUS: some
    s(t) with agreement to depth s(t) forcing image agreement to
    depth t. Bounded delay needs s(t) <= t + c. Nothing about
    compactness or ultrametricity forces the modulus to be that
    tight, so the two conditions are not the same condition unless
    the class of maps makes them so.

H3. And they are not — and the corpus ALREADY KNOWS THIS one section
    up, which is the real defect being chased here. The reading
    lemma's own rig (explore_reading_geometry.py) carries the
    even-position digit extraction as its witness that the reading
    criterion is METRIC AND NOT TOPOLOGICAL, uniformly continuous
    with unbounded Lipschitz exponent, and the abstract-window
    section states it outright. The gate one section down was
    nonetheless written as CONTINUITY. So this rig has two halves:
    re-derive that witness independently and exactly, then measure
    what the gate was actually resting on. Take the
    positional window b = 2 and the
    DECIMATION map D(n) = sum_t d_{2t}(n) 2^t, which reads the
    even-indexed binary digits of n and packs them down. D sends
    integers to integers. Its depth-t image digit e_{t-1} is d_{2t-2}
    and nothing else, so agreement to depth 2t-1 forces image
    agreement to depth t, and a pair differing only at position 2t-2
    agrees to depth 2t-2 with images differing at depth t. Hence
    c_min(D, t) = (2t - 2) - t + 1 = t - 1, exactly: finite at every
    t, unbounded in t. D is continuous and is NOT readable at bounded
    delay.

H4. So the gate's stated form is false in the direction nobody
    tested, and the repair is a WORD: readable at bounded delay iff
    the map extends to a LIPSCHITZ self-map of the completion, the
    minimal delay being the base-2 logarithm of the constant. Both
    halves are then one line each. Whatever content the gate carries
    is not in either half.

H5. Where the content goes. Write the three classes a map can fall
    in: LIPSCHITZ (readable at bounded delay), MIDDLE (continuous,
    modulus unbounded — readable only at a growing lookahead), and
    DISCONTINUOUS (unreadable at ANY modulus, however fast-growing).
    H3 inhabits MIDDLE. The gate as the corpus uses it is then the
    claim that on the ARITHMETIC maps — multiplication, floor
    division, digit shifts — the MIDDLE class is EMPTY, so that
    "continuous" and "Lipschitz" cannot be told apart there. That is
    a claim about the MAPS and not about the topology, it has never
    been stated, and it is measurable.

H6. The measurement H5 needs is a second reading of a table the rigs
    already print. Read c_min(f, t) along a COLUMN — t fixed, range N
    growing — and it settles iff f is continuous, since c_min(f, t)
    is the finite lookahead the modulus assigns to depth t and a
    quantity growing without bound at a FIXED t is the failure of
    that modulus to exist. Read it along a ROW — N fixed, t growing —
    and it is constant iff f is Lipschitz. MIDDLE is
    column-settling and row-growing at once. The corpus's existing
    discriminator reads the DIAGONAL (deepest realized agreement
    against the data cap) and by construction cannot separate MIDDLE
    from DISCONTINUOUS.

H7. A free consequence to check rather than assume: if the corpus's
    combs really do refute CONTINUITY, then every map they kill is
    unreadable at any modulus, which is strictly stronger than the
    bounded-delay statement those theorems are recorded as making.

TRANSPLANT, marked: P4 and P5 below carry the word "gated" over from
the rigs that measured along the diagonal. The column reading is new,
and it is exactly what a transplanted verdict could get wrong — a
diagonal-gated map that turns out column-settling is MIDDLE, not
unreadable, and would be the first arithmetic member of that class.

PREDICTIONS, frozen before the engine
-------------------------------------
P1  CONTROL. c_min(id, t) = 0 at every window, every t, every N; and
    c_min(2n, t) = 0 at the base-10 window, where multiplication by
    any integer is the textbook delay-0 read. Either failing means
    the instrument is wrong and no verdict below is readable.
P2  THE WITNESS, exact. At b = 2, c_min(D, t) = t - 1 at every t once
    the range admits a witness pair (N > 2^{2t-1}), and that value
    does not move as N grows. KILL: any t where the printed value
    differs from t - 1, or moves with N. H3 is a derivation, so a
    miss here is a defect in the derivation or in the rig, not a
    finding.
P3  THE MIDDLE CLASS IS INHABITED. From P2: D is column-settling and
    row-growing. The gate's stated form is refuted at a row of its
    own table.
P4  THE ARITHMETIC MAPS AVOID IT. For 2n, 3n and n//2 at the four CF
    windows, there is a fixed t at which c_min grows across the three
    ranges with no plateau — DISCONTINUOUS, not MIDDLE. KILL: every
    map at some window settles at every fixed t while still growing
    in t, which puts an arithmetic map in MIDDLE and is a larger find
    than the one predicted.
P5  THE REPAIRING CELLS ARE LIPSCHITZ, NOT MIDDLE. The shift cells
    recorded as needing legality repair and reading at bounded delay
    anyway are row-CONSTANT: c_min(L_r, t) does not grow with t, so
    their delay IS a Lipschitz constant above 1. KILL: row-growing
    at any of them, which would mean the recorded bounded-delay
    reading was a data-cap artifact.
P6  THE B-ADIC ROW HAS AN EMPTY MIDDLE, MEASURED. At b = 10, n//v
    for v = 2, 4, 5 is row-constant and n//v for v = 3, 6, 7 is
    column-growing at a fixed t, with nothing in between.

DESIGN
------
Windows: the four CF windows the fourth storey uses (phi-1, cbrt(2)-1
certified by interval arithmetic over exact rationals, e-2 likewise,
and the exploding a_k = 2^k), plus positional b = 2 and b = 10.

c_min is computed exactly, not sampled. Sorting the integers by their
digit tuple with position 0 most significant makes every depth-p cell
a contiguous block, so if two members of a cell have different depth-t
images then some CONSECUTIVE pair inside it does; scanning consecutive
pairs therefore finds the true maximum agreement depth at each t.
Digit strings are cut at depth t_max + C_MAX + 2 so an agreement depth
is never truncated below the largest delay the table can report.

Per window the usable depth K(N) — the largest t with q_t <= N — is
computed and printed, and every table is read only to t <= K(N) - 1,
since a deeper column is vacuous zeros that read as perfect agreement.

E1  CONTROLS AND SANITY. Greedy digits reconstruct n exactly and
    satisfy the window's legality, all n < N, every window. c_min(id)
    and the base-10 2n calibration print BEFORE any verdict.
E2  THE TWO READINGS. For every window and every map in
    {n+1, 2n, 3n, n//2}, the c_min(f, t) row at each of
    N = 30000, 100000, 300000, stacked so the column read (fixed t
    down the three rows) and the row read (across t) are both on the
    page. This is the whole instrument; E4 and E5 are the same table
    at other maps.
E3  THE WITNESS. c_min(D, t) at b = 2 over the same three ranges,
    against the frozen closed form t - 1.
E4  THE B-ADIC ROW. c_min(n//v, t) at b = 10 for v = 2..7, three
    ranges — the row whose gate is stated as rad(v) | rad(b).
E5  THE REPAIRING SHIFT CELLS. c_min(L_r, t) for r = 1..4 at the
    cubic and at e-2, three ranges, with the repair count beside it,
    so a bounded reading is seen to be range-stable rather than
    cap-shaped.

RESOURCE: the cost is one greedy descent per (window, map, input),
each costing the digit count rather than the weight-list length; six
windows times three ranges times up to seven maps at N <= 300000.
Estimate 4-8 minutes wall. Memory is digit tuples only, no numpy and
no BLAS; the per-range lists are rebuilt and dropped between windows,
so the peak is one range's worth — the sibling rig of this shape
peaked at 280MB against the 512MB ceiling, and this one is run under
memwatch for the same reason.

RUN RECORD
----------
Two rounds. E1-E5 first, all controls green before any verdict was
read. Then E6, added on reading E2's prints: a COLUMN read is
informative only where the deepest realized agreement CAP moved
between the two ranges, and at round-number ranges it does not always
— at W1 the usable depth is 12 at both N = 100000 and N = 300000, so
that column stands still for want of range and not for want of
growth. E6 indexes the ranges by DEPTH instead, N = q_(K+1) - 1 at
three successive K, which moves the cap by one per step by
construction. P7 was frozen before E6 ran. Wall 26.8 s for E1-E5,
41.1 s for the rig as it stands; peak working set 250.4 MB against
memwatch's 512 MB ceiling. The 4-8 minute estimate overshot by about
8x, for the reason the sibling rig recorded: the greedy descent starts
at the largest weight below v, so it costs the digit count and not the
built weight-list length.
E1 green at every window: zero reconstruction failures, zero legality
failures, c_min(id) = 0 at every window and depth, and the base-10
calibration c_min(2n) = 0 at every depth. P1 lands.
A SECOND INSTRUMENT CEILING, which decides where a column may be
read: T_MAX = 10 does NOT move when E6 moves the cap, so at a depth t
near the top of the table a stalled A(t) can be the table's own ceiling
rather than a settling modulus — pairs agreeing deeper have images
agreeing past t_max and leave the maximum. Every column verdict below
is therefore read at t = 1 or t = 2, where no such censoring can reach,
and a stall higher up is not read as evidence either way. The visible
instance is E5's stride 1 at e - 2, where A(2) stands at 13 while the
cap moves 13 -> 15; nothing here rests on it.
ONE INSTRUMENT CEILING, named rather than buried: digit strings are
cut at depth t_max + C_MAX + 2 = 24, so a realized agreement deeper
than 24 cannot be seen. At W0 the usable depth passes that (24, 25,
26 at the three E6 ranges) and CAP saturates at 24. W0's arithmetic
columns are off-scale at every t >= 2 and every range regardless, so
W0 serves here as a calibration against a window whose gate is
already a theorem, and no growth reading is taken from it.

FINDINGS (each at its own tier)
-------------------------------
F1  THE TWO HALVES ARE NOT PEERS (theorem, and the identity is the
    corpus's own — the reading lemma already states readability at
    lookahead c as verbatim Lipschitz 2^c). Delay c is exactly the
    Lipschitz bound d(f x, f y) <= 2^c d(x, y), and a Lipschitz map
    on a dense subset of a complete space extends uniquely with the
    same constant. So READABLE AT BOUNDED DELAY iff f extends to a
    LIPSCHITZ self-map of the completion — both directions one line,
    the minimal delay being log2 of the constant. The half the corpus
    argues, readable => continuous, is the weaker of the two and is
    that line; every unreadability result behind the gate is its
    contrapositive.
F2  THE MIDDLE CLASS IS INHABITED, SO THE STATED IFF IS FALSE
    (theorem, already owned by the reading lemma's rig and here
    RE-DERIVED independently and confirmed to the digit — the value
    of the re-derivation being that it is taken in the GATE's own
    observable, c_min, which is what makes the two sections
    commensurable). At b = 2 the decimation D printed
    c_min(D, t) = t - 1 on the in-scope prefix at all three ranges —
    matched to t = 7, 8, 9 as the range admits, reaching the full row
    0 1 2 3 4 5 6 7 8 9 at N = 300000 — and the value at each fixed t
    does not move once its witness exists. D is continuous (modulus
    s(t) = 2t - 1) and readable at NO bounded delay. Continuity is
    strictly weaker than the gate's own conclusion, and the gate's
    stated form fails at a positional row of its own table — which a
    section above it had refuted before the gate was written. P2 and
    P3 land.
F3  SO THE GATE'S CONTENT IS THE EMPTY MIDDLE ON THE ARITHMETIC MAPS,
    AND THAT IS NOW MEASURED (rule at scanned scope). The b-adic row
    splits with nothing between the halves: n//v at b = 10 is
    row-constant at 1, 2, 1 for v = 2, 4, 5 and cap-shaped for
    v = 3, 6, 7 (4 3 2 -> 4 3 2 1 -> 5 4 3 2, the deepest agreement
    A(1) reading 4, 4, 5 against E4's caps 4, 4, 5),
    which is exactly rad(v) | rad(10) and no third behaviour. At the
    four CF windows 2n, 3n and n//2 are cap-shaped at every window
    under E6's moving cap. P4 and P6 land. The gate, as the corpus
    uses it, is therefore a claim about the MAPS — that arithmetic
    never lands in MIDDLE — and not about the topology.
F4  THE DISCRIMINATOR IS THE CAP GAP, AND P7'S FORM IS AN HONEST MISS
    (rule at scanned scope). P7 said a discontinuous map's fixed-t
    column RISES at every step of a moving cap. It does not always:
    at W1, c_min(2n, 1) reads 10, 11, 11 against caps 10, 11, 12, and
    3n the same. The quantity that behaves is CAP - c_min, bounded
    and small for a discontinuous map (0, 0, 1 there) and growing
    with the cap for a continuous one (n+1 at W1: 9, 10, 11; the
    witness D settles outright, its fixed-t value not moving at all
    once the range admits it). P7 was also self-contradictory at
    B10, where 2n and 3n are Lipschitz by the b-adic gate and were
    never going to rise — the prediction lumped a positional window
    in with the CF ones. Direction lands, form misses, the same shape
    of miss the sibling rig recorded at its P9: an observable frozen
    one notch too strong.
F5  THE REPAIRING CELLS ARE LIPSCHITZ, AND THE REPAIR COUNT IS
    PROVABLY NOT WHAT DECIDES THEM (rule at scanned scope — the
    open question this leg was aimed at). At e - 2, strides 1 and 2
    repair the IDENTICAL number of inputs at every range — 29390,
    99390, 298403 — and their verdicts are opposite: stride 1 is
    cap-shaped — A(t) pinned at one value across the whole row, 10
    then 13 then 13 against E2's caps 13, 13, 15 — while stride 2
    prints c_min = 0 at every depth and every range. An isometry
    that repairs 99.5 percent of its inputs sits beside an unbounded
    map that repairs the same ones. Same window, same count, opposite
    verdict: the count is excluded exactly, not approximately. At the
    cubic the bounded strides are Lipschitz with a constant above 1
    and the constant is LOCAL — stride 2 prints 0 0 0 0 1 0 0 0 0 0
    and stride 4 prints 0 0 3 2 1 0 0 0 0 0, both unchanged across
    all three ranges, so the delay is attained at one depth and is 0
    elsewhere. P5 lands. What survives as the reading: a repair
    decides nothing by its extent, only by whether its cascade
    imports information from above the digit it lands on.
F6  WHY THE STOREYS COULD CLAIM AS MUCH AS THEY DO (theorem, by
    re-reading; no correction attached). Every comb telescope and
    boundary family in the reading corpus refutes CONTINUITY — two
    inputs converging to one point whose images converge to two —
    which by F1's classes is the TOP kill, unreadable at any modulus
    however fast-growing. That is exactly what those theorems state,
    "unreadable at every depth and lookahead, no range cap", so none
    is understated and this finding corrects nothing. What the frame
    adds is the class BELOW: the one none of the corpus's machinery
    is aimed at, and the one an arithmetic map has never been shown
    to occupy.

THE READING. The question was which half of the iff carries the
content, and the answer is NEITHER. One half is a one-line metric
identity and the other is false, refuted at a positional row of the
gate's own table by a map that is continuous and needs a lookahead
growing without bound — and both facts were already the reading
lemma's, one section above the gate that contradicted them. Repairing the word
— Lipschitz for continuous —
makes the gate a theorem instead of a conjecture, and empties it: both
halves become one line each. What was doing the work all along is a
claim nobody had stated, that on the arithmetic maps the middle class
is empty, so that continuity and the Lipschitz condition cannot be
told apart there. That claim is now measured at the five windows the
arithmetic maps ran at, and it holds at every one. (Measured since,
2026-08, at a second family — the four quadratic trailing windows,
where it also holds at every tested map:
explore_quadratic_middle.py.) It also explains why the
conjecture looked
load-bearing: the corpus's own kills all land in the strongest class,
which makes the weak hypothesis look sufficient. And the leg's aimed
target, what decides a repairing cell, is closed on its most plausible
candidate and no further: at one window two strides repair the same
NUMBER of inputs, to the digit and at every range, and read at
opposite verdicts.
"""

from bisect import bisect_right
from fractions import Fraction

C_MAX = 12
T_MAX = 10
EXTRA = 10
RANGES = (30_000, 100_000, 300_000)


# ---------------------------------------------------------------- windows

def cf_certified(lo, hi, want):
    """Certified partial quotients of any x with lo < x < hi: a term is
    emitted only when the enclosure decides its floor."""
    out = []
    while len(out) < want:
        a = lo.numerator // lo.denominator
        if hi.numerator // hi.denominator != a and hi != a:
            break
        if lo - a <= 0:
            break
        out.append(a)
        lo, hi = Fraction(1) / (hi - a), Fraction(1) / (lo - a)
    return out


def icbrt(n):
    """Integer cube root by Newton descent."""
    x = 1 << ((n.bit_length() + 2) // 3 + 1)
    while True:
        y = (2 * x + n // (x * x)) // 3
        if y >= x:
            return x
        x = y


def quotients_cbrt2_minus_1(want):
    scale = 10 ** 400
    r = icbrt(2 * scale ** 3)
    lo, hi = Fraction(r, scale), Fraction(r + 1, scale)
    assert lo ** 3 < 2 < hi ** 3
    terms = cf_certified(lo - 1, hi - 1, want + 1)
    assert terms[0] == 0
    return terms[1:]


def quotients_e_minus_2(want):
    m, s, f = 400, Fraction(0), 1
    for k in range(m + 1):
        if k:
            f *= k
        s += Fraction(1, f)
    tail = Fraction(2, f * (m + 1))
    terms = cf_certified(s - 2, s + tail - 2, want + 1)
    assert terms[0] == 0
    return terms[1:]


WANT = 70


class Window:
    """A nested digit partition of the nonnegative integers."""

    def __init__(self, name, kind, a=None, base=None):
        self.name = name
        self.kind = kind            # "cf" or "pos"
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
        """Violations of the window's own legality conditions."""
        fails = 0
        if self.kind == "pos":
            return sum(1 for x in d if x > self.base - 1)
        a = self.a
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


WINDOWS = [
    Window("W0 phi-1      [0;1,1,1,...]   QUADRATIC", "cf", a=[1] * WANT),
    Window("W1 cbrt(2)-1  cubic           CERTIFIED", "cf",
           a=quotients_cbrt2_minus_1(WANT)),
    Window("W2 e-2        transcendental  CERTIFIED", "cf",
           a=quotients_e_minus_2(WANT)),
    Window("W3 a_k = 2^k  CF-defined      EXPLODING", "cf",
           a=[2 ** k for k in range(1, WANT + 1)]),
    Window("B2 base 2     POSITIONAL", "pos", base=2),
    Window("B10 base 10   POSITIONAL", "pos", base=10),
]


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
    """Largest t with q_t <= top."""
    t = 0
    while t + 1 < len(q) and q[t + 1] <= top:
        t += 1
    return t


class Frame:
    """One (window, range) frame: digits, sorted order, agreement depths."""

    def __init__(self, win, n):
        self.win, self.n = win, n
        self.kn = usable_depth(win.weights(200), n)
        self.tmax = min(T_MAX, self.kn - 1)
        self.depth = self.tmax + C_MAX + 2
        self.q = win.weights(self.kn + EXTRA)
        self.digits = [greedy(i, self.q) for i in range(n)]
        self.strings = [tuple(d[:self.depth]) for d in self.digits]
        self.order = sorted(range(n), key=lambda i: self.strings[i])
        self.agr = []
        for j in range(n - 1):
            s1, s2 = self.strings[self.order[j]], self.strings[self.order[j +
            1]]
            p = 0
            while p < self.depth and s1[p] == s2[p]:
                p += 1
            self.agr.append(p)
        self.cap = max(self.agr) if self.agr else 0

    def c_min(self, imgs):
        """c_min(f, t) for t = 1..tmax, exact over the range."""
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

    def images(self, f):
        return [tuple(greedy(f(i), self.q)[:self.tmax]) for i in range(self.n)]

    def row(self, f):
        return self.c_min(self.images(f))


def fmt(row):
    return " ".join(f"{('>' if c > C_MAX else str(c)):>2s}" for c in row)


def stacked(win, maps, extra=None):
    """The three-range c_min stack for one window: the whole instrument."""
    print("=" * 74)
    print(win.name)
    blocks = {name: [] for name, _ in maps}
    heads = []
    for n in RANGES:
        fr = Frame(win, n)
        heads.append((n, fr.kn, fr.tmax, fr.cap))
        if extra is not None:
            extra(fr)
        for name, f in maps:
            blocks[name].append((n, fr.tmax, fr.row(f)))
        del fr
    for n, kn, tmax, cap in heads:
        print(f"  N = {n:6d}: usable depth K(N) = {kn:2d}, "
              f"table to t = {tmax:2d}, deepest realized agreement "
              f"CAP = {cap}")
    for name, _ in maps:
        print(f"  {name}")
        for n, tmax, row in blocks[name]:
            print(f"    N = {n:6d}  t = 1..{tmax:<2d}  " + fmt(row))
    print()


# ------------------------------------------------------------ experiments

def e1_controls():
    print("=" * 74)
    print("E1 CONTROLS AND DIGIT SANITY (printed before any verdict)")
    for win in WINDOWS:
        fr = Frame(win, 30_000)
        recon = sum(1 for i in range(fr.n)
                    if sum(d * w for d, w in zip(fr.digits[i], fr.q)) != i)
        legal = sum(win.legality_failures(d) for d in fr.digits)
        idrow = fr.row(lambda i: i)
        print(f"  {win.name[:34]:34s} reconstruction failures {recon}, "
              f"legality failures {legal}, c_min(id) {fmt(idrow)}")
        del fr
    fr = Frame(WINDOWS[5], 100_000)
    print("  base-10 calibration c_min(2n): " + fmt(fr.row(lambda i: 2 * i)))
    del fr
    print()


ARITH = [("n+1", lambda i: i + 1), ("2n", lambda i: 2 * i),
         ("3n", lambda i: 3 * i), ("n//2", lambda i: i // 2)]


def e2_two_readings():
    print("=" * 74)
    print("E2 THE TWO READINGS: c_min(f, t) stacked over three ranges.")
    print("   COLUMN (one t, down the three N): settles => continuous.")
    print("   ROW    (across t at one N):    constant => Lipschitz.")
    for win in WINDOWS[:4]:
        stacked(win, ARITH)


def decimate(base):
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


def e3_witness():
    print("=" * 74)
    print("E3 THE WITNESS: decimation at b = 2, against the frozen "
          "closed form c_min(D, t) = t - 1")
    win = WINDOWS[4]
    D = decimate(2)
    for n in RANGES:
        fr = Frame(win, n)
        row = fr.row(D)
        pred = [t - 1 for t in range(1, fr.tmax + 1)]
        # P2's frozen scope: the closed form is claimed only where the
        # range admits a witness pair, N > 2^(2t-1). Past that the row
        # decays for want of inputs, which is a data cap and not a miss.
        scope = max((t for t in range(1, fr.tmax + 1) if 2 ** (2 * t - 1) < n),
                    default=0)
        ok = row[:scope] == pred[:scope]
        print(f"  N = {n:6d}  t = 1..{fr.tmax:<2d}  measured " + fmt(row))
        print(f"                            predicted " + fmt(pred))
        print(f"    in-scope prefix t <= {scope} (N > 2^(2t-1)): "
              f"match {ok}; beyond it the row decays for want of inputs")
        del fr
    print()


def e4_badic_row():
    print("=" * 74)
    print("E4 THE B-ADIC ROW: c_min(n//v, t) at b = 10, v = 2..7 "
          "(gate: rad(v) | rad(10))")
    maps = [(f"n//{v}", (lambda v: (lambda i: i // v))(v)) for v in range(2,
    8)]
    stacked(WINDOWS[5], maps)


def shift_map(fr, r):
    q = fr.q
    def f(i):
        d = fr.digits[i]
        return sum(d[k] * q[k + r] for k in range(len(q) - r) if d[k])
    return f


def e5_repairing_cells():
    print("=" * 74)
    print("E5 THE REPAIRING SHIFT CELLS: c_min(L_r, t) at three ranges, "
          "with the repair count")
    for win in WINDOWS[1:3]:
        print("-" * 74)
        print(win.name)
        for r in range(1, 5):
            for n in RANGES:
                fr = Frame(win, n)
                if len(fr.q) - r < 2:
                    del fr
                    continue
                f = shift_map(fr, r)
                repairs = 0
                imgs = []
                for i in range(n):
                    shifted = [0] * r + fr.digits[i][:len(fr.q) - r]
                    legal = greedy(f(i), fr.q)
                    if legal != shifted:
                        repairs += 1
                    imgs.append(tuple(legal[:fr.tmax]))
                row = fr.c_min(imgs)
                print(f"  stride {r}  N = {n:6d}  repairs "
                      f"{repairs:6d}/{n}  t = 1..{fr.tmax:<2d}  " + fmt(row))
                del fr
        print()


def e6_depth_indexed():
    """E6: the column read at ranges that force the cap to move.

    Added after reading E2's prints. A column read is informative only
    where the deepest realized agreement CAP actually moved between the
    two ranges, and at round-number ranges it does not always: at W1 the
    usable depth is 12 at both N = 100000 and N = 300000, so the flat
    column there is the cap standing still and says nothing either way.
    Here the ranges are indexed by DEPTH — N = q_(K+1) - 1 for three
    successive K, which makes the usable depth exactly K by construction
    — so every column is read across a cap that moved by one each step.

    PREDICTION P7, frozen before this run: with the cap forced to move,
    c_min(f, t) at fixed t RISES at every step for f in {2n, 3n, n//2}
    at every window — no plateau — while it stands still for n+1. KILL:
    any arithmetic map whose fixed-t column plateaus across a moving
    cap, which puts that map in MIDDLE rather than DISCONTINUOUS and is
    a larger find than the one predicted.
    """
    print("=" * 74)
    print("E6 DEPTH-INDEXED RANGES: the column read with the cap forced "
          "to move one depth per step")
    for win in WINDOWS[:4] + WINDOWS[5:]:
        q = win.weights(60)
        ktop = usable_depth(q, RANGES[-1])
        ks = [k for k in (ktop - 2, ktop - 1, ktop) if k >= 2]
        print("-" * 74)
        print(f"{win.name}   depths K = {ks}")
        rows = {name: [] for name, _ in ARITH}
        for k in ks:
            n = min(RANGES[-1], q[k + 1] - 1) if k + 1 < len(q) else RANGES[-1]
            fr = Frame(win, n)
            for name, f in ARITH:
                rows[name].append((k, n, fr.kn, fr.cap, fr.tmax, fr.row(f)))
            del fr
        for name, _ in ARITH:
            print(f"  {name}")
            for k, n, kn, cap, tmax, row in rows[name]:
                print(f"    K = {k:2d}  N = {n:6d}  usable {kn:2d}  "
                      f"CAP {cap:2d}  t = 1..{tmax:<2d}  " + fmt(row))
    print()


def main():
    e1_controls()
    e2_two_readings()
    e3_witness()
    e4_badic_row()
    e5_repairing_cells()
    e6_depth_indexed()


if __name__ == "__main__":
    main()
