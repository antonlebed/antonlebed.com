"""
explore_two_place_universality.py -- TWO PLACES AT TWO RATIOS
(the recovery chart's first row, its last residual; descends from
explore_second_ruler.py, whose model and gadget this script inherits).

THE QUESTION. The second-ruler door: a finite-window ring that only
GROWS (every move multiplies the modulus by a prime; nothing ever
divides), with tests upgraded from presence reads to three-way DEPTH
COMPARISONS sign(alpha*v_p - beta*v_q - gamma) at finitely many fixed
ratios and offsets. At three places (two independent comparisons) the
door is Minsky-complete. At exactly TWO places the linear route is
closed (the cone lemma), and the one-walk gadget -- from home
(u, u), step d until alpha*c = beta*d, then step c home -- realizes
u -> (alpha/beta)*u exactly when beta | u and lands at
ceil(alpha*u/beta) otherwise: an affine miss off the multiplicative
lattice that destroys an exponent encoding. Whether that two-place
cell reaches full universality was left open. THIS SCRIPT ASKS: is the
else wall the GADGET's or the DOOR's?

THE MODEL (verbatim from the parent). State = (control q, c, d) with
c = v_p and d = v_q the depths at two places. MOVES: c += 1, d += 1.
Nothing ever decreases. TESTS, read after every move: the sign of
c - d - gamma_1 and of alpha*c - beta*d - gamma for the finitely many
offsets the machine was built with -- two ratios, 1:1 and alpha:beta,
with gcd(alpha, beta) = 1 and alpha > beta >= 1. A test reads a SIGN
and nothing else; "the form fires" means it reads exactly zero. The
control is a finite automaton over these sign vectors. The register
of the FRACTRAN reading is the home value u, where c = d = u.

THE HAND ANALYSIS (derived before the engine; the sections verify it).

 1. THE CYCLIC PATTERN DROPS THE FORM BY A CONSTANT. Let
    F = alpha*c - beta*d. A c-step adds alpha, a d-step subtracts
    beta. A cycle of a c-steps and b d-steps changes F by
    a*alpha - b*beta =: -D. From home u the form starts at
    F_0 = (alpha - beta)*u - gamma, and after K cycles and a prefix
    of the next with a_j c-steps and b_j d-steps it reads
    F_0 - K*D + off_j, off_j = a_j*alpha - b_j*beta. It fires when
    F_0 + off_j = K*D for some j, i.e. when off_j = -F_0 (mod D).
    Returning home (c-steps until c = d fires on the 1:1 form) lands
    at u' = u + K*b + b_j = rho*u + s, with MULTIPLIER
    rho = 1 + b*(alpha - beta)/D = alpha*(b - a)/D and an offset s
    that depends only on the firing position (K enters linearly and
    cancels). So every landing is affine on each residue class of
    F_0 mod D: the realizable one-round dynamics at grade (D) is a
    generalized-Collatz family, multiplier rho per instruction.

 2. THE READ PATTERN HAS NO MISS. Take b - a = D, i.e. b*(beta - 1) =
    a*(alpha - 1): a = (beta - 1)*k, b = (alpha - 1)*k, D = k*(alpha -
    beta), and rho = alpha exactly. Order the cycle as k repetitions
    of c^(beta-1) d^(alpha-1). Inside one repetition the d-steps visit
    (beta - 1)*alpha - i*beta for i = 1..alpha-1, which modulo
    (alpha - beta) are alpha*(beta - 1 - i): alpha - 1 consecutive
    multiples of alpha, and gcd(alpha, alpha - beta) = gcd(alpha,
    beta) = 1, so they cover EVERY residue mod (alpha - beta). The k
    repetitions shift by -(alpha - beta) each, so within one cycle
    the offsets cover every residue mod D. Hence for every u the form
    fires -- there is no miss -- and the landing is alpha*u + s(r)
    with r = u mod k read off the firing position. The only cost of
    reading u mod k is a factor alpha: a JUNK multiplier, harmless to
    any exponent encoding that avoids the primes of alpha.

 3. EVERY RATIONAL MULTIPLIER FROM alpha - beta + 1 UP IS REALIZED
    WITHOUT A MISS. rho = alpha*(b - a)/(b*beta - a*alpha) = p/q is
    solved by the block c^a d^b with a = p*beta - q*alpha >= 0 and
    b = alpha*(p - q), D = alpha*q*(alpha - beta), whenever p/q >=
    alpha/beta. Its d-steps visit a*alpha - i*beta for i = 1..b:
    b consecutive multiples of beta modulo D, and gcd(beta, D) =
    gcd(beta, q) = 1 when q is coprime to beta, so they cover EVERY
    residue mod D as soon as b >= D, i.e. p - q >= q*(alpha - beta),
    i.e. p/q >= alpha - beta + 1 (which is >= alpha/beta). From that
    threshold the block fires for every u; below it, coverage of the
    classes q | u is the block's luck and not a law. On the class
    q | u the landing (p/q)*u + s has s an integer, and s is brought
    to ZERO by the control: raising gamma by D fires one cycle earlier
    and lowers the landing by b, extra d-steps before the home leg
    raise it by one each, and both are finite tables indexed by the
    firing substep, read at a DETECTOR offset (the largest gamma,
    which fires first) before the control chooses which offset's zero
    to wait for. So u -> (p/q)*u EXACTLY on q | u, the residue known.

 4. THEREFORE GRADE (D) IS UNIVERSAL. A FRACTRAN program (Conway) is a
    list of fractions p_i/q_i; a step multiplies n by the first
    fraction whose denominator divides n and halts when none does;
    FRACTRAN is Turing-complete (Conway 1987, cited, not run). Take a
    program over primes coprime to alpha*beta (relabelling is free)
    and pad every fraction by a power of a junk prime J coprime to the
    program and to beta (a prime factor of alpha serves) until it is at
    least alpha - beta + 1: the padding changes no
    divisibility test, so the padded program's state is J^E times the
    original's at every step, halting together. The two-place machine
    runs it: for each fraction in order, READ u mod q_i by item 2
    (landing alpha*u, junk absorbed), and if q_i | u MULTIPLY by the
    padded fraction by item 3 (exact); if no fraction applies, halt.
    Stripping the junk prime recovers the FRACTRAN state exactly.

PREDICTIONS, FROZEN. P1: the one-walk gadget misses at every odd u for
3:2 (the else wall reproduces -- the positive control). P2: the read
pattern of item 2 fires for EVERY u in 1..300 at every (alpha, beta) in
{(2,1), (3,2), (5,2), (5,3), (7,3)} and every k in 1..12, landing at
alpha*u + s with s taking ONE value per class of u mod k, and the firing
position determining u mod k. P3: for 3:2 and every p/q in a list of
rationals >= 3/2, the compiled instruction lands at (p/q)*u exactly on
every multiple of q in range. P4: two FRACTRAN programs -- the adder
(a, b) -> a + b and Conway's multiplier (a, b) -> a*b, relabelled onto
primes >= 5 -- run on the two-place machine at 3:2 step-exact against a
reference interpreter, the junk stripped. KILLS, as prints: a read
pattern that MISSES at some u; an offset taking two values on one
class; a compiled multiplier landing off (p/q)*u; a simulated trace
departing from the reference. THE FAST WALKER: a walk from home u takes
about (alpha - beta)*u*(a + b)/D moves, so the FRACTRAN sections jump
whole cycles in closed form (item 1's K) and step only the final
partial cycle; the closed form is checked against the literal
step-by-step walk at every u <= 300 first, and the literal walk is the
one whose control reads nothing but signs.

FINDINGS (the run's prints; tiers as the charter names them).

 F1. THE ELSE WALL IS THE GADGET'S (positive control, P1 held): the
     one-walk pattern at 3:2 fires iff u is even and misses at all 150
     odd u in 1..300. The wall the record described is real for that
     pattern and for no other reason.

 F2. THE READ PATTERN NEVER MISSES (rule, proved in item 2, verified
     at five ratios; P2 held whole): at (2,1), (3,2), (5,2), (5,3),
     (7,3), every k in 1..12 and every u in 1..300 the pattern
     (c^(beta-1) d^(alpha-1))^k fires, the closed-form cycle count
     agrees with the literal move-by-move walk at every u, the
     landing is alpha*u + s with ONE s per class of u mod k, and the
     firing substep reads u mod k. A residue read costs a factor
     alpha and nothing else.

 F3. THE EXACT MULTIPLIER'S THRESHOLD IS alpha - beta + 1, NOT
     alpha/beta (P3 as frozen KILLED below it and held above it). The
     block c^a d^b, a = p*beta - q*alpha, b = alpha*(p - q), fires at
     every u and lands at (p/q)*u exactly on q | u for every listed
     ratio at or above 2 with q coprime to 6 -- x2, x4, x11/5, x21/5,
     x17/5, x33/7, x25/7, x23/11, from u_min over 40 multiples, the
     literal sign-reading control agreeing at the first 8 -- and the
     item-3 derivation says why: the d-steps are b consecutive
     multiples of beta modulo D = 3q, all residues iff b >= D. Below
     the threshold the needed classes are covered by luck: x3/2,
     x5/3, x7/4, x9/5 compile and land exactly, x11/7 does not
     (class 14 mod 21 never fires). The first freeze had the
     threshold at alpha/beta; the kill at x11/7 found the gap, and
     the padding absorbs it at no cost.

 F4. TWO PLACES AT TWO RATIOS ARE UNIVERSAL (rule, proved in item 4
     on Conway's cited theorem; the compile verified step-exact; P4
     held): the adder 5^3 7^2 -> 7^5 in 3 steps and Conway's
     multiplier program relabelled onto {5, 7, 11, 13, 17, 19},
     5^2 7^3 -> 11^6 in 25 steps and 5^3 7^2 -> 11^6 in 26, run on
     the two-place machine at 3:2 with junk prime 3, the trace
     stripped of 3s equal to the reference interpreter's at every
     step and halting with it; the final register has 63 and 64
     decimal digits (every read multiplies by 3). Padded program:
     2717/119, 51/19, 81/17, 63/13, 17/5, 27/7. So the threshold of
     the second-ruler door is the SECOND RATIO at any number of
     windows from two: one comparison slope is one-counter decidable,
     two ratios at two places are Minsky-complete, and the linear
     cone lemma priced a route and not the door.

RUN RECORD. python explore_two_place_universality.py -- CHECKS: 22/22
passed, 4.1 s, pure Python, trivial memory. Sections: S1 the one-walk
control (300 u), S2 the read pattern (5 ratios x 12 k x 300 u, closed
form against literal), S3 thirteen multipliers, S4 three FRACTRAN
runs.

CITED, NOT RUN: Conway 1987 (FRACTRAN universality). Everything else
here asserts.
"""

import sys
from fractions import Fraction
from math import gcd

CHECKS = []


def check(name, ok):
    CHECKS.append((name, ok))
    print(("  ok    " if ok else "  FAIL  ") + name)


# ---------------------------------------------------------------------------
# The pattern and its closed form (item 1).

def read_pattern(alpha, beta, k):
    """k repetitions of c^(beta-1) d^(alpha-1): a = (beta-1)k,
    b = (alpha-1)k, D = k(alpha-beta), multiplier alpha."""
    return ("c" * (beta - 1) + "d" * (alpha - 1)) * k


def mult_pattern(alpha, beta, p, q, k=1):
    """a = k(p beta - q alpha) c-steps then b = a + k p (alpha - beta)
    d-steps: multiplier p/q, D = k q alpha (alpha - beta)."""
    a = k * (p * beta - q * alpha)
    m = k * p * (alpha - beta)
    assert a >= 0 and m > 0
    return "c" * a + "d" * (a + m)


def pattern_data(alpha, beta, pattern):
    a = pattern.count("c")
    b = pattern.count("d")
    D = b * beta - a * alpha
    assert D > 0
    offs = []
    cc = dd = 0
    for ch in pattern:
        if ch == "c":
            cc += 1
        else:
            dd += 1
        offs.append((cc * alpha - dd * beta, cc, dd))
    rho = Fraction(alpha * (b - a), D)
    return a, b, D, offs, rho


def fast_first_zero(u, alpha, beta, pattern, gamma):
    """The first (cycle count, substep j) at which alpha*c - beta*d -
    gamma reads zero along the pattern from home u, in closed form;
    None if it never fires. Returns (cycles, j, c, d)."""
    a, b, D, offs, _ = pattern_data(alpha, beta, pattern)
    F0 = (alpha - beta) * u - gamma
    best = None
    for j, (off, cc, dd) in enumerate(offs):
        num = F0 + off
        if num >= 0 and num % D == 0:
            kc = num // D
            cand = (kc, j)
            if best is None or cand < best:
                best = cand
    if best is None:
        return None
    kc, j = best
    off, cc, dd = offs[j]
    return kc, j, u + kc * a + cc, u + kc * b + dd


def literal_first_zero(u, alpha, beta, pattern, gamma, limit=10 ** 7):
    """The same event, walked move by move with sign reads only."""
    c = d = u
    steps = 0
    while steps < limit:
        for j, ch in enumerate(pattern):
            if ch == "c":
                c += 1
            else:
                d += 1
            steps += 1
            F = alpha * c - beta * d - gamma
            if F == 0:
                return steps, j, c, d
            if F < 0 and steps > len(pattern) * 2 and (
                    alpha * (c + len(pattern)) - beta * d - gamma < 0):
                # a full cycle below zero with no zero: a miss
                return None
    return None


def go_home(c, d):
    """c-steps until c - d fires; returns the home value. The walk is
    d - c moves of one kind and its length is not the question, so it
    is jumped; the literal executor walks it."""
    return max(c, d)


# ---------------------------------------------------------------------------
# The compiled instruction (item 3): a finite table over u mod D.

class Instruction:
    """One round: a detector offset gamma_det (largest, fires first);
    on its firing substep the control reads r = u mod M from a table,
    M = D / gcd(D, alpha - beta) being what a substep can tell apart
    (u and u' fire at the same substep iff (alpha-beta)(u-u') = 0 mod
    D), then waits for offset gamma[r]'s zero, then takes t[r] extra
    d-steps, then walks home. Lands at rho*u exactly on the classes
    it was compiled for; r is what the control learned. Needs
    (alpha-beta)*u >= D*(n_det+1) so the detector's form starts above
    zero: u_min."""

    def __init__(self, alpha, beta, pattern, classes, exact=None):
        """classes: the residues (mod M) the instruction must fire on
        and read; exact: the subset it must land on rho*u exactly
        (default all -- the landing rho*u + s must then have s an
        integer, which on a class with q not dividing u it is not)."""
        self.alpha, self.beta, self.pattern = alpha, beta, pattern
        a, b, D, offs, rho = pattern_data(alpha, beta, pattern)
        self.a, self.b, self.D, self.offs, self.rho = a, b, D, offs, rho
        M = D // gcd(D, alpha - beta)
        self.mod = M
        self.classes = sorted(set(x % M for x in classes))
        exact = self.classes if exact is None else sorted(
            set(x % M for x in exact))
        # calibrate on gamma = 0: firing substep and landing offset per class
        self.r_of_sub = {}
        self.n_of_r = {}
        self.t_of_r = {}
        for r in self.classes:
            seen = set()
            for u in range(r + D * 40, r + D * 40 + 3 * D, M):
                z = fast_first_zero(u, alpha, beta, pattern, 0)
                if z is None:
                    raise ValueError(f"class {r} mod {M} never fires")
                kc, j, c, d = z
                L0 = go_home(c, d)
                s0 = L0 - rho * u
                seen.add((j, s0))
            if len(seen) != 1:
                raise ValueError(f"class {r} mod {M} not affine: {seen}")
            (j, s0), = seen
            if j in self.r_of_sub and self.r_of_sub[j] != r:
                raise ValueError(f"substep {j} fires for two classes")
            self.r_of_sub[j] = r
            if r not in exact:
                self.n_of_r[r] = 0
                self.t_of_r[r] = 0
                continue
            if s0.denominator != 1:
                raise ValueError(f"class {r}: fractional offset {s0}")
            s0 = int(s0)
            n = max(0, -(-s0 // b))          # ceil(s0 / b) when s0 > 0
            self.n_of_r[r] = n
            self.t_of_r[r] = b * n - s0      # >= 0
            assert self.t_of_r[r] >= 0
        self.n_det = max(self.n_of_r.values(), default=0) + 1
        self.gamma_det = D * self.n_det
        self.u_min = -(-(D * (self.n_det + 1)) // (alpha - beta))

    def run(self, u):
        """Execute on u in closed form. Returns (landing, r)."""
        if u < self.u_min:
            raise ValueError(f"u={u} below u_min={self.u_min}")
        z = fast_first_zero(u, self.alpha, self.beta, self.pattern,
                            self.gamma_det)
        if z is None:
            raise ValueError("detector never fires")
        kc_det, j, _, _ = z
        r = self.r_of_sub[j]
        gamma = self.D * self.n_of_r[r]
        kc, j2, c, d = fast_first_zero(u, self.alpha, self.beta,
                                      self.pattern, gamma)
        assert (kc, j2) >= (kc_det, j), "the detector must fire first"
        d += self.t_of_r[r]
        return go_home(c, d), r

    def run_literal(self, u):
        """Execute on u move by move: the control reads only the signs
        of c - d and of alpha*c - beta*d - gamma over its offset set."""
        alpha, beta, pattern = self.alpha, self.beta, self.pattern
        offsets = sorted({self.gamma_det} |
                         {self.D * n for n in self.n_of_r.values()},
                         reverse=True)
        c = d = u
        r = None
        target = None
        done = False
        while not done:
            for j, ch in enumerate(pattern):
                if ch == "c":
                    c += 1
                else:
                    d += 1
                signs = {g: (alpha * c - beta * d - g > 0)
                         - (alpha * c - beta * d - g < 0) for g in offsets}
                if r is None and signs[self.gamma_det] == 0:
                    r = self.r_of_sub[j]
                    target = self.D * self.n_of_r[r]
                if r is not None and signs[target] == 0:
                    done = True
                    break
        d += self.t_of_r[r]
        while (c - d) < 0:
            c += 1
        return c, r


# ---------------------------------------------------------------------------
# FRACTRAN (item 4).

def fractran_run(fracs, n, max_steps=10 ** 5):
    trace = [n]
    for _ in range(max_steps):
        for f in fracs:
            if n % f.denominator == 0:
                n = n * f.numerator // f.denominator
                trace.append(n)
                break
        else:
            return trace, True
    return trace, False


def strip(n, J):
    while n % J == 0:
        n //= J
    return n


class TwoPlaceFractran:
    """The compile of item 4 at ratio alpha:beta with junk prime J."""

    def __init__(self, fracs, alpha, beta, J):
        self.alpha, self.beta, self.J = alpha, beta, J
        for f in fracs:
            assert gcd(f.numerator * f.denominator, J) == 1
            assert gcd(f.numerator * f.denominator, alpha * beta) == 1
        self.padded = []
        for f in fracs:
            g = f
            while g < alpha - beta + 1:
                g *= J
            self.padded.append(g)
        self.reads = []
        self.mults = []
        for f, g in zip(fracs, self.padded):
            q = f.denominator
            self.reads.append(Instruction(alpha, beta, read_pattern(
                alpha, beta, q), range(q * (alpha - beta))))
            p, qq = g.numerator, g.denominator
            pat = mult_pattern(alpha, beta, p, qq)
            D = qq * alpha * (alpha - beta)
            ins = Instruction(alpha, beta, pat, range(D), range(0, D, qq))
            self.mults.append(ins)

    def step(self, u):
        """One FRACTRAN step on the two-place machine: reads in program
        order, the first divisible one multiplied. Returns (u', halted)."""
        for rd, ml, f in zip(self.reads, self.mults, self.padded):
            q = f.denominator
            L, r = rd.run(u)
            assert L == self.alpha * u
            u = L
            if r % q == 0:
                L2, _ = ml.run(u)
                assert L2 == f * u
                return L2, False
        return u, True


# ---------------------------------------------------------------------------

def s1_positive_control():
    print("S1. Positive control: the one-walk gadget's else wall at 3:2")
    misses = 0
    for u in range(1, 301):
        z = literal_first_zero(u, 3, 2, "d", 0)
        if u % 2 == 0:
            check_ok = z is not None and z[3] == 3 * u // 2
        else:
            check_ok = z is None
        misses += (z is None)
        if not check_ok:
            check(f"one-walk gadget at u={u}", False)
    check(f"one-walk gadget 3:2 on 1..300: fires iff u even, "
          f"{misses} misses (every odd u)", misses == 150)
    print()


def s2_read_pattern():
    print("S2. The read pattern fires for every u (item 2)")
    for alpha, beta in [(2, 1), (3, 2), (5, 2), (5, 3), (7, 3)]:
        worst = 0
        for k in range(1, 13):
            pat = read_pattern(alpha, beta, k)
            a, b, D, offs, rho = pattern_data(alpha, beta, pat)
            assert rho == alpha and b - a == D
            offsets_per_class = {}
            sub_to_class = {}
            miss = 0
            for u in range(1, 301):
                zf = fast_first_zero(u, alpha, beta, pat, 0)
                zl = literal_first_zero(u, alpha, beta, pat, 0)
                if zf is None or zl is None:
                    miss += 1
                    continue
                assert zf[2:] == zl[2:], "closed form vs literal walk"
                assert zf[1] == zl[1]
                L = go_home(*zf[2:])
                s = L - alpha * u
                offsets_per_class.setdefault(u % k, set()).add(s)
                sub_to_class.setdefault(zf[1], set()).add(u % k)
            one = all(len(v) == 1 for v in offsets_per_class.values())
            fn = all(len(v) == 1 for v in sub_to_class.values())
            worst = max(worst, miss)
            if not (miss == 0 and one and fn):
                check(f"{alpha}:{beta} k={k}: miss={miss} one-offset="
                      f"{one} substep->residue={fn}", False)
        check(f"{alpha}:{beta}, k = 1..12, u = 1..300: no miss, one "
              f"offset per class mod k, firing substep reads u mod k, "
              f"landing alpha*u + s (closed form = literal walk)",
              worst == 0)
    print()


def s3_multipliers():
    print("S3. Exact rational multipliers at 3:2 (item 3)")
    # above the threshold: denominators coprime to 6, the theorem's case;
    # below it: whatever compiles is the block's luck, reported as such
    ratios = [Fraction(*t) for t in [(2, 1), (4, 1), (11, 5), (21, 5),
                                     (17, 5), (33, 7), (25, 7), (23, 11),
                                     (3, 2), (5, 3), (7, 4), (9, 5),
                                     (11, 7)]]
    for pq in ratios:
        p, q = pq.numerator, pq.denominator
        above = pq >= 2      # alpha - beta + 1 at 3:2
        pat = mult_pattern(3, 2, p, q)
        a, b, D, offs, rho = pattern_data(3, 2, pat)
        assert rho == pq
        try:
            ins = Instruction(3, 2, pat, range(D) if above
                              else range(0, D, q), range(0, D, q))
        except ValueError as e:
            check(f"x{pq} ({'at or above' if above else 'below'} the "
                  f"threshold 2): a={a} b={b} D={D}, does not compile "
                  f"({e})", not above)
            continue
        bad = 0
        lit = 0
        u0 = -(-ins.u_min // q) * q
        for i, u in enumerate(range(u0, u0 + 40 * q + 1, q)):
            L, r = ins.run(u)
            if L != pq * u or r != u % ins.mod:
                bad += 1
            if i < 8:
                L2, r2 = ins.run_literal(u)
                lit += (L2, r2) != (L, r)
        fires_all = above and all(
            fast_first_zero(u, 3, 2, pat, 0) is not None
            for u in range(ins.u_min, ins.u_min + 3 * D))
        check(f"x{pq} ({'at or above' if above else 'below'} the "
              f"threshold 2): a={a} b={b} D={D}, lands at ({pq})u "
              f"exactly on q|u from u_min={ins.u_min} over 40 multiples "
              f"({bad} off), literal control agrees at the first 8 "
              f"({lit} off)" + (", fires at EVERY u" if fires_all else ""),
              bad == 0 and lit == 0 and (fires_all or not above))
    print()


def s4_fractran():
    print("S4. FRACTRAN on two places at 3:2, junk prime 3 (item 4)")
    # the adder: 5^a 7^b -> 7^(a+b)
    adder = [Fraction(7, 5)]
    # Conway's multiplier 2^a 3^b -> 5^(ab), relabelled
    # 2->5, 3->7, 5->11, 7->13, 11->17, 13->19
    mult = [Fraction(11 * 13 * 19, 7 * 17), Fraction(17, 19),
            Fraction(1, 17), Fraction(7, 13), Fraction(17, 5),
            Fraction(1, 7)]
    for name, prog, start, want in [
            ("adder", adder, 5 ** 3 * 7 ** 2, 7 ** 5),
            ("multiplier 2x3", mult, 5 ** 2 * 7 ** 3, 11 ** 6),
            ("multiplier 3x2", mult, 5 ** 3 * 7 ** 2, 11 ** 6)]:
        machine = TwoPlaceFractran(prog, 3, 2, 3)
        ref, halted = fractran_run(prog, start)
        u = start
        sim = [u]
        ok = True
        for _ in range(len(ref) - 1):
            u, h = machine.step(u)
            assert not h
            sim.append(u)
        u2, h = machine.step(u)
        ok = h and all(strip(x, 3) == y for x, y in zip(sim, ref)) \
            and strip(u2, 3) == ref[-1] == want
        check(f"{name}: {len(ref) - 1} steps, reference halts at "
              f"{want} = {ref[-1]}, two-place trace stripped of 3s "
              f"matches at every step and halts with it "
              f"(final u has {len(str(u2))} digits)", ok)
        print(f"  padded fractions: "
              f"{[str(g) for g in machine.padded]}")
    print()


def main():
    s1_positive_control()
    s2_read_pattern()
    s3_multipliers()
    s4_fractran()
    n_ok = sum(1 for _, ok in CHECKS if ok)
    print(f"CHECKS: {n_ok}/{len(CHECKS)} passed")
    return 0 if n_ok == len(CHECKS) else 1


if __name__ == "__main__":
    sys.exit(main())
