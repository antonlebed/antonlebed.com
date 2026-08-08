"""explore_above_window.py — THE m >= 2 ABOVE-WINDOW SAIL: what
stops a window-passing walker above e, and what the stopping digit
reads (the torsion detector's unprobed direction).

THE QUESTION. The torsion detector (explore_deep_
spectrum.py finding 2) is scoped m = 1: "sailing past the window <=>
zeta_{p^{m+1}} in K" was proved only where every rel above e is a
fresh digit. At m >= 2 the p^{m-1}-lattice leaves FORCED between-rels
above e, and NO m >= 2 field has ever been observed above its window
(x^18+3 class (1,2) ceils in-window at rel 12; every censused deep
field is m = 1). Triangle-design a (3,1,2) word passing every
in-window slot: what stops it above e = 18, and does the sail =>
torsion direction survive as a WORD criterion?

THE HAND DERIVATION (worked by hand in stages 1-2, 4-5, before this
file existed).

AW1 (THE SCOPE). (p, c, m) = (3, 1, 2): e = 18, i* = 9, i-dagger =
    2, rel_c = 12, P = 27, landing = 27 + rel. In-window: fork rel 9
    (fresh s_1), slots {12, 15, 18} (t = 2 the deferral), between
    rels 10, 11, 13, 14, 16, 17 forced with digit -w_r. Slot forms
    (the reciprocal law, K = w_9 z): D_0 = 1 - w_12, D_1 =
    -(w_9 + w_15), deferral residual w_9^2 - w_18. THE DESIGNED PASS
    WORD (regime w_j = 0 for 0 < j < 9; take w_9 = 0):
    [1, 0 x 11, 1, 0 x 6] — every in-window forced digit a hole.
AW2 (ABOVE THE WINDOW). The 5-PART CLEARANCE extends the route map
    to rel 29: sigma >= 5 odd and sigma = 5 forces s_3(27 - A) = 0,
    A = 27, Lambda >= 73 (rel >= 46); sigma >= 7 gives Lambda >= 69
    (rel >= 42) — the 4-index enumeration is complete to rel 29.
    Fresh singles ride the 3-lattice (21, 24, 27); the between set
    {19, 20, 22, 23, 25, 26, 28, 29} is predicted monomial-free, so
    a between-rel r reads the PURE deep chart digit: D_r = -w_r x
    unit (cross terms need monomial content at r - 12 or r - 9
    against word digits that are zero here). By the diagonal pricing
    (DR5, theorem) digit 1 of b_i enters at level i + e: the eight
    between-rels through 29 are owned by b_1, b_2, b_4, b_5, b_7,
    b_8, b_10, b_11 mod 9 — data the word (w_0..w_18) does NOT
    carry. d's digit 2 enters at 2e = 36: d += 9 is INVISIBLE
    through depth 29.
AW3 (THE CLIMB MACHINERY IS INCOMPLETE AT m = 2 — pass 5). Pure
    steps 1 + [a]pi^k map k -> v(s^27 - 1) = 36, 48, 51, 54, 57, 60
    (k = 2, 4..8 rigid), 30 (k = 3, seat tie) [FALSIFIED by a later
    run: k = 3 lands {54, 73} — the seat tie cancels and the next step is
    rigid +e, so v >= 54; a hand note error, never engine-read —
    the pool groups by MEASURED v; explore_shallow_route.py
    finding 4], 64.. contiguous
    (k > 9), 75 / 64+j (k = 9: the seat tie cancels at w_0 = 1 —
    Teichmueller [a]^3 = [a]; pure lands 27 + delta + 36, hybrids
    1 + [a]pi^9 + [b]pi^{9+j} land 63 + j). NOTHING lands 63 =
    27 + 2e. At m = 1 the deep classes k + 2e covered every
    above-window level — why the m = 1 climb was complete. The
    engine therefore climbs with pool = pure steps + seat hybrids +
    census mates (another class-1 walker, accepted only if the
    product stays class 1). Forced rels stay uncancelable by mates
    (the forced digit is walker-independent up to rho_0, and
    canceling it forces the product out of class 1).

THE PREDICTIONS FIXED BEFORE THE RUN (worked by hand in stages 3-5,
before this file existed; a miss falsifies its lemma):

S1 (the pass): the designed field D = solve_word(3, 18,
   [1,0^11,1,0^6]) has class-1 landings ONLY at 36 and 27 + r* in
   [36, 45 + ...]: the whole window 37..45 is holes (sampled
   census), r* = the first between-rel > 18 with deep chart digit
   w_r != 0.
S2 (the stop): the climb from the class-1 floor sticks at 27 + r*
   — at a BETWEEN rel (not on the 3-lattice, not in-window, not
   CAP). Stick < CAP proves no zeta_27 (torsion => sail: forced
   digits are walker-independent, and zeta_27 is itself a class-1
   walker, v(zeta_27 - 1) = 1).
S3 (the anchor): K27 = Phi_27(x+1) is Eisenstein; its word
   satisfies the pass conditions (gate 1, w_j = 0 for 0 < j < 9,
   w_12 = 1, w_15 = -w_9, w_18 = w_9^2) AND its deep between digits
   through 29 are ALL zero; its class-1 climb passes CAP with
   Hensel margin v(Phi_27(u)) > 2 v(Phi_27'(u)) (= 2 x 45).
S4 (the diagonal read): b_1 += 3 moves w_19 with prefix <= 18
   frozen; across b_1 in {0, 3, 6} the digit w_19 takes 3 distinct
   values (k = 1 diagonal linear-injective), so sticks differ
   across the triple; b_2 += 3 freezes the prefix <= 19; d += 9 is
   INVISIBLE (identical word through 29, identical stick). Every
   variant's stick = 27 + its own first nonzero between digit.
   [Contrast DS-D(ii) at m = 1: deep perturbations moved nothing —
   the m = 1 game never reads past the word.]
S5 (the ladder): greedily zeroing the eight between digits via the
   eight owning b_i second digits succeeds one grid digit per rel
   (prefix frozen each step); the mid-rung field (19, 20 zeroed)
   sticks at 27 + its next nonzero between digit; the terminal
   field sticks past 27 + 29 = 56. Whether it is still non-torsion
   (stick < CAP, expected) or climbs to CAP (then Hensel
   adjudicates: it became zeta_27's chart) is open — both coded.

THE DESIGN. Machinery imported from the gear chain (LF, sampling,
word_of, solve_word, land). THE LEAN CLIMB is the new primitive:
pool = pure steps grouped by their own landing v(s^P - 1) + seat
hybrids + census mates; at state v only pool entries landing
exactly v can raise (ultrametric), so each level costs O(pool_v);
equivalence with explore_deep_spectrum.climb cross-checked on D.
The ladder runs two phases: digit-greedy on the pure rels,
STICK-greedy on the shallow rels (the hole is target-shifted).
Labels never read orbits; the engine only ever reads measured
digits. Run: python prime/code/explore_above_window.py

FINDINGS (entered post-run, copied from printed output).

1. THE ABOVE-WINDOW ROUTE MAP (rule in range; the enumeration is
   exact to rel 29 by the 5-part clearance): above e the between
   rels SPLIT. PURE {19, 20, 22, 23, 25, 26}: monomial-free, forced
   digit -w_r — the k = 1 diagonal verbatim (level i + e owned by
   b_i mod 9). SHALLOW-SHIFTED {28, 29}: DR1's v_p = 3 shallow
   family lands ON them (tau_0 at rel 3e + c - p i* = 28; ((1,1))
   and ((2,0)) at 29) — still forced (rho_0 is pinned), but the
   hole condition is TARGET-SHIFTED: w_r = -shallow, not 0. At
   m = 1 the same route enters above e where every rel is fresh —
   invisible; at m >= 2 it decorates forced rels. Monomial census
   in (18, 29]: {21: 5, 24: 7, 27: 13, 28: 1, 29: 2}.

2. THE GUARD CONFIRMED — A WORD-LEVEL ALL-HOLES FIELD WITHOUT
   TORSION (the designed counterexample; the non-torsion
   certificate is the forced ceiling): D = x^18 + 6x^12 - 24
   (triangle-designed word [1,0^11,1,0^6]; the sparse grid leaves
   the whole k = 1 diagonal zero) passes the ENTIRE window AND
   every pure between rel — census landings {36, 48, 51, 54, 55}
   (window 37..45 and all pure betweens holes) — and sticks at
   55 = 27 + 28, the SHALLOW rel (full-scan climb agrees): its
   forced digit at w_28 = 0 is nonzero. Stick < CAP proves no
   zeta_27 (forced digits are walker-independent, and zeta_27 is
   itself a class-1 walker). At m >= 2 "gate-open + all in-window
   forced slots holes" does NOT imply torsion: the torsion
   detector's criterion (deep_spectrum finding 2) is m = 1 exactly,
   and the m >= 2 scope guard now carries a designed witness.

3. THE ANCHOR'S SIGNATURE: K27 = Phi_27(x+1) prints word
   [1,0^8,2,0,0,1,0,0,1,0,0,1] — the variety conditions on cue
   (w_12 = 1 = w_0^2, w_15 = 1 = -w_9, w_18 = 1 = w_9^2, all
   in-window betweens zero, w_9 = 2 free), every pure deep digit
   zero, and w_28 = w_29 = 2 = the MEASURED shallow terms (a
   sailing field's forced digits vanish, so its chart digits at the
   shallow rels are PINNED — the values any sailing chart must
   carry; the ladder's knob reproduces w_28 = 2 independently, [L]).
   Census landings ride the
   3-lattice {36, 48, 51, 54, 57, 60}; the class-1 climb passes CAP
   with Hensel margin v(Phi_27(u)) = 100 > 90 = 2 v(Phi_27') —
   zeta_27 constructed. (Machinery: the pure-step trajectory map
   leaves 63 = 27 + 2e uncovered at m = 2 — AW3 — hence the
   enriched pool; at m = 1 the deep classes k + 2e cover every
   above-window level, which is why the old climb was complete.)

4. THE DIAGONAL READ (rule in range): the stick reads the k = 1
   diagonal. b_1 in {0, 3, 6} walks w_19 through {0, 1, 2}
   (linear-injective, prefix <= 18 frozen), sticks {55, 46, 46};
   b_2 + 3 moves w_20 with the prefix <= 19 frozen (stick 47);
   d + 3 moves the CARRY digit w_18 alone (the triangle's carry
   law) and ceils IN-window at 45 — the broken deferral; d + 9
   (digit 2 of d, entering at 2e = 36) is INVISIBLE through 29:
   identical word, identical stick 55. Contrast DS-D(ii) at m = 1
   (deep perturbations moved nothing — that game never reads past
   the word): at m >= 2 the game reads the grid diagonal by
   diagonal (digit k of b_i at level i + ke, DR5).

5. THE LADDER AND THE CORRECTED DETECTOR (rule in range at
   (3,1,2)): one grid digit per between rel. The pure phase is
   digit-greedy (D's are already zero); the shallow rel 28 opens at
   knob b_10's second digit = 2 — i.e. w_28 = 2, EXACTLY K27's
   measured value — and the stick climbs 55 -> 59 = 27 + 32, past
   rel 29 (its forced digit vanished with the knob) into territory
   beyond the enumerated map (level 32 sits on the k = 1 diagonal;
   which rels past 29 are pure was uncharted here — CLOSED by a
   later run: none is, every between rel >= rel_0 = 28 is shifted; the
   decoration law, explore_shallow_route.py finding 2). Every opened rel buys its rung; the
   terminal field is still non-torsion. THE m >= 2 READING: sail
   <=> torsion survives (torsion => sail at every m; a full sail
   Cauchy-converges to a primitive p^{m+1}-th root), but it is NOT
   word-readable — each deeper band of forced rels reads the next
   grid diagonal, and only the anchor's charts pass every diagonal:
   the no-mimic law (DR6) one level up.

PRE-GREEN FAILURES (two, adjudicated as they arose — the extra checking
paid its way; recorded in the hand notes, stages 6+, and git):
(1) Run 1 ([R]): AW2's purity lemma predicted the WHOLE between set
    monomial-free; rel 28 carries tau_0 (v_p = 3, Lambda = 3e + c).
    DR1's own shallow family, forgotten above the window. The
    between set splits pure/shallow; between_pred reads the pure
    rels only, and the ladder's shallow phase turned stick-greedy.
    Corollary correction to S3, same discovery: K27's "deep between
    digits ALL zero" holds for the PURE rels only — its shallow
    digits are pinned NONZERO (w_28 = w_29 = 2, finding 3).
(2) Run 2 ([D]): S1 froze "landings ONLY at 36 and 27 + r*" — the
    fresh 3-lattice landings (48, 51, 54: killing s_1 exposes
    deeper fresh rels) are landings too, and D's sparse grid zeroes
    the whole pure diagonal, so the ceiling is the shallow rel, not
    a pure one. Corrected census law: landings = {36} u {lattice <
    stick} u {stick}. (S5's mid-rung probe is vacuous for the
    sparse D — the pure phase is a no-op there.)

RUN RECORD (python prime/code/explore_above_window.py, ~8 s, exit
0): 79 checks this module + 1110 through the imported machinery.
Printed rows as copied: [R] monomial rels (18, 29]: {21: 5, 24: 7,
27: 13, 28: 1, 29: 2}; [D] x^18+6x^12-24, digits 19..29 =
[0,0,0,0,0,1,0,0,0,0,0], landings [36, 48, 51, 54, 55], stick 55
(full-scan agrees); [K] word [1,0,0,0,0,0,0,0,0,2,0,0,1,0,0,1,0,0,
1], w_28 = w_29 = 2, landings [36, 48, 51, 54, 57, 60],
v(Phi_27(u)) = 100 > 90 = 2 v(Phi'); [P] b1+3 / b1+6 stick 46,
b2+3 stick 47, d+3 stick 45 (w_18 = 2), d+9 stick 55, w_19 walk
[0, 1, 2]; [L] b_10's second digit = 2 opens rel 28 (w_28 = 2),
stick 55 -> 59.
"""

import random

import explore_local_clock as lc
import explore_arrival_defect as ad
import explore_tame_readout as tr
import explore_deep_spectrum as ds
import explore_slot_algebra as sa

CHECKS = 0

P3, E18, PP = 3, 18, 27           # p, e, p^{m+1} at (3, 1, 2)
PURE = [19, 20, 22, 23, 25, 26]   # between rels with no monomials
SHALLOW = [28, 29]                # between rels + the tau_0 v_p=3 route
TARGET = (1,) + (0,) * 11 + (1,) + (0,) * 6   # the designed pass word


def ok(cond, msg):
    global CHECKS
    if not cond:
        raise AssertionError(msg)
    CHECKS += 1


def eadd(F, A, B):
    return tuple(F.cadd(a, b) for a, b in zip(A, B))


def escale(F, A, n):
    return tuple(F.cint(a, n) for a in A)


def deep_word(name, eis, depth=29):
    return ds.word_of(name, P3, eis, depth)


def between_pred(word):
    """27 + first PURE between-rel whose deep chart digit is nonzero
    (the shallow-shifted rels 28, 29 are not word-pure: run 1)."""
    for r in PURE:
        if word[r]:
            return PP + r
    return None


# ---------------------------------------------------------------- [R]


def section_r():
    print("\n[R] the route map above the window at (3,1,2), rel <= 29")
    # the 5-part clearance (AW2): 4-index enumeration is complete
    ok(2 * E18 + 27 + 10 - PP > 29, "sigma=5 clearance fails")
    ok(3 * E18 + 5 + 10 - PP > 29, "sigma>=7 clearance fails")
    w = tr.enumerate_window(P3, 1, 2, 29)
    for r in PURE:
        ok(r not in w, "pure between rel %d carries monomials: %s"
           % (r, w.get(r)))
    for r in (21, 24, 27):
        ok(r in w, "lattice rel %d carries no monomial" % r)
    # the shallow v_p = 3 route (run-1 adjudication): tau_0-family
    # monomials land ON the between rels 28, 29 — forced still (no
    # fresh digit: rho_0 is pinned), but the hole condition shifts
    ok(sorted(w.get(28, [])) == [((1, 0),)],
       "rel 28 monomials %s != the tau_0 shallow route" % w.get(28))
    ok(sorted(w.get(29, [])) == [((1, 1),), ((2, 0),)],
       "rel 29 monomials %s != the shallow pair" % w.get(29))
    above = {r: len(w[r]) for r in sorted(w) if r > E18}
    print("  monomial rels in (18, 29]: %s" % above)
    print("  pure between set %s monomial-free; 28, 29 carry the"
          " shallow\n    v_p = 3 route (word-read, target-shifted)"
          % PURE)


# ------------------------------------------------------- the lean climb


def step_pool(F, c, P, mates=()):
    """(s, s^P, vstep) triples: pure class-preserving steps, seat
    hybrids (AW3), census mates. Grouped by vstep."""
    one = ad.const_el(F, 1)
    pool = {}

    def put(s):
        sP = ds.epow(F, s, P)
        v = F.val(ad.esub(F, sP, one))
        pool.setdefault(v, []).append((s, sP))

    for k in range(c + 1, F.amax):
        i, j = divmod(k, F.e)
        for a in range(1, F.p):
            s = [list(cc) for cc in F.one]
            s[j][0] = (s[j][0] + tr.teich(F, a) * (F.p ** i)) % F.pM
            put(tuple(tuple(cc) for cc in s))
    seat = F.e // (F.p - 1)
    for j2 in range(seat + 1, min(seat + 15, F.amax)):
        i1, j1 = divmod(seat, F.e)
        i2b, j2b = divmod(j2, F.e)
        for a in range(1, F.p):
            for b in range(1, F.p):
                s = [list(cc) for cc in F.one]
                s[j1][0] = (s[j1][0] + tr.teich(F, a) * (F.p ** i1)) % F.pM
                s[j2b][0] = (s[j2b][0] + tr.teich(F, b) * (F.p ** i2b)) \
                    % F.pM
                put(tuple(tuple(cc) for cc in s))
    for s in mates:
        put(s)
    return pool


def lean_climb(F, u, c, P, cap, pool):
    """Greedy digit ascent; only a pool entry landing exactly the
    current v can raise it (ultrametric). Class-preserving: a raise
    is accepted only if the multiplied walker stays class c.
    Returns (u, stick)."""
    one = ad.const_el(F, 1)
    uP = ds.epow(F, u, P)
    v = F.val(ad.esub(F, uP, one))
    while v < cap:
        for s, sP in pool.get(v, ()):
            u2 = F.emul(u, s)
            if F.val(ad.esub(F, u2, one)) != c:
                continue
            uP2 = F.emul(uP, sP)
            w2 = F.val(ad.esub(F, uP2, one))
            if w2 > v:
                u, uP, v = u2, uP2, w2
                break
        else:
            break
    return u, v


def census(F, rng, n=250):
    """Class-1 landing multiset + the walkers (mates for the pool)."""
    lands, mates = {}, []
    for u in ad.sample_class(F, 1, n, rng):
        v = ds.land(F, u, PP)
        lands[v] = lands.get(v, 0) + 1
        mates.append(u)
    return lands, mates


def climb_from_floor(F, rng, pool_mates, cap=None):
    if cap is None:
        cap = F.CAP
    u, P = ds.floor_walker(F, 1, rng)
    ok(P == PP, "%s: class-1 exponent %d != 27" % (F.name, P))
    pool = step_pool(F, 1, PP, mates=pool_mates)
    return lean_climb(F, u, 1, PP, cap, pool)


# ---------------------------------------------------------------- [D]


def section_d(rng):
    print("\n[D] the designed pass field D: the whole window is holes")
    eisD = sa.solve_word(P3, E18, TARGET, "SAIL")
    wD = deep_word("SAIL", eisD)
    ok(wD[:19] == list(TARGET), "SAIL word %s != target" % wD[:19])
    pred = between_pred(wD)
    print("  %s: deep digits 19..29 = %s, predicted stick %s"
          % (sa.poly_name(eisD), wD[19:30], pred))
    FD = lc.LF("SAIL", P3, [0, 1], eisD, 108)
    lands, mates = census(FD, rng)
    uD, stickD = climb_from_floor(FD, rng, mates)
    ok(stickD == pred if pred is not None else stickD > PP + 26,
       "SAIL stick %d != predicted %s" % (stickD, pred))
    ok(stickD < FD.CAP and (stickD - PP) > E18
       and (stickD - PP) % 3 != 0,
       "SAIL stick %d not an above-window between rel" % stickD)
    ok(all(v == 36 or v == stickD
           or (v % 3 == 0 and 48 <= v < stickD) for v in lands),
       "SAIL landings %s off {36, lattice, %d}"
       % (sorted(lands), stickD))
    ok(36 in lands and stickD in lands,
       "SAIL landings %s miss the floor or the ceiling"
       % sorted(lands))
    # cross-check: the full-scan climb agrees
    uf, Pf = ds.floor_walker(FD, 1, rng)
    achF, stickF = ds.climb(FD, uf, 1, Pf, 60)
    ok(stickF == stickD, "full-scan stick %d != lean %d"
       % (stickF, stickD))
    print("  census (%d walkers): landings %s — window 37..45 AND"
          " every pure\n    between rel are holes; stick %d = 27 +"
          " %d (full-scan climb agrees):\n    NO zeta_27 in D — a"
          " word-level all-holes field without torsion" %
          (sum(lands.values()), sorted(lands), stickD, stickD - PP))
    return eisD, wD, stickD


# ---------------------------------------------------------------- [K]


def phi27_shift():
    """Phi_27(x+1) = (x+1)^18 + (x+1)^9 + 1, coeffs low -> high."""
    from math import comb
    eis = [0] * 19
    for j in range(19):
        eis[j] += comb(18, j)
    for j in range(10):
        eis[j] += comb(9, j)
    eis[0] += 1
    ok(eis[18] == 1 and eis[0] == 3, "Phi27 shift malformed")
    for j in range(18):
        ok(eis[j] % 3 == 0, "Phi27(x+1) not Eisenstein at %d" % j)
    ok(eis[0] % 9 != 0, "Phi27(x+1) constant term not sharp")
    return eis


def section_k(rng):
    print("\n[K] the anchor K27 = Q_3(zeta_27): the sail with margin")
    eis27 = phi27_shift()
    w27 = deep_word("K27", eis27)
    ok(w27[0] == 1 and all(w27[j] == 0 for j in range(1, 9)),
       "K27 gate/regime: %s" % w27[:9])
    ok(w27[12] == 1 and w27[15] == (-w27[9]) % 3
       and w27[18] == (w27[9] * w27[9]) % 3,
       "K27 slot conditions: w9,w12,w15,w18 = %s"
       % [w27[9], w27[12], w27[15], w27[18]])
    ok(all(w27[j] == 0 for j in (10, 11, 13, 14, 16, 17)),
       "K27 in-window between digits: %s" % w27[:19])
    ok(all(w27[r] == 0 for r in PURE),
       "K27 pure deep digits nonzero: %s" % w27[19:30])
    print("  word passes the whole window AND every pure deep digit"
          " vanishes\n    (w_9 = %d free); w_28, w_29 = %d, %d — the"
          " MEASURED shallow terms\n    (K27's forced digits vanish,"
          " so w_r = -shallow there): %s"
          % (w27[9], w27[28], w27[29], w27[:19]))
    F27 = lc.LF("K27", P3, [0, 1], eis27, 108)
    lands, mates = census(F27, rng)
    ok(all(v == 36 or v >= F27.CAP or (v >= 48 and v % 3 == 0)
           for v in lands),
       "K27 landing off the sailing lattice: %s" % sorted(lands))
    u, stick = climb_from_floor(F27, rng, mates)
    ok(stick >= F27.CAP, "K27 climb stuck at %d" % stick)
    one = ad.const_el(F27, 1)
    u9 = ds.epow(F27, u, 9)
    v9 = F27.val(ad.esub(F27, u9, one))
    ok(v9 == 9, "K27: v(u^9 - 1) = %d != 9" % v9)
    phi = eadd(F27, eadd(F27, ds.epow(F27, u, 18), u9), one)
    vphi = F27.val(phi)
    dphi = eadd(F27, escale(F27, ds.epow(F27, u, 17), 18),
                escale(F27, ds.epow(F27, u, 8), 9))
    vdphi = F27.val(dphi)
    ok(vdphi == 45, "K27: v(Phi') = %d != 45" % vdphi)
    ok(vphi > 2 * vdphi, "K27 Hensel margin: v(Phi)=%d <= %d"
       % (vphi, 2 * vdphi))
    print("  census landings %s (the 3-lattice); climb -> CAP,"
          " Hensel margin\n    v(Phi_27(u)) = %s > 90 = 2 v(Phi'):"
          " zeta_27 constructed" %
          (sorted(lands),
           ">=%d" % F27.amax if vphi >= F27.CAP else vphi))


# ---------------------------------------------------------------- [P]


def section_p(rng, eisD, wD, stickD):
    print("\n[P] the diagonal probe: the stick reads the k = 1"
          " diagonal")
    variants = [("b1+3", 1, 9), ("b1+6", 1, 18), ("b2+3", 2, 9),
                ("d+3", 0, -9), ("d+9", 0, -27)]
    w19s, sticks = [wD[19]], {stickD}
    for name, idx, add in variants:
        eisV = list(eisD)
        eisV[idx] += add
        wV = deep_word(name, eisV)
        FV = lc.LF(name, P3, [0, 1], eisV, 66)
        lands, mates = census(FV, rng, n=80)
        uV, stick = climb_from_floor(FV, rng, mates)
        if name == "d+3":
            # d's SECOND digit enters at level e (the carry law,
            # slot_algebra finding 3): the deferral digit w_18 moves
            # off w_9^2 = 0 and the field ceils IN-window at rel 18
            ok(wV[:18] == list(TARGET[:18]) and wV[18] != 0,
               "d+3: carry digit did not move w_18 alone: %s" % wV)
            ok(stick == PP + E18, "d+3: stick %d != 45 (the broken"
               " deferral)" % stick)
        else:
            ok(wV[:19] == list(TARGET),
               "%s: word through e moved: %s" % (name, wV[:19]))
            pred = between_pred(wV)
            if pred is not None:
                ok(stick == pred, "%s: stick %d != predicted %d"
                   % (name, stick, pred))
            else:
                ok(stick > PP + 26, "%s: stick %d with all pure"
                   " digits zero" % (name, stick))
        sticks.add(stick)
        if name.startswith("b1"):
            w19s.append(wV[19])
        if name == "b2+3":
            ok(wV[:20] == wD[:20], "b2+3 moved the prefix <= 19")
        if name == "d+9":
            ok(wV[:30] == wD[:30],
               "d+9 visible through 29: %s vs %s" % (wV, wD))
            ok(stick == stickD, "d+9 moved the stick: %d != %d"
               % (stick, stickD))
        print("  %-5s digits 18..29 = %s  stick %d" %
              (name, wV[18:30], stick))
    ok(len(set(w19s)) == 3,
       "w_19 over b_1 in {0,3,6} not 3 distinct values: %s" % w19s)
    ok(len(sticks) >= 2, "sticks never moved: %s" % sorted(sticks))
    print("  w_19 over b_1 in {0,3,6}: %s (3 values, exactly one"
          " hole);\n    sticks %s — the k = 1 diagonal is READ;"
          " d+9 invisible on cue" % (w19s, sorted(sticks)))


# ---------------------------------------------------------------- [L]


def section_l(rng, eisD, stickD):
    print("\n[L] the ladder: one second-diagonal grid digit per"
          " between rel")
    # phase 1 (the pure rels): digit-greedy — zero the chart digit
    eisL = list(eisD)
    for r in PURE:
        wL = deep_word("L", eisL)
        if wL[r] != 0:
            for t in (1, 2):
                trial = list(eisL)
                trial[r - E18] += 9 * t
                wT = deep_word("Lt", trial)
                if wT[:r] == wL[:r] and wT[r] == 0:
                    eisL = trial
                    break
            else:
                ok(False, "ladder: rel %d not zeroable by b_%d's"
                   " second digit" % (r, r - E18))
    wL = deep_word("L6", eisL)
    ok(wL[:19] == list(TARGET), "ladder word through e moved")
    ok(all(wL[r] == 0 for r in PURE),
       "ladder pure digits not all zero: %s" % wL[19:30])
    # phase 2 (the shallow-shifted rels 28, 29): STICK-greedy — the
    # hole condition is w_r = -shallow, not w_r = 0 (run 1), so the
    # knob is tuned on the engine's own stick
    for r in SHALLOW:
        FL = lc.LF("L%d" % r, P3, [0, 1], eisL, 66)
        landsL, matesL = census(FL, rng, n=80)
        uL, stick = climb_from_floor(FL, rng, matesL)
        if stick > PP + r:
            continue
        ok(stick == PP + r,
           "ladder: stick %d below the shallow rel %d" % (stick, r))
        for t in (1, 2):
            trial = list(eisL)
            trial[r - E18] += 9 * t
            wT = deep_word("Lt", trial)
            if wT[:r] != deep_word("L", eisL)[:r]:
                continue
            FT = lc.LF("Lt%d" % r, P3, [0, 1], trial, 66)
            landsT, matesT = census(FT, rng, n=80)
            uT, stickT = climb_from_floor(FT, rng, matesT)
            if stickT > PP + r:
                eisL = trial
                print("  shallow rel %d: knob b_%d's second digit ="
                      " %d opens the hole\n    (w_%d = %d != 0: the"
                      " measured -shallow term); stick %d -> %d"
                      % (r, r - E18, t, r, wT[r], stick, stickT))
                break
        else:
            ok(False, "ladder: shallow rel %d not openable" % r)
    wL = deep_word("LADDER", eisL)
    FL = lc.LF("LADDER", P3, [0, 1], eisL, 108)
    landsL, matesL = census(FL, rng)
    uL, stickL = climb_from_floor(FL, rng, matesL)
    ok(stickL > PP + 29, "ladder stick %d <= 56" % stickL)
    if stickL >= FL.CAP:
        # the adjudication: it became zeta_27's chart — Hensel must hold
        one = ad.const_el(FL, 1)
        u9 = ds.epow(FL, uL, 9)
        phi = eadd(FL, eadd(FL, ds.epow(FL, uL, 18), u9), one)
        ok(FL.val(phi) > 90, "ladder passed CAP without Hensel margin")
        print("  LADDER (%s): climb -> CAP with Hensel margin — the"
              " zeroed field\n    IS Q_3(zeta_27)" % sa.poly_name(eisL))
    else:
        print("  LADDER (all eight between rels opened): stick %d ="
              " 27 + %d — still\n    non-torsion; every opened rel"
              " bought exactly its rung" % (stickL, stickL - PP))
    return stickL


# -------------------------------------------------------------- main


def main():
    rng = random.Random(211)
    print("THE m >= 2 ABOVE-WINDOW SAIL — (p, c, m) = (3, 1, 2),"
          " e = 18, P = 27")
    section_r()
    eisD, wD, stickD = section_d(rng)
    section_k(rng)
    section_p(rng, eisD, wD, stickD)
    stickL = section_l(rng, eisD, stickD)
    print("\nVERDICT: at m >= 2 the word decides the WINDOW, not the"
          " sail —\n  the sail reads the grid diagonal-by-diagonal"
          " above e (stick ladder\n  %d -> %d); sail <=> torsion"
          " survives, but it is not word-readable." % (stickD, stickL))
    imported = (lc.CHECKS + ad.CHECKS + tr.CHECKS + ds.CHECKS
                + sa.CHECKS)
    print("\n%d checks this module + %d through the imported"
          " machinery" % (CHECKS, imported))


if __name__ == "__main__":
    main()
