"""explore_mu8_grading.py — the mu_8 grading at p = 2 (a further run in
the constellation-law family, following the e = 2 trichotomy of
explore_arrival_defect.py and the odd-p face of explore_tame_face.py).

THE QUESTION (following on from explore_arrival_defect.py and
explore_tame_face.py). At e = 2 the single arrival class (m = 1,
constellation u^2 + 1, the mu_4 layer) grades
K(i)/K as the trichotomy. An e = 4, f = 1 window of Q_2 carries TWO
arrival classes: c*2^m = i* = 4 gives c = 2 (m = 1, mu_4 again) and
c = 1 (m = 2, constellation u^4 + 1 — the four primitive 8th roots,
the mu_8 layer, K(zeta8) = K(i, sqrt2, sqrt-2), up to BIQUADRATIC).
Does the class-1 landing grade K(zeta8)/K the way class-1-at-e=2
graded K(i)/K — one arrival class per cyclotomic layer?

THE HAND LEMMAS (derived by hand in three passes before this file
existed):

ML1 (the two arrival classes). Class-1 orbits at e = 4 are rigidly
    (1, 2, 4, L1): v(u^2 - 1) = 2 and v(u^4 - 1) = 4 for every
    class-1 unit (level-2 residue of t^2 is 1, F_2 forced). Class-2
    orbits are (2, 4, L2). Landings L = 4 + A, A1 = v(u^4 + 1),
    A2 = v(u^2 + 1).

ML2 (the composition). u^2 is a class-2 unit, so A1(u) = A2(u^2):
    the mu_8 game IS the mu_4 game evaluated on the SQUARE subclass —
    whose level-3 direction is forced (= res(w), from the 2s carry),
    so squares are not generic class-2 units and the two games read
    different data.

ML3 (the w-machine; e = 2 revalidated). Everything reduces to the
    canonical expansion of w = 2/pi^e (the unit part of 2 in the
    window; w_1..w_3 are pi-invariant because unit fourth powers are
    1 + O(pi^4)-deep). At e = 2 the ladder (rel-1: w_1 + 1, rel-2:
    w_2, rel-3+: unit freedom) re-derives the trichotomy of
    explore_arrival_defect.py exactly: sqrt2 has w = 1 (stop at
    rel-1: landing 5 rigid), sqrt-5 has w_1 = w_2 = 1 (stop at rel-2:
    6 rigid), Q_2(i) has w_1 = 1, w_2 = 0 (freedom: min 7, graded to
    CAP). The trichotomy is the first-nonzero position of 2's digit
    ladder — its classical
    letters (ram/unram/split) are one reading of that position.

ML4 (the rung ladder at e = 4). Class-1: A1 = 4 + rel-stop of
    I = (w + T^2) + pi^2*w*T (T = (u^2-1)/pi^2), with rigid window
    rel-1: w_1 | rel-2: w_2 + 1 | rel-3: w_3 | rel-4: w_4 + 1 |
    rel-5: w_5 + 1, and unit freedom only at rel-6 (via a_3; a_2
    cancels at every rigid offset). Rungs: L1 = 9, 10, 11, 12, 13
    rigid, 14 = the freedom dodge (deeper = collide branches; CAP
    iff zeta8 in K). Class-2: rel-1: w_1 | rel-2: w_2 + a_3 + 1 —
    freedom already at rel-2: L2min = 9 (w_1 = 1) or 10 = p(i*+1).
    THE SHAPE: the deeper cyclotomic layer has the LONGER rigid
    window — mu_8 reads ~4 more digits of the window's 2 than mu_4
    before the unit gets a choice.

ML5 (the carry law). F_2-xor bookkeeping of series sums is INVALID:
    coefficients colliding at 1 + 1 carry e levels up (2*pi^k =
    pi^(k+e)*w). The trap fired three times in derivation, caught by
    the zeta8 anchor (measured 14 vs xor's 13), the root-side
    paired-rise parity (antipodal pair members agree through level
    3, so approaches rise in pairs), and u = i exactness at
    x^4+2x^2+2. Hence: per-field predictions come from exact
    arithmetic (the engine's own ring ops extract canonical digits),
    and the ladder's rel-4/rel-5 constants are frozen as the
    falsifiable form — a miss at rel <= 3 falsifies the law, a miss
    at rel >= 4 corrects a constant (an upgraded miss, matching
    precedent from earlier runs).

THE PREDICTIONS (fixed by hand in a third pass, then hand-attacked,
before this file existed):

Zoo (all f = 1, e = 4, Eisenstein): the six pure fields x^4 - d,
d in {+-2, +-6, +-10} (w = 1/mu' in U_4); x^4+2x+2 (w_1 = 1);
x^4+2x^3+2x^2+2 (w_2 = w_3 = 1); x^4+2x^2+2 (i = 1 + pi^2 in K,
w - 1 = -pi^2*unit); Phi_8(x+1) (zeta8, the anchor field from
explore_arrival_defect.py). THE SWEEP:
all [d, 2c1, 2c2, 2c3, 1], d in {+-2, +-6, +-10}, c_i in {0, 1}
(48 polys, containing the zoo except zeta8).

MU1 (the lock): min spec1 = 9 <=> min spec2 = 9 <=> w_1 = 1, and
    then BOTH spectra are rigid {9} — the two layers' floors lock at
    the first digit. Witness: x^4+2x+2.
MU2 (the m = 1 law persists): w_1 = 0 => min spec2 = 10 = p(i*+1);
    pure fields realize spec2 minima {10, 11} both; CAP in spec2
    <=> -1 split (i in K; i is a class-2 torsion unit).
MU3 (rung 10 = the U_3 bucket): w in U_3 (w_1 = w_2 = 0) => spec1 =
    {10} rigid. All six pure fields sit there: the family mu_4
    cannot separate collapses into ONE mu_8 rung — the grading
    separates the w in U_2 minus U_3 fields (rungs 11-14) instead.
MU4 (rung 11): x^4+2x^3+2x^2+2: min spec1 = 11 (carry-free rel-3).
MU5 (rung 12): x^4+2x^2+2: min spec1 = 12 (rel-4 constant exposed).
MU6 (regression): zeta8 replicates explore_arrival_defect.py's
    measurement: spec1 = {14, CAP}, min spec2 = 10, CAP in spec2; the
    two-value spec1 is the in-pair F_2 pigeonhole cascade past amax.
MU7 (THE GRADING LAW — the headline): across the sweep, min spec1
    is a FUNCTION of w's canonical digits (w_1..w_5) alone,
    following the rung ladder — the independent side computed from
    the field's own expansion of 2, the measured side from orbits.
MU8 (dictionary rows): (a) all-three-split <=> the field is
    Q_2(zeta8) (CAP in spec1 at the exhaustive anchor); (b) CAP in
    spec2 <=> -1 split (exhaustive, L2 <= 4 + d(-1) <= 12 bounds the
    non-split tail below CAP); (c) rung 9 => NO split label (2, -2
    non-squares by parity of v(y^2 - 1); i in K contradicts rigid
    {9}); (d) by construction: x^4-2 has 2 split, x^4+2 has -2
    split, x^4+2x^2+2 has -1 split (Phi_4(1 + pi^2) = 0 exact).
Labels (never read orbits): delta in {-1, 2, -2}: split iff
    sq_approach(delta) > 2e; unram iff sq_approach(5*delta) > 2e;
    else ram. Guard: sq_approach(5) <= 2e everywhere (sqrt5 never in
    a totally ramified quartic). Starters: spec[4] min = 9 = p*i*+1
    at every field (the dying-seat floor, AD1's e = 4 face).

THE DESIGN. LF machinery of explore_local_clock; helpers imported
from explore_arrival_defect. Per sweep field: EXHAUSTIVE census at
amax = 12 (2048 representatives of U_1/U_amax: spec2 complete,
starter floor, labels via sq_approach, CAP-in-spec2) + SAMPLED
census at amax = 18 (seeded rng, 400 units per class for classes 1
and 2: deep rungs, 14-vs-CAP separation; a sampled landing BELOW a
frozen minimum falsifies outright) + the psi-gear sanity on every
sampled orbit (off-seat equality, on-seat >=). zeta8 exhaustive at
amax = 16 (replicating explore_arrival_defect.py). The independent
side: w = 2/pi^4
built from the Eisenstein relation (w = (-2/c0)*D^{-1}, D the unit
denominator; Newton inverse), verified by pi^4*w = 2 exact, digits
extracted canonically (d_n = 1 iff v(A) = 0; A <- (A - d_n)/pi with
2/pi = w*pi^3), self-checked by reconstruction to level 8. Torsion
constructed exactly where in-field (i = 1 + pi^2 at x^4+2x^2+2 with
Phi_4(i) = 0 asserted; zeta8 = 1 + pi at the cyclotomic model).
Run: python prime/code/explore_mu8_grading.py

FINDINGS (entered post-run, copied from printed output;
tier-labeled).

1. THE RUNG LADDER — the mu_8 grading (rule in range; the headline,
   MU7): at every censused e = 4, f = 1 window of Q_2 (48 Eisenstein
   quartics + zeta8) the class-1 (mu_8) landing minimum is a FUNCTION
   of the canonical digits w_1..w_5 of w = 2/pi^4 alone — 16
   digit-vectors realized in the sweep (zeta8's (0,1,0,0,1) is a
   seventeenth), each a single rung — following the staircase
   L1 = 9 / 10 / 11 / 12 / 13 / 14 at the first stop of
   (w_1; w_2 + 1; w_3; w_4; w_5 + 1; unit freedom), and the spectrum
   is RIGID (single-valued) at every rung <= 13. The breathing
   transient's deepest class reads the expansion of the wild prime
   itself, five digits deep, before any unit choice exists.

2. THE LOCK (rule in range; MU1): min L1 = 9 <=> min L2 = 9 <=>
   w_1 = 1, and then the class-1 AND class-2 spectra are both rigid
   {9} — the mu_4 and mu_8 floors lock at the first digit; the 24
   rung-9 fields are exactly the sweep's w_1 = 1 half. (Starters
   keep the 9 FLOOR only: their spectrum stays graded 9..CAP — the
   seat game has a free dodge the arrival games lack.)

3. THE LAYER-DEPTH SPLIT (rule in range; MU2 + ML4): class-2 (mu_4)
   unit freedom enters at rel-2 — its min is 10 = p(i*+1) at every
   w_1 = 0 field (the m = 1 cross-p law persists at e = 4), with
   {10, 11} both realized at all six pure fields — while class-1
   (mu_8) freedom enters only at rel-6: the deeper cyclotomic layer
   reads four more digits of the window's 2 before the unit gets a
   choice. Starters land 9 = p*i*+1 at all 49 fields (AD1's e = 4
   face).

4. THE TWO-AXIS DICTIONARY (rule in range over the census; MU8): the
   rung is NOT the decomposition type of K(zeta8)/K — it grades the
   ramification FILTRATION position (the higher-unit class of 2)
   while the label triple grades the decomposition: rungs 9 and 11
   are BOTH all-ram triples (totally ramified biquadratic) split by
   wildness depth; rung 10 is the blind bucket (exactly one non-ram
   letter, in any slot — all six pure fields collapse there, w in
   U_3: the game stops on its own 2S term before the letters can
   speak); rung 12 <=> (-1 unram); rung 13 <=> (-1 split, i in K);
   rung 14 with CAP tail <=> all split (Q_2(zeta8) itself, digits
   (0,1,0,0,1)). CAP in spec2 <=> -1 split, both directions,
   exhaustively. At e = 2 the trichotomy's letter and break coincide
   (one break in a quadratic); e = 4 splits the two axes apart.

5. MU6 replicated explore_arrival_defect.py's measurement exactly:
   zeta8 spec1 = {14, CAP}, min spec2 = 10 with CAP present, starter
   floor 9; the {14, CAP} two-value shape is the in-pair F_2
   pigeonhole cascade past amax.

6. THE BASE-FREEDOM (rule in range; section [4], added in a later
   pass when the invariance question surfaced): the rung is
   UNIFORMIZER-INVARIANT — at one field per rung, five alternative
   uniformizers pi' = pi*eta each (30 combinations), the ladder read
   on the digits of 2/pi'^4 in base pi' stops at the same rung every
   time, and the digits UP TO the stop never move — while digits
   BEYOND the stop flip freely with the base (e.g. x4-2's w_4 flips
   under eta = 1+pi+pi^2+pi^3). The intrinsic object is the STOP
   POSITION — a break in the filtration, Hasse-Herbrand-shaped —
   and the digits are its coordinates; "a function of the digits"
   is base-free in VALUE precisely because the pre-stop prefix is.

PRE-GREEN FAILURES (two, adjudicated):
(a) the label machinery's even-valuation scaling — sq_approach
    searches UNIT squares, but sqrt2 = pi^2 is not a unit: delta =
    2m must test m*w against unit squares (2 = pi^4*w); x^4-2's
    construction-true "2 split" exposed it on the first run.
(b) the rel-4 constant — the hand xor said rel-4 = w_4 + 1, the
    census said rel-4 = w_4 (the rel-2 collision's carry lands at
    rel-6, not rel-4): (0,1,0,1,0) measured 12 (predicted 13) and
    (0,1,0,0,0) measured 13 (predicted 12, MU5's recorded miss); the
    single swap explains both and zeta8's (0,1,0,0,1) -> 14 confirms
    it. Exactly the exposure ML5 froze: rel <= 3 held everywhere,
    the constant beyond corrected once.

RUN RECORD (python explore_mu8_grading.py, ~21 s, exit 0): 164,327
checks passed (gear sanity dominates the count: ~39K sampled orbits,
per-step asserts; 163,497 before section [4] was added in a later
pass). Sweep rows as printed: rung column = pred = L1
measured at all 48; L2min = 9 at the 24 w_1 = 1 fields, 10
elsewhere; starters 9 at all; labels as in finding 4. i-orbit at
x^4+2x^2+2: [2, 4, 13] (13 = CAP at amax 12). Section [4]: all six
rungs invariant over 5 uniformizers each; flips beyond the stop:
5/3/4/0/0/0 vectors at rungs 9/10/11/12/13/14. Green after the two
adjudications above; no other failures.
"""

import random

import explore_local_clock as lc
import explore_arrival_defect as ad

CHECKS = 0


def ok(cond, msg):
    global CHECKS
    if not cond:
        raise AssertionError(msg)
    CHECKS += 1


# ------------------------------------------------------------ w machinery


def scale_el(F, A, n):
    """Element A times integer n."""
    return tuple(F.cint(c, n) for c in A)


def unit_inv(F, D):
    """Inverse of a unit D with D = 1 + (v >= 1): Newton x <- x(2 - Dx)."""
    x = F.one
    two = ad.const_el(F, 2)
    for _ in range(7):
        x = F.emul(x, ad.esub(F, two, F.emul(D, x)))
    ok(F.val(ad.esub(F, F.emul(D, x), F.one)) == F.CAP,
       "%s: unit_inv failed" % F.name)
    return x


def w_element(F):
    """w = 2/pi^4 from the Eisenstein relation; verified exactly."""
    c0, c1, c2, c3 = F.eis[0], F.eis[1], F.eis[2], F.eis[3]
    mu0 = c0 // 2
    inv_mu0 = pow(mu0 % F.pM, -1, F.pM)
    D = [list(F.zero_c) for _ in range(F.e)]
    D[0][0] = 1
    D[1][0] = ((c1 // 2) * inv_mu0) % F.pM
    D[2][0] = ((c2 // 2) * inv_mu0) % F.pM
    D[3][0] = ((c3 // 2) * inv_mu0) % F.pM
    Dinv = unit_inv(F, tuple(tuple(c) for c in D))
    w = scale_el(F, Dinv, (-inv_mu0) % F.pM)
    # verify: pi^4 * w = 2 exactly (to working precision)
    pi = [list(F.zero_c) for _ in range(F.e)]
    pi[1][0] = 1
    pi = tuple(tuple(c) for c in pi)
    pi2 = F.emul(pi, pi)
    pi4 = F.emul(pi2, pi2)
    ok(F.val(ad.esub(F, F.emul(pi4, w), ad.const_el(F, 2))) == F.CAP,
       "%s: pi^4 * w != 2" % F.name)
    return w


def pi_el(F):
    el = [list(F.zero_c) for _ in range(F.e)]
    el[1][0] = 1
    return tuple(tuple(c) for c in el)


def digits(F, wp, pip, n=8):
    """F_2 digits of wp in base pip, where wp = 2/pip^4: division by
    pip via (A - d) * pip^3 * wp / 2 (coefficients exactly even)."""
    pip3 = F.emul(F.emul(pip, pip), pip)
    A, out = wp, []
    for _ in range(n):
        d = 1 if F.val(A) == 0 else 0
        out.append(d)
        B = [list(c) for c in A]
        B[0][0] = (B[0][0] - d) % F.pM
        C = F.emul(F.emul(tuple(tuple(c) for c in B), pip3), wp)
        ok(all(c[0] % 2 == 0 for c in C),
           "%s: odd coefficient in digit division" % F.name)
        A = tuple(((c[0] // 2),) for c in C)
    ok(out[0] == 1, "%s: leading digit not 1" % F.name)
    return out


def w_digits(F, w, n=8):
    """Canonical F_2 digits of w = 2/pi^4 at the model uniformizer,
    self-checked by reconstruction to level n."""
    pi = pi_el(F)
    digs = digits(F, w, pi, n)
    R = ad.const_el(F, 0)
    pw = F.one
    for d in digs:
        if d:
            R = tuple(F.cadd(a, b) for a, b in zip(R, pw))
        pw = F.emul(pw, pi)
    ok(F.val(ad.esub(F, w, R)) >= n,
       "%s: digit reconstruction fails" % F.name)
    return digs


def rung(digs):
    """The rung ladder: predicted min spec1 from w_1..w_5.

    rel-1..3 constants as frozen (ML4). The rel-4/rel-5 constants are
    the ADJUDICATED ones (first-run misses, the exposure ML5 named):
    hand xor said rel-4 = w_4 + 1, rel-5 = w_5 + 1; measured rel-4 =
    w_4 (the rel-2 collision's carry lands at rel-6, not rel-4), so
    (0,1,0,1,0) -> 12 and (0,1,0,0,0) -> 13 — one swap explains both
    misses, zeta8's (0,1,0,0,1) -> 14 confirms."""
    w1, w2, w3, w4, w5 = digs[1], digs[2], digs[3], digs[4], digs[5]
    if w1:
        return 9
    if w2 == 0:
        return 10
    if w3:
        return 11
    if w4:
        return 12
    if w5 == 0:
        return 13
    return 14


# ------------------------------------------------------------ census bits


def sq_el(F, tgt):
    """max over U_1/U_amax representatives u of v(u^2 - tgt)."""
    best = 0
    for u in F.units():
        vv = F.val(ad.esub(F, F.emul(u, u), tgt))
        if vv > best:
            best = vv
    return best


def labels(F, w):
    """Independent classical labels for delta in {-1, 2, -2}.

    Even-valuation generators scale by the unit part: delta = 2m has
    delta square in K iff m*w is a unit square (2 = pi^4*w, e = 4)."""
    lab = {}
    for delta in (-1, 2, -2):
        if delta == -1:
            t_split, t_unram = ad.const_el(F, -1), ad.const_el(F, -5)
        else:
            m = delta // 2
            t_split = scale_el(F, w, m)
            t_unram = scale_el(F, w, 5 * m)
        if sq_el(F, t_split) > 2 * F.e:
            lab[delta] = "split"
        elif sq_el(F, t_unram) > 2 * F.e:
            lab[delta] = "unram"
        else:
            lab[delta] = "ram"
    return lab


def sampled_spec(F, rng, per_class=400):
    """Sampled landing spectra for classes 1, 2 + psi-gear sanity."""
    spec = {}
    for c in (1, 2):
        for u in ad.sample_class(F, c, per_class, rng):
            o = F.orbit(u)
            for k in range(len(o) - 1):
                ps = min(2 * o[k], o[k] + F.e)
                if ps > F.amax:
                    break
                if o[k] == F.seat:
                    ok(o[k + 1] >= ps, "%s: seat below psi" % F.name)
                else:
                    ok(o[k + 1] == ps,
                       "%s: gear violation %s" % (F.name, o))
            if F.seat in o:
                n = o.index(F.seat)
                if n + 1 < len(o):
                    spec.setdefault(o[0], set()).add(o[n + 1])
    return spec


def build_i(F):
    """i = 1 + pi^2 (the x^4+2x^2+2 model); Phi_4(i) = 0 asserted."""
    el = [list(F.zero_c) for _ in range(F.e)]
    el[0][0] = 1
    el[2][0] = 1
    i_el = tuple(tuple(c) for c in el)
    ok(F.val(F.esub1(scale_el(F, F.emul(i_el, i_el), -1))) == F.CAP,
       "%s: (1+pi^2)^2 != -1" % F.name)
    return i_el


# ------------------------------------------------------------------- zoo

SWEEP = []
for d in (-2, 2, -6, 6, -10, 10):
    for c3 in (0, 1):
        for c2 in (0, 1):
            for c1 in (0, 1):
                SWEEP.append((d, 2 * c1, 2 * c2, 2 * c3))

ZOO = {
    (-2, 0, 0, 0): "x4-2",
    (2, 0, 0, 0): "x4+2",
    (-6, 0, 0, 0): "x4-6",
    (6, 0, 0, 0): "x4+6",
    (-10, 0, 0, 0): "x4-10",
    (10, 0, 0, 0): "x4+10",
    (2, 2, 0, 0): "x4+2x+2",
    (2, 0, 2, 0): "x4+2x^2+2",
    (2, 0, 2, 2): "x4+2x^3+2x^2+2",
}
PURE = [k for k in ZOO if k[1] == k[2] == k[3] == 0]


def run():
    rng = random.Random(187)
    print("THE MU_8 GRADING — the constellation law at e = 4")
    print("=" * 64)

    print("\n[1] the sweep: 48 Eisenstein quartics, digits vs landings")
    print("    %-22s %-6s %-4s %-4s %-6s %-5s %s"
          % ("field", "w1-w5", "pred", "L1", "L2min", "start", "labels"))
    fn = {}          # digit-vector -> set of measured min L1 (MU7)
    rows = {}
    for key in SWEEP:
        d, c1, c2, c3 = key
        name = ZOO.get(key, "[%d,%d,%d,%d]" % (d, c1, c2, c3))
        eis = [d, c1, c2, c3, 1]
        F = lc.LF(name, 2, [0, 1], eis, 12)
        w = w_element(F)
        digs = w_digits(F, w)
        pred = rung(digs)
        spec, _ = ad.landing_spectra(F, F.units())
        lab = labels(F, w)
        ok(ad.sq_approach(F, 5) <= 2 * F.e, "%s: sqrt5 in K?" % name)
        F18 = lc.LF(name, 2, [0, 1], eis, 18)
        sspec = sampled_spec(F18, rng)
        m1 = min(sspec[1])
        m2 = min(spec[2])
        # MU7: the grading law (rel-4 constant adjudicated, see rung())
        ok(m1 == pred, "%s: min L1 %d, predicted %d" % (name, m1, pred))
        # rigidity: every rigid rung is single-valued in the sample
        if pred <= 13:
            ok(sspec[1] == {pred},
               "%s: rung %d not rigid: %s" % (name, pred, sorted(sspec[1])))
        fn.setdefault(tuple(digs[1:6]), set()).add(m1)
        # the measured dictionary rows (rule in range over this census)
        nonram = [k for k in (-1, 2, -2) if lab[k] != "ram"]
        if pred in (9, 11):
            ok(not nonram, "%s: rung %d with non-ram %s" % (name, pred, lab))
        elif pred == 10:
            ok(len(nonram) == 1,
               "%s: rung 10 non-ram count %d" % (name, len(nonram)))
        elif pred == 12:
            ok(lab[-1] == "unram" and lab[2] == "ram" and lab[-2] == "ram",
               "%s: rung 12 labels %s" % (name, lab))
        elif pred == 13:
            ok(lab[-1] == "split" and lab[2] == "ram" and lab[-2] == "ram",
               "%s: rung 13 labels %s" % (name, lab))
        # starters (AD1 at e = 4)
        ok(min(spec[4]) == 9, "%s: starter floor %d != 9"
           % (name, min(spec[4])))
        # MU1: the lock
        if digs[1] == 1:
            ok(m2 == 9 and spec[2] == {9},
               "%s: w1=1 but spec2 %s" % (name, sorted(spec[2])))
            ok(sspec[1] == {9} and sspec[2] == {9},
               "%s: w1=1 not rigid-9" % name)
            # MU8(c): no split label at rung 9
            ok("split" not in lab.values(),
               "%s: rung 9 with a split label %s" % (name, lab))
        else:
            # MU2: the m = 1 law
            ok(m2 == 10, "%s: min L2 %d != 10" % (name, m2))
        # MU2/MU8(b): CAP in spec2 <=> -1 split
        ok((F.CAP in spec[2]) == (lab[-1] == "split"),
           "%s: CAP-in-spec2 vs -1-label mismatch" % name)
        # MU3: the U_3 bucket
        if digs[1] == 0 and digs[2] == 0:
            ok(spec[1] == {10} and sspec[1] == {10},
               "%s: U_3 field spec1 not rigid {10}: %s / %s"
               % (name, sorted(spec[1]), sorted(sspec[1])))
        rows[key] = (digs, pred, m1, m2, lab)
        print("    %-22s %s%s%s%s%s  %-4d %-4d %-6d %-5d %s"
              % (name, digs[1], digs[2], digs[3], digs[4], digs[5],
                 pred, m1, m2, min(spec[4]),
                 " ".join("%d:%s" % (k, lab[k]) for k in (-1, 2, -2))))
    # MU7 function-ness across the sweep
    for dv, mins in sorted(fn.items()):
        ok(len(mins) == 1, "digits %s give minima %s" % (dv, sorted(mins)))
    print("  MU7: %d digit-vectors, each a single rung — function-ness holds"
          % len(fn))

    print("\n[2] zoo deep points")
    # MU4 hit; MU5's hand value 12 MISSED (measured 13) — the rel-4
    # constant adjudication (see rung()); rung 12's witness is
    # [-2,0,2,0] with digits (0,1,0,1,0)
    ok(rows[(2, 0, 2, 2)][2] == 11, "rung-11 field missed")
    ok(rows[(-2, 0, 2, 0)][2] == 12, "rung-12 field missed")
    ok(rows[(2, 0, 2, 0)][2] == 13, "rung-13 field missed")
    # MU8(d): constructed splits
    ok(rows[(-2, 0, 0, 0)][4][2] == "split", "x4-2: 2 not split")
    ok(rows[(2, 0, 0, 0)][4][-2] == "split", "x4+2: -2 not split")
    ok(rows[(2, 0, 2, 0)][4][-1] == "split", "x4+2x^2+2: -1 not split")
    # MU2: pure fields realize spec2 minima {10, 11}
    for key in PURE:
        name = ZOO[key]
        F = lc.LF(name, 2, [0, 1], [key[0], key[1], key[2], key[3], 1], 12)
        spec, _ = ad.landing_spectra(F, F.units())
        ok({10, 11} <= spec[2],
           "%s: spec2 lacks {10,11}: %s" % (name, sorted(spec[2])))
    print("  rung 11 at x4+2x^3+2x^2+2 (hand hit); rung 12 at [-2,0,2,0],")
    print("  rung 13 at x4+2x^2+2 (hand 12 missed: rel-4 adjudicated)")
    print("  constructed splits verified; pure spec2 carries {10, 11}")
    # torsion at the i-field: i lands CAP as a class-2 unit
    F = lc.LF("x4+2x^2+2", 2, [0, 1], [2, 0, 2, 0, 1], 12)
    i_el = build_i(F)
    o = F.orbit(i_el)
    ok(o[0] == 2 and o[-1] == F.CAP,
       "i-orbit not class-2-to-CAP: %s" % o)
    print("  i = 1 + pi^2: Phi_4(i) = 0 exact, orbit %s" % o)

    print("\n[3] zeta8 (anchor field, exhaustive amax 16)")
    F = lc.LF("Q2(zeta8)", 2, [0, 1], [2, 4, 6, 4, 1], 16)
    w = w_element(F)
    digs = w_digits(F, w)
    spec, _ = ad.landing_spectra(F, F.units())
    ok(spec[1] == {14, F.CAP},
       "zeta8: spec1 %s != {14, CAP}" % sorted(spec[1]))
    ok(min(spec[2]) == 10 and F.CAP in spec[2],
       "zeta8: spec2 %s" % sorted(spec[2]))
    ok(min(spec[4]) == 9, "zeta8: starter floor")
    ok(rung(digs) == 14, "zeta8: digits %s predict %d, measured 14"
       % (digs, rung(digs)))
    lab = labels(F, w)
    ok(all(v == "split" for v in lab.values()),
       "zeta8: labels not all split: %s" % lab)
    print("  digits w1-w5 = %s, rung 14; spec1 = {14, CAP}; labels all split"
          % (digs[1:6],))

    print("\n[4] uniformizer invariance: the rung is base-free")
    ETAS = ((1, 1, 0, 0), (1, 0, 1, 0), (1, 0, 0, 1),
            (1, 1, 0, 1), (1, 1, 1, 1))
    PREFIX = {9: 1, 10: 2, 11: 3, 12: 4, 13: 5, 14: 5}
    for name, eis, r in (
            ("x4+2x+2", [2, 2, 0, 0, 1], 9),
            ("x4-2", [-2, 0, 0, 0, 1], 10),
            ("x4+2x^3+2x^2+2", [2, 0, 2, 2, 1], 11),
            ("[-2,0,2,0]", [-2, 0, 2, 0, 1], 12),
            ("x4+2x^2+2", [2, 0, 2, 0, 1], 13),
            ("Q2(zeta8)", [2, 4, 6, 4, 1], 14)):
        F = lc.LF(name, 2, [0, 1], eis, 20)
        w = w_element(F)
        d0 = w_digits(F, w)
        ok(rung(d0) == r, "%s: base rung %d != %d" % (name, rung(d0), r))
        P = PREFIX[r]
        flips = 0
        for ev in ETAS:
            eta = [list(F.zero_c) for _ in range(F.e)]
            for j, b in enumerate(ev):
                eta[j][0] = b
            eta = tuple(tuple(c) for c in eta)
            e2 = F.emul(eta, eta)
            wp = F.emul(w, unit_inv(F, F.emul(e2, e2)))
            pip = F.emul(pi_el(F), eta)
            d2 = digits(F, wp, pip)
            ok(rung(d2) == r,
               "%s eta=%s: rung %d != %d" % (name, ev, rung(d2), r))
            ok(d2[1:P + 1] == d0[1:P + 1],
               "%s eta=%s: stop-prefix digits moved" % (name, ev))
            if d2[1:6] != d0[1:6]:
                flips += 1
        print("  %-16s rung %-2d invariant over 5 uniformizers"
              " (%d vectors flip beyond the stop)" % (name, r, flips))

    print("\n%d checks passed" % CHECKS)


if __name__ == "__main__":
    run()
