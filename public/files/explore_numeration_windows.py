"""
What a base buys (MOONSHOT probe, P96; the P87 base seed): numeration
systems read through the windows -- the two-readings criterion and the
readability chart.

Setting: the walls corpus asks of every operation "through which
residue window can it be read?"; this chart asks it of REPRESENTATIONS
of the naturals. A numeration system is a digit map plus readers, and
the instrument is a locality grade per (system, query):
 - WINDOW-READ (L0): answer is a function of O(1) digit positions,
   independent of input length; for position-indexed queries (digit j
   of a sum, divisibility read at a suffix) the window is a fixed-size
   set placed relative to the queried position, UNIFORM in it -- for
   one fixed j, digit j of x + y is trivially a function of positions
   0..j, so only the uniform grade is a wall statement.
 - SCAN-READ (L1): one pass, O(1) state -- a finite automaton or
   transducer over digits (direction named: LSD- or MSD-first;
   multi-input queries read aligned digit tuples, Buchi convention).
 - WALLED (L2): no fixed window and no O(1)-state pass; needs
   unbounded state / full reconstruction.

The census, each system anchored at its Ostrowski window(s):
 - positional base b: digits are BOTH the b-adic residue ladder
   n mod b^j (finite place, one prime set rad(b), growing depth) AND
   the greedy size decomposition (archimedean window, MSD-first).
 - mixed radix on a divisibility chain (factorial, primorial): the
   same two readings; the scale chain is a chain of quotients.
 - CRT residues at a prime set P (the tower's representation): finite
   places, many windows, depth 1. No archimedean reading.
 - greedy on a NON-chain scale (Zeckendorf on Fibonacci): archimedean
   reading only -- prefixes are NOT residues (proved below).
 - exponent vector n = prod p^(a_p): the valuation half of every
   finite place; multiplicative queries go window-local, addition
   dies.

PREDICTIONS (stated before the run, P86 discipline; adjudication
recorded per item after the run -- PR1-PR7 all landed; the one
number not predicted in advance, the Nerode class counts of PR6,
came out at the saturation ceiling, recorded there):
 PR1 (criterion, proved + swept exact): THE TWO-READINGS CRITERION.
     For greedy numeration on a scale 1 = U_0 < U_1 < U_2 < ...,
     the low prefix (digits 0..j-1, weighted) equals n mod U_j for
     ALL n and j **iff** the scale is a divisibility chain
     (U_j | U_i for all i >= j). Proof (<=): greedy leaves remainder
     < U_i after each step, so the prefix value is < U_j, and every
     subtracted term U_i (i >= j) is 0 mod U_j. Proof (=>): n = U_i
     has the single-digit greedy rep, prefix value 0, forcing
     U_i = 0 mod U_j. Verified: exhaustive over ALL 9139 scales
     (1, a, b, c), 2 <= a < b < c <= 40, AND all 3876 length-5
     scales (1, a, b, c, d) <= 20 -- property holds iff chain, no
     exceptions either sweep (S1c); chain battery base 2/10,
     factorial, primorial pass at depth (S1a); Zeckendorf fails with
     witnesses both ways (S1b). LANDED.
 PR2 (rule, proved + verified): GREEDY BUYS ORDER. For EVERY scale
     (chain or not), greedy digit strings in MSD-first lex order ARE
     numeric order (first differing digit d_i < d'_i forces
     x < y since the low part is < U_i). So size = top position and
     order = lex scan are what GREEDY buys; residue prefixes are what
     the CHAIN buys; base b is the coincidence -- one string, both
     windows. Verified: sortedness of reversed digit tuples over six
     scales incl. Zeckendorf and a non-chain scale (S2). LANDED.
 PR3 (rules, witness families): THE CARRY WALL. Addition in base b is
     NOT window-read -- for every window half-width w there are input
     pairs agreeing on the window around position j with different
     output digit j (the nines family: carry chains propagate
     arbitrarily far), and the HOLE family (launch the carry from a
     single position m strictly between a low band {0..w} and the
     band around j; the inputs differ only at m) defeats the natural
     augmented window too -- since m can dodge ANY fixed finite set,
     the same construction rules out every uniform window (rule,
     proved; both families verified, S3a) -- but addition IS
     scan-read: the LSD-first transducer with one carry state
     computes it exactly (S3b).
     Zeckendorf has the same wall shape (the alternating-sum cascade
     F_2+F_4+...+F_{2m} = F_{2m+1}-1: adding 1 rewrites the whole
     string; S3d); its scan-read repair is classical (Frougny: for
     Pisot scales, normalization/addition is a finite transducer --
     contact, not re-proved). CRT addition and multiplication are
     window-read by construction (depth-1 reads, one channel in, one
     channel out; S3c). The exponent vector WALLS addition
     entirely: for ANY finite prime window W there is a CRT-built
     family y_t (== 2^t - 1 mod 2^(t+1), == 1 mod every other p in W)
     whose W-window exponent vector is constant zero while
     v_2(1 + y_t) = t takes every value -- no function of any fixed
     window computes even one coordinate of a sum (proved: CRT always
     solves the congruences; verified t = 3..12 at W = {2,3,5,7};
     S3e). LANDED.
 PR4 (witnesses): SIZE/ORDER ARE WALLED off the archimedean window.
     CRT: (1, 31) vs (31, 1) -- identical residue windows mod 30,
     opposite order (the archimedean wall, WALLS.md SII, holding at
     the representation level; S4a). Exponent vector: 7 and 23 have
     the same all-zero {2,3,5}-window, 7 < 11 < 23 (S4b). LANDED.
 PR5 (criterion, proved + verified): DIVISIBILITY LOCALITY IN BASE b.
     m | n is window-read from the last j digits iff m | b^j (iff
     rad(m) | rad(b)): (<=) n == suffix mod b^j; (=>) n = 0 vs
     n = b^j share the suffix, forcing m | b^j. Every fixed m is
     scan-read (MSD Horner automaton, m states; S5b). CRT: p | n is
     window-read (one digit = 0) for p in P; q outside P is WALLED --
     (q, q + N) share the whole P-window and disagree (S5c; the same
     witness shape is the membership-certificate clause, ALGEBRA.md
     SXII: no finite window is injective on N). Exponent vector:
     divisibility, gcd, lcm all window-read (componentwise <=, min,
     max on supp(m); S5d). Verified m = 8 (j = 3) vs m in
     {3, 7, 9, 11} witnessed at every j <= 5 (S5a). Zeckendorf sits
     between: divisibility is recognizable for Pisot scales (the
     Bruyere-Hansel logic with addition -- contact, not re-proved)
     but NOT window-read from any suffix -- (0, U_j) with U_j odd
     share every suffix of width w < j and differ in parity
     (witnessed for w <= 8; S5f). LANDED.
 PR6 (classical contact + observation): PRIMALITY IS WALLED in every
     base (primes are not recognizable by finite automata --
     Minsky-Papert 1966; any base and stronger machine classes,
     Hartmanis-Shank 1968; contacts, not re-proved). Computed
     evidence at the instrument's own tier: the Nerode lower bound --
     binary prefixes of length L distinguished by primality of
     8-bit extensions -- GROWS with L (S5e). LANDED: class counts
     32/64/128/256/512 at L = 6..10 -- the bound saturates its
     ceiling 2^(L-1) at EVERY tested length (all prefix pairs
     distinguished); the saturation was not predicted in advance,
     recorded as observed.
 PR7 (census observation): NO FREE ROW. Every system in the census
     pays -- a walled query at its stated tier, or (the diagonal) the
     unbounded alphabet -- and buys a reading (S8; a fact of THIS
     census, not a theorem over all systems). LANDED.

THE CHART (the readability chart -- locality grade per system x query;
L0 = window-read, L1 = scan-read, L2 = walled; L2? = expected walled,
stated at expectation tier -- no proof and no transferable contact):

  system / query   size   order  add    mult      m | n          prime?
  base b           L0*    L1     L1     L2(x)     L0 iff rad(m)  L2 (M-P,
                                                  |rad(b), else L1  H-S)
  mixed radix      L0*    L1     L1     L2?       L0 at j with   L2?
  (chain: fact.,                                  m | U_j (fact.:
  primorial)                                      all m; primorial:
                                                  squarefree m)
  CRT at P         L2     L2     L0     L0        L0 (p in P)    L2
                                                  L2 (q not in P)
  Zeckendorf       L0*    L1     L1(F)  L2(x')    L1(F), not L0  L2?
  exponent vector  L2     L2     L2     L0        L0 (+gcd,lcm)  L1 (scan:
                                                                 one entry,
                                                                 equal 1)
    (* size = top position: one read IF the length/top pointer is
     given; as a digit-string question it is the L1 length scan.
     (F) = Frougny's Pisot transducers, classical contact.
     (x) = full multiplication: not b-recognizable -- with it,
     Buchi arithmetic (N, +, V_b) would decide multiplication;
     contact. (x') = same argument through the decidable Pisot
     logic (Bruyere-Hansel). Mult-by-CONSTANT is L1 (S6a).
     L2? cells: the constant-base contacts do not transfer verbatim
     to a growing alphabet (mixed radix) or to Zeckendorf primality;
     no claim minted. CRT prime? L2: witnessed -- (7, 187) share the
     mod-30 window, 7 prime, 187 = 11 x 17 (S5c).)

Readings of the chart (the seed's answer):
 - WHAT A BASE BUYS: base b (and every divisibility-chain mixed
   radix) is the COINCIDENCE of the two readings -- one digit string
   is simultaneously the archimedean greedy expansion (size at the
   top, order by lex scan) and the residue ladder n mod U_j (carries
   by one-state scan, divisibility by the ladder moduli window-read
   at the low digits). The two-readings
   criterion says the coincidence is EXACTLY the divisibility chain --
   Zeckendorf keeps only the greedy half, the tower keeps only the
   residue half, the exponent vector keeps only the valuation half.
 - THE TOWER AS A CELL: the CRT row's walls (size, order, out-of-set
   divisibility) are the walls corpus read at the representation
   level; the deletion names the window the row dropped. Its buys --
   window-read + and x -- are exactly what the carry ladder pays for.
 - THE DIAGONAL: factorial/primorial mixed radix is a divisibility
   chain THROUGH every prime, so it reads both windows AND all
   finite places -- the factorial chain window-reads EVERY m | n
   (m | m! always; S7a), the primorial chain exactly the SQUAREFREE
   m (m | p_j# iff m squarefree over primes <= p_j -- 4 divides no
   primorial); the price is the unbounded digit alphabet (radix
   grows with position; S7a).
 - HARD PROBLEMS LIVE BETWEEN WINDOWS (framing observation): each
   column is L0/L1 in SOME row; factoring/primality are the transport
   problem between the additive rows and the valuation row.

Classical contacts (named, not re-proved): Ostrowski (the window
census itself); Buchi-Bruyere ((N, +, V_b): b-recognizable =
definable; multiplication breaks it); Cobham-Semenov (recognizable in
two independent bases = eventually periodic -- the cross-base
rigidity behind "the chart is per-base"); Frougny (Pisot numeration:
normalization/addition finite-state); Renyi (beta-expansions, the
non-chain greedy family); Minsky-Papert 1966 + Hartmanis-Shank 1968
(primes not finite-automaton recognizable, any base);
Bruyere-Hansel (Pisot-scale recognizability with addition); Fraenkel
(mixed-radix systems of numeration).

Provenance (at birth): none of this needs the tower -- the carrier is
generic greedy numeration on N (the criterion) and finite-state
readers (the grades). The tower enters as the residue-only ROW of the
chart, and the deletion names which window that row is missing; the
primorial chain is the diagonal cell. The chart is the walls corpus'
question asked one level up: not "which window reads this operation"
but "which windows does a REPRESENTATION keep readable".

Run: python prime/code/explore_numeration_windows.py   (~1 s, pure
Python, memory trivial). Checks: 22.
"""

import sys

# ---------------------------------------------------------------- helpers

CHECKS = []


def check(name, cond):
    status = "PASS" if cond else "FAIL"
    print("  [%s] %s" % (status, name))
    CHECKS.append((name, bool(cond)))


def greedy(n, U):
    """Greedy digits of n on scale U (U[0] == 1, strictly increasing).
    d[i] multiplies U[i]; the top digit may exceed the local radix if n
    is large -- prefix/order tests are unaffected."""
    d = [0] * len(U)
    rem = n
    for i in reversed(range(len(U))):
        d[i], rem = divmod(rem, U[i])
    return d


def prefix_val(d, U, j):
    return sum(d[i] * U[i] for i in range(j))


def digit(n, base, i):
    return n // base ** i % base


def v2(n):
    t = 0
    while n % 2 == 0:
        n //= 2
        t += 1
    return t


def crt_pair(r1, m1, r2, m2):
    # m1, m2 coprime
    x = r1
    while x % m2 != r2:
        x += m1
    return x


def expvec(n, W):
    out = []
    for p in W:
        t = 0
        while n % p == 0:
            n //= p
            t += 1
        out.append(t)
    return tuple(out)


SCALES = {
    "base2": [2 ** i for i in range(13)],
    "base10": [10 ** i for i in range(5)],
    "factorial": [1, 2, 6, 24, 120, 720, 5040],
    "primorial": [1, 2, 6, 30, 210, 2310],
    "fibonacci": [1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610,
                  987, 1597, 2584, 4181, 6765, 10946, 17711, 28657],
    "nonchain": [1, 3, 7, 19, 50, 131],
}
SCALES["base2"][0] = 1  # 2**0 already 1; explicit


# ------------------------------- S1: the two-readings criterion


def s1a():
    ok = True
    for name in ("base2", "base10", "factorial", "primorial"):
        U = SCALES[name]
        for n in range(4000):
            d = greedy(n, U)
            for j in range(1, len(U)):
                if prefix_val(d, U, j) != n % U[j]:
                    ok = False
    check("S1a two-readings: chain scales (base 2/10, factorial, primorial), prefix = residue, n < 4000, all depths", ok)


def s1b():
    U = SCALES["fibonacci"]
    # (=>)-proof witness: n = U_3 = 5, prefix_1 = 0 but 5 mod 2 = 1
    d5 = greedy(5, U)
    w1 = prefix_val(d5, U, 1) == 0 and 5 % U[1] == 1
    # same residue mod U_1 = 2, different prefixes: n = 1 vs n = 3
    w2 = (1 % 2 == 3 % 2) and prefix_val(greedy(1, U), U, 1) != prefix_val(greedy(3, U), U, 1)
    # same prefix, different residue: n = 0 vs n = 5
    w3 = (prefix_val(greedy(0, U), U, 1) == prefix_val(d5, U, 1)) and (0 % 2 != 5 % 2)
    check("S1b two-readings: Zeckendorf prefixes are NOT residues (witnesses both directions)", w1 and w2 and w3)


def s1c():
    def sweep(scales_iter):
        ok, tested = True, 0
        for U in scales_iter:
            chain = all(U[i + 1] % U[i] == 0 for i in range(1, len(U) - 1))
            holds = True
            for n in range(3 * U[-1]):
                d = greedy(n, U)
                for j in range(1, len(U)):
                    if prefix_val(d, U, j) != n % U[j]:
                        holds = False
                        break
                if not holds:
                    break
            if holds != chain:
                ok = False
            tested += 1
        return ok, tested

    ok4, t4 = sweep([1, a, b, c]
                    for a in range(2, 41)
                    for b in range(a + 1, 41)
                    for c in range(b + 1, 41))
    ok5, t5 = sweep([1, a, b, c, d]
                    for a in range(2, 21)
                    for b in range(a + 1, 21)
                    for c in range(b + 1, 21)
                    for d in range(c + 1, 21))
    check("S1c two-readings criterion: property <=> divisibility chain, exact on all %d scales (1,a,b,c) <= 40 and all %d scales (1,a,b,c,d) <= 20" % (t4, t5), ok4 and ok5)


# ------------------------------- S2: greedy buys order


def s2():
    ok = True
    for name, U in SCALES.items():
        reps = [tuple(reversed(greedy(n, U))) for n in range(800)]
        if reps != sorted(reps):
            ok = False
    check("S2 greedy buys order: MSD-lex = numeric order on all 6 scales incl. Zeckendorf + non-chain, n < 800", ok)


# ------------------------------- S3: the carry wall


def s3a():
    # Family 1 (nines): defeats any window [j-w, j+w] around the queried
    # position -- the inputs differ only at position 0, below the window.
    ok = True
    for base in (2, 10):
        for w in range(6):
            j = w + 1
            x = base ** (j + 1) - 1          # digits b-1 at positions 0..j
            xp = x - (base - 1)              # position 0 dropped to 0
            lo, hi = j - w, j + w
            agree = all(digit(x, base, i) == digit(xp, base, i)
                        for i in range(lo, hi + 1))
            differ = digit(x + 1, base, j) != digit(xp + 1, base, j)
            if not (lo >= 1 and agree and differ):
                ok = False
    check("S3a carry wall: base-b addition not window-read (nines family, w = 0..5, bases 2 and 10)", ok)
    # Family 2 (the hole): defeats the augmented window {0..w} + [j-w, j+w]
    # -- the carry is launched from a single position m strictly between
    # the bands (x and x' differ only at m; x' + y = x exactly). Since m
    # can dodge any fixed finite set the same way, no uniform window works.
    ok2 = True
    for base in (2, 10):
        for w in range(5):
            j, m = 2 * w + 4, w + 2          # w < m < j - w
            x = sum((base - 1) * base ** i for i in range(m, j + 1))
            xp = x - base ** m               # digit m: b-1 -> b-2
            y = base ** m
            S = list(range(0, w + 1)) + list(range(j - w, j + w + 1))
            agree = all(digit(x, base, i) == digit(xp, base, i) for i in S if i != m)
            outside = m not in S
            differ = digit(x + y, base, j) != digit(xp + y, base, j)
            if not (agree and outside and differ and xp + y == x):
                ok2 = False
    check("S3a carry wall: the hole family defeats the augmented window {0..w} + band(j, w) too (w = 0..4)", ok2)


def s3b():
    def add_scan(x, y, base, L):
        carry, out = 0, 0
        for i in range(L):
            s = digit(x, base, i) + digit(y, base, i) + carry
            out += (s % base) * base ** i
            carry = s // base
        return out

    ok = True
    for base in (2, 3, 10):
        for x in range(0, 300):
            for y in range(0, 300):
                if add_scan(x, y, base, 12) != x + y:
                    ok = False
    # mixed radix: same one-carry-state scan (carry <= 1 since per-position
    # digits are < radix: d1 + d2 + 1 <= 2*radix - 1)
    U = SCALES["factorial"]

    def add_scan_mixed(x, y):
        dx, dy = greedy(x, U), greedy(y, U)
        carry, out = 0, 0
        for i in range(len(U)):
            radix = (U[i + 1] // U[i]) if i + 1 < len(U) else 10 ** 9
            s = dx[i] + dy[i] + carry
            out += (s % radix) * U[i]
            carry = s // radix
        return out

    for x in range(0, 300):
        for y in range(0, 300):
            if add_scan_mixed(x, y) != x + y:
                ok = False
    check("S3b carry wall: LSD one-carry-state transducer computes + exactly (bases 2/3/10 + factorial scale, exhaustive x,y < 300)", ok)


def s3c():
    # CRT: + and x are window-read by construction -- channel output is a
    # function of channel inputs alone (implementation-consistency check
    # of the corpus locality law, exhaustive Z/30 pairs).
    ok = True
    for p in (2, 3, 5):
        for op in (lambda u, v: u + v, lambda u, v: u * v):
            table = {}
            for x in range(30):
                for y in range(30):
                    key = (x % p, y % p)
                    val = op(x, y) % p
                    if table.setdefault(key, val) != val:
                        ok = False
    check("S3c CRT: + and x window-read per channel (exhaustive Z/30, all 900 pairs, both ops)", ok)


def s3d():
    U = SCALES["fibonacci"]
    ok = True
    for m in range(1, 7):
        x = sum(U[i] for i in range(0, 2 * m, 2))   # U_0+U_2+...+U_{2m-2}
        xp = x - 1                                   # drop the bottom term
        j = 2 * m - 1
        dx, dxp = greedy(x, U), greedy(xp, U)
        agree = all(dx[i] == dxp[i] for i in range(1, len(U)))  # differ only at 0
        d_out, d_outp = greedy(x + 1, U), greedy(xp + 1, U)
        if not (agree and d_out[j] != d_outp[j]):
            ok = False
    check("S3d carry wall in Zeckendorf: the alternating-sum cascade (inputs differ at digit 0, sums differ at the top), m = 1..6", ok)


def s3e():
    W = [2, 3, 5, 7]
    ok = True
    base_vec = (0, 0, 0, 0)  # the all-zero window
    for t in range(3, 13):
        y = crt_pair(2 ** t - 1, 2 ** (t + 1), 1, 3 * 5 * 7)
        if expvec(y, W) != base_vec:
            ok = False
        if v2(1 + y) != t:
            ok = False
    # small witness: same window, different v2 of the sum
    small = expvec(7, [2, 3, 5]) == expvec(11, [2, 3, 5]) and v2(1 + 7) != v2(1 + 11)
    check("S3e exponent vector walls +: constant zero W-window, v2(1+y_t) = t for t = 3..12 (W = {2,3,5,7}) + small witness", ok and small)


# ------------------------------- S4: size/order off the archimedean window


def s4a():
    r = lambda n: (n % 2, n % 3, n % 5)
    ok = r(1) == r(31) and (1 < 31) and not (31 < 1)
    check("S4a CRT walls order: (1,31) vs (31,1) -- identical mod-30 windows, opposite order", ok)


def s4b():
    W = [2, 3, 5]
    ok = (expvec(7, W) == expvec(23, W) and 7 < 11 < 23
          and len(bin(7)) != len(bin(23)))  # size differs too, same window
    check("S4b exponent vector walls size/order: 7 vs 23 share the zero window, straddle 11", ok)


# ------------------------------- S5: divisibility


def s5a():
    # m = 8: window-read from the last 3 digits (8 | 1000)
    ok = all((n % 8 == 0) == ((n % 1000) % 8 == 0) for n in range(4000))
    # m in {3,7,9,11}: the witness pair (0, 10^j) shares the j-digit
    # suffix (both all-zero) and disagrees on m-divisibility
    for m in (3, 7, 9, 11):
        for j in range(0, 6):
            same_suffix = (0 % 10 ** j) == (10 ** j % 10 ** j) if j > 0 else True
            disagree = (0 % m == 0) != (10 ** j % m == 0)
            if not (same_suffix and disagree):
                ok = False
    check("S5a suffix criterion: 8 | n from 3 digits; 3/7/9/11 defeated at every suffix window j <= 5 (base 10)", ok)


def s5b():
    ok = True
    for m in (3, 7, 9, 11, 12):
        for n in range(4000):
            state = 0
            for ch in str(n):
                state = (state * 10 + int(ch)) % m
            if state != n % m:
                ok = False
    check("S5b every m is scan-read in base b: MSD Horner automaton, m states (m = 3/7/9/11/12, n < 4000)", ok)


def s5c():
    ok = all(7 % p == 37 % p for p in (2, 3, 5)) \
        and 7 % 7 == 0 and 37 % 7 != 0
    # primality is walled the same way: (7, 187) share the window,
    # 7 is prime, 187 = 11 x 17
    ok = ok and all(7 % p == 187 % p for p in (2, 3, 5)) and 187 == 11 * 17
    check("S5c CRT walls out-of-set divisibility and primality: (7, 37) and (7, 187) share the whole P-window", ok)


def s5d():
    import math
    W = [2, 3, 5, 7, 11, 13]

    def vec(n):
        return expvec(n, W)

    def smooth(n):
        v = vec(n)
        out = 1
        for p, a in zip(W, v):
            out *= p ** a
        return out == n

    ok = True
    for m in range(1, 60):
        if not smooth(m):
            continue
        vm = vec(m)
        for n in range(1, 300):
            if not smooth(n):
                continue
            vn = vec(n)
            if (n % m == 0) != all(a <= b for a, b in zip(vm, vn)):
                ok = False
            if vec(math.gcd(m, n)) != tuple(min(a, b) for a, b in zip(vm, vn)):
                ok = False
    check("S5d exponent vector: m | n = componentwise <=, gcd = min (all 13-smooth m < 60, n < 300)", ok)


def s5f():
    # Zeckendorf divisibility is not window-read from a suffix: (0, U_j)
    # with U_j odd share every suffix of width w < j (all-zero low
    # digits) and differ in parity.
    U = SCALES["fibonacci"]
    ok = True
    for w in range(0, 9):
        found = False
        for j in range(w + 1, len(U)):
            if U[j] % 2 == 1:
                d = greedy(U[j], U)
                if all(d[i] == 0 for i in range(w + 1)) and U[j] % 2 != 0 % 2:
                    found = True
                    break
        if not found:
            ok = False
    check("S5f Zeckendorf: parity not window-read from any suffix w <= 8 (witness (0, U_j), U_j odd)", ok)


def s5e():
    E = 8
    LIMIT = 2 ** 19
    sieve = bytearray([1]) * LIMIT
    sieve[0] = sieve[1] = 0
    for i in range(2, int(LIMIT ** 0.5) + 1):
        if sieve[i]:
            sieve[i * i::i] = bytearray(len(sieve[i * i::i]))
    counts = []
    for L in range(6, 11):
        vecs = set()
        for u in range(2 ** (L - 1), 2 ** L):
            base_val = u << E
            vecs.add(bytes(sieve[base_val + w] for w in range(2 ** E)))
        counts.append(len(vecs))
    growing = all(a < b for a, b in zip(counts, counts[1:]))
    print("    Nerode lower bound (binary, 8-bit extensions), L = 6..10: %s" % counts)
    check("S5e primality evidence: Nerode class lower bound grows with prefix length (contact: Minsky-Papert)", growing)


# ------------------------------- S6: multiplication


def s6a():
    ok = True
    for c in (3, 7):
        for n in range(4000):
            carry, out = 0, 0
            for i in range(8):
                d = digit(n, 10, i)
                s = c * d + carry
                out += (s % 10) * 10 ** i
                carry = s // 10
            if out != c * n:
                ok = False
    check("S6a mult-by-constant is scan-read: LSD transducer, carry < c states (c = 3, 7, base 10, n < 4000)", ok)


def s6b():
    ok = True
    for x in range(1, 200):
        for y in range(1, 200):
            vx, vy = expvec(x, [2, 3, 5, 7]), expvec(y, [2, 3, 5, 7])
            if expvec(x * y, [2, 3, 5, 7]) != tuple(a + b for a, b in zip(vx, vy)):
                ok = False
    check("S6b exponent vector: x is digit-wise addition of vectors (x, y < 200, W = {2,3,5,7})", ok)


# ------------------------------- S7: the diagonal (chain through every prime)


def s7a():
    # m | j! for every j >= m, so EVERY m gets a prefix window in the
    # factorial chain. Tested where the prefix truly truncates
    # (m = 2..10, window at U_j <= 7! = 5040, n up to 4x the window).
    U = SCALES["factorial"]
    ok = True
    for m in range(2, 11):
        j = next(j for j in range(len(U)) if U[j] % m == 0)
        for n in range(20000):
            d = greedy(n, U)
            if (n % m == 0) != (prefix_val(d, U, j) % m == 0):
                ok = False
    # the primorial chain reads exactly the squarefree m: 4 divides no
    # primorial, 6 | U_2 = 6 (m | p_j# iff m squarefree over its primes)
    P = SCALES["primorial"]
    prim = all(u % 4 != 0 for u in P) and any(u % 6 == 0 for u in P) \
        and any(u % 30 == 0 for u in P) and all(u % 9 != 0 for u in P)
    # the price: the digit alphabet grows with position
    maxd = [0] * (len(U) - 1)
    for n in range(20000):
        d = greedy(n, U)
        for i in range(len(U) - 1):
            maxd[i] = max(maxd[i], d[i])
    growing = all(a < b for a, b in zip(maxd[:5], maxd[1:6]))
    check("S7a the diagonal: factorial reads EVERY m (m = 2..10, n < 20000), primorial the squarefree m; the alphabet grows", ok and prim and growing)


# ------------------------------- S8: the census assert


def s8():
    # The readability chart as data: per system, the bought columns and
    # what the row PAYS -- a walled query at its stated tier, or the
    # unbounded alphabet (grades justified by S1-S7 + named contacts;
    # 'mult?/primality?' = expectation tier, no claim minted).
    chart = {
        "base b":       {"buys": ["size", "order", "add(scan)", "m|n"], "pays": ["mult", "primality"]},
        "mixed radix":  {"buys": ["size", "order", "add(scan)", "every m|n"], "pays": ["unbounded alphabet", "mult?/primality?"]},
        "CRT at P":     {"buys": ["add", "mult", "p|n (p in P)"], "pays": ["size", "order", "q|n (q not in P)", "primality"]},
        "Zeckendorf":   {"buys": ["size", "order", "add(Frougny)"], "pays": ["prefix-residues", "mult", "primality?"]},
        "exponent vec": {"buys": ["mult", "m|n", "gcd", "factorization"], "pays": ["add", "size", "order"]},
    }
    print("    the readability chart (census):")
    for k, v in chart.items():
        print("      %-13s buys %-38s pays %s" % (k, ", ".join(v["buys"]), ", ".join(v["pays"])))
    ok = all(v["buys"] and v["pays"] for v in chart.values())
    check("S8 census: every system buys a reading and pays (a walled query or the alphabet)", ok)


# ---------------------------------------------------------------- main

def main():
    print("What a base buys: the two-readings criterion + the readability chart")
    print()
    print("S1 the two-readings criterion")
    s1a(); s1b(); s1c()
    print("S2 greedy buys order")
    s2()
    print("S3 the carry wall")
    s3a(); s3b(); s3c(); s3d(); s3e()
    print("S4 size/order off the archimedean window")
    s4a(); s4b()
    print("S5 divisibility")
    s5a(); s5b(); s5c(); s5d(); s5f(); s5e()
    print("S6 multiplication")
    s6a(); s6b()
    print("S7 the diagonal")
    s7a()
    print("S8 the chart")
    s8()
    print()
    fails = [n for n, c in CHECKS if not c]
    print("%d checks, %d failed" % (len(CHECKS), len(fails)))
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
