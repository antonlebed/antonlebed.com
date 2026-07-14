"""explore_telescope.py — THE TELESCOPE SCAN: is the storey ladder
the Herbrand function's shadow — "one window up" an upper-numbering
transport, the next band's game the (c, m-1) game psi-transported?

THE QUESTION. psi(i) = min(p*i, i+e) drives window game,
pins, and gaps across storeys (the shallow-route general law,
established in explore_shallow_route.py). Is the storey ladder the
HERBRAND FUNCTION's shadow — each storey-j band the (c, m-1) game's
band transported one window up? KILL-SHAPE: the transport fails at a
measured storey — cheapest test the general-m delta-r = 1 pin at (3,1,3).

THE HAND DERIVATION (worked out by hand, frozen and committed
before this file existed).

T1 (THE SCALING BIJECTION). A (c, m-1)-game monomial {(x_l, i_l)}
   maps to {(p*x_l, i_l)} (sizes *p, offsets FIXED): A -> pA
   (j -> j+1), kappa invariant (p-scaling shifts every base-p digit
   one position: identical carry pattern), W -> pW, e = p*e', so
   MASTER gives rel = p*rel' exactly. Backward: a storey-j (c, m)
   monomial with all sizes p-divisible descends by /p; if some part
   has p !| x_l the kappa-mini-lemma (parts == 0 mod p^{j-kappa})
   forces kappa >= j, so
     FLOOR LEMMA: every non-descending storey-j monomial pays
     rel >= rel_j + j*e.
   The first j*e rels of each storey-j band are EXACTLY the
   p-scaled (c, m-1) storey-(j-1) band. Corollaries:
     rel_j(c, m) = p*rel_{j-1}(c, m-1) = p^j * rel_0(c, m-j)
     rel_j(pc, m-1) = rel_{j+1}(c, m)   [the in-field telescope:
     one clock step u -> u^p re-reads the (c, m) game as the
     (pc, m-1) game — same seat, one storey consumed]
   The storey ladder is the game's own psi-orbit.

T2 (GAMMA PRESERVATION — Wilson blocks). (pn)! = p^n * n! * u_n
   with u_n == (-1)^n mod p (each run ((j-1)p+1 .. jp-1) == -1). So
   unit(C(pP'; p*x_1..p*x_l, p(P'-A'))) == unit(C(P'; ...)) *
   (-1)^{P' - Sum x - (P'-A')} = +1 exactly, and v_p (= kappa
   structure) equal. Monomial VALUES are also preserved (digits
   live in F_p: rho^p = rho, s^p = s). So the transported band's
   forced-digit table is VERBATIM the lower game's table; the ONLY
   m-dependence anywhere is the prefactor (-1)^{v_p} =
   (-1)^{m-j+1+kappa} — the pin ladder (-1)^{m+1-j}, already
   storey-consistent.

T3 (THE GENERAL-m delta-r = 1 PIN, M3 redone at general m; scope
   inherited from M3: first band, GATE-OPEN regime — the step
   [w_0]^{m+1} = 1 needs w_0 = 1, and gate-closed slot pins carry
   w_0-powers). Term =
   (-1)^{v_p} * gamma * rho^A * prod s_{i_l}^{x_l}; first band
   j = 0, kappa = 0: prefactor (-1)^{m+1}. delta-r = 1, c = 1
   (monomials ((1,1),) gamma 1 and ((2,0),) gamma -1/2):
   contribution = (-1)^{m+1}(rho*s_1 - rho^2/2); with the fork-1
   value s_1 = -k_1 + rho/2 the rho^2 cancels:
     D_{rel_0+1} = -w_{rel_0+1} + (-1)^m * k_1
   PIN w_{rel_0+1} = (-1)^m * k_1 (m = 2: +k_1, measured in
   explore_shallow_route.py; m = 3: -k_1 — THE KILL TEST). ASSUMPTION
   NAMED: s_1 = -k_1 + rho/2 is m-UNIFORM (the fork system's
   m-blindness, measured at m = 2); a miss at w_137 with a hit at w_136 indicts s_1's
   m-uniformity, not the prefactor. Storey-1 transported twins
   (T1 + T2, positions *p of the m = 2 band):
     w_{rel_1} = (-1)^{m+1-j} = -1;  w_{rel_1 + p} = (-1)^{m-1}*k_1
   (the scaled fork lattice lands on the SAME k_1 = w_{p^m}).

T4 (THE CLASSICAL CONTACT — honest scope). (a) IDENTITY: the clock
   map psi(i) = min(pi, i+e) = p * phi_seat(i), phi_seat the
   two-slope function breaking AT the Kummer seat e/(p-1), slopes
   1 and 1/p — HERBRAND'S SHAPE, not the phi_{L/K} of any single
   degree-p layer (a degree-p break is never divisible by p below
   the extreme — the cutoff law's t = p*i* - delta, p !| delta —
   while p | seat at every m >= 1). The p-power map on higher
   units is classical (Serre-grade); the two gears are the two
   Herbrand slopes. Contact, not novelty.
   (b) THE ANCHOR BREAKS: for K81 = Q_3(zeta_81), hand arithmetic
   gives i_G(sigma_a) = v(zeta^a - zeta) = p^s for a == 1 mod p^s
   exactly (wild layers) and 1 (tame): THE i_G SPECTRUM IS THE
   SEAT LADDER {c*p^j}, the lower breaks one below ({0, 2, 8,
   26}), Serre phi giving upper breaks {0, 1, 2, 3} EQUALLY SPACED — the textbook
   cyclotomic ladder measured in the game's own model. Scope:
   measured at the p = 3 anchor, not a general CFT theorem.

THE PREDICTIONS (fixed and committed
before this file existed; every m = 3 pin line is an m = 2 -> m = 3
TRANSPLANT and every e = 54 diagonal-read line an e = 18 -> e = 54
transplant, NAMED per the standing discipline):

TS-A (symbolic): rel_j(c,m) = p*rel_{j-1}(c,m-1) and
   rel_j(pc,m-1) = rel_{j+1}(c,m) over p in {2,3,5,7}, c in
   1..min(p-1,3), m in 1..4; min(pi, i+e) = p*phi_seat(i) for all
   i in 1..3e.
TS-B (gamma/Wilson): for p in {3,5}, n in {p^2, p^3} (p = 3) /
   {p^2} (p = 5), every part-multiset (<= 3 parts, sum <= n): v_p
   and unit-mod-p of the multinomial equal those of the p-scaled
   multinomial. No exceptions.
TS-C (the monomial-transport bijection): the (3,1,3)@90 census has
   NO storey-0 monomial; its monomials (all j >= 1) = EXACTLY the
   sizes-x3 images of the (3,1,2)@30 census (rel x3, gamma
   preserved); at rel 84: {((3,0),)}; at 87: {((3,1),), ((6,0),)}.
TS-D (K81 word regression; k_1 := w_27 measured in-run, value
   unfrozen): pure holes w_r = 0 at every between rel r in
   (54, 136), v_3(r) = 0, r != 136, and at r in {57, 60, 66, 69,
   75, 78}; pins w_84 = 2, w_87 = k_1, w_136 = 1,
   w_137 = (-k_1) mod 3 [THE KILL TEST].
TS-E (breaks): i_G(sigma_a) = {1, 3, 9, 27, 1} at a = {2, 4, 10,
   28, 80}; i_G value set = {1, 3, 9, 27}; lower breaks
   {0, 2, 8, 26}; phi(2), phi(8), phi(26) = 1, 2, 3.
TS-F (perturbation sticks; each field = K81's eis with ONE
   coefficient bumped; first word difference at the predicted
   diagonal level, stick = 81 + first violated forced rel):
     b_24 += 9  -> first diff 78,  stick 159  (t = 1 pure hole)
     b_30 += 9  -> first diff 84,  stick 165  (storey-1 onset pin)
     b_33 += 9  -> first diff 87,  stick 168  (transported k_1)
     b_26 += 27 -> first diff 134, stick 215  (t = 0 pure hole)
     b_28 += 27 -> first diff 136, stick 217  (storey-0 onset pin)
     b_29 += 27 -> first diff 137, stick 218  (delta-r = 1, KILL)
   K81's own climb-from-floor reaches >= its cap (pool adequacy
   control; a perturbed stick BELOW prediction indicts the pool,
   ABOVE falsifies the pin).
TS-G (provenance): every assert compares measured word/climb
   values; no assert derives its reference through the law under
   test (sticks from climbs, words from w_digits, independently).

THE DESIGN. Machinery imported whole: lc.LF fields, ds.word_of /
land / floor_walker, tr.enumerate machinery via
sr.scope_census / gamma_unit / master_rel, aw.step_pool /
lean_climb via sr.climb_c (mate powers), ad.sample_class. The
anchor K81 = Q_3[x]/(Phi_81(x+1)), zeta_81 = 1 + pi an EXACT sail
witness ((1+pi)^81 = 1 — no climb needed for the sail); climbs use
enriched pools (class-1 census + class-3 and class-9 mates: the
lower-storey defect games fill the G_t neighborhoods at m = 3).
Sections: [S] symbolic identities; [W] the gamma/Wilson sweep;
[M] the transport bijection; [K] the anchor (word regression,
breaks, adequacy control); [P] the six perturbation sticks.
Estimated ~5 min (seven e = 54 pools/climbs dominate), < 100 MB.

Run: python prime/code/explore_telescope.py

FINDINGS (entered post-run, copied from printed output).

1. THE TELESCOPE (T1 + T2 landed whole; the scaling bijection is
   derivation-tier algebra, its census face verified exhaustively
   in range): the (3,1,3)@90 census (cap 4, 55 monomials) is
   BIJECTIVE with the sizes-x3 image of the (3,1,2)@30 census
   (cap 3, 55 monomials) — rel x3, offsets fixed, gamma and v_p
   preserved monomial-for-monomial; no storey-0 monomial in the
   censused range (the 136 onset is a clearance derived in
   explore_shallow_route.py); rel 84 = {((3,0),)}, rel 87 = {((3,1),), ((6,0),)}
   (the x3 shallow pair — explore_shallow_route.py's onset_content t >= 1
   branch listed only ((3,1),); the pair is what the bijection demands and the
   census confirms). The gamma/Wilson lemma held at all 836 (p = 3)
   + 639 (p = 5) part-multisets. With the floor lemma (non-
   descenders pay >= j*e), each storey-j band opens as a VERBATIM
   copy of the (c, m-1) band: the storey ladder is one psi-orbit —
   rel_j(c, m) = p^j * rel_0(c, m-j) and rel_j(pc, m-1) =
   rel_{j+1}(c, m) swept symbolically (90 storey rows).

2. THE GENERAL-m PIN LADDER (rule in range — the anchor + six
   designed perturbations at (3,1,3), all GATE-OPEN like the M3
   derivation; THE KILL TEST PASSED): gate-open the
   pins are w_{rel_j} = (-1)^{m+1-j} and w_{rel_j + p^j} =
   (-1)^{m-j} * k_1 — the fork digit k_1 = w_{p^m} returns at
   EVERY storey with alternating sign. Measured in ONE word: K81
   has k_1 = w_27 = 2 and pins (w_84, w_87, w_136, w_137) =
   (2, 2, 1, 1) = (-1, +k_1, +1, -k_1) exactly; every t = 0 pure
   hole in (54, 136) and every t = 1 pure hole below 84 is zero.
   The six single-coefficient perturbations of Phi_81(x+1) stick
   at 81 + (their violated rel) EXACTLY: sticks (159, 165, 168,
   215, 217, 218) at violated rels (78, 84, 87, 134, 136, 137) —
   the delta-r = 1 kill test is the 218. The diagonal read
   transfers to e = 54: first word difference at i + k*e for a
   b_i += p^{k+1} bump, all six fields.

3. THE HERBRAND CONTACT (the classical name): (a) the clock map is
   p * phi_seat EXACTLY (swept p <= 7, i <= 3e) — the two gears
   are the two Herbrand slopes; (b) K81's ramification filtration,
   measured by direct sigma-action (i_G = v(zeta^a - zeta), all 53
   nontrivial a): i_G = p^s for a == 1 mod p^s exactly — THE i_G
   SPECTRUM IS THE SEAT LADDER {c*p^j}, the lower breaks one
   below ({0, 2, 8, 26}), Serre phi giving upper breaks (1, 2, 3)
   equally spaced.
   The window game is the unit-filtration reading of the
   cyclotomic tower's ramification; the arc's words, pins, and
   designed sticks are the digit-level structure the classical
   objects do not carry. VERDICT: YES — the
   storey ladder is the Herbrand function's shadow, "one window
   up" is the transport (x p positions across windows; one clock
   step in-field), and the next band's game is the (c, m-1) game
   transported VERBATIM (T2: no sign from gamma; the only
   m-dependence in the term structure is the prefactor (-1)^{v_p} —
   the fork values' m-uniformity is the separately MEASURED half,
   T3's named assumption paid by the w_137 hit).

RECORD: first run green — no pre-green failures, the predictions
paid 100% (every TS line, including all named transplants). Note:
k_1(K81) = 2 = k_1(K27) (unexplained — a self-similarity candidate
for the word-atlas census).

RUN RECORD (python prime/code/explore_telescope.py, ~177 s,
exit 0): 362,646 checks (the [S] clock sweep at large e dominates
the count). Printed rows as copied: [S] 90 storey rows; [W] 836 +
639 multisets; [M] caps 4/3, 55 = 55 monomials; [K] k_1 = 2, pins
(2, 2, 1, 1), breaks [0, 2, 8, 26] -> (1, 2, 3); [P] sail witness
exact, K81 climb 222 >= cap 222, sticks 159/165/168/215/217/218 at
first diffs 78/84/87/134/136/137.
"""

import random
from fractions import Fraction
from math import comb

import explore_local_clock as lc
import explore_arrival_defect as ad
import explore_tame_readout as tr
import explore_deep_spectrum as ds
import explore_above_window as aw
import explore_shallow_route as sr

CHECKS = 0


def ok(cond, msg):
    global CHECKS
    if not cond:
        raise AssertionError(msg)
    CHECKS += 1


def vp(x, p):
    if x == 0:
        return 10 ** 9
    v = 0
    while x % p == 0:
        v += 1
        x //= p
    return v


# ------------------------------------------------------------- fields


def phi81_shift():
    """Phi_81(x+1) = (x+1)^54 + (x+1)^27 + 1 (Eisenstein at 3)."""
    eis = [comb(54, i) + (comb(27, i) if i <= 27 else 0)
           for i in range(55)]
    eis[0] += 1
    return eis


# ---------------------------------------------------------------- [S]


def rel_onset(p, c, m, j):
    return c * (p - 1) * p ** m * (m - j) - c * (p ** m - p ** j)


def section_s():
    print("\n[S] the symbolic telescope: ladder scaling, the in-field"
          " step, clock = p*phi_seat")
    rows = 0
    for p in (2, 3, 5, 7):
        for c in range(1, min(p, 4)):
            for m in range(1, 5):
                e = c * (p - 1) * p ** m
                for j in range(m):
                    if j >= 1:
                        ok(rel_onset(p, c, m, j)
                           == p * rel_onset(p, c, m - 1, j - 1),
                           "ladder scaling fails at (%d,%d,%d,j=%d)"
                           % (p, c, m, j))
                    if m >= 2 and j <= m - 1:
                        ok(rel_onset(p, p * c, m - 1, j)
                           == rel_onset(p, c, m, j + 1),
                           "in-field step fails at (%d,%d,%d,j=%d)"
                           % (p, c, m, j))
                    rows += 1
                seat = Fraction(e, p - 1)
                for i in range(1, 3 * e + 1):
                    phi = i if i <= seat else seat + Fraction(i - seat, p)
                    ok(min(p * i, i + e) == p * phi,
                       "clock != p*phi_seat at p=%d e=%d i=%d"
                       % (p, e, i))
    print("  ladder + in-field identities: %d storey rows;"
          " clock = p*phi_seat swept" % rows)


# ---------------------------------------------------------------- [W]


def multi_unit_vp(n, parts, p):
    """(v_p, unit mod p) of the multinomial C(n; parts, n - sum)."""
    M = 1
    rem = n
    for x in parts:
        M *= comb(rem, x)
        rem -= x
    v = vp(M, p)
    return v, (M // p ** v) % p


def section_w():
    print("\n[W] the gamma/Wilson lemma: p-scaling preserves v_p and"
          " the unit part")
    for p, ns in ((3, (9, 27)), (5, (25,))):
        rows = 0
        for n in ns:
            stack = [[]]
            while stack:
                m = stack.pop()
                if m:
                    v1, u1 = multi_unit_vp(n, m, p)
                    v2, u2 = multi_unit_vp(p * n, [p * x for x in m], p)
                    ok((v1, u1) == (v2, u2),
                       "gamma/v_p not preserved: p=%d n=%d %s ->"
                       " (%d,%d) vs (%d,%d)" % (p, n, m, v1, u1, v2, u2))
                    rows += 1
                if len(m) < 3:
                    lo = m[-1] if m else 1
                    for x in range(lo, n - sum(m) + 1):
                        stack.append(m + [x])
        print("  p=%d: %d part-multisets, all preserved" % (p, rows))


# ---------------------------------------------------------------- [M]


def scaled(mono):
    return tuple(sorted((3 * x, i) for x, i in mono))


def section_m():
    print("\n[M] the monomial-transport bijection:"
          " (3,1,3)@90 = x3 of (3,1,2)@30")
    c90, cap90 = sr.scope_census(3, 1, 3, 90)
    c30, cap30 = sr.scope_census(3, 1, 2, 30)
    n90 = sum(len(v) for v in c90.values())
    n30 = sum(len(v) for v in c30.values())
    for r, monos in c90.items():
        for mo in monos:
            A = sum(x for x, i in mo)
            ok(vp(A, 3) >= 1, "storey-0 monomial %s at rel %d <= 90"
               % (mo, r))
    image = {}
    for r, monos in c30.items():
        for mo in monos:
            image.setdefault(3 * r, set()).add(scaled(mo))
            g1 = sr.gamma_unit(3, 2, mo)
            g2 = sr.gamma_unit(3, 3, scaled(mo))
            ok(g1 == g2, "gamma moved: %s %d -> %d" % (mo, g1, g2))
    got = {r: set(monos) for r, monos in c90.items()}
    ok(got == image, "bijection fails: extra %s / missing %s"
       % ({r: got[r] - image.get(r, set()) for r in got
           if got[r] - image.get(r, set())},
          {r: image[r] - got.get(r, set()) for r in image
           if image[r] - got.get(r, set())}))
    ok(got.get(84) == {((3, 0),)}, "rel 84 content %s" % got.get(84))
    ok(got.get(87) == {((3, 1),), ((6, 0),)},
       "rel 87 content %s" % got.get(87))
    print("  censuses: (3,1,3)@90 cap %d, %d monomials; (3,1,2)@30"
          " cap %d, %d monomials — bijective, gamma-preserved"
          % (cap90, n90, cap30, n30))
    print("  rel 84 = {((3,0),)}, rel 87 = {((3,1),), ((6,0),)} (the"
          " x3 shallow pair)")


# ---------------------------------------------------------------- [K]


PURE_T0 = [r for r in range(55, 136) if r % 3 != 0]
PURE_T1 = [57, 60, 66, 69, 75, 78]


def section_k(eis81):
    print("\n[K] the anchor K81 = Q_3(zeta_81): word regression,"
          " breaks, upper numbering")
    w = sr.deep_word("K81", 3, eis81, 140)
    k1 = w[27]
    for r in PURE_T0:
        ok(w[r] == 0, "K81: t=0 pure hole w_%d = %d != 0" % (r, w[r]))
    for r in PURE_T1:
        ok(w[r] == 0, "K81: t=1 pure hole w_%d = %d != 0" % (r, w[r]))
    ok(w[84] == 2, "K81: w_84 = %d != 2 = -1 (storey-1 onset pin)"
       % w[84])
    ok(w[87] == k1, "K81: w_87 = %d != k_1 = %d (transported fork"
       " digit)" % (w[87], k1))
    ok(w[136] == 1, "K81: w_136 = %d != 1 = (-1)^{m+1} (storey-0"
       " onset pin)" % w[136])
    ok(w[137] == (-k1) % 3, "K81: w_137 = %d != -k_1 = %d (THE KILL"
       " TEST)" % (w[137], (-k1) % 3))
    print("  k_1 = w_27 = %d; pins (w_84, w_87, w_136, w_137) ="
          " (%d, %d, %d, %d) — all on cue" % (k1, w[84], w[87],
                                              w[136], w[137]))
    # breaks by direct sigma-action: i_G(a) = v(z^a - z), z = zeta_81
    Fb = lc.LF("K81b", 3, [0, 1], eis81, 60)
    z = [list(c) for c in Fb.one]
    z[1][0] = (z[1][0] + 1) % Fb.pM
    z = tuple(tuple(c) for c in z)
    ig = {}
    for a in range(2, 81):
        if a % 3 == 0:
            continue
        za = ds.epow(Fb, z, a)
        ig[a] = Fb.val(ad.esub(Fb, za, z))
    for a, want in ((2, 1), (4, 3), (10, 9), (28, 27), (80, 1)):
        ok(ig[a] == want, "i_G(sigma_%d) = %d != %d" % (a, ig[a], want))
    ok(set(ig.values()) == {1, 3, 9, 27},
       "i_G value set %s != the seat ladder" % sorted(set(ig.values())))
    for s in (1, 2, 3):
        for a in ig:
            if (a - 1) % 3 ** s == 0 and (a - 1) % 3 ** (s + 1) != 0:
                ok(ig[a] == 3 ** s, "i_G(sigma_%d) = %d != p^%d"
                   % (a, ig[a], s))
    sizes = [1 + sum(1 for a in ig if ig[a] >= t + 1)
             for t in range(0, 28)]
    breaks = [t for t in range(27) if sizes[t] > sizes[t + 1]]
    ok(breaks == [0, 2, 8, 26], "lower breaks %s != [0, 2, 8, 26]"
       % breaks)
    phi, acc = {}, Fraction(0)
    for t in range(1, 28):
        acc += Fraction(sizes[t], sizes[0])
        phi[t] = acc
    ok((phi[2], phi[8], phi[26]) == (1, 2, 3),
       "upper breaks %s != (1, 2, 3)" % ((phi[2], phi[8], phi[26]),))
    print("  i_G: a=2 -> 1 (tame), 1+3u -> 3, 1+9u -> 9, 1+27u -> 27"
          " — the i_G spectrum = the seat ladder")
    print("  lower breaks %s, phi -> upper breaks (1, 2, 3): equally"
          " spaced" % (breaks,))
    return w, k1


# ---------------------------------------------------------------- [P]


TRIALS = [
    (24, 9, 78, 159, "t=1 pure hole"),
    (30, 9, 84, 165, "storey-1 onset pin"),
    (33, 9, 87, 168, "transported k_1 pin"),
    (26, 27, 134, 215, "t=0 pure hole"),
    (28, 27, 136, 217, "storey-0 onset pin"),
    (29, 27, 137, 218, "delta-r = 1 pin (KILL)"),
]

AMAX = 224
CAP = 222


def mates_for(F, rng):
    _, m1 = sr.census_c(F, 1, 81, rng, 120)
    m3 = list(ad.sample_class(F, 3, 50, rng))
    m9 = list(ad.sample_class(F, 9, 50, rng))
    return m1 + m3 + m9


def section_p(eis81, w81, rng):
    print("\n[P] the perturbation sticks: one bumped coefficient, one"
          " violated rel, stick = 81 + rel")
    F81 = lc.LF("K81", 3, [0, 1], eis81, AMAX)
    zeta = [list(c) for c in F81.one]
    zeta[1][0] = (zeta[1][0] + 1) % F81.pM
    zeta = tuple(tuple(c) for c in zeta)
    ok(ds.land(F81, zeta, 81) == F81.CAP,
       "zeta_81 = 1 + pi is not an exact 81st root")
    print("  sail witness: (1 + pi)^81 = 1 exactly (v >= CAP)")
    _, stick = sr.climb_c(F81, 1, 81, rng, mates_for(F81, rng), cap=CAP)
    ok(stick >= CAP, "K81 adequacy control: climb stuck at %d < %d"
       % (stick, CAP))
    print("  K81 climb-from-floor reaches %d >= cap %d (pool adequate"
          " through the zone)" % (stick, CAP))
    for pos, bump, relv, want, label in TRIALS:
        trial = list(eis81)
        trial[pos] += bump
        name = "K81b%d" % pos
        wt = sr.deep_word(name, 3, trial, 140)
        diff = next(i for i in range(141) if wt[i] != w81[i])
        ok(diff == relv, "%s: first word diff at %d != %d (the"
           " diagonal read)" % (name, diff, relv))
        Ft = lc.LF(name, 3, [0, 1], trial, AMAX)
        _, stick = sr.climb_c(Ft, 1, 81, rng, mates_for(Ft, rng),
                              cap=CAP)
        ok(stick == want, "%s (%s): stick %d != %d"
           % (name, label, stick, want))
        print("  b_%d += %d: first diff %d, stick %d = 81 + %d (%s)"
              % (pos, bump, diff, stick, relv, label))


# --------------------------------------------------------------- main


def main():
    import time
    t0 = time.time()
    rng = random.Random(9217)
    eis81 = phi81_shift()
    ok(all(c % 3 == 0 for c in eis81[:54]) and eis81[0] % 9 != 0
       and eis81[54] == 1, "Phi_81(x+1) is not Eisenstein")
    section_s()
    section_w()
    section_m()
    w81, _ = section_k(eis81)
    section_p(eis81, w81, rng)
    print("\nALL %d CHECKS PASS (%.0f s)" % (CHECKS, time.time() - t0))


if __name__ == "__main__":
    main()
