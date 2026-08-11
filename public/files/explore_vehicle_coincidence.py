"""explore_vehicle_coincidence.py -- the coincidence locus: which two
offers summon ONE vehicle, across the six curve supplies and the two
number rings, and what the menu's tie width owes it

THE QUESTION. explore_menu_invisibility.py's mechanism exception found two
cores each summoning exactly the other's increment -- one vehicle, recorded
once, so a tie WIDTH the dedup collapses at one state and not its
neighbour -- and closing it took a dedicated scan (S7 there). Nothing has
asked what coincidence does elsewhere: which (core, door) pairs CAN wear
another's shape, whether the locus of such pairs is degenerate or
patterned, and where menus carry width as signal at all. The suspicion is
written in the SUPPLY MATRIX's own vocabulary: a vehicle is the core at
its door exponent merged with the rider minrep(-n*c), so coincidence is a
multiset equation over the matrix and the locus should be a matrix-level
structure, before any state or region enters.

THE HAND-ATTACK, on paper before any engine code.

 D1 THE TWO FORMS, exhaustive. Write an offer's vehicle as {X:n} + r_X
    where r_X = rep(neg(n*cX)), the unique minimal representative (the
    uniqueness gate holds at all six rings, and both number rings' reps
    are proved unique). Suppose vehicle(X,n) = vehicle(Y,m) at distinct
    offers.
    - X != Y (THE EXCHANGE). Comparing X-multiplicities: n + r_X(X) =
      r_Y(X), so r_Y contains X at exponent >= n; comparing Y: r_X
      contains Y at exponent >= m; and setting s := r_X - {Y:m} gives
      r_X = {Y:m} + s  AND  r_Y = {X:n} + s
      -- each core rides inside the OTHER's rider at exactly the other's
      door exponent, and the riders agree off the pair. Conversely any
      such (X,n,Y,m,s) is a coincidence. s empty is the mechanism
      exception's shape.
    - X = Y, n > m (THE ECHO). The same comparison collapses to
      rep(neg(m*c)) = {X:(n-m)} + rep(neg(n*c))
      -- the shallower door's rider carries the core itself at the door
      gap, riding on the deeper door's rider.
    There is no third form: two offers share a vehicle iff they are an
    exchange or an echo. (Multiplicities were tracked as signed multisets
    throughout, so a rider landing on its own core is covered.)

 D2 THE DOOR BOUND, derived per ring from its OWN rider content -- the
    aim's WATCH FOR: the parent's no-collision-beyond-the-window argument
    is not borrowed, the bound is re-derived here from each matrix. Let
    Nmax(q) = the largest exponent item q carries in ANY minimal
    representative. An exchange forces n <= Nmax(X) and m <= Nmax(Y)
    (each door exponent sits inside the other's rider); an echo forces
    gap = n - m <= Nmax(X). So exchange doors are BOUNDED and the
    enumeration over n <= Nmax is complete -- a theorem about the matrix,
    not a scanned window. An echo's BASE door m is unbounded, but the
    condition reads m only through the class neg(m*c), so it is periodic
    with period ord(c): echoes come in infinite arithmetic families, one
    per (item, base residue, gap) triple, enumerated completely over one
    period. The brute-force control below still scans a literal window
    W = h + max Nmax + 2 and the two enumerations are asserted equal on
    it.

 D3 THE ELLIPTIC LAW, derived. At a supply where every nonzero class's
    minimal representative is a single degree-1 item (the elliptic rings:
    m = 1 on every nonzero class), write R(c) for class c's minrep item.
    Degrees force everything: an exchange needs n = m = 1, s empty, and
    the condition becomes rep(neg cX) = {Y:1}, rep(neg cY) = {X:1}, i.e.
    X = R(c), Y = R(-c) for an inverse pair c != -c of nonzero classes,
    at doors (1,1) -- the INVERSE INVOLUTION on minrep items, exactly
    (h - 1 - t2)/2 exchanges where t2 counts nonzero 2-torsion. An echo
    needs gap = 1 and rider degree 0 at the deep door, so n = 0 mod
    ord(c), m = n - 1, rep(neg(m*c)) = rep(c) = {X:1}: one family per
    nonzero class c, (R(c), base ord(c)-1, gap 1), period ord(c). Nothing
    else exists at such a supply.

 D4 THE SKELETON LAW, a property of the forms. Both forms seat each
    participating core INSIDE a minimal representative (X in r_Y for the
    exchange, X in the shallow rider for the echo), so every core of every
    coincident offer is an item some minrep uses. The bulk of the supply
    -- every item no minrep touches -- can never wear another's shape or
    be worn. The locus lives on the minrep skeleton.

 D5 THE NUMBER RINGS, by the same forms with norms multiplying (degree 0
    becomes norm 1; the rider bound is the minreps' content, so exchange
    doors satisfy N(X)^n <= max_z m(z), tiny at both rings). Hand
    predictions: K5 (h = 2, one class-1 least item, the ramified place
    over 2, m(1) = 2): NO exchange -- the inverse involution needs
    c != -c and the lone nonzero class is 2-torsion -- and exactly one
    echo family ((P, base 1, gap 1), period 2: {P:1}+rep(1) = {P:2} =
    {P:2}+rep(0)). K23 (h = 3, split 2 with conjugate places in classes
    1 and 2): exactly one exchange -- the split pair at doors (1,1),
    rep(2) = {Q:1} and rep(1) = {P:1} -- plus one echo family per
    nonzero class (base 2, gap 1, period 3). The elliptic law's shape,
    crossed into the multiplicative world.

 D6 THE IDEAL WORLD IS EMPTY (property, no scan owed). An ideal-world
    offer's vehicle is one place at one exponent; distinct offers give
    distinct vehicles outright. Width as a signal is an ELEMENT-world
    phenomenon, created by the rider.

 D7 WHAT THE MENU'S WIDTH OWES THE LOCUS. Coincident offers always share
    a price (the cost is the vehicle's own total degree), so wherever
    both offers of a locus pair are legal at a state, they sit on one
    tier and the dedup records one vehicle: the cheapest tier's OFFER
    COUNT minus its VEHICLE COUNT should equal, state by state, the
    number of locus-induced collisions among its legal offers -- the
    width deficit IS the locus, read dynamically. The tier read is
    dedup-blind and colour-blind per the parent's refinement: an (X, n)
    offer is on the tier iff its cost equals the tier's; no core
    identity is consulted (the aim's first WATCH FOR).

TRANSPLANT FLAGS, fixed at the freeze.
 T1 The elliptic closed form is re-derived for the number rings via
    degree -> log norm (D5), not carried: the degree-0 rider step becomes
    the norm-1 rider step. Marked because the crossing is exactly where
    the ladder column broke the last port.
 T2 Realization (S6) is read over the parent's BFS region only: a count
    there is region-scoped, never "never realized".
 T3 The locus is enumerated over the FULL truncated matrix (every colour
    to dmax), wider than the parent's active-colour scope; the width
    identity is asserted only at visited states, where the menus are.

PREDICTIONS, frozen before the engine runs.
 P1 (positive controls, read before any verdict) The h = 1 engineered
    supply -- empty riders everywhere -- prints an EMPTY locus from the
    brute scan; and at the first elliptic h = 3 supply the hand-derived
    exchange {(R(1),1), (R(2),1)} sits in the brute buckets, found by
    the scan and not by the characterization code.
 P2 (the characterization) At all six curve supplies and both number
    rings, the brute-force instance set on the window equals the closed
    form's expansion: every coincidence is an exchange or an echo
    instance, both directions, 0 mismatches.
 P3 (the elliptic law) At every supply with m = 1 on all nonzero
    classes, the locus is exactly D3's: (h-1-t2)/2 exchanges as the
    inverse involution at doors (1,1), h-1 echo families at gap 1.
 P4 (equivariance) The locus is closed under every supply-preserving
    automorphism, at all six rings: exchanges map to exchanges, echo
    families to echo families at the same base and gap.
 P5 (the skeleton) Every core in every brute bucket is a minrep-support
    item -- asserted on the scan's own hits, independent of D4's proof.
 P6 (the width identity) At every tree state of all six rings: legal
    tier offers minus tier vehicles equals the locus collisions among
    those offers, 0 exceptions; the per-ring deficit totals and the
    count of states with a realized collision are UNKNOWN and are the
    printed finding.
 P7 (the number rings) K5: one echo family, no exchange. K23: one
    exchange + two echo families, exactly D5. The genus-2 ring's locus
    shape is UNKNOWN beyond P2/P5 (deeper doors, nonempty s, degree-2
    cores are all newly possible at Nmax 2); its table is the finding.

KILL-SHAPES, named as observables.
  - A brute bucket pair fitting neither form prints ring, offers and
    vehicle: the characterization dies.
  - An elliptic supply whose locus differs from D3 prints the difference.
  - A state where the tier deficit differs from the locus's collision
    count prints state, tier and offers: the width identity dies, and
    the finding is a menu channel the locus does not carry.
  - A locus not closed under a preserved automorphism prints the orbit.
  - A brute-hit core outside the minrep support prints it: D4 dies.

FINDINGS (tiers below; run record at the bottom).

F1 THE TWO FORMS ARE THE WHOLE LOCUS (rule in range; six curve supplies
   and both number rings, brute pairwise scan of every offer to the
   per-ring window against the closed form's expansion, 0 mismatches
   either direction; window instances 0, 2, 5, 6, 6, 35 at the curves
   and 2, 5 at the number rings; the h = 1 control empty and the h3
   hand exchange found by the scan first, P1): every vehicle
   coincidence is an EXCHANGE or an ECHO, P2 in full. The door bound is
   the matrix's own -- every exchange door sits under Nmax and every
   echo is periodic in the core class's order -- so the enumeration is
   complete with no window in the statement (D2).

F2 THE ELLIPTIC LAW IS EXACT (rule in range; the four m=1-on-nonzero
   supplies h2, h3, h4, h5): exchanges are exactly the inverse
   involution on minrep items at doors (1,1) -- 0, 1, 1, 2 of them,
   matching (h-1-t2)/2 at t2 = 1, 0, 1, 0 -- and echoes exactly one
   gap-1 family per nonzero class (1, 2, 3, 4), P3 with 0 difference.
   An elliptic supply's locus is the minrep section of its class group:
   the involution c <-> -c plus each class's order cycle, nothing else.
   The h = 1 ring (F_2[x], trivial group, empty riders) has an EMPTY
   locus: width as a signal is created by the class group, and a
   principal world has none -- the element-world sibling of D6.

F3 THE GENUS-2 LOCUS IS THE SAME LAW WITH THE DOORS DOUBLED
   (observation at the one genus-2 supply, h = 15, Nmax = 2, table
   printed whole): the two degree-1 involution pairs appear at doors
   (1,1) AND AGAIN at doors (2,2) -- the doubled door riding on a
   doubled minimal representative, a shape no Nmax = 1 supply can
   carry -- plus the degree-2 involution pair (c13 ~ c14, order 5) at
   doors (1,1); every exchange is involution-shaped (inverse classes,
   equal doors, s empty), none mixed-degree. Echoes: the four degree-1
   minrep items carry FIVE families each (bases 3, 10, 13, 14 at gap 1
   and base 13 at gap 2, period 15) against the elliptic single family,
   the extra bases being the classes whose minreps use the item at
   exponent 1 or 2; the two degree-2 items carry one family each
   (base 4, gap 1, period 5).

F4 THE LOCUS IS EQUIVARIANT (rule in range; six supplies, every
   preserved automorphism -- 1, 1, 2, 2, 4, 4 of them -- 0 exceptions):
   exchanges transport to exchanges and echo families to echo families
   at the same base and gap, so the locus is a union of preserved-Aut
   orbits, the same equivariance the menu verdicts obey (P4).

F5 THE SKELETON LAW HOLDS ON THE SCAN'S OWN HITS (property by D4;
   asserted at every brute bucket: 0, 2, 5, 6, 6, 27 buckets over
   supports of 0, 1, 2, 3, 4, 6 items): every core of every coincident
   offer is an item some minimal representative uses. Items outside
   the minrep support -- the bulk of every supply, all of it above
   degree 2 -- never share a vehicle with anything.

F6 THE WIDTH DEFICIT IS THE LOCUS, STATE BY STATE, AND WHICH FORM A
   REGION REALIZES IS THE RING'S OWN (rule in range for the identity;
   126 BFS-tree states over the six rings, 0 exceptions -- at every
   state the cheapest tier's legal-offer count minus its vehicle count
   equals the locus collisions among its offers, the walker's printed
   tie width equals the vehicle count, and no tier bucket holds more
   than two offers -- so the deficit counts collision PAIRS exactly). Realization is common
   -- 27 of 126 states carry a collapsed tier, total deficit 33 -- and
   SPLITS BY FORM: the elliptic rings realize only ECHOES (h2: 6
   states, h4: 4, h5: 4 -- every collision a same-item pair, and all
   the elliptic families are gap 1) while g2 realizes only EXCHANGES
   (13 states, deficit 19) and h3 realizes nothing in its 9-state
   region. Both forms reach menus; which one a region's ticks and
   costs admit is ring-shaped, and region-scoped by T2.

F7 THE NUMBER RINGS CARRY THE ELLIPTIC LAW ACROSS THE BRIDGE (rule in
   range; both rings, brute against closed form on the window, P7
   exact): K5 has NO exchange -- its lone nonzero class is 2-torsion,
   the same t2 count that empties an elliptic involution -- and one
   echo family, the ramified place over 2 at base 1, gap 1, period 2.
   K23 has exactly ONE exchange, the split-2 conjugate pair at doors
   (1,1), each place riding in the other's minrep, plus one echo
   family per nonzero class (base 2, gap 1, period 3). The locus law
   crosses degree -> norm with its shape intact: over K23 the two
   conjugate places above 2 offer one vehicle at their bare doors.

WHAT THIS RIG DOES NOT CLAIM. Realization counts are the parent BFS
region's (T2); nothing is said of states outside it, and h3's zero is
a region fact, not a law. The genus-2 inventory is an observation of
one supply's table, not a classified law. The number-ring locus is
matrix-level: no nf dynamics were read (the nf walker prices doors off
the ladder column, untouched here).

RUN RECORD. One process, CPython, no BLAS. Wall 1.5 s, peak working
set 25.1 MB (memwatch) against the 512 MB ceiling. 817 checks pass
(minrep uniqueness asserted per supply, tier buckets asserted pairwise),
plus the rebuilt regions' own P1a faithfulness asserts inside
walk_tree.
"""

import os

os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")

import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import explore_class_schedule as CS
import explore_coarse_type as CT
import explore_coarsest_colouring as CC
import explore_class_species_nf as SNF
import explore_element_schedule_nf as ESN
from explore_greedy_image_ec import v2

CHECKS = 0
MARGIN = 2


def ok(cond, msg):
    global CHECKS
    assert cond, msg
    CHECKS += 1


def section(t):
    print("\n" + "=" * 72)
    print(t)
    print("=" * 72)


def vkey(veh):
    return tuple(sorted(veh.items()))


# ---------------------------------------------------------- uniform wrapper
class World(object):
    """One interface over both supply kinds: item ids, classes, the unique
    minimal representative per class as an id->exponent dict, and the group
    by its addition table."""

    def __init__(self, tag, h, add, items, cls_of, rep_of):
        self.tag = tag
        self.h = h
        self._add = add
        self.items = items
        self.cls = cls_of
        self.rep = rep_of
        self._ord = {}

    def add(self, a, b):
        return self._add(a, b)

    def neg(self, c):
        for cand in range(self.h):
            if self.add(c, cand) == 0:
                return cand
        raise AssertionError("no inverse for %s" % (c,))

    def mul(self, n, c):
        out = 0
        for _ in range(n % self.h if self.h > 1 else 0):
            out = self.add(out, c)
        return out

    def order(self, c):
        if c not in self._ord:
            t, x = 1, c
            while x != 0:
                x = self.add(x, c)
                t += 1
                assert t <= self.h + 1
            self._ord[c] = t if c != 0 else 1
        return self._ord[c]

    def veh(self, q, n):
        v = {q: n}
        for p, e in self.rep(self.neg(self.mul(n, self.cls(q)))).items():
            v[p] = v.get(p, 0) + e
        return v


def world_of_sup(sup):
    return World(sup.tag, sup.h, sup.add, list(sup.items),
                 lambda q: q[1], lambda z: sup.reps[z][0])


def world_of_nf(name, S):
    cls = dict((pl, c) for (pl, n, c, g) in S.items)
    return World(name, S.h, lambda a, b: (a + b) % S.h,
                 [pl for (pl, n, c, g) in S.items],
                 lambda q: cls[q], lambda z: S.minrep(z))


# ------------------------------------------------------------- closed form
def support_nmax(w):
    """Nmax(q): the largest exponent item q carries in any minrep."""
    nmax = {}
    for z in range(w.h):
        for q, e in w.rep(z).items():
            if e > nmax.get(q, 0):
                nmax[q] = e
    return nmax


def sub_multiset(a, q, m):
    out = dict(a)
    out[q] = out.get(q, 0) - m
    if out[q] < 0:
        return None
    if not out[q]:
        del out[q]
    return out


def add_multiset(a, q, m):
    out = dict(a)
    out[q] = out.get(q, 0) + m
    return out


def exchanges(w, nmax):
    """All exchange instances: frozenset({(X,n),(Y,m)}), X != Y, from D1's
    form with doors bounded by Nmax (D2)."""
    out = set()
    for X, nX in nmax.items():
        cX = w.cls(X)
        for n in range(1, nX + 1):
            rA = w.rep(w.neg(w.mul(n, cX)))
            for Y, mu in rA.items():
                if Y == X:
                    continue
                top = min(mu, nmax.get(Y, 0))
                for m in range(1, top + 1):
                    s = sub_multiset(rA, Y, m)
                    if s is None:
                        continue
                    rB = w.rep(w.neg(w.mul(m, w.cls(Y))))
                    if rB == add_multiset(s, X, n):
                        out.add(frozenset(((X, n), (Y, m))))
    return out


def echoes(w, nmax):
    """All echo families (X, base, gap) with base in 1..ord(cls X); the
    instances are (X, base + k*per) ~ (X, base + gap + k*per), k >= 0."""
    out = set()
    for X, nX in nmax.items():
        c = w.cls(X)
        per = w.order(c)
        for g in range(1, nX + 1):
            for m0 in range(1, per + 1):
                rB = w.rep(w.neg(w.mul(m0, c)))
                rA = w.rep(w.neg(w.mul(m0 + g, c)))
                if rB == add_multiset(rA, X, g):
                    out.add((X, m0, g))
    return out


def closed_instances(w, ex, ec, W):
    inst = set(ex)
    for (X, m0, g) in ec:
        per = w.order(w.cls(X))
        m = m0
        while m + g <= W:
            inst.add(frozenset(((X, m), (X, m + g))))
            m += per
    return inst


def brute_buckets(w, W):
    buckets = {}
    for q in w.items:
        for n in range(1, W + 1):
            buckets.setdefault(vkey(w.veh(q, n)), []).append((q, n))
    return dict((k, v) for k, v in buckets.items() if len(v) > 1)


def brute_instances(buckets):
    inst = set()
    for offers in buckets.values():
        for i in range(len(offers)):
            for j in range(i + 1, len(offers)):
                inst.add(frozenset((offers[i], offers[j])))
    return inst


def charted(w):
    """The full chart: (Nmax table, window, exchanges, echo families,
    brute buckets), with the characterization asserted against the scan."""
    nmax = support_nmax(w)
    gmax = max(nmax.values()) if nmax else 0
    W = w.h + gmax + MARGIN
    ex = exchanges(w, nmax)
    ec = echoes(w, nmax)
    binst = brute_instances(brute_buckets(w, W))
    cinst = closed_instances(w, ex, ec, W)
    ok(binst == cinst,
       "%s: brute and closed form part -- brute-only %s, closed-only %s"
       % (w.tag, sorted(map(sorted, binst - cinst))[:3],
          sorted(map(sorted, cinst - binst))[:3]))
    return nmax, W, ex, ec, binst


def is_elliptic(sup):
    """m = 1 on every nonzero class, each minrep a single degree-1 item."""
    return all(sup.m[c] == 1 for c in range(sup.h) if c != 0) and sup.h > 1


def fmt_item(q):
    return "d%d/c%s#%d" % (q[0], q[1], q[2]) if isinstance(q, tuple) \
        and len(q) == 3 and isinstance(q[0], int) else str(q)


def fmt_pair(pr):
    (a, na), (b, nb) = sorted(pr)
    return "(%s,%d)~(%s,%d)" % (fmt_item(a), na, fmt_item(b), nb)


def main():
    ladders = CT.build_ladder()

    # ------------------------------------------------------------------ S0
    section("S0  POSITIVE CONTROLS -- the empty supply and the hand "
            "exchange, read before any verdict")
    h1 = CS.Supply("h1-ctrl", 1, [[0]], {(1, 0): 2, (2, 0): 1})
    w1 = world_of_sup(h1)
    ok(not brute_buckets(w1, 6),
       "h1 control: a trivial supply grew a coincidence")
    print("h1 control: empty riders, brute scan to door 6, locus EMPTY")

    ctxs = []
    for L in ladders:
        ctxs.append((L, CC.walk_tree(L)))
    hand_done = False
    for L, ctx in ctxs:
        sup = ctx[0]
        if sup.h == 3 and is_elliptic(sup) and not hand_done:
            w = world_of_sup(sup)
            R1 = next(iter(sup.reps[1][0]))
            R2 = next(iter(sup.reps[2][0]))
            bb = brute_buckets(w, 6)
            hit = frozenset(((R1, 1), (R2, 1)))
            ok(any(hit == frozenset(pr) for pr in
                   (frozenset((o[i], o[j])) for o in bb.values()
                    for i in range(len(o)) for j in range(i + 1, len(o)))),
               "%s: the hand-derived h3 exchange is missing from the scan"
               % sup.tag)
            print("%s: hand exchange %s found by the brute scan"
                  % (sup.tag, fmt_pair(hit)))
            hand_done = True
    ok(hand_done, "no elliptic h = 3 supply found for the hand control")

    # ------------------------------------------------------------------ S1
    section("S1  THE CHARACTERIZATION -- brute scan against the two forms, "
            "all six curve supplies")
    print("window W = h + max Nmax + %d per ring; every coincidence must"
          % MARGIN)
    print("be an exchange or an echo instance, both directions\n")
    charts = {}
    for L, ctx in ctxs:
        sup = ctx[0]
        ok(sup.unique(), "%s: minrep uniqueness fails -- reps[z][0] is not"
           " THE representative" % L.name)
        w = world_of_sup(sup)
        nmax, W, ex, ec, binst = charted(w)
        charts[L.name] = (sup, w, nmax, ex, ec)
        gmax = max(nmax.values()) if nmax else 0
        print("%-8s h=%d  |support|=%2d  Nmax=%d  W=%2d  exchanges %2d  "
              "echo families %2d  instances on window %3d"
              % (L.name, sup.h, len(nmax), gmax, W, len(ex), len(ec),
                 len(binst)))

    # ------------------------------------------------------------------ S2
    section("S2  THE ELLIPTIC LAW -- involution + order echoes, nothing "
            "else")
    for L, ctx in ctxs:
        sup, w, nmax, ex, ec = charts[L.name]
        if not is_elliptic(sup):
            continue
        t2 = sum(1 for c in range(1, sup.h) if sup.neg(c) == c)
        want_ex = set()
        for c in range(1, sup.h):
            nc = sup.neg(c)
            if nc == c:
                continue
            R = next(iter(sup.reps[c][0]))
            Rn = next(iter(sup.reps[nc][0]))
            want_ex.add(frozenset(((R, 1), (Rn, 1))))
        want_ec = set()
        for c in range(1, sup.h):
            R = next(iter(sup.reps[c][0]))
            want_ec.add((R, w.order(c) - 1 if w.order(c) > 1 else 1, 1))
        ok(ex == want_ex, "%s: elliptic exchanges are not the involution"
           % L.name)
        ok(len(ex) == (sup.h - 1 - t2) // 2,
           "%s: exchange count off the formula" % L.name)
        ok(ec == want_ec, "%s: elliptic echoes are not the order cycles"
           % L.name)
        print("%-8s elliptic: %d exchanges = (h-1-t2)/2 with t2=%d, "
              "%d echo families, exact"
              % (L.name, len(ex), t2, len(ec)))

    # ------------------------------------------------------------------ S3
    section("S3  THE NON-ELLIPTIC TABLES -- the locus printed whole")
    for L, ctx in ctxs:
        sup, w, nmax, ex, ec = charts[L.name]
        if is_elliptic(sup):
            continue
        print("\n%-8s h=%d, Nmax=%d" % (L.name, sup.h,
                                        max(nmax.values()) if nmax else 0))
        for pr in sorted(ex, key=lambda p: sorted(p)):
            (a, na), (b, nb) = sorted(pr)
            print("  exchange  %s" % fmt_pair(pr))
        for (X, m0, g) in sorted(ec):
            print("  echo      %s base %d gap %d period %d"
                  % (fmt_item(X), m0, g, w.order(w.cls(X))))

    # ------------------------------------------------------------------ S4
    section("S4  EQUIVARIANCE -- the locus is a union of preserved-Aut "
            "orbits")
    for L, ctx in ctxs:
        sup, w, nmax, ex, ec = charts[L.name]
        auts = CC.preserved_autos(sup)
        for f in auts:
            fx = lambda q: (q[0], f[q[1]], q[2])
            for pr in ex:
                img = frozenset((fx(q), n) for (q, n) in pr)
                ok(img in ex, "%s: exchange %s leaves the locus under %s"
                   % (L.name, fmt_pair(pr), f))
            for (X, m0, g) in ec:
                ok((fx(X), m0, g) in ec,
                   "%s: echo (%s,%d,%d) leaves the locus under %s"
                   % (L.name, fmt_item(X), m0, g, f))
        print("%-8s closed under all %d preserved automorphisms"
              % (L.name, len(auts)))

    # ------------------------------------------------------------------ S5
    section("S5  THE SKELETON LAW -- every coincident core is a minrep "
            "item, on the scan's own hits")
    for L, ctx in ctxs:
        sup, w, nmax, ex, ec = charts[L.name]
        gmax = max(nmax.values()) if nmax else 0
        bb = brute_buckets(w, sup.h + gmax + MARGIN)
        for offers in bb.values():
            for (q, n) in offers:
                ok(q in nmax, "%s: coincident core %s outside the minrep "
                   "support" % (L.name, fmt_item(q)))
        print("%-8s %d buckets, every core in the %d-item support"
              % (L.name, len(bb), len(nmax)))

    # ------------------------------------------------------------------ S6
    section("S6  THE WIDTH DEFICIT IS THE LOCUS -- dedup-blind tier read "
            "at every tree state")
    print("legal offer: door in the state's own 3-door window, cost equal")
    print("to the tier's (no core identity consulted); the tier's offer")
    print("count minus its vehicle count must equal the locus collisions\n")
    for L, ctx in ctxs:
        sup, w, nmax, ex, ec = charts[L.name]
        item_of, states = ctx[3], ctx[6]
        inst_all = closed_instances(
            w, ex, ec, 3 + max((1 << v2(L.R.lam_state(st)) for st in states),
                               default=1) + (max(nmax.values()) if nmax
                                             else 0))
        realized_states, deficit_total, echo_seen = 0, 0, 0
        for st in states:
            stI = dict((item_of[pl], e) for pl, e in st.items() if e)
            probe = CS.CWalk(sup)
            probe.st = stI
            probe.T = 1 << v2(L.R.lam_state(st))
            best, ties = probe.menu()
            legal = []
            for q in sup.items:
                e = stI.get(q, 0)
                r0 = probe.door(q[0], e)
                for n in range(r0, r0 + 3):
                    if CS.cost(sup, q[0], q[1], n) == best:
                        legal.append((q, n))
            by_veh = {}
            for (q, n) in legal:
                by_veh.setdefault(vkey(w.veh(q, n)), []).append((q, n))
            for offers in by_veh.values():
                ok(len(offers) <= 2,
                   "%s: a tier bucket holds %d offers -- the deficit no"
                   " longer counts collision pairs at %s"
                   % (L.name, len(offers), sorted(stI.items())))
            ok(len(by_veh) == len(ties),
               "%s: tier width %d against %d distinct vehicles at %s"
               % (L.name, len(ties), len(by_veh), sorted(stI.items())))
            deficit = len(legal) - len(by_veh)
            for offers in by_veh.values():
                for i in range(len(offers)):
                    for j in range(i + 1, len(offers)):
                        pr = frozenset((offers[i], offers[j]))
                        ok(pr in inst_all,
                           "%s: tier collision %s is not in the locus at %s"
                           % (L.name, fmt_pair(pr), sorted(stI.items())))
                        (a, na), (b, nb) = sorted(pr)
                        if a == b:
                            echo_seen += 1
            ok(deficit == sum(len(o) - 1 for o in by_veh.values()),
               "%s: deficit arithmetic broke" % L.name)
            if deficit:
                realized_states += 1
                deficit_total += deficit
        print("%-8s %3d states, %3d with a collapsed tier, total deficit "
              "%3d, echo instances realized %d"
              % (L.name, len(states), realized_states, deficit_total,
                 echo_seen))

    # ------------------------------------------------------------------ S7
    section("S7  THE NUMBER RINGS -- the same forms across the "
            "degree->norm bridge")
    for (name, M, h, disc, gen) in SNF.RINGS:
        R = SNF.Ring(name, M, h, disc, gen)
        S = ESN.Supply(R)
        w = world_of_nf(name, S)
        nmax, W, ex, ec, binst = charted(w)
        print("\n%-4s h=%d  |support|=%d  Nmax=%d  W=%d  instances on "
              "window %d" % (name, S.h, len(nmax),
                             max(nmax.values()), W, len(binst)))
        for pr in sorted(ex, key=lambda p: str(sorted(p))):
            print("  exchange  %s" % fmt_pair(pr))
        for (X, m0, g) in sorted(ec, key=str):
            print("  echo      %s base %d gap %d period %d"
                  % (X, m0, g, w.order(w.cls(X))))
        if name == "K5":
            ok(not ex, "K5 grew an exchange against the 2-torsion count")
            ok(len(ec) == 1, "K5: echo family count %d against 1"
               % len(ec))
        if name == "K23":
            ok(len(ex) == 1, "K23: exchange count %d against 1" % len(ex))
            pr = next(iter(ex))
            ok(all(n == 1 for (_q, n) in pr),
               "K23: the exchange is not at doors (1,1)")
            ok(len(ec) == 2, "K23: echo family count %d against 2"
               % len(ec))

    print("\nALL CHECKS PASS: %d" % CHECKS)


if __name__ == "__main__":
    main()
