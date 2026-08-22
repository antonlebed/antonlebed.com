"""THE PINNED FRESHENING WALK: which object is non-monotone, and why.

THE QUESTION
------------
At a present-pinned class the only cure move left is FRESHENING one
coordinate, and the reader corpus's open edge is a two-step statement
about it: where no member's single freshening lands nested and strictly
improving, some member's SECOND freshening does
(explore_pinned_composite.py F5). The parent left that measured at both
ends and named the oddity it has to explain as the LOSS being
non-monotone along the walk -- worse at one freshening, better at two.
This rig asks whether that is the right object at all, and if it is not,
prints the anatomy of the one that is.

THE NAMED CLASS (imported verbatim)
-----------------------------------
Cover, streams, policies, losses, moves, quotient, the stall object and
the landscape evaluator are the parents' (explore_scale_clock.py,
explore_stall_tie.py, explore_stall_assembly.py,
explore_shift_telescope.py, explore_pinned_telescope.py,
explore_pinned_composite.py). UNRESOURCED throughout: drawdown inert,
100 policies, counted window starting at step 8, quotient by counted
trace, cure neighbours, lexicographic deficit. Patience axis 0, 1, 2, 3,
INF, where 0 reads the current image and INF refuses the reference.

WHOSE VOCABULARY THIS IS WRITTEN IN
-----------------------------------
The commit loop's, and deliberately not the quotient's. The parent
settled that the object is ONE member and its cells, so every question
below is about a single run's commit loop -- which candidates it had,
which it took, and what cell it ended the step in. The one place the
quotient still speaks is the definition of a STALL, and that is exactly
where the first finding lives. TRANSPLANT, flagged: nothing is imported
from the diagonal shift telescope. Lemma T re-indexes both coordinates
and refines neither reference; the pinned walk refines ONE reference and
re-indexes nothing, so it is not that lemma with a coordinate missing --
it is a different move, and an intuition carried over from the delay is
carried over from a move this walk does not contain.

HAND-ATTACK (fixed before the engine; the design follows it)
------------------------------------------------------------
Pinned chain: pc = 0, so at step n the chain reference is the CURRENT
image J[n] and only the tree coordinate moves. Write R_j for the run of
(st, ss, j, 0); at step n it reads ref_t = J[n-j] and ref_c = J[n].

F-A SAME-STEP REFINEMENT, NOT A RE-INDEXING. At every step n, R_{j-1}
and R_j read the SAME chain reference, and R_{j-1}'s tree reference
J[n-j+1] sits inside R_j's J[n-j]. So the pinned walk is a totally
ordered chain of runs differing in ONE input, terminating at the doubly
pinned (st, ss, 0, 0).

F-B CANDIDATES ARE MONOTONE FROM A COMMON CELL. The tree candidate is
UNIQUE -- the two children meet only at the mediant, so a reference
strictly inside one is outside the other -- and monotone: a child
containing ref_t contains every reference inside ref_t. chain_kmax is
monotone the same way. From a common cell a fresher reference never
removes a candidate.

F-C THE RACE IS THE ONLY OBSTRUCTION. From a T cell (l,r) the children
are (l,v) and (v,r) while the chain candidate S_k(v) STRADDLES v, so it
contains neither child and neither contains it. The two candidates are
incomparable, which is the whole reason a preference can cost anything;
this is the decision lemma (explore_stall_unresourced.py) read as a
statement about freshening.

D1 THE LOSS NON-MONOTONICITY IS A TAUTOLOGY, NOT A PHENOMENON. A stall
is a class every one of whose cure-neighbour classes has rank at least
its own (SC.qstalls), and unresourced the rank IS the loss order
(SC.cmp_comp with a zero clock component). The once-freshened member
sits one pt-down move from the stall's own member, so its class is a
cure neighbour and L(m-1) >= L(m) is FORCED; the distance-two escape is
by definition strictly improving, so L(m-2) < L(m). The loss profile is
therefore non-monotone BY DEFINITION of a stall with escape radius two,
and no mechanism explains it because none is needed.

D2 WHAT SURVIVES AS ODD IS THE NESTING. Pointwise nesting is not a rank
statement and stallhood constrains it not at all. The object to derive:
C_{m-1}(n) is not contained in C_m(n) at some counted n, while
C_{m-2}(n) is contained in C_m(n) at every counted n.

D3 MECHANISM CANDIDATE -- THE SPENT MEDIANT. By F-B a single step from a
COMMON cell can only refine further, so it nests. Non-nesting therefore
requires the runs to have diverged at an earlier step, and then the only
shape available is that the STALER run ends the step strictly deeper.
The pin is what makes that possible: with pc = 0 the chain reference is
as deep as the stream offers, so the straddle index reachable around a
mediant is as large as the cover allows, while a tree move SPENDS a
mediant, replacing v by the finer mediant of a child around which the
chain may not climb as far. The fresher run's extra tree move can cost
more than it buys, and the cost is paid on the chain engine. Under a
chain-preferring style pair -- which two of the three stalls carry --
the tree move is taken only when the chain is exhausted, so it is
exactly a mediant spend.

PREDICTIONS, fixed before the engine ran
----------------------------------------
C0 [positive control, run first] The three squaring-map specimens
   reproduce as singleton stalls at patiences (3,0), (3,0), (2,0); the
   once-freshened member's class is distinct from the stall's and
   neither nests pointwise nor improves; the twice-freshened member's
   class nests and improves. A miss means the population is not the
   parents' and no verdict below is read (K1).
A1 [the tautology, hard] At each stall the once-freshened member's
   class is a cure neighbour of the stall's class in the quotient's own
   neighbour map, and its rank is at least the stall's; the
   twice-freshened class's rank is strictly less. Verified against the
   evaluator's own neighbour map and ranks, not re-derived here. A
   failure is K2 and D1 is wrong.
A2 [the loss profile down to the floor] The exact loss at every
   patience on the walk from the stall's own to 0, printed as a
   profile. GUESS, marked as a guess: the profile is strictly worse at
   the first step rather than tied -- the once-freshened class is
   distinct, and a tie would make the stall a measurement tie, which
   the corpus's tie thread would already own.
A3 [where the nesting breaks] Per stall, the first counted step at
   which the once-freshened run's cell is not contained in the stall
   run's, the two cells' kinds (T or S), their ranks, and the
   containment relation between them. GUESS: at every stall the STALL
   run's cell is strictly contained in the once-freshened run's -- the
   staler run ends that step deeper (K3 if the two are incomparable
   anywhere).
A4 [the spent mediant] At that step, the full commit-loop route of both
   runs: the move types taken in order, the straddle indices reached,
   and whether both candidates were available at each iteration. GUESS:
   the fresher run takes a tree move the staler run does not, and after
   it the staler run reaches a strictly larger straddle index at that
   step than the fresher run reaches anywhere in it.
A5 [is the walk a chain of nestings] For every ordered pair on the
   freshening walk and every counted step, whether one cell sits inside
   the other. GUESS: the walk is NOT totally ordered by nesting -- the
   twice-freshened run does not nest inside the once-freshened one
   either, so the two-step landing is not a composition of two
   nestings and the escape is genuinely a two-step object (K4 if it is
   a chain, which would decompose the owe rather than break it).
A6 [does the shape reach the residue] Over the 420 doubling tree-side
   classes that one freshening cannot cure, take the witness member and
   walk the parent records as the two-step escape, and record: does the
   intermediate class nest, does it improve, and at the first counted
   step where it fails to nest, is the START class's cell strictly
   inside the intermediate's? GUESS: the intermediate fails to nest in
   a strict majority, and where it fails the start's cell is strictly
   inside in a strict majority -- A3's shape reaching past the
   specimens.

FOLLOW-UP SLATE (frozen after E0-E5's first print and before the
amended run; no prediction, control or kill above was touched)
----------------------------------------------------------------
K3 fired at all three specimens and over all 420 residue classes: the
two cells at the break are INCOMPARABLE everywhere and the staler run is
never the deeper one, so D3's stated form is dead. What E2 printed
instead is that the freshened run is far deeper in RANK (52 against 12,
46 against 13) with a tiny cell STRADDLING an endpoint of the stall's,
and what E3 printed is that at the two census stalls the break step
carries no commit-loop iteration at all in either run -- the break is
inherited whole from before the counted window. And E4 printed a shape
nobody asked for: nesting into the start is not monotone along the walk
but it is not arbitrary either, turning on at one index and staying on.
Three questions follow, and none was asked above.
B1 [THE SUFFIX LAW] Over the parents' census scope (horizons 9, 10, 12,
   16; maps identity and doubling), for every present-pinned member of
   every off-bottom finite-loss class with NO shiftable member -- the
   pinned residue, which is the telescope's complement and the scope
   every count below is stated at -- walk the freshening move and
   record at each index whether the landing class nests pointwise into
   the START class. GUESS: the indicator is a SUFFIX at every member --
   once it turns on it never turns off. Observable: the count of members
   whose indicator is not a suffix, and the first counter-example.
B2 [THE FLOOR] Every walk ends at the doubly pinned member (st, ss, 0,
   0). GUESS: its class nests pointwise into the start class at every
   member. Observable: the count of members where the floor fails to
   nest.
B3 [WHERE THE SUFFIX STARTS] The distribution of the first nesting index
   over every walk. GUESS: it never exceeds 2, which restates the
   corpus's exists-form open edge as a statement about EVERY member's
   walk rather than some member's.
K5 The indicator is not a suffix at some member. B1 is false and the law
   is about where the suffix starts rather than that there is one.
K6 The floor fails to nest at some member. B2 is false and the walk has
   no proved floor.
K7 The first nesting index exceeds 2 at some member. B3 is false; the
   two-step statement stays exists-over-members and the suffix law is
   the weaker object.

SECOND FOLLOW-UP SLATE (frozen after E6's first print and before the
third run; nothing above was touched)
----------------------------------------------------------------
K5 and K7 both fired -- the indicator is not a suffix (466 members) and
the first nesting index reaches 3 -- and B2 held with ZERO exceptions
over 19,117 members. So the universal object is not the second step at
all: it is the FLOOR. One question follows.
C1 [DOES THE FLOOR IMPROVE] For every present-pinned member, whether the
   doubly pinned floor's class is the start class, and where it is not,
   whether its loss is strictly smaller. This is a DERIVATION and not a
   guess, so it is wired hard: the quotient's signature is the tuple of
   counted INTERVALS (explore_stall_tie.py run_pol), so distinct classes
   differ at some counted interval; pointwise nesting makes that
   interval a subset of the start's, and two nested intervals that
   differ have strictly different lengths -- so the product is strictly
   smaller. Nothing about cells or ranks enters, and the shift
   telescope's CT3 equal-length clause is not needed here. Observable:
   the counts of (floor in the start class) and (distinct and strictly
   improving), and any member in neither bucket.
K8 A member whose floor class is distinct from the start's and does not
   strictly improve. The derivation above is wrong in this cover and
   nesting does not force improvement along the pinned walk.

THIRD FOLLOW-UP SLATE (frozen after E7's first print and before the
fourth run; nothing above was touched)
----------------------------------------------------------------
C1 held at 19,117 of 19,117, so the floor lemma is the universal
statement and the two-step claim is not. One question decides whether it
SUBSUMES that claim or merely stands beside it, and it is one counter on
E5's existing witness.
D1' [IS THE TWO-STEP WITNESS THE FLOOR] Over the 420 doubling tree-side
    classes one freshening cannot cure, the patience of the witness
    member E5 already selects. The twice-freshened landing is the floor
    exactly when that patience is 2. GUESS: 420 of 420 -- the corpus's
    two-step statement is the floor lemma restricted to the members that
    happen to sit two steps above the floor, and nothing about TWO is
    load-bearing in it.
K9 Any witness at patience 3. The two-step landing is then a distinct
    object from the floor at that class, the floor lemma stands beside
    the open edge rather than subsuming it, and the distance-two claim
    keeps its own content.

FOURTH FOLLOW-UP SLATE (frozen after the fourth run and before the
fifth; nothing above was touched)
----------------------------------------------------------------
The floor lemma as measured is scoped to the PINNED RESIDUE, because
that is the population every leg above iterates. Whether the residue is
load-bearing in it is one predicate away and nobody has asked.
E1' [THE UNSCOPED FLOOR] Over the same census scope, for EVERY
    off-bottom finite-loss class and every member of it -- shiftable
    classes included, and members with both patiences positive or
    infinite included -- whether the class of (st, ss, 0, 0) at that
    member's style pair nests pointwise into the member's class. GUESS,
    marked as a guess: it nests everywhere, and the pinned residue was
    incidental to the lemma rather than its hypothesis. Observable: the
    counts of members where it nests and where it does not, split by
    map, with the first failure printed.
K10 Any class where the doubly pinned run fails to nest. The residue IS
    load-bearing, the lemma keeps the scope the fifth run's fix gave it,
    and the failure's anatomy is the next thing to read.

KILL CRITERIA (observables; the meaning is weighed after the run)
----------------------------------------------------------------
K1 Any C0 control misses. The population is not the parents' and
   nothing below is a verdict.
K2 At any stall the once-freshened class is absent from the quotient's
   cure-neighbour set of the stall class, or its rank is below the
   stall's. D1 is wrong: the loss non-monotonicity is an observation
   after all and the parent's framing stands.
K3 At any stall the two cells at the first non-nesting counted step are
   INCOMPARABLE. "The staler run ends deeper" is false there, D3's
   stated form does not carry that specimen, and the rig prints the
   routes rather than a verdict.
K4 The freshening walk IS totally ordered by nesting at all three
   stalls. The two-step landing decomposes into two one-step nestings
   and the owe is cheaper than the parent stated -- a smaller owe, not
   a failure.

ENGINE
------
E0 the control (C0).
E1 the cure-neighbour and rank check, and the loss profile (A1, A2).
E2 the first non-nesting counted step and its two cells (A3).
E3 the commit-loop routes at that step (A4).
E4 the pairwise nesting lattice over the freshening walk (A5).
E5 the shape over the 420 (A6).
E6 the suffix law, the floor and the first nesting index over the
   census scope (B1, B2, B3).
E7 whether the floor improves wherever it is a distinct class (C1).
E8 the unscoped floor over every off-bottom class (E1').
   E5 also carries D1', the witness patience over the 420.
Exact big-integer arithmetic for every verdict; floating point only in
printed logs. Sequential; estimated run under a minute, the E5 census
the driver; memory trivial (no BLAS import); exit nonzero on any check
failure.

FINDINGS (entered after the run; ALL CHECKS PASS, exit 0, 8.5 s, 16.0 MB
peak under the memory watch)
----------------------------------------------------------------
F1 THE LOSS NON-MONOTONICITY IS A TAUTOLOGY, AND THE PARENT'S NAMED
   ODDITY IS NOT ONE. D1 holds mechanically at all three stalls: the
   once-freshened class sits in the quotient's own cure-neighbour set of
   the stall class with CLASS rank 12 >= 11, 14 >= 12 and 4 >= 3, and the
   twice-freshened class ranks 3, 1 and 0 against 11, 12 and 3. So "the
   loss is worse at one freshening and better at two" is entailed by the
   definition of a stall with escape radius two, at every stall there
   will ever be, and it needs no mechanism. The profiles are strictly
   worse at the first step rather than tied everywhere (A2 held), so the
   stalls are not measurement ties.
F2 THE MECHANISM GUESS IS DEAD, AND UNIFORMLY. K3 fires at 3 of 3
   specimens and the census leg fires it 420 times more: at the first
   counted step where the once-freshened run leaves the stall's cell the
   two cells are INCOMPARABLE, never ordered, at every one of the three
   stalls and at all 420 residue classes (start strictly deeper 0,
   incomparable 420). The staler run is never the deeper one, so D3's
   "the fresher run pays for a spent mediant" is false as stated. What
   the print shows instead: the freshened run is far deeper in CELL rank
   at that step (52 against 12, 46 against 13 -- cover depth, not the
   class ranks of F1) with a tiny cell straddling
   an ENDPOINT of the stall's, so the break is a boundary crossing and
   not a depth deficit.
F3 AT THE TWO CENSUS STALLS THE BREAK STEP CARRIES NO MOVE AT ALL. E3's
   routes are empty in BOTH runs at the break: the commit loop iterates
   zero times, and the cells that fail to nest are carried in whole from
   before the counted window. So no argument about that step's race can
   reach the break, and the divergence the counted window reports was
   already finished when the window opened. (At the designed specimen
   the step is not empty, and it is the STALL that moves further --
   tree, tree, chain at k=2 against the freshened run's single tree.)
F4 THE FRESHENING WALK IS NOT A CHAIN OF NESTINGS, AND NESTING INTO THE
   START IS NOT MONOTONE ALONG IT. A5 held at all three stalls: at the
   two census stalls pt=1 nests into pt=3 but not into pt=2, and pt=2
   nests into nothing. Over the census the failure of monotonicity is
   two-sided -- B1's suffix guess is FALSE, 466 members carrying an
   indicator that turns on, off and on again (first counter-example
   dbl h=9 (0,0,3,0), True/False/True) -- and B3's guess is false too,
   the first nesting index reaching 3. K5 and K7 both fire.
F5 THE FLOOR LEMMA, AND IT IS THE UNIVERSAL STATEMENT THE OPEN EDGE WAS
   LOOKING FOR. Over 19,117 present-pinned members of the pinned
   residue at census scope -- off-bottom, finite loss, no shiftable
   member -- the
   DOUBLY PINNED member of the same style pair -- both patiences 0, the
   end of the walk -- lands in a class that nests pointwise into the
   start class at 19,117 of 19,117 -- which is also why no walk fails to
   nest anywhere, the floor being every walk's last step. And that class
   is distinct from the start at 19,117 of 19,117 and
   strictly improves at 19,117 of 19,117: K8 misses, and the improving
   half is DERIVED rather than measured -- the quotient's signature is
   the tuple of counted intervals, so distinct classes differ at one of
   them, and a nested interval that differs is strictly shorter, making
   the product strictly smaller. Half of this rule is therefore proved
   from the other half.
F6 THE FLOOR LEMMA SUBSUMES THE OPEN EDGE RATHER THAN STANDING BESIDE
   IT. K9 misses: E5 takes the FIRST witness it finds at each of the 420
   classes one freshening cannot cure, and that witness sits at patience
   2 at 420 of 420 -- so a patience-2 witness exists everywhere and the
   "second freshening" the corpus's statement names can always be taken
   to be the walk to the floor. Whether some class ALSO carries a
   patience-3 witness is not asked here and would not change that.

F7 THE PINNED RESIDUE WAS INCIDENTAL, AND THE LEMMA IS UNSCOPED. K10
   misses: over the same census scope, at EVERY off-bottom finite-loss
   class and every member of it -- shiftable classes included, members
   with both patiences positive or infinite included -- the class of
   (st, ss, 0, 0) at that member's own style pair nests pointwise into
   the member's class, at 53,988 of 53,988 doubling members and 48,104
   of 48,104 identity members. NONE of the 102,092 is trivial: a member
   already doubly pinned sits at rank 0, which the margin table excludes,
   so every one of them is a statement about two distinct classes. So the
   residue, the freshening walk and the pinned coordinate are all
   scaffolding: what is true is that reading the PRESENT at both
   coordinates commits inside what any patience pair of the same style
   commits to, at every counted step.

THE VERDICT. The aim asked for a mechanism explaining a non-monotonicity,
and there are two objects under that name with opposite verdicts. The
LOSS non-monotonicity is a tautology (F1) -- entailed by stallhood plus a
distance-two escape, so a mechanism for it would explain a definition.
The NESTING non-monotonicity is real, and it is worse than the parent
knew: nesting into the start turns on and off along the walk (F4), so
there is no threshold and no suffix to find, and the guessed mechanism
for the break is refuted uniformly at 423 of 423 places it was checked
(F2), with the break at two of the three stalls carrying no commit-loop
iteration to argue about at all (F3). What replaces the two-step
statement is a stronger and simpler one that the walk's ENDPOINT carries:
from every present-pinned member, freshening to the doubly pinned member
lands in a distinct class that nests pointwise into the start and
strictly improves (F5), exhaustively at 19,117 members with the improving
half proved from the nesting half -- and the corpus's two-step claim is
exactly this lemma at the members two steps above the floor (F6). So the
derivation the reader corpus owes is no longer a two-move composite about
which step does what. It is ONE statement about the doubly pinned run:
that reading the present at both coordinates commits inside what any
staler pair of the same style commits to, at every counted step -- and
that statement needs neither the residue nor the walk that found it,
holding at 102,092 of 102,092 members of every off-bottom class (F7). It
is the pointwise, per-style form of the bottom lemma, whose greedy
optimum is a statement about the LOSS at one style pair; this one is
about the CELLS at every style pair at once.

Run record. ONE engine, four runs. The first ran E0-E5; K3 fired at all
three specimens and at every one of the 420, and the follow-up slate B1,
B2, B3 was frozen before the second run with no prediction, control or
kill touched. The second ran E6; K5 and K7 fired and B2 held clean, and
the second follow-up slate C1 was frozen before the third. The third ran
E7 and also re-scoped B1, B2 and B3 from assertions to reports -- they
are GUESSES and wiring a guess hard is the parent telescope's own
recorded trap -- so K5 and K7 report as the verdicts they are rather than
as rig failures; no count changed. The fourth added D1', one counter over
E5's existing witness, under a slate frozen before it ran. A FIFTH run
added E8 under a slate frozen before it, asking whether the pinned
residue is load-bearing in the floor lemma at all; it is not, and the
same run split the trivial members out of E8's count before that count
was ever read, which found the trivial bucket empty by construction. No
prediction, control or finding above F6 was touched at any point. Final
run ALL CHECKS PASS, exit 0, 13.3 s.
"""

import sys
from fractions import Fraction

import explore_scale_clock as SC
import explore_stall_assembly as SA
import explore_shift_telescope as TS
import explore_stall_maprate as MR
import explore_pinned_telescope as PT

FAILURES = []
K3_FIRED = []

def check(name, ok):
    print("  [%s] %s" % ("PASS" if ok else "FAIL", name))
    if not ok:
        FAILURES.append(name)

EXPECT_PATIENCE = {"census-2313..": (3, 0),
                   "census-3212..": (3, 0),
                   "designed-16": (2, 0)}

def fmt4(p):
    return "(%d,%d,%s,%s)" % (
        p[0], p[1],
        "INF" if p[2] is None else str(p[2]),
        "INF" if p[3] is None else str(p[3]))

def cell_kind(C):
    return "T" if C[0] == "T" else "S%d" % C[5]

def fmt_iv(iv):
    return "%d/%d..%d/%d" % (iv[0][0], iv[0][1], iv[1][0], iv[1][1])

# ----------------------------------------------------------------- #
# the instrumented reader: SC.run_reader verbatim, keeping the full
# cell at every step and the commit-loop route at every step
# ----------------------------------------------------------------- #

def run_traced(J_list, policy, horizon):
    """Returns (cells, routes): cells[n] the committed cell object at
    step n, routes[n] the list of (taken, kind after the move, both
    candidates available) over the commit loop's iterations."""
    s_t, s_s, pt, pc = policy[:4]
    C = SC.ROOT
    cells, routes = [], []
    for n in range(horizon):
        J = J_list[n]
        ref_t = J_list[n - pt] if pt is not None and n - pt >= 0 else None
        ref_c = J_list[n - pc] if pc is not None and n - pc >= 0 else None
        route = []
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
            both = cand_tree is not None and cand_chain is not None
            if cand_chain is not None and (cand_tree is None
                                           or prefer_chain):
                C = cand_chain
                route.append(("chain", cell_kind(C), both))
            else:
                C = cand_tree
                route.append(("tree", cell_kind(C), both))
        clo, chi = SC.interval(C)
        if SC.lt(J[0], clo) or SC.lt(chi, J[1]):
            raise AssertionError("commitment lost the image")
        cells.append(C)
        routes.append(route)
    return cells, routes

def relation(a, b):
    """Containment of interval a against interval b."""
    ab = PT.inside(a, b)
    ba = PT.inside(b, a)
    if ab and ba:
        return "equal"
    if ab:
        return "a-inside-b"
    if ba:
        return "b-inside-a"
    return "incomparable"

def walk_members(p0):
    """The freshening walk from a pinned-chain member down to 0."""
    out, cur = [p0], p0
    while cur[2] is not None and cur[2] > 0:
        cur = (cur[0], cur[1], cur[2] - 1, cur[3], cur[4])
        out.append(cur)
    return out

def loss_of(ev, sig):
    q = ev["qloss"][sig][1]
    return None if q[2] else Fraction(q[0], q[1])

def first_break(J, a, b, horizon):
    """First counted step at which a's cell is not inside b's."""
    ca = TS.counted_cells(J, a, horizon)
    cb = TS.counted_cells(J, b, horizon)
    for i, (x, y) in enumerate(zip(ca, cb)):
        if not TS.nested_or_equal(x[:2], y[:2]):
            return SC.N0 + i
    return None

# ----------------------------------------------------------------- #
# E0: the control
# ----------------------------------------------------------------- #

def e0_control():
    print("\nE0  THE CONTROL (the parents' stalls, one and two steps)")
    seen = {}
    for tag, digs, horizon in TS.SQ_SPECIMENS:
        ev = SA.evaluate(list(digs), "sq", horizon)
        sig_of = {p: s for s, ps in ev["mem"].items() for p in ps}
        if not ev["stalls"]:
            check("%s reproduces as a stall" % tag, False)
            continue
        for s in ev["stalls"]:
            mem = ev["mem"][s]
            pats = sorted({(p[2], p[3]) for p in mem})
            check("%s singleton stall at patience %s"
                  % (tag, EXPECT_PATIENCE[tag]),
                  len(mem) == 1 and pats == [EXPECT_PATIENCE[tag]])
            p0 = sorted(mem, key=SC.pol_key)[0]
            wk = walk_members(p0)
            if len(wk) < 3:
                check("%s has two freshenings to spend" % tag, False)
                continue
            cx = TS.counted_cells(ev["J"], p0, horizon)
            Lx = loss_of(ev, s)
            z, w = sig_of[wk[1]], sig_of[wk[2]]
            cz = TS.counted_cells(ev["J"], wk[1], horizon)
            cw = TS.counted_cells(ev["J"], wk[2], horizon)
            Lz, Lw = loss_of(ev, z), loss_of(ev, w)
            check("%s: one freshening leaves the class and neither "
                  "nests nor improves" % tag,
                  z != s and not TS.nests_pointwise(cz, cx)
                  and not (Lz is not None and Lz < Lx))
            check("%s: two freshenings nest and improve" % tag,
                  w not in (s, z) and TS.nests_pointwise(cw, cx)
                  and Lw is not None and Lw < Lx)
            seen[tag] = (ev, horizon, s, p0, wk, sig_of)
    return seen

# ----------------------------------------------------------------- #
# E1: the cure-neighbour check and the loss profile
# ----------------------------------------------------------------- #

def e1_profile(seen):
    print("\nE1  THE TAUTOLOGY CHECK AND THE LOSS PROFILE")
    for tag in sorted(seen):
        ev, horizon, s, p0, wk, sig_of = seen[tag]
        z, w = sig_of[wk[1]], sig_of[wk[2]]
        check("%s: the once-freshened class is a cure neighbour of "
              "the stall class" % tag, z in ev["nbrs"][s])
        check("%s: its rank is at least the stall's (%d >= %d)"
              % (tag, ev["qranks"][z], ev["qranks"][s]),
              ev["qranks"][z] >= ev["qranks"][s])
        check("%s: the twice-freshened class ranks strictly below "
              "(%d < %d)" % (tag, ev["qranks"][w], ev["qranks"][s]),
              ev["qranks"][w] < ev["qranks"][s])
        parts = []
        for p in wk:
            L = loss_of(ev, sig_of[p])
            parts.append("pt=%s %s" % (p[2], "INF" if L is None
                                       else "%.6e" % float(L)))
        print("    %s: %s" % (tag, " | ".join(parts)))
        L0, L1 = loss_of(ev, s), loss_of(ev, z)
        print("      first step %s"
              % ("strictly worse" if L1 > L0 else
                 ("tied" if L1 == L0 else "BETTER")))

# ----------------------------------------------------------------- #
# E2/E3: the first non-nesting step and the routes there
# ----------------------------------------------------------------- #

def e2_break(seen):
    print("\nE2  WHERE THE NESTING BREAKS, AND WHICH RUN IS DEEPER")
    out = {}
    for tag in sorted(seen):
        ev, horizon, s, p0, wk, sig_of = seen[tag]
        n = first_break(ev["J"], wk[1], p0, horizon)
        if n is None:
            check("%s: the once-freshened run breaks nesting "
                  "somewhere counted" % tag, False)
            continue
        cs, rs = run_traced(ev["J"], p0, horizon)
        cf, rf = run_traced(ev["J"], wk[1], horizon)
        rel = relation(SC.interval(cf[n]), SC.interval(cs[n]))
        print("    %s: first break at counted step %d" % (tag, n))
        print("      stall     %s cell %-4s rank %2d  %s"
              % (fmt4(p0), cell_kind(cs[n]), SC.rank(cs[n]),
                 fmt_iv(SC.interval(cs[n]))))
        print("      freshened %s cell %-4s rank %2d  %s"
              % (fmt4(wk[1]), cell_kind(cf[n]), SC.rank(cf[n]),
                 fmt_iv(SC.interval(cf[n]))))
        print("      relation (freshened vs stall): %s" % rel)
        if rel != "b-inside-a":
            K3_FIRED.append(tag)
        out[tag] = (n, cs, rs, cf, rf)
    print("  K3 fires at %d of %d specimens: the two cells at the break "
          "are not ordered, so the staler run is not the deeper one and "
          "D3's stated form is dead (%s)"
          % (len(K3_FIRED), len(seen), ", ".join(K3_FIRED) or "none"))
    return out

def e3_routes(seen, brk):
    print("\nE3  THE COMMIT-LOOP ROUTES AT THE BREAK")
    for tag in sorted(seen):
        if tag not in brk:
            continue
        n, cs, rs, cf, rf = brk[tag]
        for lbl, rt in (("stall    ", rs[n]), ("freshened", rf[n])):
            body = " -> ".join(
                "%s%s%s" % (t, "" if k[0] == "T" else "[k=" + k[1:] + "]",
                            "*" if b else "")
                for t, k, b in rt)
            print("      %s %-14s %s" % (lbl, tag, body or "(no move)"))

        def maxk(rt):
            ks = [int(k[1:]) for _t, k, _b in rt if k[0] == "S"]
            return max(ks) if ks else 0
        ts = sum(1 for t, _k, _b in rs[n] if t == "tree")
        tf = sum(1 for t, _k, _b in rf[n] if t == "tree")
        print("      tree moves: stall %d, freshened %d | largest "
              "straddle index: stall %d, freshened %d"
              % (ts, tf, maxk(rs[n]), maxk(rf[n])))

# ----------------------------------------------------------------- #
# E4: the nesting lattice over the walk
# ----------------------------------------------------------------- #

def e4_lattice(seen):
    print("\nE4  THE NESTING LATTICE OVER THE FRESHENING WALK")
    chain_at = []
    for tag in sorted(seen):
        ev, horizon, s, p0, wk, sig_of = seen[tag]
        cells = {p: TS.counted_cells(ev["J"], p, horizon) for p in wk}
        print("    %s  columns = the run nested INTO, pt %s"
              % (tag, " ".join(str(b[2]) for b in wk)))
        for a in wk:
            row = ["." if a == b else
                   ("Y" if TS.nests_pointwise(cells[a], cells[b])
                    else "-")
                   for b in wk]
            print("      pt=%s  %s" % (a[2], " ".join(row)))
        consec = all(TS.nests_pointwise(cells[wk[i + 1]], cells[wk[i]])
                     for i in range(len(wk) - 1))
        chain_at.append(consec)
        print("      each step nests into the previous: %s"
              % ("YES" if consec else "no"))
    check("the freshening walk is NOT a chain of nestings at all "
          "three stalls", not all(chain_at))

# ----------------------------------------------------------------- #
# E5: the shape over the 420
# ----------------------------------------------------------------- #

def e5_residue():
    print("\nE5  THE SHAPE OVER THE 420 (doubling, tree side)")
    tot = 0
    inter_nests = inter_improves = 0
    deeper = incomp = nobreak = 0
    wit_pat = {}
    for horizon in PT.CENSUS_HORIZONS:
        for _wname, digs in MR.census_pool(horizon):
            ev = SA.evaluate(digs, "dbl", horizon)
            sig_of = {p: s for s, ps in ev["mem"].items() for p in ps}
            cellcache = {}
            for s in ev["marg"]:
                _nt, sh, _fz, _imp, _v, _ptw = TS.class_stats(
                    ev, horizon, s, cellcache, sig_of)
                if sh:
                    continue
                walks = PT.walk_class(ev, horizon, s, cellcache, sig_of)
                rec = walks["tree"]
                if rec is None or rec["best"] is not None:
                    continue
                cx = cellcache[s]
                Lx = Fraction(ev["qloss"][s][1][0],
                              ev["qloss"][s][1][1])
                wit = None
                for p in ev["mem"][s]:
                    if not PT.is_present_pinned(p) or \
                            PT.side_of(p) != "tree":
                        continue
                    q1 = PT.freshen(p)
                    z = sig_of[q1]
                    if z == s or not PT.is_present_pinned(q1):
                        continue
                    q2 = PT.freshen(q1)
                    w = sig_of[q2]
                    if w in (s, z) or ev["qloss"][w][1][2]:
                        continue
                    if w not in cellcache:
                        rep = sorted(ev["mem"][w], key=SC.pol_key)[0]
                        cellcache[w] = TS.counted_cells(ev["J"], rep,
                                                        horizon)
                    Lw = Fraction(ev["qloss"][w][1][0],
                                  ev["qloss"][w][1][1])
                    if TS.nests_pointwise(cellcache[w], cx) and Lw < Lx:
                        wit = (p, q1, z)
                        break
                if wit is None:
                    continue
                tot += 1
                p, q1, z = wit
                wit_pat[p[2]] = wit_pat.get(p[2], 0) + 1
                if z not in cellcache:
                    rep = sorted(ev["mem"][z], key=SC.pol_key)[0]
                    cellcache[z] = TS.counted_cells(ev["J"], rep,
                                                    horizon)
                nests = TS.nests_pointwise(cellcache[z], cx)
                inter_nests += nests
                Lz = ev["qloss"][z][1]
                inter_improves += ((not Lz[2])
                                   and Fraction(Lz[0], Lz[1]) < Lx)
                if nests:
                    nobreak += 1
                    continue
                n = first_break(ev["J"], q1, p, horizon)
                if n is None:
                    nobreak += 1
                    continue
                cs, _rs = run_traced(ev["J"], p, horizon)
                cf, _rf = run_traced(ev["J"], q1, horizon)
                rel = relation(SC.interval(cf[n]), SC.interval(cs[n]))
                if rel == "b-inside-a":
                    deeper += 1
                else:
                    incomp += 1
        print("  h=%-2d dbl done" % horizon)
    print("  witnessed classes %d | intermediate nests %d, improves %d"
          % (tot, inter_nests, inter_improves))
    print("  of the non-nesting intermediates: start strictly deeper "
          "%d, incomparable %d (no counted break %d)"
          % (deeper, incomp, nobreak))
    print("  witness patiences %s -- the twice-freshened landing is the "
          "FLOOR exactly at patience 2, so K9 %s"
          % (sorted(wit_pat.items()),
             "FIRES" if any(k != 2 for k in wit_pat) else "misses"))
    check("the residue reproduces 420 witnessed classes (%d)" % tot,
          tot == 420)

# ----------------------------------------------------------------- #
# E6: the suffix law, the floor, and where the suffix starts
# ----------------------------------------------------------------- #

def e6_suffix():
    print("\nE6  THE SUFFIX LAW OVER THE CENSUS SCOPE")
    members = 0
    nonsuffix = []
    floor_fail = []
    firsts = {}
    never = 0
    floor_same = floor_better = 0
    floor_other = []
    for horizon in PT.CENSUS_HORIZONS:
        for mp in PT.CENSUS_MAPS:
            for _wname, digs in MR.census_pool(horizon):
                ev = SA.evaluate(digs, mp, horizon)
                sig_of = {p: s for s, ps in ev["mem"].items()
                          for p in ps}
                cellcache = {}

                def cells(sig):
                    if sig not in cellcache:
                        rep = sorted(ev["mem"][sig], key=SC.pol_key)[0]
                        cellcache[sig] = TS.counted_cells(
                            ev["J"], rep, horizon)
                    return cellcache[sig]

                for s in ev["marg"]:
                    _nt, sh, _fz, _imp, _v, _ptw = TS.class_stats(
                        ev, horizon, s, cellcache, sig_of)
                    if sh:
                        continue
                    cx = cells(s)
                    for p in ev["mem"][s]:
                        if not PT.is_present_pinned(p):
                            continue
                        members += 1
                        vec, cur = [], p
                        while PT.is_present_pinned(cur):
                            cur = PT.freshen(cur)
                            vec.append(TS.nests_pointwise(
                                cells(sig_of[cur]), cx))
                        if not vec:
                            continue
                        first = next((i for i, b in enumerate(vec) if b),
                                     None)
                        if first is None:
                            never += 1
                        else:
                            firsts[first + 1] = firsts.get(first + 1,
                                                           0) + 1
                            if not all(vec[first:]):
                                nonsuffix.append(
                                    (mp, horizon, p, tuple(vec)))
                        if not vec[-1]:
                            floor_fail.append((mp, horizon, p,
                                               tuple(vec)))
                        fl = sig_of[cur]
                        if fl == s:
                            floor_same += 1
                        elif SC.cmp_lex(ev["qloss"][fl][1],
                                        ev["qloss"][s][1]) < 0:
                            floor_better += 1
                        else:
                            floor_other.append((mp, horizon, p))
        print("  h=%-2d done" % horizon)
    print("  present-pinned members walked %d | walks that never nest %d"
          % (members, never))
    print("  first nesting index histogram %s" % sorted(firsts.items()))
    # B1, B2 and B3 are GUESSES, so their outcomes are REPORTED and
    # never wired as assertions -- the parent telescope's own recorded
    # trap. Only the derivation C1 below and the reproduction controls
    # are hard.
    print("  B1 suffix law: %d members whose indicator is not a suffix"
          " -- K5 %s" % (len(nonsuffix), "FIRES" if nonsuffix else "misses"))
    if nonsuffix:
        print("    first counter-example: %s" % (nonsuffix[0],))
    print("  B2 the floor: %d members where the doubly pinned landing "
          "fails to nest into the start -- K6 %s"
          % (len(floor_fail), "FIRES" if floor_fail else "misses"))
    if floor_fail:
        print("    first failure: %s" % (floor_fail[0],))
    mx = max(firsts) if firsts else None
    print("  B3 first nesting index: max %s -- K7 %s"
          % (mx, "FIRES" if (mx or 0) > 2 else "misses"))
    print("\nE7  DOES THE FLOOR IMPROVE")
    print("  floor lands in the start class %d | distinct and strictly "
          "improving %d | neither %d"
          % (floor_same, floor_better, len(floor_other)))
    check("every distinct floor class strictly improves (%d in "
          "neither bucket)" % len(floor_other), not floor_other)
    if floor_other:
        print("    first exception: %s" % (floor_other[0],))

# ----------------------------------------------------------------- #
# E8: the unscoped floor
# ----------------------------------------------------------------- #

def e8_unscoped():
    print("\nE8  THE FLOOR WITHOUT THE RESIDUE (every off-bottom class)")
    tab = {}
    first_fail = []
    for horizon in PT.CENSUS_HORIZONS:
        for mp in PT.CENSUS_MAPS:
            for _wname, digs in MR.census_pool(horizon):
                ev = SA.evaluate(digs, mp, horizon)
                sig_of = {p: s for s, ps in ev["mem"].items()
                          for p in ps}
                cellcache = {}

                def cells(sig):
                    if sig not in cellcache:
                        rep = sorted(ev["mem"][sig], key=SC.pol_key)[0]
                        cellcache[sig] = TS.counted_cells(
                            ev["J"], rep, horizon)
                    return cellcache[sig]

                for s in ev["marg"]:
                    cx = cells(s)
                    for p in ev["mem"][s]:
                        fl = sig_of[(p[0], p[1], 0, 0, p[4])]
                        triv = fl == s
                        ok = triv or TS.nests_pointwise(cells(fl), cx)
                        rec = tab.setdefault(mp, [0, 0, 0])
                        if triv:
                            rec[2] += 1
                        else:
                            rec[0 if ok else 1] += 1
                        if not ok and len(first_fail) < 3:
                            first_fail.append((mp, horizon, p))
        print("  h=%-2d done" % horizon)
    for mp in sorted(tab):
        ok, bad, triv = tab[mp]
        print("  %-3s: floor nests at %d of %d members whose floor is a "
              "DIFFERENT class (%d more sit in the floor's own class, "
              "where the statement is trivial)" % (mp, ok, ok + bad, triv))
    for f in first_fail:
        print("    failure: %s" % (f,))
    tot_bad = sum(v[1] for v in tab.values())
    print("  E1' guess: the floor nests everywhere -- K10 %s (%d "
          "failures)" % ("FIRES" if tot_bad else "misses", tot_bad))

# ----------------------------------------------------------------- #

def main():
    seen = e0_control()
    if FAILURES:
        print("\nCONTROL FAILED -- no verdicts read")
        print("FAILURES: %s" % FAILURES)
        return 1
    e1_profile(seen)
    brk = e2_break(seen)
    e3_routes(seen, brk)
    e4_lattice(seen)
    e5_residue()
    e6_suffix()
    e8_unscoped()
    if FAILURES:
        print("\nFAILURES: %s" % FAILURES)
        return 1
    print("\nALL CHECKS PASS")
    return 0

if __name__ == "__main__":
    sys.exit(main())
