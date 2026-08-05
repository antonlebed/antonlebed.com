"""THE UNRESOURCED CELL: stall-free by law, or by a tame battery?

THE QUESTION
------------
The reader-descent corpus's blindness table closes on a dichotomy
(explore_stall_tie.py): the "every stall is a tie" conjecture is a
THEOREM on the single-reference spine (pt = pc, unresourced) and
FALSE off it under a binding budget, where the burst trap is a
strict local minimum. One cell of that shape is unsettled — the
UNRESOURCED space OFF the spine. It measured zero stalls in all
112 unresourced landscapes of the parent battery, and the raw
material for traps is demonstrably present there: 8437 non-nested
(policy, step) counts at mixed patience with no budget anywhere
(explore_stall_tie.py F3). So either a second route to the theorem
runs through that cell, or the battery was too tame to leave the
desert.

The spine theorem's proof runs on NESTING (L1/L2 of the parent:
references shrink, so committed cells nest pointwise and the
deficit descends strictly). Off the spine that lemma is measured
DEAD. This rig asks what replaces it.

THE NAMED CLASS (unchanged, imported verbatim)
----------------------------------------------
Cover, streams, policies, losses, moves and quotient are the
parent's: the mediant-straddle cover of the CF window, policies
(s_t, s_s, pt, pc, delta) with patience axis {0,1,2,3,INF}, the
exact lexicographic deficit over counted steps, the cure move set
(single coordinate steps plus the route diagonal), the quotient by
counted-window committed-cell trace. UNRESOURCED throughout: the
four-coordinate reader, delta inert, one delta class, so the
policy space is 100 policies and the cure graph carries the two
route moves and the diagonal but no drawdown move.

HAND-ATTACK (fixed before the engine; the proofs are the design)
----------------------------------------------------------------
L1 (THE CONSERVATION ASYMMETRY — what a budget BUYS). Under a
   budget the commit loop is CUT at the spendable rank units and
   the unspent remainder banks: bank = min(cap, avail - spent).
   The budget is therefore a CONSERVED quantity, and spending it
   at step n REMOVES capacity at step n+1 — a NEGATIVE coupling
   between steps. The burst trap's whole mechanism is exactly a
   negative coupling realized: pay a little early to win a lot
   late, a trade every single move breaks. Unresourced, the loop
   runs to EXHAUSTION at every step — there is no conserved
   quantity and nothing to remove. The only cross-step channel
   left is the ratchet state C, and the ratchet is POSITIVE:
   C_{n+1} is a subset of C_n always, so a finer state is never
   paid for. The budget's role as a design variable is thus
   precisely NEGATIVE INTER-STEP COUPLING, and the question this
   rig asks is whether an unresourced world can rent one.

L2 (THE ROUTE LEMMA — the one candidate channel, and the engine's
   target). Refinement targets are MONOTONE in patience: lowering
   pc gives a newer, hence smaller, ref_c, so chain_kmax is weakly
   larger; lowering pt gives a smaller ref_t, so a tree child
   containing it exists at least as deep. Consider a commit loop
   in which at no iteration do BOTH candidates exist (call the
   step FORCED). Then the loop has no choice at any iteration: the
   fixed point is a function of the start and the reference alone,
   and it is monotone in the reference. Hence, along a
   patience-down move, forced steps NEST — and a nested trace is
   the spine proof's hypothesis, which delivers strict deficit
   descent and no stall. THEREFORE every unresourced non-nested
   step must trace to a step where both candidates coexisted and
   the two runs took different branches: A ROUTE FLIP. That is the
   whole unresourced negative channel, if L1 is right that the
   ratchet is the only other one.

L3 (WHERE THE CURE GRAPH THEN COVERS IT — and the designed hole).
   The cure set CONTAINS both route moves and the route diagonal.
   A stall born of a route flip is therefore one move from its
   own cure — unless a single world needs OPPOSITE route settings
   at two different steps, since the route is two GLOBAL bits and
   cannot be scheduled. That is the designed target of the forge:
   two demand bursts at a separation matched to the patience gap
   |pt - pc|, so that one burst is seen by ref_t while the other
   is seen by ref_c and the two steps want opposite routes. The
   parent battery contains no such world — its spike streams carry
   exactly ONE spike — which is the specific way it may have been
   tame.

L4 (TRANSPLANT, flagged as such). "Burst" is imported from the
   budgeted trap, where a burst binds a budget. Unresourced there
   is no budget for it to bind, so the transplanted object is NOT
   the trap's burst: here a large CF digit is a long chain run,
   i.e. a ROUTE PHASE. The import is the shape (a localized
   demand feature at a designed offset), never the mechanism.

L5 (the control's own hazard, from the parent's audit history). A
   check quantified over pairs that are almost never forced would
   PASS vacuously. C2 therefore gates on the SIZE of the tested
   set as well as its exception count, and reports UNTESTED rather
   than PASS below the stated floor.

PREDICTIONS, fixed before the engine ran
----------------------------------------
C1 [controls, gate]
   (i)  The instrumented reader of this rig reproduces
        SC.run_reader exactly — loss triple and full trace — on
        the nine parent rows across all 100 unresourced policies
        at horizon 120.
   (ii) This rig's census reproduces the parent's unresourced
        result on the parent battery's unresourced slice: ZERO
        stalls in all 112 landscapes.
C2 [THE ROUTE LEMMA'S ENGINE LEG — predicted PASS] Unresourced,
   over the nine parent rows and the parent battery: among
   (policy, step) pairs under a patience-down move where BOTH runs
   are forced at every step up to and including that step, the
   committed cells NEST — zero exceptions. Gate on the tested set
   being at least 20% of all (policy, step) pairs (L5). The
   complementary count — non-nested pairs, all of which must carry
   a route flip in their history — is printed beside it.
C3 [THE AIMED FORGE — the open observable; no anatomy frozen]
   The double-burst battery: streams carrying two and three large
   digits at separations 1..4 (matched to the patience axis), the
   alternating route-phase blocks, and a digit ramp; maps id, dbl
   and sq; horizons 16 and 48; UNRESOURCED only; single-row
   landscapes under the lex deficit on the behavioral quotient
   with cure moves. GUESS: the twin-burst worlds at separation
   equal to a patience gap are where a stall appears if one does.
   No direction is frozen for its anatomy.

KILL CRITERIA (observables, meaning weighed after the run)
----------------------------------------------------------
K1 Any C1 check fails: the rig is dead, no verdicts.
K2 A forge stall whose whole cure neighborhood is STRICTLY worse
   (no equal-loss neighbor): prints STRICT LOCAL MIN — the
   unresourced cell settles FALSE and the conjecture dies without
   a budget at all.
K3 A forge stall with an equal-loss neighbor of different
   behavior: prints TIE-FLAT STALL with the flat's exit status —
   the cell settles as tie-only, which the conjecture's slogan
   survives.
K4 Zero forge stalls: prints DESERT at this battery's scope; the
   report is then C2's status, which is the sharpened obstruction.
K5 [C2's own kill] A non-nested step whose two runs are BOTH
   forced throughout: L2 is FALSE, and the printed specimen names
   a second unresourced negative channel — a more valuable result
   than the forge's, and the reason C2 prints its first exception
   in full.

ENGINE
------
E1 controls: the instrumented reader against SC.run_reader on the
   nine parent rows (C1(i)); this rig's census on the parent
   battery's unresourced slice (C1(ii)).
E2 the route-lemma census (C2): per (policy, step), the FORCED
   flag (no iteration of that step's commit loop had both
   candidates) and the cumulative forced-through-n flag; the
   nesting exception count over the forced-forced set, the tested
   fraction, and the first exception in full if any.
E3 the aimed forge (C3): the double-burst battery, unresourced,
   per landscape the quotient stall census and the value-tie
   adjacency census.
E3b the density anatomy (post-run); E3c the density-selected
   forge (post-run).
E4 conditional: full anatomy of every stall found (members,
   neighbor deltas, basin, escape radius, tie/strict verdict, the
   per-step-lex retest on tie-flats), capped in print at five,
   reusing the parent's anatomy printer verbatim.
Exact big-integer arithmetic throughout (imported comparators).
Sequential, one landscape at a time; estimated run one to four
minutes, memory trivial (no BLAS import); positive controls gate
all verdicts; exit nonzero on any check failure.

FINDINGS (entered after the run; ALL CHECKS PASS, exit 0, ~18 s,
peak 21.4 MB)
----------------------------------------------------------------
F1 C1 controls exact. The instrumented reader agrees with the
   parent reader on loss triple and full trace over 9 rows x 100
   unresourced policies at horizon 120; this rig's census
   reproduces the parent's unresourced slice — 112 landscapes,
   ZERO stalls, zero adjacent value ties.

F2 C2 CONFIRMED, and the lemma's real name is THE DECISION LEMMA,
   not the route lemma of L2's frozen wording: what the engine
   measures is a preference decision being AVAILABLE (both
   candidates present at some iteration), which is broader than
   two runs taking different branches, and it is the available
   decision that does the work. Over 741,888 (policy, step) pairs
   under a patience-down move, unresourced, across the nine parent
   rows and the whole parent battery: 188,928 pairs (25.5%) have
   BOTH runs decision-free through the step, and among them the
   committed cells NEST with ZERO exceptions. Non-nesting is
   common in the whole set — 71,023 pairs, 9.6% — and those two
   numbers are NOT complements: what the zero says is that the
   71,023 lie entirely OUTSIDE the decision-free 188,928, so
   every one of them carries an available decision in its
   history.
   THE HAND PROOF COVERS ONE HALF, and the other half is the
   lemma's honest cost. From a COMMON start it is complete: under
   forced-forced each iteration has exactly one candidate; a
   smaller ref_t sits in the same tree child (containment is
   inherited downward, and the loop tests the children in a fixed
   order, so the pick is the same) and a smaller ref_c gives
   weakly larger chain_kmax, so the two loops walk the same
   branch sequence with the lower-patience run refining at least
   as far — a divergence would need a candidate to APPEAR for the
   smaller reference, which is a second candidate, i.e. not
   forced. What is NOT supplied is the induction across steps:
   at step n the two runs start from DIFFERENT cells (the
   lower-patience one inside the other), and carrying containment
   through two forced loops run from unequal starts toward
   unequal references is a monotone-fixed-point step the corpus
   records as TIGHT in its single-reference form (the bottom
   lemma's policy-level witness, explore_bootstrap_cures.py). So
   the lemma rests on the engine leg at this scope, not on a
   completed proof, and the common-start half is what a proof
   would build on.
   THE CONSEQUENCE: the spine proof's nesting is NOT dead off the
   spine. It is dead ONLY where a preference decision was
   available — necessary, NOT sufficient, and the rig's own
   counts refute the converse in one subtraction: 552,960 pairs
   lie outside the decision-free set, only 71,023 of them are
   non-nested, so 481,937 pairs carry a decision in their history
   and nest anyway — so the theorem extends off the
   spine to the whole decision-free sub-family, and the entire
   unresourced obstruction is ONE object.

F3 C3's guess REFUTED by the forge's own reach control, which is
   the run's most useful correction. The double-burst battery
   scored 20.6% decision density against the parent battery's
   26.8% — the aimed forge was aimed BELOW its own target. The
   first reading of WHY was wrong and E3c was written to settle
   it (E3b): a burst does NOT suppress decisions. Off an all-1 base
   (15.2%) one large digit RAISES density to 20.7%, twin bursts
   to 22.7%, and the size saturates — digits 4, 8 and 20 all read
   20.7%. What the aimed battery lacked is ALTERNATION: period
   [1,2] reads 21.1%, [1,4] 35.9%, [2,4] 48.4%, and the aimed
   worlds are long all-1 runs with two bursts in them, so they
   sit near the bottom of the range no matter how big the bursts
   are. What E3b measures is that density tracks the digit
   pattern's VARIETY and saturates in demand SIZE; why variety
   buys decisions is not measured here and is not claimed.
   Zero stalls and zero adjacent value ties in all 192 landscapes
   of that battery, but at that density the desert is weak
   evidence and is reported as such.

F4 THE DESERT SURVIVES AT 1.7-1.9x THE DENSITY (E3c, the
   density-selected forge; K4). Selecting worlds by the mechanism
   observable itself — every periodic stream of period <= 3 over
   digits 1..4 with heads () and (2,), 399 landscapes scored per
   horizon, top 24 taken — reaches a density band of 45.3-52.1%
   at horizon 16 and 45.8-50.9% at horizon 48 — 1.7 to 1.9 times
   the parent battery's 26.8%, against a pool median of ~30%.
   Across those 48 landscapes: ZERO stalls and ZERO adjacent
   value ties. The one unresourced negative-coupling candidate,
   run at 1.7-1.9 times the density the previous evidence ran at,
   manufactures no strict local minimum and no tie flat.

F5 THE SHARPENED OBSTRUCTION (what the cell now costs to settle).
   Any unresourced off-spine stall must have EVERY patience-down
   neighbor separated from it by an available preference decision
   — a necessary condition, from F2, that the desert of F4 says
   is not sufficient at this scope. The step from nesting to the
   ORDER is licensed rather than assumed, and it is the parent
   spine theorem's own load-bearing qualifier: nesting gives the
   finer trace a smaller factor at every counted step, which
   beats it in the lex deficit only while both traces are
   FINITE-LOSS — with an infinite counted cell the flag is
   compared first and the finite parts run over different step
   sets, so a finer trace could rank worse. Measured, not argued:
   at finite patience below the counted-window start there are
   ZERO infinite counted cells in 494,592 of them, and zero of
   the 9,482 fully nested policy pairs — a policy-move unit, not
   the per-step unit of the counts above — has the finer one
   ranking worse (E2's order licence, a gate). L1's asymmetry is the reason
   to doubt sufficiency: a budget is a conserved spendable
   quantity, so spending early removes capacity late — a negative
   inter-step coupling, which is the burst trap's whole mechanism.
   The ratchet is positive-only (C_{n+1} is a subset of C_n), and
   a preference decision redirects the ratchet without conserving
   anything. What a proof of the cell must supply is exactly what
   this rig could not: an argument that a decision cannot buy a
   late gain with an early loss.

THE VERDICT. The unresourced off-spine cell is NOT settled as a
theorem, and it is no longer a shrug. It is stall-free at every
scope measured — 112 parent, 192 aimed and 48 density-selected
runs over 348 DISTINCT worlds, the batteries overlapping in four
— and the reason has a name: nesting survives off the
spine everywhere no preference decision is available (exhaustive
at 188,928 pairs, half of it proved), so the whole open edge is
whether a preference decision alone, with no conserved budget
behind it, can manufacture a strict local minimum. Running that
decision at 1.7-1.9 times the density does not.
Tiers: the decision lemma is a RULE — verified exhaustively at
the stated scope, with the common-start half of its proof in hand
and the cross-step induction open (F2); the
desert is an OBSERVATION over 348 distinct unresourced
landscapes with its density reach reported; F3's density anatomy
is an OBSERVATION, measured at E3b after the hand reason first
given for it turned out to be backwards.

Run record. The first run exited 0 in ~7.5 s with C1 and C2 green
and the double-burst forge a desert. Post-run edits, no prediction
band touched: (1) decision_density was added as a reach control on
the forge and printed for both batteries, which is what refuted
C3's guess; (2) E3c, the density-selected forge, was added in
answer to that refutation. Final run ~18 s, peak 21.4 MB under
memwatch.
"""

import sys

import explore_scale_clock as SC
import explore_stall_tie as ST

# ----------------------------------------------------------------- #
# the instrumented reader: SC.run_reader verbatim plus one flag per
# step — did any iteration of the commit loop have BOTH candidates
# available (a route decision), or was every iteration forced?
# ----------------------------------------------------------------- #

def run_reader_routed(J_list, policy, horizon):
    """Returns (num, den, inf, trace, forced) with forced[n] True
    iff no iteration at step n had both a tree and a chain
    candidate. Loop body identical to SC.run_reader."""
    s_t, s_s, pt, pc = policy
    C = SC.ROOT
    num, den, inf = 1, 1, False
    trace = []
    forced = []
    for n in range(horizon):
        J = J_list[n]
        ref_t = J_list[n - pt] if pt is not None and n - pt >= 0 else None
        ref_c = J_list[n - pc] if pc is not None and n - pc >= 0 else None
        step_forced = True
        guard = 0
        while True:
            guard += 1
            if guard > 10 ** 6:
                raise AssertionError("commit loop runaway")
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
            if cand_tree is not None and cand_chain is not None:
                step_forced = False
            if cand_chain is not None and (cand_tree is None or prefer_chain):
                C = cand_chain
            else:
                C = cand_tree
        clo, chi = SC.interval(C)
        if SC.lt(J[0], clo) or SC.lt(chi, J[1]):
            raise AssertionError("commitment lost the image")
        if n >= SC.N0:
            lp = SC.length_pair(C)
            if lp is None:
                inf = True
            else:
                num *= lp[0]
                den *= lp[1]
        trace.append((SC.rank(C), C[5] if C[0] == "S" else 0, (clo, chi)))
        forced.append(step_forced)
    return num, den, inf, trace, forced

# ----------------------------------------------------------------- #
# batteries
# ----------------------------------------------------------------- #

def parent_battery():
    """The parent forge's worlds, verbatim (explore_stall_tie)."""
    return ST.battery_worlds()

def aimed_worlds(horizon):
    """The double-burst battery of L3: two and three large digits
    at designed separations, the route-phase blocks, the ramp."""
    worlds = []
    base = [1] * horizon
    for j in (9, 10):
        for g in (1, 2, 3, 4):
            for D in (4, 8):
                if j + g >= horizon:
                    continue
                digs = list(base)
                digs[j] = D
                digs[j + g] = D
                worlds.append(("twin%d+%d.D%d" % (j, g, D), digs))
    for g in (1, 2, 3):
        for D in (4, 8):
            if 9 + 2 * g >= horizon:
                continue
            digs = list(base)
            for m in (0, 1, 2):
                digs[9 + m * g] = D
            worlds.append(("trip9+%d.D%d" % (g, D), digs))
    for blk in (1, 2, 3, 4):
        for D in (3, 5):
            digs = []
            while len(digs) < horizon:
                digs.extend([1] * blk)
                digs.extend([D] * blk)
            worlds.append(("phase%d.D%d" % (blk, D), digs[:horizon]))
    worlds.append(("ramp", [1 + (i % 5) for i in range(horizon)]))
    worlds.append(("rampup", [1 + i // 4 for i in range(horizon)]))
    return worlds

AIMED_MAPS = ("id", "dbl", "sq")
AIMED_HORIZONS = (16, 48)

# ----------------------------------------------------------------- #
# one unresourced landscape
# ----------------------------------------------------------------- #

def decision_density(J, horizon):
    """(steps carrying an available preference decision, counted
    steps) over the finite-patience four-coordinate space — the
    forge's own reach: a battery with no decisions cannot test the
    decision lemma's complement."""
    dec = tot = 0
    for st in (0, 1):
        for ss in (0, 1):
            for pt in (0, 1, 2, 3):
                for pc in (0, 1, 2, 3):
                    fo = run_reader_routed(J, (st, ss, pt, pc),
                                           horizon)[4][SC.N0:]
                    dec += sum(0 if f else 1 for f in fo)
                    tot += len(fo)
    return dec, tot

SEEN = set()
RUNS = [0]

def landscape(J, horizon, key=None):
    """Unresourced quotient landscape: returns the census tuple.
    Every call registers its world key, so the three batteries can
    be reported as DISTINCT landscapes and not as runs — they
    overlap, the density pool and the parent battery both holding
    short periodic streams."""
    RUNS[0] += 1
    if key is not None:
        SEEN.add(key)
    space = SC.policy_space5(SC.AX_BASE, [SC.INF_D])
    sigd, lossd, clensd = {}, {}, {}
    for p in space:
        t, sg, cl = ST.run_pol(J, p, None, 0, horizon)
        sigd[p], lossd[p], clensd[p] = sg, t, cl
    return ST.census(space, sigd, lossd, clensd, [SC.INF_D])

# ----------------------------------------------------------------- #
# E1: controls
# ----------------------------------------------------------------- #

def e1_controls(imgs):
    print("\nE1  CONTROLS")
    space4 = SC.policy_space4(SC.AX_BASE)
    same = True
    for row in SC.ROWS:
        J = imgs[row]
        for pol in space4:
            a = SC.run_reader(J, pol, SC.N_MAIN)
            b = run_reader_routed(J, pol, SC.N_MAIN)
            if a[:3] != b[:3] or a[3] != b[3]:
                same = False
    SC.check("C1(i) instrumented reader reproduces the parent reader "
             "on %d rows x %d policies" % (len(SC.ROWS), len(space4)),
             same)

    n_land = n_stall = n_ties = 0
    dec = tot = 0
    for wname, digs in parent_battery():
        cyls = SC.cylinders(digs)
        for mp in ("id", "dbl"):
            J_full = SC.images(cyls, mp)
            for horizon in ST.HORIZONS:
                _m, _n, _q, _r, stalls, ties, _c = landscape(
                    J_full[:horizon], horizon,
                    (tuple(digs[:horizon]), mp, horizon))
                n_land += 1
                n_stall += len(stalls)
                n_ties += len(ties)
                a, b = decision_density(J_full[:horizon], horizon)
                dec += a
                tot += b
    print("  parent battery unresourced slice: %d landscapes, "
          "%d stalls, %d adjacent value ties" % (n_land, n_stall, n_ties))
    print("  parent battery decision density: %d of %d counted "
          "(policy, step) pairs carry an available preference "
          "decision (%.1f%%)" % (dec, tot, 100 * dec / tot))
    SC.check("C1(ii) parent battery unresourced slice reproduces "
             "112 landscapes, zero stalls",
             n_land == 112 and n_stall == 0)

# ----------------------------------------------------------------- #
# E2: the route-lemma census
# ----------------------------------------------------------------- #

def forced_prefix(forced):
    """Cumulative: out[n] True iff every step <= n was forced."""
    out, acc = [], True
    for f in forced:
        acc = acc and f
        out.append(acc)
    return out

def e2_route_census(imgs):
    print("\nE2  THE DECISION LEMMA: does nesting hold wherever the "
          "commit loop was never offered a choice?")
    total = tested = exc = nonnested = 0
    inf_cells = tot_cells = nested_pairs = nested_worse = 0
    first_exc = None
    rows = [(SC.fmt_row(r), imgs[r], SC.N_MAIN) for r in SC.ROWS]
    for wname, digs in parent_battery():
        cyls = SC.cylinders(digs)
        for mp in ("id", "dbl"):
            J_full = SC.images(cyls, mp)
            for horizon in ST.HORIZONS:
                rows.append(("%s/%s h%d" % (wname, mp, horizon),
                             J_full[:horizon], horizon))
    for label, J, horizon in rows:
        runs = {}
        for st in (0, 1):
            for ss in (0, 1):
                for pt in (0, 1, 2, 3):
                    for pc in (0, 1, 2, 3):
                        num, den, i, tr, fo = run_reader_routed(
                            J, (st, ss, pt, pc), horizon)
                        cl = [tr[n][2] for n in range(SC.N0, horizon)]
                        inf_cells += sum(
                            1 for c in cl if SC.ival_length(*c) is None)
                        tot_cells += len(cl)
                        runs[(st, ss, pt, pc)] = (
                            cl, forced_prefix(fo)[SC.N0:], (num, den, i))
        for pol, (cells, fp, loss) in runs.items():
            st, ss, pt, pc = pol
            for (dt, dc) in ((0, -1), (-1, 0)):
                qt, qc = pt + dt, pc + dc
                if qt < 0 or qc < 0:
                    continue
                cells_lo, fp_lo, loss_lo = runs[(st, ss, qt, qc)]
                if all(ST.cell_inside(a, b)
                       for a, b in zip(cells_lo, cells)):
                    nested_pairs += 1
                    if SC.cmp_lex(loss_lo, loss) > 0:
                        nested_worse += 1
                for i, (ca, cb) in enumerate(zip(cells_lo, cells)):
                    total += 1
                    nested = ST.cell_inside(ca, cb)
                    if not nested:
                        nonnested += 1
                    if fp[i] and fp_lo[i]:
                        tested += 1
                        if not nested:
                            exc += 1
                            if first_exc is None:
                                first_exc = (label, pol, (qt, qc),
                                             SC.N0 + i, ca, cb)
    frac = tested / total if total else 0.0
    print("  (policy, step) pairs under a patience-down move: %d" % total)
    print("  both runs forced through the step: %d (%.1f%% tested)"
          % (tested, 100 * frac))
    print("  non-nested overall: %d | non-nested inside the forced "
          "set: %d" % (nonnested, exc))
    if first_exc is not None:
        label, pol, low, n, ca, cb = first_exc
        print("  FIRST EXCEPTION (K5): %s  policy %s vs %s  step %d"
              % (label, pol, low, n))
        print("    lower-patience cell %s   higher-patience cell %s"
              % (ca, cb))
    print("  ORDER LICENCE: infinite counted cells %d of %d | fully "
          "nested patience-down pairs %d, of which the finer one "
          "ranks WORSE %d" % (inf_cells, tot_cells, nested_pairs,
                              nested_worse))
    SC.check("C2's order licence: nesting implies a better-or-equal "
             "lex deficit (no infinite counted cell at finite "
             "patience, no nested inversion)",
             inf_cells == 0 and nested_worse == 0)
    if frac < 0.20:
        SC.check("C2 route lemma", False,
                 "UNTESTED: forced set is %.1f%% of pairs, below the "
                 "20%% floor (L5)" % (100 * frac))
    else:
        SC.check("C2 nesting holds on the forced set "
                 "(%.1f%% of pairs)" % (100 * frac), exc == 0)
    return total, tested, exc, nonnested

# ----------------------------------------------------------------- #
# E3: the aimed forge
# ----------------------------------------------------------------- #

def e3_forge():
    print("\nE3  THE AIMED FORGE: double-burst battery, unresourced")
    n_land = n_stall_land = n_ties = 0
    dec = tot = 0
    specimens = []
    tie_example = None
    for horizon in AIMED_HORIZONS:
        worlds = aimed_worlds(horizon)
        for wname, digs in worlds:
            cyls = SC.cylinders(digs)
            for mp in AIMED_MAPS:
                J = SC.images(cyls, mp)[:horizon]
                mem, nbrs, qloss, qranks, stalls, ties, cbs = \
                    landscape(J, horizon,
                              (tuple(digs[:horizon]), mp, horizon))
                n_land += 1
                n_ties += len(ties)
                a, b = decision_density(J, horizon)
                dec += a
                tot += b
                if ties and tie_example is None:
                    tie_example = (wname, mp, horizon)
                if stalls:
                    n_stall_land += 1
                    for s in stalls:
                        specimens.append((wname, mp, horizon, None, 0,
                                          s, mem, nbrs, qloss, qranks,
                                          cbs))
        print("  horizon %d: %d worlds x %d maps done"
              % (horizon, len(worlds), len(AIMED_MAPS)))
    print("  landscapes %d | landscapes with stalls %d | "
          "adjacent value-tie pairs %d | stall specimens %d"
          % (n_land, n_stall_land, n_ties, len(specimens)))
    print("  aimed battery decision density: %d of %d counted "
          "(policy, step) pairs carry an available preference "
          "decision (%.1f%%)" % (dec, tot, 100 * dec / tot))
    if tie_example is not None:
        print("  first adjacent value tie: world %s/%s h=%d"
              % tie_example)
    return specimens

# ----------------------------------------------------------------- #
# E3b: the density-selected forge (added after the first run, which
# measured the aimed battery BELOW the parent's decision density —
# the forge had missed its own target. No prediction band touched;
# this engine selects worlds by the mechanism observable itself.)
# ----------------------------------------------------------------- #

def density_pool(horizon):
    """Deterministic pool: every periodic stream of period <= 3 over
    digits 1..4, with heads () and (2,)."""
    out = []
    seen = set()
    periods = [(a,) for a in (1, 2, 3, 4)]
    periods += [(a, b) for a in (1, 2, 3, 4) for b in (1, 2, 3, 4)]
    periods += [(a, b, c) for a in (1, 2, 3, 4) for b in (1, 2, 3, 4)
                for c in (1, 2, 3, 4)]
    for head in ((), (2,)):
        for per in periods:
            digs = tuple(SC.cf_digits(list(head), list(per), horizon))
            if digs in seen:
                continue
            seen.add(digs)
            out.append(("h%sp%s" % ("".join(map(str, head)),
                                    "".join(map(str, per))), list(digs)))
    return out

TOP_N = 24

def e3c_density_forge():
    print("\nE3c THE DENSITY-SELECTED FORGE: worlds chosen by the "
          "mechanism observable (top %d per horizon)" % TOP_N)
    specimens = []
    n_land = n_stall_land = n_ties = 0
    for horizon in AIMED_HORIZONS:
        scored = []
        for wname, digs in density_pool(horizon):
            cyls = SC.cylinders(digs)
            for mp in AIMED_MAPS:
                J = SC.images(cyls, mp)[:horizon]
                a, b = decision_density(J, horizon)
                scored.append((a / b, wname, mp, J, digs))
        scored.sort(key=lambda z: (-z[0], z[1], z[2]))
        print("  horizon %d: pool %d landscapes, decision density "
              "max %.1f%% median %.1f%%"
              % (horizon, len(scored), 100 * scored[0][0],
                 100 * scored[len(scored) // 2][0]))
        for dens, wname, mp, J, digs in scored[:TOP_N]:
            mem, nbrs, qloss, qranks, stalls, ties, cbs = \
                landscape(J, horizon,
                          (tuple(digs[:horizon]), mp, horizon))
            n_land += 1
            n_ties += len(ties)
            if stalls:
                n_stall_land += 1
                for s in stalls:
                    specimens.append((wname, mp, horizon, None, 0, s,
                                      mem, nbrs, qloss, qranks, cbs))
        print("    top-%d density band %.1f%%..%.1f%%"
              % (TOP_N, 100 * scored[TOP_N - 1][0], 100 * scored[0][0]))
    print("  landscapes %d | landscapes with stalls %d | "
          "adjacent value-tie pairs %d | stall specimens %d"
          % (n_land, n_stall_land, n_ties, len(specimens)))
    return specimens

# ----------------------------------------------------------------- #

def e3b_density_anatomy():
    """Added after the first run (no prediction band touched): the
    forge's reach control said the double-burst battery scored
    BELOW the parent's, and the first reading of why — that a
    burst suppresses decisions — is a mechanism, so it is
    measured here rather than asserted."""
    print("\nE3b DENSITY ANATOMY: what actually moves the mechanism "
          "observable (horizon 16, map dbl)")
    h = 16
    base = [1] * h

    def dens(digs):
        a, b = decision_density(SC.images(SC.cylinders(digs), "dbl")[:h], h)
        return 100.0 * a / b

    rows = [("all-1 base", base)]
    for D in (2, 4, 8, 20):
        d = list(base)
        d[10] = D
        rows.append(("one digit %d at n=10" % D, d))
    d = list(base)
    d[9] = 8
    d[11] = 8
    rows.append(("twin 8s at n=9,11", d))
    for per in ([1, 2], [1, 4], [2, 4]):
        rows.append(("period %s" % per, SC.cf_digits([], per, h)))
    for name, digs in rows:
        print("    %-22s %.1f%%" % (name, dens(digs)))
    print("    -> a burst RAISES density off an all-1 base; what the "
          "aimed battery lacked is ALTERNATION, not burst size")

def main():
    print("THE UNRESOURCED CELL: stall-free by law, or a tame battery?")
    print("=" * 70)
    imgs = SC.build_images(SC.N_MAIN)
    e1_controls(imgs)
    if SC.FAILURES:
        print("\nCONTROLS FAILED — no verdicts.")
        sys.exit(1)
    e2_route_census(imgs)
    specimens = e3_forge()
    e3b_density_anatomy()
    specimens += e3c_density_forge()
    for i, spec in enumerate(specimens[:5]):
        ST.anatomy(spec, i + 1)
    if len(specimens) > 5:
        print("  (%d further specimens not printed)"
              % (len(specimens) - 5))
    print("\n  COVERAGE: %d landscape runs over %d DISTINCT worlds "
          "(the three batteries overlap)" % (RUNS[0], len(SEEN)))
    if not specimens:
        print("  -> DESERT (K4): zero stalls across every battery run")
    print("\n" + "=" * 70)
    if SC.FAILURES:
        print("FAILURES: %s" % ", ".join(SC.FAILURES))
        sys.exit(1)
    print("ALL CHECKS PASS")
    sys.exit(0)

if __name__ == "__main__":
    main()
