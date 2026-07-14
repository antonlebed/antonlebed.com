"""explore_deep_spectrum.py — THE ODD-p DEEP SPECTRUM: the
post-freedom fork/ceiling game as digit laws, and the odd-p
reduction law (the deep-spectrum remainder and an earlier hunch
cashed here).

THE QUESTION. The tame readout priced the FLOOR:
L = p*i* + min(delta, p^m). Above freedom the spectrum was never
charted — K9 lands {12, 16, 17, 18} with holes at 13-15, the
mid-fields are FORCED to stop at 13, and TR6's i-dagger = c(p-1)
coincidence defers freedom by a w-digit condition. Chart the whole
post-freedom game as digit laws, and cash an earlier hunch: an odd-p
REDUCTION LAW, thinner than p = 2's, via the p-adic digit diagonals
(digit k of b_i feeding level i + ke).

THE HAND DERIVATION (frozen before this
file existed). Setup as explore_tame_readout.py TR1: rel =
Lambda(a) - p*i*, Lambda = e*v_p + cA + W, sigma = s_p(p^{m+1} - A)
+ sum s_p(a_i), v_p = (sigma - 1)/(p - 1).

DR1 (THE ROUTE MAP). In-window routes have v_p <= 2 (tau_i^{p^{m-j}}
    needs j <= 1; the A <= p-1 shallow family at m >= 2 has v_p = 3
    and rel > e). rho_i's first entry: rel = i x p^m via tau_i^{p^m}
    for i < i-dagger = c(p-1) (FORKS, unit pivot -gamma_1 w);
    rel = e for i = i-dagger, where BOTH routes tau^{p^m} (one
    carry) and tau^{p^{m-1}} (two carries) coincide — i p^m =
    p^{m-1}(c(p-1)^2 + i) iff i = c(p-1) — with unit parts congruent
    mod p: the pivot w(kappa w - gamma_1) == w(w - 1) vanishes to
    depth delta: THE DEFERRAL; rel = p^{m-1}(c(p-1)^2 + i) for
    i > i-dagger via the single tau_i^{p^{m-1}} (v_p = 2, unit
    pivot +kappa w^2): FREE SAILING above rel e on the
    p^{m-1}-lattice.
DR2 (THE SLOT LATTICE). Every monomial rel in (p^m, e] is == 0 mod
    p^m (fork rels; the d >= 2 sigma = p family rel = p^m(c(d-1) +
    sum d_i i) always lands on them) or lies on {rel_c + p^{m-1} t :
    t = 0..i-dagger}, rel_c = c p^{m-1}(p-1)^2 = i*(p-1)^2/p
    (class-independent). Slots with t == -c mod p are the rho-route
    rels (forks below t = i-dagger, the deferral at t = i-dagger;
    i-dagger == -c mod p); the FORCED slots are t != -c mod p —
    c(p-2) + 1 of them, no fresh digit: D_t is a WORD FUNCTION.
    Hole iff D_t = 0 (walkers pass), ceiling iff D_t != 0 (game
    over). At m = 1, c = 1: slots are rels rel_c..e consecutively.
DR3 (THE FIRST SLOT). D at rel_c = rho_0(w_0^2 - w_{rel_c}) exactly
    (gate-branch ladder digit -w_{rel_c} + the tau_0^{p^{m-1}} term,
    kappa_0 = C(p^{m+1}, p^{m-1})/p^2 == 1 == gamma_1 mod p): the
    gate-open dichotomy HOLE iff w_{rel_c} = 1. K9's 13-hole
    (w_4 = 1) and the mid-field {13} ceiling (w = 1 exactly:
    w_4 = 0) are two values of the ONE digit w_{rel_c}.
DR4 (THE TORSION DETECTOR — Krasner). Above rel e every rel (on the
    p^{m-1}-lattice) has a fresh unit pivot, so a walker passing
    every forced slot extends digit-by-digit to v(u^{p^{m+1}} - 1)
    = infinity, i.e. a primitive zeta_{p^{m+1}} IN K; conversely
    Krasner bounds non-torsion landings by the (p, e)-geometric
    conjugate distances. So: gate-open + ALL forced slots holes
    <=> zeta_{p^{m+1}} in K, and the all-holes word class is
    EXACTLY the anchor's word. Non-torsion gate-open-deep fields
    have a FINITE ceiling at their first non-hole slot; torsion
    fields' spectra are infinite lattices (censuses print sampled
    prefixes).
DR5 (THE ODD-p REDUCTION LAW — an earlier hunch cashed). The game
    never reads w past depth e (gate w_0, ladder w_1..w_{p^m-1},
    slots [rel_c, e], the deferral pivot w_delta). By the diagonal
    pricing (digit k of b_i enters at level i + ke, digit k of d at
    level ke; w = -1/(d - sum b_i pi^i)), w mod pi^{e+1} is a
    function of EXACTLY (b_1..b_{e-1} mod p; d mod p^2): the k = 1
    diagonal enters at level >= e + 1 entirely — odd p has NO gamma
    layer (p = 2's b_i mod 4 below e/2 exists because its window
    3e/2 - 1 exceeds e). THE ODD-p WORD = (w_0..w_e), length e + 1,
    w_0 in F_p^* (the gate is a free digit; p = 2's always-open
    gate is the F_2 pigeonhole). Counts match: p^{e-1} * p(p-1) =
    (p-1)p^e. BONUS over p = 2: eta-change perturbs w at depth
    v(eta^{-e} - 1) >= v_pi(e) + 1 >= e + 1 (p | e at arrival
    windows), so the whole word is pi-INVARIANT — a field
    invariant, where p = 2's deep word digits are pi-covariant.
DR6 (THE SKELETON TWIST). reduce(Phi_9(x+1)) = x^6 + 6x^5 + 6x^4 +
    3x^3 + 3 (b mod 3 = [0,0,1,2,2], d = -1) shares K9's word, so
    by DR4 it CONTAINS zeta_9 — the odd-p skeleton design is not a
    mimic (p = 2's 3-term design walks stopless in a NON-cyclotomic
    field) but the anchor field itself in reduced dress: at odd p
    the anchor's grid class has exactly one member field. The
    stopless-mimic option was a wildness privilege.

THE PREDICTIONS (fixed before the run, including a later Krasner
revision, hand-attacked before this file existed; a miss falsifies
its lemma):

DS-A (route map brute; scopes (3,1,1), (3,2,1), (5,1,1), (3,1,2)):
     (i) window rels on the fork/slot lattice; (ii) first-entry
     rels as DR1, both routes at rel e for i-dagger; (iii) gamma_1
     == kappa_0 == 1 mod p; (iv) fresh singles at e + p^{m-1},
     e + 2p^{m-1}; (v) the rel_c monomial list = the single
     tau_0^{p^{m-1}} where p does not divide c; 5-distinct-index
     bound clears relmax per scope.
DS-B (the w_{rel_c} dichotomy, designed pair at p = 3, e = 6):
     x^6+3x^4+3 (delta 4, w_4 = 2): class-1 spectrum {12, 13}.
     x^6-3x^4+3 (delta 4, w_4 = 1): {12, 14} — hole 13 (the
     dichotomy), ceiling 14 (D_5 = [rho_1](w^2)_0 = -rho_0^2 != 0).
     Three-field ceiling ladder 13/13/14 at C / +3x^4 / -3x^4.
DS-C (deep spectra at censused fields, never censused deep):
     x^18+3 class (3,1): lattice {30,33,36,39,42,43}, holes 40, 41,
     ceiling 43; class (1,2): {36, 39}, holes 37, 38 (between-slot
     ladder rels), ceiling 39 at rel_c = 12. x^18+3x^5+3 class
     (3,1): {30, 32} (ladder ceiling rel 5). x^12+3 class (2,1):
     {21, 24, 26} = freedom 3 + fork 6 + ceiling rel_c = 8 (t = 0
     forced, fork 9 unreachable) — regression.
     C/D class-1 {12, 13}; K9 class-1 visited {12, 16, 17, 18}
     within [12, 18], then torsion (DS-D iii).
DS-D (THE REDUCTION LAW): (i) word pi-invariance under sampled eta;
     (ii) deep perturbations (b_i += 3, d += 9) of C and the DS-B
     designs: words AND climb profiles (visited set + stick)
     unchanged; (iii) THE TWIN reduce(Phi_9(x+1)) = eis
     [3,0,0,3,6,6,1]: word == K9's, visited cap [12,18] ==
     {12,16,17,18}, and the climb passes CAP: the torsion detector
     fires — zeta_9 constructed in the twin (Krasner: the twin IS
     Q_3(zeta_9)); at K9 the climb also passes CAP; at C and the
     DS-B designs it STICKS at the ceiling; (iv) the bijection: all
     3^5 x 6 = 1458 grid words at e = 6 pairwise distinct;
     (v) cross-p: reduce(Phi_25(x+1)) word == Phi_25(x+1)'s word to
     depth 21 (b mod 5, d mod 25).

THE DESIGN. Machinery imported from explore_tame_readout (LF
censuses, w_element/w_digits, enumerate_window, law_row). THE CLIMB
is the new primitive: from a floor walker, greedily perturb one
digit u -> u(1 + [a]pi^k) (k > c: class-preserving) whenever
v(u^{p^{m+1}} - 1) increases; the visited set = the achievable
landings >= floor (each step's rejected digits witness the current
value; holes are skipped automatically), the stick = the ceiling,
and passing CAP = the constructive Krasner walk to torsion. Every
censused field also passes law_row (floor regression). Labels never
read orbits; the engine only ever reads MEASURED digits.
Run: python prime/code/explore_deep_spectrum.py

FINDINGS (entered post-run, copied from printed output).

1. THE SLOT GAME (rule in range; enumeration brute at (3,1,1),
   (3,2,1), (5,1,1), (3,1,2), censuses at p = 3): the post-freedom
   game quantizes on the fork/slot lattice of DR1/DR2 — every
   monomial rel in (p^m, e] is a fork rel i x p^m or a slot
   rel_c + p^{m-1}t, forced slots carry no fresh digit, fresh
   singles ride the p^{m-1}-lattice above e. Each forced slot is a
   hole or a ceiling READING THE WORD: D_{rel_c} = rho_0(w_0^2 -
   w_{rel_c}) exact (gate-open: hole iff w_{rel_c} = 1 — K9's
   13-hole vs the mid-field {13} ceiling, two values of one digit);
   the designed pair splits the dichotomy on cue (w_4 = 2: {12, 13};
   w_4 = 1: holes 13-15, sailing 16+). The next slot at (3,1,1)
   measures D = -rho_0(w_3 + w_5) (derived here as the slot-1 law
   -(w_{p^m} + w_{rel_c+p^{m-1}}) of the reciprocal law,
   explore_slot_algebra.py finding 2; design 0+0 passes, probe 0+1
   ceils at {12, 14}, K9 2+1 == 0 passes). The m = 2 and c > 1 faces called
   sight-unseen: x^18+3 class (3,1) lands exactly the predicted
   lattice {30,33,36,39,42,43} (holes 40, 41; ceiling 43 via
   rho_4 = rho_0), class (1,2) {36, 39} (ceiling at rel_c = 12);
   x^12+3 class (2,1) {21, 24, 26} (ceiling rel_c = 8, fork 9
   unreachable) — re-derived as freedom + fork +
   slot; x^18+3x^5+3 class (3,1) {30, 32} (ladder ceiling rel 5).

2. THE TORSION DETECTOR (rule, Hensel-certified by the climb;
   SCOPE m = 1 EXACTLY, where every rel above e is a fresh digit —
   at m >= 2 the p^{m-1}-lattice leaves forced between-rels above
   e, and the word-criterion FAILS there by designed witness:
   x^18+6x^12-24 passes the whole window without zeta_27; the sail
   reads the grid diagonal-by-diagonal above e,
   explore_above_window.py): sailing past the window <=>
   zeta_{p^{m+1}} in K (torsion => sail holds at every m). The climb is
   CONSTRUCTIVE: greedy digit ascent past v = 30 gives Hensel
   margin v(Phi_9(u)) >= 27 > 18 = 2 v(Phi_9') — zeta_9 is thereby
   constructed in x^6-3x^4+3 and in reduce(Phi_9(x+1)); non-torsion
   words ceil in-window (the probe; C/D; every DS-C field).
   COROLLARY: THE 2-TERM DESIGN x^6 - 3x^4 + 3 GENERATES
   Q_3(zeta_9). The odd-p twist on the earlier skeleton hunch: at p = 2 the
   3-term design MIMICS the anchor's readout in a different field
   (stopless through a finite window); at odd p the window is
   followed by open-ended sailing, so passing it FORCES the torsion
   in — no mimic exists, the design IS the anchor field. The
   stopless-mimic option is a wildness privilege.

3. THE ODD-p REDUCTION LAW (theorem — the diagonal pricing is exact
   algebra; spectra rule in range): the word (w_0..w_e), length
   e + 1, is a function of EXACTLY (b_1..b_{e-1} mod p; d mod p^2);
   odd p has NO gamma layer — the k = 1 diagonal enters at e + 1
   exactly (witnessed live: the cross-p row first compared depth
   e + 1 and FAILED on b_1's second bit; at depth e it is
   identical). The grid -> word map is a BIJECTION at e = 6
   (1458/1458 words distinct = (p-1)p^e). Deep perturbations
   (b_i += 3, d += 9) move neither word nor climb profile (4
   pairs). Cross-p: reduce(Phi_25(x+1)) prints Z25's word verbatim
   to depth 20. reduce(Phi_9(x+1)) = x^6 + 6x^5 + 6x^4 + 3x^3 + 3
   (b mod 3 = [0,0,1,2,2], d = -1).

4. THE WORD IS A CHART, NOT A FIELD INVARIANT (rule in range;
   corrects DR5's invariance clause; the exact action derived in
   explore_slot_algebra.py finding 4): the element twist obeys
   v(eta^{-e} - 1) = p^m k (at (3,1,1): 3k — the class-1 sample
   moves w_3 on cue), chart re-expansion mixes digit r to depth
   r + k (dead at p | r); full invariance from k > i-dagger =
   c(p-1) — "k >= i*" was the (c,m) = (1,1) coincidence. The
   SPECTRUM is the field invariant, made word-level exact:
   K9's genuine chart-word set is EXACTLY the 3-word solution
   variety of its forced-digit laws {w_4 = 1, w_5 = -w_3, w_6 =
   w_3^2} (K9's [1,0,0,2,1,1,1] ~ the design's [1,0,0,0,1,0,0] ~
   [1,0,0,1,1,2,1]). CAVEAT: section_d(i)'s printed vectors
   are MIXED-PAIR artifacts — w_digits divides by its own argument,
   so (old pi, new w) extracts along neither chart; they witness
   prefix depth only and are NOT chart words (the [1,0,0,1,1,1,0]
   vector violates w_5 = -w_3).

PRE-GREEN FAILURES (three, adjudicated in-session — the slate paid
its way; see git history):
(1) DS-B froze {12, 14} for x^6-3x^4+3: run 1 printed {12} u
    [16, ..]. The hand D_5 dropped the rho_1-pass's w_3 part and
    the tau_0^2 companion; the corrected slot digit -rho_0(w_3+w_5)
    fits all three censused words.
(2) The interim Krasner-cap revision predicted the
    design sticks below CAP: run 2's climb reached CAP, and the
    Hensel margin proves zeta_9 IN the design — the derivation's
    pi-invariance "bonus" (DR5) was wrong (char-p binomial; TR5's
    boundary was already the settled truth); the design is
    Q_3(zeta_9) in another chart, and finding 4 is the corrected
    law. DR4's "all-holes word class = the anchor's word" scopes to
    the anchor's eta-ORBIT of words.
(3) The cross-p row compared depth e + 1, where the k = 1 diagonal
    of b_1 lives: the failure was the diagonal pricing firing on
    cue; fixed to depth e.

RUN RECORD (python explore_deep_spectrum.py, ~6 s, exit 0): 140
checks this module + 49,791 through the imported census/gear
machinery. Printed rows as copied: [A] 4 scopes lattice clean
(forks/slots/forced 1/3/2, 3/5/3, 3/5/4, 1/3/2; relmax 8/14/22/21);
[B] +3x^4 {12,13}, -3x^4 {12,16,17,18,19,20,...}, probe {12,14},
C/D {12,13}, K9 {12,16,17,18,19,21,...} digs [0,0,2,1,1]; [C]
x^12+3 2->{21,24,26}; x^18+3 1->{36,39}, 3->{30,33,36,39,42,43};
x^18+3x^5+3 3->{30,32}; [D] K9 word [1,0,0,2,1,1,1], mixed-pair
vectors [1,0,0,1,1,1,0] / [1,0,0,2,1,1,2]; twin word == K9's, climb -> CAP;
1458/1458; Phi_25 word match at depth 20.
"""

import itertools
import random
from math import comb

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


# ---------------------------------------------------------------- [A]


def section_a():
    print("\n[A] DS-A: the route map — forks, slots, deferral, sailing")
    for p, c, m in [(3, 1, 1), (3, 2, 1), (5, 1, 1), (3, 1, 2)]:
        pm, pm1 = p ** m, p ** (m - 1)
        n = p ** (m + 1)
        istar, e = c * pm, c * (p - 1) * pm
        idag = c * (p - 1)
        relc = c * pm1 * (p - 1) ** 2
        relmax = e + 2 * pm1
        # 5-distinct-index exclusion must clear relmax. Cases: v_p = 1
        # forces sum s_p >= 5 with sigma = p, so A = p^{m+1} exactly
        # (possible only at p >= 5): rel = e + W >= e + 10; v_p >= 2:
        # rel >= 2e + 5c + 10 - p*i* = e(p-2)/(p-1) + 5c + 10.
        def bound_ok(r):
            v2 = e * (p - 2) + (p - 1) * (5 * c + 10) > r * (p - 1)
            v1 = p < 5 or e + 10 > r
            return v1 and v2
        while not bound_ok(relmax):
            relmax -= pm1
        ok(relmax >= e + pm1, "(%d,%d,%d): relmax too tight" % (p, c, m))
        w = tr.enumerate_window(p, c, m, relmax)
        slots = set(relc + pm1 * t for t in range(idag + 1))
        ok(max(slots) == e, "(%d,%d,%d): slot lattice must end at e"
           % (p, c, m))
        # (i) window rels on the fork/slot lattice
        for rel in w:
            if pm < rel <= e:
                ok(rel % pm == 0 or rel in slots,
                   "(%d,%d,%d): off-lattice rel %d: %s"
                   % (p, c, m, rel, w[rel]))
        # (ii) first-entry rels per index
        first = {}
        for rel in sorted(w):
            for mono in w[rel]:
                for _, i in mono:
                    first.setdefault(i, rel)
        for i in range(1, idag):
            ok(first.get(i) == i * pm,
               "(%d,%d,%d): rho_%d first entry %s != %d"
               % (p, c, m, i, first.get(i), i * pm))
        ok(first.get(idag) == e,
           "(%d,%d,%d): rho_idag first entry %s != e" % (p, c, m,
                                                         first.get(idag)))
        both = [mo for mo in w[e] if any(i == idag for _, i in mo)]
        ok(sorted(both) == sorted([((pm, idag),), ((pm1, idag),)]),
           "(%d,%d,%d): coincidence routes %s" % (p, c, m, both))
        # (iii) unit parts
        g1 = comb(n, pm) // p
        k0 = comb(n, pm1) // (p * p)
        ok(g1 % p == 1 and k0 % p == 1,
           "(%d,%d,%d): gamma_1/kappa_0 = %d/%d != 1 mod p"
           % (p, c, m, g1 % p, k0 % p))
        # (iv) fresh singles above e on the p^{m-1}-lattice
        for t in (1, 2):
            rel = e + t * pm1
            if rel > relmax:
                continue
            ok(first.get(idag + t) == rel,
               "(%d,%d,%d): sailing single at rel %d missing (%s)"
               % (p, c, m, rel, first.get(idag + t)))
        # (v) the rel_c monomial list (p not dividing c scopes)
        if c % p:
            ok(sorted(w[relc]) == [((pm1, 0),)],
               "(%d,%d,%d): rel_c list %s" % (p, c, m, w[relc]))
        # forced slots carry no fresh digit
        for t in range(idag + 1):
            if t % p == (-c) % p:
                continue
            rel = relc + pm1 * t
            for mono in w.get(rel, []):
                for _, i in mono:
                    ok(first[i] < rel,
                       "(%d,%d,%d): fresh digit rho_%d at forced slot %d"
                       % (p, c, m, i, rel))
        print("  (p,c,m)=(%d,%d,%d): lattice clean, forks %d, slots %d"
              " (forced %d), sailing fresh, relmax %d"
              % (p, c, m, idag - 1, idag + 1, c * (p - 2) + 1, relmax))


# ------------------------------------------------------------ the climb


def epow(F, u, n):
    r, b = F.one, u
    while n:
        if n & 1:
            r = F.emul(r, b)
        b = F.emul(b, b)
        n >>= 1
    return r


def land(F, u, P):
    return F.val(ad.esub(F, epow(F, u, P), ad.const_el(F, 1)))


def climb(F, u, c, P, cap):
    """Greedy one-digit ascent with a full neighbor scan at every
    accepted walker (class-preserving: k > c). Every scan landing is
    witnessed by a genuine class-c unit u*s; a walker at v passes
    every rel below v, so one digit-change stops it at any fork
    below v — the collected set is exactly the achievable landings
    up to the stick. Returns (achieved set, stick value); stick >=
    cap means torsion (the constructive Krasner walk)."""
    steps = []
    for k in range(c + 1, F.amax):
        i, j = divmod(k, F.e)
        for a in range(1, F.p):
            s = [list(cc) for cc in F.one]
            s[j][0] = (s[j][0] + tr.teich(F, a) * (F.p ** i)) % F.pM
            steps.append(epow(F, tuple(tuple(cc) for cc in s), P))
    one = ad.const_el(F, 1)
    uP = epow(F, u, P)
    v = F.val(ad.esub(F, uP, one))
    achieved = {v}
    while v < cap:
        nxt = None
        for sP in steps:
            w = F.val(ad.esub(F, F.emul(uP, sP), one))
            achieved.add(w)
            if w > v and (nxt is None or w < nxt[0]):
                nxt = (w, sP)
        if nxt is None:
            break
        v = nxt[0]
        uP = F.emul(uP, nxt[1])
    return achieved, v


def floor_walker(F, c, rng, batch=60):
    us = list(ad.sample_class(F, c, batch, rng))
    P = 1
    t = c
    while t < F.seat:
        t *= F.p
        P *= F.p
    P *= F.p
    lo = min(us, key=lambda u: land(F, u, P))
    return lo, P


def climb_row(F, c, rng, want_visited, want_stick, cap=None):
    """want_stick None => torsion: climb must pass cap; want_visited
    compared within [floor, max(want_visited)]."""
    if cap is None:
        cap = F.CAP
    u, P = floor_walker(F, c, rng)
    ach, stick = climb(F, u, c, P, cap)
    hi = max(want_visited)
    got = sorted(x for x in ach if min(want_visited) <= x <= hi)
    ok(got == sorted(want_visited),
       "%s: class %d achieved %s != %s" % (F.name, c, got, want_visited))
    if want_stick is None:
        ok(stick >= cap, "%s: class %d climb stuck at %d, not torsion"
           % (F.name, c, stick))
    elif want_stick == "sub":
        ok(stick < cap, "%s: class %d climb reached cap %d: torsion in a"
           " field whose word forbids it" % (F.name, c, stick))
    else:
        ok(stick == want_stick, "%s: class %d stick %d != %d"
           % (F.name, c, stick, want_stick))
    return got, stick


# ---------------------------------------------------------------- [B]


def section_b(rng, results):
    print("\n[B] DS-B: the w_rel_c dichotomy at e = 6 — hole vs ceiling")
    e6 = [
        ("x^6+3x^4+3", [3, 0, 0, 0, 3, 0, 1]),
        ("x^6-3x^4+3", [3, 0, 0, 0, -3, 0, 1]),
        ("x^6-3x^5-3x^4+3", [3, 0, 0, 0, -3, -3, 1]),
        ("x^6+3 (C)", [3, 0, 0, 0, 0, 0, 1]),
        ("x^6-6 (D)", [-6, 0, 0, 0, 0, 0, 1]),
        ("zeta9 (K9)", [3, 9, 18, 21, 15, 6, 1]),
    ]
    for name, eis in e6:
        F, spec, delta, digs, orbits = tr.field_readout(
            name, 3, eis, 30, [1, 3], rng)
        tr.law_row(F, spec, delta, 3)
        results[name] = (F, spec, delta, digs)
        print("  %-12s delta=%-3s digs=%s %s"
              % (name, tr.fmt_delta(F, delta), digs[1:6],
                 ad.fmt_spec(F, spec)))
    # designed digits
    F, spec, delta, digs = results["x^6+3x^4+3"]
    ok(delta == 4 and digs[4] == 2, "+3x^4: delta/w4 %d/%s" % (delta, digs))
    ok(spec[1] == {12, 13}, "+3x^4: class-1 %s" % sorted(spec[1]))
    climb_row(F, 1, rng, [12, 13], 13)
    F, spec, delta, digs = results["x^6-3x^4+3"]
    ok(delta == 4 and digs[4] == 1,
       "-3x^4: delta/w4 %d/%s" % (delta, digs))
    ok(not spec[1] & {13, 14, 15},
       "-3x^4: hole range hit: %s" % sorted(spec[1]))
    climb_row(F, 1, rng, [12, 16, 17, 18], None)
    F, spec, delta, digs = results["x^6-3x^5-3x^4+3"]
    ok(delta == 4 and digs[4] == 1 and digs[5] == 1,
       "probe: delta/w4/w5 %d/%s" % (delta, digs))
    ok(spec[1] == {12, 14}, "probe: class-1 %s" % sorted(spec[1]))
    climb_row(F, 1, rng, [12, 14], 14)
    for name in ["x^6+3 (C)", "x^6-6 (D)"]:
        F, spec, delta, digs = results[name]
        ok(spec[1] == {12, 13}, "%s: class-1 %s" % (name, sorted(spec[1])))
        climb_row(F, 1, rng, [12, 13], 13)
    F, spec, delta, digs = results["zeta9 (K9)"]
    ok({x for x in spec[1] if x < F.CAP} <= {12} | set(range(16, F.CAP)),
       "K9: landing in the hole range: %s" % sorted(spec[1]))
    vis, stick = climb_row(F, 1, rng, [12, 16, 17, 18], None)
    print("  slots read the word: w4 = 2 ceils 13; w4 = 1, w3+w5 = 1"
          " ceils 14;\n    w4 = 1, w3+w5 = 0 SAILS: x^6-3x^4+3 climbs"
          " to CAP — Hensel: zeta_9 in it")


# ---------------------------------------------------------------- [C]


def section_c(rng):
    print("\n[C] DS-C: deep spectra at the censused e = 12/18 fields")
    F, spec, delta, digs, orbits = tr.field_readout(
        "x^12+3", 3, [3] + [0] * 11 + [1], 32, [2, 6], rng,
        n_heavy=300, n_light=20)
    tr.law_row(F, spec, delta, 3)
    ok({x for x in spec[2] if x < F.CAP} == {21, 24, 26},
       "x^12+3: class-2 %s != {21,24,26}" % sorted(spec[2]))
    climb_row(F, 2, rng, [21, 24, 26], 26)
    print("  x^12+3       %s  (regression: fork 6, ceiling rel_c = 8)"
          % ad.fmt_spec(F, spec))
    F, spec, delta, digs, orbits = tr.field_readout(
        "x^18+3", 3, [3] + [0] * 17 + [1], 48, [1, 3, 9], rng,
        n_heavy=300, n_light=15)
    tr.law_row(F, spec, delta, 3)
    lat3 = {30, 33, 36, 39, 42, 43}
    ok({x for x in spec[3] if x < F.CAP} <= lat3,
       "x^18+3: class-3 off-lattice %s" % sorted(spec[3]))
    climb_row(F, 3, rng, sorted(lat3), 43)
    ok({x for x in spec[1] if x < F.CAP} <= {36, 39},
       "x^18+3: class-1 off-lattice %s" % sorted(spec[1]))
    climb_row(F, 1, rng, [36, 39], 39)
    print("  x^18+3       %s  (holes 40, 41; ceilings 43 / 39)"
          % ad.fmt_spec(F, spec))
    F, spec, delta, digs, orbits = tr.field_readout(
        "x^18+3x^5+3", 3, [3, 0, 0, 0, 0, 3] + [0] * 12 + [1], 48,
        [1, 3, 9], rng, n_heavy=300, n_light=15)
    tr.law_row(F, spec, delta, 3)
    ok({x for x in spec[3] if x < F.CAP} == {30, 32},
       "x^18+3x^5+3: class-3 %s != {30,32}" % sorted(spec[3]))
    climb_row(F, 3, rng, [30, 32], 32)
    print("  x^18+3x^5+3  %s  (ladder ceiling rel 5)"
          % ad.fmt_spec(F, spec))


# ---------------------------------------------------------------- [D]


def word_of(name, p, eis, depth):
    """The word (w_0..w_depth) via a digit twin at small amax."""
    e = len(eis) - 1
    Fd = lc.LF(name + "-w", p, [0, 1], eis, depth + 7)
    w, pi = tr.w_element(Fd)
    return tr.w_digits(Fd, w, pi, depth + 1)


def reduce_eis(p, eis):
    """The grid representative: b_i mod p, d mod p^2."""
    e = len(eis) - 1
    d = (-(eis[0] // p)) % (p * p)
    if d > p * p - p:
        d -= p * p          # small representative of d mod p^2
    out = [(-p * d)] + [p * ((eis[i] // p) % p) for i in range(1, e)] + [1]
    return out


def section_d(rng, results):
    print("\n[D] DS-D: THE ODD-p REDUCTION LAW — word, twin, bijection")
    # (i) prefix depth of the eta-action: preserved to 3k (the char-p
    # binomial of eta^{-e} - 1). NOTE: these vectors are
    # MIXED-PAIR extractions (w_digits divides by its own argument;
    # (old pi, new w) follows neither chart) — prefix witnesses only,
    # NOT chart words; the true orbit action (matched pairs, the
    # 3-word variety, the k > i-dagger boundary):
    # explore_slot_algebra.py section [O].
    Fd = lc.LF("K9-winv", 3, [0, 1], [3, 9, 18, 21, 15, 6, 1], 15)
    w, pi = tr.w_element(Fd)
    base = tr.w_digits(Fd, w, pi, 7)
    moved = []
    for t in range(4):
        eta = next(iter(ad.sample_class(Fd, 1 + t, 1, rng)))
        if t == 3:  # include a Teichmueller factor [2]
            eta = tuple(tuple((tr.teich(Fd, 2) * x) % Fd.pM for x in cc)
                        for cc in eta)
        inv = tr.unit_inv(Fd, epow(Fd, eta, 6))
        w2 = tr.w_digits(Fd, Fd.emul(w, inv), pi, 7)
        dep = min(3 * (1 + t), 7)
        ok(w2[:dep] == base[:dep],
           "eta in U_%d moved the word above depth %d: %s vs %s"
           % (1 + t, dep, w2, base))
        if w2 != base:
            moved.append((1 + t, w2))
    ok(any(k < 3 for k, _ in moved),
       "no shallow eta moved the word: covariance witness missing")
    print("  eta in U_k preserves depth 3k (mixed-pair prefix witness;"
          " the true orbit\n    action: explore_slot_algebra.py [O]);"
          " K9's word %s vs mixed-pair\n    vectors %s"
          % (base, [m[1] for m in moved[:2]]))
    # (ii) deep-perturbation pairs: word + climb profile unchanged
    pairs = [
        ("C+9x^2", [3, 0, 9, 0, 0, 0, 1], "x^6+3 (C)", [12, 13], 13),
        ("C d+9", [-24, 0, 0, 0, 0, 0, 1], "x^6+3 (C)", [12, 13], 13),
        ("-3x^4+9x", [3, 9, 0, 0, -3, 0, 1], "x^6-3x^4+3",
         [12, 16, 17, 18], None),
        ("-3x^4 d+9", [-24, 0, 0, 0, -3, 0, 1], "x^6-3x^4+3",
         [12, 16, 17, 18], None),
    ]
    bases = {"x^6+3 (C)": [3, 0, 0, 0, 0, 0, 1],
             "x^6-3x^4+3": [3, 0, 0, 0, -3, 0, 1]}
    for name, eis, basename, wantv, wants in pairs:
        ok(word_of(name, 3, eis, 6) ==
           word_of(basename, 3, bases[basename], 6),
           "%s: word moved off %s" % (name, basename))
        F = lc.LF(name, 3, [0, 1], eis, 30)
        climb_row(F, 1, rng, wantv, wants)
    print("  4 deep perturbations (b_i += 3, d += 9): word + climb frozen")
    # (iii) THE TWIN: reduce(Phi_9(x+1)) is the anchor field itself
    twin = reduce_eis(3, [3, 9, 18, 21, 15, 6, 1])
    ok(twin == [3, 0, 0, 3, 6, 6, 1], "twin eis %s" % twin)
    ok(word_of("twin", 3, twin, 6) ==
       word_of("K9", 3, [3, 9, 18, 21, 15, 6, 1], 6),
       "twin word != K9 word")
    Ft = lc.LF("reduce(Phi9)", 3, [0, 1], twin, 30)
    climb_row(Ft, 1, rng, [12, 16, 17, 18], None)
    print("  reduce(Phi_9(x+1)) = x^6+6x^5+6x^4+3x^3+3: word == K9's,"
          "\n    climb -> CAP (Hensel margin 27 > 18): zeta_9 in the twin")
    # (iv) the bijection at e = 6: all 1458 grid words distinct
    words = set()
    for bs in itertools.product(range(3), repeat=5):
        for d in (1, 2, 4, -4, -2, -1):
            eis = [-3 * d] + [3 * b for b in bs] + [1]
            words.add(tuple(word_of("g", 3, eis, 6)))
    ok(len(words) == 1458, "grid words: %d distinct != 1458" % len(words))
    print("  the bijection: 1458/1458 grid words distinct at e = 6")
    # (v) cross-p: the Phi_25 anchor and its reduction share the word
    phi25 = [sum(comb(5 * j, k) for j in range(5)) for k in range(21)]
    r25 = reduce_eis(5, phi25)
    ok(word_of("Z25", 5, phi25, 20) == word_of("rZ25", 5, r25, 20),
       "Phi_25 reduction word mismatch")
    print("  cross-p: reduce(Phi_25(x+1)) word == Z25's word (depth e = 20)")


# ------------------------------------------------------------------- run


def run():
    rng = random.Random(198)
    print("THE ODD-p DEEP SPECTRUM — the post-freedom game + reduction law")
    print("=" * 66)
    results = {}
    section_a()
    section_b(rng, results)
    section_c(rng)
    section_d(rng, results)
    print("\nALL GREEN — %d checks this module (+%d imported machinery)"
          % (CHECKS, tf.CHECKS + tr.CHECKS))


if __name__ == "__main__":
    run()
