"""explore_cutoff_ladder.py — THE WILD-LAYER CUTOFF LADDER: which
fractional level cuts, in general (the open question left by
explore_tame_face.py's finding 4).

THE QUESTION (explore_tame_face.py finding 4). The
mid-fields' class-1 spectrum top 13 = 3 + 3*(7/3) + 3 is the approach
to the collided cluster cut at the FRACTIONAL level 7/3; at the p = 2
ramified quadratics the cut is 3/2 = 3e/4. Which fractional level
cuts, in general?

THE HAND LEMMAS (derived by hand before this file existed):

CL1 (the reduction — cluster product = storey-down power). The
    collided cluster of the class-c (c*p^m = i*) game is the p^m
    preimages of zeta_p among the primitive p^{m+1}-th roots, and
      prod_{omega^{p^m} = zeta_p} (u - omega) = u^{p^m} - zeta_p
    exactly. So the cluster's approach sum is v(u^{p^m} - zeta_p),
    bounded by D_m := max_y v_K(y^{p^m} - zeta_p) — the p^m-POWER
    KUMMER DEFECT of zeta_p in K, a K-INTERNAL quantity (no composite
    field needed). Cluster members are pairwise at v(zeta_{p^j} - 1),
    j <= m, minimal mutual distance v(zeta_{p^m} - 1) = i*/p^{m-1}
    (= i* at m = 1); when D_m/p^m is below it every member sits at
    the same depth:
      THE CUTOFF: the per-root approach ends at D_m / p^m.
    (C: 3d = 7 -> d = 7/3. p = 2, target -1: (u-i)(u+i) = u^2 + 1,
    d = 3/2 at delta = 3. AD8's Hensel cap A <= 2e IS delta <= p*i*.)

CL2 (the ceiling identity). v(u^{p^{m+1}} - 1) = v(u^{p^m} - 1)
    + sum_{j=1..p-1} v(u^{p^m} - zeta_p^j); the seat class forces
    v(u^{p^m} - 1) = i*, one factor can reach D_m, each other is then
    pinned at min(D_m, i*). delta(zeta_p^j) = delta(zeta_p) for p∤j
    (y = w^j: v(w^{pj} - c^j) >= v(w^p - c) + v(unit sum); symmetric).
      TOP(c, m) = i* + D_m + (p-2)*min(D_m, i*);  m = 1: (p-1)i* + delta.
    Only class i*/p can push v(y^{p^m} - zeta_p) past i* (psi(cl) =
    i* forces cl = i*/p), so the defect is intrinsically the
    arrival-class quantity — defect climbs exist iff p | i*, matching
    the arrival window L1.

CL3 (the value menu + the trichotomy one layer up). The matching walk
    that computes delta stops only at non-psi-image levels; the image
    of psi on (0, i*] covers p*Z inside (i*, p*i*], so
      delta in {l in (i*, p*i*) : p ∤ l} u {p*i*} u {inf}.
    (e = 2, p = 2: {3} u {4} u {inf} — ONE ramified value exists,
    which is why all four ramified quadratics share the cut 3/2.)
    Trichotomy, all p, m = 1: K(zeta_{p^2})/K is RAMIFIED iff
    delta < p*i* (fractional cut delta/p), UNRAMIFIED iff
    delta = p*i* (residue cut at the integer level i*), SPLIT iff
    delta = inf (zeta_{p^2} in K). At the boundary 1 + c*pi^{p*i*}
    the Artin-Schreier image of x^p - x on F_p is {0}: any c != 0
    yields the degree-p unramified extension — f = 1 odd-p
    unramified specimens EXIST and are word-designable: slots 4, 5
    holes + slot-6 non-hole at e = 6, i.e. word
    {w4 = 1, w5 = -w3, w6 != w3^2} (K9's variety is the all-holes
    word); the grid preimage exists uniquely (reduction-law
    bijection, explore_deep_spectrum.py DS-D iv).

CL4 (the Hasse-Herbrand contact). Classical Kummer-conductor: for
    L = K(x^{1/p}) with x a unit of defect depth delta (p ∤ delta,
    delta < p*i*), the ramification break of L/K is
      t = p*i* - delta   (lower = upper; single break, degree p).
    The cutoff re-read: departure = conjugate distance - t =
    p*i* - t = delta in v_L units, i.e. delta/p in v_K units — the
    same law in classical dress. The textbook cyclotomic break
    ladder 2^k - 1 of Q_2(zeta_{2^n}) is the delta = 1 rigid case
    (v(zeta - 1) = 1 at cyclotomic bases). Breaks are computable
    directly in cyclotomic models: pi_L = zeta - 1 = x, sigma:
    zeta -> zeta^k, i_G(sigma) = v(zeta^k - zeta) = t + 1.

THE PREDICTIONS (fixed before the run — hand-derived and hand-attacked
before this file existed; a measured stick ABOVE a frozen value
falsifies the law, one BELOW indicts climb adequacy or the prior
census — adjudicated if it fires):

WL1 (the identity, m = 1): landing-climb stick(class i*/p) =
    (p-1)*i* + delta(defect climb), the two climbs independent.
    Fields: C = x^6+3, D = x^6-6, x^6+3x^4+3 (delta 7, stick 13);
    x^12+3 (14, 26); x^18+3 (25, 43); p = 2 quadratics sqrt2 /
    sqrt-2 / sqrt10 / sqrt-10 (3, 5), sqrt-5 (4, 6), Q2(i)
    (torsion, CAP); K9 (torsion: y = zeta9 gives v = CAP).
WL2 (the menu): every measured finite delta lies in
    {l in (i*, p*i*): p ∤ l} u {p*i*} — in particular NEVER
    p | delta below p*i*.
WL3 (the ladder, m = 2): x^18+3 class (1, 2): D_2 = 21 by the
    independent 9th-power defect climb; stick 39 = 9 + 21 + 9;
    per-root cut 21/9 = 7/3; D_2 <= D_1 = 25.
WL4 (the designed unramified specimen, fresh): the 1458-point
    (b, d)-grid at e = 6 contains exactly one field with word
    [1,0,0,2,1,1,2]; its f = 1 game: delta = 9 = p*i*, class-1
    spectrum and climb-visited {12, 15} (holes 13, 14); its f = 3
    lift (g = x^3+2x+1) has defect stick >= 13 = 2*v(3) + 1
    (Newton margin: zeta9 IN the unramified cubic — K(zeta9)/K
    UNRAMIFIED), while C's f = 3 lift sticks at 7 (ramified: the
    non-image levels are residue-blind).
WL5 (the breaks, direct sigma vs the formula): (i) K9-model,
    sigma: z9 -> z9^4 and z9^7: v(z9^k - z9) = 3 both -> t = 2 =
    3*i*_E - delta_E, delta_E = 1 measured exhaustively in
    E = Q3(zeta3) = x^2+3x+3; (ii) zeta8-model, v(z8^k - z8) =
    {2, 4, 2} at k = 3, 5, 7 -> subgroup breaks t = 1 (sqrt-2),
    3 (i), 1 (sqrt2) = 4 - delta of the fixed field's defect
    (3, 1, 3): delta_{Q2(i)}(target i) = 1 measured exhaustively
    in x^2+2x+2; breaks of Q2(zeta8)/Q2 = {1, 3} = 2^k - 1
    (the classical ladder as the delta = 1 case).
WL6 (p = 5, fresh): x^20+30 (r = 1 mod 5, a 4th power: zeta5 in);
    zeta5 constructed EXACTLY by quartic radicals (sqrt5 = pi^10 *
    sqrt(-w), zeta5 = (-1+sqrt5)/4 + pi^5*sqrt(-t(1+pi^10 t)/8));
    delta in the menu; class-1 landing stick = 20 + delta; census
    floors 30 (class 1) and 26 (class 5) regress the tame readout.
WL7 (p = 2 quartics): x^4-2: delta in {7, 8} (the hand walk passes
    6 = psi(3) — an image level, not a stop; i not in K caps at 8);
    x^4+4x+2: delta in {5, 7, 8, inf}; Phi8(x+1): torsion (y = i);
    every stick = 4 + delta; the menu forbids 6.

THE DESIGN. LF machinery of explore_local_clock; sample_class,
landing_spectra, const_el from explore_arrival_defect; w_element,
w_digits, unit_inv, newton_sqrt_el, pi_el from explore_tame_readout;
gear_check from explore_tame_face. THE TARGETED CLIMB is the one new
primitive: greedy one-digit ascent on v(y^P * T - 1) (T = 1: the
landing climb; T = zeta_p^{-1}: the defect climb; T = -1 or i^{-1}
at p = 2), full neighbor scan, min-improving acceptance, steps
sweeping ALL nonzero residue vectors (f >= 2 needs mixed digits);
class-preserving k > c. Torsion certificates: a defect stick past
p*i* is Hensel-boundary (the p-power map U_a -> U_{a+e} is onto for
a > i*), and past 2*v(p) it is Newton — both cited where asserted.
zeta_p constructed exactly per field (Newton square roots via the
window unit; quartic radicals at p = 5); labels never read orbits.
Quadratics exhaustive; e >= 4 fields sampled + climbed. Run:
python prime/code/explore_cutoff_ladder.py

FINDINGS (entered post-run, copied from printed output).

1. THE CUTOFF LAW (rule in range; seventeen fields at p = 2, 3, 5):
   the forced approach to a one-storey-up torsion root ends at the
   fractional level delta/p (v_K units), delta = max_y v(y^p -
   zeta_p) the KUMMER DEFECT of the storey-down root — a K-internal
   quantity, measured by its own climb, no composite field touched.
   Verified through the ceiling identity stick = (p-1)*i* + delta
   (CL2) with the two climbs independent at every finite-delta
   field (fourteen; the three split fields realize defect CAP,
   Q2(i)'s top CAP with it, zeta8/K9 landing CAPs inherited from
   explore_arrival_defect / explore_tame_face):
   the mid-fields' 7/3 IS delta = 7 over p = 3 (C, D, x^6+3x^4+3:
   stick 13 = 2*3 + 7); the p = 2 quadratics' 3/2 IS delta = 3 over
   p = 2 (stick 5 = 2 + 3, four fields); fresh cuts: 14/3 at x^12+3
   (delta 14, stick 26), 25/3 at x^18+3 (25, 43), 21/5 at x^20+30
   (21, 41 — the first p = 5 mid-field censused), 7/2 at both
   censused ramified quartics of Q2 (7, 11).

2. THE MENU + THE TRICHOTOMY ONE LAYER UP (rule in range): every
   measured finite delta lies in {l in (i*, p*i*): p ∤ l} u {p*i*}
   — never p | delta below the boundary (no 6 at e = 6 or at the
   quartics). The tame face's trichotomy is the DEFECT READ AT
   THREE RANGES: K(zeta_{p^{m+1}})/K ramified <=> delta < p*i*
   (fractional cut delta/p), unramified <=> delta = p*i* (residue
   cut at the INTEGER level i* — sqrt-5's cut prints 2 = i* on
   cue), split <=> delta = inf (Q2(i), zeta8, K9: torsion realizes
   CAP). At e = 2, p = 2 the ramified menu is the single value {3}:
   THAT is why all four ramified quadratics share the cut 3/2.

3. THE UNRAMIFIED LETTER EXISTS AT ODD p, f = 1 (rule, designed
   witness + certificates): the Artin-Schreier image of x^p - x on
   F_p is {0}, so any nonzero boundary residue at depth p*i* opens
   the degree-p unramified extension. Designed: the word
   [1,0,0,2,1,1,2] (K9's variety with the third law broken:
   w6 = 2 != w3^2) has the unique grid preimage
   x^6+6x^5+6x^4+3x^3+12; measured delta = 9 = p*i* exactly,
   class-1 spectrum and climb-visited {12, 15} (holes 13, 14 — the
   frozen prediction verbatim), and its unramified-cubic lift
   (g = x^3+2x+1) climbs the defect to 14 >= 13 = 2v(3)+1, the
   Newton margin: zeta9 IS in the lift, K(zeta9)/K is UNRAMIFIED —
   while C's lift sticks at 7 (the non-image levels are
   residue-blind: ramified stays ramified). The e = 6 alphabet is
   complete: delta = 7 ram / 9 unram / inf split.

4. THE LADDER AT m = 2 (rule in range + one observation): the
   (1, 2)-game's ceiling reads the p^m-power defect D_m: x^18+3
   has D_2 = 21 by the independent 9th-power climb, stick
   39 = 9 + 21 + 9 (CL2 at m = 2), per-root cut D_2/p^2 = 7/3,
   and D_2 < D_1 = 25 (9th powers are scarcer than cubes).
   Observation: 21 = 3 * 7 = e(K/C) * delta_C, where the cube
   subfield C = Q3((-3)^{1/6}) sits in x^18+3 (pi -> pi^3) — the
   arithmetic SUGGESTS the storey-2 defect descends to C, making
   the two cuts equal at 7/3, but realization is NOT established
   (the C-optimal witness is a K-cube only mod U_4, and the
   correction enters at psi(4) = 12 < 21 — the naive transport
   argument has a gap); whether D_m = e * delta_subfield in
   general is open.

5. THE HASSE-HERBRAND CONTACT (the formula t = p*i* - delta is
   classical Kummer-conductor theory; the instances verified by
   direct sigma-action): K9-model: i_G = v(sigma(pi) - pi) =
   v(z9^k - z9) = 3 for both sigma -> t = 2 = 3*i*_E - delta_E with
   delta_E = 1 measured exhaustively in E = Q3(zeta3); zeta8-model:
   i_G = {2, 4, 2} at k = 3, 5, 7 -> subgroup breaks 1, 3, 1 =
   4 - delta of the fixed quadratics (3, 1, 3 — including
   delta(target i) = 1 in Q2(i), the mu4 -> mu8 storey); the tower
   breaks {1, 3} = 2^k - 1: the TEXTBOOK cyclotomic break ladder is
   the delta = 1 rigid case of the cutoff law (v(zeta - 1) = 1 at
   cyclotomic bases). One law, classical dress: departure =
   conjugate distance - break.

RUN RECORD (python explore_cutoff_ladder.py, 3.6 s, exit 0): 98
checks passed. Ceilings/defects as printed:
  C / D / x^6+3x^4+3   delta 7   stick 13   cut 7/3
  K9                   delta CAP (split)    C-f3: delta 7 (RAM)
  designed [12,0,0,3,6,6,1]  delta 9, spec {12,15}, stick 15;
                             f=3 lift: 14 >= 13 (zeta9 in: UNRAM)
  x^12+3               delta 14  stick 26   cut 14/3
  x^18+3               delta 25  stick 43   cut 25/3
           (1,2)-game  D_2   21  stick 39   cut 21/9 = 7/3
  x^20+30              delta 21  stick 41   cut 21/5
  sqrt2/-2/10/-10      delta 3   top 5      cut 3/2
  sqrt-5               delta 4   top 6      cut 2 = i* (unram)
  Q2(i)                delta CAP top CAP    (split)
  x^4-2 / x^4+4x+2     delta 7   stick 11   cut 7/2
  breaks: K9/E t = 2; zeta8 subgroup breaks 1, 3, 1; tower {1, 3}
PRE-GREEN FAILURES (two, both caught by the engine's own asserts):
(1) Q2(sqrt-5) was first modeled as x^2+5 — NOT Eisenstein at 2
    (5 is a 2-adic unit), so LF read garbage; menu_ok flagged the
    impossible delta = 2 <= i* and the model was rebuilt on
    pi = 1 + sqrt(-5) (x^2-2x+6). The menu is a MODEL tripwire.
(2) The quartic landing climb was first called with P = 8 —
    measuring storey 2's v(u^8 - 1) (stick 14) instead of the mu4
    landing v(u^4 - 1); the frozen identity 4 + delta caught it,
    P = 4 is the game.
"""

import random
from fractions import Fraction

import explore_local_clock as lc
import explore_arrival_defect as ad
import explore_tame_face as tf
import explore_tame_readout as tr

CHECKS = 0


def ok(cond, msg):
    global CHECKS
    if not cond:
        raise AssertionError(msg)
    CHECKS += 1


# ---------------------------------------------------------------- helpers


def ct(F, n):
    return ad.const_el(F, n)


def epow(F, u, n):
    r, b = F.one, u
    while n:
        if n & 1:
            r = F.emul(r, b)
        b = F.emul(b, b)
        n >>= 1
    return r


def residues(F):
    """All nonzero residue vectors of the residue field, as int tuples."""
    out = []

    def rec(pref):
        if len(pref) == F.f:
            if any(pref):
                out.append(tuple(pref))
            return
        for a in range(F.p):
            rec(pref + [a])

    rec([])
    return out


def sample_cls(F, c, count, rng):
    """count random units with v(u - 1) = c exactly (any f)."""
    monos = []
    for i in range(F.M):
        for j in range(F.e):
            n = F.e * i + j
            if c <= n < F.amax:
                monos.append((i, j, n))
    res = residues(F)
    for _ in range(count):
        u = [list(cc) for cc in F.one]
        lead = False
        for i, j, n in monos:
            if n == c:
                r = rng.choice(res)
                lead = True
            elif rng.random() < 0.5:
                r = rng.choice(res + [F.zero_c])
            else:
                continue
            for l in range(F.f):
                u[j][l] = (u[j][l] + r[l] * (F.p ** i)) % F.pM
        if not lead:
            continue
        uu = tuple(tuple(cc) for cc in u)
        if F.val(F.esub1(uu)) == c:
            yield uu


def tclimb(F, starts, c, P, T, cap):
    """Greedy one-digit ascent on v(y^P * T - 1), full neighbor scan,
    min-improving acceptance (deep_spectrum's climb, target-shifted
    and f-general). Returns (achieved set, stick)."""
    steps = []
    for k in range(c + 1, F.amax):
        i, j = divmod(k, F.e)
        for r in residues(F):
            s = [list(cc) for cc in F.one]
            for l in range(F.f):
                s[j][l] = (s[j][l] + r[l] * (F.p ** i)) % F.pM
            steps.append(epow(F, tuple(tuple(cc) for cc in s), P))
    one = ct(F, 1)

    def obj(uP):
        return F.val(ad.esub(F, F.emul(uP, T), one))

    best = None
    for y in starts:
        uP = epow(F, y, P)
        v = obj(uP)
        if best is None or v > best[0]:
            best = (v, uP)
    v, uP = best
    achieved = {v}
    while v < cap:
        nxt = None
        for sP in steps:
            w = obj(F.emul(uP, sP))
            achieved.add(w)
            if w > v and (nxt is None or w < nxt[0]):
                nxt = (w, sP)
        if nxt is None:
            break
        v = nxt[0]
        uP = F.emul(uP, nxt[1])
    return achieved, v


def defect_climb(F, T_inv, cap, rng, n=60):
    """delta = max_y v(y^{p^m} - zeta) as a climb on v(y^P * T - 1),
    class i*/p, P = p (storey 1). Returns stick."""
    c = F.seat // F.p
    starts = list(sample_cls(F, c, n, rng))
    _, stick = tclimb(F, starts, c, F.p, T_inv, cap)
    return stick


def landing_climb(F, c, P, cap, rng, n=60):
    """The landing game's climb: start from the floor walker."""
    starts = list(sample_cls(F, c, n, rng))
    one = ct(F, 1)
    lo = min(starts, key=lambda y: F.val(ad.esub(F, epow(F, y, P), one)))
    return tclimb(F, [lo], c, P, one, cap)


def unit_sqrt(F, A):
    """Element square root of a unit (odd p, f = 1): Teichmueller
    leading part + Newton on the 1-unit remainder."""
    d0 = A[0][0] % F.p
    s0 = next(s for s in range(1, F.p) if (s * s - d0) % F.p == 0)
    t_inv = ct(F, pow(tr.teich(F, d0), -1, F.pM))
    u = F.emul(A, t_inv)
    r = F.emul(ct(F, tr.teich(F, s0)), tr.newton_sqrt_el(F, u))
    ok(F.val(ad.esub(F, F.emul(r, r), A)) >= F.amax,
       "%s: unit_sqrt failed" % F.name)
    return r


def zeta3_el(F):
    """Exact zeta3 = (-1 + sqrt(-3))/2 via -3 = pi^e * w."""
    w, pi = tr.w_element(F)
    root = unit_sqrt(F, w)                      # sqrt(w); w0 = 1 residue
    s = F.emul(root, epow(F, pi, F.e // 2))     # sqrt(-3)
    inv2 = pow(2, -1, F.pM)
    z3 = tuple(F.cadd(F.cint(a, inv2), F.cint(b, inv2))
               for a, b in zip(ct(F, -1), s))
    phi = tuple(F.cadd(F.cadd(a, b), c) for a, b, c in
                zip(F.emul(z3, z3), z3, ct(F, 1)))
    ok(F.val(phi) >= F.amax, "%s: Phi_3(zeta3) != 0" % F.name)
    ok(F.val(F.esub1(z3)) == F.seat,
       "%s: v(zeta3 - 1) != i*" % F.name)
    return z3


def zeta5_el(F):
    """Exact zeta5 by quartic radicals: sqrt5 = pi^10 * t,
    zeta5 = (-1 + sqrt5)/4 + pi^5 * sqrt(-t(1 + pi^10 t)/8)."""
    w, pi = tr.w_element(F)                     # 5 = -pi^20 * w
    minus_w = tuple(F.cint(a, -1) for a in w)
    pi10 = epow(F, pi, 10)
    inv4, inv8 = pow(4, -1, F.pM), pow(8, -1, F.pM)
    for sgn in (1, -1):
        t = tuple(F.cint(a, sgn) for a in unit_sqrt(F, minus_w))
        sqrt5 = F.emul(pi10, t)
        # inner = -t*(1 + pi^10 t)/8
        one_plus = tuple(F.cadd(a, b) for a, b in
                         zip(ct(F, 1), F.emul(pi10, t)))
        inner = tuple(F.cint(a, -inv8 % F.pM)
                      for a in F.emul(t, one_plus))
        if (inner[0][0] % F.p) not in (1, 4):   # QR test mod 5
            continue
        ipart = F.emul(epow(F, pi, 5), unit_sqrt(F, inner))
        re = tuple(F.cint(F.cadd(a, b), inv4)
                   for a, b in zip(ct(F, -1), sqrt5))
        z5 = tuple(F.cadd(a, b) for a, b in zip(re, ipart))
        phi, pw = ct(F, 1), ct(F, 1)
        for _ in range(4):
            pw = F.emul(pw, z5)
            phi = tuple(F.cadd(a, b) for a, b in zip(phi, pw))
        if F.val(phi) >= F.amax:
            ok(F.val(F.esub1(z5)) == F.seat,
               "%s: v(zeta5 - 1) != i*" % F.name)
            return z5
    raise AssertionError("%s: zeta5 construction failed" % F.name)


def zinv(F, z, k):
    """zeta^{-1} = zeta^{k} for a primitive (k+1)-th ... (caller
    passes the right power: zeta3 -> ^2, zeta5 -> ^4)."""
    return epow(F, z, k)


def menu_ok(F, delta, name):
    """CL3: finite delta in {l in (i*, p*i*): p ∤ l} u {p*i*}."""
    lo, hi = F.seat, F.p * F.seat
    ok((lo < delta < hi and delta % F.p != 0) or delta == hi,
       "%s: delta %d off the menu (i* %d)" % (name, delta, lo))


def digits_prefix(F, w, pi, n, bail=None):
    """First n Teichmueller digits of w; early-exit if digit j != want
    for (j, want) in bail."""
    pik = epow(F, pi, F.e - 1)
    A, out = w, []
    for j in range(n):
        d = A[0][0] % F.p
        out.append(d)
        if bail and j in bail and bail[j] != d:
            return None
        B = [list(c) for c in A]
        B[0][0] = (B[0][0] - tr.teich(F, d)) % F.pM
        C = F.emul(F.emul(tuple(tuple(c) for c in B), pik), w)
        assert all(c[0] % F.p == 0 for c in C), "inexact digit division"
        A = tuple(((-(c[0] // F.p)) % F.pM,) for c in C)
    return out


# ------------------------------------------------------------------- run


def run():
    rng = random.Random(213)
    print("THE WILD-LAYER CUTOFF LADDER — which fractional level cuts")
    print("=" * 66)

    # ------------- [1] p = 3, e = 6: the ram trio, K9, the f = 3 labels
    print("\n[1] e = 6: delta = 7 prices the 7/3 cut; the f = 3 labels")
    trio = [("x^6+3 (C)", [3, 0, 0, 0, 0, 0, 1]),
            ("x^6-6 (D)", [-6, 0, 0, 0, 0, 0, 1]),
            ("x^6+3x^4+3", [3, 0, 0, 0, 3, 0, 1])]
    for name, eis in trio:
        F = lc.LF(name, 3, [0, 1], eis, 18)
        z3 = zeta3_el(F)
        delta = defect_climb(F, zinv(F, z3, 2), 14, rng)
        menu_ok(F, delta, name)
        ok(delta == 7, "%s: delta %d != 7" % (name, delta))
        _, stick = landing_climb(F, 1, 9, 16, rng)
        ok(stick == (F.p - 1) * F.seat + delta,
           "%s: stick %d != (p-1)i* + delta = %d"
           % (name, stick, 2 * F.seat + delta))
        print("  %-12s delta=%d  stick=%d = 2*%d + %d   cut %s"
              % (name, delta, stick, F.seat, delta,
                 Fraction(delta, F.p)))
    # K9: torsion — y = zeta9 realizes v = CAP (split letter)
    F = lc.LF("Q3(zeta9)", 3, [0, 1], [3, 9, 18, 21, 15, 6, 1], 18)
    z9 = tuple(((1,) if j <= 1 else (0,)) for j in range(6))  # x + 1
    ok(F.val(ad.esub(F, epow(F, z9, 9), ct(F, 1))) >= F.CAP,
       "K9: zeta9^9 != 1")
    z3ind = zeta3_el(F)                          # independent target
    delta_k9 = max(F.val(ad.esub(F, epow(F, y, 3), z3ind))
                   for y in (z9, F.emul(z9, z9)))
    ok(delta_k9 >= F.CAP, "K9: no cube root of the constructed zeta3"
       " among {zeta9, zeta9^2} (defect %d)" % delta_k9)
    print("  %-12s delta=CAP (y = zeta9: split letter)" % "K9")

    # the f = 3 lifts: ramified sticks are residue-blind; unram flips
    g3 = [1, 2, 0, 1]                            # x^3 + 2x + 1, irred/F_3
    Fc3 = lc.LF("C-f3", 3, g3, [3, 0, 0, 0, 0, 0, 1], 18)
    z3c = zeta3_el(Fc3)
    d_c3 = defect_climb(Fc3, zinv(Fc3, z3c, 2), 14, rng, n=40)
    ok(d_c3 == 7, "C-f3: delta %d != 7 (ram label broken)" % d_c3)
    print("  C-f3         delta=7 (unramified cubic adds nothing: RAM)")

    # ------------- [2] the designed unramified specimen (WL4)
    print("\n[2] the designed unramified field: word [1,0,0,2,1,1,2]")
    target = [1, 0, 0, 2, 1, 1, 2]
    hits = []
    for d in (1, 2, 4, 5, 7, 8):
        for b1 in range(3):
            for b2 in range(3):
                for b3 in range(3):
                    for b4 in range(3):
                        for b5 in range(3):
                            eis = [3 * d, 3 * b1, 3 * b2, 3 * b3,
                                   3 * b4, 3 * b5, 1]
                            Fd = lc.LF("g", 3, [0, 1], eis, 16)
                            w, pi = tr.w_element(Fd)
                            digs = digits_prefix(
                                Fd, w, pi, 7,
                                bail=dict(enumerate(target)))
                            if digs == target:
                                hits.append(tuple(eis))
    ok(len(hits) == 1, "designed word hits %d grid points" % len(hits))
    eis_u = list(hits[0])
    print("  grid preimage: eis = %s" % (eis_u,))
    F, spec, dw, digs, orbits = tr.field_readout(
        "designed-unram", 3, eis_u, 30, [1, 3], rng)
    tr.law_row(F, spec, dw, 3)
    ok(min(spec[1]) == 12 and not (spec[1] & {13, 14})
       and spec[1] <= {12, 15},
       "designed: class-1 spectrum %s" % sorted(spec[1]))
    Fu = lc.LF("designed-unram", 3, [0, 1], eis_u, 18)
    z3u = zeta3_el(Fu)
    _, d_u = tclimb(Fu, list(sample_cls(Fu, 1, 60, rng)), 1, 3,
                    zinv(Fu, z3u, 2), 14)
    ok(d_u == 9, "designed: delta %d != 9 = p*i*" % d_u)
    ach_l, stick_u = landing_climb(Fu, 1, 9, 16, rng)
    ok(stick_u == 15, "designed: landing stick %d != 15" % stick_u)
    ok({v for v in ach_l if 12 <= v <= 15} == {12, 15},
       "designed: climb-visited %s != {12, 15}" % sorted(ach_l))
    Fu3 = lc.LF("designed-f3", 3, g3, eis_u, 18)
    z3u3 = zeta3_el(Fu3)
    d_u3 = defect_climb(Fu3, zinv(Fu3, z3u3, 2), 14, rng, n=40)
    ok(d_u3 >= 13, "designed-f3: delta %d < 13 = 2v(3)+1 — zeta9 not"
       " certified in the unramified cubic" % d_u3)
    print("  f=1: delta=9 = p*i* (boundary), spectrum %s, stick 15"
          % ad.fmt_spec(F, {1: spec[1]}).strip())
    print("  f=3: delta stick %d >= 13 — zeta9 IN the unramified cubic"
          "\n       => K(zeta9)/K UNRAMIFIED: the letter exists at odd"
          " p, f = 1" % d_u3)

    # ------------- [3] the ladder: e = 12, e = 18, the m = 2 storey
    print("\n[3] the ladder: x^12+3, x^18+3, and the m = 2 storey")
    F12 = lc.LF("x^12+3", 3, [0, 1], [3] + [0] * 11 + [1], 34)
    z3 = zeta3_el(F12)
    d12 = defect_climb(F12, zinv(F12, z3, 2), F12.p * F12.seat + 2, rng)
    menu_ok(F12, d12, "x^12+3")
    ok(d12 == 14, "x^12+3: delta %d != 14" % d12)
    _, s12 = landing_climb(F12, 2, 9, 30, rng)
    ok(s12 == 26 == 2 * 6 + d12, "x^12+3: stick %d != 26" % s12)
    print("  x^12+3   delta=14  stick=26 = 2*6 + 14    cut %s"
          % Fraction(d12, 3))
    F18 = lc.LF("x^18+3", 3, [0, 1], [3] + [0] * 17 + [1], 48)
    z3 = zeta3_el(F18)
    d18 = defect_climb(F18, zinv(F18, z3, 2), F18.p * F18.seat + 2, rng,
                       n=40)
    menu_ok(F18, d18, "x^18+3")
    ok(d18 == 25, "x^18+3: delta %d != 25" % d18)
    _, s18 = landing_climb(F18, 3, 9, 46, rng, n=40)
    ok(s18 == 43 == 2 * 9 + d18, "x^18+3: stick %d != 43" % s18)
    # the m = 2 storey: the 9th-power defect prices the (1, 2) game
    c2 = 1
    starts = list(sample_cls(F18, c2, 40, rng))
    _, D2 = tclimb(F18, starts, c2, 9, zinv(F18, z3, 2), 30)
    ok(D2 == 21, "x^18+3: D_2 %d != 21" % D2)
    ok(D2 <= d18, "x^18+3: D_2 %d > D_1 %d" % (D2, d18))
    _, s182 = landing_climb(F18, 1, 27, 42, rng, n=40)
    ok(s182 == 39 == 9 + D2 + 9,
       "x^18+3: (1,2) stick %d != 39 = i* + D_2 + i*" % s182)
    print("  x^18+3   delta=25  stick=43 = 2*9 + 25    cut %s"
          % Fraction(d18, 3))
    print("           D_2=21    stick=39 = 9 + 21 + 9  cut %s = 7/3"
          % Fraction(D2, 9))

    # ------------- [4] p = 5: the fresh face (WL6)
    print("\n[4] p = 5: x^20+30 — zeta5 by radicals, the identity fresh")
    ok(tf.unit_res(-30, 5) == 1, "x^20+30: residue r != 1")
    F5 = lc.LF("x^20+30", 5, [0, 1], [30] + [0] * 19 + [1], 48)
    z5 = zeta5_el(F5)
    d5 = defect_climb(F5, zinv(F5, z5, 4), F5.p * F5.seat + 2, rng, n=40)
    menu_ok(F5, d5, "x^20+30")
    _, s5 = landing_climb(F5, 1, 25, 47, rng, n=40)
    ok(s5 == 4 * 5 + d5, "x^20+30: stick %d != 20 + %d" % (s5, d5))
    units = list(sample_cls(F5, 1, 250, rng)) + \
        list(sample_cls(F5, 5, 250, rng)) + [z5]
    spec, orbits = ad.landing_spectra(F5, units)
    ok(min(spec[1]) == 30, "x^20+30: class-1 floor %d" % min(spec[1]))
    ok(min(spec[5]) == 26, "x^20+30: class-5 floor %d" % min(spec[5]))
    print("  x^20+30  delta=%d  stick=%d = 4*5 + %d   cut %s"
          % (d5, s5, d5, Fraction(d5, 5)))

    # ------------- [5] p = 2: quadratics exhaustive, quartics (WL7)
    print("\n[5] p = 2: the mu_4 storey — quadratics + quartics")
    quads = [("Q2(sqrt2)", [-2, 0, 1], 3), ("Q2(sqrt-2)", [2, 0, 1], 3),
             ("Q2(sqrt10)", [-10, 0, 1], 3),
             ("Q2(sqrt-10)", [10, 0, 1], 3),
             ("Q2(sqrt-5)", [6, -2, 1], 4),   # pi = 1 + sqrt(-5)
             ("Q2(i)", [2, 2, 1], None)]
    for name, eis, want in quads:
        F = lc.LF(name, 2, [0, 1], eis, 10)
        Tm1 = ct(F, -1)
        best, top = 0, 0
        extra = []
        if name == "Q2(i)":
            extra = [tuple(((1,), (1,)))]        # i = x + 1
        for y in list(F.units()) + extra:
            y2 = F.emul(y, y)
            v = F.val(ad.esub(F, y2, Tm1))
            cls = F.val(F.esub1(y))
            if v > best:
                best = v
            if cls == 1:
                o = F.orbit(y)
                if F.seat in o:
                    i = o.index(F.seat)
                    if i + 1 < len(o) and o[i + 1] > top:
                        top = o[i + 1]
        if want is None:
            ok(best >= F.CAP, "%s: delta %d not CAP" % (name, best))
            ok(top >= F.CAP, "%s: top %d not CAP" % (name, top))
            print("  %-13s delta=CAP top=CAP (split)" % name)
        else:
            menu_ok(F, best, name)
            ok(best == want, "%s: delta %d != %d" % (name, best, want))
            ok(top == F.seat + best,
               "%s: top %d != i* + delta = %d" % (name, top,
                                                  F.seat + best))
            print("  %-13s delta=%d top=%d = 2 + %d   cut %s"
                  % (name, best, top, best, Fraction(best, 2)))
    quartics = [("x^4-2", [-2, 0, 0, 0, 1], {7, 8}),
                ("x^4+4x+2", [2, 4, 0, 0, 1], {5, 7, 8}),
                ("Q2(zeta8)", [2, 4, 6, 4, 1], None)]
    for name, eis, dset in quartics:
        F = lc.LF(name, 2, [0, 1], eis, 16)
        Tm1 = ct(F, -1)
        if dset is None:
            i_el = epow(F, tuple(((1,), (1,), (0,), (0,))), 2)  # (x+1)^2
            v = F.val(ad.esub(F, F.emul(i_el, i_el), Tm1))
            ok(v >= F.CAP, "zeta8: i^2 != -1")
            print("  %-13s delta=CAP (split: i = zeta8^2)" % name)
            continue
        d = defect_climb(F, Tm1, 2 * F.e + 2, rng)
        menu_ok(F, d, name)
        ok(d in dset, "%s: delta %d not in %s" % (name, d, dset))
        ok(d != 6, "%s: the forbidden image value 6" % name)
        _, s = landing_climb(F, 2, 4, 14, rng)
        ok(s == F.seat + d, "%s: stick %d != 4 + %d" % (name, s, d))
        print("  %-13s delta=%d stick=%d = 4 + %d   cut %s"
              % (name, d, s, d, Fraction(d, 2)))

    # ------------- [6] the breaks: direct sigma vs p*i* - delta (WL5)
    print("\n[6] the Hasse-Herbrand contact: t = p*i* - delta, direct")
    # E = Q3(zeta3): delta_E = 1 exhaustively
    E = lc.LF("Q3(zeta3)", 3, [0, 1], [3, 3, 1], 10)
    z3e = tuple(((1,), (1,)))                    # zeta3 = x + 1
    dE = max(E.val(ad.esub(E, epow(E, y, 3), z3e)) for y in E.units())
    ok(dE == 1, "E: delta %d != 1" % dE)
    K9 = lc.LF("Q3(zeta9)", 3, [0, 1], [3, 9, 18, 21, 15, 6, 1], 18)
    z9 = tuple(((1,) if j <= 1 else (0,)) for j in range(6))
    pi9 = tr.pi_el(K9)
    for k in (4, 7):
        t1 = K9.val(ad.esub(K9, ad.esub(K9, epow(K9, z9, k), ct(K9, 1)),
                            pi9))
        ok(t1 == 3, "K9: v(z9^%d - z9) = %d != 3" % (k, t1))
    ok(3 - 1 == 3 * 1 - dE,
       "K9/E: break 2 != p*i*_E - delta_E")
    print("  K9/E:    i_G = 3 both sigma -> t = 2 = 3*1 - %d" % dE)
    # Q2(i): delta(target i) = 1 exhaustively
    Qi = lc.LF("Q2(i)", 2, [0, 1], [2, 2, 1], 10)
    i_el = tuple(((1,), (1,)))
    dI = max(Qi.val(ad.esub(Qi, Qi.emul(y, y), i_el))
             for y in Qi.units())
    ok(dI == 1, "Q2(i): delta(i) %d != 1" % dI)
    Z8 = lc.LF("Q2(zeta8)", 2, [0, 1], [2, 4, 6, 4, 1], 12)
    z8 = tuple(((1,), (1,), (0,), (0,)))
    pi8 = tr.pi_el(Z8)
    ig = {}
    for k in (3, 5, 7):
        ig[k] = Z8.val(ad.esub(Z8, ad.esub(Z8, epow(Z8, z8, k),
                                           ct(Z8, 1)), pi8))
    ok(ig == {3: 2, 5: 4, 7: 2}, "zeta8: i_G %s" % ig)
    # subgroup breaks = p*i*_K - delta_K: sqrt-2 (k=3), i (k=5), sqrt2 (k=7)
    ok(ig[7] - 1 == 2 * 2 - 3, "sqrt2: t != 4 - 3")
    ok(ig[3] - 1 == 2 * 2 - 3, "sqrt-2: t != 4 - 3")
    ok(ig[5] - 1 == 2 * 2 - dI, "i: t != 4 - 1")
    ok(sorted({ig[3] - 1, ig[5] - 1, ig[7] - 1}) == [1, 3],
       "zeta8/Q2: breaks != {1, 3} = 2^k - 1")
    print("  zeta8:   i_G = {3: 2, 5: 4, 7: 2} -> subgroup breaks"
          " 1, 3, 1\n           = 4 - delta (3, 1, 3); tower breaks"
          " {1, 3} = 2^k - 1 (classical ladder)")

    print("\n%d checks passed" % CHECKS)


if __name__ == "__main__":
    run()
