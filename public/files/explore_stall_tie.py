"""THE STALL-TIE QUESTION: is the closing shape a theorem?

THE QUESTION
------------
The reader-descent corpus's blindness table closes on a conjecture,
its closing shape: every stall strict descent found is
a TIE artifact, and two instruments dissolve them all — REFINE THE
RULER where coarseness starves the signal, QUOTIENT THE SPACE where
coordinates outnumber behaviors. At the scanned grid the pair
already suffices: lexicographic deficit descent on the behavioral
quotient stalls nowhere off the optimum at any setting
(explore_scale_clock.py). Whether that is a THEOREM of exact reader
spaces is the open question. Two separable halves:

  H1 (the tie half): every stall off the bottom sits on a tie —
     some neighbor has EXACTLY equal loss; there are no strict
     local minima. The slate's vertiginous form: exact learning
     cannot stall except by measurement ties.
  H2 (the cure half): under the lex deficit on the behavioral
     quotient there are no stalls at all — the instrument pair
     suffices as instrumented.

THE NAMED CLASS (what the theorem must quantify over)
-----------------------------------------------------
Spaces: commitment-policy spaces on the mediant-straddle cover of
the continued-fraction window (explore_cf_redundant.py's cover;
machinery imported verbatim from explore_scale_clock.py). A stream
is any nested, strictly shrinking sequence of rational intervals
J_n (a CF digit stream pushed through an exact monotone map); a
world is a finite set of such rows; the horizon is any finite
length beyond the counted-window start N0. Policies are
(s_t, s_s, pt, pc, delta) over the patience axis {0,1,2,3,INF} and
the cap-quotiented drawdown axis; readers are the unresourced,
throttled and banking commit loops, any (B, W). Losses: the exact
deficit (product of committed cell lengths over counted steps),
lexicographically refined — finite beats infinite, two infinites
compare finite parts. Moves: single coordinate steps plus the
route-preference diagonal (the cure set). Quotient: counted-window
committed-cell trace signature. A stall is an off-bottom quotient
class none of whose cure-graph neighbors ranks strictly lower.

HAND-ATTACK (fixed before the engine; the proofs are the design)
----------------------------------------------------------------
L1 (C_min monotonicity, proved). For a bounded nondegenerate
   interval J, let C_min(J) be the inclusion-minimum cover cell
   containing J (it exists: the bottom lemma,
   explore_bootstrap_cures.py). If J' is a subset of J then
   C_min(J') is a subset of C_min(J). Proof: every cell containing
   J contains J', so the containing family of J sits inside the
   containing family of J'; C_min(J') is contained in every member
   of the larger family, in particular in C_min(J), which is a
   member of it.

L2 (THE SPINE THEOREM, proved by hand; the engine leg is
   prediction C2). Restrict to the single-reference subfamily
   pt = pc = p (one reference J_{n-p} per step), unresourced,
   greedy multi-commit. Then:
   (i)  the committed cell at step n is exactly C_min(J_{n-p}):
        greedy multi-commit reaches the minimum from any containing
        start in any preference order (the bottom lemma), and the
        ratchet start is consistent across steps because
        C_min(J_{n-p}) is a subset of C_min(J_{n-1-p}) by L1
        (references shrink). Corollary: at equal patience the trace
        is route-free — all four preference variants share one
        behavior class.
   (ii) per-step committed lengths are pointwise monotone in p:
        J_{n-(p-1)} is a subset of J_{n-p}, so by L1 the
        patience-(p-1) cell sits inside the patience-p cell at
        every step. Hence the deficit is monotone along the
        patience diagonal, STRICTLY unless the counted traces
        coincide — in which case the two policies are one quotient
        class.
   (iii) the refuser (p = INF) commits nothing and prices infinite;
        the lex order ranks any finite-patience class strictly
        better (finite beats infinite).
   THEOREM (this cover, this move set, any nested strictly
   shrinking stream, any horizon): on the spine subspace
   {pt = pc}, with the diagonal patience step as the move,
   lexicographic deficit descent on the behavioral quotient has NO
   stall off the bottom, and the bottom is greedy patience. The
   closing shape is a theorem on the spine.

L3 (where the general theorem must be fought). Off the spine the
   reader holds two references of different ages and the fixed
   point is preference-dependent (the single-reference hypothesis
   of the bottom lemma is TIGHT — the policy-level witness in
   explore_bootstrap_cures.py), so no L1-style
   containment argument exists; under resources the landscape is
   measurably path-dependent (route-locking, the start-delay law).
   Any counterexample to H1/H2 lives at mixed patience, under
   resources, or both.

L4 (the tie door; TRANSPLANT, flagged as such). In the amnesia
   corpus a designed world realized an exact product tie between
   DISTINCT factor multisets (explore_tie_world.py's witness-free
   tie). The same algebraic door is open here: the deficit is a
   product of interval lengths, so two DIFFERENT counted traces
   can tie exactly — a value tie the quotient does not merge
   (different behaviors) and the lex refinement does not break
   (equal finite parts). If a designed world realizes such a tie
   on the only descent path, H2 fails as instrumented; the
   candidate third instrument is the fully lexicographic PER-STEP
   deficit (first differing counted step decides). The transplant
   is from a different algebra (normalizer products over one
   prime); whether interval-length products cooperate is exactly
   what the forge asks.

PREDICTIONS, fixed before the engine ran
----------------------------------------
C1 [controls, gate]
   (i)  The census code of this rig, run on the parent's own
        tables at (B, W) = (2, 0), reproduces the parent's
        landscape exactly: ONE cure-set stall under the composite
        clock order (the disagreement stall), ZERO single-move and
        ZERO cure-set stalls under the deficit-only order.
   (ii) The same at (2, 2): zero stalls under both orders.
C2 [THE SPINE ENGINE LEG — predicted PASS, the theorem is proved]
   On all nine parent rows, unresourced, p in {0,1,2,3}:
   (i) the four preference variants at pt = pc = p share one
   signature; (ii) the patience-(p-1) committed cell is contained
   in the patience-p cell at every counted step; (iii) the lex
   deficit is monotone in p along the spine, strict wherever the
   signatures differ, and the p = INF class ranks strictly worst;
   (iv) the spine quotient has zero stalls off the bottom, which
   is greedy.
C3 [the mechanism census — GUESS, printed, no gate] Off the spine,
   unresourced, some single patience step (pt, pc) -> (pt, pc - 1)
   or (pt - 1, pc) produces a NON-NESTED counted step (the
   containment of C2(ii) fails at mixed patience) — expected from
   preference-dependence; the census prints the count either way.
C4 [THE FORGE — the open observable; guesses marked as such]
   Across the designed-world battery (periodic tails of period
   <= 2 over digits {1,2,3} with short heads, spike streams, the
   Fibonacci word; maps id and dbl; horizons 16 and 120; settings
   unresourced, (1,0), (2,0), (2,2); single-row landscapes under
   the lex deficit on the behavioral quotient with cure moves):
   GUESS: at least one stall appears somewhere in the battery.
   No direction is frozen for its anatomy — that is what the
   experiment is for.
C5 [the tie raw material — GUESS] The battery realizes at least
   one exact deficit tie between distinct ADJACENT behavior
   classes at the short horizon (the tie door of L4 is open).

KILL CRITERIA (observables, meaning weighed after the run)
----------------------------------------------------------
K1 Any C1 or C2 check fails: the rig (or the hand proof) is dead;
   no verdicts.
K2 A forge stall whose whole cure neighborhood is STRICTLY worse
   (no equal-loss neighbor): prints as STRICT LOCAL MIN.
K3 A forge stall with an equal-loss neighbor of different
   behavior: prints as TIE-FLAT STALL, with the flat's exit status
   (does the equal-rank component reach a strictly better
   neighbor) and the per-step-lex retest.
K4 Zero forge stalls: prints as DESERT — the census result at
   this battery's scope.

ENGINE
------
E1 controls: parent tables at (2,0) and (2,2) via
   explore_scale_clock.setting_tables; this rig's own census
   helpers must reproduce the parent's stall counts under both
   orders (C1).
E2 the spine leg (C2) on the nine parent rows.
E3 the mechanism census (C3): non-nested counted steps across
   single patience moves, unresourced, all preference pairs, both
   patience coordinates, per parent row.
E4 the forge (C4/C5): the designed-world battery; per landscape,
   quotient stall census under the lex deficit with cure moves,
   value-tie adjacency census; full anatomy of every stall found
   (members, neighborhood comparison, flat reachability), capped
   in print at the first five.
E5 conditional: the per-step-lex third instrument, run on every
   K3 specimen.
Exact big-integer arithmetic throughout (imported comparators).
Sequential, one landscape at a time; estimated run one to three
minutes, memory trivial; positive controls gate all verdicts;
exit nonzero on any check failure.

FINDINGS (entered after the run; ALL CHECKS PASS, exit 0, ~14 s)
----------------------------------------------------------------
F1 C1 controls exact: this rig's census on the parent's tables
   reproduces the parent landscape at both settings — (2, 0): one
   composite cure-set stall, zero deficit-order stalls (single and
   cure); (2, 2): zero and zero.
F2 C2 CONFIRMED IN FULL — the spine theorem's engine leg: on all
   nine parent rows, equal patience is route-free (one signature
   per p across the four preference variants), the patience-(p-1)
   cell sits inside the patience-p cell at every counted step, the
   lex deficit is monotone along the spine and strict across
   distinct classes (id/phi ln -6610.60 < -6502.81 < -6395.02 <
   -6287.22), and the refuser ranks strictly worst. The hand proof
   (L1, L2) stands.
F3 C3 CONFIRMED: mixed-patience non-nestedness is real and
   widespread even unresourced — 8437 non-nested (policy, step)
   counts across the nine rows (784-1835 per row; sq/sqrt2 the
   one zero). The raw material for traps exists without resources.
F4 THE STRICT TRAP EXISTS — K2 fired; both halves refuted in the
   general class. 6 of 448 landscapes carry a stall under the lex
   deficit on the behavioral quotient with cure moves, and every
   one is a STRICT LOCAL MIN: zero tied neighbors, every cure
   move strictly worse. All six live in spike streams (an all-1
   digit tail with one 8) under the dbl map at B = 2, W in
   {0, 2}; the stall classes sit at chain-first entry
   (sigma = (1, 0) or (1, 1)) with patience (0, 2) or (0, 3);
   basins 2-22 classes; the short horizon already carries one.
   Unresourced landscapes: ZERO stalls in all 112 — the
   non-nestedness of F3 never assembles into a trap without a
   budget at this battery's scope. Anatomy of the dissected
   specimen (spike1@10/dbl, horizon 16, (2, 0)): the stall
   (patience (0, 2)) against its chain-patience-down neighbor is
   a pure two-step TRADE — the neighbor is better at step 9
   (5/1786 < 1/357, cross-multiplication 1785 < 1786) and worse
   at step 14 (5/3645909 > 1/768298), net +0.0517 ln; the route
   flip costs +1.14 ln at step 12 alone; patience up costs +10.6
   ln. The trade re-derived by hand: ln(1785/1786) +
   ln(3841490/3645909) = -0.00056 + 0.05225 = +0.0517.
F5 Every specimen's escape radius through the cure graph is 2:
   two-move lookahead cures every stall this corpus has found,
   the parent's disagreement stall included.
F6 C5 CONFIRMED, and the tie door is open but innocent at scope:
   exactly one adjacent equal-deficit pair of distinct behaviors
   in 448 landscapes (h3t12/dbl, horizon 16, (1, 0)); no
   tie-flat stall anywhere in the battery.

THE VERDICT. The closing shape is NOT a theorem of exact reader
spaces; it settles as a dichotomy.
(i)  On the single-reference spine (pt = pc, unresourced) it is a
     THEOREM, proved by hand for this cover and move set at any
     nested strictly shrinking stream and any horizon: lex-deficit
     descent on the behavioral quotient stalls nowhere off the
     bottom, and the bottom is greedy patience (L1 + L2; engine
     leg F2).
(ii) Off the spine, under a binding budget, THE BURST TRAP exists:
     a strict local minimum that is a TRADE, not a tie — a demand
     burst makes one patience pay a little early to win a lot
     late, and every single move breaks the paired structure. The
     conjecture's slogan (exact learning cannot stall except by
     measurement ties) is FALSE as stated; the instrument pair
     (refine the ruler, quotient the space) does not suffice in
     general. What survives at every specimen: escape radius 2 —
     no stall found to date, tie-born or trade-born, survives
     two-move lookahead.

Run record. The first run exited 0 in ~14 s, all controls and
spine checks green on the first run; the forge found the six
specimens (K2), so C4's guess held and the anatomy became the
finding. Post-run edits: the anatomy printer gained members,
neighbor deltas, basin and escape radius; E6 (the dissection of
the hand-checkable specimen) was added; no prediction band was
touched.
Tiers: the spine theorem is a THEOREM for this cover and move
set (proof in L1/L2, engine leg exhaustive at the nine rows);
the burst trap's existence is exact and exhaustive at the
battery's scope (the six specimens exhibited); the radius-2
statement is an observation over every stall found so far.
"""

import sys
from functools import cmp_to_key

import explore_scale_clock as SC

# ----------------------------------------------------------------- #
# small exact helpers
# ----------------------------------------------------------------- #

def le(a, b):
    """Fraction a <= b by cross-multiplication (den >= 0)."""
    return a[0] * b[1] <= b[0] * a[1]

def cell_inside(ca, cb):
    """Interval of cell/interval ca inside interval of cb."""
    (la, ha), (lb, hb) = ca, cb
    return le(lb, la) and le(ha, hb)

def frac_cmp(a, b):
    left = a[0] * b[1]
    right = b[0] * a[1]
    return -1 if left < right else (1 if left > right else 0)

def cmp_steplex(ca, cb):
    """Per-step lexicographic deficit: compare counted length
    lists step by step, infinite (None) worse than finite, first
    strict difference decides."""
    for za, zb in zip(ca, cb):
        if za is None and zb is None:
            continue
        if za is None:
            return 1
        if zb is None:
            return -1
        c = frac_cmp(za, zb)
        if c:
            return c
    return 0

# ----------------------------------------------------------------- #
# runners: one policy, one row, any resource mode
# ----------------------------------------------------------------- #

def run_pol(J_list, pol5, B, W, horizon):
    """Returns (loss_triple, sig, counted_lengths). B None means
    unresourced (the 4-coordinate reader; delta is inert)."""
    if B is None:
        num, den, inf, trace = SC.run_reader(J_list, pol5[:4], horizon)
        counted = tuple(trace[n][2] for n in range(SC.N0, len(trace)))
        clens = [SC.ival_length(*c) for c in counted]
        return (num, den, inf), hash(counted), clens
    num, den, inf, sg, _, _, clens = SC.run_reader_banking(
        J_list, pol5, horizon, B, W)
    return (num, den, inf), sg, clens

def spine_trace(J_list, p, horizon, st=0, ss=0):
    """Counted committed intervals at pt = pc = p, unresourced."""
    trace = SC.run_reader(J_list, (st, ss, p, p), horizon)[3]
    return [trace[n][2] for n in range(SC.N0, horizon)]

# ----------------------------------------------------------------- #
# the landscape census (this rig's own, controlled against parent)
# ----------------------------------------------------------------- #

def census(space, sigd, lossd, clensd, daxis):
    """Quotient landscape of a single loss dict under the lex
    deficit: returns (members, nbrs, qloss, qranks, stalls,
    tie_adjacent_pairs, clens_by_sig)."""
    nbr = lambda p: SC.neighbors_cure(p, SC.AX_BASE, daxis)
    mem, nbrs, _key = SC.build_quotient(space, sigd, nbr)
    qloss = {}
    clens_by_sig = {}
    for p in space:
        s = sigd[p]
        if s in qloss:
            assert qloss[s] == (0, lossd[p]), "loss not trace-determined"
        else:
            qloss[s] = (0, lossd[p])
            clens_by_sig[s] = clensd[p]
    qranks = SC.qrank_map(mem, qloss)
    stalls = SC.qstalls(mem, qranks, nbrs)
    ties = set()
    for s in mem:
        for t in nbrs[s]:
            if SC.cmp_comp(qloss[s], qloss[t]) == 0:
                ties.add(tuple(sorted((s, t))))
    return mem, nbrs, qloss, qranks, stalls, ties, clens_by_sig

def flat_exit(s0, nbrs, qranks):
    """BFS the equal-rank flat containing s0; True iff some flat
    member has a strictly lower-ranked neighbor."""
    r = qranks[s0]
    seen, front = {s0}, [s0]
    while front:
        nxt = []
        for s in front:
            for t in nbrs[s]:
                if qranks[t] < r:
                    return True, len(seen)
                if qranks[t] == r and t not in seen:
                    seen.add(t)
                    nxt.append(t)
        front = nxt
    return False, len(seen)

# ----------------------------------------------------------------- #
# E1: controls against the parent landscape
# ----------------------------------------------------------------- #

def e1_controls(imgs, jlens):
    print("\nE1  CONTROLS: this rig's census on the parent's tables")
    ok = True
    for (B, W), want_comp, want_def in (((2, 0), 1, 0), ((2, 2), 0, 0)):
        space, tab, sigd, lagd = SC.setting_tables(imgs, jlens, B, W)
        daxis = SC.d_axis(W)
        sig8 = {p: tuple(sigd[(p, r)] for r in SC.ROWS8) for p in space}
        nbr = lambda p: SC.neighbors_cure(p, SC.AX_BASE, daxis)
        mem, nbrs, _key = SC.build_quotient(space, sig8, nbr)
        loss8 = {}
        for p in space:
            s = sig8[p]
            if s not in loss8:
                loss8[s] = (sum(lagd[(p, r)] for r in SC.ROWS8),
                            SC.agg([tab[(p, r)] for r in SC.ROWS8]))
        qr_comp = SC.qrank_map(mem, loss8)
        st_comp = SC.qstalls(mem, qr_comp, nbrs)
        qr_def = SC.qrank_map(mem, {s: (0, loss8[s][1]) for s in mem})
        st_def = SC.qstalls(mem, qr_def, nbrs)
        nbr_s = lambda p: SC.neighbors_single5(p, SC.AX_BASE, daxis)
        mem_s, nbrs_s, _k = SC.build_quotient(space, sig8, nbr_s)
        qr_defs = SC.qrank_map(mem_s, {s: (0, loss8[s][1])
                                       for s in mem_s})
        st_defs = SC.qstalls(mem_s, qr_defs, nbrs_s)
        print("  (B,W)=(%d,%d): composite cure stalls %d | "
              "deficit-order stalls single %d cure %d"
              % (B, W, len(st_comp), len(st_defs), len(st_def)))
        ok &= (len(st_comp) == want_comp and len(st_def) == want_def
               and len(st_defs) == want_def)
    SC.check("C1 census reproduces the parent landscape", ok)

# ----------------------------------------------------------------- #
# E2: the spine engine leg
# ----------------------------------------------------------------- #

def e2_spine(imgs):
    print("\nE2  THE SPINE LEG: single-reference patience diagonal")
    route_free = contain = monot = stall_free = True
    for row in SC.ROWS:
        J = imgs[row]
        traces = {}
        losses = {}
        for p in (0, 1, 2, 3):
            sigs = set()
            for st in (0, 1):
                for ss in (0, 1):
                    num, den, inf, tr = SC.run_reader(
                        J, (st, ss, p, p), SC.N_MAIN)
                    sigs.add(hash(tuple(
                        tr[n][2] for n in range(SC.N0, SC.N_MAIN))))
            if len(sigs) != 1:
                route_free = False
            traces[p] = spine_trace(J, p, SC.N_MAIN)
            losses[p] = SC.run_reader(J, (0, 0, p, p), SC.N_MAIN)[:3]
        for p in (1, 2, 3):
            for ca, cb in zip(traces[p - 1], traces[p]):
                if not cell_inside(ca, cb):
                    contain = False
            c = SC.cmp_lex(losses[p - 1], losses[p])
            same = traces[p - 1] == traces[p]
            if c > 0 or (c == 0 and not same):
                monot = False
        inf_loss = SC.run_reader(J, (0, 0, SC.INF_P, SC.INF_P),
                                 SC.N_MAIN)[:3]
        if SC.cmp_lex(losses[3], inf_loss) >= 0:
            stall_free = False
        print("  %s: spine losses ln %s | refuser shortfall ln %.2f"
              % (SC.fmt_row(row),
                 ["%.2f" % SC.ln_loss(losses[p]) for p in (0, 1, 2, 3)],
                 SC.ln_loss(inf_loss)))
    SC.check("C2(i) equal patience is route-free", route_free)
    SC.check("C2(ii) spine containment at every counted step", contain)
    SC.check("C2(iii) lex deficit monotone along the spine, "
             "strict across distinct classes", monot)
    SC.check("C2(iv) refuser strictly worst on the spine", stall_free)

# ----------------------------------------------------------------- #
# E3: the mechanism census off the spine
# ----------------------------------------------------------------- #

def e3_mechanism(imgs):
    print("\nE3  MECHANISM CENSUS: non-nested steps at mixed patience")
    total = 0
    for row in SC.ROWS:
        J = imgs[row]
        cells = {}
        for st in (0, 1):
            for ss in (0, 1):
                for pt in (0, 1, 2, 3):
                    for pc in (0, 1, 2, 3):
                        tr = SC.run_reader(
                            J, (st, ss, pt, pc), SC.N_MAIN)[3]
                        cells[(st, ss, pt, pc)] = [
                            tr[n][2] for n in range(SC.N0, SC.N_MAIN)]
        bad = 0
        for (st, ss, pt, pc), tr in cells.items():
            for (dt, dc) in ((0, -1), (-1, 0)):
                qt, qc = pt + dt, pc + dc
                if qt < 0 or qc < 0:
                    continue
                for ca, cb in zip(cells[(st, ss, qt, qc)], tr):
                    if not cell_inside(ca, cb):
                        bad += 1
        total += bad
        print("  %s: non-nested (policy, step) count %d"
              % (SC.fmt_row(row), bad))
    print("  total non-nested count %d (C3 guessed > 0)" % total)
    return total

# ----------------------------------------------------------------- #
# E4: the forge
# ----------------------------------------------------------------- #

def battery_worlds():
    """The designed-world battery: (name, digits-builder)."""
    worlds = []
    seen = set()
    tails = [(a,) for a in (1, 2, 3)] + \
            [(a, b) for a in (1, 2, 3) for b in (1, 2, 3)]
    for head in ((), (2,), (3,)):
        for tail in tails:
            digs = tuple(SC.cf_digits(list(head), list(tail), SC.N_MAIN))
            if digs in seen:
                continue
            seen.add(digs)
            worlds.append(("h%st%s" % ("".join(map(str, head)),
                                       "".join(map(str, tail))),
                           list(digs)))
    for j in (6, 8, 10, 12):
        digs = [1] * SC.N_MAIN
        digs[j] = 8
        worlds.append(("spike1@%d" % j, digs))
    for j in (8, 12):
        digs = SC.cf_digits([], [1, 2], SC.N_MAIN)
        digs[j] = 8
        worlds.append(("spike12@%d" % j, digs))
    worlds.append(("fib", SC.fib_word(SC.N_MAIN)))
    return worlds

SETTINGS = [(None, 0), (1, 0), (2, 0), (2, 2)]
HORIZONS = [16, SC.N_MAIN]

def e4_forge():
    print("\nE4  THE FORGE: designed-world stall hunt (lex deficit, "
          "behavioral quotient, cure moves)")
    worlds = battery_worlds()
    print("  battery: %d streams x maps (id, dbl) x %d settings x "
          "horizons %s" % (len(worlds), len(SETTINGS), HORIZONS))
    n_land = n_stall_land = n_ties = 0
    specimens = []
    tie_example = None
    for wname, digs in worlds:
        cyls = SC.cylinders(digs)
        for mp in ("id", "dbl"):
            J_full = SC.images(cyls, mp)
            for horizon in HORIZONS:
                J = J_full[:horizon]
                for (B, W) in SETTINGS:
                    daxis = SC.d_axis(W) if B is not None else [SC.INF_D]
                    space = SC.policy_space5(SC.AX_BASE, daxis)
                    sigd, lossd, clensd = {}, {}, {}
                    for p in space:
                        t, sg, cl = run_pol(J, p, B, W, horizon)
                        sigd[p], lossd[p], clensd[p] = sg, t, cl
                    mem, nbrs, qloss, qranks, stalls, ties, cbs = \
                        census(space, sigd, lossd, clensd, daxis)
                    n_land += 1
                    n_ties += len(ties)
                    if ties and tie_example is None:
                        tie_example = (wname, mp, horizon, B, W,
                                       sorted(ties)[0])
                    if stalls:
                        n_stall_land += 1
                        for s in stalls:
                            specimens.append(
                                (wname, mp, horizon, B, W, s, mem,
                                 nbrs, qloss, qranks, cbs))
    print("  landscapes %d | landscapes with stalls %d | "
          "adjacent value-tie pairs %d | stall specimens %d"
          % (n_land, n_stall_land, n_ties, len(specimens)))
    if tie_example is not None:
        w, mp, h, B, W, (s, t) = tie_example
        print("  first adjacent value tie: world %s/%s h=%d "
              "(B,W)=(%s,%d) — distinct behaviors, equal deficit"
              % (w, mp, h, B, W))
    return specimens, n_ties

def anatomy(spec, idx):
    wname, mp, horizon, B, W, s, mem, nbrs, qloss, qranks, cbs = spec
    print("\n  SPECIMEN %d: world %s/%s horizon %d (B,W)=(%s,%s)"
          % (idx, wname, mp, horizon, B, W))
    print("    class: %s | rank %d of %d | size %d"
          % (SC.summarize_class(mem[s]), qranks[s],
             max(qranks.values()) + 1, len(mem[s])))
    for p in sorted(mem[s], key=SC.pol_key):
        print("      member %s" % SC.fmt_pol5(p))
    for t in sorted(nbrs[s], key=lambda t: qranks[t]):
        print("      nbr %s rank %d dln %+.4f"
              % (SC.summarize_class(mem[t]), qranks[t],
                 SC.ln_loss(qloss[t][1]) - SC.ln_loss(qloss[s][1])))
    basin = 0
    for s2 in mem:
        t = SC.qdescend(s2, qranks, nbrs,
                        {u: min(SC.pol_key(p) for p in mem[u])
                         for u in mem}, True)
        if t == s:
            basin += 1
    print("    basin (best-improve descent) %d of %d classes"
          % (basin, len(mem)))
    print("    escape radius through the cure graph %s"
          % escape_radius(s, nbrs, qranks))
    tied = [t for t in nbrs[s] if SC.cmp_comp(qloss[s], qloss[t]) == 0]
    worse = [t for t in nbrs[s]
             if SC.cmp_comp(qloss[t], qloss[s]) > 0]
    print("    neighbors %d: tied %d, strictly worse %d"
          % (len(nbrs[s]), len(tied), len(worse)))
    if not tied:
        print("    -> STRICT LOCAL MIN (K2): no equal-loss neighbor")
        return "strict"
    has_exit, flat_size = flat_exit(s, nbrs, qranks)
    print("    -> TIE-FLAT STALL (K3): flat size %d, exit %s"
          % (flat_size, has_exit))
    # E5: the per-step-lex third instrument on this landscape
    order = sorted(mem, key=cmp_to_key(
        lambda a, b: cmp_steplex(cbs[a], cbs[b])))
    ranks2 = {order[0]: 0}
    r = 0
    for prev, cur in zip(order, order[1:]):
        if cmp_steplex(cbs[prev], cbs[cur]) < 0:
            r += 1
        ranks2[cur] = r
    still = (ranks2[s] > 0 and
             all(ranks2[t] >= ranks2[s] for t in nbrs[s]))
    print("    per-step-lex retest: still stalls %s" % still)
    return "flat-exit" if has_exit else "flat-basin"

def escape_radius(s, nbrs, qranks):
    """Fewest cure-graph moves from s to any class ranked below s."""
    seen, front, radius = {s}, [s], 0
    while front:
        radius += 1
        nxt = []
        for u in front:
            for t in nbrs[u]:
                if qranks[t] < qranks[s]:
                    return radius
                if t not in seen:
                    seen.add(t)
                    nxt.append(t)
        front = nxt
    return None

# ----------------------------------------------------------------- #
# E6: deep dissection of the hand-checkable specimen (added after
# the first run, which found the strict local minima; no prediction
# band was touched — this engine only prints the smallest specimen's
# per-step cells so the strictness is hand-verifiable)
# ----------------------------------------------------------------- #

def e6_dissect():
    print("\nE6  DISSECTION: spike1@10/dbl horizon 16 (B,W)=(2,0)")
    digs = [1] * 16
    digs[10] = 8
    J = SC.images(SC.cylinders(digs), "dbl")
    B, W = 2, 0
    daxis = SC.d_axis(W)
    space = SC.policy_space5(SC.AX_BASE, daxis)
    sigd, lossd, clensd = {}, {}, {}
    for p in space:
        t, sg, cl = run_pol(J, p, B, W, 16)
        sigd[p], lossd[p], clensd[p] = sg, t, cl
    mem, nbrs, qloss, qranks, stalls, ties, cbs = \
        census(space, sigd, lossd, clensd, daxis)
    print("  stream digits %s" % digs)
    print("  counted images (steps 8..15):")
    for n in range(SC.N0, 16):
        lo, hi = J[n]
        print("    n=%2d  J = [%d/%d, %d/%d]"
              % (n, lo[0], lo[1], hi[0], hi[1]))
    for s in stalls:
        reps = sorted(mem[s], key=SC.pol_key)
        print("  stall class %s:" % SC.summarize_class(mem[s]))
        show = [("STALL", reps[0])]
        for t in sorted(nbrs[s], key=lambda t: qranks[t]):
            show.append(("nbr", sorted(mem[t], key=SC.pol_key)[0]))
        for tag, p in show:
            tr = SC.run_reader_banking(J, p, 16, B, W)
            cl = tr[6]
            lnl = SC.ln_loss(lossd[p]) if not lossd[p][2] else None
            print("    %s %s  ln %s" % (tag, SC.fmt_pol5(p),
                  "INF(shortfall %.4f)" % SC.ln_frac(
                      lossd[p][0], lossd[p][1])
                  if lossd[p][2] else "%.4f" % lnl))
            cells = []
            for z in cl:
                cells.append("inf" if z is None
                             else "%d/%d" % (z[0], z[1]))
            print("      counted lengths: %s" % " ".join(cells))

# ----------------------------------------------------------------- #

def main():
    print("THE STALL-TIE QUESTION: is the closing shape a theorem?")
    print("=" * 70)
    imgs = SC.build_images(SC.N_MAIN)
    jlens = {row: SC.j_length_pairs(imgs[row]) for row in SC.ROWS}
    e1_controls(imgs, jlens)
    if SC.FAILURES:
        print("\nCONTROLS FAILED — no verdicts.")
        sys.exit(1)
    e2_spine(imgs)
    e3_mechanism(imgs)
    specimens, n_ties = e4_forge()
    kinds = []
    for i, spec in enumerate(specimens[:8]):
        kinds.append(anatomy(spec, i + 1))
    if len(specimens) > 8:
        print("  (%d further specimens not printed)"
              % (len(specimens) - 8))
    if not specimens:
        print("\n  -> DESERT (K4): zero stalls across the battery")
    else:
        e6_dissect()
    print("\n" + "=" * 70)
    if SC.FAILURES:
        print("FAILURES: %s" % ", ".join(SC.FAILURES))
        sys.exit(1)
    print("ALL CHECKS PASS")
    sys.exit(0)

if __name__ == "__main__":
    main()
