"""THE LADDER-ENTRY LEMMA: what a chain-preferring run must already
know before a door on the ladder can open.

THE QUESTION
------------
explore_near_side.py closed the shape question and left ONE pinned
configuration: the elder chained to a straddle S_q(w) while the
flank run stands in a cell that still holds L_q, the straddle's
near ladder point, strictly interior. The census says that bucket
is empty under the identity map and the maps fill it, and the owe
is a derivation. This rig asks the question one level under the
shape: not "which refusal blocks the flank" but "how did the flank
get onto the ladder BELOW the elder at all" — every cell that
holds L_q interior sits inside the near child (l, w), and the only
way in is a DOOR. So the object is the door, and the question is
what the identity map forces to be true at the moment one opens.

THE NAMED CLASS (imported verbatim)
-----------------------------------
Cover, streams, maps, cells, references and the commit loop are the
parents' (explore_scale_clock.py, explore_seed_exclusion.py,
explore_chain_persistence.py). The readers are the chain-preferring
slice (st, ss) = (1, 0). This rig walks SINGLE runs rather than
pairs: every claim below is about one run's own descent, and the
pair statement follows because both runs share the chain
reference. The run axis is therefore (P, pc) directly — tree
patience P in {0, 1, 2, 3, INF} against chain patience pc in the
same set, 25 runs, which covers every run the census's twenty
chain-preferring pairs contain (a pair contributes patiences pt and
pt - 1 against a shared pc).

NOTATION. (l, r) a tree cell, w = l (+) r its vertex, x the stream
point, x in (l, w). L_j = l + j w the near ladder, R_j = r + j w
the away ladder, S_k(w) = (L_k, R_k). conv_i the convergents of x
and a_i its partial quotients. c the chain reference, T the run's
tree reference; index(.) is the step index of the cylinder, so a
LARGER index is a FINER reference.

HAND-ATTACK (fixed before the engine; the derivation this rig
checks)
------------------------------------------------------------
G1 THE VERTEX OF AN OCCUPIED STRADDLE IS A CONVERGENT. A run's
   cell always contains x, so a run standing at S_k(w) with
   k >= 1 has x in (L_k, w) and hence in (L_1, w): the ladder at w
   is entered. It never is at a strict semiconvergent. Write
   w = M_b = conv_{sigma-2} + b conv_{sigma-1} with 1 <= b < a_sigma;
   its tree cell is (conv_{sigma-1}, M_{b-1}) and the mediant of
   the near child (conv_{sigma-1}, M_b) is M_{b+1}, so L_1 = M_{b+1}
   and the descent continues into (l, L_1), the side AWAY from w,
   because b + 1 <= a_sigma. So x is not in (L_1, w) and the ladder
   is never entered. At w = conv_sigma the same step turns the
   other way: L_1 = conv_sigma (+) conv_{sigma-1}, x lies in
   C_sigma = (L_1, w), and the ladder runs exactly a_{sigma+1}
   rungs, since C_{sigma+1} = (L_a, L_{a+1}) with a = a_{sigma+1}.
   So every occupied straddle vertex is a convergent and every
   occupied index is at most a_{sigma+1}.
G2 THE PLACEMENT LEMMA. Under the identity map the cylinders
   strictly inside (L_j, w), any j >= 0, are exactly those of index
   at least sigma + 1. C_sigma = (L_1, w) shares the endpoint w
   with every (L_j, w) and so is never strict; every coarser
   cylinder holds w interior or more; C_{sigma+1} = (L_a, L_{a+1})
   is strictly inside whenever j < a, and every finer cylinder sits
   inside it. Moreover C_{sigma+2} and finer have their near
   endpoint STRICTLY past L_a: a cylinder shares its parent's
   endpoint only at a partial quotient 1 and only the FAR one,
   which for C_{sigma+1} is L_{a+1}.
G3 THE MAXED-LADDER LEMMA. If c is a cylinder of index at least
   sigma + 2 then kmax at w is exactly a = a_{sigma+1}: by G2
   c sits in (L_a, L_{a+1}] with its near end strictly past L_a, so
   L_a < c.lo <= L_{a+1}, while every R_k exceeds w and so exceeds
   c.hi. The ladder is maxed the moment the chain reference is that
   fine, and it can never grow further.
G4 THE LADDER-ENTRY LEMMA (identity map, stale regime pc <= P - 1).
   A door out of a cell of the w family — from (l, r) into (l, w),
   or out of S_k(w) into (L_k, w) — requires the run's tree
   reference T strictly inside the child, hence by G2
   index(T) >= sigma + 1. The stale regime makes the chain
   reference at least one step finer, index(c) >= index(T) + 1
   >= sigma + 2, so by G3 kmax at w is already a. Therefore
   (i) the door from (l, r) into (l, w) is NEVER taken: a
   chain-preferring run at a tree cell with a live candidate
   chains, and a >= 1; and (ii) a door out of S_k(w) is taken only
   at k = a: at k < a the run first deepens to S_a(w), the
   straddle move being preferred there too. Both runs read the same
   c, so both compute the same a: the elder cannot chain to an
   index the flank has already left below, and every cell the flank
   holds inside (l, w) is inside (L_a, w). The lagging bucket is
   empty.
G5 WHAT THE MAP BREAKS. G2 and G3 are the identity map's private
   property — they are statements about CYLINDERS. (Superseded in
   part by explore_reference_families.py, which sorts reference
   FAMILIES rather than maps: G2 holds at every determinant-1
   reference, cylinder or not, and G3 fails nowhere at all, in any
   family. Neither is private to cylinders. What IS private is the
   step G4 takes from them, below.) Under sq and dbl
   a reference is the image of a cylinder, the determinant is no
   longer +-1, and a reference fine enough to open a door on the
   ladder need not have maxed the ladder. The map-neutral form of
   G4 is an INVARIANT of the exit: once a run doors out of the w
   family at index k, kmax at w never afterwards exceeds k. That
   invariant, not the refusal shape, is what the crossings violate.

PREDICTIONS, fixed before the engine ran
----------------------------------------
S1 [gate, positive control] The three sq stall specimens under sq
   each show the exit-index invariant VIOLATED at some
   chain-preferring run: a door out of a w family at index k
   followed by kmax at w rising above k. A rig that cannot see the
   violation the maps are known to produce proves nothing about the
   identity map (K1).
S2 [G1] Over the identity scans every straddle a run occupies has a
   vertex equal to a convergent of the stream point, and an index
   at most the next partial quotient. Zero exceptions (K2).
S3 [G2] Every door taken out of a w family under the identity map
   carries a tree reference of index at least sigma + 1, where
   w = conv_sigma. Zero exceptions (K3). Doors at NON-convergent
   vertices are tallied separately and are expected to be the bulk:
   they are how the run crosses a run of partial quotients.
S4 [G3] At every chain move under the identity map whose chain
   reference has index at least sigma + 2, the index taken equals
   a_{sigma+1}. Zero exceptions (K4).
S5 [G4, the consequence] Under the identity map, in the stale
   regime, ZERO doors from a tree cell into EITHER child of a
   CONVERGENT vertex, and every door out of a straddle at a
   convergent vertex taken at index k = a_{sigma+1}. And the
   map-neutral form: zero exit-index violations.
S6 [non-vacuity] In the FRESH regime (pc >= P) the identity map DOES
   show both of the moves S5 forbids in the stale regime. If it
   does not, the regime split is decorative and G4 proves less than
   it appears to — the interesting outcome, and a finding either
   way.
S7 [the map contrast] Under sq and dbl the exit-index invariant is
   violated in the STALE regime, and the violations are where the
   crossings are. GUESS on the split: sq and dbl both violate.

KILL CRITERIA (observables, meaning weighed after the run)
----------------------------------------------------------
K1 An S1 control miss: the exit-index instrument does not see the
   drift the maps are known to produce — no verdicts.
K2 An S2 miss: G1 dies at the printed specimen.
K3 An S3 miss: G2 dies at the printed specimen.
K4 An S4 miss: G3 dies at the printed specimen, and G4 with it.
Otherwise every tally prints as a finding; S5/S6/S7 misses scope
the derivation, not the rig.

ENGINE
------
E1 the control (S1): the three sq stall specimens under sq, every
   chain-preferring run, the exit-index invariant tested.
E2 the identity census (S2, S3, S4, S5, S6): exhaustive digit
   products {1,2,3,40}^6, {1,2,4,9,30}^6, {1,2,3}^7 and {1,2}^10
   under the identity map over all 25 runs; every micro-decision of
   every commit loop classified — the vertex against the point's
   convergents, the door's tree-reference index against sigma, the
   chain index against the next partial quotient, and the exit
   index against every later kmax at that vertex.
E3 the map contrast (S7): the same instrument under sq and dbl over
   {1,2,3,40}^6 and {1,2,4,9,30}^6, exit-index violations tallied
   by map and regime. Its run axis, and E1's, is the twelve runs
   the parents' map pairs contain rather than the identity
   census's twenty-five — the reason is at MAP_RUNS and is itself a
   reading of the lemma.
E5 the correspondence (added by the audit of this record, which
   computed it outside the rig after noticing that H3 read identity
   of OBJECTS off equality of COUNTS; its numbers were known before
   it ran, and the leg exists so the record prints what its prose
   states — the E4b/E6 precedent this thread set, fourth firing):
   per map, the SET of (stream, run) violating the exit-index
   invariant in the stale regime against the SET of
   (stream, fresher-run) whose pair crosses.
E4 the pair control: the nesting law itself re-checked on the
   smallest identity scan at the census's twenty chain-preferring
   pairs, so the single-run instrument is anchored to the pair
   statement it is meant to explain.
Exact big-integer arithmetic for every verdict; measured run about
four minutes, the correspondence leg carrying most of it; memory
trivial; exit nonzero on any check failure.

FINDINGS (entered after the run; ALL CHECKS PASS, exit 0)
----------------------------------------------------------------
H1 THE THREE LEMMAS HOLD AT CENSUS SCOPE, EXACTLY. Over the four
   exhaustive identity scans at all twenty-five runs: every straddle
   any run occupies sits at a CONVERGENT vertex at an index within
   the next partial quotient (G1, zero exceptions); all 1,503,476
   doors taken at a convergent vertex carry a tree reference of
   index at least sigma + 1 (G2, zero exceptions); and all 292,661
   chain moves whose chain reference has index at least sigma + 2
   land on exactly a_{sigma+1} (G3, zero exceptions). These are the
   three arithmetic inputs of G4 and they are confirmations of a
   derivation, not its evidence.
H2 THE STALE REGIME IS CLOSED, AND THE SPLIT IS NOT DECORATIVE.
   Under the identity map, in the stale regime: ZERO doors from a
   tree cell into EITHER child of a convergent vertex (against
   720,498 in the fresh regime) — the tally keys the cell doored out
   of and so forbids both children, where G4 needs only the NEAR
   one, and an empty superset is the stronger statement (the child
   split is explore_reference_families.py's, which measured both
   children entered in quantity wherever such doors occur at all) —
   every one of the 177,186 straddle exits
   taken at the maxed index (against 259,612 fresh exits, EVERY one
   of them below it), and zero exit-index violations in 2,447,520
   exits (against 626,722 violations in 7,263,472 fresh ones). The
   fresh regime does all three of the things the stale regime
   cannot, so G4's hypothesis is doing the work and the regime split
   is real rather than a way of describing an empty case.
H3 THE MAP-NEUTRAL INVARIANT IS THE CROSSING, AS ONE OBJECT. E5
   settles this by SETS rather than counts, which is what the audit
   of this record asked for after the raw tallies agreed under dbl
   (1,006 violations against the predecessor's 1,006 bad pairs) and
   agreement of counts is not identity of objects. Deduplicated —
   E2's two map alphabets share the digits 1 and 2, so 64 streams
   are scanned twice and the honest figures are distinct
   (stream, run) keys — the dbl sets COINCIDE, 998 against 998,
   with nothing on either side. Under sq every one of the 2,606
   crossings has a violating flank run and 1,504 violating runs
   carry no crossing: the invariant is NECESSARY and not
   sufficient, since a run may exit low and the other run never
   chain past it. The identity map's stale regime has zero
   violations, so no crossing is available there at all.
   SCOPE, and it is not a small one: under sq and dbl the tallies
   keyed to "convergent" compare against the convergents of the
   UNMAPPED stream point, which is not the point those runs track,
   so the G1/G2/G3 columns in the map legs measure only that the
   identity map's coordinates do not describe a mapped run. The
   exit-index invariant asks nothing about convergents, and it is
   the only number the map legs carry.
H4 THE LAW IS A THEOREM (identity map, chain-preferring slice).
   Every case closes, by the FLANK's own regime rather than the
   pair's. Write P for the FRESHER run's tree patience, so the
   elder's is P + 1. If the flank is
   the FRESHER run: at pc <= P - 1 the flank is stale and G4 keeps
   its cells inside (L_a, w) = (L_q, w); at pc >= P its tree
   reference sits inside the chain reference and the predecessor's
   D5 opens its door. D5 asserts that opening without splitting the
   catalog's two partner shapes, and the audit of this record
   supplied the split, since the theorem's tier rests on it: the
   door child is bounded on the ladder side by L_q and on the far
   side by the flank cell's own outer endpoint, and T <= c gives
   BOTH — c sits strictly inside S_q(w), so T.lo >= c.lo > L_q,
   and the flank's cell strictly contains whatever reference put it
   there, which contains c, so T.hi <= c.hi is inside that outer
   endpoint. It holds at a tree cell and at a straddle alike, and
   at a straddle for the reason that looks like the exception —
   the cell was entered by a CHAIN move, so it strictly contains
   the chain reference rather than the tree one. If the flank is
   the ELDER run, whose patience is P + 1:
   at pc <= P it is ITSELF stale and G4 applies to it —
   the boundary pc = P, which is the pair's FRESH regime, is the
   elder's STALE one, and that is why the two arguments meet with no
   gap — and at pc >= P + 1 the elder's own reference is inside the
   chain reference and D5 applies. The one elder outside that
   arithmetic is the INFINITE-patience one, which holds no tree
   reference at all: it never takes a door, so its cell is the
   deepest straddle the shared chain reference allows, and it cannot
   be the flank in the first place. So the flanking role no longer
   has to be assumed: the predecessor's measured fact that the
   fresher run is the flank at every observed crossing is now a
   consequence rather than a premise, and the near-side
   endpoint-equality enumeration the whole thread was owed is not
   needed — the shape of the refusal never enters. The theorem
   imports two proved lemmas from explore_chain_persistence.py, the
   crossing catalog D1 and the fresh-regime lemma D5, and adds
   G1-G4 here.
H5 WHY THE MAP BREAKS IT, IN ONE SENTENCE. The ladder index is a
   function of the chain reference alone, and under the identity map
   a tree reference fine enough to open a door on the ladder is
   necessarily coarser than a chain reference that has already maxed
   that ladder — a statement about cylinders, hence about
   determinant +-1. (The "hence" is superseded by
   explore_reference_families.py: the statement is about cylinders
   and does NOT reduce to determinant +-1. A determinant-1 family
   out of phase with the digits — every Stern-Brocot node rather
   than the partial-quotient subsequence — keeps G1, G2 and G3 and
   breaks the lemma anyway, because G4's step silently reads one
   reference STEP as one partial quotient. The surviving scope of
   everything below is unchanged: it is all stated under the
   identity map, where the two coincide.) Under sq and dbl a
   reference is the image of a cylinder, the two finenesses
   decouple, and a run can walk off the ladder at an index the other
   run later chains past. The accidental proof of this is at
   MAP_RUNS: at P = 0 under a map the descent to contain the current
   image is a harmonic slog past the
   commit loop's runaway guard, because no chain move is coarse
   enough to collapse the run of doors — under the identity map the
   same descent is one chain move, which is G4's mechanism showing
   up as a cost rather than as a theorem.

THE VERDICT. The near-side owe is discharged without being paid.
It asked for an enumeration of the endpoint-equality branches; the
answer is that the flank never reaches the cell where such a branch
could matter, because the door that would put it there cannot open
until the chain reference has already maxed the ladder the door
leads onto. The chain-preferring nesting law under the identity map
is a theorem at the whole chain-preferring policy slice, and the
map is where it fails because the map is where a reference stops
being a Farey interval.

Run record. THREE runs. The first two took about ninety seconds
each; the third added E5 and runs about four minutes. The first found
the exit tally recording only convergent-vertex exits, which made
the map-neutral invariant invisible under the maps and failed the
S1 control — the instrument, not the slate, and the fix was to drop
the condition. The same run found the P = 0 map cost recorded at
MAP_RUNS. The second carried H1 to H5. The third is the audit's:
E5, and with it H3's rewrite from counts to sets and the split of
D5's door-opening step that H4 now carries. No prediction or
threshold was touched across any of the three, and the E1 control
gates everything after it.
"""

import sys
import itertools

import explore_scale_clock as SC
import explore_seed_exclusion as SE
import explore_chain_persistence as CP

FAILURES = []


def check(name, ok):
    tag = "PASS" if ok else "FAIL"
    print("  [%s] %s" % (tag, name))
    if not ok:
        FAILURES.append(name)


PATIENCES = (0, 1, 2, 3, None)
RUNS = [(P, pc) for P in PATIENCES for pc in PATIENCES]

ID_SCANS = [
    ((1, 2, 3, 40), 6),
    ((1, 2, 4, 9, 30), 6),
    ((1, 2, 3), 7),
    ((1, 2), 10),
]

MAP_SCANS = CP.MAP_SCANS
# The map legs run the axis the parents' map scans contain: their
# pairs are pt in {2, 3, INF} x pc in {1, 2, 3}, so P = 0 never
# appears. It cannot: at P = 0 the tree reference IS the current
# image, and under a map the descent to contain it is a harmonic
# slog past the commit loop's runaway guard, because there is no
# chain move coarse enough to collapse the run of doors. Under the
# identity map the chain DOES collapse it, which is the lemma's own
# picture — so the axis restriction is the map's cost, not a choice
# about coverage.
MAP_RUNS = [(P, pc) for P in (1, 2, 3, None) for pc in (1, 2, 3)]
PAIR_POLS = [(1, 0, pt, pc)
             for pt in (1, 2, 3, None)
             for pc in (0, 1, 2, 3, None)]


def is_stale(P, pc):
    """The regime of one RUN: the chain reference strictly finer
    than this run's own tree reference."""
    if pc is None or P is None:
        return None
    return pc <= P - 1


def cell_vertex(cell):
    if cell[0] == "T":
        return SC.mediant(cell[1], cell[2]), cell[1], cell[2], 0
    _, v, l, r, _, k = cell
    return v, l, r, k


def conv_index(cvs, v):
    for i, c in enumerate(cvs):
        if CP.eq_frac(c, v):
            return i
    return None


def refs(J, n, P, pc):
    rt = J[n - P] if P is not None and n - P >= 0 else None
    rc = J[n - pc] if pc is not None and n - pc >= 0 else None
    return rt, rc


def trace_run(J, P, pc, horizon, cvs, digs, tally, spec):
    """Walk one run, classifying every micro-decision. `tally` is a
    dict of counters; `spec` collects up to a few specimens per
    violation kind."""
    stale = is_stale(P, pc)
    reg = "stale" if stale else ("fresh" if stale is False else "none")
    C = SC.ROOT
    exits = []          # (vertex, l, r, exit_index, step)
    for n in range(horizon):
        rt, rc = refs(J, n, P, pc)
        C, records = SE.commit_step(C, rt, rc, 1, 0)
        for cell, cand_tree, cand_chain, took in records:
            v, l, r, k = cell_vertex(cell)
            sig = conv_index(cvs, v)
            at_conv = sig is not None
            a_next = (digs[sig + 1]
                      if at_conv and sig + 1 < len(digs) else None)
            if took == "chain":
                kk = cand_chain[5]
                key = ("chain", reg, "conv" if at_conv else "semi")
                tally[key] = tally.get(key, 0) + 1
                if not at_conv:
                    spec.setdefault("G1-vertex", []).append(
                        (digs, P, pc, n, v))
                elif a_next is not None and kk > a_next:
                    spec.setdefault("G1-index", []).append(
                        (digs, P, pc, n, kk, a_next))
                ci = n - pc if pc is not None else None
                if (at_conv and a_next is not None and ci is not None
                        and ci >= sig + 2):
                    tally[("G3", reg, kk == a_next)] = \
                        tally.get(("G3", reg, kk == a_next), 0) + 1
                    if kk != a_next:
                        spec.setdefault("G3", []).append(
                            (digs, P, pc, n, kk, a_next, ci, sig))
            elif took == "door":
                ti = n - P if P is not None else None
                kind = "conv" if at_conv else "semi"
                tally[("door", reg, kind, cell[0])] = \
                    tally.get(("door", reg, kind, cell[0]), 0) + 1
                if at_conv and ti is not None:
                    ok = ti >= sig + 1
                    g2 = ("G2", reg, ok)
                    tally[g2] = tally.get(g2, 0) + 1
                    if not ok:
                        spec.setdefault("G2", []).append(
                            (digs, P, pc, n, ti, sig))
                    if cell[0] == "S" and a_next is not None:
                        xk = ("exit-k", reg, k == a_next)
                        tally[xk] = tally.get(xk, 0) + 1
                # the exit invariant is map-neutral: it never asks
                # whether the vertex is a convergent, and under a map
                # it almost never is
                exits.append((v, l, r, k, n))
    # the exit-index invariant: after leaving the w family at index
    # k, kmax at w must never rise above k
    for v, l, r, k, n1 in exits:
        worst = k
        for m in range(n1 + 1, horizon):
            _, rc = refs(J, m, P, pc)
            if rc is None:
                continue
            worst = max(worst, SC.chain_kmax(v, l, r, rc))
        ok = worst <= k
        xi = ("exit-inv", reg, ok)
        tally[xi] = tally.get(xi, 0) + 1
        if not ok:
            spec.setdefault("exit-inv", []).append(
                (digs, P, pc, n1, k, worst))
    return tally


def scan(scans, mapname, label, runs=RUNS, keep_specimens=3):
    tally = {}
    spec = {}
    for alpha, h in scans:
        for digs in itertools.product(alpha, repeat=h):
            dl = list(digs)
            J = SC.images(SC.cylinders(dl), mapname)[:h]
            cvs = CP.convergents(dl)
            for P, pc in runs:
                trace_run(J, P, pc, h, cvs, dl, tally, spec)
        print("  %s: scanned %s^%d" % (label, sorted(set(alpha)), h))
    for k in sorted(spec):
        spec[k] = spec[k][:keep_specimens]
    return tally, spec


def show(tally, spec, prefix=""):
    for k in sorted(tally, key=str):
        print("    %s%-46s %d" % (prefix, str(k), tally[k]))
    for k in sorted(spec):
        for s in spec[k]:
            print("    %sSPECIMEN %-12s %s" % (prefix, k, s))


def e1_control():
    print("\nE1  THE CONTROL (sq stall specimens, exit-index)")
    hits = 0
    for name, digs in CP.SPECIMENS:
        dl = list(digs)
        h = len(dl)
        J = SC.images(SC.cylinders(dl), "sq")[:h]
        cvs = CP.convergents(dl)
        t, sp = {}, {}
        for P, pc in MAP_RUNS:
            trace_run(J, P, pc, h, cvs, dl, t, sp)
        bad = sum(v for k, v in t.items()
                  if k[0] == "exit-inv" and k[2] is False)
        print("  %-10s exit-index violations: %d" % (name, bad))
        hits += (bad > 0)
    check("S1 the exit-index invariant is violated under sq at all "
          "three specimens", hits == 3)


def e2_identity():
    print("\nE2  THE IDENTITY CENSUS")
    tally, spec = scan(ID_SCANS, "id", "id")
    show(tally, spec)
    g1 = len(spec.get("G1-vertex", [])) + len(spec.get("G1-index", []))
    check("S2 every occupied straddle sits at a convergent vertex at "
          "an index within the next partial quotient", g1 == 0)
    check("S3 every door at a convergent vertex carries a tree "
          "reference of index >= sigma + 1",
          sum(v for k, v in tally.items()
              if k[0] == "G2" and k[2] is False) == 0)
    check("S4 every chain move with a reference of index >= sigma + 2 "
          "lands on the maxed ladder index",
          sum(v for k, v in tally.items()
              if k[0] == "G3" and k[2] is False) == 0)
    check("S5a no stale-regime door from a tree cell into either "
          "child of a convergent vertex",
          tally.get(("door", "stale", "conv", "T"), 0) == 0)
    check("S5b every stale-regime door out of a straddle at a "
          "convergent vertex leaves at the maxed index",
          tally.get(("exit-k", "stale", False), 0) == 0)
    check("S5c no stale-regime exit-index violation under id",
          tally.get(("exit-inv", "stale", False), 0) == 0)
    check("S6 the fresh regime does take the moves the stale regime "
          "forbids (the split is not decorative)",
          tally.get(("door", "fresh", "conv", "T"), 0) > 0
          and tally.get(("exit-k", "fresh", False), 0) > 0)


def e3_maps():
    print("\nE3  THE MAP CONTRAST")
    for mp in ("sq", "dbl"):
        tally, spec = scan(MAP_SCANS, mp, mp, runs=MAP_RUNS)
        show(tally, spec, prefix=mp + " ")
        n = tally.get(("exit-inv", "stale", False), 0)
        check("S7 %s violates the exit-index invariant in the stale "
              "regime" % mp, n > 0)


def e5_correspondence():
    """Is the exit-index invariant the SAME object as the pair
    crossing, or two counts that happen to agree? Per map, the set
    of (stream, run) that violate it in the stale regime against the
    set of (stream, fresher-run) whose pair crosses."""
    print("\nE5  THE CORRESPONDENCE (violations against crossings)")
    for mp in ("sq", "dbl"):
        viol, cross = set(), set()
        for alpha, h in MAP_SCANS:
            for digs in itertools.product(alpha, repeat=h):
                dl = list(digs)
                J = SC.images(SC.cylinders(dl), mp)[:h]
                cvs = CP.convergents(dl)
                for P, pc in MAP_RUNS:
                    t = {}
                    trace_run(J, P, pc, h, cvs, dl, t, {})
                    if t.get(("exit-inv", "stale", False), 0):
                        viol.add((digs, P, pc))
                for pol in CP.POLS:
                    if SE.run_pair(J, pol, h)["last_bad"] is not None:
                        ptd = 3 if pol[2] is None else pol[2] - 1
                        cross.add((digs, ptd, pol[3]))
        print("  %-4s violating runs %d   crossing pairs %d   "
              "crossings with no violation %d   violations with no "
              "crossing %d"
              % (mp, len(viol), len(cross), len(cross - viol),
                 len(viol - cross)))
        check("E5 %s: every crossing's flank run violates the "
              "exit-index invariant" % mp, not (cross - viol))
        if mp == "dbl":
            check("E5 dbl: the two sets coincide exactly, so the "
                  "matching counts are one object and not a "
                  "coincidence", viol == cross)


def e4_pair_control():
    print("\nE4  THE PAIR CONTROL (nesting on the smallest id scan)")
    alpha, h = ID_SCANS[3]
    runs = bad = 0
    for digs in itertools.product(alpha, repeat=h):
        J = SC.images(SC.cylinders(list(digs)), "id")[:h]
        for pol in PAIR_POLS:
            runs += 1
            if SE.run_pair(J, pol, h)["last_bad"] is not None:
                bad += 1
    print("  %d pair runs, %d bad" % (runs, bad))
    check("E4 the nesting law holds on the anchor scan", bad == 0)


def main():
    print("=" * 62)
    print("THE LADDER-ENTRY LEMMA")
    print("=" * 62)
    e1_control()
    e2_identity()
    e3_maps()
    e5_correspondence()
    e4_pair_control()
    print("\n" + "=" * 62)
    if FAILURES:
        print("FAILURES: %s" % FAILURES)
        return 1
    print("ALL CHECKS PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
