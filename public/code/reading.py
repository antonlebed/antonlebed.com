"""
reading.py -- which maps a digit-by-digit reader computes at bounded
lookahead, what the numeration's tiles charge for it, and which place
pays for a wall.

QUESTION. A NUMERATION writes the points of a complete metric space X
as digit streams: its depth-t TILES C_t are the sets of points sharing
a t-digit prefix, nested, with mesh delta_t -> 0 and Lebesgue number
l_t (every set of diameter < l_t lies in one depth-t tile). A reader
of f at lookahead c sees an input tile at depth t + c and must commit
an output tile at depth t holding the image, the commitments nesting.
Which f can be read at bounded c, what does the tiles' shape charge,
and for the integer maps n -> mn and n -> floor(n/m), what decides?
The integer and polynomial numerations are the specimens: base b
(trailing digits of n, completing to the b-adic integers), the
primorial chain (n mod p_1 p_2 ... p_t, completing to the product of
the F_p), leading base b (the reals by their high digits), Zeckendorf
and the d-bonacci numerations (trailing, completing to an odometer or
a torus translation), and over F_q[x] both the trailing x-adic
numeration and the leading one at the place at infinity.

THE ARGUMENT (written before this script).
  (1) THE READING LEMMA. If f is L-Lipschitz, a depth-(t + c) tile
      has image of diameter <= L delta_{t+c}, which lies in one
      depth-t tile once L delta_{t+c} < l_t. Where tiles nest and the
      choice is made consistently, this per-level fit is a reader.
      Three tile shapes give three regimes: BALLS of an ultrametric
      (l_t = delta_t, the fit costs log_b L digits and nothing more);
      a PARTITION of a connected space (l_t = 0, the lemma is silent,
      readability is a per-map alignment question); an OVERLAPPING
      cover with l_t = rho delta_t (the fit costs a margin log_b(1/rho)
      on top).
  (2) THE BALL REGIME IS EVERY NON-ARCHIMEDEAN PLACE'S. In an
      ultrametric two points at distance < r lie in the same ball of
      radius r, so a numeration whose depth-t tiles are the balls of
      radius delta_t has l_t = delta_t. Every completion of Q or F_q(x)
      at a place other than the archimedean one is ultrametric, and its
      digit numeration's tiles are its balls. So a WALL -- an input
      point where a map Lipschitz in the place's own metric commits no
      output at any bounded lookahead -- needs a partition of a
      connected space, and among the completions of Q and F_q(x) only
      R is connected. The leading base-b numeration
      of R is the one numeration here with walls; the p-adic (char 0)
      and x-adic or 1/x-adic (char p) numerations have none. This is
      the question a clause priced at the archimedean place owes: at
      the carries and at a bundle's capacity the characteristic owned
      the price; here the PLACE does, since Q_p carries and still
      reads every scaling at bounded lookahead.
  (3) THE WALL CRITERION. At a partition cover of an interval with a
      rational vertex set B (the tile endpoints, which stay endpoints
      at every deeper level), take f continuous and strictly monotone
      and y irrational. If f(y) is not in B, f(y) lies interior to its
      tile at every depth and the image interval of a fine enough input
      tile fits: emission grows without bound. If f(y) is in B, every
      input tile around y has image straddling f(y), whose two sides
      agree only to the vertex's own depth: emission freezes at a
      constant. The permanent walls of f are f^-1(B) minus B.
  (4) THE LIPSCHITZ CRITERION. On a trailing numeration the agreement
      ultrametric is dist(y, z) = b^-(agreement depth), and "agreement
      to t + c forces image agreement to t" is dist(fy, fz) <= b^c
      dist(y, z).
      So f is readable at lookahead c iff it is b^c-Lipschitz, and a
      map on a dense subset extends to the completion with the same
      constant. Continuity is not enough: at a compact completion it
      buys a modulus s(t), and bounded lookahead needs s(t) <= t + c.
      Three classes: LIPSCHITZ, MIDDLE (continuous, lookahead growing
      with depth) and DISCONTINUOUS. The decimation D(n) = sum over
      j >= 0 of n_2j 2^j at base 2, n_j the digit of n at position j,
      needs input digits 0..2t - 2 for output digits 0..t - 1, so
      c_min(D, t) = t - 1: MIDDLE is inhabited.
  (5) THE DIVISION CRITERION ON A CHAIN. Let a trailing numeration's
      tiles be the classes n mod M_t for a divisor chain M_1 | M_2 |
      ... . Multiplication by m is 1-Lipschitz. floor(n/m) is readable
      at lookahead c at depth t iff m M_t divides M_{t+c}: if it does,
      n mod m is fixed by n mod M_{t+c}, and the quotients of inputs
      agreeing there differ by a multiple of M_{t+c}/m, which M_t
      divides; if not, some residue r < m has floor((r + M_{t+c})/m)
      - floor(r/m) not divisible by M_t, and the pair (r, r + M_{t+c})
      agrees at depth t + c and not after division. At base b this is
      m | b^c, bounded for every t iff rad(m) | rad(b). At the primorial
      chain m p_t# | p_{t+c}# holds iff m is squarefree with every prime
      in (p_t, p_{t+c}], so for each m >= 2 it fails at every depth from
      the index of m's least prime on: the primorial completion reads no floor
      division. Over F_q[x] the same algebra runs with polynomial
      division (the remainder has degree below deg m, so it is fixed
      by the residue mod m), and at base x the criterion is m = u x^j,
      u a nonzero constant.
  (6) NOT A TOPOLOGICAL RING (the comb). Take the d-bonacci numeration, q_k =
      q_(k-1) + ... + q_(k-d), q_j = 2^j for j < d, greedy digits.
      2 q_k = q_(k+1) + q_(k-d) walks a carry DOWN d places, so the
      step-(d + 1) comb T_K = q_d + q_(2d+1) + ... + q_K doubles to a
      step-d comb whose bottom cycles through d phases as K steps by
      d + 1. T_K and T_(K+d+1) agree to depth K + d + 1, and their
      doubles differ at a digit <= d - 2, at every K: x2 has no
      continuous extension, so the completion carries no continuous
      addition extending the integers'. d = 2 is Zeckendorf. The units
      read: n -> n + 1 at lookahead 1 at Zeckendorf.

HAND-ATTACK (on paper, before any engine code).
  - Necessity in (5) over Z: as r runs over 0..m - 1 the one-step
    difference floor((r + M)/m) - floor(r/m) takes the value
    floor(M/m) and, when m does not divide M, also floor(M/m) + 1. Two
    consecutive integers are never both divisible by N = M_t >= 2, so
    m | M is forced, and then the difference is M/m, divisible by N iff
    m N | M. Inputs agreeing at depth t + c differ by k M, a chain of k
    one-steps, so one-step pairs decide. The criterion is proved over Z.
  - Over F_q[x] the one-step argument does NOT transfer: division by m
    is F_q-linear, so the condition is that floor(kM/m) lies in (N)
    for EVERY polynomial k, and the pairs (n, n + kM) are not chains of
    +M steps. Sufficiency stands as written; necessity is not proved
    here, so the brute pair search over all polynomials below a degree
    bound is necessity's only evidence and the tier is a rule at that
    scope.
  - Half-open tiles: at leading base 10, y -> 2y maps vertices to
    vertices, and the image [2a, 2a + 2h) of a depth-(t + 1) tile has
    endpoints on the grid of step 2h, which contains the depth-t
    vertices; nothing lies strictly inside, so c = 1 suffices. y -> 3y
    fails at every c, since 3 does not divide 10^c.
  - P-W as first written listed sqrt(3) as emitting; 3 is a vertex, so
    it freezes. Corrected here, before the run.

PREDICTIONS (frozen before any engine code).
  P-L  At trailing base 10, n -> 7n reads at c = 0 and floor(n/4)
       needs c = 2 (4 | 10^2, 4 does not divide 10), at every depth
       scanned.
  P-B  (the new control) Every scaling reads at bounded lookahead at
       both non-archimedean arms: at the 3-adic numeration y -> 2y and
       y -> y/2 read at c = 0; at the 1/x-adic numeration of F_2((1/x))
       multiplication and division by u = x + 1 and u = x^2 + x + 1
       read at c = 0 after the degree shift, exhaustively over all
       inputs of the scanned length. At leading base 10 (R), y -> 3y
       needs lookahead >= k on the input prefix 0.33...3 (k threes)
       for every k scanned, while y -> 2y reads at c <= 1 everywhere
       scanned (the positive control on the wall detector).
  P-W  At leading base 10, y -> y^2 freezes emission at y = sqrt(0.2),
       sqrt(0.5), sqrt(2), sqrt(3) (images 0.2, 0.5, 2, 3 are
       vertices) and emits without bound at y = sqrt(1/3), sqrt(1/7)
       (images 1/3 and 1/7 are in no Z[1/10]).
  P-M  c_min(D, t) = t - 1 exactly at t = 1..10 at base 2.
  P-R  The chain criterion (5) agrees with a brute pair search at
       every (chain, m, t, c) scanned: bases 10 and 12, m = 2..12; the
       primorial chain, m = 2..30, t = 1..4; F_2[x] at bases x and
       x(x + 1), every m of degree <= 3.
  P-X  (added before its engine, after the others ran) The criterion in
       (5) sorts floor(n/m) into all three classes by the chain alone:
       readable at depth t iff the chain absorbs m past t, Lipschitz
       iff the least such lookahead is bounded, MIDDLE iff it is finite
       at every depth and unbounded, DISCONTINUOUS iff some depth never
       absorbs. On the sparse chain with radix 2 at the indices t that
       are powers of two and radix 3 elsewhere, floor(n/2) and
       floor(n/4) are MIDDLE, with c_min(n//2, t) = 2^(floor(log2 t) + 1)
       - t, floor(n/3) is Lipschitz at c <= 2, and floor(n/5) is
       discontinuous, over t = 1..40. So an empty arithmetic middle is a
       fact about fixed-radix chains, not about rings.
  P-C  At d = 2..6 the doubled comb's low digits take exactly d
       patterns over K, with period d(d + 1) in K, inputs agreeing to
       exactly K + d + 1 and doubles differing at a digit <= d - 2.

FINDINGS (entered after the run; prints copied from it).
  - The first run failed one positive control: floor(n/3) at base 10
    "read" at c = 4, 3, 2 at t = 1, 2, 3, because the brute scanned
    n < 30000 and past 10^(t + c) >= 30000 every input tile held one
    sample. The scan now covers four full periods of each input
    modulus; the control then prints [None, None, None]. P-X's first
    run failed n//4 on its lookahead ceiling of 80, below the
    c = 128 - t the depths t = 32..40 need; at 200 it passes.
  - P-L holds: 7n at [0, 0, 0], n//2 at [1, 1, 1], n//4 at [2, 2, 2].
  - P-B holds: 1/x-adic multiplication and division by x + 1 and
    x^2 + x + 1 fix output digits 1..j from input digits 1..j at every
    j to 12. Its 3-adic arm and both leading base 10 arms hold by
    algebra (multiplication mod 3^j is well defined; 3 (10^k - 1)/3 =
    10^k - 1, so 3y maps the tile 0.3...3 onto [1 - 10^-k,
    1 + 2 10^-k); 2a + 2 <= 10 (floor(2a/10) + 1)) and are argued,
    no longer checked.
  - P-W holds: y^2 emission at input depth 20, 60, 120, 200 is
    [0, 0, 0, 0] at sqrt(0.2) and sqrt(0.5), [-1, -1, -1, -1] at
    sqrt(2) and sqrt(3), [19, 59, 119, 199] at sqrt(1/3) and
    [19, 59, 119, 200] at sqrt(1/7).
  - P-M holds: c_min(D, t) = [0, 1, ..., 9] at t = 1..10.
  - P-R holds: over Z the brute agrees with m M_t | M_(t+c) at
    1142/1142 (chain, m, t, c) at bases 10, 12 and the primorial chain
    (this brute runs the one-step reduction the proof uses, so it
    checks the floor arithmetic, not the reduction); over F_2[x], where
    the brute takes every pair below its degree bound and is the only
    evidence for necessity, at 168/168. At the primorial chain n//3
    reads only at depth 1 and n//5 at depths 1 and 2; n//4 at none.
  - P-X holds: on the sparse chain n//2 has c_min
    [1, 2, 1, 4, 3, 2, 1, 8, 7, 6, ...], largest 32 over t = 1..40
    and equal to 2^(floor(log2 t) + 1) - t throughout; n//4 is finite
    everywhere, largest 96; n//3 at most 2; n//5 unread at all 40
    depths. Floor division falls in MIDDLE on a ring.
  - P-C holds at d = 2..6: d patterns, period d(d + 1), inputs
    agreeing to exactly K + d + 1, doubles apart at digit d - 2 (0, 1,
    2, 3, 4). At Zeckendorf the successor reads at c = 1 at t = 1..8
    and 2n at no c <= 6 at depths 1 to 3.
  - P-C2 holds: 112/112 doubles at d = 2..8 are the proof's phase
    sets; with the phase index shifted by one, 0/112 match.

SETTLED ON AUDIT (the argument above stays as frozen; these replace it).
  - (1) and (2): ball tiles have Lebesgue number at least delta_t (at
    base b exactly b delta_t), so the fit costs at most ceil(log_b L)
    digits. The overlapping cover's margin is not proved by a Lebesgue
    number, since the next commitment must be a child of the last. The
    ball regime holds for Lipschitz SELF-MAPS of the unit ball with
    ABSOLUTE tiles; read with the leading exponent first (floating
    tiles), a map cancelling leading digits needs unbounded lookahead
    at every place. A wall needs a NON-REDUNDANT numeration of R; an
    overlapping one (signed digits) reads y -> 3y. The archimedean
    price is the redundancy a wall-free numeration of R must carry.
  - (3): f must be increasing for the half-open tiles; a decreasing f
    can wall at a vertex: when B = -B, negation maps a tile [v, v + h)
    of width h onto (-v - h, -v], meeting the tiles on both sides of
    the vertex -v at every depth past -v's own, so it walls at every
    vertex v.
  - (5) over F_q[x]: necessity IS proved. If m does not divide M, write
    M = qm + s, s != 0, and take k = x^(deg m - deg s): floor(kM/m) =
    kq + a, a a nonzero constant, which cannot lie in (M_t). The brute
    search stands as a check, not as the only evidence.
  - (6) is proved at every d >= 2, one induction uniform in d. LEMMA
    0: a 0/1 string with no d consecutive ones is the greedy expansion
    of its value, since such a string on indices < k sums to at most
    q_k - 1 (one of the top d indices is absent; bases q_j - 1 =
    2^j - 1). LEMMA A: 2 q_k = q_(k+1) + q_(k-d) for k >= d, as
    2 q_k - q_(k+1) = q_k - q_(k-1) - ... - q_(k-d+1) = q_(k-d); and
    q_0 + ... + q_(d-1) = q_d. THE PHASES: write K = d + (d + 1) i'
    with i = i' mod d. For i <= d - 2 the digits of 2 T_K are the
    bottom {0, ..., i} and the teeth j = i + 1 mod d with
    d + 1 + i <= j <= K + 1; for i = d - 1 they are the teeth
    j = 0 mod d with d <= j <= K + 1. Base: 2 T_d = q_(d+1) + q_0.
    Step: 2 T_(K+d+1) = 2 T_K + q_(K+d+2) + q_(K+1) by Lemma A. The
    added q_(K+1) doubles the top tooth and each 2 q_j = q_(j+1) +
    q_(j-d) re-doubles the tooth d below, so every tooth moves up one,
    the deposits at j + 1 disjoint from the teeth left; at the bottom
    tooth d + 1 + i the carry moves q_(i+1) down onto the bottom, giving
    {0, ..., i + 1}, and at i = d - 2 the full bottom {0, ..., d - 1}
    consolidates to the tooth q_d; at i = d - 1 the tooth d splits to
    q_(d+1) + q_0. Every result has teeth d apart and its bottom run,
    of length at most d - 1, below a gap, so it is canonical by Lemma
    0. The d bottoms differ pairwise at a digit <= d - 2, so the d
    phase limits are d image points over the one input limit, and x2
    has no continuous extension at any d. The scan P-C is a check on
    this proof; P-C2 checks the stated sets themselves.
  P-C2 (predicted before its code) The greedy digits of 2 T_K equal
       the phase set above exactly, at d = 2..8 and every K = d +
       (d + 1) i' with i' < 3d + 1.
  - P-C's "positive control" 2n at Zeckendorf is the control that the
    scan sees a tear.
  - The QUESTION's "completing to an odometer or a torus translation":
    the d >= 3 completions are totally disconnected, measurably
    conjugate to a torus translation (Berthe, Jolivet and Siegel,
    Uniform Distribution Theory 7, 2012), not equal to one.
  - A wall is bounded emission, not only "no digit"; on a real
    interval every non-redundant numeration by interval tiles has one
    (y -> v + lam (y - y0), v a depth-1 endpoint), and signed binary
    digits read every L-Lipschitz self-map of [-1, 1] at lookahead
    ceil(log2 L) + 1, since an interval of length r/2 inside a tile of
    half-width r lies in one of its three children.

RUN RECORD: 18/18 checks, 2.5 s, peak commit 104 MB under a memory guard.
"""

import math

CHECKS = []


def check(name, ok, detail=""):
    CHECKS.append(bool(ok))
    tail = f"  ({detail})" if detail else ""
    print(f"  {'PASS' if ok else 'FAIL'}  {name}{tail}")


# ---------------------------------------------------------------- trailing
def trailing_cmin(f, mod_in, mod_out, t, cmax, reps):
    """Least c <= cmax such that f(n) mod mod_out(t) is fixed by
    n mod mod_in(t + c) over reps full periods of mod_in(t + c), so
    every input tile holds reps members; None if no c works."""
    for c in range(cmax + 1):
        Mi, Mo = mod_in(t + c), mod_out(t)
        seen, ok = {}, True
        for n in range(reps * Mi):
            key, val = n % Mi, f(n) % Mo
            if seen.setdefault(key, val) != val:
                ok = False
                break
        if ok:
            return c
    return None


def section_l():
    print("L  the lemma's ball regime at trailing base 10")
    p = lambda k: 10 ** k
    rows = {}
    for name, f in (("7n", lambda n: 7 * n), ("n//2", lambda n: n // 2),
                    ("n//4", lambda n: n // 4), ("n//3", lambda n: n // 3)):
        rows[name] = [trailing_cmin(f, p, p, t, 3, 4) for t in (1, 2, 3)]
        print(f"     {name:5s} c_min at t = 1, 2, 3: {rows[name]}")
    check("positive control: n//3 reads at no c <= 3 (3 is no unit of "
          "Z[1/10])", rows["n//3"] == [None] * 3)
    check("P-L: 7n at c = 0, n//4 at c = 2, n//2 at c = 1, depths 1 to 3",
          rows["7n"] == [0] * 3 and rows["n//4"] == [2] * 3
          and rows["n//2"] == [1] * 3)


# ---------------------------------------------------------- F_2[x] algebra
def pmul(a, b):
    r = 0
    while b:
        if b & 1:
            r ^= a
        a <<= 1
        b >>= 1
    return r


def pdivmod(a, b):
    q, db = 0, b.bit_length() - 1
    while a and a.bit_length() - 1 >= db:
        s = a.bit_length() - 1 - db
        q ^= 1 << s
        a ^= b << s
    return q, a


def ppow(a, k):
    r = 1
    for _ in range(k):
        r = pmul(r, a)
    return r


def section_b():
    print("B  which place pays for a wall: the 1/x-adic arm")
    # The 3-adic and leading base 10 arms hold by algebra (FINDINGS).
    # 1/x-adic arm over F_2: an input is its N leading digits, top digit 1
    N = 12
    okt = True
    for u in (0b11, 0b111):
        du = u.bit_length() - 1
        oku = True
        for mode in ("mul", "div"):
            for j in range(1, N + 1):
                seen = {}
                for low in range(1 << (N - 1)):
                    X = (1 << (N - 1)) | low
                    if mode == "mul":
                        Y = pmul(X, u)
                    else:
                        Y = pdivmod(X << (du + 1), u)[0]
                    top = Y >> (Y.bit_length() - j)
                    key = X >> (N - j)
                    if seen.setdefault(key, top) != top:
                        oku = False
        okt &= oku
        print(f"     1/x-adic u = {bin(u)}: y*u and y/u, output digits "
              f"1..j fixed by input digits 1..j, j = 1..{N}: {oku}")
    check("P-B 1/x-adic arm: multiplication and division by x + 1 and "
          "x^2 + x + 1 read at c = 0", okt)


# ------------------------------------------------------------------ walls
def leading_emission(num, den, n):
    """Output depth committed by y -> y^2 at leading base 10 on the
    depth-n input tile around sqrt(num/den); -1 is a tile of width 10,
    -2 not even that."""
    Y = math.isqrt(num * 10 ** (2 * n) // den)
    lo, hi = Y * Y, (Y + 1) * (Y + 1)        # units 10^-2n, half-open
    best = -2
    for t in range(-1, 2 * n + 1):
        w = 10 ** (2 * n - t)
        k = lo // w
        if hi <= (k + 1) * w:
            best = t
        else:
            break
    return best


def section_w():
    print("W  the wall criterion at leading base 10, y -> y^2")
    frozen, grows = {}, {}
    for label, num, den in (("sqrt(0.2)", 1, 5), ("sqrt(0.5)", 1, 2),
                            ("sqrt(2)", 2, 1), ("sqrt(3)", 3, 1),
                            ("sqrt(1/3)", 1, 3), ("sqrt(1/7)", 1, 7)):
        e = [leading_emission(num, den, n) for n in (20, 60, 120, 200)]
        print(f"     {label:9s} emission at input depth 20, 60, 120, 200: "
              f"{e}")
        frozen[label] = len(set(e)) == 1
        grows[label] = e[-1] >= 190
    check("P-W: sqrt(0.2), sqrt(0.5), sqrt(2), sqrt(3) freeze",
          all(frozen[k] for k in ("sqrt(0.2)", "sqrt(0.5)", "sqrt(2)",
                                  "sqrt(3)")))
    check("P-W: sqrt(1/3), sqrt(1/7) emit without bound",
          grows["sqrt(1/3)"] and grows["sqrt(1/7)"])


# ----------------------------------------------------------------- middle
def section_m():
    print("M  the middle class: the decimation at base 2")

    def D(n):
        out, t = 0, 0
        while n >> (2 * t):
            out |= ((n >> (2 * t)) & 1) << t
            t += 1
        return out

    p = lambda k: 2 ** k
    got = [trailing_cmin(D, p, p, t, 12, 4) for t in range(1, 11)]
    print(f"     c_min(D, t), t = 1..10: {got}")
    check("P-M: c_min(D, t) = t - 1", got == list(range(10)))


# ----------------------------------------------------------------- chains
def primorial(t):
    ps, x, n = [], 1, 2
    while len(ps) < t:
        if all(n % p for p in ps):
            ps.append(n)
            x *= n
        n += 1
    return x


def int_brute(m, N, M):
    """Division by m keeps its quotient mod N across every one-step
    pair (n, n + M), n over three periods of m?"""
    return all((n + M) // m % N == n // m % N for n in range(3 * m))


def poly_brute(m, N, M):
    """Over F_2[x]: all n below degree deg M + deg m + 2, grouped by
    n mod M, keep n div m mod N?"""
    D = (M.bit_length() - 1) + (m.bit_length() - 1) + 2
    seen = {}
    for n in range(1 << D):
        key = pdivmod(n, M)[1]
        val = pdivmod(pdivmod(n, m)[0], N)[1]
        if seen.setdefault(key, val) != val:
            return False
    return True


def section_r():
    print("R  the division criterion on a divisor chain")
    agree = total = 0
    for mods, ms, ts, cs in (
            (lambda k: 10 ** k, range(2, 13), (1, 2, 3), range(5)),
            (lambda k: 12 ** k, range(2, 13), (1, 2, 3), range(5)),
            (primorial, range(2, 31), (1, 2, 3, 4), range(7))):
        for m in ms:
            for t in ts:
                for c in cs:
                    N, M = mods(t), mods(t + c)
                    total += 1
                    agree += int_brute(m, N, M) == (M % (m * N) == 0)
    print(f"     Z chains (bases 10, 12, primorial): brute agrees with "
          f"m M_t | M_(t+c) at {agree}/{total} (chain, m, t, c)")
    check("P-R over Z: the criterion matches the brute pair search",
          agree == total)
    reads = {m: [t for t in range(1, 6)
                 if any(primorial(t + c) % (m * primorial(t)) == 0
                        for c in range(8))] for m in (3, 5, 15, 35, 4)}
    print(f"     primorial chain, depths t <= 5 at which n//m reads at "
          f"some c <= 7: {reads}")
    check("P-R primorial: n//3 reads at depth 1, n//5 at 1 and 2, n//4 "
          "at none, t <= 5",
          reads[3] == [1] and reads[5] == [1, 2] and reads[4] == [])
    agree = total = 0
    for g in (0b10, 0b110):
        for m in range(2, 16):
            for t in (1, 2):
                for c in (0, 1, 2):
                    N, M = ppow(g, t), ppow(g, t + c)
                    total += 1
                    crit = pdivmod(M, pmul(m, N))[1] == 0
                    agree += poly_brute(m, N, M) == crit
    print(f"     F_2[x] at bases x and x^2 + x: brute agrees with "
          f"m M_t | M_(t+c) at {agree}/{total} (base, m, t, c)")
    check("P-R over F_2[x]: the criterion matches the brute search",
          agree == total)


def section_x():
    print("X  the three classes on one sparse chain")
    radix = lambda t: 2 if t & (t - 1) == 0 else 3
    M = [1]
    for t in range(1, 260):
        M.append(M[-1] * radix(t))
    cls = {}
    for m in (2, 3, 4, 5):
        cs = []
        for t in range(1, 41):
            c = next((c for c in range(0, 200)
                      if int_brute(m, M[t], M[t + c])), None)
            cs.append(c)
        cls[m] = cs
        seen = [x for x in cs if x is not None]
        top = max(seen) if seen else None
        print(f"     n//{m}: c_min at t = 1..10 {cs[:10]}, largest over "
              f"t = 1..40 {top}, unread depths {cs.count(None)}")
    want2 = [2 ** (t.bit_length()) - t for t in range(1, 41)]
    check("P-X: n//2 is MIDDLE, c_min = 2^(floor(log2 t) + 1) - t",
          cls[2] == want2 and None not in cls[2])
    check("P-X: n//4 is finite at every depth and unbounded",
          None not in cls[4] and max(cls[4]) >= 16)
    check("P-X: n//3 is Lipschitz at c <= 2", max(cls[3]) <= 2)
    check("P-X: n//5 reads at no depth", cls[5] == [None] * 40)


# ------------------------------------------------------------------ combs
def greedy(n, q):
    digs = set()
    for k in range(len(q) - 1, -1, -1):
        if q[k] <= n:
            digs.add(k)
            n -= q[k]
    assert n == 0
    return digs


def first_diff(a, b):
    d = a ^ b
    return min(d) if d else None


def section_c():
    print("C  the comb: x2 against the d-bonacci numerations")
    allok = True
    for d in range(2, 7):
        per = d * (d + 1)
        Ks = [d + (d + 1) * i for i in range(3 * d + 1)]
        q = [2 ** j for j in range(d)]
        while len(q) < Ks[-1] + 2 * d + 4:
            q.append(sum(q[-d:]))
        T = {K: sum(q[j] for j in range(d, K + 1, d + 1)) for K in Ks}
        pats = {K: frozenset(x for x in greedy(2 * T[K], q) if x < d)
                for K in Ks}
        npat = len(set(pats.values()))
        periodic = all(pats[K] == pats[K + per] for K in Ks
                       if K + per in pats)
        pairs = [K for K in Ks if K + d + 1 in T]
        agree = all(first_diff(greedy(T[K], q), greedy(T[K + d + 1], q))
                    == K + d + 1 for K in pairs)
        low = max(first_diff(greedy(2 * T[K], q),
                             greedy(2 * T[K + d + 1], q)) for K in pairs)
        ok = npat == d and periodic and agree and low <= d - 2
        allok &= ok
        print(f"     d = {d}: patterns {npat}, period d(d + 1) = {per} "
              f"{periodic}, inputs agree to K+d+1 {agree}, doubles first "
              f"apart at a digit <= {low}")
    check("P-C: d patterns, period d(d + 1), agreement K + d + 1, "
          "doubles apart at a digit <= d - 2, d = 2..6", allok)
    # the proof's phase sets, read against greedy extraction
    def phase_set(d, i, K):
        if i <= d - 2:
            return set(range(i + 1)) | {j for j in range(d + 1 + i, K + 2)
                                        if j % d == (i + 1) % d}
        return {j for j in range(d, K + 2) if j % d == 0}

    miss = cells = shifted = 0
    for d in range(2, 9):
        Ks = [d + (d + 1) * i for i in range(3 * d + 1)]
        q = [2 ** j for j in range(d)]
        while len(q) < Ks[-1] + 2 * d + 4:
            q.append(sum(q[-d:]))
        for n, K in enumerate(Ks):
            T = sum(q[j] for j in range(d, K + 1, d + 1))
            got = greedy(2 * T, q)
            cells += 1
            miss += got != phase_set(d, n % d, K)
            shifted += got == phase_set(d, (n + 1) % d, K)
    print(f"     phase sets: {cells - miss}/{cells} doubles match the proof; "
          f"with the phase index shifted by one, {shifted}/{cells}")
    check("P-C2: the proof's phase set is 2 T_K's digits, d = 2..8",
          miss == 0 and cells > 0)
    check("negative control: the phase sets shifted by one match no double",
          shifted == 0)
    # the successor reads at Zeckendorf; x2 is the positive control
    q = [1, 2]
    while q[-1] < 30000:
        q.append(q[-1] + q[-2])
    lim = q[-1]
    masks = [sum(1 << k for k in greedy(n, q)) for n in range(2 * lim)]

    def zc(f, t):
        for c in range(7):
            seen, ok = {}, True
            for n in range(lim):
                key = masks[n] & ((1 << (t + c)) - 1)
                val = masks[f(n)] & ((1 << t) - 1)
                if seen.setdefault(key, val) != val:
                    ok = False
                    break
            if ok:
                return c
        return None

    inc = [zc(lambda n: n + 1, t) for t in range(1, 9)]
    dbl = [zc(lambda n: 2 * n, t) for t in (1, 2, 3)]
    print(f"     Zeckendorf c_min: n + 1 at t = 1..8 {inc}; 2n at "
          f"t = 1..3 {dbl}")
    check("positive control: 2n reads at no c <= 6 at Zeckendorf, "
          "depths 1 to 3",
          dbl == [None] * 3)
    check("the successor reads at c = 1 at every scanned depth",
          inc == [1] * 8)


def main():
    section_l()
    section_b()
    section_w()
    section_m()
    section_r()
    section_x()
    section_c()
    print(f"{sum(CHECKS)}/{len(CHECKS)} checks passed")
    raise SystemExit(0 if all(CHECKS) else 1)


if __name__ == "__main__":
    main()
