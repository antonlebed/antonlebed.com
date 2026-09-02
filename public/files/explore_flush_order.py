"""What removes the deep unflushed interior at the two pairs that
still owe the flush lemma an argument -- the REMOVAL ORDER of the
flushed-exempt closure, its seeds, and whether the cascade follows the
depth grading or crosses it.

THE QUESTION
------------
c_int = max(c_saf, L*) is an observation with both sides proved lower
bounds and no sufficiency proof (explore_flush_law.py). The lemma a
proof owes keeps its invariant R1 -- the safe states from which a
(0, 0)-holder is reachable under zero input by moves whose EVERY reply
is safe; a state is FLUSHED when it holds the zero residual -- and its
failing side has been narrowed to two pairs. Forgiving the flushed
states (exempt from having to serve, still legal targets) rescues
nothing at 13 of the 41 losing pairs, but at 11 of those R1 is a shell
of 6 to 17 states whose unflushed part is a rim of at most ten, all
one zero-input move from a flush (explore_flush_depth.py F3). The two
that are neither sit at V1 (1,1,1,2) x5, (s, s_0) = (1, 0) and (1, 1),
c = 3: there R1 carries 910 and 962 unflushed states of 925 and 977 to
depth 6 and the forgiveness saves NOT ONE of them. Those two are the
whole of what a proof owes over a DEEP unflushed interior, and they
are the cells where L* is set by a late tail rather than a late digit.

This rig asks what removes them. The flushed-exempt closure is a
greatest fixpoint; run it in synchronous ROUNDS and every removed
state carries a round. Round 1 is the SEEDS -- the unflushed states
with no output digit whose every reply lies in R1, which fail against
R1 itself and not against anything the closure has already taken.
Everything after is what the seeds cost. The reading is the shape:
whether the cascade runs down the depth grading (a state dying because
its neighbour one step nearer the flush died), whether a depth level
goes whole in one round, and what the seeds have that the states of R1
at the WINNING lookahead do not. The target was narrowed to two pairs
precisely so this can print states rather than counts of them.

Conventions are the engine's (explore_redundant_ostrowski.py, Game): a
state is (pos, branch set, pzd, pze), pzd recording that the last
input digit was zero and pze that the last output digit was; a branch
is the lattice point sum (e - m d)_k theta_k - M in the frame of the
current period. SAFE is the safety fixpoint
(explore_flush_price.safety_wins). A DIRECT failure of a set B is a
state of B with no digit keeping every reply in B. The DEPTH of a
state of R1 is its distance in the flush map -- 0 at a flushed state,
k when k zero-input moves through safe-replied moves reach one.

THE HAND-ATTACK (on paper, before the engine)
---------------------------------------------
H1  THE ROUND IS NOT THE PARENT'S TO HAND OVER. The greatest fixpoint
    is unique, but the ROUND a state leaves in is not: the parents'
    closure_exempt sweeps ASYNCHRONOUSLY (`for s in list(I)` with I
    mutating inside the loop), so a state can leave in the same pass
    as the state it depended on, and its round number would be an
    artifact of the id order the interning happened to give. The round
    is this rig's whole observable, so the iteration is rebuilt
    SYNCHRONOUS -- round r removes every non-exempt state of I_{r-1}
    with no digit all of whose replies lie in I_{r-1} -- and the
    fixpoint it reaches is checked against the parent's (K0c). Nothing
    else in the rig is new: the game, the box, the safety fixpoint,
    the flush refinement and the direct-failure set are the parents'.
H2  THE SEEDS ARE NON-EMPTY AND THE ROUNDS PARTITION THE UNFLUSHED
    SIDE. Round 1 is exactly the unflushed part of closure(g, R1)'s
    direct failures, and the parent found an unflushed direct failure
    at every pair holding an unflushed state (explore_flush_seed.py
    K2b), so round 1 is non-empty at both pairs. No unflushed state
    survives (explore_flush_depth.py F3), so every one of the 910 and
    962 carries a round and the profile sums to those counts.
H3  DEPTH SHOULD NOT GRADE THE CASCADE, and the transplant is marked.
    If the collapse ran along the flush chain, a state at depth d
    would die because its depth-(d-1) neighbour died and the round
    would be a function of the depth -- monotone one way or the other.
    The parent already refuted the state-level reading of depth where
    survivors exist: 572 survivors sit at depth 1 while 2,822 states
    at depth >= 2 die, so depth is a property of the SET and not a
    mark the state carries (explore_flush_depth.py F5). TRANSPLANT,
    marked: that was measured where something survives and here
    nothing does, so the mechanism is imported and not the reading.
    PREDICTED: neither direction is a function -- some round carries
    two depths and some depth carries two rounds.
H4  A LEVEL COLLAPSING WHOLE IS THE RIVAL SHAPE, and a level of ONE
    state collapses whole by arithmetic. So the reading is restricted
    to levels of two or more and the singletons are counted apart.
H5  THE PROFILE'S SHAPE IS THE THREAD'S VERDICT AND CARRIES NO PRIOR.
    A long thin cascade -- many rounds of a few states -- is an
    obstruction propagating state by state with no lemma in sight. A
    short fat one -- two or three rounds of hundreds -- is a
    population failing on one shared ground, and that ground is the
    proof route. Printed either way; the weighing is after the run.
H6  A CHARACTERIZATION OF THE SEEDS IS ONLY A CANDIDATE UNTIL THE
    WINNING LOOKAHEAD REFUSES IT. At c = c_int the winning set is
    exactly R1 (explore_flush_closure.py), so R1 has no direct failure
    there and there are no seeds to compare against. What CAN be
    compared is the label: any property carried by every seed at c = 3
    and by some state of R1 at c = 4 cannot be the reason the seeds
    fail, because the c = 4 state carrying it does not fail. That is a
    negative control on every candidate, and it is cheap.
    UNDER-READ, and K8 is the correction: what can be compared is not
    only the label but the STATE, the whole object the game interns.
    The slate stays as written -- this is the record of what was
    thought before the run -- and F4 carries what the comparison
    actually was.
H7  THE PRICE FIXES c_saf AT BOTH CELLS BEFORE THE ENGINE RUNS. A
    losing pair is c_saf <= c < c_int, the corpus reads c_int = 4 at
    both cells and a flush price of 1 at 28 grid cells and 2 at one
    (OSTROWSKI section III), and both of this rig's pairs are at
    c = 3. So one of the two cells is the grid's ONLY price-2 cell,
    with c_saf = 2 and a second losing pair at c = 2, and the other
    has c_saf = 3 and c = 3 as its only one. Which is which the run
    says; that exactly one of them is the price-2 cell is a
    prediction, and the c = 2 pair of that cell is read alongside.
TRANSPLANT, marked: the game, its box, the grid, the frozen c_int /
c_saf readings, the safety fixpoint, the flush refinement, the
direct-failure set and the exempt closure are the parents'
(explore_redundant_ostrowski.py, explore_flush_price.py,
explore_flush_closure.py, explore_flush_seed.py,
explore_flush_depth.py); nothing here re-derives them.

PREDICTIONS, FIXED BEFORE THE RUN (observables -- what the rig PRINTS,
never what they would mean).
  K0 (controls, run FIRST; nothing below is read if any leg is red)
     (a) at both cells c_int = 4, and exactly one of them reads
         c_saf = 2 with the other at 3 (H7).
     (b) at c = 3 the two pairs reproduce the parent's counts: R1 of
         925 and 977 states, 910 and 962 of them unflushed, depth 6
         (explore_flush_depth.py F3).
     (c) the synchronous rounds reach the parent's own fixpoint at
         every pair read -- closure_exempt(g, R1, flushed) to the
         state -- and at the two target pairs that fixpoint is exactly
         the flushed states.
  K1 THE ROUND PROFILE (H5), at each target pair: the number of
     rounds, and per round the count removed with its depth
     histogram. Printed, no numeric prediction; the shape is read
     after the run.
  K2 THE SEEDS (H2), per pair: their count, their depth histogram,
     and per seed the position, pzd, pze, branch-set size and cap
     signature (how many of its output digits are broken by the
     LARGEST LEGAL input reply against how many only by a smaller
     one, explore_flush_seed.cap_signature). PREDICTED: non-empty at
     both. KILL, as an observable: an empty round 1 at either pair,
     which would contradict the parent's K2b.
  K3 IS THE ROUND A FUNCTION OF THE DEPTH, OR THE DEPTH OF THE ROUND?
     The round-by-depth contingency table at each pair. PREDICTED
     (H3): neither -- some round carries two or more depths AND some
     depth carries two or more rounds. KILL, as an observable: every
     round confined to one depth, or every depth to one round, which
     would make the cascade the flush chain itself.
  K4 DOES A LEVEL GO WHOLE? Per depth level of two or more states,
     whether all of it leaves in one round; the count of such levels
     and of the singletons apart (H4). Printed, no prediction.
  K5 THE NEGATIVE PANEL (H6): for each label value carried by EVERY
     seed at c = 3, whether some state of R1 at c = 4 carries it too.
     Labels: the position, pzd, pze, the branch-set size, whether the
     branch set holds a zero coordinate, and the cap signature's two
     halves. PREDICTED: every such value is matched at c = 4, so no
     label of this list singles the seeds out. KILL, as an
     observable: a value carried by every seed and by no state of R1
     at c = 4 -- which would BE a candidate reason and the route the
     thread is asking for.
  K6 state counts, wall-clock and peak per stage.
  K8 POST-HOC, and the one this leg turns on. K5 and K7 compare
     DESCRIPTIONS of the seed; this compares the seed's own STATE --
     the complete object the game interns, position and branch set and
     both digit-history flags -- against the states of R1 at the
     winning lookahead. A state occurring there is a state that does
     not fail there, so any predicate holding on every seed holds on
     it too and separates nothing. THE CONTROL IS THE WHOLE TEST: the
     same question over ALL the unflushed states says whether verbatim
     recurrence is a real constraint or something every state of the
     losing game satisfies.
  K7 POST-HOC, added after the run and predicted by nothing: the
     seeds' depth PARITY against the unflushed population's, and the
     seeds' full label TUPLE against R1 at the winning lookahead --
     the tuple because K5 tests labels one at a time and a conjunction
     can separate where no single label does. Both are read at the
     tier a post-hoc reading earns, and the parity is swept over the
     whole corpus in s2 rather than claimed from the two pairs.

THE DESIGN ---------- One stage, s1, over the two target cells of the grid --
V1 (1,1,1,2) at m = 5 with (s, s_0) = (1, 0) and (1, 1) -- plus, at whichever
of them prices at 2, its second losing pair at c = 2. Per cell the lookahead
ascends 0..c_int with the parent's cap (h3_bound, else LOOKCAP), c_saf the
least c whose SAFE holds every init and c_int the least whose W does, so both
controls come off the same ascent that builds the games. Per losing pair:
Game(win, 1, m, (0,), c, s, s_0), SAFE by the parent's safety loop, R1 and its
depth map by the parent's flush refinement of SAFE, the direct failures by the
parent's closure, and then the synchronous rounds of the flushed-exempt
closure, each round's removals recorded with their depths. The seeds are round
1 and are printed state by state (position, pzd, pze, branch count, cap
signature), capped at SEED_PRINT with the profile printed whole either way. The
c = c_int pass is read for K5's negative panel only: its R1 and the label
values every seed shares. Stage s2 (added after s1 ran, to give s1's one
generalizable reading its range) sweeps every losing pair of the corpus -- the
grid and the band -- and prints, per pair, the seeds with their depth histogram
against the unflushed population's own odd share and against R1's depth. Stage
s3 (added at the audit, when scoping F4 showed the decisive comparison was a
second of compute) reads the seeds' own STATES against R1 at the winning
lookahead, with every unflushed state as its control. Cells by ORDER_CELLS, the
stages by ORDER_STAGES, one process per stage under memwatch.

FINDINGS (post-run; the prints are the record. s1 1 s at 127 MB, s2
37 s at 349 MB, one process each under memwatch.)
----------------------------------------------
F1  THE CONTROLS HOLD, AND ONE HAND-DERIVATION DOES NOT. K0(b) and
    K0(c) are green at both target pairs -- R1 of 925 and 977 states
    with 910 and 962 unflushed to depth 6, the parent's counts to the
    state, and the SYNCHRONOUS fixpoint equal to the parent's
    asynchronous one and equal to the 15 flushed states at both -- and
    s2 reproduces the corpus's 41 losing pairs with 7 entirely
    flushed. H7 is REFUTED and K0(a) with it: both cells read
    c_saf = 3 and price 1, neither is the grid's one price-2 cell, and
    there is no second losing pair to read. The inference was that a
    price-2 cell must carry a c = 3 losing pair; the corpus's nonzero
    price also lands at c_int = 2 cells, where price 2 means
    c_saf = 0 and the losing pairs are c = 0 and c = 1 (OSTROWSKI
    section III). The refuted half is an arithmetic claim about the
    corpus's bookkeeping and touches nothing the rig builds; K0(b) and
    K0(c), which are the build's own fidelity, decide that.
F2  THE CASCADE CROSSES THE DEPTH GRADING, BOTH WAYS (K1, K3, K4;
    observation at the two pairs). Eight rounds at both, removing
    20, 48, 110, 137, 190, 222, 182, 1 and 22, 49, 112, 149, 216, 227,
    186, 1 -- rising for six rounds and ending on a SINGLE state at
    depth 4 at both. Seven of the eight rounds carry two or more
    depths and every one of the six depths carries two or more rounds,
    so the round is not a function of the depth nor the depth of the
    round; and NO depth level of two or more states leaves in one
    round, 0 of 6 at both pairs, with no singleton level to make the
    reading cheap. So the collapse is neither a chain down the flush
    grading nor a level going whole: a state does not die because the
    state one step nearer the flush died. H3 holds and K3's kill
    missed. The amplification is the size of it -- twenty-odd seeds
    cost 910 and 962 states in eight rounds.
F3  THE SEEDS ARE TWENTY AND TWENTY-TWO, AND THEY ARE UNIFORM (K2;
    observation). 2.2% and 2.3% of the unflushed side, and exactly the
    direct failures of R1 outside the flushed states, which is the
    parent's K2b set. Every seed at both pairs: the last input digit
    ZERO (pzd), no zero branch, position 2 or 5 of the game's six
    (the engine runs positions 0..P + 1 and wraps to 2, so these are
    phases 2 and 1 of the period-4 window),
    a branch set of 1 or 10, and every one of its three output digits
    broken by the LARGEST LEGAL input reply with none broken only by a
    smaller one. That last is the corpus's own majority mechanism at
    100% here, against 700 of 1,005 grid digits and 609 of 653 band
    ones (explore_flush_seed.py K3).
F4  THE SEEDS RECUR VERBATIM AT THE WINNING LOOKAHEAD, SO NO
    LOOKAHEAD-FREE INVARIANT SEPARATES THEM (K5, K7, K8;
    observation), and this is what the leg turns on. Only two of them
    are shared by every seed -- pzd true and no zero branch -- and R1
    at the WINNING lookahead carries them at 1,116 and 2,095 states,
    and 1,174 and 2,213. Taking the labels as a TUPLE does not rescue
    it: the seeds fall into 6 distinct (position, pzd, pze, branch
    count, zero) tuples at each pair and every one of the twelve is
    carried by states of R1 at the winning lookahead, 15 to 89 of
    them. And the STATES settle it where the descriptions only
    suggest it (K8): every one of the 20 and 22 seeds occurs VERBATIM
    in R1 at the winning lookahead -- the same position, the same
    branch set point for point, the same two digit-history flags --
    among states that do not fail there. The control says the test
    constrains: only 439 of the 910 unflushed states and 468 of the
    962 recur that way, so verbatim recurrence is a property fewer
    than half of them have and every seed has. WHAT THAT SETTLES, and
    exactly that: having a digit whose every reply stays inside is a
    function of the STATE AND THE LOOKAHEAD and not of the state --
    the same object fails at c = 3 and does not at c = 4, because one
    lookahead changes which input digits are legal and which lattice
    vector the reply subtracts. So no property of the state ALONE is
    equivalent to it, and no lookahead-free invariant can be the
    separating one. It does NOT exclude a proof whose argument uses c;
    the lemma is indexed by c, so such a proof was never on the table
    to exclude. What the seeds say is where the c has to enter.
F5  THE ODD-DEPTH SEED LAW IS LOCAL AND NOT A LAW (K7 swept, s2;
    observation over the 23 deep pairs). At the two target pairs every
    seed sits at ODD depth -- 20 of 20 and 22 of 22, at depths 1, 3
    and 5 and never 2, 4 or 6, against 58% odd in the unflushed
    population -- which is why it was swept. It holds at 13 of the 23
    pairs whose R1 has depth 2 or more and fails at 10, and at V2
    (2,1,3,1) x2 (1, 0) and (1, 1) every seed sits at depth 2, wholly
    EVEN. The parity is a fact about these pairs and carries no rule.
F6  WHERE THE SEEDS SIT IS A CORPUS-WIDE READING, AND IT NAMES THE
    WINDOW RATHER THAN THE CELLS (s2; observation, 23 deep pairs). The
    deepest seed of a pair is 1 at 10 pairs, 2 at 9, 3 at 2 and 5 at
    2: strictly shallower than R1's own depth at 18 of the 23, and at
    depth <= 2 at 19. Every one of the four pairs whose seeds climb
    past depth 2 is the V1 (1,1,1,2) window -- x3 (2,2) and x4 (3,3)
    at c = 1 reaching depth 3, and the two target pairs reaching 5 of
    R1's 6. So the direct failures live against the flushed core
    almost everywhere in the corpus, and the one window where they
    climb into the interior is the window whose L* a late tail sets.

  TIER. F2 through F4 are OBSERVATIONS at the two pairs, F5 and F6
  observations exhaustive at the corpus's 41 losing pairs. THE
  THREAD'S KILL IS MET: this leg hands back NO proof route for the
  lemma that at c >= max(c_saf, L*) every state of R1 has a digit
  keeping every reply in R1, and both routes it was built to test came
  back negative. F2 refuses the flush grading an inductive role -- the
  cascade crosses it in both directions, so a proof by induction on
  the depth has nothing to induct along. F4 refuses a LOOKAHEAD-FREE
  state invariant, and this half is an ARGUMENT rather than a pattern:
  the seeds -- the only states failing against R1 itself rather than
  against what the closure already took -- occur VERBATIM in R1 at the
  winning lookahead, so any predicate true of every seed is true of a
  state that does not fail, whatever the predicate reads. Failing is
  therefore a property of the state AND the lookahead together, and an
  invariant on states alone cannot be the thing proved. That is a
  constraint on the proof and not its impossibility -- a proof may use
  c, and the lemma being indexed by c it must -- so what the leg hands
  back is where the c has to enter and no route through it. What
  survives the leg is F6,
  which is about the FAILING side and not the winning one: it moves
  the phenomenon from two cells to one window, and it is the shape any
  later attempt would start from -- an attempt that must now read
  something the state does not carry at all, its reachability or the
  strategy that reached it.

RUN RECORD. ORDER_STAGES=s1, ORDER_STAGES=s2 and ORDER_STAGES=s3, each
python memwatch.py explore_flush_order.py; peaks and walls in the
findings header; nothing ran bare.
"""

import os
import sys
import time
from collections import Counter

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from explore_redundant_ostrowski import (               # noqa: E402
    GRID, WINDOWS, Game, LOOKCAP, h3_bound)
from explore_flush_price import BAND, window_of         # noqa: E402
from explore_flush_closure import safety_set, closure   # noqa: E402
from explore_flush_seed import (                        # noqa: E402
    flush_refine, closure_exempt, cap_signature)

CELLS = [("V1 (1,1,1,2)", (1, 1, 1, 2), 5, 1, 0),
         ("V1 (1,1,1,2)", (1, 1, 1, 2), 5, 1, 1)]
PARENT_R1 = {(1, 0): (925, 910, 6), (1, 1): (977, 962, 6)}
SEED_PRINT = 40


def hist_str(h):
    return ",".join("%d:%d" % (d, h[d]) for d in sorted(h)) or "-"


def rounds_exempt(g, base, exempt):
    """H1: the flushed-exempt closure run SYNCHRONOUSLY -- round r
    removes every non-exempt state of I_{r-1} with no digit all of
    whose replies lie in I_{r-1}. Returns the surviving set and the
    removals per round, in order."""
    I = set(base)
    out = []
    while True:
        gone = set()
        for s in I:
            if s in exempt:
                continue
            if not any(all(s2 in I for _x, s2 in succ)
                       for succ in g.trans[s].values()):
                gone.add(s)
        if not gone:
            return I, out
        out.append(gone)
        I -= gone


def labels_of(g, i):
    """K5: the labels the panel may test. Every entry is a property of
    the STATE alone -- readable at any lookahead, which is what makes
    the comparison against the winning lookahead mean anything. The cap
    signature is deliberately NOT here: it is read against a set, and
    against R1 at the winning lookahead it is zero for every state by
    construction, so it would separate the seeds vacuously."""
    pos, br, pzd, pze = g.states[i]
    return dict(pos=pos, pzd=pzd, pze=pze, nbr=len(br),
                zero=((0, 0) in br))


def read_cell(win, m, s, s0, top):
    """Ascend c = 0..c_int, keeping the losing pairs' games and the
    winning one's R1."""
    rows = []
    c_int = c_saf = None
    win_R1 = win_g = None
    for look in range(top + 1):
        t0 = time.time()
        g = Game(win, 1, m, (0,), look, s, s0)
        S = safety_set(g)
        R1, dist = flush_refine(g, S)
        if c_saf is None and all(i in S for i in g.init):
            c_saf = look
        winning = all(i in g.W for i in g.init)
        if winning:
            c_int = look
            win_R1, win_g = R1, g
            rows.append(dict(look=look, win=True, g=g, R1=R1, dist=dist,
                             states=g.n_states, wall=time.time() - t0))
            break
        rows.append(dict(look=look, win=False, g=g, R1=R1, dist=dist,
                         states=g.n_states, wall=time.time() - t0))
    return c_int, c_saf, rows, win_g, win_R1


def report_pair(name, m, s, s0, look, g, R1, dist, tallies):
    holds = set(i for i in R1 if g.holds0[i])
    unf = R1 - holds
    depth = max(dist.values()) if R1 else 0
    _I, direct = closure(g, R1)
    surv, rnds = rounds_exempt(g, R1, holds)
    ref = closure_exempt(g, R1, holds)
    print("  %s x%d (%d,%d) c=%d  states %d  R1 %d (%df, %d unflushed)  "
          "depth %d" % (name, m, s, s0, look, g.n_states, len(R1),
                        len(holds), len(unf), depth))
    want = PARENT_R1.get((s, s0)) if look == 3 else None
    if want is not None:
        got = (len(R1), len(unf), depth)
        print("    K0(b) parent's counts %s  got %s  %s"
              % (str(want), str(got), "ok" if got == want else "BAD"))
        tallies["k0b_bad"] += 0 if got == want else 1
    same = surv == ref
    print("    K0(c) synchronous fixpoint == the parent's: %s;  survivors "
          "%d, the flushed states %d, equal: %s"
          % ("ok" if same else "BAD", len(surv), len(holds),
             "yes" if surv == holds else "NO"))
    tallies["k0c_bad"] += 0 if same else 1

    removed = sum(len(r) for r in rnds)
    print("    K1 rounds %d, removing %d of %d unflushed  %s"
          % (len(rnds), removed, len(unf),
             "ok" if removed == len(unf) else "PARTIAL"))
    for r, gone in enumerate(rnds, 1):
        print("       round %-3d n=%-5d depths %s"
              % (r, len(gone), hist_str(Counter(dist[i] for i in gone))))

    seeds = rnds[0] if rnds else set()
    seed_direct = seeds == (direct - holds)
    print("    K2 seeds %d  depths %s;  == the direct failures outside the "
          "flushed states: %s"
          % (len(seeds), hist_str(Counter(dist[i] for i in seeds)),
             "yes" if seed_direct else "NO"))
    tallies["k2_empty"] += 1 if not seeds else 0
    for n, i in enumerate(sorted(seeds)):
        if n >= SEED_PRINT:
            print("       ... %d more, the profile above is whole"
                  % (len(seeds) - SEED_PRINT))
            break
        lab = labels_of(g, i)
        by_cap, other = cap_signature(g, i, R1)
        print("       seed pos %d pzd %-5s pze %-5s branches %-4d zero %-5s "
              "digits broken by the largest legal reply %d, by a smaller "
              "one %d  depth %d"
              % (lab["pos"], lab["pzd"], lab["pze"], lab["nbr"],
                 lab["zero"], by_cap, other, dist[i]))

    rd = {}
    for r, gone in enumerate(rnds, 1):
        for i in gone:
            rd.setdefault(r, Counter())[dist[i]] += 1
    dr = {}
    for r, gone in enumerate(rnds, 1):
        for i in gone:
            dr.setdefault(dist[i], Counter())[r] += 1
    multi_r = sum(1 for r in rd if len(rd[r]) > 1)
    multi_d = sum(1 for d in dr if len(dr[d]) > 1)
    print("    K3 rounds carrying two or more depths: %d of %d;  depths "
          "carrying two or more rounds: %d of %d;  a function either way: "
          "%s" % (multi_r, len(rd), multi_d, len(dr),
                  "YES" if (multi_r == 0 or multi_d == 0) else "no"))
    for d in sorted(dr):
        print("       depth %-2d n=%-5d rounds %s"
              % (d, sum(dr[d].values()),
                 ",".join("%d:%d" % (r, dr[d][r]) for r in sorted(dr[d]))))
    whole = [d for d in dr if sum(dr[d].values()) >= 2 and len(dr[d]) == 1]
    single = [d for d in dr if sum(dr[d].values()) == 1]
    odd = sum(1 for i in seeds if dist[i] % 2)
    odd_u = sum(1 for i in unf if dist[i] % 2)
    print("    K7 (post-hoc, not predicted) seeds at ODD depth: %d of %d; "
          " unflushed states at odd depth: %d of %d (%.0f%%)"
          % (odd, len(seeds), odd_u, len(unf), 100.0 * odd_u / len(unf)))
    print("    K4 depth levels of two or more leaving in ONE round: %d of "
          "%d;  singleton levels: %d"
          % (len(whole), sum(1 for d in dr if sum(dr[d].values()) >= 2),
             len(single)))
    return seeds


def negative_panel(g3, seeds, g4, R1_4):
    """K5: every label value EVERY seed carries, against R1 at the
    winning lookahead."""
    if not seeds:
        print("    K5 no seeds; the panel is vacuous")
        return
    labs = [labels_of(g3, i) for i in seeds]
    shared = {}
    for key in ("pos", "pzd", "pze", "nbr", "zero"):
        vals = set(l[key] for l in labs)
        if len(vals) == 1:
            shared[key] = vals.pop()
    if not shared:
        print("    K5 no label value is carried by EVERY seed; the panel "
              "has nothing to test")
        return
    at4 = [labels_of(g4, i) for i in R1_4]
    unmatched = []
    for key, v in sorted(shared.items()):
        hit = sum(1 for l in at4 if l[key] == v)
        print("    K5 every seed has %s = %s;  states of R1 at the winning "
              "lookahead carrying it: %d" % (key, v, hit))
        if hit == 0:
            unmatched.append(key)
    print("    K5 labels the winning lookahead does NOT match: %s"
          % (", ".join(unmatched) if unmatched else "none"))
    keys = ("pos", "pzd", "pze", "nbr", "zero")
    tup = set(tuple(l[k] for k in keys) for l in labs)
    tup4 = Counter(tuple(l[k] for k in keys) for l in at4)
    miss = sorted(t for t in tup if not tup4[t])
    print("    K7 (post-hoc, not predicted) the seeds' full label TUPLES "
          "(%s): %d distinct;  carried by no state of R1 at the winning "
          "lookahead: %d" % (", ".join(keys), len(tup), len(miss)))
    for t in sorted(tup):
        print("       %s  seeds %d  at the winning lookahead %d"
              % (str(t), sum(1 for l in labs
                             if tuple(l[k] for k in keys) == t), tup4[t]))


def s1_cells():
    print("== s1  the two pairs that owe the lemma an argument: the "
          "removal ORDER of the flushed-exempt closure, its seeds, the "
          "round against the depth, and the seeds' labels against R1 at "
          "the winning lookahead")
    t0 = time.time()
    tallies = dict(k0b_bad=0, k0c_bad=0, k2_empty=0, price=Counter(),
                   cint_ok=True)
    pick = os.environ.get("ORDER_CELLS")
    keep = set(int(i) for i in pick.split(",")) if pick else None
    for n, (name, period, m, s, s0) in enumerate(CELLS):
        if keep is not None and n not in keep:
            continue
        win = window_of(period)
        hb = h3_bound(win, m, s, s0)
        top = LOOKCAP if hb is None else hb
        c_int, c_saf, rows, g4, R1_4 = read_cell(win, m, s, s0, top)
        price = None if (c_int is None or c_saf is None) else c_int - c_saf
        tallies["price"][price] += 1
        tallies["cint_ok"] = tallies["cint_ok"] and c_int == 4
        print("  == %s x%d (%d,%d)  c_int %s  c_saf %s  price %s"
              % (name, m, s, s0, c_int, c_saf, price))
        for r in rows:
            if r["win"] or c_saf is None or r["look"] < c_saf:
                continue
            seeds = report_pair(name, m, s, s0, r["look"], r["g"], r["R1"],
                                r["dist"], tallies)
            if r["look"] == 3 and g4 is not None:
                negative_panel(r["g"], seeds, g4, R1_4)
    print("== s1 summary")
    print("  K0(a) c_int = 4 at both: %s.  H7's price half is REFUTED and "
          "stays printed as the record -- it predicted one cell at price 2, "
          "and both read price 1 (prices %s); the corpus's one price-2 grid "
          "cell sits at c_int = 2, where price 2 means c_saf = 0. Nothing "
          "the rig BUILDS depends on it; K0(b) and K0(c) are that."
          % ("ok" if tallies["cint_ok"] else "BAD",
             hist_str(Counter(tallies["price"]))))
    print("  K0(b) parent-count mismatches: %d" % tallies["k0b_bad"])
    print("  K0(c) synchronous-fixpoint mismatches: %d" % tallies["k0c_bad"])
    print("  K2 pairs with an empty round 1: %d" % tallies["k2_empty"])
    print("  K6 s1 wall %.0f s" % (time.time() - t0))


def seed_parity(g, R1, dist):
    """s2: the depths of R1's direct failures outside the flushed
    states, against the depths of the unflushed states themselves."""
    holds = set(i for i in R1 if g.holds0[i])
    unf = R1 - holds
    _I, direct = closure(g, R1)
    seeds = direct - holds
    return (seeds, unf, Counter(dist[i] for i in seeds),
            Counter(dist[i] for i in unf))


def sweep_cell(win, name, m, s, s0, top, tallies):
    c_saf = None
    for look in range(top + 1):
        g = Game(win, 1, m, (0,), look, s, s0)
        S = safety_set(g)
        R1, dist = flush_refine(g, S)
        if c_saf is None and all(i in S for i in g.init):
            c_saf = look
        if all(i in g.W for i in g.init):
            return
        if c_saf is None:
            continue
        seeds, unf, sh, uh = seed_parity(g, R1, dist)
        if not unf:
            tallies["allflush"] += 1
            continue
        tallies["pairs"] += 1
        depth = max(dist.values())
        odd = sum(sh[d] for d in sh if d % 2)
        odd_u = sum(uh[d] for d in uh if d % 2)
        trivial = depth == 1
        tallies["trivial" if trivial else "deep"] += 1
        smax = max(sh) if sh else 0
        if not trivial:
            tallies["seed_depth"][smax] += 1
            tallies["below"] += 1 if smax < depth else 0
            tallies["shallow"] += 1 if smax <= 2 else 0
            if smax > 2:
                tallies["climb"].append((name, m, s, s0, look, depth, smax))
        allodd = odd == len(seeds) and seeds
        if not trivial:
            tallies["deep_allodd"] += 1 if allodd else 0
            if not allodd:
                tallies["bad"].append((name, m, s, s0, look, depth,
                                       hist_str(sh)))
        if not seeds:
            tallies["noseed"] += 1
        print("    %-14s x%d (%d,%d) c=%d  depth %-2d  seeds %-4d %s  odd "
              "%d/%d;  unflushed %d, odd %d (%.0f%%)  %s"
              % (name, m, s, s0, look, depth, len(seeds), hist_str(sh),
                 odd, len(seeds), len(unf), odd_u,
                 100.0 * odd_u / len(unf),
                 "trivial (depth 1)" if trivial
                 else ("ALL ODD" if allodd
                       else ("ALL EVEN" if odd == 0 else "MIXED"))))


def s2_sweep():
    print("== s2  the seeds' depth parity over every losing pair of the "
          "corpus: per pair the depth of R1, the seeds and their depth "
          "histogram, against the unflushed population's own odd share")
    t0 = time.time()
    tallies = dict(pairs=0, allflush=0, trivial=0, deep=0, deep_allodd=0,
                   noseed=0, bad=[], below=0, shallow=0, climb=[],
                   seed_depth=Counter())
    print("  the grid")
    for name, period in WINDOWS:
        win = window_of(period)
        for m in (2, 3, 4, 5):
            for s, s0 in GRID:
                if (s, s0) == (0, 0):
                    continue
                hb = h3_bound(win, m, s, s0)
                sweep_cell(win, name, m, s, s0,
                           LOOKCAP if hb is None else hb, tallies)
    print("  the band")
    for name, period, m, s, _want in BAND:
        sweep_cell(window_of(period), name, m, s, s, LOOKCAP, tallies)
    print("== s2 summary")
    print("  losing pairs read %d (parent: 41), entirely flushed %d "
          "(parent: 7)" % (tallies["pairs"] + tallies["allflush"],
                           tallies["allflush"]))
    print("  pairs holding an unflushed state: %d;  depth 1 (the parity is "
          "vacuous there): %d;  depth >= 2: %d"
          % (tallies["pairs"], tallies["trivial"], tallies["deep"]))
    print("  of the depth >= 2 pairs, every seed at ODD depth: %d of %d"
          % (tallies["deep_allodd"], tallies["deep"]))
    print("  pairs with NO seed at all: %d" % tallies["noseed"])
    print("  of the depth >= 2 pairs, the DEEPEST seed: %s;  strictly "
          "shallower than R1's own depth at %d of %d;  at depth <= 2 at %d"
          % (hist_str(tallies["seed_depth"]), tallies["below"],
             tallies["deep"], tallies["shallow"]))
    for c in tallies["climb"]:
        print("    seeds past depth 2: %s x%d (%d,%d) c=%d  R1 depth %d, "
              "deepest seed %d" % c)
    for b in tallies["bad"]:
        print("    NOT ALL ODD  %s x%d (%d,%d) c=%d depth %d  seed depths %s"
              % b)
    print("  K6 s2 wall %.0f s" % (time.time() - t0))


def s3_states():
    """K8: the seeds' own STATES against R1 at the winning lookahead --
    the complete state object and not a description of it."""
    print("== s3  the seeds' own STATES against R1 at the winning "
          "lookahead: how many of the c = 3 states occur VERBATIM -- "
          "position, branch set, both digit-history flags -- among the "
          "states of R1 at c = c_int, which do not fail")
    t0 = time.time()
    for name, period, m, s, s0 in CELLS:
        win = window_of(period)
        hb = h3_bound(win, m, s, s0)
        top = LOOKCAP if hb is None else hb
        c_int, _c_saf, rows, g4, R1_4 = read_cell(win, m, s, s0, top)
        r3 = next(r for r in rows if r["look"] == 3)
        g3, R1, dist = r3["g"], r3["R1"], r3["dist"]
        holds = set(i for i in R1 if g3.holds0[i])
        unf = R1 - holds
        _I, direct = closure(g3, R1)
        seeds = direct - holds
        full4 = set(g4.states[i] for i in R1_4)
        _I4, direct4 = closure(g4, R1_4)
        hit = lambda ss: sum(1 for i in ss if g3.states[i] in full4)
        print("  %s x%d (%d,%d)  c_int %d;  R1 there %d states, %d of them "
              "direct failures" % (name, m, s, s0, c_int, len(R1_4),
                                   len(direct4)))
        print("    K8 c = 3 states occurring VERBATIM in R1 at c = %d: "
              "seeds %d of %d;  every unflushed state %d of %d;  the "
              "flushed states %d of %d"
              % (c_int, hit(seeds), len(seeds), hit(unf), len(unf),
                 hit(holds), len(holds)))
        print("    K8 the seeds' depths there: %s"
              % hist_str(Counter(dist[i] for i in seeds
                                 if g3.states[i] in full4)))
    print("  K6 s3 wall %.0f s" % (time.time() - t0))


STAGES = {"s1": s1_cells, "s2": s2_sweep, "s3": s3_states}


def main():
    for name in os.environ.get("ORDER_STAGES", "s1,s2,s3").split(","):
        STAGES[name.strip()]()


if __name__ == "__main__":
    main()
