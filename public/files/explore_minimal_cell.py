"""THE MINIMAL CELL: what the doubly pinned reader actually commits to.

THE QUESTION
------------
The reader corpus's open edge is the nesting half of the floor lemma:
from any member of any off-bottom finite-loss class, the doubly pinned
policy of that member's own style pair commits, at every counted step,
inside the cell that member's class commits to (measured at 102,092 of
102,092 members over the census scope, explore_pinned_freshening.py E8).
The parent left it measured and unproved, and named as the cheapest
probe the question of whether the doubly pinned run is HISTORY-FREE.
This rig carries a derivation that answers more than the probe, and its
job is to verify each load-bearing step of that derivation over the
census scope.

THE NAMED CLASS (imported verbatim)
-----------------------------------
Cover, streams and the commit loop are the parents'
(explore_scale_clock.py, explore_stall_assembly.py,
explore_stall_maprate.py, explore_shift_telescope.py). UNRESOURCED
throughout: drawdown inert, the 100 policies of the unresourced axis,
counted window starting at step 8, patience axis 0, 1, 2, 3, INF, where
0 reads the current image and INF refuses the reference. The population
is the parents' census scope: horizons 9, 10, 12, 16, maps identity and
doubling, MR.census_pool at each horizon.

WHOSE VOCABULARY THIS IS WRITTEN IN
-----------------------------------
The COVER's, and deliberately not the quotient's and not the commit
loop's. The parent asked its questions about routes -- which candidate a
run had and which it took -- and every one of them came back saying the
route does not decide the answer. So the object here is the CELL as a
geometric thing: a Stern-Brocot interval carrying a straddle index. The
quotient never appears below; neither does a class, a loss or a rank.
TRANSPLANT, flagged: nothing is imported from the diagonal shift
telescope or from the pinned freshening walk. Both are statements about
comparing two runs, and the derivation below compares a run against a
CONSTRUCTION that no run performs.

HAND-ATTACK (fixed before the engine; the design follows it)
------------------------------------------------------------
G-A THE CELLS ARE ONE FAMILY. A T cell ("T", l, r, d) and an S cell
("S", v, l, r, d, k) are the single object (l, r, k) with v = l + r and
interval S_k(l,r) = (l + kv, r + kv); the T cell is k = 0, and the S
cell's own k >= 1. Read that way the two moves are uniform: CHAIN
replaces k by chain_kmax(v, l, r, ref_c), legal when that exceeds k;
TREE splits the CURRENT interval at v into (l + kv, v) and (v, r + kv)
and takes whichever strictly contains ref_t. This is the commit loop
verbatim -- from a T cell the children are (l, v) and (v, r), which is
the k = 0 case of the same formula, and from an S cell the loop's own
children are built from interval(C), which is (l + kv, r + kv).

G-B EVERY INTERVAL A RUN HOLDS IS A STERN-BROCOT INTERVAL. det(l + kv,
v) = det(l, v) = det(l, r), so a tree move from a straddle produces a
unimodular pair, and (l + kv, v) is the k-fold right descendant of
(l, v): the tree move from S_k is an ordinary Stern-Brocot descent, just
k + 1 levels of it at once. ROOT is unimodular, so by induction every
cell is (SB interval, straddle index).

G-C TERMINATION IS A PROPERTY OF THE REFERENCES ALONE. The loop breaks
exactly when no child strictly contains ref_t and k = chain_kmax(ref_c).
For the DOUBLY PINNED policy both references are J[n], so the break
condition reads: the current SB interval is one no child of which
strictly contains J[n], and the straddle index is maximal for J[n].

G-D THE CANONICAL CELL. SB intervals strictly containing a fixed J form
a CHAIN -- the Stern-Brocot family is laminar -- and J has positive
length, so the chain is finite and has a deepest member I*(J). Define
M(J) = (I*(J), kmax(I*(J), J)). By G-C the doubly pinned loop started
from ANY cell strictly containing J -- which forces both I* inside the
base pair and the index at or below that pair's kmax -- terminates at
exactly M(J): it can only stop at I*, and only at the maximal index
there. So the doubly pinned run is history-free AND style-free -- the
style pair orders the route and nothing else, and M(J) is a function of
J alone, computable with no policy and no loop.

G-E THE CANONICAL CELL IS THE MINIMUM. Let C = (I, k) be the cell ANY
policy holds at step n. Every move that built it required strict
containment of a reference containing J[n], so I strictly contains J[n]
and k <= kmax(I, J[n]). By the chain, I* is inside I. If I = I*, then
k <= kmax and S_kmax is inside S_k. If I* is strictly inside I, then
J[n] cannot straddle v -- if it did, no SB interval below I would
contain it and I* would BE I -- so J[n] lies strictly inside one of the
two children (l + kv, v), (v, r + kv) of S_k, that child is an SB
interval strictly containing J[n], hence I* is inside it, hence inside
S_k. Either way M(J[n]) is inside C.

G-F WHAT THAT SETTLES. C*_n = M(J[n]) is inside C^q_n for every policy
q, every style pair, every step -- counted or not, any class, any
patiences. The floor lemma's nesting half is the counted-window, same-
style, off-bottom corner of it, and the improving half is already
derived from nesting alone (explore_pinned_freshening.py C1). The
parent's probe (is the doubly pinned run history-free) is answered YES
and is not needed: G-E never mentions a start.

PREDICTIONS, fixed before the engine ran
----------------------------------------
Q0 [positive control, run first] The local traced runner reproduces
   SC.run_reader's trace -- rank, chain index and interval at every
   step -- for every policy on every stream in the population. A miss
   means the engine is not the parents' and no verdict below is read
   (K1). NEGATIVE control, run with it: over the horizon-9 doubling
   pool, the 25 policies of style (0,0) are pairwise INCOMPARABLE at
   some step. Zero means the containment test cannot print False and no
   verdict below is read (K2).
Q1 [history- and style-freeness] At every stream and every step, the
   four doubly pinned policies (st, ss, 0, 0) hold the SAME cell
   (l, r, k). Observable: the count of steps where any two differ, and
   the first. Reported alongside: whether their RANKS agree, which the
   derivation does not claim -- rank counts the route, and G-D says the
   route is what is free.
Q2 [the canonical form] At every stream and every step, the doubly
   pinned cell equals M(J[n]) as built by a direct Stern-Brocot descent
   that runs no policy and no commit loop. Observable: mismatches, and
   the first.
Q3 [the minimum] At every stream, every one of the 100 policies and
   every step, the doubly pinned cell's interval is inside that
   policy's. Observable: failures split by map, the first anatomy, and
   -- as a scale reading, not a verdict -- how often the containment is
   PROPER rather than equality.
Q4 [the structure lemma, wired hard] Every cell held by every policy at
   every step is (I, k) with I unimodular, I strictly containing J[n],
   k <= chain_kmax(I, J[n]), and I* inside I. This is G-B and the first
   sentence of G-E, so it is a derivation and not a guess: a failure is
   a hole in the proof, not a surprise about the population.
Q5 [strictness] Every committed cell STRICTLY contains the current
   image at every step. G-E leans on this; the commit loop only asserts
   non-strict containment, so the strict form is measured and not
   assumed.

KILL CRITERIA (observables; the meaning is weighed after the run)
----------------------------------------------------------------
K1 Any Q0 trace mismatch. The engine is not the parents' and nothing
   below is a verdict.
K2 The Q0 negative control finds zero incomparable pairs. The
   instrument cannot print False and nothing below is a verdict.
K3 Any Q3 failure. The minimum claim is false in this cover, G-E is
   wrong, and the floor lemma keeps its measured-only standing.
K4 Any Q1 or Q2 mismatch. G-D is wrong: the doubly pinned terminal
   depends on the route or the history after all, and the proof's
   collapse does not happen even if Q3 holds.
K5 Any Q4 or Q5 violation. The structure the whole derivation is
   written on does not hold in this cover.

ENGINE
------
E1 the controls (Q0), positive then negative.
E2 the census sweep: for every stream, every policy and every step,
   Q1 through Q5 at once (Q1, Q2 and Q5 once per step; Q3 and Q4 once
   per policy-step).
Exact big-integer arithmetic for every verdict; no floating point
anywhere. Sequential; estimated run a few minutes, the 100-policy sweep
over 1,468 stream-instances the driver; memory trivial (no BLAS
import); exit nonzero on any check failure.

FINDINGS (entered after the run; ALL CHECKS PASS, exit 0, 11.3 s,
14.1 MB peak under the memory watch)
----------------------------------------------------------------
F1 THE CONTROLS. The traced runner reproduces SC.run_reader at 0
   mismatches over 146,800 policy-runs, and the containment test prints
   False readily: of 46,800 style-(0,0) policy pairs on the horizon-9
   doubling pool, 5,261 are INCOMPARABLE at some step (first: hp1,
   (0,0,1,0) against (0,0,1,1), step 4). Neither kill fires.
F2 THE DOUBLY PINNED CELL IS A FUNCTION OF THE IMAGE. Over 17,892
   stream-steps the four doubly pinned policies hold the same cell at
   every one, and it equals M(J[n]) -- built by a Stern-Brocot descent
   that runs no policy and no commit loop -- at every one. Their RANKS
   agree too, which G-D does not claim and which the print gives for
   free: not only the terminal but the route length is style-free here.
F3 THE STRUCTURE THE PROOF STANDS ON HOLDS EXACTLY. Over 1,789,200
   policy-steps: every committed cell is (unimodular pair, straddle
   index), every base pair STRICTLY contains the current image, no
   index exceeds that pair's kmax, and I* sits inside every base pair.
   Zero violations of any of the four, and zero policy-steps where a
   committed cell contains the image only non-strictly -- so G-E's
   strictness lean is real in this cover and not an assumption.
F4 THE MINIMAL CELL THEOREM. At 894,600 of 894,600 doubling and 894,600
   of 894,600 identity policy-steps the doubly pinned cell is inside the
   policy's -- every policy, every style pair, every step, counted or
   not, no class scoping anywhere -- and it is PROPERLY inside at
   759,156 doubling and 695,360 identity of them; the rest are
   equalities, of which 35,784 per map are the four doubly pinned
   policies meeting themselves. With G-D and G-E this is a proof and
   not a census: the
   doubly pinned run commits to the canonical minimal cell of the
   current image, which no other policy can be inside because every
   policy's cell is a Stern-Brocot interval strictly containing that
   image carrying an admissible straddle index. The floor lemma's
   nesting half is the counted-window, same-style, off-bottom corner of
   it; the improving half already follows from nesting
   (explore_pinned_freshening.py C1); so the floor lemma is a theorem
   and the parent's history-freeness probe is answered YES and is not
   needed -- G-E never mentions a start.
F5 THE OPEN EDGE WAS NOT OPEN, AND THE PROOF SAT IN THE NEIGHBOURING
   SECTION OF THE SAME DOC. The BOTTOM LEMMA (explore_bootstrap_cures.py,
   proved) already carries corollary (ii) verbatim: any policy's
   committed cell contains its references, which contain the current
   image, which the containing sub-poset's inclusion MINIMUM sits inside
   -- so greedy patience dominates every policy at every step in ANY
   policy space of this family. That IS the floor lemma's nesting half,
   unscoped, and it was proved before the pinned residue thread began.
   Two readings let the threads pass each other: the bottom lemma was
   read as a statement about the LOSS at one style pair when its
   corollary is about CELLS at every style pair, and its minimum was
   read as something greedy REACHES rather than as a bound on every
   containing cell. What survives as this rig's own is the CLOSED FORM
   the bottom lemma does not give: the Newman argument proves bottom(R)
   exists and is unique without naming it, and G-D names it --
   bottom(R) = M(R), the deepest Stern-Brocot interval strictly
   containing R at its maximal straddle index, computable with no
   policy, no route and no commit loop, matching the run at 17,892 of
   17,892 steps. So the floor lemma is a corollary of the bottom lemma,
   the doubly pinned run's cell is M(J[n]), and the rest of this rig is
   a second independent proof of a theorem the corpus already held.
"""

import os
os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")

import sys

import explore_scale_clock as SC
import explore_stall_maprate as MR
import explore_shift_telescope as TS

FAILURES = []

def check(name, ok):
    print("  [%s] %s" % ("PASS" if ok else "FAIL", name))
    if not ok:
        FAILURES.append(name)

POLICIES = [(st, ss, pt, pc)
            for st in (0, 1) for ss in (0, 1)
            for pt in SC.AX_BASE for pc in SC.AX_BASE]

FLOORS = [(st, ss, 0, 0) for st in (0, 1) for ss in (0, 1)]

# ----------------------------------------------------------------- #
# the instrumented reader: SC.run_reader verbatim, keeping the cell
# ----------------------------------------------------------------- #

def run_cells(J_list, policy, horizon):
    """Committed cell object at every step."""
    s_t, s_s, pt, pc = policy
    C = SC.ROOT
    cells = []
    for n in range(horizon):
        ref_t = J_list[n - pt] if pt is not None and n - pt >= 0 else None
        ref_c = J_list[n - pc] if pc is not None and n - pc >= 0 else None
        while True:
            cand_tree = cand_chain = None
            if C[0] == "T":
                _, l, r, d = C
                v = SC.mediant(l, r)
                if ref_t is not None:
                    for ch in (("T", l, v, d + 1), ("T", v, r, d + 1)):
                        if SC.contains(ch, ref_t):
                            cand_tree = ch
                            break
                if ref_c is not None:
                    k = SC.chain_kmax(v, l, r, ref_c)
                    if k >= 1:
                        cand_chain = ("S", v, l, r, d, k)
                prefer_chain = (s_t == 1)
            else:
                _, v, l, r, d, k = C
                if ref_c is not None:
                    k2 = SC.chain_kmax(v, l, r, ref_c)
                    if k2 > k:
                        cand_chain = ("S", v, l, r, d, k2)
                if ref_t is not None:
                    mL, mR = SC.interval(C)
                    for ch in (("T", mL, v, d + k + 1),
                               ("T", v, mR, d + k + 1)):
                        if SC.contains(ch, ref_t):
                            cand_tree = ch
                            break
                prefer_chain = (s_s == 0)
            if cand_tree is None and cand_chain is None:
                break
            if cand_chain is not None and (cand_tree is None
                                           or prefer_chain):
                C = cand_chain
            else:
                C = cand_tree
        cells.append(C)
    return cells

def key_of(C):
    """The cell as (l, r, k): the base pair and the straddle index."""
    if C[0] == "T":
        return (C[1], C[2], 0)
    return (C[2], C[3], C[5])

def minimal_cell(J):
    """M(J): the deepest Stern-Brocot interval strictly containing J,
    carrying its maximal straddle index. No policy, no commit loop."""
    l, r = SC.ROOT[1], SC.ROOT[2]
    while True:
        v = SC.mediant(l, r)
        if SC.contains(("T", l, v, 0), J):
            r = v
        elif SC.contains(("T", v, r, 0), J):
            l = v
        else:
            break
    return (l, r, SC.chain_kmax(SC.mediant(l, r), l, r, J))

def det(l, r):
    return r[0] * l[1] - l[0] * r[1]

def inside(a, b):
    """Interval a inside interval b, endpoints allowed."""
    return TS.frac_le(b[0], a[0]) and TS.frac_le(a[1], b[1])

def incomparable(a, b):
    return not inside(a, b) and not inside(b, a)

def population():
    for horizon in TS.CENSUS_HORIZONS:
        for mp in TS.CENSUS_MAPS:
            for wname, digs in MR.census_pool(horizon):
                J = SC.images(SC.cylinders(list(digs)), mp)[:horizon]
                yield horizon, mp, wname, J

# ----------------------------------------------------------------- #
# E1: the controls
# ----------------------------------------------------------------- #

def e1_controls():
    print("\nE1  THE CONTROLS")
    bad = 0
    first = None
    n_pol = 0
    for horizon, mp, wname, J in population():
        for p in POLICIES:
            cells = run_cells(J, p, horizon)
            tr = SC.run_reader(J, p, horizon)[3]
            n_pol += 1
            for n in range(horizon):
                C = cells[n]
                row = (SC.rank(C), C[5] if C[0] == "S" else 0,
                       SC.interval(C))
                if row != tr[n]:
                    bad += 1
                    if first is None:
                        first = (mp, horizon, wname, p, n)
    print("  positive: %d policy-runs against SC.run_reader, %d step "
          "mismatches" % (n_pol, bad))
    if first:
        print("    first mismatch: %s" % (first,))
    check("Q0 positive control: the traced runner is the parents'",
          bad == 0)

    pairs = 0
    seen_inc = 0
    first_inc = None
    style00 = [p for p in POLICIES if p[0] == 0 and p[1] == 0]
    for horizon, mp, wname, J in population():
        if horizon != 9 or mp != "dbl":
            continue
        cells = {p: run_cells(J, p, horizon) for p in style00}
        for i, p in enumerate(style00):
            for q in style00[i + 1:]:
                pairs += 1
                for n in range(horizon):
                    a = SC.interval(cells[p][n])
                    b = SC.interval(cells[q][n])
                    if incomparable(a, b):
                        seen_inc += 1
                        if first_inc is None:
                            first_inc = (wname, p, q, n)
                        break
    print("  negative: %d style-(0,0) policy pairs on the h=9 dbl pool, "
          "%d incomparable somewhere" % (pairs, seen_inc))
    if first_inc:
        print("    first incomparable pair: %s" % (first_inc,))
    check("Q0 negative control: the containment test can print False",
          seen_inc > 0)

# ----------------------------------------------------------------- #
# E2: the census sweep
# ----------------------------------------------------------------- #

def e2_sweep():
    print("\nE2  THE CENSUS SWEEP (Q1-Q5 over every policy and step)")
    q1_bad = q2_bad = q5_bad = 0
    q1_rank_bad = 0
    q3_bad = {}
    q3_ok = {}
    q3_proper = {}
    q4_bad = [0, 0, 0, 0]
    firsts = {}
    steps = 0
    polsteps = 0
    for horizon, mp, wname, J in population():
        cells = {p: run_cells(J, p, horizon) for p in POLICIES}
        for n in range(horizon):
            steps += 1
            Jn = J[n]
            fl = [cells[p][n] for p in FLOORS]
            keys = set(key_of(C) for C in fl)
            if len(keys) != 1:
                q1_bad += 1
                firsts.setdefault("Q1", (mp, horizon, wname, n, keys))
            if len(set(SC.rank(C) for C in fl)) != 1:
                q1_rank_bad += 1
            fkey = key_of(fl[0])
            mk = minimal_cell(Jn)
            if mk != fkey:
                q2_bad += 1
                firsts.setdefault("Q2", (mp, horizon, wname, n, fkey, mk))
            fiv = SC.interval(fl[0])
            istar = (mk[0], mk[1])
            for p in POLICIES:
                polsteps += 1
                C = cells[p][n]
                l, r, k = key_of(C)
                iv = SC.interval(C)
                if not SC.contains(("T", iv[0], iv[1], 0), Jn):
                    q5_bad += 1
                    firsts.setdefault("Q5", (mp, horizon, wname, n, p))
                if det(l, r) != 1:
                    q4_bad[0] += 1
                    firsts.setdefault("Q4a", (mp, horizon, wname, n, p))
                if not SC.contains(("T", l, r, 0), Jn):
                    q4_bad[1] += 1
                    firsts.setdefault("Q4b", (mp, horizon, wname, n, p))
                elif k > SC.chain_kmax(SC.mediant(l, r), l, r, Jn):
                    q4_bad[2] += 1
                    firsts.setdefault("Q4c", (mp, horizon, wname, n, p))
                if not inside((istar[0], istar[1]), (l, r)):
                    q4_bad[3] += 1
                    firsts.setdefault("Q4d", (mp, horizon, wname, n, p))
                if inside(fiv, iv):
                    q3_ok[mp] = q3_ok.get(mp, 0) + 1
                    if iv != fiv:
                        q3_proper[mp] = q3_proper.get(mp, 0) + 1
                else:
                    q3_bad[mp] = q3_bad.get(mp, 0) + 1
                    firsts.setdefault("Q3", (mp, horizon, wname, n, p,
                                             fiv, iv))
        del cells
    print("  swept %d stream-steps and %d policy-steps" % (steps, polsteps))
    print("  Q1 the four doubly pinned cells differ at %d of %d steps "
          "(ranks differ at %d)" % (q1_bad, steps, q1_rank_bad))
    print("  Q2 the doubly pinned cell is not M(J[n]) at %d of %d steps"
          % (q2_bad, steps))
    print("  Q5 a committed cell fails to strictly contain the image at "
          "%d of %d policy-steps" % (q5_bad, polsteps))
    print("  Q4 violations: non-unimodular %d, base pair not strictly "
          "containing %d, index over kmax %d, I* not inside %d"
          % tuple(q4_bad))
    for mp in sorted(set(list(q3_ok) + list(q3_bad))):
        ok, bad = q3_ok.get(mp, 0), q3_bad.get(mp, 0)
        print("  Q3 %-3s: the doubly pinned cell nests at %d of %d "
              "policy-steps (%d of them properly)"
              % (mp, ok, ok + bad, q3_proper.get(mp, 0)))
    for tag in sorted(firsts):
        print("    first %s: %s" % (tag, firsts[tag]))
    check("Q1 the doubly pinned cell is style-free", q1_bad == 0)
    check("Q2 the doubly pinned cell is M(J[n])", q2_bad == 0)
    check("Q3 the doubly pinned cell is the minimum",
          sum(q3_bad.values()) == 0)
    check("Q4 the structure lemma", sum(q4_bad) == 0)
    check("Q5 every committed cell strictly contains the image",
          q5_bad == 0)

# ----------------------------------------------------------------- #

def main():
    e1_controls()
    if FAILURES:
        print("\nCONTROLS FAILED -- no verdicts read")
        print("FAILURES: %s" % FAILURES)
        return 1
    e2_sweep()
    if FAILURES:
        print("\nFAILURES: %s" % FAILURES)
        return 1
    print("\nALL CHECKS PASS")
    return 0

if __name__ == "__main__":
    sys.exit(main())
