"""The dual pole: the walls corpus at the archimedean window.

THE QUESTION
------------
By Ostrowski's theorem the rationals have one residue window per prime
(the finite places) plus exactly one archimedean window, where size,
sign, and order live. The primorial tower keeps every finite window and
deletes the archimedean one; its walls corpus (explore_size_transform.py,
explore_size_crystallization.py) measures exactly what that deletion
costs: which operations can still be read through residue windows.

This experiment builds the MIRROR object — the integers read ONLY
through the archimedean window — and asks whether the same walls
machinery runs there with exact laws. Deleting the finite places is
injective (an integer is its real embedding), exactly as the tower's
own deletion is injective (an integer is its residue vector), so the
dual object is about READABILITY, not information: the tower's walls
ask what channel-local reads compute; the dual's ask what
FINITE-PRECISION SIZE reads compute.

THE FINITE SECTIONS (the dual rungs). The size window at base b,
precision t reads n /= 0 as

    W_{b,t}(n) = (sign n, e, m),   e = floor(log_b |n|),
                 m = floor(|n| / b^(e+1-t))   (the t leading digits).

Where the tower's ladder ascends by adding residue windows, the dual
ladder ascends by adding digits of precision — a floating-point number
IS the dual rung. Shallow regime (e+1 <= t): the window is exact.
Deep fibers have length L = b^(e+1-t).

THE DESIGN
----------
Predictions fixed before the engine ran, each marked property / rule /
conjecture. Statements imported from the finite pole's corpus are
transplants and marked [T]; the engine also charts what is native to
this pole.

P1 [T, property] THE FIBER LEMMA: the fibers of W_{b,t} are
    sign-definite integer intervals of length exactly b^max(0,e+1-t).
    (Finite-pole mirror: channel-subset fibers are arithmetic
    progressions.)
P2 [T, rule] THE DUAL HIDING LAW: on a deep fiber, the bias of the
    event [n = r mod p] away from 1/p is < 1/L, and is EXACTLY zero on
    every deep fiber if and only if p | b (equal class counts on an
    interval of length L iff p | L, and p | b^j iff p | b). Mirror of
    the finite pole's sign-hiding law, where the bias is exactly zero
    iff channel 2 is among the unknown windows.
P3 [T, property] THE RESIDUE WALL: the residue map n mod p is
    non-constant on every fiber of length >= 2, and the predicate
    [p | n] is non-constant on every fiber of length > p — no deep
    size window reads any finite place exactly. Below the prime's own
    scale (L <= p) the predicate can leak (a fiber may miss every
    multiple): the shallow leak.
P4 [property + witnesses] THE EXPONENT-DETERMINACY SPLIT:
    e(a*b) - e(a) - e(b) is in {0, 1} — the product's exponent is
    determined up to one by exponents alone. The difference's exponent
    e(a-b) is undetermined by windows at ANY precision short of exact:
    two operands sharing one deep fiber realize differences across the
    fiber's whole exponent range, both signs, and zero. So equality,
    the zero-test of a difference, and comparison of nearby values are
    all unreadable — THE EQUALITY WALL. The finite pole's crown
    capability (the exact zero-test) is precisely this pole's blind
    spot, and "never test floating-point values for equality" is its
    folklore shadow.
P5 [rule-shape] GRADED LOCALITY: multiplication read at output
    precision t from operand windows at precision t+c has a NONZERO
    exception set for every lookahead c, with density decaying by a
    factor of about b per unit of c; the distinguisher between * and -
    is AMBIGUITY WIDTH, not density — a multiplication exception is
    confined to 2 adjacent output windows (one straddled boundary),
    while subtraction's ambiguity spans unboundedly many windows as
    fibers deepen (catastrophic cancellation as an exact statement).
P6 [conjecture] THE EXACT-LOCAL CLASS: the functions computable
    window-to-window with ZERO exceptions at some fixed lookahead, on
    all deep fibers, are exactly the base's own scalings
    {n -> s * b^j * n : s = +-1, j >= 0} together with constants.
    The finite pole's exact-local class is ALL polynomial functions;
    the dual pole's is a thin group — one pole's locality is
    algebraic, the other's measure-graded. In particular doubling is
    exactly local at base 2 and graded at base 10: exactness of a map
    is base-relative here, never so at the finite pole.
P7 [native, rule] THE TWO-ENDS LAW: base b's TRAILING digits read
    exactly the finite places p | b (n mod p is a function of the last
    digit block); its LEADING digits perfectly hide exactly the same
    places (P2). One numeration, two ends: the same primes exactly
    readable at one end and exactly invisible at the other.

Kill criteria, named at the freeze: P2's iff failing in either
direction kills the mirror; multiplication acquiring a zero-exception
lookahead (P5) collapses the graded/exact split. Positive controls:
the locality tester must classify n -> b*n as exactly local and
n -> n+1 as graded; the bias meter must report nonzero bias for some
p not dividing b.

Engine: pure python, exhaustive small ranges (bases 2, 3, 10;
precisions t <= 4; operands below 10^7), single process, seconds-scale.

THE FINDINGS
------------
Verdict: the dual pole is RICH. The walls machinery runs there with
exact mirror laws, and the pole carries one native unification with no
finite-pole counterpart. 132 checks green.

F1 THE FIBER LEMMA (property, exhaustive at bases 2, 3, 10): the
   fibers of W_{b,t} are sign-definite contiguous integer intervals of
   length exactly b^max(0, e+1-t). One fiber geometry per pole:
   arithmetic progressions hide size, intervals hide residue.
F2 THE DUAL HIDING LAW (rule; derived + exhaustive over the scanned
   depths): the bias of [n = r mod p] on a deep fiber is EXACTLY zero
   on every deep fiber iff p | b, and otherwise nonzero on every deep
   fiber with bias < 1/L (the printed maxima sit at the smallest
   scanned depth: 0.0208 = 2/(3*32) at b=2, p=3, L=32, the derived
   ceiling (p-1)/(pL) attained). Mirror of the finite pole's
   sign-hiding law (bias exactly zero iff channel 2 is unknown).
F3 THE RESIDUE WALL (property): no deep fiber decides any residue
   (the map is non-constant at length >= 2, the predicate [p | n] at
   length > p); below the prime's scale the predicate can leak — the
   fiber [4, 6) decides [7 | n] = False. The mirror of the size wall,
   with a shallow boundary the size wall does not have.
F4 THE EXPONENT-DETERMINACY SPLIT + THE EQUALITY WALL (property +
   witnesses): e(ab) - e(a) - e(b) lands in {0, 1} (proved by the
   two-sided bound b^(e_a+e_b) <= ab < b^(e_a+e_b+2); scanned below
   64 and 300 at bases 2 and 10) — the product's exponent is read
   from exponents alone, up to one. One deep fiber (L = 64, base 2)
   realizes difference exponents {0..5}, both signs, and zero:
   equality, comparison of nearby values, and the zero-test of a
   difference are unreadable at every precision short of exact. The
   finite pole's crown capability is exactly this pole's blind spot.
F5 GRADED LOCALITY (rule-shape, measured): multiplication read at
   output precision 2 has nonzero exceptions at every lookahead
   c = 1..5, density falling 0.8125 -> 0.0598 with consecutive ratios
   1.79-2.09 (the factor b = 2), and every exception a pair of
   ADJACENT windows (one straddled boundary; asserted, width <= 2
   always). Subtraction's max ambiguity width at the same precision
   grows 10 -> 18 -> 26 across fiber depths 3/5/7 — linear in depth,
   unbounded. Catastrophic cancellation is an AMBIGUITY-WIDTH
   phenomenon: multiplication's one boundary caps the spread of an
   exception at two adjacent windows while one subtraction exception
   spreads across the whole exponent range. (Subtraction's exception
   DENSITY was not measured here; the width split is the finding.)
   (Settled since, by explore_dual_measure.py: these densities are
   COUNTING measure on operand-window pairs at fixed depth; their
   exact closed forms are the period law and the pair limit
   2(1 - b^-j)/b^c — the limit ratio is exactly b, the 1.79-2.09
   wobble is finite precision plus the saturated c=1 cell — and the
   log-uniform re-read multiplies the limit by (b-1)^2/(b ln^2 b).)
F6 THE RADICAL LAW (rule; the frozen P6 REFUTED and replaced): the
   run refuted the conjectured exact-local class {s*b^j*x} — 2*x at
   base 10 is exactly local at lookahead 1. The corrected law,
   derived in check_radical_law and swept at bases 2, 6, 10:

       c*x is exactly window-local  IFF  rad(c) | rad(b)

   (exact c up to the sweep tops: base 2 -> {2,4,8,16},
   base 6 -> {2,3,4,6,8,9,12}, base 10 -> {2,4,5,8,10}). THE
   UNIFICATION, unpredicted: this is the SAME divisor condition as F2
   — the exactly computable scalings are the scalings by perfectly
   hidden primes. And the condition itself is not new at the OTHER
   end of the numeration: m | n is window-read from the LOW digits
   iff rad(m) | rad(b) (the settled numeration criterion,
   explore_numeration_windows.py). What this run adds is the
   condition's jurisdiction over the leading end, twice over —
   perfect hiding (F2) and exact locality (this law) — so one radical
   condition now governs three laws across the numeration's two ends.
   At the finite pole, locality (the polynomial criterion) and hiding
   (the coarsening facts) are separate statements. Addition (x+1) and
   powers (x^2, x^3) stay graded at every scanned lookahead,
   consistent with the class being scalings + constants only
   (conjecture beyond the swept families). (Settled since, by
   explore_dual_locality.py: the full exact class is LARGER — the
   numerator criterion floor((u/v)*x) local iff rad(u) | rad(b), the
   denominator free, plus non-arithmetic fiber-permuting maps; this
   law survives verbatim as the integer-scaling case.)
F7 THE TWO-ENDS LAW (rule): base b's trailing digits read exactly the
   finite places p | b (n mod p factors through the last digit — the
   prime case of the settled low-digit criterion, m | n window-read
   iff rad(m) | rad(b), explore_numeration_windows.py); its leading
   digits perfectly hide exactly the same places (F2). One
   numeration, two ends: the same primes exactly readable at one end,
   exactly invisible at the other.

The structural split the slate predicted stands in the prints: the
finite pole's locality is algebraic and binary (local = polynomial),
the archimedean pole's is measure-graded (geometric exception
densities, with a thin exact class carved by the radical condition).
(Settled since: the thinness is the ARITHMETIC core's — the full
exact class also carries fiber-permuting digit maps; the
classification is explore_dual_locality.py's.)

Run record: one mid-run refutation (P6, the assert fired with all
positive controls green; corrected law derived by hand, then swept),
two pre-run feasibility range corrections; an audit round then
strengthened four checks (multiplication-exception adjacency asserted,
the zero/both-signs realization asserted as one fact, the trailing-
block converse added, scan wording descoped) — final run 132 checks,
~2 s wall clock, trivial memory.
"""

CHECKS = 0


def ok(cond, label):
    global CHECKS
    assert cond, "FAIL: " + label
    CHECKS += 1


def ndigits(a, b):
    """Number of base-b digits of a >= 1, minus 1 (the exponent e)."""
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


def fibers_at(b, t, e):
    """All positive-sign fibers at exponent e (deep: e+1 > t), as
    (mantissa, lo, hi) with the fiber = [lo, hi)."""
    j = max(0, e + 1 - t)
    out = []
    lo_m = b ** (t - 1) if e + 1 >= t else b**e
    hi_m = b**t if e + 1 >= t else b ** (e + 1)
    for m in range(lo_m, hi_m):
        out.append((m, m * b**j, (m + 1) * b**j))
    return out


# ---------------------------------------------------------------- CHECK 1
def check_fiber_lemma():
    print("CHECK 1 - the fiber lemma (P1)")
    for b, t in [(2, 2), (3, 2), (10, 2), (2, 4)]:
        E = 6 if b == 2 else 4
        groups = {}
        for n in range(1, b ** (E + 1)):
            groups.setdefault(window(n, b, t), []).append(n)
        for (s, e, m), ns in groups.items():
            L = b ** max(0, e + 1 - t)
            contig = ns == list(range(ns[0], ns[0] + len(ns)))
            assert contig and len(ns) == L, (b, t, e, m)
        print("  b=%2d t=%d: %5d windows, every fiber a contiguous "
              "interval of length b^max(0,e+1-t)" % (b, t, len(groups)))
    ok(True, "fiber lemma exhaustive")


# ---------------------------------------------------------------- CHECK 2
def fiber_bias(lo, hi, p):
    """Max over residue classes of |count/L - 1/p| on [lo, hi)."""
    L = hi - lo
    counts = [0] * p
    for n in range(lo, hi):
        counts[n % p] += 1
    return max(abs(c / L - 1 / p) for c in counts)


def check_dual_hiding():
    print("CHECK 2 - the dual hiding law (P2)")
    configs = {2: [(2, 6), (2, 8), (3, 9)],
               3: [(2, 4), (2, 5), (3, 6)],
               10: [(2, 3), (2, 4), (3, 5)]}
    saw_nonzero_control = False
    for b in (2, 3, 10):
        for p in (2, 3, 5, 7, 11, 13):
            biases = []
            for t, e in configs[b]:
                for m, lo, hi in fibers_at(b, t, e):
                    biases.append((fiber_bias(lo, hi, p), hi - lo))
            allzero = all(x == 0 for x, _ in biases)
            somenonzero = any(x > 0 for x, _ in biases)
            divides = b % p == 0
            ok(allzero == divides,
               "bias zero on all deep fibers iff p|b (b=%d p=%d)" % (b, p))
            if not divides:
                ok(somenonzero, "leak exists for p=%d b=%d" % (p, b))
                saw_nonzero_control = True
                ok(all(x < 1 / L for x, L in biases),
                   "bias < 1/L for p=%d b=%d" % (p, b))
            print("  b=%2d p=%2d: %s" %
                  (b, p, "EXACTLY HIDDEN (p | b)" if divides else
                   "leaks, max bias %.4f < 1/L on every deep fiber"
                   % max(x for x, _ in biases)))
    ok(saw_nonzero_control, "positive control: the bias meter sees leaks")


# ---------------------------------------------------------------- CHECK 3
def check_residue_wall():
    print("CHECK 3 - the residue wall + the shallow leak (P3)")
    for b, t, e, p in [(2, 2, 5, 3), (10, 2, 3, 7), (3, 2, 4, 5)]:
        for m, lo, hi in fibers_at(b, t, e):
            L = hi - lo
            if L >= 2:
                ok_res = len({n % p for n in range(lo, hi)}) > 1
                assert ok_res, "residue map constant on a fiber"
            if L > p:
                vals = {n % p == 0 for n in range(lo, hi)}
                assert vals == {True, False}, "predicate constant, L > p"
        ok(True, "wall at b=%d t=%d e=%d p=%d" % (b, t, e, p))
    # the shallow leak: a fiber below the prime's scale missing all
    # multiples decides the predicate
    m, lo, hi = fibers_at(2, 2, 2)[0]  # fiber [4, 6), length 2
    assert all(n % 7 != 0 for n in range(lo, hi))
    ok(True, "shallow leak: [%d,%d) decides [7 | n] = False" % (lo, hi))
    print("  deep fibers decide no residue; the shallow leak prints above")


# ---------------------------------------------------------------- CHECK 4
def check_exponent_split():
    print("CHECK 4 - the exponent-determinacy split + equality wall (P4)")
    for b in (2, 10):
        N = 64 if b == 2 else 300
        deltas = set()
        for a in range(1, N):
            for c in range(1, N):
                deltas.add(ndigits(a * c, b) - ndigits(a, b) - ndigits(c, b))
        ok(deltas == {0, 1},
           "e(ab) - e(a) - e(b) in {0,1} over the scan (b=%d)" % b)
        print("  b=%2d: product exponent determined up to 1 by exponents "
              "alone (deltas %s)" % (b, sorted(deltas)))
    # subtraction: one deep fiber realizes every difference exponent,
    # both signs, and zero
    b, t, e = 2, 3, 8
    m, lo, hi = fibers_at(b, t, e)[0]
    L = hi - lo
    diffs = {a - c for a in range(lo, hi) for c in range(lo, hi)}
    exps = {ndigits(abs(d), b) for d in diffs if d != 0}
    ok(exps == set(range(0, ndigits(L - 1, b) + 1)),
       "difference exponents span the fiber's whole range")
    ok(0 in diffs and any(d > 0 for d in diffs) and
       any(d < 0 for d in diffs),
       "one window-pair realizes zero AND both signs: equality and "
       "comparison undetermined together")
    # at precision one short of exact the wall still stands
    m2, lo2, hi2 = fibers_at(b, e, e)[0]  # t = e: fiber length 2
    ok(hi2 - lo2 == 2, "one digit short of exact still leaves a pair")
    print("  one fiber (L=%d) realizes difference exponents %s, both "
          "signs, and zero: equality/comparison/zero-test all walled"
          % (L, sorted(exps)))


# ---------------------------------------------------------------- CHECK 5
def succ_window(w, b, t):
    """The next positive window after w in the size order."""
    s, e, m = w
    return (s, e, m + 1) if m + 1 < b**t else (s, e + 1, b ** (t - 1))


def mult_ambiguity(b, t, c, gap):
    """Over all operand-window pairs at precision t+c and exponent
    t+c+gap: exception count, max ambiguity width of W_t(a*b), and
    whether every width-2 exception is a pair of ADJACENT windows."""
    tp = t + c
    e = tp + gap
    fibs = fibers_at(b, tp, e)
    exceptions, maxwidth, total, adjacent = 0, 1, 0, True
    for ma, loa, hia in fibs:
        for mb, lob, hib in fibs:
            total += 1
            vals = {window(a * bb, b, t)
                    for a in range(loa, hia) for bb in range(lob, hib)}
            if len(vals) > 1:
                exceptions += 1
                maxwidth = max(maxwidth, len(vals))
                if len(vals) == 2:
                    w1, w2 = sorted(vals, key=lambda w: (w[1], w[2]))
                    adjacent = adjacent and succ_window(w1, b, t) == w2
    return exceptions, total, maxwidth, adjacent


def sub_ambiguity(b, t, c, gap):
    """Max ambiguity width of W_t(a-b) over same-exponent operand-window
    pairs at precision t+c, exponent t+c+gap (zero excluded from the
    width count; its reachability is CHECK 4's)."""
    tp = t + c
    e = tp + gap
    fibs = fibers_at(b, tp, e)
    maxwidth = 1
    for ma, loa, hia in fibs:
        for mb, lob, hib in fibs:
            vals = {window(a - bb, b, t)
                    for a in range(loa, hia) for bb in range(lob, hib)
                    if a != bb}
            maxwidth = max(maxwidth, len(vals))
    return maxwidth


def check_graded_locality():
    print("CHECK 5 - graded locality: density vs ambiguity width (P5)")
    b, t, gap = 2, 2, 3
    prev = None
    print("  multiplication, output precision t=%d, fiber depth %d:" %
          (t, gap + 1))
    for c in range(1, 6):
        exc, total, width, adjacent = mult_ambiguity(b, t, c, gap)
        frac = exc / total
        ok(exc > 0, "mult exceptions exist at lookahead c=%d" % c)
        ok(width <= 2, "mult ambiguity confined to 2 windows at c=%d" % c)
        ok(adjacent, "every mult exception straddles ONE boundary "
           "(adjacent windows) at c=%d" % c)
        ratio = ("ratio %.2f" % (prev / frac)) if prev and frac else ""
        print("    c=%d: %5d/%5d exceptional (%.4f) %s, max width %d"
              % (c, exc, total, frac, ratio, width))
        prev = frac
    widths = []
    for gap2 in (2, 4, 6):
        w = sub_ambiguity(b, t, 1, gap2)
        widths.append(w)
        print("    subtraction, fiber depth %d: max ambiguity width %d"
              % (gap2 + 1, w))
    ok(widths == sorted(widths) and widths[-1] > widths[0],
       "subtraction ambiguity width grows with depth")
    ok(widths[-1] > 2, "subtraction escapes the 2-window confinement")


# ---------------------------------------------------------------- CHECK 6
def exact_local(f, b, t, cmax, gap):
    """Least lookahead c <= cmax at which f reads window-to-window with
    zero exceptions on all scanned deep fibers, or None."""
    for c in range(0, cmax + 1):
        tp = t + c
        e = tp + gap
        clean = True
        for m, lo, hi in fibers_at(b, tp, e):
            vals = {window(f(n), b, t) for n in range(lo, hi) if f(n) != 0}
            if len(vals) > 1:
                clean = False
                break
        if clean:
            return c
    return None


def check_exact_local_class():
    print("CHECK 6 - the exact-local class (P6) + positive controls")
    cases = [
        (2, "b*x", lambda n: 2 * n, True),
        (2, "b^2*x", lambda n: 4 * n, True),
        (2, "-x", lambda n: -n, True),
        (2, "3*x", lambda n: 3 * n, False),
        (2, "x+1", lambda n: n + 1, False),
        (2, "x^2", lambda n: n * n, False),
        (2, "x^3", lambda n: n ** 3, False),
        (10, "b*x", lambda n: 10 * n, True),
        (10, "2*x", lambda n: 2 * n, True),
        (10, "x+1", lambda n: n + 1, False),
    ]
    for b, name, f, expect_exact in cases:
        cmax = 6 if b == 2 else 2
        gap = 2 if b == 2 else 1
        c = exact_local(f, b, 2, cmax, gap)
        ok((c is not None) == expect_exact,
           "%s at base %d expected %s" %
           (name, b, "exact" if expect_exact else "graded"))
        print("  base %2d  %-6s: %s" %
              (b, name, ("exactly local at lookahead %d" % c)
               if c is not None else
               "graded (exceptions at every c <= %d)" % cmax))
    print("  NOTE: the frozen P6 class was refuted mid-run (2*x at base "
          "10 is exact); the corrected law is tested next")


# ---------------------------------------------------------------- CHECK 6b
def rad_divides(c, b):
    """rad(c) | rad(b): every prime factor of c divides b."""
    x = c
    for p in range(2, x + 1):
        while x % p == 0:
            if b % p != 0:
                return False
            x //= p
    return True


def check_radical_law():
    """The corrected exact-local law, derived after P6's refutation:
    c*x is exactly window-local iff rad(c) | rad(b) — the SAME divisor
    condition as the dual hiding law. Derivation: on a fiber scaled to
    [cm, cm+c), output boundaries are the multiples of B = b^lookahead;
    cm mod B ranges over multiples of gcd(c, B), and a straddle exists
    at lookahead j iff gcd(c, b^j) < c; one exists at EVERY lookahead
    iff c divides no power of b, i.e. iff rad(c) does not divide
    rad(b)."""
    print("CHECK 6b - the radical law: exact-local scalings = the "
          "hidden primes' scalings")
    for b in (2, 6, 10):
        # sweep range and cmax matched so that every b-smooth c in
        # range has its minimal lookahead (least j with c | b^j) in reach
        cmax = 6 if b == 2 else 3
        gap = 2 if b == 2 else 0
        top = 21 if b == 2 else 13
        exact_cs, graded_cs = [], []
        for c in range(2, top):
            got = exact_local(lambda n: c * n, b, 2, cmax, gap)
            ok((got is not None) == rad_divides(c, b),
               "c*x exact iff rad(c)|rad(b) (b=%d c=%d)" % (b, c))
            (exact_cs if got is not None else graded_cs).append(c)
        print("  base %2d: exact c = %s" % (b, exact_cs))
    print("  one divisor condition governs hiding (P2) and locality: "
          "the exactly computable scalings are the perfectly hidden ones")


# ---------------------------------------------------------------- CHECK 7
def check_two_ends():
    print("CHECK 7 - the two-ends law (P7)")
    for b, p in [(10, 2), (10, 5), (2, 2), (6, 3)]:
        ok(all((n % b) % p == n % p for n in range(1, 5000)),
           "trailing digit reads n mod %d at base %d" % (p, b))
    # the converse: for p not dividing b, no trailing block reads the
    # residue — n and n+b share every trailing digit yet always differ
    # mod p
    for b, p in [(10, 3), (2, 5), (6, 7)]:
        ok(all(n % p != (n + b) % p for n in range(1, 5000)),
           "no trailing block reads mod %d at base %d" % (p, b))
    print("  trailing digits read exactly the places p | b; CHECK 2 "
          "showed leading digits perfectly hide exactly those places")


if __name__ == "__main__":
    check_fiber_lemma()
    check_dual_hiding()
    check_residue_wall()
    check_exponent_split()
    check_graded_locality()
    check_exact_local_class()
    check_radical_law()
    check_two_ends()
    print("ALL CHECKS PASSED (%d)" % CHECKS)
