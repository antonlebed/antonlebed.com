"""explore_menu_invisibility.py -- which aut-conjugate pair-merges are
menu-invisible, and is there an invariant that says so in advance?

THE QUESTION. Of the 140 pair-merges of active colours at the six rings,
explore_coarsest_colouring.py found 14 that no menu parts -- every one
conjugate under the supply-preserving automorphisms of the class group --
while eleven aut-conjugate pairs DO part a menu, so aut-conjugacy is
necessary and not sufficient, and WHICH aut-conjugate pairs part was
measured and left unexplained. The price's own fibres are proved
insufficient (two colours can share their whole cost column and still part
a menu). This rig hunts the invariant that separates the two kinds.

THE HAND-ATTACK, on paper before any engine code.

 D1 THE EQUIVARIANCE THEOREM. Let f be a supply-preserving automorphism of
    the class group: n(d, f(c)) = n(d, c) at every colour of the truncated
    matrix. Relabel every item along f, (d, c, i) -> (d, f(c), i). This is
    an automorphism of the whole abstract dynamics: degrees and the group
    law are preserved by construction; principality is preserved since
    f(0) = 0; m(f(x)) = m(x), since f and its inverse carry effective
    multisets of class x and degree D to effective multisets of class f(x)
    and degree D; and by the uniqueness gate (it holds at all six rings)
    minrep(f(x)) = f(minrep(x)). Doors, covering and the tick read degrees
    and exponents only. Costs: cost(d, f(c), n) = d*n + m(-n*f(c)) =
    d*n + m(f(-n*c)) = cost(d, c, n). So menus transport: the menu at the
    relabelled state is the relabelled menu. And the abstract walker IS the
    ring engine at every state either rig has touched (the faithfulness
    control on the tree, and at all 1417 off-tree principal swapped
    states), so ENGINE menus transport wherever faithfulness holds.

 D2 THE TRANSPORT COROLLARY. If (st, st') is a menu witness for the merge
    {A, B} -- a principal swap whose merged menu projections differ --
    then (f(st), f(st')) is a menu witness for {f(A), f(B)}: the swap
    shape, principality, and the merged projection all transport, a
    difference surviving any bijective relabelling of the context colours.
    So the menu verdict must be CONSTANT ON ORBITS of pairs under the
    supply-preserving automorphism group.

 D3 THE TENSION THAT DECIDES THE QUESTION. The measured inventory is NOT
    orbit-constant as it stands: at the five-class curve ring the degree-1
    survivors include {1,2} and {1,3} (class labels with neg(1) = 2,
    neg(3) = 4) while {3,4}, {2,3} and {2,4} part -- and the orbit of the
    pair {1,2} under the four supply-preserving automorphisms contains
    {3,4}, the orbit of {1,3} contains both {2,3} and {2,4}. By D2 one of
    two things is true, and a transported witness decides which: either
    the survivors are REGION ARTIFACTS (the constructed attacks never
    offered the transported witness states, and the survivors part the
    moment they are), or equivariance fails at the engine, which would be
    a class-sensitive hole in the faithfulness result itself.

 D4 THE TELLTALE MECHANISM, the invariant candidate. At a principal swap
    the two states differ only in which of the pair's items carries which
    exponent. Context vehicles are unchanged: a rider is a function of its
    core's colour and door alone, covering reads the degree multiset
    (unchanged -- the pair shares one degree), and the tick reads degrees
    and exponents as a multiset (unchanged). Costs never separate the
    pair: m(-n*a) = m(-n*b) for every n, by D1. What CAN separate is
    rider COMPOSITION: the pair's own cores at door n summon
    minrep(-n*a) against minrep(-n*b) = f(minrep(-n*a)), and the two
    project equally through the merge iff they differ only inside the
    merge itself. Call a door n TELLTALE for the pair if the two riders'
    colour multisets, with both merged colours relabelled alike, differ.
    Then the merged menus at a principal swap should differ exactly when
    the cheapest tier prices a pair core at a telltale door -- and a
    pair-merge is menu-invisible in a region exactly when no state of the
    region does so. The telltale set is computed from the supply matrix
    alone, so the invariant lives at the class-group level; whether a
    telltale door is ever PRICED ONTO a cheapest tier is the dynamics'
    half, decided by the same matrix through the walker.

 D5 WHAT THE MECHANISM PREDICTS OF THE TABLE, derivable by hand where
    minreps are single degree-1 items (the four elliptic rings, m = 1 on
    every nonzero class). Three-class curve: both surviving pairs have
    classes {1,2} = {c,-c} with every -n*c landing inside the merge, so
    NO telltale door exists -- absolute survivors, certified by the
    matrix with no region in the statement. Four-class curve: the same
    class pair {2,3} has no telltale door at degree 1 (the riders land
    inside the merge or on the self-inverse class, which f fixes), but at
    degrees 2 and 4 the SAME rider difference falls outside the merge and
    n = 1 is telltale at cost 3 -- parting cheap, which is what was
    measured. Five-class curve, degree 1: every pair has a telltale door
    at cost 2 or 3 (some -n*a lands outside the merge with -n*b its
    distinct conjugate), so ALL SIX should part -- three were measured
    invisible, which is exactly D3's tension. Five-class curve, degree 5:
    n = 1 is telltale (the riders are degree-1 items of distinct classes,
    outside the merge) at cost 5*1 + 1 = 6, and a degree-5 core with a
    tick against it should never make a cheapest tier in the walked
    region -- invisible by PRICING, not by certificate. The genus-2
    ring's two survivors: UNKNOWN at the freeze, the table prints.

TRANSPLANT FLAGS, fixed at the freeze.
 T1 From the walked region to the verdicts. A conviction is absolute (a
    witness is a witness), but "invisible" stays region-scoped: this rig
    can only ever say no state of ITS region parts the pair.
 T2 From the six function fields to the number rings: nothing is carried;
    the scope is the six rings the colouring claim was minted on.
 T3 The pricing threshold read beside the table (the largest cheapest-tier
    cost over the region's principal tree states) is a PROXY observable
    for "what a cheapest tier can cost here", frozen as a column to read,
    never a premise of the mechanism claim.

PREDICTIONS, frozen before the engine runs.
 P1 (positive control) Identity transport: every stored menu witness,
    re-evaluated through the identity automorphism, fires again.
 P2 (equivariance, measured at the engine) Every stored menu witness,
    transported through every supply-preserving automorphism, is a menu
    witness for the image pair; and the abstract walker agrees with the
    engine at every transported state, 0 parting.
 P3 (the convictions) Exactly the three degree-1 survivors of the
    five-class curve are convicted by transported witnesses; the final
    verdict is constant on every supply-preserving orbit of pairs; the
    inventory lands at 11 invisible and 14 parting.
 P4 (the mechanism) At every principal swap over an aut-conjugate pair in
    the instrumented region, the merged engine menus differ IFF the
    cheapest tier prices a pair core at a telltale door (read off the
    abstract walker's own tie records). 0 exceptions, both directions.
    [As frozen, "prices" was read off the tie records' named cores, and
    the run refuted that READ at four swaps of one genus-2 pair: two
    cores can offer the SAME increment multiset -- each core's rider
    exactly the other's increment -- and the menu records the shared
    vehicle once, under one name, so a pair core on the tier can wear a
    context core's label. The mechanism's claim is untouched; the
    predicate now reads offers at the colour level -- an (X, n) offer is
    on the tier iff its cost equals the tier's -- which is dedup-blind
    and needs no item identities. Left standing because the design is
    the record of what was frozen.]
 P5 (the table) The telltale set is EMPTY at the three-class curve's two
    survivors and the four-class curve's degree-1 survivor -- absolute,
    region-free invisibility -- and nonempty with cheap least cost at
    every pair that parts. The five-class curve's degree-5 pairs are
    invisible with a nonempty telltale set priced above the region's
    tiers. The genus-2 survivors: UNKNOWN which of the two shapes they
    take; the table prints and the count is the finding.

 P6 (the pricing hunt; designed after the table above printed, its
    trigger the nine survivors whose telltale cost sits at or under the
    region ceiling -- the proxy's per-region maximum mixes doors from
    different states, so a per-state adversarial search is owed before
    any survivor is called robust). For each surviving pair with a
    nonempty telltale set, states are BUILT to price a telltale door
    onto a cheapest tier while a principal swap is available: the pair's
    items seated at exponents differing by the class-difference order
    (so the swap stays principal), context colours seated beside them,
    minrep completion, and a greedy descent from each seed. Frozen
    expectation: UNKNOWN in general; for the five-class curve's
    degree-5 family a hand-derivation says no state can do it -- a
    degree-5 core prices its door-1 telltale (cost 6) only when seated
    at an exponent at or above the tick, which the tick's own doubling
    caps at 2, and a tick of 2 caps every degree-1 offer at cost 4 --
    so the shield should hold there; the observable prints either way.

KILL-SHAPES, named as observables.
  - A transported witness whose merged engine menus AGREE prints ring,
    pair, automorphism and state: equivariance fails at the engine, and
    the finding is a class-sensitive hole in faithfulness, not an
    invariant.
  - A mechanism exception prints the swap, both merged menus, and the
    tie/telltale detail, in either direction.
  - A final verdict not constant on an orbit prints the orbit.
  - If the telltale classification and the verdicts disagree anywhere
    beyond P5's frozen unknowns, the honest output is the table itself.

FINDINGS (tiers below; run record at the bottom).

F1 MENUS TRANSPORT ALONG EVERY SUPPLY-PRESERVING AUTOMORPHISM -- the
   equivariance property (D1), proved for the abstract dynamics from the
   construction, holds at the ENGINE wherever it was put: all 126 stored
   menu witnesses transported through all preserved automorphisms fired
   for their image pairs, 376 transports in all (6, 10, 26, 54, 144, 136
   per ring, 0 agreeing),
   with the abstract walker matching the engine at every transported
   state (12 + 20 + 52 + 108 + 288 + 272, 0 parting). P1 and P2 in full.

F2 THE OLD SURVIVOR SET WAS A REGION ARTIFACT ON ITS MIXED ORBITS --
   P3 exactly. Transport convicts the five-class curve's three degree-1
   survivors ((1,1)~(1,2) by (1,3)~(1,4) transported; (1,1)~(1,3) and
   (1,1)~(1,4) by (1,2)~(1,3)), after which every preserved-Aut orbit of
   pairs is verdict-constant, as D2 requires.

F3 THE MECHANISM (rule in range; six rings, 181 principal swaps over the
   25 aut-conjugate pairs at the tree plus every stored and transported
   witness state, 68 parting, 0 exceptions either direction; every hunt
   witness of F4 re-explained): at a principal swap the merged menus
   differ IFF the cheapest tier prices a pair core at a TELLTALE door --
   a door n where minrep(-n*a) and minrep(-n*b) differ outside the merge
   as colour multisets. The frozen read of "prices" (the tie records'
   named cores) was refuted at four swaps of one genus-2 pair by vehicle
   coincidence -- two cores each summoning exactly the other's increment
   offer ONE vehicle, recorded under one name -- and the colour-level
   read (an (X, n) offer is on the tier iff its cost equals the tier's)
   closed all four.

F4 EVERY SURVIVOR WITH A TELLTALE DOOR FALLS TO THE PRICING HUNT -- P6's
   unknown resolved the strong way, against the frozen shield sketch.
   States built to price a telltale door onto a cheapest tier with a
   principal swap in hand convict all nine: the three-class curve's
   degree-3 pair, the five-class curve's whole degree-5 layer, and the
   genus-2 ring's degree-2 and degree-4 inverse pairs. The shield sketch
   failed because it modelled the tick's 2-part as doubling per exponent;
   it doubles per exponent-CEILING (a degree-5 item at exponent 8 sits
   exactly at tick 8, prices its door-1 telltale at cost 6, and the
   unseated degree-1 opens cost 10 beside it). Region-scoped survival is
   fragile twice over in one rig.

F5 THE LAW (rule in range; six rings, asserted at every same-degree pair
   of active colours, and over the aut-conjugate 25 in both directions):
   A PAIR-MERGE IS MENU-INVISIBLE IFF NO DOOR IS TELLTALE -- iff the two
   colours' summoned riders agree outside the merge at every door. Only
   two pairs in the whole corpus satisfy it, the degree-1 inverse pairs
   of the three- and four-class curves, and their invisibility is
   ABSOLUTE: certified by the supply matrix with no region in the
   statement, since no state can price a door that does not exist. The
   final inventory is 2 invisible and 23 parting of the 25 aut-conjugate
   pairs. Aut-conjugacy is subsumed rather than refined: at a same-degree
   pair an empty telltale set forces the cost columns to agree (a rider
   difference in total degree is visible through the merge), so the pair
   sits in one price fibre, and the price fibres ARE the preserved-Aut
   orbits -- the necessary condition the old inventory measured was the
   telltale criterion's shadow.

WHAT THIS RIG DOES NOT CLAIM. The law is verified at the six rings'
active colours; "invisible" quantifies over the states this rig and its
parent could reach or build, made absolute only where the telltale set is
empty. The number rings carry the ladder column and are untouched (T2).

RUN RECORD. One process, CPython, no BLAS. Wall 1.5 s, peak working set
21.3 MB (memwatch) against the 512 MB ceiling. 736 checks here, plus the rebuilt
region's own (the imported machinery re-runs its tree walk, pair sweep
and constructed stage).
"""

import os

os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")

import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import explore_class_schedule as CS
import explore_coarse_type as CT
import explore_coarsest_colouring as CC
from explore_greedy_image_ec import v2

CHECKS = 0
NWIN = 32          # telltale window: doors 1..NWIN scanned for the table


def ok(cond, msg):
    global CHECKS
    assert cond, msg
    CHECKS += 1


def section(t):
    print("\n" + "=" * 72)
    print(t)
    print("=" * 72)


# ---------------------------------------------------------------- telltale
def rider_proj(sup, mk, x):
    """The colour multiset of minrep(x), both merged colours relabelled
    alike. Uniqueness holds at all six rings, so reps[x][0] is THE rep."""
    out = {}
    for (d, c, _i), e in sup.reps[x][0].items():
        col = (d, c)
        key = "M" if col in mk else col
        out[key] = out.get(key, 0) + e
    return tuple(sorted((str(k), v) for k, v in out.items()))


def telltale(sup, A, B, n):
    """Is door n telltale for the pair {A, B}? The two riders' merged
    colour multisets differ."""
    mk = frozenset((A, B))
    xa = sup.neg(sup.mul(n, A[1]))
    xb = sup.neg(sup.mul(n, B[1]))
    return rider_proj(sup, mk, xa) != rider_proj(sup, mk, xb)


def telltale_table(sup, A, B):
    """(least telltale door, its cost) over the window, or (None, None)."""
    for n in range(1, NWIN + 1):
        if telltale(sup, A, B, n):
            return n, CS.cost(sup, A[0], A[1], n)
    return None, None


# ---------------------------------------------------------------- transport
def transport_state(places, item_of, f, st):
    out = {}
    for pl, e in st.items():
        if e:
            d, c, i = item_of[pl]
            out[places[(d, f[c], i)]] = e
    return out


def probe_menu(L, sup, item_of, st):
    """The abstract walker's menu at an engine state, tick handed over."""
    probe = CS.CWalk(sup)
    probe.st = dict((item_of[pl], e) for pl, e in st.items() if e)
    probe.T = 1 << v2(L.R.lam_state(st))
    return probe.menu()


def probe_matches_engine(L, sup, places, item_of, st, c0, t0):
    ca, ta = probe_menu(L, sup, item_of, st)
    return (ca == c0 and
            sorted(tuple(sorted(CS.to_place(v, places).items()))
                   for v, _c, _n in ta)
            == sorted(tuple(sorted(v.items())) for v in t0))


def merged_diff(L, ctx, mk, st0, st1):
    """Do the engine menus at st0, st1 differ through the merge mk?"""
    col_of, menus = ctx[2], ctx[5]
    c0, t0 = CC.engine_menu(L, menus, st0)
    c1, t1 = CC.engine_menu(L, menus, st1)
    return (CC.proj_menu(col_of, c0, t0, mk)
            != CC.proj_menu(col_of, c1, t1, mk))


def tier_prices_telltale(L, ctx, mk, st, cache):
    """Does the cheapest tier at st price a pair core at a telltale door?
    Read at the COLOUR level: an (X, n) offer is on the tier iff its cost
    equals the tier's -- dedup-blind, since two cores can offer one
    increment multiset and the menu then records it under one name. The
    probe (for the tick, covering and the tier cost) is cached per
    state."""
    sup, item_of, pls_of = ctx[0], ctx[3], ctx[4]
    A, B = sorted(mk)
    key = tuple(sorted((pl, e) for pl, e in st.items() if e))
    if key not in cache:
        probe = CS.CWalk(sup)
        probe.st = dict((item_of[pl], e) for pl, e in st.items() if e)
        probe.T = 1 << v2(L.R.lam_state(st))
        cache[key] = (probe, probe.menu()[0])
    probe, best = cache[key]
    for X in (A, B):
        exps = set(st.get(pl, 0) for pl in pls_of.get(X, ()))
        for e in exps:
            r0 = probe.door(X[0], e)
            for j in (0, 1, 2):
                n = r0 + j
                if (CS.cost(sup, X[0], X[1], n) == best
                        and telltale(sup, A, B, n)):
                    return True
    return False


# ------------------------------------------------------------- the sweeps
def swap_states(ctx, mk, st0):
    """Every principal swap the state offers the pair: one representative
    item per (colour, exponent) as in the pair sweep, distinct exponents
    exchanged, principality kept."""
    sup, col_of = ctx[0], ctx[2]
    pls_of = ctx[4]
    A, B = sorted(mk)
    reps = {}
    for col in (A, B):
        bye = {}
        for pl in pls_of.get(col, ()):
            e = st0.get(pl, 0)
            if e not in bye:
                bye[e] = pl
        reps[col] = bye
    out = []
    for eA, px in sorted(reps[A].items()):
        for eB, py in sorted(reps[B].items()):
            if eA == eB:
                continue
            st1 = dict(st0)
            st1[px] = eB
            st1[py] = eA
            st1 = dict((pl, e) for pl, e in st1.items() if e)
            if CC.class_sum(sup, col_of, st1) == 0:
                out.append(st1)
    return out


def main():
    ladders = CT.build_ladder()
    world = []
    section("S0  THE REGION REBUILT -- tree, pair sweep, constructed states")
    print("the pair records of explore_coarsest_colouring.py regenerated,")
    print("witness states in hand; counts as measured there\n")
    for L in ladders:
        ctx = CC.walk_tree(L)
        offtree = [0, []]
        pairs = CC.sweep_ring(L, ctx, offtree)
        CC.constructed_stage(L, ctx, offtree, pairs)
        sup = ctx[0]
        aut = [f for f in CC.preserved_autos(sup)]
        conj = sorted(mk for mk in pairs
                      if CC.aut_conjugate(sup, *sorted(mk)))
        k2n = sum(1 for mk in pairs if pairs[mk]["k2"])
        print("%-8s %3d pairs, %2d aut-conjugate, %2d with a menu witness,"
              " |preserved Aut| %d"
              % (L.name, len(pairs), len(conj), k2n, len(aut)))
        ok(offtree[1] == [], "%s: the walker parted from the engine in the"
           " rebuilt region" % L.name)
        world.append((L, ctx, pairs, aut, conj))

    # ---------------------------------------------------------------- S1
    section("S1  TRANSPORT -- every stored witness through every "
            "supply-preserving automorphism")
    print("P1: the identity re-fires every witness. P2: every transported")
    print("witness fires for the image pair, and the abstract walker")
    print("agrees with the engine at every transported state.\n")
    convicted = {}                # (ring, mk) -> (via mk, f)
    for L, ctx, pairs, aut, conj in world:
        sup, places, col_of, item_of = ctx[0], ctx[1], ctx[2], ctx[3]
        fired = agreed = faith = 0
        for mk in sorted(pairs, key=sorted):
            rec = pairs[mk]
            if not rec["k2"]:
                continue
            key0, key1, _r = rec["k2"]
            st0, st1 = dict(key0), dict(key1)
            A, B = sorted(mk)
            for f in aut:
                u0 = transport_state(places, item_of, f, st0)
                u1 = transport_state(places, item_of, f, st1)
                mkU = frozenset(((A[0], f[A[1]]), (B[0], f[B[1]])))
                ok(CC.class_sum(sup, col_of, u0) == 0
                   and CC.class_sum(sup, col_of, u1) == 0,
                   "%s: a transported state is not principal" % L.name)
                for st in (u0, u1):
                    c0, t0 = CC.engine_menu(L, ctx[5], st)
                    if probe_matches_engine(L, sup, places, item_of,
                                            st, c0, t0):
                        faith += 1
                    else:
                        print("    FAITHFULNESS PARTS at %s %s" %
                              (L.name, sorted(st.items())))
                diff = merged_diff(L, ctx, mkU, u0, u1)
                ident = all(f[c] == c for c in range(sup.h))
                if ident:
                    ok(diff, "%s: P1 -- the identity transport of %s ~ %s"
                       " does not fire" % (L.name, A, B))
                if diff:
                    fired += 1
                    if len(mkU) == 2 and mkU in pairs \
                            and not pairs[mkU]["k2"] \
                            and (L.name, mkU) not in convicted:
                        convicted[(L.name, mkU)] = (mk, dict(f))
                        pairs[mkU]["k2"] = (
                            tuple(sorted(u0.items())),
                            tuple(sorted(u1.items())), "transported")
                else:
                    agreed += 1
                    print("    EQUIVARIANCE FAILS at %s: %s ~ %s through"
                          " %s" % (L.name, A, B, sorted(f.items())))
        print("%-8s transported witnesses fired %4d, agreed %d,"
              " faithful states %4d" % (L.name, fired, agreed, faith))
        ok(agreed == 0,
           "%s: a transported witness did not fire -- equivariance has a"
           " hole at the engine" % L.name)
    print("\nconvictions by transport:")
    if not convicted:
        print("    none")
    for (name, mkU), (src, f) in sorted(convicted.items(),
                                        key=lambda kv: (kv[0][0],
                                                        sorted(kv[0][1]))):
        A, B = sorted(mkU)
        sA, sB = sorted(src)
        print("    %-8s %s ~ %s  convicted by %s ~ %s transported"
              % (name, A, B, sA, sB))

    # ---------------------------------------------------------------- S2
    section("S2  THE MECHANISM -- merged menus part IFF a cheapest tier "
            "prices a pair core at a telltale door")
    print("every principal swap over every aut-conjugate pair, at the tree")
    print("states plus every stored and transported witness state; the")
    print("telltale read is the supply matrix's, the tier the walker's\n")
    for L, ctx, pairs, aut, conj in world:
        sup, places, col_of, item_of = ctx[0], ctx[1], ctx[2], ctx[3]
        states = [dict(s) for s in ctx[6]]
        seenk = set(tuple(sorted((pl, e) for pl, e in s.items() if e))
                    for s in states)
        for mk in sorted(pairs, key=sorted):
            rec = pairs[mk]
            if rec["k2"]:
                for key in (rec["k2"][0], rec["k2"][1]):
                    if key not in seenk:
                        seenk.add(key)
                        states.append(dict(key))
        swaps = parts = 0
        exc = []
        pcache = {}
        for st0 in states:
            if CC.class_sum(sup, col_of, st0) != 0:
                continue
            for mk in conj:
                sws = swap_states(ctx, mk, st0)
                if not sws:
                    continue
                told = tier_prices_telltale(L, ctx, mk, st0, pcache)
                for st1 in sws:
                    swaps += 1
                    diff = merged_diff(L, ctx, mk, st0, st1)
                    if diff:
                        parts += 1
                    if diff != told:
                        exc.append((mk, st0, st1, diff, told))
        print("%-8s %5d principal swaps over %2d aut-conjugate pairs,"
              " %4d part, %d mechanism exceptions"
              % (L.name, swaps, len(conj), parts, len(exc)))
        for mk, st0, st1, diff, told in exc[:4]:
            A, B = sorted(mk)
            print("    EXCEPTION %s ~ %s: menus %s, telltale tier %s at %s"
                  % (A, B, "part" if diff else "agree",
                     "yes" if told else "no", sorted(st0.items())))
        ok(not exc, "%s: the mechanism has exceptions" % L.name)

    # ---------------------------------------------------------------- S3
    section("S3  THE INVENTORY RE-SORTED, and orbit constancy")
    print("verdicts after transport; the supply-preserving orbit of every")
    print("pair must be verdict-constant (the equivariance theorem)\n")
    tot_inv = tot_part = 0
    for L, ctx, pairs, aut, conj in world:
        sup = ctx[0]
        inv = [mk for mk in conj if not pairs[mk]["k2"]]
        prt = [mk for mk in conj if pairs[mk]["k2"]]
        tot_inv += len(inv)
        tot_part += len(prt)
        for mk in conj:
            A, B = sorted(mk)
            for f in aut:
                mkU = frozenset(((A[0], f[A[1]]), (B[0], f[B[1]])))
                if len(mkU) != 2 or mkU not in pairs:
                    continue
                ok((pairs[mk]["k2"] is None)
                   == (pairs[mkU]["k2"] is None),
                   "%s: verdict not orbit-constant at %s ~ %s" %
                   (L.name, A, B))
        print("%-8s invisible %s" % (L.name, [tuple(sorted(m))
                                              for m in sorted(inv,
                                                              key=sorted)]))
        print("         parting   %s" % [tuple(sorted(m))
                                         for m in sorted(prt, key=sorted)])
    print("\nfinal count: %d menu-invisible, %d parting, of %d"
          " aut-conjugate pairs" % (tot_inv, tot_part, tot_inv + tot_part))

    # ---------------------------------------------------------------- S4
    section("S4  THE TABLE -- the telltale set against the verdicts")
    print("least telltale door and its cost per pair; beside them the")
    print("region's price ceiling (the largest cheapest-tier cost over the")
    print("principal tree states), the pricing proxy the design froze\n")
    print("%-8s %-22s %-10s %8s %8s %8s  %s"
          % ("ring", "pair", "verdict", "door", "cost", "ceiling", "shape"))
    absolute = priced = anomalies = 0
    for L, ctx, pairs, aut, conj in world:
        sup, col_of, menus = ctx[0], ctx[2], ctx[5]
        ceil = 0
        for s in ctx[6]:
            key = tuple(sorted((pl, e) for pl, e in s.items() if e))
            if CC.class_sum(sup, col_of, s) == 0 and key in menus:
                ceil = max(ceil, menus[key][0])
        for mk in conj:
            A, B = sorted(mk)
            invis = pairs[mk]["k2"] is None
            n, kappa = telltale_table(sup, A, B)
            if invis and n is None:
                shape = "ABSOLUTE: no telltale door exists"
                absolute += 1
            elif invis:
                shape = ("priced out" if kappa > ceil
                         else "PRICED IN YET INVISIBLE -- anomaly")
                priced += 1 if kappa > ceil else 0
                anomalies += 0 if kappa > ceil else 1
            else:
                shape = ("telltale within the ceiling" if kappa is not None
                         and kappa <= ceil else
                         "PARTS ABOVE THE CEILING -- proxy too coarse")
                anomalies += (0 if kappa is not None and kappa <= ceil
                              else 1)
            print("%-8s %-22s %-10s %8s %8s %8d  %s"
                  % (L.name, "%s ~ %s" % (A, B),
                     "invisible" if invis else "parts",
                     "-" if n is None else n,
                     "-" if kappa is None else kappa, ceil, shape))
    print("\nabsolute survivors %d, priced-out survivors %d, anomalies %d"
          % (absolute, priced, anomalies))

    # ---------------------------------------------------------------- S5
    section("S5  THE PRICING HUNT -- states built to price a telltale "
            "door onto a tier, swap in hand")
    print("for every survivor with a nonempty telltale set: pair items")
    print("seated with the swap kept principal, context beside them,")
    print("minrep completion, greedy descent; every principal swap of")
    print("every built state is put to the engine\n")
    for L, ctx, pairs, aut, conj in world:
        sup, places, col_of, item_of = ctx[0], ctx[1], ctx[2], ctx[3]
        pls_of, menus = ctx[4], ctx[5]
        for mk in conj:
            if pairs[mk]["k2"]:
                continue
            A, B = sorted(mk)
            n1, _k = telltale_table(sup, A, B)
            if n1 is None:
                print("%-8s %s ~ %s  ABSOLUTE -- no telltale door, not"
                      " hunted" % (L.name, A, B))
                continue
            n0 = CC.ordc(sup, sup.add(B[1], sup.neg(A[1])))
            built = tested = 0
            hit = None
            ctxcols = [None] + [C for C in sorted(ctx[7])
                                if C not in (A, B)]
            for eA in range(1, 6):
                for eB in sorted(set((max(0, eA - n0), eA + n0))):
                    if eA == eB or hit:
                        continue
                    for C in ctxcols:
                        if hit:
                            break
                        kk = ((0,) if C is None
                              else (1, 2, CC.ordc(sup, C[1])))
                        for k in kk:
                            st = {}
                            plA = places[(A[0], A[1], 0)]
                            plB = places[(B[0], B[1], 0)]
                            if eA:
                                st[plA] = eA
                            if eB:
                                st[plB] = eB
                            tot = sup.add(sup.mul(eA, A[1]),
                                          sup.mul(eB, B[1]))
                            if C is not None and k:
                                plC = places[(C[0], C[1], 0)]
                                st[plC] = st.get(plC, 0) + k
                                tot = sup.add(tot, sup.mul(k, C[1]))
                            for it, e in sup.reps[sup.neg(tot)][0].items():
                                p2 = places[it]
                                st[p2] = st.get(p2, 0) + e
                            cur = st
                            for _step in range(4):
                                if CC.class_sum(sup, col_of, cur) != 0:
                                    break
                                built += 1
                                for st1 in swap_states(ctx, mk, cur):
                                    tested += 1
                                    if merged_diff(L, ctx, mk, cur, st1):
                                        hit = (cur, st1)
                                        break
                                if hit:
                                    break
                                _c0, t0 = CC.engine_menu(L, menus, cur)
                                cur = dict(cur)
                                for p2, e in t0[0].items():
                                    cur[p2] = cur.get(p2, 0) + e
            if hit:
                print("%-8s %s ~ %s  CONVICTED by the hunt at %s"
                      % (L.name, A, B, sorted(hit[0].items())))
                ok(tier_prices_telltale(L, ctx, mk, hit[0], {}),
                   "%s: a hunt witness the mechanism does not explain"
                   % L.name)
                pairs[mk]["k2"] = (
                    tuple(sorted(hit[0].items())),
                    tuple(sorted(hit[1].items())), "hunted")
            else:
                print("%-8s %s ~ %s  holds: %d built states, %d principal"
                      " swaps, all agreeing" % (L.name, A, B, built,
                                                tested))

    # ---------------------------------------------------------------- S6
    section("S6  THE LAW -- menu-invisible IFF no telltale door")
    print("the inventory after the hunt; orbit constancy re-asserted; the")
    print("telltale criterion asserted over every same-degree pair\n")
    fin_inv = fin_prt = 0
    for L, ctx, pairs, aut, conj in world:
        sup = ctx[0]
        inv = [mk for mk in conj if not pairs[mk]["k2"]]
        fin_inv += len(inv)
        fin_prt += len(conj) - len(inv)
        for mk in conj:
            A, B = sorted(mk)
            for f in aut:
                mkU = frozenset(((A[0], f[A[1]]), (B[0], f[B[1]])))
                if len(mkU) == 2 and mkU in pairs:
                    ok((pairs[mk]["k2"] is None)
                       == (pairs[mkU]["k2"] is None),
                       "%s: final verdict not orbit-constant at %s ~ %s"
                       % (L.name, A, B))
        for mk in sorted(pairs, key=sorted):
            A, B = sorted(mk)
            if A[0] != B[0]:
                continue
            n1, _k = telltale_table(sup, A, B)
            ok((pairs[mk]["k2"] is None) == (n1 is None),
               "%s: the law fails at %s ~ %s -- verdict %s, telltale %s"
               % (L.name, A, B,
                  "invisible" if pairs[mk]["k2"] is None else "parts",
                  "empty" if n1 is None else "door %d" % n1))
        if inv:
            print("%-8s invisible: %s" % (L.name,
                                          [tuple(sorted(m))
                                           for m in sorted(inv,
                                                           key=sorted)]))
    print("\nTHE LAW HOLDS over every same-degree pair of active colours")
    print("at the six rings: a pair-merge is menu-invisible iff NO door is")
    print("telltale -- iff the two colours' summoned riders agree outside")
    print("the merge at every door. Final count: %d invisible, %d parting"
          " aut-conjugate pairs." % (fin_inv, fin_prt))

    print("\n%d checks passed here, plus the rebuilt region's own." % CHECKS)


if __name__ == "__main__":
    main()
