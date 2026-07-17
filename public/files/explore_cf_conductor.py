"""The conductor law: the continued-fraction reading delay reads unit
indices of quadratic orders.

THE QUESTION
------------
explore_cf_window.py established the rate law for integer Mobius maps
on continued-fraction streams: the digit-delay of x -> M(x) is the
signed accumulated rate mismatch, and the measured digit-rate ratios
r_out/r_in sat at INTEGERS across all nine scanned quadratic pairs
(3, 2, 3 at phi; 1, 2, 1 at sqrt2; 2, 3, 2 at sqrt3). Why integers,
and which integers?

THE CONDUCTOR LAW (the hypothesis under test). For a quadratic
irrational y with eventually periodic CF of tail period ell(y), the
period matrix's dominant eigenvalue eta(y) is the fundamental
automorph of the lattice L_y = Z + Zy: the smallest unit > 1 of the
multiplier ring O'(y) = {lam : lam L_y <= L_y}, which is the order of
discriminant b^2 - 4ac for y's primitive integer equation. Writing
eps for the fundamental unit of the maximal order (GL convention:
norm +-1 allowed, the CF period matrix lives in GL(2,Z)) and
i(y) = the unit index [O_K^x : O'(y)^x] (mod +-1), we have
eta(y) = eps^i(y), the convergent denominators grow like
q_t ~ eta^(t/ell), and the scale-per-digit rate is

    r(y) = 2 ln eta(y) / ell(y) = 2 i(y) R_K / ell(y),

R_K = ln eps the regulator. So for any integer Mobius map between
quadratics of one field the measured digit-rate ratio should be

    r_out/r_in = (i_out / i_in) * (ell_in / ell_out),

and the reading DELAY of a det != +-1 map reads the unit index of a
conductor order: the window is an instrument that measures orders.

Classical background imported (not re-proved here): the ring class
number formula h(O_f) * [O_K^x : O_f^x] = h_K * f * prod_{p|f}
(1 - (D_K/p)/p). Since Pic(O_f) surjects onto Pic(O_K), the index i
divides the CEILING f * prod_{p|f}(1 - (D_K/p)/p), and the quotient
ceiling/i equals h(O_f)/h_K — where the ceiling is not attained, the
deficit is exactly the ring class number growth. The law must
therefore read the realized INDEX, never the ceiling formula; the
test battery contains two witnesses that separate them.

THE DESIGN
----------
Machinery, three INDEPENDENT computations of the rate ratio per pair:
  (1) DYNAMIC — the interval reader of explore_cf_window.py emits
      output quotients from input cylinders; measured ratio =
      q_rate(emitted)/q_rate(input) at depth 150 (a reader that
      knows no algebra). Convention note: q_rate measures q-growth
      ln(q_t)/t -> ln(eta)/ell = i R_K/ell, HALF the cell-scale
      rate 2 i R_K/ell (cell size ~ 1/q^2); every ratio is
      convention-free, the factor 2 cancels.
  (2) SPECTRAL — exact surd CF (integer P,Q,D states) finds the tail
      period ell and the period matrix; its eigenvalue eta is
      computed exactly as an element of Q(sqrt d).
  (3) ALGEBRAIC — the conductor f from y's primitive equation
      discriminant f^2 D_K, the fundamental unit eps from the CF of
      omega, the index i = min{i : eps^i in O_f}.
The identity eta == eps^i is asserted EXACTLY (Fraction arithmetic)
at every scanned pair — the spectral and algebraic sides must agree
before any dynamic verdict is read.

The hand derivation was attacked on paper first; all nine
already-measured pairs were recovered by hand (i_in = 1 throughout:
Z+Z phi, Z[sqrt2], Z[sqrt3] all maximal):
  (2x,phi) i=3 ell 1->1: 3.  (3x,phi) i=4 ell 1->2: 2.
  (x/2,phi) O' = Z+2phi Z, i=3, ell 1->1: 3.
  (2x,sqrt2) i=2 ell 1->2: 1 (the Pell delay-0 print).
  (3x,sqrt2) i=4 ell 1->2: 2.  (x/2,sqrt2) O' = Z[sqrt2] WHOLE,
  i=1 ell 1->1: 1 — ratio 1 by a DIFFERENT mechanism than (2x,sqrt2).
  (2x,sqrt3) i=2 ell 2->2: 2.  (3x,sqrt3) i=3 ell 2->2: 3.
  (x/2,sqrt3) i=2 ell 2->2: 2.

PREDICTIONS, fixed before any engine ran (the sight-unseen battery
was NOT pre-measured; CF periods below were hand-computed on paper):
  P-A (E1, recovery): the law reproduces all nine measured ratios
      within 6%, and eta == eps^i exactly at every pair.
  P-B (E2, sight-unseen): (5x, phi) ratio 5 (i=5, ell 1->1, tail
      (11), eta = phi^5); (7x, phi) ratio 4 (i=8, ell 1->2, tail
      (3,15), eta = phi^8); (5x, sqrt2) ratio 3 (i=3, ell 1->1,
      sqrt50 = [7;(14)], eta = (1+sqrt2)^3); (8x, phi) ratio 3
      (i=6, ell 1->2, tail (1,16), eta = phi^6).
  P-C (E2, the index vs the formula): at (5x, sqrt2) the ceiling is
      6 but i = 3; at (8x, phi) the ceiling is 12 but i = 6. The
      measured ratios follow the INDEX (3 and 3, not 6 and 6), and
      ceiling/i = 2 = h(O_f)/h_K at both (the class-number deficit,
      via the imported formula). At the other slate rows the ceiling
      is attained (f=2,3,5,7 over sqrt5: 3,4,5,8; f=2,3 over sqrt2:
      2,4; f=2,3 over sqrt3: 2,3).
  P-D (E3, necessity scan): over the family x_a = (a+sqrt(a^2+4))/2
      = [(a)] (a = 1..10) and maps x -> nx (n = 2,3,5,6), the
      spectral identity eta = eps^i holds exactly at every row
      including i_in > 1 rows (nonsquarefree a^2+4), and EVERY
      scanned n owns at least one rate-mismatched witness
      (predicted ratio != 1) — the necessity evidence; matched
      witnesses also occur (a = 2 at n = 2: the Pell coincidence),
      so mismatch is orbit-local, never a property of n alone.
      Dynamic spot-check: the first mismatched (n, a) row per n
      measures within 6% of the algebraic prediction.
  P-E (E4, the reduction lemma live): every primitive integer Mobius
      map M with |det M| = n is U diag(1,n) V (Smith normal form)
      with U, V unimodular, and unimodular maps read at bounded
      delay both ways, so M's readability at y equals the scaling's
      readability at V(y) and witnesses TRANSPORT. The composed
      det-6 map M = U diag(6,1) V = [[12,-11],[6,-5]] must stall
      linearly at the transported witness y* = x*+1 (x* = the first
      mismatched n=6 witness from E3) with the transported rate
      ratio, while the composed det-2 map [[4,-3],[2,-1]] reads the
      transported Pell witness 2+sqrt2 at bounded delay.

Positive control: the rig must reproduce the (2x, phi) measured
ratio ~3.01 and the (2x, sqrt2) ratio ~1 of explore_cf_window.py
before any new verdict is read. Harness: check() exits nonzero on
any failure (the failure path of this pattern has been verified to
fire in explore_cf_window.py's development).

Necessity in general (every det != +-1 map owns a mismatched
witness) entered the run CONJECTURED: E3+E4 prove the reduction to
scalings and exhibit witnesses at every scanned n; the open core was
that every n > 1 owns one.

THE SECOND WAVE: THE NECESSITY PROOF (designed after E1-E4 printed;
E3's table showed x_1 = phi mismatched at every scanned n, and the
reason generalizes to a proof that phi is a UNIVERSAL witness):
  (1) i(n) >= 2 for n >= 2: any multiplier maps 1 into the lattice,
      so the multiplier ring O' sits INSIDE Z + Z n phi; phi in
      Z + Z n phi would need phi = u + v n phi with integer u, v,
      so vn = 1 — impossible. Hence phi not in O' and i(n) != 1.
  (2) THE FLOOR-RIGIDITY LEMMA: over CF digit words of length ell
      (all digits >= 1) the period matrix's dominant eigenvalue is
      >= phi^ell, with equality IFF the word is all-1s. Proof: for
      fixed ell the determinant is (-1)^ell, so the eigenvalue
      (tr + sqrt(tr^2 - 4 det))/2 is strictly increasing in the
      trace; the trace is strictly increasing in every digit (its
      digit-derivative is a partial product's top-left entry, >= 1);
      the all-1s word has trace = the Lucas number L_ell and
      eigenvalue phi^ell.
  (3) Suppose the rate ratio at (nx, phi) were 1: ell_in = 1 and
      i_in = 1 give i(n) = ell(n phi); the spectral identity gives
      eta(n phi) = eps^i = phi^i = phi^ell; by (2) the period word
      is all-1s; the all-1s tail's periodic point is phi (the unique
      positive fixed point of [[1,1],[1,0]]), so n phi is a
      GL(2,Z)-word image of phi, its lattice homothetic to Z+Z phi,
      its multiplier order MAXIMAL (homothety preserves the
      multiplier ring) — i(n) = 1, contradicting (1).
      So i(n) != ell(n phi) and the ratio != 1 at EVERY n >= 2.
  (4) Rate forcing (the reading lemma's scale account, both signs):
      ratio > 1 makes the determined-output count e(t) ~ t/ratio,
      delay linear positive; ratio < 1 pins ~t/ratio digits from the
      image interval, delay linear negative — |delay| unbounded
      either way (boundary hugs are finite for Mobius maps: rational
      preimages).
  (5) Smith transport (E4): every primitive integer Mobius map with
      |det| = n >= 2 owns the transported witness V^-1(phi).
  The lean point, flagged: step (4) is the rate law's accounting —
  scale-forcing on quadratic orbits with the boundary collapse;
  steps (1)-(3) are algebra on top of two classical imports (Serret;
  the automorph identity). (Audit note, post-run: a SECOND lean was
  later named for the Smith extension only — the sign-crossing
  unimodular legs; see the tier summary.)

E5 PREDICTIONS, fixed before E5 ran:
  P-F (a) floor rigidity exhaustively at ell <= 6, digits <= 4:
      trace > L_ell at every non-all-1s word, = L_ell at all-1s;
      (b) the Fibonacci apparition rank i(n) >= 3 for every
      n = 2..2000 (F_1 = F_2 = 1);
      (c) i(n) != ell(n phi) for EVERY n = 2..40 — the proof's
      numerical consequence, sight-unseen beyond the n <= 6 scan
      (for n phi the conductor is exactly n: disc(y^2 - ny - n^2) =
      5 n^2).

FINDINGS (entered after the run; ALL ENGINES PASS)
--------------------------------------------------
P1  THE CONDUCTOR LAW CONFIRMED AT RECOVERY. All nine measured pairs
    reproduced: predictions 3,2,3 / 1,2,1 / 2,3,2 with dynamic
    measurements 3.0112, 1.9828, 2.9609 / 0.9947, 2.0020, 0.9960 /
    1.9923, 2.9959, 1.9796 (worst deviation ~1%), and eta = eps^i
    EXACT (Fraction identity) at every input and output lattice.
    Ratio 1 twice by different mechanisms: (2x, sqrt2) via i=2,
    ell 1->2; (x/2, sqrt2) via i=1 (the det-2 map x/2 lands on the
    MAXIMAL order Z[sqrt2]).
P2  ALL FOUR SIGHT-UNSEEN RATIOS LAND, AND THE INDEX BEATS THE
    FORMULA. (5x, phi) 5.0219 vs 5; (7x, phi) 3.9714 vs 4;
    (5x, sqrt2) 3.0035 vs 3; (8x, phi) 2.9521 vs 3. At the two
    designed separating witnesses the ceiling is NOT attained —
    (5x, sqrt2): ceiling 6, index 3, measured 3; (8x, phi): ceiling
    12, index 6, measured 3 — the law reads the realized INDEX,
    never the formula; the deficit ceiling/i = 2 = h(O_f)/h_K at
    both (imported ring class number formula). The reading delay is
    an instrument: the stall slope of x -> nx at a quadratic stream
    measures the unit index of a conductor order.
P3  NECESSITY EVIDENCE + TWO OFF-PREDICTION STRUCTURES. Every
    scanned n in {2,3,5,6} owns mismatched witnesses; matched
    witnesses also occur at every n (mismatch is orbit-local, never
    a property of the map alone; the Pell coincidence n=2, a=2
    confirmed). OFF-SLATE: (a) FRACTIONAL ratios BELOW 1 — 3/5 at
    (2x, a=3,5,7,9), 1/2 at (3x, a=5,7,8,10), down to 5/13 at
    (5x, a=9): the det != +-1 stall is TWO-SIDED, the reader can
    emit ahead linearly (negative linear delay), so "stall" means
    |rate mismatch|, either sign. (b) INPUT-CONDUCTOR COMPENSATION,
    a third ratio-1 mechanism: at (5x, a=4) the input x_4 = 2+sqrt5
    has f_in = 2, i_in = 3, and (i_out/i_in)(ell_in/ell_out) =
    (15/3)(1/5) = 1 — MATCHED through cancellation of both sides'
    conductors; likewise (2x, a=4) and (6x, a=4). eta = eps^i exact
    at all 40 rows including every i_in > 1 row. Dynamic
    spot-checks: 3.0140/3, 1.9779/2, 5.0274/5, 1.9534/2.
P4  SMITH TRANSPORT CONFIRMED. M6 = U diag(6,1) V = (12,-11,6,-5),
    det 6, at the transported witness phi+1: measured ratio 1.9985
    vs transported prediction 2, delay 28 -> 73 over depths 60 ->
    150 (slope 0.5 = 1 - 1/2, the rate account); the det-2
    composite (4,-3,2,-1) reads the transported Pell witness
    2+sqrt2 at delay -2, non-growing. Witnesses transport through
    unimodular factors as the reduction lemma demands.
P5  THE NECESSITY PROOF STANDS. All three checkable parts hold:
    floor rigidity exhaustive (trace > L_ell at every non-all-1s
    word, = L_ell at all-1s; 5460 words, ell <= 6, digits <= 4);
    apparition rank i(n) >= 3 for every n = 2..2000; and
    i(n) != ell(n phi) at every n = 2..40 — sample rows (2,3,1),
    (3,4,2), (4,6,2), (5,5,1), (6,12,6), (7,8,2), (8,6,2),
    (9,12,6). With steps (1)-(5) of the second-wave design, the
    unit gate's NECESSITY for the scaling family is proved with phi
    as the universal witness, and via Smith transport every
    primitive integer Mobius map with det != +-1 owns a mismatched
    witness.

Tier summary: THE CONDUCTOR LAW — r(y) = 2 i(y) R_K / ell(y), so
r_out/r_in = (i_out/i_in)(ell_in/ell_out) — is a RULE at the
scanned scopes: 17 dynamically measured pairs (9 recovery + 4
sight-unseen + 4 spot-checks, all within 6%, plus the E4 composite)
and the exact spectral-algebraic identity eta = eps^i at all 53
scanned pairs (asserted on both the input and output lattice of
each). The identity "period matrix eigenvalue = fundamental
automorph of the multiplier order" is classical (imported; the
engine asserts it exactly as its consistency guard). The
ceiling-deficit reading (ceiling/i = h(O_f)/h_K) is the imported
ring class number formula; the engine verifies divisibility and the
separation. The reduction lemma (readability transports through
unimodular factors; necessity reduces to scalings) is classical
Smith + Serret machinery verified live at the scanned composites.
NECESSITY of the unit gate is now a RULE, proved algebraically for
every scaling x -> nx (phi the universal witness: floor rigidity +
apparition rank, steps (1)-(3) all-n algebra) and extended to every
primitive integer Mobius map by the reduction lemma. TWO lean
points, named: the rate-forcing step (4) — the rate law's scale
accounting on quadratic orbits, measured throughout this corpus,
not separately proved in general — and, for the Smith extension
only, the unimodular legs: bounded delay is a rule at
nonnegative-entry words, resting on the classical negation rewrites
for sign-crossing factors (the E4 composite, with a negative-entry
factor, is the one live instance). The scaling family's necessity
leans on (4) alone. (Settled since: both lean points are CLOSED at
this proof's scope by explore_cf_flow.py — rate forcing is proved
at quadratic streams, and the Smith transport needs unimodular maps
only at quadratic streams, where GL(2,Z)-equivalence forces ratio 1
and bounded delay; the word-factorization lean survives only for
general non-quadratic streams.)

RUN RECORD: ALL ENGINES PASS, < 0.2 s. E1 nine-pair recovery table
+ two positive controls; E2 four sight-unseen rows with ceilings;
E3 forty-row scan (matched/mismatch verdicts as printed) + four
dynamic spot-checks; E4 transport prints as quoted; E5 floor
rigidity 5460 words + apparition ranks to 2000 + the n = 2..40
inequation. Harness failure path verified to fire: a forced-fail
copy (one expected ratio edited 3 -> 4) exits 1.
"""

from fractions import Fraction
from math import gcd, isqrt, log

from explore_cf_window import WITNESSES, emitted, q_rate


# ------------------------------------------------------------------ #
# exact surd CF: x = (P + sqrt(D)) / Q                                #
# ------------------------------------------------------------------ #

def surd_cf(P, D, Q, cap=2000):
    """Digits + tail period of (P + sqrt(D))/Q, exactly.
    Returns (digits, k, ell): digits[k:k+ell] is the primitive period
    and (Pk, Qk) the state at its start is also returned via closure
    of the recurrence; here we return the periodic point too."""
    if (D - P * P) % Q:
        P, D, Q = P * abs(Q), D * Q * Q, Q * abs(Q)
    s = isqrt(D)
    assert s * s != D, "D must be a nonsquare"
    seen, digits, states = {}, [], []
    while len(digits) < cap:
        key = (P, Q)
        if key in seen:
            k = seen[key]
            return digits[:k], digits[k:], states[k], D
        seen[key] = len(digits)
        states.append((P, Q))
        a = (P + s) // Q if Q > 0 else (P + s + 1) // Q
        digits.append(a)
        P = a * Q - P
        Q = (D - P * P) // Q
    raise AssertionError("period not found within cap")


def period_eigenvalue(period, state, D):
    """The period matrix's dominant eigenvalue as an exact field
    element A + B*sqrt(d0), d0 the squarefree kernel of D: the
    eigenvalue at the fixed point z = (Pk + sqrt(D))/Qk is
    w21*z + w22 for the period word's matrix [[w11,w12],[w21,w22]]."""
    w11, w12, w21, w22 = 1, 0, 0, 1
    for a in period:                 # right-multiply: the word in order
        w11, w12, w21, w22 = a * w11 + w12, w11, a * w21 + w22, w21
    Pk, Qk = state
    d0, t = squarefree_kernel(D)
    A = Fraction(w21 * Pk, Qk) + w22
    B = Fraction(w21 * t, Qk)
    return A, B, d0


def squarefree_kernel(D):
    """D = t^2 * d0 with d0 squarefree; returns (d0, t)."""
    d0, t, m, p = 1, 1, D, 2
    while p * p <= m:
        if m % p == 0:
            e = 0
            while m % p == 0:
                m //= p
                e += 1
            t *= p ** (e // 2)
            if e % 2:
                d0 *= p
        p += 1 if p == 2 else 2
    return d0 * m, t


# ------------------------------------------------------------------ #
# field arithmetic in Q(sqrt d0): elements as (A, B) Fractions       #
# ------------------------------------------------------------------ #

def fmul(x, y, d0):
    return (x[0] * y[0] + x[1] * y[1] * d0, x[0] * y[1] + x[1] * y[0])


def in_order(x, f, d0):
    """Is A + B sqrt(d0) in the order of conductor f (inside O_K)?"""
    A, B = x
    if d0 % 4 == 1:
        b = 2 * B                      # omega = (1 + sqrt d0)/2
        return (A - B).denominator == 1 and b.denominator == 1 \
            and int(b) % f == 0
    return A.denominator == 1 and B.denominator == 1 \
        and int(B) % f == 0


def fundamental_unit(d0):
    """The fundamental unit of O_K (GL convention) from the CF of
    omega, as (A, B)."""
    if d0 % 4 == 1:
        pre, per, state, D = surd_cf(1, d0, 2)
    else:
        pre, per, state, D = surd_cf(0, d0, 1)
    A, B, k = period_eigenvalue(per, state, D)
    assert k == d0
    return A, B


def unit_index(f, d0, eps, bound=500):
    """min{i >= 1 : eps^i in O_f}."""
    x = eps
    for i in range(1, bound + 1):
        if in_order(x, f, d0):
            return i
        x = fmul(x, eps, d0)
    raise AssertionError("unit index exceeds bound")


def kronecker(DK, p):
    if p == 2:
        if DK % 2 == 0:
            return 0
        return 1 if DK % 8 in (1, 7) else -1
    r = pow(DK % p, (p - 1) // 2, p)
    return 0 if r == 0 else (1 if r == 1 else -1)


def ceiling_index(f, DK):
    """f * prod_{p | f} (1 - (DK/p)/p): the classical bound i must
    divide; ceiling/i = h(O_f)/h_K."""
    val, m, p = Fraction(f), f, 2
    while p * p <= m:
        if m % p == 0:
            val *= 1 - Fraction(kronecker(DK, p), p)
            while m % p == 0:
                m //= p
        p += 1 if p == 2 else 2
    if m > 1:
        val *= 1 - Fraction(kronecker(DK, m), m)
    assert val.denominator == 1
    return int(val)


# ------------------------------------------------------------------ #
# the lattice data of a quadratic irrational                          #
# ------------------------------------------------------------------ #

def mobius_surd(mat, P, D, Q):
    """The surd (P2 + sqrt(D2))/Q2 for M((P+sqrt(D))/Q)."""
    ma, mb, mc, md = mat
    F, E = ma * P + mb * Q, mc * P + md * Q
    P2 = F * E - ma * mc * D
    t = Q * (ma * md - mb * mc)
    Q2 = E * E - mc * mc * D
    if t < 0:
        P2, t, Q2 = -P2, -t, -Q2
    g = gcd(gcd(abs(P2), t), abs(Q2))
    return P2 // g, (t // g) ** 2 * D, Q2 // g


def lattice_data(P, D, Q):
    """(f, ell, eta, d0) for y = (P+sqrt(D))/Q: conductor of the
    multiplier ring of Z+Zy, tail period length, the exact period
    eigenvalue, the field kernel."""
    if (D - P * P) % Q:
        P, D, Q = P * abs(Q), D * Q * Q, Q * abs(Q)
    # primitive equation: Q^2 y^2 - 2PQ y + (P^2 - D) = 0
    g = gcd(gcd(Q * Q, 2 * P * Q), abs(P * P - D))
    disc = 4 * Q * Q * D // (g * g)
    d0, _ = squarefree_kernel(D)
    DK = d0 if d0 % 4 == 1 else 4 * d0
    f = isqrt(disc // DK)
    assert f * f * DK == disc
    pre, per, state, D2 = surd_cf(P, D, Q)
    A, B, k = period_eigenvalue(per, state, D2)
    assert k == d0
    return f, len(per), (A, B), d0


def law_row(mat, P, D, Q, eps, d0):
    """One pair's algebraic read: (i_in, ell_in, i_out, ell_out,
    predicted ratio), asserting eta == eps^i exactly on both sides."""
    f_in, ell_in, eta_in, k1 = lattice_data(P, D, Q)
    P2, D2, Q2 = mobius_surd(mat, P, D, Q)
    f_out, ell_out, eta_out, k2 = lattice_data(P2, D2, Q2)
    assert k1 == d0 and k2 == d0
    i_in = unit_index(f_in, d0, eps)
    i_out = unit_index(f_out, d0, eps)
    ok_in = power_equals(eps, i_in, eta_in, d0)
    ok_out = power_equals(eps, i_out, eta_out, d0)
    pred = Fraction(i_out * ell_in, i_in * ell_out)
    return i_in, ell_in, i_out, ell_out, f_out, pred, ok_in and ok_out


def power_equals(eps, i, eta, d0):
    x = (Fraction(1), Fraction(0))
    for _ in range(i):
        x = fmul(x, eps, d0)
    return x == eta


# ------------------------------------------------------------------ #
# harness                                                              #
# ------------------------------------------------------------------ #

FAILS = []


def check(label, ok):
    print(("  PASS  " if ok else "  FAIL  ") + label)
    if not ok:
        FAILS.append(label)


SURDS = {"phi": (1, 5, 2), "sqrt2": (0, 2, 1), "sqrt3": (0, 3, 1)}
MAPS9 = {"2x": (2, 0, 0, 1), "3x": (3, 0, 0, 1), "x/2": (1, 0, 0, 2)}
MEASURED9 = {("2x", "phi"): 3, ("3x", "phi"): 2, ("x/2", "phi"): 3,
             ("2x", "sqrt2"): 1, ("3x", "sqrt2"): 2, ("x/2", "sqrt2"): 1,
             ("2x", "sqrt3"): 2, ("3x", "sqrt3"): 3, ("x/2", "sqrt3"): 2}
EPS_CACHE = {}


def eps_of(d0):
    if d0 not in EPS_CACHE:
        EPS_CACHE[d0] = fundamental_unit(d0)
    return EPS_CACHE[d0]


def dynamic_ratio(mat, quots, n=150):
    out = emitted(mat, quots, n)
    return q_rate(out) / q_rate(quots[: n + 1]), len(out)


# ------------------------------------------------------------------ #
# E1: recovery of the nine measured pairs                             #
# ------------------------------------------------------------------ #

def e1():
    print("E1 RECOVERY (the law vs the nine measured ratios)")
    all_law, all_dyn = True, True
    for wname, (P, D, Q) in SURDS.items():
        d0, _ = squarefree_kernel(D)
        eps = eps_of(d0)
        for mname, mat in MAPS9.items():
            i_in, l_in, i_out, l_out, f, pred, spec = \
                law_row(mat, P, D, Q, eps, d0)
            meas, _ = dynamic_ratio(mat, WITNESSES[wname])
            tag = f"({mname}, {wname})"
            print(f"    {tag:15s} f {f:2d}  i {i_in}->{i_out}  "
                  f"ell {l_in}->{l_out}  pred {str(pred):4s}  "
                  f"meas {meas:.4f}  eta=eps^i {'OK' if spec else 'NO'}")
            all_law &= spec and pred == MEASURED9[(mname, wname)]
            all_dyn &= abs(meas / float(pred) - 1) <= 0.06
    check("law reproduces all nine ratios, eta = eps^i exact each pair",
          all_law)
    check("dynamic ratio within 6% of prediction at all nine", all_dyn)
    m, _ = dynamic_ratio(MAPS9["2x"], WITNESSES["phi"])
    check("positive control: (2x, phi) measures ~3.01 as before",
          abs(m - 3.0112) < 0.02)
    m2, _ = dynamic_ratio(MAPS9["2x"], WITNESSES["sqrt2"])
    check("positive control: (2x, sqrt2) measures ~1 (Pell)",
          abs(m2 - 1) < 0.02)
    print("    note: ratio 1 twice by different mechanisms -- "
          "(2x, sqrt2): i=2, ell 1->2; (x/2, sqrt2): i=1, ell 1->1")


# ------------------------------------------------------------------ #
# E2: the sight-unseen battery + the index vs the formula             #
# ------------------------------------------------------------------ #

SIGHT_UNSEEN = [
    ("5x", (5, 0, 0, 1), "phi", 5),
    ("7x", (7, 0, 0, 1), "phi", 4),
    ("5x", (5, 0, 0, 1), "sqrt2", 3),
    ("8x", (8, 0, 0, 1), "phi", 3),
]


def e2():
    print("\nE2 SIGHT-UNSEEN (predictions fixed before the run)")
    ok_pred, ok_spec = True, True
    deficits = []
    for mname, mat, wname, predicted in SIGHT_UNSEEN:
        P, D, Q = SURDS[wname]
        d0, _ = squarefree_kernel(D)
        eps = eps_of(d0)
        i_in, l_in, i_out, l_out, f, pred, spec = \
            law_row(mat, P, D, Q, eps, d0)
        meas, _ = dynamic_ratio(mat, WITNESSES[wname])
        DK = d0 if d0 % 4 == 1 else 4 * d0
        ceil = ceiling_index(f, DK)
        att = "attained" if ceil == i_out else f"NOT attained (h_f = {ceil // i_out})"
        print(f"    ({mname}, {wname}): f {f}  i {i_out}  ell {l_in}->{l_out}"
              f"  pred {str(pred)}  meas {meas:.4f}  "
              f"ceiling {ceil} {att}")
        ok_pred &= pred == predicted and abs(meas / predicted - 1) <= 0.06
        ok_spec &= spec and ceil % i_out == 0
        deficits.append(ceil // i_out)
    check("all four sight-unseen ratios land as predicted (5, 4, 3, 3)",
          ok_pred)
    check("eta = eps^i exact; i divides the ceiling at all four", ok_spec)
    check("the two designed witnesses separate index from formula: "
          "deficits (1, 1, 2, 2)", deficits == [1, 1, 2, 2])
    print("    the measured ratio follows the INDEX where the ceiling "
          "is not attained; the deficit is h(O_f)/h_K (imported formula)")


# ------------------------------------------------------------------ #
# E3: the necessity scan over x_a = [(a)]                             #
# ------------------------------------------------------------------ #

def e3():
    print("\nE3 NECESSITY SCAN (x -> nx over x_a = [(a)], a = 1..10)")
    ok_spec, per_n_mismatch, spot_rows = True, {}, []
    all_rows = {}
    for n in (2, 3, 5, 6):
        mat = (n, 0, 0, 1)
        found = []
        for a in range(1, 11):
            P, D, Q = a, a * a + 4, 2
            d0, _ = squarefree_kernel(D)
            eps = eps_of(d0)
            i_in, l_in, i_out, l_out, f, pred, spec = \
                law_row(mat, P, D, Q, eps, d0)
            ok_spec &= spec
            mark = "mismatch" if pred != 1 else "MATCHED"
            found.append((a, pred))
            print(f"    n={n} a={a:2d}: i {i_in}->{i_out}  "
                  f"ell {l_in}->{l_out}  pred {str(pred):5s} {mark}")
        mism = [(a, p) for a, p in found if p != 1]
        per_n_mismatch[n] = mism
        all_rows[n] = found
        if mism:
            spot_rows.append((n, mism[0][0], mism[0][1]))
    check("eta = eps^i exact at all 40 rows (incl. i_in > 1 rows)",
          ok_spec)
    check("every scanned n owns a mismatched witness",
          all(per_n_mismatch[n] for n in (2, 3, 5, 6)))
    check("the Pell coincidence: n=2, a=2 is matched (pred 1)",
          any(a == 2 and p == 1 for a, p in all_rows[2]))
    # dynamic spot-checks: first mismatched row per n
    ok_dyn = True
    for n, a, pred in spot_rows:
        quots = [a] * 200
        meas, _ = dynamic_ratio((n, 0, 0, 1), quots, 120)
        print(f"    spot n={n} a={a}: pred {str(pred)}  meas {meas:.4f}")
        ok_dyn &= abs(meas / float(pred) - 1) <= 0.06
    check("dynamic spot-check within 6% at the first mismatch per n",
          ok_dyn)
    return spot_rows


# ------------------------------------------------------------------ #
# E4: the reduction lemma live (Smith transport)                      #
# ------------------------------------------------------------------ #

def matmul(X, Y):
    return (X[0] * Y[0] + X[1] * Y[2], X[0] * Y[1] + X[1] * Y[3],
            X[2] * Y[0] + X[3] * Y[2], X[2] * Y[1] + X[3] * Y[3])


def e4(spot_rows):
    print("\nE4 SMITH TRANSPORT (the reduction lemma live)")
    U, V = (2, 1, 1, 1), (1, -1, 0, 1)          # V(y) = y - 1
    n, a, pred = next(r for r in spot_rows if r[0] == 6)
    M6 = matmul(matmul(U, (6, 0, 0, 1)), V)
    M2 = matmul(matmul(U, (2, 0, 0, 1)), V)
    det6 = M6[0] * M6[3] - M6[1] * M6[2]
    det2 = M2[0] * M2[3] - M2[1] * M2[2]
    print(f"    M6 = U diag(6,1) V = {M6} (det {det6}); "
          f"witness y* = x_{a}+1")
    quots6 = [a + 1] + [a] * 300                 # x_a + 1
    meas, _ = dynamic_ratio(M6, quots6, 150)
    d60 = 60 - len(emitted(M6, quots6, 60))
    d150 = 150 - len(emitted(M6, quots6, 150))
    print(f"    M6 at y*: meas ratio {meas:.4f} vs transported pred "
          f"{str(pred)}; delay(60) = {d60}, delay(150) = {d150}")
    check("M6 measured ratio = the transported scaling prediction",
          abs(meas / float(pred) - 1) <= 0.06)
    check("M6 stalls linearly at the transported witness",
          d150 - d60 >= 20)
    quots2 = [3] + [2] * 300                     # (1+sqrt2) + 1
    m2, _ = dynamic_ratio(M2, quots2, 150)
    e60 = 60 - len(emitted(M2, quots2, 60))
    e150 = 150 - len(emitted(M2, quots2, 150))
    print(f"    M2 = {M2} (det {det2}) at 2+sqrt2: ratio {m2:.4f}; "
          f"delay(60) = {e60}, delay(150) = {e150}")
    check("M2 reads the transported Pell witness at bounded delay",
          abs(m2 - 1) <= 0.06 and abs(e150 - e60) <= 5)


# ------------------------------------------------------------------ #
# E5: the necessity proof's checkable parts                           #
# ------------------------------------------------------------------ #

def e5():
    print("\nE5 THE NECESSITY PROOF (phi the universal witness)")
    # (a) floor rigidity: trace > L_ell off the all-1s word
    lucas = {1: 1, 2: 3, 3: 4, 4: 7, 5: 11, 6: 18}
    ok_rig = True
    from itertools import product as iproduct
    for ell in range(1, 7):
        for word in iproduct(range(1, 5), repeat=ell):
            w11, w12, w21, w22 = 1, 0, 0, 1
            for a in word:
                w11, w12, w21, w22 = (a * w11 + w12, w11,
                                      a * w21 + w22, w21)
            tr = w11 + w22
            if word == (1,) * ell:
                ok_rig &= tr == lucas[ell]
            else:
                ok_rig &= tr > lucas[ell]
    check("floor rigidity: trace > L_ell except all-1s "
          "(ell <= 6, digits <= 4, 5460 words)", ok_rig)
    # (b) apparition rank >= 3
    ok_app, ranks = True, {}
    for n in range(2, 2001):
        a, b, i = 1, 1, 2
        while b % n:
            a, b, i = b, (a + b) % n, i + 1
        ranks[n] = i
        ok_app &= i >= 3
    check("i(n) = Fibonacci apparition rank >= 3 for n = 2..2000",
          ok_app)
    # (c) i(n) != ell(n phi) for n = 2..40
    ok_neq, closest = True, []
    for n in range(2, 41):
        pre, per, state, D = surd_cf(n, 5 * n * n, 2)
        ell = len(per)
        i = ranks[n]
        ok_neq &= i != ell
        closest.append((n, i, ell))
    print("    (n, i, ell) sample: " +
          "  ".join(f"({n},{i},{l})" for n, i, l in closest[:8]))
    check("i(n) != ell(n phi) at every n = 2..40 (ratio never 1)",
          ok_neq)


if __name__ == "__main__":
    e1()
    e2()
    rows = e3()
    e4(rows)
    e5()
    print("\n" + ("ALL ENGINES PASS" if not FAILS
                  else f"{len(FAILS)} FAILURES: {FAILS}"))
    raise SystemExit(1 if FAILS else 0)
