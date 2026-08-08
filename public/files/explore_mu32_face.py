"""explore_mu32_face.py — the e = 16 face: the readout law's
falsification row (the fifth run in the constellation-law depth
series).

THE QUESTION. The readout law predicts the e = 16, f = 1 window of
Q_2 sight-unseen: FOUR arrival classes c*2^m = i* = 16 — (c, m) =
(8, 1), (4, 2), (2, 3), (1, 4), constellations u^2+1 (mu_4), u^4+1
(mu_8), u^8+1 (mu_16), u^16+1 (mu_32) — reading (1, 3, 7, 23) digits
of w = 2/pi^16, with exactly TWO in-window Kummer constants at rel-8
and rel-20 (blind rungs 40/52, matching e = 8's two) and the top
staircase 33..56. Does the window obey the row? The row was fixed in
an earlier run, then self-corrected by EL2's own onset formula in a
later run (see finding 2 below). A miss at rel <= 3 here would
falsify the law outright; a rel >= 4 miss would instead correct a
constant (EL5's fixed form). This is the cheap kill-shot named when
the row was first fixed.

THE HAND DERIVATION (worked by hand before this file existed; the
EL1-EL5 machinery of explore_mu16_face.py is inherited, not
re-derived):

SL1 (classes). Seat i* = e/(p-1) = 16; arrival classes are exactly
    the 2-power starts {1, 2, 4, 8} plus starters at 16 — any other
    class doubles past the seat and never arrives (EL1). Landing
    L = 2e + rel = 32 + rel.
SL2 (the constants, ALL k swept — not only the 2-power binomials).
    v2(C(16,k)) = 4 - v2(k) (Kummer); term C(16,k)t^k sits at
    rel-(16*(3 - v2(k)) + k) for the top class: k = 8 -> rel-8,
    k = 4 -> rel-20, k = 2 -> rel-34, k = 12 -> rel-28, k = 14 ->
    rel-46, k = 6 -> rel-38, odd k -> rel-(48+k). In-window
    (rel < 24): ONLY k = 8 and k = 4. The same onset formula
    rel-((j-1)e + e/2^j) is class-independent (c*2^{m-j} = e/2^j).
    This confirms an earlier correction: TWO in-window constants; the
    j = 3 constant sits at rel-34, PAST the freedom rung 24; the
    once-proposed third blind rung "26" was e = 8's absolute register.
SL3 (freedom, EL4 at e = 16). rho_i enters at rel-min(2^m*i,
    e/2 + 2^{m-1}*i), the two entries coinciding + pair-cancelling
    at i = c. Top class (c = 1, m = 4): rho_1 both routes at rel-16,
    cancelled; rho_2 at rel-24 = 3e/2 — window 23. Intermediate
    (c > 1): rho_1 survives at rel-2^m — windows 1, 3, 7.

THE PREDICTIONS (fixed before the run; labels never read orbits;
falsification form per EL5):

SX1 (the lock): w1 = 1 <=> min spec_c = 33 for all c in {8, 4, 2, 1},
    all four arrival spectra rigid {33}; starters floor 33, graded.
SX2 (the m = 1 law): w1 = 0 => min spec8 = 34 = p(i*+1).
SX3 (m = 2): min spec4 = 32 + first-stop of (w1; w2; w3; free at 4) —
    rigid 33/34/35, floor 36 graded.
SX4 (m = 3): min spec2 = 32 + first-stop of (w1..w7; free at 8) —
    rigid 33..39, floor 40 graded.
SX5 (m = 4, THE HEADLINE): min spec1 = 32 + first-stop of (w1..w7;
    w8+1; w9..w19; w20+1; w21; w22; w23; free at 24) — a function of
    w1..w23 alone, rigid at every rung <= 55, freedom dodge 56, CAP
    iff zeta32 in K. Window 23 = 3e/2 - 1.
SX6 (the blind rungs): pure sixteenics x^16 - d have w in Q_2 odd, so
    w1..w15 = 0: spec1 = {40} RIGID (the game stops on its own
    12870-term). The second blind rung is 52 = 32 + 20; there is NO
    third in-window constant.
SX7 (the anchor): Phi32(x+1), zeta32 = 1 + pi exact: digit vector
    (w1..w23) = (0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0) —
    the unique no-stop walk, forced by zeta32 in K + SX5; landings
    starters 33, spec8 min 34 + CAP, spec4 min 36 + CAP, spec2 min
    40 + CAP, spec1 min 56 + CAP (torsion tower zeta32, zeta16 =
    zeta32^2, zeta8, i).
SX8 (the readout row): the four windows (m = 1..4) = (1, 3, 7, 23) =
    (2^m - 1 at m <= 3, 3e/2 - 1 at the top) — the third censused
    multi-class 2-power window (after e = 4, 8), the fourth point on
    the top-readout line; the readout grows linearly in e.

THE DESIGN. Machinery inherited: LF (explore_local_clock), w/digit
extraction any-e (explore_mu16_face; per-digit halving verified
lossless — the division is by pi, not 2, confirmed by a separate
digit-by-digit check, digits identical at M = 7/20/28/53), sampled
spectra + psi-gear sanity (explore_mu16_face.sampled_spec), class sampling
(explore_arrival_defect). [0] THE SCAN: a seeded random sample
(2500 of the 196,608-member family [d, 2c1..2c15, 1],
d in {+-2, +-6, +-10}, c_i in {0, 1}) — digits w1..w23 exact
(reconstruction self-checked), predicted rungs, coverage histogram;
no silent caps: the sample size is printed, unrealized rungs go to
[1]. [1] DESIGNED BACKFILL (the readout law read backwards — random
search is hopeless past ~rel-9): sparse Eisenstein families place a
chosen stop — x^16 + 2b x^j - 2mu lands rung 32+j (j = 1..7); adding
2b2 x^8 passes the rel-8 constant for rungs 41..47; mu mod 4 tunes
the rel-16 digit (two odd contributions carry e levels deeper) for
rungs 48/52; 4c x^i terms land rel-(16+i) for 49..51; 4c x^4 feeds
rel-20 to pass the second constant, + 4c2 x^{4+i} for 53..55 and the
designed no-stop walk 56. The engine only ever MEASURES digits and
applies the fixed ladder — design steers coverage, never the read.
Rungs still unrealized after the grid are printed (no silent caps).
[2] THE CENSUS: one witness per realized rung + all six pure
sixteenics — sampled falsify-outright at amax 64 (250 units per class
in {1, 2, 4, 8, 16}, seeded rng, psi-gear sanity on every orbit):
minima, rigidity, the lock, floors per slate. [3] THE ANCHOR:
Phi32(x+1), zeta32 = 1 + pi exact — digits, landings, CAP rows via
exact torsion. [4] INVARIANCE: one witness per censused rung x three
alternative uniformizers pi' = pi*eta — stop position and pre-stop
digit prefix on the digits of 2/pi'^16 in base pi' (the invariance
protocol from explore_mu16_face.py, applied here at e = 16).
Run: python prime/code/explore_mu32_face.py

FINDINGS (entered post-run, copied from printed output).

1. THE MU_32 RUNG LADDER (rule in range; the headline, SX5): at every
   censused e = 16, f = 1 window of Q_2 (30 sixteenics + zeta32) the
   class-1 (mu_32) landing minimum is a FUNCTION of the canonical
   digits w1..w23 of w = 2/pi^16 alone, following the staircase
   L1 = 33..56 at the first stop of (w1..w7; w8+1; w9..w19; w20+1;
   w21; w22; w23; freedom at rel-24), spectra RIGID at every rung
   <= 55 — all TWENTY-FOUR rungs realized and hit (scan: 33-43, 46,
   52 in-sample, counts roughly halving 1252/641/278/174/75/39/19/12
   at rungs 33-40; the deep rest by designed witnesses). The deepest
   class reads twenty-three digits of the wild prime.

2. THE ROW CONFIRMED (rule in range across e = 2, 4, 8, 16 + the
   e = 12 offsets; SX8): the four windows at e = 16 are (m = 1..4) =
   (1, 3, 7, 23) = (2^m - 1 at m <= 3, 3e/2 - 1 at the top) —
   exactly the row fixed in an earlier run and self-corrected in a
   later run by EL2's own onset formula, confirmed sight-unseen.
   A miss at rel <= 3 would have falsified the readout law; none
   occurred at any of the 31 censused fields. The top readout's
   linear growth in e now stands
   at four 2-power windows: 2, 5, 11, 23 digits at e = 2, 4, 8, 16.

3. THE TWO BLIND RUNGS (rule in range; SX6 + SL2): the in-window
   Kummer constants of (1+t)^16 sit at rel-8 (C(16,8) = 12870,
   v2 = 1) and rel-20 (C(16,4) = 1820, v2 = 2) ONLY — the j = 3
   constant (C(16,2) = 120, v2 = 3) onsets at rel-34, past the
   freedom rung 24, and SL2's all-k sweep puts every non-2-power
   binomial out-of-window (k = 12, 14 at rel-28/46; odd k at
   rel-(48+k)). All six pure sixteenics (w in Q_2 odd: w1..w15 = 0)
   collapse at spec1 = {40} rigid; the rung-52 witness x^16+2x^8-6
   stops on its own 1820-term. Two blind rungs, matching e = 8's two
   — the once-proposed third ("26") was e = 8's absolute register,
   killed in an earlier run and confirmed dead here.

4. THE DESIGNED READOUT (rule in range for stop placement; the law
   read backwards): sparse Eisenstein families PLACE the stop —
   x^16 + 2b x^j - 2mu lands rung 32+j (j <= 7); adding 2b2 x^8
   passes the rel-8 constant (41..47); mu mod 4 tunes the rel-16
   digit through the carry (48 at mu = 1 mod 4, 52 at mu = 3 mod 4);
   4c x^i feeds rel-(16+i) (49..51); 4c x^4 passes rel-20 (53..56).
   Every target hit within <= 9 grid tries, engine always reading
   the ladder off measured digits (design steers coverage, never the
   read). The designed-readout idea, proposed but left untried in an
   earlier run, is realized here at the STOP level; printing a full
   chosen digit VECTOR stays untested.

5. THE ANCHOR (rule in range; SX7): zeta32's digit vector is
   (0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0) — the unique
   no-stop walk, nonzero exactly on the Kummer skeleton — with
   landings starters 33, spec8 min 34, spec4 min 36, spec2 min 40,
   spec1 min 56, CAP present in all four arrival specs via exact
   torsion (zeta32 = 1 + pi; i^2 = -1 = zeta32^16; zeta8^2 = i).

6. THE THREE SHALLOW LAWS + THE LOCK (rule in range; SX1-SX4): the
   m = 1 law persists (class-8 floor 34 = p(i*+1) at every w1 = 0
   field), the class-4 ladder reads (w1; w2; w3) with floor 36, the
   class-2 ladder (w1..w7) with floor 40, starters land 33 = p*i*+1
   at all 31 fields; w1 = 1 locks all four arrival classes rigid
   {33} (orbit-censused at the rung-33 witness; w1 = 1 holds at
   1252/2500 of the seeded sample — half, as at e = 4 and 8).

7. THE BASE-FREEDOM (rule in range; section [4]): stop position and
   pre-stop digit prefix are UNIFORMIZER-INVARIANT at all 24 rungs
   x 3 alternative uniformizers (post-stop digits flip 3/3 at
   shallow rungs; 0/3 at the deep sparse witnesses 48/52/54/55/56,
   where the sparse fields' post-stop digits happen not to move).

PRE-GREEN FAILURES: none — green on the first complete run. The
one exposed constant row (rel-8/20) had already been resolved in an
earlier round, where EL2's own onset formula killed the previously
proposed third constant before any code for this script existed — so
the usual adjudication between prediction and code had nothing left
to arbitrate this time.

RUN RECORD (python explore_mu32_face.py, ~43 s, exit 0): 225,983
checks passed (370 this module + 225,613 in the imported machinery;
gear sanity dominates: 38,750 sampled orbits — 31 censused fields x
5 classes x 250 — with per-step asserts; digit reconstruction
self-checked at every scan/census/invariance extraction). Scan
histogram (2500 seeded of 196,608): {33: 1252, 34: 641, 35: 278,
36: 174, 37: 75, 38: 39, 39: 19, 40: 12, 41: 4, 42: 1, 43: 3,
46: 1, 52: 1}. Designed witnesses as printed: 44/45/47 =
[-2,2@8,2@(12/13/15)], 48 = x^16+2x^8-2, 49/50/51 =
[-6,4@(1/2/3),2@8], 52 = x^16+2x^8-6, 53/54/55 =
[-6,4@4,4@(5/6/7),2@8], 56 = [-6,4@4,2@8]. zeta32 landings:
1->{56,CAP} 2->{40,52,56,60,CAP} 4->{36,40,44,50,52,54,...}
8->{34,36,38,40,42,44,...} 16->{33,34,35,36,37,38,...}.
"""

import random

import explore_local_clock as lc
import explore_arrival_defect as ad
import explore_mu8_grading as mu8
import explore_mu16_face as m16

CHECKS = 0


def ok(cond, msg):
    global CHECKS
    if not cond:
        raise AssertionError(msg)
    CHECKS += 1


E = 16
NDIG = 24


# ------------------------------------------------------------ the ladders


def rung1_16(digs):
    """Top class (mu_32, m = 4) predicted min: stops (w1..w7; w8+1;
    w9..w19; w20+1; w21; w22; w23), freedom at rel-24 (SX5)."""
    for k in range(1, NDIG):
        s = (1 - digs[k]) if k in (8, 20) else digs[k]
        if s:
            return 32 + k
    return 56


def rung2_16(digs):
    """Class-2 (mu_16, m = 3) predicted min: stops (w1..w7), free at 8."""
    for k in range(1, 8):
        if digs[k]:
            return 32 + k
    return 40


def rung4_16(digs):
    """Class-4 (mu_8, m = 2) predicted min: stops (w1; w2; w3), free 4."""
    for k in (1, 2, 3):
        if digs[k]:
            return 32 + k
    return 36


def rung8_16(digs):
    """Class-8 (mu_4, m = 1) predicted min: stop (w1), freedom rel-2."""
    return 33 if digs[1] else 34


# ------------------------------------------------------------ census bits


def digit_field(name, eis):
    """Digit-only twin (amax 32): w + 23 digits, reconstruction-checked."""
    F = lc.LF(name, 2, [0, 1], eis, 32)
    w = m16.w_element_g(F)
    digs = m16.w_digits_g(F, w, n=NDIG)
    return F, w, digs


def census_field_16(name, eis, rng, amax=64, per_class=250):
    F = lc.LF(name, 2, [0, 1], eis, amax)
    w = m16.w_element_g(F)
    digs = m16.w_digits_g(F, w, n=NDIG)
    spec = m16.sampled_spec(F, rng, (1, 2, 4, 8, 16), per_class)
    return F, w, digs, spec


def check_slate_16(name, digs, spec):
    """SX1-SX5 assertions common to every censused e = 16 field."""
    p1, p2 = rung1_16(digs), rung2_16(digs)
    p4, p8 = rung4_16(digs), rung8_16(digs)
    s1, s2 = spec.get(1, set()), spec.get(2, set())
    s4, s8 = spec.get(4, set()), spec.get(8, set())
    s16 = spec.get(16, set())
    ok(min(s1) == p1, "%s: class-1 min %s != pred %d" % (name, sorted(s1), p1))
    ok(min(s2) == p2, "%s: class-2 min %s != pred %d" % (name, sorted(s2), p2))
    ok(min(s4) == p4, "%s: class-4 min %s != pred %d" % (name, sorted(s4), p4))
    ok(min(s8) == p8, "%s: class-8 min %s != pred %d" % (name, sorted(s8), p8))
    ok(min(s16) == 33, "%s: starter floor %s != 33" % (name, sorted(s16)))
    if p1 < 56:
        ok(s1 == {p1}, "%s: class-1 spectrum %s not rigid" % (name, s1))
    if p2 < 40:
        ok(s2 == {p2}, "%s: class-2 spectrum %s not rigid" % (name, s2))
    if p4 < 36:
        ok(s4 == {p4}, "%s: class-4 spectrum %s not rigid" % (name, s4))
    if digs[1]:
        ok(s2 == {33} and s4 == {33} and s8 == {33},
           "%s: the lock — spectra %s %s %s not {33}" % (name, s2, s4, s8))
        ok(len(s16) > 1, "%s: starter spectrum unexpectedly rigid" % name)
    return p1


# ------------------------------------------------------------------- zoo

D_SET = (-2, 2, -6, 6, -10, 10)

PURE = [(d,) + (0,) * 15 for d in D_SET]

PHI32 = [2, 16, 120, 560, 1820, 4368, 8008, 11440, 12870,
         11440, 8008, 4368, 1820, 560, 120, 16, 1]


def poly_name(key):
    nz = [(j, c) for j, c in enumerate(key) if c and j > 0]
    s = "[%d" % key[0]
    for j, c in nz:
        s += ",%d@%d" % (c, j)
    return s + "]"


def designed_candidates(r, rng):
    """Sparse-family candidates for target rung r (from the hand
    derivation worked before this file existed).
    Yields eis coefficient tuples (length 16, without the leading 1)."""
    MUS = (1, 3, 5, 7, 9, 11, 13, 15)
    BS = (1, 3)
    if 33 <= r <= 39:                       # stop rel-(r-32) via 2b x^j
        j = r - 32
        for mu in MUS:
            for b in BS:
                key = [-2 * mu] + [0] * 15
                key[j] = 2 * b
                yield tuple(key)
    elif 41 <= r <= 47:                     # pass rel-8, stop rel-(r-32)
        j = r - 32
        for mu in MUS:
            for b in BS:
                for b2 in BS:
                    key = [-2 * mu] + [0] * 15
                    key[8] = 2 * b2
                    key[j] = 2 * b
                    yield tuple(key)
    elif r == 40:                           # the first blind rung: pure
        for d in D_SET:
            yield (d,) + (0,) * 15
    elif r in (48, 52):                     # rel-16 digit tuned by mu
        for mu in MUS:
            for b in BS:
                key = [-2 * mu] + [0] * 15
                key[8] = 2 * b
                yield tuple(key)
    elif 49 <= r <= 51:                     # 4c x^i lands rel-(16+i)
        i = r - 48
        for mu in MUS:
            for b in BS:
                for c in BS:
                    key = [-2 * mu] + [0] * 15
                    key[8] = 2 * b
                    key[i] = 4 * c
                    yield tuple(key)
    elif 53 <= r <= 55:                     # pass rel-20 via 4c x^4
        i = r - 52
        for mu in MUS:
            for b in BS:
                for c in BS:
                    for c2 in BS:
                        key = [-2 * mu] + [0] * 15
                        key[8] = 2 * b
                        key[4] = 4 * c
                        key[4 + i] = 4 * c2
                        yield tuple(key)
    elif r == 56:                           # the designed no-stop walk
        for mu in MUS:
            for b in BS:
                for c in BS:
                    key = [-2 * mu] + [0] * 15
                    key[8] = 2 * b
                    key[4] = 4 * c
                    yield tuple(key)
    # fallback: seeded random four-term perturbations
    for _ in range(300):
        key = [-2 * rng.choice(MUS)] + [0] * 15
        for _ in range(rng.randrange(1, 4)):
            key[rng.randrange(1, 16)] = 2 * rng.randrange(1, 8)
        yield tuple(key)


def run():
    rng = random.Random(190)
    print("THE E = 16 FACE — the readout law's falsification row")
    print("=" * 68)

    # [0] the scan: seeded random sample of the sixteenic family
    SAMPLE = 2500
    print("\n[0] the scan: %d seeded of the 196,608 family, digits -> rungs"
          % SAMPLE)
    seen_keys = set()
    while len(seen_keys) < SAMPLE:
        d = rng.choice(D_SET)
        bits = rng.randrange(1 << 15)
        seen_keys.add((d, bits))
    by_rung = {}
    for d, bits in sorted(seen_keys):
        key = tuple([d] + [2 * ((bits >> k) & 1) for k in range(15)])
        F, w, digs = digit_field(poly_name(key), list(key) + [1])
        by_rung.setdefault(rung1_16(digs), []).append(key)
    hist = {r: len(v) for r, v in sorted(by_rung.items())}
    print("    rung histogram (sample): %s" % hist)

    # [1] designed backfill for unrealized rungs
    missing = [r for r in range(33, 57) if r not in by_rung]
    print("\n[1] designed backfill for rungs %s" % missing)
    for r in list(missing):
        found = None
        tried = 0
        for key in designed_candidates(r, rng):
            tried += 1
            F, w, digs = digit_field(poly_name(key), list(key) + [1])
            if rung1_16(digs) == r:
                found = key
                break
        if found is not None:
            by_rung.setdefault(r, []).append(found)
            missing.remove(r)
            print("    rung %d witness (try %d): %s"
                  % (r, tried, poly_name(found)))
    if missing:
        print("    STILL UNREALIZED: %s" % missing)
    else:
        print("    all 24 rungs 33..56 realized")

    # [2] the census: one witness per realized rung + the pure sixteenics
    print("\n[2] the census: sampled falsify-outright, amax 64, 250/class")
    print("    %-24s %-23s %-4s %-4s %-4s %-4s %-4s %-5s"
          % ("field", "w1-w23", "pred", "L1", "L2m", "L4m", "L8m", "start"))
    witnesses = [by_rung[r][0] for r in sorted(by_rung)]
    for key in PURE:
        if key not in witnesses:
            witnesses.append(key)
    rung_witness = {}
    for key in witnesses:
        name = poly_name(key)
        F, w, digs, spec = census_field_16(name, list(key) + [1], rng)
        p1 = check_slate_16(name, digs, spec)
        rung_witness.setdefault(p1, (key, digs))
        if key in PURE:
            ok(digs[1:16] == [0] * 15,
               "%s: pure sixteenic digits w1..w15 not zero" % name)
            ok(p1 == 40 and spec[1] == {40},
               "%s: blind rung %s" % (name, spec[1]))
        print("    %-24s %-23s %-4d %-4d %-4d %-4d %-4d %-5d"
              % (name, "".join(str(x) for x in digs[1:NDIG]), p1,
                 min(spec[1]), min(spec[2]), min(spec[4]), min(spec[8]),
                 min(spec[16])))
    F, w, digs = digit_field("x16-2", [-2] + [0] * 15 + [1])
    ok(m16.F_is_one(F, w), "x16-2: w != 1")
    print("    censused fields: %d (rungs realized: %s)"
          % (len(witnesses), sorted(rung_witness)))

    # [3] the anchor: Q2(zeta32)
    print("\n[3] the anchor: Phi32(x+1), zeta32 = 1 + pi exact")
    F, w, digs, spec = census_field_16("zeta32", PHI32, rng)
    target = [0] * NDIG
    target[0] = 1
    target[8] = 1
    target[20] = 1
    ok(digs == target, "zeta32: digit vector %s" % digs[1:NDIG])
    print("    digits w1..w23 = %s (the no-stop walk — SX7)"
          % "".join(str(x) for x in digs[1:NDIG]))
    z32 = [list(F.zero_c) for _ in range(F.e)]
    z32[0][0] = 1
    z32[1][0] = 1
    z32 = tuple(tuple(c) for c in z32)
    z16 = F.emul(z32, z32)
    z8 = F.emul(z16, z16)
    i_el = F.emul(z8, z8)
    ok(F.val(ad.esub(F, F.emul(i_el, i_el), ad.const_el(F, -1))) == F.CAP,
       "zeta32: i^2 != -1 (z32^16 = i^2 != -1)")
    ok(F.val(ad.esub(F, F.emul(z8, z8), i_el)) == F.CAP,
       "zeta32: zeta8^2 != i")
    for u, c in ((z32, 1), (z16, 2), (z8, 4), (i_el, 8)):
        ok(F.val(F.esub1(u)) == c, "zeta32: torsion class %d" % c)
        o = F.orbit(u)
        n = o.index(F.seat)
        spec.setdefault(c, set()).add(o[n + 1])
        ok(o[n + 1] >= F.CAP, "zeta32: torsion class %d not CAP" % c)
    p1 = check_slate_16("zeta32", digs, spec)
    ok(p1 == 56 and min(spec[1]) == 56, "zeta32: class-1 56")
    ok(min(spec[2]) == 40 and min(spec[4]) == 36 and min(spec[8]) == 34,
       "zeta32: SX7 floors")
    for c in (1, 2, 4, 8):
        ok(any(v >= F.CAP for v in spec[c]),
           "zeta32: CAP missing in spec%d" % c)
    print("    landings: %s (SX7 floors 33/34/36/40/56 + CAP rows)"
          % ad.fmt_spec(F, spec))

    # [4] uniformizer invariance of the stop position
    print("\n[4] invariance: one witness per rung x 3 uniformizers")
    for r in sorted(rung_witness):
        key, digs0 = rung_witness[r]
        name = poly_name(key)
        F = lc.LF(name, 2, [0, 1], list(key) + [1], 32)
        w = m16.w_element_g(F)
        pi = mu8.pi_el(F)
        stop = r - 32 if r < 56 else 24
        flips = 0
        for et in ((1, 1), (2, 1), (1, 1, 1, 1)):
            eta = [list(F.zero_c) for _ in range(F.e)]
            eta[0][0] = 1
            for j, cc in enumerate(et, start=1):
                eta[j][0] = cc
            eta = tuple(tuple(c) for c in eta)
            pip = F.emul(pi, eta)
            e16 = F.one
            for _ in range(E):
                e16 = F.emul(e16, eta)
            wp = F.emul(w, mu8.unit_inv(F, e16))
            digsp = m16.digits_g(F, wp, pip, n=NDIG)
            ok(rung1_16(digsp) == r,
               "%s: rung moved under uniformizer change" % name)
            ok(digsp[1:stop + 1] == digs0[1:stop + 1],
               "%s: pre-stop digit prefix moved" % name)
            if digsp[1:NDIG] != digs0[1:NDIG]:
                flips += 1
        print("    rung %d (%s): stop invariant, %d/3 variants flip"
              " post-stop digits" % (r, name, flips))

    total = CHECKS + m16.CHECKS + mu8.CHECKS + ad.CHECKS + lc.CHECKS
    print("\nALL CHECKS PASSED: %d (this module %d; imported machinery "
          "%d)" % (total, CHECKS, total - CHECKS))


if __name__ == "__main__":
    run()
