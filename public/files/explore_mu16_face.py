"""explore_mu16_face.py — the e = 8 three-layer face: the mu_16 rung
ladder in the constellation-law family.

THE QUESTION (the natural follow-up to explore_mu8_grading.py's
mu_8 staircase). An e = 8, f = 1 window of Q_2 carries THREE arrival
classes: c*2^m = i* = 8 gives (c, m) = (4, 1), (2, 2), (1, 3) —
constellations u^2 + 1 (mu_4), u^4 + 1 (mu_8), u^8 + 1 (mu_16), one
per cyclotomic layer. (1) Does the class-1 landing grade K(zeta16)/K
the way the mu_8 staircase graded K(zeta8)/K at e = 4? (2) How many
digits of w = 2/pi^8 does each class read before unit freedom — is
there a digit-count law in m? (3) Do the rungs sit as filtration
breaks (the Hasse-Herbrand shape, explore_mu8_grading.py finding 6)?

THE HAND LEMMAS (derived before this file existed):

EL1 (orbit rigidity). Class-1 orbits are rigidly (1, 2, 4, 8, L1):
    v(u^2+1) = 2 and v(u^4+1) = 4 are forced below the seat. Class-2:
    (2, 4, 8, L2); class-4: (4, 8, L4); starters (8, L8). L = 8 + A,
    A_m = v(u^{2^m} + 1). At e = 12 the arrival set is {6, 3} ONLY —
    classes 1, 2, 4, 8 jump 8 -> 16 past the seat and never arrive.

EL2 (the direct-binomial machine). u^{2^m} + 1 = 2 + sum C(2^m,k)t^k
    with v2(C(2^m, 2^{m-j})) = j (Kummer), so after /pi^e the j-term
    onsets at rel-((j-1)e + e/2^j) and carries base-digit rho_i at
    rel-((j-1)e + e/2^j + 2^{m-j}i); the pure-power term puts rho_i
    at rel-2^m*i, its square-cross carry at rel-(e + 2^{m-1}i).
    Validated: the machine re-derives the CORRECTED e = 4 ladder
    (w1; w2+1; w3; w4; w5+1; free at 6) including the rel-4 = w4
    constant explore_mu8_grading.py's engine corrected and rung 13 =
    (0,1,0,0,0).

EL3 (the e = 8 ladders). Class-4 (m = 1): stops (w1; free at 2) —
    rungs 17, floor 18 = p(i*+1). Class-2 (m = 2): stops (w1; w2;
    w3; free at 4) — rungs 17/18/19 rigid, floor 20. Class-1
    (m = 3): stops (w1; w2; w3; w4+1; w5; w6; w7; w8; w9; w10; w11;
    free at 12) — rungs 17..27 rigid, freedom dodge 28, CAP iff
    zeta16 in K. Rigid-window lengths (1, 3, 11).

EL4 (THE CANCELLATION LAW -> THE READOUT LAW). Base digit rho_i
    enters at rel-min(2^m*i, e/2 + 2^{m-1}*i); the two entries
    COINCIDE and pair-cancel exactly at i = c = e/2^m — the class's
    own index digit is forced out of its game. Intermediate classes
    (c > 1): rho_1 survives at rel-2^m — window 2^m - 1 digits,
    layer-intrinsic, independent of e. The top class (c = 1): rho_1
    pair-cancels (its re-entries at rel-3e/2 cancel on-branch via
    the forced rel-e/2 constant), rho_2 enters at rel-3e/2 — window
    3e/2 - 1 digits, the 1.5x bonus exclusive to 2-power e. Checks:
    e=2 top window 2 (explore_arrival_defect.py), e=4 windows (1, 5)
    (explore_mu8_grading.py), e=8 windows (1, 3, 11) (this engine),
    e=12 top class c = 3 odd: NO bonus, window 3 (this engine, TL9).

EL5 (the carry law, ML5 carried over). F_2-xor of series is invalid
    (1 + 1 carries e levels: 2*pi^k = pi^(k+e)*w). Per-field
    predictions come from exact ring arithmetic on the field's own
    expansion of 2; the ladder constants at rel >= 4 are frozen as
    the falsifiable form — a miss at rel <= 3 falsifies the law, a
    miss at rel >= 4 corrects a constant (an upgraded miss, the
    explore_class_gap.py / explore_mu8_grading.py precedent).

THE SLATE (frozen and hand-attacked before this file existed;
labels never read orbits):

TL1 (the lock): w1 = 1 <=> min spec1 = 17 <=> min spec2 = 17 <=> min
    spec4 = 17, and then all three arrival spectra are rigid {17};
    starters keep floor 17 with a graded spectrum (the seat dodge).
TL2 (the m = 1 law persists): w1 = 0 => min spec4 = 18 = p(i*+1).
TL3 (the m = 2 ladder): min spec2 = 16 + first-stop of (w1; w2; w3;
    free at 4): rungs 17/18/19 with rigid spectra, floor 20 graded.
TL4 (the m = 3 ladder — THE HEADLINE): min spec1 = 16 + first-stop
    of (w1; w2; w3; w4+1; w5; w6; w7; w8; w9; w10; w11; free at 12):
    a FUNCTION of w's canonical digits w1..w11 alone across the
    census, spectra RIGID (single-valued) at every rung <= 27,
    freedom dodge 28, CAP tail iff zeta16 in K.
TL5 (the blind rung): all six pure octics x^8 - d (w = 1/mu' in
    1 + 2Z_2: w1..w7 = 0): spec1 = {20} RIGID (the game stops on its
    own 70-term), spec2 floor 20 graded, spec4 floor 18, starters 17.
TL6 (the zeta16 anchor): digit vector (w1..w11) =
    (0,0,0,1,0,0,0,0,0,0,0) — the unique no-stop walk, predicted
    from explore_arrival_defect.py's measured 28 + the ladder;
    landings replicate explore_arrival_defect.py's AD6: starters 17,
    spec4 min 18 CAP present, spec2 min 20 CAP present, spec1 min 28
    CAP present.
TL7 (THE READOUT LAW): the three windows are (m = 1, 2, 3) =
    (1, 3, 11) = (2^1 - 1, 2^2 - 1, 3e/2 - 1) digits of 2/pi^8.
TL8 (dictionary rows): (a) CAP in spec-c <=> the layer's torsion in
    K (c = 4: i; c = 2: zeta8; c = 1: zeta16) — asserted exactly at
    the anchor (torsion constructed), and in the sampled direction
    (CAP seen => split label) at sweep witnesses; (b) rung 17 => no
    split label (i in K would put CAP in spec4, contradicting rigid
    {17}); (c) by construction: x^8-2 has 2 = (pi^4)^2 split (w = 1
    exactly), x^8+2 has -2 split (w = -1).
TL9 (the no-bonus probe): x^12 - 2: seat-passing classes are a
    subset of {6, 3, 12}; starters floor 25 = p*i*+1; class-6
    (m = 1) floor 26; class-3 (m = 2, the TOP layer with c = 3 odd)
    floor 28 = 2e + 4 — window 3, not 3e/2 - 1 = 17: the 1.5x bonus
    needs c = 1.
LABELS (orbit-free; delta = 2m tests m*w against unit squares since
    2 = pi^8*w and pi^8 is a square): split iff sq(delta) > 2e = 16
    over exhaustive U_1/U_17 representatives; guard sq(5) <= 16
    (no unramified subextension in a totally ramified octic).
    Scope (budget-frozen): the full triple at the first rung-17
    witness (TL8b) + the constructive rows (TL8c) + lazy at any sweep
    witness whose sampled spectrum shows CAP (TL8a coherence);
    the anchor's labels come from exact torsion, no search.

THE DESIGN. LF machinery of explore_local_clock; helpers imported
from explore_arrival_defect and explore_mu8_grading (w_element and
digit extraction generalized here to any e). [0] THE SCAN: all 768
Eisenstein octics [d, 2c1..2c7, 1], d in {+-2, +-6, +-10}, c_i in
{0, 1} — digits w1..w11 extracted exactly (independent side only,
reconstruction self-checked), predicted rungs per ladder, coverage
histogram; a randomized backfill search (seeded, coefficients up to
6, |d| <= 14) hunts witnesses for any unrealized rung and reports
what stays missing (no silent caps). [1] THE CENSUS: per realized
class-1 rung, two scan-order witnesses (+ all six pure octics),
SAMPLED falsify-outright at amax = 32 (400 units per class in
{1, 2, 4, 8}, seeded rng, psi-gear sanity on every orbit): minima
and rigidity per slate. [2] LABELS at the frozen scope. [3] THE
ANCHOR: Phi16(x+1), zeta16 = 1 + pi exact (x^8 + 1 asserted 0),
zeta8 = zeta16^2, i = zeta16^4 — digits, landings, CAP rows both
ways. [4] THE PROBE: x^12 - 2 at amax = 32, classes {1..4, 6, 8,
12} sampled. [5] INVARIANCE: one witness per censused rung x three
alternative uniformizers pi' = pi*eta — the ladder's stop position
and pre-stop digit prefix on the digits of 2/pi'^8 in base pi'
(explore_mu8_grading.py finding-6 protocol at e = 8).
Run: python prime/code/explore_mu16_face.py

FINDINGS (entered post-run, copied from printed output; tiers
below).

1. THE MU_16 RUNG LADDER (rule in range; the headline, TL4): at every
   censused e = 8, f = 1 window of Q_2 (26 Eisenstein octics + zeta16)
   the class-1 (mu_16) landing minimum is a FUNCTION of the canonical
   digits w1..w11 of w = 2/pi^8 alone, following the staircase
   L1 = 17..28 at the first stop of (w1; w2; w3; w4+1; w5; w6; w7;
   w8; w9; w10+1; w11; freedom at rel-12), spectra RIGID at every
   rung <= 27 — all twelve rungs REALIZED and hit exactly (in-family:
   384/192/96/48/24/12/6/3 at rungs 17-24, halving rung by rung, plus
   3 at the blind rung 26; 25, 27, 28 realized by backfill witnesses
   with coefficients up to 6). The deepest class reads ELEVEN digits
   of the wild prime.

2. THE TWO BLIND RUNGS (rule in range; the adjudicated correction):
   the ladder's +1 constants sit at rel-4 and rel-10 = the KUMMER
   SKELETON of (1 + t)^8 — the j-th binomial C(8, 2^{3-j}) t^{2^{3-j}}
   has v_2 = j and lands at rel-((j-1)e + e/2^j): j = 1 (70t^4) at
   rel-4, j = 2 (28t^2) at rel-10. Where the window's own digit is
   silent (w4 = 0 / w10 = 0) the game stops on its own term: rungs 20
   and 26 are blind buckets (all six pure octics collapse at 20; the
   i-fields x^8+2x^4+2 and x^8+2x^4-6 sit at 26), and the no-stop
   walk must MATCH the skeleton (w4 = 1 AND w10 = 1) to reach the
   freedom rung 28. At e = 4 only j = 1 exists — the U_3 bucket at
   rung 10 was the same phenomenon one layer down.
   (A later run CORRECTS the last sentence: j = 2 exists at e = 4
   too (C(4,1) = 4t, v_2 = 2, at rel-5 = 5e/4: exactly
   explore_mu8_grading.py's measured 1 - w_5 ladder slot), so e = 4's
   blind pair is 10 AND 13 (the i-quartics: the mu8 dictionary's rung
   13 <=> i in K); only e = 2 degenerates to a single constant. The
   general enumeration: explore_readout_proof.py L3.)

3. THE READOUT LAW (rule in range across e = 2, 4, 8, 12; TL7 + TL9):
   the rigid windows at e = 8 are (m = 1, 2, 3) = (1, 3, 11) digits =
   (2^1 - 1, 2^2 - 1, 3e/2 - 1). An INTERMEDIATE layer (c = e/2^m >
   1) reads 2^m - 1 digits — a layer-intrinsic count, independent of
   the window — while the window's TOP layer (c = 1, only at 2-power
   e) reads 3e/2 - 1: the class's own index digit rho_c is
   pair-cancelled out of its game (EL4), and for c = 1 that defers
   freedom from rel-2^m to rel-3e/2. Census scope: at e = 8 both the
   stop rows AND the freedom offsets are censused (rungs 17/18/19
   realized for m = 2, 17 for m = 1); at e = 12 the censused fact is
   the freedom OFFSET alone — x^12-2's floors 26/28 = 2e + 2^m with
   a non-rigid class-3 spectrum {28, 30} witness freedom at rel-4,
   but its digits w1w2w3 = 0 leave the e = 12 stop rows untested.
   The probe thereby confirms the bonus needs c = 1: the top class
   c = 3 landed floor 28 = 2e + 4, not 2e + 17. Verified rows: e = 2
   (explore_arrival_defect.py), e = 4 (explore_mu8_grading.py), e = 8
   + the e = 12 offsets (this engine).
   As e doubles the top readout grows linearly — the tower reads ALL
   of 2, each 2-power window ever deeper into its own expansion of
   the wild prime.

4. THE THREE-LAYER FACE (rule in range; TL1-TL3, TL5): the m = 1 law
   persists at e = 8 (class-4 floor 18 = p(i*+1) at every w1 = 0
   field), the class-2 (mu_8) ladder reads (w1; w2; w3) with floor
   20 and rigid rungs 17/18/19, starters land 17 = p*i*+1 at all 27
   fields, and the first-digit lock generalizes: w1 = 1 locks ALL
   THREE arrival classes at rigid {17} (384/768 of the family —
   exactly half, as at e = 4), starters keeping the graded dodge.

5. THE ANCHOR + DICTIONARY ROWS (rule in range; TL6, TL8): zeta16's
   digit vector is (0,0,0,1,0,0,0,0,0,1,0) — the unique no-stop walk,
   matching the corrected skeleton — and its landings replicate
   explore_arrival_defect.py's AD6 exactly (starters 17, spec4 min
   18, spec2 min 20, spec1 min 28, CAP present in all three arrival
   specs via exact torsion zeta16 = 1 + pi, zeta8 = zeta16^2,
   i = zeta16^4). The rung-17 witness carries no split label (TL8b),
   x^8-2 / x^8+2 have 2 / -2 split by construction, and the lazy
   TL8a row fired non-vacuously: both rung-26 census fields have CAP
   in spec4 with -1 split confirmed — x^8+2x^4+2 contains
   i = 1 + pi^4 EXACTLY ((pi^4+1)^2 = -1), the e = 8 analog of
   explore_mu8_grading.py's x^4+2x^2+2.

6. THE BASE-FREEDOM (rule in range; section [5]): the stop position
   is UNIFORMIZER-INVARIANT at all twelve rungs — one witness per
   rung x three alternative uniformizers pi' = pi*eta, the ladder
   read on the digits of 2/pi'^8 in base pi' stops at the same rung
   with the pre-stop prefix unmoved, while post-stop digits flip
   (3/3 variants at rungs 17-19/21-23/25, 2/3 at 20, 0/3 at
   24/26/27/28 where the window leaves little or no post-stop room) —
   the explore_mu8_grading.py finding-6 invariance carried to e = 8.

PRE-GREEN FAILURES (one, adjudicated): the rel-10 constant — the
slate's class-1 stop vector had rel-10 = w10; the first run's
rung-26 witness (predicted 26, measured {28, 30}) and the diagnostic
census of all eight (w9, w10, w11) patterns localized it to the
DROPPED j = 2 binomial: pass 1 pruned 28t^2 as "level 18" but I_1 =
(u^8+1)/pi^8 shifts it to rel-10 — exactly where EL2's own onset
formula (j-1)e + e/2^j put it; 28t^2/pi^8 = 7w^2rho^2pi^10, odd
constant. One mechanism corrects rows 26/27/28 + TL6's zeta16 vector
(predicted w10 = 0, true w10 = 1 — explore_arrival_defect.py's
measured 28 then follows); rungs 17..25 and every rel <= 3 stood.
Exactly the exposure EL5 froze (rel >= 4 constants falsifiable-form;
the explore_class_gap.py / explore_mu8_grading.py precedent).
Also one engine-sanity bug fixed pre-green, not a slate item: the
zeta8 torsion assert tested zeta8^4 = 1 where zeta8^4 = -1.

RUN RECORD (python explore_mu16_face.py, ~36 s, exit 0): 189,483
checks passed (gear sanity dominates: 46,000 sampled orbits — 27
e = 8 fields x 4 classes x 400 + x^12-2's 7 classes x 400 — with
per-step asserts). Census rows as printed: pred = L1 measured at all 26 sweep
fields + zeta16; L2min = 17/18/19/20 by first-nonzero of w1w2w3;
L4min = 17 iff w1 else 18; starters 17 everywhere. Histogram (768
octics): {17: 384, 18: 192, 19: 96, 20: 48, 21: 24, 22: 12, 23: 6,
24: 3, 26: 3}; backfill found 25/27/28 (e.g. [-14,4,4,4,2,0,0,4],
[-14,0,4,4,6,0,4,0], [-6,0,4,0,2,0,4,0]). zeta16 landings:
1->{28,CAP} 2->{20,26,28,30,CAP} 4->{18,20,22,25,26,27,...}
8->{17,...}. x^12-2: 3->{28,30} 6->{26,28,30,32,CAP}
12->{25,26,...}, arrival classes exactly {6, 3, 12}. Labels:
rung-17 witness all-ram; CAP-in-spec4 at both rung-26 fields with
-1 split. Green after the one adjudication above.
"""

import random

import explore_local_clock as lc
import explore_arrival_defect as ad
import explore_mu8_grading as mu8

CHECKS = 0


def ok(cond, msg):
    global CHECKS
    if not cond:
        raise AssertionError(msg)
    CHECKS += 1


# ------------------------------------------------------- general w machinery


def w_element_g(F):
    """w = 2/pi^e from the Eisenstein relation, any e; verified exactly."""
    c0 = F.eis[0]
    mu0 = c0 // 2
    inv_mu0 = pow(mu0 % F.pM, -1, F.pM)
    D = [list(F.zero_c) for _ in range(F.e)]
    D[0][0] = 1
    for j in range(1, F.e):
        D[j][0] = ((F.eis[j] // 2) * inv_mu0) % F.pM
    Dinv = mu8.unit_inv(F, tuple(tuple(c) for c in D))
    w = mu8.scale_el(F, Dinv, (-inv_mu0) % F.pM)
    piw = mu8.pi_el(F)
    pe = F.one
    for _ in range(F.e):
        pe = F.emul(pe, piw)
    ok(F.val(ad.esub(F, F.emul(pe, w), ad.const_el(F, 2))) == F.CAP,
       "%s: pi^e * w != 2" % F.name)
    return w


def digits_g(F, wp, pip, n=12):
    """F_2 digits of wp in base pip, wp = 2/pip^e: division by pip via
    (A - d) * pip^(e-1) * wp / 2 (coefficients exactly even)."""
    pipk = F.one
    for _ in range(F.e - 1):
        pipk = F.emul(pipk, pip)
    A, out = wp, []
    for _ in range(n):
        d = 1 if F.val(A) == 0 else 0
        out.append(d)
        B = [list(c) for c in A]
        B[0][0] = (B[0][0] - d) % F.pM
        C = F.emul(F.emul(tuple(tuple(c) for c in B), pipk), wp)
        ok(all(c[0] % 2 == 0 for c in C),
           "%s: odd coefficient in digit division" % F.name)
        A = tuple(((c[0] // 2),) for c in C)
    ok(out[0] == 1, "%s: leading digit not 1" % F.name)
    return out


def w_digits_g(F, w, n=12):
    """Canonical digits at the model uniformizer, reconstruction-checked."""
    pi = mu8.pi_el(F)
    digs = digits_g(F, w, pi, n)
    R = ad.const_el(F, 0)
    pw = F.one
    for d in digs:
        if d:
            R = tuple(F.cadd(a, b) for a, b in zip(R, pw))
        pw = F.emul(pw, pi)
    ok(F.val(ad.esub(F, w, R)) >= n, "%s: digit reconstruction" % F.name)
    return digs


# ------------------------------------------------------------ the ladders


def rung1(digs):
    """Class-1 (mu_16) predicted min: stops (w1; w2; w3; w4+1; w5; w6;
    w7; w8; w9; w10+1; w11), freedom at rel-12.

    The rel-10 constant is the ADJUDICATED one (first-run miss, the
    exposure EL5 named): the slate's stop vector had rel-10 =
    w10 — pass 1 dropped the j = 2 binomial 28t^2, whose /pi^8 shift
    lands it at rel-10 = (j-1)e + e/2^j exactly as EL2's onset formula
    says, contributing 28t^2/pi^8 = 7w^2rho^2pi^10, odd constant at
    rel-10. One mechanism corrects rows 26/27/28 + the TL6 vector;
    rungs 17..25 and every rel <= 3 stood. The blind rungs 20 and 26
    are the binomial skeleton of (1+t)^8 (see PRE-GREEN FAILURES)."""
    stops = [digs[1], digs[2], digs[3], 1 - digs[4], digs[5], digs[6],
             digs[7], digs[8], digs[9], 1 - digs[10], digs[11]]
    for k, s in enumerate(stops, start=1):
        if s:
            return 16 + k
    return 28


def rung2(digs):
    """Class-2 (mu_8) predicted min: stops (w1; w2; w3), freedom rel-4."""
    for k in (1, 2, 3):
        if digs[k]:
            return 16 + k
    return 20


def rung4(digs):
    """Class-4 (mu_4) predicted min: stop (w1), freedom rel-2."""
    return 17 if digs[1] else 18


# ------------------------------------------------------------ census bits


def sampled_spec(F, rng, classes, per_class=400):
    """Sampled landing spectra + psi-gear sanity, per start class."""
    spec = {}
    for c in classes:
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


def sq_el(F, tgt):
    """max v(u^2 - tgt) over U_1/U_amax representatives, early exit."""
    thr = 2 * F.e
    best = 0
    for u in F.units():
        vv = F.val(ad.esub(F, F.emul(u, u), tgt))
        if vv > best:
            best = vv
            if best > thr:
                return best
    return best


def label_of(FL, w, delta):
    """split/unram/ram for delta in {-1, 2, -2}, orbit-free (amax 17)."""
    if delta == -1:
        t_split, t_unram = ad.const_el(FL, -1), ad.const_el(FL, -5)
    else:
        m = delta // 2
        t_split = mu8.scale_el(FL, w, m)
        t_unram = mu8.scale_el(FL, w, 5 * m)
    if sq_el(FL, t_split) > 2 * FL.e:
        return "split"
    if sq_el(FL, t_unram) > 2 * FL.e:
        return "unram"
    return "ram"


def label_field(eis, name):
    """A fresh amax-17 twin of a census field, for exhaustive labels."""
    FL = lc.LF(name, 2, [0, 1], eis, 17)
    wL = w_element_g(FL)
    ok(sq_el(FL, ad.const_el(FL, 5)) <= 2 * FL.e, "%s: sqrt5 in K?" % name)
    return FL, wL


def census_field(name, eis, rng, amax=32):
    F = lc.LF(name, 2, [0, 1], eis, amax)
    w = w_element_g(F)
    digs = w_digits_g(F, w)
    spec = sampled_spec(F, rng, (1, 2, 4, 8))
    return F, w, digs, spec


def check_slate(name, digs, spec, F):
    """TL1-TL5 assertions common to every censused e = 8 field."""
    p1, p2, p4 = rung1(digs), rung2(digs), rung4(digs)
    s1, s2, s4 = spec.get(1, set()), spec.get(2, set()), spec.get(4, set())
    s8 = spec.get(8, set())
    ok(min(s1) == p1, "%s: class-1 min %s != pred %d" % (name, s1, p1))
    ok(min(s2) == p2, "%s: class-2 min %s != pred %d" % (name, s2, p2))
    ok(min(s4) == p4, "%s: class-4 min %s != pred %d" % (name, s4, p4))
    ok(min(s8) == 17, "%s: starter floor %s != 17" % (name, s8))
    if p1 < 28:
        ok(s1 == {p1}, "%s: class-1 spectrum %s not rigid" % (name, s1))
    if p2 < 20:
        ok(s2 == {p2}, "%s: class-2 spectrum %s not rigid" % (name, s2))
    if digs[1]:
        ok(s2 == {17} and s4 == {17},
           "%s: the lock — spectra %s %s not {17}" % (name, s2, s4))
        ok(len(s8) > 1, "%s: starter spectrum unexpectedly rigid" % name)
    return p1


# ------------------------------------------------------------------- zoo

SCAN = []
for d in (-2, 2, -6, 6, -10, 10):
    for bits in range(128):
        cs = [2 * ((bits >> k) & 1) for k in range(7)]
        SCAN.append(tuple([d] + cs))

PURE = [(-2,) + (0,) * 7, (2,) + (0,) * 7, (-6,) + (0,) * 7,
        (6,) + (0,) * 7, (-10,) + (0,) * 7, (10,) + (0,) * 7]

PHI16 = [2, 8, 28, 56, 70, 56, 28, 8, 1]


def poly_name(key):
    return "[" + ",".join(str(c) for c in key) + "]"


def run():
    rng = random.Random(188)
    print("THE E = 8 THREE-LAYER FACE — the constellation law's mu_16 rung")
    print("=" * 68)

    # [0] the scan: digits + predicted rungs over the octic family
    print("\n[0] the scan: 768 Eisenstein octics, digits w1..w11 -> rungs")
    by_rung = {}
    for key in SCAN:
        eis = list(key) + [1]
        F = lc.LF(poly_name(key), 2, [0, 1], eis, 16)
        w = w_element_g(F)
        digs = w_digits_g(F, w)
        by_rung.setdefault(rung1(digs), []).append(key)
    hist = {r: len(v) for r, v in sorted(by_rung.items())}
    print("    rung histogram: %s" % hist)

    missing = [r for r in range(17, 29) if r not in by_rung]
    if missing:
        print("    backfill search for rungs %s ..." % missing)
        tries = 0
        while missing and tries < 4000:
            tries += 1
            d = rng.choice((-2, 2, -6, 6, -10, 10, -14, 14))
            cs = tuple(2 * rng.randrange(4) for _ in range(7))
            key = (d,) + cs
            eis = list(key) + [1]
            F = lc.LF(poly_name(key), 2, [0, 1], eis, 16)
            w = w_element_g(F)
            digs = w_digits_g(F, w)
            r = rung1(digs)
            if r in missing:
                by_rung.setdefault(r, []).append(key)
                missing.remove(r)
                print("      rung %d witness found: %s" % (r, poly_name(key)))
        if missing:
            print("      STILL UNREALIZED after %d tries: %s" % (tries,
                                                                 missing))

    # [1] the census: two witnesses per realized rung + the pure octics
    print("\n[1] the census: sampled falsify-outright, amax 32, 400/class")
    print("    %-26s %-13s %-4s %-4s %-6s %-6s %-5s"
          % ("field", "w1-w11", "pred", "L1", "L2min", "L4min", "start"))
    witnesses = []
    seen = set()
    for r in sorted(by_rung):
        for key in by_rung[r][:2]:
            if key not in seen:
                seen.add(key)
                witnesses.append(key)
    for key in PURE:
        if key not in seen:
            seen.add(key)
            witnesses.append(key)
    rung_witness = {}
    cap_fields = []
    for key in witnesses:
        name = poly_name(key)
        eis = list(key) + [1]
        F, w, digs, spec = census_field(name, eis, rng)
        p1 = check_slate(name, digs, spec, F)
        rung_witness.setdefault(p1, (key, digs))
        if key in PURE:
            ok(digs[1:8] == [0] * 7,
               "%s: pure octic digits w1..w7 not zero" % name)
            ok(p1 == 20 and spec[1] == {20},
               "%s: blind rung %s" % (name, spec[1]))
        for c in (1, 2, 4):
            if any(v >= F.CAP for v in spec.get(c, set())):
                cap_fields.append((key, c))
        print("    %-26s %-13s %-4d %-4d %-6d %-6d %-5d"
              % (name, "".join(str(x) for x in digs[1:12]), p1,
                 min(spec[1]), min(spec[2]), min(spec[4]), min(spec[8])))
    print("    censused fields: %d (rungs realized: %s)"
          % (len(witnesses), sorted(rung_witness)))

    # [2] labels at the frozen scope
    print("\n[2] labels (orbit-free, exhaustive U_1/U_17)")
    if 17 in rung_witness:
        key, _ = rung_witness[17]
        FL, wL = label_field(list(key) + [1], poly_name(key))
        lab = {d: label_of(FL, wL, d) for d in (-1, 2, -2)}
        ok("split" not in lab.values(),
           "rung-17 witness %s has a split label: %s" % (FL.name, lab))
        print("    rung-17 witness %s: %s (no split — TL8b)" % (FL.name, lab))
    FL, wL = label_field([-2, 0, 0, 0, 0, 0, 0, 0, 1], "x8-2")
    ok(F_is_one(FL, wL), "x8-2: w != 1")
    ok(label_of(FL, wL, 2) == "split", "x8-2: 2 not split")
    FL, wL = label_field([2, 0, 0, 0, 0, 0, 0, 0, 1], "x8+2")
    ok(label_of(FL, wL, -2) == "split", "x8+2: -2 not split")
    print("    constructive rows: x8-2 has 2 split, x8+2 has -2 split")
    need = {4: (-1,), 2: (-1, 2), 1: (-1, 2, -2)}
    for key, c in cap_fields:
        FL, wL = label_field(list(key) + [1], poly_name(key))
        for delta in need[c]:
            ok(label_of(FL, wL, delta) == "split",
               "%s: CAP in spec%d without split labels" % (FL.name, c))
        print("    CAP in spec%d at %s: split labels confirmed (lazy TL8a)"
              % (c, FL.name))
    if not cap_fields:
        print("    no sweep witness showed CAP (lazy TL8a row vacuous here;"
              " both-ways rows live at the anchor)")

    # [3] the anchor: Q2(zeta16)
    print("\n[3] the anchor: Phi16(x+1), zeta16 = 1 + pi exact")
    F, w, digs, spec = census_field("zeta16", PHI16, rng)
    ok(digs[1:12] == [0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0],
       "zeta16: digit vector %s" % digs[1:12])
    print("    digits w1..w11 = %s (the no-stop walk — TL6)"
          % "".join(str(x) for x in digs[1:12]))
    # exact torsion: zeta16 = 1 + pi; zeta8 = zeta16^2; i = zeta16^4
    z16 = [list(F.zero_c) for _ in range(F.e)]
    z16[0][0] = 1
    z16[1][0] = 1
    z16 = tuple(tuple(c) for c in z16)
    z8 = F.emul(z16, z16)
    i_el = F.emul(z8, z8)
    ok(F.val(ad.esub(F, F.emul(i_el, i_el), ad.const_el(F, -1))) == F.CAP,
       "zeta16: i^2 != -1")
    ok(F.val(ad.esub(F, F.emul(z8, F.emul(z8, F.emul(z8, z8))),
                     ad.const_el(F, -1))) == F.CAP, "zeta16: zeta8^4 != -1")
    for u, c in ((z16, 1), (z8, 2), (i_el, 4)):
        ok(F.val(F.esub1(u)) == c, "zeta16: torsion class %d" % c)
        o = F.orbit(u)
        n = o.index(F.seat)
        spec.setdefault(c, set()).add(o[n + 1])
        ok(o[n + 1] >= F.CAP, "zeta16: torsion class %d not CAP" % c)
    p1 = check_slate("zeta16", digs, spec, F)
    ok(p1 == 28 and min(spec[1]) == 28, "zeta16: class-1 28")
    ok(min(spec[2]) == 20 and min(spec[4]) == 18, "zeta16: AD6 floors")
    for c in (1, 2, 4):
        ok(any(v >= F.CAP for v in spec[c]),
           "zeta16: CAP missing in spec%d" % c)
    print("    landings: %s (explore_arrival_defect.py's AD6 replicated:"
          " 17/18/20/28 + CAP rows)" % ad.fmt_spec(F, spec))

    # [4] the probe: x^12 - 2 (the no-bonus row)
    print("\n[4] the probe: x^12 - 2, e = 12 — the top class c = 3 (odd)")
    eis12 = [-2] + [0] * 11 + [1]
    F = lc.LF("x12-2", 2, [0, 1], eis12, 32)
    w = w_element_g(F)
    digs = w_digits_g(F, w)
    ok(digs[1:4] == [0, 0, 0], "x12-2: w1..w3 not zero")
    spec = sampled_spec(F, rng, (1, 2, 3, 4, 6, 8, 12))
    ok(set(spec) <= {6, 3, 12},
       "x12-2: unexpected arrival classes %s" % sorted(spec))
    ok(min(spec[12]) == 25, "x12-2: starter floor %s" % spec[12])
    ok(min(spec[6]) == 26, "x12-2: class-6 floor %s" % spec[6])
    ok(min(spec[3]) == 28, "x12-2: class-3 floor %s" % spec[3])
    print("    landings: %s" % ad.fmt_spec(F, spec))
    print("    class-3 floor 28 = 2e + 4: window 3, not 3e/2 - 1 = 17 —")
    print("    the 1.5x readout bonus needs c = 1 (TL9)")

    # [5] uniformizer invariance of the stop position
    print("\n[5] invariance: one witness per rung x 3 uniformizers")
    for r in sorted(rung_witness):
        key, digs0 = rung_witness[r]
        name = poly_name(key)
        F = lc.LF(name, 2, [0, 1], list(key) + [1], 16)
        w = w_element_g(F)
        pi = mu8.pi_el(F)
        stop = (rung1(digs0) - 16 if rung1(digs0) < 28 else 12)
        flips = 0
        for et in ((1, 1), (2, 1), (1, 1, 1, 1)):
            eta = [list(F.zero_c) for _ in range(F.e)]
            eta[0][0] = 1
            for j, cc in enumerate(et, start=1):
                eta[j][0] = cc
            eta = tuple(tuple(c) for c in eta)
            pip = F.emul(pi, eta)
            e8 = F.one
            for _ in range(8):
                e8 = F.emul(e8, eta)
            wp = F.emul(w, mu8.unit_inv(F, e8))
            digsp = digits_g(F, wp, pip)
            ok(rung1(digsp) == r,
               "%s: rung moved under uniformizer change" % name)
            ok(digsp[1:stop + 1] == digs0[1:stop + 1],
               "%s: pre-stop digit prefix moved" % name)
            if digsp[1:12] != digs0[1:12]:
                flips += 1
        print("    rung %d (%s): stop invariant, %d/3 variants flip"
              " post-stop digits" % (r, name, flips))

    print("\nALL CHECKS PASSED: %d" % CHECKS)


def F_is_one(F, w):
    return F.val(F.esub1(w)) == F.CAP


if __name__ == "__main__":
    run()
