"""explore_coarsest_colouring.py -- is (degree, class) the COARSEST faithful
colouring?

THE QUESTION. The abstract walker reads a ring as a supply matrix n(d, c)
over the class group -- items coloured by (degree, class) -- and its element
menu is the ring engine's at every state of the ring's own branch tree
(explore_class_schedule.py F1), with the orbit count the multinomial of that
colouring (F5). What was never shown is COARSEST: whether some PROPER
coarsening of (degree, class) prices the same menus. This rig re-runs the
faithfulness control under every proper coarsening at once.

THE LATTICE, and what a pair witness does and does not transfer. A
colouring phi coarser than (degree, class) merges at least two colours
A != B, so two exponent-assignments sharing their {A,B}-merge projection
share their phi-projection too -- the STATE side of a pair witness rides
up the lattice for free. The EVIDENCE side does not always follow: a K1
witness (one assignment principal, the other not) transfers to every
coarser phi outright, principality reading no projection at all, and so
does a menu difference in COST or TIE WIDTH, both projection-invariant --
but a menu difference living only in vehicle COMPOSITION can collapse
under a coarser projection. [The first draft of this slate claimed the
unconditional transfer and the audit refuted it on paper; left standing
because the design is the record of what was frozen.] So the pair sweep
finds the witnesses, and S3 then walks the WHOLE lattice -- every
partition of the active colours, Bell(4..10) per ring -- declaring a
coarsening broken only on a transferring witness or on a stored witness
RE-PROJECTED through that very partition, with the unresolved count
printed rather than argued away. "Active" = the colour of some item
seated at a tree state or appearing in a tree state's menu; a coarsening
that merges only colours the walked region never touches cannot be
refuted by that region, and the verdict is scoped to the active supply.

THE WITNESS SHAPE, one swap. For items x of colour A and y of colour B
with st(x) != st(y), the swapped assignment st' (x and y exchange
exponents, everything else fixed) has the SAME M_AB-projection as st. Two
observables, and they are different faithfulness claims:
  K1  THE STATE SPACE PARTS: st is principal and st' is not, so the
      coarsened data cannot tell a state from a non-state. Principality is
      class-sum zero, and the swap moves it by (e_x - e_y)*(c_B - c_A) --
      zero iff that product vanishes in the group.
  K2  A MENU PARTS: st' is principal too, and the engines' menus at st and
      st', projected through the merge (vehicles as multisets of
      (phi-colour, exponent), plus the cost), differ. This is the
      kill-shape's own observable -- "breaks a menu" -- and the sharper of
      the two, since a walker is a menu machine before it is a state
      recogniser.
Within-colour choice of x and y is immaterial: F1's uniqueness gate holds
at all six rings, so items of one colour are interchangeable already.

THE HAND-ATTACK, on paper before any engine code.

  (a) CROSS-DEGREE MERGES should die trivially: the price reads the degree
  (cost = d*n + m(-n*c)), covering reads divisibility of degrees, and the
  tick reads the seated degrees through lambda -- three separate mechanisms
  any of which shows in a menu. The only subtlety is that a PRINCIPAL swap
  needs (e_x - e_y)*(c_B - c_A) = 0, so at h > 1 a cross-degree
  cross-class pair may offer no principal swap in a small region and die
  by K1 alone.

  (b) SAME-DEGREE CROSS-CLASS MERGES are the real question, and ONE FAMILY
  HAS A DEFENCE. If sigma is a group automorphism with n(d, sigma(c)) =
  n(d, c) for every colour -- inversion c -> -c is the standing candidate,
  conjugate places carrying inverse classes -- then relabelling every item
  along sigma is a symmetry of the whole dynamics: it preserves degrees,
  the group law, and the minrep map up to relabelling, and it fixes
  principality (sigma(0) = 0). A FULL sigma-conjugation therefore maps
  states to states and menus to menus, and both project equally through
  the merge {(d, c), (d, -c)} -- so no witness of that shape exists. What
  the merge still has to survive is the PARTIAL swap: exchange one pair
  and leave the rest of the state fixed. Where the rest of the state
  carries class-sensitive context, a partial swap is not a
  sigma-conjugation -- but for it to be a K2 witness at all it must first
  be principal, which needs (e_x - e_y)*2c = 0, and the region may never
  supply that. So the inverse-class merge plausibly survives K2 while K1
  fires freely against it ((e_x - e_y)*2c != 0 is easy). If that is what
  prints, "coarsest" SPLITS BY OBSERVABLE: (degree, class) coarsest for
  the state space, (degree, class-up-to-inversion) not refuted for menus
  in the region -- and the count is the tiebreak, (c) below.

  (c) THE COUNT HALF CAN BREAK WHERE THE MENUS DO NOT. The orbit count of
  a colouring is the per-cell multinomial (F5), and merging two colours of
  sizes n1, n2 replaces S(n1) x S(n2) by S(n1 + n2) in the putative orbit.
  A global sigma adds ONE relabelling, not the full mixing: the group
  generated is S(n1) x S(n2) extended by sigma, of index
  (n1 + n2)! / (2 * n1! * n2!) in the merged symmetric group when
  n1 = n2. At cells of width 1 + 1 the extension IS the full S(2), so the
  merged formula can hold there and the discriminating cell needs width
  2 + 2 or better -- whether the region reaches one is an observable, not
  a prediction.

  (d) THE PRICE'S OWN FIBRES are computable outright: colour two colours
  alike iff their whole cost columns n -> d*n + m(-n*c) agree. Asymptotics
  pin the degree (cost/n -> d), so a fibre is same-degree; within a
  degree, equal columns need m(-n*c) = m(-n*c') for every n, which the
  inversion symmetry supplies when m(c) = m(-c). The prediction is that
  the fibres are exactly the inversion orbits, so "the price's own fibres"
  and "class up to inversion" are one coarsening at these six rings.

TRANSPLANT FLAGS, fixed at the freeze.
 T1 From the walked trajectories to swapped states. A swapped st' is
    principal but not necessarily greedy-REACHABLE; the engines price any
    element state, and the control below (P1b) runs the identity-colouring
    walker against the engine AT THE SWAPPED STATES too, so faithfulness
    off the tree is measured rather than assumed.
 T2 From the function fields to the number rings. NOTHING is carried. The
    number-ring port adds a ladder column the matrix cannot supply
    (explore_element_schedule_nf.py F2), so its coarsening question has an
    extra axis this rig does not touch; scope here is the six function
    fields the colouring claim was minted on.
 T3 From F5's orbit counts to the merged formula. The merged multinomial
    below is a NEW formula (cells pooled across colours); F5's refined and
    degree-blind formulas are re-run beside it as controls, not trusted.

PREDICTIONS, frozen before the engine runs.
 P1a (positive control) The identity colouring reproduces every engine
     menu at every branch-tree state of all six rings, 0 off -- F1's
     control through imported machinery.
 P1b (positive control, off the tree) The identity walker also reproduces
     the engine menu at every PRINCIPAL swapped state visited. A failure
     here is a scope finding about F1, and it is recorded rather than
     asserted.
 P1c (positive control, count) The identity multinomial is 0 shapes off at
     every truncated supply, and the degree-blind one is off somewhere at
     every ring with h > 1 (F5's two measured directions).
 P2  Every active pair carries a witness of some kind, EXCEPT possibly
     inverse-class pairs {(d, c), (d, -c)}: unbroken pairs, if any, sit
     inside the inversion family.
 P3  Every active cross-degree pair carries a witness; at the h = 1 ring
     every swap is principal, so its cross-degree pairs all carry K2.
 P4  Inverse-class pairs at h > 1: K1 fires against every active one; K2
     fires against NONE in the region (the sigma defence, hand-attack b).
     If K2 fires on an inverse pair, the defence is refuted and (degree,
     class) is coarsest outright -- the stronger, simpler verdict.
 P5  The price-fibre partition, computed from the cost columns, equals the
     inversion partition {(d, c)} ~ {(d, -c)} at every ring: no accidental
     fibre beyond the automorphism.
 P6  The count under the inversion merge: UNKNOWN, the observable is the
     per-shape comparison. The mechanism that would break it needs a
     merged cell of width >= 2 + 2 (hand-attack c); whether the truncated
     region reaches one decides, and either way the number prints.

KILL-SHAPES, named as observables.
  - The question CLOSES iff the unbroken-pair set is EMPTY at every ring:
    then every proper coarsening of the active colouring breaks a menu or
    the state space in the walked region, and (degree, class) is coarsest
    there. [As frozen this treated the pair condition as sufficient; the
    audit's transfer correction makes the closing criterion S3's lattice
    walk at 0 unresolved, the pair condition being necessary. Left
    standing because the design is the record of what was frozen.]
  - A surviving pair PRINTS: ring, pair, swaps attempted, principal swaps
    found, menus compared -- so a survival by starvation (no principal
    swap ever offered) is distinguishable from a survival by agreement.

FINDINGS (tiers below; run record at the bottom).

F1 (DEGREE, CLASS) IS COARSEST FOR THE FAITHFULNESS CONTROL -- the closing
   verdict, made by the LATTICE WALK and not by the pair sweep alone (rule
   in range; six rings, ALL 141,526 proper coarsenings of the active
   colours -- 14, 51, 202, 4139, 115974, 21146 per ring -- each broken by
   a TRANSFERRING witness: 141,414 by the state space, 112 by a cost or
   tie-width menu difference, 0 needing a re-projected witness and 0
   unresolved). Underneath it the pair sweep: all 140 pair-merges of
   active colours -- 6, 10, 15, 28, 45, 36 -- part, 126 parting a MENU
   (K2) and the 14 others the STATE SPACE (K1: two exponent-assignments
   with one merge-projection, one principal and one not) while every
   principal swap's menus agree. The region: the ring's own branch tree
   five levels deep, plus 1548 constructed states (0, 20, 158, 216, 804,
   350 per ring) built so that no pair survives by starvation -- every
   pair was OFFERED a principal swap.

F2 THE MENU HALF ALONE DOES NOT SEE 14 MERGES, AND EVERY ONE IS
   AUT-CONJUGATE -- P2/P4 lost as frozen and won one level up. The frozen
   defence was inversion; the measured one is conjugacy under the
   supply-preserving automorphism group (h5's degree-1 and degree-5
   layers pair up under x -> u*x, u in (Z/5)^*, not only u = -1; |Aut|
   1, 1, 2, 2, 4, 8 with 1, 1, 2, 2, 4, 4 preserving the supply). The
   containment is STRICT and one-way: aut-conjugacy is necessary for menu
   survival, not sufficient -- 11 aut-conjugate pairs DO part a menu (h4
   (2,2)~(2,3) and (4,2)~(4,3); h5 (1,2)~(1,3), (1,2)~(1,4), (1,3)~(1,4);
   g2 all six degree-1 pairs). Each of the 14 survivors held through 28-64
   principal swaps including context states built to defeat the global
   relabelling (a third colour the automorphism moves, seated beside the
   swap at its class's own order). WHICH aut-conjugate pairs the menus
   part is measured and UNEXPLAINED -- at h5 the degree-1 pairs through
   class 1 survive while the pairs among classes {2, 3, 4} part; at g2
   every degree-1 pair parts while the degree-2 and degree-4 inverse pairs
   survive -- an open reading whose witnesses sit in the k2 records.

F3 THE THREE OBSERVABLES GENUINELY PART, so "faithful" is three claims.
   The aut-orbit merge survives the menus (F2), breaks the state space
   (K1 at every survivor), and breaks the COUNT: pooling the S4
   configurations, the merged multinomial is off at 0, 0, 2, 2, 5, 11
   shapes (aut-orbit) and 0, 0, 2, 2, 10, 8 (inversion) against the
   identity's 0 everywhere -- the merged formula counts item mixings that
   are not principal, which is K1 arriving as arithmetic. The controls
   frame it: degree-blind off 0, 9, 6, 5, 5, 11 (its F_2[x] zero is h = 1,
   where the two formulas are one formula, F5's row re-read).

F4 THE NAMED COARSENINGS ALL BREAK, price fibres included, and the
   transfer-valid evaluator moved two of the first draft's verdicts.
   Degree-only (lockstep) breaks a MENU at h4 (by a re-projected witness,
   the one place the sweep needed one) and at g2 (cost/width), the state
   space only at h3 and h5; class-only breaks a menu at every ring it
   merges on; one-colour breaks a menu everywhere. The PRICE'S OWN FIBRES
   equal the inversion partition at four rings, are COARSER at h5 and g2
   (the cost columns of all four degree-1 classes collide), and are
   EXACTLY the preserved-Aut orbits at all six -- P5 lost as frozen and
   won one level up, the same shape as P4: the price's degeneracy is the
   automorphism group's, no more and no less. They break a MENU at g2 and
   only the state space at h3, h4, h5 -- so a colour's whole cost column
   does not determine its dynamics, and the price cannot name its own
   colouring, but the menus alone convict it at just one ring. Class-up-to-preserved-Aut breaks a menu at g2 (its orbit
   there pools the four broken degree-1 pairs) and the state space
   elsewhere it merges.

F5 FAITHFULNESS OF THE IDENTITY COLOURING EXTENDS OFF THE WALKED TREE
   (P1b, measured): at all 1417 principal swapped states -- states no
   greedy walk chose -- the abstract walker's menu is the engine's, 0
   parting. F1's control was PR2's trajectory plus the branch tree; this
   is every principal state the sweep touched.

WHAT THIS RIG CANNOT DO, so it is not claimed. The verdict is scoped to
the ACTIVE colours of the walked-plus-constructed region; a coarsening
merging only colours that region never touches is unrefuted by
construction. The number rings are untouched (T2): their coarsest
question carries the ladder column as an extra axis. And the open residue
in F2 -- what, beyond aut-conjugacy, decides menu survival -- is named,
not answered.

RUN RECORD. One process, CPython, no BLAS. Wall 1.6 s, peak working set
~18 MB against the 512 MB ceiling. 4845 checks here, plus the imported
machinery's own (six ring engines imported, never rewritten).
"""

import os

os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")

import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from math import factorial

from math import gcd

import explore_class_schedule as CS
import explore_coarse_type as CT
from explore_greedy_image_ec import v2

CHECKS = 0
BFS_D = CS.BFS_D          # five levels: the void plus states <= 4 moves out
COL_N = 8                 # doors the price-fibre columns are read over


def ok(cond, msg):
    global CHECKS
    assert cond, msg
    CHECKS += 1


def section(t):
    print("\n" + "=" * 72)
    print(t)
    print("=" * 72)


# ------------------------------------------------------------- projections
def proj_veh_p(col_of, veh, phi):
    """A vehicle through an arbitrary colouring phi: colour -> block label.
    A colour outside phi's domain (the partition covers ACTIVE colours;
    a stored witness state's menu can reach others) stays itself, and
    labels are stringified so heterogeneous ones sort."""
    return tuple(sorted((str(phi.get(col_of[pl], col_of[pl])), e)
                        for pl, e in veh.items() if e))


def proj_menu_p(col_of, cost, ties, phi):
    return (cost, tuple(sorted(proj_veh_p(col_of, v, phi) for v in ties)))


def class_sum(sup, col_of, st):
    s = 0
    for pl, e in st.items():
        if e:
            s = sup.add(s, sup.mul(e, col_of[pl][1]))
    return s


def proj_veh(col_of, veh, merged):
    out = []
    for pl, e in veh.items():
        if e:
            c = col_of[pl]
            out.append((("M",) if c in merged else ("c",) + c, e))
    return tuple(sorted(out))


def proj_menu(col_of, cost, ties, merged):
    return (cost, tuple(sorted(proj_veh(col_of, v, merged) for v in ties)))


def proj_state(col_of, st, merged):
    return tuple(sorted(
        (("M",) if col_of[pl] in merged else ("c",) + col_of[pl], e)
        for pl, e in st.items() if e))


# ------------------------------------------- S0/S1 the tree and the controls
def walk_tree(L):
    """The ring's own branch tree, engine menus cached, active colours
    collected; the identity-colouring walker asserted against the engine at
    every state (P1a)."""
    sup, places = CS.ring_supply(L)
    R = L.R
    col_of = dict((pl, (d, c)) for (d, c, i), pl in places.items())
    item_of = dict((pl, q) for q, pl in places.items())
    pls_of = {}
    for (d, c, i), pl in sorted(places.items()):
        pls_of.setdefault((d, c), []).append(pl)

    menus = {}                    # state key -> (cost, ties)
    active = set()
    states = []
    seen, frontier = set(), [{}]
    for lvl in range(BFS_D + 1):
        expand = lvl < BFS_D
        nxt = []
        for st0 in frontier:
            key = tuple(sorted((pl, e) for pl, e in st0.items() if e))
            if key in seen:
                continue
            seen.add(key)
            lam0 = R.lam_state(st0)
            c0, t0 = L.mod.MENUS["element"](R, st0, lam0)
            menus[key] = (c0, t0)
            states.append(dict(st0))
            for pl, e in st0.items():
                if e:
                    active.add(col_of[pl])
            for v in t0:
                for pl in v:
                    active.add(col_of[pl])
            probe = CS.CWalk(sup)
            probe.st = dict((item_of[pl], e) for pl, e in st0.items() if e)
            probe.T = 1 << v2(lam0)
            ca, ta = probe.menu()
            ok(ca == c0, "%s: P1a cost %d against the ring's %d at %s"
               % (L.name, ca, c0, key))
            ok(sorted(tuple(sorted(CS.to_place(v, places).items()))
                      for v, _c, _n in ta)
               == sorted(tuple(sorted(v.items())) for v in t0),
               "%s: P1a menus part at %s" % (L.name, key))
            if not expand:
                continue
            for veh in t0:
                st1 = dict(st0)
                for pl, e in veh.items():
                    st1[pl] = st1.get(pl, 0) + e
                nxt.append(st1)
        frontier = nxt
    return sup, places, col_of, item_of, pls_of, menus, states, active


def engine_menu(L, menus, st):
    key = tuple(sorted((pl, e) for pl, e in st.items() if e))
    if key not in menus:
        lam = L.R.lam_state(st)
        menus[key] = L.mod.MENUS["element"](L.R, st, lam)
    return menus[key]


def attack(L, ctx, offtree, pairs, st0, only=None):
    """Every swap st0 offers, against every pair (or one named pair)."""
    sup, places, col_of, item_of, pls_of, menus, states, active = ctx
    key0 = tuple(sorted((pl, e) for pl, e in st0.items() if e))
    ok(class_sum(sup, col_of, st0) == 0,
       "%s: an attacked state is not principal at %s" % (L.name, key0))
    reps = {}
    for col in sorted(active):
        bye = {}
        for pl in pls_of[col]:
            e = st0.get(pl, 0)
            if e not in bye:
                bye[e] = pl
        reps[col] = bye
    cols = sorted(active)
    todo = ([tuple(sorted(only))] if only else
            [(cols[i], cols[j]) for i in range(len(cols))
             for j in range(i + 1, len(cols))])
    for A, B in todo:
        mk = frozenset((A, B))
        rec = pairs.setdefault(mk, {
            "swaps": 0, "principal": 0, "agree": 0,
            "k1": None, "k2": None})
        if rec["k1"] and rec["k2"] and not only:
            continue
        for eA, px in sorted(reps[A].items()):
            for eB, py in sorted(reps[B].items()):
                if eA == eB:
                    continue
                rec["swaps"] += 1
                st1 = dict(st0)
                st1[px] = eB
                st1[py] = eA
                st1 = dict((pl, e) for pl, e in st1.items() if e)
                ok(proj_state(col_of, st0, mk)
                   == proj_state(col_of, st1, mk),
                   "%s: the swap moved the projection" % L.name)
                if class_sum(sup, col_of, st1) != 0:
                    if rec["k1"] is None:
                        rec["k1"] = (key0, eA, eB)
                    continue
                rec["principal"] += 1
                c0, t0 = engine_menu(L, menus, st0)
                c1, t1 = engine_menu(L, menus, st1)
                # P1b: the identity walker at the swapped state,
                # recorded rather than asserted
                probe = CS.CWalk(sup)
                probe.st = dict((item_of[pl], e)
                                for pl, e in st1.items() if e)
                probe.T = 1 << v2(L.R.lam_state(st1))
                ca, ta = probe.menu()
                same = (ca == c1 and
                        sorted(tuple(sorted(
                            CS.to_place(v, places).items()))
                               for v, _c, _n in ta)
                        == sorted(tuple(sorted(v.items())) for v in t1))
                offtree[0] += 1
                if not same:
                    offtree[1].append((L.name, st1))
                m0 = proj_menu(col_of, c0, t0, mk)
                m1 = proj_menu(col_of, c1, t1, mk)
                if m0 != m1:
                    # a difference in COST or TIE WIDTH survives EVERY
                    # coarser projection; a composition-only difference
                    # need not, so the robust kind is kept preferentially
                    # and S4 re-projects the other kind per partition
                    key1 = tuple(sorted(st1.items()))
                    robust = (c0 != c1 or len(t0) != len(t1))
                    if rec["k2"] is None or (robust and not rec["k2"][2]):
                        rec["k2"] = (key0, key1, robust)
                else:
                    rec["agree"] += 1


def sweep_ring(L, ctx, offtree):
    """Every active pair-merge attacked by every swap the tree offers."""
    pairs = {}                    # frozenset({A,B}) -> record
    for st0 in ctx[6]:
        attack(L, ctx, offtree, pairs, st0)
    return pairs


def ordc(sup, c):
    """The additive order of a class."""
    n, x = 1, c
    while x != 0:
        x = sup.add(x, c)
        n += 1
    return n


def constructed_stage(L, ctx, offtree, pairs):
    """For every pair still lacking a menu verdict, a state built to OFFER a
    principal swap: seat one colour's item at the additive order of the class
    difference (so the swap preserves principality by construction), plus
    the minimal representative that makes the seed principal at all. Turns a
    survival by starvation into a verdict either way."""
    sup, places, col_of, item_of, pls_of, menus, states, active = ctx
    built = 0
    for mk in sorted(pairs, key=sorted):
        rec = pairs[mk]
        if rec["k2"]:
            continue
        A, B = sorted(mk)
        n0 = ordc(sup, sup.add(B[1], sup.neg(A[1])))
        for X in (A, B):
            for n in sorted(set((1, n0, 2 * n0))):
                want = sup.neg(sup.mul(n, X[1]))
                rep = sup.reps[want][0]
                st = {}
                pl = places[(X[0], X[1], 0)]
                st[pl] = st.get(pl, 0) + n
                for it, e in rep.items():
                    p2 = places[it]
                    st[p2] = st.get(p2, 0) + e
                # the seed alone is too symmetric a state -- a core move is
                # never at the best cost there -- so the engine's own greedy
                # walk DESCENDS from it, and the pair is attacked at every
                # state on the way down, where the cheap opens are spent and
                # the seated items' own moves surface in the menu
                cur = st
                for _step in range(5):
                    built += 1
                    attack(L, ctx, offtree, pairs, cur, only=mk)
                    if pairs[mk]["k2"]:
                        break
                    _c0, t0 = engine_menu(L, menus, cur)
                    cur = dict(cur)
                    for p2, e in t0[0].items():
                        cur[p2] = cur.get(p2, 0) + e
        # THE CONTEXT STAGE: a global relabelling along a supply
        # automorphism f with f(A) = B defends the pair against every swap
        # whose context is f-symmetric -- so a THIRD colour C is seated
        # beside the swap. The swap stays principal (n0 is the order of the
        # class difference) while f moves C's class, so no relabelling maps
        # the swapped state back and any surviving agreement is the state's
        # own doing, not a symmetry's.
        if pairs[mk]["k2"]:
            continue
        for C in sorted(active):
            if C in (A, B) or pairs[mk]["k2"]:
                continue
            # k runs over the context class's own order too: there the
            # context self-cancels and the swap is principal with the
            # asymmetric context actually beside it
            for k in sorted(set((1, 2, ordc(sup, C[1])))):
                for X in (A, B):
                    if pairs[mk]["k2"]:
                        break
                    want = sup.neg(sup.add(sup.mul(n0, X[1]),
                                           sup.mul(k, C[1])))
                    rep = sup.reps[want][0]
                    st = {places[(X[0], X[1], 0)]: n0}
                    plC = places[(C[0], C[1], 0)]
                    st[plC] = st.get(plC, 0) + k
                    for it, e in rep.items():
                        p2 = places[it]
                        st[p2] = st.get(p2, 0) + e
                    built += 1
                    attack(L, ctx, offtree, pairs, st, only=mk)
    return built


def group_autos(sup):
    """Every automorphism of the class group, from its addition table alone:
    generators found greedily, images extended coset by coset, bijectivity
    checked at the end. h <= 15 here, so brute is cheap."""
    h = sup.h
    gens, span = [], {0}
    for c in range(h):
        if c not in span:
            gens.append(c)
            span = set(sup.add(s, sup.mul(k, c)) for s in span
                       for k in range(ordc(sup, c)))
    out = []

    def rec(i, f):
        if i == len(gens):
            if len(set(f.values())) == h:
                out.append(dict(f))
            return
        g = gens[i]
        og = ordc(sup, g)
        m = next(k for k in range(1, og + 1) if sup.mul(k, g) in f)
        for y in range(h):
            if sup.mul(m, y) != f[sup.mul(m, g)]:
                continue
            f2 = dict(f)
            good = True
            for k in range(1, m):
                if not good:
                    break
                for s in list(f):
                    z = sup.add(s, sup.mul(k, g))
                    w = sup.add(f[s], sup.mul(k, y))
                    if z in f2 and f2[z] != w:
                        good = False
                        break
                    f2[z] = w
            if good:
                rec(i + 1, f2)

    rec(0, {0: 0})
    return out


_PA_CACHE = {}


def preserved_autos(sup):
    """The subgroup of Aut(C) preserving the supply matrix over the full
    window: f with n(d, f(c)) = n(d, c) at every colour. The cache key is
    the CONTENT, never id() -- a collected Supply's id gets reused."""
    key = (sup.h, tuple(tuple(r) for r in sup.addc),
           tuple(sorted(sup.cnt.items())))
    if key not in _PA_CACHE:
        _PA_CACHE[key] = [f for f in group_autos(sup)
                          if all(sup.cnt.get((d, f[c]), 0) == v
                                 for (d, c), v in sup.cnt.items())]
    return _PA_CACHE[key]


def aut_conjugate(sup, A, B):
    return (A[0] == B[0]
            and any(f[A[1]] == B[1] for f in preserved_autos(sup)))


def inv_partner(sup, col):
    return (col[0], sup.neg(col[1]))


def s1_report(L, sup, active, pairs):
    """Three observables per pair: a menu parts (K2), only the state space
    parts (K1 with menus agreeing at every principal swap), or nothing does.
    A pair without K2 is a MENU SURVIVOR, and the principal/agree counts say
    whether it survived by agreement or was never offered a principal swap."""
    xdeg = xcls = inv = 0
    k2 = 0
    survivors = []
    for mk, rec in sorted(pairs.items(), key=lambda kv: sorted(kv[0])):
        A, B = sorted(mk)
        if A[0] != B[0]:
            xdeg += 1
        elif B == inv_partner(sup, A):
            inv += 1
        else:
            xcls += 1
        if rec["k2"]:
            k2 += 1
        else:
            survivors.append((A, B, rec))
    print("%-8s %3d active colours  %4d pairs (%d xdeg, %d xcls, %d inv)"
          "  K2 %4d  menu-survivors %d"
          % (L.name, len(active), len(pairs), xdeg, xcls, inv,
             k2, len(survivors)))
    for A, B, rec in survivors:
        tag = "inverse" if B == inv_partner(sup, A) else "NON-INVERSE"
        how = ("by agreement" if rec["principal"]
               else "BY STARVATION -- no principal swap offered")
        broken = "state space parts (K1)" if rec["k1"] else "NOTHING parts"
        print("    survivor %s ~ %s  [%s]  %s; %s; swaps %d, principal %d,"
              " agreeing %d"
              % (A, B, tag, broken, how, rec["swaps"], rec["principal"],
                 rec["agree"]))
    return survivors


# --------------------------------------- evaluating a WHOLE coarsening
def eval_partition(ctx, pairs, blocks, full=False):
    """One coarsening, on transfer-VALID evidence only. blocks maps every
    active colour to its block label. A K1 witness transfers to any coarser
    colouring outright (principality reads no projection), as does a menu
    difference in COST or TIE WIDTH (both projection-invariant); a
    composition-only menu difference is RE-PROJECTED through this very
    partition before it counts. Returns (kind, detail): kind in 'improper',
    'k1', 'robust', 'reproj', 'unresolved' -- with full=True the k1 early
    exit is skipped so the menu evidence is still looked for."""
    col_of, menus = ctx[2], ctx[5]
    merged = [mk for mk in pairs
              if len(set(blocks[c] for c in mk)) == 1]
    if not merged:
        return "improper", None
    k1_hit = None
    for mk in merged:
        if pairs[mk]["k1"]:
            k1_hit = mk
            if not full:
                return "k1", mk
            break
    for mk in merged:
        k2 = pairs[mk]["k2"]
        if k2 and k2[2]:
            return "robust", mk
    for mk in merged:
        k2 = pairs[mk]["k2"]
        if k2:
            key0, key1, _r = k2
            c0, t0 = menus[key0]
            c1, t1 = menus[key1]
            if (proj_menu_p(col_of, c0, t0, blocks)
                    != proj_menu_p(col_of, c1, t1, blocks)):
                return "reproj", mk
    if k1_hit:
        return "k1", k1_hit
    return "unresolved", None


def partitions_gen(cols):
    """Every partition of cols, as restricted growth strings."""
    n = len(cols)

    def rec(i, labels, nb):
        if i == n:
            yield dict(zip(cols, labels))
            return
        for b in range(nb + 1):
            labels.append(b)
            for p in rec(i + 1, labels, nb + 1 if b == nb else nb):
                yield p
            labels.pop()

    return rec(0, [], 0)


def s4_lattice(L, ctx, pairs):
    """EVERY proper coarsening of the active colours, evaluated outright --
    the pair sweep alone cannot license the universal claim, because a
    composition-only menu witness can collapse under a coarser projection."""
    cols = sorted(ctx[7])
    tally = {"k1": 0, "robust": 0, "reproj": 0, "unresolved": 0}
    total = 0
    for blocks in partitions_gen(cols):
        if len(set(blocks.values())) == len(cols):
            continue
        total += 1
        kind, _w = eval_partition(ctx, pairs, blocks)
        tally[kind] += 1
    print("%-8s %8d proper coarsenings: %d by state space, %d by a "
          "cost/width menu difference, %d by re-projection, %d UNRESOLVED"
          % (L.name, total, tally["k1"], tally["robust"], tally["reproj"],
             tally["unresolved"]))
    return total, tally


# ------------------------------------------------- S2 the named coarsenings
def named_verdicts(L, ctx, pairs):
    sup, active = ctx[0], ctx[7]

    def cost_col(col):
        return tuple(CS.cost(sup, col[0], col[1], n)
                     for n in range(1, COL_N + 1))

    names = [
        ("degree only (lockstep)", lambda c: c[0]),
        ("class only (degree-blind)", lambda c: c[1]),
        ("one colour", lambda c: 0),
        ("price fibres", cost_col),
        ("class up to inversion", lambda c: (c[0], min(c[1],
                                                       sup.neg(c[1])))),
        ("class up to preserved Aut",
         lambda c: (c[0], min(f[c[1]] for f in preserved_autos(sup)))),
    ]
    out = {}
    for name, phi in names:
        blocks = dict((c, phi(c)) for c in active)
        kind, _w = eval_partition(ctx, pairs, blocks, full=True)
        text = {
            "improper": "no active pair merged",
            "robust": "BREAKS A MENU (cost or width)",
            "reproj": "BREAKS A MENU (re-projected witness)",
            "k1": "breaks the state space only",
            "unresolved": "UNRESOLVED in region",
        }[kind]
        out[name] = text
        print("    %-28s %s" % (name, text))
    return out


def fibre_check(L, sup, active):
    """P5: the price-fibre partition against the inversion partition AND
    against the preserved-Aut orbit partition, on the active colours."""
    def cost_col(col):
        return tuple(CS.cost(sup, col[0], col[1], n)
                     for n in range(1, COL_N + 1))
    fib, invp, autp = {}, {}, {}
    for col in active:
        fib.setdefault(cost_col(col), set()).add(col)
        invp.setdefault((col[0], min(col[1], sup.neg(col[1]))),
                        set()).add(col)
        autp.setdefault((col[0], min(f[col[1]]
                                     for f in preserved_autos(sup))),
                        set()).add(col)
    a = sorted(frozenset(v) for v in fib.values())
    b = sorted(frozenset(v) for v in invp.values())
    c = sorted(frozenset(v) for v in autp.values())
    return a == b, a == c, a, b


# ------------------------------------------------------- S3 the count half
def merged_orbit(sup, phi, rows):
    """The multinomial of an arbitrary coarsening: at each phi-cell, choose
    which of the cell's items are seated and divide inside repeated
    exponents."""
    tot = 1
    for k, exps in rows.items():
        n = sum(v for col, v in sup.cnt.items() if phi(col) == k)
        kk = len(exps)
        if kk > n:
            return 0
        num = factorial(n) // factorial(n - kk)
        mult = {}
        for e in exps:
            mult[e] = mult.get(e, 0) + 1
        for v in mult.values():
            num //= factorial(v)
        tot *= num
    return tot


def count_half(L, sup):
    """Pooled distinct configurations of the truncated supply, grouped per
    coarsening, against that coarsening's multinomial."""
    small = CS.Supply(sup.tag, sup.h, sup.addc,
                      dict((k, v) for k, v in sup.cnt.items() if k[0] <= 4),
                      dmax=4)
    lv, _census = CS.levels(small, CS.BUDGET)
    configs = set()
    for level in lv:
        for w in level.values():
            configs.add(w.config())

    U = preserved_autos(small)

    def phis():
        yield "identity", lambda c: c
        yield "degree-blind", lambda c: c[0]
        yield "inversion", lambda c: (c[0], min(c[1], small.neg(c[1])))
        yield "aut-orbit", lambda c: (c[0], min(f[c[1]] for f in U))

    out = {}
    for name, phi in phis():
        shapes = {}
        for cfg in configs:
            rows = {}
            for (d, c, i), e in cfg:
                rows.setdefault(phi((d, c)), []).append(e)
            key = tuple(sorted((k, tuple(sorted(v)))
                               for k, v in rows.items()))
            shapes.setdefault(key, set()).add(cfg)
        off = 0
        for key, cfgs in shapes.items():
            want = merged_orbit(small, phi, dict((k, list(v))
                                                 for k, v in key))
            if want != len(cfgs):
                off += 1
        out[name] = (len(shapes), len(configs), off)
    return out


# ------------------------------------------------------------------- main
def main():
    CT.EC.DMAX = CS.DMAX
    CT.G2.DMAX = CS.DMAX
    ladders = CT.build_ladder()

    section("S0/S1  THE PAIR SWEEP -- every proper coarsening, by the "
            "lattice reduction")
    print("Every unordered pair of active colours is a maximal proper")
    print("coarsening; a witness against it transfers to every coarser")
    print("colouring. K2 = a menu parts at a principal swap; K1 = the swap")
    print("leaves the state space. P1a is asserted at every tree state.\n")
    offtree = [0, []]
    ctxs, allpairs, allsurv = {}, {}, {}
    for L in ladders:
        ctx = walk_tree(L)
        ctxs[L.name] = (L, ctx)
        pairs = sweep_ring(L, ctx, offtree)
        built = constructed_stage(L, ctx, offtree, pairs)
        print("  [%s: %d constructed states for the pairs the tree "
              "starved]" % (L.name, built))
        allpairs[L.name] = pairs
        allsurv[L.name] = s1_report(L, ctx[0], ctx[7], pairs)
    print("\nP1b off the tree: %d principal swapped states priced by the"
          % offtree[0])
    print("identity walker against the engine, %d parting."
          % len(offtree[1]))
    if offtree[1]:
        for name, st1 in offtree[1][:5]:
            print("  PARTS %s %s" % (name, sorted(st1.items())))

    section("S2  THE NAMED COARSENINGS AND THE PRICE'S FIBRES")
    for L in ladders:
        _L, ctx = ctxs[L.name]
        sup, active = ctx[0], ctx[7]
        print("  %s:" % L.name)
        named_verdicts(L, ctx, allpairs[L.name])
        same, same_aut, a, b = fibre_check(L, sup, active)
        print("    price fibres == inversion partition on active colours: %s"
              % same)
        print("    price fibres == preserved-Aut orbits on active colours: "
              "%s" % same_aut)
        if not same:
            print("      fibres    %s" % a)
            print("      inversion %s" % b)

    section("S3  THE WHOLE LATTICE -- every proper coarsening, evaluated "
            "outright")
    print("A composition-only menu witness can collapse under a coarser")
    print("projection, so the universal claim is not the pair sweep's to")
    print("make: every partition of the active colours is walked, broken")
    print("by a transferring witness or by re-projecting a stored one.\n")
    lattice = {}
    for L in ladders:
        _L, ctx = ctxs[L.name]
        lattice[L.name] = s4_lattice(L, ctx, allpairs[L.name])
    unres = sum(t["unresolved"] for _tot, t in lattice.values())

    section("S4  THE COUNT HALF -- the merged multinomial against the "
            "enumerated configurations")
    print("%-8s %-14s %8s %8s %6s" % ("ring", "colouring", "shapes",
                                      "configs", "off"))
    for L in ladders:
        _L, ctx = ctxs[L.name]
        sup = ctx[0]
        rows = count_half(L, sup)
        for name in ("identity", "degree-blind", "inversion", "aut-orbit"):
            sh, cf, off = rows[name]
            print("%-8s %-14s %8d %8d %6d" % (L.name, name, sh, cf, off))
        ok(rows["identity"][2] == 0,
           "%s: the identity multinomial is off -- the control is broken"
           % L.name)
        if sup.h > 1:
            ok(rows["degree-blind"][2] > 0,
               "%s: the degree-blind formula is exact here, against F5"
               % L.name)

    section("VERDICT -- coarsest, read per observable")
    all_broken = True
    menu_surv = []
    for L in ladders:
        sup = ctxs[L.name][1][0]
        surv = allsurv[L.name]
        whole = [s for s in surv if not s[2]["k1"]]
        if whole:
            all_broken = False
        for A, B, rec in surv:
            menu_surv.append((L.name, A, B,
                              B == inv_partner(sup, A), rec))
        print("  %s: %d pairs, %d menu-survivors, %d with nothing parting"
              % (L.name, len(allpairs[L.name]), len(surv), len(whole)))
    if all_broken and unres == 0:
        print("\n  THE WALK: every active pair-merge parts the state space")
        print("  or a menu, and the LATTICE WALK (S3) finds every proper")
        print("  coarsening broken with 0 unresolved -- (degree, class) is")
        print("  COARSEST for the walk in the walked region.")
    elif unres:
        print("\n  THE WALK: %d coarsenings in the lattice walk are"
              % unres)
        print("  UNRESOLVED by the stored witnesses -- the universal claim")
        print("  is NOT made; the unresolved partitions are the residue.")
    print("\n  THE MENUS ALONE: pairs no principal swap could part, against")
    print("  conjugacy under the supply-preserving automorphisms --")
    if not menu_surv:
        print("    none -- every active pair-merge parts a MENU.")
    exact = True
    for name, A, B, isinv, rec in menu_surv:
        sup = ctxs[name][1][0]
        conj = aut_conjugate(sup, A, B)
        if not conj:
            exact = False
        print("    %-8s %s ~ %s  %-12s aut-conjugate %-5s "
              "(principal %d, agreeing %d)"
              % (name, A, B, "inverse" if isinv else "non-inverse",
                 conj, rec["principal"], rec["agree"]))
    for L in ladders:
        name = L.name
        sup = ctxs[name][1][0]
        surv_set = set(frozenset((A, B)) for n2, A, B, _i, _r in menu_surv
                       if n2 == name)
        missing = []
        for mk in allpairs[name]:
            A, B = sorted(mk)
            if aut_conjugate(sup, A, B) and mk not in surv_set:
                missing.append((A, B))
                exact = False
        print("  %-8s |Aut| %d, supply-preserving %d%s"
              % (name, len(group_autos(sup)), len(preserved_autos(sup)),
                 "  AUT-CONJUGATE PAIR BROKEN: %s" % missing
                 if missing else ""))
    if exact:
        print("\n  ... the menu-survivors are EXACTLY the aut-conjugate")
        print("  pairs: the menu half alone reaches (degree, class up to")
        print("  the supply-preserving automorphisms), and the state space")
        print("  and the count (S3) are what refute those merges.")
    else:
        print("\n  ... the menu-survivors are NOT exactly the aut-conjugate")
        print("  pairs; the residue is listed above and is the finding.")
    print("\n%d checks here, plus the imported machinery's own." % CHECKS)


if __name__ == "__main__":
    main()
