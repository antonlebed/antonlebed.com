"""WHAT SEPARATES A DETERMINANT-2 REFERENCE THAT RESPECTS G2 FROM ONE
THAT DOES NOT — the last lattice label in the door inequalities.

THE QUESTION
------------
explore_reference_families.py sorted the reader corpus's nesting law by
what a reference family's lattice does and dissolved the sort into two
per-decision index inequalities at the door. One input survived that
dissolution still keyed to a lattice fact. G2 — at a door taken at a
convergent vertex v of cylinder index sigma, the opening tree reference
J has index(J) >= sigma + 1 — was measured as a determinant law ONE
WAY: |det J| = 1 is SUFFICIENT (568,195 doors, zero failures) and
nothing more, since |det| = 2 holds at 14,939 doors and fails at
73,354, and |det| = 3 holds at 18,735 and fails at 65,377.

A determinant that merely PERMITS failure is not a hypothesis. This rig
asks what the permission is actually keyed to, and the answer has to be
a property of ONE reference against ONE point, carrying no family label
and no lattice label.

NOTATION, the parent's. (l, r) a tree cell, v = l (+) r its vertex,
x the point the reference family converges to, C_j its cylinders,
index(J) the largest j with J inside C_j, sigma the convergent index of
the vertex, a = a_{sigma+1} the next partial quotient, L_j = l (+) j v
the near ladder. Every convergent-keyed quantity is read against the
FAMILY's own digits, never the unmapped stream's.

HAND-ATTACK (on paper, fixed before any engine code)
----------------------------------------------------
D1 THE DETERMINANT-1 FLOOR, derived here rather than cited. Let
   bc - ad = 1 and let p/q lie strictly inside (a/b, c/d). Both
   p/q - a/b = (pb - aq)/(qb) and c/d - p/q = (cq - pd)/(qd) are
   positive with integer numerators, hence at least 1/(qb) and 1/(qd).
   Their sum is c/d - a/b = 1/(bd), so 1/(bd) >= (b + d)/(qbd) and
   q >= b + d, attained by the mediant. So the interior fraction of
   least denominator across a determinant-1 interval is the mediant,
   at denominator exactly b + d: such a reference holds no interior
   structure the tree did not put there. (The adjacency property this
   rests on — consecutive tree fractions satisfy m2 n1 - m1 n2 = 1 —
   is classical and was read full text; the floor statement above was
   not found stated in the sources read, so it is derived and
   machine-controlled here rather than badged.)
D2 DETERMINANT 2 ALWAYS BREAKS THAT FLOOR, BY EXACTLY A FACTOR OF TWO.
   Let bc - ad = 2 with both endpoints reduced. If b is even then a is
   odd, and ad = bc - 2 is even forces d even and c odd. If b is odd
   then d is odd (b odd with d even makes bc - ad odd), and bc - ad = 2
   gives c = a mod 2. Either way a + c and b + d are both even, so
       m = ((a+c)/2) / ((b+d)/2)
   is an integer fraction, and b(a+c)/2 - a(b+d)/2 = (bc - ad)/2 = 1.
   So m is a Farey NEIGHBOUR of both endpoints — reduced, of
   denominator exactly (b+d)/2, half the determinant-1 floor — and both
   halves (a/b, m) and (m, c/d) have determinant 1, so by D1 their own
   interior floors are b + q_m and q_m + d, both above q_m. Every
   interior fraction other than m lies strictly inside one half, so m
   is the interior fraction of LEAST denominator and the only one at
   that denominator, and a determinant-2 reference is exactly two tree
   cells glued at m. Note what this does NOT say: those half-floors
   need not reach b + d, so an interval can hold interior fractions
   below the determinant-1 floor besides m — (0/1, 2/5) has
   determinant 2, floor 6, and holds 1/3, 1/4 and 1/5. The factor of
   two is a statement about the MINIMUM, not about a gap swept clean.
D3 THE GENERAL FORM. Every rational interval is a finite union of
   maximal tree cells: descend from the root, emit a cell once it lies
   inside J, recurse only while the cell still meets J's interior.
   It terminates because only finitely many cells hold a given rational
   in their interior. Determinant 1 is one piece; determinant 2 is two,
   by D2; determinant 3 is two or three and NOT three always —
   (1/2, 2/1) splits at 1/1 alone while (0/1, 3/1) needs 1/1 and 2/1.
   So the piece count is not the determinant. (Read full text for this
   step: Vuillemin, "Exact real computer arithmetic with continued
   fractions", INRIA RR-0760. It represents a real as an infinite
   product of determinant-+-1 homographies — the tree descent — and
   does interval arithmetic over arbitrary rational endpoints, but it
   does not decompose such an interval into maximal unimodular cells;
   the precision control there is the nesting of the successive images,
   not a piece count. One source read, not the whole line: so the
   construction above is stated here as an elementary property of the
   tree and is attributed to nobody, which is what the read settles and
   all it settles.)
D4 WHERE THE SEPARATOR MUST LIVE. C_j is an interval, so J lies inside
   C_j exactly when every piece does: index(J) is the MINIMUM over the
   pieces. That is a triviality. The content is which piece attains it.
   Exactly one piece contains x.
D5 THE DOOR LEMMA, and it makes D4's occupied piece free. The commit
   loop's containment is STRICT at both ends (explore_scale_clock.py
   contains()), and every door at v enters a child cell having v as an
   ENDPOINT. So the reference is strictly inside that child and v is
   not in it. A determinant-1 interval containing x is a node on x's
   own Stern-Brocot path, and the path's nodes are totally ordered; the
   nodes between C_sigma and C_{sigma+1} are the semiconvergent
   intervals (L_j, v), every one of which has v as an endpoint. A node
   holding no v is therefore no coarser than C_{sigma+1}. Hence:
   ANY determinant-1 reference that opens a door at a convergent vertex
   has index >= sigma + 1. That derives the sufficiency the parent only
   measured — and it applies verbatim to the piece of ANY reference
   that contains x, since that piece is determinant 1 and inherits the
   strict containment.
D6 SO THE SEPARATOR IS THE UNOCCUPIED PIECES. G2 holds at a door iff
   every piece the point does NOT occupy also reaches sigma + 1.
   Determinant 1 is sufficient because it is the case with no
   unoccupied piece. The determinant leaves the statement.

PREDICTIONS, fixed before the engine ran
----------------------------------------
Q1 [CONTROL, D2 machine-checked] Every determinant-2 interval has
   exactly two pieces, glued at m with q_m = (b+d)/2, and no interior
   fraction of denominator below q_m. Over an exhaustive box of reduced
   determinant-2 pairs AND over every determinant-2 reference the scan
   itself builds.
Q2 [the determinant is not the piece count] Determinant-3 references in
   the scanned corpus realize BOTH two and three pieces. All-three
   would mean the two sorts coincide at this scope — a scope note on
   Q3 at determinant 3, not a kill.
Q3 [THE SEPARATOR] At every door at a convergent vertex, in every
   family and at every determinant, the OCCUPIED piece has index
   >= sigma + 1, and the door's G2 verdict equals the conjunction over
   the UNOCCUPIED pieces. Zero exceptions to either.
   KILL, as observables: a nonzero count in the "occupied piece short"
   tally, or any disagreement between G2 and the unoccupied-piece
   conjunction.
Q4 [the sharper form, a GUESS and scoped as one] At a determinant-2
   door where G2 fails, the offending unoccupied piece leaves
   C_{sigma+1} across the boundary NEAREST THE VERTEX, because the door
   is what put the reference against v in the first place. Printed as a
   per-door tally of which boundary is crossed. Whatever it says it
   scopes the guess and does not touch Q3.

GATES (positive controls, run before any verdict is read)
---------------------------------------------------------
K1 The decomposition is a decomposition: over every reference the scan
   builds, the pieces are contiguous, their union is J exactly, and
   every one has determinant 1.
K2 THE REPRODUCTION GATE. This rig's own walk reproduces the parent's
   G2-per-determinant table exactly — 568,195 / 0 at |det| = 1,
   14,939 / 73,354 at 2, 18,735 / 65,377 at 3, over the same ten
   families and BOTH preference slices. A rig that cannot reproduce the
   table it is explaining explains nothing.
K3 Q1's box control.
Any K miss aborts before the separator tallies print.

ENGINE
------
E1 the gates (K1, K2, K3).
E2 the separator: per door, the piece decomposition of the opening
   reference, the occupied piece's index against sigma, and the G2
   verdict against the unoccupied conjunction (Q1 realized, Q2, Q3).
E3 Q4's boundary split, per offending piece, with the
   per-door reading recovered at determinant 2.
Exact big-integer arithmetic throughout; the scans and runs are the
parent's, imported; decompositions memoized per reference, which is
what keeps the cost near the parent's; memory trivial; exit nonzero on
any check failure.

FINDINGS (entered after the run; ALL CHECKS PASS, exit 0)
----------------------------------------------------------
F1 THE DETERMINANT IS NOT THE HYPOTHESIS, AND IT NEVER WAS: THE
   REFERENCE'S PIECES ARE. Decompose the opening reference into its
   maximal tree cells. One of them holds the family's own tail — the
   OCCUPIED piece, and F6 is where it can fail to be exactly one —
   and over all 738,910 classified doors,
   ten families, both preference slices, every determinant, that piece
   reaches sigma + 1 EVERY TIME: 568,195 at |det| = 1, 88,293 at 2,
   82,422 at 3, zero short. THAT COLUMN IS THE WHOLE OF THE EMPIRICAL
   CONTENT, and the rest of the table cannot come out any other way:
   the pieces TILE the reference, so index(J) IS the minimum over
   them (D4), and once the occupied piece never attains that minimum
   the G2 verdict is the conjunction over the unoccupied ones by
   arithmetic. The printed cross-tabulation — 568,195 holds at
   |det| = 1 with nothing unoccupied to fail, 14,939 against 73,354
   at 2, 18,676 against 63,746 at 3, no off-diagonal anywhere — is
   therefore a CONTROL on the decomposition code and not evidence for
   the criterion; it is reported because a decomposition bug is
   exactly what would put an entry off the diagonal.
   So the answer to what separates a determinant-2 reference that
   respects G2 from one that does not is: WHERE ITS UNOCCUPIED PIECE
   SITS. Determinant 1 is sufficient for the trivial reason that it
   has none — one piece, and the point is in it.
F2 AND THE OCCUPIED PIECE'S IMMUNITY IS A LEMMA, NOT A TALLY (D5). The
   commit loop's containment is strict and every door enters a child
   with the vertex as an ENDPOINT, so the reference — and hence its
   occupied piece — excludes v. A determinant-1 interval holding the
   point is a node on the point's own path; the nodes between C_sigma
   and C_{sigma+1} are the semiconvergent intervals, every one with v
   as an endpoint; so a node holding no v is no coarser than
   C_{sigma+1}. The scan's zeros are that lemma's control, and it also
   DERIVES the parent's measured sufficiency: |det| = 1 never fails G2
   because a determinant-1 reference IS its own occupied piece.
F3 THE PIECE COUNT IS NOT THE DETERMINANT, WHICH IS WHY THE
   RESTATEMENT IS NOT A RELABELLING (Q2). Determinant 2 is always two
   pieces (D2, and 88,293 of 88,293 doors), but determinant 3 is two
   pieces at 49,245 doors and three at 34,867. A determinant-3
   reference with two pieces has ONE unoccupied piece, exactly like a
   determinant-2 one, and is governed by the same conjunction — the
   determinant sort cuts across the piece sort rather than refining
   it.
F4 WHAT DETERMINANT 2 ACTUALLY FORCES, on paper (D2): its two pieces
   are glued at the half-mediant ((a+c)/2)/((b+d)/2), a Farey
   neighbour of BOTH endpoints, whose denominator is exactly half the
   determinant-1 floor b + d and is the least in the interior. So the
   determinant-2 case is not "off the lattice" in any loose sense: it
   is two lattice cells with one extra cell boundary inside, and the
   whole of G2's failure is that the point lives in only one of them.
F5 Q4 IS SCOPED AND THE GUESS IS WRONG AS STATED. Q4 was frozen as a
   per-DOOR tally, which is well posed only at determinant 2, where
   there is exactly one unoccupied piece; at determinant 3 a
   three-piece reference has two, and both can fail, so the tally is
   taken PER OFFENDING PIECE and the two readings coincide where the
   prediction lives. At the 73,354 failing determinant-2 doors the
   offender crosses the vertex-side boundary of C_{sigma+1} at 44,920
   and the far boundary at 28,434, never both. So the door does press
   the reference toward the vertex — a clear majority, 61.2% — but it
   does not force the side, and at determinant 3 the majority
   reverses (38,423 toward the vertex against 51,819 away). No door
   in the scan has an offender with C_{sigma+1} past the read
   horizon, so nothing is excluded from those counts. The direction
   is a tendency of the door, not a mechanism, and nothing in F1
   rests on it.
F6 THE OCCUPIED PIECE IS WELL POSED, AND THAT WAS NOT FREE. A finite
   digit stream names a cylinder, not a real, so "the piece containing
   the point" is read through the family's TAIL WINDOW — the finest
   reference met with the finest cylinder — and a seam running through
   that window is genuinely ambiguous rather than resolvable. It
   happens at 1,690 doors, all at determinant 3, and they are excluded
   from F1's tallies and counted here rather than assigned a side. An
   earlier pass of this rig picked an interior rational of the window
   instead and so chose a side by coincidence; it returned tallies
   identical to these, which says the ambiguity is real but never
   load-bearing.

THE VERDICT. G2 was the last input to the door inequalities keyed to a
lattice label, and the label was a proxy for a decomposition. A
reference is a finite union of tree cells; the door lemma gives the
cell holding the point its index for free; and G2 asks the remaining
cells — the part of the reference the tree did not put there — to
reach the same depth. Determinant 1 satisfies that vacuously, which is
the whole of its sufficiency, and determinants 2 and 3 satisfy it
sometimes because sometimes the unoccupied cells are deep enough. No
family label, no lattice label, and no determinant survives in the
statement.

Run record. Three runs. The first carried F1 to F5 and passed every
gate; reading it is what exposed the occupied piece's dependence on an
arbitrary interior rational, so the second replaced that with the tail
window (F6) and added K0, D1's own control, after two full-text
sources returned the unimodular adjacency property but not the
smallest-denominator floor. The second run's separator tallies are
identical to the first's. The third is this record's audit: Q4 was
recording only the FIRST offending piece in left-to-right order,
which reports a tie-break as a fact wherever a reference has two of
them, so it now counts per piece — determinant 2 unchanged and
determinant 3 moved, which is the audit's own control on the
distinction mattering. The same pass replaced a float sort key inside
the decomposition with an exact one; K1's contiguity check was all
that stood behind it. A fourth followed the audit's find that D2's
prose over-read its own proof — the half-floors b + q_m and q_m + d
clear q_m but need not clear b + d, so "unique below the floor" was
false where Q1's frozen prediction ("none below q_m") was right — and
added the uniqueness-at-the-minimum control the prose had been
asserting without one. About seven seconds each; peak working set
24 MB under memwatch.
"""

import os
import sys
import itertools
from fractions import Fraction

import explore_scale_clock as SC
import explore_seed_exclusion as SE
import explore_chain_persistence as CP
import explore_reference_families as RF

FAILURES = []


def check(name, ok):
    print("  [%s] %s" % ("PASS" if ok else "FAIL", name))
    if not ok:
        FAILURES.append(name)


# ----------------------------------------------------------------- #
# the decomposition                                                  #
# ----------------------------------------------------------------- #

def flt(a, b):
    """Strict order on fractions given as (num, den), den >= 0, with
    (1, 0) reading as the point at infinity."""
    return not RF.frac_le(b, a)


def mediant(a, b):
    return (a[0] + b[0], a[1] + b[1])


ROOT_IV = ((0, 1), (1, 0))


def pieces(J):
    """The maximal tree cells contained in J, left to right (D3)."""
    out = []
    stack = [ROOT_IV]
    guard = 0
    while stack:
        guard += 1
        if guard > 10 ** 6:
            raise AssertionError("decomposition runaway")
        C = stack.pop()
        if RF.contains_iv(J, C):
            out.append(C)
            continue
        if flt(C[0], J[1]) and flt(J[0], C[1]):
            m = mediant(C[0], C[1])
            stack.append((m, C[1]))
            stack.append((C[0], m))
    # Exact key: a float ratio would be a rounding step inside a rig
    # whose whole point is exact arithmetic, and K1's contiguity check
    # is what would have to catch it.
    out.sort(key=lambda c: Fraction(c[0][0], c[0][1]))
    return out


PIECE_CACHE = {}


def pieces_cached(J):
    got = PIECE_CACHE.get(J)
    if got is None:
        got = pieces(J)
        PIECE_CACHE[J] = got
    return got


def contiguous(J, ps):
    """K1: the pieces tile J exactly, each of determinant 1."""
    if not ps:
        return False
    if ps[0][0] != J[0] or ps[-1][1] != J[1]:
        return False
    for i in range(1, len(ps)):
        if ps[i - 1][1] != ps[i][0]:
            return False
    return all(RF.det2(p[0], p[1]) == 1 for p in ps)


def least_interior_denominator(J):
    """Brute force: the smallest denominator of a fraction strictly
    inside J, searched upward. Control for D1/D2 only, never in the
    scan path."""
    q = 1
    while True:
        lo = J[0][0] * q // J[0][1]
        for p in range(lo, lo + 2 + q):
            f = (p, q)
            if flt(J[0], f) and flt(f, J[1]):
                return q
        q += 1
        if q > 4000:
            raise AssertionError("no interior fraction found")


# ----------------------------------------------------------------- #
# the walk — the parent's commit loop, tallied per DOOR              #
# ----------------------------------------------------------------- #

def tail_window(refs, fcyls):
    """The family's own tail: the finest reference met with the finest
    cylinder, an INTERVAL rather than a point. A finite digit stream
    names a cylinder and not a real, so "the piece containing x" is
    only well posed through this window — picking some interior
    rational instead would choose a side of a seam by coincidence,
    which is a convention feeding a headline tally. None when the two
    do not meet (counted, never folded into either verdict)."""
    a, b = refs[-1], fcyls[-1]
    lo = a[0] if RF.frac_le(b[0], a[0]) else b[0]
    hi = a[1] if RF.frac_le(a[1], b[1]) else b[1]
    if not flt(lo, hi) or hi[1] == 0:
        return None
    return (lo, hi)


def occupied(ps, win):
    """The index in ps of the piece containing the whole tail window,
    or None when a seam runs through it — the genuinely ambiguous
    case, which gets its own bucket (D4's degenerate case)."""
    hits = [i for i, p in enumerate(ps) if RF.contains_iv(p, win)]
    return hits[0] if len(hits) == 1 else None


def walk(refs, ridx, fcvs, fdigs, fcyls, P, pc, s_t, s_s, win, tally):
    """One run over one family; every DOOR at a convergent vertex
    decomposed. Mirrors explore_reference_families.trace's control
    flow and records nothing else."""
    h = len(refs)
    C = SC.ROOT
    for n in range(h):
        rt = refs[n - P] if P is not None and n - P >= 0 else None
        rc = refs[n - pc] if pc is not None and n - pc >= 0 else None
        ti = ridx[n - P] if P is not None and n - P >= 0 else None
        try:
            C, records = SE.commit_step(C, rt, rc, s_t, s_s)
        except AssertionError:
            tally["runaway"] = tally.get("runaway", 0) + 1
            return
        for cell, cand_tree, cand_chain, took in records:
            if took != "door":
                continue
            v, l, r, k = RF.cell_vertex(cell)
            sig = RF.conv_index(fcvs, v)
            if sig is None or ti is None:
                continue
            ok = ti >= sig + 1
            dt = RF.det2(rt[0], rt[1])
            tally[("G2det", ok, dt)] = tally.get(("G2det", ok, dt), 0) + 1

            ps = pieces_cached(rt)
            npc = len(ps)
            tally[("pieces", dt, npc)] = \
                tally.get(("pieces", dt, npc), 0) + 1
            oi = occupied(ps, win)
            if oi is None:
                tally["seam"] = tally.get("seam", 0) + 1
                continue
            occ_idx = RF.intrinsic_index(ps[oi], fcyls)
            occ_ok = occ_idx is not None and occ_idx >= sig + 1
            # Q3's kill, as an observable: the occupied piece SHORT.
            tally[("occ", dt, occ_ok)] = \
                tally.get(("occ", dt, occ_ok), 0) + 1
            if not occ_ok:
                tally.setdefault("occ-short-spec", []).append(
                    (fdigs[:8], P, pc, n, dt, occ_idx, sig))
            # Q3's second half: G2 against the UNOCCUPIED conjunction.
            un = True
            offenders = []
            for i, p in enumerate(ps):
                if i == oi:
                    continue
                pi = RF.intrinsic_index(p, fcyls)
                if pi is None or pi < sig + 1:
                    un = False
                    offenders.append(p)
            tally[("unocc", dt, ok, un)] = \
                tally.get(("unocc", dt, ok, un), 0) + 1
            # Q4: which boundary of C_{sigma+1} each offender crosses.
            # PER PIECE and not per door: a three-piece reference has
            # two unoccupied pieces and both can fail, so recording
            # only the first would report a left-to-right tie-break as
            # a fact. At determinant 2 there is exactly one unoccupied
            # piece and the two readings coincide.
            if offenders and sig + 1 >= len(fcyls):
                tally[("side-horizon", dt)] = \
                    tally.get(("side-horizon", dt), 0) + 1
            for offender in (offenders if sig + 1 < len(fcyls) else []):
                A = fcyls[sig + 1]
                if flt(v, A[0]):
                    near_v, far_v = A[0], A[1]
                    tv = flt(offender[0], near_v)
                    fv = flt(far_v, offender[1])
                elif flt(A[1], v):
                    near_v, far_v = A[1], A[0]
                    tv = flt(near_v, offender[1])
                    fv = flt(offender[0], far_v)
                else:
                    tally["v-inside"] = tally.get("v-inside", 0) + 1
                    continue
                tally[("side", dt, tv, fv)] = \
                    tally.get(("side", dt, tv, fv), 0) + 1


def scan(name, tally, pref):
    for alpha, hh in RF.SCANS:
        for digs in itertools.product(alpha, repeat=hh):
            fam = RF.build_family(name, digs)
            if fam is None:
                continue
            refs, fdigs, fcvs, fcyls = fam
            win = tail_window(refs, fcyls)
            if win is None:
                tally["no-win"] = tally.get("no-win", 0) + 1
                continue
            ridx = [RF.intrinsic_index(iv, fcyls) for iv in refs]
            for P, pc in RF.RUNS:
                walk(refs, ridx, fcvs, fdigs, fcyls, P, pc,
                     pref[0], pref[1], win, tally)


# ----------------------------------------------------------------- #
# E1  the gates                                                      #
# ----------------------------------------------------------------- #

def e1_gates():
    print("\nE1  THE GATES")

    # K0: D1's floor, brute-forced. Derived on paper above and not
    # found stated in the sources read, so it carries its own control.
    d1box = d1bad = 0
    for b in range(1, 13):
        for d in range(1, 13):
            for a in range(0, 13):
                for c in range(0, 13):
                    if b * c - a * d != 1:
                        continue
                    d1box += 1
                    if least_interior_denominator(((a, b), (c, d))) \
                            != b + d:
                        d1bad += 1
    print("  K0 determinant-1 box: %d intervals, %d whose least "
          "interior denominator is not b + d" % (d1box, d1bad))
    check("K0 (D1) the interior fraction of least denominator across "
          "a determinant-1 interval is the mediant, at denominator "
          "exactly b + d", d1box > 0 and d1bad == 0)

    # K3 / Q1: the box control on D2.
    box = bad = 0
    seam_bad = floor_bad = min_bad = 0
    for b in range(1, 13):
        for d in range(1, 13):
            for a in range(0, 13):
                for c in range(0, 13):
                    if RF.reduce_frac((a, b)) != (a, b):
                        continue
                    if RF.reduce_frac((c, d)) != (c, d):
                        continue
                    if b * c - a * d != 2:
                        continue
                    box += 1
                    J = ((a, b), (c, d))
                    ps = pieces(J)
                    if len(ps) != 2:
                        bad += 1
                        continue
                    m = ps[0][1]
                    if m != ((a + c) // 2, (b + d) // 2):
                        seam_bad += 1
                    qm = (b + d) // 2
                    if least_interior_denominator(J) != qm:
                        floor_bad += 1
                    # UNIQUENESS AT THE MINIMUM, which the prose
                    # claims and this box is the only control on. Not
                    # uniqueness below b + d: that is false, and
                    # (0/1, 2/5) is the specimen (D2).
                    at_min = [(p, qm) for p in range(0, 13 * qm + 1)
                              if flt(J[0], (p, qm)) and flt((p, qm), J[1])]
                    if at_min != [m]:
                        min_bad += 1
    print("  K3 determinant-2 box: %d intervals, %d not two-piece, "
          "%d wrong seam, %d wrong interior floor, %d with a second "
          "fraction at the minimum" % (box, bad, seam_bad, floor_bad,
                                       min_bad))
    check("K3 (Q1) every determinant-2 interval is two tree cells "
          "glued at the half-mediant, the ONLY interior fraction at "
          "the least denominator, which is exactly half the "
          "determinant-1 floor",
          box > 0 and bad == 0 and seam_bad == 0 and floor_bad == 0
          and min_bad == 0)

    # K1: the decomposition is a decomposition, over the corpus's own
    # references rather than a box.
    seen = tiled = 0
    for name in RF.FAMILIES:
        for alpha, hh in RF.SCANS:
            for digs in itertools.product(alpha, repeat=hh):
                fam = RF.build_family(name, digs)
                if fam is None:
                    continue
                for iv in fam[0]:
                    if iv in PIECE_CACHE:
                        continue
                    seen += 1
                    ps = pieces_cached(iv)
                    if contiguous(iv, ps):
                        tiled += 1
    print("  K1 references decomposed %d, tiling exactly %d"
          % (seen, tiled))
    check("K1 the pieces tile every reference exactly, each of "
          "determinant 1", seen > 0 and tiled == seen)


PARENT_G2 = {(True, 1): 568195, (False, 1): 0,
             (True, 2): 14939, (False, 2): 73354,
             (True, 3): 18735, (False, 3): 65377}


def e1_reproduction(tally):
    print("\n  K2  THE REPRODUCTION GATE")
    got = {}
    for k, vv in tally.items():
        if isinstance(k, tuple) and k[0] == "G2det":
            got[(k[1], k[2])] = vv
    for key in sorted(PARENT_G2, key=str):
        print("    |det|=%d G2 %-5s  parent %7d  here %7d"
              % (key[1], "holds" if key[0] else "FAILS",
                 PARENT_G2[key], got.get(key, 0)))
    ok = all(got.get(k, 0) == v for k, v in PARENT_G2.items())
    check("K2 this rig's own walk reproduces the parent's "
          "G2-per-determinant table exactly", ok)


# ----------------------------------------------------------------- #
# E2, E3  the separator                                              #
# ----------------------------------------------------------------- #

def e2_separator(tally):
    print("\nE2  THE SEPARATOR")

    print("\n  PIECE COUNT BY DETERMINANT (Q1 realized, Q2):")
    dets = sorted(set(k[1] for k in tally
                      if isinstance(k, tuple) and k[0] == "pieces"))
    for d in dets:
        row = sorted((k[2], v) for k, v in tally.items()
                     if isinstance(k, tuple) and k[0] == "pieces"
                     and k[1] == d)
        print("    |det|=%d  %s" % (d, ", ".join("%d pieces: %d" % r
                                                 for r in row)))
    two_only = all(k[2] == 2 for k in tally
                   if isinstance(k, tuple) and k[0] == "pieces"
                   and k[1] == 2)
    check("Q1 every determinant-2 door is opened by a two-piece "
          "reference", two_only)
    d3 = set(k[2] for k in tally
             if isinstance(k, tuple) and k[0] == "pieces" and k[1] == 3)
    print("  Q2 determinant-3 piece counts realized: %s"
          % sorted(d3))

    print("\n  THE OCCUPIED PIECE (Q3's kill):")
    short = 0
    for d in dets:
        good = tally.get(("occ", d, True), 0)
        bad = tally.get(("occ", d, False), 0)
        short += bad
        print("    |det|=%d  reaches sigma+1: %7d   SHORT: %d"
              % (d, good, bad))
    for s in tally.get("occ-short-spec", [])[:3]:
        print("    SPECIMEN occupied-short %s" % (s,))
    check("Q3a the piece of the opening reference that contains the "
          "point reaches sigma+1 at every door, every determinant",
          short == 0)

    print("\n  G2 AGAINST THE UNOCCUPIED CONJUNCTION (Q3):")
    print("    %-8s %10s %10s %10s %10s"
          % ("|det|", "G2 & un", "G2 & !un", "!G2 & un", "!G2 & !un"))
    off = 0
    for d in dets:
        a = tally.get(("unocc", d, True, True), 0)
        b = tally.get(("unocc", d, True, False), 0)
        c = tally.get(("unocc", d, False, True), 0)
        e = tally.get(("unocc", d, False, False), 0)
        off += b + c
        print("    %-8d %10d %10d %10d %10d" % (d, a, b, c, e))
    check("Q3b the G2 verdict at a door equals the conjunction over "
          "the pieces the point does not occupy, at every "
          "determinant", off == 0)

    if tally.get("seam"):
        print("  ambiguous doors (a seam runs through the tail window, "
              "so no piece is the occupied one): %d" % tally["seam"])
    if tally.get("no-win"):
        print("  streams whose finest reference and finest cylinder do "
              "not meet: %d" % tally["no-win"])
    if tally.get("v-inside"):
        print("  doors with the vertex inside C_sigma+1: %d"
              % tally["v-inside"])


def e3_boundary(tally):
    print("\nE3  WHICH BOUNDARY THE OFFENDER CROSSES (Q4)")
    print("  Counted per offending PIECE, not per door: a three-piece")
    print("  reference has two unoccupied pieces and both can fail.")
    print("  At determinant 2 there is exactly one, so the two")
    print("  readings coincide there.")
    print("    %-8s %12s %12s %12s"
          % ("|det|", "toward v", "away only", "both"))
    dets = sorted(set(k[1] for k in tally
                      if isinstance(k, tuple) and k[0] == "side"))
    tv2 = tot2 = 0
    for d in dets:
        both = tally.get(("side", d, True, True), 0)
        tv = tally.get(("side", d, True, False), 0)
        fv = tally.get(("side", d, False, True), 0)
        none = tally.get(("side", d, False, False), 0)
        if none:
            print("    |det|=%d  %d offenders crossing NEITHER "
                  "boundary" % (d, none))
        print("    %-8d %12d %12d %12d" % (d, tv, fv, both))
        if d == 2:
            tv2, tot2 = tv + both, tv + fv + both + none
    if tot2:
        print("  Q4 at determinant 2: %d of %d failing doors have the "
              "offender crossing the vertex-side boundary (%.1f%%)"
              % (tv2, tot2, 100.0 * tv2 / tot2))
    hz = sorted((k[1], v) for k, v in tally.items()
                if isinstance(k, tuple) and k[0] == "side-horizon")
    if hz:
        print("  doors with an offender but no C_sigma+1 inside the "
              "read horizon, excluded above: %s"
              % ", ".join("|det|=%d: %d" % r for r in hz))


def main():
    os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")
    print("WHAT SEPARATES A DETERMINANT-2 REFERENCE THAT RESPECTS G2")
    print("scans: %s" % (RF.SCANS,))
    print("families: %s" % (RF.FAMILIES,))
    e1_gates()
    if FAILURES:
        print("\nGATE FAILED -- no verdicts from any later leg.")
        return 1
    tally = {}
    for name in RF.FAMILIES:
        for pref in (RF.CHAIN_PREF, RF.TREE_PREF):
            scan(name, tally, pref)
    e1_reproduction(tally)
    if FAILURES:
        print("\nGATE FAILED -- no verdicts from any later leg.")
        return 1
    e2_separator(tally)
    e3_boundary(tally)
    print("\n%d checks failed" % len(FAILURES))
    for f in FAILURES:
        print("  FAIL %s" % f)
    return 1 if FAILURES else 0


if __name__ == "__main__":
    sys.exit(main())
