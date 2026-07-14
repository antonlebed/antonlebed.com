"""explore_readout_proof.py — THE READOUT THEOREM: the general proof
of the readout law (the constellation arc's proof session).

THE QUESTION. The readout law stood at rule in range
(four censused 2-power windows, e = 2..16 + the e = 12 offsets):
a 2-power window's arrival classes read (2^m - 1, top 3e/2 - 1)
digits of 2/pi^e. Two gaps separated rule-in-range
from rule: (1) no free-digit entry beats 3e/2 at c = 1, and (2) the
carry bookkeeping at arbitrary e. This session closes both by a
general proof, and spot-falsifies it SIGHT-UNSEEN at e = 32 — a
window no engine has ever touched.

THE HAND DERIVATION (frozen before this file existed).

Setup: K/Q_2 totally ramified degree e, f = 1, pi uniformizer,
w = 2/pi^e a unit with canonical {0,1}-digits w_i (Teichmueller, so
digit^k = digit — the f = 1 seat; f >= 2 Frobenius-twists digits and
the pair-cancellation below dies, matching the two-gear kernel
dodge). Class-(c, mu) unit (c * 2^mu = e): u = 1 + rho pi^c, rho a
unit with free digits rho_i. rel = v(S), S = (u^(2^mu) + 1)/pi^e;
landing L = 2e + rel. Carry rule: 2 pi^r = w pi^(r+e) (EL5).

L1 (multinomial Kummer, exact — Legendre both sides):
    v2(multinomial(2^mu; a_0, a_1, ..., ones)) =
    s2(2^mu - A) + sum_i s2(a_i) - 1 =: sigma(a) - 1.
L2 (the tau alphabet + level formula): t = rho pi^c = sum tau_i,
    tau_0 = pi^c, tau_i = rho_i pi^(c+i); the monomial
    a = (a_i multiplicities, A = sum a_i, W = sum i*a_i) of
    u^(2^mu) contributes to S at level
        Lambda(a) = e*(sigma(a) - 2) + c*A + W
    with coefficient odd-unit * w-power * prod rho_i (idempotence).
L3 (THE ENUMERATION LEMMA, top class c = 1, e = 2^s >= 4): the
    monomials with Lambda < 3e/2 are EXACTLY
      (a_0 = e)   at 0    [with w: (w-1) + w pi^e]
      (a_0 = e/2) at e/2  [c_1 w pi^(e/2), c_1 = C(e,e/2)/2 odd
                           => c_1 w == w mod pi^e: the tail is w's]
      (a_1 = e), (a_1 = e/2) at e  [the rho_1 PAIR]
      (a_0 = e/4) at 5e/4 [c_2 w^2 pi^(5e/4), c_2 odd]
    and at the boundary 3e/2 the rho_2 carrier (a_2 = e/2) is the
    unique rho_2-monomial. Proof: sigma-split — sigma = 1 forces
    A = e single part (Lambda = e*i0); sigma = 2 forces (e/2, e/2)
    pairs (Lambda >= e + e/2) or A = e/2 single (Lambda =
    (1+i0)e/2); sigma = 3 forces A = e/4 at index 0; sigma >= 4
    gives Lambda >= 2e. At e = 2: no c_2 slot, single constant at
    e/2 = 1. At e = 4 the c_2 slot is (a_0 = 1) = 4*tau_0 = w^2
    pi^5: same term.
L3' (intermediate classes c > 1, ANY e with 2^mu | e): in-window
    (Lambda < 2^mu) is EMPTY beyond the leading 1; the rho_1 carrier
    (a_1 = 2^mu), coefficient exactly 1, sits alone at the boundary
    2^mu (c = 2 adds the j = 1 constant AT the freedom rung —
    harmless, floor graded). Covers odd-c top classes: the e = 12
    no-bonus row is this lemma.
L4 (THE ON-BRANCH LADDER, top class): summing the L3 list by digit
    level and using "alive past r' => that digit summed to 0":
      r < e/2:          D_r = w_r
      r = e/2:          D_r = w_{e/2} + 1
      e/2 < r < 5e/4:   D_r = w_r   (at r = e the +1 from 2 = w pi^e
                        CANCELS against the c_1-tail digit
                        w_{r-e/2} = w_{e/2} = 1 forced on-branch;
                        the rho_1 pair drops mod 2, carry to 2e)
      r = 5e/4:         D_r = w_{5e/4} + 1
      5e/4 < r < 3e/2:  D_r = w_r
    THE PAIR RESIDUAL: rho_1 (1 + c_1 w) pi^e with v(1 + c_1) >= e
    (c_1 odd) and v(c_1(w - 1)) = e/2 on-branch => the residual
    lands at 3e/2 EXACTLY — below 3e/2 the ladder is rho-free on
    every live branch; off-branch it sits above the stop. This
    closes gap (1); the sigma-split's exact 2-content is
    gap (2).
L5 (freedom): rho_2's unique boundary monomial has unit coefficient
    c_1 w => rho_2 toggles D_{3e/2}: floor 3e/2 attained and graded.
    Intermediate: rho_1 toggles at 2^mu.
THE THEOREM (all censused shapes are corollaries): windows
    (2^mu - 1 intermediate | 3e/2 - 1 top); skeleton constants at
    e/2 and 5e/4 only (one at e = 2; the j = 3 constant at 2e + e/8
    NEVER enters any window); blind rungs; the unique no-stop
    vector; the lock w_1 = 1; the m = 1 law p(i*+1); the odd-c
    no-bonus. NEW COROLLARY C7: zeta_{2e} makes the class-1 game
    literally stopless (zeta^e = -1), and Q_2(zeta_{2e}) is the only
    e-window containing it => the digit vector of
    w = 2/(zeta_{2e} - 1)^e is EXACTLY the skeleton (nonzero at e/2,
    5e/4 alone below 3e/2) for EVERY e = 2^s — the censused
    zeta16/zeta32 vectors were instances.

PREDICTIONS (fixed before the run; labels never read orbits;
under the proof EVERY row is load-bearing — a miss at ANY rel
falsifies the proof, superseding EL5's rel <= 3 / rel >= 4 split):

RL1 (row): e = 32 carries FIVE arrival classes (c, mu) = (16,1),
    (8,2), (4,3), (2,4), (1,5); windows (1, 3, 7, 15, 47);
    landings L = 64 + rel.
RL2 (skeleton): top-class constants at rel-16 and rel-40 ONLY
    (j = 3 at 68, past freedom 48); blind rungs 80 and 104; freedom
    dodge 112.
RL3 (lock): w1 = 1 => all five arrival classes rigid {65}; starters
    floor 65 graded.
RL4 (pure): x^32 - d: spec1 = {80} rigid.
RL5 (anchor): Phi64(x+1), zeta64 = 1 + pi: digit vector nonzero
    exactly at {16, 40} (C7); landings starters 65, spec16 min 66,
    spec8 min 68, spec4 min 72, spec2 min 80, spec1 min 112; CAP in
    all five arrival specs via exact torsion (i = zeta64^16 in class
    16, zeta8 in 8, zeta16 in 4, zeta32 in 2, zeta64 in 1).
RL6 (m = 1): w1 = 0 => spec16 min 66 = p(i* + 1).
RL7 (ladders): at every censused e = 32 field all five class minima
    = the ONE general ladder on measured digits; spectra rigid below
    freedom (64 + 2^mu for c > 1; 112 for c = 1).
PL (proof-verification rows): L1 exhaustive (factorial v2 vs s2
    formula); the L3/L3' enumeration brute-checked at e = 2..64 top
    + a mixed intermediate scope incl. non-2-power e (the >= 4-part
    exclusion asserted); identity rows at real fields
    (v(c_1 w - w) >= e, v(1 + c_1 w) = min(v(w-1), e*v2(1+c_1)));
    the general ladder == every frozen per-e ladder (mu8.rung,
    m16.rung1/2/4, m32.rung*_16).

THE DESIGN. [A] L1 brute over part-multisets (n = 2, 4, ..., 64).
[B] the enumeration lemma: brute over monomials with <= 3 distinct
indices under the per-part-count sigma lower bounds (1-part
sigma >= 1, 2-part >= 2, 3-part >= 3 — structural, s2 >= 1 per
part; >= 4 parts excluded by sigma >= 4 => Lambda >= 2e, asserted
per scope row), v2 via per-factorial Legendre — verified against
integer factorials in [A] over [B]'s whole parameter space; assert
in-window lists + boundary carriers match L3/L3' verbatim. [C] proof-internal identities + DIRECT rel checks
(v(u^(2^mu) + 1) - e vs the ladder on measured digits, mu squarings
per unit, no orbit) at e = 8/16 regression witnesses from the
censused zoos and at the e = 32 scan: seeded random Eisenstein
32-ics (d in {+-2, +-6, +-10}, random even middle coefficients),
plus designed spot rows (pure d, 2b x^16 rel-16 passers, a rel-5
stop) — the engine only ever reads MEASURED digits. [D] the zeta64
anchor exact (torsion classes, digit vector, sampled landing specs
incl. starters, CAP rows). [E] orbit ties at a subset of scan fields
(sampled_spec: psi-gear sanity + landing = 64 + rel). [F] the
general ladder vs the frozen per-e ladders (exhaustive where the
window allows, weight-<= 2 + seeded sample at e = 16 top).
Run: python prime/code/explore_readout_proof.py

FINDINGS (entered post-run, copied from printed output; tiers below).

1. THE READOUT THEOREM (theorem — the proof is general in e, the
   engine verifies it): for every totally ramified f = 1 window
   K/Q_2 of degree e and every arrival class (c, mu) with
   c * 2^mu = e, the landing ladder is the L4/L3' staircase on the
   canonical digits of 2/pi^e — windows 2^mu - 1 (c > 1, ANY e,
   odd-c tops included) and 3e/2 - 1 (c = 1, e = 2^s), skeleton
   constants at rel-e/2 and rel-5e/4 alone (rel-1 at e = 2; the
   j = 3 constant NEVER enters a window), freedom carried by rho_2
   (top) / rho_1 (intermediate), spectra rigid below freedom on
   every live branch. Gap (1) closes by the sigma-split: every
   rho-route lands >= 3e/2 on-branch, the rho_1 pair's residual at
   e + v(c_1(w-1)) = 3e/2 exactly via the forced rel-e/2 constant;
   gap (2) closes because the only in-window carry sites are the two
   skeleton constants and the r = e cross-cancellation (the +1 from
   2 = w pi^e killed by the c_1-tail digit w_{e/2} = 1). The lock,
   the m = 1 law p(i*+1), the blind rungs, the unique no-stop
   vector, and the i-in-K-pins-w1-silent rule are corollaries.
   Enumeration lemma brute-verified verbatim: 10,029 L1 multisets
   (both formulas against the factored integer multinomial),
   6 top rows e = 2..64, 10 intermediate rows incl. e = 12, 24.

2. THE e = 32 FACE CONFIRMS SIGHT-UNSEEN (rule in range made
   prediction: RL1-RL4, RL6, RL7 all hit): 24 seeded scan fields +
   7 designed + 6 pures + zeta64 — at every scan and designed field
   all five class minima equal the ONE general ladder on measured
   digits (40 units per class direct rel, rigid below freedom,
   floors attained); the pures censused at the top class.
   Scan class-1 histogram {66: 2, 68: 2, 70: 2, 71: 1, 73: 2,
   74: 1, 76: 1, 77: 2, 78: 2, 79: 3, 80: 6} (the sparse grid
   skews deep); designed rows landed 69 (x32+2x5-2), 65 (the lock
   witness x32+2x-2, ALL FIVE classes rigid {65}), 96 (x32+2x16-2),
   104 (x32+2x16-6 — the second blind rung realized), 81/82/83
   ([-2,2@16,2@(17/18/19)]); pures spec1 = {80} rigid x6. The row
   (1, 3, 7, 15, 47); the top readout series now 2, 5, 11, 23, 47
   digits at e = 2, 4, 8, 16, 32.

3. THE ANCHOR + C7's FIRST SIGHT-UNSEEN INSTANCE (RL5): zeta64's
   digit vector is nonzero EXACTLY at {16, 40} — predicted by
   corollary C7 before the engine existed (the fifth skeleton
   vector; zeta16/zeta32 were censused, this one was called) — with
   spec mins 112/80/72/68/66/65 at classes 1/2/4/8/16/32 and CAP in
   all five arrival specs via exact torsion (zeta64^32 = -1
   asserted; torsion classes 2/4/8/16 at v = c).

4. PROOF-INTERNAL IDENTITIES + REGRESSION (PL): v(c_1 w - w) >= e,
   v(c_2 w^2 - w^2) >= e, and v(1 + c_1 w) = min(v(w-1),
   e*v2(1+c_1)) hold at all 44 digit-bearing fields (e = 8, 16, 32,
   the anchor included);
   the general ladder reproduces mu8.rung, m16.rung1/2/4, and
   m32.rung1_16/2/4/8 verbatim (exhaustive at windows <= 11, weight
   <= 2 + 5000 sampled at the e = 16 top); the e = 8/16 regression
   witnesses reprint their censused rungs (x8+2x4+2 digits
   0001... -> 26; x16+2x8-6 digits ...w8=1... -> 52; the lock twins
   all-ones -> 17/33).

PRE-GREEN FAILURES: one, engine-side — the brute-checker's lam()
double-subtracted e (the pi^e shift was already folded into the
"- 1"), caught by its own FIRST assert (e = 2) against the
hand-frozen expected list; the hand lists stood unchanged, no field
arithmetic had run. Coverage note: the first green run's sparse scan
drew zero w1 = 1 fields (P(none) ~ 29% at the grid's ~5% rate),
leaving RL3 scan-unexercised; the lock witness x32+2x-2 +
x32+2x16-2/-6 were added as designed rows after first green and the
engine re-run whole (coverage steering, the read untouched).

RUN RECORD (python explore_readout_proof.py, ~12 s, exit 0): 35,237
checks passed (28,072 this module + 7,165 in the imported machinery;
[A]'s 2 x 10,029 integer-v2 rows and [F]'s exhaustive + sampled
ladder vectors dominate this module; digit-reconstruction
self-checks dominate the imported count — 44 digit-bearing fields).
zeta64 landings as printed: spec mins (1/2/4/8/16/32) =
112/80/72/68/66/65, CAP x5 arrival classes.
"""

import math
import random

import explore_local_clock as lc
import explore_arrival_defect as ad
import explore_mu8_grading as mu8
import explore_mu16_face as m16
import explore_mu32_face as m32

CHECKS = 0


def ok(cond, msg):
    global CHECKS
    if not cond:
        raise AssertionError(msg)
    CHECKS += 1


def s2(n):
    return bin(n).count("1")


def v2_fact(n):                       # Legendre
    return n - s2(n)


def v2_multinomial(n, parts):
    """v2( n! / (prod a_i! * (n - A)!) ), parts = the a_i >= 1."""
    A = sum(parts)
    v = v2_fact(n) - v2_fact(n - A)
    for a in parts:
        v -= v2_fact(a)
    return v


# ------------------------------------------------- the general ladder


def ladder_rel(e, mu, digs):
    """THE ONE LADDER (L4 + L3'): first-stop rel for class c = e/2^mu.
    digs[k] = w_k (digs[0] = 1). Returns the freedom level on
    no-stop."""
    c = e >> mu
    if c == 1:
        end = 3 * e // 2
        skel = {e // 2} if e < 4 else {e // 2, 5 * e // 4}
    else:
        end = 1 << mu
        skel = set()
    for r in range(1, end):
        d = digs[r]
        if r in skel:
            d = 1 - d
        if d:
            return r
    return end


# ------------------------------------------------- [A] + [B] the lemma


def v2_int(m):
    v = 0
    while m % 2 == 0:
        m //= 2
        v += 1
    return v


def check_L1():
    """The formula v2_multinomial (Legendre) AND the sigma - 1 shortcut
    against the LITERAL integer multinomial — the reference is the
    factored integer, imported from outside both formulas."""
    n_checked = 0
    for t in (1, 2, 3, 4, 5, 6):
        n = 1 << t
        singles = [(a,) for a in range(1, n + 1)]
        pairs = [(a, b) for a in range(1, n + 1) for b in range(a, n + 1)
                 if a + b <= n]
        triples = [(a, b, cc) for a in range(1, n + 1)
                   for b in range(a, n + 1) for cc in range(b, n + 1)
                   if a + b + cc <= n]
        for parts in singles + pairs + triples:
            A = sum(parts)
            m = math.factorial(n) // math.factorial(n - A)
            for a in parts:
                m //= math.factorial(a)
            truth = v2_int(m)
            ok(v2_multinomial(n, parts) == truth,
               "L1 Legendre miss n=%d parts=%s" % (n, parts))
            ok(s2(n - A) + sum(s2(a) for a in parts) - s2(n) == truth,
               "L1 s2-form miss n=%d parts=%s" % (n, parts))
            n_checked += 1
    print("[A] L1 multinomial Kummer: %d part-multisets vs integer v2"
          % n_checked)


def enum_in_window(e, mu):
    """Brute enumeration of monomials with Lambda <= window end.
    Returns sorted list of (Lambda, ((index, part), ...)).

    Scope: <= 3 distinct indices. Justification asserted here: with
    k parts sigma >= k (each part contributes s2 >= 1; A < 2^mu adds
    one more), so 4 parts give Lambda >= e*(4-2) + cA + W >= 2e +
    4c > window at every class — no index assignment can rescue a
    4-part monomial."""
    c = e >> mu
    n = 1 << mu
    end = 3 * e // 2 if c == 1 else 1 << mu
    ok(2 * e + 4 * c > end, "4-part exclusion fails e=%d mu=%d" % (e, mu))
    imax = end + e                     # Lambda >= cA + W - e >= i - e
    found = []

    def lam(parts_ix):
        parts = tuple(a for _, a in parts_ix)
        A = sum(parts)
        if A > n:
            return None
        W = sum(i * a for i, a in parts_ix)
        return e * (v2_multinomial(n, parts) - 1) + c * A + W

    for i0 in range(imax + 1):
        for a0 in range(1, n + 1):
            if c * a0 + i0 * a0 - e > end:    # sigma >= 1 bound
                break
            L = lam(((i0, a0),))
            if L is not None and L <= end:
                found.append((L, ((i0, a0),)))
    for i0 in range(imax + 1):
        for a0 in range(1, n + 1):
            if c * a0 + i0 * a0 > end:        # sigma >= 2 bound
                break
            for i1 in range(i0 + 1, imax + 1):
                for a1 in range(1, n + 1):
                    if c * (a0 + a1) + i0 * a0 + i1 * a1 > end:
                        break
                    L = lam(((i0, a0), (i1, a1)))
                    if L is not None and L <= end:
                        found.append((L, ((i0, a0), (i1, a1))))
    for i0 in range(imax + 1):                # sigma >= 3: cA+W <= end-e
        for a0 in range(1, n + 1):
            if e + c * a0 + i0 * a0 > end:
                break
            for i1 in range(i0 + 1, imax + 1):
                for a1 in range(1, n + 1):
                    if e + c * (a0 + a1) + i0 * a0 + i1 * a1 > end:
                        break
                    for i2 in range(i1 + 1, imax + 1):
                        for a2 in range(1, n + 1):
                            if (e + c * (a0 + a1 + a2) + i0 * a0
                                    + i1 * a1 + i2 * a2 > end):
                                break
                            L = lam(((i0, a0), (i1, a1), (i2, a2)))
                            if L is not None and L <= end:
                                found.append(
                                    (L, ((i0, a0), (i1, a1), (i2, a2))))
    return sorted(found)


def check_L3():
    # top class rows: (e, expected in-window list, expected boundary)
    for s in (1, 2, 3, 4, 5, 6):
        e = 1 << s
        inw = [(0, ((0, e),))]
        if s >= 2:
            inw += [(e // 2, ((0, e // 2),)),
                    (e, ((1, e // 2),)), (e, ((1, e),)),
                    (5 * e // 4, ((0, e // 4),))]
        else:
            inw += [(1, ((0, 1),)), (2, ((1, 1),)), (2, ((1, 2),))]
        got = enum_in_window(e, s)
        end = 3 * e // 2
        got_in = [x for x in got if x[0] < end]
        ok(got_in == sorted(inw),
           "L3 in-window mismatch e=%d: %s" % (e, got_in))
        rho2_bnd = [x for x in got if x[0] == end
                    and any(i == 2 and a for i, a in x[1])]
        ok(len(rho2_bnd) == 1 and rho2_bnd[0][1] == ((2, e // 2 if s >= 2
                                                      else 1),),
           "L3 rho_2 carrier not unique e=%d: %s" % (e, rho2_bnd))
        print("[B] top e=%-3d in-window %d terms + carrier: verbatim"
              % (e, len(got_in)))
    # intermediate rows incl. non-2-power e
    for (e, mu) in ((4, 1), (8, 1), (8, 2), (16, 1), (16, 2), (16, 3),
                    (12, 1), (12, 2), (24, 3), (32, 4)):
        c = e >> mu
        ok(c > 1, "scope error")
        n = 1 << mu
        got = enum_in_window(e, mu)
        got_in = [x for x in got if x[0] < n]
        ok(got_in == [(0, ((0, n),))],
           "L3' in-window not empty e=%d mu=%d: %s" % (e, mu, got_in))
        rho1_bnd = [x for x in got if x[0] == n
                    and any(i == 1 and a for i, a in x[1])]
        ok(len(rho1_bnd) == 1 and rho1_bnd[0][1] == ((1, n),),
           "L3' rho_1 carrier not unique e=%d mu=%d: %s"
           % (e, mu, rho1_bnd))
        bnd_const = [x for x in got if x[0] == n
                     and all(i == 0 for i, a in x[1])]
        ok(len(bnd_const) == (1 if c == 2 else 0),
           "L3' c=2 boundary constant e=%d mu=%d: %s" % (e, mu, bnd_const))
        print("[B] intermediate (e=%d, mu=%d): window clean, carrier unique"
              % (e, mu))


# --------------------------------------------- [C] fields + direct rel


NDIG32 = 48


def make_field(name, eis, amax):
    F = lc.LF(name, 2, [0, 1], eis, amax)
    w = m16.w_element_g(F)
    digs = m16.w_digits_g(F, w, n=(3 * F.e) // 2 + 1)
    return F, w, digs


def direct_rel(F, u, mu):
    z = u
    for _ in range(mu):
        z = F.emul(z, z)
    return F.val(ad.esub(F, z, ad.const_el(F, -1))) - F.e


def check_identities(F, w, digs):
    """PL identity rows: constant-tail absorption + the residual seat."""
    e = F.e
    c1 = math.comb(e, e // 2) // 2
    c2 = math.comb(e, e // 4) // 4 if e >= 4 else None
    ok(c1 % 2 == 1, "%s: c_1 even" % F.name)
    ok(F.val(mu8.scale_el(F, w, c1 - 1)) >= e, "%s: c_1 w tail" % F.name)
    if c2 is not None:
        ok(c2 % 2 == 1, "%s: c_2 even" % F.name)
        w2 = F.emul(w, w)
        ok(F.val(mu8.scale_el(F, w2, c2 - 1)) >= e, "%s: c_2 w^2 tail"
           % F.name)
    d = next((k for k in range(1, len(digs)) if digs[k]), None)
    if d is not None:
        one_c1w = ad.esub(F, ad.const_el(F, 1), mu8.scale_el(F, w, -c1))
        v2c = 1
        while (1 + c1) % (1 << (v2c + 1)) == 0:
            v2c += 1
        want = min(d, e * v2c)
        if want < F.amax:
            ok(F.val(one_c1w) == want,
               "%s: residual seat v(1+c_1 w) = %d != %d"
               % (F.name, F.val(one_c1w), want))


def check_field_direct(F, w, digs, rng, per_class=40):
    """RL7 at any e: direct rel vs the general ladder, all classes."""
    e = F.e
    s = e.bit_length() - 1
    rows = 0
    for mu in range(1, s + 1):
        c = e >> mu
        pred = ladder_rel(e, mu, digs)
        end = 3 * e // 2 if c == 1 else 1 << mu
        rels = set()
        for u in ad.sample_class(F, c, per_class, rng):
            r = direct_rel(F, u, mu)
            rels.add(min(r, end))
            rows += 1
        if pred < end:
            ok(rels == {pred}, "%s class-%d: rels %s != rigid {%d}"
               % (F.name, c, sorted(rels), pred))
        else:
            ok(min(rels) == end, "%s class-%d: floor %s != %d"
               % (F.name, c, sorted(rels), end))
    check_identities(F, w, digs)
    return rows


# ------------------------------------------------------------ the zoo


D_SET = (-2, 2, -6, 6, -10, 10)


def scan_fields_32(rng, count=24):
    """Seeded random Eisenstein 32-ics: d + sparse even middles."""
    seen, out = set(), []
    while len(out) < count:
        key = [rng.choice(D_SET)] + [0] * 31
        for _ in range(rng.randrange(1, 5)):
            key[rng.randrange(1, 32)] = 2 * rng.randrange(1, 4)
        t = tuple(key)
        if t in seen:
            continue
        seen.add(t)
        out.append(t)
    return out


def run():
    rng = random.Random(192)
    print("== [A]/[B] the enumeration lemma ==")
    check_L1()
    check_L3()

    print("== [F] the general ladder vs the frozen ladders ==")
    import itertools
    for v in itertools.product((0, 1), repeat=5):        # mu8 e=4 top
        digs = [1] + list(v)
        ok(8 + ladder_rel(4, 2, digs) == mu8.rung(digs),
           "mu8.rung mismatch %s" % (v,))
    for v in itertools.product((0, 1), repeat=11):       # m16 e=8
        digs = [1] + list(v)
        ok(16 + ladder_rel(8, 3, digs) == m16.rung1(digs),
           "m16.rung1 mismatch %s" % (v,))
    for v in itertools.product((0, 1), repeat=3):
        digs = [1] + list(v) + [0] * 8
        ok(16 + ladder_rel(8, 2, digs) == m16.rung2(digs), "m16.rung2")
        ok(16 + ladder_rel(8, 1, digs) == m16.rung4(digs), "m16.rung4")
    vecs = [[0] * 23]                                     # m32 e=16 top
    vecs += [[1 if i == a else 0 for i in range(23)] for a in range(23)]
    vecs += [[1 if i in (a, b) else 0 for i in range(23)]
             for a in range(23) for b in range(a + 1, 23)]
    for _ in range(5000):
        vecs.append([rng.randrange(2) for _ in range(23)])
    for v in vecs:
        digs = [1] + list(v)
        ok(32 + ladder_rel(16, 4, digs) == m32.rung1_16(digs),
           "m32.rung1_16 mismatch")
    for v in itertools.product((0, 1), repeat=7):
        digs = [1] + list(v) + [0] * 16
        ok(32 + ladder_rel(16, 3, digs) == m32.rung2_16(digs), "rung2_16")
    for v in itertools.product((0, 1), repeat=3):
        digs = [1] + list(v) + [0] * 20
        ok(32 + ladder_rel(16, 2, digs) == m32.rung4_16(digs), "rung4_16")
    for v in ((0,), (1,)):
        digs = [1] + list(v) + [0] * 22
        ok(32 + ladder_rel(16, 1, digs) == m32.rung8_16(digs), "rung8_16")
    print("frozen ladders reproduced (e = 4, 8, 16, all classes)")

    print("== [C] regression witnesses (e = 8, 16) ==")
    for name, eis in (("x8-2", [-2, 0, 0, 0, 0, 0, 0, 0, 1]),
                      ("x8+2x4+2", [2, 0, 0, 0, 2, 0, 0, 0, 1]),
                      ("x8+2x-2", [-2, 2, 0, 0, 0, 0, 0, 0, 1])):
        F, w, digs = make_field(name, eis, 40)
        check_field_direct(F, w, digs, rng)
        print("  %s: digits %s ok" % (name, "".join(map(str, digs[1:12]))))
    for name, eis in (("x16-2", [-2] + [0] * 15 + [1]),
                      ("x16+2x8-6", [-6] + [0] * 7 + [2] + [0] * 7 + [1]),
                      ("x16+2x-2", [-2, 2] + [0] * 14 + [1])):
        F, w, digs = make_field(name, eis, 72)
        check_field_direct(F, w, digs, rng)
        print("  %s: digits %s ok" % (name, "".join(map(str, digs[1:24]))))

    print("== [C] THE e = 32 SCAN (sight-unseen) ==")
    hist = {}
    scan_zoo = []
    for key in scan_fields_32(rng):
        name = m32.poly_name(key)
        F, w, digs = make_field(name, list(key) + [1], 120)
        check_field_direct(F, w, digs, rng)
        r1 = 64 + ladder_rel(32, 5, digs)
        hist[r1] = hist.get(r1, 0) + 1
        scan_zoo.append((name, F, w, digs))
    print("  scan class-1 rung histogram: %s" % dict(sorted(hist.items())))

    print("== [C] designed spot rows (e = 32) ==")
    designed = [("x32+2x5-2", [-2, 0, 0, 0, 0, 2] + [0] * 26 + [1]),
                ("x32+2x-2", [-2, 2] + [0] * 30 + [1]),
                ("x32+2x16-2", [-2] + [0] * 15 + [2] + [0] * 15 + [1]),
                ("x32+2x16-6", [-6] + [0] * 15 + [2] + [0] * 15 + [1])]
    for j in (17, 18, 19):
        key = [-2] + [0] * 31
        key[16] = 2
        key[j] = 2
        designed.append((m32.poly_name(tuple(key)), key + [1]))
    for name, eis in designed:
        F, w, digs = make_field(name, eis, 120)
        check_field_direct(F, w, digs, rng)
        print("  %s: class-1 rung %d (digits-read)"
              % (name, 64 + ladder_rel(32, 5, digs)))
    for d in D_SET:                                       # RL4 pures
        name = "x32%+d" % (-d)
        F, w, digs = make_field(name, [d] + [0] * 31 + [1], 120)
        ok(all(digs[k] == 0 for k in range(1, 16)),
           "%s: pure digits not silent" % name)
        ok(64 + ladder_rel(32, 5, digs) == 80, "%s: pure rung != 80" % name)
        rels = set()
        for u in ad.sample_class(F, 1, 40, rng):
            rels.add(direct_rel(F, u, 5))
        ok(rels == {16}, "%s: spec1 %s != rigid {80}" % (name, rels))
        check_identities(F, w, digs)
    print("  pures: spec1 = {80} rigid x6")

    print("== [D] THE ZETA64 ANCHOR ==")
    eis = [int(math.comb(32, k)) for k in range(33)]
    eis[0] = 2
    F, w, digs = make_field("zeta64", eis, 120)
    z = tuple(F.cadd(a, b) for a, b in zip(F.one, mu8.pi_el(F)))
    zp = z
    for _ in range(5):
        zp = F.emul(zp, zp)
    ok(F.val(ad.esub(F, zp, ad.const_el(F, -1))) >= F.CAP,
       "zeta64^32 != -1")
    ok(set(k for k in range(1, NDIG32) if digs[k]) == {16, 40},
       "zeta64 digit vector: %s"
       % [k for k in range(1, NDIG32) if digs[k]])
    spec = m16.sampled_spec(F, rng, (1, 2, 4, 8, 16, 32), 50)
    for c, want in ((1, 112), (2, 80), (4, 72), (8, 68), (16, 66),
                    (32, 65)):
        ok(min(spec[c]) == want, "zeta64 spec%d min %s != %d"
           % (c, sorted(spec[c])[:3], want))
    tors = z                          # zeta64 class 1; squarings climb
    for c in (2, 4, 8, 16):           # zeta32/16/8/4: v(t - 1) = c
        tors = F.emul(tors, tors)
        ok(F.val(F.esub1(tors)) == c, "zeta64 torsion class %d" % c)
        o = F.orbit(tors)
        ok(o[-1] >= F.CAP, "zeta64 torsion class %d not CAP" % c)
    o = F.orbit(z)
    ok(o[-1] >= F.CAP, "zeta64 class-1 torsion not CAP")
    check_identities(F, w, digs)
    print("  zeta64: vector {16, 40}, spec mins 112/80/72/68/66/65, CAP x5")

    print("== [E] orbit ties (psi-gear + landing = 64 + rel) ==")
    for name, F, w, digs in scan_zoo[:5]:
        spec = m16.sampled_spec(F, rng, (1, 2, 4, 8, 16), 30)
        for mu in range(1, 6):
            c = 32 >> mu
            pred = ladder_rel(32, mu, digs)
            end = 3 * 32 // 2 if c == 1 else 1 << mu
            if pred < end:
                ok(min(spec[c]) == 64 + pred,
                   "%s: orbit landing class-%d %s != %d"
                   % (name, c, sorted(spec[c])[:3], 64 + pred))
        print("  %s: orbit landings match direct rels" % name)

    total = (CHECKS + lc.CHECKS + ad.CHECKS + mu8.CHECKS + m16.CHECKS
             + m32.CHECKS)
    print("ALL CHECKS PASSED: %d (this module %d + imported %d)"
          % (total, CHECKS, total - CHECKS))


if __name__ == "__main__":
    run()
