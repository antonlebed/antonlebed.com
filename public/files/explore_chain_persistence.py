"""CHAIN-PREFERRING PERSISTENCE: what gates the nesting law — the
map, the regime, and the crossing geometry.

THE QUESTION
------------
explore_seed_exclusion.py left the chain-preferring nesting law a
rule at census scope: a reader preferring the chain at both cell
kinds ((st, ss) = (1, 0)) has its tree-patience-down run nested
pointwise at every step under the identity map — 14,680 pairs,
zero exceptions — and the named owe was a persistence proof: from
a nested pair state, drift never happens. This rig asks what that
proof may assume: is the law a property of the commit loop alone
(any image stream), or does it consume the identity map's special
structure? And whichever way, what is the exact geometry of a
drift when one exists?

THE NAMED CLASS (imported verbatim)
-----------------------------------
Cover, streams, maps, cells and the lockstep pair walk are the
parents' (explore_scale_clock.py, explore_seed_exclusion.py).
Policies (1, 0, pt, pc), pt in {2, 3, INF} x pc in {1, 2, 3},
each against its tree-patience-down (INF lowered to 3). Pair
badness = any step whose committed intervals fail nested-or-equal
in either direction (closed containment).

HAND-ATTACK (fixed before the engine; the derivation this rig
checks)
------------------------------------------------------------
Both runs' committed cells always contain the stream point (every
cell entered contains a reference, every reference contains the
current image, and the images nest onto the point). Write w for a
vertex (a cell's mediant), cell(w) for the tree cell whose
mediant w is, L_j = l + j*w for its chain points on the stream
point's side, S_q(w) for the straddle of index q at w.

D1 THE CROSSING CATALOG. Two cells around the stream point can
   fail to nest only as S_q(w) x a flank cell whose interior
   holds an endpoint of S_q(w) — a tree cell (L_i, w) with i < q,
   or a straddle at the vertex L_q itself, which reaches from
   below L_q up past it. Straddles at the INTERMEDIATE vertices
   L_i, i < q, are the ones that nest rather than cross; all
   other pairs nest. (Proved by enumerating the cells whose
   interior holds L_q: an intermediate vertex's straddle reaches
   right only to w + j*L_i, whose coordinate ratio against
   (L_{i-1}, w) stays at most 2 and so falls short of L_q's,
   while the straddles AT L_q are exactly the family that
   brackets it.)
D2 PATH-FOLLOWING. The two runs share the chain reference. If the
   elder run's micro-path ever lands on a cell of the fresher
   run's path, it follows the same decisions until it halts:
   chain candidates are a function of cell and chain reference
   alone, and a door child containing the elder tree reference
   contains the fresher one, children being interior-disjoint. So
   from a met cell, the fresher commit nests inside the elder's.
D3 CHAIN RESYNC. A chain-preferring run passing a straddle
   family's entry cell with a live candidate always chains, to
   the index kmax which is a function of vertex and chain
   reference alone — the engine reads the vertex's two parents
   too, but a vertex determines them (each has one Farey parent
   pair) — so both runs passing there land in the SAME straddle:
   the pair re-equalizes at every live chain vertex.
D4 KMAX MONOTONICITY. References only shrink, so kmax at a fixed
   vertex never decreases over steps, and a run's straddle index
   always equals kmax at the step it entered or deepened. Hence
   no run ever doors out of S_k(w) while the other holds a
   DEEPER straddle at w — the deeper index would exceed the
   current kmax.
D5 THE REGIME SPLIT. The fresher run's tree reference t and the
   shared chain reference c are members of one nested reference
   chain, hence comparable, with discrete indices: either t is at
   least as fresh as c (pc >= pt - 1, "fresh regime") or t is at
   least one step staler than the PREVIOUS chain reference
   (pc <= pt - 2, "stale regime"). In the fresh regime a drift
   needs the FLANK run's tree reference to poke past a chain
   vertex that c sits strictly inside of — impossible when that
   reference is inside c, since the straddle committer chained
   to the index c fits, so c and everything inside it lies
   strictly within the straddle and cannot hold its endpoint:
   the door opens, the flank run descends, and the argument
   never mentions the map. This reaches the FRESHER run's
   reference, which the fresh regime puts inside c; the elder's
   is one step staler and can sit outside, so the derivation
   covers the fresher-run-flanks role only — which E4c reports
   is the role every observed crossing takes (the elder commits
   the straddle in all 3,626). In the stale regime the drift
   shape is live unless the references' SHAPE forbids it.
D6 FAREY RIGIDITY (the identity map's private property). Under
   the identity map every reference is a continued-fraction
   cylinder: a Farey interval (endpoint determinant +-1). A Farey
   interval holding a vertex u strictly interior contains all of
   cell(u); equivalently a reference strictly inside a straddle
   never holds the straddle's vertex interior. Moreover the
   pivots of the point's descent are its convergents; for a pivot
   w = conv_sigma the cylinders hold w interior before index
   sigma, touch w as an endpoint exactly at sigma, and sit
   strictly on the point's side after; the only cylinder of the
   form (L_j, w) is (L_1, w). These exclusions close the stale
   drift shapes traced by hand, except a residual family of
   endpoint-equality branches (references with an endpoint
   exactly at a semiconvergent, doors blocked by the strict
   containment test) not yet exhausted — so the identity law is
   expected to survive every scan below while remaining a rule
   with a proved skeleton, not yet a theorem.
Under sq and dbl the references are images of cylinders and the
determinant is not +-1: a reference can straddle a vertex while
hugging it, blocking the elder run's chasing door forever — the
drift shape D5 leaves live. Scouting found such drifts; this rig
freezes the claims.

PREDICTIONS, fixed before the engine ran
----------------------------------------
S1 [gate, positive control] The three sq stall specimen worlds
   (near-miss, flagship, designed) each show at least one bad
   step in some (1, 0) pair under sq; the same digit streams
   under id show none. A detector that cannot see the sq drift
   proves nothing about id (K1).
S2 [the id law, widened] Exhaustive scans over the frozen digit
   alphabets below, identity map, all nine policy pairs: ZERO bad
   steps. A single miss kills the law and the specimen is the
   finding (K2).
S3 [the map gate] The same scans under sq and dbl show bad pairs
   in both maps.
S4 [the regime law] Every off-identity bad pair sits in the stale
   regime: pc <= pt - 2 for finite pt, pc <= 2 for the
   INF-lowered pair. Zero fresh-regime failures under any map.
S5 [the crossing geometry] GUESS, marked as such: at every
   off-identity first-crossing, (a) one committed cell is a
   straddle with an interval endpoint strictly interior to the
   other cell (the catalog shape D1), and (b) the straddle
   committer's tree reference holds that endpoint vertex strictly
   interior WITHOUT containing the vertex's cell — the shape
   Farey rigidity forbids under id. Tallied, exceptions printed;
   a miss is a finding about the catalog, not a dead rig.

S7 [the policy completion, frozen before E6 ran] The nine pairs
   E2 scans are pt in {2, 3, INF} x pc in {1, 2, 3}, while the
   census this widens ran pt in {1, 2, 3, INF} against the base
   axis {0, 1, 2, 3, INF} for pc — so E2 is exhaustive in
   STREAMS and short of the census in POLICIES, and "widens the
   census" is not earned until the missing eleven pairs run.
   GUESS: they behave like the nine — zero bad steps under the
   identity map over the same alphabets. A miss is the more
   interesting outcome by far: it would put the law's boundary
   inside the policy set rather than at the map, and the first
   specimen is then the finding.

KILL CRITERIA (observables, meaning weighed after the run)
----------------------------------------------------------
K1 An S1 control miss: the walk or detector is broken — no
   verdicts.
K2 An S2 miss: the identity law is dead at the printed specimen.
K3 Otherwise every tally prints as a finding; S4/S5 misses scope
   the derivation, not the rig.

ENGINE
------
E1 the controls (S1): the three sq stall specimens under sq and
   under id, all nine pairs.
E2 the identity scan (S2): exhaustive digit products, id —
   alphabets {1,2,3,40}^6, {1,2,3}^7, {1,2,4,9,30}^7,
   {1,2,7,25}^8, {1,3,5,80}^7, {1,2}^10, {1,2,3}^9, {1}^16.
E3 the map contrast (S3, S4): {1,2,3,40}^6 and {1,2,4,9,30}^6
   under sq and dbl; per bad pair the (pt, pc) tally and the
   regime split.
E4 the crossing read (S5): for every E3 bad pair, re-walk to the
   first bad step, classify the committed pair against the
   catalog, and test the committer's tree reference for the
   rigidity violation; print the first specimens per map.
E4b the door-block shapes (added by the review of this record,
   which had computed the tally outside the rig to check F4's
   mechanism claim — the leg exists so the record prints what its
   prose states, and its numbers were known before it ran): per
   crossing, the committing run's block shape —
   rigidity, endpoint equality at the vertex, no tree reference,
   or other — split by map and by finite/infinite patience.
E4c the bad-state kinds (same provenance as E4b: the word
   CROSSING carries the catalog, and a bad state could equally
   be an INVERTED containment — the elder run's cell strictly
   inside the fresher's — which is not a crossing at all): the
   first bad state per pair, whether any step of that pair is
   ever INVERTED, and WHICH run committed the straddle, since
   the refused door belongs to the other one and that decides
   whose tree reference D5's regime argument has to reach.
E6 the policy completion (S7, added by the same review): the
   eleven chain-preferring pairs E2 omits — pt = 1 against every
   pc, and pc in {0, INF} against every pt — over E2's alphabets
   under the identity map, so the scan's policy set matches the
   census's chain-preferring slice exactly.
E5 the away-side exclusion (same provenance as E4b: the review
   checked F5's hand argument, found its coefficient case
   analysis incomplete at one index, and wired the check the
   repaired argument needs): over complete digit products, can
   any identity cylinder endpoint equal an away-side straddle
   endpoint (1 + j) conv_sigma - conv_{sigma-1}? Tallied at
   j >= 1 (the straddle case, which must be empty) and at j = 0
   (the boundary the repaired argument excludes by the straddle
   index alone, which must NOT be empty or that exclusion is
   decorative).
Exact big-integer arithmetic for every verdict; estimated run
ten minutes; memory trivial; exit nonzero on any check
failure.

FINDINGS (entered after the run; ALL CHECKS PASS, exit 0)
----------------------------------------------------------------
F1 THE CONTROLS HOLD. Each of the three sq stall specimens drifts
   in exactly one policy pair ((1, 0, 3, 1) every time); the same
   digit streams under the identity map never drift.
F2 THE IDENTITY LAW AT EXHAUSTIVE SCOPE, AND THE POLICY SET
   COMPLETED (S7 held). 3,740,720 pair runs with ZERO bad steps:
   E2's 1,683,324 over eight complete digit products up to
   {1,2,7,25}^8 and {1,2}^10 at nine policy pairs, plus E6's
   2,057,396 at the eleven pairs E2 omitted — pt = 1 against
   every pc, and pc in {0, INF} against every pt — so the scan's
   policy set is now exactly the census's chain-preferring slice
   (four tree patiences x five chain patiences = twenty pairs)
   and "widens the census" is earned in both dimensions rather
   than one. The eight products are not eight independent
   scopes: the walk is prefix-deterministic (a step's state
   reads only the digits up to it), so {1,2,3}^7 is covered by
   {1,2,3}^9 and its runs are re-runs — 3,696,980 of the runs
   carry distinct coverage, and both figures are stated because
   the smaller one is what the scope means. The
   census evidence (14,680 curated-world pairs) widens by better
   than two orders of magnitude and the law survives digit
   values far outside the curated pools.
F3 THE MAP GATE AND THE REGIME LAW. The same commit loop drifts
   as soon as the map moves off the identity: sq 2,620 bad pairs
   (2,440 at (pt, pc) = (3, 1), 23 at (INF, 1), 157 at
   (INF, 2)), dbl 1,006 (all at (3, 1)). Every bad pair sits in
   the stale regime — the fresher run's tree reference strictly
   staler than the shared chain reference — and the fresh regime
   shows zero failures under every scanned map: the door
   direction argument (D5) is map-free, as predicted — derived
   for the flanking role every observed crossing takes (F4) and
   measured for both.
F4 ONE CATALOG, TWO MECHANISMS, AND THE SPLIT IS THE MAP'S.
   Every off-identity failure really is a CROSSING and never an
   inverted containment: all 3,626 first bad states are OVERLAP,
   and no step of any bad pair is ever INVERTED (E4c) — the
   elder run's cell never sits strictly inside the fresher's,
   under either map. The same tally fixes the ROLES, which is
   what D5's regime argument needs: the ELDER run commits the
   straddle in every one of the 3,626, so the refused door is
   always the fresher run's — the reference the fresh regime
   puts inside the chain reference, and the one case the
   argument covers. All 3,626 classify into the catalog shape
   (a committed straddle with an interval endpoint strictly
   interior to the other committed cell), and the E4b tally
   partitions their door blocks with no remainder and no
   overlap: sq finite-patience 2,440 RIGIDITY — the committer's
   tree reference holds the vertex strictly interior without
   containing the vertex's cell, the shape a Farey interval
   cannot take (printed specimen: reference (25/9, 49/16),
   determinant -41, straddling the vertex 3); sq infinite-
   patience 180 NO-REF — that reader holds no tree reference, so
   no door can open and no block is needed; dbl 1,006 ENDPOINT —
   zero rigidity violations, every one blocked by a reference
   endpoint sitting EXACTLY at the crossing vertex (printed
   specimen: reference (10/3, 7/2), right end exactly the vertex
   7/2, so the strict containment test refuses the chasing door
   at the shared endpoint), the doubling map aligning cylinder
   endpoints onto the vertex lattice. Not one crossing under
   either map falls outside the three. The two blocking families
   the hand derivation named are exactly the two the maps
   realize.
F5 THE AWAY-SIDE EXCLUSION (property, from the convergent
   coordinates). For a pivot w = conv_sigma the away-side
   straddle endpoints are R_j(w) = (1 + j) conv_sigma -
   conv_{sigma-1}, with j the straddle index — a NEGATIVE second
   coefficient — while consecutive convergents are independent,
   so an equality forces its coefficients to match. Reference
   endpoints from index sigma onward are non-negative
   combinations of the same two convergents (the convergent
   recurrence has non-negative coefficients), and endpoints older
   than index sigma - 1 have denominators below q_sigma, which
   the away-side endpoints exceed for every j >= 1. The one
   endpoint the coefficient argument does NOT cover is index
   sigma - 1's far end, conv_{sigma-1} + conv_{sigma-2} =
   conv_sigma - (a_sigma - 1) conv_{sigma-1}, which is a negative
   combination exactly when a_sigma >= 2: matching coefficients
   there forces j = 0, and a straddle's index is at least 1. So
   no identity reference endpoint ever equals an away-side
   straddle endpoint, and the straddle-index bound is
   load-bearing rather than decorative — at j = 0 the
   coincidences are real and common (E5: zero coincidences in
   491,520 straddle-index checks, against 45,056 in 94,208 at
   j = 0). dbl's door-block shape is impossible under the
   identity map.

THE VERDICT. The chain-preferring nesting law is the identity
map's law, not the commit loop's: off the identity the same
readers drift abundantly, always in the stale regime, always in
the catalog's crossing shape, by exactly the two mechanisms the
hand derivation isolated — the non-Farey interior straddle (sq)
and the vertex-lattice endpoint equality (dbl). Under the
identity map the derivation now stands as a proved skeleton —
path-following (D2), chain resync (D3), kmax monotonicity (D4),
the crossing catalog (D1), Farey rigidity killing the interior
shape (D6), and the away-side exclusion (F5) killing the
endpoint shape on the far side — plus the measured law at
3,696,980-run exhaustive scope. What remains open for the
theorem: exhausting the NEAR-SIDE endpoint-equality branches
(references ending exactly at a semiconvergent on the stream
point's side), where the traced cases die by chain resync but no
enumeration closes the family. The law stays a rule at widened
scope; the remaining owe is one enumeration, not a mechanism.

Run record. SEVEN runs — about four minutes each through the
sixth, about ten once E6 joined; E1 through E4
print identically across every run that reached them. Runs one
to three produced the record above: the first exited 1 because
S5b — declared a tallied guess, with K3 scoping every S3-S5 miss
as a finding — had been wired as an exit-affecting check, and
the wiring was corrected to match the predictions as fixed (S3
through S5 print with their tallies; the gates are S1 and S2),
no prediction or threshold touched; the second crashed on a
summary format string after all sections had printed; the third
carried F1 to F5. Runs four to six each added a leg for a review
of this record, in the order the review found them and with the
numbers known before the leg ran (each leg's engine entry says
so): E4b, after F4's two-mechanism reading was found resting on
ONE traced dbl specimen; E5, after F5's coefficient case
analysis was found incomplete at index sigma - 1 — the endpoint
there is a NEGATIVE combination whenever the next partial
quotient is at least 2, so the exclusion rests on the straddle
index and not on the coefficient signs — with the argument
repaired and both its halves checked; and E4c, after the review
asked what the word CROSSING was resting on — extended in the
same pass with the straddle committer's role, once the review
found D5 stated for both roles and derived for one. A seventh
run added E6, the review having found E2 exhaustive in streams
but eleven policy pairs short of the census slice it claimed to
widen; S7 was frozen before that leg ran. Estimated and actual
run time rises to about ten minutes with E6 in.
"""

import sys
import itertools

import explore_scale_clock as SC
import explore_seed_exclusion as SE

FAILURES = []


def check(name, ok):
    tag = "PASS" if ok else "FAIL"
    print("  [%s] %s" % (tag, name))
    if not ok:
        FAILURES.append(name)


POLS = [(1, 0, pt, pc)
        for pt in (2, 3, None)
        for pc in (1, 2, 3)]

ID_SCANS = [
    ((1, 2, 3, 40), 6),
    ((1, 2, 3), 7),
    ((1, 2, 4, 9, 30), 7),
    ((1, 2, 7, 25), 8),
    ((1, 3, 5, 80), 7),
    ((1, 2), 10),
    ((1, 2, 3), 9),
    ((1,), 16),
]

MAP_SCANS = [
    ((1, 2, 3, 40), 6),
    ((1, 2, 4, 9, 30), 6),
]

AWAY_ALPHA = (1, 2, 3, 5)
AWAY_H = 7
AWAY_JMAX = 5

SPECIMENS = (("near-miss", SE.NEARMISS),
             ("flagship", SE.FLAGSHIP),
             ("designed", SE.DESIGNED))


def is_stale(pol):
    _, _, pt, pc = pol
    if pt is None:
        return pc <= 2
    return pc <= pt - 2


def bad_pairs(digs, mp, horizon):
    J = SC.images(SC.cylinders(list(digs)), mp)[:horizon]
    out = []
    for pol in POLS:
        pd = SE.run_pair(J, pol, horizon)
        if pd["last_bad"] is not None:
            out.append((pol, pd))
    return out


def walk_cells(J, pol, horizon):
    """Lockstep walk keeping per-step committed cells and refs."""
    st, ss, pt, pc = pol
    ptd = 3 if pt is None else pt - 1
    Cx = Cy = SC.ROOT
    rows = []
    for n in range(horizon):
        rtx = J[n - pt] if pt is not None and n - pt >= 0 else None
        rty = J[n - ptd] if n - ptd >= 0 else None
        rc = J[n - pc] if pc is not None and n - pc >= 0 else None
        Cx, _ = SE.commit_step(Cx, rtx, rc, st, ss)
        Cy, _ = SE.commit_step(Cy, rty, rc, st, ss)
        rows.append((Cx, Cy, rtx, rty, rc))
    return rows


def strictly_inside(x, iv):
    lo, hi = iv
    return SC.lt(lo, x) and SC.lt(x, hi)


def covers(ref, iv):
    lo, hi = iv
    return SE.frac_le(ref[0], lo) and SE.frac_le(hi, ref[1])


def vertex_cell(cell, endpoint_is_left):
    """The tree cell of a straddle interval's endpoint vertex:
    for S_k at v born of (l, r), the left endpoint l + k*v has
    cell (l + (k-1)*v, v); mirror on the right."""
    _, v, l, r, _, k = cell
    if endpoint_is_left:
        prev = (l[0] + (k - 1) * v[0], l[1] + (k - 1) * v[1])
    else:
        prev = (r[0] + (k - 1) * v[0], r[1] + (k - 1) * v[1])
    return prev, v


def eq_frac(a, b):
    return a[0] * b[1] == b[0] * a[1]


def straddle_role(Cx, Cy):
    """Which run committed the straddle whose endpoint sits
    inside the other's cell — 'elder' (the parent policy) or
    'fresher' (its tree-patience-down). The door that was
    refused belongs to the OTHER one, which is what decides
    whose tree reference the regime argument must reach."""
    for lbl, P, Q in (("elder", Cx, Cy), ("fresher", Cy, Cx)):
        if P[0] != "S":
            continue
        mL, mR = SC.interval(P)
        qiv = SC.interval(Q)
        if any(strictly_inside(u, qiv) for u in (mL, mR)):
            return lbl
    return "none"


def block_shape(Cx, Cy, rtx, rty):
    """At a crossing, the door-block shape of the run that
    committed the straddle: 'rigidity' (its tree reference holds
    the crossing vertex strictly interior without containing the
    vertex's cell), 'endpoint' (a reference endpoint sits exactly
    at the vertex), 'no-ref' (that run holds no tree reference at
    all), or 'other'."""
    for P, Q, t in ((Cx, Cy, rtx), (Cy, Cx, rty)):
        if P[0] != "S":
            continue
        mL, mR = SC.interval(P)
        qiv = SC.interval(Q)
        for u, left in ((mL, True), (mR, False)):
            if not strictly_inside(u, qiv):
                continue
            if t is None:
                return "no-ref"
            cl, cr = vertex_cell(P, left)
            civ = (cl, cr) if SC.lt(cl, cr) else (cr, cl)
            if strictly_inside(u, t) and not covers(t, civ):
                return "rigidity"
            if eq_frac(t[0], u) or eq_frac(t[1], u):
                return "endpoint"
            return "other"
    return "unclassified"


def classify_crossing(Cx, Cy, rtx, rty):
    """Catalog test at a bad step: find a straddle among the two
    committed cells with an interval endpoint strictly interior
    to the other; then test the committer's tree reference for
    the rigidity violation at that vertex. Returns (matched,
    violated, vertex) for the first matching shape, or
    (False, False, None)."""
    for P, Q, t in ((Cx, Cy, rtx), (Cy, Cx, rty)):
        if P[0] != "S":
            continue
        mL, mR = SC.interval(P)
        qiv = SC.interval(Q)
        for u, left in ((mL, True), (mR, False)):
            if not strictly_inside(u, qiv):
                continue
            cl, cr = vertex_cell(P, left)
            civ = (cl, cr) if SC.lt(cl, cr) else (cr, cl)
            viol = (t is not None and strictly_inside(u, t)
                    and not covers(t, civ))
            return True, viol, u
    return False, False, None


def e1_controls():
    print("\nE1  THE CONTROLS (sq specimens vs their id streams)")
    sq_bad = id_bad = 0
    for name, digs in SPECIMENS:
        h = len(digs)
        nb_sq = len(bad_pairs(digs, "sq", h))
        nb_id = len(bad_pairs(digs, "id", h))
        sq_bad += (nb_sq > 0)
        id_bad += nb_id
        print("  %-9s sq bad pols: %d   id bad pols: %d"
              % (name, nb_sq, nb_id))
    check("S1a every sq specimen drifts in some pair", sq_bad == 3)
    check("S1b the same streams under id never drift", id_bad == 0)


def e2_id_scan():
    print("\nE2  THE IDENTITY SCAN (exhaustive, frozen alphabets)")
    total_runs = 0
    total_bad = 0
    for alpha, h in ID_SCANS:
        nb = 0
        n = 0
        for digs in itertools.product(alpha, repeat=h):
            hits = bad_pairs(digs, "id", h)
            n += len(POLS)
            if hits:
                nb += len(hits)
                for pol, pd in hits[:3]:
                    print("  ID DRIFT digs=%s pol=%s states=%s"
                          % (digs, pol, pd["states"]))
        total_runs += n
        total_bad += nb
        print("  id %s^%d: %d pair runs, %d bad"
              % (set(alpha), h, n, nb))
    check("S2 zero id bad pairs across all scans (%d runs)"
          % total_runs, total_bad == 0)


def e3_e4_maps():
    print("\nE3/E4  THE MAP CONTRAST AND THE CROSSING READ")
    tallies = {}
    viol_by = {}
    shapes = {}
    kinds = {}
    fresh_bad = 0
    n_bad = n_class = n_viol = 0
    shown = {}
    for mp in ("sq", "dbl"):
        for alpha, h in MAP_SCANS:
            for digs in itertools.product(alpha, repeat=h):
                J = SC.images(SC.cylinders(list(digs)), mp)[:h]
                for pol in POLS:
                    pd = SE.run_pair(J, pol, h)
                    if pd["last_bad"] is None:
                        continue
                    n_bad += 1
                    key = (mp, pol[2], pol[3])
                    tallies[key] = tallies.get(key, 0) + 1
                    if not is_stale(pol):
                        fresh_bad += 1
                        print("  FRESH-REGIME BAD: %s %s %s"
                              % (mp, digs, pol))
                    rows = walk_cells(J, pol, h)
                    bad_n = next(
                        i for i, s in enumerate(pd["states"])
                        if s in ("OVERLAP", "INVERTED"))
                    Cx, Cy, rtx, rty, _ = rows[bad_n]
                    m, v, u = classify_crossing(Cx, Cy, rtx, rty)
                    n_class += m
                    n_viol += v
                    cm, vm = viol_by.get(mp, (0, 0))
                    viol_by[mp] = (cm + m, vm + v)
                    sk = (mp, "INF" if pol[2] is None else "fin",
                          block_shape(Cx, Cy, rtx, rty))
                    shapes[sk] = shapes.get(sk, 0) + 1
                    kk = (mp, pd["states"][bad_n],
                          "INVERTED" in pd["states"],
                          straddle_role(Cx, Cy))
                    kinds[kk] = kinds.get(kk, 0) + 1
                    if m and shown.get(mp, 0) < 2:
                        shown[mp] = shown.get(mp, 0) + 1
                        print("  %s specimen digs=%s pol=%s "
                              "step=%d vertex=%d/%d viol=%s"
                              % (mp, digs, pol, bad_n,
                                 u[0], u[1], v))
    for key in sorted(tallies, key=str):
        print("  bad tally %s: %d" % (key, tallies[key]))
    ok3 = (any(k[0] == "sq" for k in tallies)
           and any(k[0] == "dbl" for k in tallies))
    print("  [%s] S3 sq and dbl both drift (finding, not a gate)"
          % ("pred-HIT" if ok3 else "pred-MISS"))
    print("  [%s] S4 fresh-regime bad pairs: %d (finding)"
          % ("pred-HIT" if fresh_bad == 0 else "pred-MISS",
             fresh_bad))
    for mp in sorted(viol_by):
        c_m, v_m = viol_by[mp]
        print("  S5 %s: catalog %d/%d, rigidity violations %d/%d"
              % (mp, c_m, c_m, v_m, c_m))
    print("  [%s] S5a all %d crossings classify (finding)"
          % ("pred-HIT" if n_class == n_bad else "pred-MISS",
             n_bad))
    print("  [%s] S5b rigidity violations %d/%d (finding)"
          % ("pred-HIT" if n_viol == n_bad else "pred-MISS",
             n_viol, n_bad))
    print("  E4c the bad-state kinds (map, first bad state, any "
          "INVERTED step at all, straddle committer):")
    for key in sorted(kinds, key=str):
        print("    %-34s %d" % (str(key), kinds[key]))
    print("  E4b the door-block shapes (map, patience, shape):")
    for key in sorted(shapes, key=str):
        print("    %-22s %d" % (str(key), shapes[key]))


POLS_REST = [(1, 0, pt, pc)
             for pt in (1, 2, 3, None)
             for pc in (0, 1, 2, 3, None)
             if (pt, pc) not in
             [(a, b) for a in (2, 3, None) for b in (1, 2, 3)]]


def e6_policy_completion():
    """S7: the chain-preferring pairs E2 does not scan, so the
    policy set matches the census's slice."""
    print("\nE6  THE POLICY COMPLETION (identity, the %d pairs E2"
          " omits)" % len(POLS_REST))
    n = nb = 0
    for alpha, h in ID_SCANS:
        for digs in itertools.product(alpha, repeat=h):
            J = SC.images(SC.cylinders(list(digs)), "id")[:h]
            for pol in POLS_REST:
                n += 1
                pd = SE.run_pair(J, pol, h)
                if pd["last_bad"] is not None:
                    nb += 1
                    if nb <= 3:
                        print("  ID DRIFT digs=%s pol=%s states=%s"
                              % (digs, pol, pd["states"]))
    print("  %d pair runs over the same alphabets, %d bad" % (n, nb))
    check("S7 zero id bad pairs at the completing policies", nb == 0)


def convergents(digs):
    p2, q2, p1, q1 = 0, 1, 1, 0
    out = []
    for a in digs:
        p, q = a * p1 + p2, a * q1 + q2
        out.append((p, q))
        p2, q2, p1, q1 = p1, q1, p, q
    return out


def e5_away_side():
    """The away-side exclusion (F5) machine-checked: can any
    identity reference endpoint equal an away-side straddle
    endpoint (1 + j) conv_sigma - conv_{sigma-1}? j >= 1 is the
    straddle case; j = 0 is the boundary the argument excludes by
    the straddle index alone, and it must show real coincidences
    or that exclusion is decorative."""
    print("\nE5  THE AWAY-SIDE EXCLUSION (identity cylinders)")
    n_chk = [0, 0]
    n_hit = [0, 0]
    for digs in itertools.product(AWAY_ALPHA, repeat=AWAY_H):
        cv = convergents(list(digs))
        ends = [e for iv in SC.cylinders(list(digs)) for e in iv]
        for s in range(1, len(cv)):
            for j in range(0, AWAY_JMAX + 1):
                a = ((1 + j) * cv[s][0] - cv[s - 1][0],
                     (1 + j) * cv[s][1] - cv[s - 1][1])
                if a[1] <= 0:
                    continue
                slot = 0 if j == 0 else 1
                n_chk[slot] += 1
                if any(eq_frac(e, a) for e in ends):
                    n_hit[slot] += 1
    print("  j >= 1 (straddles): %d checks, %d coincidences"
          % (n_chk[1], n_hit[1]))
    print("  j = 0  (boundary):  %d checks, %d coincidences"
          % (n_chk[0], n_hit[0]))
    check("S6a no identity endpoint meets an away-side straddle "
          "endpoint", n_hit[1] == 0)
    check("S6b the j = 0 boundary really does coincide, so the "
          "straddle-index bound is load-bearing", n_hit[0] > 0)


def main():
    print("CHAIN-PREFERRING PERSISTENCE: the map gate, the regime,"
          " the crossing geometry")
    e1_controls()
    e2_id_scan()
    e3_e4_maps()
    e6_policy_completion()
    e5_away_side()
    print()
    if FAILURES:
        print("FAILURES: %d" % len(FAILURES))
        for f in FAILURES:
            print("  " + f)
        return 1
    print("ALL CHECKS PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
