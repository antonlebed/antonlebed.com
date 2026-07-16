"""The dual locality criterion: which functions can be read
window-to-window at the archimedean pole.

THE QUESTION
------------
The dual pole (explore_dual_pole.py) reads the integers only through
the size window W_{b,t}(n) = (sign, exponent, t leading base-b digits);
its fibers are integer intervals, and a function f is EXACTLY
WINDOW-LOCAL if for some fixed lookahead c, every output window of f at
precision t is determined by the operand's window at precision t + c —
zero exceptions on every deep fiber, at every t. The sibling run found
the scalings c*x exactly local iff rad(c) | rad(b) (the radical law)
and conjectured the full exact class to be these scalings plus
constants. This experiment settles the classification: what IS the
exact-local class, and what theorem carves it?

In native floating-point vocabulary, exactly window-local = correctly
truncatable from bounded extra precision: the bounded case of the
Table Maker's Dilemma, and the non-redundant MSB-first (online
arithmetic) computability question. The classification below is the
integer-truncation answer.

THE DESIGN
----------
The paper derivation preceded the engine; each prediction is marked
with its pre-run status (derived on paper / expected). The method is
the BOUNDARY-PREIMAGE argument: for monotone f, the image of a fiber
straddles a window boundary M*b^J iff the crossing point
n*(M) = min{n : f(n) >= M*b^J} lies strictly inside the fiber; fibers
are exactly the base-b grid intervals, so

    f is exception-free at a scale  IFF  every crossing point in
    range is grid-aligned at that scale.

Two consecutive crossings differ by floor(x) or ceil(x) of the real
step x between preimages; when x is not an integer BOTH values occur
within any boundary run of one full period of the step's fractional
part, they differ by 1, and two values differing by 1 cannot both be
multiples of b^j >= 2 — so if every crossing in such a run were
grid-aligned, every step in it would be, a contradiction: a
misaligned crossing (an exception) exists inside every period-length
run of boundaries: THE CONSECUTIVE-CROSSINGS LEMMA. Witnesses are
therefore CONSTRUCTED at every lookahead, never swept blindly (a sweep
misses density-b^{-c} exceptions; the probe run that preceded this
engine produced three such false "exact" verdicts before the
witnesses were targeted).

Predictions, fixed before the engine ran:

D1 [derived, rule] THE NUMERATOR CRITERION: f(n) = floor((u/v) n),
    gcd(u, v) = 1, is exactly window-local at base b IFF
    rad(u) | rad(b). The denominator is FREE: floor(n/v) is exactly
    local for EVERY v at every base — division is the leading end's
    free operation, multiplication its gated one. (Long division
    emits quotient digits MSB-first from bounded remainder state;
    multiplication's carries flow LSB-to-MSB, against the read.)
    Alignment half: rad(u) | rad(b) makes every crossing
    n* = ceil(v*M*b^J / u) an exact multiple of b^j once the
    lookahead clears u's depth in b AND v's width (the extra
    log_b(v) also retires the shallow-output boundaries, whose
    preimages then sit in shallow operand fibers). Straddle half:
    otherwise the consecutive-crossings lemma yields a misaligned
    crossing at every scale. The sibling's radical law is the
    v = 1 case.
D2 [derived, rule] THE PHASE LAW: floor((n+s)/v) is exactly local
    iff s = 0 (0 <= s < v). In particular ceil(n/v) and
    round-to-nearest are GRADED while floor(n/v) is exact:
    ceil - floor = [v does not divide n], a residue read, and the
    residue wall (explore_dual_pole.py: no deep fiber decides a
    residue predicate) forbids it. Truncation is the unique local
    rounding phase.
D3 [derived, rule] THE SHIFT WALL: f(n) = n + a is graded for every
    a != 0 — the crossing M*b^J - a is misaligned at every depth
    j > v_b(a). With D1/D2: no nonzero additive structure survives.
D4 [derived construction at k=2; expected k=3] THE CURVATURE WALL:
    f(n) = n^k, k >= 2, is graded at every lookahead: near mantissa
    m = b^{s-c} + u0 (u0 ~ b^c/2, s = t+2c-1) the square's crossing
    point falls strictly inside a fiber, at every c and base; cubes
    the same by crossing-point search over the mantissa range.
D5 [derived, property] THE STRUCTURAL SPLIT: the full exact-local
    class is far larger than the arithmetic members — any map that
    permutes every fiber onto itself (base 2: XOR by an
    exponent-dependent mask below the top bit; base 10: a digit
    permutation applied below the top digit) is exactly local at
    lookahead 0 and is no scaling. At the finite pole's squarefree
    moduli — every tower rung — locality SATURATES into algebra
    (every channel-local map is already a polynomial, by per-channel
    interpolation; a squarefree-only equivalence — the locality
    criterion, explore_size_transform.py); at the dual pole
    locality and algebraicity SPLIT: the local class is the
    fiber-cellular (prefix-tree) maps, its arithmetic core the thin
    D1 scalings, and the gap is digit machinery foreign to the ring.
D6 [derived, rule] THE TWO-ENDS EXCHANGE: at the TRAILING end
    (residues mod b^t), multiplication by any c is free
    (c*n mod b^t is a function of n mod b^t) and division is gated:
    floor(n/v) mod b^t is a function of n mod b^{t+d} iff
    rad(v) | rad(b). At the LEADING end (this experiment),
    division is free and multiplication is gated by rad(u) | rad(b)
    (D1). One radical condition, two ends, sitting on OPPOSITE
    parts of u/v: each end freely reads the operation whose carry
    flow points away from it.
D7 [derived, rule] THE DEPTH THRESHOLD (composite hiding): on a
    fiber of length b^j the residue counts mod m are exactly equal
    iff m | b^j; so perfect hiding of m on every fiber at depth
    >= j holds iff rad(m) | rad(b) and j >= j_m with
    j_m = max_p ceil(v_p(m) / v_p(b)) — the prime case (j_m = 1,
    p | b) is the sibling's dual hiding law.

Kill criteria, named at the freeze: a rad(u)-violating scaling
verifying exact at the scanned scope kills D1 (and the boundary
method); a graded claim whose witness search fails at some lookahead
kills that wall; any exception for the fiber-permuting maps kills D5.
Positive controls: the sibling's verdicts (2x exact, 3x graded, x+1
graded at base 2) must reproduce, and the boundary-preimage verdicts
must agree with a small brute-force sweep wherever both run.

Engine: pure python, exact integers throughout; witnesses verified
by DEFINITION (two operands in one deep fiber whose f-values lie in
different windows), never by the generating bookkeeping; seconds.

THE FINDINGS
------------
Verdict: the classification is settled, and the conjectured class
("scalings by rad(c) | rad(b), plus constants") was too small TWICE —
on the arithmetic side it missed every denominator, and on the
structural side it missed a whole non-arithmetic stratum. 497 checks
green.

F1 THE NUMERATOR CRITERION (rule; the alignment argument + the
   consecutive-crossings lemma, swept at bases 2, 6, 10):
   floor((u/v) n), gcd(u, v) = 1, is exactly window-local iff
   rad(u) | rad(b) — and the DENOMINATOR IS FREE: floor(n/v) is
   exactly local for every v at every base. 19 + 23 + 23 smooth-
   numerator scalings had every scanned window boundary's crossing
   grid-aligned (each scan asserted to have met deep crossings);
   6 + 3 + 5 rough-numerator scalings received a
   constructed exception at every lookahead (c <= 6 at base 2, <= 4
   at 6 and 10); brute sweeps at small scales agree with the
   boundary-preimage verdicts (6 cases); the sibling's verdicts (2x
   exact, 3x graded, x+1 graded) reproduce. Division is the leading
   end's free operation, multiplication its gated one.
F2 THE PHASE LAW (rule): floor((n+s)/v) is exactly local iff s = 0 —
   every phase s = 1..v-1 graded at every scanned lookahead
   (v = 3, 5 at base 2; v = 3, 7 at base 10), so ceil(n/v) and
   round-to-nearest are GRADED while floor is exact. Truncation is
   the unique local rounding phase: ceil - floor = [v does not
   divide n] is a residue read, and the residue wall forbids it.
   (Digit-set scope, settled by explore_dual_lipschitz.py: this
   uniqueness is the STANDARD-window case of the phase-shape law —
   each digit set's free phase is its own cell shape, and on the
   balanced windows the free phase is round-to-nearest, floor
   walled.)
F3 THE SHIFT WALL (rule): n + a is graded for every a != 0 (shifts
   1, 2, 3, 4, 12, 16 at base 2 and 1, 2, 7, 100 at base 10, every
   lookahead; the witness crossing M*b^J - a is misaligned at every
   depth j > v_b(a)). No nonzero additive structure survives.
F4 THE CURVATURE WALL (rule): n^2 and n^3 are graded at every
   lookahead at bases 2, 6, 10 (crossing points = integer roots of
   window boundaries; witness found at every scanned c); the derived
   mantissa family m = b^(s-c) + u0 verifies at 4/4 spot checks.
F5 THE STRUCTURAL SPLIT (property + witnesses): the exact-local
   class strictly exceeds its arithmetic members — the XOR
   window-mask (base 2) and the below-the-top digit permutation
   (base 10) are exactly local at lookahead 0 and are NON-MONOTONE —
   every member of the F1 scaling family is monotone, so they sit
   outside the whole arithmetic core, not merely off the exact
   scalings.
   The finite pole's locality saturates into algebra on squarefree
   moduli (channel-local = polynomial, every tower rung); the dual
   pole's does not: local = fiber-cellular (prefix-tree) maps, whose
   arithmetic members across every family swept here (scalings,
   phases, shifts, powers) are exactly the thin F1 family
   (conjectured beyond the swept families). Locality and
   algebraicity split at this pole.
F6 THE TWO-ENDS EXCHANGE (rule): trailing end — multiplication by
   any c free, division gated (floor(n/v) mod b^t reads from t + d
   trailing digits for v = 2, 5, 8 at base 10, 4 at base 2, 9 at
   base 6; collision witnesses at every block length k <= 4 for
   v = 3, 7 at base 10, 3 at base 2, 7 at base 6). Leading end (F1)
   — division free, multiplication gated. One radical condition at
   both ends, sitting on OPPOSITE parts of u/v: each end freely
   reads the operation whose carry flow points away from it.
F7 THE DEPTH THRESHOLD (rule, elementary): residue counts mod m on a
   depth-j fiber are exactly equal iff m | b^j, so perfect hiding of
   a composite modulus needs rad(m) | rad(b) AND depth
   j >= j_m = max_p ceil(v_p(m)/v_p(b)) (verified for m up to 25 at
   bases 2, 6, 10; the prime case j_m = 1 is the dual hiding law).

Run record: the pre-engine probe produced three false "exact"
verdicts from blind sweeps (exception density ~b^-c outruns sampled
fibers) before the witnesses were targeted — the method note in the
design is that lesson; one witness-pair correction after the first
run (the XOR non-scaling pair straddled exponent classes, whose masks
shift consistently; its own assert caught it — replaced with
same-class neighbors); an audit round then scoped the alignment
sweep's wording to its scanned range, added the deep-crossing
counter asserts, corrected the phase law's mechanism cite (the
residue wall, not the hiding law) and the finite-pole mirror's
squarefree scope — final run 497 checks, ~1 s wall clock, trivial
memory.
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


def fiber_of(n, b, tp):
    """(lo, hi, j) of n's fiber at precision tp; deep iff j >= 1."""
    e = ndigits(n, b)
    j = max(0, e + 1 - tp)
    lo = (n // b**j) * b**j
    return lo, lo + b**j, j


def rad_divides(u, b):
    """rad(u) | rad(b): every prime factor of u divides b."""
    x = u
    for p in range(2, x + 1):
        while x % p == 0:
            if b % p != 0:
                return False
            x //= p
    return True


def pair_witness(f, n_star, b, t, tp):
    """True iff n_star sits strictly inside a deep fiber at precision
    tp and f jumps windows between n_star - 1 and n_star — a
    definition-level exception witness."""
    if n_star < 2:
        return False
    lo, hi, j = fiber_of(n_star, b, tp)
    if j < 1 or n_star == lo:
        return False
    a, c = f(n_star - 1), f(n_star)
    if a == 0 or c == 0:
        return False
    return window(a, b, t) != window(c, b, t)


def iroot(x, k):
    """Integer floor k-th root."""
    if x < 0:
        raise ValueError
    r = int(round(x ** (1.0 / k)))
    while r**k > x:
        r -= 1
    while (r + 1) ** k <= x:
        r += 1
    return r


def brute_exact(f, b, t, c, depths=(1, 2)):
    """Full-sweep exception count at output precision t, lookahead c,
    over every fiber at the given depths (small scales only)."""
    tp = t + c
    exc = 0
    for j in depths:
        e = tp + j - 1
        for m in range(b ** (tp - 1), b**tp):
            lo, hi = m * b**j, (m + 1) * b**j
            vals = {window(f(n), b, t) for n in range(lo, hi) if f(n) != 0}
            if len(vals) > 1:
                exc += 1
    return exc


# ---------------------------------------------------------------- CHECK 1
def scaling_crossings_aligned(u, v, b, t, c, Jspan):
    """The exact half of D1 by boundary-preimage exhaustion: for every
    window boundary M*b^J in the scanned range, the crossing of
    floor(u*n/v) is grid-aligned (or shallow) at operand precision
    t + c. Also returns the count of DEEP crossings seen, so a scan
    that only met shallow fibers cannot pass silently."""
    tp = t + c
    deep = 0
    for J in Jspan:
        for M in range(b ** (t - 1), b**t):
            target = v * M * b**J
            n_star = -((-target) // u)  # ceil
            lo, hi, j = fiber_of(n_star, b, tp)
            if j >= 1:
                deep += 1
                if n_star != lo:
                    return False, (J, M, n_star), deep
    return True, None, deep


def check_numerator_exact():
    print("CHECK 1 - the numerator criterion, exact half (D1)")
    grids = {2: ([1, 2, 4, 8], [1, 3, 5, 7, 9]),
             6: ([1, 2, 3, 4, 6, 9], [1, 5, 7, 11]),
             10: ([1, 2, 4, 5, 8, 10], [1, 3, 7, 9])}
    from math import gcd
    for b, (us, vs) in grids.items():
        n_pairs = 0
        for u in us:
            for v in vs:
                if gcd(u, v) != 1 or (u == 1 and v == 1):
                    continue
                # lookahead clearing u's depth in b plus v's width
                du = 0
                x, p = u, 2
                while x > 1:
                    if x % p == 0:
                        k = 0
                        while x % p == 0:
                            x //= p
                            k += 1
                        vb = 0
                        bb = b
                        while bb % p == 0:
                            bb //= p
                            vb += 1
                        du = max(du, -(-k // vb))
                    p += 1
                cstar = du + ndigits(max(v, 1), b) + 2
                lo_J = cstar + 2 + ndigits(u, b)
                good, bad, deep = scaling_crossings_aligned(
                    u, v, b, 2, cstar, range(lo_J, lo_J + 4))
                ok(good, "crossings aligned for %d*n/%d at base %d "
                   "(bad=%s)" % (u, v, b, bad))
                ok(deep > 0, "scan met deep crossings for %d*n/%d at "
                   "base %d" % (u, v, b))
                n_pairs += 1
        print("  base %2d: %d smooth-numerator scalings, every scanned "
              "window boundary's crossing grid-aligned" % (b, n_pairs))
    # brute agreement control: the method's verdicts match full sweeps
    agree = [
        (2, lambda n: 2 * n, True), (2, lambda n: 3 * n, False),
        (2, lambda n: n // 3, True), (2, lambda n: 2 * n // 3, True),
        (2, lambda n: 3 * n // 5, False), (10, lambda n: n // 7, True),
    ]
    for b, f, expect in agree:
        cmax = 6 if b == 2 else 3
        got = None
        for c in range(0, cmax + 1):
            if brute_exact(f, b, 2, c) == 0:
                got = c
                break
        ok((got is not None) == expect, "brute sweep agrees (b=%d)" % b)
    print("  brute-force sweeps at small scales agree with the "
          "boundary-preimage verdicts (6 cases)")


# ---------------------------------------------------------------- CHECK 2
def graded_witness_scaling(u, v, b, t, c, s=0):
    """A definition-level exception for floor((u*n + s*?)/v)-style maps:
    scan window boundaries, return a witnessing crossing or None.
    Here f = floor(u*n/v) shifted by phase -s in the crossing."""
    tp = t + c

    def f(n):
        return (u * n + s) // v

    for J in range(c + 2, c + 8):
        for M in range(b ** (t - 1), b**t):
            target = v * M * b**J - s
            n_star = -((-target) // u)
            if pair_witness(f, n_star, b, t, tp):
                return n_star
    return None


def check_numerator_graded():
    print("CHECK 2 - the numerator criterion, graded half (D1) + "
          "sibling controls")
    cases = {2: [(3, 1), (5, 1), (7, 1), (3, 5), (5, 3), (6, 5)],
             6: [(5, 1), (7, 1), (5, 7)],
             10: [(3, 1), (7, 1), (3, 7), (6, 1), (7, 4)]}
    for b, pairs in cases.items():
        cmax = 6 if b == 2 else 4
        for u, v in pairs:
            assert not rad_divides(u, b)
            for c in range(0, cmax + 1):
                w = graded_witness_scaling(u, v, b, 2, c)
                ok(w is not None,
                   "witness for %d*n/%d at base %d, c=%d" % (u, v, b, c))
        print("  base %2d: %d rough-numerator scalings, constructed "
              "exception at every lookahead c <= %d" % (b, len(pairs), cmax))
    # sibling positive controls: 2x exact, 3x graded, x+1 graded (base 2)
    ok(brute_exact(lambda n: 2 * n, 2, 2, 1) == 0, "2x exact (control)")
    ok(all(graded_witness_scaling(3, 1, 2, 2, c) for c in range(5)),
       "3x graded (control)")
    ok(all(graded_witness_shift(1, 2, 2, c) for c in range(5)),
       "x+1 graded (control)")
    print("  sibling verdicts reproduce: 2x exact, 3x graded, x+1 graded")


# ---------------------------------------------------------------- CHECK 3
def check_phase_law():
    print("CHECK 3 - the phase law: truncation is the unique local "
          "phase (D2)")
    for b, v in [(2, 3), (2, 5), (10, 3), (10, 7)]:
        cmax = 5 if b == 2 else 3
        # floor is exact: crossings of floor(n/v) are v*M*b^J,
        # grid-aligned at every J >= j — checked in CHECK 1's grid
        # (u = 1 rows); here the other phases die
        for s in range(1, v):
            for c in range(0, cmax + 1):
                w = graded_witness_scaling(1, v, b, 2, c, s=s)
                ok(w is not None, "floor((n+%d)/%d) graded at base %d "
                   "c=%d" % (s, v, b, c))
        print("  base %2d, v=%d: every phase s=1..%d graded at every "
              "c <= %d; s=0 exact" % (b, v, v - 1, cmax))
    # named corollaries: ceil and round-to-nearest are graded
    for b, v in [(2, 3), (10, 3)]:
        wc = graded_witness_scaling(1, v, b, 2, 2, s=v - 1)
        wr = graded_witness_scaling(1, v, b, 2, 2, s=v // 2)
        ok(wc is not None and wr is not None,
           "ceil and round graded at base %d" % b)
    print("  ceil(n/v) and round-to-nearest graded; the exact phase is "
          "truncation alone")


# ---------------------------------------------------------------- CHECK 4
def graded_witness_shift(a, b, t, c):
    """Exception witness for f = n + a at lookahead c: the crossing
    M*b^J - a, taken deep enough that b^j does not divide a."""
    tp = t + c

    def f(n):
        return n + a

    va = 0
    x = a
    while x % b == 0:
        x //= b
        va += 1
    for J in range(max(c + 2, va + c + 3), va + c + 9):
        for M in range(b ** (t - 1), b**t):
            n_star = M * b**J - a
            if pair_witness(f, n_star, b, t, tp):
                return n_star
    return None


def check_shift_wall():
    print("CHECK 4 - the shift wall: n + a graded for every a != 0 (D3)")
    for b in (2, 10):
        cmax = 6 if b == 2 else 4
        shifts = [1, 2, 3, 4, 12, 16] if b == 2 else [1, 2, 7, 100]
        for a in shifts:
            for c in range(0, cmax + 1):
                ok(graded_witness_shift(a, b, 2, c) is not None,
                   "n+%d graded at base %d c=%d" % (a, b, c))
        print("  base %2d: shifts %s all graded at every c <= %d"
              % (b, shifts, cmax))


# ---------------------------------------------------------------- CHECK 5
def graded_witness_power(k, b, t, c):
    """Exception witness for f = n^k: crossing points are integer
    k-th roots of window boundaries; scan boundaries."""
    tp = t + c

    def f(n):
        return n**k

    for J in range(k * (c + 2), k * (c + 2) + 4 * k + 8):
        for M in range(b ** (t - 1), b**t):
            n_star = iroot(M * b**J - 1, k) + 1  # ceil root
            if pair_witness(f, n_star, b, t, tp):
                return n_star
    return None


def check_curvature_wall():
    print("CHECK 5 - the curvature wall: n^k graded, k = 2, 3 (D4)")
    for b in (2, 6, 10):
        cmax = 5 if b == 2 else 3
        for k in (2, 3):
            for c in range(0, cmax + 1):
                ok(graded_witness_power(k, b, 2, c) is not None,
                   "n^%d graded at base %d c=%d" % (k, b, c))
        print("  base %2d: squares and cubes have a constructed "
              "exception at every c <= %d" % (b, cmax))
    # the derived square witness family: mantissa m = b^{s-c} + u0
    # (u0 ~ b^c/2, s = t + 2c - 1) puts the crossing inside a fiber
    hits = 0
    for b, c in [(2, 2), (2, 4), (10, 2), (6, 2)]:
        t = c + 3
        s = t + 2 * c - 1
        u0 = (b**c - 2) // 2 if b % 2 == 0 else (b**c - 1) // 2
        m0 = b ** (t + c - 1) + u0
        # the crossing just above m0^2's cell start, at growing depth
        found = False
        for j in range(1, 14):
            n0 = m0 * b**j
            q = (m0 * m0) // b**s + 1
            n_star = iroot(q * b ** (s + 2 * j) - 1, 2) + 1
            if (n0 < n_star < (m0 + 1) * b**j
                    and pair_witness(lambda n: n * n, n_star, b, t, t + c)):
                found = True
                break
        hits += found
    ok(hits == 4, "the derived m = b^(s-c)+u0 family witnesses at all "
       "4 spot checks")
    print("  the derived witness family (m = b^(s-c) + u0) verifies at "
          "4/4 spot checks")


# ---------------------------------------------------------------- CHECK 6
def check_structural_split():
    print("CHECK 6 - the structural split: exact-local is bigger than "
          "arithmetic (D5)")

    def f_xor(n):
        e = ndigits(n, 2)
        mask = (0b1011010 << max(0, e - 8)) & ((1 << e) - 1)
        return n ^ mask

    exc = sum(brute_exact(f_xor, 2, t, 0, depths=(1, 2, 3))
              for t in (1, 2, 3, 4))
    ok(exc == 0, "XOR window-mask exact at lookahead 0")

    def f_perm(n):
        e = ndigits(n, 10)
        digits = []
        x = n
        for i in range(e):
            digits.append((3 * (x % 10) + 1) % 10)
            x //= 10
        out = x  # the untouched top digit
        for d in reversed(digits):
            out = 10 * out + d
        return out

    exc = sum(brute_exact(f_perm, 10, t, 0, depths=(1, 2))
              for t in (1, 2))
    ok(exc == 0, "digit permutation exact at lookahead 0")
    # neither is in the scaling family: every floor((u/v)n) is
    # monotone (as is every negative scaling, decreasingly), while
    # both maps rise AND fall
    ok(f_xor(256) < f_xor(257) and f_xor(257) > f_xor(258),
       "XOR map is non-monotone: outside the whole scaling family")
    ok(f_perm(100) < f_perm(101) and f_perm(102) > f_perm(103),
       "perm map is non-monotone: outside the whole scaling family")
    print("  fiber-permuting maps (XOR mask base 2, digit permutation "
          "base 10) are exactly local at c=0 and non-monotone (no "
          "truncated scaling is):")
    print("  locality does not saturate into algebra here -- the finite "
          "pole's channel-local = polynomial (squarefree) has no mirror")


# ---------------------------------------------------------------- CHECK 7
def check_two_ends_exchange():
    print("CHECK 7 - the two-ends exchange (D6)")
    # trailing end, multiplication free: c*n mod b^t = fn of n mod b^t
    for b, t in [(2, 3), (10, 2)]:
        for cc in (3, 7, 11):
            ok(all((cc * n) % b**t == (cc * (n % b**t)) % b**t
                   for n in range(1, 2000)),
               "trailing mult free (b=%d c=%d)" % (b, cc))
    # trailing end, division gated: floor(n/v) mod b^t readable iff
    # rad(v) | rad(b)
    for b, v, d in [(10, 2, 1), (10, 5, 1), (10, 8, 3), (2, 4, 2),
                    (6, 9, 2)]:
        t = 2
        seen = {}
        okv = True
        for n in range(1, 40000):
            key = n % b ** (t + d)
            val = (n // v) % b**t
            if seen.setdefault(key, val) != val:
                okv = False
                break
        ok(okv, "floor(n/%d) mod %d^%d reads from %d trailing digits"
           % (v, b, t, t + d))
    for b, v in [(10, 3), (10, 7), (2, 3), (6, 7)]:
        for k in range(1, 5):
            seenk = {}
            coll = None
            for n in range(1, 4 * v * b**k):
                key = n % b**k
                val = (n // v) % b
                if seenk.setdefault(key, val) != val:
                    coll = n
                    break
            ok(coll is not None,
               "floor(n/%d) unreadable from %d trailing digits (b=%d)"
               % (v, k, b))
    print("  trailing: multiplication free, division gated by "
          "rad(v) | rad(b); leading (CHECKs 1-2): division free, "
          "multiplication gated by rad(u) | rad(b) -- the ends exchange")


# ---------------------------------------------------------------- CHECK 8
def check_depth_threshold():
    print("CHECK 8 - the composite hiding depth threshold (D7)")
    for b, ms in [(2, [4, 8, 12]), (10, [4, 20, 8, 25, 3]),
                  (6, [4, 9, 8, 5])]:
        for m in ms:
            # j_m from the formula, when rad(m) | rad(b)
            smooth = rad_divides(m, b)
            jm = None
            if smooth:
                jm = 0
                x, p = m, 2
                while x > 1:
                    if x % p == 0:
                        k = 0
                        while x % p == 0:
                            x //= p
                            k += 1
                        vb = 0
                        bb = b
                        while bb % p == 0:
                            bb //= p
                            vb += 1
                        jm = max(jm, -(-k // vb))
                    p += 1
            for j in range(1, 5):
                L = b**j
                # counts on a few fibers at depth j
                equal_all = True
                for A in (L, 3 * L, 7 * L, (b**2 + 1) * L):
                    counts = [0] * m
                    for n in range(A, A + L):
                        counts[n % m] += 1
                    if len(set(counts)) != 1:
                        equal_all = False
                        break
                ok(equal_all == (L % m == 0),
                   "equal counts iff m | b^j (b=%d m=%d j=%d)" % (b, m, j))
                if smooth:
                    ok((L % m == 0) == (j >= jm),
                       "threshold j_m = %d (b=%d m=%d j=%d)" % (jm, b, m, j))
        print("  base %2d: equal residue counts on a depth-j fiber iff "
              "m | b^j; threshold j_m = max_p ceil(v_p(m)/v_p(b))" % b)


if __name__ == "__main__":
    check_numerator_exact()
    check_numerator_graded()
    check_phase_law()
    check_shift_wall()
    check_curvature_wall()
    check_structural_split()
    check_two_ends_exchange()
    check_depth_threshold()
    print("ALL CHECKS PASSED (%d)" % CHECKS)
